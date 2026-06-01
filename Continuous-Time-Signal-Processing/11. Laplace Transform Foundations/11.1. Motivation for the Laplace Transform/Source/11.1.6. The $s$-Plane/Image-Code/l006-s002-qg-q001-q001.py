from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150
MARGIN_LEFT_PX = 115
MARGIN_RIGHT_PX = 120
MARGIN_BOTTOM_PX = 95
MARGIN_TOP_PX = 110

def px_to_pt(px):
    return px * 72 / CANONICAL_DPI

def px_to_data(px):
    return px / PX_PER_DATA_UNIT

plt.rcParams.update({
    "mathtext.fontset": "cm",
    "font.family": "serif",
})

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"

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

POINT_SIZE = px_to_pt(17.8)
POINT_EDGE = px_to_pt(4.3)

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
    x_axis_label="$\sigma$",
    y_axis_label="$j\omega$",
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
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(t, X_TICK_LABEL_Y, math_label(t), fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR, zorder=6)

    for y in yticks:
        if abs(y) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if y_tick_label_side == "right":
            ax.text(Y_TICK_LABEL_X, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha="left", va="center", color=TICK_LABEL_COLOR, zorder=6)
        else:
            ax.text(-Y_TICK_LABEL_X, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha="right", va="center", color=TICK_LABEL_COLOR, zorder=6)

    if show_origin:
        ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$", fontsize=TICK_LABEL_SIZE, ha="left", va="top", color=TICK_LABEL_COLOR, zorder=6)

    ax.text(x_axis_end + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, x_axis_label,
            fontsize=AXIS_LABEL_SIZE, ha="left", va="center", color=LABEL_COLOR, clip_on=False)
    ax.text(0, y_axis_end + Y_AXIS_LABEL_Y_PAD, y_axis_label,
            fontsize=TOP_LABEL_SIZE, ha="center", va="bottom", color=LABEL_COLOR, clip_on=False)

def draw_point(ax, sigma, omega, label=None):
    ax.plot(
        sigma,
        omega,
        marker="o",
        markersize=POINT_SIZE,
        markerfacecolor=SIGNAL_COLOR,
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=POINT_EDGE,
        linestyle="None",
        zorder=6,
    )
    if label is not None:
        dx = 0.35 if sigma >= 0 else -0.35
        dy = 0.30 if omega >= 0 else -0.30
        ha = "left" if sigma >= 0 else "right"
        if sigma == 0:
            ha = "right"
        va = "bottom" if omega >= 0 else "top"
        if sigma == 0 and omega < 0:
            ha = "left"
            va = "top"
        ax.text(sigma + dx, omega + dy, label,
                fontsize=ANNOTATION_SIZE,
                ha=ha,
                va=va,
                color=ANNOTATION_COLOR,
                zorder=7)

def draw_projection(ax, sigma, omega):
    ax.plot([sigma, sigma], [0.0, omega], color=GUIDE_COLOR, linewidth=GUIDE_LW,
            linestyle=(0, (1.1, 2.4)), zorder=3)
    ax.plot([0.0, sigma], [omega, omega], color=GUIDE_COLOR, linewidth=GUIDE_LW,
            linestyle=(0, (1.1, 2.4)), zorder=3)

def draw_annotation(ax, text, x, y, *, ha="center", va="center", size=ANNOTATION_SIZE*0.9):
    ax.text(x, y, text, fontsize=size, ha=ha, va=va, color=ANNOTATION_COLOR, zorder=7)

def save_figure(fig, output_path: Path):
    fig.savefig(output_path, dpi=CANONICAL_DPI, bbox_inches="tight", facecolor="white")

def main():
    xlim = (-6, 6)
    ylim = (-6, 6)
    xticks = list(range(-5, 6))
    yticks = list(range(-5, 6))

    fig, ax = make_ct_signal_figure(xlim, ylim)
    setup_ct_signal_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=xticks,
        yticks=yticks,
        x_axis_label=r"$\sigma$",
        y_axis_label=r"$j\omega$",
        show_grid=True,
        y_tick_label_side="left",
        x_minor_grid_step=1,
        y_minor_grid_step=1,
        equal_aspect=True,
    )

    pass

    output_path = Path(r"/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/11.1--motivation-for-the-laplace-transform-Images/images/l006-s002-qg-q001-q001.png")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    save_figure(fig, output_path)

if __name__ == "__main__":
    main()
