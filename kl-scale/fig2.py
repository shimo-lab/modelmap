"""Reproduce Figure 2, optionally recomputing t-SNE from logp data."""

import argparse
import json
import pickle
from collections import defaultdict, deque
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.collections import LineCollection
from matplotlib.gridspec import GridSpec
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle

from src.tsne import compute_fig2_coordinates

MODEL_TYPE_ORDER = [
    "llama-1",
    "llama-2",
    "llama-3",
    "mistral",
    "gpt_neox",
    "gptj",
    "gemma",
    "falcon",
    "opt",
    "deepseek",
    "others",
]

# DeepSeek is present in the fine-tuning data but was omitted from type2color.json.
DEFAULT_TYPE_COLORS = {"deepseek": "#191970"}
GENERATION_MARKERS = {0: "o", 1: "s", 2: "D", 3: "^"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Plot quantization, fine-tuning, and layer t-SNE coordinates."
    )
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path("data"),
        help="Directory containing model_info/ and tsne/.",
    )
    parser.add_argument(
        "--output-path",
        type=Path,
        default=Path("output/fig2.png"),
        help="Path of the generated figure.",
    )
    parser.add_argument("--dpi", type=int, default=450)
    parser.add_argument(
        "--recompute-tsne",
        action="store_true",
        help=(
            "Recompute all coordinates from data/logp using double-centered Q "
            "and the paper's perplexities before plotting."
        ),
    )
    parser.add_argument(
        "--random-state",
        type=int,
        default=42,
        help="Random seed used when --recompute-tsne is specified.",
    )
    return parser.parse_args()


