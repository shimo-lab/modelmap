
![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/LxRUvkSATmy-UDKN54Q3H.jpeg)

# 👑 NeuralMonarch-7B

NeuralMonarch-7B is a DPO fine-tuned of [mlabonne/Monarch-7B](https://huggingface.co/mlabonne/Monarch-7B/) using the [jondurbin/truthy-dpo-v0.1](https://huggingface.co/datasets/jondurbin/truthy-dpo-v0.1) and [argilla/distilabel-intel-orca-dpo-pairs](https://huggingface.co/datasets/argilla/distilabel-intel-orca-dpo-pairs) preference datasets.

It is based on a merge of the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):
* [mlabonne/OmniTruthyBeagle-7B-v0](https://huggingface.co/mlabonne/OmniTruthyBeagle-7B-v0)
* [mlabonne/NeuBeagle-7B](https://huggingface.co/mlabonne/NeuBeagle-7B)
* [mlabonne/NeuralOmniBeagle-7B](https://huggingface.co/mlabonne/NeuralOmniBeagle-7B)

Special thanks to [Jon Durbin](https://huggingface.co/jondurbin), [Intel](https://huggingface.co/Intel), and [Argilla](https://huggingface.co/argilla) for the preference datasets.

**Try the demo**: https://huggingface.co/spaces/mlabonne/NeuralMonarch-7B-GGUF-Chat

## 🔍 Applications

This model uses a context window of 8k. I recommend using it with the Mistral Instruct chat template (works perfectly with LM Studio).

Compared to other 7B models, it performs well in instruction following and reasoning tasks. For a chat/RP model with strong reasoning abilities, check out [mlabonne/AlphaMonarch-7B](https://huggingface.co/mlabonne/AlphaMonarch-7B).

## ⚡ Quantized models

* **GGUF**: https://huggingface.co/mlabonne/NeuralMonarch-7B-GGUF

## 🏆 Evaluation

### Nous

NeuralMonarch-7B is one of the best-performing 7B models on Nous' benchmark suite (evaluation performed using [LLM AutoEval](https://github.com/mlabonne/llm-autoeval)). See the entire leaderboard [here](https://huggingface.co/spaces/mlabonne/Yet_Another_LLM_Leaderboard).

| Model | Average | AGIEval | GPT4All | TruthfulQA | Bigbench |
|---|---:|---:|---:|---:|---:|
| [**NeuralMonarch-7B**](https://huggingface.co/mlabonne/NeuralMonarch-7B) [📄](https://gist.github.com/mlabonne/64050c96c6aa261a8f5b403190c8dee4) | **62.73** | **45.31** | **76.99** | **78.35** | **50.28** |
| [AlphaMonarch-7B](https://huggingface.co/mlabonne/AlphaMonarch-7B) [📄](https://gist.github.com/mlabonne/1d33c86824b3a11d2308e36db1ba41c1) | 62.74 | 45.37 | 77.01 | 78.39 | 50.2 |
| [Monarch-7B](https://huggingface.co/mlabonne/Monarch-7B) [📄](https://gist.github.com/mlabonne/0b8d057c5ece41e0290580a108c7a093) | 62.68 | 45.48 | 77.07 | 78.04 | 50.14 |
| [teknium/OpenHermes-2.5-Mistral-7B](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B) [📄](https://gist.github.com/mlabonne/88b21dd9698ffed75d6163ebdc2f6cc8) | 52.42 | 42.75 | 72.99 | 52.99 | 40.94 |
| [mlabonne/NeuralHermes-2.5-Mistral-7B](https://huggingface.co/mlabonne/NeuralHermes-2.5-Mistral-7B) [📄](https://gist.github.com/mlabonne/14687f1eb3425b166db511f31f8e66f6) | 53.51 | 43.67 | 73.24 | 55.37 | 41.76 |
| [mlabonne/NeuralBeagle14-7B](https://huggingface.co/mlabonne/NeuralBeagle14-7B) [📄](https://gist.github.com/mlabonne/ad0c665bbe581c8420136c3b52b3c15c) | 60.25 | 46.06 | 76.77 | 70.32 | 47.86 |
| [mlabonne/NeuralOmniBeagle-7B](https://huggingface.co/mlabonne/NeuralOmniBeagle-7B) [📄](https://gist.github.com/mlabonne/0e49d591787185fa5ae92ca5d9d4a1fd) | 62.3 | 45.85 | 77.26 | 76.06 | 50.03 |
| [eren23/dpo-binarized-NeuralTrix-7B](https://huggingface.co/eren23/dpo-binarized-NeuralTrix-7B) [📄](https://gist.github.com/CultriX-Github/dbdde67ead233df0c7c56f1b091f728c) | 62.5 | 44.57 | 76.34 | 79.81 | 49.27 |
| [CultriX/NeuralTrix-7B-dpo](https://huggingface.co/CultriX/NeuralTrix-7B-dpo) [📄](https://gist.github.com/CultriX-Github/df0502599867d4043b45d9dafb5976e8) | 62.5 | 44.61 | 76.33 | 79.8 | 49.24 |

### EQ-bench

NeuralMonarch-7B is also outperforming 70B and 120B parameter models on [EQ-bench](https://eqbench.com/) by [Samuel J. Paech](https://twitter.com/sam_paech), who kindly ran the evaluations.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/dnCFxieqLiAC3Ll6CfdZW.png)

### Open LLM Leaderboard

NeuralMonarch-7B is one of the best-performing 7B models on the Open LLM Leaderboard.

### MT-Bench

```
########## First turn ##########
                                    score
model                       turn         
gpt-4                       1     8.95625
OmniBeagle-7B               1     8.31250
AlphaMonarch-7B             1     8.23750
claude-v1                   1     8.15000
NeuralMonarch-7B            1     8.09375
gpt-3.5-turbo               1     8.07500
claude-instant-v1           1     7.80000

########## Second turn ##########
                                     score
model                       turn          
gpt-4                       2     9.025000
claude-instant-v1           2     8.012658
OmniBeagle-7B               2     7.837500
gpt-3.5-turbo               2     7.812500
claude-v1                   2     7.650000
AlphaMonarch-7B             2     7.618750
NeuralMonarch-7B            2     7.375000

########## Average ##########
                                score
model                                
gpt-4                        8.990625
OmniBeagle-7B                8.075000
gpt-3.5-turbo                7.943750
AlphaMonarch-7B              7.928125
claude-instant-v1            7.905660
claude-v1                    7.900000
NeuralMonarch-7B             7.734375
NeuralBeagle14-7B            7.628125
```

## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "mlabonne/NeuralMonarch-7B"
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