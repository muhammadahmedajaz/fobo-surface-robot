# Design decision log

Cost, local component availability and the movement demands of water soccer shaped FOBO's design. The dates below identify planning and design reviews.

## D01. Feasibility and cost

Planning review, 6 November 2025.

The robot needed directional control, torque, precision and speed within a $150-200 planning budget. Commercial underwater propulsion and advanced control hardware exceeded the available means.

The selected direction used obtainable DC motors, servo-adjustable mounts and a simpler controller. Water pumps were considered during discussion, while the design work returned to motor-based propulsion and the platform's mass requirements.

## D02. Hull and structure

Concept selection reviewed on 30 November 2025.

Flat, V-shaped and dual-catamaran concepts were considered. The selection criteria included maneuverability, stability, cost and availability, weight, thrust capability and fit to the game.

The catamaran was selected with two hulls joined by a bridge and a central electronics/battery bay. Stability during directional changes and the intended reduction of water resistance formed part of the rationale. The [hull-concept figure](../assets/figures/hull-concept-selection.png) illustrates the three categories.

## D03. Mass and packaging

The early design used a 3.2 kg planning mass. Four propulsion motors at approximately 300 g each represented about 1.2 kg of that allocation. Lighter, high-thrust underwater alternatives exceeded the budget.

The build account describes a roughly 2.5 kg bare body and a 4.5-5 kg equipped platform, with an approximate envelope of 23 × 17 × 13 in. These values distinguish the preliminary mass target from the assembled prototype.

## D04. Rotating propulsion units

Concept development progressed from two thrusters with a separate turning mechanism to four fixed units, then four rotatable units. Servo-adjustable corner motors appeared in the November planning discussions.

The selected arrangement uses MG996R servos to redirect the motor/propeller units. Motor reversal and opposing-drive groups provide forward/reverse movement and pivot turns. The rotating mounts add mechanical interfaces, servo power requirements and actuator sealing work.

## D05. Motor and propeller matching

Selection discussion, 13-14 November 2025.

The 25GA-370 12 V / 1360 RPM and JGB37-550 12 V / 680 RPM options were compared. A roughly 6 kgf total thrust target and an available 6 × 4E propeller were discussed during development.

The physical build uses four 680 RPM motors. The choice considered torque, speed, motor mass and affordability. Numerical thrust calculations from this stage remain planning estimates; the repository's command plots describe PWM and servo commands.

## D06. Rear boosters

The four lower thrusters did not provide the forceful ball pushing desired. Two raised rear propellers were added for additional forward pushing, with continued capability after a main-thruster failure as a second design intention.

The rear units are visible in operating footage. The published four-IBT-2 controller implements the four main DC propulsion channels.

## D07. XPS form and fiberglass shell

XPS foam established the hull and bridge geometry before fiberglass application. Manual shaping and sanding are visible in the [construction video](../assets/build/development/foam-shaping.mp4).

The build account specifies three basic layers, with local reinforcement reaching six around curved regions. Mounts were integrated with the fiberglass structure, with wooden inserts and adhesive also used.

## D08. Actuator protection

An early tube-based motor pod with shaft supports and multiple sealing interfaces was considered too complex for the build. The implemented method placed motors and servos in matching XPS cavities, sealed using hot glue and silicone. Motor shafts remained outside the surrounding foam.

The arrangement supported operation through the project. Water entered one servo during the final round and stopped it. A serviceable enclosure and repeated exposure checks are priorities for a further sealing revision.

## D09. Integrated RC control

The hardware-tested receiver uses ESP32/ESP-NOW, CRC-8, four IBT-2 modules and a PCA9685. Earlier electronics notes describe an L298N configuration; replication should follow the published IBT-2 signal maps.

CH0/CH1 control motor turning and throttle. CH2 supplies a shared numerical angle to the four servo outputs. I²C uses GPIO 32/33, separate from motor outputs 21/22. The main-loop inactive branch stops the motors and centres the servos after link loss.

## D10. Camera feedback

Extension discussions, 20-21 December 2025.

Timed trajectories and camera point following were explored under a one-day Python development constraint and without dedicated sensing hardware. The mobile-camera experiment was narrowed to motor-only control. A direct camera-command interface required receiver input changes from the joystick ESP-NOW path.

Later PC/laptop YOLO/OpenCV work bench-tested target detection, ESP32 commands and motor response. On-water autonomous following is a further validation stage.

## D11. Validation scope

The project distinguishes physical operation, software behavior and model-based analysis. The competition result belongs to the RC platform. Firmware command maps explain the implemented motor and servo logic. The yaw/PID study uses a nominal plant, and the vision work has a bench-test scope.

This separation allows each result to be reproduced using its appropriate setup. See the [test record](validation.md), [analysis](analysis.md) and [technical references](journey-sources.md).
