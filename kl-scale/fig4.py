"""Reproduce Figure 4: KL divergence during Pythia pretraining."""

import argparse
import pickle
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from src.metrics import kl_bits_per_byte_from_difference
from src.preprocess import preprocess_pretraining
from src.pythia import (
    PRETRAINING_CHECKPOINT_EXCLUSIONS,
    format_checkpoint_step,
)

COLORMAP_NAMES = ("Reds", "Oranges", "Greens", "Blues", "Purples", "Greys")
SERIES_COLORS = tuple(
    plt.get_cmap(colormap_name)(0.8) for colormap_name in COLORMAP_NAMES
)
LINE_STYLES = ("-", "--", "-.", ":", (0, (6, 2, 1, 2, 1, 2)))

LogpResults = dict[str, dict[int, np.ndarray]]
KlSeries = dict[str, tuple[np.ndarray, np.ndarray]]


def load_results(path: Path | str) -> LogpResults:
    """Load pickled pretraining results from `path`.

    The expected format is a dict mapping model sizes to a dict of
    checkpoint step -> logp arrays.
    """
    input_path = Path(path)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    with input_path.open("rb") as f:
        return pickle.load(f)


def compute_kl_by_model_size(
    logp_results: LogpResults,
    mean_text_bytes: float,
) -> KlSeries:
    """Compute KL estimates (bits/byte) per model size and checkpoint.

    Returns a dict mapping model size to `(steps, kl)`, where each KL value is
    attached to the earlier checkpoint in the consecutive checkpoint pair.
    """
    result: KlSeries = {}
    for model_size, checkpoint_logp in logp_results.items():
        checkpoint_steps = np.array(sorted(checkpoint_logp.keys()), dtype=int)
        if len(checkpoint_steps) < 2:
            continue

        logp_matrix = np.vstack(
            [
                np.asarray(checkpoint_logp[checkpoint_step], dtype=np.float64)
                for checkpoint_step in checkpoint_steps
            ]
        )
        diffs = np.diff(logp_matrix, axis=0)
        kl = kl_bits_per_byte_from_difference(
            diffs,
            mean_text_bytes=mean_text_bytes,
            axis=1,
        )
        result[model_size] = (checkpoint_steps[:-1], kl)
    return result


def format_step_ticks(ax, steps: np.ndarray, *, log_scaled: bool = False) -> None:
    """Set readable checkpoint tick labels."""
    tick_positions = np.log10(1 + steps) if log_scaled else steps
    ax.set_xticks(tick_positions)
    ax.set_xticklabels(
        [format_checkpoint_step(int(step)) for step in steps],
        rotation=-45,
        ha="left",
    )


def plot_series(
    ax,
    model_sizes: list[str],
    kl_by_model_size: KlSeries,
    *,
    warmup_step: int,
    during_warmup: bool,
) -> np.ndarray:
    """Plot either warmup or post-warmup KL series and return shown steps."""
    shown_steps: set[int] = set()

    for model_index, model_size in enumerate(model_sizes):
        if model_size not in kl_by_model_size:
            continue

        checkpoint_steps, kl = kl_by_model_size[model_size]
        mask = (
            checkpoint_steps < warmup_step
            if during_warmup
            else checkpoint_steps >= warmup_step
        )
        if not np.any(mask):
            continue

        xs = checkpoint_steps[mask]
        ys = kl[mask]
        plot_xs = np.log10(1 + xs) if during_warmup else xs
        color = SERIES_COLORS[model_index % len(SERIES_COLORS)]
        line_style = LINE_STYLES[model_index % len(LINE_STYLES)]

        ax.plot(
            plot_xs,
            ys,
            label=model_size.upper(),
            color=color,
            linestyle=line_style,
            linewidth=1,
        )
        shown_steps.update(int(step) for step in xs)

    return np.array(sorted(shown_steps), dtype=int)


