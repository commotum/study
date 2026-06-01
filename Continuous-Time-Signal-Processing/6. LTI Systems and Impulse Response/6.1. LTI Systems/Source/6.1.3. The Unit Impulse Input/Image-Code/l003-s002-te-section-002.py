"""Section image combining five labeled candidate inputs with a shared LTI reference note."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.ticker import MultipleLocator

plt.rcParams.update({
    "mathtext.fontset": "cm",
    "font.family": "serif",
})

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

SIGNAL_LW = px_to_pt(7.1)
AXIS_LW = px_to_pt(4.3)
TICK_LW = px_to_pt(2.7)
GRID_LW = px_to_pt(1.3)
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


def math_label(value):
    if isinstance(value, str):
        return value
    if abs(value - int(value)) < 1e-9:
        return rf"${int(value)}$"
    return rf"${value:g}$"


def setup_ct_signal_axes(ax, *, xlim, ylim, xticks, yticks):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.xaxis.set_minor_locator(MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(MultipleLocator(0.5))
    ax.grid(True, which="both", linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    x_axis_start, x_axis_end = xlim
    y_axis_start, y_axis_end = ylim
    ax.quiver(x_axis_start, 0, x_axis_end - x_axis_start, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y_axis_start, 0, y_axis_end - y_axis_start, **AXIS_ARROW_KW)

    for t in xticks:
        if abs(float(t)) < 1e-12:
            continue
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(t, X_TICK_LABEL_Y, math_label(t), fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR, zorder=6)

    for y in yticks:
        if abs(float(y)) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(-Y_TICK_LABEL_X, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha="right", va="center", color=TICK_LABEL_COLOR, zorder=6)

    ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$", fontsize=TICK_LABEL_SIZE, ha="left", va="top", color=TICK_LABEL_COLOR, zorder=6)
    ax.text(x_axis_end + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, r"$t$", fontsize=AXIS_LABEL_SIZE, ha="left", va="center", color=TICK_LABEL_COLOR, clip_on=False)
    ax.text(0, y_axis_end + Y_AXIS_LABEL_Y_PAD, r"$x(t)$", fontsize=TOP_LABEL_SIZE, ha="center", va="bottom", color=TICK_LABEL_COLOR, clip_on=False)


def draw_unit_impulse(ax, t0, amp=1.0):
    ax.plot([t0, t0], [0.0, amp], color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="butt", zorder=4)


def draw_step(ax):
    t = [-2.5, 0, 0, 2.5]
    x = [0, 0, 1, 1]
    ax.plot(t, x, color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="butt", zorder=4)


def draw_rect_pulse(ax):
    ax.plot([-0.7, -0.7, 0.7, 0.7], [0, 1, 1, 0], color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="butt", zorder=4)


def draw_panel(ax, signal_label, kind, signal_formula, t_imp=None, amp=1.0):
    setup_ct_signal_axes(ax, xlim=(-2.5, 2.5), ylim=(-0.2, 1.6), xticks=[-2, -1, 1, 2], yticks=[1])
    if kind == "impulse":
        draw_unit_impulse(ax, t_imp, amp=amp)
    elif kind == "step":
        draw_step(ax)
    elif kind == "pulse":
        draw_rect_pulse(ax)
    elif kind == "scaled":
        draw_unit_impulse(ax, t_imp, amp=amp)
        ax.text(t_imp, 1.35, r"2", fontsize=TICK_LABEL_SIZE * 0.8, color=LABEL_COLOR, ha="left", va="bottom")

    ax.text(-2.2, 1.45, signal_label, fontsize=TICK_LABEL_SIZE * 0.96, fontweight="bold", color=LABEL_COLOR, ha="left", va="center")
    ax.text(1.85, 1.56, signal_formula, fontsize=TICK_LABEL_SIZE * 0.73, color=LABEL_COLOR, ha="right", va="top")


panel_defs = [
    ("A", "impulse", r"$x_A(t)=\delta(t)$", 0, 1.0),
    ("B", "step", r"$x_B(t)=u(t)$", None, 1.0),
    ("C", "impulse", r"$x_C(t)=\delta(t-2)$", 2, 1.0),
    ("D", "scaled", r"$x_D(t)=2\delta(t)$", 0, 2.0),
    ("E", "pulse", r"$x_E(t)=rectangular\ pulse$", None, 1.0),
]

fig = plt.figure(figsize=(16.2, 4.8), dpi=CANONICAL_DPI, facecolor="white", constrained_layout=True)
left, bottom, width, height = 0.04, 0.24, 0.88, 0.62
panel_w = 0.165
gap = 0.015
for i, item in enumerate(panel_defs):
    ax = fig.add_axes([left + i * (panel_w + gap), bottom, panel_w, height])
    draw_panel(ax, *item)

# Shared LTI system descriptor note.
fig.text(0.5, 0.08, r"candidate inputs to the same LTI system", fontsize=TICK_LABEL_SIZE * 0.85, color=LABEL_COLOR, ha="center", va="center")
fig.text(0.5, 0.01, r"LTI\ system", fontsize=TOP_LABEL_SIZE * 0.45, color=LABEL_COLOR, ha="center", va="bottom")

output_path = Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/6.1--lti-systems-Images/images/l003-s002-te-section-002.png')
output_path.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(output_path, dpi=CANONICAL_DPI, facecolor="white", bbox_inches="tight")
