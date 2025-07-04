
# Japanese Stable LM Base Gamma 7B

## Model Description

This is a 7B-parameter decoder-only language model with a focus on maximizing Japanese language modeling performance and Japanese downstream task performance.
We conducted continued pretraining using Japanese data on the English language model, [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1), to transfer the model's knowledge and capabilities to Japanese.

*If you are looking for an instruction-following model, check [Japanese Stable LM Instruct Gamma 7B](https://huggingface.co/stabilityai/japanese-stablelm-instruct-gamma-7b)*.

*If you are in search of a smaller model, please check [Japanese StableLM-3B-4E1T Base](https://huggingface.co/stabilityai/japanese-stablelm-3b-4e1t-base).*


## Usage

Ensure you are using Transformers 4.34.0 or newer.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("stabilityai/japanese-stablelm-base-gamma-7b")
model = AutoModelForCausalLM.from_pretrained(
  "stabilityai/japanese-stablelm-base-gamma-7b",
  torch_dtype="auto",
)
model.cuda()
inputs = tokenizer("AI で科学研究を加速するには、", return_tensors="pt").to("cuda")
tokens = model.generate(
  **inputs,
  max_new_tokens=64,
  temperature=0.75,
  top_p=0.95,
  do_sample=True,
)
print(tokenizer.decode(tokens[0], skip_special_tokens=True))
```

## Model Details

* **Developed by**: [Stability AI](https://stability.ai/)
* **Model type**: `Japanese Stable LM Base Gamma 7B` model is an auto-regressive language model based on the transformer decoder architecture.
* **Language(s)**: Japanese
* **License**: This model is licensed under [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
* **Contact**: For questions and comments about the model, please join [Stable Community Japan](https://discord.gg/StableJP). For future announcements / information about Stability AI models, research, and events, please follow https://twitter.com/StabilityAI_JP.

### Model Architecture

For details, please see Mistral AI's [paper](https://arxiv.org/abs/2310.06825) and [release blog post](https://mistral.ai/news/announcing-mistral-7b/). 


### Training Dataset

Around 100B tokens from a mixture of the following corpora were used for the continued pretraining.

- [Japanese/English Wikipedia](https://dumps.wikimedia.org/other/cirrussearch)
- [Japanese mc4](https://huggingface.co/datasets/mc4)
- [Japanese CC-100](http://data.statmt.org/cc-100/ja.txt.xz)
- [Japanese OSCAR](https://oscar-project.github.io/documentation/)
- [SlimPajama](https://huggingface.co/datasets/cerebras/SlimPajama-627B) without the Books3 subset


## Use and Limitations

### Intended Use

The model is intended to be used by all individuals as a foundational model for application-specific fine-tuning without strict limitations on commercial use.

### Limitations and bias

The pre-training dataset may have contained offensive or inappropriate content even after applying data cleansing filters which can be reflected in the model-generated text. We recommend users exercise reasonable caution when using these models in production systems. Do not use the model for any applications that may cause harm or distress to individuals or groups.

## Credits

The continued pre-training was carried out by [Takuya Akiba](https://huggingface.co/iwiwi).
Other aspects, including data preparation and evaluation, were handled by the Language Team of Stability AI Japan, notably [Meng Lee](https://huggingface.co/leemeng), [Fujiki Nakamura](https://huggingface.co/fujiki), [Makoto Shing](https://huggingface.co/mkshing), [Paul McCann](https://huggingface.co/polm-stability), and [Naoki Orii](https://huggingface.co/mrorii).


## Acknowledgements

This model is based on Mistral-7B-v0.1 released by the Mistral AI team. We are grateful to the Mistral AI team for providing such an excellent base model.

We are grateful for the contributions of the EleutherAI Polyglot-JA team in helping us to collect a large amount of pre-training data in Japanese. Polyglot-JA members includes Hyunwoong Ko (Project Lead), Fujiki Nakamura (originally started this project when he commited to the Polyglot team), Yunho Mo, Minji Jung, KeunSeok Im, and Su-Kyeong Jang.

We are also appreciative of [AI Novelist/Sta (Bit192, Inc.)](https://ai-novel.com/index.php) and the numerous contributors from [Stable Community Japan](https://discord.gg/VPrcE475HB) for assisting us in gathering a large amount of high-quality Japanese textual data for model training.