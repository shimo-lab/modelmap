# Model Card for TowerInstruct-7B-v0.1

## Model Details

### Model Description

TowerInstruct-7B is a language model that results from fine-tuning TowerBase on the TowerBlocks supervised fine-tuning dataset. TowerInstruct-7B-v0.1 is the first model in the series. 
The model is trained to handle several translation-related tasks, such as general machine translation (e.g., sentence- and paragraph-level translation, terminology-aware translation, context-aware translation), automatic post edition, named-entity recognition, gramatical error correction, and paraphrase generation. 
We will release more details in the upcoming technical report.

- **Developed by:** Unbabel, Instituto Superior Técnico, CentraleSupélec University of Paris-Saclay 
- **Model type:** A 7B parameter model fine-tuned on a mix of publicly available, synthetic datasets on translation-related tasks, as well as conversational datasets and code instructions.
- **Language(s) (NLP):** English, Portuguese, Spanish, French, German, Dutch, Italian, Korean, Chinese, Russian
- **License:** CC-BY-NC-4.0, Llama 2 is licensed under the [LLAMA 2 Community License](https://ai.meta.com/llama/license/), Copyright © Meta Platforms, Inc. All Rights Reserved.
- **Finetuned from model:** [TowerBase](https://huggingface.co/Unbabel/TowerBase-7B-v0.1)

## Intended uses & limitations

The model was initially fine-tuned on a filtered and preprocessed supervised fine-tuning dataset ([TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.1)), which contains a diverse range of data sources:
- Translation (sentence and paragraph-level)
- Automatic Post Edition
- Machine Translation Evaluation
- Context-aware Translation
- Terminology-aware Translation
- Multi-reference Translation
- Named-entity Recognition
- Paraphrase Generation
- Synthetic Chat data 
- Code instructions

You can find the dataset and all data sources of [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.1) here.

Here's how you can run the model using the `pipeline()` function from 🤗 Transformers:

```python
# Install transformers from source - only needed for versions <= v4.34
# pip install git+https://github.com/huggingface/transformers.git
# pip install accelerate

import torch
from transformers import pipeline

pipe = pipeline("text-generation", model="Unbabel/TowerInstruct-v0.1", torch_dtype=torch.bfloat16, device_map="auto")
# We use the tokenizer’s chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
messages = [
    {"role": "user", "content": "Translate the following text from Portuguese into English.\nPortuguese: Um grupo de investigadores lançou um novo modelo para tarefas relacionadas com tradução.\nEnglish:"},
]
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=256, do_sample=False)
print(outputs[0]["generated_text"])
# <|im_start|>user
# Translate the following text from Portuguese into English.
# Portuguese: Um grupo de investigadores lançou um novo modelo para tarefas relacionadas com tradução.
# English:<|im_end|>
# <|im_start|>assistant
# A group of researchers has launched a new model for translation-related tasks.
```

### Out-of-Scope Use

The model is not guaranteed to perform for languages other than the 10 languages it supports. Even though we trained the model on conversational data and code instructions, it is not intended to be used as a conversational chatbot or code assistant. 
We are currently working on improving quality and consistency on document-level translation. This model should is not intended to be use as a document-level translator.

## Bias, Risks, and Limitations

TowerInstruct-v0.1 has not been aligned to human preferences, so the model may generate problematic outputs (e.g., hallucinations, harmful content, or false statements).  

## Prompt Format

TowerInstruct-v0.1 was trained using the ChatML prompt templates without any system prompts. An example follows below:
```
<|im_start|>user
{USER PROMPT}<|im_end|>
<|im_start|>assistant
{MODEL RESPONSE}<|im_end|>
<|im_start|>user
[...]
```

### Supervised tasks

The prompts for all supervised tasks can be found in [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.1). We have used multiple prompt templates for each task. While different prompts may offer different outputs, the difference in downstream performance should be very minimal.

## Training Details

### Training Data

Link to [TowerBlocks](https://huggingface.co/datasets/Unbabel/TowerBlocks-v0.1).

#### Training Hyperparameters

The following hyperparameters were used during training:

- total_train_batch_size: 256

- learning_rate: 7e-06

- lr_scheduler_type: cosine

- lr_scheduler_warmup_steps: 500

- weight_decay: 0.01

- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08

- num_epochs: 4

- max_seq_length: 2048

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

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
