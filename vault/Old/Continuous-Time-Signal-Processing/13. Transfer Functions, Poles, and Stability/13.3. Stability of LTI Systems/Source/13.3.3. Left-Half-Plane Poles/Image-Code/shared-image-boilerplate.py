"""Shared matplotlib boilerplate for CTS EE01-M13-03 image generation.

This file is a reusable reference for topic workers. It intentionally avoids
rendering any specific figure so later workers can copy or adapt the helpers
without importing other local modules.
"""

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
    "axes.edgecolor": "#222222",
    "axes.labelcolor": "#444444",
    "xtick.color": "#444444",
    "ytick.color": "#444444",
})


COURSE_NAME = "Continuous Time Signal Processing"
COURSE_CODE = "CTS"
COURSE_ID = "EE01"
UNIT_NUMBER = 13
UNIT_NAME = "Unit 13"
MODULE_ID = "EE01-M13-03"
MODULE_NUMBER = "13.3"
MODULE_NAME = "Stability of LTI Systems"

CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150
INCHES_PER_DATA_UNIT = PX_PER_DATA_UNIT / CANONICAL_DPI

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

SIGNAL_LW = 7.1 * 72 / CANONICAL_DPI
SMOOTH_SIGNAL_LW = 5.2 * 72 / CANONICAL_DPI
AXIS_LW = 4.3 * 72 / CANONICAL_DPI
TICK_LW = 2.7 * 72 / CANONICAL_DPI
GRID_LW = 1.3 * 72 / CANONICAL_DPI
GUIDE_LW = 3.3 * 72 / CANONICAL_DPI
ANNOTATION_LW = 2.9 * 72 / CANONICAL_DPI

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

OPEN_MARKER_SIZE = 20.0 * 72 / CANONICAL_DPI
CLOSED_MARKER_SIZE = 17.8 * 72 / CANONICAL_DPI
ENDPOINT_EDGEWIDTH = 5.1 * 72 / CANONICAL_DPI

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

__all__ = [
    "np",
    "plt",
    "Path",
    "MultipleLocator",
    "COURSE_NAME",
    "COURSE_CODE",
    "COURSE_ID",
    "UNIT_NUMBER",
    "UNIT_NAME",
    "MODULE_ID",
    "MODULE_NUMBER",
    "MODULE_NAME",
    "CANONICAL_DPI",
    "PX_PER_DATA_UNIT",
    "INCHES_PER_DATA_UNIT",
    "MARGIN_LEFT_PX",
    "MARGIN_RIGHT_PX",
    "MARGIN_BOTTOM_PX",
    "MARGIN_TOP_PX",
    "SIGNAL_COLOR",
    "AXIS_COLOR",
    "LABEL_COLOR",
    "TICK_LABEL_COLOR",
    "GRID_COLOR",
    "GUIDE_COLOR",
    "ANNOTATION_COLOR",
    "SIGNAL_LW",
    "SMOOTH_SIGNAL_LW",
    "AXIS_LW",
    "TICK_LW",
    "GRID_LW",
    "GUIDE_LW",
    "ANNOTATION_LW",
    "TICK_LABEL_SIZE",
    "AXIS_LABEL_SIZE",
    "TOP_LABEL_SIZE",
    "ANNOTATION_SIZE",
    "TICK_HALF_LEN",
    "X_TICK_LABEL_Y",
    "Y_TICK_LABEL_X",
    "ORIGIN_LABEL_X",
    "ORIGIN_LABEL_Y",
    "X_AXIS_LABEL_X_PAD",
    "X_AXIS_LABEL_Y",
    "Y_AXIS_LABEL_Y_PAD",
    "OPEN_MARKER_SIZE",
    "CLOSED_MARKER_SIZE",
    "ENDPOINT_EDGEWIDTH",
    "AXIS_ARROW_SHAFT_WIDTH_DATA",
    "AXIS_ARROW_KW",
    "px_to_pt",
    "px_to_data",
    "make_ct_signal_figure",
    "math_label",
    "setup_ct_signal_axes",
    "plot_signal",
    "plot_smooth_signal",
    "plot_guide_line",
    "plot_open_marker",
    "plot_closed_marker",
    "draw_vertical_segment",
    "draw_horizontal_segment",
    "draw_exponential_tail",
    "save_figure",
]


def px_to_pt(px: float) -> float:
    return px * 72 / CANONICAL_DPI


def px_to_data(px: float) -> float:
    return px / PX_PER_DATA_UNIT


def make_ct_signal_figure(xlim, ylim):
    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]

    axes_w_px = x_range * PX_PER_DATA_UNIT
    axes_h_px = y_range * PX_PER_DATA_UNIT
    fig_w_px = MARGIN_LEFT_PX + axes_w_px + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_BOTTOM_PX + axes_h_px + MARGIN_TOP_PX

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


