
<div align="center">
  <img src="https://raw.githubusercontent.com/imoneoi/openchat/master/assets/logo_new.png" style="width: 65%">
  <h1>Advancing Open-source Language Models with Mixed-Quality Data</h1>
</div>

<p align="center" style="margin-top: 0px;">
  <a href="https://openchat.team">
    <img src="https://github.com/alpayariyak/openchat/blob/master/assets/logo_nobg.png?raw=true" alt="OpenChat Logo" style="width:20px; vertical-align: middle; display: inline-block; margin-right: 5px; margin-left: 10px; margin-top: 0px; margin-bottom: 0px;"/>
    <span class="link-text" style=" margin-right: 5px;">Online Demo</span>
  </a> |
  <a href="https://github.com/imoneoi/openchat">
    <img src="https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png" alt="GitHub Logo" style="width:20px; vertical-align: middle; display: inline-block; margin-right: 5px; margin-left: 5px; margin-top: 0px; margin-bottom: 0px;"/>
    <span class="link-text" style=" margin-right: 5px;">GitHub</span>
  </a> |
  <a href="https://arxiv.org/pdf/2309.11235.pdf">
    <img src="https://github.com/alpayariyak/openchat/blob/master/assets/arxiv-logomark-small-square-border.png?raw=true" alt="ArXiv Logo" style="width:20px; vertical-align: middle; display: inline-block; margin-right: 5px; margin-left: 5px; margin-top: 0px; margin-bottom: 0px;"/>
    <span class="link-text" style="margin-right: 5px;">Paper</span>
  </a> |
  <a href="https://discord.gg/pQjnXvNKHY">
    <img src="https://cloud.githubusercontent.com/assets/6291467/26705903/96c2d66e-477c-11e7-9f4e-f3c0efe96c9a.png" alt="Discord Logo" style="width:20px; vertical-align: middle; display: inline-block; margin-right: 5px; margin-left: 5px; margin-top: 0px; margin-bottom: 0px;"/>
    <span class="link-text">Discord</span>
  </a>
</p>

<p align="center" style="margin-top: 0px;">
    <span class="link-text" style=" margin-right: 0px; font-size: 0.8em">Sponsored by RunPod</span>
   <img src="https://styles.redditmedia.com/t5_6075m3/styles/profileIcon_71syco7c5lt81.png?width=256&height=256&frame=1&auto=webp&crop=256:256,smart&s=24bd3c71dc11edc5d4f88d0cbc1da72ed7ae1969" alt="RunPod Logo" style="width:30px; vertical-align: middle; display: inline-block; margin-right: 5px; margin-left: 5px; margin-top: 0px; margin-bottom: 0px;"/>
</p>

<div style="background-color: white; padding: 0.7em; border-radius: 0.5em; color: black; display: flex; flex-direction: column; justify-content: center; text-align: center">
  <a href="https://huggingface.co/openchat/openchat-3.5-0106" style="text-decoration: none; color: black;">
    <span style="font-size: 1.7em; font-family: 'Helvetica'; letter-spacing: 0.1em; font-weight: bold; color: black;">Llama 3 Version: OPENCHAT</span><span style="font-size: 1.8em; font-family: 'Helvetica'; color: #3c72db; ">3.6</span>
        <span style="font-size: 1.0em;  font-family: 'Helvetica'; color:  white; background-color: #90e0ef; vertical-align: top; border-radius: 6em; padding: 0.066em 0.4em; letter-spacing: 0.1em; font-weight: bold;">20240522</span>
    <span style="font-size: 0.85em; font-family: 'Helvetica'; color: black;">
      <br> 🏆 The Overall Best Performing Open-source 8B Model 🏆
      <br> 🚀 Outperforms Llama-3-8B-Instruct and open-source finetunes/merges 🚀
    </span>
  </a>
</div>

<div style="display: flex; justify-content: center; align-items: center; width: 110%; margin-left: -5%;">
  <img src="https://raw.githubusercontent.com/imoneoi/openchat/master/assets/benchmarks-openchat-3.6-20240522.svg" style="width: 100%; border-radius: 1em">
</div>

<div style="display: flex; justify-content: center; align-items: center">
  <p>* Llama-3-Instruct often fails to follow the few-shot templates. See <a href="https://huggingface.co/openchat/openchat-3.6-8b-20240522/discussions/6">example</a>.</p>
</div>

<div align="center">
<h2> Usage </h2>
</div>

