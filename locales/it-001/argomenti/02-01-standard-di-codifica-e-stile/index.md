# 2.1 Standard di codifica e stile

## Panoramica e motivazioni

Gli standard di codifica sono le convenzioni condivise che permettono a molte persone di scrivere codice come se lo avesse scritto un solo autore attento. Coprono nomi, formattazione, organizzazione dei file, idiomi, gestione degli errori e i paradigmi che un team preferisce. In un piccolo team può prevalere il gusto individuale. In un grande team (centinaia o migliaia di ingegneri, molti collaboratori esterni, alto ricambio), l'incoerenza diventa una tassa che si paga a ogni lettura, a ogni revisione e a ogni inserimento. Gli standard trasformano innumerevoli piccole discussioni di stile in un'unica decisione che poi una macchina fa rispettare al posto tuo.

Per le grandi organizzazioni la posta è concreta. Il codice si legge molto più spesso di quanto si scriva. Nei contesti aziendali e governativi, una riga di codice può essere letta da auditor, revisori della sicurezza e manutentori anni dopo che il suo autore se n'è andato. Uno stile coerente abbassa il costo mentale di quella lettura, riduce la superficie in cui nascono i bug e rende affidabile l'analisi automatica tra i [linter](https://en.wikipedia.org/wiki/Lint_(software)) (strumenti che segnalano in automatico probabili bug e violazioni di stile), gli scanner di sicurezza e gli strumenti di [refactoring](https://en.wikipedia.org/wiki/Code_refactoring). Dove si applica una regolamentazione, come nei servizi finanziari, nella sanità, nella difesa e nei sistemi del settore pubblico, gli standard fanno parte anche dell'evidenza che una base di codice è manutenibile e controllata.

L'approccio moderno è trattare lo stile come una questione risolta e automatizzata anziché come materia di continuo giudizio umano. Formattatori e linter girano nell'editor, negli hook di pre-commit e nell'[integrazione continua](https://en.wikipedia.org/wiki/Continuous_integration) (CI), il processo automatico di build e test eseguito a ogni modifica. Sono le macchine a far rispettare lo stile, così che tu possa spendere l'attenzione della revisione su progetto e correttezza. L'obiettivo non è l'uniformità fine a se stessa. È la rimozione dell'attrito: dovresti poter passare tra servizi e team senza reimparare le basi.

## Principi chiave

- La coerenza batte la preferenza individuale; un unico stile concordato, applicato ovunque, vale più dello stile "migliore" applicato a macchia di leopardo.
- Automatizza l'applicazione. Formattatori e linter sono la fonte di verità, non i commenti di revisione sugli spazi.
- Ottimizza per il lettore e il manutentore, non per l'autore originale.
- Preferisci le convenzioni che la più ampia comunità del linguaggio già usa alle regole interne su misura.
- Rendi facile adottare lo standard: fornisci configurazioni condivise, modelli e strumenti anziché un PDF che nessuno legge.
- Le regole di stile dovrebbero essere poche, difendibili e inequivocabili; ogni regola ha un meccanismo di applicazione o è solo un suggerimento.
- I nomi sono la decisione di leggibilità con la leva più alta e meritano indicazioni esplicite.

## Raccomandazioni

### Adotta una guida di stile canonica per ogni linguaggio

Per ogni linguaggio che usi, adotta come base una guida di stile largamente riconosciuta (per esempio la guida della comunità o del fornitore per quel linguaggio) e documenta solo le differenze di cui la tua organizzazione ha bisogno. Non inventare uno stile interno da zero. Pubblica la tua scelta in un luogo centrale e reperibile e versionala come codice.

### Rendi i formattatori impostazioni predefinite non negoziabili

Usa un formattatore automatico con posizioni nette per ogni linguaggio che ne abbia uno, con un'unica configurazione condivisa inserita nel repository. La formattazione non dovrebbe mai comparire in revisione, perché viene applicata automaticamente al salvataggio e verificata nella CI. Dove un linguaggio manca di un formattatore solido, scegli un'unica configurazione del linter e trattala allo stesso modo.

### Esegui i linter come cancelli obbligatori, non come consigli

Configura i linter con un insieme di regole concordato, fai fallire la build in caso di violazioni e tieni l'insieme di regole nel [controllo di versione](https://en.wikipedia.org/wiki/Version_control), così che i cambiamenti passino per la revisione. Separa le regole correggibili in automatico (applicale in automatico) da quelle che richiedono giudizio umano (segnala e blocca). Introduci le nuove regole in modalità "avviso", smaltisci l'arretrato, poi promuovile a "errore".

### Applica a più livelli

Offri l'integrazione nell'editor per un feedback immediato, hook di pre-commit per l'applicazione locale e controlli di CI come cancello autorevole. Prima si coglie una violazione, meno costa. La CI deve essere l'ultima rete di protezione, perché gli hook locali possono essere aggirati.

### Dai ai nomi regole esplicite

Standardizza le convenzioni di maiuscole e minuscole per linguaggio, richiedi nomi che rivelino l'intenzione, vieta le abbreviazioni fuorvianti e definisci convenzioni per booleani, collezioni, unità e operazioni asincrone. Metti per iscritto il tuo vocabolario di dominio in un glossario condiviso, così che lo stesso concetto abbia lo stesso nome ovunque.

### Gestisci con deliberazione la coerenza tra linguaggi diversi

In una base di codice che copre più linguaggi, punta a concetti coerenti (schemi di gestione degli errori, struttura dei log, organizzazione dei progetti) anche dove la sintassi differisce. Fornisci configurazioni per linguaggio da un repository centrale, così che un nuovo servizio erediti automaticamente gli standard tramite modelli o scheletri.

### Codifica idiomi e paradigmi

Vai oltre la formattazione. Metti per iscritto gli idiomi preferiti, come gestire gli errori, come strutturare i moduli e quando usare eccezioni rispetto a tipi di risultato, insieme ai paradigmi che i tuoi team preferiscono. È qui che vivono leggibilità e manutenibilità vere.

## Compromessi: vantaggi e svantaggi

| Approccio | Vantaggi | Svantaggi |
|---|---|---|
| Formattatore automatico rigido, zero configurazione | Chiude ogni dibattito sulla formattazione; coerenza immediata; inserimento banale | Alcune scelte sgradite non sono negoziabili; grande differenza iniziale alla prima applicazione |
| Linter configurabile con regole interne | Su misura per l'organizzazione; può codificare vere regole di prevenzione dei bug | Deriva delle configurazioni; discussioni sulle minuzie; onere di manutenzione |
| Standard della comunità adottato in blocco | Familiare ai nuovi assunti; ecosistema di strumenti solido; poca manutenzione | Può non adattarsi a vincoli specifici; qualche regola scomoda |
| Standard interno su misura | Si adatta esattamente all'organizzazione | Costoso da scrivere e mantenere; sconosciuto ai nuovi assunti; strumenti deboli |
| Autonomia per team | Morale locale alto; specifico al contesto | Frammentazione; mobilità tra team dolorosa; strumenti incoerenti |

Le impostazioni predefinite fatte rispettare scambiano un po' di autonomia individuale con grandi guadagni collettivi: meno attrito in revisione, inserimento più rapido e automazione affidabile. Il rischio principale è sovraccaricare lo standard con centinaia di regole che rallentano tutti senza prevenire difetti reali. Mantieni l'insieme di regole piccolo e basato sulle prove e propendi per adottare uno standard esistente, così che la manutenzione resti economica.

## Domande da discutere con il tuo team

1. **Quali regole del linter dovrebbero far fallire la build, e come si promuove una regola da avviso a errore senza bloccare tutti?** Questo capitolo sostiene che ogni regola abbia bisogno di un meccanismo di applicazione e che le nuove regole debbano entrare in modalità avviso, farsi smaltire l'arretrato, poi passare a errore. In un grande team, portare a errore una regola su una base di codice sporca blocca da un giorno all'altro centinaia di modifiche non correlate. Porta alla riunione prove concrete: il numero attuale di violazioni per ogni regola candidata e se è correggibile in automatico o richiede giudizio umano. Nei contesti aziendali e governativi la linea tra superato e fallito alimenta anche i cancelli di audit, quindi un insieme di regole ambiguo indebolisce la tua storia di conformità. Decidi un'introduzione graduale: correggi in automatico ciò che puoi, metti a bilancio la pulizia, poi imponi il cancello.

2. **Quando applicherete per la prima volta un formattatore al codice legacy, come eviterete che quella riformattazione rovini git blame e sommerga le revisioni?** La tabella dei compromessi avverte di una grande differenza iniziale, e la sezione sugli antipattern segnala il mescolare commit di riformattazione con modifiche di logica. Una singola riformattazione generale riscrive migliaia di righe e fa puntare blame alla riformattazione anziché al vero autore, il che danneggia chiunque faccia debug anni dopo. Esegui la riformattazione come un unico commit isolato e chiaramente etichettato e registralo in un file di esclusione di blame, così che la storia resti utile. Per gli auditor che tracciano chi ha cambiato che cosa, quell'isolamento è la differenza tra evidenza pulita e rumore. Concorda la sequenza prima di toccare il codice, non dopo.

3. **Chi possiede il vostro glossario dei nomi e il vocabolario di dominio, e come viene aggiunto un nuovo termine?** Il capitolo chiama i nomi la decisione di leggibilità con la leva più alta e chiede di scrivere il vocabolario di dominio in un glossario condiviso. Senza un responsabile nominato, lo stesso concetto assume tre nomi diversi tra i team, e gli strumenti di analisi statica e di ricerca perdono affidabilità. Porta come segnale concreto esempi di concetti che hanno già nomi in conflitto nella tua base di codice. Assegna un responsabile e un percorso di proposta leggero, così che aggiungere o rinominare un termine sia una piccola modifica rivista anziché una discussione in ogni pull request. La risposta cambia l'inserimento: un nuovo assunto legge un solo glossario anziché ricostruire l'intento da codice incoerente.

4. **Per ogni linguaggio, adottate in blocco una guida di stile riconosciuta della comunità o del fornitore, e dove le differenze interne sono davvero giustificate?** Questo capitolo sostiene che dovresti prendere uno standard esistente come base e documentare solo le differenze di cui la tua organizzazione ha bisogno, perché uno standard su misura è costoso da scrivere e sconosciuto ai nuovi assunti. La spinta contraria è reale: un vincolo interno (una regola di sicurezza, un framework legacy, un mandato di accessibilità) a volte è davvero in conflitto con l'impostazione predefinita della comunità, e ogni differenza che tieni è una regola di cui ora sei proprietario e che mantieni per sempre. Porta alla riunione l'elenco delle differenze proposte, ciascuna con il vincolo concreto che la motiva, e sii pronto a tagliare qualsiasi differenza che sia solo gusto. Nei contesti aziendali e governativi, una base che corrisponde alla più ampia comunità del linguaggio significa anche che collaboratori esterni e nuovi fornitori arrivano già fluenti, il che accorcia l'inserimento e rafforza l'evidenza di manutenibilità che gli auditor cercano.

5. **In una base di codice poliglotta, quali convenzioni sono davvero universali e quali restano locali al linguaggio, e come impedite che le configurazioni per repository divergano?** Il capitolo chiede concetti coerenti (gestione degli errori, struttura dei log, organizzazione dei progetti) tra linguaggi anche dove la sintassi differisce, e configurazioni per linguaggio servite da un repository centrale perché i nuovi servizi ereditino automaticamente gli standard. La tensione è che imporre gli idiomi di un linguaggio a un altro produce codice goffo e non idiomatico, mentre lasciare che ogni team biforchi la propria configurazione finisce per far significare "lo standard" nulla. Porta come segnale concreto un inventario delle attuali configurazioni di linter e formattatore per repository e un confronto che mostri quanto già divergono. Per una grande organizzazione con decine di servizi, decidi il meccanismo di distribuzione (modelli, scheletri, un pacchetto di configurazione condiviso) così che una modifica di regola si propaghi una volta anziché essere copiata a mano in ogni repository.

6. **Quando è legittimo disattivare una regola, chi rivede la deroga e come impedite che disattivazioni generalizzate svuotino lo standard?** La sezione sugli antipattern segnala le deroghe inline diffuse come segno di una regola sbagliata o di un team che ha rinunciato, eppure una politica rigida senza eccezioni spinge le persone a scrivere codice peggiore solo per soddisfare il linter. Concorda un percorso leggero: una deroga deve portare una motivazione, stare nell'ambito più stretto possibile ed essere visibile in revisione anziché sepolta in un file di esclusione globale. Porta il numero attuale di deroghe per regola e per repository, perché una regola derogata centinaia di volte sta dicendo qualcosa sulla regola, non sul codice. Nel lavoro regolamentato e pubblico, deroghe generalizzate non spiegate indeboliscono direttamente la storia di audit, perché la pipeline non può più mostrare che il codice integrato abbia davvero superato i cancelli concordati.

## Lente settoriale

**Startup.** Vince la velocità, quindi adotta fin dal primo giorno le impostazioni predefinite del formattatore e del linter della comunità per il tuo unico linguaggio e collegale a un hook di pre-commit e alla CI prima che arrivi il secondo ingegnere. Non scrivere uno stile interno che non hai tempo di mantenere: la configurazione fornita nel repository è l'intero standard. Quando aggiungi un secondo linguaggio, ricorri alla guida canonica di quel linguaggio anziché inventare convenzioni da zero.

**Piccola impresa.** Senza uno specialista di strumenti dedicato e con un budget ridotto, appoggiati interamente al formattatore gratuito e con posizioni nette fornito con il tuo linguaggio o accanto a esso e accetta le sue impostazioni predefinite anziché regolarle. È un chiaro caso di comprare anziché costruire: mantenere un insieme di regole su misura costa tempo che non hai, mentre un formattatore già pronto non costa nulla e chiude subito il dibattito sullo stile. Tieni la configurazione nel repository, così che l'unico collaboratore esterno che assumerai l'anno prossimo la erediti senza una conversazione.

**Grande impresa.** Su larga scala il compito è la governance tra molti team: un repository centrale di standard ingegneristici con le configurazioni condivise di formattatore e linter per linguaggio, nuovi servizi generati da modelli che ne importano le configurazioni e cancelli di CI che bloccano le integrazioni non conformi. Versiona l'insieme di regole come codice e instrada le modifiche attraverso una revisione periodica, così che gli standard evolvano deliberatamente anziché derivare. Il ritorno è che gli ingegneri che passano tra team trovano codice familiare, e che gli strumenti automatici producono un segnale affidabile perché ogni repository è coerente.

**Ente pubblico.** Appalti e responsabilità plasmano la scelta: imponi uno specifico insieme di regole di stile e sicurezza come parte dei requisiti di autorizzazione all'esercizio e fai emettere alla pipeline un rapporto che mostri che ogni modifica integrata ha superato i cancelli concordati come evidenza di audit. Poiché un formattatore viene applicato automaticamente, il codice di più fornitori e collaboratori esterni appare coerente, il che protegge il lavoro di manutenzione pubblica ben oltre la fine dei contratti. Privilegia basi della comunità riconosciute rispetto a regole su misura, così che lo standard sia trasparente e qualsiasi futuro fornitore possa adottarlo senza dipendenza da soluzioni proprietarie.

## Esempi

**Startup.** Una startup di quattro persone adotta fin dal primo giorno le impostazioni predefinite del formattatore e del linter della comunità per il suo unico linguaggio, collegandole a un hook di pre-commit e alla CI, così che nessuno discuta di spazi in revisione. Poiché la configurazione sta dentro il repository, il quinto e il sesto assunto la ereditano automaticamente e non vedono mai un commento sulla formattazione. Quando in seguito il team aggiunge un secondo linguaggio, ricorre alla guida standard di quel linguaggio anziché inventare uno stile interno che non ha tempo di mantenere.

**Grande impresa.** Una grande banca gestisce servizi in Java, Python e TypeScript su decine di team. Pubblica un repository centrale di "standard ingegneristici" che contiene le configurazioni condivise di formattatore e linter per ogni linguaggio. I nuovi servizi sono generati da un modello che ne importa le configurazioni, così che ogni repository nasca conforme. La CI blocca le integrazioni a qualsiasi violazione e una revisione trimestrale governa le modifiche alle regole. Il tempo di inserimento degli ingegneri che passano da un team all'altro scende in modo percepibile, perché ogni repository appare familiare.

**Ente pubblico.** Un'agenzia del settore pubblico che modernizza un sistema legacy impone un insieme di regole di linting per accessibilità e sicurezza come parte dei requisiti di autorizzazione all'esercizio (ATO, authority to operate), l'approvazione formale necessaria per far funzionare il sistema in produzione. La conformità di stile diventa parte dell'evidenza di audit: la pipeline produce un rapporto che mostra che tutto il codice integrato ha superato i cancelli di [analisi statica](https://en.wikipedia.org/wiki/Static_program_analysis) concordati. Poiché un formattatore viene applicato automaticamente, i collaboratori esterni di più fornitori producono codice visivamente coerente, il che rende più facile il lavoro di manutenzione a lungo termine del governo dopo la fine dei contratti.

## Business case: motivazioni, ROI e TCO

Il costo di adozione degli standard è per lo più una tantum: scegliere le guide, collegare gli strumenti e applicare un grande commit iniziale di riformattazione. Il costo ricorrente è basso, perché l'applicazione è automatizzata. Il costo del *non* adottare standard è ricorrente e cumulativo: ogni revisione spende minuti sullo stile, ogni inserimento è più lento, gli strumenti di analisi statica producono rumore e il codice incoerente nasconde bug. In una grande organizzazione, quei minuti si sommano in perdite equivalenti a tempo pieno.

Il ritorno si vede in una latenza di revisione ridotta, meno commenti di revisione sullo stile, inserimento più rapido e un segnale più alto dagli strumenti automatici. Negli ambienti regolamentati c'è un ulteriore ritorno nella prontezza all'audit: controlli dimostrabili e fatti rispettare riducono lo sforzo e il rischio delle revisioni di conformità. Per sostenere il caso con la leadership, presenta gli standard come una leva economica e ad alto effetto sulla produttività degli sviluppatori e sulla postura di audit, e dai un numero al costo attuale dell'incoerenza usando l'analisi dei commenti di revisione e i dati dei sondaggi sull'inserimento.

## Antipattern e insidie

- **Stile discusso in revisione del codice:** il segno che l'applicazione non è automatizzata; sposta la regola negli strumenti.
- **Il documento di standard che nessuno legge:** una pagina di wiki senza applicazione è decorazione; ogni regola ha bisogno di un meccanismo.
- **Proliferazione di regole:** centinaia di regole pedanti che rallentano il lavoro senza prevenire difetti.
- **Deriva delle configurazioni:** ogni repository biforca la propria configurazione del linter finché "lo standard" non significa nulla.
- **Formattare l'intero repository nel mezzo del lavoro su una funzionalità:** mescolare commit di riformattazione con modifiche di logica distrugge revisione e blame; esegui le grandi riformattazioni in commit isolati e chiaramente etichettati.
- **Ignorare il linter con deroghe generalizzate:** disattivazioni inline diffuse segnalano una regola sbagliata o un team che ha rinunciato.
- **Standard senza responsabilità:** l'assenza di un responsabile chiaro significa che le regole non evolvono mai e marciscono.

## Modello di maturità

- **Livello 1, Avvio:** lo stile è per singolo autore e reattivo; nessuna configurazione condivisa; la formattazione è discussa in revisione e decisa da chi ci tiene di più quel giorno.
- **Livello 2, Sviluppo:** i singoli team adottano un formattatore e un linter, ma configurazioni e insiemi di regole variano da team a team e da repository a repository, quindi la coerenza si ferma al confine di ogni team.
- **Livello 3, Standardizzazione:** configurazioni centrali condivise per linguaggio sono documentate e fatte rispettare in tutta l'organizzazione; la CI blocca le integrazioni non conformi; i nuovi repository ereditano automaticamente gli standard tramite modelli o scheletri.
- **Livello 4, Gestione:** lo standard è misurato e controllato con dati: tassi di violazione, numero di deroghe, commenti di revisione sullo stile e tempo di inserimento sono seguiti rispetto a valori di riferimento, e le modifiche alle regole sono promosse o ritirate sulla base di quelle prove anziché delle opinioni.
- **Livello 5, Orchestrazione:** gli standard sono migliorati di continuo e integrati in tutta l'organizzazione; gli idiomi poliglotti e il vocabolario di dominio sono documentati e fatti rispettare, l'applicazione è quasi priva di attrito e l'insieme di regole si adatta al mutare di linguaggi, strumenti ed esigenze dell'organizzazione.

## Spunti di discussione

- Dove passa la linea tra una regola fatta rispettare e una linea guida documentata che si fida del giudizio dell'ingegnere?
- Come dovrebbe l'organizzazione gestire una regola amata della comunità che è in conflitto con un vero vincolo interno?
- Chi possiede gli standard, e come vengono proposte, discusse e introdotte le modifiche alle regole senza creare disagi?
- In una base di codice poliglotta, quali convenzioni dovrebbero essere davvero universali e quali dovrebbero restare locali al linguaggio?
- Come si adottano gli standard su una grande base di codice legacy senza una riformattazione dirompente tutta in una volta?
- Quale ruolo dovrebbero avere gli strumenti assistiti dall'IA nel suggerire o far rispettare idiomi oltre la formattazione meccanica?

## Punti chiave

- Tratta lo stile come un problema automatizzato e risolto, così che le persone rivedano progetto e correttezza.
- Adotta standard esistenti della comunità e documenta solo le differenze.
- Applica a livello di editor, pre-commit e CI, con la CI come cancello autorevole.
- Mantieni l'insieme di regole piccolo, difendibile e governato centralmente.
- Nomi e idiomi, non gli spazi, sono dove si vince davvero la leggibilità.

## Riferimenti e letture di approfondimento

- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt e David Thomas, *The Pragmatic Programmer*
- Steve McConnell, *Code Complete*
- Dustin Boswell e Trevor Foucher, *The Art of Readable Code*
- Kevlin Henney (a cura di), *97 Things Every Programmer Should Know*
- Google, *Google Engineering Practices* e guide di stile dei linguaggi (come esempi di riferimento)
