
# `Llama 3 Youko 8B (rinna/llama-3-youko-8b)`

![rinna-icon](./rinna.png)

# Overview

We conduct continual pre-training of [meta-llama/Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B) on **22B** tokens from a mixture of Japanese and English datasets. The continual pre-training significantly improves the model's performance on Japanese tasks.

The name `youko` comes from the Japanese word [`妖狐/ようこ/Youko`](https://ja.wikipedia.org/wiki/%E5%A6%96%E7%8B%90), which is a kind of Japanese mythical creature ([`妖怪/ようかい/Youkai`](https://ja.wikipedia.org/wiki/%E5%A6%96%E6%80%AA)).

| Size | Continual Pre-Training | Instruction-Tuning |
| :-   | :-                     | :-                 |
| 8B   | Llama 3 Youko 8B [[HF]](https://huggingface.co/rinna/llama-3-youko-8b) [[GPTQ]](https://huggingface.co/rinna/llama-3-youko-8b-gptq) | Llama 3 Youko 8B Instruct [[HF]](https://huggingface.co/rinna/llama-3-youko-8b-instruct) [[GPTQ]](https://huggingface.co/rinna/llama-3-youko-8b-instruct-gptq) |
| 70B  | Llama 3 Youko 70B [[HF]](https://huggingface.co/rinna/llama-3-youko-70b) [[GPTQ]](https://huggingface.co/rinna/llama-3-youko-70b-gptq) | Llama 3 Youko 70B Instruct [[HF]](https://huggingface.co/rinna/llama-3-youko-70b-instruct) [[GPTQ]](https://huggingface.co/rinna/llama-3-youko-70b-instruct-gptq) |

* **Library**

    The model was trained using code based on [EleutherAI/gpt-neox](https://github.com/EleutherAI/gpt-neox).

* **Model architecture**

    A 32-layer, 4096-hidden-size transformer-based language model. Refer to the [Llama 3 Model Card](https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md) for architecture details.

* **Training: Built with Meta Llama 3**

    The model was initialized with the [meta-llama/Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B) model and continually trained on around **22B** tokens from a mixture of the following corpora
    - [Japanese CC-100](https://huggingface.co/datasets/cc100)
    - [Japanese C4](https://huggingface.co/datasets/mc4)
    - [Japanese OSCAR](https://huggingface.co/datasets/oscar-corpus/colossal-oscar-1.0)
    - [The Pile](https://huggingface.co/datasets/EleutherAI/pile)
    - [Wikipedia](https://dumps.wikimedia.org/other/cirrussearch)
    - rinna curated Japanese dataset
  
* **Contributors**

    - [Koh Mitsuda](https://huggingface.co/mitsu-koh)
    - [Xinqi Chen](https://huggingface.co/Keely0419)
    - [Toshiaki Wakatsuki](https://huggingface.co/t-w)
    - [Kei Sawada](https://huggingface.co/keisawada)

* **Release date**

    May 1, 2024

---

# Benchmarking

Please refer to [rinna's LM benchmark page (Sheet 20240507)](https://rinnakk.github.io/research/benchmarks/lm/index.html).

---

# How to use the model

~~~~python
import transformers
import torch

model_id = "rinna/llama-3-youko-8b"
pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto"
)
output = pipeline(
    "西田幾多郎は、",
    max_new_tokens=256,
    do_sample=True
)
print(output[0]["generated_text"])
~~~~

---

# Tokenization
The model uses the original [meta-llama/Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B) tokenizer.

---

# How to cite
```bibtex
@misc{rinna-llama-3-youko-8b,
    title = {rinna/llama-3-youko-8b},
    author = {Mitsuda, Koh and Chen, Xinqi and Wakatsuki, Toshiaki and Sawada, Kei},
    url = {https://huggingface.co/rinna/llama-3-youko-8b}
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
@article{llama3modelcard,
    title = {Llama 3 Model Card},
    author = {AI@Meta},
    year = {2024},
    url = {https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md}
}

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
[Meta Llama 3 Community License](https://llama.meta.com/llama3/license/)