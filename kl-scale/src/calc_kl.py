"""Calculate KL-divergence distributions used by Figure 3.

The input log-probability vectors contain one sequence log-likelihood per
evaluation text.  Following the approximation used in the paper, KL is
estimated from the variance of pairwise log-likelihood differences:

    KL(bits/byte) = Var(log p - log q) / (2 * mean_text_bytes * log(2))

The public ``calculate_all`` function loads the source data and returns the
distributions in memory. Figure 3 calls it directly on every run.
"""

from __future__ import annotations

import json
import pickle
import random
from collections import defaultdict
from itertools import combinations
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np

try:
    from .metrics import approximate_kl_bits_per_byte
    from .preprocess import preprocess_pretraining
    from .pythia import (
        PRETRAINING_CHECKPOINT_EXCLUSIONS,
        PYTHIA_ANOMALOUS_SEED_MODELS,
        PYTHIA_MODEL_SIZES,
    )
except ImportError:
    from metrics import approximate_kl_bits_per_byte
    from preprocess import preprocess_pretraining
    from pythia import (
        PRETRAINING_CHECKPOINT_EXCLUSIONS,
        PYTHIA_ANOMALOUS_SEED_MODELS,
        PYTHIA_MODEL_SIZES,
    )



def load_pickle(path: Path) -> Any:
    with path.open("rb") as f:
        return pickle.load(f)


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def load_texts(path: Path) -> list[str]:
    texts = load_json(path)
    if not isinstance(texts, list) or not all(isinstance(text, str) for text in texts):
        raise ValueError(f"{path} must contain a JSON list of strings.")
    return texts


def mean_text_bytes(texts: Sequence[str]) -> float:
    if not texts:
        raise ValueError("At least one evaluation text is required.")
    return float(np.mean([len(text.encode("utf-8")) for text in texts]))


def pairwise_kls(
    logp_by_name: Mapping[str, np.ndarray],
    names: Sequence[str],
    *,
    mean_text_bytes: float,
) -> np.ndarray:
    missing = [name for name in names if name not in logp_by_name]
    if missing:
        raise KeyError(f"Missing logp data for: {missing}")
    return np.asarray(
        [
            approximate_kl_bits_per_byte(
                logp_by_name[name_a],
                logp_by_name[name_b],
                mean_text_bytes=mean_text_bytes,
            )
            for name_a, name_b in combinations(names, 2)
        ],
        dtype=np.float64,
    )


def consecutive_checkpoint_kls(
    checkpoint_logp: Mapping[int, np.ndarray],
    *,
    mean_text_bytes: float,
    interval: int = 1_000,
) -> tuple[np.ndarray, np.ndarray]:
    """Return checkpoint steps and KLs for adjacent checkpoints at `interval`."""
    steps = sorted(checkpoint_logp)
    pairs = [
        (previous, current)
        for previous, current in zip(steps, steps[1:])
        if current - previous == interval
    ]
    if not pairs:
        raise ValueError(f"No consecutive checkpoints with interval={interval}.")

    end_steps = np.asarray([current for _, current in pairs], dtype=np.int64)
    kls = np.asarray(
        [
            approximate_kl_bits_per_byte(
                checkpoint_logp[previous],
                checkpoint_logp[current],
                mean_text_bytes=mean_text_bytes,
            )
            for previous, current in pairs
        ],
        dtype=np.float64,
    )
    return end_steps, kls


