# 6.1 Strategia e preparazione per l'IA

## Panoramica e motivazioni

L'[intelligenza artificiale](https://en.wikipedia.org/wiki/Artificial_intelligence) è passata da novità di ricerca a capacità centrale che le grandi organizzazioni sono ormai chiamate a distribuire in modo responsabile e su larga scala. Per le imprese e le agenzie governative, la vera domanda non è più se l'IA possa fare qualcosa di impressionante in una dimostrazione. È se uno specifico investimento risolve un problema reale meglio delle alternative, può essere gestito in sicurezza per anni e può sopravvivere ad audit, appalti e controllo pubblico. La strategia per l'IA è la disciplina di decidere dove applicare l'IA, dove evitarla e di quali fondamenta hai bisogno prima che il primo modello arrivi in produzione.

Per i grandi team, scala e inerzia alzano la posta. Un'iniziativa mal impostata può bruciare budget, distrarre ingegneri di talento ed erodere la fiducia di regolatori e cittadini quando fallisce in pubblico. Una ben scelta può automatizzare la routine, far emergere intuizioni da dati che non avresti mai potuto raggiungere prima e liberare persone competenti per lavoro di maggior valore. La differenza raramente è il modello stesso. Si riduce a quanto bene imposti il problema, quanto sono pronti i tuoi dati e il tuo talento e quanto è onesto il tuo business case.

I contesti governativi e regolamentati aggiungono altri vincoli. Gli enti pubblici devono giustificare la spesa, garantire trasparenza, evitare discriminazioni illecite ed essere responsabili davanti ai funzionari eletti e al pubblico. Le regole sugli appalti possono vietare il lock-in con un unico fornitore, esigere spiegabilità e richiedere che i fornitori espongano il comportamento del modello. Qui, tratta conformità, verificabilità e opzioni di uscita come requisiti di prim'ordine, non ripensamenti.

## Principi chiave

- Parti da un problema che vale la pena risolvere, non da una tecnologia in cerca di un uso.
- Preferisci l'approccio più semplice che soddisfa il bisogno; l'IA è un'opzione tra molte e spesso non la migliore.
- Tratta preparazione dei dati, talento e maturità della piattaforma come prerequisiti, non come filoni paralleli da sistemare dopo.
- Prendi esplicitamente le decisioni tra costruire e comprare e rivedile man mano che il mercato e le tue capacità cambiano.
- Quantifica il costo totale di proprietà, comprese operazione, monitoraggio ed eventuale sostituzione, non solo la licenza o il pilota.
- Progetta l'uscita fin dal primo giorno: evita architetture che rendono proibitivamente costoso cambiare fornitore o modello.
- Nei contesti regolamentati e pubblici, tratta trasparenza, conformità agli appalti e responsabilità come vincoli di progetto.
- Misura il costo del *non* agire accanto al costo dell'agire.

## Raccomandazioni

### Imposta il problema prima di scegliere una tecnologia

Scrivi un'enunciazione del problema di una pagina. Nomina la decisione o il compito che vuoi migliorare, il riferimento attuale, l'esito misurabile che vuoi e che cosa succede quando il sistema sbaglia. Poi chiediti se il problema si adatti affatto all'IA. Ci sono abbastanza dati rilevanti? Il compito è basato su schemi anziché su regole? Puoi tollerare risposte probabilistiche? Un umano può controllare l'output? Molti problemi sono risolti meglio con software deterministico, una migliore progettazione dei processi o semplicemente una migliore igiene dei dati. Scrivi esplicitamente dove l'IA *non* è adatta: per esempio, decisioni che per legge devono essere perfettamente spiegabili, o dove il costo di un raro errore è catastrofico e impossibile da cogliere.

### Usa un albero decisionale tra costruire, comprare, mettere a punto e fare prompt

Procedi dal più economico e rapido al più costoso e controllato:

