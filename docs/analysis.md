# Calculated maps and nominal heading model

All data files in this repository are calculated or simulated. The physical firmware has been hardware-tested, but the source material did not include measured thrust, motor-speed, radio-latency or heading-response logs.

## Reproduction

Use Python 3.12:

```bash
python -m pip install -r requirements.txt
python tools/generate_figures.py
python -m unittest discover -s tests -v
```

To generate files somewhere else, pass `--output-dir PATH`. The generator reads the receiver's numeric constants and the MATLAB model parameters, records the receiver SHA-256, and exports CSV, JSON, PNG and SVG files.

## Servo command map

The map reproduces Arduino integer mapping, the channel deadband, 0–180° clipping, 600–2400 µs pulse conversion and 12-bit PCA tick conversion. All four outputs have the same command in the supplied source. Nominal examples are:

| CH2 | Angle command | Pulse | PCA ticks |
| --- | --- | --- | --- |
| −1000 | 0° | 600 µs | 123 |
| −500 | 40° | 1000 µs | 205 |
| 0 | 90° | 1500 µs | 307 |
| 500 | 140° | 2000 µs | 410 |
| 1000 | 180° | 2400 µs | 492 |

Arduino integer division truncates toward zero, so the sampled mapping has discrete steps. The graph's physical-angle interpretation depends on the servo calibration and mount.

## Motor command map

The plotted grid covers steering and throttle from −1000 to +1000 in 20-unit steps. Each cell applies the receiver's mode selection, motor deadband, saturation and integer conversion to 10-bit PWM. CSV columns represent motor groups 0/2 and 1/3.

A signed PWM value is a command; it is not a measured motor RPM, vehicle speed or propulsive force.

## Heading model

The plant and controller are:

$$G(s)=\frac{0.5}{s(0.8s+1)},\qquad C(s)=0.4s+3+\frac{0.8}{s}.$$

The reference transfer function is `CG/(1+CG)`. For a torque-like disturbance added after the controller at the plant input, the appropriate path is `G/(1+CG)`.

The common closed-loop denominator is `[0.8, 1.2, 1.5, 0.4]`. The reference numerator is `[0.2, 1.5, 0.4]`; the disturbance numerator is `[0.5, 0]`. The nominal closed-loop poles are approximately −0.5814 ± 1.0700j and −0.3372.

The heading plot uses a 45° reference, 0.025 s samples and a 20 s horizon. Its sampled overshoot is 33.73% and its sampled 2% settling time is 8.90 s. Settling time is the first sampled time after which the response remains in the ±2% band over that horizon.

The disturbance plot uses a zero reference and a 0.3 step in model-input units after five seconds. No calibrated conversion from those input units to the robot's physical motor torque is asserted.

## MATLAB and Simulink

`simulation/yaw_pid.m` preserves the nominal parameters and corrects the original disturbance test to `sys_dist = feedback(sys, C)`. The original version is retained in `archive/yaw_pid_original.m` for comparison.

The MATLAB script's default reference step is one radian; the Python figure instead uses 45°. Match the reference amplitude before comparing their numerical headings.

The supplied Simulink model records R2023a and uses the same P/I/D gains with derivative filter coefficient N=100. The MATLAB/Python model uses an ideal derivative. They are related nominal studies and should not be treated as numerically identical implementations.

The physical firmware has no heading sensor feedback and does not execute this PID controller. This simulation does not establish autonomous heading control on water.

