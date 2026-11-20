# 5.4 Progettazione dei contenuti e della comunicazione

## Panoramica e motivazioni

La progettazione dei contenuti e della comunicazione è il lavoro di dare forma a parole, messaggi e informazioni che un prodotto usa per aiutare le persone ad agire. Copre la [strategia dei contenuti](https://en.wikipedia.org/wiki/Content_strategy) (quali contenuti dovrebbero esistere, per chi e perché), la scrittura UX e il microcopy (le etichette, i pulsanti, i suggerimenti e i messaggi di errore dentro un'interfaccia) e le comunicazioni che raggiungono gli utenti tramite email, notifiche e altri canali. Le parole sono interfaccia. Per la maggior parte del software, il contenuto è l'esperienza del prodotto molto più degli elementi visivi.

Per i grandi team, il contenuto è un problema di coordinamento e di fiducia. Quando molti team scrivono in modo indipendente, la terminologia diverge, il tono passa da amichevole a burocratico da una schermata all'altra e lo stesso concetto prende tre nomi diversi. Gli utenti perdono il filo e perdono fiducia. Una strategia dei contenuti condivisa lo risolve. Una guida di voce e tono, un vocabolario controllato e schemi riutilizzabili per errori e stati vuoti fanno per le parole ciò che un design system fa per i pixel: permettono a team indipendenti di produrre un insieme coerente e affidabile.

Nelle imprese e negli enti pubblici, un contenuto chiaro è spesso un requisito legale ed etico, non una questione di stile. Le leggi sul [linguaggio semplice](https://en.wikipedia.org/wiki/Plain_language) richiedono che le comunicazioni pubbliche siano comprensibili alle persone che devono agire su di esse. Un contenuto formulato male in un modulo di prestazioni, un'istruzione medica o un avviso di sicurezza può causare danno reale: una scadenza mancata, un dosaggio sbagliato, una vittima di frode. E in un'era di ["dark pattern"](https://en.wikipedia.org/wiki/Dark_pattern) manipolatori (progetti di interfaccia che ingannano o spingono le persone a scelte contro il proprio interesse), il modo in cui un prodotto presenta le scelte è una questione di fiducia, sicurezza e sempre più di regolamentazione.

## Principi chiave

- Le parole sono UI; il contenuto è una parte centrale dell'esperienza, non un riempitivo aggiunto dopo.
- Scrivi per l'obiettivo e il contesto del lettore, in linguaggio semplice, nel momento in cui ne ha bisogno.
- Chiarezza prima dell'ingegnosità; un utente confuso non è deliziato da un messaggio di errore spiritoso.
- La coerenza di terminologia e tono riduce il carico cognitivo e costruisce fiducia.
- Buoni valori predefiniti e stati vuoti utili guidano le persone al successo.
- Onestà per progetto: non ingannare, pressare o far vergognare mai gli utenti per spingerli a scelte.
- Il contenuto dovrebbe essere strutturato e riutilizzabile, non scritto nel codice e duplicato.
- Progetta le comunicazioni per l'intero percorso multicanale, rispettando l'attenzione.

## Raccomandazioni

### Stabilisci una strategia dei contenuti e una voce

Parti decidendo per chi è il contenuto, quali compiti lo aiuta a svolgere e come dovrebbe suonare. Scrivi una guida di voce e tono con esempi concreti e un glossario di terminologia ([vocabolario controllato](https://en.wikipedia.org/wiki/Controlled_vocabulary)) così che la stessa cosa si chiami sempre allo stesso modo. Lascia che il tono segua il contesto: rassicurante in un errore, calmo in un avviso di sicurezza, festoso in un successo. La voce resta costante; il tono si adatta. Tratta il contenuto come una risorsa gestita, con responsabili, revisione e un ciclo di vita, non come testo digitato in un campo all'ultimo momento.

### Scrivi microcopy che aiuti le persone ad agire

Etichetta i pulsanti con l'azione che compiono ("Invia domanda", non "OK"). Scrivi suggerimenti e testi di aiuto che prevengano gli errori prima che accadano. Metti in testa le parole importanti così che chi scorre la schermata colga comunque il punto. Usa la seconda persona e la forma attiva. Tieni le frasi brevi e specifiche. Ogni pezzo di microcopy dovrebbe ridurre l'incertezza su che cosa accadrà e che cosa fare dopo.

### Fai del linguaggio semplice lo standard e soddisfa i requisiti di legge

Scrivi a un [livello di lettura](https://en.wikipedia.org/wiki/Readability) adatto all'intero pubblico, non agli autori. Preferisci parole comuni, frasi brevi e istruzioni concrete; espandi gergo e acronimi alla prima occorrenza o evitali. Nel settore pubblico, il linguaggio semplice è spesso richiesto da legge e politica: segui gli standard di linguaggio semplice applicabili e testa la comprensione con utenti reali, comprese persone con minore alfabetizzazione e parlanti non nativi. Il linguaggio semplice non è "abbassare il livello". Anche i lettori esperti preferiscono un testo chiaro ed efficiente.

### Progetta deliberatamente messaggi di errore, stati vuoti e valori predefiniti

Un messaggio di errore dovrebbe dire che cosa è andato storto, perché e come correggerlo, in linguaggio semplice, senza colpa e senza codici su cui l'utente non può agire. Conserva l'input dell'utente e metti il messaggio proprio dove sta il problema. Gli stati vuoti sono un'occasione di onboarding: spiega che cosa appartiene qui e come aggiungerlo, anziché mostrare un vuoto bianco. Scegli valori predefiniti utili e sicuri così che la maggior parte degli utenti riesca senza cambiare nulla e fai del valore predefinito l'opzione che serve l'interesse dell'utente, non solo quello dell'azienda.

### Progetta per fiducia e sicurezza; evita i dark pattern

Presenta le scelte con onestà e simmetria: annullare l'iscrizione dovrebbe essere facile quanto iscriversi e rifiutare dovrebbe essere prominente quanto accettare. Non usare il confirmshaming ("No grazie, non mi piace risparmiare"), il consenso preselezionato, i costi nascosti, l'urgenza falsa o i flussi a trappola facili da imboccare e difficili da lasciare. Oltre all'etica, molti di questi schemi sono ormai illegali secondo la legge sulla tutela dei consumatori e sulla privacy. Poni particolare cura nelle comunicazioni su sicurezza, privacy e denaro, perché è lì che la manipolazione fa più danno e dove i truffatori imitano i messaggi legittimi.

### Progetta in modo coerente le comunicazioni multicanale

Email, notifiche push, SMS e messaggi in-app fanno parte di un unico percorso. Coordinali così che gli utenti non siano sommersi né contraddetti tra i canali. Rispetta l'attenzione: notifica solo quando è tempestivo e utile, lascia che gli utenti controllino frequenza e canale e rendi ogni messaggio accessibile e semplice. Assicurati che le comunicazioni transazionali (ricevute, avvisi, scadenze) siano affidabili, chiare e difficili da confondere con il [phishing](https://en.wikipedia.org/wiki/Phishing): un'identità del mittente e una formattazione coerenti aiutano gli utenti a fidarsi dei messaggi genuini.

## Compromessi: vantaggi e svantaggi

| Decisione | Vantaggi | Svantaggi |
|---|---|---|
| Strategia dei contenuti centralizzata | Coerenza, fiducia, riuso | Onere, può rallentare i team se diventa un collo di bottiglia |
| Linguaggio semplice ovunque | Comprensione, inclusione, conformità legale | Sforzo di riscrittura; gli specialisti possono resistere a perdere il gergo |
| Voce giocosa e di marca | Personalità, memorabilità | Può sbagliare negli errori, nelle situazioni ad alta posta o con pubblici diversi |
| Valori predefiniti forti | La maggior parte degli utenti riesce senza sforzo | Rischio di spinte; vanno fissati nell'interesse dell'utente |
| Messaggistica multicanale ricca | Tempestiva, coinvolgente | Diventa facilmente rumore; onere di privacy e consenso |

La tensione centrale è tra personalità del marchio e chiarezza e tra coinvolgimento e rispetto dell'attenzione. Il contesto la risolve. Lascia che la voce aggiunga calore dove la posta è bassa e dai priorità a una chiarezza semplice e calma dove la posta è alta (errori, denaro, sicurezza, aspetti legali). Su valori predefiniti e messaggistica, la linea etica è semplice: il design serve l'interesse genuino dell'utente o sfrutta la sua disattenzione?

## Domande da discutere con il tuo team

1. **Messaggi di errore, stati vuoti e valori predefiniti sono schemi condivisi nel nostro design system, o reinventati a ogni schermata?** Sono i momenti a più alta leva di tutta l'esperienza: un buon errore dice che cosa è andato storto, perché e come correggerlo senza colpa né un codice su cui non si può agire e un buono stato vuoto insegna alle persone che cosa appartiene lì anziché mostrare un vuoto. Quando ogni team li scrive da zero ottieni "Error 500" in un posto e un messaggio utile in un altro e gli utenti perdono fiducia. Decidi se questi schemi vivono nel design system accanto ai componenti, con strutture concordate e testo di esempio. Porta tre veri messaggi di errore e tre stati vuoti dal tuo prodotto e leggili ad alta voce. Se uno incolpa l'utente o non offre alcun percorso di ripristino, hai trovato il tuo primo elemento di arretrato.

2. **Il nostro contenuto è strutturato e riutilizzabile, o scritto nel codice e duplicato tra le schermate?** Il testo digitato direttamente in un componente non può essere aggiornato in modo coerente, non può essere rivisto e non può essere localizzato senza una modifica del codice, il che blocca in silenzio ogni mercato futuro e ogni correzione di formulazione. Diventa acuto su larga scala, dove lo stesso concetto prende tre nomi perché non c'è glossario né fonte unica. Decidi come il contenuto è archiviato, chi possiede il vocabolario controllato e come una modifica di formulazione si propaga senza un rilascio per schermata. Porta un esempio di un termine che il tuo prodotto scrive o nomina in modo incoerente e ricostruisci in quanti posti dovresti modificarlo. Se la risposta è "cerca e sostituisci a mano", il tuo contenuto è intrappolato nel codice.

3. **Quando entrano nel flusso di lavoro i content designer, e chi ha l'autorità di bloccare un flusso manipolatorio?** Se il contenuto è un ripensamento (lorem ipsum fino al lancio, poi qualsiasi cosa stia nella casella) le parole che portano la maggior parte dell'esperienza ricevono meno riflessione e i dark pattern si infiltrano sotto la pressione della crescita perché nessuno possiede l'onestà. Concorda che il contenuto è un input di design fin dall'inizio, con una guida di voce e tono e una revisione nel flusso di lavoro, e nomina chi può fermare un flusso di confirmshaming o di consenso preselezionato prima che venga rilasciato. È ormai una questione legale oltre che etica, perché la legge sulla tutela dei consumatori e sulla privacy mette sempre più fuori legge questi schemi. Porta un flusso recente e chiediti se rifiutare sia facile e prominente quanto accettare. Se non lo è, decidi oggi chi è responsabile di correggerlo.

4. **A che livello di lettura stiamo davvero scrivendo, e come sappiamo che gli utenti reali capiscono il nostro contenuto a più alta posta?** Il linguaggio semplice è facile da dichiarare e difficile da provare: gli autori scrivono al proprio livello di comprensione e i lettori che più hanno bisogno di chiarezza, persone con minore alfabetizzazione e parlanti non nativi, sono i meno rappresentati nella stanza. Per una grande organizzazione la posta si compone, perché una lettera di prestazioni o un avviso di sicurezza confusi vengono copiati a milioni di destinatari prima che qualcuno misuri se arrivano. Decidi un livello di lettura obiettivo per l'intero pubblico, espandi o vieta il gergo alla prima occorrenza e impegnati in test di comprensione con persone reali anziché fidarti del solo punteggio di leggibilità. Porta le tue tre comunicazioni a più alto traffico e l'evidenza che qualcuno fuori dal team di redazione può agire correttamente su di esse. Nei contesti aziendali e governativi, aggiungi la legge o politica sul linguaggio semplice applicabile e sii onesto su quali documenti fallirebbero oggi un audit.

5. **Chi governa come, quando e con che frequenza messaggiamo gli utenti tra email, push, SMS e in-app, così che l'intero percorso resti coerente?** Quando ogni team possiede il proprio canale, gli utenti vengono sommersi, contraddetti e infine addestrati a ignorare o disiscriversi da tutto, compresi i messaggi transazionali che contano davvero. Coordinare il percorso significa concordare limiti di frequenza, dare agli utenti un vero controllo su canale e consenso e mantenere un'identità del mittente coerente così che i messaggi genuini siano difficili da confondere con il phishing che li imita. Porta un registro di ogni messaggio che un singolo utente potrebbe ricevere in una settimana intensa e conta i duplicati, le contraddizioni e quelli che potrebbero essere scambiati per una truffa. La spinta contraria è la pressione al coinvolgimento, poiché i team di crescita vogliono sempre un altro punto di contatto e il rispetto dell'attenzione non ha una metrica immediata. Nei contesti aziendali e governativi, aggiungi gli obblighi di consenso e privacy che trasformano la messaggistica non richiesta in esposizione legale e nomina chi può porre il veto a una campagna che abusa del canale.

6. **Come misuriamo se il nostro contenuto funziona, e dove la voce del marchio cede del tutto alla chiarezza semplice?** Il contenuto che non viene mai misurato deriva sul gusto e vince la formulazione la parte interessata che grida più forte anziché l'utente. Lega il contenuto a segnali reali, categorie dei ticket di assistenza, funnel di completamento e conversione, tassi di errore e ricorso e tassi di disiscrizione e reclamo, così che una riscrittura sia giudicata dall'esito anziché dalla preferenza. Allo stesso tempo, concorda dove la voce deve cedere: un errore spiritoso, un messaggio sul denaro scherzoso o un avviso di sicurezza giocoso erode la fiducia proprio quando la posta è più alta. Porta un flusso ad alto traffico, la metrica che muove e una proposta di linea tra dove la personalità aiuta e dove la chiarezza calma è obbligatoria. Per un'organizzazione grande o pubblica, nomina chi possiede quella linea e come un miglioramento provato si propaga tra i team, anziché vincere una schermata e perdere le altre.

## Lente settoriale

**Startup.** Senza uno scrittore e con due ingegneri, tratta il contenuto come un compito dei fondatori, non un'assunzione. Spendi un giorno sulle parole a più alta leva: dai ai pulsanti il nome della loro azione, trasforma il cruscotto vuoto in un tutorial di primo avvio e fai dire agli errori che cosa correggere. Scrivi una guida di voce di una pagina così che il tono resti semplice man mano che cresci e salta glossario e piattaforma dei contenuti finché l'incoerenza non fa davvero male.

**Piccola impresa.** Senza un content designer e con un budget ridotto, appoggiati alle convenzioni di linguaggio semplice e microcopy integrate negli strumenti che già usi e compra modelli per l'email transazionale anziché costruirli da zero. Dai priorità alle poche schermate che perdono clienti, uno stato vuoto, un errore al checkout, un flusso di cancellazione, e mantieni il rifiuto facile quanto l'accettazione così da stare lontano dalla legge sui dark pattern. Esegui un verificatore di leggibilità gratuito su tutto ciò che è rivolto ai clienti prima che venga rilasciato.

**Grande impresa.** Il problema è la coerenza tra molti team: una guida condivisa di voce e tono, un vocabolario controllato così che un concetto mantenga un nome e schemi di errore, stato vuoto e valore predefinito che vivano nel design system accanto ai componenti. Conserva il contenuto sotto controllo di versione, strutturato e localizzabile anziché scritto nel codice, dagli responsabili e revisione e coordina la messaggistica multicanale così che gli utenti non siano sommersi né contraddetti. Governa centralmente l'onestà così che nessun team rilasci confirmshaming o consenso preselezionato sotto pressione di crescita.

**Ente pubblico.** Il linguaggio semplice è spesso un dovere legale, non una preferenza, quindi segui gli standard applicabili e testa la comprensione con destinatari reali, comprese persone con minore alfabetizzazione e parlanti non nativi. Apri ogni avviso con l'azione e la scadenza, elimina il gergo e fai identificare chiaramente a ogni comunicazione il proprio mittente così che le persone non la scambino per una truffa. Mantieni oneste e simmetriche le scelte, pubblica gli standard di contenuto ai quali ti tieni e dai alle persone un percorso semplice per contestare una decisione che non capiscono.

## Esempi

**Startup.** Una piccola startup senza scrittori ha notato che la maggior parte degli utenti in prova si iscriveva, vedeva un cruscotto vuoto e non tornava mai più. Un fondatore ha speso un giorno a riscrivere il microcopy: lo stato vuoto ora spiegava che cosa aggiungere e offriva un progetto di esempio con un clic, i pulsanti nominavano la propria azione anziché dire "OK" e i messaggi di errore dicevano che cosa era andato storto e come correggerlo. L'attivazione è salita in modo evidente la settimana dopo e lo stesso fondatore ha scritto una guida di voce di una pagina così che l'intero team mantenesse il tono semplice e coerente man mano che cresceva.

**Grande impresa.** Un'azienda SaaS ha riscritto il proprio onboarding, i messaggi di errore e gli stati vuoti attorno a un microcopy chiaro e orientato all'azione e a una guida di voce documentata. I ticket di assistenza per domande "come faccio a..." sono calati, l'attivazione è migliorata perché gli stati vuoti ora insegnavano agli utenti che cosa fare e la conversione da prova a pagante è salita. L'azienda ha anche rimosso un flusso di cancellazione con confirmshaming dopo che aveva danneggiato la fiducia e attirato critiche, sostituendolo con un percorso di cancellazione semplice e simmetrico che, in modo controintuitivo, ha migliorato reputazione e riconquiste.

**Ente pubblico.** Un'agenzia ha riscritto una lettera di idoneità alle prestazioni che i destinatari fraintendevano di routine, causando appuntamenti mancati e perdita ingiusta di prestazioni. Applicando gli standard di linguaggio semplice, il team ha aperto con l'azione richiesta e la scadenza, ha tolto il gergo legale e ha testato la comprensione con destinatari reali, compresi parlanti non nativi. La comprensione è salita nettamente e i tassi di scadenze mancate sono calati, riducendo ricorsi e pratiche. Poiché la lettera ora identificava chiaramente se stessa e il proprio mittente, i destinatari erano anche meno propensi a scambiarla per una truffa.

## Business case: motivazioni, ROI e TCO

La qualità del contenuto guida esiti misurabili: maggiore completamento dei compiti e conversione, minor volume di assistenza, meno errori e ricorsi e maggiore fiducia e fidelizzazione. Un microcopy chiaro e valori predefiniti utili riducono il numero di persone che si bloccano e contattano l'assistenza o abbandonano. Le comunicazioni in linguaggio semplice riducono il costo a valle: meno chiamate confuse, meno errori da correggere, meno ricorsi nei contesti governativi. Un design affidabile e non manipolatorio protegge la reputazione e riduce l'esposizione legale man mano che la regolamentazione sui dark pattern si stringe.

Sul TCO, il costo di adozione è modesto: content designer o scrittori formati, una guida di voce e un glossario e la revisione nel flusso di lavoro. Il costo del non adottare è diffuso e grande: carico di assistenza e call center, transazioni abbandonate, correzione degli errori, ricorsi, sanzioni normative per schemi manipolatori o comunicazioni non conformi ed erosione della fiducia. Questi costi atterrano su assistenza e operazioni anziché sul bilancio del prodotto, quindi la leadership tende a sottopesarli.

Per presentare il caso, lega il lavoro sui contenuti alle categorie dei ticket di assistenza, ai funnel di completamento e conversione, ai tassi di errore e ricorso e ai tassi di disiscrizione o reclamo. Una piccola riscrittura di un flusso ad alto traffico o di una comunicazione ad alto volume di solito produce un miglioramento chiaro e attribuibile ed è ciò che giustifica scalare la pratica.

## Antipattern e insidie

- **Contenuto come ripensamento**: lorem ipsum fino al lancio, poi qualsiasi cosa stia nella casella.
- **Gergo e linguaggio interno**: scrivere dalla prospettiva dell'organizzazione, non dell'utente.
- **Errori che incolpano e non aiutano**: "Error 500" o "Input non valido" senza percorso di ripristino.
- **Stati vuoti bianchi**: un vuoto dove dovrebbe esserci una guida.
- **Dark pattern**: confirmshaming, consenso preselezionato, costi nascosti, flussi a trappola, urgenza falsa.
- **Terminologia incoerente**: tre nomi per un concetto nel prodotto.
- **Spam di notifiche**: sovra-messaggistica che addestra gli utenti a ignorare o disiscriversi.
- **Leggibilità non testata**: presumere che il contenuto sia chiaro senza testarlo con utenti reali.
- **Testo scritto nel codice e duplicato**: impossibile da aggiornare o localizzare in modo coerente.

## Modello di maturità

**Livello 1: Avvio.** Nessuna pratica sui contenuti. Le parole sono scritte ad hoc da chiunque costruisca la schermata, reagendo a ciò di cui la casella ha bisogno al momento. Terminologia e tono sono incoerenti, gli errori incolpano l'utente o mostrano codici su cui non si può agire e gli stati vuoti sono un vuoto bianco.

**Livello 2: Sviluppo.** Può esistere una guida di stile o qualche nota di voce e alcuni team hanno preso abitudini di linguaggio semplice. Il contenuto è ancora un'attività tardiva e per team con poco riuso e pochi test, quindi qualità e coerenza variano molto da una squadra all'altra.

**Livello 3: Standardizzazione.** Una strategia dei contenuti, una guida di voce e tono e un vocabolario controllato sono documentati e usati tra i team. Il linguaggio semplice è lo standard e, dove richiesto, conforme; errori, stati vuoti e valori predefiniti seguono schemi condivisi; il contenuto è strutturato, rivisto e riutilizzabile anziché scritto nel codice per schermata.

**Livello 4: Gestione.** Il contenuto è misurato rispetto agli esiti con dati. I risultati di leggibilità e test di comprensione, le categorie dei ticket di assistenza, i funnel di completamento e conversione, i tassi di errore e ricorso e i tassi di disiscrizione e reclamo sono seguiti rispetto a valori di riferimento e ogni modifica di contenuto è giudicata sul fatto che muova quei numeri. I dark pattern sono verificati rispetto a una politica documentata e la frequenza dei messaggi multicanale è monitorata rispetto a limiti concordati.

**Livello 5: Orchestrazione.** Il contenuto è migliorato di continuo e integrato nell'organizzazione. Gli schemi vivono nel design system, localizzati e accessibili per impostazione predefinita; il vocabolario controllato mantiene un nome per concetto ovunque; le comunicazioni multicanale sono coordinate e controllate dall'utente; e la pratica si adatta al mutare di regolamentazione, pubblico e canali, ritirando e riscrivendo il contenuto sull'evidenza anziché sull'opinione.

## Spunti di discussione

- Dove dovrebbe la voce del marchio cedere del tutto alla chiarezza semplice, e chi decide la linea?
- Come fate rispettare una politica senza dark pattern quando i team di crescita sono pressati sulle metriche?
- Come mantenete coerente la terminologia tra molti team senza strozzarli?
- Qual è il livello di lettura giusto per un servizio usato dall'intero pubblico?
- Come dovrebbero essere governati frequenza delle notifiche e controllo del canale nell'organizzazione?
- Come rendete le comunicazioni genuine distinguibili dal phishing che le imita?

## Punti chiave

- Il contenuto è UI centrale; progetta le parole con lo stesso rigore degli elementi visivi.
- Il linguaggio semplice migliora la comprensione per tutti ed è spesso richiesto per legge.
- Errori, stati vuoti e valori predefiniti sono momenti ad alta leva: progettali per aiutare.
- Evita i dark pattern: presenta le scelte con onestà e simmetria; sono sempre più illegali.
- Terminologia e tono coerenti costruiscono fiducia e riducono il carico cognitivo.
- Coordina le comunicazioni multicanale e rispetta attenzione e controllo dell'utente.
- La qualità del contenuto si vede direttamente in volume di assistenza, completamento, errori e fiducia.

## Riferimenti e letture di approfondimento

- Ginny Redish, *Letting Go of the Words*
- Torrey Podmajersky, *Strategic Writing for UX*
- Sarah Richards, *Content Design*
- Kristina Halvorson e Melissa Rach, *Content Strategy for the Web*
- Nicole Fenton e Kate Kiefer Lee, *Nicely Said*
- Erika Hall, *Conversational Design*
- Harry Brignull, *Deceptive Patterns* (ricerca sui dark pattern)
- U.S. Federal Plain Language Guidelines e PlainLanguage.gov
- UK Government Digital Service, indicazioni di content design e di stile
- Nielsen Norman Group, articoli su messaggi di errore, microcopy e leggibilità
