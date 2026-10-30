# Camera feedback and vision control

The HydroBot competition platform used joystick RC control. Later work explored camera feedback for target following, building on the ESP32 motor-control system.

## Mobile-camera concept

The December 2025 discussions considered using a phone camera to observe a visible point, compute a movement command and send it to the receiver. The practical experiment was narrowed to motor-only control.

The proposed behavior included command smoothing, a deadband around the target position and stopping when the target was lost. A direct phone interface requires a receiver input path compatible with those commands.

## PC/laptop implementation

The YOLO/OpenCV pipeline ran on a PC/laptop and sent commands to an ESP32. Bench tests covered target detection, command transmission and physical motor response.

| Work item | Validation stage |
| --- | --- |
| YOLO/OpenCV target detection | Bench-tested |
| Commands to ESP32 | Bench-tested |
| Motor response | Bench-tested |
| Autonomous following on water | Further field-validation stage |

The published transmitter and receiver implement the competition's ESP-NOW joystick controller. The vision extension has a separate command-input scope.

A repeatable field trial should record the camera setup, target definition, controller revision, command interface and target-loss response alongside the vehicle trajectory.

[Controller build guide](build-guide.md) · [Engineering journey](build-journey.md) · [Test record](validation.md)
