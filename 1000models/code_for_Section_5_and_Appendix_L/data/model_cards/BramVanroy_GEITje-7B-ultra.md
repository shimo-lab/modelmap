
<p align="center" style="margin:0;padding:0">
<img src="https://huggingface.co/BramVanroy/GEITje-7B-ultra/resolve/main/geitje-ultra-banner.png" alt="GEITje Ultra banner" width="800" style="margin-left:'auto' margin-right:'auto' display:'block'"/>
</p>

<div style="margin:auto; text-align:center">
<h1 style="margin-bottom: 0">GEITje 7B ultra</h1>
<em>A conversational model for Dutch, aligned through AI feedback.</em>
</div>

This model is a fine-tuned version of [BramVanroy/GEITje-7B-ultra-sft](https://huggingface.co/BramVanroy/GEITje-7B-ultra-sft) on a synthetic DPO dataset of around 56M tokens that was generated with gpt-4-turbo and [Rijgersberg/GEITje-7B-chat](https://huggingface.co/Rijgersberg/GEITje-7B-chat) for Dutch.

> [!TIP]
> 🚀 Looking for the fast GGUF version? You can find it, and how to use it with `ollama`, [here](https://huggingface.co/BramVanroy/GEITje-7B-ultra-GGUF). 🚀 

## Citation

If you use GEITje 7B Ultra (SFT) or any of its derivatives or quantizations, place cite the following paper:

```bibtex
@misc{vanroy2024geitje7bultraconversational,
      title={GEITje 7B Ultra: A Conversational Model for Dutch}, 
      author={Bram Vanroy},
      year={2024},
      eprint={2412.04092},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.04092}, 
}
```

## Model description

This is a Dutch instruction/chat model ultimately based on Mistral and aligned with AI feedback via DPO. It is a DPO continuation of the SFT trained [BramVanroy/GEITje-7B-ultra-sft](https://huggingface.co/BramVanroy/GEITje-7B-ultra-sft), which in turn is based on [Rijgersberg/GEITje-7B](https://huggingface.co/Rijgersberg/GEITje-7B), which in turn is based on Mistral 7B and further pretrained on Dutch data. In (rather naive) [benchmarks](https://huggingface.co/spaces/BramVanroy/open_dutch_llm_leaderboard) it outperforms all the original GEITje models on average (but barely). However, note that these benchmarks should be taken with a massive grain of salt (see the disclaimer below the benchmarks on that page). The best evaluation is to try the models and see for yourself.


## Usage

One-off:

```python
from transformers import pipeline, Conversation

# load_in_8bit: lower precision but saves a lot of GPU memory
# device_map=auto: loads the model across multiple GPUs
chatbot = pipeline("conversational", model="BramVanroy/GEITje-7B-ultra", model_kwargs={"load_in_8bit": True}, device_map="auto")

start_messages = [
    {"role": "system", "content": "Je bent een grappige chatbot die Bert heet. Je maakt vaak mopjes."},
    {"role": "user", "content": "Hallo, ik ben Bram. Ik wil vanavond graag een film kijken. Heb je enkele suggesties?"}
]
conversation = Conversation(start_messages)
conversation = chatbot(conversation)
response = conversation.messages[-1]["content"]
print(response)
```

Interactive conversation:

```python
from transformers import pipeline, Conversation

# load_in_8bit: lower precision but saves a lot of memory
# device_map=auto: loads the model across multiple GPUs
# attn_implementation: uses flash attention, if your device supports it - otherwise remove it
chatbot = pipeline("conversational", model="BramVanroy/GEITje-7B-ultra", model_kwargs={"load_in_8bit": True, "attn_implementation": "flash_attention_2"}, device_map="auto")

while (system_message := input("System message ('q' to quit): ")) != "q":
    start_messages = [
        {"role": "system", "content": system_message},
    ]
    conversation = Conversation(start_messages)
    while (user_input := input("User ('r' to reset): ")) != "r":
        conversation.add_user_input(user_input)
        conversation = chatbot(conversation)
        response = conversation.messages[-1]["content"]
        print("Assistant:", response)

```

## Intended uses & limitations

Although the model has been aligned with gpt-4-turbo output, which has strong content filters, the model could still generate wrong, misleading, and potentially even offensive content. Use at your own risk. 

Because the model was trained on synthetic data created with OpenAI/Azure services, this model cannot be used for commercial purposes.

## Training and evaluation data

The training data consists of a synthetic dataset based on [UltraFeedback binarized](https://huggingface.co/datasets/HuggingFaceH4/ultrafeedback_binarized) created with gpt-4-turbo and geitje-chat. A given prompt, translated from the original dataset, is given to the two models who then generated an answer. Then, gpt-4-turbo is always selected as the best answer which DPO will optimise for. While this is not completely fair, I did not have the budget to actually have gpt-4 rate both replies. Furthermore, while an impressive model, GEITje chat still seems behind gpt-4-turbo in the testing that I have done.

In total the dataset consists of 56,137,090 tokens (combination of prompt + rejected + chosen) and a test set of 6,178,969 tokens (11.00%). 

  
## Training procedure

The great [alignment handbook](https://github.com/huggingface/alignment-handbook/) was used for training, with a custom slurm script for compatibility with our cluster. It was trained in full, without LoRA or other adapters.

The model was trained in bfloat16 with flash attention 2 on two nodes of four A100 80GB each for around 11 hours. I thank the [Flemish Super Computer](https://www.vscentrum.be/compute) for their compute.

For conversational usage, the model relies on the Zephyr chat template, which is compatible with system messages. A small portion of the data of *-sft contained system messages, so it is assumed the model can handle system messages at least a little bit.

In earlier iterations I found that using the alignment handbook's defaults (beta=0.01) led to poor results (hallucinations of random tokens). After investigating, it seems that such a low beta does not work well for this dataset as it gives the model too much room to deviate from its initial base model. After a [hyperparameter search](https://huggingface.co/posts/BramVanroy/492522322273746) and manual analysis of the resulting metrics, I selected the current model as the best one, with a beta of 0.1.

Recipe used with the handbook:

```yaml
# Model arguments
model_name_or_path: BramVanroy/GEITje-7B-ultra-sft
model_revision: main
torch_dtype: bfloat16
use_flash_attention_2: true

# Data training arguments
# For definitions, see: src/h4/training/config.py
dataset_mixer:
  BramVanroy/ultra_feedback_dutch: 1.0
dataset_splits:
- train_prefs
- test_prefs
preprocessing_num_workers: 8

# DPOTrainer arguments
bf16: true
beta: 0.1
do_eval: true
evaluation_strategy: steps
eval_steps: 100
gradient_accumulation_steps: 4
gradient_checkpointing: true
gradient_checkpointing_kwargs:
  use_reentrant: False
hub_model_id: BramVanroy/GEITje-ultra
learning_rate: 5.0e-7
log_level: info
logging_steps: 10
lr_scheduler_type: cosine
max_length: 2048
max_prompt_length: 1536
num_train_epochs: 1
optim: adamw_torch
output_dir: data/GEITje-ultra
per_device_train_batch_size: 4
per_device_eval_batch_size: 4
push_to_hub: true
save_strategy: "steps"
save_steps: 100
save_total_limit: 3
seed: 42
warmup_ratio: 0.1
```

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-07
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- total_eval_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 1.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rewards/chosen | Rewards/rejected | Rewards/accuracies | Rewards/margins | Logps/rejected | Logps/chosen | Logits/rejected | Logits/chosen |
|:-------------:|:-----:|:----:|:---------------:|:--------------:|:----------------:|:------------------:|:---------------:|:--------------:|:------------:|:---------------:|:-------------:|
| 0.03          | 0.22  | 100  | 0.0260          | -0.9740        | -9.8635          | 0.9913             | 8.8895          | -524.8940      | -508.1891    | -3.0753         | -3.0315       |
| 0.0184        | 0.44  | 200  | 0.0164          | -1.7162        | -12.4772         | 0.9926             | 10.7610         | -551.0317      | -515.6115    | -3.0349         | -2.9873       |
| 0.0121        | 0.66  | 300  | 0.0142          | -2.0575        | -13.6818         | 0.9938             | 11.6244         | -563.0778      | -519.0242    | -3.0325         | -2.9835       |
| 0.0198        | 0.88  | 400  | 0.0139          | -2.1431        | -13.8857         | 0.9950             | 11.7426         | -565.1163      | -519.8801    | -3.0293         | -2.9801       |


### Framework versions

- Transformers 4.36.2
- Pytorch 2.1.2+cu121
- Datasets 2.14.6
- Tokenizers 0.15.0
 
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)

Results for the English Open LLM Leaderboard. For results specific to Dutch, check out [ScandEval](https://scandeval.com/dutch-nlg/).

Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_BramVanroy__GEITje-7B-ultra)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |10.91|
|IFEval (0-Shot)    |37.23|
|BBH (3-Shot)       |12.88|
|MATH Lvl 5 (4-Shot)| 0.91|
|GPQA (0-shot)      | 1.68|
|MuSR (0-shot)      | 1.52|
|MMLU-PRO (5-shot)  |11.24|