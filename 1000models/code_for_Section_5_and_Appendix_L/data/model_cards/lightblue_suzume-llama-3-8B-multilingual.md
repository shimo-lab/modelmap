
<p align="center">
  <img width=400 src="https://cdn-uploads.huggingface.co/production/uploads/64b63f8ad57e02621dc93c8b/kg3QjQOde0X743csGJT-f.png" alt="Suzume - a Japanese tree sparrow"/>
</p>

# Suzume

[[Paper](https://arxiv.org/abs/2405.12612)] [[Dataset](https://huggingface.co/datasets/lightblue/tagengo-gpt4)]

This Suzume 8B, a multilingual finetune of Llama 3 ([meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)).

Llama 3 has exhibited excellent performance on many English language benchmarks. 
However, it also seemingly been finetuned on mostly English data, meaning that it will respond in English, even if prompted in other languages.

We have fine-tuned Llama 3 on almost 90,000 multilingual conversations meaning that this model has the smarts of Llama 3 but has the added ability to chat in more languages.

Please feel free to comment on this model and give us feedback in the Community tab!

We will release a paper in the future describing how we made the training data, the model, and the evaluations we have conducted of it.

# How to use

The easiest way to use this model on your own computer is to use the [GGUF version of this model (lightblue/suzume-llama-3-8B-multilingual-gguf)](https://huggingface.co/lightblue/suzume-llama-3-8B-multilingual-gguf) using a program such as [jan.ai](https://jan.ai/) or [LM Studio](https://lmstudio.ai/).

If you want to use this model directly in Python, we recommend using vLLM for the fastest inference speeds.

```python
from vllm import LLM, SamplingParams

sampling_params = SamplingParams(temperature=0.0, max_tokens=100)
llm = LLM(model="lightblue/suzume-llama-3-8B-multilingual")

messages = []
messages.append({"role": "user", "content": "Bonjour!"})
prompt = llm.llm_engine.tokenizer.tokenizer.apply_chat_template(conversation=messages, add_generation_prompt=True, tokenize=False)
prompts = [prompt]

outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

# Evaluation scores

We achieve the following MT-Bench scores across 6 languages:

|                 | **meta-llama/Meta-Llama-3-8B-Instruct** | **lightblue/suzume-llama-3-8B-multilingual** | **Nexusflow/Starling-LM-7B-beta** | **gpt-3.5-turbo** |
|-----------------|-----------------------------------------|----------------------------------------------|-----------------------------------|-------------------|
| **German** 🇩🇪   | NaN                                     | 7.26                                         | 6.99                              | 7.68              |
| **French** 🇫🇷   | NaN                                     | 7.66                                         | 7.29                              | 7.74              |
| **Japanese** 🇯🇵 | NaN                                     | 6.56                                         | 6.22                              | 7.84              |
| **Russian** 🇷🇺 * | NaN                                     | 8.19                                         | 8.28                              | 7.94              |
| **Chinese** 🇨🇳  | NaN                                     | 7.11                                         | 6.97                              | 7.55              |
| **English** 🇺🇸  | 7.98                                    | 7.73                                         | 7.92                              | 8.26              |

\* (Note the Russian scores exclude code, reasoning and math problems due to not having any translated reference answers for these questions.)

We observe minimal degredation of Llama 3's English ability while achieving best-in-class multilingual abilities compared to the top rated 7B model ([Nexusflow/Starling-LM-7B-beta](https://huggingface.co/Nexusflow/Starling-LM-7B-beta)) on the [Chatbot Arena Leaderboard](https://chat.lmsys.org/?leaderboard).

[Here is our evaluation script.](https://drive.google.com/file/d/15HPn7452t8LbTD9HKSl7ngYYWnsoOG08/view?usp=sharing)


# Training data

We train on three sources of data to create this model:

* [lightblue/tagengo-gpt4](https://huggingface.co/datasets/lightblue/tagengo-gpt4) - 76,338 conversations
    * A diverse dataset of initial inputs sampled from [lmsys/lmsys-chat-1m](https://huggingface.co/datasets/lmsys/lmsys-chat-1m) and then used to prompt `gpt-4-0125-preview`
* [megagonlabs/instruction_ja](https://github.com/megagonlabs/instruction_ja) - 669 conversations
    * A hand-edited dataset of nearly 700 Japanese conversations taken originally from translations of the [kunishou/hh-rlhf-49k-ja](https://huggingface.co/datasets/kunishou/hh-rlhf-49k-ja) dataset.
* [openchat/openchat_sharegpt4_dataset](https://huggingface.co/datasets/openchat/openchat_sharegpt4_dataset/resolve/main/sharegpt_gpt4.json) - 6,206 conversations
    * Multilingual conversations of humans talking to GPT-4.


<details><summary>We prepare our data like so:</summary>

```python
import pandas as pd
from datasets import Dataset, load_dataset, concatenate_datasets

### Tagengo
gpt4_dataset = load_dataset("lightblue/tagengo-gpt4", split="train")
gpt4_dataset = gpt4_dataset.filter(lambda x: x["response"][1] == "stop")
####

### Megagon
megagon_df = pd.read_json(
    "https://raw.githubusercontent.com/megagonlabs/instruction_ja/main/data/data.jsonl",
    lines=True,
    orient="records"
    )
role_map = {"user": "human", "agent": "gpt"}
megagon_df["conversations"] = megagon_df.utterances.apply(lambda x: [{"from": role_map[y["name"]], "value": y["text"]} for y in x])
megagon_df["language"] = "Japanese"
megagon_df = megagon_df[["conversations", "language"]]
megagon_dataset = Dataset.from_pandas(df)
###

### Openchat
openchat_df = pd.read_json("https://huggingface.co/datasets/openchat/openchat_sharegpt4_dataset/resolve/main/sharegpt_gpt4.json?download=true")
openchat_df["conversations"] = openchat_df["items"]
openchat_dataset = Dataset.from_pandas(openchat_df)
###


dataset = concatenate_datasets([gpt4_dataset, megagon_dataset, openchat_dataset])
dataset = dataset.filter(lambda x: not any([y["value"] is None for y in x["conversations"]]))
dataset.select_columns(["conversations"]).to_json("/workspace/llm_training/axolotl/llama3-multilingual/tagengo_openchat_megagon.json")
```

</details>
<br/>

# workspace/llm_training/axolotl/llama3-multilingual/output_tagengo_openchat_megagon_8B_llama3

This model is a fine-tuned version of [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) on the above described dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6595


## Training procedure

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
<details><summary>See axolotl config</summary>

axolotl version: `0.4.0`
```yaml
base_model: meta-llama/Meta-Llama-3-8B-Instruct
model_type: LlamaForCausalLM
tokenizer_type: AutoTokenizer  # PreTrainedTokenizerFast

load_in_8bit: false
load_in_4bit: false
strict: false

datasets:
  - path: /workspace/llm_training/axolotl/llama3-multilingual/tagengo_openchat_megagon.json
    ds_type: json # see other options below
    type: sharegpt
    conversation: llama-3
dataset_prepared_path: /workspace/llm_training/axolotl/llama3-multilingual/prepared_tagengo_openchat_megagon
val_set_size: 0.01
output_dir: /workspace/llm_training/axolotl/llama3-multilingual/output_tagengo_openchat_megagon_8B_llama3

sequence_len: 8192
sample_packing: true
pad_to_sequence_len: true

use_wandb: true
wandb_project: wandb_project
wandb_entity: wandb_entity
wandb_name: wandb_name

gradient_accumulation_steps: 2
micro_batch_size: 2
num_epochs: 1
optimizer: paged_adamw_8bit
lr_scheduler: cosine
learning_rate: 1e-5

train_on_inputs: false
group_by_length: false
bf16: auto
fp16:
tf32: false

gradient_checkpointing: true
gradient_checkpointing_kwargs:
  use_reentrant: false
early_stopping_patience:
resume_from_checkpoint:
logging_steps: 1
xformers_attention:
flash_attention: true

warmup_steps: 10
evals_per_epoch: 5
eval_table_size:
saves_per_epoch: 1
debug:
deepspeed: /workspace/axolotl/deepspeed_configs/zero2.json
weight_decay: 0.0
special_tokens:
  pad_token: <|end_of_text|>
```

</details><br>

<details><summary>Note - we added this Llama 3 template to fastchat directly as the Llama 3 chat template was not supported when we trained this model.</summary>
  
```python
from fastchat.conversation import Conversation
from fastchat.conversation import register_conv_template
from fastchat.conversation import SeparatorStyle

register_conv_template(
    Conversation(
        name="llama-3",
        system_template="<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n{system_message}",
        roles=("<|start_header_id|>user<|end_header_id|>\n", "<|start_header_id|>assistant<|end_header_id|>\n"),
        sep_style=SeparatorStyle.ADD_NEW_LINE_SINGLE,
        sep="<|eot_id|>",
        stop_token_ids=[128009],
        stop_str="<|eot_id|>",
    )
)
```

</details><br>


### Training hyperparameters

This model was trained using 4 x A100 (80GB) for roughly 2.5 hours.

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- distributed_type: multi-GPU
- num_devices: 4
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- total_eval_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 10
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.1894        | 0.0   | 1    | 1.0110          |
| 0.8493        | 0.2   | 73   | 0.7057          |
| 0.8047        | 0.4   | 146  | 0.6835          |
| 0.7644        | 0.6   | 219  | 0.6687          |
| 0.7528        | 0.8   | 292  | 0.6615          |
| 0.7794        | 1.0   | 365  | 0.6595          |


### Framework versions

- Transformers 4.38.2
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.0

# How to cite

Please cite [this paper](https://arxiv.org/abs/2405.12612) when referencing this model.

```tex
@article{devine2024tagengo,
  title={Tagengo: A Multilingual Chat Dataset},
  author={Devine, Peter},
  journal={arXiv preprint arXiv:2405.12612},
  year={2024}
}
```

# Developer

Peter Devine - ([ptrdvn](https://huggingface.co/ptrdvn))