def load_json(path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def load_pickle(path):
    with path.open("rb") as f:
        return pickle.load(f)


def load_data(data_dir, tsne_dir=None):
    model_info_dir = data_dir / "model_info"
    tsne_dir = tsne_dir or data_dir / "tsne"

    model_list = load_json(model_info_dir / "model_list.json")
    model_to_type = load_json(model_info_dir / "modelname2type.json")
    type_to_color = load_json(model_info_dir / "type2color.json")
    type_to_color.update(DEFAULT_TYPE_COLORS)

    return {
        "model_list": model_list,
        "model_to_type": model_to_type,
        "type_to_color": type_to_color,
        "sibling_info": load_json(model_info_dir / "sibling_info.json"),
        "quantization": load_pickle(tsne_dir / "8bit_quantization_tsne.pkl"),
        "fine_tuning": load_pickle(tsne_dir / "ft_tsne.pkl"),
        "layer": load_pickle(tsne_dir / "layer_tsne.pkl"),
    }


def model_color(model_name, model_to_type, type_to_color):
    model_type = model_to_type.get(str(model_name), "others")
    return type_to_color.get(model_type, type_to_color["others"])


def style_panel(ax, title):
    ax.set_facecolor("white")
    for spine in ax.spines.values():
        spine.set_color("black")
        spine.set_linewidth(0.5)

    ax.add_patch(
        Rectangle(
            (0, 1.02),
            1,
            0.1,
            transform=ax.transAxes,
            facecolor="lightgray",
            edgecolor="none",
            clip_on=False,
        )
    )
    ax.text(
        0.5,
        1.07,
        title,
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=15,
        fontweight="bold",
    )
    ax.tick_params(labelsize=10, colors="black")
    ax.set_aspect("equal", adjustable="box")


def marker_legend(ax, labels, markers, location="upper left"):
    handles = [
        Line2D(
            [],
            [],
            marker=marker,
            linestyle="",
            markerfacecolor="white",
            markeredgecolor="black",
            markeredgewidth=0.5,
            markersize=8,
        )
        for marker in markers
    ]
    legend = ax.legend(
        handles,
        labels,
        loc=location,
        fontsize=11,
        frameon=True,
        facecolor="whitesmoke",
    )
    legend.get_frame().set_edgecolor("none")


def plot_quantization(ax, data, model_to_type, type_to_color):
    model_names = list(data)
    original = np.vstack([data[name]["original"] for name in model_names])[:, [1, 0]]
    quantized = np.vstack([data[name]["quantized"] for name in model_names])[:, [1, 0]]
    point_colors = [
        model_color(name, model_to_type, type_to_color) for name in model_names
    ]

    segments = np.stack([original, quantized], axis=1)
    ax.add_collection(
        LineCollection(segments, colors="black", linewidths=0.2, alpha=1, zorder=3)
    )
    ax.scatter(
        original[:, 0], original[:, 1], c=point_colors, s=40, marker="o", zorder=2
    )
    ax.scatter(
        quantized[:, 0], quantized[:, 1], c=point_colors, s=40, marker="s", zorder=2
    )

    marker_legend(ax, ["original", "8-bit quantized"], ["o", "s"])
    ax.set_xticks([-10, -5, 0, 5])
    ax.set_yticks([-5, 0, 5])


def fine_tuning_graph(sibling_info, model_names):
    model_names = set(model_names)
    children = defaultdict(list)
    parent_of = {}

    for child, raw_parent in sibling_info.items():
        if isinstance(raw_parent, list) and len(raw_parent) != 1:
            continue
        parents = raw_parent if isinstance(raw_parent, list) else [raw_parent]
        parents = [parent for parent in parents if parent in model_names]
        if child not in model_names or len(parents) != 1:
            continue
        parent = parents[0]
        children[parent].append(child)
        parent_of[child] = parent

    roots = [name for name in model_names if name not in parent_of]
    depths = {}
    queue = deque((root, 0) for root in roots)
    while queue:
        name, depth = queue.popleft()
        if name in depths:
            continue
        depths[name] = depth
        queue.extend((child, depth + 1) for child in children[name])

    return children, depths


def plot_fine_tuning(ax, coordinates, sibling_info, model_to_type, type_to_color):
    children, depths = fine_tuning_graph(sibling_info, coordinates)

    segments = []
    for parent, child_names in children.items():
        for child in child_names:
            segments.append([coordinates[parent], coordinates[child]])
    ax.add_collection(
        LineCollection(segments, colors="black", linewidths=0.2, alpha=1, zorder=3)
    )

    # Plot later generations last so descendants remain visible at overlaps.
    for model_name in sorted(coordinates, key=lambda name: depths[name]):
        point = np.asarray(coordinates[model_name])
        ax.scatter(
            point[0],
            point[1],
            c=[model_color(model_name, model_to_type, type_to_color)],
            s=40,
            marker=GENERATION_MARKERS[depths[model_name]],
            zorder=2,
        )

    marker_legend(
        ax,
        [f"gen {generation + 1}" for generation in GENERATION_MARKERS],
        list(GENERATION_MARKERS.values()),
    )
    ax.set_xticks([-10, -5, 0, 5, 10])
    ax.set_yticks([-5, 0, 5])


def layer_shades(color, count, fade_strength=0.8):
    rgb = np.asarray(colors.to_rgb(color))
    progress = np.linspace(0, 1, count)
    shades = rgb + (1 - rgb) * (1 - progress[:, None]) * fade_strength
    return np.clip(shades, 0, 1)[::-1]


def plot_layers(ax, data, model_list, model_to_type, type_to_color):
    for model_name in model_list:
        if model_name not in data:
            continue

        points = np.asarray(data[model_name])
        # Match the orientation used in the paper's cached Figure 2 panel.
        points = points[:, [1, 0]] * np.array([1, -1])

        shades = layer_shades(
            model_color(model_name, model_to_type, type_to_color), len(points)
        )

        if len(points) > 1:
            segments = np.stack([points[:-1], points[1:]], axis=1)
            ax.add_collection(
                LineCollection(
                    segments,
                    colors=shades[:-1],
                    linewidths=0.4,
                    alpha=0.5,
                    zorder=0,
                )
            )

        ax.scatter(
            points[:, 0],
            points[:, 1],
            c=shades,
            s=20,
            edgecolors="black",
            linewidths=0.1,
            alpha=0.7,
            zorder=1,
        )
        ax.scatter(
            points[-1, 0],
            points[-1, 1],
            marker="s",
            c="white",
            s=30,
            edgecolors="black",
            linewidths=0.1,
            zorder=2,
        )


def add_type_legend(fig, grid_spec, type_to_color):
    ax = fig.add_subplot(grid_spec)
    ax.axis("off")
    for model_type in MODEL_TYPE_ORDER:
        ax.scatter(
            [],
            [],
            label=model_type,
            color=type_to_color[model_type],
            s=40,
        )
    legend = ax.legend(
        ncol=len(MODEL_TYPE_ORDER),
        loc="center",
        fontsize=11.5,
        frameon=True,
        facecolor="whitesmoke",
        columnspacing=0.7,
        handletextpad=0.01,
    )
    legend.get_frame().set_edgecolor("none")


def create_figure(data):
    fig = plt.figure(figsize=(12, 4), tight_layout=True, dpi=450)
    grid = GridSpec(
        2,
        3,
        figure=fig,
        width_ratios=[1, 1, 1],
        height_ratios=[1.2, 0.1],
    )
    axes = [fig.add_subplot(grid[0, index]) for index in range(3)]

    style_panel(axes[0], "(a) Quantization")
    style_panel(axes[1], "(b) Fine-tuning")
    style_panel(axes[2], "(c) Layer")

    plot_quantization(
        axes[0], data["quantization"], data["model_to_type"], data["type_to_color"]
    )
    plot_fine_tuning(
        axes[1],
        data["fine_tuning"],
        data["sibling_info"],
        data["model_to_type"],
        data["type_to_color"],
    )
    plot_layers(
        axes[2],
        data["layer"],
        data["model_list"],
        data["model_to_type"],
        data["type_to_color"],
    )
    add_type_legend(fig, grid[1, :], data["type_to_color"])
    return fig


def main() -> None:
    args = parse_args()
    if args.recompute_tsne:
        coordinates = compute_fig2_coordinates(
            args.data_dir, random_state=args.random_state
        )
        data = load_data(args.data_dir)
        data.update(coordinates)
    else:
        data = load_data(args.data_dir)
    fig = create_figure(data)

    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output_path, dpi=args.dpi)
    plt.close(fig)
    print(f"Saved figure to {args.output_path}")


if __name__ == "__main__":
    main()
