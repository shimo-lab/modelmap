
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="200" height="32"/>](https://wandb.ai/statking/huggingface/runs/90a8kp39)
# zephyr-7b-sft-full-orpo

This model is a fine-tuned version of [mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) on the HuggingFaceH4/ultrafeedback_binarized dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4701
- Rewards/chosen: -0.0364
- Rewards/rejected: -0.0499
- Rewards/accuracies: 0.6587
- Rewards/margins: 0.0135
- Logps/rejected: -0.9978
- Logps/chosen: -0.7282
- Logits/rejected: -2.9263
- Logits/chosen: -2.9434
- Nll Loss: 0.4357
- Log Odds Ratio: -0.6093
- Log Odds Chosen: 0.4456

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7e-06
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- distributed_type: multi-GPU
- num_devices: 4
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- total_eval_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: inverse_sqrt
- lr_scheduler_warmup_steps: 100
- num_epochs: 1

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen | Nll Loss | Log Odds Ratio | Log Odds Chosen |
|:-------------:|:------:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|:--------:|:--------------:|:---------------:|
| 0.5226        | 0.1049 | 100  | 0.5280          | -0.0386        | -0.0472          | 0.6329             | 0.0086          | -0.9448        | -0.7728      | -2.7583         | -2.7860       | 0.4953   | -0.6326        | 0.2873          |
| 0.5074        | 0.2098 | 200  | 0.5134          | -0.0381        | -0.0478          | 0.6409             | 0.0098          | -0.9566        | -0.7612      | -2.6736         | -2.7002       | 0.4774   | -0.6357        | 0.3190          |
| 0.5265        | 0.3146 | 300  | 0.5012          | -0.0379        | -0.0479          | 0.6329             | 0.0099          | -0.9572        | -0.7588      | -2.7317         | -2.7594       | 0.4653   | -0.6374        | 0.3278          |
| 0.5194        | 0.4195 | 400  | 0.4912          | -0.0371        | -0.0478          | 0.6429             | 0.0107          | -0.9559        | -0.7417      | -2.6640         | -2.6974       | 0.4560   | -0.6284        | 0.3607          |
| 0.5008        | 0.5244 | 500  | 0.4847          | -0.0373        | -0.0489          | 0.6508             | 0.0117          | -0.9786        | -0.7455      | -2.5957         | -2.6294       | 0.4499   | -0.6209        | 0.3873          |
| 0.4725        | 0.6293 | 600  | 0.4794          | -0.0362        | -0.0470          | 0.6349             | 0.0107          | -0.9394        | -0.7248      | -2.6147         | -2.6477       | 0.4435   | -0.6320        | 0.3567          |
| 0.4875        | 0.7341 | 700  | 0.4767          | -0.0368        | -0.0498          | 0.6409             | 0.0129          | -0.9955        | -0.7365      | -2.6910         | -2.7213       | 0.4416   | -0.6158        | 0.4180          |
| 0.4796        | 0.8390 | 800  | 0.4740          | -0.0371        | -0.0508          | 0.6508             | 0.0137          | -1.0162        | -0.7416      | -2.7913         | -2.8114       | 0.4396   | -0.6169        | 0.4363          |
| 0.4851        | 0.9439 | 900  | 0.4714          | -0.0357        | -0.0466          | 0.6528             | 0.0109          | -0.9324        | -0.7143      | -2.9543         | -2.9692       | 0.4361   | -0.6245        | 0.3669          |


### Framework versions

- Transformers 4.41.0.dev0
- Pytorch 2.3.0+cu121
- Datasets 2.19.1
- Tokenizers 0.19.1
