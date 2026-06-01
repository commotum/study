from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


plt.rcParams.update({
    "mathtext.fontset": "cm",
    "font.family": "serif",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
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
DEFAULT_DPI = 160
DEFAULT_FIGSIZE = (9.12, 7.68)
DEFAULT_COMPARISON_FIGSIZE = (13.4, 9.75)

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
    value = float(value)
    if np.isclose(value, round(value)):
        return rf"${int(round(value))}$"
    return rf"${value:g}$"


def standard_ct_figure(square=False):
    figsize = (5.6, 5.6) if square else DEFAULT_FIGSIZE
    fig, ax = plt.subplots(figsize=figsize, dpi=DEFAULT_DPI)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    return fig, ax


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
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(t, -0.16, math_label(t), fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR, zorder=6)

    for y in yticks:
        if abs(y) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if y_tick_label_side == "right":
            ax.text(0.12, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha="left", va="center", color=TICK_LABEL_COLOR, zorder=6)
        else:
            ax.text(-0.12, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha="right", va="center", color=TICK_LABEL_COLOR, zorder=6)

    if show_origin:
        ax.text(0.06, -0.08, r"$0$", fontsize=TICK_LABEL_SIZE, ha="left", va="top", color=TICK_LABEL_COLOR, zorder=6)

    x_pad = 0.08 * (xlim[1] - xlim[0]) / 6
    y_pad = 0.08 * (ylim[1] - ylim[0]) / 4

    ax.text(
        x_axis_end + x_pad,
        -0.03,
        x_axis_label,
        fontsize=AXIS_LABEL_SIZE,
        ha="left",
        va="center",
        color=LABEL_COLOR,
        clip_on=False,
    )
    ax.text(
        0,
        y_axis_end + y_pad,
        y_axis_label,
        fontsize=TOP_LABEL_SIZE,
        ha="center",
        va="bottom",
        color=LABEL_COLOR,
        clip_on=False,
    )


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


def draw_dotted_guide(ax, x_values, y_values):
    ax.plot(
        x_values,
        y_values,
        color=GUIDE_COLOR,
        linewidth=GUIDE_LW,
        linestyle=(0, (1.1, 2.4)),
        zorder=3,
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


def draw_support_bracket(ax, t_start, t_end, br_y=-0.38, label="duration"):
    ax.plot([t_start, t_end], [br_y, br_y], color=ANNOTATION_COLOR, linewidth=1.3, zorder=5)
    ax.plot([t_start, t_start], [br_y - 0.06, br_y + 0.06], color=ANNOTATION_COLOR, linewidth=1.3, zorder=5)
    ax.plot([t_end, t_end], [br_y - 0.06, br_y + 0.06], color=ANNOTATION_COLOR, linewidth=1.3, zorder=5)
    ax.text(
        (t_start + t_end) / 2,
        br_y - 0.12,
        label,
        fontsize=ANNOTATION_SIZE,
        ha="center",
        va="top",
        color=ANNOTATION_COLOR,
    )


def draw_offset_line(ax, t_start, t_end, offset):
    ax.plot(
        [t_start, t_end],
        [offset, offset],
        color=GUIDE_COLOR,
        linewidth=1.4,
        linestyle=(0, (1.1, 2.4)),
        zorder=3,
    )


def draw_amplitude_bracket(ax, x_bracket, offset, max_value):
    ax.plot([x_bracket, x_bracket], [offset, max_value], color=ANNOTATION_COLOR, linewidth=1.3, zorder=5)
    ax.plot([x_bracket - 0.07, x_bracket + 0.07], [offset, offset], color=ANNOTATION_COLOR, linewidth=1.3, zorder=5)
    ax.plot([x_bracket - 0.07, x_bracket + 0.07], [max_value, max_value], color=ANNOTATION_COLOR, linewidth=1.3, zorder=5)


def save_ct_figure(fig, output_path):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, bbox_inches="tight", facecolor="white")


def draw_rect_signal(
    ax,
    start,
    end,
    height,
    *,
    baseline=0,
    edge_color=SIGNAL_COLOR,
    fill_color=SIGNAL_COLOR,
    fill_alpha=0.0,
    lw=SIGNAL_LW,
    zorder=4,
):
    xs = [start, start, end, end]
    ys = [baseline, height, height, baseline]
    if fill_alpha > 0:
        ax.fill(xs, ys, color=fill_color, alpha=fill_alpha, zorder=zorder - 1, linewidth=0)
    plot_signal(ax, xs, ys, lw=lw, color=edge_color, zorder=zorder)


def draw_zero_line(ax, xlim, *, lw=2.1, color=SIGNAL_COLOR, zorder=4):
    plot_signal(ax, [xlim[0], xlim[1]], [0, 0], lw=lw, color=color, zorder=zorder)


def draw_texts(ax, texts):
    for item in texts or []:
        params = dict(
            fontsize=item.get("fontsize", ANNOTATION_SIZE),
            ha=item.get("ha", "center"),
            va=item.get("va", "center"),
            color=item.get("color", LABEL_COLOR),
            rotation=item.get("rotation", 0),
            clip_on=item.get("clip_on", False),
            zorder=item.get("zorder", 7),
        )
        ax.text(item["x"], item["y"], item["text"], **params)


def draw_annotations(ax, annotations):
    for item in annotations or []:
        params = dict(
            fontsize=item.get("fontsize", ANNOTATION_SIZE),
            color=item.get("color", LABEL_COLOR),
            ha=item.get("ha", "center"),
            va=item.get("va", "center"),
        )
        if "arrowprops" in item:
            params["arrowprops"] = item["arrowprops"]
        ax.annotate(item["text"], xy=item["xy"], xytext=item["xytext"], **params)


def render_panel(ax, panel):
    setup_ct_signal_axes(
        ax,
        xlim=panel["xlim"],
        ylim=panel["ylim"],
        xticks=panel["xticks"],
        yticks=panel["yticks"],
        x_axis_label=panel.get("x_label", r"$\tau$"),
        y_axis_label=panel.get("y_label", r"$x(\tau)$"),
        show_grid=panel.get("show_grid", True),
        show_origin=panel.get("show_origin", True),
        y_tick_label_side=panel.get("y_tick_label_side", "left"),
        equal_aspect=panel.get("equal_aspect", True),
    )

    if panel.get("zero_line"):
        draw_zero_line(ax, panel["xlim"], lw=panel.get("zero_line_lw", 2.1), color=panel.get("zero_line_color", SIGNAL_COLOR), zorder=panel.get("zero_line_zorder", 4))

    if panel.get("main_rect"):
        rect = panel["main_rect"]
        draw_rect_signal(
            ax,
            rect["start"],
            rect["end"],
            rect["height"],
            baseline=rect.get("baseline", 0),
            edge_color=rect.get("edge_color", SIGNAL_COLOR),
            fill_color=rect.get("fill_color", SIGNAL_COLOR),
            fill_alpha=rect.get("fill_alpha", 0.0),
            lw=rect.get("lw", SIGNAL_LW),
            zorder=rect.get("zorder", 4),
        )

    if panel.get("overlap"):
        overlap = panel["overlap"]
        height = overlap["height"]
        draw_rect_signal(
            ax,
            overlap["start"],
            overlap["end"],
            height,
            baseline=overlap.get("baseline", 0),
            edge_color=overlap.get("edge_color", SIGNAL_COLOR),
            fill_color=overlap.get("fill_color", SIGNAL_COLOR),
            fill_alpha=overlap.get("fill_alpha", 0.18),
            lw=overlap.get("lw", SIGNAL_LW),
            zorder=overlap.get("zorder", 4),
        )

    if panel.get("interval_bracket"):
        bracket = panel["interval_bracket"]
        draw_support_bracket(
            ax,
            bracket["start"],
            bracket["end"],
            br_y=bracket.get("y", -0.38),
            label=bracket.get("text", "duration"),
        )

    if panel.get("offset_line"):
        offset = panel["offset_line"]
        draw_offset_line(ax, offset["start"], offset["end"], offset["y"])

    if panel.get("amplitude_bracket"):
        bracket = panel["amplitude_bracket"]
        draw_amplitude_bracket(ax, bracket["x"], bracket["offset"], bracket["max"])

    draw_texts(ax, panel.get("texts"))
    draw_annotations(ax, panel.get("annotations"))
    draw_texts(ax, panel.get("figure_texts"))


def render_single_stack(spec):
    fig, axes = plt.subplots(
        len(spec["panels"]),
        1,
        figsize=spec.get("figure_size", DEFAULT_FIGSIZE),
        dpi=DEFAULT_DPI,
    )
    if len(spec["panels"]) == 1:
        axes = [axes]

    for ax, panel in zip(axes, spec["panels"]):
        render_panel(ax, panel)

    for item in spec.get("figure_texts", []):
        fig.text(
            item["x"],
            item["y"],
            item["text"],
            fontsize=item.get("fontsize", ANNOTATION_SIZE),
            ha=item.get("ha", "center"),
            va=item.get("va", "center"),
            color=item.get("color", LABEL_COLOR),
            rotation=item.get("rotation", 0),
        )

    fig.tight_layout(pad=0.9, h_pad=1.2)
    save_ct_figure(fig, spec["output_path"])
    plt.close(fig)


def render_comparison(spec):
    fig, axes = plt.subplots(
        3,
        2,
        figsize=spec.get("figure_size", DEFAULT_COMPARISON_FIGSIZE),
        dpi=DEFAULT_DPI,
    )

    columns = spec["columns"]
    for col_idx, column in enumerate(columns):
        for row_idx, panel in enumerate(column["panels"]):
            render_panel(axes[row_idx, col_idx], panel)

        header = column.get("header_text")
        if header:
            axes[0, col_idx].text(
                0.5,
                1.12,
                header,
                transform=axes[0, col_idx].transAxes,
                fontsize=column.get("header_fontsize", ANNOTATION_SIZE),
                ha="center",
                va="bottom",
                color=column.get("header_color", LABEL_COLOR),
                clip_on=False,
            )

    for item in spec.get("figure_texts", []):
        fig.text(
            item["x"],
            item["y"],
            item["text"],
            fontsize=item.get("fontsize", ANNOTATION_SIZE),
            ha=item.get("ha", "center"),
            va=item.get("va", "center"),
            color=item.get("color", LABEL_COLOR),
            rotation=item.get("rotation", 0),
        )

    fig.tight_layout(pad=0.9, h_pad=1.0, w_pad=1.0)
    save_ct_figure(fig, spec["output_path"])
    plt.close(fig)


def render_image(spec):
    if spec["layout"] == "single":
        render_single_stack(spec)
    elif spec["layout"] == "comparison":
        render_comparison(spec)
    else:
        raise ValueError(f"unknown layout: {spec['layout']}")

SPEC = {'layout': 'single',
 'output_path': '/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/6.3--convolution-setup-Images/images/l007-s004-qg-q001-q001.png',
 'figure_size': (10.0, 9.8),
 'panels': [{'xlim': (-0.4, 4.4),
             'ylim': (-0.35, 3.65),
             'xticks': [0, 1, 2, 4],
             'yticks': [3],
             'x_label': '$\\tau$',
             'y_label': '$x(\\tau)$',
             'zero_line': False,
             'y_tick_label_side': 'left',
             'equal_aspect': True,
             'show_origin': True,
             'main_rect': {'start': 0, 'end': 2, 'height': 3},
             'overlap': {'start': 1, 'end': 2, 'height': 3, 'fill_alpha': 0.22},
             'texts': [{'text': '$x(\\tau)=3$', 'x': 1.0, 'y': 3.18, 'fontsize': 15},
                       {'text': 'overlap 1<=tau<=2',
                        'x': 1.5,
                        'y': 1.45,
                        'fontsize': 14}]},
            {'xlim': (-0.4, 4.4),
             'ylim': (-0.35, 1.65),
             'xticks': [0, 1, 2, 4],
             'yticks': [-1],
             'x_label': '$\\tau$',
             'y_label': '$h(1-\\tau)$',
             'zero_line': False,
             'y_tick_label_side': 'left',
             'equal_aspect': True,
             'show_origin': True,
             'main_rect': {'start': 1, 'end': 4, 'height': -1},
             'overlap': {'start': 1, 'end': 2, 'height': -1, 'fill_alpha': 0.22},
             'texts': [{'text': '$h(1-\\tau)=-1$',
                        'x': 2.25,
                        'y': -0.62,
                        'fontsize': 15},
                       {'text': 'overlap 1<=tau<=2',
                        'x': 1.5,
                        'y': 0.45,
                        'fontsize': 14}]},
            {'xlim': (-0.4, 4.4),
             'ylim': (-3.65, 0.75),
             'xticks': [0, 1, 2, 4],
             'yticks': [-3],
             'x_label': '$\\tau$',
             'y_label': '$x(\\tau)h(1-\\tau)$',
             'zero_line': False,
             'y_tick_label_side': 'left',
             'equal_aspect': True,
             'show_origin': True,
             'main_rect': {'start': 1, 'end': 2, 'height': -3, 'fill_alpha': 0.18},
             'texts': [{'text': '$x(\\tau)h(1-\\tau)=-3$',
                        'x': 1.5,
                        'y': -1.42,
                        'fontsize': 15}]}],
 'figure_texts': [{'text': 'fixed $t=1$',
                   'x': 0.5,
                   'y': 0.978,
                   'fontsize': 15,
                   'va': 'top'}]}

if __name__ == "__main__":
    render_image(SPEC)
