
TinyLlama-1.1B-intermediate-step-715k-1.5T finetuned using OpenAssistant/oasst_top1_2023-08-25 dataset.

SFT code:
https://github.com/jzhang38/TinyLlama/tree/main/sft

Evaluation Results at:
https://huggingface.co/datasets/open-llm-leaderboard/details_habanoz__tinyllama-oasst1-top1-instruct-full-lr1-5-v0.1_public/blob/main/results_2023-11-23T17-25-53.937618.json

Command used:
```bash
accelerate launch finetune.py \
    --model_name_or_path TinyLlama/TinyLlama-1.1B-intermediate-step-715k-1.5T \
    --output_dir ./output/1_5T_FT_lr1e-5_ep5_top1_2023-08-25 \
    --logging_steps 10 \
    --save_strategy epoch \
    --data_seed 42 \
    --save_total_limit 2 \
    --evaluation_strategy epoch \
    --eval_dataset_size 512 \
    --max_eval_samples 1000 \
    --per_device_eval_batch_size 1 \
    --max_new_tokens 32 \
    --dataloader_num_workers 3 \
    --group_by_length=False \
    --logging_strategy steps \
    --remove_unused_columns False \
    --do_train \
    --do_eval \
    --warmup_ratio 0.05 \
    --lr_scheduler_type constant \
    --dataset OpenAssistant/oasst_top1_2023-08-25 \
    --dataset_format oasst1 \
    --source_max_len 1 \
    --target_max_len 1023 \
    --per_device_train_batch_size 2 \
    --gradient_accumulation_steps 8 \
    --max_steps 0 \
    --num_train_epochs 5 \
    --learning_rate 1e-5 \
    --adam_beta2 0.999 \
    --max_grad_norm 1.0 \
    --weight_decay 0.0 \
    --seed 0 \
    --trust_remote_code
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_habanoz__tinyllama-oasst1-top1-instruct-full-lr1-5-v0.1)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |35.58|
|AI2 Reasoning Challenge (25-Shot)|32.85|
|HellaSwag (10-Shot)              |58.16|
|MMLU (5-Shot)                    |25.96|
|TruthfulQA (0-shot)              |38.35|
|Winogrande (5-shot)              |57.70|
|GSM8k (5-shot)                   | 0.45|

