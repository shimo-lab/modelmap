"""Collect fine-tuning parent relationships from Hugging Face model metadata.

Fine-tuning log-likelihoods are already contained in ``oyama2025_logp.pkl``.
This script only identifies each model's base model; it does not calculate
new log-likelihood vectors.
"""

import argparse
import json
import os
from collections import Counter
from pathlib import Path
from typing import Any

from huggingface_hub import HfApi
from tqdm import tqdm

Parent = str | list[str] | None


def parse_args():
    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description="Collect base-model metadata for the fine-tuning analysis."
    )
    parser.add_argument(
        "--model-list-path",
        type=Path,
        default=repo_root / "data" / "model_info" / "model_list.json",
        help="JSON file containing model repository names.",
    )
    parser.add_argument(
        "--output-path",
        type=Path,
        default=repo_root / "output" / "sibling_info.json",
        help="Destination for child-to-parent metadata.",
    )
    parser.add_argument(
        "--error-path",
        type=Path,
        default=repo_root / "output" / "sibling_info_errors.json",
        help="Destination for models whose metadata could not be retrieved.",
    )
    parser.add_argument(
        "--token",
        default=os.getenv("HF_TOKEN"),
        help="Hugging Face token. Defaults to the HF_TOKEN environment variable.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="Timeout in seconds for each Hub request.",
    )
    parser.add_argument(
        "--max-models",
        type=int,
        default=None,
        help="Process only the first N models.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow existing output files to be replaced.",
    )
    return parser.parse_args()


def load_json(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def save_json(value, path: Path, *, overwrite: bool):
    if path.exists() and not overwrite:
        raise FileExistsError(
            f"Refusing to overwrite existing file: {path}. "
            "Pass --overwrite or choose another path."
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(value, f, ensure_ascii=False, indent=2)
        f.write("\n")


def validate_model_list(value: Any) -> list[str]:
    if not isinstance(value, list) or not all(
        isinstance(model_name, str) and model_name for model_name in value
    ):
        raise ValueError("Model list must be a JSON list of non-empty strings.")
    if len(value) != len(set(value)):
        raise ValueError("Model list contains duplicate repository names.")
    return value


def normalize_parent(value: Any) -> Parent:
    """Normalize Hub base-model metadata while preserving merge parents."""
    if value is None:
        return None
    if isinstance(value, str):
        return value or None
    if isinstance(value, (list, tuple)):
        parents = []
        for parent in value:
            if isinstance(parent, str) and parent:
                parents.append(parent)
            elif isinstance(parent, dict):
                repo_id = parent.get("id") or parent.get("name")
                if isinstance(repo_id, str) and repo_id:
                    parents.append(repo_id)
        if not parents:
            return None
        return parents[0] if len(parents) == 1 else parents
    return None


def parent_from_model_info(info) -> Parent:
    """Extract base-model metadata using public huggingface_hub attributes."""
    parent = normalize_parent(getattr(info, "base_models", None))
    if parent is not None:
        return parent

    card_data = getattr(info, "card_data", None)
    if card_data is None:
        return None
    if hasattr(card_data, "get"):
        return normalize_parent(card_data.get("base_model"))
    return normalize_parent(getattr(card_data, "base_model", None))


def collect_sibling_info(
    model_names: list[str],
    *,
    api: HfApi,
    timeout: float,
) -> tuple[dict[str, Parent], dict[str, str]]:
    sibling_info = {}
    errors = {}

    for model_name in tqdm(model_names, desc="Reading model metadata"):
        try:
            info = api.model_info(
                model_name,
                timeout=timeout,
                expand=["baseModels", "cardData"],
            )
            sibling_info[model_name] = parent_from_model_info(info)
        except Exception as exc:
            sibling_info[model_name] = None
            errors[model_name] = f"{type(exc).__name__}: {exc}"

    return sibling_info, errors


def validate_sibling_info(value: Any):
    if not isinstance(value, dict):
        raise ValueError("Sibling info must be a child-to-parent JSON object.")

    invalid = {}
    for child, parent in value.items():
        if not isinstance(child, str) or not child:
            invalid[str(child)] = "child name is not a non-empty string"
            continue
        normalized = normalize_parent(parent)
        if parent is not None and normalized is None:
            invalid[child] = f"unsupported parent value: {parent!r}"

    if invalid:
        examples = dict(list(invalid.items())[:5])
        raise ValueError(
            f"Invalid sibling metadata ({len(invalid)} entries): {examples}"
        )

    counts = Counter()
    for parent in value.values():
        normalized = normalize_parent(parent)
        if normalized is None:
            counts["no_parent"] += 1
        elif isinstance(normalized, list):
            counts["multiple_parents"] += 1
        else:
            counts["single_parent"] += 1

    return {
        "entries": len(value),
        "single_parent": counts["single_parent"],
        "multiple_parents": counts["multiple_parents"],
        "no_parent": counts["no_parent"],
    }


def main():
    args = parse_args()
    model_names = validate_model_list(load_json(args.model_list_path))

    if args.max_models is not None:
        if args.max_models <= 0:
            raise ValueError("--max-models must be positive.")
        model_names = model_names[: args.max_models]

    api = HfApi(token=args.token)
    sibling_info, errors = collect_sibling_info(
        model_names,
        api=api,
        timeout=args.timeout,
    )
    summary = validate_sibling_info(sibling_info)

    # Check both destinations before writing either file.
    for path in (args.output_path, args.error_path):
        if path.exists() and not args.overwrite:
            raise FileExistsError(
                f"Refusing to overwrite existing file: {path}. "
                "Pass --overwrite or choose another path."
            )

    save_json(sibling_info, args.output_path, overwrite=args.overwrite)
    save_json(errors, args.error_path, overwrite=args.overwrite)
    print(f"Saved sibling info to {args.output_path}: {summary}")
    print(f"Saved {len(errors)} retrieval errors to {args.error_path}")


if __name__ == "__main__":
    main()
