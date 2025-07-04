# `StableLM 2 12B Chat`

## Model Description

`Stable LM 2 12B Chat` is a 12 billion parameter instruction tuned language model trained on a mix of publicly available datasets and synthetic datasets, utilizing [Direct Preference Optimization (DPO)](https://arxiv.org/abs/2305.18290).

## Usage

**NOTE**: This model requires `transformers>=4.40.0`

`StableLM 2 12B Chat` uses the following instruction ChatML format.
This format is also available through the tokenizer's `apply_chat_template` method:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('stabilityai/stablelm-2-12b-chat')
model = AutoModelForCausalLM.from_pretrained(
    'stabilityai/stablelm-2-12b-chat',
    device_map="auto",
)

prompt = [{'role': 'user', 'content': 'Implement snake game using pygame'}]
inputs = tokenizer.apply_chat_template(
    prompt,
    add_generation_prompt=True,
    return_tensors='pt'
)

tokens = model.generate(
    inputs.to(model.device),
    max_new_tokens=100,
    temperature=0.7,
    do_sample=True,
)
output = tokenizer.decode(tokens[:, inputs.shape[-1]:][0], skip_special_tokens=False)

print(output)
```

StableLM 2 12B Chat also supports function calling. The following is an example of how to use it:
```python
system_prompt = """\
You are a helpful assistant with access to the following functions. You must use them if required -\n
[
  {
    "type": "function",
    "function": {
      "name": "TextToImage",
      "description": "This function is able to create, draw, or illustrate an image from a text prompt.",
      "parameters": {
        "type": "object",
        "properties": {
          "prompt": {
            "type": "string",
            "description": "The description of image that the user wants to create."
          }
        },
        "required": [
          "prompt"
        ]
      }
    }
  }
]
"""
messages = [
    {'role': 'system', 'content': system_prompt},
    {'role': "user", 'content': "Please, generate a picture of the Eiffel Tower at night!"}
]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors='pt'
)

tokens = model.generate(
    inputs.to(model.device),
    max_new_tokens=1024,
    temperature=0.5,
    do_sample=True
)
output = tokenizer.decode(tokens[:, inputs.shape[-1]:][0], skip_special_tokens=True)

print(output)
"""
[
  {
    "name": "TextToImage",
    "arguments": {
      "prompt": "Eiffel Tower at night."
    }
  }
]
"""

