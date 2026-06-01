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
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
TICK_LW = px_to_pt(2.7)
GRID_LW = px_to_pt(1.3)
SIGNAL_LW = px_to_pt(7.1)
TICK_LABEL_SIZE = px_to_pt(35.6)
AXIS_LABEL_SIZE = px_to_pt(53.3)
TOP_LABEL_SIZE = px_to_pt(57.8)
TICK_HALF_LEN = px_to_data(8.25)
X_AXIS_LABEL_X_PAD = px_to_data(15)
X_AXIS_LABEL_Y = -px_to_data(4.5)
X_TICK_LABEL_Y = -px_to_data(24)
Y_TICK_LABEL_X = px_to_data(18)
ORIGIN_LABEL_X = px_to_data(9)
ORIGIN_LABEL_Y = -px_to_data(12)
Y_AXIS_LABEL_Y_PAD = px_to_data(18)

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

def make_axis(ax, xlim=(-1, 8), ylim=(-0.1, 1.4)):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks([0, 2, 4, 6, 8])
    ax.set_yticks([0, 0.6, 1.0])
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.2))
    ax.grid(True, which="both", linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    ax.quiver(xlim[0], 0, xlim[1] - xlim[0], 0, **AXIS_ARROW_KW)
    ax.quiver(0, ylim[0], 0, ylim[1] - ylim[0], **AXIS_ARROW_KW)
    for t in [0, 2, 4, 6, 8]:
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW)
        ax.text(t, X_TICK_LABEL_Y, rf"${t:g}$", fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR)
    for y in [0.6, 1.0]:
        if y == 0:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW)
        ax.text(-Y_TICK_LABEL_X, y, rf"${y:g}$", fontsize=TICK_LABEL_SIZE, ha="right", va="center", color=TICK_LABEL_COLOR)
    ax.text(xlim[0] + 0.15, -0.5, rf"$0$", fontsize=TICK_LABEL_SIZE, ha="left", va="top", color=TICK_LABEL_COLOR)
    ax.text(xlim[1] + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, r"$\tau$", fontsize=AXIS_LABEL_SIZE, ha="left", va="center", color=TICK_LABEL_COLOR)
    ax.text(0, ylim[1] + Y_AXIS_LABEL_Y_PAD, r"$\tau$-axis", fontsize=TOP_LABEL_SIZE, ha="center", va="bottom", color=TICK_LABEL_COLOR)

def show_support(ax, interval, y=0.2):
    a, b = interval
    t = np.array([a, a, b, b, a])
    val = np.array([0.0, y, y, 0.0, 0.0])
    ax.plot(t, val, color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="butt", solid_joinstyle="miter")

def show_overlap(ax, interval):
    a, b = interval
    if b > a:
        ax.fill_between([a, b], 0.35, 0.55, color="#777777", alpha=0.20)
        ax.plot([a, b], [0.45, 0.45], color="#777777", linewidth=px_to_pt(3.0), solid_capstyle="round")

fig = plt.figure(figsize=(12.0, 10.0), dpi=CANONICAL_DPI, facecolor="white", constrained_layout=True)
ax1 = fig.add_subplot(4, 1, 1)
ax2 = fig.add_subplot(4, 1, 2)
ax3 = fig.add_subplot(4, 1, 3)
ax4 = fig.add_subplot(4, 1, 4)

for a in [ax1, ax2, ax3, ax4]:
    make_axis(a)

x_support = (0.0, 4.0)
show_support(ax1, x_support)
ax1.set_title(r"$x(\tau)$", fontsize=TICK_LABEL_SIZE)

h_supports = [( -4.0, 0.0), (0.0, 4.0), (4.0, 8.0)]
for k, (a) in enumerate(h_supports, start=2):
    axis = [ax2, ax3, ax4][k-2]
    show_support(axis, a, y=0.2)
    o0, o1 = max(a[0], x_support[0]), min(a[1], x_support[1])
    show_overlap(axis, (o0, o1))

# Labels and emphasis
ax1.set_ylabel(r"$p$", fontsize=TICK_LABEL_SIZE)
ax2.set_ylabel(r"$t=p$", fontsize=TICK_LABEL_SIZE)
ax3.set_ylabel(r"$t=q$", fontsize=TICK_LABEL_SIZE)
ax4.set_ylabel(r"$t=r$", fontsize=TICK_LABEL_SIZE)

# Output plot at bottom panel.
# Use the shared bottom axis row as a concise y(t) sketch with breakpoints.
output_t = np.array([0.0, 0.0, 4.0, 8.0, 8.0])
output_y = np.array([0.0, 0.0, 1.0, 0.0, 0.0])
ax4.plot(output_t, output_y, color=SIGNAL_COLOR, linewidth=SIGNAL_LW, solid_capstyle="butt", solid_joinstyle="miter", zorder=5)
ax4.text(4.0, 0.2, r"$q$", ha="center")
ax4.text(2.0, 0.2, r"overlap begins", fontsize=px_to_pt(25), color=AXIS_COLOR)
ax4.text(4.0, 0.75, r"max overlap", fontsize=px_to_pt(25), color=AXIS_COLOR)
ax4.text(6.0, 0.2, r"ends", fontsize=px_to_pt(25), color=AXIS_COLOR)

out = Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/7.4--direct-convolution-for-lti-systems-Images/images/l007-s004-qg-q001-q001.png')
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=CANONICAL_DPI, bbox_inches='tight', facecolor='white')
