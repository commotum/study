"""Shared matplotlib boilerplate for CTS EE01-M01-03 image generation.

This file is a reusable reference for later topic image workers. It defines the
shared continuous-time signal style, canonical export scale, and helper
functions for axes, plots, markers, guides, and measurement brackets.

It intentionally does not render any figure or call ``plt.show()``.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


mpl.rcParams.update(
    {
        "mathtext.fontset": "cm",
        "font.family": "serif",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
    }
)


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
X_TICK_LABEL_Y = -24 / PX_PER_DATA_UNIT
Y_TICK_LABEL_X = 18 / PX_PER_DATA_UNIT
ORIGIN_LABEL_X = 9 / PX_PER_DATA_UNIT
ORIGIN_LABEL_Y = -12 / PX_PER_DATA_UNIT
X_AXIS_LABEL_X_PAD = 15 / PX_PER_DATA_UNIT
X_AXIS_LABEL_Y = -4.5 / PX_PER_DATA_UNIT
Y_AXIS_LABEL_Y_PAD = 18 / PX_PER_DATA_UNIT

OPEN_MARKER_SIZE = 20.0 * 72 / CANONICAL_DPI
CLOSED_MARKER_SIZE = 17.8 * 72 / CANONICAL_DPI
ENDPOINT_EDGEWIDTH = 5.1 * 72 / CANONICAL_DPI

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

BRACKET_CAP_HALF_LEN = 9 / PX_PER_DATA_UNIT
AMPLITUDE_CAP_HALF_LEN = 10.5 / PX_PER_DATA_UNIT
BRACKET_LABEL_GAP = 18 / PX_PER_DATA_UNIT

DEFAULT_SAVEFIG_KW = dict(
    dpi=CANONICAL_DPI,
    facecolor="white",
    bbox_inches="tight",
)


def px_to_pt(px: float) -> float:
    """Convert pixels to matplotlib points using the canonical render scale."""

    return px * 72 / CANONICAL_DPI


def px_to_data(px: float) -> float:
    """Convert pixels to data units using the canonical pixels-per-unit scale."""

    return px / PX_PER_DATA_UNIT


def ensure_parent_dir(path: Path | str) -> Path:
    """Create the parent directory for a target path and return the Path."""

    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    return output_path


def save_figure(fig: plt.Figure, output_path: Path | str, **savefig_kw) -> None:
    """Save a figure with the shared export defaults."""

    path = ensure_parent_dir(output_path)
    kwargs = dict(DEFAULT_SAVEFIG_KW)
    kwargs.update(savefig_kw)
    fig.savefig(path, **kwargs)


def make_ct_signal_figure(xlim: tuple[float, float], ylim: tuple[float, float]):
    """Create a figure whose pixel size tracks the requested data limits."""

    x_range = float(xlim[1] - xlim[0])
    y_range = float(ylim[1] - ylim[0])

    axes_w_px = x_range * PX_PER_DATA_UNIT
    axes_h_px = y_range * PX_PER_DATA_UNIT
    fig_w_px = MARGIN_LEFT_PX + axes_w_px + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_BOTTOM_PX + axes_h_px + MARGIN_TOP_PX

    fig, ax = plt.subplots(
        figsize=(fig_w_px / CANONICAL_DPI, fig_h_px / CANONICAL_DPI),
        dpi=CANONICAL_DPI,
        facecolor="white",
        constrained_layout=True,
    )

    return fig, ax


def math_label(value) -> str:
    """Return a math-text label for numeric tick values or pass through text."""

    if isinstance(value, str):
        return value

    if np.isscalar(value):
        numeric = float(value)
        rounded = int(np.rint(numeric))
        if np.isclose(numeric, rounded):
            return rf"${rounded}$"
        return rf"${numeric:g}$"

    raise TypeError(f"Unsupported label value: {value!r}")


def setup_ct_signal_axes(
    ax,
    *,
    xlim: tuple[float, float],
    ylim: tuple[float, float],
    xticks,
    yticks,
    x_axis_label: str = r"$t$",
    y_axis_label: str = r"$x(t)$",
    show_grid: bool = True,
    show_origin: bool = True,
    y_tick_label_side: str = "left",
    x_minor_grid_step: float = 1,
    y_minor_grid_step: float = 1,
    equal_aspect: bool = True,
):
    """Apply the shared continuous-time signal axes treatment."""

    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)

    if equal_aspect:
        ax.set_aspect("equal", adjustable="box")

    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(x_minor_grid_step))
    ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(y_minor_grid_step))

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

    for tick in xticks:
        if np.isclose(tick, 0):
            continue

        ax.plot(
            [tick, tick],
            [-TICK_HALF_LEN, TICK_HALF_LEN],
            color=AXIS_COLOR,
            lw=TICK_LW,
            zorder=5,
        )
        ax.text(
            tick,
            X_TICK_LABEL_Y,
            math_label(tick),
            fontsize=TICK_LABEL_SIZE,
            ha="center",
            va="top",
            color=TICK_LABEL_COLOR,
            zorder=6,
        )

    for tick in yticks:
        if np.isclose(tick, 0):
            continue

        ax.plot(
            [-TICK_HALF_LEN, TICK_HALF_LEN],
            [tick, tick],
            color=AXIS_COLOR,
            lw=TICK_LW,
            zorder=5,
        )

        if y_tick_label_side == "right":
            label_x = Y_TICK_LABEL_X
            label_ha = "left"
        else:
            label_x = -Y_TICK_LABEL_X
            label_ha = "right"

        ax.text(
            label_x,
            tick,
            math_label(tick),
            fontsize=TICK_LABEL_SIZE,
            ha=label_ha,
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

    return ax


def plot_signal(ax, t, x, *, lw: float = SIGNAL_LW, color: str = SIGNAL_COLOR, zorder: int = 4):
    """Plot a connected piecewise continuous-time signal."""

    ax.plot(
        t,
        x,
        color=color,
        linewidth=lw,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=zorder,
    )


def plot_smooth_signal(
    ax,
    t,
    x,
    *,
    lw: float = SMOOTH_SIGNAL_LW,
    color: str = SIGNAL_COLOR,
    zorder: int = 4,
):
    """Plot a smooth continuous-time curve."""

    ax.plot(
        t,
        x,
        color=color,
        linewidth=lw,
        solid_capstyle="round",
        zorder=zorder,
    )


def draw_open_endpoint(ax, t0: float, x0: float):
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


def draw_closed_endpoint(ax, t0: float, x0: float):
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


def draw_horizontal_bracket(
    ax,
    x_start: float,
    x_end: float,
    y: float,
    *,
    label: str | None = None,
    label_gap: float = BRACKET_LABEL_GAP,
    cap_half_len: float = BRACKET_CAP_HALF_LEN,
    color: str = ANNOTATION_COLOR,
    linewidth: float = ANNOTATION_LW,
    fontsize: float = ANNOTATION_SIZE,
    zorder: int = 5,
):
    """Draw a horizontal measurement bracket, optionally with a label."""

    ax.plot([x_start, x_end], [y, y], color=color, linewidth=linewidth, zorder=zorder)
    ax.plot(
        [x_start, x_start],
        [y - cap_half_len, y + cap_half_len],
        color=color,
        linewidth=linewidth,
        zorder=zorder,
    )
    ax.plot(
        [x_end, x_end],
        [y - cap_half_len, y + cap_half_len],
        color=color,
        linewidth=linewidth,
        zorder=zorder,
    )

    if label is not None:
        ax.text(
            (x_start + x_end) / 2,
            y - label_gap,
            label,
            fontsize=fontsize,
            ha="center",
            va="top",
            color=color,
        )


def draw_vertical_bracket(
    ax,
    x: float,
    y_start: float,
    y_end: float,
    *,
    label: str | None = None,
    label_gap: float = BRACKET_LABEL_GAP,
    cap_half_len: float = BRACKET_CAP_HALF_LEN,
    color: str = ANNOTATION_COLOR,
    linewidth: float = ANNOTATION_LW,
    fontsize: float = ANNOTATION_SIZE,
    zorder: int = 5,
):
    """Draw a vertical measurement bracket, optionally with a label."""

    ax.plot([x, x], [y_start, y_end], color=color, linewidth=linewidth, zorder=zorder)
    ax.plot(
        [x - cap_half_len, x + cap_half_len],
        [y_start, y_start],
        color=color,
        linewidth=linewidth,
        zorder=zorder,
    )
    ax.plot(
        [x - cap_half_len, x + cap_half_len],
        [y_end, y_end],
        color=color,
        linewidth=linewidth,
        zorder=zorder,
    )

    if label is not None:
        ax.text(
            x + label_gap,
            (y_start + y_end) / 2,
            label,
            fontsize=fontsize,
            ha="left",
            va="center",
            color=color,
        )


def draw_reference_line(ax, x_values, y_values):
    """Draw a dotted reference line for offsets, maxima, minima, or baselines."""

    ax.plot(
        x_values,
        y_values,
        color=GUIDE_COLOR,
        linewidth=GUIDE_LW,
        linestyle=(0, (1.1, 2.4)),
        zorder=3,
    )


def signal_plot_defaults() -> dict:
    """Return the standard line style used for connected signal traces."""

    return {
        "color": SIGNAL_COLOR,
        "linewidth": SIGNAL_LW,
        "solid_capstyle": "butt",
        "solid_joinstyle": "miter",
        "zorder": 4,
    }


def smooth_signal_plot_defaults() -> dict:
    """Return the standard line style used for smooth curves."""

    return {
        "color": SIGNAL_COLOR,
        "linewidth": SMOOTH_SIGNAL_LW,
        "solid_capstyle": "round",
        "zorder": 4,
    }

