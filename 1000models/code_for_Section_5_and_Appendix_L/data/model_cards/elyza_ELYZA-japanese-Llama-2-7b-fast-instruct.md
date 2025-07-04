
## ELYZA-japanese-Llama-2-7b

![ELYZA-Japanese-Llama2-image](./key_visual.png)


### Model Description
**ELYZA-japanese-Llama-2-7b** は、 Llama2をベースとして日本語能力を拡張するために追加事前学習を行ったモデルです。
詳細は [Blog記事](https://note.com/elyza/n/na405acaca130) を参照してください。

### Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
DEFAULT_SYSTEM_PROMPT = "あなたは誠実で優秀な日本人のアシスタントです。"
text = "クマが海辺に行ってアザラシと友達になり、最終的には家に帰るというプロットの短編小説を書いてください。"

model_name = "elyza/ELYZA-japanese-Llama-2-7b-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto")

if torch.cuda.is_available():
    model = model.to("cuda")

prompt = "{bos_token}{b_inst} {system}{prompt} {e_inst} ".format(
    bos_token=tokenizer.bos_token,
    b_inst=B_INST,
    system=f"{B_SYS}{DEFAULT_SYSTEM_PROMPT}{E_SYS}",
    prompt=text,
    e_inst=E_INST,
)


with torch.no_grad():
    token_ids = tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")

    output_ids = model.generate(
        token_ids.to(model.device),
        max_new_tokens=256,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )
output = tokenizer.decode(output_ids.tolist()[0][token_ids.size(1) :], skip_special_tokens=True)
print(output)
"""
承知しました。以下にクマが海辺に行ってアザラシと友達になり、最終的には家に帰るというプロットの短編小説を記述します。

クマは山の中でゆっくりと眠っていた。
その眠りに落ちたクマは、夢の中で海辺を歩いていた。
そこにはアザラシがいた。
クマはアザラシに話しかける。

「おはよう」とクマが言うと、アザラシは驚いたように顔を上げた。
「あ、こんにちは」アザラシは答えた。
クマはアザラシと友達になりたいと思う。

「私はクマと申します。」クマは...
"""
```

### ELYZA-japanese-Llama-2-7b Models

| Model Name                                   | Vocab Size | #Params |
|:---------------------------------------------|:----------:|:-------:|
|[elyza/ELYZA-japanese-Llama-2-7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b)| 32000 | 6.27B |
|[elyza/ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct)| 32000 | 6.27B |
|[elyza/ELYZA-japanese-Llama-2-7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast)| 45043 | 6.37B |
|[elyza/ELYZA-japanese-Llama-2-7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct)| 45043 | 6.37B |

### Developers
以下アルファベット順

- [Akira Sasaki](https://huggingface.co/akirasasaki)
- [Masato Hirakawa](https://huggingface.co/m-hirakawa)
- [Shintaro Horie](https://huggingface.co/e-mon)
- [Tomoaki Nakamura](https://huggingface.co/tyoyo)

### Licence

Llama 2 is licensed under the LLAMA 2 Community License, Copyright (c) Meta Platforms, Inc. All Rights Reserved.

### How to Cite

```tex
@misc{elyzallama2023, 
      title={ELYZA-japanese-Llama-2-7b}, 
      url={https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b}, 
      author={Akira Sasaki and Masato Hirakawa and Shintaro Horie and Tomoaki Nakamura},
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