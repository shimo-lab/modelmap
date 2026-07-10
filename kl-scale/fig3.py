"""Create Figure 3 from KL distributions calculated in memory."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
from matplotlib.patches import PathPatch, Rectangle
from matplotlib.scale import SymmetricalLogTransform

from src.calc_kl import calculate_all

PLOT_SETTINGS = (
    ("pretraining_last_1k", "Later"),
    ("pretraining_first_1k", "Early"),
    ("pretraining_seed", "Seed"),
    ("pretraining_size", "Size"),
    ("quantization_8bit", "8-bit"),
    ("quantization_4bit", "4-bit"),
    ("finetuning_parent_child", "FT"),
    ("finetuning_within_type", "Intra-type"),
    ("finetuning_random", "Random"),
    ("layer_adjacent", "Layer"),
)

SECTION_SPANS = (
    (0, 3, "Sec. 3.1"),
    (4, 5, "Sec. 3.2"),
    (6, 8, "Sec. 3.3"),
    (9, 9, "Sec. 3.4"),
)

LINTHRESH = 0.1
LINSCALE = 0.9
DISPLAY_MAX = 50.0
COLORBAR_MAX = 10.0
TICK_VALUES = np.asarray([0, 0.05, 0.1, 0.5, 1, 5, 10, 50], dtype=float)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Calculate KL distributions and create Figure 3."
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path("data"),
        help="Directory containing texts.json, logp/, and model_info/.",
    )
    parser.add_argument(
        "--output-path",
        type=Path,
        default=Path("output/fig3.png"),
        help="Path of the generated figure.",
    )
    parser.add_argument("--dpi", type=int, default=450)
    parser.add_argument("--random-seed", type=int, default=0)
    parser.add_argument("--first-window", type=int, default=50)
    parser.add_argument("--last-window", type=int, default=50)
    return parser.parse_args()


def symlog_transform(values: np.ndarray) -> np.ndarray:
    transform = SymmetricalLogTransform(
        base=10,
        linthresh=LINTHRESH,
        linscale=LINSCALE,
    )
    return transform.transform_non_affine(np.asarray(values, dtype=float))


def format_tick(value: float) -> str:
    if value == 0:
        return "0"
    if value < 0.1:
        return f"{value:.2f}"
    if value < 1:
        return f"{value:.1f}"
    return f"{value:g}"


def add_gradient_fill(
    ax: plt.Axes,
    body,
    *,
    x_limits: tuple[float, float],
    y_limits: tuple[float, float],
    cmap: mpl.colors.Colormap,
    color_max: float,
) -> None:
    path = body.get_paths()[0]
    body.set_facecolor("none")
    body.set_edgecolor("0.25")
    body.set_linewidth(0.5)

    patch = PathPatch(path, facecolor="none", edgecolor="none")
    ax.add_patch(patch)
    gradient = np.minimum(
        np.linspace(y_limits[0], y_limits[1], 1024),
        color_max,
    ).reshape(-1, 1)
    image = ax.imshow(
        gradient,
        origin="lower",
        aspect="auto",
        extent=(*x_limits, *y_limits),
        cmap=cmap,
        norm=Normalize(y_limits[0], color_max, clip=True),
        interpolation="nearest",
        zorder=body.get_zorder() - 0.1,
    )
    image.set_clip_path(patch)


def add_section_headers(ax: plt.Axes, positions: np.ndarray) -> None:
    y = 1.025
    height = 0.105
    for start, end, label in SECTION_SPANS:
        left = positions[start] - 0.43
        right = positions[end] + 0.43
        rectangle = Rectangle(
            (left, y),
            right - left,
            height,
            transform=ax.get_xaxis_transform(),
            facecolor="#e6e6e6",
            edgecolor="none",
            clip_on=False,
            zorder=0,
        )
        ax.add_patch(rectangle)
        ax.text(
            (left + right) / 2,
            y + height / 2,
            label,
            transform=ax.get_xaxis_transform(),
            ha="center",
            va="center",
            fontsize=15,
            fontweight="bold",
            clip_on=False,
        )


def plot_figure(results: dict[str, np.ndarray]) -> plt.Figure:
    labels = [label for _, label in PLOT_SETTINGS]
    raw_values = [
        np.clip(np.asarray(results[key], dtype=float), None, DISPLAY_MAX)
        for key, _ in PLOT_SETTINGS
    ]
    transformed_values = [symlog_transform(values) for values in raw_values]
    positions = np.arange(len(PLOT_SETTINGS), dtype=float)

    fig, ax = plt.subplots(figsize=(14.5, 4.8))
    violins = ax.violinplot(
        transformed_values,
        positions=positions,
        widths=0.72,
        showmeans=False,
        showmedians=False,
        showextrema=False,
        points=200,
        bw_method="scott",
    )

    y_min = float(symlog_transform(np.asarray([0]))[0])
    y_max = float(symlog_transform(np.asarray([DISPLAY_MAX]))[0])
    x_limits = (-0.65, len(PLOT_SETTINGS) - 0.35)
    y_limits = (y_min, y_max)
    cmap = mpl.colormaps["rainbow"]
    colorbar_max = float(symlog_transform(np.asarray([COLORBAR_MAX]))[0])

    for body in violins["bodies"]:
        add_gradient_fill(
            ax,
            body,
            x_limits=x_limits,
            y_limits=y_limits,
            cmap=cmap,
            color_max=colorbar_max,
        )

    medians = symlog_transform(np.asarray([np.median(values) for values in raw_values]))
    ax.scatter(
        positions,
        medians,
        marker="_",
        s=115,
        linewidths=1.8,
        color="black",
        zorder=4,
        label="Median",
    )

    tick_positions = symlog_transform(TICK_VALUES)
    ax.set_xlim(*x_limits)
    ax.set_ylim(*y_limits)
    ax.set_xticks(positions, labels)
    ax.set_yticks(tick_positions, [format_tick(value) for value in TICK_VALUES])
    ax.set_ylabel("KL (bits/byte)", fontsize=18)
    ax.tick_params(axis="x", labelsize=14, pad=6)
    ax.tick_params(axis="y", labelsize=13)
    ax.grid(axis="y", color="0.88", linewidth=0.7, zorder=-2)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    add_section_headers(ax, positions)

    colorbar = fig.colorbar(
        mpl.cm.ScalarMappable(
            norm=Normalize(y_min, colorbar_max, clip=True),
            cmap=cmap,
        ),
        ax=ax,
        pad=0.015,
        fraction=0.022,
    )
    colorbar_ticks = TICK_VALUES[TICK_VALUES <= COLORBAR_MAX]
    colorbar.set_ticks(symlog_transform(colorbar_ticks))
    colorbar.set_ticklabels([format_tick(value) for value in colorbar_ticks])
    colorbar.ax.tick_params(labelsize=11)
    colorbar.set_label("KL (bits/byte)", fontsize=13)

    ax.legend(
        loc="upper left",
        frameon=False,
        fontsize=11,
        handletextpad=0.3,
    )
    fig.subplots_adjust(left=0.07, right=0.93, bottom=0.18, top=0.80)
    return fig


def main() -> None:
    args = parse_args()
    results = calculate_all(
        args.data_dir,
        first_window=args.first_window,
        last_window=args.last_window,
        random_seed=args.random_seed,
    )

    figure = plot_figure(results)
    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(args.output_path, dpi=args.dpi, bbox_inches="tight")
    plt.close(figure)
    print(f"Saved figure to {args.output_path}")


if __name__ == "__main__":
    main()
