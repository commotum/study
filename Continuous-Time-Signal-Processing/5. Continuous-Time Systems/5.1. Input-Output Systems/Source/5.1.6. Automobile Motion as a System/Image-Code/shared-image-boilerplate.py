"""Shared matplotlib boilerplate for Continuous-Time Signal Processing image generation."""

from __future__ import annotations

from pathlib import Path

import numpy as np
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt


# Global rendering defaults.
plt.rcParams.update({
    "mathtext.fontset": "cm",
    "font.family": "serif",
})


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


# Colors
SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"


# Line widths (points)
SIGNAL_LW = px_to_pt(7.1)
SMOOTH_SIGNAL_LW = px_to_pt(5.2)
AXIS_LW = px_to_pt(4.3)
TICK_LW = px_to_pt(2.7)
GRID_LW = px_to_pt(1.3)
GUIDE_LW = px_to_pt(3.3)
ANNOTATION_LW = px_to_pt(2.9)

# Font sizes (points)
TICK_LABEL_SIZE = px_to_pt(35.6)
AXIS_LABEL_SIZE = px_to_pt(53.3)
TOP_LABEL_SIZE = px_to_pt(57.8)
ANNOTATION_SIZE = px_to_pt(33.3)

# Tick/label offsets (data units)
TICK_HALF_LEN = px_to_data(8.25)
X_TICK_LABEL_Y = -px_to_data(24)
Y_TICK_LABEL_X = px_to_data(18)
ORIGIN_LABEL_X = px_to_data(9)
ORIGIN_LABEL_Y = -px_to_data(12)
X_AXIS_LABEL_X_PAD = px_to_data(15)
X_AXIS_LABEL_Y = -px_to_data(4.5)
Y_AXIS_LABEL_Y_PAD = px_to_data(18)

# Endpoint markers
OPEN_MARKER_SIZE = px_to_pt(20.0)
CLOSED_MARKER_SIZE = px_to_pt(17.8)
ENDPOINT_EDGEWIDTH = px_to_pt(5.1)

# Annotation helpers
BRACKET_CAP_HALF_LEN = px_to_data(9)
BRACKET_LABEL_GAP = px_to_data(18)

# Axis arrow style
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
    """Create a figure sized from explicit data-unit limits.

    This keeps 1 data unit equal on x and y because axis extents are converted
    to pixels by a shared scale before figure creation.
    """

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

    if isinstance(value, (int, np.integer)):
        return rf"${int(value)}$"

    if abs(value - np.pi) < 1e-12:
        return r"$\pi$"
    if abs(value - np.pi / 2) < 1e-12:
        return r"$\dfrac{\pi}{2}$"
    if abs(value - np.pi / 4) < 1e-12:
        return r"$\dfrac{\pi}{4}$"

    if abs(value - round(value)) < 1e-12:
        return rf"${int(round(value))}$"

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
    show_origin=True,
    y_tick_label_side="left",
    x_minor_grid_step=1,
    y_minor_grid_step=1,
    equal_aspect=True,
):
    """Apply standard CT-signal axes styling for a provided Axes object."""

    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)

    if equal_aspect:
        ax.set_aspect("equal", adjustable="box")

    ax.set_xticks(list(xticks))
    ax.set_yticks(list(yticks))

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
        if abs(float(t)) < 1e-12:
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

    for y in yticks:
        if abs(float(y)) < 1e-12:
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


def plot_signal(ax, t, x, *, lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    ax.plot(
        t,
        x,
        color=color,
        linewidth=lw,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=zorder,
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


def draw_open_endpoint(ax, t0, x0):
    ax.plot(
        [t0],
        [x0],
        marker="o",
        markersize=OPEN_MARKER_SIZE,
        markerfacecolor="white",
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=ENDPOINT_EDGEWIDTH,
        linestyle="None",
        zorder=6,
    )


def draw_closed_endpoint(ax, t0, x0):
    ax.plot(
        [t0],
        [x0],
        marker="o",
        markersize=CLOSED_MARKER_SIZE,
        markerfacecolor=SIGNAL_COLOR,
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=ENDPOINT_EDGEWIDTH,
        linestyle="None",
        zorder=6,
    )


def draw_dotted_guide(ax, x_values, y_values):
    ax.plot(
        x_values,
        y_values,
        color=GUIDE_COLOR,
        linewidth=GUIDE_LW,
        linestyle=(0, (1.1, 2.4)),
        zorder=3,
    )


def draw_duration_bracket(ax, t_start, t_end, br_y):
    ax.plot(
        [t_start, t_end],
        [br_y, br_y],
        color=ANNOTATION_COLOR,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )
    ax.plot(
        [t_start, t_start],
        [br_y - BRACKET_CAP_HALF_LEN, br_y + BRACKET_CAP_HALF_LEN],
        color=ANNOTATION_COLOR,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )
    ax.plot(
        [t_end, t_end],
        [br_y - BRACKET_CAP_HALF_LEN, br_y + BRACKET_CAP_HALF_LEN],
        color=ANNOTATION_COLOR,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )


def draw_duration_text(ax, t_start, t_end, br_y, text, *, fontsize=ANNOTATION_SIZE):
    ax.text(
        (t_start + t_end) / 2,
        br_y - BRACKET_LABEL_GAP,
        text,
        fontsize=fontsize,
        ha="center",
        va="top",
        color=ANNOTATION_COLOR,
    )


def save_ct_figure(fig, output_path):
    """Save a figure to the destination with standard export settings."""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=CANONICAL_DPI, facecolor="white", bbox_inches="tight")
    return output_path
