

# NeuralLLaMa-3-8b-ORPO-v0.3

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64d71ab4089bc502ceb44d29/JyQNE7gAAyYTxKMO2PraO.png)



```python
!pip install -qU transformers accelerate bitsandbytes

from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer, BitsAndBytesConfig
import torch

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

MODEL_NAME = 'Kukedlc/NeuralLLaMa-3-8b-ORPO-v0.3'
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map='cuda:0', quantization_config=bnb_config)

prompt_system = "Sos un modelo de lenguaje de avanzada que habla español de manera fluida, clara y precisa.\
Te llamas Roberto el Robot y sos un aspirante a artista post moderno"
prompt = "Creame una obra de arte que represente tu imagen de como te ves vos roberto como un LLm de avanzada, con arte ascii, mezcla diagramas, ingenieria y dejate llevar"
chat = [
    {"role": "system", "content": f"{prompt_system}"},
    {"role": "user", "content": f"{prompt}"},
]

chat = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(chat, return_tensors="pt").to('cuda')
streamer = TextStreamer(tokenizer)
_ = model.generate(**inputs, streamer=streamer, max_new_tokens=1024, do_sample=True, temperature=0.3, repetition_penalty=1.2, top_p=0.9,)
```

# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Kukedlc__NeuralLLaMa-3-8b-ORPO-v0.3)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |72.66|
|AI2 Reasoning Challenge (25-Shot)|69.54|
|HellaSwag (10-Shot)              |84.90|
|MMLU (5-Shot)                    |68.39|
|TruthfulQA (0-shot)              |60.82|
|Winogrande (5-shot)              |79.40|
|GSM8k (5-shot)                   |72.93|