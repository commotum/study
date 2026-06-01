import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


plt.rcParams.update({
    "mathtext.fontset": "cm",
    "font.family": "serif",
})

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"

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

DEFAULT_FIGSIZE = (9.12, 7.68)
SQUARE_FIGSIZE = (5.6, 5.6)
DPI = 160

AXIS_ARROW_KW = dict(
    angles="xy",
    scale_units="xy",
    scale=1,
    width=0.0048,
    headwidth=4.2,
    headlength=5.5,
    headaxislength=4.3,
    color=AXIS_COLOR,
    pivot="tail",
    clip_on=False,
)


def math_label(value):
    if isinstance(value, str):
        return value
    if abs(value - int(value)) < 1e-9:
        return rf"${int(value)}$"
    return rf"${value:g}$"


def new_ct_figure(*, square=False, dpi=DPI):
    figsize = SQUARE_FIGSIZE if square else DEFAULT_FIGSIZE
    return plt.subplots(figsize=figsize, dpi=dpi)


def setup_ct_signal_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_axis_label=r"$t$",
    y_axis_label=r"$x(t)$",
    show_grid=True,
    show_origin=True,
    y_tick_label_side="left",
    equal_aspect=True,
):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)

    if equal_aspect:
        ax.set_aspect("equal", adjustable="box")

    ax.set_xticks(xticks)
    ax.set_yticks(yticks)

    if show_grid:
        ax.grid(True, linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
        ax.set_axisbelow(True)

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    x_axis_start, x_axis_end = xlim
    y_axis_start, y_axis_end = ylim

    ax.quiver(x_axis_start, 0, x_axis_end - x_axis_start, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y_axis_start, 0, y_axis_end - y_axis_start, **AXIS_ARROW_KW)

    for t in xticks:
        if abs(t) < 1e-12:
            continue
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN],
                color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(t, -0.16, math_label(t),
                fontsize=TICK_LABEL_SIZE, ha="center", va="top",
                color=TICK_LABEL_COLOR, zorder=6)

    for y in yticks:
        if abs(y) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y],
                color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if y_tick_label_side == "right":
            ax.text(0.12, y, math_label(y),
                    fontsize=TICK_LABEL_SIZE, ha="left", va="center",
                    color=TICK_LABEL_COLOR, zorder=6)
        else:
            ax.text(-0.12, y, math_label(y),
                    fontsize=TICK_LABEL_SIZE, ha="right", va="center",
                    color=TICK_LABEL_COLOR, zorder=6)

    if show_origin:
        ax.text(0.06, -0.08, r"$0$",
                fontsize=TICK_LABEL_SIZE, ha="left", va="top",
                color=TICK_LABEL_COLOR, zorder=6)

    x_pad = 0.08 * (xlim[1] - xlim[0]) / 6
    y_pad = 0.08 * (ylim[1] - ylim[0]) / 4

    ax.text(x_axis_end + x_pad, -0.03, x_axis_label,
            fontsize=AXIS_LABEL_SIZE, ha="left", va="center",
            color=LABEL_COLOR, clip_on=False)
    ax.text(0, y_axis_end + y_pad, y_axis_label,
            fontsize=TOP_LABEL_SIZE, ha="center", va="bottom",
            color=LABEL_COLOR, clip_on=False)


