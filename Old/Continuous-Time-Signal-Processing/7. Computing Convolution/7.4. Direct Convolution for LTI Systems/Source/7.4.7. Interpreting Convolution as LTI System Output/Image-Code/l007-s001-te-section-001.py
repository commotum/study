from __future__ import annotations

from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.ticker import MultipleLocator

plt.rcParams.update(
    {
        "mathtext.fontset": "cm",
        "font.family": "serif",
    }
)

CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150


def px_to_pt(px: float) -> float:
    return px * 72 / CANONICAL_DPI


def px_to_data(px: float) -> float:
    return px / PX_PER_DATA_UNIT


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
ANNOTATION_LW = px_to_pt(2.9)
TICK_HALF_LEN = px_to_data(8.25)
X_TICK_LABEL_Y = -px_to_data(24)
Y_TICK_LABEL_X = px_to_data(18)
ORIGIN_LABEL_X = px_to_data(9)
ORIGIN_LABEL_Y = -px_to_data(12)
X_AXIS_LABEL_X_PAD = px_to_data(15)
X_AXIS_LABEL_Y = -px_to_data(4.5)
Y_AXIS_LABEL_Y_PAD = px_to_data(18)

TICK_LABEL_SIZE = px_to_pt(35.6)
AXIS_LABEL_SIZE = px_to_pt(53.3)
TOP_LABEL_SIZE = px_to_pt(57.8)
ANNOTATION_SIZE = px_to_pt(33.3)

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


def math_label(value: float | str) -> str:
    if isinstance(value, str):
        return value
    if abs(float(value) - int(value)) < 1e-9:
        return rf"${int(value)}$"
    return rf"${value:g}$"


def make_ct_signal_figure(xlim: tuple[float, float], ylim: tuple[float, float]):
    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]
    fig_w_px = 115 + x_range * PX_PER_DATA_UNIT + 120
    fig_h_px = 95 + y_range * PX_PER_DATA_UNIT + 110
    return plt.subplots(
        figsize=(fig_w_px / CANONICAL_DPI, fig_h_px / CANONICAL_DPI),
        dpi=CANONICAL_DPI,
        facecolor="white",
        constrained_layout=True,
    )


def setup_ct_signal_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_axis_label: str = r"$t$",
    y_axis_label: str = r"$x(t)$",
    show_grid: bool = True,
    y_tick_label_side: str = "left",
    x_minor_grid_step: float = 1,
    y_minor_grid_step: float = 1,
    equal_aspect: bool = True,
) -> None:
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

    ax.quiver(
        xlim[0],
        0,
        xlim[1] - xlim[0],
        0,
        **AXIS_ARROW_KW,
    )
    ax.quiver(
        0,
        ylim[0],
        0,
        ylim[1] - ylim[0],
        **AXIS_ARROW_KW,
    )

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
        ax.plot(
            [-TICK_HALF_LEN, TICK_HALF_LEN],
            [y, y],
            color=AXIS_COLOR,
            lw=TICK_LW,
            zorder=5,
        )
        x_txt = -Y_TICK_LABEL_X if y_tick_label_side == "left" else Y_TICK_LABEL_X
        ha = "right" if y_tick_label_side == "left" else "left"
        ax.text(
            x_txt,
            y,
            math_label(y),
            fontsize=TICK_LABEL_SIZE,
            ha=ha,
            va="center",
            color=TICK_LABEL_COLOR,
            zorder=6,
        )

    ax.text(
        xlim[1] + X_AXIS_LABEL_X_PAD,
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
        ylim[1] + Y_AXIS_LABEL_Y_PAD,
        y_axis_label,
        fontsize=TOP_LABEL_SIZE,
        ha="center",
        va="bottom",
        color=LABEL_COLOR,
        clip_on=False,
    )
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


