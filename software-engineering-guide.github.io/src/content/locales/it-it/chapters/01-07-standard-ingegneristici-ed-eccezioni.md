# 1.7 Standard ingegneristici ed eccezioni

## Panoramica e motivazioni

Uno **standard ingegneristico** è una regola documentata e concordata su come si svolge il lavoro. Per esempio, "tutti i servizi devono esporre un endpoint di controllo dello stato" oppure "tutte le pagine web pubbliche devono rispettare le **[WCAG](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (Web Content Accessibility Guidelines) 2.2 livello AA**". Uno standard non è un suggerimento e nemmeno una semplice convenzione. È un impegno che l'organizzazione prende con se stessa, idealmente verificabile. Questo capitolo riguarda l'intero ciclo di vita degli standard, come una grande organizzazione li **redige, pubblica, adotta, fa rispettare e fa evolvere** e, altrettanto importante, come gestisce i casi che legittimamente ne restano fuori attraverso un **processo di eccezioni** governato (detto anche **processo di deroga**): un permesso documentato e a tempo di discostarsi da uno standard per una ragione dichiarata.

La motivazione è che su larga scala le norme informali smettono di funzionare. Quando cinque ingegneri condividono una stanza, "come si fanno le cose qui" viaggia per conversazione e osmosi. Quando cinquemila ingegneri sono distribuiti su decine di team, tre fusi orari e un decennio di ricambio del personale, quella conoscenza tacita si frammenta in centinaia di abitudini locali incompatibili. Gli standard sono il modo di scrivere una volta sola le lezioni faticosamente apprese, così che ogni team le erediti anziché reimparare ciascuna attraverso la propria interruzione di servizio. Riducono il [carico cognitivo](https://en.wikipedia.org/wiki/Cognitive_load), rendono le [revisioni del codice](https://en.wikipedia.org/wiki/Code_review) una questione di sostanza anziché di stile, permettono alle persone di spostarsi tra team e danno ad auditor e regolatori qualcosa di concreto da valutare.

Ma gli standard portano con sé una propria modalità di fallimento: la rigidità. Uno standard che non ammette eccezioni finirà prima o poi per bloccare lavoro legittimo: uno spike, un vincolo di un fornitore, un caso davvero nuovo che gli autori non avevano immaginato. I team allora si fermano oppure, peggio, ignorano in silenzio lo standard, il che corrode la credibilità di *ogni* standard. Il rimedio è il vecchio aforisma "l'eccezione conferma la regola". Un processo di eccezioni visibile e fondato su principi è ciò che mantiene gli standard sia credibili sia umani. Questo capitolo si basa su decisioni e governance (capitolo 1.5) e registri delle decisioni (capitolo 1.6), e alimenta direttamente standard di codifica e stile (capitolo 2.1), liste di controllo (capitolo 12.2) e modelli (capitolo 12.3).

## Principi chiave

- **Uno standard enuncia un risultato e ne dà il motivo.** Regola più motivazione; senza il *perché*, le persone non sanno giudicare quando si applica davvero.
- **Se non si può verificare, non è ancora uno standard.** Preferisci affermazioni verificabili alle aspirazioni.
- **Gli standard sono documenti vivi.** Sono versionati, con un responsabile, datati e rivisti, non scolpiti nella pietra e abbandonati.
- **Automatizza l'applicazione dove puoi; riserva la revisione umana al giudizio.** Le macchine controllano il meccanico; le persone controllano ciò che ha significato.
- **Le deviazioni sono attese, non vergognose, ma devono essere visibili.** Una deroga onesta batte sempre la non conformità silenziosa.
- **Metti un limite di tempo a ogni eccezione.** Un'eccezione permanente è un difetto dello standard; portalo alla luce e correggi lo standard.
- **Parole ed esempi al posto di gergo e imposizioni.** Le persone seguono gli standard che capiscono e da cui possono copiare.

## Raccomandazioni

### Scrivi standard chiari, verificabili e motivati

Un buon standard è un breve documento autosufficiente con una forma prevedibile, così che i lettori sappiano dove guardare. Adotta un unico **modello di standard** (capitolo 12.3) e usalo ovunque. Le sezioni essenziali comprendono:

- **Titolo e identificatore:** un nome stabile e un numero di riferimento per la citazione.
- **Stato:** bozza, attivo, superato o ritirato, con una data.
- **La regola:** enunciata come risultato, in modo chiaro e inequivocabile ("deve", "dovrebbe", "può", usati con deliberazione, secondo le convenzioni **RFC 2119** per le parole chiave dei requisiti).
- **Motivazione:** *perché* questa regola esiste; il costo o il rischio che previene.
- **Esempi:** un esempio conforme e uno non conforme; il concreto batte l'astratto.
- **Come viene verificato:** il test automatico, la regola del linter o il passaggio di revisione che lo verifica.
- **Responsabile e data di revisione:** chi lo mantiene e quando verrà riesaminato.

La motivazione e il campo "come viene verificato" sono ciò che separa uno standard vero da un desiderio. Se non sai dire perché una regola esista, chiediti se debba esistere. Se non sai dire come si verifichi la conformità, la regola verrà applicata in modo incoerente e mal sopportata.

### Abbina a ogni standard una lista di controllo di buone pratiche

Gli standard definiscono la destinazione. Una **lista di controllo di buone pratiche**, un breve elenco ordinato di passaggi concreti o voci da confermare, aiuta le persone ad arrivarci e permette loro di autoverificarsi prima della revisione. I manuali ingegneristici del settore pubblico usano molto questo schema. **[NHS Wales](https://en.wikipedia.org/wiki/NHS_Wales)** e **Digital Health and Care Wales (DHCW)** pubblicano standard ingegneristici con liste di controllo pratiche, e il **[Government Digital Service](https://en.wikipedia.org/wiki/Government_Digital_Service) (GDS) del Regno Unito** abbina il proprio Service Standard e il Technology Code of Practice alle indicazioni operative del Service Manual. La lista di controllo è lo standard reso utilizzabile: "Hai aggiunto un audit di accessibilità? Hai provato con uno screen reader? Hai coperto la navigazione solo da tastiera?" Vedi il capitolo 12.2 per lo schema delle liste di controllo per intero.

### Pubblica gli standard dove le persone già lavorano e mantienili reperibili

Conserva gli standard nel **[controllo di versione](https://en.wikipedia.org/wiki/Version_control)** (un repository di sorgenti) come Markdown, resi in un sito interno ricercabile, così che abbiano gratis storia, revisione tramite pull request e confronto delle differenze, lo stesso argomento dei registri delle decisioni (capitolo 1.6). Un solo catalogo, un solo modello, una sola casella di ricerca. Portare in superficie conta quanto conservare. Collega lo standard pertinente dal modello della pull request, dal messaggio d'errore del linter e dallo scheletro del servizio, così che la regola giusta compaia nel momento del lavoro anziché in una cartella che nessuno visita.

### Applica prima con l'automazione, poi con la revisione umana

Esistono due modi di far rispettare uno standard, e le organizzazioni mature li usano entrambi con deliberazione:

- **Applicazione automatica:** [linter](https://en.wikipedia.org/wiki/Lint_(software)), formattatori, [analisi statica](https://en.wikipedia.org/wiki/Static_program_analysis), policy-as-code (per esempio **Open Policy Agent (OPA)**), controlli nell'**[integrazione continua](https://en.wikipedia.org/wiki/Continuous_integration) (CI)** e **fitness function architetturali** (test automatici che asseriscono che una proprietà di progetto sia ancora valida). L'automazione è coerente, instancabile, immediata e incontestabile, il che la rende ideale per la maggioranza meccanica degli standard (formattazione, nomi, regole sulle dipendenze, metadati obbligatori).
- **Revisione umana:** revisione del codice, comitati di revisione architetturale e revisione della sicurezza, riservate a ciò che le macchine non sanno giudicare: se un'astrazione è solida, se un compromesso è saggio, se l'*intento* di uno standard è rispettato anche quando la sua lettera è scomoda.

La regola pratica: **automatizza ciò che si può verificare e spendi la scarsa attenzione umana sul giudizio.** Ogni standard che riesci a spostare dalla revisione alla CI libera i revisori per fare il ragionamento che solo loro sanno fare.

### Governa le deviazioni con un processo documentato di eccezioni e deroghe

Nessuno standard si adatta a ogni caso, quindi progetta la via di fuga di proposito. Un buon processo di eccezioni specifica:

- **Chi può concedere una deroga:** un'autorità nominata e responsabile, proporzionata al rischio (un tech lead per una deviazione di stile a bassa posta; un comitato di architettura o sicurezza per la deroga a un controllo di sicurezza). Questo si lega direttamente al modello di governance del capitolo 1.5.
- **Che cosa deve essere registrato:** lo standard da cui ci si discosta, la ragione specifica, l'ambito, i controlli compensativi o le mitigazioni e il rischio accettato. Cattura tutto come registro delle decisioni (capitolo 1.6), così che la motivazione sia conservata.
- **Una scadenza obbligatoria:** ogni deroga è **a tempo**, con una data di fine esplicita. È la regola singola più importante: impedisce che un'eccezione temporanea diventi in silenzio una politica permanente.
- **Revisione periodica:** un responsabile rivede le deroghe aperte con una cadenza e le rinnova con nuova giustificazione, le chiude quando il lavoro è conforme o, se la stessa eccezione continua a ripresentarsi, lo considera una prova che *lo standard stesso* è sbagliato e lo rivede.

Quest'ultimo punto è il cuore di "l'eccezione conferma la regola". Un flusso costante di deroghe contro un solo standard non è un fallimento di disciplina. È un dato. Ti dice che lo standard è tarato male, e il rimedio è far evolvere lo standard, non continuare a concedere eccezioni.

### Tratta gli standard come documenti vivi con una responsabilità chiara

Dai a ogni standard un **responsabile** (un ruolo, non solo una persona) incaricato di tenerlo aggiornato e una **cadenza di revisione** (almeno annuale). Offri un percorso leggero perché chiunque possa proporre una modifica tramite una pull request o una **[RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (request for comments)**, una proposta scritta fatta circolare per ricevere feedback prima dell'adozione. Versiona gli standard, depreca-li in modo esplicito e annuncia i cambiamenti. Un catalogo di standard mai rivisto marcisce in folklore che le persone citano a proprio comodo e di cui si fidano poco.

## Compromessi: vantaggi e svantaggi

| Scelta | Vantaggi | Svantaggi |
|---|---|---|
| **Molti standard dettagliati** | Coerenza, inserimento facile, pronti per l'audit | Rigidità; onere di manutenzione; possono superare la pratica |
| **Pochi standard di alto livello** | Flessibili; poca manutenzione | Incoerenza; più ridiscussioni per team |
| **Applicazione automatica** | Coerente, immediata, instancabile, scalabile | Costo iniziale; falsi positivi; cieca all'intento |
| **Applicazione tramite revisione umana** | Giudica intento e sfumature | Lenta, incoerente, un collo di bottiglia su larga scala |
| **Rigidi, nessuna eccezione** | Messaggio semplice; niente da aggirare | Blocca il lavoro legittimo; spinge alla non conformità silenziosa |
| **Processo di eccezioni governato** | Mantiene gli standard credibili e umani | Richiede governance, registri e coerenza di seguito |

La tensione centrale è tra **coerenza e flessibilità**. Uno standard esiste per rimuovere la variazione; un processo di eccezioni esiste per ammettere la variazione davvero giustificata. Se ti sbilanci troppo verso la rigidità, le persone aggirano i tuoi standard. Se ti sbilanci troppo verso la lassità, gli standard non significano nulla. Il processo di eccezioni è la valvola di sfogo che ti permette di tenere una linea ferma *e* di restare onesto sulla realtà.

## Domande da discutere con il tuo team

1. **Qual è il numero giusto di standard per la vostra scala, e i vostri stanno scivolando verso la rigidità o verso l'incoerenza?** Il catalogo stesso è un compromesso: molti standard dettagliati comprano coerenza, inserimento facile e prontezza all'audit a costo di rigidità e onere di manutenzione, mentre pochi standard di alto livello restano flessibili ma lasciano che ogni team rimetta in discussione le stesse questioni. Per una grande impresa o un ente pubblico, la dimensione giusta dipende da quanta variazione potete davvero tollerare rispetto a quanto i vostri auditor e il vostro inserimento hanno bisogno di fissare. Porta prove: quanti standard attivi avete, quanti sono stati rivisti nell'ultimo anno e quanto spesso i team ridiscutono cose che uno standard avrebbe potuto risolvere. Un catalogo che supera la pratica diventa folklore, e uno troppo scarno scarica il costo su ogni team. Decidi con deliberazione che cosa merita uno standard e pota quelli che non si guadagnano più il posto.

2. **Dove la lettera di uno standard passa in automatico mentre il suo intento viene violato in silenzio, e come lo individuerete?** L'automazione è coerente, instancabile e cieca all'intento, il che significa che un linter o un controllo di policy può diventare verde mentre l'obiettivo vero (un'astrazione solida, un compromesso saggio, una pagina davvero accessibile) viene mancato. La regola pratica è automatizzare ciò che si può verificare e spendere la scarsa revisione umana sul giudizio, e la parte difficile è concordare quali standard hanno un intento che nessun controllo di CI può asserire. Porta esempi: standard che le persone soddisfano alla lettera vanificandone lo scopo, come un endpoint di controllo dello stato che segnala "sano" mentre il servizio è guasto, o codice che passa il formattatore ma ne oscura il significato. Negli ambienti regolamentati l'intento conta di più per i controlli di sicurezza, dove una casella verde può nascondere un rischio reale. Decidi quali standard conservano un revisore umano specificamente per giudicare l'intento, e formula quegli standard attorno al risultato, così che macchina e revisore puntino allo stesso bersaglio.

3. **Chi possiede il ciclo di retroazione dalla deroga allo standard, e a che punto un'eccezione ricorrente vi costringe a cambiare la regola?** Un flusso costante di deroghe contro un solo standard è un dato, non indisciplina, e il segnale va sprecato se nessuno è responsabile di leggerlo e di agire. La considerazione contraria è che rivedere uno standard è lavoro vero, quindi resta più facile continuare ad approvare meccanicamente le deroghe che correggere la regola mal tarata che sta sotto. Porta i numeri: quali standard generano più eccezioni, se le deroghe sono davvero a tempo e riviste con una cadenza e quante sono diventate in silenzio permanenti. Per gli standard critici per la sicurezza fisica e per la sicurezza informatica in imprese ed enti pubblici, una deroga deve registrare controlli compensativi, una mitigazione, il rischio accettato e una scadenza rigida, altrimenti una deviazione temporanea diventa una politica non documentata che emerge al successivo audit. Assegna un responsabile alla revisione delle deroghe aperte, fissa una soglia oltre la quale eccezioni ripetute innescano una revisione dello standard e tratta un'eccezione permanente come un difetto dello standard da correggere.

4. **La regola giusta compare nel momento del lavoro, o vive in una cartella che nessuno apre?** Uno standard che nessuno riesce a trovare viene applicato per fortuna, e su larga scala la maggior parte della non conformità non è sfida ma ignoranza: un ingegnere non sapeva che la regola esistesse o non riusciva a trovarla quando serviva. La considerazione contraria è lo sforzo, poiché portare in superficie uno standard nel modello della pull request, nel messaggio d'errore del linter e nello scheletro del servizio costa un vero lavoro di integrazione che un singolo sito centrale non richiede. Porta prove sulla reperibilità: come gli ingegneri trovano oggi gli standard, se un nuovo assunto riesce a trovare in meno di un minuto la regola di accessibilità o sicurezza che governa il suo compito e quanto spesso i revisori citano uno standard che l'autore semplicemente non aveva visto. Per una grande impresa o un ente pubblico, gli auditor chiedono sempre più spesso non solo se uno standard esista, ma se sia stato comunicato e fosse accessibile nel punto della decisione, quindi tratta il portarlo in superficie come parte dello standard, non come un ripensamento, e misura se le persone riescono a raggiungere la regola quando ne hanno bisogno.

5. **Chi possiede ogni standard attivo, quando è stato rivisto per l'ultima volta e come individuereste quelli che sono marciti in silenzio in folklore?** Gli standard decadono in silenzio: una regola scritta tre anni fa per un framework che non usate più resta nel catalogo, citata a proprio comodo e poco creduta, trascinando giù la credibilità degli standard che sono ancora giusti. Per una grande organizzazione il costo della responsabilità è la cadenza di revisione stessa, che sembra un onere finché un'interruzione o un audit non espone uno standard che non corrisponde più alla realtà. Porta alla discussione i numeri: quanti standard hanno un responsabile nominato (un ruolo, non solo una persona ormai andata via), quanti sono stati rivisti nell'ultimo anno, quanti sono formalmente deprecati rispetto a semplicemente stantii e quali sono i più e i meno citati. Nei contesti aziendali e governativi, un auditor si aspetta che ogni standard sia versionato, datato e dimostrabilmente aggiornato, quindi concorda una cadenza minima di revisione, assegna a ogni standard un responsabile e ritira quelli che non si guadagnano più il posto prima che mettano a rischio la fiducia nel resto.

6. **L'autorità di concedere una deroga è davvero proporzionata al rischio dello standard derogato?** Una deviazione di stile e una deviazione da un controllo di sicurezza non sono la stessa decisione, eppure molte organizzazioni instradano entrambe a un comitato pesante (che blocca il lavoro legittimo) o le lasciano passare entrambe da un solo tech lead (che permette a un rischio serio di essere accettato da qualcuno senza il mandato di accettarlo). La tensione è tra velocità e responsabilità: troppo attrito di approvazione spinge alla non conformità silenziosa, mentre troppo poco significa che deviazioni importanti passano in una conversazione in chat. Porta una mappa dei tuoi standard con le relative autorità di approvazione, più un campione di deroghe concesse di recente, e controlla se qualcuno ha derogato a un controllo critico per la sicurezza fisica o informatica senza il comitato corrispondente, il controllo compensativo, la mitigazione e l'accettazione del rischio registrata. Per imprese ed enti pubblici è una questione di separazione dei compiti che i regolatori esaminano direttamente, quindi collega ogni classe di standard a un'autorità nominata e proporzionata al rischio, e assicurati che la persona che accetta un rischio sia davvero responsabile delle conseguenze.

## Lente settoriale

**Startup.** Mantieni minuscolo il catalogo: scrivi solo la manciata di regole la cui assenza ti farebbe davvero male, come una configurazione del formattatore, un requisito di controllo dello stato e pagine navigabili da tastiera, e fai rispettare ciascuna con un linter o un controllo di CI anziché con una riunione di revisione. Salta del tutto il comitato per le deroghe; un TODO datato nel codice e una nota di una riga nella pull request è una perfetta eccezione a tempo a questa scala. La tua risorsa più scarsa è l'attenzione ingegneristica, quindi resisti a redigere standard per problemi che non hai ancora.

**Piccola impresa.** Senza un responsabile degli standard dedicato e con un budget ridotto, compra i tuoi standard anziché costruirli: adotta riferimenti pubblicati come il Service Standard del GDS britannico, le indicazioni di sicurezza OWASP o le regole di lint raccomandate dal tuo framework, e appoggiati ai controlli già integrati nei tuoi strumenti e nella CI ospitata. Tieni una breve pagina di regole locali per le poche cose davvero specifiche per te. Chi guida l'ingegneria concede e registra le eccezioni nel ticket, con una data di scadenza, così che anche un processo leggero resti onesto.

**Grande impresa.** Il lavoro è la governance tra molti team: un catalogo, un modello, motivazione ed esempi per ogni standard e policy-as-code che fa fallire la pipeline per la maggioranza meccanica. Conduci un processo di deroghe la cui autorità di approvazione sia proporzionata al rischio, metti un limite di tempo a ogni eccezione, rivedi con una cadenza le deroghe aperte ed estrai dalle deroghe ricorrenti il segnale che uno standard deve cambiare. Misura la quota di standard applicati in automatico e il volume e l'età delle deroghe aperte, e riferisci entrambi alla funzione di governance, così che gli standard restino un sistema gestito anziché un cimitero.

**Ente pubblico.** Pubblica apertamente i tuoi standard ingegneristici nella tradizione di DHCW e GDS, e abbina a ciascuno una lista di controllo che i team completano prima di una valutazione del servizio, così che la conformità sia visibile al pubblico e agli organi di vigilanza. Fai di un responsabile senior nominato l'autorità per le deroghe importanti e richiedi che ogni eccezione registri il criterio specifico, il controllo compensativo o la mitigazione provvisoria, un piano di rimedio e una scadenza rigida. Le regole sugli appalti e sulla trasparenza fanno sì che sia i tuoi standard sia le tue deviazioni diventino parte della documentazione pubblica, quindi tratta verificabilità e tracciabilità come requisiti di progetto fin dall'inizio.

## Esempi

**Startup.** Una startup di sette persone tiene esattamente tre standard scritti (una configurazione condivisa del formattatore, un requisito di endpoint di controllo dello stato e "tutte le pagine pubbliche devono essere navigabili da tastiera"), ciascuno fatto rispettare da un linter o da un controllo di CI anziché da una riunione di revisione. Quando un'ingegnera deve rilasciare un prototipo usa e getta che viola la regola del controllo dello stato, non esiste un comitato per le deroghe: lascia un TODO datato nel codice e una nota di una riga nella pull request che spiega perché e quando lo correggerà. È un'eccezione a tempo su scala di startup, onesta e visibile senza alcun onere di processo. I tre controlli si ripagano da soli mantenendo la revisione del codice sulla sostanza anziché sullo stile.

**Grande impresa.** Una banca globale mantiene un manuale ingegneristico interno di circa quaranta standard attivi, ciascuno in un unico modello con motivazione, esempi e una lista di controllo di buone pratiche collegata. Circa il 70% è fatto rispettare in automatico: formattazione, politica sulle dipendenze, metadati obbligatori dei servizi e controlli di sicurezza codificati come policy-as-code che fa fallire la pipeline di CI. Un team dei pagamenti deve rilasciare su un database che non supporta ancora una funzione di cifratura obbligatoria. Anziché bloccare il rilascio, presenta una deroga che indica lo standard, il controllo compensativo ([cifratura](https://en.wikipedia.org/wiki/Encryption) a livello applicativo) e una scadenza a 90 giorni. Il comitato di sicurezza la concede e la registra. Novanta giorni dopo, la revisione scopre che la piattaforma ora supporta la funzione in modo nativo e la deroga viene chiusa. Lo standard ha tenuto, il lavoro è stato rilasciato e la deviazione è pienamente tracciabile per il prossimo audit.

**Ente pubblico.** Un'agenzia sanitaria nazionale ispirata all'approccio di DHCW e GDS pubblica apertamente i propri standard ingegneristici, ciascuno abbinato a una lista di controllo che i team completano prima di una valutazione del servizio. L'accessibilità secondo WCAG 2.2 AA è uno standard rigido, fatto rispettare da un audit automatico nella CI più una valutazione manuale. Un sistema clinico legacy non può soddisfare subito un criterio di accessibilità senza rischiare funzioni critiche per la sicurezza dei pazienti. Il team chiede un'eccezione a tempo. Un responsabile senior nominato la concede e registra il criterio specifico, la mitigazione provvisoria (una linea telefonica di accesso assistito), il piano di rimedio e una scadenza di sei mesi, creando esattamente l'evidenza tracciabile e rivedibile che gli organi di vigilanza richiedono (capitoli 4.6, 10.4).

## Business case: motivazioni, ROI e TCO

Uno standard costa il tempo per scriverlo, automatizzarne il controllo e mantenerlo. Il ritorno si incassa ogni volta che il controllo viene eseguito e ogni volta che un ingegnere non deve fermarsi a dibattere una questione risolta. Gli standard convertono un costo decisionale ricorrente e distribuito in un costo di redazione una tantum, la stessa economia dei registri delle decisioni (capitolo 1.6), amplificata perché uno standard governa migliaia di casi futuri, non una singola scelta passata.

Sul **costo totale di proprietà (TCO)**, cioè il costo complessivo lungo la vita di costruire, gestire e mantenere un sistema, gli standard abbassano le voci più grandi: inserimento (i nuovi assunti ereditano la coerenza anziché ricostruirla a ritroso), manutenzione (il codice uniforme costa meno da modificare) e garanzia (gli audit costano meno quando la conformità è verificabile da una macchina e le deviazioni sono già documentate). Il processo di eccezioni protegge quel ROI dalla sua minaccia principale: gli standard che degenerano in folklore ignorato. Un processo di deroghe credibile mantiene gli standard affidabili, e gli standard affidabili sono quelli che le persone seguono davvero. Il costo di saltare tutto questo è invisibile su qualsiasi cruscotto. Si manifesta come inserimento lento, qualità incoerente e rilievi di audit, e si accumula a ogni nuovo team e a ogni partenza.

## Antipattern e insidie

- **Regole senza motivazione:** uno standard che nessuno capisce è uno standard che nessuno sa applicare correttamente né contestare onestamente.
- **Standard aspirazionali e non verificabili:** "il codice dovrebbe essere manutenibile" è un valore, non uno standard; non si può far rispettare né contestare.
- **Nessun processo di eccezioni:** impone una falsa scelta tra bloccare il lavoro legittimo e tollerare la non conformità silenziosa.
- **Eccezioni permanenti:** deroghe senza scadenza che diventano in silenzio la vera politica, non documentata.
- **Deroghe senza registro:** deviazioni concesse in un corridoio o in una chat, invisibili al prossimo audit e al prossimo ingegnere.
- **Ignorare il segnale:** concedere ripetutamente la stessa eccezione invece di leggerla come prova che lo standard deve cambiare.
- **Applicazione a forza di insistenza:** affidarsi ai revisori per cogliere ciò che dovrebbe cogliere un linter, sprecando il giudizio sul meccanico.
- **Cimitero degli standard:** un catalogo scritto una volta, senza responsabile, mai rivisto, citato a proprio comodo e creduto da pochi.
- **Guardiania del gergo:** standard scritti per i loro autori anziché per i lettori, senza esempi da copiare.

## Modello di maturità

- **Livello 1 (Avvio):** gli standard sono conoscenza tribale nelle teste degli ingegneri senior, applicata in modo reattivo. L'applicazione è un insistere occasionale in revisione del codice; le deviazioni sono invisibili; "il modo in cui lo facciamo" varia da team a team e da chi ha rivisto la modifica.
- **Livello 2 (Sviluppo):** alcuni standard sono messi per iscritto, in formati incoerenti e in posti sparsi, e l'adozione varia molto da team a team. L'applicazione è per lo più manuale. Le eccezioni avvengono in modo informale, senza registri né date di scadenza.
- **Livello 3 (Standardizzazione):** un solo catalogo, un solo modello, motivazione ed esempi per ogni standard e liste di controllo di buone pratiche, applicati in modo coerente tra i team. Applicazione automatica per la maggioranza meccanica. Un processo di eccezioni documentato, con approvatori nominati, motivazione registrata e deroghe a tempo.
- **Livello 4 (Gestione):** il sistema degli standard è misurato rispetto a valori di riferimento. Si seguono la quota di standard applicati in automatico rispetto a quelli applicati dalla revisione umana, il volume di deroghe per standard, il tempo di chiusura e quante deroghe sono scadute pur restando aperte, e si riferiscono questi dati alla funzione di governance. L'autorità di approvazione è proporzionata al rischio e sottoposta ad audit; la cadenza di revisione e la scadenza sono fatte rispettare sulla base delle prove anziché della buona volontà; uno standard il cui tasso di deroghe supera una soglia concordata è segnalato per la revisione.
- **Livello 5 (Orchestrazione):** gli standard sono portati in superficie nel momento del lavoro e fatti rispettare da policy-as-code e fitness function. Le deroghe sono estratte come segnale, così che le eccezioni ricorrenti guidino di continuo l'evoluzione degli standard, e il catalogo è riequilibrato al mutare della pratica. Standard, liste di controllo e deroghe sono un unico sistema vivo e adattivo integrato in inserimento, consegna e audit.

## Spunti di discussione

1. Quali dei vostri standard sapete enunciare con una regola verificabile *e* una motivazione chiara, e quali sono in realtà solo aspirazioni?
2. Quale quota dei vostri standard è fatta rispettare in automatico rispetto a un revisore che se ne accorge? Che cosa servirebbe per spostarne dieci in più nella CI?
3. Dove avvengono oggi le deviazioni, e lo sapreste? Sono registrate e a tempo, o silenziose?
4. Chi può concedere una deroga al vostro standard più critico per la sicurezza fisica o informatica, e quell'autorità è proporzionata al rischio?
5. Guardate il vostro standard più derogato. È un problema di disciplina, o lo standard è semplicemente sbagliato?
6. Quando è stato rivisto per l'ultima volta ogni standard attivo, e chi lo possiede? Quali sono diventati in silenzio folklore?

## Punti chiave

- Uno standard ingegneristico è una **regola enunciata come risultato, con una motivazione, esempi e un modo per verificarla**: se non si può verificare, non è ancora uno standard.
- Abbina a ogni standard una **lista di controllo di buone pratiche**, perché le persone possano autoverificarsi, secondo lo schema dei manuali del settore pubblico (NHS Wales / DHCW, GDS britannico).
- Conserva gli standard nel **controllo di versione**, mantienili **vivi** con responsabili nominati e date di revisione e portali in superficie nel momento del lavoro.
- **Automatizza ciò che si può verificare** con linter, policy-as-code e fitness function; riserva la **revisione umana** al giudizio.
- Governa le deviazioni con un **processo di eccezioni e deroghe documentato e a tempo**: approvatore nominato, motivazione registrata, scadenza obbligatoria, revisione periodica.
- Un'eccezione ricorrente è un **segnale per correggere lo standard**, non solo per continuare a concedere deroghe: "l'eccezione conferma la regola". Vedi i capitoli 1.5 (governance), 1.6 (registri delle decisioni), 2.1 (standard di codifica), 12.2 (liste di controllo) e 12.3 (modelli).

## Riferimenti e letture di approfondimento

- UK Government Digital Service, *Government Service Standard*, *Technology Code of Practice* e *GOV.UK Service Manual*.
- NHS Digital / NHS England, *Service Standard* e indicazioni ingegneristiche.
- Digital Health and Care Wales (DHCW) / NHS Wales, standard ingegneristici pubblicati e liste di controllo di buone pratiche.
- Scott Bradner, *RFC 2119: Key Words for Use in RFCs to Indicate Requirement Levels* (IETF, 1997).
- World Wide Web Consortium (W3C), *Web Content Accessibility Guidelines (WCAG) 2.2*.
- Neal Ford, Rebecca Parsons e Patrick Kua, *Building Evolutionary Architectures* (le fitness function come governance automatizzata).
- Torin Sandall et al., documentazione di *Open Policy Agent* (policy-as-code).
- GitLab, *The GitLab Handbook*: un esempio pubblico di standard organizzativi vivi e sotto controllo di versione.
- Google, *Software Engineering at Google* (Winters, Manshreck, Wright): standard, leggibilità e applicazione automatizzata su larga scala.
- Atul Gawande, *The Checklist Manifesto*: il caso a favore delle liste di controllo come pratica professionale.
