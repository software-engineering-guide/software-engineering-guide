# 9.2 Osservabilità e telemetria

## Panoramica e motivazioni

La [telemetria](https://en.wikipedia.org/wiki/Telemetry) è il dato che un sistema emette sul proprio comportamento: le metriche, i log, le tracce e gli eventi raccolti dal software in esecuzione. Il monitoraggio risponde da quella telemetria a domande che già sapevi di dover porre. Il disco è pieno? Il tasso di errore è sopra una soglia? Il servizio è attivo? L'[osservabilità](https://en.wikipedia.org/wiki/Observability_(software)) è più ampia. È la capacità di porre nuove domande sullo stato interno di un sistema dall'esterno, senza rilasciare nuovo codice, così da capire comportamenti che non avevi anticipato. Man mano che i sistemi crescono in [microservizi](https://en.wikipedia.org/wiki/Microservices) distribuiti e [architetture a eventi](https://en.wikipedia.org/wiki/Event-driven_architecture), i guasti che fanno più male sono quelli che nessuno aveva visto arrivare e l'osservabilità è ciò che ti permette di farne il debug. Il monitoraggio ti dice che qualcosa non va. L'osservabilità ti aiuta a scoprire perché.

Per i grandi team, questa distinzione è decisiva. Potevi capire un monolite leggendo i log su una sola macchina. Una piattaforma moderna attraversa centinaia di servizi, molti team, più regioni e dipendenze di terze parti, dove una singola richiesta dell'utente può toccare decine di componenti. Nessuno tiene l'intero sistema nella testa. Una telemetria condivisa e di alta qualità diventa il tessuto connettivo che permette a qualsiasi ingegnere di seguire una richiesta attraverso i confini, di allineare i sintomi tra i servizi e di ragionare su un sistema che nessuno possiede per intero. Senza di essa, gli incidenti si trascinano, la colpa vola tra i team e le cause radice restano nascoste.

I sistemi aziendali e governativi alzano la posta con conformità, verificabilità e responsabilità pubblica. I regolatori possono richiedere evidenza di chi ha avuto accesso a che cosa e quando. I team di sicurezza hanno bisogno di telemetria per rilevare le intrusioni. I servizi rivolti ai cittadini devono mostrare di rispettare gli impegni di prestazione pubblicati. Una buona osservabilità serve tutto questo insieme: è uno strumento ingegneristico, un controllo di sicurezza e un meccanismo di responsabilità in uno. Standardizzarsi su una strumentazione aperta evita il lock-in sugli agenti proprietari di un singolo fornitore, il che conta enormemente quando i sistemi devono durare decenni e sopravvivere ai cicli di appalto.

*Vedi anche:* capitolo 9.1 (site reliability engineering e SLO), capitolo 9.3 (gestione degli incidenti) e capitolo 3.3 (sistemi distribuiti).

## Principi chiave

- **Strumenta per domande sconosciute.** Progetta la telemetria così da poter indagare guasti nuovi, oltre a quelli che avevi previsto.
- **Tre pilastri, una storia.** Metriche, log e tracce sono viste complementari; il loro valore si moltiplica quando sono correlate, non isolate.
- **Struttura tutto.** Una telemetria strutturata e analizzabile dalle macchine con campi coerenti batte il testo libero che solo gli umani possono leggere.
- **Correla con identificativi condivisi.** ID di traccia e di richiesta propagati ovunque ti permettono di ricucire un singolo evento tra i servizi.
- **Dai l'allarme sui sintomi, non sulle cause.** Chiama le persone per problemi visibili agli utenti; lascia che dashboard e indagine facciano emergere la causa sottostante.
- **Ogni chiamata deve essere azionabile.** Un allarme che non richiede alcuna azione umana è rumore che erode la fiducia e causa fatica.
- **L'alta cardinalità è una funzionalità.** La capacità di sezionare per utente, richiesta, regione e versione è ciò che rende possibile il debug in produzione.
- **Possiedi la tua strumentazione.** Standardizzati su una telemetria aperta e neutrale rispetto ai fornitori così da controllare i tuoi dati e poter cambiare backend.

## Raccomandazioni

### Costruisci sui tre pilastri e oltre

Le **metriche** sono serie temporali numeriche, economiche da conservare e ideali per dashboard, andamenti e soglie di allarme. I **log** sono registrazioni discrete e con timestamp di eventi, ricche di dettagli ed essenziali per l'indagine forense. Le **[tracce](https://en.wikipedia.org/wiki/Tracing_(software))** seguono una singola richiesta mentre si muove tra i servizi, mostrando latenza e dipendenze lungo il grafo di chiamate distribuito. Oltre a questi, considera gli **eventi** (cambiamenti di stato significativi come i deploy), i **profili** (dove il codice spende CPU e memoria) e il **[real user monitoring](https://en.wikipedia.org/wiki/Real_user_monitoring)** dell'esperienza effettiva del client. Nessun pilastro basta da solo. L'obiettivo è muoversi con fluidità tra di essi durante un'indagine.

### Standardizzati su OpenTelemetry e sul logging strutturato

Adotta [OpenTelemetry](https://en.wikipedia.org/wiki/OpenTelemetry) come standard neutrale rispetto ai fornitori per generare e raccogliere metriche, log e tracce. Separa la strumentazione dal backend di analisi, così puoi cambiare fornitore senza ristrumentare centinaia di servizi. Questa proprietà è critica per i sistemi aziendali e governativi di lunga vita. Emetti i log come record strutturati (per esempio JSON) con nomi di campo coerenti per timestamp, gravità, servizio e identificativi. Propaga un ID di traccia o di correlazione dal bordo attraverso ogni chiamata a valle e includilo in ogni riga di log e in ogni exemplar di metrica, così che i tre pilastri si colleghino automaticamente.

### Progetta gli allarmi per l'azionabilità e il basso rumore

La tua filosofia degli allarmi decide se la reperibilità è sostenibile. Dai l'allarme soprattutto sui sintomi che gli utenti sentono, espressi come tassi di consumo dell'SLO ([obiettivo di livello di servizio](https://en.wikipedia.org/wiki/Service-level_objective)). Chiama quando stai consumando il tuo budget di errore (il divario ammesso da quell'obiettivo) abbastanza in fretta da violarlo, usando allarmi di consumo a più finestre per bilanciare rilevamento rapido e falsi allarmi. Riserva le chiamate ai problemi che richiedono un'azione umana immediata e instrada tutto il resto a ticket o dashboard. Sfoltisci senza pietà gli allarmi che scattano senza richiedere azione, perché la fatica da allarmi è una causa principale di incidenti veri mancati e di esaurimento dei reperibili. Ogni allarme dovrebbe rimandare a un runbook.

### Modella la salute con dashboard e monitoraggio degli SLO

Costruisci dashboard attorno a un chiaro modello di salute, non a un muro di ogni metrica che hai. Un buon quadro di partenza sono i "quattro segnali d'oro": latenza, traffico, errori e saturazione. Crea dashboard a livello di servizio che mostrino a colpo d'occhio lo stato degli SLO e il budget di errore residuo, più dashboard di livello superiore che modellano la salute complessiva del sistema e dei percorsi degli utenti. Curale deliberatamente, perché dashboard che mostrano tutto non comunicano nulla. Tienile vicine agli allarmi e ai runbook, così che chi risponde passi rapidamente dal segnale al contesto all'azione.

### Abilita il debug in produzione con l'alta cardinalità

I problemi di produzione più difficili colpiscono una fetta stretta: un cliente, una regione, una versione dell'API, un tipo di dispositivo. Per indagarli ti serve una telemetria **ad alta cardinalità**, la capacità di raggruppare e filtrare per campi con molti valori distinti come l'ID utente o l'ID di richiesta. Eventi larghi e ricchi di attributi che portano molte dimensioni per record ti permettono di porre domande arbitrarie a posteriori. Mantieni abbastanza cardinalità e fedeltà di campionamento da isolare i valori anomali e privilegia le tracce collegate agli exemplar così che un picco su una metrica ti porti dritto a richieste lente rappresentative.

### Gestisci costo, conservazione e campionamento

Il volume della telemetria cresce con il sistema e può diventare una spesa importante. Fissa politiche di conservazione per classe di dati: tieni brevemente i dati ad alta risoluzione e più a lungo gli aggregati. Applica un campionamento intelligente alle tracce, orientato a conservare errori e richieste lente, così da trattenere la coda interessante senza pagare per ogni successo di routine. Rivedi regolarmente la spesa di telemetria, perché i costi di osservabilità non gestiti possono rivaleggiare con l'infrastruttura che osservano.

## Compromessi: vantaggi e svantaggi

| Decisione | Vantaggi | Svantaggi |
|---|---|---|
| Eventi ad alta cardinalità | Potente debug, chiedi qualsiasi cosa | Maggior costo di archiviazione e query |
| Campionamento aggressivo | Costo inferiore, meno rumore | Può perdere eventi rari |
| Allarmi basati sui sintomi | Meno chiamate, azionabili | Richiede buoni SLO per funzionare bene |
| Standard OpenTelemetry | Neutrale rispetto ai fornitori, portabile | Sforzo di migrazione, strumenti in maturazione |
| Lunga conservazione dei log | Migliore forense e audit | Costo di archiviazione, esposizione della privacy |

Le decisioni di osservabilità si riducono a una tensione tra fedeltà e costo. Catturare tutto a piena risoluzione ti dà una visione retrospettiva perfetta, ma su larga scala è proibitivamente costoso. Taglia in modo aggressivo e risparmi denaro, ma puoi buttare via l'unica registrazione che avrebbe spiegato un'interruzione. Campionamento e livelli di conservazione sono come i team maturi percorrono questa linea, conservando errori e valori anomali mentre diradano i dati di routine. Il compromesso sugli allarmi è tra sensibilità e rumore: troppi allarmi causano fatica e incidenti mancati, troppo pochi lasciano marcire i problemi. Gli allarmi basati sui sintomi e guidati dagli SLO risolvono gran parte di questo, ma solo se hai SLO significativi in atto.

## Domande da discutere con il tuo team

1. **Qual è il vostro piano per portare i servizi preesistenti su OpenTelemetry, e come evitate di pagare due stack di strumentazione durante la transizione?** La strumentazione neutrale rispetto ai fornitori è la proprietà che permette di cambiare backend senza ristrumentare centinaia di servizi e conta di più per i sistemi aziendali e governativi di lunga vita che sopravvivono a qualsiasi singolo contratto con un fornitore. La migrazione è dove le buone intenzioni si fermano: i patrimoni strumentati a metà lasciano lacune esattamente dove una richiesta passa da un servizio nuovo a uno vecchio, rompendo la traccia da capo a capo. Portate un inventario alla discussione: quali servizi emettono dati di agenti proprietari, quali emettono OpenTelemetry e dove il contesto di traccia viene perso al confine. Decidete una sequenza che segua i veri percorsi delle richieste anziché gli organigrammi e mettete a bilancio la finestra in cui gestite entrambi i collettori. La risposta determina se possedete davvero la vostra telemetria o restate vincolati agli agenti di un solo fornitore.

2. **Quando avete verificato l'ultima volta ogni allarme per azionabilità, e quante chiamate del mese scorso non richiedevano alcuna azione umana?** La fatica da allarmi è una causa principale di incidenti veri mancati e di esaurimento dei reperibili, quindi una chiamata che non richiede azione non è un rumore innocuo, erode attivamente la risposta da cui dipendete. Portate le ricevute: estraete le chiamate del mese scorso, segnate ciascuna come azionata o ignorata e contate quante corrispondevano a un runbook. Per un grande team che attraversa molti servizi, gli allarmi rumorosi di un team desensibilizzano la reperibilità condivisa per tutti. Fissate lo standard che ogni chiamata rimandi a un runbook e sia legata a un tasso di consumo dell'SLO, poi cancellate il resto senza pietà. Il risultato di questa verifica dovrebbe tagliare direttamente il vostro volume di chiamate e dirvi quali servizi non hanno un SLO significativo dietro i loro allarmi.

3. **Qual è la vostra strategia di campionamento delle tracce, e quanto siete sicuri che conservi gli errori e la coda lenta?** Il volume della telemetria cresce con il sistema e il costo di osservabilità non gestito può rivaleggiare con l'infrastruttura che osserva, quindi campionerete e la domanda è se campionate in modo intelligente. Eliminare cardinalità o campionare alla cieca rimuove esattamente le registrazioni necessarie a fare il debug dei problemi stretti che colpiscono un cliente, una regione o una versione dell'API. Portate i vostri attuali livelli di conservazione e regole di campionamento: privilegiate la conservazione di errori e richieste lente, usate tracce collegate agli exemplar così che un picco di metrica porti a una richiesta lenta rappresentativa? Per i sistemi sottoposti ad audit e vincolati dalla privacy, riconciliate la conservazione con le regole di minimizzazione dei dati così da non accumulare dati personali per fare il debug. La risposta fissa dove spendete il budget di telemetria e se la vostra prossima dura interruzione sarà spiegabile o un mistero.

4. **Quali dei vostri SLO sono veri impegni sul percorso dell'utente, e quali sono metriche proxy a cui nessuno fuori dal team responsabile crede?** Gli allarmi basati sui sintomi funzionano solo quando i sintomi corrispondono a cose che gli utenti sentono davvero, quindi un allarme collegato a una soglia di CPU o a un obiettivo di disponibilità inventato chiama le persone per problemi che possono non contare restando muto su quelli che contano. Per una grande organizzazione, gli SLO sono anche il contratto che permette a team indipendenti di condividere una rotazione di reperibilità senza rilitigare la gravità a ogni incidente. Portate il catalogo attuale degli SLO, il percorso utente che ciascun obiettivo deve proteggere e le violazioni dell'ultimo trimestre con se i clienti si siano davvero lamentati. Nei contesti aziendali e governativi, legate gli SLO più visibili agli impegni di prestazione pubblicati a cui il servizio è tenuto, così che lo stesso segnale di consumo che chiama un ingegnere sia anche l'evidenza che mostrate a un regolatore o a un organo di controllo. La discussione dovrebbe ritirare le metriche proxy e lasciarvi con un breve elenco di obiettivi che un non ingegnere riconoscerebbe come promesse agli utenti.

5. **Chi possiede la governance dei dati di telemetria, e potete provare che i dati personali sono oscurati prima di finire nel vostro backend di osservabilità?** Eventi ad alta cardinalità e lunga conservazione dei log sono esattamente le funzionalità che rendono possibile il debug ed esattamente quelle che trasformano un archivio di osservabilità in una copia non gestita dei dati personali dei vostri utenti. La spinta contraria è reale: gli ingegneri vogliono attributi più ricchi e conservazione più lunga, mentre privacy e ufficio legale vogliono minimizzazione dei dati e durate brevi. Portate una mappa dei flussi di dati che mostri quali campi portano dati personali o sensibili, dove avviene l'oscuramento o la tokenizzazione nella pipeline e quali sono i vostri livelli di conservazione per classe di dati. Per i sistemi regolamentati e pubblici, nominate il responsabile, mappate la conservazione alla base giuridica e alle regole di minimizzazione dei dati con cui operate e siate pronti a mostrare a un auditor che l'accesso alla telemetria stessa è registrato e controllato. La risposta decide se la vostra piattaforma di osservabilità è una risorsa o una violazione permanente in attesa di essere scoperta.

6. **Quando un incidente attraversa i servizi di più team, la vostra telemetria permette a un solo addetto di seguire la richiesta da capo a capo, o la traccia si spezza a ogni confine di proprietà?** Tutta la promessa di una telemetria correlata e con ID propagati è che un singolo ingegnere possa ragionare su un sistema che nessuno possiede per intero e quella promessa crolla esattamente al confine in cui il contesto di traccia viene perso o dove due team usano identificativi e strumenti incompatibili. Pesate la spinta verso l'autonomia dei team nella scelta degli strumenti di osservabilità contro il costo condiviso di un patrimonio frammentato in cui ogni passaggio di consegne è un vicolo cieco durante un'interruzione. Portate una cronologia recente di un incidente tra più team e segnate dove chi rispondeva ha perso il filo, più un inventario di quali servizi propagano un ID di correlazione comune e quali no. Per una grande impresa o una piattaforma governativa assemblata da molti fornitori e sistemi di lunga vita, decidete quanto mandare a livello centrale, uno standard comune di contesto di traccia e uno schema comune di ID, rispetto a ciò che lasciate ai team, perché i componenti che ri-appaltate nel corso dei decenni devono comunque interoperare sulla stessa richiesta. La risposta vi dice se il vostro prossimo incidente tra più team sarà un'indagine coordinata o un giro di rimpalli di colpe.

## Lente settoriale

**Startup.** Con una manciata di servizi e nessuna mano di riserva, strumenta con OpenTelemetry dal primo giorno e rilascia log JSON strutturati che portano un ID di richiesta da capo a capo. Quel piccolo investimento trasforma "l'app è lenta" in una traccia che puoi leggere e ti lascia libero di passare da un livello gratuito a un backend a pagamento più avanti senza ristrumentare. Salta dashboard elaborate e macchinario di SLO finché non hai utenti la cui esperienza puoi davvero misurare.

**Piccola impresa.** Non hai uno specialista di osservabilità e hai un budget stretto, quindi appoggiati a un backend gestito in cui strumentazione, archiviazione e dashboard sono incluse anziché assemblare uno stack tuo. La scelta tra comprare e costruire favorisce quasi sempre il comprare qui; la tua scarsa attenzione è meglio spesa sui due o tre allarmi dei segnali d'oro che ti dicono che il servizio è giù che a gestire una pipeline di telemetria. Fissa un limite rigido di conservazione così che il costo della telemetria non superi in silenzio l'infrastruttura che osserva.

**Grande impresa.** Il lavoro è la governance tra molti team: uno standard OpenTelemetry condiviso, uno schema comune di ID di correlazione e dashboard SLO curate così che un singolo addetto possa seguire una richiesta attraverso decine di servizi. Gestisci la telemetria come un centro di costo con livelli di conservazione e politica di campionamento, standardizza gli allarmi sui tassi di consumo degli SLO per mantenere sostenibile una reperibilità condivisa e sfoltisci centralmente gli allarmi rumorosi così che la fatica di un team non desensibilizzi tutti. Tratta lo strato di strumentazione come infrastruttura neutrale rispetto ai fornitori che sopravvive a qualsiasi singolo contratto di backend.

**Ente pubblico.** Regole di appalto, trasparenza e responsabilità pubblica plasmano il progetto. Standardizzati su una strumentazione aperta così che un sistema destinato a girare per decenni sopravviva al ri-appalto a fornitori diversi senza essere ostaggio di agenti proprietari ed esigi quella portabilità nel contratto. Usa log di audit strutturati per mostrare chi ha avuto accesso a quale record e quando, oscura o tokenizza i dati personali prima che raggiungano l'archivio di telemetria e riconcilia la conservazione con la legge sulla minimizzazione dei dati. Pubblica dashboard SLO per i servizi rivolti ai cittadini così che gli stessi segnali che i tuoi ingegneri osservano siano evidenza visibile degli impegni a cui sei tenuto.

## Esempi

**Startup.** Una startup di quattro persone rilascia un backend mobile e continua a ricevere vaghi reclami "l'app è lenta" che non riesce a riprodurre. Il team aggiunge OpenTelemetry ai suoi pochi servizi e passa a log JSON strutturati con un ID di richiesta portato dall'app attraverso ogni passaggio. La segnalazione di lentezza successiva si risolve in minuti: una traccia mostra un indice di database mancante sulla tabella degli ordini sotto una specifica query. Poiché hanno scelto presto una strumentazione aperta, più tardi passano da un livello gratuito a un backend a pagamento senza ristrumentare nulla.

**Grande impresa.** Una grande piattaforma di e-commerce strumenta ogni servizio con OpenTelemetry, propagando un ID di traccia dal browser del cliente attraverso checkout, pagamento, magazzino e spedizione. Quando la conversione cala, un ingegnere reperibile parte da un allarme di consumo dell'SLO, apre i segnali d'oro della dashboard del checkout, nota una latenza elevata in una regione e segue una traccia exemplar fino a una lenta chiamata al database in un solo servizio. Gli attributi ad alta cardinalità mostrano che il problema è confinato a una categoria di prodotto, il che guida una correzione mirata in minuti anziché ore.

**Ente pubblico.** Un servizio sanitario nazionale gestisce una piattaforma di cartelle dei pazienti sotto rigorose regole di audit e privacy. I log strutturati catturano chi ha avuto accesso a quale record e quando, alimentando sia il monitoraggio di sicurezza sia la reportistica di conformità, mentre i campi che identificano personalmente sono oscurati o tokenizzati nella telemetria. Dashboard SLO pubbliche mostrano disponibilità e latenza della prenotazione di appuntamenti rivolta ai cittadini. Standardizzandosi su una strumentazione aperta, l'ente evita il lock-in proprietario su un sistema destinato a girare per decenni e a essere ri-appaltato a fornitori diversi nel corso della sua vita.

## Business case: motivazioni, ROI e TCO

Il ritorno principale dell'osservabilità è un calo drastico del tempo necessario per rilevare e risolvere gli incidenti. Per un servizio in cui il fermo è costoso, ridurre il tempo medio di risoluzione da ore a minuti ripaga gli strumenti molte volte in un solo grande incidente. L'osservabilità fa anche risparmiare il tempo di ingegneria che spenderesti altrimenti a indovinare, riprodurre bug e discutere su quale team sia in colpa e accorcia il ciclo di riscontro che permette ai team di rilasciare con fiducia. Anche il valore di sicurezza e conformità è reale: la stessa telemetria supporta il rilevamento delle intrusioni e l'evidenza di audit.

Il costo totale di proprietà comprende sforzo di strumentazione, costi di archiviazione e query della telemetria e la disciplina di curare il segnale dal rumore. Questi costi sono visibili e ricorrenti, il che tenta la leadership a investire troppo poco. Il costo del non adottare è maggiore ma più difficile da vedere: interruzioni prolungate, problemi di prestazione non diagnosticati, incidenti di sicurezza scoperti tardi o mai ed ingegneri che si esauriscono su allarmi su cui non possono fare nulla. Presenta il caso con dati concreti sugli incidenti. Mostra il tempo di risoluzione e l'impatto sul business delle interruzioni recenti e proietta la riduzione che una telemetria migliore darebbe. Impostare l'osservabilità come un'assicurazione che accelera anche la consegna, anziché come puro centro di costo, vince la discussione.

## Antipattern e insidie

- **Allarme su tutto.** Chiamare per ogni anomalia addestra chi risponde a ignorare gli allarmi, così gli incidenti veri sfuggono.
- **Chiamate basate sulle cause.** Dare l'allarme sulle cause interne anziché sui sintomi per gli utenti inonda la reperibilità di rumore e perde i guasti nuovi.
- **Log non strutturati.** I log in testo libero che non si possono interrogare né correlare costringono a lenti grep manuali durante gli incidenti.
- **Tre pilastri isolati.** Metriche, log e tracce in strumenti disconnessi senza ID condivisi impediscono di seguire un evento da capo a capo.
- **Proliferazione di dashboard.** Centinaia di dashboard non curate significano che nessuno sa quale mostri se il sistema è sano.
- **Collasso della cardinalità.** Eliminare i campi ad alta cardinalità per risparmiare rimuove esattamente i dati necessari a fare il debug dei problemi stretti.
- **Lock-in sul fornitore.** Agenti proprietari ovunque rendono proibitivo cambiare backend e tengono in ostaggio i tuoi dati.

## Modello di maturità

**Livello 1, Avvio.** L'osservabilità è ad hoc e reattiva. Controlli di base dell'uptime e log non strutturati vivono sulle singole macchine, il debug significa accedere ai server per fare grep e non c'è telemetria condivisa. Gli allarmi sono rumorosi, basati sulle cause e spesso ignorati, così gli incidenti veri emergono dai reclami degli utenti anziché dai segnali.

**Livello 2, Sviluppo.** Compaiono pratiche di base ma variano per team. Alcuni servizi inviano metriche e log a un posto centrale, esistono poche dashboard e allarmi a soglia, ma i log sono solo semi-strutturati e le tracce sono assenti o parziali. La correlazione tra servizi è manuale e se un ingegnere può seguire una richiesta da capo a capo dipende da quali team sono coinvolti.

**Livello 3, Standardizzazione.** La strumentazione è documentata e fatta rispettare in tutta l'organizzazione. OpenTelemetry nei servizi con un ID di traccia o correlazione propagato, logging strutturato con nomi di campo coerenti, tracciamento distribuito, dashboard curate dei segnali d'oro e allarmi sui sintomi basati sugli SLO sono lo standard che ogni team segue. Ogni chiamata rimanda a un runbook ed è legata a un SLO e la reperibilità è sostenibile anziché una fonte di esaurimento.

**Livello 4, Gestione.** Il patrimonio di osservabilità stesso è misurato e controllato rispetto a valori di riferimento. Segui copertura della strumentazione e tasso di propagazione del contesto di traccia nei servizi, la quota di chiamate azionate rispetto a ignorate, tempo medio di rilevamento e risoluzione, raggiungimento degli SLO e consumo del budget di errore e costo di telemetria per servizio rispetto a un budget. Lacune e rumore degli allarmi sono ridotti con dati verso obiettivi espliciti, la fedeltà di campionamento è verificata così che le registrazioni di errori e coda lenta sopravvivano e le decisioni di procedere o meno su copertura e conservazione sono prese sull'evidenza anziché sull'opinione.

**Livello 5, Orchestrazione.** L'osservabilità è continuamente migliorata e integrata nell'organizzazione. Una telemetria ad alta cardinalità e ricca di eventi permette l'indagine ad hoc di qualsiasi fetta, gli allarmi sono guidati dal tasso di consumo dell'SLO con rumore minimo e campionamento e conservazione si adattano a costo e rischio mutevoli. La telemetria alimenta di routine pianificazione della capacità, rilevamento della sicurezza e decisioni di prodotto e la piattaforma riregola i propri segnali, budget e copertura man mano che si spostano il sistema, il quadro delle minacce e gli obblighi normativi.

## Spunti di discussione

- Dov'è il giusto equilibrio tra fedeltà della telemetria e costo per i vostri servizi più critici?
- Come decidete che cosa merita una chiamata rispetto a un ticket rispetto a una sola voce di dashboard?
- Qual è la vostra strategia per propagare gli ID di correlazione tra team che non condividono una base di codice né un ciclo di rilascio?
- Come preservate il potere di debug ad alta cardinalità rispettando i requisiti di privacy e minimizzazione dei dati?
- Gli strumenti di osservabilità dovrebbero essere imposti centralmente o scelti per team, e quali sono le conseguenze nell'uno e nell'altro caso?
- Come dimostrereste agli auditor che la vostra telemetria è completa e a prova di manomissione?

## Punti chiave

- Il monitoraggio rileva i problemi noti; l'osservabilità ti permette di indagare quelli sconosciuti senza rilasciare nuovo codice.
- Metriche, log e tracce hanno il massimo valore quando sono correlati tramite identificativi condivisi, non isolati.
- Standardizzati su OpenTelemetry e sul logging strutturato per restare neutrale rispetto ai fornitori e portabile lungo la lunga vita dei sistemi.
- Dai l'allarme sui sintomi visibili agli utenti tramite i tassi di consumo degli SLO, rendi azionabile ogni chiamata e sfoltisci senza sosta il rumore.
- Cura le dashboard attorno a un chiaro modello di salute come i segnali d'oro anziché mostrare ogni metrica.
- Una telemetria ad alta cardinalità e ricca di eventi è ciò che rende possibile il debug dei problemi di produzione stretti.

## Riferimenti e letture di approfondimento

- Charity Majors, Liz Fong-Jones, George Miranda, *Observability Engineering: Achieving Production Excellence*
- Cindy Sridharan, *Distributed Systems Observability*
- Betsy Beyer et al., *Site Reliability Engineering* (capitoli su monitoraggio e allarmi)
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud*
- Progetto OpenTelemetry, specifica e documentazione (Cloud Native Computing Foundation)
- Google, *The Four Golden Signals* (Site Reliability Engineering, capitolo sul monitoraggio)
