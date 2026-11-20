# 11.1 La pipeline di scoperta

## Panoramica e motivazioni

La pipeline di scoperta è il flusso di lavoro che decide **che cosa costruire e perché** e definisce **che aspetto avrà il successo**, prima e accanto alla consegna. Dove la pipeline di consegna (capitolo 11.2) trasforma le idee convalidate in software funzionante, la pipeline di scoperta trasforma problemi, evidenza e strategia in un insieme ordinato per priorità e verificabile di esiti voluti. Nella pratica moderna le due girano di continuo e in parallelo, spesso chiamate sviluppo *a doppio binario*, anziché come fasi sequenziali. La scoperta continua ad alimentare la consegna con una scorta pronta di lavoro ben inquadrato e a rischio ridotto e la consegna continua a riportare nella scoperta i dati sugli esiti del mondo reale.

Per i grandi team, una pipeline di scoperta debole è la modalità di fallimento più costosa del software. Un team con un'ottima consegna e una scarsa scoperta costruisce la cosa sbagliata in modo efficiente: rilascia in fretta, raggiunge gli obiettivi di velocità e non muove comunque nessuna metrica di business. Il costo è invisibile sulle dashboard ingegneristiche ed enorme sul bilancio. La pipeline di scoperta è come rendi visibile quel costo: costringe gli obiettivi a essere espliciti, misurabili e falsificabili prima che tu impegni grandi investimenti.

I contesti aziendali e governativi alzano la posta. Le imprese coordinano decine di team rispetto a una strategia condivisa, quindi obiettivi locali disallineati si compongono in portafogli sprecati. I programmi governativi impegnano finanziamenti pubblici pluriennali rispetto a mandati legislativi, dove "abbiamo costruito ciò che diceva il contratto" non è una difesa se l'esito (cittadini serviti, tempi di attesa ridotti, frodi prevenute) non si materializza mai. Una pipeline di scoperta disciplinata, espressa attraverso obiettivi, misure e requisiti di qualità espliciti, è come entrambi mantengono verificabile il proprio intento.

## Principi chiave

- **Esiti anziché produzioni.** Misura il cambiamento che crei per utenti e business, non le funzionalità che rilasci.
- **Rendi l'intento esplicito e misurabile.** Un obiettivo che non puoi misurare è un'opinione che non puoi gestire.
- **Riduci il rischio prima di costruire.** L'esperimento più economico batte l'opinione più sicura.
- **Scoperta e consegna girano di continuo in parallelo**, non come cancelli sequenziali.
- **Gli attributi di qualità sono requisiti, non ripensamenti.** Affidabilità, sicurezza e accessibilità si scoprono e si specificano, non si sperano.
- **L'allineamento batte l'ottimizzazione locale.** Obiettivi annidati collegano il lavoro dei team alla strategia.
- **Chiudi il ciclo.** Gli esiti consegnati sono evidenza che rientra nella scoperta.

## Raccomandazioni

### Inquadra la direzione con gli OKR

