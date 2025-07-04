# chronos-hermes-13b-v2
([chronos-13b-v2](https://huggingface.co/elinas/chronos-13b-v2) + [Nous-Hermes-Llama2-13b](https://huggingface.co/NousResearch/Nous-Hermes-Llama2-13b)) 75/25 merge

This offers the imaginative writing style of chronos while still retaining coherency and being capable. Outputs are long and utilize exceptional prose.
Supports a maxium context length of 4096.

- [GPTQ Quantized Weights](https://huggingface.co/Austism/chronos-hermes-13b-v2-GPTQ)

## Prompt Format

The model follows the Alpaca prompt format:
```
### Instruction:
<prompt>

### Response:

```
This is an adaption of [chronos-hermes-13b](https://huggingface.co/Austism/chronos-hermes-13b) for llama-2.