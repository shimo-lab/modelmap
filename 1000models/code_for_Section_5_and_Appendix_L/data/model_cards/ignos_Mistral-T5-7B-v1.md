
# Model Card for Model ID

  This model is a finetuning of [Toten5/Marcoroni-neural-chat-7B-v2](https://huggingface.co/Toten5/Marcoroni-neural-chat-7B-v2)
    
## Model Details

### Model Description

- **Developed by:** Ignos
- **Model type:** Mistral
- **License:** Apache-2.0

## Uses

  Model created to improve instructional behavior.

## Bias, Risks, and Limitations

  The same bias, risks and limitations from base models.

## Training Details

### Training Data

- [tatsu-lab/alpaca](https://huggingface.co/datasets/tatsu-lab/alpaca)

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

- 3 x RTX 4090
- 48 vCPU 377 GB RAM

#### Software

- Axolotl 0.3.0

### Framework versions

- PEFT 0.6.0
