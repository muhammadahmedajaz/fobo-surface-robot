# Test and reproduction record

## Hardware baseline

The transmitter and integrated receiver are the hardware-tested project firmware. Their SHA-256 hashes are recorded in `firmware/baseline.sha256`.

Operating footage documents the physical platform in outdoor and competition water trials. The [media index](../assets/build/README.md) identifies the source recordings and excerpts.

## Software verification

The repository checks:

- CRC-8 reference value and rejection of a corrupted packet.
- Signed little-endian packet layout and the 21-byte payload.
- Arduino integer mapping, servo neutral/endpoints and command bounds.
- Motor neutral, full drive and opposing-drive turning.
- Stability, reference convergence and disturbance rejection of the nominal heading model.
- Regeneration of command maps, figures and numerical data.

Run `python -m unittest discover -s tests -v`.

GitHub Actions compiles both ESP32 sketches using the reference versions in the [build guide](build-guide.md), runs the analysis checks and regenerates the figures.

## Figures and media

The development timeline uses design-review dates from `data/build_journey.json`. Hull and component layouts are conceptual illustrations. Generate them with `tools/generate_journey_figures.py`, `tools/generate_mechanical_layout.py` and `tools/generate_project_banner.py`.

The [media index](../assets/build/README.md) records source filenames, selected intervals, frame times and encoding details for the construction photographs and operating clips.

Command maps describe software outputs. Heading plots describe nominal simulations. The [vision tests](vision-extension.md) cover bench detection, ESP32 commands and motor response.

## Recording a hardware run

Record the firmware commit, board/core/library versions, wiring, power configuration, test conditions, input and observed result. Timestamped samples support latency, tracking-error and response-time measurements.

Measured datasets should state units and test conditions. Keep them identifiable alongside calculated command maps and simulation outputs.

