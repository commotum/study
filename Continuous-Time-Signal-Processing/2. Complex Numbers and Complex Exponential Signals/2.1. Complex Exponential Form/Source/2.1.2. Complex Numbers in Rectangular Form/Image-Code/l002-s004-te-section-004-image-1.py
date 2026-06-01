from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator


def px_to_pt(px):
    return px * 72 / CANONICAL_DPI


def px_to_data(px):
    return px / PX_PER_DATA_UNIT


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

TICK_LW = px_to_pt(2.7)
GRID_LW = px_to_pt(1.3)
TICK_LABEL_SIZE = px_to_pt(35.6)
AXIS_LABEL_SIZE = px_to_pt(53.3)
TOP_LABEL_SIZE = px_to_pt(57.8)
CLOSED_MARKER_SIZE = px_to_pt(17.8)
ENDPOINT_EDGEWIDTH = px_to_pt(5.1)

TICK_HALF_LEN = px_to_data(8.25)
ORIGIN_LABEL_X = px_to_data(9)
ORIGIN_LABEL_Y = -px_to_data(12)
X_AXIS_LABEL_X_PAD = px_to_data(15)
X_AXIS_LABEL_Y = -px_to_data(4.5)
Y_AXIS_LABEL_Y_PAD = px_to_data(18)
X_TICK_LABEL_Y = -px_to_data(24)
Y_TICK_LABEL_X = px_to_data(18)
GRID_ALPHA = 0.18

AXIS_ARROW_KW = dict(
    angles="xy",
    scale_units="xy",
    scale=1,
    units="xy",
    width=px_to_data(4.3),
    headwidth=4.2,
    headlength=5.5,
    headaxislength=4.3,
    color=AXIS_COLOR,
    pivot="tail",
    clip_on=False,
)

OUTPUT_PATH = Path(r"/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/2.1--complex-exponential-form-Images/images/l002-s004-te-section-004-image-1.png")
POINT_X = 4
POINT_Y = -1


def configure_matplotlib():
    mpl.rcParams.update(
        {
            "mathtext.fontset": "cm",
            "font.family": "serif",
            "figure.facecolor": BACKGROUND_COLOR,
            "axes.facecolor": BACKGROUND_COLOR,
            "savefig.facecolor": BACKGROUND_COLOR,
            "axes.grid": False,
        }
    )


def math_label(value):
    if isinstance(value, str):
        return value
    numeric = float(value)
    rounded = round(numeric)
    if np.isclose(numeric, rounded):
        return rf"${int(rounded)}$"
    return rf"${numeric:g}$"


def make_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]
    fig_w_px = MARGIN_LEFT_PX + x_range * PX_PER_DATA_UNIT + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_BOTTOM_PX + y_range * PX_PER_DATA_UNIT + MARGIN_TOP_PX
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
    fig.savefig(
        output_path,
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        bbox_inches="tight",
    )


def setup_complex_plane_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_axis_label=r"$\Re\{z\}$",
    y_axis_label=r"$\Im\{z\}$",
    x_minor_grid_step=1,
    y_minor_grid_step=1,
):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.xaxis.set_minor_locator(MultipleLocator(x_minor_grid_step))
    ax.yaxis.set_minor_locator(MultipleLocator(y_minor_grid_step))
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
        if abs(t) < 1e-12:
            continue
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(t, X_TICK_LABEL_Y, math_label(t), fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR, zorder=6)

    for y in yticks:
        if abs(y) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(-Y_TICK_LABEL_X, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha="right", va="center", color=TICK_LABEL_COLOR, zorder=6)

    ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$", fontsize=TICK_LABEL_SIZE, ha="left", va="top", color=TICK_LABEL_COLOR, zorder=6)
    ax.text(x_axis_end + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, x_axis_label, fontsize=AXIS_LABEL_SIZE, ha="left", va="center", color=LABEL_COLOR, clip_on=False)
    ax.text(0, y_axis_end + Y_AXIS_LABEL_Y_PAD, y_axis_label, fontsize=TOP_LABEL_SIZE, ha="center", va="bottom", color=LABEL_COLOR, clip_on=False)


def draw_point(ax, x, y):
    ax.plot(
        x,
        y,
        marker="o",
        markersize=CLOSED_MARKER_SIZE,
        markerfacecolor=SIGNAL_COLOR,
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=ENDPOINT_EDGEWIDTH,
        linestyle="None",
        zorder=7,
    )


def main():
    configure_matplotlib()
    xlim = (-4.5, 6.5)
    ylim = (-5.5, 4.5)
    xticks = np.arange(-4, 7, 1)
    yticks = np.arange(-5, 5, 1)
    fig, ax = make_figure(xlim, ylim)
    setup_complex_plane_axes(ax, xlim=xlim, ylim=ylim, xticks=xticks, yticks=yticks)
    draw_point(ax, POINT_X, POINT_Y)
    save_figure(fig, OUTPUT_PATH)
    plt.close(fig)


if __name__ == "__main__":
    main()
