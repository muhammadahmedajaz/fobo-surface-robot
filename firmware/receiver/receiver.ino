// ===========================================================
// ESP32 RX (ESP-NOW) + 4x IBT-2 motor drivers + PCA9685 servos
// - Uses new ESP32 v3.0+ ledcAttach(pin,freq,res) / ledcWrite(pin,duty)
// - CH0 = steer (X), CH1 = throttle (Y), CH2 = servo vector (left/right)
// - Front servos mirror: front = center + offset, rear = center - offset
// ===========================================================

#include <Arduino.h>
#include <WiFi.h>
#include <esp_now.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// ================== RcFrame + CRC-8 (unchanged) ==================
typedef struct __attribute__((packed)) {
  uint8_t  protoVersion;
  uint8_t  flags;
  uint16_t frameId;
  int16_t  ch[8];
  uint8_t  crc;
} RcFrame;

uint8_t crc8(const uint8_t *data, size_t len) {
  uint8_t crc = 0x00;
  while (len--) {
    crc ^= *data++;
    for (uint8_t i = 0; i < 8; i++) {
      if (crc & 0x80) crc = (crc << 1) ^ 0x07;
      else crc <<= 1;
    }
  }
  return crc;
}

// ================== RC link state (unchanged) ==================
static RcFrame lastFrame;
static int16_t channels[8] = {0};
static volatile bool newFrameFlag = false;
static bool linkActive = false;
static bool failsafeActive = true;
static uint32_t lastRxMs = 0;
static uint16_t lastFrameId = 0;
const uint32_t HARD_FAILSAFE_MS = 300;

// ===== ESP-NOW receive callback (unchanged) =====
void onDataRecv(const esp_now_recv_info_t *info, const uint8_t *incomingData, int len) {
  if (len != sizeof(RcFrame)) return;
  RcFrame f;
  memcpy(&f, incomingData, sizeof(RcFrame));
  uint8_t computed = crc8((uint8_t*)&f, sizeof(RcFrame) - 1);
  if (computed != f.crc) return;

  lastFrame = f;
  for (int i = 0; i < 8; i++) channels[i] = f.ch[i];

  lastRxMs = millis();
  linkActive = true;
  failsafeActive = false;
  lastFrameId = f.frameId;
  newFrameFlag = true;
}

// ===== Failsafe behaviour (unchanged) =====
void applyHardFailsafe() {
  channels[0] = 0;
  channels[1] = -1000;
  channels[2] = 0;
  channels[3] = 0;
  for (int i = 4; i < 8; i++) channels[i] = 0;
  failsafeActive = true;
}

// ===== Public RC API (unchanged) =====
bool rcInit() {
  WiFi.mode(WIFI_STA);
  delay(50);
  if (esp_now_init() != ESP_OK) {
    Serial.println("rcInit: Error initializing ESP-NOW");
    return false;
  }
  esp_now_register_recv_cb(onDataRecv);
  applyHardFailsafe();
  linkActive = false;
  Serial.println("rcInit: ESP-NOW RX initialized");
  return true;
}
void rcUpdate() {
  uint32_t now = millis();
  if (linkActive && (now - lastRxMs > HARD_FAILSAFE_MS)) {
    Serial.println("rcUpdate: HARD FAILSAFE triggered (link lost)");
    applyHardFailsafe();
    linkActive = false;
  }
}
bool rcLinkActive() { return linkActive; }
bool rcFailsafeActive() { return failsafeActive; }
int16_t rcGetChannel(int ch) { if (ch < 0 || ch > 7) return 0; return channels[ch]; }
uint16_t rcGetLastFrameId() { return lastFrameId; }

// ====================================================
// Motor pin definitions (as you provided)
// Treat each pair as RPWM (forward) and LPWM (reverse)
// ====================================================
#define M1_PWM 25
#define M1_DIR 26
#define M2_PWM 27
#define M2_DIR 14
#define M3_PWM 23
#define M3_DIR 22
#define M4_PWM 21
#define M4_DIR 17

const int motor_pwm_pins[4][2] = {
  { M1_PWM, M1_DIR }, // motor0
  { M2_PWM, M2_DIR }, // motor1
  { M3_PWM, M3_DIR }, // motor2
  { M4_PWM, M4_DIR }  // motor3
};

