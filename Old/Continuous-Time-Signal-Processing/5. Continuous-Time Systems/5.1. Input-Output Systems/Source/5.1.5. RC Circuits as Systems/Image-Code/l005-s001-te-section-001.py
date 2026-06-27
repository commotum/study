from __future__ import annotations

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use("Agg")

plt.rcParams.update(
    {
        "mathtext.fontset": "cm",
        "font.family": "serif",
    }
)

CANVAS_W = 8.9
CANVAS_H = 3.35
DPI = 300

OUTPUT_PATH = Path("/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/5.1--input-output-systems-Images/images/l005-s001-te-section-001.png")

BACKGROUND_COLOR = "white"
LINE_COLOR = "#222222"
SIGNAL_COLOR = "#2f78b7"
LABEL_COLOR = "#444444"

WIRE_LW = 2.45
COMPONENT_LW = 2.45
ANNOTATION_LW = 2.25

TEXT_SIZE = 18
LABEL_SIZE = 18
SIGNAL_LABEL_SIZE = 17

INPUT_LABEL = "$v_s(t)$"
RESISTOR_COMPONENT_LABEL = "$R$"
CAPACITOR_COMPONENT_LABEL = "$C$"
SHOW_VR_LABEL = False
SHOW_VC_LABEL = True
VR_LABEL_TEXT = "$v_R(t)$"
VC_LABEL_TEXT = "$v_C(t)$"
SOURCE_HIGHLIGHT = False
CAP_BRANCH_HIGHLIGHT = False
RES_BRANCH_HIGHLIGHT = False
SHOW_POLARITY_HINT = False


def draw_line(ax, start, end, *, color=LINE_COLOR, lw=WIRE_LW, zorder=2):
    ax.plot([start[0], end[0]], [start[1], end[1]], color=color, linewidth=lw, solid_capstyle="butt", zorder=zorder)


def draw_node(ax, point, *, size=5.2, color=LINE_COLOR, zorder=6):
    ax.plot(point[0], point[1], marker="o", markersize=size, markerfacecolor=color, markeredgecolor=color, markeredgewidth=0, linestyle="None", zorder=zorder)


def draw_arrow(ax, start, end, *, color=SIGNAL_COLOR, lw=ANNOTATION_LW, mutation_scale=18, zorder=6):
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops=dict(
            arrowstyle="->",
            color=color,
            lw=lw,
            mutation_scale=mutation_scale,
            shrinkA=0,
            shrinkB=0,
        ),
        annotation_clip=False,
        zorder=zorder,
    )


def draw_label(ax, x, y, text, *, color=LABEL_COLOR, size=TEXT_SIZE, ha="center", va="center", zorder=10):
    ax.text(x, y, text, fontsize=size, ha=ha, va=va, color=color, zorder=zorder, clip_on=False)


def draw_resistor(ax, start, end, *, color=LINE_COLOR, lw=COMPONENT_LW, zorder=3):
    start = np.asarray(start, dtype=float)
    end = np.asarray(end, dtype=float)
    delta = end - start
    length = float(np.hypot(delta[0], delta[1]))
    if length <= 1e-9:
        return
    unit = delta / length
    lead = min(0.17 * length, 0.30)
    body = length - 2.0 * lead
    if body <= 0:
        draw_line(ax, tuple(start), tuple(end), color=color, lw=lw, zorder=zorder)
        return
    amplitude = min(0.13, 0.22 * body)
    perp = np.array([-unit[1], unit[0]])
    draw_line(ax, tuple(start), tuple(start + lead * unit), color=color, lw=lw, zorder=zorder)
    draw_line(ax, tuple(end - lead * unit), tuple(end), color=color, lw=lw, zorder=zorder)
    n_points = 13
    s = np.linspace(0.0, body, n_points)
    offsets = np.zeros(n_points)
    if n_points > 2:
        offsets[1:-1] = amplitude * np.where(np.arange(1, n_points - 1) % 2 == 1, 1.0, -1.0)
    pts = start + lead * unit + s[:, None] * unit + offsets[:, None] * perp
    ax.plot(pts[:, 0], pts[:, 1], color=color, linewidth=lw, solid_capstyle="butt", solid_joinstyle="miter", zorder=zorder)


