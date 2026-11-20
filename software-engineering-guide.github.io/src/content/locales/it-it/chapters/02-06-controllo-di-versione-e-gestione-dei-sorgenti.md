# 2.6 Controllo di versione e gestione dei sorgenti

## Panoramica e motivazioni

Pensa al [controllo di versione](https://en.wikipedia.org/wiki/Version_control) come al sistema di registrazione della tua base di codice. Cattura ogni modifica, compreso chi l'ha fatta, quando e perché, e permette a molte persone di lavorare sullo stesso software senza sovrascriversi a vicenda. Per una grande organizzazione è molto più di un backup. È il fondamento su cui poggiano collaborazione, [integrazione continua](https://en.wikipedia.org/wiki/Continuous_integration) (CI), audit e gestione dei rilasci. Le scelte che fai su rami, struttura dei repository e disciplina dei commit plasmano quanto in fretta il tuo team può muoversi, e con quanta sicurezza.

Per i grandi team, la gestione dei sorgenti è in realtà un problema di coordinamento su larga scala. Quando centinaia di ingegneri inviano modifiche a codice condiviso, hanno bisogno di una strategia che mantenga piccole le integrazioni, mantenga rilasciabile il ramo principale e mantenga leggibile la storia. Un team che integra di continuo scorre in modo fluido. Un team che lascia divergere i rami per settimane barcolla da una crisi di integrazione all'altra. La struttura del tuo repository, uno grande o molti, plasma anche il modo in cui i team condividono il codice e si coordinano.

I contesti aziendali e governativi aggiungono altre esigenze: tracciabilità, controllo degli accessi e conservazione. Una modifica può dover essere collegata a un elemento di lavoro approvato per l'audit. I segreti non devono mai entrare nella storia. L'accesso ai repository deve rispettare i confini di sicurezza. Qui le tue pratiche di controllo di versione diventano parte del quadro di controllo dell'organizzazione, e un errore come un segreto trapelato o una storia non verificabile può avere conseguenze serie.

## Principi chiave

- Integra spesso modifiche piccole; la lunga divergenza è la radice del dolore delle integrazioni.
- Mantieni il ramo principale sempre rilasciabile.
- La storia è documentazione; scrivi i commit per il futuro lettore che dovrà capire perché.
- Non committare mai segreti; tratta qualsiasi segreto che raggiunge la storia come compromesso.
- Automatizza l'applicazione dell'igiene (hook, controlli di CI) anziché affidarti alla sola disciplina.
- Scegli la struttura del repository (mono o poli) in base a come i team condividono davvero il codice e si coordinano, non alla moda.
- Collega le modifiche alla loro motivazione (elementi di lavoro, ticket o decisioni) per la tracciabilità.

## Raccomandazioni

### Preferisci lo sviluppo basato sul trunk con rami di breve durata

Propendi per lo [sviluppo basato sul trunk](https://en.wikipedia.org/wiki/Trunk-based_development): integra spesso in un ramo principale condiviso, usando rami di funzionalità di breve durata misurati in ore o giorni, non settimane. I rami brevi mantengono piccole le integrazioni e continua l'integrazione, e quell'abitudine è fortemente associata a un'alta prestazione di consegna. Quando il lavoro non è ancora finito, non parcheggiarlo su un ramo di lunga durata. Usa i [feature flag](https://en.wikipedia.org/wiki/Feature_toggle), interruttori a runtime che nascondono il lavoro incompleto, così da integrarlo in sicurezza. Riserva i rami di rilascio di lunga durata al vero supporto multi-versione e affrontali sapendo il costo di manutenzione che portano.

### Scegli un modello di ramificazione adatto alla cadenza dei rilasci

Adegua il tuo [modello di ramificazione](https://en.wikipedia.org/wiki/Branching_(version_control)) al modo in cui rilasci davvero. Se rilasci in continuo, lo sviluppo basato sul trunk con ramificazione minima ti serve bene. Se consegni rilasci versionati ai clienti, o supporti più versioni vive insieme, potresti aver bisogno di rami di rilascio e retroportazioni. Stai alla larga dai modelli pesanti con molti rami di lunga durata a meno che il tuo modello di rilascio non li richieda davvero, perché moltiplicano l'onere di integrazione e manutenzione.

### Decidi con deliberazione tra monorepo e polirepo

Ricorri a un [monorepo](https://en.wikipedia.org/wiki/Monorepo), un unico repository che contiene molti progetti, quando i team condividono molto codice, hanno bisogno di modifiche atomiche tra progetti e vogliono strumenti e visibilità unificati. In cambio, accetti la necessità di strumenti di build e controlli di accesso scalati. Ricorri ai polirepo, repository separati per progetto o servizio, quando team e servizi sono davvero indipendenti, vogliono accessi e cicli di rilascio isolati e non hanno bisogno di modifiche atomiche tra repository. In cambio, accetti il costo di coordinare modifiche che attraversano più repository. Entrambi funzionano su larga scala. È la scelta sbagliata per il tuo schema di accoppiamento a creare un attrito costante.

### Fai rispettare l'igiene dei commit e i conventional commit

Chiedi messaggi di commit che spieghino perché una modifica è stata fatta, non solo che cosa. Adotta una convenzione come i conventional commit, così che i messaggi siano strutturati e interpretabili da una macchina, il che permette di automatizzare registri delle modifiche e versionamento. Mantieni atomici i commit, una modifica logica ciascuno, così che la storia resti bisecabile e facile da annullare. Lascia che hook e controlli di CI facciano rispettare il formato dei messaggi e l'igiene di base, anziché affidarti alla memoria.

### Tieni i binari di grandi dimensioni e il codice generato fuori dalla storia ordinaria

Non committare grandi risorse binarie direttamente nella storia principale, perché gonfiano per sempre ogni clone. Usa invece un meccanismo di archiviazione di file grandi o un repository di artefatti. Come regola, evita di committare anche il codice generato; generalo nella build. Quando devi davvero committare un artefatto generato, isolalo e marcalo chiaramente, così che non inquini revisioni e differenze.

### Impedisci che i segreti entrino mai nel repository

Metti la scansione automatica dei segreti negli hook di pre-commit e nella CI, così che le credenziali vengano bloccate prima ancora di arrivare. Dai agli ingegneri un vero sistema di gestione dei segreti, così che non abbiano mai bisogno di codificare una credenziale nel codice. E tratta qualsiasi segreto che raggiunge la storia come compromesso: ruotalo subito. Una volta che un segreto è stato inviato e clonato, rimuoverlo dalla storia è difficile e inaffidabile.

### Stabilisci controllo degli accessi e tracciabilità

Imposta l'accesso ai repository in modo che rispetti i confini di sicurezza e il [minimo privilegio](https://en.wikipedia.org/wiki/Principle_of_least_privilege). Collega commit o pull request agli elementi di lavoro, così che ogni modifica sia riconducibile alla sua motivazione, il che aiuta sia il contesto ingegneristico quotidiano sia l'audit. Proteggi i tuoi rami chiave con controlli e revisioni obbligatori, così che nulla venga integrato senza superare i cancelli concordati.

## Compromessi: vantaggi e svantaggi

| Scelta | Vantaggi | Svantaggi |
|---|---|---|
| Sviluppo basato sul trunk | Integrazione continua; integrazioni piccole; alto flusso | Richiede feature flag e disciplina; meno isolamento |
| Rami di funzionalità di lunga durata | Forte isolamento del lavoro in corso | Integrazioni dolorose; integrazione ritardata; deriva |
| Monorepo | Modifiche atomiche tra progetti; strumenti condivisi; visibilità | Richiede strumenti di build scalati; controllo di accesso grossolano di default |
| Polirepo | Rilasci indipendenti; accesso isolato; strumenti semplici per repository | Modifiche tra repository difficili; onere di coordinamento delle versioni |
| Conventional commit | Registri delle modifiche e versionamento automatici; storia coerente | Convenzione iniziale; serve applicazione |

Il grande compromesso qui è tra frequenza di integrazione e isolamento. I rami di lunga durata sembrano più sicuri perché il tuo lavoro sta in disparte, ma proprio quell'isolamento causa le integrazioni costose e le sorprese di integrazione più avanti. Lo sviluppo basato sul trunk rinuncia a quella sensazione di isolamento in cambio di un'integrazione continua ed economica, e ti chiede di portare feature flag e disciplina. La decisione monorepo/polirepo scambia facilità tra progetti con indipendenza dei team. Scegli quella che corrisponde a quanto strettamente accoppiato è davvero il tuo codice.

## Domande da discutere con il tuo team

1. **Quali controlli devono essere superati prima che qualcosa venga integrato nel vostro ramo principale protetto, e quel ramo è davvero sempre rilasciabile?** Questo capitolo tratta un ramo principale rilasciabile come principio centrale e chiama antipattern un ramo principale non protetto, in cui codice rotto o non rivisto raggiunge il ramo da cui tutti dipendono. In un grande team un ramo principale rosso blocca tutti insieme, quindi il cancello che richiedi è una proprietà di sicurezza condivisa, non personale. Porta le prove: che cosa la protezione dei rami fa rispettare davvero oggi e quanto spesso il ramo principale è attualmente rotto. Decidi l'insieme richiesto, test superati, scansioni di sicurezza e revisione, e rendi il ramo principale rilasciabile per policy anziché per speranza. Quel cancello è ciò che permette a molte persone di integrare di continuo senza timore.

2. **Vale la pena adottare i conventional commit per l'onere di convenzione per il vostro team, dato ciò che automatizzano?** Il capitolo raccomanda messaggi di commit strutturati e interpretabili da una macchina proprio perché permettono di automatizzare registri delle modifiche e versionamento, e chiede commit atomici così che la storia resti bisecabile e annullabile. Il compromesso è reale: paghi una convenzione iniziale e serve applicazione, in cambio di note di rilascio generate e storia affidabile. Porta il segnale di che cosa fai oggi a mano, come scrivere registri delle modifiche o cercare quale commit abbia introdotto una regressione. Se rilasci spesso o mantieni più versioni, l'automazione di solito si ripaga; se tagli raramente rilasci, una convenzione più leggera può bastare. Lascia che hook e CI facciano rispettare il formato, così che non dipenda dalla memoria.

3. **Avete accettato il costo operativo che la vostra struttura di repository richiede, che sia gli strumenti di un monorepo o il coordinamento tra repository?** Questo capitolo dice che sia il monorepo sia il polirepo funzionano su larga scala e che è la scelta sbagliata per il tuo schema di accoppiamento a creare un attrito costante. Un monorepo richiede strumenti di build scalati e un controllo di accesso più fine, mentre i polirepo fanno di qualsiasi modifica che attraversi repository un progetto di coordinamento con rischio di sfasamento delle versioni. Porta il segnale concreto: quanto spesso le tue modifiche attraversano i confini dei progetti e se i tuoi strumenti di build e di accesso possono sostenere la struttura che hai. Se le modifiche atomiche tra progetti sono comuni, investi negli strumenti da monorepo; se team e servizi sono davvero indipendenti, accetta con deliberazione il costo di coordinamento tra repository. Il punto è adeguare la struttura a quanto strettamente accoppiato è davvero il tuo codice, poi finanziare gli strumenti che quella struttura richiede.

4. **Se una credenziale attiva fosse committata ora in un repository molto frequentato, quanto in fretta la rilevereste, e la rotazione è davvero automatica anziché una speranza?** Questo capitolo tratta qualsiasi segreto che raggiunge la storia come compromesso e avverte che rimuoverlo in seguito è difficile e inaffidabile, quindi prevenzione e rotazione rapida sono le uniche vere difese. Per un grande team l'esposizione si cumula: un segreto inviato a un repository condiviso viene clonato su decine di macchine e replicato nelle cache della CI in pochi minuti, quindi una risposta umana lenta garantisce una violazione. La considerazione contraria è l'attrito: una scansione aggressiva in pre-commit e una rotazione forzata rallentano le persone e producono falsi positivi, quindi devi regolare i controlli anziché spegnerli. Porta le prove: se la scansione dei segreti gira sia negli hook di pre-commit sia nella CI, il tuo tempo medio per rilevare e ruotare una fuga nota e se gli ingegneri dispongano almeno di un sistema di gestione dei segreti che elimini la tentazione di codificarli nel codice. Nei contesti aziendali e governativi, collega questo al tuo processo di gestione degli incidenti e alle regole di conservazione, perché una credenziale trapelata in una storia verificabile è sia un evento di sicurezza sia di conformità, e il regolatore chiederà chi sapeva e con quanta rapidità ha agito.

5. **I vostri rami sono davvero di breve durata, e dove non lo sono, perché il lavoro incompleto viene parcheggiato su un ramo anziché nascosto dietro un feature flag?** Il capitolo propende con decisione per lo sviluppo basato sul trunk perché la lunga divergenza è la radice del dolore delle integrazioni, e offre i feature flag come meccanismo che permette di integrare in sicurezza il lavoro incompleto anziché isolarlo per settimane. In un grande team questa è una proprietà di coordinamento, non una preferenza personale: ogni ramo che vive per settimane diventa una biforcazione privata della realtà che qualcuno dovrà alla fine riconciliare, e il costo di quella riconciliazione cresce con l'organico. La considerazione contraria è che i feature flag portano un proprio costo, tra cui complessità a runtime, test delle combinazioni e flag obsoleti da ritirare. Porta i dati: la tua distribuzione reale della durata dei rami, quanto spesso l'integrazione produce conflitti o sorprese e quanti rami di lunga durata esistono ora e perché. Per un'organizzazione grande o regolamentata, aggiungi il quadro dei rilasci, poiché un vero supporto multi-versione può giustificare rami di rilascio di lunga durata con una retroportazione disciplinata, e questa è una decisione diversa dal parcheggiare lontano dal ramo principale il lavoro quotidiano sulle funzionalità.

6. **Ogni modifica della vostra storia è riconducibile al suo autore e alla sua motivazione entro i giusti confini di sicurezza, e reggerebbe a un audit?** Questo capitolo tratta controllo degli accessi, minimo privilegio e collegamento delle modifiche agli elementi di lavoro come parte del quadro di controllo dell'organizzazione, non come finitura facoltativa. Per un grande team, la tracciabilità è ciò che trasforma un flusso opaco di commit in qualcosa su cui si può ragionare durante un incidente o una revisione di conformità, e i confini di accesso sono ciò che impedisce a un singolo account compromesso di raggiungere codice che non dovrebbe mai toccare. La considerazione contraria è la velocità degli sviluppatori: collegamenti obbligatori agli elementi di lavoro, permessi granulari e revisioni obbligatorie aggiungono cerimonia che un piccolo team veloce potrebbe ragionevolmente saltare. Porta le prove: se i rami protetti richiedono davvero i controlli e le revisioni che dichiari, se i commit fanno riferimento davvero a elementi di lavoro approvati e come l'accesso si mappa oggi sui tuoi veri confini di sicurezza. Nei contesti aziendali e governativi, collega questo a classificazione, conservazione e obblighi di audit, perché una storia non verificabile o una concessione di accesso troppo ampia diventa un rilievo che può fermare un programma o far fallire un accreditamento.

## Lente settoriale

**Startup.** Vincono velocità e sopravvivenza. Usa un solo repository, lavora basandoti sul trunk, integra rami di breve durata più volte al giorno e nascondi il lavoro incompleto dietro semplici feature flag anziché rami lunghi. Attiva la scansione dei segreti fin dal primo commit, perché una chiave trapelata in un repository pubblico può affondare un'azienda senza un team di sicurezza che la contenga. Salta modelli di ramificazione elaborati e processi pesanti; un ramo principale protetto e messaggi di commit significativi sono disciplina sufficiente per muoversi in fretta.

**Piccola impresa.** Senza uno specialista di piattaforma o DevOps dedicato e con un budget ridotto, compra le impostazioni predefinite gestite anziché costruirle. Un fornitore di Git ospitato ti dà protezione dei rami, revisioni obbligatorie e scansione dei segreti di serie, quindi appoggiati a quelli anziché ospitare in proprio un server che non sai mantenere. Imposta la decisione come igiene dei dati: sappi quali repository contengono configurazione sensibile, tieni le credenziali nel gestore di segreti del fornitore e lascia che sia la piattaforma a far rispettare le poche regole di cui hai davvero bisogno.

**Grande impresa.** Il problema difficile è la coerenza tra molti team. Standardizza protezione dei rami, convenzioni dei commit e scansione dei segreti come politica dell'intera organizzazione, così che i gruppi smettano di reinventarle, e fai con deliberazione la scelta tra monorepo e polirepo per ogni schema di accoppiamento, finanziando gli strumenti di build scalati o il coordinamento tra repository che richiede. Instrada le modifiche ai revisori giusti con regole di titolarità del codice, collega i commit agli elementi di lavoro per la tracciabilità e tratta l'igiene del controllo di versione come un controllo governato con responsabili e metriche anziché una questione di abitudine individuale.

**Ente pubblico.** Regole sugli appalti, trasparenza e responsabilità pubblica plasmano l'intera impostazione. Richiedi che ogni commit faccia riferimento a un elemento di lavoro approvato, controlla l'accesso per confine di classificazione e rendi obbligatorie la scansione dei segreti e la rotazione immediata sotto un processo di incidente documentato. Supporta più versioni in esercizio con rami di rilascio di lunga durata e retroportazione disciplinata dove le sedi non possono aggiornare tutte insieme, e mantieni verificabile e conservata la storia, così che richieste di accreditamento, accesso agli atti e vigilanza possano ricevere risposta senza affannarsi.

## Esempi

**Startup.** Una startup di tre persone lavora basandosi sul trunk per abitudine e necessità, integrando rami di breve durata nel principale più volte al giorno e nascondendo le funzionalità a metà dietro semplici flag. Attivano la scansione dei segreti nella CI dal primo commit, perché una chiave API trapelata in un repository pubblico potrebbe affondare un'azienda che non ha un team di sicurezza per contenere le conseguenze. Un repository, un ramo principale protetto e messaggi di commit significativi danno loro disciplina sufficiente per muoversi in fretta senza inciampare nella propria storia.

**Grande impresa.** Una grande società tecnologica gestisce un monorepo con centinaia di servizi e librerie condivise. Strumenti di build scalati e regole di titolarità del codice instradano ogni modifica ai revisori giusti. Un singolo commit può aggiornare atomicamente una libreria condivisa e ogni consumatore insieme, evitando i problemi di sfasamento delle versioni che affliggono i repository distribuiti. Lo sviluppo basato sul trunk con feature flag mantiene rilasciabile il ramo principale e la scansione dei segreti blocca le credenziali al momento del commit in tutto il repository.

**Ente pubblico.** Un fornitore nazionale della difesa si attiene a una rigorosa tracciabilità. Ogni commit deve fare riferimento a un elemento di lavoro approvato. La protezione dei rami richiede scansioni di sicurezza superate e una revisione indipendente, e l'accesso è strettamente controllato per confine di classificazione. La scansione dei segreti è obbligatoria e qualsiasi credenziale esposta innesca la rotazione immediata sotto un processo di incidente. Rami di rilascio di lunga durata supportano più versioni in esercizio in sedi che non possono aggiornare tutte insieme, con retroportazione disciplinata delle correzioni di sicurezza.

## Business case: motivazioni, ROI e TCO

Una buona gestione dei sorgenti è quasi gratuita da adottare e costosa da non avere. Lo sviluppo basato sul trunk e l'integrazione continua sono tra le pratiche più fortemente associate a un'alta prestazione di consegna del software, che a sua volta correla con migliori risultati organizzativi. Una storia pulita e tracciabile riduce il tempo necessario per diagnosticare incidenti e soddisfare gli audit, e una ramificazione disciplinata ti risparmia il costo ricorrente e non a bilancio di crisi di integrazione e maratone di integrazione.

Il rischio più sbilanciato sono i segreti nel controllo di versione. Una singola credenziale trapelata può causare una violazione il cui costo supera di gran lunga qualsiasi investimento in strumenti, e la storia fa sì che tali fughe restino. Prevenirle è economico; ripulire dopo non lo è. Scelte di struttura scadenti si manifestano come attrito cronico: ogni modifica tra repository diventa un progetto di coordinamento, o ogni build del monorepo diventa un collo di bottiglia. Per sostenere il caso con la leadership, collega la tua strategia di ramificazione alle metriche di consegna e al tempo di diagnosi degli incidenti e presenta scansione dei segreti e controllo degli accessi come controlli a basso costo contro rischi di violazione e di audit ad alto costo.

## Antipattern e insidie

- **Rami divergenti di lunga durata:** settimane di lavoro isolato che confluiscono in eventi di integrazione dolorosi e rischiosi.
- **Segreti nella storia:** credenziali codificate nel codice che persistono per sempre nei cloni e richiedono rotazione una volta esposte.
- **Committare grandi binari nella storia principale:** gonfia per sempre ogni clone e rallenta tutte le operazioni.
- **Messaggi di commit privi di significato:** "fix", "wip", "changes" che distruggono il valore della storia come documentazione.
- **Committare codice generato come se fosse scritto a mano:** differenze rumorose, conflitti di integrazione e confusione sulla fonte di verità.
- **Struttura di repository sbagliata per l'accoppiamento:** polirepo per codice strettamente accoppiato, o monorepo senza strumenti scalati.
- **Ramo principale non protetto:** nessun controllo obbligatorio, così che codice rotto o non rivisto raggiunge il ramo da cui tutti dipendono.

## Modello di maturità

- **Livello 1, Avvio:** ad hoc e reattivo. La ramificazione è improvvisata, i rami vivono per settimane, i messaggi di commit dicono "fix" o "wip", non c'è scansione dei segreti e l'integrazione barcolla da una crisi di integrazione all'altra.
- **Livello 2, Sviluppo:** compaiono pratiche di base ma variano per team. Un modello di ramificazione e convenzioni sui messaggi esistono in alcuni posti, ma i rami vivono ancora troppo a lungo, l'applicazione è parziale, la scansione dei segreti è a macchia di leopardo e la struttura dei repository è stata ereditata anziché scelta.
- **Livello 3, Standardizzazione:** le pratiche sono documentate e fatte rispettare in tutta l'organizzazione: sviluppo basato sul trunk con rami brevi, un ramo principale protetto e sempre rilasciabile, convenzioni dei commit fatte rispettare, scansione dei segreti sia negli hook sia nella CI, accesso al minimo privilegio e una scelta deliberata tra monorepo e polirepo.
- **Livello 4, Gestione:** le pratiche sui sorgenti sono misurate e controllate con dati. Si seguono durata dei rami, frequenza di integrazione, tasso di rottura del ramo principale, tempo medio per rilevare e ruotare un segreto trapelato e tracciabilità da modifica a elemento di lavoro rispetto a valori di riferimento concordati, e si agisce quando i numeri derivano anziché aspettare il prossimo incidente.
- **Livello 5, Orchestrazione:** le pratiche sono migliorate di continuo e integrate in tutta l'organizzazione. Ramificazione, struttura dei repository e strumenti si adattano al mutare di team e accoppiamento del codice, l'automazione fa rispettare l'igiene da un capo all'altro e i dati del controllo di versione alimentano le decisioni di consegna, sicurezza e rischio in tutta l'organizzazione.

## Spunti di discussione

- La durata dei rami del vostro team è davvero breve, e se no, che cosa impedisce l'integrazione continua?
- La vostra scelta tra monorepo e polirepo corrisponde a quanto è davvero accoppiato il vostro codice?
- Come gestite oggi grandi binari e artefatti generati, e quanto vi costa?
- Che cosa accadrebbe se una credenziale attiva fosse committata ora, e quanto in fretta la rilevereste e la ruotereste?
- Quanta disciplina su messaggi di commit e tracciabilità vale la pena far rispettare nel vostro contesto?
- Come cambiano i feature flag la vostra strategia di ramificazione, e quali nuovi rischi introducono?

## Punti chiave

- Integra spesso con rami di breve durata; la lunga divergenza causa il dolore che sembra evitare.
- Mantieni rilasciabile il ramo principale e proteggilo con controlli obbligatori.
- Non lasciare mai che i segreti entrino nella storia; scansiona in automatico e ruota subito se accade.
- Scegli monorepo o polirepo in base al tuo vero accoppiamento e alle esigenze di coordinamento.
- Tratta la storia dei commit come documentazione, con commit significativi, convenzionali e atomici.

## Riferimenti e letture di approfondimento

- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Jez Humble e David Farley, *Continuous Delivery*
- Scott Chacon e Ben Straub, *Pro Git*
- Paul Hammant e altri, scritti sullo sviluppo basato sul trunk
- Specifica Conventional Commits (come standard di riferimento)
- Martin Fowler, articoli su schemi di ramificazione e integrazione continua
