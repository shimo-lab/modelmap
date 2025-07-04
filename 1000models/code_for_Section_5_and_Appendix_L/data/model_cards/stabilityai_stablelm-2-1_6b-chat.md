# `StableLM 2 Chat 1.6B`

## Model Description

`Stable LM 2 Chat 1.6B` is a 1.6 billion parameter instruction tuned language model inspired by [HugginFaceH4's Zephyr 7B](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) training pipeline. The model is trained on a mix of publicly available datasets and synthetic datasets, utilizing [Direct Preference Optimization (DPO)](https://arxiv.org/abs/2305.18290).

## Usage

`StableLM 2 1.6B Chat` uses the following ChatML format:


```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('stabilityai/stablelm-2-1_6b-chat')
model = AutoModelForCausalLM.from_pretrained(
    'stabilityai/stablelm-2-1_6b-chat',
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
    do_sample=True
)
output = tokenizer.decode(tokens[:, inputs.shape[-1]:][0], skip_special_tokens=False)

print(output)
```


## Model Details

* **Developed by**: [Stability AI](https://stability.ai/)
* **Model type**: `StableLM 2 Chat 1.6B` model is an auto-regressive language model based on the transformer decoder architecture.
* **Language(s)**: English
* **Paper**: [Stable LM 2 1.6B Technical Report](https://drive.google.com/file/d/1JYJHszhS8EFChTbNAf8xmqhKjogWRrQF/view?usp=sharing)
* **Library**: [Alignment Handbook](https://github.com/huggingface/alignment-handbook.git)
* **Finetuned from model**: [https://huggingface.co/stabilityai/stablelm-2-1_6b](https://huggingface.co/stabilityai/stablelm-2-1_6b)
* **License**: [StabilityAI Non-Commercial Research Community License](https://huggingface.co/stabilityai/stablelm-2-1_6b-chat/blob/main/LICENSE). If you want to use this model for your commercial products or purposes, please contact us [here](https://stability.ai/contact) to learn more.
* **Contact**: For questions and comments about the model, please email `lm@stability.ai`

### Training Dataset

The dataset is comprised of a mixture of open datasets large-scale datasets available on the [HuggingFace Hub](https://huggingface.co/datasets):
1. SFT Datasets
- HuggingFaceH4/ultrachat_200k
- meta-math/MetaMathQA
- WizardLM/WizardLM_evol_instruct_V2_196k
- Open-Orca/SlimOrca
- openchat/openchat_sharegpt4_dataset
- LDJnr/Capybara
- hkust-nlp/deita-10k-v0
- teknium/OpenHermes-2.5

2. Preference Datasets:
- allenai/ultrafeedback_binarized_cleaned
- Intel/orca_dpo_pairs
- argilla/dpo-mix-7k

## Performance

### MT-Bench

| Model                   | Size | MT-Bench |
|-------------------------|------|----------|
| Mistral-7B-Instruct-v0.2| 7B   | 7.61     |
| Llama2-Chat             | 70B  | 6.86     |
| stablelm-zephyr-3b      | 3B   | 6.64     |
| MPT-30B-Chat            | 30B  | 6.39     |
| **stablelm-2-1_6b-chat**    | **1.6B** | **5.83**     |
| stablelm-2-zephyr-1.6b  | 1.6B | 5.42     |
| Falcon-40B-Instruct     | 40B  | 5.17     |
| Qwen-1.8B-Chat          | 1.8B | 4.95     |
| dolphin-2.6-phi-2       | 2.7B | 4.93     |
| phi-2                   | 2.7B | 4.29     |
| TinyLlama-1.1B-Chat-v1.0| 1.1B | 3.46     |

### OpenLLM Leaderboard

| Model                                  | Size | Average | ARC Challenge (acc_norm) | HellaSwag (acc_norm) | MMLU (acc_norm) | TruthfulQA (mc2) | Winogrande (acc) | Gsm8k (acc) |
|----------------------------------------|------|---------|-------------------------|----------------------|-----------------|------------------|------------------|-------------|
| microsoft/phi-2                        | 2.7B | 61.32%  | 61.09%                  | 75.11%               | 58.11%          | 44.47%           | 74.35%           | 54.81%      |
| **stabilityai/stablelm-2-1_6b-chat**       | 1.6B | 50.80%  | 43.94%                  | 69.22%               | 41.59%          | 46.52%           | 64.56%            | 38.96%       |
| stabilityai/stablelm-2-zephyr-1_6b     | 1.6B | 49.89%  | 43.69%                  | 69.34%               | 41.85%          | 45.21%           | 64.09%           | 35.18%      |
| microsoft/phi-1_5                      | 1.3B | 47.69%  | 52.90%                  | 63.79%               | 43.89%          | 40.89%           | 72.22%           | 12.43%      |
| stabilityai/stablelm-2-1_6b            | 1.6B | 45.54%  | 43.43%                  | 70.49%               | 38.93%          | 36.65%           | 65.90%           | 17.82%      |
| mosaicml/mpt-7b                        | 7B   | 44.28%  | 47.70%                  | 77.57%               | 30.80%          | 33.40%           | 72.14%           | 4.02%       |
| KnutJaegersberg/Qwen-1_8B-Llamaified*  | 1.8B | 44.75%  | 37.71%                  | 58.87%               | 46.37%          | 39.41%           | 61.72%           | 24.41%      |
| openlm-research/open_llama_3b_v2       | 3B   | 40.28%  | 40.27%                  | 71.60%               | 27.12%          | 34.78%           | 67.01%           | 0.91%       |
| iiuae/falcon-rw-1b                     | 1B   | 37.07%  | 35.07%                  | 63.56%               | 25.28%          | 35.96%           | 62.04%           | 0.53%       |
| TinyLlama/TinyLlama-1.1B-3T            | 1.1B | 36.40%  | 33.79%                  | 60.31%               | 26.04%          | 37.32%           | 59.51%           | 1.44%       |


## Use and Limitations

### Intended Use

The model is intended to be used in chat-like applications. Developers must evaluate the model for safety performance in their specific use case. Read more about [safety and limitations](#limitations-and-bias) below.

### Limitations and Bias
​
This model is not trained against adversarial inputs. We strongly recommend pairing this model with an input and output classifier to prevent harmful responses.

Through our internal red teaming, we discovered that while the model will not output harmful information if not prompted to do so, it will hallucinate many facts. It is also willing to output potentially harmful outputs or misinformation when the user requests it.
Using this model will require guardrails around your inputs and outputs to ensure that any outputs returned are not misinformation or harmful.
Additionally, as each use case is unique, we recommend running your own suite of tests to ensure proper performance of this model.
Finally, do not use the models if they are unsuitable for your application, or for any applications that may cause deliberate or unintentional harm to others.


## How to Cite

```bibtex
@misc{StableLM-2-1.6B,
      url={[https://huggingface.co/stabilityai/stablelm-2-1.6b](https://huggingface.co/stabilityai/stablelm-2-1.6b)},
      title={Stable LM 2 1.6B},
      author={Stability AI Language Team}
}
```