
# Tamil LLaMA 7B Instruct v0.1

Welcome to the inaugural release of the Tamil LLaMA 7B instruct model – an important step in advancing LLMs for the Tamil language. This model is ready for immediate inference and is also primed for further fine-tuning to cater to your specific NLP tasks.

To dive deep into the development and capabilities of this model, please read the [research paper](https://arxiv.org/abs/2311.05845) and the [introductory blog post (WIP)]() that outlines our journey and the model's potential impact.

## Model description

The Tamil LLaMA models have been enhanced and tailored specifically with an extensive Tamil vocabulary of 16,000 tokens, building upon the foundation set by the original LLaMA-2.

- **Model type:** A 7B parameter GPT-like model fine-tuned on [Tamil-Alpaca-Orca](https://huggingface.co/datasets/abhinand/tamil-alpaca-orca) - a mix of Tamil-translated [Stanford-Alpaca](https://huggingface.co/datasets/tatsu-lab/alpaca) and a subset of [OpenOrca](https://huggingface.co/datasets/Open-Orca/OpenOrca) datasets.
- **Language(s):** Tamil and English
- **License:** GNU General Public License v3.0
- **Finetuned from model:** [abhinand/tamil-llama-7b-base-v0.1](https://huggingface.co/abhinand/tamil-llama-7b-base-v0.1)
- **Training Precision:** `float16`
- **Code:** [GitHub](https://github.com/abhinand5/tamil-llama)

## Prompting Format

**Prompt Template Without Input**

```
{system_prompt}

### Instruction:
{instruction or query}

### Response:
{response}
```

**Prompt Template With Input**

```
{system_prompt}

### Instruction:
{instruction or query}

### Input:
{input}

### Response:
{response}
```

## Related Models

| Model                    | Type                        | Data              | Base Model           | # Params | Download Links                                                         |
|--------------------------|-----------------------------|-------------------|----------------------|------|------------------------------------------------------------------------|
| Tamil LLaMA 7B Base      | Base model                  | 12GB              | LLaMA 7B             | 7B   | [HF Hub](https://huggingface.co/abhinand/tamil-llama-7b-base-v0.1)     |
| Tamil LLaMA 13B Base     | Base model                  | 4GB               | LLaMA 13B            | 13B  | [HF Hub](https://huggingface.co/abhinand/tamil-llama-13b-base-v0.1)    |
| Tamil LLaMA 7B Instruct  | Instruction following model | 145k instructions | Tamil LLaMA 7B Base  | 7B   | [HF Hub](https://huggingface.co/abhinand/tamil-llama-7b-instruct-v0.1) |
| Tamil LLaMA 13B Instruct | Instruction following model | 145k instructions | Tamil LLaMA 13B Base | 13B  | [HF Hub](abhinand/tamil-llama-13b-instruct-v0.1)                       |

## Usage Note

It's important to note that the models have not undergone detoxification. Therefore, while they possess impressive linguistic capabilities, there is a possibility for them to generate content that could be deemed harmful or offensive. We urge users to exercise discretion and supervise the model's outputs closely, especially in public or sensitive applications.

## Meet the Developers

Get to know the creators behind this innovative model and follow their contributions to the field:

- [Abhinand Balachandran](https://www.linkedin.com/in/abhinand-05/)

## Citation

If you use this model or any of the the Tamil-Llama datasets in your research, please cite:

```bibtex
@misc{balachandran2023tamilllama,
      title={Tamil-Llama: A New Tamil Language Model Based on Llama 2}, 
      author={Abhinand Balachandran},
      year={2023},
      eprint={2311.05845},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

We hope this model serves as a valuable tool in your NLP toolkit and look forward to seeing the advancements it will enable in the understanding and generation of the Tamil language.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_abhinand__tamil-llama-7b-instruct-v0.1)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |45.52|
|AI2 Reasoning Challenge (25-Shot)|48.04|
|HellaSwag (10-Shot)              |70.97|
|MMLU (5-Shot)                    |39.95|
|TruthfulQA (0-shot)              |41.70|
|Winogrande (5-shot)              |70.64|
|GSM8k (5-shot)                   | 1.82|

