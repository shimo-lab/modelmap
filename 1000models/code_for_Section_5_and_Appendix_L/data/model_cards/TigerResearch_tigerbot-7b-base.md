<div style="width: 100%;">
    <p align="center" width="20%">
      <img src="http://x-pai.algolet.com/bot/img/logo_core.png" alt="TigerBot" width="20%", style="display: block; margin: auto;"></img>
    </p>
</div>
<p align="center">
<font face="黑体" size=5"> A cutting-edge foundation for your very own LLM. </font>
</p>
<p align="center">
	💻<a href="https://github.com/TigerResearch/TigerBot" target="_blank">Github</a> • 🌐 <a href="https://tigerbot.com/" target="_blank">TigerBot</a> • 🤗 <a href="https://huggingface.co/TigerResearch" target="_blank">Hugging Face</a>
</p>

# 快速开始

- 方法1，通过transformers使用

  - 下载 TigerBot Repo

     ```shell
     git clone https://github.com/TigerResearch/TigerBot.git
     ```

  - 启动infer代码

    ```shell
    python infer.py --model_path TigerResearch/tigerbot-7b-base
    ```

- 方法2:

  - 下载 TigerBot Repo
    
     ```shell
    git clone https://github.com/TigerResearch/TigerBot.git
    ```

  - 安装git lfs： `git lfs install`

  - 通过huggingface或modelscope平台下载权重
    ```shell
    git clone https://huggingface.co/TigerResearch/tigerbot-7b-base
    git clone https://www.modelscope.cn/TigerResearch/tigerbot-7b-base-v3.git
    ```
    
  - 启动infer代码
    
    ```shell
    python infer.py --model_path tigerbot-7b-base(-v3) --model_type base --max_generate_length 64
    ```

------

# Quick Start

- Method 1, use through transformers

  - Clone TigerBot Repo

     ```shell
     git clone https://github.com/TigerResearch/TigerBot.git
     ```

  - Run infer script

    ```shell
    python infer.py --model_path TigerResearch/tigerbot-7b-base
    ```

- Method 2:

  - Clone TigerBot Repo

    ```shell
    git clone https://github.com/TigerResearch/TigerBot.git
    ```

  - install git lfs： `git lfs install`

  - Download weights from huggingface or modelscope
    ```shell
    git clone https://huggingface.co/TigerResearch/tigerbot-7b-base
    git clone https://www.modelscope.cn/TigerResearch/tigerbot-7b-base-v3.git
    ```
  
  - Run infer script
  
     ```shell
     python infer.py --model_path tigerbot-7b-base(-v3) --model_type base --max_generate_length 64
     ```