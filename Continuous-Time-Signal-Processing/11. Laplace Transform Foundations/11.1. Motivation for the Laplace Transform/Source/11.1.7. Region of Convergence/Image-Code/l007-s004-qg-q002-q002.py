"""ROC shading example image for boundary sigma = 2, left half-plane."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np


CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150
INCHES_PER_DATA_UNIT = PX_PER_DATA_UNIT / CANONICAL_DPI

MARGIN_LEFT_PX = 115
MARGIN_RIGHT_PX = 120
MARGIN_BOTTOM_PX = 95
MARGIN_TOP_PX = 110


def px_to_pt(px: float) -> float:
    return px * 72 / CANONICAL_DPI


def px_to_data(px: float) -> float:
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
ANNOTATION_COLOR = "#555555"

SIGNAL_LW = px_to_pt(7.1)
AXIS_LW = px_to_pt(4.3)
TICK_LW = px_to_pt(2.7)
GRID_LW = px_to_pt(1.3)

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


def make_ct_figure(xlim, ylim):
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
    if abs(value - int(value)) < 1e-9:
        return f"${int(value)}$"
    return f"${value:g}$"


def setup_axes(ax, *, xlim, ylim, xticks, yticks):
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

    for x in xticks:
        if abs(x) < 1e-12:
            continue
        ax.plot([x, x], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(x, X_TICK_LABEL_Y, math_label(x), fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR)

    for y in yticks:
        if abs(y) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(-Y_TICK_LABEL_X, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha="right", va="center", color=TICK_LABEL_COLOR)

    ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, "$0$", fontsize=TICK_LABEL_SIZE, ha="left", va="top", color=TICK_LABEL_COLOR)
    ax.text(x_axis_end + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, r"$\sigma$", fontsize=AXIS_LABEL_SIZE, ha="left", va="center", color=LABEL_COLOR, clip_on=False)
    ax.text(0, y_axis_end + Y_AXIS_LABEL_Y_PAD, r"$j\omega$", fontsize=TOP_LABEL_SIZE, ha="center", va="bottom", color=LABEL_COLOR, clip_on=False)


def mark_boundary_half_plane(ax, *, xlim, ylim, sigma0, shade_right=False):
    ymin, ymax = ylim
    if shade_right:
        x_fill = [sigma0, xlim[1]]
    else:
        x_fill = [xlim[0], sigma0]

    ax.fill_betweenx(np.array([ymin, ymax]), np.array([x_fill[0], x_fill[0]]), np.array([x_fill[1], x_fill[1]]),
                    color=SIGNAL_COLOR, alpha=0.10, zorder=1)

    ax.plot([sigma0, sigma0], [ymin, ymax], color=AXIS_COLOR, lw=AXIS_LW, linestyle=(0, (3, 2.2)), zorder=4)
    ax.plot(
        [sigma0], [ymin + px_to_data(8)],
        marker="o",
        markersize=px_to_pt(12.0),
        markerfacecolor="white",
        markeredgecolor=AXIS_COLOR,
        markeredgewidth=px_to_pt(2.4),
        linestyle="None",
        zorder=6,
    )
    ax.plot(
        [sigma0], [ymax - px_to_data(8)],
        marker="o",
        markersize=px_to_pt(12.0),
        markerfacecolor="white",
        markeredgecolor=AXIS_COLOR,
        markeredgewidth=px_to_pt(2.4),
        linestyle="None",
        zorder=6,
    )

    boundary = "{:.0f}".format(sigma0) if abs(sigma0 - int(sigma0)) < 1e-9 else "{:.3g}".format(sigma0)
    ax.text(sigma0 + px_to_data(5), ymax - px_to_data(12), rf"$\sigma={boundary}$ (excluded)",
            fontsize=ANNOTATION_SIZE, ha="left", va="top", color=ANNOTATION_COLOR, zorder=6)


def main():
    xlim = (-4.5, 4.5)
    ylim = (-3.5, 3.5)
    fig, ax = make_ct_figure(xlim, ylim)

    setup_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=[-4, -3, -2, -1, 0, 1, 2, 3, 4],
        yticks=[-3, -2, -1, 0, 1, 2, 3],
    )

    mark_boundary_half_plane(ax, xlim=xlim, ylim=ylim, sigma0=2, shade_right=False)

    output_path = Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/11.1--motivation-for-the-laplace-transform-Images/images/l007-s004-qg-q002-q002.png')
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=CANONICAL_DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()