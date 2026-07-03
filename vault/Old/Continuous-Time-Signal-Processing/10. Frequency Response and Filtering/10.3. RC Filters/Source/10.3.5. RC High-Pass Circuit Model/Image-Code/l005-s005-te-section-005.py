
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

CANONICAL_DPI = 300
BACKGROUND_COLOR = "white"
LINE_COLOR = "#222222"
LABEL_COLOR = "#222222"
NOTE_COLOR = "#555555"

def px_to_pt(px):
    return px * 72 / CANONICAL_DPI

WIRE_LW = px_to_pt(4.3)
COMPONENT_LW = px_to_pt(4.3)
NODE_SIZE = px_to_pt(10.5)
OPEN_SIZE = px_to_pt(18.0)
ENDPOINT_EDGE = px_to_pt(5.1)
LABEL_SIZE = px_to_pt(31.0)
SMALL_LABEL_SIZE = px_to_pt(27.0)
NOTE_SIZE = px_to_pt(29.0)
ARROW_MS = 18

OUTPUT_PATH = Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/10.3--rc-filters-Images/images/l005-s005-te-section-005.png')
SCENE = {'layout': 'comparison', 'figsize': [12.4, 4.8], 'panels': [{'layout': 'single', 'kind': 'high-pass', 'mirror': False, 'show_source_label': True, 'show_input_arrow': False, 'show_output_arrow': True, 'show_output_node_label': False, 'output_target': 'shunt', 'swap_labels': False, 'note_text': None, 'panel_title': None, 'source_text': '$v_{in}(t)$', 'output_text': '$v_{out}(t)$', 'show_component_labels': True, 'figsize': [5.9, 4.8]}, {'layout': 'single', 'kind': 'low-pass', 'mirror': False, 'show_source_label': True, 'show_input_arrow': False, 'show_output_arrow': True, 'show_output_node_label': False, 'output_target': 'shunt', 'swap_labels': False, 'note_text': None, 'panel_title': None, 'source_text': '$v_{in}(t)$', 'output_text': '$v_{out}(t)$', 'show_component_labels': True, 'figsize': [5.9, 4.8]}]}

def save_figure(fig, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=CANONICAL_DPI, bbox_inches="tight", facecolor=BACKGROUND_COLOR)
    plt.close(fig)

def make_figure(figsize):
    return plt.subplots(figsize=figsize, dpi=CANONICAL_DPI, facecolor=BACKGROUND_COLOR, constrained_layout=True)

def setup_panel(ax, xlim=(0.0, 12.0), ylim=(0.1, 4.95)):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

def mirror_x(x, mirror=False, width=12.0):
    return width - x if mirror else x

def draw_wire(ax, start, end, *, color=LINE_COLOR, lw=WIRE_LW, zorder=2):
    ax.plot([start[0], end[0]], [start[1], end[1]], color=color, linewidth=lw, solid_capstyle="butt", zorder=zorder)

def draw_node(ax, x, y, *, size=NODE_SIZE, color=LINE_COLOR, zorder=6):
    ax.plot(x, y, marker="o", markersize=size, markerfacecolor=color, markeredgecolor=color, markeredgewidth=0, linestyle="None", zorder=zorder)

def draw_open_node(ax, x, y, *, size=OPEN_SIZE, color=LINE_COLOR, zorder=6):
    ax.plot(x, y, marker="o", markersize=size, markerfacecolor="white", markeredgecolor=color, markeredgewidth=ENDPOINT_EDGE, linestyle="None", zorder=zorder)

def draw_source(ax, x, y, *, label=None, show_polarity=True):
    draw_open_node(ax, x, y)
    if show_polarity:
        ax.text(x, y + 0.14, r"$+$", fontsize=SMALL_LABEL_SIZE, ha="center", va="center", color=LABEL_COLOR, zorder=7)
        ax.text(x, y - 0.14, r"$-$", fontsize=SMALL_LABEL_SIZE, ha="center", va="center", color=LABEL_COLOR, zorder=7)
    if label is not None:
        ax.text(x, y + 0.55, label, fontsize=LABEL_SIZE, ha="center", va="bottom", color=LABEL_COLOR, zorder=7)

def draw_label(ax, x, y, text, *, size=LABEL_SIZE, ha="center", va="center", color=LABEL_COLOR, zorder=7):
    ax.text(x, y, text, fontsize=size, ha=ha, va=va, color=color, zorder=zorder)

def draw_arrow(ax, start, end, *, color=LINE_COLOR, lw=COMPONENT_LW, label=None, label_side="above", label_offset=0.20, zorder=5):
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops=dict(arrowstyle="->", color=color, lw=lw, mutation_scale=ARROW_MS, shrinkA=0, shrinkB=0),
        annotation_clip=False,
        zorder=zorder,
    )
    if label is not None:
        midx = (start[0] + end[0]) / 2.0
        midy = (start[1] + end[1]) / 2.0
        if label_side == "above":
            draw_label(ax, midx, midy + label_offset, label, size=LABEL_SIZE, ha="center", va="bottom", color=LABEL_COLOR)
        elif label_side == "below":
            draw_label(ax, midx, midy - label_offset, label, size=LABEL_SIZE, ha="center", va="top", color=LABEL_COLOR)
        elif label_side == "left":
            draw_label(ax, midx - label_offset, midy, label, size=LABEL_SIZE, ha="right", va="center", color=LABEL_COLOR)
        else:
            draw_label(ax, midx + label_offset, midy, label, size=LABEL_SIZE, ha="left", va="center", color=LABEL_COLOR)

