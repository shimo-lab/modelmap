

# Gemma 7B OpenHermes v0.80

- Eval  Loss: `0.4544`
- Train Loss: `0.3129`
- lr: `5e-5`
- optimizer: adamw
- lr_scheduler_type: cosine

## Model Details

This is an instruction-following model finetuned from the Gemma 1.1 7B model. It was finetuned on the OpenHermes-2.5 dataset to improve its ability to engage in open-ended conversation and respond helpfully to user instructions and queries. The model can engage in dialogue, answer questions, and assist with a variety of tasks.

### Model Description

- **Developed by:** `lemon-mint`
- **Model type:** Gemma
- **Language(s) (NLP):** English
- **License:** [gemma-terms-of-use](https://ai.google.dev/gemma/terms)
- **Finetuned from model:** [google/gemma-1.1-7b-it](https://huggingface.co/google/gemma-1.1-7b-it)

# Limitations and Ethical Considerations

As Gemma 7B OpenHermes has been trained on extensive web data, biases present in the training data may be reflected in the model. Additionally, there is a possibility that it may generate sentences containing errors or incorrect information. Therefore, rather than blindly trusting the model's output, it is necessary to refer to it with caution.