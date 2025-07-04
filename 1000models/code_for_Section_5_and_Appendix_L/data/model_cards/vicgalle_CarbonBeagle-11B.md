# CarbonBeagle-11B

An experiment in merging models of different architectures and sizes. Here are the steps:

1. Upscale mlabonne/NeuralBeagle14-7B to vicgalle/franken-Beagle-11B.
2. DPO-tune vicgalle/franken-Beagle-11B to vicgalle/NeuralBeagle-11B.
3. Merge vicgalle/NeuralBeagle-11B and jeonsworld/CarbonVillain-en-10.7B-v4.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/5fad8602b8423e1d80b8a965/C1FMtz2kX9UyCwX1CGDKM.png)

## Merge Details
### Merge Method

This model was merged using the [linear](https://arxiv.org/abs/2203.05482) merge method.

### Models Merged

The following models were included in the merge:
* [vicgalle/NeuralBeagle-11B](https://huggingface.co/vicgalle/NeuralBeagle-11B)
* [jeonsworld/CarbonVillain-en-10.7B-v4](https://huggingface.co/jeonsworld/CarbonVillain-en-10.7B-v4)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
    - model: jeonsworld/CarbonVillain-en-10.7B-v4
      parameters:
        weight: 1.0
    - model: vicgalle/NeuralBeagle-11B
      parameters:
        weight: 0.5
merge_method: linear

dtype: float16
```

## Evaluations

At the time of its creation (21-01-2024), it is the best model in the Open LLM Leaderboard for its size class (10.7B-11B), and also 13B models:


![image/png](https://cdn-uploads.huggingface.co/production/uploads/5fad8602b8423e1d80b8a965/J4Jd_lx-Nja7CsNBSQ9re.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/5fad8602b8423e1d80b8a965/W2WgMmI7KZlyd61bJTgFs.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/5fad8602b8423e1d80b8a965/oytHEbGe68rxXV-5PwsXj.png)

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_vicgalle__CarbonBeagle-11B)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |74.64|
|AI2 Reasoning Challenge (25-Shot)|71.84|
|HellaSwag (10-Shot)              |88.93|
|MMLU (5-Shot)                    |66.62|
|TruthfulQA (0-shot)              |69.43|
|Winogrande (5-shot)              |84.06|
|GSM8k (5-shot)                   |66.94|


# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_vicgalle__CarbonBeagle-11B)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |22.36|
|IFEval (0-Shot)    |54.15|
|BBH (3-Shot)       |33.06|
|MATH Lvl 5 (4-Shot)| 5.51|
|GPQA (0-shot)      | 6.94|
|MuSR (0-shot)      | 9.19|
|MMLU-PRO (5-shot)  |25.29|

