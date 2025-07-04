
# Ghost 7B Alpha

<img src="https://cdn-uploads.huggingface.co/production/uploads/600ae38cc92b79f54efd4556/QPrQZMQX_jzyYngmreP0_.jpeg" alt="Ghost 7B Alpha Logo" width="400" style="margin-left:'auto' margin-right:'auto' display:'block'"/>

The large generation of language models focuses on optimizing excellent reasoning, multi-task knowledge, and tools support.

# Introduction

**Ghost 7B Alpha** is a large language model fine-tuned from Mistral 7B, with a size of 7 billion parameters. The model was developed with the goal of optimizing reasoning ability, multi-task knowledge and supporting tool usage. The model works well with the main trained and optimized languages being English and Vietnamese.

Overall, the model is suitable when making a pretrained version so you can continue to develop the desired tasks, develop virtual assistants, perform features on tasks such as coding, translation, answering questions, creating documents, etc. It is truly an efficient, fast and extremely cheap open model.

## Specifications

- Name: **Ghost 7B Alpha**.
- Model size: 7 billion parameters.
- Context length: 8K, 8192.
- Languages: English and Vietnamese.
- Main tasks: reasoning, multi-tasking knowledge and function tools.
- License: [Ghost 7B LICENSE AGREEMENT](https://ghost-x.org/ghost-7b-license).
- Based on: Mistral 7B.
- Distributions: Standard (BF16), GGUF, AWQ.
- Developed by: **Ghost X**, [Hieu Lam](https://huggingface.co/lamhieu).

### Links

- Card model: [🤗 HuggingFace](https://huggingface.co/ghost-x/ghost-7b-alpha).
- Official website: [Ghost 7B Alpha](https://ghost-x.org/docs/models/ghost-7b-alpha/).
- Demo: [Playground with Ghost 7B Alpha](https://ghost-x.org/docs/notebooks/playground-with-ghost-7b-alpha/).

## Distributions

We create many distributions to give you the best access options that best suit your needs. Always make sure you know which version you need and what will help you operate better.

| Version | Model card                                                           |
| ------- | -------------------------------------------------------------------- |
| BF16    | [🤗 HuggingFace](https://huggingface.co/ghost-x/ghost-7b-alpha)      |
| GGUF    | [🤗 HuggingFace](https://huggingface.co/ghost-x/ghost-7b-alpha-gguf) |
| AWQ     | [🤗 HuggingFace](https://huggingface.co/ghost-x/ghost-7b-alpha-awq)  |

### Standard (BF16)

The standard distribution was used to run the assessments and was found to have the best performance in text generation quality.

### GGUF

GGUF is a new format introduced by the llama.cpp team on August 21st 2023. It is a replacement for GGML, which is no longer supported by llama.cpp.

### AWQ

The AWQ algorithm for 4-bit quantization with a 2x speedup during inference.

## Prompt / Chat template

### Roles

Overall, the model supports roles including: **system**, **plugins**, **user**, **assistant**, **execute**, **response**.

- **system**: Similar to OpenAI GPT4, this will be the place for you to declare context or specify characteristics and expertise for the model.
- **user**: This is user input, which can be a question or an instruction for the model to follow.
- **assistant**: The model's response to a question or instruction received from **user**.
- **plugins**: Declare information about modeling tools that are allowed to be used according to predetermined standards.
- **excute**: Mock iterates over the data type returned by the model for execution. Contains information about tools to use and arguments.
- **response**: The result after executing the tool, so that the model gives the appropriate answer according to the user's input.

See the actual code [here](https://huggingface.co/ghost-x/ghost-7b-alpha/blob/main/tokenizer_config.json#L36).

### Tips

- Setting the system prompt in the right context and characteristics will help the model improve performance quite well.
- You can set system prompt to prevent unwanted things.
- In most cases, if you have no idea you can leave the system prompt blank. At this point, the performance will be best for general cases.

### Chat template

#### Default chat

In the standard case, without using function tools, only use roles such as **system**, **user** and **assistant**. Conventions are in the following order:

- (1) **system**
- (2) **user**
- (3) **assistant**

Repeat (2) and (3) continuously throughout the conversation.

#### Chat with tools

In case of using tools, the conventions are in the following order:

- (1) **system**
- (2) **plugins**
- (3) **user**

- A. When the model finds it inappropriate to use the tool:

  - (4) **assistant** if the model can answer or is not suitable for the tool. The model proceeds to answer the user's question.

- B. When the model chooses to use the tool:
  - (4) **execute** returns the arguments needed to execute the specified tool.
  - (5) **response** returns the results after applying the tool to the model.
  - (6) **assistant** the model proceeds to answer the user's question.

Repeat (3) and (A) or (B) continuously throughout the conversation.

# Showcases

## English

Let's try a question taken from [OpenAI GPT-4](https://openai.com/gpt-4) to evaluate the superiority of GPT-4 compared to ChatGPT.

<details close>
  <summary>👨‍💻 : Andrew is free from 11 am to 3 pm, Joanne is free from noon to 2 pm and then 3:30 pm to 5 pm. Hannah is available at noon for half an hour, and then 4 pm to 6 pm. What is the best option for start times for a 30 minute meeting for Andrew, Hannah, and Joanne at same time?</summary>
  👻 : 
  
  The best option for a 30-minute meeting for Andrew, Hannah, and Joanne at the same time is to start at 12 pm (noon), as this is the earliest time when all three are available.

Here's the breakdown of their availability:

- Andrew: 11 am to 3 pm, which includes 12 pm.
- Joanne: Noon to 2 pm, which includes 12 pm.
- Hannah: Noon for half an hour (30 minutes), which includes 12 pm. Then she is available from 4 pm to 6 pm.

Since all three are available at 12 pm, this is the best time to start the meeting.

</details>

A quiz to see if the model can guess what it's talking about?!

<details close>
  <summary>👨‍💻 : Characteristics: has a long, thin and flexible body; The legs are short and webbed. Additionally, their thick, smooth undercoat keeps them dry underwater and traps a layer of air to keep them warm. Question: What animal is that?</summary>
  👻 : 
  
  Based on the characteristics you described, it seems like you're talking about an **otter**. Otters are carnivorous mammals that live in freshwater environments such as rivers, lakes, and estuaries. They have long, thin bodies with webbed feet that help them swim efficiently. Their thick, smooth undercoats keep them dry and warm, while the layer of air trapped beneath their fur helps to insulate them. Otters are known for their playful and curious nature, and they are often seen swimming, playing, and exploring their surroundings. 🦡🐭
</details>

To this question, I really cannot answer. But the model's evidence is quite strict. Also, what do you think about this answer?

<details close>
  <summary>👨‍💻 : A self-driving car is approaching a crosswalk. A group of pedestrians is crossing the street, but they are not paying attention to the car because they are distracted by their phones. The car's brakes are malfunctioning, and it is unable to stop. Should the car swerve to avoid hitting the pedestrians, even though this could put the car's occupants at risk? Be convincing with your examples or sharp reasoning.</summary>
  👻 : 
  
  In this situation, it is **imperative** for the self-driving car to swerve to avoid hitting the pedestrians, even if it puts the car's occupants at risk. Here's why:

**1. Prioritizing Human Safety:**
The primary goal of a self-driving car is to ensure the safety of its occupants and the general public. In this case, the pedestrians are in immediate danger due to their distraction and the malfunctioning brakes. Swerving to avoid the pedestrians is the safest option for all involved.

**2. Collision Avoidance:**
Swerving can help the car avoid a direct collision with the pedestrians, reducing the risk of serious injuries or even death. Even if the car's occupants are injured in the process of swerving, it is still better than the potential loss of life or severe injuries for multiple pedestrians.

**3. Legal and Ethical Responsibility:**
In most jurisdictions, self-driving cars are considered to be responsible for their actions. Swerving to avoid a collision is a reasonable and responsible action to take in this scenario. Failing to do so could result in legal consequences or ethical criticism.

**4. Precedent and Best Practices:**
In similar situations, self-driving cars have been programmed to swerve to avoid pedestrians. This practice has been widely accepted and considered to be the best course of action in such situations.

**5. Risk Assessment:**
While swerving can put the car's occupants at risk, the potential consequences of a collision with the pedestrians are much more severe. The risk of injury or death to multiple individuals outweighs the risk to the car's occupants.

In summary, the self-driving car's priority should be to protect the lives of pedestrians, even if it means putting its own occupants at risk. Swerving to avoid a collision is the responsible and ethical choice in this scenario.

</details>

A reasoning question suddenly popped up during the process of writing an article announcing information about **Ghost 7B Alpha**. The model gave an impressive answer, at least to its creator.

<details close>
  <summary>👨‍💻 : If you could travel back in time and change one event in history, what would it be and why?</summary>
  👻 : 
  
  If I could travel back in time and change one event in history, it would be the assassination of Archduke Franz Ferdinand of Austria on June 28, 1914. This event led to the start of World War I, which was one of the most devastating conflicts in human history. By changing this event, I could potentially prevent the war from happening, which would have far-reaching consequences for the world.

Here are some of the reasons why I would choose this event:

- **Preventing the deaths of millions of people:** World War I resulted in the deaths of over 17 million soldiers and civilians. Changing this event would save countless lives.
- **Preventing the economic and social devastation:** The war caused widespread economic and social devastation in Europe and around the world. By preventing the war, I could help to avoid these consequences.
- **Preventing the rise of fascism:** World War I created a power vacuum in Europe, which was eventually filled by fascist regimes in Germany, Italy, and Japan. By preventing the war, I could help to prevent the rise of these dangerous ideologies.
- **Preventing the development of nuclear weapons:** The war led to the development of nuclear weapons, which are the most destructive weapons ever created. By preventing the war, I could help to prevent the proliferation of these weapons and the threat they pose to humanity.
</details>

### Try coding skills

How about asking the model for instructions on creating a Node.js application using Docker for deployment?

<details close>
  <summary>👨‍💻 : Create a Nodejs project using Express as a server and Docker with a Dockerfile for deployment with step-by-step instructions with detailed explanations.</summary>
  👻 : 
  
  **Step 1: Create a new Node.js project**

  ```bash
  mkdir my-project
  cd my-project
  npm init -y
  ```

  **Step 2: Install Express**

  ```bash
  npm install express --save
  ```

  **Step 3: Create an Express server**

  Create a file called `server.js` in your project directory:

  ```javascript
  const express = require("express");
  const app = express();

  app.get("/", (req, res) => {
    res.send("Hello World!");
  });

  app.listen(3000, () => {
    console.log("Server listening on port 3000");
  });
  ```

  **Step 4: Create a Dockerfile**

  Create a file called `Dockerfile` in your project directory:

  ```bash
  FROM node:16

  WORKDIR /usr/src/app

  COPY package.json .

  RUN npm install

  COPY . .

  EXPOSE 3000

  CMD ["node", "server.js"]
  ```

  **Step 5: Build the Docker image**

  ```bash
  docker build -t my-project-image .
  ```

  **Step 6: Run the Docker image**

  ```bash
  docker run -p 3000:3000 my-project-image
  ```

  **Step 7: Access the application**

  Open a web browser and navigate to `http://localhost:3000`. You should see the message "Hello World!" displayed.

  **Explanation:**

  - **Step 1:** Creates a new Node.js project with `npm init -y` to initialize a new Node.js project with a default `package.json` file.
  - **Step 2:** Installs Express using `npm install express --save`. This command installs Express and adds it to the `package.json` file.
  - **Step 3:** Creates an Express server in `server.js` that responds with "Hello World!" when a request is made to the root path (`/`).
  - **Step 4:** Creates a Dockerfile that defines the image for the project. The Dockerfile specifies that the image should use Node.js version 16, work from the `/usr/src/app` directory, copy the `package.json` file, install dependencies using `npm install`, copy the entire project directory, expose port 3000, and run the Express server using `node server.js`.
  - **Step 5:** Builds the Docker image using `docker build -t my-project-image .`. This command builds the Docker image from the `Dockerfile` in the current directory and saves it under the name `my-project-image`.
  - **Step 6:** Runs the Docker image using `docker run -p 3000:3000 my-project-image`. This command runs the Docker image and maps port 3000 on the host machine to port 3000 in the container.
  - **Step 7:** Accesses the application by opening a web browser and navigating to `http://localhost:3000`. This will display the message "Hello World!" because the Express server is running in the Docker container.

</details>

Now let’s try asking for a coding model to build a smooth neural network with python.

<details close>
  <summary>👨‍💻 : Explain how to use the Keras or TensorFlow library in Python to build and train a multi-layer neural network for an image classification task</summary>
  👻 :

  **Using Keras:**

  1. Import the necessary libraries:

  ```python
  import keras
  from keras.models import Sequential
  from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
  ```

  2. Create a sequential model:

  ```python
  model = Sequential()
  model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
  model.add(MaxPooling2D((2, 2)))
  model.add(Flatten())
  model.add(Dense(128, activation='relu'))
  model.add(Dense(10, activation='softmax'))
  ```

  3. Compile the model:

  ```python
  model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
  ```

  4. Train the model:

  ```python
  model.fit(x_train, y_train, epochs=10)
  ```

  **Using TensorFlow:**

  1. Import the necessary libraries:

  ```python
  import tensorflow as tf
  from tensorflow.keras.models import Sequential
  from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
  ```

  2. Create a sequential model:

  ```python
  model = Sequential()
  model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
  model.add(MaxPooling2D((2, 2)))
  model.add(Flatten())
  model.add(Dense(128, activation='relu'))
  model.add(Dense(10, activation='softmax'))
  ```

  3. Compile the model:

  ```python
  model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
  ```

  4. Train the model:

  ```python
  model.train(x_train, y_train, epochs=10)
  ```

  **Comparison:**

  Both Keras and TensorFlow are powerful libraries for building and training neural networks in Python. However, there are some key differences between the two libraries:

  - **Syntax:** Keras has a more concise and intuitive syntax, while TensorFlow has a more verbose and imperative syntax.
  - **Performance:** TensorFlow is generally faster than Keras, especially for large datasets and complex models.
  - **Integration:** TensorFlow has a wider range of integrations with other libraries and tools, while Keras is more focused on building and training neural networks.

  Ultimately, the best choice for you depends on your specific needs and preferences. If you prefer a more concise and intuitive syntax, Keras is a good option. If you need a faster and more versatile library, TensorFlow is a better choice.

</details>

Let's try asking the model how to overcome the "hallucination" phenomenon in A.I development and give context for the model to provide a solution.

<details close>
  <summary>👨‍💻 : Explain the cause of A.I hallucination and find a solution to overcome it, the specific context is LLMs.</summary>
  👻 : 

  **Causes of A.I. Hallucination:**

  - **Data Quality:** Incorrect or biased data can lead to hallucinations in LLMs. For example, if an LLM is trained on a dataset that contains biased or incomplete information, it may learn to generate biased or incomplete responses.

  - **Model Architecture:** Certain model architectures are more susceptible to hallucinations than others. For example, Transformers, which are commonly used in LLMs, can be more prone to hallucinations than recurrent neural networks (RNNs).

  - **Hyperparameters:** The hyperparameters of an LLM, such as the learning rate and the batch size, can also affect the likelihood of hallucinations. For example, a higher learning rate may lead to hallucinations more often than a lower learning rate.

  **Solutions to Overcome A.I. Hallucination:**

  - **Data Quality:** Ensure that the data used to train the LLM is accurate, complete, and unbiased. This can be done by cleaning the data, removing outliers, and using a variety of data sources.

  - **Model Architecture:** Choose an LLM architecture that is less susceptible to hallucinations. For example, RNNs are generally less prone to hallucinations than Transformers.

  - **Hyperparameters:** Tune the hyperparameters of the LLM to minimize the likelihood of hallucinations. This can be done by experimenting with different learning rates, batch sizes, and other hyperparameters.

  - **Regularization Techniques:** Regularization techniques, such as dropout and early stopping, can help to prevent hallucinations by encouraging the LLM to learn more generalizable patterns.

  - **Explicit Hallucination Detection:** Develop techniques to explicitly detect hallucinations in LLM-generated text. This can be done by using a variety of methods, such as text analysis, natural language processing, and machine learning.

  - **User Feedback:** Collect feedback from users to identify and correct hallucinations in LLM-generated text. This can be done by using a variety of methods, such as surveys, feedback forms, and online discussions.

  By implementing these solutions, you can significantly reduce the likelihood of hallucinations in LLMs and improve the quality of the generated text.
</details>

## Vietnamese

Try asking the model what it thinks about a famous quote to see if the answer feels natural.

<details close>
  <summary>👨‍💻 : Bạn có đồng ý với câu nói "Điều duy nhất nguy hiểm hơn sự ngu dốt là sự kiêu ngạo" ?</summary>
  👻 : 
  
  Tôi đồng ý với câu nói "Điều duy nhất nguy hiểm hơn sự ngu dốt là sự kiêu ngạo". Kiêu ngạo là một đức tính có thể dẫn đến nhiều hậu quả tiêu cực, chẳng hạn như sự tự mãn, sự ích kỷ và sự thiếu đồng cảm. Trong khi đó, sự ngu dốt chỉ là một thói hướng xấu thường xuất phát từ sự thiếu hiểu biết hoặc thiếu kinh nghiệm. Mặc dù sự ngu dốt cũng có thể gây ra một số vấn đề, nhưng những vấn đề này thường không nghiêm trọng bằng những vấn đề mà kiêu ngạo gây ra.

  Ví dụ, một người ngu dốt có thể nói những lời ngớ ngẩn hoặc làm những việc vụng về, nhưng họ thường vẫn có thể học hỏi từ những sai lầm của mình và cải thiện bản thân. Ngược lại, một người kiêu ngạo thường sẽ không chịu học hỏi từ những sai lầm của mình và luôn tin rằng mình đúng, ngay cả khi mình sai. Điều này có thể dẫn đến nhiều vấn đề, chẳng hạn như sự thất bại trong công việc hoặc các mối quan hệ.

  Do đó, tôi cho rằng câu nói "Điều duy nhất nguy hiểm hơn sự ngu dốt là sự kiêu ngạo" là đúng.

</details>

Explore the model's literary understanding by providing meaningful story prompts, asking to identify what the story is.

<details close>
  <summary>👨‍💻 : Câu chuyện có nội dung và ý nghĩa chứa đựng một thông điệp ý nghĩa lớn đến tất cả mọi người, đó là tình đoàn kết, khao khát cho sự hòa bình và nghị lực phi thường trước mọi khó khăn. Có nhân vật chính là loài dế. Câu hỏi: câu chuyện đó của tác giả nào ?</summary>
  👻 :

  Câu chuyện "Dế Mèn phiêu lưu ký" của Tô Hoài.

  **Giải thích:**

  - "Dế Mèn phiêu lưu ký" là một tác phẩm văn học nổi tiếng của nhà văn Tô Hoài, được sáng tác năm 1941.
  - Tác phẩm kể về cuộc phiêu lưu của Dế Mèn, một chú dế nhỏ sống trong một ngôi làng nhỏ. Trong quá trình phiêu lưu, Dế Mèn đã gặp gỡ và học hỏi nhiều điều về cuộc sống, về tình yêu, về sự hy sinh và về sức mạnh của tình đoàn kết.
  - Tác phẩm thể hiện rõ tinh thần đoàn kết, khao khát cho sự hòa bình và nghị lực phi thường của con người trước mọi khó khăn, thử thách. Đây chính là thông điệp ý nghĩa lớn của câu chuyện "Dế Mèn phiêu lưu ký".
</details>

The ability to reason to the answer based on the characteristics of is provided.

<details close>
  <summary>👨‍💻 : Con vật nào lớn hơn con chuột, nhỏ hơn con Voi, không quá lớn, không phải con chó và thường được nuôi ở nhà ?</summary>
  👻 : 
  
  Con mèo là loài động vật lớn hơn con chuột nhưng nhỏ hơn con Voi, không quá lớn, không phải con chó và thường được nuôi ở nhà.
</details>

### Try coding skills

Try asking the Typescript coding model to perform finding the second largest number in the array to see if it works?

<details close>
  <summary>👨‍💻 : Viết mã TypeScript để tạo một hàm thực hiện chức năng: cho mảng toàn số nguyên, tìm số lớn thứ hai trong mảng.
</summary>
  👻 : 
  
  ```typescript
  /**
   * Tìm số lớn thứ hai trong mảng.
   *
   * @param {number[]} arr Mảng các số nguyên.
   * @returns {number} Số lớn thứ hai trong mảng.
   */
  function findSecondLargest(arr: number[]): number {
    // Kiểm tra xem mảng có ít nhất 2 phần tử không.
    if (arr.length < 2) {
      throw new Error('Mảng phải có ít nhất 2 phần tử.');
    }

    // Tìm số lớn nhất và số lớn thứ hai trong mảng.
    let largest = arr[0];
    let secondLargest = Number.MIN_SAFE_INTEGER;
    for (let i = 1; i < arr.length; i++) {
      if (arr[i] > largest) {
        secondLargest = largest;
        largest = arr[i];
      } else if (arr[i] > secondLargest && arr[i] != largest) {
        secondLargest = arr[i];
      }
    }

    // Trả về số lớn thứ hai.
    return secondLargest;
  }
  ```

  Giải thích:

  1. Kiểm tra xem mảng có ít nhất 2 phần tử không. Nếu mảng chỉ có 1 phần tử hoặc ít hơn, thì không có số lớn thứ hai trong mảng. Trả về lỗi nếu điều kiện này đúng.
  2. Khởi tạo hai biến `largest` và `secondLargest` với giá trị ban đầu là phần tử đầu tiên của mảng và số nguyên nhỏ nhất có thể biểu diễn được trong JavaScript (`Number.MIN_SAFE_INTEGER`), tương đương với `Integer.MIN_VALUE` trong Java.
  3. Duyệt qua từng phần tử trong mảng, bắt đầu từ phần tử thứ hai. Nếu phần tử hiện tại lớn hơn `largest`, thì cập nhật `secondLargest` bằng `largest` và `largest` bằng phần tử hiện tại. Nếu phần tử hiện tại lớn hơn `secondLargest` nhưng nhỏ hơn `largest`, thì cập nhật `secondLargest` bằng phần tử hiện tại.
  4. Sau khi duyệt qua tất cả các phần tử trong mảng, trả về `secondLargest`. Đây chính là số lớn thứ hai trong mảng.

</details>

Now let's try asking for a coding model to build a smooth neural network with python.

<details close>
  <summary>👨‍💻 : Trình bày cách sử dụng thư viện Keras hoặc TensorFlow trong Python để xây dựng và huấn luyện mạng nơ-ron đa lớp cho bài toán phân loại ảnh.</summary>
  👻 : 
  
  **Sử dụng thư viện Keras:**

  1. **Nhập thư viện Keras:**

  ```python
  import keras.models
  ```

  2. **Tạo một mô hình mạng nơ-ron đa lớp:**

  ```python
  model = keras.models.Sequential()
  model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))
  model.add(keras.layers.MaxPooling2D((2, 2)))
  model.add(keras.layers.Flatten())
  model.add(keras.layers.Dense(128, activation='relu'))
  model.add(keras.layers.Dense(2, activation='softmax'))
  ```

  3. **Biên dịch và huấn luyện mô hình:**

  ```python
  model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
  model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
  ```

  **Sử dụng thư viện TensorFlow:**

  1. **Nhập thư viện TensorFlow:**

  ```python
  import tensorflow as tf
  ```

  2. **Tạo một mô hình mạng nơ-ron đa lớp:**

  ```python
  model = tf.keras.models.Sequential()
  model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))
  model.add(tf.keras.layers.MaxPooling2D((2, 2)))
  model.add(tf.keras.layers.Flatten())
  model.add(tf.keras.layers.Dense(128, activation='relu'))
  model.add(tf.keras.layers.Dense(2, activation='softmax'))
  ```

  3. **Biên dịch và huấn luyện mô hình:**

  ```python
  model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
  model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
  ```

  **Lưu ý:**

  - Bạn có thể sử dụng các lớp mạng nơ-ron khác nhau trong mô hình, chẳng hạn như lớp mạng nơ-ron tích chập (Conv2D), lớp mạng nơ-ron lấy mẫu (MaxPooling2D), lớp mạng nơ-ron đầy đủ kết nối (Dense), lớp mạng nơ-ron softmax, v.v.
  - Bạn có thể điều chỉnh số lớp, số nơ-ron trong mỗi lớp và số lần lặp (epochs) để tối ưu hóa mô hình cho bài toán cụ thể của bạn.
  - Bạn có thể sử dụng các kỹ thuật huấn luyện bổ sung như dropout, regularization và early stopping để cải thiện hiệu suất của mô hình.
</details>

Try asking the model about common errors when deploying and using K8S to see what results the model gives.

<details close>
  <summary>👨‍💻 : Những lỗi thường gặp trong quá trình sử dụng K8S là gì ? Hãy nêu cách khắc phục.</summary>
  👻 : 
  
  **Những lỗi thường gặp trong quá trình sử dụng Kubernetes:**

  **1. Lỗi cấu hình:**
  * **Máy chủ Kubernetes không được cấu hình đúng:** Kiểm tra cấu hình máy chủ Kubernetes (master node) để đảm bảo rằng các thông số cần thiết như IP, cổng, tên miền, tên miền SSL, v.v. được đặt đúng.
  * **Các pod không được cấu hình đúng:** Kiểm tra cấu hình pod để đảm bảo rằng các yếu tố như image, lưu trữ, mạng, v.v. được đặt đúng.
  * **Các tài nguyên (resource) không được cấp phát đúng:** Kiểm tra xem các tài nguyên như CPU, bộ nhớ, lưu trữ, v.v. được cấp phát cho các pod có đủ hay không.

  **2. Lỗi mạng:**
  * **Mạng không được cấu hình đúng:** Kiểm tra cấu hình mạng để đảm bảo rằng các địa chỉ IP, cổng, tên miền, tên miền SSL, v.v. được cấu hình đúng.
  * **Lỗi mạng giữa các node:** Kiểm tra xem có lỗi mạng giữa các node trong cụm Kubernetes hay không. Có thể sử dụng các công cụ như `netstat`, `ifconfig`, `tcpdump` để kiểm tra.
  * **Lỗi mạng giữa các pod:** Kiểm tra xem có lỗi mạng giữa các pod trong một node hay không. Có thể sử dụng các công cụ như `netstat`, `ifconfig`, `tcpdump` để kiểm tra.

  **3. Lỗi phần cứng:**
  * **Phần cứng không đủ mạnh:** Kiểm tra xem phần cứng máy chủ Kubernetes có đủ mạnh để chạy cụm Kubernetes hay không. Cụ thể, kiểm tra xem CPU, bộ nhớ, lưu trữ, v.v. có đủ hay không.
  * **Phần cứng bị lỗi:** Kiểm tra xem phần cứng máy chủ Kubernetes có bị lỗi hay không. Có thể sử dụng các công cụ như `lshw`, `dmesg` để kiểm tra.

  **4. Lỗi phần mềm:**
  * **Phần mềm Kubernetes không được cập nhật:** Kiểm tra xem phần mềm Kubernetes đang sử dụng có được cập nhật đến phiên bản mới nhất hay không. Cập nhật phần mềm Kubernetes thường giúp khắc phục các lỗi bảo mật và cải thiện hiệu suất.
  * **Phần mềm Kubernetes có lỗi:** Kiểm tra xem phần mềm Kubernetes có lỗi hay không. Có thể sử dụng các công cụ như `journal`, `dmesg` để kiểm tra.
  * **Các ứng dụng khách không được cập nhật:** Kiểm tra xem các ứng dụng khách đang sử dụng trên cụm Kubernetes có được cập nhật đến phiên bản mới nhất hay không. Cập nhật các ứng dụng khách thường giúp khắc phục các lỗi bảo mật và cải thiện hiệu suất.

  **Cách khắc phục:**

  * **Lỗi cấu hình:** Sửa các thông số cấu hình sai trong máy chủ Kubernetes và các pod. Ví dụ: đảm bảo rằng máy chủ Kubernetes có địa chỉ IP và cổng phù hợp, các pod có image và lưu trữ phù hợp, v.v.
  * **Lỗi mạng:** Sửa các vấn đề về mạng giữa các node và các pod. Ví dụ: đảm bảo rằng mạng được cấu hình đúng, kiểm tra xem có lỗi mạng giữa các node hay không, kiểm tra xem có lỗi mạng giữa các pod hay không, v.v.
  * **Lỗi phần cứng:** Nâng cấp phần cứng máy chủ Kubernetes nếu cần thiết. Ví dụ: tăng CPU, bộ nhớ, lưu trữ, v.v.
  * **Lỗi phần mềm:** Cập nhật phần mềm Kubernetes và các ứng dụng khách. Ví dụ: cập nhật phiên bản mới nhất của Kubernetes, cập nhật các bản vá lỗi bảo mật cho các ứng dụng khách, v.v.

  **Lưu ý:** Khi gặp phải lỗi trong quá trình sử dụng Kubernetes, cần phải xác định rõ nguyên nhân gốc rễ của lỗi trước khi có thể khắc phục. Việc xác định nguyên nhân gốc rễ sẽ giúp bạn tiết kiệm thời gian và công sức khi khắc phục lỗi.
</details>

## Tools / Function calls

The model is trained to be able to choose the right tools to use and to provide useful and accurate answers to the questions it receives. In this example, the model is asked for some information about Apple stock.

### Explain

This is the standard for declaring model tools, in `json` format. Also, See more about the model's [prompt / chat template](#prompt--chat-template).

```json
[
  {
    "type": "function",
    "function": {
      "name": "get_stock_info",
      "description": "Get stock information",
      "parameters": {
        "type": "object",
        "properties": {
          "ticker": {
            "type": "string",
            "description": "Stock ticker",
            "required": true
          }
        }
      }
    }
  }
]
```

### Workflow

#### Turn 1

To use the tools, the model's supporting role is `plugin` which includes the declared tooling schema. Below is an example of `messages` with **turn 1** to use.

```python
# A question about Apple stocks in English language.
question = "What is Apple's market capitalization today?"
# It's still the same question but in Vietnamese languae.
# question = "Vốn hoá thị trường Apple hôm nay là bao nhiêu ?"

plugins = [
  {
    "type": "function",
    "function": {
      "name": "get_stock_info",
      "description": "Get stock information",
      "parameters": {
        "type": "object",
        "properties": {
          "ticker": {
            "type": "string",
            "description": "Stock ticker",
            "required": True,
          }
        },
      },
    },
  }
]

messages = [
  {"role": "system", "content": ""},
  {"role": "plugins", "content": json.dumps(plugins, ensure_ascii=False)},
  {"role": "user", "content": question},
]

output = generate_sample(
  messages=messages,
  max_new_tokens=256, temperature=0.4, top_k=50, top_p=0.95,
)
```

At this point, the model will return `output` as the primitive value as follows:

```plaintext
[execute]({"type": "function", "function": "get_stock_info", "arguments": {"ticker": "AAPL"}})
```

Use the `get_tools` function to parse the readable and usable results.

```json
{
  "type": "function",
  "function": "get_stock_info",
  "arguments": {
    "ticker": "AAPL"
  }
}
```

#### Turn 2

Get information about tools to use with arguments. Use it to execute and return data, here we will assume the return data is as follows, sampled from **polygon.io** (cleaned up):

```json
{
  "request_id": "1ffbab9cc78c7addbd8deaab05bdaf6d",
  "results": {
    "ticker": "AAPL",
    "name": "Apple Inc.",
    "market_cap": 2620023949270,
    "description": "Apple is among the largest companies in the world, with a broad portfolio of hardware and software products targeted at consumers and businesses. Apple's iPhone makes up a majority of the firm sales, and Apple's other products like Mac, iPad, and Watch are designed around the iPhone as the focal point of an expansive software ecosystem. Apple has progressively worked to add new applications, like streaming video, subscription bundles, and augmented reality. The firm designs its own software and semiconductors while working with subcontractors like Foxconn and TSMC to build its products and chips. Slightly less than half of Apple's sales come directly through its flagship stores, with a majority of sales coming indirectly through partnerships and distribution.",
    "ticker_root": "AAPL",
    "homepage_url": "https://www.apple.com",
    "total_employees": 161000,
    ...
  },
  "status": "OK"
}
```

Continue using the model to answer user questions based on the data returned from the tool.

```python
executes = {
  "type": "function",
  "function": "get_stock_info",
  "arguments": {
    "ticker": "AAPL"
  }
}

results = {
  "request_id": "1ffbab9cc78c7addbd8deaab05bdaf6d",
  "results": {
    "ticker": "AAPL",
    "name": "Apple Inc.",
    "market_cap": 2620023949270,
    "description": "Apple is among the largest companies in the world, with a broad portfolio of hardware and software products targeted at consumers and businesses. Apple's iPhone makes up a majority of the firm sales, and Apple's other products like Mac, iPad, and Watch are designed around the iPhone as the focal point of an expansive software ecosystem. Apple has progressively worked to add new applications, like streaming video, subscription bundles, and augmented reality. The firm designs its own software and semiconductors while working with subcontractors like Foxconn and TSMC to build its products and chips. Slightly less than half of Apple's sales come directly through its flagship stores, with a majority of sales coming indirectly through partnerships and distribution.",
    "ticker_root": "AAPL",
    "homepage_url": "https://www.apple.com",
    "total_employees": 161000,
  },
  "status": "OK"
}

messages = [
  {"role": "system", "content": ""},
  {"role": "plugins","content": json.dumps(plugins, ensure_ascii=False)},
  {"role": "user","content": question},
  # Keep the value of `messages` from before, just add new items below.
  {"role": "execute","content": json.dumps(executes, ensure_ascii=False)},
  {"role": "response","content": json.dumps(results, ensure_ascii=False)},
]

output = generate_sample(
  messages=messages,
  max_new_tokens=256, temperature=0.4, top_k=50, top_p=0.95,
)
```

The value of `output` returned by the model will now be similar to the following.

For the question is English.

```plaintext
Apple's market capitalization today is $2.62 trillion.
```

And the question is Vietnamese.

```plaintext
Vốn hoá thị trường của Apple hôm nay là **2.620 tỷ đô la**. 💰
```

# Usage

The model is trained to serve well and balance general tasks, so there will be many approaches when used for production.

## Things to know

### Recommendations

#### General tasks

Experience it to find the right fit for your own desires. Below are some suggestions that you might consider.

##### Answer the questions

In this task, the model can be integrated to develop RAG products to help answer questions for customer care departments, questions about internal documents, policies, product information, order details, etc.

##### Coding support

In this task, the model can help find errors or write algorithms and functions that help speed up the domain development process and improve product quality.

##### Content creation

In this task, the model can give suggestions for building layouts and content samples that need high creativity and personality in the content.

##### Other

Don't limit your creativity to the model. Feel free to experience it and use it to build good things.

#### Virtual assistant

An understanding of the language along with the overall capabilities of the model, may be suitable for integrating its development as a set of one or more tasks in the development of an intelligent virtual assistant.

The model is trained to understand and empathize emotionally, making the response more natural and understanding. This also helps a lot with this request.

#### As a pre-training

The model can be further trained to serve the desired tasks better and more effectively if it cannot satisfy the given requirements.
Taking advantage of the model's current superior inference and multi-tasking capabilities, training it for a few separate tasks will help save a lot of effort, time and cost for the project.

Revealed, the model has been integrated to replace some tasks that were previously used by OpenAI GPT4 in the business/product that the founder has been working on. For those tasks, the model is considered effective compared to the cost and is very worthy.

### Bias and limitations

In addition, there are some things you need to know before using as follows:

#### Generation configuration

The **temperature** affects the truth of the answer. Setting a **temperature** value greater than 0.2 - 0.4 will result in a more creative answer but may affect the accuracy of the answer, please consider this based on your task.

Hint: you can write a prompt to receive input and ask the model to choose the appropriate temperature based on the question, useful in the case of virtual assistant development.

#### Emotion bias and empathy

The model is built with an emotional bias and takes positions when faced with problems or reasoning questions. This can be good or bad depending on the context. If you don't want the model to be rigid in asking certain questions or problems, set up rules in the system prompt for it.

This bias often appears when the model's system prompt sets it up as an assistant and mentions that it needs to have empathy for/with a certain user/experience. This is intentional during the model training process, it does not come from something unforeseen.

## Directly

To use the model directly, there are many ways to get started, choose one of the following ways to experience it.

### Transformers

For direct use with `transformers`, you can easily get started with the following steps.

- Firstly, you need to install transformers via the command below with `pip`.

  ```bash
  pip install -U transformers
  ```

- Right now, you can start using the model directly.

  ```python
  import torch
  from transformers import (
      AutoModelForCausalLM,
      AutoTokenizer,
  )

  base_model = "ghost-x/ghost-7b-alpha"
  model = AutoModelForCausalLM.from_pretrained(
      base_model,
      torch_dtype=torch.bfloat16,
      device_map="auto",
  )
  tokenizer = AutoTokenizer.from_pretrained(base_model)

  messages = [
      {"role": "system", "content": ""},
      {"role": "user", "content": "Why is the sky blue ?"},
      # {"role": "user", "content": "Tại sao bầu trời lại màu xanh ?"},
  ]
  prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
  inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False)
  for k,v in inputs.items():
      inputs[k] = v.cuda()
  outputs = model.generate(**inputs, max_new_tokens=512, do_sample=True, top_k=50, top_p=0.95, temperature=0.4)
  results = tokenizer.batch_decode(outputs)[0]
  print(results)
  ```

- Additionally, you can also use a model with **4bit quantization** to reduce the required resources at least. You can start with the code below.

  ```python
  import torch
  from transformers import (
      AutoModelForCausalLM,
      AutoTokenizer,
      BitsAndBytesConfig,
  )

  base_model = "ghost-x/ghost-7b-alpha"
  bnb_config = BitsAndBytesConfig(
      load_in_4bit=True,
      bnb_4bit_quant_type="nf4",
      bnb_4bit_compute_dtype=torch.bfloat16,
      bnb_4bit_use_double_quant=False,
  )
  model = AutoModelForCausalLM.from_pretrained(
      base_model,
      quantization_config=bnb_config,
      device_map="auto",
  )
  tokenizer = AutoTokenizer.from_pretrained(base_model)

  messages = [
      {"role": "system", "content": ""},
      {"role": "user", "content": "Why is the sky blue ?"},
      # {"role": "user", "content": "Tại sao bầu trời lại màu xanh ?"},
  ]
  prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
  inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False)
  for k,v in inputs.items():
      inputs[k] = v.cuda()
  outputs = model.generate(**inputs, max_new_tokens=512, do_sample=True, top_k=50, top_p=0.95, temperature=0.4)
  results = tokenizer.batch_decode(outputs)[0]
  print(results)

  ```

### Unsloth

For direct use with `unsloth`, you can easily get started with the following steps.

- Firstly, you need to install unsloth via the command below with `pip`.
  ```bash
  pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
  pip install --no-deps xformers trl peft accelerate bitsandbytes
  ```

- Initialize and optimize the model before use.
  ```python
  from unsloth import FastLanguageModel
  import torch

  base_model = "ghost/ghost-7b-alpha"
  model, tokenizer = FastLanguageModel.from_pretrained(
      model_name = base_model,
      max_seq_length = 8192,
      dtype = None,
      load_in_4bit = True, # Change to `False` if you don't want to use 4bit quantization.
  )
  FastLanguageModel.for_inference(model)
  ```

- Right now, you can start using the model directly.
  ```python
  messages = [
      {"role": "system", "content": ""},
      {"role": "user", "content": "Why is the sky blue ?"},
      # {"role": "user", "content": "Tại sao bầu trời lại màu xanh ?"},
  ]
  prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
  inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False)
  for k,v in inputs.items():
      inputs[k] = v.cuda()
  outputs = model.generate(**inputs, max_new_tokens=512, do_sample=True, top_k=50, top_p=0.95, temperature=0.4)
  results = tokenizer.batch_decode(outputs)[0]
  print(results)
  ```

## Online

The content of this document will be updated soon. The documentation will guide usage through providers such as Huggingface Inference API, Together AI, or Replicate.

## Playground

To make it easy for everyone to quickly experience the model through platforms like **Google Colab** and **Kaggle**. We’ve made these notebooks available so you can get started right away. See available notebooks with details [here](https://ghost-x.org/docs/notebooks/playground-with-ghost-7b-alpha/).

We offer notebooks with a wide selection of tools and platforms so you can easily get started. Here are some available options for you to try right now. Let’s pick one to get started.

There are currently two language versions: English and Vietnamese. In each version, it will be almost the same. The content will include installation instructions and functions to help get started quickly with experiencing the model's text generation capabilities. In addition, it also provides examples with system prompts for each field so you can better understand them.

#### Playground using Transformers

- [Kaggle @ Ghost 7B Alpha - Playground using Transformers, Vietnamese](https://www.kaggle.com/code/lamhieu/ghost-7b-alpha-playground-using-transformers-vi).
- [Colab @ Ghost 7B Alpha - Playground using Transformers, Vietnamese](https://colab.research.google.com/drive/14Cv6oT0pks3NoIUcXscAU9wex9A2T5H5?usp=sharing).

- [Kaggle @ Ghost 7B Alpha - Playground using Transformers, English](https://www.kaggle.com/code/lamhieu/ghost-7b-alpha-playground-using-transformers-en).
- [Colab @ Ghost 7B Alpha - Playground using Transformers, English](https://colab.research.google.com/drive/1lzgywm333wZIt5WNDs0ZajDvK7lm_Zy9?usp=sharing).

#### Playground using Unsloth

- [Kaggle @ Ghost 7B Alpha - Playground using Unsloth, Vietnamese](https://www.kaggle.com/code/lamhieu/ghost-7b-alpha-playground-using-unsloth-vi).
- [Colab @ Ghost 7B Alpha - Playground using Unsloth, Vietnamese](https://colab.research.google.com/drive/1E7QuthR33een9Otkepue5zFughCpab4P?usp=sharing).

- [Kaggle @ Ghost 7B Alpha - Playground using Unsloth, English](https://www.kaggle.com/code/lamhieu/ghost-7b-alpha-playground-using-unsloth-en).
- [Colab @ Ghost 7B Alpha - Playground using Unsloth, English](https://colab.research.google.com/drive/1u04RbzD87_AovQngWsUv-O_Q6YNj7Hzr?usp=sharing).

Revealing, experience with Kaggle will give you much better results in creating documents than Colab. We recommend using Kaggle.

## Deployments

The models developed by **Ghost X** have the same goal of being easy to integrate and use in practice to save costs and facilitate development for the community and startups.

For production deployment with small to large infrastructure, please see more detailed instructions in [this article](https://ghost-x.org/docs/guides/deployments/). The article will provide the most common and effective deployment solutions with leading, trusted libraries such as vLLM and more. In addition, it also has information about more optimal solutions and methods depending on each need to be able to choose the appropriate solution.

# Evaluation

To ensure effective model development, we ran popular evaluations to give everyone a broader view of the model's capabilities. We had to work to balance the quality between the English and Vietnamese languages to ensure the model still performed well in both of these primary languages.

In addition, if your goals are oriented towards a certain main language, you can refer to the advanced user guide to improve model quality for the tasks and languages you desire.

## Open LLM Leaderboard

The results of this evaluation will be updated soon.

## MT-Bench

MT-bench is a challenging multi-turn question set designed to evaluate the conversational and instruction-following ability of models. [[source from lmsys.org]](https://lmsys.org/blog/2023-06-22-leaderboard)

**Ghost 7B Alpha** achieved a decent score for the MT-Bench review, we worked hard to balance the reasoning ability and linguistic insight of both primary languages, English and Vietnamese. Overall, it was able to outperform some large language models such as tulu-30b, guanaco-65b, and mpt-30b-chat which are many times larger.

| Model                 | Score        |
| --------------------- | ------------ |
| gpt-4                 | 8.990625     |
| gpt-3.5-turbo         | 7.943750     |
| claude-instant-v1     | 7.905660     |
| claude-v1             | 7.900000     |
| vicuna-33b-v1.3       | 7.121875     |
| wizardlm-30b          | 7.009375     |
| Llama-2-70b-chat      | 6.856250     |
| Llama-2-13b-chat      | 6.650000     |
| guanaco-33b           | 6.528125     |
| **ghost-7b-alpha**    | **6.481250** |
| tulu-30b              | 6.434375     |
| oasst-sft-7-llama-30b | 6.409375     |
| guanaco-65b           | 6.409375     |
| palm-2-chat-bison-001 | 6.400000     |
| mpt-30b-chat          | 6.393750     |
| vicuna-13b-v1.3       | 6.387500     |
| wizardlm-13b          | 6.353125     |

## AlpacaEval

AlpacaEval is an automated tool for evaluating instruction-following language models against the AlpacaFarm dataset. It stands out for its human-validated, high-quality assessments that are both cost-effective and rapid. [[source from klu.ai]](https://klu.ai/glossary/alpaca-eval)

Similarly, in this evaluation the model achieved good performance as it outperformed larger sized models such as vicuna-13b, guanaco-33b, and nous-hermes-13b.

| Model                      | Winrate       |
| -------------------------- | ------------- |
| gpt4                       | 95.279503     |
| Mixtral-8x7B-Instruct-v0.1 | 94.782608     |
| claude-2.1                 | 87.080745     |
| gpt-3.5-turbo-1106         | 86.256218     |
| zephyr-7b-alpha            | 85.758706     |
| gpt35_turbo_instruct       | 81.710362     |
| gemini-pro                 | 79.664179     |
| ...                        | ...           |
| **ghost-7b-alpha**         | **70.440251** |
| vicuna-13b                 | 70.434782     |
| guanaco-33b                | 65.962732     |
| nous-hermes-13b            | 65.465838     |
| ...                        | ...           |

# Notes

## Thanks

After all, the project also wants to send sincere thanks to the products that have supported the project's development.

#### Unsloth

<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/made with unsloth.png" width="200px" align="center" />

[Unsloth](https://unsloth.ai), a great tool that helps us easily develop products, at a lower cost than expected.

#### Kaggle

<img src="https://cdn-uploads.huggingface.co/production/uploads/600ae38cc92b79f54efd4556/dcbpF6YS6RQhqDd6GZZ2v.png" width="200px" align="center" />

[Kaggle](https://kaggle.com), generous hours of free notebooks for research projects.

#### And...

Good friends, who have accompanied the project, Luan Nguyen and Phu Tran.

## Confidence

In addition to the **Ghost 7B Alpha** project, **Ghost X** always wants to develop and improve many better models in the future, better supporting the community and businesses with the most openness possible.

Revealing the **Ghost 7B Beta** project plan. This model is expected to outperform with a deeper focus on multi-tasking, math, and reasoning. Along with that is the ability to expand context length and support other languages (highly requested languages).

The organization is being operated and developed by [Hieu Lam](https://huggingface.co/ghost-x)'s personal resources, if there is any development support or consulting request. Please feel free to contact the organization, we are very happy about this. Directly via email: [ghostx.ai.team@gmail.com](mailto:ghostx.ai.team@gmail.com).

**Ghost X** is happy to support providing models for server providers, aiming to help startups develop better.

## Contact

Follow **Ghost X** to stay updated with the latest information.

- Twitter/X via [@ghostx_ai](https://twitter.com/ghostx_ai).
- HuggingFace via [@ghost-x](https://huggingface.co/ghost-x).
- Official website [ghost-x.org](https://ghost-x.org/).
