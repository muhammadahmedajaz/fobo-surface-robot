# Cross-check of the recovered project report

The December 2025 project report is useful for recovering construction photographs, design history and assembly descriptions. Ahmed supplied it with the warning that some parts may be inaccurate. The current repository therefore uses the tested source for firmware behaviour and keeps unresolved hardware claims visible during this documentation draft.

| Report item | Cross-check and treatment |
| --- | --- |
| XPS/fiberglass twin-hull construction | Matches Ahmed's November build notes and the fabrication photographs. Retained with the photographs. |
| Three basic fiberglass layers, locally up to six | Also present in Ahmed's November description. Retained as a reported layup, with resin/cloth details still needed. |
| Four DC motors on MG996R rotating mounts | Matches the build notes and four motor/four servo outputs in the supplied source. Exact physical motor-index mapping still needs a mounting diagram. |
| L298N motor drivers in Chapters 4, 7 and 9 | The supplied hardware-tested implementation uses four IBT-2 modules with RPWM/LPWM pairs. Keep the repository's IBT-2 map. Whether L298N was an earlier version remains unresolved. |
| IMU-based heading control and PID on the physical robot | No IMU readout or PID controller is present in the supplied receiver. The included heading model is a separate simulation study. Hardware implementation would require separate source and test records. |
| Independent servo angle control | The supplied receiver uses CH2 to command the same numerical angle on all four PCA9685 outputs. Physical mounting can change how these commands orient the motors. |
| Network byte order assumed in Table 6.1 | The ESP32 code copies a packed native structure without byte swapping. The documented reference packet is little-endian and 21 bytes long. |
| 20–50 ms control-frame period | The supplied transmitter schedules a frame every 10 ms. Keep the source-derived value. |
| Wi-Fi/ESP control plus FlySky fallback | The supplied main source implements ESP-NOW. The report does not establish the final physical selector, receiver wiring or switching procedure for a second radio. |
| Four 680 RPM motors and two BLDC boosters with 10-inch propellers | Candidate final specifications from the report. Two raised rear propellers appear in footage, but model numbers, actual propeller sizes and booster controls need the builder's confirmation. |
| Silicone seams, epoxy/silicone near motor shafts, sealed cable exits | Section 9.3.1 describes these steps. They are retained as report claims for review, rather than a verified sealing recipe. Servo sealing and shaft details remain incomplete. |
| O-rings or cable glands | Section 7.5 uses conditional wording. Do not infer that a specific gland or shaft-seal assembly was installed. |
| 23 × 17 × 13 inches and an 18 × 18 × 18 inch limit | Both appear in the report and are incompatible as complete envelopes. Final measured dimensions and the actual competition constraint need clarification. |
| Dual 12 V packs in the summary; a 3S 2200 mAh pack in Chapter 4 | The battery descriptions conflict. Retain the earlier project record as a record, and obtain the actual installed battery arrangement before drawing the full harness. |
| Speed 1.5 m/s, 90-degree turn under 0.8 s, 15–20 minute runtime, 600 m radio range | No matching measurement logs accompany these numbers. They are not published as measured FOBO results. |
| Fully waterproof / zero ingress | Operating footage and the report do not establish a rated ingress-protection level or a documented duration/depth test. Describe the actual sealing construction and recorded observations once confirmed. |
| Figure 3.1 described as three hull concepts | The embedded image depicts a single illustrated arrangement. It is not photographic evidence of three manufactured alternatives. |
| Figure 3.2 described as propulsion layouts | The embedded image is a propeller rendering. It does not show the stated layout comparison. |
| Prototype captions implying a completed assembly | Use the fabrication photos according to what is visible. Early hull or enclosure pictures are not a complete actuator installation. |

The original report is not bundled into this draft. Its personal cover-page details and unverified claims are unnecessary for reproducing the controller or understanding the recovered construction photographs.
