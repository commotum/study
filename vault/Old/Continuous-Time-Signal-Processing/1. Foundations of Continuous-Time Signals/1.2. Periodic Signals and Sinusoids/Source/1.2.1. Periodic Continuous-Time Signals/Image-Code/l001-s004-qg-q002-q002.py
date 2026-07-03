from __future__ import annotations

from pathlib import Path

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np


BACKGROUND_COLOR = "white"
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

X_TICK_LABEL_Y = -24 / PX_PER_DATA_UNIT
Y_TICK_LABEL_X = 18 / PX_PER_DATA_UNIT
ORIGIN_LABEL_X = 9 / PX_PER_DATA_UNIT
ORIGIN_LABEL_Y = -12 / PX_PER_DATA_UNIT
X_AXIS_LABEL_X_PAD = 15 / PX_PER_DATA_UNIT
X_AXIS_LABEL_Y = -4.5 / PX_PER_DATA_UNIT
Y_AXIS_LABEL_Y_PAD = 18 / PX_PER_DATA_UNIT

BRACKET_CAP_HALF_LEN = 9 / PX_PER_DATA_UNIT
BRACKET_LABEL_GAP = 18 / PX_PER_DATA_UNIT

AXIS_ARROW_SHAFT_WIDTH_DATA = 4.3 / PX_PER_DATA_UNIT
VECTOR_ARROW_SHAFT_WIDTH_DATA = 4.3 / PX_PER_DATA_UNIT

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

GRID_ALPHA = 0.18
GRID_LINESTYLE = (0, (1.1, 2.4))

OUTPUT_PATH = Path(
    "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/"
    "2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/"
    "1.2--periodic-signals-and-sinusoids-Images/images/l001-s004-qg-q002-q002.png"
)

PHASE_KNOTS = np.array([0.0, 0.08, 0.18, 0.32, 0.44, 0.57, 0.70, 0.86, 1.0], dtype=float)
SHAPE_VALUES = np.array([0.25, 1.05, 0.65, -0.55, 0.35, 1.15, 0.45, -0.10, 0.25], dtype=float)

PERIOD = 5.0
START_TIME = 1.0
VERTICAL_OFFSET = 1.35
AMPLITUDE_SCALE = 1.0
X_LIM = (-0.40, 11.40)
Y_LIM = (-0.95, 3.05)
XTICKS = np.arange(0, 12, 1)
YTICKS = np.array([0, 1, 2, 3], dtype=float)
BRACKET_X0 = 1.0
BRACKET_X1 = 6.0
BRACKET_Y = -0.45
BRACKET_LABEL = None


def configure_matplotlib():
    mpl.rcParams.update(
        {
            "mathtext.fontset": "cm",
            "font.family": "serif",
            "figure.facecolor": BACKGROUND_COLOR,
            "axes.facecolor": BACKGROUND_COLOR,
            "savefig.facecolor": BACKGROUND_COLOR,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.spines.left": False,
            "axes.spines.bottom": False,
            "axes.grid": False,
        }
    )


configure_matplotlib()


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


def save_figure(fig, output_path, *, dpi=CANONICAL_DPI):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=dpi, bbox_inches="tight", facecolor=BACKGROUND_COLOR)


def math_label(value):
    if isinstance(value, str):
        return value
    numeric = float(value)
    rounded = round(numeric)
    if np.isclose(numeric, rounded):
        return rf"${int(rounded)}$"
    return rf"${numeric:g}$"


def draw_bracket(ax, x0, x1, y, *, label=None):
    ax.plot([x0, x1], [y, y], color=ANNOTATION_COLOR, lw=ANNOTATION_LW, zorder=5)
    ax.plot(
        [x0, x0],
        [y - BRACKET_CAP_HALF_LEN, y + BRACKET_CAP_HALF_LEN],
        color=ANNOTATION_COLOR,
        lw=ANNOTATION_LW,
        zorder=5,
    )
    ax.plot(
        [x1, x1],
        [y - BRACKET_CAP_HALF_LEN, y + BRACKET_CAP_HALF_LEN],
        color=ANNOTATION_COLOR,
        lw=ANNOTATION_LW,
        zorder=5,
    )
    if label is not None:
        ax.text(
            (x0 + x1) / 2,
            y + BRACKET_LABEL_GAP,
            label,
            fontsize=ANNOTATION_SIZE,
            ha="center",
            va="bottom",
            color=ANNOTATION_COLOR,
            zorder=6,
        )


def setup_axes(ax, *, xlim, ylim, xticks, yticks):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(1))
    ax.grid(True, which="both", linewidth=GRID_LW, alpha=GRID_ALPHA, color=GRID_COLOR)
    ax.set_axisbelow(True)

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    x_axis_start, x_axis_end = xlim
    y_axis_start, y_axis_end = ylim
    ax.quiver(x_axis_start, 0, x_axis_end - x_axis_start, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y_axis_start, 0, y_axis_end - y_axis_start, **AXIS_ARROW_KW)

    for t in xticks:
        if np.isclose(float(t), 0.0):
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
        if np.isclose(float(y), 0.0):
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
        r"$t$",
        fontsize=AXIS_LABEL_SIZE,
        ha="left",
        va="center",
        color=LABEL_COLOR,
        clip_on=False,
    )
    ax.text(
        0,
        y_axis_end + Y_AXIS_LABEL_Y_PAD,
        r"$x(t)$",
        fontsize=TOP_LABEL_SIZE,
        ha="center",
        va="bottom",
        color=LABEL_COLOR,
        clip_on=False,
    )


def periodic_shape(t, *, period, start_time=0.0, vertical_offset=0.0, amplitude_scale=1.0):
    phase = np.mod(np.asarray(t, dtype=float) - start_time, period) / period
    return vertical_offset + amplitude_scale * np.interp(phase, PHASE_KNOTS, SHAPE_VALUES)


def main():
    t = np.linspace(X_LIM[0], X_LIM[1], 4800)
    x = periodic_shape(
        t,
        period=PERIOD,
        start_time=START_TIME,
        vertical_offset=VERTICAL_OFFSET,
        amplitude_scale=AMPLITUDE_SCALE,
    )

    fig, ax = make_figure(X_LIM, Y_LIM)
    setup_axes(ax, xlim=X_LIM, ylim=Y_LIM, xticks=XTICKS, yticks=YTICKS)

    ax.plot(
        t,
        x,
        color=SIGNAL_COLOR,
        linewidth=SIGNAL_LW,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=4,
    )

    draw_bracket(ax, BRACKET_X0, BRACKET_X1, BRACKET_Y, label=BRACKET_LABEL)

    save_figure(fig, OUTPUT_PATH)


if __name__ == "__main__":
    main()
