Merge:
```
slices:
  - sources:
      - model: viethq188/LeoScorpius-7B-Chat-DPO
        layer_range: [0, 32]
      - model: GreenNode/GreenNodeLM-7B-v1olet
        layer_range: [0, 32]
merge_method: slerp
base_model: viethq188/LeoScorpius-7B-Chat-DPO
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5 # fallback for rest of tensors
dtype: float16
```


![image/png](https://cdn-uploads.huggingface.co/production/uploads/63a259d0f30c46422789d38d/tmdM1fjNAmzV125zWd3_J.png)

# Go Bruins V2.1 - A Fine-tuned Language Model

## Updates 

## Overview

**Go Bruins-V2** is a language model fine-tuned on the rwitz/go-bruins architecture. It's designed to push the boundaries of NLP applications, offering unparalleled performance in generating human-like text.

## Model Details

- **Developer:** Ryan Witzman
- **Base Model:** [rwitz/go-bruins](https://huggingface.co/rwitz/go-bruins)
- **Fine-tuning Method:** Direct Preference Optimization (DPO)
- **Training Steps:** 642
- **Language:** English
- **License:** MIT

## Capabilities

Go Bruins excels in a variety of NLP tasks, including but not limited to:
- Text generation
- Language understanding
- Sentiment analysis

## Usage

**Warning:** This model may output NSFW or illegal content. Use with caution and at your own risk.

### For Direct Use:

```python
from transformers import pipeline

model_name = "rwitz/go-bruins-v2"
inference_pipeline = pipeline('text-generation', model=model_name)

input_text = "Your input text goes here"
output = inference_pipeline(input_text)

print(output)
```


### Not Recommended For:

- Illegal activities
- Harassment
- Professional advice or crisis situations

## Training and Evaluation

Trained on a dataset from [athirdpath/DPO_Pairs-Roleplay-Alpaca-NSFW](https://huggingface.co/datasets/athirdpath/DPO_Pairs-Roleplay-Alpaca-NSFW), Go Bruins V2 has shown promising improvements over its predecessor, Go Bruins.

# Evaluations

| Metric        | Average | Arc Challenge | Hella Swag | MMLU | Truthful Q&A | Winogrande | GSM8k |
|---------------|---------|---------------|------------|------|--------------|------------|-------|
| **Score**     | 72.07    | 69.8        | 87.05|  64.75      | 59.7     | 81.45  | 69.67 |

Note: The original MMLU evaluation has been corrected to include 5-shot data rather than 1-shot data.
## Contact

For any inquiries or feedback, reach out to Ryan Witzman on Discord: `rwitz_`.

---
## Citations
```
@misc{unacybertron7b,
  title={Cybertron: Uniform Neural Alignment}, 
  author={Xavier Murias},
  year={2023},
  publisher = {HuggingFace},
  journal = {HuggingFace repository},
  howpublished = {\url{https://huggingface.co/fblgit/una-cybertron-7b-v2-bf16}},
}
```

*This model card was created with care by Ryan Witzman.*
rewrite this model card for new version called go-bruins-v2 that is finetuned on dpo on the original go-bruins model on athirdpath/DPO_Pairs-Roleplay-Alpaca-NSFW