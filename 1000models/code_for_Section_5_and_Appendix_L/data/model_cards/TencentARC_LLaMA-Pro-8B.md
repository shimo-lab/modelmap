
# LLaMA-Pro-8B Model Card

## Model Description
LLaMA-Pro is a progressive version of the original LLaMA model, enhanced by the addition of Transformer blocks. It specializes in integrating both general language understanding and domain-specific knowledge, particularly in programming and mathematics.

## Development and Training
Developed by Tencent's ARC Lab, LLaMA-Pro is an 8.3 billion parameter model. It's an expansion of LLaMA2-7B, further trained on code and math corpora totaling 80 billion tokens.

## Intended Use
This model is designed for a wide range of NLP tasks, with a focus on programming, mathematics, and general language tasks. It suits scenarios requiring integration of natural and programming languages.

## Performance
LLaMA-Pro demonstrates advanced performance across various benchmarks. It outperforms existing models in the LLaMA series in handling diverse tasks, showcasing its capability as an intelligent language agent.

### Overall Performance on Languages, math and code tasks

  | Model | ARC | Hellaswag | MMLU | TruthfulQA | Winogrande | GSM8K | GSM8K-PoT | HumanEval | MBPP | Avg |
  | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
  | LLAMA PRO (8B) | 54.10 | 77.94 | 47.88 | 39.04 | 73.95 | 17.89 | 25.42 | 28.66 | 33.20 | 44.2 |
  | LLaMA2-7B | 53.07 | 78.59 | 46.87 | 38.76 | 74.03 | 14.48 | 17.68 | 13.05 | 20.09 | 39.62 |
  | CodeLLaMA-7B | 39.93 | 60.80 | 31.12 | 37.82 | 64.01 | 5.16 | 25.20 | 33.50 | 41.40 | 37.66 |
  | LLAMA PRO-INSTRUCT | 52.30 | 76.88 | 52.57 | 48.80 | 72.53 | 43.59 | 55.61 | 44.51 | 37.88 | 53.8 |

### Performance on GPT4 Evaluation

| Model | MT Bench |
| :-: | :-: |
| Alpaca-13B | 4.53 |
| CodeLLaMA-7B-Instruct | 5.71 |
| Vicuna-7B | 6.17 |
| LLaMA2-7B-Chat | 6.27 |
| LLAMA PRO-INSTRUCT | 6.32 | 

## Limitations
While LLaMA-Pro addresses some limitations of previous models in the series, it may still encounter challenges specific to highly specialized domains or tasks.

## Ethical Considerations
Users should be aware of potential biases in the model and use it responsibly, considering its impact on various applications.