def calculate_pretraining_kls(
    raw_logp: Mapping[str, Mapping[int, np.ndarray]],
    *,
    first_window: int,
    last_window: int,
    texts_path: Path | str | None = None,
) -> dict[str, np.ndarray]:
    seed_names = sorted(name for name in raw_logp if name.startswith("410m-seed"))
    main_logp, main_info = preprocess_pretraining(
        raw_logp,
        texts_path=texts_path,
        exclude_model_sizes=seed_names,
        exclude_checkpoints=PRETRAINING_CHECKPOINT_EXCLUSIONS,
    )
    main_mean_text_bytes = float(main_info["mean_text_bytes"])

    interval_kls = {}
    for model_name in PYTHIA_MODEL_SIZES:
        end_steps, values = consecutive_checkpoint_kls(
            main_logp[model_name],
            mean_text_bytes=main_mean_text_bytes,
        )
        interval_kls[model_name] = values[end_steps > 2_000]

    if any(
        len(values) < max(first_window, last_window) for values in interval_kls.values()
    ):
        raise ValueError(
            "Not enough 1k checkpoint intervals for the requested windows."
        )

    first = np.concatenate([values[:first_window] for values in interval_kls.values()])
    last = np.concatenate([values[-last_window:] for values in interval_kls.values()])
    common_main_steps = set.intersection(
        *(set(main_logp[name]) for name in PYTHIA_MODEL_SIZES)
    )
    if not common_main_steps:
        raise ValueError("Main pretraining runs have no common checkpoint.")
    final_main_step = max(common_main_steps)
    main_final_logp = {
        name: main_logp[name][final_main_step] for name in PYTHIA_MODEL_SIZES
    }
    size = pairwise_kls(
        main_final_logp,
        PYTHIA_MODEL_SIZES,
        mean_text_bytes=main_mean_text_bytes,
    )

    seed_logp, seed_info = preprocess_pretraining(
        raw_logp,
        texts_path=texts_path,
        exclude_model_sizes=(
            *PYTHIA_MODEL_SIZES,
            *PYTHIA_ANOMALOUS_SEED_MODELS,
        ),
    )
    valid_seed_names = sorted(seed_logp)
    common_steps = set.intersection(
        *(set(seed_logp[name]) for name in valid_seed_names)
    )
    if not common_steps:
        raise ValueError("Seed runs have no common checkpoint.")
    final_step = max(common_steps)
    seed_final_logp = {name: seed_logp[name][final_step] for name in valid_seed_names}
    seed = pairwise_kls(
        seed_final_logp,
        valid_seed_names,
        mean_text_bytes=float(seed_info["mean_text_bytes"]),
    )

    return {
        "pretraining_first_1k": first,
        "pretraining_last_1k": last,
        "pretraining_seed": seed,
        "pretraining_size": size,
    }


def calculate_quantization_kls(
    full_precision_logp: np.ndarray,
    model_names: Sequence[str],
    quantized_logp: Mapping[str, np.ndarray],
    *,
    mean_text_bytes: float,
) -> np.ndarray:
    model_to_index = {name: index for index, name in enumerate(model_names)}
    unknown = sorted(set(quantized_logp) - set(model_to_index))
    if unknown:
        raise KeyError(f"Quantized models are absent from model_list.json: {unknown}")

    values = np.asarray(
        [
            approximate_kl_bits_per_byte(
                full_precision_logp[model_to_index[name]],
                quantized_logp[name],
                mean_text_bytes=mean_text_bytes,
            )
            for name in quantized_logp
            if quantized_logp[name] is not None
        ],
        dtype=np.float64,
    )
    return values


def normalize_parent(parent: Any) -> str | None:
    if isinstance(parent, str):
        return parent
    if isinstance(parent, list) and len(parent) == 1 and isinstance(parent[0], str):
        return parent[0]
    return None


def sample_distinct_pair(
    ids: Sequence[int],
    rng: random.Random,
) -> tuple[int, int]:
    if len(ids) < 2:
        raise ValueError("At least two model IDs are required to sample a pair.")
    id_a, id_b = rng.sample(list(ids), 2)
    return int(id_a), int(id_b)


