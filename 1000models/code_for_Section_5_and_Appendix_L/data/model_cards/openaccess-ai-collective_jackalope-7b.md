
<p><h1>🐰🦌 Jackalope 7B 🐰🦌</h1></p>


![Jackalope Logo](https://huggingface.co/openaccess-ai-collective/jackalope-7b/resolve/main/images/jackalope.jpg "Jackalope Logo")
[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)


# Jackalope 7B

We have used the [SlimOrca dataset](https://huggingface.co/datasets/Open-Orca/SlimOrca), PIPPA, and various other open datasets
to fine-tune on top of [Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-v0.1).

This dataset is our attempt to reproduce the dataset generated for Microsoft Research's [Orca Paper](https://arxiv.org/abs/2306.02707).
We use [OpenChat](https://huggingface.co/openchat) packing, trained with [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl).

This release highlights the efficiency of SlimOrca, while improving the ability of the model's multi-turn chat.

HF Leaderboard evals puts this model only slightly below the MistralOrca release, but can be considered a 
reasonable tradeoff for a more general model that can handle multi-turn chat.

If you'd like to try the model now, we have it running on fast GPUs unquantized: https://huggingface.co/spaces/openaccess-ai-collective/jackalope-7b


Join the OpenAccess AI Collective Discord for more information about Axolotl trainer and other OAAIC models here:

https://discord.gg/5y8STgB3P3

Also join the AlignmentLab Discord for sneak-peak announcements:

https://AlignmentLab.ai



# Quantized Models

Quantized versions of this model are generously made available by [TheBloke](https://huggingface.co/TheBloke).

- AWQ: https://huggingface.co/TheBloke/Jackalope-7B-AWQ
- GPTQ: https://huggingface.co/TheBloke/Jackalope-7B-GPTQ
- GGUF: https://huggingface.co/TheBloke/Jackalope-7B-GGUF


# Prompt Template

We used [OpenAI's Chat Markup Language (ChatML)](https://github.com/openai/openai-python/blob/main/chatml.md) format, with `<|im_start|>` and `<|im_end|>` tokens added to support this.

This means that, e.g., in [oobabooga](https://github.com/oobabooga/text-generation-webui/) the "`MPT-Chat`" instruction template should work, as it also uses ChatML.

This formatting is also available via a pre-defined [Transformers chat template](https://huggingface.co/docs/transformers/main/chat_templating),
which means that lists of messages can be formatted for you with the `apply_chat_template()` method:

```python
chat = [
  {"role": "system", "content": "You are JackalopeAI, a large language model trained by OpenAccess AI Collective. Write out your reasoning step-by-step to be sure you get the right answers!"}
  {"role": "user", "content": "How are you?"},
  {"role": "assistant", "content": "I am doing well!"},
  {"role": "user", "content": "Please tell me about the mythical creatures called jackalopes."},
]
tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
```

which will yield:

```
<|im_start|>system
You are JackalopeAI. Write out your reasoning step-by-step to be sure you get the right answers!
<|im_end|>
<|im_start|>user
How are you?<|im_end|>
<|im_start|>assistant
I am doing well!<|im_end|>
<|im_start|>user
Please tell me about the mythical creatures called jackalopes.<|im_end|>
<|im_start|>assistant
```

If you use `tokenize=True` and `return_tensors="pt"` instead, then you will get a tokenized
and formatted conversation ready to pass to `model.generate()`.


# Evaluation

## HuggingFace Leaderboard Performance

![All benchmarks](https://huggingface.co/openaccess-ai-collective/jackalope-7b/resolve/main/images/bench.png)


| Metric | Value |
|-----------------------|--|
| MMLU (5-shot)         | 63.63 |
| ARC (25-shot)         | 63.31 |
| HellaSwag (10-shot)   | 83.29 |
| TruthfulQA (0-shot)   | 49.99 |
| Avg.                  | 65.06 |

We use [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) to run the benchmark tests above, using the same version as the HuggingFace LLM Leaderboard.

# Dataset

We used a verified, curated, filtered selection of most of the GPT-4 augmented data from the OpenOrca dataset.
Additionally we include multi-turn chat from PIPPA, various datasets 
by LDJ from Nous Research, MetaMathQA, and Chain-of-Thought augmented data from the train split of RiddleSense.

- [Open-Orca/OpenOrca](https://huggingface.co/datasets/Open-Orca/OpenOrca)
- [LDJnr/LessWrong-Amplify-Instruct](https://huggingface.co/datasets/LDJnr/LessWrong-Amplify-Instruct)
- [LDJnr/Pure-Dove](https://huggingface.co/datasets/LDJnr/Pure-Dove)
- [LDJnr/Verified-Camel](https://huggingface.co/datasets/LDJnr/Verified-Camel)
- [PygmalionAI/PIPPA](https://huggingface.co/datasets/PygmalionAI/PIPPA)
- [meta-math/MetaMathQA](https://huggingface.co/datasets/meta-math/MetaMathQA)
- [riddle_sense](https://huggingface.co/datasets/riddle_sense)


# Training

We trained with 8x A6000 GPUs for 96 hours, completing 4 epochs of full fine tuning on our dataset in one training run.
Commodity cost was ~$650.


# Citation

```bibtex
@software{lian2023jackalope,
  title = {Jackalope 7B: Mistral-7B Model Multi-Turn Chat tuned on Filtered OpenOrcaV1 GPT-4 Dataset},
  author = {Wing Lian and Bleys Goodson and Guan Wang and Eugene Pentland and Austin Cook and Chanvichet Vong and "Teknium"},
  year = {2023},
  publisher = {HuggingFace},
  journal = {HuggingFace repository},
  howpublished = {\url{openaccess-ai-collective/jackalope-7b},
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
