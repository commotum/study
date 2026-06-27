from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


plt.rcParams.update(
    {
        "mathtext.fontset": "cm",
        "font.family": "serif",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)

BLUE = "#2f78b7"
AXIS = "#222222"
TEXT = "#444444"
GUIDE = "#777777"
GRID = "#000000"

TAU = r"$\tau$"
T_AXIS = r"$t$"


def configure():
    plt.rcParams.update(
        {
            "mathtext.fontset": "cm",
            "font.family": "serif",
            "figure.facecolor": "white",
            "axes.facecolor": "white",
        }
    )


def math_label(value):
    if isinstance(value, str):
        return value
    if abs(value - round(value)) < 1e-9:
        return f"${int(round(value))}$"
    return f"${value:g}$"


def setup_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks=(),
    yticks=(),
    xlabel=TAU,
    ylabel="",
    show_origin=True,
):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_facecolor("white")
    ax.grid(True, color=GRID, alpha=0.16, linewidth=0.6)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    x0, x1 = xlim
    y0, y1 = ylim
    ax.annotate(
        "",
        xy=(x1, 0),
        xytext=(x0, 0),
        arrowprops=dict(
            arrowstyle="-|>",
            color=AXIS,
            lw=1.35,
            shrinkA=0,
            shrinkB=0,
            mutation_scale=12,
        ),
        zorder=1,
    )
    ax.annotate(
        "",
        xy=(0, y1),
        xytext=(0, y0),
        arrowprops=dict(
            arrowstyle="-|>",
            color=AXIS,
            lw=1.35,
            shrinkA=0,
            shrinkB=0,
            mutation_scale=12,
        ),
        zorder=1,
    )
    tick_len = 0.07 * (y1 - y0)
    for item in xticks:
        if isinstance(item, (tuple, list)) and len(item) == 2:
            x, label = item
        else:
            x, label = item, None
        ax.plot([x, x], [-tick_len, tick_len], color=AXIS, lw=1.15, zorder=4)
        if label is None:
            label = math_label(x)
        ax.text(
            x,
            -0.11 * (y1 - y0),
            label,
            fontsize=14,
            ha="center",
            va="top",
            color=TEXT,
            zorder=5,
        )
    for item in yticks:
        if isinstance(item, (tuple, list)) and len(item) == 2:
            y, label = item
        else:
            y, label = item, None
        ax.plot([-tick_len, tick_len], [y, y], color=AXIS, lw=1.15, zorder=4)
        if label is None:
            label = math_label(y)
        ax.text(
            -0.02 * (x1 - x0),
            y,
            label,
            fontsize=13,
            ha="right",
            va="center",
            color=TEXT,
            zorder=5,
        )
    if show_origin:
        ax.text(
            0.06 * (x1 - x0) / 12,
            -0.04 * (y1 - y0),
            r"$0$",
            fontsize=14,
            ha="left",
            va="top",
            color=TEXT,
            zorder=5,
        )
    if ylabel:
        ax.text(
            0,
            y1 + 0.06 * (y1 - y0),
            ylabel,
            fontsize=18,
            ha="center",
            va="bottom",
            color=TEXT,
            clip_on=False,
            zorder=5,
        )
    ax.text(
        x1 + 0.05 * (x1 - x0),
        -0.03 * (y1 - y0),
        xlabel,
        fontsize=18,
        ha="left",
        va="center",
        color=TEXT,
        clip_on=False,
        zorder=5,
    )


def draw_support(ax, start, end, *, y, height, label=None, fill_alpha=0.12):
    ax.fill_between([start, end], [y, y], [y + height, y + height], color=BLUE, alpha=fill_alpha, zorder=2)
    ax.plot(
        [start, end, end, start, start],
        [y, y, y + height, y + height, y],
        color=BLUE,
        lw=2.2,
        zorder=3,
    )
    if label is not None:
        ax.text(
            (start + end) / 2.0,
            y + height + 0.08 * height + 0.05,
            label,
            fontsize=15,
            ha="center",
            va="bottom",
            color=TEXT,
            zorder=5,
        )


