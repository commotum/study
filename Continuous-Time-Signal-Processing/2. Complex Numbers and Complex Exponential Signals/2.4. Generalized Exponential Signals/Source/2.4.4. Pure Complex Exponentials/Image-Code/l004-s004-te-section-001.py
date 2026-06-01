"""Render the rotating-phasor diagram for pure complex exponentials."""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


# ---------------------------------------------------------------------------
# Canonical style constants
# ---------------------------------------------------------------------------

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


def px_to_pt(px):
    return px * 72 / CANONICAL_DPI


def px_to_data(px):
    return px / PX_PER_DATA_UNIT


SIGNAL_LW = px_to_pt(7.1)
AXIS_LW = px_to_pt(4.3)
TICK_LW = px_to_pt(2.7)
GUIDE_LW = px_to_pt(3.3)

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
PHASOR_ARROW_WIDTH_DATA = px_to_data(4.7)

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

PHASOR_ARROW_KW = dict(
    angles="xy",
    scale_units="xy",
    scale=1,
    units="xy",
    width=PHASOR_ARROW_WIDTH_DATA,
    headwidth=4.6,
    headlength=6.1,
    headaxislength=5.0,
    color=SIGNAL_COLOR,
    pivot="tail",
    clip_on=False,
)

IMAGE_OUTPUT_PATH = Path(
    "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/2.4--generalized-exponential-signals-Images/images/l004-s004-te-section-001.png"
)


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def configure_matplotlib():
    mpl.rcParams.update(
        {
            "mathtext.fontset": "cm",
            "font.family": "serif",
            "figure.facecolor": BACKGROUND_COLOR,
            "axes.facecolor": BACKGROUND_COLOR,
            "savefig.facecolor": BACKGROUND_COLOR,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.spines.left": False,
            "axes.spines.bottom": False,
        }
    )


def math_label(value):
    if isinstance(value, str):
        return value
    numeric = float(value)
    rounded = int(round(numeric))
    if abs(numeric - rounded) < 1e-9:
        return rf"${rounded}$"
    return rf"${numeric:g}$"


def make_figure(xlim, ylim, *, dpi=CANONICAL_DPI):
    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]
    fig_w_px = MARGIN_LEFT_PX + x_range * PX_PER_DATA_UNIT + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_BOTTOM_PX + y_range * PX_PER_DATA_UNIT + MARGIN_TOP_PX
    fig, ax = plt.subplots(
        figsize=(fig_w_px / dpi, fig_h_px / dpi),
        dpi=dpi,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=True,
    )
    return fig, ax


def save_figure(fig, output_path, *, dpi=CANONICAL_DPI):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        output_path,
        dpi=dpi,
        bbox_inches="tight",
        facecolor=BACKGROUND_COLOR,
    )


def setup_complex_plane_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_axis_label=r"$\Re\{z\}$",
    y_axis_label=r"$\Im\{z\}$",
):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)

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
        if abs(float(y)) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
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


def draw_unit_circle(ax, *, radius=1.0, color=GUIDE_COLOR, alpha=0.75):
    theta = np.linspace(0, 2 * np.pi, 600)
    ax.plot(
        radius * np.cos(theta),
        radius * np.sin(theta),
        color=color,
        linewidth=px_to_pt(2.1),
        alpha=alpha,
        solid_capstyle="round",
        zorder=2,
    )


def draw_phasor(ax, theta, *, alpha=1.0, zorder=5):
    x = np.cos(theta)
    y = np.sin(theta)
    ax.quiver(0, 0, x, y, alpha=alpha, zorder=zorder, **PHASOR_ARROW_KW)
    return x, y


def draw_angle_arc(ax, theta_end, *, radius=0.34, color=GUIDE_COLOR):
    theta = np.linspace(0.06, theta_end - 0.06, 200)
    arc_x = radius * np.cos(theta)
    arc_y = radius * np.sin(theta)
    ax.plot(
        arc_x,
        arc_y,
        color=color,
        linewidth=GUIDE_LW,
        solid_capstyle="round",
        zorder=3,
    )
    ax.annotate(
        "",
        xy=(arc_x[-1], arc_y[-1]),
        xytext=(arc_x[-7], arc_y[-7]),
        arrowprops=dict(
            arrowstyle="-|>",
            color=color,
            lw=px_to_pt(1.2),
            mutation_scale=8,
            shrinkA=0,
            shrinkB=0,
        ),
        zorder=4,
    )

    mid_theta = 0.46 * theta_end
    label_r = radius + px_to_data(12)
    ax.text(
        label_r * np.cos(mid_theta),
        label_r * np.sin(mid_theta),
        r"$\omega t$",
        fontsize=ANNOTATION_SIZE,
        ha="center",
        va="center",
        color=ANNOTATION_COLOR,
        zorder=6,
    )


def build_figure():
    xlim = (-1.58, 1.82)
    ylim = (-1.48, 1.52)
    fig, ax = make_figure(xlim, ylim)

    setup_complex_plane_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=[-1, 1],
        yticks=[-1, 1],
    )

    draw_unit_circle(ax)

    theta_previous = np.deg2rad(24)
    theta_current = np.deg2rad(60)

    # Earlier phasor position, faint enough to read as a trail.
    draw_phasor(ax, theta_previous, alpha=0.26, zorder=3)

    # Current phasor position on the unit circle.
    draw_phasor(ax, theta_current, alpha=1.0, zorder=5)

    # Angle marker from the positive real axis to the current phasor.
    draw_angle_arc(ax, theta_current, radius=0.36, color=GUIDE_COLOR)

    save_figure(fig, IMAGE_OUTPUT_PATH)
    plt.close(fig)


def main():
    configure_matplotlib()
    build_figure()


if __name__ == "__main__":
    main()
