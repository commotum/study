"""Render the phasor real-axis projection diagram for lesson l004-s001."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np


BACKGROUND_COLOR = "white"
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

MARGIN_LEFT_PX = 115
MARGIN_RIGHT_PX = 120
MARGIN_BOTTOM_PX = 95
MARGIN_TOP_PX = 110


def px_to_pt(px):
    return px * 72 / CANONICAL_DPI


def px_to_data(px):
    return px / PX_PER_DATA_UNIT


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

AXIS_ARROW_SHAFT_WIDTH_DATA = px_to_data(4.3)
VECTOR_ARROW_SHAFT_WIDTH_DATA = px_to_data(4.0)

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


def configure_matplotlib():
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


def make_phasor_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
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


def math_label(value):
    if isinstance(value, str):
        return value
    numeric = float(value)
    rounded = round(numeric)
    if abs(numeric - rounded) < 1e-9:
        return rf"${int(rounded)}$"
    return rf"${numeric:g}$"


def _coerce_tick_labels(ticks, labels):
    if labels is None:
        return [math_label(tick) for tick in ticks]
    labels = list(labels)
    if len(labels) != len(ticks):
        raise ValueError("tick label count must match tick count")
    return labels


def _draw_centered_tick(ax, value, *, axis="x"):
    if axis == "x":
        ax.plot([value, value], [-TICK_HALF_LEN, TICK_HALF_LEN],
                color=AXIS_COLOR, lw=TICK_LW, zorder=5)
    elif axis == "y":
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [value, value],
                color=AXIS_COLOR, lw=TICK_LW, zorder=5)
    else:
        raise ValueError("axis must be 'x' or 'y'")


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
    x_minor_grid_step=0.5,
    y_minor_grid_step=0.5,
    equal_aspect=True,
):
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

    x_labels = _coerce_tick_labels(xticks, x_tick_labels)
    y_labels = _coerce_tick_labels(yticks, y_tick_labels)

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

    ax.text(x_axis_end + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, x_axis_label,
            fontsize=AXIS_LABEL_SIZE,
            ha="left", va="center",
            color=LABEL_COLOR,
            clip_on=False)

    ax.text(0, y_axis_end + Y_AXIS_LABEL_Y_PAD, y_axis_label,
            fontsize=TOP_LABEL_SIZE,
            ha="center", va="bottom",
            color=LABEL_COLOR,
            clip_on=False)


def draw_dotted_guide(ax, x_values, y_values):
    ax.plot(
        x_values,
        y_values,
        color=GUIDE_COLOR,
        linewidth=GUIDE_LW,
        linestyle=(0, (1.1, 2.4)),
        zorder=3,
    )


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
):
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
        headwidth=4.2,
        headlength=5.5,
        headaxislength=4.3,
        color=color,
        pivot="tail",
        clip_on=False,
        zorder=zorder,
    )
    return x0 + dx, y0 + dy


def circle_points(radius, center, theta_start, theta_end, num=96):
    theta = np.linspace(theta_start, theta_end, num)
    center = np.asarray(center, dtype=float)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    return x, y, theta


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
    x, y, _ = circle_points(radius, center, theta_start, theta_end)
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


def save_figure(fig, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        output_path,
        dpi=CANONICAL_DPI,
        bbox_inches="tight",
        facecolor=BACKGROUND_COLOR,
    )
    plt.close(fig)


def main():
    output_path = Path(
        "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/2.2--phasors-and-sinusoids-Images/images/l004-s001-te-section-001.png"
    )

    xlim = (-0.7, 3.35)
    ylim = (-0.7, 2.85)
    fig, ax = make_phasor_figure(xlim, ylim)

    setup_phasor_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=[1, 2, 3],
        yticks=[1, 2],
        x_axis_label=r"$\Re\{X\}$",
        y_axis_label=r"$\Im\{X\}$",
        show_grid=True,
        show_origin=True,
        x_minor_grid_step=0.5,
        y_minor_grid_step=0.5,
        equal_aspect=True,
    )

    amplitude = 2.55
    theta = np.deg2rad(55.0)
    x_tip = amplitude * np.cos(theta)
    y_tip = amplitude * np.sin(theta)

    draw_dotted_guide(ax, [x_tip, x_tip], [0, y_tip])
    draw_dotted_guide(ax, [0, x_tip], [0, 0])

    draw_vector_arrow(ax, 0, 0, x_tip, y_tip, color=SIGNAL_COLOR, zorder=4)

    draw_phase_arc(
        ax,
        0,
        theta,
        radius=0.62,
        center=(0.0, 0.0),
        color=ANNOTATION_COLOR,
        lw=ANNOTATION_LW,
        zorder=5,
        label=r"$\theta(t)$",
        label_radius=0.82,
        arrow=True,
    )

    mid_x = 0.56 * x_tip
    mid_y = 0.56 * y_tip
    normal_x = -np.sin(theta)
    normal_y = np.cos(theta)
    ax.text(
        mid_x + 0.11 * normal_x,
        mid_y + 0.11 * normal_y,
        r"$A$",
        fontsize=ANNOTATION_SIZE,
        ha="center",
        va="center",
        color=LABEL_COLOR,
        zorder=6,
    )

    ax.text(
        x_tip * 0.58,
        0.10,
        r"$A\,\cos\theta(t)$",
        fontsize=ANNOTATION_SIZE,
        ha="center",
        va="bottom",
        color=LABEL_COLOR,
        zorder=6,
    )

    save_figure(fig, output_path)


if __name__ == "__main__":
    main()
