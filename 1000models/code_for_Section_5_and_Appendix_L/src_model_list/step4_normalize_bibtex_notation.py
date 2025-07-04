import logging
import pickle as pkl
import re
import string
from collections import defaultdict
from difflib import SequenceMatcher
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


class DisjointSet:
    # https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    def __init__(self, n: int) -> None:
        self.num = n
        self.rs = [1] * n
        self.ps = list(range(n))
        self.gs = [{i} for i in range(n)]

    def find(self, x: int) -> int:
        if x == self.ps[x]:
            return x
        else:
            self.ps[x] = self.find(self.ps[x])
            return self.ps[x]

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def unite(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rs[x] < self.rs[y]:
            x, y = y, x
        self.rs[x] += self.rs[y]
        self.ps[y] = x
        self.gs[x].update(self.gs[y])
        self.num -= 1

    def size(self, x: int) -> int:
        return self.rs[self.find(x)]

    def count(self) -> int:
        return self.num

    def group(self, x: int) -> set:
        return self.gs[self.find(x)]


def str_sim(s1: str, s2: str) -> float:
    if s1 == s2:
        return 1.0

    if len(s1) == 0 or len(s2) == 0:
        return 0.0

    # normalize each title
    s1_norm = normalize_title(s1)
    s2_norm = normalize_title(s2)

    # if the length of normalized string is 0, return 0
    if not s1_norm or not s2_norm:
        return 0.0

    # compute a similarity ratio between two sequences
    # https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher
    ratio = SequenceMatcher(None, s1_norm, s2_norm).ratio()
    return ratio


def normalize_title(s: str) -> str:
    # lowercase
    s = s.lower()

    # unify multiple spaces, including newlines and tabs, into one
    s = " ".join(s.split())

    # remove parentheses if their count is equal
    if s.count("{") == s.count("}"):
        s = s.replace("{", "").replace("}", "")

    # remove latex commands
    s = repr(s).replace(r"\textbf", "")

    # replace "\\" with "" (remove)
    s = s.replace("\\", "")

    # "unify multiple '-' into one '-'" (e.g. "a--b" => "a-b")
    s = re.sub(r"-+", "-", s)

    if s[0] == "'" and s[-1] == "'":
        s = s[1:-1]

    return s


def casefix(s1: str, s2: str) -> bool:
    s1 = normalize_title(s1)
    s2 = normalize_title(s2)
    s1, s2 = sorted([s1, s2])

    if (
        s1
        == "introducing mpt-7b: a new standard for open-source, commercially usable llms"  # noqa: E501
        and s2 == "introducing mpt-7b: a new standard for open-source, ly usable llms"  # noqa: E501
    ):
        # typo: "commercially" => "ly"
        return True

    if (
        s1 == "ultrafeedback: boosting language models with high-quality feedback"  # noqa: E501
        and s2 == "ultrafeedback: boosting language models with scaled ai feedback"  # noqa: E501
    ):
        # different version
        # v1: https://arxiv.org/abs/2310.01377v1
        # v2: https://arxiv.org/abs/2310.01377v2
        return True

    if (
        s1
        == "class meet spock: an education tutoring chatbot based on learning science principles"  # noqa: E501
        and s2
        == "class: a design framework for building intelligent tutoring systems based on learning science principles"  # noqa: E501
    ):
        # different version
        # v1: https://arxiv.org/abs/2305.13272v1
        # v2: https://arxiv.org/abs/2305.13272v2
        return True

    if (
        s1 == "stable lm 2 1.6 b technical report"
        and s2 == "stable lm 2 1.6b technical report"
    ):
        # different between "1.6 b" and "1.6b"
        return True

    if s1 == "stable lm 2 1.6b" and s2 == "stable lm 2 1.6b technical report":
        # with or without "technical report"
        return True

    if (
        s1
        == "mentallama: interpretable mental health analysis on social media with large language models"  # noqa: E501
        and s2
        == "mentalllama: interpretable mental health analysis on social media with large language models"  # noqa: E501
    ):
        # typo: "mental" => "menta"
        return True

    # other cases seems to be different

    return False


def fix_url_line(line: str) -> str:
    """
    This function detects the `url = { ... }` part in a line and
    replaces it with the first valid URL (https?://) found inside,
    even if there are multiple URLs or broken Markdown links
    (like `[https://...](`). The replacement is done
    in the format `url = { ... }`.
    """
    # capture the url = { ... } part in 3 groups
    # group(1): "url = {"
    # group(2): content
    # group(3): "}" (comma etc. can be processed separately)
    pattern = r"(url\s*=\s*\{)([^}]*)(\})"

    def replacer(match: re.Match) -> str:

        # content including broken Markdown
        content = match.group(2)

        # extract the first URL-like string from the content
        # considering the characters until a space, ) or ] or } appears
        found = re.search(r"https?://[^)\]\s}]+", content)
        if found:
            url = found.group(0)
            # make sure the format is "url = {URL}"
            return f"url = {{{url}}}"
        else:
            # do nothing if no URL is found
            return match.group(0)

    return re.sub(pattern, replacer, line)


def clean_bibtex(bibtex: str) -> str:
    lines = bibtex.split("\n")
    lines = [line.strip() for line in lines if line.strip()]
    # delete "% change this date"
    lines = [line.replace("% change this date", "") for line in lines]
    lines = [line.strip() for line in lines if line.strip()]

    # if the second to last line is "," and the last line has "}" twice, fix it
    if lines[-2][-1] == "," and lines[-1] == r"}}":
        lines[-2] = lines[-2][:-1] + r"},"
        lines[-1] = r"}"

    # if the last 3 lines are ",", the second to last line is "}",
    # and the last line is "}", fix it
    if (
        len(lines) >= 3
        and lines[-3][-1] == ","
        and lines[-2] == r"}"
        and lines[-1] == r"}"
    ):
        lines[-3] = lines[-3][:-1] + r"},"
        lines[-2] = r"}"
        lines[-1] = ""

    bibtex = "\n".join([line for line in lines if line.strip()])

    # replace https://https:// with https://
    bibtex = re.sub(r"https://https://", "https://", bibtex)
    # replace howpublished[whitespace] = [whitespace] {\url{...}}
    # with url = {...}
    bibtex = re.sub(
        r"howpublished\s*=\s*\{\\url\{(.+?)\}\}", r"url = {\1}", bibtex)
    # replace howpublished[whitespace]=[whitespace]"\url{...}" with url = {...}
    bibtex = re.sub(
        r"howpublished\s*=\s*\"\\url\{(.+?)\}\"", r"url = {\1}", bibtex)
    # remove howpublished={Software} if it exists
    bibtex = re.sub(r"howpublished={Software}", "", bibtex)
    assert r"howpublished" not in bibtex, print(bibtex)

    # fix url = {[https://...](https://...)} to url = {https://...}
    bibtex = fix_url_line(bibtex)

    library = bibtexparser.parse_string(bibtex)
    url = library.entries[0].get("url")
    if url is not None:
        url = url.value
        if url == "":
            # if url contatins nothing, remove it
            library.entries[0].pop("url")
        # if url does not start with http or https,
        # add https:// on case-by-case basis
        elif r"https://" not in url and r"http://" not in url:
            if url[:3] == "www":
                if url == "www.mosaicml.com/blog/mpt-30b":
                    new_url = "https://www.databricks.com/blog/mpt-30b"
                elif url == "www.mosaicml.com/blog/mpt-7b":
                    new_url = "https://www.databricks.com/blog/mpt-7b"
                else:
                    new_url = f"https://{url}"
                library.entries[0]["url"] = new_url
            elif url == "openaccess-ai-collective/jackalope-7b":
                url = r"https://huggingface.co/openaccess-ai-collective/jackalope-7b"  # noqa: E501
                library.entries[0]["url"] = url
            else:
                raise NotImplementedError(f"url: {url}")

    # if note contains url
    if "note" in library.entries[0]:
        note = library.entries[0].get("note")
        if note:
            note = note.value
            if "http" in note:
                if r"\url" in note and note[0] == "{" and note[-1] == "}":
                    note_url = note.replace(r"\url{", "").replace("}", "")
                else:
                    note_url = note
                url = library.entries[0].get("url")
                # if url is None, add url
                if url is None:
                    library.entries[0]["url"] = note_url
                    library.entries[0].pop("note")
                # if url is not None, check if it is same as note_url
                # if note_url is not in url, add note_url as note
                else:
                    url = url.value
                    assert len(url) > 0
                    if url != note_url:
                        library.entries[0]["note"] = note_url

    # remove urldate if it exists
    if "urldate" in library.entries[0]:
        library.entries[0].pop("urldate")
    # remove empty fields
    keys = []
    for k, v in library.entries[0].items():
        if v == "":
            keys.append(k)
    for key in keys:
        library.entries[0].pop(key)

    # convert software, techreport, online to misc
    entry_type = library.entries[0].entry_type
    if entry_type in ["software", "techreport", "online"]:
        library.entries[0].entry_type = "misc"

    # convert article to misc if journal is not in
    if entry_type == "article":
        if "journal" not in library.entries[0]:
            library.entries[0].entry_type = "misc"

    # case-by-case for some bibtex based on their title
    title = library.entries[0].get("title").value
    if title == "Qwen2 Technical Report":
        # citation of Qwen2 on huggingface does not have author, so add it
        # e.g. https://huggingface.co/Qwen/Qwen2-7B
        bibtex = r"""@misc{qwen2,
      title={Qwen2 Technical Report},
      author={An Yang and Baosong Yang and Binyuan Hui and Bo Zheng and Bowen Yu and Chang Zhou and Chengpeng Li and Chengyuan Li and Dayiheng Liu and Fei Huang and Guanting Dong and Haoran Wei and Huan Lin and Jialong Tang and Jialin Wang and Jian Yang and Jianhong Tu and Jianwei Zhang and Jianxin Ma and Jianxin Yang and Jin Xu and Jingren Zhou and Jinze Bai and Jinzheng He and Junyang Lin and Kai Dang and Keming Lu and Keqin Chen and Kexin Yang and Mei Li and Mingfeng Xue and Na Ni and Pei Zhang and Peng Wang and Ru Peng and Rui Men and Ruize Gao and Runji Lin and Shijie Wang and Shuai Bai and Sinan Tan and Tianhang Zhu and Tianhao Li and Tianyu Liu and Wenbin Ge and Xiaodong Deng and Xiaohuan Zhou and Xingzhang Ren and Xinyu Zhang and Xipin Wei and Xuancheng Ren and Xuejing Liu and Yang Fan and Yang Yao and Yichang Zhang and Yu Wan and Yunfei Chu and Yuqiong Liu and Zeyu Cui and Zhenru Zhang and Zhifang Guo and Zhihao Fan},  # noqa: E501
      year={2024},
      eprint={2407.10671},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2407.10671},
}"""
    else:
        authors = library.entries[0].get("author")
        assert authors is not None
        authors = authors.value
        if " and " not in authors and " and\n" not in authors:
            # only one author or comma separated authors
            if authors == "L, Jungwon, A, Seungjun":
                authors = "Jungwon Lee and Seungjun Ahn"
            elif authors in ("L, Junbum", " {L. Junbum} ", " {Lee Junbum} "):
                authors = "Junbum Lee"
            elif authors == "Tow, Jonathan":
                authors = "Jonathan Tow"
            elif authors == "Dao, Tri":
                authors = "Tri Dao"
            elif authors == "Wang, Ben":
                authors = "Ben Wang"
            else:
                author_list = authors.split(",")
                new_author_list = []
                for author in author_list:
                    author = author.strip()
                    # if author doen't have alphabet, remove. e.g. ":".
                    if not any(c.isalpha() for c in author):
                        continue
                    new_author_list.append(author)
                authors = " and ".join(new_author_list)
        else:
            # the original bibtex contains redundant "," after "Winnie"
            if (
                authors
                == "Ethayarajh, Kawin and Xu, Winnie, and Jurafsky, Dan and Kiela, Douwe"  # noqa: E501
            ):
                authors = (
                    "Kawin Ethayarajh and Winnie Xu and Dan Jurafsky and Douwe Kiela"  # noqa: E501
                )
            # coexistence of "and" and "," in the author
            elif authors == "Duy Quang Do, Hoang Le and Duc Thang Nguyen":
                authors = "Duy Quang Do and Hoang Le and Duc Thang Nguyen"
            elif "," not in authors:
                author_list = authors.split(" and ")
                new_author_list = []
                for author in author_list:
                    author = author.strip()
                    # if author doen't have alphabet, remove. e.g. ":".
                    if not any(c.isalpha() for c in author):
                        continue
                    new_author_list.append(author)
                authors = " and ".join(new_author_list)

        library.entries[0]["author"] = authors

        # enclose team names with {}
        # these team names are selected manually, so some may be missing
        teams = [
            "DeciAI Research Team",
            "MosaicML NLP Team",
            "Stability AI Language Team",
            "YuLan-Team",
            "Gemini Team",
            "Nexusflow.ai team",
            "Griffin Team",
            "Xwin-LM Team",
            "Together Computer",
            "01. AI",
            "OpenAI",
            "DeepSeek-AI",
            "AI@Meta",
            "AI@Waktaverse",
            "42dot Inc.",
            "IDEA-CCNL",
            "CodeGemma Team",
        ]
        for team in teams:
            if team in authors and "{" + team + "}" not in authors:
                authors = authors.replace(team, "{" + team + "}")
                library.entries[0]["author"] = authors

        bibtex = bibtexparser.write_string(library)

    # considering latex special characters
    bibtex = bibtex.replace("_", r"\_")
    bibtex = bibtex.replace("&", r"\&")
    bibtex = bibtex.replace("%", r"\%")

    return bibtex


def norm_authors(authors: str) -> str:
    if " and " not in authors:
        authors = authors.replace(", ", " and")
    else:
        if ", " in authors:
            authors_list = authors.split(" and ")
            new_authors_list = []
            for author in authors_list:
                if ", " in author:
                    last, first = author.split(", ")
                    new_author = f"{first} {last}"
                    new_authors_list.append(new_author)
                else:
                    new_authors_list.append(author)
            authors = " and ".join(new_authors_list)

    return authors


def main():
    with open(DATA_PATH, "rb") as f:
        modeldata = pkl.load(f)
    model_names = []
    model_name2created_at = {}
    for model_dict in modeldata:
        model_name = model_dict["model_name"]
        created_at = model_dict["created_at"]
        model_names.append(model_name)
        model_name2created_at[model_name] = created_at

    bibtex_dir = Path("data/bibtex")
    model_name_bibId2bibtex = {}
    for model_name in tqdm(model_names):
        file_name = model_name2file_name(model_name)
        bibtex_path = bibtex_dir / f"{file_name}.bib"
        if not bibtex_path.exists():
            continue
        with open(bibtex_path, "r") as f:
            bibtex = f.read()
        bibtex_list = bibtex.split(SEP)
        for bibId, bibtex in enumerate(bibtex_list):
            model_name_bibId2bibtex[(model_name, bibId)] = bibtex

    model_name_bibId2title = {}
    for model_name_bibId, bibtex in model_name_bibId2bibtex.items():
        library = bibtexparser.parse_string(bibtex)
        entry = library.entries[0]
        model_name_bibId2title[model_name_bibId] = entry.get("title").value
    assert len(model_name_bibId2bibtex) == len(model_name_bibId2title)

    model_name_bibIds = list(model_name_bibId2title.keys())
    ds = DisjointSet(len(model_name_bibIds))
    checked_title_i_and_title_j = set()
    for i, (model_name_i, bibId_i) in tqdm(list(enumerate(model_name_bibIds))):
        title_i = model_name_bibId2title[(model_name_i, bibId_i)]

        for j in range(i + 1, len(model_name_bibIds)):
            model_name_j, bibId_j = model_name_bibIds[j]
            title_j = model_name_bibId2title[(model_name_j, bibId_j)]

            if str_sim(title_i, title_j) == 1.0:
                ds.unite(i, j)
            # tiles are similar, but not exactly the same,
            # so check manually if they are same on case-by-case basis
            elif 0.65 <= str_sim(title_i, title_j) < 1.0:
                if casefix(title_i, title_j):
                    ds.unite(i, j)
            # even if title is not similar, check if they have same authors
            else:
                bib_i = model_name_bibId2bibtex[(model_name_i, bibId_i)]
                library_i = bibtexparser.parse_string(bib_i)
                authors_i = library_i.entries[0].get("author")
                bib_j = model_name_bibId2bibtex[(model_name_j, bibId_j)]
                library_j = bibtexparser.parse_string(bib_j)
                authors_j = library_j.entries[0].get("author")
                if authors_i is not None and authors_j is not None:
                    authors_i = authors_i.value
                    authors_j = authors_j.value

                    authors_i = norm_authors(authors_i)
                    authors_j = norm_authors(authors_j)

                    if authors_i == authors_j:
                        if sorted([title_i, title_j]) == [
                            "A Conversational Paradigm for Program Synthesis",
                            "CodeGen: An Open Large Language Model for Code with Multi-Turn Program Synthesis",  # noqa: E501
                        ]:
                            ds.unite(i, j)
                        else:
                            # even if authors are same,
                            # we checked they are different
                            # (for example, single author or team name)
                            if tuple(sorted([title_i, title_j])
                                     ) in checked_title_i_and_title_j:
                                continue
                            checked_title_i_and_title_j.add(
                                tuple(sorted([title_i, title_j]))
                            )
                            logger.info(
                                f"'{title_i}' and '{title_j}' have same authors: {authors_i}, but they seem different."  # noqa: E501
                            )

    root_i2max_bib = {}
    entryid_set = set()
    model_name_bibId2bibtex_new = {}
    for i, (model_name_i, bibId_i) in tqdm(list(enumerate(model_name_bibIds))):
        # get representative root
        root_i = ds.find(i)

        # if reprsentative bibtex is already determined, use it
        if root_i in root_i2max_bib:
            model_name_bibId2bibtex_new[(model_name_i, bibId_i)] = \
                root_i2max_bib[root_i]
            continue

        # get all bibtex in the same group
        gs = ds.group(root_i)

        bib2count = defaultdict(int)
        for j in gs:
            model_name_j, bibId_j = model_name_bibIds[j]
            bib_j = model_name_bibId2bibtex[(model_name_j, bibId_j)]
            bib2count[bib_j] += 1

        # check max_key is one
        max_bib = max(bib2count, key=bib2count.get)
        max_bib_list = []
        for bib in bib2count:
            if bib2count[bib] < bib2count[max_bib]:
                continue
            else:
                max_bib_list.append(bib)

        if len(max_bib_list) > 1:
            hasarxiv = False
            for bib in max_bib_list:
                library = bibtexparser.parse_string(bib)
                # if arxiv is in the ID, use it
                if library.entries[0]["ID"].startswith("arxiv:"):
                    max_bib = bib
                    hasarxiv = True
                    break
            # if arxiv is not in the ID, use the one with max length
            if not hasarxiv:
                max_bib = max(max_bib_list, key=lambda x: len(x))

        # assert uniqueness for entryid
        # some bibtex have same entryid, so we need to change it
        library = bibtexparser.parse_string(max_bib)
        fields = library.entries[0]
        entryid = fields["ID"]
        if entryid in entryid_set:
            title = fields["title"]
            title_words = title.split()
            title_words = [
                word for word in title_words if word not in string.punctuation
            ]
            new_entryid = "-".join(title_words).replace(":-", ":")
            logger.info(
                f"model_name: {model_name_i}, root_i: {root_i}, "
                f"entry id: {entryid} => {new_entryid}"
            )
            assert new_entryid not in entryid_set, \
                f"{new_entryid} is already used"
            entryid_set.add(new_entryid)
            library.entries[0].key = new_entryid
            max_bib = bibtexparser.write_string(library)

        # "_" is not allowed in latex, so replace it with "-"
        elif "_" in entryid:
            new_entryid = entryid.replace("_", "-")
            assert new_entryid not in entryid_set, \
                f"{new_entryid} is already used"
            logger.info(
                f"model_name: {model_name_i}, root_i: {root_i}, "
                f"entry id: {entryid} => {new_entryid}"
            )
            entryid_set.add(entryid)
            library.entries[0].key = new_entryid
            max_bib = bibtexparser.write_string(library)

        else:
            entryid_set.add(entryid)

        root_i2max_bib[root_i] = max_bib
        model_name_bibId2bibtex_new[(model_name_i, bibId_i)] = \
            root_i2max_bib[root_i]

    model_name2entryidset = defaultdict(set)
    bibtex_set = set()
    for model_name_bibId in model_name_bibId2bibtex_new.keys():
        model_name, bibId = model_name_bibId
        bibtex = model_name_bibId2bibtex_new[model_name_bibId]
        library = bibtexparser.parse_string(bibtex)
        fields = library.entries[0]
        entryid = fields["ID"]

        try:
            year = int(fields["year"])
        except Exception as e:
            created_at = model_name2created_at[model_name]
            year = int(created_at.split("-")[0])
            logger.error(
                f"model_name: {model_name}, "
                f"{e}, created_at: {created_at} => {year}"
            )
            library.entries[0]["year"] = str(year)
            if model_name == "Deci/DeciLM-7B-instruct":
                # year entry does not have "," in the end, so add it.
                # # below is the original bibtex:
                # @misc{DeciFoundationModels,
                # title = {DeciLM-7B-instruct},
                # author = {DeciAI Research Team},
                # year = {2023}
                # url={https://huggingface.co/Deci/DeciLM-7B-instruct},
                # }
                # since year entry does not have "," in the end,
                # url entry is also not detected.
                # so we need to add url entry manually.
                url = "https://huggingface.co/Deci/DeciLM-7B-instruct"
                library.entries[0]["url"] = url
            bibtex = bibtexparser.write_string(library)

        bibtex = clean_bibtex(bibtex)
        # all bibtex
        bibtex_set.add(bibtex)
        # model_name, entryid, year, authors
        authors = bibtexparser.parse_string(bibtex).entries[0].get("author")
        assert authors is not None, f"following bibtex has no author: {bibtex}"
        authors = authors.value
        model_name2entryidset[model_name].add((entryid, year, authors))

    # save bibtex
    output_dir = Path("data")
    output_path = output_dir / "model_list.bib"
    bibtex_list = sorted(list(bibtex_set))
    with open(output_path, "w") as f:
        for bibtex in bibtex_list:
            f.write(bibtex)
            f.write(SEP)
    logger.info(f"Saving to {output_path}")

    def get_last_name(authors: str) -> str:

        first_author = authors.split(" and")[0]
        first_author = first_author.strip()

        # team name case
        if "{" and "}" in first_author:
            return first_author.replace("{", "").replace("}", "").strip()

        if ", " in first_author:
            splits = first_author.split(", ")
            last_name = splits[0]
        else:
            splits = first_author.split(" ")
            last_name = " ".join(splits[1:])

        return last_name.strip()

    # save model_name2entryidset
    model_name2entryid = {}
    for model_name in sorted(model_name2entryidset.keys()):
        entryidlist = [entryid for entryid, _, _ in sorted(
            model_name2entryidset[model_name],
            key=lambda x: (x[1], get_last_name(x[2]))
        )]
        model_name2entryid[model_name] = entryidlist

    output_path = output_dir / "model_name2entryid.pkl"
    with open(output_path, "wb") as f:
        pkl.dump(model_name2entryid, f)


if __name__ == "__main__":
    main()
