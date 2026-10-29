# Test and reproduction record

## Hardware baseline

Muhammad Ahmed confirmed on 30 October 2026 that all supplied controller firmware has been hardware-tested. The main transmitter and integrated receiver are preserved byte for byte in this repository. Their hashes are recorded in `firmware/baseline.sha256`.

The project video documents FOBO on water. The exact firmware revision, core/library versions and quantitative measurements corresponding to that clip were not recorded with it.

## Software checks added with the documentation

- CRC-8 reference check value and rejection of a corrupted packet.
- Signed little-endian packet layout and 21-byte payload size.
- Arduino integer-map behaviour, servo neutral/endpoints and command bounds.
- Motor neutral, full drive and opposite-direction turning examples.
- Stability, unit-reference convergence and constant-disturbance rejection of the nominal heading model.
- Regeneration of all command maps, figures and numerical data.

Run `python -m unittest discover -s tests -v`. These checks validate documentation tools and model properties; they do not replace physical tests.

The GitHub Actions workflow also defines reference ESP32 compilation using the versions in the build guide. Read its actual run result for compilation status; the presence of a workflow is not a passing build result.

## Recording a new hardware run

For a new result, record firmware commit, board/core/library versions, wiring changes, battery and supply configuration, test conditions, actual input and observed result. Use timestamped samples when reporting latency, tracking error or response time.

Published calculated datasets are labelled in their file headers and analysis notes. New measured datasets should state units and test conditions and be identified separately.

