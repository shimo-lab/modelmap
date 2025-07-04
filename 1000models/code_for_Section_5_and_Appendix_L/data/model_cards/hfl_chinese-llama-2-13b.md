
# Chinese-LLaMA-2-13B

**This is the full Chinese-LLaMA-2-13B model，which can be loaded directly for inference and full-parameter training.**

**Related models👇**
* Long context base models
  * [Chinese-LLaMA-2-7B-16K (full model)](https://huggingface.co/hfl/chinese-llama-2-7b-16k)
  * [Chinese-LLaMA-2-LoRA-7B-16K (LoRA model)](https://huggingface.co/hfl/chinese-llama-2-lora-7b-16k)
  * [Chinese-LLaMA-2-13B-16K (full model)](https://huggingface.co/hfl/chinese-llama-2-13b-16k)
  * [Chinese-LLaMA-2-LoRA-13B-16K (LoRA model)](https://huggingface.co/hfl/chinese-llama-2-lora-13b-16k)
* Base models
  * [Chinese-LLaMA-2-7B (full model)](https://huggingface.co/hfl/chinese-llama-2-7b)
  * [Chinese-LLaMA-2-LoRA-7B (LoRA model)](https://huggingface.co/hfl/chinese-llama-2-lora-7b)
  * [Chinese-LLaMA-2-13B (full model)](https://huggingface.co/hfl/chinese-llama-2-13b)
  * [Chinese-LLaMA-2-LoRA-13B (LoRA model)](https://huggingface.co/hfl/chinese-llama-2-lora-13b)
* Instruction/Chat models
  * [Chinese-Alpaca-2-7B (full model)](https://huggingface.co/hfl/chinese-alpaca-2-7b)
  * [Chinese-Alpaca-2-LoRA-7B (LoRA model)](https://huggingface.co/hfl/chinese-alpaca-2-lora-7b)
  * [Chinese-Alpaca-2-13B (full model)](https://huggingface.co/hfl/chinese-alpaca-2-13b)
  * [Chinese-Alpaca-2-LoRA-13B (LoRA model)](https://huggingface.co/hfl/chinese-alpaca-2-lora-13b)

# Description of Chinese-LLaMA-Alpaca-2 
This project is based on the Llama-2, released by Meta, and it is the second generation of the Chinese LLaMA & Alpaca LLM project. We open-source Chinese LLaMA-2 (foundation model) and Alpaca-2 (instruction-following model). These models have been expanded and optimized with Chinese vocabulary beyond the original Llama-2. We used large-scale Chinese data for incremental pre-training, which further improved the fundamental semantic understanding of the Chinese language, resulting in a significant performance improvement compared to the first-generation models. The relevant models support a 4K context and can be expanded up to 18K+ using the NTK method.

The main contents of this project include:

* 🚀 New extended Chinese vocabulary beyond Llama-2, open-sourcing the Chinese LLaMA-2 and Alpaca-2 LLMs.
* 🚀 Open-sourced the pre-training and instruction finetuning (SFT) scripts for further tuning on user's data
* 🚀 Quickly deploy and experience the quantized LLMs on CPU/GPU of personal PC
* 🚀 Support for LLaMA ecosystems like 🤗transformers, llama.cpp, text-generation-webui, LangChain, vLLM etc.

Please refer to [https://github.com/ymcui/Chinese-LLaMA-Alpaca-2/](https://github.com/ymcui/Chinese-LLaMA-Alpaca-2/) for details.