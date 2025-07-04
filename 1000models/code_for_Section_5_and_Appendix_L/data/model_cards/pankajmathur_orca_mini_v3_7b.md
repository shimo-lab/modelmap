
# orca_mini_v3_7b

A LLama2-7b model trained on Orca Style datasets.

<br>

![orca-mini](https://huggingface.co/psmathur/orca_mini_v3_7b/resolve/main/orca_minis_small.jpeg)

<br>

🤔 How good is orca-mini-v3-7b? Do the evaluation results from HuggingFace Open LLM leaderboard translate to real-world use cases?

🔍 Now you can figure it out for yourself! 

Introducing the orca-mini chatbot powered by the orca-mini-v3-7b model. Dive in and see how the open source 7b model stacks up in the world of massive language models. 🌍

⏰ Hurry up before I run out of GPU credits! 😉

Check it out here 👉

[https://huggingface.co/spaces/psmathur/psmathur-orca_mini_v3_7b](https://huggingface.co/spaces/psmathur/psmathur-orca_mini_v3_7b)


<br>

**P.S. If you're interested to collaborate, please connect with me at www.linkedin.com/in/pankajam.**

<br>

### quantized versions

Big thanks to [@TheBloke](https://huggingface.co/TheBloke)

1) https://huggingface.co/TheBloke/orca_mini_v3_7B-GGML

2) https://huggingface.co/TheBloke/orca_mini_v3_7B-GPTQ

<br>

#### license disclaimer:

This model is bound by the license & usage restrictions of the original Llama-2 model. And comes with no warranty or gurantees of any kind.

<br>

## evaluation

We evaluated orca_mini_v3_7b on a wide range of tasks using [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) from EleutherAI. 

Here are the results on metrics used by [HuggingFaceH4 Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)

|||||
|:------:|:--------:|:-------:|:--------:|
|**Task**|**Metric**|**Value**|**Stderr**|
|*arc_challenge*|acc_norm|0.5717|0.0145|
|*hellaswag*|acc_norm|0.7966|0.0043|
|*mmlu*|acc_norm|0.5234|0.035|
|*truthfulqa_mc*|mc2|0.5029|0.0156|
|**Total Average**|-|**0.59865**||


<br>

## example esage

Here is prompt format

```
### System:
You are an AI assistant that follows instruction extremely well. Help as much as you can.

### User:
Tell me about Orcas.

### Assistant:

```

Below shows a code example on how to use this model

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

tokenizer = AutoTokenizer.from_pretrained("psmathur/orca_mini_v3_7b", use_fast=False)
model = AutoModelForCausalLM.from_pretrained(
  "psmathur/orca_mini_v3_7b",
  torch_dtype=torch.float16,
  load_in_8bit=True,
  low_cpu_mem_usage=True,
  device_map="auto"
)
system_prompt = "### System:\nYou are an AI assistant that follows instruction extremely well. Help as much as you can.\n\n"

#generate text steps
instruction = "Tell me about Orcas."
prompt = f"{system_prompt}### User: {instruction}\n\n### Assistant:\n"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
output = model.generate(**inputs, do_sample=True, top_p=0.95, top_k=0, max_new_tokens=4096)

print(tokenizer.decode(output[0], skip_special_tokens=True))

```

<br>

#### limitations & biases:

While this model aims for accuracy, it can occasionally produce inaccurate or misleading results. 

Despite diligent efforts in refining the pretraining data, there remains a possibility for the generation of inappropriate, biased, or offensive content. 

Exercise caution and cross-check information when necessary.


<br>

### citiation:

Please kindly cite using the following BibTeX:

```
@misc{orca_mini_v3_7b,
  author = {Pankaj Mathur},
  title = {orca_mini_v3_7b: An explain tuned Llama2-7b model},
  year = {2023},
  publisher = {GitHub, HuggingFace},
  journal = {GitHub repository, HuggingFace repository},
  howpublished = {\url{https://https://huggingface.co/psmathur/orca_mini_v3_7b},
}
```

```
@misc{mukherjee2023orca,
      title={Orca: Progressive Learning from Complex Explanation Traces of GPT-4}, 
      author={Subhabrata Mukherjee and Arindam Mitra and Ganesh Jawahar and Sahaj Agarwal and Hamid Palangi and Ahmed Awadallah},
      year={2023},
      eprint={2306.02707},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

```
@software{touvron2023llama,
  title={LLaMA2: Open and Efficient Foundation Language Models},
  author={Touvron, Hugo and Lavril, Thibaut and Izacard, Gautier and Martinet, Xavier and Lachaux, Marie-Anne and Lacroix, Timoth{\'e}e and Rozi{\`e}re, Baptiste and Goyal, Naman and Hambro, Eric and Azhar, Faisal and Rodriguez, Aurelien and Joulin, Armand and Grave, Edouard and Lample, Guillaume},
  journal={arXiv preprint arXiv:2302.13971},
  year={2023}
}
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_psmathur__orca_mini_v3_7b)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 47.98   |
| ARC (25-shot)         | 56.91          |
| HellaSwag (10-shot)   | 79.64    |
| MMLU (5-shot)         | 52.37         |
| TruthfulQA (0-shot)   | 50.51   |
| Winogrande (5-shot)   | 74.27   |
| GSM8K (5-shot)        | 7.13        |
| DROP (3-shot)         | 15.06         |

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_psmathur__orca_mini_v3_7b)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |53.47|
|AI2 Reasoning Challenge (25-Shot)|56.91|
|HellaSwag (10-Shot)              |79.64|
|MMLU (5-Shot)                    |52.37|
|TruthfulQA (0-shot)              |50.51|
|Winogrande (5-shot)              |74.27|
|GSM8k (5-shot)                   | 7.13|


# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_pankajmathur__orca_mini_v3_7b)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |13.52|
|IFEval (0-Shot)    |28.21|
|BBH (3-Shot)       |17.84|
|MATH Lvl 5 (4-Shot)| 0.30|
|GPQA (0-shot)      | 0.00|
|MuSR (0-shot)      |22.71|
|MMLU-PRO (5-shot)  |12.04|

