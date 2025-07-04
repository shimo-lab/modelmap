
# XGLM-1.7B

XGLM-1.7B is a multilingual autoregressive language model (with 1.7 billion parameters) trained on a balanced corpus of a diverse set of languages totaling 500 billion sub-tokens. It was introduced in the paper [Few-shot Learning with Multilingual Language Models](https://arxiv.org/abs/2112.10668) by Xi Victoria Lin\*, Todor Mihaylov, Mikel Artetxe, Tianlu Wang, Shuohui Chen, Daniel Simig, Myle Ott, Naman Goyal, Shruti Bhosale, Jingfei Du, Ramakanth Pasunuru, Sam Shleifer, Punit Singh Koura, Vishrav Chaudhary, Brian O'Horo, Jeff Wang, Luke Zettlemoyer, Zornitsa Kozareva, Mona Diab, Veselin Stoyanov, Xian Li\* (\*Equal Contribution). The original implementation was released in [this repository](https://github.com/pytorch/fairseq/tree/main/examples/xglm).

## Training Data Statistics

The training data statistics of XGLM-1.7B is shown in the table below.

| ISO-639-1| family          | name                    |  # tokens    |       ratio |   ratio w/ lowRes upsampling |
|:--------|:-----------------|:------------------------|-------------:|------------:|-------------:|
| en      | Indo-European    | English                 | 803526736124 | 0.489906    |       0.3259 |
| ru      | Indo-European    | Russian                 | 147791898098 | 0.0901079   |       0.0602 |
| zh      | Sino-Tibetan     | Chinese                 | 132770494630 | 0.0809494   |       0.0483 |
| de      | Indo-European    | German                  |  89223707856 | 0.0543992   |       0.0363 |
| es      | Indo-European    | Spanish                 |  87303083105 | 0.0532282   |       0.0353 |
| fr      | Indo-European    | French                  |  77419639775 | 0.0472023   |       0.0313 |
| ja      | Japonic          | Japanese                |  66054364513 | 0.040273    |       0.0269 |
| it      | Indo-European    | Italian                 |  41930465338 | 0.0255648   |       0.0171 |
| pt      | Indo-European    | Portuguese              |  36586032444 | 0.0223063   |       0.0297 |
| el      | Indo-European    | Greek (modern)          |  28762166159 | 0.0175361   |       0.0233 |
| ko      | Koreanic         | Korean                  |  20002244535 | 0.0121953   |       0.0811 |
| fi      | Uralic           | Finnish                 |  16804309722 | 0.0102455   |       0.0681 |
| id      | Austronesian     | Indonesian              |  15423541953 | 0.00940365  |       0.0125 |
| tr      | Turkic           | Turkish                 |  12413166065 | 0.00756824  |       0.0101 |
| ar      | Afro-Asiatic     | Arabic                  |  12248607345 | 0.00746791  |       0.0099 |
| vi      | Austroasiatic    | Vietnamese              |  11199121869 | 0.00682804  |       0.0091 |
| th      | Tai–Kadai        | Thai                    |  10842172807 | 0.00661041  |       0.044  |
| bg      | Indo-European    | Bulgarian               |   9703797869 | 0.00591635  |       0.0393 |
| ca      | Indo-European    | Catalan                 |   7075834775 | 0.0043141   |       0.0287 |
| hi      | Indo-European    | Hindi                   |   3448390110 | 0.00210246  |       0.014  |
| et      | Uralic           | Estonian                |   3286873851 | 0.00200399  |       0.0133 |
| bn      | Indo-European    | Bengali, Bangla         |   1627447450 | 0.000992245 |       0.0066 |
| ta      | Dravidian        | Tamil                   |   1476973397 | 0.000900502 |       0.006  |
| ur      | Indo-European    | Urdu                    |   1351891969 | 0.000824241 |       0.0055 |
| sw      | Niger–Congo      | Swahili                 |    907516139 | 0.000553307 |       0.0037 |
| te      | Dravidian        | Telugu                  |    689316485 | 0.000420272 |       0.0028 |
| eu      | Language isolate | Basque                  |    105304423 | 6.42035e-05 |       0.0043 |
| my      | Sino-Tibetan     | Burmese                 |    101358331 | 6.17976e-05 |       0.003  |
| ht      | Creole           | Haitian, Haitian Creole |     86584697 | 5.27902e-05 |       0.0035 |
| qu      | Quechuan         | Quechua                 |      3236108 | 1.97304e-06 |       0.0001 |

## Model card

For intended usage of the model, please refer to the [model card](https://github.com/pytorch/fairseq/blob/main/examples/xglm/model_card.md) released by the XGLM-1.7B development team. 

## Example (COPA)
The following snippet shows how to evaluate our models (GPT-3 style, zero-shot) on the Choice of Plausible Alternatives (COPA) task, using examples in English, Chinese and Hindi.

```python
import torch
import torch.nn.functional as F

from transformers import XGLMTokenizer, XGLMForCausalLM

tokenizer = XGLMTokenizer.from_pretrained("facebook/xglm-1.7B")
model = XGLMForCausalLM.from_pretrained("facebook/xglm-1.7B")

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