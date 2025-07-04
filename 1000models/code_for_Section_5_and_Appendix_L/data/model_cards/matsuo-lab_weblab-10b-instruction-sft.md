
# weblab-10b-instruction-sft

# Overview
This repository provides a Japanese-centric multilingual GPT-NeoX model of 10 billion parameters.

* **Library**
    
    The model was trained using code based on [EleutherAI/gpt-neox](https://github.com/EleutherAI/gpt-neox).

* **Model architecture**

    A 36-layer, 4864-hidden-size transformer-based language model.

* **Pre-training**

    The model was trained on around **600B** tokens from a mixture of the following corpora.

    - [Japanese C4](https://huggingface.co/datasets/mc4)
    - [The Pile](https://huggingface.co/datasets/EleutherAI/pile)

* **Instruction-supervised-finetuning**

    The model was finetuned on a subset records from a mixture of the following dataset. Training epoch: 1.

    - [Alpaca (English)](https://github.com/gururise/AlpacaDataCleaned/blob/main/alpaca_data_cleaned.json)
    - [Alpaca (Japanese translation)](https://github.com/shi3z/alpaca_ja/blob/main/alpaca_cleaned_ja.json)
    - [Flan 2021 (English)](https://huggingface.co/datasets/conceptofmind/flan2021_submix_original)
    - [Flan CoT (English)](https://huggingface.co/datasets/conceptofmind/cot_submix_original)
    - [Flan Dialog (English)](https://huggingface.co/datasets/conceptofmind/dialog_submix_original)

* **Model Series**

    | Variant | Link |
    | :-- | :--|
    | weblab-10b-instruction-sft | https://huggingface.co/matsuo-lab/weblab-10b-instruction-sft |
    | weblab-10b | https://huggingface.co/matsuo-lab/weblab-10b |

* **Authors**
    
    Takeshi Kojima

---

# Benchmarking

* **Japanese benchmark : JGLUE 8-task (2023-08-27)**

    - *We used [Stability-AI/lm-evaluation-harness](https://github.com/Stability-AI/lm-evaluation-harness/tree/2f1583c0735eacdfdfa5b7d656074b69577b6774) library for evaluation.*
    - *The 8-task average accuracy is based on results of JCommonsenseQA-1.1, JNLI-1.1, MARC-ja-1.1, JSQuAD-1.1, jaqket_v2-0.2, xlsum_ja-1.0, xwinograd_ja, and mgsm-1.0.*
    - *model loading is performed with float16, and evaluation is performed with template version 0.3 using the few-shot in-context learning.*
    - *The number of few-shots is 3,3,3,2,1,1,0,5.*
    - *special_tokens_map.json is modified to avoid errors during the evaluation of the second half benchmarks. As a result, the results of the first half benchmarks became slightly different.*
   
    model | average | jcommonsenseqa | jnli | marc_ja | jsquad | jaqket_v2 | xlsum_ja | xwinograd_ja | mgsm
    | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
    weblab-10b-instruction-sft | 59.11 | 74.62 | 66.56 | 95.49 | 78.34 | 63.32 | 20.57 | 71.95 | 2
    weblab-10b | 50.74 | 66.58 | 53.74 | 82.07 | 62.94 | 56.19 | 10.03 | 71.95 | 2.4

* **Japanese benchmark : JGLUE 4-task (2023-08-18)**

    - *We used [Stability-AI/lm-evaluation-harness](https://github.com/Stability-AI/lm-evaluation-harness/tree/2f1583c0735eacdfdfa5b7d656074b69577b6774) library for evaluation.*
    - *The 4-task average accuracy is based on results of JCommonsenseQA-1.1, JNLI-1.1, MARC-ja-1.1, and JSQuAD-1.1.*
    - *model loading is performed with float16, and evaluation is performed with template version 0.3 using the few-shot in-context learning.*
    - *The number of few-shots is 3,3,3,2.*
   
    | Model | Average | JCommonsenseQA | JNLI | MARC-ja | JSQuAD |
    | :-- | :-- | :-- | :-- | :-- | :-- |
    | weblab-10b-instruction-sft | 78.78 | 74.35 | 65.65 | 96.06 | 79.04 |
    | weblab-10b | 66.38 | 65.86 | 54.19 | 84.49 | 60.98 |

---

# How to use the model

~~~~python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("matsuo-lab/weblab-10b-instruction-sft")
model = AutoModelForCausalLM.from_pretrained("matsuo-lab/weblab-10b-instruction-sft", torch_dtype=torch.float16)

if torch.cuda.is_available():
    model = model.to("cuda")

text = "大規模言語モデルについて説明してください。"
text = f'以下は、タスクを説明する指示です。要求を適切に満たす応答を書きなさい。\n\n### 指示:\n{text}\n\n### 応答:'
token_ids = tokenizer.encode(text, add_special_tokens=False, return_tensors="pt")

with torch.no_grad():
    output_ids = model.generate(
        token_ids.to(model.device),
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7,
        top_p=0.95
    )

output = tokenizer.decode(output_ids.tolist()[0])
print(output)

~~~~
---

# Licenese
[cc-by-nc-4.0](https://creativecommons.org/licenses/by-nc/4.0/)