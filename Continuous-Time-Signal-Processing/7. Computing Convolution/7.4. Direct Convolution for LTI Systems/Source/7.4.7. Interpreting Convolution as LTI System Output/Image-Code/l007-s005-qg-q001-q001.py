from __future__ import annotations

from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams.update({"mathtext.fontset": "cm", "font.family": "serif"})

CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150

def px_to_pt(px: float) -> float:
    return px * 72 / CANONICAL_DPI

def px_to_data(px: float) -> float:
    return px / PX_PER_DATA_UNIT

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
GRID_COLOR = "#000000"
TICK_LABEL_COLOR = "#444444"
GRID_LW = px_to_pt(1.3)
TICK_LW = px_to_pt(2.7)
SIGNAL_LW = px_to_pt(7.1)
TICK_LABEL_SIZE = px_to_pt(35.6)
AXIS_LABEL_SIZE = px_to_pt(53.3)
TOP_LABEL_SIZE = px_to_pt(57.8)


def style_axis(ax):
    ax.set_xlim( -0.5, 8.0)
    ax.set_ylim(-0.2, 1.4)
    ax.set_aspect('equal', adjustable='box')
    ax.grid(True, which='both', linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    ax.axhline(0, color=AXIS_COLOR, lw=TICK_LW)
    ax.axvline(0, color=AXIS_COLOR, lw=TICK_LW)
    for t in [0,2,4,6,8]:
        ax.plot([t, t], [-0.03, 0.03], color=AXIS_COLOR, lw=TICK_LW)
        ax.text(t, -0.10, rf"${t:g}$", fontsize=TICK_LABEL_SIZE*0.8, ha='center', va='top', color=TICK_LABEL_COLOR)
    for y in [0, 0.6, 1.0]:
        if y == 0:
            continue
        ax.plot([-0.03, 0.03], [y, y], color=AXIS_COLOR, lw=TICK_LW)
        ax.text(-0.10, y, rf"${y:g}$", fontsize=TICK_LABEL_SIZE*0.8, ha='right', va='center', color=TICK_LABEL_COLOR)


def draw_rect(ax, t0, t1, y=1.0):
    w = t1 - t0
    pts_t = np.array([t0, t0, t1, t1, t0])
    pts_x = np.array([0, y, y, 0, 0])
    ax.plot(pts_t, pts_x, color=SIGNAL_COLOR, linewidth=SIGNAL_LW)


def draw_signal(ax, t, x):
    ax.plot(t, x, color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle='butt', solid_joinstyle='miter')

fig, axs = plt.subplots(3, 1, figsize=(10, 10), dpi=CANONICAL_DPI, facecolor='white', constrained_layout=True)

# Top: x(t)
style_axis(axs[0])
draw_rect(axs[0], 0, 6)
axs[0].text(3, 1.18, r'$x(t)$', fontsize=20, ha='center', color=AXIS_COLOR)
axs[0].text(0, -0.06, r'$0$', fontsize=TICK_LABEL_SIZE*0.7, ha='left', va='top')

# Middle: h(t)
draw_rect(axs[1], 0, 2)
style_axis(axs[1])
axs[1].text(1, 1.18, r'$h(t)$', fontsize=20, ha='center', color=AXIS_COLOR)

# Bottom: y(t)
style_axis(axs[2])
t_y = np.array([0, 0, 2, 6, 8, 8])
y_y = np.array([0, 0, 1, 1, 0, 0])
draw_signal(axs[2], t_y, y_y)
axs[2].text(4, 1.05, r'$y(t)$', fontsize=20, ha='center', color=AXIS_COLOR)
axs[2].text(0, -0.06, r'$a$', fontsize=TICK_LABEL_SIZE*0.7)
axs[2].text(2, -0.06, r'$b$', fontsize=TICK_LABEL_SIZE*0.7)
axs[2].text(6, -0.06, r'$d$', fontsize=TICK_LABEL_SIZE*0.7)
axs[2].text(4, 0.05, r'$c$', fontsize=TICK_LABEL_SIZE*0.7)
axs[2].text(1, 0.7, r'$a<t<b$', fontsize=16)
axs[2].text(4, 0.7, r'$b<t<c$', fontsize=16)
axs[2].text(7, 0.7, r'$c<t<d$', fontsize=16)
axs[2].text( -0.4, 0.0, r'$0$', fontsize=TICK_LABEL_SIZE*0.7)

out = Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/7.4--direct-convolution-for-lti-systems-Images/images/l007-s005-qg-q001-q001.png')
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=CANONICAL_DPI, bbox_inches='tight', facecolor='white')
