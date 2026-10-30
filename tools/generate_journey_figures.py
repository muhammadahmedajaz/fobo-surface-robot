"""Generate source-labelled FOBO history and concept illustrations.

Dates are record dates, not inferred construction dates. Hull outlines are
illustrative cross-sections, not recovered handwriting or dimensioned CAD.
"""
import json
import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "figures"
INK, TEAL, RED, LIGHT, MUTED = "#182b3a", "#087f8c", "#b52b3a", "#f2f6f7", "#52616b"


def save(fig, stem):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / f"{stem}.png", dpi=160)
    fig.savefig(OUT / f"{stem}.svg", metadata={"Date": None})
    plt.close(fig)


def timeline(record):
    fig, ax = plt.subplots(figsize=(13.5, 10.4))
    fig.patch.set_facecolor("white")
    ax.set(xlim=(0, 13.5), ylim=(0, 10.4))
    ax.axis("off")
    ax.text(.5, 9.94, "FOBO / THE RECOVERED ENGINEERING RECORD", fontsize=21,
            weight="bold", color=INK)
    ax.text(.5, 9.55, "Discussion dates and later clarifications • not a complete build log",
            fontsize=12, color=MUTED)
    ax.plot([2.7, 2.7], [2.0, 8.85], color="#c3d8dc", lw=3, zorder=1)
    for i, event in enumerate(record["milestones"]):
        y = 8.8 - i * 1.33
        color = TEAL if i < 4 else RED
        ax.scatter([2.7], [y], s=110, color=color, edgecolor="white", linewidth=2, zorder=3)
        ax.text(.5, y+.10, event["label"], fontsize=11.2, weight="bold", color=INK, va="top")
        ax.add_patch(FancyBboxPatch((3.08, y-.87), 9.85, 1.12,
                                   boxstyle="round,pad=.09", facecolor=LIGHT,
                                   edgecolor="none", zorder=0))
        ax.text(3.34, y+.03, event["title"], fontsize=13.5, weight="bold", color=INK, va="top")
        detail = "\n".join(textwrap.wrap(event["detail"], width=105))
        ax.text(3.34, y-.29, detail, fontsize=10.8, color=INK, va="top", linespacing=1.4)
        ax.text(3.34, y-.70, f'{event["record_type"]}  |  {event["sources"][0]}–{event["sources"][-1]}'
                if len(event["sources"]) > 1 else f'{event["record_type"]}  |  {event["sources"][0]}',
                fontsize=9, color=MUTED, va="top")
    ax.add_patch(FancyBboxPatch((.5, .56), 12.43, .47, boxstyle="round,pad=.06",
                               facecolor="#fff0df", edgecolor="none"))
    ax.text(.75, .79, "COMPETITION OUTCOME", fontsize=10, weight="bold", color=RED, va="center")
    ax.text(3.5, .79, f'{record["competition"]["result"]} • event date unrecovered',
            fontsize=12, weight="bold", color=INK, va="center")
    ax.text(.5, .23, "Read with docs/journey-sources.md • spacing is not an elapsed-time scale • original handwritten attachments unrecovered",
            fontsize=9.6, color=MUTED)
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    save(fig, "build-journey-timeline")


def hull_concepts(record):
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 5.8))
    fig.patch.set_facecolor("white")
    for ax, concept in zip(axes, record["hull_concepts"]):
        ax.set(xlim=(0, 4.2), ylim=(0, 4.5))
        ax.axis("off")
        ax.add_patch(FancyBboxPatch((.12, .65), 3.96, 3.7, boxstyle="round,pad=.03",
                                   facecolor=LIGHT, edgecolor="none"))
        ax.text(2.1, 4.01, concept["label"], fontsize=13.5, weight="bold", color=INK, ha="center")
        ax.plot([.43, 3.77], [2.66, 2.66], color="#80b9c5", lw=1.4, ls="--")
        color = RED if concept["id"] == "catamaran" else MUTED
        if concept["id"] == "flat":
            shape = [( .68, 2.94), (3.52, 2.94), (3.52, 2.42), (.68, 2.42)]
            ax.add_patch(Polygon(shape, facecolor="#dbe4e8", edgecolor=color, lw=2))
        elif concept["id"] == "v":
            shape = [(.68, 3.08), (3.52, 3.08), (2.1, 1.98)]
            ax.add_patch(Polygon(shape, facecolor="#dbe4e8", edgecolor=color, lw=2))
        else:
            for x in (.7, 2.65):
                ax.add_patch(FancyBboxPatch((x, 2.18), .85, .89, boxstyle="round,pad=.03,rounding_size=.18",
                                           facecolor="#f3d9dc", edgecolor=color, lw=2))
            ax.plot([1.15, 3.05], [3.18, 3.18], color=INK, lw=4)
        ax.text(2.1, 1.62, concept["status"], fontsize=12, color=color, weight="bold", ha="center")
        ax.text(2.1, 1.25, concept["note"], fontsize=10.6, color=INK, ha="center", va="top", linespacing=1.4)
    fig.suptitle("FOBO / HULL CONCEPTS IN THE DESIGN RECORD", fontsize=20, weight="bold", color=INK, y=.96)
    fig.text(.5, .845, "Reconstructed illustrative sections • not original sketches or dimensioned hull geometry",
             fontsize=11.5, ha="center", color=MUTED)
    fig.text(.5, .075, "Source S10 • No comparative drag/stability measurements or numerical decision weights recovered",
             fontsize=10, ha="center", color=MUTED)
    fig.subplots_adjust(left=.025, right=.975, top=.81, bottom=.12, wspace=.07)
    save(fig, "hull-concept-selection")


if __name__ == "__main__":
    plt.rcParams.update({"font.family": "DejaVu Sans", "svg.fonttype": "none",
                         "svg.hashsalt": "fobo-journey-2026"})
    data = json.loads((ROOT / "data" / "build_journey.json").read_text())
    timeline(data)
    hull_concepts(data)
