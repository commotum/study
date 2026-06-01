from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.ticker import MultipleLocator

rcParams.update({
    "mathtext.fontset": "cm",
    "font.family": "serif",
})

CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150
SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"

TICK_LABEL_SIZE = 35.6 * 72 / CANONICAL_DPI
AXIS_LABEL_SIZE = 53.3 * 72 / CANONICAL_DPI
TOP_LABEL_SIZE = 57.8 * 72 / CANONICAL_DPI
TICK_HALF_LEN = 8.25 / PX_PER_DATA_UNIT
X_TICK_LABEL_Y = -24 / PX_PER_DATA_UNIT
Y_TICK_LABEL_X = 18 / PX_PER_DATA_UNIT
ORIGIN_LABEL_X = 9 / PX_PER_DATA_UNIT
ORIGIN_LABEL_Y = -12 / PX_PER_DATA_UNIT
X_AXIS_LABEL_X_PAD = 15 / PX_PER_DATA_UNIT
X_AXIS_LABEL_Y = -4.5 / PX_PER_DATA_UNIT
Y_AXIS_LABEL_Y_PAD = 18 / PX_PER_DATA_UNIT
SIGNAL_LW = 7.1 * 72 / CANONICAL_DPI
TICK_LW = 2.7 * 72 / CANONICAL_DPI
GRID_LW = 1.3 * 72 / CANONICAL_DPI

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

def math_label(value):
    if abs(float(value) - round(float(value))) < 1e-9:
        return rf"${int(round(float(value)))}$"
    return rf"${float(value):g}$"


def setup_ct_signal_axes(ax, *, xlim, ylim, xticks, yticks):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(1))
    ax.grid(True, which="both", linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
    ax.set_axisbelow(True)

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    x0, x1 = xlim
    y0, y1 = ylim
    ax.quiver(x0, 0, x1 - x0, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y0, 0, y1 - y0, **AXIS_ARROW_KW)

    for t in xticks:
        if abs(t) < 1e-12:
            continue
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW)
        ax.text(t, X_TICK_LABEL_Y, math_label(t), fontsize=TICK_LABEL_SIZE,
                ha="center", va="top", color=TICK_LABEL_COLOR)

    for y in yticks:
        if abs(y) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW)
        ax.text(-Y_TICK_LABEL_X, y, math_label(y), fontsize=TICK_LABEL_SIZE,
                ha="right", va="center", color=TICK_LABEL_COLOR)

    ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$", fontsize=TICK_LABEL_SIZE,
            ha="left", va="top", color=TICK_LABEL_COLOR)
    ax.text(x1 + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, r"$t$", fontsize=AXIS_LABEL_SIZE,
            ha="left", va="center", color=LABEL_COLOR, clip_on=False)
    ax.text(0, y1 + Y_AXIS_LABEL_Y_PAD, r"$x(t)$", fontsize=TOP_LABEL_SIZE,
            ha="center", va="bottom", color=LABEL_COLOR, clip_on=False)

def plot_signal(ax, t, x):
    ax.plot(t, x, color=SIGNAL_COLOR, linewidth=SIGNAL_LW,
            solid_capstyle="butt", solid_joinstyle="miter", zorder=4)

def make_ct_signal_figure(xlim, ylim):
    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]
    fig_w_px = 115 + x_range * PX_PER_DATA_UNIT + 120
    fig_h_px = 95 + y_range * PX_PER_DATA_UNIT + 110
    return fig_w_px / CANONICAL_DPI, fig_h_px / CANONICAL_DPI


def main():
    xlim = (-2.45, 2.45)
    ylim = (-0.4, 2.4)
    xticks = [-2, -1, 0, 1, 2]
    yticks = [0, 1, 2]
    t = [-2, 0, 2]
    x = [2, 0, 2]

    fig, ax = plt.subplots(
        figsize=make_ct_signal_figure(xlim, ylim),
        dpi=CANONICAL_DPI,
        facecolor="white",
        constrained_layout=True,
    )
    setup_ct_signal_axes(ax, xlim=xlim, ylim=ylim, xticks=xticks, yticks=yticks)
    plot_signal(ax, t, x)

    output_path = Path("/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/1.1--continuous-time-signal-basics-Images/images/l005-s002-qg-q002-q002.png")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=CANONICAL_DPI, bbox_inches="tight", facecolor="white")


if __name__ == "__main__":
    main()