// LEDC parameters (safe for WROOM-32)
const int LEDC_FREQ = 10000; // Hz
const int LEDC_RES  = 10;    // bits => 0..1023
const int LEDC_MAX_DUTY = (1 << LEDC_RES) - 1; // 1023

// joystick deadband (in -1000..1000)
const int JOYSTICK_DEAD = 50;

// attach motor pins to PWM using v3.0+ API
void motorsAttachAll() {
  for (int i = 0; i < 4; ++i) {
    int p_r = motor_pwm_pins[i][0];
    int p_l = motor_pwm_pins[i][1];
    pinMode(p_r, OUTPUT);
    pinMode(p_l, OUTPUT);
    // attach pins to PWM generator (v3.0+)
    ledcAttach(p_r, LEDC_FREQ, LEDC_RES);
    ledcAttach(p_l, LEDC_FREQ, LEDC_RES);
    ledcWrite(p_r, 0);
    ledcWrite(p_l, 0);
  }
}

// set single motor speed -1000..1000
void motorSetOne(int idx, int speed) {
  speed = constrain(speed, -1000, 1000);
  int p_r = motor_pwm_pins[idx][0];
  int p_l = motor_pwm_pins[idx][1];

  if (abs(speed) <= JOYSTICK_DEAD) {
    ledcWrite(p_r, 0);
    ledcWrite(p_l, 0);
    return;
  }

  uint32_t duty = map(abs(speed), 0, 1000, 0, LEDC_MAX_DUTY);

  if (speed > 0) {
    ledcWrite(p_r, duty);
    ledcWrite(p_l, 0);
  } else {
    ledcWrite(p_r, 0);
    ledcWrite(p_l, duty);
  }
}

void motorSetAll(int s0, int s1, int s2, int s3) {
  motorSetOne(0, s0);
  motorSetOne(1, s1);
  motorSetOne(2, s2);
  motorSetOne(3, s3);
}

// ================== Simple control logic ==================
// CH0 = steer X, CH1 = throttle Y, CH2 = servo vector
const int TURN_THRESHOLD = 200; // tuneable

void applyControlFromChannels() {
  int16_t steer = rcGetChannel(0);
  int16_t throttle = rcGetChannel(1);

  if (abs(steer) < JOYSTICK_DEAD) steer = 0;
  if (abs(throttle) < JOYSTICK_DEAD) throttle = 0;

  if (abs(steer) > abs(throttle) && abs(steer) > TURN_THRESHOLD) {
    int turnSpeed = steer;
    if (turnSpeed > 0) {
      int right = map(turnSpeed, 0, 1000, 200, 1000);
      int left  = -right;
      // order: motorSetAll(m0,m1,m2,m3)
      motorSetAll(left, right, left, right);
    } else {
      int s = -turnSpeed;
      int leftSpeed = map(s, 0, 1000, 200, 1000);
      int rightSpeed = -leftSpeed;
      motorSetAll(leftSpeed, rightSpeed, leftSpeed, rightSpeed);
    }
  } else {
    motorSetAll(throttle, throttle, throttle, throttle);
  }
}

// ================== PCA9685 Servos ==================
// I2C pins remapped to avoid conflicts with motor pins
#define I2C_SDA_PIN 32
#define I2C_SCL_PIN 33

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x40);

// Servo calibration - tune these for your MG996R
const int SERVO_FREQ = 50;     // Hz
const int SERVOMIN_US = 600;   // microseconds (safe)
const int SERVOMAX_US = 2400;  // microseconds (safe)
const int SERVO_CENTER = 90;   // deg
const int SERVO_MAX_OFFSET = 100; // degrees max each side initially (tune)

// Convert microseconds -> 12-bit ticks (Adafruit uses 12-bit)
uint16_t microsToTicks(uint16_t microseconds) {
  const float period_us = 1000000.0f / SERVO_FREQ; // ~20000us
  float ticks = (microseconds / period_us) * 4096.0f;
  return (uint16_t)constrain((int)round(ticks), 0, 4095);
}

uint16_t angleToTicks(int angle) {
  angle = constrain(angle, 0, 180);
  uint16_t pulse_us = map(angle, 0, 180, SERVOMIN_US, SERVOMAX_US);
  return microsToTicks(pulse_us);
}

