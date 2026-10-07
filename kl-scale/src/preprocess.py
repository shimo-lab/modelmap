"""Preprocess Pythia log-likelihood vectors for downstream analyses."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Hashable, Iterable, Mapping

import numpy as np

try:
    from .utils import load_texts
except ImportError:
    from utils import load_texts

ModelSize = Hashable
CheckpointStep = int
CheckpointKey = tuple[ModelSize, CheckpointStep]


def preprocess_pretraining(
    logp_results: Mapping[ModelSize, Mapping[CheckpointStep, np.ndarray]],
    *,
    texts_path: Path | str | None = None,
    warmup_step: int = 2000,
    clip_bottom_frac: float = 0.02,
    remove_top_k: int | None = None,
    remove_top_frac: float | None = 0.03,
    exclude_model_sizes: Iterable[ModelSize] = (),
    exclude_checkpoints: Iterable[CheckpointKey] = (),
    drop_outlier_texts: bool = True,
) -> tuple[dict[ModelSize, dict[CheckpointStep, np.ndarray]], dict[str, Any]]:
    """Filter and normalize pretraining log-likelihood vectors.

    The input maps each model size and checkpoint step to a log-likelihood
    vector. The procedure excludes configured outliers, clips values at a
    global lower quantile, scores texts by their largest post-warmup change,
    and removes the highest-scoring texts.
    """

    exclude_model_sizes = set(exclude_model_sizes)
    exclude_checkpoints = set(exclude_checkpoints)

    n_texts = None
    for model_size, checkpoint_logp in logp_results.items():
        for checkpoint_step, logp_vector in checkpoint_logp.items():
            if logp_vector is None:
                continue
            logp_vector = np.asarray(logp_vector)
            if logp_vector.ndim != 1:
                raise ValueError(
                    f"logp_results[{model_size}][{checkpoint_step}] must be "
                    "a 1D vector, "
                    f"got shape={logp_vector.shape}"
                )
            if n_texts is None:
                n_texts = len(logp_vector)
            elif len(logp_vector) != n_texts:
                raise ValueError(
                    "All logp vectors must have the same length. "
                    f"Expected {n_texts}, got {len(logp_vector)} at "
                    f"({model_size}, {checkpoint_step})"
                )

    if n_texts is None:
        raise ValueError("logp_results is empty.")

    values_for_clip = []

    for model_size, checkpoint_logp in logp_results.items():
        if model_size in exclude_model_sizes:
            continue

        for checkpoint_step, logp_vector in checkpoint_logp.items():
            if (model_size, checkpoint_step) in exclude_checkpoints:
                continue
            if logp_vector is None:
                continue
            values_for_clip.append(np.asarray(logp_vector, dtype=np.float64))

    if not values_for_clip:
        raise ValueError("No vectors left after excluding outlier models/checkpoints.")

    all_values = np.concatenate(values_for_clip)
    clip_threshold = np.nanquantile(all_values, clip_bottom_frac)

    clipped_logp_results: dict[ModelSize, dict[CheckpointStep, np.ndarray]] = {}

    for model_size, checkpoint_logp in logp_results.items():
        clipped_logp_results[model_size] = {}
        for checkpoint_step, logp_vector in checkpoint_logp.items():
            if logp_vector is None:
                continue
            logp_vector = np.asarray(logp_vector, dtype=np.float64)
            clipped_logp_results[model_size][checkpoint_step] = np.maximum(
                logp_vector,
                clip_threshold,
            )

    outlier_scores = np.full(n_texts, -np.inf, dtype=np.float64)

    for model_size, checkpoint_logp in clipped_logp_results.items():
        if model_size in exclude_model_sizes:
            continue

        checkpoint_steps = sorted(checkpoint_logp.keys())
        warmup_or_later_steps = [
            step for step in checkpoint_steps if step >= warmup_step
        ]

        for previous_step, next_step in zip(
            warmup_or_later_steps[:-1],
            warmup_or_later_steps[1:],
        ):
            if (model_size, previous_step) in exclude_checkpoints:
                continue
            if (model_size, next_step) in exclude_checkpoints:
                continue

            diff = np.abs(checkpoint_logp[next_step] - checkpoint_logp[previous_step])
            diff = np.nan_to_num(diff, nan=-np.inf)

            outlier_scores = np.maximum(outlier_scores, diff)

    if np.all(np.isneginf(outlier_scores)):
        raise ValueError(
            "No consecutive checkpoints found after warmup_step. "
            "Check step keys and warmup_step."
        )

    outlier_scores[np.isneginf(outlier_scores)] = np.nan

    if remove_top_k is None:
        if remove_top_frac is None:
            remove_top_k = 0
        else:
            remove_top_k = int(round(n_texts * remove_top_frac))

    remove_top_k = max(0, min(remove_top_k, n_texts))

    keep_text_mask = np.ones(n_texts, dtype=bool)

    if remove_top_k > 0:
        score_for_sort = np.nan_to_num(outlier_scores, nan=-np.inf)
        removed_indices = np.argpartition(score_for_sort, -remove_top_k)[-remove_top_k:]
        removed_indices = removed_indices[
            np.argsort(score_for_sort[removed_indices])[::-1]
        ]
        keep_text_mask[removed_indices] = False
    else:
        removed_indices = np.array([], dtype=int)

    processed_logp_results: dict[ModelSize, dict[CheckpointStep, np.ndarray]] = {}

    for model_size, checkpoint_logp in clipped_logp_results.items():
        if model_size in exclude_model_sizes:
            continue

        processed_logp_results[model_size] = {}

        for checkpoint_step, logp_vector in checkpoint_logp.items():
            if (model_size, checkpoint_step) in exclude_checkpoints:
                continue

            if drop_outlier_texts:
                processed_logp_vector = logp_vector[keep_text_mask]
            else:
                processed_logp_vector = logp_vector.copy()
                processed_logp_vector[~keep_text_mask] = np.nan

            processed_logp_results[model_size][checkpoint_step] = processed_logp_vector

    if texts_path is None:
        texts_path = Path(__file__).resolve().parents[1] / "data" / "texts.json"
    else:
        texts_path = Path(texts_path)
    texts = load_texts(texts_path)
    if len(texts) != n_texts:
        raise ValueError(
            f"{texts_path} contains {len(texts)} texts, but logp vectors "
            f"contain {n_texts} values."
        )
    mean_text_bytes = np.mean(
        [len(text.encode("utf-8")) for text in np.array(texts)[keep_text_mask]]
    )

    info = {
        "clip_threshold": clip_threshold,
        "clip_bottom_frac": clip_bottom_frac,
        "warmup_step": warmup_step,
        "outlier_scores": outlier_scores,
        "removed_indices": removed_indices,
        "keep_text_mask": keep_text_mask,
        "n_texts_original": n_texts,
        "n_texts_removed": int(len(removed_indices)),
        "n_texts_remaining": int(keep_text_mask.sum()),
        "mean_text_bytes": mean_text_bytes,
    }

    return processed_logp_results, info
