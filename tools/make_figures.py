"""Generate the profile figures added in the 2026-11 refresh (light and dark SVG).

Diagrams only: no measured or simulated data. Run from the repo root:
    python tools/make_figures.py
"""
from pathlib import Path

import logging

import matplotlib

matplotlib.use("svg")
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).resolve().parent.parent / "profile" / "assets"
FONT = "'Segoe UI', Helvetica, Arial, sans-serif"

# GitHub Primer colours, matching the existing profile figures.
THEMES = {
    "light": dict(text="#1f2328", muted="#8c959f", card="#f6f8fa", border="#d0d7de",
                  accent="#0969da", highlight="#bf3989", good="#1a7f37"),
    "dark": dict(text="#e6edf3", muted="#6e7681", card="#161b22", border="#30363d",
                 accent="#4493f8", highlight="#f778ba", good="#3fb950"),
}

plt.rcParams.update({
    "svg.fonttype": "none",
    "svg.hashsalt": "morphonerva",
    "font.family": ["Segoe UI", "Helvetica", "Arial", "sans-serif"],
})


def canvas(height_in):
    fig = plt.figure(figsize=(12, height_in))
    fig.patch.set_alpha(0)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 864)
    ax.set_ylim(0, height_in * 72)
    ax.axis("off")
    return fig, ax


def card(ax, x, y, w, h, c, edge=None, fill=None, lw=1.2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=8",
                                fc=fill or c["card"], ec=edge or c["border"], lw=lw))


def arrow(ax, x0, y0, x1, y1, color, style="-|>", ls="-", rad=0.0):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle=style, mutation_scale=12,
                                 color=color, lw=1.4, linestyle=ls,
                                 connectionstyle=f"arc3,rad={rad}"))


def save(fig, name, theme):
    fig.savefig(OUT / f"{name}-{theme}.svg", metadata={"Date": None}, transparent=True)
    plt.close(fig)


def evidence_ladder(theme):
    """Four public evidence labels as a staircase of increasing strength."""
    c = THEMES[theme]
    fig, ax = canvas(3.3)
    steps = [
        ("Target", "a goal, not a result", 52),
        ("Estimated", "from a model or simulation,", 86, "assumptions stated"),
        ("Measured", "on our hardware: workload,", 120, "precision, power boundary"),
        ("Externally", "reproduced by", 154, "someone else"),
    ]
    x, w, gap, base = 24, 150, 14, 30
    for i, step in enumerate(steps):
        title, line1, h = step[0], step[1], step[2]
        line2 = step[3] if len(step) > 3 else None
        xi = x + i * (w + gap)
        strong = i >= 2
        card(ax, xi, base, w, h, c, edge=c["accent"] if strong else c["border"],
             lw=1.8 if strong else 1.2)
        ax.text(xi + w / 2, base + h - 16, title if title != "Externally" else "Externally verified",
                ha="center", va="center", fontsize=11, fontweight="bold",
                color=c["accent"] if strong else c["text"])
        ax.text(xi + w / 2, base + h - 33, line1, ha="center", va="center", fontsize=8.2,
                color=c["muted"])
        if line2:
            ax.text(xi + w / 2, base + h - 45, line2, ha="center", va="center", fontsize=8.2,
                    color=c["muted"])
    # Bracket over the strong steps.
    bx0, bx1 = x + 2 * (w + gap), x + 4 * (w + gap) - gap
    by = base + 154 + 22
    ax.plot([bx0, bx0, bx1, bx1], [by - 6, by, by, by - 6], color=c["highlight"], lw=1.4)
    ax.text((bx0 + bx1) / 2, by + 10, "performance results are published from here",
            ha="center", va="center", fontsize=9.5, fontweight="bold", color=c["highlight"])
    ax.text(x, by + 10, "stronger evidence  →", ha="left", va="center", fontsize=9.5,
            color=c["muted"])
    # Sourced: a side label, not a rung.
    sx = x + 4 * (w + gap) + 6
    card(ax, sx, base, 864 - sx - 18, 72, c)
    ax.text(sx + (864 - sx - 18) / 2, base + 56, "Sourced", ha="center", va="center",
            fontsize=11, fontweight="bold", color=c["text"])
    ax.text(sx + (864 - sx - 18) / 2, base + 39, "someone else's published", ha="center",
            va="center", fontsize=8.2, color=c["muted"])
    ax.text(sx + (864 - sx - 18) / 2, base + 27, "result, always cited", ha="center",
            va="center", fontsize=8.2, color=c["muted"])
    save(fig, "evidence-ladder", theme)