// PCA9685 channels for servos
const uint8_t SERVO_CH_FL = 0;
const uint8_t SERVO_CH_FR = 1;
const uint8_t SERVO_CH_RL = 2;
const uint8_t SERVO_CH_RR = 3;

void pcaInit() {
  Wire.begin(I2C_SDA_PIN, I2C_SCL_PIN); // remapped I2C
  pwm.begin();
  pwm.setPWMFreq(SERVO_FREQ);
  delay(10);
  Serial.println("PCA9685 initialized at 50Hz (I2C 32=SDA,33=SCL)");
  // center servos
  pwm.setPWM(SERVO_CH_FL, 0, angleToTicks(SERVO_CENTER));
  pwm.setPWM(SERVO_CH_FR, 0, angleToTicks(SERVO_CENTER));
  pwm.setPWM(SERVO_CH_RL, 0, angleToTicks(SERVO_CENTER));
  pwm.setPWM(SERVO_CH_RR, 0, angleToTicks(SERVO_CENTER));
}

void pcaSetServoAngle(uint8_t ch, int angle) {
  pwm.setPWM(ch, 0, angleToTicks(angle));
}

// Map CH2 (-1000..1000) to servo offsets and write front/ rear mirrored behavior
void applyServosFromChannel() {
  int16_t ch2 = rcGetChannel(2);
  if (abs(ch2) < 20) ch2 = 0;

  int offsetDeg = map(ch2, -1000, 1000, -SERVO_MAX_OFFSET, SERVO_MAX_OFFSET);

  // Front servos: center + offset
  int fl = constrain(SERVO_CENTER + offsetDeg, 0, 180);
  int fr = constrain(SERVO_CENTER + offsetDeg, 0, 180); // mirrored
  // Rear servos: center - offset (opposite of front) to get back motors go opposite
  int rl = constrain(SERVO_CENTER + offsetDeg, 0, 180);
  int rr = constrain(SERVO_CENTER + offsetDeg, 0, 180);

  pcaSetServoAngle(SERVO_CH_FL, fl);
  pcaSetServoAngle(SERVO_CH_FR, fr);
  pcaSetServoAngle(SERVO_CH_RL, rl);
  pcaSetServoAngle(SERVO_CH_RR, rr);
}

// ================ Setup / Loop ================
unsigned long lastPrintMs = 0;

void setup() {
  Serial.begin(115200);
  delay(300);
  Serial.println();
  Serial.println("=== ESP32 RX + 4x IBT2 + PCA9685 servos (integrated) ===");

  if (!rcInit()) {
    Serial.println("rcInit failed, halting.");
    while (true) delay(1000);
  }

  // motors
  motorsAttachAll();
  Serial.println("Motors attached.");

  // PCA9685 / servos
  pcaInit();
  Serial.println("PCA9685 + servos ready.");
}

void loop() {
  rcUpdate();

  if (rcLinkActive() && !rcFailsafeActive()) {
    applyControlFromChannels();  // motor control
    applyServosFromChannel();    // servo vectoring via CH2
  } else {
    // failsafe: stop motors and center servos
    motorSetAll(0,0,0,0);
    pcaSetServoAngle(SERVO_CH_FL, SERVO_CENTER);
    pcaSetServoAngle(SERVO_CH_FR, SERVO_CENTER);
    pcaSetServoAngle(SERVO_CH_RL, SERVO_CENTER);
    pcaSetServoAngle(SERVO_CH_RR, SERVO_CENTER);
  }

  // debug print every 200 ms
  unsigned long now = millis();
  if (now - lastPrintMs >= 200) {
    lastPrintMs = now;
    Serial.print("Link=");
    Serial.print(rcLinkActive() ? "ON" : "OFF");
    Serial.print("  Failsafe=");
    Serial.print(rcFailsafeActive() ? "ON" : "OFF");
    Serial.print("  FrameId=");
    Serial.print(rcGetLastFrameId());
    Serial.print("  | CH: ");
    for (int i = 0; i < 8; ++i) {
      Serial.print(rcGetChannel(i));
      if (i < 7) Serial.print(", ");
    }
    Serial.println();
  }
}

