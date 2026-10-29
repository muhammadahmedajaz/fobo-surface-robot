#include <Arduino.h>
#include <WiFi.h>

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  delay(500);
  Serial.print("Receiver Wi-Fi MAC: ");
  Serial.println(WiFi.macAddress());
}

void loop() {}