def _frame(start, end):
    p0 = np.asarray(start, dtype=float)
    p1 = np.asarray(end, dtype=float)
    delta = p1 - p0
    length = float(np.hypot(delta[0], delta[1]))
    if length <= 0:
        raise ValueError("start and end must differ")
    unit = delta / length
    perp = np.array([-unit[1], unit[0]])
    return p0, p1, unit, perp, length

def draw_resistor(ax, start, end, *, lead_fraction=0.18, zigzags=6, color=LINE_COLOR, lw=COMPONENT_LW, zorder=3):
    p0, p1, unit, perp, length = _frame(start, end)
    if zigzags < 1:
        draw_wire(ax, p0, p1, color=color, lw=lw, zorder=zorder)
        return
    lead = min(lead_fraction * length, 0.35 * length)
    body_length = length - 2 * lead
    if body_length <= 0:
        draw_wire(ax, p0, p1, color=color, lw=lw, zorder=zorder)
        return
    draw_wire(ax, p0, p0 + lead * unit, color=color, lw=lw, zorder=zorder)
    draw_wire(ax, p1 - lead * unit, p1, color=color, lw=lw, zorder=zorder)
    body_points = 2 * zigzags + 1
    s = np.linspace(0.0, body_length, body_points)
    offsets = np.zeros(body_points)
    if body_points > 2:
        offsets[1:-1] = min(px_to_pt(7.5) / 20.0, 0.24 * body_length) * np.where(np.arange(1, body_points - 1) % 2 == 1, 1.0, -1.0)
    pts = p0 + lead * unit + s[:, None] * unit + offsets[:, None] * perp
    ax.plot(pts[:, 0], pts[:, 1], color=color, linewidth=lw, solid_capstyle="butt", solid_joinstyle="miter", zorder=zorder)

def draw_capacitor(ax, start, end, *, lead_fraction=0.22, plate_span=None, color=LINE_COLOR, lw=COMPONENT_LW, zorder=3):
    p0, p1, unit, perp, length = _frame(start, end)
    lead = min(lead_fraction * length, 0.38 * length)
    if 2 * lead >= length:
        draw_wire(ax, p0, p1, color=color, lw=lw, zorder=zorder)
        return
    if plate_span is None:
        plate_span = 0.75 * length
    half_span = 0.5 * min(plate_span, 0.75 * length)
    left_center = p0 + lead * unit
    right_center = p1 - lead * unit
    draw_wire(ax, p0, left_center, color=color, lw=lw, zorder=zorder)
    draw_wire(ax, right_center, p1, color=color, lw=lw, zorder=zorder)
    for center in (left_center, right_center):
        a = center - half_span * perp
        b = center + half_span * perp
        ax.plot([a[0], b[0]], [a[1], b[1]], color=color, linewidth=lw, solid_capstyle="butt", zorder=zorder + 1)

def draw_ground(ax, x, y, *, color=LINE_COLOR, lw=COMPONENT_LW, zorder=2):
    stem = 0.30
    width = 0.66
    step = 0.12
    base_y = y - stem
    draw_wire(ax, (x, y), (x, base_y), color=color, lw=lw, zorder=zorder)
    for idx, frac in enumerate((1.0, 0.68, 0.36)):
        yy = base_y - idx * step
        half = 0.5 * width * frac
        ax.plot([x - half, x + half], [yy, yy], color=color, linewidth=lw, solid_capstyle="butt", zorder=zorder)

def draw_horizontal_arrow(ax, x0, x1, y, *, label=None, label_side="above", color=LINE_COLOR, lw=COMPONENT_LW, zorder=5):
    draw_arrow(ax, (x0, y), (x1, y), color=color, lw=lw, label=label, label_side=label_side, label_offset=0.18, zorder=zorder)

def draw_vertical_arrow(ax, x, y0, y1, *, label=None, label_side="right", color=LINE_COLOR, lw=COMPONENT_LW, zorder=5):
    draw_arrow(ax, (x, y0), (x, y1), color=color, lw=lw, label=label, label_side=label_side, label_offset=0.26, zorder=zorder)

