// Milestone 5 - TX: Real RcFrame with joysticks + buttons on ESP32

#include <WiFi.h>
#include <esp_now.h>

// ====== CHANGE THIS TO YOUR RX ESP32 MAC ADDRESS ======
// Example: 4C:C3:82:BE:80:3C  -->  { 0x4C, 0xC3, 0x82, 0xBE, 0x80, 0x3C }
uint8_t peerMac[] = { 0x4C, 0xC3, 0x82, 0xBE, 0x80, 0x3C };
// ======================================================

// ---- Pin definitions ----
const int JOY1_X_PIN = 34;  // ADC1
const int JOY1_Y_PIN = 35;  // ADC1
const int JOY2_X_PIN = 32;  // ADC1
const int JOY2_Y_PIN = 33;  // ADC1

const int BTN1_PIN   = 25;
const int BTN2_PIN   = 26;
const int BTN3_PIN   = 27;

// ===== RcFrame + CRC-8 =====
typedef struct __attribute__((packed)) {
  uint8_t  protoVersion;   // protocol version
  uint8_t  flags;          // bit0: armed, etc. (later)
  uint16_t frameId;        // increments every frame
  int16_t  ch[8];          // 8 channels
  uint8_t  crc;            // CRC-8
} RcFrame;

// CRC-8 (polynomial 0x07, initial value 0x00)
uint8_t crc8(const uint8_t *data, size_t len) {
  uint8_t crc = 0x00;
  while (len--) {
    crc ^= *data++;
    for (uint8_t i = 0; i < 8; i++) {
      if (crc & 0x80)
        crc = (crc << 1) ^ 0x07;
      else
        crc <<= 1;
    }
  }
  return crc;
}

RcFrame frame;
uint16_t frameCounter = 0;

const unsigned long FRAME_PERIOD_MS = 10;  // 100 Hz
unsigned long lastFrameMs = 0;

// ---- Helpers to map inputs to RC channel values ----

// Map raw ADC (0..4095) to -1000..+1000
int16_t mapStick(int raw) {
  long val = map(raw, 0, 4095, -1000, 1000);
  return (int16_t)val;
}

// Return 0 or 1000 based on button state (pressed / not pressed)
int16_t readButtonRc(uint8_t pin) {
  // Buttons wired to GND with INPUT_PULLUP:
  // LOW = pressed, HIGH = not pressed
  return (digitalRead(pin) == LOW) ? 1000 : 0;
}

// Updated send callback for new ESP-NOW API (IDF 5.5 / Arduino-ESP32 v3.x)
void onDataSent(const esp_now_send_info_t *tx_info, esp_now_send_status_t status) {
  // Uncomment if you want debug spam:
  // Serial.print("Send status: ");
  // Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Success" : "Fail");
}

void setup() {
  Serial.begin(115200);
  delay(500);

  Serial.println();
  Serial.println("=== ESP32 RC TX - Milestone 5 (Joysticks + Buttons) ===");

  // Joysticks are analog inputs (no pinMode needed for ADC pins)
  pinMode(BTN1_PIN, INPUT_PULLUP);
  pinMode(BTN2_PIN, INPUT_PULLUP);
  pinMode(BTN3_PIN, INPUT_PULLUP);

  WiFi.mode(WIFI_STA);
  delay(100);

  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW!");
    while (true) {
      delay(1000);
    }
  }

  esp_now_register_send_cb(onDataSent);

  esp_now_peer_info_t peerInfo = {};
  memcpy(peerInfo.peer_addr, peerMac, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;

  if (esp_now_add_peer(&peerInfo) != ESP_OK) {
    Serial.println("Failed to add peer");
    while (true) {
      delay(1000);
    }
  }

  Serial.println("ESP-NOW TX initialized. Sending live RC data...");
}

void loop() {
  unsigned long now = millis();
  if (now - lastFrameMs >= FRAME_PERIOD_MS) {
    lastFrameMs = now;

    // ---- Read raw joystick ADCs ----
    int joy1X_raw = analogRead(JOY1_X_PIN);
    int joy1Y_raw = analogRead(JOY1_Y_PIN);
    int joy2X_raw = analogRead(JOY2_X_PIN);
    int joy2Y_raw = analogRead(JOY2_Y_PIN);

    // ---- Map to RC ranges ----
    int16_t ch1 = mapStick(joy1X_raw);  // e.g. steering/roll
    int16_t ch2 = mapStick(joy1Y_raw);  // e.g. throttle
    int16_t ch3 = mapStick(joy2X_raw);
    int16_t ch4 = mapStick(joy2Y_raw);

    int16_t ch5 = readButtonRc(BTN1_PIN);
    int16_t ch6 = readButtonRc(BTN2_PIN);
    int16_t ch7 = readButtonRc(BTN3_PIN);
    int16_t ch8 = 0;  // reserved / future use

    // ---- Fill frame ----
    frame.protoVersion = 1;
    frame.flags        = 0;              // we’ll use this later
    frame.frameId      = frameCounter++;

    frame.ch[0] = ch1;
    frame.ch[1] = ch2;
    frame.ch[2] = ch3;
    frame.ch[3] = ch4;
    frame.ch[4] = ch5;
    frame.ch[5] = ch6;
    frame.ch[6] = ch7;
    frame.ch[7] = ch8;

    // ---- CRC ----
    frame.crc = crc8((uint8_t*)&frame, sizeof(RcFrame) - 1);

    // ---- Send via ESP-NOW ----
    esp_err_t result = esp_now_send(peerMac, (uint8_t*)&frame, sizeof(RcFrame));

    // Debug print (comment out later if too spammy)
    if (result == ESP_OK) {
      Serial.print("Sent frameId=");
      Serial.print(frame.frameId);
      Serial.print(" | ch: ");
      for (int i = 0; i < 8; i++) {
        Serial.print(frame.ch[i]);
        if (i < 7) Serial.print(", ");
      }
      Serial.print(" | crc=0x");
      Serial.println(frame.crc, HEX);
    } else {
      Serial.print("ESP-NOW send error: ");
      Serial.println(result);
    }
  }
}
