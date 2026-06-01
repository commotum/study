"""Block diagram image for section 1: unit impulse input through an LTI system."""

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
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
ANNOTATION_COLOR = "#555555"

SIGNAL_LW = px_to_pt(7.1)
AXIS_LW = px_to_pt(4.3)
TICK_LW = px_to_pt(2.7)
GRID_LW = px_to_pt(1.3)
ANNOTATION_LW = px_to_pt(2.9)

TICK_HALF_LEN = 0.055
TOP_LABEL_SIZE = px_to_pt(57.8)
AXIS_LABEL_SIZE = px_to_pt(53.3)
ANNOTATION_SIZE = px_to_pt(33.3)


def save_figure(fig, path: str | Path):
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=CANONICAL_DPI, facecolor="white", bbox_inches="tight")


def add_arrow(ax, x0, y0, x1, y1, *, label=None, label_offset=(0, 0.12)):
    ax.annotate(
        "",
        xy=(x1, y1),
        xytext=(x0, y0),
        arrowprops=dict(
            arrowstyle="->",
            lw=AXIS_LW,
            color=SIGNAL_COLOR,
            shrinkA=0,
            shrinkB=0,
        ),
    )
    if label:
        ax.text(x0 + 0.5 * (x1 - x0) + label_offset[0], max(y0, y1) + label_offset[1], label,
                color=LABEL_COLOR, fontsize=AXIS_LABEL_SIZE, ha="center", va="bottom")


def draw_unit_impulse(ax, x0, y0, amp):
    ax.plot([x0, x0], [y0, y0 + amp], color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="butt", zorder=4)
    ax.plot([x0, x0], [y0 + amp, y0 + amp + 0.06], color=SIGNAL_COLOR, linewidth=AXIS_LW, solid_capstyle="butt", zorder=5)


def draw_reference_waveform(ax, x_start, y_base):
    t = np.linspace(0, 2.6, 260)
    y = y_base + 0.45 * np.exp(-1.0 * t) * np.sin(2.2 * np.pi * t)
    y += 0.15 * np.exp(-1.3 * t)
    ax.plot(x_start + t, y, color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="round", zorder=4)


fig, ax = plt.subplots(
    figsize=(12.0, 4.8),
    dpi=CANONICAL_DPI,
    facecolor="white",
    constrained_layout=True,
)

ax.set_xlim(-0.8, 10.5)
ax.set_ylim(-1.0, 2.2)
ax.set_aspect("equal", adjustable="box")
ax.axis("off")

# Input signal and label.
ax.text(0.1, 1.55, r"$x(t)=\delta(t)$", color=LABEL_COLOR, fontsize=TOP_LABEL_SIZE, ha="left", va="center")
add_arrow(ax, 1.05, 1.0, 2.45, 1.0)
draw_unit_impulse(ax, 0.7, 0.20, 0.7)
ax.plot([0.7, 0.7], [0.20, 1.0], color=AXIS_COLOR, linewidth=TICK_LW, alpha=0.15)

# LTI system block.
system = Rectangle((2.9, 0.3), 2.4, 1.4, edgecolor=AXIS_COLOR, facecolor="white", lw=AXIS_LW)
ax.add_patch(system)
ax.text(4.1, 1.0, r"LTI\ system", color=LABEL_COLOR, fontsize=AXIS_LABEL_SIZE, ha="center", va="center")

# Output label and arrow.
add_arrow(ax, 5.3, 1.0, 6.65, 1.0)
ax.text(6.72, 1.15, r"response\ to\ $\delta(t)$", color=LABEL_COLOR, fontsize=TOP_LABEL_SIZE * 0.58, ha="left", va="center")

# Response waveform.
ax.text(7.35, 1.0, r"$y(t)$", color=TICK_LABEL_COLOR, fontsize=ANNOTATION_SIZE, ha="left", va="center")
draw_reference_waveform(ax, 7.55, 0.78)

# small framing points
for x in [0.45, 2.85, 5.25, 9.95]:
    ax.plot([x, x], [0.15, 1.95], color="none")

save_figure(fig, '/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/6.1--lti-systems-Images/images/l003-s001-te-section-001.png')
