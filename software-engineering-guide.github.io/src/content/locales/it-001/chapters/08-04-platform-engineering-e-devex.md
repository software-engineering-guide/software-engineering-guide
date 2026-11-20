# 8.4 Platform engineering ed esperienza degli sviluppatori

## Panoramica e motivazioni

Il [platform engineering](https://en.wikipedia.org/wiki/Platform_engineering) è la disciplina di costruire e gestire un prodotto interno, una piattaforma interna per sviluppatori (IDP), che altri ingegneri usano per costruire, rilasciare e gestire il proprio software. Anziché ogni team assemblare da zero le proprie pipeline, infrastruttura e strumenti, un team di piattaforma dedicato fornisce capacità curate e self-service lungo "golden path" ben supportati, cioè percorsi opinati e supportati con predefiniti sensati incorporati. L'[esperienza degli sviluppatori](https://en.wikipedia.org/wiki/Developer_experience) (DevEx) è la questione strettamente correlata di come ci si sente a essere un ingegnere nell'organizzazione: con quanta facilità e rapidità uno sviluppatore può passare dall'idea al software in esecuzione e quanto attrito si frappone.

Per i grandi team, questo conta perché il [carico cognitivo](https://en.wikipedia.org/wiki/Cognitive_load) e l'attrito non scalano con grazia. Quando hai molti team, il numero di strumenti, sistemi e decisioni che ogni ingegnere deve destreggiare continua a crescere. Ben presto, una larga frazione del loro tempo va in impianti infrastrutturali e coordinamento anziché nel consegnare valore. Senza una piattaforma, ogni team risolve gli stessi problemi, come predisposizione, distribuzione, osservabilità e conformità, in modo incoerente e ripetuto. Una buona piattaforma assorbe questa complessità condivisa. I team possono allora concentrarsi sul proprio dominio ereditando comunque gli standard dell'organizzazione per sicurezza, affidabilità e costo.

La rilevanza per imprese ed enti pubblici è alta, perché queste organizzazioni combinano scala e rigorosa governance. Una piattaforma è il luogo naturale in cui codificare una volta sola requisiti di conformità, sicurezza e audit, come strade asfaltate che i team seguono per impostazione predefinita. Questo batte l'aspettarsi che ogni team interpreti e implementi correttamente la politica da solo. Trasforma la governance da fonte di attrito in una proprietà invisibile del flusso di lavoro standard, esattamente ciò di cui le grandi organizzazioni regolamentate hanno bisogno per muoversi in fretta senza perdere il controllo.

## Principi chiave

- Tratta la piattaforma come un prodotto, con utenti, una roadmap e il mandato di guadagnarsi l'adozione anziché imporla.
- Fornisci golden path: percorsi opinati e ben supportati che rendono il modo giusto il modo facile.
- Rendi le capacità self-service così che i team non aspettino ticket e passaggi di consegne umani.
- Asfalta strade anziché erigere cancelli; incorpora guardrail che guidano senza bloccare il lavoro legittimo.
- Riduci senza sosta il carico cognitivo sugli sviluppatori di applicazioni.
- Misura esperienza e produttività degli sviluppatori con segnali bilanciati e multidimensionali.
- Mantieni i golden path facoltativi ma così buoni che i team li scelgano.

## Raccomandazioni

### Costruisci la piattaforma come un prodotto

Il cambiamento singolo più importante è trattare la piattaforma come un prodotto al servizio di clienti interni, non come uno standard imposto dall'alto. In pratica, significa capire i bisogni degli sviluppatori attraverso ricerca e riscontri, mantenere una roadmap, misurare adozione e soddisfazione ed essere responsabili dell'esperienza. Una piattaforma che i team sono costretti a usare ma che li rallenta sarà odiata e aggirata. Una piattaforma che rende davvero i team più veloci si diffonderà per reputazione. L'adozione guadagnata con la qualità è la misura più vera del successo di una piattaforma.

### Fornisci golden path e strade asfaltate

Definisci golden path per i percorsi comuni: creare un nuovo servizio, distribuirlo, aggiungere un database, collegare l'osservabilità, soddisfare i requisiti di conformità. Un golden path è un percorso supportato, opinato e da capo a capo con predefiniti sensati incorporati. Lungo questi percorsi, incorpora guardrail, cioè scansione di sicurezza, controlli di politica e buone pratiche, così che un team che segue il percorso sia automaticamente conforme e sicuro. L'obiettivo è semplice: il modo più facile di fare una cosa dovrebbe essere anche quello corretto, sicuro e conforme. Mantieni i percorsi facoltativi, così che i team con esigenze davvero insolite possano divergere. Ma rendi i percorsi abbastanza convincenti da far sì che la maggior parte dei team non voglia mai farlo.

### Offri un'infrastruttura davvero self-service

Elimina i passaggi di consegne a ticket e attesa esponendo infrastruttura e capacità attraverso interfacce self-service: un portale, uno strumento a riga di comando, un'API o repository basati su modelli. Uno sviluppatore dovrebbe poter predisporre un ambiente conforme, avviare un nuovo servizio da un modello o richiedere un database in minuti, senza presentare una richiesta e aspettare giorni un altro team. Il self-service è ciò che trasforma una piattaforma da collo di bottiglia in acceleratore. E funziona solo perché i guardrail sottostanti rendono sicuro il self-service.

### Offri portali per sviluppatori, cataloghi dei servizi e scorecard

Un portale per sviluppatori ti dà un unico pannello di vetro: un catalogo di tutti i servizi con i loro responsabili, documentazione, dipendenze e salute. I cataloghi dei servizi rendono individuabili proprietà e architettura. È prezioso su larga scala, dove nessuno può tenere l'intero sistema in testa. Le scorecard misurano ogni servizio rispetto a standard come copertura dei test, postura di sicurezza, prontezza della reperibilità e documentazione e danno ai team un quadro chiaro e oggettivo di dove si trovano e che cosa migliorare. Insieme, questi strumenti tagliano il tempo che gli ingegneri spendono a cercare informazioni e chiariscono la responsabilità.

### Misura l'esperienza degli sviluppatori con quadri bilanciati

Resisti alle metriche di produttività a numero singolo. Sono facilmente manipolabili e ingannevoli. Usa quadri multidimensionali come SPACE (soddisfazione e benessere, prestazioni, attività, comunicazione e collaborazione, efficienza e flusso) per catturare la vera trama dell'esperienza degli sviluppatori. Combina dati percettivi da sondaggi con dati di sistema dagli strumenti. Segui metriche di consegna come tempo di consegna e frequenza di distribuzione accanto al sentimento degli sviluppatori. Lo scopo è capire e rimuovere l'attrito, non classificare gli individui. Una misurazione che sembra sorveglianza corroderà la fiducia da cui la piattaforma dipende.

### Riduci il carico cognitivo come obiettivo di prim'ordine

Il carico cognitivo, lo sforzo mentale totale che uno sviluppatore deve spendere per fare il proprio lavoro, è la tassa nascosta che le piattaforme esistono per ridurre. Minimizza il numero di strumenti, concetti e cambi di contesto che uno sviluppatore di applicazioni deve padroneggiare. Fornisci predefiniti sensati, così che i team prendano meno decisioni di basso valore. Struttura la proprietà così che ogni team possieda una fetta delimitata e comprensibile del sistema. Quando valuti qualsiasi funzionalità della piattaforma, poni una sola domanda: riduce o aumenta il carico sui team che la useranno?

## Compromessi: vantaggi e svantaggi

| Scelta | Vantaggi | Svantaggi | Adatto a |
|---|---|---|---|
| Piattaforma come prodotto (facoltativa) | Si guadagna l'adozione; resta utile | Più lenta a raggiungere la copertura completa | La maggior parte delle organizzazioni |
| Piattaforma imposta | Standardizzazione rapida | Risentimento; espedienti | Solo forti esigenze di governance |
| Comprare un portale/piattaforma | Più rapido a dare valore | Meno su misura; costo di licenza | Team che vogliono un vantaggio di partenza |
| Costruire in casa | Si adatta alle esigenze esatte | Alto costo di costruzione e manutenzione | Organizzazioni grandi e distintive |
| Solo golden path rigidi | Massima coerenza | Blocca i casi limite legittimi | Carichi molto uniformi |
| Percorsi flessibili con vie di fuga | Bilancia coerenza e autonomia | Un po' di divergenza da gestire | Esigenze di team diverse |

La tensione di fondo è standardizzazione contro autonomia. Troppo poca standardizzazione e ogni team reinventa la ruota in modo incoerente. Troppa e soffochi i team le cui esigenze differiscono davvero. La filosofia della piattaforma come prodotto risolve questo rendendo la standardizzazione attraente anziché obbligatoria. Un secondo vero compromesso è costruire contro comprare. Costruire una piattaforma in casa si adatta alle tue esigenze esatte ma comporta un costo continuo sostanziale. Adottare strumenti esistenti accelera il valore, al prezzo di una certa personalizzazione.

## Domande da discutere con il tuo team

1. **Come saprete che la piattaforma riduce il carico cognitivo anziché aggiungere un altro strumento da imparare?** Il carico cognitivo è lo sforzo mentale totale che un ingegnere spende per fare il lavoro e una piattaforma che aggiunge concetti e cambi di contesto può peggiorarlo pur apparendo impressionante. Adottate un test per ogni funzionalità: riduce o aumenta il carico sui team che la usano? Su larga scala è decisivo, perché una piattaforma sta davanti a centinaia di ingegneri e un'astrazione confusa li tassa tutti ogni giorno. Portate evidenza: quanti strumenti e portali uno sviluppatore tocca per rilasciare una modifica, il tempo al primo deploy per un nuovo assunto e riscontri qualitativi su dove le persone si bloccano. Se la piattaforma allunga la catena di strumenti anziché accorciarla, avete costruito una tassa, non una strada asfaltata.

2. **Quali standard fanno rispettare le vostre scorecard, e che cosa succede davvero a un servizio che ottiene un cattivo punteggio?** Le scorecard misurano ogni servizio rispetto ad aspettative come copertura dei test, postura di sicurezza, prontezza della reperibilità e documentazione e il loro valore crolla se un punteggio rosso non ha conseguenze. Decidete se le scorecard sono puramente consultive, alimentano la revisione o filtrano certe capacità e decidete chi possiede gli standard. Nelle organizzazioni regolamentate le scorecard possono dare agli organi di controllo una visibilità continua sulla postura di conformità, sostituendo la reportistica manuale, quindi l'asticella che fissate conta. Portate le vostre bozze di standard e un campione di servizi veri valutati rispetto ad esse e discutete dove i team si opporrebbero legittimamente. Una scorecard su cui nessuno agisce è una dashboard; una scorecard legata a chiare aspettative cambia il comportamento.

3. **State gestendo la piattaforma come un vero prodotto, con una roadmap, ricerca sugli utenti e metriche di adozione, o come un mandato?** La scommessa centrale di questo capitolo è che la standardizzazione dovrebbe essere attraente anziché imposta e questo regge solo se trattate gli ingegneri interni come clienti da conquistare. Decidete chi fa da product manager della piattaforma, come raccogliete i bisogni degli sviluppatori e quali numeri di adozione e soddisfazione definiscono il successo. Per le grandi organizzazioni un mandato è allettante perché standardizza in fretta, ma genera espedienti e risentimento quando gli strumenti rallentano le persone. Portate gli attuali tassi di adozione volontaria, i segnali di soddisfazione e i principali punti di attrito che i team riportano oggi. Se i team abbandonerebbero la piattaforma nel momento in cui il mandato cadesse, non avete costruito un prodotto, avete costruito una politica.

4. **Quando un team raggiunge il bordo di un golden path, qual è la via di fuga, e chi decide se allargare il percorso o tenere la linea?** Un golden path è un percorso supportato e opinato con predefiniti sensati e il suo valore viene dal fatto che la maggior parte dei team resti su di esso, eppure un percorso senza uscita diventa un cancello che spinge fuori del tutto dalla piattaforma il lavoro davvero insolito. Concordate in anticipo come un team chiede una deviazione, chi la rivede e come distinguete un'eccezione una tantum da un segnale che il percorso stesso dovrebbe cambiare. Per una grande organizzazione questa è la differenza tra una piattaforma che assorbe la diversità e una che si frammenta in strumenti ombra nel momento in cui un team si sente bloccato. Portate il conteggio attuale dei team che sono andati fuori percorso, le ragioni che hanno dato e quanto tempo richiede approvare un'eccezione. Nei contesti aziendali e governativi, legate ogni via di fuga ai controlli di conformità che aggira, così che una deviazione dalla strada asfaltata non diventi in silenzio una deviazione dalla base di sicurezza o di accreditamento.

5. **State costruendo la piattaforma in casa o comprandola, e avete prezzato onestamente il costo continuo di entrambe le strade?** La piattaforma è essa stessa un prodotto con un ciclo di vita e la scelta tra costruire e comprare fissa la vostra struttura di costo per anni: un portale interno si adatta alle vostre esigenze esatte ma richiede un team finanziato per mantenerlo, mentre una piattaforma acquistata raggiunge il valore più in fretta al prezzo di licenze e di un adattamento mai perfetto. Decidete quali capacità sono abbastanza distintive da costruire e quali sono commodity da comprare e rivedete quella linea man mano che i fornitori maturano. Per un grande team la posta è la leva: una scelta sbagliata di costruire affonda scarsi ingegneri senior in impianti che un prodotto avrebbe gestito, mentre una scelta sbagliata di comprare vincola centinaia di sviluppatori alla roadmap di qualcun altro. Portate una stima realistica del costo totale per ogni opzione, compresi manutenzione, aggiornamenti e costo di uscita. Negli appalti aziendali e governativi, aggiungete i termini di accreditamento e portabilità dei dati e preferite contratti che vi permettano di uscire senza abbandonare il catalogo dei servizi e le scorecard che avete costruito sopra.

6. **Come è finanziato e dimensionato il team di piattaforma rispetto agli sviluppatori che serve, e che cosa gli succede quando i budget si stringono?** Una piattaforma si guadagna il posto con la leva, poiché un piccolo team moltiplica la produttività di una popolazione molto più grande di sviluppatori di applicazioni, ma la stessa impostazione la rende un facile bersaglio quando la finanza cerca tagli e il beneficio è diffuso anziché attribuibile a una sola linea di prodotto. Decidete il modello di finanziamento, il rapporto tra ingegneri di piattaforma e sviluppatori che supportano e come difenderete quell'investimento con l'evidenza anziché con la fede. Per una grande organizzazione una piattaforma sottofinanziata è peggio di nessuna: i team dipendono da essa, decade e l'attrito ritorna con una dipendenza attaccata. Portate l'organico della piattaforma, il suo andamento di adozione e soddisfazione e una stima delle ore di sviluppo recuperate nell'organizzazione. Nel governo e nelle imprese regolamentate, presentate la piattaforma come il luogo in cui la conformità è codificata una volta, così che tagliarla non faccia risparmiare denaro, ma ridisperda il lavoro di audit e sicurezza su ogni team che dovrà ora farlo a mano.

## Lente settoriale

**Startup.** Con una manciata di ingegneri e nessun margine da sprecare, non montare un team di piattaforma; costruisci un unico repository modello di golden path che un nuovo servizio può clonare e far girare in un'ora. Precablalo con CI, una build di container, linting e un controllo di salute e lascia che si diffonda perché fa chiaramente risparmiare tempo, non perché qualcuno lo imponga. Compra ogni capacità commodity che puoi, mantieni piccola la catena di strumenti e tratta il carico cognitivo, non la copertura, come ciò che va protetto.

**Piccola impresa.** Non hai uno specialista di piattaforma dedicato e hai un budget stretto, quindi appoggiati a una piattaforma gestita o a un'offerta cloud opinata anziché costruire tu una piattaforma interna per sviluppatori. Imposta la decisione come comprare contro costruire e di default compra: un portale acquistato e i suoi modelli danno ai tuoi ingegneri generalisti dei golden path senza un team che li mantenga. Scegli strumenti self-service e facili da lasciare, così che un cambio di fornitore non lasci in secca la manciata di servizi che gestisci.

**Grande impresa.** Scala e molti team fanno della coerenza di portafoglio il premio: un team di piattaforma finanziato, golden path con guardrail, predisposizione self-service, un catalogo dei servizi e scorecard che rendono visibili proprietà e qualità su centinaia di servizi. Gestisci la piattaforma come un prodotto che si guadagna un'adozione volontaria anziché un mandato che genera espedienti e codifica sicurezza e conformità una volta come strade asfaltate così che la governance viaggi insieme per impostazione predefinita. Misura l'esperienza degli sviluppatori con quadri bilanciati e difendi il finanziamento della piattaforma con le ore di sviluppo recuperate.

**Ente pubblico.** Regole di appalto, trasparenza e responsabilità pubblica plasmano la piattaforma. Codifica i controlli di sicurezza obbligatori e i requisiti di accreditamento come guardrail lungo i golden path, così che un team che predispone attraverso il portale self-service erediti un ambiente che già soddisfa la base dei controlli, trasformando mesi di accreditamento manuale in un passaggio in gran parte automatizzato. Usa le scorecard per dare agli organi di controllo una visibilità continua e verificabile sulla postura di conformità e negli appalti esigi portabilità dei dati e interfacce aperte così che il catalogo e le strade asfaltate che costruisci non siano vincolati a un solo fornitore.

## Esempi

**Startup.** Una startup di dodici persone non ha un team di piattaforma, quindi un ingegnere senior spende qualche venerdì a costruire un unico repository modello "nuovo servizio" precablato con CI, un Dockerfile, linting e un controllo di salute. Qualsiasi ingegnere può clonarlo e avere un servizio in esecuzione in staging entro un'ora, anziché copiare la configurazione da un progetto più vecchio e indovinare le lacune. Il modello è il golden path e, poiché fa chiaramente risparmiare tempo a tutti, l'intero team lo adotta senza che a nessuno venga detto di farlo.

**Grande impresa.** Una grande compagnia di assicurazioni forma un team di piattaforma che rilascia un portale interno per sviluppatori. Cataloga ogni servizio con il suo responsabile, la documentazione e la scorecard di salute. I nuovi servizi sono creati da modelli golden path precablati con CI/CD, scansione di sicurezza, osservabilità e controlli di conformità. Database e ambienti sono predisposti in self-service attraverso il portale. Il tempo di inserimento di un nuovo ingegnere scende da settimane a giorni e l'evidenza di audit è prodotta automaticamente perché ogni servizio segue la stessa strada asfaltata. L'adozione della piattaforma è volontaria e si diffonde perché i team che la usano rilasciano in modo percettibilmente più rapido.

**Ente pubblico.** Un'agenzia federale che gestisce decine di servizi digitali mette in piedi una piattaforma condivisa. Codifica i controlli di sicurezza obbligatori e i requisiti di accreditamento come guardrail lungo i suoi golden path. Un team che predispone l'infrastruttura attraverso il portale self-service eredita un ambiente che già soddisfa la base dei controlli. Questo trasforma un esercizio di accreditamento manuale lungo mesi in uno in gran parte automatizzato. Le scorecard seguono la postura di conformità di ogni servizio, dando agli organi di controllo visibilità continua senza reportistica manuale e liberando il prezioso personale specialistico dalla revisione ripetitiva.

## Business case: motivazioni, ROI e TCO

Il ROI del platform engineering viene dal tempo degli sviluppatori recuperato e dalla coerenza guadagnata. Quando gli ingegneri spendono meno tempo a lottare con l'infrastruttura e a cercare informazioni, più del loro costoso tempo va a consegnare valore di prodotto. Inserimento più rapido, meno soluzioni duplicate e conformità automatizzata si traducono in capacità misurabile e rischio ridotto. Poiché la piattaforma serve molti team, ogni suo miglioramento è moltiplicato su tutta l'organizzazione.

Sul TCO, il costo di adozione è un investimento reale e continuo: un team di piattaforma finanziato, strumenti (costruiti o acquistati) e la disciplina di gestire la piattaforma come un prodotto con miglioramento continuo. Il costo del non adottare è diffuso ma grande: ogni team che paga ripetutamente la stessa tassa infrastrutturale, sicurezza e conformità incoerenti, inserimento lento e ingegneri senior che si consumano nella fatica. Per la leadership, il caso si presenta meglio in termini di leva. Un team di piattaforma modesto e ben gestito moltiplica la produttività di una popolazione molto più grande di sviluppatori di applicazioni e codifica la governance una volta anziché contare sul fatto che ogni team la faccia bene.

## Antipattern e insidie

- **Piattaforma imposta, non offerta.** Imporre una piattaforma che gli sviluppatori non gradiscono genera espedienti e risentimento.
- **Team di piattaforma nella torre d'avorio.** Costruire senza capire i veri bisogni degli sviluppatori produce strumenti che nessuno vuole.
- **Cancelli anziché strade asfaltate.** Guardrail che bloccano il lavoro legittimo spingono i team ad aggirare del tutto la piattaforma.
- **Metrica di produttività unica.** Ridurre la produttività a un solo numero manipolabile distorce il comportamento ed erode la fiducia.
- **Misurazione come sorveglianza.** Metriche DevEx usate per classificare gli individui distruggono la sicurezza psicologica di cui la piattaforma ha bisogno.
- **Golden path senza via di fuga.** Percorsi rigidi che non possono flettersi per i veri casi limite diventano ostacoli.
- **Piattaforma sottofinanziata.** Trattare la piattaforma come un progetto collaterale la affama e garantisce una cattiva esperienza.

## Modello di maturità

**Livello 1: Avvio.** Non esiste una piattaforma. Ogni team assembla i propri strumenti e la propria infrastruttura in modo reattivo, con pesanti passaggi di consegne a ticket, soluzioni duplicate e alto carico cognitivo. Ogni team risolve da solo predisposizione, distribuzione e conformità, in modo incoerente.

**Livello 2: Sviluppo.** Compaiono alcuni strumenti condivisi, modelli e repository di partenza, spesso costruiti da un ingegnere entusiasta, ma sono frammentati e in parte manuali. Alcuni team adottano un golden path mentre altri lo ignorano, il self-service è limitato e l'esperienza degli sviluppatori non è misurata, quindi il valore della piattaforma poggia sull'aneddoto.

**Livello 3: Standardizzazione.** Un team di piattaforma gestisce golden path documentati, predisposizione self-service, un portale per sviluppatori con un catalogo dei servizi e scorecard, applicati in tutta l'organizzazione. I guardrail per sicurezza, politica e conformità sono incorporati nelle strade asfaltate, così che il flusso di lavoro standard sia quello conforme e le stesse convenzioni valgano tra i team anziché variare per gruppo.

**Livello 4: Gestione.** La piattaforma è misurata e controllata con dati rispetto a valori di riferimento. Adozione, soddisfazione, tempo al primo deploy, tempo di consegna e frequenza di distribuzione sono seguiti con quadri bilanciati come SPACE e segnali combinati di sondaggi e di sistema; i risultati delle scorecard alimentano la revisione e carico cognitivo, tempo di inserimento e ore di sviluppo recuperate sono monitorati rispetto a obiettivi. Le decisioni di investire in una capacità o ritirarla poggiano sull'evidenza, non sul patrocinio.

**Livello 5: Orchestrazione.** La piattaforma è un prodotto maturo con alta adozione volontaria, continuamente migliorato da riscontri e metriche degli sviluppatori e integrato con la pianificazione di sicurezza, conformità e distribuzione nell'organizzazione. I golden path si adattano al mutare dei bisogni, la governance è una proprietà invisibile del flusso di lavoro standard e il team di piattaforma ritira, sostituisce e ridefinisce di routine le capacità man mano che evolvono tecnologia e organizzazione.

## Spunti di discussione

- Come vi guadagnate l'adozione di una piattaforma senza imporla, e quando, se mai, un mandato è giustificato?
- Quali golden path darebbero per primi più valore ai vostri team?
- Come misurate l'esperienza degli sviluppatori senza che sembri sorveglianza?
- Dove dovrebbero esistere vie di fuga così che i team insoliti non siano costretti a lasciare del tutto la piattaforma?
- Qual è la giusta dimensione e il giusto modello di finanziamento per un team di piattaforma rispetto agli sviluppatori che serve?
- Come decidete che cosa costruire in casa e che cosa comprare per il vostro portale per sviluppatori e i vostri strumenti?

## Punti chiave

- Gestisci la piattaforma come un prodotto che si guadagna l'adozione rendendo i team davvero più veloci.
- Fornisci golden path e strade asfaltate che rendono facile il modo corretto, sicuro e conforme.
- Offri vero self-service così che i team smettano di aspettare ticket e passaggi di consegne.
- Usa portali, cataloghi e scorecard per rendere visibili proprietà, architettura e qualità.
- Misura l'esperienza degli sviluppatori con quadri bilanciati come SPACE, mai con un solo numero manipolabile.
- Tratta la riduzione del carico cognitivo come lo scopo centrale della piattaforma.

## Riferimenti e letture di approfondimento

- Matthew Skelton e Manuel Pais, *Team Topologies*.
- Nicole Forsgren, Margaret-Anne Storey, Chandra Maddila et al., "The SPACE of Developer Productivity" (articolo).
- Nicole Forsgren, Jez Humble e Gene Kim, *Accelerate*.
- Gregor Hohpe, *The Software Architect Elevator*.
- Camille Fournier, *The Manager's Path*.
- Cloud Native Computing Foundation, white paper sul platform engineering.
