from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.ticker import MultipleLocator

"""Reusable matplotlib/numpy boilerplate for Continuous-Time Signal Basics images.

This module provides shared style constants and helper functions for topic-image
workers. It does not generate or save a specific image by itself.
"""

# ---------------------------------------------------------------------------
# Module/session metadata
# ---------------------------------------------------------------------------
COURSE_NAME = "Continuous Time Signal Processing"
COURSE_CODE = "CTS"
COURSE_ID = "EE01"
UNIT_NUMBER = 1
UNIT_NAME = "Unit 1"
MODULE_ID = "EE01-M01-01"
MODULE_NUMBER = "1.1"
MODULE_NAME = "Continuous-Time Signal Basics"


# ---------------------------------------------------------------------------
# Canonical geometry / typography
# ---------------------------------------------------------------------------
CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150
INCHES_PER_DATA_UNIT = PX_PER_DATA_UNIT / CANONICAL_DPI

MARGIN_LEFT_PX = 115
MARGIN_RIGHT_PX = 120
MARGIN_BOTTOM_PX = 95
MARGIN_TOP_PX = 110


# ---------------------------------------------------------------------------
# Style palette
# ---------------------------------------------------------------------------
def _configure_global_style() -> None:
    rcParams.update({
        "mathtext.fontset": "cm",
        "font.family": "serif",
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
        "axes.facecolor": "white",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.spines.left": False,
        "axes.spines.bottom": False,
    })


SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"


# ---------------------------------------------------------------------------
# Typographic and drawing scales
# ---------------------------------------------------------------------------
def px_to_pt(px: float) -> float:
    return px * 72 / CANONICAL_DPI


def px_to_data(px: float) -> float:
    return px / PX_PER_DATA_UNIT


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

SIGNAL_LW = px_to_pt(7.1)
SMOOTH_SIGNAL_LW = px_to_pt(5.2)
AXIS_LW = px_to_pt(4.3)
TICK_LW = px_to_pt(2.7)
GRID_LW = px_to_pt(1.3)
GUIDE_LW = px_to_pt(3.3)
ANNOTATION_LW = px_to_pt(2.9)

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
)


# Initialize defaults on import.
_configure_global_style()


# ---------------------------------------------------------------------------
# Figure + axis helpers
# ---------------------------------------------------------------------------
def make_ct_signal_figure(
    xlim: tuple[float, float],
    ylim: tuple[float, float],
    *,
    dpi: int = CANONICAL_DPI,
    constrained_layout: bool = True,
):
    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]

    axes_w_px = x_range * PX_PER_DATA_UNIT
    axes_h_px = y_range * PX_PER_DATA_UNIT
    fig_w_px = MARGIN_LEFT_PX + axes_w_px + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_BOTTOM_PX + axes_h_px + MARGIN_TOP_PX

    fig, ax = plt.subplots(
        figsize=(fig_w_px / dpi, fig_h_px / dpi),
        dpi=dpi,
        facecolor="white",
        constrained_layout=constrained_layout,
    )
    return fig, ax


def math_label(value) -> str:
    if isinstance(value, str):
        return value
    numeric_value = float(value)
    if np.isclose(numeric_value, round(numeric_value)):
        return rf"${int(round(numeric_value))}$"
    return rf"${numeric_value:g}$"


