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


SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
TICK_LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GUIDE_COLOR = "#777777"
ANNOTATION_COLOR = "#555555"

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
DPI = 160

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


def math_label(value):
    if abs(value - int(value)) < 1e-9:
        return rf"${int(value)}$"
    return rf"${value:g}$"


def setup_ct_signal_axes(
    ax,
    *,
    xlim,
    ylim,
    xticks,
    yticks,
    x_axis_label=r"$\tau$",
    y_axis_label=r"$x(\tau)$",
    show_grid=True,
    show_origin=True,
    y_tick_label_side="left",
    equal_aspect=False,
    show_x_tick_labels=True,
    show_y_tick_labels=True,
):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)

    if equal_aspect:
        ax.set_aspect("equal", adjustable="box")

    ax.set_xticks(xticks)
    ax.set_yticks(yticks)

    if show_grid:
        ax.grid(True, linewidth=GRID_LW, alpha=0.18, color=GRID_COLOR)
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
        ax.plot([t, t], [-TICK_HALF_LEN, TICK_HALF_LEN],
                color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if show_x_tick_labels:
            ax.text(t, -0.16, math_label(t),
                    fontsize=TICK_LABEL_SIZE, ha="center", va="top",
                    color=TICK_LABEL_COLOR, zorder=6)

    for y in yticks:
        if abs(y) < 1e-12:
            continue
        ax.plot([-TICK_HALF_LEN, TICK_HALF_LEN], [y, y],
                color=AXIS_COLOR, lw=TICK_LW, zorder=5)
        if show_y_tick_labels:
            if y_tick_label_side == "right":
                ax.text(0.12, y, math_label(y),
                        fontsize=TICK_LABEL_SIZE, ha="left", va="center",
                        color=TICK_LABEL_COLOR, zorder=6)
            else:
                ax.text(-0.12, y, math_label(y),
                        fontsize=TICK_LABEL_SIZE, ha="right", va="center",
                        color=TICK_LABEL_COLOR, zorder=6)

    if show_origin:
        ax.text(0.06, -0.08, r"$0$",
                fontsize=TICK_LABEL_SIZE, ha="left", va="top",
                color=TICK_LABEL_COLOR, zorder=6)

    x_pad = 0.08 * (xlim[1] - xlim[0]) / 6
    y_pad = 0.08 * (ylim[1] - ylim[0]) / 4

    if x_axis_label:
        ax.text(x_axis_end + x_pad, -0.03, x_axis_label,
                fontsize=AXIS_LABEL_SIZE, ha="left", va="center",
                color=LABEL_COLOR, clip_on=False)

    if y_axis_label:
        ax.text(0, y_axis_end + y_pad, y_axis_label,
                fontsize=TOP_LABEL_SIZE, ha="center", va="bottom",
                color=LABEL_COLOR, clip_on=False)


def plot_signal(ax, t, x, *, lw=SIGNAL_LW, color=SIGNAL_COLOR, zorder=4):
    ax.plot(
        t,
        x,
        color=color,
        linewidth=lw,
        solid_capstyle="butt",
        solid_joinstyle="miter",
        zorder=zorder,
    )


def plot_smooth_signal(ax, t, x, *, lw=2.35, color=SIGNAL_COLOR, zorder=4):
    ax.plot(
        t,
        x,
        color=color,
        linewidth=lw,
        solid_capstyle="round",
        zorder=zorder,
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


def shade_region(ax, x_left, x_right, *, alpha=0.08, color=SIGNAL_COLOR, zorder=0):
    ax.axvspan(x_left, x_right, color=color, alpha=alpha, zorder=zorder)


def causal_exponential(t, alpha=1.0, amplitude=1.0, t0=0.0):
    tau = np.asarray(t, dtype=float) - t0
    return amplitude * np.exp(-alpha * tau) * np.where(tau >= 0, 1.0, 0.0)


def make_output_path(filename):
    # Save into the lesson's images directory, not beside the script.
    return Path(__file__).resolve().parent.parent / "images" / filename


def build_panel(ax, t_cutoff):
    xlim = (-4.4, 4.4)
    ylim = (-0.2, 1.45)
    xticks = [-4, -2, 0, 2, 4]
    yticks = [0, 0.5, 1.0]

    setup_ct_signal_axes(
        ax,
        xlim=xlim,
        ylim=ylim,
        xticks=xticks,
        yticks=yticks,
        x_axis_label=r"$\tau$",
        y_axis_label="",
        show_origin=True,
        equal_aspect=False,
        show_x_tick_labels=True,
        show_y_tick_labels=True,
    )

    shade_region(ax, xlim[0], t_cutoff)
    draw_dotted_guide(ax, [t_cutoff, t_cutoff], [ylim[0], ylim[1]])

    tau_x = np.linspace(xlim[0] + 0.05, t_cutoff - 0.02, 500)
    x_tau = 0.98 + 0.12 * np.sin(1.7 * (tau_x + 0.35)) + 0.07 * np.cos(3.2 * (tau_x - 0.2))
    plot_smooth_signal(ax, tau_x, x_tau, lw=2.8)

    sample_tau = np.array([-3.5, -2.4, -1.5, -0.6, 0.4, 1.0])
    sample_x = 0.98 + 0.12 * np.sin(1.7 * (sample_tau + 0.35)) + 0.07 * np.cos(3.2 * (sample_tau - 0.2))
    ax.plot(
        sample_tau,
        sample_x,
        linestyle="None",
        marker="o",
        markersize=4.5,
        markerfacecolor=SIGNAL_COLOR,
        markeredgecolor=SIGNAL_COLOR,
        zorder=6,
    )

    tau_left = np.linspace(xlim[0] + 0.05, t_cutoff, 400)
    h_left = 0.55 * causal_exponential(t_cutoff - tau_left, alpha=0.9, amplitude=1.0, t0=0.0)
    tau_right = np.linspace(t_cutoff + 0.02, xlim[1] - 0.05, 160)
    h_right = np.zeros_like(tau_right)

    tau_trace = np.concatenate([tau_left, [t_cutoff, t_cutoff], tau_right])
    h_trace = np.concatenate([h_left, [h_left[-1], 0.0], h_right])
    plot_signal(ax, tau_trace, h_trace, lw=3.0)

    ax.text(-3.78, 1.28, r"present and past input values",
            fontsize=ANNOTATION_SIZE, ha="left", va="center",
            color=ANNOTATION_COLOR)
    ax.text(1.65, 1.28, r"future input values" "\n" r"excluded by causality",
            fontsize=14, ha="center", va="center",
            color=ANNOTATION_COLOR)

    ax.text(-3.95, 1.06, r"$x(\tau)$",
            fontsize=17, ha="left", va="center",
            color=LABEL_COLOR)
    ax.text(-3.95, 0.56, r"$h(t-\tau)$",
            fontsize=17, ha="left", va="center",
            color=LABEL_COLOR)
    ax.text(1.72, 0.20, r"$0$ for $\tau>t$",
            fontsize=ANNOTATION_SIZE, ha="center", va="center",
            color=ANNOTATION_COLOR)

    ax.text(t_cutoff, -0.16, r"$t$",
            fontsize=TICK_LABEL_SIZE, ha="center", va="top",
            color=TICK_LABEL_COLOR, zorder=7)


def main():
    output_path = make_output_path("l006-s001-te-section-001.png")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(9.12, 5.2), dpi=DPI)

    t_cutoff = 1.25

    build_panel(ax, t_cutoff)

    fig.tight_layout(pad=1.0)
    fig.savefig(output_path, bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    main()
