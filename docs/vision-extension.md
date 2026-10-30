# Later mobile-camera and OpenCV work

The HydroBot competition platform was remotely controlled. Vision work was a later extension of FOBO.

Ahmed reports work using a mobile-phone camera and OpenCV. The earlier test record also identifies a PC/laptop-based YOLO/OpenCV target-detection pipeline that sent control commands to the ESP32.

| Part of the work | Recorded status |
| --- | --- |
| Mobile-phone camera / OpenCV work | Reported by Ahmed as follow-on development |
| PC/laptop YOLO/OpenCV target detection | Implemented and bench-tested |
| Commands sent to ESP32 | Bench-tested |
| Motor response to the commands | Bench-tested |
| Autonomous target following in water | Not tested in water |

The phone app, camera transport, command protocol and exact relationship between the mobile and PC revisions are not yet recorded here. No particular UDP, USB, Wi-Fi-streaming app or phone-only processing setup is asserted.

The preserved transmitter/receiver sketches implement joystick RC control. The recovered archive did not contain an identified runnable source package for this vision extension. The repository therefore documents its tested scope without substituting demonstration code for the original implementation.

To reproduce the extension, the next source addition should contain the actual camera input, detection model and labels, command interface, ESP32-side changes and a bench-test example. A later water trial would need its own firmware revision and recorded observations.