def draw_span(ax, start, end, *, alpha=0.09):
    if end > start:
        ax.axvspan(start, end, color=BLUE, alpha=alpha, zorder=1)


def draw_mark(ax, x, *, y0, y1, label=None, label_y=None):
    ax.plot([x, x], [y0, y1], color=GUIDE, lw=1.15, linestyle=(0, (1.1, 2.4)), zorder=2)
    if label is not None:
        ax.text(
            x,
            label_y if label_y is not None else y1 + 0.03,
            label,
            fontsize=14,
            ha="center",
            va="bottom",
            color=TEXT,
            zorder=5,
        )


def draw_note(ax, x, y, text, *, ha="center", va="center", size=14):
    ax.text(x, y, text, fontsize=size, ha=ha, va=va, color=TEXT, zorder=5)


def plot_triangle(ax, xs, ys):
    ax.plot(xs, ys, color=BLUE, lw=2.6, solid_capstyle="round", zorder=4)


def save(fig, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def draw_panel(ax, panel):
    setup_axes(
        ax,
        xlim=(-4.8, 8.8),
        ylim=(-0.55, 2.2),
        xticks=panel["xticks"],
        yticks=[],
        xlabel=TAU,
        ylabel="",
        show_origin=False,
    )
    overlap = panel["overlap"]
    if overlap is not None:
        draw_span(ax, overlap[0], overlap[1])
    draw_support(ax, panel["fixed"][0], panel["fixed"][1], y=1.18, height=0.42, label='$x(\\tau)$')
    draw_support(ax, panel["moving"][0], panel["moving"][1], y=0.34, height=0.42, label='$h(t-\\tau)$')
    for mark in panel["marks"]:
        draw_mark(ax, mark["x"], y0=mark["y0"], y1=mark["y1"], label=mark["label"], label_y=mark["label_y"])
    ax.set_title(panel["title"], fontsize=15, pad=8, color=TEXT)


def main():
    configure()
    fig, axes = plt.subplots(1, 3, figsize=(13.6, 4.7), dpi=160, sharey=True)
    panels = [{'title': 'first contact\n$t = 0$', 'fixed': (0, 4), 'moving': (-4, 0), 'overlap': None, 'xticks': [(-4, '$-4$'), (0, '$0$'), (4, '$4$'), (8, '$8$')], 'marks': [{'x': -4, 'y0': 0.0, 'y1': 1.1, 'label': '$t-4$', 'label_y': 1.48}, {'x': 0, 'y0': 0.0, 'y1': 1.1, 'label': '$t$', 'label_y': 1.48}]}, {'title': 'peak alignment\n$t = 4$', 'fixed': (0, 4), 'moving': (0, 4), 'overlap': (0, 4), 'xticks': [(-4, '$-4$'), (0, '$0$'), (4, '$4$'), (8, '$8$')], 'marks': [{'x': 0, 'y0': 0.0, 'y1': 1.1, 'label': '$t-4$', 'label_y': 1.48}, {'x': 4, 'y0': 0.0, 'y1': 1.1, 'label': '$t$', 'label_y': 1.48}]}, {'title': 'last contact\n$t = 8$', 'fixed': (0, 4), 'moving': (4, 8), 'overlap': None, 'xticks': [(-4, '$-4$'), (0, '$0$'), (4, '$4$'), (8, '$8$')], 'marks': [{'x': 4, 'y0': 0.0, 'y1': 1.1, 'label': '$t-4$', 'label_y': 1.48}, {'x': 8, 'y0': 0.0, 'y1': 1.1, 'label': '$t$', 'label_y': 1.48}]}]
    for ax, panel in zip(axes, panels):
        draw_panel(ax, panel)
    fig.subplots_adjust(wspace=0.24)
    save(fig, '/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/7.2--convolution-of-simple-signals-Images/images/l001-s002-qg-q001-q001.png')


if __name__ == '__main__':
    main()
