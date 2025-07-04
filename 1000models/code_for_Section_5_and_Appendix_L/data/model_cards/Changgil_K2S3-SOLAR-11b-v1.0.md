
---
## Developed by : 
* K2S3

## Model Number:
* K2S3-SOLAR-11b-v1.0

## Base Model : 
* [upstage/SOLAR-10.7B-Instruct-v1.0](https://huggingface.co/upstage/SOLAR-10.7B-Instruct-v1.0)

### Training Data
* The training data for this model includes the Standard Korean Dictionary, training data from KULLM at Korea University, abstracts of master's and doctoral theses, and Korean language samples from AI Hub.
* 이 모델의 훈련 데이터에는 표준대국어사전, 고려대 KULLM의 훈련 데이터, 석박사학위 논문의 초록, 그리고 AI Hub의 한국어 데이터 샘플들이 포함됩니다.

### Training Method
* This model was fine-tuned on the "upstage/SOLAR-10.7B-Instruct-v1.0" base model using a full parameter tuning method with SFT (Supervised Fine-Tuning).
* 이 모델은 "upstage/SOLAR-10.7B-Instruct-v1.0" 기반 모델을 SFT를 사용하여 전체 파라미터 조정 방법으로 미세조정되었습니다.

### Hardware
* Hardware: Utilized two A100 (80G*2EA) GPUs for training.
* Training Factors: This model was fine-tuned with SFT, using the HuggingFace SFTtrainer and applied fsdp. Key training adjustments include the addition of new Korean tokens trained with the SentencePieceBPETokenizer, trained for 2 epochs, batch size of 1, and gradient accumulation of 32.
* 이 모델은 SFT를 사용하여 HuggingFace SFTtrainer와 fsdp를 적용하여 미세조정되었습니다. 주요 훈련 조정으로는 SentencePieceBPETokenizer로 훈련된 새로운 한글 토큰들을 추가, 2 에폭 훈련, 배치 크기 1, 그리고 그라디언트 누적 32를 포함합니다.