# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->

在llama-2-13b上使用huangyt/FINETUNE2_TEST資料集進行訓練，總資料筆數約2.2w

# Fine-Tuning Information
- **GPU:** RTX4090 (single core / 24564MiB)
- **model:** meta-llama/Llama-2-13b-hf
- **dataset:** huangyt/FINETUNE2_TEST (共約2.2w筆訓練集)
- **peft_type:** LoRA
- **lora_rank:** 8
- **lora_target:** gate_proj, up_proj, down_proj
- **per_device_train_batch_size:** 8
- **gradient_accumulation_steps:** 8
- **learning_rate :** 5e-5
- **epoch:** 1
- **precision:** bf16
- **quantization:** load_in_4bit

# Fine-Tuning Detail
- **train_loss:** 0.567
- **train_runtime:** 2:47:57 (use deepspeed)

# Evaluation
- 評估結果來自**HuggingFaceH4/open_llm_leaderboard**
- 與Llama-2-13b比較4種Benchmark，包含**ARC**、**HellaSwag**、**MMLU**、**TruthfulQA**

| Model                                    |Average|  ARC  |HellaSwag| MMLU  |TruthfulQA|
|------------------------------------------|-------|-------|---------|-------|----------|
|meta-llama/Llama-2-13b-hf                 | 56.9  | 58.11 |  80.97  | 54.34 |  34.17   |
|meta-llama/Llama-2-13b-chat-hf            | 59.93 | 59.04 |  81.94  | 54.64 |  44.12   |
|CHIH-HUNG/llama-2-13b-FINETUNE2_TEST_2.2w | 58.46 | 56.23 |  82.7   | 55.35 |  39.55   |

# How to convert dataset to json

- 在**load_dataset**中輸入資料集名稱，並且在**take**中輸入要取前幾筆資料
- 觀察該資料集的欄位名稱，填入**example**欄位中(例如system_prompt、question、response)
- 最後指定json檔儲存位置 (**json_filename**)

```py
import json
from datasets import load_dataset

# 讀取數據集，take可以取得該數據集前n筆資料
dataset = load_dataset("huangyt/FINETUNE2_TEST", split="train", streaming=True)

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
json_filename = "FINETUNE2_TEST.json"

# 寫入 JSON 文件
with open(json_filename, "w") as json_file:
    json.dump(extracted_data, json_file, indent=4)

print(f"數據已提取並保存為 {json_filename}")
```