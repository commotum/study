from __future__ import annotations

from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.rcParams.update({"mathtext.fontset": "cm", "font.family": "serif"})

CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150

def px_to_pt(px: float) -> float:
    return px * 72 / CANONICAL_DPI

def px_to_data(px: float) -> float:
    return px / PX_PER_DATA_UNIT

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
TICK_LW = px_to_pt(2.7)
GRID_LW = px_to_pt(1.3)
SIGNAL_LW = px_to_pt(7.1)
ANNOTATION_LW = px_to_pt(2.9)
TICK_LABEL_SIZE = px_to_pt(35.6)
AXIS_LABEL_SIZE = px_to_pt(53.3)
TOP_LABEL_SIZE = px_to_pt(57.8)
ANNOTATION_SIZE = px_to_pt(33.3)
TICK_HALF_LEN = px_to_data(8.25)
X_AXIS_LABEL_X_PAD = px_to_data(15)
X_AXIS_LABEL_Y = -px_to_data(4.5)
X_TICK_LABEL_Y = -px_to_data(24)
Y_TICK_LABEL_X = px_to_data(18)
ORIGIN_LABEL_X = px_to_data(9)
ORIGIN_LABEL_Y = -px_to_data(12)
Y_AXIS_LABEL_Y_PAD = px_to_data(18)

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

def make_ct_signal_figure(xlim, ylim):
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

def setup_ct_signal_axes(ax, *, xlim, ylim, xticks, yticks, x_axis_label=r"$t$", y_axis_label=r"$y(t)$", show_grid=True, y_tick_label_side="left", x_minor_grid_step=1, y_minor_grid_step=1, equal_aspect=True):
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

    ax.quiver(xlim[0], 0, xlim[1] - xlim[0], 0, **AXIS_ARROW_KW)
    ax.quiver(0, ylim[0], 0, ylim[1] - ylim[0], **AXIS_ARROW_KW)

    for t in xticks:
        if abs(t) < 1e-12:
            continue
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(t, X_TICK_LABEL_Y, math_label(t), fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR)
    for y in yticks:
        if abs(y) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        x_txt = Y_TICK_LABEL_X if y_tick_label_side == "right" else -Y_TICK_LABEL_X
        ha = "left" if y_tick_label_side == "right" else "right"
        ax.text(x_txt, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha=ha, va="center", color=TICK_LABEL_COLOR)

    ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$", fontsize=TICK_LABEL_SIZE, ha="left", va="top", color=TICK_LABEL_COLOR)
    ax.text(xlim[1] + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, x_axis_label, fontsize=AXIS_LABEL_SIZE, ha="left", va="center", color=AXIS_COLOR)
    ax.text(0, ylim[1] + Y_AXIS_LABEL_Y_PAD, y_axis_label, fontsize=TOP_LABEL_SIZE, ha="center", va="bottom", color=TICK_LABEL_COLOR)

def plot_signal(ax, t, x, *, lw=SIGNAL_LW):
    ax.plot(t, x, color=SIGNAL_COLOR, linewidth=lw, solid_capstyle="butt", solid_joinstyle="miter", zorder=4)

def save_figure(fig, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=CANONICAL_DPI, bbox_inches="tight", facecolor="white")

fig, ax = make_ct_signal_figure(xlim=(-3.0, 5.0), ylim=(-0.5, 2.0))
setup_ct_signal_axes(
    ax,
    xlim=(-3.0, 5.0),
    ylim=(-0.5, 2.0),
    xticks=[-1.0, 0.0, 1.0, 2.0, 3.0, 4.0],
    yticks=[0.0, 1.0],
    x_axis_label=r"$t$",
    y_axis_label=r"$y(t)$",
    x_minor_grid_step=0.5,
    y_minor_grid_step=0.5,
)

t = np.array([-3.0, -1.0, 0.0, 3.0, 5.0])
x = np.array([0.0, 0.0, 1.4, 0.0, 0.0])
plot_signal(ax, t, x)
ax.text(-1.0, -0.28, r"$-1$", fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR)
ax.text(3.0, -0.28, r"$3$", fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR)
ax.text(1.0, 1.55, r"$y(t)>0$", fontsize=ANNOTATION_SIZE, ha="center", va="center", color=AXIS_COLOR)

save_figure(fig, '/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/7.4--direct-convolution-for-lti-systems-Images/images/l007-s003-qg-q001-q001.png')
