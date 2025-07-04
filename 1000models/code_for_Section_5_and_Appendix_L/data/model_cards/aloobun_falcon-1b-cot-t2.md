
### Prompt template : chatml

fintuned for CoT reasoning.

```
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

model = "aloobun/falcon-1b-cot-t2"
tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
sequences = pipeline(
   "<|im_start|>user\nDoes P=NP?<|im_end|>\n<|im_start|>assistant\n",
    max_length=256,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")
```

>Fine-tuning language models is like tuning the strings of an AI banjo in the cosmic saloon of the digital frontier. We're not just slinging code; it's a harmonious quest to shape the minds of silicon wanderers, crafting binary ballads and electronic echoes. Picture it as cybernetic bardic magic, where we, the tech sorcerers, weave algorithms with strands of imagination. But, in this cosmic hoedown, there's a twist – as we twang the strings of artificial intelligence, we're also seeding the algorithms with a bit of human stardust, adding quirks and quirksome biases. So, as we two-step into this frontier of creation, are we summoning AI troubadours of the future or just conjuring interstellar jesters, spinning tales of silicon whimsy and digital campfire banter?