
# Dolphin 2.9.1 Yi 1.5 9b 🐬

Curated and trained by Eric Hartford, Lucas Atkins, and Fernando Fernandes, and Cognitive Computations

This is our most spectacular outcome ever. FFT, all parameters, 16bit.  70.9 MMLU on 9b!  And it talks like a dream.

Although the max positional embeddings is 4k, we used rope theta of 1000000.0 and we trained with sequence length 12k.  We plan to train on the upcoming 32k version as well.

[![Discord](https://img.shields.io/discord/1156064224225808488?logo=Discord&logoColor=%23ffffff&label=Discord&link=https%3A%2F%2Fdiscord.gg%2FtCMkMDDHwm)](https://discord.gg/cognitivecomputations)
Discord: https://discord.gg/cognitivecomputations

<img src="https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/ldkN1J0WIDQwU4vutGYiD.png" width="600" />

Our appreciation for the sponsors of Dolphin 2.9.1:
- [Crusoe Cloud](https://crusoe.ai/) - provided excellent on-demand 8xH100 node
- [OnDemand](https://on-demand.io/) - provided inference sponsorship

This model is based on Yi-1.5-9b, and is governed by apache 2.0 license.

The base model has 4k context, but we used rope theta of 1000000.0 and the full-weight fine-tuning was with 12k sequence length.

Dolphin 2.9.1 uses ChatML prompt template format.

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

Dolphin is licensed according to apache 2.0 license.  We grant permission for any use, including commercial. Dolphin was trained on data generated from GPT4, among other models.

## Evals

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/tF9uD2W2yWODNdc--P68I.png)

## Training

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
<details><summary>See axolotl config</summary>

axolotl version: `0.4.0`
```yaml
base_model: 01-ai/Yi-1.5-9B
model_type: LlamaForCausalLM
tokenizer_type: LlamaTokenizer
trust_remote_code: true

# load_in_8bit: false
# load_in_4bit: true
# strict: false

# adapter: qlora
# lora_modules_to_save: [embed_tokens, lm_head]

# lora_r: 32
# lora_alpha: 16
# lora_dropout: 0.05
# lora_target_linear: True
# lora_fan_in_fan_out:

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

dataset_prepared_path: yi34b
val_set_size: 0.03
output_dir: ./out-yi

sequence_len: 12000
sample_packing: true
pad_to_sequence_len: true

wandb_project: dolphin-2.9-yi-34b
wandb_watch:
wandb_run_id:
wandb_log_model:

gradient_accumulation_steps: 8
micro_batch_size: 2
num_epochs: 3
optimizer: adamw_8bit
lr_scheduler: cosine
learning_rate: 1e-5

train_on_inputs: false
group_by_length: false
bf16: auto
fp16:
tf32: true

gradient_checkpointing: true
gradient_checkpointing_kwargs:
  use_reentrant: false
early_stopping_patience:
# resume_from_checkpoint: /workspace/axolotl/dbrx-checkpoint
logging_steps: 1
xformers_attention:
flash_attention: true

warmup_steps: 10
evals_per_epoch: 4
eval_table_size:
saves_per_epoch: 4
save_total_limit: 2
save_steps:
debug:
deepspeed: /workspace/axolotl/deepspeed_configs/zero3_bf16.json
weight_decay: 0.05
fsdp:
fsdp_config:
special_tokens:
  bos_token: "<|startoftext|>"
  eos_token: "<|im_end|>"
  pad_token: "<unk>"
  unk_token: "<unk>"
tokens:
  - "<|im_start|>"
  

```

</details><br>

# out-yi

This model is a fine-tuned version of [01-ai/Yi-1.5-9B](https://huggingface.co/01-ai/Yi-1.5-9B) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4396

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 8
- total_train_batch_size: 128
- total_eval_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 10
- num_epochs: 3

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 0.6332        | 0.0024 | 1    | 0.6469          |
| 0.4811        | 0.2499 | 106  | 0.4739          |
| 0.4465        | 0.4997 | 212  | 0.4547          |
| 0.4472        | 0.7496 | 318  | 0.4480          |
| 0.4373        | 0.9994 | 424  | 0.4429          |
| 0.4147        | 1.2384 | 530  | 0.4432          |
| 0.3879        | 1.4882 | 636  | 0.4400          |
| 0.3872        | 1.7381 | 742  | 0.4371          |
| 0.4044        | 1.9879 | 848  | 0.4344          |
| 0.3509        | 2.2269 | 954  | 0.4410          |
| 0.3628        | 2.4767 | 1060 | 0.4401          |
| 0.3652        | 2.7266 | 1166 | 0.4397          |
| 0.3674        | 2.9764 | 1272 | 0.4396          |


### Framework versions

- Transformers 4.40.2
- Pytorch 2.2.2+cu121
- Datasets 2.15.0
- Tokenizers 0.19.1
