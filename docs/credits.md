# Credits and references

FOBO was built by Muhammad Ahmed and his teammate. The first-place HydroBot Soccer League result is a team achievement. This repository is maintained by [Muhammad Ahmed](https://github.com/muhammadahmedajaz).

Construction photographs come from the project report. Development and operating footage were supplied by the project team. The [media index](../assets/build/README.md) lists source recordings and processing details.

The [engineering case study](build-journey.md) covers design, fabrication, propulsion and control. The [technical references](journey-sources.md) identify the design discussions, implementation source and validation scope. Concept illustrations are original repository graphics.

## Dependencies and primary references

- [Espressif Arduino-ESP32 3.3.0 release](https://github.com/espressif/arduino-esp32/releases/tag/3.3.0), based on ESP-IDF 5.5.0.
- [ESP-IDF 5.5 ESP-NOW callback change](https://docs.espressif.com/projects/esp-idf/en/v5.5/esp32/migration-guides/release-5.x/5.5/wifi.html).
- [Arduino-ESP32 LEDC migration](https://docs.espressif.com/projects/arduino-esp32/en/latest/migration_guides/2.x_to_3.0.html).
- [Adafruit PWM Servo Driver library](https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library).
- [Adafruit BusIO](https://github.com/adafruit/Adafruit_BusIO).
- [Adafruit PCA9685 pin and power guide](https://learn.adafruit.com/16-channel-pwm-servo-driver/pinouts).
- [HandsOn BTS7960 module guide](https://www.handsontec.com/dataspecs/module/BTS7960%20Motor%20Driver.pdf).

NumPy, SciPy and Matplotlib are used for the reproducible analysis. MATLAB/Simulink files require the corresponding MathWorks products. External libraries and tools retain their respective licences; they are not vendored into this repository.