def calculate_finetuning_kls(
    logp: np.ndarray,
    model_names: Sequence[str],
    model_to_type: Mapping[str, str],
    sibling_info: Mapping[str, Any],
    *,
    mean_text_bytes: float,
    random_seed: int,
    num_random_pairs: int | None,
) -> dict[str, np.ndarray]:
    if len(logp) != len(model_names):
        raise ValueError(
            f"Fine-tuning logp has {len(logp)} rows but model list has "
            f"{len(model_names)}."
        )

    model_to_id = {name: index for index, name in enumerate(model_names)}
    child_parent_by_type: dict[str, list[tuple[int, int]]] = defaultdict(list)

    for child_name, parent_value in sibling_info.items():
        parent_name = normalize_parent(parent_value)
        if child_name not in model_to_id or parent_name not in model_to_id:
            continue
        model_type = model_to_type.get(child_name)
        if model_type is None:
            continue
        child_parent_by_type[model_type].append(
            (model_to_id[child_name], model_to_id[parent_name])
        )

    child_parent_pairs = [
        pair for pairs in child_parent_by_type.values() for pair in pairs
    ]
    if not child_parent_pairs:
        raise ValueError("No valid child-parent pairs were found.")

    child_parent = np.asarray(
        [
            approximate_kl_bits_per_byte(
                logp[child],
                logp[parent],
                mean_text_bytes=mean_text_bytes,
            )
            for child, parent in child_parent_pairs
        ]
    )

    within_type_pairs = []
    global_candidate_ids = []
    rng = random.Random()
    for model_type, related_pairs in child_parent_by_type.items():
        candidates = list({model_id for pair in related_pairs for model_id in pair})
        if len(candidates) < 2:
            continue
        global_candidate_ids.extend(candidates)
        rng.seed(random_seed)
        within_type_pairs.extend(
            sample_distinct_pair(candidates, rng) for _ in related_pairs
        )

    pair_count = num_random_pairs or len(child_parent_pairs)
    global_candidates = list(set(global_candidate_ids))
    global_pairs = [
        sample_distinct_pair(global_candidates, rng) for _ in range(pair_count)
    ]

    def kls_for_pairs(pairs: Sequence[tuple[int, int]]) -> np.ndarray:
        return np.asarray(
            [
                approximate_kl_bits_per_byte(
                    logp[a],
                    logp[b],
                    mean_text_bytes=mean_text_bytes,
                )
                for a, b in pairs
            ],
            dtype=np.float64,
        )

    return {
        "finetuning_parent_child": child_parent,
        "finetuning_within_type": kls_for_pairs(within_type_pairs),
        "finetuning_random": kls_for_pairs(global_pairs),
    }


def calculate_layer_kls(
    layer_logp: Mapping[str, Mapping[int, np.ndarray] | None],
    *,
    mean_text_bytes: float,
) -> np.ndarray:
    values = []
    for model_name, logp_by_layer in layer_logp.items():
        if logp_by_layer is None:
            continue
        layers = sorted(logp_by_layer)
        for previous, current in zip(layers, layers[1:]):
            values.append(
                approximate_kl_bits_per_byte(
                    logp_by_layer[previous],
                    logp_by_layer[current],
                    mean_text_bytes=mean_text_bytes,
                )
            )
    if not values:
        raise ValueError("No adjacent layer pairs were found.")
    return np.asarray(values, dtype=np.float64)


def calculate_all(
    data_dir: Path | str,
    *,
    first_window: int = 50,
    last_window: int = 50,
    random_seed: int = 0,
    num_random_pairs: int | None = None,
) -> dict[str, np.ndarray]:
    """Load all source data and calculate the Figure 3 distributions."""
    data_dir = Path(data_dir)
    if first_window <= 0 or last_window <= 0:
        raise ValueError("first_window and last_window must be positive.")
    if num_random_pairs is not None and num_random_pairs <= 0:
        raise ValueError("num_random_pairs must be positive.")

    logp_dir = data_dir / "logp"
    model_info_dir = data_dir / "model_info"
    texts = load_texts(data_dir / "texts.json")
    evaluation_mean_text_bytes = mean_text_bytes(texts)

    model_names = load_json(model_info_dir / "model_list.json")
    full_precision_logp = np.asarray(load_pickle(logp_dir / "oyama2025_logp.pkl"))

    results = calculate_pretraining_kls(
        load_pickle(logp_dir / "pretraining_logp.pkl"),
        first_window=first_window,
        last_window=last_window,
        texts_path=data_dir / "texts.json",
    )
    results["quantization_8bit"] = calculate_quantization_kls(
        full_precision_logp,
        model_names,
        load_pickle(logp_dir / "8bit_quantization_logp.pkl"),
        mean_text_bytes=evaluation_mean_text_bytes,
    )
    results["quantization_4bit"] = calculate_quantization_kls(
        full_precision_logp,
        model_names,
        load_pickle(logp_dir / "4bit_quantization_logp.pkl"),
        mean_text_bytes=evaluation_mean_text_bytes,
    )
    results.update(
        calculate_finetuning_kls(
            full_precision_logp,
            model_names,
            load_json(model_info_dir / "modelname2type.json"),
            load_json(model_info_dir / "sibling_info.json"),
            mean_text_bytes=evaluation_mean_text_bytes,
            random_seed=random_seed,
            num_random_pairs=num_random_pairs,
        )
    )
    results["layer_adjacent"] = calculate_layer_kls(
        load_pickle(logp_dir / "layer_logp.pkl"),
        mean_text_bytes=evaluation_mean_text_bytes,
    )
    return results
