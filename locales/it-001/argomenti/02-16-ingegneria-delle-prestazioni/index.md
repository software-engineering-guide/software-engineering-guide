# 2.16 Ingegneria delle prestazioni

## Panoramica e motivazioni

L'ingegneria delle prestazioni è l'arte di rendere il codice abbastanza veloce, di proposito, usando la misura anziché l'istinto. Questo capitolo lavora a livello di codice e di componenti: funzioni, cicli, strutture dati, query, allocazioni e il modo in cui un singolo servizio spende il proprio tempo. È il compagno del capitolo 3.5, che tratta le prestazioni a livello di sistema (scalare in orizzontale, bilanciamento del carico, capacità e resilienza). Quando un sistema è lento, il capitolo 3.5 chiede di quante macchine hai bisogno; questo capitolo chiede perché una macchina stia facendo così tanto lavoro in primo luogo. Di solito ti serviranno entrambi, e la vista a livello di codice è dove si nasconde una quantità sorprendente di costo e latenza.

Per i grandi team questa disciplina conta perché le prestazioni decadono in silenzio. Nessun singolo commit rende lento un servizio, ma mille piccoli, ciascuno con una chiamata al database o un ciclo non limitato in più, sì. Senza un metodo condiviso per misurare, fissare budget e controllare le prestazioni, scopri il marcire solo quando un cliente si lamenta o un lancio si squaglia. Un metodo trasforma le prestazioni da un incendio eroico in una proprietà di routine da proteggere.

