from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np


plt.rcParams.update(
    {
        "mathtext.fontset": "cm",
        "font.family": "serif",
        "figure.facecolor": "white",
        "axes.facecolor": "white",
    }
)

CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"

SIGNAL_LW = 7.1 * 72.0 / CANONICAL_DPI
AXIS_LW = 4.3 * 72.0 / CANONICAL_DPI
TICK_LW = 2.7 * 72.0 / CANONICAL_DPI
GRID_LW = 1.3 * 72.0 / CANONICAL_DPI
GUIDE_LW = 3.3 * 72.0 / CANONICAL_DPI

TICK_LABEL_SIZE = 35.6 * 72.0 / CANONICAL_DPI
AXIS_LABEL_SIZE = 53.3 * 72.0 / CANONICAL_DPI
TOP_LABEL_SIZE = 57.8 * 72.0 / CANONICAL_DPI
ANNOTATION_SIZE = 30.0 * 72.0 / CANONICAL_DPI

TICK_HALF_LEN = 8.25 / PX_PER_DATA_UNIT
X_TICK_LABEL_Y = -24 / PX_PER_DATA_UNIT
Y_TICK_LABEL_X = 18 / PX_PER_DATA_UNIT
ORIGIN_LABEL_X = 9 / PX_PER_DATA_UNIT
ORIGIN_LABEL_Y = -12 / PX_PER_DATA_UNIT
X_AXIS_LABEL_X_PAD = 15 / PX_PER_DATA_UNIT
X_AXIS_LABEL_Y = -4.5 / PX_PER_DATA_UNIT
Y_AXIS_LABEL_Y_PAD = 18 / PX_PER_DATA_UNIT

OPEN_MARKER_SIZE = 20.0 * 72.0 / CANONICAL_DPI
CLOSED_MARKER_SIZE = 17.8 * 72.0 / CANONICAL_DPI
ENDPOINT_EDGEWIDTH = 5.1 * 72.0 / CANONICAL_DPI

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

OUTPUT_PATH = Path(
    "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/12.2--derivative-properties-Images/images/l006-s001-te-section-001.png"
)


def math_label(value):
    if isinstance(value, str):
        return value
    if abs(value - int(value)) < 1e-9:
        return rf"${int(value)}$"
    return rf"${value:g}$"


def make_figure():
    fig, axes = plt.subplots(
        2,
        3,
        figsize=(12.8, 6.2),
        dpi=CANONICAL_DPI,
        facecolor="white",
        constrained_layout=True,
    )
    return fig, axes


