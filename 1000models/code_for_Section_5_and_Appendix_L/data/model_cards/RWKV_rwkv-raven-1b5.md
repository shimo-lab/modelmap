
![RWKlogo.png](https://s3.amazonaws.com/moonup/production/uploads/62441d1d9fdefb55a0b7d12c/UWpP-lGRZJJDaEx_uUlDv.png)

# Model card for RWKV-4 | 1B5 parameters chat version (Raven)

RWKV is a project led by [Bo Peng](https://github.com/BlinkDL). Learn more about the model architecture in the blogposts from Johan Wind [here](https://johanwind.github.io/2023/03/23/rwkv_overview.html) and [here](https://johanwind.github.io/2023/03/23/rwkv_details.html). Learn more about the project by joining the [RWKV discord server](https://discordapp.com/users/468093332535640064).

# Table of contents

0. [TL;DR](#TL;DR)
1. [Model Details](#model-details)
2. [Usage](#usage)
3. [Citation](#citation)

## TL;DR

Below is the description from the [original repository](https://github.com/BlinkDL/RWKV-LM)
> RWKV is an RNN with transformer-level LLM performance. It can be directly trained like a GPT (parallelizable). It's combining the best of RNN and transformer - great performance, fast inference, saves VRAM, fast training, "infinite" ctx_len, and free sentence embedding.

## Model Details

The details of the architecture can be found on the blogpost mentioned above and the Hugging Face blogpost of the integration.

## Usage

### Convert the raw weights to the HF format

You can use the [`convert_rwkv_checkpoint_to_hf.py`](https://github.com/huggingface/transformers/tree/main/src/transformers/models/rwkv/convert_rwkv_checkpoint_to_hf.py) script by specifying the repo_id of the original weights, the filename and the output directory. You can also optionally directly push the converted model on the Hub by passing `--push_to_hub` flag and `--model_name` argument to specify where to push the converted weights.

```bash
python convert_rwkv_checkpoint_to_hf.py --repo_id RAW_HUB_REPO --checkpoint_file RAW_FILE --output_dir OUTPUT_DIR --push_to_hub --model_name dummy_user/converted-rwkv
```

### Generate text

You can use the `AutoModelForCausalLM` and `AutoTokenizer` classes to generate texts from the model. Expand the sections below to understand how to run the model in different scenarios:
The "Raven" models needs to be prompted in a specific way, learn more about that [in the integration blogpost](https://huggingface.co/blog/rwkv).

### Running the model on a CPU

<details>
<summary> Click to expand </summary>

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("RWKV/rwkv-raven-1b5")
tokenizer = AutoTokenizer.from_pretrained("RWKV/rwkv-raven-1b5")

prompt = "\nIn a shocking finding, scientist discovered a herd of dragons living in a remote, previously unexplored valley, in Tibet. Even more surprising to the researchers was the fact that the dragons spoke perfect Chinese."

inputs = tokenizer(prompt, return_tensors="pt")
output = model.generate(inputs["input_ids"], max_new_tokens=40)
print(tokenizer.decode(output[0].tolist(), skip_special_tokens=True))
```


### Running the model on a single GPU

<details>
<summary> Click to expand </summary>

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("RWKV/rwkv-raven-1b5").to(0)
tokenizer = AutoTokenizer.from_pretrained("RWKV/rwkv-raven-1b5")

prompt = "\nIn a shocking finding, scientist discovered a herd of dragons living in a remote, previously unexplored valley, in Tibet. Even more surprising to the researchers was the fact that the dragons spoke perfect Chinese."

inputs = tokenizer(prompt, return_tensors="pt").to(0)
output = model.generate(inputs["input_ids"], max_new_tokens=40)
print(tokenizer.decode(output[0].tolist(), skip_special_tokens=True))
```

</details>

</details>

### Running the model in half-precision, on GPU

<details>
<summary> Click to expand </summary>

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("RWKV/rwkv-raven-1b5", torch_dtype=torch.float16).to(0)
tokenizer = AutoTokenizer.from_pretrained("RWKV/rwkv-raven-1b5")

prompt = "\nIn a shocking finding, scientist discovered a herd of dragons living in a remote, previously unexplored valley, in Tibet. Even more surprising to the researchers was the fact that the dragons spoke perfect Chinese."

inputs = tokenizer(prompt, return_tensors="pt").to(0)
output = model.generate(inputs["input_ids"], max_new_tokens=40)
print(tokenizer.decode(output[0].tolist(), skip_special_tokens=True))
```

</details>


### Running the model multiple GPUs
<details>
<summary> Click to expand </summary>

```python
# pip install accelerate
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("RWKV/rwkv-raven-1b5", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("RWKV/rwkv-raven-1b5")

prompt = "\nIn a shocking finding, scientist discovered a herd of dragons living in a remote, previously unexplored valley, in Tibet. Even more surprising to the researchers was the fact that the dragons spoke perfect Chinese."

inputs = tokenizer(prompt, return_tensors="pt").to(0)
output = model.generate(inputs["input_ids"], max_new_tokens=40)
print(tokenizer.decode(output[0].tolist(), skip_special_tokens=True))
```

</details>

## Citation

If you use this model, please consider citing the original work, from the original repo [here](https://github.com/BlinkDL/ChatRWKV/)