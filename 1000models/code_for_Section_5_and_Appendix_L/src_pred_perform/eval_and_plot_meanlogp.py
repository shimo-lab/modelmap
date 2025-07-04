import logging
from pathlib import Path

import matplotlib.pyplot as plt
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


def main():
    df_path = Path("output/split_data/groupkfold/seed0.csv")
    df = pd.read_csv(df_path)
    mean_logp = df["mean_logp"].values

    output_dir = Path("output/eval_and_plot_meanlogp")
    output_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    for metric in ["pearson", "spearman"]:
        row = {"metric": metric}
        for task_name in TASK_NAMES:
            true = df[task_name].values
            if metric == "pearson":
                score = pearsonr(true, mean_logp)[0]
            else:
                score = spearmanr(true, mean_logp)[0]
            row[task_name] = f"{score:.3f}"
        rows.append(row)
    result_df = pd.DataFrame(rows)
    logger.info(result_df)
    result_df.to_csv(output_dir / "meanlogp.csv", index=False)

    def prange(data, p1, p2):
        q1 = np.percentile(data, p1)
        q2 = np.percentile(data, p2)
        return q1, q2

    # all tasks
    fig, axes = plt.subplots(2, 4, figsize=(20, 8))

    # hyperparameter
    title_fs = 17
    label_fs = 16
    tick_fs = 12
    cbar_label_fs = 22
    cbar_tick_fs = 12
    s = 20
    linewidths = 0.2
    task_name2ticks = {
        "ARC": [20, 40, 60, 80],
        "TruthfulQA": [40, 60, 80],
        "Winogrande": [40, 60, 80],
        "HellaSwag": [20, 40, 60, 80, 100],
        "MMLU": [20, 40, 60, 80],
        "GSM8K": [0, 20, 40, 60, 80],
        "6-taskmean": [20, 40, 60, 80],
        "mean_logp": [-1400, -1100, -800, -500],
    }
    cmap = plt.get_cmap("gnuplot_r")

    for i, task_name in enumerate(TASK_NAMES):
        ax = axes[i % 2, (i // 2) % 4]

        # data
        true = df[task_name].values

        # plot
        xs, ys, cs = zip(*sorted(zip(mean_logp, true, mean_logp),
                                 key=lambda x: x[2]))
        vmin, vmax = prange(mean_logp, 10, 100)
        scatter = ax.scatter(
            xs,
            ys,
            c=cs,
            cmap=cmap,
            s=s,
            vmin=vmin,
            vmax=vmax,
            linewidths=linewidths,
            edgecolors="black",
            rasterized=True,
        )

        # identity line
        x_min = min(xs)
        x_max = max(xs)
        y_min = min(ys)
        y_max = max(ys)
        dx = 0.05 * (x_max - x_min)
        dy = 0.05 * (y_max - y_min)
        ax.plot(
            [x_min - dx, x_max + dx],
            [y_min - dy, y_max + dy],
            color="black",
            linestyle="--",
            alpha=0.5,
        )

        # label
        ax.set_xlabel("mean log-likelihood", fontsize=label_fs)
        pr = pearsonr(xs, ys)[0]
        sr = spearmanr(xs, ys).correlation
        if task_name == "6-taskmean":
            ax.set_ylabel("6-TaskMean score", fontsize=label_fs, labelpad=10)
            ax.set_title(
                "6-TaskMean: " + r"$r$" + f" = {pr:.3f}, "
                + r"$\rho$" + f" = {sr:.3f}",
                fontsize=title_fs,
                pad=10,
            )
        elif task_name == "mean_logp":
            ax.set_ylabel(
                "mean log-likelihood", fontsize=label_fs, labelpad=10)
            ax.set_title(
                "mean log-likelihood: "
                + r"$r$"
                + f" = {pr:.3f}, "
                + r"$\rho$"
                + f" = {sr:.3f}",
                fontsize=title_fs,
                pad=10,
            )
        else:
            ax.set_ylabel("benchmark score", fontsize=label_fs, labelpad=10)
            ax.set_title(
                f"{task_name}: "
                + r"$r$"
                + f" = {pr:.3f}, "
                + r"$\rho$"
                + f" = {sr:.3f}",
                fontsize=title_fs,
                pad=10,
            )
        ticks = task_name2ticks[task_name]
        ax.set_xticks(task_name2ticks["mean_logp"])
        ax.set_yticks(ticks)
        ax.tick_params(labelsize=tick_fs)

        # colorbar
        if i == 0:
            cb_ax = fig.add_axes([0.92, 0.065, 0.015, 0.885])
            cbar = fig.colorbar(scatter, cax=cb_ax)
            cbar.set_label(
                "mean log-likelihood",
                rotation=270,
                labelpad=40,
                fontsize=cbar_label_fs,
            )
            cbar.ax.tick_params(labelsize=cbar_tick_fs)

    # save
    fig.subplots_adjust(
        left=0.04, right=0.87, bottom=0.07, top=0.95, wspace=0.35, hspace=0.35
    )
    output_path = output_dir / "meanlogp_all_tasks.pdf"
    plt.savefig(output_path, dpi=150)
    logger.info(f"save to {output_path}")
    plt.close()


if __name__ == "__main__":
    main()
