
<p align="center" width="100%">
<img src="https://huggingface.co/bofenghuang/vigogne-2-13b-instruct/resolve/main/vigogne_logo.png" alt="Vigogne" style="width: 40%; min-width: 300px; display: block; margin: auto;">
</p>

# Vigogne-2-13B-Instruct: A Llama-2 based French instruction-following model

Vigogne-2-13B-Instruct is a model based on [LLaMA-2-13B](https://ai.meta.com/llama) that has been fine-tuned to follow French instructions.

For more information, please visit the Github repo: https://github.com/bofenghuang/vigogne

**Usage and License Notices**: Vigogne-2-13B-Instruct follows the same usage policy as Llama-2, which can be found [here](https://ai.meta.com/llama/use-policy).

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig
from vigogne.preprocess import generate_instruct_prompt

model_name_or_path = "bofenghuang/vigogne-2-13b-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, padding_side="right", use_fast=False)
model = AutoModelForCausalLM.from_pretrained(model_name_or_path, torch_dtype=torch.float16, device_map="auto")

user_query = "Expliquez la différence entre DoS et phishing."
prompt = generate_instruct_prompt(user_query)
input_ids = tokenizer(prompt, return_tensors="pt")["input_ids"].to(model.device)
input_length = input_ids.shape[1]

generated_outputs = model.generate(
    input_ids=input_ids,
    generation_config=GenerationConfig(
        temperature=0.1,
        do_sample=True,
        repetition_penalty=1.0,
        max_new_tokens=512,
    ),
    return_dict_in_generate=True,
)
generated_tokens = generated_outputs.sequences[0, input_length:]
generated_text = tokenizer.decode(generated_tokens, skip_special_tokens=True)
print(generated_text)
```

You can also infer this model by using the following Google Colab Notebook.

<a href="https://colab.research.google.com/github/bofenghuang/vigogne/blob/main/notebooks/infer_instruct.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

## Example Outputs

*todo*

## Limitations

Vigogne is still under development, and there are many limitations that have to be addressed. Please note that it is possible that the model generates harmful or biased content, incorrect information or generally unhelpful answers.
