- base model: [OpenAssistant/pythia-12b-pre-v8-12.5k-steps](https://huggingface.co/OpenAssistant/pythia-12b-pre-v8-12.5k-steps)
- wandb: https://wandb.ai/open-assistant/supervised-finetuning/runs/pcw1ejda
- [sampling report](https://raw.githubusercontent.com/Open-Assistant/oasst-model-eval/main/sampling_reports/oasst-sft/2023-05-07_OpenAssistant_pythia-12b-sft-v8-7k-steps_sampling_noprefix2.json)

```
pythia-12b-sft-8:
  dtype: fp16
  log_dir: "pythia_log_12b"
  learning_rate: 6e-6
  model_name: OpenAssistant/pythia-12b-pre-v8-12.5k-steps
  output_dir: pythia_model_12b
  weight_decay: 0.0
  residual_dropout: 0.0
  max_length: 2048
  use_flash_attention: true
  warmup_steps: 100
  gradient_checkpointing: true
  gradient_accumulation_steps: 2
  per_device_train_batch_size: 4
  per_device_eval_batch_size: 4
  eval_steps: 251
  save_steps: 500
  num_train_epochs: 8
  save_total_limit: 4
  num_train_epochs: 8
  save_total_limit: 3
  use_custom_sampler: true
  sort_by_length: false
  save_strategy: steps
  datasets:
    - oasst_export:
        lang: "bg,ca,cs,da,de,en,es,fr,hr,hu,it,nl,pl,pt,ro,ru,sl,sr,sv,uk"
        input_file_path: 2023-05-06_OASST_labels.jsonl.gz
        val_split: 0.05
    - vicuna:
        val_split: 0.05
        max_val_set: 800
        fraction: 0.4
    - dolly15k:
        val_split: 0.05
        max_val_set: 300
    - grade_school_math_instructions:
        val_split: 0.05
    - code_alpaca:
        val_split: 0.05
        max_val_set: 250
    - red_pajama:
        fraction: 0.05
        max_val_set: 1000
    - wizardlm_70k:
        val_split: 0.05
        max_val_set: 500
        fraction: 0.4
    - poem_instructions:
        fraction: 0.5
        val_split: 0.025
```