def verification_flow(theme):
    """Generic model-to-hardware checking flow with a stop-the-line loop."""
    c = THEMES[theme]
    fig, ax = canvas(2.6)
    stages = [
        ("Reference", "model", "defines correct"),
        ("Hardware", "design", "written to spec"),
        ("Simulation", "", "two independent tools"),
        ("Gate-level", "check", "after synthesis"),
        ("Formal", "proofs", "for key properties"),
        ("FPGA", "build", "real device"),
        ("Board", "measurement", "with instruments"),
    ]
    n, x0, gap = len(stages), 10, 18
    w = (864 - 2 * x0 - (n - 1) * gap) / n
    y, h = 70, 82
    for i, (a, b, note) in enumerate(stages):
        xi = x0 + i * (w + gap)
        first = i == 0
        card(ax, xi, y, w, h, c, edge=c["accent"] if first else c["border"],
             lw=1.8 if first else 1.2)
        ax.text(xi + w / 2, y + h - 22, a, ha="center", va="center", fontsize=11,
                fontweight="bold", color=c["accent"] if first else c["text"])
        if b:
            ax.text(xi + w / 2, y + h - 38, b, ha="center", va="center", fontsize=11,
                    fontweight="bold", color=c["accent"] if first else c["text"])
        ax.text(xi + w / 2, y + 16, note, ha="center", va="center", fontsize=8.2,
                color=c["muted"])
        if i < n - 1:
            arrow(ax, xi + w + 2, y + h / 2, xi + w + gap - 2, y + h / 2, c["muted"])
    # Every stage is compared with the reference model; a mismatch stops the line.
    xs = x0 + w / 2
    xe = x0 + (n - 1) * (w + gap) + w / 2
    ly = y - 22
    ax.plot([xs, xe], [ly, ly], color=c["highlight"], lw=1.4, ls=(0, (4, 3)))
    for i in range(1, n):
        xi = x0 + i * (w + gap) + w / 2
        ax.plot([xi, xi], [y, ly], color=c["highlight"], lw=1.0, ls=(0, (2, 3)))
    arrow(ax, xs, ly, xs, y - 2, c["highlight"])
    ax.text(864 / 2, ly - 16, "every step is compared with the reference model; "
            "a mismatch stops the line", ha="center", va="center", fontsize=9.5,
            fontweight="bold", color=c["highlight"])
    save(fig, "verification-flow", theme)


def roadmap(theme):
    """Stage-level roadmap. Status words describe the present only."""
    c = THEMES[theme]
    fig, ax = canvas(2.3)
    stops = [
        ("Research", ["models, encoders,", "methods"], "done"),
        ("Prototype 0", ["digital core, in design", "and simulation"], "now"),
        ("Prototype 1", ["measured on", "FPGA hardware"], "next"),
        ("Pilots", ["with design", "partners"], "next"),
        ("Custom silicon", ["efficiency at", "scale"], "next"),
    ]
    xs = [58 + i * (805 - 58) / 4 for i in range(5)]
    y = 112
    ax.plot([xs[0], xs[-1]], [y, y], color=c["border"], lw=3, solid_capstyle="butt")
    ax.plot([xs[0], xs[1]], [y, y], color=c["accent"], lw=3, solid_capstyle="butt")
    for x, (name, sub, state) in zip(xs, stops):
        if state == "done":
            ax.plot(x, y, "o", ms=12, mfc=c["accent"], mec=c["accent"], mew=2)
        elif state == "now":
            ax.plot(x, y, "o", ms=16, mfc=c["highlight"], mec=c["accent"], mew=2)
            ax.text(x, y + 30, "we are here", ha="center", va="center", fontsize=9.5,
                    fontweight="bold", color=c["highlight"])
        else:
            ax.plot(x, y, "o", ms=12, mfc=c["card"], mec=c["muted"], mew=2)
        ax.text(x, y - 32, name, ha="center", va="center", fontsize=11, fontweight="bold",
                color=c["text"])
        for k, line in enumerate(sub):
            ax.text(x, y - 56 - 11 * k, line, ha="center", va="center", fontsize=8.6,
                    color=c["muted"])
    save(fig, "roadmap", theme)


if __name__ == "__main__":
    for t in THEMES:
        evidence_ladder(t)
        verification_flow(t)
        roadmap(t)
    print("wrote figures to", OUT)
