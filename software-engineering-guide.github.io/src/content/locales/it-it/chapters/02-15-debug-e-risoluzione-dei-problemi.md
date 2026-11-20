# 2.15 Debug e risoluzione dei problemi

## Panoramica e motivazioni

Il debug è il lavoro disciplinato di scoprire perché un sistema fa qualcosa che non dovrebbe, e la risoluzione dei problemi (troubleshooting) è la stessa competenza rivolta a un sistema di produzione in funzione sotto pressione di tempo. Entrambi sono il [metodo scientifico](https://en.wikipedia.org/wiki/Scientific_method) applicato ai difetti: osservi un comportamento sorprendente, formuli un'ipotesi sulla sua causa, progetti un esperimento che la confermerebbe o la smentirebbe e lasci che siano le prove, non l'intuizione, a dirti che cosa cambiare. Fatto così, il debug è una competenza ingegneristica che si può imparare e insegnare. Fatto come folklore, diventa superstizione: cambiare righe a caso, riavviare i server e sperare.

Per un grande team, la differenza è costosa. Un singolo difetto difficile può attirare ingegneri di diversi servizi, consumare ore di reperibilità e bloccare un rilascio. Quando ognuno fa debug per istinto, quello sforzo non si cumula, perché nessuno può riprodurre né spiegare ciò che altri hanno provato. Quando il team condivide un metodo (riprodurre prima, isolare per ricerca, catturare il bug in un test che fallisce, poi correggere), lo stesso sforzo diventa un processo ripetibile e una suite di regressione in crescita. Il debug si collega strettamente alla strategia di test (capitolo 2.4), alla qualità del software (capitolo 2.11) e alle abitudini di costruzione (capitolo 2.9) che rendono diagnosticabile il codice in primo luogo.

Nei contesti aziendali e governativi la posta sale. I difetti aziendali attraversano i confini di servizi e team, quindi chi vede il sintomo raramente è chi possiede la causa. I sistemi governativi aggiungono vincoli che la maggior parte degli ingegneri non incontra mai: ambienti isolati o riservati in cui non puoi collegare un debugger alla produzione, build riproducibili che devono essere diagnosticate dagli artefatti e tracce di audit che devono registrare che cosa hai cambiato e perché. In tutti e tre l'obiettivo è lo stesso: sostituire le congetture con le prove.

## Principi chiave

- **Riproduci prima di teorizzare.** Un bug che non puoi innescare a comando è una voce, non un difetto.
- **Il debug è verifica di ipotesi.** Enuncia ciò che credi, poi progetta l'esperimento più economico che potrebbe provare che ti sbagli.
- **Leggi per primi l'errore e lo stack trace.** Il sistema di solito ti dice dove si è rotto prima che tu cambi una riga.
- **Cerca nello spazio del problema, non scansionarlo.** Dimezza la regione sospetta a ogni passo anziché leggere dall'alto in basso.
- **Riduci al minimo.** Spoglia il caso finché resta solo l'innesco essenziale.
- **Una modifica alla volta.** Le modifiche a pioggia distruggono le prove che ti avrebbero detto quale modifica contava.
- **Cattura il bug in un test che fallisce prima di correggerlo.** La correzione è provata solo quando quel test diventa verde e resta verde.
- **Trova la causa radice, non il sintomo più vicino.** Una toppa che nasconde il sintomo lascia il difetto libero di ritornare.

## Raccomandazioni

### Riproduci il difetto in modo affidabile prima di cambiare qualsiasi cosa

Il tuo primo compito è una riproduzione affidabile: una serie di passi o un caso automatico che inneschi il bug a comando. Senza di essa non puoi distinguere una vera correzione da una coincidenza, perché il sintomo può andare e venire per ragioni che non hai mai controllato. Fissa input, ambiente, versioni e tempi. Se il bug è intermittente, cerca la variabile nascosta che lo fa comparire (un record di dati specifico, un confine di orologio, una richiesta concorrente) finché la riproduzione è affidabile. Una riproduzione affidabile è l'artefatto singolo più prezioso nel debug, perché tutto ciò che viene dopo diventa misurabile.

### Leggi l'errore, i log e lo stack trace prima di toccare il codice

Prima di formulare una sola teoria, leggi ciò che il sistema ti ha già detto. Lo [stack trace](https://en.wikipedia.org/wiki/Stack_trace) (la registrazione della catena di chiamate nel momento del fallimento) di solito nomina il file, la riga e la sequenza che hanno fallito. Il messaggio dell'eccezione, le righe di log intorno e i valori in ambito restringono la ricerca prima che tu abbia cambiato qualcosa. Gli ingegneri sprecano ore a teorizzare su cause che il traceback aveva escluso alla prima riga. Tratta l'output dell'errore come il primo testimone, leggilo con attenzione e per intero e solo poi decidi che cosa indagare.

### Isola con la ricerca binaria nello spazio del problema

Non scansionare il codice dall'alto in basso. Cercalo. Usa la [ricerca binaria](https://en.wikipedia.org/wiki/Binary_search_algorithm): trova un punto in cui lo stato è ancora buono e un punto in cui è già cattivo, poi controlla il punto medio e ripeti, dimezzando ogni volta la regione sospetta. Questo trasforma una ricerca di mille righe in dieci domande. Quando la regressione è comparsa su un intervallo di commit, applica la stessa idea alla storia con la bisezione: `git bisect` percorre l'intervallo di commit e marchi ogni revisione come buona o cattiva finché nomina l'esatta modifica che ha introdotto il difetto. Automatizza il test buono-o-cattivo e la bisezione si esegue da sola.

### Riduci a un esempio riproducibile minimo

Una volta che puoi innescare il bug, riducilo. Un [esempio riproducibile minimo](https://en.wikipedia.org/wiki/Minimal_reproducible_example) è il più piccolo input e percorso di codice che ancora fallisce: togli dati, funzionalità e passi finché ogni ulteriore rimozione fa sparire il bug. La riduzione non è lavoro a vuoto; ogni elemento che elimini è una causa che hai escluso, quindi il caso minimo spesso punta dritto al difetto. Quando l'input è grande o strutturato, automatizza la riduzione con il [delta debugging](https://en.wikipedia.org/wiki/Delta_debugging), un algoritmo che toglie sistematicamente porzioni di un input che fallisce per trovare il sottoinsieme minimo che fallisce. Una riproduzione piccola e autosufficiente è anche la miglior segnalazione di bug possibile da consegnare a un altro team.

### Strumenta con i log, poi usa un debugger interattivo

Adegua lo strumento al bug. Log e strumentazione mirata sono ideali quando devi vedere il comportamento nel tempo, tra processi o in un ambiente che non puoi mettere in pausa. Un debugger interattivo, che ti permette di impostare punti di interruzione, procedere riga per riga e ispezionare lo stato vivo, è ideale quando puoi eseguire il codice in locale e hai bisogno di osservare da vicino una singola esecuzione. Aggiungi la strumentazione come esperimento deliberato legato a un'ipotesi, non come istruzioni di stampa sparse, e rimuovila o promuovila a log strutturato permanente una volta risolto il bug. In produzione, appoggiati al debug guidato dall'osservabilità: eventi ad alta cardinalità e tracciamento distribuito (capitolo 9.2) ti permettono di seguire una richiesta attraverso molti servizi, spesso l'unico modo di fare debug di un sistema distribuito a cui non puoi collegare un debugger.

### Scrivi un test che fallisce e cattura il bug prima di correggerlo

Prima di scrivere la correzione, scrivi un test che fallisce a causa del bug. Questo fa tre cose insieme: prova che hai davvero capito la causa, definisce esattamente che cosa significa "corretto" e diventa una protezione permanente. Poi fai la correzione e guarda il test diventare verde. Quel test ora si unisce alla tua suite come protezione di [test di regressione](https://en.wikipedia.org/wiki/Regression_testing), così che lo stesso difetto non possa ritornare inosservato. Questa pratica lega il debug direttamente alla tua strategia di test (capitolo 2.4): ogni bug difficile che risolvi lascia la suite più forte di come l'ha trovata, e un test instabile riceve lo stesso trattamento (riproduci il non determinismo, poi proteggiti) anziché un'annotazione di ripetizione.

### Trova la causa radice e mantieni l'analisi senza colpevolizzazione

Correggere il sintomo non è correggere il bug. Risali dal fallimento alla sua vera origine, chiedendoti perché a ogni livello finché arrivi a una causa che puoi rimuovere anziché mascherare. Per i difetti arrivati in produzione, conduci un'analisi delle cause radice senza colpevolizzazione come parte della gestione degli incidenti (capitolo 9.3): concentrati sulle condizioni di sistema e di processo che hanno lasciato il bug rilasciarsi e sopravvivere, mai sulla persona che ha scritto la riga. La colpa spinge le informazioni nel sommerso, e il debug funziona di informazioni. Il risultato è sia una correzione sia un cambiamento nel modo in cui la prossima volta quella classe di difetti viene colta prima.

## Compromessi: vantaggi e svantaggi

| Approccio | Vantaggi | Svantaggi |
|---|---|---|
| Log e strumentazione | Funziona in produzione e nei sistemi distribuiti; cattura il comportamento nel tempo | Rumore, costo e proliferazione di log; può alterare i bug di temporizzazione |
| Debugger interattivo | Ispezione precisa dello stato vivo; rapido per i bug locali | Inutile in produzione riservata o isolata; può nascondere bug di concorrenza |
| Disciplina del riprodurre prima | Trasforma le congetture in misura; rende possibile un test che fallisce | Lenta all'inizio; alcuni bug sono davvero difficili da innescare |
| Ricerca binaria e bisezione | Isolamento rapido, anche in codice sconosciuto | Richiede un test buono-o-cattivo affidabile; difficile quando i bug interagiscono |
| Riduzione con delta debugging | Riduce automaticamente input enormi all'innesco | Costo di preparazione; presume che il fallimento sia deterministico |
| Correggere subito il sintomo | Ripristina il servizio in fretta sotto pressione | Lascia la causa radice libera di ritornare; accumula debito |

La tensione centrale è tra velocità e certezza. Durante un incidente in produzione potresti dover prima fermare l'emorragia (un ripristino o una toppa al sintomo) per ripristinare il servizio, ed è legittimo. L'errore è fermarsi lì. Risolvi la tensione separando i due compiti: mitiga in fretta per proteggere gli utenti, poi riproduci, trova la causa radice e aggiungi la protezione di regressione prima di considerare chiuso il difetto. Una correzione del sintomo senza seguito è un bug che hai accettato di reincontrare.

## Domande da discutere con il tuo team

1. **Quando qualcuno incontra un bug difficile, qual è la prima cosa che fa, e si tratta di riprodurre o di tirare a indovinare?** La risposta onesta rivela se il tuo team ha un metodo condiviso o una stanza piena di folklore privato. Chiedi alle persone di raccontare ad alta voce il loro ultimo difetto difficile: hanno ottenuto prima una riproduzione affidabile, o hanno iniziato a cambiare codice e riavviare cose? Un team che riproduce per primo può passare un bug da una persona all'altra, perché la riproduzione viaggia; un team che tira a indovinare no, perché ogni tentativo è irripetibile. Questo conta di più man mano che il team cresce, poiché chi vede un sintomo è sempre meno chi può correggerlo. Se l'impostazione predefinita è tirare a indovinare, concorda il riprodurre per primo come norma e fai di una riproduzione pulita il prezzo d'ingresso a un ticket di bug.

2. **I bug che correggiamo tornano, e ce ne accorgeremmo?** Un difetto che ritorna è un difetto la cui causa radice non è mai stata rimossa e la cui correzione non è mai stata protetta da un test. Estrai l'ultimo trimestre di incidenti e ticket riaperti e conta quanti erano ripetizioni o cugini stretti di bug precedenti. Ogni ripetizione è prova che il team ha rattoppato un sintomo, saltato il test che fallisce o interrotto troppo presto l'analisi delle cause radice. La soluzione è una regola: nessun bug è chiuso finché un test che fallisce sul vecchio comportamento passa sul nuovo ed entra nella suite. Porta un recente bug ricorrente e chiediti quale protezione l'avrebbe colto, perché quella protezione è ciò che ti mancava.

3. **Possiamo fare debug dei nostri sistemi di produzione, dati i modi in cui ci è consentito toccarli?** Negli ambienti aziendali e soprattutto governativi, spesso non puoi collegare un debugger, non puoi riprodurre con dati reali e non puoi cambiare un sistema in esecuzione senza una traccia di audit. Se la tua unica tecnica di debug è un debugger interattivo locale, sei cieco proprio dove vivono i bug più difficili. Chiediti quali evidenze un fallimento in produzione lascia davvero: log strutturati, tracce distribuite (capitolo 9.2), core dump o artefatti di build riproducibili. Decidi ora che cosa devi catturare per impostazione predefinita perché un futuro incidente sia diagnosticabile, perché non puoi aggiungere strumentazione a un fallimento già avvenuto. Nei contesti regolamentati, conferma che la stessa traccia soddisfi anche i tuoi obblighi di audit.

4. **Quando un incidente in produzione ci costringe a fermare in fretta l'emorragia, come ci assicuriamo che la causa radice venga comunque trovata dopo?** Durante un incidente, un ripristino o una toppa al sintomo è la prima mossa giusta per proteggere gli utenti, ma il pericolo è che il ticket si chiuda nel momento in cui il servizio ritorna e il difetto di fondo non venga mai diagnosticato. Per un grande team è qui che il debito si accumula in modo invisibile, perché la stessa classe di fallimenti riemerge su un servizio diverso e con un ingegnere reperibile diverso mesi dopo. Porta i tuoi ultimi incidenti di gravità uno e controlla ciascuno: a seguito della mitigazione sono arrivati una riproduzione, un'analisi delle cause radice e una protezione di regressione, o la storia è finita a "servizio ripristinato"? Concorda una regola esplicita per cui un incidente mitigato resta aperto finché la causa radice non è capita e protetta e indica chi è responsabile di quel seguito. Nei contesti aziendali e governativi, collega questo al tuo processo di gestione degli incidenti (capitolo 9.3) così che la revisione post-incidente sia un passaggio richiesto e verificabile anziché una cortesia che salta quando parte il prossimo incendio.

5. **Quanto di un fallimento riusciamo davvero a ricostruire a posteriori, e chi ha deciso che cosa catturiamo per impostazione predefinita?** Non puoi collegare strumentazione a un fallimento già avvenuto, quindi la diagnosticabilità di qualsiasi incidente è fissata in anticipo dai log, dalle tracce, dalle metriche e dai dump che hai scelto di emettere. La considerazione contraria è costo e rumore: gli eventi ad alta cardinalità e il tracciamento completo non sono gratis, e un eccesso di log seppellisce il segnale gonfiando l'archiviazione e, nei contesti regolamentati, la tua esposizione sulla conservazione dei dati. Porta un incidente recente reale e chiediti che evidenze ha lasciato, poi risali a ciò che avresti voluto catturare e a quanto costerebbe conservarlo. Decidi con deliberazione quali segnali sono attivi per impostazione predefinita rispetto a campionati o su richiesta e registra quella decisione, così che sia una politica, non un incidente. Per un sistema aziendale o governativo, aggiungi chi è responsabile di quel bilancio di osservabilità e se la traccia catturata soddisfi anche gli obblighi di audit, privacy e residenza dei dati.

6. **Trattiamo il debug come una competenza insegnata e misurabile, o i nuovi ingegneri la assorbono per osmosi?** Il debug si può imparare, eppure la maggior parte dei team non lo insegna mai esplicitamente, così che gli junior ereditano il folklore che sta loro più vicino, e il metodo del riprodurre per primo si diffonde in modo disomogeneo o per niente. La tensione è che un insegnamento deliberato (programmazione in coppia sui bug difficili, resoconti dei risultati post-incidente, monitoraggio di metriche) costa tempo senior che sembra sempre necessario altrove. Porta due numeri alla discussione: il tuo tasso di difetti ripetuti e il tuo tempo di diagnosi, perché se non riesci a misurarli non puoi dire se il tuo metodo sta migliorando o decadendo. Valuta se l'inserimento comprenda un vero esercizio di debug e se i risultati delle cause radice alimentino davvero un rilevamento più precoce. In un'organizzazione grande o pubblica, una pratica di debug documentata e misurata diventa anche evidenza di rigore ingegneristico che auditor, regolatori e organi di vigilanza si aspettano sempre più di vedere.

## Lente settoriale

**Startup.** Con una manciata di ingegneri e nessun margine, il tuo obiettivo è rendere i bug economici da riprodurre e impossibili da dimenticare, non costruire processi pesanti. Appoggiati a `git bisect`, a una riproduzione locale rapida e a un test che fallisce per ogni bug corretto, perché quell'abitudine costa minuti e ti impedisce di ripagare lo stesso difetto mentre cerchi di rilasciare. Salta i postmortem formali, ma non saltare mai il test di regressione: è l'unico artefatto abbastanza piccolo da potertelo sempre permettere e abbastanza prezioso da tenere sempre.

**Piccola impresa.** Probabilmente non hai uno specialista dedicato di affidabilità o osservabilità e hai un budget ridotto per gli strumenti, quindi privilegia ciò che il tuo stack già ti dà: stack trace leggibili, log strutturati e il tracciamento integrato nei framework e nei servizi ospitati che hai acquistato. Quando valuti una nuova piattaforma, pesa quanto diagnosticabili rende i fallimenti, perché uno strumento economico che nasconde che cosa è andato storto ti costa molto più in tempo di congetture di quanto la licenza abbia risparmiato. Riprodurre per primo e una modifica alla volta sono discipline gratuite che rendono più in fretta quando nessuno ha ore da sprecare.

**Grande impresa.** I tuoi bug difficili attraversano i confini di servizi e team, quindi chi vede il sintomo raramente ne possiede la causa, e un metodo condiviso conta più delle capacità di qualsiasi individuo. Standardizza il riprodurre per primo, l'isolamento per ricerca binaria, un test che fallisce prima della correzione e postmortem senza colpevolizzazione tra i team e investi nel tracciamento distribuito (capitolo 9.2) così che una richiesta possa essere seguita attraverso i servizi. Gestisci il debug come una capacità misurata: segui il tasso di difetti ripetuti e il tempo di diagnosi e riporta i risultati delle cause radice nel rilevamento più precoce così che la stessa classe di fallimenti non faccia il giro della tua mappa dei servizi.

**Ente pubblico.** Regole sugli appalti, ambienti riservati e responsabilità pubblica plasmano come ti è consentito fare debug. Spesso non puoi collegare un debugger alla produzione né copiare dati dei cittadini su un portatile, quindi progetta per la diagnosi a partire da ciò che è consentito: build riproducibili, record sintetici in un'enclave isolata e log e tracce strutturati catturati per impostazione predefinita. Registra nella traccia di audit ogni passo diagnostico e ogni modifica e richiedi che i fornitori espongano abbastanza telemetria e riproducibilità della build da permetterti di indagare i fallimenti in modo indipendente anziché dipendere dalla parola del fornitore.

## Esempi

**Startup.** Un team di quattro ingegneri vede continuamente fallire il pagamento per una frazione degli utenti, ma mai nei test. Anziché tirare a indovinare, un ingegnere ottiene una riproduzione affidabile ripetendo l'esatto payload della richiesta che fallisce, poi legge lo stack trace che aveva ignorato, che punta a una chiamata di interpretazione delle date. Un rapido `git bisect` sui commit della settimana indica la modifica che ha cambiato una libreria di date. Scrivono un test che fallisce con il timestamp incriminato, correggono l'interprete, guardano il test diventare verde e lo tengono nella suite. L'intera indagine richiede un pomeriggio perché hanno riprodotto prima di teorizzare, e il bug non ritorna.

**Grande impresa.** Una piattaforma di pagamenti vede timeout intermittenti che nessun singolo team sa spiegare, perché il sintomo compare nel pagamento ma la causa vive tre servizi più in là. Gli ingegneri reperibili usano il tracciamento distribuito (capitolo 9.2) per seguire una singola richiesta fallita attraverso i confini dei servizi e trovano una chiamata a valle che occasionalmente va in deadlock sotto carico concorrente, una classica [race condition](https://en.wikipedia.org/wiki/Race_condition) in cui il risultato dipende da una sfortunata temporizzazione tra thread. La riproducono con un test di carico, la catturano in un test di integrazione che fallisce, correggono il locking e conducono un postmortem senza colpevolizzazione (capitolo 9.3) che aggiunge un intervallo di tracciamento e un allarme così che la prossima volta venga colto in minuti, non giorni.

**Ente pubblico.** Un'agenzia di prestazioni gestisce il proprio sistema di pratiche in un ambiente isolato in cui gli ingegneri non possono collegare un debugger alla produzione né copiare dati dei cittadini sui portatili. Un difetto di calcolo emerge nella riconciliazione. Il team fa debug con ciò che l'ambiente consente: log strutturati, una build riproducibile che possono avviare in un'enclave di test isolata e record sintetici che ricreano il caso che fallisce. Ogni passo diagnostico è registrato nella traccia di audit, la correzione viene rilasciata con un test che prima fallisce e poi passa come evidenza e l'analisi delle cause radice alimenta un nuovo controllo prima del rilascio. Poiché la riproduzione ha usato dati sintetici, nessun record di cittadini ha mai lasciato il confine.

## Business case: motivazioni, ROI e TCO

Il ritorno di un debug disciplinato si misura in ore di ingegneri non spese a tirare a indovinare e in difetti che non ritornano. Un bug intermittente non diagnosticato può consumare giorni di tempo senior e ripetute escalation di reperibilità; un metodo basato sul riprodurre per primo lo trasforma in un compito delimitato e delegabile, e l'abitudine del test che fallisce impedisce allo stesso difetto di addebitarti di nuovo il trimestre successivo. In una grande organizzazione, l'effetto cumulativo del non ripagare mai lo stesso bug è sostanziale e migliora direttamente il tasso di fallimento delle modifiche e il tempo medio di ripristino che la leadership già segue.

Il costo totale di proprietà è soprattutto formazione e strumenti, ed è modesto. Servono convenzioni condivise (riprodurre per primo, una modifica alla volta, un test che fallisce prima della correzione), debugger e tracciamento già comuni nella catena di strumenti e l'investimento in osservabilità descritto nel capitolo 9.2. Il costo più grande e nascosto è l'alternativa: una cultura della superstizione in cui gli ingegneri applicano modifiche a pioggia, i sintomi vengono rattoppati e ritornano e il carico di reperibilità cresce senza limite. Ridurre il lavoro ripetitivo della reperibilità da solo spesso giustifica l'investimento, e il caso da presentare alla leadership si dice più semplicemente così: meno incidenti ripetuti e ripristino più rapido per un costo una tantum in abitudini e strumentazione.

## Antipattern e insidie

- **Debug a pioggia:** cambiare molte cose insieme, così che anche una correzione non ti insegna nulla sulla causa.
- **Correggere senza riprodurre:** dichiarare vittoria su un bug che non sei mai riuscito a innescare a comando.
- **Ignorare l'output dell'errore:** teorizzare su cause che lo stack trace aveva già escluso.
- **Toppe al sintomo:** mettere a tacere il sintomo mentre la causa radice sopravvive per ritornare.
- **Proliferazione di istruzioni di stampa:** output di debug sparso lasciato nel codice, che aggiunge rumore anziché un esperimento legato a un'ipotesi.
- **Saltare il test di regressione:** correggere il bug ma non lasciare alcuna protezione, così che possa tornare in silenzio.
- **Ripetere i test instabili:** nascondere il non determinismo con ripetizioni anziché fare debug della race condition sottostante o dell'[heisenbug](https://en.wikipedia.org/wiki/Heisenbug), un bug che cambia o svanisce nel momento in cui provi a osservarlo.
- **Postmortem guidati dalla colpa:** punire l'autore, il che spinge nel sommerso le informazioni da cui il debug dipende.

## Modello di maturità

- **Livello 1, Avvio:** il debug è folklore individuale e reazione. Gli ingegneri tirano a indovinare, applicano modifiche a pioggia e riavviano le cose. I bug sono corretti al sintomo, le riproduzioni sono rare e gli stessi difetti ritornano. La produzione è appena diagnosticabile e nessuno può passare un bug a qualcun altro perché nessun tentativo è ripetibile.
- **Livello 2, Sviluppo:** alcuni ingegneri riproducono in modo affidabile, leggono gli stack trace e usano i debugger, ma la pratica è incoerente e varia da persona a persona e da team a team. I log esistono ma sono rumorosi e non strutturati. Le correzioni a volte sono accompagnate da un test che fallisce, spesso no, e l'analisi delle cause radice avviene solo quando qualcuno insiste.
- **Livello 3, Standardizzazione:** riprodurre per primo, isolamento per ricerca binaria, una modifica alla volta e un test che fallisce prima della correzione sono norme di team documentate e fatte rispettare nell'organizzazione. Bisezione e riduzione con delta debugging sono pratica comune. La produzione ha log strutturati e tracciamento (capitolo 9.2) e i postmortem senza colpevolizzazione (capitolo 9.3) sono la risposta standard per ogni difetto sfuggito.
- **Livello 4, Gestione:** la pratica di debug è misurata e controllata rispetto a valori di riferimento. Tasso di difetti ripetuti, tempo di diagnosi, numero di ticket riaperti e quota di correzioni rilasciate con un test di regressione sono seguiti per team e rivisti con una cadenza. Il completamento di riproduzione e causa radice è trattato come un cancello anziché una buona intenzione, e gli andamenti rispetto al riferimento guidano dove investire in strumenti, formazione e osservabilità.
- **Livello 5, Orchestrazione:** il debug è una competenza insegnata e integrata con qualità (capitolo 2.11) e gestione degli incidenti (capitolo 9.3), e l'intero ciclo si adatta di continuo. L'osservabilità è progettata dentro così che la maggior parte dei bug in produzione sia diagnosticabile senza debugger, ogni bug risolto rafforza la suite di regressione e i risultati delle cause radice alimentano un rilevamento più precoce così che le classi di difetti siano prevenute anziché diagnosticate di nuovo. L'organizzazione riequilibra lo sforzo man mano che sistemi e modi di fallimento evolvono, e il tasso di difetti ripetuti continua a scendere.

## Spunti di discussione

1. Quale frazione dei vostri bug recenti è stata riprodotta in modo affidabile prima che qualcuno cambiasse codice, e che cosa dice quella frazione del vostro metodo?
2. Quando compare una regressione, il vostro team ricorre alla bisezione, o legge il codice a mano finché qualcuno lo individua?
3. Quanto è diagnosticabile oggi il vostro sistema di produzione, e che cosa dareste per aver catturato di un fallimento già avvenuto?
4. Le vostre correzioni sono costantemente accompagnate da un test che prima fallisce e poi passa, e se no, dove si rompe quella disciplina?
5. Come gestite i test instabili: fate debug del non determinismo, o lo coprite con ripetizioni?
6. Il debug viene insegnato deliberatamente ai nuovi ingegneri, o li lasciate ad assorbire il folklore per osmosi?

## Punti chiave

- Il debug è verifica di ipotesi: riproduci in modo affidabile, leggi l'errore e lo stack trace, poi isola con ricerca binaria e bisezione anziché scansionare.
- Riduci il fallimento a un esempio riproducibile minimo, usando il delta debugging per input grandi, perché ogni elemento rimosso è una causa esclusa.
- Adegua lo strumento al bug: strumentazione e tracciamento per produzione e sistemi distribuiti (capitolo 9.2), debugger interattivi per l'indagine locale.
- Scrivi un test che fallisce e cattura il bug prima di correggerlo, così che la correzione sia provata e il difetto sia protetto per sempre (capitolo 2.4).
- Trova e rimuovi la causa radice, conduci postmortem senza colpevolizzazione (capitolo 9.3) e tratta il debug come una competenza che si impara, non come folklore.
- Cambia una cosa alla volta; modifiche a pioggia e toppe al sintomo distruggono le prove e invitano il bug a ritornare.

## Riferimenti e letture di approfondimento

- David J. Agans, *Debugging: The 9 Indispensable Rules for Finding Even the Most Elusive Software and Hardware Problems*
- Andreas Zeller, *Why Programs Fail: A Guide to Systematic Debugging*
- Andreas Zeller e Ralf Hildebrandt, "Simplifying and Isolating Failure-Inducing Input" (l'algoritmo di delta debugging)
- Brian W. Kernighan e Rob Pike, *The Practice of Programming* (capitolo sul debug)
- Andrew Hunt e David Thomas, *The Pragmatic Programmer* (i capitoli su debug e asserzioni)
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction* (il capitolo sul debug)
- John Regehr, "Reducers Are Fuzzers" e scritti correlati sulla riduzione dei casi di test
- Charity Majors, Liz Fong-Jones e George Miranda, *Observability Engineering* (debug della produzione con telemetria ad alta cardinalità e tracciamento)
- Betsy Beyer, Chris Jones, Jennifer Petoff e Niall Richard Murphy, a cura di, *Site Reliability Engineering* (postmortem senza colpevolizzazione e debug della produzione)
