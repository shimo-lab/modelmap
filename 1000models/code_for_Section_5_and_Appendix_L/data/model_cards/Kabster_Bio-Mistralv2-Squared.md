# Bio-Mistralv2-Squared-SLERP

Bio-Mistralv2-Squared is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the SLERP merge method.

### 🤖💬 Models Merged

The following models were included in the merge:
* [BioMistral/BioMistral-7B](https://huggingface.co/BioMistral/BioMistral-7B)
* [mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)

### 🧩 Configuration

The following YAML configuration was used to produce this model:

```yaml

slices:
  - sources:
      - model: BioMistral/BioMistral-7B
        layer_range: [0, 32]
      - model: mistralai/Mistral-7B-Instruct-v0.2
        layer_range: [0, 32]
merge_method: slerp
base_model: BioMistral/BioMistral-7B
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16

```

### 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "Kabster/Bio-Mistralv2-Squared"
messages = [{"role": "user", "content": "What is fluimucil used for?"}]

tokenizer = AutoTokenizer.from_pretrained(model)
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

outputs = pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.2, top_k=100, top_p=0.95)
print(outputs[0]["generated_text"])
```