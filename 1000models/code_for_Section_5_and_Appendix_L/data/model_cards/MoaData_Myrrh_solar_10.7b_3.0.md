## Model Details

**Model Developers** : Taeeon Park, Gihong Lee

**dataset** :  dpo medical dataset (AI-hub dataset 활용 자체 제작)

**Training Method Method** : DPO.

**Company** : MoAData

## Usage
```
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
repo = "MoaData/Myrrh_solar_10.7b_3.0"
model = AutoModelForCausalLM.from_pretrained(
        repo,
        return_dict=True,
        torch_dtype=torch.float16,
        device_map='auto'
)
tokenizer = AutoTokenizer.from_pretrained(repo)
```