# 11.2 La pipeline di consegna

## Panoramica e motivazioni

La pipeline di consegna è il flusso di lavoro che trasforma un'idea convalidata in software funzionante nelle mani degli utenti (in modo affidabile, ripetibile e misurabile) e poi riporta i dati sugli esiti risultanti nella scoperta (capitolo 11.1). È il percorso industrializzato da un commit di codice a una modifica in produzione a un effetto misurato su utenti e business. Dove la scoperta risponde a *che cosa e perché*, la consegna risponde a *come lo rilasciamo in sicurezza, quanto in fretta e se ha davvero funzionato*.

Questo capitolo è deliberatamente integrativo. La meccanica vive nel dettaglio altrove: strategia di test (capitolo 2.4), automazione di test e processi (capitolo 8.5), [integrazione continua](https://en.wikipedia.org/wiki/Continuous_integration) e [consegna continua](https://en.wikipedia.org/wiki/Continuous_delivery) (CI/CD) e strategie di distribuzione (capitolo 8.1), infrastruttura come codice (capitolo 8.2), affidabilità e SLO (obiettivi di livello di servizio, capitolo 9.1) e sperimentazione (capitolo 7.4). Qui le assembliamo in un'unica pipeline da un capo all'altro e, soprattutto, vi associamo le **metriche di esito** che dicono se l'intera macchina sta producendo valore anziché limitarsi a produrre rilasci.

Per i grandi team, la pipeline di consegna è il singolo investimento a più alta leva nell'efficacia ingegneristica. Un decennio di ricerca, più notoriamente il programma DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) riassunto in *Accelerate*, mostra che i team con pipeline di consegna veloci, automatiche e a basso rischio superano gli altri su produttività *e* stabilità *e* esiti organizzativi. La vecchia credenza che velocità e sicurezza si scambino l'una contro l'altra è empiricamente falsa. Nelle imprese, una pipeline solida è ciò che permette a centinaia di ingegneri di integrare senza collassare nel caos delle unioni e nel teatro dei rilasci manuali. Nel governo, sostituisce i rilasci "big bang" ad alta cerimonia, trimestrali e tutto-o-niente (storicamente una causa primaria di programmi falliti) con modifiche piccole, reversibili e verificabili che soddisfano gli obblighi di controllo delle modifiche *attraverso* l'automazione anziché a dispetto di essa.

## Principi chiave

- **Automatizza tutto ciò che si ripete.** I passi manuali sono lenti, soggetti a errori e non verificabili.
- **Lotti piccoli, rilasci frequenti.** Le modifiche piccole sono più facili da rivedere, testare, rilasciare e invertire.
- **Costruisci la qualità dentro.** Test e cancelli rapidi e automatici colgono i difetti prima della produzione, non dopo.
- **Separa distribuzione e rilascio.** Rilascia il codice al buio; attiva le funzionalità con i flag quando sei pronto.
- **Rendi tutto reversibile.** Rollback rapido ed esposizione progressiva trasformano la distribuzione da scommessa a esperimento.
- **La pipeline è la fonte di verità.** Se non è nel controllo di versione e nella pipeline, non è successo.
- **Misura gli esiti, non solo le produzioni.** Il conteggio dei deploy è una produzione; una metrica mossa è un esito.

## Raccomandazioni

### Automatizza la suite di test e usala come cancello

L'automazione dei test è la fondazione che rende sicura la consegna veloce. Implementa un portafoglio di test bilanciato e per lo più automatico (capitolo 2.4): molti test unitari veloci, meno test di integrazione e di contratto, un piccolo numero di test end-to-end, più controlli automatici di sicurezza (SAST/DAST/SCA: analisi statica, dinamica e di composizione del software), accessibilità e prestazioni. Eseguili come **cancelli di qualità** nella pipeline così che nessuna modifica raggiunga la produzione senza superarli. Mantieni la suite veloce e affidabile: una suite lenta o instabile viene aggirata, il che ne vanifica lo scopo (capitolo 8.5). Punta a far dare allo sviluppatore un chiaro segnale di superato/fallito entro minuti da un commit.

### Pratica l'integrazione continua e la consegna continua

**Integrazione continua (CI):** ogni sviluppatore unisce frequentemente piccole modifiche nella linea principale (idealmente ogni giorno) e ogni unione innesca una build e un'esecuzione di test automatiche. È sostenuta al meglio dallo sviluppo trunk-based (capitolo 2.6), che mantiene i rami di breve durata e l'integrazione continua. **Consegna continua (CD):** ogni modifica che supera la pipeline è *sempre in uno stato rilasciabile* e può essere distribuita a richiesta. La **distribuzione continua** fa un passo in più: ogni modifica che supera i controlli viene distribuita automaticamente in produzione. Scegli il livello di automazione adatto al tuo profilo di rischio; gli ambienti regolati possono fermarsi alla consegna continua con un passo di promozione controllato (capitolo 8.1), ma dovrebbero comunque automatizzare tutto fino a quel cancello.

### Distribuisci in sicurezza con strategie progressive

Separa la **distribuzione** (codice che gira in produzione) dal **rilascio** (utenti che sperimentano la modifica) ed esponi le modifiche gradualmente:

- I **[feature flag](https://en.wikipedia.org/wiki/Feature_toggle)** ti permettono di distribuire il codice al buio e di rilasciare a segmenti su richiesta, e di tornare indietro istantaneamente commutando.
- I **rilasci canary** instradano una piccola percentuale di traffico alla nuova versione, osservando le metriche di salute prima di allargare.
- Le **distribuzioni blue-green** tengono due ambienti e commutano il traffico in modo atomico, con rollback istantaneo.
- Le **distribuzioni rolling** sostituiscono le istanze in modo incrementale.
- La **consegna progressiva** combina flag, canary e analisi automatica per promuovere o tornare indietro sulla base di segnali dal vivo.

Abbina ogni strategia a un rollback automatico innescato da violazioni degli SLO o dal consumo del budget di errore (il ritmo a cui i fallimenti consumano il budget di inaffidabilità consentito; capitolo 9.1). Vedi il capitolo 8.1 per la meccanica.

### Strumenta le metriche di esito: misura la pipeline e l'impatto

Una pipeline di consegna che rilascia in fretta ma rilascia la cosa sbagliata è spreco veloce. Misura a tre livelli:

1. **Flusso di consegna, le quattro metriche DORA:**
   - *Frequenza di distribuzione:* quanto spesso rilasci in produzione.
   - *[Tempo di attesa](https://en.wikipedia.org/wiki/Lead_time) per le modifiche:* dal commit alla produzione.
   - *Tasso di fallimento delle modifiche:* percentuale di rilasci che causano un degrado.
   - *Tempo di ripristino dopo un deploy fallito:* quanto in fretta ripristini il servizio (in precedenza MTTR, tempo medio di ripristino).
   Le prestazioni d'élite distribuiscono a richiesta, con tempi di attesa sotto l'ora, bassi tassi di fallimento e ripristino in minuti. Aggiungi **metriche di flusso** dal pensiero del flusso di valore (tempo di ciclo, [lavoro in corso](https://en.wikipedia.org/wiki/Work_in_process), efficienza del flusso) per vedere dove il lavoro aspetta.

2. **Affidabilità e qualità, SLI e SLO** (indicatori e obiettivi di livello di servizio; capitolo 9.1): il servizio rispetta i suoi obiettivi di affidabilità e gli impegni sugli attributi di qualità (capitolo 11.1) dopo ogni modifica?

3. **Esiti per il business e per gli utenti** (capitoli 7.3–7.4): la modifica ha mosso i risultati chiave e i KPI definiti dalla scoperta? È qui che il rilascio incontra l'esperimento: rilascia dietro un flag, misura rispetto a un controllo e tieni solo ciò che vince.

### Chiudi il ciclo verso la scoperta

L'ultimo atto della pipeline di consegna non è la distribuzione; è l'**evidenza**. Le metriche di esito (l'attivazione è salita, il tempo di checkout è sceso, i ticket di supporto sono calati) rifluiscono nella pipeline di scoperta (capitolo 11.1) come base per il giro successivo di scommesse. Quando scoperta e consegna sono unite da questo ciclo di riscontro, l'organizzazione diventa un sistema che impara: le ipotesi sono rilasciate, misurate e poi scalate o invertite, di continuo.

### Rendi la consegna verificabile e governata

Nei contesti aziendali e governativi, tratta la pipeline stessa come un controllo di conformità. Poiché ogni modifica passa attraverso il controllo di versione e una pipeline automatica, ottieni "gratis" una traccia di audit immutabile: chi ha cambiato che cosa, quali test e approvazioni l'hanno condizionata e quando è stata distribuita. Codifica separazione dei compiti, revisioni obbligatorie e controlli di politica come **politica come codice** (regole di governance espresse in forma applicabile da una macchina e sotto controllo di versione; capitolo 8.2) così che il controllo delle modifiche sia fatto rispettare automaticamente e documentato di continuo (capitoli 4.6 e 10.2), anziché ricostruito a mano prima di un audit.

## Compromessi: vantaggi e svantaggi

| Decisione | Vantaggi | Svantaggi |
|---|---|---|
| **Distribuzione continua (automatica in produzione)** | Riscontro più rapido; lotti più piccoli; minor fatica manuale | Esige test maturi, monitoraggio, rollback; difficile con cancelli regolati |
| **Consegna continua con promozione manuale** | Punto di controllo umano/di conformità; favorevole all'audit | Più lenta; rischio di accumulare modifiche al cancello |
| **Feature flag** | Separazione distribuzione/rilascio; rollback istantaneo; targeting | Debito di flag e complessità combinatoria se non potati |
| **Canary / consegna progressiva** | Limita il raggio d'azione; promozione guidata dai dati | Richiede forte osservabilità e gestione del traffico |
| **Blue-green** | Commutazione e rollback istantanei | Raddoppia il costo degli ambienti; le migrazioni di dati e di stato sono delicate |
| **Pesante processo di rilascio manuale** | Sembra controllato; familiare agli auditor | Lento, soggetto a errori, non riproducibile, mal verificabile nella pratica |

La credenza storica sul compromesso, *vai più veloce e romperai di più*, è quella chiave da ritirare. L'evidenza mostra che le pratiche che aumentano la velocità (automazione, lotti piccoli, test rapidi, reversibilità) sono le *stesse* pratiche che aumentano la stabilità. I veri compromessi riguardano **investimento e granularità del controllo**, non velocità contro sicurezza.

## Domande da discutere con il tuo team

1. **Qual è il vostro vero profilo di rischio e giustifica il fermarsi alla consegna continua anziché andare alla distribuzione continua?** Scegliere il livello di automazione è una decisione vera, non un predefinito. La distribuzione continua dà il riscontro più rapido e i lotti più piccoli, ma esige test maturi, forte osservabilità e rollback istantaneo, quindi un contesto regolato può razionalmente fermarsi a un cancello di promozione controllato. Portate evidenza: il vostro tasso di fallimento delle modifiche, il vostro tempo di ripristino e l'affidabilità della vostra suite di test, perché dicono se l'automatico-in-produzione è sicuro oggi. Per impresa e governo, automatizzate tutto fino al cancello e fate del cancello stesso politica come codice, così che il passo umano aggiunga controllo senza aggiungere fatica manuale. Se non potete ancora fidarvi che la pipeline colga una modifica sbagliata, investite in cancelli e osservabilità prima di girare l'interruttore.

2. **La vostra pipeline può produrre l'evidenza di audit che chiederebbe un regolatore, senza che nessuno la ricostruisca a mano?** Trattate la pipeline stessa come un controllo di conformità. Ogni modifica dovrebbe portare una traccia immutabile di chi ha cambiato che cosa, quali test e approvazioni l'hanno condizionata e quando è stata distribuita, generata automaticamente. Nell'impresa e nel governo, codificate separazione dei compiti e revisioni obbligatorie come politica come codice così che il controllo delle modifiche sia fatto rispettare e documentato di continuo anziché assemblato in preda al panico prima di un audit. Il segnale da portare: scegliete una recente modifica in produzione e provate a produrre la sua intera traccia di approvazioni e test in cinque minuti. Se non ci riuscite, state pagando una preparazione manuale dell'audit e portando un rischio che l'automazione rimuoverebbe.

3. **Quando un rilascio comincia a degradare in produzione, che cosa innesca un rollback ed è automatico?** La reversibilità è ciò che rende la velocità razionale anziché avventata, quindi l'innesco del rollback merita una progettazione esplicita. Decidete se una violazione degli SLO o il consumo del budget di errore riporta indietro automaticamente, o se un umano deve accorgersene, decidere e agire mentre gli utenti soffrono. Portate i vostri ultimi incidenti e misurate il divario tra "la metrica ha cominciato a degradare" e "modifica invertita"; quel divario è il vostro vero raggio d'azione. Per i grandi team che rilasciano molte volte al giorno, il rollback manuale non scala e flag più analisi canary vi permettono di promuovere o tornare indietro su segnali dal vivo. Se la vostra risposta è "qualcuno viene chiamato e capisce cosa fare", state trattando ogni deploy come una scommessa irreversibile.

4. **Quando rilasciate una funzionalità, misurate se ha davvero mosso la metrica che doveva muovere, o contate il deploy e passate oltre?** Una pipeline che rilascia in fretta ma non controlla mai l'impatto è spreco veloce e il divario tra produzione ed esito è dove la maggior parte dell'investimento di consegna perde in silenzio. Per una grande organizzazione, centinaia di rilasci a settimana rendono allettante trattare la frequenza di distribuzione come tabellone dei punteggi, eppure la frequenza misura il movimento, non il valore; la spinta contraria è che misurare gli esiti costa strumentazione, un gruppo di controllo e la disciplina di lasciare spenta una funzionalità perdente. Portate le ultime funzionalità rilasciate e, per ciascuna, la metrica obiettivo definita dalla scoperta, il prima e il dopo misurati e che cosa avete fatto quando non si è mossa. Nei portafogli aziendali e governativi, nominate chi rivede gli esiti con una cadenza fissa e chi ha l'autorità di ritirare una funzionalità rilasciata che non si è mai ripagata, perché una modifica di cui nessuno risponde della misurazione è una che nessuno spegnerà mai. Il test onesto è se sapete indicare una funzionalità che avete invertito *perché* l'evidenza diceva che perdeva.

5. **Quanto ci mette la vostra pipeline a dare allo sviluppatore un segnale di superato/fallito e si fidano abbastanza dei test da non aggirarli?** La velocità del riscontro e la fiducia nella suite sono ciò che fa davvero sbarrare i cancelli di qualità anziché farli aggirare ed entrambe si erodono in silenzio man mano che il codice cresce. Per un grande team, una suite che richiede quaranta minuti o che è instabile una volta su dieci addestra centinaia di ingegneri a unire sul rosso, a disattivare i controlli o a rieseguire finché diventa verde, il che toglie in silenzio la sicurezza che giustificava l'andare veloci; le considerazioni in competizione sono copertura e realismo dei test contro velocità e stabilità del riscontro e spingere troppo l'una mina l'altra. Portate la durata attuale della pipeline, il tasso di riesecuzioni per instabilità e qualsiasi evidenza di cancelli saltati o segnati come non bloccanti. Nei contesti aziendali e governativi dove quei cancelli portano anche SAST, DAST e controlli di politica che soddisfano la conformità, un cancello aggirato è sia un rischio di qualità sia un buco di audit, quindi misurate se il cancello è davvero obbligatorio o solo consultivo. Se gli sviluppatori non sanno articolare perché si fidano di una build verde, il cancello è decorazione.

6. **Chi è responsabile di mantenere coerente il percorso di consegna tra i team e di potare il debito dei feature flag, o ogni team sta reinventando la propria pipeline?** Man mano che un'organizzazione cresce, la consegna o converge su una strada asfaltata condivisa o si frammenta in decine di pipeline su misura con cancelli incompatibili, tracce di audit disomogenee e flag che sopravvivono al loro scopo. La tensione è reale: una strada asfaltata centrale dà coerenza, governance ed economie di scala, ma un mandato che ignora i genuini vincoli di un team genera pipeline ombra e risentimento, quindi la strada asfaltata deve essere abbastanza buona da far aderire i team volentieri. Portate un inventario di quante pipeline distinte esistono oggi, come sono governate creazione e rimozione dei flag e quanto variano tempo di attesa e qualità dell'audit tra i vostri team migliori e peggiori. Nei contesti aziendali e governativi, aggiungete l'angolo della conformità: pipeline incoerenti significano che separazione dei compiti ed evidenza del controllo delle modifiche sono dimostrate in modo diverso (o per niente) in ogni team e una singola strada asfaltata sottoposta ad audit con politica come codice trasforma ciò da scommessa per team in garanzia organizzativa. Se nessuno è responsabile di rimuovere i flag obsoleti, il debito combinatorio renderà alla fine il sistema non testabile.

## Lente settoriale

**Startup.** La velocità è sopravvivenza, quindi compra la tua pipeline anziché costruirla: collega lo sviluppo trunk-based a un runner CI ospitato, condiziona ogni unione a test unitari rapidi e a una scansione di sicurezza e distribuisci direttamente in produzione dietro un servizio di feature flag ospitato. Salta il team di piattaforma e gli strumenti su misura; la tua risorsa più scarsa è l'attenzione ingegneristica e una pipeline che un singolo generalista può mantenere batte una elaborata che nessuno ha tempo di riparare. Segui le quattro metriche DORA su una semplice dashboard dal primo giorno così da imparare presto il tuo flusso e poter mostrare agli investitori che rilasci ogni giorno senza rompere nulla.

**Piccola impresa.** Senza un ingegnere dei rilasci dedicato e con un bilancio stretto, tratta la consegna come qualcosa che assembli da servizi gestiti anziché un sistema che dotti di personale: CI/CD gestita, uno strumento di flag ospitato e una piattaforma cloud che gestisce distribuzione e rollback per te. Resisti a costruire un'infrastruttura di pipeline personalizzata che non puoi permetterti di mantenere e tieni il percorso abbastanza semplice che chiunque sia reperibile possa capirlo sotto pressione. Preferisci strumenti che offrono subito consegna progressiva e rollback con un clic, perché sono le capacità che trasformano un temuto deploy del venerdì in uno di routine.

**Grande impresa.** Il problema centrale è la coerenza tra molti team: una pipeline a strada asfaltata supportata con cancelli automatici di test, sicurezza e politica come codice a cui i team aderiscono anziché reinventare. Standardizza l'interfaccia così che le metriche DORA e SLO siano confrontabili in tutta l'organizzazione, metti a bilancio esplicitamente la capacità di piattaforma che mantiene la strada asfaltata e gestisci i feature flag e le regressioni del tempo di attesa come beni governati anziché folklore per team. Governance e audit si accodano automaticamente quando ogni modifica scorre lungo lo stesso percorso versionato e condizionato.

**Ente pubblico.** Regole di appalto, trasparenza e responsabilità pubblica plasmano la pipeline, quindi privilegia la consegna continua che si ferma a un cancello di promozione automatico che fa rispettare separazione dei compiti e approvazioni obbligatorie come politica come codice. Fai della pipeline stessa il controllo di conformità: ogni modifica porta una traccia di audit immutabile che soddisfa gli obblighi di controllo delle modifiche e di autorizzazione a operare senza ricostruzione manuale. Sostituisci i rilasci "big bang" ad alta cerimonia con modifiche piccole, reversibili e disaccoppiate così da poter provare un flusso rivolto al pubblico in una regione, misurare i tassi di errore e di completamento e tornare indietro in minuti se degrada.

## Esempi

**Startup.** Un team di tre ingegneri che rilascia uno strumento di analisi B2B comincia distribuendo a mano il venerdì pomeriggio, il che significa un rilascio temuto una volta a settimana e un fine settimana di ansia. In un pomeriggio collegano lo sviluppo trunk-based a una pipeline GitHub Actions: test unitari rapidi, un linter e una scansione di sicurezza condizionano ogni unione e una build superata va direttamente in produzione dietro i flag LaunchDarkly. La frequenza di distribuzione salta da settimanale a più volte al giorno e poiché ogni nuova funzionalità viene rilasciata al buio e si attiva prima per un cliente amico, un'esportazione CSV rotta viene colta e spenta in minuti anziché diventare un incidente del lunedì. Seguono le quattro metriche DORA su una semplice dashboard per poter mostrare agli investitori che il team rilascia ogni giorno senza rompere nulla.

**Grande impresa.** Un assicuratore globale consolida 40 team su una pipeline condivisa a strada asfaltata (una catena di strumenti predefinita, supportata e pre-integrata a cui i team aderiscono; capitolo 8.4): sviluppo trunk-based, cancelli automatici di test e sicurezza e distribuzione canary con rollback automatico alla violazione degli SLO. La frequenza di distribuzione sale da mensile a molte volte al giorno; il tempo di attesa scende da sei settimane a meno di un giorno; il tasso di fallimento delle modifiche cala perché i lotti sono piccoli e i cancelli automatici. Fondamentale, le funzionalità di prodotto ora vengono rilasciate dietro flag e misurate rispetto a controlli, così che l'assicuratore possa legare ogni rilascio al suo effetto sul tasso di completamento dei preventivi, collegando la pipeline di consegna direttamente ai risultati chiave sul lato della scoperta del capitolo 11.1.

**Ente pubblico.** Un ente pubblico sostituisce i rilasci "big bang" trimestrali (ciascuno un fine settimana di passi manuali e frequente fonte di interruzioni) con una pipeline di consegna continua che si ferma a un cancello di promozione automatico che fa rispettare separazione dei compiti e approvazioni obbligatorie come politica come codice. Ogni modifica porta una traccia di audit immutabile che soddisfa gli obblighi di controllo delle modifiche e di ATO (autorizzazione a operare) dell'ente (capitolo 4.6). I rilasci diventano piccoli, frequenti e reversibili; il tempo di ripristino scende da giorni a minuti; e poiché la distribuzione è disaccoppiata dal rilascio tramite flag, l'ente può provare un nuovo flusso di prestazioni con una regione prima del lancio nazionale, misurando completamento ed errori prima di impegnarsi.

## Business case: motivazioni, ROI e TCO

Il ritorno dell'investimento nella pipeline di consegna è tra i meglio documentati nel software. Un tempo di attesa più rapido e una maggiore frequenza di distribuzione significano che le idee raggiungono gli utenti (e cominciano a restituire valore, o a essere corrette) prima. Un tasso di fallimento delle modifiche più basso e un ripristino più rapido significano meno interruzioni, meno lavoro in emergenza e meno danno reputazionale e normativo. La ricerca DORA collega queste capacità a prestazioni commerciali e organizzative superiori, non semplicemente al comfort ingegneristico. L'effetto composto conta: un team che rilascia e impara ogni giorno itera 20–30 volte più spesso di uno che rilascia ogni mese e quel tasso di apprendimento è decisivo nella vita di un prodotto.

Sul **[costo totale di proprietà](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**, l'automazione sposta il costo dalla fatica manuale perpetua a un investimento una tantum più manutenzione nella pipeline. Un rilascio manuale consuma ore di ingegneri senior ogni singola volta, scala male e produce una debole evidenza di audit. Una pipeline automatica ammortizza quel costo, poi lo *riduce* man mano che il volume cresce, producendo al contempo continuamente un'evidenza più forte. La reversibilità abbassa il costo del fallimento stesso: quando qualsiasi modifica può essere annullata in secondi, il costo atteso di un cattivo deploy collassa, ed è ciò che rende razionale anziché avventato muoversi in fretta.

Per presentare il caso alla leadership, misura il valore di riferimento attuale con le quattro metriche DORA e le ore manuali spese per rilascio, poi quantifica la fatica rimossa e le interruzioni evitate. Il costo di adozione è reale, cioè ingegneria della pipeline, investimento nei test e una capacità di piattaforma/strada asfaltata (capitolo 8.4), ma il costo del *non* investire è pagato di continuo in riscontro lento, rischio nel giorno del rilascio, esaurimento degli ingegneri e dolore da audit. L'argomento decisivo è il legame con la scoperta: una pipeline di consegna veloce e misurata è ciò che rende le scommesse convalidate della pipeline di scoperta davvero testabili in produzione.

## Antipattern e insidie

- **Misurare la produzione, non l'esito:** festeggiare i conteggi dei deploy mentre le metriche obiettivo restano piatte.
- **Suite di test lente o instabili:** cancelli che gli sviluppatori imparano a ignorare o aggirare.
- **Rilasci big-bang e poco frequenti:** lotti grandi che sono rischiosi, difficili da correggere e difficili da invertire.
- **Distribuzione e rilascio confusi:** niente feature flag, così che ogni deploy è una scommessa irreversibile rivolta all'utente.
- **Teatro del rilascio manuale:** liste di controllo eseguite a mano, lente, incoerenti e mal verificabili.
- **Pipeline automatica, nessuna osservabilità:** rilasciare in fretta senza capacità di rilevare o diagnosticare le regressioni.
- **Debito di feature flag:** flag mai rimossi, che si accumulano in una complessità combinatoria non testabile.
- **Manipolare le metriche DORA:** spezzare i deploy per gonfiare la frequenza anziché migliorare il flusso.
- **Nessun ciclo di riscontro:** esiti mai misurati, così che la consegna non informa mai il successivo ciclo di scoperta.

## Modello di maturità

- **Livello 1, Avvio:** Rilasci manuali, poco frequenti e ad alta cerimonia; test per lo più manuali ed eseguiti a mano; successo misurato come "è stato rilasciato"; i rollback sono dolorosi e improvvisati; nessuna idea condivisa di come dovrebbe funzionare la consegna.
- **Livello 2, Sviluppo:** Alcuni team mettono in piedi la CI con build automatiche e pochi test; i rilasci sono pianificati; esiste un monitoraggio di base; le pratiche variano da team a team e le metriche DORA non sono ancora seguite, quindi la consegna è migliore a macchia ma incoerente nell'organizzazione.
- **Livello 3, Standardizzazione:** Una pipeline documentata a strada asfaltata è imposta in tutta l'organizzazione: consegna continua con cancelli automatici di test e sicurezza, distribuzione progressiva con rollback e separazione dei compiti fatta rispettare come politica come codice. La pipeline fornisce una traccia di audit immutabile e ogni team segue lo stesso percorso versionato anziché uno su misura.
- **Livello 4, Gestione:** La pipeline è misurata e controllata rispetto a valori di riferimento. Le quattro metriche DORA (frequenza di distribuzione, tempo di attesa, tasso di fallimento delle modifiche, tempo di ripristino), il raggiungimento degli SLO, il consumo del budget di errore e le metriche di flusso come tempo di ciclo e lavoro in corso sono seguiti rispetto a obiettivi e cancelli e rollback scattano su soglie misurate anziché sul giudizio. Il debito dei flag, i tassi di test instabili e le regressioni del tempo di attesa sono monitorati e ogni decisione di procedere o fermarsi è presa sull'evidenza.
- **Livello 5, Orchestrazione:** La consegna è continuamente migliorata e integrata con scoperta e pianificazione dei rischi. La distribuzione continua gira dove appropriato con consegna progressiva e rollback automatico; le funzionalità sono rilasciate come esperimenti misurati le cui metriche di esito ritornano al giro successivo di scommesse; le prestazioni DORA d'élite sono sostenute tra i team grazie alla strada asfaltata; e l'organizzazione riaggiusta in modo adattivo cancelli, soglie e capacità man mano che si spostano carico, rischio e mix di prodotto.

## Spunti di discussione

1. Quali sono le vostre attuali quattro metriche DORA e dove sta il maggior collo di bottiglia nel vostro flusso dal commit alla produzione?
2. Potete separare oggi distribuzione e rilascio? Se no, che cosa cambierebbero i feature flag del vostro rischio?
3. Quanto dura la vostra suite di test e gli sviluppatori si fidano abbastanza da non aggirarla?
4. Quando avete rilasciato la vostra ultima funzionalità, avete misurato se ha mosso la metrica che doveva muovere?
5. In un contesto regolato, il vostro processo di controllo delle modifiche rallenta la consegna *oppure* è fatto rispettare automaticamente dalla pipeline?
6. Quali feature flag del vostro codice avrebbero dovuto essere rimossi mesi fa?

## Punti chiave

- La pipeline di consegna trasforma le idee convalidate in software funzionante e misurato e riporta gli esiti alla scoperta (capitolo 11.1).
- Automatizza l'intero percorso: **cancelli di test** rapidi, **CI/CD** e **infrastruttura come codice**, con la pipeline come fonte di verità.
- **Separa distribuzione e rilascio** e usa strategie progressive (flag, canary, blue-green) con rollback automatico.
- Misura a tre livelli: metriche **DORA/di flusso**, **affidabilità/SLO** ed **esiti per business/utenti**.
- Velocità e stabilità sono **complementi**, non compromessi: le pratiche che danno l'una danno l'altra.
- La pipeline è anche un **controllo di conformità**: l'automazione produce una traccia di audit immutabile e continua.
- Il ROI è rapido, ben documentato (DORA) e composto; il costo principale del non investire è pagato di continuo.

## Riferimenti e letture di approfondimento

- *Accelerate: The Science of Lean Software and DevOps*, di Nicole Forsgren, Jez Humble, Gene Kim (le metriche DORA e l'evidenza).
- *Continuous Delivery*, di Jez Humble e David Farley (il testo fondativo).
- *The DevOps Handbook*, di Kim, Humble, Debois, Willis.
- *The Phoenix Project*, di Gene Kim, Kevin Behr, George Spafford (narrazione sul flusso).
- *Site Reliability Engineering*, a cura di Beyer, Jones, Petoff, Murphy (SLI/SLO, budget di errore).
- *Team Topologies*, di Matthew Skelton e Manuel Pais (strade asfaltate e progettazione dei team di consegna).
- *Feature Flags / progressive delivery*, scritti di Pete Hodgson e delle comunità LaunchDarkly/Split.
- Google DORA, rapporti *Accelerate State of DevOps* (annuali).
- Kim, Gene, *The Unicorn Project* (visione del flusso dal lato dell'esperienza dello sviluppatore).
- Reinertsen, Donald, *The Principles of Product Development Flow* (dimensione dei lotti, code, economia del flusso).
