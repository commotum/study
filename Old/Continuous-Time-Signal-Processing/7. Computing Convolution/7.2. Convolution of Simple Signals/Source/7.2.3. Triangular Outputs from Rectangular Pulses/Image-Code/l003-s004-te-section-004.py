"""Shared matplotlib boilerplate for CTS continuous-time signal figures.

This module centralizes the textbook signal-plot styling used across
EE01-M07-02, Convolution of Simple Signals. Later topic workers can copy or
adapt these helpers without re-reading the full style guide.

Only matplotlib and NumPy are used here.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
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




def draw_pulse_box(ax, left, right, height=1.0, baseline=0.0, *, fill_alpha=0.08, outline_lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    """Draw a rectangular pulse with a light fill."""

    ax.fill_between([left, right], baseline, height, color=color, alpha=fill_alpha, zorder=zorder - 1)
    plot_signal(
        ax,
        [left, left, right, right],
        [baseline, height, height, baseline],
        lw=outline_lw,
        color=color,
        zorder=zorder,
    )


def draw_triangle_output(ax, x0, xm, x1, y_peak, *, lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    """Draw a simple triangular output sketch."""

    plot_signal(ax, [x0, xm, x1], [0, y_peak, 0], lw=lw, color=color, zorder=zorder)


def draw_line_segment(ax, x0, y0, x1, y1, *, lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    """Draw a single line segment with the shared signal styling."""

    plot_signal(ax, [x0, x1], [y0, y1], lw=lw, color=color, zorder=zorder)


def draw_timeline_axis(ax, xmin, xmax, markers=None, marker_labels=None, *, axis_label=r"$t$", label_y=-0.23, marker_height=0.08):
    """Draw a compact horizontal timeline with a right arrow."""

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(-0.55, 0.55)
    ax.axis("off")
    ax.annotate(
        "",
        xy=(xmax, 0),
        xytext=(xmin, 0),
        arrowprops=dict(arrowstyle="->", color=AXIS_COLOR, lw=AXIS_LW, shrinkA=0, shrinkB=0),
    )
    if markers is not None:
        for x in markers:
            ax.plot([x, x], [-marker_height, marker_height], color=AXIS_COLOR, lw=TICK_LW, zorder=3)
    if marker_labels is not None:
        for x, label in marker_labels:
            ax.text(x, label_y, label, fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR)
    ax.text(xmax + 0.02 * (xmax - xmin), -0.02, axis_label, fontsize=AXIS_LABEL_SIZE, ha="left", va="center", color=LABEL_COLOR, clip_on=False)


def main():
    configure_matplotlib()
    image_output_path = Path(r"/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/7.2--convolution-of-simple-signals-Images/images/l003-s004-te-section-004.png")
    image_output_path.parent.mkdir(parents=True, exist_ok=True)

    fig = plt.figure(figsize=(9.6, 7.9), dpi=DPI)
    gs = fig.add_gridspec(2, 1, height_ratios=[1.22, 0.82], hspace=0.30)
    ax_main = fig.add_subplot(gs[0])
    ax_branch = fig.add_subplot(gs[1])

    setup_ct_signal_axes(
        ax_main,
        xlim=(-0.65, 4.15),
        ylim=(-0.22, 3.85),
        xticks=[0, 2],
        yticks=[2, 3],
        x_axis_label=r"$\tau$",
        y_axis_label=r"$x(\tau)$",
        show_grid=True,
        show_origin=False,
        equal_aspect=True,
    )
    draw_pulse_box(ax_main, 0, 2, height=2, baseline=0, fill_alpha=0.10)
    draw_pulse_box(ax_main, 0, 2, height=3, baseline=0, fill_alpha=0.05)
    overlap_left = max(0, 0)
    overlap_right = min(2, 2)
    if overlap_right <= overlap_left:
        overlap_right = overlap_left + 0.05
    ax_main.axvspan(overlap_left, overlap_right, color=SIGNAL_COLOR, alpha=0.18, zorder=1)
    ax_main.text(0.08, 2.13, r"$x(\tau)$", fontsize=15, color=LABEL_COLOR, ha="left", va="bottom")
    ax_main.text(0 - 0.06, 3.13, r"$h(t-\tau)$", fontsize=15, color=LABEL_COLOR, ha="left", va="bottom")
    ax_main.text((overlap_left + overlap_right) / 2, 0.20, r"shrinking overlap length 4 - t", fontsize=13, color=ANNOTATION_COLOR, ha="center", va="bottom")
    ax_main.text((overlap_left + overlap_right) / 2, 3.26, r"height product 2 times 3 = 6", fontsize=14.5, color=ANNOTATION_COLOR, ha="center", va="bottom")
    ax_main.text(0, -0.19, r"$0$", fontsize=15, color=TICK_LABEL_COLOR, ha="center", va="top")
    ax_main.text(2, -0.19, r"$2$", fontsize=15, color=TICK_LABEL_COLOR, ha="center", va="top")
    ax_main.text(0, -0.19, r"$t-2$", fontsize=15, color=TICK_LABEL_COLOR, ha="center", va="top")
    ax_main.text(2, -0.19, r"$t$", fontsize=15, color=TICK_LABEL_COLOR, ha="center", va="top")
    ax_main.text(0.5, 1.03, r"Falling overlap region and output branch", transform=ax_main.transAxes, fontsize=15, color=LABEL_COLOR, ha="center", va="bottom")

    setup_ct_signal_axes(
        ax_branch,
        xlim=(1.8, 4.15),
        ylim=(-0.25, 13.4),
        xticks=[2, 4],
        yticks=[12],
        x_axis_label=r"$t$",
        y_axis_label=r"$y(t)$",
        show_grid=True,
        show_origin=True,
        equal_aspect=True,
    )
    draw_line_segment(ax_branch, 2, 12, 4, 0)
    ax_branch.text(2.1, 12.12, r"y(t)=6(4-t)", fontsize=14.5, color=LABEL_COLOR, ha="left", va="bottom")

    fig.savefig(image_output_path, bbox_inches="tight", facecolor="white")


if __name__ == "__main__":
    main()
