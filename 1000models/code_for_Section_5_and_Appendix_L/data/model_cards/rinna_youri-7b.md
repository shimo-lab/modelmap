
# `rinna/youri-7b`

![rinna-icon](./rinna.png)

# Overview
We conduct continual pre-training of [llama2-7b](https://huggingface.co/meta-llama/Llama-2-7b-hf) on **40B** tokens from a mixture of Japanese and English datasets. The continual pre-training significantly improves the model's performance on Japanese tasks.

The name `youri` comes from the Japanese word [`妖狸/ようり/Youri`](https://ja.wikipedia.org/wiki/%E5%8C%96%E3%81%91%E7%8B%B8), which is a kind of Japanese mythical creature ([`妖怪/ようかい/Youkai`](https://ja.wikipedia.org/wiki/%E5%A6%96%E6%80%AA)).

* **Library**
    
    The model was trained using code based on [EleutherAI/gpt-neox](https://github.com/EleutherAI/gpt-neox).

* **Model architecture**

    A 32-layer, 4096-hidden-size transformer-based language model. Refer to the [llama2 paper](https://arxiv.org/abs/2307.09288) for architecture details.

* **Continual pre-training**

    The model was initialized with the [llama2-7b](https://huggingface.co/meta-llama/Llama-2-7b-hf) model and continually trained on around **40B** tokens from a mixture of the following corpora
    - [Japanese CC-100](http://data.statmt.org/cc-100/ja.txt.xz)
    - [Japanese C4](https://huggingface.co/datasets/mc4)
    - [Japanese OSCAR](https://huggingface.co/datasets/oscar-corpus/colossal-oscar-1.0)
    - [The Pile](https://huggingface.co/datasets/EleutherAI/pile)
    - [Wikipedia](https://dumps.wikimedia.org/other/cirrussearch)
    - rinna curated Japanese dataset

* **Contributors**
    
    - [Tianyu Zhao](https://huggingface.co/tianyuz)
    - [Akio Kaga](https://huggingface.co/rakaga)
    - [Kei Sawada](https://huggingface.co/keisawada)

* **Release date**

    October 31, 2023

---

# Benchmarking

Please refer to [rinna's LM benchmark page (Sheet 20231031)](https://rinnakk.github.io/research/benchmarks/lm/index.html).

    
---

# How to use the model

~~~~python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("rinna/youri-7b")
model = AutoModelForCausalLM.from_pretrained("rinna/youri-7b")

if torch.cuda.is_available():
    model = model.to("cuda")

text = "西田幾多郎は、"
token_ids = tokenizer.encode(text, add_special_tokens=False, return_tensors="pt")

with torch.no_grad():
    output_ids = model.generate(
        token_ids.to(model.device),
        max_new_tokens=200,
        min_new_tokens=200,
        do_sample=True,
        temperature=1.0,
        top_p=0.95,
        pad_token_id=tokenizer.pad_token_id,
        bos_token_id=tokenizer.bos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

output = tokenizer.decode(output_ids.tolist()[0])
print(output)
"""
西田幾多郎は、プラトンの復権を主張し、対する従来の西洋哲学は、近代の合理主義哲学に委ね、「従来の哲学は破 壊されてしまった」と述べている。 西田幾多郎は、西洋近代哲学の「徹底的な検討」を拒んだ。それは、「現代的理解の脆弱性を補う筈の、従来のヨーロッパに伝わる哲学的な方法では到底それができなかったからである」とい
"""
~~~~

---

# Tokenization
The model uses the original llama-2 tokenizer.

---

# How to cite
```bibtex
@misc{rinna-youri-7b,
    title = {rinna/youri-7b},
    author = {Zhao, Tianyu and Kaga, Akio and Sawada, Kei},
    url = {https://huggingface.co/rinna/youri-7b}
}

@inproceedings{sawada2024release,
    title = {Release of Pre-Trained Models for the {J}apanese Language},
    author = {Sawada, Kei and Zhao, Tianyu and Shing, Makoto and Mitsui, Kentaro and Kaga, Akio and Hono, Yukiya and Wakatsuki, Toshiaki and Mitsuda, Koh},
    booktitle = {Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)},
    month = {5},
    year = {2024},
    pages = {13898--13905},
    url = {https://aclanthology.org/2024.lrec-main.1213},
    note = {\url{https://arxiv.org/abs/2404.01657}}
}
```
---

# References
```bibtex
@software{gpt-neox-library,
    title = {{GPT}-{N}eo{X}: Large Scale Autoregressive Language Modeling in {P}y{T}orch},
    author = {Andonian, Alex and Anthony, Quentin and Biderman, Stella and Black, Sid and Gali, Preetham and Gao, Leo and Hallahan, Eric and Levy-Kramer, Josh and Leahy, Connor and Nestler, Lucas and Parker, Kip and Pieler, Michael and Purohit, Shivanshu and Songz, Tri and Phil, Wang and Weinbach, Samuel},
    doi = {10.5281/zenodo.5879544},
    month = {8},
    year = {2021},
    version = {0.0.1},
    url = {https://www.github.com/eleutherai/gpt-neox}
}
```
---

# License
[The llama2 license](https://ai.meta.com/llama/license/)
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_rinna__youri-7b)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |47.11|
|AI2 Reasoning Challenge (25-Shot)|49.06|
|HellaSwag (10-Shot)              |74.89|
|MMLU (5-Shot)                    |42.22|
|TruthfulQA (0-shot)              |36.03|
|Winogrande (5-shot)              |71.82|
|GSM8k (5-shot)                   | 8.64|