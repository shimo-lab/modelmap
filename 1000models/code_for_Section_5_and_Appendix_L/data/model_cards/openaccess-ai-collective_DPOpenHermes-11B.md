# DPOpenHermes 11B

This is a mergekit merge of DPOpenHermes-7B from seperate versions of it.

```
slices:
  - sources:
    - model: openaccess-ai-collective/DPOpenHermes-7B
      revision: dpo-v0
      layer_range: [0, 24]
  - sources:
    - model: openaccess-ai-collective/DPOpenHermes-7B
      layer_range: [8, 32]
merge_method: passthrough
dtype: bfloat16
```