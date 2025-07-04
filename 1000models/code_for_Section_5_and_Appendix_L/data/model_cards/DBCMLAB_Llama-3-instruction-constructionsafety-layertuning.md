
# Model Card for Model ID

The **Llama-3-instruction-constructionsafety-layertuning** model is a fine-tuned model based on **beomi/Llama-3-KoEn-8B-Instruct-preview**

<!-- Provide a quick summary of what the model is/does. -->
## Model Details

**Llama-3-instruction-constructionsafety-layertuning**

Llama-3-instruction-constructionsafety-layertuning model is fine-tuned model based on beomi/Llama-3-KoEn-8B-Instruction-preview.

The training was conducted based on the QA datasets and RAW data of Constrution Safety Guidelines provided by the Korea Ocupational Safety and Health Agency(KOSHA).

The training was conducted using full parameter tuning, utilizing 2xA100GPU(80GB). Approximately 11,000 data were used for the training process.

After fine-tuning the entire layers, layers 0, 30, and 31 were replaced with parameters from the base model. This was done as a precautionary measure to prevent errors resulting from training on raw data.


## Simple Use


```
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_name = "DBCMLAB/Llama-3-instruction-constructionsafety-layertuning"
token = "your_access_token"
tuned_model = AutoModelForCausalLM.from_pretrained(
    model_name,
    token=access_token,
    torch_dtype="auto",
    device_map="auto",
)

tokenizer = AutoTokenizer.from_pretrained(model_name, token=access_token)

tokenizer.pad_token = tokenizer.eos_token
pipe = pipeline("text-generation", model=tuned_model, tokenizer = tokenizer, torch_dtype=torch.bfloat16, device_map="auto")

# We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
messages = [
    {
        "role": "system",
        "content": "친절한 건설안전전문가로서 상대방의 요청에 최대한 '자세하고' 친절하게 답하자. 모든 대답은 한국어(Korean)으로 대답해줘.",
    },
    {"role": "user", "content": "흙막이 가시설 공사시 작업자 안전조치에 대해서 10가지 정도 알려주세요."},
]
prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipe(prompt, max_new_tokens=1024, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])

```
### Output

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

친절한 건설안전전문가로서 상대방의 요청에 최대한 '자세하고' 친절하게 답하자. 모든 대답은 한국어(Korean)으로 대답해줘.<|eot_id|><|start_header_id|>user<|end_header_id|>

흙막이 가시설 공사시 작업자 안전조치에 대해서 10가지 정도 알려주세요.<|eot_id|><|start_header_id|>assistant<|end_header_id|>

1. 흙막이 공사 착공 전에 지하매설물의 유무를 확인하고 지하매설물을 보호하기 위한 조치를 취하여야 한다. 2. 흙막이 벽의 배면 지반 높이가 흙막이 벽 높이보다 낮은 경우, 지반의 붕괴를 방지하기 위한 필요한 조치를 취하여야 한다. 3. 흙막이 벽은 주변 지반 및 구조물의 균열을 방지하고, 인접 구조물에 영향을 미치지 않도록 설치하여야 한다. 4. 흙막이 공사 중 인접 구조물, 제3자의 권리 또는 이익을 침해하지 않도록 조치를 취하여야 한다. 5. 흙막이 공사 중 지하수위의 저하로 인하여 인접한 도로나 건축물 등에 영향을 미칠 우려가 있는 경우, 그 우려가 없도록 조치를 취하여야 한다. 6. 흙막이 공사 시 비상경보시설을 설치하여 응급상황에 대비하고, 안전교육을 실시하여야 한다. 7. 흙막이 공사 중 관계기관의 요구가 있는 경우, 그 요구에 따라 조치를 취하여야 한다. 8. 흙막이 공사 중 흙막이 벽의 기울기를 1/50 이상 1/30 이하로 유지하고, 수평으로 설치하는 흙막이의 경우에는 지반이 수평으로 유지되도록 하여야 한다. 9. 흙막이 공사 중 흙막이 벽에 작용하는 토압이 설계기준을 초과하지 않도록 하여야 한다. 10. 흙막이 공사 중 흙막이 벽의 무너짐을 방지하기 위하여 지반이 수평으로 유지되도록 하여야 한다.

```


### Training Data
Training Data will be provided upon requests.
<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->


## Citation instructions

**Llama-3-instruction-constructionsafety-layertuning**
```
@article{llama3cs-layertuning,
  title={Llama-3-instruction-constructionsafety-layertuning},
  author={L, Jungwon, A, Seungjun},
  year={2024},
  url={https://huggingface.co/DBCM/Llama-3-instruction-constructionsafety-layertuning}
}
```

**Llama-3-Open-Ko**
```
@article{llama3koen,
  title={Llama-3-KoEn},
  author={L, Junbum},
  year={2024},
  url={https://huggingface.co/beomi/Llama-3-KoEn-8B}
}
```

**Original Llama-3**
```
@article{llama3modelcard,
  title={Llama 3 Model Card},
  author={AI@Meta},
  year={2024},
  url = {https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md}
```