# 4.1 Fondamenti e cultura della sicurezza

## Panoramica e motivazioni

La sicurezza non è una funzionalità da incollare alla fine, e non è il compito di un solo team specializzato separato dall'ingegneria. In una grande organizzazione, la sicurezza è una proprietà di come l'intero sistema è progettato, costruito, gestito e governato. Quando migliaia di ingegneri rilasciano codice su centinaia di servizi, l'anello più debole decide quanto danno può fare un incidente. Un singolo bucket di archiviazione configurato male, una dipendenza non aggiornata o un account di servizio con privilegi eccessivi possono esporre milioni di record. Fondamenti e cultura sono ciò che impedisce che questo accada su larga scala.

Per le imprese, la posta è finanziaria e reputazionale: costi delle violazioni, sanzioni normative, clienti persi e valutazioni deprezzate. Per gli enti pubblici, si estende alla sicurezza nazionale, alla fiducia del pubblico e alla continuità dei servizi essenziali. Entrambi i contesti condividono una dura verità: non puoi far rispettare la sicurezza soltanto con controlli e cancelli. Deve essere interiorizzata da chi fa il lavoro. Una cultura in cui gli ingegneri capiscono le minacce, sentono la responsabilità e sono premiati per aver sollevato preoccupazioni produce risultati molto migliori di una che si appoggia a un team di sicurezza sovraccarico che gioca da portiere.