1. **Fai prompt a un modello ospitato esistente.** Se un modello generico (come Claude di Anthropic, o offerte comparabili di altri fornitori) risolve il problema con un prompt accurato e il recupero, fai prima quello. Costo più basso, iterazione più rapida, nessuna infrastruttura di addestramento.
2. **Aumenta con recupero o strumenti.** Se il divario è conoscenza o azioni, aggiungi la [generazione aumentata dal recupero](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (RAG), che preleva documenti rilevanti al momento della query e li fornisce al modello come contesto, e l'uso di strumenti prima di toccare i pesi del modello.
3. **Metti a punto o adatta.** Se il prompting non può ottenere in modo coerente l'accuratezza, il tono o il formato necessari, esegui il [fine-tuning](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)) di un modello più piccolo sui tuoi dati: cioè addestra ulteriormente un modello preaddestrato sui tuoi esempi per specializzarlo. Compra controllo al costo di una pipeline [MLOps](https://en.wikipedia.org/wiki/MLOps) (machine learning operations).
4. **Compra un prodotto specializzato.** Per domini ben definiti (elaborazione di documenti, punteggio delle frodi), un prodotto maturo di un fornitore può battere qualsiasi cosa tu costruisca.
5. **Costruisci da zero.** Riserva l'addestramento di [modelli di fondazione](https://en.wikipedia.org/wiki/Foundation_model) (grandi modelli preaddestrati su dati ampi e adattabili a molti compiti) alle organizzazioni con dati unici, profondo talento e ragioni strategiche. Per quasi tutte le imprese e le agenzie, è la scelta sbagliata.

### Stabilisci prerequisiti di dati, talento e piattaforma

Verifica i tuoi dati per disponibilità, qualità, etichettatura, lignaggio e base giuridica d'uso. Conferma di avere davvero il diritto di usarli per l'IA, compresi eventuali dati personali o di terzi. Valuta onestamente il talento: ti servono data scientist e anche ingegneri ML, ingegneri dei dati, product manager che capiscano i sistemi probabilistici e revisori capaci di valutare gli output. Prima di scalare, metti in piedi una base di piattaforma: tracciamento degli esperimenti, un registro dei modelli (il sistema di registrazione delle versioni dei modelli addestrati e del loro stato di approvazione), monitoraggio ed erogazione sicura, così che ogni nuovo caso d'uso non reinventi le operazioni.

### Gestisci deliberatamente i contesti regolamentati e governativi

Coinvolgi presto appalti, legale e rischio. Richiedi ai fornitori di dichiarare provenienza del modello, pratiche sui dati di addestramento, risultati delle valutazioni e limiti noti. Preferisci contratti che concedano portabilità di dati e prompt ed evita formati proprietari che ti intrappolano. Dove opportuno, pubblica scopo e salvaguardie dei sistemi di IA rivolti al pubblico e dai alle persone un canale per contestare le decisioni automatizzate. Allineati a quadri riconosciuti (vedi capitolo 6.5) così che gli audit trovino un processo documentato e difendibile.

### Calcola il costo totale di proprietà e proteggiti dal lock-in

Modella il costo dell'intero ciclo di vita: inferenza o licenze, pipeline di dati, revisione umana, monitoraggio, riaddestramento, risposta agli incidenti e dismissione. Confrontalo con il costo dello stato attuale e delle alternative. Riduci il lock-in mettendo il modello dietro un'interfaccia interna, mantenendo portabili prompt e insiemi di dati di valutazione e provando di tanto in tanto un secondo fornitore.

## Compromessi: vantaggi e svantaggi

| Approccio | Vantaggi | Svantaggi | Ideale quando |
|---|---|---|---|
| Prompt a un modello ospitato | Veloce, economico, nessuna infrastruttura, facile da cambiare | Meno controllo, costo per chiamata, questioni di condivisione dei dati | Prototipi, compiti ampi, requisiti incerti |
| Aumento con recupero | Ancora le risposte ai tuoi dati, aggiornabile | La qualità del recupero è difficile, aggiunge infrastruttura | Compiti ricchi di conoscenza |
| Fine-tuning di un modello più piccolo | Controllo, costo per chiamata più basso su larga scala, opzione on-premises | Richiede MLOps, dati e manutenzione | Compiti stabili, ad alto volume e specializzati |
| Comprare un prodotto | Collaudato, supportato, rapido al valore | Costo di licenza, lock-in, adattamento limitato | Problemi di commodity ben definiti |
| Costruire un modello di fondazione | Massimo controllo e differenziazione | Costo enorme, talento raro, alto rischio | Quasi mai, fuori dai laboratori di frontiera |

Il compromesso dominante è controllo contro costo e velocità. Il prompting ti dà la massima velocità e flessibilità ma il minimo controllo; costruire ti dà il massimo controllo ma richiede risorse che poche organizzazioni dovrebbero spendere. La maggior parte dei grandi team dovrebbe vivere nel mezzo: prima prompt e recupero, fine-tuning in modo selettivo e comprare per i bisogni di commodity. Il lock-in scambia comodità a breve termine con rischio a lungo termine e conta soprattutto negli enti pubblici, dove sono comuni obblighi di uscita pluriennali.

## Domande da discutere con il tuo team

1. **Dove si colloca ciascuno dei nostri tre principali casi d'uso candidati sulla scala prompt, poi recupero, poi fine-tuning, poi acquisto, poi costruzione, e quale evidenza lo sposterebbe di un gradino?** Conta perché la maggior parte dello spreco di spesa in IA viene dal partire un gradino troppo in alto: addestrare un modello quando un prompt accurato avrebbe funzionato. Per un grande team, concordare la scala come valore predefinito condiviso impedisce a ciascun gruppo di reinventare una costosa pipeline. Porta l'enunciazione del problema di una pagina per ogni candidato, il riferimento attuale e una lettura onesta se il divario sia conoscenza (recupero), coerenza (fine-tuning) o una commodity risolta (acquisto). Nei contesti aziendali e governativi, aggiungi il costo di appalto e di audit di ogni gradino, poiché un modello messo a punto si trascina dietro un onere MLOps che una chiamata ospitata non ha. La risposta dovrebbe permetterti di uccidere o declassare almeno un progetto sovradimensionato nella stanza.

2. **Qual è il nostro piano di uscita concreto per il fornitore o il modello da cui dipendiamo di più, e l'abbiamo davvero testato?** Il lock-in è economico da accettare e costoso da sciogliere e negli enti pubblici puoi portare obblighi di uscita pluriennali che non puoi soddisfare se non hai mai provato. Porta l'elenco delle funzioni proprietarie su cui ti appoggi, se prompt e insiemi di dati di valutazione sono portabili e come il modello sta dietro un'interfaccia interna (o no). Il segnale da osservare è se qualcuno ha mai eseguito la tua suite di valutazione contro un secondo fornitore; se no, il tuo piano di uscita è una speranza, non un piano. Se la risposta onesta è che cambiare richiederebbe mesi e riscrivere codice centrale, trattalo come un difetto di progetto da correggere ora, non un ponte da attraversare dopo.

3. **Che cosa dice una scheda onesta di preparazione sui nostri diritti sui dati, e quali casi d'uso squalifica oggi?** Saltare la preparazione dei dati è il fallimento che affonda in silenzio i piloti: il modello funziona, ma non hai mai avuto la base giuridica per usare i dati, o sono privi di etichette e di lignaggio. Per una grande organizzazione, i dati personali e di terzi sollevano limiti di consenso e contrattuali che variano per giurisdizione e per insieme di dati. Porta un audit di disponibilità, qualità, etichettatura, lignaggio e base giuridica per ogni candidato e sii disposto a segnare alcuni casi d'uso come bloccati finché esistano le fondamenta dei dati. Nei contesti regolamentati e pubblici, una base giuridica inutilizzabile non è un ritardo, è un arresto netto e finanziare il lavoro di preparazione dovrebbe essere una voce esplicita del piano anziché un ripensamento.

4. **Come sapremo che un caso d'uso di IA in esercizio funziona davvero, e quale evidenza ce lo farebbe uccidere?** La maggior parte dei portafogli di IA accumula zombie: piloti che sono stati rilasciati, hanno impressionato qualcuno e ora girano per sempre senza che nessuno controlli se si guadagnano ancora il loro costo. Concorda il riferimento e la metrica di successo prima del lancio, poi fissa una soglia esplicita di chiusura, così che la decisione di fermarsi sia presa in anticipo anziché difesa sul momento. Porta la metrica attuale, il costo della supervisione umana per esito e la deriva che hai visto dal lancio. Per i portafogli aziendali e governativi, nomina chi rivede ogni sistema con una cadenza fissa e chi ha l'autorità di ritirarlo; un caso d'uso che nessuno è responsabile di rivedere è uno che nessuno spegnerà mai.

5. **Dove resta un umano nel ciclo, quanto costa quella supervisione e l'abbiamo davvero messa a bilancio?** I casi d'uso di IA dall'aspetto più economico sono quelli che presumono in silenzio la piena automazione, poi perdono costo attraverso la revisione, la correzione e l'escalation che la realtà rimette dentro. Decidi deliberatamente quali decisioni una persona deve confermare, quali il modello può prendere da solo e quali non può mai prendere, poi prezza il tempo umano che questo implica. Porta il volume dei casi a bassa confidenza, il costo di una risposta sbagliata e l'attuale percorso di escalation. Nei contesti regolamentati e pubblici, lega ogni decisione automatizzata a un funzionario responsabile e a una via di ricorso, perché una supervisione che non sai descrivere è una supervisione che non hai.

6. **Abbiamo il talento e la piattaforma per gestire ciò che proponiamo, o stiamo presumendo in silenzio una capacità che non abbiamo?** I piani ambiziosi di IA falliscono meno sul modello che sulle fondamenta poco glamour: nessuno che mantenga la pipeline, nessuno che sappia valutare gli output, nessuna piattaforma su cui distribuire. Abbina ogni caso d'uso candidato alle competenze e all'infrastruttura di cui ha davvero bisogno e sii onesto dove il divario è un'assunzione, un partner o una ragione per non costruire. Porta un inventario di chi può possedere ogni sistema in produzione, su quale piattaforma girerà e quali capacità dovresti comprare. Per un'organizzazione grande o pubblica, aggiungi i tempi di appalto e assunzione, poiché un piano che dipende da talento che non puoi reclutare nella finestra rilevante è un piano per consegnare meno.

## Lente settoriale

**Startup.** Dominano velocità e sopravvivenza. Scegli un caso d'uso ristretto che tocchi il tuo valore centrale, rilascialo su un modello ospitato dietro una sottile interfaccia e limita duramente la spesa. Evita di costruire infrastruttura o addestrare modelli: la tua risorsa più scarsa è l'attenzione ingegneristica e una pipeline di fine-tuning che non puoi mantenere è una passività, non un fossato. Tieni economico il cambio così da poter seguire un mercato in rapido movimento.

**Piccola impresa.** Probabilmente non hai data scientist e hai un budget ridotto, quindi tratta l'IA come qualcosa che compri integrato negli strumenti che già usi, non un programma per cui dotare di personale. Imposta la preparazione come una questione di igiene dei dati e di privacy anziché un progetto di apprendimento automatico: sappi quali dati dei clienti detieni, che cosa ti è permesso farne e dove una risposta automatica sbagliata ti costerebbe un cliente. Preferisci i fornitori che rendono l'IA facoltativa, trasparente e facile da spegnere.

**Grande impresa.** Il problema è la governance del portafoglio tra molti team: una scala condivisa tra costruire e comprare, valutazioni di preparazione coerenti e analisi di lock-in e costo totale così che i gruppi smettano di reinventare costose pipeline. Metti a bilancio esplicitamente l'onere di MLOps e supervisione umana, standardizza lo strato di interfaccia così che i fornitori restino sostituibili e gestisci i casi d'uso di IA come un portafoglio con metriche chiare e criteri di chiusura anziché una dispersione di piloti.

**Ente pubblico.** Trasparenza, regole sugli appalti e responsabilità plasmano ogni scelta. Privilegia sistemi che citano fonti ufficiali anziché generare politica, tieni un umano responsabile delle decisioni rilevanti ed esigi portabilità dei dati e dichiarazione dei limiti del modello nei contratti. Pubblica una descrizione in linguaggio semplice e una via di ricorso, onora gli eventuali obblighi di uscita pluriennali che firmi e tieni l'IA fuori dalle decisioni finali di valutazione che devono poggiare su un funzionario responsabile.

## Esempi

**Startup.** Una startup di pianificazione di cinque persone voleva aggiungere una funzionalità in linguaggio naturale "fissami una riunione" senza togliere i suoi due ingegneri dal prodotto centrale. Ha scelto il più piccolo problema che contasse, analizzare una richiesta in un orario proposto, e l'ha rilasciato con un modello ospitato dietro una sottile API interna così da poter cambiare fornitore più avanti. Il team ha fissato un tetto mensile rigido di spesa, ha seguito se gli utenti accettavano gli orari suggeriti e ha concordato di riconsiderare un modello messo a punto solo se il volume avesse mai giustificato il lavoro extra.

**Grande impresa.** Un'assicurazione multinazionale voleva accelerare lo smistamento dei sinistri. Anziché addestrare un modello su misura, ha impostato il problema in modo ristretto (instradare e riassumere i sinistri in arrivo), ha fatto un prototipo con un modello ospitato più recupero sui propri documenti di polizza e ha misurato rispetto a tempo e accuratezza della gestione umana. Solo dopo aver provato il valore ha messo a punto un modello più piccolo per il tipo di sinistro a più alto volume per tagliare il costo per chiamata. Ha tenuto il modello dietro un'API interna così da poter cambiare fornitore e ha modellato un TCO a tre anni che includeva la revisione umana dei casi a bassa confidenza.

**Ente pubblico.** Un'autorità fiscale nazionale ha considerato un assistente di IA per aiutare il personale a rispondere alle domande dei cittadini. Poiché quelle risposte toccavano obblighi legali, l'agenzia ha insistito sulla trasparenza: il sistema poteva solo far emergere indicazioni ufficiali con citazioni, mai inventare politica e un umano rivedeva ogni suggerimento automatico prima che partisse. Gli appalti hanno richiesto al fornitore di dichiarare i limiti del modello e di concedere la portabilità dei dati e l'agenzia ha pubblicato una descrizione in linguaggio semplice del sistema e una via di ricorso. Ha tenuto l'IA completamente fuori dalle decisioni finali di accertamento, riservandole ai funzionari responsabili.

## Business case: motivazioni, ROI e TCO

La strategia per l'IA esiste per aiutarti a evitare due fallimenti speculari: investire troppo in IA che non ripaga mai e investire troppo poco mentre i concorrenti o le agenzie pari avanzano. Il ROI viene da lavoro risparmiato, tempo di ciclo ridotto, tassi di errore abbassati e capacità nuove abilitate. Misurali rispetto a un riferimento genuino e scontali per il costo reale della supervisione umana, che raramente scompare.

Il TCO deve includere le voci poco glamour: pipeline di dati, monitoraggio, riaddestramento man mano che il mondo deriva, revisione di sicurezza ed eventuale dismissione. Un pilota che sembra economico può diventare costoso una volta che gira su larga scala per anni. Presenta anche il costo del *non* adottare: servizio più lento, costo manuale più alto e deriva strategica. Presenta il caso alla leadership con una vista di portafoglio: poche scommesse ad alta confidenza, metriche di successo chiare, criteri di chiusura per i fallimenti e una valutazione di preparazione che mostri che esistono le fondamenta di dati e talento. Chiedi ai leader di finanziare esplicitamente la preparazione; saltala e garantisci costose rilavorazioni.

## Antipattern e insidie

- **Soluzione in cerca di un problema.** Comprare l'IA perché l'hanno fatto i pari, poi cercare un caso d'uso.
- **Saltare la preparazione dei dati.** Lanciare modelli su dati non disponibili, non etichettati o legalmente inutilizzabili.
- **Decisioni guidate dalla dimostrazione.** Impegnarsi in base a una dimostrazione rifinita senza una valutazione di qualità da produzione.
- **Ignorare il ciclo umano.** Presumere la piena automazione e sotto-budgettare la revisione, che è dove si nasconde la maggior parte del costo.
- **Lock-in silenzioso.** Costruire a fondo sulle funzioni proprietarie di un fornitore senza piano di uscita.
- **Sottovalutare le operazioni.** Trattare il rilascio come il traguardo anziché l'inizio di un obbligo di manutenzione.
- **Conformità come ripensamento.** Adattare trasparenza e verificabilità dopo il progetto, a multipli del costo.

## Modello di maturità

1. **Avvio.** Esperimenti ad hoc, nessuna strategia condivisa, decisioni guidate da moda ed entusiasmo individuale.
2. **Sviluppo.** L'impostazione del problema esiste per alcuni progetti; compare una prima base di piattaforma; costruire contro comprare è discusso ma incoerente.
3. **Standardizzazione.** Un portafoglio di casi d'uso di IA con metriche chiare, un albero decisionale documentato, valutazioni di preparazione e analisi di lock-in e TCO, applicati in modo coerente tra i team.
4. **Gestione.** Il portafoglio è misurato: preparazione, ROI, TCO e costo della supervisione umana sono seguiti rispetto a valori di riferimento; i criteri di chiusura sono fatti rispettare sull'evidenza; impatto su consegna e qualità guidano ogni decisione di procedere o meno.
5. **Orchestrazione.** La strategia per l'IA è integrata con la pianificazione di business e rischio; la preparazione è mantenuta di continuo; l'organizzazione ritira, sostituisce e ridefinisce di routine i sistemi di IA sull'evidenza, riequilibrando il portafoglio al mutare di mercato e quadro di rischio.

## Spunti di discussione

- Come decidete quando un problema è davvero inadatto all'IA, e chi ha l'autorità di dire no?
- Quale soglia di preparazione dovrebbe filtrare un progetto dal pilota alla produzione?
- Quanto lock-in è accettabile in cambio di un più rapido tempo al valore?
- Negli enti pubblici, come dovrebbero gli obblighi di trasparenza plasmare la scelta tra costruire e comprare?
- Come mantenete oneste le stime di TCO quando fornitori ed entusiasti hanno incentivi a sottostimarle?
- Chi possiede il portafoglio di IA, e come sono prese le decisioni di chiusura?

## Punti chiave

- La strategia parte da un problema reale e da un riferimento onesto, non da una tecnologia.
- Preferisci l'opzione più semplice: prompt, poi recupero, poi fine-tuning, poi acquisto e raramente costruire da zero.
- Preparazione di dati, talento e piattaforma sono prerequisiti; finanziarla fa parte del piano.
- I contesti regolamentati e governativi richiedono per progetto trasparenza, conformità agli appalti e opzioni di uscita.
- Modella il TCO completo e il costo dell'inazione e proteggiti dal lock-in del fornitore fin dalla prima decisione architetturale.

## Riferimenti e letture di approfondimento

- Ajay Agrawal, Joshua Gans e Avi Goldfarb, *Prediction Machines: The Simple Economics of Artificial Intelligence*.
- Eric Siegel, *The AI Playbook: Mastering the Rare Art of Machine Learning Deployment*.
- Andriy Burkov, *The Hundred-Page Machine Learning Book*.
- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- Organizzazione per la cooperazione e lo sviluppo economico, *OECD AI Principles*.
- Thomas H. Davenport, *The AI Advantage: How to Put the Artificial Intelligence Revolution to Work*.
