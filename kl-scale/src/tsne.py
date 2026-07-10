"""Build double-centered logp matrices and t-SNE coordinates for Figures 1 and 2."""

import argparse
import json
import pickle
from pathlib import Path

import numpy as np
from sklearn.manifold import TSNE

try:
    from .preprocess import preprocess_pretraining
    from .pythia import (
        PRETRAINING_CHECKPOINT_EXCLUSIONS,
        PYTHIA_ANOMALOUS_SEED_MODELS,
    )
except ImportError:
    from preprocess import preprocess_pretraining
    from pythia import (
        PRETRAINING_CHECKPOINT_EXCLUSIONS,
        PYTHIA_ANOMALOUS_SEED_MODELS,
    )


PAPER_PERPLEXITY = {
    "pretraining": 30,
    "quantization": 30,
    "fine_tuning": 20,
    "layer": 30,
}

FIG1_EXCLUDE_MODEL_SIZES = PYTHIA_ANOMALOUS_SEED_MODELS
FIG1_EXCLUDE_CHECKPOINTS = PRETRAINING_CHECKPOINT_EXCLUSIONS
FIG1_MODEL_ORDER = [
    "410m-seed1",
    "410m-seed2",
    "410m-seed5",
    "410m-seed6",
    "410m-seed7",
    "410m-seed8",
    "410m-seed9",
    "410m",
    "1b",
    "1.4b",
    "2.8b",
    "6.9b",
]
FIG2_PANELS = ("quantization", "fine_tuning", "layer")

TSNE_FILENAMES = {
    "pretraining": "pretraining_tsne_2d.pkl",
    "quantization": "8bit_quantization_tsne.pkl",
    "fine_tuning": "ft_tsne.pkl",
    "layer": "layer_tsne.pkl",
}


