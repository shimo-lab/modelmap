
**delta v1.1 merge**  


# Vicuna Model Card

## Model details

**Model type:**
Vicuna is an open-source chatbot trained by fine-tuning LLaMA on user-shared conversations collected from ShareGPT.
It is an auto-regressive language model, based on the transformer architecture.

**Model date:**
Vicuna was trained between March 2023 and April 2023.

**Organizations developing the model:**
The Vicuna team with members from UC Berkeley, CMU, Stanford, and UC San Diego.

**Paper or resources for more information:**
https://vicuna.lmsys.org/

**License:**
Apache License 2.0

**Where to send questions or comments about the model:**
https://github.com/lm-sys/FastChat/issues

## Intended use
**Primary intended uses:**
The primary use of Vicuna is research on large language models and chatbots.

**Primary intended users:**
The primary intended users of the model are researchers and hobbyists in natural language processing, machine learning, and artificial intelligence.

## Training dataset
70K conversations collected from ShareGPT.com.

## Evaluation dataset
A preliminary evaluation of the model quality is conducted by creating a set of 80 diverse questions and utilizing GPT-4 to judge the model outputs. See https://vicuna.lmsys.org/ for more details.

## Major updates of weights v1.1
- Refactor the tokenization and separator. In Vicuna v1.1, the separator has been changed from `"###"` to the EOS token `"</s>"`. This change makes it easier to determine the generation stop criteria and enables better compatibility with other libraries.
- Fix the supervised fine-tuning loss computation for better model quality.