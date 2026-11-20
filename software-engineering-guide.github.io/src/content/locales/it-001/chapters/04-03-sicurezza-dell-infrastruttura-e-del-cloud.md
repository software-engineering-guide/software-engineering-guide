# 4.3 Sicurezza dell'infrastruttura e del cloud

## Panoramica e motivazioni

Le applicazioni girano su infrastruttura e oggi quell'infrastruttura è in gran parte basata sul cloud, definita dal software e in continuo cambiamento. Un singolo ingegnere può ormai predisporre un database, aprire un percorso di rete o concedere un permesso con un solo comando, a una scala e a una velocità che il controllo delle modifiche tradizionale non aveva previsto. Quel potere è esattamente il motivo per cui la configurazione errata, non gli exploit esotici, è la principale causa delle violazioni del cloud. Un bucket di archiviazione reso pubblico per sbaglio o un ruolo di accesso troppo ampio possono esporre in pochi secondi i dati di un'intera organizzazione.

Per le grandi imprese, l'infrastruttura cloud copre più fornitori, migliaia di account e un mix di servizi gestiti, container e funzioni serverless. La superficie d'attacco non è un perimetro statico. È una raccolta viva e sterminata di risorse e identità. Per gli enti pubblici, la stessa complessità incontra rigidi regimi di autorizzazione, mandati di residenza dei dati e confini di classificazione che plasmano ogni scelta architetturale. In entrambi, lo strato dell'identità è diventato il nuovo perimetro: chi può fare che cosa, su quale risorsa, a quali condizioni.

