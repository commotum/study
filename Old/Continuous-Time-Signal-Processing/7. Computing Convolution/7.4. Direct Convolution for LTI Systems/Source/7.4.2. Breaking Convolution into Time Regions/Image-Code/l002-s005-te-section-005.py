from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'mathtext.fontset': 'cm',
    'font.family': 'serif',
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'savefig.facecolor': 'white',
})

SIGNAL_COLOR = '#2f78b7'
AXIS_COLOR = '#222222'
LABEL_COLOR = '#444444'
TICK_LABEL_COLOR = '#444444'
GRID_COLOR = '#000000'
GUIDE_COLOR = '#777777'
ANNOTATION_COLOR = '#555555'

SIGNAL_LW = 3.2
AXIS_LW = 1.4
TICK_LW = 1.2
GRID_LW = 0.6
GUIDE_LW = 1.5

TICK_LABEL_SIZE = 16
AXIS_LABEL_SIZE = 24
TOP_LABEL_SIZE = 26
ANNOTATION_SIZE = 15

TICK_HALF_LEN = 0.055
OPEN_MARKER_SIZE = 9
CLOSED_MARKER_SIZE = 8
ENDPOINT_EDGEWIDTH = 2.3

AXIS_ARROW_KW = dict(
    angles='xy',
    scale_units='xy',
    scale=1,
    width=0.0048,
    headwidth=4.2,
    headlength=5.5,
    headaxislength=4.3,
    color=AXIS_COLOR,
    pivot='tail',
    clip_on=False,
)

CONFIG = {'kind': 'bounds_rows',
 'figsize': (9.12, 7.9),
 'output_path': '/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/7.4--direct-convolution-for-lti-systems-Images/images/l002-s005-te-section-005.png',
 'xlim': (-0.4, 6.4),
 'ylim': (-0.65, 3.35),
 'axis_y': -0.35,
 'rows': [{'y': 2.35,
           'fixed': (0.0, 3.0),
           'moving': (-1.0, 1.0),
           'shade': (0.0, 1.0),
           'fixed_center': 1.5,
           'moving_center': 0.0,
           'fixed_label': '$x(\\tau)\\text{ support }[0,3]$',
           'moving_label': '$h(t-\\tau)\\text{ support }[t-2,t]$',
           'region_label': '$0<t<2$',
           't_text': '$t=1$',
           'bounds': ('$0$', '$t$')},
          {'y': 1.25,
           'fixed': (0.0, 3.0),
           'moving': (1.0, 3.0),
           'shade': (1.0, 3.0),
           'fixed_center': 1.5,
           'moving_center': 2.0,
           'fixed_label': '$x(\\tau)\\text{ support }[0,3]$',
           'moving_label': '$h(t-\\tau)\\text{ support }[t-2,t]$',
           'region_label': '$2<t<3$',
           't_text': '$t=5/2$',
           'bounds': ('$t-2$', '$t$')},
          {'y': 0.15,
           'fixed': (0.0, 3.0),
           'moving': (3.0, 5.0),
           'shade': (3.0, 3.0),
           'fixed_center': 1.5,
           'moving_center': 4.0,
           'fixed_label': '$x(\\tau)\\text{ support }[0,3]$',
           'moving_label': '$h(t-\\tau)\\text{ support }[t-2,t]$',
           'region_label': '$3<t<5$',
           't_text': '$t=4$',
           'bounds': ('$t-2$', '$3$')}]}
OUTPUT_PATH = Path(r'/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/7.4--direct-convolution-for-lti-systems-Images/images/l002-s005-te-section-005.png')


def configure_matplotlib():
    plt.rcParams.update({
        'mathtext.fontset': 'cm',
        'font.family': 'serif',
        'figure.facecolor': 'white',
        'axes.facecolor': 'white',
        'savefig.facecolor': 'white',
    })


