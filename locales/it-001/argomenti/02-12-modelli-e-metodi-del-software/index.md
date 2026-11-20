# 2.12 Modelli e metodi del software

## Panoramica e motivazioni

Un modello software è una semplificazione deliberata di un sistema, costruita per rispondere a una domanda specifica. Un metodo è un modo disciplinato di produrre software, compresi i modelli che usa lungo la strada. Insieme formano un'area di conoscenza dello Software Engineering Body of Knowledge (SWEBOK), perché sono gli strumenti mentali che usi per ragionare su un sistema prima, durante e dopo averlo costruito. Un diagramma delle classi UML ([Unified Modelling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language)), un [diagramma entità-relazione](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) (ERD), una [macchina a stati](https://en.wikipedia.org/wiki/Finite-state_machine), una [specifica formale](https://en.wikipedia.org/wiki/Formal_specification) e un prototipo usa e getta sono tutti modelli. [Waterfall](https://en.wikipedia.org/wiki/Waterfall_model), [prototipazione](https://en.wikipedia.org/wiki/Software_prototyping), sviluppo formale e [agile](https://en.wikipedia.org/wiki/Agile_software_development) sono tutti metodi.

Perché darsi pena di fare modelli? Perché la memoria di lavoro umana è piccola e i sistemi software sono grandi. Nessuno può tenere a mente un sistema di centomila righe, quindi disegniamo immagini e scriviamo astrazioni che mostrano una faccia alla volta: i dati, il flusso di controllo, gli stati, le interazioni. Un modello non è mai pensato per essere fedele al codice; è pensato per essere adatto a una decisione. Un buon modello mostra esattamente ciò che serve per decidere qualcosa e nasconde tutto il resto.

Nei grandi team la vera posta è coordinamento e comunicazione. Quando centinaia di ingegneri, architetti, analisti e auditor lavorano su un sistema, i modelli condivisi sono il terreno comune in cui negoziano progetto, requisiti e rischio. Pensa quindi alla modellazione come a uno strumento con un compito da svolgere. Rende quando un modello costa meno dell'errore che previene. Diventa spreco quando lo disegni fine a se stesso, lo tieni a lungo dopo che è diventato obsoleto o lo elabori oltre la decisione che doveva servire. La modellazione si collega strettamente ai requisiti del software (capitolo 2.8), ai principi di progettazione del software (capitolo 2.2), all'architettura e alle sue notazioni come C4 e arc42 (capitolo 3.1) e ai modi di lavorare agili (capitolo 10.7).

## Principi chiave

- Ogni modello ha uno scopo; se non sai nominare la decisione che un modello informa, non disegnarlo.
- L'astrazione è l'atto centrale della modellazione: includi ciò che conta per lo scopo, ometti il resto.
- La coerenza conta all'interno dei modelli e tra modelli; i modelli contraddittori sono peggio di nessuno.
- I modelli sono prima di tutto artefatti di comunicazione; il loro pubblico determina notazione e dettaglio.
- Preferisci il modello più leggero che risponde alla domanda; l'elaborazione ha un costo di mantenimento.
- Un modello vale quanto la sua analisi; un modello non verificato è un presupposto non testato.
- Scegli il metodo in base a incertezza, rischio e conseguenze di un fallimento del problema.

## Raccomandazioni

### Modella con astrazione, scopo e coerenza

Inizia ogni modello nominandone scopo e destinatario. Poi astrai senza pietà verso quello scopo: un diagramma di sequenza pensato per risolvere una race condition dovrebbe mostrare tempi e messaggi, non ogni campo. Mantieni i tuoi modelli coerenti l'uno con l'altro, così che le entità in un ERD, le classi in un diagramma delle classi e i nomi nei requisiti concordino tutti, e coerenti con la realtà, il che significa aggiornare o eliminare un modello quando il sistema va avanti. Un modello obsoleto di cui le persone si fidano è un pericolo. Un modello obsoleto che tutti ignorano è spreco che costa ancora attenzione.

