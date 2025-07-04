
# Model Card for LDCC-SOLAR-10.7B

## Developed by : Wonchul Kim ([Lotte Data Communication](https://www.ldcc.co.kr) AI Technical Team)

## Hardware and Software

* **Hardware**: We utilized an A100x4 * 1 for training our model
* **Training Factors**: We fine-tuned this model using a combination of the [DeepSpeed library](https://github.com/microsoft/DeepSpeed) and the [HuggingFace TRL Trainer](https://huggingface.co/docs/trl/trainer) / [HuggingFace Accelerate](https://huggingface.co/docs/accelerate/index)

## Method
- This model was trained using the learning method introduced in the [SOLAR paper](https://arxiv.org/pdf/2312.15166.pdf).

## Base Model 
- [yanolja/KoSOLAR-10.7B-v0.1](https://huggingface.co/yanolja/KoSOLAR-10.7B-v0.1) (This model is no longer supported due to a tokenizer issue.)

## Caution
- If you want to fine-tune this model, it is recommended to use the [tokenizer.json](https://huggingface.co/LDCC/LDCC-SOLAR-10.7B/blob/v1.1/tokenizer.json) and [tokenizer_config.json](https://huggingface.co/LDCC/LDCC-SOLAR-10.7B/blob/v1.1/tokenizer_config.json) files from revision v1.1.