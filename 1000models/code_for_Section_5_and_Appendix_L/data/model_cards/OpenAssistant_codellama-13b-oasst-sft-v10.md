# Open-Assistant CodeLlama 13B SFT v10

This model is an Open-Assistant fine-tuning of Meta's CodeLlama 13B LLM.

**Note**: Due to the new RoPE Theta value (1e6 instead of 1e4), for correct results you must load this model with `trust_remote_code=True` or use the latest main branch of Huggingface transformers (until version 4.33 is released).

## Model Details

- **Finetuned from:** [codellama/CodeLlama-7b-hf](https://huggingface.co/codellama/CodeLlama-7b-hf) via [epfLLM/Megatron-LLM](https://github.com/epfLLM/Megatron-LLM)
- **Model type:** Causal decoder-only transformer language model
- **Language:** English
- **Weights & Biases training logs:** 6123 steps, BS 64 [run56_oa_llamacode](https://wandb.ai/open-assistant/public-sft/runs/run56_oa_llamacode) 
- **Demo:** [Continuations for 250 random prompts (without system message)](https://open-assistant.github.io/oasst-model-eval/?f=https%3A%2F%2Fraw.githubusercontent.com%2FOpen-Assistant%2Foasst-model-eval%2Fmain%2Fsampling_reports%2Foasst-sft%2F2023-08-26_OpenAssistant_codellama-13b-oasst-sft-v10_sampling_noprefix2.json)
- **License:** [LLAMA 2 COMMUNITY LICENSE AGREEMENT](https://huggingface.co/meta-llama/Llama-2-70b/raw/main/LICENSE.txt)
- **Contact:** [Open-Assistant Discord](https://ykilcher.com/open-assistant-discord)

## Prompting / Prompt Template

Due to public demand (see [survey](https://twitter.com/erhartford/status/1682403597525430272)) we changed the prompt-template for this model from custom prompter/assistant tokens to OpenAI's [chatml](https://github.com/openai/openai-python/blob/main/chatml.md) standard prompt format.
We hope that this leads to greater compatibility with chat inference/frontend applications.

Prompt dialogue template:

```
"""
<|im_start|>system
{system_message}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
"""
```

The model input can contain multiple conversation turns between user and assistant, e.g.
```
<|im_start|>user
{prompt 1}<|im_end|>
<|im_start|>assistant
{reply 1}<|im_end|>
<|im_start|>user
{prompt 2}<|im_end|>
<|im_start|>assistant
(...)
```

The model was partly trained with orca system messages.  
For inference we recommend to use the official [Llama2 system message](https://github.com/facebookresearch/llama/blob/ea9f33d6d3ea8ed7d560d270986407fd6c2e52b7/example_chat_completion.py#L57-L61):
```
<|im_start|>system
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
<|im_end|>
```

### Credits & Special Thanks

- Thanks to [Meta AI](https://ai.meta.com/) for training and releasing the CodeLLlama model.
- Distributed training support was provided by EPFL's [Machine Learning and Optimization Laboratory](https://www.epfl.ch/labs/mlo/), and [Natural Language Processing Lab](https://nlp.epfl.ch/).
- The open-source [epfLLM/Megatron-LLM](https://github.com/epfLLM/Megatron-LLM) trainer was used for fine-tuning.
- [rombodawg](https://huggingface.co/rombodawg) curated the [LosslessMegaCodeTrainingV2_1m_Evol_Uncensored](https://huggingface.co/datasets/rombodawg/LosslessMegaCodeTrainingV2_1m_Evol_Uncensored) dataset.
- [ehartford](https://huggingface.co/ehartford) generated and published the [ehartford/dolphin](https://huggingface.co/datasets/ehartford/dolphin).
- [shahules786](https://github.com/shahules786) de-duped and filtered the Dolphin and Megacode dataset with a clustering/controid approach and generated orca-best & bestofmegacode.
- [andreaskoepf](https://github.com/andreaskoepf/) prepared & orchestrated the training.

## Ethical Considerations and Limitations

Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. 
For these reasons, as with all LLMs, the potential outputs of codellama-13b-oasst-sft-v10 cannot be predicted
in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses
to user prompts. Therefore, before deploying any applications of codellama-13b-oasst-sft-v10, developers should
perform safety testing and tuning tailored to their specific applications of the model.

Please see Meta's [Responsible Use Guide](https://ai.meta.com/llama/responsible-use-guide/).

## Configuration Details

The "pretokenizer" utility used to tokenize the datamix is part of the Open-Assistant github repository and can be found here: [model/pretokenizer](https://github.com/LAION-AI/Open-Assistant/tree/main/model/pretokenizer).


### Pretokenizer Configuration


```
orca_megacode_oasst_best:
  datasets:
    - orca-chat:
        val_split: 0.01
        max_val_set: 1000
    - bestofmegacode:
        val_split: 0.01
        max_val_set: 1000
    - oasst_export:
        lang: "bg,ca,cs,da,de,en,es,fr,hr,hu,it,nl,pl,pt,ro,ru,sl,sr,sv,uk"
        #hf_dataset_name: OpenAssistant/oasst1
        input_file_path: 2023-08-25_oasst_ready.jsonl.gz
        top_k: 1
        val_split: 0.025
  output_dir: "output/orca_megacode_oasst_best"
  filename_prefix: "orca_megacode_oasst_best"
  min_assistant_tokens: 1
```

