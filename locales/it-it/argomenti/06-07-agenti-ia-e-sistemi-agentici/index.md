# 6.7 Agenti IA e sistemi agentici

## Panoramica e motivazioni

Un **agente IA** è un [grande modello linguistico](https://en.wikipedia.org/wiki/Large_language_model) (LLM) avvolto in un ciclo: gli viene dato un obiettivo, può chiamare strumenti, tiene una certa memoria di ciò che ha fatto e decide da solo il passo successivo finché l'obiettivo è raggiunto o rinuncia. Quel ciclo è l'intera differenza tra un agente e le semplici chiamate di prompt e risposta del capitolo 6.3. Una singola chiamata risponde a una domanda. Un agente legge la sua email, cerca in un database, apre un ticket, controlla il risultato e riprova. Il modello non produce più solo testo; sceglie azioni nei tuoi sistemi.

Quel cambiamento muta il problema ingegneristico. Quando un modello scrive solo parole, un cattivo output è una cattiva frase. Quando un modello guida strumenti, un cattivo output può inviare un messaggio sbagliato, cancellare un record o spostare denaro. Quindi un [agente intelligente](https://en.wikipedia.org/wiki/Intelligent_agent) si capisce meglio come un pianificatore non fidato dentro un sistema fidato e la maggior parte del tuo lavoro va nel limitare ciò che quel pianificatore può fare. Questo capitolo si basa direttamente sulle fondamenta degli LLM del capitolo 6.3, sulle questioni di fiducia e responsabilità del capitolo 6.5 e sulle pratiche di piattaforma del capitolo 6.6.

Per i grandi team la posta è organizzativa quanto tecnica. Le imprese vogliono agenti collegati a veri sistemi interni (ticketing, finanza, anagrafiche dei clienti), il che significa che gli agenti ereditano veri controlli di accesso e veri obblighi di gestione delle modifiche. Gli enti pubblici aggiungono la responsabilità pubblica: un'azione autonoma che colpisce un cittadino deve essere spiegabile, supervisionabile e verificabile a posteriori. Lo schema è potente. Distribuito senza disciplina, è un modo rapido di automatizzare gli errori.

## Principi chiave

- Un agente è un modello più un ciclo, strumenti, memoria e un obiettivo. Il rischio vive nel ciclo, non nella prosa.
- Limita l'autonomia al compito. Dai la minima libertà che porta a termine il lavoro.
- Preferisci un flusso fisso quando i passi sono noti. Ricorri all'autonomia aperta solo quando non lo sono.
- Tratta ogni strumento come superficie d'attacco e concedigli il minimo privilegio con cui può lavorare.
- Metti un umano nel ciclo per le azioni rilevanti o irreversibili e rendi economico il ripristino.
- Valuta sul successo del compito, non su come si legge la trascrizione.
- Traccia ogni esecuzione. Un'azione che non puoi ricostruire è un'azione che non puoi governare.
- Il progetto più semplice che funziona è di solito quello giusto. Spesso non è affatto un agente.

## Raccomandazioni

### Parti con un flusso, aggiungi autonomia solo dove devi

L'errore più comune è ricorrere a un agente autonomo quando una pipeline fissa basterebbe. Se già conosci i passi (estrarre i campi, convalidarli, cercare un record, redigere una risposta), scrivilo come un flusso orchestrato con il modello che riempie specifici spazi. L'autonomia si guadagna il posto quando il percorso non può davvero essere predeterminato, per esempio la ricerca aperta o il triage su molti possibili strumenti. Limita l'autonomia al compito: fissa un tetto al numero di passi, restringi l'insieme di strumenti a ciò di cui questo obiettivo ha bisogno e fissa una chiara condizione di arresto. Una buona regola è dare al modello esattamente tanta libertà quanta ne richiede il problema e non un grado di più.

### Fai dell'uso degli strumenti la capacità centrale e rendilo sicuro

L'uso degli strumenti (detto anche chiamata di funzioni) è ciò che trasforma un modello in un agente. Definisci ogni strumento con uno schema preciso, convalida ogni argomento che il modello fornisce e applica il [principio del minimo privilegio](https://en.wikipedia.org/wiki/Principle_of_least_privilege): un agente di reportistica di sola lettura ottiene credenziali di sola lettura, mai un accesso in scrittura che potrebbe usare male. Esegui gli strumenti dentro una [sandbox](https://en.wikipedia.org/wiki/Sandbox_(computer_security)) così che una cattiva chiamata non possa andare oltre il suo raggio d'impatto. Preferisci molti strumenti ristretti e a scopo singolo a pochi ampi, perché uno strumento ristretto è più facile da ragionare, autorizzare e verificare. È la stessa moderazione che il capitolo 6.3 sollecita per l'uso di strumenti degli LLM, resa centrale.

### Usa schemi espliciti di ragionamento e pianificazione

Gli agenti funzionano meglio quando il loro pensiero è strutturato. In uno schema di ragionare e agire (reso popolare dalla ricerca ReAct), il modello alterna ragionamento sulla situazione e azione, poi osserva il risultato prima di ragionare di nuovo. Per obiettivi più difficili, fai pianificare prima il modello (scomporre in sotto-compiti) e poi eseguire, così da poter ispezionare e persino approvare il piano prima che qualsiasi strumento giri. Tieni questi cicli osservabili e interrompibili. Un piano che puoi leggere è un piano che puoi fermare.

### Tieni gli umani nel ciclo per le azioni rilevanti

Decidi, per strumento e per azione, se il modello può agire da solo o deve chiedere prima. Le azioni reversibili e a bassa posta (cercare, redigere) possono girare senza sorveglianza. Quelle rilevanti o irreversibili (inviare comunicazioni esterne, spostare denaro, modificare dati di produzione, decidere il caso di un cittadino) hanno bisogno di un cancello con [umano nel ciclo](https://en.wikipedia.org/wiki/Human-in-the-loop) con reale autorità di dire no. Progetta per la reversibilità dove puoi: preferisci predisporre una modifica anziché confermarla e fai dell'annullamento una funzionalità di prim'ordine così che un'azione sbagliata costi minuti, non un incidente.

### Tratta il modello di sicurezza come avversariale

Gli agenti allargano la superficie d'attacco descritta nel capitolo 4.2. La minaccia principale è la [prompt injection](https://en.wikipedia.org/wiki/Prompt_injection): istruzioni malevole nascoste in una pagina web, un documento o un'email che l'agente legge e obbedisce. Strettamente correlato è il [problema del confused deputy](https://en.wikipedia.org/wiki/Confused_deputy_problem), in cui un attaccante inganna un agente privilegiato a usare male il proprio accesso legittimo, per esempio esfiltrando dati attraverso uno strumento che l'agente può chiamare. Presumi che qualsiasi contenuto l'agente assorba possa essere ostile. Separa le istruzioni fidate dai dati non fidati, vincola gli strumenti così che un agente dirottato non possa raggiungere sistemi sensibili e non lasciare mai che l'output grezzo del modello inneschi un'azione irreversibile senza convalida.

### Valuta sul successo del compito e testa in regressione il non determinismo

Giudica gli agenti da se portano a termine il compito, non da se la trascrizione suona intelligente. Costruisci un insieme di valutazione di obiettivi rappresentativi con criteri di successo verificabili (il ticket ha ottenuto la priorità giusta, il rimborso ha corrisposto alla politica) e fallo girare a ogni modifica di prompt, modello o strumento. Poiché gli agenti sono non deterministici, un singolo passaggio prova poco: esegui ogni caso più volte e segui un tasso di successo, non un superato o fallito. Questo estende la disciplina di valutazione offline e online dei capitoli 6.3 e 6.2 (ingegneria dell'apprendimento automatico e MLOps) a sistemi il cui output è una sequenza di azioni.

### Strumenta le esecuzioni per osservabilità, costo e gestione dei fallimenti

Non puoi governare ciò che non vedi. Traccia ogni esecuzione dell'agente da capo a capo (capitolo 6.6): l'obiettivo, ogni passo di ragionamento, ogni chiamata di strumento con i suoi argomenti e risultato, i token spesi e l'esito finale. Questo tracciamento è insieme il tuo debugger, la tua traccia di audit e il tuo contatore dei costi. Fissa budget rigidi su passi, tempo e spesa, perché un agente che gira in tondo può bruciare latenza e denaro in fretta. Gestisci esplicitamente il fallimento: ritenta gli errori transitori degli strumenti con backoff, ma rileva i cicli in cui il modello ripete un'azione fallita e fallisci in sicurezza anziché dibattersi.

## Compromessi: vantaggi e svantaggi

| Scelta | Vantaggi | Svantaggi | Ideale quando |
|---|---|---|---|
| Flusso fisso (il modello riempie spazi) | Prevedibile, economico, facile da testare e verificare | Rigido; si rompe sui percorsi imprevisti | I passi sono noti in anticipo |
| Singolo agente autonomo | Flessibile; gestisce obiettivi aperti | Più difficile da controllare, valutare e limitare | Il percorso non può essere predeterminato |
| Orchestrazione multi-agente | Parallelismo; ruoli specializzati | Costo di coordinamento, errori che si compongono, spesa più alta | Un compito si scompone davvero in parti indipendenti |
| Azione senza sorveglianza | Veloce, basso attrito | Gli errori si eseguono senza controllo | Le azioni sono reversibili e a bassa posta |
| Cancello con umano nel ciclo | Sicurezza, responsabilità, reversibilità | Più lento; richiede capacità di revisori | Le azioni sono rilevanti o irreversibili |

La tensione centrale è autonomia contro controllo. Più autonomia gestisce più situazioni ma richiede più guardrail, più valutazione e più denaro e fallisce in modi più difficili da prevedere. I progetti multi-agente tentano i team con l'eleganza, eppure ogni agente aggiuntivo aggiunge onere di coordinamento e un altro posto in cui un piccolo errore si compone in un risultato sbagliato. Risolvi la tensione partendo dalla minima autonomia che risolve il problema e aggiungendo libertà solo quando un compito concreto ti ci costringe, sempre abbinata a un guardrail corrispondente.

## Domande da discutere con il tuo team

1. **Questa funzionalità ha davvero bisogno di un agente, o un flusso fisso sarebbe più sicuro ed economico?** L'autonomia è seducente, ma la maggior parte dei lavori ha passi conoscibili che una pipeline orchestrata gestisce con molto meno rischio. Per un grande team, adottare per default gli agenti significa che ogni gruppo si accolla oneri di valutazione, tracciamento e sicurezza che un progetto più semplice eviterebbe. Porta il compito specifico e chiediti se i suoi passi possono essere predeterminati; se sì, un agente è probabilmente sovra-ingegnerizzazione. Riserva l'autonomia aperta agli obiettivi in cui il percorso varia davvero per caso. La risposta dovrebbe spingere la maggior parte delle funzionalità verso un flusso e lasciare un piccolo insieme deliberato come veri agenti.

2. **Per ogni strumento che il nostro agente può chiamare, qual è la cosa peggiore che un agente dirottato potrebbe farci, e che cosa lo impedisce?** Gli attacchi di prompt injection e confused deputy rivolgono contro di te l'accesso legittimo dell'agente, quindi la lente giusta è avversariale (capitolo 4.2). Fai l'inventario di ogni strumento, del suo ambito di privilegio e se un'istruzione malevola infilata attraverso contenuto assorbito potrebbe raggiungerlo. Per le imprese che collegano gli agenti ai sistemi interni, è qui che minimo privilegio, sandboxing e cancelli umani sulle azioni irreversibili diventano reali. Porta l'elenco degli strumenti e le credenziali che ciascuno detiene. Se qualsiasi azione rilevante è raggiungibile senza convalida o controllo umano, quella è la prima cosa da correggere.

3. **Come sapremmo che il tasso di successo di un agente è calato, dato che ogni esecuzione sembra plausibile?** Gli agenti sono non deterministici, quindi una trascrizione che si legge bene può comunque aver compiuto l'azione sbagliata e una singola esecuzione verde non prova nulla. Chiediti se hai un insieme di valutazione di obiettivi con esiti verificabili, eseguito molte volte per caso per produrre un tasso di successo anziché un singolo superamento. Per i rilasci ad alta posta o pubblici, discuti come le tracce delle esecuzioni ti permettono di ricostruire esattamente che cosa è successo quando qualcosa va storto (capitoli 6.5 e 6.6). Se il tuo unico segnale sono le lamentele degli utenti, sei già in ritardo. La risposta dovrebbe finanziare un banco di valutazione prima della scala, non dopo un incidente.

4. **Quali azioni di questo agente sono davvero irreversibili, chi detiene l'autorità di approvarle e abbiamo la capacità di revisori per dotare di personale quel cancello?** La tentazione è lasciar agire il modello senza sorveglianza ovunque, ma un cancello umano è reale solo se una persona nominata con l'autorità di dire no è disponibile quando l'agente chiede. Per un grande team, una coda di approvazione che nessuno possiede diventa in silenzio un timbro di gomma e la sicurezza che hai progettato evapora sotto il volume. Porta l'elenco completo delle azioni che l'agente può compiere, segna ciascuna come reversibile o irreversibile e stima il volume giornaliero di casi a bassa confidenza che atterrerebbe su un revisore. Pesa l'attrito e il costo di personale di un cancello contro il raggio d'impatto di un errore senza sorveglianza e preferisci riprogettare un'azione irreversibile in una predisposta e annullabile anziché aggiungere un altro revisore. Nei contesti aziendali e governativi, lega ogni azione rilevante a un funzionario responsabile e a una registrazione di gestione delle modifiche, perché un'azione autonoma che colpisce un cittadino o un cliente che nessun umano ha approvato è esattamente il fallimento che un audit troverà.

5. **Stiamo ricorrendo a un progetto multi-agente perché il compito si scompone davvero, o perché sembra elegante?** Dividere il lavoro tra agenti specializzati è seducente, eppure ogni agente in più aggiunge onere di coordinamento e un altro posto in cui un piccolo errore si compone in un risultato sbagliato. Per una grande organizzazione il costo non è solo spesa e latenza: un sistema multi-agente è molto più difficile da tracciare, valutare e ragionare quando fallisce, quindi l'onere di governance si moltiplica con ogni ruolo che aggiungi. Porta il compito e mostra, in concreto, quali parti girano in modo indipendente e in parallelo, poi confronta il tasso di successo e il costo misurati di una versione multi-agente contro un singolo agente sullo stesso insieme di valutazione. Se vince o pareggia il singolo agente, il progetto elegante è sovra-ingegnerizzazione. Per i rilasci regolamentati o pubblici, ricorda che ogni agente nella catena è un altro componente che un organo di controllo deve poter ispezionare, quindi una struttura aggiunta che non sai giustificare è una passività aggiunta.

6. **Quali sono i budget rigidi su passi, tempo e spesa di un agente, e come verrebbe colto un agente che gira in tondo prima che faccia salire costo o latenza?** Un agente che ripete un'azione fallita può bruciare denaro e tempo senza avviso, quindi l'autonomia illimitata è un rischio finanziario quanto di sicurezza. Per un grande team che gestisce molti agenti, un singolo ciclo che si comporta male può far schizzare una bolletta cloud o esaurire un limite di frequenza che affama ogni altro carico, il che fa dei tetti per esecuzione una questione operativa condivisa anziché di un solo team. Porta i budget attuali di passi, tempo e token per ogni agente, gli allarmi che scattano quando un'esecuzione li supera e il rilevamento dei cicli che fallisce in sicurezza anziché dibattersi. Pesa budget stretti, che possono interrompere un compito legittimamente difficile, contro budget larghi che lasciano scappare il costo. Nei contesti aziendali e governativi dove la spesa deve essere prevista e giustificata, un agente il cui costo è illimitato è una voce che non puoi difendere in una revisione di bilancio né in un audit.

## Lente settoriale

**Startup.** Rilascia un agente ristretto che tocchi il tuo valore centrale, su un modello ospitato, con il più piccolo insieme di strumenti che fa il lavoro e un tetto rigido su passi e spesa. Resisti alla dimostrazione multi-agente: la tua scarsa attenzione ingegneristica è meglio spesa a limitare l'autonomia di un singolo agente e a tracciarne le esecuzioni che a coordinare ruoli che non puoi mantenere. Tieni ogni azione rilevante dietro un unico cancello "bozza, mai invio" così che un errore costi un clic per annullare, non un incidente.

**Piccola impresa.** Non hai nessuno che gestisca un banco di valutazione o una sandbox, quindi preferisci agenti integrati in strumenti di cui già ti fidi e attiva solo l'autonomia che puoi supervisionare a occhio. Tratta qualsiasi agente che può inviare, pagare o cancellare per tuo conto come qualcosa da tenere spento finché una persona conferma ogni azione, perché un messaggio automatico sbagliato a un cliente ti costa la relazione. Privilegia i fornitori che ti mostrano che cosa l'agente ha fatto e ti permettono di spegnere l'automazione.

**Grande impresa.** Il problema è governare gli agenti tra molti team: schemi condivisi per limitare l'autonomia, credenziali degli strumenti al minimo privilegio, sandboxing, cancelli con umano nel ciclo e tracciamento da capo a capo così che nessun gruppo reinventi i guardrail. Collega gli agenti ai sistemi interni sotto gli stessi controlli di accesso che avrebbe un umano, filtra le azioni irreversibili dietro approvatori nominati e gestione delle modifiche e gestisci il portafoglio con metriche di tasso di successo, budget per esecuzione e test avversariali di injection. Standardizza lo strato di tracciamento e valutazione così che il comportamento di qualsiasi agente possa essere ricostruito e verificato.

**Ente pubblico.** Appalti, trasparenza e responsabilità pubblica limitano ogni scelta. Tieni gli agenti a raccogliere fatti e redigere e riserva ogni decisione che colpisce un cittadino a un umano responsabile, perché la responsabilità di una decisione del settore pubblico non può essere delegata a un modello. Registra ogni esecuzione così che un organo di controllo possa vedere quali fonti sono state consultate e che cosa è stato fatto, esigi che i fornitori dichiarino gli strumenti e i limiti dell'agente e prova attraverso un insieme di valutazione avversariale che l'agente rifiuta di agire oltre il proprio mandato limitato.

## Esempi

**Startup.** Una startup di analisi di cinque persone costruisce un agente di triage dell'assistenza. Legge un ticket in arrivo, cerca nella documentazione e o redige una risposta o instrada il ticket a un umano e quello è l'intero insieme di strumenti. Le credenziali sono di sola lettura più una singola azione "crea bozza" che non invia mai senza che una persona clicchi invia. Ogni esecuzione è tracciata così che i fondatori possano vedere perché un ticket è stato instradato dove è stato e un insieme di valutazione notturno di cinquanta ticket reali esegue l'agente cinque volte ciascuno per seguire un tasso di accuratezza dell'instradamento. Quando l'ingegnosa dimostrazione multi-agente di un concorrente li tenta, restano a singolo agente perché il loro compito non si scompone.

**Grande impresa.** Una banca costruisce un agente per aiutare il personale operativo a riconciliare i pagamenti falliti. Si integra con i sistemi interni sotto gli stessi controlli di accesso di un impiegato umano, concessi attraverso credenziali di servizio al minimo privilegio delimitate alla sola riconciliazione. L'agente può indagare liberamente (leggere i libri mastri, cercare nella storia delle transazioni) ma qualsiasi azione che sposta denaro o modifica un record è predisposta e richiede un approvatore umano nominato, soddisfacendo la gestione delle modifiche. I documenti assorbiti sono trattati come non fidati per smussare la prompt injection, gli strumenti girano in sandbox e ogni esecuzione è tracciata da capo a capo per l'audit. Un insieme di valutazione offline filtra ogni modifica di modello o prompt e budget per esecuzione limitano passi e spesa così che un agente che gira in tondo non possa far salire costo o latenza.

**Ente pubblico.** Un'agenzia di prestazioni sperimenta un agente per aiutare i funzionari di pratiche a mettere insieme i fatti di una richiesta: prelevare registri, controllare le regole di idoneità e redigere un riepilogo. L'agenzia traccia una linea netta: l'agente raccoglie e redige, ma un funzionario umano prende e possiede ogni decisione che colpisce un cittadino, perché la responsabilità delle decisioni del settore pubblico non può essere delegata a un modello (capitolo 6.5). Ogni esecuzione è completamente registrata, mostrando quali fonti sono state consultate e che cosa è stato redatto, così che un organo di controllo possa verificare qualsiasi caso. L'autonomia è deliberatamente limitata a leggere e redigere, gli strumenti sono al minimo privilegio e in sandbox e un insieme di valutazione avversariale conferma che l'agente rifiuta di agire oltre il raccogliere fatti.

## Business case: motivazioni, ROI e TCO

Gli agenti portano ritorno automatizzando lavoro a più passi che prima richiedeva a una persona di cliccare tra i sistemi: triage, riconciliazione, ricerca e operazioni di routine. Il valore compare come lavoro completato senza un umano a ogni passo, tempi di ciclo più rapidi e personale liberato per compiti ad alto giudizio. Poiché gli agenti si costruiscono su LLM e strumenti esistenti, il tempo a un prototipo funzionante è breve, ed è esattamente per questo che i team sovra-costruiscono.

Il costo totale di proprietà è dove gli agenti differiscono dalle semplici funzionalità LLM. Oltre al costo di inferenza paghi le integrazioni degli strumenti, l'impianto di sandboxing e permessi, il banco di valutazione, lo stack di tracciamento e osservabilità (capitolo 6.6) e i revisori umani che dotano di personale i cancelli di approvazione. Un agente che gira in tondo o mal limitato aggiunge un costo variabile che può schizzare senza avviso, quindi i budget su passi e spesa fanno parte del progetto, non un ripensamento. Il costo del non adottare è operazioni più lente e fatica manuale che i tuoi concorrenti automatizzano. Il costo dell'adottare con noncuranza è un'azione autonoma che invia il messaggio sbagliato, fa trapelare dati o prende una decisione senza responsabile. Presenta il caso alla leadership abbinando un obiettivo concreto di automazione a un piano concreto per guardrail, valutazione e supervisione umana e dicendo con onestà che i guardrail sono la maggior parte del costo.

## Antipattern e insidie

- **Agente quando un flusso basterebbe.** Assumersi l'intero rischio dell'autonomia per un compito i cui passi erano conoscibili.
- **Strumenti e credenziali troppo ampi.** Un unico strumento "fa tutto" anziché strumenti ristretti e al minimo privilegio.
- **Cecità alla prompt injection.** Immettere contenuto non fidato in un agente che detiene veri privilegi.
- **Nessun cancello umano sulle azioni irreversibili.** Lasciare che il modello invii, paghi o cancelli senza controllo.
- **Teatro multi-agente.** Dividere un compito semplice tra agenti, pagando costo di coordinamento senza guadagno.
- **Valutazione a sensazione.** Giudicare da come si legge la trascrizione anziché dal tasso di successo del compito.
- **Cicli illimitati.** Nessun tetto su passi, tempo o spesa, così un agente bloccato brucia denaro e latenza.
- **Esecuzioni non tracciate.** Nessuna registrazione di ciò che l'agente ha fatto, lasciandoti incapace di debuggare, verificare o rendere conto.

## Modello di maturità

- **Livello 1, Avvio:** Gli agenti sono prototipati ad hoc con ampio accesso agli strumenti e senza limiti. Il successo è giudicato dalle dimostrazioni, in modo reattivo, dopo che qualcosa si rompe. Non c'è un insieme di valutazione, né tracciamento, né cancello umano sulle azioni rilevanti.
- **Livello 2, Sviluppo:** Alcuni agenti hanno cicli limitati e strumenti al minimo privilegio ed esiste un tracciamento di base, ma la pratica varia da team a team. Un insieme di valutazione manuale coglie regressioni grossolane in pochi progetti mentre altri non ne hanno. L'approvazione umana protegge le azioni irreversibili più ovvie, eppure la copertura è disomogenea e non documentata.
- **Livello 3, Standardizzazione:** Schemi condivisi governano autonomia, permessi degli strumenti, sandboxing e cancelli con umano nel ciclo, documentati e fatti rispettare in ogni team. Ogni azione rilevante è filtrata o convalidata, gli agenti sono tracciati da capo a capo e un insieme di valutazione automatico con punteggio del tasso di successo gira a ogni modifica. La prompt injection è trattata come una minaccia permanente con una risposta definita.
- **Livello 4, Gestione:** Il portafoglio degli agenti è misurato e controllato rispetto a valori di riferimento. Tasso di successo per compito, tasso di superamento della difesa dalla prompt injection, costo e numero di passi per esecuzione, latenza di approvazione umana e incidenti di ciclo o fallimento sono seguiti come metriche; soglie di ripristino e di chiusura sono fatte rispettare su quell'evidenza anziché sulle lamentele. I budget per esecuzione su passi, tempo e spesa sono monitorati e una regressione in qualsiasi metrica innesca azione prima della scala, non dopo un incidente.
- **Livello 5, Orchestrazione:** L'autonomia è adeguata al rischio del compito per politica e regolata di continuo man mano che arrivano i risultati. La valutazione continua offline e online lega il comportamento dell'agente agli esiti di business e l'organizzazione ritira, ridefinisce o riassegna di routine i permessi agli agenti man mano che il quadro di rischio si sposta. Tracciamento, budget di costo e tracce di audit sono uniformi nel portafoglio; le difese da injection e confused deputy sono testate in modo avversariale; la responsabilità delle azioni autonome è chiara e verificabile.

## Spunti di discussione

1. Quali delle vostre attuali funzionalità LLM sono diventate in silenzio agenti, e l'autonomia di ciascuna è stata limitata di proposito?
2. Per ogni strumento dell'agente, qual è il modo più economico in cui un attaccante potrebbe abusarne attraverso contenuto iniettato, e che cosa lo impedisce?
3. Dove avete scelto progetti multi-agente, e potete mostrare che il costo di coordinamento ha ripagato rispetto a un singolo agente?
4. Quali azioni dell'agente sono davvero irreversibili, e ciascuna potrebbe essere riprogettata per essere reversibile o predisposta?
5. Se un agente compisse domani un'azione dannosa, potreste ricostruire esattamente che cosa ha fatto e chi ne era responsabile?

## Punti chiave

- Un agente è un LLM in un ciclo con strumenti, memoria e un obiettivo. Il rischio vive nel ciclo e negli strumenti, non nel testo.
- Preferisci un flusso fisso quando i passi sono noti; riserva l'autonomia agli obiettivi davvero aperti e limitala strettamente.
- L'uso degli strumenti è la capacità centrale. Dai a ogni strumento minimo privilegio, uno schema convalidato e una sandbox.
- Filtra le azioni rilevanti e irreversibili dietro un umano con reale autorità e progetta per un ripristino economico.
- Tratta gli agenti come avversariali: difenditi dalla prompt injection e dall'abuso del confused deputy (capitolo 4.2).
- Valuta sul tasso di successo del compito su molte esecuzioni e traccia ogni esecuzione per debug, controllo dei costi e audit (capitoli 6.5 e 6.6).
- Spesso la risposta giusta è non costruire affatto un agente.

## Riferimenti e letture di approfondimento

- Shunyu Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models*.
- Timo Schick et al., *Toolformer: Language Models Can Teach Themselves to Use Tools*.
- Anthropic, *Building Effective Agents* (indicazioni ingegneristiche su flussi contro agenti).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications* (comprese prompt injection ed eccessiva agency).
- Simon Willison, scritti sulla prompt injection e sulla "lethal trifecta" per gli agenti IA.
- Norman Hardy, *The Confused Deputy* (l'enunciazione classica del problema del confused deputy).
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Stuart Russell e Peter Norvig, *Artificial Intelligence: A Modern Approach* (agenti intelligenti e azione razionale).
