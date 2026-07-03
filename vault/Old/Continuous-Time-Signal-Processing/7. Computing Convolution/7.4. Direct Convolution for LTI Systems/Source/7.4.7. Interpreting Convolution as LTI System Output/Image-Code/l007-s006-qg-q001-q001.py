from __future__ import annotations

from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.ticker import MultipleLocator

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
TICK_HALF_LEN = px_to_data(8.25)
X_TICK_LABEL_Y = -px_to_data(24)
Y_TICK_LABEL_X = px_to_data(18)
X_AXIS_LABEL_X_PAD = px_to_data(15)
X_AXIS_LABEL_Y = -px_to_data(4.5)
Y_AXIS_LABEL_Y_PAD = px_to_data(18)
ORIGIN_LABEL_X = px_to_data(9)
ORIGIN_LABEL_Y = -px_to_data(12)
AXIS_ARROW_SHAFT_WIDTH_DATA = px_to_data(4.3)
AXIS_ARROW_KW = dict(angles='xy', scale_units='xy', scale=1, units='xy', width=AXIS_ARROW_SHAFT_WIDTH_DATA, headwidth=4.2, headlength=5.5, headaxislength=4.3, color=AXIS_COLOR, pivot='tail', clip_on=False)

def make_axis(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xticks([ -1, 0, 1, 2, 3, 4, 5, 6, 7, 8 ])
    ax.set_yticks([0, 1])
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.2))
    ax.grid(True, which='both', linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    ax.quiver(xlim[0], 0, xlim[1]-xlim[0], 0, **AXIS_ARROW_KW)
    ax.quiver(0, ylim[0], 0, ylim[1]-ylim[0], **AXIS_ARROW_KW)
    for t in [0, 2, 4, 6, 8]:
        if t == 0:
            continue
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW)
        ax.text(t, X_TICK_LABEL_Y, rf"${t:g}$", fontsize=TICK_LABEL_SIZE, ha='center', va='top', color=TICK_LABEL_COLOR)
    for y in [1]:
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW)
        ax.text(-Y_TICK_LABEL_X, y, rf"${y:g}$", fontsize=TICK_LABEL_SIZE, ha='right', va='center', color=TICK_LABEL_COLOR)
    ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$", fontsize=TICK_LABEL_SIZE, ha='left', va='top', color=TICK_LABEL_COLOR)
    ax.text(xlim[1] + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, r"$t$", fontsize=AXIS_LABEL_SIZE, ha='left', va='center')
    ax.text(0, ylim[1] + Y_AXIS_LABEL_Y_PAD, r"$y(t)$", fontsize=TOP_LABEL_SIZE, ha='center', va='bottom', color=TICK_LABEL_COLOR)

def draw_block(ax):
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 6)
    ax.axis('off')
    ax.annotate('', xy=(1.3, 3.2), xytext=(0.2, 3.2), arrowprops=dict(arrowstyle='->', lw=TICK_LW, color=AXIS_COLOR))
    ax.text(0.6, 3.5, r'$x(t)$', fontsize=20, color=AXIS_COLOR)
    block = Rectangle((2.7, 2.1), 2.6, 2.2, edgecolor=AXIS_COLOR, facecolor='white', lw=TICK_LW)
    ax.add_patch(block)
    ax.text(3.95, 3.2, r'$h(t)$', fontsize=22, ha='center', color=AXIS_COLOR)
    ax.annotate('', xy=(6.0, 3.2), xytext=(5.5, 3.2), arrowprops=dict(arrowstyle='->', lw=TICK_LW, color=AXIS_COLOR))
    ax.text(6.45, 3.5, r'$y(t)=(x*h)(t)$', fontsize=18, color=AXIS_COLOR)

fig, axs = plt.subplots(2, 1, figsize=(11, 9.5), dpi=CANONICAL_DPI, facecolor='white', constrained_layout=True, height_ratios=[1, 2])
fig.delaxes(axs[0])
ax_block = fig.add_axes([0.08, 0.72, 0.84, 0.18])
ax_plot = fig.add_axes([0.12, 0.12, 0.80, 0.55])

draw_block(ax_block)
make_axis(ax_plot, (-1.0, 8.0), (-0.5, 1.8))
# Output shape with p,q,r,s and regions
t = np.array([0.0, 0.0, 2.0, 6.0, 8.0, 8.0])
y = np.array([0.0, 0.0, 1.2, 1.2, 0.0, 0.0])
ax_plot.plot(t, y, color=SIGNAL_COLOR, linewidth=SIGNAL_LW)
for p,txt in zip([0.0,2.0,6.0,8.0], [r'$p$', r'$q$', r'$r$', r'$s$']):
    ax_plot.text(p, -0.08, txt, fontsize=TICK_LABEL_SIZE*0.7, ha='center', va='top', color=TICK_LABEL_COLOR)
ax_plot.text(1.0, 1.0, r'$p<t<q$', fontsize=26, color=AXIS_COLOR)
ax_plot.text(4.0, 1.0, r'$q<t<r$', fontsize=26, color=AXIS_COLOR)
ax_plot.text(7.0, 1.0, r'$r<t<s$', fontsize=26, color=AXIS_COLOR)

out = Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/7.4--direct-convolution-for-lti-systems-Images/images/l007-s006-qg-q001-q001.png')
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=CANONICAL_DPI, bbox_inches='tight', facecolor='white')
