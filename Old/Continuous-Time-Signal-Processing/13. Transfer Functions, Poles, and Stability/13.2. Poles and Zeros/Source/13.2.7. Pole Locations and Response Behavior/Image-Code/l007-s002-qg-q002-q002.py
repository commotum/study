
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

BACKGROUND_COLOR = "white"
CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150
MARGIN_LEFT_PX = 115
MARGIN_RIGHT_PX = 120
MARGIN_BOTTOM_PX = 95
MARGIN_TOP_PX = 110

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"

SIGNAL_LW = 7.1 * 72 / CANONICAL_DPI
AXIS_LW = 4.3 * 72 / CANONICAL_DPI
TICK_LW = 2.7 * 72 / CANONICAL_DPI
GRID_LW = 1.3 * 72 / CANONICAL_DPI
GUIDE_LW = 3.3 * 72 / CANONICAL_DPI
ANNOTATION_LW = 2.9 * 72 / CANONICAL_DPI

TICK_LABEL_SIZE = 35.6 * 72 / CANONICAL_DPI
AXIS_LABEL_SIZE = 53.3 * 72 / CANONICAL_DPI
TOP_LABEL_SIZE = 57.8 * 72 / CANONICAL_DPI
ANNOTATION_SIZE = 33.3 * 72 / CANONICAL_DPI

TICK_HALF_LEN = 8.25 / PX_PER_DATA_UNIT
OPEN_MARKER_SIZE = 20.0 * 72 / CANONICAL_DPI
CLOSED_MARKER_SIZE = 17.8 * 72 / CANONICAL_DPI
ENDPOINT_EDGEWIDTH = 5.1 * 72 / CANONICAL_DPI
POLE_MARKER_SIZE = 21.0 * 72 / CANONICAL_DPI
POLE_MARKER_EDGEWIDTH = 5.1 * 72 / CANONICAL_DPI

X_TICK_LABEL_Y = -24 / PX_PER_DATA_UNIT
Y_TICK_LABEL_X = 18 / PX_PER_DATA_UNIT
ORIGIN_LABEL_X = 9 / PX_PER_DATA_UNIT
ORIGIN_LABEL_Y = -12 / PX_PER_DATA_UNIT
X_AXIS_LABEL_X_PAD = 15 / PX_PER_DATA_UNIT
X_AXIS_LABEL_Y = -4.5 / PX_PER_DATA_UNIT
Y_AXIS_LABEL_Y_PAD = 18 / PX_PER_DATA_UNIT

POINT_LABEL_OFFSET = (8 / PX_PER_DATA_UNIT, 8 / PX_PER_DATA_UNIT)
GRID_LINESTYLE = (0, (1.1, 2.4))
AXIS_ARROW_SHAFT_WIDTH_DATA = 4.3 / PX_PER_DATA_UNIT
AXIS_ARROW_KW = dict(
    angles="xy",
    scale_units="xy",
    scale=1,
    units="xy",
    width=AXIS_ARROW_SHAFT_WIDTH_DATA,
    headwidth=4.2,
    headlength=5.5,
    headaxislength=4.3,
    color=AXIS_COLOR,
    pivot="tail",
    clip_on=False,
)

CONFIG = {'covered_template': 's-plane-single-pole', 'xlim': (-3.5, 3.5), 'ylim': (-4.5, 4.5), 'xticks': [-3, -2, -1, 1, 2, 3], 'yticks': [-4, -3, -2, -1, 1, 2, 3, 4], 'x_axis_label': '$\\sigma$', 'y_axis_label': '$j\\omega$', 'poles': [{'x': 1, 'y': -2, 'label': '$1-j2$', 'label_offset': (0.1, -0.62), 'label_ha': 'left', 'label_va': 'top'}], 'guides': [{'x_values': [1, 1], 'y_values': [0, -2], 'color': '#777777'}, {'x_values': [0, 1], 'y_values': [-2, -2], 'color': '#777777'}], 'annotations': [{'text': '$\\sigma=1$', 'xy': (1, 0), 'xytext': (1.1, 0.35), 'arrow': False, 'ha': 'left', 'va': 'bottom', 'color': '#555555', 'fontsize': 11}, {'text': '$\\omega=-2$', 'xy': (0, -2), 'xytext': (-0.95, -2.55), 'arrow': False, 'ha': 'left', 'va': 'bottom', 'color': '#555555', 'fontsize': 11}], 'render_notes': ['Single-pole coordinate-reading prompt in the right-lower half-plane.', 'Guides isolate the positive real part and negative imaginary part.'], 'show_grid': True, 'show_origin': True, 'x_minor_grid_step': 1, 'y_minor_grid_step': 1, 'output_path': '/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/13.2--poles-and-zeros-Images/images/l007-s002-qg-q002-q002.png'}