def setup_ct_signal_axes(
    ax,
    *,
    xlim: tuple[float, float],
    ylim: tuple[float, float],
    xticks: list[float],
    yticks: list[float],
    x_axis_label: str = r"$t$",
    y_axis_label: str = r"$x(t)$",
    show_grid: bool = True,
    show_origin: bool = True,
    y_tick_label_side: str = "left",
    x_minor_grid_step: float = 1,
    y_minor_grid_step: float = 1,
    equal_aspect: bool = True,
    grid_alpha: float = 0.18,
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
        ax.grid(True, which="both", linewidth=GRID_LW, alpha=grid_alpha, color=GRID_COLOR)
        ax.set_axisbelow(True)

    # Draw a small origin tick cross whenever 0 is one of the requested major ticks.
    if any(abs(t) < 1e-12 for t in xticks) or any(abs(y) < 1e-12 for y in yticks):
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [0, 0], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.plot([0, 0], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.tick_params(
        left=False,
        bottom=False,
        labelleft=False,
        labelbottom=False,
    )

    x_axis_start, x_axis_end = xlim
    y_axis_start, y_axis_end = ylim

    # Axes with arrowheads on positive ends only.
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

    # Centered x-axis ticks and labels.
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

    # Centered y-axis ticks and labels.
    for y in yticks:
        if abs(y) < 1e-12:
            continue
        ax.plot(
            [-TICK_HALF_LEN, TICK_HALF_LEN],
            [y, y],
            color=AXIS_COLOR,
            lw=TICK_LW,
            zorder=5,
        )

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

    ax.text(
        x_axis_end + X_AXIS_LABEL_X_PAD,
        X_AXIS_LABEL_Y,
        x_axis_label,
        fontsize=AXIS_LABEL_SIZE,
        ha="left",
        va="center",
        color=LABEL_COLOR,
        clip_on=False,
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
    )


def plot_signal(
    ax,
    t: np.ndarray | list[float],
    x: np.ndarray | list[float],
    *,
    linewidth: float = SIGNAL_LW,
    color: str = SIGNAL_COLOR,
    zorder: int = 4,
) -> None:
    ax.plot(
        t,
        x,
        color=color,
        linewidth=linewidth,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=zorder,
    )


def plot_smooth_signal(
    ax,
    t: np.ndarray | list[float],
    x: np.ndarray | list[float],
    *,
    linewidth: float = SMOOTH_SIGNAL_LW,
    color: str = SIGNAL_COLOR,
    zorder: int = 4,
) -> None:
    ax.plot(
        t,
        x,
        color=color,
        linewidth=linewidth,
        solid_capstyle="round",
        zorder=zorder,
    )


def draw_open_endpoint(ax, t0: float, x0: float, *, color: str = SIGNAL_COLOR) -> None:
    ax.plot(
        t0,
        x0,
        marker="o",
        markersize=OPEN_MARKER_SIZE,
        markerfacecolor="white",
        markeredgecolor=color,
        markeredgewidth=ENDPOINT_EDGEWIDTH,
        linestyle="None",
        zorder=6,
    )


def draw_closed_endpoint(ax, t0: float, x0: float, *, color: str = SIGNAL_COLOR) -> None:
    ax.plot(
        t0,
        x0,
        marker="o",
        markersize=CLOSED_MARKER_SIZE,
        markerfacecolor=color,
        markeredgecolor=color,
        markeredgewidth=ENDPOINT_EDGEWIDTH,
        linestyle="None",
        zorder=6,
    )


def draw_dotted_guide(ax, x_values, y_values, *, color: str = GUIDE_COLOR) -> None:
    ax.plot(
        x_values,
        y_values,
        color=color,
        linewidth=GUIDE_LW,
        linestyle=(0, (1.1, 2.4)),
        zorder=3,
    )


def save_figure(fig, output_path: str | Path, *, dpi: int = CANONICAL_DPI) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=dpi, facecolor="white", bbox_inches="tight")

OUTPUT_PATH = r"/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/1.1--continuous-time-signal-basics-Images/images/l003-s003-qg-q001-prompt-q001.png"

POINT_MARKER_SIZE = px_to_pt(13.3)

def draw_point(ax, t0, x0):
    ax.plot(
        t0,
        x0,
        marker="o",
        markersize=POINT_MARKER_SIZE,
        markerfacecolor=SIGNAL_COLOR,
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=0.0,
        linestyle="None",
        zorder=6,
    )

def main():
    xlim = (-1.8, 3.8)
    ylim = (-2.8, 2.8)
    fig, ax = make_ct_signal_figure(xlim, ylim)
    setup_ct_signal_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=[-1, 0, 1, 3],
        yticks=[-2, 0, 2],
        x_axis_label=r"$t$",
        y_axis_label=r"$x(t)$",
    )
    plot_signal(ax, [-1, 1], [-2, 2])
    plot_signal(ax, [1, 3], [2, 0])
    draw_point(ax, -1, -2)
    draw_point(ax, 1, 2)
    draw_point(ax, 3, 0)
    save_figure(fig, OUTPUT_PATH)
    plt.close(fig)

if __name__ == "__main__":
    main()
