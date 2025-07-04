
<p><h1>🐋 Mistral-7B-SlimOrca 🐋</h1></p>


PRE-RELEASE, DEMO MODEL


![OpenOrca Logo](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca/resolve/main/Images/MistralOrcaLogo.png "MistralOrca Logo")
[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)


# OpenOrca - Mistral - 7B - 8k - Slim Data!

We have used our own [OpenOrca dataset](https://huggingface.co/datasets/Open-Orca/OpenOrca) to fine-tune on top of [Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-v0.1). 
This dataset is our attempt to reproduce the dataset generated for Microsoft Research's [Orca Paper](https://arxiv.org/abs/2306.02707).
We use [OpenChat](https://huggingface.co/openchat) packing, trained with [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl).

This model is being released as a demonstration of the performance of our new curated subset of the OpenOrca data: **[SlimOrca](https://huggingface.co/datasets/Open-Orca/SlimOrca)**.

This new dataset release provides an efficient means of reaching performance on-par with using larger slices of our data, while only including ~500k GPT-4 completions.

HF Leaderboard evals place this model as near parity with our recent [MistralOrca](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca) release, which was the #1 model at release time recently.

Codename: "*MistralSlimOrca*"

We are in-process with training more models, so keep a look out on our org for releases coming soon with exciting partners.

We will also give sneak-peak announcements on our Discord, which you can find here:

https://AlignmentLab.ai

or check the OpenAccess AI Collective Discord for more information about Axolotl trainer here:

https://discord.gg/5y8STgB3P3



# Prompt Template

We used [OpenAI's Chat Markup Language (ChatML)](https://github.com/openai/openai-python/blob/main/chatml.md) format, with `<|im_start|>` and `<|im_end|>` tokens added to support this.

This means that, e.g., in [oobabooga](https://github.com/oobabooga/text-generation-webui/) the "`MPT-Chat`" instruction template should work, as it also uses ChatML.

This formatting is also available via a pre-defined [Transformers chat template](https://huggingface.co/docs/transformers/main/chat_templating),
which means that lists of messages can be formatted for you with the `apply_chat_template()` method:

```python
chat = [
  {"role": "system", "content": "You are MistralSlimOrca, a large language model trained by Alignment Lab AI. Write out your reasoning step-by-step to be sure you get the right answers!"}
  {"role": "user", "content": "How are you?"},
  {"role": "assistant", "content": "I am doing well!"},
  {"role": "user", "content": "Please tell me about how mistral winds have attracted super-orcas."},
]
tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
```

which will yield:

```
<|im_start|>system
You are MistralSlimOrca, a large language model trained by Alignment Lab AI. Write out your reasoning step-by-step to be sure you get the right answers!
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

See [this notebook](https://colab.research.google.com/drive/tbd) for inference details.

Note that you need the development snapshot of Transformers currently, as support for Mistral hasn't been released into PyPI yet:

```
pip install git+https://github.com/huggingface/transformers
```


# Evaluation

## HuggingFace Leaderboard Performance

We have evaluated using the methodology and tools for the HuggingFace Leaderboard, and find that we have dramatically improved upon the base model.
We find **106%** of the base model's performance on HF Leaderboard evals, averaging **65.85**.


This is also **98.6%** of *`Llama2-70b-chat`*'s performance!

![HF Leaderboard](https://huggingface.co/Open-Orca/Mistral-7B-SlimOrca/resolve/main/Images/MistralSlimOrca7BHFLeaderboard.png)


| Metric | Value |
|-----------------------|-------|
| MMLU (5-shot)         | 62.77 |
| ARC (25-shot)         | 62.54 |
| HellaSwag (10-shot)   | 83.86 |
| TruthfulQA (0-shot)   | 54.23 |
| Avg.                  | 65.85 |

We use [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) to run the benchmark tests above, using the same version as the HuggingFace LLM Leaderboard.


# Dataset

We used a curated, filtered selection of most of the GPT-4 augmented data from our OpenOrca dataset, which aims to reproduce the Orca Research Paper dataset.

The key change in this dataset is that we've done an additional pass, using GPT-4 to remove answers which appear wrong based on the human annotations from the FLAN dataset.
This reduces the dataset size to only ~500k entries, allowing training to a similar quality level to our previous releases with 2/3 the compute requirement.


# Training

We trained with 8x A6000 GPUs for 40 hours, completing 4 epochs of full fine tuning on our dataset in one training run.
Commodity cost was ~$240.


# Citation

```bibtex
@software{lian2023mistralslimorca1
  title = {MistralSlimOrca: Mistral-7B Model Instruct-tuned on Filtered, Corrected, OpenOrcaV1 GPT-4 Dataset},
  author = {Wing Lian and Bleys Goodson and Guan Wang and Eugene Pentland and Austin Cook and Chanvichet Vong and "Teknium"},
  year = {2023},
  publisher = {HuggingFace},
  url = {https://huggingface.co/Open-Orca/Mistral-7B-SlimOrca}
}
@misc{SlimOrca,
  title = {SlimOrca: An Open Dataset of GPT-4 Augmented FLAN Reasoning Traces, with Verification},
  author = {Wing Lian and Guan Wang and Bleys Goodson and Eugene Pentland and Austin Cook and Chanvichet Vong and "Teknium"},
  year = {2023},
  publisher = {HuggingFace},
  url = {https://https://huggingface.co/Open-Orca/SlimOrca}
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
