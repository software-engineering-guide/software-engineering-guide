# 5.7 Sviluppo di applicazioni mobili

## Panoramica e motivazioni

Lo [sviluppo di applicazioni mobili](https://en.wikipedia.org/wiki/Mobile_app_development) è la disciplina di costruire software per telefoni e tablet. Per molte persone, un telefono è ormai il computer principale o l'unico che possiedono. Questo fa dell'app mobile la porta d'ingresso al tuo servizio e spesso la superficie su cui gli utenti giudicano l'intera organizzazione.

Il mobile è un ambiente ingegneristico distinto, non una piccola versione del web o del desktop. Il dispositivo gira in una tasca, a batteria, su connessioni che vanno e vengono. Gli schermi sono piccoli. Il sistema operativo controlla che cosa la tua app può fare. Esistono due piattaforme dominanti ([iOS](https://en.wikipedia.org/wiki/IOS) di Apple e [Android](https://en.wikipedia.org/wiki/Android_%28operating_system%29) di Google), ciascuna con propri linguaggi, regole di design e store. Non puoi semplicemente rilasciare un aggiornamento quando ti pare, perché uno store lo rivede prima e gli utenti scelgono quando installarlo. Questo capitolo si basa sull'ingegneria frontend (capitolo 5.6), sui fondamenti di UX (capitolo 5.1) e sull'accessibilità (capitolo 5.3) e si appoggia alla sicurezza delle applicazioni (capitolo 4.2) e a CI/CD e consegna (capitolo 8.1).

La rilevanza per imprese ed enti pubblici è alta. Le imprese rilasciano app per i clienti e app interne per la propria forza lavoro, spesso gestite attraverso la [gestione dei dispositivi mobili](https://en.wikipedia.org/wiki/Mobile_device_management) (MDM: software centrale che configura e protegge i dispositivi aziendali). Gli enti pubblici costruiscono app rivolte ai cittadini per prestazioni, sanità, identità e pagamenti e devono servire tutti, comprese le persone con dispositivi vecchi e connessioni lente, sotto leggi sull'accessibilità. In entrambi i contesti, il mobile è un impegno serio e di lunga durata, quindi trattalo con lo stesso rigore che dai a qualsiasi altro sistema di produzione.

## Principi chiave

- Progetta per il dispositivo: schermo piccolo, batteria e una rete che va e viene.
- Presumi connettività intermittente; lavora prima offline e sincronizza quando puoi.
- Rispetta le convenzioni di design e di interazione di ciascuna piattaforma.
- Non controlli i tempi di rilascio; li controllano lo store e l'utente.
- La frammentazione è normale; supporta una gamma reale di dispositivi e versioni del sistema operativo.
- Memorizza i dati in modo sicuro sul dispositivo, perché i dispositivi si perdono e vengono rubati.
- L'accessibilità è un requisito, non una rifinitura.
- Scegli il tuo approccio di costruzione per l'intera vita dell'app, non solo per il giorno del lancio.

## Raccomandazioni

### Scegli deliberatamente l'approccio di costruzione

Ci sono tre approcci generali e ciascuno si adatta a bisogni diversi.

Lo [sviluppo nativo](https://en.wikipedia.org/wiki/Mobile_app_development) significa scrivere separatamente per ogni piattaforma usando i suoi strumenti: Swift per iOS, Kotlin per Android. Ottieni le migliori prestazioni, il più pieno accesso alle funzioni del dispositivo e la sensazione di piattaforma più fedele, al costo di costruire e mantenere due basi di codice.

I [framework multipiattaforma](https://en.wikipedia.org/wiki/Cross-platform_software) permettono a una sola base di codice di puntare a entrambe le piattaforme. [React Native](https://en.wikipedia.org/wiki/React_Native) usa JavaScript e rende veri componenti nativi. [Flutter](https://en.wikipedia.org/wiki/Flutter_%28software%29) usa il linguaggio Dart e disegna i propri widget. Riducono lo sforzo duplicato e possono accelerare la consegna, ma aggiungono una dipendenza dalla salute del framework e possono restare indietro rispetto alle funzioni di piattaforma più nuove.

Una [progressive web app](https://en.wikipedia.org/wiki/Progressive_web_app) (PWA: un sito web che può essere installato e funzionare offline) non richiede uno store e si aggiorna all'istante, ma ha accesso limitato ad alcune funzioni del dispositivo e una presenza più debole sulla schermata iniziale.

Scegli in base alle funzioni del dispositivo richieste, al profilo di prestazioni, all'orizzonte di manutenzione, alle competenze che puoi assumere e alla portata di cui hai bisogno. Un'app consumer ad alte prestazioni può giustificare il nativo. Un'app di contenuti e moduli con un piccolo team può adattarsi bene al multipiattaforma o a una PWA.

### Segui le linee guida di design della piattaforma

Ogni piattaforma ha convenzioni pubblicate e dettagliate. Apple fornisce le [Human Interface Guidelines](https://en.wikipedia.org/wiki/Human_interface_guidelines) e Google fornisce il [Material Design](https://en.wikipedia.org/wiki/Material_Design). Coprono navigazione, gesti, tipografia, spaziatura e comportamenti di sistema. Seguirle rende la tua app familiare, il che abbassa lo sforzo che gli utenti spendono per impararla. Combatterle fa sentire un'app estranea e goffa. Una base di codice multipiattaforma deve comunque rispettare le convenzioni per piattaforma dove differiscono, anziché imporre l'aspetto di una piattaforma all'altra.

### Progetta per i vincoli del mobile

Costruisci offline-first: lascia che i compiti centrali funzionino senza connessione, memorizza le modifiche localmente e sincronizza quando la rete ritorna. Gestisci con attenzione i conflitti quando gli stessi dati cambiano in due posti. Sii parsimonioso con batteria e dati: raggruppa le chiamate di rete, evita posizione costante o lavoro in background, comprimi i payload e rispetta le impostazioni di risparmio dati dell'utente. Pianifica la frammentazione, l'ampia diffusione di dimensioni di schermo, potenza dei dispositivi e versioni del sistema operativo. Scegli un intervallo di supporto in base ai dati d'uso reali e testa su hardware modesto, non solo sui modelli di punta. Progetta per schermi piccoli con chiara gerarchia, bersagli di tocco grandi e contenuto che si adatta a dimensioni e orientamenti diversi.

### Pianifica distribuzione, versionamento e aggiornamenti

La pubblicazione passa attraverso l'[Apple App Store](https://en.wikipedia.org/wiki/App_Store_%28Apple%29) e [Google Play](https://en.wikipedia.org/wiki/Google_Play), ciascuno con processi di revisione e politiche che possono ritardare o rifiutare un rilascio. Metti il tempo di revisione nel tuo calendario e leggi presto le politiche. Poiché gli utenti scelgono quando aggiornare, avrai sempre molte versioni sul campo contemporaneamente. Mantieni la tua app retrocompatibile con i client più vecchi e versiona le tue API (capitolo 2.3) così che una vecchia app continui a funzionare. Fornisci un modo per richiedere un aggiornamento quando devi, per esempio un avviso di aggiornamento forzato quando una versione è non sicura o non supportata, e usalo con parsimonia. Le imprese possono anche distribuire app interne attraverso MDM o canali privati anziché gli store pubblici.

### Usa con cura notifiche push e deep link

Le [notifiche push](https://en.wikipedia.org/wiki/Push_technology) ti permettono di raggiungere gli utenti quando l'app è chiusa. Usale per un valore genuino, rispetta il consenso dell'utente e i permessi della piattaforma ed evita il rumore, perché le persone disattivano le notifiche delle app che esagerano. I [deep link](https://en.wikipedia.org/wiki/Deep_linking) mandano un utente dritto a una schermata specifica da un link o da una notifica. Configurali così che un link apra il posto giusto nell'app e ripieghi con grazia sul web quando l'app non è installata.

### Proteggi l'app e i suoi dati

Tratta il dispositivo come non fidato e possibilmente perso. Memorizza i dati sensibili nell'archiviazione sicura della piattaforma (il [Keychain di iOS](https://en.wikipedia.org/wiki/Keychain_%28software%29) o l'Android Keystore), mai in file semplici. Offri l'[autenticazione biometrica](https://en.wikipedia.org/wiki/Biometrics) (impronta o volto) per sbloccare le azioni sensibili, sostenuta da un codice. Considera il [certificate pinning](https://en.wikipedia.org/wiki/Public_key_pinning) (verificare che il server presenti un certificato atteso) per le connessioni ad alto valore e pianifica la rotazione di quei certificati. Minimizza ciò che memorizzi sul dispositivo, proteggi i segreti e segui le indicazioni più ampie nella sicurezza delle applicazioni (capitolo 4.2).

### Costruisci una vera pipeline di test e consegna

Testa su dispositivi reali, non solo su [emulatori](https://en.wikipedia.org/wiki/Emulator) e simulatori, perché hardware, sensori e prestazioni differiscono. Usa un laboratorio di dispositivi o una device farm nel cloud per coprire una diffusione rappresentativa di modelli e versioni del sistema operativo. Automatizza build, test, firma e invio allo store attraverso [integrazione e consegna continue](https://en.wikipedia.org/wiki/CI/CD) (capitolo 8.1), compresa la distribuzione beta ai tester prima del rilascio pubblico. Gestire in sicurezza chiavi di firma e credenziali dello store fa parte di questa pipeline.

### Fai dell'accessibilità un requisito

Supporta le funzioni di accessibilità di ciascuna piattaforma: lettori di schermo ([VoiceOver](https://en.wikipedia.org/wiki/VoiceOver) su iOS, [TalkBack](https://en.wikipedia.org/wiki/Google_TalkBack) su Android), dimensionamento dinamico del testo, contrasto di colore sufficiente e bersagli di tocco grandi. Etichetta i controlli così che la tecnologia assistiva possa descriverli. Testa con gli strumenti assistivi reali, non solo con controlli automatici. Per gli enti pubblici soprattutto, l'accessibilità è un mandato di legge e i dettagli vivono nell'accessibilità (capitolo 5.3).

## Compromessi: vantaggi e svantaggi

| Approccio | Vantaggi | Svantaggi |
|---|---|---|
| Nativo (Swift, Kotlin) | Migliori prestazioni, pieno accesso al dispositivo, vera sensazione di piattaforma | Due basi di codice, costo più alto, più personale |
| React Native | Una base di codice JavaScript, veri componenti nativi, iterazione rapida | Dipendenza dal framework, complessità di bridging, ritardo sulle funzioni |
| Flutter | Una base di codice, UI coerente, ottime prestazioni | Competenze Dart meno comuni, dimensione dell'app maggiore, modello di widget proprio |
| Progressive web app | Nessuno store, aggiornamenti istantanei, una base di codice web | Funzioni del dispositivo limitate, presenza più debole, limiti di piattaforma |
| Aggiornamenti forzati | Rimuovono in fretta le vecchie versioni non sicure | Infastidiscono gli utenti se abusati; possono bloccare l'accesso |
| Certificate pinning | Forte protezione contro l'intercettazione | Si rompe se i certificati ruotano senza aggiornamenti dell'app |

Il compromesso ricorrente è portata e velocità di consegna contro profondità e fedeltà. Il nativo dà l'esperienza più ricca e fedele ma costa di più da costruire e mantenere. Gli approcci multipiattaforma e PWA risparmiano sforzo e allargano la portata, a un certo costo in sensazione di piattaforma o accesso al dispositivo. Per un piccolo team che rilascia moduli e contenuti, condividere una base di codice è spesso saggio. Per un'esigente app consumer, la profondità nativa può valere il prezzo. Decidi con l'intera vita dell'app in vista, non solo il lancio.

## Domande da discutere con il tuo team

1. **Per quanto tempo supportiamo i vecchi client sul campo, e la nostra API è versionata per tenerli in funzione?** Poiché gli utenti scelgono quando aggiornare, hai sempre molte versioni dell'app installate contemporaneamente e una modifica del backend che presume che tutti siano aggiornati romperà la lunga coda dei client più vecchi. Decidi la tua finestra di retrocompatibilità, versiona le tue API così che una vecchia app continui a funzionare e mantieni un percorso di aggiornamento forzato usato di rado per le versioni davvero non sicure. Conta per le app dei cittadini governative e per quelle della forza lavoro aziendale allo stesso modo, dove le persone con dispositivi vecchi non possono o non vogliono aggiornare secondo il tuo calendario. Porta i tuoi attuali dati di distribuzione delle versioni e chiediti che cosa si rompe per il client più vecchio ancora in uso reale. Se non conosci quella distribuzione, strumentala prima di rilasciare la tua prossima modifica che rompe.

2. **Qual è la nostra soglia per inviare una notifica push, e chi decide che cosa vale interrompere un utente?** Le notifiche push raggiungono le persone quando l'app è chiusa, il che le rende potenti e facili da abusare e gli utenti disattivano le notifiche (o cancellano l'app) dei prodotti che esagerano. Concorda che cosa conta come valore genuino, come gli utenti controllano frequenza e canale e come rispetti il consenso della piattaforma anziché assillare per il permesso. Senza una soglia condivisa, ogni team con una metrica da raggiungere ricorrerà a una push e l'intero canale degrada in rumore. Porta le notifiche inviate nell'ultimo mese e chiediti per quali l'utente ti avrebbe ringraziato. Se la maggior parte era promozionale, stringi la politica prima che lo faccia il tasso di disattivazione.

3. **La nostra pipeline di consegna mobile è reale, con firma, una device farm e distribuzione beta, o il rilascio è una stressante corsa manuale?** Il mobile aggiunge rischi che il web non ha: la revisione dello store può ritardare o rifiutare un rilascio, chiavi di firma e credenziali dello store vanno gestite in sicurezza e hardware e sensori differiscono abbastanza da far sì che gli emulatori nascondano problemi reali. Automatizzare build, test, firma e invio allo store attraverso CI/CD, con distribuzione beta ai tester e una device farm nel cloud che copra i modelli che i tuoi utenti portano davvero, è ciò che trasforma i rilasci da imprese eroiche in routine. Decidi chi possiede la pipeline e le chiavi di firma e come il tempo di revisione dello store è incorporato in ogni piano di rilascio. Porta la storia del tuo ultimo rilascio e conta i passi manuali. Ciascuno è un posto in cui un rilascio stressante può andare storto sotto scadenza.

4. **Abbiamo scelto tra nativo, multipiattaforma o progressive web app per l'intera vita di questo prodotto, o solo per il giorno del lancio?** L'approccio di costruzione è la singola leva maggiore su costo e capacità di un'app mobile per anni e una scelta fatta per rilasciare in fretta può intrappolarti: il nativo compra il più ricco accesso al dispositivo e la sensazione di piattaforma al prezzo di due basi di codice e due insiemi di competenze, mentre multipiattaforma e PWA condividono il codice ma aggiungono una dipendenza da un framework o perdono l'accesso ad alcune funzioni del dispositivo. Per un grande team, questa decisione guida le assunzioni, il budget di manutenzione e quanto in fretta puoi adottare ogni rilascio annuale del sistema operativo, quindi merita un responsabile esplicito anziché un valore predefinito fissato da chi ha scritto il primo prototipo. Porta le funzioni del dispositivo richieste, il profilo di prestazioni, l'orizzonte di manutenzione e le competenze che puoi davvero assumere e sii onesto su quali funzioni di piattaforma perderesti con ciascuna opzione. Nei contesti aziendali e governativi, pesa se l'app è un impegno di lunga durata che deve sopravvivere al ricambio del personale e a un decennio di cambiamenti di piattaforma e registra la decisione e la sua motivazione così che un futuro team non debba tirare a indovinare perché la base di codice sia fatta così.

5. **Quale intervallo di supporto di dispositivi e versioni del sistema operativo serve ai nostri utenti reali, e stiamo testando sull'hardware che portano davvero anziché sui telefoni sulle nostre scrivanie?** La frammentazione è la condizione normale del mobile: gli utenti coprono un'ampia diffusione di dimensioni di schermo, potenza dei dispositivi e versioni del sistema operativo e un'app regolata sui modelli di punta del team uscirà lenta o rotta sull'hardware modesto che gran parte del tuo pubblico possiede. Fissare un intervallo di supporto è un compromesso tra portata e sforzo, perché ogni modello e versione più vecchi che prometti di supportare allarga la matrice dei test e l'onere di manutenzione, quindi l'intervallo deve venire dai dati d'uso reali anziché da un'ipotesi. Porta la tua distribuzione di dispositivi e versioni del sistema operativo, i modelli che una device farm o un laboratorio coprono attualmente e le prestazioni che hai misurato su hardware di fascia bassa, non solo su simulatori. Per le app governative dei cittadini è quasi non negoziabile, perché devi servire tutti, comprese le persone con dispositivi vecchi e connessioni lente sotto obblighi di accessibilità e per le flotte aziendali dovresti testare gli esatti dispositivi rinforzati che il personale porta anziché un campione generico.

6. **Quali dati sensibili vivono sul dispositivo, e ciascuno è protetto contro un telefono perso, rubato o nelle mani di qualcun altro?** Un dispositivo mobile viaggia in tasca e si perde o viene rubato, quindi qualsiasi dato o segreto memorizzato in un file semplice è a un telefono smarrito dall'esposizione e il raggio d'impatto cresce con ogni utente. Le considerazioni tirano l'una contro l'altra: tenere dati in cache sul dispositivo è ciò che fa funzionare l'offline-first e mantiene veloce l'app, eppure ogni elemento in cache è una passività che deve stare nell'archiviazione sicura della piattaforma (il Keychain di iOS o l'Android Keystore), essere minimizzato e idealmente essere protetto da biometria o da un codice. Porta un inventario di che cosa esattamente l'app conserva localmente, dove è memorizzato ciascun elemento, che cosa lo sblocca e se le connessioni ad alto valore usano il certificate pinning con un piano di rotazione praticabile. Nei contesti aziendali, lega questo alla politica di gestione dei dispositivi mobili e alla cancellazione da remoto e in quelli governativi tratta i dati personali sul dispositivo come un'esposizione di privacy e legale che deve essere giustificata, documentata e difendibile in un audit.

## Lente settoriale

**Startup.** Con un team minuscolo e poca liquidità, raramente puoi permetterti due basi di codice native o due insiemi di competenze, quindi un framework multipiattaforma o persino una PWA che raggiunge entrambi gli store da una sola base di codice di solito vince. Rilascia offline-first per l'unico compito centrale che conta, tieni ogni token nell'archiviazione sicura anziché in un file semplice e metti il tempo di revisione dello store in ogni rilascio così che un rifiuto non faccia saltare la data di un lancio. Salta aggiornamenti forzati, certificate pinning e device farm finché l'uso reale non li giustifica.

**Piccola impresa.** Senza uno specialista mobile dedicato e con un budget ridotto, propendi con forza per comprare anziché costruire: un costruttore di app no-code, un'app white-label dal tuo fornitore di punto vendita o prenotazioni o una PWA ben fatta dal tuo sito esistente spesso batte un'app su misura che non puoi mantenere. Se commissioni un'app, possiedi tu stesso le chiavi di firma e gli account dello store così che un appaltatore non possa tenere in ostaggio la tua presenza e insisti su accessibilità e archiviazione sicura sul dispositivo nel contratto. Limita l'ambito a uno o due compiti che i clienti fanno davvero su un telefono.

**Grande impresa.** Su larga scala, l'app è un impegno di lunga durata tra molti team, quindi standardizza l'approccio di costruzione, lo schema di archiviazione sicura, la pipeline CI/CD e la politica di versionamento delle API anziché lasciare che ogni prodotto li reinventi. Le app interne per la forza lavoro di solito passano attraverso la gestione dei dispositivi mobili per installazione, configurazione, cancellazione da remoto e politica, mentre le app per i clienti richiedono una device farm che copra l'uso reale e accessibilità e sicurezza verificate. Governa centralmente chiavi di firma, credenziali dello store e tempi di rilascio così che una modifica del backend che rompe non lasci mai in secca la lunga coda dei client più vecchi.

**Ente pubblico.** Regole sugli appalti, trasparenza e responsabilità pubblica plasmano ogni scelta. Devi servire tutti, comprese le persone con dispositivi vecchi e connessioni lente, quindi l'accessibilità è un mandato di legge verificato con strumenti assistivi reali e un ampio intervallo di supporto dei dispositivi è quasi non negoziabile. Privilegia approcci e contratti che evitino il lock-in con il fornitore, tengano portabili i dati e permettano al pubblico di ispezionare che cosa l'app fa con i suoi dati e tratta i dati personali sul dispositivo come un'esposizione che devi giustificare e documentare in un audit.

## Esempi

**Startup.** Una startup di tre persone che costruisce un'app di monitoraggio delle abitudini doveva raggiungere sia iOS sia Android ma non poteva permettersi due basi di codice native né due insiemi di competenze. Hanno scelto un framework multipiattaforma così che un piccolo team potesse rilasciare su entrambi gli store e hanno progettato offline-first fin dall'inizio così che un utente potesse registrare un'abitudine in metropolitana senza segnale e sincronizzare dopo. Hanno tenuto il token di accesso nell'archiviazione sicura della piattaforma anziché in un file semplice, messo il tempo di revisione dello store in ogni piano di rilascio e testato su un paio di telefoni vecchi economici accanto ai propri, il che ha colto prestazioni lente che altrimenti avrebbero rilasciato.

**Grande impresa.** Un'azienda di logistica ha costruito un'app interna per i suoi autisti e il personale di magazzino. Poiché magazzini e percorsi di consegna hanno segnale a chiazze, il team ha scelto un progetto offline-first: scansioni e aggiornamenti di stato si salvano localmente e sincronizzano quando la connessione ritorna. Ha usato un framework multipiattaforma per servire una base di codice a entrambe le piattaforme con un piccolo team. L'app è distribuita attraverso la gestione dei dispositivi mobili anziché gli store pubblici, così che l'IT controlli installazione, configurazione e politica di sicurezza sui dispositivi aziendali. Le credenziali sensibili vivono nell'archiviazione sicura della piattaforma e la biometria sblocca l'app. Una device farm nel cloud testa una diffusione rappresentativa dei dispositivi rinforzati che il personale porta davvero.

**Ente pubblico.** Un'agenzia nazionale ha rilasciato un'app rivolta ai cittadini per identità e prestazioni. L'accessibilità era un requisito rigido fin dal primo giorno: pieno supporto per i lettori di schermo, dimensionamento dinamico del testo e forte contrasto, testati con strumenti assistivi reali per soddisfare la legge. Poiché i cittadini usano un'enorme gamma di dispositivi, il team ha supportato un'ampia fascia di modelli più vecchi e connessioni lente e ha mantenuto funzionanti offline i compiti centrali. I dati sensibili restano nell'archiviazione sicura del dispositivo, la biometria protegge l'accesso e le connessioni ad alto valore usano il certificate pinning con un processo di rotazione pianificato. Il versionamento delle API mantiene funzionanti le app installate più vecchie ed esiste un percorso di aggiornamento forzato usato di rado per le correzioni di sicurezza. I tempi di revisione dello store sono incorporati in ogni piano di rilascio.

## Business case: motivazioni, ROI e TCO

Il mobile è dove molti utenti incontrano il tuo servizio, quindi l'app incide su adozione, soddisfazione e completamento dei compiti che contano per la tua organizzazione. Un'app veloce, affidabile e ben progettata aumenta l'uso e riduce il carico di assistenza. Per le imprese, un'app mobile interna può rendere misurabilmente più produttiva una forza lavoro mobile e tagliare la carta. Per gli enti pubblici, un'app utilizzabile per i cittadini allarga l'accesso e riduce la domanda al call center e di persona.

Sul costo totale di proprietà (TCO), la scelta dell'approccio è la leva maggiore. Il nativo significa pagare due basi di codice e due insiemi di competenze per l'intera vita dell'app. Il multipiattaforma scambia parte di questo con una dipendenza che devi tenere aggiornata. Oltre al codice, metti a bilancio commissioni e cicli di revisione degli store, un laboratorio di test sui dispositivi o una device farm nel cloud, il supporto continuo delle versioni del sistema operativo man mano che le piattaforme rilasciano ogni anno e il lavoro di sicurezza che il mobile richiede. Il costo di investire troppo poco compare come crash su dispositivi non supportati, incidenti di sicurezza da dati sul dispositivo non protetti, rilasci rifiutati o ritardati e utenti che abbandonano un'app lenta o goffa.

Per presentare il caso alla leadership, collega l'app a esiti concreti: completamento dei compiti, fidelizzazione, produttività della forza lavoro o costo di assistenza ridotto. Prezza la decisione sull'approccio completo lungo la vita dell'app, non solo il primo rilascio, e nomina i rischi (sicurezza, legge sull'accessibilità, rifiuto dello store) che una seria pratica mobile riduce.

## Antipattern e insidie

- **Trattare il mobile come un sito web rimpicciolito**: ignorare tocco, gesti e convenzioni di piattaforma.
- **Presumere una rete perfetta**: nessuna gestione offline, così l'app si rompe nel momento in cui cade il segnale.
- **Testare solo sull'ultimo modello di punta**: nascondere scarse prestazioni sui dispositivi che gli utenti reali portano.
- **Memorizzare segreti in file semplici**: dati sensibili esposti quando un dispositivo è perso o rubato.
- **Sovraccarico di notifiche**: troppe push, così gli utenti silenziano o cancellano l'app.
- **Ignorare il tempo di revisione dello store**: piani di rilascio che presumono una pubblicazione istantanea e poi slittano.
- **Nessun percorso di aggiornamento forzato**: vecchie versioni non sicure vivono senza modo di ritirarle.
- **Consumare batteria e dati**: lavoro costante in background e rete chiacchierona che gli utenti notano.
- **Accessibilità come ripensamento**: escludere utenti e, per gli enti pubblici, violare la legge.
- **Una base di codice forzata a sembrare identica ovunque**: un'app che si sente estranea su entrambe le piattaforme.

## Modello di maturità

**Livello 1: Avvio.** Il mobile è ad hoc e reattivo. L'app è costruita come un sito web, testata sui telefoni del team stesso e spesso si rompe offline. Poca attenzione va ad archiviazione sicura, accessibilità o tempi di revisione dello store. I rilasci sono una stressante corsa manuale e nessuno possiede l'approccio di costruzione né le chiavi di firma.

**Livello 2: Sviluppo.** Compaiono pratiche di base, ma sono incoerenti tra team e prodotti. Un approccio di costruzione è scelto per una data app, segue le basi della piattaforma ed è testato su alcuni dispositivi reali ed esistono qualche gestione offline e archiviazione sicura. Le build sono in parte automatizzate e qualcuno possiede gli invii allo store, eppure l'app di un altro team può ancora fare tutto questo in modo diverso o per niente.

**Livello 3: Standardizzazione.** La buona pratica è documentata e fatta rispettare nell'organizzazione. L'offline-first è il valore predefinito, un intervallo di supporto dei dispositivi documentato è testato su un laboratorio di dispositivi o una device farm nel cloud e linee guida di design della piattaforma e accessibilità sono seguite e verificate con strumenti assistivi reali. Archiviazione sicura, biometria e versionamento delle API sono standard, la CI/CD automatizza build, test, firma e distribuzione beta e il tempo di revisione dello store è pianificato in ogni rilascio.

**Livello 4: Gestione.** La qualità del mobile è misurata e controllata rispetto a valori di riferimento. Crash, avvio a freddo e prestazioni di resa delle schermate, uso di batteria e dati e tassi di completamento dei compiti sono catturati di continuo da dispositivi reali e seguiti rispetto a obiettivi, con ripartizioni per modello e per versione del sistema operativo così che una regressione su hardware di fascia bassa sia colta, non rilasciata. Accessibilità e sicurezza sono verificate anziché presunte, i tassi di disattivazione delle notifiche e di adozione degli aggiornamenti sono monitorati e l'intervallo di supporto e l'approccio di costruzione sono rivisti su questa evidenza. Le decisioni di correggere o ritirare un rilascio poggiano sulle metriche, non su come l'app si sentiva sul telefono del responsabile.

**Livello 5: Orchestrazione.** Il mobile è migliorato di continuo e integrato nell'organizzazione e si adatta al mutare del panorama dei dispositivi. Rotazione dei certificati, percorsi di aggiornamento forzato e ripristino sono di routine, l'intervallo di supporto e l'approccio di costruzione sono ridefiniti sull'evidenza man mano che le piattaforme rilasciano ogni anno e l'intera diffusione di utenti e dispositivi è trattata come di prim'ordine. La pianificazione mobile è collegata a sicurezza, accessibilità, API e pratica di consegna, così che un cambio di sistema operativo, una nuova fascia di dispositivi o un cambio di politica sia assorbito come lavoro di routine anziché un'emergenza.

## Spunti di discussione

- Come decidete tra nativo, multipiattaforma e progressive web app per un dato prodotto?
- Quale intervallo di supporto di dispositivi e versioni del sistema operativo si adatta ai vostri dati d'utenza reali, e come lo tenete aggiornato?
- Dove l'offline-first è essenziale nella vostra app, e come gestirete i conflitti di sincronizzazione?
- Quando un aggiornamento forzato è giustificato, e come evitate di bloccare gli utenti in modo ingiusto?
- Come testerete su dispositivi reali a una scala che rifletta i vostri utenti?
- Quali dati sensibili vivono sul dispositivo, e come è protetto ciascuno?
- Come rispettate le convenzioni di ciascuna piattaforma da una base di codice condivisa?

## Punti chiave

- Scegli l'approccio di costruzione (nativo, multipiattaforma o PWA) per l'intera vita dell'app.
- Segui le linee guida di design della piattaforma così che l'app sia familiare e abbassi lo sforzo dell'utente.
- Progetta per i vincoli del mobile: offline-first, batteria e dati parsimoniosi, frammentazione, schermi piccoli.
- Non controlli i tempi di rilascio; pianifica revisione dello store, versionamento e aggiornamenti forzati.
- Usa notifiche push e deep link con moderazione e consenso.
- Proteggi i dati sul dispositivo con archiviazione sicura, biometria e, dove giustificato, certificate pinning.
- Testa su dispositivi reali e automatizza la pipeline mobile attraverso CI/CD.
- Fai dell'accessibilità un requisito, che per gli enti pubblici è un mandato di legge.

## Riferimenti e letture di approfondimento

- Apple, *Human Interface Guidelines*
- Google, linee guida *Material Design*
- Apple, *App Store Review Guidelines*
- Google, *Google Play developer policies* e documentazione per sviluppatori Android
- OWASP, *Mobile Application Security Verification Standard (MASVS)* e *Mobile Security Testing Guide*
- Documentazione del progetto React Native
- Documentazione del progetto Flutter
- Google, indicazioni di *web.dev* sulle progressive web app
- Riferimenti U.S. Section 508 e WCAG (Web Content Accessibility Guidelines) per l'accessibilità mobile
- NIST, *Guidelines on mobile device security and management*
