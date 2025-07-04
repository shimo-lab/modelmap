
# longchat-13b-16k Model Card

## Usage
Please use load_model from FastChat or LongChat repo to load the model (or chatting API from FastChat). There is a monkey patch needed to use the model.
Usage referece:

(LongChat) python3 eval.py --model-name-or-path  lmsys/longchat-13b-16k --task topics 

(FastChat) python3 -m fastchat.serve.cli --model-path lmsys/longchat-13b-16k

Under the hood, the monkey patch is added in:

https://github.com/lm-sys/FastChat/blob/da0641e567cf93756b0978ab5a6b092e96f06240/fastchat/model/model_adapter.py#L429

## Model details

**Model type:**
longchat-13b-16k is an open-source chatbot trained by fine-tuning llama-13b on user-shared conversations collected from ShareGPT, using the condensing rotary embedding technique reported in the [blog](https://lmsys.org/blog/2023-06-29-longchat).

**Model date:**
longchat-13b-16k was trained on June 2023.

**Organizations developing the model:**
The LongChat developers: Dacheng Li*, Rulin Shao*, Anze Xie, Ying Sheng, Lianmin Zheng, Ion Stoica, Xuezhe Ma, and Hao Zhang

**Paper or resources for more information:**
https://github.com/DachengLi1/LongChat

**Where to send questions or comments about the model:**
https://github.com/DachengLi1/LongChat

## Intended use
**Primary intended uses:**
The primary use of longchat-13b-16k is for research purposes.

**Primary intended users:**
The primary intended users of the model are researchers in natural language processing, machine learning, and artificial intelligence.

## Training dataset
18K conversations collected from ShareGPT.com.

## Evaluation dataset
A preliminary evaluation of the model quality is conducted by our released [LongEval](https://github.com/DachengLi1/LongChat).