
## MiniChat-3B

📑 [arXiv](https://arxiv.org/abs/2311.07052) | 👻 [GitHub](https://github.com/GeneZC/MiniMA) | 🤗 [HuggingFace-MiniMA](https://huggingface.co/GeneZC/MiniMA-3B) | 🤗 [HuggingFace-MiniChat](https://huggingface.co/GeneZC/MiniChat-3B) | 🤗 [HuggingFace-MiniChat-1.5](https://huggingface.co/GeneZC/MiniChat-1.5-3B) | 🤖 [ModelScope-MiniMA](https://modelscope.cn/models/GeneZC/MiniMA-3B) | 🤖 [ModelScope-MiniChat](https://modelscope.cn/models/GeneZC/MiniChat-3B)

🆕 **Updates: MiniChat-1.5-3B**

❗ Must comply with LICENSE of LLaMA2 since it is derived from LLaMA2.

A language model distilled and finetuned from an adapted version of LLaMA2-7B following "Towards the Law of Capacity Gap in Distilling Language Models".

Outperforming a wide range of 3B competitors in GPT4 evaluation and even competing with several 7B chat models.

<img src="./teaser_b.jpg" alt="teaser_b" width="687" />

The following is an example code snippet to use MiniChat-3B:

```python
import torch

from transformers import AutoModelForCausalLM, AutoTokenizer

from conversation import get_default_conv_template

# MiniChat
tokenizer = AutoTokenizer.from_pretrained("GeneZC/MiniChat-3B", use_fast=False)
# GPU.
model = AutoModelForCausalLM.from_pretrained("GeneZC/MiniChat-3B", use_cache=True, device_map="auto", torch_dtype=torch.float16).eval()
# CPU.
# model = AutoModelForCausalLM.from_pretrained("GeneZC/MiniChat-3B", use_cache=True, device_map="cpu", torch_dtype=torch.float32).eval()
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
conv = get_default_conv_template("minichat")

question = "Implement a program to find the common elements in two arrays without using any extra data structures."
conv.append_message(conv.roles[0], question)
conv.append_message(conv.roles[1], None)
prompt = conv.get_prompt()
input_ids = tokenizer([prompt]).input_ids
output_ids = model.generate(
    torch.as_tensor(input_ids).to(device),
    do_sample=True,
    temperature=0.7,
    max_new_tokens=1024,
)
output_ids = output_ids[0][len(input_ids[0]):]
output = tokenizer.decode(output_ids, skip_special_tokens=True).strip()
# output: "def common_elements(arr1, arr2):\n    if len(arr1) == 0:\n        return []\n    if len(arr2) == 0:\n        return arr1\n\n    common_elements = []\n    for element in arr1:\n        if element in arr2:\n            common_elements.append(element)\n\n    return common_elements"
# Multiturn conversation could be realized by continuously appending questions to `conv`.
```

## Bibtex

```bibtex
@article{zhang2023law,
    title={Towards the Law of Capacity Gap in Distilling Language Models},
    author={Zhang, Chen and Song, Dawei and Ye, Zheyu and Gao, Yan},
    year={2023},
    url={https://arxiv.org/abs/2311.07052}
}
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_GeneZC__MiniChat-3B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 42.94   |
| ARC (25-shot)         | 44.03          |
| HellaSwag (10-shot)   | 67.19    |
| MMLU (5-shot)         | 39.17         |
| TruthfulQA (0-shot)   | 45.67   |
| Winogrande (5-shot)   | 65.27   |
| GSM8K (5-shot)        | 10.54        |
| DROP (3-shot)         | 28.73         |
