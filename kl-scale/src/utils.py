"""Shared text-loading and log-likelihood utilities."""

import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Sequence

import numpy as np
import torch
from numpy.typing import NDArray
from tqdm import tqdm

try:
    from my_lens import get_final_norm
except ModuleNotFoundError as exc:
    if exc.name != "my_lens":
        raise
    from .my_lens import get_final_norm
from tuned_lens.model_surgery import get_unembedding_matrix


def load_texts(path: Path | str) -> list[str]:
    """Load evaluation texts from a JSON file."""
    path = Path(path)
    if path.suffix == ".json":
        with open(path, "r", encoding="utf-8") as f:
            texts = json.load(f)
    else:
        raise ValueError(f"Unsupported texts file extension: {path.suffix}")

    if not isinstance(texts, list) or not all(isinstance(text, str) for text in texts):
        raise ValueError("Texts file must contain a list of strings.")

    return texts


def _sequence_logp_from_logits(
    logits: torch.Tensor,
    input_ids: torch.Tensor,
) -> torch.Tensor:
    """Calculate sequence log-likelihood from causal LM logits.

    logits[:, i, :] predicts input_ids[:, i + 1].
    """
    target_ids = input_ids[:, 1:].to(logits.device)
    shifted_logits = logits[:, :-1, :]
    log_probs = shifted_logits.log_softmax(dim=-1)

    token_log_probs = log_probs.gather(
        dim=2,
        index=target_ids.unsqueeze(-1),
    ).squeeze(-1)

    return token_log_probs.sum(dim=1)


def calc_logp(
    tokenizer: Any,
    model: Any,
    texts: Sequence[str],
) -> NDArray[np.float32]:
    """Calculate one sequence-level log-likelihood for each text."""
    logp_values = []
    model.eval()

    for text in tqdm(texts, desc="Calculating logp"):
        inputs = tokenizer(
            text,
            return_tensors="pt",
        )

        input_ids = inputs["input_ids"].to(model.device)
        with torch.inference_mode():
            outputs = model(input_ids, output_hidden_states=False)
            text_logp = _sequence_logp_from_logits(outputs.logits, input_ids).item()

        logp_values.append(text_logp)

    # float32 is ample for model-produced log-likelihoods and keeps released
    # logp pickles below GitHub's per-file size limit.
    return np.asarray(logp_values, dtype=np.float32)


def calc_layer_logp(
    tokenizer: Any,
    model: Any,
    texts: Sequence[str],
    *,
    final_norm_path: str | None = None,
) -> dict[int, NDArray[np.float32]]:
    """Calculate logit-lens log-likelihood scores for each hidden state.

    Note:
        hidden_states[0] is usually the embedding output.
        hidden_states[i] for i > 0 corresponds to the output of
        transformer block i in most Hugging Face causal language models.

    The result maps each hidden-state index to its log-likelihood scores.
    """
    layer_logp_values = defaultdict(list)

    final_norm = get_final_norm(model, final_norm_path=final_norm_path)
    unembedding = get_unembedding_matrix(model)
    model.eval()

    for text in tqdm(texts, desc="Calculating layer logp"):
        inputs = tokenizer(
            text,
            return_tensors="pt",
        )

        input_ids = inputs["input_ids"].to(model.device)
        with torch.inference_mode():
            outputs = model(
                input_ids=input_ids,
                output_hidden_states=True,
                use_cache=False,
            )

            for layer, hidden_state in enumerate(outputs.hidden_states):
                if layer == len(outputs.hidden_states) - 1:
                    logits = outputs.logits
                else:
                    normalized_hidden_state = final_norm(hidden_state)
                    logits = unembedding(normalized_hidden_state)

                log_likelihood = _sequence_logp_from_logits(logits, input_ids).item()

                layer_logp_values[layer].append(log_likelihood)

    return {
        layer: np.asarray(values, dtype=np.float32)
        for layer, values in layer_logp_values.items()
    }
