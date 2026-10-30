# Journey sources and recovery record

The [engineering journey](build-journey.md) and [decision log](decision-log.md) were reconstructed on **30 October 2026**. This register identifies the basis of the narrative and the limits of what has been recovered.

Earlier conversations were retrieved as attributed, dated excerpts and summaries, **not as a complete raw chat export with every attachment**. The dates below are source-record dates. They are not automatically construction or test dates. Historical discussion dates and times use UTC; an evening UTC exchange can fall on the following date in Pakistan.

Public documentation includes relevant project facts and short source descriptions. It does not publish whole private conversations or unrelated personal material. Reconstructed diagrams are labelled as new illustrations, not original notebook pages.

## Evidence types

| Type | Meaning in this reconstruction |
| --- | --- |
| Builder report | Ahmed's account of a choice, construction detail or result; retrospective when stated later |
| Assistant proposal | Advice or a calculation supplied in the conversation; implementation requires separate evidence |
| Preserved source | Directly inspectable firmware or analysis behavior |
| Photo / video | Evidence of what is visible; it does not establish unrecorded measurements or exact code revision |
| Project report | A useful secondary record, supplied with an explicit accuracy caveat |
| Current interpretation | Analysis written during reconstruction; not attributed to the team's past thoughts |

<a id="s01-s05"></a>

## S01–S05 — 6 November 2025: mission and feasibility

| ID | Record and attribution | Material used |
| --- | --- | --- |
| S01 | User, 16:59:12 UTC; assistant, 16:59:35 | Planning-stage dual catamaran, two-square-foot constraint, rectangular-versus-square question. Assistant proposed 24 × 12 in, narrow twin hulls, draft and a rough displacement estimate. The proposal is not the as-built drawing. |
| S02 | User, 17:03:16; assistant, 17:03:39 | Directional control, torque, precision and speed for water soccer. Assistant offered a more elaborate main/lateral-thruster and control architecture. |
| S03 | User, 17:11:38 | Maximum planning budget $150–200; advanced equipment outside the available means; suitable waterproof motors unavailable; proposed four servo-rotatable corner motors. |
| S04 | User, 17:22:58 | Rejected water pumps as the solution and wanted design/weight analysis before motor selection. |
| S05 | User, 17:29:07 | 3.2 kg planning mass and a request to search for obtainable motors. This is not a final measured mass. |

<a id="s06"></a>

## S06 — 6 November 2025: waterproofing complexity

The assistant's **18:45:45 UTC** proposal described a tube-based motor pod with shaft supports, sealing elements, hatch and cable interfaces. At **18:47:27**, Ahmed rejected the complexity and requested a simpler approach. A bottle/PVC housing was then suggested.

These discussions establish the complexity objection and alternative advice. The implemented XPS/glue/silicone method comes from S17, not from treating either proposed pod as an actual build.

<a id="s07-s08"></a>

## S07–S08 — 13–14 November 2025: motor and propeller discussions

| ID | Record and attribution | Material used |
| --- | --- | --- |
| S07 | 13 November, user questions around 09:22:53 and 09:28:38 UTC; selection discussion around 09:26 | 25GA-370 12 V / 1360 RPM compared with JGB37-550 12 V / 680 RPM; roughly 6 kgf total thrust goal. Earlier wording about per-motor and total targets was inconsistent. No thrust measurement was supplied. |
| S08 | 14 November, user at 14:12:40; assistant estimates around 14:13–14:16 | User had a 6 × 4E propeller and asked about thrust. Assistant gave changing, assumption-dependent estimates and recommended testing. Neither the exact final propeller nor achieved thrust follows from this exchange. |

<a id="s09-s11"></a>

## S09–S11 — 30 November 2025: build and design retrospective

| ID | Record and attribution | Material used |
| --- | --- | --- |
| S09 | User, 13:58:10 UTC | Dual hull, 23 × 17 × 13 in stated envelope alongside an inconsistent 18 in cube constraint; three main fiberglass layers, locally six; XPS/fiberglass central bay; mounts; four rotating MG996R units; two rear boosters; about 2.5 kg bare and 4.5–5 kg equipped. |
| S10 | User, 14:09:49 | Flat baseline, V-shaped and catamaran concepts; two thrusters plus turning mechanism → four fixed → four rotatable; boosters for pushing/fallback; approximately 300 g per motor; lighter high-thrust options unaffordable; cost, stability, maneuverability, thrust, weight and requirements fit. Ahmed says paper sketches exist. No original scan accompanies the recovered excerpt. |
| S11 | User, 15:28:52 | Electronics account names L298N, 3S 2200 mAh, regulator-powered MG996R servos, organized wiring and a power-distribution-diagram request. Precise relationship to the later IBT-2 source is unresolved. |

