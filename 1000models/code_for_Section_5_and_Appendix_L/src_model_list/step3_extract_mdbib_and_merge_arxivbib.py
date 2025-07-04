import logging
import pickle as pkl
import re
from pathlib import Path

import bibtexparser
from tqdm import tqdm
from utils import DATA_PATH, SEP, model_name2file_name

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def extract_bibtex_entries(md_text):

    # extract code blocks from the Markdown text
    code_block_pattern = re.compile(
        r"```+([\w+-]*)\s([\s\S]*?)```", re.MULTILINE)
    code_blocks = []
    leftover_texts = []

    last_end = 0
    for match in code_block_pattern.finditer(md_text):
        start, end = match.span()
        # main text before the code block
        if start > last_end:
            leftover_texts.append(md_text[last_end:start])
        # code block
        code_blocks.append(match.group(2))
        last_end = end

    # the last part of the text after the last code block
    if last_end < len(md_text):
        leftover_texts.append(md_text[last_end:])

    # extract BibTeX entries from both code blocks and leftover texts
    all_bibtex_entries = []
    # 1) inside code blocks
    for block_text in code_blocks:
        all_bibtex_entries.extend(_parse_bibtex_text(block_text))
    # 2) outside code blocks
    for leftover in leftover_texts:
        all_bibtex_entries.extend(_parse_bibtex_text(leftover))

    # if @param or @return is included, remove it
    all_bibtex_entries = [
        e for e in all_bibtex_entries
        if ("@param" not in e and "@return" not in e)
    ]

    # if '@' is not included, remove it (this may be redundant)
    all_bibtex_entries = [e for e in all_bibtex_entries if "@" in e]

    return all_bibtex_entries


def _parse_bibtex_text(text):

    # find the first occurrence of @xxxx{...}
    has_bibtex_pattern = re.compile(r"@\w+\s*\{", re.IGNORECASE)

    # split on the next @xxxx{, but keep the @xxxx{ in the next entry
    bibtex_split_pattern = re.compile(r"(?=@\w+\s*\{)", re.IGNORECASE)

    # if there is no comma after "@type{key", add it
    fix_comma_pattern = re.compile(r"^(\s*@\w+\{[^,\n]+)\s*$", re.MULTILINE)

    # roughly check if there is a BibTeX entry
    if not has_bibtex_pattern.search(text):
        return []

    splitted = bibtex_split_pattern.split(text.strip())
    splitted = [s.strip() for s in splitted if s.strip()]

    results = []
    for entry_text in splitted:
        # if the first line does not start with "@xxxx{", skip it
        if not re.match(r"^@\w+\s*\{", entry_text):
            continue

        # fix missing commas: "@type{key" → "@type{key,"
        entry_text = fix_comma_pattern.sub(r"\1,", entry_text)

        # fix the number of '{' and '}' in the entire entry
        entry_text = _fix_unbalanced_braces_in_entry(entry_text)

        # if the last character is not '}',
        # remove everything after the last '}'
        if not entry_text.strip().endswith("}"):
            entry_text = "}".join(entry_text.split("}")[:-1]) + "}"

        results.append(entry_text)

    return results


def _fix_unbalanced_braces_in_entry(entry_text):
    # count the number of '{' and '}' in the entire entry and add '}' if needed
    # this implementation is not perfect, but it looks good enough in our case
    open_braces = entry_text.count("{")
    close_braces = entry_text.count("}")
    diff = open_braces - close_braces
    if diff > 0:
        entry_text += "}" * diff
    return entry_text


