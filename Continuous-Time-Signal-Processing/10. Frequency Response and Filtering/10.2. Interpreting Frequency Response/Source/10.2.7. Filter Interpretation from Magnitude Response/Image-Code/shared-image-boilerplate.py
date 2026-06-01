"""Shared matplotlib boilerplate for CTS module 10.2 frequency-response figures.

This file centralizes the canonical styling, sizing, and small plotting helpers
used by later topic workers for EE01-M10-02, Interpreting Frequency Response.
It is intentionally self-contained and uses only matplotlib, NumPy, and Path.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator


# ---------------------------------------------------------------------------
# Global style
# ---------------------------------------------------------------------------

BACKGROUND_COLOR = "white"


def configure_matplotlib() -> None:
    """Re-apply the shared serif and white-background defaults."""

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


# ---------------------------------------------------------------------------
# Shared module metadata
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

COURSE_NAME = "Continuous Time Signal Processing"
COURSE_CODE = "CTS"
COURSE_ID = "EE01"
UNIT_NUMBER = 10
UNIT_NAME = "Unit 10"
MODULE_ID = "EE01-M10-02"
MODULE_NUMBER = "10.2"
MODULE_NAME = "Interpreting Frequency Response"


# ---------------------------------------------------------------------------
# Canonical render scale
# ---------------------------------------------------------------------------

CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150
INCHES_PER_DATA_UNIT = PX_PER_DATA_UNIT / CANONICAL_DPI

MARGIN_LEFT_PX = 115
MARGIN_RIGHT_PX = 120
MARGIN_BOTTOM_PX = 95
MARGIN_TOP_PX = 110


def px_to_pt(px: float) -> float:
    """Convert pixels to points at the canonical render scale."""

    return px * 72 / CANONICAL_DPI


def px_to_data(px: float) -> float:
    """Convert pixels to data units at the canonical render scale."""

    return px / PX_PER_DATA_UNIT


# ---------------------------------------------------------------------------
# Shared visual constants
# ---------------------------------------------------------------------------

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"

GRID_ALPHA = 0.18
GUIDE_DASH_STYLE = (0, (1.1, 2.4))

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

BRACKET_CAP_HALF_LEN = px_to_data(9)
BRACKET_LABEL_GAP = px_to_data(18)
AMPLITUDE_CAP_HALF_LEN = px_to_data(10.5)

OPEN_MARKER_SIZE = px_to_pt(20.0)
CLOSED_MARKER_SIZE = px_to_pt(17.8)
ENDPOINT_EDGEWIDTH = px_to_pt(5.1)

DEFAULT_X_MINOR_GRID_STEP = 1
DEFAULT_Y_MINOR_GRID_STEP = 1

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


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def make_ct_signal_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
    """Create a CTS figure sized from explicit signal limits."""

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


def make_frequency_response_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
    """Alias for the standard CTS figure helper with a module-specific name."""

    return make_ct_signal_figure(xlim, ylim, dpi=dpi)


def math_label(value):
    """Format a tick value as math text."""

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
    x_axis_label=r"$t$",
    y_axis_label=r"$x(t)$",
    show_grid=True,
    show_origin=True,
    y_tick_label_side="left",
    x_minor_grid_step=DEFAULT_X_MINOR_GRID_STEP,
    y_minor_grid_step=DEFAULT_Y_MINOR_GRID_STEP,
    equal_aspect=True,
    show_x_tick_labels=True,
    show_y_tick_labels=True,
):
    """Configure a clean continuous-time signal axis layout."""

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

    # Draw axes with arrowheads only on positive ends.
    ax.quiver(x_axis_start, 0, x_axis_end - x_axis_start, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y_axis_start, 0, y_axis_end - y_axis_start, **AXIS_ARROW_KW)

    # Draw centered x-axis ticks and labels.
    for t in xticks:
        if abs(float(t)) < 1e-12:
            continue

        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN],
                color=AXIS_COLOR, lw=TICK_LW, zorder=5)

        if show_x_tick_labels:
            ax.text(t, X_TICK_LABEL_Y, math_label(t),
                    fontsize=TICK_LABEL_SIZE,
                    ha="center", va="top",
                    color=TICK_LABEL_COLOR,
                    zorder=6)

    # Draw centered y-axis ticks and labels.
    for y in yticks:
        if abs(float(y)) < 1e-12:
            continue

        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y],
                color=AXIS_COLOR, lw=TICK_LW, zorder=5)

        if show_y_tick_labels:
            if y_tick_label_side == "right":
                ax.text(Y_TICK_LABEL_X, y, math_label(y),
                        fontsize=TICK_LABEL_SIZE,
                        ha="left", va="center",
                        color=TICK_LABEL_COLOR,
                        zorder=6)
            else:
                ax.text(-Y_TICK_LABEL_X, y, math_label(y),
                        fontsize=TICK_LABEL_SIZE,
                        ha="right", va="center",
                        color=TICK_LABEL_COLOR,
                        zorder=6)

    # Manual origin label.
    if show_origin:
        ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$",
                fontsize=TICK_LABEL_SIZE,
                ha="left", va="top",
                color=TICK_LABEL_COLOR,
                zorder=6)

    # Axis labels.
    ax.text(x_axis_end + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, x_axis_label,
            fontsize=AXIS_LABEL_SIZE,
            ha="left", va="center",
            color=LABEL_COLOR,
            clip_on=False)

    ax.text(0, y_axis_end + Y_AXIS_LABEL_Y_PAD, y_axis_label,
            fontsize=TOP_LABEL_SIZE,
            ha="center", va="bottom",
            color=LABEL_COLOR,
            clip_on=False)


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
    x_minor_grid_step=DEFAULT_X_MINOR_GRID_STEP,
    y_minor_grid_step=DEFAULT_Y_MINOR_GRID_STEP,
    equal_aspect=True,
    show_x_tick_labels=True,
    show_y_tick_labels=True,
):
    """Configure a frequency-response axis layout using the shared CTS style."""

    setup_ct_signal_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=xticks,
        yticks=yticks,
        x_axis_label=x_axis_label,
        y_axis_label=y_axis_label,
        show_grid=show_grid,
        show_origin=show_origin,
        y_tick_label_side=y_tick_label_side,
        x_minor_grid_step=x_minor_grid_step,
        y_minor_grid_step=y_minor_grid_step,
        equal_aspect=equal_aspect,
        show_x_tick_labels=show_x_tick_labels,
        show_y_tick_labels=show_y_tick_labels,
    )


def plot_signal(ax, t, x, *, lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    """Plot a connected piecewise continuous-time signal trace."""

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
    """Plot a smooth signal curve."""

    ax.plot(
        t,
        x,
        color=color,
        linewidth=lw,
        solid_capstyle="round",
        zorder=zorder,
    )


def draw_open_endpoint(ax, t0, x0):
    """Draw an open endpoint marker."""

    ax.plot(
        t0,
        x0,
        marker="o",
        markersize=OPEN_MARKER_SIZE,
        markerfacecolor="white",
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=ENDPOINT_EDGEWIDTH,
        linestyle="None",
        zorder=6,
    )


def draw_closed_endpoint(ax, t0, x0):
    """Draw a closed endpoint marker."""

    ax.plot(
        t0,
        x0,
        marker="o",
        markersize=CLOSED_MARKER_SIZE,
        markerfacecolor=SIGNAL_COLOR,
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=ENDPOINT_EDGEWIDTH,
        linestyle="None",
        zorder=6,
    )


def draw_dotted_guide(ax, x_values, y_values):
    """Draw a subtle dotted guide line."""

    ax.plot(
        x_values,
        y_values,
        color=GUIDE_COLOR,
        linewidth=GUIDE_LW,
        linestyle=GUIDE_DASH_STYLE,
        zorder=3,
    )


def draw_horizontal_reference_line(
    ax,
    y,
    *,
    xlim=None,
    color=GUIDE_COLOR,
    linewidth=GUIDE_LW,
    linestyle=GUIDE_DASH_STYLE,
    zorder=3,
):
    """Draw a horizontal reference line across the current plot width."""

    if xlim is None:
        xlim = ax.get_xlim()

    ax.plot(
        [xlim[0], xlim[1]],
        [y, y],
        color=color,
        linewidth=linewidth,
        linestyle=linestyle,
        zorder=zorder,
    )


def draw_vertical_reference_line(
    ax,
    x,
    *,
    ylim=None,
    color=GUIDE_COLOR,
    linewidth=GUIDE_LW,
    linestyle=GUIDE_DASH_STYLE,
    zorder=3,
):
    """Draw a vertical reference line across the current plot height."""

    if ylim is None:
        ylim = ax.get_ylim()

    ax.plot(
        [x, x],
        [ylim[0], ylim[1]],
        color=color,
        linewidth=linewidth,
        linestyle=linestyle,
        zorder=zorder,
    )


def draw_unity_reference_line(
    ax,
    *,
    xlim=None,
    y=1.0,
    color=ANNOTATION_COLOR,
    linewidth=ANNOTATION_LW,
    linestyle="-",
    zorder=3,
):
    """Draw the unity reference line used on magnitude-response plots."""

    draw_horizontal_reference_line(
        ax,
        y,
        xlim=xlim,
        color=color,
        linewidth=linewidth,
        linestyle=linestyle,
        zorder=zorder,
    )


def save_figure(fig, output_path, *, dpi=CANONICAL_DPI, close=True):
    """Save a figure with the shared white background and tight bounding box."""

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        path,
        dpi=dpi,
        bbox_inches="tight",
        facecolor=BACKGROUND_COLOR,
        edgecolor=BACKGROUND_COLOR,
    )
    if close:
        plt.close(fig)
    return path
