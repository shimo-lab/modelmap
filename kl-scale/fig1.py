"""Create Figure 1 from pretraining t-SNE trajectories."""

import argparse
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.collections import LineCollection

from src.tsne import (
    FIG1_EXCLUDE_CHECKPOINTS,
    FIG1_EXCLUDE_MODEL_SIZES,
    FIG1_MODEL_ORDER,
    PAPER_PERPLEXITY,
    load_pretraining_embedding,
    prepare_fig1_inputs,
    run_tsne,
)

STYLE_SEQUENCE = [
    ("Greys", "X"),
    ("Greys", "X"),
    ("Greys", "X"),
    ("Greys", "X"),
    ("Greys", "X"),
    ("Greys", "X"),
    ("Greys", "X"),
    ("Reds", "o"),
    ("Oranges", "s"),
    ("Greens", "v"),
    ("Blues", "^"),
    ("Purples", "D"),
]

LEGEND_ITEMS = [
    ("410M", "Reds", "o"),
    ("410M other seeds", "Greys", "X"),
    ("1B", "Oranges", "s"),
    ("1.4B", "Greens", "v"),
    ("2.8B", "Blues", "^"),
    ("6.9B", "Purples", "D"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create the pretraining t-SNE trajectory plot."
    )
    parser.add_argument(
        "--input-path",
        type=Path,
        default=Path("data/logp/pretraining_logp.pkl"),
        help="Path to pretraining logp pickle.",
    )
    parser.add_argument(
        "--tsne-path",
        type=Path,
        default=Path("data/tsne/pretraining_tsne_2d.pkl"),
        help="Optional read-only path to a cached 2D t-SNE pickle.",
    )
    parser.add_argument(
        "--output-path",
        type=Path,
        default=Path("output/fig1.png"),
        help="Path to save the generated figure.",
    )
    parser.add_argument(
        "--recompute-tsne",
        action="store_true",
        help="Ignore the read-only cache and recompute t-SNE in memory.",
    )
    parser.add_argument("--random-state", type=int, default=42)
    return parser.parse_args()


def trajectory_colors(
    colormap_name: str,
    point_count: int,
    fade_strength: float = 0.8,
) -> np.ndarray:
    base_color = np.array(colors.to_rgb(mpl.colormaps[colormap_name](0.8)))
    shades = np.array(
        [
            base_color
            + (1 - base_color)
            * (1 - point_index / max(point_count - 1, 1))
            * fade_strength
            for point_index in range(point_count)
        ]
    )
    return np.clip(shades, 0, 1)


def adjacent_squared_distances(
    q_matrix: np.ndarray,
    model_slices: dict[str, slice],
) -> np.ndarray:
    distances = []
    for model_slice in model_slices.values():
        model_q_matrix = q_matrix[model_slice]
        distances.extend(
            np.linalg.norm(
                model_q_matrix[point_index + 1] - model_q_matrix[point_index]
            )
            ** 2
            for point_index in range(len(model_q_matrix) - 1)
        )
    return np.asarray(distances, dtype=np.float64)


def add_legend(axes: plt.Axes) -> None:
    for label, colormap_name, marker in LEGEND_ITEMS:
        axes.scatter(
            [],
            [],
            label=label,
            color=mpl.colormaps[colormap_name](0.8),
            marker=marker,
            s=115,
            edgecolors="black",
            linewidths=0.45,
        )

    axes.legend(
        loc="lower center",
        bbox_to_anchor=(0.5, 1.03),
        ncol=3,
        frameon=True,
        fontsize=18,
        handletextpad=0.4,
        columnspacing=1.8,
        borderpad=0.8,
    )


def plot_trajectories(
    embedding: np.ndarray,
    q_matrix: np.ndarray,
    model_names: list[str],
    model_slices: dict[str, slice],
) -> plt.Figure:
    if len(model_names) > len(STYLE_SEQUENCE):
        raise ValueError(
            f"STYLE_SEQUENCE has {len(STYLE_SEQUENCE)} entries, "
            f"but {len(model_names)} models were loaded."
        )

    plot_xy = embedding[:, [1, 0]]

    figure, axes = plt.subplots(figsize=(7.2, 7.4))
    all_distances = adjacent_squared_distances(q_matrix, model_slices)
    linewidth_scale = np.quantile(all_distances, 0.95)
    if linewidth_scale <= 0:
        linewidth_scale = 1.0

    add_legend(axes)

    for model_index, model_name in enumerate(model_names):
        model_slice = model_slices[model_name]
        points = plot_xy[model_slice]
        model_q_matrix = q_matrix[model_slice]
        colormap_name, marker = STYLE_SEQUENCE[model_index]
        point_colors = trajectory_colors(colormap_name, len(points))

        if len(points) > 1:
            segments = np.stack([points[:-1], points[1:]], axis=1)
            distances = np.array(
                [
                    np.linalg.norm(
                        model_q_matrix[point_index + 1] - model_q_matrix[point_index]
                    )
                    ** 2
                    for point_index in range(len(model_q_matrix) - 1)
                ]
            )
            linewidths = np.minimum(distances, linewidth_scale) / linewidth_scale * 0.45
            line_collection = LineCollection(
                segments,
                colors=point_colors[1:],
                linewidths=linewidths,
                alpha=0.85,
                zorder=1,
            )
            axes.add_collection(line_collection)

        axes.scatter(
            points[:, 0],
            points[:, 1],
            c=point_colors,
            s=9 if marker != "X" else 12,
            marker=marker,
            alpha=0.78,
            edgecolors="black",
            linewidths=0.08,
            zorder=2,
        )
        axes.scatter(
            points[-1, 0],
            points[-1, 1],
            c=[point_colors[-1]],
            s=145 if marker != "X" else 120,
            marker=marker,
            edgecolors="black",
            linewidths=0.5,
            zorder=3,
        )

    axes.tick_params(labelsize=17, width=1.6, length=8, pad=8)
    for spine in axes.spines.values():
        spine.set_linewidth(1.4)
    axes.set_aspect("equal", "box")

    return figure


def main() -> None:
    args = parse_args()

    prepared = prepare_fig1_inputs(
        args.input_path,
        model_order=FIG1_MODEL_ORDER,
        exclude_model_sizes=FIG1_EXCLUDE_MODEL_SIZES,
        exclude_checkpoints=FIG1_EXCLUDE_CHECKPOINTS,
    )
    q_matrix = prepared["q_matrix"]
    model_names = prepared["model_names"]
    model_slices = prepared["model_slices"]

    embedding = None
    if not args.recompute_tsne:
        embedding = load_pretraining_embedding(
            args.tsne_path,
            q_matrix,
            model_names,
            model_slices,
        )
    if embedding is None:
        embedding = run_tsne(
            q_matrix,
            PAPER_PERPLEXITY["pretraining"],
            args.random_state,
        )

    figure = plot_trajectories(embedding, q_matrix, model_names, model_slices)
    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(args.output_path, dpi=300, bbox_inches="tight")
    plt.close(figure)
    print(f"Saved figure to {args.output_path}")


if __name__ == "__main__":
    main()
