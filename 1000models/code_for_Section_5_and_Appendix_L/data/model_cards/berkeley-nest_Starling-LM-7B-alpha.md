# Starling-LM-7B-alpha

<!-- Provide a quick summary of what the model is/does. -->

- **Developed by:** Banghua Zhu * , Evan Frick * , Tianhao Wu * , Hanlin Zhu and Jiantao Jiao.
- **Model type:** Language Model finetuned with RLHF / RLAIF
- **License:** Apache-2.0 license under the condition that the model is not used to compete with OpenAI
- **Finetuned from model:** [Openchat 3.5](https://huggingface.co/openchat/openchat_3.5) (based on [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1))
 


We introduce Starling-7B, an open large language model (LLM) trained by Reinforcement Learning from AI Feedback (RLAIF). The model harnesses the power of our new GPT-4 labeled ranking dataset, [berkeley-nest/Nectar](https://huggingface.co/datasets/berkeley-nest/Nectar), and our new reward training and policy tuning pipeline. Starling-7B-alpha scores 8.09 in MT Bench with GPT-4 as a judge, outperforming every model to date on MT-Bench except for OpenAI's GPT-4 and GPT-4 Turbo. We release the ranking dataset [Nectar](https://huggingface.co/datasets/berkeley-nest/Nectar), the reward model [Starling-RM-7B-alpha](https://huggingface.co/berkeley-nest/Starling-RM-7B-alpha) and the language model [Starling-LM-7B-alpha](https://huggingface.co/berkeley-nest/Starling-LM-7B-alpha) on HuggingFace, and an online demo in LMSYS [Chatbot Arena](https://chat.lmsys.org). Stay tuned for our forthcoming code and paper, which will provide more details on the whole process.

Starling-LM-7B-alpha is a language model trained from [Openchat 3.5](https://huggingface.co/openchat/openchat_3.5) with reward model [berkeley-nest/Starling-RM-7B-alpha](https://huggingface.co/berkeley-nest/Starling-RM-7B-alpha) and policy optimization method [advantage-induced policy alignment (APA)](https://arxiv.org/abs/2306.02231). The evaluation results are listed below.


| Model                 | Tuning Method    | MT Bench | AlpacaEval | MMLU |
|-----------------------|------------------|----------|------------|------|
| GPT-4-Turbo           | ?                | 9.32     | 97.70      |      |
| GPT-4                 | SFT + PPO        | 8.99     | 95.28      | 86.4 |
| **Starling-7B**           | C-RLFT + APA     | 8.09     | 91.99      | 63.9 |
| Claude-2              | ?                | 8.06     | 91.36      | 78.5 |
| GPT-3.5-Turbo         | ?                | 7.94     | 89.37      | 70   |
| Claude-1              | ?                | 7.9      | 88.39      | 77   |
| Tulu-2-dpo-70b        | SFT + DPO        | 7.89     | 95.1       |      |
| Openchat-3.5          | C-RLFT           | 7.81     | 88.51      | 64.3 |
| Zephyr-7B-beta        | SFT + DPO        | 7.34     | 90.60      | 61.4 |
| Llama-2-70b-chat-hf   | SFT + PPO        | 6.86     | 92.66      | 63   |
| Neural-chat-7b-v3-1   | SFT + DPO        | 6.84     | 84.53      | 62.4 | 
| Tulu-2-dpo-7b         | SFT + DPO        | 6.29     | 85.1       |      |



For more detailed discussions, please check out our [blog post](https://starling.cs.berkeley.edu), and stay tuned for our upcoming code and paper!
<!-- Provide the basic links for the model. -->

- **Blog:** https://starling.cs.berkeley.edu/
- **Paper:** Coming soon!
- **Code:** Coming soon!



## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

**Important: Please use the exact chat template provided below for the model. Otherwise there will be a degrade in the performance. The model output can be verbose in rare cases. Please consider setting temperature = 0 to make this happen less.**

Our model follows the exact chat template and usage as [Openchat 3.5](https://huggingface.co/openchat/openchat_3.5). Please refer to their model card for more details.
In addition, our model is hosted on LMSYS [Chatbot Arena](https://chat.lmsys.org) for free test.

The conversation template is the same as Openchat 3.5:
```
import transformers
tokenizer = transformers.AutoTokenizer.from_pretrained("openchat/openchat_3.5")

# Single-turn
tokens = tokenizer("GPT4 Correct User: Hello<|end_of_turn|>GPT4 Correct Assistant:").input_ids
assert tokens == [1, 420, 6316, 28781, 3198, 3123, 1247, 28747, 22557, 32000, 420, 6316, 28781, 3198, 3123, 21631, 28747]

# Multi-turn
tokens = tokenizer("GPT4 Correct User: Hello<|end_of_turn|>GPT4 Correct Assistant: Hi<|end_of_turn|>GPT4 Correct User: How are you today?<|end_of_turn|>GPT4 Correct Assistant:").input_ids
assert tokens == [1, 420, 6316, 28781, 3198, 3123, 1247, 28747, 22557, 32000, 420, 6316, 28781, 3198, 3123, 21631, 28747, 15359, 32000, 420, 6316, 28781, 3198, 3123, 1247, 28747, 1602, 460, 368, 3154, 28804, 32000, 420, 6316, 28781, 3198, 3123, 21631, 28747]

# Coding Mode
tokens = tokenizer("Code User: Implement quicksort using C++<|end_of_turn|>Code Assistant:").input_ids
assert tokens == [1, 7596, 1247, 28747, 26256, 2936, 7653, 1413, 334, 1680, 32000, 7596, 21631, 28747]
```
## Code Examples

```python
import transformers

tokenizer = transformers.AutoTokenizer.from_pretrained("berkeley-nest/Starling-LM-7B-alpha")
model = transformers.AutoModelForCausalLM.from_pretrained("berkeley-nest/Starling-LM-7B-alpha")

def generate_response(prompt):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    outputs = model.generate(
        input_ids,
        max_length=256,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )
    response_ids = outputs[0]
    response_text = tokenizer.decode(response_ids, skip_special_tokens=True)
    return response_text

# Single-turn conversation
prompt = "Hello, how are you?"
single_turn_prompt = f"GPT4 Correct User: {prompt}<|end_of_turn|>GPT4 Correct Assistant:"
response_text = generate_response(single_turn_prompt)
print("Response:", response_text)

## Multi-turn conversation
prompt = "Hello"
follow_up_question =  "How are you today?"
response = ""
multi_turn_prompt = f"GPT4 Correct User: {prompt}<|end_of_turn|>GPT4 Correct Assistant: {response}<|end_of_turn|>GPT4 Correct User: {follow_up_question}<|end_of_turn|>GPT4 Correct Assistant:"
response_text = generate_response(multi_turn_prompt)
print("Multi-turn conversation response:", response_text)

### Coding conversation
prompt = "Implement quicksort using C++"
coding_prompt = f"Code User: {prompt}<|end_of_turn|>Code Assistant:"
response = generate_response(coding_prompt)
print("Coding conversation response:", response)
```

## License
The dataset, model and online demo is a research preview intended for non-commercial use only, subject to the data distillation [License](https://github.com/facebookresearch/llama/blob/main/MODEL_CARD.md) of LLaMA, [Terms of Use](https://openai.com/policies/terms-of-use) of the data generated by OpenAI, and [Privacy Practices](https://chrome.google.com/webstore/detail/sharegpt-share-your-chatg/daiacboceoaocpibfodeljbdfacokfjb) of ShareGPT. Please contact us if you find any potential violation.


## Acknowledgment
We would like to thank Wei-Lin Chiang from Berkeley for detailed feedback of the blog and the projects. We would like to thank the [LMSYS Organization](https://lmsys.org/) for their support of [lmsys-chat-1M](https://huggingface.co/datasets/lmsys/lmsys-chat-1m) dataset, evaluation and online demo. We would like to thank the open source community for their efforts in providing the datasets and base models we used to develope the project, including but not limited to Anthropic, Llama, Mistral, Hugging Face H4, LMSYS, OpenChat, OpenBMB, Flan and ShareGPT.

## Citation
```
@misc{starling2023,
    title = {Starling-7B: Improving LLM Helpfulness & Harmlessness with RLAIF},
    url = {},
    author = {Zhu, Banghua and Frick, Evan and Wu, Tianhao and Zhu, Hanlin and Jiao, Jiantao},
    month = {November},
    year = {2023}
}
```