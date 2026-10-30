"""Draw the repository cover as editable vector artwork.

The propulsion layout is a conceptual top view. Operating photographs are
published separately in assets/build and retain their original hardware detail.
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, Rectangle, Arc
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def draw():
    plt.rcParams.update({"font.family": "DejaVu Sans", "svg.fonttype": "none",
                         "svg.hashsalt": "fobo-cover-2026"})
    bg, white, muted = "#101d27", "#f5f7f8", "#a9bbc6"
    red, teal, edge = "#d94955", "#5ac6c5", "#91a8b7"
    fig, ax = plt.subplots(figsize=(14, 6.2))
    fig.patch.set_facecolor(bg)
    ax.set(xlim=(0, 14), ylim=(0, 6.2))
    ax.axis("off")
    for x in np.arange(8.1, 14, .36):
        for y in np.arange(.85, 5.5, .36):
            ax.plot(x, y, ".", color="#233744", ms=2, zorder=0)
    ax.plot([.65, 1.14], [5.48, 5.48], color=red, lw=3)
    ax.text(1.33, 5.48, "SURFACE ROBOTICS / ENGINEERING CASE STUDY", fontsize=10.5,
            color=muted, va="center", weight="bold")
    ax.text(.58, 4.13, "FOBO", fontsize=78, weight="bold", color=white)
    ax.text(.68, 3.48, "Servo-vectored surface robot", fontsize=23, color=white)
    ax.text(.70, 2.86, "Four rotating thrusters on a fiberglass catamaran.",
            fontsize=12.5, color=muted)
    ax.add_patch(FancyBboxPatch((.70, 1.67), 5.93, .65,
                               boxstyle="round,pad=.04,rounding_size=.06",
                               facecolor="#203340", edgecolor="#304b5c"))
    ax.text(.96, 1.99, "1st / 64", fontsize=18, color="#edc87f", weight="bold", va="center")
    ax.text(2.57, 1.99, "HYDROBOT SOCCER LEAGUE", fontsize=10.5, color=white,
            weight="bold", va="center")
    ax.text(.70, 1.04, "ESP32 / ESP-NOW     ·     IBT-2     ·     PCA9685",
            fontsize=11.2, color=muted)
    ax.text(.70, .49, "DESIGN  /  FABRICATION  /  CONTROL  /  WATER TRIALS",
            fontsize=9.5, color="#7f99aa")
    ax.text(10.78, 5.48, "PROPULSION LAYOUT", fontsize=10.5, color=muted,
            ha="center", weight="bold")
    for y in (2.20, 3.79):
        ax.add_patch(Rectangle((9.2, y), 3.16, .17, facecolor="#4c6575", edgecolor="none"))
    for x in (8.76, 11.74):
        points = [(x, 1.40), (x+1.12, 1.40), (x+1.12, 4.35),
                  (x+.56, 4.95), (x, 4.35)]
        ax.add_patch(Polygon(points, facecolor="#622c36", edgecolor=red, lw=1.8))
        ax.plot([x+.2, x+.2, x+.56], [1.65, 4.24, 4.63], color="#9c3b48", lw=.8)
    ax.add_patch(FancyBboxPatch((9.95, 2.62), 1.70, 1.13,
                               boxstyle="round,pad=.03,rounding_size=.08",
                               facecolor="#263b49", edgecolor=edge, lw=1))
    ax.add_patch(Rectangle((10.30, 2.95), 1.0, .49, facecolor="#142733", edgecolor="#698695", lw=.8))
    ax.text(10.80, 3.18, "ESP32", fontsize=9, color=muted, ha="center", va="center")
    for x in (9.32, 12.30):
        for y in (2.12, 4.02):
            ax.add_patch(Arc((x, y), .86, .86, theta1=10, theta2=155,
                             edgecolor="#367f85", lw=1, ls=(0, (3, 3))))
            ax.add_patch(Circle((x, y), .16, facecolor=teal, edgecolor=bg, lw=1.5))
            ax.annotate("", xy=(x+.43, y+.51), xytext=(x, y),
                        arrowprops={"arrowstyle": "-|>", "color": teal, "lw": 1.7,
                                    "mutation_scale": 13})
        ax.add_patch(Circle((x, 1.66), .29, facecolor=bg, edgecolor=edge, lw=1.2))
        for angle in (90, 270):
            a=np.deg2rad(angle)
            ax.plot([x, x+.23*np.cos(a)], [1.66, 1.66+.23*np.sin(a)],
                    color=edge, lw=3, solid_capstyle="round")
        ax.add_patch(Circle((x, 1.66), .055, facecolor=white, edgecolor="none"))
    ax.text(10.80, .81, "Four rotating motor / propeller units", fontsize=10,
            color=white, ha="center")
    ax.text(10.80, .49, "Conceptual top view", fontsize=9, color="#7f99aa", ha="center")
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    out=ROOT/"assets"/"figures"
    fig.savefig(out/"fobo-project-banner.png", dpi=160, facecolor=bg)
    fig.savefig(out/"fobo-project-banner.svg", facecolor=bg, metadata={"Date": None})
    plt.close(fig)


if __name__ == "__main__":
    draw()

    # Keep SVG exports stable and free of trailing whitespace.
    for stem in ['fobo-project-banner']:
        svg = ROOT / "assets" / "figures" / (stem + ".svg")
        svg.write_text("\n".join(line.rstrip() for line in svg.read_text().splitlines()) + "\n")
