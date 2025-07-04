# `StableLM-Base-Alpha-7B-v2`

## Model Description

`StableLM-Base-Alpha-7B-v2` is a 7 billion parameter decoder-only language model pre-trained on diverse English datasets. This model is the successor to the first [`StableLM-Base-Alpha-7B`](https://huggingface.co/stabilityai/stablelm-base-alpha-7b) model, addressing previous shortcomings through the use of improved data sources and mixture ratios.

## Usage

Get started generating text with `StableLM-Base-Alpha-7B-v2` by using the following code snippet:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("stabilityai/stablelm-base-alpha-7b-v2")
model = AutoModelForCausalLM.from_pretrained(
  "stabilityai/stablelm-base-alpha-7b-v2",
  trust_remote_code=True,
  torch_dtype="auto",
)
model.cuda()
inputs = tokenizer("The weather is always wonderful", return_tensors="pt").to("cuda")
tokens = model.generate(
  **inputs,
  max_new_tokens=64,
  temperature=0.75,
  top_p=0.95,
  do_sample=True,
)
print(tokenizer.decode(tokens[0], skip_special_tokens=True))
```

## Model Details

* **Developed by**: [Stability AI](https://stability.ai/)
* **Model type**: `StableLM-Base-Alpha-v2` models are auto-regressive language models based on the transformer decoder architecture.
* **Language(s)**: English
* **Library**: [GPT-NeoX](https://github.com/EleutherAI/gpt-neox)
* **License**: Model checkpoints are licensed under the Creative Commons license ([CC BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/)). Under this license, you must give [credit](https://creativecommons.org/licenses/by/4.0/#) to Stability AI, provide a link to the license, and [indicate if changes were made](https://creativecommons.org/licenses/by/4.0/#). You may do so in any reasonable manner, but not in any way that suggests the Stability AI endorses you or your use.
* **Contact**: For questions and comments about the model, please email `lm@stability.ai`

### Model Architecture

| Parameters     | Hidden Size | Layers | Heads | Sequence Length |
|----------------|-------------|--------|-------|-----------------|
| 6,890,209,280  | 4096        | 32     | 32    | 4096            |

The model is a decoder-only transformer similar to the `StableLM-Base-Alpha` (v1) with the following configurations:

* **Activation**: SwiGLU ([Shazeer, 2020](https://arxiv.org/abs/2002.05202))
* **Decoder Layer**: Parallel Attention and MLP residuals with a single input LayerNorm ([Wang & Komatsuzaki, 2021](https://github.com/kingoflolz/mesh-transformer-jax/tree/master))
* **Position Embeddings**: Rotary Position Embeddings ([Su et al., 2021](https://arxiv.org/abs/2104.09864))
* **Bias**: LayerNorm bias terms only

## Training

`StableLM-Base-Alpha-7B-v2` is pre-trained using a multi-stage context length extension schedule following similar work ([Nijkamp et al. 2023](https://blog.salesforceairesearch.com/xgen/)); first pre-training at a context length of 2048 for 1 trillion tokens, then fine-tuning at a context length of 4096 for another 100B tokens.

### Training Dataset

The first pre-training stage relies on 1 trillion tokens sourced from a mix of the public Falcon RefinedWeb extract ([Penedo et al., 2023](https://huggingface.co/datasets/tiiuae/falcon-refinedweb)), RedPajama-Data ([Together Computer 2023](https://github.com/togethercomputer/RedPajama-Data), The Pile ([Gao et al., 2020](https://arxiv.org/abs/2101.00027)), and internal datasets with web text sampled at a rate of 71%.

In the second stage, we include the StarCoder ([Li et al., 2023](https://arxiv.org/abs/2305.06161)) dataset and down sample web text to 55% while increasing sampling proportions of naturally long text examples in the aforementioned sources.

### Training Procedure

The model is pre-trained on the dataset mixes mentioned above in mixed-precision (FP16), optimized with AdamW, and trained using the NeoX tokenizer with a vocabulary size of 50,257. We outline the complete hyperparameters choices in the project's [GitHub repository - config](https://github.com/Stability-AI/StableLM/blob/main/configs/stablelm-base-alpha-7b-v2.yaml).

### Training Infrastructure

* **Hardware**: `StableLM-Base-Alpha-7B-v2` was trained on the Stability AI cluster - occupying 384 NVIDIA A100 40GB GPUs across AWS P4d instances. Training took approximately 16.33 days to complete across both stages.

* **Software**: We use a fork of gpt-neox ([EleutherAI, 2021](https://github.com/EleutherAI/gpt-neox)) and train under 2D parallelism (Data and Tensor Parallel) with ZeRO-1 ([Rajbhandari et al., 2019](https://arxiv.org/abs/1910.02054v3)) and rely on flash-attention as well as rotary embedding kernels from FlashAttention-2 ([Dao et al., 2023](https://tridao.me/publications/flash2/flash2.pdf))

## Use and Limitations

### Intended Use

These models are intended to be used by all individuals as foundational models for application-specific fine-tuning without strict limitations on commercial use.

### Limitations and bias

The pre-training dataset may have contained offensive or inappropriate content even after applying data cleansing filters which can be reflected in the model-generated text. We recommend that users exercise caution when using these models in production systems. Do not use the models for any applications that may cause harm or distress to individuals or groups.

### How to cite

```bibtex
@misc{StableLMAlphaV2Models, 
      url={[https://huggingface.co/stabilityai/stablelm-base-alpha-7b-v2](https://huggingface.co/stabilityai/stablelm-base-alpha-7b-v2)},
      title={StableLM Alpha v2 Models},
      author={Tow, Jonathan}
}
```
