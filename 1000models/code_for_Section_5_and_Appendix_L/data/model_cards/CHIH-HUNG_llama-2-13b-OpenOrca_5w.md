# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->

在llama-2-13b上使用open orca前5萬筆資料集進行訓練

# Fine-Tuning Information
- **GPU:** RTX4090 (single core / 24564MiB)
- **model:** meta-llama/Llama-2-13b-hf
- **dataset:** Open-Orca/OpenOrca (取前5w筆訓練集)
- **peft_type:** LoRA
- **lora_rank:** 8
- **lora_target:** q_proj, v_proj
- **per_device_train_batch_size:** 8
- **gradient_accumulation_steps:** 8
- **learning_rate :** 5e-5
- **epoch:** 1
- **precision:** bf16
- **quantization:** load_in_4bit

# Fine-Tuning Detail
- **train_loss:** 0.903261117822906
- **train_runtime:** 7:19:57 (use deepspeed)

# Evaluation
- 評估結果來自**HuggingFaceH4/open_llm_leaderboard**
- 與Llama-2-13b和其他使用Open-Orca的模型比較4種Benchmark
- Benchmark包含**ARC**、**HellaSwag**、**MMLU**、**TruthfulQA**

| Model                                   |Average|  ARC  |HellaSwag| MMLU  | TruthfulQA |
|-----------------------------------------|-------|-------|---------|-------|------------|
|meta-llama/Llama-2-13b-hf                | 56.9  | 58.11 |  80.97  | 54.34 |   34.17    |
|meta-llama/Llama-2-13b-chat-hf           | 59.93 | 59.04 |  81.94  | 54.64 |   44.12    |
|Open-Orca/OpenOrca-Platypus2-13B         | 64.6  | 62.8  |  83.15  | 59.39 |   53.08    |
|Open-Orca/OpenOrcaxOpenChat-Preview2-13B | 63.81 | 62.37 |  82.96  | 58.68 |   51.23    |
|circulus/Llama-2-13b-orca-v1             | 62.91 | 62.03 |  82.27  | 57.71 |   49.61    |
|CHIH-HUNG/llama-2-13b-open_orca_20w      | 60.46 | 59.9  |  82.51  | 56.3  |   43.14    |
|CHIH-HUNG/llama-2-13b-OpenOrca_5w        | 61.2  | 61.01 |  82.82  | 56.09 |   44.87    |


# How to convert dataset to json

- 在**load_dataset**中輸入資料集名稱，並且在**take**中輸入要取前幾筆資料
- 觀察該資料集的欄位名稱，填入**example**欄位中(例如system_prompt、question、response)
- 最後指定json檔儲存位置 (**json_filename**)

```py
import json
from datasets import load_dataset

# 讀取數據集，take可以取得該數據集前n筆資料
dataset = load_dataset("Open-Orca/OpenOrca", split="train", streaming=True).take(50000)

# 提取所需欄位並建立新的字典列表
extracted_data = []
for example in dataset:
    extracted_example = {
        ### open orca
        "system_prompt": example["system_prompt"],
        "question": example["question"],
        "response": example["response"]
    }
    extracted_data.append(extracted_example)

# 指定 JSON 文件名稱
json_filename = "open_orca.json"

# 寫入 JSON 文件
with open(json_filename, "w") as json_file:
    json.dump(extracted_data, json_file, indent=4)

print(f"數據已提取並保存為 {json_filename}")
```
