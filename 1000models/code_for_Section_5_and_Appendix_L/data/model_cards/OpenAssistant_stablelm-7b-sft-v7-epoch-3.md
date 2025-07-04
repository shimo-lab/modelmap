
# Open-Assistant StableLM-7B SFT-7 Model


This is the 7th iteration English supervised-fine-tuning (SFT) model of 
the [Open-Assistant](https://github.com/LAION-AI/Open-Assistant) project. 
It is based on a StableLM 7B that was fine-tuned on human demonstrations 
of assistant conversations collected through the 
[https://open-assistant.io/](https://open-assistant.io/) human feedback web 
app before April 12, 2023. 

## Model Details

- **Developed by:** [Open-Assistant Contributors](https://open-assistant.io/)
- **Model type:** Transformer-based Language Model
- **Language:** English
- **Finetuned from:** [stabilityai/stablelm-base-alpha-7b](https://huggingface.co/stabilityai/stablelm-base-alpha-7b)
- **Code:** [Open-Assistant/model/model_training](https://github.com/LAION-AI/Open-Assistant/tree/main/model/model_training)
- **Demo:** TODO
- **License:** Creative Commons license ([CC BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/))
- **Contact:** [Open-Assistant Discord](https://ykilcher.com/open-assistant-discord)

## Prompting

Two special tokens are used to mark the beginning of user and assistant turns:
`<|prompter|>` and `<|assistant|>`. Each turn ends with a `<|endoftext|>` token.

Input prompt example:
```
<|prompter|>What is a meme, and what's the history behind this word?<|endoftext|><|assistant|>
```
The input ends with the `<|assistant|>` token to signal that the model should 
start generating the assistant reply.


## Dev Details

- wandb: https://wandb.ai/open-assistant/supervised-finetuning/runs/08dfhyuc
- base model: [stabilityai/stablelm-base-alpha-7b](https://huggingface.co/stabilityai/stablelm-base-alpha-7b)
- checkpoint: 3 epochs (12000 steps)

command: `deepspeed trainer_sft.py --configs defaults stablelm-7b oasst-mix --cache_dir /home/ubuntu/data_cache --output_dir .saved/stable-lm-7b-1 --num_train_epochs 4 --deepspeed`

data:
```
oasst-mix:
  save_strategy: epoch
  sort_by_length: false
  use_custom_sampler: false
  datasets:
    - oasst_export:
        lang: "bg,ca,cs,da,de,en,es,fr,hr,hu,it,nl,pl,pt,ro,ru,sl,sr,sv,uk"
        input_file_path: 2023-04-12_oasst_release_ready_synth.jsonl.gz
    - vicuna:
        val_split: 0.05
        max_val_set: 800
        fraction: 1.0
    - dolly15k:
        val_split: 0.05
        max_val_set: 300
    - grade_school_math_instructions:
        val_split: 0.05
    - code_alpaca:
        val_split: 0.05
        max_val_set: 250
```


stablelm:
```
stablelm-7b:
  dtype: fp16
  log_dir: stablelm_log_7b
  model_name: stabilityai/stablelm-base-alpha-7b
  output_dir: stablelm_7b
  max_length: 4096
  warmup_steps: 100
  gradient_checkpointing: true
  gradient_accumulation_steps: 2
  per_device_train_batch_size: 4
  per_device_eval_batch_size: 4
  eval_steps: 100
  save_steps: 500
  num_train_epochs: 4
  save_total_limit: 4
  use_flash_attention: true
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
      "total_num_steps": "auto"
    }
  },
  "zero_optimization": {
    "stage": 2,
    "allgather_partitions": true,
    "allgather_bucket_size": 1e9,
    "overlap_comm": false,
    "reduce_scatter": true,
    "reduce_bucket_size": 1e9,
    "contiguous_gradients": true
  },
  "gradient_accumulation_steps": "auto",
  "gradient_clipping": "auto",
  "steps_per_print": 2000,
  "train_batch_size": "auto",
  "train_micro_batch_size_per_gpu": "auto",
  "wall_clock_breakdown": false
}
```