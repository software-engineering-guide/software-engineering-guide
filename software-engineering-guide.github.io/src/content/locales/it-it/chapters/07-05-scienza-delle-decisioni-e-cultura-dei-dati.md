# 7.5 Scienza delle decisioni e cultura basata sui dati

## Panoramica e motivazioni

La scienza delle decisioni è la pratica di collegare i dati alle decisioni reali, attingendo a statistica, scienze comportamentali e giudizio per aiutare le persone a scegliere bene in condizioni di incertezza. Una cultura basata sui dati è la condizione organizzativa in cui questo accade per impostazione predefinita: le persone cercano l'evidenza, ragionano con attenzione su causa ed effetto, comunicano l'incertezza con onestà e aggiornano le proprie convinzioni quando i dati lo giustificano. Questo capitolo è deliberatamente il coronamento della sequenza sui dati, perché tutta la strategia, l'ingegneria, l'analisi e la sperimentazione che lo precedono sono inutili se non cambiano le decisioni in meglio.

Per i grandi team è qui che gli investimenti sui dati falliscono più spesso, non nelle pipeline ma nell'ultimo miglio dalla conoscenza all'azione. Le imprese spendono molto in piattaforme e dashboard e prendono comunque le decisioni importanti per gerarchia, abitudine o per chi presenta con più sicurezza. Una modalità di fallimento comune è il teatro dei dati: dashboard e analisi elaborate prodotte per sembrare rigorose mentre la vera decisione era stata presa in anticipo e i dati scelti a posteriori per giustificarla. Gli enti pubblici aggiungono posta alta e controllo. Le decisioni di politica pubblica giustificate da deboli affermazioni causali possono allocare male denaro pubblico e danneggiare i cittadini e la richiesta di responsabilità fa del ragionare onestamente sull'evidenza un obbligo civico, non solo una buona pratica.

