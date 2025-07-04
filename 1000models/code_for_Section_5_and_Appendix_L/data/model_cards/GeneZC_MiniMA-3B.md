
## MiniMA-3B

📑 [arXiv](https://arxiv.org/abs/2311.07052) | 👻 [GitHub](https://github.com/GeneZC/MiniMA) | 🤗 [HuggingFace-MiniMA](https://huggingface.co/GeneZC/MiniMA-3B) | 🤗 [HuggingFace-MiniChat](https://huggingface.co/GeneZC/MiniChat-3B) | 🤗 [HuggingFace-MiniChat-1.5](https://huggingface.co/GeneZC/MiniChat-1.5-3B) | 🤖 [ModelScope-MiniMA](https://modelscope.cn/models/GeneZC/MiniMA-3B) | 🤖 [ModelScope-MiniChat](https://modelscope.cn/models/GeneZC/MiniChat-3B)

🆕 **Updates: MiniChat-1.5-3B**

❗ Must comply with LICENSE of LLaMA2 since it is derived from LLaMA2.

A language model distilled from an adapted version of LLaMA2-7B following "Towards the Law of Capacity Gap in Distilling Language Models".

Establishing a new compute-performance pareto frontier.

<img src="./teaser_a.jpg" alt="teaser_a" width="700" />

The following is an example code snippet to use MiniMA-3B:

```python
import torch

from transformers import AutoModelForCausalLM, AutoTokenizer

# MiniMA
tokenizer = AutoTokenizer.from_pretrained("GeneZC/MiniMA-3B", use_fast=False)
# GPU.
model = AutoModelForCausalLM.from_pretrained("GeneZC/MiniMA-3B", use_cache=True, device_map="auto", torch_dtype=torch.float16).eval()
# CPU.
# model = AutoModelForCausalLM.from_pretrained("GeneZC/MiniMA-3B", use_cache=True, device_map="cpu", torch_dtype=torch.float16).eval()

prompt = "Question: Sherrie tells the truth. Vernell says Sherrie tells the truth. Alexis says Vernell lies. Michaela says Alexis tells the truth. Elanor says Michaela tells the truth. Does Elanor tell the truth?\nAnswer: No\n\nQuestion: Kristian lies. Sherrie says Kristian lies. Delbert says Sherrie lies. Jerry says Delbert tells the truth. Shalonda says Jerry tells the truth. Does Shalonda tell the truth?\nAnswer: No\n\nQuestion: Vina tells the truth. Helene says Vina lies. Kandi says Helene tells the truth. Jamey says Kandi lies. Ka says Jamey lies. Does Ka tell the truth?\nAnswer: No\n\nQuestion: Christie tells the truth. Ka says Christie tells the truth. Delbert says Ka lies. Leda says Delbert tells the truth. Lorine says Leda tells the truth. Does Lorine tell the truth?\nAnswer:"
input_ids = tokenizer([prompt]).input_ids
output_ids = model.generate(
    torch.as_tensor(input_ids).cuda(),
    do_sample=True,
    temperature=0.7,
    max_new_tokens=1024,
)
output_ids = output_ids[0][len(input_ids[0]):]
output = tokenizer.decode(output_ids, skip_special_tokens=True).strip()
# output: "No"
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
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_GeneZC__MiniMA-3B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 36.2   |
| ARC (25-shot)         | 43.43          |
| HellaSwag (10-shot)   | 68.06    |
| MMLU (5-shot)         | 28.69         |
| TruthfulQA (0-shot)   | 39.76   |
| Winogrande (5-shot)   | 65.98   |
| GSM8K (5-shot)        | 2.73        |
| DROP (3-shot)         | 4.72         |
