"""Shared metrics for log-likelihood vectors."""

from __future__ import annotations

import numpy as np


def kl_bits_per_byte_from_difference(
    logp_difference: np.ndarray,
    *,
    mean_text_bytes: float,
    axis: int | None = None,
) -> float | np.ndarray:
    """Estimate KL in bits/byte from centered log-likelihood differences."""
    if mean_text_bytes <= 0:
        raise ValueError("mean_text_bytes must be positive.")

    difference = np.asarray(logp_difference, dtype=np.float64)
    if not np.all(np.isfinite(difference)):
        raise ValueError("logp difference contains NaN or infinite values.")

    return np.var(difference, axis=axis, dtype=np.float64) / (
        2.0 * mean_text_bytes * np.log(2.0)
    )


def approximate_kl_bits_per_byte(
    logp_a: np.ndarray,
    logp_b: np.ndarray,
    *,
    mean_text_bytes: float,
) -> float:
    """Estimate KL in bits/byte from two aligned log-likelihood vectors."""
    a = np.asarray(logp_a, dtype=np.float64)
    b = np.asarray(logp_b, dtype=np.float64)
    if a.ndim != 1 or b.ndim != 1:
        raise ValueError(f"logp vectors must be 1D, got {a.shape} and {b.shape}.")
    if a.shape != b.shape:
        raise ValueError(
            f"logp vectors must have equal shapes, got {a.shape} and {b.shape}."
        )

    return float(
        kl_bits_per_byte_from_difference(
            a - b,
            mean_text_bytes=mean_text_bytes,
        )
    )
