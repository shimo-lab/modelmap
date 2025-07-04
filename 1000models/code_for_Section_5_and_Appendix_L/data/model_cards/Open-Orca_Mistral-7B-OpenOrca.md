
<p><h1>🐋 Mistral-7B-OpenOrca 🐋</h1></p>


![OpenOrca Logo](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca/resolve/main/Images/MistralOrcaLogo.png "MistralOrca Logo")
[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)


# OpenOrca - Mistral - 7B - 8k

We have used our own [OpenOrca dataset](https://huggingface.co/datasets/Open-Orca/OpenOrca) to fine-tune on top of [Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-v0.1). 
This dataset is our attempt to reproduce the dataset generated for Microsoft Research's [Orca Paper](https://arxiv.org/abs/2306.02707).
We use [OpenChat](https://huggingface.co/openchat) packing, trained with [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl).

This release is trained on a curated filtered subset of most of our GPT-4 augmented data.
It is the same subset of our data as was used in our [OpenOrcaxOpenChat-Preview2-13B model](https://huggingface.co/Open-Orca/OpenOrcaxOpenChat-Preview2-13B).

**HF Leaderboard evals place this model as #1 for all models smaller than 30B at release time, outperforming all other 7B and 13B models!**

This release provides a first: a fully open model with class-breaking performance, capable of running fully accelerated on even moderate consumer GPUs.
Our thanks to the Mistral team for leading the way here. 

We affectionately codename this model: "*MistralOrca*"

If you'd like to try the model now, we have it running on fast GPUs unquantized: https://huggingface.co/spaces/Open-Orca/Mistral-7B-OpenOrca

Want to visualize our full (pre-filtering) dataset? Check out our [Nomic Atlas Map](https://atlas.nomic.ai/map/c1b88b47-2d9b-47e0-9002-b80766792582/2560fd25-52fe-42f1-a58f-ff5eccc890d2).

[<img src="https://huggingface.co/Open-Orca/OpenOrca-Preview1-13B/resolve/main/OpenOrca%20Nomic%20Atlas.png" alt="Atlas Nomic Dataset Map" width="400" height="400" />](https://atlas.nomic.ai/map/c1b88b47-2d9b-47e0-9002-b80766792582/2560fd25-52fe-42f1-a58f-ff5eccc890d2)


We are in-process with training more models, so keep a look out on our org for releases coming soon with exciting partners.

We will also give sneak-peak announcements on our Discord, which you can find here:

https://AlignmentLab.ai

or check the OpenAccess AI Collective Discord for more information about Axolotl trainer here:

https://discord.gg/5y8STgB3P3


# Quantized Models

Quantized versions of this model are generously made available by [TheBloke](https://huggingface.co/TheBloke).

- AWQ: https://huggingface.co/TheBloke/Mistral-7B-OpenOrca-AWQ
- GPTQ: https://huggingface.co/TheBloke/Mistral-7B-OpenOrca-GPTQ
- GGUF: https://huggingface.co/TheBloke/Mistral-7B-OpenOrca-GGUF


# Prompt Template

We used [OpenAI's Chat Markup Language (ChatML)](https://github.com/openai/openai-python/blob/main/chatml.md) format, with `<|im_start|>` and `<|im_end|>` tokens added to support this.

This means that, e.g., in [oobabooga](https://github.com/oobabooga/text-generation-webui/) the "`MPT-Chat`" instruction template should work, as it also uses ChatML.

This formatting is also available via a pre-defined [Transformers chat template](https://huggingface.co/docs/transformers/main/chat_templating),
which means that lists of messages can be formatted for you with the `apply_chat_template()` method:

```python
chat = [
  {"role": "system", "content": "You are MistralOrca, a large language model trained by Alignment Lab AI. Write out your reasoning step-by-step to be sure you get the right answers!"}
  {"role": "user", "content": "How are you?"},
  {"role": "assistant", "content": "I am doing well!"},
  {"role": "user", "content": "Please tell me about how mistral winds have attracted super-orcas."},
]
tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
```

which will yield:

```
<|im_start|>system
You are MistralOrca, a large language model trained by Alignment Lab AI. Write out your reasoning step-by-step to be sure you get the right answers!
<|im_end|>
<|im_start|>user
How are you?<|im_end|>
<|im_start|>assistant
I am doing well!<|im_end|>
<|im_start|>user
Please tell me about how mistral winds have attracted super-orcas.<|im_end|>
<|im_start|>assistant
```

If you use `tokenize=True` and `return_tensors="pt"` instead, then you will get a tokenized 
and formatted conversation ready to pass to `model.generate()`.


# Inference

See [this notebook](https://colab.research.google.com/drive/1yZlLSifCGELAX5GN582kZypHCv0uJuNX?usp=sharing) for inference details.

Note that you need the development snapshot of Transformers currently, as support for Mistral hasn't been released into PyPI yet:

```
pip install git+https://github.com/huggingface/transformers
```


# Evaluation

## HuggingFace Leaderboard Performance

We have evaluated using the methodology and tools for the HuggingFace Leaderboard, and find that we have dramatically improved upon the base model.
We find **106%** of the base model's performance on HF Leaderboard evals, averaging **65.84**.

At release time, this beats all 7B and 13B models!

This is also **98.6%** of *`Llama2-70b-chat`*'s performance!

![HF Leaderboard](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca/resolve/main/Images/MistralOrca7BHFLeaderboard.png)


| Metric | Value |
|-----------------------|-------|
| MMLU (5-shot)         | 62.24 |
| ARC (25-shot)         | 64.08 |
| HellaSwag (10-shot)   | 83.99 |
| TruthfulQA (0-shot)   | 53.05 |
| Avg.                  | 65.84 |

We use [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) to run the benchmark tests above, using the same version as the HuggingFace LLM Leaderboard.


## AGIEval Performance

We compare our results to the base Mistral-7B model (using LM Evaluation Harness).

We find **129%** of the base model's performance on AGI Eval, averaging **0.397**.
As well, we significantly improve upon the official `mistralai/Mistral-7B-Instruct-v0.1` finetuning, achieving **119%** of their performance.

![AGIEval Performance](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca/resolve/main/Images/MistralOrca7BAGIEval.png "AGIEval Performance")

## BigBench-Hard Performance

We find **119%** of the base model's performance on BigBench-Hard, averaging **0.416**.

![BigBench-Hard Performance](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca/resolve/main/Images/MistralOrca7BBigBenchHard.png "BigBench-Hard Performance")

## GPT4ALL Leaderboard Performance

We gain a slight edge over our previous releases, again topping the leaderboard, averaging **72.38**.

![GPT4ALL Performance](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca/resolve/main/Images/MistralOrca7BGPT4ALL.png "GPT4ALL Performance")

## MT-Bench Performance

MT-Bench uses GPT-4 as a judge of model response quality, across a wide range of challenges.
We find our performance is *on-par with `Llama2-70b-chat`*, averaging **6.86**.

![MT-Bench Performance](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca/resolve/main/Images/MistralOrca7BMTBENCH.png "MT-Bench Performance")


# Dataset

We used a curated, filtered selection of most of the GPT-4 augmented data from our OpenOrca dataset, which aims to reproduce the Orca Research Paper dataset.


# Training

We trained with 8x A6000 GPUs for 62 hours, completing 4 epochs of full fine tuning on our dataset in one training run.
Commodity cost was ~$400.


# Citation

```bibtex
@software{lian2023mistralorca1
  title = {MistralOrca: Mistral-7B Model Instruct-tuned on Filtered OpenOrcaV1 GPT-4 Dataset},
  author = {Wing Lian and Bleys Goodson and Guan Wang and Eugene Pentland and Austin Cook and Chanvichet Vong and "Teknium"},
  year = {2023},
  publisher = {HuggingFace},
  journal = {HuggingFace repository},
  howpublished = {\url{https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca},
}
@misc{mukherjee2023orca,
      title={Orca: Progressive Learning from Complex Explanation Traces of GPT-4}, 
      author={Subhabrata Mukherjee and Arindam Mitra and Ganesh Jawahar and Sahaj Agarwal and Hamid Palangi and Ahmed Awadallah},
      year={2023},
      eprint={2306.02707},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
@misc{longpre2023flan,
      title={The Flan Collection: Designing Data and Methods for Effective Instruction Tuning}, 
      author={Shayne Longpre and Le Hou and Tu Vu and Albert Webson and Hyung Won Chung and Yi Tay and Denny Zhou and Quoc V. Le and Barret Zoph and Jason Wei and Adam Roberts},
      year={2023},
      eprint={2301.13688},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```

