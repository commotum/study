"""Question image: top-to-bottom diagram and interpretation of g(t) as reference response."""

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


fig, ax = plt.subplots(figsize=(5.2, 8.5), dpi=CANONICAL_DPI, facecolor="white", constrained_layout=True)
ax.set_xlim(-0.8, 2.2)
ax.set_ylim(-1.4, 3.2)
ax.axis("off")

ax.text(0.2, 2.88, r"$\delta(t)$", color=LABEL_COLOR, fontsize=TOP_LABEL_SIZE, ha="left", va="center")
draw_unit_impulse(ax, 1.0, 1.35, amp=0.85)
add_arrow(ax, 1.0, 2.0, 1.0, 1.23)

sys = Rectangle((0.33, 1.07), 1.45, 1.0, edgecolor=AXIS_COLOR, facecolor="white", lw=AXIS_LW)
ax.add_patch(sys)
ax.text(1.055, 1.57, r"LTI\ system", color=LABEL_COLOR, fontsize=TOP_LABEL_SIZE * 0.46, ha="center", va="center")

ax.text(1.1, 0.8, r"$g(t)$", color=LABEL_COLOR, fontsize=TOP_LABEL_SIZE * 0.78, ha="left", va="center")
add_arrow(ax, 1.055, 1.07, 1.055, 0.28)

t = np.linspace(0.0, 1.0, 220)
y = 0.8 - 0.58 * (1 - np.exp(-2.6 * (t + 0.02)))
ax.plot(np.full_like(t, 1.055) + 0.32 * t, y + 0.8, color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="round")
ax.text(1.56, 1.15, r"response\ waveform", color=ANNOT_COLOR, fontsize=ANNOTATION_SIZE * 0.9, ha="left", va="bottom")
ax.text(0.14, 0.33, r"reference\ response\ for\ later\ impulse\ inputs", color=ANNOT_COLOR, fontsize=ANNOTATION_SIZE * 0.75, ha="left", va="top")

save_path = Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/6.1--lti-systems-Images/images/l003-s004-qg-q002-q002.png')
save_path.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(save_path, dpi=CANONICAL_DPI, facecolor='white', bbox_inches='tight')
