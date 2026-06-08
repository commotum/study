from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


plt.rcParams.update(
    {
        "mathtext.fontset": "cm",
        "font.family": "serif",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)


DPI = 300
BLUE = "#2f78b7"
WIRE = "#222222"
TEXT = "#444444"
BOX_EDGE = "#cfcfcf"

FIGSIZE = (10.2, 4.9)
XMIN, XMAX = 0.0, 11.4
YMIN, YMAX = -2.8, 2.8

INPUT_X = 1.15
SERIES_START_X = 2.05
SERIES_END_X = 5.00
GROUND_Y = -1.55
NODE_Y = 0.0


SCENES = {
    "l002-s001-te-section-image-01": {
        "input_label": r"$V_{in}$",
        "output_label": r"$V_o$",
        "topology": "lowpass",
        "box_lines": [
            "s-domain RC workflow",
            r"$Z_C=\frac{1}{sC}$",
            r"$H(s)=\frac{V_o(s)}{V_i(s)}$",
        ],
    },
    "l002-s002-te-section-image-02": {
        "input_label": r"$V_i$",
        "output_label": r"$V_o$",
        "topology": "lowpass",
        "box_lines": [
            "voltage divider",
            r"$Z_C=\frac{1}{sC}$",
            r"$H(s)=\frac{Z_C}{R+Z_C}$",
        ],
    },
    "l002-s003-te-section-image-03": {
        "input_label": r"$V_i$",
        "output_label": r"$V_o$",
        "topology": "lowpass",
        "box_lines": [
            "low-pass form",
            r"$H(s)=\frac{1}{1+sRC}$",
            r"$|H(j\omega)|\to 0\ \;(\omega\to\infty)$",
        ],
    },
    "l002-s004-te-section-image-04": {
        "input_label": r"$V_i$",
        "output_label": r"$V_o$",
        "topology": "highpass",
        "box_lines": [
            "output across $R$",
            r"$H(s)=\frac{sRC}{1+sRC}$",
            r"$H(0)=0,\ \ H(\infty)=1$",
        ],
    },
}


def make_figure():
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI, facecolor="white", constrained_layout=True)
    ax.set_xlim(XMIN, XMAX)
    ax.set_ylim(YMIN, YMAX)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")
    return fig, ax


def draw_wire(ax, x1, y1, x2, y2, lw=2.2):
    ax.plot([x1, x2], [y1, y2], color=WIRE, lw=lw, solid_capstyle="round", zorder=1)


def draw_node(ax, x, y, radius=0.07):
    ax.add_patch(Circle((x, y), radius=radius, facecolor=BLUE, edgecolor=BLUE, zorder=4))


def draw_ground(ax, x, y_top, width=0.44, spacing=0.11, lw=1.9):
    stem = 0.24
    draw_wire(ax, x, y_top, x, y_top - stem, lw=lw)
    y = y_top - stem
    ax.plot([x - width / 2, x + width / 2], [y, y], color=WIRE, lw=lw, zorder=1)
    ax.plot([x - width * 0.33, x + width * 0.33], [y - spacing, y - spacing], color=WIRE, lw=lw, zorder=1)
    ax.plot([x - width * 0.16, x + width * 0.16], [y - 2 * spacing, y - 2 * spacing], color=WIRE, lw=lw, zorder=1)


def draw_horizontal_resistor(ax, x1, x2, y=0.0, amp=0.23, nzig=6, lw=2.0):
    lead = 0.22
    left = x1 + lead
    right = x2 - lead
    draw_wire(ax, x1, y, left, y, lw=lw)
    draw_wire(ax, right, y, x2, y, lw=lw)
    xs = np.linspace(left, right, 2 * nzig + 1)
    ys = np.full_like(xs, y)
    for i in range(1, len(xs) - 1):
        ys[i] = y + amp if i % 2 else y - amp
    ax.plot(xs, ys, color=WIRE, lw=lw, solid_capstyle="round", solid_joinstyle="miter", zorder=2)


def draw_horizontal_capacitor(ax, x1, x2, y=0.0, gap=0.19, plate_h=0.68, lw=2.0):
    lead = 0.28
    left_plate = x1 + lead
    right_plate = left_plate + gap
    draw_wire(ax, x1, y, left_plate, y, lw=lw)
    draw_wire(ax, right_plate, y, x2, y, lw=lw)
    ax.plot([left_plate, left_plate], [y - plate_h / 2, y + plate_h / 2], color=WIRE, lw=lw, zorder=2)
    ax.plot([right_plate, right_plate], [y - plate_h / 2, y + plate_h / 2], color=WIRE, lw=lw, zorder=2)


