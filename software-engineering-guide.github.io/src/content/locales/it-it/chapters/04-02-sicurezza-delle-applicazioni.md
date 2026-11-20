# 4.2 Sicurezza delle applicazioni

## Panoramica e motivazioni

La sicurezza delle applicazioni è dove le minacce astratte incontrano il codice concreto. La maggior parte delle violazioni che arrivano sui titoli risale a un difetto a livello applicativo: un'injection, un flusso di autenticazione rotto, un segreto esposto o una dipendenza compromessa. Per i grandi team che rilasciano molti servizi, la parte difficile non è sapere che questi difetti esistono. È prevenirli in modo coerente in una base di codice sterminata scritta da migliaia di mani nell'arco di molti anni.

Per le imprese, la sicurezza delle applicazioni è una questione di fiducia dei clienti e di obbligo normativo. Un difetto in un flusso di accesso o in un percorso di pagamento può innescare frodi, sanzioni e notifica obbligatoria della violazione. I sistemi governativi affrontano gli stessi rischi tecnici con dati di posta più alta: idoneità alle prestazioni, registri fiscali, dati di giustizia penale e infrastrutture nazionali. In entrambi i contesti, l'applicazione è la porta d'ingresso e gli attaccanti la sondano di continuo e in modo automatico.

Questo capitolo tratta le pratiche che mantengono resilienti le applicazioni: conoscere e difendersi dalle classi comuni di vulnerabilità, convalidare l'input e codificare l'output, fare bene autenticazione e autorizzazione, gestire i segreti e proteggere la supply chain del software che determina sempre più la tua reale superficie d'attacco.

*Vedi anche:* il capitolo 4.1 (fondamenti di sicurezza, modellazione delle minacce e ciclo di vita sicuro dello sviluppo), il capitolo 10.3 (supply chain open source e licenze) e il capitolo 10.2 (SBOM, rischio e garanzia).

## Principi chiave