I problemi difficili qui sono cognitivi e culturali, non tecnici. Le persone confondono la [correlazione con la causalità](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation), ignorano i [fattori di confondimento](https://en.wikipedia.org/wiki/Confounding) (variabili nascoste che guidano sia la presunta causa sia l'effetto), si ancorano al primo numero che vedono e leggono le stime puntuali come certezze. E nella spinta a diventare guidate dai dati, le organizzazioni possono scivolare nella sorveglianza: misurare gli individui in modo così invasivo da distruggere la fiducia e provocare manipolazioni. Costruire una vera cultura della misurazione significa ragionare correttamente, comunicare fedelmente l'incertezza e misurare sistemi ed esiti senza trasformare i dati in uno strumento di controllo sulle persone.

## Principi chiave

- Lo scopo dei dati è decidere meglio, non produrre report.
- Decidi che cosa ti farebbe cambiare idea prima di guardare i dati.
- Correlazione non è causalità; interroga i fattori di confondimento prima di agire.
- Comunica l'incertezza con onestà; una stima puntuale senza intervallo inganna.
- Sii informato dai dati, non schiavo dei dati; giudizio e contesto contano ancora.
- Misura per imparare e migliorare i sistemi, non per sorvegliare e punire gli individui.
- Aggiorna le convinzioni quando l'evidenza lo giustifica; cambiare idea è una forza.
- La [sicurezza psicologica](https://en.wikipedia.org/wiki/Psychological_safety) è un prerequisito per un'analisi onesta e per il dissenso.

## Raccomandazioni

### Collega i dati alle decisioni ed evita il teatro dei dati

Lega l'analisi a una decisione specifica fin dall'inizio: che cosa faremo di diverso a seconda di ciò che troviamo? Prima di raccogliere i dati, enuncia la decisione, le opzioni e quale evidenza favorirebbe ciascuna, idealmente quale risultato ti farebbe cambiare idea. Questo protegge dal teatro dei dati, in cui l'analisi si limita a decorare una decisione già presa. Se nessun risultato realistico altererebbe la scelta, non spendere nell'analisi. Prendi con onestà la decisione di giudizio e dillo. Pretendi che le presentazioni partano dalla decisione e dalla raccomandazione, non da un giro di grafici.

### Ragiona con attenzione sulla causalità

La maggior parte delle domande di business e di politica pubblica è causale (questa azione produrrà questo esito), ma la maggior parte dei dati disponibili è osservazionale e infestata da fattori di confondimento. Insegna ai team la differenza tra correlazione e causalità e le trappole: variabili di confondimento, [distorsione di selezione](https://en.wikipedia.org/wiki/Selection_bias), causalità inversa e correlazione spuria. Preferisci gli esperimenti randomizzati per le affermazioni causali dove è fattibile. Dove gli esperimenti sono impossibili, usa accurate tecniche di [inferenza causale](https://en.wikipedia.org/wiki/Causal_inference) e dichiara esplicitamente le tue assunzioni anziché scivolare da "associato a" a "causa". Sii particolarmente scettico verso una storia convincente costruita su una singola correlazione.

### Comunica l'incertezza agli stakeholder

I numeri presentati come stime puntuali precise invitano a una falsa fiducia. Comunica intervalli, intervalli di confidenza o credibilità e le assunzioni chiave dietro qualsiasi cifra. Usa un linguaggio semplice e visualizzazioni oneste (barre di errore, intervalli, bande di scenario) così che i decisori colgano ciò che è noto e ignoto. Distingui ciò che i dati mostrano, ciò che deduci e ciò che assumi. Calibra la fiducia all'evidenza: presenta una previsione da pochi dati per quello che è. L'incertezza comunicata con onestà costruisce più fiducia della falsa precisione, perché sopravvive al contatto con la realtà.

### Costruisci una cultura della misurazione senza sorveglianza

Crea un ambiente in cui i team definiscono di routine metriche di successo, misurano gli esiti e imparano da essi, ma indirizza la misurazione a sistemi, processi ed esiti anziché al monitoraggio degli individui. Le metriche usate per sorvegliare e classificare le persone vengono manipolate, generano paura e distruggono l'onestà che le buone decisioni richiedono (una dinamica colta dalla [legge di Goodhart](https://en.wikipedia.org/wiki/Goodhart's_law): una misura che diventa un obiettivo smette di essere una buona misura). Privilegia metriche aggregate e orientate agli esiti. Coinvolgi i team nella scelta delle proprie misure e separa le metriche di apprendimento dalla valutazione delle prestazioni. Proteggi la sicurezza psicologica così che le persone portino a galla presto le cattive notizie e il dissenso.

### Favorisci sane abitudini e alfabetizzazione sui dati

Alza ampiamente l'alfabetizzazione sui dati così che le persone sappiano leggere un grafico con spirito critico, mettere in discussione la definizione di una metrica e individuare un'affermazione ingannevole. Normalizza il chiedere "come lo sappiamo?" e "che cosa ci farebbe cambiare idea?". Premia le persone che aggiornano le proprie opinioni alla luce dell'evidenza e che conducono esperimenti che falliscono in modo istruttivo. Rendi sicuro dire "i dati non ce lo dicono" anziché fabbricare certezza. I leader danno il tono: quando cambiano decisione in base all'evidenza e ammettono l'incertezza, la cultura segue.

### Proteggiti da pregiudizi e abusi

Fai attenzione ai pregiudizi prevedibili: la [distorsione di conferma](https://en.wikipedia.org/wiki/Confirmation_bias) nella scelta dei dati a sostegno, la [distorsione del sopravvissuto](https://en.wikipedia.org/wiki/Survivorship_bias) nell'ignorare ciò che manca, l'ancoraggio a un numero iniziale e la distorsione retrospettiva nei postmortem. Inserisci la revisione dell'avvocato del diavolo, la pre-registrazione di ciò che ti aspetti di trovare e prospettive diverse sulle analisi importanti. Prendi sul serio l'etica dei dati (equità, trasparenza ed evitare il danno), specialmente quando le decisioni incidono su mezzi di sussistenza, prestazioni o diritti delle persone.

## Compromessi: vantaggi e svantaggi

| Scelta | Vantaggi | Svantaggi | Adatto a |
|---|---|---|---|
| Guidato dai dati (i dati decidono) | Riduce i pregiudizi, coerente | Ignora il contesto, manipolabile, fragile | Domini ben compresi |
| Informato dai dati (dati più giudizio) | Bilancia evidenza e contesto | Più lento, richiede giudizio | Decisioni complesse o nuove |
| Sperimentare per la causalità | Forte evidenza causale | Costoso, lento, non sempre fattibile | Scelte reversibili ad alta posta |
| Inferenza osservazionale | Usa i dati disponibili | Rischio di confondimento, affermazioni più deboli | Quando gli esperimenti sono impossibili |
| Metriche di esito/di sistema | Guida il miglioramento, poca manipolazione | Meno responsabilità individuale | Culture dell'apprendimento |
| Sorveglianza individuale | Visibilità granulare | Manipolazione, paura, fiducia erosa | Raramente giustificata |

La tensione definitoria è rigore contro velocità e fattibilità. Gli esperimenti randomizzati danno la più forte evidenza causale, ma costano tempo e sono spesso impossibili per scelte strategiche o di politica pubblica una tantum, dove deve bastare un attento giudizio sui fattori di confondimento e assunzioni esplicite. La seconda tensione è tra misurazione e fiducia: più misuri gli individui in modo granulare, più puoi vedere e meno comportamento onesto ottieni. Una cultura matura propende per un giudizio informato dai dati e una misurazione aggregata e orientata agli esiti. Accetta una precisione apparente leggermente minore in cambio di decisioni che reggono e di una forza lavoro che dice la verità.

## Domande da discutere con il tuo team

1. **Enunci che cosa ti farebbe cambiare idea prima di guardare i dati, e quella domanda è scritta nei tuoi documenti di decisione?** La più forte protezione del capitolo dal teatro dei dati è nominare la decisione, le opzioni e l'evidenza che favorirebbe ciascuna, idealmente il risultato che ribalterebbe la tua scelta, prima di raccogliere i dati. Se nessun risultato realistico altererebbe la decisione, la mossa onesta è saltare l'analisi e prendere apertamente la decisione di giudizio. Per le imprese e gli enti in cui una singola scelta strategica o di politica pubblica può sprecare più dell'intero costo di un programma di analisi, questa disciplina ha un'alta leva. Porta una decisione recente e chiediti se qualche risultato avrebbe potuto cambiarla, o se i grafici si sono limitati a decorare una conclusione già raggiunta. Se "che cosa ci farebbe cambiare idea?" non è una domanda standard nei tuoi documenti di decisione, rendila tale e pretendi che le presentazioni partano dalla raccomandazione, non da un giro di grafici.

2. **Quando compare una correlazione convincente, come interroghi i fattori di confondimento prima di agire, e preferisci un esperimento dove è fattibile?** Il capitolo avverte che la maggior parte delle domande di business e di politica pubblica è causale mentre la maggior parte dei dati disponibili è osservazionale e piena di fattori di confondimento, distorsione di selezione e causalità inversa. I suoi stessi esempi ripetono un'unica trappola: i clienti coinvolti si auto-selezionano in una funzionalità o in un programma, così la correlazione grezza con un minore abbandono o con un maggiore reperimento di lavoro svanisce in un confronto controllato. Agire su quella correlazione significa una campagna o una politica costose e mal dirette. Porta una decisione recente che poggiava su una singola correlazione e chiediti quale variabile nascosta potrebbe guidare entrambi i lati. Dove un esperimento è fattibile, preferiscilo; dove non lo è, usa accurati metodi di inferenza causale e dichiara esplicitamente le tue assunzioni anziché scivolare da "associato a" a "causa".

3. **Le tue metriche sono mirate a migliorare sistemi ed esiti, o a monitorare gli individui, e hai separato le metriche di apprendimento dalla valutazione delle prestazioni?** Il capitolo traccia una linea netta: la misurazione puntata sulle persone viene manipolata, genera paura e distrugge l'onestà che le buone decisioni richiedono, una dinamica che la legge di Goodhart prevede una volta che una misura diventa un obiettivo. Privilegia metriche aggregate e orientate agli esiti, il coinvolgimento dei team nella scelta delle proprie misure e la protezione della sicurezza psicologica così che le persone portino presto a galla le cattive notizie. Nei contesti governativi e aziendali, sorvegliare il personale in prima linea erode la fiducia che rende possibili dati accurati fin dall'inizio. Porta la domanda concreta: quali delle tue metriche potrebbero essere usate per classificare o punire gli individui e le persone le manipolerebbero sotto pressione? Se metriche di apprendimento e valutazione delle prestazioni sono intrecciate, separale, così che la misurazione guidi il miglioramento anziché un comportamento difensivo.

4. **Quando un numero arriva a un decisore, arriva come un intervallo con le sue assunzioni allegate, o come una stima puntuale che invita a una falsa fiducia?** Il capitolo sostiene che l'incertezza comunicata con onestà costruisce più fiducia della falsa precisione, perché sopravvive al contatto con la realtà, eppure la spinta verso un'unica cifra sicura è forte quando un leader vuole una risposta netta. Per un grande team la pressione contraria è reale: intervalli e barre di errore possono sembrare evasivi a dirigenti che premiano la decisione, quindi gli analisti imparano a togliere le cautele per farsi sentire. Porta un report recente e controlla se distingueva ciò che i dati mostrano, ciò che hai dedotto e ciò che hai assunto e se una previsione costruita su pochi dati era etichettata esattamente per quello che era. Nei contesti aziendali e governativi, dove una cifra può finire in un fascicolo per il consiglio, in una richiesta di bilancio o in una testimonianza pubblica, una stima puntuale presentata come certezza è una passività, quindi concorda uno standard della casa per cui le cifre rilevanti portano un intervallo, le assunzioni chiave e una dichiarazione semplice di confidenza.

5. **Qui è davvero sicuro dire "i dati non ce lo dicono", e a chi è permesso mettere in discussione come è definita una metrica?** Il capitolo tratta l'alfabetizzazione sui dati e la sicurezza psicologica come prerequisiti: le persone devono saper leggere un grafico con spirito critico, chiedere "come lo sappiamo?" e ammettere l'incertezza senza penalità, o la cultura fabbrica falsa certezza per impostazione predefinita. La tensione per una grande organizzazione è che un'ampia alfabetizzazione richiede tempo di formazione e budget veri e mettere in discussione la metrica preferita di una persona anziana può sembrare dannoso per la carriera, quindi numeri non esaminati viaggiano verso l'alto senza essere contestati. Porta evidenza su chi nella stanza può davvero interrogare la definizione e la provenienza di una metrica e ricorda l'ultima volta che qualcuno è stato premiato anziché punito per aver aggiornato la propria opinione o riportato un fallimento istruttivo. Per imprese ed enti pubblici, dove una misura mal definita può guidare finanziamenti o rendicontazione pubblica, nomina esplicitamente chi ha titolo per contestare una metrica e proteggilo quando lo fa.

6. **Come proteggi le analisi importanti dai pregiudizi prevedibili, e inserisci il dissenso prima di una decisione anziché dopo?** Il capitolo elenca le trappole che corrompono in silenzio l'evidenza: la distorsione di conferma nella scelta dei dati a sostegno, la distorsione del sopravvissuto nell'ignorare ciò che manca, l'ancoraggio a un numero iniziale e la distorsione retrospettiva nei postmortem. La considerazione contraria è la velocità, poiché la revisione dell'avvocato del diavolo, la pre-registrazione di ciò che ti aspetti di trovare e le prospettive diverse rallentano tutte una decisione e sono le prime cose tagliate sotto pressione di scadenza. Porta una recente analisi ad alta posta e chiediti che cosa sarebbe emerso se qualcuno fosse stato incaricato di sostenere il caso opposto e se il team aveva scritto le proprie aspettative prima di vedere i risultati. Nei contesti aziendali e specialmente governativi, dove le decisioni incidono su mezzi di sussistenza, prestazioni o diritti delle persone, tratta l'etica dei dati e il dissenso strutturato come requisiti permanenti delle analisi rilevanti, non extra che un trimestre affollato può lasciar cadere in silenzio.

## Lente settoriale

**Startup.** Senza analisti e con poche settimane di autonomia per ogni scommessa, la tua scienza delle decisioni è un'abitudine anziché una funzione: prima di un grande impegno, chiedi quale risultato ti farebbe cambiare idea e se un esperimento economico può rispondere più in fretta di una riunione. Guardati con decisione dallo scommettere il trimestre su una singola correlazione appariscente, perché un team minuscolo non si riprende da una roadmap mal diretta. Tienila leggera, una riga scritta nel documento di decisione che nomina il segnale che ti farebbe fermare, non una revisione formale che non eseguirai mai.

**Piccola impresa.** Probabilmente non hai uno specialista dei dati e compri analisi dentro strumenti che già usi, quindi il rischio è fidarsi di una dashboard del fornitore senza mettere in discussione come è definita una metrica o se il suo confronto è equo. Spendi la tua scarsa attenzione sul ragionamento anziché sugli strumenti: separa correlazione e causalità sulle una o due decisioni che muovono davvero l'attività e dichiara onestamente a te stesso l'intervallo prima di impegnare denaro che non puoi riavere. Quando uno strumento si offre di automatizzare una decisione, tieni una persona nel ciclo ovunque una scelta sbagliata ti costerebbe un cliente.

**Grande impresa.** Tra molti team il problema è coerenza e governance: un'aspettativa condivisa che le analisi nominino in anticipo la decisione e i criteri di chiusura, che le affermazioni causali dichiarino le proprie assunzioni e che le cifre rilevanti portino intervalli nei fascicoli per il consiglio e negli audit. Separa le metriche di apprendimento dalla valutazione delle prestazioni in tutta l'organizzazione così che la misurazione non degeneri in sorveglianza e manipolazione. Investi in un'ampia alfabetizzazione sui dati e in pratiche di revisione come l'avvocato del diavolo e la pre-registrazione, così che un presentatore sicuro di sé non possa sostituire l'evidenza su larga scala.

**Ente pubblico.** Appalti, trasparenza e responsabilità pubblica alzano la posta su ogni affermazione causale, perché una politica giustificata da una correlazione spuria alloca male denaro pubblico e può danneggiare i cittadini. Preferisci disegni di confronto rigorosi per la valutazione dei programmi, comunica gli effetti come intervalli con assunzioni dichiarate agli organi di controllo e documenta il ragionamento così che un audit possa seguirlo. Indirizza la misurazione agli esiti dei programmi anziché alla sorveglianza dei funzionari e dai al pubblico un resoconto chiaro di come l'evidenza ha plasmato la decisione.

## Esempi

**Startup.** Una startup pre-Serie A ha notato che gli utenti iscritti al forum della community abbandonavano molto meno e i fondatori erano pronti a puntare l'intera roadmap su funzionalità del forum. Prima di impegnarsi, uno ha chiesto che cosa avrebbe cambiato loro idea e uno sguardo rapido ha mostrato che i clienti già fidelizzati erano semplicemente quelli che si prendevano la briga di iscriversi al forum. Hanno condotto un piccolo esperimento anziché scommettere il trimestre su una correlazione e hanno fatto di "che cosa ci farebbe cambiare idea?" una domanda standard nei documenti di decisione.

**Grande impresa.** Un'azienda di servizi finanziari ha notato che i clienti che usavano una particolare funzionalità avevano un abbandono molto minore e ha quasi lanciato una costosa campagna per spingere tutti verso di essa. Una revisione di scienza delle decisioni ha segnalato l'ovvio fattore di confondimento: i clienti già coinvolti si auto-selezionavano nella funzionalità. Un esperimento controllato ha poi mostrato che la funzionalità in sé aveva poco effetto causale sull'abbandono. L'azienda ha evitato un grande investimento mal diretto e la leadership ha adottato "che cosa ci farebbe cambiare idea?" come domanda standard prima delle grandi spese.

**Ente pubblico.** Un'agenzia pubblica che valutava un programma per l'occupazione ha resistito a rivendicare il successo dalla statistica grezza secondo cui i partecipanti trovavano lavoro a un tasso elevato, riconoscendo che persone motivate si auto-selezionano in tali programmi. Ha usato un disegno di confronto rigoroso e ha comunicato l'effetto stimato come un intervallo con assunzioni dichiarate agli organi di controllo. La misurazione si è concentrata sugli esiti del programma anziché sulla sorveglianza dei funzionari, il che ha preservato la fiducia in prima linea guidando comunque responsabilità e miglioramento.

## Business case: motivazioni, ROI e TCO

Il ROI della scienza delle decisioni è il costo evitato di decisioni sbagliate prese con sicurezza e la migliore qualità delle decisioni che un'organizzazione prende migliaia di volte. Una singola grande scelta strategica o di politica pubblica giustificata da una correlazione spuria può sprecare molto più dell'intero costo di costruire buone pratiche decisionali. Una migliore calibrazione (sapere che cosa sai e che cosa non sai) ti permette di dimensionare le scommesse in modo appropriato ed evitare sia impegni sconsiderati sia la paralisi. In aggregato, una cultura basata sui dati si compone: ogni team che prende decisioni appena migliori e meglio ragionate è una leva enorme.

Il costo di adozione è per lo più culturale e formativo: formazione sull'alfabetizzazione dei dati, tempo per un'analisi e una revisione accurate e la disponibilità dei leader a cambiare decisione e ad ammettere l'incertezza. In denaro costa meno delle piattaforme dei capitoli precedenti ma è più difficile da installare, perché chiede a persone potenti di farsi governare dall'evidenza. Pesalo contro il costo del non adottare: teatro dei dati che spreca sforzo analitico, decisioni guidate dalla voce più sicura di sé, affermazioni causali che crollano al contatto con la realtà e, dove la sorveglianza prende piede, una forza lavoro che manipola le metriche e nasconde le cattive notizie. Alla leadership, il caso è semplice. Tutto l'investimento precedente sui dati si ripaga solo se l'ultimo miglio dalla conoscenza alla decisione è solido e la scienza delle decisioni è quell'ultimo miglio.

## Antipattern e insidie

- Teatro dei dati: analisi prodotta per giustificare una decisione già presa.
- Scivolare da "correlato con" a "causa" senza interrogare i fattori di confondimento.
- Presentare stime puntuali come certezze, nascondendo l'intervallo di incertezza.
- Distorsione di conferma: cercare solo dati che sostengono una conclusione preferita.
- Decisioni HiPPO in cui l'opinione della persona meglio pagata prevale sull'evidenza.
- Trasformare le metriche in sorveglianza individuale, provocando manipolazione e paura.
- La legge di Goodhart in azione: una metrica obiettivo che smette di misurare ciò che conta.
- Punire le persone per fallimenti istruttivi, uccidendo onestà e sperimentazione.

## Modello di maturità

1. **Avvio.** Le decisioni corrono su gerarchia e intuizione e vince la voce più forte o più anziana. La correlazione è trattata liberamente come causalità, l'incertezza è ignorata e le poche metriche in uso sorvegliano gli individui e vengono manipolate.
2. **Sviluppo.** Alcuni team consultano i dati e mostrano consapevolezza delle trappole causali, ma l'analisi è spesso selettiva, prodotta per giustificare una decisione già presa. L'incertezza è raramente comunicata e le pratiche di misurazione sono incoerenti da un team all'altro.
3. **Standardizzazione.** L'organizzazione documenta e fa rispettare una pratica condivisa: le analisi sono legate a una decisione nominata con criteri predefiniti, i team distinguono correlazione e causalità e preferiscono gli esperimenti per le affermazioni causali, i numeri portano intervalli e assunzioni dichiarate e la misurazione è indirizzata agli esiti anziché agli individui, con la sicurezza psicologica protetta.
4. **Gestione.** La qualità delle decisioni è misurata e controllata rispetto a valori di riferimento. L'organizzazione segue quanto spesso le analisi hanno nominato un segnale di chiusura prima che arrivassero i dati, la quota di cifre rilevanti uscite con un intervallo comunicato, quante affermazioni causali poggiavano su esperimenti anziché su semplice correlazione e se le decisioni sono state invertite sull'evidenza. Le pratiche di protezione dai pregiudizi come la pre-registrazione e la revisione dell'avvocato del diavolo sono verificate e le metriche che cominciano a essere manipolate sono colte e ritirate.
5. **Orchestrazione.** Il ragionamento solido è continuamente migliorato e integrato nell'organizzazione. "Che cosa ci farebbe cambiare idea?" è una routine prima di qualsiasi decisione importante, il rigore causale e l'onesta incertezza sono norme culturali e i leader si aggiornano visibilmente sull'evidenza e ammettono ciò che non si sa. La misurazione guida l'apprendimento senza sorveglianza, le pratiche decisionali si adattano al mutare di organizzazione e rischi e ogni livello decide meglio di conseguenza.

## Spunti di discussione

- Dove nella vostra organizzazione i dati sono usati per decorare decisioni già prese?
- Quale decisione recente poggiava su una correlazione che potrebbe non essere causale?
- Con quanta onestà i vostri report comunicano l'incertezza, e chi resiste agli intervalli?
- Le vostre metriche sono mirate a migliorare i sistemi o a monitorare gli individui?
- Quando un leader ha cambiato per ultimo visibilmente una decisione a causa dei dati?
- Come impedite che la ricerca della misurazione sconfini nella sorveglianza?

## Punti chiave

- Il punto dei dati è decidere meglio; proteggiti dal teatro dei dati.
- Enuncia che cosa ti farebbe cambiare idea prima di guardare i dati.
- Non scambiare mai correlazione per causalità; interroga i fattori di confondimento e preferisci gli esperimenti.
- Comunica l'incertezza con onestà; la falsa precisione distrugge la fiducia quando fallisce.
- Sii informato dai dati, non schiavo dei dati; giudizio e contesto contano ancora.
- Misura sistemi ed esiti per imparare, non gli individui per sorvegliarli.
- Proteggi la sicurezza psicologica così che le persone aggiornino le convinzioni e portino a galla le cattive notizie.

## Riferimenti e letture di approfondimento

- Daniel Kahneman, "Thinking, Fast and Slow."
- Judea Pearl e Dana Mackenzie, "The Book of Why."
- Douglas W. Hubbard, "How to Measure Anything."
- Nate Silver, "The Signal and the Noise."
- Cathy O'Neil, "Weapons of Math Destruction."
- Darrell Huff, "How to Lie with Statistics."
- Philip Tetlock e Dan Gardner, "Superforecasting."
- Charles Wheelan, "Naked Statistics."
