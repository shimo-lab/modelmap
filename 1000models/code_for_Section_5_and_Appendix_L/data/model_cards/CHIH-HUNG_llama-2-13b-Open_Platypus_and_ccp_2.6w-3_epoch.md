# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->

在llama-2-13b上使用garage-bAInd/Open-Platypus資料集進行訓練，總資料筆數約2.5w + ccp

# Fine-Tuning Information
- **GPU:** RTX4090 (single core / 24564MiB)
- **model:** meta-llama/Llama-2-13b-hf
- **dataset:** garage-bAInd/Open-Platypus (共約2.5w筆訓練集) + ccp (約1200筆)
- **peft_type:** LoRA
- **lora_rank:** 8
- **lora_target:** gate_proj, up_proj, down_proj
- **per_device_train_batch_size:** 8
- **gradient_accumulation_steps:** 8
- **learning_rate :** 5e-5
- **epoch:** 3
- **precision:** bf16
- **quantization:** load_in_4bit

# Fine-Tuning Detail
- **train_loss:** 0.6
- **train_runtime:** 12:24:34 (use deepspeed)

# Evaluation
- 評估結果來自**HuggingFaceH4/open_llm_leaderboard**
- 與Llama-2-13b比較4種Benchmark，包含**ARC**、**HellaSwag**、**MMLU**、**TruthfulQA**

| Model                                                   |Average|  ARC  |HellaSwag| MMLU  |TruthfulQA|
|---------------------------------------------------------|-------|-------|---------|-------|----------|
|meta-llama/Llama-2-13b-hf                                | 56.9  | 58.11 |  80.97  | 54.34 |  34.17   |
|meta-llama/Llama-2-13b-chat-hf                           | 59.93 | 59.04 |  81.94  | 54.64 |  44.12   |
|Open-Orca/OpenOrca-Platypus2-13B                         | 63.19 | 61.52 |  82.27  | 58.85 |  50.11   |
|CHIH-HUNG/llama-2-13b-Open_Platypus_and_ccp_2.6w         | 59.41 | 58.96 |  82.51  | 56.12 |  40.07   |
|CHIH-HUNG/llama-2-13b-Open_Platypus_and_ccp_2.6w-3_epoch | 59.78 | 58.62 |  82.56  | 55.84 |  42.09   |

# How to convert dataset to json

- 在**load_dataset**中輸入資料集名稱，並且在**take**中輸入要取前幾筆資料
- 觀察該資料集的欄位名稱，填入**example**欄位中(例如instruction、input、output)
- 最後指定json檔儲存位置 (**json_filename**)

```py
import json
from datasets import load_dataset

# 讀取數據集，take可以取得該數據集前n筆資料
dataset = load_dataset("garage-bAInd/Open-Platypus", split="train", streaming=True)

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
json_filename = "Open-Platypus.json"

# 寫入 JSON 文件
with open(json_filename, "w") as json_file:
    json.dump(extracted_data, json_file, indent=4)

print(f"數據已提取並保存為 {json_filename}")
```