# Technical references and scope

Design rationale follows the project's planning discussions, construction account, report and operating media. Implementation details refer to the published hardware-tested firmware. Dates in the discussion index use UTC and identify technical reviews or exchanges.

## Design record

<a id="s01-s05"></a>

| Reference | Date | Technical subject |
| --- | --- | --- |
| S01 | 6 November 2025 | Rectangular/square footprint, twin-hull layout and an initial 24 × 12 in proposal |
| S02 | 6 November 2025 | Directional control, torque, precision and speed for water soccer |
| S03 | 6 November 2025 | $150-200 planning budget, component availability and rotating corner motors |
| S04 | 6 November 2025 | Propulsion alternatives and design/weight analysis |
| S05 | 6 November 2025 | 3.2 kg preliminary mass and motor sourcing |

<a id="s06"></a>

S06, 6 November 2025: motor-pod alternatives and the decision to simplify actuator protection.

<a id="s07-s08"></a>

| Reference | Date | Technical subject |
| --- | --- | --- |
| S07 | 13 November 2025 | 25GA-370 / 1360 RPM versus JGB37-550 / 680 RPM; total thrust target |
| S08 | 14 November 2025 | Available 6 × 4E propeller and loading estimates |

<a id="s09-s11"></a>

| Reference | Date | Technical subject |
| --- | --- | --- |
| S09 | 30 November 2025 | XPS/fiberglass body, mounts, approximate envelope and mass |
| S10 | 30 November 2025 | Hull alternatives, rotating propulsion, boosters and selection criteria |
| S11 | 30 November 2025 | Battery, regulator-powered servos and earlier electronics configuration |

<a id="s12-s15"></a>

| Reference | Date | Technical subject |
| --- | --- | --- |
| S12 | 20 December 2025 | Integrated ESP-NOW, four-IBT-2 and PCA9685 receiver |
| S13 | 20 December 2025 | Timed motion, camera feedback and target-loss behavior |
| S14 | 21 December 2025 | Mobile-camera processing and a proposed direct receiver interface |
| S15 | 21 December 2025 | Motor-only scope for the camera-following experiment |

<a id="s16"></a>

S16, 18 October 2026 UTC: technical clarification of PC/laptop YOLO/OpenCV detection, ESP32 commands and motor response in bench tests.

<a id="s17"></a>

S17, 30 October 2026: construction clarification covering XPS, hot glue and silicone actuator packaging; the final-round servo ingress failure; four 680 RPM propulsion motors; movement modes; approximate dimensions and the HydroBot result.

<a id="s18"></a>

S18: December 2025 project report, `proj_rep (4).pdf`. Construction photographs and design context are used alongside the implementation notes in [report cross-check](report-cross-check.md).

<a id="s19"></a>

S19: project photographs and videos. The [media index](../assets/build/README.md) gives original filenames, frame times and encoding details, including the eight development recordings added to the gallery.

<a id="s20"></a>

S20: [transmitter and receiver source](../firmware), [baseline hashes](../firmware/baseline.sha256) and the [nominal analysis](analysis.md).

## Interpreting the results

| Material | Engineering meaning |
| --- | --- |
| Budget, preliminary mass and thrust target | Planning values |
| Approximate dimensions and equipped mass | Prototype build values |
| Construction and operating videos | Visual record of fabrication and operation |
| Firmware and calculated command maps | Implemented channel mapping, timing and PWM behavior |
| Heading/PID plots | Nominal simulation results |
| PC/laptop vision tests | Bench verification of detection, commands and motor response |

The physical competition platform uses joystick RC control. The yaw model is a separate control study. On-water autonomous target following is a further validation stage of the vision extension.

Concept figures illustrate layouts and mechanisms. They are schematic, and their spacing does not specify manufacturing dimensions. Timeline dates identify design discussions and reviews.

## Propulsion calculations

Motor-selection exchanges included assistant-generated estimates based on assumed torque, loading and efficiency. These calculations informed the discussion of candidate parts and are treated as planning estimates.

For propeller testing, the International Towing Tank Conference's *Open Water Test*, procedure 7.5-02-03-02.1, revision 04 (2021), distinguishes thrust, torque, rotational rate and advance speed. Dividing shaft torque by propeller radius gives an equivalent tangential force; axial thrust requires the relevant propeller relationship or measurement.

[ITTC open-water procedure, §§2.1-2.2 and 3.2-3.3](https://www.ittc.info/media/11808/75-02-03-021.pdf)

## Figure sources

[Development milestones](../data/build_journey.json) supply the timeline and hull-concept figure. [generate_journey_figures.py](../tools/generate_journey_figures.py) and [generate_project_banner.py](../tools/generate_project_banner.py) produce editable SVG and PNG outputs. The [media index](../assets/build/README.md) credits photographs and footage.
