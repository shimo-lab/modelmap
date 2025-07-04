## Model
- base_model : yanolja/KoSOLAR-10.7B-v0.2
- training objective: freeze, instruction Tuning 
## Dataset
공개 데이터 수집
- Deduplicating Training Data Makes Language Models Better 알고리즘 활용
- instruction version 1.4

## Code
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "jjingyeom/freeze_KoSoLAR-10.7B-v0.2_1.4_dedup"
model = AutoModelForCausalLM.from_pretrained(
        model_name,
)
tokenizer = AutoTokenizer.from_pretrained(model_name)
```