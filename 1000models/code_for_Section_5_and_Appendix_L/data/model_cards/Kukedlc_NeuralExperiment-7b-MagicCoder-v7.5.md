

# Datacard for Custom Trained Model
- Base Model : [Kukedlc/NeuralExperiment-7b-dare-ties](https://huggingface.co/Kukedlc/NeuralExperiment-7b-dare-ties)

  
## Model Description
This model is an experimental AI trained on three distinct datasets focusing on logical reasoning, mathematics, and programming. The training process involved fine-tuning from the last layer (31) backward with a gradually decreasing learning rate. The primary goal is to address and rectify the common 'INSTINST' bug observed in leaderboard models through targeted training on the latest layers.

## Datasets Used for Training
- `microsoft/orca-math-word-problems-200k`: A large-scale dataset of mathematical word problems aimed at enhancing the model's numerical reasoning and problem-solving capabilities.
- `ise-uiuc/Magicoder-Evol-Instruct-110K`: A dataset designed to improve code generation and understanding, contributing to the model's programming language proficiency.
- `sahil2801/CodeAlpaca-20k`: A dataset focused on programming challenges to further refine the model's coding and logical reasoning skills.

Each dataset contributed 20,000 data points to the training process, ensuring a balanced representation of logic, mathematics, and programming tasks.

## Training Environment
- The model was trained on Kaggle's free GPU environment, allowing for cost-effective fine-tuning and experimentation.
- Users interested in replicating or extending this training can find the Kaggle notebook in my profile or request it directly for collaborative purposes.

## Preliminary Results
- The model shows promising results in solving logical puzzles and mathematical problems, especially those with misleading or non-obvious solutions that it initially struggled with.
- Ongoing experiments aim to quantify the impact of targeted training on the model's reasoning capabilities across different domains.

## Invitation for Collaboration
- Feedback, suggestions, and collaborative efforts are highly encouraged to further refine and evaluate the model.
- If interested in contributing or experimenting with this model, please feel free to reach out or access the code directly from my Kaggle profile.

## Contact Information
- For any inquiries, suggestions, or collaboration proposals, please contact me!

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "Kukedlc/NeuralExperiment-7b-MagicCoder-v7"
messages = [{"role": "user", "content": "What is a large language model?"}]

tokenizer = AutoTokenizer.from_pretrained(model)
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

outputs = pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])
```

![Kukedlc/NeuralExperiment-7b-dare-ties](https://raw.githubusercontent.com/kukedlc87/imagenes/main/DALL%C2%B7E%202024-03-05%2000.28.41%20-%20Imagine%20a%20visual%20representation%20of%20a%20language%20model%20inspired%20by%20the%20Mandelbrot%20fractal.%20The%20scene%20should%20depict%20an%20abstract%2C%20intricate%20network%20resembl.webp)
