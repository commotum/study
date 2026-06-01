"""Shared matplotlib boilerplate for CTS module EE01-M02-02.

This file collects the reusable styling defaults and helper functions used by
the Continuous Time Signal Processing phasors-and-sinusoids image session.
Later topic workers can copy or adapt these helpers without re-reading the full
style guide.

The module is reference-only: it does not render any figure on import.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np


BACKGROUND_COLOR = "white"

COURSE_NAME = "Continuous Time Signal Processing"
COURSE_CODE = "CTS"
COURSE_ID = "EE01"
UNIT_NUMBER = 2
UNIT_NAME = "Unit 2"
MODULE_ID = "EE01-M02-02"
MODULE_NUMBER = "2.2"
MODULE_NAME = "Phasors and Sinusoids"

BOILERPLATE_PATH = Path(__file__).resolve()
BOILERPLATE_DIR = BOILERPLATE_PATH.parent
SESSION_SLUG = "continuous-time-signal-processing-ee01-m02-02"

CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150
INCHES_PER_DATA_UNIT = PX_PER_DATA_UNIT / CANONICAL_DPI

def px_to_pt(px):
    """Convert pixels to points at the canonical render scale."""

    return px * 72 / CANONICAL_DPI


def px_to_data(px):
    """Convert pixels to data units at the canonical render scale."""

    return px / PX_PER_DATA_UNIT


MARGIN_LEFT_PX = 115
MARGIN_RIGHT_PX = 120
MARGIN_BOTTOM_PX = 95
MARGIN_TOP_PX = 110

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"

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
    color=SIGNAL_COLOR,
    pivot="tail",
    clip_on=False,
)

PI = np.pi
TAU = 2 * np.pi
DEG_PER_RAD = 180.0 / np.pi
RAD_PER_DEG = np.pi / 180.0


def configure_matplotlib():
    """Apply the shared serif font and white background defaults."""

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


def math_label(value):
    """Return a mathtext label for a numeric value or pass through a string."""

    if isinstance(value, str):
        return value

    numeric = float(value)
    rounded = round(numeric)
    if abs(numeric - rounded) < 1e-9:
        return rf"${int(rounded)}$"
    return rf"${numeric:g}$"


def degree_label(value):
    """Return a mathtext degree label such as $45^\circ$."""

    numeric = float(value)
    rounded = round(numeric)
    if abs(numeric - rounded) < 1e-9:
        return rf"${int(rounded)}^\circ$"
    return rf"${numeric:g}^\circ$"


def pi_fraction_label(numerator, denominator=1):
    """Return a mathtext label for a rational multiple of pi."""

    if denominator <= 0:
        raise ValueError("denominator must be positive")

    numerator = int(round(numerator))
    denominator = int(round(denominator))

    if numerator == 0:
        return r"$0$"

    sign = "-" if numerator < 0 else ""
    n = abs(numerator)

    if denominator == 1:
        if n == 1:
            return rf"${sign}\pi$"
        return rf"${sign}{n}\pi$"

    if n == 1:
        return rf"${sign}\dfrac{{\pi}}{{{denominator}}}$"
    return rf"${sign}\dfrac{{{n}\pi}}{{{denominator}}}$"


def pi_tick_positions(numerators, denominator=1):
    """Return tick positions for rational multiples of pi."""

    numerators = np.asarray(numerators, dtype=float)
    return numerators * np.pi / denominator


def deg_to_rad(degrees):
    """Convert degrees to radians."""

    return np.asarray(degrees, dtype=float) * RAD_PER_DEG


def rad_to_deg(radians):
    """Convert radians to degrees."""

    return np.asarray(radians, dtype=float) * DEG_PER_RAD


def wrap_to_pi(theta):
    """Wrap angles to the interval (-pi, pi]."""

    theta = np.asarray(theta, dtype=float)
    return (theta + np.pi) % TAU - np.pi


def wrap_to_tau(theta):
    """Wrap angles to the interval [0, 2*pi)."""

    theta = np.asarray(theta, dtype=float)
    return np.mod(theta, TAU)


def _make_data_scaled_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
    """Create a figure sized from explicit data limits."""

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
        constrained_layout=True,
    )
    return fig, ax


def make_generic_figure(*, figsize=None, dpi=CANONICAL_DPI):
    """Create a generic CTS figure with shared background and layout defaults."""

    return plt.subplots(
        figsize=figsize,
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=True,
    )


def make_ct_signal_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
    """Create a standard continuous-time signal figure sized from data limits."""

    return _make_data_scaled_figure(xlim, ylim, dpi=dpi)


def make_cartesian_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
    """Create a generic equal-aspect Cartesian figure sized from data limits."""

    return _make_data_scaled_figure(xlim, ylim, dpi=dpi)


def make_phasor_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
    """Create a phasor-plane figure sized from data limits."""

    return _make_data_scaled_figure(xlim, ylim, dpi=dpi)


def _coerce_tick_labels(ticks, labels, formatter):
    """Return a label list that matches a tick list."""

    if labels is None:
        return [formatter(tick) for tick in ticks]

    labels = list(labels)
    if len(labels) != len(ticks):
        raise ValueError("tick label count must match tick count")
    return labels


def _draw_centered_tick(ax, value, *, axis="x"):
    """Draw a tick centered on the axis line."""

    if axis == "x":
        ax.plot([value, value], [-TICK_HALF_LEN, TICK_HALF_LEN],
                color=AXIS_COLOR, lw=TICK_LW, zorder=5)
    elif axis == "y":
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [value, value],
                color=AXIS_COLOR, lw=TICK_LW, zorder=5)
    else:
        raise ValueError("axis must be 'x' or 'y'")


def setup_origin_axes(
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
    x_tick_labels=None,
    y_tick_labels=None,
    y_tick_label_side="left",
    show_x_tick_labels=True,
    show_y_tick_labels=True,
    x_minor_grid_step=1,
    y_minor_grid_step=1,
    equal_aspect=True,
):
    """Configure a clean origin-centered Cartesian axis layout."""

    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)

    if equal_aspect:
        ax.set_aspect("equal", adjustable="box")

    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.xaxis.set_minor_locator(mticker.MultipleLocator(x_minor_grid_step))
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(y_minor_grid_step))

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

    x_labels = _coerce_tick_labels(xticks, x_tick_labels, math_label)
    y_labels = _coerce_tick_labels(yticks, y_tick_labels, math_label)

    for t, label in zip(xticks, x_labels):
        if abs(float(t)) < 1e-12:
            continue

        _draw_centered_tick(ax, t, axis="x")
        if show_x_tick_labels and label is not None:
            ax.text(t, X_TICK_LABEL_Y, label,
                    fontsize=TICK_LABEL_SIZE,
                    ha="center", va="top",
                    color=TICK_LABEL_COLOR,
                    zorder=6)

    for y, label in zip(yticks, y_labels):
        if abs(float(y)) < 1e-12:
            continue

        _draw_centered_tick(ax, y, axis="y")
        if show_y_tick_labels and label is not None:
            if y_tick_label_side == "right":
                ax.text(Y_TICK_LABEL_X, y, label,
                        fontsize=TICK_LABEL_SIZE,
                        ha="left", va="center",
                        color=TICK_LABEL_COLOR,
                        zorder=6)
            else:
                ax.text(-Y_TICK_LABEL_X, y, label,
                        fontsize=TICK_LABEL_SIZE,
                        ha="right", va="center",
                        color=TICK_LABEL_COLOR,
                        zorder=6)

    if show_origin:
        ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$",
                fontsize=TICK_LABEL_SIZE,
                ha="left", va="top",
                color=TICK_LABEL_COLOR,
                zorder=6)

    if x_axis_label is not None:
        ax.text(x_axis_end + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, x_axis_label,
                fontsize=AXIS_LABEL_SIZE,
                ha="left", va="center",
                color=LABEL_COLOR,
                clip_on=False)

    if y_axis_label is not None:
        ax.text(0, y_axis_end + Y_AXIS_LABEL_Y_PAD, y_axis_label,
                fontsize=TOP_LABEL_SIZE,
                ha="center", va="bottom",
                color=LABEL_COLOR,
                clip_on=False)


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
    show_x_tick_labels=True,
    show_y_tick_labels=True,
    x_minor_grid_step=1,
    y_minor_grid_step=1,
    equal_aspect=True,
):
    """Configure the shared continuous-time signal axis style."""

    setup_origin_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=xticks,
        yticks=yticks,
        x_axis_label=x_axis_label,
        y_axis_label=y_axis_label,
        show_grid=show_grid,
        show_origin=show_origin,
        x_tick_labels=None,
        y_tick_labels=None,
        y_tick_label_side=y_tick_label_side,
        show_x_tick_labels=show_x_tick_labels,
        show_y_tick_labels=show_y_tick_labels,
        x_minor_grid_step=x_minor_grid_step,
        y_minor_grid_step=y_minor_grid_step,
        equal_aspect=equal_aspect,
    )


def setup_phasor_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_axis_label=r"$\Re\{X\}$",
    y_axis_label=r"$\Im\{X\}$",
    show_grid=True,
    show_origin=True,
    x_tick_labels=None,
    y_tick_labels=None,
    y_tick_label_side="left",
    show_x_tick_labels=True,
    show_y_tick_labels=True,
    x_minor_grid_step=1,
    y_minor_grid_step=1,
    equal_aspect=True,
):
    """Configure the shared complex-plane style used for phasor diagrams."""

    setup_origin_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=xticks,
        yticks=yticks,
        x_axis_label=x_axis_label,
        y_axis_label=y_axis_label,
        show_grid=show_grid,
        show_origin=show_origin,
        x_tick_labels=x_tick_labels,
        y_tick_labels=y_tick_labels,
        y_tick_label_side=y_tick_label_side,
        show_x_tick_labels=show_x_tick_labels,
        show_y_tick_labels=show_y_tick_labels,
        x_minor_grid_step=x_minor_grid_step,
        y_minor_grid_step=y_minor_grid_step,
        equal_aspect=equal_aspect,
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
    """Draw an open-circle endpoint marker."""

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
    """Draw a closed-circle endpoint marker."""

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
        linestyle=(0, (1.1, 2.4)),
        zorder=3,
    )


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
    """Draw a vertical guide or marker line."""

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
    """Draw a horizontal guide or marker line."""

    ax.plot([x0, x1], [y, y], color=color, linewidth=lw, linestyle=linestyle, zorder=zorder)


def draw_support_bracket(
    ax,
    start,
    end,
    y=-0.38,
    *,
    label=None,
    color=ANNOTATION_COLOR,
):
    """Draw a bracket marking a support or duration interval."""

    ax.plot([start, end], [y, y], color=color, linewidth=ANNOTATION_LW, zorder=5)
    ax.plot([start, start], [y - BRACKET_CAP_HALF_LEN, y + BRACKET_CAP_HALF_LEN],
            color=color, linewidth=ANNOTATION_LW, zorder=5)
    ax.plot([end, end], [y - BRACKET_CAP_HALF_LEN, y + BRACKET_CAP_HALF_LEN],
            color=color, linewidth=ANNOTATION_LW, zorder=5)
    if label is not None:
        ax.text(
            (start + end) / 2,
            y - BRACKET_LABEL_GAP,
            label,
            fontsize=ANNOTATION_SIZE,
            ha="center",
            va="top",
            color=color,
        )


def draw_duration_bracket(ax, start, end, y=-0.38, *, label=None):
    """Convenience wrapper for a support-duration bracket."""

    draw_support_bracket(ax, start, end, y=y, label=label)


def draw_amplitude_bracket(
    ax,
    x_bracket,
    y0,
    y1,
    *,
    color=ANNOTATION_COLOR,
):
    """Draw a vertical amplitude bracket."""

    ax.plot([x_bracket, x_bracket], [y0, y1], color=color, linewidth=ANNOTATION_LW, zorder=5)
    ax.plot([x_bracket - AMPLITUDE_CAP_HALF_LEN, x_bracket + AMPLITUDE_CAP_HALF_LEN], [y0, y0],
            color=color, linewidth=ANNOTATION_LW, zorder=5)
    ax.plot([x_bracket - AMPLITUDE_CAP_HALF_LEN, x_bracket + AMPLITUDE_CAP_HALF_LEN], [y1, y1],
            color=color, linewidth=ANNOTATION_LW, zorder=5)


def draw_offset_line(ax, x_start, x_end, offset):
    """Draw a baseline or offset reference line."""

    draw_horizontal_marker_line(ax, offset, x_start, x_end)


def shade_region(ax, x_left, x_right, *, alpha=0.08, color=SIGNAL_COLOR, zorder=0):
    """Shade a vertical support region."""

    ax.axvspan(x_left, x_right, color=color, alpha=alpha, zorder=zorder)


def unit_step(t):
    """Return the unit step u(t)."""

    return np.where(np.asarray(t, dtype=float) >= 0, 1.0, 0.0)


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


def causal_exponential(t, alpha=1.0, amplitude=1.0, t0=0.0):
    """Return amplitude * exp(-alpha * (t - t0)) * u(t - t0)."""

    tau = np.asarray(t, dtype=float) - t0
    return amplitude * np.exp(-alpha * tau) * unit_step(tau)


def shifted_causal_exponential(t, alpha=1.0, amplitude=1.0, shift=0.0):
    """Alias for a delayed causal exponential."""

    return causal_exponential(t, alpha=alpha, amplitude=amplitude, t0=shift)


def sinusoid(t, *, amplitude=1.0, omega=1.0, phase=0.0, offset=0.0, kind="cos"):
    """Return a sine or cosine wave with an optional offset."""

    t = np.asarray(t, dtype=float)
    angle = omega * t + phase

    if kind == "cos":
        return offset + amplitude * np.cos(angle)
    if kind == "sin":
        return offset + amplitude * np.sin(angle)
    raise ValueError("kind must be 'cos' or 'sin'")


def cosine_wave(t, *, amplitude=1.0, omega=1.0, phase=0.0, offset=0.0):
    """Return a cosine wave."""

    return sinusoid(t, amplitude=amplitude, omega=omega, phase=phase, offset=offset, kind="cos")


def sine_wave(t, *, amplitude=1.0, omega=1.0, phase=0.0, offset=0.0):
    """Return a sine wave."""

    return sinusoid(t, amplitude=amplitude, omega=omega, phase=phase, offset=offset, kind="sin")


def phasor_complex(magnitude, angle):
    """Return a complex phasor magnitude * exp(j * angle)."""

    return np.asarray(magnitude, dtype=float) * np.exp(1j * np.asarray(angle, dtype=float))


def phasor_components(magnitude, angle):
    """Return the Cartesian components of a phasor."""

    magnitude = np.asarray(magnitude, dtype=float)
    angle = np.asarray(angle, dtype=float)
    return magnitude * np.cos(angle), magnitude * np.sin(angle)


def phasor_endpoint(magnitude, angle, origin=(0.0, 0.0)):
    """Return the endpoint of a phasor drawn from a given origin."""

    origin = np.asarray(origin, dtype=float)
    x, y = phasor_components(magnitude, angle)
    return origin[0] + x, origin[1] + y


def circle_points(radius=1.0, center=(0.0, 0.0), *, theta_start=0.0, theta_end=TAU, num=256):
    """Return sampled points on a circular arc."""

    theta = np.linspace(theta_start, theta_end, num)
    center = np.asarray(center, dtype=float)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    return x, y, theta


def unit_circle_points(center=(0.0, 0.0), *, num=256):
    """Return sampled points on the unit circle."""

    return circle_points(1.0, center, num=num)


def draw_unit_circle(
    ax,
    *,
    radius=1.0,
    center=(0.0, 0.0),
    color=GUIDE_COLOR,
    lw=GRID_LW,
    linestyle=(0, (1.1, 2.4)),
    alpha=0.18,
    zorder=2,
):
    """Draw a light reference circle."""

    circle = mpatches.Circle(
        center,
        radius=radius,
        fill=False,
        edgecolor=color,
        linewidth=lw,
        linestyle=linestyle,
        alpha=alpha,
        zorder=zorder,
    )
    ax.add_patch(circle)
    return circle


def draw_vector_arrow(
    ax,
    x0,
    y0,
    dx,
    dy,
    *,
    color=SIGNAL_COLOR,
    zorder=4,
    width=VECTOR_ARROW_SHAFT_WIDTH_DATA,
    headwidth=4.2,
    headlength=5.5,
    headaxislength=4.3,
):
    """Draw a data-scaled arrow and return its endpoint."""

    ax.quiver(
        x0,
        y0,
        dx,
        dy,
        angles="xy",
        scale_units="xy",
        scale=1,
        units="xy",
        width=width,
        headwidth=headwidth,
        headlength=headlength,
        headaxislength=headaxislength,
        color=color,
        pivot="tail",
        clip_on=False,
        zorder=zorder,
    )
    return x0 + dx, y0 + dy


def draw_phasor(
    ax,
    magnitude,
    angle,
    *,
    origin=(0.0, 0.0),
    color=SIGNAL_COLOR,
    zorder=4,
    label=None,
    label_offset=(0.08, 0.08),
    label_kwargs=None,
):
    """Draw a phasor vector from an origin and optionally label it."""

    origin = np.asarray(origin, dtype=float)
    dx, dy = phasor_components(magnitude, angle)
    x1, y1 = draw_vector_arrow(
        ax,
        origin[0],
        origin[1],
        float(np.asarray(dx, dtype=float)),
        float(np.asarray(dy, dtype=float)),
        color=color,
        zorder=zorder,
    )

    if label is not None:
        text_kwargs = {
            "fontsize": ANNOTATION_SIZE,
            "ha": "left",
            "va": "bottom",
            "color": LABEL_COLOR,
        }
        if label_kwargs:
            text_kwargs.update(label_kwargs)

        offset = np.asarray(label_offset, dtype=float)
        ax.text(x1 + offset[0], y1 + offset[1], label, **text_kwargs)

    return x1, y1


def draw_projection_guides(ax, x, y, *, color=GUIDE_COLOR):
    """Draw orthogonal dotted guides from a point to the coordinate axes."""

    draw_dotted_guide(ax, [x, x], [0, y])
    draw_dotted_guide(ax, [0, x], [y, y])


def draw_arc(
    ax,
    radius,
    theta_start,
    theta_end,
    *,
    center=(0.0, 0.0),
    color=ANNOTATION_COLOR,
    lw=ANNOTATION_LW,
    zorder=5,
    num=96,
    arrow=False,
):
    """Draw an arc between two angles and optionally add an arrowhead."""

    x, y, _ = circle_points(
        radius,
        center,
        theta_start=theta_start,
        theta_end=theta_end,
        num=num,
    )
    ax.plot(x, y, color=color, linewidth=lw, zorder=zorder)

    if arrow and len(x) >= 2:
        draw_vector_arrow(
            ax,
            x[-2],
            y[-2],
            x[-1] - x[-2],
            y[-1] - y[-2],
            color=color,
            zorder=zorder,
            width=px_to_data(2.2),
        )

    return x, y


def draw_phase_arc(
    ax,
    theta_start,
    theta_end,
    *,
    radius=0.55,
    center=(0.0, 0.0),
    color=ANNOTATION_COLOR,
    lw=ANNOTATION_LW,
    zorder=5,
    label=None,
    label_radius=None,
    arrow=False,
):
    """Draw a phase-angle arc and optionally annotate it."""

    x, y = draw_arc(
        ax,
        radius,
        theta_start,
        theta_end,
        center=center,
        color=color,
        lw=lw,
        zorder=zorder,
        arrow=arrow,
    )

    if label is not None:
        mid = 0.5 * (theta_start + theta_end)
        rr = radius if label_radius is None else label_radius
        center = np.asarray(center, dtype=float)
        ax.text(
            center[0] + rr * np.cos(mid),
            center[1] + rr * np.sin(mid),
            label,
            fontsize=ANNOTATION_SIZE,
            ha="center",
            va="center",
            color=color,
            zorder=zorder + 1,
        )

    return x, y


def save_figure(fig, output_path):
    """Save a figure using the shared export settings and close it."""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        output_path,
        dpi=CANONICAL_DPI,
        bbox_inches="tight",
        facecolor=BACKGROUND_COLOR,
    )
    plt.close(fig)
