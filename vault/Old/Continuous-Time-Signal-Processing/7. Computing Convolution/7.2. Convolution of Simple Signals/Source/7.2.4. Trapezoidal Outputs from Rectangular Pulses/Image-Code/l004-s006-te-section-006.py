"""Shared matplotlib boilerplate for CTS continuous-time signal figures.

This module centralizes the textbook signal-plot styling used across
EE01-M07-02, Convolution of Simple Signals. Later topic workers can copy or
adapt these helpers without re-reading the full style guide.

Only matplotlib and NumPy are used here.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


plt.rcParams.update(
    {
        "mathtext.fontset": "cm",
        "font.family": "serif",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)


COURSE_NAME = "Continuous Time Signal Processing"
COURSE_CODE = "CTS"
COURSE_ID = "EE01"
UNIT_NUMBER = 7
UNIT_NAME = "Unit 7"
MODULE_ID = "EE01-M07-02"
MODULE_NUMBER = "7.2"
MODULE_NAME = "Convolution of Simple Signals"

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
DPI = 160

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


def configure_matplotlib():
    """Re-apply the shared serif and white-background defaults."""

    plt.rcParams.update(
        {
            "mathtext.fontset": "cm",
            "font.family": "serif",
            "figure.facecolor": BACKGROUND_COLOR,
            "axes.facecolor": BACKGROUND_COLOR,
        }
    )


def new_ct_figure(*, square=False, dpi=DPI):
    """Create a standard CTS figure and axes pair."""

    figsize = SQUARE_FIGSIZE if square else DEFAULT_FIGSIZE
    return plt.subplots(figsize=figsize, dpi=dpi)


def math_label(value):
    """Return a mathtext label for a tick value."""

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
    """Configure a clean continuous-time signal axis layout."""

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

    # Draw axes through the origin with arrowheads only on positive ends.
    ax.quiver(x_axis_start, 0, x_axis_end - x_axis_start, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y_axis_start, 0, y_axis_end - y_axis_start, **AXIS_ARROW_KW)

    for t in xticks:
        if abs(t) < 1e-12:
            continue
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN],
                color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(t, -0.16, math_label(t),
                fontsize=TICK_LABEL_SIZE, ha="center", va="top",
                color=TICK_LABEL_COLOR, zorder=6)

    for y in yticks:
        if abs(y) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y],
                color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if y_tick_label_side == "right":
            ax.text(0.12, y, math_label(y),
                    fontsize=TICK_LABEL_SIZE, ha="left", va="center",
                    color=TICK_LABEL_COLOR, zorder=6)
        else:
            ax.text(-0.12, y, math_label(y),
                    fontsize=TICK_LABEL_SIZE, ha="right", va="center",
                    color=TICK_LABEL_COLOR, zorder=6)

    if show_origin:
        ax.text(0.06, -0.08, r"$0$",
                fontsize=TICK_LABEL_SIZE, ha="left", va="top",
                color=TICK_LABEL_COLOR, zorder=6)

    x_pad = 0.08 * (xlim[1] - xlim[0]) / 6
    y_pad = 0.08 * (ylim[1] - ylim[0]) / 4

    ax.text(x_axis_end + x_pad, -0.03, x_axis_label,
            fontsize=AXIS_LABEL_SIZE, ha="left", va="center",
            color=LABEL_COLOR, clip_on=False)
    ax.text(0, y_axis_end + y_pad, y_axis_label,
            fontsize=TOP_LABEL_SIZE, ha="center", va="bottom",
            color=LABEL_COLOR, clip_on=False)


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


def draw_amplitude_bracket(
    ax,
    x_bracket,
    y0,
    y1,
    *,
    color=ANNOTATION_COLOR,
    tick_half_width=0.07,
):
    """Draw a vertical amplitude bracket."""

    ax.plot([x_bracket, x_bracket], [y0, y1], color=color, linewidth=1.3, zorder=5)
    ax.plot([x_bracket - tick_half_width, x_bracket + tick_half_width], [y0, y0],
            color=color, linewidth=1.3, zorder=5)
    ax.plot([x_bracket - tick_half_width, x_bracket + tick_half_width], [y1, y1],
            color=color, linewidth=1.3, zorder=5)


def draw_offset_line(ax, x_start, x_end, offset):
    """Draw a dotted baseline or offset reference."""

    draw_horizontal_marker_line(ax, offset, x_start, x_end)


def shade_region(ax, x_left, x_right, *, alpha=0.08, color=SIGNAL_COLOR, zorder=0):
    """Shade a vertical support region."""

    ax.axvspan(x_left, x_right, color=color, alpha=alpha, zorder=zorder)


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


def causal_exponential(t, alpha=1.0, amplitude=1.0, t0=0.0):
    """Return a causal exponential amplitude * exp(-alpha * (t - t0)) * u(t - t0)."""

    tau = np.asarray(t) - t0
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


def make_output_path(filename):
    """Return a path beside this boilerplate file for rendered assets."""

    return Path(__file__).resolve().parent / filename

def save_figure(fig, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, bbox_inches="tight", facecolor="white")


def draw_rect_outline(ax, left, right, *, base=0.0, top=1.0, fill=True, fill_alpha=0.08, lw=SIGNAL_LW):
    if fill:
        ax.fill_between([left, right], [top, top], [base, base],
                        color=SIGNAL_COLOR, alpha=fill_alpha, zorder=2)
    ax.plot([left, left, right, right, left],
            [base, top, top, base, base],
            color=SIGNAL_COLOR, lw=lw,
            solid_capstyle="butt", solid_joinstyle="miter",
            zorder=4)


def draw_pulse_panel(ax, left, right, *, y_label, width_label, title=None):
    pad = max(0.65, 0.18 * (right - left))
    setup_ct_signal_axes(
        ax,
        xlim=(left - pad, right + pad),
        ylim=(-0.58, 1.48),
        xticks=[left, right],
        yticks=[1],
        x_axis_label=r"$t$",
        y_axis_label=y_label,
    )
    draw_rect_outline(ax, left, right, fill=False)
    draw_support_bracket(ax, left, right, y=-0.34, label=rf"${width_label}$")
    if title:
        ax.set_title(title, fontsize=18, color=LABEL_COLOR, pad=7)


def draw_snapshot_panel(
    ax,
    fixed_width,
    moving_width,
    *,
    t_value,
    fixed_label=r"$x(\tau)$",
    moving_label=r"$h(t-\tau)$",
    fixed_width_label=None,
    moving_width_label=None,
    overlap_label=None,
    title=None,
    moving_left_label=None,
    moving_right_label=r"$t$",
    fixed_left_label=r"$0$",
    fixed_right_label=None,
    show_symbolic_labels=True,
    phase_caption=None,
):
    fixed_left = 0.0
    fixed_right = float(fixed_width)
    moving_left = float(t_value) - float(moving_width)
    moving_right = float(t_value)
    xlim_left = min(fixed_left, moving_left) - 0.85
    xlim_right = max(fixed_right, moving_right) + 0.85
    setup_ct_signal_axes(
        ax,
        xlim=(xlim_left, xlim_right),
        ylim=(-0.72, 1.58),
        xticks=[fixed_left, fixed_right],
        yticks=[1],
        x_axis_label=r"$\tau$",
        y_axis_label=r"$1$",
    )

    overlap_left = max(fixed_left, moving_left)
    overlap_right = min(fixed_right, moving_right)
    if overlap_right > overlap_left:
        ax.fill_between([overlap_left, overlap_right], [1, 1], [0, 0],
                        color=SIGNAL_COLOR, alpha=0.20, zorder=3)

    draw_rect_outline(ax, fixed_left, fixed_right, fill=False)
    draw_rect_outline(ax, moving_left, moving_right, fill=False)

    ax.text((fixed_left + fixed_right) / 2, 1.20, fixed_label,
            fontsize=18, ha="center", va="bottom", color=LABEL_COLOR)
    ax.text((moving_left + moving_right) / 2, 1.20, moving_label,
            fontsize=18, ha="center", va="bottom", color=LABEL_COLOR)

    if fixed_width_label is None:
        fixed_width_label = rf"${int(fixed_width)}$"
    if moving_width_label is None:
        moving_width_label = rf"${int(moving_width)}$"

    draw_support_bracket(ax, fixed_left, fixed_right, y=-0.38, label=fixed_width_label)
    draw_support_bracket(ax, moving_left, moving_right, y=-0.53, label=moving_width_label)

    ax.text(fixed_left, -0.12, fixed_left_label, fontsize=16,
            ha="center", va="top", color=TICK_LABEL_COLOR)
    ax.text(fixed_right, -0.12, fixed_right_label or rf"${int(fixed_width)}$",
            fontsize=16, ha="center", va="top", color=TICK_LABEL_COLOR)
    ax.text(moving_left, -0.12, moving_left_label or rf"$t-{int(moving_width)}$",
            fontsize=16, ha="center", va="top", color=TICK_LABEL_COLOR)
    ax.text(moving_right, -0.12, moving_right_label,
            fontsize=16, ha="center", va="top", color=TICK_LABEL_COLOR)

    if overlap_label is not None and overlap_right > overlap_left:
        ax.text((overlap_left + overlap_right) / 2, 0.48, overlap_label,
                fontsize=18, ha="center", va="center", color=LABEL_COLOR)
    elif overlap_label is not None:
        ax.text((fixed_right + moving_left) / 2, 0.18, overlap_label,
                fontsize=18, ha="center", va="center", color=LABEL_COLOR)

    if phase_caption:
        ax.set_title(phase_caption, fontsize=18, color=LABEL_COLOR, pad=7)
    if title:
        ax.text(0.5, 1.02, title, transform=ax.transAxes,
                fontsize=18, ha="center", va="bottom", color=LABEL_COLOR)


def draw_breakpoint_timeline(
    ax,
    *,
    x_width,
    h_width,
    breakpoints,
    region_labels,
    title=None,
    show_curve=False,
    curve_alpha=1.0,
):
    short = min(x_width, h_width)
    long = max(x_width, h_width)
    total = x_width + h_width
    ymax = 1.28
    setup_ct_signal_axes(
        ax,
        xlim=(-0.85, total + 0.85),
        ylim=(-0.42, ymax),
        xticks=breakpoints,
        yticks=[1],
        x_axis_label=r"$t$",
        y_axis_label=r"$y(t)$",
    )

    ax.plot([-0.7, total + 0.7], [0, 0], color=AXIS_COLOR, lw=1.35, zorder=2)
    if show_curve:
        pts_x = [-0.6, 0, short, long, total, total + 0.6]
        pts_y = [0, 0, short, short, 0, 0]
        ax.plot(pts_x, pts_y, color=SIGNAL_COLOR, lw=SIGNAL_LW,
                alpha=curve_alpha, solid_capstyle="butt", solid_joinstyle="miter", zorder=4)

    for bp in breakpoints:
        ax.plot([bp, bp], [-0.05, 0.17], color=AXIS_COLOR, lw=1.2, zorder=5)
        ax.text(bp, -0.12, rf"${bp}$", fontsize=16, ha="center", va="top", color=TICK_LABEL_COLOR)

    if len(region_labels) == 2 and len(breakpoints) == 2:
        left_x = breakpoints[0] - 0.25
        right_x = breakpoints[1] + 0.25
        ax.text(left_x, -0.20, region_labels[0], fontsize=14, ha="right", va="center", color=LABEL_COLOR)
        ax.text(right_x, -0.20, region_labels[1], fontsize=14, ha="left", va="center", color=LABEL_COLOR)
    else:
        centers = [
            breakpoints[0] - 0.15,
            (breakpoints[0] + breakpoints[1]) / 2,
            (breakpoints[1] + breakpoints[2]) / 2,
            (breakpoints[2] + breakpoints[3]) / 2,
            breakpoints[3] + 0.15,
        ]
        y_positions = [-0.20, 0.24, 0.24, 0.24, -0.20]
        for x, y, label in zip(centers, y_positions, region_labels):
            ax.text(x, y, label, fontsize=14, ha="center", va="center", color=LABEL_COLOR)

    if title:
        ax.set_title(title, fontsize=18, color=LABEL_COLOR, pad=7)


def draw_output_full(ax, *, x_width, h_width, title=None):
    short = min(x_width, h_width)
    long = max(x_width, h_width)
    total = x_width + h_width
    setup_ct_signal_axes(
        ax,
        xlim=(-0.75, total + 0.75),
        ylim=(-0.40, short + 0.90),
        xticks=[0, short, long, total],
        yticks=list(range(1, short + 1)),
        x_axis_label=r"$t$",
        y_axis_label=r"$y(t)$",
    )
    ax.plot([-0.6, 0], [0, 0], color=AXIS_COLOR, lw=1.35, zorder=2)
    ax.plot([0, short], [0, short], color=SIGNAL_COLOR, lw=SIGNAL_LW, zorder=4)
    if long > short:
        ax.plot([short, long], [short, short], color=SIGNAL_COLOR, lw=SIGNAL_LW, zorder=4)
    ax.plot([long, total], [short, 0], color=SIGNAL_COLOR, lw=SIGNAL_LW, zorder=4)
    ax.plot([total, total + 0.6], [0, 0], color=AXIS_COLOR, lw=1.35, zorder=2)
    for bp, y in [(0, 0), (short, short), (long, short), (total, 0)]:
        draw_closed_endpoint(ax, bp, y)
    ax.text(-0.25, -0.18, r"$no\ overlap$", fontsize=14, ha="right", va="top", color=LABEL_COLOR)
    ax.text(short / 2, short * 0.45 + 0.05, r"$growing\ overlap$", fontsize=14, ha="center", va="center", color=LABEL_COLOR)
    ax.text((short + long) / 2, short + 0.24, r"$full\ overlap$", fontsize=14, ha="center", va="center", color=LABEL_COLOR)
    ax.text((long + total) / 2, short * 0.45 + 0.05, r"$shrinking\ overlap$", fontsize=14, ha="center", va="center", color=LABEL_COLOR)
    ax.text(total + 0.26, -0.18, r"$no\ overlap$", fontsize=14, ha="left", va="top", color=LABEL_COLOR)
    if title:
        ax.set_title(title, fontsize=18, color=LABEL_COLOR, pad=7)


def draw_output_phase(ax, *, x_width, h_width, phase, title=None):
    short = min(x_width, h_width)
    long = max(x_width, h_width)
    total = x_width + h_width
    setup_ct_signal_axes(
        ax,
        xlim=(-0.75, total + 0.75),
        ylim=(-0.40, short + 0.90),
        xticks=[0, short, long, total],
        yticks=list(range(1, short + 1)),
        x_axis_label=r"$t$",
        y_axis_label=r"$y(t)$",
    )
    ax.plot([-0.6, total + 0.6], [0, 0], color=AXIS_COLOR, lw=1.35, zorder=2)
    if phase == "grow":
        ax.plot([0, short], [0, short], color=SIGNAL_COLOR, lw=SIGNAL_LW, zorder=4)
        draw_closed_endpoint(ax, 0, 0)
        draw_closed_endpoint(ax, short, short)
        ax.text(short / 2, short * 0.55 + 0.06, r"$growing\ overlap$", fontsize=14, ha="center", va="center", color=LABEL_COLOR)
    elif phase == "plateau":
        ax.plot([short, long], [short, short], color=SIGNAL_COLOR, lw=SIGNAL_LW, zorder=4)
        draw_closed_endpoint(ax, short, short)
        draw_closed_endpoint(ax, long, short)
        ax.text((short + long) / 2, short + 0.20, r"$full\ overlap$", fontsize=14, ha="center", va="center", color=LABEL_COLOR)
    elif phase == "shrink":
        ax.plot([long, total], [short, 0], color=SIGNAL_COLOR, lw=SIGNAL_LW, zorder=4)
        draw_closed_endpoint(ax, long, short)
        draw_closed_endpoint(ax, total, 0)
        ax.text((long + total) / 2, short * 0.55 + 0.06, r"$shrinking\ overlap$", fontsize=14, ha="center", va="center", color=LABEL_COLOR)
    elif phase == "zero":
        ax.plot([-0.6, 0], [0, 0], color=SIGNAL_COLOR, lw=SIGNAL_LW, zorder=4)
        ax.plot([total, total + 0.6], [0, 0], color=SIGNAL_COLOR, lw=SIGNAL_LW, zorder=4)
        ax.text(0.3, 0.24, r"$no\ overlap$", fontsize=14, ha="left", va="center", color=LABEL_COLOR)
        ax.text(total - 0.3, 0.24, r"$no\ overlap$", fontsize=14, ha="right", va="center", color=LABEL_COLOR)
    if title:
        ax.set_title(title, fontsize=18, color=LABEL_COLOR, pad=7)


def render_overview(config):
    fig = plt.figure(figsize=config.get("figsize", (11.2, 13.0)), dpi=DPI)
    gs = fig.add_gridspec(3, 2, height_ratios=[1.0, 1.35, 1.55], hspace=0.48, wspace=0.35)
    ax_x = fig.add_subplot(gs[0, 0])
    ax_h = fig.add_subplot(gs[0, 1])
    ax_snap = fig.add_subplot(gs[1, :])
    ax_out = fig.add_subplot(gs[2, :])
    draw_pulse_panel(ax_x, 0, config["x_width"], y_label=r"$x(t)$", width_label=str(config["x_width"]))
    draw_pulse_panel(ax_h, 0, config["h_width"], y_label=r"$h(t)$", width_label=str(config["h_width"]))
    draw_snapshot_panel(
        ax_snap,
        config["x_width"],
        config["h_width"],
        t_value=config["snapshot_t"],
        fixed_label=r"$x(\tau)$",
        moving_label=r"$h(t-\tau)$",
        fixed_width_label=rf"${config['x_width']}$",
        moving_width_label=rf"${config['h_width']}$",
        overlap_label=config["snapshot_overlap_label"],
        moving_left_label=config.get("snapshot_moving_left_label"),
        moving_right_label=r"$t$",
        phase_caption=config.get("snapshot_title"),
    )
    draw_output_full(ax_out, x_width=config["x_width"], h_width=config["h_width"], title=config.get("output_title"))
    save_figure(fig, config["output_path"])


def render_sweep_prompt(config):
    fig = plt.figure(figsize=config.get("figsize", (11.6, 4.7)), dpi=DPI)
    gs = fig.add_gridspec(1, 3, wspace=0.32)
    for idx in range(3):
        ax = fig.add_subplot(gs[0, idx])
        draw_snapshot_panel(
            ax,
            config["x_width"],
            config["h_width"],
            t_value=config["snapshot_ts"][idx],
            fixed_label=r"$x(\tau)$",
            moving_label=r"$h(t-\tau)$",
            fixed_width_label=rf"${config['x_width']}$",
            moving_width_label=rf"${config['h_width']}$",
            overlap_label=config["overlap_labels"][idx],
            moving_left_label=config["moving_left_labels"][idx],
            moving_right_label=r"$t$",
            phase_caption=config.get("snapshot_titles", [None, None, None])[idx],
        )
    save_figure(fig, config["output_path"])


def render_sweep_tutorial(config):
    fig = plt.figure(figsize=config.get("figsize", (12.1, 7.6)), dpi=DPI)
    gs = fig.add_gridspec(2, 4, height_ratios=[1.0, 0.95], hspace=0.44, wspace=0.28)
    for idx in range(4):
        ax = fig.add_subplot(gs[0, idx])
        draw_snapshot_panel(
            ax,
            config["x_width"],
            config["h_width"],
            t_value=config["snapshot_ts"][idx],
            fixed_label=r"$x(\tau)$",
            moving_label=r"$h(t-\tau)$",
            fixed_width_label=rf"${config['x_width']}$",
            moving_width_label=rf"${config['h_width']}$",
            overlap_label=config["overlap_labels"][idx],
            moving_left_label=config["moving_left_labels"][idx],
            moving_right_label=r"$t$",
            phase_caption=config["snapshot_titles"][idx],
        )
    ax_t = fig.add_subplot(gs[1, :])
    draw_breakpoint_timeline(
        ax_t,
        x_width=config["x_width"],
        h_width=config["h_width"],
        breakpoints=config["breakpoints"],
        region_labels=config["region_labels"],
        title=config.get("timeline_title"),
        show_curve=False,
    )
    save_figure(fig, config["output_path"])


def render_no_overlap(config):
    fig = plt.figure(figsize=config.get("figsize", (11.2, 6.4)), dpi=DPI)
    gs = fig.add_gridspec(2, 2, height_ratios=[1.0, 0.95], hspace=0.38, wspace=0.26)
    for idx in range(2):
        ax = fig.add_subplot(gs[0, idx])
        draw_snapshot_panel(
            ax,
            config["x_width"],
            config["h_width"],
            t_value=config["snapshot_ts"][idx],
            fixed_label=r"$x(\tau)$",
            moving_label=r"$h(t-\tau)$",
            fixed_width_label=rf"${config['x_width']}$",
            moving_width_label=rf"${config['h_width']}$",
            overlap_label=r"$0$",
            moving_left_label=config["moving_left_labels"][idx],
            moving_right_label=r"$t$",
            phase_caption=config.get("snapshot_titles", [None, None])[idx],
        )
    ax_t = fig.add_subplot(gs[1, :])
    draw_breakpoint_timeline(
        ax_t,
        x_width=config["x_width"],
        h_width=config["h_width"],
        breakpoints=[0, config["x_width"] + config["h_width"]],
        region_labels=[config["left_region"], config["right_region"]],
        title=config.get("timeline_title"),
        show_curve=False,
    )
    save_figure(fig, config["output_path"])


def render_phase(config):
    fig = plt.figure(figsize=config.get("figsize", (9.6, 7.6)), dpi=DPI)
    gs = fig.add_gridspec(2, 1, height_ratios=[1.05, 1.0], hspace=0.36)
    ax_snap = fig.add_subplot(gs[0, 0])
    draw_snapshot_panel(
        ax_snap,
        config["x_width"],
        config["h_width"],
        t_value=config["snapshot_t"],
        fixed_label=r"$x(\tau)$",
        moving_label=r"$h(t-\tau)$",
        fixed_width_label=rf"${config['x_width']}$",
        moving_width_label=rf"${config['h_width']}$",
        overlap_label=config["overlap_label"],
        moving_left_label=config["moving_left_label"],
        moving_right_label=r"$t$",
        phase_caption=config.get("snapshot_title"),
    )
    ax_out = fig.add_subplot(gs[1, 0])
    draw_output_phase(ax_out, x_width=config["x_width"], h_width=config["h_width"], phase=config["phase"], title=config.get("output_title"))
    save_figure(fig, config["output_path"])


def render_input_output_prompt(config):
    fig = plt.figure(figsize=config.get("figsize", (11.0, 6.0)), dpi=DPI)
    gs = fig.add_gridspec(2, 2, height_ratios=[1.0, 0.92], hspace=0.38, wspace=0.30)
    ax_x = fig.add_subplot(gs[0, 0])
    ax_h = fig.add_subplot(gs[0, 1])
    draw_pulse_panel(ax_x, 0, config["x_width"], y_label=r"$x(t)$", width_label=str(config["x_width"]))
    draw_pulse_panel(ax_h, 0, config["h_width"], y_label=r"$h(t)$", width_label=str(config["h_width"]))
    ax_t = fig.add_subplot(gs[1, :])
    draw_breakpoint_timeline(
        ax_t,
        x_width=config["x_width"],
        h_width=config["h_width"],
        breakpoints=config["breakpoints"],
        region_labels=config["region_labels"],
        title=config.get("timeline_title"),
        show_curve=False,
    )
    save_figure(fig, config["output_path"])


def render_input_output_full(config):
    fig = plt.figure(figsize=config.get("figsize", (11.0, 8.4)), dpi=DPI)
    gs = fig.add_gridspec(2, 2, height_ratios=[1.0, 1.5], hspace=0.36, wspace=0.30)
    ax_x = fig.add_subplot(gs[0, 0])
    ax_h = fig.add_subplot(gs[0, 1])
    draw_pulse_panel(ax_x, 0, config["x_width"], y_label=r"$x(t)$", width_label=str(config["x_width"]))
    draw_pulse_panel(ax_h, 0, config["h_width"], y_label=r"$h(t)$", width_label=str(config["h_width"]))
    ax_out = fig.add_subplot(gs[1, :])
    draw_output_full(ax_out, x_width=config["x_width"], h_width=config["h_width"], title=config.get("output_title"))
    save_figure(fig, config["output_path"])


def render_scene(config):
    scene = config["scene"]
    if scene == "overview":
        render_overview(config)
    elif scene == "sweep_prompt":
        render_sweep_prompt(config)
    elif scene == "sweep_tutorial":
        render_sweep_tutorial(config)
    elif scene == "no_overlap":
        render_no_overlap(config)
    elif scene == "phase":
        render_phase(config)
    elif scene == "input_output_prompt":
        render_input_output_prompt(config)
    elif scene == "input_output_full":
        render_input_output_full(config)
    else:
        raise ValueError(f"Unknown scene type: {scene}")

CONFIG = {'h_width': 2,
 'moving_left_label': '$t-2$',
 'output_path': '/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/7.2--convolution-of-simple-signals-Images/images/l004-s006-te-section-006.png',
 'output_title': None,
 'overlap_label': '$7-t$',
 'phase': 'shrink',
 'scene': 'phase',
 'snapshot_t': 6.0,
 'snapshot_title': '$5<t<7$',
 'x_width': 5}

def main():
    render_scene(CONFIG)


if __name__ == '__main__':
    main()
