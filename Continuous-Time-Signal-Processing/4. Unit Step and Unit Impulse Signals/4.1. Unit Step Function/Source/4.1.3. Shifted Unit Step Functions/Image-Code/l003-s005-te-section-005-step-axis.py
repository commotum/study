"""Render a minimal shifted-unit-step time-axis diagram."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_PATH = Path(
    "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/"
    "2-Build-Lessons/4-Image-Generation/1-Outputs/"
    "Continuous-Time-Signal-Processing/4.1--unit-step-function-Images/"
    "images/l003-s005-te-section-005-step-axis.png"
)

BACKGROUND_COLOR = "white"
SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"

CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150

MARGIN_LEFT_PX = 115
MARGIN_RIGHT_PX = 120
MARGIN_BOTTOM_PX = 95
MARGIN_TOP_PX = 110

TICK_HALF_LEN = 8.25 / PX_PER_DATA_UNIT
X_TICK_LABEL_Y = -(24 / PX_PER_DATA_UNIT)
ORIGIN_LABEL_X = 9 / PX_PER_DATA_UNIT
ORIGIN_LABEL_Y = -(12 / PX_PER_DATA_UNIT)
X_AXIS_LABEL_X_PAD = 15 / PX_PER_DATA_UNIT
X_AXIS_LABEL_Y = -(4.5 / PX_PER_DATA_UNIT)
AXIS_ARROW_SHAFT_WIDTH_DATA = 4.3 / PX_PER_DATA_UNIT

SIGNAL_LW = 7.1 * 72 / CANONICAL_DPI
AXIS_LW = 4.3 * 72 / CANONICAL_DPI
TICK_LW = 2.7 * 72 / CANONICAL_DPI

TICK_LABEL_SIZE = 35.6 * 72 / CANONICAL_DPI
AXIS_LABEL_SIZE = 53.3 * 72 / CANONICAL_DPI
MARKER_LABEL_SIZE = 38.0 * 72 / CANONICAL_DPI
MARKER_EXPR_SIZE = 35.0 * 72 / CANONICAL_DPI

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


def px_to_pt(px):
    return px * 72 / CANONICAL_DPI


def px_to_data(px):
    return px / PX_PER_DATA_UNIT


def math_label(value):
    if isinstance(value, str):
        return value
    if abs(value - int(value)) < 1e-9:
        return rf"${int(value)}$"
    return rf"${value:g}$"


def make_figure(xlim, ylim):
    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]
    fig_w_px = MARGIN_LEFT_PX + x_range * PX_PER_DATA_UNIT + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_BOTTOM_PX + y_range * PX_PER_DATA_UNIT + MARGIN_TOP_PX
    fig, ax = plt.subplots(
        figsize=(fig_w_px / CANONICAL_DPI, fig_h_px / CANONICAL_DPI),
        dpi=CANONICAL_DPI,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=True,
    )
    return fig, ax


def draw_time_axis(ax, xlim):
    ax.quiver(
        xlim[0],
        0,
        xlim[1] - xlim[0],
        0,
        **AXIS_ARROW_KW,
    )


def draw_xticks(ax, ticks):
    for t in ticks:
        if abs(t) < 1e-12:
            continue
        ax.plot(
            [t, t],
            [-TICK_HALF_LEN, TICK_HALF_LEN],
            color=AXIS_COLOR,
            lw=TICK_LW,
            zorder=5,
        )
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


def draw_switch_marker(ax, t0, step_label, name_label):
    marker_top = 0.78
    ax.plot(
        [t0, t0],
        [0, marker_top],
        color=SIGNAL_COLOR,
        lw=SIGNAL_LW,
        solid_capstyle="butt",
        zorder=4,
    )
    ax.text(
        t0,
        1.08,
        name_label,
        fontsize=MARKER_LABEL_SIZE,
        ha="center",
        va="bottom",
        color=LABEL_COLOR,
        zorder=6,
    )
    ax.text(
        t0,
        0.90,
        step_label,
        fontsize=MARKER_EXPR_SIZE,
        ha="center",
        va="bottom",
        color=LABEL_COLOR,
        zorder=6,
    )


def save_figure(fig):
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        OUTPUT_PATH,
        dpi=CANONICAL_DPI,
        bbox_inches="tight",
        facecolor=BACKGROUND_COLOR,
    )


def main():
    plt.rcParams.update(
        {
            "mathtext.fontset": "cm",
            "font.family": "serif",
            "figure.facecolor": BACKGROUND_COLOR,
            "axes.facecolor": BACKGROUND_COLOR,
            "savefig.facecolor": BACKGROUND_COLOR,
        }
    )

    xlim = (-2.4, 6.15)
    ylim = (-0.35, 1.55)

    fig, ax = make_figure(xlim, ylim)

    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    draw_time_axis(ax, xlim)
    draw_xticks(ax, np.arange(-2, 7, 1))

    draw_switch_marker(ax, -1, r"$u(t+1)$", r"$y_2$")
    draw_switch_marker(ax, 2, r"$u(t-2)$", r"$y_1$")
    draw_switch_marker(ax, 5, r"$u(t-5)$", r"$y_3$")

    ax.text(
        xlim[1] + X_AXIS_LABEL_X_PAD,
        X_AXIS_LABEL_Y,
        r"$t$",
        fontsize=AXIS_LABEL_SIZE,
        ha="left",
        va="center",
        color=LABEL_COLOR,
        clip_on=False,
        zorder=7,
    )

    save_figure(fig)


if __name__ == "__main__":
    main()
