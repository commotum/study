from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


plt.rcParams.update(
    {
        "mathtext.fontset": "cm",
        "font.family": "serif",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
    }
)

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

SIGNAL_LW = 7.1 * 72 / CANONICAL_DPI
AXIS_LW = 4.3 * 72 / CANONICAL_DPI
TICK_LW = 2.7 * 72 / CANONICAL_DPI
GRID_LW = 1.3 * 72 / CANONICAL_DPI

TICK_LABEL_SIZE = 35.6 * 72 / CANONICAL_DPI
AXIS_LABEL_SIZE = 53.3 * 72 / CANONICAL_DPI

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


def make_figure(xlim, ylim):
    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]
    fig_w_px = MARGIN_LEFT_PX + x_range * PX_PER_DATA_UNIT + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_BOTTOM_PX + y_range * PX_PER_DATA_UNIT + MARGIN_TOP_PX
    fig, ax = plt.subplots(
        figsize=(fig_w_px / CANONICAL_DPI, fig_h_px / CANONICAL_DPI),
        dpi=CANONICAL_DPI,
        constrained_layout=True,
    )
    return fig, ax


def math_label(value):
    if abs(value - round(value)) < 1e-9:
        return rf"${int(round(value))}$"
    return rf"${value:g}$"


def setup_axes(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks(np.arange(-4, 3, 1))
    ax.set_yticks(np.arange(-2, 3, 1))
    ax.xaxis.set_minor_locator(MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(MultipleLocator(0.5))
    ax.grid(True, which="both", linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    x_axis_start, x_axis_end = xlim
    y_axis_start, y_axis_end = ylim
    ax.quiver(x_axis_start, 0, x_axis_end - x_axis_start, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y_axis_start, 0, y_axis_end - y_axis_start, **AXIS_ARROW_KW)

    for t in np.arange(-4, 3, 1):
        if abs(t) < 1e-12:
            continue
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(t, X_TICK_LABEL_Y, math_label(t), fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR)

    for y in np.arange(-2, 3, 1):
        if abs(y) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(-Y_TICK_LABEL_X, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha="right", va="center", color=TICK_LABEL_COLOR)

    ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$", fontsize=TICK_LABEL_SIZE, ha="left", va="top", color=TICK_LABEL_COLOR)
    ax.text(x_axis_end + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, r"$\Re(s)$", fontsize=AXIS_LABEL_SIZE, ha="left", va="center", color=LABEL_COLOR, clip_on=False)
    ax.text(0, y_axis_end + Y_AXIS_LABEL_Y_PAD, r"$\Im(s)$", fontsize=AXIS_LABEL_SIZE, ha="center", va="bottom", color=LABEL_COLOR, clip_on=False)


def add_half_plane_shading_and_labels(ax, xlim):
    ax.axvspan(xlim[0], 0, facecolor="#dfeaf4", alpha=0.42, zorder=0)
    ax.axvspan(0, xlim[1], facecolor="#f4e4d9", alpha=0.38, zorder=0)
    ax.text(-4.1, 2.22, r"LHP: $\Re(s)<0$", fontsize=11, ha="left", va="center", color=LABEL_COLOR)
    ax.text(0.45, 2.22, r"RHP: $\Re(s)>0$", fontsize=11, ha="left", va="center", color=LABEL_COLOR)


def plot_pole(ax, z):
    ax.plot(
        z.real,
        z.imag,
        marker="x",
        markersize=9.2,
        markeredgewidth=2.2,
        color=SIGNAL_COLOR,
        linestyle="None",
        zorder=6,
    )


def plot_zero(ax, z):
    ax.plot(
        z.real,
        z.imag,
        marker="o",
        markersize=8.7,
        markerfacecolor="white",
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=2.0,
        linestyle="None",
        zorder=6,
    )


def save_figure(fig, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=CANONICAL_DPI, facecolor="white", bbox_inches="tight")


def render(output_path, poles, zeros, note_text, boundary_note):
    xlim = (-4.4, 2.4)
    ylim = (-2.6, 2.6)
    fig, ax = make_figure(xlim, ylim)
    add_half_plane_shading_and_labels(ax, xlim)
    setup_axes(ax, xlim, ylim)
    for pole in poles:
        plot_pole(ax, pole)
    for zero in zeros:
        plot_zero(ax, zero)
    ax.text(
        -4.15,
        -2.34,
        note_text,
        fontsize=8.2,
        ha="left",
        va="bottom",
        color=LABEL_COLOR,
        bbox=dict(boxstyle="round,pad=0.22", facecolor="white", edgecolor="#d0d0d0", alpha=0.9),
    )
    ax.text(
        -0.38,
        1.24,
        boundary_note,
        fontsize=8.1,
        ha="right",
        va="bottom",
        color=LABEL_COLOR,
    )
    save_figure(fig, output_path)
    plt.close(fig)


if __name__ == "__main__":
    output_path = Path(
        "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/13.3--stability-of-lti-systems-Images/images/l002-s004-qg-q002-q002.png"
    )
    poles = np.array([-2.0 + 0.0j, -1.0 - 1.0j, 0.0 + 1.0j])
    zeros = np.array([-3.0 + 0.0j, 2.0 + 0.0j])
    render(output_path, poles, zeros, r"Strict test: only poles with $\Re(p)<0$ are stable.", r"boundary pole at $\Re(s)=0$")
