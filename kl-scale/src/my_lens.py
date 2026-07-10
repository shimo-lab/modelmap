from __future__ import annotations

import warnings
from typing import Any

from torch import nn
from tuned_lens.model_surgery import (
    get_final_norm as _tuned_lens_get_final_norm,
)

_FINAL_NORM_ATTRIBUTE_CANDIDATES = (
    "final_layer_norm",
    "ln_f",
    "final_layernorm",
    "norm_f",
    "norm",
)

_MISSING = object()


def _get_attribute_path(obj: Any, path: str) -> Any:
    """Resolve a dotted attribute path such as ``model.norm``."""
    value = obj

    for name in path.split("."):
        value = getattr(value, name, _MISSING)

        if value is _MISSING:
            return _MISSING

    return value


def _get_explicit_final_norm(
    model: nn.Module,
    path: str,
) -> nn.Module:
    """Get a final norm from an explicitly specified attribute path."""
    final_norm = _get_attribute_path(model, path)

    if final_norm is _MISSING:
        raise AttributeError(
            f"Model {type(model).__name__} does not have the attribute path {path!r}."
        )

    if not isinstance(final_norm, nn.Module):
        raise TypeError(
            f"The object at {path!r} is not an nn.Module: {type(final_norm).__name__}."
        )

    return final_norm


def _find_final_norm_by_attribute(
    model: nn.Module,
) -> nn.Module:
    """Find a final norm using common attribute names.

    This function is used only when the installed tuned-lens version does not
    support the model architecture.
    """
    base_model = getattr(model, "base_model", None)

    roots: list[tuple[str, nn.Module]] = []

    if isinstance(base_model, nn.Module):
        roots.append(("base_model", base_model))

    if not isinstance(base_model, nn.Module) or base_model is not model:
        roots.append(("model", model))

    matches: dict[int, tuple[nn.Module, list[str]]] = {}

    for root_name, root in roots:
        for attribute_name in _FINAL_NORM_ATTRIBUTE_CANDIDATES:
            candidate = getattr(root, attribute_name, _MISSING)

            if candidate is _MISSING or candidate is None:
                continue

            if not isinstance(candidate, nn.Module):
                continue

            location = f"{root_name}.{attribute_name}"
            candidate_id = id(candidate)

            if candidate_id not in matches:
                matches[candidate_id] = (candidate, [location])
            else:
                matches[candidate_id][1].append(location)

    if not matches:
        searched = ", ".join(_FINAL_NORM_ATTRIBUTE_CANDIDATES)
        raise NotImplementedError(
            f"Could not determine the final norm for "
            f"{type(model).__name__}. "
            f"Searched these attributes: {searched}. "
            "Specify final_norm_path explicitly."
        )

    if len(matches) > 1:
        locations = [
            "/".join(candidate_locations) for _, candidate_locations in matches.values()
        ]

        raise RuntimeError(
            "Multiple possible final norm modules were found: "
            f"{locations}. "
            "Specify final_norm_path explicitly to avoid selecting "
            "the wrong module."
        )

    final_norm, locations = next(iter(matches.values()))

    warnings.warn(
        "The final norm was inferred heuristically from "
        f"{'/'.join(locations)} because the installed tuned-lens version "
        f"does not support {type(model).__name__}.",
        RuntimeWarning,
        stacklevel=2,
    )

    return final_norm


def get_final_norm(
    model: nn.Module,
    *,
    final_norm_path: str | None = None,
) -> nn.Module:
    """Return the final normalization module of a transformer model.

    Resolution order:

    1. An explicitly supplied ``final_norm_path``.
    2. The implementation provided by tuned-lens.
    3. A local fallback using common final-norm attribute names.

    Args:
        model:
            Transformer model whose final norm should be returned.
        final_norm_path:
            Optional dotted path relative to ``model``, such as
            ``"model.norm"`` or ``"transformer.ln_f"``.

    Raises:
        AttributeError:
            The explicitly supplied path does not exist.
        TypeError:
            The object at the explicitly supplied path is not an nn.Module.
        NotImplementedError:
            Neither tuned-lens nor the local fallback recognizes the model.
        RuntimeError:
            Multiple possible final norm modules were found.
    """
    if final_norm_path is not None:
        return _get_explicit_final_norm(model, final_norm_path)

    try:
        return _tuned_lens_get_final_norm(model)
    except NotImplementedError:
        pass
    except ValueError as exc:
        if str(exc) != "Model does not have a `base_model` attribute.":
            raise

    return _find_final_norm_by_attribute(model)
