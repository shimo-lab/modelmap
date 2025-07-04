**The license is `cc-by-nc-sa-4.0`.**  
  
# **🐻‍❄️You_can_cry_Snowman-13B🐻‍❄️**  
![img](https://drive.google.com/uc?export=view&id=11c1FV1hKPXriGJRVhNDN-9up0wMF9QZk)  



## Model Details

**Model Developers** Seungyoo Lee(DopeorNope)

I am in charge of Large Language Models (LLMs) at Markr AI team in South Korea.

**Input** Models input text only.

**Output** Models generate text only.

**Model Architecture**  
You_can_cry_Snowman-13B is an auto-regressive language model based on the SOLAR architecture.

---

## **Base Model**  

[kyujinpy/Sakura-SOLAR-Instruct](https://huggingface.co/kyujinpy/Sakura-SOLAR-Instruct)   

[Weyaxi/SauerkrautLM-UNA-SOLAR-Instruct](https://huggingface.co/Weyaxi/SauerkrautLM-UNA-SOLAR-Instruct)   


## **Implemented Method**

I have merged two models by increasing the parameter size to create a larger model.

I wanted to check how much the performance of the SOLAR base model changes when the scale of the parameters is increased.

---
  
# Implementation Code


## Load model
```python

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

repo = "DopeorNope/You_can_cry_Snowman-13B"
OpenOrca = AutoModelForCausalLM.from_pretrained(
        repo,
        return_dict=True,
        torch_dtype=torch.float16,
        device_map='auto'
)
OpenOrca_tokenizer = AutoTokenizer.from_pretrained(repo)
```


---