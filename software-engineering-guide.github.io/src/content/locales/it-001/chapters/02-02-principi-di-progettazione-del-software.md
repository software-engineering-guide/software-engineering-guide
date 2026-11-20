# 2.2 Principi di progettazione del software

## Panoramica e motivazioni

I principi di progettazione del software sono euristiche per disporre il codice in modo da poterlo capire, modificare ed estendere nel tempo. Comprendono acronimi con un nome ([SOLID](https://en.wikipedia.org/wiki/SOLID) per cinque principi di progettazione [orientata agli oggetti](https://en.wikipedia.org/wiki/Object-oriented_programming), [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) per don't-repeat-yourself, [KISS](https://en.wikipedia.org/wiki/KISS_principle) per keep-it-simple, [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) per you-aren't-gonna-need-it), concetti strutturali ([accoppiamento](https://en.wikipedia.org/wiki/Coupling_(computer_programming)), [coesione](https://en.wikipedia.org/wiki/Cohesion_(computer_science)), [separazione delle responsabilità](https://en.wikipedia.org/wiki/Separation_of_concerns)), [design pattern](https://en.wikipedia.org/wiki/Software_design_pattern) catalogati, approcci di modellazione di livello più alto come il [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design) (modellare il software nel linguaggio del dominio di business) e la scelta tra stili orientati agli oggetti, [funzionali](https://en.wikipedia.org/wiki/Functional_programming) e [orientati ai dati](https://en.wikipedia.org/wiki/Data-oriented_design). Nessuno di questi è una legge. Sono esperienza compressa, e vanno applicati con giudizio.

Per i grandi team il valore dei principi condivisi è il coordinamento. Quando centinaia di ingegneri lavorano sullo stesso sistema, hanno bisogno di un vocabolario comune per le discussioni di progetto e di un insieme comune di valori predefiniti, così che moduli scritti in modo indipendente combacino. Un buon progetto è ciò che permette a molte persone di cambiare un sistema in parallelo senza continue collisioni. È anche ciò che mantiene un sistema modificabile dieci anni dopo, la durata normale dei sistemi aziendali e governativi, ben oltre la permanenza degli autori originali.

La capacità critica non è memorizzare i principi. È sapere quando ciascuno di essi fuorvia. Ogni principio ha una modalità di fallimento: DRY può produrre l'astrazione sbagliata, SOLID può produrre indirezione inutile, YAGNI può affamare un'estensibilità di cui hai davvero bisogno. Questo capitolo tratta i principi come strumenti con un ambito di applicabilità, e dà risalto ad accoppiamento e coesione come proprietà più profonde che gli acronimi cercano di servire.

## Principi chiave

- Gestisci prima accoppiamento e coesione; la maggior parte dei principi con un nome sono modi indiretti di migliorare queste due proprietà.
- Ottimizza per il cambiamento: un buon progetto minimizza il costo delle modifiche che dovrai davvero fare.
- Preferisci il progetto più semplice che funziona ora, ma mantieni i confini dove il cambiamento è probabile.
- La duplicazione costa meno dell'astrazione sbagliata; aspetta che lo schema sia chiaro.
- Rendi esplicite le dipendenze e puntale verso ciò che è stabile.
- Modella il dominio nel linguaggio del dominio; allinea i confini del software ai confini del business.
- Scegli i paradigmi in base al problema, non all'ideologia; la maggior parte dei grandi sistemi è pragmaticamente mista.

## Raccomandazioni

### Usa SOLID come lente, non come lista di controllo

Applica la responsabilità singola per mantenere coesi i moduli, l'inversione delle dipendenze per puntare le dipendenze verso astrazioni dove esiste davvero un confine e l'aperto-chiuso dove i punti di estensione sono reali. Non fabbricare interfacce, factory e livelli solo per soddisfare l'acronimo quando c'è una sola implementazione e nessuna seconda in vista. L'indirezione ha un costo, e lo paghi a ogni lettura.

### Applica DRY alla conoscenza, non al testo

DRY riguarda il non duplicare un singolo pezzo autorevole di *conoscenza*. Non riguarda l'eliminare righe che si somigliano soltanto. Due pezzi di codice che sembrano simili ma cambiano per ragioni diverse dovrebbero restare separati. Preferisci un po' di duplicazione a un'astrazione condivisa prematura che accoppia cose non correlate. Estrai l'astrazione quando lo schema reale si è presentato due o tre volte.

### Lascia che KISS e YAGNI resistano alla speculazione

Costruisci per i requisiti che hai, non per quelli che immagini. Evita la generalità speculativa, come framework configurabili, sistemi di plugin e punti di estensione che nessuno ha chiesto. Il contrappeso è che una certa flessibilità costa davvero meno se inserita presto, come un'interfaccia stabile o una giuntura pulita. YAGNI argomenta contro l'*implementazione* speculativa, non contro i confini ponderati.

### Progetta esplicitamente per basso accoppiamento e alta coesione

Fai fare a ogni modulo una sola cosa ben definita (coesione) e fallo dipendere dal minor numero possibile di altri moduli, attraverso interfacce strette (basso accoppiamento). Quando rivedi un progetto, chiediti quali modifiche si propagano oltre i confini dei moduli. Quelle propagazioni sono la vera misura dell'accoppiamento. La separazione delle responsabilità è la stessa idea applicata a livelli e questioni trasversali.

### Usa i design pattern come vocabolario, applica gli antipattern come avvertimenti

I pattern sono nomi condivisi utili per soluzioni ricorrenti. Ricorri a uno quando il problema gli corrisponde davvero. Non imporre pattern per sembrare sofisticato, perché il codice denso di pattern è spesso segno di sovraingegnerizzazione. Impara i comuni [antipattern](https://en.wikipedia.org/wiki/Anti-pattern) (oggetti onnipotenti, modelli anemici dove non appropriati, grandi palle di fango, monoliti distribuiti) come etichette diagnostiche.

### Adotta il Domain-Driven Design dove il dominio è complesso

Per sistemi con ricche regole di business, usa gli strumenti tattici e strategici del DDD: un linguaggio onnipresente condiviso con gli esperti di dominio, contesti delimitati che dividono il sistema in parti modellate in modo indipendente e mappe dei contesti che descrivono come quelle parti si relazionano. I contesti delimitati sono particolarmente preziosi su scala aziendale, perché allineano la responsabilità dei team ai confini dei modelli. Il DDD è eccessivo per semplici sistemi [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) (create, read, update, delete: creare, leggere, aggiornare, eliminare).

### Scegli i paradigmi per adeguatezza

Usa l'orientamento agli oggetti per incapsulare comportamenti con stato e modellare domini. Usa lo stile funzionale per trasformazioni, concorrenza e prevedibilità attraverso l'[immutabilità](https://en.wikipedia.org/wiki/Immutable_object). Usa la progettazione orientata ai dati dove dominano prestazioni e comportamento della cache. I grandi sistemi li mescolano tutti e tre. Fai la scelta per componente e mantieni puliti i confini tra gli stili.

## Compromessi: vantaggi e svantaggi

| Principio / approccio | Applicato bene | Modalità di fallimento |
|---|---|---|
| SOLID | Giunture chiare dove avviene il cambiamento; unità testabili | Proliferazione di interfacce e livelli; indirezione senza ritorno |
| DRY | Unica fonte di verità per la conoscenza reale | L'astrazione sbagliata accoppia codice non correlato |
| KISS / YAGNI | Sistemi snelli e comprensibili | Giunture sotto-progettate; costosi adeguamenti per flessibilità necessaria |
| Design pattern | Vocabolario condiviso; strutture collaudate | Culto dei pattern; complessità accidentale |
| Domain-Driven Design | Modelli e team allineati; complessità domata | Pesante cerimonia su domini semplici; confini di contesto sbagliati |
| Funzionale / immutabile | Prevedibilità; concorrenza più sicura | Adattamento scomodo a problemi intrinsecamente con stato; sorprese di prestazioni |

La tensione ricorrente è tra sotto-progettazione e sovra-progettazione. I sistemi sotto-progettati accumulano accoppiamento e diventano rigidi. I sistemi sovra-progettati affogano nell'astrazione che qualcuno deve capire e mantenere. La risposta non è un punto fisso. È una disciplina: rinviare le decisioni finché hai informazioni sufficienti, mantenendo le giunture che ti permettono di cambiare idea.

## Domande da discutere con il tuo team

1. **Qual è la vostra soglia concreta per estrarre un'astrazione condivisa, e come impedite a DRY di produrre quella sbagliata?** Questo capitolo è netto nel dire che la duplicazione costa meno dell'astrazione sbagliata e che dovresti aspettare che lo schema sia comparso due o tre volte prima di estrarre. In un grande team il pericolo è che qualcuno fattorizzi due frammenti simili in un modulo condiviso oltre i confini dei team, e poi ogni modifica futura a un chiamante si propaghi all'altro. Il segnale da portare è se i duplicati cambiano per la stessa ragione o si somigliano soltanto adesso. Concorda una regola del tre e richiedi che un'astrazione candidata sia davvero cambiata insieme prima di accoppiare i chiamanti. Quel singolo accordo previene una classe di accoppiamento costosa da sciogliere una volta che molti team ne dipendono.

2. **Come rendete visibili accoppiamento e coesione nella revisione del progetto anziché lasciarli all'intuito?** I principi chiave pongono accoppiamento e coesione sopra ogni acronimo e definiscono l'accoppiamento come le modifiche che si propagano oltre i confini dei moduli. L'intuito non scala su centinaia di ingegneri che vedono ciascuno solo il proprio angolo del sistema. Porta prove che una macchina può produrre: grafi delle dipendenze e dati di co-modifica che mostrano quali moduli vengono continuamente modificati insieme negli stessi commit. Aggiungi una domanda di revisione esplicita che chieda quali confini di modulo una modifica ti costringe ad attraversare. Quando due moduli cambiano sempre insieme, è il segnale per unirli o per correggere il confine tra loro.

3. **Dov'è, nei vostri sistemi, la linea tra un dominio abbastanza ricco da giustificare il Domain-Driven Design e una semplice applicazione CRUD in cui è eccessivo?** Il capitolo raccomanda i contesti delimitati del DDD proprio perché allineano la responsabilità dei team ai confini dei modelli, e avverte che il DDD è eccessivo per semplici sistemi di creazione, lettura, aggiornamento ed eliminazione e degrada in cerimonia senza vera modellazione. Sbagliare in entrambe le direzioni è costoso: un DDD pesante su un dominio sottile seppellisce un'applicazione semplice nella cerimonia, mentre un modello condiviso esteso tra molti team impone un continuo coordinamento tra team. Porta i segnali che decidono davvero: la densità delle regole di business e quanti team hanno bisogno di possedere parti in modo indipendente. Riserva il macchinario strategico al nucleo complesso e lascia semplici i margini semplici. Così eviti sia il teatro del DDD sia la grande palla di fango.

4. **Quando un'astrazione, un'interfaccia o un design pattern vale l'indirezione che aggiunge, e chi ha l'autorità di dichiarare un progetto sovra-ingegnerizzato?** Questo capitolo è esplicito nel dire che l'indirezione ha un costo che si paga a ogni lettura e che fabbricare interfacce, factory e livelli per soddisfare SOLID o per sembrare sofisticati è una modalità di fallimento. In un grande team la pressione va nell'altra direzione: i revisori lasciano passare astrazione in più perché sembra disciplina, e nessuno vuole essere quello che sostiene meno struttura. La considerazione contraria è reale, perché alcune giunture si guadagnano davvero il posto e toglierle in seguito è costoso. Porta alla discussione prove concrete: quante implementazioni ha oggi un'interfaccia, quante volte il punto di estensione è mai stato sfruttato e quanti file un lettore deve aprire per seguire un unico percorso del codice. Concorda che una sola implementazione senza una seconda in vista sia una ragione predefinita per riportare tutto in linea e indica chi può definire un progetto sovra-ingegnerizzato senza che suoni come un insulto. Nei sistemi aziendali e governativi che sopravvivono ai propri autori di un decennio, l'indirezione gratuita è una tassa che ogni futuro manutentore paga, quindi tratta "che cosa ci compra questa astrazione" come domanda permanente di revisione, non come una sfida personale.

5. **Come decidete quale paradigma usa ciascun componente, orientato agli oggetti, funzionale o orientato ai dati, e come mantenete puliti i confini tra loro?** Il capitolo sostiene che i grandi sistemi siano pragmaticamente misti e che si debba scegliere per componente in base all'adeguatezza, usando l'orientamento agli oggetti per i domini con stato, lo stile funzionale per trasformazioni e concorrenza e la progettazione orientata ai dati dove dominano prestazioni e comportamento della cache. Se non gestita, la scelta del paradigma diventa una questione di chi ha scritto per primo il modulo, e lo stato mutabile si infiltra in ciò che dovrebbero essere trasformazioni pure, oppure un purismo funzionale combatte un problema intrinsecamente con stato. Le prove da portare sono dove sta il vostro dolore reale: quali componenti sono difficili da testare per via dello stato nascosto, quali percorsi caldi sono limitati dalla cache e dove lo stile attuale impone soluzioni goffe. Decidi con deliberazione il paradigma predefinito per ogni livello e metti per iscritto dove cadono le giunture tra gli stili, così che un nucleo funzionale e un margine imperativo non si contaminino a vicenda. Per un sistema regolamentato o governativo in cui un calcolo deve essere verificabile e riproducibile per un dato periodo, un nucleo immutabile e funzionale è spesso un requisito di conformità anziché un gusto, e quel vincolo dovrebbe guidare il confine anziché seguirlo.

6. **Come impedite che questi principi si induriscano in dogma, e dove registrate il ragionamento dietro una decisione di progetto perché un team futuro possa rivederla?** Ogni principio di questo capitolo ha un ambito di applicabilità e una modalità di fallimento, e l'intera impostazione li tratta come strumenti da applicare con giudizio anziché leggi da imporre. In un grande team un principio diventa in silenzio una regola: DRY vieta qualsiasi duplicazione, SOLID impone un'interfaccia per classe e le eccezioni pragmatiche vengono bloccate in revisione da chi cita l'acronimo anziché il risultato. La tensione è che una certa coerenza aiuta davvero centinaia di ingegneri a coordinarsi, quindi non puoi semplicemente dichiarare ogni principio facoltativo. Porta esempi in cui seguire un principio alla lettera ha prodotto un progetto peggiore, e porta i registri delle decisioni, se esistono, che spiegano perché un dato confine o un'astrazione esiste. Concorda che i principi sono valori predefiniti da cui un ingegnere può discostarsi con una motivazione registrata, e cattura le scelte di progetto importanti in un breve registro delle decisioni architetturali, così che il team successivo erediti il ragionamento e non solo il codice. Nei sistemi aziendali e pubblici, dove gli autori originali se ne sono andati da tempo e gli audit chiedono perché il sistema abbia la forma che ha, quella traccia scritta è la differenza tra un progetto che i team futuri possono modificare in sicurezza e uno che temono di toccare.

## Lente settoriale

**Startup.** Privilegia il progetto più semplice che rilascia e mantieni un solo modulo ben fattorizzato finché un vero secondo caso d'uso non impone una giuntura. La tua risorsa più scarsa è l'attenzione ingegneristica, quindi interfacce, livelli e framework speculativi prematuri sono puro costo. Segui la regola del tre prima di estrarre qualsiasi astrazione condivisa e lascia che YAGNI uccida i punti di estensione che nessuno ha ancora chiesto.

**Piccola impresa.** Senza un architetto dedicato e con un budget ridotto, appoggiati al progetto già incorporato nei framework e nelle librerie che acquisti anziché inventare i tuoi pattern. Riserva lo sforzo di progettazione su misura alla manciata di regole che sono davvero il tuo business e mantieni convenzionale tutto il resto, così che un collaboratore esterno o un nuovo assunto possa leggerlo. Un po' di duplicazione che capisci batte un'astrazione ingegnosa che solo il suo autore sa mantenere.

**Grande impresa.** Il ritorno dei principi condivisi è il coordinamento tra molti team: un vocabolario comune per la revisione dei progetti e contesti delimitati che allineano i confini dei modelli alla responsabilità dei team, così che i gruppi evolvano in modo indipendente. Gestisci accoppiamento e coesione in modo esplicito con dati su dipendenze e co-modifica e registra le decisioni di progetto importanti, così che i sistemi restino modificabili ben dopo che i loro autori sono passati ad altro. Guardati allo stesso modo dall'astrazione sbagliata che accoppia i team e dalla sovra-ingegnerizzazione che tassa ogni lettore.

**Ente pubblico.** Verificabilità e riproducibilità dettano spesso il progetto. Un nucleo immutabile e funzionale permette di riprodurre esattamente un calcolo storico per un dato periodo, cosa che un intricato grafo di oggetti con stato mutabile nascosto non può garantire. Preferisci contratti pubblicati ed espliciti alle tabelle condivise ai confini dei contesti e mantieni il progetto e i suoi registri delle decisioni leggibili per gli auditor e per qualunque team erediti il sistema un decennio dopo.

## Esempi

**Startup.** Una startup di tre ingegneri che costruisce il suo primo prodotto resiste alla tentazione di dividere ogni funzionalità in strati di interfacce e factory, tenendo un solo modulo ben fattorizzato finché non compare un vero secondo caso d'uso. Quando la stessa logica compare per la terza volta nei flussi di iscrizione e fatturazione, estraggono una piccola funzione condivisa anziché un framework speculativo. Questo mantiene la base di codice abbastanza piccola da poter essere tenuta a mente da chiunque di loro, e le poche giunture che tracciano cadono dove il prodotto ha più probabilità di cambiare.

**Grande impresa.** Una grande piattaforma assicurativa modella polizza, sinistri e fatturazione come contesti delimitati separati, ciascuno posseduto da un team dedicato con un proprio modello di dati e confine di servizio. Dove i contesti si incontrano, come quando un sinistro fa riferimento a una polizza, comunicano attraverso contratti pubblicati ed espliciti anziché tabelle di database condivise. Questo permette ai tre team di evolvere in modo indipendente, e il linguaggio onnipresente mantiene precise le conversazioni con sottoscrittori e attuari. Una versione precedente condivideva un unico modello esteso, e ogni modifica richiedeva coordinamento tra team.

**Ente pubblico.** Un sistema nazionale di elaborazione fiscale privilegia deliberatamente un nucleo funzionale e orientato ai dati per il suo motore di calcolo. Le regole fiscali sono espresse come trasformazioni pure su record di input immutabili, il che le rende verificabili, testabili e riproducibili per un dato anno d'imposta. Le parti imperative e con stato (flusso di lavoro, notifiche) sono tenute ai margini. Gli auditor possono indicare una specifica versione di regola e riprodurre esattamente qualsiasi calcolo storico, che è un requisito di legge che un intricato grafo di oggetti con stato mutabile nascosto non potrebbe garantire.

## Business case: motivazioni, ROI e TCO

La qualità del progetto è un investimento nella *modificabilità* di un sistema, e la modificabilità domina il costo totale di proprietà. Gran parte del costo di un sistema cade dopo il primo rilascio, in modifica ed estensione. I sistemi ben progettati mantengono il costo del cambiamento più o meno piatto nel tempo. Quelli mal progettati vedono salire il costo di ogni modifica finché il sistema diventa di fatto non modificabile e va riscritto, il risultato più costoso di tutti.

Il costo di adozione è soprattutto competenza e disciplina di revisione: insegnare i principi e spendere tempo di progettazione in anticipo. Il costo del non adottarli è il lento accumulo di [debito tecnico](https://en.wikipedia.org/wiki/Technical_debt), velocità di consegna in calo, tassi di difetti in crescita e costose riscritture finali. Per sostenere il caso con la leadership, collega la disciplina di progetto alla prevedibilità della consegna e all'evitare programmi di riscrittura e segui indicatori anticipatori come il tasso di fallimento delle modifiche e il tempo per implementare funzionalità comparabili nel tempo. Guardati anche dal fallimento opposto: investire troppo nel progetto per futuri incerti distrugge anch'esso valore. L'argomento è dunque a favore di un progetto *appropriato*, calibrato su quanto siano probabili e costosi i cambiamenti futuri.

## Antipattern e insidie

- **Generalità speculativa:** costruire estensibilità per requisiti immaginati che non arrivano mai.
- **L'astrazione sbagliata:** forzare insieme codice non correlato per soddisfare DRY, creando un accoppiamento peggiore della duplicazione.
- **Culto dei pattern:** applicare design pattern fine a se stessi, aggiungendo indirezione senza beneficio.
- **Oggetti anemici o onnipotenti:** modelli senza comportamento, o oggetti che fanno tutto; entrambi segnalano responsabilità collocate male.
- **Monolite distribuito:** servizi divisi fisicamente ma ancora strettamente accoppiati, che combinano i costi di entrambi gli approcci.
- **Grande palla di fango:** nessuna struttura riconoscibile; ogni modifica rischia tutto.
- **Teatro del DDD:** adottare il vocabolario e la struttura delle cartelle senza la modellazione del dominio che dà loro valore.

## Modello di maturità

- **Livello 1, Avvio:** il progetto è ad hoc e reattivo; l'accoppiamento si accumula senza controllo; i principi sono sconosciuti o invocati come slogan, e le astrazioni compaiono o spariscono per abitudine individuale.
- **Livello 2, Sviluppo:** i team conoscono i principi e li applicano, ma in modo incoerente e spesso dogmatico; alcuni gruppi gestiscono con deliberazione accoppiamento e coesione mentre altri no, e non c'è un vocabolario condiviso nell'organizzazione.
- **Livello 3, Standardizzazione:** un vocabolario di progetto condiviso, una regola del tre per estrarre astrazioni, l'analisi di accoppiamento e coesione e contesti delimitati allineati ai team sono documentati e attesi in tutta l'organizzazione, applicati in modo coerente nella revisione dei progetti anziché lasciati al gusto individuale.
- **Livello 4, Gestione:** la salute del progetto è misurata rispetto a valori di riferimento: dati di accoppiamento e co-modifica, tasso di fallimento delle modifiche e tempo per implementare funzionalità comparabili sono seguiti nel tempo, così che astrazioni e confini siano aggiunti, mantenuti o rimossi sulla base delle prove, e la sovra-ingegnerizzazione e l'astrazione sbagliata siano colte dai dati anziché dalle opinioni.
- **Livello 5, Orchestrazione:** la disciplina di progetto è integrata con la pianificazione di consegna e rischio in tutta l'organizzazione; i principi sono applicati con sfumature e modalità di fallimento note; le scelte di paradigma e di confine sono deliberate e riviste di continuo, e l'organizzazione effettua regolarmente refactoring, ridefinisce l'ambito e ritira astrazioni al mutare di dominio e prove.

## Spunti di discussione

- Come distinguete una giuntura necessaria dalla generalità speculativa prima di avere il requisito futuro?
- Quando DRY ha portato il vostro team all'astrazione sbagliata, e come l'avete riconosciuta?
- Dove dovrebbero cadere i confini dei contesti delimitati, e quanto dovrebbero rispecchiare l'organigramma?
- Quanto progetto dovrebbe precedere il codice nel vostro contesto, e come registrate le decisioni?
- Quali parti del vostro sistema trarrebbero beneficio da uno stile più funzionale o orientato ai dati?
- Come impedite che i principi di progetto si induriscano in dogma che resiste alle eccezioni pragmatiche?

## Punti chiave

- Accoppiamento e coesione sono le proprietà che contano; gli acronimi sono mezzi per quei fini.
- Ogni principio ha una modalità di fallimento; sappi quando ciascuno fuorvia.
- Preferisci un po' di duplicazione a un'astrazione prematura o sbagliata.
- Usa il DDD e i contesti delimitati per allineare domini complessi alla responsabilità dei team.
- Scegli i paradigmi per adeguatezza; i grandi sistemi sono pragmaticamente misti.
- Progetta per i cambiamenti di cui avrai davvero bisogno, evitando sia la sotto- sia la sovra-progettazione.

## Riferimenti e letture di approfondimento

- Robert C. Martin, *Clean Architecture* e *Agile Software Development, Principles, Patterns, and Practices*
- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code* e *Patterns of Enterprise Application Architecture*
- David L. Parnas, *On the Criteria to Be Used in Decomposing Systems into Modules*
- Sandi Metz, *Practical Object-Oriented Design*
