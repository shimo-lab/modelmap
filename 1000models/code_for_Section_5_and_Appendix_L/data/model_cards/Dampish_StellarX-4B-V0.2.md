# StellarX: A Base Model by Dampish and Arkane

StellarX is a powerful autoregressive language model designed for various natural language processing tasks. It has been trained on a massive dataset containing 810 billion tokens(trained on 300B tokens), trained on "redpajama," and is built upon the popular GPT-NeoX architecture. With approximately 4 billion parameters, StellarX offers exceptional performance and versatility.

## Model Details

- **Training Data:** StellarX is trained on a large-scale dataset provided by "redpajama" maintained by the group "togethercumputer." This dataset has been instrumental in shaping StellarX's language capabilities and general-purpose understanding.
- **Model Architecture:** StellarX is built upon the GPT-NeoX architecture, which may, be, inspired by GPT-3 and shares similarities with GPT-J-6B. The architecture incorporates key advancements in transformer-based language models, ensuring high-quality predictions and contextual understanding.
- **Model Size:** StellarX consists of approximately 4 billion parameters, making it a highly capable language model for a wide range of natural language processing tasks.
- **Carbon-Friendly and Resource-Efficient:** StellarX has been optimized for carbon efficiency and can be comfortably run on local devices. When loaded in 8 bits, the model requires only about 5GB of storage, making it more accessible and convenient for various applications.
- **V0.2** Meaning what version it is on, currently version 0.2, Assume version 0.2 has only been trained on 300B tokens and the goal is 810B tokens. The next version aims to have a way higher accuracy.

## How to Use

To load StellarX using the Hugging Face Transformers library, you can use the following code snippet:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("Dampish/StellarX-4B-V0")
model = AutoModelForCausalLM.from_pretrained("Dampish/StellarX-4B-V0")
```

This model is particularly beneficial for those seeking a language model that is powerful, compact, and can be run on local devices without a hefty carbon footprint. Remember, when considering Darius1, it's not just about the impressive numbers—it's about what these numbers represent: powerful performance, optimized resources, and responsible computing.

**For any queries related to this model, feel free to reach out to "Dampish#3607" on discord.**

## Licensing and Usage
StellarX, developed by the Dampish, is made available under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC-BY-NC-SA-4.0). This license ensures that you can utilize the model for research purposes and personal use without any restrictions, while also promoting the sharing and adaptation of the model under certain conditions.

# Research and Personal Use
StellarX can be freely used for research purposes, allowing you to explore its capabilities, conduct experiments, and develop novel applications. Whether you're a student, researcher, or hobbyist, the model's availability under the CC-BY-NC-SA-4.0 license empowers you to unlock the potential of StellarX for your own non-commercial projects.

# Commercial Usage
For commercial usage of StellarX, an additional licensing arrangement must be established. If you intend to leverage the model for any commercial purpose, such as integrating it into a product or service, you are required to reach an agreement with the Dampish. This agreement will specify the terms, including the agreed-upon percentage or licensing fee to be paid for the commercial use of StellarX.

To initiate discussions regarding commercial usage, please contact Dampish through the designated channels mentioned earlier. They will be able to provide you with further information and guide you through the process of establishing a licensing arrangement tailored to your specific requirements.

# Importance of Licensing Compliance
It is crucial to respect the licensing terms to ensure the fair usage and continued development of StellarX. The revenue generated from commercial licensing supports the efforts of the Dampish in advancing the model and making it more widely accessible.

# Note on CC-BY-NC-SA-4.0
Under the CC-BY-NC-SA-4.0 license, you are allowed to modify and adapt StellarX, incorporating it into your own projects. However, any derivative work or modifications should also be shared under the same license terms, ensuring the continued openness and collaborative spirit of the project.

Please review the complete text of the CC-BY-NC-SA-4.0 license to familiarize yourself with its provisions and requirements. It is essential to comply with the terms of the license to respect the intellectual property rights and contributions of the Dampish and the wider community involved in developing StellarX.
## GPT-NeoX and Model Selection

GPT-NeoX-20B, a sibling model to StellarX, is a 20 billion parameter autoregressive language model trained on the Pile using the GPT-NeoX library. StellarX draws inspiration from the architectural advancements and performance of GPT-NeoX models. While the specifics of StellarX's architecture and parameters may differ, it benefits from the proven capabilities of GPT-NeoX and its suitability for diverse natural language processing tasks.

## Training and Evaluation

StellarX's training dataset comprises a comprehensive collection of English-language texts, covering various domains, thanks to the efforts of "redpajama" dataset by the group "togethercumputer" group.

Evaluation of GPT-NeoX 20B performance has demonstrated its competence across different natural language tasks. Although since this description provides a brief summary, we refer to the GPT-NeoX Paper https://arxiv.org/abs/2204.06745, comparing GPT-NeoX 20B to other models on tasks such as OpenAI's LAMBADA, SciQ, PIQA, TriviaQA, and ARC Challenge.

## Limitations and Considerations

StellarX, like its sibling models, is intended primarily for research purposes. It provides a powerful foundation for extracting useful features and insights from the English language. While StellarX can be further fine-tuned and adapted for deployment, users should conduct their own risk and bias assessments before using it as a basis for downstream tasks.

It's important to note that StellarX is not intended for direct deployment without supervision. It is not designed for human-facing interactions, unlike models like ChatGPT, which have been fine-tuned using reinforcement learning from human feedback to better understand human instructions and dialogue.

Furthermore, StellarX is not limited to the English language if trained properly and can sometimes be used for translation aswell as text generation in other languages.

Lastly, users should be aware of potential biases and limitations inherent in

Special thanks to the group that created the training dataset. The Redpajama dataset, used to train StellarX, thank you togethercumputer.

## Community and Support

To inquire about StellarX and receive support, you can join the Dampish's 
server and engage in discussions in the #questions channel. It is recommended to explore the existing documentation and resources available for GPT-NeoX-20B to familiarize yourself with the model before seeking assistance on. For better information about GPT-NeoX, you can reach out to eleutherAI.

## Summary

StellarX, a base language model developed by the Dampish, offers impressive language capabilities and flexibility. Trained on an extensive dataset and built upon the GPT-NeoX architecture, StellarX excels in various natural language processing tasks. Its carbon-friendly and resource-efficient design makes it accessible for local device deployment. Researchers and enthusiasts can freely explore StellarX for research purposes and personal use, while commercial users should adhere to the licensing terms.

**Again i am really grateful for the data made by togethercumputers and their willingness to opensource, they inspired this project and sparked the idea in Stellar-models, i am truly really really grateful to them.
-dampish**



Discord: https://discord.gg/vasyNnUa  
OR Reach out to me personally on Discord via the username: Dampish#3607

Thank you for your time.



