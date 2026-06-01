
from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

BACKGROUND_COLOR = 'white'
SIGNAL_COLOR = '#2f78b7'
AXIS_COLOR = '#222222'
LABEL_COLOR = '#444444'

DPI = 300
CANVAS_W = 8.0
CANVAS_H = 3.35

WIRE_LW = 2.45
COMPONENT_LW = 2.45
ANNOTATION_LW = 2.25

LABEL_SIZE = 18
COMPONENT_LABEL_SIZE = 18
SIGNAL_LABEL_SIZE = 17

OUTPUT_PATH = Path('/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/10.3--rc-filters-Images/images/l001-s004-te-section-004.png')
CONFIG = {'mirror': False,
 'show_input_arrow': True,
 'show_input_label': True,
 'input_label': '$v_{in}(t)$',
 'show_resistor_label': True,
 'resistor_label': '$R$',
 'show_resistor_voltage_label': False,
 'resistor_voltage_label': '$v_R(t)$',
 'show_capacitor_label': True,
 'capacitor_label': '$C$',
 'show_capacitor_voltage_label': False,
 'capacitor_voltage_label': '$v_C(t)$',
 'show_output_arrow': True,
 'output_arrow_label': '$v_{out}(t)=v_C(t)$',
 'show_output_node_label': False,
 'output_node_label': '$v_{out}(t)$',
 'show_output_node_dot': True}

plt.rcParams.update(
    {
        'mathtext.fontset': 'cm',
        'font.family': 'serif',
        'figure.facecolor': BACKGROUND_COLOR,
        'axes.facecolor': BACKGROUND_COLOR,
        'savefig.facecolor': BACKGROUND_COLOR,
        'text.color': LABEL_COLOR,
        'axes.labelcolor': LABEL_COLOR,
        'xtick.color': LABEL_COLOR,
        'ytick.color': LABEL_COLOR,
    }
)

def setup_figure():
    fig, ax = plt.subplots(figsize=(8.9, 3.8), dpi=DPI, facecolor=BACKGROUND_COLOR)
    ax.set_facecolor(BACKGROUND_COLOR)
    ax.set_xlim(0.0, CANVAS_W)
    ax.set_ylim(0.0, CANVAS_H)
    ax.set_aspect('equal', adjustable='box')
    ax.set_axis_off()
    return fig, ax

def tx(x):
    x = float(x)
    if CONFIG['mirror']:
        return CANVAS_W - x
    return x

def p(x, y):
    return (tx(x), float(y))

def side_ha():
    return 'left' if not CONFIG['mirror'] else 'right'

def draw_wire(ax, start, end, *, color=AXIS_COLOR, lw=WIRE_LW, zorder=2):
    ax.plot(
        [start[0], end[0]],
        [start[1], end[1]],
        color=color,
        linewidth=lw,
        solid_capstyle='butt',
        zorder=zorder,
    )

def draw_node(ax, point, *, size=5.2, color=AXIS_COLOR, zorder=6):
    ax.plot(
        point[0],
        point[1],
        marker='o',
        markersize=size,
        markerfacecolor=color,
        markeredgecolor=color,
        markeredgewidth=0,
        linestyle='None',
        zorder=zorder,
    )

def draw_arrow(ax, start, end, *, color=SIGNAL_COLOR, lw=ANNOTATION_LW, mutation_scale=18, zorder=6):
    ax.annotate(
        '',
        xy=end,
        xytext=start,
        arrowprops=dict(
            arrowstyle='->',
            color=color,
            lw=lw,
            mutation_scale=mutation_scale,
            shrinkA=0,
            shrinkB=0,
        ),
        annotation_clip=False,
        zorder=zorder,
    )

def draw_label(ax, x, y, text, *, color=LABEL_COLOR, size=LABEL_SIZE, ha='center', va='center', zorder=10):
    ax.text(
        x,
        y,
        text,
        fontsize=size,
        ha=ha,
        va=va,
        color=color,
        zorder=zorder,
        clip_on=False,
    )

def draw_resistor(ax, start, end, *, color=AXIS_COLOR, lw=COMPONENT_LW, zorder=3):
    start = np.asarray(start, dtype=float)
    end = np.asarray(end, dtype=float)
    delta = end - start
    length = float(np.hypot(delta[0], delta[1]))
    if length <= 1e-9:
        return
    unit = delta / length
    perp = np.array([-unit[1], unit[0]])
    lead = min(0.17 * length, 0.30)
    body = length - 2.0 * lead
    if body <= 0:
        draw_wire(ax, tuple(start), tuple(end), color=color, lw=lw, zorder=zorder)
        return
    amplitude = min(0.13, 0.22 * body)
    draw_wire(ax, tuple(start), tuple(start + lead * unit), color=color, lw=lw, zorder=zorder)
    draw_wire(ax, tuple(end - lead * unit), tuple(end), color=color, lw=lw, zorder=zorder)
    n_points = 13
    s = np.linspace(0.0, body, n_points)
    offsets = np.zeros(n_points)
    if n_points > 2:
        offsets[1:-1] = amplitude * np.where(np.arange(1, n_points - 1) % 2 == 1, 1.0, -1.0)
    pts = start + lead * unit + s[:, None] * unit + offsets[:, None] * perp
    ax.plot(
        pts[:, 0],
        pts[:, 1],
        color=color,
        linewidth=lw,
        solid_capstyle='butt',
        solid_joinstyle='miter',
        zorder=zorder,
    )

