"""Question image: interpretation of r(t) as reference response from delta input."""

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
ANNOT_COLOR = "#555555"
SIGNAL_LW = px_to_pt(7.1)
AXIS_LW = px_to_pt(4.3)
TOP_LABEL_SIZE = px_to_pt(57.8)
ANNOTATION_SIZE = px_to_pt(33.3)


def add_arrow(ax, x0, y0, x1, y1):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle="->", color=SIGNAL_COLOR, lw=AXIS_LW, shrinkA=0, shrinkB=0))


def draw_unit_impulse(ax, x0, y0, amp=1.0):
    ax.plot([x0, x0], [y0, y0 + amp], color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="butt", zorder=4)


fig, ax = plt.subplots(figsize=(12.0, 4.8), dpi=CANONICAL_DPI, facecolor="white", constrained_layout=True)
ax.set_xlim(-0.75, 10.6)
ax.set_ylim(-1.1, 2.2)
ax.set_aspect("equal", adjustable="box")
ax.axis("off")

ax.text(0.05, 1.55, r"$\delta(t)$", color=LABEL_COLOR, fontsize=TOP_LABEL_SIZE, ha="left", va="center")
draw_unit_impulse(ax, 0.8, 0.35, amp=0.85)
add_arrow(ax, 1.1, 1.0, 2.5, 1.0)

sys = Rectangle((2.75, 0.28), 2.45, 1.45, edgecolor=AXIS_COLOR, facecolor="white", lw=AXIS_LW)
ax.add_patch(sys)
ax.text(3.98, 1.0, r"LTI\ system", color=LABEL_COLOR, fontsize=TOP_LABEL_SIZE * 0.52, ha="center", va="center")

ax.text(5.35, 1.18, r"$r(t)$", color=LABEL_COLOR, fontsize=TOP_LABEL_SIZE * 0.84, ha="left", va="center")
add_arrow(ax, 5.35, 1.0, 6.7, 1.0)

wave_t = np.linspace(0, 2.4, 240)
wave_y = 0.95 + 0.58 * np.exp(-1.2 * wave_t) * np.cos(2.6 * wave_t)
ax.plot(6.7 + 0.5 * wave_t, wave_y, color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="round")
ax.text(7.95, 1.45, r"$r(t)$", color=ANNOT_COLOR, fontsize=ANNOTATION_SIZE * 1.0, ha="right", va="bottom")
ax.text(9.1, 0.92, r"reference\ response\ for\ later\ impulse\ inputs", color=ANNOT_COLOR, fontsize=ANNOTATION_SIZE * 0.82, ha="left", va="top")

save_path = Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/6.1--lti-systems-Images/images/l003-s004-qg-q001-q001.png')
save_path.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(save_path, dpi=CANONICAL_DPI, facecolor='white', bbox_inches='tight')
