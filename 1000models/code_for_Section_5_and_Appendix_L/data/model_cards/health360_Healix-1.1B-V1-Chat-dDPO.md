# Healix 1.1B Model Card

## Model Description
Healix 1.1B is a state-of-the-art large language model specifically designed for medical applications. With 1.1 billion parameters, it has been trained on a vast corpus of medical literature to provide accurate and reliable responses to complex medical queries. This model aims to assist healthcare professionals and researchers by offering insights derived from medical data.

## Training Data
The model leverages an extensive compilation of medical literature, including research papers, clinical trial reports, and textbooks, ensuring a broad understanding of medical topics.

## Intended Use
This model is designed for medical research, clinical support, and healthcare applications. It serves to enhance medical text generation, query response, and evidence-based information dissemination. It is not a substitute for professional medical consultation.
## Limitations
While Healix 1.1B offers advanced medical insights, it has limitations in data quality and representativeness, and may inadvertently produce biased or incorrect information.
## Performance
Healix 1.1B demonstrated a remarkable accuracy of 64%, outperforming the LLAMA 2 7B model, which achieved an accuracy of 62% despite its larger size of 7 billion parameters. This highlights Healix 1.1B's superior ability to handle real emergency-focused medical questions, showcasing the effectiveness of specialized training and architecture in domain-specific applications.
## Ethical Considerations
Users are urged to use Healix 1.1B responsibly, considering the ethical implications, patient privacy, and data security. The model's outputs should be used as a supplementary information source alongside professional medical judgment.

## Papers
Details on the development, training, and evaluation of Healix 1.1B will be available in our forthcoming publications, offering insights into its creation and the advancements it brings to medical informatics.

### Input Format
Use the Alpaca model format.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_health360__Healix-1.1B-V1-Chat-dDPO)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |33.00|
|AI2 Reasoning Challenge (25-Shot)|30.55|
|HellaSwag (10-Shot)              |44.78|
|MMLU (5-Shot)                    |24.64|
|TruthfulQA (0-shot)              |41.55|
|Winogrande (5-shot)              |56.51|
|GSM8k (5-shot)                   | 0.00|

