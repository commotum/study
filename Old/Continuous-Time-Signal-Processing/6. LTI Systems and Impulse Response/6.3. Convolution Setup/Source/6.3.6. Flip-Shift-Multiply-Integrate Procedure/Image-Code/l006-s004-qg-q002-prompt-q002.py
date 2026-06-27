"""Shared matplotlib boilerplate for CTS continuous-time signal figures.

This module centralizes the signal-plot styling used across
EE01-M06-03, Convolution Setup. Later topic workers can copy or adapt these
helpers without re-reading the full style guide.

Only matplotlib and NumPy are used here.
"""

from __future__ import annotations

import matplotlib
matplotlib.use("Agg")

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator


BACKGROUND_COLOR = "white"


COURSE_NAME = "Continuous Time Signal Processing"
COURSE_CODE = "CTS"
COURSE_ID = "EE01"
UNIT_NUMBER = 6
UNIT_NAME = "Unit 6"
MODULE_ID = "EE01-M06-03"
MODULE_NUMBER = "6.3"
MODULE_NAME = "Convolution Setup"

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


def configure_matplotlib():
    """Apply the shared serif and white-background defaults."""

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


def new_ct_figure(*, figsize=None, dpi=CANONICAL_DPI):
    """Create a generic CTS figure with the shared background and layout."""

    return plt.subplots(
        figsize=figsize,
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=True,
    )


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

    # Draw axes through the origin with arrowheads only on positive ends.
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
    gridspec = fig.add_gridspec(len(panel_ylims), 1, height_ratios=[ylim[1] - ylim[0] for ylim in panel_ylims])
    axes = [fig.add_subplot(gridspec[i, 0]) for i in range(len(panel_ylims))]
    return fig, axes


