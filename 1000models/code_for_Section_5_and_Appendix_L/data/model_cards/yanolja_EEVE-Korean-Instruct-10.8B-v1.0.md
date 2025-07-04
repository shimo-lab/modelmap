[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)

<p align="left">
  <img src="https://huggingface.co/yanolja/EEVE-Korean-Instruct-10.8B-v1.0/resolve/main/eeve_logo.webp" width="50%"/>
<p>

# EEVE-Korean-Instruct-10.8B-v1.0

## Join Our Community on Discord!

If you're passionate about the field of Large Language Models and wish to exchange knowledge and insights, we warmly invite you to join our Discord server. It's worth noting that Korean is the primary language used in this server. The landscape of LLM is evolving rapidly, and without active sharing, our collective knowledge risks becoming outdated swiftly. Let's collaborate and drive greater impact together! Join us here: [Discord Link](https://discord.gg/b27bAHg95m).

## Our Dedicated Team (Alphabetical Order)
| Research        | Engineering     | Product Management | UX Design   |
|-----------------|-----------------|--------------------|--------------
| Myeongho Jeong  | Geon Kim        | Bokyung Huh        | Eunsue Choi |
| Seungduk Kim    | Rifqi Alfi      |                    |             |
| Seungtaek Choi  | Sanghoon Han    |                    |             |
|                 | Suhyun Kang     |                    |             |

## About the Model

This model is a fine-tuned version of [yanolja/EEVE-Korean-10.8B-v1.0](https://huggingface.co/yanolja/EEVE-Korean-10.8B-v1.0), which is a Korean vocabulary-extended version of [upstage/SOLAR-10.7B-v1.0](https://huggingface.co/upstage/SOLAR-10.7B-v1.0). Specifically, we utilized Direct Preference Optimization (DPO) through the use of [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl).

For more details, please refer to our technical report: [Efficient and Effective Vocabulary Expansion Towards Multilingual Large Language Models](https://arxiv.org/abs/2402.14714).

## Prompt Template
```
A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.
Human: {prompt}
Assistant:
```
## How to Use it
```python
from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("yanolja/EEVE-Korean-Instruct-10.8B-v1.0")
tokenizer = AutoTokenizer.from_pretrained("yanolja/EEVE-Korean-Instruct-10.8B-v1.0")

prompt_template = "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.\nHuman: {prompt}\nAssistant:\n"
text = '한국의 수도는 어디인가요? 아래 선택지 중 골라주세요.\n\n(A) 경성\n(B) 부산\n(C) 평양\n(D) 서울\n(E) 전주'
model_inputs = tokenizer(prompt_template.format(prompt=text), return_tensors='pt')

outputs = model.generate(**model_inputs, max_new_tokens=256)
output_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
print(output_text)
```

### Example Output
```
A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions.
Human: 한국의 수도는 어디인가요? 아래 선택지 중 골라주세요.

(A) 경성
(B) 부산
(C) 평양
(D) 서울
(E) 전주
Assistant:
(D) 서울이 한국의 수도입니다. 서울은 나라의 북동부에 위치해 있으며, 정치, 경제, 문화의 중심지입니다. 약 1,000만 명이 넘는 인구를 가진 세계에서 가장 큰 도시 중 하나입니다. 서울은 높은 빌딩, 현대적인 인프라, 활기 문화 장면으로 유명합니다. 또한, 많은 역사적 명소와 박물관이 있어 방문객들에게 풍부한 문화 체험을 제공합니다.
```

### Training Data
  - Korean-translated version of [Open-Orca/SlimOrca-Dedup](https://huggingface.co/datasets/Open-Orca/SlimOrca-Dedup)
  - Korean-translated version of [argilla/ultrafeedback-binarized-preferences-cleaned](https://huggingface.co/datasets/argilla/ultrafeedback-binarized-preferences-cleaned)
  - No other dataset was used

## Citation

```
@misc{kim2024efficient,
      title={Efficient and Effective Vocabulary Expansion Towards Multilingual Large Language Models}, 
      author={Seungduk Kim and Seungtaek Choi and Myeongho Jeong},
      year={2024},
      eprint={2402.14714},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
```
@misc{cui2023ultrafeedback,
      title={UltraFeedback: Boosting Language Models with High-quality Feedback}, 
      author={Ganqu Cui and Lifan Yuan and Ning Ding and Guanming Yao and Wei Zhu and Yuan Ni and Guotong Xie and Zhiyuan Liu and Maosong Sun},
      year={2023},
      eprint={2310.01377},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
```
@misc{SlimOrcaDedup,
  title = {SlimOrca Dedup: A Deduplicated Subset of SlimOrca},
  author = {Wing Lian and Guan Wang and Bleys Goodson and Eugene Pentland and Austin Cook and Chanvichet Vong and "Teknium" and Nathan Hoos},
  year = {2023},
  publisher = {HuggingFace},
  url = {https://huggingface.co/datasets/Open-Orca/SlimOrca-Dedup/}
}
```
```
@misc{mukherjee2023orca,
      title={Orca: Progressive Learning from Complex Explanation Traces of GPT-4}, 
      author={Subhabrata Mukherjee and Arindam Mitra and Ganesh Jawahar and Sahaj Agarwal and Hamid Palangi and Ahmed Awadallah},
      year={2023},
      eprint={2306.02707},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_yanolja__EEVE-Korean-Instruct-10.8B-v1.0)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |66.48|
|AI2 Reasoning Challenge (25-Shot)|64.85|
|HellaSwag (10-Shot)              |83.04|
|MMLU (5-Shot)                    |64.23|
|TruthfulQA (0-shot)              |54.09|
|Winogrande (5-shot)              |81.93|
|GSM8k (5-shot)                   |50.72|

