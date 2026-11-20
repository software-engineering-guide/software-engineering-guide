# 10.6 Gestione dei progetti

## Panoramica e motivazioni

La [gestione dei progetti](https://en.wikipedia.org/wiki/Project_management) è la disciplina di trasformare l'intento in esiti consegnati sotto vincoli. Coordini persone, ambito, calendario, costo, rischio e qualità così che il lavoro finisca davvero e consegni valore. Nel software è spesso trattata con sospetto, legata a piani pesanti e [diagrammi di Gantt](https://en.wikipedia.org/wiki/Gantt_chart) che la realtà ignora. Ma il bisogno di fondo non scompare mai. Qualcuno deve assicurarsi che il lavoro giusto avvenga nell'ordine giusto, che le dipendenze siano gestite, che i rischi emergano presto e che gli [stakeholder](https://en.wikipedia.org/wiki/Project_stakeholder) sappiano che cosa aspettarsi. La domanda non è *se* gestire i progetti, ma *quanto leggermente e in modo adattivo* puoi farlo rispettando comunque i tuoi obblighi.

Perché trattarlo esplicitamente? I progetti software falliscono a tassi allarmanti e falliscono molto più spesso per ragioni di gestione che per ragioni puramente tecniche: ambito poco chiaro, dipendenze non gestite, rischio non affrontato, stakeholder assenti e la fantasia di stime precise a lungo raggio. I grandi programmi sono particolarmente esposti: con molti team, fornitori e orizzonti di più trimestri, piccoli fallimenti di coordinamento si compongono. La buona gestione dei progetti è in gran parte la pratica di prendere impegni onesti, scomporre sensatamente il lavoro e creare un riscontro rapido così che i problemi emergano finché sono ancora economici da correggere.

I contesti aziendali e governativi alzano la posta e cambiano i vincoli. Le imprese gestiscono portafogli di iniziative intrecciate rispetto a strategia e cicli di bilancio (capitolo 10.1). I governi aggiungono regole di appalto, stanziamenti pluriennali, gestione degli appaltatori e responsabilità pubblica. Lì, il predefinito storico (contratti grandi, a ambito fisso, [a cascata](https://en.wikipedia.org/wiki/Waterfall_model)) ha una lunga storia di fallimenti costosi e visibili. Questo capitolo copre i fondamentali che si applicano tra approcci predittivi, adattivi e ibridi. Il capitolo 10.7 (Agile) approfondisce la consegna adattiva e il capitolo 10.1 copre la gestione di portafoglio e programmi sopra il singolo progetto.

## Principi chiave

- **Gestisci esiti, non attività.** Finito significa valore consegnato, non compiti chiusi.
- **Scomponi e ordina.** Un lavoro piccolo, ordinato e consapevole delle dipendenze batte i piani big-bang.
- **Le stime sono intervalli, non promesse.** Comunica onestamente l'incertezza.
- **Fai emergere il rischio presto e di continuo.** Il problema più economico è quello colto per primo.
- **Adegua il metodo al lavoro.** Predittivo, adattivo o ibrido: in base a incertezza e vincoli.
- **Rendi trasparente lo stato.** Un flusso visibile batte i report rassicuranti.
- **Gli stakeholder sono parte del team.** L'assenza del cliente è un rischio del progetto.

## Raccomandazioni

### Scegli deliberatamente predittivo, adattivo o ibrido

Non esiste un modello di consegna universalmente corretto; esiste un adattamento tra metodo e contesto:

- **Predittivo (guidato dal piano, "a cascata"):** ambito fissato in anticipo, poi calendario e costo derivati. Si adatta al lavoro con requisiti davvero stabili e ben compresi e vincoli esterni rigidi (certificazione normativa, integrazione fisica). La sua modalità di fallimento è fingere che i requisiti del software siano stabili quando non lo sono.
- **Adattivo ([agile](https://en.wikipedia.org/wiki/Agile_software_development)):** l'ambito si flette; tempo e costo sono fissati in brevi iterazioni che consegnano software funzionante e assorbono l'apprendimento. Si adatta alla maggior parte del lavoro di prodotto e servizi digitali, dove i requisiti si scoprono (capitoli 11.1, 10.7).
- **Ibrido:** un nucleo adattivo dentro un guscio di governance predittivo, comune e spesso corretto in impresa e governo, dove finanziamento, conformità e contratti richiedono tappe e audit mentre la consegna beneficia dell'iterazione.

Quadri come il [PMBOK](https://en.wikipedia.org/wiki/Project_Management_Body_of_Knowledge) (Project Management Body of Knowledge, del [Project Management Institute](https://en.wikipedia.org/wiki/Project_Management_Institute)) e [PRINCE2](https://en.wikipedia.org/wiki/PRINCE2) (PRojects IN Controlled Environments) codificano la pratica predittiva e ibrida. Il punto è prendere in prestito la loro disciplina (ruoli, rischio, cancelli di fase) senza importare cerimonie di cui il lavoro non ha bisogno.

### Gestisci l'ambito rispetto al triplice vincolo

Ambito, calendario e costo si muovono insieme, delimitati dalla qualità: il classico ["triangolo di ferro"](https://en.wikipedia.org/wiki/Project_management_triangle). Non puoi fissarli tutti e tre e aggiungere ambito gratis. Qualcosa cede e fingere il contrario è come cominciano le [marce della morte](https://en.wikipedia.org/wiki/Death_march_(project_management)). Rendi espliciti i compromessi e decidi *quale* variabile si flette. I metodi adattivi fissano tempo e costo e flettono l'ambito. I contratti a prezzo fisso fissano ambito e costo e in realtà flettono qualità o calendario a meno di gestirli. Controlla lo [scope creep](https://en.wikipedia.org/wiki/Scope_creep) con un processo di modifica leggero (capitolo 12.3) e preferisci *ridurre l'ambito a un nucleo prezioso* a far slittare tutto.

### Stima onestamente, in intervalli, e ripeti la previsione

La stima è dove i progetti più spesso mentono a sé stessi. Tratta le stime come intervalli probabilistici, non singoli numeri e allargale per il lavoro lontano e poco compreso (il ["cono dell'incertezza"](https://en.wikipedia.org/wiki/Cone_of_Uncertainty)). Preferisci metodi relativi ed empirici: il throughput storico e il tempo di ciclo (capitoli 11.2, 11.3) prevedono meglio delle congetture eroiche dal basso. Dove puoi, sostituisci la stima con la *misura*. Un team che chiude 8 voci a settimana impiegherà circa 5 settimane per 40 voci, a prescindere dai punti storia (di nuovo la [legge di Little](https://en.wikipedia.org/wiki/Little%27s_law): throughput e lavoro in corso, non le stime, fissano il tempo di consegna). Ripeti la previsione di continuo man mano che arriva la realtà. Un piano che non cambia mai non è gestito.

### Gestisci le dipendenze e il percorso critico

Su larga scala, il rischio dominante raramente è la velocità di un solo team. Sono le *dipendenze tra team e fornitori*. Mappale esplicitamente, individua il [percorso critico](https://en.wikipedia.org/wiki/Critical_path_method) (la sequenza che determina il termine più precoce) e attacca per prime le dipendenze più lunghe e più rischiose. Riduci l'accoppiamento dove puoi (una dipendenza rimossa vale più di una dipendenza tracciata) e usa interfacce e contratti chiari così che i team possano progredire in parallelo (capitoli 1.2, 2.3). Per i programmi tra team, una regolare sincronizzazione su dipendenze e rischi batte un report di stato che nessuno legge.

### Tieni un registro dei rischi vivo

La gestione del rischio è l'attività di gestione dei progetti a più alta leva e la più spesso saltata. Tieni un semplice e vivo **[registro dei rischi](https://en.wikipedia.org/wiki/Risk_register)**: ogni rischio con probabilità, impatto, responsabile e mitigazione o piano di contingenza (capitolo 12.3). Rivedilo regolarmente, ritira i rischi passati e aggiungi quelli nuovi man mano che emergono. Distingui i rischi (potrebbero accadere) dai problemi (stanno già accadendo) e dalle decisioni (capitolo 1.6). L'obiettivo non è un documento. È un'abitudine di guardare avanti, così da anticipare i problemi anziché scoprirli alla scadenza.

### Coinvolgi gli stakeholder e comunica con trasparenza

La maggior parte dei fallimenti di progetto "a sorpresa" era visibile presto a qualcuno che non è stato ascoltato. Identifica gli stakeholder, capisci le loro preoccupazioni e tienili davvero coinvolti. L'assenza del cliente è essa stessa un rischio principale. Comunica lo stato attraverso un *flusso trasparente* (bacheche visibili, grafici burn-up, software funzionante dimostrato) anziché report verde-giallo-rosso che premiano l'ottimismo. Fai escalation con onestà e presto. Un progetto ben gestito fa viaggiare in fretta le cattive notizie.

## Compromessi: vantaggi e svantaggi

| Approccio | Vantaggi | Svantaggi |
|---|---|---|
| **Predittivo / a cascata** | Ambito e costo prevedibili; adatto a contratti e audit | Scarso adattamento a requisiti incerti; riscontro tardivo; rischio big-bang |
| **Adattivo / agile** | Riscontro rapido; assorbe il cambiamento; valore precoce | Più difficile fissare in anticipo ambito/costo; richiede un cliente coinvolto |
| **Ibrido** | Iterazione dentro la governance; adatto a impresa/governo | Tensione tra cadenze; può ereditare entrambi gli oneri |
| **Stime dettagliate in anticipo** | Conforto per pianificatori e finanziatori | Precisamente sbagliate; costose da produrre; decadono in fretta |
| **Previsione empirica (metriche di flusso)** | Fondata, autocorrettiva | Richiede storia e disciplina; sembra meno "certa" |
| **Pesante cerimonia di rischio/processo** | Accurata; buona per programmi ad alta posta | Rallenta i piccoli team; può diventare spunta di caselle |

La tensione centrale è **prevedibilità contro adattabilità**. Finanziatori, contratti e audit vogliono impegni fermi. Il lavoro software incerto ha bisogno di spazio per imparare. Risolvilo come fa l'Agile (capitolo 10.7): impegnati con fermezza su esiti e scadenze lasciando flettere l'ambito e usa una governance ibrida per soddisfare la supervisione senza congelare la consegna.

## Domande da discutere con il tuo team

1. **Come avvolgerete i team di consegna adattivi in un guscio di governance predittivo senza ereditare l'onere di entrambi?** L'ibrido è comune e spesso corretto in impresa e governo, dove cicli di finanziamento, conformità e contratti richiedono tappe e audit mentre la consegna beneficia dell'iterazione. Il rischio è reale: un ibrido progettato male eredita insieme la pesante documentazione della cascata e le cerimonie dell'agile e i team sentono l'attrito di due cadenze che si combattono. Portate evidenza: mappate dove cadono davvero i vostri cancelli di finanziamento, i punti di controllo di conformità e le tappe contrattuali e verificate se ciascuno richiede un documento che il lavoro di consegna non produce altrimenti. La risposta dovrebbe lasciare che l'iterazione soddisfi la supervisione anziché combatterla, alimentando il ritmo di governance con incrementi funzionanti dimostrati e un registro dei rischi vivo anziché fermarsi ad assemblare report separati. Prendete in prestito la disciplina di un quadro come PRINCE2 senza importare cerimonie di cui il lavoro non ha bisogno.

2. **Il vostro stato di progetto è flusso trasparente, o report verde-giallo-rosso che premiano l'ottimismo?** La maggior parte dei fallimenti a sorpresa era visibile presto a qualcuno che non è stato ascoltato e lo stato "anguria" (verde fuori, rosso dentro) è come le cattive notizie oneste restano sepolte fino alla scadenza. Sostituite i report rassicuranti con bacheche visibili, grafici burn-up e software funzionante dimostrato e rendete l'escalation precoce un atto sicuro anziché un rischio di carriera. Portate evidenza: guardate il vostro ultimo progetto in difficoltà e chiedetevi quando è esistito il primo segnale d'allarme rispetto a quando la leadership l'ha sentito. L'assenza del cliente è essa stessa un rischio principale, quindi controllate se uno stakeholder coinvolto è davvero nel ciclo o se state costruendo con sicurezza verso la cosa sbagliata. Un progetto ben gestito fa viaggiare in fretta le cattive notizie e la correzione è tanto culturale quanto di strumenti.

3. **Conoscete il nucleo minimo prezioso a cui riducereste l'ambito se calendario e costo smettessero di muoversi?** Ambito, calendario e costo si muovono insieme delimitati dalla qualità e quando i finanziatori fissano tutti e tre, la qualità diventa la valvola di sfogo silenziosa e cominciano le marce della morte. I metodi adattivi fissano tempo e costo e flettono l'ambito, il che funziona solo se avete già deciso quale fetta consegna valore vero e quali funzionalità sono negoziabili. Portate evidenza: per il vostro attuale rilascio, sapete nominare il nucleo che deve essere rilasciato e l'elenco che tagliereste per primo, o ogni funzionalità è trattata in silenzio come obbligatoria? La risposta dovrebbe permettervi di ridurre l'ambito a un nucleo prezioso anziché far slittare tutto e dovrebbe essere stabilita prima che arrivi la pressione, non improvvisata alla scadenza. Controllate il resto con un processo di modifica leggero così che lo scope creep non mangi il margine su cui contavate.

4. **Quale dipendenza tra team è sul vostro percorso critico in questo momento, e chi risponde di rimuoverla o ridurne il rischio?** Su larga scala la minaccia dominante raramente è la velocità di un solo team; è la sequenza di dipendenze tra team e fornitori che fissa il termine più precoce possibile. Se nessuno sa nominare l'attuale dipendenza del percorso critico, state gestendo il progresso locale mentre ciò che governa davvero la vostra data deriva non osservato. Portate evidenza: una mappa delle dipendenze che mostra quali passaggi alimentano quali, dove corre la catena più lunga e quali collegamenti sono ancora non costruiti o contrattualmente bloccati, più un responsabile nominato per ogni collegamento rischioso. Puntate ad attaccare per prime le dipendenze più lunghe e più rischiose e a rimuovere l'accoppiamento dove potete, perché una dipendenza eliminata vale più di una dipendenza tracciata. Nei programmi aziendali e governativi i collegamenti più difficili spesso attraversano i confini di fornitori o enti, quindi nominate il responsabile su ciascun lato e confermate che il contratto gli permetta di agire, o la dipendenza resterà irrisolta finché non diventa un ritardo pubblico.

5. **Come ripetete la previsione man mano che arriva la realtà, e quanto in fretta uno slittamento diventa visibile a chi finanzia il lavoro?** Un piano che non cambia mai non è gestito; è difeso e una data a numero singolo difesa oltre l'evidenza è come i progetti slittano in silenzio fino alla scadenza. Sostituite la stima con la misura ovunque possiate, prevedendo da throughput storico e tempo di ciclo anziché da congetture eroiche dal basso e allargate l'intervallo per il lavoro lontano e poco compreso. Portate evidenza: il vostro vero tasso di completamento settimanale, la dimensione attuale dell'arretrato e il termine proiettato che ne deriva, confrontati con la data che la leadership crede attualmente. La risposta dovrebbe dare ai finanziatori una proiezione onesta e che si restringe che vedono a ogni ciclo anziché una data fissa che regge finché collassa. Nel governo e in altri contesti vincolati dagli stanziamenti, una previsione che fa emergere presto lo slittamento vi permette di ridefinire l'ambito o ribasare entro le regole, mentre uno slittamento nascosto diventa un fallimento di supervisione e un titolo di giornale.

6. **Qual è il processo più leggero che soddisfa comunque i vostri veri obblighi, e dove la cerimonia si è staccata dal ridurre il rischio?** Sia gestire troppo poco sia troppo ha un costo reale: caos, rilavorazione e dipendenze perse da una parte e spunta di caselle che rallenta la consegna senza abbassare il rischio dall'altra. La tensione è che audit, conformità e termini contrattuali impongono veri requisiti, eppure i team tendono a tenere ogni rituale molto dopo che ha smesso di guadagnarsi il posto. Portate evidenza: per ogni report, cancello e riunione ricorrente, nominate l'obbligo o il rischio specifico che affronta e segnalate quelli che nessuno sa ricondurre a nessuno dei due. La risposta dovrebbe permettervi di ritirare la cerimonia che produce solo rassicurazione preservando gli artefatti che soddisfano un vero auditor o finanziatore. Nei contesti aziendali e governativi, mappate ogni cerimonia alla regola di stanziamento, appalto o normativa nominata che serve, così da poter difendere il taglio del resto davanti alla supervisione anziché tirare a indovinare che cosa la conformità richieda.

## Lente settoriale

**Startup.** Gestisci con quasi nessuna cerimonia ma con vera disciplina. Scomponi il rilascio in piccole fette ordinate, impegnati su una data di lancio lasciando che l'ambito si fletta verso un nucleo prezioso e indica ai fondatori un intervallo anziché una data singola, ripetendo la previsione ogni settimana da quante fette chiudi davvero. Un registro dei rischi di dieci righe in un documento condiviso che nomina l'unica dipendenza che potrebbe affondare la data, con un responsabile e un ripiego, vale più di qualsiasi strumento, perché la tua risorsa più scarsa è l'attenzione e uno slittamento colto tardi può porre fine all'azienda.

**Piccola impresa.** Non hai un responsabile di progetto e hai poco margine, quindi appoggiati agli strumenti che già gestisci anziché montare un ufficio di governance. Segui il lavoro su un'unica bacheca visibile, tieni un breve elenco di rischi vivo e privilegia comprare un prodotto di pianificazione o ticketing anziché costruire il processo da zero. Decidi in anticipo quale singola funzionalità deve essere rilasciata perché valga la pena fare il rilascio, perché quando il calendario si stringe non avrai persone di riserva per negoziare l'ambito al momento.

**Grande impresa.** Il problema è il coordinamento tra molti team, fornitori e cicli di finanziamento. Avvolgi i team adattivi in un guscio di governance predittivo, alimenta il ritmo delle tappe con incrementi dimostrati e un registro dei rischi vivo anziché assemblare report separati e mantieni una mappa delle dipendenze tra team così che il percorso critico sia gestito anziché scoperto. Standardizza nel portafoglio stime basate su intervalli e ripetute empiricamente così che la leadership confronti i progetti su proiezioni oneste e che si restringono anziché su date fisse ottimistiche.

**Ente pubblico.** Regole di appalto, stanziamenti pluriennali e responsabilità pubblica plasmano ogni scelta. Privilegia incrementi modulari e basati sugli esiti consegnati in modo adattivo sotto un quadro di governance che soddisfa stanziamenti e supervisione, anziché un unico contratto a cascata a prezzo fisso e ambito fisso con un go-live lontano. Un registro dei rischi vivo e incrementi trasparenti e dimostrati danno a auditor e legislatori una visibilità reale e flettere l'ambito verso un nucleo prezioso dentro un finanziamento fisso ti permette di rilasciare presto una capacità utile anziché rischiare tutto su una sola data.

## Esempi

**Startup.** Una startup di sette persone che corre per rilasciare il suo primo prodotto a pagamento gestisce il progetto con quasi nessuna cerimonia ma con vera disciplina. Scompone il rilascio in piccole fette ordinate, si impegna su una data di lancio lasciando che l'ambito si fletta verso un nucleo prezioso anziché promettere ogni funzionalità e indica ai fondatori un intervallo anziché una data singola, ripetendo la previsione ogni settimana da quante fette il team chiude davvero. Un registro dei rischi di dieci righe in un documento condiviso nomina l'unica dipendenza che potrebbe affondare la data, un'integrazione di pagamenti non finita, con un responsabile e un ripiego, così che la minaccia maggiore sia osservata anziché scoperta alla scadenza.

**Grande impresa.** Una banca che sostituisce la propria piattaforma di erogazione dei prestiti gestisce un programma ibrido: un guscio predittivo con tappe di finanziamento trimestrali e cancelli di conformità, che avvolge team adattivi che consegnano incrementi funzionanti ogni due settimane. Una mappa delle dipendenze tra team espone che un servizio di identità condiviso è sul percorso critico. Così il programma lo ordina per primo e ne riduce il rischio, evitando una cascata tardiva. Le stime sono espresse come intervalli e ripetute ogni mese dal throughput effettivo, così che la leadership veda una proiezione onesta e che si restringe anziché una data fissa che slitta in silenzio.

**Ente pubblico.** Un ente abbandona un singolo contratto a cascata a prezzo fisso e ambito fisso (lo schema dietro diversi fallimenti pubblici) a favore di appalti modulari: incrementi più piccoli e basati sugli esiti consegnati in modo adattivo sotto un quadro di governance che soddisfa stanziamenti e supervisione. Un registro dei rischi vivo e incrementi trasparenti e dimostrati danno a auditor e legislatori una visibilità reale. Poiché l'ambito si flette verso un nucleo prezioso dentro un finanziamento fisso, il programma può rilasciare presto una capacità utile anziché rischiare tutto su un unico go-live lontano (capitoli 10.1, 10.3).

## Business case: motivazioni, ROI e TCO

Il ritorno di una buona gestione dei progetti è dominato dal **fallimento evitato**. I grandi progetti software hanno molta più probabilità di essere in ritardo, fuori budget o cancellati che di rispettare un piano fisso originale e le perdite sono enormi: costo irrecuperabile, più valore non realizzato e, nel governo, danno pubblico e politico. Le discipline qui (stima onesta, gestione delle dipendenze, lavoro precoce sul rischio, stakeholder coinvolti e ambito adattivo) sono esattamente quelle che spostano un progetto fuori dalla curva del fallimento. Anche un modesto taglio della probabilità di un grande sforamento o di una cancellazione fa impallidire il costo di gestire bene il progetto.

Sul **costo totale di proprietà**, una gestione leggera e adattiva abbassa il costo lungo la vita del lavoro. Un riscontro rapido coglie presto gli errori costosi. La consegna incrementale comincia a restituire valore prima, il che migliora i tempi del ROI. Un flusso trasparente riduce l'onere di reportistica che una governance pesante impone. Sia gestire *troppo poco* (caos, rilavorazione, dipendenze perse) sia *troppo* (cerimonia che rallenta la consegna) ha un costo reale. L'obiettivo è il processo più leggero che soddisfa i tuoi obblighi effettivi. Presenta il caso alla leadership contrapponendo il costo a pieno carico di un recente progetto in difficoltà al costo quasi nullo di un registro dei rischi, di una mappa delle dipendenze e di previsioni oneste basate su intervalli.

## Antipattern e insidie

- **Piani con tutto fisso:** ambito, calendario e costo tutti bloccati, con la qualità come valvola di sfogo silenziosa.
- **Stime come promesse:** date a numero singolo trattate come impegni, poi difese oltre l'evidenza.
- **Ignorare le dipendenze:** gestire la velocità di ogni team mentre il percorso critico tra team slitta.
- **Teatro del registro dei rischi:** un documento creato una volta e mai rivisto.
- **Stato anguria:** verde fuori, rosso dentro; ottimismo premiato sull'onestà.
- **Cliente assente:** nessuno stakeholder coinvolto, così si costruisce con sicurezza la cosa sbagliata.
- **Consegna big-bang:** tutto integrato e rilasciato alla fine, massimizzando il rischio (confronta il capitolo 11.2).
- **Processo fine a sé stesso:** cerimonia e report che consumano sforzo senza ridurre il rischio.

## Modello di maturità

- **Livello 1 (Avvio):** I progetti corrono su eroismi e speranza; ambito, rischio e dipendenze sono gestiti ad hoc se lo sono; le stime sono singoli numeri difesi oltre l'evidenza; le sorprese arrivano alla scadenza.
- **Livello 2 (Sviluppo):** Pianificazione di base, reportistica di stato e un elenco di rischi esistono su alcuni progetti ma non su altri; il metodo di consegna è scelto per abitudine anziché per adattamento; stima e tracciamento delle dipendenze variano da team a team, quindi la pratica è incoerente nell'organizzazione.
- **Livello 3 (Standardizzazione):** Un approccio documentato è fatto rispettare in tutta l'organizzazione: il metodo di consegna è scelto per adattarsi al lavoro, l'ambito è gestito rispetto al triplice vincolo, ci si aspetta su ogni progetto un registro dei rischi vivo e una mappa delle dipendenze e le stime sono basate su intervalli e ripetute con stakeholder coinvolti.
- **Livello 4 (Gestione):** La consegna è misurata e controllata rispetto a valori di riferimento. Throughput, tempo di ciclo, accuratezza delle previsioni, tassi di chiusura di dipendenze e rischi e varianza di calendario e costo sono seguiti per progetto e riportati nel portafoglio; le proiezioni sono empiriche e si restringono; gli slittamenti emergono presto e innescano ridefinizione dell'ambito o ribasamento sull'evidenza anziché sull'ottimismo.
- **Livello 5 (Orchestrazione):** La gestione dei progetti è integrata con pianificazione di portafoglio, finanziamento e rischio e continuamente migliorata. La governance ibrida soddisfa la supervisione senza rallentare la consegna, le dipendenze tra team e tra fornitori sono gestite in modo proattivo, le retrospettive riportano nella pratica un cambiamento misurato e l'organizzazione adatta i propri metodi e riequilibra il lavoro man mano che si spostano vincoli e priorità.

## Spunti di discussione

1. Quale metodo di consegna (predittivo, adattivo, ibrido) ha davvero bisogno ciascuna delle vostre attuali iniziative, e corrisponde a quello che state usando?
2. Quando vi siete impegnati per l'ultima volta su una data, era un intervallo o un singolo numero, e come ha plasmato le aspettative?
3. Qual è la dipendenza del percorso critico tra i vostri team in questo momento, e chi risponde di ridurne il rischio?
4. Il vostro registro dei rischi è un'abitudine viva o un documento una tantum?
5. Dove la qualità sta assorbendo in silenzio la pressione quando ambito, calendario e costo sono tutti fissi?
6. Come cambierebbero le vostre previsioni se sostituiste la stima con il throughput misurato?

## Punti chiave

- La gestione dei progetti trasforma l'intento in esiti consegnati sotto il vincolo di ambito, calendario, costo e qualità.
- **Adegua il metodo al lavoro:** predittivo, adattivo o ibrido e privilegia la governance ibrida in impresa e governo.
- Tratta le **stime come intervalli**, ripeti la previsione da **metriche di flusso empiriche** e non lasciare che le date a numero singolo diventino bugie.
- **Dipendenze e rischio** sono le modalità di fallimento dominanti su larga scala: mappale e gestiscile entrambe di continuo.
- Tieni gli **stakeholder coinvolti** e lo stato **trasparente**; fai viaggiare in fretta le cattive notizie.
- Il ROI è il fallimento evitato; vince il processo più leggero che soddisfa i tuoi obblighi. Vedi i capitoli 10.7 (Agile), 10.1 (gestione di portafoglio e programmi), 11.2 (consegna) e 11.3 (teoria delle code).

## Riferimenti e letture di approfondimento

- Project Management Institute, *A Guide to the Project Management Body of Knowledge (PMBOK Guide)*.
- AXELOS, *Managing Successful Projects with PRINCE2*.
- Frederick Brooks, *The Mythical Man-Month* (perché aggiungere persone a un progetto in ritardo lo ritarda ancora).
- Tom DeMarco e Timothy Lister, *Peopleware* e *Waltzing with Bears* (gestione del rischio).
- Steve McConnell, *Software Estimation: Demystifying the Black Art*.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability* (previsione empirica).
- Standish Group, *CHAOS Report* (esiti dei progetti software, da leggere con spirito critico).
- U.S. Digital Service, *Digital Services Playbook*; UK Government, *Government Service Standard* (consegna moderna nel settore pubblico).
- Bent Flyvbjerg e Dan Gardner, *How Big Things Get Done* (consegna dei megaprogetti).
