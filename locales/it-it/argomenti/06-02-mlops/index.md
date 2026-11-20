# 6.2 Ingegneria dell'apprendimento automatico (MLOps)

## Panoramica e motivazioni

L'ingegneria dell'apprendimento automatico, di solito chiamata [MLOps](https://en.wikipedia.org/wiki/MLOps), è la disciplina di portare l'[apprendimento automatico](https://en.wikipedia.org/wiki/Machine_learning) fuori dai taccuini e dagli esperimenti e dentro sistemi di produzione affidabili, osservabili e manutenibili. Il software tradizionale si comporta come dice il suo codice. Un sistema di ML si comporta come dicono insieme il suo codice, i suoi dati e i parametri appresi del suo modello. Questo rende i sistemi di ML più difficili da testare, più difficili da riprodurre e inclini a fallire in silenzio man mano che il mondo si allontana dai dati su cui sono stati addestrati. L'MLOps porta il rigore dell'ingegneria del software (controllo di versione, test, consegna continua e monitoraggio) a questa realtà in tre parti di codice più dati più modelli.

Per i grandi team, l'MLOps è ciò che separa un modello una tantum che abbaglia in una dimostrazione da una flotta di modelli che molti team possono costruire, distribuire e gestire in sicurezza. Senza piattaforme e pratiche condivise, ogni team reinventa pipeline di dati, cicli di addestramento e rilascio e finisci con sistemi fragili che nessuno sa riprodurre sei mesi dopo. Le imprese si affidano all'MLOps per scalare su decine di modelli, rispettare gli obiettivi di livello di servizio e soddisfare gli auditor che chiedono come sia stata prodotta una data previsione.

Negli enti pubblici e nei settori regolamentati, l'MLOps è spesso un requisito di conformità sotto mentite spoglie. Riproducibilità, lignaggio e versionamento sono ciò che permette a un'agenzia di rispondere a una domanda giuridicamente significativa: esattamente quale modello, addestrato su quali dati, con quale codice, ha prodotto la decisione che ha colpito un cittadino? Una pratica MLOps matura mantiene quella domanda rispondibile anni dopo, il che è sia buona ingegneria sia una salvaguardia legale.

*Vedi anche:* il capitolo 8.1 (CI/CD e consegna), il capitolo 9.2 (osservabilità e monitoraggio) e il capitolo 6.6 (infrastruttura e operazioni per l'IA).

## Principi chiave

- Tratta dati, codice e modelli come artefatti versionati congiuntamente; cambiarne uno cambia il comportamento del sistema.
- Automatizza il percorso da dati a modello addestrato a rilascio così che sia ripetibile e verificabile.
- Rendi ogni modello riconducibile ai dati, al codice e alla configurazione esatti che lo hanno prodotto.
- Valuta i modelli su dati rappresentativi tenuti da parte prima del rilascio e continua a valutarli dopo.
- Presumi che i modelli degradino; monitora la deriva (la graduale divergenza dei dati dal vivo o delle relazioni input-output da ciò su cui il modello è stato addestrato), i problemi di qualità dei dati e il decadimento delle prestazioni fin dal primo giorno.
- Preferisci pipeline noiose e riproducibili a esperimenti ingegnosi e irriproducibili.
- Separa le preoccupazioni di velocità di sperimentazione e affidabilità di produzione e collegale deliberatamente.

## Raccomandazioni

### Gestisci esplicitamente l'intero ciclo di vita del ML

Definisci e strumenta ogni fase: acquisizione e convalida dei dati, [ingegneria delle feature](https://en.wikipedia.org/wiki/Feature_engineering), addestramento, valutazione, rilascio e monitoraggio. Rendi espliciti i confini tra le fasi così che ciascuna possa essere testata, ripetuta e verificata. Evita il fallimento comune in cui un modello è addestrato in un taccuino ad hoc e gettato oltre il muro alle operazioni. Avvolgi invece il ciclo di vita in una pipeline orchestrata che qualsiasi ingegnere autorizzato possa eseguire da un checkout pulito.

### Usa feature store, tracciamento degli esperimenti e registri dei modelli

Un **feature store** centralizza le definizioni delle feature così che le stesse trasformazioni girino sia in addestramento sia in erogazione. Questo elimina il training-serving skew (incoerenze tra come le feature sono calcolate per l'addestramento rispetto alle previsioni dal vivo) e permette ai team di riusare le feature anziché ricalcolarle. Il **tracciamento degli esperimenti** registra i parametri di ogni esecuzione di addestramento, la versione del codice, la versione dei dati e le metriche, così che i risultati siano confrontabili e riproducibili. Un **registro dei modelli** è il sistema di registrazione dei modelli addestrati, che tiene versioni, lignaggio, risultati di valutazione, stato di approvazione e fase di rilascio. Insieme, questi ti permettono di rispondere a "che cosa è cambiato?" quando il comportamento si sposta e di promuovere o ripristinare i modelli attraverso fasi governate.

### Rendi riproducibili e versionati dati e modelli con lignaggio

Versiona i tuoi insiemi di dati, non solo il tuo codice. Usa archiviazione indirizzabile per contenuto o strumenti di versionamento dei dati così che un'esecuzione di addestramento faccia riferimento a un'istantanea immutabile. Fissa il codice con i commit git e gli ambienti con dipendenze bloccate e immagini di container. Cattura il lignaggio da capo a capo: quali dati grezzi hanno alimentato quali feature, quali feature e quale codice hanno prodotto quale modello e dove quel modello è distribuito. Quando arriva un incidente o un audit, il lignaggio trasforma un incubo forense in una semplice query. Registra la casualità (seed) e l'hardware ovunque i risultati ne dipendano.

### Scegli gli schemi di rilascio in base al carico di lavoro

- Il punteggio **batch** gira con una pianificazione su grandi insiemi di dati; il più semplice da gestire, tollerante alla latenza, ideale per rapporti e decisioni periodiche.
- L'erogazione **online (in tempo reale)** risponde a singole richieste entro stretti budget di latenza; richiede un recupero delle feature a bassa latenza e un'attenta pianificazione della capacità.
- Lo **streaming** assegna punteggi agli eventi in continuo man mano che arrivano; adatto al rilevamento delle frodi e al monitoraggio dove la freschezza è critica.
- L'**edge** esegue i modelli su dispositivi o hardware on-premises per ragioni di latenza, privacy, connettività o sovranità dei dati, comune nei contesti governativi e sul campo.

Scegli lo schema più semplice che soddisfa il requisito e progetta il tuo rilascio con rilasci in ombra, canary e ripristino istantaneo.

### Monitora deriva, degrado e qualità dei dati

Strumenta input e output in produzione. Osserva la **deriva dei dati** (distribuzioni di input che si spostano), la **[deriva del concetto](https://en.wikipedia.org/wiki/Concept_drift)** (la relazione tra input e obiettivo che cambia), i fallimenti di **qualità dei dati** (valori nulli, modifiche di schema, fonti a monte rotte) e il **degrado delle prestazioni** misurato rispetto a una verità di riferimento ritardata dove ce l'hai. Fissa soglie di allarme, scrivi runbook e collega il monitoraggio ai tuoi inneschi di riaddestramento. Il degrado silenzioso è la classica modalità di fallimento del ML e il monitoraggio è la tua unica difesa.

## Compromessi: vantaggi e svantaggi

| Decisione | Opzione A | Opzione B | Compromesso |
|---|---|---|---|
| Schema di erogazione | Batch | Online | Semplicità e costo contro freschezza e latenza |
| Calcolo delle feature | Feature store | Pipeline per modello | Coerenza e riuso contro onere iniziale |
| Piattaforma | Comprare una piattaforma MLOps gestita | Assemblare strumenti open source | Velocità e supporto contro flessibilità e lock-in |
| Riaddestramento | Pianificato | Innescato dalla deriva | Prevedibilità contro reattività e complessità |
| Rigore di riproducibilità | Versionamento completo dei dati | Tracciamento leggero | Forza dell'audit contro archiviazione e sforzo |

Il compromesso generale è investimento ora contro fragilità dopo. Una pesante infrastruttura di riproducibilità e monitoraggio costa sforzo iniziale, ma previene il costo molto più grande di fallimenti inspiegabili, modelli irriproducibili e fiducia erosa. Le piattaforme gestite accelerano i team ma possono creare lock-in; gli stack open source offrono controllo al prezzo di lavoro di integrazione. Le grandi organizzazioni di solito traggono beneficio da un team di piattaforma condiviso che nasconde questa complessità dietro valori predefiniti da strada asfaltata.

## Domande da discutere con il tuo team

1. **Come verremmo a sapere che un modello distribuito è degradato in silenzio prima che un cliente o un cittadino ne sia danneggiato, e chi possiede quell'allarme?** Il decadimento silenzioso è la classica modalità di fallimento del ML: il codice gira ancora, il modello restituisce ancora punteggi sicuri e la qualità scivola man mano che il mondo deriva dai dati di addestramento. Per un grande team che gestisce molti modelli, ti serve questa risposta per modello, non una volta per la flotta, perché ciascuno ha il proprio profilo di deriva e il proprio ritardo della verità di riferimento. Porta i tuoi attuali monitor per deriva dei dati, deriva del concetto e rotture di qualità dei dati, le soglie di allarme e il runbook che dice chi risponde. Nei contesti regolamentati in cui le etichette arrivano con settimane di ritardo, discuti i segnali sostitutivi che puoi osservare nel frattempo, perché aspettare la verità di riferimento ritardata significa aspettare di scoprire il danno. Se nessun responsabile unico è nominato per l'allarme di deriva di un modello, quel modello è di fatto non monitorato.

2. **Se un auditor ci chiedesse di riprodurre una specifica previsione di diciotto mesi fa, potremmo davvero farlo da capo a capo?** La riproducibilità è il requisito di conformità nascosto dentro la buona ingegneria: permette a un'agenzia di rispondere esattamente a quale modello, addestrato su quali dati, con quale codice, ha prodotto una decisione che ha colpito qualcuno. Porta un esempio reale e prova a ricostruirlo: l'istantanea immutabile dei dati, il commit git, le dipendenze bloccate e l'immagine di container, i seed registrati e il lignaggio dai dati grezzi attraverso le feature al modello distribuito. Il segnale è se qualche anello di quella catena manca o è manuale. Per gli enti pubblici e i settori regolamentati, decidi il periodo di conservazione che la legge richiede davvero e conferma che la tua archiviazione mantenga il lignaggio rispondibile per l'intera finestra, poiché un divario trasforma una query di routine in un'emergenza forense.

3. **Qual è la nostra regola per promuovere un modello in produzione e ripristinarlo, ed è fatta rispettare dal registro o solo dalla fiducia?** La promozione non governata è come gli esperimenti da taccuino filtrano in produzione e come un cattivo modello indugia perché nessuno può ripristinarlo in modo pulito. Per molti team, la differenza tra maturo e fragile è se il registro dei modelli filtra la promozione con approvazione e valutazione obbligatorie, o se un ingegnere può spingere i pesi a mano. Porta il tuo attuale percorso di promozione, il tuo meccanismo di ripristino e l'evidenza che rilasci in ombra o canary girano davvero prima del traffico pieno. Discuti se il riaddestramento è pianificato o innescato dalla deriva e se i modelli riaddestrati superano cancelli di convalida prima del rilascio, perché riaddestrare su dati dal vivo senza convalida amplifica la deriva o l'avvelenamento. La risposta dovrebbe essere fatta rispettare nella piattaforma, non in una pagina wiki che si confida le persone seguano.

4. **Costruiamo la nostra piattaforma MLOps su strumenti open source, ne compriamo una gestita o mescoliamo i due, e chi ha pesato il lock-in?** Questa scelta fissa il tetto di quanto in fretta ogni futuro modello viene rilasciato e di quanto controllo mantieni su dati e pipeline. Una piattaforma gestita porta i team in produzione in fretta e si fa carico del supporto, ma può intrappolare le tue definizioni di feature, i registri di lignaggio e gli artefatti dei modelli in un formato proprietario che non puoi lasciare facilmente; uno stack open source assemblato ti mantiene portabile al prezzo di vero lavoro di integrazione e manutenzione. Porta il costo totale di proprietà per ciascun percorso (licenza o costruzione, archiviazione, calcolo per il riaddestramento e il personale di piattaforma per gestirlo), una lettura onesta della capacità del tuo team di gestire infrastruttura e un test di uscita concreto: potresti esportare registro, feature store e lignaggio e ricostruire altrove? Nei contesti aziendali e governativi, aggiungi vincoli di appalto e regole di sovranità dei dati, poiché una piattaforma che archivia dati di addestramento in una regione o in un formato che il tuo regolatore vieta è squalificata per quanto comoda.

5. **Il nostro feature store e il registro dei modelli dovrebbero essere un'unica piattaforma centralizzata o federati per team, e quanto ci costa oggi il training-serving skew?** Centralizzare le definizioni delle feature elimina lo skew in cui una feature è calcolata in un modo in addestramento e in un altro in erogazione, che è una fonte silenziosa e costosa di perdita di accuratezza, ma una singola piattaforma può diventare un collo di bottiglia che rallenta ogni team. Federare dà autonomia ai team moltiplicando l'impianto e le possibilità che due team definiscano la stessa feature in modo incoerente. Porta l'evidenza di dove lo skew ti ha già morso, quanti team riusano le feature rispetto a ricostruirle e i valori predefiniti da strada asfaltata che un team di piattaforma condiviso potrebbe offrire. Per una grande organizzazione, pesa il beneficio di governance di un unico sistema di registrazione verificabile contro il costo di consegna di una coda centrale e nei contesti regolamentati privilegia il lignaggio centralizzato che permette a un auditor di ricondurre qualsiasi previsione al codice esatto delle feature che l'ha prodotta.

6. **Abbiamo adeguato lo schema di rilascio di ciascun modello alle sue reali esigenze di latenza, freschezza e sovranità, o abbiamo impostato tutto a un'unica forma?** Batch, online, streaming ed edge portano ciascuno costo operativo e complessità molto diversi e scegliere quello sbagliato o spende troppo in infrastruttura in tempo reale di cui un rapporto notturno non aveva mai bisogno o affama un punteggiatore di frodi della freschezza da cui dipende. Decidi per carico di lavoro quale schema il requisito giustifica davvero e resisti a standardizzare sull'opzione più complessa perché sembra moderna. Porta il budget di latenza, il volume, il costo di una risposta vecchia e il ritardo della verità di riferimento per ciascun modello. Nei contesti governativi e sul campo, pesa deliberatamente edge e on-premises, perché le regole di sovranità dei dati o una connettività intermittente possono forzare i modelli su hardware locale e quella scelta rimodella come versioni, monitori e ripristini ogni modello che vi spingi.

## Lente settoriale

**Startup.** La tua risorsa più scarsa è l'attenzione ingegneristica, quindi tieni leggero l'MLOps e compralo. Segui gli esperimenti in un semplice strumento ospitato, fissa ogni modello distribuito alla sua istantanea di dati di addestramento e al commit del codice in git e aggiungi un controllo di deriva economico anziché una piattaforma. Salta il feature store e le pipeline su misura finché un secondo o terzo modello non rende valido il riuso; uno stack fragile che non puoi mantenere ti affonderà più in fretta di una capacità mancante.

**Piccola impresa.** Probabilmente non hai uno specialista di piattaforma ML e hai un budget ridotto, quindi tratta l'MLOps come qualcosa integrato negli strumenti che già gestisci anziché un sistema per cui dotare di personale. Preferisci un servizio gestito che si occupi per te di versionamento, rilascio e monitoraggio e imposta la disciplina come questione di igiene dei dati e riproducibilità: sappi quale modello e quali dati hanno prodotto un dato risultato e mantieni la capacità di ripristinare. Privilegia i fornitori che ti lasciano esportare i tuoi dati e modelli così che un successivo cambio resti possibile.

**Grande impresa.** Il problema è la scala su decine di modelli e molti team: un feature store condiviso, tracciamento degli esperimenti e un registro dei modelli con promozione governata così che i gruppi smettano di reinventare le pipeline. Metti a bilancio un team di piattaforma che offra valori predefiniti da strada asfaltata, standardizza lignaggio e monitoraggio così che ogni modello sia verificabile e ogni incidente spiegabile e gestisci deliberatamente costruire contro comprare e il lock-in dietro un'interfaccia che mantiene sostituibili gli strumenti sottostanti. Fai rispettare cancelli di convalida e ripristino nella piattaforma, non per convenzione.

**Ente pubblico.** Riproducibilità, lignaggio e versionamento sono requisiti di conformità sotto mentite spoglie, quindi trattali come di prim'ordine fin dal primo giorno. Versiona l'esatto insieme di dati e il codice dietro ogni modello distribuito, conserva quel lignaggio per il periodo richiesto per legge e sii in grado di riprodurre qualsiasi previsione storica che abbia colpito un cittadino. Tieni un umano a rivedere le decisioni rilevanti, pesa edge e on-premises dove le regole di sovranità dei dati lo richiedono ed esigi che qualsiasi piattaforma di un fornitore conceda piena portabilità di dati, feature e lignaggio.

## Esempi

**Startup.** Una piccola startup di analisi ha rilasciato il suo primo modello di previsione dell'abbandono con un data scientist e una configurazione leggera. Ha seguito gli esperimenti in un semplice strumento ospitato, fissato ogni modello distribuito alla sua istantanea di dati di addestramento e al commit del codice in git e aggiunto un semplice lavoro settimanale che confrontava gli input recenti con la distribuzione di addestramento. Quando una fonte di dati ha cambiato il formato della data e le previsioni hanno cominciato a derivare, quel semplice controllo l'ha colto in giorni anziché dopo una telefonata furiosa di un cliente e il team ha potuto riprodurre l'ultimo buon modello e ripristinare.

**Grande impresa.** Una banca al dettaglio gestisce decine di modelli di credito e frodi. Ha standardizzato su un feature store condiviso tra i team, un servizio di tracciamento degli esperimenti e un registro dei modelli con cancelli di approvazione obbligatori. Ogni modello in produzione risale alla sua istantanea di dati di addestramento e al commit del codice. I modelli di frode sono distribuiti come punteggiatori in streaming; quelli di credito girano in batch. Uno strato di monitoraggio osserva la deriva degli input e dà allarme quando lo schema di una fonte di dati cambia, il che una volta ha colto un flusso a monte rotto prima che corrompesse le decisioni.

**Ente pubblico.** Un'agenzia di prestazioni pubbliche usa un modello di ML per dare priorità alle revisioni dei casi. Poiché quelle decisioni toccano l'accesso dei cittadini ai servizi, l'agenzia versiona l'esatto insieme di dati e il codice dietro ogni modello distribuito, conserva questo lignaggio per il periodo richiesto per legge e può riprodurre su richiesta qualsiasi previsione storica. I modelli sono distribuiti in batch con un umano che rivede i casi segnalati e un monitor di deriva impone una rivalutazione obbligatoria ogni volta che la popolazione in ingresso si sposta, così che il modello non sia mai applicato in silenzio fuori dalle condizioni per cui è stato convalidato.

## Business case: motivazioni, ROI e TCO

L'MLOps si ripaga trasformando esperimenti fragili in risorse affidabili. Il ROI viene da un più rapido tempo alla produzione per i nuovi modelli, meno costosi incidenti, meno infrastruttura duplicata e la capacità di gestire molti modelli con un piccolo team di piattaforma. Un feature store e un registro condivisi possono tagliare in modo drastico il tempo di consegna per modello, perché i team smettono di ricostruire lo stesso impianto.

Il TCO copre costruzione o licenza della piattaforma, archiviazione per dati e modelli versionati, calcolo per il riaddestramento e il personale per gestire il tutto. Pesalo contro il costo del non adottare: modelli che non puoi riprodurre né verificare, fallimenti silenziosi che danneggiano clienti o cittadini e rilievi normativi. Nei contesti regolamentati, il costo di un modello inspiegabile in un audit può far impallidire l'intero investimento MLOps. Presenta il caso alla leadership impostando l'MLOps come riduzione del rischio e accelerazione della consegna, non onere: una strada asfaltata che ogni futuro modello percorrerà.

## Antipattern e insidie

- **Salti dal taccuino alla produzione.** Rilasciare modelli addestrati in taccuini non governati senza riproducibilità.
- **Training-serving skew.** Codice delle feature diverso in addestramento e in erogazione, causando perdita silenziosa di accuratezza.
- **Nessun versionamento dei dati.** Versionare il codice ma non i dati, così le esecuzioni non possono essere riprodotte.
- **Rilascia e dimentica.** Rilasciare un modello senza monitoraggio, scoprendo il degrado solo quando gli utenti si lamentano.
- **Riaddestramento col pilota automatico.** Riaddestrare automaticamente su dati dal vivo senza convalida, amplificando deriva o avvelenamento.
- **Infrastruttura una tantum.** Ogni team che costruisce la propria pipeline, moltiplicando costo e fragilità.
- **Ignorare le etichette ritardate.** Presumere di poter misurare subito l'accuratezza quando la verità di riferimento arriva con settimane di ritardo.

## Modello di maturità

1. **Avvio.** Modelli costruiti ad hoc in taccuini; rilascio manuale; nessun versionamento di dati o modelli; nessun monitoraggio; riprodurre una previsione passata è tirare a indovinare.
2. **Sviluppo.** Compaiono un po' di tracciamento degli esperimenti e un registro dei modelli, ma le pratiche variano per team; il rilascio è semi-automatizzato; il monitoraggio di base copre alcuni modelli; il versionamento dei dati è parziale e il lignaggio ha divari.
3. **Standardizzazione.** Una piattaforma condivisa con feature store, registro, pipeline riproducibili e lignaggio da capo a capo è documentata e fatta rispettare nell'organizzazione; il monitoraggio di deriva e qualità dei dati gira su tutti i modelli; promozione e ripristino seguono un percorso governato che ogni team usa.
4. **Gestione.** La flotta è misurata rispetto a valori di riferimento: tassi di deriva, rotture di qualità dei dati, accuratezza dei modelli rispetto alla verità di riferimento ritardata, training-serving skew, tempo alla produzione e costo operativo per modello sono seguiti come metriche; soglie di allarme e cancelli di convalida sono fatti rispettare sull'evidenza e la salute di ogni modello è rivista con una cadenza fissa con un responsabile nominato.
5. **Orchestrazione.** Il ciclo di vita è completamente automatizzato, verificabile e adattivo; il riaddestramento innescato dalla deriva gira dietro cancelli di convalida; strade asfaltate self-service permettono ai team di rilasciare in sicurezza; la valutazione continua lega le prestazioni dei modelli alle metriche di business e la piattaforma si integra con consegna, rischio e conformità così che i modelli siano ritirati, sostituiti e ridefiniti di routine man mano che dati e condizioni cambiano.

## Spunti di discussione

- Come bilanciate la libertà di sperimentazione con la riproducibilità in produzione?
- Qual è il giusto innesco di riaddestramento (pianificazione, deriva o decadimento delle prestazioni) per i vostri casi d'uso?
- Per quanto tempo dovete conservare dati e lignaggio dei modelli, e che cosa guida quel requisito?
- Feature store e registri dovrebbero essere piattaforme centralizzate o federati per team?
- Come monitorate l'accuratezza quando le etichette della verità di riferimento arrivano con lunghi ritardi?
- Quando vale il suo costo l'aggiunta di complessità operativa del rilascio edge?

## Punti chiave

- Il comportamento del ML viene da codice più dati più modelli; versiona e governa tutti e tre insieme.
- Feature store, tracciamento degli esperimenti e registri sono la spina dorsale del ML riproducibile.
- Il lignaggio rende i modelli verificabili e gli incidenti spiegabili: essenziale nei contesti regolamentati.
- Scegli batch, online, streaming o edge per adattarti a esigenze di latenza, freschezza e sovranità.
- I modelli degradano; il monitoraggio di deriva, qualità dei dati e decadimento non è facoltativo.

## Riferimenti e letture di approfondimento

- Chip Huyen, *Designing Machine Learning Systems*.
- Andriy Burkov, *Machine Learning Engineering*.
- D. Sculley et al., *Hidden Technical Debt in Machine Learning Systems*.
- Mark Treveil et al., *Introducing MLOps*.
- Valliappa Lakshmanan, Sara Robinson e Michael Munn, *Machine Learning Design Patterns*.
- Emmanuel Ameisen, *Building Machine Learning Powered Applications*.
