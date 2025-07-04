# Shisa 7B

![Shi-chan and Sa-chan/シーちゃんとサーちゃん](https://huggingface.co/augmxnt/shisa-7b-v1/resolve/main/shisa.webp)

**Shisa 7B** (`shisa-7b-v1`) is a bilingual Japanese and English (JA/EN) general-purpose chat model that aims to achieve strong Japanese language performance while retaining robust English capabilities, using a synthetic-data driven approach.

This model is based on [Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-v0.1) with a custom JA-optimized extended tokenizer that is >2X more efficient in Japanese than Mistral's original tokenizer. The base model was pre-trained for an additional 8B primarily Japanese tokens. It was then subsequently fine-tuned with an expanded, machine-translated version of [airoboros-3.1](https://huggingface.co/datasets/jondurbin/airoboros-3.1), a set of the highest-scoring items from [ultrafeedback_binarized](https://huggingface.co/datasets/HuggingFaceH4/ultrafeedback_binarized), and additional freshly generated [airoboros](https://github.com/jondurbin/airoboros) data directly to the target languages.

We also release our base model, datasets, and pipeline code under a permissive Apache 2.0 license which can be used for any purpose, commercial or otherwise:
* [shisa-base-7b-v1](https://huggingface.co/augmxnt/shisa-base-7b-v1) - our base model w/ an extended tokenizer and additional JA pre-training
* [shisa-pretrain-en-ja-v1](https://huggingface.co/datasets/augmxnt/shisa-pretrain-en-ja-v1) - our pre-training data set
* [ultra-orca-boros-en-ja](https://huggingface.co/datasets/augmxnt/ultra-orca-boros-en-ja-v1) - a synthetically generated, machine-translated, programmatically validated JA/EN fine-tuning dataset
* [shisa-en-ja-dpo-v1](https://huggingface.co/datasets/augmxnt/shisa-en-ja-dpo-v1) - Small subset of DPO pairs from ultrafeedback, along with JA DPO pairs using GPT-4 generated items as the chosen value, and outputs from our preliminary 7b model as the rejected values
* [Shisa repository](https://github.com/AUGMXNT/shisa) - this includes our translation, dataset generation, training, and evaluation code

Moreover, we are in the process of publishing extended writeups and more details of our process, including ablation results, testing methodology, and key findings [on our project wiki](https://github.com/AUGMXNT/shisa/wiki) that may be of interest to fellow researchers.

## Fine-Tuning
Our original intuition was to see if we could create a stronger Japanese model using the best [existing public JA training sets](https://github.com/AUGMXNT/shisa/wiki/A-Review-of-Public-Japanese-Training-Sets) and incorporating them. After initial review and testing, however, we decided that focusing solely on translation/generation of our own synthetic datasets could yield superior results with less training.

We compared multiple translation tools and, via manual review, judged that while `gpt-4` almost always delivered the highest quality translations, Google's `text-bison-32k` was a good balance of quality, cost and throughput. Over various iterations, we refined our translation approach to include some additional algorithms for flagging and filtering invalid translations, re-translating and backfilling as necessary.

We also took this project as an opportunity to apply some newer techniques such as incorporating [NEFTune](https://arxiv.org/abs/2310.05914) and [DPO](https://arxiv.org/abs/2305.18290) training.

For our v1 release, we picked from our release candidates based on a significant amount of human preference testing (thousands of generations and multiple rounds of pairwise comparisons). We analyzed our results with both win/loss/draw and [BTL modeling](https://datascience.oneoffcoder.com/btl-model.html) (iLSR) using [choix](https://github.com/lucasmaystre/choix)).


The best candidate model was fine-tuned in a 3-step process:

1. First, the model was fine-tuned on `ultra-orca-boros-en-ja` and SlimOrca ([WandB Log](https://wandb.ai/jondurbin/shisa-7b-v1/runs/k8pfog9d/overview)) 
2. Next, we add one additional epoch at performed using only a subset of Japanese ultra-orca-boros-en-ja items to enhance JA performance (as SlimOrca from the first step is mostly EN) ([WandB Log](https://wandb.ai/jondurbin/shisa-mega-7b-v1.1/runs/dopsr0o7/overview))
3. Finally, the model was tuned using a DPOTrainer on a small subset of ultrafeedback (EN) and our own JA DPO dataset which uses gpt-4 outputs as the chosen values and outputs from stage 1's prelim model as rejected values. ([WandDB Log](https://wandb.ai/jondurbin/shisa-mega-dpo-7b-v1.1) )

During our training process, we also gained some key insights on [why some existing Japanese models seem to underperform](https://github.com/AUGMXNT/shisa/wiki/A-Review-of-Public-Japanese-Training-Sets#analysis) even versus models that have no additional JA training, and we hope that sharing this analysis will be useful to other teams developing Japanese language models.

While we need to explore this further, as an experimental validation, we applied a version of our fine-tuning set onto an existing base model ("Gamma 7B") and the initial JA MT-Bench results suggests that we can drastically increase functional performance with our tuning approach:

| Model                          | Score |
| ------------------------------ | ----- |
| shisa-gamma-7b-allsources-v0.4 |  5.65 |
| ja-stablelm-instruct-gamma-7b* |  4.01 |


## Performance
Throughout our training, we did extensive human evaluation for each model to cross-validate our model performance, and we are currently conducting ongoing larger scale manual head-to-head testing between models. Our intention is open up and scale this data collection as we further develop our tools. For more information and updates, please see our [project wiki](https://github.com/AUGMXNT/shisa/wiki).

While we believe [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) is a useful metric for our [base model](https://huggingface.co/augmxnt/shisa-base-7b-v1), and it was extremely useful during our tuning process for initial validations, as our fine-tune training includes a percentage of the benchmark train splits, we provide these llm-jp-eval results primarily as a point of interest:

| AVR   | MC    | NLI   | QA    | RC    |
|-------|-------|-------|-------|-------|
| 0.7480| 0.8900| 0.8040| 0.4153| 0.8825|

*(We run a [slightly modified llm-jp-eval](https://github.com/llm-jp/llm-jp-eval/compare/main...AUGMXNT:llm-jp-eval:main) to support testing of Qwen and to emit a `bos_token` if available)*

For our final model, since it's customary to include benchmarks, we've used Stability AI Japan's [Japanese MT-Bench](https://github.com/Stability-AI/FastChat) as a more representative test of our model's capabilities. For [our JA MT-Bench testing](https://github.com/Stability-AI/FastChat/compare/jp-stable...AUGMXNT:FastChat:jp-stable) we use a Japanese prompt ("あなたは役立つアシスタントです。") as well as `--num-choices 4` in an effort to reduce sampling variability, however we've still observed regular 0.5+ point (and sometimes even greater swings) between generations, as well as issues with default prompts and parameters when testing, so again, we'd urge caution in over-interpreting these scores and treating them as more of a probabilistic directional indicator, rather than a definitive score or ranking: 

| Benchmark   | Score |
| ----------- | ----- |
| JA MT-Bench |  5.23 |
| MT-Bench    |  5.71 |

There is an [MT-Bench Leaderboard](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard), but as JA MT-Bench is still under development, for convenience, here is a comparison of the JA MT-Bench scores of some other models (our scores were rated by `gpt-4-0613`):

| Model                                             | Score |
| ------------------------------------------------- | ---- |
| gpt-4-0613                                        | 9.40 |
| gpt-4-1106-preview                                | 9.17 |
| gpt-3.5-turbo*                                    | 8.41 |
| Qwen-14B-Chat                                     | 7.47 |
| **shisa-7b-v1**                               | **5.23** |
| ELYZA-japanese-Llama-2-7b-fast-instruct*          | 4.86 |
| ja-stablelm-instruct-gamma-7b*                    | 4.01 |
| japanese-stablelm-instruct-alpha-7b*              | 2.74 |
| Mistral-7B-OpenOrca-ja*                           | 2.23 |
| youri-7b-chat*                                    | 2.00 |
| Mistral-7B-Instruct-v0.1*                         | 1.78 |
| llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0* | 1.31 |

*(Marked JA MT-Bench results in this section are [sourced from shi3z](https://note.com/shi3zblog/n/n6b2ac5874021))*

## Limitations
Although our model demonstrates a reasonably high level of Japanese fluency,  as a 7B parameter model, it is prone to higher hallucination rates and less effective instruction following and reasoning than larger-class models. Also, it still does not have complete mastery of the Japanese language and a native speaker will spot occasional mistakes like some non-idiomatic/awkward phrasing, improper tenses/speech levels, etc.

We've also noticed a small amount of language leakage, likely largely attributable to our tokenizer expansion. These may be fixable with sampler settings like [Min P](https://www.reddit.com/r/LocalLLaMA/comments/17vonjo/your_settings_are_probably_hurting_your_model_why/)) or additional targeted training, and we plan on doing additional work on automated detection/sampler sweeps in the future. One interesting observation is, based on our data collection, we found that as we iterated, the DPO process significantly exacerbated this issue, but also that our DPO models still had significantly higher human preference rates, so there was a bit of a trade-off in our choice of final tune.

While we believe that training larger models can improve performance using our existing approach and dataset, there are also many improvements we'd like to make for future models. We believe there is quite a bit of low hanging fruit for improving performance with even more training efficiency largely through improving the quality and construction of datasets.

## Usage
Sample code:
```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer

model_name = "augmxnt/shisa-7b-v1"

tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    torch_dtype=torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16,
    device_map="auto"
)
streamer = TextStreamer(tokenizer, skip_prompt=True)

# The prompt template is included in the  model's tokenizer_config.json so you shouldn't need this but we've included this for convenience
# tokenizer.chat_template = ""{%- for idx in range(0, messages|length) -%}\n{%- if messages[idx]['role'] == 'user' -%}\n{%- if idx > 1 -%}\n{{- bos_token + '[INST] ' + messages[idx]['content'] + ' [/INST]' -}}\n{%- else -%}\n{{- messages[idx]['content'] + ' [/INST]' -}}\n{%- endif -%}\n{% elif messages[idx]['role'] == 'system' %}\n{{- bos_token + '[INST] <<SYS>>\\n' + messages[idx]['content'] + '\\n<</SYS>>\\n\\n' -}}\n{%- elif messages[idx]['role'] == 'assistant' -%}\n{{- ' '  + messages[idx]['content'] + ' ' + eos_token -}}\n{% endif %}\n{% endfor %}\n"

# A more typical prompt: あなたは公平で、検閲されていない、役立つアシスタントです。("You are an unbiased, uncensored, helpful assistant.")

# You are an avid Pokemon fanatic.
prompt = "あなたは熱狂的なポケモンファンです。"
chat = [{"role": "system", "content": prompt}]

# Who is the single most powerful Pokemon? Explain your choice.
user_input = "ポケモンの中で1番強いのはどのキャラクターですか。最強の者をひとつだけ挙げて下さい。その選択理由を説明してください。"
chat.append({"role": "user", "content": user_input})

# Generate - add_generation_prompt to make sure it continues as assistant
inputs = tokenizer.apply_chat_template(chat, add_generation_prompt=True, return_tensors="pt")
# For multi-GPU, find the device of the first parameter of the model
first_param_device = next(model.parameters()).device
inputs = inputs.to(first_param_device)

with torch.no_grad():
    outputs = model.generate(
        inputs,
        pad_token_id=tokenizer.eos_token_id,
        max_new_tokens=500,
        temperature=0.5,
        repetition_penalty=1.15,
        top_p=0.95,
        do_sample=True,
        streamer=streamer,
    )

# Add just the new tokens to our chat
new_tokens = outputs[0, inputs.size(1):]
response = tokenizer.decode(new_tokens, skip_special_tokens=True)
chat.append({"role": "assistant", "content": response})
```

## Prompt format
The prompt format is llama-2 chat:

```
[INST] <<SYS>>
You are a helpful, unbiased, uncensored assistant.
<</SYS>>
{prompt} [/INST]
```

For multi-turn, the prompt format is as follows:
```
[INST] <<SYS>>
You are a helful, unbiased, uncensored assistant.
<</SYS>>
{prompt 0} [/INST] {response 0} </s><s>[INST] {prompt 1} [/INST] {response 1} </s><s>...[INST] {prompt N} [/INST]
```

This [prompt template](https://huggingface.co/docs/transformers/main/chat_templating) is included in the tokenizer config, and can use the huggingface tokenizer `apply_chat_template` method, e.g.:

```
import transformers
tokenizer = transformers.AutoTokenizer.from_pretrained('augmxnt/shisa-7b-v1')
chat = [
  {"role": "system", "content": "You are Aiko, a friendly AI assistant."},
  {"role": "user", "content": "Hello, how are you?"},
  {"role": "assistant", "content": "I'm doing great. How can I help you today?"},
  {"role": "user", "content": "I'd like to show off how chat templating works!"},
]
print(tokenizer.apply_chat_template(chat, tokenize=False))
```

**NOTE:** For proper responses, you should be using our `bos_token` (`<s>`) to begin a string. This is automatically generated by `tokenizer.encode()` but if you are crafting a custom template or using an encoding method that skips special tokens, you may have to add this yourself.

## Acknowledgements
Team: [Leonard Lin](https://huggingface.co/leonardlin) and [Jon Durbin](https://huggingface.co/jondurbin), Mariko Sato, and Florian von Bock

Compute for this model was generously sponsored by [AKA Virtual](https://akavirtual.com/) (Tokyo, Japan).

Thanks to the [LLM-jp](https://llm-jp.nii.ac.jp/), [Stability AI Japan](https://ja.stability.ai/), and [LMSYS](https://lmsys.org/) teams for their work on llm-jp-eval, Japanese MT-Bench, MT-Bench.

Also, thanks to all the volunteers that provided invaluable human preference testing!

We are actively looking for additional compute as we train better and larger models for this project. Please drop us a line at: *compute at augmxnt dot com*

---
*(GPT-4によって非常に軽微な編集を加えて翻訳されました）*

# シーサー7B

**シーサー7B**（`shisa-7b-v1`）は、合成データ駆動のアプローチを用いて、優れた日本語と英語能力を両立することを目指すバイリンガル（日本語/英語）汎用チャットモデルです。

このモデルは、[Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-v0.1)を基に、Mistralのオリジナルのトークナイザーよりも日本語において2倍以上効率的な、日本語最適化拡張トークナイザーをカスタムして作成されました。ベースモデルは、主に日本語のトークンを追加で80億ものトレーニングを行いました。そして、その後、[airoboros-3.1](https://huggingface.co/datasets/jondurbin/airoboros-3.1)の拡張された機械翻訳版、[ultrafeedback_binarized](https://huggingface.co/datasets/HuggingFaceH4/ultrafeedback_binarized)からの最高得点項目のセット、そして新たに生成された[airoboros](https://github.com/jondurbin/airoboros)のデータを直接目標言語で微調整しています。

商用を含むあらゆる目的で使用可能な寛容なApache 2.0ライセンスの下で、ベースモデル、データセット、およびパイプラインコードも公開しています：
* [shisa-base-7b-v1](https://huggingface.co/augmxnt/shisa-base-7b-v1) - 拡張トークナイザーと追加の日本語プレトレーニングを備えた当方のベースモデル
* [shisa-pretrain-en-ja-v1](https://huggingface.co/datasets/augmxnt/shisa-pretrain-en-ja-v1) - 当方のプレトレーニングデータセット
* [ultra-orca-boros-en-ja](https://huggingface.co/datasets/jondurbin/ultra-orca-boros-en-ja) - 合成生成、機械翻訳、プログラムによる検証によるJA/EN微調整データセット
* [shisa-en-ja-dpo-v1](https://huggingface.co/datasets/augmxnt/shisa-en-ja-dpo-v1) - ultrafeedbackからのDPOペアの小さなサブセットと、選択された値としてGPT-4生成項目を使用した日本語のDPOペア、そして初期の7ビリオンモデルの出力を却下した値
* [シーサーリポジトリ](https://github.com/AUGMXNT/shisa) - 翻訳、データセットの生成、トレーニング、評価コードなどが含まれています

さらに、アブレーション結果、テスト方法論、主要な調査結果など、プロセスの詳細や拡張ライトアップを公開する過程にあります。これは[当プロジェクトwiki](https://github.com/AUGMXNT/shisa/wiki)で研究者に興味深い情報として提供されています。

## 微調整

最初の直感は、最良の[既存の公開日本語トレーニングセット](https://github.com/AUGMXNT/shisa/wiki/A-Review-of-Public-Japanese-Training-Sets)を使用して、それらを組み入れることでより強力な日本語モデルを作成できるかどうかを見ることでした。しかし、初期の検討とテストの後、自らの合成データセットの翻訳/生成にだけ焦点を当てることで、短期間のトレーニングで優れた結果を得ることができると結論付けました。

私たちは複数の翻訳ツールを比較し、手動でレビューを行った結果、`gpt-4`がほぼ常に最高品質の翻訳を提供しながら、Googleの `text-bison-32k`は品質、コスト、スループットのバランスが良いと判断しました。複数の繰り返しを経て、無効な翻訳のフラグ付けとフィルタリング、必要に応じた再翻訳とバックフィルのための追加のアルゴリズムを含むように、翻訳アプローチを洗練させました。

また、このプロジェクトを[NEFTune](https://arxiv.org/abs/2310.05914)と[DPO](https://arxiv.org/abs/2305.18290)トレーニングを取り入れるなど、新しい技術を適用する機会ともなりました。

v1リリースのために、私たちは大量の人間の嗜好テスト（数千の生成と複数ラウンドのペアワイズ比較）に基づいてリリース候補から選択しました。私たちは、勝ち/負け/引き分けと、[BTLモデル](https://datascience.oneoffcoder.com/btl-model.html)（iLSR）を使用して[choix](https://github.com/lucasmaystre/choix)で結果を分析しました。

最良の候補モデルは、3ステップのプロセスで微調整されました：

1. 最初に、モデルは`ultra-orca-boros-en-ja`とSlimOrca ([WandB Log](https://wandb.ai/jondurbin/shisa-7b-v1/runs/k8pfog9d/overview))で微調整されました。
2. 次に、日本語のパフォーマンスを向上させるためにultra-orca-boros-en-jaの一部を使用して1回追加のエポックを追加しました（最初の段階のSlimOrcaは主に英語）([WandB Log](https://wandb.ai/jondurbin/shisa-mega-7b-v1.1/runs/dopsr0o7/overview))。
3. 最後に、モデルは小規模のultrafeedback（英語）と自身のJA DPOデータセットに対してDPOTrainerを使用して調整されました。ここで使用したJA DPOデータセットはgpt-4の出力を選出された値とし、ステージ1の予備モデルの出力を却下した値とします。([WandDB Log](https://wandb.ai/jondurbin/shisa-mega-dpo-7b-v1.1) )

私たちのトレーニングプロセス中に、何故一部の既存の日本語モデルが、追加の日本語トレーニングがないモデルに対してもパフォーマンスが低いのか、といういくつかの重要な洞察を得ることができました。この分析結果を共有すれば、他のチームが日本語モデルを開発する際の参考になると思います。

さらに探求する必要はありますが、実験的な検証として、微調整セットのバージョンを既存のベースモデル（"Gamma 7B"）に適用し、初期のJA MT-Bench結果が示すように、私たちのチューニングアプローチで機能性のパフォーマンスを劇的に向上させることができました：

| モデル                          | スコア |
| ------------------------------ | ----- |
| shisa-gamma-7b-allsources-v0.4 |  5.65 |
| ja-stablelm-instruct-gamma-7b* |  4.01 |

## パフォーマンス
トレーニング全体を通じて、各モデルについて人間による評価を行い、モデルのパフォーマンスを相互に検証しました。現在、モデル間の手動での比較テストを大規模に行っています。私たちの目指すところは、ツールをさらに発展させることでこのデータ収集を公開して拡張することです。詳細と更新情報については、[プロジェクトwiki](https://github.com/AUGMXNT/shisa/wiki) をご覧ください。

我々は、[llm-jp-eval](https://github.com/llm-jp/llm-jp-eval)は、私たちの[基本モデル](https://huggingface.co/augmxnt/shisa-base-7b-v1)の有用な指標であり、初期の検証のための微調整プロセス中に非常に役立つと考えていますが、微調整トレーニングにはベンチマークのトレイン分割の一部が含まれているため、私たちが提供するllm-jp-evalの結果は主に興味深いポイントとして提供しています：

| AVR   | MC    | NLI   | QA    | RC    |
|-------|-------|-------|-------|-------|
| 0.7480| 0.8900| 0.8040| 0.4153| 0.8825|

*(Qwenのテストをサポートし、可能であれば`bos_token`を発行するために、[わずかに修正したllm-jp-eval](https://github.com/llm-jp/llm-jp-eval/compare/main...AUGMXNT:llm-jp-eval:main) を実行しています)*

最終モデルについては、ベンチマークを含めるのが一般的なため、私たちのモデルの能力をより代表的にテストするために、Stability AI Japanの[Japanese MT-Bench](https://github.com/Stability-AI/FastChat)を使用しました。[私たちのJA MT-Bench テスト](https://github.com/Stability-AI/FastChat/compare/jp-stable...AUGMXNT:FastChat:jp-stable)では、サンプリング変動を減らすために、日本語のプロンプト（"あなたは役立つアシスタントです。"）と `--num-choices 4`を使用していますが、生成間で0.5+点（時にはそれ以上の変動）を頻繁に観察し、テスト時のデフォルトのプロンプトとパラメータに問題があったという経験から、これらのスコアを過度に解釈することには注意が必要で、これらを確定的なスコアやランキングではなく、より確率的な方向指標として扱うことをお勧めします： 

| ベンチマーク   | スコア |
| ----------- | ----- |
| JA MT-Bench |  5.23 |
| MT-Bench    |  5.71 |

[MT-Bench Leaderboard](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard)がありますが、JA MT-Benchはまだ開発中であるため、便宜上、他のモデルのJA MT-Benchスコアとの比較を示します（私たちのスコアは`gpt-4-0613`によって評価されました）：

| モデル                                             | スコア |
| ------------------------------------------------- | ---- |
| gpt-4-0613                                        | 9.40 |
| gpt-4-1106-preview                                | 9.17 |
| gpt-3.5-turbo*                                    | 8.41 |
| Qwen-14B-Chat                                     | 7.47 |
| **shisa-7b-v1**                               | **5.23** |
| ELYZA-japanese-Llama-2-7b-fast-instruct*          | 4.86 |
| ja-stablelm-instruct-gamma-7b*                    | 4.01 |
| japanese-stablelm-instruct-alpha-7b*              | 2.74 |
| Mistral-7B-OpenOrca-ja*                           | 2.23 |
| youri-7b-chat*                                    | 2.00 |
| Mistral-7B-Instruct-v0.1*                         | 1.78 |
| llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0* | 1.31 |

*(このセクションでマークされたJA MT-Benchの結果は[shi3zから引用](https://note.com/shi3zblog/n/n6b2ac5874021)しました)*

## 制限事項
当モデルは十分な日本語の流暢さを示していますが、7Bパラメータのモデルとしては、より大きなクラスのモデルに比べて幻覚率が高く、指示の追跡や推論が効果的でない傾向があります。また、日本語の完全な習得はまだ達しておらず、ネイティブスピーカーはたまに非慣用的/違和感のある表現や不適切な時制/話し言葉のレベルなどの間違いを見つけることがあります。

また、私たちのトークナイザーの拡張に大いに起因する可能性が高いが、わずかな言語リークを確認しています。これらは[Min P](https://www.reddit.com/r/LocalLLaMA/comments/17vonjo/your_settings_are_probably_hurting_your_model_why/)などのサンプラー設定や追加のターゲット指向型トレーニングで修正可能な可能性があり、今後、自動検出/サンプラーのスウィープについて追加の作業を行う予定です。興味深い観察としては、私たちのデータ収集に基づいて、DPOプロセスがこの問題を大幅に悪化させることがわかりましたが、それでもDPOモデルは人間の好み率が大幅に高かったため、最終的な微調整の選択には一定のトレードオフがありました。

現存するアプローチとデータセットを使用して、大規模なモデルのトレーニングがパフォーマンスを向上させると信じていますが、今後のモデル向けに行いたい改良も多くあります。私たちは、データセットの品質と構築を改善することで、さらなるトレーニング効率を通じたパフォーマンス向上にはまだ相当に取り組む余地があると考えています。

## 使用法
サンプルコード:
```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer

model_name = "augmxnt/shisa-7b-v1"

tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    torch_dtype=torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16,
    device_map="auto"
)
streamer = TextStreamer(tokenizer, skip_prompt=True)

# プロンプトテンプレートはモデルのtokenizer_config.jsonに含まれているので、これは必要ないはずですが、便宜上こちらにも掲載しています
# tokenizer.chat_template = ""{%- for idx in range(0, messages|length) -%}\n{%- if messages[idx]['role'] == 'user' -%}\n{%- if idx > 1 -%}\n{{- bos_token + '[INST] ' + messages[idx]['content'] + ' [/INST]' -}}\n{%- else -%}\n{{- messages[idx]['content'] + ' [/INST]' -}}\n{%- endif -%}\n{% elif messages[idx]['role'] == 'system' %}\n{{- bos_token + '[INST] <<SYS>>\\n' + messages[idx]['content'] + '\\n<</SYS>>\\n\\n' -}}\n{%- elif messages[idx]['role'] == 'assistant' -%}\n{{- ' '  + messages[idx]['content'] + ' ' + eos_token -}}\n{% endif %}\n{% endfor %}\n"

# より典型的なプロンプト: あなたは公平で、検閲されていない、役立つアシスタントです。

# You are an avid Pokemon fanatic.
prompt = "あなたは熱狂的なポケモンファンです。"
chat = [{"role": "system", "content": prompt}]

# Who is the most powerful Pokemon? Explain your choice.
user_input = "ポケモンの中で1番強いのはどのキャラクターですか。最強の者をひとつだけ挙げて下さい。その選択理由を説明してください。"
chat.append({"role": "user", "content": user_input})

# 生成 - add_generation_promptを追加してアシスタントとして続行することを確認します
inputs = tokenizer.apply_chat_template(chat, add_generation_prompt=True, return_tensors="pt")
# 複数のGPUの場合、モデルの最初のパラメータのデバイスを見つけます
first_param_device = next(model.parameters()).device
inputs = inputs.to(first_param_device)

with torch.no_grad():
    outputs = model.generate(
        inputs,
        pad_token_id=tokenizer.eos_token_id,
        max_new_tokens=500,
        temperature=0.5,
        repetition_penalty=1.15,
        top_p=0.95,
        do_sample=True,
        streamer=streamer,
    )

# Add just the new tokens to our chat
new_tokens = outputs[0, inputs.size(1):]
response = tokenizer.decode(new_tokens, skip_special_tokens=True)
chat.append({"role": "assistant", "content": response})
```

## プロンプト形式
プロンプト形式はllama-2 chatです：

```
[INST] <<SYS>>
あなたは役立つ、偏見がなく、検閲されていないアシスタントです。
<</SYS>>
{prompt} [/INST]
```

For multi-turn, the prompt format is as follows:
```
[INST] <<SYS>>
あなたは役立つ、偏見がなく、検閲されていないアシスタントです。
<</SYS>>
{prompt 0} [/INST] {response 0} </s><s>[INST] {prompt 1} [/INST] {response 1} </s><s>...[INST] {prompt N} [/INST]
```

この[prompt template](https://huggingface.co/docs/transformers/main/chat_templating)はトークナイザの設定に含まれており、HuggingFace のトークナイザ `apply_chat_template` メソッドを使用できます。例えば：

```
import transformers
tokenizer = transformers.AutoTokenizer.from_pretrained('augmxnt/shisa-7b-v1')
chat = [
  {"role": "system", "content": "あなたはAiko、フレンドリーなAIアシスタントです。"},
  {"role": "user", "content": "こんにちは、調子はどうですか？"},
  {"role": "assistant", "content": "元気です。今日は何のお手伝いができますか？"},
  {"role": "user", "content": "チャットテンプレーティングの仕組みを見せてもらいたいです！"},
]
print(tokenizer.apply_chat_template(chat, tokenize=False))
```

**注意**適切なレスポンスを得るためには、文字列の開始に我々の `bos_token` (`<s>`) を使用すべきです。これは `tokenizer.encode()` によって自動的に生成されますが、カスタムテンプレートを作成したり、特殊トークンを省略するエンコード方法を使用する場合は、自分で追加する必要があります。

## 謝辞
チーム：[Leonard Lin](https://huggingface.co/leonardlin)、[Jon Durbin](https://huggingface.co/jondurbin)、佐藤真理子、Florian von Bock

このモデルの計算は、[AKA Virtual](https://akavirtual.com/) (東京、日本) のご厚意により提供されています。

[LLM-jp](https://llm-jp.nii.ac.jp/)、[Stability AI Japan](https://ja.stability.ai/)、[LMSYS](https://lmsys.org/)のチームが、llm-jp-eval, Japanese MT-Bench, MT-Benchに取り組んでくれて感謝しています。

また、貴重なヒューマンプリファレンステストを提供してくださったすべてのボランティアにも感謝いたします！

このプロジェクトのためにより良く、より大きなモデルを訓練するために、追加の計算を積極的に探しています。お問い合わせは次の宛先までお願いいたします：*compute at augmxnt dot com*