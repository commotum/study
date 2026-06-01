"""Question image (top-to-bottom): distinguish input vs output direction and labels."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams.update({
    "mathtext.fontset": "cm",
    "font.family": "serif",
})

CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150


def px_to_pt(px: float) -> float:
    return px * 72 / CANONICAL_DPI

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
SIGNAL_LW = px_to_pt(7.1)
AXIS_LW = px_to_pt(4.3)
TOP_LABEL_SIZE = px_to_pt(57.8)
ANNOTATION_SIZE = px_to_pt(33.3)


def add_arrow(ax, x0, y0, x1, y1):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle="->", color=SIGNAL_COLOR, lw=AXIS_LW, shrinkA=0, shrinkB=0))


def draw_unit_impulse(ax, x0, y0, amp=1.0):
    ax.plot([x0, x0], [y0, y0 + amp], color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="butt", zorder=4)


def draw_decay(ax, y_start):
    t = np.linspace(0, 1.4, 180)
    y = y_start - 0.7 + 0.55 * np.exp(-1.5 * t) * np.cos(3 * t)
    ax.plot(0.0 + 0.0 * t, y, color=AXIS_COLOR, lw=0)
    x = np.linspace(0, 1.2, 2)
    baseline = np.array([y_start - 0.7, y_start - 0.7])
    # Use a left-anchored parametric curve translated to plot area.
    tx = x
    ty = y_start - 0.7 + 0.5 * np.exp(-1.8 * tx) * np.cos(3 * tx)
    ax.plot(np.full_like(tx, 0.0), ty, color=SIGNAL_COLOR, linewidth=0.0)


def draw_response(ax):
    t = np.linspace(-0.55, 0.55, 220)
    y = 0.85 - 0.5 * np.exp(-1.7 * (t + 0.55))
    x = 0.15 * t + 0.12
    ax.plot(x, y, color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="round", zorder=4)


fig, ax = plt.subplots(figsize=(5.0, 8.2), dpi=CANONICAL_DPI, facecolor="white", constrained_layout=True)
ax.set_xlim(-0.9, 2.3)
ax.set_ylim(-1.4, 3.2)
ax.axis("off")

ax.text(0.35, 2.95, r"$\delta(t)$", color=LABEL_COLOR, fontsize=TOP_LABEL_SIZE, ha="left", va="center")
draw_unit_impulse(ax, 1.0, 1.25, amp=0.9)

block = Rectangle((0.55, 1.5), 1.05, 1.0, edgecolor=AXIS_COLOR, facecolor="white", lw=AXIS_LW)
ax.add_patch(block)
ax.text(1.07, 2.0, r"LTI\ system", color=LABEL_COLOR, fontsize=TOP_LABEL_SIZE * 0.46, ha="center", va="center")

add_arrow(ax, 1.075, 1.5, 1.075, 0.55)
ax.text(0.0, 1.0, r"$\delta(t)$", color=LABEL_COLOR, fontsize=TOP_LABEL_SIZE * 0.41, ha="right", va="center")

ax.text(0.7, 0.4, r"$y(t)$", color=LABEL_COLOR, fontsize=TOP_LABEL_SIZE * 0.72, ha="left", va="center")
add_arrow(ax, 1.075, 1.5, 1.075, 0.22)

decay_t = np.linspace(0.18, 1.08, 220)
decay_y = 0.4 + 0.55 * np.exp(-2.0 * (decay_t - 0.18)) * np.cos(4.0 * (decay_t - 0.18))
ax.plot(decay_t, decay_y, color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="round")

save_path = Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/6.1--lti-systems-Images/images/l003-s003-qg-q002-q002.png')
save_path.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(save_path, dpi=CANONICAL_DPI, facecolor='white', bbox_inches='tight')
