
TinyLlama-1.1B-intermediate-step-715k-1.5T finetuned using airoboros-3.1-no-mathjson-max-1k dataset. 

Qlora is used. Adapter is merged.

SFT code:
https://github.com/habanoz/qlora.git

Command used:
```bash
accelerate launch $BASE_DIR/qlora/train.py \
  --model_name_or_path $BASE_MODEL \
  --working_dir $BASE_DIR/$OUTPUT_NAME-checkpoints \
  --output_dir $BASE_DIR/$OUTPUT_NAME-peft \
  --merged_output_dir $BASE_DIR/$OUTPUT_NAME \
  --final_output_dir $BASE_DIR/$OUTPUT_NAME-final \
  --num_train_epochs 1 \
  --logging_steps 1 \
  --save_strategy steps \
  --save_steps 75 \
  --save_total_limit 2 \
  --data_seed 11422 \
  --evaluation_strategy steps \
  --per_device_eval_batch_size 4 \
  --eval_dataset_size 0.01 \
  --eval_steps 75 \
  --max_new_tokens 1024 \
  --dataloader_num_workers 3 \
  --logging_strategy steps \
  --do_train \
  --do_eval \
  --lora_r 64 \
  --lora_alpha 16 \
  --lora_modules all \
  --bits 4 \
  --double_quant \
  --quant_type nf4 \
  --lr_scheduler_type constant \
  --dataset habanoz/airoboros-3.1-no-mathjson-max-1k \
  --dataset_format airoboros_chat \
  --model_max_len 1024 \
  --per_device_train_batch_size 4 \
  --gradient_accumulation_steps 4 \
  --learning_rate 1e-5 \
  --adam_beta2 0.999 \
  --max_grad_norm 0.3 \
  --lora_dropout 0.0 \
  --weight_decay 0.0 \
  --seed 11422 \
  --gradient_checkpointing \
  --use_flash_attention_2 \
  --ddp_find_unused_parameters False
  ```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_habanoz__TinyLlama-1.1B-intermediate-step-715k-1.5T-lr-5-1epch-airoboros3.1-1k-instruct-V1)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |34.98|
|AI2 Reasoning Challenge (25-Shot)|30.72|
|HellaSwag (10-Shot)              |54.32|
|MMLU (5-Shot)                    |24.78|
|TruthfulQA (0-shot)              |41.67|
|Winogrande (5-shot)              |57.62|
|GSM8k (5-shot)                   | 0.76|