### Scegli modelli strutturali o comportamentali per adattarli alla domanda

Usa modelli strutturali per mostrare di che cosa è fatto un sistema e come le parti si relazionano: diagrammi delle classi, diagrammi dei componenti e diagrammi entità-relazione per la struttura dei dati. Usa modelli comportamentali per mostrare che cosa fa un sistema nel tempo: macchine a stati per oggetti con cicli di vita significativi, diagrammi di sequenza per le interazioni tra componenti e diagrammi di attività per flussi di lavoro e processi di business. Scegli l'unica notazione che mette a nudo la decisione che hai davanti. La maggior parte dei sistemi ha bisogno solo di una manciata di tipi di diagramma, disegnati selettivamente, non dell'intero catalogo UML applicato a tutto.

### Analizza i modelli, non limitarti a disegnarli

Un modello si guadagna il posto con l'analisi, non solo con il disegno. Controlla una macchina a stati per stati irraggiungibili, transizioni mancanti e deadlock. Controlla un ERD per problemi di normalizzazione e relazioni orfane. Ripercorri un diagramma di sequenza rispetto ai requisiti per trovare percorsi d'errore mancanti. Rivedi i tuoi modelli con gli esperti di dominio che sanno individuare che cosa è sbagliato. E dove il costo di un fallimento è alto, ricorri all'analisi supportata da strumenti (verificatori di modelli, verificatori di coerenza, simulazione) anziché guardare a occhio.

### Applica i metodi euristici come impostazione predefinita

La maggior parte del software è costruita con metodi euristici: approcci iterativi basati sull'esperienza che usano i modelli in modo informale e giudicano i risultati rispetto alle aspettative anziché alle dimostrazioni. Per la maggior parte dei sistemi aziendali e governativi è esattamente giusto: i requisiti evolvono e un difetto è di solito recuperabile. I metodi euristici si abbinano naturalmente all'agile (capitolo 10.7): modella quanto basta per allineare il team, poi costruisci e impara.

### Riserva i metodi formali ai nuclei ad alta conseguenza

