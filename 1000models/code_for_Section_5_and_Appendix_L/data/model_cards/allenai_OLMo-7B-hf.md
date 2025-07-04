

<img src="https://allenai.org/olmo/olmo-7b-animation.gif" alt="OLMo Logo" width="800" style="margin-left:'auto' margin-right:'auto' display:'block'"/>


# Model Card for OLMo 7B

<!-- Provide a quick summary of what the model is/does. -->

OLMo is a series of **O**pen **L**anguage **Mo**dels designed to enable the science of language models.
The OLMo models are trained on the [Dolma](https://huggingface.co/datasets/allenai/dolma) dataset.
We release all code, checkpoints, logs (coming soon), and details involved in training these models.
This model has been converted from [allenai/OLMo-7B](https://huggingface.co/allenai/OLMo-7B) for the
Hugging Face Transformers format.

## Model Details

The core models released in this batch are the following: 
| Size | Training Tokens | Layers | Hidden Size | Attention Heads | Context Length |
|------|--------|---------|-------------|-----------------|----------------|
| [OLMo 1B](https://huggingface.co/allenai/OLMo-1B-hf)   | 3 Trillion |16     | 2048        | 16              | 2048  |
| [OLMo 7B](https://huggingface.co/allenai/OLMo-7B-hf) | 2.5 Trillion   | 32     | 4096        | 32              |  2048  |
| [OLMo 7B Twin 2T](https://huggingface.co/allenai/OLMo-7B-Twin-2T-hf) | 2 Trillion   | 32     | 4096        | 32              |  2048  |

We are releasing many checkpoints for these models, for every 1000 training steps. These have not
yet been converted into Hugging Face Transformers format, but are available in [allenai/OLMo-7B](https://huggingface.co/allenai/OLMo-7B).

### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** Allen Institute for AI (AI2)
- **Supported by:** Databricks, Kempner Institute for the Study of Natural and Artificial Intelligence at Harvard University, AMD, CSC (Lumi Supercomputer), UW
- **Model type:** a Transformer style autoregressive language model.
- **Language(s) (NLP):** English
- **License:** The code and model are released under Apache 2.0.
- **Contact:** Technical inquiries: `olmo at allenai dot org`. Press: `press at allenai dot org`
- **Date cutoff:** Feb./March 2023 based on Dolma dataset version.


### Model Sources

<!-- Provide the basic links for the model. -->

- **Project Page:** https://allenai.org/olmo
- **Repositories:** 
    - Core repo (training, inference, fine-tuning etc.): https://github.com/allenai/OLMo
    - Evaluation code: https://github.com/allenai/OLMo-Eval
    - Further fine-tuning code: https://github.com/allenai/open-instruct
- **Paper:** [Link](https://arxiv.org/abs/2402.00838)
- **Technical blog post:** https://blog.allenai.org/olmo-open-language-model-87ccfc95f580
- **W&B Logs:** https://wandb.ai/ai2-llm/OLMo-7B/reports/OLMo-7B--Vmlldzo2NzQyMzk5
<!-- - **Press release:** TODO -->

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Inference
Quickly get inference running with the following:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
olmo = AutoModelForCausalLM.from_pretrained("allenai/OLMo-7B-hf")
tokenizer = AutoTokenizer.from_pretrained("allenai/OLMo-7B-hf")
message = ["Language modeling is"]
inputs = tokenizer(message, return_tensors='pt', return_token_type_ids=False)
# optional verifying cuda
# inputs = {k: v.to('cuda') for k,v in inputs.items()}
# olmo = olmo.to('cuda')
response = olmo.generate(**inputs, max_new_tokens=100, do_sample=True, top_k=50, top_p=0.95)
print(tokenizer.batch_decode(response, skip_special_tokens=True)[0])
>> 'Language modeling is the first step to build natural language generation...'
```
Alternatively, with the pipeline abstraction:
```python
from transformers import pipeline
olmo_pipe = pipeline("text-generation", model="allenai/OLMo-7B-hf")
print(olmo_pipe("Language modeling is "))
>> 'Language modeling is a branch of natural language processing that aims to...'
```

Or, you can make this slightly faster by quantizing the model, e.g. `AutoModelForCausalLM.from_pretrained("allenai/OLMo-7B-hf", torch_dtype=torch.float16, load_in_8bit=True)` (requires `bitsandbytes`).
The quantized model is more sensitive to typing / cuda, so it is recommended to pass the inputs as `inputs.input_ids.to('cuda')` to avoid potential issues.

### Fine-tuning

This model does not directly support our fine-tuning processes. Model fine-tuning can be done
from the final checkpoint or many intermediate checkpoints of
[allenai/OLMo-7B](https://huggingface.co/allenai/OLMo-7B).

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

Core model results for the 7B model are found below.

|                                   | [Llama 7B](https://arxiv.org/abs/2302.13971) | [Llama 2 7B](https://huggingface.co/meta-llama/Llama-2-7b) | [Falcon 7B](https://huggingface.co/tiiuae/falcon-7b) | [MPT 7B](https://huggingface.co/mosaicml/mpt-7b) | **OLMo 7B** (ours) |
| --------------------------------- | -------- | ---------- | --------- | ------ | ------- |
| arc_challenge       | 44.5             | 39.8             | 47.5         | 46.5         | 48.5            |
| arc_easy            | 57.0             | 57.7             | 70.4         | 70.5         | 65.4            |
| boolq               | 73.1             | 73.5             | 74.6         | 74.2         | 73.4            |
| copa                | 85.0             | 87.0             | 86.0         | 85.0         | 90              |
| hellaswag           | 74.5             | 74.5             | 75.9         | 77.6         | 76.4            |
| openbookqa          | 49.8             | 48.4             | 53.0         | 48.6         | 50.2            |
| piqa                | 76.3             | 76.4             | 78.5         | 77.3         | 78.4            |
| sciq                | 89.5             | 90.8             | 93.9         | 93.7         | 93.8            |
| winogrande          | 68.2             | 67.3             | 68.9         | 69.9         | 67.9            |
| **Core tasks average**  | 68.7             | 68.4             | 72.1         | 71.5         | 71.6            |
| truthfulQA (MC2)    | 33.9             | 38.5             | 34.0         | 33           | 36.0            |
| MMLU (5 shot MC)    | 31.5             | 45.0             | 24.0         | 30.8         | 28.3            |
| GSM8k (mixed eval.) | 10.0 (8shot CoT) | 12.0 (8shot CoT) | 4.0 (5 shot) | 4.5 (5 shot) | 8.5 (8shot CoT) |
| **Full average**        | 57.8             | 59.3             | 59.2         | 59.3         | 59.8            |

And for the 1B model:

| task       | random | [StableLM 2 1.6b](https://huggingface.co/stabilityai/stablelm-2-1_6b)\* | [Pythia 1B](https://huggingface.co/EleutherAI/pythia-1b) | [TinyLlama 1.1B](https://huggingface.co/TinyLlama/TinyLlama-1.1B-intermediate-step-1195k-token-2.5T) | **OLMo 1B** (ours) |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ | ----------------- | --------- | -------------------------------------- | ------- |
| arc_challenge | 25     | 43.81             | 33.11     | 34.78                                  | 34.45   |
| arc_easy      | 25     | 63.68             | 50.18     | 53.16                                  | 58.07   |
| boolq         | 50     | 76.6              | 61.8      | 64.6                                   | 60.7    |
| copa          | 50     | 84                | 72        | 78                                     | 79      |
| hellaswag     | 25     | 68.2              | 44.7      | 58.7                                   | 62.5    |
| openbookqa    | 25     | 45.8              | 37.8      | 43.6                                   | 46.4    |
| piqa          | 50     | 74                | 69.1      | 71.1                                   | 73.7    |
| sciq          | 25     | 94.7              | 86        | 90.5                                   | 88.1    |
| winogrande    | 50     | 64.9              | 53.3      | 58.9                                   | 58.9    |
| Average       | 36.11  | 68.41             | 56.44     | 61.48                                  | 62.42   |

\*Unlike OLMo, Pythia, and TinyLlama, StabilityAI has not disclosed yet the data StableLM was trained on, making comparisons with other efforts challenging.

## Model Details

### Data
For training data details, please see the [Dolma](https://huggingface.co/datasets/allenai/dolma) documentation.

### Architecture

OLMo 7B architecture with peer models for comparison.

|                        | **OLMo 7B**   | [Llama 2 7B](https://huggingface.co/meta-llama/Llama-2-7b) | [OpenLM 7B](https://laion.ai/blog/open-lm/) | [Falcon 7B](https://huggingface.co/tiiuae/falcon-7b) | PaLM 8B |
|------------------------|-------------------|---------------------|--------------------|--------------------|------------------|
| d_model     | 4096              | 4096                | 4096               | 4544               | 4096             |
| num heads              | 32                | 32                  | 32                 | 71                 | 16               |
| num layers             | 32                | 32                  | 32                 | 32                 | 32               |
| MLP ratio              | ~8/3         | ~8/3           | ~8/3          | 4                  | 4                |
| LayerNorm type         | non-parametric LN | RMSNorm             | parametric LN      | parametric LN      | parametric LN    |
| pos embeddings         | RoPE              | RoPE                | RoPE               | RoPE               | RoPE             |
| attention variant      | full              | GQA                 | full               | MQA                | MQA              |
| biases                 | none              | none                | in LN only         | in LN only         | none             |
| block type             | sequential        | sequential          | sequential         | parallel           | parallel         |
| activation             | SwiGLU            | SwiGLU              | SwiGLU             | GeLU               | SwiGLU           |
| sequence length        | 2048              | 4096                | 2048               | 2048               | 2048             |
| batch size (instances) | 2160              | 1024                | 2048               | 2304               | 512              |
| batch size (tokens)    | ~4M          | ~4M            | ~4M           | ~4M           | ~1M         |
| weight tying           | no                | no                  | no                 | no                 | yes              |


### Hyperparameters 

AdamW optimizer parameters are shown below.

| Size | Peak LR    | Betas           | Epsilon     | Weight Decay |
|------|------------|-----------------|-------------|--------------|
| 1B   | 4.0E-4   | (0.9, 0.95)   | 1.0E-5    | 0.1          |
| 7B   | 3.0E-4   | (0.9, 0.99)   | 1.0E-5    | 0.1          |

Optimizer settings comparison with peer models.

|                       | **OLMo 7B**  | [Llama 2 7B](https://huggingface.co/meta-llama/Llama-2-7b) | [OpenLM 7B](https://laion.ai/blog/open-lm/) | [Falcon 7B](https://huggingface.co/tiiuae/falcon-7b) |
|-----------------------|------------------|---------------------|--------------------|--------------------|
| warmup steps          | 5000             | 2000                | 2000               | 1000               |
| peak LR               | 3.0E-04 | 3.0E-04    | 3.0E-04   | 6.0E-04  |
| minimum LR            | 3.0E-05 | 3.0E-05    | 3.0E-05   | 1.2E-05   |
| weight decay          | 0.1              | 0.1                 | 0.1                | 0.1                |
| beta1                 | 0.9              | 0.9                 | 0.9                | 0.99               |
| beta2                 | 0.95             | 0.95                | 0.95               | 0.999              |
| epsilon               | 1.0E-05 | 1.0E-05    | 1.0E-05   | 1.0E-05   |
| LR schedule           | linear           | cosine              | cosine             | cosine             |
| gradient clipping     | global 1.0       | global 1.0          | global 1.0         | global 1.0         |
| gradient reduce dtype | FP32             | FP32                | FP32               | BF16               |
| optimizer state dtype | FP32             | most likely FP32    | FP32               | FP32               |



## Environmental Impact

OLMo 7B variants were either trained on MI250X GPUs at the LUMI supercomputer, or A100-40GB GPUs provided by MosaicML.
A summary of the environmental impact. Further details are available in the paper.

|           | GPU Type   | Power Consumption From GPUs | Carbon Intensity (kg CO₂e/KWh) | Carbon Emissions (tCO₂eq) |
|-----------|------------|-----------------------------|--------------------------------|---------------------------|
| OLMo 7B Twin  | MI250X ([LUMI supercomputer](https://www.lumi-supercomputer.eu))   |  135 MWh                     | 0*                             | 0*                        |
| OLMo 7B   | A100-40GB ([MosaicML](https://www.mosaicml.com)) |  104 MWh                     | 0.656                          | 75.05                     |

## Bias, Risks, and Limitations

Like any base language model or fine-tuned model without safety filtering, it is relatively easy for a user to prompt these models to generate harmful and generally sensitive content.
Such content can also be produced unintentionally, especially in the case of bias, so we recommend users consider the risks of applications of this technology.

Otherwise, many facts from OLMo or any LLM will often not be true, so they should be checked.


## Citation

**BibTeX:**

```
@article{Groeneveld2023OLMo,
  title={OLMo: Accelerating the Science of Language Models},
  author={Groeneveld, Dirk and Beltagy, Iz and Walsh, Pete and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},
  journal={Preprint},
  year={2024}
}
```

**APA:**

Groeneveld, D., Beltagy, I., Walsh, P., Bhagia, A., Kinney, R., Tafjord, O., Jha, A., Ivison, H., Magnusson, I., Wang, Y., Arora, S., Atkinson, D., Authur, R., Chandu, K., Cohan, A., Dumas, J., Elazar, Y., Gu, Y., Hessel, J., Khot, T., Merrill, W., Morrison, J., Muennighoff, N., Naik, A., Nam, C., Peters, M., Pyatkin, V., Ravichander, A., Schwenk, D., Shah, S., Smith, W., Subramani, N., Wortsman, M., Dasigi, P., Lambert, N., Richardson, K., Dodge, J., Lo, K., Soldaini, L., Smith, N., & Hajishirzi, H. (2024). OLMo: Accelerating the Science of Language Models. Preprint.

## Model Card Contact


For errors in this model card, contact Nathan, Akshita or Shane, `{nathanl, akshitab, shanea} at allenai dot org`.