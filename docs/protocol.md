# ESP-NOW frame and command semantics

Both main sketches declare a packed `RcFrame` and send its memory bytes directly. On the classic ESP32 this is a 21-byte, little-endian payload.

| Byte offset | Field | Type / length | Meaning |
| --- | --- | --- | --- |
| 0 | protoVersion | uint8 / 1 byte | TX sends 1 |
| 1 | flags | uint8 / 1 byte | TX sends 0; no arming logic implemented |
| 2–3 | frameId | uint16 / 2 bytes | Incrementing counter, wraps at 65535 |
| 4–19 | ch[0..7] | eight int16 values / 16 bytes | Four joystick axes, three buttons, one reserved value |
| 20 | crc | uint8 / 1 byte | CRC over bytes 0–19 |

CRC-8 parameters are polynomial 0x07, initial value 0x00, no reflection and no final XOR. The check value for ASCII `123456789` is 0xF4.

The firmware rejects the wrong frame length or CRC. It does not enforce the version field, frame ordering or an armed flag. The frame counter is used for diagnostics. The peer is unencrypted in the supplied transmitter.

## Payload example

```bash
python tools/protocol_example.py
```

The Python helper demonstrates packing, signed little-endian channels and CRC checking. It provides no radio transport. A PC cannot send ESP-NOW merely by calling this encoder; an ESP32 bridge or suitable radio implementation would be a separate component.

## Actuator commands

Channel 0 controls motor steering; channel 1 controls throttle. Values are normally −1000–1000. If steering dominates throttle and exceeds 200, the motor groups receive opposite-direction commands. Otherwise all four follow throttle. Final commands with absolute magnitude 50 or less produce zero PWM.

Channel 2 maps to a servo offset of −100–100 degrees. Values with absolute magnitude below 20 are treated as zero. Every servo is commanded to `constrain(90 + offset, 0, 180)`.

Buttons are encoded as 0 or 1000. Channels 3–7 have no actuator effect in the current receiver.

## Timing and link-loss branch

The TX schedules sends at 10 ms intervals, a nominal 100 Hz. RX considers the link lost when elapsed time since the last valid frame exceeds 300 ms. Its main loop then commands zero motor PWM and centred servos.

The received channel array and flags are shared between the Wi-Fi callback and the loop without a protected frame snapshot. This is a possible future software improvement; the published baseline preserves the hardware-tested behaviour.