def configure_matplotlib():
    plt.rcParams.update(
        {
            "mathtext.fontset": "cm",
            "font.family": "serif",
            "figure.facecolor": BACKGROUND_COLOR,
            "axes.facecolor": BACKGROUND_COLOR,
            "savefig.facecolor": BACKGROUND_COLOR,
        }
    )


configure_matplotlib()


def px_to_pt(px):
    return px * 72 / CANONICAL_DPI


def px_to_data(px):
    return px / PX_PER_DATA_UNIT


def make_figure(xlim, ylim):
    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]
    fig_w_px = MARGIN_LEFT_PX + x_range * PX_PER_DATA_UNIT + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_BOTTOM_PX + y_range * PX_PER_DATA_UNIT + MARGIN_TOP_PX
    fig, ax = plt.subplots(
        figsize=(fig_w_px / CANONICAL_DPI, fig_h_px / CANONICAL_DPI),
        dpi=CANONICAL_DPI,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=True,
    )
    return fig, ax


def math_label(value):
    if isinstance(value, str):
        return value
    numeric = float(value)
    rounded = round(numeric)
    if abs(numeric - rounded) < 1e-9:
        return rf"${int(rounded)}$"
    return rf"${numeric:g}$"


def draw_dotted_guide(ax, x_values, y_values, *, color=GUIDE_COLOR, lw=GUIDE_LW):
    ax.plot(
        x_values,
        y_values,
        color=color,
        linewidth=lw,
        linestyle=GRID_LINESTYLE,
        zorder=3,
    )


def draw_pole(ax, item):
    x = item["x"]
    y = item["y"]
    marker = item.get("marker", "x")
    size = item.get("markersize", POLE_MARKER_SIZE)
    edgewidth = item.get("markeredgewidth", POLE_MARKER_EDGEWIDTH)
    color = item.get("color", SIGNAL_COLOR)
    kwargs = dict(
        marker=marker,
        markersize=size,
        markeredgewidth=edgewidth,
        linestyle="None",
        zorder=item.get("zorder", 6),
    )
    if marker != "x":
        kwargs["markerfacecolor"] = item.get("markerfacecolor", "white")
        kwargs["markeredgecolor"] = item.get("markeredgecolor", color)
    else:
        kwargs["markeredgecolor"] = item.get("markeredgecolor", color)
    ax.plot(x, y, **kwargs)
    label = item.get("label")
    if label is not None:
        dx, dy = item.get("label_offset", POINT_LABEL_OFFSET)
        ax.text(
            x + dx,
            y + dy,
            label,
            fontsize=item.get("label_size", ANNOTATION_SIZE),
            ha=item.get("label_ha", "left"),
            va=item.get("label_va", "bottom"),
            color=item.get("label_color", LABEL_COLOR),
            clip_on=False,
            zorder=item.get("zorder", 6) + 1,
        )


def draw_annotation(ax, item):
    color = item.get("color", ANNOTATION_COLOR)
    fontsize = item.get("fontsize", ANNOTATION_SIZE)
    ha = item.get("ha", "left")
    va = item.get("va", "bottom")
    clip_on = item.get("clip_on", False)
    if item.get("arrow", False):
        arrowprops = dict(
            arrowstyle="->",
            color=item.get("arrow_color", GUIDE_COLOR),
            lw=item.get("arrow_lw", 1.2),
            shrinkA=0,
            shrinkB=0,
        )
        ax.annotate(
            item["text"],
            xy=item["xy"],
            xytext=item["xytext"],
            textcoords="data",
            fontsize=fontsize,
            ha=ha,
            va=va,
            color=color,
            arrowprops=arrowprops,
            clip_on=clip_on,
        )
    else:
        ax.text(
            item["xytext"][0],
            item["xytext"][1],
            item["text"],
            fontsize=fontsize,
            ha=ha,
            va=va,
            color=color,
            clip_on=clip_on,
        )


