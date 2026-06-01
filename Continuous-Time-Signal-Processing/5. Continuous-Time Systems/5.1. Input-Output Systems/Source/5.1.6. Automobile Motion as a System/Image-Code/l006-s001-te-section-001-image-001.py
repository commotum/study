"""Section image for Automobile Motion as a System.

Minimal one-dimensional car-motion schematic with an input-output signal chain.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


plt.rcParams.update({
    "mathtext.fontset": "cm",
    "font.family": "serif",
})


CANONICAL_DPI = 300
PX_PER_DATA_UNIT = 150
INCHES_PER_DATA_UNIT = PX_PER_DATA_UNIT / CANONICAL_DPI

MARGIN_LEFT_PX = 115
MARGIN_RIGHT_PX = 120
MARGIN_BOTTOM_PX = 95
MARGIN_TOP_PX = 110


def px_to_pt(px):
    return px * 72 / CANONICAL_DPI


def px_to_data(px):
    return px / PX_PER_DATA_UNIT


# Colors and geometry.
SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
SIGNAL_LW = px_to_pt(7.1)
SIGNAL_LW_THIN = px_to_pt(4.8)



def make_canvas(xlim, ylim):
    x_range = xlim[1] - xlim[0]
    y_range = ylim[1] - ylim[0]
    fig_w_px = MARGIN_LEFT_PX + x_range * PX_PER_DATA_UNIT + MARGIN_RIGHT_PX
    fig_h_px = MARGIN_BOTTOM_PX + y_range * PX_PER_DATA_UNIT + MARGIN_TOP_PX
    fig, ax = plt.subplots(
        figsize=(fig_w_px / CANONICAL_DPI, fig_h_px / CANONICAL_DPI),
        dpi=CANONICAL_DPI,
        facecolor="white",
        constrained_layout=True,
    )
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("auto")
    ax.axis("off")
    return fig, ax


def draw_car(ax, x_center=9.35, y_base=1.55, length=2.0, height=0.55):
    body_y0 = y_base
    body_y1 = y_base + 0.45
    body = Rectangle(
        (x_center - length / 2, body_y0),
        length,
        height,
        facecolor="white",
        edgecolor=AXIS_COLOR,
        lw=px_to_pt(3.8),
    )
    ax.add_patch(body)

    rear_wheel_x = x_center - length * 0.42
    front_wheel_x = x_center + length * 0.30
    wheel_r = 0.15
    for cx in (rear_wheel_x, front_wheel_x):
        ax.add_patch(plt.Circle((cx, body_y0), wheel_r, ec=AXIS_COLOR, fc="white", lw=px_to_pt(3.8)))

    # Cabin and rear marker.
    ax.plot(
        [x_center - length * 0.32, x_center - length * 0.12],
        [body_y1, body_y1 + 0.22],
        color=AXIS_COLOR,
        lw=px_to_pt(3.8),
    )
    ax.plot(
        [x_center - length * 0.12, x_center + length * 0.12],
        [body_y1 + 0.22, body_y1 + 0.22],
        color=AXIS_COLOR,
        lw=px_to_pt(3.8),
    )
    ax.plot(
        [x_center + length * 0.12, x_center + length * 0.45],
        [body_y1 + 0.22, body_y1],
        color=AXIS_COLOR,
        lw=px_to_pt(3.8),
    )


def draw_road(ax, x0=0.5, x1=12.8, y=1.55):
    ax.plot([x0, x1], [y, y], color=AXIS_COLOR, lw=px_to_pt(4.0))
    dash_y = y - 0.1
    for cx in np.linspace(x0 + 0.3, x1 - 0.3, 14):
        ax.plot([cx, cx + 0.16], [dash_y, dash_y], color=AXIS_COLOR, lw=px_to_pt(2.2))


def draw_integrator(ax, x0, y0, w=1.2, h=1.0):
    block = Rectangle(
        (x0, y0),
        w,
        h,
        facecolor="white",
        edgecolor=AXIS_COLOR,
        lw=px_to_pt(3.5),
    )
    ax.add_patch(block)
    ax.text(
        x0 + w / 2,
        y0 + h * 0.55,
        r"$\int$",
        fontsize=px_to_pt(40.0),
        color=AXIS_COLOR,
        ha="center",
        va="center",
    )


def draw_signal_arrow(ax, x0, y0, x1, y1, label=None, label_dy=0.0):
    ax.annotate(
        "",
        xy=(x1, y1),
        xytext=(x0, y0),
        arrowprops={
            "arrowstyle": "->",
            "color": SIGNAL_COLOR,
            "lw": SIGNAL_LW_THIN,
            "shrinkA": 0,
            "shrinkB": 0,
            "mutation_scale": 11,
        },
        clip_on=False,
    )
    if label is not None:
        ax.text(
            (x0 + x1) / 2,
            max(y0, y1) + label_dy,
            label,
            fontsize=px_to_pt(34.0),
            color=SIGNAL_COLOR,
            ha="center",
            va="bottom",
        )


def draw_output_drop(ax, x_top, y_top, x_bottom, y_bottom):
    ax.annotate(
        "",
        xy=(x_bottom, y_bottom),
        xytext=(x_top, y_top),
        arrowprops={
            "arrowstyle": "->",
            "color": SIGNAL_COLOR,
            "lw": SIGNAL_LW_THIN,
            "shrinkA": 0,
            "shrinkB": 0,
            "mutation_scale": 11,
        },
        clip_on=False,
    )


def save_figure(fig, path):
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=CANONICAL_DPI, facecolor="white", bbox_inches="tight")
    return output


def main():
    fig, ax = make_canvas((0.0, 13.0), (0.65, 4.6))

    road_y = 1.55
    draw_road(ax, x0=0.4, x1=12.6, y=road_y)
    draw_car(ax, x_center=9.35, y_base=1.55)

    ax.text(
        9.35,
        2.95,
        r"$x(t)$",
        fontsize=px_to_pt(39.2),
        color=SIGNAL_COLOR,
        ha="left",
        va="center",
    )

    # Integration chain: a(t) -> [∫] -> v(t) -> [∫] -> x(t)
    y_sig = 3.35

    # First input source and first integrator.
    draw_signal_arrow(ax, 0.8, y_sig, 3.2, y_sig, label=r"$a(t)$", label_dy=0.17)
    draw_integrator(ax, 3.2, y_sig - 0.5, w=1.35, h=1.0)

    # First output.
    draw_signal_arrow(
        ax,
        4.55,
        y_sig,
        5.78,
        y_sig,
        label=r"$v(t)$",
        label_dy=0.17,
    )

    # Second integrator and final output.
    draw_integrator(ax, 5.78, y_sig - 0.5, w=1.35, h=1.0)
    draw_signal_arrow(
        ax,
        7.13,
        y_sig,
        8.72,
        y_sig,
        label=r"$x(t)$",
        label_dy=0.17,
    )

    # Map final output signal to physical car output.
    draw_output_drop(ax, 8.72, y_sig - 0.04, 9.48, road_y + 0.10)

    # Axis labels to anchor meaning of chain.
    ax.text(0.6, 3.82, r"Input", fontsize=px_to_pt(29.0), color=AXIS_COLOR)
    ax.text(11.0, 3.82, r"Output", fontsize=px_to_pt(29.0), color=AXIS_COLOR)

    save_figure(fig, Path("/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/5.1--input-output-systems-Images/images/l006-s001-te-section-001-image-001.png"))


if __name__ == "__main__":
    main()
