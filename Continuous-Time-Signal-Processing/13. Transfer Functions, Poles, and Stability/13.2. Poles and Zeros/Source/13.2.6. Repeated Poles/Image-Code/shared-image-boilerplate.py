"""Shared matplotlib boilerplate for CTS poles-and-zeros image generation.

This file centralizes the visual defaults for the EE01-M13-02 module so later
topic workers can copy or adapt the same axis, marker, and annotation helpers
without rereading the full style guide.

Only NumPy and matplotlib are used for plotting; no image is rendered here.
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
UNIT_NUMBER = 13
UNIT_NAME = "Unit 13"
MODULE_ID = "EE01-M13-02"
MODULE_NUMBER = "13.2"
MODULE_NAME = "Poles and Zeros"

CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150
INCHES_PER_DATA_UNIT = PX_PER_DATA_UNIT / CANONICAL_DPI

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

SIGNAL_LW = 7.1 * 72 / CANONICAL_DPI
SMOOTH_SIGNAL_LW = 5.2 * 72 / CANONICAL_DPI
AXIS_LW = 4.3 * 72 / CANONICAL_DPI
TICK_LW = 2.7 * 72 / CANONICAL_DPI
GRID_LW = 1.3 * 72 / CANONICAL_DPI
GUIDE_LW = 3.3 * 72 / CANONICAL_DPI
ANNOTATION_LW = 2.9 * 72 / CANONICAL_DPI

TICK_LABEL_SIZE = 35.6 * 72 / CANONICAL_DPI
AXIS_LABEL_SIZE = 53.3 * 72 / CANONICAL_DPI
TOP_LABEL_SIZE = 57.8 * 72 / CANONICAL_DPI
ANNOTATION_SIZE = 33.3 * 72 / CANONICAL_DPI

TICK_HALF_LEN = 8.25 / PX_PER_DATA_UNIT
OPEN_MARKER_SIZE = 20.0 * 72 / CANONICAL_DPI
CLOSED_MARKER_SIZE = 17.8 * 72 / CANONICAL_DPI
ENDPOINT_EDGEWIDTH = 5.1 * 72 / CANONICAL_DPI

POLE_MARKER_SIZE = 21.0 * 72 / CANONICAL_DPI
POLE_MARKER_EDGEWIDTH = 5.1 * 72 / CANONICAL_DPI

X_TICK_LABEL_Y = -24 / PX_PER_DATA_UNIT
Y_TICK_LABEL_X = 18 / PX_PER_DATA_UNIT
ORIGIN_LABEL_X = 9 / PX_PER_DATA_UNIT
ORIGIN_LABEL_Y = -12 / PX_PER_DATA_UNIT
X_AXIS_LABEL_X_PAD = 15 / PX_PER_DATA_UNIT
X_AXIS_LABEL_Y = -4.5 / PX_PER_DATA_UNIT
Y_AXIS_LABEL_Y_PAD = 18 / PX_PER_DATA_UNIT

BRACKET_CAP_HALF_LEN = 9 / PX_PER_DATA_UNIT
BRACKET_LABEL_GAP = 18 / PX_PER_DATA_UNIT
AMPLITUDE_CAP_HALF_LEN = 10.5 / PX_PER_DATA_UNIT

POINT_LABEL_OFFSET = (8 / PX_PER_DATA_UNIT, 8 / PX_PER_DATA_UNIT)
GRID_LINESTYLE = (0, (1.1, 2.4))

AXIS_ARROW_SHAFT_WIDTH_DATA = 4.3 / PX_PER_DATA_UNIT
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
    """Apply the shared serif, mathtext, and white-background defaults."""

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


def px_to_pt(px):
    """Convert pixels to points at the canonical render scale."""

    return px * 72 / CANONICAL_DPI


def px_to_data(px):
    """Convert pixels to data units at the canonical render scale."""

    return px / PX_PER_DATA_UNIT


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


def make_complex_plane_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
    """Create a standard complex-plane figure sized from explicit limits."""

    return make_ct_signal_figure(xlim, ylim, dpi=dpi)


def make_s_plane_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
    """Alias for the shared pole-zero plotting canvas."""

    return make_complex_plane_figure(xlim, ylim, dpi=dpi)


make_signal_figure = make_ct_signal_figure
make_time_domain_figure = make_ct_signal_figure
make_waveform_figure = make_ct_signal_figure
make_pole_zero_figure = make_complex_plane_figure
make_plane_figure = make_complex_plane_figure


def make_output_path(filename, *, image_dir="images"):
    """Return a path in the lesson image folder for a rendered asset."""

    return Path(__file__).resolve().parent / image_dir / filename


def math_label(value):
    """Return a mathtext label for a numeric tick or pass through a string."""

    if isinstance(value, str):
        return value

    numeric = float(value)
    rounded = round(numeric)
    if abs(numeric - rounded) < 1e-9:
        return rf"${int(rounded)}$"
    return rf"${numeric:g}$"


def complex_xy(value):
    """Convert a complex number or pair into Cartesian coordinates."""

    if isinstance(value, (tuple, list, np.ndarray)):
        if len(value) == 2:
            return float(value[0]), float(value[1])

    z = complex(value)
    return float(np.real(z)), float(np.imag(z))


def format_cartesian_pair(x, y):
    """Format a Cartesian coordinate pair as math text."""

    return rf"$({x:g}, {y:g})$"


def _set_manual_cartesian_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_tick_labels=None,
    y_tick_labels=None,
    x_axis_label,
    y_axis_label,
    show_grid=True,
    show_origin=True,
    y_tick_label_side="left",
    show_x_tick_labels=True,
    show_y_tick_labels=True,
    x_minor_grid_step=1,
    y_minor_grid_step=1,
    equal_aspect=True,
):
    """Internal shared axis layout for origin-centered CTS figures."""

    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)

    if equal_aspect:
        ax.set_aspect("equal", adjustable="box")

    ax.set_xticks(xticks)
    ax.set_yticks(yticks)

    if x_minor_grid_step is not None and x_minor_grid_step > 0:
        ax.xaxis.set_minor_locator(MultipleLocator(x_minor_grid_step))
    if y_minor_grid_step is not None and y_minor_grid_step > 0:
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

    if x_tick_labels is None:
        x_tick_labels = xticks
    if y_tick_labels is None:
        y_tick_labels = yticks

    for t, label in zip(xticks, x_tick_labels):
        if abs(float(t)) < 1e-12:
            continue

        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)

        if show_x_tick_labels:
            ax.text(
                t,
                X_TICK_LABEL_Y,
                math_label(label),
                fontsize=TICK_LABEL_SIZE,
                ha="center",
                va="top",
                color=TICK_LABEL_COLOR,
                zorder=6,
            )

    for y, label in zip(yticks, y_tick_labels):
        if abs(float(y)) < 1e-12:
            continue

        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)

        if show_y_tick_labels:
            if y_tick_label_side == "right":
                ax.text(
                    Y_TICK_LABEL_X,
                    y,
                    math_label(label),
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
                    math_label(label),
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

    _set_manual_cartesian_axes(
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
    )


def setup_complex_plane_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_tick_labels=None,
    y_tick_labels=None,
    x_axis_label=r"$\Re\{s\}$",
    y_axis_label=r"$\Im\{s\}$",
    show_grid=True,
    show_origin=True,
    y_tick_label_side="left",
    show_x_tick_labels=True,
    show_y_tick_labels=True,
    x_minor_grid_step=1,
    y_minor_grid_step=1,
    equal_aspect=True,
):
    """Configure a pole-zero style complex-plane diagram."""

    _set_manual_cartesian_axes(
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
    )


setup_signal_axes = setup_ct_signal_axes
setup_time_domain_axes = setup_ct_signal_axes
setup_waveform_axes = setup_ct_signal_axes
setup_s_plane_axes = setup_complex_plane_axes
setup_pole_zero_axes = setup_complex_plane_axes


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
    """Plot a smooth signal curve."""

    ax.plot(
        t,
        x,
        color=color,
        linewidth=lw,
        solid_capstyle="round",
        zorder=zorder,
    )


def _draw_marked_point(
    ax,
    x,
    y,
    *,
    marker="o",
    markersize=CLOSED_MARKER_SIZE,
    markerfacecolor=SIGNAL_COLOR,
    markeredgecolor=SIGNAL_COLOR,
    markeredgewidth=ENDPOINT_EDGEWIDTH,
    label=None,
    label_offset=POINT_LABEL_OFFSET,
    label_size=ANNOTATION_SIZE,
    label_color=LABEL_COLOR,
    zorder=6,
):
    """Draw a single marked point with an optional text label."""

    plot_kwargs = dict(
        marker=marker,
        markersize=markersize,
        linestyle="None",
        zorder=zorder,
    )
    if markerfacecolor is not None:
        plot_kwargs["markerfacecolor"] = markerfacecolor
    if markeredgecolor is not None:
        plot_kwargs["markeredgecolor"] = markeredgecolor
    if markeredgewidth is not None:
        plot_kwargs["markeredgewidth"] = markeredgewidth

    ax.plot(x, y, **plot_kwargs)

    if label is not None:
        ax.text(
            x + label_offset[0],
            y + label_offset[1],
            label,
            fontsize=label_size,
            ha="left",
            va="bottom",
            color=label_color,
            zorder=zorder + 1,
        )


def draw_open_endpoint(ax, t0, x0, *, label=None, label_offset=POINT_LABEL_OFFSET):
    """Draw an open endpoint marker."""

    _draw_marked_point(
        ax,
        t0,
        x0,
        marker="o",
        markersize=OPEN_MARKER_SIZE,
        markerfacecolor="white",
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=ENDPOINT_EDGEWIDTH,
        label=label,
        label_offset=label_offset,
    )


def draw_closed_endpoint(ax, t0, x0, *, label=None, label_offset=POINT_LABEL_OFFSET):
    """Draw a closed endpoint marker."""

    _draw_marked_point(
        ax,
        t0,
        x0,
        marker="o",
        markersize=CLOSED_MARKER_SIZE,
        markerfacecolor=SIGNAL_COLOR,
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=ENDPOINT_EDGEWIDTH,
        label=label,
        label_offset=label_offset,
    )


def draw_zero(ax, x, y, *, label=None, label_offset=POINT_LABEL_OFFSET):
    """Draw a zero marker as an open circle."""

    draw_open_endpoint(ax, x, y, label=label, label_offset=label_offset)


def draw_pole(ax, x, y, *, label=None, label_offset=POINT_LABEL_OFFSET):
    """Draw a pole marker as an x-shaped marker."""

    _draw_marked_point(
        ax,
        x,
        y,
        marker="x",
        markersize=POLE_MARKER_SIZE,
        markerfacecolor=None,
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=POLE_MARKER_EDGEWIDTH,
        label=label,
        label_offset=label_offset,
    )


def draw_point(ax, x, y, *, label=None, label_offset=POINT_LABEL_OFFSET):
    """Draw a generic filled point marker."""

    _draw_marked_point(ax, x, y, label=label, label_offset=label_offset)


def draw_complex_point(ax, value, **kwargs):
    """Draw a point given as a complex number or coordinate pair."""

    x, y = complex_xy(value)
    draw_point(ax, x, y, **kwargs)


def draw_dotted_guide(ax, x_values, y_values):
    """Draw a subtle dotted guide line."""

    ax.plot(
        x_values,
        y_values,
        color=GUIDE_COLOR,
        linewidth=GUIDE_LW,
        linestyle=GRID_LINESTYLE,
        zorder=3,
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


def draw_support_bracket(ax, start, end, y=-0.38, *, label=None, color=ANNOTATION_COLOR):
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
    """Convenience wrapper for a duration bracket."""

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


def draw_offset_line(ax, x_start, x_end, offset):
    """Draw a baseline or offset reference line."""

    draw_horizontal_marker_line(ax, offset, x_start, x_end)


def shade_region(ax, x_left, x_right, *, alpha=0.08, color=SIGNAL_COLOR, zorder=0):
    """Shade a vertical region behind the main content."""

    ax.axvspan(x_left, x_right, color=color, alpha=alpha, zorder=zorder)


def save_figure(fig, output_path):
    """Save a figure with the shared export settings."""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=CANONICAL_DPI, bbox_inches="tight", facecolor=BACKGROUND_COLOR)
    plt.close(fig)
