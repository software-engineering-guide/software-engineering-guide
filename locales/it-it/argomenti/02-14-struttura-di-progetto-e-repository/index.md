# 2.14 Struttura di progetto e repository

## Panoramica e motivazioni

La struttura di progetto e repository è l'organizzazione fisica di una base di codice: le cartelle, i file e le convenzioni di nomi che decidono dove vive ogni cosa. Un *repository* (spesso abbreviato in "repo") è il contenitore sotto [controllo di versione](https://en.wikipedia.org/wiki/Version_control) che tiene i file di un progetto e la loro storia. Un *progetto*, a volte chiamato *soluzione* quando raggruppa più componenti correlati, è l'unità logica di software che stai costruendo. La struttura è la mappa che usi per trovare, capire e modificare quel software.

In un piccolo team, una persona può tenere a mente l'intera organizzazione. In un grande team, con centinaia o migliaia di ingegneri, frequenti spostamenti tra team e collaboratori esterni che entrano e escono, ogni repository organizzato in modo diverso fa pagare una nuova tassa cognitiva. Quando apri un repo sconosciuto, dovresti poter indovinare dove vivono sorgenti, test, documentazione e configurazione di rilascio, senza leggere un manuale. Quando ogni repo risponde a quelle domande allo stesso modo, la mobilità costa poco e l'inserimento è rapido. Quando ogni repo è un caso unico, ogni cambio di contesto diventa una piccola ricerca.

Nei contesti aziendali e governativi, una struttura coerente è anche una questione di controllo e garanzia. Auditor, revisori della sicurezza e manutentori a lungo termine, che spesso lavorano anni dopo che gli autori originali se ne sono andati, hanno bisogno di individuare in modo affidabile documenti di specifica, file di licenza, politiche di sicurezza e definizioni di build. Un'organizzazione prevedibile permette anche agli strumenti automatici (scanner, analizzatori di dipendenze, controlli di conformità) di funzionare allo stesso modo su un intero portafoglio di sistemi. Questo capitolo tratta quindi la struttura come una convenzione che decidi una volta e applichi ovunque. È strettamente legata a standard di codifica e stile (capitolo 2.1), controllo di versione e gestione dei sorgenti (capitolo 2.6) e documentazione (capitolo 2.7).

## Principi chiave

