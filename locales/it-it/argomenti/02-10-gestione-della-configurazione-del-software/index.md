# 2.10 Gestione della configurazione del software

## Panoramica e motivazioni

La [gestione della configurazione del software](https://en.wikipedia.org/wiki/Software_configuration_management) (SCM, software configuration management) è la disciplina di identificare i componenti di un sistema software, controllare come cambiano, registrare lo stato di ogni modifica e verificare che ciò che hai costruito e consegnato corrisponda a ciò che intendevi. Risponde a una domanda che sembra semplice ma diventa difficile su larga scala: che cosa c'è esattamente in questo rilascio, come ci è arrivato e chi l'ha approvato? [SWEBOK](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) tratta la SCM come un'area di conoscenza fondamentale per una ragione chiara: ogni altra attività ingegneristica ha bisogno di una configurazione stabile e nota rispetto a cui lavorare.

In un grande team, la SCM è il tessuto connettivo che mantiene coerenti migliaia di parti in movimento. Codice sorgente, librerie, immagini di container, definizioni dell'infrastruttura, dati di configurazione, documentazione e artefatti di test cambiano tutti con i propri tempi, e un sistema consegnato è una specifica combinazione di versioni specifiche di tutti loro. Senza una gestione deliberata della configurazione, quella combinazione è sconosciuta e non può essere riprodotta. Non puoi ricreare un rilascio passato, ricondurre un difetto alla modifica che l'ha causato né dire con sicurezza che cosa sta girando in produzione.

I contesti aziendali e governativi alzano la posta. I programmi regolamentati e del settore pubblico devono mostrare che le modifiche sono state autorizzate, riviste e registrate; che una build consegnata risale a requisiti e sorgenti approvati; e che nulla è entrato nel sistema senza controllo. Qui la SCM è tanto un sistema di evidenze quanto uno ingegneristico. Il [controllo di versione](https://en.wikipedia.org/wiki/Version_control) (capitolo 2.6) gestisce la storia dei sorgenti; la SCM governa l'intera configurazione e il processo controllato con cui cambia. È strettamente legata all'[infrastruttura come codice](https://en.wikipedia.org/wiki/Infrastructure_as_code) (capitolo 8.2), alle pipeline di consegna (capitolo 8.1) e ad audit e garanzia (capitolo 10.2).

## Principi chiave

- Tutto ciò che determina il comportamento del sistema è un [elemento di configurazione](https://en.wikipedia.org/wiki/Configuration_item) sotto controllo, non solo il codice sorgente.
- Una [baseline](https://en.wikipedia.org/wiki/Baseline_(configuration_management)) è un punto di riferimento noto e concordato; le modifiche si fanno rispetto alle baseline deliberatamente, non casualmente.
- Il cambiamento è controllato e registrato, non impedito; l'obiettivo è un cambiamento autorizzato e tracciabile.
- La contabilità di stato significa poter sempre rispondere a che cosa c'è in una configurazione e qual è la sua storia delle modifiche.
- Gli audit verificano che il sistema costruito e consegnato corrisponda alla configurazione registrata e ai requisiti approvati.
- La riproducibilità non è negoziabile: qualsiasi versione rilasciata deve poter essere ricostruita da input controllati.
- Automatizza identificazione, registrazione e verifica; la contabilità manuale non scala e non sopravvive a un audit.

## Raccomandazioni

### Definisci il processo SCM e assegna la responsabilità

Metti per iscritto un piano SCM che dica che cosa è sotto controllo di configurazione, come si identificano gli elementi, come le modifiche vengono proposte e approvate e come lo stato viene registrato e verificato. Assegna una responsabilità chiara, come un responsabile della configurazione o un team incaricato, così che la SCM non sia compito di tutti e quindi di nessuno. Adegua il processo al rischio: un piccolo strumento interno richiede un controllo leggero, mentre un sistema critico per la sicurezza o regolamentato richiede comitati e registri formali. Ancora il piano a uno standard riconosciuto come IEEE 828, così che auditor e partner possano seguirlo.

### Identifica gli elementi di configurazione e stabilisci le baseline

Elenca gli elementi di configurazione che determinano il comportamento del sistema: sorgenti, dipendenze, script di build, immagini di container, definizioni dell'infrastruttura, dati di configurazione, schemi e documenti chiave. Dai a ciascuno un identificatore stabile e uno schema di versionamento. Fissa baseline in punti significativi (una versione rilasciata, un insieme di requisiti approvato, una build certificata) così da avere un riferimento concordato rispetto a cui cambiare e a cui tornare. Una baseline è immutabile: una volta dichiarata, non la modifichi. La sostituisci solo con una nuova baseline creata attraverso il processo di modifica.

### Controlla il cambiamento con un processo definito e comitati adeguati

Instrada le modifiche agli elementi controllati attraverso un percorso definito: proposta, valutazione d'impatto, approvazione, implementazione e verifica. Per gli elementi a rischio più alto, usa un [comitato di controllo delle modifiche](https://en.wikipedia.org/wiki/Change_control_board) (CCB) che pesi costo, rischio e calendario prima di autorizzare una modifica. Dimensiona il comitato: un cancello automatico leggero per le modifiche di codice di routine e un CCB formale e interfunzionale per le modifiche che toccano baseline, interfacce o comportamento regolamentato. Registra ogni decisione e il ragionamento che sta dietro e collega le decisioni di configurazione importanti ai registri delle decisioni (capitolo 1.6) perché il ragionamento sopravviva.

### Mantieni la contabilità di stato della configurazione

Tieni un registro accurato e interrogabile di ogni elemento di configurazione: la sua versione attuale, a quale baseline appartiene e le richieste di modifica applicate. Questa contabilità di stato è ciò che ti permette di rispondere, in ogni momento, a che cosa contiene un rilascio e come ci è arrivato. Genera il registro automaticamente dai tuoi strumenti di riferimento (controllo di versione, pipeline, registro degli artefatti) anziché mantenere un foglio di calcolo parallelo che si allontana dalla realtà. Questo registro è la spina dorsale della tracciabilità dal requisito alla modifica alla build al rilascio in esercizio.

### Conduci audit di configurazione

Verifica due cose a intervalli regolari. Un audit funzionale di configurazione conferma che la configurazione si comporta come i suoi requisiti specificano. Un audit fisico di configurazione conferma che gli artefatti consegnati corrispondono alla configurazione registrata: che la build venga dai sorgenti e dalle dipendenze registrati e non contenga nulla di non contabilizzato. Automatizza il più possibile: [build riproducibili](https://en.wikipedia.org/wiki/Reproducible_builds), checksum degli artefatti, distinte base del software (SBOM) e attestazioni di provenienza trasformano l'audit da ispezione manuale a controllo continuo.

### Gestisci rilasci e consegna come eventi controllati

Tratta un rilascio come una specifica baseline identificata consegnata attraverso un processo ripetibile. Versiona esplicitamente i rilasci, produci un manifesto o una distinta base che descriva esattamente che cosa è incluso e registra la corrispondenza tra rilascio, revisione dei sorgenti e artefatto distribuito. Firma e calcola il checksum degli artefatti rilasciati così che chiunque a valle possa verificarne l'integrità. Collega la gestione dei rilasci alla pipeline di consegna (capitolo 8.1), così che la promozione attraverso gli ambienti sia essa stessa controllata, registrata e reversibile.

### Scegli e integra gli strumenti SCM

Appoggiati a strumenti che automatizzano identificazione, controllo, contabilità e audit anziché affidarti alla sola disciplina: controllo di versione per i sorgenti, registri di artefatti e immagini per i binari, una pipeline immutabile per le build, infrastruttura come codice per gli ambienti e strumenti di dipendenze e SBOM per la provenienza. Collegali così che una singola modifica fluisca in modo tracciabile dal commit al rilascio distribuito. Ciò che cerchi è una catena di strumenti in cui il registro della configurazione sia un sottoprodotto del lavoro, non una faccenda impiegatizia separata.

## Compromessi: vantaggi e svantaggi

| Scelta | Vantaggi | Svantaggi |
|---|---|---|
| Comitati formali di controllo delle modifiche | Forte autorizzazione e traccia di audit; rischio pesato prima del cambiamento | Throughput più lento; onere se applicati a modifiche di routine |
| Cancelli automatici leggeri | Flusso rapido; poco onere; scala a molte modifiche | Più deboli per baseline ad alto rischio; meno deliberazione |
| Baseline immutabili rigorose | Punti di riferimento riproducibili e verificabili | Servono disciplina e strumenti; attrito se usate troppo |
| Contabilità di stato automatica | Registro accurato e sempre aggiornato; pronto per l'audit | Investimento iniziale in strumenti e integrazione |
| Registri di configurazione manuali | Semplici da avviare; nessuno strumento necessario | Si allontanano dalla realtà; falliscono su larga scala e sotto audit |

Il compromesso centrale è tra controllo e flusso. Un controllo pesante delle modifiche dà forte garanzia ma rallenta la consegna. Un controllo leggero scorre veloce ma indebolisce la tracciabilità. La risposta non è sceglierne uno in assoluto; è graduare il controllo per rischio: automatizza le modifiche di routine attraverso cancelli rapidi e riserva comitati formali e baseline immutabili agli elementi per cui autorizzazione e verificabilità contano davvero. Il secondo compromesso è tra investimento iniziale in strumenti e costo impiegatizio continuo e rischio di audit. La contabilità automatica costa di più da impostare e molto meno da gestire.

## Domande da discutere con il tuo team

1. **Che cosa appartiene esattamente all'elenco degli elementi di configurazione, e chi possiede la decisione quando compare qualcosa di nuovo?** La SCM funziona solo se l'elenco degli elementi controllati corrisponde all'insieme delle cose che determinano davvero il comportamento, e in un sistema grande quell'insieme è più ampio di quanto la maggior parte dei team pensi: sorgenti, dipendenze, script di build, immagini di container, definizioni dell'infrastruttura, schemi, feature flag e i dati di configurazione che cambiano in silenzio ciò che il software fa. Se nessuno possiede l'elenco, diventa obsoleto, e l'elemento che ti ha fermato in produzione si rivela essere l'unica cosa a cui nessuno aveva pensato di dare controllo. Porta alla riunione il tuo inventario attuale e cerca elementi che determinano il comportamento e mancano. Assegna un responsabile (un responsabile della configurazione o un team nominato) così che aggiungere un nuovo elemento sia una decisione deliberata, non un incidente, perché la SCM che è compito di tutti non è compito di nessuno.

2. **Possiamo provare che un artefatto distribuito viene dai sorgenti e dalla pipeline che pensiamo, e quella prova sopravvivrebbe a una manomissione?** Riproducibilità e tracciabilità sono lo scopo stesso della SCM, e la versione acuta della domanda è se puoi ricondurre il binario in esecuzione a uno specifico commit e a un'esecuzione di build con evidenze, non asserzioni. In un sistema regolamentato o di alto valore questa è anche la tua difesa della supply chain: attestazioni di provenienza firmate, checksum degli artefatti e una distinta base del software trasformano "siamo abbastanza sicuri" in qualcosa che un auditor o chi risponde a un incidente può verificare. Porta il tuo ultimo rilascio e prova a ripercorrerlo all'indietro dall'artefatto distribuito alla modifica approvata. Se qualsiasi passaggio è un'affermazione manuale anziché un collegamento registrato e verificabile, è lì che un attaccante o un errore in buona fede possono infilare qualcosa senza essere notati, e chiuderlo significa integrare firma e provenienza nella pipeline così che la traccia sia un sottoprodotto della consegna.

3. **Qualcuno può oggi modificare un rilascio sul posto, e che cosa farebbe questo alla nostra capacità di fidarci di esso?** Una baseline è utile solo se è immutabile: nel momento in cui "il rilascio" può essere modificato a cose fatte, non puoi più riprodurlo né fare affidamento su di esso come riferimento, e ogni audit successivo diventa archeologia. Il fallimento classico è una configurazione modificata direttamente in produzione o un tag spostato in silenzio, ed è esattamente la scorciatoia che sembra innocua e rende impossibile ricostruire un rilascio più tardi. Porta alla riunione la risposta onesta: chi ha l'accesso per cambiare una baseline distribuita senza passare dal processo di modifica, ed è mai successo? La soluzione è rendere le baseline davvero immutabili e instradare ogni modifica attraverso proposta, valutazione d'impatto, approvazione e verifica, graduando il rigore così che le modifiche di routine fluiscano attraverso cancelli automatici veloci mentre le modifiche a baseline e regolamentate vadano a un comitato.

4. **La nostra contabilità di stato della configurazione è generata automaticamente dai nostri strumenti di riferimento, o mantenuta a mano, e quanto si è allontanata da ciò che è davvero distribuito?** La contabilità di stato è il registro che ti permette di rispondere, in ogni momento, a che cosa contiene un rilascio e come ci è arrivato, e in un sistema grande quel registro è affidabile solo se scaturisce dal lavoro anziché essere digitato in un foglio di calcolo parallelo. La spinta contraria è che un registro tenuto a mano sembra economico da avviare e flessibile, mentre automatizzarlo significa integrare controllo di versione, pipeline e registro degli artefatti così che il registro diventi un sottoprodotto della consegna. Porta il registro su cui oggi fai affidamento, scegli a caso tre rilasci recenti e verifica se versioni, baseline e richieste di modifica applicate registrate corrispondono a ciò che gli strumenti dicono sia stato rilasciato. Per un programma aziendale o governativo, un registro di stato che diverge dalla realtà non è un problema di ordine, è un rilievo di audit in attesa di accadere, perché un auditor che coglie una lacuna smette di fidarsi dell'intero resoconto e ti chiede di ricostruirlo a mano.

5. **Il nostro controllo delle modifiche è graduato per rischio, o lo stesso livello di cerimonia governa ogni modifica a prescindere da ciò che tocca?** Controllo e flusso tirano in direzioni opposte: un comitato formale di controllo delle modifiche pesa costo, rischio e calendario prima di autorizzare una modifica, ma applicare quella cerimonia a un ritocco di codice di routine aggiunge solo ritardo, mentre far passare una baseline condivisa o un flusso di pagamenti regolamentato attraverso un cancello automatico veloce elimina la deliberazione proprio dove serve. I modi di fallire sono simmetrici: una pesantezza uniforme che le persone imparano ad aggirare, o una lassità uniforme che lascia passare senza esame una modifica ad alto rischio. Porta un campione delle modifiche dell'ultimo trimestre ordinate per ciò che ciascuna toccava e verifica se il rigore che ha ricevuto corrispondesse davvero al suo rischio. In un contesto regolamentato o pubblico, indica quali classi di elementi devono raggiungere un comitato interfunzionale e quali possono fluire attraverso cancelli automatici e registra esplicitamente quella graduazione, perché "usiamo il giudizio" non è un controllo che un auditor o un organo di vigilanza possa verificare.

6. **Quando abbiamo condotto l'ultimo audit funzionale e fisico di configurazione, e quanta parte dell'evidenza sarebbe un registro vivo anziché una ricostruzione?** Un audit funzionale di configurazione conferma che il sistema si comporta come i suoi requisiti specificano, e un audit fisico di configurazione conferma che gli artefatti consegnati corrispondono alla configurazione registrata e non contengono nulla di non contabilizzato; se li salti, ti fidi del fatto che le tue baseline e la tua contabilità di stato siano oneste senza mai controllare. La tensione è il costo: gli audit manuali sono lenti e penosi, ed è esattamente per questo che i team li rinviano, e la via d'uscita è automatizzare i controlli con build riproducibili, checksum degli artefatti, distinte base del software e attestazioni di provenienza, così che la verifica diventi continua. Porta il tuo rilascio più recente e prova a produrre, sul momento, la traccia dal requisito alla modifica alla build al rilascio in esercizio e la prova dall'artefatto ai sorgenti. Per i programmi aziendali e governativi, questa traccia di evidenze è ciò che certificazione e vigilanza richiedono, quindi la domanda onesta è se l'audit di domani riceverebbe risposta da registri che già possiedi o da un esercizio di archeologia che non puoi permetterti.

## Lente settoriale

**Startup.** Mantieni la SCM leggera ma reale. Metti sorgenti, definizioni dell'infrastruttura e dati di configurazione nel controllo di versione e fai di ogni rilascio una build con tag prodotta da un'unica pipeline anziché un artefatto assemblato a mano. Salta i comitati di controllo delle modifiche e le baseline formali, eccessivi alla tua dimensione, ma non lasciare mai che qualcuno modifichi la configurazione direttamente in produzione, perché quell'unica scorciatoia è ciò che rende un rilascio impossibile da riprodurre quando un cliente incontra un bug martedì prossimo.

**Piccola impresa.** Senza un responsabile della configurazione e con un budget ridotto, appoggiati a strumenti che ti danno la SCM quasi gratis: una piattaforma di controllo di versione ospitata, la sua pipeline integrata e un registro di artefatti, così che il registro della configurazione sia un sottoprodotto anziché un lavoro da dotare di personale. Compra questa capacità incorporata in strumenti che già paghi anziché costruire un processo su misura. Spendi la tua scarsa attenzione sulle due abitudini che contano di più, rilasci con tag riproducibili e tenere le configurazioni che cambiano il comportamento fuori dalle modifiche manuali in produzione.

**Grande impresa.** Il problema è la coerenza tra molti team: un piano SCM condiviso, una tassonomia comune degli elementi di configurazione, un controllo delle modifiche graduato e una contabilità di stato generata automaticamente da controllo di versione, registro degli artefatti e pipeline. Riserva comitati formali di controllo delle modifiche e baseline immutabili alle piattaforme condivise e ai flussi regolamentati, lascia che le modifiche di routine fluiscano attraverso cancelli automatici e standardizza provenienza firmata e SBOM, così che il rilascio di qualsiasi team possa essere tracciato e qualsiasi auditor possa interrogare un registro vivo anziché commissionare una ricostruzione.

**Ente pubblico.** Regole sugli appalti, trasparenza e responsabilità pubblica plasmano il processo. Segui un piano SCM formale allineato a uno standard riconosciuto come IEEE 828, fissa baseline degli elementi di configurazione alle tappe contrattuali e instrada ogni modifica a una baseline controllata attraverso un comitato che registri impatto, decisione e motivazione. Richiedi che gli artefatti consegnati siano riproducibili da input controllati, con checksum e tracciabili da un capo all'altro dal requisito approvato alla build consegnata, perché quella traccia documentata di evidenze è esattamente ciò che certificazione, audit e vigilanza pubblica richiedono.

## Esempi

**Startup.** Una startup di sei persone mantiene la SCM leggera ma reale: sorgenti, definizioni dell'infrastruttura e dati di configurazione vivono tutti nel controllo di versione, e ogni rilascio è una build con tag e versione prodotta dalla stessa pipeline anziché assemblata a mano. Quando un cliente segnala un bug comparso martedì scorso, risalgono dall'artefatto distribuito all'esatto commit in pochi minuti anziché tirare a indovinare. Saltano comitati di controllo delle modifiche e baseline formali, che sarebbero eccessivi alla loro dimensione, ma si rifiutano di lasciare che qualcuno modifichi la configurazione direttamente in produzione, perché quell'unica scorciatoia è ciò che rende impossibile riprodurre un rilascio più tardi.

**Grande impresa.** Una grande società di servizi finanziari pone tutti gli artefatti distribuibili, le definizioni dell'infrastruttura e i dati di configurazione sotto controllo di configurazione. Ogni rilascio è una baseline immutabile e versionata con una distinta base del software generata, e ogni artefatto distribuito porta un'attestazione di provenienza firmata che lo collega a una specifica revisione dei sorgenti e a un'esecuzione della pipeline. Le modifiche di routine alle applicazioni fluiscono attraverso cancelli automatici della pipeline, mentre le modifiche alle baseline della piattaforma condivisa o ai flussi di pagamento regolamentati vanno a un comitato di controllo delle modifiche. La contabilità di stato è generata automaticamente da controllo di versione, registro degli artefatti e pipeline, così che gli auditor interroghino un registro vivo anziché chiedere una ricostruzione.

**Ente pubblico.** Un programma della difesa segue un piano SCM formale allineato a IEEE 828. Gli elementi di configurazione sono elencati e fissati in baseline alle tappe contrattuali, e un comitato di controllo delle modifiche autorizza ogni modifica a una baseline controllata, registrando impatto, decisione e motivazione. Gli audit funzionali di configurazione confermano che il sistema consegnato soddisfa i requisiti specificati, e gli audit fisici di configurazione confermano che gli artefatti consegnati corrispondono esattamente alla configurazione registrata. I rilasci sono riproducibili da input controllati, con checksum e tracciabili da un capo all'altro, dal requisito approvato alla richiesta di modifica alla build consegnata, che è esattamente la traccia di evidenze che certificazione e vigilanza richiedono.

## Business case: motivazioni, ROI e TCO

La SCM esiste per controllare rischio e costo nella vita di un sistema. Il ritorno viene da riproducibilità e tracciabilità: puoi ricreare qualsiasi rilascio, ricondurre i difetti alle modifiche che li hanno causati e rispondere alle domande di audit da registri anziché da archeologia. Questo riduce il tempo di diagnosi degli incidenti, la spesa e la durata degli audit e previene la classe costosa di fallimenti in cui nessuno sa dire che cosa stia girando né come ricostruirlo.

Il costo totale di proprietà favorisce l'automazione. I registri di configurazione manuali sono economici da avviare e costosi in modo costante da mantenere, e falliscono esattamente quando ne hai più bisogno, durante un incidente o un audit, perché si sono allontanati dalla realtà. Identificazione, contabilità e audit automatici costano di più all'inizio ma trasformano il registro della configurazione in un sottoprodotto quasi gratuito della pipeline di consegna. Per sostenere il caso con la leadership, presenta la SCM come il controllo che rende riproducibili i rilasci e verificabili le modifiche e pesala rispetto al costo di rilasci non riproducibili, audit prolungati e rischio di conformità di modifiche incontrollate.

## Antipattern e insidie

- **Configurazione per conoscenza tribale:** il vero contenuto di un rilascio vive solo nella testa di un ingegnere, non in alcun registro.
- **Baseline mutabili:** "il rilascio" viene modificato sul posto, così che non può più essere riprodotto né considerato un riferimento affidabile.
- **Dati di configurazione non controllati:** il codice è sotto controllo di versione ma la configurazione che ne cambia il comportamento viene modificata ad hoc in produzione.
- **Teatro del controllo delle modifiche:** un comitato che approva tutto in modo meccanico, aggiungendo ritardo senza aggiungere vero esame.
- **Contabilità di stato manuale:** un foglio di calcolo di versioni che diverge in silenzio da ciò che è davvero distribuito.
- **Build non riproducibili:** rilasci che non possono essere ricostruiti da input controllati, così che audit e ricostruzioni diventano congetture.
- **Rilasci non tracciabili:** nessuna corrispondenza dall'artefatto distribuito alla revisione dei sorgenti, alla richiesta di modifica e all'approvazione.

## Modello di maturità

- **Livello 1 (Avvio):** la SCM è ad hoc e reattiva. Solo i sorgenti sono controllati; i rilasci sono assemblati a mano; non ci sono baseline, né un registro affidabile di ciò che è distribuito, né modo di riprodurre una build passata.
- **Livello 2 (Sviluppo):** esistono pratiche di base ma variano da team a team. Alcuni sistemi definiscono elementi di configurazione e un processo di modifica e versionano i rilasci, esistono baseline qua e là, ma i registri sono in parte manuali e il rigore del controllo è incoerente nell'organizzazione.
- **Livello 3 (Standardizzazione):** le pratiche sono documentate e fatte rispettare in tutta l'organizzazione. Una tassonomia comune degli elementi di configurazione, baseline immutabili, controllo delle modifiche graduato e contabilità di stato sono stabiliti e in gran parte automatizzati; i rilasci sono riproducibili e tracciabili e gli audit sono sostenuti da strumenti anziché dalla memoria.
- **Livello 4 (Gestione):** la SCM è misurata e controllata con dati. Tasso di riproducibilità, copertura della tracciabilità dal requisito all'artefatto distribuito, tempo di attraversamento delle modifiche per ogni livello di controllo, incidenti di deriva della configurazione e rilievi di audit sono seguiti rispetto a valori di riferimento e obiettivi. Le deviazioni innescano correzioni e ogni decisione di procedere o meno poggia su queste prove anziché su asserzioni.
- **Livello 5 (Orchestrazione):** la SCM è migliorata di continuo e integrata in tutta l'organizzazione. Completamente automatizzata e verificata di continuo con build riproducibili, SBOM, attestazioni di provenienza e contabilità di stato viva, il processo è intrecciato con consegna, sicurezza e audit e si adatta al mutare di rischio ed esiti di consegna, ritirando e ridefinendo i controlli sulla base delle prove.

## Spunti di discussione

- Potete riprodurre oggi esattamente il vostro ultimo rilascio da input controllati, e quanto tempo ci vorrebbe?
- Quali elementi di configurazione determinano il comportamento ma non sono davvero sotto controllo, in particolare dati di configurazione e infrastruttura?
- Il vostro controllo delle modifiche è graduato per rischio, o aggiunge onere uniforme o lassità uniforme ovunque?
- Dove vive il vostro registro della configurazione, e quanto si è allontanato da ciò che è davvero distribuito?
- Quali evidenze potreste produrre in un audit domani, e quanta parte sarebbe ricostruzione anziché registro?
- Come cambiano build riproducibili, SBOM e provenienza ciò che i vostri audit possono verificare automaticamente?

## Punti chiave

- La SCM controlla l'intera configurazione (codice, dipendenze, infrastruttura e dati di configurazione), non solo i sorgenti.
- Le baseline sono punti di riferimento immutabili; il cambiamento è autorizzato e registrato rispetto a esse, non impedito.
- La contabilità di stato deve permetterti di rispondere, in ogni momento, a che cosa contiene un rilascio e come ci è arrivato.
- Gli audit verificano che ciò che è stato costruito e consegnato corrisponda alla configurazione registrata e ai requisiti approvati.
- Gradua il controllo per rischio e automatizza identificazione, contabilità e audit così che il registro sia un sottoprodotto della consegna.

## Riferimenti e letture di approfondimento

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, area di conoscenza Software Configuration Management
- IEEE Std 828, *Standard for Configuration Management in Systems and Software Engineering*
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (processo di gestione della configurazione)
- Jez Humble e David Farley, *Continuous Delivery*
- Bob Aiello e Leslie Sachs, *Configuration Management Best Practices: Practical Methods that Work in the Real World*
- Indicazioni NIST sulla sicurezza della supply chain del software, sulle distinte base del software (SBOM) e sulla provenienza degli artefatti
- CNCF e standard aperti per la provenienza e l'attestazione delle build (come quadri di riferimento)