def draw_vertical_capacitor(ax, x, y_top=0.0, y_bottom=GROUND_Y, gap=0.19, plate_w=0.68, lw=2.0):
    lead = 0.28
    top_plate = y_top - lead
    bottom_plate = top_plate - gap
    draw_wire(ax, x, y_top, x, top_plate, lw=lw)
    draw_wire(ax, x, bottom_plate, x, y_bottom + 0.28, lw=lw)
    ax.plot([x - plate_w / 2, x + plate_w / 2], [top_plate, top_plate], color=WIRE, lw=lw, zorder=2)
    ax.plot([x - plate_w / 2, x + plate_w / 2], [bottom_plate, bottom_plate], color=WIRE, lw=lw, zorder=2)
    draw_ground(ax, x, y_bottom + 0.28, lw=lw)


def draw_vertical_resistor(ax, x, y_top=0.0, y_bottom=GROUND_Y, amp=0.23, nzig=6, lw=2.0):
    lead = 0.22
    top = y_top - lead
    bottom = y_bottom + 0.22
    draw_wire(ax, x, y_top, x, top, lw=lw)
    draw_wire(ax, x, bottom, x, y_bottom + 0.22, lw=lw)
    ys = np.linspace(top, bottom, 2 * nzig + 1)
    xs = np.full_like(ys, x)
    for i in range(1, len(ys) - 1):
        xs[i] = x + amp if i % 2 else x - amp
    ax.plot(xs, ys, color=WIRE, lw=lw, solid_capstyle="round", solid_joinstyle="miter", zorder=2)
    draw_ground(ax, x, y_bottom + 0.22, lw=lw)


def place_label(ax, text, x, y, color=TEXT, size=18, ha="center", va="center"):
    ax.text(x, y, text, color=color, fontsize=size, ha=ha, va=va, zorder=5)


def draw_callout(ax, lines):
    text = "\n".join(lines)
    ax.text(
        6.55,
        2.05,
        text,
        color=TEXT,
        fontsize=16.8,
        ha="left",
        va="top",
        linespacing=1.35,
        bbox=dict(boxstyle="round,pad=0.36", facecolor="white", edgecolor=BOX_EDGE, linewidth=1.1),
        zorder=6,
    )


def render_scene(scene_key):
    scene = SCENES[scene_key]
    fig, ax = make_figure()

    # Input node and reference ground.
    draw_node(ax, INPUT_X, NODE_Y)
    draw_wire(ax, INPUT_X, NODE_Y, INPUT_X, GROUND_Y + 0.28)
    draw_ground(ax, INPUT_X, GROUND_Y + 0.28)
    place_label(ax, scene["input_label"], INPUT_X, 0.52, color=BLUE, size=19)

    # Shared left-to-right branch geometry.
    draw_wire(ax, INPUT_X + 0.07, NODE_Y, SERIES_START_X, NODE_Y)

    if scene["topology"] == "lowpass":
        draw_horizontal_resistor(ax, SERIES_START_X, SERIES_END_X, NODE_Y)
        draw_wire(ax, SERIES_END_X, NODE_Y, SERIES_END_X + 0.12, NODE_Y)
        draw_node(ax, SERIES_END_X + 0.12, NODE_Y)
        draw_vertical_capacitor(ax, SERIES_END_X + 0.12, NODE_Y, GROUND_Y)
        place_label(ax, r"$R$", 3.46, 0.56, color=TEXT, size=18)
        place_label(ax, r"$C$", SERIES_END_X + 0.62, -0.22, color=TEXT, size=18)
        place_label(ax, scene["output_label"], SERIES_END_X + 0.12, 0.52, color=BLUE, size=19)
    else:
        draw_horizontal_capacitor(ax, SERIES_START_X, SERIES_END_X, NODE_Y)
        draw_wire(ax, SERIES_END_X, NODE_Y, SERIES_END_X + 0.12, NODE_Y)
        draw_node(ax, SERIES_END_X + 0.12, NODE_Y)
        draw_vertical_resistor(ax, SERIES_END_X + 0.12, NODE_Y, GROUND_Y)
        place_label(ax, r"$C$", 3.46, 0.56, color=TEXT, size=18)
        place_label(ax, r"$R$", SERIES_END_X + 0.62, -0.22, color=TEXT, size=18)
        place_label(ax, scene["output_label"], SERIES_END_X + 0.12, 0.52, color=BLUE, size=19)

    draw_callout(ax, scene["box_lines"])

    return fig


def main():
    stem = Path(__file__).stem
    if stem not in SCENES:
        raise KeyError(f"Unknown scene key: {stem}")

    fig = render_scene(stem)
    image_path = Path(__file__).resolve().parents[1] / "images" / f"{stem}.png"
    image_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(image_path, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
