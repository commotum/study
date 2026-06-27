from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

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
GRID_LW = 1.3 * 72 / CANONICAL_DPI
GUIDE_LW = 3.3 * 72 / CANONICAL_DPI
TICK_LW = 2.7 * 72 / CANONICAL_DPI
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
    y_tick_label_side="left",
    x_minor_grid_step=1,
    y_minor_grid_step=1,
):
    plt.rcParams.update(
        {
            "mathtext.fontset": "cm",
            "font.family": "serif",
        }
    )

    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
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

    ax.quiver(
        x_axis_start,
        0,
        x_axis_end - x_axis_start,
        0,
        **AXIS_ARROW_KW,
    )
    ax.quiver(
        0,
        y_axis_start,
        0,
        y_axis_end - y_axis_start,
        **AXIS_ARROW_KW,
    )

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
        ax.plot([ -TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
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
        zorder=6,
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
        zorder=6,
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


def add_trend_arrow(ax, x, y, direction, color=ANNOTATION_COLOR):
    if direction == "left":
        ax.annotate(
            "",
            xy=(x - 0.8, y + 0.7),
            xytext=(x, y - 0.9),
            arrowprops=dict(arrowstyle="->", color=color, linewidth=2.4, shrinkA=0, shrinkB=0),
            clip_on=False,
        )
    elif direction == "right":
        ax.annotate(
            "",
            xy=(x + 0.8, y + 0.7),
            xytext=(x, y - 0.9),
            arrowprops=dict(arrowstyle="->", color=color, linewidth=2.4, shrinkA=0, shrinkB=0),
            clip_on=False,
        )


def save_figure(fig, output_path):
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_file, dpi=CANONICAL_DPI, bbox_inches="tight", facecolor="white")


def main():
    xlim = (-5, 5)
    ylim = (-8, 8)

    fig, ax = make_ct_signal_figure(xlim, ylim)
    setup_ct_signal_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=[-5, -3, -1, 1, 3, 5],
        yticks=[-8, -6, -4, -2, 2, 4, 6, 8],
        x_axis_label=r"$t$",
        y_axis_label=r"$x(t)$",
        x_minor_grid_step=1,
        y_minor_grid_step=2,
    )

    t = np.linspace(-5.0, 5.0, 4000)
    envelope = 3.0 + 0.4 * np.abs(t + 5.0)
    carrier = np.cos((2 * np.pi / 5.0) * t)
    x = envelope * carrier

    plot_smooth_signal(ax, t, x)

    ax.plot(t, envelope, color=ANNOTATION_COLOR, lw=GUIDE_LW, linestyle=(0, (1.1, 2.4)), zorder=3)
    ax.plot(t, -envelope, color=ANNOTATION_COLOR, lw=GUIDE_LW, linestyle=(0, (1.1, 2.4)), zorder=3)

    add_trend_arrow(ax, -5.0, x[0], "left")
    add_trend_arrow(ax, 5.0, x[-1], "right")

    save_figure(fig, "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/5.4--stability-Images/images/l001-s004-qg-q002-q002.png")


if __name__ == "__main__":
    main()
