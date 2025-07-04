
# MPT-7B-Chat

MPT-7B-Chat is a chatbot-like model for dialogue generation.
It was built by finetuning [MPT-7B](https://huggingface.co/mosaicml/mpt-7b) on the [ShareGPT-Vicuna](https://huggingface.co/datasets/jeffwan/sharegpt_vicuna), [HC3](https://huggingface.co/datasets/Hello-SimpleAI/HC3),
 [Alpaca](https://huggingface.co/datasets/tatsu-lab/alpaca), [HH-RLHF](https://huggingface.co/datasets/Anthropic/hh-rlhf), and [Evol-Instruct](https://huggingface.co/datasets/victor123/evol_instruct_70k) datasets.
  * License: _CC-By-NC-SA-4.0_ (non-commercial use only)
  * [Demo on Hugging Face Spaces](https://huggingface.co/spaces/mosaicml/mpt-7b-chat)


This model was trained by [MosaicML](https://www.mosaicml.com) and follows a modified decoder-only transformer architecture.

## Model Date

May 5, 2023

## Model License

_CC-By-NC-SA-4.0_ (non-commercial use only)

## Documentation

* [Blog post: Introducing MPT-7B: A New Standard for Open-Source, Commercially Usable LLMs](https://www.mosaicml.com/blog/mpt-7b)
* [Codebase (mosaicml/llm-foundry repo)](https://github.com/mosaicml/llm-foundry/)
* Questions: Feel free to contact us via the [MosaicML Community Slack](https://mosaicml.me/slack)!

### Example Dialogue

**SamIAm85**:
>I want you to come up with a tweet based on this summary of the article:
>"Introducing MPT-7B, the latest entry in our MosaicML Foundation Series.
>MPT-7B is a transformer trained from scratch on IT tokens of text and code.
>It is open source and it matches the quality of LLaMA-7B.
>MPT-7B was trained on the MosaicML platform in 9.5 days with zero human intervention at a cost of ~$200k.
>Starting today, you can train, finetune, and deploy your own private MPT models, either starting from one of our checkpoints or training from scratch.
>For inspiration, we are also releasing three finetuned models in addition to the base MPT-7B: MPT-7B-Instruct, MPT-7B-Chat, and MPT-7B-Story Writer-65k+, the last of which uses a context length of 65k tokens!

**MPT-7B-Instruct**:
>Here's my suggestion for a tweet:
>"Exciting news! @MosaicML has launched #MPT_7B - a new standard for open-source LLMs. With training on 17 tokens of text & code, it matches the quality of LLaMA-7B. Now you can train, fine-tune, and deploy your own private MPT models via their platform. Check out the full blog post here: https://bit.ly/3j6UJzZ"

**SamIAm85**:
>Is there anything you want to say to MosaicML about this exciting news?

**MPT-7B-Instruct**:
> As an Al language model myself, I am very impressed with the advancements made by MosaicML in developing such high-quality open-source LLMs.
> This new version of MPT-7B is truly impressive and I look forward to seeing what innovative applications developers will create using these powerful tools.
> Thank you for your hard work and dedication to advancing Al research and development.

## How to Use

This model is best used with the MosaicML [llm-foundry repository](https://github.com/mosaicml/llm-foundry) for training and finetuning.

```python
import transformers
model = transformers.AutoModelForCausalLM.from_pretrained(
  'mosaicml/mpt-7b-chat',
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

name = 'mosaicml/mpt-7b-chat'

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

name = 'mosaicml/mpt-7b-chat'

config = transformers.AutoConfig.from_pretrained(name, trust_remote_code=True)
config.max_seq_len = 4096 # (input + output) tokens can now be up to 4096

model = transformers.AutoModelForCausalLM.from_pretrained(
  name,
  config=config,
  trust_remote_code=True
)
```

This model was trained with the [EleutherAI/gpt-neox-20b](https://huggingface.co/EleutherAI/gpt-neox-20b) tokenizer.

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neox-20b")
```

The model can then be used, for example, within a text-generation pipeline.  
Note: when running Torch modules in lower precision, it is best practice to use the [torch.autocast context manager](https://pytorch.org/docs/stable/amp.html).

```python
from transformers import pipeline

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

### Training Configuration

This model was trained on 8 A100-80GBs for about 8.2 hours, followed by training for 6.7 hours on 32 A100-40GBs using the [MosaicML Platform](https://www.mosaicml.com/platform).
The model was trained with sharded data parallelism using [FSDP](https://pytorch.org/docs/stable/fsdp.html) and used the AdamW optimizer.

## Limitations and Biases

_The following language is modified from [EleutherAI's GPT-NeoX-20B](https://huggingface.co/EleutherAI/gpt-neox-20b)_

MPT-7B-Chat can produce factually incorrect output, and should not be relied on to produce factually accurate information.
MPT-7B-Chat was trained on various public datasets.
While great efforts have been taken to clean the pretraining data, it is possible that this model could generate lewd, biased or otherwise offensive outputs.

## Acknowledgements

This model was finetuned by Sam Havens and the MosaicML NLP team

## Disclaimer

The license on this model does not constitute legal advice. We are not responsible for the actions of third parties who use this model. Please cosult an attorney before using this model for commercial purposes.


## MosaicML Platform

If you're interested in [training](https://www.mosaicml.com/training) and [deploying](https://www.mosaicml.com/inference) your own MPT or LLMs on the MosaicML Platform, [sign up here](https://forms.mosaicml.com/demo?utm_source=huggingface&utm_medium=referral&utm_campaign=mpt-7b).


## Citation

Please cite this model using the following format:

```
@online{MosaicML2023Introducing,
    author    = {MosaicML NLP Team},
    title     = {Introducing MPT-7B: A New Standard for Open-Source, Commercially Usable LLMs},
    year      = {2023},
    url       = {www.mosaicml.com/blog/mpt-7b},
    note      = {Accessed: 2023-03-28}, % change this date
    urldate   = {2023-03-28} % change this date
}
```
