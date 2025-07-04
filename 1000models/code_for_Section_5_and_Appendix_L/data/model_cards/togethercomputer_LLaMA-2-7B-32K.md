
# LLaMA-2-7B-32K

## Model Description

LLaMA-2-7B-32K is an open-source, long context language model developed by Together, fine-tuned from Meta's original Llama-2 7B model. 
This model represents our efforts to contribute to the rapid progress of the open-source ecosystem for large language models. 
The model has been extended to a context length of 32K with position interpolation, 
allowing applications on multi-document QA, long text summarization, etc.

## What's new?

This model introduces several improvements and new features:

1. **Extended Context:** The model has been trained to handle context lengths up to 32K, which is a significant improvement over the previous versions.

2. **Pre-training and Instruction Tuning:** We have shared our data recipe, which consists of a mixture of pre-training and instruction tuning data.

3. **Fine-tuning Examples:** We provide examples of how to fine-tune the model for specific applications, including book summarization and long context question and answering.

4. **Software Support:** We have updated both the inference and training stack to allow efficient inference and fine-tuning for 32K context.

## Model Architecture

The model follows the architecture of Llama-2-7B and extends it to handle a longer context. It leverages the recently released FlashAttention-2 and a range of other optimizations to improve the speed and efficiency of inference and training.

## Training and Fine-tuning

The model has been trained using a mixture of pre-training and instruction tuning data. 
- In the first training phase of continued pre-training, our data mixture contains 25% RedPajama Book, 25% RedPajama ArXiv (including abstracts), 25% other data from RedPajama, and 25% from the UL2 Oscar Data, which is a part of OIG (Open-Instruction-Generalist), asking the model to fill in missing chunks, or complete the text. 
To enhance the long-context ability, we exclude data shorter than 2K word. The inclusion of UL2 Oscar Data is effective in compelling the model to read and utilize long-range context.
- We then fine-tune the model to focus on its few shot capacity under long context, including 20% Natural Instructions (NI), 20% Public Pool of Prompts (P3), 20% the Pile. We decontaminated all data against HELM core scenarios . We teach the model to leverage the in-context examples by packing examples into one 32K-token sequence. To maintain the knowledge learned from the first piece of data, we incorporate 20% RedPajama-Data Book and 20% RedPajama-Data ArXiv.

Next, we provide examples of how to fine-tune the model for specific applications. 
The example datasets are placed in [togethercomputer/Long-Data-Collections](https://huggingface.co/datasets/togethercomputer/Long-Data-Collections)
You can use the [OpenChatKit](https://github.com/togethercomputer/OpenChatKit) to fine-tune your own 32K model over LLaMA-2-7B-32K.
Please refer to [OpenChatKit](https://github.com/togethercomputer/OpenChatKit) for step-by-step illustrations.

1. Long Context QA.

   We take as an example the multi-document question answering task from the paper “Lost in the Middle: How Language Models Use Long Contexts”. The input for the model consists of (i) a question that requires an answer and (ii) k documents, which are passages extracted from Wikipedia. Notably, only one of these documents contains the answer to the question, while the remaining k − 1 documents, termed as "distractor" documents, do not. To successfully perform this task, the model must identify and utilize the document containing the answer from its input context. 

   With OCK, simply run the following command to fine-tune:
   ```
   bash training/finetune_llama-2-7b-32k-mqa.sh
   ```

2. Summarization.

   Another example is BookSum, a unique dataset designed to address the challenges of long-form narrative summarization. This dataset features source documents from the literature domain, including novels, plays, and stories, and offers human-written, highly abstractive summaries. We here focus on chapter-level data.  BookSum poses a unique set of challenges, necessitating that the model comprehensively read through each chapter.

   With OCK, simply run the following command to fine-tune:
   ```
   bash training/finetune_llama-2-7b-32k-booksum.sh
   ```


## Inference

You can use the [Together API](https://together.ai/blog/api-announcement) to try out LLaMA-2-7B-32K for inference. 
The updated inference stack allows for efficient inference.

To run the model locally, we strongly recommend to install Flash Attention V2, which is necessary to obtain the best performance:
```
# Please update the path of `CUDA_HOME`
export CUDA_HOME=/usr/local/cuda-11.8
pip install transformers==4.31.0
pip install sentencepiece
pip install ninja
pip install flash-attn --no-build-isolation
pip install git+https://github.com/HazyResearch/flash-attention.git#subdirectory=csrc/rotary
```

You can use this model directly from the Hugging Face Model Hub or fine-tune it on your own data using the OpenChatKit.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("togethercomputer/LLaMA-2-7B-32K")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/LLaMA-2-7B-32K", trust_remote_code=True, torch_dtype=torch.float16)

input_context = "Your text here"
input_ids = tokenizer.encode(input_context, return_tensors="pt")
output = model.generate(input_ids, max_length=128, temperature=0.7)
output_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(output_text)
```

Alternatively, you can set `trust_remote_code=False` if you prefer not to use flash attention.


## Limitations and Bias

As with all language models, LLaMA-2-7B-32K may generate incorrect or biased content. It's important to keep this in mind when using the model.

## Community

Join us on [Together Discord](https://discord.gg/6ZVDU8tTD4)