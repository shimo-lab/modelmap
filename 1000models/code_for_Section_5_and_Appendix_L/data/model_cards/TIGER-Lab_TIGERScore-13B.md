

## TIGERScore

[Project Page](https://tiger-ai-lab.github.io/TIGERScore/) | [Paper](https://arxiv.org/abs/2310.00752) | [Code](https://github.com/TIGER-AI-Lab/TIGERScore) | [🤗Demo](https://huggingface.co/spaces/TIGER-Lab/TIGERScore) | 
[🤗TIGERScore-7B](https://huggingface.co/TIGER-Lab/TIGERScore-7B-V1.2) | [🤗TIGERScore-13B](https://huggingface.co/TIGER-Lab/TIGERScore-13B-V1.2)

## Introduction

We present TIGERScore, a **T**rained metric that follows **I**nstruction **G**uidance to perform **E**xplainable, and **R**eference-free evaluation over a wide spectrum of text generation tasks. Our metric is based on LLaMA-2, trained on our meticulously curated instruction-tuning dataset [MetricInstruct](https://huggingface.co/datasets/TIGER-Lab/MetricInstruct) which covers 6 text generation tasks and 23 text generation datasets. 

Existing automatic metrics are lagging and suffer from issues like 1) **Dependency on references**, 2) **Limited to specific domains**, 3) **Lack of attribution**. Contrary to them, TIGERScore is designed to be driven by natural language instruction and provide detailed error analysis to pinpoint the mistakes in the generated text.

Specifically, TIGERScore takes an instruction, an associated input context along with a hypothesis output that might contain errors. Then, TIGERScore will evaluate this hypothesis output and list several errors, each consisting of the error location, aspect, explanation and penalty scores (score reduced, starting from 0). The sum of the reduced scores is taken as the overall rating of this output.

As a reference-free metric, its correlation can even surpass the best existing reference-based metrics. We believe TIGERScore demonstrates the possibility of building universal explainable metrics to evaluate any text generation task.

## Training Data

