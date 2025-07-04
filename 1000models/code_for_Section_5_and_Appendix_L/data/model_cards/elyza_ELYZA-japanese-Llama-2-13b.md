
## ELYZA-japanese-Llama-2-13b

![ELYZA-Japanese-Llama2-image](./key_visual.png)


### Model Description
**ELYZA-japanese-Llama-2-13b** は、 Llama 2をベースとして日本語能力を拡張するために追加事前学習を行ったモデルです。
詳細は [Blog記事](https://note.com/elyza/n/n5d42686b60b7) を参照してください。

### Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "elyza/ELYZA-japanese-Llama-2-13b"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    use_cache=True,
    device_map="auto",
    low_cpu_mem_usage=True,
)
model.eval()

text = "自然言語処理とは、"
token_ids = tokenizer.encode(text, add_special_tokens=False, return_tensors="pt")

with torch.no_grad():
    output_ids = model.generate(
        token_ids.to(model.device),
        max_new_tokens=256,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )
output = tokenizer.decode(output_ids.tolist()[0], skip_special_tokens=True)
print(output)
```

### ELYZA-japanese-Llama-2-13b Models

| Model Name                                   | Vocab Size | #Params |
|:---------------------------------------------|:----------:|:-------:|
|[elyza/ELYZA-japanese-Llama-2-13b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b)| 32000 | 13.02B |
|[elyza/ELYZA-japanese-Llama-2-13b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-instruct)| 32000 | 13.02B |
|[elyza/ELYZA-japanese-Llama-2-13b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-fast)| 44581 | 13.14B |
|[elyza/ELYZA-japanese-Llama-2-13b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-fast-instruct)| 44581 | 13.14B |

### Developers

- [Akira Sasaki](https://huggingface.co/akirasasaki)
- [Masato Hirakawa](https://huggingface.co/m-hirakawa)
- [Shintaro Horie](https://huggingface.co/e-mon)
- [Tomoaki Nakamura](https://huggingface.co/tyoyo)
- [Sam Passaglia](https://huggingface.co/passaglia)
- [Daisuke Oba](https://huggingface.co/daisuk30ba) (intern)

### Licence

Llama 2 is licensed under the LLAMA 2 Community License, Copyright (c) Meta Platforms, Inc. All Rights Reserved.

### How to Cite

```tex
@misc{elyzallama2023, 
      title={ELYZA-japanese-Llama-2-13b}, 
      url={https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b}, 
      author={Akira Sasaki and Masato Hirakawa and Shintaro Horie and Tomoaki Nakamura and Sam Passaglia and Daisuke Oba},
      year={2023},
}
```
    
### Citations

```tex
@misc{touvron2023llama,
      title={Llama 2: Open Foundation and Fine-Tuned Chat Models}, 
      author={Hugo Touvron and Louis Martin and Kevin Stone and Peter Albert and Amjad Almahairi and Yasmine Babaei and Nikolay Bashlykov and Soumya Batra and Prajjwal Bhargava and Shruti Bhosale and Dan Bikel and Lukas Blecher and Cristian Canton Ferrer and Moya Chen and Guillem Cucurull and David Esiobu and Jude Fernandes and Jeremy Fu and Wenyin Fu and Brian Fuller and Cynthia Gao and Vedanuj Goswami and Naman Goyal and Anthony Hartshorn and Saghar Hosseini and Rui Hou and Hakan Inan and Marcin Kardas and Viktor Kerkez and Madian Khabsa and Isabel Kloumann and Artem Korenev and Punit Singh Koura and Marie-Anne Lachaux and Thibaut Lavril and Jenya Lee and Diana Liskovich and Yinghai Lu and Yuning Mao and Xavier Martinet and Todor Mihaylov and Pushkar Mishra and Igor Molybog and Yixin Nie and Andrew Poulton and Jeremy Reizenstein and Rashi Rungta and Kalyan Saladi and Alan Schelten and Ruan Silva and Eric Michael Smith and Ranjan Subramanian and Xiaoqing Ellen Tan and Binh Tang and Ross Taylor and Adina Williams and Jian Xiang Kuan and Puxin Xu and Zheng Yan and Iliyan Zarov and Yuchen Zhang and Angela Fan and Melanie Kambadur and Sharan Narang and Aurelien Rodriguez and Robert Stojnic and Sergey Edunov and Thomas Scialom},
      year={2023},
      eprint={2307.09288},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```