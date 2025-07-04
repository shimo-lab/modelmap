
![image/png](https://cdn-uploads.huggingface.co/production/uploads/64c14f6b02e1f8f67c73bd05/lFg2fOnPhcKFfJGnIvcTd.png)

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->

Llama2 13B finetuned to process longer (32K) contexts using interpolation and then further instruct finetuned with ShareGPT and Orca-Chat.

## Model Details

### Model Description

This is next version of the model trained and evaluated as part of the experiments described in the repo
[http://github.com/abacusai/Long-Context](https://github.com/abacusai/Long-Context). This version
was trained with a scaling factor of 8 and shows better reasoning and math abilites on State of the Art benchmarks

- **Developed by:** [Abacus.AI](https://abacus.ai)
- **Model type:** Transformer based autoregressive causal language model
- **License:** Llama 2 Community License: https://github.com/facebookresearch/llama/blob/main/LICENSE
- **Finetuned from model:** Llama V2 13B

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** [http://github.com/abacusai/Long-Context](https://github.com/abacusai/Long-Context)

### Direct Use

Since the model is instruct finetuned it can also be directly used for various prompted tasks. We have tested
it on open book question answering using the long context to supply search results.

## Bias, Risks, and Limitations

The model has not been evaluated for safety and is only intended for research and experiments.