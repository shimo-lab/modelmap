
<p align="center" width="100%">
<img src="https://huggingface.co/bofenghuang/vigogne-2-7b-chat/resolve/v2.0/logo_v2.jpg" alt="Vigogne" style="width: 30%; min-width: 300px; display: block; margin: auto;">
</p>

# Vigogne-2-7B-Chat-V2.0: A Llama-2-based French Chat LLM

Vigogne-2-7B-Chat-V2.0 is a French chat LLM, based on [LLaMA-2-7B](https://ai.meta.com/llama), optimized to generate helpful and coherent responses in conversations with users.

Check out our [release blog](https://github.com/bofenghuang/vigogne/blob/main/blogs/2023-08-17-vigogne-chat-v2_0.md) and [GitHub repository](https://github.com/bofenghuang/vigogne) for more information.

**Usage and License Notices**: Vigogne-2-7B-Chat-V2.0 follows Llama-2's [usage policy](https://ai.meta.com/llama/use-policy). A significant portion of the training data is distilled from GPT-3.5-Turbo and GPT-4, kindly use it cautiously to avoid any violations of OpenAI's [terms of use](https://openai.com/policies/terms-of-use).

## Changelog

All previous versions are accessible through branches.

- **V1.0**: Trained on 420K chat data.
- **V2.0**: Trained on 520K data. Check out our [release blog](https://github.com/bofenghuang/vigogne/blob/main/blogs/2023-08-17-vigogne-chat-v2_0.md) for more details.

## Prompt Template

We utilized prefix tokens `<user>:` and `<assistant>:` to distinguish between user and assistant utterances.

You can apply this formatting using the [chat template](https://huggingface.co/docs/transformers/main/chat_templating) through the `apply_chat_template()` method.

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bofenghuang/vigogne-2-7b-chat")

conversation = [
    {"role": "user", "content": "Bonjour ! Comment ça va aujourd'hui ?"},
    {"role": "assistant", "content": "Bonjour ! Je suis une IA, donc je n'ai pas de sentiments, mais je suis prêt à vous aider. Comment puis-je vous assister aujourd'hui ?"},
    {"role": "user", "content": "Quelle est la hauteur de la Tour Eiffel ?"},
    {"role": "assistant", "content": "La Tour Eiffel mesure environ 330 mètres de hauteur."},
    {"role": "user", "content": "Comment monter en haut ?"},
]

print(tokenizer.apply_chat_template(conversation, tokenize=False, add_generation_prompt=True))
```

You will get

```
<s><|system|>: Vous êtes Vigogne, un assistant IA créé par Zaion Lab. Vous suivez extrêmement bien les instructions. Aidez autant que vous le pouvez.
<|user|>: Bonjour ! Comment ça va aujourd'hui ?
<|assistant|>: Bonjour ! Je suis une IA, donc je n'ai pas de sentiments, mais je suis prêt à vous aider. Comment puis-je vous assister aujourd'hui ?</s>
<|user|>: Quelle est la hauteur de la Tour Eiffel ?
<|assistant|>: La Tour Eiffel mesure environ 330 mètres de hauteur.</s>
<|user|>: Comment monter en haut ?
<|assistant|>:
```

## Usage

### Inference using the quantized versions

The quantized versions of this model are generously provided by [TheBloke](https://huggingface.co/TheBloke)!

- AWQ for GPU inference: [TheBloke/Vigogne-2-7B-Chat-AWQ](https://huggingface.co/TheBloke/Vigogne-2-7B-Chat-AWQ)
- GTPQ for GPU inference: [TheBloke/Vigogne-2-7B-Chat-GPTQ](https://huggingface.co/TheBloke/Vigogne-2-7B-Chat-GPTQ)
- GGUF for CPU+GPU inference: [TheBloke/Vigogne-2-7B-Chat-GGUF](https://huggingface.co/TheBloke/Vigogne-2-7B-Chat-GGUF)

These versions facilitate testing and development with various popular frameworks, including [AutoAWQ](https://github.com/casper-hansen/AutoAWQ), [vLLM](https://github.com/vllm-project/vllm), [AutoGPTQ](https://github.com/PanQiWei/AutoGPTQ), [GPTQ-for-LLaMa](https://github.com/qwopqwop200/GPTQ-for-LLaMa), [llama.cpp](https://github.com/ggerganov/llama.cpp), [text-generation-webui](https://github.com/oobabooga/text-generation-webui), and more.

### Inference using the unquantized model with 🤗 Transformers

```python
from typing import Dict, List, Optional
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig, TextStreamer

model_name_or_path = "bofenghuang/vigogne-2-7b-chat"
revision = "v2.0"

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, revision=revision, padding_side="right", use_fast=False)
model = AutoModelForCausalLM.from_pretrained(model_name_or_path, revision=revision, torch_dtype=torch.float16, device_map="auto")

streamer = TextStreamer(tokenizer, timeout=10.0, skip_prompt=True, skip_special_tokens=True)


def chat(
    query: str,
    history: Optional[List[Dict]] = None,
    temperature: float = 0.7,
    top_p: float = 1.0,
    top_k: float = 0,
    repetition_penalty: float = 1.1,
    max_new_tokens: int = 1024,
    **kwargs,
):
    if history is None:
        history = []

    history.append({"role": "user", "content": query})

    input_ids = tokenizer.apply_chat_template(history, add_generation_prompt=True, return_tensors="pt").to(model.device)
    input_length = input_ids.shape[1]

    generated_outputs = model.generate(
        input_ids=input_ids,
        generation_config=GenerationConfig(
            temperature=temperature,
            do_sample=temperature > 0.0,
            top_p=top_p,
            top_k=top_k,
            repetition_penalty=repetition_penalty,
            max_new_tokens=max_new_tokens,
            pad_token_id=tokenizer.eos_token_id,
            **kwargs,
        ),
        streamer=streamer,
        return_dict_in_generate=True,
    )

    generated_tokens = generated_outputs.sequences[0, input_length:]
    generated_text = tokenizer.decode(generated_tokens, skip_special_tokens=True)

    history.append({"role": "assistant", "content": generated_text})

    return generated_text, history


# 1st round
response, history = chat("Un escargot parcourt 100 mètres en 5 heures. Quelle est sa vitesse ?", history=None)

# 2nd round
response, history = chat("Quand il peut dépasser le lapin ?", history=history)

# 3rd round
response, history = chat("Écris une histoire imaginative qui met en scène une compétition de course entre un escargot et un lapin.", history=history)
```

You can also use the Google Colab Notebook provided below.

<a href="https://colab.research.google.com/github/bofenghuang/vigogne/blob/main/notebooks/infer_chat.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

### Inference using the unquantized model with vLLM

Set up an OpenAI-compatible server with the following command:

```bash
# Install vLLM
# This may take 5-10 minutes.
# pip install vllm

# Start server for Vigogne-Chat models
python -m vllm.entrypoints.openai.api_server --model bofenghuang/vigogne-2-7b-chat

# List models
# curl http://localhost:8000/v1/models
```

Query the model using the openai python package.

```python
import openai

# Modify OpenAI's API key and API base to use vLLM's API server.
openai.api_key = "EMPTY"
openai.api_base = "http://localhost:8000/v1"

# First model
models = openai.Model.list()
model = models["data"][0]["id"]

# Chat completion API
chat_completion = openai.ChatCompletion.create(
    model=model,
    messages=[
        {"role": "user", "content": "Parle-moi de toi-même."},
    ],
    max_tokens=1024,
    temperature=0.7,
)
print("Chat completion results:", chat_completion)
```

## Limitations

Vigogne is still under development, and there are many limitations that have to be addressed. Please note that it is possible that the model generates harmful or biased content, incorrect information or generally unhelpful answers.
