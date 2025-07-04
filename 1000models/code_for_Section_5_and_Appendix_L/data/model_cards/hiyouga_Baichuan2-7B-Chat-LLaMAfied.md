
This is the LLaMAfied version of [Baichuan2-7B-Chat](https://huggingface.co/baichuan-inc/Baichuan2-7B-Chat) model by Baichuan Inc.

This model is converted with https://github.com/hiyouga/LLaMA-Factory/blob/main/tests/llamafy_baichuan2.py

You may use this model for fine-tuning in downstream tasks, we recommend using our efficient fine-tuning toolkit. https://github.com/hiyouga/LLaMA-Factory

- **Developed by:** Baichuan Inc.
- **Language(s) (NLP):** Chinese/English
- **License:** [Baichuan2 License](https://huggingface.co/baichuan-inc/Baichuan2-7B-Chat/resolve/main/Baichuan2%20%E6%A8%A1%E5%9E%8B%E7%A4%BE%E5%8C%BA%E8%AE%B8%E5%8F%AF%E5%8D%8F%E8%AE%AE.pdf)

Usage:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

tokenizer = AutoTokenizer.from_pretrained("hiyouga/Baichuan2-7B-Chat-LLaMAfied", use_fast=False)
model = AutoModelForCausalLM.from_pretrained("hiyouga/Baichuan2-7B-Chat-LLaMAfied").cuda()
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

query = "<reserved_106>晚上睡不着怎么办<reserved_107>"
inputs = tokenizer([query], return_tensors="pt")
inputs = inputs.to("cuda")
generate_ids = model.generate(**inputs, max_new_tokens=256, streamer=streamer)
```

You could also alternatively launch a CLI demo by using the script in [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)

```bash
python src/cli_demo.py --template baichuan2 --model_name_or_path hiyouga/Baichuan2-7B-Chat-LLaMAfied
```

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_hiyouga__Baichuan2-7B-Chat-LLaMAfied)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 47.92   |
| ARC (25-shot)         | 52.47          |
| HellaSwag (10-shot)   | 74.04    |
| MMLU (5-shot)         | 53.88         |
| TruthfulQA (0-shot)   | 48.04   |
| Winogrande (5-shot)   | 69.14   |
| GSM8K (5-shot)        | 10.92        |
| DROP (3-shot)         | 26.94         |
