

# **V0.3 IS UP**

[Link to V0.3](https://huggingface.co/maywell/Synatra-7B-v0.3-base)

# **Synatra-V0.1-7B**  

Made by StableFluffy

[Visit my website! - Currently on consturction..](https://www.stablefluffy.kr/)

## License

This model is strictly [*non-commercial*](https://creativecommons.org/licenses/by-nc/4.0/) (**cc-by-nc-4.0**) use only which takes priority over the **LLAMA 2 COMMUNITY LICENSE AGREEMENT**.
The "Model" is completely free (ie. base model, derivates, merges/mixes) to use for non-commercial purposes as long as the the included **cc-by-nc-4.0** license in any parent repository, and the non-commercial use statute remains, regardless of other models' licences. 
The licence can be changed after new model released.

## Model Details
**Base Model**  
[mistralai/Mistral-7B-Instruct-v0.1](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)    

**Trained On**  
A6000 48GB * 8

## Instruction format

**학습 과정의 실수로 [/INST]가 아닌 [\INST]가 적용되었습니다. v0.2 에서 수정 될 예정입니다.**

In order to leverage instruction fine-tuning, your prompt should be surrounded by `[INST]` and `[\INST]` tokens. The very first instruction should begin with a begin of sentence id. The next instructions should not. The assistant generation will be ended by the end-of-sentence token id.
Plus, It is strongly recommended to add a space at the end of the prompt.

E.g.
```
text = "<s>[INST] 아이작 뉴턴의 업적을 알려줘. [\INST] "
```

# **Model Benchmark**

## KULLM Evaluation
구름v2 repo 에서 제공되는 데이터셋과 프롬프트를 사용하여 평가했습니다.
당시 GPT4와 현재 GPT4가 완전히 동일하지는 않기에 실제 결과와 약간의 차이가 존재 할 수 있습니다.

![img](./kullm_eval.png)
| Model | 이해가능성 | 자연스러움 | 맥락유지 | 흥미로움 | 지시어사용 | 전반적퀄리티
| --- | --- | --- | --- | --- | --- | ---
| GPT-3.5 | 0.980 | 2.806 | 2.849 | 2.056 | 0.917 | 3.905
| GPT-4 | 0.984 | 2.897 | 2.944 | 2.143 | 0.968 | 4.083
| KoAlpaca v1.1 | 0.651 | 1.909 | 1.901 | 1.583 | 0.385 | 2.575
| koVicuna | 0.460 | 1.583 | 1.726 | 1.528 | 0.409 | 2.440 
| KULLM v2 | 0.742 | 2.083 | 2.107 | 1.794 | 0.548 | 3.036
| **Synatra-V0.1-7B** | **0.960** | **2.821** | **2.755** | **2.356** | **0.934** | **4.065**

## KOBEST_BOOLQ, SENTINEG, WIC - ZERO_SHOT
[EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness/tree/polyglot)를 사용하여 BoolQ, SentiNeg, Wic을 측정했습니다.

HellaSwag와 COPA는 원본코드를 수정하는 과정에서 어려움을 겪어 아직 진행하지 않았습니다.

### NOTE
BoolQ에는 Instruction 모델의 이해를 돕기위해 "위 글에 대한 질문에 사실을 확인하는 작업입니다.", "예, 아니오로 대답해주세요."의 프롬프트를 추가했습니다.
SentiNeg에는 Instruction 모델의 이해를 돕기위해 "위 문장의 긍정, 부정 여부를 판단하세요."의 프롬프트를 추가했습니다.
Wic의 경우는 [INST], [\INST]만 추가하였습니다.


| Model | COPA | HellaSwag | BoolQ | SentiNeg | Wic
| --- | --- | --- | --- | --- | ---
| EleutherAI/polyglot-ko-12.8b | 0.7937 | 0.5954 | 0.4818 | 0.9117 | 0.3985
| **Synatra-V0.1-7B** | **NaN** | **NaN** | **0.849** | **0.8690** | **0.4881**

# **Implementation Code**

Since, chat_template already contains insturction format above.
You can use the code below.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda" # the device to load the model onto

model = AutoModelForCausalLM.from_pretrained("maywell/Synatra-V0.1-7B")
tokenizer = AutoTokenizer.from_pretrained("maywell/Synatra-V0.1-7B")

messages = [
    {"role": "user", "content": "What is your favourite condiment?"},
]

encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")

model_inputs = encodeds.to(device)
model.to(device)

generated_ids = model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
decoded = tokenizer.batch_decode(generated_ids)
print(decoded[0])
```

If you run it on oobabooga your prompt would look like this. - ** Need to add Space at the end! **
```
[INST] 링컨에 대해서 알려줘. [\INST] 
```

> Readme format: [beomi/llama-2-ko-7b](https://huggingface.co/beomi/llama-2-ko-7b)

---
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_maywell__Synatra-V0.1-7B)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 53.54   |
| ARC (25-shot)         | 55.29          |
| HellaSwag (10-shot)   | 76.63    |
| MMLU (5-shot)         | 55.29         |
| TruthfulQA (0-shot)   | 55.76   |
| Winogrande (5-shot)   | 72.77   |
| GSM8K (5-shot)        | 19.41        |
| DROP (3-shot)         | 39.63         |
