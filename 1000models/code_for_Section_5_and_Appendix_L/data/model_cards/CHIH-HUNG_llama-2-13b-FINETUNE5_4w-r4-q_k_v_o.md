# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->

在llama-2-13b上使用huangyt/FINETUNE5資料集進行訓練，總資料筆數約4w

# Fine-Tuning Information
- **GPU:** RTX4090 (single core / 24564MiB)
- **model:** meta-llama/Llama-2-13b-hf
- **dataset:** huangyt/FINETUNE3 (共約3.3w筆訓練集)
- **peft_type:** LoRA
- **lora_rank:** 16
- **lora_target:** q_proj, k_proj, v_proj, o_proj
- **per_device_train_batch_size:** 8
- **gradient_accumulation_steps:** 8
- **learning_rate :** 4e-4
- **epoch:** 1
- **precision:** bf16
- **quantization:** load_in_4bit

# Fine-Tuning Detail
- **train_loss:** 0.579
- **train_runtime:** 4:6:11 (use deepspeed)

# Evaluation
- 與Llama-2-13b比較4種Benchmark，包含**ARC**、**HellaSwag**、**MMLU**、**TruthfulQA**
- 評估結果使用**本地**所測的分數，並使用load_in_8bit

| Model                                 | Average |   ARC   |HellaSwag| MMLU  | TruthfulQA | Time (s) |
|---------------------------------------|---------|---------|---------|-------|------------|----------|
| FINETUNE5_4w-r4-q_k_v_o               |  56.09  |  54.35  |  79.24  | 54.01 |   36.75    |  22095   |
| FINETUNE5_4w-r8-q_k_v_o               |  57.55  |  55.38  |  79.57  | 54.03 |   41.21    |  22127   |
| FINETUNE5_4w-r16-q_k_v_o              |  57.26  |  54.35  |  79.74  | 52.29 |   42.68    |  22153   |
| FINETUNE5_4w-r4-gate_up_down          |  56.51  |  52.82  |  79.13  | 52.83 |   41.28    |  22899   |
| FINETUNE5_4w-r8-gate_up_down          |  56.10  |  52.73  |  79.14  | 52.56 |   39.99    |  22926   |
| FINETUNE5_4w-r16-gate_up_down         |  56.23  |  52.39  |  79.48  | 53.42 |   39.62    |  22963   |
| FINETUNE5_4w-r4-q_k_v_o_gate_up_down  |  56.06  |  52.56  |  79.21  | 51.67 |   40.80    |  24303   |
| FINETUNE5_4w-r8-q_k_v_o_gate_up_down  |  56.35  |  51.88  |  79.42  | 52.00 |   42.10    |  24376   |
| FINETUNE5_4w-r16-q_k_v_o_gate_up_down |  56.73  |  54.18  |  79.53  | 52.77 |   40.46    |  24439   |

# How to convert dataset to json

- 在**load_dataset**中輸入資料集名稱，並且在**take**中輸入要取前幾筆資料
- 觀察該資料集的欄位名稱，填入**example**欄位中(例如system_prompt、question、response)
- 最後指定json檔儲存位置 (**json_filename**)

```py
import json
from datasets import load_dataset

# 讀取數據集，take可以取得該數據集前n筆資料
dataset = load_dataset("huangyt/FINETUNE5", split="train", streaming=True)

# 提取所需欄位並建立新的字典列表
extracted_data = []
for example in dataset:
    extracted_example = {
        "instruction": example["instruction"],
        "input": example["input"],
        "output": example["output"]
    }
    extracted_data.append(extracted_example)

# 指定 JSON 文件名稱
json_filename = "FINETUNE5.json"

# 寫入 JSON 文件
with open(json_filename, "w") as json_file:
    json.dump(extracted_data, json_file, indent=4)

print(f"數據已提取並保存為 {json_filename}")
```