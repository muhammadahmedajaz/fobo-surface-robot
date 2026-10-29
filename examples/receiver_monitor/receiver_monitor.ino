// Milestone 6 - RX: Reusable RC API + failsafe on ESP32
// - Receives RcFrame from TX via ESP-NOW
// - Validates CRC-8
// - Maintains channels[] array
// - Provides rcInit(), rcUpdate(), rcLinkActive(), rcFailsafeActive(), rcGetChannel()

#include <WiFi.h>
#include <esp_now.h>

// ===== RcFrame + CRC-8 =====
typedef struct __attribute__((packed)) {
  uint8_t  protoVersion;
  uint8_t  flags;
  uint16_t frameId;
  int16_t  ch[8];
  uint8_t  crc;
} RcFrame;

// CRC-8 function (poly 0x07, init 0x00)
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

// ===== Internal RC link state =====
static RcFrame lastFrame;
static int16_t channels[8] = {0};

static volatile bool newFrameFlag = false;

static bool     linkActive     = false;
static bool     failsafeActive = true;
static uint32_t lastRxMs       = 0;
static uint16_t lastFrameId    = 0;

// Failsafe timing (tune as you like)
const uint32_t HARD_FAILSAFE_MS = 300;  // after this, force safe state

// ===== ESP-NOW receive callback (NEW API) =====
void onDataRecv(const esp_now_recv_info_t *info, const uint8_t *incomingData, int len) {
  if (len != sizeof(RcFrame)) {
    return;  // ignore unexpected size
  }

  RcFrame f;
  memcpy(&f, incomingData, sizeof(RcFrame));

  // CRC check (exclude last crc byte)
  uint8_t computed = crc8((uint8_t*)&f, sizeof(RcFrame) - 1);
  if (computed != f.crc) {
    return;  // bad CRC -> drop
  }

  // Store frame
  lastFrame = f;
  for (int i = 0; i < 8; i++) {
    channels[i] = f.ch[i];
  }

  lastRxMs        = millis();
  linkActive      = true;
  failsafeActive  = false;
  lastFrameId     = f.frameId;

  newFrameFlag = true;

  // If you ever need MAC:
  // const uint8_t *mac = info->src_addr;
}

// ===== Failsafe behaviour =====
void applyHardFailsafe() {
  // Example safe state:
  // CH1: steering neutral (0)
  // CH2: throttle minimum (-1000)
  // CH3,4: neutral
  channels[0] = 0;       // steering neutral
  channels[1] = -1000;   // throttle min
  channels[2] = 0;
  channels[3] = 0;

  // Buttons off
  for (int i = 4; i < 8; i++) {
    channels[i] = 0;
  }

  failsafeActive = true;
}

// ===== Public API =====

// Call once in setup()
bool rcInit() {
  WiFi.mode(WIFI_STA);
  delay(50);

  if (esp_now_init() != ESP_OK) {
    Serial.println("rcInit: Error initializing ESP-NOW");
    return false;
  }

  esp_now_register_recv_cb(onDataRecv);

  // Start in failsafe state until first valid frame
  applyHardFailsafe();
  linkActive = false;

  Serial.println("rcInit: ESP-NOW RX initialized");
  return true;
}

// Call frequently in loop()
void rcUpdate() {
  uint32_t now = millis();

  // Link was active, but no frames for too long -> failsafe
  if (linkActive && (now - lastRxMs > HARD_FAILSAFE_MS)) {
    Serial.println("rcUpdate: HARD FAILSAFE triggered (link lost)");
    applyHardFailsafe();
    linkActive = false;
  }
}

// True if link is currently active (recent valid frame)
bool rcLinkActive() {
  return linkActive;
}

// True if failsafe is currently active (link lost or not yet established)
bool rcFailsafeActive() {
  return failsafeActive;
}

// Get channel value, ch = 0..7
int16_t rcGetChannel(int ch) {
  if (ch < 0 || ch > 7) {
    return 0;
  }
  return channels[ch];
}

// Optional: expose last frame ID (for debugging / logging)
uint16_t rcGetLastFrameId() {
  return lastFrameId;
}

// ===== Example main sketch using the API =====

unsigned long lastPrintMs = 0;

void setup() {
  Serial.begin(115200);
  delay(500);

  Serial.println();
  Serial.println("=== ESP32 RC RX - Milestone 6 (API + failsafe) ===");

  if (!rcInit()) {
    Serial.println("rcInit failed, halting.");
    while (true) {
      delay(1000);
    }
  }

  Serial.println("RC link ready. Waiting for transmitter...");
  Serial.println();
}

void loop() {
  rcUpdate();  // maintain failsafe timing

  // Debug print every 200 ms
  unsigned long now = millis();
  if (now - lastPrintMs >= 200) {
    lastPrintMs = now;

    bool     link = rcLinkActive();
    bool     fs   = rcFailsafeActive();
    uint16_t id   = rcGetLastFrameId();

    Serial.print("Link=");
    Serial.print(link ? "ON" : "OFF");
    Serial.print("  Failsafe=");
    Serial.print(fs ? "ON" : "OFF");
    Serial.print("  FrameId=");
    Serial.print(id);
 
   Serial.print("  | CH: ");

    for (int i = 0; i < 8; i++) {
      Serial.print(rcGetChannel(i));
      if (i < 7) Serial.print(", ");
    }
    Serial.println();
  }

  // Here is where your project logic would go, e.g.:
  // if (rcLinkActive() && !rcFailsafeActive()) {
  //   int16_t throttle = rcGetChannel(1);
  //   int16_t steering = rcGetChannel(0);
  //   // drive motors, servos, etc.
  // } else {
  //   // keep motors off / safe
  // }
}
