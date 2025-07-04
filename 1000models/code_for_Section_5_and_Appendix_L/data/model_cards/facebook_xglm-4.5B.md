
# XGLM-4.5B

XGLM-4.5B is a multilingual autoregressive language model (with 4.5 billion parameters) trained on a balanced corpus of a diverse set of 134 languages. It was introduced in the paper [Few-shot Learning with Multilingual Language Models](https://arxiv.org/abs/2112.10668) by Xi Victoria Lin\*, Todor Mihaylov, Mikel Artetxe, Tianlu Wang, Shuohui Chen, Daniel Simig, Myle Ott, Naman Goyal, Shruti Bhosale, Jingfei Du, Ramakanth Pasunuru, Sam Shleifer, Punit Singh Koura, Vishrav Chaudhary, Brian O'Horo, Jeff Wang, Luke Zettlemoyer, Zornitsa Kozareva, Mona Diab, Veselin Stoyanov, Xian Li\* (\*Equal Contribution). The original implementation was released in [this repository](https://github.com/pytorch/fairseq/tree/main/examples/xglm).

## Model card

For intended usage of the model, please refer to the [model card](https://github.com/pytorch/fairseq/blob/main/examples/xglm/model_card.md) released by the XGLM-4.5B development team. 

## Example (COPA)
The following snippet shows how to evaluate our models (GPT-3 style, zero-shot) on the Choice of Plausible Alternatives (COPA) task, using examples in English, Chinese and Hindi.

```python
import torch
import torch.nn.functional as F

from transformers import XGLMTokenizer, XGLMForCausalLM

tokenizer = XGLMTokenizer.from_pretrained("facebook/xglm-4.5B")
model = XGLMForCausalLM.from_pretrained("facebook/xglm-4.5B")

data_samples = {
    'en': [
        {
            "premise": "I wanted to conserve energy.",
            "choice1": "I swept the floor in the unoccupied room.",
            "choice2": "I shut off the light in the unoccupied room.",
            "question": "effect",
            "label": "1"
        },
        {
            "premise": "The flame on the candle went out.",
            "choice1": "I blew on the wick.",
            "choice2": "I put a match to the wick.",
            "question": "cause",
            "label": "0"
        }
    ],
    'zh': [
        {
            "premise": "我想节约能源。",
            "choice1": "我在空着的房间里扫了地板。",
            "choice2": "我把空房间里的灯关了。",
            "question": "effect",
            "label": "1"
        },
        {
            "premise": "蜡烛上的火焰熄灭了。",
            "choice1": "我吹灭了灯芯。",
            "choice2": "我把一根火柴放在灯芯上。",
            "question": "cause",
            "label": "0"
        }
    ],
    'hi': [
        {
            "premise": "M te vle konsève enèji.",
            "choice1": "Mwen te fin baleye chanm lib la.",
            "choice2": "Mwen te femen limyè nan chanm lib la.",
            "question": "effect",
            "label": "1"
        },
        {
            "premise": "Flam bouji a te etenn.",
            "choice1": "Mwen te soufle bouji a.",
            "choice2": "Mwen te limen mèch bouji a.",
            "question": "cause",
            "label": "0"
        }
    ]
}

def get_logprobs(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids, output_ids = inputs["input_ids"], inputs["input_ids"][:, 1:]
    outputs = model(**inputs, labels=input_ids)
    logits = outputs.logits
    logprobs = torch.gather(F.log_softmax(logits, dim=2), 2, output_ids.unsqueeze(2))
    return logprobs

# Zero-shot evaluation for the Choice of Plausible Alternatives (COPA) task.
# A return value of 0 indicates that the first alternative is more plausible,
# while 1 indicates that the second alternative is more plausible.
def COPA_eval(prompt, alternative1, alternative2):
    lprob1 = get_logprobs(prompt + "\n" + alternative1).sum()
    lprob2 = get_logprobs(prompt + "\n" + alternative2).sum()
    return 0 if lprob1 > lprob2 else 1

for lang in data_samples_long:
    for idx, example in enumerate(data_samples_long[lang]):
        predict = COPA_eval(example["premise"], example["choice1"], example["choice2"])
        print(f'{lang}-{idx}', predict, example['label'])
        
# en-0 1 1
# en-1 0 0
# zh-0 1 1
# zh-1 0 0
# hi-0 1 1
# hi-1 0 0
```