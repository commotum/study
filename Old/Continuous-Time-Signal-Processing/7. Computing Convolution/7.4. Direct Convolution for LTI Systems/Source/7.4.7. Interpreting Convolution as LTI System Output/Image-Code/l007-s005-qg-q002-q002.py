from __future__ import annotations

from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

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


def style_axis(ax):
    ax.set_xlim(-1.0, 7.0)
    ax.set_ylim(-0.2, 1.4)
    ax.set_aspect("equal", adjustable='box')
    ax.grid(True, which='both', linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    for t in [-1, 0, 2, 4, 6, 7]:
        ax.plot([t, t], [-0.03, 0.03], color=AXIS_COLOR, lw=TICK_LW)
        ax.text(t, -0.10, rf"${t:g}$", fontsize=TICK_LABEL_SIZE*0.8, ha='center', va='top', color=TICK_LABEL_COLOR)
    for y in [0, 0.6, 1.0]:
        if y == 0:
            continue
        ax.plot([-0.03, 0.03], [y, y], color=AXIS_COLOR, lw=TICK_LW)
        ax.text(-0.10, y, rf"${y:g}$", fontsize=TICK_LABEL_SIZE*0.8, ha='right', va='center', color=TICK_LABEL_COLOR)
    ax.plot([ -1, 7 ], [0,0], color=AXIS_COLOR, lw=TICK_LW)
    ax.plot([0,0], [-0.2,1.3], color=AXIS_COLOR, lw=TICK_LW)


def draw_tri(ax, t, x):
    ax.plot(t, x, color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle='round', solid_joinstyle='round')

fig, axs = plt.subplots(3, 1, figsize=(10, 10), dpi=CANONICAL_DPI, facecolor='white', constrained_layout=True)

# Top triangular x(t)
style_axis(axs[0])
xt = np.array([-1.0, 0.0, 1.5, 3.0, 4.0])
xx = np.array([0.0, 0.0, 1.0, 0.0, 0.0])
draw_tri(axs[0], xt, xx)
axs[0].text(1.5, 1.04, r'$x(t)$', fontsize=20, ha='center', color=AXIS_COLOR)

# Middle h(t) rectangle
style_axis(axs[1])
ht = np.array([0.0, 0.0, 1.0, 1.0, 0.0])
hx = np.array([0.0, 1.0, 1.0, 0.0, 0.0])
draw_tri(axs[1], ht, hx)
axs[1].text(0.5, 1.04, r'$h(t)$', fontsize=20, ha='center', color=AXIS_COLOR)

# Bottom hump output
ty = np.array([-1.0, 0.0, 2.0, 4.0, 6.0])
y = np.array([0.0, 0.0, 1.2, 0.0, 0.0])
style_axis(axs[2])
draw_tri(axs[2], ty, y)
axs[2].text(2, 1.05, r'$y(t)$', fontsize=20, ha='center', color=AXIS_COLOR)
axs[2].text(2, -0.06, r'$a$', fontsize=TICK_LABEL_SIZE*0.7)
axs[2].text(4, -0.06, r'$b$', fontsize=TICK_LABEL_SIZE*0.7)
axs[2].text(6, -0.06, r'$c$', fontsize=TICK_LABEL_SIZE*0.7)
axs[2].text(1, 0.65, r'$a<t<b$', fontsize=16)
axs[2].text(5, 0.65, r'$b<t<c$', fontsize=16)

out = Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/7.4--direct-convolution-for-lti-systems-Images/images/l007-s005-qg-q002-q002.png')
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=CANONICAL_DPI, bbox_inches='tight', facecolor='white')
