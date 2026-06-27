
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

BACKGROUND_COLOR = "white"

def configure_matplotlib():
    plt.rcParams.update(
        {
            "mathtext.fontset": "cm",
            "font.family": "serif",
            "figure.facecolor": BACKGROUND_COLOR,
            "axes.facecolor": BACKGROUND_COLOR,
            "savefig.facecolor": BACKGROUND_COLOR,
            "savefig.edgecolor": BACKGROUND_COLOR,
        }
    )

configure_matplotlib()

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

GRID_ALPHA = 0.18
GUIDE_DASH_STYLE = (0, (1.1, 2.4))

def px_to_pt(px):
    return px * 72 / CANONICAL_DPI

def px_to_data(px):
    return px / PX_PER_DATA_UNIT

SIGNAL_LW = px_to_pt(7.1)
SMOOTH_SIGNAL_LW = px_to_pt(5.2)
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

OPEN_MARKER_SIZE = px_to_pt(20.0)
CLOSED_MARKER_SIZE = px_to_pt(17.8)
ENDPOINT_EDGEWIDTH = px_to_pt(5.1)

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

def setup_frequency_response_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_axis_label=r"$\omega$",
    y_axis_label=r"$|H(j\omega)|$",
    show_grid=True,
    show_origin=True,
    y_tick_label_side="left",
    x_minor_grid_step=1,
    y_minor_grid_step=0.5,
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
        if abs(float(t)) < 1e-12:
            continue
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(t, X_TICK_LABEL_Y, math_label(t), fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR, zorder=6)

    for y in yticks:
        if abs(float(y)) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if y_tick_label_side == "right":
            ax.text(Y_TICK_LABEL_X, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha="left", va="center", color=TICK_LABEL_COLOR, zorder=6)
        else:
            ax.text(-Y_TICK_LABEL_X, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha="right", va="center", color=TICK_LABEL_COLOR, zorder=6)

    if show_origin:
        ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$", fontsize=TICK_LABEL_SIZE, ha="left", va="top", color=TICK_LABEL_COLOR, zorder=6)

    ax.text(x_axis_end + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, x_axis_label, fontsize=AXIS_LABEL_SIZE, ha="left", va="center", color=LABEL_COLOR, clip_on=False)
    ax.text(0, y_axis_end + Y_AXIS_LABEL_Y_PAD, y_axis_label, fontsize=TOP_LABEL_SIZE, ha="center", va="bottom", color=LABEL_COLOR, clip_on=False)

def plot_smooth_signal(ax, t, x, *, lw=SMOOTH_SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    ax.plot(t, x, color=color, linewidth=lw, solid_capstyle="round", zorder=zorder)

def draw_dotted_guide(ax, x_values, y_values):
    ax.plot(x_values, y_values, color=GUIDE_COLOR, linewidth=GUIDE_LW, linestyle=GUIDE_DASH_STYLE, zorder=3)

def draw_unity_reference_line(ax, *, xlim, y=1.0):
    ax.plot([xlim[0], xlim[1]], [y, y], color=ANNOTATION_COLOR, linewidth=ANNOTATION_LW, linestyle="-", zorder=3)

def mark_endpoint(ax, x, y, label, *, label_y=-0.24):
    draw_dotted_guide(ax, [x, x], [0, y])
    ax.plot(
        x,
        y,
        marker="o",
        markersize=CLOSED_MARKER_SIZE,
        markerfacecolor=SIGNAL_COLOR,
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=ENDPOINT_EDGEWIDTH,
        linestyle="None",
        zorder=6,
    )
    ax.text(x, label_y, label, fontsize=ANNOTATION_SIZE, ha="center", va="top", color=ANNOTATION_COLOR)

def save_figure(fig, output_path, *, dpi=CANONICAL_DPI):
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=dpi, bbox_inches="tight", facecolor=BACKGROUND_COLOR, edgecolor=BACKGROUND_COLOR)
    plt.close(fig)
    return path

OUTPUT_PATH = Path(r"/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/10.2--interpreting-frequency-response-Images/images/l007-s004-qg-q002-q002.png")


def response(x):
    s = 0.5 * (1.0 + np.tanh((x - 2.85) / 0.58))
    return 0.4 + (1.5 - 0.4) * s


def main():
    xlim = (0.0, 6.0)
    ylim = (0.0, 1.9)
    fig, ax = make_ct_signal_figure(xlim, ylim)
    setup_frequency_response_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=[1, 3, 5],
        yticks=[0.5, 1.0, 1.5],
    )
    draw_unity_reference_line(ax, xlim=xlim, y=1.0)

    x = np.linspace(0.0, 6.0, 801)
    y = response(x)
    plot_smooth_signal(ax, x, y)

    x_low = 0.65
    x_high = 5.35
    mark_endpoint(ax, x_low, response(x_low), r"$\omega_L$")
    mark_endpoint(ax, x_high, response(x_high), r"$\omega_H$")

    save_figure(fig, OUTPUT_PATH)


if __name__ == "__main__":
    main()
