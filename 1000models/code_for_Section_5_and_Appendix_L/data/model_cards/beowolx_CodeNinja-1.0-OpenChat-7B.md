
<p align="center">
<img width="700px" alt="DeepSeek Coder" src="https://cdn-uploads.huggingface.co/production/uploads/64b566ab04fa6584c03b5247/5COagfF6EwrV4utZJ-ClI.png">
</p>
<hr>

# CodeNinja: Your Advanced Coding Assistant

## Overview

CodeNinja is an enhanced version of the renowned model [openchat/openchat-3.5-1210](https://huggingface.co/openchat/openchat-3.5-1210). It having been fine-tuned through Supervised Fine Tuning on two expansive datasets, encompassing over 400,000 coding instructions. Designed to be an indispensable tool for coders, CodeNinja aims to integrate seamlessly into your daily coding routine.

Discover the quantized versions at: [beowolx/CodeNinja-1.0-OpenChat-7B-GGUF](https://huggingface.co/beowolx/CodeNinja-1.0-OpenChat-7B-GGUF).

### Key Features

- **Expansive Training Database**: CodeNinja has been refined with datasets from [glaiveai/glaive-code-assistant-v2](https://huggingface.co/datasets/glaiveai/glaive-code-assistant-v2) and [TokenBender/code_instructions_122k_alpaca_style](https://huggingface.co/datasets/TokenBender/code_instructions_122k_alpaca_style), incorporating around 400,000 coding instructions across various languages including Python, C, C++, Rust, Java, JavaScript, and more.

- **Flexibility and Scalability**: Available in a 7B model size, CodeNinja is adaptable for local runtime environments.

- **Advanced Code Completion**: With a substantial context window size of 8192, it supports comprehensive project-level code completion.

## Prompt Format

CodeNinja maintains the same prompt structure as OpenChat 3.5. Effective utilization requires adherence to this format:

```
GPT4 Correct User: Hello<|end_of_turn|>GPT4 Correct Assistant: Hi<|end_of_turn|>GPT4 Correct User: How are you today?<|end_of_turn|>GPT4 Correct Assistant:
```

🚨 Important: Ensure the use of `<|end_of_turn|>` as the end-of-generation token.

**Adhering to this format is crucial for optimal results.**

## Usage Instructions

### Using LM Studio

The simplest way to engage with CodeNinja is via the [quantized versions](https://huggingface.co/beowolx/CodeNinja-1.0-OpenChat-7B-GGUF) on [LM Studio](https://lmstudio.ai/). Ensure you select the "OpenChat" preset, which incorporates the necessary prompt format. The preset is also available in this [gist](https://gist.github.com/beowolx/b219466681c02ff67baf8f313a3ad817).

### Using the Transformers Library

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Initialize the model
model_path = "beowolx/CodeNinja-1.0-OpenChat-7B"
model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto")
# Load the OpenChat tokenizer
tokenizer = AutoTokenizer.from_pretrained("openchat/openchat-3.5-1210", use_fast=True)

def generate_one_completion(prompt: str):
    messages = [
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": ""}  # Model response placeholder
    ]

    # Generate token IDs using the chat template
    input_ids = tokenizer.apply_chat_template(messages, add_generation_prompt=True)

    # Produce completion
    generate_ids = model.generate(
        torch.tensor([input_ids]).to("cuda"),
        max_length=256,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

    # Process the completion
    completion = tokenizer.decode(generate_ids[0], skip_special_tokens=True)
    completion = completion.split("\n\n\n")[0].strip()

    return completion
```

## License
CodeNinja is licensed under the MIT License, with model usage subject to the Model License.

## Contact
For queries or support, please open an issue in the repository.