def plot_kl(
    logp_results: LogpResults,
    output_path: Path | str,
    *,
    mean_text_bytes: float | None = None,
    warmup_step: int = 2000,
    remove_top_k: int = 300,
) -> None:
    """Render and save the KL plots to `output_path`."""
    processed_logp_results, info = preprocess_pretraining(
        logp_results,
        warmup_step=warmup_step,
        remove_top_k=remove_top_k,
        exclude_checkpoints=PRETRAINING_CHECKPOINT_EXCLUSIONS,
    )

    model_sizes = list(processed_logp_results.keys())
    if not model_sizes:
        raise ValueError("No model sizes left to plot after filtering.")

    figure, axes = plt.subplots(1, 2, figsize=(8, 3), dpi=300)
    label_font_size = 15
    tick_font_size = 12
    title_font_size = 18

    inferred_mean_text_bytes = float(info["mean_text_bytes"])
    kl_mean_text_bytes = (
        inferred_mean_text_bytes if mean_text_bytes is None else mean_text_bytes
    )
    kl_by_model_size = compute_kl_by_model_size(
        processed_logp_results,
        kl_mean_text_bytes,
    )

    warmup_axes = axes[0]
    warmup_steps = plot_series(
        warmup_axes,
        model_sizes,
        kl_by_model_size,
        warmup_step=warmup_step,
        during_warmup=True,
    )
    warmup_axes.legend(fontsize=tick_font_size)
    if len(warmup_steps) > 0:
        format_step_ticks(warmup_axes, warmup_steps, log_scaled=True)
    warmup_axes.set_xlabel("Step", fontsize=label_font_size)
    warmup_axes.set_ylabel("KL (bits/byte)", fontsize=label_font_size)
    warmup_axes.tick_params(axis="both", labelsize=tick_font_size)

    post_warmup_axes = axes[1]
    after_steps = plot_series(
        post_warmup_axes,
        model_sizes,
        kl_by_model_size,
        warmup_step=warmup_step,
        during_warmup=False,
    )
    post_warmup_axes.set_xlabel("Step", fontsize=label_font_size)
    if len(after_steps) > 0:
        max_step = int(after_steps.max())
        tick_start = 10000 if max_step >= 10000 else int(after_steps.min())
        x_tick_position = np.arange(tick_start, max_step + 1, 20000)
        if len(x_tick_position) == 0:
            x_tick_position = after_steps
        format_step_ticks(post_warmup_axes, x_tick_position)
    post_warmup_axes.set_yscale("log")
    post_warmup_axes.set_yticks([0.01, 0.1])
    post_warmup_axes.set_yticklabels(
        [r"$10^{-2}$", r"$10^{-1}$"],
        fontsize=tick_font_size,
    )
    post_warmup_axes.legend(fontsize=tick_font_size)
    post_warmup_axes.tick_params(axis="both", labelsize=tick_font_size)

    warmup_axes.set_title("During Warmup", fontsize=title_font_size)
    post_warmup_axes.set_title("After Warmup", fontsize=title_font_size)

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output, dpi=300, bbox_inches="tight")
    plt.close(figure)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Plot pretraining KL from pickled results."
    )
    parser.add_argument(
        "--input-path",
        "--input",
        "-i",
        dest="input_path",
        type=Path,
        default=Path("data/logp/pretraining_logp.pkl"),
        help="Path to input pickle file",
    )
    parser.add_argument(
        "--output-path",
        "--output",
        "-o",
        dest="output_path",
        type=Path,
        default=Path("output/fig4.png"),
        help="Path to output image file",
    )
    parser.add_argument(
        "--mean-text-bytes",
        "--mean-text-len",
        dest="mean_text_bytes",
        type=float,
        default=None,
        help=(
            "Override the mean text length used in KL normalization; "
            "inferred after preprocessing by default"
        ),
    )
    parser.add_argument(
        "--warmup-step",
        type=int,
        default=2000,
        help="First checkpoint step treated as post-warmup",
    )
    parser.add_argument(
        "--remove-top-k",
        type=int,
        default=300,
        help="Number of outlier texts removed during preprocessing",
    )
    parser.add_argument(
        "--model-sizes",
        default="410m,1b,1.4b,2.8b,6.9b",
        help="Comma-separated model sizes to plot, in display order",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    logp_results = load_results(args.input_path)

    model_sizes = [
        model_size.strip()
        for model_size in args.model_sizes.split(",")
        if model_size.strip()
    ]
    logp_results = {
        model_size: logp_results[model_size]
        for model_size in model_sizes
        if model_size in logp_results
    }

    plot_kl(
        logp_results,
        args.output_path,
        mean_text_bytes=args.mean_text_bytes,
        warmup_step=args.warmup_step,
        remove_top_k=args.remove_top_k,
    )


if __name__ == "__main__":
    main()