Questo capitolo tratta come proteggere quella base: la [gestione delle identità e degli accessi](https://en.wikipedia.org/wiki/Identity_management) (IAM), la [segmentazione della rete](https://en.wikipedia.org/wiki/Network_segmentation), la [cifratura](https://en.wikipedia.org/wiki/Encryption) e la [gestione delle chiavi](https://en.wikipedia.org/wiki/Key_management), la sicurezza di container e carichi [serverless](https://en.wikipedia.org/wiki/Serverless_computing) e la gestione continua della postura che impedisce a un patrimonio cloud in rapido movimento di scivolare nel pericolo.

## Principi chiave

- **L'identità è il perimetro.** Le decisioni di accesso poggiano su un'identità forte e un'autorizzazione a grana fine, non sulla posizione di rete.
- **Minimo privilegio, sempre.** Ogni identità, umana o macchina, ottiene i permessi minimi necessari e non di più.
- **Segmenta per contenere.** Dividi reti e carichi così che una compromissione in un'area non possa diffondersi liberamente.
- **Cifra ovunque.** Proteggi i dati in transito e a riposo per impostazione predefinita, con chiavi ben gestite.
- **Immutabile e dichiarativo.** Definisci l'infrastruttura come codice (IaC), rilascia in modo immutabile e tratta la deriva come un difetto.
- **Verifica continua.** La postura non è un audit una tantum; scansiona e fai rispettare di continuo.
- **Configurazione sicura per impostazione predefinita.** Lo stato predefinito di qualsiasi risorsa dovrebbe essere bloccato, non aperto.

## Raccomandazioni

### Progetta con deliberazione la gestione delle identità e degli accessi

L'IAM è la parte più importante della sicurezza del cloud, e la più spesso gestita male.

- Usa il **[controllo degli accessi basato sui ruoli](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC)** per concedere permessi per funzione lavorativa e il **[controllo degli accessi basato sugli attributi](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC)** dove servono decisioni più fini e consapevoli del contesto (basate su etichette, ambiente, classificazione dei dati o orario).
- Elimina le credenziali statiche di lunga durata a favore di token di breve durata emessi automaticamente e della federazione di identità del carico di lavoro.
- Imponi la [MFA](https://en.wikipedia.org/wiki/Multi-factor_authentication) (autenticazione a più fattori) per ogni accesso umano e richiedi un'autenticazione forte per le azioni privilegiate.
- Applica il minimo privilegio con rigore: parti da zero e aggiungi permessi deliberatamente. Rivedi e pota regolarmente i permessi inutilizzati; l'accesso tende ad accumularsi.
- Separa i compiti così che nessuna singola identità possa sia fare sia approvare modifiche sensibili.
- Usa account o progetti dedicati per creare confini rigidi tra ambienti (produzione, staging, sviluppo) e tra unità di business.

### Segmenta le reti e micro-segmenta i carichi

Le reti piatte lasciano gli attaccanti liberi di muoversi lateralmente una volta dentro. Dividi e contieni.

- Segmenta a livello di rete in livelli e zone, consentendo solo il traffico di cui ciascun livello ha legittimamente bisogno.
- Applica la **micro-segmentazione** così che i singoli carichi comunichino solo con i pari specifici che richiedono, fatta rispettare da una politica consapevole dell'identità anziché da ampie regole di sottorete.
- Nega per impostazione predefinita il traffico est-ovest; richiedi regole di consenso esplicite.
- Metti gli archivi di dati sensibili in sottoreti private senza esposizione diretta a internet, raggiunti solo attraverso percorsi controllati.
- Usa la connettività privata verso i servizi gestiti anziché instradare su internet pubblico dove possibile.

### Cifra i dati e gestisci le chiavi correttamente

La cifratura è forte solo quanto la gestione delle chiavi che c'è dietro.

- Cifra **in transito** con [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Transport Layer Security) aggiornato ovunque, compreso il traffico interno tra servizi.
- Cifra **a riposo** per impostazione predefinita tutto l'archiviazione, i database e i backup.
- Gestisci le chiavi con un **Key Management Service (KMS)** e usa un **[modulo di sicurezza hardware](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM)** per le chiavi della massima garanzia e per i requisiti normativi.
- Ruota le chiavi con una pianificazione e supporta la rotazione rapida in caso di sospetta compromissione.
- Controlla e verifica chi può usare e gestire le chiavi separatamente da chi può accedere ai dati, così che la custodia delle chiavi faccia rispettare la separazione dei compiti.
- Considera le chiavi gestite dal cliente dove la normativa o la fiducia contrattuale richiedono che sia l'organizzazione a detenere le chiavi anziché il fornitore.

### Proteggi container, Kubernetes e serverless

Ogni modello di calcolo porta i propri rischi.

- **Container:** costruisci da immagini di base minime e fidate; scansiona le immagini alla ricerca di vulnerabilità prima del rilascio; esegui come non-root; rendi i filesystem di sola lettura dove possibile; e non incorporare mai segreti nelle immagini.
- **[Kubernetes](https://en.wikipedia.org/wiki/Kubernetes):** attiva l'RBAC e delimita strettamente gli account di servizio; applica network policy per la micro-segmentazione; usa admission controller e motori di policy per far rispettare gli standard; limita i container privilegiati; isola i carichi sensibili; e tieni aggiornati piano di controllo e nodi.
- **Serverless:** applica il minimo privilegio al ruolo di esecuzione di ogni funzione (una fonte comune di sovra-permessi); convalida tutti gli input degli eventi; gestisci i segreti attraverso l'archivio di segreti della piattaforma; e monitora gli schemi di invocazione anomali.

Qualunque sia il modello, tieni aggiornato il runtime e fresche le immagini. Un container è sicuro quanto il software al suo interno.

### Gestisci di continuo la postura di sicurezza del cloud

Il cloud cambia troppo in fretta perché audit manuali periodici tengano il passo.

- Adotta strumenti di **Cloud Security Posture Management (CSPM)** per rilevare di continuo configurazioni errate, esposizione pubblica e violazioni delle politiche in tutti gli account.
- Definisci la politica di sicurezza come codice e falla rispettare al momento del rilascio così che le cattive configurazioni siano bloccate prima di arrivare.
- Preferisci la prevenzione (protezioni che fermano la configurazione errata) al rilevamento (allarmi a cose fatte) e combina entrambi.
- Mantieni un inventario accurato di risorse e identità; non puoi proteggere ciò che non vedi.
- Segui e rimedia alla deriva tra l'infrastruttura come codice dichiarata e lo stato effettivo in esecuzione.

## Compromessi: vantaggi e svantaggi

| Decisione | Vantaggi | Svantaggi |
|---|---|---|
| RBAC | Semplice, comprensibile, facile da verificare | Grossolano, esplosione di ruoli su larga scala |
| ABAC | A grana fine, consapevole del contesto, scala con le etichette | Complesso da progettare e da ragionare |
| Chiavi gestite dal fornitore (KMS) | Facile, integrato, basso onere operativo | Il fornitore detiene la custodia; meno controllo |
| Chiavi gestite dal cliente/HSM | Pieno controllo, soddisfa mandati rigorosi | Onere operativo, rischio di perdere le chiavi |
| Protezioni preventive | Fermano la configurazione errata prima che accada | Possono bloccare lavoro legittimo, richiedono regolazione |
| Solo CSPM investigativo | Flessibile, non bloccante | Il danno può avvenire prima del rilevamento |
| Micro-segmentazione | Forte contenimento del movimento laterale | Complessità operativa, proliferazione delle politiche |

Il compromesso dominante è controllo contro onere operativo. Controlli più stretti (chiavi gestite dal cliente, micro-segmentazione rigorosa, ABAC) riducono il rischio, ma richiedono competenze e manutenzione che i piccoli team faticano a sostenere. Il livello giusto dipende da quanto sono sensibili i dati e quali normative si applicano. Un approccio pragmatico stratifica forti valori predefiniti sicuri per tutti, poi riserva rigore extra ai sistemi a più alto rischio e privilegia protezioni automatiche che fanno della scelta sicura il valore predefinito anziché una disciplina manuale.

## Domande da discutere con il tuo team

1. **Dove traccerete confini rigidi di account o progetto, e che cosa appartiene a ciascuno?** Account e progetti dedicati creano il contenimento più forte che il cloud offre, così che una compromissione in sviluppo non possa raggiungere la produzione e un'unità di business non possa toccare i dati di un'altra. Decidi il tuo schema di confini prima che il patrimonio cresca a migliaia di account, perché adattare l'isolamento a una struttura piatta è lento e rischioso. Per il lavoro aziendale e governativo, questi confini corrispondono anche in modo pulito a separazione degli ambienti, classificazione dei dati e limiti del raggio d'impatto che gli auditor si aspettano di vedere. Porta un diagramma attuale di quali carichi condividono oggi un account e segna dove un singolo ruolo troppo ampio abbraccia produzione e non produzione. Se i dati sensibili stanno nello stesso account dei carichi sperimentali, quello è il confine da correggere per primo.

2. **Qual è il vostro standard su chi può gestire le chiavi rispetto a chi può accedere ai dati cifrati?** La cifratura è forte solo quanto la gestione delle chiavi e separare la custodia delle chiavi dall'accesso ai dati trasforma il tuo KMS in un punto di applicazione della separazione dei compiti. Decidi chi può creare, ruotare e usare le chiavi e assicurati che quell'insieme non si sovrapponga alle persone che possono leggere i dati che quelle chiavi proteggono. Per i sistemi regolamentati e governativi, questo spesso guida la scelta tra chiavi gestite dal fornitore e chiavi gestite dal cliente o HSM, che portano più controllo e più rischio operativo di perdere le chiavi. Porta le tue attuali politiche delle chiavi e controlla se una singola identità può sia gestire una chiave sia leggere i dati dietro di essa, perché è un divario silenzioso comune. Se custodia e accesso non sono divisi, la cifratura a riposo ti protegge meno di quanto suggerisca il cruscotto.

3. **Come renderete inevitabili i valori predefiniti sicuri nella vostra landing zone anziché semplicemente raccomandati?** La configurazione errata, non gli exploit esotici, è la principale causa delle violazioni del cloud e la soluzione sono protezioni preventive che bloccano un database pubblico o un bucket non cifrato prima che arrivi, non allarmi a cose fatte. Decidi quali politiche farete rispettare al momento del rilascio (nessuna archiviazione pubblica, cifratura attiva per impostazione predefinita, etichette obbligatorie) e quali solo rileverete e segnalerete. Per un grande team, codificarle in landing zone e modelli di infrastruttura come codice significa che ogni nuovo account eredita la protezione senza sforzo per team, trasformando la sicurezza da tassa ricorrente in un investimento una tantum. Porta i rilievi di configurazione errata dell'ultimo mese e chiediti quali una protezione preventiva avrebbe fermato del tutto. Se la tua gestione della postura è solo investigativa, il danno può avvenire prima che qualcuno veda l'allarme, quindi sposta i controlli a più alto impatto sulla prevenzione.

4. **Come eliminate le credenziali statiche di lunga durata senza rompere l'automazione che in silenzio dipende da esse?** Le chiavi di accesso incorporate che non scadono mai sono tra le cause più comuni di violazioni del cloud, perché una singola chiave trapelata in uno script, un log o un repository consegna a un attaccante un accesso durevole. La spinta contraria è operativa: i lavori CI legacy, i compiti cron e le integrazioni di terze parti spesso presumono che esista una chiave statica e passarli a token di breve durata o alla federazione di identità del carico di lavoro richiede tempo di ingegneria che nessuno ha pianificato. Per un grande team, un percorso di migrazione condiviso (emettere token automaticamente, fissare uno standard di scadenza e dare allarme su ogni nuova chiave di lunga durata) impedisce a ogni gruppo di inventare la propria risposta più debole. Porta un inventario di ogni credenziale statica in uso, la sua età, il suo raggio d'impatto e se il sistema che alimenta può accettare oggi l'identità federata. Nei contesti aziendali e governativi, lega la scadenza ai cicli di audit e di autorizzazione, perché una credenziale che sopravvive alla persona che l'ha creata è esattamente il rilievo che blocca un'autorizzazione continua.

5. **Quando una risorsa è configurata male o una chiave è compromessa, quanto in fretta potete rilevare, contenere e rimediare, e l'avete misurato?** Un bucket pubblico o un ruolo troppo ampio è pericoloso solo quanto la finestra in cui resta aperto, quindi il tempo medio di rilevamento e di rimedio è il numero che limita davvero la tua esposizione. La tensione è tra protezioni preventive che fermano l'errore al momento del rilascio e una gestione investigativa della postura che coglie ciò che sfugge e ti servono cifre oneste per entrambe anziché la rassicurante ipotesi che le protezioni coprano tutto. Porta i rilievi di configurazione errata e deriva dell'ultimo trimestre con marche temporali, il tempo mediano dall'introduzione al rimedio e il registro delle prove per una rotazione da compromissione di chiave. Per i patrimoni aziendali e governativi che si estendono su migliaia di account, concorda chi possiede il rimedio per un rilievo che nessun team possiede in modo ovvio, perché un allarme senza un responsabile è un allarme che invecchia in incidente.

6. **Come manterrete coerente la postura di sicurezza attraverso più cloud, account e team senza rallentare tutti a passo d'uomo?** I patrimoni multi-cloud e multi-account si frammentano in fretta: ogni fornitore ha il proprio modello IAM, i propri valori predefiniti e i propri strumenti di postura, quindi una politica fatta rispettare in un posto cade in silenzio in un altro. Il compromesso è tra un controllo centrale che garantisce coerenza e un'autonomia locale che lascia ai team muoversi in fretta e spingersi troppo da una parte o dall'altra o strozza la consegna o lascia derivare gli standard. Porta la tua attuale mappa di copertura: quali account ereditano le protezioni della landing zone, quali non sono gestiti e dove lo stesso controllo è espresso in tre modi diversi tra i fornitori. Per un'organizzazione grande o pubblica, aggiungi l'angolo dell'audit, perché gli auditor si aspettano uno standard difendibile applicato ovunque e un controllo che esiste nel tuo cloud primario ma non nel secondario è un divario che un attaccante o un valutatore determinato troverà per primo.

## Lente settoriale

**Startup.** Vincono velocità e sopravvivenza, quindi appoggiati interamente ai valori predefiniti sicuri che arrivano gratis: cifratura a riposo attiva, archiviazione privata a meno che un umano la apra, MFA sull'account root e l'identità del carico di lavoro integrata del fornitore anziché chiavi di accesso incollate. Non montare una piattaforma CSPM né fare a mano una micro-segmentazione che non puoi mantenere; una singola protezione che blocca un database aperto a internet compra la maggior parte della protezione per un pomeriggio di lavoro. Tieni tutto in infrastruttura come codice fin dall'inizio così che il rafforzamento scali con te anziché diventare una riscrittura più avanti.

**Piccola impresa.** Senza un ingegnere di sicurezza dedicato e con un budget ridotto, preferisci servizi gestiti i cui valori predefiniti sono già rinforzati e la cui gestione delle chiavi è fatta per te, anziché costruire la tua disciplina KMS. Tratta la sicurezza del cloud come una questione di igiene della configurazione: sappi quali bucket e database esistono, tienili privati, richiedi la MFA e attiva i controlli di postura nativi del fornitore che non costano nulla di più. Quando compri strumenti, privilegia quelli che segnalano di serie esposizione pubblica e archiviazione non cifrata, perché quei due errori causano la maggior parte delle violazioni evitabili.

**Grande impresa.** Il vero problema è la coerenza tra migliaia di account e molti team, quindi il lavoro è lavoro di piattaforma: landing zone che predispongono ogni account già rinforzato, protezioni fatte rispettare come policy-as-code e CSPM che scansiona di continuo la deriva. Standardizza il modello IAM, le regole di custodia delle chiavi e la base di segmentazione così che i gruppi smettano di reinventare versioni più deboli e misura la postura nell'intero patrimonio anziché fidarti della parola di ciascun team. Metti a bilancio l'ingegneria continua per tenere aggiornate le politiche man mano che i fornitori aggiungono servizi e il patrimonio cresce.

**Ente pubblico.** Regole sugli appalti, mandati di residenza dei dati e regimi di autorizzazione plasmano ogni scelta, quindi i controlli di sicurezza fanno anche da evidenza di audit. Privilegia una gestione delle chiavi con convalida FIPS e custodia separata dall'accesso ai dati, regioni isolate che tengono i dati entro i confini nazionali e immagini di container firmate e scansionate con un rigoroso controllo di ammissione. Pubblica le salvaguardie che puoi, alimenta la gestione continua della postura direttamente nell'autorizzazione continua e richiedi ai fornitori di dichiarare i propri valori predefiniti di configurazione e di supportare i controlli di segmentazione e custodia delle chiavi che i tuoi confini di classificazione esigono.

## Esempi

**Startup.** Una piccola startup gestisce tutto in un solo account cloud e non può dotare di personale un team di piattaforma, quindi si appoggia a valori predefiniti che arrivano sicuri: cifratura a riposo attiva per impostazione predefinita, bucket di archiviazione privati a meno che un umano li apra esplicitamente e MFA richiesta sull'account root. Anziché chiavi di accesso di lunga durata incollate nella CI, usa l'identità del carico di lavoro integrata del fornitore così che la pipeline ottenga automaticamente credenziali di breve durata. Una singola protezione gratuita che segnala qualsiasi database aperto a internet la salva dall'errore cloud più comune e più costoso, al costo di un pomeriggio per metterla in piedi.

**Grande impresa.** Un'azienda di media che gestisce migliaia di account su due fornitori cloud fa rispettare uno schema di landing zone: ogni account è predisposto da un modello con cifratura a riposo attiva per impostazione predefinita, nessun accesso pubblico all'archiviazione, etichette obbligatorie e una base di politiche di protezione. Il CSPM scansiona di continuo la deriva e la federazione di identità del carico di lavoro ha eliminato le chiavi di lunga durata per i sistemi CI. Quando uno sviluppatore tenta per sbaglio di aprire un database a internet, una politica preventiva blocca la modifica e apre automaticamente un ticket.

**Ente pubblico.** Un'agenzia affine alla difesa opera in una regione cloud isolata con la residenza dei dati fatta rispettare dalla politica così che nessun dato lasci i confini nazionali. Le chiavi più sensibili vivono in HSM con convalida FIPS (Federal Information Processing Standards), con la custodia delle chiavi separata dall'accesso ai dati per far rispettare la separazione dei compiti. I cluster Kubernetes usano rigorose network policy e controlli di ammissione; ogni immagine di container è scansionata e firmata prima di poter girare. La gestione continua della postura alimenta direttamente le evidenze di autorizzazione continua dell'agenzia.

## Business case: motivazioni, ROI e TCO

La sicurezza dell'infrastruttura cloud è dove un piccolo investimento sventa perdite catastrofiche da prima pagina. Il costo totale di proprietà comprende strumenti CSPM, servizi di gestione delle chiavi, il tempo di ingegneria per progettare IAM e segmentazione al minimo privilegio e lo sforzo continuo per tenere aggiornate le politiche. Questi costi sono reali ma modesti. Il costo di saltarli è una singola risorsa configurata male che espone un intero database di clienti, insieme alle sanzioni normative, ai costi di notifica e al danno duraturo al marchio che ne seguono. Le violazioni da configurazione errata del cloud sono tra gli incidenti più comuni e più evitabili del settore.

Automazione e riuso amplificano il ROI. Codifica i valori predefiniti sicuri in landing zone e modelli di infrastruttura come codice e ogni nuovo account e carico eredita la protezione senza sforzo per team, trasformando la sicurezza da tassa manuale ricorrente in un investimento di piattaforma una tantum. Per gli enti pubblici e le imprese regolamentate, una forte gestione della postura abbassa anche il costo di audit e autorizzazione continua producendo le evidenze automaticamente. Quando presenti il caso alla leadership, sottolinea che lo strato di identità e configurazione è ora il principale vettore di violazione, che la configurazione errata è prevenibile e che le protezioni tagliano sia il rischio sia l'attrito della revisione manuale.

## Antipattern e insidie

- **Permessi jolly.** Concedere un ampio accesso `*` "per far funzionare le cose" e non stringerlo mai.
- **Chiavi statiche di lunga durata.** Chiavi di accesso incorporate in script e CI che non scadono mai e prima o poi trapelano.
- **Reti piatte.** Nessuna segmentazione, così un host compromesso raggiunge tutto.
- **Pubblico per errore.** Archiviazione e database esposti a internet da impostazioni predefinite o trascurate.
- **Cifratura senza disciplina delle chiavi.** Attivare la cifratura ma lasciare l'accesso alle chiavi spalancato o non ruotarle mai.
- **Segreti incorporati nelle immagini.** Credenziali incorporate in immagini di container che si diffondono ovunque l'immagine giri.
- **Ruoli serverless con troppi permessi.** Funzioni a cui è concesso molto più del necessario perché la delimitazione è stata saltata.
- **Postura solo da audit.** Rilevare le configurazioni errate a cose fatte anziché prevenirle al momento del rilascio.
- **Ignorare la deriva.** Lasciare che l'ambiente in esecuzione diverga dall'infrastruttura come codice finché nessuno sa lo stato reale.

## Modello di maturità

**Livello 1: Avvio.** Predisposizione manuale guidata da chiunque abbia bisogno di una risorsa. Ampi permessi jolly e chiavi statiche di lunga durata. Reti piatte senza segmentazione. Cifratura applicata in modo incoerente, se non affatto. Nessuna gestione della postura; le configurazioni errate emergono solo dopo che un incidente impone la domanda.

**Livello 2: Sviluppo.** Compaiono alcuni ruoli IAM e la MFA e la cifratura a riposo è attivata per gli archivi principali, ma la pratica varia da team a team. Esistono livelli di rete di base senza negazione per impostazione predefinita. Le revisioni della configurazione avvengono periodicamente e a mano. L'infrastruttura è in parte definita come codice, quindi il rafforzamento dipende da quale gruppo ha predisposto l'account.

**Livello 3: Standardizzazione.** RBAC e ABAC al minimo privilegio con credenziali di breve durata sono documentati e fatti rispettare nell'organizzazione. La segmentazione usa la negazione per impostazione predefinita est-ovest. La cifratura in transito e a riposo è attiva per impostazione predefinita, con chiavi nel KMS con una pianificazione di rotazione e custodia separata dall'accesso ai dati. Il rafforzamento di container e Kubernetes è uno standard e il CSPM gira rispetto a politiche definite applicate in modo coerente a ogni account.

**Livello 4: Gestione.** La postura è misurata, non presunta. Segui metriche nominate rispetto a valori di riferimento e obiettivi: la quota di identità entro la propria base di minimo privilegio, tempo medio di rilevamento e rimedio di configurazioni errate e deriva, copertura di protezioni e CSPM nei vari account, conformità alla rotazione delle chiavi e il numero di credenziali di lunga durata sopravvissute. I rilievi sono sottoposti a triage per raggio d'impatto, il rimedio ha un responsabile e un obiettivo di livello di servizio e i dati di andamento su questi numeri guidano dove va il prossimo sforzo di rafforzamento.

**Livello 5: Orchestrazione.** I valori predefiniti sicuri sono incorporati in landing zone e infrastruttura come codice così che ogni risorsa nasca già rinforzata e i controlli si adattino al mutare del patrimonio e del quadro delle minacce. La micro-segmentazione usa una politica consapevole dell'identità; chiavi gestite dal cliente e HSM proteggono i sistemi a più alta garanzia con separazione della custodia. Le protezioni preventive bloccano la configurazione errata al momento del rilascio, la deriva è rilevata e rimediata automaticamente e le evidenze di postura alimentano automaticamente l'autorizzazione continua. La sicurezza è integrata con consegna e pianificazione del rischio e l'organizzazione ritira e ridefinisce di routine i controlli man mano che fornitori, servizi e normative cambiano.

## Spunti di discussione

1. Dove l'ABAC vale la sua complessità rispetto a restare con l'RBAC nel vostro ambiente?
2. Come eliminate le credenziali di lunga durata senza rompere l'automazione legacy?
3. Qual è la giusta divisione tra protezioni preventive e gestione investigativa della postura?
4. Quali sistemi giustificano chiavi gestite dal cliente o HSM dato il loro costo operativo?
5. Come evitate che i permessi al minimo privilegio si accumulino in silenzio tornando al sovra-privilegio?
6. Come dovrebbe la complessità multi-cloud cambiare il vostro approccio a postura e politica coerenti?

## Punti chiave

- L'identità è il nuovo perimetro; investi in un IAM al minimo privilegio con credenziali di breve durata.
- Segmenta le reti e micro-segmenta i carichi per contenere la compromissione.
- Cifra in transito e a riposo per impostazione predefinita e gestisci le chiavi con KMS/HSM e separazione della custodia.
- Rinforza container, Kubernetes e serverless; tieni aggiornati runtime e immagini.
- Preferisci protezioni preventive al rilevamento a cose fatte e gestisci la postura di continuo.
- Incorpora i valori predefiniti sicuri in landing zone e infrastruttura come codice così che la protezione scali automaticamente.
- La configurazione errata, non gli exploit esotici, è la principale causa delle violazioni del cloud ed è prevenibile.

## Riferimenti e letture di approfondimento

- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- Center for Internet Security, *CIS Benchmarks* (fornitori cloud, Kubernetes, Docker)
- Cloud Security Alliance, *Cloud Controls Matrix* e *Security Guidance for Cloud Computing*
- NIST, *SP 800-190: Application Container Security Guide*
- Liz Rice, *Container Security*
- Marco Lancini e altri, letteratura di ingegneria su *postura e rilevamento della sicurezza del cloud*
- Pilastri di sicurezza Well-Architected dei fornitori (come indicazioni architetturali neutrali rispetto al fornitore)