def draw_source_symbol(ax, left_x, right_x, y, *, color=LINE_COLOR, lw=1.6):
    cx = 0.5 * (left_x + right_x)
    radius = 0.21
    circle = plt.Circle((cx, y), radius, fill=False, linewidth=lw, color=color, zorder=3)
    ax.add_patch(circle)
    ax.plot([left_x - 0.05, left_x], [y, y], color=color, linewidth=WIRE_LW, solid_capstyle="butt", zorder=3)
    ax.plot([right_x, right_x + 0.05], [y, y], color=color, linewidth=WIRE_LW, solid_capstyle="butt", zorder=3)
    draw_label(ax, cx, y + 0.24, "+", color=color, size=17, ha="center", va="center", zorder=9)
    draw_label(ax, cx, y - 0.28, "-", color=color, size=17, ha="center", va="center", zorder=9)


def draw_capacitor(ax, node_x, *, color=LINE_COLOR, lw=COMPONENT_LW, zorder=3):
    y_top = 1.55
    y_plate_top = 1.22
    y_plate_bottom = 0.96
    y_ground = 0.68
    half_plate = 0.36

    draw_line(ax, (node_x, y_top), (node_x, y_plate_top + 0.02), color=color, lw=lw, zorder=zorder)
    ax.plot([node_x - half_plate, node_x + half_plate], [y_plate_top, y_plate_top], color=color, linewidth=lw, solid_capstyle="butt", zorder=zorder)
    ax.plot([node_x - half_plate, node_x + half_plate], [y_plate_bottom, y_plate_bottom], color=color, linewidth=lw, solid_capstyle="butt", zorder=zorder)
    draw_line(ax, (node_x, y_plate_bottom - 0.02), (node_x, y_ground + 0.02), color=color, lw=lw, zorder=zorder)


def draw_ground(ax, point, *, color=LINE_COLOR, lw=COMPONENT_LW, zorder=2):
    x, y = point
    y_stem_bottom = y - 0.08
    draw_line(ax, (x, y), (x, y_stem_bottom), color=color, lw=lw, zorder=zorder)
    widths = (0.38, 0.26, 0.14)
    offsets = (0.00, 0.075, 0.15)
    for width, offset in zip(widths, offsets):
        yy = y_stem_bottom - offset
        ax.plot([x - width, x + width], [yy, yy], color=color, linewidth=lw, solid_capstyle="butt", zorder=zorder)


def highlight_region(ax, x0, x1, y0, y1, *, color=SIGNAL_COLOR, lw=3.0, zorder=1):
    rect = plt.Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, linewidth=lw, linestyle="--", color=color, alpha=0.45, zorder=zorder)
    ax.add_patch(rect)