Per le imprese, le prestazioni sono denaro: codice più veloce significa meno macchine, bollette cloud più basse e la capacità di rispettare un [accordo sul livello di servizio](https://en.wikipedia.org/wiki/Service-level_agreement) (SLA) sulla latenza senza sovradimensionare. Per gli enti pubblici, le prestazioni sono accesso: una pagina che si carica su un vecchio telefono con una connessione mobile debole è la differenza tra un cittadino che completa una richiesta di prestazione e uno che rinuncia. I sistemi pubblici hanno anche bisogno di evidenze di benchmark riproducibili, perché appalti e organi di vigilanza ti chiederanno di provare i numeri, non solo di asserirli.

## Principi chiave

- **Misura prima di ottimizzare.** Il collo di bottiglia non è quasi mai dove immagini. Profila, poi agisci.
- **Evita l'ottimizzazione prematura.** L'avvertimento di Donald Knuth vale: ottimizzare codice che non conta costa chiarezza e non compra nulla.
- **Definisci "abbastanza veloce" come un numero.** Un budget di prestazioni con un obiettivo e un percentile trasforma l'opinione in un superato o fallito.
- **Le medie mentono; i percentili dicono la verità.** È la coda (p99) che gli utenti sentono, non la media.
- **Le vittorie algoritmiche battono la rifinitura minuta.** Una classe di complessità migliore supera qualsiasi quantità di ingegnosità sui fattori costanti.
- **Latenza e throughput sono obiettivi diversi.** Migliorarne uno può peggiorare l'altro; sappi quale stai comprando.
- **Fai benchmark onesti o non farli.** Riscaldamento, varianza e un carico di lavoro rappresentativo separano i numeri reali dalla finzione.
- **Controlla le prestazioni nella CI, osservale in produzione.** Le regressioni colte prima dell'integrazione costano poco; quelle colte dagli utenti, molto.

## Raccomandazioni

### Misura prima e profila prima di toccare una riga

La regola più antica di questo campo è la più ignorata: trova il collo di bottiglia prima di ottimizzare. Ricorri a un [profiler](https://en.wikipedia.org/wiki/Profiling_(computer_programming)), uno strumento che campiona o strumenta un programma in esecuzione per mostrare dove spende tempo e memoria. Profila la CPU (quali funzioni bruciano cicli), memoria e allocazioni (che cosa viene allocato e quanto spesso, poiché il rimescolio di allocazioni guida le pause della garbage collection) e l'I/O (tempo speso ad attendere disco, rete o database). Un [flame graph](https://en.wikipedia.org/wiki/Flame_graph), una visualizzazione impilata in cui ogni riquadro è una funzione e la sua larghezza è il tempo speso, rende ovvio a colpo d'occhio il costo dominante: cerca i riquadri più larghi, non le pile più profonde. Ottimizza prima il costo più grande, rimisura e fermati quando raggiungi il budget. Questo si collega alle pratiche di osservabilità del capitolo 9.2, perché un profilo di produzione batte qualsiasi ipotesi fatta da un portatile.

Guardati anche dall'errore opposto. La frase completa di Knuth è che l'ottimizzazione prematura è la radice di molti mali, e si riferiva alle piccole inefficienze che ti tentano di sacrificare codice leggibile per una velocità immaginata. Scrivi prima la versione chiara, misura e ottimizza solo il codice che il profiler accusa.

### Definisci che cosa significa "abbastanza veloce" con i budget di prestazioni

La velocità non è una virtù in astratto; è un obiettivo che raggiungi o manchi. Fissa un **budget di prestazioni**: un limite concreto come "latenza p99 del pagamento sotto 300 ms" o "questo endpoint alloca meno di 1 MB per richiesta". Collegalo a qualcosa che utenti o business sentono ed esprimilo come **percentile**, non come media, perché la media nasconde la coda lenta dove vivono gli utenti reali. Se l'1% delle richieste impiega 5 secondi, la tua media può sembrare a posto mentre una quota significativa di clienti soffre. I budget danno a un team una definizione di completato condivisa e indiscutibile e una linea che una regressione varca in modo visibile.

### Ricorri all'efficienza algoritmica prima della rifinitura minuta

Le vittorie più grandi ed economiche vengono dall'[efficienza algoritmica](https://en.wikipedia.org/wiki/Algorithmic_efficiency), cioè come il lavoro cresce al crescere dell'input, descritta con la [notazione O-grande](https://en.wikipedia.org/wiki/Big_O_notation) (un modo di classificare il tasso di crescita, così che un ordinamento O(n log n) scali molto meglio di uno O(n al quadrato)). Un ciclo annidato invisibile a dieci elementi diventa una catastrofe a diecimila. Prima di rifinire a mano una funzione calda, chiediti se sta facendo fondamentalmente troppo lavoro: una query N+1 accidentale, una scansione lineare che dovrebbe essere una ricerca hash o un lavoro ripetuto che potrebbe essere memorizzato. Questo si collega ai fondamenti algoritmici del capitolo 2.13. Nessuna rifinitura dei fattori costanti salva la classe di complessità sbagliata.

### Distingui la latenza dal throughput e rispetta la coda

La **latenza** è quanto dura una singola operazione; il **throughput** è quante operazioni si completano per unità di tempo. Non sono lo stesso obiettivo e ottimizzarne uno può danneggiare l'altro. Il raggruppamento (batching) migliora il throughput ma aggiunge latenza al primo elemento del gruppo; aggiungere lavoratori paralleli alza il throughput ma può peggiorare la latenza di coda per contesa. Decidi di quale hanno davvero bisogno i tuoi utenti. E osserva sempre la coda: la latenza p95 e p99, il 5% e l'1% più lenti delle richieste, perché su larga scala un utente fa molte richieste e colpisce spesso la coda. Riporta i percentili, imposta allarmi su di essi e fissa budget per essi.

### Conosci i limiti del parallelismo

Quando parallelizzi, ricorda la [legge di Amdahl](https://en.wikipedia.org/wiki/Amdahl%27s_law): l'accelerazione ottenuta aggiungendo processori è limitata dalla frazione del lavoro che deve girare in serie. Se il 10% di un lavoro è intrinsecamente sequenziale, nessun numero di core ti porta oltre un'accelerazione di 10 volte. Concorrenza (strutturare il lavoro così che i compiti possano progredire in modo indipendente) e parallelismo (eseguirli davvero nello stesso momento) aggiungono vera complessità, dalle race condition al costo di coordinamento. Misura la frazione seriale prima di presumere che più thread ti salveranno, e sii onesto sul fatto che la versione corretta più semplice è spesso abbastanza veloce.

### Usa cache e località dei dati e rispetta i loro costi

Una [cache](https://en.wikipedia.org/wiki/Cache_(computing)), un archivio veloce di risultati recenti o costosi da calcolare, è lo strumento di prestazioni più potente che hai e il più pericoloso. La battuta di Phil Karlton secondo cui i due problemi difficili dell'informatica sono l'invalidazione della cache e dare nomi alle cose è un avvertimento: una cache obsoleta serve risposte sbagliate e la logica di invalidazione è dove nascono bug sottili. Usa la cache con deliberazione, imposta scadenze e conosci la tua storia di correttezza prima di ottimizzare il tasso di successo. Al livello più basso, la [località dei riferimenti](https://en.wikipedia.org/wiki/Locality_of_reference), tenere vicini in memoria i dati usati insieme, sfrutta la gerarchia di cache della CPU e può rendere il codice diverse volte più veloce senza alcun cambiamento algoritmico, trasformando i mancati successi in successi. Gli array contigui battono le strutture che inseguono puntatori per questa ragione. Questo si interseca con le scelte di disposizione dei dati del capitolo 3.4.

### Fai benchmark onesti e diffida dei microbenchmark

Un benchmark che mente è peggio di nessuno, perché dà falsa confidenza. Riscalda prima di misurare, così da misurare il comportamento a regime anziché l'avvio una tantum e la compilazione just-in-time. Esegui molte iterazioni e riporta la varianza, non un singolo numero fortunato. Usa un carico di lavoro rappresentativo con dimensioni e distribuzioni di dati realistiche, perché un microbenchmark su un input giocattolo spesso misura la capacità del compilatore di cancellare il tuo test anziché la vera velocità del codice. Guardati dalle trappole classiche: un valore che l'ottimizzatore prova inutilizzato e rimuove, un ciclo che il runtime estrae o una cache calda nel benchmark e fredda in produzione. In caso di dubbio, misura l'intero percorso, non la funzione isolata.

### Controlla le prestazioni nella CI e osservale in produzione

Fai delle prestazioni una proprietà che la pipeline protegge. Aggiungi test di prestazioni alla strategia del capitolo 2.4, con cancelli di regressione che fanno fallire la build quando un benchmark chiave o un budget peggiora oltre una soglia. Questo coglie il lento scivolamento prima che venga integrato. Poi chiudi il cerchio in produzione con la telemetria del capitolo 9.2: segui i veri percentili di latenza, i tassi di allocazione e le query lente rispetto ai tuoi budget, perché il traffico di produzione trova i casi che i tuoi benchmark non hanno mai immaginato.

## Compromessi: vantaggi e svantaggi

| Approccio | Vantaggi | Svantaggi |
|---|---|---|
| Ottimizzare subito, per intuizione | Sembra produttivo; qualche vittoria fortunata | Di solito rifinisce il codice sbagliato; aggiunge complessità senza guadagno |
| Misurare prima, poi ottimizzare | Prende di mira il vero collo di bottiglia; basato sulle prove | Richiede strumenti e disciplina; più lento da avviare |
| Cache | Grandi guadagni di latenza e throughput | Bug di invalidazione; dati obsoleti; costo di memoria |
| Più parallelismo | Throughput più alto sul lavoro parallelo | Tetto di Amdahl; contesa; bug di concorrenza |
| Micro-ottimizzazione | Spreme i fattori costanti | Piccolo tetto; danneggia la leggibilità; spesso è rumore |
| Miglioramento algoritmico | Le vittorie scalano con la dimensione dell'input | Richiede analisi; a volte una riscrittura più grande |
| Cancelli di prestazioni nella CI | Ferma presto e a basso costo le regressioni | I benchmark instabili erodono la fiducia; serve un ambiente stabile |

La tensione centrale è tra sforzo e ritorno, e la risoluzione è la misura. Il lavoro sulle prestazioni ha rendimenti nettamente decrescenti: la prima correzione guidata dal profilo può dimezzare la latenza, la decima può togliere un punto percentuale raddoppiando la complessità del codice. La risolvi rifiutandoti di ottimizzare senza un numero in mano e un budget da raggiungere. Misura per trovare la correzione che vale la pena fare e fermati nel momento in cui superi il budget anziché inseguire la velocità fine a se stessa.

## Domande da discutere con il tuo team

1. **Avete un budget di prestazioni scritto per i vostri percorsi critici, ed è espresso come percentile?** Molti team hanno un vago senso che le cose dovrebbero essere "veloci" ma nessun numero rispetto a cui fallire, il che significa che le prestazioni non sono compito di nessuno finché qualcosa si rompe. Un budget come "p99 sotto 300 ms" rende concreto l'obiettivo, dà ai revisori qualcosa da far rispettare e trasforma una regressione in un evento visibile anziché in uno scivolamento lento. Conta di più nei grandi team, dove la latenza si insinua attraverso molte mani e nessun singolo autore vede il costo cumulativo. Porta i tuoi dati di latenza attuali e chiediti se riporti medie, che ti lusingano, o percentili, che dicono la verità. Se non sai dire che cosa significhi "abbastanza veloce" come numero, è la prima cosa da correggere.

2. **L'ultima volta che avete ottimizzato qualcosa, un profiler vi ha detto dove guardare, o avete tirato a indovinare?** Il collo di bottiglia è notoriamente altrove rispetto a dove gli ingegneri esperti se lo aspettano, e il tempo speso a rifinire il codice sbagliato è tempo perso due volte, una nel lavoro e una nella complessità aggiunta. Una cultura che profila per prima spende lo sforzo dove rende e lascia in pace il codice chiaro. Chiedi al tuo team di ricordare le ultime tre correzioni di prestazioni e se ciascuna sia partita da una misura o da un'intuizione. Valuta se riesci a profilare in produzione, o in un ambiente di staging realistico, perché un profilo da portatile può fuorviare gravemente. La risposta rivela se il tuo lavoro sulle prestazioni è ingegneria o folklore.

3. **Che cosa impedisce oggi a una regressione di prestazioni di raggiungere la produzione?** In un team in crescita, la risposta onesta è spesso "la lamentela di un cliente", il che significa che gli utenti sono il tuo test di regressione. Un cancello di CI che fa fallire la build quando un benchmark o un budget peggiora coglie il problema quando costa poco correggerlo e l'autore ricorda ancora la modifica. Discuti se i tuoi benchmark sono abbastanza stabili da farne un cancello, perché un test di prestazioni instabile che grida al lupo verrà ignorato o disattivato. Parla anche di che cosa osservi in produzione, poiché alcune regressioni compaiono solo con traffico e dati reali. L'obiettivo è fare delle prestazioni una proprietà che il sistema difende automaticamente, non una che riscopri durante un incidente.

4. **Ottimizzate per latenza o throughput su ogni percorso critico, e qualcuno ha messo per iscritto questa scelta?** Sono obiettivi diversi che tirano in direzioni opposte: raggruppamento e lavoratori paralleli alzano il throughput ma possono aggiungere latenza alle singole richieste, quindi un team che ottimizza d'istinto spesso compra l'asse sbagliato e fa aspettare gli utenti per risparmiare tempo macchina di cui nessuno era a corto. In un grande team il pericolo si moltiplica, perché un gruppo rifinisce un servizio condiviso per il throughput di massa mentre un altro ne dipende per la latenza interattiva, e nessuno conosce l'obiettivo dell'altro. Porta lo schema d'uso effettivo di ciascun percorso (richiesta interattiva rispetto a lotto in background), la latenza percentile attuale e il throughput sostenuto di cui hai bisogno, poi decidi esplicitamente l'asse anziché lasciare che emerga un valore predefinito. Per un sistema aziendale o governativo sotto un SLA, indica rispetto a quale metrica è scritto l'accordo, perché ottimizzare l'asse non misurato può violare un contratto mentre i tuoi cruscotti sembrano sani.

5. **Come sapete che i vostri benchmark misurano lavoro reale anziché l'ottimizzatore che cancella il vostro test?** Un benchmark che mente è peggio di nessuno, perché consegna al team falsa confidenza e poi una regressione viene comunque rilasciata. I team riportano di routine un singolo numero fortunato da un'esecuzione a freddo su un input giocattolo, che misura avvio, compilazione just-in-time e capacità del compilatore di rimuovere codice inutilizzato anziché il comportamento che gli utenti incontrano davvero. Porta un esempio di benchmark e interrogalo: si riscalda, esegue molte iterazioni, riporta la varianza, usa dimensioni e distribuzioni di dati rappresentative e sconfigge l'eliminazione del codice morto sul proprio risultato? La spinta contraria è che i benchmark onesti sono più lenti da scrivere ed eseguire dei microbenchmark rapidi, quindi concorda dove le approssimazioni economiche sono accettabili e dove pretendi rigore. In un contesto pubblico o regolamentato in cui appalti e organi di vigilanza ti chiederanno di riprodurre i numeri, cattura dispositivo, carico di lavoro e ambiente accanto al risultato così che l'affermazione possa essere verificata anziché solo asserita.

6. **Quando il lavoro sulle prestazioni compete con le funzionalità per gli stessi ingegneri, come decidete, e chi detiene l'autorità sul budget?** Le prestazioni hanno rendimenti nettamente decrescenti, quindi la prima correzione guidata dal profilo può dimezzare la latenza mentre la decima toglie un punto percentuale per il doppio della complessità del codice, e senza una regola vince la voce più forte o la scadenza più vicina. Le considerazioni in gioco sono reali: il debito di prestazioni non corretto si accumula in silenzio e diventa più costoso da sanare, eppure inseguire la velocità oltre il budget affama la roadmap e aggiunge complessità che rallenta il lavoro futuro. Porta lo stato attuale del budget per ogni percorso critico, il costo stimato dello stato attuale in macchine o conversioni perse e il ritorno marginale della prossima ottimizzazione, così che lo scambio sia fatto sulle prove anziché sulla pressione. Per una grande impresa o un programma governativo, indica chi possiede il budget di prestazioni e chi può autorizzare la spesa di tempo ingegneristico su di esso, perché un obiettivo che nessuno è responsabile di difendere è uno che si erode in silenzio.

## Lente settoriale

**Startup.** La velocità di consegna batte il processo, quindi resisti a riscritture e a grandi framework di prestazioni. Spendi un pomeriggio con un profiler sul percorso di cui gli utenti si lamentano davvero, correggi il costo più grande (spesso una query N+1 o una scansione lineare accidentale) e aggiungi un budget percentile leggero alla CI così che la vittoria non possa regredire in silenzio. Riserva l'ottimizzazione profonda al momento in cui un numero reale, non un'intuizione, dice che il codice è troppo lento.

**Piccola impresa.** Senza uno specialista di prestazioni e con un budget ridotto, appoggiati agli strumenti che già paghi: il profiler del tuo runtime, i percentili di latenza nel cruscotto dell'hosting e l'analizzatore di query integrato nel database. Fissa uno o due budget semplici legati a qualcosa che i clienti sentono, come il tempo di caricamento della pagina o del pagamento, e tratta una violazione come un segnale di comprare un livello più veloce o correggere la query peggiore anziché avviare un progetto di rifinitura che non sai dotare di personale.

**Grande impresa.** Alla scala di una flotta, le prestazioni sono costo diretto, quindi governale come disciplina condivisa: strumenti di profilazione standard, budget percentili legati a metriche di business e cancelli di regressione nella CI applicati in modo coerente, così che il lento scivolamento di un singolo team non gonfi l'intera bolletta cloud. Segui latenza, allocazione e throughput rispetto ai valori di riferimento tra i servizi e conserva evidenze di benchmark riproducibili, perché una riduzione del 30% della CPU su una grande flotta è un risparmio ricorrente che vale la pena verificare e difendere dalle penali degli SLA.

**Ente pubblico.** Le prestazioni sono una garanzia di accesso: una pagina che si carica su un vecchio telefono con una connessione debole decide se un cittadino completa una richiesta di prestazione. Fissa budget espliciti rispetto a dispositivi realistici di fascia bassa e reti limitate e pubblica risultati di benchmark riproducibili che catturino dispositivo, rete e carico di lavoro, così che appalti e organi di vigilanza possano verificare i numeri anziché prenderli per fede. Preferisci una misurazione trasparente e verificabile alle asserzioni dei fornitori e pretendi dai fornitori le stesse evidenze riproducibili.

## Esempi

**Startup.** Un piccolo team SaaS nota che la propria dashboard è lenta ed è tentato di riscriverla in un framework più veloce. Invece spendono un pomeriggio con un profiler e un flame graph, che mostra che il 70% del tempo di richiesta è un singolo endpoint che emette una query al database per riga, il classico schema N+1. La sostituiscono con una query raggruppata, la latenza scende da 1,2 secondi a 90 millisecondi e aggiungono un budget p99 di 200 ms a un leggero benchmark di CI così che la correzione non possa regredire in silenzio. Nessuna riscrittura, un pomeriggio, una vittoria di dieci volte.

**Grande impresa.** Una piattaforma di vendita al dettaglio gestisce migliaia di istanze e la sua bolletta cloud è dominata da un servizio di raccomandazioni. Una campagna di profilazione trova un forte rimescolio di allocazioni che causa frequenti pause della garbage collection, più una cache con un basso tasso di successo. Rifinire le strutture dati per la località e correggere le chiavi della cache riduce la CPU per richiesta del 40%, il che permette al team di far girare lo stesso traffico su il 40% di macchine in meno. Il risparmio ripaga lo sforzo ingegneristico in settimane, e un SLA sulla latenza p99 che a volte veniva violato ora regge comodamente, evitando penali contrattuali.

**Ente pubblico.** Un'autorità fiscale nazionale deve servire i cittadini su vecchi dispositivi e connessioni rurali lente. Il team fissa un budget esplicito: la pagina di dichiarazione deve diventare interattiva in meno di 3 secondi su un telefono di fascia bassa con un profilo 3G limitato. Profilano la pagina, tagliano il lavoro che blocca l'interattività e pubblicano risultati di benchmark riproducibili, catturando dispositivo, rete e carico di lavoro, così che organi di vigilanza e auditor di accessibilità possano verificare l'affermazione anziché prenderla per fede. Le prestazioni qui non sono una leva di costo ma una garanzia di accesso che mantiene utilizzabile il servizio per tutti.

## Business case: motivazioni, ROI e TCO

Il ritorno dell'ingegneria delle prestazioni si vede in tre registri. Il primo è il costo dell'infrastruttura: codice più veloce fa lo stesso lavoro su meno macchine, e per una grande flotta una riduzione del 30% della CPU è un risparmio diretto e ricorrente che supera di gran lunga lo sforzo ingegneristico una tantum. Il secondo è ricavo e soddisfazione: la latenza correla con conversione, abbandono e fiducia degli utenti, quindi tagliare la coda è una leva di crescita, non solo un compito di igiene. Il terzo è il rischio evitato: la violazione di uno SLA porta penali, e un lancio che si squaglia sotto carico porta danno reputazionale e costo di spegnimento incendi.

Il costo totale di proprietà è modesto e concentrato all'inizio. Si investe in strumenti di profilazione, un ambiente di benchmark stabile e cancelli di CI, più la disciplina di scrivere budget e leggere profili. Il costo più grande e nascosto è l'alternativa: il debito di prestazioni si accumula in silenzio, e adattare a posteriori la velocità a un sistema lento dopo il lancio costa molto più che proteggerla di continuo. Presenta il caso alla leadership nelle sue unità. Traduci la latenza in tassi di conversione o di completamento dei cittadini, traduci la CPU in spesa cloud mensile e traduci un cancello di regressione in incidenti evitati. L'argomento più forte è che le prestazioni sono economiche da proteggere commit dopo commit e rovinose da recuperare dopo che sono marcite.

## Antipattern e insidie

- **Ottimizzare senza profilare.** Rifinire codice che non è il collo di bottiglia mentre il costo reale resta intatto.
- **Ottimizzazione prematura.** Sacrificare chiarezza per una velocità immaginata che il profiler non avrebbe mai segnalato.
- **Riportare medie.** Nascondere una coda dolorosa dietro una media confortevole; gli utenti sentono il p99, non la media.
- **Teatro dei microbenchmark.** Numeri da un carico giocattolo che l'ottimizzatore ha mezzo cancellato, senza riscaldamento né varianza riportata.
- **Cache senza una storia di invalidazione.** Inseguire il tasso di successo servendo dati obsoleti o sbagliati.
- **Presumere che più thread aiutino.** Ignorare la legge di Amdahl e la frazione seriale, poi affogare nella contesa.
- **Nessun cancello di regressione.** Lasciare che gli utenti siano il test di prestazioni perché nulla nella CI protegge il budget.
- **Ottimizzare l'asse sbagliato.** Comprare throughput con il raggruppamento quando gli utenti avevano bisogno di bassa latenza, o il contrario.

## Modello di maturità

- **Livello 1, Avvio:** le prestazioni si affrontano solo quando qualcosa si rompe. Nessun budget, nessuna abitudine di profilazione, nessun benchmark. L'ottimizzazione è un tirare a indovinare guidato dall'intuito e le medie sono l'unica metrica che qualcuno riporta.
- **Livello 2, Sviluppo:** alcuni team profilano durante gli incidenti e tengono qualche benchmark, ma la pratica è incoerente e dipende dall'entusiasmo individuale. I budget esistono in modo informale per un percorso critico o due e i percentili compaiono su alcuni cruscotti, ma nulla fa da cancello a una regressione prima del rilascio e ogni team reinventa il proprio approccio.
- **Livello 3, Standardizzazione:** i percorsi critici portano budget percentili scritti e la profilazione è il primo passo documentato e atteso prima che qualcuno ottimizzi. La CI comprende test di prestazioni con cancelli di regressione, le regole di benchmark onesto (riscaldamento, varianza, dati rappresentativi) sono scritte e fatte rispettare in tutta l'organizzazione e ogni team segue lo stesso metodo anziché il proprio.
- **Livello 4, Gestione:** l'organizzazione misura le prestazioni come proprietà controllata. Percentili di latenza, throughput, tassi di allocazione e numero di query lente sono seguiti rispetto a valori di riferimento espliciti in produzione e nella CI, le regressioni sono quantificate rispetto a soglie anziché discusse e i budget sono legati a metriche di business come conversione o spesa cloud, così che una violazione inneschi una decisione basata sui dati. Le evidenze di benchmark sono riproducibili e catturate con dispositivo, carico di lavoro e ambiente per l'audit.
- **Livello 5, Orchestrazione:** le prestazioni sono migliorate di continuo e integrate in tutta l'organizzazione. Budget, profilazione, benchmark onesto e analisi dei flame graph sono competenze di routine, i cancelli di regressione sono stabili e affidabili e i dati di produzione e CI chiudono il ciclo in modo automatico. L'organizzazione adatta i budget al mutare di traffico, hardware e priorità di business, riequilibra lo sforzo verso i percorsi dove il ritorno è più alto e difende le prestazioni come proprietà permanente anziché come campagna periodica.

## Spunti di discussione

1. Quale dei vostri percorsi critici ha oggi un budget scritto e basato sui percentili, e quali sono protetti solo dalla speranza?
2. Quando un profiler vi ha sorpreso l'ultima volta, e che cosa vi ha insegnato su dove presumete vada il tempo?
3. I vostri benchmark si riscaldano, riportano la varianza e usano dati rappresentativi, o stanno misurando l'ottimizzatore?
4. Dove state spendendo macchine per coprire codice che una campagna di profilazione potrebbe rendere più economico?
5. Per il vostro carico più parallelizzato, qual è la frazione seriale, e la legge di Amdahl limita l'accelerazione che state inseguendo?
6. Se un collega integrasse una modifica che raddoppia la latenza p99, quanto passerebbe prima che qualcuno se ne accorga, e come lo scoprirebbe?

## Punti chiave

- Misura prima di ottimizzare; il collo di bottiglia è raramente dove immagini e l'ottimizzazione prematura costa chiarezza senza guadagno.
- Definisci "abbastanza veloce" come un budget percentile, perché le medie nascondono la coda dove vivono gli utenti reali.
- Preferisci vittorie algoritmiche (una classe O-grande migliore) alla rifinitura minuta e sappi se ti serve latenza o throughput.
- Rispetta i limiti del parallelismo (legge di Amdahl) e i rischi della cache (invalidazione e obsolescenza).
- Fai benchmark onesti con riscaldamento, varianza e carichi rappresentativi e diffida dei microbenchmark.
- Controlla le prestazioni nella CI (capitolo 2.4) e osservale in produzione (capitolo 9.2); affianca la vista a livello di sistema del capitolo 3.5.
- Le prestazioni sono costo per le imprese, accesso per gli enti pubblici, economiche da proteggere di continuo e costose da adattare a posteriori.

## Riferimenti e letture di approfondimento

- Brendan Gregg, *Systems Performance: Enterprise and the Cloud* (profilazione, flame graph e metodo).
- Brendan Gregg, *BPF Performance Tools* (osservabilità e profilazione pratiche su Linux).
- Donald E. Knuth, "Structured Programming with go to Statements" (*ACM Computing Surveys*, 1974): la fonte della massima sull'ottimizzazione prematura.
- Donald E. Knuth, *The Art of Computer Programming* (analisi algoritmica e complessità).
- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest e Clifford Stein, *Introduction to Algorithms* (O-grande ed efficienza algoritmica).
- Gene M. Amdahl, "Validity of the Single Processor Approach to Achieving Large-Scale Computing Capabilities" (1967): l'origine della legge di Amdahl.
- Ulrich Drepper, "What Every Programmer Should Know About Memory" (la gerarchia di memoria e la località dei dati).
- Martin Kleppmann, *Designing Data-Intensive Applications* (latenza, throughput e comportamento di coda nei sistemi).
- Aleksey Shipilev, "JMH and the pitfalls of microbenchmarking" (pratica di benchmark onesto su runtime gestiti).
- Ilya Grigorik, *High Performance Browser Networking* (prestazioni lato client e di rete per utenti con poca banda).
