
# Tamil LLaMA 7B Base v0.1 [pre-trained]

Welcome to the inaugural release of the Tamil LLaMA 7B base model – an important step in advancing LLMs for the Tamil language. This model is ready for immediate inference and is also primed for further fine-tuning to cater to your specific NLP tasks.

To dive deep into the development and capabilities of this model, please read the [research paper](https://arxiv.org/abs/2311.05845) and the [introductory blog post (WIP)]() that outlines our journey and the model's potential impact.

> **Please Note:** This model, labeled as a foundational Tamil Language Model (LLM), is designed primarily for Causal Language Modeling (LM) purposes. In other words, if you are looking for an instruction following model in Tamil, you may find [abhinand/tamil-llama-7b-instruct-v0.1](https://huggingface.co/abhinand/tamil-llama-7b-instruct-v0.1) more suitable for your needs.

## Model description

The Tamil LLaMA models have been enhanced and tailored specifically with an extensive Tamil vocabulary of 16,000 tokens, building upon the foundation set by the original LLaMA-2.

- **Model type:** A 7B parameter model for Causal LM pre-trained on [CulturaX](https://huggingface.co/datasets/uonlp/CulturaX) dataset's Tamil subset.
- **Language(s):** Tamil and English
- **License:** GNU General Public License v3.0
- **Source Model:** [meta-llama/Llama-2-7b-hf](https://huggingface.co/meta-llama/Llama-2-7b-hf)
- **Training Precision:** `float16`
- **Code:** [GitHub](https://github.com/abhinand5/tamil-llama)

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

If you use this model or the Tamil-Llama dataset in your research, please cite:

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