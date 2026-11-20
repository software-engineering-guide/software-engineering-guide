# 4.8 Crittografia e gestione delle chiavi

## Panoramica e motivazioni

Quasi ogni sistema che costruisci dipende già dalla [crittografia](https://en.wikipedia.org/wiki/Cryptography), la pratica di proteggere le informazioni con tecniche matematiche così che solo le parti previste possano leggerle o fidarsi di esse. Il tuo traffico web viaggia su canali cifrati, le tue password sono sottoposte ad hash, i tuoi aggiornamenti software sono firmati e i dati dei tuoi clienti stanno cifrati su disco. La buona notizia per la maggior parte degli ingegneri è che non ti viene chiesto di inventare nulla di tutto questo. La parte difficile non è la matematica. È usare correttamente blocchi costruttivi collaudati e, soprattutto, gestire le chiavi da cui quei blocchi dipendono.

Questo capitolo è scritto per ingegneri che non sono crittografi, il che vale per quasi tutti noi. Ti serve abbastanza comprensione per fare scelte sensate, per sapere che cosa garantisce ciascuno strumento e per evitare gli errori che trasformano algoritmi forti in un falso conforto. Il capitolo 4.3 (sicurezza dell'infrastruttura e del cloud) cita di passaggio cifratura e gestione delle chiavi; qui andiamo più a fondo su che cosa cifrare, come e come gestire il ciclo di vita delle chiavi che lo rende reale.

Per le grandi imprese, la crittografia si dirama su migliaia di servizi, certificati e chiavi e un singolo certificato scaduto o una chiave persa può mettere fuori uso un sistema critico o far trapelare un archivio di dati. Per gli enti pubblici, la crittografia è spesso imposta, convalidata e verificata, con regole di classificazione dei dati che dettano esattamente quali chiavi proteggono quali segreti e chi può detenerle. In entrambi i contesti, il fallimento ricorrente è lo stesso: buoni algoritmi vanificati da una gestione sciatta delle chiavi.

## Principi chiave

- **Non scrivere la tua crittografia.** Usa librerie collaudate e largamente riviste e algoritmi standard. Gli schemi nuovi falliscono in modi che solo gli esperti colgono.
- **Gli algoritmi sono la parte facile; le chiavi sono la parte difficile.** Il ciclo di vita di una chiave è dove vive la maggior parte dei fallimenti reali.
- **Sappi che cosa garantisce ogni primitiva.** Riservatezza, integrità e autenticità sono proprietà diverse che richiedono strumenti diversi.
- **Cifra in transito e a riposo per impostazione predefinita.** Fai della protezione lo standard, non un'opzione.
- **Separa la custodia delle chiavi dall'accesso ai dati.** Chi gestisce una chiave non dovrebbe poter leggere automaticamente i dati che essa protegge.
- **Pianifica il cambiamento.** Gli algoritmi si indeboliscono, le chiavi trapelano e gli standard evolvono. Costruisci per la rotazione e la migrazione fin dal primo giorno.
- **Preferisci implementazioni convalidate dove conta.** Per il lavoro regolamentato e governativo, scegli moduli con una convalida riconosciuta.

## Raccomandazioni

### Non scrivere la tua crittografia

È la regola d'oro e vale la pena dirla per prima. Non progettare mai il tuo algoritmo di cifratura, non inventare mai il tuo protocollo, non implementare mai a mano una primitiva da un articolo. La crittografia funzionante sembra semplice e nasconde modalità di guasto sottili (canali laterali di temporizzazione, padding oracle, casualità debole) che sopravvivono solo ad anni di revisione esperta. Usa librerie consolidate come il modulo crittografico standard della tua piattaforma o una libreria ben considerata e usale al più alto livello di astrazione disponibile. Ricorri a modalità di cifratura autenticata e a interfacce "facili" che fanno della scelta sicura il valore predefinito, anziché assemblare tu pezzi di basso livello.

### Adegua la primitiva alla garanzia di cui hai bisogno

Strumenti diversi forniscono garanzie diverse e confonderli è un errore comune e pericoloso. Impara le tre famiglie principali.

- La crittografia a **[chiave simmetrica](https://en.wikipedia.org/wiki/Symmetric-key_algorithm)** usa un'unica chiave segreta condivisa sia per cifrare sia per decifrare. È veloce e protegge la **riservatezza**, ma entrambe le parti devono già condividere la chiave. AES è il cavallo di battaglia standard.
- La crittografia a **[chiave pubblica](https://en.wikipedia.org/wiki/Public-key_cryptography)** usa una coppia di chiavi matematicamente collegate: una chiave pubblica che chiunque può detenere e una chiave privata che tieni segreta. Risolve la distribuzione delle chiavi e abilita le **firme digitali**, che provano l'**autenticità** (chi l'ha inviato) e l'**integrità** (che non è stato alterato).
- Una **[funzione di hash crittografica](https://en.wikipedia.org/wiki/Cryptographic_hash_function)** produce un'impronta di dimensione fissa dei dati e fornisce il controllo dell'**integrità**. L'hash è a senso unico e non è cifratura. Per memorizzare le password, usa una funzione di hash per password lenta e con sale, mai un semplice hash veloce (vedi capitolo 4.2 sulla sicurezza delle applicazioni).

La lezione pratica: la cifratura nasconde i dati ma non prova chi li ha inviati e un hash rileva la manomissione ma non nasconde nulla. La maggior parte dei sistemi reali le combina, ed è esattamente per questo che dovresti appoggiarti a librerie che le raggruppano correttamente.

### Cifra in transito con TLS aggiornato

Proteggi ogni salto di rete con il [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS), il protocollo che protegge i dati mentre si spostano tra i sistemi. Richiedi versioni TLS moderne, disabilita quelle obsolete, scegli suite di cifratura forti e convalida correttamente i certificati anziché disattivare i controlli per "farlo funzionare". Cifra anche il traffico interno tra servizi, non solo il bordo pubblico, perché una postura zero trust presume che la rete interna sia ostile. Automatizza emissione e rinnovo dei certificati così che il TLS sia il valore predefinito senza sforzo ovunque.

### Cifra a riposo con la cifratura a busta

Cifra per impostazione predefinita i dati memorizzati: database, archiviazione di oggetti, backup e log. Lo schema standard è la **cifratura a busta**, dove una **chiave di cifratura dei dati (DEK)** cifra i dati veri e propri e una **chiave di cifratura delle chiavi (KEK)** tenuta in un servizio di gestione delle chiavi cifra la DEK. Questo ti permette di ruotare la chiave principale senza ricifrare terabyte di dati e tiene la potente chiave radice dentro un confine rinforzato. Memorizza accanto ai dati solo la DEK avvolta e recuperala e svolgila al momento dell'uso.

### Gestisci il ciclo di vita delle chiavi con deliberazione

Il ciclo di vita di una chiave è la parte davvero difficile della crittografia e dove nasce la maggior parte delle violazioni e delle interruzioni. Gestisci ogni fase di proposito:

- **Generazione:** crea le chiavi da una forte fonte casuale, con una forza appropriata.
- **Distribuzione:** porta le chiavi ai sistemi che ne hanno bisogno senza esporle in codice, file di configurazione o chat.
- **Rotazione:** sostituisci le chiavi con una pianificazione e sii in grado di ruotare in fretta in caso di sospetta compromissione.
- **Revoca:** invalida in fretta una chiave o un certificato compromesso e assicurati che i sistemi rispettino la revoca.
- **Distruzione:** ritira in modo sicuro il materiale delle chiavi vecchie così che non possa essere recuperato.

Usa un **servizio di gestione delle chiavi (KMS)** per centralizzare tutto questo e usa un [modulo di sicurezza hardware](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM), un dispositivo a prova di manomissione che genera e custodisce le chiavi così che non escano mai in chiaro, per le tue chiavi della massima garanzia. Separa chi può gestire le chiavi da chi può leggere i dati protetti, così che la custodia delle chiavi faccia rispettare la separazione dei compiti. Questo si collega direttamente a classificazione dei dati e regole di custodia del capitolo 4.5 (privacy e protezione dei dati).

### Distingui la gestione dei segreti dalla gestione delle chiavi

Si sovrappongono ma non sono la stessa cosa. La **gestione delle chiavi** governa le chiavi crittografiche e il loro ciclo di vita, di solito dentro un KMS o un HSM che esegue le operazioni crittografiche per te così che la chiave grezza non esca mai. La **gestione dei segreti** governa le credenziali applicative (password di database, token API, certificati) che i servizi devono recuperare e usare in chiaro, di solito da un vault di segreti con accesso di breve durata e verificato. Usa un KMS per le chiavi, un gestore di segreti per le credenziali e non incollare mai né le une né gli altri nel codice sorgente o in file d'ambiente inseriti nel controllo di versione.

### Automatizza PKI e cicli di vita dei certificati

L'**infrastruttura a chiave pubblica (PKI)** è il sistema di autorità di certificazione, certificati e catene di fiducia che lega le chiavi pubbliche alle identità. Su larga scala, il rischio PKI dominante è la scadenza a sorpresa di un certificato che mette fuori uso un servizio. Mantieni un inventario di ogni certificato, monitora le scadenze e automatizza emissione e rinnovo così che nessun umano debba ricordare. I certificati di breve durata rinnovati automaticamente sono più sicuri di quelli di lunga durata accuditi a mano, perché l'automazione rimuove il singolo punto di guasto umano. I protocolli standard qui supportano l'interoperabilità tra fornitori (capitolo 3.8 su interoperabilità e standard aperti).

### Costruisci per l'agilità crittografica e la migrazione post-quantistica

Gli algoritmi si indeboliscono col tempo e gli standard si spostano. L'**agilità crittografica** significa progettare i sistemi così da poter scambiare algoritmi e dimensioni delle chiavi senza una riscrittura dolorosa: astrai la crittografia dietro una piccola interfaccia, versiona i dati cifrati così da sapere quale algoritmo li ha prodotti e tieni un inventario crittografico di che cosa usi dove. Conta ora a causa della [crittografia post-quantistica](https://en.wikipedia.org/wiki/Post-quantum_cryptography), la nuova famiglia di algoritmi progettati per resistere ai futuri computer quantistici. Gli avversari possono raccogliere oggi dati cifrati per decifrarli dopo, quindi i segreti di lunga durata hanno bisogno di un piano di migrazione. Non devi farti prendere dal panico, ma dovresti conoscere il tuo inventario ed essere pronto ad adottare gli algoritmi post-quantistici standardizzati man mano che le piattaforme li rilasciano.

### Preferisci implementazioni convalidate dove richiesto

Per i sistemi regolamentati e governativi, usare un algoritmo forte non basta; l'implementazione deve essere convalidata. **FIPS 140** (Federal Information Processing Standard 140) è lo standard statunitense per convalidare i moduli crittografici e molti contratti richiedono crittografia convalidata FIPS. Il lavoro governativo può anche seguire indicazioni nazionali come la suite Commercial National Security Algorithm (CNSA) della NSA per i sistemi classificati. Controlla quale regime si applica prima di costruire, perché adattare tardi i moduli convalidati è costoso. Questo si collega a evidenze di conformità e governance (capitolo 4.6).

## Compromessi: vantaggi e svantaggi

| Decisione | Vantaggi | Svantaggi |
|---|---|---|
| KMS gestito dal fornitore | Facile, integrato, basso onere operativo | Il fornitore detiene la custodia; meno controllo diretto |
| Chiavi gestite dal cliente / HSM | Piena custodia, soddisfa mandati rigorosi | Onere operativo, rischio di perdere le chiavi |
| Certificati automatici di breve durata | Nessuna scadenza a sorpresa, revoca rapida | Richiede un investimento iniziale in automazione |
| Certificati di lunga durata | Semplice, meno parti mobili | Scadenze gestite da umani causano interruzioni |
| Cifratura a busta | Rotazione economica delle chiavi, protegge la chiave principale | Più parti mobili da capire |
| Agilità crittografica in anticipo | Migrazioni future economiche | Astrazione e sforzo di progetto extra ora |
| Adozione precoce del post-quantistico | Protegge i segreti di lunga durata | Strumenti immaturi, chiavi più grandi, qualche rischio |

La tensione centrale è controllo contro onere operativo. Tenere le proprie chiavi in un HSM dà la massima custodia e soddisfa i mandati più rigorosi, ma richiede competenza e crea un nuovo rischio catastrofico: perdi la chiave e perdi i dati, in modo irrecuperabile. I servizi gestiti dal fornitore rimuovono quell'onere ma pongono la custodia presso il fornitore. Risolvilo a strati: usa servizi gestiti con valori predefiniti sensati per la maggior parte dei sistemi e riserva chiavi gestite dal cliente e HSM ai dati a più alta classificazione dove il controllo extra vale il costo e il rischio.

## Domande da discutere con il tuo team

1. **Avete un inventario completo di chiavi, certificati e algoritmi su cui vi appoggiate?** Non puoi ruotare, migrare o verificare ciò che non vedi e la maggior parte delle organizzazioni scopre di avere molto più materiale crittografico sparso tra i servizi di quanto qualcuno ne segua. Un inventario è il prerequisito di ogni decisione successiva: monitoraggio delle scadenze dei certificati, rotazione delle chiavi, ambito FIPS e pianificazione post-quantistica dipendono tutti da esso. Porta un elenco dei tuoi attuali certificati e delle loro scadenze e chiediti chi possiede ciascuno e che cosa si rompe quando scade. Per un grande patrimonio, la risposta onesta è di solito che non esiste una singola fonte di verità e costruirne una è il primo passo a più alta leva. Se oggi non puoi enumerare la tua crittografia, agilità e rotazione sono aspirazioni, non capacità.

2. **Potete ruotare o revocare in fretta una chiave compromessa, e l'avete mai provato?** Rotazione e revoca sono le parti del ciclo di vita delle chiavi che contano solo sotto pressione e i team scoprono di routine durante un incidente che una chiave è scritta nel codice in una dozzina di posti o che la revoca non si propaga davvero. Decidi il tuo tempo obiettivo per ruotare una chiave e revocare un certificato, poi provalo prima di averne bisogno. Porta la storia della tua ultima esposizione di credenziali e percorri che cosa ha richiesto in pratica la rotazione. Per i sistemi aziendali e governativi, una rotazione non provata può significare scegliere tra un'esposizione prolungata e un'interruzione autoinflitta. Se la rotazione non è mai stata testata, presumi che non funzioni.

3. **Dove sta la custodia delle chiavi, e fa rispettare la separazione dei compiti?** Chi può gestire una chiave e chi può leggere i dati che essa protegge non dovrebbero essere la stessa persona, perché fondere quei poteri vanifica in silenzio lo scopo della cifratura a riposo. Questa scelta guida anche se usi chiavi gestite dal fornitore, chiavi gestite dal cliente o HSM, ciascuna con diverso controllo e diverso rischio operativo. Porta le tue attuali politiche delle chiavi e controlla se una singola identità può sia amministrare una chiave sia accedere al testo in chiaro dietro di essa, un divario silenzioso comune. Per i dati regolamentati e classificati, le regole di custodia possono essere dettate dalla classificazione dei dati (capitolo 4.5) e da un mandato. Se custodia e accesso non sono separati, la tua cifratura ti protegge meno di quanto suggerisca il cruscotto.

4. **Come vi riprendereste se la chiave principale che protegge la vostra cifratura a busta fosse persa o distrutta?** Chiavi gestite dal cliente e HSM ti danno la custodia, ma ti consegnano una nuova modalità di guasto catastrofica: perdi la chiave di cifratura delle chiavi e ogni chiave di cifratura dei dati che essa avvolge diventa permanentemente illeggibile, insieme ai dati che stanno dietro. Pesalo contro il rischio opposto di un backup troppo ampio che ricrea in silenzio proprio il problema di custodia che stavi cercando di risolvere. Porta i tuoi attuali accordi di backup e deposito delle chiavi, il raggio d'impatto di ciascuna chiave principale e l'evidenza che un ripristino è stato davvero eseguito anziché solo documentato. Per i patrimoni aziendali e governativi, lega questo alle tue regole di classificazione dei dati: le chiavi più sensibili spesso vietano copie casuali, quindi il ripristino deve essere progettato deliberatamente, testato con una pianificazione e riconciliato con qualsiasi requisito normativo di provare che il materiale di chiavi ritirato sia stato distrutto.

5. **Quanto sono pronti i vostri sistemi a una migrazione post-quantistica, e quali segreti di lunga durata migrereste per primi?** Gli avversari possono raccogliere oggi traffico e archivi cifrati e decifrarli quando i computer quantistici matureranno, quindi qualsiasi segreto che deve restare riservato per anni è già esposto a un futuro che non puoi vedere. La pressione contraria è che gli strumenti post-quantistici sono ancora giovani, le chiavi sono più grandi e muoversi troppo presto rischia di scommettere su un algoritmo che cambia prima di assestarsi. Porta il tuo inventario crittografico, un elenco di segreti ordinati per quanto a lungo devono restare riservati e una lettura onesta se la tua architettura può scambiare algoritmi senza una riscrittura. Per il lavoro governativo e regolamentato, i registri con mandati di riservatezza pluridecennali rendono questo concreto anziché teorico e gli appalti possono presto richiedere un piano di migrazione documentato e il supporto degli algoritmi post-quantistici standardizzati.

6. **Quando la normativa richiede crittografia convalidata, sapete esattamente quali moduli sono nell'ambito e se si qualificano?** Usare un algoritmo forte non è lo stesso che usare un'implementazione convalidata e i team scoprono di routine tardi che una libreria, un runtime di linguaggio o un servizio cloud non è coperto dal confine FIPS 140 che un contratto esige. La tensione è che i moduli convalidati possono restare indietro rispetto alle librerie correnti per funzionalità e velocità, quindi sceglierli vincola il tuo stack in modi che contano per l'ingegneria. Porta l'elenco dei moduli crittografici che ogni sistema regolamentato chiama davvero, i certificati di convalida che li coprono e il mandato specifico (FIPS 140, CNSA o una regola di settore) che si applica. Per i programmi aziendali e governativi, decidi questo prima di costruire, perché adattare i moduli convalidati e riautorizzare un sistema a posteriori è costoso, lento e spesso costringe a riprogettare proprio i componenti che pensavi finiti.

## Lente settoriale

**Startup.** Appoggiati interamente ai valori predefiniti collaudati della tua piattaforma e spendi zero tempo di ingegneria in crittografia su misura. Attiva la cifratura a riposo gestita, termina il TLS con certificati rinnovati automaticamente, fai l'hash delle password con una funzione lenta standard e tieni i segreti nel gestore di segreti della piattaforma anziché nel repository. La tua unica decisione di progetto è una sottile interfaccia attorno alla manciata di campi che cifri nell'applicazione, così che un futuro passaggio fuori dalle chiavi gestite dal fornitore non sia una riscrittura.

**Piccola impresa.** Non hai un crittografo e hai poca voglia di gestire un HSM, quindi compra la custodia anziché costruirla: usa il KMS e il gestore di segreti gestiti dal fornitore che arrivano con i tuoi strumenti cloud o SaaS. Imposta il lavoro come igiene, cioè nessuna chiave nel codice, cifratura attivata ovunque per impostazione predefinita e scadenze dei certificati monitorate così che nulla scada a sorpresa. Riserva le chiavi gestite dal cliente ai rari dati per cui un contratto o un regolatore le richiede davvero.

**Grande impresa.** Il problema è scala e coerenza tra migliaia di servizi, certificati e chiavi. Gestisci un KMS centralizzato con cifratura a busta, automatizza l'intero ciclo di vita dei certificati così che nessuna scadenza sia accudita a mano e mantieni un unico inventario crittografico che alimenta rotazione, ambito FIPS e pianificazione post-quantistica. Separa la custodia delle chiavi dall'accesso ai dati come controllo dell'intera organizzazione e fai della cifratura una capacità di piattaforma che ogni team eredita anziché un compito che ciascuno reinventa.

**Ente pubblico.** Appalti, convalida e audit plasmano ogni scelta. Usa moduli convalidati FIPS 140 e segui indicazioni nazionali come CNSA per i sistemi classificati, lega la custodia delle chiavi alla classificazione dei dati così che le chiavi più sensibili stiano presso personale abilitato con rigorosa separazione dei compiti e genera evidenze continue di crittografia convalidata per l'autorizzazione continua. Documenta un piano di migrazione post-quantistica per i registri che devono restare riservati per decenni e richiedi ai fornitori di dichiarare quali moduli sono convalidati prima di impegnarti.

## Esempi

**Startup.** Un piccolo team che costruisce un'app di monitoraggio della salute si appoggia interamente a valori predefiniti collaudati. Terminano il TLS con certificati rinnovati automaticamente, attivano la cifratura a riposo sul database gestito e sull'archiviazione di oggetti con il KMS del fornitore e fanno l'hash delle password con una funzione lenta e con sale di una libreria standard. Anziché scrivere loro stessi qualsiasi crittografia, usano una chiamata di cifratura autenticata di alto livello per l'unico campo che devono cifrare nell'applicazione. I segreti vivono nel gestore di segreti della piattaforma, mai nel repository. Costa pochi pomeriggi e rimuove un'intera categoria di errori catastrofici.

**Grande impresa.** Una banca globale gestisce un KMS centralizzato e una flotta di HSM, con un inventario crittografico che segue ogni chiave e certificato tra migliaia di servizi. La cifratura a busta protegge i dati dei clienti, con chiavi dei dati avvolte da chiavi principali che ruotano con una pianificazione mentre i dati restano fermi. Emissione e rinnovo dei certificati sono completamente automatizzati dopo che un'interruzione pubblica ha insegnato loro il costo di un singolo certificato scaduto. Gli amministratori delle chiavi sono un team separato dagli ingegneri applicativi, così che la custodia faccia rispettare la separazione dei compiti, e uno strato di agilità crittografica permette loro di iniziare a sperimentare algoritmi post-quantistici per gli archivi di lunga durata.

**Ente pubblico.** Un'agenzia nazionale che tratta registri classificati usa solo moduli crittografici convalidati FIPS 140 e segue le indicazioni NSA CNSA per i suoi sistemi a più alta classificazione. Le chiavi sono generate e tenute in HSM che non rilasciano mai materiale di chiavi in chiaro e la custodia è legata alla classificazione dei dati così che le chiavi più sensibili stiano presso personale abilitato con rigorosa separazione dei compiti. I certificati girano su una PKI interna gestita con cicli di vita automatizzati e le evidenze continue di crittografia convalidata alimentano l'autorizzazione continua dell'agenzia. Un piano documentato di migrazione post-quantistica protegge i registri che devono restare riservati per decenni.

## Business case: motivazioni, ROI e TCO

La crittografia è un altro ambito in cui un investimento modesto previene perdite catastrofiche da prima pagina. Il costo totale di proprietà comprende un KMS o un HSM, strumenti di gestione di segreti e certificati e il tempo di ingegneria per progettare i cicli di vita e tenere aggiornato un inventario. Questi costi sono reali ma limitati. Il costo di saltarli è una violazione di dati non cifrati, un'interruzione di più ore da un certificato scaduto o una perdita di dati irrecuperabile da una chiave gestita male, ciascuna con sanzioni normative, costi di notifica e danno reputazionale duraturo.

Il ROI più forte viene da automazione e riuso. I cicli di vita automatici dei certificati eliminano la più comune interruzione autoinflitta. La gestione centralizzata delle chiavi con valori predefiniti sensati significa che ogni nuovo servizio eredita cifratura in transito e a riposo senza sforzo per team, trasformando la crittografia da tassa ricorrente in capacità di piattaforma. Per il lavoro regolamentato e governativo, moduli convalidati ed evidenze automatiche abbassano anche il costo di audit e autorizzazione. Quando presenti il caso alla leadership, impostalo con semplicità: gli algoritmi sono gratuiti e collaudati, il rischio vive nella gestione delle chiavi e nelle operazioni sui certificati e un piccolo investimento automatizzato lì previene i fallimenti costosi.

## Antipattern e insidie

- **Scrivere la propria crittografia.** Algoritmi su misura o protocolli costruiti a mano che falliscono in modi sottili e solo da esperti.
- **Chiavi e segreti scritti nel codice.** Credenziali incollate nel sorgente, nei file di configurazione o in chat, dove trapelano e non possono essere ruotate.
- **Cifratura senza disciplina delle chiavi.** Attivare la cifratura ma lasciare l'accesso alle chiavi spalancato o non ruotarle mai.
- **Confondere hash e cifratura.** Trattare un hash come reversibile, o memorizzare le password con un hash veloce anziché lento e con sale.
- **Roulette dei certificati.** Nessun inventario, nessun monitoraggio delle scadenze e periodiche interruzioni a sorpresa quando un certificato scade.
- **Custodia delle chiavi e accesso ai dati fusi.** Un'identità che può sia gestire una chiave sia leggere i dati che essa protegge.
- **Nessun piano di rotazione.** Chiavi che non sono mai state ruotate e non possono essere ruotate in fretta sotto pressione.
- **Crittografia senza agilità.** Algoritmi cablati così a fondo che scambiarli richiede una riscrittura, bloccando qualsiasi migrazione futura.
- **Ignorare i mandati di convalida.** Usare algoritmi forti in moduli non convalidati dove è richiesta la convalida FIPS o simile.

## Modello di maturità

- **Livello 1, Avvio:** La cifratura è incoerente e spesso assente, applicata in modo reattivo quando qualcuno nota un divario. Chiavi e segreti sono scritti nel codice o condivisi informalmente in chat e file di configurazione. Non c'è inventario, né rotazione e i certificati scadono a sorpresa e i team occasionalmente scrivono la propria crittografia.
- **Livello 2, Sviluppo:** TLS e cifratura a riposo sono attivati per i sistemi principali ed esiste un KMS o un gestore di segreti, ma l'adozione è disomogenea e varia da team a team. Alcuni certificati sono monitorati mentre altri no, la rotazione è manuale e rara e nessun inventario crittografico completo lega il tutto.
- **Livello 3, Standardizzazione:** La cifratura in transito e a riposo è il valore predefinito documentato e fatto rispettare nell'organizzazione. Le chiavi vivono in un KMS con rotazione pianificata e cifratura a busta, la custodia delle chiavi è separata dall'accesso ai dati, i cicli di vita dei certificati sono automatizzati, un inventario crittografico è mantenuto e i moduli convalidati sono usati ovunque la normativa li richieda.
- **Livello 4, Gestione:** Il patrimonio crittografico è misurato e controllato rispetto a valori di riferimento. Segui l'anticipo sulla scadenza dei certificati, la percentuale di chiavi ruotate secondo pianificazione, il tempo medio di revoca di una chiave compromessa, i rilevamenti di segreti nel codice per periodo e la copertura dell'inventario e rivedi queste metriche rispetto a obiettivi. Rotazione e revoca sono provate con una cadenza con tempi registrati e le deviazioni innescano azioni correttive anziché passare inosservate.
- **Livello 5, Orchestrazione:** La crittografia è una capacità di piattaforma che ogni servizio eredita per impostazione predefinita ed è migliorata di continuo e integrata nell'organizzazione. Rotazione e revoca sono rapide e routinariamente esercitate, gli HSM proteggono le chiavi a più alta garanzia e agilità crittografica più un piano attivo di migrazione post-quantistica mantengono il patrimonio adattivo al mutare di algoritmi e mandati. Le evidenze di conformità sono prodotte automaticamente e alimentano l'autorizzazione continua.

## Spunti di discussione

1. Quali sistemi del vostro patrimonio giustificano chiavi gestite dal cliente o HSM dato il loro costo operativo e il rischio di perdita catastrofica?
2. Come costruireste e mantenereste un'unica fonte di verità per ogni chiave e certificato che possedete?
3. Qual è oggi il vostro tempo realistico per ruotare una chiave compromessa, e che cosa lo rende lento?
4. Dove la vostra architettura rende difficile scambiare un algoritmo crittografico, e come lo correggereste prima di una migrazione forzata?
5. Quali dei vostri segreti di lunga durata conterebbero se un avversario li raccogliesse ora e li decifrasse anni dopo?
6. Segreti e chiavi finiscono mai nel codice, nella configurazione o nei log, e come lo sapreste?

## Punti chiave

- **Non scrivere la tua crittografia.** Usa librerie collaudate e algoritmi standard al più alto livello di astrazione sicuro.
- **Gli algoritmi sono facili; la gestione delle chiavi è difficile.** Il ciclo di vita di una chiave (generazione, distribuzione, rotazione, revoca, distruzione) è dove vivono i fallimenti reali.
- **Conosci le tue garanzie:** la cifratura simmetrica e a chiave pubblica protegge la riservatezza, le firme provano autenticità e integrità e l'hash rileva la manomissione ma non è cifratura.
- **Cifra in transito con TLS aggiornato e a riposo con cifratura a busta**, come valore predefinito per ogni sistema.
- **Separa la custodia delle chiavi dall'accesso ai dati**, usa un KMS per le chiavi e un gestore di segreti per le credenziali e non scrivere mai nel codice né le une né le altre.
- **Automatizza i cicli di vita dei certificati** per eliminare l'interruzione da scadenza a sorpresa e mantieni un inventario crittografico.
- **Costruisci per l'agilità crittografica** e avvia un piano di migrazione post-quantistica per i segreti di lunga durata.
- **Preferisci implementazioni convalidate** (FIPS 140 e indicazioni nazionali applicabili) dove la normativa o la classificazione le richiedono.

## Riferimenti e letture di approfondimento

- National Institute of Standards and Technology, *FIPS 140-3: Security Requirements for Cryptographic Modules*.
- National Institute of Standards and Technology, *SP 800-57: Recommendation for Key Management*.
- National Institute of Standards and Technology, *SP 800-131A: Transitioning the Use of Cryptographic Algorithms and Key Lengths*.
- National Institute of Standards and Technology, standard di crittografia post-quantistica (FIPS 203, 204 e 205).
- Niels Ferguson, Bruce Schneier e Tadayoshi Kohno, *Cryptography Engineering*.
- Jean-Philippe Aumasson, *Serious Cryptography*.
- David Wong, *Real-World Cryptography*.
- Internet Engineering Task Force, *RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3*.
- Open Web Application Security Project, *Cryptographic Storage Cheat Sheet* e *Transport Layer Protection Cheat Sheet*.
- National Security Agency, indicazioni sulla suite *Commercial National Security Algorithm (CNSA)*.
