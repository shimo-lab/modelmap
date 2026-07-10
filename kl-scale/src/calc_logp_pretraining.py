import os
import pickle
from argparse import ArgumentParser
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

try:
    from .pythia import PYTHIA_CHECKPOINT_STEPS, PYTHIA_MODEL_SIZES
    from .utils import calc_logp, load_texts
except ImportError:
    from pythia import PYTHIA_CHECKPOINT_STEPS, PYTHIA_MODEL_SIZES
    from utils import calc_logp, load_texts


def parse_args():
    parser = ArgumentParser(
        description="Calculate logp values for Pythia pretraining checkpoints."
    )
    parser.add_argument(
        "--texts-path",
        type=Path,
        default=None,
        help="Path to the JSON texts list. Defaults to <repo>/data/texts.json.",
    )
    parser.add_argument(
        "--output-path",
        type=Path,
        default=None,
        help=(
            "Path to the output pickle. Defaults to "
            "<repo>/output/logp/pretraining_logp.pkl."
        ),
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow replacement of an existing output file.",
    )
    parser.add_argument(
        "--device",
        type=str,
        default=None,
        help=(
            "Torch device to run on, for example cuda:0 or cpu. "
            "Defaults to cuda:0 when available."
        ),
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=None,
        help="Hugging Face cache directory. Defaults to HF_CACHE_DIR if set.",
    )
    return parser.parse_args()


def resolve_device(device_arg: str | None) -> str:
    if device_arg is not None:
        return device_arg
    if torch.cuda.is_available():
        return "cuda:0"
    return "cpu"


def main():
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    texts_path = args.texts_path or (repo_root / "data" / "texts.json")
    output_path = args.output_path or (
        repo_root / "output" / "logp" / "pretraining_logp.pkl"
    )
    cache_dir = args.cache_dir or os.getenv("HF_CACHE_DIR", None)
    device = resolve_device(args.device)

    if cache_dir is not None:
        print(f"Using Hugging Face cache directory: {cache_dir}")
    print(f"Running on device: {device}")
    print(f"Loading texts from: {texts_path}")

    if output_path.exists() and not args.overwrite:
        raise FileExistsError(
            f"Refusing to overwrite existing output: {output_path}. "
            "Pass --overwrite or choose another path under output/."
        )

    target_model_sizes = (
        [PYTHIA_MODEL_SIZES[0]]
        + [f"410m-seed{seed_index}" for seed_index in range(1, 10)]
        + list(PYTHIA_MODEL_SIZES[1:])
    )
    target_checkpoint_steps = PYTHIA_CHECKPOINT_STEPS

    texts = load_texts(texts_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    logp_results = {}
    for model_size in target_model_sizes:
        logp_results[model_size] = {}
        tokenizer = AutoTokenizer.from_pretrained(f"EleutherAI/pythia-{model_size}")
        tokenizer.pad_token = tokenizer.eos_token

        for checkpoint_step in target_checkpoint_steps:
            try:
                model = AutoModelForCausalLM.from_pretrained(
                    f"EleutherAI/pythia-{model_size}",
                    revision=f"step{checkpoint_step}",
                    cache_dir=cache_dir,
                    torch_dtype=torch.float16
                    if device.startswith("cuda")
                    else torch.float32,
                )
                model.eval()
                model.to(device)

                logp_results[model_size][checkpoint_step] = calc_logp(
                    tokenizer,
                    model,
                    texts,
                )

                del model
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()

                with open(output_path, "wb") as f:
                    pickle.dump(logp_results, f)
            except Exception as exc:
                print(
                    f"Error loading model pythia-{model_size} "
                    f"step {checkpoint_step}: {exc}"
                )
                logp_results[model_size][checkpoint_step] = None

    with open(output_path, "wb") as f:
        pickle.dump(logp_results, f)


if __name__ == "__main__":
    main()
