

<div align="center">
<img width="260px" src="https://cdn-uploads.huggingface.co/production/uploads/5f3fe13d79c1ba4c353d0c19/BrQCb95lmEIFz79QAmoNA.png"></div>


![image/png](https://cdn-uploads.huggingface.co/production/uploads/5f3fe13d79c1ba4c353d0c19/2FhDh8NDvMl7iSxbQz9BP.png)




<div align="center">
  
  <h1>Advancing Open-source Large Language Models in Medical Domain</h1>
</div>

<p align="center" style="margin-top: 0px;">
  <a href="https://colab.research.google.com/drive/1F5oV20InEYeAJGmBwYF9NM_QhLmjBkKJ?usp=sharing">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="OpenChat Logo" style="width:20px; vertical-align: middle; display: inline-block; margin-right: 5px; margin-left: 10px; margin-top: 0px; margin-bottom: 0px;"/>
    <span class="link-text" style=" margin-right: 5px;">Online Demo</span>
  </a> |
  <a href="https://github.com/openlifescience-ai">
    <img src="https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png" alt="GitHub Logo" style="width:20px; vertical-align: middle; display: inline-block; margin-right: 5px; margin-left: 5px; margin-top: 0px; margin-bottom: 0px;"/>
    <span class="link-text" style=" margin-right: 5px;">GitHub</span>
  </a> |
  <a href="#">
    <img src="https://github.com/alpayariyak/openchat/blob/master/assets/arxiv-logomark-small-square-border.png?raw=true" alt="ArXiv Logo" style="width:20px; vertical-align: middle; display: inline-block; margin-right: 5px; margin-left: 5px; margin-top: 0px; margin-bottom: 0px;"/>
    <span class="link-text" style="margin-right: 5px;">Paper</span>
  </a> |
  <a href="https://discord.gg/A5Fjf5zC69">
    <img src="https://cloud.githubusercontent.com/assets/6291467/26705903/96c2d66e-477c-11e7-9f4e-f3c0efe96c9a.png" alt="Discord Logo" style="width:20px; vertical-align: middle; display: inline-block; margin-right: 5px; margin-left: 5px; margin-top: 0px; margin-bottom: 0px;"/>
    <span class="link-text">Discord</span>
  </a>
</p>

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/5f3fe13d79c1ba4c353d0c19/KGmRE5w2sepNtwsEu8t7K.jpeg)

Introducing OpenBioLLM-8B: A State-of-the-Art Open Source Biomedical Large Language Model


OpenBioLLM-8B is an advanced open source language model designed specifically for the biomedical domain. Developed by Saama AI Labs, this model leverages cutting-edge techniques to achieve state-of-the-art performance on a wide range of biomedical tasks.

🏥 **Biomedical Specialization**: OpenBioLLM-8B is tailored for the unique language and knowledge requirements of the medical and life sciences fields. It was fine-tuned on a vast corpus of high-quality biomedical data, enabling it to understand and generate text with domain-specific accuracy and fluency.

🎓 **Superior Performance**: With 8 billion parameters, OpenBioLLM-8B outperforms other open source biomedical language models of similar scale. It has also demonstrated better results compared to larger proprietary & open-source models like GPT-3.5 and Meditron-70B on biomedical benchmarks.

🧠 **Advanced Training Techniques**: OpenBioLLM-8B builds upon the powerful foundations of the **Meta-Llama-3-8B** and [Meta-Llama-3-8B](meta-llama/Meta-Llama-3-8B) models. It incorporates the DPO dataset and fine-tuning recipe along with a custom diverse medical instruction dataset. Key components of the training pipeline include:

<div align="center">
<img width="1200px" src="https://cdn-uploads.huggingface.co/production/uploads/5f3fe13d79c1ba4c353d0c19/oPchsJsEpQoGcGXVbh7YS.png">
</div>

