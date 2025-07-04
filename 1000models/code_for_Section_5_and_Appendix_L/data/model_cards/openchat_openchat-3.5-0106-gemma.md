
<div align="center">
  <a>
    <img src="https://cdn-uploads.huggingface.co/production/uploads/63972847b3e2256c9ce1307b/Ez9cDw8xstbTKlFtBgbVs.png" >
  </a>
</div>


## The highest performing Gemma model in the world. Trained with OpenChat's C-RLFT on openchat-3.5-0106 data. Achieving similar performance to Mistral-based openchat, and much better than Gemma-7b and Gemma-7b-it.

Please refer to [openchat-3.5-0106](https://huggingface.co/openchat/openchat-3.5-0106) for details.

> P.S.: 6T pre-training tokens + 0.003 init std dev + C-RLFT is the secret sauce?
>
> P.P.S.: @Google team, we know your model is great, but please use an OSI-approved license like Mistral (or even Phi and Orca).

## Benchmarks

| Model                       | # Params | Average  | MT-Bench | HumanEval | BBH MC   | AGIEval  | TruthfulQA | MMLU     | GSM8K    | BBH CoT  |
|-----------------------------|----------|----------|----------|-----------|----------|----------|------------|----------|----------|----------|
| **OpenChat-3.5-0106 Gemma** | **7B**   | 64.4     | 7.83     | 67.7      | **52.7** | **50.2** | 55.4       | 65.7     | **81.5** | 63.7     |
| OpenChat-3.5-0106 Mistral   | **7B**   | **64.5** | 7.8      | **71.3**  | 51.5     | 49.1     | **61.0**   | 65.8     | 77.4     | 62.2     |
| ChatGPT (March)             | ???B     | 61.5     | **7.94** | 48.1      | 47.6     | 47.1     | 57.7       | **67.3** | 74.9     | **70.1** |
|                             |          |          |          |           |          |          |            |          |          |          |
| Gemma-7B                    | 7B       | -        | -        | 32.3      | -        | 41.7     | -          | 64.3     | 46.4     | -        |
| Gemma-7B-it *               | 7B       | 25.4     | -        | 28.0      | 38.4     | 32.5     | 34.1       | 26.5     | 10.8     | 7.6      |
| OpenHermes 2.5              | 7B       | 59.3     | 7.54     | 48.2      | 49.4     | 46.5     | 57.5       | 63.8     | 73.5     | 59.9     |

*: `Gemma-7b-it` failed to understand and follow most few-shot templates.

## Usage

To use this model, we highly recommend installing the OpenChat package by following the [installation guide](https://github.com/imoneoi/openchat#installation) in our repository and using the OpenChat OpenAI-compatible API server by running the serving command from the table below. The server is optimized for high-throughput deployment using [vLLM](https://github.com/vllm-project/vllm) and can run on a consumer GPU with 24GB RAM. To enable tensor parallelism, append `--tensor-parallel-size N` to the serving command.

Once started, the server listens at `localhost:18888` for requests and is compatible with the [OpenAI ChatCompletion API specifications](https://platform.openai.com/docs/api-reference/chat). Please refer to the example request below for reference. Additionally, you can use the [OpenChat Web UI](https://github.com/imoneoi/openchat#web-ui) for a user-friendly experience.

If you want to deploy the server as an online service, you can use `--api-keys sk-KEY1 sk-KEY2 ...` to specify allowed API keys and `--disable-log-requests --disable-log-stats --log-file openchat.log` for logging only to a file. For security purposes, we recommend using an [HTTPS gateway](https://fastapi.tiangolo.com/es/deployment/concepts/#security-https) in front of the server.

| Model                   | Size | Context | Weights                                                                | Serving                                                                                                                |
|-------------------------|------|---------|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| OpenChat-3.5-0106-Gemma | 7B   | 8192    | [Huggingface](https://huggingface.co/openchat/openchat-3.5-0106-gemma) | `python -m ochat.serving.openai_api_server --model openchat/openchat-3.5-0106-gemma --engine-use-ray --worker-use-ray` |

<details>
  <summary>Example request (click to expand)</summary>

```bash
curl http://localhost:18888/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openchat_3.5_gemma_new",
    "messages": [{"role": "user", "content": "You are a large language model named OpenChat. Write a poem to describe yourself"}]
  }'
```


</details>

## Conversation template

⚠️ **Notice:** This is different from the Mistral version. End-of-turn token is `<end_of_turn>` now (Mistral version is `<|end_of_turn|>`). Remember to set `<end_of_turn>` as end of generation token.

```
GPT4 Correct User: Hello<end_of_turn>GPT4 Correct Assistant: Hi<end_of_turn>GPT4 Correct User: How are you today?<end_of_turn>GPT4 Correct Assistant:
```

With system message (**NOT** recommended, may degrade performance)

```
You are a helpful assistant.<end_of_turn>GPT4 Correct User: Hello<end_of_turn>GPT4 Correct Assistant: Hi<end_of_turn>GPT4 Correct User: How are you today?<end_of_turn>GPT4 Correct Assistant:
```

## Hallucination of Non-existent Information
OpenChat may sometimes generate information that does not exist or is not accurate, also known as "hallucination". Users should be aware of this possibility and verify any critical information obtained from the model.

## Safety
OpenChat may sometimes generate harmful, hate speech, biased responses, or answer unsafe questions. It's crucial to apply additional AI safety measures in use cases that require safe and moderated responses.

<div align="center">
<h2> License </h2>
</div>

Our OpenChat 3.5 code and models are distributed under the Apache License 2.0.

## Citation 

```
@article{wang2023openchat,
  title={OpenChat: Advancing Open-source Language Models with Mixed-Quality Data},
  author={Wang, Guan and Cheng, Sijie and Zhan, Xianyuan and Li, Xiangang and Song, Sen and Liu, Yang},
  journal={arXiv preprint arXiv:2309.11235},
  year={2023}
}
```

<div align="center">
<h2> 💌 Contact </h2>
</div>

**Project Lead:**
- Guan Wang [imonenext at gmail dot com]
- [Alpay Ariyak](https://github.com/alpayariyak) [aariyak at wpi dot edu]