The assistant subsequently drafted report sections, diagrams/placeholders and comparative language. These outputs do not independently establish measured hull superiority, completed PID hardware or numerical decision weights.

<a id="s12-s15"></a>

## S12–S15 — 20–21 December 2025: controller and camera extension

| ID | Record and attribution | Material used |
| --- | --- | --- |
| S12 | User, 20 December, 16:18:01 UTC | Shared integrated ESP32 receiver with ESP-NOW, CRC, four IBT-2 outputs, PCA9685 and 300 ms failsafe. Date of source discussion, not established first commissioning. |
| S13 | User, 20 December, 16:04:29, 16:08:46 and 16:25:06; assistant, 16:20:47 | One-day Python extension constraint, no dedicated sensors available, trajectory/point-following interest and camera/target-loss questions. Assistant explained timed open-loop motion and proposed camera feedback alternatives. |
| S14 | User/assistant, 21 December, around 16:49 | Onboard phone as vision source/processor and a proposed direct link to the receiver. Assistant suggestions included colored-target tracking, command updates, smoothing and stopping on target loss; receiver input changes were required. |
| S15 | User, 21 December, 16:52:08 and 16:53:36 | Narrowed that follow-on experiment to practical motor-only control without the servo setup. This is not evidence that servos were absent from the competition robot. |

<a id="s16"></a>

## S16 — 18 October 2026: vision test scope

The user messages at **21:02:53, 21:03:45 and 21:04:35 UTC** on 18 October (19 October in Pakistan) identify PC/laptop YOLO/OpenCV target detection, commands to ESP32 and motor response as bench-tested. They do not establish autonomous following in water. The original runnable implementation and precise phone-versus-PC revision sequence remain unrecovered. See [vision extension](vision-extension.md).

<a id="s17"></a>

## S17 — 30 October 2026: builder clarification

Ahmed directly confirmed the construction sequence and actual low-cost protection method: shape XPS, cover with fiberglass; place ordinary motors in motor-sized foam cavities with only their shafts outside; use hot glue and silicone around the bodies; place servos in servo-sized XPS cavities and seal similarly.

He reported water entering one servo during the final round and stopping it, with the protection otherwise working well through the project. He confirmed four 680 RPM motors/four propellers, rotating mounts, common forward/reverse drive, lateral vectoring and opposing-drive pivot turns. The report's dimensions were confirmed as approximate, with roughly 1–2 in variation. He also confirmed the 1st-of-64 competition result and requested the later camera/OpenCV work be included.

This is a **retrospective builder account**. It does not date the fabrication steps, the competition final or the failure to 30 October 2026.

<a id="s18"></a>

## S18 — Supplied December 2025 report

The 50-page `proj_rep (4).pdf`, created 1 December 2025, supplies construction photographs and a broader project narrative. Ahmed cautioned that some content may be inaccurate. Its creation date does not date every event described inside it.

The report also uses the project name “Black panther.” That is a source-name difference, not evidence of a separate manufactured robot. The repository follows Ahmed's current FOBO/HydroBot naming.

The [report cross-check](report-cross-check.md) records conflicts involving dimensions, driver hardware, battery descriptions, PID/IMU implementation, independent servo commands, packet details, performance and waterproofing. The personal cover page and full report have not been republished.

### Report-only manufacturing leads

The manufacturing chapter lists repeated fiberglass work, difficulty avoiding silicone bubbles, cable routing through the hull, and alignment of rotating mounts. It also gives a detailed assembly order and curing schedule. These are retained as leads for confirmation, because the supplied report includes known inaccuracies and matching dated builder accounts have not been recovered for these particular items.

The public narrative therefore does not invent how many failed fiberglass attempts occurred, which wire leaked, a repair sequence, a measured vibration problem, or an exact curing process.

<a id="s19"></a>

## S19 — Physical photographs and operating footage

The [gallery](gallery.md) and [media provenance](../assets/build/README.md) identify photographs recovered from the report and frames/excerpts from Ahmed's supplied videos. They corroborate the XPS/fiberglass body and show the physical project operating in water, rear propellers, ball interaction and the team display.

No capture-time log ties every clip to a specific firmware revision. Footage does not provide calibrated speed, thrust, runtime, range or ingress measurements. Report renders and placeholder illustrations are not original sketches or proof of manufactured alternatives.

