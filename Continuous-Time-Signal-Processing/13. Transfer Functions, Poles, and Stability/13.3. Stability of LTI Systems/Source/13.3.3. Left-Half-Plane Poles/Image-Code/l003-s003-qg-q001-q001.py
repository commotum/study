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
})


CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150
MARGIN_LEFT_PX = 115
MARGIN_RIGHT_PX = 120
MARGIN_BOTTOM_PX = 95
MARGIN_TOP_PX = 110

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
ANNOTATION_COLOR = "#555555"

SIGNAL_LW = 7.1 * 72 / CANONICAL_DPI
AXIS_LW = 4.3 * 72 / CANONICAL_DPI
TICK_LW = 2.7 * 72 / CANONICAL_DPI
GRID_LW = 1.3 * 72 / CANONICAL_DPI

TICK_LABEL_SIZE = 35.6 * 72 / CANONICAL_DPI
AXIS_LABEL_SIZE = 53.3 * 72 / CANONICAL_DPI
TOP_LABEL_SIZE = 57.8 * 72 / CANONICAL_DPI
ANNOTATION_SIZE = 33.3 * 72 / CANONICAL_DPI

TICK_HALF_LEN = 8.25 / PX_PER_DATA_UNIT
X_TICK_LABEL_Y = -24 / PX_PER_DATA_UNIT
Y_TICK_LABEL_X = 18 / PX_PER_DATA_UNIT
ORIGIN_LABEL_X = 9 / PX_PER_DATA_UNIT
ORIGIN_LABEL_Y = -12 / PX_PER_DATA_UNIT
X_AXIS_LABEL_X_PAD = 15 / PX_PER_DATA_UNIT
X_AXIS_LABEL_Y = -4.5 / PX_PER_DATA_UNIT
Y_AXIS_LABEL_Y_PAD = 18 / PX_PER_DATA_UNIT

POLE_MARKER_SIZE = 18.0 * 72 / CANONICAL_DPI
ZERO_MARKER_SIZE = 16.0 * 72 / CANONICAL_DPI
POLE_EDGEWIDTH = 4.2 * 72 / CANONICAL_DPI
ZERO_EDGEWIDTH = 4.0 * 72 / CANONICAL_DPI

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

OUTPUT_PATH = Path(
    "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/13.3--stability-of-lti-systems-Images/images/l003-s003-qg-q001-q001.png"
)


def px_to_data(px):
    return px / PX_PER_DATA_UNIT


def make_figure(xlim, ylim):
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


def setup_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_axis_label=r"$\Re\{s\}$",
    y_axis_label=r"$\Im\{s\}$",
    show_grid=True,
    show_origin=True,
):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(1))

    if show_grid:
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
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(t, X_TICK_LABEL_Y, math_label(t), fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR, zorder=6)

    for y in yticks:
        if abs(y) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(-Y_TICK_LABEL_X, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha="right", va="center", color=TICK_LABEL_COLOR, zorder=6)

    if show_origin:
        ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$", fontsize=TICK_LABEL_SIZE, ha="left", va="top", color=TICK_LABEL_COLOR, zorder=6)

    ax.text(x1 + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, x_axis_label, fontsize=AXIS_LABEL_SIZE, ha="left", va="center", color=LABEL_COLOR, clip_on=False)
    ax.text(0, y1 + Y_AXIS_LABEL_Y_PAD, y_axis_label, fontsize=TOP_LABEL_SIZE, ha="center", va="bottom", color=LABEL_COLOR, clip_on=False)


def add_pole(ax, x, y, label, dx=0.12, dy=0.12, ha="left", va="bottom"):
    ax.plot(
        x,
        y,
        marker="x",
        markersize=POLE_MARKER_SIZE,
        markeredgewidth=POLE_EDGEWIDTH,
        color=SIGNAL_COLOR,
        linestyle="None",
        zorder=7,
    )
    ax.text(x + dx, y + dy, label, fontsize=ANNOTATION_SIZE, ha=ha, va=va, color=ANNOTATION_COLOR, zorder=8)


def add_zero(ax, x, y, label=None, dx=0.12, dy=0.12, ha="left", va="bottom"):
    ax.plot(
        x,
        y,
        marker="o",
        markersize=ZERO_MARKER_SIZE,
        markerfacecolor="white",
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=ZERO_EDGEWIDTH,
        linestyle="None",
        zorder=7,
    )
    if label is not None:
        ax.text(x + dx, y + dy, label, fontsize=ANNOTATION_SIZE, ha=ha, va=va, color=ANNOTATION_COLOR, zorder=8)


def save_figure(fig, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=CANONICAL_DPI, facecolor="white", bbox_inches="tight")


def main():
    xlim = (-3.4, 3.4)
    ylim = (-3.0, 3.0)
    fig, ax = make_figure(xlim, ylim)
    setup_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=[-3, -2, -1, 0, 1, 2, 3],
        yticks=[-2, -1, 0, 1, 2],
    )

    ax.axvspan(xlim[0], 0, color=SIGNAL_COLOR, alpha=0.05, zorder=0)
    ax.text(-2.75, 2.22, r"$\mathrm{LHP}$", fontsize=TOP_LABEL_SIZE * 0.82, ha="left", va="center", color=SIGNAL_COLOR, zorder=2)
    ax.text(1.8, 2.22, r"$\mathrm{RHP}$", fontsize=TOP_LABEL_SIZE * 0.82, ha="left", va="center", color=ANNOTATION_COLOR, zorder=2)
    ax.text(0.12, 2.48, r"$\Re\{s\}=0$", fontsize=ANNOTATION_SIZE, ha="left", va="bottom", color=ANNOTATION_COLOR, zorder=2)

    add_pole(ax, -2, 0, r"$-2$", dx=-0.12, dy=-0.34, ha="right", va="top")
    add_pole(ax, -0.5, 0, r"$-0.5$", dx=-0.10, dy=-0.34, ha="right", va="top")
    add_pole(ax, 0.2, 0, r"$0.2$", dx=0.14, dy=0.20, ha="left", va="bottom")
    add_pole(ax, -1, 2, r"$-1+2j$", dx=-0.14, dy=0.18, ha="right", va="bottom")

    add_zero(ax, 0, 2, r"$j2$", dx=0.16, dy=0.10, ha="left", va="bottom")
    add_zero(ax, 0, -2, r"$-j2$", dx=0.16, dy=-0.18, ha="left", va="top")

    save_figure(fig, OUTPUT_PATH)


if __name__ == "__main__":
    main()
