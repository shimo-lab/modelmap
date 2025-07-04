
This is Mistral, but in 11B.

I took layers of the original Mistral-7B, and duplicated some layer, this is the first frankeinstein method that I found "acceptable" to expend Mistral.

It seems that the first 8 layers of the model is very important, having duplicate of those layers in the model make me think it confuse the model.

UPDATE: Forced mergekit to output bfloat16 file, should be the same thing, but since the base model is bfloat16, wanted it to stay bf16 like the OG model. Even if it was written bfloat16 in the config file earlier, it was float16.

<!-- description start -->
## Description

This repo contains fp16 files of Mistral-11B-v0.1.

<!-- description end -->
<!-- description start -->
## Model used

- [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1/)

<!-- description end -->
<!-- prompt-template start -->
## Prompt template: Alpaca

```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{prompt}

### Response:

```

## The secret sauce

```
slices:
  - sources:
    - model: mistralai/Mistral-7B-v0.1
      layer_range: [0, 24]
  - sources:
    - model: mistralai/Mistral-7B-v0.1
      layer_range: [8, 32]
merge_method: passthrough
dtype: bfloat16
```


Special thanks to Sushi.

If you want to support me, you can [here](https://ko-fi.com/undiai).