def setup_ct_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_label=r'$\\tau$',
    y_label='',
    show_grid=True,
    show_origin=True,
    y_tick_label_side='left',
    equal_aspect=True,
):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    if equal_aspect:
        ax.set_aspect('equal', adjustable='box')
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    if show_grid:
        ax.grid(True, linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
        ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    x0, x1 = xlim
    y0, y1 = ylim
    ax.quiver(x0, 0, x1 - x0, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y0, 0, y1 - y0, **AXIS_ARROW_KW)
    for t in xticks:
        if abs(t) < 1e-12:
            continue
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(t, -0.16, math_label(t), fontsize=TICK_LABEL_SIZE, ha='center', va='top', color=TICK_LABEL_COLOR, zorder=6)
    for y in yticks:
        if abs(y) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if y_tick_label_side == 'right':
            ax.text(0.12, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha='left', va='center', color=TICK_LABEL_COLOR, zorder=6)
        else:
            ax.text(-0.12, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha='right', va='center', color=TICK_LABEL_COLOR, zorder=6)
    if show_origin:
        ax.text(0.06, -0.08, r'$0$', fontsize=TICK_LABEL_SIZE, ha='left', va='top', color=TICK_LABEL_COLOR, zorder=6)
    x_pad = 0.08 * (xlim[1] - xlim[0]) / 6
    y_pad = 0.08 * (ylim[1] - ylim[0]) / 4
    ax.text(x1 + x_pad, -0.03, x_label, fontsize=AXIS_LABEL_SIZE, ha='left', va='center', color=LABEL_COLOR, clip_on=False)
    if y_label:
        ax.text(0, y1 + y_pad, y_label, fontsize=TOP_LABEL_SIZE, ha='center', va='bottom', color=LABEL_COLOR, clip_on=False)
    return ax


def math_label(value):
    if isinstance(value, str):
        return value
    if abs(value - int(value)) < 1e-9:
        return rf'$%d$' % int(value)
    return rf'$%g$' % value


def draw_bar(ax, start, end, y, *, lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    ax.plot([start, end], [y, y], color=color, linewidth=lw, solid_capstyle='butt', zorder=zorder)
    ax.plot([start, start], [y - 0.05, y + 0.05], color=color, lw=1.6, zorder=zorder)
    ax.plot([end, end], [y - 0.05, y + 0.05], color=color, lw=1.6, zorder=zorder)


def draw_signal_segment(ax, xs, ys, *, lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    ax.plot(xs, ys, color=color, linewidth=lw, solid_capstyle='butt', solid_joinstyle='miter', zorder=zorder)


def draw_dashed_vline(ax, x, y0, y1, *, color=GUIDE_COLOR, lw=GUIDE_LW, zorder=3):
    ax.plot([x, x], [y0, y1], color=color, linewidth=lw, linestyle=(0, (1.1, 2.4)), zorder=zorder)


def draw_band(ax, x0, x1, y0, y1, *, alpha=0.12, color=SIGNAL_COLOR, zorder=1):
    ax.fill_between([x0, x1], [y0, y0], [y1, y1], color=color, alpha=alpha, zorder=zorder)


def draw_text(ax, x, y, text, *, size=14, ha='center', va='bottom', color=LABEL_COLOR, bbox=None, zorder=7):
    ax.text(x, y, text, fontsize=size, ha=ha, va=va, color=color, bbox=bbox, zorder=zorder)


def draw_axis_line(ax, y, x0, x1, *, arrow=True):
    if arrow:
        ax.quiver(x0, y, x1 - x0, 0, **AXIS_ARROW_KW)
    else:
        ax.plot([x0, x1], [y, y], color=AXIS_COLOR, lw=AXIS_LW, zorder=2)


def draw_tick(ax, x, y, *, half=0.05):
    ax.plot([x, x], [y - half, y + half], color=AXIS_COLOR, lw=1.1, zorder=5)


def draw_support_row(ax, *, y, fixed, moving, fixed_label, moving_label, region_label, shade=None, bounds=None, t_text=None):
    fixed_y = y + 0.17
    moving_y = y - 0.05
    if shade is not None:
        draw_band(ax, shade[0], shade[1], y - 0.16, y + 0.28, alpha=0.12)
    draw_bar(ax, fixed[0], fixed[1], fixed_y, lw=6.0)
    draw_bar(ax, moving[0], moving[1], moving_y, lw=6.0)
    draw_text(ax, (fixed[0] + fixed[1]) / 2, fixed_y + 0.12, fixed_label, size=13)
    draw_text(ax, (moving[0] + moving[1]) / 2, moving_y + 0.12, moving_label, size=13)
    draw_text(ax, ax.get_xlim()[0] + 0.08, y + 0.09, region_label, size=13, ha='left')
    if t_text is not None:
        draw_text(ax, ax.get_xlim()[0] + 0.08, y - 0.10, t_text, size=12, ha='left', color=ANNOTATION_COLOR)
    if bounds is not None:
        lower, upper = bounds
        draw_text(ax, shade[0] if shade is not None else moving[0], y - 0.30, lower, size=12, va='top')
        draw_text(ax, shade[1] if shade is not None else moving[1], y - 0.30, upper, size=12, va='top')


def render_section_overlap():
    fig = plt.figure(figsize=(9.12, 7.68), dpi=160)
    ax = fig.add_axes([0.11, 0.22, 0.83, 0.68])
    setup_ct_axes(
        ax,
        xlim=(-0.35, 1.62),
        ylim=(-0.9, 1.45),
        xticks=[0, 0.5, 1.0, 1.5],
        yticks=[],
        x_label=r'$\tau$',
        y_label='',
        show_grid=True,
    )
    draw_signal_segment(ax, [0.0, 1.0], [0.0, 1.0])
    draw_bar(ax, 0.35, 1.35, 0.72, lw=4.0)
    draw_band(ax, 0.35, 1.0, 0.0, 0.98, alpha=0.14)
    draw_text(ax, 0.07, 1.06, r'$x(\tau)=\tau$', size=15, ha='left')
    draw_text(ax, 0.92, 0.88, r'$h(t-\tau)=1$', size=15, ha='left')
    draw_text(ax, 0.50, -0.15, r'$[0,1]$', size=14)
    draw_text(ax, 0.85, 0.48, r'$[t-1,t]$', size=14)
    draw_text(ax, 0.35, -0.28, r'$a(t)$', size=14)
    draw_text(ax, 1.00, -0.28, r'$b(t)$', size=14)
    draw_axis_line(ax, -0.58, -0.12, 1.55, arrow=True)
    draw_tick(ax, 0.35, -0.58)
    draw_tick(ax, 1.00, -0.58)
    draw_text(ax, 0.35, -0.70, r'$a(t)$', size=13, va='top')
    draw_text(ax, 1.00, -0.70, r'$b(t)$', size=13, va='top')
    draw_text(ax, 1.58, -0.56, r'$t$', size=16, ha='left', va='center')
    fig.savefig(OUTPUT_PATH, bbox_inches='tight', facecolor='white')


def render_endpoint_alignment():
    fixed = CONFIG['fixed']
    moving = CONFIG['moving']
    fig, ax = plt.subplots(figsize=CONFIG['figsize'], dpi=160)
    setup_ct_axes(
        ax,
        xlim=CONFIG['xlim'],
        ylim=CONFIG['ylim'],
        xticks=CONFIG['xticks'],
        yticks=[],
        x_label=r'$\tau$',
        y_label='',
        show_grid=True,
    )
    draw_bar(ax, fixed[0], fixed[1], CONFIG['fixed_y'], lw=6.0)
    draw_bar(ax, moving[0], moving[1], CONFIG['moving_y'], lw=6.0)
    draw_text(ax, (fixed[0] + fixed[1]) / 2, CONFIG['fixed_y'] + 0.18, CONFIG['fixed_label'], size=13)
    draw_text(ax, (moving[0] + moving[1]) / 2, CONFIG['moving_y'] + 0.18, CONFIG['moving_label'], size=13)
    for x in fixed:
        draw_dashed_vline(ax, x, CONFIG['fixed_y'] - 0.02, CONFIG['fixed_y'] + 0.20)
    for x in moving:
        draw_dashed_vline(ax, x, CONFIG['moving_y'] - 0.02, CONFIG['moving_y'] + 0.20)
    for x, lab, y in CONFIG['endpoint_labels']:
        draw_text(ax, x, y, lab, size=13, va='bottom')
    fig.savefig(OUTPUT_PATH, bbox_inches='tight', facecolor='white')


def render_ordering():
    fig = plt.figure(figsize=CONFIG['figsize'], dpi=160)
    ax = fig.add_axes([0.08, 0.30, 0.86, 0.58])
    setup_ct_axes(
        ax,
        xlim=CONFIG['xlim'],
        ylim=CONFIG['ylim'],
        xticks=[],
        yticks=[],
        x_label=r'$\tau$',
        y_label='',
        show_grid=True,
    )
    draw_bar(ax, CONFIG['fixed'][0], CONFIG['fixed'][1], CONFIG['fixed_y'], lw=6.0)
    draw_bar(ax, CONFIG['moving'][0], CONFIG['moving'][1], CONFIG['moving_y'], lw=6.0)
    draw_text(ax, (CONFIG['fixed'][0] + CONFIG['fixed'][1]) / 2, CONFIG['fixed_y'] + 0.18, CONFIG['fixed_label'], size=13)
    draw_text(ax, (CONFIG['moving'][0] + CONFIG['moving'][1]) / 2, CONFIG['moving_y'] + 0.18, CONFIG['moving_label'], size=13)
    for x, lab, y in CONFIG['endpoint_labels']:
        draw_text(ax, x, y, lab, size=13, va='bottom')
    for x, y0, y1 in CONFIG.get('guides', []):
        draw_dashed_vline(ax, x, y0, y1)
    for x, y, text in CONFIG.get('callouts', []):
        draw_text(
            ax,
            x,
            y,
            text,
            size=12,
            va='center',
            bbox=dict(boxstyle='round,pad=0.18', fc='white', ec=GUIDE_COLOR, lw=0.8),
        )
    ax2 = fig.add_axes([0.12, 0.10, 0.80, 0.12])
    ax2.set_xlim(*CONFIG['bottom_xlim'])
    ax2.set_ylim(-0.25, 0.25)
    for spine in ax2.spines.values():
        spine.set_visible(False)
    ax2.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    ax2.quiver(CONFIG['bottom_xlim'][0], 0, CONFIG['bottom_xlim'][1] - CONFIG['bottom_xlim'][0], 0, **AXIS_ARROW_KW)
    if CONFIG.get('bottom_labels'):
        for x, label in CONFIG['bottom_labels']:
            draw_tick(ax2, x, 0.0, half=0.04)
            ax2.text(x, -0.11, label, fontsize=14, ha='center', va='top', color=TICK_LABEL_COLOR)
    ax2.text(CONFIG['bottom_xlim'][1] + 0.10, 0.0, r'$t$', fontsize=AXIS_LABEL_SIZE, ha='left', va='center', color=LABEL_COLOR, clip_on=False)
    fig.savefig(OUTPUT_PATH, bbox_inches='tight', facecolor='white')


def render_rows(*, include_bounds=False):
    rows = CONFIG['rows']
    fig, ax = plt.subplots(figsize=CONFIG['figsize'], dpi=160)
    setup_ct_axes(
        ax,
        xlim=CONFIG['xlim'],
        ylim=CONFIG['ylim'],
        xticks=CONFIG.get('xticks', []),
        yticks=[],
        x_label=r'$\tau$',
        y_label='',
        show_grid=True,
    )
    for row in rows:
        y = row['y']
        if row.get('shade') is not None:
            draw_band(ax, row['shade'][0], row['shade'][1], y - 0.16, y + 0.28, alpha=0.14)
        draw_bar(ax, row['fixed'][0], row['fixed'][1], y + 0.17, lw=5.8)
        draw_bar(ax, row['moving'][0], row['moving'][1], y - 0.05, lw=5.8)
        draw_text(ax, row['fixed_center'], y + 0.32, row['fixed_label'], size=12)
        draw_text(ax, row['moving_center'], y + 0.10, row['moving_label'], size=12)
        draw_text(ax, CONFIG['xlim'][0] + 0.08, y + 0.08, row['region_label'], size=12, ha='left')
        if row.get('t_text'):
            draw_text(ax, CONFIG['xlim'][0] + 0.08, y - 0.10, row['t_text'], size=11, ha='left', color=ANNOTATION_COLOR)
        if include_bounds and row.get('bounds'):
            lower, upper = row['bounds']
            if row.get('shade') is not None:
                draw_text(ax, row['shade'][0], y - 0.31, lower, size=11, va='top')
                draw_text(ax, row['shade'][1], y - 0.31, upper, size=11, va='top')
            else:
                draw_text(ax, row['moving'][0], y - 0.31, lower, size=11, va='top')
                draw_text(ax, row['moving'][1], y - 0.31, upper, size=11, va='top')
    draw_axis_line(ax, CONFIG['axis_y'], CONFIG['xlim'][0] + 0.05, CONFIG['xlim'][1] - 0.05, arrow=True)
    if CONFIG.get('bottom_labels'):
        for x, label in CONFIG['bottom_labels']:
            draw_tick(ax, x, CONFIG['axis_y'], half=0.04)
            ax.text(x, CONFIG['axis_y'] - 0.12, label, fontsize=13, ha='center', va='top', color=TICK_LABEL_COLOR)
    ax.text(CONFIG['xlim'][1] + 0.12, CONFIG['axis_y'], r'$t$', fontsize=AXIS_LABEL_SIZE, ha='left', va='center', color=LABEL_COLOR, clip_on=False)
    fig.savefig(OUTPUT_PATH, bbox_inches='tight', facecolor='white')


def render():
    kind = CONFIG['kind']
    if kind == 'section_overlap':
        render_section_overlap()
    elif kind == 'endpoint_alignment':
        render_endpoint_alignment()
    elif kind == 'ordering':
        render_ordering()
    elif kind == 'classification_rows':
        render_rows(include_bounds=False)
    elif kind == 'bounds_rows':
        render_rows(include_bounds=True)
    else:
        raise ValueError(f'Unknown kind: {kind}')


if __name__ == '__main__':
    configure_matplotlib()
    render()
