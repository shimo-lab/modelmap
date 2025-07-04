# Llama-3-8B-UltraMedical

> Experience it in our 🤗 [Huggingface Space Demo](https://huggingface.co/spaces/TsinghuaC3I/UltraMedical-LM)!

<!-- Provide a quick summary of what the model is/does. -->

Llama-3-8B-UltraMedical is an open-access large language model (LLM) specialized in biomedicine. Developed by the [Tsinghua C3I Lab](https://github.com/TsinghuaC3I), this model aims to enhance medical examination access, literature comprehension, and clinical knowledge.

Building on the foundation of Meta's Llama-3-8B, Llama-3-8B-UltraMedical is trained on our [UltraMedical](https://github.com/TsinghuaC3I/UltraMedical) dataset, which includes 410,000 diverse entries comprising both synthetic and manually curated samples.

Llama-3-8B-UltraMedical has achieved top average scores across several popular medical benchmarks, including MedQA, MedMCQA, PubMedQA, and MMLU-Medical.
In these benchmarks, Llama-3-8B-UltraMedical significantly outperforms Flan-PaLM, OpenBioLM-8B, Gemini-1.0, GPT-3.5, and Meditron-70b.
We extend our gratitude to Meta for the Llama model, which provided an excellent foundation for our fine-tuning efforts.

## Usage

### Input Examples

This model utilizes the Llama-3 default chat template without a system prompt.
Below, we provide input examples for multi-choice QA, PubMedQA, and open-ended questions.

> Note: To reproduce our evaluation results for the medical QA benchmark, we recommend using the following format to organize questions and multiple-choice options.

- Input example for MedQA and MedMCQA:
```
A 42-year-old homeless man is brought to the emergency room after he was found unconscious in a park. He has alcohol on his breath and is known to have a history of chronic alcoholism. A noncontrast CT scan of the head is normal. The patient is treated for acute alcohol intoxication and admitted to the hospital. The next day, the patient demands to be released. His vital signs are a pulse 120/min, a respiratory rate 22/min, and blood pressure 136/88 mm Hg. On physical examination, the patient is confused, agitated, and sweating profusely, particularly from his palms. Generalized pallor is present. What is the mechanism of action of the drug recommended to treat this patient_s most likely condition?

A. It increases the duration of GABA-gated chloride channel opening.
B. It increases the frequency of GABA-gated chloride channel opening.
C. It decreases the frequency of GABA-gated chloride channel opening.
D. It decreases the duration of GABA-gated chloride channel opening.
```

- Input example for PubMedQA: We organize the context and questions in a multi-choice format, similar to [MedPrompt](https://github.com/microsoft/promptbase).

```
Context: Pediatric glioblastoma is a malignant disease with an extremely poor clinical outcome. Patients usually suffer from resistance to radiation therapy, so targeted drug treatment may be a new possibility for glioblastoma therapy. Survivin is also overexpressed in glioblastoma. YM155, a novel small-molecule survivin inhibitor, has not been examined for its use in glioblastoma therapy.
Context: The human glioblastoma cell line M059K, which expresses normal DNA-dependent protein kinase (DNA-PK) activity and is radiation-resistant, and M059J, which is deficient in DNA-PK activity and radiation-sensitive, were used in the study. Cell viability, DNA fragmentation, and the expression of survivin and securin following YM155 treatment were examined using MTT (methylthiazolyldiphenyl-tetrazolium) assay, ELISA assay, and Western blot analysis, respectively.
Context: YM155 caused a concentration-dependent cytotoxic effect, inhibiting the cell viability of both M059K and M059J cells by 70% after 48 hours of treatment with 50 nM YM155. The half-maximal inhibitory concentration (IC50) was around 30-35 nM for both cell lines. Apoptosis was determined to have occurred in both cell lines because immunoreactive signals from the DNA fragments in the cytoplasm were increased 24 hours after treatment with 30 nM YM155. The expression of survivin and securin in the M059K cells was greater than that measured in the M059J cells. Treatment with 30 nM YM155, for both 24 and 48 hours, significantly suppressed the expression of survivin and securin in both cell lines.
Does novel survivin inhibitor YM155 elicit cytotoxicity in glioblastoma cell lines with normal or deficiency DNA-dependent protein kinase activity?

A. maybe
B. yes
C. no
```

- Input example for open-ended questions:

```
hi doctor,i am chaitanya.age 28,from hyderabad.my problem is ....i got thyroid in my frist preganacy .my delivary date was on july 24th 2009 but on july 6th early morning around 7 oclock suddenly heany bleeding started and i rushed to the hospital but they could not save the baby(boy)...i lost my frist baby.then after 6 month i concevied again but doctors said that baby is having some heart problem and the sevarity of the problem can be known after the baby birth and i should go for a planned delivery.doctors did a c section on cotober 21 2010.doctors said that babys problem is not that serious but it is a heart problem so we need wait and see for 7 days.on 5th day the baby is dead.i want to know is their any problem in me that it is happing like this...do i need o go for any test before planning for next baby.i had 2 c section till now.what are the chances for me for the next baby.how long do i need to wait and plan for next preganacy.
```
```
Investigate the mechanistic implications of statins, primarily used for lipid modulation, on the immunomodulatory pathways, with an emphasis on delineating their therapeutic impact in the context of managing clinical outcomes for individuals afflicted with cardiovascular diseases, including a requirement to discuss the implications for atherosclerotic disease progression.
```


### Inference with vLLM

```python
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams

llm = LLM(model="TsinghuaC3I/Llama-3-8B-UltraMedical", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("TsinghuaC3I/Llama-3-8B-UltraMedical")
sampling_params = SamplingParams(temperature=0.7, top_p=0.9, max_tokens=1024, stop=["<|eot_id|>"])

messages = [
    {"role": "user", "content": """The question format used in the above input examples。"""},
]
prompts = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
print(prompts[0])
"""
<|begin_of_text|><|start_header_id|>user<|end_header_id|>

{question}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

"""

outputs = llm.generate(prompts=prompts, sampling_params=sampling_params)
print(outputs[0].outputs[0].text)
```

Note: This version of the model supports only single-turn dialog and has limited capabilities in multi-turn dialogue. We plan to enhance this in the next update.


## Evaluation Results

Llama-3-8B-UltraMedical achieved the best average results among 7B-level models on popular medical benchmarks, including MedQA, MedMCQA, PubMedQA, and MMLU-Medical. We would like to acknowledge Meta's remarkable Llama model, which served as an excellent base for our fine-tuning process.

| Released Date |                 Model                  | Average | MedQA | MedMCQA | PubMedQA | MMLU.ck | MMLU.mg | MMLU.an | MMLU.pm | MMLU.cb | MMLU.cm |
|:-------------:|:--------------------------------------:|:-------:|:-----:|:-------:|:--------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|    2024.04    | **Llama-3-8B-UltraMedical (Ensemble)** |  77.77  | 77.5  |  63.8   |   78.2   |  77.4   |  88.0   |  74.8   |  84.6   |  79.9   |  75.7   |
|    2024.04    |  **Llama-3-8B-UltraMedical (Greedy)**  |  75.20  | 73.3  |  61.5   |   77.0   |  78.9   |  78.0   |  74.1   |  83.8   |  78.5   |  71.7   |
|    2024.04    |              OpenBioLM-8B              |  72.48  | 59.0  |  56.9   |   74.1   |  76.1   |  86.1   |  69.8   |  78.2   |  84.2   |  68.0   |
|    2024.04    |     Llama-3-8B-Instruct (Ensemble)     |  71.23  | 62.4  |  56.5   |   75.8   |  72.5   |  84.0   |  71.1   |  70.6   |  80.6   |  67.6   |
|    2024.04    |      Llama-3-8B-Instruct (Greedy)      |  68.56  | 60.9  |  50.7   |   73.0   |  72.1   |  76.0   |  63.0   |  77.2   |  79.9   |  64.2   |
|    2024.04    |              Internist-7B              |  67.79  | 60.5  |  55.8   |   79.4   |  70.6   |  71.0   |  65.9   |  76.1   |    -    |  63.0   |
|    2024.02    |                Gemma-7B                |  64.18  | 47.2  |  49.0   |   76.2   |  69.8   |  70.0   |  59.3   |  66.2   |  79.9   |  60.1   |
|    2024.03    |         Meerkat-7B (Ensemble)          |  63.94  | 74.3  |  60.7   |    -     |  61.9   |  70.4   |  61.5   |  69.5   |  55.4   |  57.8   |
|    2023.03    |               MedAlpaca                |  58.03  | 41.7  |  37.5   |   72.8   |  57.4   |  69.0   |  57.0   |  67.3   |  65.3   |  54.3   |
|    2024.02    |             BioMistral-7B              |  57.26  | 46.6  |  45.7   |   68.1   |  63.1   |  63.3   |  49.9   |  57.4   |  63.4   |  57.8   |

In the table above:

- For MedQA, we use the 4 options from the US set. For MedMCQA, we use the Dev split. For PubMedQA, we use the reasoning required set.

- For MMLU, we include Clinical Knowledge (CK), Medical Genetics (MG), Anatomy (An), Professional Medicine (PM), College Biology (CB), and College Medicine (CM) to maintain consistency with previous studies.

- Greedy search is employed as our default decoding strategy. We denote ensemble scores with self-consistency as `(Ensemble)`. In our experiments, we conduct 10 decoding trials, and final decisions are made via majority vote (temperature=0.7, top_p=0.9).

- Partial results for 7B pre-trained models are sourced from the [Open Medical-LLM Leaderboard](https://huggingface.co/spaces/openlifescienceai/open_medical_llm_leaderboard).

## Training Details

<!-- Provide a longer summary of what this model is. -->

This model is trained using the full parameters and the Fully Sharded Data Parallel (FSDP) framework. 
The training process was performed on 8 x A6000 GPUs for about 50 hours.

Hyperparameters:

- torch type: bfloat16
- epochs: 3
- learning rate: 2e-5
- learning rate scheduler type: cosine
- warmup ratio: 0.04
- max length: 1024
- global batch size: 128

- **License:** [Meta Llama-3 License](https://llama.meta.com/llama3/license/).
- **Finetuned from model:** [Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B)
- **Finetuned on data:** [UltraMedical](https://github.com/TsinghuaC3I/UltraMedical)


## Limitations & Safe Use

While our model offers promising capabilities, it is crucial to exercise caution when using it in real-world clinical settings due to potential hallucination issues. Hallucinations, where the model generates incorrect or misleading information, can pose significant risks in clinical decision-making. Users are advised to validate the model's outputs with trusted medical sources and expert consultation to ensure safety and accuracy.

## Citation

```latex
@misc{UltraMedical,
  author = {Zhang, Kaiyan and Ding, Ning and Qi, Biqing and Zeng, Sihang and Li, Haoxin and Zhu, Xuekai and Chen, Zhang-Ren and Zhou, Bowen},
  title = {UltraMedical: Building Specialized Generalists in Biomedicine.},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/TsinghuaC3I/UltraMedical}},
}
```