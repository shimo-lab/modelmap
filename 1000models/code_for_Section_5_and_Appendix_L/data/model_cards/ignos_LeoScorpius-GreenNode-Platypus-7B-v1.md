
# Model Card for Model ID

  This model is a finetuning of other models based on mistralai/Mistral-7B-v0.1.
    
## Model Details

### Model Description

  The model has been generated from the merging of the models [viethq188/LeoScorpius-7B-Chat-DPO](https://huggingface.co/viethq188/LeoScorpius-7B-Chat-DPO) and [GreenNode/GreenNodeLM-7B-v1olet](https://huggingface.co/GreenNode/GreenNodeLM-7B-v1olet) and a later finetuning with a Platypus dataset [garage-bAInd/Open-Platypus](https://huggingface.co/datasets/garage-bAInd/Open-Platypus).

- **Developed by:** Ignos
- **Model type:** Mistral
- **License:** Apache-2.0

## Uses

  The model aims to have good overall comparative results on HuggingFace metrics, improving reasoning.

## Bias, Risks, and Limitations

  The same bias, risks and limitations from base models.

## Training Details

### Training Data

- [garage-bAInd/Open-Platypus](https://huggingface.co/datasets/garage-bAInd/Open-Platypus)

### Training Procedure

- Training with QLoRA approach and merging with base model.

### Results

- Huggingface evaluation pending

#### Summary

## Technical Specifications

### Model Architecture and Objective

- Models based on Mistral Architecture

### Compute Infrastructure

- Training on RunPod

#### Hardware

- 4 x Nvidia RTX 4090
- 64 vCPU 503 GB RAM

#### Software

- Mergekit (main)
- Axolotl 0.3.0

## Training procedure

The following `bitsandbytes` quantization config was used during training:
- quant_method: bitsandbytes
- load_in_8bit: False
- load_in_4bit: True
- llm_int8_threshold: 6.0
- llm_int8_skip_modules: None
- llm_int8_enable_fp32_cpu_offload: False
- llm_int8_has_fp16_weight: False
- bnb_4bit_quant_type: nf4
- bnb_4bit_use_double_quant: True
- bnb_4bit_compute_dtype: bfloat16

### Framework versions

- PEFT 0.6.0