- **Non fidarti mai dell'input.** Tratta tutti i dati che attraversano un confine di fiducia come ostili finché non sono convalidati.
- **Valori predefiniti sicuri.** Il percorso sicuro dovrebbe essere quello facile; il comportamento non sicuro dovrebbe richiedere uno sforzo deliberato e visibile.
- **Fallisci chiuso.** Quando un controllo di sicurezza non può completarsi, nega l'accesso anziché consentirlo.
- **Difesa in profondità a livello applicativo.** Combina convalida, codifica, parametrizzazione e protezioni del framework; non appoggiarti a una sola.
- **Minimo privilegio per identità e token.** Delimita le credenziali in modo stretto e falle scadere in fretta.
- **Le tue dipendenze sono il tuo codice.** Sei responsabile della sicurezza di tutto ciò che rilasci, compresi i componenti di terze parti e open source.
- **Standard anziché improvvisazione.** Usa quadri collaudati come l'ASVS dell'[OWASP](https://en.wikipedia.org/wiki/OWASP) (Open Worldwide Application Security Project) anziché inventare i tuoi controlli di sicurezza.

## Raccomandazioni

### Conosci e difendi l'OWASP Top 10, verifica con ASVS

L'OWASP Top 10 è l'elenco di riferimento del settore dei rischi più critici delle applicazioni web: controllo degli accessi rotto, fallimenti crittografici, injection, progettazione non sicura, configurazione di sicurezza errata, componenti vulnerabili, fallimenti di autenticazione, fallimenti di integrità dei dati, fallimenti di registrazione e server-side request forgery. Trattalo come conoscenza richiesta a ogni ingegnere, non solo come un riferimento di conformità da archiviare.

Per uno standard rigoroso e testabile, adotta l'**OWASP Application Security Verification Standard (ASVS)**. L'ASVS definisce requisiti di sicurezza a tre livelli di garanzia, dandoti controlli concreti e verificabili contro cui progettare e testare. Scegli il livello adatto al rischio di ciascuna applicazione e verifica rispetto a esso.

### Convalida l'input e codifica l'output

Le falle di injection restano tra le più dannose proprio perché sono così facili da introdurre. Difenditi con controlli a strati:

- **Convalida l'input** rispetto a rigidi elenchi consentiti (tipo atteso, lunghezza, formato, intervallo). Rifiuta anziché sanificare dove puoi.
- **Usa query parametrizzate** e [prepared statement](https://en.wikipedia.org/wiki/Prepared_statement) per ogni accesso al database; non costruire mai SQL per concatenazione di stringhe. Usa correttamente query builder sicuri e ORM (object-relational mapper).
- **Codifica l'output** in base al contesto. HTML, attributi HTML, JavaScript, URL e CSS richiedono ciascuno una codifica diversa. Appoggiati all'escape automatico del framework e capiscine i limiti.
- **Previeni il [cross-site scripting](https://en.wikipedia.org/wiki/Cross-site_scripting) (XSS)** con la codifica dell'output più una forte Content Security Policy come secondo strato.
- **Previeni command injection e template injection** evitando di invocare la shell con dati non fidati e usando template privi di logica o in sandbox.

### Fai bene autenticazione e autorizzazione

L'autenticazione prova chi è un utente. L'autorizzazione decide che cosa può fare. Entrambe falliscono spesso, quindi falle bene.

- Preferisci protocolli consolidati: **[OAuth 2.0](https://en.wikipedia.org/wiki/OAuth)** per l'autorizzazione delegata e **[OpenID Connect](https://en.wikipedia.org/wiki/OpenID_Connect) (OIDC)** per l'autenticazione. Non costruirli da zero.
- Imponi l'**[autenticazione a più fattori](https://en.wikipedia.org/wiki/Multi-factor_authentication) (MFA)**, specialmente per l'accesso privilegiato e amministrativo.
- Memorizza le password solo come hash con sale usando un algoritmo moderno, lento e che richiede molta memoria (come [Argon2](https://en.wikipedia.org/wiki/Argon2) o [bcrypt](https://en.wikipedia.org/wiki/Bcrypt)). Non memorizzare né registrare mai credenziali in chiaro.
- Gestisci con cura le **sessioni**: genera token crittograficamente forti, imposta i flag secure e HttpOnly sui cookie, ruota al cambio di privilegio e fai scadere le sessioni inattive.
- Fai rispettare l'**autorizzazione sul server per ogni richiesta**, verificando che il principale autenticato possieda o possa accedere alla specifica risorsa. L'autorizzazione rotta a livello di oggetto (accedere al record di un altro utente cambiando un ID) è uno dei difetti di API più comuni e gravi.
- Centralizza la logica di autorizzazione dove praticabile così che la politica sia coerente e verificabile.

### Gestisci i segreti e ruota le chiavi

I segreti scritti nel codice sorgente sono una causa perenne di violazioni. Costruisci un'abitudine disciplinata attorno alla gestione dei segreti:

- Memorizza i segreti in un gestore di segreti o vault dedicato, mai nel sorgente, nei file di configurazione o in variabili d'ambiente inserite nel controllo di versione.
- Scansiona automaticamente commit e repository alla ricerca di segreti trapelati e blocca i merge che li introducono.
- Ruota chiavi e credenziali regolarmente e subito a ogni sospetta esposizione. Preferisci credenziali di breve durata emesse automaticamente a quelle statiche di lunga durata.
- Applica il minimo privilegio a ogni segreto: delimitalo esattamente a ciò di cui ha bisogno.
- Cifra i segreti a riposo e in transito e verifica gli accessi a essi.

### Proteggi la supply chain del software

Le applicazioni moderne sono per lo più assemblate da componenti di terze parti, il che rende la supply chain una superficie d'attacco primaria.

- Mantieni una **[distinta base del software](https://en.wikipedia.org/wiki/Software_bill_of_materials) (SBOM)** per ogni applicazione così da sapere esattamente che cosa rilasci e poter rispondere in fretta quando arriva una nuova vulnerabilità.
- Scansiona di continuo le dipendenze (Software Composition Analysis, o SCA) e rimedia prontamente ai componenti con vulnerabilità note.
- Fissa e verifica le versioni delle dipendenze; usa lockfile e registri fidati.
- Adotta **SLSA** (Supply-chain Levels for Software Artifacts) per alzare l'integrità della build e genera attestazioni di **provenienza** che descrivono come gli artefatti sono stati costruiti.
- **Firma gli artefatti** e verifica le firme prima del rilascio così da poter fidarti che ciò che gira sia ciò che hai costruito.
- Proteggi il sistema di build stesso; una pipeline CI compromessa può iniettare codice malevolo in ogni consumatore a valle.

## Compromessi: vantaggi e svantaggi

| Decisione | Vantaggi | Svantaggi |
|---|---|---|
| Comprare/adottare un provider di identità (OIDC) | Collaudato, MFA integrata, meno codice da proteggere | Dipendenza dal fornitore, sforzo di integrazione, costo |
| Costruire autenticazione su misura | Pieno controllo, nessuna dipendenza esterna | Estremamente facile sbagliare, alta manutenzione |
| Convalida rigida con elenchi consentiti | Blocca intere classi di vulnerabilità | Può rompere casi limite legittimi, più lavoro iniziale |
| Credenziali di breve durata | Piccola finestra di violazione, revoca automatica | Richiede un'infrastruttura di emissione robusta |
| Aggiornamenti aggressivi delle dipendenze | Meno vulnerabilità note | Ricambio, possibili modifiche che rompono, onere di test |
| SBOM + firma + provenienza | Risposta rapida agli incidenti, fiducia verificabile | Investimento in strumenti e processo, cambio di cultura |

Il compromesso ricorrente è rigore iniziale contro esposizione continua. Costruire autenticazione su misura o saltare l'igiene delle dipendenze sembra più veloce oggi e ti costa enormemente dopo. Adottare standard collaudati e controlli automatici della supply chain costa sforzo ora, ma trasforma un rischio illimitato e imprevedibile in uno gestito e limitato. Per i grandi team conta più di tutto il moltiplicatore dell'automazione: un controllo applicato una volta in un modello da strada asfaltata protegge ogni servizio che lo usa.

## Domande da discutere con il tuo team

1. **Quali controlli ASVS incorporerete nel vostro framework da strada asfaltata così che gli ingegneri li ottengano gratis?** La mossa a più alta leva per un grande team è rendere il percorso sicuro quello predefinito, così che un controllo scritto una volta in un framework condiviso protegga ogni servizio che lo adotta. Decidi quali requisiti ASVS (query parametrizzate, codifica dell'output, flag di sessione sicuri, controlli di autorizzazione lato server) appartengono al modello anziché alla memoria di ciascun ingegnere. Per i portafogli aziendali e governativi, decidi anche quali applicazioni richiedono ASVS di Livello 2 rispetto al Livello 3 e legalo alla sensibilità dei dati che ciascuna tocca. Porta un elenco dei tuoi servizi e segna quali ereditano già questi valori predefiniti e quali reimplementano la sicurezza a mano, perché quelli fatti a mano sono dove si nascondono injection e controllo degli accessi rotto. Se i valori predefiniti sicuri vivono solo in una pagina wiki, saranno saltati sotto la pressione della consegna, quindi mettili nel codice.

2. **Come troverete e correggerete l'autorizzazione rotta a livello di oggetto in ogni API, non solo in quelle nuove?** Accedere al record di un altro utente cambiando un ID è uno dei difetti di API più comuni e gravi, e si nasconde negli endpoint più vecchi che precedono i vostri standard attuali. L'autorizzazione lato server a ogni richiesta e a ogni oggetto è la regola, ma la parte difficile è verificare che regga in una base di codice sterminata e vecchia di anni scritta da molte mani. Decidi se centralizzerete la logica di autorizzazione, aggiungerete test automatici che tentano l'accesso tra tenant o eseguirete test mirati prima sulle API a più alto rischio. Porta il tuo inventario degli endpoint che espongono identificatori di oggetti e ordinali per sensibilità di ciò che restituiscono. Senza una scansione deliberata, continuerete a rilasciare questo difetto e lo scoprirete solo quando lo fa un ricercatore o un attaccante.

3. **Qual è il vostro piano per la prossima vulnerabilità diffusa nelle dipendenze: quanto in fretta potete trovare e correggere ogni servizio interessato?** Quando un difetto critico compare in una libreria popolare, le aziende con una SBOM accurata identificano i servizi interessati in ore mentre altre passano settimane a cercare, e quel divario di velocità decide quanto danno subisci. Decidi ora se produci una distinta base del software per ogni artefatto, se la scansione delle dipendenze gira in ogni pipeline e chi possiede la decisione di correzione d'emergenza. Per gli acquirenti regolamentati e governativi, SBOM e provenienza firmata sono sempre più una condizione per fare affari, quindi questa prontezza protegge anche i ricavi. Porta la risposta onesta a un'esercitazione: scegli una libreria che usi ampiamente e cronometra quanto ci vuole a elencare ogni servizio che la rilascia. Se la risposta si misura in giorni, investi in inventario e firma prima che il prossimo incidente ti ci costringa.

4. **Come passerete da segreti statici di lunga durata a credenziali di breve durata emesse automaticamente, e quali sistemi lo impediscono oggi?** I segreti scritti nel codice e di lunga durata sono una causa perenne di violazioni e la soluzione, credenziali di breve durata emesse su richiesta, dipende da un'infrastruttura di emissione che i sistemi più vecchi spesso non possono usare. Per un grande team il pericolo è l'adozione disomogenea: una piattaforma moderna ruota le chiavi ogni ora mentre un servizio legacy rilascia ancora una password di database statica in un file di configurazione. Decidi quali carichi possono consumare subito un gestore di segreti o un sistema di identità del carico di lavoro, quali richiedono prima un investimento e chi possiede il runbook di rotazione nel momento in cui una chiave è sospettata trapelata. Porta un inventario di ogni credenziale in uso, la sua durata, il suo raggio d'impatto se esposta e se la scansione dei commit la coglierebbe prima del merge. Nei contesti aziendali e governativi, collega questo all'audit: gli esaminatori si aspettano sempre più evidenza di rotazione, accesso delimitato e registrazione degli accessi per ogni segreto, e una credenziale statica che non puoi ruotare senza interruzione è un rilievo in attesa di essere scritto.

5. **Dove eseguite ancora un'autenticazione artigianale o incoerente, e qual è il piano per consolidarla su protocolli collaudati?** Costruire l'autenticazione è uno dei modi più facili di introdurre difetti sottili e sfruttabili, eppure la maggior parte dei grandi patrimoni porta almeno un flusso di accesso legacy che precede la decisione di standardizzare su OAuth 2.0 e OIDC. Le pressioni in competizione sono reali: migrare un vecchio flusso rischia di rompere utenti e integrazioni esistenti, mentre lasciarlo al suo posto tiene un bersaglio di alto valore sotto-difeso. Decidi se consolidate su un unico provider di identità, imponete la MFA in modo uniforme e fissate una scadenza per ritirare ogni flusso su misura, o accettate eccezioni documentate con controlli compensativi. Porta una mappa di ogni percorso di autenticazione nella flotta, quali impongono la MFA, quali memorizzano le password con un hash moderno e ad alta memoria e quali sono su misura. Per i portafogli aziendali e governativi, aggiungi l'angolo della conformità: standard come la NIST SP 800-63 fissano attese concrete sulla garanzia dell'identità e un flusso artigianale che non può dimostrarle non sopravvivrà a un audit o a una revisione di autorizzazione all'esercizio.

6. **Come verificate che questi controlli reggano davvero in produzione, e potete provarlo con evidenze anziché asserzioni?** Scrivere un valore predefinito sicuro non è lo stesso che sapere che ogni servizio lo rispetta ancora, e i controlli marciscono in silenzio man mano che il codice cambia, le eccezioni si accumulano e nuovi endpoint vengono rilasciati. Per un grande team la domanda è la copertura: quali servizi eseguono analisi statica, scansione delle dipendenze e test dinamici o di penetrazione e come sapete che quelli che li saltano non siano le vostre applicazioni a più alto rischio? Decidi quale verifica è obbligatoria nella pipeline rispetto a periodica, chi fa il triage dei rilievi e quali evidenze conservi per mostrare che un controllo è stato testato e superato in una data. Porta la tua attuale mappa di copertura, il tuo tempo medio di rimedio per gravità e l'elenco delle applicazioni senza un test recente. Nei contesti regolamentati e governativi questa evidenza non è facoltativa: auditor, funzionari di autorizzazione e investigatori delle violazioni chiedono tutti la prova che i controlli siano stati verificati e una politica senza registri di test raramente li soddisfa.

## Lente settoriale

**Startup.** Con due o tre ingegneri e nessuno specialista di sicurezza, la tua leva è ereditare la sicurezza anziché costruirla: adotta un provider di identità OIDC gestito, appoggiati a un framework il cui ORM parametrizza le query per impostazione predefinita e tieni i segreti nel gestore di segreti della tua piattaforma anziché in file `.env` che un collega potrebbe committare per errore. Attiva la scansione automatica delle dipendenze che apre pull request di correzione e consideralo sufficiente per ora. Non costruire autenticazione o crittografia su misura, perché una singola query iniettata o una chiave trapelata può far fallire l'azienda prima che abbia clienti.

**Piccola impresa.** Probabilmente non hai uno specialista di sicurezza applicativa e hai un budget ridotto, quindi compra controlli integrati negli strumenti e nelle piattaforme che già paghi anziché dotare di personale una funzione dedicata. Scegli un provider di identità ospitato con MFA inclusa, un database gestito che ti orienti verso l'accesso parametrizzato e un host di repository che scansioni i commit alla ricerca di segreti trapelati di serie. Concentra la tua scarsa attenzione sulle basi dell'OWASP Top 10 che causano la maggior parte delle violazioni reali e preferisci i fornitori che rilasciano valori predefiniti sicuri che non puoi disattivare con leggerezza.

**Grande impresa.** Tra molti team la sfida è la coerenza: incorpora i controlli ASVS in framework da strada asfaltata così che ogni nuovo servizio erediti gratis query parametrizzate, codifica dell'output, sessioni sicure e autorizzazione lato server. Mantieni SBOM accurate e scansione delle dipendenze su tutta la flotta così che la prossima vulnerabilità diffusa in una libreria sia questione di ore, non di settimane, e centralizza la politica di autorizzazione così che l'accesso tra tenant diventi testabile. Standardizza su un unico provider di identità con MFA imposta e gestisci la sicurezza applicativa come un portafoglio governato con livelli ASVS per fascia di rischio ed evidenze verificabili.

**Ente pubblico.** Regole sugli appalti, trasparenza e responsabilità pubblica plasmano i controlli che devi dimostrare, non solo implementare. Verifica i servizi rivolti ai cittadini rispetto all'OWASP ASVS a un livello adeguato alla sensibilità dei dati, firma ogni artefatto rilasciato e attesta la sua provenienza secondo SLSA per soddisfare i mandati sulla supply chain, ed emetti credenziali di breve durata da un vault centrale con piena registrazione degli accessi. Aspettati di dover mostrare ad auditor e funzionari di autorizzazione una catena di custodia documentata dal sorgente alla produzione e di allineare la garanzia dell'identità a standard pubblicati come la NIST SP 800-63.

## Esempi

**Startup.** Un team SaaS di tre ingegneri salta la costruzione del proprio accesso e adotta fin dal primo giorno un provider OIDC gestito, ottenendo MFA e reimpostazioni di password sicure senza scrivere codice critico per la sicurezza che non può permettersi di sbagliare. Si appoggia all'ORM del framework così che le query siano parametrizzate per impostazione predefinita, tiene i segreti nel gestore di segreti della piattaforma anziché in file `.env` che un collega potrebbe committare per errore e attiva la scansione automatica delle dipendenze che apre una pull request quando una libreria ha bisogno di una correzione. Niente di questo rallenta il team e significa che una chiave trapelata o una query iniettata non fa fallire l'azienda prima che abbia clienti.

**Grande impresa.** Una piattaforma di vendita al dettaglio che serve decine di milioni di acquirenti standardizza l'autenticazione su OIDC attraverso un unico provider di identità, imponendo la MFA al personale e l'autenticazione a gradini per le modifiche ad alto valore degli account. Tutto l'accesso al database passa attraverso un ORM configurato per parametrizzare le query e una Content Security Policy sostiene la codifica dell'output. Dopo una vulnerabilità ampiamente pubblicizzata in una popolare libreria di logging, la SBOM dell'azienda le permette di identificare ogni servizio interessato in poche ore e di correggerli in due giorni, mentre i concorrenti senza inventari hanno passato settimane a cercare.

**Ente pubblico.** Un'agenzia federale di prestazioni costruisce servizi rivolti ai cittadini verificati rispetto all'OWASP ASVS Livello 2, con il Livello 3 per i componenti che trattano i registri più sensibili. I segreti vivono in un vault centrale che emette credenziali di breve durata; la scansione dei commit blocca qualsiasi chiave trapelata. Ogni artefatto rilasciato è firmato e la sua provenienza attestata secondo SLSA, soddisfacendo un mandato federale per supply chain del software verificabili e dando agli auditor una chiara catena di custodia dal sorgente alla produzione.

## Business case: motivazioni, ROI e TCO

La spesa per la sicurezza delle applicazioni abbassa la categoria di violazione più probabile e più costosa. Il costo totale di proprietà comprende strumenti (scanner, gestori di segreti, provider di identità), tempo degli ingegneri per rimediare ai rilievi e il lieve attrito dei valori predefiniti sicuri. Contro questo, pesa il costo di saltarla: le violazioni da injection e da controllo degli accessi rotto espongono di routine milioni di record, innescando sanzioni normative, notifica obbligatoria, perdite per frode, sprint di rimedio e danno reputazionale che deprime i ricavi per anni.

Il ROI è più forte quando i controlli sono automatizzati e riutilizzati. Una singola integrazione di identità ben configurata, un solo strato di query rinforzato in un framework condiviso e una sola pipeline che blocca le dipendenze vulnerabili proteggono l'intera flotta a un costo marginale per servizio. I controlli della supply chain in particolare sono passati da facoltativi a essenziali: una dipendenza compromessa può trasformare ogni tuo cliente in una vittima e regolatori e acquirenti aziendali richiedono sempre più SBOM e provenienza firmata come condizione per fare affari. Quando presenti il caso alla leadership, lega l'investimento a rischi specifici e nominati e a requisiti di appalto e conformità che bloccano i ricavi se non li soddisfi.

## Antipattern e insidie

- **Scrivere la propria crittografia o autenticazione.** Produce quasi sempre difetti sottili e sfruttabili.
- **Convalida solo lato client.** Facilmente aggirabile; il server deve riconvalidare tutto.
- **Sanificazione a elenco di blocco.** Provare a togliere i caratteri "cattivi" anziché consentire solo quelli buoni; gli attaccanti trovano le falle.
- **Segreti nel sorgente o in file d'ambiente.** La singola causa più comune di fughe di credenziali.
- **Ignorare l'autorizzazione sull'accesso agli oggetti.** Dare per scontato che un utente autenticato possa accedere a qualsiasi oggetto di cui può indovinare l'ID.
- **Dipendenze lasciate lì.** Non aggiornare mai i componenti di terze parti finché una violazione lo impone.
- **Trattare la Top 10 come il traguardo.** È un pavimento, non uno standard completo; usa ASVS per la profondità.
- **Registrare dati sensibili.** Password, token e PII (informazioni di identificazione personale) nei log diventano una violazione in attesa di accadere.

## Modello di maturità

**Livello 1: Avvio.** La sicurezza delle applicazioni dipende dalla conoscenza dei singoli sviluppatori e reagisce solo dopo gli incidenti. Nessun controllo standard. I segreti stanno nel sorgente. Le dipendenze sono raramente aggiornate. L'autenticazione è su misura e ad hoc e i difetti di injection o di controllo degli accessi rotto si trovano per fortuna anziché per processo.

**Livello 2: Sviluppo.** Compaiono pratiche di base ma variano da team a team. Si diffonde la consapevolezza dell'OWASP Top 10, esistono alcune protezioni a livello di framework ed esiste un gestore di segreti ma è usato in modo disomogeneo. La scansione delle dipendenze gira occasionalmente. I nuovi sistemi adottano un provider di identità standard, mentre i servizi più vecchi tengono intatti i propri flussi di accesso artigianali.

**Livello 3: Standardizzazione.** I controlli sono documentati e fatti rispettare nell'organizzazione. I requisiti basati su ASVS sono fissati per fascia di rischio, query parametrizzate e codifica dell'output sono la norma e un provider di identità centrale con MFA è richiesto. I segreti sono gestiti e scansionati automaticamente, le SBOM sono prodotte e la scansione delle dipendenze gira in ogni pipeline.

**Livello 4: Gestione.** La pratica è misurata e controllata rispetto a valori di riferimento. Copertura di scansioni e test, tempo medio di rimedio per gravità, quota di servizi che ereditano i valori predefiniti da strada asfaltata, età di rotazione di credenziali e segreti e conformità ASVS sono tutti seguiti su cruscotti. Le eccezioni sono registrate con date di scadenza, la deriva dal riferimento innesca azioni e i rilasci sono filtrati da soglie di sicurezza definite anziché da giudizi.

**Livello 5: Orchestrazione.** La sicurezza è migliorata di continuo e integrata nell'organizzazione. I valori predefiniti sicuri sono incorporati in framework da strada asfaltata così che il percorso sicuro sia automatico, credenziali di breve durata sono usate ovunque e una piena garanzia della supply chain con firma e provenienza (SLSA) è standard. La verifica è continua, la risposta alle nuove vulnerabilità è rapida e misurata e ogni incidente alimenta i modelli condivisi così che una sola correzione rafforzi l'intera flotta.

## Spunti di discussione

1. Dove dovrebbe vivere la logica di autorizzazione per essere insieme coerente e manutenibile tra molti servizi?
2. Quanto aggressivamente dovreste aggiornare le dipendenze dato il compromesso tra esposizione e ricambio?
3. Quale livello ASVS è appropriato per ogni classe di applicazione del vostro portafoglio?
4. Come eliminate i segreti di lunga durata senza creare un'infrastruttura di emissione fragile?
5. Che cosa servirebbe alla vostra organizzazione per produrre e consumare SBOM e provenienza per ogni artefatto?
6. Come evitate che i valori predefiniti sicuri vengano disattivati sotto la pressione della consegna?

## Punti chiave

- L'OWASP Top 10 è conoscenza essenziale; ASVS fornisce lo standard testabile.
- Stratifica convalida dell'input, parametrizzazione e codifica dell'output per sconfiggere injection e XSS.
- Usa protocolli collaudati (OAuth 2.0, OIDC) e imponi la MFA; non costruire mai l'autenticazione da zero.
- Fai rispettare l'autorizzazione lato server per ogni richiesta e ogni oggetto.
- Tieni i segreti fuori dal sorgente, gestiscili centralmente e ruota verso credenziali di breve durata.
- La supply chain è una superficie d'attacco primaria; usa SBOM, SCA, firma e provenienza (SLSA).
- Controlli automatici e riutilizzabili proteggono l'intera flotta a un costo marginale per servizio.

## Riferimenti e letture di approfondimento

- OWASP, *Top 10 Web Application Security Risks*
- OWASP, *Application Security Verification Standard (ASVS)*
- OWASP, *Cheat Sheet Series* (Input Validation, Authentication, Authorization, Secrets Management)
- Dafydd Stuttard e Marcus Pinto, *The Web Application Hacker's Handbook*
- Aaron Parecki, *OAuth 2.0 Simplified*
- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines*
- Cloud Native Computing Foundation e OpenSSF, *SLSA framework* e indicazioni sulla *Supply-chain Security*
