
# 🐈‍⬛ Mistral-7B-v0.1-flashback-v2

![](https://huggingface.co/timpal0l/Mistral-7B-v0.1-flashback-v2/resolve/main/flashcat.png?download=true)


Mistral-7B-v0.1-flashback-v2 is a continuation of the pretraining process for the base Mistral-7B-v0.1 model, utilizing 2 251 233 forum threads from the Swedish website https://www.flashback.org/. Which is rougly 40GB of text.
It is a full finetune for one epoch.

* GGUF Version available [**Here**](https://huggingface.co/timpal0l/Mistral-7B-v0.1-flashback-v2-GGUF)
* Instruct version [**Here**](https://huggingface.co/timpal0l/Mistral-7B-v0.1-flashback-v2-instruct)

## How to use:
```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "timpal0l/Mistral-7B-v0.1-flashback-v2"
device = "cuda:0" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
model.eval()
model.to(device)

prompt = "Idag är det den bästa"
input_ids = tokenizer(prompt, return_tensors="pt")["input_ids"].to(device)

generated_token_ids = model.generate(
    inputs=input_ids,
    max_new_tokens=256,
    do_sample=True,
    temperature=0.8,
    top_p=1,
)[0]

generated_text = tokenizer.decode(generated_token_ids)
generated_text
```
```
<s> Idag är det den bästa dagen i hela veckan, för nu tar det slut!\n\n>! Gnällfesten!\n\nJag sitter här, oerhört förvirrad, och försöker förstå varför vi ens måste fortsätta att existera efter döden. Jag menar, jag förstår ju egentligen att det aldrig kan ta slut, eller inte "ta slut" i den bemärkelsen att materian försvinner, men det är inte det jag pratar om.\n\nDöden, det faktum att man dör och aldrig kan uppleva livet igen. Det som är liv och ger livet en mening, det försvinner i döden. Och sen börjas det om, om och om igen. Varför behöver vi så många liv? Vi är ju inte ens medvetna av att vi någonsin har levt, så varför ska vi komma hit och bli medvetna hela tiden?\n\nDet här är en sådan fråga som jag aldrig kan få
```
## Data Format:
To mimic the data format used in pre-training it has the following structure:
```html
# Thread_Title

username_thread_creator:
Hello, this is my thread...

username_user_1:
This is a response to the thread, without qouting anything.

username_user_2:
> username_user_1: This is a response to the thread, without qouting anything.
I am now quoting username_user_1...
```
### Random training sample:
```html
# Tips om aktiviter och sevärdheter i Stockholm för någon med funktionsnedsättning

Roozbeh:
Hej!

Jag jobbar som assistent åt en kille på ett stödboende.
Nästa vecka åker han, jag och en kollega till Stockholm och han är superpeppad på att se sig omkring.
Har ni några guld tips?
Får gärna ge förslag både dag och kvällstid om ni kommer på något.
Vi har redan tänkt på att se slottet.
Och gamla staden, finns där något kanske?
Bra cafen/restauranger som inte är allt för dyra.
Några ställen som man bara måste se eller göra i Stockholm?
Han är inte rullstolsbunden ska nämnas, är ung och i ganska bra kondition fysiskt.
Alla tips är välkomna tack!

Annéa:
Beror lite på vad man gillar. Om ni ändå är vi Slottet så har ni ju dom stora turistgatorna i Gamla Stan runt hörnet precis, dock inget ställe man vill gå på om man tycker det är jobbigt med folk och att trängas och ingenstans där man äter särskilt bra eller billigt.

Laust:
Åka upp på globen funkar med rullstol

Thomaz:
Välkomna! 🙂
Vad har han för intressen?
Är ni ändå på slottet kan jag rekommendera livrustkammaren, där kläder och attiraljer såsom vagnar (och även uppstoppade hästar) från svenska kungligheter är utställda.

Anne-Jorunn:
Gröna Lund och skansen är guld, om hen klarar av att åka karusell så går ni också förbi alla köer om du är stödperson.
Abba museumet, Vasamuseumet, militärhistoriska museet, tekniska museet, Junibacken. Finns mycket bra.
Annars kan det vara skoj att gå runt på Mall of Scandinavia, skönt att vara inne med toaletter inom räckhåll.

Muscab:
> Roozbeh: Hej!
>
> Jag jobbar som assistent åt en kille på ett stödboende.
> Nästa vecka åker han, jag och en kollega till Stockholm och han är superpeppad på att se sig omkring.
> Har ni några guld tips?
> Får gärna ge förslag både dag och kvällstid om ni kommer på något.
> Vi har redan tänkt på att se slottet.
> Och gamla staden, finns där något kanske?
> Bra cafen/restauranger som inte är allt för dyra.
> Några ställen som man bara måste se eller göra i Stockholm?
> Han är inte rullstolsbunden ska nämnas, är ung och i ganska bra kondition fysiskt.
> Alla tips är välkomna tack!

Jag tror de mesta platser är ganska ovänliga för rullstol. Backar, grusvägar, kullersten, trånga dörrar, trappor. Finns det någon restaurang/café som är billig och rullstolsvänlig? Vet inte. Köp ett paket glassar på ica istället.

Något man måste göra i Stockholm? Det finns inte mycket att se. Turister brukade gå runt i gamla stan och titta på tunnelbanestationer.

Annéa:
> Muscab: Jag tror de mesta platser är ganska ovänliga för rullstol. Backar, grusvägar, kullersten, trånga dörrar, trappor. Finns det någon restaurang/café som är billig och rullstolsvänlig? Vet inte. Köp ett paket glassar på ica istället.
>
> Något man måste göra i Stockholm? Det finns inte mycket att se. Turister brukade gå runt i gamla stan och titta på tunnelbanestationer.

Han sitter ju INTE i rullstol...

Tharsika:
Vad har han för problematik? Vad kan störa/vara svårt för honom ? Rullstol ? Kramp? Utåtagerande ?

Muscab:
> Annéa: Han sitter ju INTE i rullstol...

Läste fel. 🤦

Boine:
Armémuseum
Historiska museet
Åka djurgårdsfärjan alt. ”Skärgårdstur” med SL
Utsikt på Södermalm + promenaden dit. Mariaberget & Monteliusvägen
Gamla stan - Mårten Trotzig gränd samt kanonkulorna i husväggen några meter från Stortorget
Målningar i tunnelbanan
Spela äventyrsgolf inomhus
Se guldbron - Slussen
Utsikt Katarinahissen - Slussen, man går in i porten till Gondolen (nog nerlagd) tar hissen längst upp och går en våning upp annars får man gå dit bakvägen onödigt långt.
Gå hela Drottninggatan
Slottet ev tajma in vaktavlösning

Kolla om det finns något personen har intresse av/om, finns en hel gratis museum

Roozbeh:
Vilka bra tips! Tack allihopa vad fint av er att bidra! Så uppskattat verkligen 🙂
Nu är vi åter hemma igen efter resan till Stockholm.
Resan gick jättebra, vi planerade noga och gjorde det mesta av tid med hänsyn till funktionsnedsättningen. Vi gick såklart efter vad han själv önskade göra och gav förslag på vad Stockholm erbjuder. Då vi bara var i Stockholm under ca 24 timmar måste jag säga att vi fick gjort mycket mer än vi väntade oss. Vi hade ingen bil. Istället köpte vi ett 24 tim kort för kollektivtrafiken och med hjälp av SL appen och google maps navigerade jag runt oss i staden.

Hotellet vi bodde på låg nära Centralstationen.

Detta gjorde vi:

Gick runt hela Gamla Stan. Åt på restaurang där samt i Vasaplan och även fikade på diverse caféer i Gamla Stan. Vi såg det Kungliga slottet både inuti och utanpå, var uppskattat! Han tyckte det var så häftigt. Strosade runt i alla gränder, torg och gator i Gamla Stan, gick in i trevliga små butiker och tog fina foton! Vi tittade på alla båtar i hamnen. Parlamentet. Stadshuset. Vi gick in på diverse olika ställen vi gick förbi som han impulsivt kände dragning till. Typ karaokebar, kulturhuset, pubbar etc. Allt han kände för gjorde vi. Det var hans resa 100 %.

Åkte med färja till Djurgården och besökte ABBA museet där han fick lyssna på sånger, se rekvisita, sjunga och t.om åka helikopter i VR.
Vi shoppade också såklart då Stockholm har så många butiker!(Hela Drottninggatan och ställen på/nära Vasaplan)
Under resan interagerade han med en massa Stockholmare. Sade till flertalet tjejer att han älskade dom haha vilket charmör! Vi gick förbi en högvakt vid slottet som han hälsade på. Det var en hon, och vakten rörde inte en min men följde honom med blicken. Givetvis fick vi säga det att dom inte pratar med någon då det ingår i jobbet etc.

Han blev bemött med respekt och ömhet av de flesta ska sägas. Han var glad över att ha fått prata med så många människor. Vi stannade ofta då han ville fråga t.ex poliser eller andra arbetare om saker, alla var gulliga och vänliga mot honom.
Vi åkte under resan buss, tunnelbana(också en önskan att få göra) och färjor till olika färjterminaler för att få se Stockholm från vattnet.

Såg också Sergels Torg på kvällen eller "Plattan" som jag tror den också kallas. En pelare var vackert upplyst i blått ljus där och han berättade exalterat om hur många filmer han sett som har plattan som scenplats etc. Kvällen bjöd på solnedgången från hotellets tak. Åt en fantastisk frukostbuffé på morgonen med flera omgångar god mat! Härligt att han njöt.

Då han faktiskt har en fysisk och kognitiv nedsättning är vi så glada att han orkade så mycket! Bäst av allt sa han sig vara väldigt nöjd med resan. Vi ska nu planera fler resor till Stockholm i framtiden. Då gör vi fler saker, sånt vi inte hann med den här gången. Var lite begränsat med tid(24 timmar) samt behövde vi tänka på att energi skulle räcka till utan att kroppen skulle triggas till att hans nedsättnings symptom blossade upp. Behövs ju givetvis pauser med jämna mellanrum då.
Tack och lov för apparna som jag kunde leda oss efter. Att åka kollektivt hade varit svårt annars och jag kunde se efter kartan var våra besöksmål låg samt vilka vägar som kunde spara oss onödig tid.

Tack ska ni ha för tipsen, igen. Tack till Stockholm för att ni tog emot oss med respekt han var så nöjd med resan.
Hej så länge, vi kommer åter i framtiden! 😁
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_timpal0l__Mistral-7B-v0.1-flashback-v2)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |57.53|
|AI2 Reasoning Challenge (25-Shot)|57.17|
|HellaSwag (10-Shot)              |80.74|
|MMLU (5-Shot)                    |59.98|
|TruthfulQA (0-shot)              |40.66|
|Winogrande (5-shot)              |77.19|
|GSM8k (5-shot)                   |29.42|

