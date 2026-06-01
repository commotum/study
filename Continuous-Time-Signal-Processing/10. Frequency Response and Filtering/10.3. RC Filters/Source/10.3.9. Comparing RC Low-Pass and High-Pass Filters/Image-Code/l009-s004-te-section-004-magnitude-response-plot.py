from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150
BACKGROUND_COLOR = "white"

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"

plt.rcParams.update(
    {
        "mathtext.fontset": "cm",
        "font.family": "serif",
        "figure.facecolor": BACKGROUND_COLOR,
        "axes.facecolor": BACKGROUND_COLOR,
        "savefig.facecolor": BACKGROUND_COLOR,
        "text.color": LABEL_COLOR,
        "axes.labelcolor": LABEL_COLOR,
        "xtick.color": TICK_LABEL_COLOR,
        "ytick.color": TICK_LABEL_COLOR,
    }
)


def px_to_pt(px):
    return px * 72 / CANONICAL_DPI


def px_to_data(px):
    return px / PX_PER_DATA_UNIT


MARGIN_LEFT_PX = 115
MARGIN_RIGHT_PX = 120
MARGIN_BOTTOM_PX = 95
MARGIN_TOP_PX = 110

SIGNAL_LW = px_to_pt(7.1)
SMOOTH_SIGNAL_LW = px_to_pt(5.2)
AXIS_LW = px_to_pt(4.3)
TICK_LW = px_to_pt(2.7)
GRID_LW = px_to_pt(1.3)
GUIDE_LW = px_to_pt(3.3)
ANNOTATION_LW = px_to_pt(2.9)

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

OUTPUT_PATH = Path(
    "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/10.3--rc-filters-Images/images/l009-s004-te-section-004-magnitude-response-plot.png"
)

MODE = "lowpass"
SHOW_CURVE_LABELS = True
SHOW_FREQUENCY_END_LABELS = False
SHOW_ENDPOINT_NUMBERS = True


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
    if abs(value - round(value)) < 1e-9:
        return rf"${int(round(value))}$"
    return rf"${value:g}$"