def save_figure(fig, output_path):
    """Save a figure to disk with the shared export settings."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=CANONICAL_DPI, bbox_inches="tight", facecolor=BACKGROUND_COLOR)
    plt.close(fig)



def _ax_text(ax, item):
    ax.text(
        item["x"],
        item["y"],
        item["text"],
        fontsize=item.get("fontsize", ANNOTATION_SIZE),
        ha=item.get("ha", "center"),
        va=item.get("va", "center"),
        color=item.get("color", ANNOTATION_COLOR),
        rotation=item.get("rotation", 0),
        zorder=item.get("zorder", 8),
        clip_on=item.get("clip_on", False),
    )


def _fig_text(fig, item):
    fig.text(
        item["x"],
        item["y"],
        item["text"],
        fontsize=item.get("fontsize", ANNOTATION_SIZE),
        ha=item.get("ha", "center"),
        va=item.get("va", "center"),
        color=item.get("color", ANNOTATION_COLOR),
        rotation=item.get("rotation", 0),
        zorder=item.get("zorder", 8),
    )


def _fig_arrow(fig, arrow):
    fig.axes[0].annotate(
        "",
        xy=(arrow["x2"], arrow["y2"]),
        xytext=(arrow["x1"], arrow["y1"]),
        xycoords="figure fraction",
        textcoords="figure fraction",
        arrowprops=dict(
            arrowstyle=arrow.get("arrowstyle", "->"),
            color=arrow.get("color", ANNOTATION_COLOR),
            lw=arrow.get("lw", 2.2),
            shrinkA=0,
            shrinkB=0,
        ),
        zorder=arrow.get("zorder", 8),
    )


def _auto_bounds(segments, xticks, *, x_pad=0.85, y_pad=0.7, top_pad=0.0, bottom_pad=0.0):
    xs = [0.0]
    ys = [0.0]
    for start, end, height, _, _ in segments:
        xs.extend([float(start), float(end)])
        ys.append(float(height))
    xs.extend(float(x) for x in xticks)
    xmin = min(xs) - x_pad
    xmax = max(xs) + x_pad
    ymin = min(ys) - y_pad - bottom_pad
    ymax = max(ys) + y_pad + top_pad
    return (xmin, xmax), (ymin, ymax)


def _make_panel(
    segments,
    *,
    y_label,
    xticks,
    yticks,
    x_axis_label=r"$\tau$",
    xlim=None,
    ylim=None,
    show_grid=True,
    show_origin=True,
    show_x_tick_labels=True,
    show_y_tick_labels=True,
    y_tick_label_side="left",
    equal_aspect=True,
    x_pad=0.85,
    y_pad=0.7,
    top_pad=0.0,
    bottom_pad=0.0,
    baseline=0.0,
    reflection_axis=None,
    shade_regions=None,
    support_brackets=None,
    vertical_lines=None,
    horizontal_lines=None,
    texts=None,
):
    if xlim is None or ylim is None:
        xlim, ylim = _auto_bounds(
            segments,
            xticks,
            x_pad=x_pad,
            y_pad=y_pad,
            top_pad=top_pad,
            bottom_pad=bottom_pad,
        )
    return {
        "segments": segments,
        "xlim": xlim,
        "ylim": ylim,
        "xticks": xticks,
        "yticks": yticks,
        "x_axis_label": x_axis_label,
        "y_label": y_label,
        "show_grid": show_grid,
        "show_origin": show_origin,
        "show_x_tick_labels": show_x_tick_labels,
        "show_y_tick_labels": show_y_tick_labels,
        "y_tick_label_side": y_tick_label_side,
        "equal_aspect": equal_aspect,
        "baseline": baseline,
        "reflection_axis": reflection_axis,
        "shade_regions": shade_regions or [],
        "support_brackets": support_brackets or [],
        "vertical_lines": vertical_lines or [],
        "horizontal_lines": horizontal_lines or [],
        "texts": texts or [],
    }


def _render_panel(ax, panel):
    setup_ct_signal_axes(
        ax,
        xlim=tuple(panel["xlim"]),
        ylim=tuple(panel["ylim"]),
        xticks=panel["xticks"],
        yticks=panel["yticks"],
        x_axis_label=panel.get("x_axis_label", r"$\tau$"),
        y_axis_label=panel.get("y_label", r"$x(\tau)$"),
        show_grid=panel.get("show_grid", True),
        show_origin=panel.get("show_origin", True),
        y_tick_label_side=panel.get("y_tick_label_side", "left"),
        show_x_tick_labels=panel.get("show_x_tick_labels", True),
        show_y_tick_labels=panel.get("show_y_tick_labels", True),
        x_minor_grid_step=1,
        y_minor_grid_step=1,
        equal_aspect=panel.get("equal_aspect", True),
    )

    for span in panel.get("shade_regions", []):
        shade_region(
            ax,
            span["x_left"],
            span["x_right"],
            alpha=span.get("alpha", 0.08),
            color=span.get("color", SIGNAL_COLOR),
            zorder=span.get("zorder", 0),
        )

    if panel.get("reflection_axis") is not None:
        draw_vertical_marker_line(
            ax,
            panel["reflection_axis"],
            panel["ylim"][0],
            panel["ylim"][1],
            color=panel.get("reflection_color", GUIDE_COLOR),
            linestyle=panel.get("reflection_linestyle", (0, (4.0, 4.0))),
            lw=panel.get("reflection_lw", GUIDE_LW),
            zorder=panel.get("reflection_zorder", 3),
        )

    for line in panel.get("vertical_lines", []):
        draw_vertical_marker_line(
            ax,
            line["x"],
            line["y0"],
            line["y1"],
            color=line.get("color", GUIDE_COLOR),
            linestyle=line.get("linestyle", (0, (1.1, 2.4))),
            lw=line.get("lw", GUIDE_LW),
            zorder=line.get("zorder", 3),
        )

    for line in panel.get("horizontal_lines", []):
        draw_horizontal_marker_line(
            ax,
            line["y"],
            line["x0"],
            line["x1"],
            color=line.get("color", GUIDE_COLOR),
            linestyle=line.get("linestyle", (0, (1.1, 2.4))),
            lw=line.get("lw", GUIDE_LW),
            zorder=line.get("zorder", 3),
        )

    if panel.get("segments"):
        draw_piecewise_constant_signal(
            ax,
            panel["segments"],
            xlim=tuple(panel["xlim"]),
            baseline=panel.get("baseline", 0.0),
            color=panel.get("signal_color", SIGNAL_COLOR),
            lw=panel.get("signal_lw", SIGNAL_LW),
            zorder=panel.get("signal_zorder", 4),
        )

    for bracket in panel.get("support_brackets", []):
        draw_support_bracket(
            ax,
            bracket["start"],
            bracket["end"],
            y=bracket.get("y", -0.38),
            label=bracket.get("label"),
            color=bracket.get("color", ANNOTATION_COLOR),
        )

    for item in panel.get("texts", []):
        _ax_text(ax, item)


def render(spec):
    if spec["kind"] == "stacked":
        fig, axes = make_stacked_ct_signal_figure(
            tuple(spec["xlim"]),
            [tuple(panel["ylim"]) for panel in spec["panels"]],
            gap_px=spec.get("gap_px", 38),
        )
        for ax, panel in zip(axes, spec["panels"]):
            _render_panel(ax, panel)
    else:
        fig, ax = make_ct_signal_figure(tuple(spec["panel"]["xlim"]), tuple(spec["panel"]["ylim"]))
        _render_panel(ax, spec["panel"])

    for item in spec.get("fig_texts", []):
        _fig_text(fig, item)

    for arrow in spec.get("fig_arrows", []):
        _fig_arrow(fig, arrow)

    save_figure(fig, Path(spec["image_output_path"]))

SPEC = {'kind': 'stacked',
 'image_output_path': '/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/6.3--convolution-setup-Images/images/l006-s004-qg-q002-prompt-q002.png',
 'xlim': (-1.85, 4.85),
 'panel_ylims': [(-0.7, 2.7), (-1.7, 0.7)],
 'panels': [{'segments': [(-1, 2, 2, True, True)],
             'xlim': (-1.85, 4.85),
             'ylim': (-0.7, 2.7),
             'xticks': [-1, 0, 2, 4],
             'yticks': [2],
             'x_axis_label': None,
             'y_label': '$x(\\tau)$',
             'show_grid': True,
             'show_origin': False,
             'show_x_tick_labels': False,
             'show_y_tick_labels': True,
             'y_tick_label_side': 'left',
             'equal_aspect': True,
             'baseline': 0.0,
             'reflection_axis': None,
             'shade_regions': [{'x_left': 0, 'x_right': 2, 'alpha': 0.08}],
             'support_brackets': [],
             'vertical_lines': [],
             'horizontal_lines': [],
             'texts': []},
            {'segments': [(0, 4, -1, True, True)],
             'xlim': (-1.85, 4.85),
             'ylim': (-1.7, 0.7),
             'xticks': [-1, 0, 2, 4],
             'yticks': [-1],
             'x_axis_label': '$\\tau$',
             'y_label': '$h(3-\\tau)$',
             'show_grid': True,
             'show_origin': True,
             'show_x_tick_labels': True,
             'show_y_tick_labels': True,
             'y_tick_label_side': 'left',
             'equal_aspect': True,
             'baseline': 0.0,
             'reflection_axis': None,
             'shade_regions': [{'x_left': 0, 'x_right': 2, 'alpha': 0.08}],
             'support_brackets': [],
             'vertical_lines': [],
             'horizontal_lines': [],
             'texts': []}],
 'gap_px': 46,
 'fig_texts': [],
 'fig_arrows': []}

if __name__ == "__main__":
    render(SPEC)
