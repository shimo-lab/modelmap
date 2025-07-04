
# StableLM-Base-Alpha

📢 **DISCLAIMER**: The StableLM-Base-Alpha models have been superseded. Find the latest versions in the Stable LM Collection [here](https://huggingface.co/collections/stabilityai/stable-lm-650852cfd55dd4e15cdcb30a).

## Model Description

`StableLM-Base-Alpha` is a suite of 3B and 7B parameter decoder-only language models pre-trained on a diverse collection of English and Code datasets with a sequence length of 4096 to push beyond the context window limitations of existing open-source language models.

## Usage

Get started generating text with `StableLM-Base-Alpha` by using the following code snippet:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("StabilityAI/stablelm-base-alpha-3b")
model = AutoModelForCausalLM.from_pretrained("StabilityAI/stablelm-base-alpha-3b")
model.half().cuda()

inputs = tokenizer("What's your mood today?", return_tensors="pt").to("cuda")
tokens = model.generate(
  **inputs,
  max_new_tokens=64,
  temperature=0.7,
  do_sample=True,
)
print(tokenizer.decode(tokens[0], skip_special_tokens=True))
```

## Model Details

* **Developed by**: [Stability AI](https://stability.ai/)
* **Model type**: StableLM-Base-Alpha models are auto-regressive language models based on the NeoX transformer architecture.
* **Language(s)**: English
* **Library**: [GPT-NeoX](https://github.com/EleutherAI/gpt-neox)
* **License**: Base model checkpoints (StableLM-Base-Alpha) are licensed under the Creative Commons license (CC BY-SA-4.0). Under the license, you must give credit to Stability AI, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the Stability AI endorses you or your use.


* **Contact**: For questions and comments about the model, please email `lm@stability.ai`

## Training

| Parameters | Hidden Size | Layers | Heads | Sequence Length |
|------------|-------------|--------|-------|-----------------|
| 3B         | 4096        | 16     | 32    | 4096            |
| 7B         | 6144        | 16     | 48    | 4096            |

### Training Dataset

`StableLM-Base-Alpha` is pre-trained on a new experimental dataset built atop [The Pile](https://huggingface.co/datasets/EleutherAI/the_pile) and is threes times larger at approximately 1.5T tokens.

### Training Procedure

Models are pre-trained on the aforementioned dataset in mixed-precision (FP16), optimized with Adam, and trained using the NeoX tokenizer with a vocabulary size of 50,257. We outline the complete hyperparameters choices in the project's [GitHub repository](https://github.com/Stability-AI/StableLM/blob/main/configs/stablelm-base-alpha-3b.yaml).

## Use and Limitations

### Intended Use

These models are intended to be used by all individuals as foundational models for application-specific fine-tuning without strict limitations on commercial use.

### Limitations and bias

The pre-training dataset may contain offensive or inappropriate content even after applying data cleansing filters which can be reflected in generated text. We recommend users exercise reasonable caution when using these models in production systems. Do not use the models for any applications that may cause harm or distress to individuals or groups.

## Citations

```bibtext
@software{gpt-neox-library,
  title = {{GPT-NeoX: Large Scale Autoregressive Language Modeling in PyTorch}},
  author = {Andonian, Alex and Anthony, Quentin and Biderman, Stella and Black, Sid and Gali, Preetham and Gao, Leo and Hallahan, Eric and Levy-Kramer, Josh and Leahy, Connor and Nestler, Lucas and Parker, Kip and Pieler, Michael and Purohit, Shivanshu and Songz, Tri and Phil, Wang and Weinbach, Samuel},
  url = {https://www.github.com/eleutherai/gpt-neox},
  doi = {10.5281/zenodo.5879544},
  month = {8},
  year = {2021},
  version = {0.0.1},
}
```