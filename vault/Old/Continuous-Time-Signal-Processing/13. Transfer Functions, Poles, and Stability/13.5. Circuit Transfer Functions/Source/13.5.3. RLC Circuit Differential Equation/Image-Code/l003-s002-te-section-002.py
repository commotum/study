from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch


CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
ANNOTATION_COLOR = "#555555"
GUIDE_COLOR = "#777777"


def px_to_pt(px):
    return px * 72.0 / CANONICAL_DPI


def make_figure():
    fig, ax = plt.subplots(
        figsize=(8.8, 5.4),
        dpi=CANONICAL_DPI,
        facecolor="white",
        constrained_layout=True,
    )
    ax.set_xlim(0.0, 10.0)
    ax.set_ylim(0.0, 6.0)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    return fig, ax


def draw_line(ax, p0, p1, color=AXIS_COLOR, lw=2.2, zorder=2):
    ax.plot(
        [p0[0], p1[0]],
        [p0[1], p1[1]],
        color=color,
        linewidth=lw,
        solid_capstyle="round",
        zorder=zorder,
    )


def draw_node(ax, x, y, size=0.065):
    ax.add_patch(Circle((x, y), radius=size, facecolor=AXIS_COLOR, edgecolor=AXIS_COLOR, lw=0, zorder=4))


def draw_resistor(ax, x0, x1, y, amp=0.22, nzig=7):
    lead = 0.25
    draw_line(ax, (x0 - lead, y), (x0, y))
    draw_line(ax, (x1, y), (x1 + lead, y))

    xs = np.linspace(x0, x1, 2 * nzig + 1)
    ys = np.full_like(xs, y)
    offsets = np.array([amp if i % 2 else -amp for i in range(1, 2 * nzig)])
    ys[1:-1] = y + offsets
    ax.plot(xs, ys, color=AXIS_COLOR, linewidth=2.2, solid_capstyle="round", solid_joinstyle="miter", zorder=3)


def draw_inductor(ax, x0, x1, y, nloops=4):
    lead = 0.22
    draw_line(ax, (x0 - lead, y), (x0, y))
    draw_line(ax, (x1, y), (x1 + lead, y))

    body_x0 = x0
    seg = (x1 - x0) / nloops
    theta = np.linspace(np.pi, 0.0, 120)
    for i in range(nloops):
        cx = body_x0 + seg * (i + 0.5)
        r = seg / 2.0
        x = cx + r * np.cos(theta)
        yy = y + r * np.sin(theta)
        ax.plot(x, yy, color=AXIS_COLOR, linewidth=2.2, solid_capstyle="round", zorder=3)


def draw_capacitor(ax, x, y_top, y_bottom, plate_half_width=0.38, gap=0.30):
    mid = 0.5 * (y_top + y_bottom)
    y1 = mid + gap / 2.0
    y2 = mid - gap / 2.0
    draw_line(ax, (x, y_top), (x, y1))
    draw_line(ax, (x, y2), (x, y_bottom))
    draw_line(ax, (x - plate_half_width, y1), (x + plate_half_width, y1))
    draw_line(ax, (x - plate_half_width, y2), (x + plate_half_width, y2))


def draw_source(ax, x, y_top, y_bottom, center_y=2.75, radius=0.50):
    draw_line(ax, (x, y_top), (x, center_y + radius))
    draw_line(ax, (x, center_y - radius), (x, y_bottom))
    ax.add_patch(Circle((x, center_y), radius=radius, facecolor="white", edgecolor=AXIS_COLOR, linewidth=2.2, zorder=3))
    ax.text(x, center_y + 0.18, "+", fontsize=15, color=AXIS_COLOR, ha="center", va="center", zorder=4)
    ax.text(x, center_y - 0.20, "-", fontsize=15, color=AXIS_COLOR, ha="center", va="center", zorder=4)


