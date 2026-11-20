# 2.7 Documentazione

## Panoramica e motivazioni

La [documentazione](https://en.wikipedia.org/wiki/Software_documentation) è la conoscenza scritta che permette alle persone di usare, far funzionare e modificare il software senza dover ricostruire la comprensione dal solo codice. Ha molti generi: come iniziare, come svolgere un compito, come è strutturato un sistema, come rispondere a un incidente, che cosa accetta e restituisce un'[API](https://en.wikipedia.org/wiki/API). Ciascuno serve un lettore diverso con un bisogno diverso. Una buona documentazione non è facoltativa. È la differenza tra una conoscenza che scala in una grande organizzazione e una che vive nella testa di poche persone.

Per i grandi team, la documentazione è la tua migliore difesa contro il rischio della persona chiave (il pericolo quando la conoscenza critica sta presso una sola persona o poche) e il modo più rapido di inserire i nuovi arrivati. Quando centinaia di ingegneri dipendono da sistemi che non hanno costruito, e le persone entrano, si spostano e se ne vanno di continuo, l'organizzazione può funzionare solo se la conoscenza è messa per iscritto e facile da trovare. I sistemi non documentati diventano fragili: solo i loro autori possono modificarli in sicurezza, e quando quegli autori se ne vanno, l'organizzazione perde la capacità di mantenere il proprio software. È uno dei fallimenti più comuni e costosi su larga scala.

I contesti aziendali e governativi alzano ulteriormente la posta. I sistemi vivono a lungo, quindi la tua documentazione deve servire i manutentori anni, anche decenni, dopo che il team originale se n'è andato. I regimi normativi e di audit impongono spesso documenti specifici come evidenza di controllo: registri dell'architettura, [runbook](https://en.wikipedia.org/wiki/Runbook) (procedure operative e di risposta agli incidenti passo per passo) e registri delle decisioni. I sistemi del settore pubblico passati tra fornitori si affidano interamente alla documentazione per trasportare la conoscenza oltre i confini contrattuali. Eppure la documentazione è notoriamente soggetta a marcire, quindi la vera sfida è mantenerla accurata man mano che il software cambia.

## Principi chiave

- Scrivi per un lettore specifico con un bisogno specifico; tipi diversi di documentazione servono scopi diversi.
- Tieni la documentazione vicino al codice e trattala come codice (docs-as-code).
- L'accuratezza batte la completezza; una piccola quantità di documentazione affidabile batte una grande quantità sbagliata.
- Genera ciò che si può generare; non mantenere a mano ciò che uno strumento può produrre dalla fonte di verità.
- Combatti attivamente il marcire della documentazione; i documenti obsoleti sono peggio di nessuno perché fuorviano.
- Rendi la documentazione reperibile; la conoscenza introvabile è di fatto assente.
- Registra le decisioni e la loro motivazione, non solo lo stato attuale.

## Raccomandazioni

### Adotta docs-as-code

Tieni la documentazione nel [controllo di versione](https://en.wikipedia.org/wiki/Version_control) accanto al codice che descrive, scrivila in un linguaggio di marcatura in testo semplice e rivedila con lo stesso processo di pull request. Così resta versionata, rivedibile e vicina al codice, e puoi aggiornare entrambi insieme. Pubblicala attraverso una pipeline automatizzata, così che l'ultima versione sia sempre disponibile. Trattare i documenti come codice porta la stessa disciplina che mantiene affidabile il codice: revisione, storia e automazione.

### Struttura i contenuti con il framework Diátaxis

Organizza la documentazione in quattro tipi distinti, perché mescolarli non serve nessun lettore: tutorial (orientati all'apprendimento, per i nuovi arrivati), guide pratiche (orientate al compito, per un obiettivo specifico), riferimento (orientato all'informazione, preciso e completo) e spiegazione (orientata alla comprensione, il perché e il contesto). Mantienili separati e tutto diventa più facile da scrivere, navigare e mantenere, perché ogni pagina ha un compito chiaro e un destinatario chiaro.

### Mantieni i documenti operativi essenziali

Dai a ogni repository un [README](https://en.wikipedia.org/wiki/README) chiaro come porta d'ingresso: che cosa è, come costruirlo e farlo girare e dove andare dopo. Scrivi runbook per i compiti operativi e la risposta agli incidenti, così che chiunque sia reperibile possa agire, non solo gli esperti. Mantieni una documentazione dell'architettura che spieghi la struttura del sistema e i componenti chiave. E fornisci una documentazione di inserimento che renda produttivo in fretta un nuovo ingegnere. Sono i documenti di cui senti di più la mancanza quando non ci sono.

### Genera la documentazione delle API e i registri delle modifiche dalla fonte di verità

Genera la documentazione di riferimento delle API dal contratto leggibile da macchina o dalle annotazioni del codice, così che non possa divergere dall'interfaccia reale. Tieni un [registro delle modifiche](https://en.wikipedia.org/wiki/Changelog), idealmente generato da commit strutturati o note di rilascio, così che i consumatori possano vedere che cosa è cambiato tra le versioni. Automatizzarli toglie dal tuo piatto la documentazione mantenuta a mano più soggetta a marcire e la mantiene affidabile.

### Registra le decisioni architetturali

Cattura le decisioni architetturali e di progetto importanti come registri leggeri e datati che dichiarano il contesto, la decisione e le sue conseguenze. Questi registri delle decisioni conservano la motivazione che altrimenti andrebbe persa, così che i futuri manutentori possano vedere perché il sistema è com'è anziché metterlo in dubbio o ripetere vecchi errori. Rendono soprattutto nelle lunghe vite dei sistemi aziendali e governativi.

### Combatti con deliberazione il marcire della documentazione

Tratta la documentazione obsoleta come un difetto. Aggiorna i documenti nella stessa modifica che altera il comportamento e fanne un'aspettativa di revisione. Assegna la responsabilità, così che ogni documento importante abbia qualcuno che ne risponde. Rivedi di tanto in tanto l'accuratezza della documentazione di alto valore, elimina ciò che è obsoleto e rimuovi o segnala chiaramente tutto ciò di cui non ti fidi più. La documentazione che marcisce meno è la documentazione viva: generata o testata rispetto al sistema stesso.

### Investi nella gestione della conoscenza e nella reperibilità

Rendi la documentazione trovabile attraverso una buona ricerca, una navigazione chiara e una casa conosciuta, così che le persone possano individuare ciò che serve senza dover chiedere a qualcuno. Non lasciare che si frammenti in troppe wiki e strumenti scollegati. E cattura la [conoscenza tacita](https://en.wikipedia.org/wiki/Tacit_knowledge), la comprensione informale che vive nelle conversazioni in chat e nelle teste delle persone, in una forma durevole e reperibile prima che scivoli via.

## Compromessi: vantaggi e svantaggi

| Approccio | Vantaggi | Svantaggi |
|---|---|---|
| Docs-as-code | Versionato, rivedibile, vicino al codice; poco marcire | Richiede disciplina degli ingegneri; meno amichevole per autori non tecnici |
| Wiki / base di conoscenza | Facile da modificare; accessibile a tutti | Si allontana dal codice; si frammenta; marcisce in silenzio |
| Documentazione generata (API, registro delle modifiche) | Sempre accurata; poca manutenzione | Limitata a ciò che la fonte esprime; richiede strumenti |
| Spiegazione scritta a mano | Contesto e motivazione ricchi che le macchine non sanno produrre | Laboriosa; incline a diventare obsoleta |
| Struttura Diátaxis | Scopo chiaro per pagina; più facile da navigare e mantenere | Sforzo iniziale di strutturazione; richiede disciplina dell'autore |

Il compromesso centrale è tra sforzo e accuratezza e durevolezza. La documentazione più economica da scrivere, una rapida pagina di wiki, è anche la più soggetta a marcire e frammentarsi. La documentazione più durevole, generata dalla fonte o rivista come codice, costa più disciplina in anticipo ma resta affidabile. Una buona regola pratica: genera ciò che puoi, tieni il resto vicino al codice e rivisto come codice, e riserva la spiegazione scritta a mano, laboriosa, alla motivazione che solo le persone possono fornire.

## Domande da discutere con il tuo team

1. **I vostri documenti sono separati per bisogno del lettore, o tutorial, riferimento e spiegazione si mescolano in un'unica pagina?** Questo capitolo raccomanda la divisione Diátaxis in tutorial, guide pratiche, riferimento e spiegazione, ed elenca il mescolare i tipi come un antipattern che non serve nessun lettore. Su larga scala, un nuovo arrivato che impara il sistema e un ingegnere reperibile che cerca un fatto preciso hanno bisogno di pagine diverse, e una singola pagina mista rallenta entrambi. Porta il segnale: scegli i tuoi documenti più visitati e controlla se ciascuno ha un compito chiaro e un destinatario chiaro. Ristruttura i peggiori in tipi distinti, così che ogni pagina sia più facile da scrivere, navigare e tenere aggiornata. Quella struttura è ciò che rende mantenibile la documentazione man mano che l'organizzazione cresce.

2. **Catturate le decisioni architetturali importanti con la loro motivazione, o solo lo stato attuale?** Il capitolo raccomanda registri delle decisioni leggeri e datati che dichiarano contesto, decisione e conseguenze, e nota che rendono soprattutto nelle lunghe vite dei sistemi aziendali e governativi. Senza di essi, un manutentore anni dopo non riesce a vedere perché il sistema è com'è, quindi mette in dubbio scelte solide o ripete vecchi errori. Porta come segnale concreto una decisione difficile recente il cui ragionamento ora vive solo in una conversazione in chat o nella memoria di qualcuno. Adotta un breve formato di registro delle decisioni e rendi la scrittura di uno parte di qualsiasi modifica di progetto importante. La motivazione è esattamente la conoscenza che solo le persone possono fornire e che marcisce più in fretta quando non è scritta.

3. **Qualsiasi ingegnere reperibile può rispondere a un incidente solo dai vostri runbook, senza chiamare la persona che ha costruito il sistema?** Questo capitolo indica i runbook come documento operativo essenziale, così che chiunque sia reperibile possa agire, non solo gli esperti, e descrive un team governativo che ha potuto ereditare un sistema solo perché i runbook avevano trasportato la conoscenza oltre un confine contrattuale. Il rischio della persona chiave è il fallimento da cui questo protegge: quando l'unico esperto è irraggiungibile o se n'è andato, una procedura di ripristino non documentata trasforma un incidente di routine in un'interruzione. Porta le prove: prendi un incidente recente e verifica se il solo runbook l'avrebbe risolto. Scrivi e collauda runbook per le procedure che le persone temono e tratta come difetto un runbook che non regge da solo. È la differenza tra un ripristino alle 2 di notte e un'escalation alle 2 di notte.

4. **Quali dei vostri riferimenti API e registri delle modifiche sono generati dalla fonte di verità, e quali sono ancora mantenuti a mano e si allontanano in silenzio?** Questo capitolo ti dice di generare la documentazione di riferimento dal contratto leggibile da macchina o dalle annotazioni del codice, così che non possa divergere dall'interfaccia reale, ed elenca il mantenere a mano contenuti generabili come antipattern. Per un grande team, una documentazione API scritta a mano che resta indietro rispetto all'interfaccia reale è peggio di nessuna: ogni consumatore che si fida scrive un'integrazione rotta, e il fallimento emerge lontano dalla pagina obsoleta che l'ha causato. Porta il segnale concreto: campiona una manciata delle tue interfacce più usate e confronta il riferimento pubblicato con il contratto reale per vedere quanto ciascuno si è allontanato. Dove trovi deriva, collega il riferimento alla build così che si rigeneri a ogni modifica e ritira la copia mantenuta a mano. Nei contesti aziendali e governativi, dove le interfacce sono consumate tra team, fornitori e confini contrattuali che non vedi mai, un riferimento generato e autorevole è spesso l'unica cosa che impedisce agli integratori di costruire su una finzione.

5. **Chi possiede ogni documento di alto valore, e come ve ne accorgereste oggi se uno fosse diventato obsoleto?** Il capitolo tratta la documentazione obsoleta come un difetto e avverte che i documenti senza responsabile marciscono perché aggiornarli non è compito di nessuno, mentre i documenti obsoleti presentati come attuali distruggono la fiducia in tutta la documentazione. Su larga scala il pericolo non è una singola pagina sbagliata ma la lenta erosione della fiducia: una volta che i lettori si sono scottati con istruzioni superate, smettono di fidarsi dell'intero corpus e tornano a interrompere le persone. Porta una mappa di responsabilità dei tuoi documenti più critici e una risposta onesta su come si rileva il marcire, se con una cadenza di revisione, con la generazione, con test rispetto al sistema o per pura fortuna. Assegna un responsabile nominato a ogni documento che conta e preferisci la documentazione viva, generata o testata, così che l'obsolescenza emerga meccanicamente anziché attraverso un lettore imbarazzato. Per i sistemi aziendali e governativi che sopravvivono ai propri team originali, la documentazione senza responsabile è una passività che un auditor o un fornitore subentrante finirà per addebitarti.

6. **Quanto è reperibile la vostra documentazione, e quanta conoscenza critica vive ancora solo nelle conversazioni in chat e nelle teste delle persone?** Questo capitolo dice che la conoscenza introvabile è di fatto assente, avverte contro la frammentazione dei documenti in troppe wiki e strumenti scollegati e ti esorta a catturare la conoscenza tacita in una forma durevole e reperibile prima che scivoli via. In una grande organizzazione lo stesso fatto viene spesso riscoperto, richiesto di nuovo e di nuovo risposto cento volte perché nessuno riesce a trovare dove fosse già stato scritto, e ogni partenza porta fuori dalla porta un contesto insostituibile. Porta le prove: conta quante case separate di documentazione mantieni, prova a trovare tre fatti importanti con la sola ricerca e nota dove le vere risposte si sono rivelate stare nella memoria di qualcuno o in un messaggio sepolto. Consolida verso una casa conosciuta con una vera ricerca e una navigazione chiara e fai della cattura della conoscenza tacita una parte di routine del lavoro anziché un salvataggio eroico. Nei contesti del settore pubblico e fortemente esternalizzati, dove i sistemi passano tra fornitori e team per contratto, la conoscenza scritta e reperibile è l'unica cosa che sopravvive al passaggio di consegne.

## Lente settoriale

**Startup.** Con una manciata di ingegneri e nessuna liquidità da sprecare, documenta solo ciò di cui avrebbe davvero bisogno un'interruzione delle 2 di notte o un nuovo assunto: un vero README per servizio, un runbook collaudato per la procedura di rilascio e ripristino che tutti temono e qualche nota datata sulle decisioni che altrimenti dimenticheresti. Genera la documentazione delle API dal contratto così da non mantenerla mai a mano. Resisti alla tentazione di costruire una piattaforma di documentazione; una cartella versionata di marcatura accanto al codice basta finché non senti un dolore vero.

**Piccola impresa.** Senza un redattore tecnico e con un budget ridotto, appoggiati alla documentazione che i tuoi strumenti già generano e a un docs-as-code leggero anziché a un programma con personale dedicato. Imposta la scelta come comprare contro costruire: preferisci piattaforme che producono un proprio riferimento aggiornato e una base di conoscenza ricercabile a una wiki che devi curare a mano. Spendi il tuo scarso sforzo sui due o tre documenti la cui assenza fermerebbe l'attività e lascia che una pagina sbagliata o mancante sia l'innesco per correggere la responsabilità.

**Grande impresa.** Tra molti team il problema è coerenza e reperibilità: una pipeline docs-as-code condivisa, una struttura comune come Diátaxis, riferimenti API e registri delle modifiche generati e registri delle decisioni applicati allo stesso modo ovunque, così che la conoscenza non si frammenti in decine di wiki. Assegna la responsabilità di ogni documento di alto valore e misura l'accuratezza, non solo la presenza. Tratta registri dell'architettura, runbook e registri delle decisioni come evidenza di audit e standardizza come vengono prodotti, così che una revisione di controllo trovi una traccia documentata e difendibile anziché un affannarsi.

**Ente pubblico.** Regole sugli appalti e responsabilità pubblica fanno della documentazione un prodotto da consegnare, non una cortesia. Scrivi documentazione dell'architettura, runbook e registri delle decisioni nei contratti come artefatti obbligatori, rivisti per accuratezza, così che la conoscenza sopravviva a un cambio di fornitore e un sistema possa essere gestito da chiunque lo erediti. Richiedi che qualsiasi operatore autorizzato possa rispondere a un incidente solo dal runbook e tieni i registri delle decisioni come traccia pubblica trasparente del perché le scelte sono state fatte. Una documentazione scarna qui non è un disagio privato; diventa un'ingegneria inversa costosa finanziata dal contribuente.

## Esempi

**Startup.** Una startup di cinque persone scrive un vero README per ogni servizio e un breve runbook per l'unica procedura di rilascio e ripristino che tutti temono, così che un'interruzione alle 2 di notte non dipenda dal svegliare l'unico fondatore che conosce il sistema. Genera la documentazione delle API dal contratto anziché scriverla a mano e annota qualche nota datata che spiega perché hanno scelto il database e l'approccio all'autenticazione. Resta leggera, ma significa che il sesto e il settimo assunto si inseriscono dai documenti anziché interrompendo tutti.

**Grande impresa.** Una grande società di software tiene tutta la documentazione negli stessi repository del codice, scritta in marcatura e rivista nelle pull request accanto alle modifiche che descrive. I riferimenti API sono generati dai contratti dei servizi, così da non derivare mai. I registri delle modifiche sono generati da commit strutturati e i registri delle decisioni architetturali conservano il ragionamento dietro le scelte principali. Un sito di documentazione pubblicato si costruisce automaticamente a ogni integrazione. I nuovi ingegneri diventano produttivi in fretta perché guide di inserimento e runbook sono aggiornati e reperibili, e gli ingegneri reperibili si appoggiano ai runbook anziché chiamare gli autori originali.

**Ente pubblico.** Un'agenzia nazionale eredita un sistema da un fornitore in uscita, dipendendo interamente dalla documentazione per trasportare la conoscenza oltre il confine contrattuale. Poiché il fornitore precedente aveva mantenuto documentazione dell'architettura, runbook e registri delle decisioni come prodotti obbligatori, il nuovo team può gestire e modificare il sistema senza gli autori originali. Dove la documentazione era scarna, l'agenzia affronta una costosa ingegneria inversa. Quell'esperienza guida una nuova politica: la documentazione è un prodotto contrattuale, rivisto per accuratezza anziché trattato come un ripensamento, e i runbook devono permettere a qualsiasi operatore autorizzato di rispondere agli incidenti.

## Business case: motivazioni, ROI e TCO

La documentazione si ripaga con un inserimento più breve, meno rischio della persona chiave, risposta agli incidenti più rapida e un costo del cambiamento più basso nella vita di un sistema. Nuovi ingegneri che raggiungono la produttività in giorni anziché settimane, personale reperibile che risolve gli incidenti da un runbook anziché fare escalation, manutentori che cambiano un sistema con fiducia anni dopo che è stato costruito: sono grandi risparmi ricorrenti che si cumulano in una grande organizzazione e in una lunga vita del sistema.

Quanto costa la documentazione? Sforzo di scrittura e manutenzione. Quanto costa il *non* documentare? Si paga di continuo: in inserimento lento, domande ripetute, colli di bottiglia sulle persone chiave, ripristino degli incidenti più lento e, all'estremo, sistemi che nessuno può modificare in sicurezza, costringendo a costose riscritture o ingegneria inversa. Negli scenari di cambio di fornitore e di audit, la documentazione mancante può portare costi contrattuali e di conformità diretti. Per sostenere il caso con la leadership, dai un numero al tempo di inserimento, al tempo di risposta agli incidenti e a quanta conoscenza critica sta nelle teste dei singoli. Poi presenta docs-as-code e la generazione come modi di ottenere documentazione durevole senza un corrispondente onere di manutenzione. E sottolinea che la documentazione inaccurata è una passività, quindi l'investimento deve includere il mantenerla aggiornata.

## Antipattern e insidie

- **Documentazione obsoleta presentata come attuale:** fuorvia i lettori e distrugge la fiducia in tutta la documentazione.
- **La wiki scritta una volta sola:** pagine create e mai aggiornate, che si allontanano in silenzio dalla realtà.
- **Frammentazione della documentazione:** conoscenza sparsa in molti strumenti e wiki così che nulla si può trovare.
- **Mescolare i tipi di documentazione:** tutorial, riferimento e spiegazione confusi in un'unica pagina, che non serve nessun lettore.
- **Mantenere a mano contenuti generabili:** documentazione API scritta a mano che inevitabilmente diverge dall'interfaccia reale.
- **Conoscenza tribale:** comprensione critica tenuta solo nelle teste delle persone e nella storia delle chat, persa quando se ne vanno.
- **Documentazione come ripensamento:** scritta alla fine, se mai, anziché insieme alla modifica.
- **Nessuna responsabilità:** documenti senza un responsabile marciscono perché aggiornarli non è compito di nessuno.

## Modello di maturità

- **Livello 1, Avvio.** La documentazione è scarsa, sparsa e obsoleta, e la conoscenza vive nelle teste delle persone. Ciò che esiste è stato scritto una volta e mai più toccato, quindi un'interruzione o una partenza significa fare ingegneria inversa del sistema.
- **Livello 2, Sviluppo.** Esistono documenti chiave, come README e qualche runbook, ma sono mantenuti in modo incoerente e difficili da trovare. Alcuni team documentano bene e altri a malapena, e non c'è un'aspettativa condivisa su che cosa un repository debba contenere né dove debba stare.
- **Livello 3, Standardizzazione.** Docs-as-code è la norma nell'organizzazione: una struttura comune come Diátaxis, riferimenti API e registri delle modifiche generati, registri delle decisioni e un'aspettativa in revisione che i documenti cambino insieme al codice che descrivono. Ogni documento di alto valore ha un responsabile nominato e c'è una casa conosciuta con una vera ricerca.
- **Livello 4, Gestione.** La documentazione è misurata, non solo presente. Si seguono la copertura dei documenti essenziali, il tasso di modifica dei documenti rispetto a quello del codice, il tempo di inserimento, la risoluzione degli incidenti dal solo runbook e la freschezza rispetto a una soglia di obsolescenza definita, e si rivedono queste metriche rispetto a valori di riferimento. Il marcire è colto meccanicamente attraverso generazione, test rispetto al sistema e controlli di collegamenti e accuratezza, e le pagine obsolete sono segnalate o eliminate sulla base delle prove anziché per caso.
- **Livello 5, Orchestrazione.** La documentazione è migliorata di continuo e integrata in tutta l'organizzazione: viva, in gran parte generata o testata rispetto al sistema, con responsabile, reperibile e adattiva. Le metriche ritornano a guidare dove si investe, la conoscenza tacita è catturata come parte di routine del lavoro e il corpus è riequilibrato e sfoltito attivamente al mutare di sistemi, team e lettori.

## Spunti di discussione

- Quale documentazione, se sparisse domani, farebbe più male alla vostra organizzazione, ed esiste oggi e resta aggiornata?
- Come fate dell'aggiornamento della documentazione una parte naturale del cambiare il codice anziché una faccenda separata?
- Dove potete sostituire la documentazione scritta a mano con una documentazione generata legata alla fonte di verità?
- Come misurate se la vostra documentazione è accurata e usata, non solo presente?
- Come dovrebbero cambiare gli assistenti IA il modo in cui scrivete, mantenete e cercate la documentazione, e dove potrebbero introdurre contenuti plausibili ma sbagliati?
- Come catturate la conoscenza tacita prima che le persone che la detengono se ne vadano?

## Punti chiave

- Tratta la documentazione come codice: versionata, rivista, vicina alla fonte e pubblicata automaticamente.
- Struttura i contenuti per bisogno del lettore con tutorial, guide pratiche, riferimento e spiegazione.
- Mantieni gli essenziali di alto valore: README, runbook, documentazione dell'architettura, inserimento e registri delle decisioni.
- Genera documentazione delle API e registri delle modifiche così che non possano derivare dalla fonte di verità.
- Combatti il marcire con responsabilità, aspettative di revisione e potatura; la documentazione inaccurata è peggio di nessuna.

## Riferimenti e letture di approfondimento

- Daniele Procida, framework di documentazione *Diátaxis*
- Andrew Etter, *Modern Technical Writing*
- Anne Gentle, *Docs Like Code*
- Google, *Developer Documentation Style Guide* e indicazioni di Season of Docs (come esempi di riferimento)
- Michael Nygard, *Documenting Architecture Decisions* (registri delle decisioni architetturali)
- Andrew Hunt e David Thomas, *The Pragmatic Programmer* (su conoscenza e documentazione)
- *Keep a Changelog* (come convenzione di riferimento)