I [metodi formali](https://en.wikipedia.org/wiki/Formal_methods) esprimono le specifiche in matematica e usano la verifica, sia essa dimostrazione o [verifica esaustiva di modelli](https://en.wikipedia.org/wiki/Model_checking), per stabilire proprietà. Costano vera competenza e tempo, e rendono proprio dove il fallimento è catastrofico o irreversibile: controllo critico per la sicurezza, protocolli crittografici, nuclei di regolamento finanziario e simili. Applicali al piccolo nucleo critico, non all'intero sistema. E nota che la sola specifica formale, anche senza dimostrazione completa, spesso aggiunge valore semplicemente costringendoti a essere preciso.

### Usa la prototipazione per ritirare l'incertezza

Quando requisiti o fattibilità sono poco chiari, costruisci un prototipo per imparare, poi decidi, di proposito, se farlo evolvere o scartarlo. I prototipi usa e getta esplorano una domanda a basso costo e poi vengono eliminati. I prototipi evolutivi diventano il prodotto e devono essere costruiti a standard di produzione. Il fallimento classico è lasciare che un prototipo usa e getta scivoli in produzione per caso. Indica quindi il tipo del prototipo prima di costruirlo.

### Adegua il metodo al rischio, non alla moda

Scegli i metodi in base all'incertezza del problema e alle conseguenze di un fallimento. L'alta incertezza favorisce prototipazione e iterazione agile. L'alta conseguenza favorisce analisi formale e verifica rigorosa. Un sistema che ha entrambe ha bisogno di un nucleo formale critico dentro un involucro per il resto agile. Qualunque cosa tu faccia, non adottare un metodo solo perché è prestigioso o perché un fornitore lo vende.

## Compromessi: vantaggi e svantaggi

| Modello o metodo | Applicato bene | Modalità di fallimento |
|---|---|---|
| Modelli strutturali (UML, ERD) | Immagine condivisa di parti e dati | Proliferazione di diagrammi; deriva dal codice |
| Modelli comportamentali (stato, sequenza, attività) | Mettono a nudo tempi, stati e casi limite | Diagrammi troppo dettagliati che nessuno legge |
| Metodi euristici | Rapidi, flessibili, adatti alla maggior parte dei sistemi | Indisciplinati; presupposti nascosti |
| Metodi formali | Proprietà dimostrabili per nuclei critici | Costo alto; applicati all'intero sistema |
| Prototipazione | Apprendimento economico; ritira presto il rischio | Codice usa e getta promosso in produzione |
| Metodi agili | Si adattano ai requisiti mutevoli | Saltano la modellazione necessaria per i problemi difficili |

La tensione ricorrente è tra rigore e velocità. Troppa poca modellazione porta in produzione presupposti nascosti. Troppa modellazione brucia sforzo su diagrammi che non informano mai una decisione e marciscono nel momento in cui il codice cambia. Non esiste una dose fissa che risolva questo, solo una regola di proporzione: investi in un modello o in un metodo in proporzione all'incertezza che risolve e al costo di sbagliare la decisione. Un motore di pagamenti e un microsito di marketing meritano trattamenti diversi.

## Domande da discutere con il tuo team

1. **Analizziamo i nostri modelli, o li disegniamo e basta e andiamo avanti?** Un modello si guadagna il posto con l'analisi, non con l'esistere: una macchina a stati che non controlli mai per stati irraggiungibili o transizioni mancanti è un presupposto non testato travestito da diagramma. In un grande team è qui che si nascondono i difetti reali, perché un'immagine dall'aria plausibile viene presa per buona proprio quando nessuno l'ha confrontata con i requisiti per trovare il percorso d'errore mancante o la relazione orfana. Porta alla riunione il tuo modello comportamentale più importante e prova a romperlo: quale transizione è indefinita, quale stato non ha uscita, quale sequenza non ha timeout? Dove il costo di un fallimento è alto, la risposta dovrebbe spingerti verso un'analisi supportata da strumenti (verificatori di modelli, verificatori di coerenza, simulazione) anziché guardare a occhio, perché l'intera ragione di modellare un nucleo critico è trovare il difetto su una lavagna anziché in produzione.

2. **Quando due dei nostri modelli sono in disaccordo, quale vince, e chi nota la contraddizione?** La coerenza conta all'interno dei modelli e tra modelli, e i modelli contraddittori sono peggio di nessuno, perché le persone agiscono su entrambi. In un grande sistema le entità del modello di dati, le classi del progetto e i nomi dei requisiti si allontanano in silenzio mentre team diversi aggiornano artefatti diversi, e il primo segno è spesso un bug in produzione in cui due componenti non concordavano su che cosa fosse una cosa. Porta un esempio: scegli un concetto centrale e verifica se ERD, codice e requisiti concordano davvero sulla sua forma e sul suo ciclo di vita. Se no, decidi quale artefatto è autorevole e chi è responsabile di tenere allineati gli altri, e sii disposto a eliminare un modello piuttosto che lasciare che uno obsoleto continui a mentire al team.

3. **Quale nucleo del nostro sistema, se sbagliato, fa perdere denaro vero o danneggia qualcuno, e riceve il rigore che merita?** La mossa centrale di questo capitolo è adeguare il metodo al rischio: metodi euristici e agili per la maggioranza recuperabile, specifica formale e verifica per il piccolo nucleo ad alta conseguenza e prototipazione economica per ciò che è davvero incerto. I modi di fallire sono simmetrici ed entrambi costosi: applicare metodi formali a un microsito di marketing brucia denaro, e trattare un motore di regolamento o un insieme di regole di ammissibilità come lavoro agile ordinario invita il difetto catastrofico e irreversibile. Porta una mappa del tuo sistema e segna dove un errore è catastrofico rispetto a recuperabile e dove i requisiti sono certi rispetto a sconosciuti. La risposta dovrebbe concentrare il tuo investimento di modellazione dove stanno denaro e ambiguità e negarlo esplicitamente ovunque altrove, così che un nucleo formale critico possa stare dentro un involucro per il resto agile senza che un metodo invada il territorio dell'altro.

4. **Quanta modellazione facciamo prima di scrivere codice, e quella dose cambia con l'incertezza che abbiamo davanti?** La grande progettazione iniziale e nessuna progettazione sono entrambe modalità di fallimento, e la giusta dose sta nel mezzo, governata da quanta incertezza un modello ritira davvero. In un grande team la pressione va in entrambe le direzioni: un processo di governance può esigere un insieme completo di diagrammi prima di qualsiasi codice, fissando decisioni prese con meno informazioni, mentre la pressione della consegna può spingere un team a saltare l'unica macchina a stati che avrebbe colto un caso limite costoso. Porta i tuoi ultimi due progetti e ordina i modelli che hai prodotto in quelli che hanno informato una decisione reale e quelli disegnati solo perché un modello lo chiedeva. Nei programmi aziendali e governativi, dove un cancello di fase o un comitato di approvazione impone spesso documenti in anticipo, vieni pronto a sostenere una modellazione che segue il rischio anziché un elenco fisso di prodotti da consegnare, così che il nucleo dei pagamenti riceva il suo rigore e lo strumento di reportistica interna non anneghi in diagrammi che nessuno legge.

5. **Abbiamo concordato una notazione condivisa e un'unica casa per i nostri modelli, o ogni team inventa la propria?** I modelli sono prima di tutto artefatti di comunicazione, e il loro valore crolla quando una macchina a stati disegnata nello strumento di un team non può essere letta, trovata o creduta dal team che la eredita. Per centinaia di ingegneri le considerazioni in gioco sono reali: una notazione e un repository imposti comprano coerenza e reperibilità, ma impongono anche un costo di apprendimento e possono spingere le persone verso strumenti pesanti quando una lavagna fotografata basterebbe. Porta esempi di dove un modello vivesse davvero (una wiki, uno strumento di diagrammi, una presentazione, il portatile di qualcuno) e chiediti chi potrebbe trovarlo e capirlo sei mesi dopo. Nei contesti aziendali e regolamentati l'angolo dell'audit lo acuisce: un auditor che non riesce a trovare il modello di dati attuale né a ricondurre una decisione a una macchina a stati documentata tratterà il sistema come non documentato, quindi concorda una piccola notazione condivisa e una collocazione durevole e accetta una cattura leggera anziché la cerimonia dove la conseguenza è bassa.

6. **Prima di costruire un prototipo, decidiamo di proposito se è usa e getta o evolutivo, e ci atteniamo a quella scelta?** Il fallimento classico e costoso è un prototipo usa e getta che scivola in silenzio in produzione perché ha fatto bella figura nella dimostrazione e nessuno ne aveva indicato il tipo in anticipo. La tensione è genuina: i prototipi usa e getta comprano l'apprendimento più economico possibile e dovrebbero essere eliminati, mentre i prototipi evolutivi diventano il prodotto e devono essere costruiti a standard di produzione fin dalla prima riga, e confondere i due o spreca rifacimenti o rilascia codice fragile in un ruolo per cui non era stato progettato. Porta un prototipo recente e chiediti che cosa fu deciso prima che fosse costruito, chi aveva l'autorità di promuoverlo o scartarlo e se quella decisione sia sopravvissuta alla pressione della consegna. Nel settore pubblico e in altri contesti con responsabilità, dove un sistema rivolto ai cittadini porta obblighi di trasparenza e affidabilità, tratta la promozione accidentale come un fallimento di controllo: fissa in anticipo il destino del prototipo e fai dello scartare un usa e getta riuscito un esito celebrato anziché uno spreco da evitare.

## Lente settoriale

**Startup.** Modella su una lavagna, fotografala e vai avanti. La tua risorsa più scarsa è l'attenzione ingegneristica, quindi ricorri a un modello solo quando costa meno dell'errore che previene: una macchina a stati degli abbonamenti prima di programmare i casi limite della fatturazione, non un intero catalogo UML per un prodotto che potrebbe cambiare direzione il mese prossimo. Resta euristico e agile, tieni i metodi formali del tutto fuori dal tavolo e tratta ogni prototipo come usa e getta a meno che tu non decida consapevolmente altrimenti.

**Piccola impresa.** Probabilmente non hai nessuno il cui lavoro sia la modellazione formale, quindi appoggiati ai modelli già incorporati negli strumenti e nei framework che acquisti anziché montare una pratica di modellazione tua. Imposta i pochi modelli che disegni attorno a decisioni concrete: un semplice schizzo del modello di dati per concordare quali dati dei clienti detieni, un diagramma di stato per l'unico flusso di lavoro che ti fa perdere un cliente quando si rompe. Preferisci un prodotto acquistato con un modello di dati collaudato a costruire e documentare il tuo e mantieni ciò che disegni abbastanza leggero da poter essere mantenuto da una sola persona.

**Grande impresa.** Il problema centrale è il coordinamento tra molti team, quindi i modelli condivisi diventano il terreno comune: un modello di dati concordato, una notazione coerente e un luogo in cui ERD, diagrammi C4 e macchine a stati possano essere trovati e creduti. Standardizza una piccola notazione e fai rispettare la coerenza, così che le entità di requisiti, progetto e database non si allontanino tra i team. Riserva specifica formale e verifica di modelli ai nuclei ad alta conseguenza (regolamento, riconciliazione, controllo degli accessi), finanzia la competenza specialistica che richiedono e mantieni una traccia di audit da ogni modello documentato alla decisione che ha giustificato.

**Ente pubblico.** Le regole fissate per legge devono essere riconducibili alla norma, ed è qui che la specifica formale si guadagna il costo: specifica con precisione la logica di ammissibilità o di accertamento, verifica proprietà chiave e lascia che gli auditor riconducano ogni esito alla regola che l'ha prodotto. Gli appalti aggiungono un peso proprio, poiché documenti e modelli sono spesso prodotti contrattuali da consegnare, quindi concorda quali modelli portano davvero decisioni anziché essere prodotti solo per soddisfare una lista di controllo. Pubblica descrizioni in linguaggio semplice di come funzionano i sistemi importanti e usa la prototipazione usa e getta per mettere alla prova con utenti reali l'accettazione delle domande rivolta ai cittadini prima di impegnarti in una costruzione di produzione.

## Esempi

**Startup.** Una piccola startup che costruisce un prodotto di fatturazione degli abbonamenti schizza il ciclo di vita dell'abbonamento (prova, attivo, scaduto, annullato, riattivato) come macchina a stati su una lavagna prima di scrivere codice. Ripercorrendo il diagramma, notano di non aver mai definito che cosa succede quando il pagamento di un account scaduto alla fine viene accreditato, un caso limite che avrebbe lasciato clienti reali in un limbo. Quel modello di cinque minuti risparmia un grattacapo in produzione, e lo fotografano anziché mantenere uno strumento pesante di diagrammi. Ovunque altrove restano agili e modellano quanto basta per allineare, perché alla loro scala un difetto è recuperabile e i metodi formali sarebbero puro costo.

**Grande impresa.** Una banca globale costruisce una nuova piattaforma di pagamenti. Il team usa un diagramma entità-relazione per concordare il modello di dati condiviso tra i team di conti, libro mastro e messaggistica, e diagrammi C4 (capitolo 3.1) per mostrare come i servizi si incastrano. Modellano il ciclo di vita della transazione (in sospeso, compensata, regolata, stornata, contestata) come macchina a stati esplicita, e l'analisi rivela che manca una transizione per gli storni parziali. La lacuna viene corretta su una lavagna anziché in produzione. I diagrammi di sequenza ripercorrono il flusso di regolamento rispetto ai requisiti (capitolo 2.8) per far emergere percorsi di timeout e ripetizione mancanti. La consegna quotidiana è agile, ma l'algoritmo centrale di riconciliazione, dove un errore significa denaro reale perso, riceve una specifica formale ed è verificato con un verificatore di modelli prima dell'implementazione. La modellazione è concentrata dove stanno denaro e ambiguità e tenuta leggera ovunque altrove.

**Ente pubblico.** Un'agenzia fiscale nazionale modernizza l'accertamento delle prestazioni. Poiché le regole di ammissibilità sono fissate per legge e sottoposte ad audit, il team scrive una specifica formale delle regole come trasformazioni pure e verifica proprietà chiave, come che nessun richiedente sia insieme ammissibile e non ammissibile e che ogni caso arrivi a una decisione, così che gli auditor possano ricondurre gli esiti alla norma. Accanto al nucleo formale, il team costruisce un prototipo usa e getta del modulo di accettazione rivolto ai cittadini da provare con utenti reali. Scoprono che una procedura guidata a più passaggi riduce gli errori, poi scartano il prototipo e ricostruiscono l'accettazione a standard di produzione. I diagrammi di attività documentano il processo del funzionario da un capo all'altro per formazione e audit. Alle regole ad alta conseguenza va il rigore formale; all'esperienza utente incerta va la prototipazione economica; nessun metodo è applicato dove appartiene all'altro.

## Business case: motivazioni, ROI e TCO

Il ritorno della modellazione viene dal trovare i difetti prima, dove costa molto meno correggerli. Una contraddizione trovata su una lavagna costa minuti. La stessa contraddizione trovata in produzione può costare un'interruzione, un programma di rifacimento o, nei domini regolamentati, una responsabilità legale. I modelli abbassano anche il costo totale di proprietà servendo come comunicazione durevole. Un sistema che sopravvive ai propri autori, il caso normale nei contesti aziendali e governativi, costa molto meno da mantenere quando il suo modello di dati, le sue macchine a stati e i suoi flussi chiave sono documentati con accuratezza.

I costi sono reali e vanno pesati. I modelli richiedono tempo per essere costruiti, competenza per essere costruiti bene e sforzo continuo per essere tenuti aggiornati; i metodi formali aggiungono lavoro specialistico. Il punto di pareggio è governato da incertezza e conseguenza. Dove entrambe sono basse, la modellazione pesante distrugge valore e vincono le euristiche agili. Dove una delle due è alta, la modellazione mirata e, per il nucleo critico, la verifica formale si ripagano molte volte prevenendo la classe costosa di fallimenti. Per sostenere il caso con la leadership, collega l'investimento di modellazione a rischi specifici ritirati e alla manutenibilità dei sistemi di lunga durata. E controlla se i modelli sono davvero consultati, perché un modello inutilizzato è puro costo.

## Antipattern e insidie

- **Modellare fine a se stessi:** produrre diagrammi perché un processo li richiede, non perché informano una decisione.
- **Modelli obsoleti creduti come verità:** diagrammi che non corrispondono più al codice ma su cui si fa ancora affidamento.
- **Grande progettazione iniziale:** modelli esaustivi prodotti prima di qualsiasi codice, che fissano decisioni prese con meno informazioni.
- **Proliferazione di diagrammi:** ogni tipo UML applicato uniformemente, che annega le poche viste utili nel rumore.
- **Metodi formali ovunque:** applicare una verifica costosa a codice dove le conseguenze di un fallimento non la giustificano.
- **Promozione accidentale del prototipo:** un prototipo usa e getta rilasciato in silenzio come prodotto.
- **Notazione al posto della sostanza:** discutere della correttezza UML anziché se il modello risponde alla domanda.

## Modello di maturità

- **Livello 1 (Avvio):** la modellazione è ad hoc o assente e puramente reattiva; nessun metodo è nominato; i modelli, quando sono disegnati, sono incoerenti, non analizzati e abbandonati appena finisce la riunione.
- **Livello 2 (Sviluppo):** alcuni team disegnano diagrammi comuni e seguono un metodo con un nome, ma la pratica è disomogenea nell'organizzazione: i modelli sono spesso prodotti in modo cerimoniale, si allontanano dal codice e raramente sono analizzati alla ricerca di difetti.
- **Livello 3 (Standardizzazione):** una notazione condivisa, una guida alla scelta del metodo documentata e regole di coerenza sono definite e fatte rispettare in tutta l'organizzazione; i modelli sono scelti per scopo, mantenuti allineati al sistema, rivisti alla ricerca di difetti e il metodo è adeguato al rischio di ciascun problema.
- **Livello 4 (Gestione):** la modellazione è misurata e controllata rispetto a valori di riferimento; i team seguono quanti difetti l'analisi coglie prima dell'implementazione, quanto i modelli si allontanano dal codice, se ogni modello sia stato davvero consultato per una decisione reale e il rifacimento e il tempo di ciclo risparmiati rispetto a un riferimento definito; la scelta del metodo è calibrata su incertezza e conseguenza misurate e i nuclei critici sono verificati formalmente rispetto a obiettivi di copertura concordati.
- **Livello 5 (Orchestrazione):** modellazione e scelta del metodo sono migliorate di continuo e integrate con la pianificazione di consegna e rischio in tutta l'organizzazione; l'investimento si adatta al mutare di incertezza e conseguenza, i modelli sono regolarmente mantenuti aggiornati, ritirati o approfonditi sulla base delle prove e i metodi formali, euristici e di prototipazione sono composti così che ciascuno stia esattamente dove rende.

## Spunti di discussione

- Per il vostro ultimo progetto, quali modelli hanno informato una decisione reale, e quali sono stati disegnati solo perché un processo lo richiedeva?
- Dove, nei vostri sistemi, una specifica formale si ripagherebbe, e dove sarebbe spreco?
- Come decidete se un prototipo è usa e getta o evolutivo, e fate rispettare quella decisione?
- Come impedite che i modelli si allontanino dal codice, o accettate che alcuni vadano eliminati invece?
- Qual è la giusta quantità di modellazione prima del codice nel vostro contesto, e come cambia con l'incertezza?
- Quale modello comportamentale (di stato, di sequenza o di attività) avrebbe colto il vostro più recente incidente in produzione?

## Punti chiave

- Un modello è un'astrazione con uno scopo; se non sai nominare la decisione che informa, non disegnarlo.
- Adegua modelli strutturali e comportamentali alla domanda specifica e mantienili coerenti e aggiornati.
- Analizza i modelli; un modello non verificato è un presupposto non testato.
- I metodi euristici e agili si adattano alla maggior parte dei sistemi; riserva i metodi formali ai nuclei ad alta conseguenza.
- Usa i prototipi per ritirare l'incertezza e decidi in anticipo se sono usa e getta o evolutivi.
- Investi nella modellazione in proporzione all'incertezza che risolve e al costo di sbagliare la decisione.

## Riferimenti e letture di approfondimento

- IEEE Computer Society, *SWEBOK Guide (Software Engineering Body of Knowledge), Version 4.0*, area di conoscenza Software Engineering Models and Methods
- Martin Fowler, *UML Distilled: A Brief Guide to the Standard Object Modelling Language*
- Grady Booch, James Rumbaugh, Ivar Jacobson, *The Unified Modelling Language User Guide*
- Frederick P. Brooks, *The Mythical Man-Month* e *No Silver Bullet: Essence and Accident in Software Engineering*
- Daniel Jackson, *Software Abstractions: Logic, Language, and Analysis* (il linguaggio di modellazione Alloy)
- Leslie Lamport, *Specifying Systems* (TLA+)
- Simon Brown, *Software Architecture for Developers* (il modello C4)
- David Harel, *Statecharts: A Visual Formalism for Complex Systems*
