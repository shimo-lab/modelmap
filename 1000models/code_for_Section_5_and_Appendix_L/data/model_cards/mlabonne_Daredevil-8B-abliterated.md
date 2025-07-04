
# Daredevil-8B-abliterated

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/gFEhcIDSKa3AWpkNfH91q.jpeg)

Abliterated version of [mlabonne/Daredevil-8B](https://huggingface.co/mlabonne/Daredevil-8B) using [failspy](https://huggingface.co/failspy)'s notebook.

It based on the technique described in the blog post "[Refusal in LLMs is mediated by a single direction](https://www.alignmentforum.org/posts/jGuXSZgv6qfdhMCuJ/refusal-in-llms-is-mediated-by-a-single-direction)".

Thanks to Andy Arditi, Oscar Balcells Obeso, Aaquib111, Wes Gurnee, Neel Nanda, and failspy.

## 🔎 Applications

This is an uncensored model. You can use it for any application that doesn't require alignment, like role-playing.

Tested on LM Studio using the "Llama 3" preset.

## ⚡ Quantization

* **GGUF**: https://huggingface.co/mlabonne/Daredevil-8B-abliterated-GGUF

## 🏆 Evaluation

### Open LLM Leaderboard

Daredevil-8B-abliterated is the second best-performing 8B model on the Open LLM Leaderboard in terms of MMLU score (27 May 24).

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/ekwRGgnjzEOyprT8sEBFt.png)

### Nous

Evaluation performed using [LLM AutoEval](https://github.com/mlabonne/llm-autoeval). See the entire leaderboard [here](https://huggingface.co/spaces/mlabonne/Yet_Another_LLM_Leaderboard).

| Model | Average | AGIEval | GPT4All | TruthfulQA | Bigbench |
|---|---:|---:|---:|---:|---:|
| [mlabonne/Daredevil-8B](https://huggingface.co/mlabonne/Daredevil-8B) [📄](https://gist.github.com/mlabonne/080f9c5f153ea57a7ab7d932cf896f21) | 55.87 | 44.13 | 73.52 | 59.05 | 46.77 |
| [**mlabonne/Daredevil-8B-abliterated**](https://huggingface.co/mlabonne/Daredevil-8B-abliterated) [📄](https://gist.github.com/mlabonne/32cdd8460804662c856bcb2a20acd49e) | **55.06** | **43.29** | **73.33** | **57.47** | **46.17** |
| [mlabonne/Llama-3-8B-Instruct-abliterated-dpomix](https://huggingface.co/mlabonne/Llama-3-8B-Instruct-abliterated-dpomix) [📄](https://gist.github.com/mlabonne/d711548df70e2c04771cc68ab33fe2b9) | 52.26 | 41.6 | 69.95 | 54.22 | 43.26 |
| [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) [📄](https://gist.github.com/mlabonne/8329284d86035e6019edb11eb0933628) | 51.34 | 41.22 | 69.86 | 51.65 | 42.64 |
| [failspy/Meta-Llama-3-8B-Instruct-abliterated-v3](https://huggingface.co/failspy/Meta-Llama-3-8B-Instruct-abliterated-v3) [📄](https://gist.github.com/mlabonne/f46cce0262443365e4cce2b6fa7507fc) | 51.21 | 40.23 | 69.5 | 52.44 | 42.69 |
| [mlabonne/OrpoLlama-3-8B](https://huggingface.co/mlabonne/OrpoLlama-3-8B) [📄](https://gist.github.com/mlabonne/22896a1ae164859931cc8f4858c97f6f) | 48.63 | 34.17 | 70.59 | 52.39 | 37.36 |
| [meta-llama/Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B) [📄](https://gist.github.com/mlabonne/616b6245137a9cfc4ea80e4c6e55d847) | 45.42 | 31.1 | 69.95 | 43.91 | 36.7 |

## 🌳 Model family tree

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/ekwRGgnjzEOyprT8sEBFt.png)

## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "mlabonne/Daredevil-8B-abliterated"
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