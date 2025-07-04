
# Model Card for Llama-3-8B-Instruct-abliterated-v2

## Overview
This model card describes the Llama-3-8B-Instruct-abliterated-v2 model, which is an orthogonalized version of the meta-llama/Llama-3-8B-Instruct model, and an improvement upon the previous generation Llama-3-8B-Instruct-abliterated. This variant has had certain weights manipulated to inhibit the model's ability to express refusal.

[Join the Cognitive Computations Discord!](https://discord.gg/cognitivecomputations)

## Details

* The model was trained with more data to better pinpoint the "refusal direction".
* This model is MUCH better at directly and succinctly answering requests without producing even so much as disclaimers.

## Methodology

The methodology used to generate this model is described in the preview paper/blog post: '[Refusal in LLMs is mediated by a single direction](https://www.alignmentforum.org/posts/jGuXSZgv6qfdhMCuJ/refusal-in-llms-is-mediated-by-a-single-direction)'

## Quirks and Side Effects
This model may come with interesting quirks, as the methodology is still new and untested. The code used to generate the model is available in the Python notebook [ortho_cookbook.ipynb](https://huggingface.co/failspy/llama-3-70B-Instruct-abliterated/blob/main/ortho_cookbook.ipynb).
Please note that the model may still refuse to answer certain requests, even after the weights have been manipulated to inhibit refusal.

## Availability

## How to Use
This model is available for use in the Transformers library.  
GGUF Quants are available [here](https://huggingface.co/failspy/Llama-3-8B-Instruct-abliterated-v2-GGUF).  