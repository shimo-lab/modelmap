
# Open-Assistant SFT-4 12B Model


This is the 4th iteration English supervised-fine-tuning (SFT) model of 
the [Open-Assistant](https://github.com/LAION-AI/Open-Assistant) project. 
It is based on a Pythia 12B that was fine-tuned on human demonstrations 
of assistant conversations collected through the 
[https://open-assistant.io/](https://open-assistant.io/) human feedback web 
app before March 25, 2023. 

## Model Details

- **Developed by:** [Open-Assistant Contributors](https://open-assistant.io/)
- **Model type:** Transformer-based Language Model
- **Language:** English
- **Finetuned from:** [EleutherAI / pythia-12b-deduped](https://huggingface.co/EleutherAI/pythia-12b-deduped)
- **Code:** [Open-Assistant/model/model_training](https://github.com/LAION-AI/Open-Assistant/tree/main/model/model_training)
- **Demo:** [Continuations for 250 random prompts](https://open-assistant.github.io/oasst-model-eval/?f=https%3A%2F%2Fraw.githubusercontent.com%2FOpen-Assistant%2Foasst-model-eval%2Fmain%2Fsampling_reports%2Foasst-sft%2F2023-04-03_andreaskoepf_oasst-sft-4-pythia-12b-epoch-3_5_sampling_noprefix_lottery.json%0Ahttps%3A%2F%2Fraw.githubusercontent.com%2FOpen-Assistant%2Foasst-model-eval%2Fmain%2Fsampling_reports%2Fchat-gpt%2F2023-04-11_gpt-3.5-turbo_lottery.json)
- **License:** Apache 2.0
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

- wandb: https://wandb.ai/open-assistant/supervised-finetuning/runs/770a0t41
- base model: [andreaskoepf/pythia-12b-pre-2000](https://huggingface.co/andreaskoepf/pythia-12b-pre-2000)
- checkpoint: 4000 steps

command: `deepspeed trainer_sft.py --configs defaults reference-data reference-pythia-12b --cache_dir /home/ubuntu/data_cache --output_dir .saved/oasst-sft-3-pythia-12b-reference_2kpre --num_train_epochs 8 --residual_dropout 0.2 --deepspeed --use_flash_attention true --model_name andreaskoepf/pythia-12b-pre-2000`

data:
```
reference-data:
  datasets:
    - oasst_export:
      lang: "bg,ca,cs,da,de,en,es,fr,hr,hu,it,nl,pl,pt,ro,ru,sl,sr,sv,uk"
      input_file_path: 2023-03-25_oasst_research_ready_synth_labels.jsonl.gz
      val_split: 0.05
    - alpaca
  sort_by_length: false
  use_custom_sampler: false
```


pythia:
```
reference-pythia-12b:
  dtype: fp16
  log_dir: "pythia_log_12b"
  learning_rate: 6e-6
  model_name: EleutherAI/pythia-12b-deduped
  output_dir: pythia_model_12b
  weight_decay: 0.0
  max_length: 2048
  warmup_steps: 100
  gradient_checkpointing: true
  gradient_accumulation_steps: 2
  per_device_train_batch_size: 4
  per_device_eval_batch_size: 4
  eval_steps: 100
  save_steps: 1000
  num_train_epochs: 8
  save_total_limit: 4
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