from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle


OUTPUT_PATH = Path(
    "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/"
    "2-Build-Lessons/4-Image-Generation/1-Outputs/"
    "Continuous-Time-Signal-Processing/6.3--convolution-setup-Images/"
    "images/l001-s001-te-section-001.png"
)

BACKGROUND_COLOR = "white"
SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"
FILL_COLOR = "#f7fbff"

plt.rcParams.update(
    {
        "mathtext.fontset": "cm",
        "font.family": "serif",
        "figure.facecolor": BACKGROUND_COLOR,
        "axes.facecolor": BACKGROUND_COLOR,
        "savefig.facecolor": BACKGROUND_COLOR,
    }
)


def add_arrow(ax, start, end, *, color=ANNOTATION_COLOR, lw=2.0, mutation_scale=14):
    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=mutation_scale,
        linewidth=lw,
        color=color,
        shrinkA=2,
        shrinkB=2,
        zorder=3,
    )
    ax.add_patch(arrow)


def add_box(ax, xy, width, height, text, *, fontsize=17, edgecolor=AXIS_COLOR):
    box = Rectangle(
        xy,
        width,
        height,
        linewidth=1.8,
        edgecolor=edgecolor,
        facecolor=FILL_COLOR,
        zorder=2,
    )
    ax.add_patch(box)
    ax.text(
        xy[0] + width / 2,
        xy[1] + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        color=LABEL_COLOR,
        zorder=4,
    )


def add_impulse_symbol(ax, x, y, label):
    ax.plot([x, x], [y - 0.055, y + 0.09], color=SIGNAL_COLOR, lw=2.5, zorder=4)
    add_arrow(ax, (x, y + 0.045), (x, y + 0.1), color=SIGNAL_COLOR, lw=1.9, mutation_scale=10)
    ax.plot([x - 0.032, x + 0.032], [y - 0.055, y - 0.055], color=AXIS_COLOR, lw=1.2)
    ax.text(x, y - 0.1, label, ha="center", va="top", fontsize=13, color=LABEL_COLOR)


def main():
    fig, ax = plt.subplots(figsize=(13.2, 6.8), dpi=300)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(
        0.5,
        0.93,
        r"Continuous-time convolution as accumulated LTI responses",
        ha="center",
        va="center",
        fontsize=18,
        color=LABEL_COLOR,
    )

    ax.text(0.08, 0.55, r"$x(t)$", ha="center", va="center", fontsize=28, color=LABEL_COLOR)
    add_arrow(ax, (0.13, 0.55), (0.24, 0.55), color=SIGNAL_COLOR, lw=2.4)
    ax.text(
        0.19,
        0.61,
        r"decompose over $\tau$",
        ha="center",
        va="bottom",
        fontsize=14,
        color=ANNOTATION_COLOR,
    )

    ax.text(
        0.30,
        0.82,
        r"weighted impulse contributions",
        ha="center",
        va="center",
        fontsize=13,
        color=ANNOTATION_COLOR,
    )
    ax.text(
        0.53,
        0.82,
        r"LTI system",
        ha="center",
        va="center",
        fontsize=13,
        color=ANNOTATION_COLOR,
    )
    ax.text(
        0.74,
        0.82,
        r"shifted impulse responses",
        ha="center",
        va="center",
        fontsize=13,
        color=ANNOTATION_COLOR,
    )

    rows = [
        (0.70, r"$x(\tau_1)\,d\tau$", r"$x(\tau_1)d\tau\,h(t-\tau_1)$", r"$\tau_1$"),
        (0.55, r"$x(\tau_2)\,d\tau$", r"$x(\tau_2)d\tau\,h(t-\tau_2)$", r"$\tau_2$"),
        (0.40, r"$x(\tau_3)\,d\tau$", r"$x(\tau_3)d\tau\,h(t-\tau_3)$", r"$\tau_3$"),
    ]

    for y, weight, response, tau_label in rows:
        add_impulse_symbol(ax, 0.27, y, tau_label)
        ax.text(0.34, y, weight, ha="left", va="center", fontsize=15, color=LABEL_COLOR)
        add_arrow(ax, (0.43, y), (0.485, y), color=ANNOTATION_COLOR, lw=1.9)
        add_box(ax, (0.49, y - 0.045), 0.105, 0.09, r"$h(t)$", fontsize=18)
        add_arrow(ax, (0.60, y), (0.655, y), color=ANNOTATION_COLOR, lw=1.9)
        ax.text(0.66, y, response, ha="left", va="center", fontsize=14, color=LABEL_COLOR)
        add_arrow(ax, (0.82, y), (0.89, 0.55), color=GUIDE_COLOR, lw=1.8)

    ax.text(0.295, 0.295, r"$\vdots$", ha="center", va="center", fontsize=24, color=GUIDE_COLOR)
    ax.text(0.735, 0.295, r"$\vdots$", ha="center", va="center", fontsize=24, color=GUIDE_COLOR)

    add_box(ax, (0.875, 0.485), 0.10, 0.13, r"$\int(\cdot)\,d\tau$", fontsize=16)
    add_arrow(ax, (0.975, 0.55), (1.025, 0.55), color=SIGNAL_COLOR, lw=2.4)
    ax.text(1.045, 0.55, r"$y(t)$", ha="left", va="center", fontsize=26, color=LABEL_COLOR, clip_on=False)

    ax.text(
        0.5,
        0.18,
        r"$y(t)=\int_{-\infty}^{\infty} x(\tau)\,h(t-\tau)\,d\tau$",
        ha="center",
        va="center",
        fontsize=22,
        color=LABEL_COLOR,
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH, dpi=300, bbox_inches="tight", facecolor=BACKGROUND_COLOR)
    plt.close(fig)


if __name__ == "__main__":
    main()
