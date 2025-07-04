# Model Card for TowerBase-7B-v0.1

## Model Details

### Model Description

TowerBase-7B is a language model that results from continuing the pretraining of Llama 2 on a mix of 20 billion tokens of monolingual data in ten different languages — English, Portuguese, Spanish, French, German, Dutch, Italian, Korean, Chinese, Russian — and bilingual data. TowerBase-7B-v0.1 is the first model in the series. 
The resulting model shows improved performance on the supported languages, while maintaining Llama 2's capabilities on English. It is particularly well-suited for fine-tuning on translation and related tasks: check out [TowerInstruct](https://huggingface.co/Unbabel/TowerInstruct-7B-v0.1).

We will release more details in the upcoming technical report.

- **Developed by:** Unbabel, Instituto Superior Técnico, CentraleSupélec University of Paris-Saclay 
- **Model type:** A 7B parameter model built on top of Llama 2 by continuing pretraining on multilingual data.
- **Language(s) (NLP):** English, Portuguese, Spanish, French, German, Dutch, Italian, Korean, Chinese, Russian
- **License:** CC-BY-NC-4.0, Llama 2 is licensed under the LLAMA 2 Community License, Copyright © Meta Platforms, Inc. All Rights Reserved.

## Intended uses & limitations

The model is intended for research purposes in the 10 languages it supports.
The model is able to perform well on translation and related tasks (e.g., APE, GEC) on a few-shot regime. 
It can also be fine-tuned to perform these tasks in a zero-shot fashion (see [TowerInstruct](https://huggingface.co/Unbabel/TowerInstruct-7B-v0.1), as well as other multilingual tasks.

### Out-of-Scope Use

The model is not guaranteed to perform well for languages other than the 10 languages it supports.

## Bias, Risks, and Limitations

TowerBase-v0.1 has not been aligned to human preferences, so the model may generate problematic outputs (e.g., hallucinations, harmful content, or false statements). 

## Run the model

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Unbabel/TowerBase-7B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(model_id)

text = "English: My name is TowerBase.\nPortuguese:"
inputs = tokenizer(text, return_tensors="pt")

outputs = model.generate(**inputs, max_new_tokens=20)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### Training Data

Filtered versions of [mc4](https://huggingface.co/datasets/mc4) and bilingual data from various sources (e.g., [OPUS](https://opus.nlpl.eu/)).

## Citation 

```bibtex
@misc{tower_llm_2024,
      title={Tower: An Open Multilingual Large Language Model for Translation-Related Tasks}, 
      author={Duarte M. Alves and José Pombal and Nuno M. Guerreiro and Pedro H. Martins and João Alves and Amin Farajian and Ben Peters and Ricardo Rei and Patrick Fernandes and Sweta Agrawal and Pierre Colombo and José G. C. de Souza and André F. T. Martins},
      year={2024},
      eprint={2402.17733},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```