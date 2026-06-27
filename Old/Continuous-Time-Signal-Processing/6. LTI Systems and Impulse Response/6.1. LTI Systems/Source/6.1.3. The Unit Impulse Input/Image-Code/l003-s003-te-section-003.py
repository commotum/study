"""Section image: distinguish input impulse and output response in LTI block diagram."""

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


fig, ax = plt.subplots(figsize=(12.0, 4.8), dpi=CANONICAL_DPI, facecolor="white", constrained_layout=True)
ax.set_xlim(-0.7, 10.4)
ax.set_ylim(-1.1, 2.25)
ax.set_aspect("equal", adjustable="box")
ax.axis("off")

ax.text(0.2, 1.5, r"$x(t)=\delta(t)$", color=LABEL_COLOR, fontsize=TOP_LABEL_SIZE * 0.98, ha="left", va="center")
draw_unit_impulse(ax, 1.0, 0.35, amp=0.9)
add_arrow(ax, 1.2, 1.0, 2.65, 1.0)

block = Rectangle((2.9, 0.3), 2.45, 1.4, edgecolor=AXIS_COLOR, facecolor="white", lw=AXIS_LW)
ax.add_patch(block)
ax.text(4.125, 1.0, r"LTI\ system", color=LABEL_COLOR, fontsize=TOP_LABEL_SIZE * 0.52, ha="center", va="center")

ax.text(5.35, 1.22, r"$y(t)$", color=LABEL_COLOR, fontsize=TOP_LABEL_SIZE * 0.8, ha="left", va="center")
add_arrow(ax, 5.35, 1.0, 6.85, 1.0)

wave_t = np.linspace(0, 2.4, 260)
wave_y = 1.0 - 0.18 + 0.60 * np.exp(-1.15 * wave_t) * np.cos(3.1 * wave_t)
ax.plot(6.8 + wave_t * 0.52, wave_y, color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="round")
ax.text(7.5, 1.65, r"non-impulse\ response", color=LABEL_COLOR, fontsize=ANNOTATION_SIZE, ha="left", va="bottom")

save_path = Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/6.1--lti-systems-Images/images/l003-s003-te-section-003.png')
save_path.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(save_path, dpi=CANONICAL_DPI, facecolor='white', bbox_inches='tight')