Usa gli **[obiettivi e risultati chiave](https://en.wikipedia.org/wiki/OKR) (OKR)** per collegare la strategia all'esecuzione dei team. Un *Obiettivo* è un'enunciazione qualitativa e ispiratrice di uno stato finale desiderato ("Rendere senza sforzo l'onboarding della prima volta"). I *Risultati chiave* sono il piccolo numero (tipicamente 2–4) di esiti misurabili che provano che l'obiettivo viene raggiunto ("Aumentare l'attivazione a 7 giorni dal 40% al 60%"; "Ridurre del 30% i ticket di supporto sull'onboarding"). I risultati chiave esprimono **esiti**, non compiti: "rilasciare il nuovo wizard" è un compito che si finge risultato.

Fai scendere gli OKR per *allineamento*, non per dettatura: la leadership fissa un piccolo numero di obiettivi aziendali; i team propongono risultati chiave e propri obiettivi che salgono verso di essi. Fissali con una cadenza regolare (comunemente trimestrale con una cornice annuale), rivedili a metà ciclo e valutali onestamente alla fine. Tienili separati dalle valutazioni delle prestazioni: gli OKR valutati per la retribuzione diventano presto sottodimensionati. Vedi il capitolo 10.1 per come gli OKR si collegano alla gestione di portafoglio e programmi.

### Monitora la salute con i KPI

Distingui gli **[indicatori chiave di prestazione](https://en.wikipedia.org/wiki/Performance_indicator) (KPI)** dagli OKR. Gli OKR descrivono il *cambiamento* che vuoi in questo periodo; i KPI descrivono la *salute continua* che devi sostenere a prescindere da ciò che stai cambiando (disponibilità, tasso di conversione, costo per transazione, soddisfazione del cliente). Una metrica può essere entrambe le cose (un KPI che stai cercando attivamente di muovere diventa un risultato chiave), ma la maggior parte dei KPI sono guardrail che monitori, non obiettivi verso cui scattare.

Classifica ogni metrica importante come **anticipatrice** (predittiva e azionabile ora, come le iscrizioni di prova) o **ritardata** (confermativa e lenta, come i ricavi annuali). La scoperta si affida agli indicatori anticipatori per orientarsi prima che quelli ritardati confermino. Diffida delle metriche di vanità che salgono in modo affidabile ma non predicono nulla (visualizzazioni di pagina grezze, utenti registrati totali); preferisci metriche di rapporto e di coorte che resistono alla manipolazione. Vedi i capitoli 7.3 e 7.4 per il macchinario di analisi e sperimentazione dietro queste misure.

### Specifica esplicitamente gli attributi di qualità del sistema

I requisiti funzionali dicono che cosa fa il sistema. Gli **attributi di qualità del sistema** (le "-ilità": affidabilità, prestazioni, scalabilità, sicurezza, accessibilità, manutenibilità, operabilità) dicono quanto bene deve farlo. Sono abitualmente poco scoperti: tutti li presumono, nessuno li specifica e emergono come incidenti in produzione. Trattali come output di scoperta di prim'ordine. Identifica i **requisiti architetturalmente significativi** (le esigenze di qualità che plasmano materialmente l'architettura) per ogni iniziativa. Quantificali ("latenza p99 sotto 200 ms a 10× il carico attuale"; "WCAG (Web Content Accessibility Guidelines) 2.2 AA"; "obiettivo di tempo di ripristino di 15 minuti"). E dove puoi, codificali come **funzioni di idoneità** automatiche (controlli eseguibili che verificano di continuo un attributo di qualità) che la pipeline di consegna può verificare. È il complemento, sul lato della scoperta, del capitolo 3.1 (fondamenti dell'architettura) e del capitolo 3.5 (scalabilità, prestazioni, resilienza).

### Rendi SMART ogni obiettivo

Che tu stia scrivendo un risultato chiave, un criterio di accettazione o un obiettivo di qualità, applica il test **[SMART](https://en.wikipedia.org/wiki/SMART_criteria)**:

- **Specifico:** nomina un esito chiaro e non ambiguo.
- **Misurabile:** ha una metrica e una fonte di verità.
- **Raggiungibile:** è realistico dati vincoli ed evidenza.
- **Rilevante:** sale verso un obiettivo superiore e verso il valore per l'utente.
- **Temporizzato:** ha una scadenza o una data di revisione.

"Migliorare le prestazioni" fallisce ogni lettera. "Ridurre il tempo mediano di checkout da 8 s a 3 s per gli utenti mobile entro la fine del Q3, misurato con monitoraggio degli utenti reali" le supera tutte e cinque. I criteri SMART convertono l'ambizione vaga in un'affermazione falsificabile che la scoperta può testare e la consegna può verificare.

### Conduci una scoperta continua guidata dall'evidenza

Struttura la scoperta come una pipeline ripetibile, non una fase una tantum:

1. **Percepisci.** Raccogli segnali: ricerca sugli utenti, dati di supporto, analisi, input di mercato e di conformità.
2. **Inquadra.** Mappa le opportunità (un *albero opportunità-soluzione* collega un esito desiderato ai bisogni degli utenti e alle soluzioni candidate che potrebbero muoverlo).
3. **Ipotizza.** Enuncia le assunzioni come affermazioni falsificabili: "Crediamo che [modifica] causerà [esito] per [segmento] e sapremo se [misura] si muove."
4. **Sperimenta.** Convalida le assunzioni più rischiose con il test più economico: interviste, prototipi, test a porta finta (pubblicizzare una funzionalità non ancora costruita per misurare la domanda reale), [esperimenti A/B](https://en.wikipedia.org/wiki/A/B_testing) (confronti randomizzati di due varianti, capitolo 7.4).
5. **Decidi.** Persevera, cambia rotta o abbandona e porta i sopravvissuti nell'arretrato di consegna con i loro criteri di successo SMART allegati.

L'output della pipeline di scoperta non è un elenco di funzionalità; è un flusso di *scommesse convalidate e misurabili* pronte per la consegna.

## Compromessi: vantaggi e svantaggi

| Approccio | Vantaggi | Svantaggi |
|---|---|---|
| **Obiettivi basati sugli esiti (OKR)** | Allinea i team all'impatto; dà autonomia sul *come* | Difficili da scrivere bene; si è tentati di riempirli di compiti; attribuzione rumorosa |
| **Roadmap di produzioni/funzionalità** | Prevedibili, facili da comunicare e contrattualizzare | Premiano il rilascio sull'impatto; nascondono il rischio della cosa sbagliata |
| **Scoperta pesante in anticipo** | Riduce lo spreco di costruzione; requisiti solidi | Rallenta l'avvio; rischia la paralisi da analisi; assunzioni ancora non testate |
| **Scoperta continua a doppio binario** | Riduce il rischio di continuo; riscontro rapido | Richiede capacità di ricerca e disciplina; più difficile da pianificare |
| **Attributi di qualità espliciti come obiettivi SMART** | Previene sorprese sulle "-ilità"; verificabile | Sforzo per quantificare; può vincolare troppo l'esplorazione iniziale |

La tensione centrale è **impegno contro apprendimento**. Le imprese, e specialmente i governi, hanno spesso bisogno di impegni fermi per bilanci e contratti, il che spinge verso roadmap di produzioni. I buoni esiti hanno bisogno di spazio per imparare, il che spinge verso OKR ed esperimenti. Risolvilo così: impegnati con fermezza su *problemi ed esiti* e tieni le *soluzioni* in modo morbido.

## Domande da discutere con il tuo team

1. **Chi nel vostro team possiede davvero la scoperta e ha la capacità di condurla di continuo anziché in uno sprint una tantum?** Lo sviluppo a doppio binario funziona solo quando qualcuno tiene aperto il binario della scoperta ogni settimana anziché solo all'inizio di un trimestre. In una grande organizzazione la scoperta spesso non ha un responsabile dedicato, quindi collassa su chi ha tempo libero, cioè nessuno, e il team ripiega sul costruire. Portate evidenza: contate quante delle vostre ultime dieci funzionalità sono passate da un'ipotesi documentata e da un test economico prima della costruzione, rispetto a quante sono andate direttamente nell'arretrato. Nei contesti aziendali e governativi, dove una singola iniziativa disallineata può sprecare più team-trimestri, nominate un responsabile di prodotto o un trio (prodotto, design, ingegneria) responsabile del ciclo percepisci-inquadra-ipotizza-sperimenta-decidi. Se nessuno lo possiede, dotatelo di personale prima di discutere di qualsiasi altra cosa.

2. **Quali delle vostre iniziative attuali hanno requisiti architetturalmente significativi che non avete mai quantificato e potreste codificarne qualcuno come funzione di idoneità?** Le "-ilità" (affidabilità, prestazioni, sicurezza, accessibilità) vengono presunte e poi emergono come incidenti in produzione. Passate in rassegna ogni iniziativa attiva, chiedetevi quali attributi di qualità plasmano materialmente l'architettura e controllate se ciascuno ha un numero e una fonte di verità: "p99 sotto 200 ms a 10x il carico", "WCAG 2.2 AA", "obiettivo di tempo di ripristino di 15 minuti". Per impresa e governo, requisiti di accessibilità o sicurezza non quantificati creano esposizione legale e di audit diretta. Il segnale da portare sono i vostri ultimi tre incidenti: quanti risalivano a un attributo di qualità che nessuno aveva specificato? Dove potete trasformare un obiettivo in una funzione di idoneità automatica che la pipeline di consegna verifica, fatelo, perché un obiettivo specificato ma non fatto rispettare deriva.

3. **Quando vi siete impegnati per ultimo su una soluzione, avete testato per prima l'assunzione più rischiosa o la più facile?** I team convalidano in modo affidabile l'assunzione con cui si sentono più a loro agio e saltano quella che ucciderebbe davvero l'idea. Per ogni iniziativa, elencate le sue assunzioni (desiderabilità, vitalità, fattibilità) e ordinatele per "quanto è morta questa idea se qui sbagliamo", poi puntate il test più economico in cima a quell'elenco. Conta su larga scala perché un team sicuro e senior può impegnare un trimestre di ingegneria su una convinzione non testata e il costo resta invisibile fino al lancio. Portate l'artefatto: la vostra ultima ipotesi enunciata come "Crediamo che [modifica] causi [esito] per [segmento], misurato da [metrica]" e chiedetevi se l'avete testata o semplicemente costruita. Se non sapete nominare l'assunzione più rischiosa, non siete pronti a impegnare capacità di costruzione.

4. **Quanti dei vostri risultati chiave sono genuini esiti e quanti sono compiti o date di rilascio vestiti da esiti?** Il fallimento più comune nella pianificazione basata sugli esiti è riempire i risultati chiave con il lavoro che già pianificavate di fare ("lanciare il nuovo wizard") anziché con il cambiamento che quel lavoro dovrebbe causare ("alzare l'attivazione a 7 giorni dal 40% al 60%"). Su larga scala questo vanifica in silenzio l'intero scopo: decine di team riportano verde mentre nessuna metrica di business si muove, perché tutti si sono valutati sul rilasciare. La spinta contraria è reale, le roadmap di produzioni sono più facili da comunicare, contrattualizzare e prevedere, ed è esattamente per questo che si riaffacciano. Portate il vostro attuale insieme di OKR e segnate ogni risultato chiave come esito o produzione, poi controllate se la valutazione degli OKR è intrecciata con la retribuzione, poiché i risultati legati alla paga vengono presto sottodimensionati. Per i portafogli aziendali e governativi, dove il finanziamento è impegnato rispetto a obiettivi dichiarati, una roadmap di produzioni senza misura di esito è un rilievo di audit in attesa di accadere; insistete che ogni iniziativa si impegni con fermezza su un problema e un esito misurabile tenendo la soluzione in modo morbido.

5. **Quali dei vostri KPI continuerebbero a salire anche se il prodotto stesse peggiorando e quali guardrail proteggono le metriche che state attivamente cercando di muovere?** Ogni metrica che elevate a obiettivo invita la [legge di Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law): una volta che una misura diventa l'obiettivo, le persone ottimizzano la misura anziché la cosa che doveva rappresentare. Le metriche di vanità (visualizzazioni di pagina grezze, utenti registrati cumulativi) salgono in modo affidabile e non predicono nulla, mentre un singolo risultato chiave inseguito senza guardrail può essere raggiunto degradando qualcosa che non avete mai nominato. La tensione è che gli indicatori anticipatori vi permettono di orientarvi presto ma sono rumorosi e manipolabili, mentre quelli ritardati sono affidabili ma confermano troppo tardi per agire. Portate il vostro inventario di metriche classificato come anticipatorio o ritardato e come obiettivo o guardrail e mettete alla prova ogni obiettivo chiedendovi "come potrebbe un team astuto raggiungere questo numero peggiorando il prodotto". Nei contesti regolati e pubblici, pubblicate i guardrail accanto agli obiettivi, perché un organo di controllo che vede solo la metrica di testa non sa distinguere il genuino valore pubblico da un numero manipolato.

6. **Quando la consegna rilascia qualcosa, come rientra davvero nella scoperta l'esito del mondo reale, o il ciclo resta aperto?** Lo sviluppo a doppio binario si compone solo se gli esiti consegnati rifluiscono come evidenza per il giro successivo; quando il ciclo resta aperto, i team rilasciano, festeggiano e non imparano mai se la scommessa ha pagato, così le stesse assunzioni non testate si ripetono. In una grande organizzazione il percorso di riscontro è dove la responsabilità più probabilmente cade in una fessura: la consegna possiede il rilascio, l'analisi possiede la dashboard e nessuno possiede il confronto tra risultato chiave promesso e osservato. Portate le vostre ultime dieci iniziative rilasciate e chiedetevi, per ciascuna, se qualcuno ha controllato la metrica di esito rispetto all'obiettivo SMART originale e se quel controllo ha cambiato una decisione successiva. Per i programmi aziendali e governativi che impegnano finanziamenti pluriennali, nominate la cadenza e il responsabile per ritirare o ridefinire le funzionalità che non hanno mosso la loro metrica, perché una funzionalità rilasciata che nessuno rivede diventa costo permanente senza revisione responsabile.

## Lente settoriale

**Startup.** Con un team minuscolo e poca autonomia, la tua pipeline di scoperta è deliberatamente leggera ma mai saltata: un giorno di interviste ai clienti e un test a porta finta costano quasi nulla rispetto alle settimane che una costruzione sbagliata brucia. Scegli un indicatore anticipatore che rappresenti il tuo valore centrale, enuncia ogni scommessa come una singola ipotesi falsificabile e uccidi le idee prima di scrivere codice anziché dopo. Gli OKR formali sono eccessivi con cinque persone; un esito onesto e misurabile per ciclo basta a impedire che la velocità diventi movimento senza progresso.

**Piccola impresa.** Probabilmente non hai un ricercatore o un analista di prodotto dedicato, quindi tratta la scoperta come un'abitudine, non un ruolo: poche conversazioni strutturate con veri clienti e una semplice metrica che già raccogli. La questione tra costruire e comprare domina, perché la maggior parte degli attributi di qualità (affidabilità, sicurezza, accessibilità) costa meno ottenerla da un fornitore rispettabile che specificarla e farla rispettare da soli. Scrivi uno o due obiettivi SMART così da poter dire se uno strumento acquistato o una piccola costruzione ha davvero mosso l'esito ed evita di impegnare un bilancio scarso su funzionalità che nessuno ha convalidato come volute.

**Grande impresa.** La scala trasforma la scoperta in un problema di coordinamento tra decine di team: senza una cadenza OKR condivisa e una definizione comune di "esito", gli obiettivi locali derivano e si duplicano e scommesse disallineate si compongono in portafogli sprecati. Standardizza come i requisiti architetturalmente significativi sono quantificati e codificali come funzioni di idoneità così che gli attributi di qualità siano governati, non presunti. Gestisci la scoperta come portafoglio con espliciti criteri di chiusura e un ciclo che riporta le metriche di esito consegnate al ciclo successivo, così che la leadership si orienti sull'impatto anziché su un arretrato di funzionalità.

**Ente pubblico.** Appalti e finanziamenti pluriennali richiedono impegni fermi, che spingono con forza verso contratti di produzioni, eppure il valore pubblico vive negli esiti: cittadini serviti, tempi di attesa tagliati, onere ridotto. Inquadra i programmi attorno a esiti pubblici misurabili e attributi di qualità non negoziabili (accessibilità WCAG, linguaggio semplice, sicurezza) e rendi l'evidenza di scoperta, compresi i test di usabilità con utenti di tecnologie assistive, parte del registro che gli organi di controllo possono verificare. Definisci il successo come esiti per i contribuenti o i cittadini anziché moduli consegnati, così che "abbiamo costruito ciò che diceva il contratto" non possa mai sostituire un risultato che non si è mai materializzato.

## Esempi

**Startup.** Un team seed di quattro persone che costruisce un'app di pianificazione per saloni di parrucchieri è tentato di costruire un widget di prenotazione online perché alcuni utenti rumorosi lo hanno chiesto. Conduce invece una settimana di scoperta: cinque interviste ai titolari, un pulsante a porta finta "Prenota online" sul sito di marketing e un singolo indicatore anticipatore (la percentuale di appuntamenti che finisce in un mancato appuntamento). Le interviste e i dati sui clic rivelano che i mancati appuntamenti, non la prenotazione, sono il vero dolore, quindi scrive un solo risultato chiave SMART (ridurre i mancati appuntamenti dal 22% a meno del 10% per i saloni pilota in questo trimestre) e rilascia per prima una piccola funzionalità di caparra e promemoria, uccidendo il widget di prenotazione prima di scriverne una riga.

**Grande impresa.** Il gruppo pagamenti di una banca retail sostituisce una roadmap a conteggio di funzionalità con tre OKR trimestrali, uno dei quali è "Far sembrare istantanei i pagamenti di tutti i giorni", con risultati chiave per il tempo p95 di conferma del bonifico, il tasso di successo al primo tentativo e i contatti di supporto legati ai pagamenti. Gli attributi di qualità del sistema sono specificati in anticipo (disponibilità del 99,99%, conferma sotto il secondo, ambito PCI-DSS (Payment Card Industry Data Security Standard) ridotto al minimo) e collegati alla consegna come funzioni di idoneità. La scoperta conduce interviste settimanali ai clienti e test a porta finta prima di impegnare l'ingegneria. Due funzionalità candidate sono uccise nella scoperta per non aver mosso gli indicatori anticipatori (risparmiando stimati due trimestri di sforzo di costruzione), mentre una correzione di latenza più piccola e poco appariscente muove di più il risultato chiave.

**Ente pubblico.** Un'agenzia fiscale nazionale che modernizza la dichiarazione online fissa un obiettivo di programma "Ridurre l'onere della dichiarazione per i contribuenti ordinari", con risultati chiave SMART: tagliare il tempo mediano di dichiarazione da 45 a 20 minuti, alzare il completamento in self-service riuscito dal 60% all'85% e rispettare WCAG 2.2 AA e gli standard di linguaggio semplice come attributi di qualità non negoziabili. I KPI (disponibilità durante la stagione delle dichiarazioni, volume del call center) sono monitorati come guardrail. La scoperta usa test di usabilità moderati con veri contribuenti, compresi utenti di tecnologie assistive, prima di ogni rilascio. Poiché il successo è definito come esiti per i contribuenti anziché moduli consegnati, il programma può mostrare agli organi di controllo valore pubblico misurabile, non solo spesa.

## Business case: motivazioni, ROI e TCO

Il ritorno di una pipeline di scoperta è dominato dallo **spreco evitato**. L'esperienza del settore, ripresa dai programmi di esperimenti controllati nelle grandi aziende tecnologiche, trova ripetutamente che una larga quota delle funzionalità costruite, spesso citata attorno alla metà o più, non produce alcun miglioramento misurabile o danneggia attivamente la metrica obiettivo. Supponi che anche un quarto della capacità di costruzione di un team vada a idee che la scoperta avrebbe ucciso a basso costo. La pipeline si ripaga allora molte volte: una settimana di ricerca sugli utenti e un test a porta finta costano quasi nulla rispetto a un trimestre di ingegneria, più l'onere di manutenzione continuo di una funzionalità inutilizzata.

L'inquadramento del **[costo totale di proprietà](https://en.wikipedia.org/wiki/Total_cost_of_ownership)** (TCO) conta perché le funzionalità non convalidate non sono gratis dopo il lancio. Ogni funzionalità rilasciata porta costi perpetui: manutenzione, test, superficie di sicurezza, supporto e carico cognitivo (capitolo 10.4). Uccidere una cattiva idea nella scoperta evita non solo il costo di costruzione ma l'intera coda della proprietà. Gli attributi di qualità espliciti seguono la stessa logica: specificare affidabilità e accessibilità come obiettivi SMART in anticipo costa molto meno che adattarli dopo un'interruzione, una violazione o una causa.

Per presentare il caso alla leadership, sposta la conversazione da "quanto stiamo rilasciando" a "quanto stiamo muovendo le metriche che contano" e mostra alcuni esempi concreti di costose funzionalità che non hanno mosso nulla. Il costo di adozione è modesto (capacità di ricerca, una cadenza OKR e la disciplina di scrivere criteri SMART) e il rischio principale del *non* adottare è silenzioso, non contato e composto.

## Antipattern e insidie

- **Roadmap di funzionalità che si fingono strategia:** elenchi di produzioni senza esito né misura dichiarati.
- **Risultati chiave che sono compiti:** "lanciare X" anziché "migliorare Y di Z".
- **Teatro degli OKR:** obiettivi scritti, archiviati e mai rivisti né valutati.
- **OKR sottodimensionati o eroici:** obiettivi fissati per garantire il 100% (nulla imparato) o un'ambizione fantastica senza piano.
- **Attributi di qualità non specificati:** affidabilità, sicurezza e accessibilità presunte anziché quantificate, poi scoperte in produzione.
- **Metriche di vanità:** misure che salgono sempre e non predicono nulla.
- **Scoperta come fase una tantum:** uno "sprint di scoperta" all'inizio, poi nessuna convalida continuata.
- **Costruire la soluzione prima di testare l'assunzione:** saltare l'esperimento più economico perché il team è sicuro.
- **Fissazione sulle metriche e [legge di Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law):** una volta che una misura diventa l'obiettivo, smette di essere una buona misura; bilanciala con KPI di guardrail.

## Modello di maturità

- **Livello 1, Avvio:** Il lavoro è definito come funzionalità su una roadmap e il successo è "l'abbiamo rilasciato". Non ci sono misure di esito né obiettivi di qualità espliciti; la scoperta avviene per caso, se avviene e le decisioni sono guidate dall'opinione più rumorosa.
- **Livello 2, Sviluppo:** Gli OKR e i KPI esistono per alcuni team ma non per altri; gli obiettivi sono dichiarati ma spesso a forma di produzione; gli attributi di qualità sono nominati ma non quantificati. Un team può condurre uno "sprint di scoperta" una tantum, poi smettere di convalidare una volta cominciata la costruzione, quindi la pratica è reale ma incoerente nell'organizzazione.
- **Livello 3, Standardizzazione:** Una cadenza OKR coerente allineata alla strategia, risultati chiave SMART e attributi di qualità specificati e verificabili sono documentati e attesi in tutta l'organizzazione. La scoperta è un'attività riconosciuta e dotata di personale con ipotesi ed esperimenti e i requisiti architetturalmente significativi sono identificati per ogni iniziativa anziché presunti.
- **Livello 4, Gestione:** Il portafoglio è misurato rispetto a valori di riferimento. Indicatori anticipatori e ritardati, tasso di successo della scoperta e l'esito che ogni scommessa rilasciata ha davvero mosso sono seguiti rispetto al suo obiettivo SMART; le ipotesi sono valutate sull'evidenza e i criteri di chiusura sono fatti rispettare; le funzioni di idoneità riportano di continuo la conformità degli attributi di qualità, così che la deriva da un obiettivo specificato di affidabilità, prestazioni o accessibilità sia colta con i dati anziché in un incidente.
- **Livello 5, Orchestrazione:** La scoperta continua a doppio binario è integrata con portafoglio, rischio e bilancio; le scommesse convalidate fluiscono con costanza verso la consegna e le metriche di esito ritornano automaticamente a orientare il giro successivo. Gli indicatori anticipatori orientano l'investimento e l'organizzazione ritira, ridefinisce e riequilibra di routine le iniziative sull'evidenza, adattando la pipeline stessa man mano che si spostano mercato e metriche.

## Spunti di discussione

1. Guardate la vostra roadmap attuale: quante voci dichiarano un esito misurabile rispetto a una semplice funzionalità da rilasciare?
2. Quali dei risultati chiave del vostro team sono in realtà compiti camuffati e come li riscrivereste?
3. Da quali attributi di qualità del sistema dipende il vostro prodotto che non sono mai stati quantificati esplicitamente?
4. Qual è l'esperimento più economico che avrebbe potuto uccidere la vostra ultima funzionalità fallita prima che la costruiste?
5. Come risolvete la tensione tra gli impegni fermi che bilancio e appalti esigono e l'apprendimento che i buoni esiti richiedono?
6. Quali dei vostri KPI continuerebbero a salire anche se il prodotto stesse peggiorando?

## Punti chiave

- La pipeline di scoperta decide il *che cosa* e il *perché* e definisce il successo **prima** che la consegna impegni risorse.
- Usa gli **OKR** per il cambiamento che vuoi, i **KPI** per la salute che sostieni e classifica le metriche come anticipatrici o ritardate.
- Tratta gli **attributi di qualità del sistema** come requisiti espliciti, quantificati e verificabili, non come assunzioni.
- Rendi **SMART** ogni obiettivo, risultato chiave e criterio di accettazione.
- Conduci la scoperta **di continuo e in parallelo** alla consegna; convalida a basso costo le assunzioni più rischiose.
- Il ROI dominante è lo **spreco evitato**: sia il costo di costruzione sia il TCO perpetuo delle funzionalità inutilizzate.
- Chiudi il ciclo: le **metriche di esito** consegnate (capitolo 11.2) sono l'evidenza primaria per il giro successivo di scoperta.

## Riferimenti e letture di approfondimento

- *Measure What Matters*, di John Doerr (sugli OKR).
- *Radical Focus*, di Christina Wodtke (OKR nella pratica).
- *Continuous Discovery Habits*, di Teresa Torres (alberi opportunità-soluzione, scoperta a doppio binario).
- *Inspired* ed *Empowered*, di Marty Cagan (scoperta di prodotto e team orientati agli esiti).
- *Lean Analytics*, di Alistair Croll e Benjamin Yoskovitz (indicatori anticipatori, metriche di vanità).
- *The Lean Startup*, di Eric Ries (costruisci-misura-impara, apprendimento convalidato).
- *Escaping the Build Trap*, di Melissa Perri (esiti anziché produzioni).
- *Outcomes Over Output*, di Joshua Seiden.
- *Software Architecture in Practice*, di Bass, Clements, Kazman (attributi di qualità).
- Doran, G. T., "There's a S.M.A.R.T. way to write management's goals and objectives" (*Management Review*, 1981): origine dei criteri SMART.
