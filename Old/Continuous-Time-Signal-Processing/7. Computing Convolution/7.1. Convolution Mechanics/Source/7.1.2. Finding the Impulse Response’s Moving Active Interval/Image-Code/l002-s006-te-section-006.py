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
        "savefig.facecolor": "white",
    }
)


SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GUIDE_COLOR = "#777777"

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

FIGSIZE = (9.12, 7.68)
DPI = 160
X_LIMITS = (0.45, 9.60)
AXIS_START = 0.60
AXIS_END = 9.05
Y_LIMITS = (-0.95, 0.95)
SUPPORT_BAND = (-0.16, 0.16)


def math_label(value):
    if isinstance(value, str):
        return value
    if abs(value - int(value)) < 1e-9:
        return rf"${int(value)}$"
    return rf"${value:g}$"


def draw_panel(
    ax,
    *,
    support_left,
    support_right,
    endpoint_labels,
    axis_label,
    function_label,
    annotations,
):
    ax.set_xlim(*X_LIMITS)
    ax.set_ylim(*Y_LIMITS)
    ax.set_aspect("auto")

    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    ax.set_xticks([])
    ax.set_yticks([])

    support = np.asarray([support_left, support_right], dtype=float)
    ax.fill_between(
        support,
        SUPPORT_BAND[0],
        SUPPORT_BAND[1],
        color=SIGNAL_COLOR,
        alpha=0.12,
        zorder=1,
    )

    ax.quiver(AXIS_START, 0, AXIS_END - AXIS_START, 0, **AXIS_ARROW_KW)

    ax.plot(
        [support_left, support_right],
        [0, 0],
        color=SIGNAL_COLOR,
        linewidth=SIGNAL_LW,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=3,
    )

    for x in support:
        ax.plot([x, x], [-TICK_HALF_LEN, TICK_HALF_LEN], color=AXIS_COLOR, lw=TICK_LW, zorder=4)
        ax.plot(
            x,
            0,
            marker="o",
            markersize=8,
            markerfacecolor=SIGNAL_COLOR,
            markeredgecolor=SIGNAL_COLOR,
            linestyle="None",
            zorder=5,
        )

    ax.text(
        support_left,
        -0.22,
        endpoint_labels[0],
        fontsize=TICK_LABEL_SIZE,
        ha="center",
        va="top",
        color=TICK_LABEL_COLOR,
        zorder=6,
    )
    ax.text(
        support_right,
        -0.22,
        endpoint_labels[1],
        fontsize=TICK_LABEL_SIZE,
        ha="center",
        va="top",
        color=TICK_LABEL_COLOR,
        zorder=6,
    )

    ax.text(
        (support_left + support_right) / 2,
        0.42,
        function_label,
        fontsize=TOP_LABEL_SIZE,
        ha="center",
        va="bottom",
        color=LABEL_COLOR,
        zorder=6,
    )

    ax.text(
        AXIS_END + 0.16,
        -0.02,
        axis_label,
        fontsize=AXIS_LABEL_SIZE,
        ha="left",
        va="center",
        color=LABEL_COLOR,
        clip_on=False,
        zorder=6,
    )

    for x, y, text, ha in annotations:
        ax.text(
            x,
            y,
            text,
            fontsize=ANNOTATION_SIZE,
            ha=ha,
            va="bottom",
            color=GUIDE_COLOR,
            zorder=6,
        )


def build_figure():
    fig, axes = plt.subplots(2, 1, figsize=FIGSIZE, dpi=DPI, sharex=True)
    fig.patch.set_facecolor("white")

    draw_panel(
        axes[0],
        support_left=2.0,
        support_right=8.0,
        endpoint_labels=(r"$0$", r"$2$"),
        axis_label=r"$u$",
        function_label=r"$h(u)$",
        annotations=[
            (7.55, 0.64, r"$t$ fixed", "left"),
        ],
    )

    draw_panel(
        axes[1],
        support_left=2.0,
        support_right=8.0,
        endpoint_labels=(r"$t-2$", r"$t$"),
        axis_label=r"$\tau$",
        function_label=r"$h(t-\tau)$",
        annotations=[
            (2.0, 0.50, r"$u=2 \mapsto \tau=t-2$", "center"),
            (8.0, 0.50, r"$u=0 \mapsto \tau=t$", "center"),
            (5.0, 0.68, r"$t-\tau$ reverses endpoint order", "center"),
        ],
    )

    fig.subplots_adjust(left=0.06, right=0.97, top=0.95, bottom=0.08, hspace=0.42)
    return fig


def main():
    fig = build_figure()
    output_path = Path(
        "/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/"
        "2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/"
        "7.1--convolution-mechanics-Images/images/l002-s006-te-section-006.png"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
