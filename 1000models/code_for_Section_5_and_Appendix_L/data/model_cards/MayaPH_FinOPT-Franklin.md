
# 🤗 FinOPT-Franklin
Released June 1, 2023

## Model Description
FinOPT-Franklin is a language model based on the OPT-1.3B architecture, which has been fine-tuned on a financial question-answering dataset. The model aims to provide accurate and informative responses to financial-related questions.

## FinOPT Series
The FinOPT series of language models come in various model sizes. Kindly refer to this Huggingface Hub [link](https://huggingface.co/models?search=mayaph/finopt) to see the other checkpoints of FinOPT.

| Model Name          | Parameter Size |
|---------------------|----------------|
| <b>FinOPT-Franklin</b>     | <b>1.3B</b>           |
| [FinOPT-Lincoln](https://huggingface.co/MayaPH/FinOPT-Lincoln)       | 350M           |
| [FinOPT-Washington](https://huggingface.co/MayaPH/FinOPT-Washington) | 125M          |

## Intended Use
FinOPT-Franklin is designed to assist users in obtaining relevant and reliable information about financial topics. It can be used as a tool for performing question-answering tasks in the financial domain, including banking queries, investment advice, and general financial inquiries.

The model is intended to be used by individuals seeking information about financial topics, as well as developers and researchers working on natural language processing (NLP) tasks in the financial domain.

## Usage
To use FinOPT-Franklin, you are required to provide attribution in accordance with the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) license. Please include the following attribution notice when utilizing FinOPT-Franklin in your work:

```python
# This code uses FinOPT-Franklin, a language model developed by Maya Philippines.
# The model is licensed under the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) license.
# For more information, visit: https://creativecommons.org/licenses/by-sa/4.0/

from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("MayaPH/FinOPT-Franklin")

model = AutoModelForCausalLM.from_pretrained("MayaPH/FinOPT-Franklin")
```

Please ensure that you include the relevant attribution notice in your code or any other form of usage to comply with the license terms.

## Limitations and Caveats
While FinOPT-Franklin has been fine-tuned on a financial question-answering dataset, it is important to note the following limitations and caveats:

1. **Domain-Specific Focus:** The model's training data primarily consists of financial questions and answers from the financial QA dataset. It may not perform as well on questions outside the financial domain.

2. **Potential Bias:** The model may reflect biases present in the training data. It is crucial to carefully evaluate and interpret the model's responses, particularly on sensitive topics such as investment advice or financial recommendations.

3. **Confidence and Verification:** The model generates responses based on patterns learned from the training data, but it does not have inherent fact-checking capabilities. Users should verify the information provided by the model from reliable sources before making any financial decisions.

## Training Data
FinOPT-Franklin was trained on a financial question-answering dataset, which consists of questions and answers related to various financial topics. The dataset was collected from online sources and financial forums, and manually handcrafted.

## Ethical Considerations
When using FinOPT-Franklin, it is important to consider the following ethical considerations:

1. **Privacy and Security:** Avoid sharing sensitive personal or financial information while interacting with the model. The model does not have privacy safeguards, so exercise caution when discussing personal or confidential matters.

2. **Fairness and Bias:** The model's responses may reflect biases present in the training data. Be aware of potential biases and make an effort to evaluate responses critically and fairly.

3. **Transparency:** The model operates as a predictive text generator based on patterns learned from the training data. The model's inner workings and the specific training data used are proprietary and not publicly available.

4. **User Responsibility:** Users should take responsibility

 for their own financial decisions and not solely rely on the information provided by the model. Consult with financial professionals or reliable sources for specific financial advice or recommendations.

## Further Information
For additional information or inquiries about FinOPT-Franklin, please contact the Maya Philippines iOps Team via jasper.catapang@maya.ph.

## Disclaimer
FinOPT-Franklin is an AI language model trained by Maya Philippines. It is provided "as is" without warranty of any kind, express or implied. The model developers and Maya Philippines shall not be liable for any direct or indirect damages arising from the use of this model.

## Acknowledgments
The development of FinOPT-Franklin was made possible by Maya Philippines and the curation and creation of the financial question-answering dataset.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_MayaPH__FinOPT-Franklin)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 25.54   |
| ARC (25-shot)         | 27.73          |
| HellaSwag (10-shot)   | 24.91    |
| MMLU (5-shot)         | 23.12         |
| TruthfulQA (0-shot)   | 52.4   |
| Winogrande (5-shot)   | 50.51   |
| GSM8K (5-shot)        | 0.0        |
| DROP (3-shot)         | 0.1         |
