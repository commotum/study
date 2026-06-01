from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch


OUTPUT_PATH = Path(
    "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/"
    "2-Build-Lessons/4-Image-Generation/1-Outputs/"
    "Continuous-Time-Signal-Processing/6.3--convolution-setup-Images/"
    "images/l006-s001-te-section-001.png"
)

BACKGROUND_COLOR = "white"
SIGNAL_COLOR = "#2f78b7"
SECONDARY_COLOR = "#606060"
PRODUCT_COLOR = "#7aa6c8"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"
GRID_COLOR = "#000000"

plt.rcParams.update(
    {
        "mathtext.fontset": "cm",
        "font.family": "serif",
        "figure.facecolor": BACKGROUND_COLOR,
        "axes.facecolor": BACKGROUND_COLOR,
        "savefig.facecolor": BACKGROUND_COLOR,
    }
)


def add_arrow(fig, start, end, *, text=None):
    arrow = FancyArrowPatch(
        start,
        end,
        transform=fig.transFigure,
        arrowstyle="-|>",
        mutation_scale=18,
        linewidth=2.0,
        color=ANNOTATION_COLOR,
        shrinkA=2,
        shrinkB=2,
        zorder=20,
    )
    fig.patches.append(arrow)
    if text:
        x_mid = (start[0] + end[0]) / 2
        y_mid = (start[1] + end[1]) / 2
        fig.text(x_mid, y_mid + 0.02, text, ha="center", va="bottom", fontsize=11, color=ANNOTATION_COLOR)


def setup_axis(ax, title):
    ax.set_xlim(-1.5, 3.3)
    ax.set_ylim(-0.35, 1.55)
    ax.set_xticks([-1, 0, 1, 2, 3])
    ax.set_yticks([1])
    ax.grid(True, linewidth=0.55, alpha=0.16, color=GRID_COLOR)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    ax.annotate(
        "",
        xy=(3.25, 0),
        xytext=(-1.45, 0),
        arrowprops=dict(arrowstyle="-|>", lw=1.5, color=AXIS_COLOR, shrinkA=0, shrinkB=0),
        zorder=4,
    )
    ax.annotate(
        "",
        xy=(0, 1.48),
        xytext=(0, -0.3),
        arrowprops=dict(arrowstyle="-|>", lw=1.5, color=AXIS_COLOR, shrinkA=0, shrinkB=0),
        zorder=4,
    )
    for tick in [-1, 0, 1, 2, 3]:
        ax.plot([tick, tick], [-0.045, 0.045], color=AXIS_COLOR, lw=1.0, zorder=5)
        ax.text(tick, -0.13, rf"${tick}$", ha="center", va="top", fontsize=9, color=TICK_LABEL_COLOR)
    ax.plot([-0.045, 0.045], [1, 1], color=AXIS_COLOR, lw=1.0, zorder=5)
    ax.text(-0.10, 1, r"$1$", ha="right", va="center", fontsize=9, color=TICK_LABEL_COLOR)
    ax.text(3.30, -0.03, r"$\tau$", ha="left", va="center", fontsize=13, color=LABEL_COLOR)
    ax.text(0.5, 1.045, title, transform=ax.transAxes, ha="center", va="bottom", fontsize=12, color=LABEL_COLOR)


def plot_rect(ax, start, end, level, *, color=SIGNAL_COLOR, label=None):
    xs = [-1.45, start, start, end, end, 3.25]
    ys = [0, 0, level, level, 0, 0]
    ax.plot(xs, ys, color=color, lw=2.8, solid_capstyle="butt", solid_joinstyle="miter", zorder=6)
    if label:
        ax.text((start + end) / 2, level + 0.09, label, ha="center", va="bottom", fontsize=11, color=color)


def plot_triangle(ax, left, peak, right, *, color=SECONDARY_COLOR, label=None):
    xs = [-1.45, left, peak, right, 3.25]
    ys = [0, 0, 1, 0, 0]
    ax.plot(xs, ys, color=color, lw=2.7, solid_capstyle="round", zorder=6)
    if label:
        ax.text(peak, 1.09, label, ha="center", va="bottom", fontsize=11, color=color)


