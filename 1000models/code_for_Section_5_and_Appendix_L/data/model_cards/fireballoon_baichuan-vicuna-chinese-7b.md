
# baichuan-vicuna-chinese-7b

baichuan-vicuna-chinese-7b是在**中英双语**sharegpt数据上全参数微调的对话模型。

- 基座模型：[baichuan-7B](https://huggingface.co/baichuan-inc/baichuan-7B),在1.2T tokens上预训练的中英双语模型
- 微调数据：[ShareGPT](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/blob/main/ShareGPT_V3_unfiltered_cleaned_split.json), [ShareGPT-ZH](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/Chinese-instruction-collection), [COT & COT-ZH](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/Chain-of-Thought), [Leetcode](https://www.kaggle.com/datasets/erichartford/leetcode-solutions), [dummy](https://github.com/lm-sys/FastChat)
- 训练代码：基于[FastChat](https://github.com/lm-sys/FastChat)

baichuan-vicuna-chinese-7b is a chat model supervised finetuned on vicuna sharegpt data in both **English** and **Chinese**.

- Foundation model: [baichuan-7B](https://huggingface.co/baichuan-inc/baichuan-7B), a commercially available language model pre-trained on a 1.2T Chinese-English bilingual corpus.
- Finetuning data: [ShareGPT](https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/blob/main/ShareGPT_V3_unfiltered_cleaned_split.json), [ShareGPT-ZH](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/Chinese-instruction-collection), [COT & COT-ZH](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT/tree/main/Chain-of-Thought), [Leetcode](https://www.kaggle.com/datasets/erichartford/leetcode-solutions), [dummy](https://github.com/lm-sys/FastChat)
- Training code: based on [FastChat](https://github.com/lm-sys/FastChat)

**[NEW]** 4bit-128g GPTQ量化版本：[baichuan-vicuna-chinese-7b-gptq](https://huggingface.co/fireballoon/baichuan-vicuna-chinese-7b-gptq)


# Training config
```
{batch_size: 256, epoch: 3, learning_rate: 2e-5, context_length: 4096, deepspeed_zero: 3, mixed_precision: bf16, gradient_clipping: 1.0}
```

# Inference
Inference with [FastChat](https://github.com/lm-sys/FastChat):
```
python3 -m fastchat.serve.cli --model-path fireballoon/baichuan-vicuna-chinese-7b
```

Inference with Transformers:
```ipython
>>> from transformers import AutoTokenizer, AutoModelForCausalLM, TextStreamer
>>> tokenizer = AutoTokenizer.from_pretrained("fireballoon/baichuan-vicuna-chinese-7b", use_fast=False)
>>> model = AutoModelForCausalLM.from_pretrained("fireballoon/baichuan-vicuna-chinese-7b").half().cuda()
>>> streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
>>> instruction = "A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the user's questions. USER: {} ASSISTANT:"
>>> prompt = instruction.format("How can I improve my time management skills?")  # user message
>>> generate_ids = model.generate(tokenizer(prompt, return_tensors='pt').input_ids.cuda(), max_new_tokens=2048, streamer=streamer)
'''
Improving time management skills can help you to be more productive and efficient with your time. Here are some tips to help you improve your time management skills:

1. Prioritize tasks: Make a list of all the tasks you need to complete and prioritize them based on their importance and urgency. This will help you to focus on the most important tasks first and avoid getting overwhelmed.
2. Use a calendar or planner: Use a calendar or planner to schedule your tasks and appointments. This will help you to stay organized and ensure that you don't miss any important events or deadlines.
3. Limit distractions: Identify and eliminate distractions, such as social media notifications or email notifications, that can keep you from focusing on your tasks. Consider using tools like browser extensions or apps to block distracting websites.
4. Take breaks: Take regular breaks throughout the day to recharge and refocus. This will help you to stay productive and avoid burnout.
5. Learn to say no: Don't be afraid to say no to requests or invitations that don't align with your goals or values. This will help you to focus on your priorities and avoid overcommitting yourself.
6. Learn to delegate: If possible, delegate tasks to others to free up your own time and focus on more important tasks.
7. Learn to be flexible: Be prepared to adjust your plans and priorities as needed. Things don't always go according to plan, and it's okay to adjust your schedule to accommodate unexpected events or challenges.

Remember that improving your time management skills takes practice and patience. Be kind to yourself and don't be too hard on yourself if you don't get everything done perfectly right away.
'''
```

Gradio multi-turn dialogue example: https://huggingface.co/fireballoon/baichuan-vicuna-chinese-7b/blob/main/app.py
```
python app.py
```

# Test cases on [Ziya-Eval-Chinese](https://huggingface.co/datasets/IDEA-CCNL/Ziya-Eval-Chinese)

```
Q: 小明有200元，买书花了66元，买文具花了12元，小明剩下的钱比原来少了多少元？
A: 小明剩下的钱比原来少了66+12=78元。

Q: 请翻译这段英文：Timmy was fined a large sum of money by the judge for drunken driving·
A: Timmy 因醉驾被处以高额罚金

Q: 贝多芬和柴可夫斯基在风格上有什么差异吗
A: 贝多芬和柴可夫斯基都是古典音乐历史上最重要的作曲家之一，他们的风格在某些方面存在差异。贝多芬的作品通常以严肃和内在的特质为特点，他的音乐常常呈现出深沉而丰富的情感。他的旋律通常是简单而优美的，强调和声变化和音乐构成。柴可夫斯基的作品则常常呈现出更为华丽和梦幻的特质，他的音乐常常具有戏剧性和歌唱性。柴可夫斯基的旋律常常更加复杂，强调和声和旋律的对比，音乐常常充满色彩和装饰。总的来说，贝多芬和柴可夫斯基的音乐风格在内省性和歌唱性方面存在着明显的差异，但两位作曲家在古典音乐史上都具有重要地位，他们的作品仍然被广泛演奏和赞扬。
```

```
Q: 写一篇高中青涩的爱情故事，男主是“我”，女主叫小美。我在高一喜欢上了小美。 开始写吧

A: 我叫陈默，是一个高一新生，在开学的第一天，我就对一个女孩一见钟情，她叫小美，是我班上的同学。那是一个阳光明媚的上午，我正在教室外走廊上，看着同学们有说有笑地走进教室，突然一个女孩吸引了我的目光。她穿着一条白色的连衣裙，在阳光下闪闪发光，她好像在看着我，我也对她微笑了一下，就这样，我们互相认识了。

接下来的日子里，我总是忍不住偷偷地看她，上课的时候，我总是不由自主地想到她，我甚至开始期待着每一次能和她见面。我开始给她写情书，每天放学后都会给她写一封信，表达我的思念和爱意。

但是，小美似乎并不怎么在意我，她总是跟她的好朋友有说有笑，好像对我置之不理。我感到很失落，但还是忍不住想要接近她。我会在课间的时候偷偷地看着她，在食堂吃饭的时候假装不经意地碰到她，在路上遇到她时跟她打招呼。

就这样，我坚持着每天给她写信，表达我的思念和爱意，直到高二的时候，小美终于给了我回应。我们开始一起上下学，一起吃午饭，一起做很多事情。我终于得到了她的爱，我感觉自己是世界上最幸福的人。

然而，我们的幸福并没有持续多久。高三的时候，小美开始变得忙碌起来，她要参加很多补习班和考试，我担心她会累垮，于是开始跟她吵架。最终，我们还是分手了，我很难过，感觉自己失去了最爱的人。

现在，我已经毕业多年，每当我看到小美，我还是会想起我们在一起的时光，我知道，那是我一生中最美好的回忆。
```

```
Q: 从零学习编程，请给我一个三个月的学习计划

A: 以下是一个三个月的学习计划，供您参考：

1. 第1-2周：Python基础
* 学习Python基础知识，如变量和数据类型、循环、条件语句、函数和方法等。
* 练习编程基础练习，如从键盘读取和写入数据、控制流语句和函数调用等。
1. 第3-4周：Python面向对象编程
* 学习Python中面向对象编程的基础知识，如类、方法、属性和方法、继承和多态等。
* 练习面向对象编程练习，如类创建、类调用和类组合等。
1. 第5-6周：Python高级主题
* 学习Python的高级主题，如异常、内存管理、调试技术和性能优化等。
* 练习高级主题练习，如异常处理、内存管理和性能优化等。
1. 第7-8周：Python Web开发
* 学习Python Web开发的基础知识，如Django框架、Flask框架和HTML、CSS和JavaScript等。
* 练习Web开发练习，如Django或Flask应用程序创建、HTTP请求和响应和用户界面设计等。
1. 第9-10周：项目实践
* 选择一个感兴趣的项目进行实践，如网络爬虫、数据分析、机器学习或Web开发等。
* 完成项目并进行演示和讲解。
1. 第11-12周：复习和强化
* 复习所学知识，并进行强化练习以加深理解。
* 参加考试以评估学习成果。

注意：学习计划仅供参考，您可以根据自己的学习节奏和兴趣进行调整。
```

```
Q: 实现一个Python函数以使用动态编程查找两个输入字符串的最长公共子序列

A: 这里有一个Python函数，使用动态编程查找两个输入字符串的最长公共子序列(LCS)：

def lcs(s1, s2):
   n = len(s1)
   m = len(s2)
   dp = [s1[0]]
   max_length = 0
   
   for i in range(1, n + 1):
       for j in range(1, m + 1):
           if s1[i-1] == s2[j-1]:
               dp.append(s1[i-1])
               max_length = max(max_length, j-i+1)
               
   return max(max_length, len(s1))

该函数使用动态规划来计算LCS。它从第一个字符串中的第一个字符开始，并将其添加到存储子序列的`dp`列表中。然后，它循环遍历两个字符串中的字符，如果它们相匹配，则将相应字符添加到`dp`列表中，并将`max_length`存储为当前字符串的最大长度。

最后，该函数返回`max_length`和两个输入字符串的长度之间的最大值，这表示LCS的长度。请注意，该函数假设输入字符串是字符串，而不是字符数组。如果要将其修改为处理数组，则需要相应地修改该函数。
```