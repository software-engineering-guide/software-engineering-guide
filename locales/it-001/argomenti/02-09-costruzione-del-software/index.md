# 2.9 Costruzione del software

## Panoramica e motivazioni

La [costruzione del software](https://en.wikipedia.org/wiki/Software_construction) è il momento in cui il progetto diventa codice in esecuzione. È il lavoro dettagliato di programmazione, verifica, [test unitari](https://en.wikipedia.org/wiki/Unit_testing), [test di integrazione](https://en.wikipedia.org/wiki/Integration_testing) e [debug](https://en.wikipedia.org/wiki/Debugging). La Guida dello [Software Engineering Body of Knowledge](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) (SWEBOK) tratta la costruzione come un'area di conoscenza a sé, e a ragione: è qui che avviene la maggior parte del tuo lavoro quotidiano. Le scelte che fai riga per riga (come contieni la complessità, come gestisci gli errori, quanto leggibili lasci le cose) decidono se un sistema potrà essere capito, modificato e di cui ci si potrà fidare per gli anni a venire.

In un grande team, la costruzione è uno sforzo di gruppo, non solitario. Centinaia di ingegneri scrivono in una base di codice condivisa che sopravviverà alla permanenza di qualsiasi persona nel team. Quindi la soglia non è "funziona sulla mia macchina oggi". È "uno sconosciuto può modificarlo in sicurezza fra cinque anni". La costruzione si collega verso monte ai requisiti (capitolo 2.8) e al progetto (capitolo 2.2), che ti dicono che cosa costruire e quale forma abbia. Si collega di lato a standard di codifica (capitolo 2.1), testing (capitolo 2.4) e revisione del codice (capitolo 2.5), che plasmano come il lavoro viene espresso, verificato e ispezionato. Una buona costruzione trasforma un progetto solido in una risorsa manutenibile. Una cattiva costruzione trasforma anche un buon progetto in una passività.

Nei contesti aziendali e governativi la costruzione ha un peso aggiuntivo. Questi sistemi sono di lunga durata, fortemente regolamentati e spesso critici per la sicurezza o per i cittadini. La [programmazione difensiva](https://en.wikipedia.org/wiki/Defensive_programming), una gestione disciplinata degli errori e un codice evidentemente corretto non sono finezze qui; sono requisiti di garanzia, audit e continuità attraverso decenni e ricambio del personale. L'obiettivo è un codice che comunica il proprio intento, resiste al fallimento e può essere verificato. Un codice che gira soltanto non basta.

## Principi chiave

- Riduci la complessità al massimo; il principale nemico della costruzione su larga scala è il codice che nessuno riesce a comprendere del tutto.
- Anticipa il cambiamento; costruisci in modo che le probabili modifiche future siano localizzate ed economiche.
- Costruisci per la verifica; scrivi codice la cui correttezza sia facile da controllare con test, revisione e ragionamento.
- Riusa con deliberazione; costruisci su componenti esistenti e affidabili anziché reinventare, ma evita l'accoppiamento con le astrazioni sbagliate.
- Segui gli standard; la coerenza in una base di codice riduce il costo cognitivo di ogni modifica futura.
- Gestisci errori e stati non validi in modo esplicito; rendi visibili le modalità di fallimento anziché silenziose.
- Mantieni leggibile il codice; la costruzione è prima di tutto comunicazione con i futuri manutentori e solo poi con il compilatore.

## Raccomandazioni

### Riduci la complessità come disciplina primaria

Fai della riduzione della complessità, sia essenziale sia accidentale, il tuo obiettivo centrale. Scrivi funzioni e moduli piccoli e con un solo scopo. Preferisci nomi chiari a trucchi ingegnosi. Mantieni superficiale l'annidamento e lineare il flusso di controllo. Localizza le decisioni, così che capire un pezzo di codice non ti costringa a tenere a mente l'intero sistema. La complessità è ciò che rende le grandi basi di codice lente da modificare e pericolose da toccare, quindi pesa ogni scelta in base a se aggiunge complessità o la toglie. Applica anche in piccolo i principi di progettazione del capitolo 2.2: alta coesione, basso accoppiamento e una chiara [separazione delle responsabilità](https://en.wikipedia.org/wiki/Separation_of_concerns) contano tanto in una singola funzione quanto in un'architettura.

### Costruisci per il cambiamento e per la verifica

Pensa in anticipo ai cambiamenti più probabili (nuove regole di business, nuove integrazioni, nuove normative) e isolali dietro interfacce stabili così che il cambiamento resti locale. Allo stesso tempo, scrivi codice facile da verificare: [funzioni pure](https://en.wikipedia.org/wiki/Pure_function) (gli stessi input danno sempre lo stesso output, senza effetti collaterali) dove puoi, stato nascosto minimo e dipendenze rese esplicite così che i test possano sostituirle. Il codice difficile da testare è di solito codice difficile da capire e da cambiare. La testabilità (capitolo 2.4) è un segnale di progetto, non solo una questione di QA.

### Riusa con deliberazione e standardizza

Ricorri a librerie e componenti interni ben mantenuti e affidabili prima di riscrivere logica di base e usali attraverso interfacce chiare (capitolo 2.3). Costruisci componenti riutilizzabili solo quando esiste un vero secondo caso d'uso, perché generalizzare troppo presto è di per sé una forma di complessità. Applica in modo uniforme gli standard di codifica e di stile della tua organizzazione (capitolo 2.1), idealmente fatti rispettare da formattatori e [linter](https://en.wikipedia.org/wiki/Lint_(software)) automatici, così che l'intera base di codice si legga come se l'avesse scritta un solo autore attento.

### Pratica la programmazione difensiva con giudizio

Valida gli input ai confini di fiducia (richieste esterne, I/O di file e di rete, input utente) e tratta qualsiasi dato che attraversa quei confini come ostile finché non è provato il contrario. All'interno di un modulo ben testato, però, non soffocare ogni riga in controlli ridondanti che nascondono la logica e sopprimono i fallimenti reali. La regola è semplice: difenditi ai confini, fidati all'interno. Usa le [asserzioni](https://en.wikipedia.org/wiki/Assertion_(software_development)) per documentare e far rispettare invarianti che non dovrebbero mai essere false in un programma corretto. Usa [eccezioni](https://en.wikipedia.org/wiki/Exception_handling) e gestione degli errori per condizioni che possono legittimamente verificarsi a runtime. Tieni separati i due: le asserzioni proteggono i presupposti del programmatore, la gestione degli errori gestisce il fallimento atteso.

### Gestisci gli errori in modo esplicito e fallisci in sicurezza

Per ogni errore, decidi con deliberazione che cosa fare: riprendersi, riprovare, propagare o fallire subito. Non inghiottire mai in silenzio un'eccezione né ignorare un errore restituito; un fallimento soppresso ritorna più tardi come un difetto misterioso. Mantieni il contesto nei messaggi di errore e nei log così che i fallimenti possano essere diagnosticati. Nei sistemi critici per la sicurezza e per i cittadini, fallisci verso uno stato sicuro e noto anziché continuare in uno corrotto. Dedica al percorso d'errore tanta attenzione quanta al percorso felice, perché in produzione è nel percorso d'errore che la fiducia si vince o si perde.

### Incorpora la qualità durante la costruzione

La qualità si costruisce dentro, non si ispeziona a posteriori. Scrivi test unitari insieme al codice, esegui di continuo [analisi statica](https://en.wikipedia.org/wiki/Static_program_analysis) e linter e tieni le funzioni abbastanza piccole da poterci ragionare. Usa nomi e struttura autoesplicativi così che i tuoi commenti possano spiegare perché, non che cosa. Fai [refactoring](https://en.wikipedia.org/wiki/Code_refactoring) strada facendo per mantenere abitabile il codice. La revisione del codice (capitolo 2.5) è la rete di protezione umana, ma gran parte della qualità deve esserci prima ancora che la revisione cominci.

### Scegli e standardizza gli strumenti di costruzione

Standardizza la catena di strumenti (compilatori, sistemi di build, formattatori, linter, analizzatori statici, debugger, gestori di dipendenze e configurazioni dell'IDE) così che ogni ingegnere lavori in un ambiente coerente e riproducibile. Collega questi strumenti alla pipeline così che i controlli di qualità non siano facoltativi. Introduci con deliberazione gli strumenti di programmazione assistiti dall'IA e tratta il loro output come una bozza che deve superare gli stessi standard, la stessa revisione e gli stessi test di qualsiasi altro codice.

## Compromessi: vantaggi e svantaggi

| Pratica | Vantaggi | Svantaggi |
|---|---|---|
| Riduzione aggressiva della complessità | Leggibile, modificabile, basso tasso di difetti | Può sembrare lenta; rischia sovra-astrazione se mal applicata |
| Ampi controlli difensivi | Coglie presto gli stati errati, confini solidi | Ingombra la logica; può mascherare bug reali se esagerata |
| Asserzioni per le invarianti | Documenta e fa rispettare i presupposti | Disattivate in alcune build di produzione; non sono gestione degli errori |
| Largo riuso di librerie | Meno codice da possedere; consegna più rapida | Rischio di dipendenza, accoppiamento, esposizione alla supply chain |
| Standard e linting rigorosi | Base di codice uniforme e a basso attrito | Preparazione iniziale; può sembrare rigido ai singoli |
| Costruire per la testabilità | Codice verificabile e modificabile | Può aggiungere indirezione che alcuni vedono come cerimonia |

Il compromesso centrale nella costruzione è tra velocità a breve termine e modificabilità a lungo termine. Prendere scorciatoie (saltare la gestione degli errori, tollerare la complessità, ignorare gli standard) sembra più veloce sul momento, ed è quasi sempre più costoso nella vita del sistema. Il fallimento opposto è la sovra-ingegnerizzazione: troppa difensività, astrazione speculativa e generalità di cui nessuno ha bisogno. La costruzione competente sta nel mezzo: il più semplice possibile, difensiva quanto richiedono i confini e non di più.

## Domande da discutere con il tuo team

1. **Qual è la nostra definizione condivisa e concreta di "troppo complesso", e dove la facciamo rispettare prima dell'integrazione?** "Riduci la complessità" è la disciplina centrale della costruzione, ma come slogan perde ogni discussione contro una scadenza. In un grande team in cui centinaia di persone scrivono in un'unica base di codice, la complessità deve essere misurabile, quindi concorda segnali su cui agirai davvero: lunghezza delle funzioni, profondità di annidamento, complessità ciclomatica e il numero di cose che un lettore deve tenere a mente per capire una modifica. Porta alla riunione il tuo peggior trasgressore e chiediti se la tua attuale revisione l'avrebbe colto. La risposta dovrebbe diventare un cancello nella pipeline o una voce di lista di controllo della revisione, perché una soglia fatta rispettare da uno strumento vale più di un principio fatto rispettare dalla forza di volontà, e risparmia al tuo prossimo assunto il lento accumulo di codice che nessuno può toccare in sicurezza.

2. **In produzione, i nostri percorsi d'errore si comportano come li abbiamo progettati, e quando ne abbiamo esercitato uno di proposito l'ultima volta?** Il consiglio sulla costruzione dice di dedicare al percorso d'errore tanta attenzione quanta al percorso felice, eppure il percorso d'errore è di solito il codice meno testato che possiedi, e in un sistema critico per i cittadini o per la sicurezza è dove la fiducia si vince o si perde. Un'eccezione soppressa o un codice di ritorno ignorato diventa settimane dopo un difetto misterioso, e "fallire verso uno stato sicuro" è una promessa che non puoi mantenere se non l'hai mai vista accadere. Porta la tua storia degli incidenti: quante interruzioni passate sono riconducibili a un errore inghiottito o a un percorso di ripristino non testato? L'azione è testare il fallimento di proposito (inietta la carta rifiutata, il timeout, l'input malformato) e richiedere che ogni errore sia gestito, registrato con contesto o propagato, mai scartato in silenzio.

3. **Quali parti della nostra base di codice sono difficili da testare, e che cosa ci dice quella difficoltà sul progetto?** Il codice che resiste al testing è quasi sempre codice che nasconde stato, si accoppia alle dipendenze sbagliate o fa troppo, quindi la testabilità è un segnale di progetto, non un ripensamento di QA. In un sistema aziendale di lunga durata questo conta perché i moduli che oggi sono dolorosi da testare sono quelli che uno sconosciuto avrà paura di modificare fra cinque anni. Porta la classe o il servizio per cui il tuo team teme di scrivere test e chiediti perché: lo stato è nascosto, le dipendenze sono impossibili da sostituire, la funzione fa tre lavori? La risposta dovrebbe guidare il refactoring verso funzioni pure, dipendenze esplicite e piccole unità con un solo scopo, perché rendere verificabile il codice è lo stesso lavoro che renderlo comprensibile ed economico da modificare.

4. **Quando riusiamo una libreria esterna rispetto a costruire noi la capacità, e chi possiede il rischio di supply chain che ci assumiamo?** Ricorrere a una libreria affidabile è più rapido che reinventare la logica di base, eppure ogni dipendenza che aggiungi è codice che non controlli, che non puoi verificare con facilità e che devi correggere il giorno in cui viene compromesso. In un grande team il pericolo è che cento ingegneri portino ciascuno le proprie dipendenze transitive finché nessuno sa dire che cosa la base di codice esegua davvero. Porta il tuo inventario delle dipendenze e chiediti tre cose concrete: quante librerie non sono più mantenute, quante portano vulnerabilità note e quante racchiudono una logica abbastanza semplice da possedere in proprio. La considerazione contraria è reale, perché scrivere in proprio crittografia o gestione delle date è quasi sempre peggio di una libreria collaudata, quindi l'obiettivo è una politica di riuso deliberata anziché l'evitamento generalizzato. Nei contesti aziendali e governativi, aggiungi l'angolo degli appalti e della conformità delle licenze, poiché una dipendenza non verificata può portare una licenza incompatibile con i tuoi obblighi o una provenienza che nessun auditor accetterà.

5. **Come sottoponiamo il codice generato dall'IA agli stessi standard di costruzione del codice scritto da persone, e riusciamo a distinguere i due quando conta?** Gli assistenti di programmazione IA producono bozze plausibili in fretta, e la tentazione è trattare il loro output come finito perché compila e appare idiomatico. La regola del capitolo è che il codice generato supera la stessa revisione, gli stessi test e gli stessi standard di qualsiasi altro, e un grande team deve rendere operativa quella regola anziché aspirazionale. Porta esempi di modifiche assistite dall'IA rilasciate di recente e chiediti se ciascuna portava test, ha superato l'analisi statica ed è stata davvero capita dalla persona che l'ha sottoposta, o se è stata fatta passare sulla fiducia. La pressione contraria è la velocità, perché questi assistenti sono davvero produttivi e rallentare a passo di lumaca ogni suggerimento spreca il beneficio. Nei contesti regolamentati e governativi, aggiungi l'angolo della provenienza e della responsabilità, perché potresti dover attestare chi è responsabile di una riga di codice e se un frammento generato porti una questione di licenza o di diritto d'autore a cui non sai rispondere.

6. **La nostra catena di strumenti di costruzione è davvero standardizzata e fatta rispettare nella pipeline, o i singoli lavorano ancora in configurazioni incompatibili?** Una catena di strumenti condivisa di formattatore, linter, analizzatore statico, sistema di build e gestore di dipendenze permette a un ingegnere di muoversi con fiducia tra servizi sconosciuti, perché il codice si legge con una sola voce e i controlli sono identici ovunque. Quando deriva, ogni team reinventa la propria configurazione, il tempo di revisione si spende a discutere di stile e i difetti che l'analizzatore di un team avrebbe colto sfuggono in un altro. Porta l'elenco dei repository che non eseguono i controlli standard a ogni commit e chiediti perché ciascuno se ne sia tirato fuori. La tensione è che un'unica configurazione imposta può sembrare rigida ai team con esigenze davvero diverse, quindi decidi dove l'uniformità vale l'attrito e dove un'eccezione documentata va bene. Per una grande impresa o un ente pubblico, collega questo a riproducibilità e audit, perché una build che non puoi riprodurre byte per byte da una catena di strumenti controllata è una build che non potrai difendere davanti a un valutatore anni dopo.

## Lente settoriale

**Startup.** Vince la velocità, quindi metti al primo giorno un formattatore e un linter condivisi, valida gli input al tuo unico confine esterno e mantieni pulito il codice interno anziché difensivo a ogni riga. Salta l'astrazione speculativa e il processo pesante: con due o tre ingegneri l'intero team tiene a mente la base di codice, e il vero rischio è una complessità che sopravvive a quella memoria condivisa. Appoggiati a librerie affidabili per tutto ciò che è di base, così da scrivere meno codice possibile da possedere bene.

**Piccola impresa.** Senza un ingegnere di build dedicato e con un budget ridotto, preferisci le convenzioni che i tuoi strumenti esistenti fanno rispettare gratis: un formattatore e un linter forniti con il linguaggio, impostazioni predefinite sensate e un piccolo insieme di regole che tutti possano ricordare. Compra o adotta librerie ben mantenute anziché costruire infrastruttura che non hai personale per mantenere. Spendi la tua limitata disciplina sulle due cose che fanno più male se trascurate: validare l'input al confine e non inghiottire mai un errore in silenzio.

**Grande impresa.** Con centinaia di ingegneri che scrivono in codice condiviso, la priorità è uniformità e applicazione: una catena di strumenti standard collegata alla pipeline, cancelli di analisi statica e regole di validazione ai confini applicate ovunque, così che le persone si muovano con fiducia tra i servizi. Gestisci il rischio di dipendenze e supply chain come un processo governato anziché un'improvvisazione per team e usa le asserzioni per codificare invarianti di dominio che devono valere per ogni team. Tratta gli standard di costruzione come il substrato che mantiene abitabile una base di codice attraverso decenni e ricambio del personale.

**Ente pubblico.** Sistemi di lunga durata e critici per i cittadini fanno della costruzione disciplinata una questione di garanzia e di responsabilità. Isola dietro interfacce stabili le regole volatili come la legislazione, così che il cambiamento resti locale e riconducibile ai requisiti, fallisci verso stati sicuri e noti anziché continuare in uno corrotto e consegna ogni modulo con test che fanno anche da evidenza di audit. Gli obblighi di appalto e trasparenza significano che la tua catena di strumenti, le dipendenze e la gestione degli errori devono essere documentate abbastanza bene da permettere a un dipendente pubblico che arriva anni dopo, o a un auditor esterno, di verificare che il codice sia corretto.

## Esempi

**Startup.** Una startup di tre ingegneri imposta fin dal primo giorno un formattatore e un linter condivisi e li esegue a ogni commit, così che la base di codice si legga con una sola voce anche man mano che aggiungono collaboratori esterni. Validano gli input al confine dell'API e trattano tutto ciò che viene da fuori come ostile, ma mantengono pulita la logica interna anziché soffocarla in controlli ridondanti. Quando un webhook di pagamento comincia a fallire, la correzione è rapida perché nessuna eccezione è mai stata inghiottita in silenzio e il messaggio d'errore porta contesto sufficiente per puntare dritto alla causa. L'intera impostazione ha richiesto un pomeriggio e ha risparmiato loro il lento accumulo di complessità che avrebbe reso penosa la prima settimana del loro prossimo assunto.

**Grande impresa.** Una società globale di pagamenti fa rispettare una catena di strumenti condivisa tra centinaia di ingegneri: formattazione e linting automatici a ogni commit, cancelli di analisi statica nella pipeline e una regola per cui tutti gli input esterni sono validati ai confini dei servizi. La logica di dominio usa asserzioni per far rispettare invarianti come "una registrazione contabile quadra sempre", mentre le condizioni a runtime come una carta rifiutata sono gestite come esiti espliciti e registrati. Poiché gli standard sono uniformi e gli errori non vengono mai inghiottiti in silenzio, gli ingegneri si muovono con fiducia tra servizi sconosciuti e gli incidenti in produzione possono essere diagnosticati direttamente dai log.

**Ente pubblico.** Un'agenzia fiscale nazionale costruisce un sistema di accertamento di lunga durata che dovrebbe funzionare per decenni sotto una legislazione mutevole. La costruzione isola ogni regola fiscale dietro un'interfaccia stabile, così che i cambiamenti legislativi annuali restino locali e riconducibili ai requisiti (capitolo 2.8). La validazione difensiva protegge ogni input rivolto ai cittadini. I percorsi d'errore falliscono verso uno stato sicuro che non emette mai in silenzio un accertamento errato. Ogni modulo è consegnato con test unitari come evidenza di audit. Poiché la costruzione è standardizzata e ben documentata, i nuovi dipendenti pubblici possono mantenere in sicurezza codice scritto da predecessori che se ne sono andati da tempo.

## Business case: motivazioni, ROI e TCO

Il ritorno di una costruzione disciplinata è la capacità duratura di cambiare il software in modo economico e sicuro, ed è lì che si decide la maggior parte del costo totale di proprietà di un sistema. Gli studi di economia del software mostrano in modo costante che la maggior parte del costo di un sistema nel corso della sua vita è manutenzione, e il costo di manutenzione è dominato da quanto il codice è comprensibile e modificabile. Ridurre la complessità, gestire gli errori in modo esplicito e seguire gli standard abbassa direttamente il costo di ogni modifica futura e di ogni incidente in produzione.

Il costo di adozione è modesto e soprattutto iniziale: fissare gli standard, collegare linter e analizzatori e costruire l'abitudine di scrivere codice verificabile e difensivo. Il costo della trascuratezza, invece, si accumula. La complessità si accumula in codice lento da modificare e rischioso da toccare. Gli errori silenziosi diventano costosi incidenti in produzione. Uno stile incoerente moltiplica lo sforzo di ogni revisione e di ogni inserimento. Per sostenere il caso con la leadership, collega la qualità della costruzione al tasso di fallimento delle modifiche, al tempo medio di ripristino, al tasso di difetti sfuggiti e al tempo di inserimento, tutti migliorati direttamente dalla disciplina di costruzione.

## Antipattern e insidie

- **Deriva verso la complessità:** accumulare codice ingegnoso, profondamente annidato o sconfinato finché nessuno lo capisce.
- **Errori inghiottiti in silenzio:** blocchi catch vuoti e codici di ritorno ignorati che trasformano i fallimenti in misteri futuri.
- **Eccesso di programmazione difensiva:** controlli ridondanti ovunque che seppelliscono la logica e mascherano difetti reali.
- **Confondere asserzioni e gestione degli errori:** usare asserzioni per condizioni a runtime, o eccezioni per invarianti del programmatore.
- **Costruzione per copia e incolla:** duplicare la logica anziché riusarla, così che le correzioni vadano fatte in molti posti.
- **Generalità speculativa:** costruire astrazioni e configurabilità per esigenze che non arrivano mai.
- **Ignorare gli standard:** ogni ingegnere che programma a modo proprio, moltiplicando il carico cognitivo in tutta la base di codice.
- **Costruzione non testata:** scrivere codice senza test di accompagnamento, rinviando la verifica a una fase che non arriva mai.

## Modello di maturità

- **Livello 1 (Avvio):** la costruzione è ad hoc e reattiva; complessità e gestione degli errori variano per individuo; esistono pochi standard e i fallimenti silenziosi sono comuni.
- **Livello 2 (Sviluppo):** esistono standard di codifica, formattatori e linter, e si attendono una gestione degli errori di base e test unitari, ma la pratica è incoerente e ogni team la applica in modo diverso.
- **Livello 3 (Standardizzazione):** riduzione della complessità, validazione ai confini, gestione esplicita degli errori e testabilità sono documentate e fatte rispettare in tutta l'organizzazione, nella pipeline e in revisione, così che l'intera base di codice si legga come se l'avesse scritta un solo autore attento.
- **Livello 4 (Gestione):** la qualità della costruzione è misurata rispetto a valori di riferimento; il team segue complessità ciclomatica, tasso di difetti sfuggiti, tasso di fallimento delle modifiche, copertura di test dei percorsi d'errore e rilievi della revisione del codice, e agisce sugli andamenti anziché sulle opinioni.
- **Livello 5 (Orchestrazione):** la costruzione è migliorata di continuo e integrata in tutta l'organizzazione; pattern difensivi, standard e metriche alimentano refactoring e strumenti; gli strumenti assistiti dall'IA operano sotto gli stessi cancelli di qualità e la pratica si adatta al mutare di linguaggi, normative e rischi.

## Spunti di discussione

- Dove si accumula più complessità accidentale nella vostra base di codice, e quali abitudini di costruzione la creano?
- Qual è la regola effettiva del vostro team su dove validare gli input e dove fidarsi?
- I vostri ingegneri distinguono le asserzioni dalla gestione degli errori, ed è una distinzione coerente?
- Quanta della vostra qualità è incorporata durante la costruzione rispetto a colta più tardi in revisione o nei test?
- Come decidete quando riusare una libreria rispetto a costruire, dato il rischio di supply chain?
- Come dovrebbe il codice generato dall'IA essere sottoposto agli stessi standard di costruzione del codice scritto da persone?

## Punti chiave

- La costruzione è dove il progetto diventa codice manutenibile; ridurre la complessità è la sua disciplina centrale.
- Costruisci per il cambiamento e per la verifica: il codice testabile e modificabile è codice comprensibile.
- Difenditi ai confini di fiducia, fidati al loro interno e non inghiottire mai errori in silenzio.
- Usa le asserzioni per le invarianti e la gestione degli errori per le condizioni attese a runtime; non confonderle.
- Standardizza strumenti e stile, riusa con deliberazione e costruisci dentro la qualità anziché ispezionarla a posteriori.

## Riferimenti e letture di approfondimento

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, area di conoscenza Software Construction
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt e David Thomas, *The Pragmatic Programmer*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code*
- John Ousterhout, *A Philosophy of Software Design*
