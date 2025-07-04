
# blockchainlabs_7B_merged_test2_4 

blockchainlabs_7B_merged_test2_4 is a merge of the following models using [mergekit](https://github.com/cg123/mergekit):
* [mlabonne/NeuralBeagle14-7B](https://huggingface.co/mlabonne/NeuralBeagle14-7B)
* [udkai/Turdus](https://huggingface.co/udkai/Turdus)

## 🧩 Configuration

```yaml
slices:
  - sources:
      - model: mlabonne/NeuralBeagle14-7B
        layer_range: [0, 32]
      - model: udkai/Turdus
        layer_range: [0, 32]
merge_method: slerp
base_model: mlabonne/NeuralBeagle14-7B
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16

```