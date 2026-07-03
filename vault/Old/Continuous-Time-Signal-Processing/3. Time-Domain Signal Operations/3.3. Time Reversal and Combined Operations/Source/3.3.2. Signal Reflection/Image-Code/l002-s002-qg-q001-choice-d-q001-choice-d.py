
from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
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

def configure_matplotlib():
    mpl.rcParams.update(
        {
            "mathtext.fontset": "cm",
            "font.family": "serif",
            "figure.facecolor": BACKGROUND_COLOR,
            "axes.facecolor": BACKGROUND_COLOR,
            "savefig.facecolor": BACKGROUND_COLOR,
            "axes.grid": False,
        }
    )

configure_matplotlib()

def px_to_pt(px):
    return px * 72 / CANONICAL_DPI

def px_to_data(px):
    return px / PX_PER_DATA_UNIT

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"

SIGNAL_LW = px_to_pt(7.1)
AXIS_LW = px_to_pt(4.3)
TICK_LW = px_to_pt(2.7)
GRID_LW = px_to_pt(1.3)

TICK_LABEL_SIZE = px_to_pt(35.6)
AXIS_LABEL_SIZE = px_to_pt(53.3)
TOP_LABEL_SIZE = px_to_pt(57.8)
ANNOTATION_SIZE = px_to_pt(33.3)

TICK_HALF_LEN = px_to_data(8.25)
X_TICK_LABEL_Y = -px_to_data(24)
Y_TICK_LABEL_X = px_to_data(18)
ORIGIN_LABEL_X = px_to_data(9)
ORIGIN_LABEL_Y = -px_to_data(12)
X_AXIS_LABEL_X_PAD = px_to_data(15)
X_AXIS_LABEL_Y = -px_to_data(4.5)
Y_AXIS_LABEL_Y_PAD = px_to_data(18)

AXIS_ARROW_SHAFT_WIDTH_DATA = px_to_data(4.3)

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

def make_ct_signal_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]
    axes_w_px = x_range * PX_PER_DATA_UNIT
    axes_h_px = y_range * PX_PER_DATA_UNIT
    fig_w_px = MARGIN_LEFT_PX + axes_w_px + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_BOTTOM_PX + axes_h_px + MARGIN_TOP_PX
    fig, ax = plt.subplots(
        figsize=(fig_w_px / dpi, fig_h_px / dpi),
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=True,
    )
    return fig, ax

def make_two_panel_ct_signal_figure(xlim, ylim, *, gap_px=46, dpi=CANONICAL_DPI):
    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]
    axes_w_px = x_range * PX_PER_DATA_UNIT
    axes_h_px = y_range * PX_PER_DATA_UNIT
    fig_w_px = MARGIN_LEFT_PX + 2 * axes_w_px + gap_px + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_BOTTOM_PX + axes_h_px + MARGIN_TOP_PX
    fig, axes = plt.subplots(
        1,
        2,
        figsize=(fig_w_px / dpi, fig_h_px / dpi),
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=True,
    )
    return fig, axes

def math_label(value):
    if isinstance(value, str):
        return value
    numeric = float(value)
    rounded = round(numeric)
    if np.isclose(numeric, rounded):
        return rf"${int(rounded)}$"
    return rf"${numeric:g}$"

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
    x_minor_grid_step=1,
    y_minor_grid_step=1,
    equal_aspect=True,
):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    if equal_aspect:
        ax.set_aspect("equal", adjustable="box")
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.xaxis.set_minor_locator(MultipleLocator(x_minor_grid_step))
    ax.yaxis.set_minor_locator(MultipleLocator(y_minor_grid_step))
    if show_grid:
        ax.grid(True, which="both", linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
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
            X_TICK_LABEL_Y,
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
                Y_TICK_LABEL_X,
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
                -Y_TICK_LABEL_X,
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
            ORIGIN_LABEL_X,
            ORIGIN_LABEL_Y,
            r"$0$",
            fontsize=TICK_LABEL_SIZE,
            ha="left",
            va="top",
            color=TICK_LABEL_COLOR,
            zorder=6,
        )
    if x_axis_label is not None:
        ax.text(
            x_axis_end + X_AXIS_LABEL_X_PAD,
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
            y_axis_end + Y_AXIS_LABEL_Y_PAD,
            y_axis_label,
            fontsize=TOP_LABEL_SIZE,
            ha="center",
            va="bottom",
            color=LABEL_COLOR,
            clip_on=False,
        )

def draw_spike(ax, t, height, *, base=0.0):
    ax.plot(
        [t, t],
        [base, height],
        color=SIGNAL_COLOR,
        linewidth=SIGNAL_LW,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=4,
    )

