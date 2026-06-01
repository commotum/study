"""Shared matplotlib boilerplate for CTS module EE01-M01-02.

This reference file centralizes the white-background serif style, canonical
sizing, axis helpers, periodic-signal utilities, and phasor helpers for the
Periodic Signals and Sinusoids module. Later topic workers can copy or adapt
these helpers without re-reading the full style guide. The module does not
render any image on import.

Only matplotlib, NumPy, and pathlib are used here.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from matplotlib.ticker import MultipleLocator
import numpy as np


# ---------------------------------------------------------------------------
# Module identity
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

COURSE_NAME = "Continuous Time Signal Processing"
COURSE_CODE = "CTS"
COURSE_ID = "EE01"
UNIT_NUMBER = 1
UNIT_NAME = "Unit 1"
MODULE_ID = "EE01-M01-02"
MODULE_NUMBER = "1.2"
MODULE_NAME = "Periodic Signals and Sinusoids"

BACKGROUND_COLOR = "white"


# ---------------------------------------------------------------------------
# Canonical geometry and typography
# ---------------------------------------------------------------------------

CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150
INCHES_PER_DATA_UNIT = PX_PER_DATA_UNIT / CANONICAL_DPI

MARGIN_LEFT_PX = 115
MARGIN_RIGHT_PX = 120
MARGIN_BOTTOM_PX = 95
MARGIN_TOP_PX = 110


def configure_matplotlib():
    """Apply the shared serif and white-background defaults."""

    mpl.rcParams.update(
        {
            "mathtext.fontset": "cm",
            "font.family": "serif",
            "figure.facecolor": BACKGROUND_COLOR,
            "axes.facecolor": BACKGROUND_COLOR,
            "savefig.facecolor": BACKGROUND_COLOR,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.spines.left": False,
            "axes.spines.bottom": False,
            "axes.grid": False,
        }
    )


configure_matplotlib()


def px_to_pt(px):
    """Convert pixels to points at the canonical render scale."""

    return px * 72 / CANONICAL_DPI


def px_to_data(px):
    """Convert pixels to data units at the canonical render scale."""

    return px / PX_PER_DATA_UNIT


# ---------------------------------------------------------------------------
# Palette
# ---------------------------------------------------------------------------

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"


# ---------------------------------------------------------------------------
# Stroke widths and sizes
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
OPEN_MARKER_SIZE = px_to_pt(20.0)
CLOSED_MARKER_SIZE = px_to_pt(17.8)
ENDPOINT_EDGEWIDTH = px_to_pt(5.1)

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

AXIS_ARROW_SHAFT_WIDTH_DATA = px_to_data(4.3)
VECTOR_ARROW_SHAFT_WIDTH_DATA = px_to_data(4.3)

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

VECTOR_ARROW_KW = dict(
    angles="xy",
    scale_units="xy",
    scale=1,
    units="xy",
    width=VECTOR_ARROW_SHAFT_WIDTH_DATA,
    headwidth=4.2,
    headlength=5.5,
    headaxislength=4.3,
    pivot="tail",
    clip_on=False,
)

GRID_ALPHA = 0.18
GRID_LINESTYLE = (0, (1.1, 2.4))


# ---------------------------------------------------------------------------
# Figure helpers
# ---------------------------------------------------------------------------

def make_ct_signal_figure(xlim, ylim, *, dpi=CANONICAL_DPI, constrained_layout=True):
    """Create a CTS-style figure sized from explicit data limits."""

    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]

    axes_w_px = x_range * PX_PER_DATA_UNIT
    axes_h_px = y_range * PX_PER_DATA_UNIT
    fig_w_px = MARGIN_LEFT_PX + axes_w_px + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_BOTTOM_PX + axes_h_px + MARGIN_TOP_PX

    fig, ax = plt.subplots(
        figsize=(fig_w_px / dpi, fig_h_px / dpi),
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=constrained_layout,
    )
    return fig, ax


def make_periodic_signal_figure(xlim, ylim, *, dpi=CANONICAL_DPI, constrained_layout=True):
    """Alias for the standard CTS figure used by periodic signal plots."""

    return make_ct_signal_figure(xlim, ylim, dpi=dpi, constrained_layout=constrained_layout)


def make_sinusoid_figure(xlim, ylim, *, dpi=CANONICAL_DPI, constrained_layout=True):
    """Alias for the standard CTS figure used by sinusoid plots."""

    return make_ct_signal_figure(xlim, ylim, dpi=dpi, constrained_layout=constrained_layout)


def make_complex_plane_figure(xlim, ylim, *, dpi=CANONICAL_DPI, constrained_layout=True):
    """Alias for the standard equal-scale figure used by phasor plots."""

    return make_ct_signal_figure(xlim, ylim, dpi=dpi, constrained_layout=constrained_layout)


def new_ct_figure(*, figsize=None, dpi=CANONICAL_DPI, constrained_layout=True):
    """Create a generic white-background figure with constrained layout."""

    return plt.subplots(
        figsize=figsize,
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=constrained_layout,
    )


def save_figure(fig, output_path, *, dpi=CANONICAL_DPI):
    """Save a figure with the shared export settings."""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        output_path,
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        bbox_inches="tight",
    )


def make_output_path(filename, *, image_dir="images"):
    """Return a path in the lesson image folder for a rendered asset."""

    return BASE_DIR / image_dir / filename


# ---------------------------------------------------------------------------
# Label helpers
# ---------------------------------------------------------------------------

def math_label(value):
    """Return a mathtext label for a numeric tick or pass through a string."""

    if isinstance(value, str):
        return value

    numeric = float(value)
    rounded = round(numeric)
    if np.isclose(numeric, rounded):
        return rf"${int(rounded)}$"
    return rf"${numeric:g}$"


def pi_label(numerator, denominator=1):
    """Format a multiple of pi for tick labels and angle annotations."""

    numerator = int(numerator)
    denominator = int(denominator)

    if denominator <= 0:
        raise ValueError("denominator must be positive")

    if numerator == 0:
        return r"$0$"

    sign = "-" if numerator < 0 else ""
    numerator = abs(numerator)

    if denominator == 1:
        if numerator == 1:
            return rf"${sign}\pi$"
        return rf"${sign}{numerator}\pi$"

    if numerator == 1:
        return rf"${sign}\dfrac{{\pi}}{{{denominator}}}$"

    return rf"${sign}\dfrac{{{numerator}\pi}}{{{denominator}}}$"


# ---------------------------------------------------------------------------
# Axis helpers
# ---------------------------------------------------------------------------

def _normalized_step(value):
    """Return a float step after guarding against a zero grid spacing."""

    numeric = float(value)
    if numeric <= 0:
        raise ValueError("grid step must be positive")
    return numeric


def _draw_x_ticks(ax, ticks, *, show_labels=True, tick_labels=None):
    """Draw centered x-axis ticks and optional labels."""

    for index, tick in enumerate(ticks):
        tick_value = float(tick)
        if np.isclose(tick_value, 0.0):
            continue

        ax.plot(
            [tick_value, tick_value],
            [-TICK_HALF_LEN, TICK_HALF_LEN],
            color=AXIS_COLOR,
            lw=TICK_LW,
            zorder=5,
        )

        if show_labels:
            label = math_label(tick_value) if tick_labels is None else tick_labels[index]
            ax.text(
                tick_value,
                X_TICK_LABEL_Y,
                label,
                fontsize=TICK_LABEL_SIZE,
                ha="center",
                va="top",
                color=TICK_LABEL_COLOR,
                zorder=6,
            )


def _draw_y_ticks(ax, ticks, *, show_labels=True, label_side="left", tick_labels=None):
    """Draw centered y-axis ticks and optional labels."""

    for index, tick in enumerate(ticks):
        tick_value = float(tick)
        if np.isclose(tick_value, 0.0):
            continue

        ax.plot(
            [-TICK_HALF_LEN, TICK_HALF_LEN],
            [tick_value, tick_value],
            color=AXIS_COLOR,
            lw=TICK_LW,
            zorder=5,
        )

        if show_labels:
            label = math_label(tick_value) if tick_labels is None else tick_labels[index]
            if label_side == "right":
                x_pos = Y_TICK_LABEL_X
                ha = "left"
            else:
                x_pos = -Y_TICK_LABEL_X
                ha = "right"

            ax.text(
                x_pos,
                tick_value,
                label,
                fontsize=TICK_LABEL_SIZE,
                ha=ha,
                va="center",
                color=TICK_LABEL_COLOR,
                zorder=6,
            )


def setup_ct_signal_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_tick_labels=None,
    y_tick_labels=None,
    x_axis_label=r"$t$",
    y_axis_label=r"$x(t)$",
    show_grid=True,
    show_origin=True,
    y_tick_label_side="left",
    show_x_tick_labels=True,
    show_y_tick_labels=True,
    x_minor_grid_step=1,
    y_minor_grid_step=1,
    equal_aspect=True,
    grid_alpha=GRID_ALPHA,
):
    """Configure a clean continuous-time signal axis layout."""

    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)

    if equal_aspect:
        ax.set_aspect("equal", adjustable="box")

    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.xaxis.set_minor_locator(MultipleLocator(_normalized_step(x_minor_grid_step)))
    ax.yaxis.set_minor_locator(MultipleLocator(_normalized_step(y_minor_grid_step)))

    if show_grid:
        ax.grid(True, which="both", linewidth=GRID_LW, alpha=grid_alpha, color=GRID_COLOR)
        ax.set_axisbelow(True)

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    x_axis_start, x_axis_end = xlim
    y_axis_start, y_axis_end = ylim

    ax.quiver(x_axis_start, 0, x_axis_end - x_axis_start, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y_axis_start, 0, y_axis_end - y_axis_start, **AXIS_ARROW_KW)

    _draw_x_ticks(ax, xticks, show_labels=show_x_tick_labels, tick_labels=x_tick_labels)
    _draw_y_ticks(
        ax,
        yticks,
        show_labels=show_y_tick_labels,
        label_side=y_tick_label_side,
        tick_labels=y_tick_labels,
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
        )


def setup_periodic_signal_axes(ax, **kwargs):
    """Alias for the shared continuous-time axis layout."""

    return setup_ct_signal_axes(ax, **kwargs)


def setup_sinusoid_axes(ax, **kwargs):
    """Alias for the shared continuous-time axis layout."""

    return setup_ct_signal_axes(ax, **kwargs)


def setup_complex_plane_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_tick_labels=None,
    y_tick_labels=None,
    x_axis_label=r"$\Re\{z\}$",
    y_axis_label=r"$\Im\{z\}$",
    show_grid=True,
    show_origin=True,
    y_tick_label_side="left",
    show_x_tick_labels=True,
    show_y_tick_labels=True,
    x_minor_grid_step=1,
    y_minor_grid_step=1,
    equal_aspect=True,
    grid_alpha=GRID_ALPHA,
):
    """Configure a complex-plane diagram with the shared CTS styling."""

    setup_ct_signal_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=xticks,
        yticks=yticks,
        x_tick_labels=x_tick_labels,
        y_tick_labels=y_tick_labels,
        x_axis_label=x_axis_label,
        y_axis_label=y_axis_label,
        show_grid=show_grid,
        show_origin=show_origin,
        y_tick_label_side=y_tick_label_side,
        show_x_tick_labels=show_x_tick_labels,
        show_y_tick_labels=show_y_tick_labels,
        x_minor_grid_step=x_minor_grid_step,
        y_minor_grid_step=y_minor_grid_step,
        equal_aspect=equal_aspect,
        grid_alpha=grid_alpha,
    )


# ---------------------------------------------------------------------------
# Plotting helpers
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
    """Plot a smooth continuous-time signal trace."""

    ax.plot(
        t,
        x,
        color=color,
        linewidth=lw,
        solid_capstyle="round",
        zorder=zorder,
    )


def draw_vertical_jump(ax, t0, y0, y1, *, color=SIGNAL_COLOR, lw=SIGNAL_LW, zorder=4):
    """Draw an idealized vertical transition at a jump discontinuity."""

    ax.plot(
        [t0, t0],
        [y0, y1],
        color=color,
        linewidth=lw,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=zorder,
    )


def draw_open_endpoint(ax, t0, x0, *, color=SIGNAL_COLOR):
    """Draw an open-circle endpoint marker."""

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


def draw_closed_endpoint(ax, t0, x0, *, color=SIGNAL_COLOR):
    """Draw a closed-circle endpoint marker."""

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


def draw_point(
    ax,
    x,
    y,
    *,
    label=None,
    label_offset=(px_to_data(8), px_to_data(8)),
    color=SIGNAL_COLOR,
    marker_size=CLOSED_MARKER_SIZE,
    edgewidth=ENDPOINT_EDGEWIDTH,
    zorder=6,
):
    """Draw a point marker with an optional text label."""

    ax.plot(
        x,
        y,
        marker="o",
        markersize=marker_size,
        markerfacecolor=color,
        markeredgecolor=color,
        markeredgewidth=edgewidth,
        linestyle="None",
        zorder=zorder,
    )

    if label is not None:
        ax.text(
            x + label_offset[0],
            y + label_offset[1],
            label,
            fontsize=ANNOTATION_SIZE,
            ha="left",
            va="bottom",
            color=LABEL_COLOR,
            zorder=zorder + 1,
        )


def draw_complex_point(ax, value, **kwargs):
    """Draw a point given as a complex number."""

    x, y = complex_xy(value)
    draw_point(ax, x, y, **kwargs)


def draw_dotted_guide(ax, x_values, y_values, *, color=GUIDE_COLOR, zorder=3):
    """Draw a subtle dotted guide line."""

    ax.plot(
        x_values,
        y_values,
        color=color,
        linewidth=GUIDE_LW,
        linestyle=GRID_LINESTYLE,
        zorder=zorder,
    )


def draw_vertical_marker_line(
    ax,
    x,
    y0,
    y1,
    *,
    color=GUIDE_COLOR,
    linestyle=GRID_LINESTYLE,
    lw=GUIDE_LW,
    zorder=3,
):
    """Draw a vertical guide or marker line."""

    ax.plot([x, x], [y0, y1], color=color, linewidth=lw, linestyle=linestyle, zorder=zorder)


def draw_horizontal_marker_line(
    ax,
    y,
    x0,
    x1,
    *,
    color=GUIDE_COLOR,
    linestyle=GRID_LINESTYLE,
    lw=GUIDE_LW,
    zorder=3,
):
    """Draw a horizontal guide or marker line."""

    ax.plot([x0, x1], [y, y], color=color, linewidth=lw, linestyle=linestyle, zorder=zorder)


def draw_offset_line(ax, x_start, x_end, offset, *, color=GUIDE_COLOR):
    """Draw a baseline or offset reference line."""

    draw_horizontal_marker_line(ax, offset, x_start, x_end, color=color)


def draw_span_bracket(ax, x_start, x_end, y, *, label=None, color=ANNOTATION_COLOR):
    """Draw a horizontal span bracket for duration or support annotations."""

    ax.plot([x_start, x_end], [y, y], color=color, linewidth=ANNOTATION_LW, zorder=5)
    ax.plot(
        [x_start, x_start],
        [y - BRACKET_CAP_HALF_LEN, y + BRACKET_CAP_HALF_LEN],
        color=color,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )
    ax.plot(
        [x_end, x_end],
        [y - BRACKET_CAP_HALF_LEN, y + BRACKET_CAP_HALF_LEN],
        color=color,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )

    if label is not None:
        ax.text(
            (x_start + x_end) / 2,
            y - BRACKET_LABEL_GAP,
            label,
            fontsize=ANNOTATION_SIZE,
            ha="center",
            va="top",
            color=color,
        )


def draw_support_bracket(ax, x_start, x_end, y=-0.38, *, label=None, color=ANNOTATION_COLOR):
    """Draw a bracket that marks a support or interval of interest."""

    draw_span_bracket(ax, x_start, x_end, y, label=label, color=color)


def draw_duration_bracket(ax, x_start, x_end, y=-0.38, *, label=r"$\Delta t$", color=ANNOTATION_COLOR):
    """Draw a time-duration bracket."""

    draw_span_bracket(ax, x_start, x_end, y, label=label, color=color)


def draw_period_bracket(ax, x_start, x_end, y=-0.38, *, label=r"$T$", color=ANNOTATION_COLOR):
    """Draw a period bracket."""

    draw_span_bracket(ax, x_start, x_end, y, label=label, color=color)


def draw_vertical_bracket(ax, x, y_start, y_end, *, label=None, color=ANNOTATION_COLOR):
    """Draw a vertical bracket for amplitude or excursion annotations."""

    ax.plot([x, x], [y_start, y_end], color=color, linewidth=ANNOTATION_LW, zorder=5)
    ax.plot(
        [x - AMPLITUDE_CAP_HALF_LEN, x + AMPLITUDE_CAP_HALF_LEN],
        [y_start, y_start],
        color=color,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )
    ax.plot(
        [x - AMPLITUDE_CAP_HALF_LEN, x + AMPLITUDE_CAP_HALF_LEN],
        [y_end, y_end],
        color=color,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )

    if label is not None:
        ax.text(
            x + BRACKET_LABEL_GAP,
            (y_start + y_end) / 2,
            label,
            fontsize=ANNOTATION_SIZE,
            ha="left",
            va="center",
            color=color,
        )


def draw_amplitude_bracket(ax, x, y_start, y_end, *, label=None, color=ANNOTATION_COLOR):
    """Draw a vertical amplitude bracket."""

    draw_vertical_bracket(ax, x, y_start, y_end, label=label, color=color)


def shade_region(ax, x_left, x_right, *, alpha=0.08, color=SIGNAL_COLOR, zorder=0):
    """Shade a vertical support or zero-region interval."""

    ax.axvspan(x_left, x_right, color=color, alpha=alpha, zorder=zorder)


# ---------------------------------------------------------------------------
# Signal-building helpers
# ---------------------------------------------------------------------------

def unit_step(t):
    """Return the unit step u(t)."""

    return np.where(np.asarray(t, dtype=float) >= 0, 1.0, 0.0)


def shifted_unit_step(t, shift=0.0):
    """Return the shifted unit step u(t - shift)."""

    return unit_step(np.asarray(t, dtype=float) - shift)


def rectangular_window(t, start=0.0, end=1.0, amplitude=1.0):
    """Return a rectangular window on [start, end]."""

    t = np.asarray(t, dtype=float)
    return amplitude * np.where((t >= start) & (t <= end), 1.0, 0.0)


def wrap_to_period(t, period, *, origin=0.0):
    """Wrap time samples into one period starting at origin."""

    period = float(period)
    if period <= 0:
        raise ValueError("period must be positive")

    t = np.asarray(t, dtype=float)
    return np.mod(t - origin, period) + origin


def periodic_extension(t, period, waveform, *, origin=0.0):
    """Extend a base waveform periodically."""

    return waveform(wrap_to_period(t, period, origin=origin))


def frequency_from_period(period):
    """Return the fundamental frequency for a given period."""

    period = float(period)
    if period <= 0:
        raise ValueError("period must be positive")
    return 1.0 / period


def angular_frequency_from_period(period):
    """Return omega_0 for a given period."""

    return 2 * np.pi * frequency_from_period(period)


def period_from_frequency(frequency):
    """Return the period for a given frequency."""

    frequency = float(frequency)
    if frequency <= 0:
        raise ValueError("frequency must be positive")
    return 1.0 / frequency


def period_from_angular_frequency(omega):
    """Return the period for a given angular frequency."""

    omega = float(omega)
    if omega <= 0:
        raise ValueError("angular frequency must be positive")
    return 2 * np.pi / omega


def harmonic_frequency(period, harmonic=1):
    """Return the harmonic frequency for a given fundamental period."""

    harmonic = float(harmonic)
    if harmonic <= 0:
        raise ValueError("harmonic must be positive")
    return harmonic * frequency_from_period(period)


def harmonic_angular_frequency(period, harmonic=1):
    """Return the harmonic angular frequency for a given fundamental period."""

    return 2 * np.pi * harmonic_frequency(period, harmonic=harmonic)


def _resolve_angular_frequency(omega=None, *, frequency=None, period=None):
    """Resolve one angular frequency from omega, frequency, or period."""

    provided = [omega is not None, frequency is not None, period is not None]
    if sum(provided) == 0:
        return 1.0

    if omega is not None:
        return float(omega)

    if frequency is not None:
        return 2 * np.pi * float(frequency)

    return angular_frequency_from_period(period)


def sinusoid(
    t,
    *,
    amplitude=1.0,
    omega=None,
    frequency=None,
    period=None,
    phase=0.0,
    offset=0.0,
    kind="cos",
):
    """Return a cosine or sine waveform with the shared periodic notation."""

    omega = _resolve_angular_frequency(omega, frequency=frequency, period=period)
    t = np.asarray(t, dtype=float)
    argument = omega * t + phase

    if kind == "sin":
        carrier = np.sin(argument)
    elif kind == "cos":
        carrier = np.cos(argument)
    else:
        raise ValueError("kind must be 'sin' or 'cos'")

    return offset + amplitude * carrier


def cosine_wave(
    t,
    *,
    amplitude=1.0,
    omega=None,
    frequency=None,
    period=None,
    phase=0.0,
    offset=0.0,
):
    """Return a cosine waveform."""

    return sinusoid(
        t,
        amplitude=amplitude,
        omega=omega,
        frequency=frequency,
        period=period,
        phase=phase,
        offset=offset,
        kind="cos",
    )


def sine_wave(
    t,
    *,
    amplitude=1.0,
    omega=None,
    frequency=None,
    period=None,
    phase=0.0,
    offset=0.0,
):
    """Return a sine waveform."""

    return sinusoid(
        t,
        amplitude=amplitude,
        omega=omega,
        frequency=frequency,
        period=period,
        phase=phase,
        offset=offset,
        kind="sin",
    )


def complex_exponential(
    t,
    *,
    amplitude=1.0,
    omega=None,
    frequency=None,
    period=None,
    phase=0.0,
    offset=0.0,
):
    """Return a complex exponential waveform."""

    omega = _resolve_angular_frequency(omega, frequency=frequency, period=period)
    t = np.asarray(t, dtype=float)
    return offset + amplitude * np.exp(1j * (omega * t + phase))


def harmonic_sinusoid(
    t,
    *,
    amplitude=1.0,
    fundamental_period=1.0,
    harmonic=1,
    phase=0.0,
    offset=0.0,
    kind="cos",
):
    """Return the harmonic sinusoid for a given fundamental period."""

    omega = harmonic_angular_frequency(fundamental_period, harmonic=harmonic)
    return sinusoid(
        t,
        amplitude=amplitude,
        omega=omega,
        phase=phase,
        offset=offset,
        kind=kind,
    )


# ---------------------------------------------------------------------------
# Complex-plane and phasor helpers
# ---------------------------------------------------------------------------

def complex_xy(value):
    """Return the real and imaginary coordinates for a complex value."""

    value = complex(value)
    return value.real, value.imag


def polar_to_cartesian(radius, angle):
    """Convert polar coordinates to a Cartesian point."""

    return radius * np.cos(angle), radius * np.sin(angle)


def draw_vector(
    ax,
    x_end,
    y_end,
    *,
    x_start=0.0,
    y_start=0.0,
    color=SIGNAL_COLOR,
    zorder=4,
):
    """Draw a vector arrow in the complex plane or on a signal diagram."""

    vector_kw = dict(VECTOR_ARROW_KW)
    vector_kw["color"] = color
    vector_kw["zorder"] = zorder
    return ax.quiver(
        x_start,
        y_start,
        x_end - x_start,
        y_end - y_start,
        **vector_kw,
    )


def draw_phasor(ax, magnitude, angle, *, x_start=0.0, y_start=0.0, color=SIGNAL_COLOR, zorder=4):
    """Draw a phasor from a magnitude-angle pair."""

    x_end, y_end = polar_to_cartesian(magnitude, angle)
    return draw_vector(
        ax,
        x_end,
        y_end,
        x_start=x_start,
        y_start=y_start,
        color=color,
        zorder=zorder,
    )


def draw_unit_circle(
    ax,
    *,
    radius=1.0,
    center=(0.0, 0.0),
    color=GUIDE_COLOR,
    lw=GUIDE_LW,
    linestyle=GRID_LINESTYLE,
    zorder=3,
):
    """Draw a unit circle or other circular guide."""

    theta = np.linspace(0.0, 2.0 * np.pi, 361)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    ax.plot(x, y, color=color, linewidth=lw, linestyle=linestyle, zorder=zorder)


def draw_angle_arc(
    ax,
    theta_start,
    theta_end,
    *,
    radius=0.55,
    center=(0.0, 0.0),
    color=ANNOTATION_COLOR,
    lw=ANNOTATION_LW,
    zorder=5,
):
    """Draw a circular angle arc between two angles in radians."""

    theta1 = np.degrees(theta_start)
    theta2 = np.degrees(theta_end)
    arc = Arc(
        center,
        2 * radius,
        2 * radius,
        angle=0.0,
        theta1=theta1,
        theta2=theta2,
        linewidth=lw,
        color=color,
        zorder=zorder,
    )
    ax.add_patch(arc)
    return arc


def draw_angle_label(
    ax,
    theta,
    *,
    radius=0.68,
    center=(0.0, 0.0),
    label=None,
    color=ANNOTATION_COLOR,
):
    """Place an angle label near a circular arc."""

    if label is None:
        label = math_label(theta)

    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    ax.text(
        x,
        y,
        label,
        fontsize=ANNOTATION_SIZE,
        ha="center",
        va="center",
        color=color,
    )


# ---------------------------------------------------------------------------
# Convenience aliases
# ---------------------------------------------------------------------------

make_periodic_signal_figure = make_ct_signal_figure
make_sinusoid_figure = make_ct_signal_figure
setup_periodic_signal_axes = setup_ct_signal_axes
setup_sinusoid_axes = setup_ct_signal_axes
