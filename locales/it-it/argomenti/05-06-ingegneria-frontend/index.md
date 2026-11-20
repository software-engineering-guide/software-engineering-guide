# 5.6 Ingegneria frontend

## Panoramica e motivazioni

L'ingegneria frontend è la disciplina di costruire lo strato rivolto al client del software: il codice che gira nel browser o sul dispositivo e trasforma progetti, contenuti e dati in un'interfaccia funzionante. Copre le scelte di framework e architettura, la strategia di rendering, la gestione dello stato, le prestazioni e la resilienza attraverso l'enorme diversità di browser, dispositivi e condizioni di rete del mondo reale. Il frontend è dove tutto il lavoro a monte (UX, design, contenuti, accessibilità, internazionalizzazione) o raggiunge con successo l'utente o si sfalda.

Per i grandi team, il frontend è unicamente impegnativo, perché è esposto a un ambiente che l'organizzazione non controlla. Browser, dispositivi, connessioni e impostazioni degli utenti variano enormemente e la piattaforma (il web) evolve di continuo. Su larga scala, le scelte architetturali si compongono. Un framework scelto oggi vincola assunzioni, prestazioni e manutenibilità per anni e migliaia di piccole decisioni su dimensione del bundle e rendering si sommano nell'esperienza che gli utenti ottengono davvero. Standard condivisi, librerie di componenti, budget di prestazioni e schemi architetturali sono ciò che impedisce a molti team indipendenti di produrre un insieme lento, incoerente e fragile.

La rilevanza per imprese ed enti pubblici è acuta. Le imprese mantengono applicazioni di lunga durata dove longevità del framework e manutenibilità contano più della novità e dove molti team devono interoperare. Gli enti pubblici servono l'intera popolazione, comprese persone con dispositivi vecchi, connessioni lente o a consumo e tecnologie assistive. Questo rende prestazioni, [miglioramento progressivo](https://en.wikipedia.org/wiki/Progressive_enhancement) e resilienza non una rifinitura facoltativa ma la differenza tra un servizio che funziona per tutti e uno che esclude i meno avvantaggiati. Un servizio pubblico che funziona solo sull'ultimo telefono con una connessione veloce fallisce il proprio mandato.

## Principi chiave

- Il frontend gira in un ambiente che non controlli; progetta per variabilità e guasto.
- Scegli tecnologia noiosa e durevole per i sistemi di lunga durata; ottimizza per manutenibilità e assunzioni.
- Le prestazioni sono una funzionalità e, per molti utenti, un prerequisito per l'accesso.
- Miglioramento progressivo: consegna prima un'esperienza di base funzionante, poi stratifica i miglioramenti.
- Invia meno codice; il codice più veloce e affidabile è quello che non rilasci.
- Adegua la strategia di rendering al tipo di contenuto e al bisogno dell'utente, non alla moda.
- Resilienza: l'interfaccia dovrebbe degradare con grazia, non rompersi, quando le cose vanno male.
- Standard e funzionalità della piattaforma sopravvivono ai framework; appoggiati alla piattaforma.

## Raccomandazioni

### Scegli i framework per longevità e adattamento, non per moda

Seleziona la tecnologia frontend in base al problema, al team, all'orizzonte di manutenzione e al mercato delle assunzioni, non a ciò che è di tendenza. Per i sistemi aziendali e governativi di lunga durata, privilegia tecnologie mature e ben supportate con ampi bacini di talento, pratiche di rilascio stabili e percorsi di aggiornamento chiari. Pesa il costo totale del ricambio di framework: le riscritture sono costose e rischiose. Preferisci approcci che si appoggiano a [standard web](https://en.wikipedia.org/wiki/Web_standards) così che il tuo investimento sopravviva al ricambio di framework e isola il codice specifico del framework dietro confini così che l'applicazione non sia ostaggio del ciclo di vita di una sola libreria.

### Adegua la strategia di rendering al bisogno

