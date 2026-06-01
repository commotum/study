from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator


BACKGROUND_COLOR = "white"

plt.rcParams.update(
    {
        "mathtext.fontset": "cm",
        "font.family": "serif",
        "figure.facecolor": BACKGROUND_COLOR,
        "axes.facecolor": BACKGROUND_COLOR,
        "savefig.facecolor": BACKGROUND_COLOR,
    }
)


CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150
INCHES_PER_DATA_UNIT = PX_PER_DATA_UNIT / CANONICAL_DPI

MARGIN_LEFT_PX = 115
MARGIN_RIGHT_PX = 120
MARGIN_BOTTOM_PX = 95
MARGIN_TOP_PX = 110


def px_to_pt(px):
    return px * 72 / CANONICAL_DPI


def px_to_data(px):
    return px / PX_PER_DATA_UNIT


SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"

GRID_ALPHA = 0.18

SIGNAL_LW = px_to_pt(7.1)
SMOOTH_SIGNAL_LW = px_to_pt(5.2)
AXIS_LW = px_to_pt(4.3)
TICK_LW = px_to_pt(2.7)
GRID_LW = px_to_pt(1.3)
GUIDE_LW = px_to_pt(3.3)
ANNOTATION_LW = px_to_pt(2.9)

TICK_LABEL_SIZE = px_to_pt(35.6)
AXIS_LABEL_SIZE = px_to_pt(53.3)
TOP_LABEL_SIZE = px_to_pt(57.8)
ANNOTATION_SIZE = px_to_pt(33.3)

TICK_HALF_LEN = px_to_data(8.25)
X_TICK_LABEL_Y = -px_to_data(24)
Y_TICK_LABEL_X = px_to_data(18)
ORIGIN_LABEL_X = px_to_data(9)
ORIGIN_LABEL_Y = -px_to_data(12)
X_AXIS_LABEL_X_PAD = px_to_data(15)
X_AXIS_LABEL_Y = -px_to_data(4.5)
Y_AXIS_LABEL_Y_PAD = px_to_data(18)

BRACKET_CAP_HALF_LEN = px_to_data(9)
BRACKET_LABEL_GAP = px_to_data(18)
AMPLITUDE_CAP_HALF_LEN = px_to_data(10.5)

OPEN_MARKER_SIZE = px_to_pt(20.0)
CLOSED_MARKER_SIZE = px_to_pt(17.8)
ENDPOINT_EDGEWIDTH = px_to_pt(5.1)

DEFAULT_X_MINOR_GRID_STEP = 1
DEFAULT_Y_MINOR_GRID_STEP = 1

AXIS_ARROW_SHAFT_WIDTH_DATA = px_to_data(4.3)
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
    zorder=2,
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


def make_ct_signal_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
    x_range = float(xlim[1]) - float(xlim[0])
    y_range = float(ylim[1]) - float(ylim[0])
    if x_range <= 0 or y_range <= 0:
        raise ValueError("xlim and ylim must define increasing ranges")

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
    if np.isclose(numeric, rounded):
        return rf"${int(rounded)}$"
    return rf"${numeric:g}$"


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
    y_tick_label_side="right",
    x_minor_grid_step=DEFAULT_X_MINOR_GRID_STEP,
    y_minor_grid_step=DEFAULT_Y_MINOR_GRID_STEP,
    equal_aspect=True,
    show_x_tick_labels=True,
    show_y_tick_labels=True,
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
        if np.isclose(t, 0):
            continue

        ax.plot(
            [t, t],
            [-TICK_HALF_LEN, TICK_HALF_LEN],
            color=AXIS_COLOR,
            lw=TICK_LW,
            zorder=5,
        )
        if show_x_tick_labels:
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
        if np.isclose(y, 0):
            continue

        ax.plot(
            [-TICK_HALF_LEN, TICK_HALF_LEN],
            [y, y],
            color=AXIS_COLOR,
            lw=TICK_LW,
            zorder=5,
        )
        if show_y_tick_labels:
            if y_tick_label_side == "right":
                ax.text(
                    Y_TICK_LABEL_X,
                    y,
                    math_label(y),
                    fontsize=TICK_LABEL_SIZE,
                    ha="left",
                    va="center",
                    color=TICK_LABEL_COLOR,
                    zorder=6,
                )
            else:
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

    if show_origin:
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

    if x_axis_label is not None:
        ax.text(
            x_axis_end + X_AXIS_LABEL_X_PAD,
            X_AXIS_LABEL_Y,
            x_axis_label,
            fontsize=AXIS_LABEL_SIZE,
            ha="left",
            va="center",
            color=LABEL_COLOR,
            clip_on=False,
            zorder=6,
        )

    if y_axis_label is not None:
        ax.text(
            0,
            y_axis_end + Y_AXIS_LABEL_Y_PAD,
            y_axis_label,
            fontsize=TOP_LABEL_SIZE,
            ha="center",
            va="bottom",
            color=LABEL_COLOR,
            clip_on=False,
            zorder=6,
        )


