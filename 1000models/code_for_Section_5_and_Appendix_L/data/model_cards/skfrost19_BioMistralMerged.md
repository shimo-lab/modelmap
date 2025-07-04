# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the SLERP merge method.

### Models Merged

The following models were included in the merge:
* [mohsenfayyaz/Mistral-7B-Instruct-v0.2_medical_bios_5000_5ep](https://huggingface.co/mohsenfayyaz/Mistral-7B-Instruct-v0.2_medical_bios_5000_5ep)
* [BioMistral/BioMistral-7B](https://huggingface.co/BioMistral/BioMistral-7B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml

slices:
  - sources:
      - model: BioMistral/BioMistral-7B
        layer_range: [0, 32]
      - model: mohsenfayyaz/Mistral-7B-Instruct-v0.2_medical_bios_5000_5ep
        layer_range: [0, 32]
merge_method: slerp
base_model: BioMistral/BioMistral-7B
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16

```