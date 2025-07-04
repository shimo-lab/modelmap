import logging
import pickle as pkl
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import GroupKFold, KFold
from utils import ADDITIONAL_DEEPSEEK_MODELS, DATA_PATH, TASK_NAMES

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main(split):
    logger.info(f"split: {split}")
    assert split in ["groupkfold", "kfold"], \
        "split must be either 'groupkfold' or 'kfold'"

    with open(DATA_PATH, "rb") as f:
        modeldata = pkl.load(f)

    rows = []
    for model_dict in modeldata:
        model_name = model_dict["model_name"]

        isvalid = True
        for task_name in TASK_NAMES:
            if task_name == "mean_logp":
                key_name = task_name
            else:
                key_name = f"score_v1_{task_name}"
            value = model_dict[key_name]
            if value is None or np.isnan(value):
                isvalid = False
                if model_name not in ADDITIONAL_DEEPSEEK_MODELS:
                    logger.info(f"{key_name} is invalid in {model_name}")
                break
        if isvalid:
            row = {
                "model_name": model_name,
                "model_type": model_dict["model_type"],
            }
            for task_name in TASK_NAMES:
                if task_name == "mean_logp":
                    key_name = task_name
                else:
                    key_name = f"score_v1_{task_name}"
                value = model_dict[key_name]
                row[task_name] = value
            rows.append(row)
    logger.info(f"number of valid models: {len(rows)}")

    n_splits = 5
    logger.info(f"n_splits: {n_splits}")
    output_dir = Path("output/split_data") / split
    output_dir.mkdir(parents=True, exist_ok=True)
    for seed in range(5):
        logger.info(f"seed: {seed}")

        df = pd.DataFrame(rows)
        df["fold"] = -1

        if split == "groupkfold":
            kf = GroupKFold(n_splits=n_splits, shuffle=True, random_state=seed)
            for fold, (_, val_index) in enumerate(
                kf.split(df, groups=df["model_type"])
            ):
                df.loc[val_index, "fold"] = fold
        else:
            kf = KFold(n_splits=n_splits, shuffle=True, random_state=seed)
            for fold, (_, val_index) in enumerate(kf.split(df)):
                df.loc[val_index, "fold"] = fold

        # distribution of each fold
        logger.info("distribution of each fold")
        for fold in range(n_splits):
            fold_df = df[df["fold"] == fold]
            logger.info(f"fold {fold}: {len(fold_df)}")

        # save the split data
        df = df.sort_values(by=["model_name"])
        output_path = output_dir / f"seed{seed}.csv"
        df.to_csv(output_path, index=False)
        logger.info(f"saved to {output_path}")


if __name__ == "__main__":
    main(split="groupkfold")
    main(split="kfold")
