# llama2-13b-orca-8k-3319

## Model Description

This model is a fine-tuning of Meta's Llama2 13B model with 8K context size on a long-conversation variant of the Dolphin dataset ([orca-chat](https://huggingface.co/datasets/shahules786/orca-chat)).

Note: **At least Huggingface Transformers [4.31.0](https://pypi.org/project/transformers/4.31.0/) is required to load this model!**


## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("OpenAssistant/llama2-13b-orca-8k-3319", use_fast=False)
model = AutoModelForCausalLM.from_pretrained("OpenAssistant/llama2-13b-orca-8k-3319", torch_dtype=torch.float16, low_cpu_mem_usage=True, device_map="auto")

system_message = "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."
user_prompt = "Write me a poem please"
prompt = f"""<|system|>{system_message}</s><|prompter|>{user_prompt}</s><|assistant|>"""
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
output = model.generate(**inputs, do_sample=True, top_p=0.95, top_k=0, max_new_tokens=256)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

## Model Details

- base model: [meta-llama/Llama-2-13b](https://huggingface.co/meta-llama/Llama-2-13b)
- License: [Llama 2 Community License Agreement](https://ai.meta.com/resources/models-and-libraries/llama-downloads/)
- sampling report: [2023-07-25_OpenAssistant_llama2-13b-orca-8k-3319_sampling_llama2_prompt.json](https://open-assistant.github.io/oasst-model-eval/?f=https%3A%2F%2Fraw.githubusercontent.com%2FOpen-Assistant%2Foasst-model-eval%2Fmain%2Fsampling_reports%2Foasst-pretrained%2F2023-07-25_OpenAssistant_llama2-13b-orca-8k-3319_sampling_llama2_prompt.json)
- wandb: [public-sft/runs/2jfazjt9](https://wandb.ai/open-assistant/public-sft/runs/2jfazjt9)
- checkpoint: 3319 steps
- datatpye: fp16
- sponsored by: [Redmond.ai](https://redmond.ai/)

## Long context (RoPE Scaling)

This model was fine-tuned with a context size of 8192 tokens using linear scaling of RoPE embeddings. This feature was recently
added to [Huggingface transformers](https://github.com/huggingface/transformers/). Before loading this model please make sure
HF transformers >=4.31.0 is installed (`pip install transformers>=4.31.0`).

## Conversation Template

For the initial response use (e.g. the [llama2 default system prompt](https://github.com/facebookresearch/llama/blob/6c7fe276574e78057f917549435a2554000a876d/llama/generation.py#L46) works well):

```
<|system|>system message</s><|prompter|>user prompt</s><|assistant|>
```

For multi-turn conversations use:

```
<|system|>system message</s><|prompter|>Q1</s><|assistant|>A1</s><|prompter|>Q2</s><|assistant|>
```

The model was trained with the following 15 system messages used to generate the training examples (see [ORCA paper](https://arxiv.org/abs/2306.02707)):

1. You are an AI assistant. Provide a detailed answer so user don’t need to search outside to understand the answer.
2. You are an AI assistant. You will be given a task. You must generate a detailed and long answer.
3. You are a helpful assistant, who always provide explanation. Think like you are answering to a five year old.
4. You are an AI assistant that follows instruction extremely well. Help as much as you can.
5. You are an AI assistant that helps people find information. Provide a detailed answer so user don’t need to search outside to understand the answer.
6. You are an AI assistant. User will you give you a task. Your goal is to complete the task as faithfully as you can. While performing the task think step-by-step and justify your steps.
7. You should describe the task and explain your answer. While answering a multiple choice question, first output the correct answer(s). Then explain why other answers are wrong. Think like you are answering to a five year old.
8. Explain how you used the definition to come up with the answer.
9. You are an AI assistant. You should describe the task and explain your answer. While answering a multiple choice question, first output the correct answer(s). Then explain why other answers are wrong. You might need to use additional knowledge to answer the question.
10. You are an AI assistant that helps people find information. User will you give you a question. Your task is to answer as faithfully as you can. While answering think step-by- step and justify your answer.
11. User will you give you a task with some instruction. Your job is follow the instructions as faithfully as you can. While answering think step-by-step and justify your answer.
12. You are a teacher. Given a task, you explain in simple steps what the task is asking, any guidelines it provides and how to use those guidelines to find the answer.
13. You are an AI assistant, who knows every language and how to translate one language to another. Given a task, you explain in simple steps what the task is asking, any guidelines that it provides. You solve the task and show how you used the guidelines to solve the task.
14. Given a definition of a task and a sample input, break the definition into small parts. Each of those parts will have some instruction. Explain their meaning by showing an example that meets the criteria in the instruction. Use the following format: Part \#: a key part of the definition. Usage: Sample response that meets the criteria from the key part. Explain why you think it meets the criteria.
15. You are an AI assistant that helps people find information.


## Datasets: Orca-Chat/Dolphin, RedPajama1T & FanFics

This model was trained on:

- [shahules786/orca-chat](https://huggingface.co/datasets/shahules786/orca-chat)
- [togethercomputer/RedPajama-Data-1T-Sample](https://huggingface.co/datasets/togethercomputer/RedPajama-Data-1T)
- [atom-in-the-universe/fanfics-10k-50k](https://huggingface.co/datasets/atom-in-the-universe/fanfics-10k-50k)

```
Dataset Composition:
    Tain (sampled):
       orca-chat: 188842 (100%)
       fanfics: 47760 (100%)
       red_pajama: 188262 (25%)
    Valid:
       orca-chat: 5000
       fanfics: 1000
       red_pajama: 1000
```
  
The dataset [shahules786/orca-chat](https://huggingface.co/datasets/shahules786/orca-chat) combines similar examples of the GPT-4 subset of [ehartford/dolphin](https://huggingface.co/datasets/ehartford/dolphin) to form longer conversations 
to improve long-context training.

Additionally, RedPajama and FanFics were used for classic language modelling as an auxiliary task to improve the RoPE scaling for the 8k context size.


## Model Configuration
```
llama2_13b_orca_8k:
  rng_seed: 0xe1291f1a
  use_custom_sampler: true
  sort_by_length: false
  dtype: fp16
  log_dir: "llama2_log_13b_orca_8k"
  learning_rate: 1e-5
  model_name: /mnt/data/llama2/Llama-2-13b-hf/
  output_dir: llama2_13b_orca_8k
  deepspeed_config: configs/zero_config_pretrain.json
  weight_decay: 0.0
  max_length: 8192
  warmup_steps: 100
  use_flash_attention: true
  gradient_checkpointing: true
  gradient_accumulation_steps: 8
  per_device_train_batch_size: 2
  per_device_eval_batch_size: 1
  residual_dropout: 0.0
  eval_steps: 200
  save_steps: 1000  # (total steps: 3319)
  num_train_epochs: 1
  save_total_limit: 4
  superhot: true
  superhot_config:
    type: linear
    scale: 2
  datasets:
    - orca-chat:
        max_val_set: 5000
    - fanfics:
        max_chunk_size: 65535
        max_val_set: 1000
    - red_pajama:
        fraction: 0.25
        max_val_set: 1000
        max_chunk_size: 65535
  peft_model: false
```

# Developers

- [shahules786](https://github.com/shahules786)
- [jordiclive](https://github.com/jordiclive)
- [andreaskoepf](https://github.com/andreaskoepf/)

# Special Thanks

We want to especially thank Eric Hartford who spared no expense in replicating ORCA and making it available at [ehartford/dolphin](https://huggingface.co/datasets/ehartford/dolphin)!
Also, shoutout to the whole team working on [LLongMA-2-13b](https://huggingface.co/conceptofmind/LLongMA-2-13b) & the [scaled-rope](https://github.com/jquesnelle/scaled-rope) repository for their awesome work: bloc97, jquesnelle & conceptofmind!

The whole Open-Assistant team is very grateful for the continued support of [Redmond.ai](https://redmond.ai/) who sponsored the training compute required for this model.

# License

- Llama 2 is licensed under the LLAMA 2 Community License, Copyright © Meta Platforms, Inc. All Rights Reserved.
- Your use of the Llama Materials must comply with applicable laws and regulations (including trade compliance laws and regulations) and adhere to the [Acceptable Use Policy](https://ai.meta.com/llama/use-policy) for the Llama Materials.