def plot_signal(ax, t, x, *, lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    ax.plot(
        np.asarray(t),
        np.asarray(x),
        color=color,
        linewidth=lw,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=zorder,
    )


def draw_duration_bracket(ax, start, end, y=-0.38, *, label=None):
    ax.plot(
        [start, end],
        [y, y],
        color=ANNOTATION_COLOR,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )
    ax.plot(
        [start, start],
        [y - BRACKET_CAP_HALF_LEN, y + BRACKET_CAP_HALF_LEN],
        color=ANNOTATION_COLOR,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )
    ax.plot(
        [end, end],
        [y - BRACKET_CAP_HALF_LEN, y + BRACKET_CAP_HALF_LEN],
        color=ANNOTATION_COLOR,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )
    if label is not None:
        ax.text(
            (start + end) / 2,
            y - BRACKET_LABEL_GAP,
            label,
            fontsize=ANNOTATION_SIZE,
            ha="center",
            va="top",
            color=ANNOTATION_COLOR,
        )


def draw_amplitude_bracket(ax, x_bracket, y0, y1, *, label=None):
    ax.plot(
        [x_bracket, x_bracket],
        [y0, y1],
        color=ANNOTATION_COLOR,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )
    ax.plot(
        [x_bracket - AMPLITUDE_CAP_HALF_LEN, x_bracket + AMPLITUDE_CAP_HALF_LEN],
        [y0, y0],
        color=ANNOTATION_COLOR,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )
    ax.plot(
        [x_bracket - AMPLITUDE_CAP_HALF_LEN, x_bracket + AMPLITUDE_CAP_HALF_LEN],
        [y1, y1],
        color=ANNOTATION_COLOR,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )
    if label is not None:
        ax.text(
            x_bracket,
            y1 + px_to_data(14),
            label,
            fontsize=ANNOTATION_SIZE,
            ha="center",
            va="bottom",
            color=ANNOTATION_COLOR,
        )


def save_ct_signal_figure(fig, output_path, *, dpi=CANONICAL_DPI):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        output_path,
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        bbox_inches="tight",
    )
    return output_path


def rectangular_periodic_trace(amplitude, width, period, left_pad, right_pad):
    t = np.array(
        [
            left_pad,
            0.0,
            0.0,
            width,
            width,
            period,
            period,
            period + width,
            period + width,
            right_pad,
        ],
        dtype=float,
    )
    x = np.array([0.0, 0.0, amplitude, amplitude, 0.0, 0.0, amplitude, amplitude, 0.0, 0.0], dtype=float)
    return t, x


AMPLITUDE = 3
PULSE_WIDTH = 2
PERIOD = 8

LEFT_PAD = 1.45
RIGHT_PAD = 1.35
X_LEFT = -LEFT_PAD
X_RIGHT = PERIOD + PULSE_WIDTH + RIGHT_PAD
Y_MIN = -1.55
Y_MAX = AMPLITUDE + 1.25

XTICKS = [0, 2, 4, 6, 8, 10]
YTICKS = [1, 2, 3]

OUTPUT_PATH = Path(
    "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/8.4--computing-fourier-series-coefficients-Images/images/l002-s002-te-section-002-plot-1.png"
)


def main():
    fig, ax = make_ct_signal_figure((X_LEFT, X_RIGHT), (Y_MIN, Y_MAX))
    setup_ct_signal_axes(
        ax,
        xlim=(X_LEFT, X_RIGHT),
        ylim=(Y_MIN, Y_MAX),
        xticks=XTICKS,
        yticks=YTICKS,
        x_axis_label=r"$t$",
        y_axis_label=r"$x(t)$",
        y_tick_label_side="right",
    )

    t, x = rectangular_periodic_trace(AMPLITUDE, PULSE_WIDTH, PERIOD, X_LEFT + 0.10, X_RIGHT - 0.10)
    plot_signal(ax, t, x)
    draw_amplitude_bracket(ax, -0.82, 0, AMPLITUDE, label=rf"$A={AMPLITUDE}$")
    draw_duration_bracket(ax, 0, PULSE_WIDTH, y=-0.45, label=rf"$\tau={PULSE_WIDTH}$")
    draw_duration_bracket(ax, 0, PERIOD, y=-1.02, label=rf"$T={PERIOD}$")

    save_ct_signal_figure(fig, OUTPUT_PATH)
    plt.close(fig)


if __name__ == "__main__":
    main()
