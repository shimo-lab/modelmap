# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->

在llama-2-13b上使用huangyt/FINETUNE3資料集進行訓練，總資料筆數約3.3w

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

| Model                                   |Average|  ARC  |HellaSwag| MMLU  | TruthfulQA |
|-----------------------------------------|-------|-------|---------|-------|------------|
| FINETUNE3_3.3w-r4-q_k_v_o               | 56.29 | 54.27 |  79.42  | 51.90 |   39.58    |
| FINETUNE3_3.3w-r8-q_k_v_o               | 56.53 | 52.99 |  79.45  | 53.53 |   40.14    |
| FINETUNE3_3.3w-r16-q_k_v_o              | 56.25 | 53.24 |  79.53  | 54.03 |   38.20    |
| FINETUNE3_3.3w-r4-gate_up_down          | 55.79 | 51.02 |  79.37  | 53.36 |   39.40    |
| FINETUNE3_3.3w-r8-gate_up_down          | 56.60 | 53.33 |  79.43  | 53.60 |   40.03    |
| FINETUNE3_3.3w-r16-gate_up_down         | 56.34 | 51.88 |  79.42  | 54.64 |   39.44    |
| FINETUNE3_3.3w-r4-q_k_v_o_gate_up_down  | 56.67 | 53.07 |  79.34  | 54.07 |   40.19    |
| FINETUNE3_3.3w-r8-q_k_v_o_gate_up_down  | 56.93 | 54.61 |  79.16  | 53.51 |   40.46    |
| FINETUNE3_3.3w-r16-q_k_v_o_gate_up_down | 57.78 | 53.92 |  79.41  | 54.68 |   43.09    |

-------------------------------------------------------------------------------------------

- 評估結果來自**HuggingFaceH4/open_llm_leaderboard**

| Model                                   |Average|  ARC  |HellaSwag| MMLU  | TruthfulQA |
|-----------------------------------------|-------|-------|---------|-------|------------|
| FINETUNE3_3.3w-r4-q_k_v_o               | 58.34 | 59.04 |  81.15  |  53   |   40.16    |
| FINETUNE3_3.3w-r8-q_k_v_o               | 58.28 | 56.06 |  81.89  | 55.04 |   40.12    |
| FINETUNE3_3.3w-r16-q_k_v_o              | 58.55 | 59.3  |  81.2   | 55.58 |   38.13    |
| FINETUNE3_3.3w-r4-gate_up_down          | 57.79 | 56.4  |  81.93  | 53.63 |   39.23    |
| FINETUNE3_3.3w-r8-gate_up_down          | 58.17 | 57.25 |  81.79  | 53.96 |   39.66    |
| FINETUNE3_3.3w-r16-gate_up_down         | 58.91 | 58.7  |  81.89  | 56.08 |   38.95    |
| FINETUNE3_3.3w-r4-q_k_v_o_gate_up_down  | 58.42 | 57.76 |  80.78  | 54.32 |   40.8     |
| FINETUNE3_3.3w-r8-q_k_v_o_gate_up_down  | 58.26 | 57.94 |  81.19  | 53.43 |   40.48    |
| FINETUNE3_3.3w-r16-q_k_v_o_gate_up_down | 59.62 | 59.22 |  81.52  | 54.94 |   42.83    |

# How to convert dataset to json

- 在**load_dataset**中輸入資料集名稱，並且在**take**中輸入要取前幾筆資料
- 觀察該資料集的欄位名稱，填入**example**欄位中(例如system_prompt、question、response)
- 最後指定json檔儲存位置 (**json_filename**)

```py
import json
from datasets import load_dataset

# 讀取數據集，take可以取得該數據集前n筆資料
dataset = load_dataset("huangyt/FINETUNE3", split="train", streaming=True)

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
json_filename = "FINETUNE3.json"

# 寫入 JSON 文件
with open(json_filename, "w") as json_file:
    json.dump(extracted_data, json_file, indent=4)

print(f"數據已提取並保存為 {json_filename}")
```