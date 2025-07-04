
# Japanese Stable LM Instruct Gamma 7B

## Model Description

This is a 7B-parameter decoder-only Japanese language model fine-tuned on instruction-following datasets, built on top of the base model [Japanese Stable LM Base Gamma 7B](https://huggingface.co/stabilityai/japanese-stablelm-base-gamma-7b).

*If you are in search of a smaller model, please check [Japanese StableLM-3B-4E1T Instruct](https://huggingface.co/stabilityai/japanese-stablelm-3b-4e1t-base/blob/main/README.md).*

## Usage

Ensure you are using Transformers 4.34.0 or newer.

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("stabilityai/japanese-stablelm-instruct-gamma-7b")
model = AutoModelForCausalLM.from_pretrained(
  "stabilityai/japanese-stablelm-instruct-gamma-7b",
  torch_dtype="auto",
)
model.eval()

if torch.cuda.is_available():
    model = model.to("cuda")

def build_prompt(user_query, inputs="", sep="\n\n### "):
    sys_msg = "以下は、タスクを説明する指示と、文脈のある入力の組み合わせです。要求を適切に満たす応答を書きなさい。"
    p = sys_msg
    roles = ["指示", "応答"]
    msgs = [": \n" + user_query, ": \n"]
    if inputs:
        roles.insert(1, "入力")
        msgs.insert(1, ": \n" + inputs)
    for role, msg in zip(roles, msgs):
        p += sep + role + msg
    return p

# Infer with prompt without any additional input
user_inputs = {
    "user_query": "与えられたことわざの意味を小学生でも分かるように教えてください。",
    "inputs": "情けは人のためならず"
}
prompt = build_prompt(**user_inputs)

input_ids = tokenizer.encode(
    prompt, 
    add_special_tokens=True, 
    return_tensors="pt"
)

tokens = model.generate(
    input_ids.to(device=model.device),
    max_new_tokens=256,
    temperature=1,
    top_p=0.95,
    do_sample=True,
)

out = tokenizer.decode(tokens[0][input_ids.shape[1]:], skip_special_tokens=True).strip()
print(out)
```

## Model Details

* **Developed by**: [Stability AI](https://stability.ai/)
* **Model type**: `Japanese Stable LM Instruct Gamma 7B` model is an auto-regressive language model based on the transformer decoder architecture.
* **Language(s)**: Japanese
* **License**: This model is licensed under [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
* **Contact**: For questions and comments about the model, please join [Stable Community Japan](https://discord.gg/StableJP). For future announcements / information about Stability AI models, research, and events, please follow https://twitter.com/StabilityAI_JP.

### Model Architecture

For details, please see Mistral AI's [paper](https://arxiv.org/abs/2310.06825) and [release blog post](https://mistral.ai/news/announcing-mistral-7b/). 


### Training Datasets

- [Japanese translation of the Databricks Dolly-15k dataset](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja)
- [Japanese translation of the subset of the Anthropic HH dataset](https://huggingface.co/datasets/fujiki/japanese_hh-rlhf-49k)
- [Wikinews](https://ja.wikinews.org/wi) [subset](https://huggingface.co/datasets/fujiki/llm-japanese-dataset_wikinews) of the [izumi-lab/llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset)



## Use and Limitations

### Intended Use

The model is intended to be used by all individuals as a foundational model for application-specific fine-tuning without strict limitations on commercial use.

### Limitations and bias

The pre-training dataset may have contained offensive or inappropriate content even after applying data cleansing filters which can be reflected in the model-generated text. We recommend users exercise reasonable caution when using these models in production systems. Do not use the model for any applications that may cause harm or distress to individuals or groups.

## Credits

The fine-tuning was carried out by [Fujiki Nakamura](https://huggingface.co/fujiki).
Other aspects, including data preparation and evaluation, were handled by the Language Team of Stability AI Japan, notably [Meng Lee](https://huggingface.co/leemeng), [Makoto Shing](https://huggingface.co/mkshing), [Paul McCann](https://huggingface.co/polm-stability), [Naoki Orii](https://huggingface.co/mrorii), and  [Takuya Akiba](https://huggingface.co/iwiwi).


## Acknowledgements

This model is based on Mistral-7B-v0.1 released by the Mistral AI team. We are grateful to the Mistral AI team for providing such an excellent base model.

We are grateful for the contributions of the EleutherAI Polyglot-JA team in helping us to collect a large amount of pre-training data in Japanese. Polyglot-JA members includes Hyunwoong Ko (Project Lead), Fujiki Nakamura (originally started this project when he commited to the Polyglot team), Yunho Mo, Minji Jung, KeunSeok Im, and Su-Kyeong Jang.

We are also appreciative of [AI Novelist/Sta (Bit192, Inc.)](https://ai-novel.com/index.php) and the numerous contributors from [Stable Community Japan](https://discord.gg/VPrcE475HB) for assisting us in gathering a large amount of high-quality Japanese textual data for model training.

