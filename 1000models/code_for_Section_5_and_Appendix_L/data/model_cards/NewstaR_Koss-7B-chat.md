<h1 style="text-align: center">Koss-7B</h1>
<h2 style="text-align: center">Training Time: 1.85h</h2>
<hr>

|        Model         |  Average ⬆️  |   ARC   | HellaSwag |   MMLU  | TruthfulQA |
|:-------------------:|:------------:|:-------:|:---------:|:-------:|:----------:|
| NewstaR/Koss-7B-chat 📑 |    55.79     |   53.67   |   78.79   |   46.72   |    43.97   |


Koss-7B is the smallest variant in the Koss series of neural network models developed by Kaleido AI for natural language processing. With 7 billion parameters, it retains much of the architecture and capabilities of the larger Koss models but requires less computation to run.

Koss-7B is intended for general NLP applications including text classification, language generation, question answering, translation, and dialogue. Its small size makes it suitable for applications with constraints on memory, compute, latency, or carbon emissions.

## Factors:

- Koss-7B should not be used for tasks requiring very specialized knowledge or skills, since its limited parameters reduce expertise in niche domains. For best performance, finetune on in-domain data.
- As with all AI systems, Koss-7B's behavior is dependent on its training data. It may exhibit biases inherited from non-diverse data. Audit data and mitigation strategies to avoid unfair impacts.
- Koss-7B is not a creative agent. Its outputs will be limited to recombinations of patterns in its training data. Do not ascribe human-like agency or consciousness.

## Recommended Prompt Template:
```
<s>[INST] {prompt} [/INST] {response} </s>
or
<s>[INST] {prompt} [/INST] 
```
The model will start it's response after the [/INST]
Example: 
```
<s>[INST] Why did the chicken cross the road? [/INST] To get to the other side! </s>
```
# Loss
![Loss.png](Loss.png)
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_NewstaR__Koss-7B-chat)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 44.98   |
| ARC (25-shot)         | 53.67          |
| HellaSwag (10-shot)   | 78.79    |
| MMLU (5-shot)         | 46.72         |
| TruthfulQA (0-shot)   | 43.97   |
| Winogrande (5-shot)   | 71.74   |
| GSM8K (5-shot)        | 7.35        |
| DROP (3-shot)         | 12.62         |
