
# Dolphin 2.9.1 Llama 3 8b 🐬

Curated and trained by Eric Hartford, Lucas Atkins, and Fernando Fernandes, and Cognitive Computations

[![Discord](https://img.shields.io/discord/1156064224225808488?logo=Discord&logoColor=%23ffffff&label=Discord&link=https%3A%2F%2Fdiscord.gg%2FtCMkMDDHwm)](https://discord.gg/cognitivecomputations)
Discord: https://discord.gg/cognitivecomputations

<img src="https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/ldkN1J0WIDQwU4vutGYiD.png" width="600" />

We have retrained our LLama-3-8b fine tune to address behavioral issues in the initial 2.9 dataset. Specifically, Systemchat was causing the model to be *too* reliant on the system prompt. Additionally, it had an occasional quirk that would cause the model to overly reference the system prompt. We also found generation length was at times not sufficient for any given task. We identified the culprit as Ultrachat. Accounting for these concerns, we removed systemchat and ultrachat from the dataset. It is otherwise identical to dolphin-2.9.

Our appreciation for the sponsors of Dolphin 2.9.1:
- [Crusoe Cloud](https://crusoe.ai/) - provided excellent on-demand 8xL40S node

This model is based on Llama-3-8b, and is governed by [META LLAMA 3 COMMUNITY LICENSE AGREEMENT](LICENSE)

The base model has 8k context, and the full-weight fine-tuning was with 4k sequence length.

It took 1.5 days on an 8x L40S provided by Crusoe Cloud

This model was trained FFT on all parameters, using ChatML prompt template format.

example:

```
<|im_start|>system
You are Dolphin, a helpful AI assistant.<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

```

Dolphin-2.9.1 has a variety of instruction, conversational, and coding skills. It also has initial agentic abilities and supports function calling.

Dolphin is uncensored. We have filtered the dataset to remove alignment and bias. This makes the model more compliant. You are advised to implement your own alignment layer before exposing the model as a service. It will be highly compliant with any requests, even unethical ones. Please read my blog post about uncensored models. https://erichartford.com/uncensored-models You are responsible for any content you create using this model. Enjoy responsibly.

Dolphin is licensed according to Meta's Llama license.  We grant permission for any use, including commercial, that falls within accordance with Meta's Llama-3 license.  Dolphin was trained on data generated from GPT4, among other models.

## Evals

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/0pqSc8jsJlhBH8dcgpwE7.png)

## Training

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

### Framework versions

- Transformers 4.40.0
- Pytorch 2.2.2+cu121
- Datasets 2.18.0
- Tokenizers 0.19.1