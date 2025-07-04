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


def main(split, double_centered):

    assert split in ["groupkfold", "kfold"], \
        "split must be either 'groupkfold' or 'kfold'"
    assert double_centered in [True, False], \
        "double_centered must be either True or False"
    logger.info(f"split: {split}, double_centered: {double_centered}")

    if double_centered:
        pred_df_path = Path("output/eval_prediction"
                            ) / f"{split}_Q" / f"{split}_mean_pred.csv"
    else:
        pred_df_path = Path("output/eval_prediction"
                            ) / f"{split}_L" / f"{split}_mean_pred.csv"
    if not pred_df_path.exists():
        raise FileNotFoundError(
            f"{pred_df_path} does not exist. Run eval_prediction.py first."
        )
    pred_df = pd.read_csv(pred_df_path)

    df_path = Path("output/split_data") / split / "seed0.csv"
    df = pd.read_csv(df_path)

    def prange(data, p1, p2):
        q1 = np.percentile(data, p1)
        q2 = np.percentile(data, p2)
        return q1, q2

    if double_centered:
        output_dir = Path("output/plot_prediction") / f"{split}_Q"
    else:
        output_dir = Path("output/plot_prediction") / f"{split}_L"
    output_dir.mkdir(parents=True, exist_ok=True)

    # 6-taskmean
    fig, ax = plt.subplots(figsize=(8, 6))

    # hyperparameter
    label_fs = 28
    tick_fs = 20
    cbar_label_fs = 28
    cbar_tick_fs = 20
    s = 20
    linewidths = 0.2
    cmap = plt.get_cmap("gnuplot_r")

    # data
    task_name = "6-taskmean"
    true = df[task_name].values
    pred = pred_df[task_name].values
    mean_logp = df["mean_logp"].values
    assert len(true) == len(pred)

    # plot
    xs, ys, cs = zip(*sorted(zip(pred, true, mean_logp), key=lambda x: x[2]))
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

    # colorbar
    cb_ax = fig.add_axes([0.78, 0.15, 0.02, 0.84])
    cbar = fig.colorbar(scatter, cax=cb_ax)
    cbar.set_label(
        "mean log-likelihood",
        rotation=270,
        labelpad=40,
        fontsize=cbar_label_fs
    )
    cbar.ax.tick_params(labelsize=cbar_tick_fs)
    cbar_ticks = [-700, -650, -600, -550, -500]
    cbar.set_ticks(cbar_ticks)

    # identity line
    xy_min = min(min(xs), min(ys))
    xy_max = max(max(xs), max(ys))
    d = 0.05 * (xy_max - xy_min)
    ax.plot(
        [xy_min - d, xy_max + d],
        [xy_min - d, xy_max + d],
        color="black",
        linestyle="--",
        alpha=0.5,
    )
    ax.set_xlabel("predicted score", fontsize=label_fs)
    ax.set_ylabel("6-TaskMean score", fontsize=label_fs, labelpad=10)
    ax.set_aspect("equal", "box")
    ax.tick_params(labelsize=tick_fs)
    ticks = [20, 40, 60, 80]
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)

    # save
    fig.subplots_adjust(
        left=0.08, right=0.8, bottom=0.15, top=0.99, wspace=0.3, hspace=0.3
    )
    output_path = output_dir / f"{split}_6-taskmean.pdf"
    plt.savefig(output_path, dpi=150)
    logger.info(f"save to {output_path}")
    plt.close()

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
        pred = pred_df[task_name].values
        pr = pearsonr(pred, true)[0]
        sr = spearmanr(pred, true).correlation
        logger.info(
            f"{task_name}: Pearson r = {pr:.3f}, Spearman ρ = {sr:.3f}"
        )
        mean_logp = df["mean_logp"].values
        assert len(true) == len(pred)

        # plot
        xs, ys, cs = zip(
            *sorted(zip(pred, true, mean_logp), key=lambda x: x[2]))
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
        xy_min = min(min(xs), min(ys))
        xy_max = max(max(xs), max(ys))
        d = 0.05 * (xy_max - xy_min)
        ax.plot(
            [xy_min - d, xy_max + d],
            [xy_min - d, xy_max + d],
            color="black",
            linestyle="--",
            alpha=0.5,
        )

        # label
        ax.set_xlabel("predicted score", fontsize=label_fs)
        if task_name == "6-taskmean":
            ax.set_ylabel("6-TaskMean score", fontsize=label_fs, labelpad=10)
            ax.set_title(
                "6-TaskMean: " + r"$r$" + f" = {pr:.3f}, " +
                r"$\rho$" + f" = {sr:.3f}",
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
        ax.set_xticks(ticks)
        ax.set_yticks(ticks)
        ax.set_aspect("equal", "box")
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
        left=0.035, right=0.87, bottom=0.07, top=0.95, wspace=0.35, hspace=0.35
    )
    output_path = output_dir / f"{split}_all_tasks.pdf"
    plt.savefig(output_path, dpi=150)
    logger.info(f"save to {output_path}")
    plt.close()


if __name__ == "__main__":
    # for split in ["groupkfold", "kfold"]:
    #     for double_centered in [True, False]:
    #         main(split, double_centered)
    main(split="groupkfold", double_centered=True)
