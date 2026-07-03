"""Question image: identify which label is input and output in a left-right block diagram."""

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
ANNOTATION_SIZE = px_to_pt(33.3)
TOP_LABEL_SIZE = px_to_pt(57.8)


def save_figure(fig, path: str | Path):
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=CANONICAL_DPI, facecolor="white", bbox_inches="tight")


def add_arrow(ax, x0, y0, x1, y1):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle="->", color=SIGNAL_COLOR, lw=AXIS_LW, shrinkA=0, shrinkB=0))


def draw_unit_impulse(ax, x0, y0, amp=1.0):
    ax.plot([x0, x0], [y0, y0 + amp], color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="butt", zorder=4)


def draw_decay(ax, x_start, y_base):
    t = np.linspace(0, 2.2, 220)
    y = y_base - 0.18 + 0.55 * np.exp(-1.3 * t) * np.sin(2.1 * t)
    y += 0.06 * np.exp(-0.5 * (t - 1.1) ** 2)
    ax.plot(x_start + t, y, color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="round", zorder=4)


fig, ax = plt.subplots(figsize=(12.0, 4.5), dpi=CANONICAL_DPI, facecolor="white", constrained_layout=True)
ax.set_xlim(-0.7, 10.3)
ax.set_ylim(-1.0, 2.1)
ax.set_aspect("equal", adjustable="box")
ax.axis("off")

ax.text(0.2, 1.55, r"$\delta(t)$", color=LABEL_COLOR, fontsize=TOP_LABEL_SIZE, ha="left", va="center")
draw_unit_impulse(ax, 0.9, 0.3, amp=0.9)
add_arrow(ax, 1.1, 1.0, 2.6, 1.0)

system = Rectangle((2.85, 0.25), 2.5, 1.45, edgecolor=AXIS_COLOR, facecolor="white", lw=AXIS_LW)
ax.add_patch(system)
ax.text(4.1, 1.0, r"LTI\ system", color=LABEL_COLOR, fontsize=TOP_LABEL_SIZE * 0.52, ha="center", va="center")

ax.text(6.2, 1.08, r"$r(t)$", color=LABEL_COLOR, fontsize=TOP_LABEL_SIZE, ha="left", va="center")
add_arrow(ax, 5.35, 1.0, 6.5, 1.0)
draw_decay(ax, 6.7, 1.0)

ax.text(6.65, 1.8, r"input", color=AXIS_COLOR, fontsize=ANNOTATION_SIZE, ha="left", va="top")
ax.text(6.65, 0.78, r"output", color=AXIS_COLOR, fontsize=ANNOTATION_SIZE, ha="left", va="top")

save_figure(fig, '/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/6.1--lti-systems-Images/images/l003-s003-qg-q001-q001.png')
