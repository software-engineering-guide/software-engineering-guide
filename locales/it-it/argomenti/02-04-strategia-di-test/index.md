# 2.4 Strategia di test

## Panoramica e motivazioni

Una strategia di [test](https://en.wikipedia.org/wiki/Software_testing) è l'insieme deliberato di scelte su che cosa testare, a quale livello, con quanta automazione e con quale grado di confidenza, così che il tuo team possa cambiare il codice in fretta senza romperlo. I test sono ciò che permette a una grande organizzazione di rilasciare spesso e in sicurezza. Codificano il comportamento atteso, colgono le regressioni e danno agli ingegneri la fiducia di fare [refactoring](https://en.wikipedia.org/wiki/Code_refactoring). Senza una strategia coerente, il testing tende ad andare in uno di due modi cattivi: assente (sviluppo dettato dalla paura e lento) o gonfio (migliaia di test lenti e instabili di cui nessuno si fida).

Per un grande team, la strategia conta più di qualsiasi singolo test. Centinaia di ingegneri che lavorano in una base di codice condivisa hanno bisogno di una rete di sicurezza veloce e affidabile. Senza di essa, ogni modifica è rischiosa e ogni rilascio diventa una prova manuale. I test funzionano anche come documentazione eseguibile del comportamento voluto, inestimabile una volta che gli autori originali sono passati ad altro. La strategia decide se la tua suite di test è una risorsa che accelera la consegna o una passività che la frena.

Nei contesti aziendali e governativi il testing ha un peso aggiuntivo. Le normative possono richiedere copertura di test ed evidenze documentate. I sistemi critici per la sicurezza e rivolti ai cittadini richiedono alta garanzia. I test di accessibilità e di sicurezza possono essere richiesti per legge. La strategia deve quindi bilanciare velocità, confidenza, costo e conformità, e deve trattare la copertura come un segnale, non come un obiettivo da manipolare.

## Principi chiave

- Testa per ottenere la fiducia di cambiare, non per raggiungere un numero.
- Privilegia test veloci, affidabili e isolati. I test lenti o instabili erodono la fiducia che rende utile una suite.
- Spingi i test al livello più basso che dà vera confidenza e riserva i test lenti e ampi al rischio di integrazione genuino.
- Un test instabile è un test rotto. Tratta l'instabilità come un difetto di prim'ordine.
- La copertura è un segnale, non un obiettivo. Un'alta copertura di codice banale prova poco.
- Testa comportamento e contratti, non dettagli di implementazione, così che i tuoi test sopravvivano al refactoring.
- Rendi il testing non funzionale (accessibilità, prestazioni, sicurezza) parte della strategia, non un ripensamento.

## Raccomandazioni

### Usa la piramide dei test come impostazione predefinita e conosci le sue critiche

Adotta come predefinito molti [test unitari](https://en.wikipedia.org/wiki/Unit_testing) veloci, meno [test di integrazione](https://en.wikipedia.org/wiki/Integration_testing) e un piccolo numero di test end-to-end, perché costo e fragilità crescono con l'ampiezza. Conosci anche le critiche: la forma dovrebbe seguire la tua architettura, non il dogma. Un sistema ricco di servizi può avere bisogno di uno strato di integrazione più grande (il "trofeo dei test"), e il vero obiettivo è la confidenza per unità di costo e velocità, non una sagoma particolare. Qualunque cosa tu faccia, evita la piramide rovesciata di test end-to-end per lo più lenti.

### Adotta TDD, BDD e lo sviluppo guidato dalle specifiche dove aiutano

Usa lo [sviluppo guidato dai test](https://en.wikipedia.org/wiki/Test-driven_development) (TDD) per guidare il progetto e garantire la testabilità, soprattutto per la logica complessa. È una disciplina di progettazione tanto quanto di testing. Usa lo [sviluppo guidato dal comportamento](https://en.wikipedia.org/wiki/Behavior-driven_development) (BDD) per esprimere i test nel linguaggio del dominio che condividi con gli stakeholder, il che è prezioso per i criteri di accettazione in ambienti regolamentati o ricchi di requisiti. Lo sviluppo guidato dalle specifiche fa un passo in più: tratta una specifica eseguibile (il comportamento concordato, espresso come esempi) come l'unica fonte di verità che sia guida l'implementazione sia la verifica. Eccelle dove i requisiti devono essere tracciabili fino all'evidenza di accettazione, come nei programmi governativi e regolamentati. Legato a tutti e tre è il **[shift-left testing](https://en.wikipedia.org/wiki/Shift-left_testing)**: spostare la verifica il più presto possibile nel ciclo di vita, scrivendo i test insieme o prima del codice ed eseguendoli di continuo, così da cogliere i difetti quando costa meno correggerli, anziché in fasi di test tardive o in produzione. Nessuno di questi è obbligatorio ovunque. Applicali dove aggiungono chiarezza.

### Impiega tecniche avanzate per il codice di alto valore

Usa il testing basato sulle proprietà per verificare invarianti su molti input generati, cogliendo casi limite che i test basati su esempi mancano. Usa il [fuzz testing](https://en.wikipedia.org/wiki/Fuzzing) su parser e confini di input non fidato per trovare arresti anomali e falle di sicurezza. Usa il [mutation testing](https://en.wikipedia.org/wiki/Mutation_testing) per misurare se i tuoi test individuano davvero guasti iniettati, un segnale di qualità molto migliore della copertura grezza. Usa con giudizio il testing a istantanee (snapshot) per l'output serializzato e stai attento alla trappola di riapprovare alla cieca le istantanee.

### Gestisci i dati di test e usa dati sintetici

Rendi deterministici i test con dati di test controllati e isolati ed evita fixture mutabili condivise che accoppiano i test tra loro. Genera [dati sintetici](https://en.wikipedia.org/wiki/Synthetic_data) che rispecchiano le caratteristiche della produzione senza esporre informazioni personali reali, il che è essenziale dove le regole sulla privacy vietano di usare dati di produzione negli ambienti di test. Fornisci factory o builder così che ogni test possa costruire esattamente i dati di cui ha bisogno.

### Tratta i test instabili come difetti

Rileva automaticamente l'instabilità, sposta i test instabili fuori dal percorso bloccante e correggili o eliminali entro una scadenza. Una suite che fallisce a caso addestra gli ingegneri a ignorare i fallimenti, il che distrugge tutto il suo valore. Segui i tassi di instabilità e rendi l'affidabilità una metrica di qualità esplicita della suite stessa.

### Usa la copertura come segnale e aggiungi il testing non funzionale

Misura la copertura per trovare le aree non testate, ma non trasformarla in un obiettivo rigido che inviti alla manipolazione con test privi di asserzioni. Affiancale il mutation testing per la profondità. Incorpora nella pipeline test di accessibilità (controlli automatici più audit manuali), test di prestazioni (riferimenti di carico e latenza con rilevamento delle regressioni) e test di sicurezza (scansione delle dipendenze, [analisi statica](https://en.wikipedia.org/wiki/Static_program_analysis) e test dinamici).

## Compromessi: vantaggi e svantaggi

| Tipo di test / pratica | Vantaggi | Svantaggi |
|---|---|---|
| Test unitari | Veloci, precisi, economici, stabili | Mancano i bug di integrazione e di sistema |
| Test di integrazione | Colgono difetti di interfaccia e di collegamento | Più lenti; più preparazione; più fragili |
| Test end-to-end | Massima confidenza nel comportamento reale | Lenti, instabili, costosi da mantenere |
| TDD | Progetto migliore, testabilità garantita | Curva di apprendimento; all'inizio sembra lento |
| Testing basato sulle proprietà | Trova casi limite, codifica invarianti | Richiede di pensare per proprietà; più difficile da scrivere |
| Mutation testing | Vera misura dell'efficacia dei test | Costoso in calcolo; lento da eseguire |
| Obiettivo di alta copertura | Fa emergere codice non testato | Manipolabile; può incentivare test di basso valore |

Il compromesso centrale è tra confidenza e velocità e costo. Test più ampi danno più confidenza ma girano più lentamente e si rompono più spesso. Test più stretti sono veloci e stabili ma mancano i difetti a livello di sistema. La giusta combinazione massimizza la confidenza per secondo di feedback e per ora di manutenzione. E l'eccesso di test è una vera modalità di fallimento: una suite gonfia di test ridondanti, lenti e fragili può costare più dei bug che previene.

## Domande da discutere con il tuo team

1. **Quali test non funzionali, di accessibilità, prestazioni e sicurezza, dovrebbero bloccare un rilascio e quali dovrebbero solo riferire?** Questo capitolo sostiene che il testing non funzionale appartenga alla strategia anziché essere un ripensamento, e nota che l'accessibilità può essere richiesta per legge e che i test di sicurezza possono far parte dell'evidenza di autorizzazione all'esercizio. Per un sistema grande o rivolto ai cittadini, un cancello bloccante rallenta la consegna, ma un difetto di accessibilità o di sicurezza trovato in produzione porta costi di rimedio, reputazione e legali che superano di gran lunga il test. Porta i segnali che decidono: la tua esposizione normativa, se il sistema è rivolto ai cittadini e quanto spesso oggi questi difetti sfuggono in produzione. Rendi bloccanti i controlli richiesti per legge e lascia che quelli a rischio più basso riferiscano con un andamento, così che il cancello rifletta il rischio reale anziché il dogma. La risposta stabilisce direttamente che cosa può e non può essere integrato.

2. **Fissate una percentuale di copertura rigida come cancello e, se sì, che cosa impedisce agli ingegneri di manipolarla con test privi di asserzioni?** Il capitolo è fermo nel dire che la copertura è un segnale, non un obiettivo, che un'alta copertura di codice banale prova poco e che un obiettivo rigido invita alla manipolazione. Un singolo numero imposto in una grande organizzazione produce in modo affidabile test che eseguono codice senza asserire nulla, il che alza la metrica e abbassa la confidenza reale. Porta alla discussione un segnale migliore: un punteggio di mutation testing sui moduli di maggior valore, che misura se i test individuano davvero guasti iniettati. Usa la copertura per trovare le aree non testate e il mutation testing per la profondità e resisti a trasformare l'uno o l'altro in un obiettivo che la leadership segue in isolamento. Decidi dove il numero aiuta davvero e dove invita solo al teatro.

3. **Qual è la vostra politica quando la suite di test diventa troppo lenta perché gli ingegneri la aspettino?** Il compromesso centrale di questo capitolo è tra confidenza e velocità e costo, e nomina l'eccesso di test come una vera modalità di fallimento in cui una suite gonfia, ridondante e lenta costa più dei bug che previene. In un grande team, il tempo di esecuzione della suite è una tassa condivisa pagata a ogni modifica, e una suite che le persone imparano ad aggirare perde tutto il suo valore. Porta le prove: tempo reale di CI, i test più lenti e quanta copertura end-to-end ridondante duplica test unitari più economici. Spingi i test al livello più basso che dà vera confidenza, parallelizza ed elimina entro una scadenza i test lenti ridondanti. L'obiettivo è ottimizzare la confidenza per secondo di feedback, non il numero grezzo di test.

4. **Quando un test diventa instabile, chi ne è responsabile, quanto in fretta va corretto o eliminato e che cosa fa rispettare quella scadenza?** Questo capitolo tratta un test instabile come un test rotto, un difetto di prim'ordine, perché una suite che fallisce a caso addestra un grande team a ignorare le build rosse e distrugge in silenzio la rete di sicurezza da cui tutti dipendono. La pressione contraria è reale: mettere in quarantena un test instabile sblocca la consegna oggi ma rischia di mascherare un vero bug intermittente, mentre bloccare su di esso ferma centinaia di ingegneri per un fallimento che può essere puro rumore. Porta le prove che risolvono la questione: il tuo attuale tasso di instabilità, quanto tempo i test restano in quarantena prima che qualcuno li tocchi e quanti test in quarantena si sono rivelati nascondere un difetto reale. Assegna un responsabile a ogni test in quarantena, fissa una scadenza rigida per correggerlo o eliminarlo e segui l'affidabilità come metrica esplicita della suite stessa. Nei contesti aziendali e governativi in cui una build verde fa parte dell'evidenza di rilascio, una pila di quarantena non gestita è anche una passività di audit, perché stai rilasciando su un segnale di cui hai concordato in privato di non fidarti.

5. **Potete usare dati di produzione negli ambienti di test, e se no, come genererete dati sintetici abbastanza fedeli da cogliere difetti reali?** Il capitolo è diretto nel dire che le regole sulla privacy spesso vietano dati personali reali nei test e che i dati sintetici devono rispecchiare le caratteristiche della produzione, altrimenti i tuoi test danno falsa confidenza. Per una grande organizzazione la tensione è tra fedeltà e conformità: i dati di produzione colgono i casi limite disordinati che quelli sintetici mancano, ma ogni loro copia moltiplica la tua esposizione e i tuoi obblighi. Porta i dettagli: quali insiemi di dati contengono dati personali o regolamentati, che cosa richiedono davvero le tue regole su privacy e residenza dei dati e quanto bene le tue fixture attuali riproducono le distribuzioni e i casi limite visti in produzione. Standardizza factory o builder così che ogni test costruisca esattamente i dati di cui ha bisogno e investi in una generazione sintetica che corrisponda alle reali distribuzioni demografiche e di volume. Nei programmi governativi e regolamentati, usare dati dei cittadini in un ambiente di test non è una scorciatoia, è una violazione da segnalare, quindi la strategia dei dati va stabilita prima di allestire il primo ambiente.

6. **Dove dovrebbero essere attesi, anziché facoltativi, TDD, BDD o lo sviluppo guidato dalle specifiche, e chi decide?** Questo capitolo presenta queste come discipline da applicare dove aggiungono chiarezza, non come obblighi per ogni riga di codice, eppure un grande team trae beneficio da un valore predefinito condiviso, così che la pratica non si frammenti team per team. Il compromesso è tra i benefici di progettazione e tracciabilità (specifiche eseguibili che gli esperti di policy possono rivedere, test che sopravvivono al refactoring) e la reale curva di apprendimento e lentezza iniziale che fanno ritorcere contro un obbligo generalizzato. Porta prove per delimitare l'ambito: quali moduli portano logica complessa o alti tassi di fallimento delle modifiche, dove i criteri di accettazione devono essere tracciabili fino ai requisiti e come riferiscono su velocità e tassi di difetti i team che già li praticano. Riserva l'aspettativa alla logica complessa e alle aree ricche di requisiti e lascia che il codice più semplice scelga da sé. Nei programmi regolamentati e governativi in cui il software deve essere tracciabile fino alla legge che implementa, lo sviluppo guidato dalle specifiche con evidenza di accettazione eseguibile è meno una preferenza che una via verso la tua autorizzazione all'esercizio, quindi indica esplicitamente dove è richiesto.

## Lente settoriale

**Startup.** Un team minuscolo non può dotarsi di QA, quindi fai guadagnare alla suite il proprio posto: test unitari veloci a ogni commit più un paio di test end-to-end sull'unico percorso che paga le bollette e nulla che non manterrai. Salta gli obiettivi di copertura e testa la logica che più temi di rompere, così da rilasciare più volte al giorno senza un passaggio di regressione manuale. Correggi un test instabile lo stesso giorno, perché a questo stadio una suite che il team impara a ignorare è peggio di nessuna suite.

**Piccola impresa.** Senza un ingegnere di test dedicato e con un budget ridotto, appoggiati ai test integrati nei framework e negli strumenti che già usi anziché a un'infrastruttura su misura che non sai supportare. Dai priorità alla manciata di controlli che proteggono ricavi e fiducia dei clienti e usa una CI ospitata, così da non mantenere in proprio l'infrastruttura di build. Preferisci comprare come servizio la scansione di accessibilità e sicurezza anziché costruirla, poiché un singolo difetto mancato può costare più di un anno dello strumento.

**Grande impresa.** Tra molti team il problema della strategia è la coerenza: una piramide predefinita condivisa, quarantena automatica dei test instabili e cancelli non funzionali che significhino la stessa cosa ovunque, così che una build verde sia affidabile chiunque l'abbia prodotta. Metti a bilancio il tempo di esecuzione della suite come tassa condivisa e parallelizza con decisione, perché il tempo reale di CI è pagato a ogni modifica da ogni ingegnere. Gestisci copertura e punteggi di mutation come segnali di portafoglio con chiara responsabilità, non come numeri che la leadership segue in isolamento.

**Ente pubblico.** Appalti e vigilanza fanno del testing un'evidenza, non solo igiene ingegneristica. Esprimi le regole di ammissibilità e di policy come specifiche eseguibili rivedute da esperti di dominio, così da poter tracciare il software fino alla legge che implementa, e rendi bloccanti i test di accessibilità e sicurezza perché sono richiesti per legge e parte dell'evidenza di autorizzazione all'esercizio. Usa dati sintetici generati per corrispondere alle distribuzioni reali, poiché i dati dei cittadini in un ambiente di test sono una violazione da segnalare, e mantieni verificabili gli artefatti di test, così che un revisore esterno possa confermare esattamente che cosa è stato verificato.

## Esempi

**Startup.** Una startup di cinque persone non può permettersi un team di QA, quindi si appoggia a una suite di test unitari veloce che gira a ogni commit più un paio di test end-to-end che coprono il percorso dall'iscrizione al pagamento che paga le bollette. I fondatori saltano la copertura esaustiva e testano invece la logica che più temono di rompere, il che permette loro di rilasciare più volte al giorno senza un passaggio di regressione manuale. Quando un test instabile comincia a fallire a caso, lo correggono lo stesso giorno, perché una suite che il team impara a ignorare è peggio di nessuna suite nella fase in cui la fiducia è tutto.

**Grande impresa.** Una grande piattaforma di e-commerce mantiene migliaia di test unitari veloci che girano a ogni commit in pochi minuti, un insieme mirato di test di integrazione attorno ai confini di pagamenti e inventario e una piccola suite di test end-to-end per i percorsi critici del pagamento. I test end-to-end instabili sono messi automaticamente in quarantena e assegnati per la riparazione. Poiché gli ingegneri si fidano della suite, rilasciano molte volte al giorno, sicuri che una build rossa significhi un problema reale.

**Ente pubblico.** Un sistema nazionale di prestazioni sotto vigilanza normativa usa il BDD per esprimere le regole di ammissibilità come specifiche eseguibili rivedute da esperti di policy, il che dà evidenza tracciabile che il software implementa la legge. Usa dati sintetici generati per corrispondere alle reali distribuzioni demografiche, perché le regole sulla privacy vietano i dati dei cittadini negli ambienti di test. Il test di accessibilità è obbligatorio e blocca il rilascio, poiché il servizio deve essere utilizzabile da tutti i cittadini. E il test di sicurezza fa parte dell'evidenza di autorizzazione all'esercizio (ATO), l'approvazione formale per far funzionare il sistema in produzione.

## Business case: motivazioni, ROI e TCO

Il ritorno del testing è la capacità di cambiare il software in fretta e in sicurezza, che è il fondamento di una velocità di consegna sostenuta. Una suite automatica affidabile sostituisce il [test di regressione](https://en.wikipedia.org/wiki/Regression_testing) manuale, lento e costoso, e coglie i difetti quando costa meno correggerli, prima del rilascio anziché in produzione. In un sistema regolamentato o rivolto ai cittadini, il costo di un difetto in produzione (rimedio, reputazione ed esposizione legale potenziale) supera di gran lunga il costo dei test che lo avrebbero colto.

Il costo di adozione è reale: si scrivono e si mantengono i test e si costruisce l'infrastruttura di [integrazione continua](https://en.wikipedia.org/wiki/Continuous_integration) (CI). Ma il costo del non testare è più alto e si accumula: sviluppo dettato dalla paura che rallenta fino a trascinarsi, regressioni frequenti e processi di rilascio manuali che non scalano. C'è anche un costo dell'eccesso di test, quindi l'argomento è a favore di una strategia ben progettata, non del massimo numero di test. Per sostenere il caso con la leadership, collega la suite a frequenza dei rilasci, tasso di fallimento delle modifiche e tempo medio di ripristino, e quantifica lo sforzo di test manuale che sostituisce e gli incidenti in produzione che previene.

## Antipattern e insidie

- **Testing a cono gelato:** perlopiù test end-to-end lenti su una base unitaria sottile; lento, instabile, costoso.
- **Copertura come obiettivo:** inseguire una percentuale con test banali o privi di asserzioni che non provano nulla.
- **Testare i dettagli di implementazione:** test accoppiati agli interni che si rompono a ogni refactoring, scoraggiando il cambiamento.
- **Instabilità tollerata:** fallimenti casuali che addestrano il team a ignorare le build rosse.
- **Dati di test mutabili e condivisi:** test che interferiscono tra loro e falliscono in modo imprevedibile.
- **Usare dati di produzione nei test:** una violazione di privacy e conformità in attesa di accadere.
- **Testing non funzionale saltato:** accessibilità, prestazioni e sicurezza scoperte solo in produzione.
- **La suite di cui non ci si fida:** così inaffidabile che gli ingegneri la rieseguono o la aggirano di routine, vanificandone lo scopo.

## Modello di maturità

- **Livello 1, Avvio:** il testing è manuale e reattivo; la copertura automatica è minima; le regressioni sono frequenti e colte tardi, spesso dagli utenti anziché dalla suite.
- **Livello 2, Sviluppo:** esistono test unitari automatici e qualche test di integrazione, ma la suite è lenta o instabile, la fiducia è bassa e la pratica varia molto da un team all'altro.
- **Livello 3, Standardizzazione:** una suite bilanciata, veloce e affidabile fa da cancello a ogni modifica; una piramide predefinita documentata, una politica sui test instabili e il testing non funzionale (accessibilità, prestazioni, sicurezza) sono fatti rispettare in modo coerente tra i team.
- **Livello 4, Gestione:** la salute della suite è misurata e controllata rispetto a valori di riferimento; si seguono e si rivedono tasso di instabilità, tempo reale di CI, punteggio di mutation sui moduli di alto valore e tasso di difetti sfuggiti; la copertura è un segnale tra molti e i cancelli scattano sulle prove anziché sulle opinioni.
- **Livello 5, Orchestrazione:** tecniche avanzate (basate sulle proprietà, mutation, fuzz) mirano al codice di alto valore; il testing è integrato con metriche di consegna come frequenza dei rilasci, tasso di fallimento delle modifiche e tempo medio di ripristino; l'organizzazione rimodella di continuo la suite su architettura e rischio, ritirando i test ridondanti e investendo dove le prove mostrano che i difetti ancora sfuggono.

## Spunti di discussione

- Che forma ha davvero la vostra distribuzione dei test, e corrisponde alla vostra architettura e al vostro rischio?
- Come decidete quando un pezzo di codice merita testing basato sulle proprietà o mutation anziché test basati su esempi?
- Qual è la vostra politica per i test instabili, ed è davvero fatta rispettare?
- Come generate dati sintetici realistici senza far trapelare informazioni sensibili?
- Dove la copertura vi aiuta davvero, e dove è stata manipolata?
- Come dovrebbero essere rivisti i test generati dall'IA perché aggiungano confidenza anziché rumore?

## Punti chiave

- Testa per ottenere confidenza nel cambiare; ottimizza la confidenza per unità di velocità e costo.
- Usa la piramide come valore predefinito ma adatta il testing alla tua architettura.
- Tratta i test instabili come difetti e la copertura come un segnale, non un obiettivo.
- Applica tecniche avanzate dove il valore giustifica il costo.
- Includi nella strategia i test di accessibilità, prestazioni e sicurezza e usa dati sintetici per proteggere la privacy.

## Riferimenti e letture di approfondimento

- Kent Beck, *Test-Driven Development: By Example*
- Lisa Crispin e Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*
- Michael Feathers, *Working Effectively with Legacy Code*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Martin Fowler, articoli sulla Test Pyramid e su schemi legati ai test
