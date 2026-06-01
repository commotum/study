"""Generated matplotlib figure for l006-s006-qg-q001-prompt-q001."""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

BACKGROUND_COLOR = "white"
CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150
MARGIN_LEFT_PX = 115
MARGIN_RIGHT_PX = 120
MARGIN_BOTTOM_PX = 95
MARGIN_TOP_PX = 110


def px_to_pt(px):
    return px * 72 / CANONICAL_DPI


def px_to_data(px):
    return px / PX_PER_DATA_UNIT


SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"

SIGNAL_LW = px_to_pt(7.1)
AXIS_LW = px_to_pt(4.3)
TICK_LW = px_to_pt(2.7)
GRID_LW = px_to_pt(1.3)
PEAK_MARKER_SIZE = px_to_pt(13.3)
TICK_LABEL_SIZE = px_to_pt(35.6)
AXIS_LABEL_SIZE = px_to_pt(53.3)
TOP_LABEL_SIZE = px_to_pt(57.8)

TICK_HALF_LEN = px_to_data(8.25)
X_TICK_LABEL_Y = -px_to_data(24)
Y_TICK_LABEL_X = px_to_data(18)
ORIGIN_LABEL_X = px_to_data(9)
ORIGIN_LABEL_Y = -px_to_data(12)
X_AXIS_LABEL_X_PAD = px_to_data(15)
X_AXIS_LABEL_Y = -px_to_data(4.5)
Y_AXIS_LABEL_Y_PAD = px_to_data(18)
AXIS_ARROW_SHAFT_WIDTH_DATA = px_to_data(4.3)
GRID_ALPHA = 0.18

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


def make_ct_signal_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
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


def make_horizontal_panels_figure(panel_xlims, ylim, *, gap_px=30, dpi=CANONICAL_DPI):
    x_ranges = [xlim[1] - xlim[0] for xlim in panel_xlims]
    y_range = ylim[1] - ylim[0]

    axes_w_px = sum(x_ranges) * PX_PER_DATA_UNIT
    axes_h_px = y_range * PX_PER_DATA_UNIT
    fig_w_px = MARGIN_LEFT_PX + axes_w_px + MARGIN_RIGHT_PX + gap_px * (len(panel_xlims) - 1)
    fig_h_px = MARGIN_BOTTOM_PX + axes_h_px + MARGIN_TOP_PX

    fig = plt.figure(
        figsize=(fig_w_px / dpi, fig_h_px / dpi),
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=True,
    )
    gridspec = fig.add_gridspec(1, len(panel_xlims), width_ratios=x_ranges)
    axes = [fig.add_subplot(gridspec[0, i]) for i in range(len(panel_xlims))]
    return fig, axes


def save_figure(fig, output_path, *, dpi=CANONICAL_DPI):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=dpi, facecolor=BACKGROUND_COLOR, bbox_inches="tight")
    plt.close(fig)


def math_label(value):
    if isinstance(value, str):
        return value
    numeric = float(value)
    rounded = round(numeric)
    if np.isclose(numeric, rounded):
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
    x_minor_grid_step=1,
    y_minor_grid_step=1,
    equal_aspect=True,
):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)

    if equal_aspect:
        ax.set_aspect("equal", adjustable="box")

    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.xaxis.set_minor_locator(MultipleLocator(x_minor_grid_step))
    ax.yaxis.set_minor_locator(MultipleLocator(y_minor_grid_step))

    if show_grid:
        ax.grid(True, which="both", linewidth=GRID_LW, alpha=GRID_ALPHA, color=GRID_COLOR)
        ax.set_axisbelow(True)

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    x_axis_start, x_axis_end = xlim
    y_axis_start, y_axis_end = ylim

    ax.quiver(x_axis_start, 0, x_axis_end - x_axis_start, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y_axis_start, 0, y_axis_end - y_axis_start, **AXIS_ARROW_KW)

    for t in xticks:
        if abs(t) < 1e-12:
            continue
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
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


def plot_signal(ax, t, x, *, lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    ax.plot(
        t,
        x,
        color=color,
        linewidth=lw,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=zorder,
    )


def draw_peak_marker(ax, t0, x0, *, color=SIGNAL_COLOR, zorder=6):
    ax.plot(
        t0,
        x0,
        marker="o",
        markersize=PEAK_MARKER_SIZE,
        markerfacecolor=color,
        markeredgecolor=color,
        linestyle="None",
        zorder=zorder,
    )


def draw_pulse(ax, start, peak, end, *, height=1.0, color=SIGNAL_COLOR, zorder=4):
    plot_signal(ax, [start, peak, end], [0.0, height, 0.0], lw=SIGNAL_LW, color=color, zorder=zorder)
    draw_peak_marker(ax, peak, height, color=color, zorder=zorder + 2)


def render_panel_pulse_figure(
    output_path,
    panel_specs,
    *,
    ylim=(-0.25, 1.25),
    gap_px=30,
    show_grid=True,
):
    if len(panel_specs) == 1:
        fig, ax = make_ct_signal_figure(panel_specs[0]["xlim"], ylim)
        axes = [ax]
    else:
        fig, axes = make_horizontal_panels_figure([spec["xlim"] for spec in panel_specs], ylim, gap_px=gap_px)

    for ax, spec in zip(axes, panel_specs):
        setup_ct_signal_axes(
            ax,
            xlim=spec["xlim"],
            ylim=ylim,
            xticks=spec["xticks"],
            yticks=spec.get("yticks", [1]),
            x_axis_label=spec.get("x_axis_label", r"$t$"),
            y_axis_label=spec.get("signal_label", r"$x(t)$"),
            show_grid=show_grid,
            show_origin=spec.get("show_origin", True),
            y_tick_label_side=spec.get("y_tick_label_side", "left"),
        )
        pulse = spec["pulse"]
        draw_pulse(
            ax,
            pulse["start"],
            pulse["peak"],
            pulse["end"],
            height=pulse.get("height", 1.0),
        )

    save_figure(fig, output_path)

OUTPUT_PATH = Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/3.3--time-reversal-and-combined-operations-Images/images/l006-s006-qg-q001-prompt-q001.png')

def main():
    panel_specs = [{'xlim': (0, 12), 'xticks': [0, 6, 12], 'signal_label': '$x(t)$', 'pulse': {'start': 0, 'peak': 6, 'end': 12}}]
    render_panel_pulse_figure(OUTPUT_PATH, panel_specs)

if __name__ == '__main__':
    main()