def draw_filter(ax, scene):
    kind = scene["kind"]
    mirror = scene.get("mirror", False)
    source_text = scene.get("source_text", r"$v_{in}(t)$")
    output_text = scene.get("output_text", r"$v_{out}(t)$")
    if scene.get("swap_labels", False):
        source_text, output_text = output_text, source_text

    show_source_label = scene.get("show_source_label", True)
    show_input_arrow = scene.get("show_input_arrow", False)
    show_output_arrow = scene.get("show_output_arrow", False)
    show_output_node_label = scene.get("show_output_node_label", False)
    show_component_labels = scene.get("show_component_labels", True)
    output_target = scene.get("output_target", "shunt")
    note_text = scene.get("note_text")
    panel_title = scene.get("panel_title")

    WIDTH = 12.0
    Y_MAIN = 2.85
    Y_GND = 0.78
    X_SOURCE = 1.40
    X_IN = 2.12
    X_SERIES_A = 2.58
    X_SERIES_B = 5.05
    X_NODE = 6.15
    X_NOTE = 8.15

    if panel_title:
        draw_label(ax, WIDTH / 2.0, 4.60, panel_title, size=SMALL_LABEL_SIZE, ha="center", va="bottom", color=LABEL_COLOR)
    if note_text:
        draw_label(ax, X_NOTE, 4.20, note_text, size=NOTE_SIZE, ha="left", va="top", color=NOTE_COLOR)

    mx = lambda value: mirror_x(value, mirror=mirror, width=WIDTH)
    src_x = mx(X_SOURCE)
    in_x = mx(X_IN)
    series_a = mx(X_SERIES_A)
    series_b = mx(X_SERIES_B)
    node_x = mx(X_NODE)

    draw_source(ax, src_x, Y_MAIN, label=source_text if show_source_label else None)
    draw_wire(ax, (src_x + (-0.16 if mirror else 0.16), Y_MAIN), (in_x, Y_MAIN))

    if kind == "high-pass":
        draw_capacitor(ax, (in_x, Y_MAIN), (series_b, Y_MAIN) if not mirror else (series_a, Y_MAIN))
        draw_wire(ax, ((series_b if not mirror else series_a), Y_MAIN), (node_x, Y_MAIN))
        draw_resistor(ax, (node_x, Y_MAIN), (node_x, Y_GND))
        if show_component_labels:
            draw_label(ax, (in_x + (series_b if not mirror else series_a)) / 2.0, Y_MAIN + 0.55, r"$C$", size=SMALL_LABEL_SIZE, ha="center", va="bottom")
            draw_label(ax, node_x + (-0.62 if mirror else 0.62), (Y_MAIN + Y_GND) / 2.0, r"$R$", size=SMALL_LABEL_SIZE, ha="right" if mirror else "left", va="center")
    else:
        draw_resistor(ax, (in_x, Y_MAIN), (series_b, Y_MAIN) if not mirror else (series_a, Y_MAIN))
        draw_wire(ax, ((series_b if not mirror else series_a), Y_MAIN), (node_x, Y_MAIN))
        draw_capacitor(ax, (node_x, Y_MAIN), (node_x, Y_GND))
        if show_component_labels:
            draw_label(ax, (in_x + (series_b if not mirror else series_a)) / 2.0, Y_MAIN + 0.55, r"$R$", size=SMALL_LABEL_SIZE, ha="center", va="bottom")
            draw_label(ax, node_x + (-0.62 if mirror else 0.62), (Y_MAIN + Y_GND) / 2.0, r"$C$", size=SMALL_LABEL_SIZE, ha="right" if mirror else "left", va="center")

    draw_node(ax, node_x, Y_MAIN)
    draw_ground(ax, node_x, Y_GND)

    if show_input_arrow:
        arrow_start = src_x + (-0.55 if mirror else 0.55)
        arrow_end = in_x + (0.06 if mirror else -0.06)
        draw_horizontal_arrow(ax, arrow_start, arrow_end, Y_MAIN + 0.46, label=source_text, label_side="above")
    if show_output_arrow:
        if output_target == "series":
            arrow_start = series_a
            arrow_end = series_b
            arrow_y = Y_MAIN + 0.46
            draw_horizontal_arrow(ax, arrow_start, arrow_end, arrow_y, label=output_text, label_side="above")
        else:
            arrow_x = node_x + (-0.64 if mirror else 0.64)
            draw_vertical_arrow(ax, arrow_x, Y_MAIN, Y_GND, label=output_text, label_side="left" if mirror else "right")
    elif show_output_node_label:
        draw_label(ax, node_x, Y_MAIN + 0.55, output_text, size=LABEL_SIZE, ha="center", va="bottom", color=LABEL_COLOR)

def draw_comparison(fig, panels):
    axes = [fig.add_subplot(1, 2, idx + 1) for idx in range(2)]
    for ax, scene in zip(axes, panels):
        setup_panel(ax)
        draw_filter(ax, scene)
    return axes

def render_scene(scene):
    if scene["layout"] == "comparison":
        fig = plt.figure(figsize=tuple(scene.get("figsize", (12.5, 4.8))), dpi=CANONICAL_DPI, facecolor=BACKGROUND_COLOR, constrained_layout=True)
        draw_comparison(fig, scene["panels"])
    else:
        fig, ax = make_figure(tuple(scene.get("figsize", (8.6, 4.6))))
        setup_panel(ax)
        draw_filter(ax, scene)
    save_figure(fig, OUTPUT_PATH)

def main():
    render_scene(SCENE)

if __name__ == "__main__":
    main()
