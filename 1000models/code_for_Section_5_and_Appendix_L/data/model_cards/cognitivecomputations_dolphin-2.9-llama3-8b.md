
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Dolphin 2.9 Llama 3 8b 🐬

Curated and trained by Eric Hartford, Lucas Atkins, and Fernando Fernandes, and Cognitive Computations

[![Discord](https://img.shields.io/discord/1156064224225808488?logo=Discord&logoColor=%23ffffff&label=Discord&link=https%3A%2F%2Fdiscord.gg%2FtCMkMDDHwm)](https://discord.gg/cognitivecomputations)
Discord: https://discord.gg/cognitivecomputations

<img src="https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/ldkN1J0WIDQwU4vutGYiD.png" width="600" />

A bug has been found in the Dolphin 2.9 dataset in SystemConversations that causes the model to overly talk about the "SYSTEM MESSAGE".  To counter this, we recommend you add a statement in the system message directing the model not to mention the system message. An example system message is "The assistant is named Dolphin.  A helpful and friendly AI assistant, Dolphin avoids discussing the system message unless directly asked about it."

My appreciation for the sponsors of Dolphin 2.9:
- [Crusoe Cloud](https://crusoe.ai/) - provided excellent on-demand 10xL40S node

This model is based on Llama-3-8b, and is governed by [META LLAMA 3 COMMUNITY LICENSE AGREEMENT](LICENSE)

The base model has 8k context, and the full-weight fine-tuning was with 4k sequence length.

It took 2.5 days on 8x L40S provided by Crusoe Cloud

This model was trained FFT on all parameters, using ChatML prompt template format.

example:

```
<|im_start|>system
You are Dolphin, a helpful AI assistant.<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

```

Dolphin-2.9 has a variety of instruction, conversational, and coding skills. It also has initial agentic abilities and supports function calling.

Dolphin is uncensored. I have filtered the dataset to remove alignment and bias. This makes the model more compliant. You are advised to implement your own alignment layer before exposing the model as a service. It will be highly compliant with any requests, even unethical ones. Please read my blog post about uncensored models. https://erichartford.com/uncensored-models You are responsible for any content you create using this model. Enjoy responsibly.

Dolphin is licensed according to Meta's Llama license.  I grant permission for any use, including commercial, that falls within accordance with Meta's Llama-3 license.  Dolphin was trained on data generated from GPT4, among other models.

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
<details><summary>See axolotl config</summary>

axolotl version: `0.4.0`
```yaml
base_model: meta-llama/Meta-Llama-3-8B
model_type: AutoModelForCausalLM
tokenizer_type: AutoTokenizer
tokenizer_use_fast: false


load_in_8bit: false
load_in_4bit: false
strict: false
model_config:

datasets:
  - path: /workspace/datasets/dolphin-2.9/dolphin201-sharegpt2.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9/Ultrachat200kunfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9/dolphin-coder-translate-sharegpt2.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9/dolphin-coder-codegen-sharegpt2.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9/m-a-p_Code-Feedback-sharegpt-unfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9/m-a-p_CodeFeedback-Filtered-Instruction-sharegpt-unfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9/not_samantha_norefusals.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9/Orca-Math-resort-unfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9/agent_instruct_react_unfiltered.jsonl
    type: sharegpt  
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9/toolbench_instruct_j1s1_3k_unfiltered.jsonl
    type: sharegpt  
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9/toolbench_negative_unfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9/toolbench_react_10p_unfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9/toolbench_tflan_cot_30p_unfiltered.jsonl
    type: sharegpt
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9/openhermes200k_unfiltered.jsonl
    type: sharegpt 
    conversation: chatml
  - path: /workspace/datasets/dolphin-2.9/SystemConversations.jsonl
    type: sharegpt
    conversation: chatml

chat_template: chatml
    

dataset_prepared_path: /workspace/datasets/dolphin-2.9/thingy
val_set_size: 0.0002
output_dir: ./out

sequence_len: 4096
sample_packing: true
pad_to_sequence_len: true

gradient_accumulation_steps: 4
micro_batch_size: 3
num_epochs: 3
logging_steps: 1
optimizer: adamw_8bit
lr_scheduler: cosine
learning_rate: 2e-5

wandb_project: dolphin-2.9-mixtral-8x22b
wandb_watch:
wandb_run_id:
wandb_log_model:

train_on_inputs: false
group_by_length: false
bf16: auto
fp16:
tf32: false

gradient_checkpointing: true
gradient_checkpointing_kwargs:
  use_reentrant: false
early_stopping_patience:
resume_from_checkpoint:
local_rank:
logging_steps: 1
xformers_attention:
flash_attention: true
saves_per_epoch: 4
save_total_limit: 2
save_steps:
evals_per_epoch: 4
eval_sample_packing: false
debug:
deepspeed: deepspeed_configs/zero3_bf16.json
weight_decay: 0.05
fsdp:
fsdp_config:
special_tokens:
  eos_token: "<|im_end|>"
  pad_token: "<|end_of_text|>"
tokens:
  - "<|im_start|>"
  - "<|im_end|>"

```

</details><br>

## Quants

GGUF : https://huggingface.co/QuantFactory/dolphin-2.9-llama3-8b-GGUF

GGUF with imatrix: https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF

Exllamav2: https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-exl2

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 3
- eval_batch_size: 3
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 4
- total_train_batch_size: 96
- total_eval_batch_size: 24
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 7
- num_epochs: 3

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 1.146         | 0.0005 | 1    | 1.1064          |
| 0.6962        | 0.2501 | 555  | 0.6636          |
| 0.6857        | 0.5001 | 1110 | 0.6503          |
| 0.6592        | 0.7502 | 1665 | 0.6419          |
| 0.6465        | 1.0002 | 2220 | 0.6317          |
| 0.5295        | 1.2395 | 2775 | 0.6408          |
| 0.5302        | 1.4895 | 3330 | 0.6351          |
| 0.5188        | 1.7396 | 3885 | 0.6227          |
| 0.521         | 1.9896 | 4440 | 0.6168          |
| 0.3968        | 2.2289 | 4995 | 0.6646          |
| 0.3776        | 2.4789 | 5550 | 0.6619          |
| 0.3983        | 2.7290 | 6105 | 0.6602          |


### Framework versions

- Transformers 4.40.0
- Pytorch 2.2.2+cu121
- Datasets 2.18.0
- Tokenizers 0.19.1