def draw_scene():
    fig, ax = plt.subplots(figsize=(CANVAS_W, CANVAS_H), dpi=DPI, facecolor=BACKGROUND_COLOR)
    ax.set_xlim(0.0, CANVAS_W)
    ax.set_ylim(0.0, CANVAS_H)
    ax.set_aspect("equal", adjustable="box")
    ax.set_axis_off()

    y_main = 1.55
    x_wire_in = 0.35
    x_source_left = 0.82
    x_source_right = 1.42
    x_source_to_res = 1.52
    x_res_start = 1.64
    x_res_end = 3.44
    x_node = 4.24

    # Optional highlighting for input/output emphasis.
    if SOURCE_HIGHLIGHT:
        highlight_region(ax, 0.58, 1.64, 1.24, 1.86, color=SIGNAL_COLOR)

    if RES_BRANCH_HIGHLIGHT:
        highlight_region(ax, x_source_to_res, x_res_end, y_main - 0.26, y_main + 0.26, color=SIGNAL_COLOR)

    if CAP_BRANCH_HIGHLIGHT:
        highlight_region(ax, x_node - 0.42, x_node + 0.42, 0.61, 1.75, color=SIGNAL_COLOR)

    # Input source + series branch.
    draw_line(ax, (x_wire_in, y_main), (x_source_left - 0.08, y_main), color=LINE_COLOR, lw=WIRE_LW, zorder=2)
    draw_source_symbol(ax, x_source_left, x_source_right, y_main)
    draw_line(ax, (x_source_right, y_main), (x_source_to_res, y_main), color=LINE_COLOR, lw=WIRE_LW, zorder=2)
    draw_line(ax, (x_source_to_res, y_main), (x_res_start, y_main), color=LINE_COLOR, lw=WIRE_LW, zorder=2)

    # Input-arrow and label.
    draw_arrow(ax, (0.20, y_main), (x_wire_in, y_main), color=SIGNAL_COLOR, lw=ANNOTATION_LW)
    draw_label(ax, 0.72, 2.24, INPUT_LABEL, color=SIGNAL_COLOR, size=SIGNAL_LABEL_SIZE, ha="center", va="center")

    # Resistor and node.
    draw_resistor(ax, (x_res_start, y_main), (x_res_end, y_main))
    draw_line(ax, (x_res_end, y_main), (x_node, y_main))
    draw_node(ax, (x_node, y_main), size=5.6)

    # Capacitor branch and reference ground.
    draw_capacitor(ax, x_node)
    ground_y = 0.68
    draw_ground(ax, (x_node, ground_y))

    # Component labels.
    draw_label(ax, 0.5 * (x_source_left + x_source_right), 0.98, INPUT_LABEL, color=SIGNAL_COLOR, size=13, ha="center", va="center")
    draw_label(ax, 2.54, 1.89, RESISTOR_COMPONENT_LABEL, color=LABEL_COLOR, size=LABEL_SIZE, ha="center", va="center")
    draw_label(ax, x_node + 0.34, 1.00, CAPACITOR_COMPONENT_LABEL, color=LABEL_COLOR, size=LABEL_SIZE, ha="left", va="center")

    if SHOW_VR_LABEL:
        draw_label(ax, 2.54, 2.42, VR_LABEL_TEXT, color=SIGNAL_COLOR, size=SIGNAL_LABEL_SIZE, ha="center", va="center")

    if SHOW_VC_LABEL:
        draw_label(ax, x_node + 0.46, 1.32, VC_LABEL_TEXT, color=SIGNAL_COLOR, size=SIGNAL_LABEL_SIZE, ha="left", va="center")

    # Current and equation-view hints.
    draw_arrow(ax, (x_node + 0.06, 2.03), (x_node + 0.06, 1.05), color=SIGNAL_COLOR, lw=ANNOTATION_LW)
    draw_label(ax, x_node + 0.05, 1.20, "$i(t)$", color=SIGNAL_COLOR, size=SIGNAL_LABEL_SIZE, ha="left", va="center")

    if SHOW_POLARITY_HINT:
        draw_label(ax, 2.53, 1.78, "$v_R(t)$", color=SIGNAL_COLOR, size=12, ha="left", va="center")
        draw_label(ax, x_node + 0.47, 1.76, "$v_C(t)$", color=SIGNAL_COLOR, size=12, ha="left", va="center")
        ax.annotate(
            "",
            xy=(2.95, 1.78),
            xytext=(0.95, 1.78),
            arrowprops=dict(arrowstyle="->", color=SIGNAL_COLOR, lw=1.4, mutation_scale=9, shrinkA=0, shrinkB=0),
            annotation_clip=False,
            zorder=6,
        )
        draw_label(ax, 2.10, 1.96, "$v_s(t)$", color=SIGNAL_COLOR, size=12, ha="left", va="center")

    Path(OUTPUT_PATH).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH, dpi=DPI, bbox_inches="tight", facecolor=BACKGROUND_COLOR)
    plt.close(fig)


if __name__ == "__main__":
    draw_scene()