def setup_axis(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_axis_label=None,
    y_axis_label=None,
    show_xtick_labels=True,
    show_ytick_labels=True,
    title=None,
):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.xaxis.set_minor_locator(mticker.MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(0.5))
    ax.grid(True, which="both", linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
    ax.set_axisbelow(True)

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    x0, x1 = xlim
    y0, y1 = ylim
    ax.quiver(x0, 0, x1 - x0, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y0, 0, y1 - y0, **AXIS_ARROW_KW)

    for t in xticks:
        if abs(t) < 1e-12:
            continue
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if show_xtick_labels:
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
        if show_ytick_labels:
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

    if title is not None:
        ax.set_title(title, fontsize=ANNOTATION_SIZE, pad=10, color=LABEL_COLOR)


def plot_signal(ax, t, x):
    ax.plot(
        t,
        x,
        color=SIGNAL_COLOR,
        linewidth=SIGNAL_LW,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=4,
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


def draw_impulse(ax, t0, y0, y1, label, label_dx=0.0, label_dy=0.0):
    ax.annotate(
        "",
        xy=(t0, y1),
        xytext=(t0, y0),
        arrowprops=dict(
            arrowstyle="-|>",
            color=SIGNAL_COLOR,
            lw=2.2,
            shrinkA=0.0,
            shrinkB=0.0,
            mutation_scale=14,
        ),
        zorder=6,
    )
    ax.text(
        t0 + label_dx,
        label_dy,
        label,
        fontsize=ANNOTATION_SIZE,
        ha="center",
        va="top",
        color=ANNOTATION_COLOR,
    )


def build_panel_top(ax, title, x_label_mode, signal_kind):
    xlim = (-0.6, 1.85)
    ylim = (-0.2, 1.95)
    setup_axis(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=[0, 1],
        yticks=[1],
        x_axis_label=None,
        y_axis_label=r"$x(t)$",
        show_xtick_labels=False,
        show_ytick_labels=True,
        title=title,
    )

    if signal_kind == "causal":
        t = np.array([-0.6, 0.0, 1.65])
        x = np.array([0.0, 0.0, 1.65])
        plot_signal(ax, t, x)
        draw_closed_endpoint(ax, 0.0, 0.0)
        draw_dotted_guide(ax, [0.0, 0.0], [0.0, 1.75])
        ax.text(
            0.38,
            1.38,
            r"$\mathrm{slope}=+1$",
            fontsize=ANNOTATION_SIZE,
            color=ANNOTATION_COLOR,
            ha="left",
            va="center",
        )
        ax.text(0.03, -0.05, r"$t=0$", fontsize=ANNOTATION_SIZE, color=ANNOTATION_COLOR, ha="left", va="top")
    elif signal_kind == "shifted":
        t = np.array([-0.6, 1.0, 1.65])
        x = np.array([0.0, 0.0, 0.65])
        plot_signal(ax, t, x)
        draw_closed_endpoint(ax, 1.0, 0.0)
        draw_dotted_guide(ax, [1.0, 1.0], [0.0, 1.0])
        ax.text(
            1.02,
            0.9,
            r"$\mathrm{slope}=+1$",
            fontsize=ANNOTATION_SIZE,
            color=ANNOTATION_COLOR,
            ha="left",
            va="center",
        )
        ax.text(1.0, -0.05, r"$t=1$", fontsize=ANNOTATION_SIZE, color=ANNOTATION_COLOR, ha="center", va="top")
    else:
        t = np.array([-0.6, 0.0, 1.0, 1.0, 1.65])
        x = np.array([0.0, 0.0, 1.0, 0.0, 0.0])
        plot_signal(ax, t, x)
        draw_closed_endpoint(ax, 0.0, 0.0)
        draw_open_endpoint(ax, 1.0, 1.0)
        draw_closed_endpoint(ax, 1.0, 0.0)
        draw_dotted_guide(ax, [1.0, 1.0], [0.0, 1.2])
        ax.text(
            0.35,
            0.84,
            r"$\mathrm{slope}=+1$",
            fontsize=ANNOTATION_SIZE,
            color=ANNOTATION_COLOR,
            ha="left",
            va="center",
        )
        ax.text(1.02, 1.06, r"$\mathrm{endpoint}$", fontsize=ANNOTATION_SIZE, color=ANNOTATION_COLOR, ha="left", va="bottom")
        ax.text(1.0, -0.05, r"$t=1$", fontsize=ANNOTATION_SIZE, color=ANNOTATION_COLOR, ha="center", va="top")


def build_panel_bottom(ax, signal_kind):
    xlim = (-0.6, 1.85)
    ylim = (-0.45, 1.45)
    setup_axis(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=[0, 1],
        yticks=[1],
        x_axis_label=r"$t$",
        y_axis_label=r"$x'(t)$",
        show_xtick_labels=True,
        show_ytick_labels=True,
        title=None,
    )

    if signal_kind == "causal":
        t = np.array([-0.6, 0.0, 0.0, 1.65])
        x = np.array([0.0, 0.0, 1.0, 1.0])
        plot_signal(ax, t, x)
        draw_closed_endpoint(ax, 0.0, 1.0)
        draw_dotted_guide(ax, [0.0, 0.0], [0.0, 1.2])
        ax.text(0.47, 1.08, r"$\mathrm{step}$", fontsize=ANNOTATION_SIZE, color=ANNOTATION_COLOR, ha="left", va="center")
    elif signal_kind == "shifted":
        t = np.array([-0.6, 1.0, 1.0, 1.65])
        x = np.array([0.0, 0.0, 1.0, 1.0])
        plot_signal(ax, t, x)
        draw_closed_endpoint(ax, 1.0, 1.0)
        draw_dotted_guide(ax, [1.0, 1.0], [0.0, 1.2])
        ax.text(1.05, 1.08, r"$\mathrm{step}$", fontsize=ANNOTATION_SIZE, color=ANNOTATION_COLOR, ha="left", va="center")
    else:
        t = np.array([-0.6, 0.0, 0.0, 1.0, 1.0, 1.65])
        x = np.array([0.0, 0.0, 1.0, 1.0, 0.0, 0.0])
        plot_signal(ax, t, x)
        draw_closed_endpoint(ax, 0.0, 1.0)
        draw_dotted_guide(ax, [1.0, 1.0], [0.0, 1.2])
        draw_impulse(ax, 1.0, 0.0, -0.32, r"$\mathrm{impulse}$", label_dx=0.02, label_dy=-0.06)
        ax.text(0.28, 1.08, r"$\mathrm{step + impulse}$", fontsize=ANNOTATION_SIZE, color=ANNOTATION_COLOR, ha="left", va="center")


def main():
    fig, axes = make_figure()

    titles = ["causal ramp", "shifted ramp", "finite ramp"]
    kinds = ["causal", "shifted", "finite"]

    for col, (title, kind) in enumerate(zip(titles, kinds)):
        build_panel_top(axes[0, col], title, "top", kind)
        build_panel_bottom(axes[1, col], kind)

    fig.savefig(OUTPUT_PATH, dpi=CANONICAL_DPI, facecolor="white", bbox_inches="tight")


if __name__ == "__main__":
    main()
