# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->

在llama-2-13b上使用dolphin前20萬筆資料集進行訓練

# Fine-Tuning Information
- **GPU:** RTX4090 (single core / 24564MiB)
- **model:** meta-llama/Llama-2-13b-hf
- **dataset:** ehartford/dolphin (取前20w筆訓練集)
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
- **train_loss:** 0.8354
- **train_runtime:** 28:42:18 (use deepspeed)

# Evaluation
- 評估結果來自**HuggingFaceH4/open_llm_leaderboard**
- 與Llama-2-13b和其他使用dolphin的模型比較4種Benchmark
- Benchmark包含**ARC**、**HellaSwag**、**MMLU**、**TruthfulQA**
- **注意**：ehartford/dolphin-llama-13b使用的是llama-1

| Model                            |Average|  ARC  |HellaSwag| MMLU  | TruthfulQA |
|----------------------------------|-------|-------|---------|-------|------------|
|meta-llama/Llama-2-13b-hf         | 56.9  | 58.11 |  80.97  | 54.34 |   34.17    |
|meta-llama/Llama-2-13b-chat-hf    | 59.93 | 59.04 |  81.94  | 54.64 |   44.12    |
|ehartford/dolphin-llama-13b       | 59.26 | 55.55 |  77.11  | 52.16 |   52.23    |
|CHIH-HUNG/llama-2-13b-dolphin_5w  |  61   | 60.67 |  82.69  | 56.23 |   44.41    |
|CHIH-HUNG/llama-2-13b-dolphin_20w | 60.17 | 59.56 |  82.55  | 55.89 |   42.67    |

# How to convert dataset to json

- 在**load_dataset**中輸入資料集名稱，並且在**take**中輸入要取前幾筆資料
- 觀察該資料集的欄位名稱，填入**example**欄位中(例如instruction、input、output)
- 最後指定json檔儲存位置 (**json_filename**)

```py
import json
from datasets import load_dataset

# 讀取數據集，take可以取得該數據集前n筆資料
dataset = load_dataset("ehartford/dolphin", split="train", streaming=True).take(200000)

# 提取所需欄位並建立新的字典列表
extracted_data = []
for example in dataset:
    extracted_example = {
        ### dolphin
        "instruction": example["instruction"],
        "input": example["input"],
        "output": example["output"]
    }
    extracted_data.append(extracted_example)

# 指定 JSON 文件名稱
json_filename = "dolphin.json"

# 寫入 JSON 文件
with open(json_filename, "w") as json_file:
    json.dump(extracted_data, json_file, indent=4)

print(f"數據已提取並保存為 {json_filename}")
```