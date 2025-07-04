
# Bloom-3B SFT model

![conversation example](https://huggingface.co/ikala/bloom-zh-3b-chat/resolve/main/bloom-chat-example.png)

It is based on a Bloom-zh's 3B that was fine-tuned on human demonstrations 
of assistant conversations collected through the 
[https://open-assistant.io/](https://open-assistant.io/) human feedback web 
app before April 12, 2023. 

supervised finetune on sequence length of 5120

## Model Details

- **Developed by:** [Open-Assistant Contributors](https://open-assistant.io/team) and [iKala](https://ikala.ai/)
- **Model type:** Transformer-based Language Model
- **Language:** English, Chinese, Japanese
- **Finetuned from:** [ckip-joint/bloom-3b-zh](https://huggingface.co/ckip-joint/bloom-3b-zh)
- **Code:** [Open-Assistant/model/model_training](https://github.com/LAION-AI/Open-Assistant/tree/main/model/model_training)
- **License:** MEDIATEK RESEARCH License ([link](https://huggingface.co/ckip-joint/bloom-3b-zh/blob/main/LICENSE_MR.md)) and RAIL License v1.0 ([link](https://huggingface.co/spaces/bigscience/license)), Non commercial

## Prompting

Two special tokens are used to mark the beginning of user and assistant turns:
`<|prompter|>` and `<|assistant|>`. Each turn ends with a `</s>` token.

Input prompt example:
```
<|prompter|>What is a meme, and what's the history behind this word?</s><|assistant|>
```
The input ends with the `<|assistant|>` token to signal that the model should 
start generating the assistant reply.

## Benchmark


| model  | MMLU  | BBH  | Humaneval @10  |
|---|---|---|---|
| [ikala/redpajama-3b-chat](https://huggingface.co/ikala/redpajama-3b-chat)  |  24.6 | 29.3  |  4.8 |
| [ikala/bloom-zh-3b-chat](https://huggingface.co/ikala/bloom-zh-3b-chat)  | 31.4  | 30.2  | 0.0  |
| llama-7b (reference)  | 30.9  |  27.6 |  10.3 |

## Dev Details

- base model: [ckip-joint/bloom-3b-zh](https://huggingface.co/ckip-joint/bloom-3b-zh)
- checkpoint: 1 epoch (6000 steps)
- hardware: NVIDIA RTX A6000 x 4

command: `deepspeed trainer_sft.py --configs defaults bloom-zh-3b datasets --num_train_epochs 2 --deepspeed`

data:
```
datasets:
  - wmt2019_zh-en:
      max_val_set: 1000
      max_train_set: 20000
  - ted_trans_en-ja:
      max_val_set: 1000
      max_train_set: 20000
  - ted_trans_zh-ja:
      max_val_set: 1000
      max_train_set: 20000
  - ikala:
      input_file_path: export_conversation_v4.4.jsonl
      val_split: 0.05
  - dolly15k:
      val_split: 0.05
  - oasst_export:
      lang: "bg,ca,cs,da,de,en,es,fr,hr,hu,it,nl,pl,pt,ro,ru,sl,sr,sv,uk,zh,ja,th,ko"
      input_file_path: 2023-04-12_oasst_release_ready_synth.jsonl.gz
      val_split: 0.05
  - joke
  - gsm8k
  - webgpt
```

with internal datasets `ikala` so if you try to reproduce please remove the dataset

bloom-zh-3b:
```
bloom-zh-3b:
  dtype: fp16
  log_dir: "bloom-zh_3b"
  learning_rate: 8e-6
  model_name: ckip-joint/bloom-3b-zh
  output_dir: bloom_model_v4_3b
  weight_decay: 0.0
  max_length: 5120
  warmup_steps: 2000
  gradient_checkpointing: true
  gradient_accumulation_steps: 32
  per_device_train_batch_size: 1
  per_device_eval_batch_size: 1
  eval_steps: 500
  save_steps: 1000
  num_train_epochs: 8
  save_total_limit: 2
  deepspeed_config: configs/zero3_config_sft.json
```

zero config:
```
{
  "fp16": {
    "enabled": "auto",
    "loss_scale": 0,
    "loss_scale_window": 1000,
    "initial_scale_power": 16,
    "hysteresis": 2,
    "min_loss_scale": 1
  },
  "bf16": {
    "enabled": "auto"
  },
  "optimizer": {
    "type": "AdamW",
    "params": {
      "lr": "auto",
      "betas": "auto",
      "eps": "auto",
      "weight_decay": "auto"
    }
  },
  "scheduler": {
    "type": "WarmupDecayLR",
    "params": {
      "warmup_min_lr": "auto",
      "warmup_max_lr": "auto",
      "warmup_num_steps": "auto",
      "warmup_type": "linear",
      "total_num_steps": "auto"
    }
  },
  "zero_optimization": {
    "stage": 3,
    "overlap_comm": true,
    "contiguous_gradients": true,
    "sub_group_size": 1e9,
    "reduce_bucket_size": "auto",
    "stage3_prefetch_bucket_size": "auto",
    "stage3_param_persistence_threshold": "auto",
    "stage3_max_live_parameters": 1e9,
    "stage3_max_reuse_distance": 1e9,
    "stage3_gather_16bit_weights_on_model_save": true
  },
  "gradient_accumulation_steps": "auto",
  "gradient_clipping": "auto",
  "steps_per_print": 2000,
  "train_batch_size": "auto",
  "train_micro_batch_size_per_gpu": "auto",
  "wall_clock_breakdown": false
}

```
