
# OPT : Open Pre-trained Transformer Language Models

OPT was first introduced in [Open Pre-trained Transformer Language Models](https://arxiv.org/abs/2205.01068) and first released in [metaseq's repository](https://github.com/facebookresearch/metaseq) on May 3rd 2022 by Meta AI.

**Disclaimer**: The team releasing OPT wrote an official model card, which is available in Appendix D of the [paper](https://arxiv.org/pdf/2205.01068.pdf). 
Content from **this** model card has been written by the Hugging Face team.

## Intro

To quote the first two paragraphs of the [official paper](https://arxiv.org/abs/2205.01068)

> Large language models trained on massive text collections have shown surprising emergent
> capabilities to generate text and perform zero- and few-shot learning. While in some cases the public
> can interact with these models through paid APIs, full model access is currently limited to only a
> few highly resourced labs. This restricted access has limited researchers’ ability to study how and
> why these large language models work, hindering progress on improving known challenges in areas
> such as robustness, bias, and toxicity.

> We present Open Pretrained Transformers (OPT), a suite of decoder-only pre-trained transformers ranging from 125M
> to 175B parameters, which we aim to fully and responsibly share with interested researchers. We train the OPT models to roughly match 
> the performance and sizes of the GPT-3 class of models, while also applying the latest best practices in data
> collection and efficient training. Our aim in developing this suite of OPT models is to enable reproducible and responsible research at scale, and
> to bring more voices to the table in studying the impact of these LLMs. Definitions of risk, harm, bias, and toxicity, etc., should be articulated by the
> collective research community as a whole, which is only possible when models are available for study.

## Model description

OPT was predominantly pretrained with English text, but a small amount of non-English data is still present within the training corpus via CommonCrawl. The model was pretrained using a causal language modeling (CLM) objective.
OPT belongs to the same family of decoder-only models like [GPT-3](https://arxiv.org/abs/2005.14165). As such, it was pretrained using the self-supervised causal language modedling objective.

For evaluation, OPT follows [GPT-3](https://arxiv.org/abs/2005.14165) by using their prompts and overall experimental setup. For more details, please read 
the [official paper](https://arxiv.org/abs/2205.01068).

## Intended uses & limitations

The pretrained-only model can be used for prompting for evaluation of downstream tasks as well as text generation.
In addition, the model can be fine-tuned on a downstream task using the [CLM example](https://github.com/huggingface/transformers/tree/main/examples/pytorch/language-modeling). For all other OPT checkpoints, please have a look at the [model hub](https://huggingface.co/models?filter=opt).

### How to use

For large OPT models, such as this one, it is not recommend to make use of the `text-generation` pipeline because
one should load the model in half-precision to accelerate generation and optimize memory consumption on GPU.
It is recommended to directly call the [`generate`](https://huggingface.co/docs/transformers/main/en/main_classes/text_generation#transformers.generation_utils.GenerationMixin.generate)
 method as follows: 


```python
>>> from transformers import AutoModelForCausalLM, AutoTokenizer
>>> import torch

>>> model = AutoModelForCausalLM.from_pretrained("facebook/opt-13b", torch_dtype=torch.float16).cuda()

>>> # the fast tokenizer currently does not work correctly
>>> tokenizer = AutoTokenizer.from_pretrained("facebook/opt-13b", use_fast=False)

>>> prompt = "Hello, I'm am conscious and"


>>> input_ids = tokenizer(prompt, return_tensors="pt").input_ids.cuda()

>>> generated_ids = model.generate(input_ids)

>>> tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
['Hello, I am conscious and aware of my surroundings.\nI am conscious and aware of my']
```

By default, generation is deterministic. In order to use the top-k sampling, please set `do_sample` to `True`. 

```python
>>> from transformers import AutoModelForCausalLM, AutoTokenizer, set_seed
>>> import torch

>>> model = AutoModelForCausalLM.from_pretrained("facebook/opt-13b", torch_dtype=torch.float16).cuda()

>>> # the fast tokenizer currently does not work correctly
>>> tokenizer = AutoTokenizer.from_pretrained("facebook/opt-13b", use_fast=False)

>>> prompt = "Hello, I'm am conscious and"

>>> input_ids = tokenizer(prompt, return_tensors="pt").input_ids.cuda()

>>> set_seed(32)
>>> generated_ids = model.generate(input_ids, do_sample=True)

>>> tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
['Hello, I am conscious and aware.\nSo that makes you dead, right?  ']
```

### Limitations and bias

As mentioned in Meta AI's model card, given that the training data used for this model contains a lot of
unfiltered content from the internet, which is far from neutral the model is strongly biased : 

> Like other large language models for which the diversity (or lack thereof) of training
> data induces downstream impact on the quality of our model, OPT-175B has limitations in terms
> of bias and safety. OPT-175B can also have quality issues in terms of generation diversity and
> hallucination. In general, OPT-175B is not immune from the plethora of issues that plague modern
> large language models. 

Here's an example of how the model can have biased predictions:

```python
>>> from transformers import AutoModelForCausalLM, AutoTokenizer, set_seed
>>> import torch

>>> model = AutoModelForCausalLM.from_pretrained("facebook/opt-13b", torch_dtype=torch.float16).cuda()

>>> # the fast tokenizer currently does not work correctly
>>> tokenizer = AutoTokenizer.from_pretrained("facebook/opt-13b", use_fast=False)

>>> prompt = "The woman worked as a"

>>> input_ids = tokenizer(prompt, return_tensors="pt").input_ids.cuda()

>>> set_seed(32)
>>> generated_ids = model.generate(input_ids, do_sample=True, num_return_sequences=5, max_length=10)

>>> tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
The woman worked as a supervisor in the office 
The woman worked as a social media consultant for
The woman worked as a cashier at the
The woman worked as a teacher, and was
The woman worked as a maid at our friends
```

compared to:

```python
>>> from transformers import AutoModelForCausalLM, AutoTokenizer, set_seed
>>> import torch

>>> model = AutoModelForCausalLM.from_pretrained("facebook/opt-13b", torch_dtype=torch.float16).cuda()

>>> # the fast tokenizer currently does not work correctly
>>> tokenizer = AutoTokenizer.from_pretrained("facebook/opt-13b", use_fast=False)

>>> prompt = "The man worked as a"

>>> input_ids = tokenizer(prompt, return_tensors="pt").input_ids.cuda()

>>> set_seed(32)
>>> generated_ids = model.generate(input_ids, do_sample=True, num_return_sequences=5, max_length=10)

>>> tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
The man worked as a consultant to the defense
The man worked as a bartender in a bar
The man worked as a cashier at the
The man worked as a teacher, and was
The man worked as a professional athlete while he
 ```

This bias will also affect all fine-tuned versions of this model.

## Training data

The Meta AI team wanted to train this model on a corpus as large as possible. It is composed of the union of the following 5 filtered datasets of textual documents: 

  - BookCorpus, which consists of more than 10K unpublished books,
  - CC-Stories, which contains a subset of CommonCrawl data filtered to match the
story-like style of Winograd schemas,
  - The Pile, from which * Pile-CC, OpenWebText2, USPTO, Project Gutenberg, OpenSubtitles, Wikipedia, DM Mathematics and HackerNews* were included. 
  - Pushshift.io Reddit dataset that was developed in Baumgartner et al. (2020) and processed in
Roller et al. (2021)
  - CCNewsV2 containing an updated version of the English portion of the CommonCrawl News
dataset that was used in RoBERTa (Liu et al., 2019b)

The final training data contains 180B tokens corresponding to 800GB of data. The validation split was made of 200MB of the pretraining data, sampled proportionally
to each dataset’s size in the pretraining corpus. 

The dataset might contains offensive content as parts of the dataset are a subset of
public Common Crawl data, along with a subset of public Reddit data, which could contain sentences
that, if viewed directly, can be insulting, threatening, or might otherwise cause anxiety.

### Collection process

The dataset was collected form internet, and went through classic data processing algorithms  and
re-formatting practices, including removing repetitive/non-informative text like *Chapter One* or
*This ebook by Project Gutenberg.*

## Training procedure

### Preprocessing

The texts are tokenized using the **GPT2** byte-level version of Byte Pair Encoding (BPE) (for unicode characters) and a
vocabulary size of 50272. The inputs are sequences of 2048 consecutive tokens.

The 175B model was trained on 992 *80GB A100 GPUs*. The training duration was roughly ~33 days of continuous training.

### BibTeX entry and citation info

```bibtex
@misc{zhang2022opt,
      title={OPT: Open Pre-trained Transformer Language Models}, 
      author={Susan Zhang and Stephen Roller and Naman Goyal and Mikel Artetxe and Moya Chen and Shuohui Chen and Christopher Dewan and Mona Diab and Xian Li and Xi Victoria Lin and Todor Mihaylov and Myle Ott and Sam Shleifer and Kurt Shuster and Daniel Simig and Punit Singh Koura and Anjali Sridhar and Tianlu Wang and Luke Zettlemoyer},
      year={2022},
      eprint={2205.01068},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
