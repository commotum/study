from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


plt.rcParams.update(
    {
        "mathtext.fontset": "cm",
        "font.family": "serif",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)


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
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"

SIGNAL_LW = 7.1 * 72.0 / CANONICAL_DPI
AXIS_LW = 4.3 * 72.0 / CANONICAL_DPI
TICK_LW = 2.7 * 72.0 / CANONICAL_DPI
GRID_LW = 1.3 * 72.0 / CANONICAL_DPI
ANNOTATION_LW = 2.9 * 72.0 / CANONICAL_DPI

TICK_LABEL_SIZE = 35.6 * 72.0 / CANONICAL_DPI
AXIS_LABEL_SIZE = 53.3 * 72.0 / CANONICAL_DPI
TOP_LABEL_SIZE = 57.8 * 72.0 / CANONICAL_DPI
ANNOTATION_SIZE = 33.3 * 72.0 / CANONICAL_DPI

TICK_HALF_LEN = 8.25 / PX_PER_DATA_UNIT
X_TICK_LABEL_Y = -24.0 / PX_PER_DATA_UNIT
Y_TICK_LABEL_X = 18.0 / PX_PER_DATA_UNIT
ORIGIN_LABEL_X = 9.0 / PX_PER_DATA_UNIT
ORIGIN_LABEL_Y = -12.0 / PX_PER_DATA_UNIT
X_AXIS_LABEL_X_PAD = 15.0 / PX_PER_DATA_UNIT
X_AXIS_LABEL_Y = -4.5 / PX_PER_DATA_UNIT
Y_AXIS_LABEL_Y_PAD = 18.0 / PX_PER_DATA_UNIT

POLE_MARKER_SIZE = 19.0 * 72.0 / CANONICAL_DPI
POLE_MULTIPLICITY_SIZE = 22.0 * 72.0 / CANONICAL_DPI
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


def make_s_plane_figure(xlim, ylim):
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
    if isinstance(value, str):
        return value
    if abs(value - int(value)) < 1e-9:
        return rf"${int(value)}$"
    return rf"${value:g}$"


def setup_s_plane_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_axis_label=r"$\sigma$",
    y_axis_label=r"$j\omega$",
):
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

    x_axis_start, x_axis_end = xlim
    y_axis_start, y_axis_end = ylim
    ax.quiver(x_axis_start, 0, x_axis_end - x_axis_start, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y_axis_start, 0, y_axis_end - y_axis_start, **AXIS_ARROW_KW)

    for t in xticks:
        if abs(t) < 1e-12:
            continue
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(
            t,
            X_TICK_LABEL_Y,
            math_label(t),
            fontsize=TICK_LABEL_SIZE,
            ha="center",
            va="top",
            color=TICK_LABEL_COLOR,
            zorder=6,
        )

    for y in yticks:
        if abs(y) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(
            -Y_TICK_LABEL_X,
            y,
            math_label(y),
            fontsize=TICK_LABEL_SIZE,
            ha="right",
            va="center",
            color=TICK_LABEL_COLOR,
            zorder=6,
        )

    ax.text(
        ORIGIN_LABEL_X,
        ORIGIN_LABEL_Y,
        r"$0$",
        fontsize=TICK_LABEL_SIZE,
        ha="left",
        va="top",
        color=TICK_LABEL_COLOR,
        zorder=6,
    )

    ax.text(
        x_axis_end + X_AXIS_LABEL_X_PAD,
        X_AXIS_LABEL_Y,
        x_axis_label,
        fontsize=AXIS_LABEL_SIZE,
        ha="left",
        va="center",
        color=LABEL_COLOR,
        clip_on=False,
    )
    ax.text(
        0,
        y_axis_end + Y_AXIS_LABEL_Y_PAD,
        y_axis_label,
        fontsize=TOP_LABEL_SIZE,
        ha="center",
        va="bottom",
        color=LABEL_COLOR,
        clip_on=False,
    )


def draw_pole(ax, x, y, *, size=POLE_MARKER_SIZE):
    ax.plot(
        x,
        y,
        marker="o",
        markersize=size,
        markerfacecolor=SIGNAL_COLOR,
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=0.9,
        linestyle="None",
        zorder=7,
    )


def draw_double_pole(ax, x, y):
    draw_pole(ax, x, y, size=POLE_MARKER_SIZE * 0.95)
    draw_pole(ax, x + 0.05, y + 0.05, size=POLE_MARKER_SIZE * 0.70)
    ax.text(
        x + 0.18,
        y + 0.16,
        r"$\times 2$",
        fontsize=POLE_MULTIPLICITY_SIZE,
        ha="left",
        va="bottom",
        color=ANNOTATION_COLOR,
        zorder=8,
    )


def add_region_labels(ax, *, stable_xy, unstable_xy, boundary_xy):
    ax.text(
        stable_xy[0],
        stable_xy[1],
        "stable",
        fontsize=ANNOTATION_SIZE,
        ha="center",
        va="center",
        color=LABEL_COLOR,
        zorder=4,
    )
    ax.text(
        unstable_xy[0],
        unstable_xy[1],
        "unstable",
        fontsize=ANNOTATION_SIZE,
        ha="center",
        va="center",
        color=LABEL_COLOR,
        zorder=4,
    )
    ax.text(
        boundary_xy[0],
        boundary_xy[1],
        "imaginary-axis\nboundary",
        fontsize=ANNOTATION_SIZE * 0.92,
        ha="center",
        va="center",
        color=GUIDE_COLOR,
        rotation=90,
        rotation_mode="anchor",
        zorder=4,
    )


def main():
    xlim = (-5.5, 2.4)
    ylim = (-3.9, 3.9)
    fig, ax = make_s_plane_figure(xlim, ylim)

    setup_s_plane_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=[-5, -4, -3, -2, -1, 1, 2],
        yticks=[-3, -2, -1, 1, 2, 3],
    )

    add_region_labels(ax, stable_xy=(-3.7, 2.65), unstable_xy=(1.15, 2.65), boundary_xy=(0.15, 0.9))

    draw_pole(ax, -4.0, 0.0)
    draw_pole(ax, 0.0, 3.0)
    draw_pole(ax, 0.0, -3.0)

    out = Path(
        "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/13.5--circuit-transfer-functions-Images/images/l005-s006-qg-q002-q002.png"
    )
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=CANONICAL_DPI, bbox_inches="tight", facecolor="white")


if __name__ == "__main__":
    main()
