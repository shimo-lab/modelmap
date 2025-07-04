This model is a 7B [Self-RAG](https://selfrag.github.io/) model that generates outputs to diverse user queries as well as *reflection tokens* to call the retrieval system adaptively and criticize its own output and retrieved passages.  

Self-RAG is trained on our instruction-following corpora with interleaving passages and reflection tokens using the standard next-token prediction objective, enabling efficient and stable learning with fine-grained feedback.  
At inference, we leverage reflection tokens covering diverse aspects of generations to sample the best output aligning users' preferences. 
See full descriptions in See full descriptions in [our paper](https://arxiv.org/abs/2310.11511). 

## Usage
Here, we show an easy way to quickly download our model from HuggingFace and run with `vllm` with pre-given passages. Make sure to install dependencies listed at [self-rag/requirements.txt](https://github.com/AkariAsai/self-rag/blob/main/requirements.txt). 
To run our full inference pipeline with a retrieval system and fine-grained tree decoding, please use [our code](https://github.com/AkariAsai/self-rag). 

```py
from transformers import AutoTokenizer, AutoModelForCausalLM
from vllm import LLM, SamplingParams

model = LLM("selfrag/selfrag_llama2_7b", download_dir="/gscratch/h2lab/akari/model_cache", dtype="half")
sampling_params = SamplingParams(temperature=0.0, top_p=1.0, max_tokens=100, skip_special_tokens=False)

def format_prompt(input, paragraph=None):
  prompt = "### Instruction:\n{0}\n\n### Response:\n".format(input)
  if paragraph is not None:
    prompt += "[Retrieval]<paragraph>{0}</paragraph>".format(paragraph)
  return prompt

query_1 = "Leave odd one out: twitter, instagram, whatsapp."
query_2 = "Can you tell me the difference between llamas and alpacas?"
queries = [query_1, query_2]

preds = model.generate([format_prompt(query) for query in queries], sampling_params)
for pred in preds:
  print("Model prediction: {0}".format(pred.outputs[0].text))
# Model prediction: Twitter, Instagram, and WhatsApp are all social media platforms.[No Retrieval]WhatsApp is the odd one out because it is a messaging app, while Twitter and # Instagram are primarily used for sharing photos and videos.[Utility:5]</s> (this query doesn't require factual grounding; just skip retrieval and do normal instruction-following generation)
# Model prediction: Sure![Retrieval]<paragraph> ... (this query requires factual grounding, call a retriever)

# generate with retrieved passage
prompt = format_prompt("Can you tell me the difference between llamas and alpacas?", paragraph="The alpaca (Lama pacos) is a species of South American camelid mammal. It is similar to, and often confused with, the llama. Alpacas are considerably smaller than llamas, and unlike llamas, they were not bred to be working animals, but were bred specifically for their fiber.")
preds = model.generate([prompt], sampling_params)
print([pred.outputs[0].text for pred in preds])
# ['[Relevant]Alpacas are considerably smaller than llamas, and unlike llamas, they were not bred to be working animals, but were bred specifically for their fiber.[Fully supported][Utility:5]</s>']
```

## Input Format
As described in the `format_prompt` function, your input should be formed as 
```
### Instruction:\n{instruction}\n\n### Response:\n".format(instruction)
```
or
```
### Instruction:\n{instruction}\n\n### Input:\n{input}\n\n### Response:\n"
```
If you have additional input. 
You can insert paragraphs anywhere after `### Response:\n"`, but make sure to mark paragraphs as paragraph tokens (i.e., `<paragraph>{0}</paragraph>`).

## Training details
Our training data is available at the HuggingFace dataset [selfrag_train_data](https://huggingface.co/datasets/selfrag/selfrag_train_data). 
See our official repository for the training details. 
We used 8 A100 40GB for training on the Stability HPC server.

## Citation and contact
If you use this model, please cite our work: 
```
@article{asai2023selfrag,
  author    = {Asai, Akari and Wu, Zeqiu and Wang, Yizhong and Sil, Avirup and Hajishirzi, Hannaneh},
  title     = {{Self-RAG}: Learning to Retrieve, Generate, and Critique through Self-Reflection},
  year      = {2023},
  journal   = { arXiv preprint arXiv:2310.11511 },
  URL       = {https://arxiv.org/abs/2310.11511}
}
```