- **Policy Optimization**: [Direct Preference Optimization: Your Language Model is Secretly a Reward Model (DPO)](https://arxiv.org/abs/2305.18290)
- **Ranking Dataset**: [berkeley-nest/Nectar](https://huggingface.co/datasets/berkeley-nest/Nectar)
- **Fine-tuning dataset**: Custom Medical Instruct dataset (We plan to release a sample training dataset in our upcoming paper; please stay updated)

This combination of cutting-edge techniques enables OpenBioLLM-8B to align with key capabilities and preferences for biomedical applications.

⚙️ **Release Details**:

- **Model Size**: 8 billion parameters
- **Quantization**: Optimized quantized versions available [Here](https://huggingface.co/aaditya/OpenBioLLM-Llama3-8B-GGUF)
- **Language(s) (NLP):** en
- **Developed By**: [Ankit Pal (Aaditya Ura)](https://aadityaura.github.io/) from Saama AI Labs 
- **License:** Meta-Llama License 
- **Fine-tuned from models:** [meta-llama/Meta-Llama-3-8B](meta-llama/Meta-Llama-3-8B)
- **Resources for more information:**
    - Paper: Coming soon

The model can be fine-tuned for more specialized tasks and datasets as needed.

OpenBioLLM-8B represents an important step forward in democratizing advanced language AI for the biomedical community. By leveraging state-of-the-art architectures and training techniques from leading open source efforts like Llama-3, we have created a powerful tool to accelerate innovation and discovery in healthcare and the life sciences.

We are excited to share OpenBioLLM-8B with researchers and developers around the world.


### Community & Resources

#### 🔥 Your Daily Dose of Medical AI Breakthroughs 🚀 
We turn hours of the latest research papers into minutes. Get daily tweets and news on the latest medical AI breakthroughs, dataset releases, and benchmark results – all carefully curated to save you time while keeping you informed.


<div align="center">
<table>
  <tr>
    <td align="center">
      <a href="https://twitter.com/OpenLifeSciAI">
        <img src="https://img.shields.io/badge/X-Follow%20%40OpenLifeSciAI-black?style=flat&logo=x" alt="Twitter Follow"/>
        <br>
        Daily updates on Medical LLMs,<br>datasets & benchmarks
      </a>
    </td>
    <td align="center">
      <a href="https://www.linkedin.com/company/openlifesciai/">
        <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn"/>
        <br>
        Daily news on Medical LLMs,<br>datasets & benchmarks
      </a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://www.youtube.com/@OpenlifesciAI">
        <img src="https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube" alt="YouTube"/>
        <br>
        Video & audio summaries of<br>latest research
      </a>
    </td>
    <td align="center">
      <a href="https://t.co/l5z6y6C4cM">
        <img src="https://img.shields.io/badge/Discord-Join-7289DA?style=for-the-badge&logo=discord" alt="Discord"/>
        <br>
        Connect with researchers &<br>discuss latest developments
      </a>
    </td>
  </tr>
</table>
</div>


### Use with transformers

**Important: Please use the exact chat template provided by Llama-3 instruct version. Otherwise there will be a degradation in the performance. The model output can be verbose in rare cases. Please consider setting temperature = 0 to make this happen less.**

See the snippet below for usage with Transformers:

```python
import transformers
import torch

model_id = "aaditya/OpenBioLLM-Llama3-8B"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device="auto",
)

messages = [
    {"role": "system", "content": "You are an expert and experienced from the healthcare and biomedical domain with extensive medical knowledge and practical experience. Your name is OpenBioLLM, and you were developed by Saama AI Labs. who's willing to help answer the user's query with explanation. In your explanation, leverage your deep medical expertise such as relevant anatomical structures, physiological processes, diagnostic criteria, treatment guidelines, or other pertinent medical concepts. Use precise medical terminology while still aiming to make the explanation clear and accessible to a general audience."},
    {"role": "user", "content": "How can i split a 3mg or 4mg waefin pill so i can get a 2.5mg pill?"},
]

prompt = pipeline.tokenizer.apply_chat_template(
		messages, 
		tokenize=False, 
		add_generation_prompt=True
)

terminators = [
    pipeline.tokenizer.eos_token_id,
    pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = pipeline(
    prompt,
    max_new_tokens=256,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.0,
    top_p=0.9,
)
print(outputs[0]["generated_text"][len(prompt):])
```

## **Training procedure**

### **Training hyperparameters**

<details>
  <summary>Click to see details</summary>

- learning_rate: 0.0002
- lr_scheduler: cosine
- train_batch_size: 12
- eval_batch_size: 8
- GPU: H100 80GB SXM5
- num_devices: 1
- optimizer: adamw_bnb_8bit
- lr_scheduler_warmup_steps: 100
- num_epochs: 4
</details>

  
### **Peft hyperparameters**

<details>
  <summary>Click to see details</summary>

- adapter: qlora
- lora_r: 128
- lora_alpha: 256
- lora_dropout: 0.05
- lora_target_linear: true
  
-lora_target_modules:
  - q_proj
  - v_proj
  - k_proj
  - o_proj
  - gate_proj
  - down_proj
  - up_proj
</details>



### **Training results**

### **Framework versions**

- Transformers 4.39.3
- Pytorch 2.1.2+cu121
- Datasets 2.18.0
- Tokenizers 0.15.1
- Axolotl
- Lm harness for evaluation


# Benchmark Results

🔥 OpenBioLLM-8B demonstrates superior performance compared to larger models, such as GPT-3.5,  Meditron-70B across 9 diverse biomedical datasets, achieving state-of-the-art results with an average score of 72.50%, despite having a significantly smaller parameter count. The model's strong performance in domain-specific tasks, such as Clinical KG, Medical Genetics, and PubMedQA, highlights its ability to effectively capture and apply biomedical knowledge.

🚨 The GPT-4, Med-PaLM-1, and Med-PaLM-2 results are taken from their official papers. Since Med-PaLM doesn't provide zero-shot accuracy, we are using 5-shot accuracy from their paper for comparison. All results presented are in the zero-shot setting, except for Med-PaLM-2 and Med-PaLM-1, which use 5-shot accuracy.

|                    | Clinical KG | Medical Genetics | Anatomy | Pro Medicine | College Biology | College Medicine | MedQA 4 opts | PubMedQA | MedMCQA | Avg   |
|--------------------|-------------|------------------|---------|--------------|-----------------|------------------|--------------|----------|---------|-------|
| **OpenBioLLM-70B** | **92.93**       | **93.197**           | **83.904**  | 93.75       | 93.827          | **85.749**           | 78.162       | 78.97    | **74.014**  | **86.05588** |
| Med-PaLM-2 (5-shot)            | 88.3        | 90               | 77.8    | **95.2**         | 94.4            | 80.9             | **79.7**         | **79.2**     | 71.3    | 84.08 |
| **GPT-4**              | 86.04       | 91               | 80      | 93.01        | **95.14**           | 76.88            | 78.87        | 75.2     | 69.52   | 82.85 |
| Med-PaLM-1 (Flan-PaLM, 5-shot) | 80.4        | 75               | 63.7    | 83.8         | 88.9            | 76.3             | 67.6         | 79       | 57.6    | 74.7  |
| **OpenBioLLM-8B**    | 76.101      | 86.1               | 69.829  | 78.21        | 84.213         | 68.042           | 58.993       | 74.12     | 56.913  | 72.502 |
| Gemini-1.0             | 76.7        | 75.8             | 66.7    | 77.7         | 88              | 69.2             | 58          | 70.7     | 54.3    | 70.79 |
| GPT-3.5 Turbo 1106     | 74.71       | 74               | 72.79   | 72.79        | 72.91           | 64.73            | 57.71        | 72.66    | 53.79   | 66    |
| Meditron-70B           | 66.79       | 69               | 53.33   | 71.69        | 76.38           | 63               | 57.1         | 76.6     | 46.85   | 64.52 |
| gemma-7b               | 69.81       | 70               | 59.26   | 66.18        | 79.86           | 60.12            | 47.21        | 76.2     | 48.96   | 64.18 |
| Mistral-7B-v0.1        | 68.68       | 71               | 55.56   | 68.38        | 68.06           | 59.54            | 50.82        | 75.4     | 48.2    | 62.85 |
| Apollo-7B              | 62.26       | 72               | 61.48   | 69.12        | 70.83           | 55.49            | 55.22        | 39.8     | 53.77   | 60    |
| MedAlpaca-7b           | 57.36       | 69               | 57.04   | 67.28        | 65.28           | 54.34            | 41.71        | 72.8     | 37.51   | 58.03 |
| BioMistral-7B          | 59.9        | 64               | 56.5    | 60.4         | 59              | 54.7             | 50.6         | 77.5     | 48.1    | 57.3  |
| AlpaCare-llama2-7b     | 49.81       | 49               | 45.92   | 33.82        | 50              | 43.35            | 29.77        | 72.2     | 34.42   | 45.36 |
| ClinicalGPT            | 30.56       | 27               | 30.37   | 19.48        | 25              | 24.27            | 26.08        | 63.8     | 28.18   | 30.52 |

<div align="center">
<img width="1600px" src="https://cdn-uploads.huggingface.co/production/uploads/5f3fe13d79c1ba4c353d0c19/_SzdcJSBjZyo8RS1bTEkP.png">
</div>

## Detailed Medical Subjectwise accuracy


![image/png](https://cdn-uploads.huggingface.co/production/uploads/5f3fe13d79c1ba4c353d0c19/UXF-V0col0Z0sS6BGPBkE.png)

# Use Cases & Examples

🚨 **Below results are from the quantized version of OpenBioLLM-70B**


# Summarize Clinical Notes

OpenBioLLM-70B can efficiently analyze and summarize complex clinical notes, EHR data, and discharge summaries, extracting key information and generating concise, structured summaries


![image/png](https://cdn-uploads.huggingface.co/production/uploads/5f3fe13d79c1ba4c353d0c19/xdwdBgOxNi_TfML0hKlI8.png)

# Answer Medical Questions

OpenBioLLM-70B can provide answers to a wide range of medical questions.


![image/png](https://cdn-uploads.huggingface.co/production/uploads/5f3fe13d79c1ba4c353d0c19/zO95GlwOQEZqCKQF69mE6.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/5f3fe13d79c1ba4c353d0c19/OKBczKw7gWeW5xsuDpc27.png)

<details>
  <summary>Click to see details</summary>


![image/png](https://cdn-uploads.huggingface.co/production/uploads/5f3fe13d79c1ba4c353d0c19/eJGHT5khppYvJb8fQ-YW4.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/5f3fe13d79c1ba4c353d0c19/Cnbwrqa_-ORHRuNRC2P6Y.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/5f3fe13d79c1ba4c353d0c19/J9DhdcvukAc9mnnW9fj2C.png)

</details>

# Clinical Entity Recognition

OpenBioLLM-70B can perform advanced clinical entity recognition by identifying and extracting key medical concepts, such as diseases, symptoms, medications, procedures, and anatomical structures, from unstructured clinical text. By leveraging its deep understanding of medical terminology and context, the model can accurately annotate and categorize clinical entities, enabling more efficient information retrieval, data analysis, and knowledge discovery from electronic health records, research articles, and other biomedical text sources. This capability can support various downstream applications, such as clinical decision support, pharmacovigilance, and medical research.


![image/png](https://cdn-uploads.huggingface.co/production/uploads/5f3fe13d79c1ba4c353d0c19/_69BW4k9LVABFwtxixL45.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/5f3fe13d79c1ba4c353d0c19/DKy5wYCoPhoPPUc1-x8_J.png)
![image/png](https://cdn-uploads.huggingface.co/production/uploads/5f3fe13d79c1ba4c353d0c19/7WD9zCCBZT4-4XlfnIQjl.png)

# Biomarkers Extraction


![image/png](https://cdn-uploads.huggingface.co/production/uploads/5f3fe13d79c1ba4c353d0c19/ZttoM4AiteT7gFYVhjIpN.png)


# Classification

OpenBioLLM-70B can perform various biomedical classification tasks, such as disease prediction, sentiment analysis, medical document categorization

![image/png](https://cdn-uploads.huggingface.co/production/uploads/5f3fe13d79c1ba4c353d0c19/Bf5MW1d75qT-1F_TR_hC0.png)

# De-Identification

OpenBioLLM-70B can detect and remove personally identifiable information (PII) from medical records, ensuring patient privacy and compliance with data protection regulations like HIPAA.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/5f3fe13d79c1ba4c353d0c19/hKX4kzm--Tw5bj6K78msy.png)



**Advisory Notice!** 

While OpenBioLLM-70B & 8B leverages high-quality data sources, its outputs may still contain inaccuracies, biases, or misalignments that could pose risks if relied upon for medical decision-making without further testing and refinement. The model's performance has not yet been rigorously evaluated in randomized controlled trials or real-world healthcare environments.

Therefore, we strongly advise against using OpenBioLLM-70B & 8B for any direct patient care, clinical decision support, or other professional medical purposes at this time. Its use should be limited to research, development, and exploratory applications by qualified individuals who understand its limitations.
OpenBioLLM-70B & 8B are intended solely as a research tool to assist healthcare professionals and should never be considered a replacement for the professional judgment and expertise of a qualified medical doctor.

Appropriately adapting and validating OpenBioLLM-70B & 8B for specific medical use cases would require significant additional work, potentially including:

- Thorough testing and evaluation in relevant clinical scenarios
- Alignment with evidence-based guidelines and best practices
- Mitigation of potential biases and failure modes
- Integration with human oversight and interpretation
- Compliance with regulatory and ethical standards

Always consult a qualified healthcare provider for personal medical needs.



# Citation

If you find OpenBioLLM-70B & 8B useful in your work, please cite the model as follows:

```
@misc{OpenBioLLMs,
  author = {Ankit Pal, Malaikannan Sankarasubbu},
  title = {OpenBioLLMs: Advancing Open-Source Large Language Models for Healthcare and Life Sciences},
  year = {2024},
  publisher = {Hugging Face},
  journal = {Hugging Face repository},
  howpublished = {\url{https://huggingface.co/aaditya/OpenBioLLM-Llama3-70B}}
}
```

The accompanying paper is currently in progress and will be released soon.

<div align="center">
<h2> 💌 Contact </h2>
</div>

We look forward to hearing you and collaborating on this exciting project!

**Contributors:**
- [Ankit Pal (Aaditya Ura)](https://aadityaura.github.io/) [aadityaura at gmail dot com]
- Saama AI Labs
- Note: I am looking for a funded PhD opportunity, especially if it fits my Responsible Generative AI, Multimodal LLMs, Geometric Deep Learning, and Healthcare AI skillset.


# References

We thank the [Meta Team](meta-llama/Meta-Llama-3-70B-Instruct) for their amazing models!


Result sources

- [1] GPT-4 [Capabilities of GPT-4 on Medical Challenge Problems] (https://arxiv.org/abs/2303.13375) 
- [2] Med-PaLM-1 [Large Language Models Encode Clinical Knowledge](https://arxiv.org/abs/2212.13138)
- [3] Med-PaLM-2 [Towards Expert-Level Medical Question Answering with Large Language Models](https://arxiv.org/abs/2305.09617)
- [4] Gemini-1.0 [Gemini Goes to Med School](https://arxiv.org/abs/2402.07023)