
## LLama3 Tabanlı Türkçe Dil Modeli: aerdincdal/CBDDO-LLM-8B-Instruct-v1

**aerdincdal/CBDDO-LLM-8B-Instruct-v1**, LLama3 mimarisi üzerine kurulu ve 2.5 milyon satırlık veri kümesi ile özelleştirilmiş Instruction Tune yöntemi kullanılarak eğitilmiş bir Türkçe dil modelidir. Bu model, doğal dil işleme alanında çeşitli görevleri etkili bir şekilde gerçekleştirebilir. Modelin eğitimi, Türkçe dilbilgisi ve sentaks kurallarını derinlemesine kavramasını sağlamış, böylece akıcı ve doğru metinler üretmesine olanak tanımıştır.

**Modelin Öne Çıkan Özellikleri:**

- **Gelişmiş LLama3 Mimarisi:** Bu mimari, doğal dil işleme modelleri için son derece etkili ve yenilikçi bir temel oluşturur.
- **Kapsamlı Veri Seti ile Eğitim:** Model, 2.5 milyon satırlık veri seti kullanılarak eğitilmiştir, bu da onun dil yapısını ve nüanslarını mükemmel bir şekilde öğrenmesini sağlar.
- **Yüksek Performans:** Model, karmaşık dil işleme görevlerini hızlı ve etkin bir şekilde gerçekleştirebilir.
- **Çok Yönlülük:** Metin oluşturma, çeviri, soru-cevap, özetleme ve kod yazma gibi çok çeşitli görevlerde başarılıdır.

### Modelin Kullanım Adımları:

1. **Gerekli Kütüphaneleri Yükleyin:**
   ```bash
   pip install transformers
   ```

2. **Modeli Test Edin:**
```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer, pipeline
import torch

model_id = "aerdincdal/CBDDO-LLM-8B-Instruct-v1"

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,  
    device_map="auto",           
    trust_remote_code=True       
)

tokenizer = AutoTokenizer.from_pretrained(
    model_id,
    trust_remote_code=True       
)

streamer = TextStreamer(tokenizer)

text_generation_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    model_kwargs={"torch_dtype": torch.bfloat16},  
    streamer=streamer
)

messages = [
    {"role": "system", "content": "Her zaman düşünceli yanıtlar veren bir chatbot'sun."},
    {"role": "user", "content": "Mona Lisa tablosu hakkında ne düşünüyorsun?"}
]

prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

terminators = [
    tokenizer.eos_token_id
]

outputs = text_generation_pipeline(
    prompt,
    max_new_tokens=2048,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.95
)

print(outputs[0]["generated_text"][len(prompt):])
```

**Çıktı:**

```
1503'te Leonardo da Vinci tarafından resmedilen Mona Lisa, 16. yüzyılda Avrupa'da resim sanatının en ünlü eserlerinden biridir. Eski bir İtalyan aristokratı olan Lisa del Giocondo'ya benzeyen bir kadın portresidir. Bu tablo, Leonardo da Vinci'nin en ünlü eserlerinden biri olarak kabul edilir ve sanatın en iyi örneklerinden biri olarak kabul edilir. Mona Lisa'nın önemi, resim sanatının gelişiminde ve sanat tarihi boyunca etkisinin büyüklüğüne dayanmaktadır.
```

### Modelin Çeşitli Kullanım Alanları:

- **Metin Oluşturma:** Çeşitli türde ve tonda metinler oluşturabilirsiniz.
- **Metin Çevirme:** Çok dilli çeviri yetenekleri ile metinleri başka dillere çevirebilir veya tercüme edebilirsiniz.
- **Soruları Yanıtlama:** Her türlü soruyu, hatta en zorlayıcı olanları bile yanıtlayabilir.
- **Özetleme:** Uzun metinleri kısa ve öz bir şekilde özetleyebilirsiniz.
- **Kod Yazma:** Verilen isteklere uygun olarak kod üretebilirsiniz.

### Kod Yazma Örneği:

Bu örnekte, model bir metni büyük harfe çeviren bir Python fonksiyonu yazmaktadır:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer, pipeline
import torch

model_id = "aerdincdal/CBDDO-LLM-8B-Instruct-v1"

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,  
    device_map="auto",           
    trust_remote_code=True       
)

tokenizer = AutoTokenizer.from_pretrained(
    model_id,
    trust_remote_code=True       
)

streamer = TextStreamer(tokenizer)