def plot_signal(ax, t, x, *, lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    ax.plot(
        t,
        x,
        color=color,
        linewidth=lw,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=zorder,
    )


def plot_smooth_signal(ax, t, x, *, lw=2.35, color=SIGNAL_COLOR, zorder=4):
    ax.plot(
        t,
        x,
        color=color,
        linewidth=lw,
        solid_capstyle="round",
        zorder=zorder,
    )


def draw_open_endpoint(ax, t0, x0):
    ax.plot(
        t0,
        x0,
        marker="o",
        markersize=OPEN_MARKER_SIZE,
        markerfacecolor="white",
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=ENDPOINT_EDGEWIDTH,
        linestyle="None",
        zorder=6,
    )


def draw_closed_endpoint(ax, t0, x0):
    ax.plot(
        t0,
        x0,
        marker="o",
        markersize=CLOSED_MARKER_SIZE,
        markerfacecolor=SIGNAL_COLOR,
        markeredgecolor=SIGNAL_COLOR,
        markeredgewidth=ENDPOINT_EDGEWIDTH,
        linestyle="None",
        zorder=6,
    )


def draw_dotted_guide(ax, x_values, y_values):
    ax.plot(
        x_values,
        y_values,
        color=GUIDE_COLOR,
        linewidth=GUIDE_LW,
        linestyle=(0, (1.1, 2.4)),
        zorder=3,
    )


def draw_rect_pulse(
    ax,
    left,
    right,
    height,
    *,
    baseline=0.0,
    color=SIGNAL_COLOR,
    lw=SIGNAL_LW,
    fill=False,
    fill_alpha=0.12,
    fill_color=SIGNAL_COLOR,
    zorder=4,
):
    if right < left:
        left, right = right, left

    xs = [left, left, right, right]
    ys = [baseline, baseline + height, baseline + height, baseline]
    plot_signal(ax, xs, ys, lw=lw, color=color, zorder=zorder)

    if fill:
        ax.fill_between(
            [left, right],
            baseline + height,
            baseline,
            color=fill_color,
            alpha=fill_alpha,
            zorder=zorder - 1,
        )


def draw_support_bracket(ax, start, end, y=-0.38, *, label=None, color=ANNOTATION_COLOR, label_offset=-0.12):
    ax.plot([start, end], [y, y], color=color, linewidth=1.3, zorder=5)
    ax.plot([start, start], [y - 0.06, y + 0.06], color=color, linewidth=1.3, zorder=5)
    ax.plot([end, end], [y - 0.06, y + 0.06], color=color, linewidth=1.3, zorder=5)
    if label is not None:
        ax.text(
            (start + end) / 2,
            y + label_offset,
            label,
            fontsize=ANNOTATION_SIZE,
            ha="center",
            va="top",
            color=color,
        )


def draw_marker_line(ax, x, y0, y1, *, color=GUIDE_COLOR, linestyle=(0, (1.1, 2.4)), lw=GUIDE_LW, zorder=3):
    ax.plot([x, x], [y0, y1], color=color, linewidth=lw, linestyle=linestyle, zorder=zorder)


def draw_triangle_sketch(ax, *, x0, x1, x2, y_peak, label=None, branch_labels=None):
    plot_signal(ax, [x0, x1, x2], [0.0, y_peak, 0.0], lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4)

    peak_label = rf"${y_peak:g}$" if label is None else label
    ax.text(
        x1,
        y_peak + 0.10,
        peak_label,
        fontsize=ANNOTATION_SIZE,
        ha="center",
        va="bottom",
        color=LABEL_COLOR,
    )

    if branch_labels:
        if len(branch_labels) > 0 and branch_labels[0]:
            ax.text(
                (x0 + x1) / 2,
                y_peak * 0.56,
                branch_labels[0],
                fontsize=ANNOTATION_SIZE,
                ha="center",
                va="bottom",
                color=LABEL_COLOR,
            )
        if len(branch_labels) > 1 and branch_labels[1]:
            ax.text(
                (x1 + x2) / 2,
                y_peak * 0.56,
                branch_labels[1],
                fontsize=ANNOTATION_SIZE,
                ha="center",
                va="bottom",
                color=LABEL_COLOR,
            )


def draw_t_axis(ax, *, y=0.0, xlim, breakpoints=None, labels=None, region_labels=None, axis_label=r"$t$"):
    x0, x1 = xlim
    ax.set_xlim(x0, x1)
    ax.set_ylim(min(-0.9, y - 0.9), max(0.9, y + 0.9))
    ax.axis("off")

    ax.plot([x0, x1], [y, y], color=AXIS_COLOR, lw=AXIS_LW, zorder=2)
    ax.annotate(
        "",
        xy=(x1, y),
        xytext=(x1 - 0.001, y),
        arrowprops=dict(
            arrowstyle="-|>",
            color=AXIS_COLOR,
            lw=AXIS_LW,
            shrinkA=0,
            shrinkB=0,
        ),
    )

    if breakpoints:
        for bp in breakpoints:
            ax.plot([bp, bp], [y - 0.055, y + 0.055], color=AXIS_COLOR, lw=TICK_LW, zorder=3)

    if labels:
        for bp, label in labels.items():
            ax.text(bp, y - 0.14, label, fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR)

    if region_labels:
        for xmid, text in region_labels:
            ax.text(xmid, y + 0.12, text, fontsize=ANNOTATION_SIZE, ha="center", va="bottom", color=LABEL_COLOR)

    ax.text(
        x1 + 0.08 * (x1 - x0),
        y - 0.02,
        axis_label,
        fontsize=AXIS_LABEL_SIZE,
        ha="left",
        va="center",
        color=LABEL_COLOR,
        clip_on=False,
    )


def save_figure(fig, output_path):
    fig.savefig(output_path, bbox_inches="tight", facecolor="white")

def _shade_interval(ax, left, right, height, *, baseline=0.0, alpha=0.16, color=SIGNAL_COLOR, zorder=2):
    ax.add_patch(Rectangle(
        (left, baseline),
        right - left,
        height - baseline,
        facecolor=color,
        edgecolor="none",
        alpha=alpha,
        zorder=zorder,
    ))


def _draw_text(ax, spec):
    ax.text(
        spec["x"],
        spec["y"],
        spec["text"],
        fontsize=spec.get("fontsize", 15),
        ha=spec.get("ha", "center"),
        va=spec.get("va", "center"),
        color=spec.get("color", LABEL_COLOR),
        clip_on=spec.get("clip_on", False),
        zorder=spec.get("zorder", 6),
    )


def _normalize_region_labels(region_labels):
    normalized = []
    for item in region_labels or []:
        if isinstance(item, dict):
            normalized.append((item["x"], item["text"]))
        else:
            normalized.append(item)
    return normalized


def render_overlap_panel(ax, cfg):
    setup_ct_signal_axes(
        ax,
        xlim=cfg["xlim"],
        ylim=cfg["ylim"],
        xticks=cfg["xticks"],
        yticks=cfg["yticks"],
        x_axis_label=cfg.get("x_axis_label", r"$	au$"),
        y_axis_label=cfg.get("y_axis_label", r"$x(	au),\,h(t-	au)$"),
        show_grid=cfg.get("show_grid", True),
        show_origin=cfg.get("show_origin", True),
        y_tick_label_side=cfg.get("y_tick_label_side", "left"),
        equal_aspect=cfg.get("equal_aspect", True),
    )

    fixed = cfg["fixed"]
    moving = cfg["moving"]

    draw_rect_pulse(
        ax,
        fixed["left"],
        fixed["right"],
        fixed["height"],
        baseline=fixed.get("baseline", 0.0),
        color=fixed.get("color", SIGNAL_COLOR),
        lw=fixed.get("lw", SIGNAL_LW),
        fill=True,
        fill_alpha=fixed.get("fill_alpha", 0.10),
        zorder=fixed.get("zorder", 4),
    )
    draw_rect_pulse(
        ax,
        moving["left"],
        moving["right"],
        moving["height"],
        baseline=moving.get("baseline", 0.0),
        color=moving.get("color", SIGNAL_COLOR),
        lw=moving.get("lw", SIGNAL_LW),
        fill=True,
        fill_alpha=moving.get("fill_alpha", 0.10),
        zorder=moving.get("zorder", 4),
    )

    overlap = cfg.get("overlap")
    if overlap:
        _shade_interval(
            ax,
            overlap["left"],
            overlap["right"],
            overlap.get("height", min(fixed["height"], moving["height"])),
            baseline=overlap.get("baseline", 0.0),
            alpha=overlap.get("alpha", 0.16),
            color=overlap.get("color", SIGNAL_COLOR),
            zorder=overlap.get("zorder", 2),
        )

    for spec in cfg.get("labels", []):
        _draw_text(ax, spec)

    for bracket in cfg.get("brackets", []):
        draw_support_bracket(
            ax,
            bracket["start"],
            bracket["end"],
            y=bracket.get("y", -0.38),
            label=bracket.get("label"),
            color=bracket.get("color", ANNOTATION_COLOR),
            label_offset=bracket.get("label_offset", -0.12),
        )

    for guide in cfg.get("guides", []):
        draw_dotted_guide(ax, guide["x"], guide["y"])

    for spec in cfg.get("edge_labels", []):
        _draw_text(ax, spec)


def render_timeline_scene(cfg):
    fig = plt.figure(figsize=cfg.get("figsize", DEFAULT_FIGSIZE), dpi=DPI)
    gs = fig.add_gridspec(
        2,
        1,
        height_ratios=cfg.get("height_ratios", [3.1, 1.0]),
        hspace=cfg.get("hspace", 0.28),
    )
    ax_top = fig.add_subplot(gs[0, 0])
    ax_bottom = fig.add_subplot(gs[1, 0])

    render_overlap_panel(ax_top, cfg["top_panel"])

    timeline = cfg["timeline"]
    draw_t_axis(
        ax_bottom,
        y=timeline.get("y", 0.0),
        xlim=timeline["xlim"],
        breakpoints=timeline.get("breakpoints", []),
        labels=timeline.get("labels"),
        region_labels=_normalize_region_labels(timeline.get("region_labels")),
        axis_label=timeline.get("axis_label", r"$t$"),
    )

    for spec in timeline.get("extra_text", []):
        _draw_text(ax_bottom, spec)

    save_figure(fig, cfg["image_output_path"])


def render_single_scene(cfg):
    fig, ax = plt.subplots(figsize=cfg.get("figsize", DEFAULT_FIGSIZE), dpi=DPI)
    render_overlap_panel(ax, cfg["panel"])
    save_figure(fig, cfg["image_output_path"])


def render_assembly_scene(cfg):
    fig = plt.figure(figsize=cfg.get("figsize", (10.2, 8.8)), dpi=DPI)
    gs = fig.add_gridspec(
        2,
        2,
        height_ratios=cfg.get("height_ratios", [1.0, 1.35]),
        hspace=cfg.get("hspace", 0.45),
        wspace=cfg.get("wspace", 0.30),
    )
    ax_x = fig.add_subplot(gs[0, 0])
    ax_h = fig.add_subplot(gs[0, 1])
    ax_y = fig.add_subplot(gs[1, :])

    for ax, panel in zip((ax_x, ax_h), cfg["inputs"]):
        setup_ct_signal_axes(
            ax,
            xlim=panel["xlim"],
            ylim=panel["ylim"],
            xticks=panel["xticks"],
            yticks=panel["yticks"],
            x_axis_label=panel.get("x_axis_label", r"$t$"),
            y_axis_label=panel["y_axis_label"],
            show_grid=panel.get("show_grid", True),
            show_origin=panel.get("show_origin", True),
            y_tick_label_side=panel.get("y_tick_label_side", "left"),
            equal_aspect=panel.get("equal_aspect", True),
        )
        draw_rect_pulse(
            ax,
            panel["left"],
            panel["right"],
            panel["height"],
            baseline=panel.get("baseline", 0.0),
            color=panel.get("color", SIGNAL_COLOR),
            lw=panel.get("lw", SIGNAL_LW),
            fill=True,
            fill_alpha=panel.get("fill_alpha", 0.10),
            zorder=panel.get("zorder", 4),
        )
        if panel.get("label"):
            ax.text(
                (panel["left"] + panel["right"]) / 2,
                panel["height"] + panel.get("label_offset", 0.14),
                panel["label"],
                fontsize=panel.get("label_size", 16),
                ha="center",
                va="bottom",
                color=panel.get("label_color", LABEL_COLOR),
            )
        if panel.get("interval_label"):
            draw_support_bracket(
                ax,
                panel["left"],
                panel["right"],
                y=panel.get("bracket_y", -0.38),
                label=panel["interval_label"],
                color=panel.get("bracket_color", ANNOTATION_COLOR),
                label_offset=panel.get("label_offset_below", -0.12),
            )
        for spec in panel.get("extra_text", []):
            _draw_text(ax, spec)

    output = cfg["output"]
    setup_ct_signal_axes(
        ax_y,
        xlim=output["xlim"],
        ylim=output["ylim"],
        xticks=output["xticks"],
        yticks=output["yticks"],
        x_axis_label=output.get("x_axis_label", r"$t$"),
        y_axis_label=output.get("y_axis_label", r"$y(t)$"),
        show_grid=output.get("show_grid", True),
        show_origin=output.get("show_origin", True),
        y_tick_label_side=output.get("y_tick_label_side", "left"),
        equal_aspect=output.get("equal_aspect", False),
    )

    if output.get("curve", False):
        plot_signal(
            ax_y,
            output["x_points"],
            output["y_points"],
            color=output.get("curve_color", SIGNAL_COLOR),
            lw=output.get("curve_lw", SIGNAL_LW),
        )

    for bp in output.get("breakpoints", []):
        ax_y.plot(
            [bp, bp],
            [-TICK_HALF_LEN, TICK_HALF_LEN],
            color=AXIS_COLOR,
            lw=TICK_LW,
            zorder=5,
        )
        if output.get("show_break_labels", True):
            ax_y.text(
                bp,
                output.get("break_label_y", -0.16),
                math_label(bp),
                fontsize=TICK_LABEL_SIZE,
                ha="center",
                va="top",
                color=TICK_LABEL_COLOR,
                zorder=6,
            )

    for spec in output.get("labels", []):
        _draw_text(ax_y, spec)

    for spec in output.get("extra_text", []):
        _draw_text(ax_y, spec)

    save_figure(fig, cfg["image_output_path"])


def main():
    kind = CONFIG["kind"]
    if kind == "timeline":
        render_timeline_scene(CONFIG)
    elif kind == "single":
        render_single_scene(CONFIG)
    elif kind == "assembly":
        render_assembly_scene(CONFIG)
    else:
        raise ValueError(f"Unknown render kind: {kind}")

CONFIG = {'kind': 'single',
 'slot_id': 'section-005',
 'section_title': 'Computing the Shrinking-Overlap Region',
 'image_output_path': '/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/7.2--convolution-of-simple-signals-Images/images/l002-s005-te-section-005.png',
 'figsize': (9.4, 6.0),
 'panel': {'xlim': (-0.8, 10.4),
           'ylim': (-0.7, 3.6),
           'xticks': [0, 2, 4, 6, 8, 10],
           'yticks': [1, 2, 3],
           'x_axis_label': '$\\tau$',
           'y_axis_label': '$x(\\tau),\\,h(t-\\tau)$',
           'equal_aspect': True,
           'fixed': {'left': 0.0,
                     'right': 4.0,
                     'height': 2.0,
                     'label': '$x(\\tau)$',
                     'fill_alpha': 0.08},
           'moving': {'left': 2.0,
                      'right': 9.0,
                      'height': 1.55,
                      'label': '$h(t-\\tau)$',
                      'fill_alpha': 0.08},
           'overlap': {'left': 2.0,
                       'right': 4.0,
                       'height': 1.55,
                       'label': '$L(t)=4-(t-7)=11-t$',
                       'alpha': 0.18},
           'brackets': [{'start': 0.0, 'end': 4.0, 'y': -0.44, 'label': '$0\\leq \\tau\\leq 4$'},
                        {'start': 2.0, 'end': 9.0, 'y': -0.44, 'label': '$t-7\\leq \\tau\\leq t$'}],
           'edge_labels': [{'x': 0.0, 'y': -0.16, 'text': '$0$', 'fontsize': 15, 'va': 'top'},
                           {'x': 4.0, 'y': -0.16, 'text': '$4$', 'fontsize': 15, 'va': 'top'},
                           {'x': 2.0, 'y': -0.16, 'text': '$t-7$', 'fontsize': 15, 'va': 'top'},
                           {'x': 9.0, 'y': -0.16, 'text': '$t$', 'fontsize': 15, 'va': 'top'}]},
 'python_output_path': '/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/7.2--convolution-of-simple-signals-Images/code/l002-s005-te-section-005.py',
 'slot_key': 'l002-s005-te-section-005',
 'lesson_index': 2,
 'lesson_title': 'Convolution of Unequal-Width Rectangular Pulses',
 'section_index': 5,
 'source_stage': 'tutorial-example',
 'image_slot_id': 'section-005',
 'template': 'shrinking-overlap-shaded-segment'}

if __name__ == '__main__':
    main()
