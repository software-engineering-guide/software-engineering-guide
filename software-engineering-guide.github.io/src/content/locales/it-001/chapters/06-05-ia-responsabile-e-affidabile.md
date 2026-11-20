# 6.5 IA responsabile e affidabile

## Panoramica e motivazioni

L'IA responsabile e affidabile è la pratica di costruire e gestire sistemi di IA equi, trasparenti, responsabili, sicuri e rispettosi della privacy. Significa anche essere in grado di mostrare tutto questo alle persone interessate e ai regolatori. Man mano che l'IA assume decisioni che plasmano la vita delle persone (assunzioni, prestiti, idoneità alle prestazioni), la domanda non è più solo "funziona?" ma "è giusto, e possiamo giustificarlo?". Un sistema accurato in media può comunque essere iniquo verso un sottogruppo, inspiegabile per la persona che colpisce o non sicuro quando usato in modo improprio. Ti guadagni la fiducia affrontando deliberatamente queste dimensioni, non sperando che si risolvano da sole.

Per i grandi team, l'IA responsabile non può essere il compito di una sola persona né una casella da spuntare alla fine. Intessila nel modo in cui progetti, valuti, distribuisci e governi i sistemi, con chiara proprietà ed escalation. Su larga scala, piccoli pregiudizi e divari nella supervisione colpiscono molte persone. Un singolo fallimento di alto profilo può danneggiare la tua reputazione e invitare regolamentazione. I quadri di governance esistono proprio perché le buone intenzioni ad hoc non scalano.

Le organizzazioni governative e regolamentate affrontano obblighi vincolanti. Leggi emergenti, come l'[EU AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act), impongono requisiti graduati per rischio. Standard come il NIST AI Risk Management Framework e la ISO/IEC 42001 ti danno modi strutturati di soddisfarli. Gli enti pubblici devono evitare discriminazioni illecite, fornire vie per contestare le decisioni automatizzate ed essere trasparenti su come l'IA è usata nell'esercizio della pubblica autorità. L'IA responsabile in questi contesti è sia un dovere etico sia una necessità legale.

