# DARE_TIES_13B

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [DARE](https://arxiv.org/abs/2311.03099) [TIES](https://arxiv.org/abs/2306.01708) merge method using [yunconglong/Truthful_DPO_TomGrc_FusionNet_7Bx2_MoE_13B](https://huggingface.co/yunconglong/Truthful_DPO_TomGrc_FusionNet_7Bx2_MoE_13B) as a base.

### Models Merged

The following models were included in the merge:
* ./13B_DPO
* ./13B_MATH_DPO

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: yunconglong/Truthful_DPO_TomGrc_FusionNet_7Bx2_MoE_13B
    parameters:
      density: 1.0
      weight: 1.0
  - model: ./13B_MATH_DPO
    parameters:
      density: 0.5
      weight: [0.33, 0.4, 0.33]
  - model: ./13B_DPO
    parameters:
      density: [0.33, 0.45, 0.66]
      weight: 0.66
merge_method: dare_ties
base_model: yunconglong/Truthful_DPO_TomGrc_FusionNet_7Bx2_MoE_13B
parameters:
  normalize: true
  int8_mask: true
dtype: bfloat16
tokenizer_source : union

```
