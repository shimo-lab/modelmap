![img](https://huggingface.co/circulus/Llama-2-13b-orca-v1/resolve/main/llama.jpg)

```
model_name = "circulus/Llama-2-13b-orca-v1"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.bfloat16, bnb_4bit_use_double_quant=True)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", quantization_config=config)
```