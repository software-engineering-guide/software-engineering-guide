# 8.2 Infrastruttura come codice e configurazione

## Panoramica e motivazioni

L'[infrastruttura come codice](https://en.wikipedia.org/wiki/Infrastructure_as_code) (IaC) significa definire e predisporre l'infrastruttura (reti, server, database, bilanciatori di carico, permessi) attraverso file di definizione leggibili dalla macchina anziché clic manuali sulla console o script ad hoc. La [gestione della configurazione](https://en.wikipedia.org/wiki/Configuration_management) estende la stessa idea alle impostazioni e allo stato dei sistemi una volta che esistono. Insieme trasformano l'infrastruttura da artefatto fatto a mano e fragile in un prodotto versionato, rivedibile e riproducibile della stessa disciplina ingegneristica che usi per il codice applicativo.

Per i grandi team, l'IaC non è una comodità ma una necessità. Quando centinaia di ingegneri hanno bisogno di ambienti e migliaia di risorse devono restare coerenti tra regioni e account, la predisposizione manuale non riesce a stare al passo e non riesce a restare corretta. L'infrastruttura configurata da esseri umani deriva, prima o poi, verso server "snowflake" unici che nessuno comprende del tutto e che non possono essere ricostruiti in modo affidabile dopo un guasto. Codificare l'infrastruttura la rende coerente, verificabile e usa e getta. Qualsiasi ambiente può essere ricreato dalla sua definizione e qualsiasi modifica è un diff rivedibile.

Le organizzazioni aziendali e governative ottengono un ulteriore beneficio decisivo: una governance applicabile. I requisiti di sicurezza e conformità, come la cifratura a riposo, la segmentazione di rete, le regioni approvate e le etichette per l'allocazione dei costi, possono essere incorporati direttamente nel codice e controllati automaticamente prima che qualcosa sia predisposto. Anziché verificare l'infrastruttura a posteriori e inseguire le violazioni, impedisci all'infrastruttura non conforme di esistere. Questo passaggio dal rilevamento alla prevenzione è la ragione fondamentale per cui l'IaC è diventata il fondamento della pratica moderna di piattaforma.

## Principi chiave

- Preferisci definizioni dichiarative che descrivono lo stato desiderato a script imperativi che descrivono i passi.
- Conserva tutte le definizioni dell'infrastruttura nel controllo di versione, riviste come qualsiasi altro codice.
- Tratta l'infrastruttura come immutabile: sostituisci anziché modificare sul posto.
- Rendi idempotente la predisposizione così che applicare ripetutamente la stessa definizione dia lo stesso risultato.
- Rileva e riconcilia di continuo la deriva, l'ambiente dal vivo che diverge dalla sua definizione dichiarata; il codice, non il sistema dal vivo, è la fonte di verità.
- Componi l'infrastruttura da moduli riutilizzabili e versionati anziché copiare e incollare.
- Codifica la politica come codice, regole organizzative espresse come codice verificabile dalla macchina, così che i guardrail siano automatici, non consultivi.
- Tieni i segreti fuori dalle definizioni; richiamali da un gestore di segreti dedicato.

## Raccomandazioni

### Scegli strumenti dichiarativi e strutturali attorno ai moduli

Adotta uno strumento IaC dichiarativo, come [Terraform](https://en.wikipedia.org/wiki/Terraform_(software)), Pulumi o un'opzione nativa del cloud come CloudFormation, e standardizzati su di esso in tutta l'organizzazione così da evitare un panorama frammentato di strumenti. La pratica architetturale chiave è la modularità: costruisci moduli piccoli, ben documentati e versionati che catturano schemi comuni (una rete conforme, un database rinforzato, un servizio standard). I team poi compongono gli ambienti da questi moduli anziché scrivere risorse grezze. Questo diffonde automaticamente buoni predefiniti e impostazioni di sicurezza e riduce drasticamente la duplicazione.

### Gestisci lo stato deliberatamente

Gli strumenti dichiarativi tengono traccia della corrispondenza tra codice e risorse reali in un file di stato. Conserva lo stato in remoto in un backend condiviso, cifrato e con accesso controllato e usa il blocco così che modifiche concorrenti non possano corromperlo. Non tenere mai lo stato su un portatile e non modificarlo mai a mano se non come azione di ripristino di ultima istanza. Lo stato è sensibile, perché può contenere metadati delle risorse e segreti, quindi proteggilo di conseguenza.

### Costruisci infrastruttura immutabile con immagini d'oro

Anziché applicare patch ai server in esecuzione, prepara un'"immagine d'oro" versionata (una macchina o un'immagine di container preconfigurata e rinforzata) e distribuisci da essa istanze fresche. Quando ti serve una modifica o una patch, costruisci una nuova immagine e rilasciala, ritirando le vecchie istanze. Questo elimina la deriva di configurazione, rende banale il rollback e mantiene ogni istanza identica e riconducibile a una build nota come buona. Le pipeline automatizzate di immagini dovrebbero includere rinforzo della sicurezza e scansione, così che la conformità sia incorporata a livello di immagine.

### Rileva e riconcilia la deriva di configurazione

La deriva avviene quando l'ambiente dal vivo diverge dalla sua definizione, di solito perché qualcuno ha fatto una modifica manuale d'emergenza. Esegui un rilevamento regolare della deriva che confronta lo stato reale con quello dichiarato e segnala le differenze. Tratta la deriva come un difetto: riconcilia aggiornando il codice e riapplicando, non lasciando al suo posto la modifica manuale. Per i sistemi che richiedono un'applicazione continua della configurazione, usa uno strumento di gestione della configurazione che fa convergere di continuo gli host verso il loro stato dichiarato.

### Adotta GitOps e la distribuzione basata su pull

Nel modello GitOps, un repository Git custodisce lo stato desiderato dichiarato del sistema e un agente automatico in esecuzione dentro l'ambiente di destinazione preleva di continuo quello stato e riconcilia il sistema dal vivo perché vi corrisponda. Questo rovescia il tradizionale modello push. Nessun sistema esterno ha bisogno di credenziali permanenti per modificare l'ambiente, perché è l'ambiente a prelevare la propria configurazione. GitOps ti dà una traccia di audit completa (ogni modifica è un commit), un rollback facile (annulla il commit) e una forte correzione della deriva (l'agente riafferma di continuo lo stato desiderato). È particolarmente potente per [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) e per le organizzazioni che vogliono un'unica fonte di verità rivedibile.

### Fai rispettare i guardrail con la politica come codice

Esprimi le regole organizzative, come regioni ammesse, cifratura obbligatoria, etichette richieste ed esposizione pubblica vietata, come politiche verificabili dalla macchina usando uno strumento come Open Policy Agent (OPA) o un motore di politiche nativo della piattaforma come Sentinel. Esegui questi controlli nella pipeline prima della predisposizione, così le violazioni sono bloccate automaticamente. La politica come codice trasforma l'intento di un team di sicurezza in un controllo eseguibile e applicato in modo uniforme e scala a migliaia di modifiche in un modo in cui la revisione manuale non potrebbe mai.

## Compromessi: vantaggi e svantaggi

| Scelta | Vantaggi | Svantaggi | Adatto a |
|---|---|---|---|
| IaC dichiarativa (Terraform/Pulumi) | Riproducibile, rivedibile, con deriva rilevabile | Curva di apprendimento; complessità della gestione dello stato | Quasi tutti i team su larga scala |
| Script imperativi | Familiari; flessibili per i casi una tantum | Non idempotenti; difficili da verificare e ripetere | Casi ristretti e transitori |
| Immutabile + immagini d'oro | Nessuna deriva; rollback banale | Onere della pipeline di build delle immagini | Flotte che richiedono coerenza |
| Gestione della configurazione mutabile | Controllo continuo a grana fine | Rischio di deriva; convergenza più lenta | Host preesistenti o di lunga vita |
| GitOps (basato su pull) | Forte traccia di audit; auto-riparante | Richiede un agente nel cluster e disciplina Git | Kubernetes e cloud-native |
| Politica come codice | Guardrail automatici e uniformi | Sforzo iniziale di stesura delle politiche | Ambienti regolamentati |

La tensione principale è tra flessibilità e controllo. Gli approcci manuali e imperativi sembrano più veloci per una singola modifica, ma accumulano un'incoerenza nascosta che diventa paralizzante su larga scala. Un'infrastruttura dichiarativa, immutabile e governata da politiche chiede più investimento iniziale e un vero cambiamento culturale, poiché gli ingegneri devono smettere di fare rapide modifiche in console, ma ripaga quell'investimento molte volte in affidabilità, verificabilità e capacità di ricostruire qualsiasi cosa su richiesta.

## Domande da discutere con il tuo team

1. **Chi possiede la libreria di moduli condivisa, e come arriva a ogni team che la usa un miglioramento di un modulo?** I moduli ripagano solo se correzioni e predefiniti rinforzati si propagano e questo richiede una chiara proprietà e un vero versionamento, non una cartella da cui tutti copiano. Decidete chi mantiene i moduli di rete conforme e di database rinforzato, come li versionate (versionamento semantico con un registro delle modifiche) e come i team ricevono gli aggiornamenti senza un'emergenza. Su larga scala è la differenza tra correggere una configurazione errata una volta e inseguirla su mille risorse modificate a mano. Portate evidenza: quante copie distinte dello stesso schema esistono oggi, quanto tempo impiega una correzione di sicurezza a raggiungere ogni ambiente e se i team fissano le versioni dei moduli o le lasciano fluttuare. Se una patch critica non può raggiungere l'intero patrimonio in giorni, la vostra modularità è cosmetica.

2. **Qual è la vostra cadenza di rilevamento della deriva, e che cosa succede davvero quando si trova una deriva?** La deriva è l'ambiente dal vivo che diverge in silenzio dal suo stato dichiarato, di solito per una modifica d'emergenza in console, e tollerarla trasforma il vostro codice in finzione. Decidete con che frequenza confrontate lo stato reale con quello dichiarato (ogni notte è un predefinito ragionevole) e, cosa più importante, decidete la risposta: riconciliare aggiornando il codice e riapplicando, mai lasciando al suo posto la modifica manuale. Nei contesti regolamentati questo è un requisito di controllo, perché gli auditor hanno bisogno che lo stato dichiarato corrisponda alla realtà in modo continuo. Portate i vostri numeri attuali: quante risorse derivano ogni settimana, quanto restano derivate e se qualcuno è responsabile di chiuderle. Trattate ogni deriva come un difetto con un responsabile, o la garanzia di fonte di verità si erode finché nessuno si fida del codice.

3. **Siete passati a GitOps e alla riconciliazione basata su pull, o un sistema esterno detiene ancora credenziali permanenti per modificare la produzione?** Nel modello pull un agente dentro l'ambiente di destinazione riconcilia di continuo il sistema dal vivo con Git, il che elimina la necessità che un sistema esterno detenga accesso in scrittura e riafferma lo stato desiderato così che la deriva si autocorregga. È una forte postura di sicurezza e di audit, poiché ogni modifica è un commit e nessun operatore ha bisogno di credenziali di produzione permanenti. Il costo è reale: un agente nel cluster da gestire e una rigorosa disciplina Git, quindi pesatelo contro la vostra attuale automazione basata su push. Portate l'elenco di chi e che cosa può oggi mutare direttamente la produzione e quale traccia di audit lasciano quelle modifiche. Per Kubernetes e le enclave ad alta garanzia questo passaggio di solito vale la pena; per una manciata di risorse statiche può essere eccessivo.

4. **Come è memorizzato, bloccato e protetto con controllo di accesso lo stato della vostra infrastruttura, e che cosa succede il giorno in cui è corrotto o perso?** Lo stato è la mappa tra il vostro codice e le risorse reali, quindi un file di stato perso o danneggiato può lasciare uno strumento cieco alle risorse che ha creato e tentare qualcuno a una riapplicazione distruttiva. Per un grande team il rischio si moltiplica, perché molti ingegneri che applicano contro uno stato condiviso hanno bisogno di un backend remoto, cifrato e bloccato così che le esecuzioni concorrenti non possano sovrascriversi. Pesate la comodità di un grande stato unico contro il raggio d'impatto che crea e considerate di dividere lo stato per ambiente o per dominio così che un singolo errore non possa far cadere tutto. Portate i fatti: dove vive oggi lo stato, se il blocco è fatto rispettare, chi può leggerlo (può contenere segreti) e se avete mai provato un ripristino. Nei contesti aziendali e governativi, trattate il backend dello stato come una risorsa sensibile e con accesso controllato, con proprio backup, registro di audit e runbook di ripristino, perché perderlo è perdere la vostra registrazione di ciò che esiste.

5. **Quando una vera emergenza richiede una modifica manuale, qual è il percorso di emergenza (break-glass) autorizzato e come viene riportata quella modifica nel codice?** Ogni pratica IaC matura incontra prima o poi l'incidente delle 3 di notte in cui aspettare una pipeline non è accettabile e la domanda onesta non è se le modifiche manuali avvengano mai ma come le contenete. Decidete in anticipo chi può aggirare la pipeline, che cosa può toccare, come l'azione è registrata e la scadenza entro cui la modifica deve essere riconciliata nel codice o annullata. Senza quell'accordo, l'eccezione d'emergenza diventa in silenzio l'abitudine di tutti i giorni e il ClickOps torna dalla porta di servizio. Portate evidenza: quante modifiche fuori banda sono avvenute nell'ultimo trimestre, quanto è rimasta non riconciliata ciascuna e se il rilevamento della deriva le ha davvero colte. Per gli enti regolamentati e pubblici, una procedura break-glass documentata con registrazione automatica è spesso un requisito di controllo, perché gli auditor si aspettano sia che le emergenze siano possibili sia che ognuna lasci una traccia e riporti il sistema al suo stato dichiarato.

6. **Quanta parte della vostra base di riferimento di sicurezza e conformità è espressa come politica che blocca automaticamente una cattiva modifica, rispetto a regole che vivono in un documento e contano sul fatto che qualcuno se le ricordi?** I guardrail scritti come prosa in un wiki sono violati di routine, perché dipendono dal fatto che ogni ingegnere li legga e li applichi sotto pressione di scadenza, mentre le stesse regole espresse come politica come codice respingono una modifica non conforme prima che sia mai predisposta. Per una grande organizzazione è l'unico modo in cui l'intento di un team di sicurezza scala a migliaia di modifiche senza diventare un collo di bottiglia di revisione. Pesate il costo iniziale di scrivere e mantenere le politiche contro il costo ricorrente di revisione manuale e rimedio a posteriori e decidete quali controlli (cifratura, regioni approvate, etichette obbligatorie, nessuna esposizione pubblica) siano abbastanza non negoziabili da far rispettare come cancelli rigidi. Portate l'elenco delle vostre regole di base attuali e segnate quali sono automatizzate e quali consultive, più quanto spesso ciascuna è violata nella pratica. Nei contesti aziendali e governativi, la politica automatica converte un audit da settimane di raccolta manuale di evidenze in una query contro controlli fatti rispettare e trasforma la conformità da rilevamento in prevenzione.

## Lente settoriale

**Startup.** Vince la velocità, quindi metti l'intero stack in un unico repository dichiarativo (Terraform è un predefinito comune), tieni lo stato in un backend gestito e cifrato e instrada ogni modifica attraverso una pull request anche con un team di tre. Salta l'apparato pesante di piattaforma: nessun team centrale di moduli, nessun motore di politiche per ora, solo controllo di versione e la disciplina di non cliccare mai in console. Questo da solo ti dà ambienti riproducibili che puoi smontare per risparmiare e ricostruire per la prossima dimostrazione.

**Piccola impresa.** Senza uno specialista di piattaforma dedicato, appoggiati ai servizi gestiti e a qualsiasi IaC che il tuo fornitore cloud o commerciale già supporta anziché montare strumenti su misura che non puoi mantenere. Privilegia comprare una piattaforma ospitata i cui predefiniti sensati (cifratura, backup, patch) sono gestiti per te rispetto a costruire una pipeline di immagini d'oro che non hai nessuno a gestire. Imposta l'obiettivo in modo ristretto: porta in codice la tua manciata di risorse critiche così da poterle ricostruire dopo un guasto o un collaboratore che se ne va.

**Grande impresa.** Il problema centrale è la coerenza tra molti team, account e regioni, quindi investi in una libreria di moduli condivisa e versionata, stato remoto e bloccato e politica come codice fatta rispettare nella pipeline. Un team centrale di piattaforma pubblica moduli e guardrail rinforzati mentre i team di prodotto si servono da soli al loro interno e il rilevamento della deriva gira di continuo così che migliaia di risorse restino in uno stato noto. Metti a bilancio il costo continuo di mantenere moduli e politiche, perché il loro valore viene da una correzione o da un predefinito rinforzato che si propaga ovunque in una volta.

**Ente pubblico.** Regole di appalto, accreditamento e responsabilità pubblica ti spingono verso infrastruttura immutabile, commit firmati e riconciliazione GitOps dentro un'enclave accreditata, così che nessun operatore detenga credenziali permanenti per modificare la produzione. Codifica la base di sicurezza richiesta nelle immagini d'oro e nella politica come codice e lascia che la cronologia dei commit serva da evidenza di audit a prova di manomissione e sempre disponibile. Privilegia strumenti aperti e portabili rispetto a formati proprietari che ti intrappolano e rendi esplicite la procedura break-glass e la sua registrazione così che le modifiche d'emergenza soddisfino comunque i requisiti di controllo della configurazione.

## Esempi

**Startup.** Una startup di cinque persone definisce l'intera configurazione AWS, cioè VPC, database e servizio di container, in un unico repository Terraform con lo stato conservato in un backend S3 cifrato e il blocco tramite DynamoDB. Ogni modifica passa da una pull request, così anche un ingegnere reperibile da solo può vedere esattamente che cosa cambierà prima di eseguire apply. Quando hanno bisogno di un ambiente di staging fresco per una grande dimostrazione, copiano un piccolo modulo e lo montano in pochi minuti, poi lo smontano altrettanto in fretta per tenere bassa la bolletta cloud.

**Grande impresa.** Un rivenditore multinazionale gestisce l'infrastruttura su diversi account e regioni cloud. Un team centrale di piattaforma pubblica moduli Terraform versionati per reti conformi, database e impalcature di servizio e fa rispettare politiche OPA che respingono qualsiasi risorsa priva di cifratura o di etichette di allocazione dei costi. I team di prodotto predispongono in autonomia i propri ambienti, ma ogni modifica scorre attraverso la pipeline, dove la politica è controllata automaticamente. Il rilevamento della deriva gira ogni notte e apre ticket per qualsiasi modifica manuale, mantenendo migliaia di risorse di continuo in uno stato noto e conforme.

**Ente pubblico.** Un'agenzia della difesa che opera in un ambiente ad alta garanzia costruisce immagini d'oro rinforzate che incorporano la base di sicurezza richiesta e distribuisce solo istanze immutabili da quelle immagini. Tutta l'infrastruttura è dichiarata in Git e riconciliata da un agente GitOps dentro l'enclave accreditata, così che nessun operatore detenga credenziali permanenti per modificare direttamente la produzione. Ogni modifica è un commit firmato. Questo dà agli auditor una cronologia completa e a prova di manomissione e soddisfa i requisiti di monitoraggio continuo e controllo della configurazione senza raccolta manuale di evidenze.

## Business case: motivazioni, ROI e TCO

Il ROI dell'IaC viene da velocità, affidabilità e riduzione del rischio. Ambienti che una volta richiedevano settimane di predisposizione manuale guidata da ticket possono essere creati in minuti, il che libera gli ingegneri e accelera i progetti. La riproducibilità taglia drasticamente il tempo di ripristino dopo i guasti, perché qualsiasi ambiente può essere ricostruito dal codice. L'applicazione automatica delle politiche riduce frequenza e costo di incidenti di sicurezza e rilievi di audit, che per le organizzazioni regolamentate possono essere sostanziali.

Sul libro mastro del TCO, i costi di adozione comprendono strumenti, formazione, costruzione di una libreria di moduli e politiche e la disciplina di smettere di fare modifiche manuali. Il costo del non adottare è più ripido e si compone nel tempo: infrastruttura snowflake che nessuno sa ricostruire, predisposizione lenta e soggetta a errori, configurazioni di sicurezza errate che portano a violazioni e audit che consumano settimane di lavoro manuale. Per la leadership, presenta l'IaC come la conversione dell'infrastruttura da passività non gestita a risorsa governata e riproducibile e come il meccanismo che rende sicurezza e conformità automatiche anziché aspirazionali.

## Antipattern e insidie

- **ClickOps in produzione.** Fare modifiche a mano nella console garantisce la deriva e distrugge la riproducibilità.
- **Segreti nel codice.** Scrivere credenziali nei file di definizione le fa trapelare nella cronologia delle versioni e nello stato.
- **Definizioni monolitiche e non modularizzate.** Un'unica enorme configurazione che nessuno osa cambiare diventa fragile quanto la configurazione manuale che ha sostituito.
- **Stato non gestito.** File di stato locali o non bloccati portano a corruzione e infrastruttura persa.
- **Deriva tollerata.** Lasciare al loro posto le modifiche manuali erode la garanzia di fonte di verità finché il codice è finzione.
- **Politica come documentazione.** Le regole che vivono in un wiki anziché in un controllo automatico sono violate di routine.
- **Proliferazione del copia e incolla.** Duplicare la configurazione tra i team significa che correzioni e miglioramenti non si diffondono mai.

## Modello di maturità

**Livello 1: Avvio.** L'infrastruttura è predisposta manualmente tramite la console e script ad hoc. Gli ambienti sono incoerenti, non documentati e non possono essere riprodotti in modo affidabile e il ripristino da un guasto è lento e incerto.

**Livello 2: Sviluppo.** Parte dell'infrastruttura è codificata, ma le pratiche variano per team. La gestione dello stato è incoerente, la deriva è comune, i segreti a volte trapelano nelle definizioni e la politica è fatta rispettare, se lo è, tramite revisione manuale.

**Livello 3: Standardizzazione.** L'IaC dichiarativa è lo standard documentato nell'organizzazione, costruita da moduli condivisi e versionati con stato gestito, remoto e bloccato. La politica come codice fa rispettare i guardrail nella pipeline, i segreti sono richiamati da un gestore dedicato e il rilevamento della deriva gira con una cadenza regolare.

**Livello 4: Gestione.** La pratica è misurata rispetto a valori di riferimento. Segui tasso di deriva e tempo medio di riconciliazione, adozione delle versioni dei moduli tra i team, violazioni di politica bloccate rispetto a sfuggite, tempo di consegna della predisposizione e quota di risorse effettivamente sotto codice. Queste metriche filtrano le modifiche e orientano dove investi, così le decisioni poggiano sull'evidenza anziché sull'aneddoto.

**Livello 5: Orchestrazione.** L'infrastruttura è immutabile e guidata da GitOps, auto-riparante contro la deriva, con evidenza di conformità prodotta automaticamente. La libreria di moduli e politiche migliora continuamente dall'uso reale e dagli incidenti e la pratica infrastrutturale è integrata con la pianificazione di sicurezza, costi e distribuzione così che l'intero patrimonio si adatti al mutare dei requisiti.

## Spunti di discussione

- Dove dovrebbe stare il confine tra moduli governati centralmente e autonomia dei team nel definire infrastruttura personalizzata?
- Come gestite la vera modifica d'emergenza che deve aggirare la pipeline, senza normalizzare il ClickOps?
- Qual è la giusta strategia per gestire e proteggere lo stato tra molti account e team?
- Quando la gestione della configurazione mutabile è ancora giustificata rispetto a un'infrastruttura pienamente immutabile?
- Come mantenete allineata la libreria di politica come codice con requisiti di sicurezza e normativi in evoluzione?
- Che aspetto ha un realistico percorso di migrazione per l'infrastruttura preesistente che precede l'IaC?

## Punti chiave

- Definisci l'infrastruttura in modo dichiarativo, versionala e trattala come codice rivedibile e riproducibile.
- Costruisci da piccoli moduli versionati per diffondere buoni predefiniti ed eliminare la duplicazione.
- Preferisci infrastruttura immutabile e immagini d'oro per abolire la deriva e semplificare il rollback.
- Gestisci lo stato deliberatamente e tieni i segreti fuori dalle definizioni.
- Adotta GitOps per una forte traccia di audit e una riconciliazione auto-riparante.
- Fai rispettare i guardrail con la politica come codice così che la conformità sia impedita sul nascere, non verificata a posteriori.

## Riferimenti e letture di approfondimento

- Kief Morris, *Infrastructure as Code: Dynamic Systems for the Cloud Age*.
- Yevgeniy Brikman, *Terraform: Up & Running*.
- Betsy Beyer, Chris Jones, Jennifer Petoff e Niall Richard Murphy (a cura di), *Site Reliability Engineering*.
- Gene Kim, Jez Humble, Patrick Debois e John Willis, *The DevOps Handbook*.
- Weaveworks, scritti fondativi su "GitOps" (Alexis Richardson et al.).
- Documentazione di Open Policy Agent e del linguaggio di politiche Rego.
- NIST Special Publication 800-53, controlli di sicurezza e privacy (famiglia gestione della configurazione).
