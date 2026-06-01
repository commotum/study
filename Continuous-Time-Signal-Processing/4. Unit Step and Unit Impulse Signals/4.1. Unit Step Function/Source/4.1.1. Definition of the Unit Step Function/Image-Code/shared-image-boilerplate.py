"""Reusable matplotlib boilerplate for CTS module image generation.

This module mirrors the continuous-time signal style guide and adds a few
step-specific helpers that are useful for Unit Step Function figures.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np


# ---------------------------------------------------------------------------
# Module metadata
# ---------------------------------------------------------------------------

COURSE_NAME = "Continuous Time Signal Processing"
COURSE_CODE = "CTS"
COURSE_ID = "EE01"
UNIT_NUMBER = 4
UNIT_NAME = "Unit 4"
MODULE_ID = "EE01-M04-01"
MODULE_NUMBER = 4.1
MODULE_NAME = "Unit Step Function"


# ---------------------------------------------------------------------------
# Paths and render scale
# ---------------------------------------------------------------------------

MODULE_ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = MODULE_ROOT
FIGURE_FACE_COLOR = "white"

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
# Styling defaults
# ---------------------------------------------------------------------------

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"

STYLE_DEFAULTS = {
    "mathtext.fontset": "cm",
    "font.family": "serif",
    "figure.facecolor": FIGURE_FACE_COLOR,
    "axes.facecolor": FIGURE_FACE_COLOR,
    "savefig.facecolor": FIGURE_FACE_COLOR,
    "axes.edgecolor": AXIS_COLOR,
    "axes.labelcolor": LABEL_COLOR,
    "xtick.color": TICK_LABEL_COLOR,
    "ytick.color": TICK_LABEL_COLOR,
    "grid.color": GRID_COLOR,
}

plt.rcParams.update(STYLE_DEFAULTS)


# ---------------------------------------------------------------------------
# Canonical sizes
# ---------------------------------------------------------------------------

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

OPEN_MARKER_SIZE = px_to_pt(20.0)
CLOSED_MARKER_SIZE = px_to_pt(17.8)
ENDPOINT_EDGEWIDTH = px_to_pt(5.1)

BRACKET_CAP_HALF_LEN = px_to_data(9)
BRACKET_LABEL_GAP = px_to_data(18)
AMPLITUDE_CAP_HALF_LEN = px_to_data(10.5)

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

GUIDE_LINESTYLE = (0, (1.1, 2.4))


# ---------------------------------------------------------------------------
# Figure helpers
# ---------------------------------------------------------------------------

def make_ct_signal_figure(xlim, ylim):
    """Create a canonical continuous-time signal figure."""
    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]

    axes_w_px = x_range * PX_PER_DATA_UNIT
    axes_h_px = y_range * PX_PER_DATA_UNIT
    fig_w_px = MARGIN_LEFT_PX + axes_w_px + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_BOTTOM_PX + axes_h_px + MARGIN_TOP_PX

    fig, ax = plt.subplots(
        figsize=(fig_w_px / CANONICAL_DPI, fig_h_px / CANONICAL_DPI),
        dpi=CANONICAL_DPI,
        facecolor=FIGURE_FACE_COLOR,
        constrained_layout=True,
    )

    return fig, ax


def save_figure(fig, path, *, tight=True, dpi=CANONICAL_DPI):
    """Persist a figure with the standard white background and tight crop."""
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        output,
        dpi=dpi,
        bbox_inches="tight" if tight else None,
        facecolor=FIGURE_FACE_COLOR,
    )
    return output


# ---------------------------------------------------------------------------
# Label formatting
# ---------------------------------------------------------------------------

def math_label(value):
    """Return a compact math-text label for tick values."""
    if isinstance(value, str):
        return value
    if abs(value - int(value)) < 1e-9:
        return rf"${int(value)}$"
    return rf"${value:g}$"


# ---------------------------------------------------------------------------
# Axis setup
# ---------------------------------------------------------------------------

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
    """Prepare a continuous-time signal axis with centered ticks and arrows."""
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)

    if equal_aspect:
        ax.set_aspect("equal", adjustable="box")

    ax.set_xticks(xticks)
    ax.set_yticks(yticks)

    if x_minor_grid_step is not None:
        ax.xaxis.set_minor_locator(MultipleLocator(x_minor_grid_step))
    if y_minor_grid_step is not None:
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
        if abs(y) < 1e-12:
            continue

        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
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


# ---------------------------------------------------------------------------
# Core plot primitives
# ---------------------------------------------------------------------------

def plot_signal(ax, t, x, *, lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    """Plot a connected continuous-time signal trace."""
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
    """Plot a smooth trace with rounded caps."""
    ax.plot(t, x, color=color, linewidth=lw, solid_capstyle="round", zorder=zorder)


def draw_open_endpoint(ax, t0, x0):
    """Draw an open endpoint marker for an excluded value."""
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
    """Draw a closed endpoint marker for an included value."""
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


def draw_dotted_guide(ax, x_values, y_values, *, color=GUIDE_COLOR, lw=GUIDE_LW):
    """Draw a gray dotted guide line."""
    ax.plot(x_values, y_values, color=color, linewidth=lw, linestyle=GUIDE_LINESTYLE, zorder=3)


# ---------------------------------------------------------------------------
# Brackets and guides
# ---------------------------------------------------------------------------

def draw_duration_bracket(
    ax,
    t_start,
    t_end,
    *,
    y=-0.38,
    label="duration",
    color=ANNOTATION_COLOR,
    lw=ANNOTATION_LW,
    label_gap=BRACKET_LABEL_GAP,
):
    """Draw a horizontal bracket used for support or duration annotation."""
    ax.plot([t_start, t_end], [y, y], color=color, linewidth=lw, zorder=5)
    ax.plot([t_start, t_start], [y - BRACKET_CAP_HALF_LEN, y + BRACKET_CAP_HALF_LEN], color=color, linewidth=lw, zorder=5)
    ax.plot([t_end, t_end], [y - BRACKET_CAP_HALF_LEN, y + BRACKET_CAP_HALF_LEN], color=color, linewidth=lw, zorder=5)
    if label:
        ax.text(
            (t_start + t_end) / 2,
            y - label_gap,
            label,
            fontsize=ANNOTATION_SIZE,
            ha="center",
            va="top",
            color=color,
        )


def draw_support_bracket(
    ax,
    t_start,
    t_end,
    *,
    y=-0.38,
    label="support",
    color=ANNOTATION_COLOR,
    lw=ANNOTATION_LW,
    label_gap=BRACKET_LABEL_GAP,
):
    """Draw a support bracket with the same geometry as a duration bracket."""
    draw_duration_bracket(
        ax,
        t_start,
        t_end,
        y=y,
        label=label,
        color=color,
        lw=lw,
        label_gap=label_gap,
    )


def draw_amplitude_bracket(
    ax,
    x,
    y_start,
    y_end,
    *,
    label="amplitude",
    color=ANNOTATION_COLOR,
    lw=ANNOTATION_LW,
    cap_half_len=AMPLITUDE_CAP_HALF_LEN,
    label_x_offset=px_to_data(10.5),
):
    """Draw a vertical bracket for amplitude or offset measurements."""
    ax.plot([x, x], [y_start, y_end], color=color, linewidth=lw, zorder=5)
    ax.plot([x - cap_half_len, x + cap_half_len], [y_start, y_start], color=color, linewidth=lw, zorder=5)
    ax.plot([x - cap_half_len, x + cap_half_len], [y_end, y_end], color=color, linewidth=lw, zorder=5)
    if label:
        ax.text(
            x + label_x_offset,
            (y_start + y_end) / 2,
            label,
            fontsize=ANNOTATION_SIZE,
            ha="left",
            va="center",
            color=color,
        )


# ---------------------------------------------------------------------------
# Step-function helpers
# ---------------------------------------------------------------------------

def unit_step(t, t0=0.0, amplitude=1.0, at_zero=1.0):
    """Return the unit-step response evaluated on an array or scalar."""
    t = np.asarray(t, dtype=float)
    return amplitude * np.heaviside(t - t0, at_zero)


def compose_step_signal(t, transitions, *, base_level=0.0, at_zero=1.0):
    """Compose a signal from step transitions at the given times.

    Parameters
    ----------
    t:
        Sample points where the signal is evaluated.
    transitions:
        Iterable of ``(amplitude, t0)`` pairs, where each amplitude is added at
        its transition time.
    base_level:
        Level before the first transition.
    at_zero:
        Value passed to ``np.heaviside`` at the transition time.
    """
    t = np.asarray(t, dtype=float)
    y = np.full_like(t, float(base_level), dtype=float)
    for amplitude, t0 in transitions:
        y += amplitude * np.heaviside(t - t0, at_zero)
    return y


def build_step_trace(xlim, transitions, *, initial_level=0.0):
    """Build connected polyline data for a piecewise-constant step trace."""
    left, right = float(xlim[0]), float(xlim[1])
    points = sorted(((float(t0), float(level)) for t0, level in transitions), key=lambda item: item[0])

    t_values = [left]
    x_values = [float(initial_level)]
    current_level = float(initial_level)

    for t0, next_level in points:
        t_values.extend([t0, t0])
        x_values.extend([current_level, next_level])
        current_level = next_level

    t_values.append(right)
    x_values.append(current_level)
    return np.asarray(t_values, dtype=float), np.asarray(x_values, dtype=float)


def plot_step_trace(ax, xlim, transitions, *, initial_level=0.0, lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    """Plot a connected step trace using repeated transition times."""
    t, x = build_step_trace(xlim, transitions, initial_level=initial_level)
    plot_signal(ax, t, x, lw=lw, color=color, zorder=zorder)
    return t, x


def build_pulse_trace(xlim, start, stop, *, low=0.0, high=1.0):
    """Build a rectangular pulse trace with vertical edges at the endpoints."""
    if stop < start:
        raise ValueError("stop must be greater than or equal to start")
    return build_step_trace(
        xlim,
        [(start, high), (stop, low)],
        initial_level=low,
    )


def plot_pulse_trace(ax, xlim, start, stop, *, low=0.0, high=1.0, lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    """Plot a rectangular pulse trace."""
    t, x = build_pulse_trace(xlim, start, stop, low=low, high=high)
    plot_signal(ax, t, x, lw=lw, color=color, zorder=zorder)
    return t, x