def load_json(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def load_pickle(path: Path):
    with path.open("rb") as f:
        return pickle.load(f)


def save_pickle(value, path: Path, *, overwrite=False):
    if path.exists() and not overwrite:
        raise FileExistsError(
            f"Refusing to overwrite existing t-SNE output: {path}. "
            "Pass --overwrite or choose another output directory."
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as f:
        pickle.dump(value, f)


def validate_logp_matrix(matrix, label):
    matrix = np.asarray(matrix, dtype=np.float64)
    if matrix.ndim != 2:
        raise ValueError(f"{label} must be a 2D matrix, got shape={matrix.shape}.")
    if not np.isfinite(matrix).all():
        raise ValueError(f"{label} contains NaN or infinite values.")
    return matrix


def double_center_logp(matrix, mean_text_bytes):
    """Return the paper's double-centered, bits-per-byte-scaled Q matrix."""
    matrix = validate_logp_matrix(matrix, "L")
    q_matrix = (
        matrix
        - matrix.mean(axis=1, keepdims=True)
        - matrix.mean(axis=0, keepdims=True)
        + matrix.mean()
    )
    scale = np.sqrt(2 * matrix.shape[1] * float(mean_text_bytes) * np.log(2))
    return q_matrix / scale


def calculate_mean_text_bytes(texts_path: Path):
    texts = load_json(texts_path)
    if not texts:
        raise ValueError(f"No texts found in {texts_path}.")
    return float(np.mean([len(text.encode("utf-8")) for text in texts]))


def run_tsne(q_matrix, perplexity, random_state=42):
    if len(q_matrix) <= perplexity:
        raise ValueError(
            f"t-SNE requires n_samples > perplexity, got "
            f"{len(q_matrix)} samples and perplexity={perplexity}."
        )
    return TSNE(
        n_components=2,
        perplexity=perplexity,
        init="pca",
        learning_rate="auto",
        random_state=random_state,
    ).fit_transform(q_matrix)


def load_pretraining_results(
    path,
    *,
    texts_path=None,
    exclude_model_sizes=(),
    exclude_checkpoints=(),
):
    """Load and preprocess the checkpoint logp data used by Figure 1."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    return preprocess_pretraining(
        load_pickle(path),
        texts_path=texts_path,
        exclude_model_sizes=exclude_model_sizes,
        exclude_checkpoints=exclude_checkpoints,
    )


def build_pretraining_matrix(logp_results, mean_text_bytes, model_order):
    """Stack checkpoints in plotting order and return L, Q, and row slices."""
    missing_models = [name for name in model_order if name not in logp_results]
    if missing_models:
        raise ValueError(f"Missing expected pretraining models: {missing_models}")

    extra_models = [name for name in logp_results if name not in model_order]
    if extra_models:
        raise ValueError(f"Unexpected pretraining models: {extra_models}")

    rows = []
    model_slices = {}
    cursor = 0
    for model_name in model_order:
        checkpoint_logp = logp_results[model_name]
        model_rows = [
            np.asarray(checkpoint_logp[step], dtype=np.float64).ravel()
            for step in sorted(checkpoint_logp)
        ]
        rows.extend(model_rows)
        next_cursor = cursor + len(model_rows)
        model_slices[model_name] = slice(cursor, next_cursor)
        cursor = next_cursor

    matrix = validate_logp_matrix(np.vstack(rows), "pretraining L")
    q_matrix = double_center_logp(matrix, mean_text_bytes)
    return matrix, q_matrix, list(model_order), model_slices


def pretraining_cache_metadata(model_names, model_slices):
    return {
        "model_names": list(model_names),
        "model_lengths": {
            name: model_slices[name].stop - model_slices[name].start
            for name in model_names
        },
        "init": "pca",
    }


def load_pretraining_embedding(path, q_matrix, model_names, model_slices):
    """Read a compatible Figure 1 cache without modifying it."""
    path = Path(path)
    if not path.exists():
        return None

    cached = load_pickle(path)
    if not isinstance(cached, dict):
        return None

    embedding = np.asarray(cached.get("embedding"))
    metadata = pretraining_cache_metadata(model_names, model_slices)
    if (
        cached.get("metadata") == metadata
        and embedding.shape == (len(q_matrix), 2)
        and np.isfinite(embedding).all()
    ):
        return embedding
    return None


def prepare_fig1_inputs(
    input_path=Path("data/logp/pretraining_logp.pkl"),
    *,
    model_order,
    texts_path=None,
    exclude_model_sizes=(),
    exclude_checkpoints=(),
):
    logp_results, info = load_pretraining_results(
        input_path,
        texts_path=texts_path,
        exclude_model_sizes=exclude_model_sizes,
        exclude_checkpoints=exclude_checkpoints,
    )
    matrix, q_matrix, model_names, model_slices = build_pretraining_matrix(
        logp_results,
        info["mean_text_bytes"],
        model_order,
    )
    return {
        "logp_matrix": matrix,
        "q_matrix": q_matrix,
        "model_names": model_names,
        "model_slices": model_slices,
        "preprocess_info": info,
    }


def save_fig1_coordinates(prepared, output_path, *, overwrite=False):
    """Save a Figure 1 embedding using the existing cache-compatible format."""
    value = {
        "embedding": prepared["embedding"],
        "metadata": pretraining_cache_metadata(
            prepared["model_names"],
            prepared["model_slices"],
        ),
    }
    save_pickle(value, Path(output_path), overwrite=overwrite)


def model_row_lookup(model_list, oyama_logp):
    oyama_logp = validate_logp_matrix(oyama_logp, "oyama2025 logp")
    if len(model_list) != len(oyama_logp):
        raise ValueError(
            "model_list and oyama2025 logp have different row counts: "
            f"{len(model_list)} != {len(oyama_logp)}."
        )
    return {
        model_name: oyama_logp[index] for index, model_name in enumerate(model_list)
    }


def build_quantization_matrix(model_list, original_by_model, quantized_logp):
    model_names = [
        model_name for model_name in model_list if model_name in quantized_logp
    ]
    if not model_names:
        raise ValueError("No quantized models match model_list.")

    missing_original = [
        model_name for model_name in model_names if model_name not in original_by_model
    ]
    if missing_original:
        raise ValueError(f"Original logp is missing models: {missing_original}")

    original = np.vstack([original_by_model[name] for name in model_names])
    quantized = np.vstack([quantized_logp[name] for name in model_names])
    return np.vstack([original, quantized]), model_names


def quantization_coordinates(embedding, model_names):
    count = len(model_names)
    return {
        model_name: {
            "original": embedding[index],
            "quantized": embedding[index + count],
        }
        for index, model_name in enumerate(model_names)
    }


def single_parent_edges(sibling_info, available_models):
    """Select non-merge fine-tuning edges whose two endpoints have logp."""
    available_models = set(available_models)
    edges = []

    for child, raw_parent in sibling_info.items():
        if child not in available_models or raw_parent is None:
            continue

        if isinstance(raw_parent, list):
            if len(raw_parent) != 1:
                continue
            parent = raw_parent[0]
        else:
            parent = raw_parent

        if parent in available_models and parent != child:
            edges.append((parent, child))

    return edges


def build_fine_tuning_matrix(model_list, oyama_logp, sibling_info):
    original_by_model = model_row_lookup(model_list, oyama_logp)
    edges = single_parent_edges(sibling_info, original_by_model)
    if not edges:
        raise ValueError("No valid fine-tuning parent-child relationships were found.")

    selected_models = {model_name for edge in edges for model_name in edge}
    model_names = [
        model_name for model_name in model_list if model_name in selected_models
    ]
    matrix = np.vstack([original_by_model[name] for name in model_names])
    return matrix, model_names


def fine_tuning_coordinates(embedding, model_names):
    return {
        model_name: embedding[index] for index, model_name in enumerate(model_names)
    }


def build_layer_matrix(model_list, layer_logp):
    model_names = [model_name for model_name in model_list if model_name in layer_logp]
    if not model_names:
        raise ValueError("No layer models match model_list.")

    rows = []
    layer_keys = {}
    for model_name in model_names:
        model_layers = layer_logp[model_name]
        keys = sorted(model_layers)
        if not keys:
            raise ValueError(f"No layers found for {model_name}.")
        layer_keys[model_name] = keys
        rows.extend(model_layers[key] for key in keys)

    return np.vstack(rows), model_names, layer_keys


def layer_coordinates(embedding, model_names, layer_keys):
    coordinates = {}
    cursor = 0
    for model_name in model_names:
        count = len(layer_keys[model_name])
        coordinates[model_name] = embedding[cursor : cursor + count]
        cursor += count
    return coordinates


def prepare_fig2_inputs(data_dir=Path("data"), panels=None):
    """Build the double-centered Q matrices without running t-SNE."""
    data_dir = Path(data_dir)
    model_info_dir = data_dir / "model_info"
    logp_dir = data_dir / "logp"
    selected_panels = set(panels or FIG2_PANELS)

    unknown_panels = selected_panels - set(FIG2_PANELS)
    if unknown_panels:
        raise ValueError(f"Unknown panels: {sorted(unknown_panels)}")

    model_list = load_json(model_info_dir / "model_list.json")
    mean_text_bytes = calculate_mean_text_bytes(data_dir / "texts.json")
    oyama_logp = None
    if selected_panels & {"quantization", "fine_tuning"}:
        oyama_logp = load_pickle(logp_dir / "oyama2025_logp.pkl")

    prepared = {}
    if "quantization" in selected_panels:
        original_by_model = model_row_lookup(model_list, oyama_logp)
        quantized_logp = load_pickle(logp_dir / "8bit_quantization_logp.pkl")
        matrix, model_names = build_quantization_matrix(
            model_list, original_by_model, quantized_logp
        )
        prepared["quantization"] = {
            "q_matrix": double_center_logp(matrix, mean_text_bytes),
            "model_names": model_names,
        }

    if "fine_tuning" in selected_panels:
        sibling_info = load_json(model_info_dir / "sibling_info.json")
        matrix, model_names = build_fine_tuning_matrix(
            model_list, oyama_logp, sibling_info
        )
        prepared["fine_tuning"] = {
            "q_matrix": double_center_logp(matrix, mean_text_bytes),
            "model_names": model_names,
        }

    if "layer" in selected_panels:
        layer_logp = load_pickle(logp_dir / "layer_logp.pkl")
        matrix, model_names, layer_keys = build_layer_matrix(model_list, layer_logp)
        prepared["layer"] = {
            "q_matrix": double_center_logp(matrix, mean_text_bytes),
            "model_names": model_names,
            "layer_keys": layer_keys,
        }

    return prepared


def compute_fig2_coordinates(data_dir=Path("data"), random_state=42, panels=None):
    """Compute Figure 2 coordinates in memory without writing pickle files."""
    prepared = prepare_fig2_inputs(data_dir, panels)
    coordinates = {}

    if "quantization" in prepared:
        values = prepared["quantization"]
        embedding = run_tsne(
            values["q_matrix"], PAPER_PERPLEXITY["quantization"], random_state
        )
        coordinates["quantization"] = quantization_coordinates(
            embedding, values["model_names"]
        )

    if "fine_tuning" in prepared:
        values = prepared["fine_tuning"]
        embedding = run_tsne(
            values["q_matrix"], PAPER_PERPLEXITY["fine_tuning"], random_state
        )
        coordinates["fine_tuning"] = fine_tuning_coordinates(
            embedding, values["model_names"]
        )

    if "layer" in prepared:
        values = prepared["layer"]
        embedding = run_tsne(
            values["q_matrix"], PAPER_PERPLEXITY["layer"], random_state
        )
        coordinates["layer"] = layer_coordinates(
            embedding, values["model_names"], values["layer_keys"]
        )

    return coordinates


def compute_fig2_tsne(
    data_dir=Path("data"),
    output_dir=Path("output/tsne"),
    random_state=42,
    panels=None,
    overwrite=False,
):
    """Compute and save Figure 2 coordinates from the logp files."""
    output_dir = Path(output_dir)
    coordinates = compute_fig2_coordinates(data_dir, random_state, panels)

    outputs = {}
    if "quantization" in coordinates:
        output_path = output_dir / TSNE_FILENAMES["quantization"]
        save_pickle(coordinates["quantization"], output_path, overwrite=overwrite)
        outputs["quantization"] = output_path

    if "fine_tuning" in coordinates:
        output_path = output_dir / TSNE_FILENAMES["fine_tuning"]
        save_pickle(coordinates["fine_tuning"], output_path, overwrite=overwrite)
        outputs["fine_tuning"] = output_path

    if "layer" in coordinates:
        output_path = output_dir / TSNE_FILENAMES["layer"]
        save_pickle(coordinates["layer"], output_path, overwrite=overwrite)
        outputs["layer"] = output_path

    return outputs


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compute t-SNE coordinates for Figures 1 and 2."
    )
    parser.add_argument(
        "--figure",
        choices=("1", "2"),
        default="2",
        help="Figure whose t-SNE coordinates should be processed.",
    )
    parser.add_argument("--data-dir", type=Path, default=Path("data"))
    parser.add_argument(
        "--pretraining-path",
        type=Path,
        default=Path("data/logp/pretraining_logp.pkl"),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("output/tsne"),
        help="Directory for generated coordinates; data/tsne is not overwritten.",
    )
    parser.add_argument(
        "--panel",
        action="append",
        choices=FIG2_PANELS,
        help="Figure 2 panel. Repeat for multiple panels; defaults to all.",
    )
    parser.add_argument("--random-state", type=int, default=42)
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow replacement of files under --output-dir.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    if args.figure == "1":
        if args.panel:
            raise ValueError("--panel is only valid with --figure 2.")

        prepared = prepare_fig1_inputs(
            args.pretraining_path,
            model_order=FIG1_MODEL_ORDER,
            exclude_model_sizes=FIG1_EXCLUDE_MODEL_SIZES,
            exclude_checkpoints=FIG1_EXCLUDE_CHECKPOINTS,
        )
        prepared["embedding"] = run_tsne(
            prepared["q_matrix"],
            PAPER_PERPLEXITY["pretraining"],
            args.random_state,
        )
        output_path = args.output_dir / TSNE_FILENAMES["pretraining"]
        save_fig1_coordinates(prepared, output_path, overwrite=args.overwrite)
        print(
            f"Saved pretraining t-SNE coordinates to {output_path} "
            f"(perplexity={PAPER_PERPLEXITY['pretraining']})"
        )
        return

    outputs = compute_fig2_tsne(
        data_dir=args.data_dir,
        output_dir=args.output_dir,
        random_state=args.random_state,
        panels=args.panel,
        overwrite=args.overwrite,
    )
    for panel, path in outputs.items():
        print(
            f"Saved {panel} t-SNE coordinates to {path} "
            f"(perplexity={PAPER_PERPLEXITY[panel]})"
        )


if __name__ == "__main__":
    main()
