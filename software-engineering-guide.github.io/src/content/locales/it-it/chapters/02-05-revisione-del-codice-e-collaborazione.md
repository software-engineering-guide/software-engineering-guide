# 2.5 Revisione del codice e collaborazione

## Panoramica e motivazioni

La [revisione del codice](https://en.wikipedia.org/wiki/Code_review) è la pratica per cui qualcuno diverso dall'autore esamina una modifica prima che venga integrata. È una delle attività di qualità e di condivisione della conoscenza con la leva più alta che un'organizzazione software possieda, e per i grandi team è anche un meccanismo primario di coordinamento e di cultura. La revisione coglie i difetti, diffonde la conoscenza della base di codice, fa rispettare gli standard e fa da mentore agli ingegneri, ma solo quando la si fa bene. Fatta male, diventa un collo di bottiglia, una fonte di attrito o un timbro di approvazione che dà una falsa garanzia.

Per i grandi team, la revisione è dove il lavoro individuale incontra la responsabilità collettiva. È spesso il principale punto di contatto tra ingegneri che altrimenti lavorano da soli, quindi le sue norme plasmano il modo in cui collabora l'intera organizzazione. La revisione diffonde la conoscenza così che nessuna parte del sistema sia compresa da una sola persona, il che riduce il rischio del [bus factor](https://en.wikipedia.org/wiki/Bus_factor), il pericolo quando la conoscenza sta in troppo poche persone, che affligge i sistemi grandi e di lunga durata. Crea anche una traccia di audit di chi ha cambiato che cosa e chi l'ha approvato.

Nei contesti aziendali e governativi, la revisione porta spesso una dimensione di conformità. La [separazione dei compiti](https://en.wikipedia.org/wiki/Separation_of_duties) (nessuna singola persona controlla un'intera modifica sensibile), le approvazioni obbligatorie e la tracciabilità sono controlli frequentemente richiesti. Una modifica che tocca sistemi sensibili può richiedere la revisione di ruoli specifici, e la traccia della revisione diventa evidenza di audit. La tua sfida è soddisfare questi controlli mantenendo la revisione rapida e costruttiva, anziché trasformarla in cerimonia.

## Principi chiave

- Rivedi per migliorare la modifica e condividere conoscenza, non per mettersi in mostra.
- Le modifiche piccole ottengono revisioni migliori, quindi mantieni le pull request (PR) mirate e di dimensione ragionevole.
- La latenza di revisione è un costo per tutto il team. Un tempo di risposta rapido mantiene tutti in movimento.
- Automatizza il meccanico (stile, test, scansioni di sicurezza) così che le persone rivedano progetto e correttezza.
- Separa i problemi bloccanti da suggerimenti e preferenze e sii esplicito su quale è quale.
- Critica il codice, non la persona. Le norme sul feedback decidono se la revisione costruisce fiducia o la corrode.
- L'autore è responsabile di rendere facile da rivedere una modifica.

## Raccomandazioni

### Rendi piccole e ben descritte le pull request

Mantieni ogni modifica concentrata su una singola questione logica e abbastanza piccola da essere rivista con attenzione. Le PR grandi ottengono revisioni superficiali. Dai una descrizione chiara di che cosa è cambiato, perché e come lo hai verificato, così che il revisore abbia contesto. Dividi in PR separate i refactoring meccanici e i cambiamenti di comportamento, così che ciascuna sia facile da ragionare. Una buona descrizione è il singolo contributo più importante dell'autore alla qualità della revisione.

### Stabilisci standard e liste di controllo per la revisione

Esplicita che cosa i revisori dovrebbero cercare: correttezza, adeguatezza al progetto, adeguatezza dei test, implicazioni di sicurezza, leggibilità e rispetto degli standard. Una lista di controllo leggera mantiene coerenti le revisioni e impedisce che dimensioni importanti sfuggano, senza trasformare la revisione in un rito di caselle da spuntare. Definisci che cosa richiede revisione, chi può approvare e le eventuali approvazioni per ruolo necessarie per le aree sensibili.

### Fissa e monitora le norme sulla latenza di revisione

Concorda un tempo di risposta obiettivo, per esempio rispondere entro un giorno lavorativo, e fai della revisione una parte di prim'ordine della giornata anziché qualcosa infilato per ultimo. Le lunghe code di revisione bloccano la consegna e tentano gli ingegneri a modifiche sovradimensionate e accorpate. Monitora il tempo alla prima revisione e il tempo all'integrazione e tratta una latenza prolungata come un problema di processo da correggere, non come una colpa personale.

### Automatizza tutto ciò che è meccanico

Esegui formattazione, [linting](https://en.wikipedia.org/wiki/Lint_(software)), test e scansione di sicurezza e delle dipendenze nell'[integrazione continua](https://en.wikipedia.org/wiki/Continuous_integration) (CI), così che i revisori non spendano mai attenzione su di essi. Riserva la revisione umana alle cose che le macchine non sanno giudicare: se il progetto è giusto, se l'approccio si adatta al sistema, se i test hanno senso e se il codice avrà ancora senso più avanti.

### Usa la programmazione in coppia e in gruppo dove si adattano

Usa la [programmazione in coppia](https://en.wikipedia.org/wiki/Pair_programming), in cui due ingegneri scrivono codice insieme a una postazione, per il lavoro complesso o ad alto rischio, l'inserimento e il trasferimento di conoscenza. È una revisione continua e spesso elimina la necessità di un passaggio di revisione separato. Usa la [programmazione in gruppo](https://en.wikipedia.org/wiki/Mob_programming) (mob programming), in cui l'intero team lavora su un compito alla volta, per decisioni di progetto critiche o per diffondere nel team la conoscenza di un'area ostica. Considerale complementi alla revisione asincrona, scelti in base al contesto, non sostituti da imporre ovunque.

### Adotta con cautela la revisione automatica e assistita dall'IA

Usa strumenti di revisione automatica e assistenti IA per cogliere problemi comuni, suggerire miglioramenti e alleggerire il carico del revisore, ma tratta il loro output come input, non come autorità. La revisione IA è buona su problemi superficiali e coerenza e debole sul giudizio profondo di progetto e sul contesto di sistema. Mantieni una persona responsabile di ogni approvazione, soprattutto per le modifiche sensibili per la sicurezza e rilevanti per la conformità.

### Fissa norme di feedback costruttivo

Fissa norme che mantengano il feedback specifico, gentile e concentrato sul codice. Incoraggia i revisori a fare domande anziché dare ordini, a spiegare il ragionamento dietro una richiesta e a lodare il buon lavoro. Segna chiaramente le preoccupazioni bloccanti e i suggerimenti facoltativi (per esempio anteponendo un prefisso alle note non bloccanti). Queste norme decidono se la revisione rafforza il team o genera risentimento.

## Compromessi: vantaggi e svantaggi

| Approccio | Vantaggi | Svantaggi |
|---|---|---|
| Revisione asincrona delle PR | Flessibile; documentata; scala tra fusi orari | Latenza; perde sfumature; può sembrare conflittuale |
| Programmazione in coppia | Revisione continua; trasferimento di conoscenza rapido; alta qualità | Due persone su un compito; faticosa; più difficile da pianificare |
| Programmazione in gruppo | Allineamento di tutto il team; diffonde conoscenza profonda | Costosa in aggregato; non per il lavoro di routine |
| Più revisori obbligatori | Forte garanzia; favorevole alla conformità | Più lenta; diffonde la responsabilità; pressione sulle code |
| Revisione assistita dall'IA | Veloce, instancabile sui problemi comuni; riduce il carico | Manca il contesto di sistema; falsa confidenza se si confida troppo |

La tensione di fondo è tra accuratezza e velocità. Una revisione più profonda coglie di più, ma rallenta la consegna e può frustrare gli autori. Una revisione più rapida mantiene il flusso, ma rischia di essere superficiale. La via d'uscita è adeguare la profondità della revisione al rischio della modifica, così che le modifiche banali ottengano una revisione leggera e quelle rischiose una profonda, e automatizzare il lavoro meccanico così che lo sforzo umano si concentri dove conta.

## Domande da discutere con il tuo team

1. **Che cosa conta come troppo grande per una pull request, e separate i refactoring meccanici dai cambiamenti di comportamento?** Questo capitolo afferma chiaramente che le PR grandi ottengono revisioni superficiali e che l'autore è responsabile della rivedibilità, e chiede di separare i refactoring dai cambiamenti di comportamento così che ciascuno sia facile da ragionare. In un grande team una PR gigante garantisce un timbro di approvazione, che dà falsa garanzia lasciando passare difetti reali. Porta le prove: la distribuzione delle dimensioni delle tue PR e come la profondità della revisione cala al crescere delle differenze. Concorda una norma pratica sulla dimensione e l'abitudine di integrare i refactoring puri separatamente dalle modifiche di logica, così che un revisore possa davvero tenere a mente ciascuna modifica. Quell'unica disciplina alza la qualità di ogni revisione che segue.

2. **Come distinguete un'obiezione bloccante da un suggerimento facoltativo, e quella convenzione è davvero usata?** Il capitolo chiede di separare i problemi bloccanti dalle preferenze e di essere espliciti su quale è quale, e segnala il bloccare su una preferenza come un antipattern corrosivo. Senza una convenzione condivisa, l'opinione di stile di un revisore si legge come una modifica richiesta, il che genera risentimento e rallenta la consegna in tutto il team. Porta come segnale concreto esempi di revisioni recenti in cui una preferenza ha bloccato un'integrazione. Adotta un marcatore leggero, per esempio un prefisso che etichetta le note non bloccanti, così che gli autori sappiano subito che cosa deve cambiare e che cosa è un suggerimento. Questo mantiene la revisione concentrata su correttezza e progetto anziché sul gusto.

3. **Chi deve approvare le modifiche al codice sensibile per la sicurezza o rilevante per la conformità, e come viene fatto rispettare questo instradamento?** Questo capitolo descrive approvazioni per ruolo, regole di titolarità del codice e separazione dei compiti in cui nessuna singola persona controlla un'intera modifica sensibile, con l'approvazione registrata come evidenza di audit. Nei contesti aziendali e governativi questi sono controlli richiesti, e il rischio è che vengano saltati oppure diventino un collo di bottiglia che congela la consegna. Porta il segnale: quali moduli sono sensibili e se le regole di titolarità instradano oggi quelle modifiche automaticamente agli approvatori giusti. Codifica l'instradamento nella configurazione della titolarità del codice e abbinalo a controlli automatici e modifiche piccole, così che il controllo sia soddisfatto senza una coda di guardiani umani. Decidi questo con deliberazione anziché scoprire la lacuna durante un audit.

4. **Quale obiettivo di latenza di revisione avete davvero concordato, e lo misurate e lo fate rispettare, o è solo un'aspirazione?** Il capitolo tratta la latenza di revisione come un costo per tutto il team e chiede di monitorare il tempo alla prima revisione e il tempo all'integrazione, trattando un ritardo prolungato come un problema di processo anziché una colpa personale. In un grande team una coda di revisione senza responsabile tassa in silenzio tutti: gli autori accorpano modifiche più grandi per evitare l'attesa, quelle modifiche ottengono poi revisioni più superficiali e il tempo di consegna deriva verso l'alto senza un singolo colpevole. La considerazione contraria è che un obiettivo rigido di latenza può spingere i revisori a sfogliare, quindi velocità e profondità vanno bilanciate anziché scambiate alla cieca. Porta le prove: la tua attuale distribuzione del tempo alla prima revisione, come varia per team e per dimensione della modifica e dove le revisioni restano ferme più a lungo. Nei contesti aziendali e governativi, collega l'obiettivo alle metriche di flusso che la leadership già segue, perché un controllo con più revisori obbligatori e nessuna norma di latenza diventa il collo di bottiglia che congela la consegna e tenta le persone ad aggirare del tutto il controllo.

5. **Per quali tipi di modifica vi fidate della revisione automatica e assistita dall'IA, e dove deve restare responsabile una persona?** Il capitolo dice di trattare l'output della revisione IA come input, non come autorità: forte sui problemi superficiali e sulla coerenza, debole sul giudizio profondo di progetto e sul contesto di sistema, con una persona responsabile di ogni approvazione. Senza un confine esplicito, un grande team scivola nell'eccesso di fiducia, in cui un commento verde di un bot si legge come una revisione superata e i veri rischi di progetto e sicurezza passano sotto falsa confidenza. La spinta contraria è che la revisione IA alleggerisce davvero il carico e coglie instancabilmente i difetti comuni, quindi vietarla spreca leva. Porta le prove: dove i suggerimenti automatici hanno colto problemi reali, dove hanno prodotto rumore e quali tipi di modifica (sensibili per la sicurezza, rilevanti per la conformità, architetturali) non lasceresti mai approvare a una macchina da sola. Per il lavoro aziendale e governativo, indica chi detiene la responsabilità di un'approvazione quando un assistente IA era nel ciclo, perché un audit chiederà chi ha rivisto una modifica, e "l'ha fatto lo strumento" non è una risposta che un regolatore accetta.

6. **Dove dovrebbero la programmazione in coppia o in gruppo sostituire la revisione asincrona, e come usate la revisione per ridurre deliberatamente il rischio del bus factor?** Il capitolo imposta la programmazione in coppia e in gruppo come revisione continua scelta in base al contesto, e indica la revisione come il meccanismo che diffonde la conoscenza così che nessuna parte del sistema sia compresa da una sola persona. Se lasciata implicita, la conoscenza si concentra: lo stesso esperto rivede ogni modifica a un sottosistema, la revisione diventa un timbro di approvazione perché nessun altro può contestarlo e il rischio del bus factor cresce proprio dove il sistema è più critico. La considerazione contraria è il costo, poiché la programmazione in gruppo spende il tempo di tutto il team e quella in coppia impegna due ingegneri, quindi non puoi imporla ovunque. Porta le prove: quali moduli hanno un solo revisore credibile, dove l'inserimento si blocca e dove un'area ostica trarrebbe beneficio da una sessione dal vivo anziché da discussioni nei commenti. In un'organizzazione grande o pubblica, tratta la diffusione deliberata della conoscenza come gestione del rischio, perché un sistema di lunga durata le cui parti critiche dipendono da una persona è una passività operativa e di continuità, non solo un disagio di organico.

## Lente settoriale

**Startup.** Con tre o quattro ingegneri, mantieni leggera la revisione: l'approvazione di un collega su una piccola pull request, controlli meccanici nella CI e nessun secondo revisore obbligatorio che bloccherebbe un'integrazione. Il vero obiettivo è meno la conformità che assicurarsi che più di una persona capisca ogni parte del sistema, quindi lavora in coppia sulle parti rischiose e consideralo inserimento. Non costruire un pesante instradamento di titolarità del codice che supererai presto; una norma condivisa di modifiche piccole e ben descritte compra gran parte del beneficio a costo quasi nullo.

**Piccola impresa.** È improbabile che tu abbia uno specialista di strumenti di revisione, quindi appoggiati a ciò che la tua piattaforma di hosting (per esempio un servizio Git gestito) offre di serie anziché costruire automazione su misura. Compra le integrazioni di linting, test e scansione di sicurezza anziché mantenerle, così che i tuoi pochi ingegneri spendano i propri scarsi minuti di revisione su progetto e correttezza. Mantieni una sola regola semplice, ogni modifica ha un altro paio d'occhi, e resisti ad aggiungere processi che nessuno saprebbe mantenere.

**Grande impresa.** La sfida è la coerenza tra molti team: standard condivisi, regole di titolarità del codice che instradano le modifiche sensibili agli approvatori giusti e approvazioni per ruolo registrate come evidenza di audit. Automatizza i controlli meccanici in tutta l'organizzazione così che la revisione umana si concentri sul progetto e segui la latenza di revisione come metrica di flusso, così che i controlli con più revisori obbligatori non diventino in silenzio colli di bottiglia. Adegua la profondità della revisione al rischio della modifica con una politica documentata, così che le modifiche banali restino rapide mentre quelle ad alto rischio ottengano separazione dei compiti e un esame più approfondito.

**Ente pubblico.** Il controllo delle modifiche è spesso obbligatorio: ogni modifica in produzione rivista e approvata da qualcuno diverso dall'autore, con la traccia conservata come evidenza di audit per soddisfare i requisiti di separazione dei compiti. Privilegia una traccia trasparente e tracciabile di chi ha scritto, chi ha approvato e quali controlli sono stati superati e investi in automazione e modifiche piccole e frequenti, così che il controllo non congeli la consegna. Dove gli strumenti di revisione sono acquistati, pretendi registri di audit esportabili ed evita la dipendenza dal fornitore, poiché l'evidenza deve sopravvivere a qualsiasi singolo fornitore e reggere al controllo pubblico.

## Esempi

**Startup.** Una startup di quattro ingegneri mantiene piccola ogni pull request e chiede l'approvazione di un collega prima dell'integrazione, meno per conformità che per assicurarsi che nessuna singola persona sia l'unica a capire una parte del sistema. La CI esegue il formattatore e i test, così che le persone spendano i propri pochi minuti di revisione su progetto e correttezza anziché sugli spazi. Quando il team incontra un pezzo ostico del flusso dei pagamenti, due di loro lavorano in coppia anziché scambiarsi commenti asincroni, il che fa anche da inserimento per l'ultimo arrivato.

**Grande impresa.** Una grande società di software richiede almeno una revisione approvante su ogni modifica, più una seconda approvazione per le modifiche ai moduli sensibili per la sicurezza individuati dalle regole di titolarità del codice. La CI gestisce tutti i controlli di stile e di test, così che i revisori si concentrino su progetto e correttezza. Il team segue il tempo alla prima revisione e tratta una mediana in crescita come segnale per riequilibrare il carico di lavoro. I nuovi ingegneri vengono inseriti attraverso la programmazione in coppia, il che accorcia il loro percorso verso il contribuire in autonomia.

**Ente pubblico.** Un'agenzia nazionale che opera sotto rigidi requisiti di controllo delle modifiche impone che ogni modifica in produzione sia rivista e approvata da qualcuno diverso dall'autore, con l'approvazione registrata per l'audit. Per evitare che questo controllo diventi un collo di bottiglia, l'agenzia investe in controlli automatici e modifiche piccole e frequenti e fissa una norma di risposta alla revisione nello stesso giorno. La traccia della revisione, che copre chi ha scritto, chi ha approvato e quali controlli sono stati superati, diventa parte dell'evidenza di conformità per ogni rilascio, soddisfacendo i requisiti di separazione dei compiti senza congelare la consegna.

## Business case: motivazioni, ROI e TCO

La revisione del codice si ripaga in tre valute: difetti colti prima della produzione, conoscenza diffusa nel team e standard rispettati automaticamente nel tempo. Cogliere un difetto in revisione costa molto meno che coglierlo in produzione, e il beneficio di condivisione della conoscenza riduce il rischio della persona chiave che altrimenti può costare caro a un'organizzazione quando qualcuno se ne va. La revisione è anche il meccanismo di trasmissione culturale che mantiene coerente un team in crescita.

Il costo della revisione è tempo di ingegneri e un po' di latenza, entrambi gestibili con buone pratiche. Il costo del *non* rivedere, o del rivedere male, comprende difetti in produzione, conoscenza in compartimenti stagni, codice incoerente e, negli ambienti regolamentati, audit falliti e rilievi di conformità. Anche una revisione troppo pesante ha un proprio costo reale: lunghe code, accorpamenti sovradimensionati, ingegneri demoralizzati. Per sostenere il caso con la leadership, collega le pratiche di revisione a tasso di fallimento delle modifiche, tempo di consegna e velocità di inserimento e segui la latenza di revisione come metrica di flusso esplicita.

## Antipattern e insidie

- **Il timbro di approvazione:** approvazioni senza un vero esame, che danno falsa garanzia e soddisfano solo la lettera di un controllo.
- **La PR gigante:** migliaia di righe che si possono solo sfogliare, garantendo una revisione superficiale.
- **Revisione solo da pignoli:** concentrarsi sulle minuzie mancando progetto e correttezza, spesso perché i controlli meccanici non sono automatizzati.
- **La revisione come guardiania:** usare la revisione per affermare dominio o bloccare gli altri, avvelenando la collaborazione.
- **La coda lenta:** revisioni ferme per giorni, che bloccano la consegna e incoraggiano l'accorpamento.
- **Fidarsi troppo della revisione IA:** trattare i suggerimenti automatici come autorevoli e abbandonare il giudizio umano sulle modifiche rischiose.
- **Bloccare per preferenza:** presentare opinioni di stile personali come modifiche richieste senza distinguerle dai difetti reali.

## Modello di maturità

- **Livello 1, Avvio:** la revisione è ad hoc e reattiva. Viene spesso saltata o fatta in modo incoerente, i problemi meccanici dominano i commenti, le norme di feedback non sono fissate e qualsiasi traccia di approvazione è incidentale anziché deliberata.
- **Livello 2, Sviluppo:** esistono pratiche di revisione di base ma variano da team a team. La revisione è richiesta in alcuni posti e lenta o facoltativa in altri, l'automazione è parziale e dimensione e qualità delle pull request oscillano molto senza un'aspettativa condivisa.
- **Livello 3, Standardizzazione:** gli standard sono documentati e fatti rispettare in tutta l'organizzazione. PR piccole e mirate, formattazione, linting, test e scansione di sicurezza automatici nella CI, liste di controllo chiare, una convenzione esplicita tra bloccante e suggerimento e regole di titolarità del codice che instradano le modifiche sensibili agli approvatori giusti.
- **Livello 4, Gestione:** la revisione è misurata e controllata rispetto a valori di riferimento. Si seguono tempo alla prima revisione, tempo all'integrazione, profondità della revisione rispetto al rischio della modifica, tasso di difetti sfuggiti e tasso di fallimento delle modifiche; la latenza prolungata è trattata come problema di processo; e i dati guidano dove riequilibrare il carico dei revisori e dove i controlli rallentano la consegna senza aggiungere garanzia.
- **Livello 5, Orchestrazione:** la revisione è migliorata di continuo e integrata in tutta l'organizzazione. La profondità si adatta al rischio della modifica, programmazione in coppia, in gruppo e assistenza IA sono usate con deliberazione con una persona responsabile, diffusione della conoscenza e rischio del bus factor sono gestiti intenzionalmente e la revisione migliora in modo misurabile qualità, flusso di consegna e inserimento.

## Spunti di discussione

- Qual è il giusto obiettivo di latenza di revisione per il vostro team, e che cosa vi impedisce di raggiungerlo?
- Come adeguate la profondità della revisione al rischio della modifica senza aggiungere burocrazia?
- Dove la programmazione in coppia o in gruppo supera la revisione asincrona nel vostro contesto?
- Quanto ci si dovrebbe fidare della revisione assistita dall'IA, e per quali tipi di modifiche?
- Come mantenete costruttivo il feedback di revisione man mano che il team cresce e si diversifica?
- Come soddisfate i requisiti di approvazione per la conformità senza creare colli di bottiglia?

## Punti chiave

- Mantieni piccole e ben descritte le pull request; l'autore è responsabile della rivedibilità.
- Automatizza il meccanico così che le persone rivedano progetto, correttezza e test.
- Segui e gestisci la latenza di revisione come costo di flusso per tutto il team.
- Adegua la profondità della revisione al rischio della modifica e distingui i problemi bloccanti dalle preferenze.
- Usa programmazione in coppia, in gruppo e assistenza IA come complementi adatti al contesto, mantenendo una persona responsabile.

## Riferimenti e letture di approfondimento

- Karl Wiegers, *Peer Reviews in Software: A Practical Guide*
- Google, *Engineering Practices: How to Do a Code Review* (come esempio di riferimento)
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Kent Beck, *Extreme Programming Explained* (sulla programmazione in coppia)
- Woody Zuill, scritti sulla programmazione in gruppo
- Michael Lopp, *Managing Humans* (sulla collaborazione ingegneristica)
