
> 🚧 Note: this repo is under construction, current uploaded version is based on KoRWKV-6B, ~28Billion tokens trained ckpt 🚧

# 🐧 KoAlpaca-KoRWKV-6B (v1.1a)

This model is a fine-tuned version of [beomi/KoRWKV-6B](https://huggingface.co/beomi/KoRWKV-6B) on an [KoAlpaca v1.1a Dataset](https://huggingface.co/datasets/beomi/KoAlpaca-v1.1a).

Detail Codes are available at [KoAlpaca Github Repository](https://github.com/Beomi/KoAlpaca)

## Generation Code

### Install Requirements

```bash
pip install -U transformers tokenizers accelerate safetensors
```

### Generation Code with HF pipeline

```python
from transformers import pipeline

pipe = pipeline('text-generation', model='beomi/KoAlpaca-KoRWKV-6B', device=0)

def gen(x):
    a = pipe(
        f'### 질문: {x}\n\n### 답변:', 
        max_new_tokens=1024, 
        return_full_text=False, 
        do_sample=True,
        top_p=0.9,
        temperature=0.7,
        early_stopping=True,
        repetition_penalty=1.2,
    )
    print(a[0]['generated_text'])
```

### Generated Samples

```
gen("오늘 기분은 좀 어때?")

 오늘은 기분이 좋은 날입니다. 왜냐하면, 오늘은 기쁜 일이 생길 수 있는 날이니까요! 
1. 아침에 일찍 일어나서 기분 좋았습니다. 2. 맛있는 음식을 먹어서 기분이 좋습니다. 3. 수업시간에 열심히 들어서 기분이 좋습니다. 4. 친구가 생일 선물을 줘서 기분이 좋습니다. 5. 내일이 토요일이라서 기분이 좋습니다. 6. 숙제를 해서 기분이 좋습니다. 7. 부모님께서 생일 축하 노래를 불러줘서 기분이 좋습니다. 8. 방 청소를 해서 기분이 좋습니다. 9. 맛있는 과자를 먹어서 기분이 좋습니다. 10. 오늘 날씨를 보니 비가 안와서 기분이 좋습니다. 11. 부모님이 나를 사랑해주셔서 기분이 좋습니다. 12. 부모님과 함께 외식을 해서 기분이 좋습니다. 13. 친구랑 같이 놀아서 기분이 좋습니다. 14. 공부를 해서 기분이 좋습니다. 15. 숙제를 잘 해서 기분이 좋습니다. 16. 맛있는 음식을 먹어서 기분이 좋습니다. 17. 친구들과 어울려 놀아서 기분이 좋습니다. 18. 내가 좋아하는 책을 읽어서 기분이 좋습니다. 19. 오늘 하루 종일 기분이 좋습니다. 20. 엄마와 아빠가 나를 사랑해 주셔서 기분이 좋습니다.
```

```
gen("칸트의 정언명령에 따른다는 점이 일반적인 선함과 다른 이유가 뭐야?")

 칸트는 도덕의 법칙을 두 가지로 구분했습니다. 첫 번째 법칙은 '정언명령'으로, 이 법칙은 어떤 상황에서든 절대적으로 지켜야 하는 보편적인 법칙입니다. 이에 따라 칸트는 "이성이 명령한 대로 행동하라"는 원칙을 제시했습니다. 
두 번째 법칙은 "모든 인간은 평등하게 태어났고, 창조주로부터 양도할 수 없는 권리를 부여받았다"는 것입니다. 이 원칙에는 모든 인간이 평등하고, 모든 인간은 동등하게 존중받아야 한다는 의미가 담겨 있습니다. 이러한 칸트의 도덕 법칙을 따르면, 선함과 악함은 상황에 따라 다르게 적용될 수 있습니다. 예를 들어, 범죄자나 장애인 등 특별한 상황에서는 선이 될 수 있는 상황이 존재합니다.
```

```
gen("다음 글을 영어로 번역해주세요. 영어 문장: 'She looks handsome.' 번역 한글 문장:")

 "She looks handsome."은 직역하면 "그녀는 잘생겨 보입니다"라는 뜻이지만, 한국어로는 "그녀는 아름다워 보입니다"로 해석됩니다. 이 문장은 원래 'The saddest thing'이라는 영화의 OST 가사 중 일부분입니다. 이 영화는 제인 폰다가 주연을 맡은 작품으로, 그녀가 매력적인 미모와 몸매를 가지고 있지만 불행한 삶을 사는 여성의 모습을 그리고 있습니다. 따라서 그녀는 아름답지만 불행해보이는 모습이라는 의미에서 사용되었습니다.
```

```
gen("서울이 인기있는 도시인 이유는?")

 서울은 많은 사람들이 거주하고 있는 대도시이기 때문입니다. 또한, 다른 나라에서는 서울보다 더 큰 대도시들이 많이 있지만, 수도가 서울에 위치한 나라는 없습니다. 이는 서울의 도시 규모가 크고 교통과 통신 등 인프라가 잘 구축되어 있기 때문입니다. 
 추가 설명: 
서울의 인구나 유동인구 등을 살펴보면, 서울을 방문하는 외국인 관광객도 매우 많습니다. 이러한 이유로 서울은 한국 내에서 가장 인기 있는 도시 중 하나로 자리잡고 있습니다.
```

```
gen("칸트 철학의 예시를 들고, 해당 철학이 가지는 의의를 3가지 알려줘.")

 칸트는 인간의 지식을 경험론적 입장에서 분석하고 종합하여 도덕철학을 정립하였습니다. 이 과정에서 그는 모든 인간은 이성을 가지고 있으며, 도덕법칙을 인식할 수 있다고 보았습니다. 이러한 인간 이성의 기능을 통해, 칸트는 '실천이성'과 '판단력'을 중시합니다. 즉, 이성적으로 판단하여 올바른 판단을 내릴 수 있는 능력이 인간에게는 있다는 것입니다. 또한, 칸트는 인간이 가진 선천적인 관념론적 사고방식을 거부하고, 경험을 통한 실천적인 사고방식으로서의 이성을 강조합니다. 
 추가 설명:
칸트의 철학은 형이상학, 인식론, 윤리학, 정치학 등 다양한 분야에서 영향을 미치고 있습니다. 특히, 그는 경험론과 합리론의 대립으로 인해 분열된 유럽의 사상계를 통합하여 새로운 철학을 제시하고자 노력하였습니다. 이를 통해 근대 철학에 큰 영향을 주었으며, 현재는 그 영향력이 여전히 유지되고 있습니다.
```

```
gen("리튬이온전지에서 발생하는 화학 현상을 화학식을 기반으로 자세히 설명해주세요.")

 리튬이온전지는 양극과 음극 사이에 있는 분리막을 통해 이온이 이동하면서 충전과 방전을 하는 원리로 작동합니다. 따라서, 전극의 반응에 의해 화학 반응이 일어납니다. 
1. 리튬이온전지 내부에는 리튬이온들이 이동하기 위한 통로가 있는데, 이를 전해질이라고 합니다. 즉, 액체 전해질을 채우고 있는 이온들의 농도 차이 때문에 전극에서 전자가 이동하는 것입니다. 이때 전해질은 물질이 아닌 화학반응을 일으키는 역할을 합니다. 2. 음극은 전자를 받아 이온으로 생성하는 부분입니다. 3. 음극에서는 산화 환원 반응을 통해 전자와 수소 이온이 이동하며, 이를 통해 전기가 발생합니다. 4. 전자는 음극에서 양극으로 이동하며, 이는 전자의 흐름이며, 이를 통해 전류가 흐르게 됩니다. 5. 전자는 양극에서 음극으로 이동하는데, 이는 전자가 전자이동을 하면서 발생한 운동에너지로 인해 발생합니다. 6. 전기적으로 가장 안정된 상태인 리튬이온은 가장 높은 온도(약 700도)에서도 잘 견딜 수 있습니다.
```

```
gen("투자 초심자가 하기 좋은 선물 투자 종류를 알려주세요.")

 주식, 채권, 금, 원유 등 다양한 상품이 있습니다. 
1. 주식 (주식투자) - 장기적인 관점에서 투자할 때 적합한 상품입니다.
2. 금 (금투자) - 안전한 투자를 원하는 사람에게 좋습니다.
3. 원유 (원자재투자) - 안정적인 수익과 가격 변동성이 적습니다.
4. 부동산 (부동산투자) - 인플레이션이 발생하는 시기에 가장 적합한 투자 방법 중 하나입니다.
5. 보험 (보험투자) - 보장자산에 대한 니즈가 있는 사람에게 적합한 상품입니다.
```


## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1.0
- mixed_precision_training: Native AMP
- Trained on 1x H100(80G PCI-E) GPU

### Framework versions

- Transformers 4.29.2
- Pytorch 1.13.1
- Datasets 2.12.0
- Tokenizers 0.13.3