To use this model, we highly recommend installing the OpenChat package by following the [installation guide](https://github.com/imoneoi/openchat#installation) in our repository and using the OpenChat OpenAI-compatible API server by running the serving command from the table below. The server is optimized for high-throughput deployment using [vLLM](https://github.com/vllm-project/vllm) and can run on a consumer GPU with 24GB RAM. To enable tensor parallelism, append `--tensor-parallel-size N` to the serving command.

Once started, the server listens at `localhost:18888` for requests and is compatible with the [OpenAI ChatCompletion API specifications](https://platform.openai.com/docs/api-reference/chat). Please refer to the example request below for reference. Additionally, you can use the [OpenChat Web UI](https://github.com/imoneoi/openchat#web-ui) for a user-friendly experience.

If you want to deploy the server as an online service, you can use `--api-keys sk-KEY1 sk-KEY2 ...` to specify allowed API keys and `--disable-log-requests --disable-log-stats --log-file openchat.log` for logging only to a file. For security purposes, we recommend using an [HTTPS gateway](https://fastapi.tiangolo.com/es/deployment/concepts/#security-https) in front of the server.

| Model                 | Size | Context | Weights                                                                 | Serving                                                                               |
|-----------------------|------|---------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| OpenChat-3.6-20240522 | 8B   | 8192    | [Huggingface](https://huggingface.co/openchat/openchat-3.6-8b-20240522) | `python -m ochat.serving.openai_api_server --model openchat/openchat-3.6-8b-20240522` |

<details>
  <summary>Example request (click to expand)</summary>

```bash
curl http://localhost:18888/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openchat_3.6",
    "messages": [{"role": "user", "content": "You are a large language model named OpenChat. Write a poem to describe yourself"}]
  }'
```

</details>

### Conversation templates

💡 **Default Mode**: Best for coding, chat and general tasks.

It's a modified version of the Llama 3 Instruct template, the only difference is role names, which are either `GPT4 Correct User` or `GPT4 Correct Assistant`

```
<|start_header_id|>GPT4 Correct User<|end_header_id|>\n\nHello<|eot_id|><|start_header_id|>GPT4 Correct Assistant<|end_header_id|>\n\nHi<|eot_id|><|start_header_id|>GPT4 Correct User<|end_header_id|>\n\nHow are you today?<|eot_id|><|start_header_id|>GPT4 Correct Assistant<|end_header_id|>\n\n
```

⚠️ **Notice:** Remember to set `<|eot_id|>` as end of generation token.

The default template is also available as the integrated `tokenizer.chat_template`, which can be used instead of manually specifying the template:

```python
messages = [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi"},
    {"role": "user", "content": "How are you today?"}
]
tokens = tokenizer.apply_chat_template(messages, add_generation_prompt=True)
```

## Inference using Transformers

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "openchat/openchat-3.6-8b-20240522"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=torch.bfloat16, device_map="auto")

messages = [
    {"role": "user", "content": "Explain how large language models work in detail."},
]
input_ids = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)

outputs = model.generate(input_ids,
    do_sample=True,
    temperature=0.5,
    max_new_tokens=1024
)
response = outputs[0][input_ids.shape[-1]:]
print(tokenizer.decode(response, skip_special_tokens=True))
```

<div align="center">
<h2> Limitations </h2>
</div>

**Foundation Model Limitations**
Despite its advanced capabilities, OpenChat is still bound by the limitations inherent in its foundation models. These limitations may impact the model's performance in areas such as:

- Complex reasoning
- Mathematical and arithmetic tasks
- Programming and coding challenges

**Hallucination of Non-existent Information**
OpenChat may sometimes generate information that does not exist or is not accurate, also known as "hallucination". Users should be aware of this possibility and verify any critical information obtained from the model.

**Safety**
OpenChat may sometimes generate harmful, hate speech, biased responses, or answer unsafe questions. It's crucial to apply additional AI safety measures in use cases that require safe and moderated responses.

<div align="center">
<h2> 💌 Contact </h2>
</div>

We look forward to hearing from you and collaborating on this exciting project!

**Project Lead:**
- Guan Wang [imonenext at gmail dot com]
- [Alpay Ariyak](https://github.com/alpayariyak) [aariyak at wpi dot edu]

<div align="center">
<h2> Citation </h2>
</div>

```
@article{wang2023openchat,
  title={OpenChat: Advancing Open-source Language Models with Mixed-Quality Data},
  author={Wang, Guan and Cheng, Sijie and Zhan, Xianyuan and Li, Xiangang and Song, Sen and Liu, Yang},
  journal={arXiv preprint arXiv:2309.11235},
  year={2023}
}
```