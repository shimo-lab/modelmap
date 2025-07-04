
---
## Developed by : 
* Changgil Song

## Model Number:
* k2s3_test_24001

## Base Model : 
* [meta-llama/Llama-2-13b-chat-hf](https://huggingface.co/meta-llama/Llama-2-13b-chat-hf)

### Training Data
* The model was trained on a diverse dataset comprising approximately 800 million tokens, including the Standard Korean Dictionary, KULLM training data from Korea University, dissertation abstracts from master's and doctoral theses, and Korean language samples from AI Hub.
* 이 모델은 표준대국어사전, 고려대 KULLM의 훈련 데이터, 석박사학위자 서지정보 논문초록, ai_hub의 한국어 데이터 샘플들을 포함하여 약 8억 개의 토큰으로 구성된 다양한 데이터셋에서 훈련되었습니다.

### Training Method
* This model was fine-tuned on the "meta-llama/Llama-2-13b-chat-hf" base model using PEFT (Parameter-Efficient Fine-Tuning) LoRA (Low-Rank Adaptation) techniques.
* 이 모델은 "meta-llama/Llama-2-13b-chat-hf" 기반 모델을 PEFT LoRA를 사용하여 미세조정되었습니다.

### Hardware and Software
* Hardware: Utilized two A100 (80G*2EA) GPUs for training.
* Training Factors: This model was fine-tuned using PEFT LoRA with the HuggingFace SFTtrainer and applied fsdp. Key parameters included LoRA r = 8, LoRA alpha = 16, trained for 2 epochs, batch size of 1, and gradient accumulation of 32.
* 이 모델은 PEFT LoRA를 사용하여 HuggingFace SFTtrainer와 fsdp를 적용하여 미세조정되었습니다. 주요 파라미터로는 LoRA r = 8, LoRA alpha = 16, 2 에폭 훈련, 배치 크기 1, 그리고 그라디언트 누적 32를 포함합니다.

### Caution 
* For fine-tuning this model, it is advised to consider the specific parameters used during training, such as LoRA r and LoRA alpha values, to ensure compatibility and optimal performance.
* 이 모델을 미세조정할 때는 LoRA r 및 LoRA alpha 값과 같이 훈련 중에 사용된 특정 파라미터를 고려하는 것이 좋습니다. 이는 호환성 및 최적의 성능을 보장하기 위함입니다.

### Additional Information
* The training leveraged the fsdp (Fully Sharded Data Parallel) feature through the HuggingFace SFTtrainer for efficient memory usage and accelerated training.
* 훈련은 HuggingFace SFTtrainer를 통한 fsdp 기능을 활용하여 메모리 사용을 효율적으로 하고 훈련 속도를 가속화했습니다.