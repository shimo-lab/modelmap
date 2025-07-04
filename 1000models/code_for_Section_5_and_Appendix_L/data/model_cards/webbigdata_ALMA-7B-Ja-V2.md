# New Translation model released.

[C3TR-Adapter](https://huggingface.co/webbigdata/C3TR-Adapter) is the QLoRA adapter for google/gemma-7b.  
Despite the 4-bit quantization, the memory GPU requirement has increased to 8.1 GB. 
However, it is possible to run it with the free version of Colab and the performance is much improved!

# webbigdata/ALMA-7B-Ja-V2

ALMA-7B-Ja-V2は日本語から英語、英語から日本語の翻訳が可能な機械翻訳モデルです。  
The ALMA-7B-Ja-V2 is a machine translation model capable of translating from Japanese to English and English to Japanese.

ALMA-7B-Ja-V2は以前のモデル([ALMA-7B-Ja](https://huggingface.co/webbigdata/ALMA-7B-Ja))に更に学習を追加し、性能を向上しています。  
The ALMA-7B-Ja-V2 adds further learning to the previous model ([ALMA-7B-Ja](https://huggingface.co/webbigdata/ALMA-7B-Ja)) and improves performance.  

日本語と英語間に加えて、このモデルは以下の言語間の翻訳能力も持っていますが、日英、英日翻訳を主目的にしています。  
In addition to translation between Japanese and English, this model also has the ability to translate between the following languages, but is primarily intended for Japanese-English and English-Japanese translation.  

- ドイツ語 German(de) and 英語 English(en)  
- 中国語 Chinese(zh) and 英語 English(en)  
- アイスランド語 Icelandic(is) and 英語 English(en)  
- チェコ語 Czech(cs) and 英語 English(en)  

# ベンチマーク結果

以下の三種の指標を使って翻訳性能を確認しました。  
The following three metrics were used to check translation performance.  

数字が大きいほど性能が良い事を意味します。  
The higher the number, the better the performance.    

## BLEU
翻訳テキストが元のテキストにどれだけ似ているかを評価する指標です。しかし、単語の出現頻度だけを見ているため、語順の正確さや文の流暢さを十分に評価できないという弱点があります  
A metric that evaluates how similar the translated text is to the original text. However, since it mainly looks at the frequency of word appearances, it may not effectively evaluate the accuracy of word order or the fluency of sentences.  

### chrF++
文字の組み合わせの一致度と語順に基づいて、翻訳の正確さを評価する指標です。弱点としては、長い文章の評価には不向きであることが挙げられます。  
A method to evaluate translation accuracy based on how well character combinations match and the order of words. A drawback is that it might not be suitable for evaluating longer sentences.  

### comet
機械学習モデルを使って翻訳の品質を自動的に評価するためのツール、人間の主観的評価に近いと言われていますが、機械学習ベースであるため、元々のモデルが学習に使ったデータに大きく依存するという弱点があります。  
A tool that uses machine learning models to automatically evaluate the quality of translations, although it is said to be similar to the evaluation ratings performed by humans. Because it is machine learning based, it has the weakness that the original model is highly dependent on the data used for training.    

## vs. NLLB-200
Meta社の200言語以上の翻訳に対応した超多言語対応機械翻訳モデルNLLB-200シリーズと比較したベンチマーク結果は以下です。  
Benchmark results compared to Meta's NLLB-200 series of super multilingual machine translation models, which support translations in over 200 languages, are shown below.  

| Model Name                   | file size |E->J chrf++/F2|E->J comet|J->E chrf++/F2|J->E comet |
|------------------------------|-----------|--------------|----------|--------------|-----------|
| NLLB-200-Distilled           | 2.46GB    | 23.6/-       | -        | 50.2/-       | -         |
| NLLB-200-Distilled           | 5.48GB    | 25.4/-       | -        | 54.2/-       | -         |
| NLLB-200                     | 5.48GB    | 24.2/-       | -        | 53.6/-       | -         |
| NLLB-200                     | 17.58GB   | 25.2/-       | -        | 55.1/-       | -         |
| NLLB-200                     | 220.18GB  | 27.9/33.2    | 0.8908   | 55.8/59.8    | 0.8792    |

## previous our model(ALMA-7B-Ja)  
| Model Name                   | file size |E->J chrf++/F2|E->J comet|J->E chrf++/F2|J->E comet |
|------------------------------|-----------|--------------|----------|--------------|-----------|
| webbigdata-ALMA-7B-Ja-q4_K_S | 3.6GB     |    -/24.2    | 0.8210   |    -/54.2    | 0.8559    |
| ALMA-7B-Ja-GPTQ-Ja-En        | 3.9GB     |    -/30.8    | 0.8743   |    -/60.9    | 0.8743    |
| ALMA-Ja(Ours)                | 13.48GB   |    -/31.8    | 0.8811   |    -/61.6    | 0.8773    |

## ALMA-7B-Ja-V2  
| Model Name                   | file size |E->J chrf++/F2|E->J comet|J->E chrf++/F2|J->E comet |
|------------------------------|-----------|--------------|----------|--------------|-----------|
| ALMA-7B-Ja-V2-GPTQ-Ja-En     | 3.9GB     |    -/33.0    | 0.8818   |    -/62.0    | 0.8774    |
| ALMA-Ja-V2(Ours)             | 13.48GB   |    -/33.9    | 0.8820   |    -/63.1    | 0.8873    |
| ALMA-Ja-V2-Lora(Ours)        | 13.48GB   |    -/33.7    | 0.8843   |    -/61.1    | 0.8775    |


ALMA-7B-Ja-V2を様々なジャンルの文章を現実世界のアプリケーションと比較した結果は以下です。  
Here are the results of a comparison of various genres of writing with the actual application.  

## 政府の公式文章 Government Official Announcements  
|                          |e->j chrF2++|e->j BLEU|e->j comet|j->e chrF2++|j->e BLEU|j->e comet|
|--------------------------|------------|---------|----------|------------|---------|----------|
| ALMA-7B-Ja-V2-GPTQ-Ja-En | 25.3       | 15.00   | 0.8848   | 60.3       | 26.82   | 0.6189   |
| ALMA-Ja-V2               | 27.2       | 15.60   | 0.8868   | 58.5       | 29.27   | 0.6155   |
| ALMA-7B-Ja-V2-Lora       | 24.5       | 13.58   | 0.8670   | 50.7       | 21.85   | 0.6196   |
| SeamlessM4T              | 27.3       | 16.76   | 0.9070   | 54.2       | 25.76   | 0.5656   |
| gpt-3.5                  | 34.6       | 28.33   | 0.8895   | 74.5       | 49.20   | 0.6382   |
| gpt-4.0                  | 36.5       | 28.07   | 0.9255   | 62.5       | 33.63   | 0.6320   |
| google-translate         | 43.5       | 35.37   | 0.9181   | 62.7       | 29.22   | 0.6446   |
| deepl                    | 43.5       | 35.74   | 0.9301   | 60.1       | 27.40   | 0.6389   |

## 古典文学 Classical Literature  
|                          |e->j chrF2++|e->j BLEU|e->j comet|j->e chrF2++|j->e BLEU|j->e comet|
|--------------------------|------------|---------|----------|------------|---------|----------|
| ALMA-7B-Ja-V2-GPTQ-Ja-En | 11.8       | 7.24    | 0.6943   | 31.9       | 9.71    | 0.5617   |
| ALMA-Ja-V2               | 10.7       | 4.93    | 0.7202   | 32.9       | 10.52   | 0.5638   |
| ALMA-7B-Ja-V2-Lora       | 12.3       | 7.25    | 0.7076   | 32.5       | 11.14   | 0.5441   |
| gpt-3.5                  | -          | -       | 0.6367   | 69.3       | 46.34   | 0.4922   |
| gpt-4.0                  | 13.3       | 8.33    | 0.7074   | 44.3       | 23.75   | 0.5518   |
| deepl                    | 14.4       | 9.18    | 0.7149   | 34.6       | 10.68   | 0.5787   |
| google-translate         | 13.5       | 8.57    | 0.7432   | 31.7       | 7.94    | 0.5856   |

## 二次創作 Fanfiction  
|                          |e->j chrF2++|e->j BLEU|e->j comet|j->e chrF2++|j->e BLEU|j->e comet|
|--------------------------|------------|---------|----------|------------|---------|----------|
| ALMA-7B-Ja-V2-GPTQ-Ja-En | 27.6       | 18.28   | 0.8643   | 52.1       | 24.58   | 0.6106   |
| ALMA-Ja-V2               | 20.4       | 8.45    | 0.7870   | 48.7       | 23.06   | 0.6050   |
| ALMA-7B-Ja-V2-Lora       | 23.9       | 18.55   | 0.8634   | 55.6       | 29.91   | 0.6093   |
| SeamlessM4T              | 25.5       | 19.97   | 0.8657   | 42.2       | 14.39   | 0.5554   |
| gpt-3.5                  | 31.2       | 23.37   | 0.9001   | -          | -       | 0.5948   |
| gpt-4.0                  | 30.7       | 24.31   | 0.8848   | 53.9       | 24.89   | 0.6163   |
| google-translate         | 32.4       | 25.36   | 0.8968   | 58.5       | 29.88   | 0.6022   |
| deepl                    | 33.5       | 28.38   | 0.9094   | 60.0       | 31.14   | 0.6124   |


## サンプルコード sample code

Googleの無料WebツールであるColabを使うとALMA_7B_Ja_V2の性能を簡単に確かめる事ができます。  
Using Colab, Google's free web tool, you can easily verify the performance of ALMA_7B_Ja_V2.  

[Sample Code For Free Colab](https://github.com/webbigdata-jp/python_sample/blob/main/ALMA_7B_Ja_V2_Free_Colab_sample.ipynb)  


## その他の版 Other Version

### llama.cpp

[llama.cpp](https://github.com/ggerganov/llama.cpp)の主な目的はMacBook上で4ビット整数量子化を使用して LLaMA モデルを実行する事です。  
The main purpose of [llama.cpp](https://github.com/ggerganov/llama.cpp) is to run the LLaMA model using 4-bit integer quantization on a MacBook.  

4ビット量子化に伴い、性能はやや低下しますが、mmngaさんが作成してくれた[webbigdata-ALMA-7B-Ja-V2-gguf](https://huggingface.co/mmnga/webbigdata-ALMA-7B-Ja-V2-gguf)を使うとMacやGPUを搭載していないWindows、Linuxで本モデルを動かす事ができます。  
Although performance is somewhat reduced with 4-bit quantization, [webbigdata-ALMA-7B-Ja-V2-gguf](https://huggingface.co/mmnga/webbigdata-ALMA-7B-Ja-V2-gguf), created by mmnga, can be used to run this model on Mac, Windows and Linux without a GPU.  

[GPU無版のColabで動かすサンプルはこちら](https://github.com/webbigdata-jp/python_sample/blob/main/ALMA_7B_Ja_V2_gguf_Free_Colab_sample.ipynb)です。
[Here is Colab(without GPU) sample code](https://github.com/webbigdata-jp/python_sample/blob/main/ALMA_7B_Ja_V2_gguf_Free_Colab_sample.ipynb).

### GPTQ

GPTQはモデルサイズを小さくする手法(量子化といいます)です。  
GPTQ is a technique (called quantization) that reduces model size.　　

[ALMA-7B-Ja-V2-GPTQ-Ja-En](https://huggingface.co/webbigdata/ALMA-7B-Ja-V2-GPTQ-Ja-En)はGPTQ量子化版で、モデルサイズ(3.9GB)とメモリ使用量を削減し、速度を向上しています。   
[ALMA-7B-Ja-V2-GPTQ-Ja-En](https://huggingface.co/webbigdata/ALMA-7B-Ja-V2-GPTQ-Ja-En) is a quantized GPTQ version, which reduces model size (3.9 GB) and memory usage and increases speed. 

ただし、性能は少し落ちてしまいます。また、日本語と英語以外の言語への翻訳能力は著しく低下しているはずです。   
However, performance is slightly reduced. Also, the ability to translate into languages other than Japanese and English should be significantly reduced.   

[Sample Code For Free Colab webbigdata/ALMA-7B-Ja-V2-GPTQ-Ja-En](https://github.com/webbigdata-jp/python_sample/blob/master/ALMA_7B_Ja_V2_GPTQ_Ja_En_Free_Colab_sample.ipynb)  

ファイル全体を一度に翻訳したい場合は、以下のColabをお試しください。 
If you want to translate the entire txt file at once, try Colab below.  

[ALMA_7B_Ja_GPTQ_Ja_En_batch_translation_sample](https://github.com/webbigdata-jp/python_sample/blob/master/ALMA_7B_Ja_V2_GPTQ_Ja_En_batch_translation_sample.ipynb)


**ALMA** (**A**dvanced **L**anguage **M**odel-based tr**A**nslator) is an LLM-based translation model, which adopts a new translation model paradigm: it begins with fine-tuning on monolingual data and is further optimized using high-quality parallel data. This two-step fine-tuning process ensures strong translation performance. 
Please find more details in their [paper](https://arxiv.org/abs/2309.11674).
```
@misc{xu2023paradigm,
      title={A Paradigm Shift in Machine Translation: Boosting Translation Performance of Large Language Models}, 
      author={Haoran Xu and Young Jin Kim and Amr Sharaf and Hany Hassan Awadalla},
      year={2023},
      eprint={2309.11674},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

Original Model [ALMA-7B](https://huggingface.co/haoranxu/ALMA-7B).  (26.95GB)  
Prevous Model [ALMA-7B-Ja](https://huggingface.co/webbigdata/ALMA-7B-Ja). (13.3 GB)  


## about this work
- **This work was done by :** [webbigdata](https://webbigdata.jp/post-21151/).