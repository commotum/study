
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

plt.rcParams.update(
    {
        "mathtext.fontset": "cm",
        "font.family": "serif",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)


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
    x_axis_label=r"$\tau$",
    y_axis_label=r"$x(\tau)$",
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

    if x_axis_label:
        ax.text(x_axis_end + x_pad, -0.03, x_axis_label, fontsize=AXIS_LABEL_SIZE, ha="left", va="center", color=LABEL_COLOR, clip_on=False)
    if y_axis_label:
        ax.text(0, y_axis_end + y_pad, y_axis_label, fontsize=TOP_LABEL_SIZE, ha="center", va="bottom", color=LABEL_COLOR, clip_on=False)


def draw_pulse_rect(
    ax,
    start,
    end,
    height,
    *,
    label=None,
    label_y=None,
    baseline=0.0,
    fill=False,
    facecolor="none",
    edgecolor=SIGNAL_COLOR,
    lw=SIGNAL_LW,
    alpha=1.0,
    zorder=4,
):
    rect = Rectangle(
        (start, baseline),
        end - start,
        height - baseline,
        fill=fill,
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=lw,
        alpha=alpha,
        zorder=zorder,
    )
    ax.add_patch(rect)
    if label is not None:
        y = height + 0.12 if label_y is None else label_y
        ax.text(
            (start + end) / 2,
            y,
            label,
            fontsize=ANNOTATION_SIZE,
            ha="center",
            va="bottom",
            color=LABEL_COLOR,
            zorder=zorder + 2,
        )
    return rect


def draw_overlap_fill(ax, start, end, height, *, baseline=0.0, alpha=0.18, zorder=2):
    rect = Rectangle(
        (start, baseline),
        end - start,
        height - baseline,
        fill=True,
        facecolor=SIGNAL_COLOR,
        edgecolor=SIGNAL_COLOR,
        linewidth=1.0,
        alpha=alpha,
        zorder=zorder,
    )
    ax.add_patch(rect)
    return rect


def draw_dotted_guide(ax, x_values, y_values):
    ax.plot(
        x_values,
        y_values,
        color=GUIDE_COLOR,
        linewidth=GUIDE_LW,
        linestyle=(0, (1.1, 2.4)),
        zorder=3,
    )


def draw_support_bracket(ax, start, end, y=-0.35, *, label=None, color=ANNOTATION_COLOR, label_offset=-0.12):
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
            zorder=6,
        )


def save_figure(fig, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def render_single_overlap_scene(
    output_path,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    fixed_interval,
    fixed_height,
    fixed_label,
    moving_interval,
    moving_height,
    moving_label,
    overlap_start,
    overlap_end,
    width_label,
    product_text,
    x_axis_label=r"$\tau$",
    y_axis_label=r"$x(\tau)$",
    lower_texts=None,
    show_grid=True,
    show_origin=True,
    y_tick_label_side="left",
):
    fig, ax = new_ct_figure()
    setup_ct_signal_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=xticks,
        yticks=yticks,
        x_axis_label=x_axis_label,
        y_axis_label=y_axis_label,
        show_grid=show_grid,
        show_origin=show_origin,
        y_tick_label_side=y_tick_label_side,
    )

    fixed_start, fixed_end = fixed_interval
    moving_start, moving_end = moving_interval

    draw_pulse_rect(ax, fixed_start, fixed_end, fixed_height, label=fixed_label)
    draw_pulse_rect(ax, moving_start, moving_end, moving_height, label=moving_label)

    overlap_height = min(fixed_height, moving_height)
    if overlap_end > overlap_start:
        draw_overlap_fill(ax, overlap_start, overlap_end, overlap_height)
        draw_dotted_guide(ax, [overlap_start, overlap_start], [0, overlap_height])
        draw_dotted_guide(ax, [overlap_end, overlap_end], [0, overlap_height])
        draw_support_bracket(ax, overlap_start, overlap_end, y=-0.28, label=width_label)
        ax.text(
            (overlap_start + overlap_end) / 2,
            max(fixed_height, moving_height) + 0.22,
            product_text,
            fontsize=ANNOTATION_SIZE,
            ha="center",
            va="bottom",
            color=LABEL_COLOR,
            zorder=7,
        )

    if lower_texts:
        for x_pos, y_pos, text in lower_texts:
            ax.text(
                x_pos,
                y_pos,
                text,
                fontsize=ANNOTATION_SIZE,
                ha="left",
                va="center",
                color=LABEL_COLOR,
                zorder=7,
            )

    save_figure(fig, output_path)