Le principali strategie di rendering si adattano ciascuna a contenuti diversi. Il rendering lato server (SSR) produce un primo disegno veloce e buona SEO ([ottimizzazione per i motori di ricerca](https://en.wikipedia.org/wiki/Search_engine_optimization)) e funziona senza JavaScript sul client, adatto a pagine ricche di contenuto e rivolte al pubblico. La [generazione di siti statici](https://en.wikipedia.org/wiki/Static_site_generator) (SSG) pre-rende al momento della build per la massima velocità e memorizzabilità in cache, ideale per contenuti che cambiano di rado. Il rendering lato client (CSR) si adatta a esperienze molto interattive simili ad app dietro autenticazione. Lo streaming e l'idratazione progressiva inviano e attivano la pagina in modo incrementale così che gli utenti vedano e usino il contenuto prima. Molti grandi sistemi li mescolano per rotta anziché sceglierne uno globalmente. Gestisci lo stato deliberatamente: tieni distinti stato del server, stato dell'URL e stato locale della UI ed evita di sovra-centralizzare tutto in un unico pesante archivio globale.

### Tratta le prestazioni come una disciplina a budget e misurata

Adotta budget di prestazioni (limiti espliciti su dimensione del bundle, numero di richieste e metriche chiave) e falli rispettare nella CI così che le regressioni facciano fallire la build. Segui i Core Web Vitals (caricamento, interattività e stabilità visiva) usando il monitoraggio degli utenti reali da dispositivi e reti effettivi, non solo test di laboratorio su macchine veloci. Riduci JavaScript in modo aggressivo: suddividi il codice e usa il [caricamento pigro](https://en.wikipedia.org/wiki/Lazy_loading) così che gli utenti scarichino solo ciò di cui una data vista ha bisogno, rinvia il lavoro non critico e preferisci le capacità della piattaforma alle librerie pesanti. Ottimizza immagini e caratteri, usa la cache in modo efficace e misura su dispositivi rappresentativi di fascia bassa e connessioni lente.

### Costruisci con miglioramento progressivo e resilienza

Parti da una base che funziona con HTML semantico e JavaScript minimo o nullo, poi migliora per i client capaci. Questo assicura che il compito centrale resti possibile quando gli script non si caricano, un dispositivo è vecchio o una rete è instabile, una realtà comune anziché un caso limite. Gestisci gli errori con grazia: mostra stati utili per condizioni di caricamento, vuoto, errore e offline anziché schermate bianche o spinner infiniti. Per i servizi da cui le persone dipendono, considera tecniche offline-first così che l'app resti utilizzabile attraverso una connettività intermittente, sincronizzando quando la connessione ritorna.

### Assicura compatibilità tra browser, dispositivi e tecnologie assistive

Testa attraverso i browser, i dispositivi e le tecnologie assistive che i tuoi utenti hanno davvero, guidato da analisi reali anziché dalle macchine del team. Usa il miglioramento progressivo e il rilevamento delle funzionalità anziché presumere che le funzionalità di piattaforma più nuove siano disponibili ovunque. Costruisci in modo [reattivo](https://en.wikipedia.org/wiki/Responsive_web_design) (vedi il capitolo sul design system) così che una base di codice serva dai telefoni ai desktop. Integra accessibilità e internazionalizzazione nell'architettura frontend fin dall'inizio, non come passaggi successivi.

### Governa il frontend come infrastruttura condivisa

Fornisci librerie di componenti condivise, linting, formattazione e strumenti di build così che i team siano coerenti e produttivi. Stabilisci linee guida architetturali (come strutturare le applicazioni, gestire lo stato e dividere i bundle) e budget di prestazioni fatti rispettare nella CI. Per frontend molto grandi, considera architetture modulari o a micro-frontend che permettano ai team di rilasciare in modo indipendente, ma pesa con cura la complessità e il costo di prestazioni aggiunti, perché non sono gratuiti.

## Compromessi: vantaggi e svantaggi

| Decisione | Vantaggi | Svantaggi |
|---|---|---|
| Framework popolare e maturo | Ampio bacino di talento, stabile, supportato | Può portare peso legacy; più lento ad adottare le funzionalità più nuove |
| Framework più recente | Funzionalità moderne, guadagni di prestazioni | Rischio di ricambio, piccolo bacino di talento, longevità incerta |
| SSR / SSG | Primo disegno veloce, SEO, funziona senza JS | Complessità di server o build, sfide di cache |
| CSR (SPA) | Ricca interattività, aspetto da app | Primo caricamento lento, dipende da JS, costo in SEO e resilienza |
| Molto JavaScript sul client | Funzionalità ricche | Scarse prestazioni su dispositivi di fascia bassa, fragile |
| Miglioramento progressivo | Resiliente, inclusivo, funziona ovunque | Più sforzo di design per definire una base funzionante |
| Micro-frontend | Rilasci indipendenti dei team, scala | Complessità, dipendenze duplicate, onere di prestazioni |

Il compromesso ricorrente è ricchezza e comodità degli sviluppatori contro portata, prestazioni e resilienza. Gli approcci pesanti sul client sono piacevoli da costruire e da mostrare su macchine veloci, ma escludono gli utenti su dispositivi e reti deboli. Per i pubblici aziendali e soprattutto governativi, inclina l'equilibrio verso prestazioni, miglioramento progressivo e durabilità, perché il costo di escludere gli utenti è alto e spesso non negoziabile.

## Domande da discutere con il tuo team

1. **Come isoliamo il codice specifico del framework così che l'applicazione non sia ostaggio del ciclo di vita di una sola libreria?** Per i sistemi aziendali e governativi di lunga durata, il ricambio di framework è la spesa evitabile maggiore: una riscrittura è costosa e rischiosa e la libreria di tendenza di oggi vincola assunzioni e manutenzione per anni. Appoggiarsi a standard web e mettere il codice specifico del framework dietro confini chiari significa che la tua logica di business e i tuoi contenuti sopravvivono al prossimo ricambio di framework. Decidi dove stanno quelle giunture e se un nuovo ingegnere saprebbe distinguere il codice di piattaforma da quello del framework. Porta una stima di quanto è costata la tua ultima migrazione di framework, o di quanto costerà quella incombente. Se la tua logica centrale è saldata alle API di una sola libreria, prezza quell'accoppiamento prima di difendere la scelta del framework.

2. **Adeguiamo la strategia di rendering per rotta, o imponiamo un'unica strategia all'intero prodotto?** Il rendering lato server dà un primo disegno veloce e funziona senza JavaScript sul client per i contenuti pubblici, la generazione statica massimizza la velocità per le pagine che cambiano di rado e il rendering sul client si adatta a superfici interattive simili ad app dietro login. Imporne una globalmente o rallenta le pagine pubbliche con JavaScript pesante o sovra-ingegnerizza una semplice pagina di contenuto. È una questione di portata per gli enti pubblici, dove un servizio che funziona solo dopo che un grande bundle si carica esclude gli utenti con dispositivi vecchi e connessioni lente. Porta le tue rotte chiave ed etichetta ciascuna con la strategia che usa davvero oggi. Se una pagina rivolta al pubblico ha bisogno di JavaScript per mostrare il proprio contenuto, decidi se è una scelta deliberata o un incidente.

3. **Quanto è disciplinata la nostra gestione dello stato, e stiamo sovra-centralizzando tutto in un unico pesante archivio globale?** Tenere distinti stato del server, stato dell'URL e stato locale della UI previene l'accoppiamento e le tempeste di re-rendering che rendono lenti e fragili i grandi frontend, eppure il predefinito allettante è buttare tutto in un unico archivio globale. Si compone su larga scala, dove molti team che toccano un archivio condiviso creano dipendenze nascoste e prestazioni imprevedibili. Concorda dove appartiene ogni tipo di stato e che cosa non appartiene all'archivio globale. Porta un componente che si ri-renderizza più di quanto dovrebbe e ricostruisci perché. Se la risposta è un archivio centrale gonfio, decidi i confini prima che l'accoppiamento si indurisca.

4. **Quali sono i nostri budget di prestazioni, fanno fallire la build nella CI e sono misurati sui dispositivi che i nostri utenti hanno davvero?** Un budget che nessuno fa rispettare è un desiderio e un budget misurato solo sui portatili veloci del team descrive un utente che non esiste. Per una grande organizzazione, i budget sono l'unico meccanismo che tiene sotto controllo dimensione del bundle e Core Web Vitals man mano che decine di team aggiungono funzionalità a una superficie condivisa, perché nessun singolo revisore può cogliere a occhio ogni regressione. La pressione contraria è la velocità di consegna: un fallimento rigido della build per pochi kilobyte sembra ostruzionistico finché non prezzi l'abbandono che previene. Porta i tuoi budget attuali, i dati di monitoraggio degli utenti reali da dispositivi di fascia bassa e connessioni lente e l'elenco dei rilasci in cui una regressione è sfuggita. Negli enti pubblici, dove il mandato è servire l'intera popolazione comprese le persone con telefoni vecchi e dati a consumo, lega il budget al decimo più lento dei tuoi utenti anziché alla mediana e rendi non negoziabile il cancello CI.

5. **Quali dei nostri servizi devono continuare a funzionare senza JavaScript sul client, e abbiamo davvero testato quel percorso?** Il miglioramento progressivo è facile da dichiarare e facile da rompere in silenzio, perché il percorso migliorato è quello che gli sviluppatori usano ogni giorno mentre la base marcisce non testata. Decidere deliberatamente conta su larga scala, poiché molti team che rilasciano su una piattaforma presumeranno ciascuno che gli script si carichino sempre a meno che uno standard condiviso dica altrimenti e una singola dipendenza rigida può rompere il compito centrale per chiunque il cui bundle fallisca. Il compromesso è reale: una base funzionante senza JavaScript costa sforzo di design e vincola come costruisci l'interattività. Porta i tuoi percorsi utente critici, un test che carichi ciascuno con gli script disabilitati o falliti e l'evidenza di quanto spesso gli script non si caricano davvero sul campo. Per un servizio pubblico, un modulo di prestazioni o fiscale che crolla quando uno script va in timeout non è un'esperienza degradata, è un cittadino che non può completare un obbligo legale, quindi tratta la base come un requisito di conformità, non un vezzo.

6. **Quando i micro-frontend ripagano davvero la loro complessità, e chi decide prima che un team vi ricorra?** I rilasci indipendenti dei team sono attraenti, ma i micro-frontend portano complessità da sistema distribuito, dipendenze duplicate e una tassa di prestazioni che gli utenti pagano in caricamenti più lenti. Senza un punto decisionale condiviso, i team ambiziosi li adottano per comodità organizzativa molto prima che la scala giustifichi il costo e l'intero prodotto eredita l'onere. La considerazione contraria è l'autonomia: i team che rilasciano su una base di codice condivisa possono bloccarsi a vicenda e a una vera scala quell'accoppiamento è esso stesso un problema costoso. Porta il numero di team che toccano la superficie, la contesa nei rilasci che vivi davvero oggi e una stima misurata della duplicazione del payload che una divisione introdurrebbe. Per le piattaforme aziendali e governative, dove le decisioni di architettura vincolano molti team per anni e devono sopravvivere ad audit e passaggi di consegne, richiedi una soglia esplicita e documentata e un responsabile che approvi il passaggio, anziché lasciare che ogni team decida da solo.

## Lente settoriale

**Startup.** Velocità e portata contano entrambe quando ogni iscrizione conta, quindi resisti alla pesante applicazione a pagina singola per le pagine pubbliche. Fai il rendering lato server del tuo marketing e del flusso di iscrizione così che si carichino in fretta sui telefoni di fascia media e sui dati instabili che usano i tuoi primi clienti e riserva l'interattività lato client all'app dietro login. Fissa un semplice budget di dimensione del bundle nella CI così che una dipendenza trascurata non possa gonfiare in silenzio la pagina e appoggiati agli standard web per mantenere manutenibile una piccola base di codice man mano che assumi.

**Piccola impresa.** Senza uno specialista frontend dedicato e con un budget ridotto, preferisci un framework mainstream ben supportato o un costruttore di siti ospitato a qualsiasi cosa su misura, così da assumere da un grande bacino di talento e comprare manutenzione anziché dotarla di personale. Imposta la scelta come durabilità: l'opzione più economica è quella che non sei costretto a riscrivere tra due anni. Esigi pagine veloci e adatte al mobile e markup accessibile di serie, poiché un checkout lento o rotto ti costa clienti che non puoi permetterti di perdere.

**Grande impresa.** Il problema è la coerenza tra molti team: una libreria di componenti condivisa, schemi architetturali concordati, linting e strumenti di build e budget di prestazioni fatti rispettare nella CI così che nessun team possa far regredire in silenzio l'insieme. Scegli i framework per longevità e assunzioni anziché novità, isola il codice specifico del framework dietro confini per sopravvivere alla prossima migrazione e adegua la strategia di rendering per superficie. Gestisci il frontend come infrastruttura condivisa con monitoraggio degli utenti reali, governance e una traccia verificabile del perché ogni scelta architetturale è stata fatta.

**Ente pubblico.** Servi l'intera popolazione, comprese persone con dispositivi vecchi, connessioni lente o a consumo e tecnologie assistive, quindi miglioramento progressivo e prestazioni sono obblighi, non rifinitura. Fai di una base funzionante senza JavaScript una regola rigida per i servizi rivolti ai cittadini, dimensiona il budget delle pagine sugli utenti più lenti anziché sulla mediana e mantieni completabile il compito centrale quando uno script fallisce. Valgono appalti e trasparenza: privilegia una tecnologia durevole e orientata agli standard che eviti il lock-in con un solo fornitore, documenta nei contratti i requisiti di accessibilità e prestazioni e sii in grado di mostrare che il servizio funziona per l'utente meno avvantaggiato, non solo per il dispositivo della dimostrazione.

## Esempi

**Startup.** Una startup in fase seed era tentata di costruire il proprio sito di marketing e il flusso di iscrizione come una pesante applicazione a pagina singola, ma i suoi clienti obiettivo erano acquirenti spesso su telefoni di fascia media con dati mobili instabili. I due fondatori hanno invece fatto il rendering lato server delle pagine pubbliche così che si caricassero in fretta e funzionassero prima che girasse qualsiasi JavaScript e hanno riservato l'interattività lato client all'app dietro login. Hanno fissato un semplice budget di dimensione del bundle nella CI così che una dipendenza trascurata non potesse gonfiare in silenzio la pagina. Il primo caricamento snello e veloce ha migliorato in modo misurabile le iscrizioni e appoggiarsi agli standard web ha mantenuto facile da mantenere la piccola base di codice man mano che assumevano.

**Grande impresa.** Un'azienda di servizi finanziari ha modernizzato un'ampia serie di applicazioni interne e per clienti standardizzando su un framework maturo, una libreria di componenti condivisa e budget di prestazioni fatti rispettare nella CI. La strategia di rendering è stata scelta per superficie: pagine renderizzate lato server e memorizzabili in cache per marketing e contenuti pubblici e un'applicazione renderizzata sul client dietro login per cruscotti interattivi. Budget di bundle e monitoraggio degli utenti reali hanno colto le regressioni prima del rilascio, mantenendo veloci i tempi di caricamento tra i molti team dell'azienda e riducendo il rischio di ricambio di framework che prima aveva forzato costose riscritture.

**Ente pubblico.** Un team nazionale di servizi digitali ha costruito servizi rivolti ai cittadini con il miglioramento progressivo come regola rigida: ogni servizio funziona prima con HTML semantico e rendering lato server e JavaScript si limita a migliorare. Questo garantisce che il servizio funzioni su telefoni vecchi, connessioni rurali lente e tecnologie assistive, popolazioni che un governo non può escludere. I budget di prestazioni mantengono le pagine leggere e veloci sui dispositivi di fascia bassa e il degrado con grazia significa che uno script fallito non blocca mai qualcuno dal completare una domanda di prestazioni. Il risultato è un servizio veloce, resiliente, accessibile e utilizzabile dall'intera popolazione.

## Business case: motivazioni, ROI e TCO

Le scelte di ingegneria frontend guidano ricavi, portata e costo. Le prestazioni sono direttamente legate a conversione, coinvolgimento e completamento dei compiti. Le esperienze più veloci superano in modo misurabile quelle più lente e per gli utenti su dispositivi deboli, le prestazioni sono la linea tra usare il servizio e abbandonarlo. Il miglioramento progressivo e il supporto multi-dispositivo ampliano il pubblico indirizzabile, che per gli enti pubblici è un mandato e per le imprese è quota di mercato. Solide scelte di framework e architettura riducono la frequenza e il costo delle riscritture, la spesa evitabile maggiore nell'ingegneria frontend.

Sul TCO, i costi di adozione sono la disciplina di budget di prestazioni e test, lo sforzo del miglioramento progressivo e l'investimento in strumenti condivisi e librerie di componenti. Il costo del non adottare si paga in esperienze lente che perdono utenti e ricavi, esclusione degli utenti di fascia bassa e di tecnologie assistive (con esposizione legale negli enti pubblici), applicazioni fragili che si rompono sul campo e costoso ricambio di framework e riscritture guidati dall'inseguire le tendenze. I problemi del frontend emergono come abbandono diffuso e carico di assistenza anziché una singola voce, quindi è facile investirvi troppo poco.

Per presentare il caso alla leadership, collega i Core Web Vitals e i tempi di caricamento ai funnel di conversione e completamento, quantifica gli utenti esclusi dagli approcci pesanti sul client e prezza il costo delle riscritture passate o incombenti rispetto alla stabilità di un'architettura durevole e orientata agli standard. Imposta budget di prestazioni e miglioramento progressivo come riduzione del rischio ed espansione della portata.

## Antipattern e insidie

- **Inseguire i framework**: riscrivere sull'ultima libreria, incorrendo in ricambio senza beneficio per l'utente.
- **Esperienze solo JavaScript**: niente funziona finché un grande bundle si carica e gira, escludendo molti utenti.
- **Testare solo su dispositivi veloci**: i portatili di punta del team nascondono la vera esperienza dell'utente.
- **Ignorare la dimensione del bundle**: crescita illimitata delle dipendenze finché le pagine sono lente ovunque.
- **Nessun budget di prestazioni**: le regressioni si accumulano in silenzio rilascio dopo rilascio.
- **Fallimenti a schermata bianca**: nessuno stato di caricamento, vuoto, errore od offline; una richiesta fallita rompe la pagina.
- **Stato globale sovra-centralizzato**: tutto in un unico archivio, creando accoppiamento e tempeste di re-rendering.
- **Micro-frontend prematuri**: complessità da sistema distribuito e payload duplicati senza la scala che li giustifichi.
- **Trascurare accessibilità e i18n nell'architettura**: incollarle dopo a costo alto.

## Modello di maturità

**Livello 1: Avvio.** Frontend ad hoc costruito per team senza standard condivisi. Molto codice lato client, nessun budget di prestazioni, testato solo sui dispositivi del team stesso. Scelte di framework fatte per preferenza o moda e uno script fallito può lasciare gli utenti a fissare una schermata bianca.

**Livello 2: Sviluppo.** Alcuni team adottano strumenti condivisi e una libreria di componenti, ma la pratica è incoerente nell'organizzazione. Le prestazioni sono misurate occasionalmente anziché messe a budget o fatte rispettare. La strategia di rendering è spesso uniforme a prescindere dal tipo di contenuto e i test su più dispositivi sono limitati e manuali.

**Livello 3: Standardizzazione.** Framework e architettura sono scelti deliberatamente per longevità e le scelte sono documentate e fatte rispettare nell'organizzazione. La strategia di rendering è adeguata per superficie, miglioramento progressivo e degrado con grazia sono lo standard e librerie di componenti condivise, linting e strumenti di build si applicano a ogni team. Compatibilità tra browser, accessibilità e internazionalizzazione sono incorporate anziché incollate dopo.

**Livello 4: Gestione.** Il frontend è misurato e controllato con dati. I budget di prestazioni sono fatti rispettare nella CI così che le regressioni facciano fallire la build e i Core Web Vitals sono seguiti con monitoraggio degli utenti reali da effettivi dispositivi di fascia bassa e connessioni lente rispetto a valori di riferimento espliciti. Dimensione del bundle, copertura degli stati di errore e offline e quota di utenti serviti sulle connessioni più lente sono riportate e riviste, così che le decisioni poggino sull'evidenza anziché sull'opinione.

**Livello 5: Orchestrazione.** Prestazioni, resilienza e portata sono migliorate di continuo e legate agli esiti di business in tutta l'organizzazione. Il frontend si appoggia agli standard web per durabilità, isola le dipendenze dal framework così che le migrazioni siano economiche ed evolve l'architettura in modo adattivo man mano che dispositivi, piattaforma e dati degli utenti reali cambiano. L'intera popolazione e tutti i dispositivi sono di prim'ordine e la pratica frontend è integrata con design, accessibilità e pianificazione del prodotto anziché trattata come una questione separata.

## Spunti di discussione

- Come decidete quando una migrazione di framework vale il suo costo e rischio?
- Quali Core Web Vitals e budget di bundle dovrebbero essere soglie rigide che fanno fallire la build?
- Dove il miglioramento progressivo è essenziale, e dove un'app lato client è accettabile?
- Come mantenete coerente l'architettura frontend tra molti team autonomi?
- Quando i micro-frontend ripagano davvero la loro complessità?
- Come dovrebbero essere integrati nella pipeline i test su dispositivi reali e reti lente?

## Punti chiave

- Il frontend gira in un ambiente che non controlli: progetta per variabilità e guasto.
- Scegli tecnologia durevole e ben supportata per i sistemi di lunga durata; appoggiati agli standard web.
- Adegua la strategia di rendering (SSR, SSG, CSR, streaming) a contenuto e bisogno, spesso mescolata per rotta.
- Tratta le prestazioni come una disciplina a budget e misurata, fatta rispettare nella CI con dati degli utenti reali.
- Costruisci con miglioramento progressivo così che l'esperienza centrale funzioni ovunque.
- Rilascia meno JavaScript; suddividi il codice, usa il caricamento pigro e preferisci le capacità della piattaforma.
- Per gli enti pubblici soprattutto, prestazioni e resilienza sono prerequisiti per un accesso equo.

## Riferimenti e letture di approfondimento

- Jeremy Keith, *Resilient Web Design*
- Aaron Gustafson, *Adaptive Web Design* (miglioramento progressivo)
- Steve Souders, *High Performance Web Sites*
- Ilya Grigorik, *High Performance Browser Networking*
- Addy Osmani, scritti su prestazioni, suddivisione del codice e costo di JavaScript
- Google, *Web Vitals* e indicazioni sulle prestazioni di web.dev
- MDN Web Docs, riferimenti su piattaforma web e miglioramento progressivo
- Alex Russell, saggi sul costo di JavaScript e sulla diversità dei dispositivi
- UK Government Digital Service, indicazioni su miglioramento progressivo e frontend
- WHATWG HTML Living Standard e specifiche della piattaforma web del W3C
