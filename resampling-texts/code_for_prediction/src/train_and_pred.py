import logging
import pickle as pkl
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr
from sklearn import linear_model

from utils import (DATA_PATH, KLS_WEIGHT_PATH, LSS_WEIGHT_PATH, TASK_NAMES,
                   UNIFORM_WEIGHT_PATH)

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def run(pred_dir, split, split_seed, n_resamples,
        sample_seed, unique_index, weights):
    with open(DATA_PATH, "rb") as f:
        modeldata = pkl.load(f)

    log_likelihood_vectors = np.array(
        [x['raw_log-likelihood-10k'] for x in modeldata])
    lower_p2 = np.quantile(log_likelihood_vectors, q=0.02)
    model_name2llv = {
        model_dict["model_name"]: np.maximum(
            model_dict["raw_log-likelihood-10k"], lower_p2
        )
        for model_dict in modeldata
    }

    task_alphas = [10**i for i in range(1, 10)]
    meanlogp_alphas = [10**i for i in range(-4, 5)]

    input_dir = Path("output/split_data") / split

    def get_tildeQ(L, unique_index, weights):
        L_d = L[:, unique_index]
        term_for_mean_L_d = weights**2
        numerator_bar_L_d = np.sum(
            L_d * term_for_mean_L_d[np.newaxis, :], axis=1
        )  # K-dim vector
        denominator_bar_L_d = np.sum(term_for_mean_L_d)  # scalar
        bar_L_d = numerator_bar_L_d / denominator_bar_L_d
        Q_d_centered_cols = L_d - bar_L_d[:, np.newaxis]
        tilde_Q_d = Q_d_centered_cols * weights[np.newaxis, :]
        tilde_Q_d = tilde_Q_d - np.mean(tilde_Q_d, axis=0)
        return tilde_Q_d

    input_path = input_dir / f"split_seed{split_seed}.csv"
    df = pd.read_csv(input_path)

    model_names = df["model_name"].values
    L = []
    for model_name in model_names:
        L.append(model_name2llv[model_name])
    L = np.array(L)
    Q = get_tildeQ(L, unique_index, weights)
    logger.info(f"Q shape: {Q.shape}")

    pred_df = None
    columns = ["model_name", "fold"] + TASK_NAMES
    for fold in range(5):
        train_ids = df["fold"] != fold
        test_ids = df["fold"] == fold

        logger.info(f"fold: {fold} "
                    f"train: {train_ids.sum()} "
                    f"test: {test_ids.sum()}")

        test_model_names = df["model_name"][test_ids].values
        fold_pred_df = pd.DataFrame(columns=columns)
        fold_pred_df["model_name"] = test_model_names
        fold_pred_df["fold"] = fold

        train_Q = Q[train_ids]
        test_Q = Q[test_ids]

        for task_name in TASK_NAMES:
            train_f = df[task_name][train_ids].values
            test_f = df[task_name][test_ids].values

            if task_name == "mean_logp":
                params = {"alphas": meanlogp_alphas, "cv": 5}
            else:
                params = {"alphas": task_alphas, "cv": 5}

            reg = linear_model.RidgeCV(**params)
            reg.fit(train_Q, train_f)

            # predict
            f_pred = reg.predict(test_Q)
            if task_name != "mean_logp":
                f_pred = np.clip(f_pred, 0, 100)
            fold_pred_df[task_name] = f_pred

            sr = spearmanr(test_f, f_pred)[0]
            pr = pearsonr(test_f, f_pred)[0]

            logger.info(f"{task_name}: spearman: {sr:.3f} pearson: {pr:.3f}")

        if pred_df is None:
            pred_df = fold_pred_df.copy()
        else:
            pred_df = pd.concat([pred_df, fold_pred_df], axis=0)

    # save prediction
    pred_df = pred_df.sort_values(by=["model_name"]).reset_index(drop=True)
    assert df["model_name"].equals(pred_df["model_name"])
    pred_path = (
        pred_dir / f"split_seed{split_seed}-"
        f"sample_seed{sample_seed}-"
        f"n_resamples{n_resamples}.csv"
    )
    pred_df.to_csv(pred_path, index=False)


def main(method, sample_seed, split_seed):
    assert method in ["lss", "uniform", "kls"]

    if method == "lss":
        WEIGHT_PATH = LSS_WEIGHT_PATH
    elif method == "uniform":
        WEIGHT_PATH = UNIFORM_WEIGHT_PATH
    elif method == "kls":
        WEIGHT_PATH = KLS_WEIGHT_PATH

    with open(WEIGHT_PATH, "rb") as f:
        idx_weight = pkl.load(f)

    split = "groupkfold"
    n_resamples_list = [10 * i for i in range(1, 10)]
    n_resamples_list += [100 * i for i in range(1, 10)]
    n_resamples_list += [1000 * i for i in range(1, 11)]

    for n_resamples in n_resamples_list:
        logger.info(
            f"split_seed: {split_seed} "
            f"sample_seed: {sample_seed} "
            f"n_resamples: {n_resamples}"
        )

        pred_dir = Path("output/train_and_pred") / split / method
        pred_dir.mkdir(parents=True, exist_ok=True)
        pred_path = (
            pred_dir / f"split_seed{split_seed}-"
            f"sample_seed{sample_seed}-"
            f"n_resamples{n_resamples}.csv"
        )
        if pred_path.exists():
            logger.info(f"pred_path exists: {pred_path}")
            continue

        unique_index = idx_weight[
            f"{sample_seed}"][f"{n_resamples}"]["unique_index"]
        weights = idx_weight[f"{sample_seed}"][f"{n_resamples}"]["weights"]

        run(
            pred_dir=pred_dir,
            split=split,
            split_seed=split_seed,
            n_resamples=n_resamples,
            sample_seed=sample_seed,
            unique_index=unique_index,
            weights=weights,
        )


if __name__ == "__main__":
    for method in ["lss", "uniform", "kls"]:
        for split_seed in range(5):
            main(method=method, sample_seed=42, split_seed=split_seed)
