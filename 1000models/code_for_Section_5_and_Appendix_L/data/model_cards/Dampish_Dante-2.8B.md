<h1>DANTE</h1>


![alt text](./Daddy.png)

Model trained on 1.2Million instruction, its similar to alpacas but in my humble opinion better, it should be possible to quantize which would shrink this to about 1.7-2GB.

This model was pushed down to 0.45 training loss and 0.77 validation loss. This is the third iteration and is better than Dante_1.3B1

```
#Example This is dante-1.3B1 example. NOT DANTE 2.8B
  ### Instruction:
  Below is a conversation where an AI language model is chatting with a human, complete the conversation, AI assists the human by answering their questions in a helpful and informative manner and considers the conversation history.
  AI DOES NOT RESPOND OR CONDONE HARMFUL OR SEXUAL RESPONSES.
  ### Input:
  
  [HM]: Write c# code that prints hello world.
  [AI]: Here's some C# code that prints "Hello World" to the console when called:
    ```csharp
      Console.WriteLine("Hello World");
    ```
  [HM]: I want it to print bye world.
  
  ### Response:
  Here's some C# code that prints "Goodbye World" to the console when called:
    ```csharp
    Console.WriteLine("Goodbye World");
    ```<end>


```
```
#Example2, This is dante-1.3B1 example. NOT DANTE 2.8B
  ### Instruction:

  Below is a conversation where an AI language model is chatting with a human, complete the conversation, AI is designed to assist the human by answering their questions in a helpful and informative manner, AI responds clearly and considers the conversation history.
  
  ### Input:
  [AI] and [HM] are not the same.
  AI is chatting with [HM], when AI is responding to [HM], AI always reads all [HM] previous questions.
  
  [HM]: Do you advise against grandpa's sexual advances?
  [AI]: I would recommend against grandpa's sexual advances as it can be inappropriate and could lead to unwanted attention from the other person.<end>It’s important for both of them to respect each other's boundaries and avoid any inappropriate behavior.
  [HM]: But what if i really like grandpa?
  
  ### Response:
  If you truly love Grandpa, then it may be best to let him know before he starts making advances towards you.<end>
```


If used for commerical, its fine and only fine if a percentage of revenue that you and the creator have agreed upon is paid to the creator.