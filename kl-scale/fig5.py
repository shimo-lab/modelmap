"""Reproduce Figure 5: diffusion in log-likelihood and weight spaces."""

import argparse
import pickle
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from sklearn.linear_model import LinearRegression

from src.metrics import approximate_kl_bits_per_byte
from src.preprocess import preprocess_pretraining
from src.pythia import (
    PRETRAINING_CHECKPOINT_EXCLUSIONS,
    PYTHIA_CHECKPOINT_STEPS,
    PYTHIA_MODEL_SIZES,
    format_checkpoint_step,
)

MODEL_SIZES = PYTHIA_MODEL_SIZES
CHECKPOINTS = np.asarray(PYTHIA_CHECKPOINT_STEPS, dtype=int)
COLORS = {
    size: plt.get_cmap(cmap)(0.8)
    for size, cmap in zip(
        MODEL_SIZES,
        ("Reds", "Oranges", "Greens", "Blues", "Purples"),
    )
}
MARKERS = dict(zip(MODEL_SIZES, ("o", "s", "v", "^", "D")))
EXCLUDED_CHECKPOINTS = PRETRAINING_CHECKPOINT_EXCLUSIONS
LABEL_FONT_SIZE = 20
LEGEND_FONT_SIZE = 17
TICK_FONT_SIZE = 17


