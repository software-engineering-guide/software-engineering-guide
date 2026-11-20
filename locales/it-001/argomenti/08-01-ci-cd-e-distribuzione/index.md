# 8.1 CI/CD e distribuzione

## Panoramica e motivazioni

[Integrazione continua](https://en.wikipedia.org/wiki/Continuous_integration) e [consegna continua](https://en.wikipedia.org/wiki/Continuous_delivery) (CI/CD) sono il tessuto connettivo tra scrivere il codice e metterlo davanti agli utenti in sicurezza. Integrazione continua significa che ogni modifica è fusa di frequente in un ramo principale condiviso, poi costruita e testata automaticamente, così i problemi di integrazione emergono in pochi minuti anziché alla fine di un lungo ciclo di rilascio. Consegna continua significa che ogni modifica che supera la pipeline è mantenuta in uno stato distribuibile, così rilasciare in produzione diventa una decisione di business anziché una corsa ingegneristica. Il [deployment continuo](https://en.wikipedia.org/wiki/Continuous_deployment) va un passo oltre e rilascia automaticamente ogni modifica che passa, senza cancello umano.

Per i grandi team, queste distinzioni contano enormemente. Quando centinaia di ingegneri fanno commit su sistemi sovrapposti, il costo dell'integrazione manuale e dei test manuali cresce in modo non lineare. Una pipeline condivisa e automatizzata è l'unico modo pratico di dare a molti contributori un riscontro rapido e affidabile e di impedire che la modifica di un team rompa in silenzio quella di un altro. La pipeline diventa l'unica fonte di verità sul fatto che il software sia sano e fa rispettare una coerenza che nessuna quantità di documentazione o di buone intenzioni può garantire su larga scala.

I contesti aziendali e governativi aggiungono un'ulteriore dimensione: verificabilità e controllo delle modifiche. Regolatori, responsabili della sicurezza e auditor hanno bisogno di evidenza che le modifiche siano state riviste, testate e approvate e che l'artefatto in esecuzione in produzione sia esattamente quello che è stato costruito e vagliato. Una pipeline CI/CD ben progettata trasforma questi obblighi di conformità da onere burocratico a sottoprodotto automatico del normale flusso di lavoro ingegneristico. Fatta bene, la distribuzione diventa insieme più rapida e più sicura, che è l'esito che conta di più per la leadership.

*Vedi anche:* capitolo 8.4 (platform engineering ed esperienza degli sviluppatori), capitolo 8.5 (automazione di test e processi) e capitolo 7.4 (analisi di prodotto e sperimentazione) per le pratiche di [feature flag](https://en.wikipedia.org/wiki/Feature_toggle) (interruttori di runtime che espongono funzionalità agli utenti senza ridistribuire) e di sperimentazione che la distribuzione progressiva (rilasciare una modifica gradualmente monitorando automaticamente le sue metriche di salute) abilita.

## Principi chiave

- Integra spesso modifiche piccole; i rami di lunga vita sono il nemico dell'integrazione continua.
- Costruisci l'artefatto una volta e promuovi lo stesso identico artefatto attraverso ogni ambiente.
- Fai della pipeline il cancello autorevole: se è verde, la modifica è rilasciabile; se è rossa, il lavoro si ferma finché non è corretta.
- Ottimizza senza sosta per un riscontro rapido così che gli sviluppatori restino nel flusso e i difetti siano colti mentre il contesto è fresco.
- Automatizza tutto ciò che si ripete, compresi test, scansioni di sicurezza, predisposizione e distribuzione.
- Tratta le definizioni della pipeline come codice sotto controllo di versione soggetto a revisione, non come configurazione da console a clic.
- Progetta rilasci sicuri e reversibili così che qualsiasi distribuzione possa essere annullata in fretta.
- Separa il deployment (installare il codice) dal rilascio (esporlo agli utenti) usando i feature flag.

## Raccomandazioni

### Progetta la pipeline come una serie di cancelli di qualità

Struttura la pipeline in fasi che progrediscono da economiche e veloci a costose e approfondite: prima compilazione e test unitari, poi test di integrazione, scansioni di sicurezza e di licenze e infine distribuzione in staging e produzione. Ogni fase è un cancello che una modifica deve superare. Ordina i cancelli così che i controlli più veloci e più probabili da fallire girino per primi, il che dà agli sviluppatori il riscontro nel tempo più breve possibile. Mantieni il ciclo di riscontro della fase di commit sotto i dieci minuti ovunque tu possa. Oltre, gli sviluppatori cambiano contesto e la produttività cala.

### Costruisci una volta, promuovi ovunque

Produci un unico artefatto immutabile nella fase di build e promuovi esattamente quell'artefatto attraverso test, staging e produzione. Non ricostruire mai per ambiente, perché una ricostruzione può introdurre differenze in silenzio. La configurazione che varia per ambiente dovrebbe essere iniettata al momento della distribuzione, non incorporata in build separate. Questa pratica è anche ciò che ti permette di dire a un auditor, con certezza, che il binario in produzione è quello che ha superato ogni cancello.

### Fai della pipeline il punto di applicazione della politica

Codifica i controlli richiesti (approvazione della revisione del codice, soglie di copertura dei test, risultati delle scansioni di sicurezza, commit firmati) direttamente nella pipeline e nelle regole di protezione dei rami. La politica manuale che vive in un wiki viene aggirata di routine sotto la pressione delle scadenze. La politica codificata nella pipeline si applica in modo uniforme e automatico a ogni modifica.

### Mantieni il ramo principale sempre rilasciabile

Usa lo sviluppo trunk-based, che integra tutto il lavoro in un unico ramo condiviso con pochi o nessun ramo di lunga vita, oppure usa rami di funzionalità di breve vita e appoggiati ai feature flag per nascondere il lavoro incompleto anziché a rami di lunga vita. Questo mantiene piccoli i conflitti di merge e mantiene il ramo principale sempre in uno stato distribuibile, che è la precondizione per una vera consegna continua.

### Scegli deliberatamente le strategie di distribuzione

Adegua la strategia di distribuzione al rischio e al raggio d'impatto del servizio:

- Le distribuzioni **rolling** sostituiscono le istanze gradualmente e sono un predefinito sensato per i servizi senza stato.
- Il **[blue-green](https://en.wikipedia.org/wiki/Blue-green_deployment)** mantiene due ambienti identici e sposta il traffico tutto in una volta, dando un percorso di rollback istantaneo.
- I rilasci **canary** instradano una piccola percentuale di traffico alla nuova versione, osservano le metriche di salute ed espandono solo se i segnali sono buoni.
- I **feature flag** separano il rilascio dalla distribuzione, permettendoti di abilitare funzionalità per utenti o coorti specifici senza ridistribuire.

### Adotta la distribuzione progressiva con rollback automatico

La distribuzione progressiva combina i rilasci canary con l'analisi automatica di metriche come tasso di errore, latenza e saturazione. Definisci in anticipo criteri di salute oggettivi, poi lascia che il sistema promuova o ripristini automaticamente in base a quei segnali. Il rollback automatico rimuove l'esitazione umana che trasforma un piccolo incidente in uno grande.

### Fornisci gestione dei rilasci e controllo delle modifiche per gli ambienti regolamentati

Nei contesti regolamentati, tieni una registrazione di gestione delle modifiche leggera ma reale. Cattura automaticamente chi ha approvato ogni modifica, quali test sono girati e quale artefatto è stato distribuito. Usa processi di comitato per le modifiche per le modifiche davvero ad alto rischio, ma riservali a quei casi. Far passare ogni modifica di routine attraverso un comitato settimanale distrugge il valore dell'automazione. Punta invece a tipi di modifica standard e preapprovati che scorrano nella pipeline senza cerimonie.

## Compromessi: vantaggi e svantaggi

| Approccio | Vantaggi | Svantaggi | Adatto a |
|---|---|---|---|
| Consegna continua (cancello di rilascio manuale) | Il business controlla i tempi; forte per finestre di rilascio regolamentate | Richiede disciplina per mantenere rilasciabile il ramo principale | Imprese con finestre di modifica |
| Deployment continuo (completamente automatico) | Riscontro più rapido; lotti più piccoli | Richiede test e osservabilità maturi | Team ad alta fiducia e alta frequenza |
| Blue-green | Rollback istantaneo; modello mentale semplice | Raddoppia il costo dell'ambiente durante il passaggio | Servizi critici che richiedono un ritorno rapido |
| Canary + distribuzione progressiva | Limita il raggio d'impatto; guidato dai dati | Complesso da costruire; richiede buone metriche | Sistemi rivolti agli utenti su larga scala |
| Feature flag | Separa il deployment dal rilascio | Debito dei flag se non ripuliti | Team che rilasciano lavoro incompleto in sicurezza |

Il compromesso centrale è velocità contro controllo, ma spesso è una falsa scelta. Un'automazione matura dà entrambi: i rilasci sono più rapidi perché sono più piccoli e più sicuri perché ognuno è verificato e reversibile. Il vero costo è l'investimento iniziale in copertura dei test, osservabilità e ingegneria della pipeline, più la disciplina continua per mantenerli in salute. Le organizzazioni che lesinano su quell'investimento ottengono la velocità senza la sicurezza, il che è peggio di un lento processo manuale.

## Domande da discutere con il tuo team

1. **Qual è il vostro obiettivo di tempo di riscontro della fase di commit e che cosa si taglia quando la suite supera i dieci minuti?** Una fase di commit lenta uccide in silenzio l'integrazione continua, perché gli sviluppatori smettono di aspettare il verde e cominciano ad accumulare modifiche. Decidete ora il numero (questo capitolo sostiene meno di dieci minuti) e decidete il meccanismo per mantenerlo: worker paralleli, una rigorosa piramide dei test e lo spostamento dei lenti controlli di integrazione in una fase successiva. Alla scala aziendale questa è una decisione di piattaforma, poiché centinaia di ingegneri condividono la stessa pipeline e ogni minuto aggiunto si moltiplica su ogni commit. Portate dati reali alla riunione: durata attuale della pipeline al p50 e al p95, i dieci test più lenti e quanto spesso la gente riesegue anziché aspettare. Se non sapete enunciare l'obiettivo e difenderlo con numeri, la vostra pipeline sta derivando verso un processo batch travestito da CI.

2. **Quale strategia di distribuzione usa ciascun servizio, e chi risponde di quella scelta?** Rolling, blue-green e canary non sono intercambiabili: scambiano in modo diverso costo, velocità di rollback e complessità e la scelta giusta dipende dal raggio d'impatto del servizio. Il blue-green compra un rollback istantaneo al prezzo di un ambiente raddoppiato durante il passaggio, il che vale la pena per un sistema di pagamenti ed è uno spreco per una dashboard interna. Il canary limita l'esposizione ma richiede buone metriche di salute e più ingegneria della pipeline. Per un patrimonio grande o regolamentato, lasciare questo all'abitudine di ciascun team produce un'incoerenza che emerge durante un incidente, quindi concordate predefiniti per fascia di servizio e registrate la decisione. Portate il vostro catalogo dei servizi ed etichettate ogni servizio con la sua strategia, il suo percorso di rollback e la persona che possiede quella scelta.

3. **Come provate che l'artefatto in produzione è esattamente quello che ha superato ogni cancello?** Costruire una volta e promuovere lo stesso artefatto è tutta la partita per la verificabilità e si rompe nel momento in cui qualcuno ricostruisce per ambiente o rattoppa una macchina in esecuzione. Nei contesti aziendali e governativi un auditor vi chiederà di ricondurre un binario in esecuzione al suo commit, alla sua revisione e alle sue approvazioni e volete che quella risposta richieda secondi, non una settimana. Decidete come lo fate rispettare: artefatti immutabili, immagini firmate, verifica della firma al momento della distribuzione e configurazione iniettata alla distribuzione anziché incorporata in build separate. Portate i divari attuali al tavolo, come qualsiasi fase che ricostruisce, qualsiasi percorso manuale di hotfix e qualsiasi punto in cui la configurazione biforca l'artefatto. La risposta determina se la vostra evidenza di conformità è un sottoprodotto della pipeline o una corsa manuale prima di ogni audit.

4. **Quando il ramo principale diventa rosso, che cosa si ferma davvero e come gestite i test instabili?** Una pipeline è un cancello autorevole solo se una build rossa ferma davvero il lavoro, eppure molte organizzazioni tollerano in silenzio un ramo principale rotto e un arretrato di fallimenti intermittenti, il che addestra gli sviluppatori a rieseguire finché diventa verde e a rilasciare sopra i fallimenti. Per un grande team questa putrefazione si compone, perché il test instabile ignorato di un team diventa la scusa di tutti per aggirare il cancello e la fiducia nella pipeline costa molto meno da mantenere che da ricostruire. Pesate le spinte in competizione: una rigorosa regola di fermare la linea protegge la qualità ma può bloccare centinaia di ingegneri per un singolo cattivo commit, mentre una politica indulgente preserva il throughput ed erode il cancello. Portate evidenza alla discussione: il vostro attuale tempo in rosso del ramo principale, il numero di test in quarantena o instabili, il tasso di riesecuzione e quanto spesso le modifiche vengono fuse nonostante un controllo fallito. Nei contesti aziendali e governativi, nominate chi possiede il triage dei test instabili e chi ha l'autorità di congelare i merge, perché un cancello che nessuno è responsabile di far rispettare è uno che gli auditor scopriranno essere stato scavalcato di routine.

5. **Qual è il vostro ciclo di vita dei feature flag, e chi è tenuto a ritirarli?** I flag sono ciò che permette di separare il deployment dal rilascio e nascondere il lavoro incompleto, ma ogni flag è un ramo nel vostro codice che non si ripulisce da solo e i flag non gestiti si accumulano in una complessità condizionale che nessuno osa toccare. In un patrimonio grande questo debito è pericoloso, perché un flag stantio può filtrare in silenzio una correzione di sicurezza o far passare in produzione percorsi di codice non testati e la persona che l'ha creato spesso è passata ad altro. Bilanciate la tensione: i flag vi hanno comprato una distribuzione incrementale e sicura, quindi l'obiettivo non è meno flag ma un ciclo di vita disciplinato con un responsabile, un'aspettativa di scadenza e strumenti che facciano emergere quelli stantii. Portate l'inventario attuale alla riunione: quanti flag sono attivi, quanto è vecchio il più vecchio, quali non hanno responsabile e se qualche flag di lunga vita funziona ormai come configurazione permanente che appartiene altrove. Per gli ambienti regolamentati, aggiungete chi può cambiare un flag in produzione e se quel cambiamento è registrato con lo stesso rigore di una distribuzione, poiché un cambio di flag è un rilascio anche quando la pipeline non gira mai.

6. **Dov'è il confine tra consegna continua con cancello umano e pieno deployment continuo, e chi fissa le soglie di rollback?** La consegna continua tiene una persona al controllo dei tempi di rilascio, il che si adatta a finestre di modifica statutarie e sistemi con alto raggio d'impatto, mentre il deployment continuo rilascia automaticamente ogni modifica che passa e richiede test, osservabilità e rollback automatico maturi per essere sicuro. Per un'organizzazione grande o regolamentata la risposta raramente è uniforme: il vostro sito di marketing può distribuire in modo continuo mentre il nucleo dei pagamenti mantiene un cancello umano documentato e tracciare quella linea per fascia di servizio previene sia attrito inutile sia automazione sconsiderata. Le considerazioni in competizione sono velocità e dimensione del lotto contro controllo e verificabilità, più il costo ingegneristico delle metriche di salute che il rollback automatico richiede. Portate l'evidenza: tasso di fallimento delle modifiche per servizio, tempo medio di ripristino, cadenza attuale dei rilasci e i segnali oggettivi (tasso di errore, latenza, saturazione) di cui vi fidereste per promuovere o ripristinare senza un umano. Nei contesti governativi e aziendali, legate ogni fascia a chi possiede le soglie di rollback e a chi approva qualsiasi passaggio da un rilascio filtrato alla piena automazione, così che la decisione sia deliberata anziché andare alla deriva.

## Lente settoriale

**Startup.** Appoggiati a una CI/CD gestita fin dal primo giorno: un runner ospitato, una pipeline, un'immagine immutabile e distribuzione automatica in staging al merge. Non costruire infrastruttura di pipeline che poi devi mantenere. I feature flag permettono a due o tre ingegneri di fondere in sicurezza lavoro a metà e di rilasciare più volte al giorno e un deploy in produzione con un clic più uno spegnimento rapido del flag è tutto il controllo delle modifiche che ti serve finché la scala non ne impone di più.

**Piccola impresa.** Senza un ingegnere di piattaforma o di rilascio dedicato, privilegia la pipeline che il tuo host dei sorgenti ti dà (Actions integrate o equivalente) e la sua strategia di distribuzione predefinita rispetto a qualsiasi cosa su misura. Imposta onestamente la scelta tra comprare e costruire: una pipeline gestita e una piattaforma di hosting con rollback integrato costano meno delle ore di ingegneria che una configurazione su misura consuma. Mantieni l'essenziale, cioè costruire una volta, promuovere lo stesso artefatto e un ripristino facile e salta il macchinario della distribuzione progressiva finché il volume non lo giustifica.

**Grande impresa.** Il problema centrale è la coerenza tra molti team: standardizza un modello di pipeline condiviso che fa rispettare revisione, scansioni, artefatti immutabili e firmati e strategie di distribuzione per fascia, così che la qualità non vari da team a team. Tratta le definizioni della pipeline come codice rivisto, cattura automaticamente l'evidenza del controllo delle modifiche e gestisci feature flag e soglie di rollback come risorse governate anziché l'abitudine privata di ciascun team. Il ritorno è una distribuzione più rapida ed evidenza di audit prodotta come sottoprodotto anziché una corsa trimestrale.

**Ente pubblico.** Regole di appalto, finestre di modifica statutarie e responsabilità pubblica plasmano la pipeline. Preferisci la consegna continua con un cancello di rilascio umano documentato alla piena automazione per i sistemi rilevanti, classifica il lavoro di routine come modifiche standard preapprovate e mantieni un percorso di rollback istantaneo (blue-green o canary automatico) per i servizi da cui i cittadini dipendono in finestre annuali ristrette. Assicurati che la pipeline registri chi ha approvato ogni modifica, quali test sono girati e quale artefatto è stato distribuito, così che gli obblighi di trasparenza e audit siano soddisfatti dal normale flusso di lavoro anziché da carte manuali.

## Esempi

**Startup.** Una startup SaaS di quattro persone mette su un'unica pipeline GitHub Actions che esegue i test unitari, costruisce una sola immagine Docker e distribuisce quella stessa immagine in staging automaticamente a ogni merge su main. Un deploy in produzione è un clic e i fondatori si appoggiano ai feature flag così da poter fondere lavoro a metà dietro un flag anziché tenere in vita un ramo per settimane. Quando un cattivo rilascio sfugge, spengono il flag in pochi secondi e correggono con calma, il che mantiene il loro minuscolo team a rilasciare più volte al giorno senza una persona dedicata alle operazioni.

**Grande impresa.** Una banca globale consolida decine di job Jenkins specifici dei team in un modello di pipeline standardizzato che ogni team di prodotto eredita. Il modello fa rispettare analisi statica, scansione delle dipendenze e un artefatto firmato e immutabile e distribuisce con canary e rollback automatico legato a soglie di tasso di errore e latenza. Poiché lo stesso artefatto è promosso dal test alla produzione e ogni cancello è registrato, gli auditor della banca possono ricondurre qualsiasi binario di produzione al suo commit, alla sua revisione e alla sua approvazione in pochi secondi, sostituendo un esercizio trimestrale manuale di raccolta delle evidenze.

**Ente pubblico.** Un'amministrazione fiscale nazionale che modernizza un sistema di dichiarazione adotta la consegna continua con un esplicito cancello di rilascio umano, così da rispettare le finestre di modifica statutarie durante la stagione delle dichiarazioni. Le modifiche di routine sono classificate come modifiche standard preapprovate che scorrono automaticamente in staging. Il rilascio in produzione richiede una singola approvazione documentata che la pipeline registra. La distribuzione blue-green dà all'amministrazione un percorso di rollback istantaneo se un difetto raggiunge la produzione, il che è critico quando milioni di cittadini dipendono dal servizio in una stretta finestra annuale.

## Business case: motivazioni, ROI e TCO

Il ritorno dell'investimento in CI/CD compare come ridotto tempo di consegna delle modifiche, minore tasso di fallimento delle modifiche e ripristino più rapido quando avvengono incidenti: le metriche che la ricerca collega costantemente sia alle prestazioni di consegna sia agli esiti organizzativi. Rilasci più rapidi e più piccoli tagliano l'onere di coordinamento che consuma capacità ingegneristica su larga scala e la verifica automatica taglia il lavoro costoso e demoralizzante di fronteggiare i difetti di produzione.

Il costo totale di proprietà pesa il costo di adozione contro il costo del non adottare. I costi di adozione comprendono costruire e mantenere le pipeline, far crescere la copertura dei test e investire in osservabilità e personale di piattaforma. Il costo del non adottare è maggiore ma meno visibile: rilasci manuali lenti, dolore di integrazione, incidenti di produzione che danneggiano la reputazione e, nei contesti regolamentati, audit falliti e rimedi. Per la leadership, l'argomento si presenta meglio in termini di riduzione del rischio e capacità. L'automazione converte il prezioso tempo degli ingegneri senior dalla fatica ripetitiva dei rilasci in lavoro di prodotto, rendendo le interruzioni più rare e più brevi.

## Antipattern e insidie

- **Pipeline snowflake.** Ogni team costruisce a mano una pipeline unica, così miglioramenti e correzioni non possono essere condivisi e la qualità varia enormemente.
- **Ricostruire per ambiente.** Ricostruire a ogni fase rompe la garanzia "costruisci una volta" e lascia che sottili differenze raggiungano la produzione.
- **Build rosse ignorate.** Tollerare un ramo principale persistentemente rotto distrugge la fiducia nella pipeline e normalizza il rilasciare sopra i fallimenti.
- **Test instabili lasciati irrisolti.** I fallimenti intermittenti addestrano gli sviluppatori a rieseguire finché diventa verde, vanificando lo scopo del cancello.
- **Teatro dell'approvazione manuale.** Un comitato per le modifiche che timbra tutto aggiunge ritardo senza aggiungere sicurezza.
- **Debito dei flag.** I feature flag mai rimossi si accumulano in una complessità condizionale non mantenibile.
- **Deploy uguale rilascio.** Accoppiare i due significa che ogni modifica rivolta agli utenti richiede una ridistribuzione rischiosa.

## Modello di maturità

**Livello 1: Avvio.** Build e distribuzioni sono in gran parte manuali, ad hoc e reattive. L'integrazione avviene tardi, i rilasci sono rari e stressanti, il rollback significa ridistribuire a mano una vecchia versione e non c'è una nozione condivisa di cancello della pipeline.

**Livello 2: Sviluppo.** Build automatiche e test unitari girano a ogni commit, ma le pratiche variano da team a team. Le distribuzioni sono scriptate ma ancora avviate e supervisionate a mano, alcuni ambienti sono coerenti e gli artefatti possono ancora essere ricostruiti a ogni fase. Dove esiste una pipeline, è spesso uno snowflake che non può essere condiviso.

**Livello 3: Standardizzazione.** Un modello di pipeline documentato e standardizzato è fatto rispettare tra i team. Promuove un singolo artefatto immutabile attraverso tutti gli ambienti, applica cancelli automatici di qualità e sicurezza, codifica controlli richiesti come l'approvazione della revisione e i risultati delle scansioni e cattura automaticamente le registrazioni delle modifiche. Strategie di distribuzione come canary o blue-green sono scelte deliberatamente per fascia di servizio.

**Livello 4: Gestione.** La distribuzione è misurata e controllata rispetto a valori di riferimento. L'organizzazione segue tempo di consegna delle modifiche, frequenza di distribuzione, tasso di fallimento delle modifiche e tempo medio di ripristino, insieme a durata della pipeline al p50 e al p95, tassi di test instabili e di riesecuzione ed età dei feature flag. Le soglie di rollback sono fissate da dati osservati di tasso di errore, latenza e saturazione, i cancelli sono fatti rispettare sull'evidenza anziché sull'abitudine e ogni metrica ha un responsabile che agisce quando devia dall'obiettivo.

**Livello 5: Orchestrazione.** La distribuzione migliora continuamente ed è integrata nell'organizzazione. La distribuzione progressiva con rollback automatico guidato dalle metriche è la norma, il rilascio è separato dal deployment tramite flag ben governati e l'evidenza di conformità è prodotta automaticamente come sottoprodotto. La pipeline si adatta al mutare del patrimonio e le metriche di distribuzione alimentano la pianificazione di business e di rischio così che l'investimento fluisca verso i miglioramenti a più alta leva.

## Spunti di discussione

- Dov'è il giusto confine tra consegna continua con un cancello umano e pieno deployment continuo per i vostri sistemi più critici?
- Come mantenete significativo un processo obbligatorio di gestione delle modifiche senza trasformarlo in teatro del timbro?
- Quali metriche di salute oggettive dovrebbero governare il rollback automatico e chi possiede le loro soglie?
- Come dovrebbero i team di piattaforma bilanciare modelli di pipeline standardizzati e le legittime esigenze dei team con requisiti insoliti?
- Qual è la vostra politica e il vostro strumento per ritirare i feature flag prima che diventino debito?
- Come misurate se una distribuzione più rapida sta davvero migliorando gli esiti di business anziché limitarsi a rilasciare di più?

## Punti chiave

- CI, CD e deployment continuo sono distinti; scegli il livello di automazione che corrisponde alla tua tolleranza al rischio e alla tua maturità.
- Costruisci l'artefatto una volta e promuovi lo stesso identico artefatto attraverso ogni ambiente.
- Progetta la pipeline come cancelli di qualità ordinati e ottimizzati per un riscontro rapido e trattala come la decisione autorevole di rilascio.
- Scegli deliberatamente le strategie di distribuzione e adotta la distribuzione progressiva con rollback automatico per limitare il raggio d'impatto.
- Separa il rilascio dal deployment con i feature flag e gestisci il debito dei flag.
- Negli ambienti regolamentati, cattura l'evidenza del controllo delle modifiche automaticamente anziché con carte manuali.

## Riferimenti e letture di approfondimento

- Jez Humble e David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*.
- Nicole Forsgren, Jez Humble e Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Gene Kim, Jez Humble, Patrick Debois e John Willis, *The DevOps Handbook*.
- Gene Kim, Kevin Behr e George Spafford, *The Phoenix Project*.
- Betsy Beyer, Chris Jones, Jennifer Petoff e Niall Richard Murphy (a cura di), *Site Reliability Engineering*.
- Pete Hodgson, "Feature Toggles (Feature Flags)" (saggio).
- ITIL (Information Technology Infrastructure Library), indicazioni sulla gestione delle modifiche.
