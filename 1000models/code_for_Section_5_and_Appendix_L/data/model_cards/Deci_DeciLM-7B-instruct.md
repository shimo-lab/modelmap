# DeciLM-7B-instruct

DeciLM-7B-instruct is a model for short-form instruction following. It is built by LoRA fine-tuning on the [SlimOrca dataset](https://huggingface.co/datasets/Open-Orca/SlimOrca).


## Model Details

### Model Description

DeciLM-7B-instruct is a derivative of the recently released [DeciLM-7B](https://huggingface.co/Deci/DeciLM-7B) language model, a pre-trained, high-efficiency generative text model with 7 billion parameters. DeciLM-7B-instruct is one the best 7B instruct models obtained using simple LoRA fine-tuning, without relying on preference optimization techniques such as RLHF and DPO.

- **Developed by:** [Deci](https://deci.ai/?utm_campaign=repos&utm_source=hugging-face&utm_medium=model-card&utm_content=decilm-7b-instruct)
- **Model type:** DeciLM is an auto-regressive language model using an optimized transformer decoder architecture that includes variable Grouped-Query Attention.
- **Language(s) (NLP):** English
- **License:** Apache 2.0

## Model Architecture

| Parameters | Layers | Heads  | Sequence Length  | GQA num_key_value_heads*  |
|:----------|:----------|:----------|:----------|:----------|
| 7.04 billion    | 32    | 32    | 8192   | Variable  |

*AutoNAC was employed to optimize the selection of the GQA num_key_value_heads for each model layer.


### Model Sources

- **Blog:** [DeciLM-7B Technical Blog](https://deci.ai/blog/introducing-DeciLM-7B-the-fastest-and-most-accurate-7b-large-language-model-to-date/?utm_campaign=repos&utm_source=hugging-face&utm_medium=model-card&utm_content=decilm-7b-instruct)
- **Demo:** [DeciLM-7B-instruct Demo](https://huggingface.co/spaces/Deci/DeciLM-7B-instruct)
- **Finetuning Notebook:** [DeciLM-7B Finetuning Notebook](https://colab.research.google.com/drive/1kEV6i96AQ94xTCvSd11TxkEaksTb5o3U?usp=sharing)
- **Text Generation Notebook:** [DeciLM-7B-instruct Text Generation Notebook](https://bit.ly/declm-7b-instruct)

### Prompt Template
```
### System:
{system_prompt}
### User:
{user_prompt}
### Assistant:
```

## Uses

The model is intended for commercial and research use in English.

## How to Get Started with the Model

Use the code below to get started with the model.

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline

model_name = "Deci/DeciLM-7B-instruct"

device = "cuda" # for GPU usage or "cpu" for CPU usage

quantize = False  # Optional. Useful for GPUs with less than 24GB memory

if quantize:
    dtype_kwargs = dict(quantization_config=BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.bfloat16
    ))
else:
    dtype_kwargs = dict(torch_dtype="auto")

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    trust_remote_code=True,
    **dtype_kwargs
)

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

deci_generator = pipeline("text-generation",
                          model=model,
                          tokenizer=tokenizer,
                          temperature=0.1,
                          device_map="auto",
                          max_length=4096,
                          return_full_text=False)

system_prompt = "You are an AI assistant that follows instruction extremely well. Help as much as you can."

user_prompt = "How do I make the most delicious pancakes the world has ever tasted?"

prompt = tokenizer.apply_chat_template([
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt},
], tokenize=False, add_generation_prompt=True)

response = deci_generator(prompt)[0]['generated_text']
print(prompt + response)
```

## Evaluation

Below are DeciLM-7B and DeciLM-7B-instruct's evaluation results.

| Model | Average | ARC | HellaSwag | MMLU | TruthfulQA | Winogrande | GSM8K | 
|:----------|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|
| DecilLM-7B | 61.55    | 59.39    | 82.51    | 59.76  | 40.33    | 79.95    | 47.38    | 
| DecilLM-7B-instruct | 63.19    | 61.01    | 82.37    | 60.24  | 49.75    | 79.72    | 46.02    | 



### Runtime Benchmarks

| Inference Tool | Hardware | Prompt length | Generation length | Generated tokens/sec | Batch Size | Number of Prompts |
|:----------|:----------|:---------:|:---------:|:---------:|:---------:|:---------:|
| HuggingFace (PyTorch) | A100 (SXM4-80GB-400W) | 512 | 512 | **1174** |  352 | 352 | 
| HuggingFace (PyTorch) | A100 (SXM4-80GB-400W) | 2048 | 2048 | **328** | 72 | 72 |
| Infery-LLM | A100 (SXM4-80GB-400W)| 512 | 512 | **4559**  | 1024 | 4096 |
| Infery-LLM | A100 (SXM4-80GB-400W) | 2048 | 2048 | **3997** | 512 | 2048 | 
| Infery-LLM | A10 | 512 | 512 | **1345** | 128 | 512 |  
| Infery-LLM | A10 | 2048 | 2048 | **599** | 32 | 128 | 

- In order to replicate the results of the Hugging Face benchmarks, you can use this [code example](https://huggingface.co/Deci/DeciLM-7B/blob/main/benchmark_hf_model.py).
- Infery-LLM, Deci's inference engine, features a suite of optimization algorithms, including selective quantization, optimized beam search, continuous batching, and custom CUDA kernels. To explore the full capabilities of Infery-LLM, [schedule a live demo](https://deci.ai/infery-llm-book-a-demo/?utm_campaign=DeciLM%207B%20Launch&utm_source=HF&utm_medium=decilm7b-model-card&utm_term=infery-demo).

## Ethical Considerations and Limitations

DeciLM-7B-instruct is a new technology that comes with inherent risks associated with its use. The testing conducted so far has been primarily in English and does not encompass all possible scenarios. Like those of all large language models, DeciLM-7B's outputs are unpredictable, and the model may generate responses that are inaccurate, biased, or otherwise objectionable. Consequently, developers planning to use DeciLM-7B should undertake thorough safety testing and tuning designed explicitly for their intended applications of the model before deployment.

## How to Cite

Please cite this model using this format.

```bibtex
@misc{DeciFoundationModels,
title = {DeciLM-7B-instruct},
author = {DeciAI Research Team},
year = {2023}
url={https://huggingface.co/Deci/DeciLM-7B-instruct},
}
```