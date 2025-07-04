
## SOLAR-10B-OrcaDPO-Jawade

### Overview
This model card is instruction finetuned version of `upstage/SOLAR-10.7B-Instruct-v1.0` model. Trained on the Intel DPO Orca dataset using LoRA. Though it should be noted SOLAR-10.7B paper states that the 
original model for alignment was trained on Intel ORCA DPO pairs. Retraining using DPO and LoRA shows slight (<1%) improvement on OpenLLM Leaderboard benchmarks against `SOLAR 10.7B-Instruct` and significant over `SOLAR 10.7B`

![model_card_image](SOLAR_ORCA.png)

## How to Use This Model

To use the model `bhavinjawade/SOLAR-10B-OrcaDPO-Jawade`, follow these steps:

1. **Import and Load the Model and Tokenizer**
   Begin by importing the model and tokenizer. Load them using the `from_pretrained` method.

   ```python
   from transformers import AutoModelForCausalLM, AutoTokenizer
   model = AutoModelForCausalLM.from_pretrained("bhavinjawade/SOLAR-10B-OrcaDPO-Jawade")
   tokenizer = AutoTokenizer.from_pretrained("bhavinjawade/SOLAR-10B-OrcaDPO-Jawade")
   ```

2. **Format the Prompt**
Format the chat input as a list of messages, each with a role ('system' or 'user') and content.

    ```python
    message = [
        {"role": "system", "content": "You are a helpful assistant chatbot."},
        {"role": "user", "content": "Is the universe real? or is it a simulation? whats your opinion?"}
    ]
    prompt = tokenizer.apply_chat_template(message, add_generation_prompt=True, tokenize=False)
    ```

3. **Create a Pipeline**
Set up a pipeline for text generation with the loaded model and tokenizer.

    ```python
    pipeline = transformers.pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer
    )
    ```

4. **Generate Text**
Use the pipeline to generate a sequence of text based on the prompt. You can adjust parameters like temperature and top_p for different styles of responses.

   ```python
   sequences = pipeline(
         prompt,
         do_sample=True,
       temperature=0.7,
          top_p=0.9,
          num_return_sequences=1,
          max_length=200,
      )
    print(sequences[0]['generated_text'])
    ```

This setup allows you to utilize the capabilities of the **bhavinjawade/SOLAR-10B-OrcaDPO-Jawade** model for generating responses to chat inputs.

### License
- **Type**: MIT License
- **Details**: This license permits reuse, modification, and distribution for both private and commercial purposes under the terms of the MIT License.

### Model Details
- **Model Name**: SOLAR-10.7B-Instruct-v1.0
- **Organization**: Upstage
- **Training Dataset**: Intel/orca_dpo_pairs
- **Technique Used**: LoRA (Low-Rank Adaptation)

### Contact Information
- https://bhavinjawade.github.io