*Vedi anche:* il capitolo 6.1 (strategia e preparazione per l'IA), il capitolo 10.5 (etica, responsabilità e interesse pubblico) e il capitolo 4.5 (privacy e protezione dei dati).

## Principi chiave

- L'equità è un obiettivo di progetto da misurare e gestire, non da presumere.
- Le persone colpite dalle decisioni dell'IA meritano spiegazione e una via per contestarle.
- La responsabilità spetta agli umani e all'organizzazione, mai al modello.
- Privacy e sicurezza devono essere progettate dentro, compresa la protezione da uso improprio e abuso.
- La governance dovrebbe seguire quadri riconosciuti così da essere difendibile e verificabile.
- La supervisione umana deve essere significativa, con reale autorità di scavalcare e fermare.
- Considera i costi più ampi dell'IA, compresa la sua impronta ambientale.

## Raccomandazioni

### Rileva e mitiga pregiudizio e iniquità

Definisci che cosa significa equità nel tuo contesto. Esistono più definizioni matematiche, a volte in conflitto, e quella giusta dipende dalla decisione e dalla legge. Testa i modelli per prestazioni disparate attraverso gruppi protetti e vulnerabili usando dati rappresentativi. Fallo prima del rilascio e continua a farlo dopo, perché il [pregiudizio](https://en.wikipedia.org/wiki/Algorithmic_bias) può emergere man mano che le popolazioni si spostano. Mitiga attraverso dati migliori, ripesatura, vincoli o cambiando il modo in cui il sistema è usato e documenta i compromessi che hai accettato. Rimuovere un attributo protetto non rimuove il pregiudizio, perché i proxy restano. Tratta l'equità come una disciplina continua di misura e gestione, non un'autorizzazione una tantum.

### Fornisci spiegabilità, interpretabilità e trasparenza

Adegua il livello di spiegazione alla posta e al pubblico. Per le decisioni rilevanti, dai alle persone colpite una ragione chiara in linguaggio semplice che possano capire e su cui possano agire. Per la governance interna, mantieni abbastanza [interpretabilità](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence) tecnica da debuggare e difendere il sistema. Preferisci modelli intrinsecamente interpretabili dove la posta è alta e l'interpretabilità è raggiungibile. Dove i modelli complessi sono necessari, usa tecniche di spiegazione restando onesto sui loro limiti. Sii trasparente su quando si usa affatto l'IA, soprattutto nelle interazioni con il pubblico.

### Governa con quadri riconosciuti

Adotta un approccio di governance strutturato anziché inventarne uno. Il **NIST AI Risk Management Framework** organizza il lavoro attorno a governare, mappare, misurare e gestire il rischio dell'IA. L'**EU AI Act** classifica i sistemi per rischio e impone obblighi di conseguenza, con requisiti rigorosi per gli usi ad alto rischio. La **ISO/IEC 42001** definisce un sistema di gestione dell'IA che può essere verificato e certificato. Mappa i tuoi sistemi su questi quadri. Mantieni documentazione come le schede di modello e di dati (sintesi standardizzate di scopo, prestazioni e limiti di un modello o di un insieme di dati). Conduci valutazioni del rischio prima del rilascio e tieni un inventario dei sistemi di IA con i loro livelli di rischio e responsabili. Una buona governance assegna ruoli chiari, diritti decisionali e percorsi di escalation.

### Assicura supervisione umana, responsabilità e ricorso

Mantieni un umano significativamente al controllo delle decisioni rilevanti, con genuina autorità e le informazioni necessarie per scavalcare il sistema, non un timbro di gomma. Assegna una chiara responsabilità: nomina un responsabile che risponda del comportamento di ogni sistema. Dai alle persone colpite da decisioni automatizzate il diritto a una spiegazione e un processo praticabile per ricorrere a un umano che possa cambiare l'esito. Registra le decisioni e la loro base, così da poter gestire ricorsi e audit con equità e prontezza.

### Proteggi privacy, sicurezza e dall'uso improprio

Minimizza i dati personali che raccogli e usi, stabilisci una base giuridica e applica tecniche di privacy adatte alla sensibilità in gioco. Fai il [red team](https://en.wikipedia.org/wiki/Red_team) dei sistemi prima e dopo il rilascio per trovare i modi in cui possono essere manipolati, aggirati o usati in modo improprio per causare danno e correggi ciò che trovi. Costruisci salvaguardie contro la generazione di contenuti dannosi, la fuga di dati sensibili o l'abilitazione di abusi. Pianifica gli incidenti: monitoraggio, risposta e divulgazione. Considera il [duplice uso](https://en.wikipedia.org/wiki/Dual-use_technology) (la stessa capacità che serve fini sia benefici sia dannosi) e l'uso improprio a valle, non solo l'uso previsto.

### Tieni conto del costo ambientale

Addestrare ed erogare grandi modelli consuma energia e acqua significative. Misura e riporta l'impronta dei principali carichi di IA. Preferisci modelli e hardware efficienti dove soddisfano il bisogno. Dimensiona i modelli al compito anziché ricorrere per default al più grande e fai entrare il costo ambientale nelle decisioni di architettura e appalto.

## Compromessi: vantaggi e svantaggi

| Tensione | Un lato | L'altro lato |
|---|---|---|
| Accuratezza contro equità | La massima accuratezza media | Esiti equi tra i gruppi |
| Prestazioni contro interpretabilità | Modelli complessi e potenti | Modelli spiegabili e difendibili |
| Automazione contro supervisione | Efficienza e scala | Controllo umano e responsabilità |
| Utilità dei dati contro privacy | Modelli più ricchi da più dati | Minimizzazione e protezione dei dati |
| Capacità contro sicurezza | Funzionalità ampia e aperta | Comportamento vincolato e protetto |
| Velocità contro governance | Rilascio rapido | Revisione e documentazione approfondite |

Raramente c'è un pranzo gratis. Migliorare l'equità può costare un po' di accuratezza. L'interpretabilità può costare un po' di prestazioni. La governance costa tempo. Il percorso responsabile è fare questi compromessi consapevolmente, documentarli e scegliere a favore delle persone colpite e della difendibilità quando la posta è alta. Presentare la governance come un freno all'innovazione è una falsa dicotomia. Il rischio dell'IA non gestito è esso stesso una minaccia all'innovazione sostenuta.

## Domande da discutere con il tuo team

1. **Quali dei nostri sistemi di IA distribuiti l'EU AI Act classificherebbe come ad alto rischio, e stiamo soddisfacendo oggi quegli obblighi?** La legge graduata per rischio è ora vincolante, non ipotetica, e un sistema che decide assunzioni, prestiti o idoneità alle prestazioni può portare requisiti rigorosi che potresti già violare. Per una grande organizzazione, questa domanda forza un inventario onesto anziché un'ipotesi comoda che la governance sia "sotto controllo". Porta il tuo elenco di sistemi di IA con i loro livelli di rischio e responsabili, mappato su EU AI Act, NIST AI Risk Management Framework e ISO/IEC 42001 dove rilevante. Il segnale da osservare è qualsiasi sistema rilevante senza classificazione del rischio, senza valutazione d'impatto e senza scheda di modello o di dati. Per gli enti pubblici che esercitano pubblica autorità, mancare gli obblighi non è una voce di arretrato, è esposizione legale e la risposta dovrebbe innescare le valutazioni e la documentazione che quei sistemi richiedono.

2. **Quando uno dei nostri modelli nega qualcosa a qualcuno, quella persona può ottenere una ragione in linguaggio semplice e raggiungere un umano che possa davvero rovesciare l'esito?** Un diritto alla spiegazione e un ricorso praticabile sono ciò che separa l'IA responsabile da una scatola nera che danneggia le persone senza rimedio. L'equità misurata in media può comunque fallire un individuo e l'interpretabilità scelta dopo il rilascio è di solito teatro. Porta una specifica decisione distribuita e ricostruiscila: la ragione che la persona colpita riceve, il canale di ricorso e se l'umano dall'altra parte ha genuina autorità e la base registrata per scavalcare. Nei contesti governativi e regolamentati, una via di ricorso è spesso un requisito di legge, non una cortesia. Se la ragione è inintelligibile o il ricorso porta a un timbro di gomma, quello è il divario da correggere prima del prossimo rilascio.

3. **Chi è l'unica persona nominata responsabile quando un modello causa danno, e ha reale autorità di fermarlo?** La responsabilità spetta agli umani e all'organizzazione, mai al modello, ma quel principio è vuoto finché a ogni sistema non è attaccato un nome e quella persona può davvero staccare la spina. Per un grande team, la proprietà diffusa significa che quando emerge un fallimento di equità o un aggiramento, tutti presumono che qualcun altro stia osservando. Porta la tua mappa di proprietà, i tuoi percorsi di escalation e l'evidenza che la supervisione è significativa: il responsabile nominato ottiene le informazioni e il potere di scavalcare o fermare il sistema, o solo di annuire? Discuti come fai red team per usi impropri e abusi che non hai ancora immaginato, poiché testare solo l'uso previsto perde i fallimenti che fanno i titoli. La risposta non dovrebbe lasciare alcun sistema rilevante senza un responsabile che possa fermarlo.

4. **Per ogni modello rilevante, quale definizione di equità abbiamo scelto, chi l'ha approvata e le nostre metriche per sottogruppo reggono davvero in produzione?** L'equità ha diverse definizioni matematiche in conflitto tra loro, quindi un modello che soddisfa tassi uguali di falsi positivi può violare esiti uguali e scegliere una definizione è un giudizio di valore che non dovrebbe essere lasciato a chi ha scritto il ciclo di addestramento. Per un grande team, un valore predefinito non esaminato nasconde la scelta dentro il codice e fa ereditare a ogni gruppo a valle una decisione che nessuno ha dibattuto. Porta la metrica di equità che hai ottimizzato, i gruppi protetti e vulnerabili su cui hai testato, i dati rappresentativi che hai usato e la deriva che hai visto dal lancio, poiché rimuovere un attributo protetto lascia proxy che tengono in vita il pregiudizio. Nei contesti aziendali e governativi, nomina la persona con autorità di accettare un compromesso di equità e registralo, perché un regolatore o un difensore civico chiederà chi ha deciso che quella definizione di equo fosse quella giusta per le persone a cui è stato negato un prestito, una prestazione o un lavoro. Se dopo il rilascio non sono monitorate metriche per sottogruppo, tratta il modello come non misurato anziché equo.

5. **Con quanti pochi dati personali può girare ciascun sistema, e ne abbiamo fatto il red team per l'uso improprio e il duplice uso a cui preferiremmo non pensare?** Privacy e sicurezza devono essere progettate dentro e il modo più economico di ridurre sia il rischio di violazione sia la superficie di abuso è raccogliere e conservare meno dati in primo luogo, eppure i team accumulano di routine input "nel caso servano dopo". Per una grande organizzazione, ogni campo in più è una questione di base giuridica, un obbligo di conservazione e un premio più grande per un attaccante o un aggiramento. Porta l'inventario dei dati e la base giuridica per ogni sistema, i risultati del red team per manipolazione, fuga e generazione dannosa e un elenco onesto delle capacità a duplice uso in cui la stessa funzionalità che aiuta un utente legittimo aiuta anche chi agisce in malafede. Nei contesti regolamentati e pubblici, lega questo al tuo piano di incidente: monitoraggio, risposta e divulgazione, perché un ente pubblico che fa trapelare dati sensibili o rilascia un sistema aggirabile affronta doveri di legge, non solo imbarazzo. Se il red team ha sempre sollecitato solo il percorso previsto, hai testato la dimostrazione, non il sistema.

6. **Misuriamo e possediamo l'impronta ambientale dei nostri principali carichi di IA, o "usa il modello più grande" è un valore predefinito non prezzato?** Addestrare ed erogare grandi modelli consuma energia e acqua reali e ricorrere per default al modello più grande per compiti che uno più piccolo gestirebbe trasforma una scorciatoia ingegneristica in un costo ricorrente che l'organizzazione non vede mai su un cruscotto. Per un grande team che gestisce molti carichi, piccole inefficienze per chiamata si compongono in un'impronta che diventa una passività di appalto e di rendicontazione man mano che le attese di divulgazione si stringono. Porta l'impronta misurata dei tuoi carichi più pesanti, un confronto tra dimensioni del modello e l'accuratezza di cui il compito ha davvero bisogno e le scelte di hardware ed erogazione che potresti ridimensionare. Nei contesti aziendali e governativi, collega questo a impegni di sostenibilità e criteri di appalto, poiché gli enti pubblici devono sempre più riportare l'impatto ambientale e giustificare la spesa e un'impronta non misurata è una cifra che un giorno ti sarà chiesto di produrre e non potrai. Decidi se il costo ambientale è un input formale della scelta del modello, o ammetti che oggi non lo è.

## Lente settoriale

**Startup.** Non puoi dotare di personale un consiglio di governance, quindi fai la versione leggera che conta comunque. Scegli modelli interpretabili dove la decisione è rilevante, scrivi una scheda di modello di una pagina, testa per esiti disparati attraverso i gruppi che puoi misurare e registra le decisioni così da poter rivedere l'equità man mano che cresci. Dai a ogni decisione avversa una ragione semplice e una via verso un umano. Saltarlo non è velocità, è una passività che non puoi permetterti se una singola decisione iniqua raggiunge la stampa o un regolatore.

**Piccola impresa.** Senza uno specialista dedicato, tratta l'IA responsabile come una questione d'acquisto: preferisci i fornitori che documentano i test di equità, espongono schede di modello e di dati e ti permettono di dichiarare ai clienti quando l'IA è in uso. Sappi quali dati personali raccolgono i tuoi strumenti e se hai una base giuridica per usarli. Dove una risposta automatica sbagliata potrebbe danneggiare un cliente, tieni una persona nel ciclo anziché fidarti di uno strumento che non puoi ispezionare né spiegare.

**Grande impresa.** Il compito è la governance su larga scala tra molti team: mappa ogni sistema su NIST AI Risk Management Framework, EU AI Act e ISO/IEC 42001, tieni un inventario con livelli di rischio e responsabili nominati e richiedi test di equità, sicurezza e privacy prima e dopo il lancio. Standardizza schede di modello e di dati, red teaming e processi di ricorso così che i gruppi smettano di reinventarli. Metti a bilancio esplicitamente i costi di governance, supervisione e interpretabilità e tratta il rischio dell'IA non gestito come una minaccia alla licenza di operare.

**Ente pubblico.** Regole sugli appalti, trasparenza e responsabilità pubblica plasmano ogni scelta. Pubblica un avviso di trasparenza in linguaggio semplice, conduci una valutazione d'impatto prima del rilascio e tieni una decisione umana significativa per qualsiasi azione che riguardi un cittadino, con una via di ricorso praticabile. Esigi che i fornitori dichiarino i limiti del modello e concedano portabilità dei dati, evita la discriminazione illecita, nomina un funzionario responsabile per ogni sistema e riporta l'impronta ambientale dei principali carichi.

## Esempi

**Startup.** Una piccola startup di prestiti che costruiva una prima funzionalità di punteggio del credito non poteva dotare di personale un consiglio di governance, quindi ha fatto la versione leggera che contava comunque. Due fondatori hanno approvato insieme il modello, lo hanno testato per esiti disparati attraverso i gruppi che potevano misurare e hanno scritto una breve scheda di modello di una pagina che copriva dati, limiti e rischi noti. Hanno scelto un modello più semplice e più interpretabile così da poter dare a ogni richiedente respinto una ragione semplice e una via verso una revisione umana e hanno registrato le decisioni per poter rivedere l'equità man mano che crescevano.

**Grande impresa.** Una banca che distribuiva un modello di credito ha istituito un consiglio di governance dell'IA, ha mappato il modello su una categoria ad alto rischio e ha richiesto test di equità attraverso gruppi demografici prima e dopo il lancio. Ha documentato il modello in una scheda di modello. Ha dato ai richiedenti respinti una ragione in linguaggio semplice e un ricorso a un sottoscrittore umano e ha fatto il red team del sistema per la manipolazione. Ha scelto un modello un po' meno accurato ma più interpretabile, perché doveva spiegare e difendere ogni decisione ai regolatori.

**Ente pubblico.** Un'agenzia pubblica che usava l'IA per aiutare ad allocare le risorse di ispezione ha allineato il proprio programma al NIST AI RMF e alle disposizioni rilevanti della legge applicabile sull'IA. Ha pubblicato un avviso di trasparenza che descriveva come funzionava il sistema e le sue salvaguardie. Ha condotto una valutazione d'impatto prima del rilascio, mantenuto una decisione umana significativa per qualsiasi azione che riguardasse un cittadino e fornito un processo di ricorso. L'equità era monitorata di continuo, il costo ambientale del carico era riportato ed era stato nominato un funzionario responsabile che rispondesse del sistema.

## Business case: motivazioni, ROI e TCO

L'IA responsabile protegge il valore tanto quanto lo crea. Il ROI è in gran parte costo evitato: meno cause per discriminazione, sanzioni normative e disastri reputazionali; audit più fluidi; e maggiore fiducia degli utenti e del pubblico, che guida l'adozione. I sistemi affidabili sono anche più robusti, perché la disciplina che produce equità e sicurezza produce anche una migliore ingegneria.

Il TCO include personale di governance, test di equità e sicurezza, documentazione, red teaming, processi di supervisione e le prestazioni a volte scambiate per interpretabilità o equità. Pesalo contro il costo del non investire: responsabilità legale, chiusure forzate, fiducia pubblica persa e il costo molto più alto di adattare la governance dopo un fallimento. Nei contesti regolamentati, l'investimento in IA responsabile è sempre più non negoziabile. Presenta il caso alla leadership impostandolo come gestione del rischio e licenza di operare: la precondizione per distribuire affatto l'IA su larga scala.

## Antipattern e insidie

- **Equità per omissione.** Presumere che un modello sia equo perché ignora gli attributi protetti.
- **Teatro della spiegabilità.** Produrre spiegazioni che non riflettono davvero come sono prese le decisioni.
- **Supervisione a timbro di gomma.** Revisione umana nominale senza reale autorità né informazioni per scavalcare.
- **Governance come ripensamento.** Incollare documentazione e revisione dopo progetto e rilascio.
- **Nessuna via di ricorso.** Lasciare le persone colpite senza modo di contestare una decisione automatizzata.
- **Ignorare l'uso improprio.** Testare solo l'uso previsto e perdere aggiramenti e abusi.
- **Cecità all'impronta.** Ricorrere per default al modello più grande senza riguardo al costo ambientale.

## Modello di maturità

1. **Avvio.** Nessun test di equità, spiegazione o governance; la responsabilità è indefinita; pregiudizio, uso improprio e problemi di privacy emergono solo dopo il danno e non c'è inventario dei sistemi di IA né dei loro rischi.
2. **Sviluppo.** Alcuni test di pregiudizio, schede di modello e red teaming avvengono su singoli sistemi, ma la pratica è incoerente tra i team; la supervisione è ad hoc; quadri come il NIST AI Risk Management Framework e l'EU AI Act sono noti ma solo in parte adottati.
3. **Standardizzazione.** La governance è documentata e fatta rispettare nell'organizzazione: i sistemi sono mappati su quadri riconosciuti e sulla ISO/IEC 42001, ciascuno ha un livello di rischio e un responsabile nominato e test di equità, sicurezza e privacy, schede di modello e di dati, vie di ricorso e red teaming per i sistemi ad alto rischio sono richiesti anziché facoltativi.
4. **Gestione.** Il programma è misurato e controllato con dati: metriche di equità per sottogruppo, risultati di sicurezza e aggiramenti, volumi di ricorsi e tassi di ribaltamento, tassi di scavalcamento della supervisione e impronta dei carichi sono seguiti rispetto a valori di riferimento e soglie; deriva ed esiti disparati innescano azioni definite; le decisioni di procedere o meno poggiano sull'evidenza anziché sulla rassicurazione.
5. **Orchestrazione.** L'IA responsabile è migliorata di continuo e integrata nell'organizzazione: il monitoraggio di equità, sicurezza e uso improprio gira in produzione, la governance è incorporata nella consegna, il costo ambientale è un input formale della scelta del modello e l'organizzazione adatta i propri controlli al mutare di legge, rischio e capacità, con la responsabilità posseduta da tutti anziché da un solo team.

## Spunti di discussione

- Quale definizione di equità si applica a una data decisione, e chi decide?
- Quanta accuratezza o prestazione è accettabile scambiare per equità o interpretabilità?
- Che cosa rende significativa la supervisione umana anziché un timbro di gomma?
- Come dovrebbero essere progettati i ricorsi contro le decisioni automatizzate per essere equi e tempestivi?
- Come fate red team per usi impropri che non avete ancora immaginato?
- Il costo ambientale dovrebbe influenzare la scelta del modello, e come lo pesereste?

## Punti chiave

- L'IA affidabile è equa, spiegabile, responsabile, sicura e rispettosa della privacy, per progetto.
- Equità e sicurezza sono discipline continue di misura e gestione, non controlli una tantum.
- Allinea la governance a NIST AI RMF, EU AI Act e ISO/IEC 42001 per essere difendibile e verificabile.
- Mantieni una supervisione umana significativa, una chiara responsabilità e un vero diritto di ricorso.
- Progetta per la privacy e contro l'uso improprio e tieni conto del costo ambientale.

## Riferimenti e letture di approfondimento

- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- Unione europea, *Artificial Intelligence Act (Regulation on Artificial Intelligence)*.
- ISO/IEC 42001, *Information technology, Artificial intelligence, Management system*.
- Solon Barocas, Moritz Hardt e Arvind Narayanan, *Fairness and Machine Learning: Limitations and Opportunities*.
- Christoph Molnar, *Interpretable Machine Learning*.
- Cathy O'Neil, *Weapons of Math Destruction*.
- Emma Strubell, Ananya Ganesh e Andrew McCallum, *Energy and Policy Considerations for Deep Learning in NLP*.