def plot_signal(ax, t, x, *, lw=SIGNAL_LW):
    ax.plot(t, x, color=SIGNAL_COLOR, linewidth=lw, solid_capstyle="butt", solid_joinstyle="miter", zorder=4)


def plot_block(ax):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    ax.annotate(
        "",
        xy=(2.0, 5.0),
        xytext=(0.45, 5.0),
        arrowprops=dict(arrowstyle="->", color=AXIS_COLOR, lw=AXIS_LW),
    )
    ax.text(1.0, 5.35, r"$x(t)$", fontsize=TICK_LABEL_SIZE * 0.9, color=AXIS_COLOR)

    block = Rectangle((4.2, 3.4), 2.0, 3.2, facecolor="white", edgecolor=AXIS_COLOR, lw=AXIS_LW)
    ax.add_patch(block)
    ax.text(5.2, 5.0, r"$h(t)$", fontsize=TOP_LABEL_SIZE * 0.45, ha="center", va="center", color=AXIS_COLOR)

    ax.annotate(
        "",
        xy=(6.75, 5.0),
        xytext=(8.0, 5.0),
        arrowprops=dict(arrowstyle="->", color=AXIS_COLOR, lw=AXIS_LW),
    )
    ax.text(7.55, 5.35, r"$y(t)=(x*h)(t)$", fontsize=TICK_LABEL_SIZE * 0.85, color=AXIS_COLOR)


def draw_tiny_axis(fig, rect, title, t, y, xlim, ylim, xticks):
    ax = fig.add_axes(rect)
    setup_ct_signal_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=xticks,
        yticks=[0, 1],
        x_axis_label=r"$t$",
        y_axis_label=title,
        show_grid=True,
        x_minor_grid_step=1,
        y_minor_grid_step=1,
        equal_aspect=False,
    )
    plot_signal(ax, t, y)
    ax.text((xlim[0] + xlim[1]) / 2, ylim[1] + 0.38, title, fontsize=ANNOTATION_SIZE, ha="center", va="bottom", color=ANNOTATION_COLOR)


fig = plt.figure(
    figsize=(13, 8),
    dpi=CANONICAL_DPI,
    facecolor="white",
    constrained_layout=True,
)

ax_block = fig.add_axes((0.08, 0.55, 0.84, 0.33))
plot_block(ax_block)

# Aligned time-axis sketches.
draw_tiny_axis(
    fig,
    (0.11, 0.22, 0.24, 0.24),
    r"$x(t)$",
    np.array([-1.0, 0.0, 0.0, 2.0, 2.0, 3.0]),
    np.array([0.0, 0.0, 1.0, 1.0, 0.0, 0.0]),
    xlim=(-1.0, 3.0),
    ylim=(-0.6, 1.6),
    xticks=[-1.0, 0.0, 1.0, 2.0],
)

draw_tiny_axis(
    fig,
    (0.38, 0.22, 0.24, 0.24),
    r"$h(t)$",
    np.array([-0.5, 0.0, 0.0, 1.5, 1.5, 2.0]),
    np.array([0.0, 0.0, 1.0, 1.0, 0.0, 0.0]),
    xlim=(-1.0, 3.0),
    ylim=(-0.6, 1.6),
    xticks=[-1.0, 0.0, 1.0, 2.0],
)

draw_tiny_axis(
    fig,
    (0.65, 0.22, 0.24, 0.24),
    r"$y(t)$",
    np.array([-1.0, -1.0, -0.5, 1.0, 1.5, 2.0]),
    np.array([0.0, 0.0, 1.2, 0.4, 0.0, 0.0]),
    xlim=(-1.0, 2.5),
    ylim=(-0.6, 1.6),
    xticks=[-1.0, 0.0, 1.0, 2.0],
)

output_path = Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/7.4--direct-convolution-for-lti-systems-Images/images/l007-s001-te-section-001.png')
output_path.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(output_path, dpi=CANONICAL_DPI, bbox_inches='tight', facecolor='white')