Questo capitolo espone i modelli mentali e le pratiche culturali che sostengono ogni altro capitolo di sicurezza di questa guida. Tratta il fare della sicurezza il compito di tutti, la [modellazione delle minacce](https://en.wikipedia.org/wiki/Threat_model), il ciclo di vita sicuro dello sviluppo, principi architetturali fondamentali come la [difesa in profondità](https://en.wikipedia.org/wiki/Defense_in_depth_(computing)) e lo [zero trust](https://en.wikipedia.org/wiki/Zero_trust_security_model) e come dare priorità al lavoro di sicurezza in base al rischio reale anziché alla paura o alla moda.

*Vedi anche:* i capitoli 4.2 (sicurezza delle applicazioni), 4.3 (sicurezza dell'infrastruttura e del cloud), 4.4 (operazioni di sicurezza) e 4.6 (conformità e governance) si basano su questi fondamenti.

## Principi chiave

- **La sicurezza è il compito di tutti.** Ogni ingegnere, product manager e operatore è responsabile della sicurezza di ciò che costruisce. Il team di sicurezza abilita, consiglia e verifica; non fa e non può fare il lavoro da solo.
- **Presumi la violazione.** Progetta come se gli attaccanti fossero già dentro. Riduci al minimo ciò che un componente compromesso può raggiungere.
- **Difesa in profondità.** Nessun singolo controllo è sufficiente. Stratifica controlli indipendenti così che il fallimento di uno non significhi il fallimento di tutti.
- **[Minimo privilegio](https://en.wikipedia.org/wiki/Principle_of_least_privilege).** Concedi l'accesso minimo necessario, per il tempo minimo, e revocalo automaticamente quando non serve più.
- **Shift left.** Trova e correggi i problemi il prima possibile, quando sono più economici da risolvere.
- **Priorità basata sul rischio.** Spendi sforzo dove la combinazione di probabilità e impatto è più alta, guidato dalla triade CIA (riservatezza, integrità e disponibilità), non su ciò che ha fatto notizia questa settimana.
- **Apprendimento senza colpe.** Tratta incidenti e quasi-incidenti di sicurezza come occasioni di apprendimento, non come occasioni di punizione.

## Raccomandazioni

### Stabilisci un programma di security champion

Inserisci un security champion designato in ogni team di ingegneria. I champion non sono specialisti di sicurezza a tempo pieno. Sono ingegneri con formazione extra e una linea diretta con il team centrale di sicurezza. Rivedono progetti, fanno triage dei rilievi, rispondono alle domande dei colleghi e portano il contesto di sicurezza nella pianificazione. Questo scala la competenza di sicurezza nell'organizzazione senza assumere uno specialista per ogni team e costruisce fiducia, perché il consiglio viene da un pari che conosce davvero la base di codice.

Dai ai champion un supporto reale: un forum regolare dove condividere ciò che imparano, budget per formazione e conferenze, riconoscimento nelle valutazioni delle prestazioni e tempo ritagliato dagli impegni di consegna. Un programma di champion che esiste solo sulla carta non produce nulla.

### Pratica la modellazione delle minacce di routine

La modellazione delle minacce è l'abitudine disciplinata di chiedersi "che cosa potrebbe andare storto?" prima di costruire. Falla per i nuovi servizi, le funzionalità importanti e qualsiasi modifica ai confini di fiducia. Tienila abbastanza leggera da avvenire davvero spesso.

- **[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)** è una lista di controllo pratica mappata su proprietà di sicurezza: Spoofing (autenticazione), Tampering (integrità), Repudiation (non ripudio), Information disclosure (riservatezza), Denial of service (disponibilità) ed Elevation of privilege (autorizzazione). Percorri ogni flusso di dati e chiediti come si applica ciascuna categoria.
- **PASTA** (Process for Attack Simulation and Threat Analysis) è un metodo più pesante in sette fasi centrato sul rischio che lega le minacce tecniche all'impatto sul business; usalo per i sistemi di alto valore.
- Gli **[alberi d'attacco](https://en.wikipedia.org/wiki/Attack_tree)** scompongono un obiettivo ("rubare i dati dei clienti") nei passi ramificati che un attaccante compirebbe, aiutandoti a trovare e potare i percorsi.

Tieni i modelli delle minacce come documenti vivi accanto al codice e rivedili ogni volta che l'architettura cambia.

### Costruisci un ciclo di vita sicuro dello sviluppo software

Intreccia la sicurezza in ogni fase anziché trattarla come un cancello finale:

- **Requisiti:** cattura requisiti di sicurezza e privacy accanto a quelli funzionali.
- **Progetto:** modella le minacce e rivedi i confini di fiducia.
- **Implementazione:** fai rispettare standard di codifica sicura, revisione del codice e scansione dei segreti prima del commit.
- **Test:** esegui [SAST](https://en.wikipedia.org/wiki/Static_application_security_testing) (static application security testing), [DAST](https://en.wikipedia.org/wiki/Dynamic_application_security_testing) (dynamic application security testing) e scansione delle dipendenze nella pipeline (vedi capitolo 4.4).
- **Rilascio:** verifica la provenienza, firma gli artefatti e controlla la configurazione.
- **Esercizio:** monitora, aggiorna e rispondi.

Il punto dello shift-left non è ammassare tutto il lavoro prima e sommergere gli ingegneri. È cogliere i tipi di difetto che costano molto meno da correggere presto.

### Adotta i principi dell'architettura zero trust

La sicurezza tradizionale del perimetro presume che tutto ciò che sta dentro la rete sia affidabile. Quell'assunzione cade nel momento in cui un attaccante ottiene un punto d'appoggio. Lo zero trust sostituisce la fiducia implicita nella rete con una verifica esplicita e continua: autentica e autorizza ogni richiesta in base a identità, postura del dispositivo e contesto, indipendentemente da dove arriva nella rete. Combina identità forte, autorizzazione al minimo privilegio, micro-segmentazione e [cifratura](https://en.wikipedia.org/wiki/Encryption) ovunque. Lo zero trust è un percorso, non un prodotto, quindi affrontalo un passo alla volta.

### Dai priorità per rischio usando la triade CIA

Imposta ogni risorsa e controllo attorno a **Riservatezza**, **Integrità** e **Disponibilità**. Non tutti i dati richiedono la stessa protezione: una pagina di marketing pubblica e un database di cartelle cliniche hanno esigenze di riservatezza molto diverse. Classifica le tue risorse, stima probabilità e impatto della compromissione e punta lo scarso sforzo di sicurezza sulle combinazioni a più alto rischio. Scrivi le tue decisioni di rischio così che altri possano rivederle e difenderle in seguito.

## Compromessi: vantaggi e svantaggi

| Approccio | Vantaggi | Svantaggi |
|---|---|---|
| Il team centrale di sicurezza possiede tutta la sicurezza | Competenza profonda, standard coerenti | Collo di bottiglia, gli ingegneri si disimpegnano, non scala |
| Sicurezza distribuita (champion) | Scala, costruisce responsabilità, feedback più rapido | Richiede investimento, competenza disomogenea, serve coordinamento |
| Modellazione delle minacce pesante in anticipo per tutto | Accurata, coglie i difetti di progetto | Rallenta la consegna, può diventare spunta di caselle |
| Modellazione delle minacce leggera e mirata al rischio | Veloce, focalizzata su ciò che conta | Può perdere minacce nei sistemi "a basso rischio" |
| Cancelli rigidi che bloccano i rilasci | Fa rispettare la conformità | Attrito, incentiva i palliativi |

La tensione centrale è tra velocità e garanzia. Se ti spingi troppo verso cancelli e controllo centrale, crei un attrito che gli ingegneri aggirano, generando shadow IT e risentimento. Se ti spingi troppo verso l'autonomia senza supporto, ottieni una sicurezza incoerente e non verificata. La risposta sostenibile è una cultura forte con protezioni abilitanti: automatizzate dove puoi, umane dove serve giudizio e sempre spiegate anziché semplicemente imposte.

## Domande da discutere con il tuo team

1. **Quali dei vostri sistemi si guadagnano una modellazione delle minacce pesante, e chi decide il livello?** In un grande patrimonio non puoi condurre un'analisi PASTA in sette fasi su ogni servizio, quindi ti serve una regola esplicita per quando basta un passaggio STRIDE di 30 minuti e quando un sistema di alto valore merita una modellazione profonda guidata dall'impatto sul business. Ancora la decisione alla tua classificazione CIA: i sistemi che contengono registri regolamentati, flussi di pagamento o logica di autenticazione stanno in cima e una pagina di marketing pubblica no. Per il lavoro aziendale e governativo, un auditor ti chiederà di difendere perché un dato sistema è stato modellato in quel modo, quindi scrivi i criteri di livello e nomina il responsabile che li applica. Porta alla riunione la tua attuale classificazione delle risorse e un elenco di servizi senza modello delle minacce, perché il divario tra le due cose è il tuo vero rischio. Se non vi accordate sull'asticella, finirete per modellare tutto in modo leggero o niente in modo profondo, ed entrambi vi deludono.

2. **Quando un security champion e una scadenza di consegna si scontrano, chi può davvero fermare il rilascio?** Un programma di champion cambia i risultati solo se il champion porta autorità reale, non solo formazione extra e buone intenzioni. Decidi in anticipo se un champion può bloccare un rilascio, se escala al team centrale di AppSec e quale gravità di rilievo giustifica fermare la consegna anziché tracciarlo. Questo conta di più sotto pressione, quando un product manager vuole derogare a un difetto di progetto la settimana prima del lancio, che è esattamente quando i difetti non affrontati sono più costosi da correggere. Porta un esempio recente in cui una preoccupazione di sicurezza ha incontrato una scadenza e ricostruisci chi ha deciso e come, perché quella storia rivela il tuo vero percorso di escalation. Se la risposta onesta è che vince sempre la consegna, i tuoi champion sono decorativi e dovresti correggere l'incentivo prima di aggiungerne altri.

3. **Che cosa cambia concretamente "presumi la violazione" nella vostra prossima revisione di progetto?** Il principio è facile da approvare con un cenno e difficile da rendere operativo, quindi ancoralo a impegni specifici: quali confini di fiducia stringerete, dove aggiungerete micro-segmentazione e come ridurrete ciò che un singolo account di servizio compromesso può raggiungere. Per un grande team il vantaggio è la riduzione del raggio d'impatto, così un attaccante che atterra in un servizio non può spostarsi sull'archivio dati dietro di esso. Nei contesti aziendali e governativi questo plasma anche le tue decisioni su minimo privilegio e credenziali di breve durata, che sono economiche da progettare dentro e dolorose da adattare dopo. Porta un diagramma reale di un servizio e chiediti che cosa fa un attaccante dopo che possiede il livello web, poi impegnati su due modifiche di contenimento questo trimestre. Un vago accordo sul fatto che le violazioni accadano è inutile a meno che sposti un permesso, una regola di rete o la durata di una credenziale.

4. **Come saprete che la vostra cultura della sicurezza sta davvero migliorando, e quale metrica difendereste davanti al consiglio?** I tassi di completamento della formazione e il numero di ticket sono facili da raccogliere e quasi inutili, perché misurano attività anziché riduzione del rischio, e una grande organizzazione ci annega. Scegli metriche di esito su cui scommetteresti davvero un budget: tempo mediano di rimedio dei rilievi ad alta gravità, quota di servizi con un modello delle minacce aggiornato, frazione di incidenti colti prima della produzione e tasso di quasi-incidenti auto-segnalati, che dovrebbe salire man mano che la fiducia cresce anziché scendere. La considerazione contraria è che ogni buona metrica può essere manipolata, quindi abbina ciascuna a una contro-metrica e rivedi l'andamento anziché l'istantanea. Porta il tuo cruscotto attuale e chiediti quali numeri cambierebbero se la sicurezza peggiorasse davvero; quelli che non cambierebbero sono decorazione. Nei contesti aziendali e governativi un regolatore o un comitato di audit chiederà evidenze che i controlli funzionano, quindi scegli metriche che puoi difendere sotto esame anziché metriche che sembrano solo verdi.

5. **Che cosa succede davvero la prossima volta che un ingegnere segnala un errore, e il vostro processo è senza colpe nella pratica o solo sulla diapositiva?** L'apprendimento senza colpe è il principio più spesso professato e meno spesso vissuto, perché il primo incidente serio mette alla prova se la leadership lo intende davvero. Decidi in anticipo come separi la responsabilità di correggere un problema dalla punizione per averlo causato e chi conduce la revisione post-incidente così che resti sui sistemi rotti anziché su individui nominati. La tensione è reale: gli stakeholder vogliono qualcuno ritenuto responsabile, eppure punire chi segnala garantisce che il prossimo errore resti nascosto finché diventa una violazione. Porta le tue ultime due revisioni di incidenti e controlla se hanno incolpato una persona o un controllo e se l'ingegnere che ha dato l'allarme è stato ringraziato o messo da parte in silenzio. Per gli enti pubblici e le imprese regolamentate, le regole obbligatorie di notifica delle violazioni alzano ulteriormente la posta, perché una cultura che nasconde gli errori mancherà anche le scadenze di segnalazione che portano sanzioni legali.

6. **Chi possiede l'attrito dei vostri strumenti shift-left, e li state comprando, costruendo o ne siete sommersi?** L'analisi statica e dinamica automatizzata, la scansione delle dipendenze e quella dei segreti sono la spina dorsale di un ciclo di vita sicuro dello sviluppo, ma una pipeline che inonda gli ingegneri di falsi positivi insegna loro a ignorare l'output di sicurezza, il che è peggio di nessuna scansione. Decidi chi regola gli strumenti, chi fa il triage dei rilievi e se compri una piattaforma integrata o assembli scanner open source che poi devi mantenere tu. Le considerazioni in competizione sono copertura contro rumore e controllo contro costo: uno scanner economico che grida al lupo brucia la fiducia che un programma di champion ha impiegato anni a costruire. Porta il tuo attuale tasso di falsi positivi, il tempo medio che gli ingegneri attendono su un controllo bloccante e l'elenco dei team che hanno disabilitato in silenzio un cancello. Nelle grandi imprese e negli enti pubblici, aggiungi l'angolo degli appalti e della dispersione degli strumenti, perché dieci team che comprano ciascuno il proprio scanner producono una copertura incoerente che nessun auditor può riconciliare.

## Lente settoriale

**Startup.** Senza un team di sicurezza e con poca liquidità, la cultura è il tuo unico controllo accessibile. Fai di una lavagna di 30 minuti di modellazione delle minacce l'abitudine prima di qualsiasi funzionalità che tocchi autenticazione o pagamenti, attiva minimo privilegio e MFA ovunque perché non costano nulla e tieni un canale senza colpe dove chiunque possa segnalare una preoccupazione. Salta processi e strumenti pesanti; gli ingegneri fondatori non possono mantenerli e la disciplina che costruisci ora è ciò che permetterà agli acquirenti aziendali di fidarsi di te più avanti.

**Piccola impresa.** Non hai uno specialista di sicurezza dedicato e hai un budget ridotto, quindi appoggiati alle impostazioni sicure predefinite degli strumenti che già compri anziché montare la tua pipeline. Privilegia le piattaforme gestite che fanno rispettare per te MFA, aggiornamenti e minimo privilegio e tratta la sicurezza come una questione di igiene dei dati: sappi quali dati sensibili detieni e chi può raggiungerli. Quando devi scegliere tra costruire e comprare, compra, perché un controllo gestito che tieni aggiornato batte uno su misura che lasci marcire.

**Grande impresa.** Alla scala di centinaia di servizi e migliaia di ingegneri, la sfida è coerenza e governance tra molti team. Conduci un programma di security champion, standardizza livelli di modellazione delle minacce legati alla classificazione CIA e fornisci modelli da strada asfaltata e controlli automatici di pipeline così che ogni team erediti buoni valori predefiniti. Segui metriche di rimedio e di copertura rispetto a valori di riferimento e tieni una traccia di audit che mostri perché ogni sistema è stato modellato e controllato nel modo in cui lo è stato.

**Ente pubblico.** Regole sugli appalti, obblighi di trasparenza e responsabilità pubblica plasmano ogni scelta. I principi zero trust e le credenziali di breve durata sono spesso imposti da politica esecutiva e devi poter mostrare a un auditor una motivazione documentata e basata sul rischio su dove sia andato il budget di rafforzamento. Dai priorità prima ai sistemi che contengono i registri di cittadini più sensibili, pubblica le salvaguardie dove il pubblico ha diritto di saperlo e richiedi ai fornitori di dichiarare i limiti anziché accettare scatole nere opache.

## Esempi

**Startup.** Una startup di dieci persone non ha un team di sicurezza né un budget per averne uno, quindi i due ingegneri fondatori fanno della modellazione delle minacce un'abitudine di lavagna di 30 minuti prima di qualsiasi funzionalità che tocchi auth o pagamenti, chiedendosi che cosa potrebbe andare storto e chi lo vorrebbe. Adottano poche abitudini fondamentali che non costano nulla: minimo privilegio su ogni ruolo cloud, MFA su ogni account e un canale senza colpe dove chiunque possa sollevare una preoccupazione senza paura di essere incolpato. Quando più avanti raccolgono un round e gli acquirenti aziendali chiedono come gestiscono la sicurezza, quella cultura iniziale permette loro di rispondere onestamente anziché correre a inventarne una.

**Grande impresa.** Una banca globale con 6.000 ingegneri gestisce un programma di security champion con un champion formato per squadra. I champion partecipano a una gilda mensile, completano formazione trimestrale e guidano la modellazione delle minacce di ogni nuovo servizio usando STRIDE. Il team centrale di AppSec mantiene modelli da strada asfaltata e controlli automatici di pipeline. In due anni, il tempo mediano di rimedio dei rilievi ad alta gravità è sceso da 45 giorni a 9 e la modellazione delle minacce in fase di progetto ha colto un difetto di autorizzazione in un'API di pagamenti prima che raggiungesse la produzione, evitando un probabile incidente da segnalare.

**Ente pubblico.** Un'agenzia fiscale nazionale che modernizza sistemi legacy adotta i principi zero trust imposti dalla politica esecutiva. Ogni chiamata interna tra servizi è autenticata con credenziali di breve durata e autorizzata per richiesta; i segmenti di rete non conferiscono più fiducia. L'agenzia modella le minacce di ogni servizio rivolto ai cittadini rispetto ad alberi d'attacco radicati in "esfiltrare i registri dei contribuenti" e "alterare una dichiarazione". La priorità basata sul rischio, allineata ai livelli di impatto CIA, concentra prima il budget di rafforzamento sui sistemi che contengono i registri più sensibili.

## Business case: motivazioni, ROI e TCO

Il costo di costruire una cultura della sicurezza è reale: tempo dei champion, formazione, strumenti e il modesto freno del fare modellazione delle minacce e revisioni. Ma quel costo è piccolo rispetto al costo del non farlo. La violazione di dati grave media arriva a milioni una volta contati indagine, notifica, rimedio, sanzioni normative, esposizione legale e affari persi. Le violazioni negli enti pubblici aggiungono interruzione della missione ed erosione della fiducia pubblica che nessuna fattura cattura del tutto.

Il ritorno sull'investimento in sicurezza viene da tre fonti: **incidenti evitati** (la violazione che non accade mai), **minor costo di rimedio** (i difetti corretti in fase di progetto costano una frazione di quelli corretti in produzione) e **consegna più rapida** (strade asfaltate e controlli automatici permettono ai team di rilasciare con fiducia anziché attendere la revisione manuale). Quando presenti il caso alla leadership, imposta la sicurezza come gestione del rischio con un cartellino del prezzo, non come un bene astratto. Mostra la perdita attesa (probabilità per impatto) dei rischi principali, il costo per ridurli e il rischio che resta. I dirigenti finanziano la riduzione del rischio che possono misurare.

## Antipattern e insidie

- **Teatro della sicurezza.** Controlli che sembrano impressionanti ma non riducono alcun rischio reale, adottati per soddisfare un audit anziché per proteggere qualcosa.
- **Il team di sicurezza come cancello alla fine.** Scoprire i difetti di progetto la settimana prima del lancio, quando sono più costosi da correggere e più probabile che vengano derogati.
- **Cultura della colpa.** Punire l'ingegnere che segnala un errore garantisce che il prossimo errore resti nascosto.
- **Modellazione delle minacce a spunta.** Compilare un modello che nessuno legge, producendo documenti scollegati dall'architettura reale.
- **Controlli uguali per tutti.** Applicare lo stesso processo pesante a un sito pubblico e a un sistema di pagamenti, sprecando sforzo e generando risentimento.
- **Priorità guidata dalla paura.** Inseguire la vulnerabilità di tendenza nelle notizie anziché ciò che minaccia davvero le tue risorse.
- **Champion solo di nome.** Nominare champion senza dare loro tempo, formazione o autorità.

## Modello di maturità

**Livello 1: Avvio.** La sicurezza è reattiva e centralizzata. Le revisioni avvengono tardi se avvengono e non c'è modellazione delle minacce. Gli incidenti guidano correzioni ad hoc. Gli ingegneri vedono la sicurezza come problema di qualcun altro e non esiste uno standard condiviso.

**Livello 2: Sviluppo.** Esiste un team di sicurezza che definisce standard, ma la pratica è incoerente tra i team. Un po' di modellazione delle minacce avviene sui progetti principali e nessuna sugli altri. È disponibile una formazione di base. La sicurezza è ancora percepita come un cancello e lo shift-left è aspirazionale anziché reale.

**Livello 3: Standardizzazione.** I security champion sono inseriti in ogni team. La modellazione delle minacce è di routine per i nuovi servizi, a livelli rispetto alla classificazione CIA, e il ciclo di vita sicuro dello sviluppo è documentato e fatto rispettare nell'organizzazione. La priorità basata sul rischio guida il lavoro, gli standard di codifica sicura e i controlli di pipeline sono la strada asfaltata predefinita e le revisioni post-incidente senza colpe sono la norma.

**Livello 4: Gestione.** Gli esiti di sicurezza sono misurati e controllati rispetto a valori di riferimento. L'organizzazione segue il tempo mediano di rimedio dei rilievi ad alta gravità, la copertura dei modelli delle minacce, la quota di incidenti colti prima della produzione e i tassi di segnalazione dei quasi-incidenti, suddivisi per team. L'autorità dei champion di fermare un rilascio è definita e davvero esercitata. Le decisioni di rischio sono quantificate come probabilità per impatto, registrate e riviste con una cadenza fissa, così che i divari di controllo emergano come dati anziché come sorprese.

**Livello 5: Orchestrazione.** La sicurezza è davvero il compito di tutti e integrata con consegna, rischio e pianificazione di business. Modellazione delle minacce e progettazione sicura sono abituali e leggere e i principi zero trust sono in gran parte realizzati. Le metriche guidano il miglioramento continuo, l'organizzazione impara dai quasi-incidenti tra i team e i controlli si adattano automaticamente al mutare del quadro delle minacce e dell'architettura.

## Spunti di discussione

1. Come misurate se una cultura della sicurezza sta davvero migliorando, oltre a contare i completamenti della formazione?
2. Dov'è il giusto confine tra ciò che gestiscono i security champion e ciò che possiede il team centrale?
3. Come mantenete preziosa la modellazione delle minacce senza lasciare che diventi una spunta burocratica?
4. Un'architettura zero trust completa è realistica per il vostro patrimonio legacy, e se no, qual è il sottoinsieme pragmatico?
5. Come dovrebbe essere prioritizzato il lavoro di sicurezza rispetto alla consegna di funzionalità quando entrambi competono per gli stessi ingegneri?
6. Quali incentivi cambiano davvero il comportamento degli ingegneri verso la responsabilità della sicurezza?

## Punti chiave

- La sicurezza è una proprietà culturale delle grandi organizzazioni, non un compito delegato a un solo team.
- I security champion scalano competenza e responsabilità nell'ingegneria.
- La modellazione delle minacce (STRIDE, PASTA, alberi d'attacco) fa emergere i difetti di progetto presto e a basso costo.
- Un SDLC sicuro e una mentalità shift-left colgono i difetti quando costano meno.
- Difesa in profondità, minimo privilegio e zero trust sono i principi architetturali fondamentali.
- La triade CIA e la priorità basata sul rischio dirigono lo scarso sforzo dove conta di più.
- Il costo di costruire una cultura della sicurezza è molto più piccolo del costo delle violazioni che previene.

## Riferimenti e letture di approfondimento

- Adam Shostack, *Threat Modeling: Designing for Security*
- Ross Anderson, *Security Engineering: A Guide to Building Dependable Distributed Systems*
- Michael Howard e Steve Lipner, *The Security Development Lifecycle*
- Betsy Beyer et al. (Google), *Building Secure and Reliable Systems*
- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- National Institute of Standards and Technology, *Secure Software Development Framework (SSDF), SP 800-218*
- OWASP, indicazioni su *Threat Modeling* e *Security Champions*
