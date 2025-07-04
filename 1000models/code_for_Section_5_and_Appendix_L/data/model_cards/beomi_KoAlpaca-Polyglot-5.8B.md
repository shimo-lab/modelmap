
Update @ 2023.06.01

- Add Safetensor sharded model weight (max shard = 1GB)

# KoAlpaca-Polyglot-5.8B (v1.1b)

This model is a fine-tuned version of [EleutherAI/polyglot-ko-5.8b](https://huggingface.co/EleutherAI/polyglot-ko-5.8b) on a KoAlpaca Dataset v1.1b

Detail Codes are available at [KoAlpaca Github Repository](https://github.com/Beomi/KoAlpaca)

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2.0
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.29.0.dev0
- Pytorch 2.0.0+cu117
- Datasets 2.10.1
- Tokenizers 0.13.2
