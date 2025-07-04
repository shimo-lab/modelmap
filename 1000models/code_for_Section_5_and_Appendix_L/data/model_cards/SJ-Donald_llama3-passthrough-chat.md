# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the passthrough merge method.

### Models Merged

The following models were included in the merge:
* [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)

### Configuration

The following YAML configuration was used to produce this model:

```yaml

slices:
  - sources:
    - model: meta-llama/Meta-Llama-3-8B-Instruct
      layer_range: [0, 24]
  - sources:
    - model: meta-llama/Meta-Llama-3-8B-Instruct
      layer_range: [8, 32]
merge_method: passthrough
dtype: float16


```