def setup_axes(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xticks([1, 2, 3, 4])
    ax.set_yticks([0.5, 1.0])
    ax.xaxis.set_minor_locator(MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(MultipleLocator(0.25))
    ax.grid(True, which="both", linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    x0, x1 = xlim
    y0, y1 = ylim
    ax.quiver(x0, 0, x1 - x0, 0, **AXIS_ARROW_KW)
    ax.quiver(0, y0, 0, y1 - y0, **AXIS_ARROW_KW)

    for t in [1, 2, 3, 4]:
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(t, X_TICK_LABEL_Y, math_label(t), fontsize=TICK_LABEL_SIZE, ha="center", va="top", color=TICK_LABEL_COLOR)
    for y in [0.5, 1.0]:
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y], color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        ax.text(-Y_TICK_LABEL_X, y, math_label(y), fontsize=TICK_LABEL_SIZE, ha="right", va="center", color=TICK_LABEL_COLOR)

    ax.text(ORIGIN_LABEL_X, ORIGIN_LABEL_Y, r"$0$", fontsize=TICK_LABEL_SIZE, ha="left", va="top", color=TICK_LABEL_COLOR)
    ax.text(x1 + X_AXIS_LABEL_X_PAD, X_AXIS_LABEL_Y, r"$\omega/\omega_c$", fontsize=AXIS_LABEL_SIZE, ha="left", va="center", color=LABEL_COLOR, clip_on=False)
    ax.text(0, y1 + Y_AXIS_LABEL_Y_PAD, r"$|H(j\omega)|$", fontsize=TOP_LABEL_SIZE, ha="center", va="bottom", color=LABEL_COLOR, clip_on=False)


def draw_dotted_guide(ax, x_values, y_values):
    ax.plot(x_values, y_values, color=GUIDE_COLOR, linewidth=GUIDE_LW, linestyle=(0, (1.1, 2.4)), zorder=3)


def draw_label(ax, x, y, text, *, size=ANNOTATION_SIZE, ha="center", va="center", color=LABEL_COLOR):
    ax.text(x, y, text, fontsize=size, ha=ha, va=va, color=color)


def lowpass_mag(u):
    return 1.0 / np.sqrt(1.0 + u * u)


def highpass_mag(u):
    return u / np.sqrt(1.0 + u * u)


def plot_curve(ax, kind, *, lw=SMOOTH_SIGNAL_LW):
    u = np.linspace(0.0, 4.2, 600)
    y = lowpass_mag(u) if kind == "lowpass" else highpass_mag(u)
    ax.plot(u, y, color=SIGNAL_COLOR, linewidth=lw, solid_capstyle="round", zorder=4)
    return u, y


def draw_cutoff_marker(ax, x=1.0):
    draw_dotted_guide(ax, [x, x], [0.0, 1.02])
    draw_label(ax, x, 1.06, r"$\omega_c$", size=ANNOTATION_SIZE, ha="center", va="bottom", color=ANNOTATION_COLOR)


def draw_end_text(ax, left_text, right_text):
    draw_label(ax, 0.14, 0.06, left_text, size=ANNOTATION_SIZE, ha="left", va="bottom", color=ANNOTATION_COLOR)
    draw_label(ax, 3.10, 0.06, right_text, size=ANNOTATION_SIZE, ha="left", va="bottom", color=ANNOTATION_COLOR)


def draw_curve_label(ax, kind):
    if kind == "lowpass":
        draw_label(ax, 0.78, 0.88, "low-pass", size=ANNOTATION_SIZE, ha="left", va="center", color=ANNOTATION_COLOR)
    else:
        draw_label(ax, 2.12, 0.88, "high-pass", size=ANNOTATION_SIZE, ha="left", va="center", color=ANNOTATION_COLOR)


def build_comparison(ax):
    plot_curve(ax, "lowpass")
    plot_curve(ax, "highpass", lw=SMOOTH_SIGNAL_LW)
    draw_cutoff_marker(ax)
    if SHOW_CURVE_LABELS:
        draw_curve_label(ax, "lowpass")
        draw_curve_label(ax, "highpass")
    if SHOW_FREQUENCY_END_LABELS:
        draw_end_text(ax, "low frequency", "high frequency")


def build_single(ax, kind):
    plot_curve(ax, kind)
    draw_cutoff_marker(ax)
    if SHOW_ENDPOINT_NUMBERS:
        if kind == "lowpass":
            draw_label(ax, 0.14, 1.03, r"$1$", size=ANNOTATION_SIZE, ha="left", va="bottom", color=ANNOTATION_COLOR)
            draw_label(ax, 3.95, 0.04, r"$0$", size=ANNOTATION_SIZE, ha="left", va="bottom", color=ANNOTATION_COLOR)
        else:
            draw_label(ax, 0.14, 0.04, r"$0$", size=ANNOTATION_SIZE, ha="left", va="bottom", color=ANNOTATION_COLOR)
            draw_label(ax, 3.95, 1.03, r"$1$", size=ANNOTATION_SIZE, ha="left", va="bottom", color=ANNOTATION_COLOR)
    if SHOW_CURVE_LABELS:
        draw_label(ax, 1.75, 0.74 if kind == "lowpass" else 0.88, "low-pass" if kind == "lowpass" else "high-pass", size=ANNOTATION_SIZE, ha="left", va="center", color=ANNOTATION_COLOR)


def render():
    xlim = (0.0, 4.2)
    ylim = (-0.15, 1.15)
    fig, ax = make_figure(xlim, ylim)
    setup_axes(ax, xlim, ylim)
    if MODE == "comparison":
        build_comparison(ax)
    else:
        build_single(ax, MODE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH, dpi=CANONICAL_DPI, bbox_inches="tight", facecolor=BACKGROUND_COLOR)
    plt.close(fig)


if __name__ == "__main__":
    render()
