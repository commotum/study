from __future__ import annotations

from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt
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

def draw_axis(ax, xlim, ylim, y_ticks=(0, 0.6, 1.0), x_ticks=None):
    if x_ticks is None:
        x_ticks = [-2, -1, 0, 1, 2, 3, 4]
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks(x_ticks)
    ax.set_yticks(list(y_ticks))
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.2))
    ax.grid(True, which="both", linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    ax.quiver(xlim[0], 0, xlim[1] - xlim[0], 0, **AXIS_ARROW_KW)
    ax.quiver(0, ylim[0], 0, ylim[1] - ylim[0], **AXIS_ARROW_KW)
    for t in x_ticks:
        if t == 0:
            continue
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW)
        ax.text(t, X_TICK_LABEL_Y, rf"${t:g}$", fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR)
    for y in y_ticks:
        if y == 0:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW)
        ax.text(-Y_TICK_LABEL_X, y, rf"${y:g}$", fontsize=TICK_LABEL_SIZE, ha="right", va="center", color=TICK_LABEL_COLOR)
    ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$", fontsize=TICK_LABEL_SIZE, ha="left", va="top", color=TICK_LABEL_COLOR)
    ax.text(xlim[1] + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, r"$\tau$", fontsize=AXIS_LABEL_SIZE, ha="left", va="center")
    ax.text(0, ylim[1] + Y_AXIS_LABEL_Y_PAD, r"$\tau$-axis", fontsize=TOP_LABEL_SIZE, ha="center", va="bottom", color=TICK_LABEL_COLOR)

def draw_interval(ax, interval, y=0.2, fill_overlap=None):
    a, b = interval
    t = np.array([a, a, b, b, a])
    val = np.array([0.0, y, y, 0.0, 0.0])
    ax.plot(t, val, color=SIGNAL_COLOR, linewidth=SIGNAL_LW)
    if fill_overlap is not None:
        c, d = fill_overlap
        if d > c:
            ax.fill_between([c, d], 0.3, 0.7, color="#777777", alpha=0.2)

a_x = (-2.0, 3.0)
h_intervals = [(-6.0, -2.0), (-4.0, 0.0), (-1.0, 3.0)]

fig = plt.figure(figsize=(12.0, 10.0), dpi=CANONICAL_DPI, facecolor="white", constrained_layout=True)
axs = [fig.add_subplot(4, 1, i + 1) for i in range(4)]
for a in axs:
    draw_axis(a, xlim=(-7.0, 8.0), ylim=(-0.05, 1.1))

# Top x(tau)
draw_interval(axs[0], a_x)
axs[0].set_title(r"$x(\tau)$", fontsize=TICK_LABEL_SIZE)

labels = [r"$t=a$", r"$t=b$", r"$t=c$"]
for idx in range(3):
    i = idx + 1
    draw_interval(axs[i], h_intervals[idx], fill_overlap=(max(a_x[0], h_intervals[idx][0]), min(a_x[1], h_intervals[idx][1])))
    axs[i].set_title(labels[idx], fontsize=TICK_LABEL_SIZE)

# Bottom output y(t) with breakpoints a,b,c
yt = np.array([-2.0, -2.0, 1.0, 3.0, 8.0])
yv = np.array([0.0, 0.0, 1.0, 0.0, 0.0])
axs[3].clear()
draw_axis(axs[3], xlim=(-2.0, 8.0), ylim=(-0.05, 1.1), x_ticks=[-2, 0, 1, 3, 4, 5, 6, 7, 8])
axs[3].plot(yt, yv, color=SIGNAL_COLOR, linewidth=SIGNAL_LW)
axs[3].set_title(r"$y(t)$", fontsize=TICK_LABEL_SIZE)
axs[3].text(-2.0, 0.9, r"$a<t<b$", fontsize=TICK_LABEL_SIZE, color=AXIS_COLOR)
axs[3].text(3.0, 0.9, r"$b<t<c$", fontsize=TICK_LABEL_SIZE, color=AXIS_COLOR)

for val, txt in [(-2.0, r"$a$"), (3.0, r"$c$")]:
    axs[3].text(val, -0.03, txt, fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR)

out = Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/7.4--direct-convolution-for-lti-systems-Images/images/l007-s004-qg-q002-q002.png')
out.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out, dpi=CANONICAL_DPI, bbox_inches='tight', facecolor='white')
