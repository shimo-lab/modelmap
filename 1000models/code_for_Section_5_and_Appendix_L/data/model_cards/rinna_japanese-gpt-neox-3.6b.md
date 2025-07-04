
# japanese-gpt-neox-3.6b

![rinna-icon](./rinna.png)

# Overview
This repository provides a Japanese GPT-NeoX model of 3.6 billion parameters.

* **Library**
    
    The model was trained using code based on [EleutherAI/gpt-neox](https://github.com/EleutherAI/gpt-neox).

* **Model architecture**

    A 36-layer, 2816-hidden-size transformer-based language model.

* **Pre-training**

    The model was trained on around **312.5B** tokens from [Japanese CC-100](http://data.statmt.org/cc-100/ja.txt.xz), [Japanese C4](https://huggingface.co/datasets/mc4), and [Japanese Wikipedia](https://dumps.wikimedia.org/other/cirrussearch) to optimize a traditional language modelling objective. 

    A final validation perplexity of **8.68** has been reached.


* **Model Series**

    | Variant | Link |
    | :-- | :--|
    | 3.6B PPO | https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo |
    | 3.6B SFT-v2 | https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2 |
    | 3.6B SFT | https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft |
    | 3.6B pretrained | https://huggingface.co/rinna/japanese-gpt-neox-3.6b |

* **Contributors**
    
    [Tianyu Zhao](https://huggingface.co/tianyuz) and [Kei Sawada](https://huggingface.co/keisawada)

* **Release date**

    March 17, 2023

# How to use the model

~~~~python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("rinna/japanese-gpt-neox-3.6b", use_fast=False)
model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt-neox-3.6b")

if torch.cuda.is_available():
    model = model.to("cuda")

text = "西田幾多郎は、"
token_ids = tokenizer.encode(text, add_special_tokens=False, return_tensors="pt")

with torch.no_grad():
    output_ids = model.generate(
        token_ids.to(model.device),
        max_new_tokens=100,
        min_new_tokens=100,
        do_sample=True,
        temperature=0.8,
        pad_token_id=tokenizer.pad_token_id,
        bos_token_id=tokenizer.bos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

output = tokenizer.decode(output_ids.tolist()[0])
print(output)
"""西田幾多郎は、この「絶対矛盾的自己同一」を「世界の自己同一」と置きかえ、さらに西田哲学を出発点として「絶対無」を「世界の成立」に変え、世界と自己を一つの統一物とみなす哲学として展開する。この世界と自己は絶対矛盾的自己同一として同一の性質を有し、同じ働きをする。西田哲学においては、この世界と自己は矛盾しあうのではなく、同一の性質をもっている。この世界と自己は同一である。絶対"""
~~~~

# Tokenization
The model uses a [sentencepiece](https://github.com/google/sentencepiece)-based tokenizer.
* The tokenizer has a vocabulary size of 32,000.
* It uses sentencepiece's byte fallback feature to decompose unknown text pieces into UTF-8 byte pieces and to avoid producing `<UNK>` tokens.
* sentencepiece's `--add_dummy_prefix` option was turned off so that a leading whitespace will not be prepended automatically.
    ~~~
    print(tokenizer.tokenize("吾輩は猫である"))
    # ['吾', '輩', 'は', '猫', 'である']
    # instead of ['▁', '吾', '輩', 'は', '猫', 'である'] as in rinna/japanese-gpt-1b
    ~~~
* sentencepiece's `--remove_extra_whitespaces` option was turned off so that leading, trailing, and duplicate whitespaces are reserved.
    ~~~
    print(tokenizer.tokenize("  吾輩は  猫である   "))
    # ['▁', '▁', '吾', '輩', 'は', '▁', '▁', '猫', 'である', '▁', '▁', '▁']
    # instead of ['▁', '吾', '輩', 'は', '▁猫', 'である'] as in rinna/japanese-gpt-1b
    ~~~
* Don't forget to set `use_fast=False` to make the above features function correctly.
    ~~~
    good_tokenizer = AutoTokenizer.from_pretrained("rinna/japanese-gpt-neox-3.6b", use_fast=False)
    bad_tokenizer = AutoTokenizer.from_pretrained("rinna/japanese-gpt-neox-3.6b")

    print(good_tokenizer.decode(good_tokenizer.encode("გამარჯობა  吾輩は  猫である   ")))
    # 'გამარჯობა  吾輩は  猫である   </s>'
    print(bad_tokenizer.decode(bad_tokenizer.encode("გამარჯობა  吾輩は  猫である   ")))
    # 'გამარ[UNK]ობა 吾輩は 猫である </s>'
    ~~~

# How to cite
```bibtex
@misc{rinna-japanese-gpt-neox-3.6b,
    title = {rinna/japanese-gpt-neox-3.6b},
    author = {Zhao, Tianyu and Sawada, Kei},
    url = {https://huggingface.co/rinna/japanese-gpt-neox-3.6b}
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

# Licenese
[The MIT license](https://opensource.org/licenses/MIT)
