
# dfurman/Llama-3-8B-Orpo-v0.1

![](https://raw.githubusercontent.com/daniel-furman/sft-demos/main/assets/llama_3.jpeg)

This is an ORPO fine-tune of [meta-llama/Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B) on 4k samples of [mlabonne/orpo-dpo-mix-40k](https://huggingface.co/datasets/mlabonne/orpo-dpo-mix-40k).

It's a successful fine-tune that follows the ChatML template!

## 🔎 Application

This model uses a context window of 8k. It was trained with the ChatML template.

## 🏆 Evaluation

### Open LLM Leaderboard

| Model ID                                                                                                                                                                                                                         |   Average |   ARC |   HellaSwag | MMLU  |   TruthfulQA |  Winogrande |  GSM8K  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------: | --------: | --------: | ---------: | --------: |  --------: |  --------: |
| [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) [📄](https://huggingface.co/datasets/open-llm-leaderboard/details_meta-llama__Meta-Llama-3-8B-Instruct)    |       66.87 |     60.75 |     78.55 |      67.07 |     51.65 |     74.51 |     68.69 |
| [**dfurman/Llama-3-8B-Orpo-v0.1**](https://huggingface.co/dfurman/Llama-3-8B-Orpo-v0.1) [📄](https://huggingface.co/datasets/open-llm-leaderboard/details_dfurman__Llama-3-8B-Orpo-v0.1)                     | **64.67** | **60.67** | **82.56** | **66.59** | **50.47** |     **79.01** |     **48.75** |
| [meta-llama/Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B) [📄](https://huggingface.co/datasets/open-llm-leaderboard/details_meta-llama__Meta-Llama-3-8B)                               |     62.35 |      59.22 |     82.02 |      66.49 |      43.95 |     77.11 |     45.34 |


## 📈 Training curves

You can find the experiment on W&B at [this address](https://wandb.ai/dryanfurman/huggingface/runs/uvr916mv?nw=nwuserdryanfurman).

## 💻 Usage

<details>

<summary>Setup</summary>

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

if torch.cuda.get_device_capability()[0] >= 8:
    !pip install -qqq flash-attn
    attn_implementation = "flash_attention_2"
    torch_dtype = torch.bfloat16
else:
    attn_implementation = "eager"
    torch_dtype = torch.float16

model = "dfurman/Llama-3-8B-Orpo-v0.1"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    model_kwargs={
        "torch_dtype": torch_dtype,
        "device_map": "auto",
        "attn_implementation": attn_implementation,
    }
)
```

</details>

### Run

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me a recipe for a spicy margarita."},
]
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
print("***Prompt:\n", prompt)

outputs = pipeline(prompt, max_new_tokens=1000, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print("***Generation:\n", outputs[0]["generated_text"][len(prompt):])
```

<details>

<summary>Output</summary>

```
"""***Prompt:
 <|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
Tell me a recipe for a spicy margarita.<|im_end|>
<|im_start|>assistant

***Generation:
 Sure! Here's a recipe for a spicy margarita:

Ingredients:

- 2 oz silver tequila
- 1 oz triple sec
- 1 oz fresh lime juice
- 1/2 oz simple syrup
- 1/2 oz fresh lemon juice
- 1/2 tsp jalapeño, sliced (adjust to taste)
- Ice cubes
- Salt for rimming the glass

Instructions:

1. Prepare the glass by running a lime wedge around the rim of the glass. Dip the rim into a shallow plate of salt to coat.
2. Combine the tequila, triple sec, lime juice, simple syrup, lemon juice, and jalapeño slices in a cocktail shaker.
3. Add ice cubes to the cocktail shaker and shake vigorously for 30 seconds to 1 minute.
4. Strain the cocktail into the prepared glass.
5. Garnish with a lime wedge and jalapeño slice.

Enjoy! This spicy margarita has a nice balance of sweetness and acidity, with a subtle heat from the jalapeño that builds gradually as you sip."""
```
</details>
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_dfurman__Llama-3-8B-Orpo-v0.1)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |11.01|
|IFEval (0-Shot)    |30.00|
|BBH (3-Shot)       |13.77|
|MATH Lvl 5 (4-Shot)| 3.78|
|GPQA (0-shot)      | 1.57|
|MuSR (0-shot)      | 2.73|
|MMLU-PRO (5-shot)  |14.23|

