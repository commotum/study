"""Shared matplotlib boilerplate for CTS lesson EE01-M09-02 / 9.2.

This module centralizes the textbook signal-plot styling used for the
"Basic Fourier Transform Pairs" lesson, especially the rectangular-pulse and
sinc-spectrum figures in the Sinc-Shaped Spectra topic. Later topic workers
can copy or adapt these helpers without re-reading the full style guide.

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
UNIT_NUMBER = 9
UNIT_NAME = "Unit 9"
MODULE_ID = "EE01-M09-02"
MODULE_NUMBER = "9.2"
MODULE_NAME = "Basic Fourier Transform Pairs"
LESSON_INDEX = 4
LESSON_TITLE = "Sinc-Shaped Spectra"


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

DEFAULT_TIME_AXIS_LABEL = r"$t$"
DEFAULT_FREQUENCY_AXIS_LABEL = r"$\omega$"
DEFAULT_TIME_SIGNAL_LABEL = r"$x(t)$"
DEFAULT_FREQUENCY_SIGNAL_LABEL = r"$X(\omega)$"
DEFAULT_MAGNITUDE_SPECTRUM_LABEL = r"$|X(\omega)|$"

DEFAULT_PULSE_DURATION = 2.0
DEFAULT_PULSE_AMPLITUDE = 1.0
DEFAULT_PULSE_CENTER = 0.0
DEFAULT_FREQUENCY_CENTER = 0.0


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


def save_figure(fig, output_path, *, dpi=CANONICAL_DPI):
    """Save a figure with the shared export settings."""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        output_path,
        dpi=dpi,
        bbox_inches="tight",
        facecolor=BACKGROUND_COLOR,
    )
    return output_path


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
    ax.set_facecolor(BACKGROUND_COLOR)
    return fig, ax


def new_ct_figure(*, figsize=None, dpi=CANONICAL_DPI):
    """Create a generic CTS figure with the shared background and layout."""

    fig, ax = plt.subplots(
        figsize=figsize,
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=True,
    )
    if hasattr(ax, "set_facecolor"):
        ax.set_facecolor(BACKGROUND_COLOR)
    return fig, ax


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
    x_axis_label=DEFAULT_TIME_AXIS_LABEL,
    y_axis_label=DEFAULT_TIME_SIGNAL_LABEL,
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

    # Draw axes through the origin with arrowheads only on the positive ends.
    ax.quiver(x_axis_start, 0, x_axis_end - x_axis_start, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y_axis_start, 0, y_axis_end - y_axis_start, **AXIS_ARROW_KW)

    for t in xticks:
        if abs(t) < 1e-12:
            continue

        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN],
                color=AXIS_COLOR, lw=TICK_LW, zorder=5)

        if show_x_tick_labels:
            ax.text(t, X_TICK_LABEL_Y, math_label(t),
                    fontsize=TICK_LABEL_SIZE, ha="center", va="top",
                    color=TICK_LABEL_COLOR, zorder=6)

    for y in yticks:
        if abs(y) < 1e-12:
            continue

        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y],
                color=AXIS_COLOR, lw=TICK_LW, zorder=5)

        if show_y_tick_labels:
            if y_tick_label_side == "right":
                ax.text(Y_TICK_LABEL_X, y, math_label(y),
                        fontsize=TICK_LABEL_SIZE, ha="left", va="center",
                        color=TICK_LABEL_COLOR, zorder=6)
            else:
                ax.text(-Y_TICK_LABEL_X, y, math_label(y),
                        fontsize=TICK_LABEL_SIZE, ha="right", va="center",
                        color=TICK_LABEL_COLOR, zorder=6)

    if show_origin:
        ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$",
                fontsize=TICK_LABEL_SIZE, ha="left", va="top",
                color=TICK_LABEL_COLOR, zorder=6)

    if x_axis_label is not None:
        ax.text(x_axis_end + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, x_axis_label,
                fontsize=AXIS_LABEL_SIZE, ha="left", va="center",
                color=LABEL_COLOR, clip_on=False)

    if y_axis_label is not None:
        ax.text(0, y_axis_end + Y_AXIS_LABEL_Y_PAD, y_axis_label,
                fontsize=TOP_LABEL_SIZE, ha="center", va="bottom",
                color=LABEL_COLOR, clip_on=False)


def setup_time_axes(ax, *, xlim, ylim, xticks, yticks, **kwargs):
    """Convenience wrapper for a time-domain plot."""

    return setup_ct_signal_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=xticks,
        yticks=yticks,
        x_axis_label=DEFAULT_TIME_AXIS_LABEL,
        y_axis_label=DEFAULT_TIME_SIGNAL_LABEL,
        **kwargs,
    )


def setup_frequency_axes(ax, *, xlim, ylim, xticks, yticks, **kwargs):
    """Convenience wrapper for a frequency-domain plot."""

    return setup_ct_signal_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=xticks,
        yticks=yticks,
        x_axis_label=DEFAULT_FREQUENCY_AXIS_LABEL,
        y_axis_label=DEFAULT_FREQUENCY_SIGNAL_LABEL,
        **kwargs,
    )


def setup_magnitude_spectrum_axes(ax, *, xlim, ylim, xticks, yticks, **kwargs):
    """Convenience wrapper for a magnitude-spectrum plot."""

    return setup_ct_signal_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=xticks,
        yticks=yticks,
        x_axis_label=DEFAULT_FREQUENCY_AXIS_LABEL,
        y_axis_label=DEFAULT_MAGNITUDE_SPECTRUM_LABEL,
        **kwargs,
    )


def plot_signal(ax, t, x, *, lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    """Plot a connected continuous-time trace."""

    ax.plot(
        t, x,
        color=color,
        linewidth=lw,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=zorder,
    )


def plot_smooth_signal(ax, t, x, *, lw=SMOOTH_SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    """Plot a smooth continuous-time curve."""

    ax.plot(
        t, x,
        color=color,
        linewidth=lw,
        solid_capstyle="round",
        zorder=zorder,
    )


def draw_open_endpoint(ax, t0, x0):
    """Draw an open-circle endpoint marker."""

    ax.plot(
        t0, x0,
        marker="o",
        markersize=OPEN_MARKER_SIZE,
        markerfacecolor="white",
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=ENDPOINT_EDGEWIDTH,
        linestyle="None",
        zorder=6,
    )


def draw_closed_endpoint(ax, t0, x0):
    """Draw a closed-circle endpoint marker."""

    ax.plot(
        t0, x0,
        marker="o",
        markersize=CLOSED_MARKER_SIZE,
        markerfacecolor=SIGNAL_COLOR,
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=ENDPOINT_EDGEWIDTH,
        linestyle="None",
        zorder=6,
    )


def draw_dotted_guide(
    ax,
    x_values,
    y_values,
    *,
    color=GUIDE_COLOR,
    lw=GUIDE_LW,
    linestyle=GUIDE_DASH_STYLE,
    zorder=3,
):
    """Draw a light dotted guide line."""

    ax.plot(
        x_values, y_values,
        color=color,
        linewidth=lw,
        linestyle=linestyle,
        zorder=zorder,
    )


def draw_vertical_guide(ax, x, y0, y1, *, color=GUIDE_COLOR, lw=GUIDE_LW):
    """Draw a vertical dotted guide line."""

    draw_dotted_guide(ax, [x, x], [y0, y1], color=color, lw=lw)


def draw_horizontal_guide(ax, x0, x1, y, *, color=GUIDE_COLOR, lw=GUIDE_LW):
    """Draw a horizontal dotted guide line."""

    draw_dotted_guide(ax, [x0, x1], [y, y], color=color, lw=lw)


def draw_duration_bracket(
    ax,
    t_start,
    t_end,
    *,
    y=-0.38,
    label="duration",
    color=ANNOTATION_COLOR,
    lw=ANNOTATION_LW,
    label_size=ANNOTATION_SIZE,
):
    """Draw a centered duration bracket under a pulse or interval."""

    ax.plot([t_start, t_end], [y, y], color=color, linewidth=lw, zorder=5)
    ax.plot([t_start, t_start], [y - BRACKET_CAP_HALF_LEN, y + BRACKET_CAP_HALF_LEN],
            color=color, linewidth=lw, zorder=5)
    ax.plot([t_end, t_end], [y - BRACKET_CAP_HALF_LEN, y + BRACKET_CAP_HALF_LEN],
            color=color, linewidth=lw, zorder=5)

    if label is not None:
        ax.text((t_start + t_end) / 2, y - BRACKET_LABEL_GAP, label,
                fontsize=label_size, ha="center", va="top", color=color)


def draw_amplitude_bracket(
    ax,
    x,
    y0,
    y1,
    *,
    color=ANNOTATION_COLOR,
    lw=ANNOTATION_LW,
    cap_half_len=AMPLITUDE_CAP_HALF_LEN,
):
    """Draw a vertical amplitude bracket."""

    ax.plot([x, x], [y0, y1], color=color, linewidth=lw, zorder=5)
    ax.plot([x - cap_half_len, x + cap_half_len], [y0, y0],
            color=color, linewidth=lw, zorder=5)
    ax.plot([x - cap_half_len, x + cap_half_len], [y1, y1],
            color=color, linewidth=lw, zorder=5)


# ---------------------------------------------------------------------------
# Fourier-pair helpers
# ---------------------------------------------------------------------------

def rectangular_pulse(t, *, duration, amplitude=1.0, center=0.0, baseline=0.0):
    """Return a centered rectangular pulse sampled on t."""

    t = np.asarray(t, dtype=float)
    half_width = 0.5 * float(duration)
    inside = np.abs(t - float(center)) <= half_width
    return baseline + float(amplitude) * inside.astype(float)


def rectangular_pulse_trace(
    *,
    duration,
    amplitude=1.0,
    center=0.0,
    baseline=0.0,
    left_pad=None,
    right_pad=None,
):
    """Return a polyline trace for a rectangular pulse with vertical edges."""

    duration = float(duration)
    center = float(center)
    amplitude = float(amplitude)
    baseline = float(baseline)

    half_width = 0.5 * duration
    left = center - half_width
    right = center + half_width

    if left_pad is None:
        left_pad = 0.6 * duration
    if right_pad is None:
        right_pad = 0.6 * duration

    t = np.array(
        [
            left - float(left_pad),
            left,
            left,
            right,
            right,
            right + float(right_pad),
        ],
        dtype=float,
    )
    x = np.array(
        [
            baseline,
            baseline,
            amplitude,
            amplitude,
            baseline,
            baseline,
        ],
        dtype=float,
    )
    return t, x


def plot_rectangular_pulse(
    ax,
    *,
    duration,
    amplitude=1.0,
    center=0.0,
    baseline=0.0,
    left_pad=None,
    right_pad=None,
    lw=SIGNAL_LW,
    color=SIGNAL_COLOR,
    zorder=4,
):
    """Plot a rectangular pulse with connected vertical edges."""

    t, x = rectangular_pulse_trace(
        duration=duration,
        amplitude=amplitude,
        center=center,
        baseline=baseline,
        left_pad=left_pad,
        right_pad=right_pad,
    )
    plot_signal(ax, t, x, lw=lw, color=color, zorder=zorder)
    return t, x


def engineering_sinc(u):
    """Return sin(u) / u with the removable singularity filled at u = 0."""

    u = np.asarray(u, dtype=float)
    out = np.ones_like(u, dtype=float)
    mask = np.abs(u) > 1e-12
    out[mask] = np.sin(u[mask]) / u[mask]
    return out


def first_sinc_zero(duration):
    """Return the first positive zero of sinc(omega * duration / 2)."""

    duration = float(duration)
    if duration <= 0:
        raise ValueError("duration must be positive")
    return 2.0 * np.pi / duration


def central_lobe_width(duration):
    """Return the width between the first pair of zeros of the central lobe."""

    return 2.0 * first_sinc_zero(duration)


def sinc_zero_locations(duration, *, count=4, center=0.0):
    """Return symmetric zero locations for a sinc spectrum."""

    duration = float(duration)
    center = float(center)
    if count < 1:
        return np.array([center], dtype=float)

    offsets = first_sinc_zero(duration) * np.arange(1, count + 1, dtype=float)
    left = center - offsets[::-1]
    right = center + offsets
    return np.concatenate([left, np.array([center], dtype=float), right])


def rectangular_pulse_transform(
    omega,
    *,
    duration,
    amplitude=1.0,
    center_frequency=0.0,
):
    """Return AT sinc(omega T / 2) for a centered rectangular pulse."""

    omega = np.asarray(omega, dtype=float)
    duration = float(duration)
    amplitude = float(amplitude)
    center_frequency = float(center_frequency)
    u = 0.5 * duration * (omega - center_frequency)
    return amplitude * duration * engineering_sinc(u)


def rectangular_pulse_magnitude_spectrum(
    omega,
    *,
    duration,
    amplitude=1.0,
    center_frequency=0.0,
):
    """Return the magnitude of the rectangular-pulse Fourier transform."""

    return np.abs(
        rectangular_pulse_transform(
            omega,
            duration=duration,
            amplitude=amplitude,
            center_frequency=center_frequency,
        )
    )


def plot_rectangular_pulse_spectrum(
    ax,
    omega,
    *,
    duration,
    amplitude=1.0,
    center_frequency=0.0,
    magnitude=True,
    lw=SMOOTH_SIGNAL_LW,
    color=SIGNAL_COLOR,
    zorder=4,
):
    """Plot a rectangular-pulse spectrum on a frequency axis."""

    if magnitude:
        y = rectangular_pulse_magnitude_spectrum(
            omega,
            duration=duration,
            amplitude=amplitude,
            center_frequency=center_frequency,
        )
    else:
        y = rectangular_pulse_transform(
            omega,
            duration=duration,
            amplitude=amplitude,
            center_frequency=center_frequency,
        )

    plot_smooth_signal(ax, omega, y, lw=lw, color=color, zorder=zorder)
    return y


def pulse_to_spectrum_peak(amplitude, duration):
    """Return the zero-frequency peak height AT for a rectangular pulse."""

    return float(amplitude) * float(duration)


