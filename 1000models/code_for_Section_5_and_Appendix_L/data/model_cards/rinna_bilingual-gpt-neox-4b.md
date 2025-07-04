
# bilingual-gpt-neox-4b

![rinna-icon](./rinna.png)

# Overview
This repository provides an English-Japanese bilingual GPT-NeoX model of 3.8 billion parameters.

* **Library**
    
    The model was trained using code based on [EleutherAI/gpt-neox](https://github.com/EleutherAI/gpt-neox).

* **Model architecture**

    A 36-layer, 2816-hidden-size transformer-based language model.

* **Pre-training**

    The model was trained on around **524B** tokens from a mixture of the following corpora

    - [Japanese CC-100](http://data.statmt.org/cc-100/ja.txt.xz)
    - [Japanese C4](https://huggingface.co/datasets/mc4)
    - [The Pile](https://huggingface.co/datasets/EleutherAI/pile)
    - [Redpajama](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T)
    - [Wikipedia](https://dumps.wikimedia.org/other/cirrussearch)

* **Model Series**

    | Variant | Link |
    | :-- | :--|
    | Bilingual 4B MiniGPT4 | https://huggingface.co/rinna/bilingual-gpt-neox-4b-minigpt4 |
    | Bilingual 4B PPO | https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-ppo |
    | Bilingual 4B SFT | https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-sft |
    | Bilingual 4B 8K | https://huggingface.co/rinna/bilingual-gpt-neox-4b-8k |
    | Bilingual 4B | https://huggingface.co/rinna/bilingual-gpt-neox-4b |
    | Japanese 3.6B PPO | https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo |
    | Japanese 3.6B SFT-v2 | https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2 |
    | Japanese 3.6B SFT | https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft |
    | Japanese 3.6B | https://huggingface.co/rinna/japanese-gpt-neox-3.6b |

* **Contributors**
    
    - [Tianyu Zhao](https://huggingface.co/tianyuz)
    - [Toshiaki Wakatsuki](https://huggingface.co/t-w)
    - [Akio Kaga](https://huggingface.co/rakaga)
    - [Koh Mitsuda](https://huggingface.co/mitsu-koh)
    - [Kei Sawada](https://huggingface.co/keisawada)

* **Release date**

    July 31, 2023

---

# Benchmarking

* **Japanese benchmark**

  Our evaluation experiments suggest that the bilingual-gpt-neox-4b model performs slightly better than the previous [Japanese GPT-NeoX 3.6B](https://huggingface.co/rinna/japanese-gpt-neox-3.6b) in Japanese tasks.
    - *The 4-task average accuracy is based on results of JCommonsenseQA, JNLI, MARC-ja, and JSQuAD.*
    - *The 6-task average accuracy is based on results of JCommonsenseQA, JNLI, MARC-ja, JSQuAD, XWinograd, and JAQKET-v2.*
   
    | Model | 4-task average accuracy | 6-task average accuracy |
    | :-- | :-- | :-- |
    | bilingual-gpt-neox-4b-instruction-ppo | 61.01 | 61.16 |
    | bilingual-gpt-neox-4b-instruction-sft | 61.02 | 61.69 |
    | **bilingual-gpt-neox-4b** | **56.12** | **51.83** |
    | japanese-gpt-neox-3.6b-instruction-ppo | 59.86 | 60.07 |
    | japanese-gpt-neox-3.6b | 55.07 | 50.32 |
    
* **English benchmark**

  Using the [EleutherAI Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/master), we found the bilingual-gpt-neox-4b performs comparably with English/multilingual models of similar sizes.
    - *The average accuracy is based on results of Arc-Challenge, Arc-Easy, BoolQ, COPA, HellaSwag, OpenBookQA, PIQA, PROST, SWAG, and WinoGrande.*
    
    | Model | Average accuracy |
    | :-- | :-- |
    | mpt-7b | 59.30 |
    | llama-7b | 57.35 |
    | bloom-7b | 51.51 |
    | xglm-7.5b | 50.96 |
    | xglm-4.5b | 50.15 |
    | **bilingual-gpt-neox-4b** | **49.49** |
    | bloom-3b | 48.56 |
    | xglm-2.9b | 47.44 |
    | bloom-1.7b | 46.54 |

---

# How to use the model

**Notice:** Since the model is **sensitive to decoding hyper-parameters** (e.g. `temperature`, `top_p`, `top_k`, `repetition_penalty`), it is suggested to explore the best setting for your task.

~~~~python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("rinna/bilingual-gpt-neox-4b", use_fast=False)
model = AutoModelForCausalLM.from_pretrained("rinna/bilingual-gpt-neox-4b")

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
        temperature=1.0,
        top_p=0.95,
        pad_token_id=tokenizer.pad_token_id,
        bos_token_id=tokenizer.bos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

output = tokenizer.decode(output_ids.tolist()[0])
print(output)
"""
西田幾多郎は、その著書「自覚の哲学」の中で、次のように書きました。  
「知識を、自分のものと考えることに満足していると、自己の限界に目覚めることを忘れてしまう。しかし、他者との協同なしには、自己の本当の理解に達することはできないのだ。知識は他者と相互の、協同の力によってこそ、得られるのである。」(引用終わり)  
この一節を、私たちは今から学び直すべきです。そして、これからの社会をリードする子どもたちに、その能力を伸ばすべく、
"""
~~~~

~~~~python
text = "Socrates says"
token_ids = tokenizer.encode(text, add_special_tokens=False, return_tensors="pt")

with torch.no_grad():
    output_ids = model.generate(
        token_ids.to(model.device),
        max_new_tokens=100,
        min_new_tokens=100,
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
Socrates says: he thinks that philosophy, as opposed to myth, can be demonstrated; as opposed to poetry, that it is not possible to have knowledge of the unknowable (that is, neither by reason nor by any art of divination). So in this case he is in agreement with Socrates in not thinking that we could prove the existence of the gods or of fate. Now, I do not know the content of Xenophon's _Symposium_, but he must have made a point of this passage that has ex
"""
~~~~

~~~~python
text = "def bubble_sort(array):"
token_ids = tokenizer.encode(text, add_special_tokens=False, return_tensors="pt")

with torch.no_grad():
    output_ids = model.generate(
        token_ids.to(model.device),
        max_new_tokens=200,
        min_new_tokens=200,
        do_sample=True,
        temperature=1.0,
        top_p=0.5,
        pad_token_id=tokenizer.pad_token_id,
        bos_token_id=tokenizer.bos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

output = tokenizer.decode(output_ids.tolist()[0])
print(output)
"""
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubble_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

The code above will sort the array from 1 to 10 in the following order:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

However, I am not sure how to do
"""
~~~~

---

# Tokenization
The model uses a [sentencepiece](https://github.com/google/sentencepiece)-based tokenizer.
* The tokenizer has a vocabulary size of 65,536.
* It uses *byte fallback* to decompose unknown text pieces into UTF-8 byte pieces to avoid producing `<UNK>` tokens.
* It can recognize *consecutive whitespaces*, *newlines*, and *tabs* to handle structured texts better.
* We turned off the default behaviour of prepending leading whitespace because it is not beneficial for processing Japanese.
* Specifically, single whitespace is always processed as one token so that any English word won't have a preceding whitespace like in many other tokenizers (e.g. `_Hello`).
  * This decision trades the English processing efficiency for a unified way to treat whitespaces.
  * It leads to a significantly lower loss of next token prediction on English data because whitespaces are easy to predict.
* **Don't forget to set `use_fast=False` to make the above features function correctly.**

---

# How to cite
```bibtex
@misc{rinna-bilingual-gpt-neox-4b,
    title = {rinna/bilingual-gpt-neox-4b},
    author = {Zhao, Tianyu and Wakatsuki, Toshiaki and Kaga, Akio and Mitsuda, Koh and Sawada, Kei},
    url = {https://huggingface.co/rinna/bilingual-gpt-neox-4b}
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

# Licenese
[The MIT license](https://opensource.org/licenses/MIT)