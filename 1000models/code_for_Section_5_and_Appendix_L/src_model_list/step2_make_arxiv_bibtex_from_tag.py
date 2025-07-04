import logging
import pickle as pkl
import time
from pathlib import Path

import arxiv
from tqdm import tqdm
from utils import DATA_PATH

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def bibtex_from_arxiv(arxiv_id):
    try:
        paper = next(arxiv.Client().results(arxiv.Search(id_list=[arxiv_id])))
        # sleep 0.5 sec
        time.sleep(0.5)
    except Exception as e:
        logger.error(f"Failed to fetch arXiv paper: {e}")
        return ""

    url = paper.entry_id
    title = paper.title
    authors = " and ".join([a.name for a in paper.authors])
    updated = paper.updated
    year = updated.strftime("%Y")
    primaryClass = paper.primary_category

    bibtex = (
        r"@misc{"
        + f"arxiv:{arxiv_id},\n"
        + f"  title = {{{title}}},\n"
        + f"  author = {{{authors}}},\n"
        + f"  year = {{{year}}},\n"
        + f"  eprint = {{{arxiv_id}}},\n"
        + r"  archivePrefix={arXiv},"
        + "\n"
        + f"  primaryClass = {{{primaryClass}}},\n"
        + f"  url = {{{url}}},\n"
        + r"}"
    )

    return bibtex


def main():
    with open(DATA_PATH, "rb") as f:
        modeldata = pkl.load(f)

    bibtex_dir = Path("data/arxiv_bibtex_from_tag")
    bibtex_dir.mkdir(parents=True, exist_ok=True)

    model_name2arxiv_ids = {}
    for model_dict in tqdm(modeldata):
        model_name = model_dict["model_name"]
        tags = model_dict["tags"]
        arxiv_ids = []
        for tag in tags:
            if tag.startswith("arxiv:"):
                arxiv_id = tag.split(":")[1]
                arxiv_ids.append(arxiv_id)

        if len(arxiv_ids) == 0:
            continue
        assert len(arxiv_ids) == len(set(arxiv_ids))
        model_name2arxiv_ids[model_name] = arxiv_ids

        for arxiv_id in arxiv_ids:
            bib_path = bibtex_dir / f"{arxiv_id}.bib"

            bibtex = bibtex_from_arxiv(arxiv_id)
            if bibtex:
                with open(bib_path, "w") as f:
                    f.write(bibtex)
                logger.info(f"Saving to {bib_path}")

    # add bibtex manually
    model_names_for_mistral7bv3 = [
        "mistralai/Mistral-7B-v0.3",
    ]

    model_names_for_codegemma = [
        "google/codegemma-2b",
        "google/codegemma-7b",
        "google/codegemma-7b-it",
    ]

    model_names_for_deepseekcoder = [
        "deepseek-ai/deepseek-coder-1.3b-base",
        "deepseek-ai/deepseek-coder-1.3b-instruct",
        "deepseek-ai/deepseek-coder-6.7b-base",
        "deepseek-ai/deepseek-coder-6.7b-instruct",
        "deepseek-ai/deepseek-coder-7b-base-v1.5",
        "deepseek-ai/deepseek-coder-7b-instruct-v1.5",
    ]

    model_names_for_deepseekllm = [
        "deepseek-ai/deepseek-llm-7b-base",
        "deepseek-ai/deepseek-llm-7b-chat",
    ]

    # Mistral 7B
    mistral7bv3_arxiv_id = "2310.06825"

    # CodeGemma: Open Code Models Based on Gemma
    codegemma_arxiv_id = "2406.11409"

    # DeepSeek-Coder: When the Large Language Model Meets Programming -- The Rise of Code Intelligence  # noqa: E501
    deepseekcoder_arxiv_id = "2401.14196"

    # DeepSeek LLM: Scaling Open-Source Language Models with Longtermism
    deepseekllm_arxiv_id = "2401.02954"

    for model_names, arxiv_id in zip(
        [
            model_names_for_mistral7bv3,
            model_names_for_codegemma,
            model_names_for_deepseekcoder,
            model_names_for_deepseekllm,
        ],
        [
            mistral7bv3_arxiv_id,
            codegemma_arxiv_id,
            deepseekcoder_arxiv_id,
            deepseekllm_arxiv_id,
        ],
    ):
        for model_name in model_names:
            if model_name in model_name2arxiv_ids:
                assert arxiv_id not in model_name2arxiv_ids[model_name]
                model_name2arxiv_ids[model_name].append(arxiv_id)
            else:
                model_name2arxiv_ids[model_name] = [arxiv_id]

        bib_path = bibtex_dir / f"{arxiv_id}.bib"
        bibtex = bibtex_from_arxiv(arxiv_id)
        if bibtex:
            with open(bib_path, "w") as f:
                f.write(bibtex)
            logger.info(f"Saving to {bib_path}")

    dict_path = bibtex_dir / "model_name2arxiv_ids.pkl"
    with open(dict_path, "wb") as f:
        pkl.dump(model_name2arxiv_ids, f)
    logger.info(f"Saving to {dict_path}")


if __name__ == "__main__":
    main()
