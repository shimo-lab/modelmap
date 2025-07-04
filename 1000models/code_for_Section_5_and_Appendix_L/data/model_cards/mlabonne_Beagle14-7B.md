
# Beagle14-7B

**Update 01/16/24: Check the DPO fine-tuned version of this model, [NeuralBeagle14-7B](https://huggingface.co/mlabonne/NeuralBeagle14-7B) (probably the best 7B model you can find)! 🎉**

Beagle14-7B is a merge of the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):
* [fblgit/UNA-TheBeagle-7b-v1](https://huggingface.co/fblgit/UNA-TheBeagle-7b-v1)
* [argilla/distilabeled-Marcoro14-7B-slerp](https://huggingface.co/argilla/distilabeled-Marcoro14-7B-slerp)

## 🏆 Evaluation

The evaluation was performed using [LLM AutoEval](https://github.com/mlabonne/llm-autoeval) on Nous suite.

|                          Model                           |AGIEval|GPT4All|TruthfulQA|Bigbench|Average|
|----------------------------------------------------------|------:|------:|---------:|-------:|------:|
|[**Beagle14-7B**](https://huggingface.co/mlabonne/Beagle14-7B)|  **44.38**|  **76.53**|     **69.44**|   **47.25**|   **59.4**|
|[OpenHermes-2.5-Mistral-7B](https://huggingface.co/teknium/OpenHermes-2.5-Mistral-7B)|  42.75|  72.99|     52.99|   40.94|  52.42|
|[NeuralHermes-2.5-Mistral-7B](https://huggingface.co/mlabonne/NeuralHermes-2.5-Mistral-7B)|  43.67|  73.24|     55.37|   41.76|  53.51|
|[Nous-Hermes-2-SOLAR-10.7B](https://huggingface.co/NousResearch/Nous-Hermes-2-SOLAR-10.7B)|  47.79|  74.69|     55.92|   44.84|  55.81|
|[Marcoro14-7B-slerp](https://huggingface.co/mlabonne/Marcoro14-7B-slerp)       |  44.66|  76.24|     64.15|   45.64|  57.67|
|[CatMarcoro14-7B-slerp](https://huggingface.co/occultml/CatMarcoro14-7B-slerp)|  45.21|  75.91|     63.81|   47.31|  58.06|

## 🧩 Configuration

```yaml
slices:
  - sources:
      - model: fblgit/UNA-TheBeagle-7b-v1
        layer_range: [0, 32]
      - model: argilla/distilabeled-Marcoro14-7B-slerp
        layer_range: [0, 32]
merge_method: slerp
base_model: fblgit/UNA-TheBeagle-7b-v1
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16
```

## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "mlabonne/Beagle14-7B"
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
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_mlabonne__Beagle14-7B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |74.76|
|AI2 Reasoning Challenge (25-Shot)|72.95|
|HellaSwag (10-Shot)              |87.95|
|MMLU (5-Shot)                    |64.70|
|TruthfulQA (0-shot)              |68.88|
|Winogrande (5-shot)              |82.64|
|GSM8k (5-shot)                   |71.42|

