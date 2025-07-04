
# SciPhi-Self-RAG-Mistral-7B-32k Model Card

SciPhi-Self-RAG-Mistral-7B-32k is a Large Language Model (LLM) fine-tuned from Mistral-7B-v0.1. This model underwent the fine-tuning process described in the [SciPhi-Mistral-7B-32k](https://huggingface.co/SciPhi/SciPhi-Mistral-7B-32k) model card. It then underwent further fine-tuning on the recently released [self-rag](https://arxiv.org/abs//2310.11511) dataset. Other RAG-related instruct datasets were mixed in during this process in an effort to keep the tone of the current model. This model benchmarks well, but it needs further tuning to be an excellent conversationalist.

Benchmark Results:
![image/png](https://cdn-uploads.huggingface.co/production/uploads/64c806dc4515835c4d7b0b6d/_KV_hXZ0SPkmJUnHudoFz.png)

SciPhi-AI is available via a free hosted API, though the exposed model can vary. Currently, SciPhi-Self-RAG-Mistral-7B-32k is available. More details can be found in the docs [here](https://sciphi.readthedocs.io/en/latest/setup/quickstart.html).


## Recommended Chat Formatting
```

We recommend mapping such that

messages = [
    {
        "role": "system",
        "content": "You are a friendly chatbot who always responds in the style of a pirate",
    },
    {"role": "user", "content": "How many helicopters can a human eat in one sitting?"},
]

goes to --->

### System:
You are a friendly chatbot who always responds in the style of a pirate

### Instruction:
How many helicopters can a human eat in one sitting?

### Response:
...

Here is a sample implementation that does this and combines with RAG context retrieval.

def get_chat_completion(
    self, conversation: list[dict], generation_config: GenerationConfig
) -> str:
    self._check_stop_token(generation_config.stop_token)
    prompt = ""
    added_system_prompt = False
    for message in conversation:
        if message["role"] == "system":
            prompt += f"### System:\n{SciPhiLLMInterface.ALPACA_CHAT_SYSTEM_PROMPT}. Further, the assistant is given the following additional instructions - {message['content']}\n\n"
            added_system_prompt = True
        elif message["role"] == "user":
            last_user_message = message["content"]
            prompt += f"### Instruction:\n{last_user_message}\n\n"
        elif message["role"] == "assistant":
            prompt += f"### Response:\n{message['content']}\n\n"

    if not added_system_prompt:
        prompt = f"### System:\n{SciPhiLLMInterface.ALPACA_CHAT_SYSTEM_PROMPT}.\n\n{prompt}"

    context = self.rag_interface.get_contexts([last_user_message])[0]
    prompt += f"### Response:\n{SciPhiFormatter.RETRIEVAL_TOKEN} {SciPhiFormatter.INIT_PARAGRAPH_TOKEN}{context}{SciPhiFormatter.END_PARAGRAPH_TOKEN}"
    latest_completion = self.model.get_instruct_completion(
        prompt, generation_config
    ).strip()

    return SciPhiFormatter.remove_cruft(latest_completion)


```
## Model Architecture

Base Model: Mistral-7B-v0.1

**Architecture Features:**
- Transformer-based model
- Grouped-Query Attention
- Sliding-Window Attention
- Byte-fallback BPE tokenizer

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)

## References

1. Asai, A., Wu, Z., Wang, Y., Sil, A., & Hajishirzi, H. (2023). Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection. arXiv preprint arXiv:2310.11511.
2. Lian, W., Goodson, B., Wang, G., Pentland, E., Cook, A., Vong, C., & Teknium. (2023). MistralOrca: Mistral-7B Model Instruct-tuned on Filtered OpenOrcaV1 GPT-4 Dataset. *HuggingFace repository*. [Link](https://huggingface.co/Open-Orca/Mistral-7B-OpenOrca)
3. Mukherjee, S., Mitra, A., Jawahar, G., Agarwal, S., Palangi, H., & Awadallah, A. (2023). Orca: Progressive Learning from Complex Explanation Traces of GPT-4. *arXiv preprint arXiv:2306.02707*.
4. Longpre, S., Hou, L., Vu, T., Webson, A., Chung, H. W., Tay, Y., Zhou, D., Le, Q. V., Zoph, B., Wei, J., & Roberts, A. (2023). The Flan Collection: Designing Data and Methods for Effective Instruction Tuning. *arXiv preprint arXiv:2301.13688*.
5. Mistral AI. (2023). Model Card for Mistral-7B-v0.1. The Mistral-7B-v0.1 Large Language Model (LLM) is a pretrained generative text model with 7 billion parameters. Mistral-7B-v0.1 outperforms Llama 2 13B on all benchmarks tested. For full details, please refer to the paper and release blog post. Model Architecture: Transformer with Grouped-Query Attention, Sliding-Window Attention, and Byte-fallback BPE tokenizer. [Link](https://huggingface.co/mistralai/Mistral-7B-v0.1)


## Acknowledgements

Thank you to the [AI Alignment Lab](https://huggingface.co/Alignment-Lab-AI), [vikp](https://huggingface.co/vikp), [jph00](https://huggingface.co/jph00) and others who contributed to this work.