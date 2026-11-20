# 2.3 API e progettazione delle interfacce

## Panoramica e motivazioni

Un'[API](https://en.wikipedia.org/wiki/API) (application programming interface, interfaccia di programmazione di un'applicazione) è il contratto attraverso cui un pezzo di software offre una capacità a un altro. È dove si incontrano team, sistemi e organizzazioni, ed è la cosa più durevole e costosa da sbagliare. Puoi modificare liberamente la firma di una funzione interna. Un'API pubblicata è diversa: è una promessa a consumatori che potresti non incontrare mai, e romperla significa romperli. Man mano che le organizzazioni dividono i [monoliti](https://en.wikipedia.org/wiki/Monolithic_application) in servizi e aprono capacità a partner e pubblico, l'API diventa la principale superficie di prodotto e il principale rischio di integrazione.

Per i grandi team, le API sono ciò che permette alle persone di lavorare in modo indipendente. Un'interfaccia ben progettata permette di cambiare la propria parte interna senza coordinarsi con ogni consumatore, che è lo scopo stesso di un confine di servizio. Una progettata male lascia trapelare dettagli interni, impone rilasci sincronizzati e trasforma un insieme di servizi in un monolite distribuito: servizi divisi ma così accoppiati da dover essere costruiti e rilasciati insieme. La progettazione delle tue API determina direttamente quanto indipendentemente possono muoversi i tuoi team.

