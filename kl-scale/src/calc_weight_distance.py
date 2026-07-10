"""Compute local weight-space distances along Pythia training trajectories.

Starting at step 0, this script computes the squared Euclidean distance from
each Pythia checkpoint to the following ten saved checkpoints. The output is a
dictionary mapping each model size to a distance matrix. Distances are stored
in the upper triangle, while the diagonal, lower triangle, and uncomputed
entries remain zero.
"""

import argparse
import gc
import os
import pickle
from pathlib import Path

import numpy as np
import torch
from tqdm import tqdm
from transformers import AutoModelForCausalLM

try:
    from .pythia import PYTHIA_CHECKPOINT_STEPS, PYTHIA_MODEL_SIZES
except ImportError:
    from pythia import PYTHIA_CHECKPOINT_STEPS, PYTHIA_MODEL_SIZES

MODEL_SIZES = PYTHIA_MODEL_SIZES
CHECKPOINTS = PYTHIA_CHECKPOINT_STEPS


def parse_args():
    parser = argparse.ArgumentParser(
        description="Calculate squared distances between nearby Pythia checkpoints."
    )
    parser.add_argument(
        "--model-size",
        nargs="+",
        choices=MODEL_SIZES,
        default=list(MODEL_SIZES),
        help="Pythia model sizes to process (default: all).",
    )
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=None,
        help="Hugging Face cache directory. Defaults to HF_CACHE_DIR if set.",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=Path("output/weight_distance")
    )
    parser.add_argument(
        "--max-offset",
        type=int,
        default=10,
        help="Number of subsequent saved checkpoints compared with each t0.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Discard an existing compatible result instead of resuming it.",
    )
    return parser.parse_args()


def output_path(output_dir):
    return output_dir / "weight_distance.pkl"


def empty_output():
    return {}


def empty_distance_matrix():
    n_checkpoints = len(CHECKPOINTS)
    return np.zeros((n_checkpoints, n_checkpoints), dtype=np.float64)


def load_or_initialize_output(path):
    if not path.exists():
        return empty_output()

    with path.open("rb") as f:
        output = pickle.load(f)

    if not isinstance(output, dict):
        raise ValueError(
            f"{path} has an incompatible format. Use --overwrite to replace it."
        )
    unknown_model_sizes = set(output) - set(MODEL_SIZES)
    if unknown_model_sizes:
        raise ValueError(
            f"{path} contains unknown model sizes: {sorted(unknown_model_sizes)}."
        )
    for model_size, distances in output.items():
        validate_distance_matrix(distances, path, model_size)
    return output


def validate_distance_matrix(distances, path, model_size):
    expected_shape = (len(CHECKPOINTS), len(CHECKPOINTS))
    if not isinstance(distances, np.ndarray) or distances.shape != expected_shape:
        raise ValueError(
            f"{path} must contain a {expected_shape} NumPy array for {model_size}."
        )
    if not np.issubdtype(distances.dtype, np.number):
        raise ValueError(f"{path} contains a non-numeric array for {model_size}.")


def save_result(result, path):
    """Atomically replace a result file, preserving resumable progress."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = path.with_suffix(path.suffix + ".tmp")
    with temporary_path.open("wb") as f:
        pickle.dump(result, f, protocol=pickle.HIGHEST_PROTOCOL)
    os.replace(temporary_path, path)


def load_model(model_name, checkpoint, cache_dir, device):
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        revision=f"step{checkpoint}",
        cache_dir=cache_dir,
        torch_dtype=torch.float16,
    )
    model.requires_grad_(False)
    model.eval()
    return model.to(device)


@torch.inference_mode()
def squared_parameter_distance(model_a, model_b, chunk_size=1_000_000):
    """Return sum_i (theta_a[i] - theta_b[i])**2 in float64 accumulation."""
    parameters_a = dict(model_a.named_parameters())
    parameters_b = dict(model_b.named_parameters())
    if parameters_a.keys() != parameters_b.keys():
        raise ValueError("The checkpoints do not have the same parameter names.")

    total = 0.0
    for name, parameter_a in parameters_a.items():
        parameter_b = parameters_b[name]
        if parameter_a.shape != parameter_b.shape:
            raise ValueError(
                f"Parameter shape mismatch for {name}: "
                f"{tuple(parameter_a.shape)} != {tuple(parameter_b.shape)}"
            )

        flat_a = parameter_a.reshape(-1)
        flat_b = parameter_b.reshape(-1)
        for start in range(0, flat_a.numel(), chunk_size):
            difference = (
                flat_a[start : start + chunk_size].float()
                - flat_b[start : start + chunk_size].float()
            )
            total += difference.square().sum(dtype=torch.float64).item()

    return total


def calculate_model_distances(model_size, args, output, path):
    distances = output.get(model_size)
    if distances is None:
        distances = empty_distance_matrix()
        output[model_size] = distances
    else:
        validate_distance_matrix(distances, path, model_size)

    device = torch.device(f"cuda:{args.gpu}")
    model_name = f"EleutherAI/pythia-{model_size}"

    # Only starting checkpoints with a complete forward window are used.
    final_start_index = len(CHECKPOINTS) - args.max_offset
    for start_index in tqdm(
        range(final_start_index),
        desc=f"pythia-{model_size} starting checkpoints",
    ):
        target_indices = range(
            start_index + 1,
            start_index + args.max_offset + 1,
        )
        # A completed row is saved only after the full forward window has been
        # calculated. Checking its final entry also handles genuine zero
        # distances, such as the identical step-0 and step-1 checkpoints.
        if distances[start_index, start_index + args.max_offset] > 0:
            continue

        reference_model = load_model(
            model_name,
            CHECKPOINTS[start_index],
            args.cache_dir,
            device,
        )
        try:
            for target_index in target_indices:
                if distances[start_index, target_index] > 0:
                    continue

                target_model = load_model(
                    model_name,
                    CHECKPOINTS[target_index],
                    args.cache_dir,
                    device,
                )
                try:
                    distance = squared_parameter_distance(reference_model, target_model)
                    distances[start_index, target_index] = distance
                finally:
                    del target_model
                    gc.collect()
                    torch.cuda.empty_cache()

            # Save after every t0 so an interrupted multi-day run can resume.
            save_result(output, path)
        finally:
            del reference_model
            gc.collect()
            torch.cuda.empty_cache()

    save_result(output, path)


def main():
    args = parse_args()
    args.cache_dir = args.cache_dir or os.getenv("HF_CACHE_DIR", None)

    if args.max_offset < 1 or args.max_offset >= len(CHECKPOINTS):
        raise ValueError(f"--max-offset must be between 1 and {len(CHECKPOINTS) - 1}.")
    if not torch.cuda.is_available():
        raise RuntimeError("CUDA is required for the real distance calculation.")

    if args.cache_dir is not None:
        print(f"Using Hugging Face cache directory: {args.cache_dir}")

    path = output_path(args.output_dir)
    output = empty_output() if args.overwrite else load_or_initialize_output(path)

    for model_size in args.model_size:
        calculate_model_distances(model_size, args, output, path)


if __name__ == "__main__":
    main()
