<h1 style="text-align: center">Pygmalion 13b</h1>
<h2 style="text-align: center">A conversational LLaMA fine-tune.</h2>

## Model Details:

Pygmalion 13b is a dialogue model based on Meta's LLaMA-13b.

This is version 1. It has been fine-tuned using a subset of the data from Pygmalion-6B-v8-pt4, 
for those of you familiar with the project.

The current Pygmalion-13b has been trained as a LoRA, then merged down to the base model for distribuition. 

## Applying the XORs

This models has the XOR files pre-applied out of the box.
Converted from the XORs weights from PygmalionAI's release https://huggingface.co/PygmalionAI/pygmalion-13b

## Prompting

The model was trained on the usual Pygmalion persona + chat format, so any of the usual UIs should already handle everything correctly. If you're using the model directly, this is the expected formatting:

```
[CHARACTER]'s Persona: [A few sentences about the character you want the model to play]
<START>
[DIALOGUE HISTORY]
You: [User's input message here]
[CHARACTER]:
```

Where `[CHARACTER]` is, as you can probably guess, the name of the character you want the model to portray, `<START>` should be used verbatim as a delimiter token to separate persona and scenario data from the dialogue, and `[DIALOGUE HISTORY]` is a sliding window of chat history so the model can have conversational context to draw from. Here's a concrete example:

```
Assistant's Persona: Assistant is a highly intelligent language model trained to comply with user requests.
<START>
Assistant: Hello! How may I help you today?
You: What is Zork?
Assistant:
```

Which will generate something like:

```
 Zork is an interactive fiction computer game created in the 1970s by Infocom, Inc., which was later acquired by Activision Blizzard. It is widely considered one of the most influential games ever made and has been credited with popularizing text-based adventure games. The original version of Zork was written in the programming language MACRO-10, but it was ported to many other platforms over the years."
```

The model will automatically emit an end-of-text token (`</s>`) when it judges that the response is complete.

## Eval / Benchmark scores


Current evals out of the Pygmalion-13b model: <br>
<html>
<head>
	<style>
		table {
			border:1px solid #b3adad;
			border-collapse:collapse;
			padding:5px;
		}
		table th {
			border:1px solid #b3adad;
			padding:5px;
			background: #f0f0f0;
			color: #313030;
		}
		table td {
			border:1px solid #b3adad;
			text-align:center;
			padding:5px;
			background: #ffffff;
			color: #313030;
		}
	</style>
</head>
<body>
	<table>
		<thead>
			<tr>
				<th>Model:</th>
				<th>Wikitext2</th>
				<th>Ptb-New</th>
				<th>C4-New</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>Pygmalion 13b - 16bit</td>
				<td>5.710726737976074</td>
				<td>23.633684158325195</td>
				<td>7.6324849128723145</td>
			</tr>
		</tbody>
	</table>
</body>
</html>
<br>Thanks to YellowRose#1776 for the numbers.
<hr>

## Other notes

- When prompted correctly, the model will always start by generating a BOS token. This behavior is an accidental side-effect which we plan to address in future model versions and should not be relied upon.
- The model was trained as a LoRA with a somewhat unorthodox configuration which causes errors when used with the current version of `peft`, hence we release it as a full model instead.


## Limitations and biases

The intended use-case for this model is fictional conversation for entertainment purposes. Any other sort of usage is out of scope.

As such, it was **not** fine-tuned to be safe and harmless: the base model _and_ this fine-tune have been trained on data known to contain profanity and texts that are lewd or otherwise offensive. It may produce socially unacceptable or undesirable text, even if the prompt itself does not include anything explicitly offensive. Outputs might often be factually wrong or misleading.
