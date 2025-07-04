
# 🧪 YamshadowExperiment28-7B

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/65dd0b848dd868f7ec95dcf0/3NLzELGy_ZF1G4nt_xvtq.jpeg)

**🎉 YamshadowExperiment28-7B is currently the best-performing 7B model on the Open LLM Leaderboard (08 Apr 24). Use it with caution, as it is likely a sign of overfitting the benchmarks.**

YamshadowExperiment28-7B is an automated merge created by [Maxime Labonne](https://huggingface.co/mlabonne) using the following configuration.
* [automerger/YamShadow-7B](https://huggingface.co/automerger/YamShadow-7B)
* [yam-peleg/Experiment28-7B](https://huggingface.co/yam-peleg/Experiment28-7B)

## 🔍 Applications

This model uses a context window of 8k. I recommend using it with the Alpaca chat template (works perfectly with LM Studio).

The model can sometimes break and output a lot of "INST". From my experience, its excellent results on the Open LLM Leaderboard are probably a sign of overfitting.

## ⚡ Quantized models

* **GGUF**: https://huggingface.co/automerger/YamshadowExperiment28-7B-GGUF

## 🏆 Evaluation

### Open LLM Leaderboard

YamshadowExperiment28-7B is currently the best-performing 7B model on the Open LLM Leaderboard (08 Apr 24).

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/ONmehD2GXYefb-O3zHbp5.png)

### EQ-bench

Thanks to [Samuel J. Paech](https://twitter.com/sam_paech), who kindly ran the evaluation.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/e6cg_7TD35JveTjx_KoTT.png)

### Nous

Evaluation performed using [LLM AutoEval](https://github.com/mlabonne/llm-autoeval). See the entire leaderboard [here](https://huggingface.co/spaces/mlabonne/Yet_Another_LLM_Leaderboard).

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/s4oKdK3FfaDsagXe7tEM2.png)

## 🌳 Model Family Tree

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/fEA4EdtSa_fssdvsUXPf1.png)

## 🧩 Configuration

```yaml
slices:
  - sources:
      - model: automerger/YamShadow-7B
        layer_range: [0, 32]
      - model: yam-peleg/Experiment28-7B
        layer_range: [0, 32]
merge_method: slerp
base_model: automerger/YamShadow-7B
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16
random_seed: 0
```

## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "automerger/YamshadowExperiment28-7B"
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