
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pygmalion-6b-vicuna-chatml

This model is a fine-tuned version of [PygmalionAI/pygmalion-6b](https://huggingface.co/PygmalionAI/pygmalion-6b) on the None dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 4
- eval_batch_size: 2
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 32
- total_eval_batch_size: 16
- optimizer: Adam with betas=(0.9,0.95) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.03
- num_epochs: 3

### Training results



### Framework versions

- Transformers 4.28.1
- Pytorch 2.0.1+cu117
- Datasets 2.11.0
- Tokenizers 0.13.3
