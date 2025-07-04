# h2oGPT Model Card
## Summary

H2O.ai's `h2ogpt-oasst1-512-12b` is a 12 billion parameter instruction-following large language model licensed for commercial use.

- Base model: [EleutherAI/pythia-12b](https://huggingface.co/EleutherAI/pythia-12b)
- Fine-tuning dataset: [h2oai/openassistant_oasst1_h2ogpt_graded](https://huggingface.co/datasets/h2oai/openassistant_oasst1_h2ogpt_graded)
- Data-prep and fine-tuning code: [H2O.ai GitHub](https://github.com/h2oai/h2ogpt)
- Training logs: [zip](https://huggingface.co/h2oai/h2ogpt-oasst1-512-12b/blob/main/pythia-12b-deduped.h2oaiopenassistant_oasst1_h2ogpt_graded.3_epochs.2ccf687ea3f3f3775a501838e81c1a0066430455.4.zip)

## Chatbot

- Run your own chatbot: [H2O.ai GitHub](https://github.com/h2oai/h2ogpt)
[![H2O.ai GitHub](https://user-images.githubusercontent.com/6147661/232930822-e7170e4d-8aa1-4f7a-ad70-ece9cdd8b0cb.png)](https://github.com/h2oai/h2ogpt)

## Usage

To use the model with the `transformers` library on a machine with GPUs, first make sure you have the `transformers` and `accelerate` libraries installed.

```bash
pip install transformers==4.28.1
pip install accelerate==0.18.0
```

```python
import torch
from transformers import pipeline

generate_text = pipeline(model="h2oai/h2ogpt-oasst1-512-12b", torch_dtype=torch.bfloat16, trust_remote_code=True, device_map="auto", prompt_type='human_bot')

res = generate_text("Why is drinking water so healthy?", max_new_tokens=100)
print(res[0]["generated_text"])
```

Alternatively, if you prefer to not use `trust_remote_code=True` you can download [instruct_pipeline.py](https://huggingface.co/h2oai/h2ogpt-oasst1-512-12b/blob/main/h2oai_pipeline.py),
store it alongside your notebook, and construct the pipeline yourself from the loaded model and tokenizer:

```python
import torch
from h2oai_pipeline import H2OTextGenerationPipeline
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("h2oai/h2ogpt-oasst1-512-12b", padding_side="left")
model = AutoModelForCausalLM.from_pretrained("h2oai/h2ogpt-oasst1-512-12b", torch_dtype=torch.bfloat16, device_map="auto")
generate_text = H2OTextGenerationPipeline(model=model, tokenizer=tokenizer, prompt_type='human_bot')

res = generate_text("Why is drinking water so healthy?", max_new_tokens=100)
print(res[0]["generated_text"])
```

## Model Architecture

```
GPTNeoXForCausalLM(
  (gpt_neox): GPTNeoXModel(
    (embed_in): Embedding(50688, 5120)
    (layers): ModuleList(
      (0-35): 36 x GPTNeoXLayer(
        (input_layernorm): LayerNorm((5120,), eps=1e-05, elementwise_affine=True)
        (post_attention_layernorm): LayerNorm((5120,), eps=1e-05, elementwise_affine=True)
        (attention): GPTNeoXAttention(
          (rotary_emb): RotaryEmbedding()
          (query_key_value): Linear(in_features=5120, out_features=15360, bias=True)
          (dense): Linear(in_features=5120, out_features=5120, bias=True)
        )
        (mlp): GPTNeoXMLP(
          (dense_h_to_4h): Linear(in_features=5120, out_features=20480, bias=True)
          (dense_4h_to_h): Linear(in_features=20480, out_features=5120, bias=True)
          (act): GELUActivation()
        )
      )
    )
    (final_layer_norm): LayerNorm((5120,), eps=1e-05, elementwise_affine=True)
  )
  (embed_out): Linear(in_features=5120, out_features=50688, bias=False)
)
```

## Model Configuration

```json
GPTNeoXConfig {
  "_name_or_path": "h2oai/h2ogpt-oasst1-512-12b",
  "architectures": [
    "GPTNeoXForCausalLM"
  ],
  "bos_token_id": 0,
  "classifier_dropout": 0.1,
  "custom_pipelines": {
    "text-generation": {
      "impl": "h2oai_pipeline.H2OTextGenerationPipeline",
      "pt": "AutoModelForCausalLM"
    }
  },
  "eos_token_id": 0,
  "hidden_act": "gelu",
  "hidden_size": 5120,
  "initializer_range": 0.02,
  "intermediate_size": 20480,
  "layer_norm_eps": 1e-05,
  "max_position_embeddings": 2048,
  "model_type": "gpt_neox",
  "num_attention_heads": 40,
  "num_hidden_layers": 36,
  "rotary_emb_base": 10000,
  "rotary_pct": 0.25,
  "tie_word_embeddings": false,
  "torch_dtype": "float16",
  "transformers_version": "4.30.0.dev0",
  "use_cache": true,
  "use_parallel_residual": true,
  "vocab_size": 50688
}

```

## Model Validation

Model validation results using [EleutherAI lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness).


[eval source code](https://github.com/h2oai/h2ogpt/issues/125#issuecomment-1548239108)

|    Task     |Version| Metric |Value |   |Stderr|
|-------------|------:|--------|-----:|---|-----:|
|arc_challenge|      0|acc     |0.3157|±  |0.0136|
|             |       |acc_norm|0.3507|±  |0.0139|
|arc_easy     |      0|acc     |0.6932|±  |0.0095|
|             |       |acc_norm|0.6225|±  |0.0099|
|boolq        |      1|acc     |0.6685|±  |0.0082|
|hellaswag    |      0|acc     |0.5140|±  |0.0050|
|             |       |acc_norm|0.6803|±  |0.0047|
|openbookqa   |      0|acc     |0.2900|±  |0.0203|
|             |       |acc_norm|0.3740|±  |0.0217|
|piqa         |      0|acc     |0.7682|±  |0.0098|
|             |       |acc_norm|0.7661|±  |0.0099|
|winogrande   |      0|acc     |0.6369|±  |0.0135|


## Disclaimer

Please read this disclaimer carefully before using the large language model provided in this repository. Your use of the model signifies your agreement to the following terms and conditions.

- Biases and Offensiveness: The large language model is trained on a diverse range of internet text data, which may contain biased, racist, offensive, or otherwise inappropriate content. By using this model, you acknowledge and accept that the generated content may sometimes exhibit biases or produce content that is offensive or inappropriate. The developers of this repository do not endorse, support, or promote any such content or viewpoints.
- Limitations: The large language model is an AI-based tool and not a human. It may produce incorrect, nonsensical, or irrelevant responses. It is the user's responsibility to critically evaluate the generated content and use it at their discretion.
- Use at Your Own Risk: Users of this large language model must assume full responsibility for any consequences that may arise from their use of the tool. The developers and contributors of this repository shall not be held liable for any damages, losses, or harm resulting from the use or misuse of the provided model.
- Ethical Considerations: Users are encouraged to use the large language model responsibly and ethically. By using this model, you agree not to use it for purposes that promote hate speech, discrimination, harassment, or any form of illegal or harmful activities.
- Reporting Issues: If you encounter any biased, offensive, or otherwise inappropriate content generated by the large language model, please report it to the repository maintainers through the provided channels. Your feedback will help improve the model and mitigate potential issues.
- Changes to this Disclaimer: The developers of this repository reserve the right to modify or update this disclaimer at any time without prior notice. It is the user's responsibility to periodically review the disclaimer to stay informed about any changes.

By using the large language model provided in this repository, you agree to accept and comply with the terms and conditions outlined in this disclaimer. If you do not agree with any part of this disclaimer, you should refrain from using the model and any content generated by it.
