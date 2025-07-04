# `StableLM-3B-4E1T`

## Model Description

`StableLM-3B-4E1T` is a 3 billion parameter decoder-only language model pre-trained on 1 trillion tokens of diverse English and code datasets for 4 epochs.

## Usage

Get started generating text with `StableLM-3B-4E1T` by using the following code snippet:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("stabilityai/stablelm-3b-4e1t")
model = AutoModelForCausalLM.from_pretrained(
  "stabilityai/stablelm-3b-4e1t",
  torch_dtype="auto",
)
model.cuda()
inputs = tokenizer("The weather is always wonderful", return_tensors="pt").to(model.device)
tokens = model.generate(
  **inputs,
  max_new_tokens=64,
  temperature=0.75,
  top_p=0.95,
  do_sample=True,
)
print(tokenizer.decode(tokens[0], skip_special_tokens=True))
```

### Run with Flash Attention 2 ⚡️

<details>
<summary> Click to expand </summary>

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("stabilityai/stablelm-3b-4e1t")
model = AutoModelForCausalLM.from_pretrained(
  "stabilityai/stablelm-3b-4e1t",
  torch_dtype="auto",
  attn_implementation="flash_attention_2",
)
model.cuda()
inputs = tokenizer("The weather is always wonderful", return_tensors="pt").to(model.device)
tokens = model.generate(
  **inputs,
  max_new_tokens=64,
  temperature=0.75,
  top_p=0.95,
  do_sample=True,
)
print(tokenizer.decode(tokens[0], skip_special_tokens=True))
```

</details>


## Model Details

* **Developed by**: [Stability AI](https://stability.ai/)
* **Model type**: `StableLM-3B-4E1T` models are auto-regressive language models based on the transformer decoder architecture.
* **Language(s)**: English
* **Library**: [GPT-NeoX](https://github.com/EleutherAI/gpt-neox)
* **License**: Model checkpoints are licensed under the Creative Commons license ([CC BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/)). Under this license, you must give [credit](https://creativecommons.org/licenses/by/4.0/#) to Stability AI, provide a link to the license, and [indicate if changes were made](https://creativecommons.org/licenses/by/4.0/#). You may do so in any reasonable manner, but not in any way that suggests the Stability AI endorses you or your use.
* **Contact**: For questions and comments about the model, please email `lm@stability.ai`

### Model Architecture

The model is a decoder-only transformer similar to the LLaMA ([Touvron et al., 2023](https://arxiv.org/abs/2307.09288)) architecture with the following modifications:

| Parameters     | Hidden Size | Layers | Heads | Sequence Length |
|----------------|-------------|--------|-------|-----------------|
| 2,795,443,200  | 2560        | 32     | 32    | 4096            |

* **Position Embeddings**: Rotary Position Embeddings ([Su et al., 2021](https://arxiv.org/abs/2104.09864)) applied to the first 25% of head embedding dimensions for improved throughput following [Black et al. (2022)](https://arxiv.org/pdf/2204.06745.pdf).
* **Normalization**: LayerNorm ([Ba et al., 2016](https://arxiv.org/abs/1607.06450)) with learned bias terms as opposed to RMSNorm ([Zhang & Sennrich, 2019](https://arxiv.org/abs/1910.07467)).
* **Tokenizer**: GPT-NeoX ([Black et al., 2022](https://arxiv.org/abs/2204.06745)).

## Training

For complete dataset and training details, please see the [StableLM-3B-4E1T Technical Report](https://stability.wandb.io/stability-llm/stable-lm/reports/StableLM-3B-4E1T--VmlldzoyMjU4?accessToken=u3zujipenkx5g7rtcj9qojjgxpconyjktjkli2po09nffrffdhhchq045vp0wyfo).

### Training Dataset

The dataset is comprised of a filtered mixture of open-source large-scale datasets available on the [HuggingFace Hub](https://huggingface.co/datasets): Falcon RefinedWeb extract ([Penedo et al., 2023](https://huggingface.co/datasets/tiiuae/falcon-refinedweb)), RedPajama-Data ([Together Computer., 2023](https://github.com/togethercomputer/RedPajama-Data)) and The Pile ([Gao et al., 2020](https://arxiv.org/abs/2101.00027)) both without the *Books3* subset, and StarCoder ([Li et al., 2023](https://arxiv.org/abs/2305.06161)).

* Given the large amount of web data, we recommend fine-tuning the base StableLM-3B-4E1T for your downstream tasks.

### Training Procedure

The model is pre-trained on the aforementioned datasets in `bfloat16` precision, optimized with AdamW, and trained using the NeoX tokenizer with a vocabulary size of 50,257. We outline the complete hyperparameters choices in the project's [GitHub repository - config](https://github.com/Stability-AI/StableLM/blob/main/configs/stablelm-3b-4e1t.yml).

### Training Infrastructure

* **Hardware**: `StableLM-3B-4E1T` was trained on the Stability AI cluster across 256 NVIDIA A100 40GB GPUs (AWS P4d instances). Training began on August 23, 2023, and took approximately 30 days to complete.

* **Software**: We use a fork of `gpt-neox` ([EleutherAI, 2021](https://github.com/EleutherAI/gpt-neox)), train under 2D parallelism (Data and Tensor Parallel) with ZeRO-1 ([Rajbhandari et al., 2019](https://arxiv.org/abs/1910.02054v3)), and rely on flash-attention as well as SwiGLU and Rotary Embedding kernels from FlashAttention-2 ([Dao et al., 2023](https://tridao.me/publications/flash2/flash2.pdf))

## Use and Limitations

### Intended Use

The model is intended to be used as a foundational base model for application-specific fine-tuning. Developers must evaluate and fine-tune the model for safe performance in downstream applications.

### Limitations and Bias
​
As a base model, this model may exhibit unreliable, unsafe, or other undesirable behaviors that must be corrected through evaluation and fine-tuning prior to deployment. The pre-training dataset may have contained offensive or inappropriate content, even after applying data cleansing filters, which can be reflected in the model-generated text. We recommend that users exercise caution when using these models in production systems. Do not use the models if they are unsuitable for your application, or for any applications that may cause deliberate or unintentional harm to others.

## How to Cite

```bibtex
@misc{StableLM-3B-4E1T,
      url={[https://huggingface.co/stabilityai/stablelm-3b-4e1t](https://huggingface.co/stabilityai/stablelm-3b-4e1t)},
      title={StableLM 3B 4E1T},
      author={Tow, Jonathan and Bellagente, Marco and Mahan, Dakota and Riquelme, Carlos}
}
```

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_stabilityai__stablelm-3b-4e1t)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |46.58|
|AI2 Reasoning Challenge (25-Shot)|46.59|
|HellaSwag (10-Shot)              |75.94|
|MMLU (5-Shot)                    |45.23|
|TruthfulQA (0-shot)              |37.20|
|Winogrande (5-shot)              |71.19|
|GSM8k (5-shot)                   | 3.34|

