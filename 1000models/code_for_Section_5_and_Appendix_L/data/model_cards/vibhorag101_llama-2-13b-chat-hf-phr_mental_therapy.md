# Model Card

<!-- Provide a quick summary of what the model is/does. -->
- This model is a finetune of the **llama-2-13b-chat-hf** model on a therapy dataset.
- The model aims to provide basic therapy to the users and improve their mental health until they seek professional help.
- The model has been adjusted to encourage giving cheerful responses to the user. The system prompt has been mentioned below.

## Model Details
### Training Hardware
- RTX A5000 24GB
- 48 Core Intel Xeon
- 128GB Ram.
### Model Hyperparameters
- This [training script](https://github.com/phr-winter23/phr-mental-chat/blob/main/finetuneModel/finetuneScriptLLaMA-2.ipynb) was used to do the finetuning.
- The shareGPT format dataset was converted to llama-2 training format using this [script](https://github.com/phr-winter23/phr-mental-chat/blob/main/finetuneModel/llamaDataMaker.ipynb).
- num_train_epochs = 2
- per_device_train_batch_size = 2
- per_device_eval_batch_size = 2
- gradient_accumulation_steps = 1
- max_seq_length = 4096
- lora_r = 64
- lora_alpha = 16
- lora_dropout = 0.1
- use_4bit = True
- bnb_4bit_compute_dtype = "float16"
- bnb_4bit_quant_type = "nf4"
- use_nested_quant = False
- fp16 = False
- bf16 = True
- Data Sample: 1000 (80:20 split)

### Model System Prompt
You are a helpful and joyous mental therapy assistant. Always answer as helpfully and cheerfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content.Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.

#### Model Training Data

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64eb1e4a55e4f0ecb9c4f406/x298HbUKHrom-RFmNgSbH.png)

### Model Benchmarks
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_vibhorag101__llama-2-13b-chat-hf-phr_mental_therapy)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 42.5   |
| ARC (25-shot)         | 38.82          |
| HellaSwag (10-shot)   | 72.76    |
| MMLU (5-shot)         | 23.12         |
| TruthfulQA (0-shot)   | 46.92   |
| Winogrande (5-shot)   | 65.59   |
| GSM8K (5-shot)        | 7.81        |