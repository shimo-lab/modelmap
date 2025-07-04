
# ✨ Falcon-7B-Instruct

**Falcon-7B-Instruct is a 7B parameters causal decoder-only model built by [TII](https://www.tii.ae) based on [Falcon-7B](https://huggingface.co/tiiuae/falcon-7b) and finetuned on a mixture of chat/instruct datasets. It is made available under the Apache 2.0 license.**

*Paper coming soon 😊.*

🤗 To get started with Falcon (inference, finetuning, quantization, etc.), we recommend reading [this great blogpost fron HF](https://huggingface.co/blog/falcon)!

## Why use Falcon-7B-Instruct?

* **You are looking for a ready-to-use chat/instruct model based on [Falcon-7B](https://huggingface.co/tiiuae/falcon-7b).**
* **Falcon-7B is a strong base model, outperforming comparable open-source models** (e.g., [MPT-7B](https://huggingface.co/mosaicml/mpt-7b), [StableLM](https://github.com/Stability-AI/StableLM), [RedPajama](https://huggingface.co/togethercomputer/RedPajama-INCITE-Base-7B-v0.1) etc.), thanks to being trained on 1,500B tokens of [RefinedWeb](https://huggingface.co/datasets/tiiuae/falcon-refinedweb) enhanced with curated corpora. See the [OpenLLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard).
* **It features an architecture optimized for inference**, with FlashAttention ([Dao et al., 2022](https://arxiv.org/abs/2205.14135)) and multiquery ([Shazeer et al., 2019](https://arxiv.org/abs/1911.02150)). 

💬 **This is an instruct model, which may not be ideal for further finetuning.** If you are interested in building your own instruct/chat model, we recommend starting from [Falcon-7B](https://huggingface.co/tiiuae/falcon-7b). 

🔥 **Looking for an even more powerful model?** [Falcon-40B-Instruct](https://huggingface.co/tiiuae/falcon-40b-instruct) is Falcon-7B-Instruct's big brother!

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

model = "tiiuae/falcon-7b-instruct"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
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

For fast inference with Falcon, check-out [Text Generation Inference](https://github.com/huggingface/text-generation-inference)! Read more in this [blogpost]((https://huggingface.co/blog/falcon). 

You will need **at least 16GB of memory** to swiftly run inference with Falcon-7B-Instruct.


# Model Card for Falcon-7B-Instruct

## Model Details

### Model Description

- **Developed by:** [https://www.tii.ae](https://www.tii.ae);
- **Model type:** Causal decoder-only;
- **Language(s) (NLP):** English and French;
- **License:** Apache 2.0;
- **Finetuned from model:** [Falcon-7B](https://huggingface.co/tiiuae/falcon-7b).

### Model Source

- **Paper:** *coming soon*.

## Uses

### Direct Use

Falcon-7B-Instruct has been finetuned on a mixture of instruct and chat datasets.

### Out-of-Scope Use

Production use without adequate assessment of risks and mitigation; any use cases which may be considered irresponsible or harmful. 

## Bias, Risks, and Limitations

Falcon-7B-Instruct is mostly trained on English data, and will not generalize appropriately to other languages. Furthermore, as it is trained on a large-scale corpora representative of the web, it will carry the stereotypes and biases commonly encountered online.

### Recommendations

We recommend users of Falcon-7B-Instruct to develop guardrails and to take appropriate precautions for any production use.

## How to Get Started with the Model


```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch

model = "tiiuae/falcon-7b-instruct"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
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

Falcon-7B-Instruct was finetuned on a 250M tokens mixture of instruct/chat datasets.

| **Data source**    | **Fraction** | **Tokens** | **Description**                       |
|--------------------|--------------|------------|-----------------------------------|
| [Bai ze](https://github.com/project-baize/baize-chatbot) | 65%          | 164M     | chat                 |
| [GPT4All](https://github.com/nomic-ai/gpt4all)              | 25%           | 62M       | instruct                                  |
| [GPTeacher](https://github.com/teknium1/GPTeacher)      | 5%           | 11M        | instruct |
| [RefinedWeb-English](https://huggingface.co/datasets/tiiuae/falcon-refinedweb) | 5%          | 13M     | massive web crawl                 |


The data was tokenized with the Falcon-[7B](https://huggingface.co/tiiuae/falcon-7b)/[40B](https://huggingface.co/tiiuae/falcon-40b) tokenizer.


## Evaluation

*Paper coming soon.*

See the [OpenLLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) for early results.

Note that this model variant is not optimized for NLP benchmarks. 


## Technical Specifications 

For more information about pretraining, see [Falcon-7B](https://huggingface.co/tiiuae/falcon-7b).

### Model Architecture and Objective

Falcon-7B is a causal decoder-only model trained on a causal language modeling task (i.e., predict the next token).

The architecture is broadly adapted from the GPT-3 paper ([Brown et al., 2020](https://arxiv.org/abs/2005.14165)), with the following differences:

* **Positionnal embeddings:** rotary ([Su et al., 2021](https://arxiv.org/abs/2104.09864));
* **Attention:** multiquery ([Shazeer et al., 2019](https://arxiv.org/abs/1911.02150)) and FlashAttention ([Dao et al., 2022](https://arxiv.org/abs/2205.14135));
* **Decoder-block:** parallel attention/MLP with a single layer norm.

| **Hyperparameter** | **Value** | **Comment**                            |
|--------------------|-----------|----------------------------------------|
| Layers             | 32        |                                        |
| `d_model`          | 4544      | Increased to compensate for multiquery                                       |
| `head_dim`         | 64        | Reduced to optimise for FlashAttention |
| Vocabulary         | 65024     |                                        |
| Sequence length    | 2048      |                                        |

### Compute Infrastructure

#### Hardware

Falcon-7B-Instruct was trained on AWS SageMaker, on 32 A100 40GB GPUs in P4d instances. 

#### Software

Falcon-7B-Instruct was trained a custom distributed training codebase, Gigatron. It uses a 3D parallelism approach combined with ZeRO and high-performance Triton kernels (FlashAttention, etc.)


## Citation

*Paper coming soon* 😊. In the meanwhile, you can use the following information to cite: 
```
@article{falcon40b,
  title={{Falcon-40B}: an open large language model with state-of-the-art performance},
  author={Almazrouei, Ebtesam and Alobeidli, Hamza and Alshamsi, Abdulaziz and Cappelli, Alessandro and Cojocaru, Ruxandra and Debbah, Merouane and Goffinet, Etienne and Heslow, Daniel and Launay, Julien and Malartic, Quentin and Noune, Badreddine and Pannier, Baptiste and Penedo, Guilherme},
  year={2023}
}
```

To learn more about the pretraining dataset, see the 📓 [RefinedWeb paper](https://arxiv.org/abs/2306.01116).

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


## License

Falcon-7B-Instruct is made available under the Apache 2.0 license.

## Contact
falconllm@tii.ae