text_generation_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    model_kwargs={"torch_dtype": torch.bfloat16},  
    streamer=streamer
)

messages = [
    {"role": "system", "content": "Her zaman düşünceli yanıtlar veren bir chatbot'sun."},
    {"role": "user", "content": "Python ile bir metni büyük harfe çeviren bir fonksiyon yaz."}
]

prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

terminators = [
    tokenizer.eos_token_id
]

outputs = text_generation_pipeline(
    prompt,
    max_new_tokens=2048,
    eos_token_id=terminators,
    do_sample=True,
    temperature=0.6,
    top_p=0.95
)

print(outputs[0]["generated_text"][len(prompt):])
```

**Çıktı:**
```python
def metni_buyuk_harfe_cevir(metin):
    """Bir metni tümüyle büyük harfe çeviren Python fonksiyonu.

    Args:
        metin: Küçük harflerle yazılmış bir metin.

    Returns:
        Büyük harflerle yazılmış metin.
    """
    return metin.upper()

# Örnek kullanım
metin = "Bu bir deneme metnidir."
buyuk_harf_metin = metni_buyuk_harfe_cevir(metin)
print(buyuk_harf_metin)
```

**Açıklama:**
Model, verilen istemi ("Python ile bir metni büyük harfe çeviren bir fonksiyon yaz.") işleyerek, açıklamaları ve dokümantasyonu içeren tam teşekküllü bir Python kodunu oluşturur. Bu fonksiyon, küçük harflerle yazılmış herhangi bir metni büyük harflere çevirebilir, böylece metinler üzerinde kolay manipülasyon sağlar.

Bu basit adımlarla, Türkçe doğal dil işleme yeteneklerinin sınırlarını zorlayabilir ve dil modelimizin size nasıl yardımcı olabileceğini keşfedebilirsiniz. Bizimle bu teknoloji yolculuğuna çıkın ve dil işleme kapasitenizi genişletin!




**BENCHMARK:**
```json
"config_general": {
    "lighteval_sha": "494ee12240e716e804ae9ea834f84a2c864c07ca",
    "num_few_shot_default": 0,
    "num_fewshot_seeds": 1,
    "override_batch_size": 1,
    "max_samples": null,
    "job_id": "",
    "start_time": 1781075.607155059,
    "end_time": 1784655.466140587,
    "total_evaluation_time_secondes": "3579.858985528117",
    "model_name": "aerdincdal/CBDDO-LLM-8B-Instruct-v1",
    "model_sha": "84430552036c85cc6a16722b26496df4d93f3afe",
    "model_dtype": "torch.bfloat16",
    "model_size": "15.08 GB"
  },
  "results": {
    "harness|arc:challenge|25": {
      "acc": 0.4991467576791809,
      "acc_stderr": 0.014611369529813262,
      "acc_norm": 0.5460750853242321,
      "acc_norm_stderr": 0.014549221105171872
    },
    "harness|hellaswag|10": {
      "acc": 0.5552678749253137,
      "acc_stderr": 0.004959204773046207,
      "acc_norm": 0.7633937462656841,
      "acc_norm_stderr": 0.004241299341050841
    },
    "harness|hendrycksTest-abstract_algebra|5": {
      "acc": 0.35,
      "acc_stderr": 0.047937248544110196,
      "acc_norm": 0.35,
      "acc_norm_stderr": 0.047937248544110196
    },
    "harness|hendrycksTest-anatomy|5": {
      "acc": 0.6148148148148148,
      "acc_stderr": 0.04203921040156279,
      "acc_norm": 0.6148148148148148,
      "acc_norm_stderr": 0.04203921040156279
    },
    "harness|hendrycksTest-astronomy|5": {
      "acc": 0.5986842105263158,
      "acc_stderr": 0.039889037033362836,
      "acc_norm": 0.5986842105263158,
      "acc_norm_stderr": 0.039889037033362836
    },
    "harness|hendrycksTest-business_ethics|5": {
      "acc": 0.62,
      "acc_stderr": 0.048783173121456316,
      "acc_norm": 0.62,
      "acc_norm_stderr": 0.048783173121456316
    },
    "harness|hendrycksTest-clinical_knowledge|5": {
      "acc": 0.7094339622641509,
      "acc_stderr": 0.02794321998933714,
      "acc_norm": 0.7094339622641509,
      "acc_norm_stderr": 0.02794321998933714
    }
```