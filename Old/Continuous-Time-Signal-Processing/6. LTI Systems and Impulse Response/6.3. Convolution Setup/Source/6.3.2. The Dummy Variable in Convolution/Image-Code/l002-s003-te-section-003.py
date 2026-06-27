from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

COURSE_NAME = "Continuous Time Signal Processing"
COURSE_CODE = "CTS"
COURSE_ID = "EE01"
UNIT_NUMBER = 6
UNIT_NAME = "Unit 6"
MODULE_ID = "EE01-M06-03"
MODULE_NUMBER = "6.3"
MODULE_NAME = "Convolution Setup"

DEFAULT_DPI = 160
DEFAULT_SIGNAL_FIGSIZE = (9.12, 7.68)
DEFAULT_SQUARE_FIGSIZE = (5.6, 5.6)

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

BLOCK_EDGE_LW = 1.6
BLOCK_FACE_COLOR = "white"
ARROW_HEAD_SCALE = 14


def apply_ct_style() -> None:
    plt.rcParams.update(
        {
            "mathtext.fontset": "cm",
            "font.family": "serif",
            "figure.facecolor": "white",
            "axes.facecolor": "white",
        }
    )


apply_ct_style()


def math_label(value):
    if isinstance(value, str):
        return value
    if abs(value - int(value)) < 1e-9:
        return rf"${int(value)}$"
    return rf"${value:g}$"


def make_figure(figsize=DEFAULT_SIGNAL_FIGSIZE, dpi=DEFAULT_DPI):
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    return fig, ax


def finalize_figure(fig, output_path, *, dpi=DEFAULT_DPI):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, bbox_inches="tight", facecolor="white", dpi=dpi)


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
        ax.text(
            t,
            -0.16,
            math_label(t),
            fontsize=TICK_LABEL_SIZE,
            ha="center",
            va="top",
            color=TICK_LABEL_COLOR,
            zorder=6,
        )

    for y in yticks:
        if abs(y) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if y_tick_label_side == "right":
            ax.text(
                0.12,
                y,
                math_label(y),
                fontsize=TICK_LABEL_SIZE,
                ha="left",
                va="center",
                color=TICK_LABEL_COLOR,
                zorder=6,
            )
        else:
            ax.text(
                -0.12,
                y,
                math_label(y),
                fontsize=TICK_LABEL_SIZE,
                ha="right",
                va="center",
                color=TICK_LABEL_COLOR,
                zorder=6,
            )

    if show_origin:
        ax.text(
            0.06,
            -0.08,
            r"$0$",
            fontsize=TICK_LABEL_SIZE,
            ha="left",
            va="top",
            color=TICK_LABEL_COLOR,
            zorder=6,
        )

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
    ax.plot(t, x, color=color, linewidth=lw, solid_capstyle="round", zorder=zorder)


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


def draw_support_bracket(ax, t_start, t_end, *, y=-0.38, label="duration"):
    ax.plot([t_start, t_end], [y, y], color=ANNOTATION_COLOR, linewidth=1.3, zorder=5)
    ax.plot([t_start, t_start], [y - 0.06, y + 0.06], color=ANNOTATION_COLOR, linewidth=1.3, zorder=5)
    ax.plot([t_end, t_end], [y - 0.06, y + 0.06], color=ANNOTATION_COLOR, linewidth=1.3, zorder=5)
    if label:
        ax.text(
            (t_start + t_end) / 2,
            y - 0.12,
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


def draw_amplitude_bracket(ax, x_bracket, y0, y1):
    ax.plot([x_bracket, x_bracket], [y0, y1], color=ANNOTATION_COLOR, linewidth=1.3, zorder=5)
    ax.plot([x_bracket - 0.07, x_bracket + 0.07], [y0, y0], color=ANNOTATION_COLOR, linewidth=1.3, zorder=5)
    ax.plot([x_bracket - 0.07, x_bracket + 0.07], [y1, y1], color=ANNOTATION_COLOR, linewidth=1.3, zorder=5)


def setup_block_diagram_axes(ax, *, xlim, ylim, equal_aspect=False):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    if equal_aspect:
        ax.set_aspect("equal", adjustable="box")
    ax.set_axis_off()
    ax.set_facecolor("white")


def draw_box(ax, x, y, w, h, *, label=None, fontsize=18, label_color=LABEL_COLOR):
    box = Rectangle(
        (x, y),
        w,
        h,
        facecolor=BLOCK_FACE_COLOR,
        edgecolor=AXIS_COLOR,
        linewidth=BLOCK_EDGE_LW,
        zorder=2,
    )
    ax.add_patch(box)
    if label is not None:
        ax.text(
            x + w / 2,
            y + h / 2,
            label,
            fontsize=fontsize,
            ha="center",
            va="center",
            color=label_color,
            zorder=3,
        )
    return box


def draw_arrow(ax, start, end, *, color=AXIS_COLOR, lw=1.8, mutation_scale=ARROW_HEAD_SCALE):
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops=dict(
            arrowstyle="-|>",
            color=color,
            linewidth=lw,
            shrinkA=0,
            shrinkB=0,
            mutation_scale=mutation_scale,
        ),
        zorder=4,
    )


def draw_label(ax, x, y, text, *, fontsize=18, color=LABEL_COLOR, ha="center", va="center"):
    ax.text(x, y, text, fontsize=fontsize, color=color, ha=ha, va=va)


def draw_signal_arrow(ax, x0, y0, x1, y1, *, color=AXIS_COLOR, lw=1.8):
    draw_arrow(ax, (x0, y0), (x1, y1), color=color, lw=lw)


def save_ct_figure(fig, output_path, *, dpi=DEFAULT_DPI):
    finalize_figure(fig, output_path, dpi=dpi)


def main():
    fig, ax = make_figure()
    setup_ct_signal_axes(
        ax,
        xlim=[-1.4, 5.4],
        ylim=[-0.7, 2.8],
        xticks=[-1, 0, 1, 2, 3, 4, 5],
        yticks=[2],
        x_axis_label="$\\tau$",
        y_axis_label="$x(\\tau)$",
    )
    plot_signal(ax, [-1, 0, 0, 4, 4, 5], [0, 0, 2, 2, 0, 0])
    fig.tight_layout()
    save_ct_figure(fig, "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/6.3--convolution-setup-Images/images/l002-s003-te-section-003.png")
    plt.close(fig)


if __name__ == "__main__":
    main()