def draw_pulse(ax, start, end, height, *, base=0.0):
    ax.plot(
        [start, start, end, end],
        [base, height, height, base],
        color=SIGNAL_COLOR,
        linewidth=SIGNAL_LW,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=4,
    )

def draw_segment(ax, points):
    pts = np.asarray(points, dtype=float)
    ax.plot(
        pts[:, 0],
        pts[:, 1],
        color=SIGNAL_COLOR,
        linewidth=SIGNAL_LW,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=4,
    )

def draw_component(ax, component):
    kind = component["kind"]
    if kind == "spike":
        draw_spike(ax, component["t"], component["height"], base=component.get("base", 0.0))
    elif kind == "pulse":
        draw_pulse(ax, component["start"], component["end"], component["height"], base=component.get("base", 0.0))
    elif kind == "segment":
        draw_segment(ax, component["points"])
    else:
        raise ValueError(f"Unknown component kind: {kind}")

def draw_components(ax, components):
    for component in components:
        draw_component(ax, component)

def draw_texts(ax, texts):
    for text in texts:
        ax.text(
            text["x"],
            text["y"],
            text["text"],
            fontsize=text.get("fontsize", ANNOTATION_SIZE),
            ha=text.get("ha", "center"),
            va=text.get("va", "bottom"),
            color=text.get("color", LABEL_COLOR),
            clip_on=text.get("clip_on", False),
            zorder=text.get("zorder", 7),
        )

def save_figure(fig, output_path, *, dpi=CANONICAL_DPI):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        output_path,
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        bbox_inches="tight",
    )
    plt.close(fig)

def render(spec):
    layout = spec["layout"]
    if layout == "single":
        fig, ax = make_ct_signal_figure(spec["xlim"], spec["ylim"])
        setup_ct_signal_axes(
            ax,
            xlim=spec["xlim"],
            ylim=spec["ylim"],
            xticks=spec["xticks"],
            yticks=spec["yticks"],
            x_axis_label=spec.get("x_label", r"$t$"),
            y_axis_label=spec.get("y_label", r"$x(t)$"),
            show_grid=spec.get("show_grid", True),
            show_origin=spec.get("show_origin", True),
            y_tick_label_side=spec.get("y_tick_label_side", "left"),
            x_minor_grid_step=spec.get("x_minor_grid_step", 1),
            y_minor_grid_step=spec.get("y_minor_grid_step", 1),
            equal_aspect=spec.get("equal_aspect", True),
        )
        draw_components(ax, spec.get("components", []))
        draw_texts(ax, spec.get("texts", []))
    elif layout == "two-panel":
        fig, axes = make_two_panel_ct_signal_figure(spec["xlim"], spec["ylim"], gap_px=spec.get("gap_px", 46))
        for ax, panel in zip(axes, (spec["left"], spec["right"])):
            setup_ct_signal_axes(
                ax,
                xlim=spec["xlim"],
                ylim=spec["ylim"],
                xticks=spec["xticks"],
                yticks=spec["yticks"],
                x_axis_label=panel.get("x_label", r"$t$"),
                y_axis_label=panel.get("y_label", r"$x(t)$"),
                show_grid=spec.get("show_grid", True),
                show_origin=spec.get("show_origin", True),
                y_tick_label_side=panel.get("y_tick_label_side", spec.get("y_tick_label_side", "left")),
                x_minor_grid_step=spec.get("x_minor_grid_step", 1),
                y_minor_grid_step=spec.get("y_minor_grid_step", 1),
                equal_aspect=spec.get("equal_aspect", True),
            )
            draw_components(ax, panel.get("components", []))
            draw_texts(ax, panel.get("texts", []))
    else:
        raise ValueError(f"Unknown layout: {layout}")
    save_figure(fig, spec["output_path"])


SPEC = {'layout': 'single',
 'output_path': '/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/3.3--time-reversal-and-combined-operations-Images/images/l002-s002-qg-q001-choice-d-q001-choice-d.png',
 'xlim': [-5.5, 5.5],
 'ylim': [-0.8, 2.8],
 'xticks': [-4, -2, 2, 4],
 'yticks': [1, 2],
 'components': [{'kind': 'spike', 't': -2, 'height': 2, 'base': 0.0}],
 'texts': [],
 'template': 'single-peak-reflection-plot',
 'notes': ['peak placed at the wrong negative time'],
 'y_label': '$x(t)$',
 'y_tick_label_side': 'left',
 'show_grid': True,
 'show_origin': True,
 'equal_aspect': True}

render(SPEC)
