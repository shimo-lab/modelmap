import json
import os
import pickle
from argparse import ArgumentParser
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

try:
    from .utils import calc_layer_logp, load_texts
except ImportError:
    from utils import calc_layer_logp, load_texts


def parse_args():
    parser = ArgumentParser(description="Calculate layer-wise logp values.")
    parser.add_argument(
        "--model-list-path",
        type=Path,
        default=None,
        help=(
            "Path to a JSON list of model names. Defaults to "
            "<repo>/data/model_info/model_list.json."
        ),
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
            "Path to the output pickle. Defaults to <repo>/output/logp/layer_logp.pkl."
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
    parser.add_argument(
        "--final-norm-path",
        type=str,
        default=None,
        help=(
            "Optional dotted attribute path to the model final norm, "
            "for example model.norm."
        ),
    )
    parser.add_argument(
        "--max-models",
        type=int,
        default=50,
        help="Limit the number of models to process. Defaults to 50.",
    )
    parser.add_argument(
        "--max-texts",
        type=int,
        default=None,
        help="Limit the number of texts to process.",
    )
    return parser.parse_args()


def resolve_device(device_arg: str | None) -> str:
    if device_arg is not None:
        return device_arg
    if torch.cuda.is_available():
        return "cuda:0"
    return "cpu"


def resolve_torch_dtype(device: str):
    if device.startswith("cuda"):
        return torch.float16
    return torch.float32


def main():
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]

    model_list_path = args.model_list_path or (
        repo_root / "data" / "model_info" / "model_list.json"
    )
    texts_path = args.texts_path or (repo_root / "data" / "texts.json")
    output_path = args.output_path or (repo_root / "output" / "logp" / "layer_logp.pkl")
    cache_dir = args.cache_dir or os.getenv("HF_CACHE_DIR", None)
    device = resolve_device(args.device)
    torch_dtype = resolve_torch_dtype(device)
    if output_path.exists() and not args.overwrite:
        raise FileExistsError(
            f"Refusing to overwrite existing output: {output_path}. "
            "Pass --overwrite or choose another path under output/."
        )

    print(f"Running on device: {device}")
    if cache_dir is not None:
        print(f"Using Hugging Face cache directory: {cache_dir}")
    print(f"Loading model list from: {model_list_path}")
    print(f"Loading texts from: {texts_path}")

    with open(model_list_path, "r", encoding="utf-8") as f:
        target_models = json.load(f)
    if args.max_models is not None:
        target_models = target_models[: args.max_models]

    texts = load_texts(texts_path)
    if args.max_texts is not None:
        texts = texts[: args.max_texts]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    all_results = {}

    for model_name in target_models:
        try:
            print(f"Calculating {model_name}...")

            model = AutoModelForCausalLM.from_pretrained(
                model_name,
                cache_dir=cache_dir,
                torch_dtype=torch_dtype,
            )
            tokenizer = AutoTokenizer.from_pretrained(
                model_name,
                cache_dir=cache_dir,
            )
            tokenizer.pad_token = tokenizer.eos_token

            model.to(device)
            all_results[model_name] = calc_layer_logp(
                tokenizer,
                model,
                texts,
                final_norm_path=args.final_norm_path,
            )

            del model
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

            with open(output_path, "wb") as f:
                pickle.dump(all_results, f)
        except Exception as exc:
            print(f"Error at model {model_name}: {exc}")
            all_results[model_name] = None
            with open(output_path, "wb") as f:
                pickle.dump(all_results, f)

    with open(output_path, "wb") as f:
        pickle.dump(all_results, f)


if __name__ == "__main__":
    main()
