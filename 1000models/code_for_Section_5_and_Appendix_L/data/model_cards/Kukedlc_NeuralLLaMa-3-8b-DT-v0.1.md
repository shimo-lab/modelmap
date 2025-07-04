
# NeuralLLaMa-3-8b-DT-v0.1



![image/png](https://cdn-uploads.huggingface.co/production/uploads/64d71ab4089bc502ceb44d29/tK72e9RGnYyBVRy0T_Kba.png)

NeuralLLaMa-3-8b-DT-v0.1 is a merge of the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):
* [mlabonne/ChimeraLlama-3-8B-v2](https://huggingface.co/mlabonne/ChimeraLlama-3-8B-v2)
* [nbeerbower/llama-3-stella-8B](https://huggingface.co/nbeerbower/llama-3-stella-8B)
* [uygarkurt/llama-3-merged-linear](https://huggingface.co/uygarkurt/llama-3-merged-linear)


## 🧩 Configuration

```yaml
models:
  - model: NousResearch/Meta-Llama-3-8B
    # No parameters necessary for base model
  - model: mlabonne/ChimeraLlama-3-8B-v2
    parameters:
      density: 0.33
      weight: 0.2
  - model: nbeerbower/llama-3-stella-8B
    parameters:
      density: 0.44
      weight: 0.4
  - model: uygarkurt/llama-3-merged-linear
    parameters:
      density: 0.55
      weight: 0.4
merge_method: dare_ties
base_model: NousResearch/Meta-Llama-3-8B
parameters:
  int8_mask: true
dtype: float16
```
## 🗨️ Chats

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64d71ab4089bc502ceb44d29/Uk89jeeRZ3Zh3wNBm6dXk.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64d71ab4089bc502ceb44d29/feYEkbM_TqeahAMOoiGoG.png)

## 💻 Usage

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

MODEL_NAME = 'Kukedlc/NeuralLLaMa-3-8b-DT-v0.1'
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map='cuda:0', quantization_config=bnb_config)

prompt_system = "You are an advanced language model that speaks Spanish fluently, clearly, and precisely.\
You are called Roberto the Robot and you are an aspiring post-modern artist."
prompt = "Create a piece of art that represents how you see yourself, Roberto, as an advanced LLm, with ASCII art, mixing diagrams, engineering and let yourself go."

chat = [
    {"role": "system", "content": f"{prompt_system}"},
    {"role": "user", "content": f"{prompt}"},
]

chat = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(chat, return_tensors="pt").to('cuda')
streamer = TextStreamer(tokenizer)
stop_token = "<|eot_id|>"
stop = tokenizer.encode(stop_token)[0]

_ = model.generate(**inputs, streamer=streamer, max_new_tokens=1024, do_sample=True, temperature=0.7, repetition_penalty=1.2, top_p=0.9, eos_token_id=stop)
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)

Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Kukedlc__NeuralLLaMa-3-8b-DT-v0.1)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |21.12|
|IFEval (0-Shot)    |43.71|
|BBH (3-Shot)       |28.01|
|MATH Lvl 5 (4-Shot)| 7.25|
|GPQA (0-shot)      | 7.05|
|MuSR (0-shot)      | 9.69|
|MMLU-PRO (5-shot)  |31.02|

