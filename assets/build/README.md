# FOBO build views and demonstrations

Construction photographs, development recordings and operating footage document the physical FOBO platform.

## Edited project reels

The earlier reel sources are:

- `FOBO_Crab_Walk_15s_Directors_Cut.mp4`
- `FOBO_15s_Vertical_Reel.mp4`

Both reels show the physical FOBO robot. They contain editing, captions and shot changes. Their titles are not a measurement of any specific manoeuvre, and the footage is not a time-synchronised firmware log.

| Repository file | Source and processing |
| --- | --- |
| `pool-and-outdoor-demo.mp4` | First reel; resized to 432 pixels wide, 15 fps, H.264; audio omitted |
| `outdoor-demo.mp4` | Second reel; resized to 432 pixels wide, 15 fps, H.264; audio omitted |
| `pool-closeup.jpg` | First reel at approximately 0.8 s |
| `pool-overview.jpg` | First reel at approximately 14.1 s |
| `outdoor-three-quarter.jpg` | Second reel at approximately 2.7 s |

The first three reel stills are resized to 640 pixels wide. `fobo-hero.jpg` is a full-resolution frame at 14.1 s of the first reel. These reel stills retain their captions. The repository cover uses the separate vector project banner, and the main pool photograph comes from the development recordings below.

## Original uploaded footage

The following excerpts preserve the selected shot's timing and omit audio. They are resized, encoded as H.264 at 15 fps and labelled as excerpts rather than full recordings.

| Repository file | Original source | Source interval |
| --- | --- | --- |
| `pool-maneuvering.mp4` | `1000167338.mp4` | 0–8 s, 640 pixels wide |
| `pool-ball-approach.mp4` | `1000167343.mp4` | 6–15 s, 360 pixels wide |
| `pool-soccer-contact.mp4` | `1000167344.mp4` | 8–19 s, 360 pixels wide |
| `pool-rear-view.jpg` | `1000167342.mp4` | Frame near 7.8 s |
| `pool-ball-contact.jpg` | `1000167344.mp4` | Frame near 14.1 s |
| `team-at-event.jpg` | `1000167295.mp4` | Frame near 2 s |
| `outdoor-trial-original.mp4` | `1000165287.mp4` | 0–12 s, 432 pixels wide, H.264 at 15 fps, audio omitted |
| `outdoor-trial-closeup.jpg` | `1000165135.mp4` | Full-resolution frame near 1.2 s |

Additional supplied recordings `1000167339.mp4`, `1000167340.mp4`, `1000167341.mp4` and `1000167345.mp4` contain related pool/event views. The selected excerpts keep the gallery focused on the robot; the source recordings remain separate from this repository.

## Construction photographs

`xps-hull-shaping.png`, `xps-twin-hull-top.png` and `xps-twin-hull-angle.png` are the three foam-stage photographs embedded in PDF page 49 of the supplied `proj_rep (4).pdf`. `fiberglass-layup-1.jpg` through `fiberglass-layup-3.jpg` are its three related fiberglass-work photographs. Embedded image bytes are preserved; no construction stages or components have been generated.

See the [implementation notes](../../docs/report-cross-check.md) for the relationship between the project report and the published controller.

The mechanical-layout, propulsion-mode and actuator-packaging figures in `assets/figures/` are explanatory drawings based on the project's construction account. They are distinct from these photographs of the actual robot. No hardware has been added to or removed from the photographs.

## Development recordings

Eight complete video streams cover foam shaping, flotation, motor packaging, propulsion assembly, launch, outdoor trials and the competition pool. Playback copies use H.264 at 24 fps, a maximum dimension of 1080 pixels and no audio. Source and published hashes, dimensions and frame times are in [development/manifest.json](development/manifest.json).

| Repository recording | Original source | Duration | Still source time |
| --- | --- | --- | --- |
| [foam-shaping.mp4](development/foam-shaping.mp4) | `1000157544.mp4` | 10.5 s | 1.3 s |
| [hull-load-check.mp4](development/hull-load-check.mp4) | `1000158944.mp4` | 7.1 s | 3.5 s |
| [motor-packaging.mp4](development/motor-packaging.mp4) | `1000159221.mp4` | 6.8 s | 5.6 s |
| [propulsion-bench.mp4](development/propulsion-bench.mp4) | `1000162797.mp4` | 5.6 s | 2.7 s |
| [launch-trial.mp4](development/launch-trial.mp4) | `1000163629.mp4` | 4.7 s | 3.8 s |
| [open-water-trial.mp4](development/open-water-trial.mp4) | `1000164522.mp4` | 80.3 s | 9.6 s |
| [open-water-run.mp4](development/open-water-run.mp4) | `1000166073.mp4` | 45.1 s | 5.4 s |
| [competition-run.mp4](development/competition-run.mp4) | `1000166422.mp4` | 20.1 s | 2.4 s |

Stills use frames extracted from the original recordings at the listed times. The [gallery](../../docs/gallery.md) places them with the corresponding build stages.
