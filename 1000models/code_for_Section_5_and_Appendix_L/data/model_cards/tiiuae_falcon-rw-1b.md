
# Falcon-RW-1B

**Falcon-RW-1B is a 1B parameters causal decoder-only model built by [TII](https://www.tii.ae) and trained on 350B tokens of [RefinedWeb](https://huggingface.co/datasets/tiiuae/falcon-refinedweb). It is made available under the Apache 2.0 license.**

See the 📓 [paper on arXiv](https://arxiv.org/abs/2306.01116) for more details.

RefinedWeb is a high-quality web dataset built by leveraging stringent filtering and large-scale deduplication. Falcon-RW-1B, trained on RefinedWeb only, matches or outperforms comparable models trained on curated data.

⚠️ Falcon is now available as a core model in the `transformers` library! To use the in-library version, please install the latest version of `transformers` with `pip install git+https://github.com/huggingface/transformers.git`, then simply remove the `trust_remote_code=True` argument from `from_pretrained()`.

⚠️ This model is intended for use as a **research artifact**, to study the influence of training on web data alone. **If you are interested in state-of-the-art models, we recommend using Falcon-[7B](https://huggingface.co/tiiuae/falcon-7b)/[40B](https://huggingface.co/tiiuae/falcon-40b), both trained on >1,000 billion tokens.**

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

model = "tiiuae/falcon-rw-1b"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
sequences = pipeline(
   "Girafatron is obsessed with giraffes, the most glorious animal on the face of this Earth. Giraftron believes all other animals are irrelevant when compared to the glorious majesty of the giraffe.\nDaniel: Hello, Girafatron!\nGirafatron:",
    max_length=200,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")

```

💥 **Falcon LLMs require PyTorch 2.0 for use with `transformers`!**



# Model Card for Falcon-RW-1B

## Model Details

### Model Description

- **Developed by:** [https://www.tii.ae](https://www.tii.ae);
- **Model type:** Causal decoder-only;
- **Language(s) (NLP):** English;
- **License:** Apache 2.0.

### Model Source

- **Paper:** [https://arxiv.org/abs/2306.01116](https://arxiv.org/abs/2306.01116).

## Uses

### Direct Use

Research on large language models, specifically the influence of adequately filtered and deduplicated web data on the properties of large language models (fairness, safety, limitations, capabilities, etc.).

### Out-of-Scope Use

Production use without adequate assessment of risks and mitigation; any use cases which may be considered irresponsible or harmful. 

Broadly speaking, we would recommend Falcon-[7B](https://huggingface.co/tiiuae/falcon-7b)/[40B](https://huggingface.co/tiiuae/falcon-40b) for any use not directly related to research on web data pipelines.

## Bias, Risks, and Limitations

Falcon-RW-1B is trained on English data only, and will not generalize appropriately to other languages. Furthermore, as it is trained on a large-scale corpora representative of the web, it will carry the stereotypes and biases commonly encountered online.

### Recommendations

We recommend users of Falcon-RW-1B to consider finetuning it for the specific set of tasks of interest, and for guardrails and appropriate precautions to be taken for any production use.

## How to Get Started with the Model


```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

model = "tiiuae/falcon-rw-1b"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
sequences = pipeline(
   "Girafatron is obsessed with giraffes, the most glorious animal on the face of this Earth. Giraftron believes all other animals are irrelevant when compared to the glorious majesty of the giraffe.\nDaniel: Hello, Girafatron!\nGirafatron:",
    max_length=200,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")

```

## Training Details

### Training Data

Falcon-RW-1B was trained on 350B tokens of [RefinedWeb](https://huggingface.co/datasets/tiiuae/falcon-refinedweb), a high-quality filtered and deduplicated web dataset. The data was tokenized with the GPT-2 tokenizer.

### Training Procedure 

Falcon-RW-1B was trained on 32 A100 40GB GPUs, using only data parallelism with ZeRO.

#### Training Hyperparameters

Hyperparameters were adapted from the GPT-3 paper ([Brown et al., 2020](https://arxiv.org/abs/2005.14165)).

| **Hyperparameter** | **Value**  | **Comment**                               |
|--------------------|------------|-------------------------------------------|
| Precision          | `bfloat16` |                                           |
| Optimizer          | AdamW      |                                           |
| Learning rate      | 2e-4       | 500M tokens warm-up, cosine decay to 2e-5 |
| Weight decay       | 1e-1       |                                           |
| Batch size         | 512        | 4B tokens ramp-up                         |


#### Speeds, Sizes, Times

Training happened in early December 2022 and took about six days. 


## Evaluation

See the 📓 [paper on arXiv](https://arxiv.org/abs/2306.01116) for in-depth evaluation.


## Technical Specifications 

### Model Architecture and Objective

Falcon-RW-1B is a causal decoder-only model trained on a causal language modeling task (i.e., predict the next token).

The architecture is adapted from the GPT-3 paper ([Brown et al., 2020](https://arxiv.org/abs/2005.14165)), but uses ALiBi ([Ofir et al., 2021](https://arxiv.org/abs/2108.12409)) and FlashAttention ([Dao et al., 2022](https://arxiv.org/abs/2205.14135)).

| **Hyperparameter** | **Value** | **Comment**                            |
|--------------------|-----------|----------------------------------------|
| Layers             | 24        |                                        |
| `d_model`          | 2048      |                                        |
| `head_dim`         | 64        | Reduced to optimise for FlashAttention |
| Vocabulary         | 50304     |                                        |
| Sequence length    | 2048      |                                        |

### Compute Infrastructure

#### Hardware

Falcon-RW-1B was trained on AWS SageMaker, on 32 A100 40GB GPUs in P4d instances. 

#### Software

Falcon-RW-1B was trained a custom distributed training codebase, Gigatron. It uses a 3D parallelism approach combined with ZeRO and high-performance Triton kernels (FlashAttention, etc.)


## Citation

```
@article{refinedweb,
  title={The {R}efined{W}eb dataset for {F}alcon {LLM}: outperforming curated corpora with web data, and web data only},
  author={Guilherme Penedo and Quentin Malartic and Daniel Hesslow and Ruxandra Cojocaru and Alessandro Cappelli and Hamza Alobeidli and Baptiste Pannier and Ebtesam Almazrouei and Julien Launay},
  journal={arXiv preprint arXiv:2306.01116},
  eprint={2306.01116},
  eprinttype = {arXiv},
  url={https://arxiv.org/abs/2306.01116},
  year={2023}
}
```


## Contact
falconllm@tii.ae
