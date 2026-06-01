from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


plt.rcParams.update({
    "mathtext.fontset": "cm",
    "font.family": "serif",
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
    "axes.facecolor": "white",
})


CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150

MARGIN_LEFT_PX = 115
MARGIN_RIGHT_PX = 120
MARGIN_BOTTOM_PX = 95
MARGIN_TOP_PX = 110

AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
REGION_COLOR = "#2f78b7"
POLE_COLOR = "#2f78b7"

AXIS_LW = 4.3 * 72 / CANONICAL_DPI
TICK_LW = 2.7 * 72 / CANONICAL_DPI
GRID_LW = 1.3 * 72 / CANONICAL_DPI

TICK_LABEL_SIZE = 35.6 * 72 / CANONICAL_DPI
AXIS_LABEL_SIZE = 53.3 * 72 / CANONICAL_DPI
NOTE_SIZE = 30.0 * 72 / CANONICAL_DPI

TICK_HALF_LEN = 8.25 / PX_PER_DATA_UNIT
X_TICK_LABEL_Y = -24 / PX_PER_DATA_UNIT
Y_TICK_LABEL_X = 18 / PX_PER_DATA_UNIT
ORIGIN_LABEL_X = 9 / PX_PER_DATA_UNIT
ORIGIN_LABEL_Y = -12 / PX_PER_DATA_UNIT
X_AXIS_LABEL_X_PAD = 15 / PX_PER_DATA_UNIT
X_AXIS_LABEL_Y = -4.5 / PX_PER_DATA_UNIT
Y_AXIS_LABEL_Y_PAD = 18 / PX_PER_DATA_UNIT

AXIS_ARROW_SHAFT_WIDTH_DATA = 4.3 / PX_PER_DATA_UNIT
AXIS_ARROW_KW = dict(
    angles="xy",
    scale_units="xy",
    scale=1,
    units="xy",
    width=AXIS_ARROW_SHAFT_WIDTH_DATA,
    headwidth=4.2,
    headlength=5.5,
    headaxislength=4.3,
    color=AXIS_COLOR,
    pivot="tail",
    clip_on=False,
)


def px_to_data(px: float) -> float:
    return px / PX_PER_DATA_UNIT


def make_ct_signal_figure(xlim, ylim):
    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]
    fig_w_px = MARGIN_LEFT_PX + x_range * PX_PER_DATA_UNIT + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_BOTTOM_PX + y_range * PX_PER_DATA_UNIT + MARGIN_TOP_PX
    fig, ax = plt.subplots(
        figsize=(fig_w_px / CANONICAL_DPI, fig_h_px / CANONICAL_DPI),
        dpi=CANONICAL_DPI,
        facecolor="white",
        constrained_layout=True,
    )
    return fig, ax


def math_label(value):
    if abs(value - int(value)) < 1e-9:
        return rf"${int(value)}$"
    return rf"${value:g}$"


def setup_s_plane_axes(ax, *, xlim, ylim, xticks, yticks):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.xaxis.set_minor_locator(MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(MultipleLocator(0.5))
    ax.grid(True, which="both", linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
    ax.set_axisbelow(True)

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    x_axis_start, x_axis_end = xlim
    y_axis_start, y_axis_end = ylim
    ax.quiver(x_axis_start, 0, x_axis_end - x_axis_start, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y_axis_start, 0, y_axis_end - y_axis_start, **AXIS_ARROW_KW)

    for t in xticks:
        if abs(t) < 1e-12:
            continue
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(t, X_TICK_LABEL_Y, math_label(t), fontsize=TICK_LABEL_SIZE,
                ha="center", va="top", color=TICK_LABEL_COLOR, zorder=6)

    for y in yticks:
        if abs(y) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(-Y_TICK_LABEL_X, y, math_label(y), fontsize=TICK_LABEL_SIZE,
                ha="right", va="center", color=TICK_LABEL_COLOR, zorder=6)

    ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$", fontsize=TICK_LABEL_SIZE,
            ha="left", va="top", color=TICK_LABEL_COLOR, zorder=6)
    ax.text(x_axis_end + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, r"$\Re\{s\}$",
            fontsize=AXIS_LABEL_SIZE, ha="left", va="center", color=LABEL_COLOR, clip_on=False)
    ax.text(0, y_axis_end + Y_AXIS_LABEL_Y_PAD, r"$\Im\{s\}$",
            fontsize=AXIS_LABEL_SIZE, ha="center", va="bottom", color=LABEL_COLOR, clip_on=False)


def pole_marker(ax, x, y, label, dx=0.0, dy=0.0):
    ax.plot(
        x,
        y,
        marker="x",
        markersize=12,
        markeredgewidth=3.2,
        color=POLE_COLOR,
        linestyle="None",
        zorder=7,
    )
    ax.text(x + dx, y + dy, label, fontsize=NOTE_SIZE, color=LABEL_COLOR,
            ha="center", va="bottom", zorder=8)


def save_figure(fig, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=CANONICAL_DPI, facecolor="white", bbox_inches="tight")


def main():
    out_path = Path(
        "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/"
        "2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/"
        "13.3--stability-of-lti-systems-Images/images/l004-s001-te-section-001.png"
    )

    xlim = (-2.2, 2.8)
    ylim = (-1.8, 1.8)
    fig, ax = make_ct_signal_figure(xlim, ylim)
    setup_s_plane_axes(ax, xlim=xlim, ylim=ylim, xticks=[-2, -1, 0, 1, 2], yticks=[-1, 0, 1])

    ax.axvspan(0, xlim[1], color=REGION_COLOR, alpha=0.10, zorder=0)
    ax.text(1.35, 1.15, r"$\Re\{s\} > 0$", fontsize=NOTE_SIZE, color=LABEL_COLOR,
            ha="center", va="center", zorder=2)
    ax.text(1.4, -1.08, r"right half-plane", fontsize=NOTE_SIZE, color=LABEL_COLOR,
            ha="center", va="center", zorder=2)

    pole_marker(ax, 1, 0, r"$s=1$", dx=0.0, dy=0.22)
    pole_marker(ax, -1, 0, r"$s=-1$", dx=0.0, dy=0.22)

    save_figure(fig, out_path)


if __name__ == "__main__":
    main()
