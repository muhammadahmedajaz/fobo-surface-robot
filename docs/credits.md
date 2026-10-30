# Credits and references

FOBO is a team-built surface robot. This repository is maintained by Muhammad Ahmed and documents the controller source, integration and analysis files shared for the project.

The HydroBot Soccer League result, first among 64 teams, is a team achievement. The hardware-testing status was confirmed by Muhammad Ahmed.

The short project clip is taken from the FOBO footage previously supplied by Ahmed. A frame from it is used as the README image.

Additional construction photographs come from the supplied December 2025 project report. New pool excerpts come from original videos Ahmed supplied, alongside two recovered edited reels. Captions identify the construction stage or the clip source rather than adopting the report's prototype captions unchanged. See [media provenance](../assets/build/README.md) and the [report cross-check](report-cross-check.md).

Ahmed's 30 October 2026 account supplies the XPS/hot-glue/silicone packaging method, the final-round servo ingress failure, the four 680 RPM motor arrangement and approximate dimensions. The later mobile-camera/OpenCV work is documented with the scope of the recorded bench tests.

The [engineering journey](build-journey.md) was reconstructed from attributed conversation excerpts/summaries, the supplied report, media and builder clarification. Its [source register](journey-sources.md) records dated user input, assistant contributions, corrections and recovery gaps. New hull/timeline illustrations are reconstructed explanatory figures; no original handwritten page is claimed for them.

## Dependencies and primary references

- [Espressif Arduino-ESP32 3.3.0 release](https://github.com/espressif/arduino-esp32/releases/tag/3.3.0), based on ESP-IDF 5.5.0.
- [ESP-IDF 5.5 ESP-NOW callback change](https://docs.espressif.com/projects/esp-idf/en/v5.5/esp32/migration-guides/release-5.x/5.5/wifi.html).
- [Arduino-ESP32 LEDC migration](https://docs.espressif.com/projects/arduino-esp32/en/latest/migration_guides/2.x_to_3.0.html).
- [Adafruit PWM Servo Driver library](https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library).
- [Adafruit BusIO](https://github.com/adafruit/Adafruit_BusIO).
- [Adafruit PCA9685 pin and power guide](https://learn.adafruit.com/16-channel-pwm-servo-driver/pinouts).
- [HandsOn BTS7960 module guide](https://www.handsontec.com/dataspecs/module/BTS7960%20Motor%20Driver.pdf).

NumPy, SciPy and Matplotlib are used for the reproducible analysis. MATLAB/Simulink files require the corresponding MathWorks products. External libraries and tools retain their respective licences; they are not vendored into this repository.

