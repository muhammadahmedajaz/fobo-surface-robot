# Mechanical design and construction

FOBO uses a fiberglass-covered XPS catamaran with four servo-rotatable propulsion units. The mechanical design supports forward/reverse drive, lateral thrust vectoring and differential-thrust pivot turns.

## Hull and structure

The design considered flat, V-shaped and twin-hull arrangements. The catamaran was selected for stability, maneuverability and the intended reduction of water resistance. Two hulls connect through a bridge with a central electronics and battery compartment.

XPS foam established the body shape before fiberglass application. The build account specifies three basic layers, with reinforcement reaching six locally in curved regions. Mounts were integrated with the fiberglass; wooden inserts and adhesive were also used.

![Conceptual component arrangement](../assets/figures/mechanical-layout-concept.png)

| Property | Prototype value |
| --- | --- |
| Length | Approximately 23 in / 58 cm |
| Width | Approximately 17 in / 43 cm |
| Height | Approximately 13 in / 33 cm |
| Dimensional variation | Roughly 1-2 in |
| Bare body mass | Approximately 2.5 kg |
| Equipped mass | Approximately 4.5-5 kg |
| Battery/electronics position | Central compartment |
| Battery in the earlier build record | 3S 2200 mAh LiPo |

The diagram shows the component arrangement schematically. The [construction photographs and videos](gallery.md) show the physical structure.

## Propulsion and rotating mounts

Four 680 RPM DC motors drive the main propellers. Motor-selection work included the JGB37-550 12 V / 680 RPM option. Approximately 300 g per motor made the four drives a significant part of the platform's mass.

Each MG996R servo rotates a motor/propeller mount. The motor provides thrust and the servo changes its direction. The concept developed from two thrusters with a turning mechanism, through four fixed units, to four rotating units.

Two raised rear propellers were added for stronger ball pushing. The published receiver controls the four main DC propulsion units.

## Motion

![Thrust directions for three planar motions](../assets/figures/propulsion-modes.png)

| Motion | Mechanical action |
| --- | --- |
| Forward / reverse | All four main propulsion units drive in the corresponding direction |
| Left / right translation | Servo mounts redirect thrust laterally |
| Pivot | Two-motor groups drive in opposing directions |

For a unit producing thrust T at angle δ, the planar components are T cos(δ) and T sin(δ). These components explain how changing mount angle redirects force without assigning a thrust value.

The receiver uses CH2 as a shared vector command. All four servo outputs receive the same numerical angle, and the physical motor orientation depends on mounting. CH0/CH1 select motor turning or common forward/reverse drive.

## Actuator packaging

Motors and servos sit in matching XPS cavities sealed with hot glue and silicone. Motor shafts remain outside the surrounding foam. One servo suffered water ingress during the final round.

The [actuator-protection guide](waterproofing.md) describes the method and its operating lesson. The [engineering journey](build-journey.md) and [decision log](decision-log.md) explain the trade-offs behind the construction.