def draw_ground(ax, point, *, color=AXIS_COLOR, lw=COMPONENT_LW, zorder=2):
    x, y = point
    stem_bottom = y - 0.08
    draw_wire(ax, (x, y), (x, stem_bottom), color=color, lw=lw, zorder=zorder)
    widths = (0.38, 0.26, 0.14)
    offsets = (0.00, 0.075, 0.15)
    for width, offset in zip(widths, offsets):
        yy = stem_bottom - offset
        ax.plot(
            [x - width, x + width],
            [yy, yy],
            color=color,
            linewidth=lw,
            solid_capstyle='butt',
            zorder=zorder,
        )

def draw_capacitor_branch(ax, node_x, *, color=AXIS_COLOR, lw=COMPONENT_LW, zorder=3):
    top_y = 1.55
    plate_top_y = 1.22
    plate_bottom_y = 0.96
    ground_y = 0.68
    plate_half_width = 0.36

    draw_wire(ax, p(node_x, top_y), p(node_x, plate_top_y + 0.02), color=color, lw=lw, zorder=zorder)
    x = tx(node_x)
    ax.plot(
        [x - plate_half_width, x + plate_half_width],
        [plate_top_y, plate_top_y],
        color=color,
        linewidth=lw,
        solid_capstyle='butt',
        zorder=zorder,
    )
    ax.plot(
        [x - plate_half_width, x + plate_half_width],
        [plate_bottom_y, plate_bottom_y],
        color=color,
        linewidth=lw,
        solid_capstyle='butt',
        zorder=zorder,
    )
    draw_wire(ax, p(node_x, plate_bottom_y - 0.02), p(node_x, ground_y + 0.02), color=color, lw=lw, zorder=zorder)
    draw_ground(ax, p(node_x, ground_y), color=color, lw=lw, zorder=zorder)

def render():
    fig, ax = setup_figure()

    y_mid = 1.55
    source_start = p(0.35, y_mid)
    resistor_start = p(1.35, y_mid)
    resistor_end = p(3.35, y_mid)
    node = p(4.15, y_mid)
    input_arrow_tip = p(1.35, y_mid)
    output_arrow_x = tx(5.35)
    output_arrow_start = (output_arrow_x, 1.82)
    output_arrow_end = (output_arrow_x, 0.83)

    if CONFIG['show_input_arrow']:
        draw_arrow(ax, source_start, input_arrow_tip, color=SIGNAL_COLOR, lw=ANNOTATION_LW, mutation_scale=18)

    draw_wire(ax, resistor_start, resistor_end, color=AXIS_COLOR, lw=WIRE_LW, zorder=2)
    draw_wire(ax, resistor_end, node, color=AXIS_COLOR, lw=WIRE_LW, zorder=2)
    draw_node(ax, node, size=5.6, color=AXIS_COLOR, zorder=6)
    draw_resistor(ax, resistor_start, resistor_end, color=AXIS_COLOR, lw=COMPONENT_LW, zorder=3)
    draw_capacitor_branch(ax, node[0], color=AXIS_COLOR, lw=COMPONENT_LW, zorder=3)

    if CONFIG['show_input_label']:
        draw_label(ax, tx(0.78), 2.22, CONFIG['input_label'], color=SIGNAL_COLOR, size=SIGNAL_LABEL_SIZE, ha='center', va='bottom')

    if CONFIG['show_resistor_label']:
        draw_label(ax, tx(2.30), 1.78, CONFIG['resistor_label'], color=LABEL_COLOR, size=COMPONENT_LABEL_SIZE, ha='center', va='bottom')

    if CONFIG['show_resistor_voltage_label']:
        draw_label(ax, tx(2.30), 2.34, CONFIG['resistor_voltage_label'], color=SIGNAL_COLOR, size=SIGNAL_LABEL_SIZE, ha='center', va='bottom')

    if CONFIG['show_capacitor_label']:
        draw_label(ax, tx(4.62), 1.00, CONFIG['capacitor_label'], color=LABEL_COLOR, size=COMPONENT_LABEL_SIZE, ha=side_ha(), va='center')

    if CONFIG['show_capacitor_voltage_label']:
        draw_label(ax, tx(4.62), 1.40, CONFIG['capacitor_voltage_label'], color=SIGNAL_COLOR, size=SIGNAL_LABEL_SIZE, ha=side_ha(), va='center')

    if CONFIG['show_output_arrow']:
        draw_arrow(ax, output_arrow_start, output_arrow_end, color=SIGNAL_COLOR, lw=ANNOTATION_LW, mutation_scale=18)
        if CONFIG['output_arrow_label']:
            draw_label(
                ax,
                tx(5.45),
                1.83,
                CONFIG['output_arrow_label'],
                color=SIGNAL_COLOR,
                size=SIGNAL_LABEL_SIZE,
                ha=side_ha(),
                va='bottom',
            )
    elif CONFIG['show_output_node_label']:
        draw_label(
            ax,
            node[0],
            2.06,
            CONFIG['output_node_label'],
            color=SIGNAL_COLOR,
            size=SIGNAL_LABEL_SIZE,
            ha='center',
            va='bottom',
        )

    if CONFIG['show_output_node_dot']:
        draw_node(ax, node, size=5.2, color=AXIS_COLOR, zorder=7)

    fig.savefig(
        OUTPUT_PATH,
        dpi=DPI,
        bbox_inches='tight',
        facecolor=BACKGROUND_COLOR,
        pad_inches=0.08,
    )
    plt.close(fig)

if __name__ == '__main__':
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    render()
