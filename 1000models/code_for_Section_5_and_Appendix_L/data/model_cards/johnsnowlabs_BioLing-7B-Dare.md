
# BioLing-7B-Dare
[<img src="https://repository-images.githubusercontent.com/104670986/2e728700-ace4-11ea-9cfc-f3e060b25ddf">](http://www.johnsnowlabs.com)


This model is developed by [John Snow Labs](https://www.johnsnowlabs.com/).

This model is available under a [CC-BY-NC-ND](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.en) license and must also conform to this [Acceptable Use Policy](https://huggingface.co/johnsnowlabs). If you need to license  this model for commercial use, please contact us at info@johnsnowlabs.com.


## 🧩 Configuration

```yaml
models:
  - model: BioMistral/BioMistral-7B
    parameters:
      density: 0.53
      weight: 0.4
  - model: Nexusflow/Starling-LM-7B-beta
    parameters:
      density: 0.53
      weight: 0.3

merge_method: dare_ties
base_model: BioMistral/BioMistral-7B
parameters:
  int8_mask: true
dtype: bfloat16
```

## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "johnsnowlabs/BioLing-7B-Dare"
messages = [{"role": "user", "content": "What is a large language model?"}]

tokenizer = AutoTokenizer.from_pretrained(model)
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

outputs = pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])
```
## 🏆 Evaluation
Coming Soon!