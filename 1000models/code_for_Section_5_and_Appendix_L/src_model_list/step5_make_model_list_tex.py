import logging
import pickle as pkl
from pathlib import Path

import numpy as np
from utils import DATA_PATH

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main():
    model_name2entryid_path = Path("data/model_name2entryid.pkl")
    with open(model_name2entryid_path, "rb") as f:
        model_name2entryid = pkl.load(f)

    with open(DATA_PATH, "rb") as f:
        modeldata = pkl.load(f)

    latex_width = 7.5
    cols = [
        "ID",
        "Model Name",
        "Model Type",
        "Size",
        "Date",
        "DLs",
        r"$\bar{\ell}_i$",
        "Task",
    ]
    rows = []
    for idx, model_dict in enumerate(modeldata, start=1):
        model_name = model_dict["model_name"]

        if model_name in model_name2entryid:
            entryids = model_name2entryid[model_name]
            model_latex_name = (
                r"\parbox[t]{"
                + str(latex_width)
                + r"cm}{"
                + model_name.replace("_", r"\_")
                + r"~\cite{"
                + ",".join(entryids)
                + r"}}"
            )
        else:
            model_latex_name = (
                r"\parbox[t]{"
                + str(latex_width)
                + r"cm}{"
                + model_name.replace("_", r"\_")
                + r"}"
            )

        model_type = model_dict["model_type"].replace("_", r"\_")
        model_size = str(model_dict["model_size"]) + "B"
        created_at = model_dict["created_at"].split("T")[0]
        downloads = str(model_dict["downloads"])
        mean_logp = f"{model_dict['mean_logp']:.2f}"
        six_task_mean = model_dict["score_v1_6-taskmean"]
        if six_task_mean is None or np.isnan(six_task_mean):
            six_task_mean = "--"
        else:
            six_task_mean = f"{model_dict['score_v1_6-taskmean']:.2f}"

        col_vals = [
            str(idx),
            model_latex_name,
            model_type,
            model_size,
            created_at,
            downloads,
            mean_logp,
            six_task_mean,
        ]

        row = {}
        for col, val in zip(cols, col_vals):
            row[col] = val
        rows.append(row)

    # convert rows to latex table format
    col_names = " & ".join(cols)

    col_str = ""
    margin = 1
    col_margin = r"@{\hspace{" + str(margin) + r"em}}"
    for idx, col in enumerate(cols):
        if col in ["Model Name", "Model Type"]:
            col_str += "l"
        else:
            col_str += "r"
        if idx < len(cols) - 1:
            col_str += col_margin

    caption = "List of 1018 models. "
    col2desc = {
        "ID": "the alphabetical index",
        "Model Name": "the name of the model",
        "Model Type": "the classification defined in this paper",
        "Size": "the size of the model (B: billion)",
        "Date": "the date of model creation",
        r"$\bar{\ell}_i$": "the mean log-likelihood",
        "Task": "the mean of the 6 benchmark scores (i.e., 6-TaskMean)",
        "DLs": "the total number of downloads",
    }
    for col in cols:
        desc = col2desc[col]
        if col == r"$\bar{\ell}_i$":
            sub = col
        else:
            sub = f"``{col}''"
        caption += f"{sub} denotes {desc}; "
    caption = caption[:-2] + "."

    head = (
        r"""
{\scriptsize
\begin{longtable}{"""
        + col_str
        + r"""}
\caption{"""
        + caption
        + r"""}\\
"""
    )

    head += r"""
\toprule
"""

    head += (
        col_names
        + r"""\\
\midrule
\endfirsthead
    """
    )

    head += r"""
\toprule
"""

    head += (
        col_names
        + r"""\\
\midrule
\endhead
"""
    )

    for row in rows:
        row_str = " & ".join([row[col] for col in cols]) + r" \\"
        head += row_str + "\n"

    table = (
        head
        + r"""
\bottomrule
\label{tab:model_list}
\end{longtable}
}
"""
    )

    output_path = Path("data/model_list.tex")
    logger.info(f"Saving to {output_path}")
    with open(output_path, "w") as f:
        f.write(table)


if __name__ == "__main__":
    main()
