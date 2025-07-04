
## L-MChat-Small

<div style="text-align:center;width:250px;height:250px;">
    <img src="https://priority.cdn.leunos.com/logo-l-mchat-rs.png" alt="L-MChat-Series-Logo"">
</div>

This was a test of mine how small merges perform, because there are a lot of 7b merges and higher but not a lot of 2b merges.

### Merge Method

This model was merged using the SLERP merge method.

### Models Merged

The following models were included in the merge:
* [rhysjones/phi-2-orange-v2](https://huggingface.co/rhysjones/phi-2-orange-v2)
* [Weyaxi/Einstein-v4-phi2](https://huggingface.co/Weyaxi/Einstein-v4-phi2)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
- sources:
  - model: Weyaxi/Einstein-v4-phi2
    layer_range:
    - 0
    - 32
  - model: rhysjones/phi-2-orange-v2
    layer_range:
    - 0
    - 32
merge_method: slerp
base_model: rhysjones/phi-2-orange-v2
parameters:
  t:
  - filter: self_attn
    value:
    - 0
    - 0.5
    - 0.3
    - 0.7
    - 1
  - filter: mlp
    value:
    - 1
    - 0.5
    - 0.7
    - 0.3
    - 0
  - value: 0.5
dtype: bfloat16
```

## Usage

Use it with the ChatML format, you can also use the Inference-API for this Model.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Artples__L-MChat-Small)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |63.14|
|AI2 Reasoning Challenge (25-Shot)|61.60|
|HellaSwag (10-Shot)              |75.90|
|MMLU (5-Shot)                    |57.41|
|TruthfulQA (0-shot)              |49.94|
|Winogrande (5-shot)              |74.98|
|GSM8k (5-shot)                   |58.98|

