Model that is fine-tuned in 4-bit precision using QLoRA on [timdettmers/openassistant-guanaco](https://huggingface.co/datasets/timdettmers/openassistant-guanaco) and sharded to be used on a free Google Colab instance that can be loaded with 4bits. 

It can be easily imported using the `AutoModelForCausalLM` class from `transformers`:

```
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
          "guardrail/llama-2-7b-guanaco-instruct-sharded",
          load_in_4bit=True)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

```