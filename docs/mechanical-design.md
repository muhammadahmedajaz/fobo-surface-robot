# FOBO: design and construction

FOBO is a remotely controlled surface robot built for water soccer. It placed first among 64 participating projects in the HydroBot Soccer League. The competition result belongs to Muhammad Ahmed and his teammate.

The design priorities were directional control, pushing the ball, dodging other robots and building within a small budget. These priorities shaped both the hull and propulsion.

## Why a twin-hull body

The team considered a flat platform, a V-shaped hull and a catamaran arrangement. The selected body has two floats joined by a bridge, with an electronics/battery bay near the centre. Stability, maneuverability and reducing water resistance were the recorded design aims. No comparative drag measurements are available for the alternative hulls.

The XPS foam was the first physical form of the design. The team shaped the foam body and then applied fiberglass over its exterior. The foam-stage and fiberglass-work photographs show that progression in the [construction gallery](gallery.md#construction).

Earlier build notes record three basic fiberglass layers, with additional layers in curved areas, locally reaching six. Mounts were mainly integrated with the fiberglass; wooden inserts and adhesive were also used. Resin type, cloth weight and curing conditions are not recorded, so this account does not prescribe a resin mixing or curing schedule.

## Layout and size

![Conceptual component arrangement](../assets/figures/mechanical-layout-concept.png)

The layout shows the reported component arrangement; individual mounting positions are schematic. The photographs show the physical outline.

| Item | Project record |
| --- | --- |
| Overall length | Approximately 23 in / 58 cm |
| Overall width | Approximately 17 in / 43 cm |
| Overall height | Approximately 13 in / 33 cm |
| Dimensional precision | Ahmed confirms the report's dimensions as approximate, with roughly 1–2 in variation |
| Bare body mass | Earlier build notes report about 2.5 kg |
| Equipped mass | Earlier build notes report about 4.5–5 kg |
| Battery/electronics | Central compartment; earlier project record lists a 3S 2200 mAh LiPo |

The dimensions describe the prototype's approximate envelope, rather than manufacturing tolerances. The report's separate 18 × 18 × 18 in constraint is inconsistent with that envelope and is not used as a compliance claim.

## Why ordinary DC motors and servos

Commercial underwater propulsion was beyond the project's budget. The team used four ordinary **680 RPM DC motors**, each driving a propeller. Earlier selection notes identify the JGB37-550 12 V, 680 RPM option. The exact installed nameplate and underwater propeller size are not preserved with the source.

Each propulsion unit was mounted on an MG996R servo so the motor and propeller could rotate together. The DC motor provides thrust; the servo changes the direction in which that thrust acts. This is **vectored thrust**.

The propulsion concept evolved from two motors with a separate turning mechanism, to four fixed units, and finally four rotating units. Each motor's approximately 300 g mass and the cost of lighter alternatives were part of the design constraint.

## How FOBO moves

![Reported propulsion modes](../assets/figures/propulsion-modes.png)

| Motion reported by the builder | Mechanical action |
| --- | --- |
| Forward | All four propulsion units drive forward |
| Backward | All four reverse their drive direction |
| Left/right translation | The servos redirect the motor/propeller units to produce a lateral thrust component |
| Pivot on the spot | Two-motor groups drive in opposing directions; reversing the groups reverses the turn |

The opposing-drive turn is **differential thrust**. Forward/backward translation, sideways translation and heading rotation correspond to three planar motions: surge, sway and yaw.

For a single unit, thrust T directed at angle δ has components T cos(δ) and T sin(δ). This explains the mechanism without assigning an unmeasured thrust value.

The supplied firmware commands all four servo outputs from CH2 with the same numerical angle. CH0/CH1 select motor turning or forward/reverse drive. Mount orientation and motor polarity determine physical directions. Four rotating mounts do not imply four independently commanded servo angles in this receiver. See the [controller build guide](build-guide.md) and [calculated command maps](analysis.md).

Two raised rear propellers are visible in the footage and were described as boosters for additional pushing force. Their controller, exact parts and wiring are outside the recovered four-IBT-2 receiver source.

## Motor and servo protection

The low-cost packaging used motor-sized and servo-sized cavities in XPS foam, sealed with hot glue and silicone. The motor shaft remained outside the foam. Ahmed confirmed this construction directly; it replaces the report's unconfirmed epoxy-around-shaft description.

During the final round, one servo stopped working because water entered it. The packaging worked through much of the project but had an observed ingress failure. The full method and this limitation are recorded in [waterproofing and the final-round failure](waterproofing.md).

## Build and test evidence

- [Construction photos and operating footage](gallery.md)
- [Media sources and excerpt times](../assets/build/README.md)
- [Corrections to the original report](report-cross-check.md)
- [Firmware baseline and software checks](validation.md)
- [Later mobile-camera/OpenCV work](vision-extension.md)