def label(ax, text, x, y, *, color=LABEL_COLOR, size=12.0, ha="center", va="center", bbox=None):
    ax.text(x, y, text, fontsize=size, color=color, ha=ha, va=va, bbox=bbox)


def main():
    fig, ax = make_figure()

    top_y = 4.7
    bottom_y = 1.3
    source_x = 1.2
    resistor_x0, resistor_x1 = 2.0, 3.6
    inductor_x0, inductor_x1 = 4.25, 6.15
    cap_x = 8.0
    source_center_y = 2.75

    draw_source(ax, source_x, top_y, bottom_y, center_y=source_center_y, radius=0.50)
    draw_line(ax, (source_x, top_y), (resistor_x0 - 0.25, top_y))
    draw_resistor(ax, resistor_x0, resistor_x1, top_y)
    draw_line(ax, (resistor_x1 + 0.25, top_y), (inductor_x0 - 0.22, top_y))
    draw_inductor(ax, inductor_x0, inductor_x1, top_y)
    draw_line(ax, (inductor_x1 + 0.22, top_y), (cap_x, top_y))
    draw_capacitor(ax, cap_x, top_y, bottom_y, plate_half_width=0.40, gap=0.34)
    draw_line(ax, (cap_x, bottom_y), (source_x, bottom_y))

    for pt in [
        (source_x, top_y),
        (resistor_x0, top_y),
        (resistor_x1, top_y),
        (inductor_x0, top_y),
        (inductor_x1, top_y),
        (cap_x, top_y),
        (source_x, bottom_y),
        (cap_x, bottom_y),
    ]:
        draw_node(ax, *pt, size=0.055)

    arrow = FancyArrowPatch(
        (2.05, top_y + 0.42),
        (6.55, top_y + 0.42),
        arrowstyle="->",
        mutation_scale=16,
        linewidth=1.8,
        color=SIGNAL_COLOR,
        zorder=5,
    )
    ax.add_patch(arrow)
    label(ax, r"$i(t)$", 4.35, top_y + 0.67, color=SIGNAL_COLOR, size=12.2)

    label(ax, r"$x(t)$", source_x - 0.95, source_center_y + 0.03, color=SIGNAL_COLOR, size=13.0, ha="right")
    label(ax, r"$R$", 2.78, top_y - 0.58, size=12.0)
    label(ax, r"$L$", 5.16, top_y - 0.58, size=12.0)
    label(ax, r"$C$", cap_x + 0.58, 2.78, size=12.0, ha="left")
    label(ax, r"$y(t)$", cap_x + 1.02, 2.78, color=SIGNAL_COLOR, size=13.0, ha="left")
    label(ax, r"$+$", cap_x + 0.50, 3.35, color=ANNOTATION_COLOR, size=12.0, ha="left")
    label(ax, r"$-$", cap_x + 0.50, 2.15, color=ANNOTATION_COLOR, size=12.0, ha="left")

    label(ax, r"$v_R(t)$", 2.78, 5.10, color=ANNOTATION_COLOR, size=11.5)
    label(ax, r"$v_L(t)$", 5.16, 5.10, color=ANNOTATION_COLOR, size=11.5)
    label(ax, r"$v_C(t)$", cap_x + 0.58, 3.95, color=ANNOTATION_COLOR, size=11.5, ha="left")

    box = dict(boxstyle="round,pad=0.28", fc="white", ec="#b8b8b8", lw=1.0)
    label(
        ax,
        r"$x(t)=v_R(t)+v_L(t)+v_C(t)$",
        5.0,
        0.63,
        color=LABEL_COLOR,
        size=12.4,
        bbox=box,
    )
    label(ax, r"series KVL", 5.0, 0.30, color=GUIDE_COLOR, size=9.8)

    out = Path("/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/13.5--circuit-transfer-functions-Images/images/l003-s002-te-section-002.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=CANONICAL_DPI, bbox_inches="tight", facecolor="white")


if __name__ == "__main__":
    main()
