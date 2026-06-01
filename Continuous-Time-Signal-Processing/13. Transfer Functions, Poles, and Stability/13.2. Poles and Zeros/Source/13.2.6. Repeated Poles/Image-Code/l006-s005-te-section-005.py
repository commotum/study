from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


BACKGROUND_COLOR = "white"
SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150
MARGIN_LEFT_PX = 115
MARGIN_RIGHT_PX = 120
MARGIN_BOTTOM_PX = 95
MARGIN_TOP_PX = 110

TICK_LW = 2.7 * 72 / CANONICAL_DPI
TICK_LABEL_SIZE = 35.6 * 72 / CANONICAL_DPI
AXIS_LABEL_SIZE = 53.3 * 72 / CANONICAL_DPI
TOP_LABEL_SIZE = 57.8 * 72 / CANONICAL_DPI
ANNOTATION_SIZE = 33.3 * 72 / CANONICAL_DPI
POLE_MARKER_SIZE = 21.0 * 72 / CANONICAL_DPI
POLE_MARKER_EDGEWIDTH = 5.1 * 72 / CANONICAL_DPI
DOUBLE_POLE_MARKER_SIZE = 13.5 * 72 / CANONICAL_DPI
DOUBLE_POLE_MARKER_EDGEWIDTH = 3.2 * 72 / CANONICAL_DPI
GRID_LW = 1.3 * 72 / CANONICAL_DPI
TICK_HALF_LEN = 8.25 / PX_PER_DATA_UNIT
X_TICK_LABEL_Y = -24 / PX_PER_DATA_UNIT
Y_TICK_LABEL_X = 18 / PX_PER_DATA_UNIT
ORIGIN_LABEL_X = 9 / PX_PER_DATA_UNIT
ORIGIN_LABEL_Y = -12 / PX_PER_DATA_UNIT
X_AXIS_LABEL_X_PAD = 15 / PX_PER_DATA_UNIT
X_AXIS_LABEL_Y = -4.5 / PX_PER_DATA_UNIT
Y_AXIS_LABEL_Y_PAD = 18 / PX_PER_DATA_UNIT
POINT_LABEL_OFFSET = (8 / PX_PER_DATA_UNIT, 8 / PX_PER_DATA_UNIT)
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


def make_figure(xlim, ylim):
    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]
    axes_w_px = x_range * PX_PER_DATA_UNIT
    axes_h_px = y_range * PX_PER_DATA_UNIT
    fig_w_px = MARGIN_LEFT_PX + axes_w_px + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_BOTTOM_PX + axes_h_px + MARGIN_TOP_PX
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


def setup_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_axis_label=r"$\Re(s)$",
    y_axis_label=r"$\Im(s)$",
    show_grid=False,
):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    if show_grid:
        ax.grid(True, which="both", linewidth=GRID_LW, alpha=0.18, color="#000000")
        ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    x_axis_start, x_axis_end = xlim
    y_axis_start, y_axis_end = ylim
    ax.quiver(x_axis_start, 0, x_axis_end - x_axis_start, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y_axis_start, 0, y_axis_end - y_axis_start, **AXIS_ARROW_KW)

    for t in xticks:
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if abs(float(t)) >= 1e-12:
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
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if abs(float(y)) >= 1e-12:
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


def draw_pole(ax, x, y, *, size=POLE_MARKER_SIZE, edgewidth=POLE_MARKER_EDGEWIDTH, zorder=6):
    ax.plot(
        x,
        y,
        marker="x",
        markersize=size,
        markeredgewidth=edgewidth,
        color=SIGNAL_COLOR,
        linestyle="None",
        zorder=zorder,
    )


def draw_repeated_pole(ax, x, y, *, label=r"$m=2$", dx=0.14, dy=0.16):
    draw_pole(ax, x, y, size=POLE_MARKER_SIZE, edgewidth=POLE_MARKER_EDGEWIDTH)
    draw_pole(ax, x, y, size=DOUBLE_POLE_MARKER_SIZE, edgewidth=DOUBLE_POLE_MARKER_EDGEWIDTH, zorder=7)
    ax.text(
        x + dx,
        y + dy,
        label,
        fontsize=ANNOTATION_SIZE,
        ha="left",
        va="bottom",
        color=LABEL_COLOR,
        zorder=8,
    )


def save_figure(fig, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=CANONICAL_DPI, bbox_inches="tight", facecolor=BACKGROUND_COLOR)
    plt.close(fig)


def main():
    xlim = (-3.6, 1.4)
    ylim = (-2.8, 2.8)
    fig, ax = make_figure(xlim, ylim)
    setup_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=[-3, -2, -1, 0, 1],
        yticks=[-2, -1, 1, 2],
        x_axis_label=r"$\Re(s)$",
        y_axis_label=r"$\Im(s)$",
        show_grid=False,
    )

    draw_repeated_pole(ax, -1.0, 2.0, label=r"$m=2$", dx=0.14, dy=0.18)
    draw_repeated_pole(ax, -1.0, -2.0, label=r"$m=2$", dx=0.14, dy=-0.34)

    save_figure(
        fig,
        Path(
            "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/13.2--poles-and-zeros-Images/images/l006-s005-te-section-005.png"
        ),
    )


if __name__ == "__main__":
    main()
