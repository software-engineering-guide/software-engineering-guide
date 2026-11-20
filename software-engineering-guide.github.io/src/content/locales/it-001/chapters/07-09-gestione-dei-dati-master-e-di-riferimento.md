# 7.9 Gestione dei dati master e di riferimento

## Panoramica e motivazioni

Chiedi a cinque sistemi quanti clienti ha l'organizzazione e ottieni cinque numeri diversi. Uno conta gli indirizzi email, uno conta i contratti, uno conta gli accessi e due non sono d'accordo sul fatto che "Acme Corp" e "ACME Corporation" siano la stessa azienda. La [gestione dei dati master](https://en.wikipedia.org/wiki/Master_data_management) (MDM) è la disciplina di riconciliare le entità centrali che il tuo business condivide, cliente, prodotto, fornitore, dipendente, sede, in un'unica versione autorevole di cui ogni sistema possa fidarsi.

Comincia ordinando i tuoi dati in tre tipi, perché richiedono trattamenti diversi. I dati master descrivono i nomi del tuo business: le persone, i luoghi e le cose a cui molti processi fanno riferimento. I dati di riferimento sono il vocabolario controllato che quei processi usano: codici di valuta, codici di paese, elenchi di unità di misura, categorie di prodotto. I dati transazionali registrano i verbi: un ordine effettuato, un pagamento eseguito, una spedizione inviata. I dati master e di riferimento hanno un volume minore delle transazioni ma sono richiamati ovunque, quindi un errore in essi contamina tutto ciò che sta a valle.

Il costo di sbagliare è concreto. Quando lo stesso cliente esiste come quattro record leggermente diversi, spedisci quattro cataloghi, non riesci a vedere una relazione che varrebbe la pena tenere e il tuo numero di ricavi per cliente è in silenzio sbagliato. Un [record d'oro](https://en.wikipedia.org/wiki/Single_source_of_truth), l'unica versione affidabile di un'entità assemblata da molte fonti, è ciò che sostituisce quelle copie in conflitto, così che ogni integrazione smetta di risolvere di nuovo lo stesso problema di corrispondenza.

Per le imprese che riconciliano sistemi accumulati in decenni di crescita e acquisizioni, l'MDM è la differenza tra una vista coerente del cliente e una permanente tassa di riconciliazione. Per gli enti pubblici la posta sale: un cittadino che compare come tre persone diverse in tre enti può vedersi negare una prestazione, essere tassato due volte o perdersi tra i dipartimenti. Questo capitolo completa strategia e governance dei dati (capitolo 7.1), che fissa proprietà e politica; modellazione dei dati e strato semantico (capitolo 7.7), che definisce che cosa significano le entità; e qualità e osservabilità dei dati (capitolo 7.8), che mantiene puliti i record nel tempo.

## Principi chiave

- Ordina i tuoi dati in master, di riferimento e transazionali; ciascuno richiede un trattamento diverso.
- Un record d'oro per entità del mondo reale, assemblato deliberatamente, non scoperto per caso.
- Scegli uno stile architetturale di MDM adatto alle tue esigenze di controllo e latenza, non alla moda.
- Corrispondenza e sopravvivenza sono regole di business, quindi mettile per iscritto e lascia che gli steward le regolino.
- I dati di riferimento sono un vocabolario condiviso; versionali e pubblicali come un'API.
- Governance e stewardship sono il motore dell'MDM; il software è solo lo strumento.
- Propaga i record d'oro come eventi così che i sistemi a valle restino sincronizzati, non stantii.
- Misura l'MDM dalle decisioni migliorate e dai duplicati rimossi, non dai record caricati.

## Raccomandazioni

### Classifica prima i dati master, di riferimento e transazionali

Non puoi gestire ciò che non hai ordinato, quindi comincia classificando i tuoi domini di dati. Un test utile per i dati master è se un valore sbagliato si propaga: se un solo indirizzo cattivo si ripercuote su fatturazione, spedizione e notifiche legali, hai a che fare con dati master. Questo guida il tuo investimento: costruisci un motore di corrispondenza per l'entità cliente, non per le righe d'ordine. Nomina i domini esplicitamente, classificali per quanto dolore causa la loro duplicazione e parti da uno o due che fanno più male, di solito cliente e prodotto perché toccano direttamente i ricavi.

### Scegli deliberatamente uno stile architetturale di MDM

Ci sono quattro stili architetturali comuni e quello giusto dipende da quanta autorità puoi centralizzare e da quanto in fretta le modifiche devono propagarsi. Lo stile registro lascia i dati nei sistemi sorgente e costruisce solo un indice di identificativi corrispondenti, così può rispondere "questi cinque record sono lo stesso cliente" senza spostare alcun dato; è economico e a basso rischio, ma di sola lettura, quindi non può correggere le sorgenti. Lo stile consolidamento porta copie in un hub centrale e le fonde in record d'oro per la reportistica, ma non rimanda le correzioni indietro, quindi le sorgenti restano disordinate. Lo stile coesistenza va oltre: sincronizza i valori ripuliti verso i sistemi sorgente, così le sorgenti migliorano nel tempo continuando a operare in modo indipendente. Lo stile hub centralizzato o transazionale fa dell'hub MDM stesso il sistema di registrazione, dove le entità sono create e modificate direttamente e ogni altro sistema consuma da esso; dà la massima coerenza e controllo ed è il più difficile da adottare perché cambia dove avviene il lavoro. Molte organizzazioni progrediscono da un registro che prova il valore verso la coesistenza man mano che cresce la fiducia e gestiscono più di uno stile su domini diversi.

### Stabilisci esplicitamente corrispondenza, fusione e regole di sopravvivenza

Il cuore dell'MDM è decidere quando due record descrivono la stessa cosa del mondo reale. È il [collegamento di record](https://en.wikipedia.org/wiki/Record_linkage), raramente semplice come una corrispondenza esatta di chiave perché i dati veri sono pieni di refusi, abbreviazioni e campi mancanti. La corrispondenza deterministica usa regole esatte su campi scelti (stessa partita IVA, o stessa email più codice postale). La corrispondenza probabilistica assegna un punteggio di somiglianza su molti campi usando la [corrispondenza approssimata di stringhe](https://en.wikipedia.org/wiki/Approximate_string_matching) e pesi, così "Bob Smith, 12 Main St" e "Robert Smith, 12 Main Street" possono essere giudicati una probabile corrispondenza sopra una soglia. Decidere quali record si riferiscono alla stessa entità si chiama risoluzione dell'identità e alimenta tutto, dalle viste del cliente al rilevamento delle frodi.

Una volta che i record corrispondono, devi decidere quali valori sopravvivono nel record d'oro. Queste regole di sopravvivenza sono logica di business, quindi rendile esplicite: preferisci il valore più recente per un numero di telefono, il valore più completo per un indirizzo, la fonte più affidabile per una ragione sociale. Fissa una fascia di soglia in cui le corrispondenze sono fuse automaticamente, una fascia inferiore in cui sono rifiutate automaticamente e una fascia intermedia in cui decide una persona, ed è qui che vive la stewardship. Mantieni ogni fusione reversibile e registrata, perché una fusione sbagliata che unisce due clienti reali è peggio di una mancata.

### Tratta i dati di riferimento come vocabolario condiviso versionato

I dati di riferimento sono il vocabolario condiviso che parlano i tuoi sistemi e un vocabolario che deriva causa disallineamenti silenziosi: quando un sistema usa il codice di paese ISO "GB" e un altro "UK", i join falliscono e i conteggi divergono. Mantieni ogni elenco di riferimento in un unico posto governato, pubblicalo per ogni consumatore e, cosa cruciale, versionalo. I codici vengono aggiunti, ritirati, divisi e fusi nel tempo e se sovrascrivi l'elenco sul posto, rompi i report storici che erano corretti con i vecchi codici.

Tratta un insieme di dati di riferimento come un'API con un contratto. Pubblicalo con date di efficacia così che un consumatore possa chiedere "quali erano i codici di regione validi in questa data", conserva i codici ritirati anziché cancellarli e registra la mappatura quando un codice cambia significato. Preferisci standard esterni riconosciuti dove esistono, come i codici ISO di paese e valuta, perché gli standard ti danno interoperabilità gratis e si collegano alla disciplina degli standard aperti nel capitolo 3.8.

### Modella gerarchie e relazioni, non solo record piatti

I dati master non sono un mucchio di righe indipendenti; sono una rete di relazioni. Un cliente appartiene a un nucleo familiare e a una capogruppo aziendale. Un prodotto confluisce in una categoria e in una marca. Queste gerarchie portano un vero significato di business: aggrega le vendite per capogruppo aziendale e il quadro cambia completamente rispetto all'aggregare per singolo conto. Modella esplicitamente queste relazioni così che i consumatori le percorrano in modo coerente anziché ogni team inventare la propria aggregazione.

Fai attenzione al caso in cui una sola entità ha bisogno di più gerarchie contemporaneamente. Un prodotto può confluire in un modo per la finanza e in un altro per il merchandising ed entrambi sono legittimi, quindi supporta più gerarchie nominate anziché forzare un unico vero albero. Contano anche le relazioni tra domini, come quale fornitore fornisce quale prodotto.

### Collega i record d'oro allo strato semantico e alla qualità dei dati

I record d'oro che l'MDM produce sono le entità affidabili a cui lo strato semantico del capitolo 7.7 fa riferimento quando definisce le metriche: "clienti attivi" significa qualcosa solo quando "cliente" è privo di ambiguità. Alimenta i tuoi record d'oro nello strato semantico così che ogni metrica conti le stesse entità deduplicate e risolte.

MDM e qualità dei dati (capitolo 7.8) sono due facce della stessa medaglia: i controlli di qualità rilevano i duplicati, i nulli e le violazioni di formato che l'MDM poi risolve e la corrispondenza dell'MDM fa emergere problemi di qualità che i controlli avevano perso. Esegui un monitoraggio continuo della qualità specificamente sui tuoi dati master: tassi di duplicati, distribuzioni di confidenza delle corrispondenze, completezza dei campi chiave e dimensione della coda di revisione, così che la deriva emerga prima che i consumatori la vedano.

### Propaga i record d'oro attraverso gli eventi

Un record d'oro che nessun sistema a valle vede non aiuta nessuno. Lo schema più forte è la propagazione guidata dagli eventi: quando un'entità è creata, fusa o corretta, l'hub MDM pubblica un evento di modifica e i sistemi sottoscritti aggiornano la propria copia locale. Si basa sull'[architettura a eventi](https://en.wikipedia.org/wiki/Event-driven_architecture) e sugli schemi di streaming del capitolo 7.2, mantenendo coerenti decine di sistemi senza fragili sincronizzazioni batch notturne che lasciano tutti un giorno indietro.

Pubblica gli eventi con abbastanza contesto da essere utili: l'identificativo dell'entità, che cosa è cambiato, i nuovi valori sopravvissuti e una versione così che i consumatori possano ordinare gli aggiornamenti e rilevare quelli che hanno perso. Rendi idempotenti i consumatori così che rieseguire un evento non faccia danni e offri un'API per i sistemi che non possono sottoscrivere. Vale il principio di architettura e archiviazione dei dati (capitolo 3.4): progetta perché il record d'oro fluisca, perché uno che nessuno consuma è solo un costoso foglio di calcolo.

### Assegna stewardship e governance prima degli strumenti

L'MDM fallisce come progetto tecnologico e riesce come progetto di governance. Il ruolo critico è lo [steward dei dati](https://en.wikipedia.org/wiki/Data_steward), una persona responsabile della qualità e delle regole di un dominio specifico, che risolve le corrispondenze ambigue, regola le regole di sopravvivenza e arbitra quando due dipartimenti non concordano su che cosa significhi "fornitore". Gli steward sono di solito persone di business con profonda conoscenza del dominio, non ingegneri e hanno bisogno di vera autorità e di tempo assegnato, perché una stewardship a tempo parziale senza mandato produce esattamente la deriva che l'MDM doveva fermare.

Avvolgi gli steward nelle strutture di governance del capitolo 7.1: un proprietario dei dati responsabile di ogni dominio, un consiglio per comporre le dispute tra domini e chiare politiche su chi può creare o fondere record master. Documenta le decisioni, perché le regole per far corrispondere un cliente sono conoscenza istituzionale che deve sopravvivere al ricambio del personale. Gli strumenti servono la governance; comprare una piattaforma MDM prima di nominare i tuoi steward è comprare un motore senza conducente.

## Compromessi: vantaggi e svantaggi

| Stile MDM | Vantaggi | Svantaggi |
|---|---|---|
| Registro (solo indice) | Economico, a basso rischio, sorgenti intatte | Sola lettura; non può correggere i dati sorgente |
| Consolidamento (copie centrali) | Record puliti per l'analisi in fretta | Le sorgenti restano disordinate; nessuna riscrittura |
| Coesistenza (sincronizza verso le sorgenti) | Le sorgenti migliorano; controllo bilanciato | Più integrazione; conflitti di sincronizzazione da gestire |
| Hub centralizzato / transazionale | Massima coerenza e controllo | Costo più alto; cambia dove avviene il lavoro |
| Corrispondenza deterministica | Prevedibile, spiegabile, verificabile | Perde refusi, varianti e dati disordinati |
| Corrispondenza probabilistica | Coglie la variazione del mondo reale | Richiede regolazione; fusioni sbagliate se trascurata |

La tensione centrale nell'MDM è controllo contro disturbo. Gli stili che ti danno i dati più puliti e coerenti (coesistenza e hub centralizzati) sono esattamente quelli che invadono di più il modo di lavorare dei sistemi sorgente e dei loro responsabili e quell'invasione è dove i programmi MDM si bloccano. Il percorso pragmatico è guadagnare fiducia con uno stile a basso rischio e spostarsi verso un controllo più forte solo dove il business case è chiaro. Il compromesso sulla corrispondenza corre in parallelo: le regole deterministiche sono verificabili ma fragili, il punteggio probabilistico è potente ma richiede stewardship e una tolleranza per l'occasionale fusione sbagliata. La maggior parte dei programmi maturi mescola entrambi.

## Domande da discutere con il tuo team

1. **Quali domini di dati master ci causano davvero dolore, e li abbiamo classificati per costo anziché trattarli tutti insieme?** Molti programmi MDM crollano sotto la loro stessa ambizione, cercando di governare ogni entità dell'impresa in una volta e non consegnando nulla per due anni. La mossa produttiva è trovare uno o due domini in cui duplicazione e conflitto ti costano denaro o fiducia reali, di solito cliente o prodotto, e quantificare quel costo: le spedizioni sprecate, le ore di riconciliazione, i numeri di ricavi sbagliati, i rilievi di audit. Porta esempi concreti della stessa entità che compare in più modi nei tuoi sistemi e lascia che quella classifica ti dica da dove partire, perché una vittoria ristretta e misurabile costruisce la credibilità che ti serve per espandere.

2. **Chi possiede ogni dominio di dati master, e i nostri steward hanno l'autorità e il tempo per fare davvero il lavoro?** Gli strumenti MDM senza una stewardship dotata di potere sono un'auto senza conducente e la modalità di fallimento più comune è nominare uno steward su una slide dandogli nessun vero mandato e nessuna ora assegnata. Le persone che risolvono le corrispondenze ambigue e compongono le dispute su "che cosa conta come cliente" hanno bisogno di competenza di dominio, autorità decisionale e tempo protetto. Porta il tuo organigramma e chiedi, per il tuo dominio principale, esattamente chi decide quando due record sono la stessa persona e chi arbitra quando vendite e finanza non concordano. Se non sai nominare quella persona e indicarne il tempo assegnato, hai trovato il divario che affonderà il programma.

3. **Quando fondiamo due record in un record d'oro, possiamo spiegare e invertire la decisione, e da dove vengono i valori sopravvissuti?** Le regole di sopravvivenza sono logica di business che la maggior parte dei team non ha mai messo per iscritto, il che significa che le fusioni avvengono per caso dell'ordine di caricamento o dei predefiniti dello strumento e una fusione sbagliata che unisce due clienti reali è dolorosa da disfare. Porta un vero record fuso e ricostruisci ogni campo sopravvissuto fino alla sua fonte e regola: perché questo indirizzo, perché questo nome, perché questo numero di telefono. Conferma che ogni fusione sia registrata e reversibile e che una fascia intermedia di corrispondenze incerte vada a una persona anziché essere fusa automaticamente. Se non sai spiegare un record d'oro specifico, i tuoi steward non possono difenderlo davanti a un auditor o a un cliente leso.

4. **Quale stile architetturale di MDM si adatta a ciascun dominio che pianifichiamo di governare, e possiamo difendere quella scelta contro il disturbo che impone ai responsabili dei sistemi sorgente?** Lo stile che scegli decide quanto puoi ripulire i dati e quanto invadi i team che possiedono le sorgenti e scegliere per moda o per proposta di un fornitore anziché per la realtà di controllo contro disturbo è come i programmi si bloccano a metà strada. Un registro prova il valore a basso costo ma non corregge mai una sorgente; un hub centralizzato dà la massima coerenza ma sposta dove i record sono creati, il che è un cambiamento organizzativo travestito da tecnico. Porta, per ogni dominio candidato, una lettura onesta di quanta autorità detieni davvero sui responsabili delle sorgenti, quanto devono essere fresche le copie a valle e che cosa una riscrittura romperebbe nei flussi di lavoro esistenti. Nei contesti aziendali e governativi, aggiungi il costo di migrazione e gestione del cambiamento dello spostare il sistema di registrazione, perché i team il cui lavoro quotidiano si sposta resisteranno a un hub su cui non sono stati consultati e un'adozione della coesistenza arenata costa più di un modesto registro che va in produzione.

5. **Come regoliamo le soglie di corrispondenza, e abbiamo concordato quale tasso di fusioni sbagliate e di corrispondenze perse possiamo tollerare in ciascun dominio?** Ogni motore di corrispondenza probabilistica scambia fusioni sbagliate (unire due entità reali) contro corrispondenze perse (lasciare un'entità divisa) e l'equilibrio è una decisione di business, non un predefinito che qualcuno ha lasciato nello strumento. Se fissi le fasce di fusione automatica e rifiuto automatico troppo larghe corrompi in silenzio i record d'oro; se le fissi troppo strette la coda di revisione umana cresce più in fretta di quanto gli steward riescano a smaltirla. Porta la distribuzione di confidenza attuale, la dimensione e l'età della coda di revisione ed esempi di errori di entrambi i tipi così che la stanza veda il costo reale di ciascuna direzione. In un dominio di identità governativo, propendi decisamente verso le corrispondenze perse e la revisione umana, perché una fusione sbagliata può negare una prestazione o esporre i dati di un cittadino a un altro e il costo di ricorso e audit di quell'errore fa impallidire il costo di un duplicato che uno steward risolve la settimana dopo.

6. **Come vengono a sapere i sistemi a valle che un record d'oro è cambiato, e quanto può essere stantio ciascuno prima che una decisione vada storta?** Un record d'oro perfettamente risolto che nessun sistema consuma è un costoso foglio di calcolo e il meccanismo di propagazione, che sia eventi di modifica, un'API di sottoscrizione o un batch notturno, fissa in silenzio quanto sia aggiornata ogni decisione dipendente. La propagazione guidata dagli eventi mantiene decine di consumatori quasi in tempo reale ma richiede consumatori idempotenti ed eventi versionati; una sincronizzazione notturna è più semplice ma lascia tutti un giorno indietro, il che può andare bene per una lista di marketing ed essere pericoloso per un controllo antifrode. Porta l'elenco dei sistemi consumatori, la freschezza di cui ciascuno ha davvero bisogno e come un consumatore che oggi perde un aggiornamento si riprende. Per un'organizzazione grande o pubblica, nomina chi possiede il contratto di questi eventi e come un sottoscrittore rileva un messaggio perso, perché una modifica di entità che non riesce in silenzio a raggiungere un ente ricrea esattamente la frammentazione che l'MDM era stato finanziato per rimuovere.

## Lente settoriale

**Startup.** Con una manciata di ingegneri e nessun margine da sprecare, non comprare una piattaforma MDM. Governa l'unica entità che sta corrompendo i tuoi numeri, di solito il cliente duplicato tra self-service e vendite, con un job di corrispondenza nel warehouse che già gestisci e una persona che rivede ogni settimana le corrispondenze incerte. Mantieni ogni fusione registrata e reversibile così che una regola sbagliata costi un pomeriggio, non una relazione con un cliente e rivedi strumenti più pesanti solo quando la coda di revisione manuale supera un singolo revisore.

**Piccola impresa.** Non hai uno steward dei dati e hai un budget stretto, quindi tratta questo come una decisione di comprare e non costruire e appoggiati agli standard che ottieni gratis. Privilegia strumenti che già deduplicano i contatti e parlano i codici ISO di paese e valuta anziché un hub su misura che non puoi mantenere e scegli l'unico dominio, tipicamente clienti o prodotti, in cui i duplicati ti costano denaro vero. Assegna la responsabilità a un responsabile nominato anche se è una frazione della settimana di una persona, perché un vocabolario che deriva senza nessuno che guardi è ciò che rompe in silenzio i tuoi report.

**Grande impresa.** Su una dozzina di sistemi ERP e CRM accumulati per acquisizione, il lavoro è governance di portafoglio: classifica i domini per costo della loro duplicazione, metti in piedi steward dotati di potere nel business e standardizza regole di sopravvivenza e versionamento dei dati di riferimento così che i gruppi smettano di risolvere di nuovo lo stesso problema di corrispondenza. Metti a bilancio esplicitamente il costo di integrazione e di stewardship permanente, propaga i record d'oro come eventi versionati così che le sorgenti migliorino nel tempo e gestisci l'MDM come un programma misurato con tassi di duplicati e metriche della coda di revisione anziché una pulizia una tantum.

**Ente pubblico.** Regole di appalto, rigorose leggi sulla condivisione dei dati e responsabilità pubblica plasmano ogni scelta. Fai della persona un'entità con chiave su un identificativo nazionale governato, versiona i dati di riferimento per data di efficacia così che i record storici restino corretti e rendi la risoluzione dell'identità deliberatamente prudente: le corrispondenze incerte vanno a steward formati, mai a fusioni automatiche, perché una fusione sbagliata può negare una prestazione o far trapelare i dati di un cittadino a un altro. Registra ogni corrispondenza per audit e ricorso, esigi portabilità dei dati e una logica di corrispondenza dichiarata dai fornitori e mantieni l'intera capacità dentro gli standard di interoperabilità a cui il settore pubblico si è già impegnato.

## Esempi

**Startup.** Un'azienda software in rapida crescita vende sia con iscrizione self-service sia con un team di vendita e i due canali creano lo stesso cliente due volte con nomi aziendali leggermente diversi. I ricavi per conto sembrano sbagliati e il team di vendita continua a chiamare a freddo utenti esistenti. Anziché comprare una piattaforma pesante, parte da un registro leggero: un job di corrispondenza nel data warehouse che collega i record per dominio email e nome aziendale normalizzato, con uno steward a tempo parziale che rivede ogni settimana le corrispondenze incerte. Costa poco, corregge l'errore di reportistica e prova il valore che giustifica più investimento man mano che crescono.

**Grande impresa.** Un produttore globale è cresciuto per acquisizione e gestisce una dozzina di sistemi ERP e CRM, ciascuno con i propri record di fornitori, così lo stesso fornitore compare in quindici modi e l'azienda non può negoziare come un unico acquirente né vedere la sua vera spesa. Mette in piedi un hub MDM in stile coesistenza per i domini fornitore e prodotto, usando una corrispondenza deterministica su identificativi fiscali e di registrazione più un punteggio probabilistico su nomi e indirizzi. Steward nominati negli acquisti regolano le regole di sopravvivenza e smaltiscono la coda di revisione e i record d'oro sono pubblicati come eventi di modifica che rifluiscono in ogni ERP così che i dati ripuliti migliorino le sorgenti. La visibilità consolidata della spesa sblocca condizioni contrattuali migliori e la tassa di riconciliazione che consumava la finanza ogni trimestre cala nettamente.

**Ente pubblico.** Un governo nazionale vuole che gli enti trattino un cittadino come una sola persona anziché uno sconosciuto a ogni sportello, rispettando al contempo rigorosi limiti legali sulla condivisione dei dati. Costruisce un hub di dati master centralizzato per l'entità persona, con chiave su un identificativo nazionale governato, con dati di riferimento versionati per data di efficacia così che i record storici restino corretti. La risoluzione dell'identità è deliberatamente prudente: le corrispondenze incerte vanno a steward formati anziché a fusioni automatiche, perché una fusione sbagliata potrebbe negare a qualcuno una prestazione o esporne i dati e ogni corrispondenza è registrata per audit e ricorso. Il guadagno è meno record duplicati, meno frodi da identità divise e un cittadino che non deve provare chi è a ogni porta, dentro gli standard di interoperabilità del capitolo 3.8.

## Business case: motivazioni, ROI e TCO

Il ritorno dell'MDM viene dal rimuovere una tassa che la maggior parte delle organizzazioni paga senza nominarla. Record duplicati e in conflitto costano denaro in modi evidenti (marketing sprecato verso la stessa persona cinque volte, errori di spedizione da indirizzi stantii, sconti di volume perduti) e in modi meno evidenti (analisti che riconciliano i conteggi, dirigenti che decidono su numeri in silenzio sbagliati, auditor che fatturano ore per districare quale record sia vero). Una vista consolidata dei fornitori spesso ripaga da sola l'intero programma attraverso migliori condizioni contrattuali.

Il costo totale di proprietà ha tre parti: la piattaforma o la costruzione, l'integrazione con sorgenti e consumatori e, la più grande nel tempo, la stewardship continua. Il costo di integrazione è facile da sottovalutare, perché collegare una dozzina di vecchi sistemi sorgente è dove i programmi MDM perdono tempi e budget e il costo di stewardship è facile da dimenticare, perché è una spesa operativa permanente, non una costruzione una tantum. Per presentare il caso alla leadership, lega l'MDM a numeri che già seguono: accuratezza dei ricavi, efficienza del marketing, risparmi sugli acquisti, costo degli audit e rischio normativo, poi parti in piccolo e lascia che una vittoria misurata su un dominio ad alto dolore finanzi l'espansione.

## Antipattern e insidie

- **Ambito da far bollire l'oceano:** governare ogni dominio in una volta, non consegnare nulla per anni e perdere lo sponsor prima della prima vittoria.
- **Strumenti prima della governance:** comprare una piattaforma MDM prima di nominare steward e responsabili, così il motore non ha conducente.
- **Steward a tempo parziale senza autorità:** assegnare la stewardship su una slide senza dare un vero mandato né tempo protetto.
- **Sopravvivenza silenziosa:** fondere i record per predefinito dello strumento o ordine di caricamento, senza regole scritte e senza modo di spiegare un record d'oro.
- **Fusioni irreversibili:** fondere automaticamente le corrispondenze incerte senza annullamento, così che una fusione sbagliata di due entità reali diventi un danno permanente.
- **Dati di riferimento sovrascritti sul posto:** modificare gli elenchi di codici senza versionamento, rompendo ogni report storico che era corretto con i vecchi codici.
- **Record d'oro che nessuno consuma:** costruire un hub immacolato a cui nessun sistema a valle si sottoscrive, così che i dati puliti non raggiungano mai le decisioni.
- **Reinventare i codici standard:** coniare i propri elenchi di paesi o valute quando esistono gli standard ISO, perdendo interoperabilità senza motivo.

## Modello di maturità

- **Livello 1, Avvio:** I dati master e di riferimento non sono gestiti. La stessa entità esiste molte volte senza una versione autorevole, gli elenchi di codici divergono, la corrispondenza è manuale e reattiva e nessuno possiede il problema, così i conteggi delle entità centrali non concordano e nessuno sa dire quale sia giusto.
- **Livello 2, Sviluppo:** I domini chiave sono riconosciuti e qualcuno li deduplica, spesso nel warehouse per la reportistica. Esiste una corrispondenza deterministica di base, gli elenchi di riferimento sono raccolti e alcune persone fungono da steward informali, ma la pratica varia da team a team, le sorgenti restano disordinate e le regole vivono nella testa delle persone anziché sulla carta.
- **Livello 3, Standardizzazione:** L'MDM è un programma governato applicato in modo coerente nell'organizzazione. I domini master hanno responsabili nominati e steward dotati di potere, le regole di corrispondenza e sopravvivenza sono documentate e fatte rispettare, i record d'oro sono prodotti e propagati ai consumatori e i dati di riferimento sono versionati e pubblicati con date di efficacia come un'API.
- **Livello 4, Gestione:** Il programma è misurato e controllato rispetto a valori di riferimento. Tassi di duplicati, distribuzioni di confidenza delle corrispondenze, tassi di fusioni sbagliate e corrispondenze perse, completezza dei campi chiave e dimensione ed età della coda di revisione sono seguiti come metriche; le soglie sono regolate su quei numeri anziché a sensazione; e il valore dell'MDM (accuratezza dei ricavi, risparmi sugli acquisti, costo di revisione) è quantificato e riportato ai responsabili con una cadenza fissa.
- **Livello 5, Orchestrazione:** I record d'oro fluiscono come eventi versionati quasi in tempo reale, alimentano lo strato semantico e sono affidabili in tutta l'organizzazione. La corrispondenza è continuamente migliorata rispetto agli esiti misurati, la gestione si estende a nuovi domini come capacità ripetibile e l'MDM è integrato con la governance e la pianificazione del rischio così che il programma si adatti al mutare di sorgenti, standard e panorama delle entità.

## Spunti di discussione

1. Se due dei vostri sistemi non concordano su quanti clienti avete, quale è giusto e come lo provereste?
2. Quale dominio di dati master darebbe la vittoria misurabile maggiore se lo governaste per primo, e quanto vale quella vittoria?
3. Dove la corrispondenza probabilistica vi aiuterebbe oggi, e siete a vostro agio con l'occasionale fusione sbagliata che implica?
4. Come versionate i vostri dati di riferimento, e che cosa si rompe nei vostri report storici quando un codice cambia significato?
5. Chi è lo steward nominato per la vostra entità più importante, e ha l'autorità e il tempo per fare davvero il lavoro?
6. Quando un record d'oro cambia, come lo scoprono i vostri sistemi a valle, e quanto possono essere stantii prima che faccia male?

## Punti chiave

- Ordina i tuoi dati in master, di riferimento e transazionali; investi corrispondenza e governance dove la duplicazione costa di più.
- Produci un record d'oro per entità del mondo reale, assemblato da regole di sopravvivenza esplicite, reversibili e registrate.
- Scegli uno stile architetturale di MDM (registro, consolidamento, coesistenza o hub centralizzato) adatto al tuo appetito per controllo e disturbo.
- Tratta i dati di riferimento come vocabolario condiviso versionato, preferisci standard riconosciuti e non sovrascrivere mai sul posto gli elenchi di codici.
- L'MDM riesce grazie a governance e stewardship, non agli strumenti; propaga i record d'oro come eventi e misura il programma dalle decisioni migliorate.

## Riferimenti e letture di approfondimento

- David Loshin, *Master Data Management*
- Alex Berson e Larry Dubov, *Master Data Management and Data Governance*
- Dan Power, *The Definitive Guide to Master Data Management*
- John Talburt, *Entity Resolution and Information Quality*
- Peter Christen, *Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection*
- Ivan P. Fellegi e Alan B. Sunter, "A Theory for Record Linkage," *Journal of the American Statistical Association*
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*
- Ralph Kimball e Margy Ross, *The Data Warehouse Toolkit*
