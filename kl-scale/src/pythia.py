"""Shared Pythia model and checkpoint definitions."""

PYTHIA_MODEL_SIZES = ("410m", "1b", "1.4b", "2.8b", "6.9b")
PYTHIA_CHECKPOINT_STEPS = (
    0,
    1,
    2,
    4,
    8,
    16,
    32,
    64,
    128,
    256,
    512,
    *range(1_000, 143_000 + 1, 1_000),
)
PYTHIA_ANOMALOUS_SEED_MODELS = ("410m-seed3", "410m-seed4")
PRETRAINING_CHECKPOINT_EXCLUSIONS = frozenset({("1b", 116_000)})


def format_checkpoint_step(checkpoint_step: int) -> int | str:
    """Format a checkpoint step using a compact ``k`` suffix when possible."""
    if checkpoint_step >= 1_000 and checkpoint_step % 1_000 == 0:
        return f"{checkpoint_step // 1_000}k"
    return checkpoint_step
