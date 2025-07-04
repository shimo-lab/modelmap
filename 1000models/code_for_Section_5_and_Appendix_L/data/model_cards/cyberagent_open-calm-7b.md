# OpenCALM-7B

## Model Description

OpenCALM is a suite of decoder-only language models pre-trained on Japanese datasets, developed by CyberAgent, Inc.

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("cyberagent/open-calm-7b", device_map="auto", torch_dtype=torch.float16)
tokenizer = AutoTokenizer.from_pretrained("cyberagent/open-calm-7b")

inputs = tokenizer("AIによって私達の暮らしは、", return_tensors="pt").to(model.device)
with torch.no_grad():
    tokens = model.generate(
        **inputs,
        max_new_tokens=64,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.05,
        pad_token_id=tokenizer.pad_token_id,
    )
    
output = tokenizer.decode(tokens[0], skip_special_tokens=True)
print(output)
```

## Model Details

|Model|Params|Layers|Dim|Heads|Dev ppl|
|:---:|:---: |:---:|:---:|:---:|:---:|
|[cyberagent/open-calm-small](https://huggingface.co/cyberagent/open-calm-small)|160M|12|768|12|19.7|
|[cyberagent/open-calm-medium](https://huggingface.co/cyberagent/open-calm-medium)|400M|24|1024|16|13.8|
|[cyberagent/open-calm-large](https://huggingface.co/cyberagent/open-calm-large)|830M|24|1536|16|11.3|
|[cyberagent/open-calm-1b](https://huggingface.co/cyberagent/open-calm-1b)|1.4B|24|2048|16|10.3|
|[cyberagent/open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b)|2.7B|32|2560|32|9.7|
|[cyberagent/open-calm-7b](https://huggingface.co/cyberagent/open-calm-7b)|6.8B|32|4096|32|8.2|

* **Developed by**: [CyberAgent, Inc.](https://www.cyberagent.co.jp/)
* **Model type**: Transformer-based Language Model
* **Language**: Japanese
* **Library**: [GPT-NeoX](https://github.com/EleutherAI/gpt-neox)
* **License**: OpenCALM is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)). When using this model, please provide appropriate credit to CyberAgent, Inc.
  * Example (en): This model is a fine-tuned version of OpenCALM-XX developed by CyberAgent, Inc. The original model is released under the CC BY-SA 4.0 license, and this model is also released under the same CC BY-SA 4.0 license. For more information, please visit: https://creativecommons.org/licenses/by-sa/4.0/
  * Example (ja): 本モデルは、株式会社サイバーエージェントによるOpenCALM-XXをファインチューニングしたものです。元のモデルはCC BY-SA 4.0ライセンスのもとで公開されており、本モデルも同じくCC BY-SA 4.0ライセンスで公開します。詳しくはこちらをご覧ください: https://creativecommons.org/licenses/by-sa/4.0/


## Training Dataset

* Wikipedia (ja)
* Common Crawl (ja)

## Author

[Ryosuke Ishigami](https://huggingface.co/rishigami)

## Citations

```bibtext
@software{gpt-neox-library,
  title = {{GPT-NeoX: Large Scale Autoregressive Language Modeling in PyTorch}},
  author = {Andonian, Alex and Anthony, Quentin and Biderman, Stella and Black, Sid and Gali, Preetham and Gao, Leo and Hallahan, Eric and Levy-Kramer, Josh and Leahy, Connor and Nestler, Lucas and Parker, Kip and Pieler, Michael and Purohit, Shivanshu and Songz, Tri and Phil, Wang and Weinbach, Samuel},
  url = {https://www.github.com/eleutherai/gpt-neox},
  doi = {10.5281/zenodo.5879544},
  month = {8},
  year = {2021},
  version = {0.0.1},
}
```