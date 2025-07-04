This is the [Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) model fine-tuned using QLoRA (4-bit precision) on my [claude_multi_instruct_1k](https://huggingface.co/datasets/Norquinal/claude_multi_instruct_1k) dataset.

## Prompt Format
The model was finetuned with the following prompt format:
```
Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{instruction}

### Response:
```

## Use in Text Generation Web UI
Install the bleeding-edge version of `transformers` from source:
```
pip install git+https://github.com/huggingface/transformers
```
Or, alternatively, change `model_type` in `config.json` from `mistral` to `llama`.

## Example Usage
>\### Instruction:
>Deconstruct five major technological innovations in 20th and 21st centuries—Internet, personal computing, mobile phones, artificial intelligence, and electric vehicles. For each innovation, provide information on their early origins, key inventors or pioneers, important milestones and breakthroughs, adoption and proliferation into mainstream use, economic effects, societal impact, ethical considerations, and potential future developments. Discuss how these innovations reshaped the way people work, communicate, and live, and explore the synergies or connections among these technologies and the potential for future transformative advancements.

>\### Response:
>Internet - The Internet was invented as a network of networks connecting computers at research institutions across the United States beginning in the late 1960s and early 1970s. Key individuals involved include Vint Cerf and Bob Kahn who developed TCP/IP protocols in the 1970s allowing different types of computers to connect over the Internet. In the 1980s, Tim Berners-Lee invented HTTP and HTML which laid the foundation for the World Wide Web. As the Internet grew, it revolutionized communication and commerce, enabling the rise of email, social media, ecommerce, and cloud computing. Today nearly half of the world's population has access to the Internet. While the Internet has brought immense benefits, there are also concerns about online privacy, misinformation, cybersecurity threats, and the impact on human interaction and attention spans. As AI becomes more capable, there will likely be new opportunities for intelligent systems to interact with the Internet and enhance its capabilities.
>
>Personal Computing - Personal computers were first envisioned by engineers like Alan Kay and Douglas Engelbart in the 1950s and 1960s. Steve Jobs and Steve Wozniak founded Apple Computer in 1976 with the release of the Apple I and II, while Bill Gates launched Microsoft in 1975. The IBM PC introduced the concept of compatible software and hardware platforms in 1981. Over time, personal computing became widespread through products from companies like Compaq, Dell, HP, and Acer. Desktop computers enabled productivity tools, video games, digital artistry, and online learning. Laptops made computing portable and ubiquitous. However, the environmental impacts of electronic waste from discarded devices need to be addressed. Future trends may involve more flexible, wearable computer interfaces that integrate with augmented reality and neural implants.   
>
>Mobile Phones - Martin Cooper of Motorola made the first mobile phone call in 1973. Nokia released the first commercially successful cellphone, the Mobira Senator, in 1982. By the mid-1990s, cellphones had become commonplace thanks to smaller handsets and affordable pricing plans. Smartphones combining voice calling with internet browsing and apps debuted in the early 2000s. Companies like Samsung, Apple, Google and Huawei have since transformed smartphones into indispensable devices for communication, entertainment, banking, navigation, and even healthcare. Mobile technology has helped bridge the digital divide and improve access to education and government services in developing countries. However, screen addiction, distraction and safety risks from texting and driving remain challenges. Innovations in foldable displays, flexible batteries, and wireless charging could lead to next generation designs.  
>
>Artificial Intelligence - Modern AI emerged from research in the 1940s by mathematicians and scientists including Turing, Shannon, von Neumann, McCarthy, and others. Deep learning algorithms based on neural networks took off in the 2010s thanks to advances in computing power, big data, and new architectures. Companies like Google, Amazon, Facebook and Microsoft have invested heavily in AI applications ranging from search engines to autonomous cars. Ethical concerns around transparency, bias and control of powerful AI systems will need to be addressed. Applications in medicine, manufacturing, logistics and transportation promise huge efficiency gains but may displace workers. Future directions include greater autonomy for robots, smarter virtual assistants, natural language processing, and machine reasoning.
>
>Electric Vehicles - Electric cars date back to the 1800s but faced range limitations compared to gasoline vehicles until the development of lithium-ion batteries in the 1990s. Tesla popularized all-electric vehicles starting in 2008 with the Roadster and Model S. Other automakers followed with hybrids and plug-in EVs. China has become the largest market due to government incentives and air pollution concerns. With continued cost reductions and improved battery technology, EVs could reach price parity with internal combustion engine (ICE) vehicles within a decade. However, issues around battery recycling, grid capacity and infrastructure investments need to be resolved. Autonomous driving technologies and shared mobility models could further boost the appeal of EVs.
>
>In summary, these five technologies have deeply altered our lives and created new possibilities, yet they come with tradeoffs and ethical dilemmas. Continued innovation and collaboration between industry, academia and governments will be needed to ensure these technologies fulfill their promises while minimizing unforeseen consequences.
>
>I hope this provides some helpful insights! Let me know if you would like me to expand on any specific points.
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Norquinal__Mistral-7B-claude-instruct)

| Metric                | Value                     |
|-----------------------|---------------------------|
| Avg.                  | 51.71   |
| ARC (25-shot)         | 63.23          |
| HellaSwag (10-shot)   | 84.99    |
| MMLU (5-shot)         | 63.84         |
| TruthfulQA (0-shot)   | 47.47   |
| Winogrande (5-shot)   | 78.14   |
| GSM8K (5-shot)        | 17.97        |
| DROP (3-shot)         | 6.35         |