<a id="s20"></a>

## S20 — Preserved firmware and analysis

The transmitter and integrated receiver are the hardware-tested files supplied by Ahmed, with hashes in [firmware/baseline.sha256](../firmware/baseline.sha256). Their behavior is directly inspectable. Reference compilation is documented in [validation](validation.md).

The nominal heading/PID analysis is a separate study with assumed plant parameters. It is not evidence that an IMU/PID loop ran on the competition robot. Compilation proves a reference build, not an additional water trial.

## What the assistant contributed and what was corrected

| Advice/output recovered | Use in the journey | Audit result |
| --- | --- | --- |
| Rectangular hull layout and buoyancy estimate | Shows the early design conversation | Assumed dimensions/draft; not final displacement validation |
| Commercial thrusters, advanced control and sensing | Shows the proposals constrained by budget | Not treated as purchased or installed |
| Tube-based pod, then bottle/PVC alternative | Documents the response to a complexity objection | Actual confirmed method was XPS, hot glue and silicone |
| Motor/propeller thrust estimates | Documents questions and changing advice | No matching measured thrust/current/RPM data |
| Report prose and decision-matrix suggestions | Helps locate design topics | No invented numerical weights or comparative tests |
| Timed trajectory and camera-tracking proposals | Explains later extension options | Suggestions separated from the confirmed bench-test scope |
| Report claims of PID/IMU, high performance and full waterproofing | Cross-checked against source and builder clarification | Removed from physical-performance claims or corrected |

Some old motor advice used assumed torque and propeller radius to suggest thrust and then applied ad hoc loading/efficiency factors. Other replies changed the estimate substantially. For example, the 14 November discussion moved from roughly **1.3–1.6 kgf per motor** to a conservative range of approximately **0.435–1.251 kgf per motor**. These are historical assistant outputs, **not measurements, confidence bounds or a validated FOBO prediction**. Repeating the exact decimals as an experimental result would misrepresent the record.

For a current technical reference, the International Towing Tank Conference's *Open Water Test*, procedure **7.5-02-03-02.1**, revision 04 (2021), defines thrust and torque coefficients using thrust, torque, water density, rotational rate and propeller diameter; its measurement section includes thrust, torque, RPM and advance speed. Dividing shaft torque by propeller radius gives an equivalent tangential force, rather than establishing axial thrust. The old advice did not supply a validated relationship between those quantities. This audit does not validate the estimates or imply that the FOBO team followed the procedure. [ITTC primary reference, §§2.1–2.2 and 3.2–3.3](https://www.ittc.info/media/11808/75-02-03-021.pdf).

## Original handwriting and coverage gaps

Ahmed explicitly mentioned paper sketches on 30 November and now recalls handwritten uploads. Searches of the available FOBO/HydroBot build history and accessible project files **have not recovered those original image attachments or their file identifiers**. The report's concept illustrations do not fill that gap. Newly drawn diagrams are not presented as his handwriting.

| Material sought | Current coverage |
| --- | --- |
| September–October 2025 FOBO build conversations | No matching dated FOBO discussions recovered |
| 6 November planning and 13–14 November propulsion discussion | Attributed dated excerpts/summaries recovered |
| Other November fabrication/debug sessions | No distinct additional dated records recovered beyond the 30 November retrospective |
| Original paper sketches / handwritten calculations | Their existence is reported; original attachments unrecovered |
| Assistant's complete responses and every code revision | Selected attributed outputs recovered; no full export |
| Physical fabrication and competition dates | Sequence partly known; exact dates unrecovered |
| Rule sheet and inspection dimensions | Unrecovered; conflicting constraints remain open |
| Full cost and component mass ledger | Unrecovered; planning budget and some reported masses available |
| Thrust/current/RPM, ingress-duration and comparative hull tests | No matching measurement logs recovered |
| Servo teardown and exact ingress path | Unrecovered |
| L298N → IBT-2 transition and booster harness | Unresolved |
| Original vision scripts and receiver changes | Unrecovered |

A FOBO-specific chat export with its attachments, or the original notebook images, would allow the handwritten portion and missing exchanges to be added accurately. This account is a sourced reconstruction of the recovered record, not a claim that every conversation and upload has been found.

The timeline is generated from [data/build_journey.json](../data/build_journey.json) by [tools/generate_journey_figures.py](../tools/generate_journey_figures.py). Visual spacing is categorical rather than elapsed-time scale. The competition outcome is shown without an invented event date.
