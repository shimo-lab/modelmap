# LAION LeoLM: **L**inguistically **E**nhanced **O**pen **L**anguage **M**odel
Meet LeoLM, the first open and commercially available German Foundation Language Model built on Llama-2. 
Our models extend Llama-2's capabilities into German through continued pretraining on a large corpus of German-language and mostly locality specific text.
Thanks to a compute grant at HessianAI's new supercomputer **42**, we release two foundation models trained with 8k context length,
[`LeoLM/leo-hessianai-7b`](https://huggingface.co/LeoLM/leo-hessianai-7b) and [`LeoLM/leo-hessianai-13b`](https://huggingface.co/LeoLM/leo-hessianai-13b) under the [Llama-2 community license](https://huggingface.co/meta-llama/Llama-2-70b/raw/main/LICENSE.txt) (70b also coming soon! 👀).
With this release, we hope to bring a new wave of opportunities to German open-source and commercial LLM research and accelerate adoption.
Read our [blog post]() or our paper (preprint coming soon) for more details!

*A project by Björn Plüster and Christoph Schuhmann in collaboration with LAION and HessianAI.*


## Model Details
- **Finetuned from:** [meta-llama/Llama-2-7b-hf](https://huggingface.co/meta-llama/Llama-2-7b-hf)
- **Model type:** Causal decoder-only transformer language model
- **Language:** English and German
- **License:** [LLAMA 2 COMMUNITY LICENSE AGREEMENT](https://huggingface.co/meta-llama/Llama-2-70b/raw/main/LICENSE.txt)
- **Contact:** [LAION Discord](https://discord.com/invite/eq3cAMZtCC) or [Björn Plüster](mailto:bjoern.pl@outlook.de)


## Use in 🤗Transformers
First install direct dependencies:
```
pip install transformers torch sentencepiece
```
If you want faster inference using flash-attention2, you need to install these dependencies:
```bash
pip install packaging ninja
pip install flash-attn==v2.1.1 --no-build-isolation
pip install git+https://github.com/HazyResearch/flash-attention.git@v2.1.1#subdirectory=csrc/rotary
```
Then load the model in transformers:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    model="LeoLM/leo-hessianai-7b",
    device_map="auto",
    torch_dtype=torch.float16,
    trust_remote_code=True  # True for flash-attn2 else False
)
```

## Training parameters
![training_parameters](imgs/training_params.png "Training Hyperparameters")


## Benchmarks
![benchmarks](imgs/benchmarks.png "Benchmark Scores")