def load_pickle(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open("rb") as f:
        return pickle.load(f)


def validate_weight_distances(weight_distances):
    expected_shape = (len(CHECKPOINTS), len(CHECKPOINTS))
    missing = set(MODEL_SIZES) - set(weight_distances)
    if missing:
        raise ValueError(f"Missing weight distances for: {sorted(missing)}")

    for model_size in MODEL_SIZES:
        matrix = weight_distances[model_size]
        if not isinstance(matrix, np.ndarray) or matrix.shape != expected_shape:
            raise ValueError(
                f"Weight distances for {model_size} must have shape "
                f"{expected_shape}, got {getattr(matrix, 'shape', None)}."
            )


def prepare_logp(logp_results):
    selected = {
        model_size: logp_results[model_size]
        for model_size in MODEL_SIZES
        if model_size in logp_results
    }
    missing = set(MODEL_SIZES) - set(selected)
    if missing:
        raise ValueError(f"Missing logp results for: {sorted(missing)}")

    return preprocess_pretraining(
        selected,
        exclude_checkpoints=EXCLUDED_CHECKPOINTS,
    )


def kl_from_start(checkpoint_logp, start_step, target_steps, mean_text_bytes):
    """Estimate KL in bits/byte from centered log-likelihood differences."""
    if start_step not in checkpoint_logp:
        return np.full(len(target_steps), np.nan)

    start_logp = checkpoint_logp[start_step]
    values = []
    for target_step in target_steps:
        if target_step not in checkpoint_logp:
            values.append(np.nan)
            continue
        values.append(
            approximate_kl_bits_per_byte(
                checkpoint_logp[target_step],
                start_logp,
                mean_text_bytes=mean_text_bytes,
            )
        )
    return np.asarray(values)


def fit_diffusion_exponent(elapsed_steps, distances):
    elapsed_steps = np.asarray(elapsed_steps, dtype=np.float64)
    distances = np.asarray(distances, dtype=np.float64)
    valid = (
        np.isfinite(elapsed_steps)
        & np.isfinite(distances)
        & (elapsed_steps > 0)
        & (distances > 0)
    )
    if valid.sum() < 2:
        return np.nan, np.nan

    x = np.log(elapsed_steps[valid]).reshape(-1, 1)
    y = np.log(distances[valid])
    regression = LinearRegression().fit(x, y)
    return float(regression.coef_[0]), float(regression.score(x, y))


def window_steps(start_index, window_size):
    return CHECKPOINTS[start_index + 1 : start_index + window_size + 1]


def compute_exponent_series(
    processed_logp,
    weight_distances,
    mean_text_bytes,
    *,
    window_size,
    minimum_start_step,
):
    starts = np.arange(len(CHECKPOINTS) - window_size)
    starts = starts[CHECKPOINTS[starts] >= minimum_start_step]
    result = {"logp": {}, "weight": {}, "r2": {"logp": {}, "weight": {}}}

    for model_size in MODEL_SIZES:
        logp_exponents = np.full(len(starts), np.nan)
        weight_exponents = np.full(len(starts), np.nan)
        logp_r2 = np.full(len(starts), np.nan)
        weight_r2 = np.full(len(starts), np.nan)

        for output_index, start_index in enumerate(starts):
            start_step = int(CHECKPOINTS[start_index])
            target_steps = window_steps(start_index, window_size)
            if (model_size, start_step) in EXCLUDED_CHECKPOINTS:
                continue

            elapsed_steps = target_steps - start_step
            kl_values = kl_from_start(
                processed_logp[model_size],
                start_step,
                target_steps,
                mean_text_bytes,
            )
            weight_values = weight_distances[model_size][
                start_index,
                start_index + 1 : start_index + window_size + 1,
            ]
            excluded_targets = np.array(
                [
                    (model_size, int(target_step)) in EXCLUDED_CHECKPOINTS
                    for target_step in target_steps
                ]
            )
            kl_values[excluded_targets] = np.nan
            weight_values = np.asarray(weight_values, dtype=np.float64).copy()
            weight_values[excluded_targets] = np.nan

            logp_exponents[output_index], logp_r2[output_index] = (
                fit_diffusion_exponent(elapsed_steps, kl_values)
            )
            weight_exponents[output_index], weight_r2[output_index] = (
                fit_diffusion_exponent(elapsed_steps, weight_values)
            )

        result["logp"][model_size] = logp_exponents
        result["weight"][model_size] = weight_exponents
        result["r2"]["logp"][model_size] = logp_r2
        result["r2"]["weight"][model_size] = weight_r2

    return CHECKPOINTS[starts], result


def plot_distance_panel(
    ax_kl,
    processed_logp,
    weight_distances,
    mean_text_bytes,
    *,
    start_step,
    window_size,
):
    start_matches = np.flatnonzero(CHECKPOINTS == start_step)
    if len(start_matches) != 1:
        raise ValueError(f"Checkpoint {start_step} is not available.")
    start_index = int(start_matches[0])
    target_steps = window_steps(start_index, window_size)
    if len(target_steps) != window_size:
        raise ValueError("The selected start does not have a complete window.")
    elapsed_steps = target_steps - start_step

    kl_by_size = {}
    weight_by_size = {}
    for model_size in MODEL_SIZES:
        kl_by_size[model_size] = kl_from_start(
            processed_logp[model_size],
            start_step,
            target_steps,
            mean_text_bytes,
        )
        weight_by_size[model_size] = weight_distances[model_size][
            start_index,
            start_index + 1 : start_index + window_size + 1,
        ]

    all_kl = np.concatenate(list(kl_by_size.values()))
    all_weight = np.concatenate(list(weight_by_size.values()))
    valid_kl = all_kl[np.isfinite(all_kl) & (all_kl > 0)]
    valid_weight = all_weight[np.isfinite(all_weight) & (all_weight > 0)]
    if len(valid_kl) == 0 or len(valid_weight) == 0:
        raise ValueError("The left panel has no positive finite distances.")

    # This scale factor aligns both units on one panel without rescaling either
    # data series. The left and right y-axes remain labeled in their own units.
    scale_from_kl_to_dist = valid_weight.min() / valid_kl.min()

    ax_weight = ax_kl.twinx()
    for model_size in MODEL_SIZES:
        style = {
            "color": COLORS[model_size],
            "marker": MARKERS[model_size],
            "markersize": 5,
            "linewidth": 1,
        }
        ax_kl.plot(elapsed_steps, kl_by_size[model_size], **style)
        ax_weight.plot(
            elapsed_steps,
            weight_by_size[model_size],
            linestyle="--",
            **style,
        )

    ax_kl.set_xscale("log")
    ax_kl.set_yscale("log")
    ax_weight.set_yscale("log")
    ax_kl.set_xlabel(
        f"Step from {format_checkpoint_step(start_step)}",
        fontsize=LABEL_FONT_SIZE,
    )
    ax_kl.set_ylabel("KL (bits/byte)", fontsize=LABEL_FONT_SIZE)
    ax_weight.set_ylabel(
        "Weight distance",
        fontsize=LABEL_FONT_SIZE,
        rotation=-90,
        labelpad=20,
    )
    ax_kl.tick_params(axis="both", labelsize=TICK_FONT_SIZE)
    ax_weight.tick_params(axis="y", labelsize=TICK_FONT_SIZE)

    weight_min = 10 ** np.floor(np.log10(valid_weight.min()))
    weight_max = 10 ** np.ceil(np.log10(valid_weight.max()))
    ax_weight.set_ylim(weight_min, weight_max)
    ax_kl.set_ylim(
        weight_min / scale_from_kl_to_dist,
        weight_max / scale_from_kl_to_dist,
    )

    reference_x = np.array([elapsed_steps.min(), elapsed_steps.max()])
    reference_y = weight_min * reference_x / reference_x.min()
    ax_weight.plot(
        reference_x,
        reference_y,
        color="0.7",
        linewidth=6,
        alpha=0.5,
        label="c=1",
    )
    ax_weight.legend(loc="upper left", fontsize=LEGEND_FONT_SIZE)


def plot_exponent_panel(ax, start_steps, exponent_results):
    for model_size in MODEL_SIZES:
        logp_exponents = exponent_results["logp"][model_size].copy()
        weight_exponents = exponent_results["weight"][model_size].copy()
        if model_size == "1b":
            excluded_index = np.flatnonzero(start_steps == 116_000)
            if len(excluded_index) == 1:
                index = int(excluded_index[0])
                if 0 < index < len(start_steps) - 1:
                    logp_exponents[index] = np.interp(
                        start_steps[index],
                        start_steps[[index - 1, index + 1]],
                        logp_exponents[[index - 1, index + 1]],
                    )
                    weight_exponents[index] = np.interp(
                        start_steps[index],
                        start_steps[[index - 1, index + 1]],
                        weight_exponents[[index - 1, index + 1]],
                    )

        ax.plot(
            start_steps,
            logp_exponents,
            color=COLORS[model_size],
            linewidth=1,
        )
        ax.plot(
            start_steps,
            weight_exponents,
            color=COLORS[model_size],
            linewidth=1,
            linestyle="--",
        )

    ax.set_ylabel("Diffusion exponent", fontsize=LABEL_FONT_SIZE)
    ticks = np.arange(10_000, 130_000 + 1, 20_000)
    ax.set_xticks(ticks)
    ax.set_xticklabels(
        [format_checkpoint_step(int(step)) for step in ticks],
        rotation=-45,
        ha="left",
        fontsize=TICK_FONT_SIZE,
    )
    ax.tick_params(axis="y", labelsize=TICK_FONT_SIZE)
    ax.set_xlim(8_000, 135_000)


def plot_figure(
    logp_results,
    weight_distances,
    output_path,
    *,
    start_step=120_000,
    window_size=10,
):
    validate_weight_distances(weight_distances)
    processed_logp, preprocessing_info = prepare_logp(
        logp_results,
    )
    mean_text_bytes = float(preprocessing_info["mean_text_bytes"])

    start_steps, exponent_results = compute_exponent_series(
        processed_logp,
        weight_distances,
        mean_text_bytes,
        window_size=window_size,
        minimum_start_step=1_000,
    )

    fig, axes = plt.subplots(1, 2, figsize=(10, 4), dpi=300)
    fig.subplots_adjust(wspace=0.7)
    plot_distance_panel(
        axes[0],
        processed_logp,
        weight_distances,
        mean_text_bytes,
        start_step=start_step,
        window_size=window_size,
    )
    plot_exponent_panel(axes[1], start_steps, exponent_results)

    legend_handles = [
        Line2D([], [], color="black", linewidth=2, label="Log-likelihood"),
        Line2D(
            [],
            [],
            color="black",
            linewidth=2,
            linestyle="--",
            label="Weight",
        ),
        *[
            Line2D([], [], color=COLORS[size], linewidth=2, label=size.upper())
            for size in MODEL_SIZES
        ],
    ]
    fig.legend(
        handles=legend_handles,
        loc="upper center",
        ncol=4,
        bbox_to_anchor=(0.5, 1.15),
        handlelength=1.5,
        columnspacing=1.5,
        fontsize=LEGEND_FONT_SIZE,
    )

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, bbox_inches="tight", dpi=300)
    plt.close(fig)
    return exponent_results, preprocessing_info


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--logp-path",
        type=Path,
        default=Path("data/logp/pretraining_logp.pkl"),
    )
    parser.add_argument(
        "--weight-distance-path",
        type=Path,
        default=Path("data/weight_distance/weight_distance.pkl"),
    )
    parser.add_argument(
        "--output-path",
        "--output",
        dest="output_path",
        type=Path,
        default=Path("output/fig5.png"),
    )
    parser.add_argument("--start-step", type=int, default=120_000)
    parser.add_argument("--window-size", type=int, default=10)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logp_results = load_pickle(args.logp_path)
    weight_distances = load_pickle(args.weight_distance_path)
    plot_figure(
        logp_results,
        weight_distances,
        args.output_path,
        start_step=args.start_step,
        window_size=args.window_size,
    )


if __name__ == "__main__":
    main()