```

## Model Details

* **Developed by**: [Stability AI](https://stability.ai/)
* **Model type**: `StableLM 2 12B Chat` model is an auto-regressive language model based on the transformer decoder architecture.
* **Language(s)**: English
* **Paper**: [Stable LM 2 Chat Technical Report]((https://arxiv.org/abs/2402.17834)
* **Library**: [Alignment Handbook](https://github.com/huggingface/alignment-handbook.git)
* **Finetuned from model**: 
* **License**: [StabilityAI Non-Commercial Research Community License](https://huggingface.co/stabilityai/stablelm-2-zephyr-1_6b/blob/main/LICENSE). If you want to use this model for your commercial products or purposes, please contact us [here](https://stability.ai/contact) to learn more.
* **Contact**: For questions and comments about the model, please email `lm@stability.ai`.

### Training Dataset

The dataset is comprised of a mixture of open datasets large-scale datasets available on the [HuggingFace Hub](https://huggingface.co/datasets) as well as an internal safety dataset:
1. SFT Datasets
- HuggingFaceH4/ultrachat_200k
- meta-math/MetaMathQA
- WizardLM/WizardLM_evol_instruct_V2_196k
- Open-Orca/SlimOrca
- openchat/openchat_sharegpt4_dataset
- LDJnr/Capybara
- hkust-nlp/deita-10k-v0
- teknium/OpenHermes-2.5
- glaiveai/glaive-function-calling-v2

2. Safety Datasets:
- Anthropic/hh-rlhf
- Internal Safety Dataset

3. Preference Datasets:
- argilla/dpo-mix-7k

## Performance

### MT-Bench

| Model                                 | Parameters | MT Bench (Inflection-corrected) |
|---------------------------------------|------------|---------------------------------|
| mistralai/Mixtral-8x7B-Instruct-v0.1 | 13B/47B    | 8.48 ± 0.06                    |
| stabilityai/stablelm-2-12b-chat       | 12B        | 8.15 ± 0.08                    |
| Qwen/Qwen1.5-14B-Chat                 | 14B        | 7.95 ± 0.10                    |
| HuggingFaceH4/zephyr-7b-gemma-v0.1    | 8.5B       | 7.82 ± 0.03                    |
| mistralai/Mistral-7B-Instruct-v0.2    | 7B         | 7.48 ± 0.02                    |
| meta-llama/Llama-2-70b-chat-hf        | 70B        | 7.29 ± 0.05                    |

### OpenLLM Leaderboard

| Model                                  | Parameters | Average | ARC Challenge (25-shot) | HellaSwag (10-shot) | MMLU (5-shot) | TruthfulQA (0-shot) | Winogrande (5-shot) | GSM8K (5-shot) |
| -------------------------------------- | ---------- | ------- | ---------------------- | ------------------- | ------------- | ------------------- | ------------------- | -------------- |
| mistralai/Mixtral-8x7B-Instruct-v0.1  | 13B/47B    | 72.71   | 70.14                  | 87.55               | 71.40         | 64.98               | 81.06               | 61.11          |
| stabilityai/stablelm-2-12b-chat        | 12B        | 68.45   | 65.02                  | 86.06               | 61.14         | 62.00               | 78.77               | 57.70          |
| Qwen/Qwen1.5-14B                       | 14B        | 66.70   | 56.57                  | 81.08               | 69.36         | 52.06               | 73.48               | 67.63          |
| mistralai/Mistral-7B-Instruct-v0.2     | 7B         | 65.71   | 63.14                  | 84.88               | 60.78         | 60.26               | 77.19               | 40.03          |
| HuggingFaceH4/zephyr-7b-gemma-v0.1     | 8.5B       | 62.41   | 58.45                  | 83.48               | 60.68         | 52.07               | 74.19               | 45.56          |
| Qwen/Qwen1.5-14B-Chat                  | 14B        | 62.37   | 58.79                  | 82.33               | 68.52         | 60.38               | 73.32               | 30.86          |
| google/gemma-7b                        | 8.5B       | 63.75   | 61.09                  | 82.20               | 64.56         | 44.79               | 79.01               | 50.87          |
| stabilityai/stablelm-2-12b             | 12B        | 63.53   | 58.45                  | 84.33               | 62.09         | 48.16               | 78.10               | 56.03          |
| mistralai/Mistral-7B-v0.1              | 7B         | 60.97   | 59.98                  | 83.31               | 64.16         | 42.15               | 78.37               | 37.83          |
| meta-llama/Llama-2-13b-hf              | 13B        | 55.69   | 59.39                  | 82.13               | 55.77         | 37.38               | 76.64               | 22.82          |
| meta-llama/Llama-2-13b-chat-hf         | 13B        | 54.92   | 59.04                  | 81.94               | 54.64         | 41.12               | 74.51               | 15.24          |

## Use and Limitations

### Intended Use

The model is intended to be used in chat-like applications. Developers must evaluate the model for safety performance in their specific use case. Read more about [safety and limitations](#limitations-and-bias) below.

### Limitations and Bias

We strongly recommend pairing this model with an input and output classifier to prevent harmful responses.
Using this model will require guardrails around your inputs and outputs to ensure that any outputs returned are not hallucinations.
Additionally, as each use case is unique, we recommend running your own suite of tests to ensure proper performance of this model.
Finally, do not use the models if they are unsuitable for your application, or for any applications that may cause deliberate or unintentional harm to others.

## How to Cite

```
@article{bellagente2024stable,
  title={Stable LM 2 1.6 B Technical Report},
  author={Bellagente, Marco and Tow, Jonathan and Mahan, Dakota and Phung, Duy and Zhuravinskyi, Maksym and Adithyan, Reshinth and Baicoianu, James and Brooks, Ben and Cooper, Nathan and Datta, Ashish and others},
  journal={arXiv preprint arXiv:2402.17834},
  year={2024}
}
```
