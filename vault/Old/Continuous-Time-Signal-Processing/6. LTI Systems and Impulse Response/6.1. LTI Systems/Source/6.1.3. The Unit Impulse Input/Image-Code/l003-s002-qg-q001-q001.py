"""Question-image showing five candidate input signals (order set A..E)."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrow
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
SMOOTH_SIGNAL_LW = px_to_pt(5.2)
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


def setup_ct_signal_axes(ax, *, xlim, ylim, xticks, yticks, y_tick_label_side="left"):
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
        if abs(float(y)) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if y_tick_label_side == "right":
            ax.text(Y_TICK_LABEL_X, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha="left", va="center", color=TICK_LABEL_COLOR, zorder=6)
        else:
            ax.text(-Y_TICK_LABEL_X, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha="right", va="center", color=TICK_LABEL_COLOR, zorder=6)

    ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$", fontsize=TICK_LABEL_SIZE, ha="left", va="top", color=TICK_LABEL_COLOR, zorder=6)
    ax.text(x_axis_end + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, r"$t$", fontsize=AXIS_LABEL_SIZE, ha="left", va="center", color=TICK_LABEL_COLOR, clip_on=False)
    ax.text(0, y_axis_end + Y_AXIS_LABEL_Y_PAD, r"$x(t)$", fontsize=TOP_LABEL_SIZE, ha="center", va="bottom", color=TICK_LABEL_COLOR, clip_on=False)


def draw_unit_impulse(ax, t0, amp=1.0):
    ax.plot([t0, t0], [0.0, amp], color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="butt", solid_joinstyle="miter", zorder=4)


def draw_step(ax):
    t = [-2.5, 0, 0, 2.5]
    x = [0, 0, 1, 1]
    ax.plot(t, x, color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="butt", solid_joinstyle="miter", zorder=4)


def draw_rect_pulse(ax, t0=-0.7, t1=0.7, amp=1.0):
    ax.plot([t0, t0, t1, t1], [0, amp, amp, 0], color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="butt", solid_joinstyle="miter", zorder=4)


def draw_signal_variant(ax, kind, *, label):
    setup_ct_signal_axes(ax, xlim=(-2.5, 2.5), ylim=(-0.2, 1.6), xticks=[-2, -1, 1, 2], yticks=[1], y_tick_label_side="left")
    if kind == "step":
        draw_step(ax)
    elif kind == "impulse-shifted":
        draw_unit_impulse(ax, 2, amp=1.0)
    elif kind == "impulse":
        draw_unit_impulse(ax, 0, amp=1.0)
    elif kind == "impulse-scaled":
        draw_unit_impulse(ax, 0, amp=2.0)
        ax.text(0.0, 1.38, r"2", color=LABEL_COLOR, fontsize=TICK_LABEL_SIZE * 0.85, ha="left", va="bottom")
    elif kind == "pulse":
        draw_rect_pulse(ax)
    else:
        raise ValueError("unknown kind")
    ax.text(-2.18, 1.46, label, fontsize=TICK_LABEL_SIZE * 1.02, fontweight="bold", color=LABEL_COLOR, ha="left", va="center")


panel_defs = [
    ("A", "u(t)", "step"),
    ("B", r"$\delta(t-2)$", "impulse-shifted"),
    ("C", r"$\delta(t)$", "impulse"),
    ("D", r"$2\delta(t)$", "impulse-scaled"),
    ("E", "rect", "pulse"),
]

fig = plt.figure(figsize=(16.0, 4.0), dpi=CANONICAL_DPI, facecolor="white", constrained_layout=True)
left, bottom, width, height = 0.06, 0.22, 0.88, 0.66
panel_width = 0.165
gap = 0.015
axes = []
for i, _ in enumerate(panel_defs):
    ax = fig.add_axes([left + i * (panel_width + gap), bottom, panel_width, height])
    axes.append(ax)

for ax, (label, symbol, kind) in zip(axes, panel_defs):
    draw_signal_variant(ax, kind, label=label)
    ax.text(1.65, 1.55, symbol, fontsize=TICK_LABEL_SIZE * 0.93, color=LABEL_COLOR, ha="right", va="top")

fig.text(0.5, 0.06, r"candidate inputs to the same LTI system", fontsize=TICK_LABEL_SIZE * 0.86, ha="center", va="center", color=LABEL_COLOR)

output_path = Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/6.1--lti-systems-Images/images/l003-s002-qg-q001-q001.png')
output_path.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(output_path, dpi=CANONICAL_DPI, facecolor="white", bbox_inches="tight")
