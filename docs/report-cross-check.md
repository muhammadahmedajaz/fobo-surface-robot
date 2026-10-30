# Report and implementation notes

The December 2025 report provides construction context and photographs. For replication, use the published firmware, signal maps and construction procedure described in this repository.

| Topic | Repository reference |
| --- | --- |
| Body construction | XPS form covered with fiberglass; three basic layers and local reinforcement around curves |
| Main propulsion | Four 680 RPM DC motors on MG996R rotating mounts |
| Motor drivers | Four IBT-2 modules with RPWM/LPWM pairs; the earlier report includes an L298N configuration |
| Servo vectoring | CH2 supplies the same numerical angle to four PCA9685 outputs; physical orientation depends on the mounts |
| Heading control | A separate nominal PID simulation; the RC receiver implements joystick control |
| Communication | ESP-NOW using a native packed, little-endian 21-byte frame |
| Frame schedule | Transmitter schedules a frame every 10 ms |
| Actuator protection | Motor-sized and servo-sized XPS cavities, hot glue and silicone; motor shafts outside the foam |
| Prototype envelope | Approximately 23 × 17 × 13 in, with roughly 1-2 in variation |
| Power | Earlier build notes identify a 3S 2200 mAh LiPo; the build guide specifies separate regulated logic and servo rails |
| Rear boosters | Two raised rear propellers for additional pushing; the published receiver covers the four main DC drives |
| Operating result | RC surface operation and first place among 64 HydroBot projects |
| Sealing result | One servo suffered water ingress during the final round |
| Performance figures | Command maps are calculated; heading plots are nominal simulations |

The 18 in cube constraint stated in the earlier report differs from the prototype's approximate length. The dimensions above describe the prototype envelope.

For control details, follow the expressions in the receiver source. Its rear-servo comments describe opposite offsets, while all four actual angle expressions use `90 + offset`.

[Build guide](build-guide.md) · [Mechanical design](mechanical-design.md) · [Actuator protection](waterproofing.md) · [Analysis](analysis.md)
