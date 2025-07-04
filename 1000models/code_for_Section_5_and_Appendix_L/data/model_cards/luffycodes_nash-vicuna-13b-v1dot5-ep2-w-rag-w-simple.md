
# Nash Model Card

## Github details
Training of Nash (Economics) Model is based code for training the equivalent Spock (Biology) model.

Please checkout the repo: https://github.com/luffycodes/Tutorbot-Spock-Bio.

## Model details

**Model type:**
Nash is an open-source educational tutoring chatbot trained by fine-tuning LLaMA and Vicuna model on synthetic student-tutorbot conversations generated using a specialized prompt.

**Model date:**
Nash was trained between July 2023 and August 2023.

**Organizations developing the model:**
The Nash team with members from Rice University and OpenStax.

## Training dataset
700 conversations generated using a [specialized prompt](https://github.com/luffycodes/Tutorbot-Spock-Bio/blob/main/prompts/conversation_gen/v3.txt) from GPT-4 based on OpenStax Economics, Microeconomics, and Macroeconomics textbooks. 

**Paper or resources for more information:**
https://arxiv.org/abs/2305.13272

**Code or resources for more information:**
Training on Nash is based on:
https://github.com/luffycodes/Tutorbot-Spock-Bio

## Use Policy

Since the model is derivate of Llama model, please abide by Llama use policy [here](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf/blob/main/USE_POLICY.md)
and [Llama-Responsible-Use-Guide](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf/blob/main/Responsible-Use-Guide.pdf).

**Ethical Considerations, License and Limitations:**
Similarly, since the model is derivate of Llama model, same ethical considers, license and limitations as Llama apply.

**Out-of-scope Uses:** 
Similarly, use in any manner that violates applicable laws or regulations (including trade compliance laws).
Use in languages other than English. Use in any other way that is prohibited by the Acceptable Use Policy and Licensing Agreement for Llama 2.

"Llama 2 is a new technology that carries risks with use. Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios. For these reasons, as with all LLMs, Llama 2’s potential outputs cannot be predicted in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses to user prompts. Therefore, before deploying any applications of Llama 2, developers should perform safety testing and tuning tailored to their specific applications of the model."

## LLM Performance based on [huggingface LLM leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)

|||Average|ARC|HellaSwag|MMLU|TruthfulQA|
|---|---|---|---|---|---|---|
|this model (fine-tuned on vicuna-13b-v1.5)|13B|61.8 |59.13 |80.64 |56.12 | 51.29 |
|lmsys/vicuna-13b-v1.5|13B|61.63 |57.08 |81.24 |56.67 |51.51 |
|meta-llama/Llama-2-13b-chat-hf|13B|59.93|59.04|81.94|54.64|44.12|

If you use this work, please cite:
CLASS Meet SPOCK: An Education Tutoring Chatbot based on Learning Science Principles
https://arxiv.org/abs/2305.13272
```
@misc{sonkar2023class,
      title={CLASS Meet SPOCK: An Education Tutoring Chatbot based on Learning Science Principles}, 
      author={Shashank Sonkar and Lucy Liu and Debshila Basu Mallick and Richard G. Baraniuk},
      year={2023},
      eprint={2305.13272},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```