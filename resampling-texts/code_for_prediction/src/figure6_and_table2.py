import logging
import pickle as pkl
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr
from tqdm import tqdm

from utils import (KLS_WEIGHT_PATH, LSS_WEIGHT_PATH, TASK_NAMES,
                   UNIFORM_WEIGHT_PATH)

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main(sample_seed=42):
    split = "groupkfold"
    input_dir = Path("output/split_data") / split
    methods = ["uniform", "kls", "lss"]
    method2results = dict()
    for method in methods:

        if method == "lss":
            WEIGHT_PATH = LSS_WEIGHT_PATH
        elif method == "uniform":
            WEIGHT_PATH = UNIFORM_WEIGHT_PATH
        elif method == "kls":
            WEIGHT_PATH = KLS_WEIGHT_PATH

        with open(WEIGHT_PATH, "rb") as f:
            idx_weight = pkl.load(f)

        n_resamples_list = [10 * i for i in range(1, 10)]
        n_resamples_list += [100 * i for i in range(1, 10)]
        n_resamples_list += [1000 * i for i in range(1, 11)]

        pred_dir = Path("output/train_and_pred") / split / method
        metric2task_name2results = {
            "pearson": {task_name: [] for task_name in TASK_NAMES},
            "spearman": {task_name: [] for task_name in TASK_NAMES},
        }
        for n_resamples in tqdm(n_resamples_list):
            unique_index = idx_weight[f"{sample_seed}"
                                      ][f"{n_resamples}"]["unique_index"]
            d = len(unique_index)
            task_name2scores = {
                task_name: {"pearson": [], "spearman": []
                            } for task_name in TASK_NAMES
            }
            for split_seed in range(5):
                input_path = input_dir / f"split_seed{split_seed}.csv"
                df = pd.read_csv(input_path)

                pred_path = (
                    pred_dir / f"split_seed{split_seed}-"
                    f"sample_seed{sample_seed}-"
                    f"n_resamples{n_resamples}.csv"
                )
                if not pred_path.exists():
                    continue

                pred_df = pd.read_csv(pred_path)

                assert df["model_name"].equals(pred_df["model_name"])

                for task_name in TASK_NAMES:
                    true = df[task_name].values
                    pred = pred_df[task_name].values
                    assert len(true) == len(pred)

                    pearson = pearsonr(true, pred)[0]
                    task_name2scores[task_name]["pearson"].append(pearson)
                    spearman = spearmanr(true, pred)[0]
                    task_name2scores[task_name]["spearman"].append(spearman)

            for metric in ["pearson", "spearman"]:
                for task_name in TASK_NAMES:
                    scores = task_name2scores[task_name][metric]
                    mean_score = np.mean(scores)
                    std_score = np.std(scores)
                    metric2task_name2results[metric][task_name].append(
                        {
                            "n_resamples": n_resamples,
                            "d": d,
                            "mean_score": mean_score,
                            "std_score": std_score,
                        }
                    )
        method2results[method] = metric2task_name2results

    for metric in ["pearson",]:
        method2color = {
            "uniform": "blue",
            "lss": "red",
            "kls": "green",
        }
        task_name2title = {
            "ARC": "ARC",
            "HellaSwag": "HellaSwag",
            "MMLU": "MMLU",
            "TruthfulQA": "TruthfulQA",
            "Winogrande": "Winogrande",
            "GSM8K": "GSM8K",
            "6-taskmean": "6-TaskMean",
            "mean_logp": "mean log-likelihood",
        }
        method2label = {
            "uniform": "Uniform",
            "lss": "LS",
            "kls": "KL",
        }
        method2marker = {
            "uniform": "o",
            "lss": "s",
            "kls": "^",
        }

        fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(22, 10))
        title_fs = 24
        label_fs = 24
        tick_fs = 24
        legend_fs = 20
        linewidth = 3
        markersize = 8
        for idx, task_name in enumerate(TASK_NAMES):
            ax = axes[idx % 2, (idx // 2) % 4]
            ax.set_title(task_name2title[task_name], fontsize=title_fs)

            for method in methods:
                metric2task_name2results = method2results[method]
                results = metric2task_name2results[metric][task_name]
                ds = [result["d"] for result in results]
                mean_score = [result["mean_score"] for result in results]
                std_score = [result["std_score"] for result in results]
                ax.plot(
                    ds,
                    mean_score,
                    label=method2label[method],
                    marker=method2marker[method],
                    markersize=markersize,
                    color=method2color[method],
                    linewidth=linewidth,
                )
                ax.fill_between(
                    ds,
                    np.array(mean_score) - np.array(std_score),
                    np.array(mean_score) + np.array(std_score),
                    alpha=0.2,
                    color=method2color[method],
                )

            ax.set_xlabel("Unique Samples: $d$", fontsize=label_fs)
            if metric == "pearson":
                ax.set_ylabel("Pearson's $r$", fontsize=label_fs)
            elif metric == "spearman":
                ax.set_ylabel("Spearman's $\\rho$", fontsize=label_fs)
            ax.set_xscale("log")
            ax.set_ylim(-0.1, 1.1)
            ax.grid(which="both", linestyle="--", linewidth=0.5)
            ax.tick_params(axis="both", which="major", labelsize=tick_fs)
            ax.legend(fontsize=legend_fs, loc="lower right")

        output_path = Path("output/images") / f"fig6_{metric}.pdf"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.subplots_adjust(
            left=0.06,
            right=0.99,
            bottom=0.09,
            top=0.95,
            wspace=0.35,
            hspace=0.4
        )
        fig.savefig(output_path)
        logger.info(f"Saved figure to {output_path}")

    # show n=10, 100, 1000, 10000 results in a table
    for metric in ["pearson",]:
        n_resamples_list = [10, 100, 1000, 10000]
        rows = []
        for n_resamples in n_resamples_list:
            # 100 -> $10^2$
            for method in methods:
                row = {'$n$': "$10^" + str(int(np.log10(n_resamples))) + "$"}
                for task_name in TASK_NAMES:
                    method2task_name2results = \
                        method2results[method][metric][task_name]
                    results = [
                        result for result in method2task_name2results
                        if result["n_resamples"] == n_resamples
                    ]
                    if len(results) == 0:
                        continue
                    result = results[0]
                    if "d" not in row:
                        row["$d$"] = result["d"]
                        row["Method"] = method2label[method]
                    row[task_name2title[task_name]] = \
                        f"{result['mean_score']:.3f} "\
                        r"$\pm$" + f" {result['std_score']:.3f}"
                rows.append(row)
        df = pd.DataFrame(rows)
        output_path = Path("output/summary") /\
            f"table2_{metric}.csv"
        logger.info(f"Saving summary to {output_path}")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)
        df.to_latex(
            output_path.with_suffix(".tex"),
            index=False,
            escape=False,
            float_format="%.3f",
            column_format=r"@{\hspace{1.2em}}r" * 2 + r"@{\hspace{1.2em}}l@{\hspace{1.2em}}" + r"r@{\hspace{1.2em}}" * (len(df.columns)-3)  # noqa
        )
        logger.info(f"Saved LaTeX table to {output_path.with_suffix('.tex')}")


if __name__ == "__main__":
    import fire
    fire.Fire(main)
