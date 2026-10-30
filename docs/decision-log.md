# FOBO decision log

This log records the problem, alternatives and decision evidence behind the build. Dates refer to recovered discussions. A retrospective report of concept evolution does not prove that every concept was physically built. Source IDs refer to the [journey source register](journey-sources.md).

## D01 — Budget and obtainable hardware

**Record:** 6 November 2025, S01–S05.

The water-soccer brief combined directional control, torque, precision and speed. Ahmed stated a maximum planning budget of $150–200 and ruled out advanced-controller/ESC proposals outside his means. Waterproof motors suitable for the proposal were unavailable to him. He rejected water pumps as the solution and asked to settle the design mass before the motor search.

**Decision:** pursue obtainable motors and a simpler control/propulsion arrangement; four servo-rotatable corner units appeared in Ahmed's own proposal. This was feasibility-led scope control. Final spending and an itemized purchasing record remain unrecovered.

## D02 — Hull and structure

**Record:** rectangular-versus-square question on 6 November; broader concept retrospective on 30 November, S01, S09–S10.

| Concept discussed | Recovered status | Basis available for comparison |
| --- | --- | --- |
| Flat baseline platform | Considered | Named by Ahmed; original drawing and test data unrecovered |
| V-shaped hull | Considered | Named by Ahmed; original drawing and test data unrecovered |
| Dual catamaran | Selected and constructed | User account, foam/fiberglass photographs and operating footage |

**Decision:** twin hulls connected by a bridge and central bay. Ahmed's stated aims included stability, maneuverability and lower water resistance. Cost, weight, thrust and requirements fit were also part of the overall selection. No numerical decision matrix or controlled hull comparison is established. The reconstructed hull figure illustrates the named categories; it does not replace the original paper sketches.

## D03 — Mass and envelope

**Record:** S01, S05, S09, S17.

The early planning discussion used a two-square-foot footprint constraint and settled on 3.2 kg as a design mass. The assistant's 24 × 12 in proposal and rough buoyancy calculation belonged to that stage. The November build description instead reports a 23 × 17 × 13 in envelope, about 2.5 kg bare and 4.5–5 kg equipped. Ahmed later confirmed the dimensions as approximate, with roughly 1–2 in variation.

**Treatment:** retain targets and later reported values with their dates. Do not retrospectively use the early buoyancy calculation to validate the heavier final body. The later 18 in cube constraint conflicts with the stated length; official rules and inspection evidence remain unrecovered.

## D04 — From fixed propulsion to rotating units

**Record:** S03, S10, S17.

Ahmed's retrospective identifies two thrusters plus a turning mechanism, four fixed units, then four rotatable units. His early 6 November proposal already includes servo rotation, so the precise dates of the earlier concept transitions remain unknown.

**Decision:** use MG996R servo mounts to redirect the four motor/propeller units. Reported motions include surge, sway and yaw through vectored thrust and opposing motor groups. The archive does not establish that each earlier option was built or quantify the improvement against it.

**Trade-off visible in the final design:** rotating units add servo mounts, power demands and moving interfaces requiring protection. This is a retrospective system observation, rather than a recovered weighted trade study.

## D05 — Motor and propeller matching

**Record:** 13–14 November 2025, S07–S08; final 680 RPM confirmation, S17.

Candidates discussed included the 25GA-370 12 V / 1360 RPM and JGB37-550 12 V / 680 RPM. Ahmed sought a roughly 6 kgf total thrust target and raised the available 6 × 4E propeller in the following day's discussion. Four motors at approximately 300 g each were a major mass commitment; lighter high-thrust alternatives exceeded the budget.

**Decision evidence:** the discussion moved to the 680 RPM option; the builder confirms four 680 RPM motors in the physical robot. The exact installed SKU and final propeller dimensions are not established. Assistant thrust estimates were revised and remain unvalidated. No kgf value from those estimates is a measured result.

## D06 — Rear boosters

**Record:** 30 November retrospective and visible rear propellers, S10, S19.

**Problem reported:** the four lower thrusters did not provide the forceful ball pushing desired. Ahmed described additional pushing and fallback capability as the reasons for two rear boosters.

**Decision:** add the rear units. Footage supports their physical presence. Part numbers, propeller size, wiring, quantitative pushing improvement and performance after a lower-unit failure remain unrecorded.

## D07 — Build the body around shaped foam

**Record:** S09, S17, S19.

**Implemented sequence:** shape the XPS body, then apply fiberglass over it. Earlier notes report three basic layers, locally up to six around curves, with fiberglass-integrated mounts and some wood/adhesive use.

**Evidence:** real foam-stage and fiberglass-work photographs corroborate the construction method. Detailed laminate properties, resin/cloth specifications, cure conditions and component-by-component mass measurements are absent. The report's detailed manufacturing schedule is not treated as an independently verified process log.

## D08 — Simplify actuator protection

**Record:** 6 November complexity objection, S06; actual procedure and failure, S17.

The assistant suggested a tube-based motor pod with shaft support, seals and enclosure interfaces. Ahmed rejected the complexity. A bottle/PVC alternative was then suggested, but the confirmed implementation used motor-sized and servo-sized XPS cavities with hot glue and silicone. Only the motor shaft extended outside its surrounding foam.

**Outcome:** useful operation through the project, followed by water entering one servo and stopping it during the final round. The entry path and a repair/teardown sequence are unrecovered. The method is documented as a prototype solution with an observed failure. No ingress rating is claimed.

## D09 — Preserve the implemented RC control

**Record:** November electronics account, S11; integrated source shared 20 December, S12; supplied tested baseline, S20.

The November record names L298N and regulator-powered MG996R servos. The supplied hardware-tested source instead drives four IBT-2 modules and a PCA9685 from an ESP32 receiver. The transition date and cause are unknown.

**Implemented behavior:** CH0/CH1 select motor turning or common forward/reverse drive; CH2 supplies the same numerical angle to four servo outputs. CRC checks and a 300 ms timeout are present. I²C uses 32/33 to avoid motor outputs 21/22. The source has been preserved byte-for-byte, including the servo comment/expression discrepancy. These code facts are not retroactive evidence of a particular debugging session.

## D10 — Give the camera extension a separate scope

**Record:** 20–21 December 2025, S13–S15; 18 October 2026 clarification, S16.

Ahmed sought practical Python functionality within a day and without dedicated sensors. Timed trajectory control and camera point following were explored. He wanted a phone to provide vision and narrowed that experiment to motor-only control. The assistant proposed tracking, a direct command link and stopping on target loss; implementing that link required changes to the archived ESP-NOW-only input.

**Confirmed result:** later PC/laptop YOLO/OpenCV detection, ESP32 commands and motor response were bench-tested. Autonomous target following was not tested in water. Original runnable scripts, receiver modifications and the relationship between the phone and PC revisions remain unrecovered. The competition result belongs to the RC platform.

## D11 — Correct the record when sources disagree

**Record:** 30 October 2026 reconstruction, S17–S20.

The supplied report helps recover photographs and earlier design context, but it also contains unsupported performance, PID/IMU and waterproofing claims. The source code and builder clarification take precedence for the preserved implementation and actual packaging.

**Documentation decision:** keep measured/reported outcomes, planning targets, assistant suggestions and retrospective recommendations identifiable. Retain unresolved version differences. List the missing original sketches rather than generate imitations. This makes the journey useful to another builder and open to correction when the original material is recovered.
