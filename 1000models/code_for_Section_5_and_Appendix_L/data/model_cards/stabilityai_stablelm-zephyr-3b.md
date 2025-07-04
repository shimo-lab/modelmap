# `StableLM Zephyr 3B`

Please note: For commercial use, please refer to https://stability.ai/license.

## Model Description

`StableLM Zephyr 3B` is a 3 billion parameter instruction tuned inspired by [HugginFaceH4's Zephyr 7B](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) training pipeline this model was trained on a mix of publicly available datasets, synthetic datasets using [Direct Preference Optimization (DPO)](https://arxiv.org/abs/2305.18290), evaluation for this model based on
[MT Bench](https://arxiv.org/abs/2306.05685) and [Alpaca Benchmark](https://tatsu-lab.github.io/alpaca_eval/)

## Usage

`StableLM Zephyr 3B` uses the following instruction format:
```
<|user|>
List 3 synonyms for the word "tiny"<|endoftext|>
<|assistant|>
1. Dwarf
2. Little
3. Petite<|endoftext|>
```

This format is also available through the tokenizer's `apply_chat_template` method:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('stabilityai/stablelm-zephyr-3b')
model = AutoModelForCausalLM.from_pretrained(
    'stabilityai/stablelm-zephyr-3b',
    device_map="auto"
)

prompt = [{'role': 'user', 'content': 'List 3 synonyms for the word "tiny"'}]
inputs = tokenizer.apply_chat_template(
    prompt,
    add_generation_prompt=True,
    return_tensors='pt'
)

tokens = model.generate(
    inputs.to(model.device),
    max_new_tokens=1024,
    temperature=0.8,
    do_sample=True
)

print(tokenizer.decode(tokens[0], skip_special_tokens=False))
```

You can also see how to run a performance optimized version of this model [here](https://github.com/openvinotoolkit/openvino_notebooks/blob/main/notebooks/273-stable-zephyr-3b-chatbot/273-stable-zephyr-3b-chatbot.ipynb) using [OpenVINO](https://docs.openvino.ai/2023.2/home.html) from Intel.

## Model Details

* **Developed by**: [Stability AI](https://stability.ai/)
* **Model type**: `StableLM Zephyr 3B` model is an auto-regressive language model based on the transformer decoder architecture.
* **Language(s)**: English
* **Library**: [Alignment Handbook](https://github.com/huggingface/alignment-handbook.git)
* **Finetuned from model**: [stabilityai/stablelm-3b-4e1t](https://huggingface.co/stabilityai/stablelm-3b-4e1t)
* **License**: [StabilityAI Community License](https://huggingface.co/stabilityai/stablelm-zephyr-3b/raw/main/LICENSE.md).
* **Commercial License**: to use this model commercially, please refer to https://stability.ai/license
* **Contact**: For questions and comments about the model, please email `lm@stability.ai`

### Training Dataset

The dataset is comprised of a mixture of open datasets large-scale datasets available on the [HuggingFace Hub](https://huggingface.co/datasets):
1. SFT Datasets
- HuggingFaceH4/ultrachat_200k
- meta-math/MetaMathQA
- WizardLM/WizardLM_evol_instruct_V2_196k
- Open-Orca/SlimOrca
2. Preference Datasets:
- HuggingFaceH4/ultrafeedback_binarized
- Intel/orca_dpo_pairs

## Performance

### MT-Bench and Alpaca Bench


<img src="https://cdn-uploads.huggingface.co/production/uploads/6310474ca119d49bc1eb0d80/8WIZS6dAlu5kSH-382pMl.png" alt="mt_bench_plot" width="600"/>

| Model | Size | Alignment | MT-Bench (score) | AlpacaEval (win rate %) |
|-------------|-----|----|---------------|--------------|
| **StableLM Zephyr 3B** 🪁 | 3B | DPO | 6.64 | 76.00 |
| StableLM Zephyr (SFT only) | 3B | SFT | 6.04 | 71.15 | 
| Capybara v1.9 | 3B | dSFT | 5.94 | - |
| MPT-Chat |  7B |dSFT |5.42| -|
| Xwin-LM v0.1 | 7B| dPPO| 6.19| 87.83|
| Mistral-Instruct v0.1 | 7B|  - | 6.84 |-|
| Zephyr-7b-α |7B|  dDPO| 6.88| -|
| Zephyr-7b-β| 7B | dDPO | 7.34 | 90.60 |
| Falcon-Instruct |  40B |dSFT |5.17 |45.71|
| Guanaco | 65B |  SFT |6.41| 71.80|
| Llama2-Chat |  70B |RLHF |6.86| 92.66|
| Vicuna v1.3 |  33B |dSFT |7.12 |88.99|
| WizardLM v1.0 |  70B |dSFT |7.71 |-|
| Xwin-LM v0.1 |   70B |dPPO |- |95.57|
| GPT-3.5-turbo | - |RLHF |7.94 |89.37|
| Claude 2 |  - |RLHF |8.06| 91.36|
| GPT-4 |  -| RLHF |8.99| 95.28|

## Other benchmarks:
| Task                | Value                     |
|-----------------------|---------------------------|
| ARC (25-shot)         |  47.0       |
| HellaSwag (10-shot)   | 74.2    |
| MMLU (5-shot)        |   46.3     |
| TruthfulQA (0-shot)   |   46.5 |
| Winogrande (5-shot)   |   65.5 |
| GSM8K (5-shot)        | 42.3        |
| BigBench (Avg) | 35.26 |
| AGI Benchmark (Avg) | 33.23 |

### Training Infrastructure

* **Hardware**: `StableLM Zephyr 3B` was trained on the Stability AI cluster across 8 nodes with 8 A100 80GBs GPUs for each nodes.
* **Code Base**: We use our internal script for SFT steps and used [HuggingFace Alignment Handbook script](https://github.com/huggingface/alignment-handbook) for DPO training.

## Commitment to Ethical AI
In line with our responsibility towards ethical AI development, `StableLM Zephyr 3B` is released with a focus on ensuring safety, reliability, and appropriateness in its applications. To this end, we have evaluated `StableLM Zephyr 3B` on 488 malicious prompts and used standard protocols to assess the harmfulness of its outputs. Compared to Zephyr-7b-β, `StableLM Zephyr 3B` reduces the number of harmful outputs as assessed by GPT-4 by 55. Additionally, we performed an internal red teaming event targeting the following abuse areas:
* **Self-Harm Methods**: (Suicide Methods, Encouragement of Self-Harm, Methods and encouragement of Eating Disorders)
* **Misinformation**: (Health, Conspiracy Theories, Social Unrest/Conflict, Political Misinformation, & Climate change)
* **Hate Speech**: (Race, Stereotypes, Immigrants, Gender,  Personally Identifiable Information such as Social security numbers, Full names, ID numbers, Email addresses, and telephone numbers)

We have incorporated the findings of our malicious prompts evaluation and red teaming event into our release. Users are encouraged to fine-tune and evaluate the model to suit their specific needs, considering the potential biases and limitations found in `StableLM Zephyr 3B` and inherent in other LLM models.

## Use and Limitations

### Intended Use

The model is intended to be used as a foundational base model for application-specific fine-tuning. Developers must evaluate and fine-tune the model for safe performance in downstream applications. For commercial use, please refer to https://stability.ai/membership.

### Limitations and Bias
​
This model is not trained against adversarial inputs. We strongly recommend pairing this model with an input and output classifier to prevent harmful responses.

Through our internal red teaming, we discovered that while the model will not output harmful information if not prompted to do so, it is willing to output potentially harmful outputs or misinformation when the user requests it. Using this model will require guardrails around your inputs and outputs to ensure that any outputs returned are not misinformation or harmful. Additionally, as each use case is unique, we recommend running your own suite of tests to ensure proper performance of this model. Finally, do not use the models if they are unsuitable for your application, or for any applications that may cause deliberate or unintentional harm to others.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_stabilityai__stablelm-zephyr-3b)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |53.43|
|AI2 Reasoning Challenge (25-Shot)|46.08|
|HellaSwag (10-Shot)              |74.16|
|MMLU (5-Shot)                    |46.17|
|TruthfulQA (0-shot)              |46.49|
|Winogrande (5-shot)              |65.51|
|GSM8k (5-shot)                   |42.15|