def main():
    arxiv_bibtex_dir = Path("data/arxiv_bibtex_from_tag")
    with open(arxiv_bibtex_dir / "model_name2arxiv_ids.pkl", "rb") as f:
        model_name2arxiv_ids = pkl.load(f)

    with open(DATA_PATH, "rb") as f:
        modeldata = pkl.load(f)
    model_names = [tmp["model_name"] for tmp in modeldata]

    md_dir = Path("data/model_cards")
    model_name2bibtex_list = {}
    for model_name in model_names:
        bibtex_list = []
        if model_name in model_name2arxiv_ids:
            arxiv_ids = model_name2arxiv_ids[model_name]
            for arxiv_id in arxiv_ids:
                bibtex_path = arxiv_bibtex_dir / f"{arxiv_id}.bib"
                if bibtex_path.exists():
                    with open(bibtex_path, "r") as f:
                        bibtex = f.read()
                    bibtex_list.append(bibtex)

        file_name = model_name2file_name(model_name)
        md_path = md_dir / f"{file_name}.md"
        if md_path.exists():
            with open(md_path, "r") as f:
                md_text = f.read()
            bibtex_list += extract_bibtex_entries(md_text)

        if model_name == "pankajmathur/orca_mini_v3_7b":
            # pankajmathur/orca_mini_v3_7b use Llama 2, but bibtex is llama,
            # so we need to change the bibtex
            bibtex_list_ = []
            for bibtex in bibtex_list:
                library = bibtexparser.parse_string(bibtex)
                entry = library.entries[0]
                title = entry.get("title").value
                if title == "LLaMA2: Open and Efficient Foundation Language Models":  # noqa
                    bibtex = r"""@misc{arxiv:2307.09288,
  title = {Llama 2: Open Foundation and Fine-Tuned Chat Models},
  author = {Hugo Touvron and Louis Martin and Kevin Stone and Peter Albert and Amjad Almahairi and Yasmine Babaei and Nikolay Bashlykov and Soumya Batra and Prajjwal Bhargava and Shruti Bhosale and Dan Bikel and Lukas Blecher and Cristian Canton Ferrer and Moya Chen and Guillem Cucurull and David Esiobu and Jude Fernandes and Jeremy Fu and Wenyin Fu and Brian Fuller and Cynthia Gao and Vedanuj Goswami and Naman Goyal and Anthony Hartshorn and Saghar Hosseini and Rui Hou and Hakan Inan and Marcin Kardas and Viktor Kerkez and Madian Khabsa and Isabel Kloumann and Artem Korenev and Punit Singh Koura and Marie-Anne Lachaux and Thibaut Lavril and Jenya Lee and Diana Liskovich and Yinghai Lu and Yuning Mao and Xavier Martinet and Todor Mihaylov and Pushkar Mishra and Igor Molybog and Yixin Nie and Andrew Poulton and Jeremy Reizenstein and Rashi Rungta and Kalyan Saladi and Alan Schelten and Ruan Silva and Eric Michael Smith and Ranjan Subramanian and Xiaoqing Ellen Tan and Binh Tang and Ross Taylor and Adina Williams and Jian Xiang Kuan and Puxin Xu and Zheng Yan and Iliyan Zarov and Yuchen Zhang and Angela Fan and Melanie Kambadur and Sharan Narang and Aurelien Rodriguez and Robert Stojnic and Sergey Edunov and Thomas Scialom},  # noqa
  year = {2023},
  eprint = {2307.09288},
  archivePrefix={arXiv},
  primaryClass = {cs.CL},
  url = {http://arxiv.org/abs/2307.09288v2},
}"""
                bibtex_list_.append(bibtex)
            bibtex_list = bibtex_list_

        if len(bibtex_list) > 0:
            model_name2bibtex_list[model_name] = bibtex_list

    bibtex_dir = Path("data/bibtex")
    # if bibtex_dir.exists(), remove all files
    if bibtex_dir.exists():
        for p in bibtex_dir.glob("*.bib"):
            p.unlink()
    bibtex_dir.mkdir(parents=True, exist_ok=True)
    for model_name, bibtex_list in tqdm(model_name2bibtex_list.items()):
        bibtex = SEP.join(bibtex_list)
        file_name = model_name2file_name(model_name)
        bibtex_path = bibtex_dir / f"{file_name}.bib"
        with open(bibtex_path, "w") as f:
            f.write(bibtex)


if __name__ == "__main__":
    main()
