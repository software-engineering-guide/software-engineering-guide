# 6.3 IA generativa e applicazioni LLM

## Panoramica e motivazioni

L'[IA generativa](https://en.wikipedia.org/wiki/Generative_artificial_intelligence), e in particolare i [grandi modelli linguistici](https://en.wikipedia.org/wiki/Large_language_model) (LLM), può produrre testo fluente, codice, riassunti e dati strutturati da istruzioni in linguaggio naturale. Questo ne fa potenti blocchi costruttivi per assistenti, ricerca, elaborazione di documenti e automazione. Ma questi punti di forza vengono con un profilo di rischio distintivo. Gli LLM sono probabilistici. Possono produrre falsità sicure di sé ([allucinazioni](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))). Sono sensibili a come li solleciti. E aprono nuove superfici d'attacco come la [prompt injection](https://en.wikipedia.org/wiki/Prompt_injection) (istruzioni malevole infilate di nascosto negli input per dirottare il comportamento del modello). Quindi costruire applicazioni LLM affidabili riguarda meno il modello e più l'ingegneria attorno ad esso: come fornisci il contesto, ancori le risposte a conoscenza fidata, vincoli gli output e valuti la qualità.

Per i grandi team, le applicazioni LLM richiedono nuovi schemi diversi sia dal software tradizionale sia dall'apprendimento automatico classico. Spesso non c'è una fase di addestramento. Il comportamento è invece plasmato da prompt, contesto recuperato, definizioni degli strumenti e guardrail (controlli a runtime che vincolano input e output del modello). Questo sposta lo sforzo ingegneristico verso la gestione del contesto, la qualità del recupero, l'orchestrazione e la valutazione. Le imprese che adottano gli LLM su larga scala hanno bisogno di schemi condivisi così che ogni team non riscopra a fatica gli stessi modi di fallire.

Le organizzazioni governative e regolamentate affrontano richieste aggiuntive. Un LLM che inventa una citazione di norma o fa trapelare dati sensibili non è solo un bug; può essere un incidente legale o di sicurezza. Questi contesti richiedono ancoraggio a fonti autorevoli, rigorosa convalida degli output, supervisione umana per gli output rilevanti e chiare registrazioni di ciò che al sistema è stato chiesto e di ciò che ha prodotto. Le tecniche di questo capitolo (generazione aumentata dal recupero, guardrail e valutazione rigorosa) sono ciò che rende gli LLM abbastanza sicuri da essere distribuiti in contesti ad alta posta. I modelli Claude di Anthropic sono un'opzione di punta tra diversi fornitori capaci; le pratiche qui si applicano a prescindere dal modello che scegli.

## Principi chiave

- Ancora il modello a conoscenza fidata anziché affidarti a ciò che ha memorizzato.
- Tratta prompt e contesto come artefatti progettati e versionati, non stringhe usa e getta.
- Presumi che il modello possa sbagliare o essere manipolato; convalida gli output e vincola le azioni.
- Dai al modello solo il contesto e gli strumenti di cui ha bisogno, non di più, per ridurre errore e superficie d'attacco.
- Valuta di continuo con insiemi di test offline, metriche online e giudizio umano.
- Tieni gli umani nel ciclo per gli output rilevanti.
- Progetta pensando al modello come a un componente non fidato dentro un sistema fidato.

## Raccomandazioni

### Progetta i prompt e gestisci il contesto deliberatamente

Tratta i prompt come codice: conservali nel controllo di versione, rivedi le modifiche e testali contro una suite di esempi. Struttura chiaramente ogni prompt: ruolo e compito, vincoli, requisiti di formato ed esempi dove aiutano. Tratta la finestra di contesto (l'intervallo fisso di testo che il modello può considerare in una volta) come una risorsa scarsa. Includi le informazioni più rilevanti, ordinale con criterio e togli il rumore, perché il contesto irrilevante o eccessivo degrada la qualità e alza il costo. Per le applicazioni a più turni, gestisci esplicitamente lo stato della conversazione, riassumendo o troncando la storia per restare entro i limiti mantenendo ciò che conta. Preferisci istruzioni chiare ed esempi few-shot (una manciata di dimostrazioni elaborate incluse nel prompt) a trucchi elaborati che si rompono nel momento in cui un modello cambia.

### Ancora le risposte con la generazione aumentata dal recupero (RAG)

Per i compiti ad alta intensità di conoscenza, recupera documenti rilevanti da un corpus fidato e forniscili al modello come contesto, dicendogli di rispondere solo da quel materiale e di citare le sue fonti. La RAG mantiene aggiornata la conoscenza senza riaddestrare, confina le risposte ai contenuti approvati e abilita citazione e verifica. Investi nella qualità del recupero: suddividi i documenti in modo sensato, scegli [embedding](https://en.wikipedia.org/wiki/Word_embedding) (rappresentazioni vettoriali numeriche che collocano significati simili vicini) adatti al tuo dominio e controlla se i passaggi recuperati contengono davvero la risposta, perché una risposta fluente costruita sul passaggio sbagliato è peggio di nessuna risposta. E quando non emerge nulla di rilevante, fai in modo che il sistema lo dica anziché inventare contenuto.

### Costruisci agenti e uso degli strumenti con moderazione

Gli LLM possono chiamare strumenti (ricerca, database, calcolatrici, API interne) e possono essere composti in agenti che pianificano e agiscono su più passi. Questo aggiunge capacità reale, ma moltiplica anche il rischio: ogni strumento è un altro modo in cui un modello sbagliato o manipolato può causare danno. Definisci gli strumenti con schemi precisi, convalida ogni argomento, applica il minimo privilegio e richiedi conferma o approvazione umana per le azioni rilevanti come inviare comunicazioni o spostare denaro. Tieni i cicli degli agenti limitati, osservabili e interrompibili. Parti da strumenti ben circoscritti e a scopo singolo prima di ricorrere all'autonomia aperta.

### Aggiungi guardrail e convalida gli output

Avvolgi il modello in strati di difesa. In ingresso, filtra e rileva la prompt injection, soprattutto quando contenuto non fidato (pagine web, documenti degli utenti) entra nel contesto. In uscita, convalida la struttura rispetto a uno schema, controlla le affermazioni rispetto alle fonti, filtra il contenuto non sicuro o non conforme e rifiuta o riprova quando la convalida fallisce. Per gli output strutturati, analizza e verifica anziché fidarti della formattazione del modello. Non lasciare mai che l'output grezzo del modello inneschi azioni irreversibili senza convalida. Tratta la mitigazione delle allucinazioni come una proprietà del sistema che ottieni attraverso ancoraggio, citazione, convalida e revisione umana, non qualcosa che il modello gestisce da solo.

### Valuta offline, online e con gli umani

Costruisci una suite di valutazione di input rappresentativi con output noti per essere buoni o valutati secondo una griglia e falla girare a ogni modifica di prompt o modello (valutazione offline). Misura il comportamento reale in produzione con metriche come successo del compito, tasso di escalation e feedback degli utenti (valutazione online). Per la qualità soggettiva, usa revisori umani e, con cautela, una valutazione basata su modelli. La valutazione è la rete di sicurezza che ti permette di cambiare prompt e modelli con fiducia. Senza, voli alla cieca.

## Compromessi: vantaggi e svantaggi

| Scelta | Vantaggi | Svantaggi | Ideale quando |
|---|---|---|---|
| Solo prompting | Semplice, veloce, economico da cambiare | Ancoraggio limitato, può allucinare | Compiti ampi, bassa posta |
| RAG | Aggiornata, ancorata, citabile | Il recupero è difficile da far bene | Compiti ricchi di conoscenza e fattuali |
| Agenti con strumenti | Potenti, possono agire | Superficie d'attacco più ampia, più difficili da controllare | Automazione ben circoscritta con guardrail |
| Modello più grande e più forte | Qualità e ragionamento migliori | Costo e latenza più alti | Compiti complessi o ad alta posta |
| Modello più piccolo ed economico | Veloce e poco costoso | Più debole sui compiti difficili | Alto volume, compiti semplici |

La tensione centrale è capacità contro controllo e costo. Più autonomia e modelli più grandi portano più valore, ma richiedono più guardrail, più valutazione e più denaro. L'ancoraggio via RAG migliora l'affidabilità al costo dell'ingegneria del recupero. L'equilibrio giusto dipende dalla posta: le applicazioni ad alta posta propendono per ancoraggio, convalida e supervisione umana, anche quando costa di più.

## Domande da discutere con il tuo team

1. **Quale soglia di accuratezza e ancoraggio deve superare una funzionalità LLM prima di affrontare il pubblico, e chi dà il via?** Una risposta fluente che cita la fonte sbagliata o inventa una politica è peggio di nessuna risposta e negli enti pubblici una citazione inventata è un incidente legale, non un bug. Per un grande team, una soglia esplicita impedisce a ciascun gruppo di fissarne una privata a sensazione. Porta la tua definizione di "abbastanza ancorato": se ogni affermazione debba risalire a una fonte recuperata e verificata, se il sistema debba rifiutare quando il recupero resta vuoto e che cosa copre davvero il tuo insieme di valutazione avversariale. Il segnale da osservare è se qualcuno può oggi rilasciare una modifica di prompt direttamente agli utenti senza una esecuzione di regressione. Se la posta è legale o di sicurezza, la risposta dovrebbe instradare gli output a più alto rischio attraverso un revisore umano con vera autorità prima del rilascio.

2. **Quali delle nostre funzionalità LLM sono in segreto agenti, e a ogni strumento è stato dato il minimo privilegio e un cancello umano sulle azioni irreversibili?** Qualsiasi funzionalità che lascia il modello chiamare strumenti o agire su più passi è entrata in territorio di agente e ogni strumento è un altro modo in cui un modello sbagliato o manipolato causa danno. Per le imprese che collegano gli LLM ad API interne, questa domanda fa emergere un rischio che l'etichetta di "semplice assistente" nasconde. Porta un inventario di ogni strumento che il modello può invocare, la sua convalida degli argomenti, il suo ambito di privilegio e quali azioni (inviare comunicazioni, spostare denaro, modificare registri) richiedono conferma. Discuti se i cicli degli agenti sono limitati, osservabili e interrompibili. La risposta dovrebbe stringere gli ambiti e aggiungere cancelli di approvazione umana ovunque un'azione rilevante o irreversibile sia oggi raggiungibile senza uno.

3. **Come sapremmo entro un giorno che la nostra qualità di recupero è calata, dato che una risposta sicura costruita sul passaggio sbagliato sembra a posto?** La RAG rende affidabili le risposte solo quando il recupero fa emergere davvero il passaggio che contiene la risposta e il recupero marcisce in silenzio man mano che i documenti cambiano, i blocchi invecchiano o gli embedding derivano dal tuo dominio. Poiché il modello scrive comunque in modo fluente su un cattivo contesto, gli utenti possono non lamentarsi finché la fiducia non è già persa. Porta le tue attuali misure di latenza e richiamo del recupero, come controlli se i passaggi recuperati contengono davvero la risposta e come la freschezza dell'indice tiene il passo con le modifiche ai documenti. Per i rilasci ad alta posta o pubblici, discuti la registrazione delle fonti recuperate per l'audit così da poter ricondurre una cattiva risposta al suo cattivo passaggio. Se non hai alcuna valutazione del recupero, stai ancorando sulla fede.

4. **Trattiamo prompt, contesto e insiemi di valutazione come artefatti versionati e rivisti, o come stringhe sparse tra taccuini e log di chat?** Quando i prompt si disperdono tra i team non versionati e duplicati, una correzione in un posto non raggiunge mai gli altri e nessuno può riprodurre che cosa al sistema era stato chiesto di fare il trimestre scorso. Per un grande team, un registro condiviso dei prompt e una suite di regressione che gira a ogni modifica sono ciò che permette di scambiare un modello o modificare un'istruzione senza rompere in silenzio una funzionalità due team più in là. La spinta contraria è la velocità: gli ingegneri iterano più in fretta quando incollano un prompt e rilasciano, quindi concorda dove sta la linea tra esperimenti rapidi e qualsiasi cosa tocchi gli utenti. Porta dove i tuoi prompt vivono oggi, se un insieme di valutazione filtra le modifiche e come versioni il corpus di recupero accanto al prompt. Nei contesti aziendali e governativi, aggiungi il requisito di audit: potresti dover mostrare esattamente quale prompt e quali fonti hanno prodotto un dato output mesi dopo e un prompt che non puoi ricostruire è una registrazione che non puoi difendere.

5. **Man mano che il volume cresce, come controlleremo il costo di inferenza senza degradare in silenzio la qualità, e chi possiede la decisione sulla scelta del modello?** Il TCO delle funzionalità LLM è dominato dall'inferenza per chiamata e costi che sembrano banali in un pilota si compongono in fretta alla scala di produzione, tentando i team di scendere in silenzio a un modello più debole sperando che nessuno noti lo scivolamento di qualità. Per una grande organizzazione, lasciare che ogni team scelga modelli e limiti di costo a sensazione produce sia bollette a sorpresa sia qualità incoerente. Il vero compromesso è capacità contro costo e latenza: un modello più grande ragiona meglio sui compiti difficili, uno più piccolo è più economico e veloce su quelli semplici e caching, instradamento e ambito del recupero muovono tutti il numero. Porta il costo per compito risolto, la qualità per fascia di modello sul tuo insieme di valutazione e dove il rigonfiamento di prompt o contesto gonfia la spesa in token. Nei bilanci aziendali e governativi, nomina chi approva la scelta del modello e il tetto di spesa, perché una voce di costo che nessuno possiede è una che nessuno controlla quando il traffico triplica.

6. **Quali dati sensibili possono raggiungere il modello, dove vanno quei dati e possiamo provare che sono rimasti entro i limiti?** Ogni prompt, documento recuperato e risultato di strumento può portare dati personali o riservati nel modello e, con un fornitore ospitato, fuori dal tuo perimetro e una fuga qui è un incidente legale o di sicurezza, non un ticket di difetto. Per un grande team che collega gli LLM ai sistemi interni, il rischio si nasconde nell'impianto: un corpus di recupero che include registri che un dato utente non dovrebbe mai vedere, o log che catturano gli input grezzi. La tensione è capacità contro esposizione, poiché oscuramento e ambito stretto possono smussare la funzionalità che stai cercando di costruire. Porta una mappa dei flussi di dati di che cosa entra nel contesto, le condizioni di conservazione e addestramento del fornitore e come oscuri, delimiti e registri i campi sensibili. Nei contesti regolamentati e pubblici, lega questo alle regole di residenza dei dati, ai doveri di conservazione dei registri e ai limiti contrattuali su come un fornitore può usare i tuoi dati, perché una supervisione che non sai dimostrare è una supervisione che non hai.

## Lente settoriale

**Startup.** Rilascia una funzionalità LLM ristretta che tocchi il tuo valore centrale, costruita su un modello ospitato con recupero sui tuoi contenuti e tieni i prompt in git dietro una sottile interfaccia così da poter cambiare fornitore. Esegui un piccolo file di valutazione di domande reali prima di ogni modifica, filtra il testo incollato dagli utenti per smussare la prompt injection e limita duramente la spesa mensile. Resisti ad agenti e self-hosting: un ciclo di chiamata di strumenti illimitato che non puoi supervisionare è una passività, non una dimostrazione.

**Piccola impresa.** Probabilmente non hai uno specialista di ML, quindi compra funzionalità LLM integrate negli strumenti che già usi anziché dotare di personale una costruzione. Imposta il rischio come una semplice domanda: dove una risposta sbagliata e sicura di sé ti costerebbe un cliente e chi controlla l'output prima che parta. Privilegia i fornitori che mostrano le proprie fonti, ti lasciano tenere un umano nel ciclo e rendono l'IA facile da spegnere quando si comporta male.

**Grande impresa.** Il problema è la scala tra molti team: pubblica schemi condivisi per RAG, guardrail e schemi degli strumenti, più un banco di valutazione comune e un registro dei prompt così che ogni gruppo smetta di riscoprire gli stessi modi di fallire. Metti a bilancio esplicitamente costo di inferenza e revisione umana, standardizza lo strato di interfaccia così che i modelli restino sostituibili e governa centralmente gli agenti con minimo privilegio, cicli limitati e registrazione di audit. Gestisci le funzionalità LLM come un portafoglio con metriche e criteri di chiusura, non una dispersione di piloti.

**Ente pubblico.** Trasparenza, regole sugli appalti e responsabilità plasmano ogni scelta. Ancora rigorosamente a fonti approvate con citazioni, rifiuta quando il recupero resta vuoto e vieta al modello di enunciare norme che non sa citare. Tieni un funzionario responsabile a rivedere gli output rilevanti, registra input e fonti recuperate per l'audit, esegui un insieme di valutazione avversariale prima di ogni rilascio ed esigi nel contratto la dichiarazione dei limiti del modello e delle condizioni di trattamento dei dati.

## Esempi

**Startup.** Una startup di strumenti per sviluppatori di tre persone ha aggiunto un assistente in chat sulla propria documentazione così che gli utenti smettessero di scrivere email per domande di base. Ha usato la RAG così che ogni risposta citasse una specifica pagina della documentazione, ha istruito il modello a dire "Non ne sono sicuro, ecco a chi chiedere" quando il recupero restava vuoto e ha tenuto i prompt in git. Prima di ogni modifica ha fatto girare i prompt su un piccolo file di vere domande degli utenti per cogliere le regressioni e ha filtrato il testo incollato dagli utenti per smussare la prompt injection. L'assistente ha gestito le domande comuni e ha passato in silenzio il resto alla casella condivisa dei fondatori.

**Grande impresa.** Un'azienda software ha costruito un assistente interno di assistenza sulla propria documentazione di prodotto. Ha usato la [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) così che le risposte citassero specifiche pagine della documentazione, ha detto al modello di dire "non lo so" quando il recupero falliva e ha verificato che ogni fonte citata esistesse davvero. I prompt erano sotto controllo di versione e testati contro una suite di vere domande di assistenza a ogni modifica. L'assistente ha deviato i ticket di routine e ha fatto escalation a operatori umani di tutto ciò a bassa confidenza, mentre le metriche online seguivano risoluzione e tassi di correzione.

**Ente pubblico.** Un'agenzia pubblica ha distribuito un assistente LLM per aiutare il personale a redigere risposte alle richieste dei cittadini. L'ancoraggio era rigoroso: il modello poteva comporre risposte solo da indicazioni approvate con citazioni ed era vietato enunciare politiche non presenti nelle fonti recuperate. Un funzionario responsabile rivedeva ogni bozza prima che partisse. Il filtraggio degli input proteggeva dalla prompt injection da documenti presentati dai cittadini, gli output erano registrati per l'audit e un insieme di valutazione di query avversariali e casi limite girava prima di ogni rilascio per confermare che il sistema rifiutasse di fare congetture su questioni di diritto.

## Business case: motivazioni, ROI e TCO

Le applicazioni LLM portano ROI automatizzando il lavoro ad alta intensità di linguaggio: rispondere a domande, riassumere documenti, redigere contenuti ed estrarre struttura da testo non strutturato. Il valore compare come ticket deviati, bozze più rapide, meno revisione manuale e nuove capacità self-service. Poiché spesso non c'è una fase di addestramento, il tempo al primo valore è breve, un grande richiamo.

Il TCO, però, è dominato dal costo continuo di inferenza, dall'infrastruttura di recupero, dalle pipeline di valutazione, dai sistemi di guardrail e dalla revisione umana. I costi per chiamata si sommano in fretta su larga scala e un'applicazione non monitorata può derivare verso comportamenti non sicuri o costosi. Il costo del non adottare è restare indietro su qualità del servizio e produttività del personale. Il costo dell'adottare con noncuranza è un incidente pubblico da allucinazione o una fuga di dati. Presenta il caso alla leadership abbinando un obiettivo concreto di produttività a un piano concreto di sicurezza e valutazione e mettendo a bilancio i guardrail e la supervisione umana che mantengono durevole il valore.

## Antipattern e insidie

- **Fidarsi dell'output fluente.** Scambiare testo sicuro e ben scritto per testo corretto.
- **RAG senza valutazione del recupero.** Presumere che il recupero funzioni e non controllare mai se fa emergere i passaggi giusti.
- **Cecità alla prompt injection.** Immettere contenuto non fidato nei prompt senza difese.
- **Agenti illimitati.** Lasciare che gli agenti compiano azioni rilevanti senza limiti né approvazione umana.
- **Nessun banco di valutazione.** Cambiare prompt e modelli a sensazione, senza test di regressione.
- **Dispersione dei prompt.** Prompt sparsi, non versionati e duplicati tra i team.
- **Sovra-automazione.** Togliere gli umani da decisioni che portano peso legale o di sicurezza.

## Modello di maturità

1. **Avvio.** Prompting ad hoc in progetti isolati; nessun ancoraggio, guardrail o valutazione; i prompt vivono dove qualcuno li ha incollati e le allucinazioni sono scoperte in produzione.
2. **Sviluppo.** Alcuni team aggiungono RAG e versionamento dei prompt, convalida di base degli output e un piccolo insieme di valutazione manuale, ma le pratiche variano da team a team e poggiano su singoli promotori anziché su un'attesa condivisa.
3. **Standardizzazione.** Schemi documentati per RAG, guardrail, schemi degli strumenti e versionamento dei prompt sono fatti rispettare nell'organizzazione; la valutazione offline automatica gira a ogni modifica di prompt o modello; i flussi ad alta posta portano metriche online e revisione umana.
4. **Gestione.** Il portafoglio è misurato rispetto a valori di riferimento: richiamo del recupero, tassi di allucinazione e rifiuto, copertura della difesa dalla injection, costo e latenza per chiamata e tassi di escalation e correzione sono seguiti su cruscotti; cancelli di rilascio e criteri di chiusura scattano sull'evidenza anziché sull'opinione e una esecuzione di regressione blocca qualsiasi modifica che muova una metrica nella direzione sbagliata.
5. **Orchestrazione.** La valutazione continua offline e online è legata agli esiti di business; difese dalla injection, agenti e ancoraggio sono governati e osservabili; l'organizzazione ritira, riaggiusta e ridefinisce di routine le funzionalità LLM e cambia modello man mano che qualità, costo e rischio si spostano.

## Spunti di discussione

- Come decidete quali output richiedono revisione umana prima dell'uso?
- Qual è il vostro standard di "abbastanza ancorato" prima che una risposta possa essere mostrata agli utenti?
- Come vi difendete dalla prompt injection quando contenuto non fidato deve entrare nel contesto?
- Quando un agente vale il suo rischio aggiuntivo rispetto a un progetto più semplice a chiamata singola?
- Come valutate la qualità soggettiva su larga scala senza affidarvi troppo alla valutazione basata su modelli?
- Come mantenete manutenibili e coerenti i prompt tra molti team?

## Punti chiave

- L'affidabilità viene dall'ingegneria attorno al modello: contesto, ancoraggio, guardrail e valutazione.
- La RAG ancora le risposte a fonti fidate e abilita citazione e verifica.
- Tratta il modello come un componente non fidato; convalida gli output e vincola l'uso degli strumenti.
- Dai agli agenti minimo privilegio, cicli limitati e approvazione umana per le azioni rilevanti.
- Valuta offline, online e con gli umani in modo continuo; è ciò che rende sicuro il cambiamento.

## Riferimenti e letture di approfondimento

- Patrick Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*.
- Jason Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Anthropic, *Building Effective Agents* (indicazioni ingegneristiche).
- Louis-François Bouchard e Louie Peters, *Building LLMs for Production*.