def plot_product(ax):
    tau = np.linspace(-1.45, 3.25, 500)
    product = np.zeros_like(tau)
    mask = (tau >= 1.0) & (tau <= 2.0)
    product[mask] = (2.5 - tau[mask]) / 1.5
    ax.plot(tau, product, color=SIGNAL_COLOR, lw=2.8, solid_capstyle="round", zorder=7)
    ax.fill_between(tau[mask], product[mask], 0, color=PRODUCT_COLOR, alpha=0.28, zorder=3)
    ax.text(1.5, 0.36, r"overlap area", ha="center", va="center", fontsize=10, color=ANNOTATION_COLOR)


def main():
    fig = plt.figure(figsize=(14.2, 8.6), dpi=300, facecolor=BACKGROUND_COLOR)
    positions = [
        (0.07, 0.56, 0.37, 0.30),
        (0.56, 0.56, 0.37, 0.30),
        (0.07, 0.16, 0.37, 0.30),
        (0.56, 0.16, 0.37, 0.30),
    ]
    axes = [fig.add_axes(pos) for pos in positions]

    setup_axis(axes[0], r"1. start with $x(\tau)$ and $h(\tau)$")
    plot_rect(axes[0], 0.0, 2.0, 1.0, color=SIGNAL_COLOR)
    plot_triangle(axes[0], 0.0, 0.75, 1.5, color=SECONDARY_COLOR)
    axes[0].text(1.82, 1.14, r"$x(\tau)$", ha="center", va="bottom", fontsize=11, color=SIGNAL_COLOR)
    axes[0].text(0.62, 1.25, r"$h(\tau)$", ha="center", va="bottom", fontsize=11, color=SECONDARY_COLOR)

    setup_axis(axes[1], r"2. flip the impulse response")
    plot_triangle(axes[1], -1.5, -0.75, 0.0, color=SECONDARY_COLOR, label=r"$h(-\tau)$")
    axes[1].axvline(0, color=GUIDE_COLOR, lw=1.4, linestyle=(0, (3.0, 3.0)), zorder=2)

    setup_axis(axes[2], r"3. shift for fixed $t=t_0$")
    plot_rect(axes[2], 0.0, 2.0, 1.0, color=SIGNAL_COLOR, label=r"$x(\tau)$")
    plot_triangle(axes[2], 1.0, 1.75, 2.5, color=SECONDARY_COLOR, label=r"$h(t_0-\tau)$")
    axes[2].axvspan(1.0, 2.0, color=PRODUCT_COLOR, alpha=0.14, zorder=1)
    axes[2].text(1.5, 1.30, r"overlap", ha="center", va="center", fontsize=10, color=ANNOTATION_COLOR)

    setup_axis(axes[3], r"4. multiply, then integrate")
    plot_product(axes[3])
    axes[3].text(
        1.5,
        1.20,
        r"$x(\tau)h(t_0-\tau)$",
        ha="center",
        va="center",
        fontsize=12,
        color=LABEL_COLOR,
    )

    add_arrow(fig, (0.45, 0.71), (0.55, 0.71), text="flip")
    add_arrow(fig, (0.75, 0.55), (0.75, 0.48), text="shift")
    add_arrow(fig, (0.45, 0.31), (0.55, 0.31), text="multiply")

    add_arrow(fig, (0.85, 0.23), (0.95, 0.23), text=r"$\int_{-\infty}^{\infty}\cdot\,d\tau$")
    fig.text(
        0.975,
        0.23,
        r"$y(t_0)$",
        ha="left",
        va="center",
        fontsize=18,
        color=LABEL_COLOR,
    )

    fig.text(
        0.5,
        0.95,
        r"Flip-shift-multiply-integrate setup for convolution",
        ha="center",
        va="center",
        fontsize=18,
        color=LABEL_COLOR,
    )
    fig.text(
        0.5,
        0.055,
        r"hold $t_0$ fixed; the shaded product area is the convolution value at that output time",
        ha="center",
        va="center",
        fontsize=12,
        color=ANNOTATION_COLOR,
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH, dpi=300, bbox_inches="tight", facecolor=BACKGROUND_COLOR)
    plt.close(fig)


if __name__ == "__main__":
    main()
