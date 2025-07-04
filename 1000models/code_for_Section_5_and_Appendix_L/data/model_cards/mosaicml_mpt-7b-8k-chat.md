
# MPT-7B-Chat-8k

MPT-7B-Chat-8k is a chatbot-like model for dialogue generation.
It was built by finetuning [MPT-7B-8k](https://huggingface.co/mosaicml/mpt-7b-8k) on the [ShareGPT-Vicuna](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered), [Camel-AI](https://huggingface.co/camel-ai),
 [GPTeacher](https://github.com/teknium1/GPTeacher), [Guanaco](https://huggingface.co/datasets/timdettmers/openassistant-guanaco), [Baize](https://github.com/project-baize/baize-chatbot) and some generated datasets.
 This is the same dataset that [MPT-30B-Chat](https://huggingface.co/mosaicml/mpt-30b-chat) was trained on.
  * License: _CC-By-NC-SA-4.0_ (non-commercial use only)

This model was trained by [MosaicML](https://www.mosaicml.com) and follows a modified decoder-only transformer architecture.

## Model Date

July 18, 2023

## Model License

_CC-By-NC-SA-4.0_ (non-commercial use only)

## Documentation

* [Blog post: MPT-7B-8k](https://www.mosaicml.com/blog/long-context-mpt-7b-8k)
* [Codebase (mosaicml/llm-foundry repo)](https://github.com/mosaicml/llm-foundry/)
* Questions: Feel free to contact us via the [MosaicML Community Slack](https://mosaicml.me/slack)!

## How to Use

This model is best used with the MosaicML [llm-foundry repository](https://github.com/mosaicml/llm-foundry) for training and finetuning.

```python
import transformers
model = transformers.AutoModelForCausalLM.from_pretrained(
  'mosaicml/mpt-7b-chat-8k',
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

name = 'mosaicml/mpt-7b-chat-8k'

config = transformers.AutoConfig.from_pretrained(name, trust_remote_code=True)
config.attn_config['attn_impl'] = 'triton'  # change this to use triton-based FlashAttention
config.init_device = 'cuda:0' # For fast initialization directly on GPU!

model = transformers.AutoModelForCausalLM.from_pretrained(
  name,
  config=config,
  torch_dtype=torch.bfloat16, # Load model weights in bfloat16
  trust_remote_code=True
)
```

The model was trained initially with a sequence length of 2048 with an additional pretraining stage for sequence length adapation up to 8192. However, ALiBi enables users to increase the maximum sequence length even further during finetuning and/or inference. For example:

```python
import transformers

name = 'mosaicml/mpt-7b-chat-8k'

config = transformers.AutoConfig.from_pretrained(name, trust_remote_code=True)
config.max_seq_len = 16384 # (input + output) tokens can now be up to 16384

model = transformers.AutoModelForCausalLM.from_pretrained(
  name,
  config=config,
  trust_remote_code=True
)
```

This model was trained with the MPT-7B-chat tokenizer which is based on the [EleutherAI/gpt-neox-20b](https://huggingface.co/EleutherAI/gpt-neox-20b) tokenizer and includes additional ChatML tokens.

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

## Data Mix

The model was trained on the following data mix:

| Data Source | Number of Tokens in Source | Proportion | 
|-------------|----------------------------|------------|
| Airoboros/GPT4-1.2 | 26.4M | 1.71% |
| Baize | 55.0M | 3.57% |
| Camel	| 301M | 19.54% | 
| GPTeacher	| 7.56M | 0.49% | 
| Guanaco | 15.6M | 1.02% | 
| LongCoversations | 18.4M | 1.19% | 
| ShareGPT | 821M | 53.24% |
| WizardLM | 297M | 19.23% |

"LongConversations" is a GPT3.5/4-generated dataset, details of which will be released at a later date.

### Training Configuration

This model was trained on 192 H100s for about 48 minutes using the [MosaicML Platform](https://www.mosaicml.com/platform).
The model was trained with sharded data parallelism using [FSDP](https://pytorch.org/docs/stable/fsdp.html) and used the AdamW optimizer.

## Limitations and Biases

_The following language is modified from [EleutherAI's GPT-NeoX-20B](https://huggingface.co/EleutherAI/gpt-neox-20b)_

MPT-7B-Chat-8k can produce factually incorrect output, and should not be relied on to produce factually accurate information.
MPT-7B-Chat-8k was trained on various public datasets.
While great efforts have been taken to clean the pretraining data, it is possible that this model could generate lewd, biased or otherwise offensive outputs.

## Acknowledgements

This model was finetuned by the MosaicML NLP team

## Disclaimer

The license on this model does not constitute legal advice. We are not responsible for the actions of third parties who use this model. Please consult an attorney before using this model for commercial purposes.


## MosaicML Platform

If you're interested in [training](https://www.mosaicml.com/training) and [deploying](https://www.mosaicml.com/inference) your own MPT or LLMs on the MosaicML Platform, [sign up here](https://www.mosaicml.com/get-started?utm_source=huggingface&utm_medium=referral&utm_campaign=mpt-7b-8k).


## Citation

Please cite this model using the following format:

```
@online{MosaicML2023Introducing,
    author    = {MosaicML NLP Team},
    title     = {Introducing MPT-30B: Raising the bar
for open-source foundation models},
    year      = {2023},
    url       = {www.mosaicml.com/blog/mpt-30b},
    note      = {Accessed: 2023-06-22},
    urldate   = {2023-06-22}
}
```