def setup_axes(ax, cfg):
    xlim = tuple(cfg["xlim"])
    ylim = tuple(cfg["ylim"])
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    xticks = cfg["xticks"]
    yticks = cfg["yticks"]
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    x_step = cfg.get("x_minor_grid_step", 1)
    y_step = cfg.get("y_minor_grid_step", 1)
    if x_step is not None and x_step > 0:
        ax.xaxis.set_minor_locator(MultipleLocator(x_step))
    if y_step is not None and y_step > 0:
        ax.yaxis.set_minor_locator(MultipleLocator(y_step))
    if cfg.get("show_grid", True):
        ax.grid(True, which="both", linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
        ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    x0, x1 = xlim
    y0, y1 = ylim
    ax.quiver(x0, 0, x1 - x0, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y0, 0, y1 - y0, **AXIS_ARROW_KW)
    x_tick_labels = cfg.get("x_tick_labels", xticks)
    y_tick_labels = cfg.get("y_tick_labels", yticks)
    for t, label in zip(xticks, x_tick_labels):
        if abs(float(t)) < 1e-12:
            continue
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if cfg.get("show_x_tick_labels", True):
            ax.text(
                t,
                X_TICK_LABEL_Y,
                math_label(label),
                fontsize=TICK_LABEL_SIZE,
                ha="center",
                va="top",
                color=TICK_LABEL_COLOR,
                zorder=6,
                clip_on=False,
            )
    for y, label in zip(yticks, y_tick_labels):
        if abs(float(y)) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if cfg.get("show_y_tick_labels", True):
            side = cfg.get("y_tick_label_side", "left")
            if side == "right":
                ax.text(
                    Y_TICK_LABEL_X,
                    y,
                    math_label(label),
                    fontsize=TICK_LABEL_SIZE,
                    ha="left",
                    va="center",
                    color=TICK_LABEL_COLOR,
                    zorder=6,
                    clip_on=False,
                )
            else:
                ax.text(
                    -Y_TICK_LABEL_X,
                    y,
                    math_label(label),
                    fontsize=TICK_LABEL_SIZE,
                    ha="right",
                    va="center",
                    color=TICK_LABEL_COLOR,
                    zorder=6,
                    clip_on=False,
                )
    if cfg.get("show_origin", True):
        ax.text(
            ORIGIN_LABEL_X,
            ORIGIN_LABEL_Y,
            r"$0$",
            fontsize=TICK_LABEL_SIZE,
            ha="left",
            va="top",
            color=TICK_LABEL_COLOR,
            zorder=6,
            clip_on=False,
        )
    x_axis_label = cfg.get("x_axis_label", r"$\sigma$")
    y_axis_label = cfg.get("y_axis_label", r"$j\omega$")
    if x_axis_label is not None:
        ax.text(
            x1 + X_AXIS_LABEL_X_PAD,
            X_AXIS_LABEL_Y,
            x_axis_label,
            fontsize=AXIS_LABEL_SIZE,
            ha="left",
            va="center",
            color=LABEL_COLOR,
            clip_on=False,
        )
    if y_axis_label is not None:
        ax.text(
            0,
            y1 + Y_AXIS_LABEL_Y_PAD,
            y_axis_label,
            fontsize=TOP_LABEL_SIZE,
            ha="center",
            va="bottom",
            color=LABEL_COLOR,
            clip_on=False,
        )


def save_figure(fig, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=CANONICAL_DPI, bbox_inches="tight", facecolor=BACKGROUND_COLOR)
    plt.close(fig)


def render():
    cfg = CONFIG
    fig, ax = make_figure(tuple(cfg["xlim"]), tuple(cfg["ylim"]))
    setup_axes(ax, cfg)
    for span in cfg.get("shading", []):
        ax.axvspan(span["x0"], span["x1"], color=span.get("color", SIGNAL_COLOR), alpha=span.get("alpha", 0.06), zorder=span.get("zorder", 0))
    for guide in cfg.get("guides", []):
        draw_dotted_guide(ax, guide["x_values"], guide["y_values"], color=guide.get("color", GUIDE_COLOR), lw=guide.get("lw", GUIDE_LW))
    for pole in cfg.get("poles", []):
        draw_pole(ax, pole)
    for annotation in cfg.get("annotations", []):
        draw_annotation(ax, annotation)
    save_figure(fig, cfg["output_path"])


if __name__ == "__main__":
    render()
