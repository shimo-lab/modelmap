
> [!WARNING]
> This model checkpoint is provided as-is and might not be up-to-date. Please use the corresponding version from https://huggingface.co/mistralai org

Conversion process:

1. Download original weights from https://models.mistralcdn.com/mistral-7b-v0-2/mistral-7B-v0.2.tar
2. Convert with https://github.com/huggingface/transformers/blob/main/src/transformers/models/mistral/convert_mistral_weights_to_hf.py
3. You may need to copy the tokenizer.model from Mistral-7B-Instruct-v0.2 repo.