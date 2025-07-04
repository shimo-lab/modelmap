import logging
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr
from utils import TASK_NAMES

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main(split, double_centered):

    assert split in ["groupkfold", "kfold"], \
        "split must be either 'groupkfold' or 'kfold'"
    assert double_centered in [True, False], \
        "double_centered must be either True or False"
    logger.info(f"split: {split}, double_centered: {double_centered}")
    task_name2scores = {
        task_name: {"pearson": [], "spearman": []} for task_name in TASK_NAMES
    }
    pred_dfs = []
    for seed in range(5):
        df_path = Path("output/split_data") / split / f"seed{seed}.csv"
        df = pd.read_csv(df_path)
        if double_centered:
            pred_df_path = (Path("output/train_and_pred") /
                            f"{split}_Q" / f"seed{seed}.csv")
        else:
            pred_df_path = (Path("output/train_and_pred") /
                            f"{split}_L" / f"seed{seed}.csv")
        pred_df = pd.read_csv(pred_df_path)
        pred_dfs.append(pred_df)

        assert df["model_name"].equals(pred_df["model_name"])

        for task_name in TASK_NAMES:
            true = df[task_name].values
            pred = pred_df[task_name].values
            assert len(true) == len(pred)

            pearson = pearsonr(true, pred)[0]
            task_name2scores[task_name]["pearson"].append(pearson)
            spearman = spearmanr(true, pred)[0]
            task_name2scores[task_name]["spearman"].append(spearman)

    if double_centered:
        output_dir = Path("output/eval_prediction") / f"{split}_Q"
    else:
        output_dir = Path("output/eval_prediction") / f"{split}_L"
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for metric in ["pearson", "spearman"]:
        row = {"metric": metric}
        for task_name in TASK_NAMES:
            scores = task_name2scores[task_name][metric]
            mean_score = np.mean(scores)
            std_score = np.std(scores)
            row[task_name] = f"{mean_score:.3f} ± {std_score:.3f}"
        rows.append(row)
    result_df = pd.DataFrame(rows)
    logger.info(result_df)
    result_df.to_csv(output_dir / f"{split}_5runs.csv", index=False)

    mean_pred_df = \
        pd.concat(pred_dfs).groupby("model_name").mean().reset_index()
    mean_pred_df = mean_pred_df.sort_values(by=["model_name"])
    mean_pred_df = mean_pred_df.drop(columns=["fold"])
    assert len(mean_pred_df) == len(df)
    assert mean_pred_df["model_name"].equals(df["model_name"])
    mean_pred_df.to_csv(output_dir / f"{split}_mean_pred.csv", index=False)

    df_path = Path("output/split_data") / split / "seed0.csv"
    df = pd.read_csv(df_path)
    rows = []
    for metric in ["pearson", "spearman"]:
        row = {"metric": metric}
        for task_name in TASK_NAMES:
            true = df[task_name].values
            pred = mean_pred_df[task_name].values
            assert len(true) == len(pred)
            if metric == "pearson":
                score = pearsonr(true, pred)[0]
            else:
                score = spearmanr(true, pred).correlation
            row[task_name] = f"{score:.3f}"
        rows.append(row)
    result_df = pd.DataFrame(rows)
    logger.info(result_df)
    result_df.to_csv(output_dir / f"{split}_5runs_mean.csv", index=False)


if __name__ == "__main__":
    for split in ["groupkfold", "kfold"]:
        for double_centered in [True, False]:
            main(split, double_centered)
