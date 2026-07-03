
"""Render the centered magnitude-spectrum stem plot for q001-choice-e."""

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

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GRID_ALPHA = 0.18

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

SIGNAL_LW = px_to_pt(7.1)
AXIS_LW = px_to_pt(4.3)
TICK_LW = px_to_pt(2.7)
GRID_LW = px_to_pt(1.3)

TICK_LABEL_SIZE = px_to_pt(35.6)
AXIS_LABEL_SIZE = px_to_pt(53.3)
TOP_LABEL_SIZE = px_to_pt(57.8)

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
    zorder=2,
)

STEM_MARKER_SIZE = px_to_pt(18.0)

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

SPEC = {'covered_template': 'magnitude-spectrum-stem-plot',
 'equal_aspect': True,
 'render_notes': ['Centered distractor spectrum that keeps only the positive-index stems and drops the mirrored '
                  'negative harmonics.',
                  'Matches the other q001 choices in axis scale and styling.'],
 'show_grid': True,
 'show_origin': True,
 'stems': [(0, 4.0), (1, 3.0), (2, 0.5)],
 'x_axis_label': '$k$',
 'x_minor_grid_step': 1,
 'xlim': (-2.7, 2.7),
 'xticks': [-2, -1, 1, 2],
 'y_axis_label': '$M_k$',
 'y_minor_grid_step': 0.5,
 'y_tick_label_side': 'left',
 'ylim': (-4.4, 4.4),
 'yticks': [-4, -3, -2, -1, 1, 2, 3, 4]}
OUTPUT_PATH = Path("/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/8.4--computing-fourier-series-coefficients-Images/images/l007-s004-qg-q001-choice-e-q001-choice-e.png")

def make_ct_signal_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
    x_range = float(xlim[1]) - float(xlim[0])
    y_range = float(ylim[1]) - float(ylim[0])
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
    x_axis_label=r"$k$",
    y_axis_label=r"$M_k$",
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
        if np.isclose(t, 0):
            continue
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(t, X_TICK_LABEL_Y, math_label(t), fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR, zorder=6)
    for y in yticks:
        if np.isclose(y, 0):
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if y_tick_label_side == "right":
            ax.text(Y_TICK_LABEL_X, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha="left", va="center", color=TICK_LABEL_COLOR, zorder=6)
        else:
            ax.text(-Y_TICK_LABEL_X, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha="right", va="center", color=TICK_LABEL_COLOR, zorder=6)
    if show_origin:
        ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$", fontsize=TICK_LABEL_SIZE, ha="left", va="top", color=TICK_LABEL_COLOR, zorder=6)
    if x_axis_label is not None:
        ax.text(x_axis_end + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, x_axis_label, fontsize=AXIS_LABEL_SIZE, ha="left", va="center", color=LABEL_COLOR, clip_on=False, zorder=6)
    if y_axis_label is not None:
        ax.text(0, y_axis_end + Y_AXIS_LABEL_Y_PAD, y_axis_label, fontsize=TOP_LABEL_SIZE, ha="center", va="bottom", color=LABEL_COLOR, clip_on=False, zorder=6)

def draw_stem_series(ax, stems, *, color=SIGNAL_COLOR, lw=SIGNAL_LW, marker_size=STEM_MARKER_SIZE):
    for k, height in sorted(stems, key=lambda pair: pair[0]):
        if np.isclose(height, 0):
            continue
        ax.plot([k, k], [0.0, height], color=color, linewidth=lw, solid_capstyle="butt", solid_joinstyle="miter", zorder=4)
        ax.plot(k, height, marker="o", markersize=marker_size, markerfacecolor=color, markeredgecolor=color, linestyle="None", zorder=5)

def save_figure(fig, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=CANONICAL_DPI, facecolor=BACKGROUND_COLOR, bbox_inches="tight")
    plt.close(fig)
    return output_path

def render():
    fig, ax = make_ct_signal_figure(SPEC["xlim"], SPEC["ylim"])
    setup_ct_signal_axes(
        ax,
        xlim=SPEC["xlim"],
        ylim=SPEC["ylim"],
        xticks=SPEC["xticks"],
        yticks=SPEC["yticks"],
        x_axis_label=SPEC.get("x_axis_label", r"$k$"),
        y_axis_label=SPEC.get("y_axis_label", r"$M_k$"),
        show_grid=SPEC.get("show_grid", True),
        show_origin=SPEC.get("show_origin", True),
        y_tick_label_side=SPEC.get("y_tick_label_side", "left"),
        x_minor_grid_step=SPEC.get("x_minor_grid_step", 1),
        y_minor_grid_step=SPEC.get("y_minor_grid_step", 0.5),
        equal_aspect=SPEC.get("equal_aspect", True),
    )
    draw_stem_series(ax, SPEC["stems"])
    save_figure(fig, OUTPUT_PATH)

if __name__ == "__main__":
    render()