def render_sequence_scene(
    output_path,
    *,
    panels,
    xlim,
    ylim,
    xticks,
    yticks,
    fixed_interval,
    fixed_height,
    fixed_label,
    moving_height,
    moving_label,
    fig_size,
    global_caption=None,
    y_axis_label=r"$x(\tau)$",
):
    fig, axs = plt.subplots(1, len(panels), figsize=fig_size, dpi=DPI, sharey=True)
    if len(panels) == 1:
        axs = [axs]

    if global_caption:
        fig.text(0.5, 0.975, global_caption, ha="center", va="top", fontsize=ANNOTATION_SIZE, color=LABEL_COLOR)

    fixed_start, fixed_end = fixed_interval
    for index, (ax, panel) in enumerate(zip(axs, panels)):
        setup_ct_signal_axes(
            ax,
            xlim=xlim,
            ylim=ylim,
            xticks=xticks,
            yticks=yticks,
            x_axis_label=r"$\tau$",
            y_axis_label=y_axis_label if panel.get("show_ylabel", index == 0) else "",
            show_grid=True,
            show_origin=panel.get("show_origin", index == 0),
            y_tick_label_side=panel.get("y_tick_label_side", "left"),
        )

        moving_start, moving_end = panel["moving_interval"]
        overlap_start, overlap_end = panel["overlap_interval"]
        panel_fixed_label = panel.get("fixed_label", fixed_label)
        panel_moving_label = panel.get("moving_label", moving_label)

        draw_pulse_rect(ax, fixed_start, fixed_end, fixed_height, label=panel_fixed_label)
        draw_pulse_rect(ax, moving_start, moving_end, moving_height, label=panel_moving_label)

        overlap_height = min(fixed_height, moving_height)
        if overlap_end > overlap_start:
            draw_overlap_fill(ax, overlap_start, overlap_end, overlap_height)
            draw_dotted_guide(ax, [overlap_start, overlap_start], [0, overlap_height])
            draw_dotted_guide(ax, [overlap_end, overlap_end], [0, overlap_height])
            draw_support_bracket(
                ax,
                overlap_start,
                overlap_end,
                y=panel.get("bracket_y", -0.28),
                label=panel.get("length_label"),
            )
        else:
            no_overlap_text = panel.get("no_overlap_text")
            if no_overlap_text:
                ax.text(
                    0.5,
                    0.62,
                    no_overlap_text,
                    transform=ax.transAxes,
                    fontsize=ANNOTATION_SIZE,
                    ha="center",
                    va="center",
                    color=LABEL_COLOR,
                    zorder=7,
                )

        ax.text(
            0.5,
            1.08,
            panel["panel_label"],
            transform=ax.transAxes,
            fontsize=ANNOTATION_SIZE,
            ha="center",
            va="bottom",
            color=LABEL_COLOR,
            zorder=7,
        )

        if panel.get("top_note"):
            ax.text(
                0.5,
                0.96,
                panel["top_note"],
                transform=ax.transAxes,
                fontsize=ANNOTATION_SIZE - 1,
                ha="center",
                va="bottom",
                color=LABEL_COLOR,
                zorder=7,
            )

    fig.subplots_adjust(wspace=0.24, top=0.84, bottom=0.18)
    save_figure(fig, output_path)


OUTPUT_PATH = r"/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/7.2--convolution-of-simple-signals-Images/images/l005-s006-te-section-006.png"

def main():
    render_sequence_scene(
        OUTPUT_PATH,
        panels=[{'panel_label': '$t<0$', 'moving_interval': (-1, 0), 'overlap_interval': (0, 0), 'length_label': '$0$', 'no_overlap_text': '$0$', 'show_ylabel': True, 'show_origin': True}, {'panel_label': '$0<t<1$', 'moving_interval': (0, 1), 'overlap_interval': (0, 1), 'length_label': '$t$', 'show_ylabel': False, 'show_origin': False}, {'panel_label': '$1<t<3$', 'moving_interval': (1.5, 2.5), 'overlap_interval': (1.5, 2.5), 'length_label': '$1$', 'show_ylabel': False, 'show_origin': False}, {'panel_label': '$3<t<4$', 'moving_interval': (2.5, 3.5), 'overlap_interval': (2.5, 3), 'length_label': '$4-t$', 'show_ylabel': False, 'show_origin': False}, {'panel_label': '$t>4$', 'moving_interval': (3.2, 4.2), 'overlap_interval': (0, 0), 'length_label': '$0$', 'no_overlap_text': '$0$', 'show_ylabel': False, 'show_origin': False}],
        xlim=(-1.4, 4.6),
        ylim=(-0.7, 2.75),
        xticks=[0, 1, 3, 4],
        yticks=[0, 1, 2],
        fixed_interval=(0, 3),
        fixed_height=2,
        fixed_label='$x(\\tau)=2$',
        moving_height=1,
        moving_label='$h(t-\\tau)=1$',
        fig_size=(18.2, 3.7),
        global_caption='$2 \\times 1 = 2$',
    )


if __name__ == "__main__":
    main()
