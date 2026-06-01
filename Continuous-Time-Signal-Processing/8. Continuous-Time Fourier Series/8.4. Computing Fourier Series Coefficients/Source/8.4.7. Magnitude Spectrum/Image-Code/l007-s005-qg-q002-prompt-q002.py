
"""Render the centered coefficient-magnitude card for q002-prompt."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

BACKGROUND_COLOR = "white"

plt.rcParams.update(
    {
        "mathtext.fontset": "cm",
        "font.family": "serif",
        "figure.facecolor": BACKGROUND_COLOR,
        "axes.facecolor": BACKGROUND_COLOR,
        "savefig.facecolor": BACKGROUND_COLOR,
    }
)

SIGNAL_COLOR = "#2f78b7"
AXIS_COLOR = "#222222"
LABEL_COLOR = "#444444"
GRID_COLOR = "#000000"
GRID_ALPHA = 0.18

CANONICAL_DPI = 300

def px_to_pt(px):
    return px * 72 / CANONICAL_DPI

CARD_BORDER_LW = px_to_pt(4.0)
CARD_SEPARATOR_LW = px_to_pt(2.0)
ROW_LABEL_SIZE = px_to_pt(46.0)
ROW_VALUE_SIZE = px_to_pt(50.0)
CARD_WIDTH = 5.9
CARD_HEIGHT = 3.3

CARD_BOX_LEFT = 0.16
CARD_BOX_RIGHT = 0.84
CARD_BOX_BOTTOM = 0.22
CARD_BOX_TOP = 0.78
CARD_LABEL_X = 0.31
CARD_VALUE_X = 0.70

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

SPEC = {'covered_template': 'coefficient-magnitude-card',
 'kind': 'card',
 'render_notes': ['Centered coefficient-magnitude card with three rows and no stems or axes.',
                  'Blue magnitudes and serif math text match the rest of the topic image set.'],
 'rows': [('DC', '$5$'), ('$k = \\pm 1$', '$0$'), ('$k = \\pm 2$', '$2$')]}
OUTPUT_PATH = Path("/home/jake/Developer/MA/PIPELINE/Electrical-and-Computer-Engineering/2-Build-Lessons/4-Image-Generation/1-Outputs/Continuous-Time-Signal-Processing/8.4--computing-fourier-series-coefficients-Images/images/l007-s005-qg-q002-prompt-q002.png")

def make_card_figure():
    fig, ax = plt.subplots(
        figsize=(CARD_WIDTH, CARD_HEIGHT),
        dpi=CANONICAL_DPI,
        facecolor=BACKGROUND_COLOR,
        constrained_layout=True,
    )
    return fig, ax

def save_figure(fig, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=CANONICAL_DPI, facecolor=BACKGROUND_COLOR, bbox_inches="tight")
    plt.close(fig)
    return output_path

def render_card(ax, rows):
    ax.set_axis_off()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    border_x = [CARD_BOX_LEFT, CARD_BOX_RIGHT, CARD_BOX_RIGHT, CARD_BOX_LEFT, CARD_BOX_LEFT]
    border_y = [CARD_BOX_BOTTOM, CARD_BOX_BOTTOM, CARD_BOX_TOP, CARD_BOX_TOP, CARD_BOX_BOTTOM]
    ax.plot(border_x, border_y, color=AXIS_COLOR, lw=CARD_BORDER_LW, transform=ax.transAxes, clip_on=False)
    row_edges = np.linspace(CARD_BOX_TOP, CARD_BOX_BOTTOM, len(rows) + 1)
    for y in row_edges[1:-1]:
        ax.plot([CARD_BOX_LEFT, CARD_BOX_RIGHT], [y, y], color=GRID_COLOR, lw=CARD_SEPARATOR_LW, alpha=GRID_ALPHA, transform=ax.transAxes, clip_on=False)
    row_centers = (row_edges[:-1] + row_edges[1:]) / 2
    for (label, value), y in zip(rows, row_centers):
        ax.text(CARD_LABEL_X, y, label, transform=ax.transAxes, fontsize=ROW_LABEL_SIZE, ha="left", va="center", color=LABEL_COLOR)
        ax.text(CARD_VALUE_X, y, value, transform=ax.transAxes, fontsize=ROW_VALUE_SIZE, ha="center", va="center", color=SIGNAL_COLOR)

def render():
    fig, ax = make_card_figure()
    render_card(ax, SPEC["rows"])
    save_figure(fig, OUTPUT_PATH)

if __name__ == "__main__":
    render()
