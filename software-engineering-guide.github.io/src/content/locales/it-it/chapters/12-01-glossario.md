# 12.1 Glossario

Questo glossario definisce i termini e gli acronimi usati in tutta la guida.
Le voci sono raggruppate in ordine alfabetico secondo i lemmi inglesi, che sono
mantenuti perché sono i termini che incontrerete in strumenti, standard e
letteratura. Dove una voce ha un acronimo comune, è mostrato tra parentesi. Le
definizioni sono volutamente concise; consultate il capitolo pertinente per una
trattazione più completa.

## A

**[ABAC (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control)**: Un modello di autorizzazione che concede l'accesso in base agli attributi valutati dell'utente, della risorsa, dell'azione e dell'ambiente (per esempio reparto, livello di autorizzazione, ora del giorno) anziché a ruoli fissi. Offre un controllo a grana fine, guidato da politiche, al prezzo di una complessità maggiore rispetto a RBAC.

**[Accessibility (a11y)](https://en.wikipedia.org/wiki/Computer_accessibility)**: La pratica di progettare e costruire software in modo che le persone con disabilità possano percepirlo, comprenderlo, navigarlo e interagirvi. Il numeronimo "a11y" abbrevia le 11 lettere tra "a" e "y".

**ADR (Architecture Decision Record)**: Un breve documento versionato che cattura una singola decisione architetturale o tecnica significativa, il suo contesto, le opzioni considerate e le sue conseguenze. Gli ADR creano una storia durevole e rivedibile del perché un sistema è com'è.

**Aggregate**: Nel Domain-Driven Design, un gruppo di oggetti di dominio trattato come un'unica unità per le modifiche ai dati, con un'entità che funge da radice dell'aggregato e fa rispettare gli invarianti. Gli aggregati definiscono i confini di consistenza e di transazione.

**[API (Application Programming Interface)](https://en.wikipedia.org/wiki/API)**: Un contratto definito attraverso cui un software richiede servizi o dati a un altro. Le API ben progettate nascondono i dettagli di implementazione e offrono interfacce stabili e versionate.

**API-first**: Un approccio di sviluppo in cui il contratto dell'API è progettato e concordato prima dell'implementazione, così che consumatori e fornitori possano lavorare in parallelo rispetto a una specifica condivisa.

**arc42**: Una struttura aperta, basata su modelli, per documentare l'architettura software, organizzata in dodici sezioni che coprono contesto, vincoli, blocchi costruttivi, esecuzione, distribuzione e decisioni.

**[ARIA (Accessible Rich Internet Applications)](https://en.wikipedia.org/wiki/WAI-ARIA)**: Una specifica W3C che definisce ruoli, stati e proprietà che rendono comprensibili alle tecnologie assistive, come i lettori di schermo, i componenti web dinamici e personalizzati.

**ASR (Architecturally Significant Requirement)**: Un requisito che ha un effetto misurabile e ad ampio raggio sull'architettura, come un vincolo di prestazioni, disponibilità, sicurezza o normativo. Gli ASR guidano le decisioni di progetto più rilevanti.

**ASVS (Application Security Verification Standard)**: Uno standard OWASP che fornisce una lista di controllo graduata di requisiti e test di sicurezza per progettare, costruire e verificare applicazioni sicure.

**[Autoscaling](https://en.wikipedia.org/wiki/Autoscaling)**: L'adeguamento automatico del numero di istanze di calcolo in esecuzione (o della loro dimensione) in risposta al carico, così che la capacità segua la domanda senza intervento manuale. Integra, ma non sostituisce, la pianificazione deliberata della capacità.

**[Availability](https://en.wikipedia.org/wiki/Availability)**: La proporzione di tempo in cui un sistema è operativo e in grado di servire richieste, spesso espressa in "nove" (per esempio 99,9%). È un obiettivo di affidabilità fondamentale codificato in SLO e SLA.

## B

**Backpressure**: Un meccanismo di controllo del flusso in cui un componente sotto carico segnala ai produttori a monte di rallentare, evitando code illimitate e fallimenti a cascata. È centrale per i sistemi di streaming e a messaggi affidabili.

**[BDD (Behaviour-Driven Development)](https://en.wikipedia.org/wiki/Behavior-driven_development)**: Una pratica collaborativa che esprime i requisiti come esempi concreti e leggibili di comportamento (spesso nella forma Given/When/Then) che fungono anche da test di accettazione automatici.

**BFF (Backend for Frontend)**: Un pattern architetturale in cui un servizio backend dedicato è costruito per uno specifico frontend o tipo di client, adattando la modellazione e l'aggregazione dei dati alle esigenze di quel client.

**[BI (Business Intelligence)](https://en.wikipedia.org/wiki/Business_intelligence)**: Gli strumenti, i processi e le pratiche per raccogliere, integrare e analizzare dati aziendali a supporto di rendicontazione, dashboard e decisioni.

**Blameless postmortem**: Una revisione di un incidente che si concentra sulle cause sistemiche e sull'apprendimento anziché sulle colpe individuali, partendo dal presupposto che le persone agiscano in modo ragionevole date le informazioni e gli incentivi che avevano.

**[Blue-green deployment](https://en.wikipedia.org/wiki/Blue-green_deployment)**: Una strategia di rilascio che gestisce due ambienti di produzione identici ("blue" e "green"), instradando il traffico verso uno mentre l'altro è aggiornato, il che permette un passaggio e un rollback quasi istantanei.

**[BM25](https://en.wikipedia.org/wiki/Okapi_BM25)**: Una funzione di ranking molto usata per la ricerca full-text che valuta quanto bene un documento corrisponde a una query usando la frequenza dei termini, la frequenza inversa nei documenti e la lunghezza del documento. È il ranking lessicale predefinito in molti motori di ricerca.

**Bounded context**: Nel Domain-Driven Design, un confine esplicito entro cui un particolare modello di dominio e il suo linguaggio ubiquo si applicano in modo coerente. Impedisce che i concetti siano confusi tra le diverse parti di un grande sistema.

**Build cache**: Un archivio di output di build calcolati in precedenza, indicizzati per gli input che li hanno prodotti, così che il lavoro invariato sia riusato anziché ricostruito. Una build cache remota condivisa permette a un intero team e alla sua CI di riusare i risultati l'uno dell'altro.

**[Bus factor](https://en.wikipedia.org/wiki/Bus_factor)**: Il numero di persone che dovrebbero essere perse (metaforicamente "investite da un autobus") prima che un progetto si fermi per mancanza di conoscenze essenziali. Un bus factor basso segnala competenze concentrate e non documentate e rischio organizzativo.

## C

**[Cache eviction policy](https://en.wikipedia.org/wiki/Cache_replacement_policies)**: La regola che una cache usa per decidere quale voce rimuovere quando è piena, come la meno usata di recente (LRU) o la meno usata di frequente (LFU). La politica determina il tasso di successo e, con esso, il valore della cache.

**[Cache invalidation](https://en.wikipedia.org/wiki/Cache_invalidation)**: Il problema di rimuovere o aggiornare i dati in cache una volta che la fonte sottostante cambia, così che i lettori non vedano valori obsoleti. È notoriamente uno dei problemi più difficili dell'informatica.

**[Cache stampede](https://en.wikipedia.org/wiki/Cache_stampede)**: Una modalità di fallimento in cui molti client mancano la cache per la stessa chiave nello stesso momento e colpiscono tutti insieme l'origine, sopraffacendola. La coalescenza delle richieste e la scadenza scaglionata la prevengono. Detta anche thundering herd.

**Canary release**: Una tecnica di distribuzione che espone prima una nuova versione a un piccolo sottoinsieme di utenti o di traffico, osserva eventuali problemi e poi espande progressivamente il rilascio se le metriche restano sane.

**[CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem)**: Un principio secondo cui un archivio di dati distribuito può garantire al massimo due tra Consistency, Availability e Partition tolerance contemporaneamente; poiché le partizioni sono inevitabili, i progettisti scambiano di fatto consistenza contro disponibilità durante di esse.

**[C4 model](https://en.wikipedia.org/wiki/C4_model)**: Un approccio leggero per visualizzare l'architettura software a quattro livelli di astrazione: System Context, Containers, Components e Code.

**[CD (Continuous Delivery / Continuous Deployment)](https://en.wikipedia.org/wiki/Continuous_delivery)**: La Continuous Delivery mantiene il software in uno stato rilasciabile così da poterlo distribuire in qualsiasi momento con un'approvazione manuale; la Continuous Deployment rilascia automaticamente ogni modifica che supera la pipeline.

**[CDN (Content Delivery Network)](https://en.wikipedia.org/wiki/Content_delivery_network)**: Una rete geograficamente distribuita di server edge che mettono in cache e servono contenuti vicino agli utenti, riducendo la latenza e alleggerendo l'infrastruttura di origine.

**Chain-of-thought prompting**: Una tecnica di prompting che chiede a un modello linguistico di svolgere passi intermedi di ragionamento prima di dare una risposta finale, migliorando le prestazioni sui problemi a più passi al costo di un output più lungo e lento.

**[CI (Continuous Integration)](https://en.wikipedia.org/wiki/Continuous_integration)**: La pratica di unire frequentemente le modifiche degli sviluppatori in una linea principale condivisa, con ogni unione convalidata da una build e una suite di test automatiche per individuare presto i problemi di integrazione.

**[CI/CD](https://en.wikipedia.org/wiki/CI/CD)**: La pipeline combinata di Continuous Integration e Continuous Delivery/Deployment che automatizza la costruzione, il test e il rilascio del software.

**CMMC (Cybersecurity Maturity Model Certification)**: Un programma del Dipartimento della Difesa degli Stati Uniti che certifica la maturità di cybersicurezza degli appaltatori che trattano informazioni di contratti federali e informazioni non classificate controllate.

**[Cohesion](https://en.wikipedia.org/wiki/Cohesion_(computer_science))**: Il grado in cui gli elementi all'interno di un modulo stanno bene insieme e servono un unico scopo ben definito. Un'alta coesione, abbinata a un basso accoppiamento, è un segno distintivo di un progetto manutenibile.

**Context window**: La quantità massima di testo, misurata in token, che un modello linguistico può considerare in una volta, comprendendo input e output. È un budget scarso che il design di prompt e contesto deve gestire deliberatamente.

**[Conway's Law](https://en.wikipedia.org/wiki/Conway's_law)**: L'osservazione che la struttura di un sistema tende a rispecchiare la struttura di comunicazione dell'organizzazione che lo costruisce. La "manovra di Conway inversa" modella deliberatamente i team per produrre un'architettura desiderata.

**Core Web Vitals**: Un insieme di metriche di prestazioni web centrate sull'utente definite da Google (come Largest Contentful Paint, Interaction to Next Paint e Cumulative Layout Shift) che misurano caricamento, interattività e stabilità visiva.

**[Cost of delay](https://en.wikipedia.org/wiki/Cost_of_delay)**: Il costo economico di non avere ancora finito qualcosa, espresso come valore perso per unità di tempo. Renderlo esplicito trasforma la prioritizzazione da opinione in aritmetica e sostiene regole di ordinamento come weighted shortest job first.

**[Coupling](https://en.wikipedia.org/wiki/Coupling_(computer_programming))**: Il grado di interdipendenza tra moduli o servizi. Un accoppiamento debole limita l'effetto a catena del cambiamento ed è un obiettivo centrale di una buona architettura.

**CQRS (Command Query Responsibility Segregation)**: Un pattern che separa il modello usato per cambiare lo stato (comandi) dal modello usato per leggerlo (query), permettendo a ciascuno di essere ottimizzato e scalato in modo indipendente.

**[CVE (Common Vulnerabilities and Exposures)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)**: Un catalogo pubblico di vulnerabilità di sicurezza divulgate, ciascuna con un identificatore univoco così che strumenti e team possano riferirsi allo stesso difetto senza ambiguità.

**CWV**: Vedi Core Web Vitals.

## D

**[DAST (Dynamic Application Security Testing)](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)**: Test di sicurezza che sondano un'applicazione in esecuzione dall'esterno, senza accesso al codice sorgente, per trovare vulnerabilità che compaiono a runtime.

**Data-ink ratio**: Un principio di Edward Tufte secondo cui un grafico dovrebbe spendere la maggior parte del proprio inchiostro sui dati stessi e poco sulla decorazione, rimuovendo griglie, bordi e chartjunk che non informano.

**[Data mesh](https://en.wikipedia.org/wiki/Data_mesh)**: Un'architettura dei dati decentralizzata e un modello operativo che tratta i dati come un prodotto posseduto dai team di dominio, sostenuto da un'infrastruttura di piattaforma self-service e da una governance federata.

**[Data visualisation](https://en.wikipedia.org/wiki/Data_and_information_visualization)**: La pratica di codificare i dati in forma visiva (posizione, lunghezza, colore e simili) in modo che schemi, confronti e tendenze diventino percepibili e le decisioni meglio informate.

**[DDD (Domain-Driven Design)](https://en.wikipedia.org/wiki/Domain-driven_design)**: Un approccio alla progettazione del software che centra il modello sul dominio di business, usando un linguaggio ubiquo condiviso, bounded context e blocchi costruttivi come entità, value object e aggregati.

**Design tokens**: Valori con nome, indipendenti dalla piattaforma (colori, spaziature, tipografia e simili), che codificano le decisioni di design così da poter essere condivisi in modo coerente in un sistema di design e in più prodotti.

**DevEx / DevX (Developer Experience)**: La qualità complessiva dell'interazione quotidiana di uno sviluppatore con strumenti, piattaforme e processi, comprendente attrito, velocità del riscontro e carico cognitivo.

**[DevOps](https://en.wikipedia.org/wiki/DevOps)**: Una cultura e un insieme di pratiche che uniscono sviluppo e operazioni software per accorciare i cicli di consegna, aumentare la frequenza di distribuzione e migliorare l'affidabilità tramite automazione e titolarità condivisa.

**DORA (DevOps Research and Assessment)**: Un programma di ricerca e le sue quattro metriche di consegna molto usate (frequenza di distribuzione, tempo di attesa per le modifiche, tasso di fallimento delle modifiche e tempo di ripristino del servizio) per confrontare le prestazioni di consegna del software.

**DPIA (Data Protection Impact Assessment)**: Una valutazione strutturata, richiesta dal GDPR per i trattamenti ad alto rischio, che individua e mitiga i rischi per la privacy prima che un progetto proceda.

**Drift (configuration)**: La graduale divergenza dello stato reale di un sistema dal suo stato dichiarato o voluto, comunemente causata da modifiche manuali; Infrastructure as Code e GitOps mirano a rilevarla e correggerla.

**Drift (model)**: Nel machine learning, il degrado delle prestazioni di un modello nel tempo man mano che cambiano le proprietà statistiche dei dati di input (data drift) o la relazione che si sta modellando (concept drift).

**[DR (Disaster Recovery)](https://en.wikipedia.org/wiki/Disaster_recovery)**: La strategia, le procedure e l'infrastruttura per ripristinare servizio e dati dopo un grave evento dirompente, tipicamente governate da obiettivi RTO e RPO.

**[DRY (Don't Repeat Yourself)](https://en.wikipedia.org/wiki/Don't_repeat_yourself)**: Un principio di progettazione secondo cui ogni pezzo di conoscenza dovrebbe avere un'unica rappresentazione autorevole, riducendo la duplicazione e il rischio di aggiornamenti incoerenti.

## E

**East-west traffic**: Traffico di rete tra servizi all'interno di un sistema o di un data center, in contrapposizione al traffico north-south tra il sistema e i client esterni. Una service mesh governa tipicamente il traffico east-west.

**[Edge computing](https://en.wikipedia.org/wiki/Edge_computing)**: Eseguire calcolo e archiviazione vicino a dove i dati sono prodotti o consumati anziché in un luogo centrale, per ridurre latenza e banda. Le content delivery network ne sono una forma precoce e diffusa.

**[Elasticity](https://en.wikipedia.org/wiki/Elasticity_(cloud_computing))**: La capacità di un sistema di acquisire e rilasciare automaticamente risorse in risposta alla domanda che cambia, così che la capacità segua da vicino il carico.

**[ELT (Extract, Load, Transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform)**: Un pattern di integrazione dei dati che carica prima i dati grezzi in un archivio di destinazione e li trasforma lì, sfruttando la scala dei moderni warehouse e lakehouse.

**[Embedding](https://en.wikipedia.org/wiki/Word_embedding)**: Una rappresentazione di testo, immagini o altri dati come vettore numerico denso, posizionato in modo che elementi simili stiano vicini. Gli embedding alimentano la ricerca semantica e vettoriale e la generazione aumentata dal recupero.

**[EN 301 549](https://en.wikipedia.org/wiki/EN_301_549)**: Lo standard europeo che specifica i requisiti di accessibilità per prodotti e servizi ICT, citato dagli appalti del settore pubblico in tutta l'UE e allineato a WCAG.

**Error budget**: La quantità ammissibile di inaffidabilità consentita da un SLO in un periodo; quando è esaurita, i team danno priorità al lavoro sull'affidabilità rispetto alle nuove funzionalità. Concilia la tensione tra velocità e stabilità.

**[ETL (Extract, Transform, Load)](https://en.wikipedia.org/wiki/Extract,_transform,_load)**: Un pattern di integrazione dei dati che estrae i dati dalle fonti, li trasforma in una forma di destinazione e li carica in una destinazione come un warehouse.

**[EU AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act)**: Regolamento dell'Unione Europea che classifica i sistemi di IA per rischio e impone obblighi di conseguenza, vietando certi usi e regolando fortemente i sistemi ad alto rischio.

**[Eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency)**: Un modello di consistenza nei sistemi distribuiti in cui le repliche possono divergere temporaneamente ma convergono allo stesso stato una volta cessata la propagazione degli aggiornamenti.

## F

**[Feature flag / feature toggle](https://en.wikipedia.org/wiki/Feature_toggle)**: Un meccanismo per abilitare o disabilitare una funzionalità a runtime senza ridistribuire, usato per rilasci graduali, sperimentazione e controllo operativo.

**Feature store**: Un sistema centralizzato per definire, archiviare e servire in modo coerente feature di machine learning curate sia per l'addestramento sia per l'inferenza, riducendo duplicazione e training/serving skew.

**[FedRAMP (Federal Risk and Authorisation Management Program)](https://en.wikipedia.org/wiki/FedRAMP)**: Un programma del governo statunitense che standardizza la valutazione di sicurezza, l'autorizzazione e il monitoraggio continuo dei servizi cloud usati dalle agenzie federali.

**Few-shot prompting**: Fornire a un modello linguistico una manciata di esempi svolti nel prompt per dimostrare il compito e il formato di output desiderati, in contrapposizione allo zero-shot prompting, che dà istruzioni senza esempi.

**FinOps**: Una disciplina e pratica culturale che porta responsabilità finanziaria alla spesa cloud variabile, dando a team di ingegneria, finanza e business la titolarità condivisa di costo e valore.

**[FISMA (Federal Information Security Modernisation Act)](https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act)**: Legge statunitense che richiede alle agenzie federali di attuare, documentare e monitorare programmi di sicurezza delle informazioni, resa operativa in gran parte tramite le indicazioni NIST.

**Flow efficiency**: La proporzione del tempo di attesa complessivo che un elemento di lavoro trascorre in lavorazione attiva anziché in attesa, calcolata come tempo a valore aggiunto diviso tempo di attesa complessivo. La maggior parte dei sistemi è sorprendentemente bassa, spesso sotto il 15 per cento.

**Four-eyes principle**: Un controllo che richiede che un'azione significativa sia rivista o approvata da almeno due persone, riducendo la probabilità di errore o malversazione.

**[Fuzz testing (fuzzing)](https://en.wikipedia.org/wiki/Fuzzing)**: Una tecnica di test automatica che fornisce a un programma input malformati, casuali o inattesi per scoprire arresti anomali, difetti di sicurezza e difetti nei casi limite.

## G

**[GDPR (General Data Protection Regulation)](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)**: Il regolamento dell'Unione Europea che disciplina il trattamento dei dati personali, concedendo diritti alle persone e imponendo obblighi a titolari e responsabili del trattamento, con sanzioni significative per l'inosservanza.

**GitOps**: Un modello operativo che usa Git come unica fonte di verità per infrastruttura e applicazioni dichiarative, con l'automazione che riconcilia di continuo il sistema in esecuzione con lo stato committato.

**Golden path / paved road**: Un modo ben supportato e con una posizione precisa per costruire e rilasciare software in un'organizzazione, progettato per rendere la scelta sicura, conforme e affidabile la più facile.

**Golden record**: Nella gestione dei dati anagrafici, la versione unica, riconciliata e autorevole di un'entità di business (come un cliente) assemblata da più sistemi sorgente tramite regole di corrispondenza e di sopravvivenza.

**[Gradual typing](https://en.wikipedia.org/wiki/Gradual_typing)**: Un approccio dei sistemi di tipi che permette a tipizzazione statica e dinamica di coesistere in un'unica base di codice, così che i tipi possano essere aggiunti in modo incrementale a un programma a tipizzazione dinamica. Type hint e controllori di tipi opzionali ne sono esempi comuni.

**[GraphQL](https://en.wikipedia.org/wiki/GraphQL)**: Un linguaggio di query e runtime per API che permette ai client di richiedere esattamente i dati di cui hanno bisogno in una sola chiamata, usando uno schema fortemente tipizzato.

**[gRPC](https://en.wikipedia.org/wiki/gRPC)**: Un framework di chiamata di procedura remota ad alte prestazioni, basato sul contratto, che usa HTTP/2 e, tipicamente, Protocol Buffers per una comunicazione efficiente tra servizi.

## H

**Hermetic build**: Una build che dipende solo da input dichiarati esplicitamente ed è isolata dall'ambiente ospite, così da produrre lo stesso output ovunque. L'ermeticità è la fondazione delle build riproducibili e di una cache affidabile.

**[HSM (Hardware Security Module)](https://en.wikipedia.org/wiki/Hardware_security_module)**: Un dispositivo hardware a prova di manomissione che genera, archivia e usa chiavi crittografiche, offrendo una protezione delle chiavi più forte degli approcci solo software.

**[HIPAA (Health Insurance Portability and Accountability Act)](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)**: Legge statunitense che, tra l'altro, fissa requisiti per la salvaguardia delle informazioni sanitarie protette (PHI) e ne disciplina l'uso e la divulgazione.

**Horizontal scaling**: Aumentare la capacità aggiungendo più istanze o nodi ("scaling out") anziché rendere più potente un singolo nodo. Sta alla base della maggior parte delle architetture resilienti su larga scala.

## I

**[IaC (Infrastructure as Code)](https://en.wikipedia.org/wiki/Infrastructure_as_code)**: La pratica di definire e predisporre l'infrastruttura tramite configurazione leggibile da macchina e sotto controllo di versione anziché con processi manuali, permettendo ripetibilità e revisione.

**[IAM (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_management)**: Il quadro di politiche e tecnologie che assicura che le giuste identità abbiano il giusto accesso alle giuste risorse nei momenti giusti.

**IDP / IdP**: "IDP" indica comunemente una Internal Developer Platform, lo strato di strumenti self-service che astrae l'infrastruttura per i team di prodotto; "IdP" indica un Identity Provider, un servizio che autentica gli utenti ed emette asserzioni. Il contesto distingue i due.

**[Idempotency](https://en.wikipedia.org/wiki/Idempotence)**: Una proprietà per cui eseguire un'operazione più volte ha lo stesso effetto che eseguirla una volta, essenziale per ritentativi sicuri nei sistemi distribuiti e nelle API.

**[i18n (Internationalisation)](https://en.wikipedia.org/wiki/Internationalization_and_localization)**: Progettare e costruire il software in modo che possa essere adattato a lingue, regioni e convenzioni culturali diverse senza modifiche ingegneristiche. Il numeronimo abbrevia le 18 lettere tra "i" e "n".

**Immutable artefact**: Un output di build che, una volta prodotto e versionato, non viene mai modificato; qualsiasi cambiamento produce una nuova versione. L'immutabilità rende i rilasci riproducibili e permette di costruire una volta e promuovere lo stesso artefatto tra gli ambienti.

**InnerSource**: L'applicazione delle pratiche di sviluppo open source (trasparenza, repository condivisi e contributo tra team) dentro una singola organizzazione.

**IaC drift**: Vedi Drift (configuration).

**[Inverted index](https://en.wikipedia.org/wiki/Inverted_index)**: La struttura dati centrale di un motore di ricerca, che mappa ogni termine all'elenco dei documenti che lo contengono, così che le query possano ricevere risposta senza scansionare ogni documento.

**[ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001)**: Uno standard internazionale che specifica i requisiti per un Sistema di Gestione della Sicurezza delle Informazioni (ISMS), fornendo un quadro certificabile per gestire il rischio di sicurezza delle informazioni.

**ISO/IEC 42001**: Uno standard internazionale che specifica i requisiti per un Sistema di Gestione dell'IA, dando alle organizzazioni un quadro certificabile per governare in modo responsabile lo sviluppo e l'uso dell'IA.

## J

**[JWT (JSON Web Token)](https://en.wikipedia.org/wiki/JSON_Web_Token)**: Un formato di token compatto, firmato (e opzionalmente cifrato) usato per trasportare asserzioni tra le parti, comunemente per autenticazione e autorizzazione nei sistemi web e API.

## K

**[Kanban](https://en.wikipedia.org/wiki/Kanban_(development))**: Un metodo lean di flusso di lavoro che visualizza il lavoro su una bacheca, limita il lavoro in corso e gestisce il flusso per migliorare produttività e prevedibilità.

**[KISS (Keep It Simple, Stupid)](https://en.wikipedia.org/wiki/KISS_principle)**: Un principio di progettazione che favorisce la soluzione più semplice che soddisfa il bisogno, sulla base del fatto che la complessità inutile aumenta costo e rischio.

**KMS (Key Management Service)**: Un sistema per creare, archiviare, ruotare e controllare l'accesso alle chiavi crittografiche, spesso sostenuto da moduli di sicurezza hardware.

**[KPI (Key Performance Indicator)](https://en.wikipedia.org/wiki/Performance_indicator)**: Una misura quantificabile usata per seguire il progresso verso uno specifico obiettivo di business o operativo.

## L

**Lakehouse**: Un'architettura dei dati che combina l'archiviazione economica e flessibile di un data lake con le funzioni di gestione, transazioni e prestazioni di un data warehouse.

**[Lead time](https://en.wikipedia.org/wiki/Lead_time)**: Il tempo trascorso da quando una modifica è richiesta (o committata) a quando è consegnata in produzione; una metrica di consegna DORA centrale.

**[Least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)**: Un principio di sicurezza che concede a ogni utente, processo o sistema solo l'accesso minimo necessario a svolgere la propria funzione, limitando il danno da compromissione o errore.

**[Little's Law](https://en.wikipedia.org/wiki/Little's_law)**: Un risultato della teoria delle code secondo cui il numero medio di elementi in un sistema stabile è pari al tasso medio di arrivo moltiplicato per il tempo medio che ciascun elemento trascorre nel sistema. Lega lavoro in corso, produttività e tempo di attesa complessivo.

**[LLM (Large Language Model)](https://en.wikipedia.org/wiki/Large_language_model)**: Un modello di machine learning addestrato su corpora di testo molto grandi per prevedere e generare linguaggio, capace di compiti come riassunto, traduzione e generazione di codice.

**[l10n (Localisation)](https://en.wikipedia.org/wiki/Language_localisation)**: Adattare il software internazionalizzato a uno specifico locale, comprese traduzione, formattazione e convenzioni culturali. Il numeronimo abbrevia le 10 lettere tra "l" e "n".

## M

**[MDM (Master Data Management)](https://en.wikipedia.org/wiki/Master_data_management)**: La disciplina e gli strumenti per creare e mantenere una vista unica, autorevole e coerente delle entità di business centrali (come clienti o prodotti) tra i sistemi.

**MITRE ATT&CK**: Una base di conoscenza pubblica e curata di tattiche e tecniche reali degli avversari, molto usata per pianificare esercizi di red team, guidare l'ingegneria del rilevamento e descrivere le minacce con un vocabolario condiviso.

**Mean Time to Recovery (MTTR)**: Il tempo medio impiegato per ripristinare il servizio dopo un guasto; una comune metrica di affidabilità e di gestione degli incidenti.

**[Mob programming](https://en.wikipedia.org/wiki/Mob_programming)**: Una pratica in cui un intero team lavora insieme sullo stesso compito allo stesso computer, ruotando chi digita, per condividere conoscenza e prendere decisioni collettivamente.

**[MLOps (Machine Learning Operations)](https://en.wikipedia.org/wiki/MLOps)**: L'insieme di pratiche che distribuiscono, monitorano e mantengono in modo affidabile ed efficiente i modelli di machine learning in produzione, estendendo i principi DevOps al ciclo di vita del ML.

**[Monorepo](https://en.wikipedia.org/wiki/Monorepo)**: Un singolo repository di controllo di versione che contiene il codice di molti progetti o dell'intera organizzazione, permettendo strumenti condivisi e modifiche atomiche tra progetti al costo di strumenti specializzati di scalatura.

**mTLS (mutual TLS)**: Una configurazione di Transport Layer Security in cui entrambe le parti presentano e verificano certificati, così che ciascuna autentichi l'altra. È un predefinito per il traffico tra servizi in una service mesh e nelle reti zero-trust. Vedi anche [mutual authentication](https://en.wikipedia.org/wiki/Mutual_authentication).

**[Mutation testing](https://en.wikipedia.org/wiki/Mutation_testing)**: Una tecnica che introduce deliberatamente piccoli difetti ("mutanti") nel codice per verificare se la suite di test li rileva, misurando la vera efficacia della suite.

## N

**[NDCG (Normalised Discounted Cumulative Gain)](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)**: Una metrica di qualità del ranking che premia il collocare risultati molto rilevanti in cima a un elenco di risultati, normalizzata così che i punteggi siano confrontabili tra query. È un pilastro della valutazione della rilevanza della ricerca.

**[NIST (National Institute of Standards and Technology)](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)**: Un'agenzia federale statunitense le cui Special Publication e i cui quadri sono standard molto citati per cybersicurezza, privacy e IA.

**NIST AI RMF (AI Risk Management Framework)**: Un quadro volontario del NIST per individuare, valutare e gestire i rischi associati ai sistemi di IA lungo il loro ciclo di vita, organizzato attorno alle funzioni Govern, Map, Measure e Manage.

**[NIST SP 800-53](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53)**: Un catalogo del NIST di controlli di sicurezza e privacy per i sistemi informativi federali, molto usato come base ben oltre il governo.

**NIST SP 800-171**: Una pubblicazione del NIST che specifica i requisiti per proteggere le informazioni non classificate controllate (CUI) nei sistemi non federali, centrale per la conformità degli appaltatori della difesa.

**[NFR (Non-Functional Requirement)](https://en.wikipedia.org/wiki/Non-functional_requirement)**: Un requisito che descrive come un sistema dovrebbe comportarsi (le sue qualità come prestazioni, sicurezza, affidabilità o usabilità) anziché quali funzioni svolge.

**North-south traffic**: Traffico di rete tra un sistema e i suoi client esterni (in entrata e in uscita dal data center o dal cluster), in contrapposizione al traffico east-west tra servizi interni. Un gateway API governa tipicamente il traffico north-south.

## O

**Observability**: Il grado in cui lo stato interno di un sistema può essere dedotto dai suoi output esterni, tipicamente ottenuto tramite telemetria: metriche, log e tracce.

**[OKR (Objectives and Key Results)](https://en.wikipedia.org/wiki/OKR)**: Un quadro di definizione degli obiettivi che abbina un obiettivo qualitativo a pochi risultati chiave misurabili per allineare e focalizzare un'organizzazione.

**OpenTelemetry (OTel)**: Uno standard aperto e neutrale rispetto ai fornitori, con relativi strumenti, per generare, raccogliere ed esportare dati di telemetria (tracce, metriche e log) dal software.

**OPA (Open Policy Agent)**: Un motore di politiche open source e di uso generale che valuta politiche (scritte nel linguaggio Rego) per far rispettare regole di autorizzazione e configurazione lungo tutto lo stack, abilitando la politica come codice.

**OSPO (Open Source Program Office)**: Una funzione organizzativa che coordina strategia open source, governance, conformità e coinvolgimento della comunità, gestendo sia il consumo sia il contributo.

**[OWASP (Open Worldwide Application Security Project)](https://en.wikipedia.org/wiki/OWASP)**: Una comunità non profit che produce risorse di sicurezza applicativa molto usate e liberamente disponibili, tra cui la OWASP Top Ten e l'ASVS.

## P

**[PACELC](https://en.wikipedia.org/wiki/PACELC_theorem)**: Un'estensione del teorema CAP secondo cui, se c'è una Partizione, un sistema scambia Availability contro Consistency, Else (in funzionamento normale) scambia Latency contro Consistency.

**[PCI DSS (Payment Card Industry Data Security Standard)](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)**: Uno standard di sicurezza mantenuto dal settore delle carte di pagamento che specifica requisiti per le organizzazioni che archiviano, elaborano o trasmettono dati dei titolari di carta.

**[Penetration testing](https://en.wikipedia.org/wiki/Penetration_test)**: Un attacco simulato e autorizzato a un sistema da parte di tester esperti per trovare e dimostrare vulnerabilità sfruttabili prima dei veri attaccanti, consegnato come riscontri ordinati per priorità e azionabili.

**[PII (Personally Identifiable Information)](https://en.wikipedia.org/wiki/Personal_data)**: Informazioni che possono identificare un individuo specifico, da sole o combinate con altri dati; il loro trattamento è governato da leggi sulla privacy e da politiche interne.

**Platform engineering**: La disciplina di costruire e gestire piattaforme interne self-service e golden path che riducono il carico cognitivo e accelerano i team di prodotto.

**POUR**: I quattro principi guida delle Web Content Accessibility Guidelines: il contenuto deve essere Perceivable (percepibile), Operable (utilizzabile), Understandable (comprensibile) e Robust (robusto).

**Production readiness review**: Un controllo strutturato, eseguito prima che un servizio vada in produzione o assuma la reperibilità, che conferma che rispetta gli standard di osservabilità, affidabilità, sicurezza, runbook e supporto operativo.

**[Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering)**: La pratica di progettare e affinare le istruzioni, il contesto e gli esempi dati a un modello linguistico per ottenere un output affidabile e di alta qualità, trattata come una disciplina ingegneristica versionata e testata anziché per tentativi.

**[Prompt injection](https://en.wikipedia.org/wiki/Prompt_injection)**: Un attacco in cui un input costruito ad arte induce un modello linguistico a ignorare le istruzioni previste e a seguire quelle dell'attaccante, l'analogo nell'era dell'IA dei difetti di iniezione. È un rischio di sicurezza centrale delle applicazioni LLM.

**Property-based testing**: Una tecnica di test che verifica che proprietà dichiarate valgano su molti input generati automaticamente, anziché affidarsi solo a esempi scelti a mano.

**Pull request (PR) / merge request (MR)**: Un insieme proposto di modifiche sottoposto a revisione e discussione prima di essere unito in un ramo condiviso, l'unità primaria di revisione del codice nella maggior parte dei flussi di lavoro.

**Purple team**: Un esercizio collaborativo in cui i team di sicurezza offensivi (red) e difensivi (blue) lavorano insieme in tempo reale, così che gli attacchi e i rilevamenti pensati per coglierli siano messi a punto gli uni contro gli altri.

## Q

**Quality gate**: Un punto di controllo automatico in una pipeline che deve essere superato (per esempio rispettando soglie di copertura, sicurezza o prestazioni) prima che una modifica possa avanzare.

**[Quorum](https://en.wikipedia.org/wiki/Quorum_(distributed_computing))**: Nei sistemi distribuiti, il numero minimo di nodi che devono concordare perché un'operazione (come una lettura o una scrittura) sia considerata riuscita, usato per mantenere la consistenza nonostante i guasti.

## R

**[RACI](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)**: Un modello di assegnazione delle responsabilità che etichetta ogni partecipante a un compito o a una decisione come Responsible (esecutore), Accountable (responsabile), Consulted (consultato) o Informed (informato).

**[RAG (Retrieval-Augmented Generation)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)**: Una tecnica che ancora l'output di un modello linguistico recuperando prima documenti o dati rilevanti e fornendoli come contesto, migliorando l'accuratezza e riducendo le allucinazioni.

**[RBAC (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control)**: Un modello di autorizzazione che assegna permessi ai ruoli e ruoli agli utenti, semplificando l'amministrazione gestendo l'accesso a livello di ruolo.

**[Red team](https://en.wikipedia.org/wiki/Red_team)**: Un gruppo che emula un avversario realistico, spesso contro un'intera organizzazione e senza avvisare i difensori, per mettere alla prova rilevamento e risposta anziché limitarsi a elencare le vulnerabilità. In contrapposizione a un blue team (difensivo).

**[Reference data](https://en.wikipedia.org/wiki/Reference_data)**: Elenchi di codici e classificazioni controllati e a lenta variazione usati per categorizzare altri dati, come codici paese, valute e valori di stato. Governarli come vocabolario condiviso e versionato mantiene i sistemi coerenti.

**Rego**: Il linguaggio di politiche dichiarativo usato da Open Policy Agent per esprimere regole per decisioni di autorizzazione e configurazione.

**[REST (Representational State Transfer)](https://en.wikipedia.org/wiki/REST)**: Uno stile architetturale per applicazioni in rete che usa operazioni senza stato su HTTP su risorse indirizzabili, apprezzato per semplicità e ampia disponibilità di strumenti.

**[Reverse proxy](https://en.wikipedia.org/wiki/Reverse_proxy)**: Un server che sta davanti a uno o più servizi backend e inoltra loro le richieste dei client, offrendo comunemente terminazione TLS, bilanciamento del carico, cache e un unico punto di ingresso.

**[RFC (Request for Comments)](https://en.wikipedia.org/wiki/Request_for_Comments)**: Una proposta scritta fatta circolare per ricevere riscontro prima di una decisione o modifica tecnica significativa, che favorisce trasparenza e titolarità condivisa. (Il termine indica anche la serie di documenti degli standard di Internet.)

**[ROI (Return on Investment)](https://en.wikipedia.org/wiki/Return_on_investment)**: Una misura del valore ottenuto da un investimento rispetto al suo costo, usata per giustificare e dare priorità alle decisioni di ingegneria e tecnologia.

**[RPA (Robotic Process Automation)](https://en.wikipedia.org/wiki/Robotic_process_automation)**: "Robot" software che automatizzano compiti ripetitivi e basati su regole interagendo con interfacce utente e sistemi esistenti come farebbe una persona.

**RPO (Recovery Point Objective)**: La massima perdita di dati accettabile misurata nel tempo (per esempio "fino a cinque minuti"), che definisce quanto frequentemente i dati devono essere protetti.

**RTO (Recovery Time Objective)**: La durata massima accettabile per ripristinare un servizio dopo un'interruzione, che guida la progettazione e l'investimento nel disaster recovery.

## S

**Saga**: Un pattern per gestire la consistenza dei dati tra servizi in una transazione distribuita ordinando transazioni locali ed emettendo azioni compensative quando un passo fallisce.

**[SAFe (Scaled Agile Framework)](https://en.wikipedia.org/wiki/Scaled_agile_framework)**: Un quadro per applicare pratiche agile e lean in grandi imprese, coordinando molti team; apprezzato per la struttura e criticato per la possibile pesantezza.

**[SAST (Static Application Security Testing)](https://en.wikipedia.org/wiki/Static_application_security_testing)**: Test di sicurezza che analizzano codice sorgente, bytecode o binari senza eseguirli per trovare vulnerabilità presto nello sviluppo.

**SBOM (Software Bill of Materials)**: Un inventario formale e leggibile da macchina dei componenti e delle dipendenze di un software, usato per gestire il rischio di supply chain e di vulnerabilità.

**SCA (Software Composition Analysis)**: Strumenti che individuano componenti open source e di terze parti in una base di codice e segnalano vulnerabilità note e rischi di licenza.

**[Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development))**: Un quadro agile che organizza il lavoro in iterazioni di durata fissa (sprint) con ruoli, eventi e artefatti definiti per consegnare incrementi di valore.

**[Section 508](https://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)**: Una legge statunitense che richiede alle agenzie federali di rendere accessibili alle persone con disabilità la loro tecnologia elettronica e dell'informazione, in pratica allineata a WCAG.

**Semantic search**: Ricerca che corrisponde sul significato anziché su parole chiave esatte, tipicamente confrontando gli embedding della query e dei documenti. È spesso combinata con la ricerca lessicale in un approccio ibrido.

**[Service mesh](https://en.wikipedia.org/wiki/Service_mesh)**: Uno strato infrastrutturale dedicato, di solito implementato con proxy sidecar, che gestisce le questioni di comunicazione tra servizi come TLS reciproco, ritentativi, timeout, spostamento del traffico e osservabilità, tenendole fuori dal codice applicativo.

**Sidecar**: Un processo o container ausiliario distribuito accanto a un'istanza applicativa principale per fornire capacità di supporto (come un proxy di service mesh) senza cambiare l'applicazione stessa.

**[SIEM (Security Information and Event Management)](https://en.wikipedia.org/wiki/Security_information_and_event_management)**: Un sistema che aggrega e correla log ed eventi di sicurezza in un ambiente per abilitare rilevamento, allerta e indagine.

**[SLA (Service Level Agreement)](https://en.wikipedia.org/wiki/Service-level_agreement)**: Un impegno formale tra un fornitore di servizi e i suoi clienti che specifica i livelli di servizio attesi e le conseguenze del mancarli.

**SLI (Service Level Indicator)**: Una misura quantitativa di qualche aspetto della qualità del servizio, come la latenza delle richieste o il tasso di errore, che alimenta gli SLO.

**SLO (Service Level Objective)**: Un valore o intervallo obiettivo per un SLI che definisce il livello di affidabilità desiderato, base dei budget di errore.

**SLSA (Supply-chain Levels for Software Artifacts)**: Un quadro di requisiti di sicurezza graduati per migliorare l'integrità e la provenienza degli artefatti software lungo il processo di build e di rilascio.

**SOAR (Security Orchestration, Automation, and Response)**: Strumenti e pratiche che automatizzano e coordinano le operazioni di sicurezza, come triage e playbook di risposta, per migliorare velocità e coerenza.

**SOC 2 (System and Organisation Controls 2)**: Un quadro di audit e un rapporto, basati sui Trust Services Criteria dell'AICPA, che valuta i controlli di un'organizzazione di servizi per sicurezza, disponibilità, integrità del trattamento, riservatezza e privacy.

**[SOLID](https://en.wikipedia.org/wiki/SOLID)**: Cinque principi di progettazione orientata agli oggetti (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation e Dependency Inversion) che promuovono codice manutenibile e flessibile.

**[SOX (Sarbanes-Oxley Act)](https://en.wikipedia.org/wiki/Sarbanes-Oxley_Act)**: Legge statunitense che stabilisce requisiti per la rendicontazione finanziaria e i controlli interni nelle società quotate, con implicazioni per i sistemi IT che sostengono i dati finanziari.

**SPACE**: Un quadro per misurare la produttività degli sviluppatori su cinque dimensioni: Satisfaction and well-being (soddisfazione e benessere), Performance, Activity, Communication and collaboration e Efficiency and flow, mettendo in guardia dalle misure a metrica singola.

**[SRE (Site Reliability Engineering)](https://en.wikipedia.org/wiki/Site_reliability_engineering)**: Una disciplina che applica approcci di ingegneria del software alle operazioni, usando SLO, budget di errore e automazione per gestire sistemi affidabili su larga scala.

**SSDF (Secure Software Development Framework)**: Il quadro del NIST (SP 800-218) di pratiche di sviluppo sicuro di alto livello, che spazia da preparare l'organizzazione, proteggere il software, produrre software ben protetto e rispondere alle vulnerabilità.

**[Static analysis](https://en.wikipedia.org/wiki/Static_program_analysis)**: Esaminare codice sorgente, bytecode o binari senza eseguirli per trovare difetti, violazioni di stile e falle di sicurezza, tipicamente tramite linter, controllori di tipi e analizzatori dedicati collegati all'editor e alla pipeline.

**[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)**: Una tassonomia di modellazione delle minacce che categorizza le minacce come Spoofing, Tampering, Repudiation, Information disclosure, Denial of service ed Elevation of privilege.

## T

**[TCO (Total Cost of Ownership)](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**: Il costo completo sulla vita di un sistema o di una decisione, comprendente acquisizione, operazione, manutenzione e dismissione finale, non solo il prezzo iniziale.

**[TDD (Test-Driven Development)](https://en.wikipedia.org/wiki/Test-driven_development)**: Una pratica di scrivere un test automatico che fallisce prima del codice che lo fa passare, poi rifattorizzare, in brevi cicli ripetuti per guidare il progetto e assicurare la copertura.

**[Technical debt](https://en.wikipedia.org/wiki/Technical_debt)**: Il costo futuro implicito di scegliere ora una soluzione di comodo anziché una migliore che richiederebbe più tempo, che va gestito deliberatamente anziché accumulato inconsapevolmente.

**TF-IDF (Term Frequency-Inverse Document Frequency)**: Uno schema di ponderazione classico che valuta l'importanza di un termine per un documento in base a quanto spesso vi compare, compensata da quanto è comune nell'intero corpus. Sta alla base di gran parte del ranking della ricerca lessicale.

**[Theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints)**: Un approccio gestionale secondo cui la produttività di un sistema è limitata in ogni momento da un singolo collo di bottiglia, quindi gli sforzi di miglioramento dovrebbero concentrarsi su quel vincolo finché non si sposta altrove.

**[Threat modelling](https://en.wikipedia.org/wiki/Threat_model)**: Una pratica strutturata di individuare, elencare e dare priorità alle potenziali minacce a un sistema così che le difese possano essere progettate presto.

**Toil**: Nell'SRE, lavoro operativo manuale, ripetitivo e automatizzabile che scala linearmente con un servizio e non dà valore duraturo; ridurlo libera capacità per l'ingegneria.

**Trunk-based development**: Una pratica di controllo dei sorgenti in cui gli sviluppatori integrano frequentemente piccole modifiche in un unico ramo condiviso, riducendo al minimo i rami di lunga durata e il dolore delle unioni.

**[Type inference](https://en.wikipedia.org/wiki/Type_inference)**: Una caratteristica del linguaggio che deduce automaticamente i tipi delle espressioni, dando gran parte della sicurezza della tipizzazione statica senza richiedere che ogni tipo sia scritto a mano.

**[Type system](https://en.wikipedia.org/wiki/Type_system)**: L'insieme di regole che un linguaggio usa per assegnare e controllare i tipi, cogliendo intere classi di errori prima che il programma giri e documentando l'intento. I sistemi di tipi vanno da dinamici a statici e da deboli a forti.

## U

**Ubiquitous language**: Nel Domain-Driven Design, un vocabolario condiviso e preciso usato in modo coerente da sviluppatori ed esperti di dominio e riflesso direttamente nel codice e nei modelli.

**[UAT (User Acceptance Testing)](https://en.wikipedia.org/wiki/Acceptance_testing)**: Test eseguiti dagli utenti finali o dai loro rappresentanti per confermare che un sistema soddisfa le esigenze di business prima di essere accettato per il rilascio.

**[UX / UI (User Experience / User Interface)](https://en.wikipedia.org/wiki/User_experience)**: La User Experience è la qualità complessiva dell'interazione di una persona con un prodotto; la User Interface è la specifica superficie visiva e interattiva attraverso cui avviene quell'interazione.

## V

**[Value object](https://en.wikipedia.org/wiki/Value_object)**: Nel Domain-Driven Design, un oggetto immutabile definito interamente dai suoi attributi anziché da un'identità distinta, come un importo di denaro o un intervallo di date.

**[Value stream mapping](https://en.wikipedia.org/wiki/Value-stream_mapping)**: Una tecnica per disegnare ogni passo dall'idea al valore consegnato, distinguendo il tempo a valore aggiunto dal tempo di attesa, così che colli di bottiglia, passaggi di consegna e cicli di rilavorazione diventino visibili e migliorabili.

**[Vector database](https://en.wikipedia.org/wiki/Vector_database)**: Un archivio di dati ottimizzato per indicizzare e cercare per similarità vettori di embedding ad alta dimensione, spina dorsale comune della ricerca semantica e della generazione aumentata dal recupero.

**Vertical scaling**: Aumentare la capacità rendendo più potente un singolo nodo ("scaling up"), il che è semplice ma alla fine limitato dalla macchina più grande disponibile.

**[VCS (Version Control System)](https://en.wikipedia.org/wiki/Version_control)**: Uno strumento, come Git, che registra le modifiche ai file nel tempo così che la storia possa essere rivista, i rami possano essere mantenuti e il lavoro possa essere coordinato.

**[Vulnerability scanning](https://en.wikipedia.org/wiki/Vulnerability_scanner)**: Ispezione automatica di sistemi, container o codice rispetto a database di debolezze e configurazioni errate note. È ampia ed economica e integra la profondità dei test di penetrazione manuali.

## W

**[WCAG (Web Content Accessibility Guidelines)](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines)**: Un insieme di linee guida W3C riconosciute a livello internazionale, organizzate attorno ai principi POUR e ai livelli di conformità A, AA e AAA, per rendere accessibile il contenuto web.

**Wardley map**: Una tecnica visiva di strategia che colloca le capacità in base al loro valore per gli utenti e alla loro maturità evolutiva, per informare le decisioni di costruire o comprare e di investimento.

**Work in progress (WIP) limit**: Un tetto al numero di elementi che possono trovarsi contemporaneamente in un dato stadio di un flusso di lavoro, una pratica Kanban centrale che migliora il flusso esponendo i colli di bottiglia e frenando l'onere del troppo lavoro parallelo.

**WSJF (Weighted Shortest Job First)**: Un metodo di prioritizzazione che ordina il lavoro dividendo il suo costo del ritardo per la sua durata stimata, così che gli elementi più brevi, più sensibili al tempo e di maggior valore siano fatti per primi.

## X

**[XSS (Cross-Site Scripting)](https://en.wikipedia.org/wiki/Cross-site_scripting)**: Una vulnerabilità web in cui un attaccante inietta script malevoli che vengono eseguiti nei browser di altri utenti, potenzialmente rubando dati o dirottando sessioni.

## Y

**[YAGNI (You Aren't Gonna Need It)](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it)**: Un principio che sconsiglia di costruire funzionalità per speculazione, sulla base del fatto che i bisogni previsti spesso non si materializzano e aggiungono costo e complessità.

## Z

**[Zero trust](https://en.wikipedia.org/wiki/Zero_trust_security_model)**: Un modello di sicurezza che non presume alcuna fiducia implicita basata sulla posizione di rete e verifica di continuo ogni richiesta di accesso rispetto a identità, dispositivo e contesto, seguendo la massima "non fidarti mai, verifica sempre".