def setup_ct_signal_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_axis_label=r"$t$",
    y_axis_label=r"$x(t)$",
    show_grid=True,
    show_origin=True,
    y_tick_label_side="left",
    x_minor_grid_step=1,
    y_minor_grid_step=1,
    equal_aspect=True,
):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)

    if equal_aspect:
        ax.set_aspect("equal", adjustable="box")

    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.xaxis.set_minor_locator(MultipleLocator(x_minor_grid_step))
    ax.yaxis.set_minor_locator(MultipleLocator(y_minor_grid_step))

    if show_grid:
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

        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN],
                color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(t, X_TICK_LABEL_Y, math_label(t),
                fontsize=TICK_LABEL_SIZE, ha="center", va="top",
                color=TICK_LABEL_COLOR, zorder=6)

    for y in yticks:
        if abs(y) < 1e-12:
            continue

        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y],
                color=AXIS_COLOR, lw=TICK_LW, zorder=5)

        if y_tick_label_side == "right":
            ax.text(Y_TICK_LABEL_X, y, math_label(y),
                    fontsize=TICK_LABEL_SIZE, ha="left", va="center",
                    color=TICK_LABEL_COLOR, zorder=6)
        else:
            ax.text(-Y_TICK_LABEL_X, y, math_label(y),
                    fontsize=TICK_LABEL_SIZE, ha="right", va="center",
                    color=TICK_LABEL_COLOR, zorder=6)

    if show_origin:
        ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$",
                fontsize=TICK_LABEL_SIZE, ha="left", va="top",
                color=TICK_LABEL_COLOR, zorder=6)

    ax.text(x_axis_end + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, x_axis_label,
            fontsize=AXIS_LABEL_SIZE, ha="left", va="center",
            color=LABEL_COLOR, clip_on=False)

    ax.text(0, y_axis_end + Y_AXIS_LABEL_Y_PAD, y_axis_label,
            fontsize=TOP_LABEL_SIZE, ha="center", va="bottom",
            color=LABEL_COLOR, clip_on=False)


def plot_signal(ax, t, x, *, lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    ax.plot(
        t,
        x,
        color=color,
        linewidth=lw,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=zorder,
    )


def plot_smooth_signal(ax, t, x, *, lw=SMOOTH_SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    ax.plot(
        t,
        x,
        color=color,
        linewidth=lw,
        solid_capstyle="round",
        zorder=zorder,
    )


def plot_guide_line(ax, x1, y1, x2, y2, *, lw=GUIDE_LW, color=GUIDE_COLOR, zorder=3):
    ax.plot(
        [x1, x2],
        [y1, y2],
        color=color,
        linewidth=lw,
        linestyle=(0, (1.1, 2.4)),
        zorder=zorder,
    )


def plot_open_marker(ax, x, y, *, size=OPEN_MARKER_SIZE, edgewidth=ENDPOINT_EDGEWIDTH,
                     color=SIGNAL_COLOR, zorder=6):
    ax.plot(
        x,
        y,
        marker="o",
        markersize=size,
        markerfacecolor="white",
        markeredgecolor=color,
        markeredgewidth=edgewidth,
        linestyle="None",
        zorder=zorder,
    )


def plot_closed_marker(ax, x, y, *, size=CLOSED_MARKER_SIZE, edgewidth=ENDPOINT_EDGEWIDTH,
                       color=SIGNAL_COLOR, zorder=6):
    ax.plot(
        x,
        y,
        marker="o",
        markersize=size,
        markerfacecolor=color,
        markeredgecolor=color,
        markeredgewidth=edgewidth,
        linestyle="None",
        zorder=zorder,
    )


def draw_vertical_segment(ax, x, y0, y1, *, color=SIGNAL_COLOR, lw=SIGNAL_LW, zorder=4):
    ax.plot([x, x], [y0, y1], color=color, linewidth=lw, zorder=zorder)


def draw_horizontal_segment(ax, x0, x1, y, *, color=SIGNAL_COLOR, lw=SIGNAL_LW, zorder=4):
    ax.plot([x0, x1], [y, y], color=color, linewidth=lw, zorder=zorder)


def draw_exponential_tail(ax, t, t0, amplitude=1.0, decay=1.0, *, color=SIGNAL_COLOR,
                          lw=SMOOTH_SIGNAL_LW, zorder=4):
    t = np.asarray(t)
    y = amplitude * np.exp(-decay * (t - t0))
    y = np.where(t >= t0, y, np.nan)
    plot_smooth_signal(ax, t, y, lw=lw, color=color, zorder=zorder)


def save_figure(fig, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=CANONICAL_DPI, facecolor="white", bbox_inches="tight")

