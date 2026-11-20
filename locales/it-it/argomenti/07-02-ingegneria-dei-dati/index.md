# 7.2 Ingegneria dei dati

## Panoramica e motivazioni

L'[ingegneria dei dati](https://en.wikipedia.org/wiki/Data_engineering) è la disciplina di costruire e gestire le pipeline e le piattaforme che spostano i dati da dove sono prodotti a dove creano valore. Copre l'acquisizione dai sistemi sorgente, la trasformazione in forme pulite e modellate, l'archiviazione in formati economici, l'orchestrazione dell'intero flusso e le pratiche di affidabilità che mantengono tutto attendibile. Se la strategia dei dati decide quali dati dovrebbero esistere e chi li possiede, l'ingegneria dei dati è l'impianto e il macchinario che li fa fluire.

Per i grandi team, questa disciplina è fondamentale. Analisi, [business intelligence](https://en.wikipedia.org/wiki/Business_intelligence), sperimentazione di prodotto, [apprendimento automatico](https://en.wikipedia.org/wiki/Machine_learning) e reportistica normativa stanno tutti a valle delle pipeline di dati. Quando quelle pipeline sono fragili, lente od opache, ogni funzione dipendente ne soffre. Le dashboard mostrano numeri stantii. I modelli si addestrano su feature corrotte. Gli auditor non riescono a ricostruire come una cifra sia stata prodotta. Alla scala di imprese ed enti pubblici, le pipeline elaborano miliardi di record da molti sistemi sorgente e un singolo fallimento silenzioso può spingere dati sbagliati dentro decisioni, pagamenti o statistiche pubbliche.

Il campo è cresciuto da script su misura e strumenti [ETL (extract, transform, load)](https://en.wikipedia.org/wiki/Extract,_transform,_load) monolitici fino al moderno data stack: componenti modulari, in gran parte guidati da SQL, per acquisizione, trasformazione, orchestrazione e archiviazione, collegati da formati aperti. Questa modularità è insieme un dono e una trappola. Ti permette di assemblare strumenti best-of-breed, ma senza disciplina ingegneristica produce una dispersione di job non documentati e non testati. Questo capitolo copre le pratiche che mantengono le pipeline idempotenti, testabili, osservabili e sostenibili nei costi su larga scala.

## Principi chiave

- Le pipeline sono software e meritano controllo di versione, test, revisione e CI/CD.
- Preferisci trasformazioni idempotenti e riproducibili che possano rieseguirsi in sicurezza.
- Rendi osservabili i flussi di dati: freschezza, volume, schema e qualità sono monitorati.
- Modella i dati deliberatamente per i loro consumatori anziché scaricare tabelle grezze.
- Scegli batch o streaming in base a reali esigenze di latenza, non alla novità.
- Ottimizza formato di archiviazione, partizionamento e costo di calcolo come questioni di prim'ordine.
- Separa acquisizione, trasformazione ed erogazione così che ciascuna possa evolvere in modo indipendente.
- Fallisci in modo rumoroso e presto; una pipeline rotta è più sicura di dati sbagliati in silenzio.

## Raccomandazioni

### Scegli ETL o ELT deliberatamente

L'ETL trasforma i dati prima di caricarli nella destinazione. L'[ELT (extract, load, transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform) carica prima i dati grezzi e li trasforma dentro un potente warehouse o lakehouse. Le moderne piattaforme cloud hanno fatto dell'ELT il predefinito, perché l'archiviazione costa poco e il calcolo è elastico e conservare i dati grezzi ti permette di rielaborare quando la logica cambia o compaiono bug. Preferisci l'ELT per i carichi di analisi: atterra dati grezzi immutabili, poi costruisci sopra trasformazioni a strati. Riserva la trasformazione prima del caricamento ai casi in cui privacy, costo o vincoli contrattuali richiedono di ripulire o filtrare i dati prima che atterrino.

### Progetta pipeline batch e streaming per le loro esigenze di latenza

La maggior parte dei bisogni di analisi è ben servita da pipeline batch pianificate, più semplici da ragionare, testare e rielaborare retroattivamente. Ricorri allo streaming solo quando il business ha davvero bisogno di dati a bassa latenza: rilevamento delle frodi, allarmi operativi, personalizzazione in tempo reale. Lo streaming aggiunge vera complessità attorno a ordinamento, semantica exactly-once, dati in ritardo e gestione dello stato. Dove ti servono entrambi, considera architetture che unifichino la logica batch e streaming anziché mantenere due basi di codice divergenti. Sii onesto sulle tue esigenze di latenza. Il "tempo reale" è spesso un desiderio non esaminato che raddoppia il tuo costo.

### Orchestra con dipendenze esplicite

Usa un orchestratore per esprimere le pipeline come [grafi aciclici orientati (DAG)](https://en.wikipedia.org/wiki/Directed_acyclic_graph) di compiti con dipendenze esplicite, ripetizioni e pianificazione. Questo ti dà visibilità su che cosa è girato, che cosa è fallito e che cosa è bloccato, oltre alla capacità di rielaborare retroattivamente e rieseguire in modo deterministico. Basa le dipendenze sulla disponibilità dei dati, non solo sull'ora dell'orologio, così che i job a valle aspettino i dati a monte anziché partire a tentoni. Tieni la logica di orchestrazione nel controllo di versione e tratta le modifiche ai DAG come modifiche di codice.

### Modella i dati per il consumo

Le tabelle grezze raramente sono adatte agli analisti. Applica la [modellazione dimensionale](https://en.wikipedia.org/wiki/Dimensional_modeling), che dispone fatti e dimensioni conformi in [schemi a stella](https://en.wikipedia.org/wiki/Star_schema), dove ti serve un'analisi governata, riutilizzabile e self-service. Le tabelle larghe denormalizzate ("one big table") possono rendere di più per specifici schemi di query e sono più semplici per alcuni consumatori, al costo di duplicazione e flessibilità. Stratifica le tue trasformazioni: uno strato grezzo di staging, uno strato centrale ripulito e conforme e data mart rivolti ai consumatori. Questa separazione ti permette di correggere la logica in un solo posto e permette ai consumatori di dipendere da interfacce stabili.

### Rendi le pipeline idempotenti e testabili

Progetta le trasformazioni in modo che rieseguirle produca lo stesso risultato, anziché duplicare o corrompere i dati, per esempio usando upsert deterministici con chiave su identificativi di business e schemi di sovrascrittura delle partizioni. Scrivi test su più livelli: test unitari per la logica di trasformazione, test di schema e test sui dati che asseriscono aspettative come unicità, chiavi non nulle, integrità referenziale e intervalli di valori accettati. Eseguili nella CI, così una modifica sbagliata è colta prima di raggiungere i dati di produzione.

### Strumenta osservabilità e affidabilità

Monitora i quattro segnali fondamentali della salute dei dati: freschezza (è aggiornato), volume (il numero di righe è nell'intervallo atteso), schema (la struttura è cambiata in modo inatteso) e distribuzione (i valori sono derivati in modo anomalo). Dai l'allarme sulle violazioni e instradale al team responsabile. Tieni runbook, turni di reperibilità e postmortem senza colpe per gli incidenti sui dati, proprio come faresti per i servizi. Segui la tracciabilità, così che quando qualcosa si rompe tu possa vedere subito l'impatto a valle.

### Ottimizza archiviazione e costo

Usa formati aperti colonnari come Parquet, o formati di tabella aperti che supportano evoluzione dello schema, viaggio nel tempo e aggiornamenti efficienti. Partiziona i dati per le colonne su cui filtri di più, tipicamente la data, ed evita la proliferazione di file minuscoli compattando. Separa dati caldi e freddi con archiviazione a livelli e politiche di ciclo di vita. Monitora la spesa di calcolo per pipeline e per query. I costi fuori controllo di solito vengono da scansioni complete, partizioni mancanti e rielaborazioni illimitate. Tratta il costo come una metrica con responsabili, non una sorpresa sulla bolletta mensile.

## Compromessi: vantaggi e svantaggi

| Scelta | Vantaggi | Svantaggi | Adatto a |
|---|---|---|---|
| ELT (trasforma sul posto) | Conserva i dati grezzi, archiviazione economica, rielaborabile | Grande impronta di archiviazione, serve governance | Analisi in cloud |
| ETL (trasforma prima del caricamento) | Controlla il costo, filtra presto i dati sensibili | Perde il grezzo, più difficile rielaborare | Carichi regolamentati o vincolati |
| Batch | Semplice, testabile, facile rielaborazione retroattiva | Latenza più alta | La maggior parte delle analisi |
| Streaming | Bassa latenza, reazione in tempo reale | Complesso, costoso, difficile da testare | Frodi, allarmi operativi |
| Schema a stella | Governato, riutilizzabile, adatto al self-service | Sforzo di modellazione iniziale | BI condivisa |
| Tabella larga | Veloce per query note, semplice | Duplicazione, meno flessibile | Uso ristretto ad alte prestazioni |

Il compromesso dominante è semplicità contro latenza e flessibilità. Batch ed ELT con schemi a stella a strati ti danno un sistema testabile, rielaborabile e ben compreso che serve la maggior parte dei bisogni a costi accessibili. Streaming, tempo reale e progetti molto denormalizzati comprano velocità e prestazioni specifiche, ma a un prezzo ripido in complessità operativa e difficoltà di test. Adotta complessità solo dove un requisito di business concreto la ripaga e tieni il percorso semplice come predefinito.

## Domande da discutere con il tuo team

1. **Hai scelto deliberatamente l'ELT rispetto all'ETL e stai conservando dati grezzi immutabili così da poter rielaborare quando la logica cambia o emergono bug?** Il predefinito del capitolo è l'ELT: atterra i dati grezzi a basso costo, poi costruisci trasformazioni a strati, perché conservare il grezzo ti permette di rieseguire tutto quando una regola cambia o un bug compare settimane dopo. Cancellare i dati grezzi preclude quell'opzione ed è un'insidia comune e dolorosa. Il caso contrario a favore dell'ETL è reale nei carichi regolamentati o vincolati, dove privacy, costo o termini contrattuali richiedono filtraggio o mascheramento prima che i dati atterrino. Porta evidenza: quanto spesso hai avuto bisogno di rielaborare la storia e quanto è costato quando non potevi? Per una pipeline governativa o aziendale che deve tracciare qualsiasi cifra alla fonte, i record grezzi immutabili sono anche un requisito di verificabilità, quindi la risposta plasma sia la tua politica di archiviazione sia la tua difendibilità legale.

2. **Quali dei quattro segnali di salute dei dati monitori davvero, e chi viene chiamato quando uno si rompe?** Il capitolo nomina quattro segnali che vale la pena osservare: freschezza, volume, schema e distribuzione. Molti team non ne monitorano nessuno e vengono a sapere dei fallimenti da un dirigente che fissa una dashboard stantia, che è il peggior rilevatore possibile. Alla scala di imprese ed enti pubblici, un singolo fallimento silenzioso può spingere dati sbagliati dentro pagamenti, report o statistiche pubbliche, quindi il costo del rilevamento tardivo si misura in fiducia e denaro, non solo in rilavorazione. Porta il tuo vero tempo medio di rilevamento e il nome di chi oggi trova per primo gli incidenti. Se la risposta è "un consumatore", ti servono allarmi instradati al team responsabile più runbook e postmortem senza colpe, trattando gli incidenti sui dati esattamente come le interruzioni di servizio.

3. **I tuoi analisti consumano data mart modellati e testati, o scarichi loro addosso tabelle grezze chiamandolo self-service?** Il capitolo è diretto: le tabelle grezze raramente sono adatte agli analisti e stratificare le trasformazioni in uno strato grezzo di staging, un nucleo conforme e data mart rivolti ai consumatori ti permette di correggere la logica una volta e dare ai consumatori interfacce stabili. La spinta contraria è la velocità, poiché modellare con schemi a stella o tabelle larghe deliberate costa sforzo iniziale ed è allettante saltarlo. Ma scaricare dati grezzi sposta il costo di modellazione su ogni analista ripetutamente, producendo numeri divergenti e ore sprecate. Porta un segnale: quale quota del tempo degli analisti va a rimodellare dati grezzi e quanti team hanno ricostruito gli stessi join. Se il numero è alto, investi in uno strato centrale conforme così che i consumatori dipendano da interfacce testate e riutilizzabili anziché reinventarle.

4. **Dove il "tempo reale" si guadagna davvero il suo costo, e dove è un desiderio non esaminato che raddoppia in silenzio il tuo onere operativo?** Il predefinito del capitolo è il batch pianificato, più semplice da ragionare, testare e rielaborare retroattivamente, con lo streaming riservato ai casi in cui il business ha davvero bisogno di bassa latenza, come il rilevamento delle frodi o gli allarmi operativi. La spinta contraria è il prestigio e le vaghe richieste degli stakeholder di dati "in diretta", che suonano economiche in una riunione di pianificazione e diventano costose in produzione, perché lo streaming si trascina dietro ordinamento, semantica exactly-once, dati in ritardo e gestione dello stato, più una seconda base di codice da tenere allineata con la logica batch. Porta evidenza alla discussione: per ogni pipeline in streaming che gestisci o proponi, nomina la decisione che alimenta e la latenza che quella decisione tollera davvero, misurata in minuti o ore anziché in aggettivi. Per una grande piattaforma aziendale o governativa, aggiungi il costo di reperibilità e test di ogni percorso in tempo reale, perché una pipeline in streaming che nessuno sa testare né presidiare ventiquattr'ore su ventiquattro è una passività di affidabilità travestita da funzionalità e la risposta onesta spesso riconduce un requisito "in tempo reale" a un batch orario che serve la stessa decisione.

5. **Quali delle tue pipeline non potrebbero essere rieseguite in sicurezza oggi, e che cosa servirebbe per rendere idempotente ogni trasformazione?** Il capitolo insiste su trasformazioni idempotenti e riproducibili, che usano upsert deterministici con chiave su identificativi di business e schemi di sovrascrittura delle partizioni, così che una riesecuzione produca lo stesso risultato anziché duplicare o corrompere i dati. La pressione contraria è la velocità di consegna, poiché un job ingenuo di sola aggiunta si rilascia più in fretta di uno progettato per essere rieseguibile e il costo di quella scorciatoia resta nascosto finché un fallimento impone una riesecuzione parziale alle 2 di notte e qualcuno conta due volte i ricavi. Porta un inventario concreto: elenca i job che corromperebbero i dati se rieseguiti da un punto di fallimento e stima il raggio d'impatto del peggiore. Alla scala di imprese ed enti pubblici, dove un singolo fallimento silenzioso può spingere dati sbagliati dentro pagamenti, report o statistiche pubbliche, un'elaborazione non idempotente non è solo scomoda, mina la verificabilità che ti permette di rielaborare un periodo dopo un cambio di regola e tracciare comunque ogni cifra alla fonte, quindi finanziare il rifacimento per rendere sicure le riesecuzioni è una questione di controllo, non solo di ordine.

6. **Sai quanto costa gestire ogni pipeline, chi possiede quel numero e quanta parte della tua bolletta cloud viene da scansioni complete e partizioni mancanti?** Il capitolo tratta formato di archiviazione, partizionamento e spesa di calcolo come questioni di prim'ordine con responsabili, avvertendo che i costi fuori controllo di solito risalgono a scansioni complete, partizioni mancanti e rielaborazioni illimitate. La considerazione contraria è che il lavoro sui costi sembra meno urgente del rilasciare funzionalità, quindi è rimandato finché la bolletta mensile diventa una sorpresa e la finanza comincia a fare domande a cui l'ingegneria non sa rispondere. Porta evidenza: spesa per pipeline e per query, la quota di costo che viene da scansioni non partizionate e il numero di file minuscoli da compattare. Per una grande organizzazione che gestisce miliardi di record da molti sistemi sorgente, una bolletta cloud senza responsabile cresce senza che nessun team si senta responsabile e nei contesti governativi la spesa pubblica deve essere giustificata voce per voce, quindi attribuire il costo di calcolo a un responsabile nominato con una metrica seguita trasforma una spesa opaca in una gestita e spesso rivela risparmi abbastanza grandi da finanziare il successivo investimento in piattaforma.

## Lente settoriale

**Startup.** La velocità batte l'architettura. Collega l'acquisizione a un connettore gestito, costruisci una manciata di trasformazioni sotto controllo di versione e eseguile su un orchestratore leggero che ripete e rielabora da solo, anziché scrivere a mano job cron che si rompono in silenzio di notte. Mantieni ogni modello idempotente dal primo commit e aggiungi pochi test economici su chiavi nulle e conteggi di righe, così che una cattiva modifica alla sorgente fallisca nella CI anziché emergere nella dashboard del lunedì del fondatore. Non montare lo streaming né una piattaforma su misura: la tua risorsa più scarsa è l'attenzione ingegneristica.

**Piccola impresa.** Senza un ingegnere dei dati dedicato, privilegia comprare uno stack integrato anziché assemblarne uno. Un servizio ELT gestito più un warehouse cloud ti dà connettori, pianificazione e archiviazione senza un team di piattaforma che li mantenga. Imposta la scelta come igiene dei dati anziché come progetto di pipeline: sappi quali sistemi sorgente alimentano i tuoi report, conserva i dati grezzi così che un numero sbagliato possa essere tracciato e rielaborato e scegli strumenti i cui costi siano prevedibili così che una scansione di tabella completa non faccia saltare il budget mensile.

**Grande impresa.** Il problema è la coerenza tra molti team e miliardi di record da molti sistemi sorgente. Standardizza lo schema ELT, il modello a strati staging-core-mart e i quattro segnali di salute dei dati così che i gruppi smettano di reinventare pipeline fragili. Fai rispettare test sui dati e CI su ogni modello, attribuisci il costo di calcolo ai team responsabili e fai passare gli incidenti sui dati attraverso la stessa disciplina di reperibilità, runbook e postmortem senza colpe che usi per i servizi, così che un fallimento silenzioso non raggiunga mai una dashboard inosservato.

**Ente pubblico.** Regole di appalto, trasparenza e responsabilità pubblica plasmano la pipeline. Atterra record grezzi immutabili per la verificabilità, trasformali in fasi a strati e testate e mantieni la tracciabilità completa così che un auditor possa risalire da qualsiasi cifra pubblicata ai suoi documenti sorgente, spesso un requisito di legge. L'elaborazione idempotente ti permette di rielaborare in sicurezza una dichiarazione o un periodo di rendicontazione quando una regola cambia e privilegiare formati aperti e codice di trasformazione portabile ti evita di restare vincolato a un singolo fornitore lungo un contratto pluriennale.

## Esempi

**Startup.** Una startup di analisi di dieci persone aveva fatto crescere un groviglio di job cron che si rompevano in silenzio di notte e a volte contavano due volte le righe quando un ingegnere ne rieseguiva uno a mano. Il team è passato a un connettore gestito per l'acquisizione, a un framework di trasformazione per modelli sotto controllo di versione e a un orchestratore leggero che ripete e rielabora da solo. Hanno reso idempotente ogni modello e aggiunto una manciata di test su chiavi nulle e conteggi di righe, così che una cattiva modifica alla sorgente ora fallisce nella CI anziché emergere nella dashboard del lunedì del fondatore.

**Grande impresa.** Un rivenditore globale ha sostituito centinaia di script di estrazione scritti a mano con uno stack ELT. Connettori gestiti atterrano i dati sorgente grezzi, un framework di trasformazione costruisce modelli testati e sotto controllo di versione in un lakehouse e un orchestratore gestisce le dipendenze con ripetizioni e rielaborazioni. I test sui dati colgono la deriva dello schema dai sistemi sorgente prima che raggiunga le dashboard. L'archiviazione colonnare partizionata ha tagliato in modo sostanziale i costi delle query, migliorando al contempo la freschezza da giornaliera a oraria.

**Ente pubblico.** Un'amministrazione fiscale acquisisce dichiarazioni e dati di terze parti attraverso una pipeline governata che atterra record grezzi immutabili per la verificabilità, poi li trasforma in fasi a strati e testate. L'elaborazione idempotente permette loro di rielaborare in sicurezza un periodo di dichiarazione quando una regola cambia. La tracciabilità completa permette agli auditor di risalire da qualsiasi cifra calcolata ai documenti sorgente, un requisito di legge per la responsabilità pubblica.

## Business case: motivazioni, ROI e TCO

Il ROI di un'ingegneria dei dati disciplinata viene da affidabilità, velocità e controllo dei costi. Pipeline affidabili significano che decisioni e report poggiano su dati attendibili, così eviti la costosa rilavorazione e il danno reputazionale dei numeri sbagliati. Pipeline modulari e testate permettono ai team di rilasciare più in fretta nuovi prodotti di dati, componendo il valore di ogni investimento a valle in analisi e ML. Ottimizzare archiviazione e calcolo riduce direttamente la bolletta cloud, spesso in misura ampia una volta corretti partizionamento e schemi di query.

Il costo di adozione comprende strumenti di piattaforma, tempo di ingegneria per costruire pipeline modulari e testate e la disciplina di trattare i dati come software. Pesalo contro il costo del non adottare: job fragili su misura che solo il loro autore capisce, corruzione silenziosa dei dati scoperta dai dirigenti, spesa cloud che lievita per scansioni di tabelle complete e analisti bloccati in attesa dei dati. Alla leadership, presenta l'ingegneria dei dati come la fondazione che rende affidabili e sostenibili nei costi analisi, BI e IA. Se investi troppo poco qui, limiti il ritorno di ogni iniziativa sui dati sopra di essa.

## Antipattern e insidie

- Pipeline costruite come script una tantum senza controllo di versione, test né revisione.
- Job non idempotenti che duplicano o corrompono i dati quando rieseguiti dopo un fallimento.
- Adottare lo streaming per prestigio quando il batch avrebbe soddisfatto il requisito di latenza.
- Scaricare tabelle grezze sugli analisti e chiamarlo self-service.
- Nessuna osservabilità, così i fallimenti sono scoperti dai consumatori a valle.
- Ignorare partizionamento e dimensione dei file finché la bolletta cloud esplode.
- Accoppiare acquisizione, trasformazione ed erogazione così che nulla possa cambiare in sicurezza.
- Cancellare i dati grezzi, rendendo impossibile rielaborare quando la logica cambia.

## Modello di maturità

1. Avvio: Script ad hoc ed esecuzioni manuali, senza test né monitoraggio. I fallimenti sono scoperti dai consumatori a valle, i job non sono rieseguibili in sicurezza e i costi cloud non sono gestiti né attribuiti.
2. Sviluppo: Alcuni team hanno adottato un orchestratore e messo le trasformazioni di base sotto controllo di versione, ma la pratica è incoerente nell'organizzazione. Esistono test occasionali, l'idempotenza è a macchia di leopardo e le pipeline rotte significano ancora fronteggiare emergenze in modo reattivo.
3. Standardizzazione: L'ELT con un modello a strati staging-core-mart, testato e sotto controllo di versione, è lo standard documentato applicato tra i team. Dipendenze orchestrate con ripetizioni e rielaborazioni, test sui dati eseguiti nella CI e convenzioni condivise per modellazione a schema a stella e partizionamento sono fatti rispettare in tutta l'organizzazione anziché lasciati a ciascun gruppo.
4. Gestione: La piattaforma è misurata e controllata. Freschezza, volume, schema e distribuzione sono monitorati con allarmi instradati ai team responsabili e SLA delle pipeline, tempo medio di rilevamento, tassi di superamento della qualità dei dati e costo di calcolo per pipeline e per query sono seguiti rispetto a valori di riferimento. Soglie di ripristino e di chiusura sono fatte rispettare sull'evidenza e costo e affidabilità hanno responsabili nominati tenuti a obiettivi.
5. Orchestrazione: Le pipeline sono trattate pienamente come software con CI/CD, contratti sui dati e rilevamento automatico delle anomalie che coglie la deriva prima dei consumatori. La logica batch e streaming è unificata dove la latenza paga davvero, la piattaforma è continuamente migliorata e self-service e capacità, livelli di archiviazione e costo sono riequilibrati in modo adattivo al mutare dei carichi, così che nuovi prodotti di dati siano rilasciati rapidamente su una base stabile.

## Spunti di discussione

- Dove nel vostro stack il "tempo reale" si guadagna davvero il costo, e dove è un desiderio?
- Quali pipeline non potrebbero essere rieseguite in sicurezza oggi, e che cosa servirebbe per correggerlo?
- Quanta parte della vostra bolletta cloud dei dati viene da scansioni complete e partizioni mancanti?
- I vostri analisti consumano data mart modellati o tabelle grezze, e quanto questo costa loro?
- Qual è il vostro tempo medio di rilevamento di un incidente sui dati, e chi lo trova per primo?
- Unificare la logica batch e streaming ridurrebbe il vostro onere di manutenzione o aggiungerebbe rischio?

## Punti chiave

- Tratta le pipeline come software: controllo di versione, test, revisione, CI/CD e osservabilità.
- Preferisci l'ELT con modelli a strati e testati; conserva i dati grezzi per la rielaborazione.
- Scegli il batch per default e lo streaming solo dove la latenza paga davvero.
- Rendi idempotenti le trasformazioni così che le riesecuzioni siano sicure.
- Modella i dati per i consumatori con schemi a stella o tabelle larghe deliberate.
- Monitora freschezza, volume, schema e distribuzione e tratta gli incidenti sui dati come interruzioni.
- Ottimizza formati di archiviazione, partizionamento e costo di calcolo come questioni di prim'ordine.

## Riferimenti e letture di approfondimento

- Joe Reis e Matt Housley, "Fundamentals of Data Engineering."
- Ralph Kimball e Margy Ross, "The Data Warehouse Toolkit."
- Martin Kleppmann, "Designing Data-Intensive Applications."
- Bill Inmon, "Building the Data Warehouse."
- James Densmore, "Data Pipelines Pocket Reference."
- Nathan Marz e James Warren, "Big Data" (architettura Lambda).
- Barr Moses e colleghi, "Data Quality Fundamentals" (osservabilità dei dati).
