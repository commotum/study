"""Shared matplotlib boilerplate for CTS continuous-time signal figures.

This reference file centralizes the visual defaults and reusable helpers for
EE01-M03-01, Time Shifting. Later topic workers can copy or adapt these
helpers without re-reading the full style guide.

The module does not render any image on import. It uses matplotlib, NumPy, and
pathlib only.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator


# ---------------------------------------------------------------------------
# Module identity
# ---------------------------------------------------------------------------

COURSE_NAME = "Continuous Time Signal Processing"
COURSE_CODE = "CTS"
COURSE_ID = "EE01"
UNIT_NUMBER = 3
UNIT_NAME = "Unit 3"
MODULE_ID = "EE01-M03-01"
MODULE_NUMBER = "3.1"
MODULE_NAME = "Time Shifting"


# ---------------------------------------------------------------------------
# Canonical geometry and styling
# ---------------------------------------------------------------------------

BACKGROUND_COLOR = "white"
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
# Typography and stroke widths
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

SHIFT_ARROW_KW = dict(
    angles="xy",
    scale_units="xy",
    scale=1,
    units="xy",
    width=AXIS_ARROW_SHAFT_WIDTH_DATA,
    headwidth=4.0,
    headlength=5.2,
    headaxislength=4.1,
    color=ANNOTATION_COLOR,
    pivot="tail",
    clip_on=False,
)

GUIDE_LINESTYLE = (0, (1.1, 2.4))


# ---------------------------------------------------------------------------
# Figure helpers
# ---------------------------------------------------------------------------

def make_ct_signal_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
    """Create a standard CTS figure sized from explicit data limits."""

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
    """Create a stacked CTS figure with one aligned x-axis across panels."""

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


def new_ct_figure(*, figsize=None, dpi=CANONICAL_DPI):
    """Create a generic white-background figure with constrained layout."""

    return plt.subplots(
        figsize=figsize,
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=True,
    )


def save_figure(fig, output_path, *, dpi=CANONICAL_DPI):
    """Save a figure using the shared export settings."""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        output_path,
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        bbox_inches="tight",
    )
    plt.close(fig)


def make_output_path(filename, *, image_dir="images"):
    """Return a path in the lesson image folder for a rendered asset."""

    return Path(__file__).resolve().parent / image_dir / filename


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


# ---------------------------------------------------------------------------
# Axis helpers
# ---------------------------------------------------------------------------

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

    ax.quiver(x_axis_start, 0, x_axis_end - x_axis_start, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y_axis_start, 0, y_axis_end - y_axis_start, **AXIS_ARROW_KW)

    for index, t in enumerate(xticks):
        if abs(t) < 1e-12:
            continue

        ax.plot(
            [t, t],
            [-TICK_HALF_LEN, TICK_HALF_LEN],
            color=AXIS_COLOR,
            lw=TICK_LW,
            zorder=5,
        )

        if show_x_tick_labels:
            label = math_label(t) if x_tick_labels is None else x_tick_labels[index]
            ax.text(
                t,
                X_TICK_LABEL_Y,
                label,
                fontsize=TICK_LABEL_SIZE,
                ha="center",
                va="top",
                color=TICK_LABEL_COLOR,
                zorder=6,
            )

    for index, y in enumerate(yticks):
        if abs(y) < 1e-12:
            continue

        ax.plot(
            [-TICK_HALF_LEN, TICK_HALF_LEN],
            [y, y],
            color=AXIS_COLOR,
            lw=TICK_LW,
            zorder=5,
        )

        if show_y_tick_labels:
            label = math_label(y) if y_tick_labels is None else y_tick_labels[index]
            if y_tick_label_side == "right":
                ax.text(
                    Y_TICK_LABEL_X,
                    y,
                    label,
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
                    label,
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


# ---------------------------------------------------------------------------
# Signal drawing helpers
# ---------------------------------------------------------------------------

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
    """Plot a smooth continuous-time signal trace."""

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
        linestyle=GUIDE_LINESTYLE,
        zorder=3,
    )


def draw_vertical_guide(ax, x, y0, y1, *, color=GUIDE_COLOR, zorder=3):
    """Draw a vertical dotted guide line."""

    ax.plot([x, x], [y0, y1], color=color, linewidth=GUIDE_LW, linestyle=GUIDE_LINESTYLE, zorder=zorder)


def draw_horizontal_guide(ax, y, x0, x1, *, color=GUIDE_COLOR, zorder=3):
    """Draw a horizontal dotted guide line."""

    ax.plot([x0, x1], [y, y], color=color, linewidth=GUIDE_LW, linestyle=GUIDE_LINESTYLE, zorder=zorder)


def draw_support_bracket(ax, start, end, y=-0.38, *, label=None, color=ANNOTATION_COLOR):
    """Draw a bracket marking a support or duration interval."""

    ax.plot([start, end], [y, y], color=color, linewidth=ANNOTATION_LW, zorder=5)
    ax.plot(
        [start, start],
        [y - BRACKET_CAP_HALF_LEN, y + BRACKET_CAP_HALF_LEN],
        color=color,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )
    ax.plot(
        [end, end],
        [y - BRACKET_CAP_HALF_LEN, y + BRACKET_CAP_HALF_LEN],
        color=color,
        linewidth=ANNOTATION_LW,
        zorder=5,
    )
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


def draw_amplitude_bracket(ax, x_bracket, y0, y1, *, color=ANNOTATION_COLOR):
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


def draw_offset_guide(ax, x_start, x_end, offset):
    """Draw a baseline or offset reference line."""

    draw_horizontal_guide(ax, offset, x_start, x_end)


def draw_shift_arrow(
    ax,
    x_start,
    x_end,
    y,
    *,
    label=None,
    label_offset=px_to_data(14),
    color=ANNOTATION_COLOR,
    zorder=5,
):
    """Draw a horizontal translation arrow used in time-shift diagrams."""

    arrow_kw = dict(SHIFT_ARROW_KW)
    arrow_kw["color"] = color
    arrow_kw["zorder"] = zorder
    ax.quiver(x_start, y, x_end - x_start, 0, **arrow_kw)

    if label is not None:
        ax.text(
            (x_start + x_end) / 2,
            y + label_offset,
            label,
            fontsize=ANNOTATION_SIZE,
            ha="center",
            va="bottom",
            color=color,
            zorder=zorder + 1,
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


# ---------------------------------------------------------------------------
# Signal-building helpers
# ---------------------------------------------------------------------------

def unit_step(t):
    """Return the unit step u(t)."""

    return np.where(np.asarray(t, dtype=float) >= 0, 1.0, 0.0)


def shifted_unit_step(t, shift=0.0):
    """Return the shifted unit step u(t - shift)."""

    return unit_step(np.asarray(t, dtype=float) - shift)


def step_difference(t, start, end, amplitude=1.0):
    """Return amplitude * (u(t - start) - u(t - end))."""

    t = np.asarray(t, dtype=float)
    return amplitude * (shifted_unit_step(t, start) - shifted_unit_step(t, end))


def rectangular_window(t, start, end, amplitude=1.0):
    """Return a rectangular window built from unit steps."""

    return step_difference(t, start, end, amplitude=amplitude)


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


def gaussian_pulse(t, sigma=1.0, amplitude=1.0, center=0.0):
    """Return a centered Gaussian pulse."""

    t = np.asarray(t, dtype=float)
    return amplitude * np.exp(-0.5 * ((t - center) / sigma) ** 2)


def causal_exponential(t, alpha=1.0, amplitude=1.0, t0=0.0):
    """Return amplitude * exp(-alpha * (t - t0)) * u(t - t0)."""

    tau = np.asarray(t, dtype=float) - t0
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


def shift_signal_samples(t, x, shift):
    """Shift a sampled signal horizontally by a constant amount."""

    t = np.asarray(t, dtype=float)
    x = np.asarray(x, dtype=float)
    return t + shift, x


def translate_signal_samples(t, x, shift):
    """Alias for shift_signal_samples."""

    return shift_signal_samples(t, x, shift)


def piecewise_linear(xs, ys):
    """Return NumPy arrays for a piecewise linear trace."""

    return np.asarray(xs, dtype=float), np.asarray(ys, dtype=float)

OUTPUT_PATH = Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/3.1--time-shifting-Images/images/l002-s003-qg-q002-choice-c-q002-choice-c.png')

def build_figure():
    xlim = (-6.2, 0.20000000000000018)
    ylim = (-0.5, 3.6)
    fig, ax = make_ct_signal_figure(xlim, ylim)
    setup_ct_signal_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=[-5, -4, -3, -2, -1],
        yticks=[1, 2, 3],
        x_axis_label=r"$t$",
        y_axis_label=r"$x(t)$",
    )

    t = [-6, -5, -4, -3, -2, -1, -1, 0]
    x = [0, 0, 1, 1, 3, 3, 0, 0]
    plot_signal(ax, t, x, lw=SIGNAL_LW, zorder=4)

    return fig

def main():
    fig = build_figure()
    save_figure(fig, Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/3.1--time-shifting-Images/images/l002-s003-qg-q002-choice-c-q002-choice-c.png'))

if __name__ == "__main__":
    main()
