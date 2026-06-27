from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


mpl.rcParams.update(
    {
        "mathtext.fontset": "cm",
        "font.family": "serif",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
    }
)


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

SIGNAL_LW = 7.1 * 72 / CANONICAL_DPI
AXIS_LW = 4.3 * 72 / CANONICAL_DPI
TICK_LW = 2.7 * 72 / CANONICAL_DPI
GRID_LW = 1.3 * 72 / CANONICAL_DPI

TICK_LABEL_SIZE = 35.6 * 72 / CANONICAL_DPI
AXIS_LABEL_SIZE = 53.3 * 72 / CANONICAL_DPI
TOP_LABEL_SIZE = 57.8 * 72 / CANONICAL_DPI
ANNOTATION_SIZE = 33.3 * 72 / CANONICAL_DPI

TICK_HALF_LEN = 8.25 / PX_PER_DATA_UNIT
X_TICK_LABEL_Y = -24 / PX_PER_DATA_UNIT
Y_TICK_LABEL_X = 18 / PX_PER_DATA_UNIT
ORIGIN_LABEL_X = 9 / PX_PER_DATA_UNIT
ORIGIN_LABEL_Y = -12 / PX_PER_DATA_UNIT
X_AXIS_LABEL_X_PAD = 15 / PX_PER_DATA_UNIT
X_AXIS_LABEL_Y = -4.5 / PX_PER_DATA_UNIT
Y_AXIS_LABEL_Y_PAD = 18 / PX_PER_DATA_UNIT

AXIS_ARROW_KW = dict(
    angles="xy",
    scale_units="xy",
    scale=1,
    units="xy",
    width=4.3 / PX_PER_DATA_UNIT,
    headwidth=4.2,
    headlength=5.5,
    headaxislength=4.3,
    color=AXIS_COLOR,
    pivot="tail",
    clip_on=False,
)

DEFAULT_SAVEFIG_KW = dict(
    dpi=CANONICAL_DPI,
    facecolor="white",
    bbox_inches="tight",
)


def px_to_pt(px: float) -> float:
    return px * 72 / CANONICAL_DPI


def px_to_data(px: float) -> float:
    return px / PX_PER_DATA_UNIT


def make_ct_signal_figure(xlim: tuple[float, float], ylim: tuple[float, float]):
    x_range = float(xlim[1] - xlim[0])
    y_range = float(ylim[1] - ylim[0])

    fig_w_px = MARGIN_LEFT_PX + x_range * PX_PER_DATA_UNIT + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_BOTTOM_PX + y_range * PX_PER_DATA_UNIT + MARGIN_TOP_PX

    fig, ax = plt.subplots(
        figsize=(fig_w_px / CANONICAL_DPI, fig_h_px / CANONICAL_DPI),
        dpi=CANONICAL_DPI,
        facecolor="white",
        constrained_layout=True,
    )
    return fig, ax


def math_label(value) -> str:
    if isinstance(value, str):
        return value
    numeric = float(value)
    rounded = int(np.rint(numeric))
    if np.isclose(numeric, rounded):
        return rf"${rounded}$"
    return rf"${numeric:g}$"


def setup_ct_signal_axes(
    ax,
    *,
    xlim: tuple[float, float],
    ylim: tuple[float, float],
    xticks,
    yticks,
    x_axis_label: str = r"$t$",
    y_axis_label: str = r"$x(t)$",
    show_grid: bool = True,
    show_origin: bool = True,
    y_tick_label_side: str = "left",
    x_minor_grid_step: float = 1,
    y_minor_grid_step: float = 1,
):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")

    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(x_minor_grid_step))
    ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(y_minor_grid_step))

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

    for tick in xticks:
        if np.isclose(tick, 0):
            continue
        ax.plot([tick, tick], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(
            tick,
            X_TICK_LABEL_Y,
            math_label(tick),
            fontsize=TICK_LABEL_SIZE,
            ha="center",
            va="top",
            color=TICK_LABEL_COLOR,
            zorder=6,
        )

    for tick in yticks:
        if np.isclose(tick, 0):
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [tick, tick], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if y_tick_label_side == "right":
            label_x = Y_TICK_LABEL_X
            label_ha = "left"
        else:
            label_x = -Y_TICK_LABEL_X
            label_ha = "right"
        ax.text(
            label_x,
            tick,
            math_label(tick),
            fontsize=TICK_LABEL_SIZE,
            ha=label_ha,
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
    return ax


def plot_signal(ax, t, x, *, lw: float = SIGNAL_LW, color: str = SIGNAL_COLOR, zorder: int = 4):
    ax.plot(
        t,
        x,
        color=color,
        linewidth=lw,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=zorder,
    )


def save_figure(fig, output_path: Path | str):
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, **DEFAULT_SAVEFIG_KW)


def label_text(ax, x: float, y: float, text: str, *, ha: str = "center", va: str = "bottom"):
    ax.text(
        x,
        y,
        text,
        fontsize=ANNOTATION_SIZE,
        ha=ha,
        va=va,
        color=LABEL_COLOR,
        clip_on=False,
        zorder=7,
    )


def render():
    xlim = (-1.55, 3.55)
    ylim = (-0.45, 2.55)

    fig, ax = make_ct_signal_figure(xlim, ylim)
    setup_ct_signal_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=[-1, 1, 3],
        yticks=[1, 2],
    )

    plot_signal(ax, np.array([-1.0, 1.0, 3.0]), np.array([0.0, 2.0, 0.0]))

    label_text(ax, -1.0, -0.26, r"$t=-1$", ha="center", va="top")
    label_text(ax, 1.0, 2.08, r"$(1,2)$", ha="center", va="bottom")
    label_text(ax, 3.0, -0.26, r"$t=3$", ha="center", va="top")

    save_figure(
        fig,
        "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/1.3--signal-size-Images/images/l003-s005-qg-q002-graph-q002.png",
    )
    plt.close(fig)


if __name__ == "__main__":
    render()