Nei contesti aziendali e governativi le API portano anche obblighi di conformità, sicurezza e longevità. Un'API del settore pubblico può essere tenuta a seguire [standard aperti](https://en.wikipedia.org/wiki/Open_standard), restare stabile per anni e servire sviluppatori esterni con cui non puoi coordinarti. Le API aziendali sostengono integrazioni con partner con livelli di servizio contrattuali. Tutto questo alza l'asticella su disciplina di versionamento, [compatibilità all'indietro](https://en.wikipedia.org/wiki/Backward_compatibility), governance ed esperienza degli sviluppatori.

## Principi chiave

- Progetta prima il contratto. L'interfaccia è una decisione di prodotto deliberata, non un sottoprodotto dell'implementazione.
- Ottimizza per l'esperienza del consumatore, non per la tua comodità.
- Tratta la compatibilità all'indietro come una promessa. Le modifiche incompatibili richiedono una nuova versione e un percorso di migrazione.
- Rendi corretta la cosa facile: valori predefiniti sensati, errori prevedibili, convenzioni coerenti.
- Progetta per il fallimento. [Idempotenza](https://en.wikipedia.org/wiki/Idempotence) (una richiesta ripetuta ha lo stesso effetto di una singola), ripetizioni, paginazione e [limitazione della frequenza](https://en.wikipedia.org/wiki/Rate_limiting) sono questioni di prim'ordine, non ripensamenti.
- Scegli lo stile del protocollo in base all'interazione, non alla moda.
- Governa le API come prodotti, con responsabili, cicli di vita e documentazione.

## Raccomandazioni

### Lavora prima sull'API e guidato dal contratto

Definisci e rivedi il contratto dell'API, comprese risorse, operazioni, schemi e semantica degli errori, prima di scrivere l'implementazione. Usa una specifica leggibile da macchina, così che il contratto possa generare documentazione, stub di client e server, server simulati e validazione. A quel punto i consumatori possono iniziare a integrarsi con il simulato mentre costruisci, e il contratto diventa l'unica fonte di verità rispetto a cui entrambe le parti testano.

### Scegli lo stile di interazione con deliberazione

Scegli tra [REST](https://en.wikipedia.org/wiki/REST) (representational state transfer), [GraphQL](https://en.wikipedia.org/wiki/GraphQL), [gRPC](https://en.wikipedia.org/wiki/GRPC) e [messaggistica guidata dagli eventi](https://en.wikipedia.org/wiki/Event-driven_architecture) in base all'interazione, non alla preferenza personale. Usa REST per interfacce orientate alle risorse, largamente interoperabili e memorizzabili in cache. Usa GraphQL quando client diversi hanno bisogno di letture flessibili e aggregate su un grafo ricco. Usa gRPC per chiamate ad alte prestazioni e fortemente tipizzate tra servizi interni. Usa la messaggistica guidata dagli eventi per flussi di lavoro asincroni e disaccoppiati e per propagare i cambiamenti di stato. Molti grandi sistemi usano più stili insieme, ciascuno dove si adatta.

### Versiona e depreca con disciplina

Adotta una strategia di versionamento esplicita e una politica di deprecazione pubblicata: come classifichi le modifiche, per quanto tempo supporti le vecchie versioni e come avvisi i consumatori. Traccia una linea netta tra modifiche compatibili all'indietro (aggiungere campi opzionali, nuovi endpoint) e modifiche incompatibili (rimuovere o rinominare campi, cambiare tipi o semantica). Non riutilizzare mai il significato di un campo esistente. Dai ai consumatori finestre di sovrapposizione per migrare e comunica i tempi con ampio anticipo.

### Rendi coerente e leggibile da macchina la semantica degli errori

Restituisci errori strutturati e prevedibili: codici stabili leggibili da macchina, messaggi leggibili da persone e abbastanza contesto per agire, senza lasciar trapelare dettagli interni sensibili. Usa la stessa semantica di stato su ogni endpoint, così che i client possano gestire gli errori in modo uniforme. Documenta ogni errore in cui un consumatore potrebbe imbattersi.

### Incorpora idempotenza, paginazione e limitazione della frequenza

Rendi sicure da ripetere le operazioni di scrittura supportando chiavi di idempotenza, così che un client che ripete dopo un timeout non addebiti due volte né crei due volte. Pagina ogni endpoint di elenco fin dal primo giorno e preferisci la paginazione basata su cursore per insiemi di dati grandi o mutevoli. Applica e documenta i limiti di frequenza e restituisci ai client lo stato attuale del limite, così che possano rallentare con grazia.

### Governa le API e investi nell'esperienza degli sviluppatori

Tratta ogni API come un prodotto, con un responsabile, un ciclo di vita e una voce di catalogo. Istituisci una revisione dei progetti o un comitato per gli standard delle API, così che le interfacce restino coerenti tra i team. Investi nell'esperienza degli sviluppatori: documentazione di riferimento accurata, guide rapide, esempi, un ambiente di prova e un registro delle modifiche. In un grande ecosistema, un portale o catalogo che renda reperibili le API è essenziale.

## Compromessi: vantaggi e svantaggi

| Stile | Ideale per | Vantaggi | Svantaggi |
|---|---|---|---|
| REST / HTTP | API pubbliche orientate alle risorse | Ubiquo, memorizzabile in cache, semplice, interoperabile | Recupero in eccesso o in difetto; molti viaggi di andata e ritorno; contratti laschi se non specificati |
| GraphQL | Letture flessibili per client vari | Query specificate dal client; un solo endpoint; schema forte | Complessità di cache e limitazione della frequenza; rischi di costo delle query; complessità del server |
| gRPC | Chiamate interne ad alte prestazioni | Veloce, compatto, fortemente tipizzato, streaming | Scarso supporto dei browser; meno leggibile da persone; strumenti più pesanti |
| Guidato dagli eventi | Flussi di lavoro asincroni e disaccoppiati | Accoppiamento lasco; scalabile; resiliente | Più difficile da ragionare; consistenza finale; complessità operativa |

Le strategie di versionamento scambiano stabilità con manutenzione. Supportare molte vecchie versioni protegge i consumatori, ma moltiplica il codice da mantenere e testare. La compatibilità all'indietro scambia la tua libertà con la stabilità dei consumatori, di solito lo scambio giusto per un'API molto usata. Il quadro generale: il costo di una cattiva decisione sull'API è pagato da ogni consumatore per l'intera vita dell'interfaccia. Vale quindi la pena spendere più sforzo di progettazione al confine che quasi ovunque altrove.

## Domande da discutere con il tuo team

1. **Come classificate una modifica come compatibile all'indietro o incompatibile, e quale controllo automatico coglie un'incompatibilità silenziosa prima che sia rilasciata?** Questo capitolo traccia una linea netta: aggiungere campi opzionali e nuovi endpoint è sicuro, mentre rimuovere o rinominare campi, cambiare tipi o riutilizzare il significato di un campo rompe i consumatori. In un grande team chi fa la modifica spesso non vede ogni consumatore, quindi un ritocco "piccolo" può rompere in silenzio partner con cui non parli mai. Porta alla riunione il segnale concreto: eseguite controlli automatici di compatibilità del contratto nella CI rispetto alla specifica pubblicata, o vi affidate al fatto che qualcuno ricordi la regola? Nei contesti aziendali e governativi, dove una modifica incompatibile impone una migrazione coordinata tra tutti i partner e può attraversare cambi di fornitori e amministrazioni, il costo scala con il numero di consumatori. Decidi le regole di classificazione e collega un cancello di compatibilità, così che una modifica incompatibile faccia fallire la build anziché un'integrazione.

2. **Quali primitive di affidabilità, chiavi di idempotenza, paginazione e limitazione della frequenza, sono obbligatorie su ogni nuovo endpoint dal primo giorno?** Il capitolo insiste che sono questioni di prim'ordine, perché aggiungere a posteriori una chiave di idempotenza a un endpoint di addebito già in produzione o la paginazione a un elenco già rilasciato è di per sé una modifica incompatibile. Un grande ecosistema amplifica questo: un endpoint che funziona nei test crolla con i volumi di dati reali, e una scrittura non idempotente trasforma un singolo singhiozzo di rete in addebiti duplicati. Porta le prove di quali endpoint attuali ne sono privi e di che cosa farebbe una tempesta di ripetizioni. Rendi non negoziabili i valori predefiniti per i nuovi endpoint: paginazione a cursore su ogni elenco, chiavi di idempotenza su ogni scrittura, limiti di frequenza documentati che restituiscono il proprio stato attuale. Così una futura migrazione forzata diventa un'abitudine di progettazione una tantum.

3. **Progettate e rivedete davvero il contratto prima di scrivere l'implementazione, o l'interfaccia trapela dal codice?** La raccomandazione di lavorare prima sull'API chiede una specifica leggibile da macchina, rivista in anticipo, che generi documentazione, stub e simulati e permetta ai consumatori di integrarsi con un simulato mentre costruisci. Quando il contratto resta indietro rispetto all'implementazione, l'interfaccia espone la struttura interna del database e cambia ogni volta che cambia l'implementazione, che è il principale antipattern di questo capitolo. Il segnale da esaminare: un consumatore può iniziare oggi a integrarsi con il vostro simulato, o deve aspettare un backend funzionante? Per le API pubbliche e dei partner, dove l'interfaccia è la superficie di prodotto e la cosa più costosa da sbagliare, spendere un giorno sul contratto fa risparmiare settimane di andirivieni di supporto. Rendi la revisione del contratto un passaggio obbligatorio prima che inizi l'implementazione.

4. **Quando due team devono esporre la stessa capacità, quale stile di interazione vince, e chi ha l'autorità di dire no a un quarto protocollo?** Questo capitolo ti dice di scegliere REST, GraphQL, gRPC o messaggistica guidata dagli eventi in base all'adeguatezza all'interazione, ma su larga scala il rischio reale è che ogni team scelga il proprio preferito e i consumatori trovino una convenzione diversa a ogni endpoint. Una grande organizzazione paga quella frammentazione in librerie client, gateway, monitoraggio e carico cognitivo su ogni integratore che ora impara quattro idiomi anziché uno. Porta l'inventario dei protocolli già in produzione, l'interazione che ciascuno doveva servire e i consumatori che ne attraversano più di uno. La considerazione contraria è autentica: un valore predefinito condiviso riduce la proliferazione, ma un mandato rigido forza problemi a forma di gRPC in un buco a forma di REST. Indica l'organo per gli standard o la revisione architetturale che possiede il processo di eccezione, perché nei patrimoni aziendali e governativi una proliferazione di stili diventa una tassa permanente sull'integrazione e un problema difficile da invertire una volta che i partner dipendono da ciascuno.

5. **Qual è la nostra politica di deprecazione pubblicata, e possiamo dimostrare di rispettare davvero la finestra di supporto che pubblicizziamo?** Il capitolo tratta versionamento e deprecazione come disciplina: una politica scritta su quanto vivono le vecchie versioni, come si avvisano i consumatori e quale sovrapposizione hanno per migrare. Una promessa che non puoi far rispettare è peggio di nessuna, perché un grande ecosistema include consumatori con cui non parli mai e che continueranno a chiamare una versione ritirata finché non si romperà in produzione. Porta alla discussione le prove: quante versioni vive porti oggi, l'uso reale di ciascuna, se riesci a vedere quali consumatori chiamano ancora un endpoint deprecato e con quanto anticipo è stato annunciato l'ultimo ritiro. La pressione contraria è costo di manutenzione contro stabilità dei consumatori, ed entrambi sono reali. Per i partner aziendali con livelli di servizio contrattuali e per le API del settore pubblico che devono sopravvivere ad amministrazioni e cambi di fornitori, la finestra di supporto è un impegno che può sopravvivere al team che l'ha preso, quindi decidi chi ne è responsabile e come si dimostra sicuro un ritiro prima che avvenga.

6. **Come sappiamo che la nostra esperienza degli sviluppatori è buona, o la stiamo presumendo perché l'API funziona per noi?** Questo capitolo imposta ogni API come un prodotto la cui adozione dipende da documentazione di riferimento accurata, guide rapide, esempi, un ambiente di prova, un registro delle modifiche e un catalogo reperibile. I team scambiano di routine "l'API funziona" con "l'API è utilizzabile", e il divario si vede in ticket di supporto, integrazioni fallite e consumatori che rinunciano in silenzio. Porta segnali misurabili anziché opinioni: tempo alla prima chiamata riuscita per un nuovo integratore, volume di ticket di supporto per endpoint, quanto è obsoleta la documentazione pubblicata rispetto al contratto vivo e se un nuovo arrivato riesce ad arrangiarsi dal portale senza scrivere al tuo team. La tensione è che documentazione e portali costano sforzo vero che compete con il rilascio di funzionalità, eppure in un grande ecosistema una scarsa esperienza degli sviluppatori scarica il costo di integrazione su centinaia di consumatori insieme. Nel settore pubblico, dove un'API aperta serve sviluppatori esterni con cui non puoi coordinarti e la trasparenza è spesso obbligatoria, un'interfaccia utilizzabile, ben documentata e reperibile fa parte dell'obbligo di responsabilità pubblica, non è un di più.

## Lente settoriale

**Startup.** Con due o tre ingegneri e nessun tempo per le cerimonie, mantieni il contratto leggero ma reale: un'unica specifica leggibile da macchina con cui i tuoi primi clienti partner di progettazione possano integrarsi mentre costruisci. Non montare ancora un gateway API, un catalogo o un comitato di governance, ma fissa le due abitudini dolorose da aggiungere dopo, chiavi di idempotenza sulle scritture e paginazione a cursore sugli elenchi, perché aggiungerle a posteriori a un endpoint in produzione è una modifica incompatibile che non puoi permetterti. Privilegia un solo stile di interazione, quasi sempre REST, così da non portare proliferazione di protocolli nel tuo primo anno.

**Piccola impresa.** Senza uno specialista di API dedicato e con un budget ridotto, appoggiati a strumenti che generano documentazione, simulati e stub di client da una specifica, così che un generalista possa mantenere l'interfaccia senza una profonda competenza di protocollo. Pesa con attenzione comprare contro costruire: un gateway già pronto o una piattaforma di gestione delle API ti dà limitazione della frequenza, chiavi e un portale per sviluppatori che altrimenti faresti a mano. Mantieni piccola la superficie e coerenti le convenzioni, poiché ogni endpoint in più e ogni formato d'errore estemporaneo è qualcosa che un team esiguo deve supportare per sempre.

**Grande impresa.** Tra molti team autonomi, il problema centrale è la coerenza senza diventare un collo di bottiglia: una guida di stile condivisa, una revisione degli standard delle API, un catalogo che renda reperibili le interfacce e controlli automatici di compatibilità all'indietro nella CI, così che un'incompatibilità silenziosa faccia fallire la build anziché un'integrazione. Governa ogni API come un prodotto con un responsabile nominato, un ciclo di vita e una politica di deprecazione pubblicata, e misura adozione, carico di supporto e frequenza di modifiche incompatibili perché il portafoglio resti sano. Standardizza in tutta l'organizzazione gli stili di interazione e le regole di versionamento, perché a questa scala la frammentazione è l'impostazione predefinita costosa.

**Ente pubblico.** Regole sugli appalti, mandati di standard aperti e responsabilità pubblica plasmano ogni scelta. Pubblica apertamente il contratto, segui gli standard aperti imposti e offri un ambiente di prova e documentazione di riferimento, così che gli sviluppatori esterni con cui non puoi coordinarti possano arrangiarsi da soli. Tratta la compatibilità all'indietro a lungo termine come un requisito di policy, poiché le integrazioni devono sopravvivere ad amministrazioni e cambi di fornitori, e rendi le modifiche incompatibili rare, fortemente governate e annunciate con largo anticipo. Mantieni l'API e la sua documentazione abbastanza trasparenti da reggere il controllo pubblico e di audit ed evita formati proprietari che intrappolerebbero una futura amministrazione.

## Esempi

**Startup.** Una startup in fase seed che rilascia la sua prima API pubblica scrive il contratto come specifica leggibile da macchina prima di programmare, così che i suoi due clienti partner di progettazione possano integrarsi con un simulato mentre il backend è ancora in costruzione. Anche con una manciata di consumatori, aggiunge chiavi di idempotenza all'endpoint di addebito e paginazione a cursore a ogni elenco, perché aggiungerle una volta che i partner dipendono dall'API significherebbe una modifica incompatibile che non può permettersi. Il contratto iniziale costa un giorno e risparmia settimane di andirivieni di supporto.

**Grande impresa.** Una grande società di pagamenti espone un'API REST pubblica a migliaia di esercenti. Ogni endpoint di scrittura accetta una chiave di idempotenza, così che una ripetizione di rete non crei mai un addebito duplicato. Ogni endpoint di elenco usa la paginazione a cursore. Gli errori portano codici stabili documentati in un riferimento pubblico. Una politica formale di deprecazione garantisce una lunga finestra di supporto per qualsiasi versione, con preavviso e guide alla migrazione. Questa disciplina è un vantaggio competitivo: gli integratori confidano che l'API non si romperà sotto di loro.

**Ente pubblico.** Un servizio digitale nazionale pubblica un'API aperta per i dati dei cittadini, seguendo gli standard aperti imposti e un processo di progettazione che parte dall'API. Il contratto è specificato e rivisto prima della costruzione, pubblicato in un catalogo centrale delle API del governo e servito con un ambiente di prova, così che gli sviluppatori di terze parti, che non possono essere coordinati uno per uno, possano integrarsi da soli. La compatibilità all'indietro a lungo termine è un requisito di policy, perché le integrazioni devono sopravvivere ad amministrazioni e cambi di fornitori. Le modifiche incompatibili sono quindi rare e fortemente governate.

## Business case: motivazioni, ROI e TCO

Una buona progettazione delle API abbassa il costo di integrazione, che è spesso il costo maggiore nel collegare sistemi e inserire partner. Con un'API chiara, stabile e ben documentata, i consumatori si integrano in giorni senza un solo ticket di supporto. Una scadente genera un carico di supporto infinito, integrazioni fallite e danno reputazionale. Quando l'API è essa stessa il prodotto, l'esperienza degli sviluppatori guida direttamente adozione e ricavi.

Il più grande costo nascosto sono le modifiche incompatibili. Ogni modifica incompatibile impone una migrazione coordinata tra tutti i consumatori, team interni e partner esterni alla pari, e il costo totale scala con il numero di consumatori e con la difficoltà per loro di muoversi in sincrono. Investire in anticipo in progettazione guidata dal contratto, compatibilità all'indietro e disciplina di versionamento evita questi costosi eventi di migrazione che coinvolgono l'intera organizzazione. Quando parli con la leadership, presenta la qualità delle API come la leva per l'autonomia dei team, la crescita dell'ecosistema dei partner e l'evitare costose migrazioni forzate. Segui tempo di integrazione, volume di ticket di supporto e frequenza di modifiche incompatibili come tue prove.

## Antipattern e insidie

- **API che partono dall'implementazione:** l'interfaccia lascia trapelare la struttura interna del database e cambia ogni volta che cambia l'implementazione.
- **Modifiche incompatibili silenziose:** riutilizzare un campo o irrigidire la validazione senza cambiare versione rompe i consumatori in modo imprevedibile.
- **Interfacce verbose:** progetti che richiedono molti viaggi di andata e ritorno per una sola operazione logica, danneggiando prestazioni e usabilità.
- **Convenzioni incoerenti:** ogni endpoint inventa i propri nomi, formato d'errore e paginazione, così che i client non possono generalizzare.
- **Nessuna paginazione né limitazione della frequenza:** endpoint che funzionano nei test e crollano con volumi di dati o carico reali.
- **Scritture non idempotenti:** le ripetizioni causano duplicati; un singolo singhiozzo di rete corrompe i dati.
- **Proliferazione di versioni:** troppe versioni vive senza deprecazione, che moltiplicano la manutenzione fino a renderla ingestibile.
- **Documentazione come ripensamento:** riferimenti non documentati o obsoleti che scaricano tutto il costo di integrazione sui consumatori.

## Modello di maturità

- **Livello 1, Avvio:** le API emergono dall'implementazione come sottoprodotto; non ci sono convenzioni condivise; l'interfaccia lascia trapelare la struttura interna del database; le modifiche incompatibili sono comuni, non annunciate e scoperte quando l'integrazione di un consumatore fallisce.
- **Livello 2, Sviluppo:** alcuni team seguono convenzioni REST di base, versionano in modo informale e scrivono la documentazione a mano, ma la pratica è incoerente tra i team; idempotenza, paginazione e limitazione della frequenza compaiono su alcuni endpoint e non su altri; i consumatori imparano ancora le stranezze di ogni API caso per caso.
- **Livello 3, Standardizzazione:** la progettazione guidata dal contratto con specifiche leggibili da macchina è documentata e fatta rispettare in tutta l'organizzazione; una politica di deprecazione pubblicata, semantica degli errori coerente e idempotenza, paginazione a cursore e limitazione della frequenza obbligatorie si applicano a ogni nuovo endpoint; una guida di stile condivisa e una revisione degli standard delle API mantengono coerenti le interfacce tra i team.
- **Livello 4, Gestione:** il portafoglio di API è misurato e controllato rispetto a valori di riferimento: controlli automatici di compatibilità all'indietro fanno da cancello a ogni modifica nella CI e si seguono tempo alla prima chiamata riuscita, volume di ticket di supporto per endpoint, frequenza di modifiche incompatibili, numero di versioni vive e uso per endpoint, così che le decisioni di deprecazione e progettazione poggino sulle prove anziché sulle opinioni. Ogni API è un prodotto governato in un catalogo con un responsabile nominato, e le metriche innescano azioni quando un servizio si allontana dai propri obiettivi.
- **Livello 5, Orchestrazione:** la strategia delle API è migliorata di continuo e integrata in tutta l'organizzazione; catalogo, gateway, regole di versionamento e cancelli di compatibilità funzionano come un unico sistema; l'organizzazione ritira, consolida e ridefinisce regolarmente le interfacce in base ad adozione e costo misurati; gli standard di stile di interazione e di versionamento si adattano al mutare di ecosistema, partner e tecnologia, e le modifiche incompatibili sono rare e ben gestite.

## Spunti di discussione

- Come decidete quando un'API interna è abbastanza stabile da essere pubblicata all'esterno?
- Qual è la giusta finestra di supporto per le versioni deprecate nel vostro contesto, e chi la paga?
- Dove GraphQL o gRPC dovrebbero sostituire REST internamente, e dove aggiungerebbero più complessità che valore?
- Come fate rispettare la coerenza delle API tra molti team autonomi senza diventare un collo di bottiglia?
- Come dovrebbero cambiare le convenzioni di progettazione le API consumabili dall'IA e le interfacce di strumenti per agenti?
- Quali controlli automatici possono cogliere le modifiche incompatibili all'indietro prima del rilascio?

## Punti chiave

- Progetta prima il contratto; l'API è un prodotto e una promessa di lunga durata.
- La compatibilità all'indietro protegge i consumatori; le modifiche incompatibili richiedono nuove versioni e percorsi di migrazione.
- Scegli REST, GraphQL, gRPC o eventi in base all'adeguatezza all'interazione, non alla moda.
- Incorpora idempotenza, paginazione, limitazione della frequenza ed errori coerenti fin dal primo giorno.
- Governa le API come prodotti con responsabili, cataloghi e una solida esperienza degli sviluppatori.

## Riferimenti e letture di approfondimento

- Roy Fielding, *Architectural Styles and the Design of Network-based Software Architectures* (tesi di dottorato)
- Arnaud Lauret, *The Design of Web APIs*
- Mike Amundsen, *RESTful Web APIs* e *Design and Build Great Web APIs*
- Sam Newman, *Building Microservices*
- OpenAPI Specification; JSON Schema (come standard di riferimento)
- Martin Kleppmann, *Designing Data-Intensive Applications*
