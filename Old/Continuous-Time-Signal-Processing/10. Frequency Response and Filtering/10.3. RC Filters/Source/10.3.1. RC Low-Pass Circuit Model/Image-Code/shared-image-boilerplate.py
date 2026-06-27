"""Shared matplotlib boilerplate for EE01-M10-03 RC Filters.

This module bundles the reusable CTS figure styling, waveform helpers,
schematic helpers, and RC response formulas used by later topic workers.
It is intentionally self-contained and uses only matplotlib and NumPy.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator


BACKGROUND_COLOR = "white"

COURSE_NAME = "Continuous Time Signal Processing"
COURSE_CODE = "CTS"
COURSE_ID = "EE01"
UNIT_NUMBER = 10
UNIT_NAME = "Unit 10"
MODULE_ID = "EE01-M10-03"
MODULE_NUMBER = "10.3"
MODULE_NAME = "RC Filters"
LESSON_SLUG = "continuous-time-signal-processing-ee01-m10-03"

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"

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
SCHEMATIC_LABEL_SIZE = ANNOTATION_SIZE

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

NODE_MARKER_SIZE = px_to_pt(10.5)
SOURCE_MARKER_SIZE = px_to_pt(18.0)

BRACKET_CAP_HALF_LEN = px_to_data(9)
BRACKET_LABEL_GAP = px_to_data(18)
AMPLITUDE_CAP_HALF_LEN = px_to_data(10.5)

AXIS_ARROW_SHAFT_WIDTH_DATA = px_to_data(4.3)
ARROW_MUTATION_SCALE = 18

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


def configure_matplotlib():
    """Apply the shared serif and white-background defaults."""

    plt.rcParams.update(
        {
            "mathtext.fontset": "cm",
            "font.family": "serif",
            "figure.facecolor": BACKGROUND_COLOR,
            "axes.facecolor": BACKGROUND_COLOR,
            "savefig.facecolor": BACKGROUND_COLOR,
            "axes.edgecolor": AXIS_COLOR,
            "axes.labelcolor": LABEL_COLOR,
            "xtick.color": TICK_LABEL_COLOR,
            "ytick.color": TICK_LABEL_COLOR,
        }
    )


configure_matplotlib()


def make_output_path(filename, *, image_dir="images"):
    """Return a path in the lesson image folder for a rendered asset."""

    return Path(__file__).resolve().parent / image_dir / filename


def save_figure(fig, output_path):
    """Save a figure with the shared export settings and close it."""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        output_path,
        dpi=CANONICAL_DPI,
        bbox_inches="tight",
        facecolor=BACKGROUND_COLOR,
    )
    plt.close(fig)


def make_generic_figure(figsize=(8.0, 4.8), *, dpi=CANONICAL_DPI):
    """Create a generic white-background matplotlib figure."""

    return plt.subplots(
        figsize=figsize,
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=True,
    )


def make_circuit_figure(figsize=(8.4, 4.6), *, dpi=CANONICAL_DPI):
    """Create a schematic-friendly figure with the shared layout defaults."""

    return plt.subplots(
        figsize=figsize,
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=True,
    )


def make_ct_signal_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
    """Create a CTS signal figure sized from explicit data limits."""

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


def make_stacked_ct_signal_figure(xlim, panel_ylims, *, gap_px=38, dpi=CANONICAL_DPI):
    """Create a stacked CTS figure sized from explicit panel data limits."""

    x_range = xlim[1] - xlim[0]
    axes_w_px = x_range * PX_PER_DATA_UNIT
    axes_h_px = sum((ylim[1] - ylim[0]) * PX_PER_DATA_UNIT for ylim in panel_ylims)
    fig_w_px = MARGIN_LEFT_PX + axes_w_px + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_TOP_PX + axes_h_px + MARGIN_BOTTOM_PX + gap_px * (len(panel_ylims) - 1)

    fig = plt.figure(
        figsize=(fig_w_px / dpi, fig_h_px / dpi),
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=True,
    )
    gridspec = fig.add_gridspec(
        len(panel_ylims),
        1,
        height_ratios=[ylim[1] - ylim[0] for ylim in panel_ylims],
    )
    axes = [fig.add_subplot(gridspec[i, 0]) for i in range(len(panel_ylims))]
    return fig, axes


def math_label(value):
    """Return a mathtext label for a numeric tick or pass through a string."""

    if isinstance(value, str):
        return value

    numeric = float(value)
    rounded = round(numeric)
    if abs(numeric - rounded) < 1e-9:
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
    show_x_tick_labels=True,
    show_y_tick_labels=True,
    x_minor_grid_step=1,
    y_minor_grid_step=1,
    equal_aspect=True,
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
        ax.grid(True, which="both", linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
        ax.set_axisbelow(True)

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    x_axis_start, x_axis_end = xlim
    y_axis_start, y_axis_end = ylim

    # Draw the axes through the origin with arrowheads only on the positive ends.
    ax.quiver(x_axis_start, 0, x_axis_end - x_axis_start, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y_axis_start, 0, y_axis_end - y_axis_start, **AXIS_ARROW_KW)

    for t in xticks:
        if abs(t) < 1e-12:
            continue

        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)

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
        if abs(y) < 1e-12:
            continue

        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)

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


def setup_cartesian_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks=None,
    yticks=None,
    x_minor_grid_step=None,
    y_minor_grid_step=None,
    show_grid=True,
    equal_aspect=False,
    x_label=None,
    y_label=None,
    hide_top_right=True,
):
    """Style a conventional matplotlib axis for clean response plots."""

    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)

    if equal_aspect:
        ax.set_aspect("equal", adjustable="box")

    if xticks is not None:
        ax.set_xticks(xticks)
    if yticks is not None:
        ax.set_yticks(yticks)

    if x_minor_grid_step is not None:
        ax.xaxis.set_minor_locator(MultipleLocator(x_minor_grid_step))
    if y_minor_grid_step is not None:
        ax.yaxis.set_minor_locator(MultipleLocator(y_minor_grid_step))

    if show_grid:
        ax.grid(True, which="both", linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
        ax.set_axisbelow(True)

    if hide_top_right:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_color(AXIS_COLOR)
        ax.spines["left"].set_color(AXIS_COLOR)
        ax.spines["bottom"].set_linewidth(AXIS_LW)
        ax.spines["left"].set_linewidth(AXIS_LW)

    ax.tick_params(
        axis="both",
        which="both",
        direction="out",
        colors=TICK_LABEL_COLOR,
        labelsize=TICK_LABEL_SIZE,
    )

    if x_label is not None:
        ax.set_xlabel(x_label, fontsize=AXIS_LABEL_SIZE, color=LABEL_COLOR)
    if y_label is not None:
        ax.set_ylabel(y_label, fontsize=AXIS_LABEL_SIZE, color=LABEL_COLOR)


def setup_circuit_axes(ax, *, xlim, ylim, equal_aspect=True):
    """Set up an empty schematic canvas with the shared white background."""

    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)

    if equal_aspect:
        ax.set_aspect("equal", adjustable="box")

    ax.set_axis_off()


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
    ax.plot([start, start], [y - BRACKET_CAP_HALF_LEN, y + BRACKET_CAP_HALF_LEN], color=color, linewidth=ANNOTATION_LW, zorder=5)
    ax.plot([end, end], [y - BRACKET_CAP_HALF_LEN, y + BRACKET_CAP_HALF_LEN], color=color, linewidth=ANNOTATION_LW, zorder=5)
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
    ax.plot(
        [x_bracket - AMPLITUDE_CAP_HALF_LEN, x_bracket + AMPLITUDE_CAP_HALF_LEN],
        [y0, y0],
        color=color,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )
    ax.plot(
        [x_bracket - AMPLITUDE_CAP_HALF_LEN, x_bracket + AMPLITUDE_CAP_HALF_LEN],
        [y1, y1],
        color=color,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )


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
    if width <= 0:
        return np.zeros_like(t)
    half_width = width / 2.0
    slope = np.maximum(1.0 - np.abs(t - center) / half_width, 0.0)
    return amplitude * slope


def causal_exponential(t, alpha=1.0, amplitude=1.0, t0=0.0):
    """Return a causal exponential amplitude * exp(-alpha * (t - t0)) * u(t - t0)."""

    tau = np.asarray(t, dtype=float) - t0
    return amplitude * np.exp(-alpha * tau) * unit_step(tau)


def shifted_causal_exponential(t, alpha=1.0, amplitude=1.0, shift=0.0):
    """Alias for a delayed causal exponential."""

    return causal_exponential(t, alpha=alpha, amplitude=amplitude, t0=shift)


def piecewise_linear(xs, ys):
    """Return NumPy arrays for a piecewise linear trace."""

    return np.asarray(xs, dtype=float), np.asarray(ys, dtype=float)


def time_shift(t, shift):
    """Shift a time vector by a constant amount."""

    return np.asarray(t, dtype=float) + shift


def time_reverse(t):
    """Reverse a time vector about the origin."""

    return -np.asarray(t, dtype=float)


def draw_piecewise_constant_signal(
    ax,
    segments,
    *,
    xlim,
    baseline=0.0,
    color=SIGNAL_COLOR,
    lw=SIGNAL_LW,
    zorder=4,
):
    """Draw a connected piecewise-constant signal with endpoint markers."""

    t = [xlim[0]]
    x = [baseline]
    current_x = xlim[0]
    current_y = baseline

    for idx, (start, end, level, left_closed, right_closed) in enumerate(segments):
        if start != current_x:
            t.append(start)
            x.append(current_y)

        t.append(start)
        x.append(level)
        t.append(end)
        x.append(level)

        next_start = segments[idx + 1][0] if idx + 1 < len(segments) else xlim[1]
        if next_start != end:
            if level != baseline:
                t.append(end)
                x.append(baseline)
            current_y = baseline
        else:
            current_y = level

        current_x = end

    if current_x < xlim[1]:
        t.append(xlim[1])
        x.append(baseline)

    plot_signal(ax, t, x, lw=lw, color=color, zorder=zorder)

    for start, end, level, left_closed, right_closed in segments:
        (draw_closed_endpoint if left_closed else draw_open_endpoint)(ax, start, level)
        (draw_closed_endpoint if right_closed else draw_open_endpoint)(ax, end, level)


def magnitude_to_db(magnitude, floor_db=-120.0):
    """Convert a magnitude response to decibels with a floor to avoid log(0)."""

    magnitude = np.abs(np.asarray(magnitude, dtype=float))
    floor = 10 ** (floor_db / 20.0)
    return 20.0 * np.log10(np.maximum(magnitude, floor))


def radians_to_degrees(theta):
    """Convert radians to degrees."""

    return np.degrees(theta)


def degrees_to_radians(theta):
    """Convert degrees to radians."""

    return np.radians(theta)


def hz_to_omega(frequency_hz):
    """Convert frequency in hertz to angular frequency in radians/second."""

    return 2.0 * np.pi * np.asarray(frequency_hz, dtype=float)


def omega_to_hz(omega):
    """Convert angular frequency in radians/second to hertz."""

    return np.asarray(omega, dtype=float) / (2.0 * np.pi)


def rc_time_constant(R, C):
    """Return the RC time constant tau = R * C."""

    return float(R) * float(C)


def rc_cutoff_angular_frequency(R, C):
    """Return the RC cutoff angular frequency 1 / (R * C)."""

    return 1.0 / rc_time_constant(R, C)


def rc_cutoff_frequency_hz(R, C):
    """Return the RC cutoff frequency in hertz."""

    return rc_cutoff_angular_frequency(R, C) / (2.0 * np.pi)


def rc_lowpass_transfer(omega, tau):
    """Return the normalized RC low-pass transfer function H(jω)."""

    omega = np.asarray(omega, dtype=float)
    s = 1j * omega * tau
    return 1.0 / (1.0 + s)


def rc_highpass_transfer(omega, tau):
    """Return the normalized RC high-pass transfer function H(jω)."""

    omega = np.asarray(omega, dtype=float)
    s = 1j * omega * tau
    return s / (1.0 + s)


def rc_lowpass_mag(omega, tau):
    """Return the magnitude response of the normalized RC low-pass filter."""

    omega = np.asarray(omega, dtype=float)
    return 1.0 / np.sqrt(1.0 + (omega * tau) ** 2)


def rc_highpass_mag(omega, tau):
    """Return the magnitude response of the normalized RC high-pass filter."""

    omega = np.asarray(omega, dtype=float)
    return (omega * tau) / np.sqrt(1.0 + (omega * tau) ** 2)


def rc_lowpass_phase(omega, tau):
    """Return the phase response of the normalized RC low-pass filter."""

    omega = np.asarray(omega, dtype=float)
    return -np.arctan(omega * tau)


def rc_highpass_phase(omega, tau):
    """Return the phase response of the normalized RC high-pass filter."""

    omega = np.asarray(omega, dtype=float)
    return np.pi / 2.0 - np.arctan(omega * tau)


def rc_lowpass_mag_db(omega, tau, floor_db=-120.0):
    """Return the low-pass magnitude response in decibels."""

    return magnitude_to_db(rc_lowpass_mag(omega, tau), floor_db=floor_db)


def rc_highpass_mag_db(omega, tau, floor_db=-120.0):
    """Return the high-pass magnitude response in decibels."""

    return magnitude_to_db(rc_highpass_mag(omega, tau), floor_db=floor_db)


def rc_lowpass_step_response(t, tau, initial=0.0, final_value=1.0, t0=0.0):
    """Return the causal first-order low-pass step response."""

    t = np.asarray(t, dtype=float) - t0
    response = initial + (final_value - initial) * (1.0 - np.exp(-np.maximum(t, 0.0) / tau))
    return np.where(t >= 0, response, initial)


def rc_highpass_step_response(t, tau, amplitude=1.0, t0=0.0):
    """Return the causal first-order high-pass step response."""

    t = np.asarray(t, dtype=float) - t0
    return amplitude * np.exp(-np.maximum(t, 0.0) / tau) * unit_step(t)


def rc_lowpass_impulse_response(t, tau, amplitude=1.0, t0=0.0):
    """Return the causal low-pass impulse response."""

    t = np.asarray(t, dtype=float) - t0
    return amplitude * (1.0 / tau) * np.exp(-np.maximum(t, 0.0) / tau) * unit_step(t)


def _vector_frame(start, end):
    """Return a local orthonormal frame for a segment from start to end."""

    p0 = np.asarray(start, dtype=float)
    p1 = np.asarray(end, dtype=float)
    delta = p1 - p0
    length = float(np.hypot(delta[0], delta[1]))
    if length <= 0:
        raise ValueError("start and end must be different points")
    unit = delta / length
    perp = np.array([-unit[1], unit[0]])
    return p0, p1, unit, perp, length


def draw_wire(ax, start, end, *, color=AXIS_COLOR, lw=AXIS_LW, zorder=2):
    """Draw a schematic wire between two points."""

    start = np.asarray(start, dtype=float)
    end = np.asarray(end, dtype=float)
    ax.plot(
        [start[0], end[0]],
        [start[1], end[1]],
        color=color,
        linewidth=lw,
        solid_capstyle="butt",
        zorder=zorder,
    )


def draw_node(ax, x, y, *, size=NODE_MARKER_SIZE, color=AXIS_COLOR, zorder=6):
    """Draw a filled schematic node."""

    ax.plot(
        x,
        y,
        marker="o",
        markersize=size,
        markerfacecolor=color,
        markeredgecolor=color,
        markeredgewidth=0,
        linestyle="None",
        zorder=zorder,
    )


def draw_open_node(ax, x, y, *, size=SOURCE_MARKER_SIZE, color=AXIS_COLOR, zorder=6):
    """Draw an open schematic node or terminal."""

    ax.plot(
        x,
        y,
        marker="o",
        markersize=size,
        markerfacecolor="white",
        markeredgecolor=color,
        markeredgewidth=ENDPOINT_EDGEWIDTH,
        linestyle="None",
        zorder=zorder,
    )


def draw_voltage_source(
    ax,
    x,
    y,
    *,
    size=SOURCE_MARKER_SIZE,
    color=AXIS_COLOR,
    show_polarity=False,
    polarity_offset=None,
    zorder=6,
):
    """Draw a simple voltage-source circle with optional polarity marks."""

    draw_open_node(ax, x, y, size=size, color=color, zorder=zorder)

    if show_polarity:
        if polarity_offset is None:
            polarity_offset = px_to_data(7)
        ax.text(
            x,
            y + polarity_offset,
            r"$+$",
            fontsize=SCHEMATIC_LABEL_SIZE,
            ha="center",
            va="bottom",
            color=color,
            zorder=zorder + 1,
        )
        ax.text(
            x,
            y - polarity_offset,
            r"$-$",
            fontsize=SCHEMATIC_LABEL_SIZE,
            ha="center",
            va="top",
            color=color,
            zorder=zorder + 1,
        )


def draw_arrow(
    ax,
    x0,
    y0,
    x1,
    y1,
    *,
    color=ANNOTATION_COLOR,
    lw=ANNOTATION_LW,
    mutation_scale=ARROW_MUTATION_SCALE,
    zorder=6,
):
    """Draw a simple annotation arrow."""

    ax.annotate(
        "",
        xy=(x1, y1),
        xytext=(x0, y0),
        arrowprops=dict(
            arrowstyle="->",
            color=color,
            lw=lw,
            mutation_scale=mutation_scale,
            shrinkA=0,
            shrinkB=0,
        ),
        annotation_clip=False,
        zorder=zorder,
    )


def draw_label(
    ax,
    x,
    y,
    text,
    *,
    fontsize=SCHEMATIC_LABEL_SIZE,
    ha="center",
    va="center",
    color=LABEL_COLOR,
    rotation=0,
    zorder=7,
    clip_on=False,
):
    """Draw a plain text label with the shared serif styling."""

    ax.text(
        x,
        y,
        text,
        fontsize=fontsize,
        ha=ha,
        va=va,
        color=color,
        rotation=rotation,
        zorder=zorder,
        clip_on=clip_on,
    )


def draw_resistor(
    ax,
    start,
    end,
    *,
    zigzags=6,
    amplitude=None,
    lead_fraction=0.18,
    color=AXIS_COLOR,
    lw=AXIS_LW,
    zorder=2,
):
    """Draw a schematic resistor along an arbitrary line segment."""

    p0, p1, unit, perp, length = _vector_frame(start, end)
    if zigzags < 1:
        draw_wire(ax, p0, p1, color=color, lw=lw, zorder=zorder)
        return

    lead = min(lead_fraction * length, 0.35 * length)
    body_length = length - 2 * lead
    if body_length <= 0:
        draw_wire(ax, p0, p1, color=color, lw=lw, zorder=zorder)
        return

    if amplitude is None:
        amplitude = min(px_to_data(7.5), 0.24 * body_length)
    else:
        amplitude = min(float(amplitude), 0.24 * body_length)

    draw_wire(ax, p0, p0 + lead * unit, color=color, lw=lw, zorder=zorder)
    draw_wire(ax, p1 - lead * unit, p1, color=color, lw=lw, zorder=zorder)

    body_points = 2 * zigzags + 1
    s = np.linspace(0.0, body_length, body_points)
    offsets = np.zeros(body_points)
    if body_points > 2:
        offsets[1:-1] = amplitude * np.where(np.arange(1, body_points - 1) % 2 == 1, 1.0, -1.0)

    pts = p0 + lead * unit + s[:, None] * unit + offsets[:, None] * perp
    ax.plot(
        pts[:, 0],
        pts[:, 1],
        color=color,
        linewidth=lw,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=zorder,
    )


def draw_capacitor(
    ax,
    start,
    end,
    *,
    plate_span=None,
    lead_fraction=0.22,
    color=AXIS_COLOR,
    lw=AXIS_LW,
    zorder=2,
):
    """Draw a schematic capacitor along an arbitrary line segment."""

    p0, p1, unit, perp, length = _vector_frame(start, end)
    lead = min(lead_fraction * length, 0.38 * length)
    if 2 * lead >= length:
        draw_wire(ax, p0, p1, color=color, lw=lw, zorder=zorder)
        return

    if plate_span is None:
        plate_span = px_to_data(18.0)
    plate_span = min(float(plate_span), 0.75 * length)
    half_span = 0.5 * plate_span

    left_center = p0 + lead * unit
    right_center = p1 - lead * unit

    draw_wire(ax, p0, left_center, color=color, lw=lw, zorder=zorder)
    draw_wire(ax, right_center, p1, color=color, lw=lw, zorder=zorder)

    for center in (left_center, right_center):
        a = center - half_span * perp
        b = center + half_span * perp
        ax.plot(
            [a[0], b[0]],
            [a[1], b[1]],
            color=color,
            linewidth=lw,
            solid_capstyle="butt",
            zorder=zorder + 1,
        )


def draw_ground(ax, x, y, *, stem_length=None, width=None, step=None, color=AXIS_COLOR, lw=AXIS_LW, zorder=2):
    """Draw a simple grounded reference symbol below a point."""

    if stem_length is None:
        stem_length = px_to_data(10.5)
    if width is None:
        width = px_to_data(16.0)
    if step is None:
        step = px_to_data(4.0)

    base_y = y - stem_length
    draw_wire(ax, (x, y), (x, base_y), color=color, lw=lw, zorder=zorder)

    for idx, frac in enumerate((1.0, 0.68, 0.36)):
        yy = base_y - idx * step
        half = 0.5 * width * frac
        ax.plot(
            [x - half, x + half],
            [yy, yy],
            color=color,
            linewidth=lw,
            solid_capstyle="butt",
            zorder=zorder,
        )


def draw_piecewise_constant_signal(
    ax,
    segments,
    *,
    xlim,
    baseline=0.0,
    color=SIGNAL_COLOR,
    lw=SIGNAL_LW,
    zorder=4,
):
    """Draw a connected piecewise-constant signal with endpoint markers."""

    t = [xlim[0]]
    x = [baseline]
    current_x = xlim[0]
    current_y = baseline

    for idx, (start, end, level, left_closed, right_closed) in enumerate(segments):
        if start != current_x:
            t.append(start)
            x.append(current_y)

        t.append(start)
        x.append(level)
        t.append(end)
        x.append(level)

        next_start = segments[idx + 1][0] if idx + 1 < len(segments) else xlim[1]
        if next_start != end:
            if level != baseline:
                t.append(end)
                x.append(baseline)
            current_y = baseline
        else:
            current_y = level

        current_x = end

    if current_x < xlim[1]:
        t.append(xlim[1])
        x.append(baseline)

    plot_signal(ax, t, x, lw=lw, color=color, zorder=zorder)

    for start, end, level, left_closed, right_closed in segments:
        (draw_closed_endpoint if left_closed else draw_open_endpoint)(ax, start, level)
        (draw_closed_endpoint if right_closed else draw_open_endpoint)(ax, end, level)


make_signal_figure = make_ct_signal_figure
make_time_domain_figure = make_ct_signal_figure
make_waveform_figure = make_ct_signal_figure
make_response_figure = make_generic_figure
make_frequency_response_figure = make_generic_figure
make_bode_figure = make_generic_figure
make_schematic_figure = make_circuit_figure

setup_signal_axes = setup_ct_signal_axes
setup_time_domain_axes = setup_ct_signal_axes
setup_waveform_axes = setup_ct_signal_axes
setup_response_axes = setup_cartesian_axes
setup_frequency_response_axes = setup_cartesian_axes
setup_schematic_axes = setup_circuit_axes