The models are trained on the 🤗 [MetricInstruct Dataset](https://huggingface.co/datasets/TIGER-Lab/MetricInstruct), which covers 6 text generation tasks and 22 text generation datasets. Check out the dataset card for more details.

## Training Procedure

The models are fine-tuned with the MetricInstruct dataset using the original Llama-2 model as base models. The training procedure varies for different models based on their sizes. Check out our paper for more details.

## Evaluation

Experiments show that TIGERScore surpasses existing baseline metrics in correlation with human ratings on all 6 held-in tasks and 1 held-out task, achiving the highest overall performance. We hope the emergence of TIGERScore can promote the research in the LLM community as a powerful, interpretable, and easy-to-use metric.

### Kendall Results
| Tasks⟶                                    | Summarization  | Translation    | Data2Text      | Long-form QA    | MathQA         | Instruction Following   | Story-Gen      | Average        |
|----------------------------------------|-----------|-----------|-----------------|-----------|-----------|-----------|-----------|-----------|
|                                        |           |           | GPT-based | Metrics        |           |           |           |           |
| GPT-3.5-turbo (few-shot)               | **30.45** | 32.3      | 30.38           | 20.91     | **58.57** | 17.73     | 3.26      | 27.65     |
| GPT-4 (zero-shot)                      | 29.32     | **35.38** | **32.26**       | **35.85** | 46.63     | **49.5**  | **25.69** | **36.38** |
|                                        |           |           | Reference-based | Metrics    |           |           |           |           |
| BLEU                                   | 8.71      | 14.5      | 23.13           | 7.73      | 17.25     | 35.92     | -0.89     | 15.19     |
| ROUGE-2f                               | 10.67     | 13.19     | 24.74           | 11.73     | 18.07     | 34.59     | 1.78      | 16.4      |
| InstructScore                          | 20.86     | 40.44     | 30.21           | 15.64     | -3.87     | 13.87     | 13.5      | 18.66     |
| GPTScore-ref                           | 10.8      | 18.74     | 27.47           | 22.13     | 14.86     | 25.4      | 12.78     | 18.88     |
| BARTScore-cnn (hypo-ref)               | 10        | 21.06     | 27.04           | 20.67     | **19.07** | 24.7      | 18.58     | 20.16     |
| BARTScore-para (hypo-ref)              | 10.41     | 24.9      | 28.42           | 20.24     | 14.1      | 26.13     | 12.11     | 19.47     |
| BERTScore                              | 17.39     | 31.57     | 30.74           | 17.7      | 9.41      | 35.61     | 2         | 20.63     |
| BLEURT                                 | 12.69     | 36.12     | **34.48**       | 23.11     | 2.88      | 27.94     | 19.18     | 22.34     |
| UniEval (summ)                         | **35.89** | 16.08     | 28.56           | **29.32** | 16.15     | 11.93     | **31.22** | 24.17     |
| COMET-22                               | 25.01     | **42.79** | 23.43           | 24.66     | -4.52     | **36.17** | 27.52     | **25.01** |
|                                        |           |           | Reference-free  |Metrics    |           |           |           |           |
| BARTScore-para (src-hypo)              | 29.12     | 7.01      | 22.32           | 18.8      | -2.21     | 4.26      | 14.15     | 13.35     |
| BARTScore-cnn (src-hypo)               | 26.63     | 9.4       | 23.69           | 28.93     | 1.23      | 19.09     | 23.29     | 18.89     |
| Llama-2-13b-chat-0-shot                | 25.22     | 11.79     | 23.45           | 15.96     | 1.08      | 19.5      | 21.52     | 16.93     |
| COMETKiwi                              | 11.87     | 36.37     | 19.08           | 12.23     | -9.38     | 26.46     | 12.78     | 15.63     |
| GPTScore-src                           | 28.2      | 6.5       | 19.81           | 27.64     | 11.64     | 20.04     | 16.36     | 18.6      |
| TigerScore-7B                          | 28.79     | 33.65     | 32.44           | 33.93     | 19.98     | 38.13     | 29.72     | 30.95     |
| TigerScore-13B                         | **31.29** | **36.5**  | **36.43**       | **33.17** | **21.58** | **41.84** | **35.33** | **33.73** |
| ∆ (ours - best reference-free)  | +2         | +0         | +13              | +4         | +10        | +15        | +14        | +15        |
| ∆ (ours - best reference-based) | -4        | -6        | +2               | +4         | +2         | +5         | +4         | +8         |

### Pearson Results

| Tasks⟶                                    | Summarization  | Translation    | Data2Text      | Long-form QA    | MathQA         | Instruction Following   | Story-Gen      | Average        |
|-------------------------------|-----------|-----------|-----------------|-----------|-----------|-----------|-----------|-----------|
|                               |           |           | GPT-based       | Metrics   |           |           |           |           |
| GPT-3.5-turbo (few-shot)      | **45.53** | **43.77** | **47.76**       | 29.84     | **61.26** | 15.36     | 7.8       | 35.9      |
| GPT-4 (zero-shot)             | 40.75     | 33.92     | 46.83           | **49.3**  | 54.98     | **60.45** | **37.74** | **46.28** |
|                               |           |           | Reference-based | Metrics   |           |           |           |           |
| BLEU                          | 11.66     | 17.47     | 34.29           | 18.21     | 18.12     | 29.47     | -0.64     | 18.37     |
| ROUGE-2f                      | 16.03     | 16.26     | 35.85           | 19.66     | 20.69     | 33.49     | 2.88      | 20.69     |
| InstructScore                 | 27.4      | 51.55     | 47.28           | 20.59     | 0.36      | 20.98     | 12.81     | 25.85     |
| GPTScore-ref                  | 13.47     | 21.05     | 48.7            | 33.4      | 18.22     | 29.66     | 18.94     | 26.2      |
| BARTScore-cnn (hypo-ref)      | 16.67     | 23.56     | 45.08           | 32.78     | **23.09** | 26.57     | 27.61     | 27.91     |
| BARTScore-para (hypo-ref)     | 19.73     | 29.04     | 47.89           | 32.7      | 17.33     | 30.2      | 17.76     | 27.81     |
| BERTScore                     | 26.26     | 37.65     | 48.22           | 26.39     | 11.19     | 45.58     | 4.08      | 28.48     |
| BLEURT                        | 17.27     | 43        | **54.32**       | 34.26     | 3.98      | 39.15     | 27.89     | 31.41     |
| UniEval (summ)                | **53.22** | 23.11     | 51.14           | **36.95** | 17.69     | 30.87     | **44.88** | 36.84     |
| COMET-22                      | 35.32     | **58.46** | 43.82           | 36.79     | -5.58     | **49.68** | 40.12     | **36.94** |
|                               |           |           | Reference-free  | Metrics   |           |           |           |           |
| BARTScore-para (src-hypo)     | 43.11     | 6.96      | 37.82           | 29.86     | -0.41     | 19.37     | 19.99     | 22.38     |
| BARTScore-cnn (src-hypo)      | 39.72     | 9.53      | 45.43           | 41.48     | 3.28      | 34.97     | 33.51     | 29.7      |
| Llama-2-13b-chat-0-shot       | 29.59     | 9.09      | 41.32           | 21.67     | 2.8       | 22.71     | 21.13     | 21.19     |
| COMETKiwi                     | 14.22     | **50.91** | 23.63           | 22.59     | -13.35    | 34.46     | 19.12     | 21.65     |
| GPTScore-src                  | 41.71     | 6.82      | 41.19           | 39.79     | 13.99     | 27.59     | 23.22     | 27.76     |
| TigerScore-7B                 | 43.95     | 37.7      | 49.13           | **46.1**  | 21.77     | 38.26     | 39.9      | 39.54     |
| TigerScore-13B                | **44.21** | 41.54     | **52.87**       | 44.76     | **24.41** | **47.52** | **47.66** | **43.28** |
| ∆ (ours - best reference-free)  | +1         | -9        | +7               | +5         | +10        | +20        | +14        | +13        |
| ∆ (ours - best reference-based) | -9        | -17       | -2              | +9         | +1         | -2        | +3         | +6         |

### Spearman Results

| Tasks⟶                                    | Summarization  | Translation    | Data2Text      | Long-form QA    | MathQA         | Instruction Following   | Story-Gen      | Average        |
|-------------------------------------------|----------------|----------------|----------------|-----------------|----------------|----------------|----------------|----------------|
|                               |           |           | GPT-based       | Metrics   |           |           |           |           |
| GPT-3.5-turbo (few-shot)                  | **38.50**      | 40.53          | 40.20          | 29.33           | **66.46**      | 23.20          | 4.77           | 34.71          |
| GPT-4 (zero-shot)                         | 36.46          | **43.87**      | **44.04**      | **48.95**       | 51.71          | **58.53**      | **32.48**      | **45.15**      |
|                               |           |           | Reference-based | Metrics   |           |           |           |           |
| BLEU                                      | 11.98          | 19.73          | 33.29          | 11.38           | 21.12          | **46.61**      | -1.17          | 20.42          |
| ROUGE-2f                                  | 14.53          | 17.83          | 35.49          | 16.83           | 22.12          | 44.56          | 2.34           | 21.96          |
| InstructScore                             | 26.33          | 47.30          | 43.93          | 21.62           | -4.15          | 16.19          | 16.13          | 23.91          |
| GPTScore-ref                              | 14.73          | 24.95          | 39.42          | 31.60           | 18.20          | 33.14          | 18.24          | 25.75          |
| BARTScore-cnn(hypo-ref)                   | 13.64          | 28.53          | 36.12          | 29.57           | **23.35**      | 32.49          | 26.64          | 27.19          |
| BARTScore-para (hypo-ref)                 | 17.18          | 33.72          | 40.79          | 28.94           | 17.27          | 34.47          | 17.43          | 27.11          |
| BERTScore                                 | 23.67          | 42.41          | 43.75          | 25.60           | 11.53          | 45.77          | 2.88           | 27.95          |
| BLEURT                                    | 17.30          | 48.41          | **48.76**      | 33.26           | 3.53           | 36.46          | 27.52          | 30.75          |
| UniEval(summ)                             | **47.52**      | 21.90          | 38.38          | **41.83**       | 19.78          | 16.02          | **44.46**      | 32.84          |
| COMET-22                                  | 33.75          | **56.35**      | 33.92          | 35.28           | -5.53          | 46.13          | 39.20          | **34.16**      |
|                               |           |           | Reference-free  | Metrics   |           |           |           |           |
| BARTScore-para (src-hypo)                 | **38.68**      | 9.60           | 32.26          | 26.86           | -2.70          | 5.92           | 20.55          | 18.74          |
| BARTScore-cnn (src-hypo)                  | 35.50          | 12.83          | 34.33          | 40.96           | 1.50           | 25.43          | 33.48          | 26.29          |
| Llama-2-13b-chat-0-shot                   | 28.53          | 14.38          | 29.24          | 19.91           | 1.08           | 21.37          | 26.78          | 20.18          |
| COMETKiwi                                 | 16.27          | **48.48**      | 27.90          | 18.05           | -11.48         | 34.86          | 18.47          | 21.79          |
| GPTScore-src                              | 37.41          | 8.90           | 28.82          | 39.48           | 14.25          | 26.46          | 23.91          | 25.61          |
| TIGERScore-7B (ours)                      | 35.11          | 41.50          | 42.39          | **47.11**       | 21.23          | 43.57          | 39.26          | 38.60          |
| TIGERScore-13B (ours)                     | 36.81          | 44.99          | **45.88**      | 46.22           | **23.32**      | **47.03**      | **46.36**      | **41.52**      |
| Δ (ours - best reference-free)            | -2             | -3             | +12            | +5              | +9             | +14            | +13            | +16            |
| ∆ (ours - best reference-based) | -9        | -11       | -3              | +5         | -0         | +0        | +2         | +7         |

## Usage

TIGERScore can be easily loaded in 2 lines of codes, and provides a friendly scoring interface function.

To use TIGERScore, first install `tigerscore` with 
```bash
pip install git+https://github.com/TIGER-AI-Lab/TIGERScore.git
```

Then load the tigerscore model variates according to you needs.
```python
# set up scorer
from tigerscore import TIGERScorer
scorer = TIGERScorer(model_name="TIGER-Lab/TIGERScore-13B") # on GPU
# scorer = TIGERScorer(model_name="TIGER-Lab/TIGERScore-13B", quantized=True) # 4 bit quantization on GPU
# scorer = TIGERScorer(model_name="TIGER-Lab/TIGERScore-13B", use_vllm=True) # VLLM on GPU, Recommended for faster evaluation (0.2s per instance)
# scorer = TIGERScorer(model_name="TIGER-Lab/TIGERScore-13B-GGUF", use_llamacpp=True) # 4 bit quantization on CPU
```

After loading, you can easily get errors of the provided **hypothesis output** given the **instruction** and **input context**
```python
# example  
instruction = "Write an apology letter."
input_context = "Reason: You canceled a plan at the last minute due to illness."
hypo_output = "Hey [Recipient],\n\nI'm really sorry for ditching our plan. I suddenly got an opportunity for a vacation so I took it. I know this might have messed up your plans and I regret that.\n\nDespite being under the weather, I would rather go for an adventure. I hope you can understand my perspective and I hope this incident doesn't change anything between us.\n\nWe can reschedule our plan for another time. Sorry again for the trouble.\n\nPeace out,\n[Your Name]\n\n---"
results = scorer.score([instruction], [hypo_output], [input_context])
print(results)
```

Results are a list of errors with detailed explanations and reasonable penalty scores:
```json
[
    {
        "num_errors": 2,
        "score": -7.0,
        "errors": {
            "error_0": {
                "location": " \"I suddenly got an opportunity for a vacation so I took it.\"",
                "aspect": " Misunderstanding context",
                "explanation": " The error lies in the context of the reason for cancelling the plan. The original reason was due to illness, but in the incorrect output, it is stated that the cancellation was due to a vacation opportunity, which is a misunderstanding of the context. The correction would be to stick to the original reason for cancelling.",
                "severity": "Major",
                "score_reduction": "5.0"
            },
            "error_1": {
                "location": " \"I hope you can understand my perspective and I hope this incident doesn't change anything between us.\"",
                "aspect": " Inappropriate tone",
                "explanation": " The tone of this sentence is too casual and lacks regret or apology. It's important to maintain a formal and regretful tone in an apology letter. The sentence could be corrected to something like \"I hope you can find it in your heart to forgive me and let this incident not strain our relationship.\"",
                "severity": "Minor",
                "score_reduction": "2.0"
            }
        },
        "raw_output": " The model-generated output contains 2 errors, with a total score reduction of 7.0.\nError location 1: ..."
    }
]
```

Check more usage at our [Github Usage Doc](https://github.com/TIGER-AI-Lab/TIGERScore#usage). Have Fun!

## Citation

If you find our work useful, please cite our paper:
```
@article{jiang2023TIGERScore,
  title={TIGERScore: Towards Building Explainable Metric for All Text Generation Tasks},
  author={Dongfu Jiang, Yishan Li, Ge Zhang, Wenhao Huang, Bill Yuchen Lin, Wenhu Chen},
  journal={arXiv preprint arXiv:2310.00752},
  year={2023}
}
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_TIGER-Lab__TIGERScore-13B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |56.79|
|AI2 Reasoning Challenge (25-Shot)|59.04|
|HellaSwag (10-Shot)              |82.79|
|MMLU (5-Shot)                    |55.07|
|TruthfulQA (0-shot)              |40.38|
|Winogrande (5-shot)              |74.74|
|GSM8k (5-shot)                   |28.73|

