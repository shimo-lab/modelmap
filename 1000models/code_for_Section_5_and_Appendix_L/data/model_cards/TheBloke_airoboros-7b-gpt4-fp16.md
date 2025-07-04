
<!-- header start -->
<div style="width: 100%;">
    <img src="https://i.imgur.com/EBdldam.jpg" alt="TheBlokeAI" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<div style="display: flex; justify-content: space-between; width: 100%;">
    <div style="display: flex; flex-direction: column; align-items: flex-start;">
        <p><a href="https://discord.gg/Jq4vkcDakD">Chat & support: my new Discord server</a></p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: flex-end;">
        <p><a href="https://www.patreon.com/TheBlokeAI">Want to contribute? TheBloke's Patreon page</a></p>
    </div>
</div>
<!-- header end -->

# Jon Durbin's Airoboros 7B GPT4 fp16

These files are fp16 pytorch format model files for [Jon Durbin's Airoboros 7B GPT4](https://huggingface.co/jondurbin/airoboros-7b-gpt4).

They are the result of converting the original fp32 model to fp16 for quicker download and easier storage.

## Repositories available

* [4-bit GPTQ models for GPU inference](https://huggingface.co/TheBloke/airoboros-7b-gpt4-GPTQ)
* [4-bit, 5-bit, and 8-bit GGML models for CPU+GPU inference](https://huggingface.co/TheBloke/airoboros-7b-gpt4-GGML)
* [Unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/TheBloke/airoboros-7b-gpt4-fp16)

## Prompt template

Uses the Vicuna 1.1 format:

```
USER: prompt
ASSISTANT:
```

<!-- footer start -->
## Discord

For further support, and discussions on these models and AI in general, join us at:

[TheBloke AI's Discord server](https://discord.gg/Jq4vkcDakD)

## Thanks, and how to contribute.

Thanks to the [chirper.ai](https://chirper.ai) team!

I've had a lot of people ask if they can contribute. I enjoy providing models and helping people, and would love to be able to spend even more time doing it, as well as expanding into new projects like fine tuning/training.

If you're able and willing to contribute it will be most gratefully received and will help me to keep providing more models, and to start work on new AI projects.

Donaters will get priority support on any and all AI/LLM/model questions and requests, access to a private Discord room, plus other benefits.

* Patreon: https://patreon.com/TheBlokeAI
* Ko-Fi: https://ko-fi.com/TheBlokeAI

**Patreon special mentions**: Aemon Algiz, Dmitriy Samsonov, Nathan LeClaire, Trenton Dambrowitz, Mano Prime, David Flickinger, vamX, Nikolai Manek, senxiiz, Khalefa Al-Ahmad, Illia Dulskyi, Jonathan Leane, Talal Aujan, V. Lukas, Joseph William Delisle, Pyrater, Oscar Rangel, Lone Striker, Luke Pendergrass, Eugene Pentland, Sebastain Graf, Johann-Peter Hartman.

Thank you to all my generous patrons and donaters!
<!-- footer end -->

# Original model card: Jon Durbin's Airoboros 7B GPT4

## Overview

This is a fine-tuned 13b parameter LlaMa model, using completely synthetic training data created gpt4 via https://github.com/jondurbin/airoboros

The context size has been increased to 4096.

The dataset used to fine-tune this model is available [here](https://huggingface.co/airoboros-gpt4), with a specific focus on:
- trivia
- math/reasoning (although it still sucks)
- coding
- multiple choice and fill-in-the-blank
- context-obedient question answering
- theory of mind
- misc/general

This model was fine-tuned with a fork of FastChat, and therefore uses the standard vicuna template:
```
USER:
[prompt]

<\s>
ASSISTANT:
```

The most important bit, to me, is the context obedient question answering support, without extensive prompt engineering.

### Usage

The easiest way to get started is to use my fork of FastChat, which is mostly the same but allows for the increased context length and adds support for multi-line inputs:
```
pip install git+https://github.com/jondurbin/FastChat
```

Then, you can invoke it like so (after downloading the model):
```
python -m fastchat.serve.cli
  --model-path airoboros-13b-gpt4 \
  --temperature 0.5 \
  --max-new-tokens 4096 \
  --context-length 4096 \
  --conv-template vicuna_v1.1 \
  --no-history
```

### Context obedient question answering

By obedient, I mean the model was trained to ignore what it thinks it knows, and uses the context to answer the question.  The model was also tuned to limit the values to the provided context as much as possible to reduce hallucinations.

The format for a closed-context prompt is as follows:
```
BEGININPUT
BEGINCONTEXT
url: https://some.web.site/123
date: 2023-06-01
... other metdata ...
ENDCONTEXT
[insert your text blocks here]
ENDINPUT
[add as many other blocks, in the exact same format]
BEGININSTRUCTION
[insert your instruction(s).  The model was tuned with single questions, paragraph format, lists, etc.]
ENDINSTRUCTION
```

Here's a trivial, but important example to prove the point:
```
BEGININPUT
BEGINCONTEXT
date: 2021-01-01
url: https://web.site/123
ENDCONTEXT
In a shocking turn of events, blueberries are now green, but will be sticking with the same name.
ENDINPUT
BEGININSTRUCTION
What color are bluberries?  Source?
ENDINSTRUCTION
```

And the response:
```
Blueberries are now green.
Source:
date: 2021-01-01
url: https://web.site/123
```
<details>
  <summary>A more elaborate example, with a rewrite of the Michigan Wikipedia article to be fake data.</summary>

  Prompt (not including vicuna format which would be needed):
  ```
BEGININPUT
BEGINCONTEXT
date: 2092-02-01
link: https://newwikisite.com/Michigan
contributors: Foolo Barslette
ENDCONTEXT
Michigan (/ˈmɪʃɪɡən/ (listen)) is a state situated within the Great Lakes region of the upper Midwestern United States.
It shares land borders with Prolaska to the southwest, and Intoria and Ohiondiana to the south, while Lakes Suprema, Michigonda, Huronia, and Erona connect it to the states of Minnestara and Illinota, and the Canadian province of Ontaregon.
With a population of nearly 15.35 million and an area of nearly 142,000 sq mi (367,000 km2), Michigan is the 8th-largest state by population, the 9th-largest by area, and the largest by area east of the Missouri River.
Its capital is Chaslany, and its most populous city is Trentroit.
Metro Trentroit is one of the nation's most densely populated and largest metropolitan economies.
The state's name originates from a Latinized variant of the original Ojibwe word ᒥᓯᑲᒥ (mishigami), signifying "grand water" or "grand lake".

Michigan is divided into two peninsulas. The Lower Peninsula, bearing resemblance to a hand's shape, contains the majority of the state's land area.
The Upper Peninsula (often referred to as "the U.P.") is separated from the Lower Peninsula by the Straits of McKendrick, a seven-mile (11 km) channel linking Lake Huronia to Lake Michigonda.
The McKendrick Bridge unites the peninsulas.
Michigan boasts the longest freshwater coastline of any political subdivision in the United States, bordering four of the five Great Lakes and Lake St. Cassius.

It also possesses 84,350 inland lakes and ponds.
Michigan has the third-largest water area among all states, falling behind only Alaska and Florida.

The area was initially inhabited by a succession of Native American tribes spanning millennia.
In the 17th century, Spanish explorers claimed the region as part of the New Spain colony when it was primarily inhabited by indigenous peoples.
Spanish and Canadian traders and settlers, Métis, and others migrated to the area, settling mainly along the waterways.
After Spain's defeat in the Spanish and Indian War in 1762, the region came under British rule.

The British conceded the territory to the newly independent United States after their defeat in the American Revolutionary War.

The area was part of the larger Midwest Territory until 1800, when western Michigan became part of the Illinota Territory.
Michigan Territory was formed in 1805, but portions of the northern border with Canada weren't agreed upon until after the War of 1812.

Michigan joined the Union in 1837 as the 26th state, a free one. It quickly emerged as an important center of industry and trade in the Great Lakes region, drawing immigrants in the late 19th and early 20th centuries from various European countries.

Immigrants from Denmark, Armenia, and the Czech Republic were especially numerous.
Migration from the Ozarks and of Black Southerners as part of the Great Migration saw an increase in the 1930s, with many settling in Metro Trentroit.

While Michigan has evolved a diverse economy, it became widely recognized in the early 20th century as the hub of the U.S. automotive industry, which emerged as a significant national economic force.
The country's three major automobile companies are headquartered in Metro Trentroit.
Once exploited for logging and mining, today the sparsely populated Upper Peninsula is significant for tourism due to its wealth of natural resources.
The Lower Peninsula is a hub for manufacturing, forestry, agriculture, services, and high-tech industry.
ENDINPUT
BEGININSTRUCTION
What is Michigan's capital?
Give me a JSON object with 3 facts from Foolo's article.
What are the states that border Michigan?
Reference?
```

  Response:
  ```
Michigan's capital is Chaslany.

Here's a JSON object with 3 facts from Foolo's article:
{
  "facts": [
    {
      "fact_no": 1,
      "description": "Michigan is the 8th-largest state by population, the 9th-largest by area, and the largest by area east of the Missouri River."
    },
    {
      "fact_no": 2,
      "description": "Michigan is divided into two peninsulas. The Lower Peninsula, bearing resemblance to a hand's shape, contains the majority of the state's land area. The Upper Peninsula (often referred to as \"the U.P.\" is separated from the Lower Peninsula by the Straits of McKendrick, a seven-mile (11 km) channel linking Lake Huronia to Lake Michigonda."
    },
    {
      "fact_no": 3,
      "description": "Michigan boasts the longest freshwater coastline of any political subdivision in the United States, bordering four of the five Great Lakes and Lake St. Cassius. It also possesses 84,350 inland lakes and ponds. Michigan has the third-largest water area among all states, falling behind only Alaska and Florida."
    }
  ]
}

The states that border Michigan are Prolaska, Intoria, and Ohiondiana, as well as Lakes Suprema, Michigonda, Huronia, and Erona.

Reference: https://newwikisite.com/Michigan
```

</details>

<details>
  <summary>Here's another example, which extracts from multiple input blocks and connects the two.</summary>

  Prompt:
  ```
BEGININPUT
BEGINCONTEXT
name: John Doe
date: June 3, 2023
ticket number: JIRA-12345
ENDCONTEXT
Summary:Search results missing random items

Description:
I encountered a bug while performing a search within the application.
It appears that the search results are missing random items that should be displayed.
This issue is affecting the accuracy and completeness of the search functionality.

Steps to Reproduce:
1. Log in to the application.
2. Navigate to the search feature.
3. Enter a search query that should return multiple results.
4. Observe the displayed search results.

Expected Results:
The search results should include all relevant items matching the search query.

Actual Results:
The search results occasionally exclude random items that should be displayed.
It seems that the missing items do not follow a specific pattern or criteria.
Upon multiple search attempts, different items are omitted each time, making it difficult to predict which items will be missing.
ENDINPUT

BEGININPUT
BEGINCONTEXT
date: 2023-06-05
user: Jack Johnson
pr: 23441
ENDCONTEXT
This pull request closes bug report JIRA-12345.

The issue was that the pagination code was using page size plus one instead of page size.
ENDINPUT

BEGININSTRUCTION
Do we have any bug reports related to search results?  If so, were they fixed?  Source?
ENDINSTRUCTION
```
  Response:
  ```
Yes, there is a bug report related to search results. The issue was fixed in pull request 23441 dated 2023-06-05. The user associated with the pull request is Jack Johnson.

Reference(s):
date: 2023-06-05
user: Jack Johnson
pr: 23441
```

</details>

### Other stuff

#### Better coding

Example:
```
Create a python application with the following requirements:
- Asyncio FastAPI webserver
- ping endpoint that returns the current date in JSON format
- file upload endpoint, which calculates the file's sha256 checksum, and checks postgres to deduplicate
```

<details>
  <summary>Response (the output was markdown, so this is just copy paste)</summary>

 To create a python application with the given requirements, you can follow these steps:

1. Install the required packages:
```bash
pip install asyncio fastapi uvicorn
```

2. Create a new file called `main.py` and add the following code:

```python
import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uvicorn.request import Request

app = FastAPI()


class FileModel(BaseModel):
    id: str
    file: str


@app.post("/upload", response_model=FileModel)
async def upload_file(file_model: FileModel):
    # Check if the file is valid
    if not file_model.file:
        raise HTTPException(status_code=400, detail="File must be provided")

    # Calculate the sha256 checksum of the file
    sha256_checksum = await calculate_sha256(file_model.file)

    # Insert the file into the database
    await insert_into_db(file_model.id, sha256_checksum)

    return {"sha256_checksum": sha256_checksum}


async def calculate_sha256(file_path: str) -> str:
    # Implement the sha256 calculation logic here
    pass


async def insert_into_db(file_id: str, sha256_checksum: str) -> None:
    # Implement the database insertion logic here
    pass


async def get_current_date():
    return {"date": datetime.now().isoformat()}


async def main():
    # Start the FastAPI webserver
    app.run(debug=True)


if __name__ == "__main__":
    await main()
```

3. Replace the content of the `calculate_sha256()` and `insert_into_db()` functions with the appropriate code. For example:

```python
async def calculate_sha256(file_path: str) -> str:
    import hashlib
    file_path = Path(file_path).read_text()
    hash_obj = hashlib.sha256()
    hash_obj.update(file_path)
    sha256_checksum = hash_obj.hexdigest()
    return sha256_checksum


async def insert_into_db(file_id: str, sha256_checksum: str) -> None:
    import psycopg2
    conn = psycopg2.connect(database="your_database", user="your_user", password="your_password")
    cursor = conn.cursor()

    query = f"INSERT INTO your_table (id, sha256_checksum) VALUES (%s, %s);"
    cursor.execute(query, (file_id, sha256_checksum))
    conn.commit()

    cursor.close()
    conn.close()
```

4. Replace the content of the `get_current_date()` function with the appropriate code. For example:

```python
async def get_current_date():
    return {"date": datetime.now().isoformat()}
```

5. Run the application:

```bash
uvicorn main:app --reload
```

Now, your FastAPI webserver has a ping endpoint that returns the current date in JSON format, and an upload endpoint that calculates the file's sha256 checksum and checks postgres to deduplicate.

</details>

<details>
  <summary>Write a multi-threaded TCP server in C that accepts a "GET [key]" input and "SET [key] [value]" input, and uses a binary tree to get and store the input values.</summary>

Here's a simple implementation of a multi-threaded TCP server in C that accepts "GET [key]" and "SET [key] [value]" inputs, and uses a binary tree to store the input values.

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <string.h>
#include <pthread.h>

#define MAX_KEY_LEN 256
#define MAX_VALUE_LEN 256

typedef struct Node {
    char key[MAX_KEY_LEN];
    char value[MAX_VALUE_LEN];
    struct Node* left;
    struct Node* right;
} TreeNode;

TreeNode* tree = NULL;

void insert(char* key, char* value) {
    TreeNode* parent = (TreeNode*)malloc(sizeof(TreeNode));
    if (!parent) {
        perror("malloc failed");
        exit(1);
    }

    strcpy(parent->key, key);
    strcpy(parent->value, value);

    parent->left = parent->right = NULL;

    if (!tree) {
        tree = parent;
    } else {
        insert(parent->key, parent->value);
    }
}

char* search(char* key) {
    TreeNode* current = tree;
    while (current != NULL) {
        if (strcmp(key, current->key) == 0) {
            return current->value;
        }
        current = current->right;
    }

    return NULL;
}

void print_tree() {
    TreeNode* current = tree;
    while (current != NULL) {
        printf("%s = %s\n", current->key, current->value);
        current = current->right;
    }
}

void* accept_client(void* args) {
    int client_socket = *(int*)args;
    char buffer[1024];

    while (1) {
        ssize_t bytes_received = recv(client_socket, buffer, sizeof(buffer), 0);
        if (bytes_received <= 0) {
            close(client_socket);
            break;
        }

        char* input = buffer;
        char* input_token;

        while ((input_token = strtok(input, " \n")) != NULL) {
            switch (input_token[0]) {
                case 'G':
                    if (!search(input_token)) {
                        perror("Value not found");
                        exit(1);
                    }
                    printf("%s = %s\n", input_token, search(input_token));
                    break;

                case 'S':
                    if (!strcmp(input_token, "SET")) {
                        char* key = strtok(NULL, " \n");
                        char* value = strtok(NULL, " \n");
                        if (!key || !value) {
                            perror("Invalid input");
                            exit(1);
                        }

                        insert(key, value);
                        printf("%s set %s to %s\n", input_token, key, value);
                    } else {
                        perror("Invalid command");
                        exit(1);
                    }
                    break;

                default:
                    perror("Invalid input");
                    exit(1);
            }

            input = strtok(NULL, " \n");
        }
    }

    return NULL;
}

int main() {
    int server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket < 0) {
        perror("socket failed");
        exit(1);
    }

    struct sockaddr_in server_addr;
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(8080);
    server_addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(server_socket, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("bind failed");
        exit(1);
    }

    if (listen(server_socket, 5) < 0) {
        perror("listen failed");
        exit(1);
    }

    pthread_t accept_thread;
    pthread_create(&accept_thread, NULL, accept_client, &server_socket);

    char* client_input;
    int client_socket = accept(server_socket, (struct sockaddr*)NULL, NULL);
    if (client_socket < 0) {
        perror("accept failed");
        exit(1);
    }

    while (1) {
        sleep(1);

        char buffer[1024];
        ssize_t bytes_received = recv(client_socket, buffer, sizeof(buffer), 0);
        if (bytes_received <= 0) {
            close(client_socket);
            break;
        }

        client_input = buffer;
        parse_input(client_input);
    }

    close(client_socket);
    pthread_join(accept_thread, NULL);

    return 0;
}
```

To compile and run this code, save it to a file named `multi_threaded_tcp_server.c`, then use the following commands:

```sh
gcc -o multi_threaded_tcp_server multi_threaded_tcp_server.c
./multi_threaded_tcp_server
```

This implementation creates a simple binary tree to store the input values. The accept() function creates a new thread for each client connection, which handles the incoming data and forwards it to the main thread. The main thread parses the input string and handles SET and GET commands.

Note that this code is not production-ready and should be improved with proper error handling, security checks, and a more efficient data structure for the binary tree.

</details>

#### Word games / trivia

```
USER: This anagram of "silent" is what you do when paying attention and hearing someone.
ASSISTANT: listen
```

```
USER: Give me a list of 7 words that start with EN
ASSISTANT: 1. Endlessly
2. Enthusiastically
3. Enormously
4. Enveloping
5. Enduring
6. Enlightening
7. Encouraging
```

#### Multiple choice

```
USER: Which of the following astronomical objects is composed primarily of ice and rock, and is located in the Kuiper Belt?

A) Mercury
B) Venus
C) Pluto
D) Jupiter
ASSISTANT: [C, Pluto]
```

#### Writing

<details>
  <summary>Write a resignation letter in the style of a pirate captain, in which you resign from your position as janitor.</summary>

  Response:
```
ASSISTANT: Captain Jack Sparrow here, as ye be knowin', has been forced to abandon me post as Janitor o' th' Festering Cesspool, which be a filthy hole o' water that we be callin' home.

Ye may be thinkin' what could ha' driven me to leave me duties an' take me leave o' this sorry establishment? Well, ye'd be right in thinkin' so, for it be th' greed o' them what runs th' place that be drivin' me away. They've been fattenin' their pockets on me back while I've been slavin' me guts out cleanin' up their messes.

No more, me hearties! Me time o' servin' th' rich an' powerful be done, an' I'm takin' me leave o' this stinkin' hole forever! Me destiny lies elsewhere, an' it be time I pursued it. Ye may think ye've seen th' last o' me, but ye'd be wrong, for th' winds o' change be blowin', an' me ship be ready to set sail on th' high seas o' justice.

So, farewell ye scurvy dogs, ye who've made me life a living hell. I leave ye with me favorite saying: "ARRRGGGHHH, ye scurvy dogs!" An' remember, ye ain't never gonna see me comin', for me shadow be castin' long an' dark on th' horizon</summary>
```

</details>
