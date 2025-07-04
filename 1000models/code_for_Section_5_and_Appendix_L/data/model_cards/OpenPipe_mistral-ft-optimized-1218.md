
**Update 12/27/2023**: We have released an updated version of this model with similar performance and a more permissive license at https://huggingface.co/OpenPipe/mistral-ft-optimized-1227. We recommend that model over this one for most users.

---

This model is intended to be a strong base suitable for downstream fine-tuning on a variety of tasks. Based on our internal evaluations, we believe it's one of the strongest models for most down-stream tasks. You can read more about our development and evaluation process [here](https://openpipe.ai/blog/mistral-7b-fine-tune-optimized).

---
[Mergekit](https://github.com/cg123/mergekit) config used to create this model:

```yaml
slices:
  - sources:
      - model: Weyaxi/OpenHermes-2.5-neural-chat-v3-3-Slerp
        layer_range: [0, 32]
      - model: Q-bert/MetaMath-Cybertron-Starling
        layer_range: [0, 32]
merge_method: slerp
base_model: mistralai/Mistral-7B-v0.1
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5 # fallback for rest of tensors
dtype: bfloat16
```


---
*Note*: It appears that https://huggingface.co/Weyaxi/Seraph-7B was merged from the same base models using the same [mergekit](https://github.com/cg123/mergekit) defaults as this model. So major credit goes to @Weyaxi both for creating one of the base merges this model was merged from, as well as being the first one to perform this exact merge as well!