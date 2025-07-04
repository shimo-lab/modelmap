import logging
import pickle as pkl
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr
from sklearn import linear_model
from utils import DATA_PATH, TASK_NAMES

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def split_train_test(xs, ys, modelIds, train_modelId, test_modelId):
    train_modelId_set = set(train_modelId)
    test_modelId_set = set(test_modelId)
    train_index = [
        i for i, modelId in enumerate(modelIds) if modelId in train_modelId_set
    ]
    modelId2test_index = {
        modelId: i for i, modelId in enumerate(modelIds)
        if modelId in test_modelId_set
    }
    test_index = [modelId2test_index[modelId] for modelId in test_modelId]
    x_train = xs[train_index]
    y_train = ys[train_index]
    x_test = xs[test_index]
    y_test = ys[test_index]
    assert len(train_index) == x_train.shape[0] == y_train.shape[0]
    assert len(test_index) == x_test.shape[0] == y_test.shape[0]
    return x_train, y_train, x_test, y_test


def main(split, double_centered):

    assert split in ["groupkfold", "kfold"], \
        "split must be either 'groupkfold' or 'kfold'"
    assert double_centered in [True, False], \
        "double_centered must be either True or False"
    logger.info(f"split: {split}, double_centered: {double_centered}")

    with open(DATA_PATH, "rb") as f:
        modeldata = pkl.load(f)
    model_name2llv = {
        model_dict["model_name"]: model_dict["log-likelihood-10k"]
        for model_dict in modeldata
    }

    task_alphas = [10**i for i in range(1, 10)]
    meanlogp_alphas = [10**i for i in range(-4, 5)]

    input_dir = Path("output/split_data") / split
    if double_centered:
        pred_dir = Path("output/train_and_pred") / f"{split}_Q"
    else:
        pred_dir = Path("output/train_and_pred") / f"{split}_L"
    pred_dir.mkdir(parents=True, exist_ok=True)

    for seed in range(5):
        logger.info(f"seed: {seed}")
        input_path = input_dir / f"seed{seed}.csv"
        df = pd.read_csv(input_path)

        model_names = df["model_name"].values

        L = []
        for model_name in model_names:
            L.append(model_name2llv[model_name])
        L = np.array(L)

        if double_centered:
            L_mean = np.mean(L, axis=1)
            Xi = L - L_mean[:, np.newaxis]
            Xi_mean = np.mean(Xi, axis=0)
            Q = Xi - Xi_mean
        else:
            Q = L

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
                logger.info(f"best alpha: {reg.alpha_}")

                # predict
                f_pred = reg.predict(test_Q)
                if task_name != "mean_logp":
                    f_pred = np.clip(f_pred, 0, 100)
                fold_pred_df[task_name] = f_pred

                sr = spearmanr(test_f, f_pred)[0]
                pr = pearsonr(test_f, f_pred)[0]

                logger.info(
                    f"{task_name}: spearman: {sr:.3f} pearson: {pr:.3f}")

            if pred_df is None:
                pred_df = fold_pred_df.copy()
            else:
                pred_df = pd.concat([pred_df, fold_pred_df], axis=0)

        # save prediction
        pred_df = pred_df.sort_values(by=["model_name"]).reset_index(drop=True)
        assert df["model_name"].equals(pred_df["model_name"])
        pred_path = pred_dir / f"seed{seed}.csv"
        pred_df.to_csv(pred_path, index=False)


if __name__ == "__main__":
    for split in ["groupkfold", "kfold"]:
        for double_centered in [True, False]:
            main(split, double_centered)
