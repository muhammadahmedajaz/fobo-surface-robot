# Cross-check of the recovered project report

The December 2025 project report is useful for recovering construction photographs, design history and assembly descriptions. Ahmed supplied it with the warning that some parts may be inaccurate. This cross-check combines the tested source, footage and Ahmed's 30 October 2026 clarification of the actual build.

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
| Four 680 RPM motors and two BLDC boosters with 10-inch propellers | Ahmed confirms four 680 RPM DC motors, four propellers and servo-mounted rotating units. Earlier selection notes identify the JGB37-550 option. Rear booster part numbers, propeller sizes and control wiring remain unconfirmed. |
| Silicone seams, epoxy/silicone near motor shafts, sealed cable exits | Superseded by Ahmed's actual method: motor-sized XPS enclosure with the shaft outside, filled/sealed using hot glue and silicone. Servos were similarly placed in XPS cavities and sealed with glue/silicone. Epoxy around the motor shaft is not part of the confirmed account. |
| O-rings or cable glands | Section 7.5 uses conditional wording. Do not infer that a specific gland or shaft-seal assembly was installed. |
| 23 × 17 × 13 inches and an 18 × 18 × 18 inch limit | Ahmed confirms the report's dimensions as approximate, with roughly 1–2 in variation. Publish the approximate 23 × 17 × 13 in envelope; do not claim it fits an 18 in cube. |
| Dual 12 V packs in the summary; a 3S 2200 mAh pack in Chapter 4 | The battery descriptions conflict. Retain the earlier project record as a record, and obtain the actual installed battery arrangement before drawing the full harness. |
| Speed 1.5 m/s, 90-degree turn under 0.8 s, 15–20 minute runtime, 600 m radio range | No matching measurement logs accompany these numbers. They are not published as measured FOBO results. |
| Fully waterproof / zero ingress | Corrected: Ahmed reports one servo failed from water ingress during the final round, while the arrangement otherwise worked well through the project. The documented foam/glue/silicone method has an observed sealing failure and no claimed ingress rating. |
| Figure 3.1 described as three hull concepts | The embedded image depicts a single illustrated arrangement. It is not photographic evidence of three manufactured alternatives. |
| Figure 3.2 described as propulsion layouts | The embedded image is a propeller rendering. It does not show the stated layout comparison. |
| Prototype captions implying a completed assembly | Use the fabrication photos according to what is visible. Early hull or enclosure pictures are not a complete actuator installation. |

The original report is not bundled here. Its personal cover-page details and unverified claims are unnecessary for reproducing the controller or understanding the recovered construction photographs.
