"""Shared matplotlib boilerplate for CTS continuous-time signal figures.

This module centralizes the textbook signal-plot styling used across
EE01-M08-04, Computing Fourier Series Coefficients. Later topic workers can
copy or adapt these helpers without re-reading the full style guide.

Only matplotlib and NumPy are used here. The module does not render any image
on import.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator


# ---------------------------------------------------------------------------
# Global matplotlib style
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Shared module metadata
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

COURSE_NAME = "Continuous Time Signal Processing"
COURSE_CODE = "CTS"
COURSE_ID = "EE01"
UNIT_NUMBER = 8
UNIT_NAME = "Unit 8"
MODULE_ID = "EE01-M08-04"
MODULE_NUMBER = "8.4"
MODULE_NAME = "Computing Fourier Series Coefficients"
LESSON_INDEX = 4
LESSON_TITLE = MODULE_NAME


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


def px_to_pt(px):
    """Convert pixels to points at the canonical render scale."""

    return px * 72 / CANONICAL_DPI


def px_to_data(px):
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

def configure_matplotlib():
    """Re-apply the shared serif and white-background defaults."""

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


def new_ct_figure(*, figsize=None, dpi=CANONICAL_DPI):
    """Create a generic CTS figure with the shared background and layout."""

    return plt.subplots(
        figsize=figsize,
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=True,
    )


def math_label(value):
    """Format a tick label as math text."""

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

    # Draw axes through the origin with arrowheads only on positive ends.
    ax.quiver(x_axis_start, 0, x_axis_end - x_axis_start, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y_axis_start, 0, y_axis_end - y_axis_start, **AXIS_ARROW_KW)

    for t in xticks:
        if np.isclose(t, 0):
            continue

        ax.plot(
            [t, t],
            [-TICK_HALF_LEN, TICK_HALF_LEN],
            color=AXIS_COLOR,
            lw=TICK_LW,
            zorder=5,
        )

        if show_x_tick_labels:
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
        if np.isclose(y, 0):
            continue

        ax.plot(
            [-TICK_HALF_LEN, TICK_HALF_LEN],
            [y, y],
            color=AXIS_COLOR,
            lw=TICK_LW,
            zorder=5,
        )

        if show_y_tick_labels:
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

    if x_axis_label is not None:
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

    if y_axis_label is not None:
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


def plot_signal(ax, t, x, *, lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    """Plot a connected piecewise continuous-time signal."""

    ax.plot(
        np.asarray(t),
        np.asarray(x),
        color=color,
        linewidth=lw,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=zorder,
    )


def plot_smooth_signal(ax, t, x, *, lw=SMOOTH_SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    """Plot a smooth continuous-time signal curve."""

    ax.plot(
        np.asarray(t),
        np.asarray(x),
        color=color,
        linewidth=lw,
        solid_capstyle="round",
        zorder=zorder,
    )


def draw_open_endpoint(ax, t0, x0):
    """Draw an open endpoint marker for excluded values."""

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
    """Draw a closed endpoint marker for included values."""

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
    """Draw a gray dotted guide line."""

    ax.plot(
        np.asarray(x_values),
        np.asarray(y_values),
        color=GUIDE_COLOR,
        linewidth=GUIDE_LW,
        linestyle=GUIDE_DASH_STYLE,
        zorder=3,
    )


def draw_duration_bracket(ax, t_start, t_end, *, y=-0.38, label="duration"):
    """Draw a support or duration bracket under a signal segment."""

    ax.plot(
        [t_start, t_end],
        [y, y],
        color=ANNOTATION_COLOR,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )
    ax.plot(
        [t_start, t_start],
        [y - BRACKET_CAP_HALF_LEN, y + BRACKET_CAP_HALF_LEN],
        color=ANNOTATION_COLOR,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )
    ax.plot(
        [t_end, t_end],
        [y - BRACKET_CAP_HALF_LEN, y + BRACKET_CAP_HALF_LEN],
        color=ANNOTATION_COLOR,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )

    if label is not None:
        ax.text(
            (t_start + t_end) / 2,
            y - BRACKET_LABEL_GAP,
            label,
            fontsize=ANNOTATION_SIZE,
            ha="center",
            va="top",
            color=ANNOTATION_COLOR,
        )


def draw_amplitude_bracket(ax, x_bracket, y0, y1, *, label=None):
    """Draw a vertical amplitude bracket between two levels."""

    ax.plot(
        [x_bracket, x_bracket],
        [y0, y1],
        color=ANNOTATION_COLOR,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )
    ax.plot(
        [x_bracket - AMPLITUDE_CAP_HALF_LEN, x_bracket + AMPLITUDE_CAP_HALF_LEN],
        [y0, y0],
        color=ANNOTATION_COLOR,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )
    ax.plot(
        [x_bracket - AMPLITUDE_CAP_HALF_LEN, x_bracket + AMPLITUDE_CAP_HALF_LEN],
        [y1, y1],
        color=ANNOTATION_COLOR,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )

    if label is not None:
        ax.text(
            x_bracket + px_to_data(14),
            (y0 + y1) / 2,
            label,
            fontsize=ANNOTATION_SIZE,
            ha="left",
            va="center",
            color=ANNOTATION_COLOR,
        )


def draw_offset_guide(ax, t_start, t_end, offset):
    """Draw a baseline guide at a constant offset."""

    draw_dotted_guide(ax, [t_start, t_end], [offset, offset])


def save_ct_signal_figure(fig, output_path, *, dpi=CANONICAL_DPI):
    """Save a signal figure with the shared white background."""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        output_path,
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        bbox_inches="tight",
    )
    return output_path

