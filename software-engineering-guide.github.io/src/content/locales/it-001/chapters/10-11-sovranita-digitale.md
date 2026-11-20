# 10.11 Sovranità digitale

## Panoramica e motivazioni

La [sovranità digitale](https://en.wikipedia.org/wiki/Digital_sovereignty) è il grado in cui un'organizzazione, una nazione o un blocco mantiene un controllo significativo sui propri dati, software e infrastruttura. Significa controllo su dove i dati risiedono fisicamente, quali leggi e governi possono imporre l'accesso ad essi e se i sistemi critici possono continuare a funzionare senza dipendere da una potenza straniera o da un singolo fornitore. Ha diverse dimensioni: la **[sovranità dei dati](https://en.wikipedia.org/wiki/Data_sovereignty)** (la cui giurisdizione e leggi governano i dati), la **sovranità operativa** (la capacità di gestire e amministrare i sistemi senza il permesso o la presenza di una terza parte), la **sovranità del software** (accesso e controllo sul sorgente e sulla sua evoluzione) e la **sovranità della supply chain** (libertà da strozzature in hardware, servizi e dipendenze). Questo capitolo sta nella parte sulla gestione perché la sovranità è fondamentalmente una decisione di strategia, appalto e rischio (capitoli 10.1–10.3) con profonde conseguenze tecniche.

La motivazione è passata da teorica a urgente. Il [cloud computing](https://en.wikipedia.org/wiki/Cloud_computing) ha concentrato gran parte dell'infrastruttura mondiale in una manciata di fornitori, per lo più sotto la giurisdizione di un solo paese. Leggi extraterritoriali come il [CLOUD Act](https://en.wikipedia.org/wiki/CLOUD_Act) statunitense (che può obbligare un fornitore a divulgare dati a prescindere da dove siano conservati) si scontrano con regimi come il [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) dell'UE, una tensione cristallizzata dalla sentenza *[Schrems II](https://en.wikipedia.org/wiki/Schrems_II)* che ha invalidato il Privacy Shield UE-USA. Aggiungi shock geopolitici, sanzioni e il rischio che un fornitore sia tagliato fuori e la dipendenza diventa una vulnerabilità strategica, non solo una nota a piè di pagina della gestione dei fornitori. La sovranità è la disciplina di decidere, deliberatamente, quanta di quella dipendenza i tuoi sistemi e dati più critici possono portare in sicurezza.

Per impresa e soprattutto governo la posta è diretta. Le multinazionali devono riconciliare regimi di protezione dei dati in conflitto ed evitare un lock-in che un regolatore o un evento geopolitico potrebbe trasformare in una migrazione esistenziale. I governi detengono dati (cartelle sanitarie, fisco, difesa, identità dei cittadini) la cui esposizione a una giurisdizione straniera è una questione di sicurezza nazionale e di fiducia pubblica. Per questo sono emerse offerte di "cloud sovrano", iniziative come [Gaia-X](https://en.wikipedia.org/wiki/Gaia-X) dell'UE e certificazioni nazionali come SecNumCloud in Francia. L'obiettivo non è l'autarchia. È un controllo proporzionato alla sensibilità di ciò che è in gioco.

## Principi chiave

- **La sovranità è uno spettro, non un interruttore.** Adegua il grado di controllo alla sensibilità dei dati e del carico.
- **La località non è la giurisdizione.** I dati conservati localmente possono comunque essere raggiungibili legalmente da un governo straniero; la sola residenza non è sovranità.
- **Progetta per l'uscita.** La capacità di lasciare un fornitore è la misura più vera di sovranità.
- **[Standard aperti](https://en.wikipedia.org/wiki/Open_standard) e [open source](https://en.wikipedia.org/wiki/Open-source_software) riducono la dipendenza:** sono strumenti di autonomia strategica, non solo risparmi di costo.
- **Controlla le chiavi.** Chi detiene e controlla le chiavi di cifratura conta spesso più di dove stanno i byte.
- **Evita di scambiare un lock-in con un altro.** Un singolo fornitore "sovrano" può essere prigioniero quanto un hyperscaler.
- **Sii proporzionato.** La sovranità ha costi reali; ruotare troppo ovunque spreca denaro e rallenta la consegna.

## Raccomandazioni

### Classifica dati e carichi per sensibilità di sovranità

Non tutto ha bisogno della stessa protezione. Classifica dati e sistemi per la conseguenza dell'accesso da parte di una giurisdizione straniera o della perdita del fornitore. I carichi pubblici e a basso rischio possono stare su infrastruttura hyperscale globale per scala e costo. I dati molto sensibili (sicurezza nazionale, sanità, identità dei cittadini, registrazioni regolamentate) giustificano controlli di sovranità più forti. Questa suddivisione in livelli, la stessa logica basata sul rischio della classificazione dei dati del capitolo 4.5, è ciò che mantiene accessibile la sovranità, concentrando i controlli costosi dove sono giustificati anziché localizzare tutto.

### Comprendi la giurisdizione, non solo la residenza

La **residenza dei dati** (la posizione fisica o geografica in cui i dati sono conservati) è necessaria ma non sufficiente. Ciò che conta legalmente è la *giurisdizione*: quali governi possono imporre la divulgazione e ai sensi di quali leggi. Un insieme di dati tenuto in un data center in-country gestito da un fornitore con sede all'estero può comunque essere raggiungibile ai sensi della legge del paese d'origine di quel fornitore (il problema del CLOUD Act). Mappa l'esposizione legale di ogni sistema: sede del fornitore, leggi applicabili ed eventuali decisioni di adeguatezza o meccanismi di trasferimento (clausole contrattuali tipo, il Data Privacy Framework UE-USA). Poi tratta quella mappa legale come parte di prim'ordine dell'architettura (capitoli 4.5, 4.6).

### Progetta per portabilità e reversibilità

Il controllo di sovranità più durevole è un'uscita credibile. Preferisci standard aperti e formati portabili (capitolo 3.8). Containerizza i carichi così che possano spostarsi. Tieni l'infrastruttura come codice (capitolo 8.2) così che un ambiente possa essere ricostruito altrove. Evita una dipendenza profonda dai servizi proprietari di un singolo fornitore per i tuoi sistemi più critici. Mantieni e *testa* periodicamente un piano di uscita, un deposito di dati e configurazione più un percorso provato verso un'alternativa, così che "potremmo andarcene se dovessimo" sia un fatto dimostrato, non una speranza. È l'antidoto al **[lock-in sul fornitore](https://en.wikipedia.org/wiki/Vendor_lock-in)**, la condizione di non poter cambiare fornitore senza costo o disturbo proibitivi.

### Usa infrastruttura sovrana e controllo delle chiavi dove giustificato

Per il livello più sensibile esistono controlli tecnici più forti: offerte di **cloud sovrano** (regioni cloud gestite da, o in partnership con, entità in-giurisdizione, a volte certificate come SecNumCloud), **[confidential computing](https://en.wikipedia.org/wiki/Confidential_computing)** (esecuzione fidata basata su hardware che tiene i dati cifrati anche mentre sono elaborati) e chiavi di cifratura controllate dal cliente: **bring your own key (BYOK)** e, in modo più forte, **hold your own key (HYOK)**, in cui il fornitore non ha mai accesso alle chiavi che sbloccano i dati. Controllare le chiavi può dare gran parte del beneficio pratico della sovranità anche su infrastruttura condivisa. I dati che un fornitore non può decifrare sono dati che non può divulgare in modo significativo.

### Privilegia open source ed ecosistemi aperti per l'autonomia strategica

Il software open source e gli standard aperti sono tra le leve di sovranità più forti, perché rimuovono l'interruttore di spegnimento del singolo fornitore. Il sorgente può essere eseguito, verificato, biforcato e mantenuto indipendentemente da qualsiasi singolo fornitore (capitoli 10.3, 3.8). Le politiche del settore pubblico di "denaro pubblico, codice pubblico" e iniziative come Gaia-X riflettono questo. L'open source non è automaticamente sovrano. Richiede comunque persone competenti per gestirlo e supportarlo e la sua supply chain deve essere messa in sicurezza (capitolo 4.2). Ma converte la dipendenza da un fornitore in dipendenza da una comunità e dalla tua capacità, che è molto più facile da controllare.

### Governa la sovranità come rischio proporzionato, non come assoluto

Metti in piedi un quadro di rischio di sovranità accanto alla tua altra governance (capitoli 10.2, 1.5). Valuta il rischio di concentrazione e giurisdizionale delle piattaforme principali. Decidi livelli obiettivo di sovranità per livello di dati e pesali rispetto a costo, capacità e velocità di consegna. L'obiettivo è una posizione difendibile e documentata ("questi carichi accettano la dipendenza hyperscale; questi richiedono controllo in-giurisdizione; ecco la nostra postura di uscita"), rivista man mano che cambiano geopolitica e regolamentazione, non una posizione assoluta una tantum.

## Compromessi: vantaggi e svantaggi

| Approccio | Vantaggi | Svantaggi |
|---|---|---|
| **Cloud hyperscale globale** | Scala, funzionalità, basso costo, velocità | Esposizione giurisdizionale; rischio di concentrazione e lock-in |
| **Cloud sovrano / fornitore in-giurisdizione** | Controllo legale; adattamento alla sicurezza nazionale; fiducia | Costo più alto; meno funzionalità; spesso scala più piccola; nuovo lock-in |
| **Controllo delle chiavi (BYOK/HYOK) su infrastruttura condivisa** | Gran parte del beneficio a costo inferiore; mantiene la scala | Complessità operativa; rischio di gestione delle chiavi; non assoluto |
| **Open source / auto-ospitato** | Verificabilità, biforcabilità, nessun interruttore di spegnimento del fornitore | Richiede capacità interna; possiedi operazioni e sicurezza |
| **Mandati di localizzazione dei dati** | Conformità normativa; rassicurazione politica | Costosi; frammentano i dati; possono ridurre resilienza e utilità |

La tensione che definisce è **controllo contro capacità e costo**. La massima sovranità (auto-ospitata, in-giurisdizione, open source, pienamente portabile) sacrifica scala, funzionalità e velocità delle piattaforme globali. La massima capacità accetta dipendenza ed esposizione giurisdizionale. La soluzione è la suddivisione in livelli: paga per la sovranità dove la conseguenza la giustifica e accetta una dipendenza pragmatica dove non lo fa.

## Domande da discutere con il tuo team

1. **Abbiamo suddiviso in livelli i nostri dati e carichi per sensibilità di sovranità, così che i controlli costosi atterrino solo dove sono giustificati?** La sovranità è uno spettro, non un interruttore e localizzare tutto brucia denaro, rinuncia a capacità e può persino ridurre la resilienza restringendo le vostre opzioni. Classificate ogni sistema per la conseguenza dell'accesso da parte di una giurisdizione straniera o della perdita del fornitore: i carichi pubblici e a basso rischio possono stare su infrastruttura hyperscale globale, mentre dati di sicurezza nazionale, sanitari o di identità dei cittadini giustificano controlli più forti. È la stessa logica basata sul rischio della classificazione dei dati ed è ciò che mantiene accessibile la sovranità. Portate i vostri sistemi gioiello e il loro hosting attuale e chiedetevi se la protezione corrisponde alla sensibilità. Se state proteggendo tutto allo stesso modo, quasi certamente state pagando troppo da qualche parte ed essendo esposti da un'altra.

2. **Gli standard aperti e l'open source fanno parte della nostra strategia di sovranità, o li trattiamo solo come risparmi di costo?** Un sorgente che potete eseguire, verificare, biforcare e mantenere rimuove l'interruttore di spegnimento del singolo fornitore, che è una delle leve di autonomia più forti che avete. Standard aperti e formati portabili sono ciò che rende possibile un'uscita credibile e un'uscita credibile è la misura più vera di sovranità. La trappola più sottile è sfuggire a un hyperscaler solo per diventare del tutto prigionieri di un solo fornitore "sovrano" senza uscita: avete scambiato un lock-in con un altro. Portate le vostre piattaforme più critiche e chiedetevi quanto strettamente ciascuna è legata ai servizi proprietari di un solo fornitore. Dove la risposta è "molto", gli standard aperti e gli ambienti containerizzati e ricostruibili sono il modo più economico di allentare la presa.

3. **Chi possiede il nostro quadro di rischio di sovranità, e con che frequenza rivediamo la posizione man mano che cambiano legge e geopolitica?** Una posizione di sovranità fissata una volta e mai rivista diventa finzione nel momento in cui arriva una sentenza, una sanzione o una nuova legge e quegli shock ora arrivano regolarmente. Mettete in piedi un quadro vivo accanto alla vostra altra governance: valutate il rischio di concentrazione e giurisdizionale delle piattaforme principali, fissate livelli obiettivo di sovranità per livello di dati e documentate una posizione difendibile che potete mostrare a un regolatore. Nominate il responsabile e la cadenza di revisione. Portate la domanda di come una sanzione o una sentenza avversa contro il vostro fornitore principale colpirebbe i vostri servizi critici la settimana prossima; se nessuno sa rispondere, il quadro non esiste ancora.

4. **Chi detiene le chiavi di cifratura dei nostri dati più sensibili, e il nostro fornitore potrebbe essere costretto a consegnare quei dati in forma leggibile?** Residenza e persino una regione "sovrana" contano poco se l'operatore conserva le chiavi, perché un ordine di divulgazione raggiunge allora dati decifrati a prescindere da dove stiano i byte. Controllare voi stessi le chiavi, tramite bring your own key o il più forte hold your own key, in cui il fornitore non le vede mai, dà spesso la maggior parte del beneficio pratico della sovranità su infrastruttura condivisa a una frazione del costo di spostare tutto. La considerazione contraria è operativa: la gestione delle chiavi non perdona e una chiave persa o mal gestita può chiudervi fuori dai vostri stessi dati quanto qualsiasi sanzione. Portate un inventario di quali insiemi di dati sono cifrati, chi detiene davvero ciascuna chiave e qual è il vostro percorso di ripristino se una chiave è persa, poi mappatelo rispetto ai vostri livelli di sovranità. Per impresa e governo, trattate la custodia delle chiavi come la linea che decide se un ordine di divulgazione straniero restituisce testo cifrato o testo in chiaro e fatene un requisito di appalto anziché un adeguamento successivo.

5. **Potremmo davvero lasciare il nostro fornitore principale in un tempo che conta, e quando l'abbiamo provato l'ultima volta?** Un'uscita credibile è la misura più vera di sovranità, eppure la maggior parte dei piani di uscita vive sulla carta e non è mai stata eseguita, così la portabilità resta una speranza anziché un fatto dimostrato. La tensione è costo e focus: provare un'uscita, tenere i carichi containerizzati e custodire un deposito di dati e configurazione consumano tutti attenzione ingegneristica che la pressione di consegna preferirebbe spendere altrove. Portate il vostro sistema più critico, una stima onesta di quanto richiederebbe una migrazione forzata, l'elenco dei servizi proprietari da cui dipende e la data della vostra ultima vera prova (se c'è stata). Per un'organizzazione grande o pubblica che porta obblighi di uscita pluriennali nei contratti, un'uscita mai provata è un impegno che potreste essere legalmente incapaci di rispettare, quindi trattate una cadenza di prove come parte del costo di esercizio del sistema, non un esercizio opzionale.

6. **Per ogni sistema gioiello, sappiamo quali governi potrebbero legalmente imporre oggi l'accesso ad esso, a prescindere da dove i dati risiedono fisicamente?** La località non è la giurisdizione: i dati in un data center in-country possono comunque essere raggiungibili ai sensi della legge del paese d'origine di un operatore con sede all'estero e i team scambiano di routine la residenza per una protezione legale. La parte difficile è che la risposta richiede input legale e di appalto, non solo un diagramma di architettura e la mappa si sposta man mano che cambiano decisioni di adeguatezza, sentenze e meccanismi di trasferimento. Portate, per ogni insieme di dati critico, la sede del fornitore, le leggi che lo raggiungono e il meccanismo di trasferimento su cui contate e siate onesti dove nessuno lo sa davvero. Nei contesti regolamentati e pubblici, un'esposizione legale non mappata su dati di cittadini o di sicurezza nazionale è un rilievo in attesa di capitare al prossimo audit, quindi finanziate la mappatura legale con la stessa esplicitezza con cui finanziate l'infrastruttura.

## Lente settoriale

**Startup.** Velocità e autonomia dominano, quindi compra la sovranità come funzionalità sottile anziché costruire uno stack sovrano che non puoi dotare di personale. Se la giurisdizione di un cliente è il vincolo, distribuisci nell'opzione in-regione del tuo fornitore esistente, tieni le tue chiavi di cifratura così che l'operatore non possa decifrare i record sensibili e mantieni containerizzato il carico così che resti portabile. Questo chiude l'accordo a un costo da fase seed ed evita una riprogettazione per cui non hai autonomia.

**Piccola impresa.** Senza uno specialista di sovranità e con un budget stretto, tratta questo come una questione di revisione dei contratti e di scelta dei fornitori, non un programma ingegneristico. Privilegia fornitori che offrono per impostazione standard regioni in-giurisdizione, termini trasparenti di trattamento dei dati e chiavi detenute dal cliente e leggi le clausole su sub-responsabili e divulgazione prima di firmare. Auto-ospitare per la sovranità raramente ripaga qui: erediteresti l'onere di operazioni e sicurezza senza le persone per portarlo.

**Grande impresa.** Il compito è la governance di portafoglio tra molti team: una suddivisione condivisa in livelli dei dati per sensibilità di sovranità, una vista del rischio di concentrazione di quanto carico critico sta su un fornitore o una giurisdizione e controllo delle chiavi, portabilità e prove di uscita standardizzati così che ogni gruppo smetta di fare la propria scommessa scoordinata. Metti a bilancio esplicitamente il costo più alto e l'onere operativo del livello sensibile e tieni una posizione documentata e verificabile che puoi mostrare a un regolatore. Gestisci la sovranità come un rischio vivo con metriche e cadenza di revisione, non una migrazione una tantum.

**Ente pubblico.** Regole di appalto, trasparenza e responsabilità pubblica plasmano ogni scelta. Privilegia l'infrastruttura sovrana certificata (per esempio una qualificazione in stile SecNumCloud) e standard aperti e open source così che la piattaforma possa essere mantenuta indipendentemente da qualsiasi singolo fornitore e richiedi portabilità e dichiarazione dell'esposizione legale nel contratto stesso. Pubblica una descrizione in linguaggio semplice di dove stanno i dati dei cittadini e chi può raggiungerli, riserva i costosi controlli sovrani al livello davvero sensibile e tieni i servizi pubblici meno sensibili su un'infrastruttura globale più economica.

## Esempi

**Startup.** Una piccola startup di sanità digitale ottiene il suo primo cliente ospedaliero in Germania, che richiede che i dati dei pazienti restino sotto giurisdizione UE. Anziché costruire in modo eccessivo uno stack sovrano che non può permettersi, i fondatori distribuiscono nella regione UE del loro fornitore cloud esistente, tengono le proprie chiavi di cifratura così che il fornitore non possa decifrare i record sensibili e mantengono containerizzato il carico così che resti portabile. Questo compra la maggior parte del beneficio di sovranità che il cliente richiede a un costo che un team da fase seed può sostenere e chiude l'accordo senza una riprogettazione generale.

**Grande impresa.** Una banca multinazionale deve tenere certi dati dei clienti entro l'UE e oltre la portata della legge di divulgazione straniera. Anziché abbandonare il proprio fornitore cloud globale, suddivide in livelli il patrimonio. I carichi generali restano su regioni hyperscale per scala. I dati dei clienti regolamentati girano in regioni UE con cifratura **hold your own key** (il fornitore non può decifrarli) e un piano di uscita testato verso un fornitore alternativo. Questo soddisfa i regolatori e la propensione al rischio di concentrazione della banca stessa (capitolo 10.2) senza una migrazione generale che distrugga capacità.

**Ente pubblico.** Un servizio sanitario nazionale detiene le cartelle cliniche dei cittadini e giudica inaccettabile l'esposizione a una giurisdizione straniera. Appalta un cloud sovrano, cioè infrastruttura gestita da un'entità in-country sotto certificazione nazionale (per esempio in stile SecNumCloud), con confidential computing per l'elaborazione più sensibile e impone standard aperti (capitolo 3.8) e componenti open source così che la piattaforma possa essere mantenuta indipendentemente da qualsiasi singolo fornitore. Il costo più alto e l'insieme più ristretto di funzionalità sono accettati come prezzo del controllo di sicurezza nazionale e della fiducia pubblica. Nel frattempo, i servizi meno sensibili (un portale di informazione pubblica) restano su un'infrastruttura globale più economica.

## Business case: motivazioni, ROI e TCO

L'economia della sovranità digitale è asimmetrica e si imposta meglio come assicurazione contro eventi a bassa probabilità e alto impatto. I costi sono visibili e ricorrenti: l'infrastruttura sovrana e in-giurisdizione è tipicamente più costosa, offre meno servizi gestiti e richiede più capacità operativa interna, tutto ciò alza il costo totale di proprietà e può rallentare la consegna. I benefici sono per lo più catastrofi evitate: sanzioni normative e riprogettazione forzata dopo una sentenza come *Schrems II*, una perdita di accesso che pone fine all'attività se un fornitore è sanzionato o tagliato fuori o il danno reputazionale e di sicurezza nazionale della divulgazione straniera di dati sensibili. Poiché quei rischi di coda sono gravi e sempre più plausibili, un investimento proporzionato in sovranità, specialmente in controlli economici ma potenti come proprietà delle chiavi, portabilità e standard aperti, ha spesso un valore atteso fortemente positivo, anche se sembra pura spesa su un foglio di calcolo a regime.

La trappola su entrambi i lati è la sproporzione. *Investire troppo poco* lascia dati e sistemi critici esposti a una singola giurisdizione o fornitore senza uscita, trasformando un rischio gestibile in uno esistenziale. *Investire troppo*, localizzando tutto e rifiutando ogni piattaforma globale, brucia denaro, rinuncia a capacità e può *ridurre* la resilienza restringendo le tue opzioni. Per presentare il caso alla leadership, lega la spesa per la sovranità a una suddivisione in livelli del rischio di dati e carichi. Quantifica l'esposizione di concentrazione e giurisdizionale dei sistemi gioiello. Prezza i controlli economici (chiavi, portabilità, prove di uscita) che ne riducono il rischio. Riserva l'infrastruttura sovrana costosa al livello che la merita davvero.

## Antipattern e insidie

- **Teatro della sovranità:** pubblicizzare la residenza dei dati in-country mentre un fornitore con sede all'estero conserva l'accesso legale ai dati.
- **Confondere cifratura e sovranità:** cifrare i dati ma lasciare che il fornitore detenga le chiavi, così che possa comunque essere costretto a decifrare.
- **Rotazione eccessiva:** localizzare e auto-ospitare tutto a costo rovinoso e capacità ridotta, a prescindere dalla sensibilità.
- **Nuovo lock-in unico:** sfuggire a un hyperscaler diventando del tutto prigionieri di un solo fornitore "sovrano" senza uscita.
- **Nessuna uscita testata:** un piano di uscita che esiste sulla carta ma non è mai stato provato, così la portabilità non è dimostrata.
- **Ignorare la supply chain umana:** presumere che open source o auto-ospitare conferisca sovranità senza le persone competenti per gestirlo.
- **Posizione statica:** fissare una posizione di sovranità una volta e non rivederla mai man mano che cambiano legge e geopolitica.

## Modello di maturità

- **Livello 1 (Avvio):** La sovranità non è considerata ed è reattiva; dati e sistemi critici stanno dove costa meno, senza mappa del rischio giurisdizionale o di concentrazione e senza responsabile.
- **Livello 2 (Sviluppo):** La residenza dei dati è affrontata per i dati regolamentati più ovvi in alcuni progetti, ma giurisdizione, controllo delle chiavi e uscita non sono considerati in modo sistematico; le pratiche variano da team a team e la dipendenza da singoli fornitori non è esaminata.
- **Livello 3 (Standardizzazione):** Dati e carichi sono suddivisi in livelli per sensibilità di sovranità sotto una politica documentata applicata in tutta l'organizzazione; la giurisdizione è mappata; controllo delle chiavi, portabilità e standard aperti sono richiesti sui livelli sensibili; i piani di uscita esistono e sono imposti anziché opzionali.
- **Livello 4 (Gestione):** La posizione è misurata e controllata rispetto a valori di riferimento: rischio di concentrazione (la quota di carichi critici su un singolo fornitore o giurisdizione), copertura della proprietà delle chiavi sui dati sensibili, completezza della mappatura delle giurisdizioni e tempi di uscita provati sono seguiti come metriche, riportati alla governance e fatti rispettare rispetto a soglie, così che una dipendenza che deriva inneschi azione sull'evidenza anziché dopo uno shock.
- **Livello 5 (Orchestrazione):** La sovranità è continuamente migliorata e integrata nell'organizzazione: il quadro di rischio vivo alimenta per impostazione predefinita architettura, appalti e pianificazione del rischio, le uscite sono provate di routine e l'organizzazione ridefinisce in modo adattivo i livelli, riequilibra i fornitori e rivede la propria posizione man mano che si spostano sentenze, sanzioni e regolamentazione.

## Spunti di discussione

1. Per il vostro insieme di dati più sensibile, quali governi potrebbero legalmente imporre l'accesso oggi, e lo sapete?
2. La vostra residenza dei dati è vera sovranità, o un fornitore con sede all'estero detiene ancora le chiavi e l'esposizione legale?
3. Potreste davvero lasciare il vostro fornitore cloud principale se doveste, e l'avete mai testato?
4. Quali dei vostri carichi hanno davvero bisogno di infrastruttura sovrana, e quali state proteggendo troppo a costo inutile?
5. Dove controllare le vostre chiavi di cifratura vi darebbe la maggior parte del beneficio di sovranità a una frazione del costo?
6. Come una sanzione, un'interruzione o una sentenza contro il vostro fornitore principale inciderebbe sui vostri servizi critici la settimana prossima?

## Punti chiave

- La sovranità digitale è controllo proporzionato su dati, software e infrastruttura, lungo le dimensioni di dati, operativa, di software e di supply chain.
- **La località non è la giurisdizione:** la sola residenza non impedisce l'accesso legale straniero; mappa chi può imporre la divulgazione.
- **Progetta per l'uscita** e **controlla le tue chiavi:** portabilità e proprietà delle chiavi sono i controlli a più alta leva e a più basso costo.
- **Standard aperti e open source** sono strumenti di autonomia strategica; riserva il costoso **cloud sovrano** al livello che lo giustifica.
- Governa la sovranità come un **rischio proporzionato e vivo** (capitoli 10.2, 10.3, 4.5, 4.6, 3.8), evitando sia la sotto-protezione sia la rovinosa rotazione eccessiva.
- Il ROI è un'assicurazione contro gravi rischi di coda (normativi, geopolitici e di lock-in) prezzata rispetto a un costo reale e ricorrente.

## Riferimenti e letture di approfondimento

- Corte di giustizia dell'Unione europea, *Data Protection Commissioner v. Facebook Ireland and Maximillian Schrems* ("Schrems II", 2020).
- Regolamento (UE) 2016/679, *Regolamento generale sulla protezione dei dati (GDPR)*; Regolamento (UE) 2023/2854, *Data Act*.
- U.S. *Clarifying Lawful Overseas Use of Data (CLOUD) Act* (2018).
- ANSSI, quadro di qualificazione *SecNumCloud* (Francia).
- Gaia-X European Association for Data and Cloud (iniziativa Gaia-X).
- ENISA, rapporti sulla sicurezza del cloud e sulla certificazione di cybersicurezza dell'UE (EUCS).
- Julia Pohle e Thorsten Thiel, "Digital Sovereignty" (*Internet Policy Review*, 2020).
- Bert Hubert, scritti sull'autonomia digitale europea e sulla dipendenza dai fornitori stranieri.
- Kai Zenner e altri, analisi della politica di sovranità digitale dell'UE (per contesto; verificare le fonti attuali).
