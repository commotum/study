from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

BACKGROUND_COLOR = "white"
SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"
CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150
MARGIN_LEFT_PX = 115
MARGIN_RIGHT_PX = 120
MARGIN_BOTTOM_PX = 95
MARGIN_TOP_PX = 110
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
OPEN_MARKER_SIZE = 20.0 * 72 / CANONICAL_DPI
CLOSED_MARKER_SIZE = 17.8 * 72 / CANONICAL_DPI
ENDPOINT_EDGEWIDTH = 5.1 * 72 / CANONICAL_DPI
POLE_MARKER_SIZE = 21.0 * 72 / CANONICAL_DPI
POLE_MARKER_EDGEWIDTH = 5.1 * 72 / CANONICAL_DPI
X_TICK_LABEL_Y = -24 / PX_PER_DATA_UNIT
Y_TICK_LABEL_X = 18 / PX_PER_DATA_UNIT
ORIGIN_LABEL_X = 9 / PX_PER_DATA_UNIT
ORIGIN_LABEL_Y = -12 / PX_PER_DATA_UNIT
X_AXIS_LABEL_X_PAD = 15 / PX_PER_DATA_UNIT
X_AXIS_LABEL_Y = -4.5 / PX_PER_DATA_UNIT
Y_AXIS_LABEL_Y_PAD = 18 / PX_PER_DATA_UNIT
POINT_LABEL_OFFSET = (8 / PX_PER_DATA_UNIT, 8 / PX_PER_DATA_UNIT)
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


def configure_matplotlib():
    plt.rcParams.update(
        {
            "mathtext.fontset": "cm",
            "font.family": "serif",
            "figure.facecolor": BACKGROUND_COLOR,
            "axes.facecolor": BACKGROUND_COLOR,
            "savefig.facecolor": BACKGROUND_COLOR,
        }
    )


configure_matplotlib()


def px_to_pt(px):
    return px * 72 / CANONICAL_DPI


def px_to_data(px):
    return px / PX_PER_DATA_UNIT


def make_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]
    axes_w_px = x_range * PX_PER_DATA_UNIT
    axes_h_px = y_range * PX_PER_DATA_UNIT
    fig_w_px = MARGIN_LEFT_PX + axes_w_px + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_BOTTOM_PX + axes_h_px + MARGIN_TOP_PX
    fig, ax = plt.subplots(
        figsize=(fig_w_px / dpi, fig_h_px / dpi),
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=True,
    )
    return fig, ax


def math_label(value):
    if isinstance(value, str):
        return value
    numeric = float(value)
    rounded = round(numeric)
    if abs(numeric - rounded) < 1e-9:
        return rf"${int(rounded)}$"
    return rf"${numeric:g}$"


def setup_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_axis_label=r"$\sigma$",
    y_axis_label=r"$j\omega$",
    show_grid=True,
    show_origin=True,
    x_minor_grid_step=1,
    y_minor_grid_step=1,
):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    if x_minor_grid_step is not None and x_minor_grid_step > 0:
        ax.xaxis.set_minor_locator(MultipleLocator(x_minor_grid_step))
    if y_minor_grid_step is not None and y_minor_grid_step > 0:
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
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if abs(float(t)) >= 1e-12:
            ax.text(t, X_TICK_LABEL_Y, math_label(t), fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR, zorder=6)

    for y in yticks:
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if abs(float(y)) >= 1e-12:
            ax.text(-Y_TICK_LABEL_X, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha="right", va="center", color=TICK_LABEL_COLOR, zorder=6)

    if show_origin:
        ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$", fontsize=TICK_LABEL_SIZE, ha="left", va="top", color=TICK_LABEL_COLOR, zorder=6)

    if x_axis_label is not None:
        ax.text(x_axis_end + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, x_axis_label, fontsize=AXIS_LABEL_SIZE, ha="left", va="center", color=LABEL_COLOR, clip_on=False)
    if y_axis_label is not None:
        ax.text(0, y_axis_end + Y_AXIS_LABEL_Y_PAD, y_axis_label, fontsize=TOP_LABEL_SIZE, ha="center", va="bottom", color=LABEL_COLOR, clip_on=False)


def draw_zero(ax, x, y, *, label=None, label_offset=POINT_LABEL_OFFSET, zorder=6):
    ax.plot(
        x,
        y,
        marker="o",
        markersize=OPEN_MARKER_SIZE,
        markerfacecolor="white",
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=ENDPOINT_EDGEWIDTH,
        linestyle="None",
        zorder=zorder,
    )
    if label is not None:
        ax.text(x + label_offset[0], y + label_offset[1], label, fontsize=ANNOTATION_SIZE, ha="left", va="bottom", color=LABEL_COLOR, zorder=zorder + 1, clip_on=False)


def draw_pole(ax, x, y, *, label=None, label_offset=POINT_LABEL_OFFSET, zorder=6):
    ax.plot(
        x,
        y,
        marker="x",
        markersize=POLE_MARKER_SIZE,
        markeredgewidth=POLE_MARKER_EDGEWIDTH,
        color=SIGNAL_COLOR,
        linestyle="None",
        zorder=zorder,
    )
    if label is not None:
        ax.text(x + label_offset[0], y + label_offset[1], label, fontsize=ANNOTATION_SIZE, ha="left", va="bottom", color=LABEL_COLOR, zorder=zorder + 1, clip_on=False)


def draw_legend(ax, x, y):
    ax.plot(x, y, marker="o", markersize=OPEN_MARKER_SIZE, markerfacecolor="white", markeredgecolor=SIGNAL_COLOR, markeredgewidth=ENDPOINT_EDGEWIDTH, linestyle="None", zorder=7, clip_on=False)
    ax.text(x + 0.22, y, r"zero", fontsize=ANNOTATION_SIZE, ha="left", va="center", color=LABEL_COLOR, zorder=7, clip_on=False)
    ax.plot(x, y - 0.55, marker="x", markersize=POLE_MARKER_SIZE, markeredgewidth=POLE_MARKER_EDGEWIDTH, color=SIGNAL_COLOR, linestyle="None", zorder=7, clip_on=False)
    ax.text(x + 0.22, y - 0.55, r"pole", fontsize=ANNOTATION_SIZE, ha="left", va="center", color=LABEL_COLOR, zorder=7, clip_on=False)


def save_figure(fig, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=CANONICAL_DPI, bbox_inches="tight", facecolor=BACKGROUND_COLOR)
    plt.close(fig)


def main():
    xlim = (-3.5, 3.5)
    ylim = (-3.5, 3.5)
    fig, ax = make_figure(xlim, ylim)
    setup_axes(ax, xlim=xlim, ylim=ylim, xticks=[-3, -2, -1, 1, 2, 3], yticks=[-3, -2, -1, 1, 2, 3])
    draw_legend(ax, 1.65, 2.35)
    save_figure(fig, Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/13.2--poles-and-zeros-Images/images/l003-s003-qg-q002-q002.png'))

if __name__ == "__main__":
    main()
