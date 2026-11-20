# 8.3 Container, orchestrazione e cloud-native

## Panoramica e motivazioni

Un [container](https://en.wikipedia.org/wiki/OS-level_virtualization) impacchetta un'applicazione insieme alle sue dipendenze in un'unica unità portabile e isolata. Gira allo stesso modo su un portatile, in un ambiente di test e in produzione. Le piattaforme di orchestrazione, la più nota delle quali è [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes), pianificano e gestiscono grandi numeri di container su flotte di macchine. Gestiscono collocazione, scalatura, salute, rete e ripristino. Il [cloud-native](https://en.wikipedia.org/wiki/Cloud-native_computing) è lo stile architetturale più ampio costruito su queste fondamenta: applicazioni progettate come servizi debolmente accoppiati, distribuibili in modo indipendente e scalabili orizzontalmente che presuppongono un'infrastruttura dinamica e auto-riparante.

Per i grandi team, container e orchestrazione risolvono un problema difficile. Devi eseguire molti servizi, costruiti da molti team, in modo affidabile ed efficiente su un'infrastruttura condivisa. I container danno a ogni team un contratto coerente di impacchettamento e di runtime, che ritira la classe di fallimenti del "da me funziona". L'orchestrazione nasconde le singole macchine dietro un substrato comune, così i team distribuiscono su una piattaforma anziché su server. Questa standardizzazione è ciò che ti permette di gestire centinaia o migliaia di servizi senza che ogni team reinventi distribuzione, scalatura e resilienza.

Le organizzazioni aziendali e governative che adottano ottengono portabilità, resilienza e una via di uscita dal lock-in. In cambio, ereditano vera complessità e nuove responsabilità di sicurezza. Una piattaforma di container è potente proprio perché è programmabile e dinamica, il che significa che devi governarla con cura. Provenienza delle immagini, isolamento multi-tenant, politica di rete e costo diventano tutte questioni a livello di piattaforma. Chi adotta nel settore pubblico aggiunge sempre più requisiti di sovranità: il controllo su dove risiedono i dati e su chi vi può accedere. Questo fa della capacità di eseguire carichi coerenti in ambienti scelti una capacità strategica, non solo un dettaglio tecnico.

## Principi chiave

- Impacchetta le applicazioni come immagini di container piccole, a scopo singolo e immutabili.
- Pratica l'igiene delle immagini: immagini di base minime, versioni fissate, scansionate per vulnerabilità e firmate.
- Progetta le applicazioni perché siano senza stato e scalabili orizzontalmente dove possibile, esternalizzando lo stato.
- Tratta il modello a stato desiderato della piattaforma di orchestrazione come fonte di verità e lascia che si auto-ripari.
- Fai rispettare isolamento e minimo privilegio tra tenant, carichi e namespace.
- Segui i principi [twelve-factor](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology), una metodologia per costruire app usa e getta, con configurazione esternalizzata e scalabili orizzontalmente, ed estendili per le realtà dei sistemi distribuiti.
- Fai del costo una questione ingegneristica di prim'ordine e visibile, non un ripensamento.
- Preferisci astrazioni portabili e basate su standard per preservare la flessibilità strategica.

## Raccomandazioni

### Pratica una rigorosa igiene delle immagini

L'immagine di container è la tua unità fondamentale di fiducia e di distribuzione, quindi trattala come tale. Parti da immagini di base minime e fidate per ridurre la superficie d'attacco. Fissa le versioni delle dipendenze e delle immagini di base per la riproducibilità. Scansiona ogni immagine per vulnerabilità note nella pipeline di build e blocca quelle con rilievi critici. Firma le immagini e verifica le firme al momento della distribuzione, così che girino solo immagini approvate e non modificate. Tieni un registro interno curato di immagini di base rinforzate da cui i team costruiscono. Questo diffonde automaticamente buoni predefiniti di sicurezza.

### Usa gli schemi di Kubernetes anziché reinventarli

Kubernetes premia i team che adottano i suoi schemi consolidati e punisce quelli che combattono il suo modello. Usa manifest dichiarativi per lo stato desiderato. Aggiungi sonde di salute così che la piattaforma possa rilevare e sostituire le istanze non sane. Imposta richieste e limiti di risorse così che lo scheduler possa impacchettare i carichi in sicurezza. Usa la scalatura orizzontale automatica per la domanda elastica. Per la logica operativa che deve girare in continuo, come gestire un database, ruotare i certificati o riconciliare risorse personalizzate, usa lo schema operator, che codifica la conoscenza operativa umana in software che osserva lo stato e agisce. Resisti alla tentazione di costruire un'orchestrazione su misura sopra la piattaforma. Preferisci i costrutti nativi.

### Progetta deliberatamente la multi-tenancy

Quando molti team condividono un cluster, l'isolamento è un requisito di sicurezza e affidabilità, non una finezza. Usa i namespace come confini di tenancy. Fai rispettare quote di risorse così che nessun tenant possa affamare gli altri. Applica politiche di rete per limitare il traffico a ciò che è esplicitamente consentito. Usa il [controllo degli accessi basato sui ruoli](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) per limitare ciò che ogni team può fare. Per i carichi con esigenze di isolamento più forti, considera cluster separati o una sandbox più forte. Decidi presto se il tuo modello è multi-tenancy morbida (team interni fidati) o rigida (carichi che si diffidano a vicenda), perché i due richiedono controlli molto diversi.

### Costruisci cloud-native, twelve-factor e oltre

La metodologia twelve-factor, con le sue dipendenze esplicite, la configurazione nell'ambiente, i processi senza stato, la disposability e così via, resta un'ottima base di riferimento per i servizi che prosperano su una piattaforma dinamica. Estendila per le realtà aggiuntive dei sistemi distribuiti. Progetta per il fallimento parziale. Rendi le operazioni idempotenti e ripetibili. Esponi salute e telemetria. Tratta l'osservabilità come una funzionalità incorporata anziché un'aggiunta. Esternalizza tutto lo stato a servizi di dati gestiti, così che le istanze dell'applicazione restino usa e getta e scalabili orizzontalmente.

### Pianifica in modo pragmatico strategie multi-cloud, ibride e sovrane

La portabilità è preziosa, ma perseguila con occhi chiari. Standardizzati su astrazioni portabili come container, Kubernetes e API aperte, così che i carichi possano spostarsi se serve. Ma evita la trappola di rifiutare ogni servizio gestito, che scambia vera produttività contro una portabilità ipotetica. Per i requisiti ibridi e sovrani, progetta in modo che gli stessi carichi e le stesse pipeline possano girare in una regione scelta, in un data center privato o in un cloud sovrano che soddisfa le regole giurisdizionali e di residenza dei dati. Rendi esplicite nell'architettura e nella politica le frontiere di sovranità e residenza.

### Rendi visibile il costo con il FinOps

Negli ambienti cloud elastici, il costo è una conseguenza diretta delle decisioni ingegneristiche, quindi dai agli ingegneri visibilità e responsabilità. Etichetta le risorse per l'allocazione dei costi. Attribuisci la spesa a team e servizi. Mostra i dati di costo accanto alle metriche di prestazione. Dimensiona correttamente i carichi, usa la scalatura automatica per adeguarti alla domanda e recupera le risorse inattive. Stabilisci una pratica FinOps che riunisca ingegneria, finanza e prodotto, così che la spesa cloud diventi una responsabilità condivisa e continua anziché una sorpresa trimestrale.

## Compromessi: vantaggi e svantaggi

| Scelta | Vantaggi | Svantaggi | Adatto a |
|---|---|---|---|
| Kubernetes | Potente, portabile, enorme ecosistema | Complessità ripida; onere operativo | Molti servizi su larga scala |
| Servizio di container gestito | Meno onere operativo; avvio più rapido | Un certo lock-in; meno controllo | Team che vogliono semplicità |
| Un unico cluster condiviso | Uso efficiente delle risorse | Isolamento più difficile; raggio d'impatto | Tenant interni fidati |
| Un cluster per tenant | Forte isolamento | Costo e onere più alti | Carichi che si diffidano o regolamentati |
| Portabilità multi-cloud | Flessibilità; evita il lock-in | Servizi al minimo comune denominatore | Mitigazione del rischio strategico |
| Servizi gestiti profondi di un solo cloud | Massima produttività | Dipendenza dal fornitore | Team focalizzati sulla velocità |

Il compromesso di fondo è capacità contro complessità. Kubernetes e le architetture cloud-native danno elasticità, resilienza e velocità. Ma impongono un onere operativo e cognitivo sostanziale che i piccoli team sottovalutano di routine. Allo stesso modo, inseguire la piena portabilità [multi-cloud](https://en.wikipedia.org/wiki/Multicloud) scambia produttività contro opzionalità. La risposta giusta dipende da scala e rischio. Le grandi organizzazioni con molti team e forti esigenze di governance di solito giustificano l'investimento. Gli sforzi più piccoli sono spesso meglio serviti da servizi gestiti che nascondono la complessità.

## Domande da discutere con il tuo team

1. **Firmate le immagini e verificate le firme al momento della distribuzione, e una vulnerabilità critica blocca davvero la build?** L'immagine è la vostra unità di fiducia, quindi la supply chain attorno ad essa merita cancelli rigidi, non avvisi. Decidete se possono girare solo immagini firmate e verificate, se la scansione blocca i rilievi critici o si limita a registrarli e chi mantiene il registro curato di immagini di base rinforzate da cui i team costruiscono. Per i carichi aziendali e governativi questo è spesso un requisito di conformità ed è anche la vostra miglior difesa contro una dipendenza avvelenata che raggiunge la produzione. Portate lo stato attuale: quale frazione delle immagini in esecuzione viene dalla vostra base rinforzata, quante portano CVE critiche non corrette e se un'immagine non firmata può oggi essere pianificata. Se un rilievo critico non ferma una distribuzione, il vostro scanner è decorazione.

2. **Come impediscono richieste, limiti e quote che un carico affami i vicini, senza lasciare inattiva capacità costosa?** Su un cluster condiviso, un carico senza limiti può mandare in crash o strozzare tutto ciò che lo circonda e quote fissate in modo troppo generoso sprecano i guadagni di utilizzo che giustificano la piattaforma. Decidete predefiniti sensati, chi li regola e come cogliete i carichi senza alcuna richiesta impostata. Su larga scala questo è sia un controllo di affidabilità sia un controllo di costo, perché il dimensionamento corretto è dove vive gran parte del risparmio FinOps. Portate dati: l'utilizzo attuale del cluster, quanto spesso i carichi vengono evacuati o strozzati e quali namespace non hanno quote. L'obiettivo è un impacchettamento denso e sicuro, quindi trattate i limiti mancanti come un difetto che la piattaforma respinge.

3. **Quale stato può vivere dentro un container, e dove va tutto il resto?** La resilienza cloud-native dipende da istanze usa e getta che la piattaforma può ripianificare a piacere e questo regge solo se lo stato importante vive in servizi di dati gestiti anziché sul disco locale del container. Decidete la regola esplicitamente, perché lo stato memorizzato in un container per caso diventa perdita di dati alla successiva ripianificazione. Per i team che migrano applicazioni più vecchie questa è spesso la parte più difficile, poiché i servizi preesistenti presuppongono un filesystem locale stabile. Portate un inventario: quali servizi scrivono stato locale, quali si affidano a sessioni appiccicose o affinità di nodo e che cosa servirebbe per esternalizzare ciascuno. Finché lo stato non è esterno, avete container che sembrano elastici ma che in realtà non possono essere spostati.

4. **Quando molti team condividono un cluster, il vostro modello di isolamento è scelto deliberatamente come multi-tenancy morbida o rigida, e i controlli corrispondono a quella scelta?** I namespace separano team interni fidati, ma non contengono un carico attivamente ostile o compromesso e trattare la tenancy morbida come se fosse rigida è un incidente di sicurezza in attesa di accadere. Decidete per carico se i tenant hanno solo bisogno di una condivisione equa o devono essere assunti come reciprocamente diffidenti, poi adeguate i controlli: namespace, quote, politiche di rete e RBAC per il caso morbido, cluster separati o una sandbox più forte per il caso rigido. Per una grande organizzazione questa decisione guida direttamente il costo, perché un cluster per tenant è molto più costoso di namespace condivisi, quindi volete spendere il budget di isolamento solo dove il modello di minaccia lo richiede. Portate l'inventario dei tenant: quali carichi condividono oggi un cluster, quali gestiscono traffico regolamentato o rivolto all'esterno e dove la politica di rete è ancora consenti-tutto. Nei contesti aziendali e governativi, mescolare carichi che si diffidano sotto una tenancy morbida è esattamente il rilievo che un auditor segnalerà, quindi nominate il confine prima che lo facciano loro.

5. **Quanto state pagando per la portabilità multi-cloud, e la userete mai davvero?** Standardizzarsi su container, Kubernetes e API aperte mantiene i carichi spostabili, ma rifiutare ogni servizio gestito per preservare quell'opzione scambia vera produttività quotidiana contro una portabilità che l'organizzazione potrebbe non esercitare mai. Decidete dove la portabilità è un vero requisito, come un obbligo di sovranità o di uscita che avete firmato, rispetto a dove è una coperta di conforto che rallenta ogni team. La considerazione contraria è la velocità: i servizi gestiti profondi rilasciano funzionalità più in fretta e un'architettura al minimo comune denominatore è una tassa permanente su ogni team. Portate l'evidenza: quali servizi gestiti avete evitato e quanto è costato in tempo di ingegneria, se avete mai spostato un carico tra fornitori e che cosa i vostri contratti vi obbligano davvero a fare. Per chi adotta nel governo e nei contesti regolamentati, le regole su residenza dei dati e cloud sovrano possono rendere la portabilità non negoziabile, quindi progettate in modo che gli stessi manifest e le stesse pipeline girino in una regione sovrana e in un'enclave privata, ma siate onesti che questo è un costo di conformità e non un'assicurazione gratuita.

6. **Ogni team può vedere quanto spende, e qualcuno possiede la bolletta prima che diventi una sorpresa?** In una piattaforma elastica, il costo è un esito diretto delle decisioni ingegneristiche, eppure senza etichette di allocazione dei costi e dashboard visibili la spesa si accumula in un fondo comune di cui nessuno si sente responsabile finché la finanza non fa escalation. Decidete come attribuite il costo a team e servizi, chi lo rivede e se gli ingegneri vedono il costo accanto alle metriche di prestazione o ne sentono parlare solo una volta a trimestre. La tensione è tra responsabilità e attrito: spingete troppo sul costo e ogni decisione diventa una trattativa di budget, ignoratelo e carichi inattivi e sovradimensionati si compongono in silenzio. Portate i numeri: spesa attuale per team, quanta capacità resta inattiva o sovradimensionata e quanto in fretta un carico fuori controllo sarebbe notato. Per i budget aziendali e governativi, la spesa cloud non attribuita è sia un difetto di governance sia un vero rischio finanziario, quindi mettete in piedi una pratica FinOps che metta ingegneria, finanza e prodotto nella stessa conversazione anziché riconciliare a posteriori.

## Lente settoriale

**Startup.** Ricorri a un servizio di container gestito anziché a un cluster Kubernetes auto-ospitato: con un paio di servizi e nessun ingegnere di piattaforma, i piani di controllo sono una distrazione che non puoi permetterti. Impacchetta piccole immagini da una base minima, fissa le versioni, aggiungi una scansione di vulnerabilità alla build e spingi tutto lo stato in un database gestito così che le istanze restino usa e getta. Salta namespace, operator e portabilità multi-cloud finché non hai davvero i servizi e le persone che li giustificano.

**Piccola impresa.** Senza uno specialista di piattaforma dedicato e con un budget stretto, appoggiati con decisione ai servizi gestiti e lascia che il fornitore gestisca l'orchestrazione che altrimenti dovresti dotare di personale. Tratta le basi dei container come il tuo pavimento di sicurezza: immagini minime, versioni fissate e una scansione nella pipeline danno la maggior parte della protezione con poco sforzo. Privilegia comprare una piattaforma supportata anziché costruirne una e mantieni abbastanza portabilità, container standard e API aperte, da non restare intrappolato se prezzi o termini cambiano.

**Grande impresa.** Il compito è la governance di piattaforma tra molti team: un team centrale di piattaforma che fornisce immagini di base rinforzate, cancelli di firma e scansione, tenancy per namespace con quote, politica di rete e RBAC, più etichette di allocazione dei costi e una dashboard FinOps. Standardizza il contratto di distribuzione così che centinaia di servizi operino allo stesso modo e gestisci sicurezza, multi-tenancy e costo in modo centrale mentre i team si servono da soli per la distribuzione. Finanzia adeguatamente il team di piattaforma, perché una piattaforma con poche risorse diventa il collo di bottiglia che l'intera organizzazione aspetta.

**Ente pubblico.** Sovranità, residenza dei dati e responsabilità pubblica plasmano l'architettura. Esegui i carichi su container standard e Kubernetes così che le stesse pipeline girino in una regione sovrana e in un'enclave accreditata on-premises e codifica i confini di residenza e di accesso come politica anziché convenzione. Attingi le immagini da un registro interno rinforzato, applica una multi-tenancy rigida ai dati più sensibili e mantieni la portabilità che ti dà resilienza e leva negoziale, poiché le regole di appalto spesso vietano il lock-in su un singolo fornitore.

## Esempi

**Startup.** Una startup di sei persone impacchetta i suoi due servizi come piccole immagini di container costruite da una base minima e li esegue su un servizio di container gestito anziché su un cluster Kubernetes auto-ospitato, così nessuno deve accudire i piani di controllo. Fissano le versioni delle immagini di base e aggiungono una scansione di vulnerabilità alla build, ma saltano deliberatamente le funzioni di orchestrazione più pesanti finché non hanno davvero più di una manciata di servizi. Lo stato vive in un database Postgres gestito, il che mantiene i container usa e getta e permette alla piattaforma di riavviarli o scalarli senza alcuna perdita di dati.

**Grande impresa.** Un'azienda di telecomunicazioni gestisce diverse centinaia di [microservizi](https://en.wikipedia.org/wiki/Microservices) su cluster Kubernetes condivisi. Un team di piattaforma fornisce immagini di base rinforzate, fa rispettare la firma delle immagini e i cancelli di vulnerabilità e isola le unità di business in namespace con quote, politiche di rete e RBAC. Etichette di allocazione dei costi e una dashboard FinOps attribuiscono la spesa a ciascuna linea di prodotto e la scalatura automatica dimensiona la capacità sulla domanda. I team di prodotto distribuiscono decine di volte al giorno su una piattaforma coerente senza gestire server. L'azienda mantiene il controllo centrale su sicurezza e costo.

**Ente pubblico.** Un servizio sanitario nazionale deve mantenere i dati dei cittadini entro i confini nazionali e sotto il controllo legale nazionale. Esegue i propri carichi in una regione di cloud sovrano usando container standard e Kubernetes, così che le stesse pipeline e gli stessi manifest girino anche in un ambiente accreditato on-premises per i dati più sensibili. I confini di residenza dei dati e di accesso sono codificati come politica, le immagini sono attinte da un registro interno rinforzato e una multi-tenancy rigida isola i carichi sensibili. La portabilità tra la regione sovrana e l'enclave privata dà al servizio resilienza e leva negoziale senza sacrificare la conformità.

## Business case: motivazioni, ROI e TCO

Il ROI di container e orchestrazione viene da maggiore utilizzo delle risorse, distribuzioni più rapide e affidabili, scalatura elastica che adegua la spesa alla domanda e resilienza migliorata grazie all'auto-riparazione. Standardizzarsi su una piattaforma comune riduce lo sforzo duplicato tra i team e accelera l'inserimento, perché ogni servizio segue lo stesso contratto di distribuzione e di operazioni.

L'analisi del TCO deve essere onesta sull'onere operativo. I costi di adozione comprendono personale di platform engineering, formazione, strumenti di sicurezza per immagini e cluster e lo sforzo continuo di gestire la piattaforma stessa. Il costo del non adottare comprende distribuzione su misura incoerente tra i team, scarso utilizzo di infrastruttura costosa, scalatura manuale fragile e difficoltà a soddisfare requisiti di resilienza e sovranità. Per la leadership, il caso poggia sulla scala. Sotto un certo numero di servizi la complessità può non ripagare e un servizio gestito è più saggio. Ma a scala aziendale e governativa, una piattaforma cloud-native governata è di solito la base più economica e resiliente, a patto di finanziare il team di piattaforma perché la gestisca come si deve.

## Antipattern e insidie

- **Immagini grasse e non scansionate.** Immagini gonfie costruite da basi non fidate portano vulnerabilità inutili e rallentano tutto.
- **Kubernetes per tutto.** Adottare un orchestratore complesso per una manciata di servizi semplici compra complessità senza ritorno.
- **Ignorare i limiti di risorse.** Senza richieste e limiti, un carico può affamare o mandare in crash i vicini.
- **Tenancy morbida per carichi ostili.** Affidarsi ai soli namespace per isolare tenant che si diffidano è un incidente di sicurezza in attesa di accadere.
- **Container con stato per caso.** Memorizzare stato importante dentro container usa e getta porta a perdita di dati alla ripianificazione.
- **Cecità al costo.** Trattare la spesa cloud come spesa generale fissa anziché come esito ingegneristico porta a bollette fuori controllo.
- **Teatro della portabilità.** Rifiutare tutti i servizi gestiti per preservare una portabilità che l'organizzazione non userà mai davvero.

## Modello di maturità

**Livello 1: Avvio.** I container sono usati ad hoc, se lo sono. Le immagini sono costruite a mano e non scansionate, la distribuzione è manuale e reattiva e non c'è una piattaforma condivisa, né visibilità dei costi, né un modello di isolamento.

**Livello 2: Sviluppo.** I team containerizzano le applicazioni e adottano un orchestratore, ma le pratiche variano tra i gruppi. Scansione delle immagini, limiti di risorse e firma sono incoerenti e costo e multi-tenancy non sono governati in modo sistematico.

**Livello 3: Standardizzazione.** Una piattaforma standardizzata è documentata e fatta rispettare nell'organizzazione: immagini di base rinforzate, cancelli di firma e scansione, tenancy per namespace con quote e politica di rete, RBAC e allocazione dei costi. Gli schemi cloud-native e twelve-factor sono la norma attesa anziché una scelta locale.

**Livello 4: Gestione.** La piattaforma è misurata e controllata rispetto a valori di riferimento. Segui utilizzo del cluster, quota di immagini in esecuzione costruite dalla base rinforzata, vulnerabilità critiche non corrette, frequenza di distribuzione e tasso di fallimento delle modifiche, tassi di evacuazione e strozzatura e costo per team e servizio rispetto al budget. I cancelli sono fatti rispettare su questa evidenza: limiti di risorse mancanti e immagini non firmate sono respinti automaticamente e la deriva dallo standard innesca azione anziché un avviso.

**Livello 5: Orchestrazione.** La piattaforma è self-service e auto-riparante, integrata nell'organizzazione e adattiva. Il FinOps dimensiona di continuo e recupera la capacità, un'architettura portabile sostiene i requisiti ibridi e sovrani e la piattaforma migliora di continuo dall'uso misurato, ritirando e sostituendo componenti man mano che si spostano carichi, costo e quadro di rischio.

## Spunti di discussione

- A quale scala adottare Kubernetes smette di essere complessità fine a sé stessa e comincia a ripagare?
- Dove sta il giusto confine tra multi-tenancy morbida e rigida per i vostri carichi?
- Quanto dovreste investire nella portabilità multi-cloud rispetto alla produttività dei servizi gestiti profondi?
- Come date agli ingegneri una vera responsabilità sui costi senza trasformare ogni decisione in una trattativa di budget?
- Qual è il vostro modello di governance per le immagini di base e chi mantiene il registro rinforzato?
- Come plasmano l'architettura della vostra piattaforma i requisiti di sovranità e residenza dei dati?

## Punti chiave

- I container standardizzano impacchettamento e runtime; l'orchestrazione standardizza le operazioni su larga scala.
- L'igiene delle immagini, cioè immagini minime, fissate, scansionate e firmate, è sicurezza fondamentale.
- Usa gli schemi nativi di Kubernetes e gli operator anziché costruire un'orchestrazione su misura.
- Scegli deliberatamente un modello di multi-tenancy in base a quanto i carichi si fidano l'uno dell'altro.
- Segui il twelve-factor ed estendilo per le realtà dei sistemi distribuiti come fallimento parziale e osservabilità.
- Tratta il costo come un esito ingegneristico e gestiscilo di continuo attraverso il FinOps.

## Riferimenti e letture di approfondimento

- Adam Wiggins, *The Twelve-Factor App* (metodologia).
- Brendan Burns, Joe Beda e Kelsey Hightower, *Kubernetes Up & Running*.
- Bilgin Ibryam e Roland Huß, *Kubernetes Patterns*.
- Cornelia Davis, *Cloud Native Patterns*.
- J.R. Storment e Mike Fuller, *Cloud FinOps*.
- Liz Rice, *Container Security*.
- Cloud Native Computing Foundation (CNCF), definizione e panorama del cloud-native.
