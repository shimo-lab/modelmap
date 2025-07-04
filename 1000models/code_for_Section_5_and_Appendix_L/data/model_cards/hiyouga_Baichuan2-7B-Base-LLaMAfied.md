
This is the LLaMAfied version of [Baichuan2-7B-Base](https://huggingface.co/baichuan-inc/Baichuan2-7B-Base) model by Baichuan Inc.

This model is converted with https://github.com/hiyouga/LLaMA-Factory/blob/main/tests/llamafy_baichuan2.py

You may use this model for fine-tuning in downstream tasks, we recommend using our efficient fine-tuning toolkit. https://github.com/hiyouga/LLaMA-Factory

- **Developed by:** Baichuan Inc.
- **Language(s) (NLP):** Chinese/English
- **License:** [Baichuan2 License](https://huggingface.co/baichuan-inc/Baichuan2-7B-Base/resolve/main/Baichuan%202%E6%A8%A1%E5%9E%8B%E7%A4%BE%E5%8C%BA%E8%AE%B8%E5%8F%AF%E5%8D%8F%E8%AE%AE.pdf)

Usage:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("hiyouga/Baichuan2-7B-Base-LLaMAfied", use_fast=False)
model = AutoModelForCausalLM.from_pretrained("hiyouga/Baichuan2-7B-Base-LLaMAfied").cuda()
```

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_hiyouga__Baichuan2-7B-Base-LLaMAfied)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 42.83   |
| ARC (25-shot)         | 49.57          |
| HellaSwag (10-shot)   | 73.45    |
| MMLU (5-shot)         | 54.86         |
| TruthfulQA (0-shot)   | 37.54   |
| Winogrande (5-shot)   | 70.72   |
| GSM8K (5-shot)        | 7.81        |
| DROP (3-shot)         | 5.85         |