- Segui il *[principio del minimo stupore](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)*: l'organizzazione dovrebbe corrispondere a ciò che un ingegnere esperto si aspetterebbe, così che non ci sia nulla da memorizzare.
- La coerenza tra repository batte l'ingegnosità locale; una struttura abbastanza uniforme ovunque vale più della struttura perfetta in un posto solo.
- Il [README](https://en.wikipedia.org/wiki/README) è la porta d'ingresso; un nuovo arrivato dovrebbe orientarsi dal solo README.
- Rendi la struttura autodescrittiva attraverso i nomi, così che cartelle e file annuncino il proprio scopo.
- Fai rispettare la struttura con scheletri e modelli, non con forza di volontà e commenti di revisione.
- Separa fisicamente le responsabilità: sorgenti, test, documentazione, build e rilascio appartengono a luoghi distinti e prevedibili.
- Organizza le dipendenze in modo che fluiscano in un'unica direzione, dai nuclei stabili verso i margini volatili.

## Raccomandazioni

### Adotta un'organizzazione coerente al livello più alto

Definisci un insieme standard di cartelle di primo livello che ogni repository usa dove applicabile e documenta a che cosa serve ciascuna. Una convenzione comune e neutrale rispetto ai fornitori comprende: una cartella dei sorgenti (spesso `src`) per il codice di produzione; una cartella dei test (spesso `test` o `tests`) per i test automatici; una cartella `docs` per la documentazione; una cartella `build` per le definizioni e gli output di build; una cartella `deploy` per il rilascio e l'*[infrastruttura come codice](https://en.wikipedia.org/wiki/Infrastructure_as_code)* (definizioni leggibili da macchina di server, reti e servizi, trattate nel capitolo 8.2); una cartella `scripts` per automazione e strumenti per sviluppatori; una cartella `examples` per esempi eseguibili; e una cartella `spec` o `specification` per specifiche di requisiti e di progetto. Non ogni repo ha bisogno di ogni cartella, ma dove una questione esiste, dovrebbe vivere nel luogo atteso con il nome atteso.

### Fai del README il punto d'ingresso

Richiedi un file README alla radice del repository come unico punto di partenza canonico. Dovrebbe dire che cosa è il progetto, come costruirlo ed eseguirlo, come eseguire i test, dove trovare la documentazione più approfondita, chi ne è responsabile e come contribuire. Il README non è l'intero insieme di documentazione; è l'indice che rimanda al resto (capitolo 2.7). Tratta un README mancante o obsoleto come un difetto, perché è la prima cosa che ogni nuovo ingegnere, auditor o integratore leggerà.

### Standardizza i file di editor e di configurazione

Inserisci nel repository la configurazione condivisa di editor e strumenti, così che ogni contributore ottenga automaticamente un comportamento coerente. Un file `.editorconfig` (un semplice file indipendente dall'editor che definisce regole di spazi, indentazione e fine riga) mantiene uniforme la formattazione di base tra editor e sistemi operativi diversi. Aggiungi un file di esclusione per il sistema di controllo di versione (così che output di build e artefatti locali non vengano mai committati), insieme alle configurazioni condivise di formattatore e linter descritte nel capitolo 2.1. Questi file rendono attive le convenzioni del repository, non solo documentate.

### Definisci convenzioni di nomi e di cartelle

Concorda convenzioni per denominare cartelle e file (maiuscole e minuscole, separatori, singolare contro plurale e suffissi richiesti come quelli che marcano i test) e applicale in modo uniforme. I nomi dovrebbero rivelare l'intento e corrispondere al vocabolario di dominio usato altrove nell'organizzazione. L'obiettivo è semplice: un percorso dovrebbe comunicare significato, così che leggere il nome di una cartella o di un file ti dica che cosa contiene senza aprirlo.

### Organizza con deliberazione livelli e dipendenze

Struttura la base di codice in modo che i suoi livelli architetturali compaiano nella disposizione delle cartelle e che le dipendenze fluiscano in un'unica direzione sensata. Le politiche di livello più alto non dovrebbero dipendere dal dettaglio di basso livello. Il codice condiviso e stabile dovrebbe stare dove molti moduli possono raggiungerlo senza creare cicli. Quando rendi fisica la stratificazione, riflessa nell'albero delle directory, gli ingegneri hanno più probabilità di rispettarla e le violazioni sono più facili da individuare in revisione e nei controlli automatici delle dipendenze.

### Fai rispettare la struttura con scheletri e modelli

Fornisci *[scheletri](https://en.wikipedia.org/wiki/Scaffold_%28programming%29)* (scaffolding), la generazione automatica di un progetto iniziale, così che i nuovi repository nascano già corretti. Un *modello* o *cookiecutter* (uno scheletro di progetto parametrizzato che genera un repository pronto a partire dalle risposte a poche domande) codifica in un unico posto l'organizzazione standard, il README, i file di configurazione e la configurazione della [CI](https://en.wikipedia.org/wiki/Continuous_integration). Quando gli ingegneri creano nuovi servizi da un modello condiviso, la coerenza diventa l'impostazione predefinita anziché un'aspirazione, e i miglioramenti al modello si propagano ai progetti futuri.

### Mantieni coerente la struttura su molti repository su larga scala

Tratta l'organizzazione stessa come uno standard governato: mantenuto centralmente come qualsiasi altro standard ingegneristico (capitolo 1.7) e versionato come codice (capitolo 2.6). Pubblicala, fornisci i modelli che la implementano e consenti deviazioni solo attraverso un processo di eccezioni documentato, così che "lo standard" conservi il proprio significato. A scala di portafoglio, quasi tutto il valore della struttura viene dalla sua uniformità tra i repository, quindi la deriva è il rischio principale da gestire.

### Lascia che la struttura informi la scelta tra monorepo e multi-repo

Metti in relazione la struttura con la decisione sul confine dei repository trattata nel capitolo 2.6. Un *[monorepo](https://en.wikipedia.org/wiki/Monorepo)* (un repository che contiene molti progetti) ha bisogno di una chiara convenzione interna per separare i progetti e il loro codice condiviso, così che l'unico albero resti navigabile. Un approccio *multi-repo* (molti piccoli repository, uno per progetto o servizio) ha bisogno di una forte coerenza tra repository, così che ogni repo sembri familiare anche se sta da solo. In entrambi i casi, una struttura documentata e basata su modelli è ciò che mantiene prevedibile la navigazione. La scelta del confine cambia dove applichi la convenzione, non se ne hai bisogno.

## Compromessi: vantaggi e svantaggi

| Scelta | Vantaggi | Svantaggi |
|---|---|---|
| Rigoroso standard di organizzazione valido per tutta l'organizzazione | Familiarità immediata; ingegneri portabili; strumenti uniformi | Occasionale scarso adattamento a progetti insoliti; richiede governance |
| Libertà di organizzazione per team | Ottimizzazione locale; alta autonomia | Frammentazione; costoso cambio di contesto; strumenti incoerenti |
| Scheletri e modelli | Repo corretti per impostazione predefinita; le modifiche si propagano | Manutenzione dei modelli; rischio di deriva dai repo generati |
| Gerarchia di cartelle profonda e a livelli | Struttura esplicita; confini chiari | Onere di navigazione; percorsi lunghi; rischio di sovra-ingegnerizzazione |
| Organizzazione piatta e poco profonda | Facile da scorrere; poca cerimonia | Scarsa separazione; si sfalda man mano che il progetto cresce |

Il compromesso dominante è tra uniformità e autonomia. Un unico standard di organizzazione toglie attrito ai molti ingegneri che si spostano tra basi di codice, a costo del progetto occasionale le cui esigenze non entrano bene nello stampo. In una grande organizzazione, il guadagno collettivo della familiarità supera quasi sempre quella perdita locale. È per questo che l'impostazione raccomandata è uno standard predefinito forte più un percorso di eccezione documentato (capitolo 1.7), anziché una rigida uniformità o una libertà non gestita. Un compromesso secondario è tra profondità e semplicità: struttura sufficiente a separare le questioni reali, ma non così tanta che la navigazione diventi una scarpinata tra cartelle vuote.

## Domande da discutere con il tuo team

1. **Quando un ingegnere passa a un repo nostro che non conosce, quanto passa prima che riesca a trovare i test, la configurazione di rilascio e il responsabile?** È la tassa di navigazione che la struttura esiste per eliminare, e a scala di portafoglio viene pagata migliaia di volte all'anno in piccoli incrementi che si sommano in una seria perdita di tempo ingegneristico. Il punto del principio del minimo stupore è che un ingegnere esperto dovrebbe poter indovinare dove vivono sorgenti, test, documentazione e rilascio senza leggere un manuale, quindi la prova onesta è se quella ipotesi riesce nei tuoi repo. Porta alla riunione un numero reale: cronometrati mentre ti orienti in due o tre repository interni sconosciuti, oppure estrai i dati di inserimento su quanto impiegano i nuovi arrivati a fare una prima modifica. Se la risposta si misura in giorni di ricerca anziché in minuti di riconoscimento, hai quantificato il costo dei repo unici, e questo giustifica l'investimento una tantum in un'organizzazione standard condivisa da ogni repo.

2. **I nostri livelli architetturali compaiono nell'albero delle cartelle, o i cicli di dipendenza si nascondono dentro un'organizzazione piatta?** La struttura non riguarda solo il trovare le cose: quando rendi fisica la stratificazione, gli ingegneri la rispettano e revisori e controlli automatici delle dipendenze possono individuare le violazioni, mentre un mucchio piatto lascia infiltrare accoppiamento improprio e cicli inosservati finché il cambiamento diventa pericoloso. In un sistema grande e di lunga durata è ciò che impedisce alla politica di livello più alto di dipendere in silenzio dal dettaglio di basso livello, ed è esattamente il tipo di erosione che costa poco da prevenire e molto da sciogliere. Porta il tuo grafo delle dipendenze o fai un rapido controllo: ci sono cicli, e qualcosa di stabile dipende da qualcosa di volatile? La risposta dovrebbe spingerti a riflettere i livelli nelle directory e ad aggiungere controlli automatici della direzione delle dipendenze, così che i confini siano visibili nell'albero e fatti rispettare nella pipeline anziché vivere solo nel modello mentale di qualcuno.

3. **I nostri nuovi repository partono corretti da un modello, o ci affidiamo a una pagina di wiki e alle buone intenzioni?** La struttura fatta rispettare da uno scheletro è l'impostazione predefinita; la struttura descritta in un documento deriva, perché la realtà segue ciò che genera i repo, non ciò che una pagina dice che dovrebbero sembrare. Per un'organizzazione grande o regolamentata è anche una questione di garanzia: quando ogni repo è generato da un modello condiviso, scanner di sicurezza, analizzatori di dipendenze e auditor trovano ogni volta nello stesso posto la licenza, la politica di sicurezza, la specifica e la definizione di build, tra fornitori e tra anni. Porta le prove: quanti dei tuoi repo recenti sono stati creati con lo scheletro dal modello standard rispetto a quelli assemblati a mano, e quanto si sono allontanati nel frattempo quelli creati dal modello? L'azione è fare del modello l'unico modo facile di avviare un repo, governarlo come standard versionato con un percorso di eccezione documentato e rilevare la deriva in automatico, perché l'uniformità è dove vive quasi tutto il valore della struttura.

4. **Abbiamo deciso se il nostro standard copre un monorepo o molti repository separati, e la stessa convenzione regge davvero su entrambi i lati di quel confine?** La scelta del confine dei repository cambia dove applichi la convenzione, non se ne hai bisogno, e sbagliarla significa un unico albero gigantesco che nessuno sa navigare o un'espansione di repo che sembrano ciascuno estraneo. Un monorepo ha bisogno di una chiara convenzione interna per separare i progetti e il loro codice condiviso così che l'unico albero resti navigabile, mentre un approccio multi-repo ha bisogno di una forte coerenza tra repository così che ogni repo autonomo sembri comunque familiare. Porta l'inventario attuale: quanti repo hai, come il codice condiviso è separato dentro un eventuale monorepo e una prova a tempo di se un ingegnere riesce a trovare un progetto dentro il grande albero in fretta quanto ne trova uno in un repo autonomo. Per una grande impresa o un programma governativo in cui fornitori diversi consegnano repository separati, decidi con deliberazione quali parti della convenzione sono universali e quali specifiche del confine, perché auditor e strumenti di piattaforma devono funzionare allo stesso modo sia che il codice arrivi come un albero sia come cinquanta.

5. **Chi possiede il nostro standard di struttura, e che cosa accade davvero quando un progetto non vi rientra davvero?** A scala di portafoglio quasi tutto il valore della struttura viene dall'uniformità, quindi i veri rischi sono uno standard senza responsabile che marcisce e un percorso di eccezione così vago che ogni team inventa in silenzio la propria organizzazione. La tensione è tra una rigida uniformità che non si adatta a nessun progetto insolito e una libertà non gestita che frammenta tutto, e la risposta sana è un forte valore predefinito più un processo di eccezione documentato e verificabile, governato da un responsabile nominato e versionato come codice. Porta le prove: c'è un unico responsabile, un documento di standard versionato con un registro delle modifiche, un registro delle eccezioni concesse e dei perché e un conteggio delle deviazioni non documentate che riesci a trovare in giro. Nei contesti aziendali e governativi un'eccezione che nessuno ha registrato è una lacuna di controllo, quindi collega ogni deviazione a una giustificazione scritta e a una data di revisione e assicurati che i contratti di appalto che impongono l'organizzazione indichino anche chi può approvare le deroghe.

6. **README e file di configurazione inseriti nel repository rendono attive le nostre convenzioni, o sono decorativi?** Un README è la porta d'ingresso e i file `.editorconfig`, di esclusione e di configurazione del linter inseriti nel repository sono ciò che rende le convenzioni capaci di far valere se stesse, eppure queste sono le prime cose a diventare obsolete e le ultime che qualcuno nota finché un auditor o un nuovo arrivato non riesce a far compilare il progetto. La tensione è tra un README snello che resta aggiornato e uno completo che deriva e tra il fidarsi che le persone formattino correttamente il codice e lasciare che la configurazione condivisa lo faccia rispettare in automatico. Porta un campione: prendi cinque repo e controlla quanti README dicono davvero che cosa è il progetto, come costruirlo, testarlo ed eseguirlo e chi ne è responsabile, e quanti portano i file di configurazione condivisi anziché affidarsi alle abitudini individuali. Per un'organizzazione grande o regolamentata, dove integratori, revisori della sicurezza e manutentori a lungo termine leggono il README prima di qualsiasi altra cosa, tratta una porta d'ingresso mancante o obsoleta come un difetto con un responsabile e controlla la presenza dei file di configurazione in automatico, così che la conformità non dipenda dalla buona volontà.

## Lente settoriale

**Startup.** Vince la velocità, quindi concorda un'unica organizzazione semplice e abbastanza piatta per il tuo primo repo (src, test, docs, scripts, un README compilato, un `.editorconfig` e file di esclusione) e salvala come modello leggero lo stesso pomeriggio. Genera il secondo servizio da esso, così che entrambi i repo sembrino familiari e un nuovo collaboratore esterno si inserisca in ore anziché ricostruire a ritroso un caso unico. Resisti a gerarchie profonde e a una governance pesante di cui non hai ancora bisogno; tutto il ritorno qui è che due fondatori e un collaboratore esterno condividano un'unica mappa.

**Piccola impresa.** Senza uno specialista di piattaforma e con un budget ridotto, adotta l'organizzazione convenzionale che il tuo linguaggio o framework già presume anziché inventarne una, così che gli strumenti già pronti e ogni nuovo assunto arrivino già addestrati su di essa. Compra lo scheletro (un generatore del framework o un modello cookiecutter) anziché costruirne uno tuo e spendi il tuo scarso sforzo a mantenere aggiornato un README compilato. Quel README è l'assicurazione più economica che hai per il giorno in cui la persona che conosceva l'organizzazione passa ad altro.

**Grande impresa.** Tra molti team e centinaia di repository l'obiettivo è l'uniformità: pubblica uno standard di struttura versionato, genera ogni nuovo servizio da modelli condivisi, rileva la deriva in automatico e consenti deviazioni solo attraverso un processo di eccezioni documentato. Poiché ogni repo appare uguale, un ingegnere riassegnato a un nuovo team è produttivo in ore e gli scanner di sicurezza e di dipendenze a livello di portafoglio trovano ogni volta nello stesso posto la licenza, la politica di sicurezza e la definizione di build. Metti a bilancio esplicitamente la manutenzione dei modelli e il rilevamento della deriva, perché quella cura è ciò che mantiene significativo lo standard su larga scala.

**Ente pubblico.** Appalti, trasparenza e responsabilità a lungo termine plasmano l'organizzazione, quindi imponi una struttura comune negli standard di consegna che vincolano ogni fornitore. Richiedi una cartella `specification` che colleghi il codice ai requisiti approvati, un file di licenza e di politica di sicurezza alla radice e una cartella `deploy` che contenga le definizioni di infrastruttura come codice, così che gli auditor individuino gli artefatti di conformità allo stesso modo in ogni sistema. Poiché i collaboratori esterni di fornitori diversi seguono tutti un'unica mappa, la manutenzione dopo la fine di un contratto costa molto meno e il pubblico ottiene una traccia difendibile e ispezionabile dal requisito al codice in esecuzione.

## Esempi

**Startup.** Una startup di tre persone concorda un'organizzazione standard semplice per il suo primo repo (src, test, docs, scripts, un README compilato, un .editorconfig e file di esclusione) e la salva come modello leggero. Quando un mese dopo avviano il secondo servizio, lo generano da quel modello, così che entrambi i repo sembrino già familiari e il nuovo collaboratore esterno si inserisca in un pomeriggio. Resistono a gerarchie di cartelle profonde di cui non hanno ancora bisogno, mantenendo l'albero abbastanza piatto da essere scorso a colpo d'occhio. Il costo è stato un pomeriggio di preparazione, e risparmia loro la proliferazione di casi unici che altrimenti farebbe di ogni futuro repo una piccola ricerca.

**Grande impresa.** Un rivenditore multinazionale gestisce centinaia di servizi in più linguaggi. Il suo team di piattaforma pubblica uno standard di struttura dei repository versionato e un insieme di modelli di progetto che lo implementano. Ogni nuovo servizio è generato da un modello, quindi arriva con le cartelle standard `src`, `test`, `docs`, `deploy` e `scripts`, un README compilato, un `.editorconfig`, file di esclusione e una pipeline di CI funzionante. Poiché ogni repository appare uguale, un ingegnere riassegnato a un nuovo team è produttivo in ore, e gli scanner di sicurezza e di dipendenze a livello di organizzazione girano in modo uniforme perché trovano sempre i file dove se li aspettano.

**Ente pubblico.** Un'agenzia nazionale che modernizza sistemi legacy impone un'organizzazione comune dei repository come parte dei propri standard di consegna per tutti i fornitori. Ogni repository deve contenere una cartella `specification` che colleghi il codice ai requisiti approvati, un README documentato, un file di licenza e di politica di sicurezza alla radice e una cartella `deploy` con le definizioni di infrastruttura come codice (capitolo 8.2). Poiché i collaboratori esterni di fornitori diversi seguono tutti la stessa struttura, gli auditor dell'agenzia possono individuare gli artefatti di conformità allo stesso modo in ogni sistema, e la manutenzione a lungo termine dopo la fine di un contratto costa molto meno perché i manutentori subentranti conoscono già la mappa.

## Business case: motivazioni, ROI e TCO

Il costo di adozione di uno standard di struttura è per lo più una tantum: concordare l'organizzazione, costruire i modelli e documentare la convenzione. Il costo ricorrente è basso, concentrato nel mantenere i modelli e governare le eccezioni. Il costo del *non* avere uno standard è ricorrente e cumulativo: ogni ingegnere che apre un repo sconosciuto paga una tassa di navigazione, ogni inserimento è più lento e gli strumenti automatici devono essere configurati per repo perché nulla sta dove ti aspetti. In una grande organizzazione, questi piccoli attriti si moltiplicano in serie perdite di tempo ingegneristico.

Il ritorno si vede in un inserimento più rapido, mobilità tra team più economica, un segnale più alto dagli strumenti a livello di portafoglio e, negli ambienti regolamentati, minori costi di audit e di manutenzione a lungo termine, perché gli artefatti sono sempre reperibili. Il *costo totale di proprietà* (TCO, cioè il costo complessivo nel corso della vita di costruire, gestire e mantenere un sistema) scende di più nei sistemi di lunga durata, dove i manutentori che beneficiano di una struttura prevedibile non sono di solito gli autori che l'hanno creata. Per sostenere il caso con la leadership, presenta la struttura come uno standard economico e ad alta leva che migliora produttività degli sviluppatori e prontezza all'audit e dai un numero al costo odierno dell'incoerenza usando i dati sul tempo di inserimento e lo sforzo speso a cercare cose in repository sconosciuti.

## Antipattern e insidie

- **Il repository unico:** ogni repo organizzato in modo diverso, così che ciascuno va reimparato da zero.
- **Il README mancante o obsoleto:** nessuna porta d'ingresso, che costringe i nuovi arrivati a ricostruire a ritroso come costruire ed eseguire il progetto.
- **Struttura per documento, non per modello:** una pagina di wiki descrive l'organizzazione standard, ma nulla la genera né la fa rispettare, così che la realtà se ne allontana.
- **Deriva dai modelli:** i repository generati da un modello divergono nel tempo e i miglioramenti al modello non li raggiungono mai.
- **Gerarchia sovra-ingegnerizzata:** nidi profondi di cartelle quasi vuote che aggiungono cerimonia senza aiutare la navigazione.
- **Responsabilità mescolate:** sorgenti, test, output di build e segreti mescolati senza una chiara separazione.
- **Output di build e artefatti locali committati:** file generati inseriti perché le regole di esclusione non sono mai state impostate, che inquinano storia e differenze.
- **Violazioni dei livelli nascoste da una struttura piatta:** nessun confine fisico, così che cicli di dipendenza e accoppiamento improprio si infiltrano inosservati.

## Modello di maturità

- **Livello 1 (Avvio):** ogni repository è organizzato ad hoc dai suoi autori, reagendo a ciò che serve nel momento; le organizzazioni variano molto; i README sono mancanti o inaffidabili; i nuovi arrivati vanno accompagnati a mano in ogni repo.
- **Livello 2 (Sviluppo):** esistono convenzioni di base informali e molti repo si somigliano; alcuni team mantengono un'organizzazione iniziale propria; ma non c'è uno standard autorevole, né scheletri condivisi, e la struttura deriva in modo percepibile da un team all'altro.
- **Livello 3 (Standardizzazione):** uno standard di struttura documentato e versionato è fatto rispettare in tutta l'organizzazione; i nuovi repository sono generati da modelli condivisi che portano un'organizzazione standard, README, file di configurazione e CI; le deviazioni passano per un processo di eccezioni documentato anziché avvenire in silenzio.
- **Livello 4 (Gestione):** la conformità allo standard è misurata e controllata con dati: controlli automatici riferiscono quale frazione dei repo corrisponde all'organizzazione, quanto i repo creati dai modelli si sono allontanati, la completezza dei README e le violazioni della direzione delle dipendenze, tutti seguiti rispetto a valori di riferimento; i tempi di inserimento e di navigazione sono misurati; le eccezioni sono registrate e riviste e le modifiche ai modelli sono approvate sulla base delle prove anziché delle opinioni.
- **Livello 5 (Orchestrazione):** la struttura è migliorata di continuo e adattiva: i miglioramenti ai modelli si propagano automaticamente ai repository esistenti, la governance della struttura è integrata con sicurezza, conformità e strumenti di piattaforma e lo standard evolve deliberatamente al mutare di linguaggi, architetture e portafoglio, mantenendo alta l'uniformità mentre l'organizzazione cambia attorno ad esso.

## Spunti di discussione

- Quali cartelle di primo livello dovrebbero essere davvero universali nella vostra organizzazione, e quali facoltative?
- Come impedite che i repository generati da un modello si allontanino da esso nel tempo?
- Dove passa la linea tra una gerarchia utile e a livelli e una cerimonia di cartelle sovra-ingegnerizzata?
- Come dovrebbe differire, se differisce, il vostro standard di struttura tra un approccio monorepo e uno multi-repo?
- Qual è il giusto processo di eccezione per un progetto le cui esigenze reali non rientrano nell'organizzazione standard?
- Quanta della vostra struttura può essere controllata automaticamente, e che cosa si affida ancora alla revisione umana?
- Chi possiede lo standard di struttura e i suoi modelli, e come vengono proposte e introdotte le modifiche?

## Punti chiave

- Organizza ogni repository in modo che qualsiasi ingegnere possa orientarsi in qualsiasi base di codice per aspettativa, seguendo il principio del minimo stupore.
- Adotta un'organizzazione coerente al livello più alto (sorgenti, test, docs, build, deploy, scripts, examples, specification) e fai del README il punto d'ingresso.
- Inserisci nel repository la configurazione di editor e strumenti (come `.editorconfig`) così che le convenzioni siano attive, non solo scritte.
- Fai rispettare la struttura con scheletri e modelli così che i nuovi repository siano corretti per impostazione predefinita.
- Su larga scala, il valore sta nell'uniformità: governa lo standard, gestisci la deriva e consenti deviazioni solo per eccezione documentata.

## Riferimenti e letture di approfondimento

- Robert C. Martin, *Clean Architecture: A Craftsman's Guide to Software Structure and Design*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Andrew Hunt e David Thomas, *The Pragmatic Programmer*
- Titus Winters, Tom Manshreck e Hyrum Wright (a cura di), *Software Engineering at Google*
- Scott Chacon e Ben Straub, *Pro Git*
- Documentazione del progetto EditorConfig (come standard di riferimento per la configurazione degli editor)
