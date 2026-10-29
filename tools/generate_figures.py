"""Reproduce FOBO's documented command maps and nominal heading simulations.

Firmware is read, never modified. CSV outputs are calculated/simulated data.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import numpy as np
from scipy import signal

ROOT = Path(__file__).resolve().parents[1]
BLUE, TEAL, ORANGE, INK = "#22577a", "#087f8c", "#d96c2c", "#182b3a"
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 11,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.labelcolor": INK, "text.color": INK,
    "axes.titlesize": 15, "axes.titleweight": "bold",
    "grid.color": "#dce4e8", "grid.linewidth": 0.6,
    "figure.facecolor": "white", "savefig.facecolor": "white",
    "svg.fonttype": "none", "svg.hashsalt": "fobo-2026",
})


def scalar(source: str, name: str) -> float:
    match = re.search(r"(?:const\s+int\s+)?\b" + re.escape(name) + r"\s*=\s*([-+0-9.]+)\s*;", source)
    if match is None:
        raise ValueError(f"Missing numeric parameter: {name}")
    return float(match.group(1))


def parameters() -> dict:
    rx_path = ROOT / "firmware/receiver/receiver.ino"
    rx = rx_path.read_text()
    for output in ("fl", "fr", "rl", "rr"):
        expected = rf"int\s+{output}\s*=\s*constrain\(SERVO_CENTER\s*\+\s*offsetDeg,\s*0,\s*180\)"
        if re.search(expected, rx) is None:
            raise ValueError("Servo expressions changed; update the analysis model before regenerating.")
    sim = (ROOT / "simulation/yaw_pid.m").read_text()
    names = ["SERVO_FREQ", "SERVOMIN_US", "SERVOMAX_US", "SERVO_CENTER", "SERVO_MAX_OFFSET", "JOYSTICK_DEAD", "TURN_THRESHOLD", "LEDC_RES", "LEDC_FREQ"]
    return {
        "firmware": {name: int(scalar(rx, name)) for name in names},
        "heading": {name: scalar(sim, name) for name in ["K", "T", "Kp", "Ki", "Kd"]},
        "receiver_sha256": hashlib.sha256(rx_path.read_bytes()).hexdigest(),
        "source": "Supplied hardware-tested receiver; command maps are calculated, not measured.",
        "model_status": "Nominal linear simulation; parameters have not been identified from water-test data.",
    }


def arduino_map(value: int, lo: int, hi: int, out_lo: int, out_hi: int) -> int:
    numerator = (int(value) - lo) * (out_hi - out_lo)
    denominator = hi - lo
    quotient = abs(numerator) // abs(denominator)
    if (numerator < 0) != (denominator < 0):
        quotient = -quotient
    return quotient + out_lo


def servo_command(channel: int, cfg: dict) -> tuple[int, int, int]:
    ch = 0 if abs(channel) < 20 else channel
    offset = arduino_map(ch, -1000, 1000, -cfg["SERVO_MAX_OFFSET"], cfg["SERVO_MAX_OFFSET"])
    angle = min(180, max(0, cfg["SERVO_CENTER"] + offset))
    pulse = arduino_map(angle, 0, 180, cfg["SERVOMIN_US"], cfg["SERVOMAX_US"])
    ticks = math.floor(pulse * cfg["SERVO_FREQ"] * 4096 / 1_000_000 + 0.5)
    return angle, pulse, min(4095, max(0, ticks))


def motor_commands(steer: int, throttle: int, cfg: dict) -> tuple[int, int]:
    dead = cfg["JOYSTICK_DEAD"]
    steer = 0 if abs(steer) < dead else steer
    throttle = 0 if abs(throttle) < dead else throttle
    if abs(steer) > abs(throttle) and abs(steer) > cfg["TURN_THRESHOLD"]:
        magnitude = arduino_map(abs(steer), 0, 1000, 200, 1000)
        group_a, group_b = (-magnitude, magnitude) if steer > 0 else (magnitude, -magnitude)
    else:
        group_a = group_b = throttle

    def duty(speed: int) -> int:
        speed = max(-1000, min(1000, speed))
        if abs(speed) <= dead:
            return 0
        magnitude = arduino_map(abs(speed), 0, 1000, 0, (1 << cfg["LEDC_RES"]) - 1)
        return magnitude if speed > 0 else -magnitude
    return duty(group_a), duty(group_b)


def heading_systems(cfg: dict):
    g_num, g_den = [cfg["K"]], [cfg["T"], 1, 0]
    c_num, c_den = [cfg["Kd"], cfg["Kp"], cfg["Ki"]], [1, 0]
    denominator = np.polyadd(np.polymul(c_den, g_den), np.polymul(c_num, g_num))
    reference = signal.TransferFunction(np.polymul(c_num, g_num), denominator)
    disturbance = signal.TransferFunction(np.polymul(g_num, c_den), denominator)
    return reference, disturbance, denominator


def save(fig, folder: Path, name: str):
    fig.savefig(folder / f"{name}.png", dpi=160, bbox_inches="tight", metadata={"Software": "FOBO reproducible analysis"})
    fig.savefig(folder / f"{name}.svg", bbox_inches="tight", metadata={"Date": None, "Creator": "FOBO reproducible analysis"})
    plt.close(fig)


def footnote(fig, text: str):
    fig.text(0.08, 0.012, text, fontsize=9, color="#5b6d77")


def card(ax, x, y, w, h, title, body="", color=BLUE, fontsize=10):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.012,rounding_size=0.018", linewidth=1.4, edgecolor=color, facecolor="#f4f8fa"))
    ax.text(x+w/2, y+h-0.045, title, ha="center", va="top", fontsize=fontsize+1, fontweight="bold", color=color)
    if body:
        ax.text(x+w/2, y+h/2-0.02, body, ha="center", va="center", fontsize=fontsize, linespacing=1.45)


def arrow(ax, start, end, label="", color="#5b6d77", offset=(0, 0.02)):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=13, linewidth=1.4, color=color))
    if label:
        ax.text((start[0]+end[0])/2+offset[0], (start[1]+end[1])/2+offset[1], label, fontsize=9, ha="center", color=color)


def diagrams(folder: Path):
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set(xlim=(0, 1), ylim=(0, 1)); ax.axis("off")
    ax.text(0.02, 0.96, "FOBO | control architecture", fontsize=20, fontweight="bold")
    card(ax, .02, .37, .16, .32, "Hand controller", "2 joysticks\n3 buttons\nESP32 transmitter")
    card(ax, .25, .37, .18, .32, "Radio frame", "ESP-NOW\n8 channels + CRC-8\n21 bytes | nominal 100 Hz")
    card(ax, .50, .37, .19, .32, "ESP32 receiver", "Size + CRC check\nMotor mixing / servo map\nLink timeout gate")
    card(ax, .77, .59, .20, .26, "4 × IBT-2", "8 PWM signals\n4 bidirectional DC motors", color=TEAL)
    card(ax, .77, .16, .20, .28, "PCA9685", "I²C on GPIO 32 / 33\nOutputs 0–3 → 4 servos\n50 Hz", color=ORANGE)
    arrow(ax, (.18,.53),(.25,.53))
    arrow(ax, (.43,.53),(.50,.53))
    arrow(ax, (.69,.60),(.77,.70), "CH0/1", offset=(0,.04))
    arrow(ax, (.69,.44),(.77,.30), "CH2", offset=(0,-.055))
    ax.text(.02,.14,"Inactive link / failsafe: zero motor PWM and servo centres at 90°.", fontsize=11)
    footnote(fig,"Hardware-tested RC firmware; 21-byte ESP-NOW frames. Radio rate shown is the scheduled value.")
    save(fig,folder,"control_architecture")

    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set(xlim=(0,1),ylim=(0,1)); ax.axis("off")
    ax.text(.02,.96,"FOBO | receiver signal wiring",fontsize=20,fontweight="bold")
    card(ax,.03,.25,.23,.58,"ESP32 receiver","Motor PWM pairs\n\nGPIO 25 / 26\nGPIO 27 / 14\nGPIO 23 / 22\nGPIO 21 / 17\n\nI²C: SDA 32 / SCL 33")
    rows=[(.76,"Motor index 0","GPIO 25 → RPWM  |  26 → LPWM"),(.60,"Motor index 1","GPIO 27 → RPWM  |  14 → LPWM"),(.44,"Motor index 2","GPIO 23 → RPWM  |  22 → LPWM"),(.28,"Motor index 3","GPIO 21 → RPWM  |  17 → LPWM")]
    for y,title,body in rows:
        card(ax,.40,y,.55,.125,title,body,color=TEAL,fontsize=10)
        arrow(ax,(.26,y+.062),(.40,y+.062))
    card(ax,.40,.04,.25,.14,"PCA9685 | 0x40","SDA 32 / SCL 33",color=ORANGE)
    card(ax,.73,.04,.22,.14,"Servo outputs","0 FL · 1 FR · 2 RL · 3 RR",color=ORANGE,fontsize=9)
    arrow(ax,(.22,.25),(.40,.11),"I²C",offset=(-.015,-.005))
    arrow(ax,(.65,.11),(.73,.11))
    footnote(fig,"Signal mapping only. Match motor indices to your physical installation; enable inputs and power rails are documented in docs/build-guide.md.")
    save(fig,folder,"receiver_wiring")

    fig, ax = plt.subplots(figsize=(14, 6))
    ax.set(xlim=(0,1),ylim=(0,1)); ax.axis("off")
    ax.text(.02,.96,"FOBO | power domains for replication",fontsize=20,fontweight="bold")
    card(ax,.02,.36,.18,.30,"Motor battery","Original build: 3S LiPo\nNominal 11.1 V")
    card(ax,.32,.66,.25,.20,"Motor-power branch","IBT-2 B+ / B−",color=TEAL)
    card(ax,.32,.37,.25,.20,"Servo regulator","5–6 V output\nSize for installed servo load",color=ORANGE)
    card(ax,.32,.08,.25,.20,"Logic regulator","5 V output\nBoard-appropriate ESP32 input")
    card(ax,.72,.66,.25,.20,"Motor drivers","Motor supply → four motors",color=TEAL)
    card(ax,.72,.37,.25,.20,"Servo power","PCA9685 V+ → servo rail",color=ORANGE)
    card(ax,.72,.08,.25,.20,"Logic power","ESP32 3.3 V → PCA9685 VCC\nIBT-2 logic: follow module guide",fontsize=9)
    for y in [.76,.47,.18]:
        arrow(ax,(.20,.51),(.32,y)); arrow(ax,(.57,y),(.72,y))
    ax.text(.02,.025,"Common signal ground across ESP32, PCA9685 and motor-driver logic.",fontsize=10,fontweight="bold")
    footnote(fig,"Reference power arrangement, not an as-built schematic. Original regulator/current ratings and connector wiring were not recorded.")
    save(fig,folder,"power_domains")


def generate(out: Path) -> dict:
    p=parameters(); cfg=p["firmware"]
    figures, data=out/"assets/figures",out/"data"
    figures.mkdir(parents=True,exist_ok=True); data.mkdir(parents=True,exist_ok=True)
    (data/"parameters.json").write_text(json.dumps(p,indent=2)+"\n")
    channels=np.arange(-1000,1001)
    mapping=np.array([servo_command(int(ch),cfg) for ch in channels])
    np.savetxt(data/"servo_command_map.csv",np.column_stack([channels,mapping]),delimiter=",",header="channel_2,command_angle_deg,pulse_us,pca9685_ticks",comments="",fmt="%d")
    fig,ax=plt.subplots(figsize=(10,5.6))
    ax.plot(channels,mapping[:,0],color=TEAL,lw=2.5,label="All four servo commands")
    ax.axhline(90,color="#8799a3",ls="--",lw=1)
    ax.set(title="Servo vectoring | calculated command map",xlabel="Channel 2 command",ylabel="Commanded angle (degrees)",ylim=(-5,185),yticks=[0,45,90,135,180])
    ax.grid(alpha=.8);ax.legend(loc="upper left",frameon=False)
    secondary=ax.secondary_yaxis("right",functions=(lambda angle:600+10*angle,lambda pulse:(pulse-600)/10))
    secondary.set_ylabel("Nominal pulse width (µs)")
    fig.tight_layout(rect=(0,.05,1,1));footnote(fig,"Calculated from receiver.ino. Physical travel depends on servo calibration and mounting.")
    save(fig,figures,"servo_command_map")

    values=np.arange(-1000,1001,20)
    a=np.zeros((len(values),len(values)));b=np.zeros_like(a);rows=[]
    for yi,throttle in enumerate(values):
        for xi,steer in enumerate(values):
            a[yi,xi],b[yi,xi]=motor_commands(int(steer),int(throttle),cfg)
            rows.append([steer,throttle,int(a[yi,xi]),int(b[yi,xi])])
    np.savetxt(data/"motor_command_map.csv",rows,delimiter=",",header="steer_ch0,throttle_ch1,signed_pwm_motors_0_2,signed_pwm_motors_1_3",comments="",fmt="%d")
    fig,axes=plt.subplots(1,2,figsize=(12,5.5),sharey=True,layout="constrained")
    for ax,arr,label in zip(axes,[a,b],["Motor indices 0 and 2","Motor indices 1 and 3"]):
        im=ax.imshow(arr,origin="lower",extent=[-1000,1000,-1000,1000],vmin=-1023,vmax=1023,cmap="RdBu",aspect="equal",interpolation="nearest")
        ax.set(title=label,xlabel="Steering channel 0")
    axes[0].set_ylabel("Throttle channel 1")
    fig.suptitle("Motor mixing | calculated signed PWM commands",fontsize=17,fontweight="bold")
    fig.colorbar(im,ax=axes,label="Signed PWM duty (−1023 to +1023)",shrink=.80)
    fig.supxlabel("Calculated from control logic; PWM duty is not measured motor speed.",fontsize=9,color="#5b6d77")
    save(fig,figures,"motor_command_map")

    ref,dist,den=heading_systems(p["heading"])
    t=np.arange(0,20.0001,.025);r=np.full_like(t,np.pi/4)
    _,y,_=signal.lsim(ref,r,t)
    np.savetxt(data/"heading_step_response.csv",np.column_stack([t,r,y,r-y]),delimiter=",",header="time_s,reference_rad,simulated_heading_rad,error_rad",comments="",fmt="%.9g")
    fig,ax=plt.subplots(figsize=(10,5.6))
    ax.plot(t,np.rad2deg(r),color=INK,ls="--",lw=1.4,label="45° reference")
    ax.plot(t,np.rad2deg(y),color=TEAL,lw=2.3,label="Nominal PID model")
    ax.set(title="Heading tracking | nominal linear simulation",xlabel="Time (s)",ylabel="Heading (degrees)")
    ax.grid(alpha=.8);ax.legend(frameon=False,loc="lower right")
    fig.tight_layout(rect=(0,.05,1,1));footnote(fig,"Model K=0.5, T=0.8; ideal PID Kp=3, Ki=0.8, Kd=0.4. These are simulation results, not water-test measurements.")
    save(fig,figures,"heading_step_response")

    disturbance=np.where(t>5,.3,0.)
    _,dy,_=signal.lsim(dist,disturbance,t)
    np.savetxt(data/"disturbance_rejection.csv",np.column_stack([t,disturbance,dy]),delimiter=",",header="time_s,plant_input_disturbance_model_units,simulated_heading_deviation_rad",comments="",fmt="%.9g")
    fig,axes=plt.subplots(2,1,figsize=(10,6.4),sharex=True,gridspec_kw={"height_ratios":[1,2]})
    axes[0].plot(t,disturbance,color=ORANGE,lw=2)
    axes[0].set(title="Plant-input disturbance | nominal linear simulation",ylabel="Disturbance\n(model units)")
    axes[1].plot(t,np.rad2deg(dy),color=TEAL,lw=2.3)
    axes[1].axhline(0,color="#8799a3",ls="--",lw=1)
    axes[1].set(xlabel="Time (s)",ylabel="Heading deviation (degrees)")
    for ax in axes:ax.grid(alpha=.8)
    fig.tight_layout(rect=(0,.05,1,1));footnote(fig,"Zero reference; disturbance enters after the controller. Response uses G/(1+CG), not the reference transfer function.")
    save(fig,figures,"disturbance_rejection")
    diagrams(figures)
    target=np.pi/4
    overshoot=max(0.,(float(np.max(y))-target)/target*100)
    outside=np.flatnonzero(np.abs(y-target)>.02*target)
    settling=None if len(outside) and outside[-1]==len(t)-1 else float(t[outside[-1]+1]) if len(outside) else 0.
    metrics={"status":"Calculated nominal-model results; not hardware measurements.","reference_deg":45,"overshoot_percent":overshoot,"sampled_2pct_settling_time_s":settling,"horizon_s":20,"sample_interval_s":.025,"closed_loop_poles":[{"real":float(x.real),"imag":float(x.imag)} for x in np.roots(den)]}
    (data/"simulation_metrics.json").write_text(json.dumps(metrics,indent=2)+"\n")
    return metrics


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir",type=Path,default=ROOT)
    args=parser.parse_args()
    print(json.dumps(generate(args.output_dir.resolve()),indent=2))
