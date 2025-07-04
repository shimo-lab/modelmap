
# MPT-7B-8k

MPT-7B-8k is a decoder-style transformer pretrained starting from MPT-7B, but updating the sequence length to 8k and training for an additional 500B tokens, resulting in a total of 1.5T tokens of text and code.
This model was trained by [MosaicML](https://www.mosaicml.com).

MPT-7B-8k is part of the family of Mosaic Pretrained Transformer (MPT) models, which use a modified transformer architecture optimized for efficient training and inference.

These architectural changes include performance-optimized layer implementations and the elimination of context length limits by replacing
positional embeddings with Attention with Linear Biases ([ALiBi](https://arxiv.org/abs/2108.12409)).
Thanks to these modifications, MPT models can be trained with high throughput efficiency and stable convergence.
MPT models can also be served efficiently with both standard HuggingFace pipelines and NVIDIA's [FasterTransformer](https://github.com/NVIDIA/FasterTransformer).

This model uses the MosaicML LLM codebase, which can be found in the [llm-foundry repository](https://github.com/mosaicml/llm-foundry). It was trained by MosaicML’s NLP team on the [MosaicML platform](https://www.mosaicml.com/training) for LLM pretraining, finetuning, and inference.

### How is this model different?

MPT-7B-8k is

* **Licensed for the possibility of commercial use.**
* **Trained on a large amount of data** (1.5T tokens like [XGen](https://huggingface.co/Salesforce/xgen-7b-8k-base) vs. 1T for [LLaMA](https://arxiv.org/abs/2302.13971), 1T for [MPT-7B](https://www.mosaicml.com/blog/mpt-7b), 300B for [Pythia](https://github.com/EleutherAI/pythia), 300B for [OpenLLaMA](https://github.com/openlm-research/open_llama), and 800B for [StableLM](https://github.com/Stability-AI/StableLM)).
* **Prepared to handle long inputs** thanks to [ALiBi](https://arxiv.org/abs/2108.12409). With ALiBi, the model can extrapolate beyond the 8k training sequence length to up to 10k, and with a few million tokens it can be finetuned to extrapolate much further.
* **Capable of fast training and inference** via [FlashAttention](https://arxiv.org/pdf/2205.14135.pdf) and [FasterTransformer](https://github.com/NVIDIA/FasterTransformer)
* **Equipped with highly efficient open-source training code** via the [llm-foundry repository](https://github.com/mosaicml/llm-foundry)

### Models finetuned off MPT-7B-8k:

The following models are finetuned on MPT-7B-8k:

* [MPT-7B-8k-Instruct](https://huggingface.co/mosaicml/mpt-7b-8k-instruct): a model for long-form instruction following (especially summarization and question-answering).
Built by finetuning MPT-7B-8k on several carefully curated datasets.
  * License: Apache 2.0

* [MPT-7B-8k-Chat](https://huggingface.co/mosaicml/mpt-7b-8k-chat): a chatbot-like model for dialogue generation.
Built by finetuning MPT-7B-8k on approximately 1.5B tokens of chat data.
  * License: _CC-By-NC-SA-4.0_

## Model Date

July 18, 2023

## Model License

Apache-2.0

## Documentation

* [Blog post: MPT-7B-8k](https://www.mosaicml.com/blog/long-context-mpt-7b-8k)
* [Codebase (mosaicml/llm-foundry repo)](https://github.com/mosaicml/llm-foundry/)
* Questions: Feel free to contact us via the [MosaicML Community Slack](https://mosaicml.me/slack)!


## How to Use

This model is best used with the MosaicML [llm-foundry repository](https://github.com/mosaicml/llm-foundry) for training and finetuning.

```python
import transformers
model = transformers.AutoModelForCausalLM.from_pretrained(
  'mosaicml/mpt-7b-8k',
  trust_remote_code=True
)
```
Note: This model requires that `trust_remote_code=True` be passed to the `from_pretrained` method.
This is because we use a custom `MPT` model architecture that is not yet part of the Hugging Face `transformers` package.
`MPT` includes options for many training efficiency features such as [FlashAttention](https://arxiv.org/pdf/2205.14135.pdf), [ALiBi](https://arxiv.org/abs/2108.12409), [QK LayerNorm](https://arxiv.org/abs/2010.04245), and more.

To use the optimized [triton implementation](https://github.com/openai/triton) of FlashAttention, you can load the model on GPU (`cuda:0`) with `attn_impl='triton'` and with `bfloat16` precision:
```python
import torch
import transformers

name = 'mosaicml/mpt-7b-8k'

config = transformers.AutoConfig.from_pretrained(name, trust_remote_code=True)
config.attn_config['attn_impl'] = 'triton'
config.init_device = 'cuda:0' # For fast initialization directly on GPU!

model = transformers.AutoModelForCausalLM.from_pretrained(
  name,
  config=config,
  torch_dtype=torch.bfloat16, # Load model weights in bfloat16
  trust_remote_code=True
)
```

Although the model was trained with a sequence length of 2048, ALiBi enables users to increase the maximum sequence length during finetuning and/or inference. For example:

```python
import transformers

name = 'mosaicml/mpt-7b-8k'

config = transformers.AutoConfig.from_pretrained(name, trust_remote_code=True)
config.max_seq_len = 10000 # (input + output) tokens can now be up to 10000

model = transformers.AutoModelForCausalLM.from_pretrained(
  name,
  config=config,
  trust_remote_code=True
)
```

This model was trained with the MPT-7B-8k tokenizer which is identical to the [EleutherAI/gpt-neox-20b](https://huggingface.co/EleutherAI/gpt-neox-20b) tokenizer.

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('mosaicml/mpt-7b-8k')
```

The model can then be used, for example, within a text-generation pipeline.  
Note: when running Torch modules in lower precision, it is best practice to use the [torch.autocast context manager](https://pytorch.org/docs/stable/amp.html).

```python
from transformers import pipeline

with torch.autocast('cuda', dtype=torch.bfloat16):
    inputs = tokenizer('Here is a recipe for vegan banana bread:\n', return_tensors="pt").to('cuda')
    outputs = model.generate(**inputs, max_new_tokens=100)
    print(tokenizer.batch_decode(outputs, skip_special_tokens=True))

# or using the HF pipeline
pipe = pipeline('text-generation', model=model, tokenizer=tokenizer, device='cuda:0')
with torch.autocast('cuda', dtype=torch.bfloat16):
    print(
        pipe('Here is a recipe for vegan banana bread:\n',
            max_new_tokens=100,
            do_sample=True,
            use_cache=True))
```

## Model Description

The architecture is a modification of a standard decoder-only transformer.

The model has been modified from a standard transformer in the following ways:
* It uses [FlashAttention](https://arxiv.org/pdf/2205.14135.pdf)
* It uses [ALiBi (Attention with Linear Biases)](https://arxiv.org/abs/2108.12409) and does not use positional embeddings
* It does not use biases


| Hyperparameter | Value |
|----------------|-------|
|n_parameters | 6.7B |
|n_layers | 32 |
| n_heads | 32 |
| d_model | 4096 |
| vocab size | 50432 |
| sequence length | 2048 |



## Training Data

### Streaming Datasets

Data was formatted using the MosaicML [StreamingDataset](https://github.com/mosaicml/streaming) library to host our data in object storage and efficiently stream it to our compute cluster during training.
StreamingDataset obviates the need to download the whole dataset before starting training, and allows instant resumption of training from any point in the dataset.


### Data Mix

The model was trained for ___T tokens. First it was trained for 1T tokens (with batch size 1760 and sequence length 2048) on the following data mix:

#### Data Mix for Original 1T Tokens Used to Train MPT-7B

| Data Source | Number of Tokens in Source | Proportion | Effective Number of Tokens | Epochs |
|-------------|----------------------------|------------|----------------------------|--------|
| mC4 3.1.0 - English | 417.99 B | 0.33 | 330 B | 0.14 |
| C4 - English - SemDedup 80% | 100.42 B | 0.299 | 299 B | 2.98 |
| RedPajama - CommonCrawl | 878.45 B | 0.1 | 100 B | 0.11 |
| The Stack - Selected Languages | 463.78 B | 0.1 | 100 B | 0.22 |
| RedPajama - Wikipedia - En | 4.87 B | 0.04 | 40 B | 8.21 |
| The Stack - Markdown | 107.07 B | 0.035 | 35 B | 0.33 |
| S2ORC | 48.85 B | 0.033 | 33 B | 0.68 |
| RedPajama - Books | 26.02 B | 0.03 | 30B | 1.15 |
| RedPajama - arXiv | 28.10 B | 0.019 | 19 B | 0.68 |
| RedPajama - StackExchange | 20.54 B | 0.014 | 14 B |0.68 |

#### Data Mix for Additional 500B Tokens Used to Further Train MPT-7B-8k

We took 80B tokens from document samples that were longer than 4096 tokens, and 120B tokens with varying document sample lengths that matched the "baseline" length distribution for a total of 200B tokens in a single dataset. 
We then trained MPT-7B for 500B tokens with a maximum sequence length of 8192, resulting in MPT-7B-8k. Since we trained for 500B tokens using 200B tokens, nearly every subset was trained on for exactly 2.5 epochs.

| Sequence Length Distribution | Number of Tokens in Source (Billion) | Proportion | Effective Number of Tokens (Billion) | Epochs |
|---|---|---|---|---|
| mC4 3.1.0 - English (200+ words) - Baseline | 33.60 | 16.80% | 84.00 | 2.50 |
| mC4 3.1.0 - English (200+ words) - ≥4096 tokens | 23.04 | 11.52% | 57.60 | 2.50 |
| c4 - English - SemDedup 80% - Baseline | 30.12 | 15.06% | 75.30 | 2.50 |
| c4 - English - SemDedup 80% - ≥4096 tokens | 0.92 | 0.46% | 2.30 | 2.50 |
| RedPajama - CommonCrawl - Baseline | 8.52 | 4.26% | 21.30 | 2.50 |
| RedPajama - CommonCrawl - ≥4096 tokens | 12.80 | 6.40% | 32.00 | 2.50 |
| The Stack - Selected Languages - Baseline | 30.00 | 15.00% | 75.00 | 2.50 |
| The Stack - Selected Languages - ≥4096 tokens | 10.00 | 5.00% | 25.00 | 2.50 |
| RedPajama - Wikipedia - Baseline | 3.60 | 1.80% | 9.00 | 2.50 |
| RedPajama - Wikipedia - ≥4096 tokens | 1.04 | 0.52% | 2.60 | 2.50 |
| The Stack - Markdown - Baseline | 4.50 | 2.25% | 11.25 | 2.50 |
| The Stack - Markdown - ≥4096 tokens | 8.00 | 4.00% | 20.00 | 2.50 |
| Semantic Scholar ORC - Baseline | 3.30 | 1.65% | 8.25 | 2.50 |
| Semantic Scholar ORC - ≥4096 tokens | 8.00 | 4.00% | 20.00 | 2.50 |
| RedPajama - Books - Baseline | 3.00 | 1.50% | 7.50 | 2.50 |
| RedPajama - Books - ≥4096 tokens | 8.00 | 4.00% | 20.00 | 2.50 |
| RedPajama - arXiv - Baseline | 1.92 | 0.96% | 4.80 | 2.50 |
| RedPajama - arXiv - ≥4096 tokens | 5.40 | 2.70% | 13.50 | 2.50 |
| RedPajama - StackExchange - Baseline | 1.44 | 0.72% | 3.60 | 2.50 |
| RedPajama - StackExchange - ≥4096 tokens | 1.52 | 1.40% | 7.00 | 4.60 |
| N Training Tokens | 200 | 100.00% | | 2.5 epochs * 200B = 500B tokens |



Samples for each batch were selected from one of the datasets with the probability specified above.
The examples were shuffled within each dataset, and each example was constructed from as many sequences from that dataset as were necessary to fill the 2048 sequence length.

The data was tokenized using the [EleutherAI/gpt-neox-20b](https://huggingface.co/EleutherAI/gpt-neox-20b) tokenizer. This BPE tokenizer has a number of desirable characteristics,
most of which are relevant for tokenizing code:
(1) It was trained on a diverse mix of data that includes code (The Pile)
(2) It applies consistent space delimitation, unlike the GPT2 tokenizer which tokenizes inconsistently depending on the presence of prefix spaces
(3) It contains tokens for repeated space characters, which allows superior compression of text with large amounts of repeated space characters.

The model vocabulary size of 50432 was set to be a multiple of 128 (as in [MEGATRON-LM](https://arxiv.org/abs/1909.08053)), model flop utilization (MFU) increased by up to four percentage points.

### Training Configuration

This model was trained on 440 A100-40GBs for about 9.5 days using the [MosaicML Platform](https://www.mosaicml.com/platform).
The model was trained with sharded data parallelism using [FSDP](https://pytorch.org/docs/stable/fsdp.html) and used the [LION](https://arxiv.org/abs/2302.06675) optimizer.

## Limitations and Biases

_The following language is modified from [EleutherAI's GPT-NeoX-20B](https://huggingface.co/EleutherAI/gpt-neox-20b)_

MPT-7B-8k is **not** intended for deployment without finetuning.
It should not be used for human-facing interactions without further guardrails and user consent.

MPT-7B-8k can produce factually incorrect output, and should not be relied on to produce factually accurate information.
MPT-7B-8k was trained on various public datasets.
While great efforts have been taken to clean the pretraining data, it is possible that this model could generate lewd, biased or otherwise offensive outputs.


## MosaicML Platform

If you're interested in [training](https://www.mosaicml.com/training) and [deploying](https://www.mosaicml.com/inference) your own MPT or LLMs on the MosaicML Platform, [sign up here](https://www.mosaicml.com/get-started?utm_source=huggingface&utm_medium=referral&utm_campaign=mpt-7b-8k).

## Disclaimer

The license on this model does not constitute legal advice. We are not responsible for the actions of third parties who use this model. Please cosult an attorney before using this model for commercial purposes.

## Citation

Please cite this model using the following format:

```
@online{MosaicML2023Introducing,
    author    = {MosaicML NLP Team},
    title     = {Introducing MPT-7B: A New Standard for Open-Source,
    ly Usable LLMs},
    year      = {2023},
    url       = {www.mosaicml.com/blog/mpt-7b},
    note      = {Accessed: 2023-03-28}, % change this date
    urldate   = {2023-03-28} % change this date
}
```
