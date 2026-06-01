from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator


BACKGROUND_COLOR = "white"


def configure_matplotlib() -> None:
    plt.rcParams.update(
        {
            "mathtext.fontset": "cm",
            "font.family": "serif",
            "figure.facecolor": BACKGROUND_COLOR,
            "axes.facecolor": BACKGROUND_COLOR,
            "savefig.facecolor": BACKGROUND_COLOR,
            "savefig.edgecolor": BACKGROUND_COLOR,
        }
    )


configure_matplotlib()

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

GRID_ALPHA = 0.18
GUIDE_DASH_STYLE = (0, (1.1, 2.4))

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
X_TICK_LABEL_Y = -24 / PX_PER_DATA_UNIT
Y_TICK_LABEL_X = 18 / PX_PER_DATA_UNIT
ORIGIN_LABEL_X = 9 / PX_PER_DATA_UNIT
ORIGIN_LABEL_Y = -12 / PX_PER_DATA_UNIT
X_AXIS_LABEL_X_PAD = 15 / PX_PER_DATA_UNIT
X_AXIS_LABEL_Y = -4.5 / PX_PER_DATA_UNIT
Y_AXIS_LABEL_Y_PAD = 18 / PX_PER_DATA_UNIT

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
    zorder=2,
)


def px_to_data(px: float) -> float:
    return px / PX_PER_DATA_UNIT


def make_frequency_response_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
    x_range = float(xlim[1]) - float(xlim[0])
    y_range = float(ylim[1]) - float(ylim[0])
    fig_w_px = MARGIN_LEFT_PX + x_range * PX_PER_DATA_UNIT + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_BOTTOM_PX + y_range * PX_PER_DATA_UNIT + MARGIN_TOP_PX
    fig, ax = plt.subplots(
        figsize=(fig_w_px / dpi, fig_h_px / dpi),
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=True,
    )
    return fig, ax


def math_label(value):
    if isinstance(value, str):
        return value
    numeric = float(value)
    rounded = round(numeric)
    if np.isclose(numeric, rounded):
        return rf"${int(rounded)}$"
    return rf"${numeric:g}$"


def setup_frequency_response_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_axis_label=r"$\omega$",
    y_axis_label=r"$|H(j\omega)|$",
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
        ax.grid(True, which="both", linewidth=GRID_LW, alpha=GRID_ALPHA, color=GRID_COLOR)
        ax.set_axisbelow(True)

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    x_axis_start, x_axis_end = xlim
    y_axis_start, y_axis_end = ylim

    ax.quiver(x_axis_start, 0, x_axis_end - x_axis_start, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y_axis_start, 0, y_axis_end - y_axis_start, **AXIS_ARROW_KW)

    for t in xticks:
        if abs(float(t)) < 1e-12:
            continue
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(t, X_TICK_LABEL_Y, math_label(t),
                fontsize=TICK_LABEL_SIZE, ha="center", va="top",
                color=TICK_LABEL_COLOR, zorder=6)

    for y in yticks:
        if abs(float(y)) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if y_tick_label_side == "right":
            ax.text(Y_TICK_LABEL_X, y, math_label(y),
                    fontsize=TICK_LABEL_SIZE, ha="left", va="center",
                    color=TICK_LABEL_COLOR, zorder=6)
        else:
            ax.text(-Y_TICK_LABEL_X, y, math_label(y),
                    fontsize=TICK_LABEL_SIZE, ha="right", va="center",
                    color=TICK_LABEL_COLOR, zorder=6)

    if show_origin:
        ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$",
                fontsize=TICK_LABEL_SIZE, ha="left", va="top",
                color=TICK_LABEL_COLOR, zorder=6)

    ax.text(x_axis_end + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, x_axis_label,
            fontsize=AXIS_LABEL_SIZE, ha="left", va="center",
            color=LABEL_COLOR, clip_on=False)
    ax.text(0, y_axis_end + Y_AXIS_LABEL_Y_PAD, y_axis_label,
            fontsize=TOP_LABEL_SIZE, ha="center", va="bottom",
            color=LABEL_COLOR, clip_on=False)


def draw_dotted_guide(ax, x_values, y_values):
    ax.plot(
        x_values,
        y_values,
        color=GUIDE_COLOR,
        linewidth=GUIDE_LW,
        linestyle=GUIDE_DASH_STYLE,
        zorder=3,
    )


def draw_unity_reference_line(ax, *, xlim=None, y=1.0):
    if xlim is None:
        xlim = ax.get_xlim()
    ax.plot(
        [xlim[0], xlim[1]],
        [y, y],
        color=ANNOTATION_COLOR,
        linewidth=ANNOTATION_LW,
        linestyle="-",
        zorder=3,
    )


def mark_sample_point(ax, x, y):
    ax.plot(
        x,
        y,
        marker="o",
        markersize=18.0 * 72 / CANONICAL_DPI,
        markerfacecolor=SIGNAL_COLOR,
        markeredgecolor=SIGNAL_COLOR,
        linestyle="None",
        zorder=6,
    )


def save_figure(fig, output_path, *, dpi=CANONICAL_DPI, close=True):
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        path,
        dpi=dpi,
        bbox_inches="tight",
        facecolor=BACKGROUND_COLOR,
        edgecolor=BACKGROUND_COLOR,
    )
    if close:
        plt.close(fig)
    return path


def build_curve():
    omega = np.linspace(0.0, 9.0, 900)
    anchors_x = np.array([0.0, 1.1, 2.0, 2.9, 3.7, 4.5, 5.2, 6.1, 7.0, 8.0, 9.0])
    anchors_y = np.array([1.60, 1.58, 1.38, 1.16, 1.05, 1.00, 0.98, 0.90, 0.76, 0.52, 0.35])
    return omega, np.interp(omega, anchors_x, anchors_y)


def main():
    xlim = (0.0, 9.0)
    ylim = (-0.22, 2.08)

    fig, ax = make_frequency_response_figure(xlim, ylim)
    setup_frequency_response_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=[2, 4, 6, 8],
        yticks=[0.5, 1.0, 1.5, 2.0],
    )

    omega, magnitude = build_curve()
    ax.plot(
        omega,
        magnitude,
        color=SIGNAL_COLOR,
        linewidth=SIGNAL_LW,
        solid_capstyle="round",
        solid_joinstyle="round",
        zorder=4,
    )

    draw_unity_reference_line(ax, xlim=xlim, y=1.0)

    sample_omegas = [1.0, 4.5, 8.0]
    for omega_sample in sample_omegas:
        magnitude_sample = np.interp(omega_sample, omega, magnitude)
        draw_dotted_guide(ax, [omega_sample, omega_sample], [0.0, magnitude_sample])
        mark_sample_point(ax, omega_sample, magnitude_sample)

    save_figure(
        fig,
        "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/10.2--interpreting-frequency-response-Images/images/l001-s005-te-section-005.png",
    )


if __name__ == "__main__":
    main()
