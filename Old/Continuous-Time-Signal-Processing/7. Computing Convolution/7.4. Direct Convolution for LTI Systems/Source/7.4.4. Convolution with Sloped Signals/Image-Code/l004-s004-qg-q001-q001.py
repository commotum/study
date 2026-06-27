"""Shared matplotlib boilerplate for CTS continuous-time signal figures.

This module centralizes the textbook signal-plot styling used across
EE01-M07-04, Direct Convolution for LTI Systems. Later topic workers can copy
or adapt these helpers without re-reading the full style guide.

Only matplotlib and NumPy are used here. The module does not render any image
on import.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


# ---------------------------------------------------------------------------
# Global matplotlib style
# ---------------------------------------------------------------------------

plt.rcParams.update(
    {
        "mathtext.fontset": "cm",
        "font.family": "serif",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
    }
)


# ---------------------------------------------------------------------------
# Shared lesson metadata
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

COURSE_NAME = "Continuous Time Signal Processing"
COURSE_CODE = "CTS"
COURSE_ID = "EE01"
UNIT_NUMBER = 7
UNIT_NAME = "Unit 7"
MODULE_ID = "EE01-M07-04"
MODULE_NUMBER = "7.4"
MODULE_NAME = "Direct Convolution for LTI Systems"
LESSON_INDEX = 4
LESSON_TITLE = "Convolution with Sloped Signals"


# ---------------------------------------------------------------------------
# Shared constants
# ---------------------------------------------------------------------------

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"

BACKGROUND_COLOR = "white"

SIGNAL_LW = 3.2
SMOOTH_SIGNAL_LW = 2.35
AXIS_LW = 1.4
TICK_LW = 1.2
GRID_LW = 0.6
GUIDE_LW = 1.5

TICK_LABEL_SIZE = 16
AXIS_LABEL_SIZE = 24
TOP_LABEL_SIZE = 26
ANNOTATION_SIZE = 15

TICK_HALF_LEN = 0.055
OPEN_MARKER_SIZE = 9
CLOSED_MARKER_SIZE = 8
ENDPOINT_EDGEWIDTH = 2.3

DEFAULT_FIGSIZE = (9.12, 7.68)
SQUARE_FIGSIZE = (5.6, 5.6)
DEFAULT_DPI = 160

AXIS_ARROW_KW = dict(
    angles="xy",
    scale_units="xy",
    scale=1,
    width=0.0048,
    headwidth=4.2,
    headlength=5.5,
    headaxislength=4.3,
    color=AXIS_COLOR,
    pivot="tail",
    clip_on=False,
)


# ---------------------------------------------------------------------------
# Small helpers
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


def make_figure(*, square=False, dpi=DEFAULT_DPI):
    """Create a standard CTS figure and axes pair."""

    figsize = SQUARE_FIGSIZE if square else DEFAULT_FIGSIZE
    return plt.subplots(figsize=figsize, dpi=dpi)


def math_label(value):
    """Format a tick value or label for math text."""

    if isinstance(value, str):
        return value
    if abs(value - int(value)) < 1e-9:
        return rf"${int(value)}$"
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
    equal_aspect=True,
):
    """Configure axes to match the continuous-time signal style guide."""

    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)

    if equal_aspect:
        ax.set_aspect("equal", adjustable="box")

    ax.set_xticks(xticks)
    ax.set_yticks(yticks)

    if show_grid:
        ax.grid(True, linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
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

        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN],
                color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(
            t,
            -0.16,
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

        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y],
                color=AXIS_COLOR, lw=TICK_LW, zorder=5)

        if y_tick_label_side == "right":
            ax.text(
                0.12,
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
                -0.12,
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
            0.06,
            -0.08,
            r"$0$",
            fontsize=TICK_LABEL_SIZE,
            ha="left",
            va="top",
            color=TICK_LABEL_COLOR,
            zorder=6,
        )

    x_pad = 0.08 * (xlim[1] - xlim[0]) / 6
    y_pad = 0.08 * (ylim[1] - ylim[0]) / 4

    ax.text(
        x_axis_end + x_pad,
        -0.03,
        x_axis_label,
        fontsize=AXIS_LABEL_SIZE,
        ha="left",
        va="center",
        color=LABEL_COLOR,
        clip_on=False,
    )

    ax.text(
        0,
        y_axis_end + y_pad,
        y_axis_label,
        fontsize=TOP_LABEL_SIZE,
        ha="center",
        va="bottom",
        color=LABEL_COLOR,
        clip_on=False,
    )

    return ax


def plot_signal(ax, t, x, *, lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    """Draw a connected piecewise continuous-time signal trace."""

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
    """Draw a smooth curve with rounded caps."""

    ax.plot(
        t,
        x,
        color=color,
        linewidth=lw,
        solid_capstyle="round",
        zorder=zorder,
    )


def draw_open_endpoint(ax, t0, x0):
    """Draw an open-circle endpoint."""

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
    """Draw a closed-circle endpoint."""

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


def draw_dotted_guide(ax, x_values, y_values, *, zorder=3):
    """Draw a subtle dotted guide line."""

    ax.plot(
        x_values,
        y_values,
        color=GUIDE_COLOR,
        linewidth=GUIDE_LW,
        linestyle=(0, (1.1, 2.4)),
        zorder=zorder,
    )


def draw_support_bracket(
    ax,
    start,
    end,
    y=-0.38,
    *,
    label=None,
    color=ANNOTATION_COLOR,
    label_offset=-0.12,
):
    """Draw a bracket marking a support or duration interval."""

    ax.plot([start, end], [y, y], color=color, linewidth=1.3, zorder=5)
    ax.plot([start, start], [y - 0.06, y + 0.06], color=color, linewidth=1.3, zorder=5)
    ax.plot([end, end], [y - 0.06, y + 0.06], color=color, linewidth=1.3, zorder=5)
    if label is not None:
        ax.text(
            (start + end) / 2,
            y + label_offset,
            label,
            fontsize=ANNOTATION_SIZE,
            ha="center",
            va="top",
            color=color,
        )


def draw_duration_bracket(ax, start, end, y=-0.38, *, label=None):
    """Convenience wrapper for a support-duration bracket."""

    draw_support_bracket(ax, start, end, y=y, label=label)


def draw_vertical_marker_line(
    ax,
    x,
    y0,
    y1,
    *,
    color=GUIDE_COLOR,
    linestyle=(0, (1.1, 2.4)),
    lw=GUIDE_LW,
    zorder=3,
):
    """Draw a vertical helper line."""

    ax.plot([x, x], [y0, y1], color=color, linewidth=lw, linestyle=linestyle, zorder=zorder)


def draw_horizontal_marker_line(
    ax,
    y,
    x0,
    x1,
    *,
    color=GUIDE_COLOR,
    linestyle=(0, (1.1, 2.4)),
    lw=GUIDE_LW,
    zorder=3,
):
    """Draw a horizontal helper line."""

    ax.plot([x0, x1], [y, y], color=color, linewidth=lw, linestyle=linestyle, zorder=zorder)


def draw_amplitude_bracket(ax, x_bracket, offset, max_value):
    """Draw a vertical amplitude bracket."""

    ax.plot([x_bracket, x_bracket], [offset, max_value], color=ANNOTATION_COLOR, linewidth=1.3, zorder=5)
    ax.plot([x_bracket - 0.07, x_bracket + 0.07], [offset, offset], color=ANNOTATION_COLOR, linewidth=1.3, zorder=5)
    ax.plot([x_bracket - 0.07, x_bracket + 0.07], [max_value, max_value], color=ANNOTATION_COLOR, linewidth=1.3, zorder=5)


def shade_region(ax, x_left, x_right, *, alpha=0.08, color=SIGNAL_COLOR, zorder=0):
    """Shade a vertical support region."""

    ax.axvspan(x_left, x_right, color=color, alpha=alpha, zorder=zorder)


def shade_overlap(ax, x_left, x_right, *, alpha=0.12, color=SIGNAL_COLOR, zorder=1):
    """Shade the overlap between two support intervals."""

    if x_right > x_left:
        ax.axvspan(x_left, x_right, color=color, alpha=alpha, zorder=zorder)


def piecewise_linear(xs, ys):
    """Return NumPy arrays for a piecewise linear trace."""

    return np.asarray(xs, dtype=float), np.asarray(ys, dtype=float)


def linear_segment(t, t0, t1, y0, y1):
    """Return a line segment sampled from (t0, y0) to (t1, y1)."""

    t = np.asarray(t, dtype=float)
    if t1 == t0:
        return np.full_like(t, y0, dtype=float)
    m = (y1 - y0) / (t1 - t0)
    return y0 + m * (t - t0)


def unit_step(t):
    """Return the unit step u(t)."""

    return np.where(np.asarray(t) >= 0, 1.0, 0.0)


def rect_pulse(t, width=1.0, amplitude=1.0, center=0.0):
    """Return a centered rectangular pulse."""

    t = np.asarray(t, dtype=float)
    half_width = width / 2.0
    return amplitude * np.where(np.abs(t - center) <= half_width, 1.0, 0.0)


def triangular_pulse(t, width=1.0, amplitude=1.0, center=0.0):
    """Return a centered triangular pulse."""

    t = np.asarray(t, dtype=float)
    half_width = width / 2.0
    slope = np.maximum(1.0 - np.abs(t - center) / half_width, 0.0)
    return amplitude * slope


def ramp_segment(t, start=0.0, end=1.0, slope=1.0, intercept=0.0):
    """Return a finite ramp segment on [start, end] and zero elsewhere."""

    t = np.asarray(t, dtype=float)
    y = slope * t + intercept
    return np.where((t >= start) & (t <= end), y, 0.0)


def causal_exponential(t, alpha=1.0, amplitude=1.0, t0=0.0):
    """Return a causal exponential amplitude * exp(-alpha * (t - t0)) * u(t - t0)."""

    tau = np.asarray(t) - t0
    return amplitude * np.exp(-alpha * tau) * unit_step(tau)


def shifted_causal_exponential(t, alpha=1.0, amplitude=1.0, shift=0.0):
    """Alias for a delayed causal exponential."""

    return causal_exponential(t, alpha=alpha, amplitude=amplitude, t0=shift)


def time_shift(t, shift):
    """Shift a time vector by a constant amount."""

    return np.asarray(t, dtype=float) + shift


def time_reverse(t):
    """Reverse a time vector about the origin."""

    return -np.asarray(t, dtype=float)


def make_output_path(filename):
    """Return a path beside this boilerplate file for rendered assets."""

    return Path(__file__).resolve().parent / filename


configure_matplotlib()

fig, ax = plt.subplots(figsize=(9.12, 7.68), dpi=160)
setup_ct_signal_axes(
    ax,
    xlim=(-0.4, 3.25),
    ylim=(-0.6, 4.85),
    xticks=[0, 1, 2, 3],
    yticks=[0, 1, 2, 3, 4],
    x_axis_label=r"$\tau$",
    y_axis_label=r"$x(\tau)$",
    show_grid=True,
)

ax.axvspan(0.0, 0.8, color=SIGNAL_COLOR, alpha=0.12, zorder=1)

plot_signal(ax, [-0.30, 0.0, 2.0, 2.0, 2.0], [0.0, 0.0, 2.0, 0.0, 0.0])
plot_signal(ax, [-0.30, -0.2, -0.2, 0.8, 0.8, 2.0], [0.0, 0.0, 4.0, 4.0, 0.0, 0.0])

draw_closed_endpoint(ax, 2.0, 2.0)
draw_closed_endpoint(ax, -0.2, 4.0)
draw_closed_endpoint(ax, 0.8, 4.0)

ax.text(0.75, 2.0 * 0.52 + 0.18, '$x(\\tau)=\\tau$', fontsize=16, ha="center", va="bottom", color=LABEL_COLOR)
ax.text((-0.2 + 0.8) / 2.0, 4.0 + 0.18, '$h(t-\\tau)=4$', fontsize=16, ha="center", va="bottom", color=LABEL_COLOR)
ax.text(2.0, 2.0 + 0.28, '$(2,2)$', fontsize=15, ha="center", va="bottom", color=LABEL_COLOR)
ax.text(-0.2, 4.0 + 0.22, '$(t-1,4)$', fontsize=14, ha="center", va="bottom", color=ANNOTATION_COLOR)
ax.text(0.8, 4.0 + 0.22, '$(t,4)$', fontsize=14, ha="center", va="bottom", color=ANNOTATION_COLOR)

ax.text((0.0 + 0.8) / 2.0, 0.28, 'overlap $[0,t]$', fontsize=15, ha="center", va="bottom", color=LABEL_COLOR)
ax.text(0.0, 0.05, '$0\\leqq \\tau\\leqq t$', fontsize=14, ha="center", va="bottom", color=ANNOTATION_COLOR)
ax.text(0.8, 0.05, '$0\\leqq t\\leqq 1$', fontsize=14, ha="center", va="bottom", color=ANNOTATION_COLOR)
ax.text(2.55, 4.85 - 0.4, '$\\tau\\cdot 4$', fontsize=15, ha="center", va="top", color=LABEL_COLOR)

Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/7.4--direct-convolution-for-lti-systems-Images/images/l004-s004-qg-q001-q001.png').parent.mkdir(parents=True, exist_ok=True)
plt.tight_layout()
fig.savefig('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/7.4--direct-convolution-for-lti-systems-Images/images/l004-s004-qg-q001-q001.png', bbox_inches="tight", facecolor="white")
plt.close(fig)
