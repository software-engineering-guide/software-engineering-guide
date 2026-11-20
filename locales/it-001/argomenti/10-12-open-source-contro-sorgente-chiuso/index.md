# 10.12 Open source contro sorgente chiuso

## Panoramica e motivazioni

Quasi ogni sistema moderno è una miscela di software che hai scritto, software che hai comprato e software che hai preso gratis. Due di quei tre portano con sé una scelta fondamentale: il software è **open source** o **a sorgente chiuso**? Il **[software open source](https://en.wikipedia.org/wiki/Open-source_software) (OSS)** è distribuito con una licenza che concede a chiunque il diritto di usare, studiare, modificare e ridistribuire il codice sorgente, le istruzioni leggibili dall'uomo che definiscono il programma. Il **software a sorgente chiuso**, detto anche **[software proprietario](https://en.wikipedia.org/wiki/Proprietary_software)**, è distribuito come prodotto finito il cui codice sorgente il fornitore tiene privato. Ottieni il diritto di eseguirlo con una licenza, ma non di ispezionare né cambiare come funziona. Una categoria intermedia, il **[software a sorgente disponibile](https://en.wikipedia.org/wiki/Source-available_software)**, pubblica il sorgente da leggere ma limita uso, modifica o ridistribuzione. È *visibile* ma non *aperto* secondo la definizione standard.

Due chiarimenti contano prima di confrontarli. Primo, "libero" è ambiguo. La comunità distingue il **libero come libertà** (la libertà di modificare e condividere, a volte scritta "libre") dal **libero come prezzo** (costo zero, "gratis"). L'open source riguarda la libertà, non necessariamente il prezzo. Secondo, le licenze open source si dividono in due famiglie. Le **[licenze permissive](https://en.wikipedia.org/wiki/Permissive_software_license)** (come [MIT](https://en.wikipedia.org/wiki/MIT_License), BSD e Apache 2.0) ti lasciano fare quasi tutto, compreso incorporare il codice in un prodotto chiuso. Le licenze **[copyleft](https://en.wikipedia.org/wiki/Copyleft)** (come la [GNU General Public Licence](https://en.wikipedia.org/wiki/GNU_General_Public_License), GPL) richiedono che anche le opere derivate che distribuisci siano rilasciate con gli stessi termini aperti, una regola di reciprocità a volte chiamata "virale" dai critici e "condividi allo stesso modo" dai sostenitori.

Questo capitolo guarda la scelta da due lati. Come **consumatore**, decidi se adottare un componente open source o proprietario. Come **produttore**, decidi se rendere open source il software che hai costruito. Per le grandi imprese e specialmente per il governo, entrambe le decisioni portano un peso molto oltre il file di licenza. Toccano appalti (capitolo 10.3), sovranità digitale (capitolo 10.11), sicurezza della supply chain (capitolo 4.2), interoperabilità (capitolo 3.8) e il calcolo di costruire o comprare (capitolo 6.1).

## Principi chiave

- **È la licenza, non il prezzo, a definire "aperto".** Leggi la licenza; gratuito e open source sono affermazioni diverse.
- **Nessun modello è intrinsecamente più sicuro.** Entrambi possono essere eccellenti o negligenti; le pratiche attorno al codice contano più della sua apertura.
- **L'apertura è una leva di riduzione della dipendenza.** L'accesso al sorgente è la protezione definitiva contro il [lock-in sul fornitore](https://en.wikipedia.org/wiki/Vendor_lock-in).
- **Possiedi sempre l'onere operativo.** Gratis da acquisire non è mai gratis da gestire; il [costo totale di proprietà](https://en.wikipedia.org/wiki/Total_cost_of_ownership) racconta la storia vera.
- **I differenziatori restano chiusi; le commodity possono aprirsi.** Rendi open source ciò che non ti distingue; proteggi ciò che lo fa.
- **Il copyleft ha conseguenze.** Capisci gli obblighi di reciprocità prima di incorporare codice copyleft in un prodotto che distribuisci.
- **Una comunità viva è una risorsa; un repository abbandonato è una passività.** Giudica il progetto, non solo la licenza.

## Raccomandazioni

### Valuta un componente sul progetto, non solo sulla licenza

Prima di adottare qualsiasi dipendenza, open source o proprietaria, valuta la sua salute: cadenza dei rilasci, numero e diversità dei manutentori, reattività alle segnalazioni di sicurezza e ampiezza di adozione. Una libreria open source con un solo manutentore e un piccolo fornitore proprietario portano lo stesso **rischio di bus factor** (il pericolo che un progetto collassi se se ne vanno una o poche persone chiave). Privilegia componenti con una base di contributori ampia o un fornitore finanziariamente solido e registra la valutazione come parte della due diligence (capitoli 10.2, 4.2).

### Leggi e segui le licenze come obbligo di prim'ordine

Mantieni un inventario di ogni componente e della sua licenza e fai rispettare una politica su quali famiglie di licenze sono accettabili per quali usi. La distinzione critica è il copyleft. Il codice **permissivo** (MIT, Apache 2.0) può in genere essere incorporato liberamente in prodotti chiusi. Il **copyleft forte** (GPL) può obbligarti a rilasciare la tua opera derivata distribuita agli stessi termini. Usa l'**analisi di composizione del software (SCA)** automatica, strumenti che scansionano le tue dipendenze per identificare componenti, licenze e vulnerabilità note e generano una **distinta dei materiali del software (SBOM)**, un elenco formale di ogni componente in un prodotto (capitoli 10.3, 4.2).

### Giudica la sicurezza dalla pratica, non dall'apertura

Non presumere che l'open source sia sicuro per l'**argomento dei "molti occhi"** ([legge di Linus](https://en.wikipedia.org/wiki/Linus%27s_law): "dati abbastanza occhi, tutti i bug sono superficiali"). E non presumere che il codice proprietario sia sicuro per la **[sicurezza per oscurità](https://en.wikipedia.org/wiki/Security_through_obscurity)** (la credenza errata che nascondere il sorgente nasconda i difetti). I molti occhi aiutano solo se persone qualificate guardano davvero e molti progetti molto usati sono scarsamente mantenuti. Entrambi i modelli portano **rischio di supply chain**: l'open source attraverso dipendenze compromesse o abbandonate, il proprietario attraverso codice opaco e canali di aggiornamento che non puoi ispezionare. Fissa le versioni, verifica la provenienza, scansiona di continuo e monitora gli avvisi a prescindere dal modello (capitolo 4.2).

### Progetta per uscita e interoperabilità

Preferisci componenti che parlano standard aperti e formati di dati portabili, così da poterli sostituire in seguito (capitoli 3.8, 10.11). Con l'open source ottieni l'uscita definitiva: se un progetto si ferma, puoi farne un **[fork](https://en.wikipedia.org/wiki/Fork_(software_development))** (creare e mantenere la tua copia). Con il software proprietario, negozia in anticipo le protezioni: esportazione dei dati in formati aperti, API documentate e **[deposito del codice sorgente (escrow)](https://en.wikipedia.org/wiki/Source_code_escrow)** (un accordo legale in cui il fornitore deposita il sorgente presso una terza parte, rilasciato a te se il fornitore fallisce). Progetta in modo che nessun singolo componente, di nessuno dei due tipi, possa tenere in ostaggio il tuo sistema.

### Pesa il costo totale di proprietà, non il prezzo di listino

Confronta le opzioni sul **costo totale di proprietà (TCO)**, il costo pieno sulla vita comprendente acquisizione, integrazione, gestione, supporto, formazione, aggiornamenti e sostituzione finale, anziché sulle sole quote di licenza. L'open source spesso scambia costo di licenza contro costo operativo e di personale più alto. Il software proprietario spesso scambia quote di abbonamento prevedibili contro lock-in e minor controllo. Includi il costo del modello stesso: l'open source auto-supportato richiede competenza interna, mentre il software proprietario richiede capacità di gestione dei fornitori.

### Come produttore, rendi open source ciò che non ti differenzia

Classifica il tuo software in ciò che ti dà un vantaggio competitivo o di missione e ciò che è impianto indifferenziato. Tieni proprietari i differenziatori. Considera di rendere open source l'infrastruttura commodity, dove una comunità può condividere manutenzione e miglioramento. Per il governo, pesa il **"denaro pubblico, codice pubblico"** (il principio per cui il software finanziato dai contribuenti dovrebbe essere pubblicamente disponibile per impostazione predefinita) come fattore di trasparenza, riuso e sovranità (capitoli 10.5, 10.11). Scegli la licenza deliberatamente: permissiva per massimizzare l'adozione, copyleft per mantenere aperto l'ecosistema.

## Compromessi: vantaggi e svantaggi

| Dimensione | Open source | Chiuso / proprietario |
|---|---|---|
| **Costo di acquisizione** | Di solito zero da acquisire | Quota di licenza o abbonamento |
| **Costo totale di proprietà** | Il costo si sposta su operazioni e personale | Più prevedibile, ma premio di lock-in |
| **Controllo e personalizzazione** | Pieno: puoi leggere e cambiare il sorgente | Limitato a ciò che il fornitore espone |
| **Supporto e responsabilità** | Comunità, o terza parte a pagamento; nessun unico responsabile da chiamare | Supporto contrattuale e una parte responsabile chiara |
| **Postura di sicurezza** | Verificabile; "molti occhi" se davvero mantenuto | Gestita dal fornitore; opaca; l'oscurità non è protezione |
| **Longevità / abbandono** | Può essere biforcato se mantenuto; può comunque appassire | Dipende da vitalità del fornitore e roadmap |
| **Lock-in sul fornitore** | Basso: sorgente e formati aperti permettono l'uscita | Alto a meno di mitigazione con standard ed escrow |
| **Ecosistema** | Comunità aperta e interoperabilità | Curato, integrato, a volte chiuso da mura |

La tensione ricorrente è **controllo contro comodità e responsabilità**. L'open source massimizza controllo, verificabilità e libertà dal lock-in, ma ti chiede di fornire tu capacità, integrazione e supporto. Il software proprietario consegna un prodotto supportato, integrato e responsabile con un contratto da far valere, ma cede controllo e invita al lock-in. La soluzione raramente è tutto o niente. La maggior parte dei patrimoni maturi mescola fondamenta open source con sistemi proprietari dove supporto, responsabilità o capacità specializzata giustificano il compromesso.

## Domande da discutere con il tuo team

1. **Facciamo rispettare una politica sulle licenze con SCA automatica e SBOM nella pipeline, specialmente per cogliere il copyleft forte prima che venga rilasciato?** Incorporare una libreria GPL in un prodotto proprietario distribuito può obbligarvi a rilasciare il vostro sorgente e quella sorpresa di solito emerge tardi, quando è costoso disfare. Mantenete un inventario di ogni componente e della sua licenza, fate rispettare quali famiglie di licenze sono accettabili per quali usi ed eseguite automaticamente l'analisi di composizione del software così che la pipeline blocchi le violazioni anziché un avvocato coglierle al momento del rilascio. Generate una SBOM come cosa ovvia. Per un patrimonio grande o governativo, questa è anche igiene della supply chain e spesso un requisito di appalto. Portate il vostro attuale inventario delle licenze, o il fatto che non ne avete uno e decidete chi possiede la politica.

2. **Quando adottiamo una dipendenza, valutiamo salute del progetto e bus factor come due diligence?** Una libreria open source con un solo manutentore e un piccolo fornitore proprietario portano lo stesso rischio: il progetto collassa se se ne vanno una o poche persone chiave. Prima di adottare qualsiasi cosa, valutate cadenza dei rilasci, numero e diversità dei manutentori, reattività alle segnalazioni di sicurezza e ampiezza di adozione e registrate la valutazione. Nessun modello è più sicuro per impostazione predefinita; i "molti occhi" aiutano solo se persone qualificate guardano davvero e molti progetti molto usati sono scarsamente mantenuti. Portate le tre o quattro dipendenze su cui il vostro prodotto conta di più e chiedetevi, per ciascuna, quante persone dovrebbero andarsene prima che diventi un vostro problema. Se non sapete rispondere, quella è la valutazione che dovete a voi stessi.

3. **Quando compriamo proprietario, assicuriamo in anticipo protezioni di uscita?** Il software proprietario offre responsabilità e comodità in cambio di controllo e il costo nascosto è il lock-in: costi di cambio che lasciano a un fornitore alzare i prezzi o degradare il servizio con poco ricorso. Negoziate le protezioni prima di firmare, quando avete ancora leva: esportazione dei dati in formati aperti, API documentate ed escrow del codice sorgente che rilascia il sorgente se il fornitore fallisce. Con l'open source la vostra uscita è la capacità di fare un fork; con il proprietario dovete scrivere l'uscita nel contratto. Portate i vostri sistemi proprietari più critici e chiedetevi che cosa succede davvero se il fornitore raddoppia il prezzo o fallisce. Se la risposta è "siamo bloccati", correggete il contratto al rinnovo.

4. **Per il software che costruiamo noi, come decidiamo che cosa rendere open source e che cosa tenere chiuso, e chi detiene l'autorità di prendere quella decisione?** Sbagliate in una direzione e regalate proprio il codice che vi differenzia; sbagliate nell'altra e accumulate impianto commodity la cui manutenzione una comunità condividerebbe volentieri. Le pressioni in competizione sono reali: gli ingegneri vogliono il vantaggio di reclutamento e reputazione di un repository pubblico, mentre prodotto e ufficio legale temono di consegnare un vantaggio ai rivali o di esporre un'euristica sensibile per la sicurezza. Portate una classificazione onesta dei vostri sistemi in differenzianti della missione rispetto a infrastruttura indifferenziata e nominate la persona o il comitato che firma un rilascio, perché una decisione ad hoc presa da chi ha spinto il repository è come i gioielli di famiglia trapelano. Per una grande impresa la questione è la strategia di portafoglio e per il governo si scontra con "denaro pubblico, codice pubblico", il principio per cui il software finanziato dai contribuenti dovrebbe essere pubblico per impostazione predefinita, quindi decidete in anticipo quali esenzioni (sicurezza nazionale, rilevamento delle frodi, dati personali) giustificano di tenere chiuso il codice.

5. **I nostri confronti tra costruire e comprare catturano il costo totale di proprietà pieno, o trattiamo ancora una licenza a costo zero come un costo zero?** L'errore finanziario più comune con l'open source è leggere "gratis da acquisire" come "gratis da gestire", poi scoprire che integrazione, operazioni, risposta alla sicurezza e supporto a pagamento fanno impallidire qualsiasi licenza evitata. La tensione è che un abbonamento proprietario sembra costoso in fattura nascondendo un premio di lock-in e un componente aperto sembra gratis in fattura spostando il costo sul vostro personale. Portate un modello di TCO a pari condizioni per due o tre vere decisioni: acquisizione, integrazione, gestione, supporto, formazione, aggiornamenti, risposta alla sicurezza e sostituzione finale, prezzati sull'intera vita anziché sul primo anno. In un patrimonio aziendale o governativo, aggiungete il costo del modello operativo stesso, poiché l'open source auto-supportato richiede competenza interna che dovete reclutare e trattenere e trattate un confronto che omette quelle voci come evidenza, non come analisi.

6. **Giudichiamo la sicurezza di un componente dalle sue pratiche, o ci appoggiamo all'etichetta di apertura, sia i "molti occhi" sia la segretezza del codice chiuso?** Entrambi i predefiniti sono trappole: i "molti occhi" vi proteggono solo quando persone qualificate rivedono davvero il codice e molti progetti aperti molto usati girano su un solo manutentore esausto, mentre il sorgente chiuso che conta sul fatto che gli attaccanti non lo vedano è sicurezza per oscurità, non un controllo. Il dibattito conta perché cambia dove spendete lo scarso sforzo di sicurezza e la risposta onesta è che entrambi i modelli portano rischio di supply chain, l'open source attraverso dipendenze compromesse o abbandonate e il proprietario attraverso canali di aggiornamento opachi che non potete ispezionare. Portate evidenza per i vostri componenti più critici: chi li rivede davvero, quanto in fretta gli avvisi vengono corretti, se le versioni sono fissate e la provenienza verificata e se generate una SBOM. Per un patrimonio grande o governativo, legatelo ad appalti e obblighi di scansione continua, perché un regolatore chiederà che cosa avete ispezionato, non se il sorgente era pubblico.

## Lente settoriale

**Startup.** Con poca autonomia costruisci su fondamenta open source perché non puoi permetterti quote di licenza e vuoi la libertà di fare un fork se un progetto si ferma. Esegui una scansione di analisi di composizione prima di rilasciare così che una libreria a copyleft forte non ti obblighi in silenzio a pubblicare il tuo sorgente e tieni strettamente chiuso il tuo unico vero differenziante. Rendi open source un piccolo strumento non critico se aiuta il reclutamento, ma non dotare di personale un onere di manutenzione che non puoi portare.

**Piccola impresa.** Senza uno specialista legale o di piattaforma interno, tratta la licenza come un rischio da non leggere male anziché un argomento che puoi padroneggiare. Privilegia strumenti proprietari supportati o distribuzioni open source commerciali dove un fornitore possiede patch e responsabilità, perché auto-supportare uno stack che non sai gestire è una falsa economia. Quando adotti un componente gratuito, controlla che la sua licenza permetta il tuo uso e che il progetto sia davvero mantenuto, non abbandonato.

**Grande impresa.** Su larga scala il problema è la coerenza tra molti team: una politica di licenze scritta, analisi di composizione del software automatica e generazione di SBOM in ogni pipeline e decisioni di costruire o comprare basate sul TCO anziché sull'abitudine del singolo team. Gestisci software aperto e proprietario come un unico portafoglio, standardizza nelle forniture protezioni di uscita come formati aperti ed escrow del codice sorgente e segui la salute delle dipendenze critiche così che un singolo progetto abbandonato non diventi un incidente. Governa anche il lato del produttore, con una regola chiara su che cosa l'organizzazione rende open source rispetto a che cosa tiene chiuso.

**Ente pubblico.** Regole di appalto, obblighi di trasparenza e responsabilità pubblica plasmano ogni scelta. Pesa "denaro pubblico, codice pubblico", il principio per cui il software finanziato dai contribuenti dovrebbe essere pubblico per impostazione predefinita, per far avanzare riuso tra enti e sovranità digitale, ritagliando strette esenzioni per il codice sensibile per la sicurezza o di dati personali. Richiedi a ogni fornitore proprietario di fornire esportazione dei dati in formati aperti ed escrow del codice sorgente così che il fallimento di un fornitore non possa lasciare in secca un servizio pubblico e pubblica il sorgente non sensibile così che i cittadini possano verificare le regole che li governano.

## Esempi

**Startup.** Una startup di tre fondatori costruisce l'intero prodotto su fondamenta open source (Linux, un database open source, un framework web) perché non può permettersi quote di licenza e vuole la libertà di fare un fork se un progetto si ferma. Prima di rilasciare, un fondatore esegue una scansione di analisi di composizione e coglie una libreria a copyleft forte che li avrebbe costretti a pubblicare il loro algoritmo di abbinamento proprietario, quindi la sostituiscono con un equivalente a licenza permissiva. Tengono quell'algoritmo, il loro unico differenziante, strettamente chiuso e rendono open source solo un piccolo strumento interno di registrazione per costruire benevolenza e attrarre ingegneri.

**Grande impresa.** Una grande compagnia di assicurazioni gestisce la sua piattaforma centrale su fondamenta open source: Linux, un database open source molto usato e un orchestratore di container. Ma compra una suite proprietaria di modellazione attuariale, perché la competenza di dominio del fornitore, le certificazioni normative e il contratto di supporto valgono la quota e non c'è un'alternativa aperta paragonabile. Paga un abbonamento per l'**open source commerciale** (distribuzioni dei componenti aperti supportate dal fornitore) per ottenere responsabilità e patch sull'impianto, tenendo strettamente proprietario e interno l'algoritmo di prezzo che la differenzia. L'analisi del TCO (capitolo 10.10) guida ogni scelta anziché l'ideologia.

**Ente pubblico.** Un'amministrazione fiscale nazionale, sotto una politica di "denaro pubblico, codice pubblico", costruisce un nuovo servizio di idoneità alle prestazioni su componenti open source e standard aperti (capitolo 3.8), così che altri enti possano riusarlo e i cittadini possano verificare le regole. Pubblica il codice non sensibile in un repository pubblico, tenendo chiuse per ragioni di sicurezza solo le euristiche di rilevamento delle frodi. Questo riduce il lock-in sul fornitore e fa avanzare la sovranità digitale (capitolo 10.11). Le regole di appalto (capitolo 10.3) richiedono a ogni componente proprietario di fornire esportazione dei dati in formati aperti ed escrow del codice sorgente, per garantire la continuità se il fornitore fallisce.

## Business case: motivazioni, ROI e TCO

L'attrattiva finanziaria dell'open source, la sua mancanza di quota di licenza, è la parte meno affidabile del caso, perché l'acquisizione è una piccola frazione del TCO. I ritorni durevoli sono strategici: libertà dal lock-in (la capacità di cambiare o abbandonare un fornitore senza ri-architettare), verificabilità per sicurezza e conformità, adozione più rapida perché gli ingegneri possono provare prima di impegnarsi e manutenzione condivisa del codice commodity in un'intera industria. I costi compensativi sono reali. Devi fornire integrazione, operazioni, risposta alla sicurezza e spesso supporto a pagamento e un progetto non mantenuto scelto male può costare più in incidenti di quanto una licenza avrebbe costato.

Il business case del software proprietario è responsabilità e comodità: un singolo fornitore responsabile del prodotto, un contratto di supporto che puoi far valere, funzionalità integrate e bilancio prevedibile. Il suo costo nascosto è il lock-in, i costi di cambio che lasciano a un fornitore alzare i prezzi o degradare il servizio con poco ricorso, più la dipendenza dalla solvibilità e dalla roadmap del fornitore. I **modelli di business** comuni sfumano la linea: **[open core](https://en.wikipedia.org/wiki/Open-core_model)** (una base aperta con componenti aggiuntivi proprietari a pagamento), **doppia licenza** (lo stesso codice offerto sia con una licenza copyleft sia con una licenza commerciale a pagamento), **[software come servizio](https://en.wikipedia.org/wiki/Software_as_a_service) (SaaS)** (il software gira come servizio ospitato che affitti, dove il sorgente può essere irrilevante perché non possiedi mai il binario) e modelli di **supporto/abbonamento** che vendono servizio attorno a codice altrimenti gratuito.

Per un produttore, il ROI del **rendere open source il proprio software non differenziante** può essere sostanziale. I contributori esterni riducono il tuo carico di manutenzione. Il progetto diventa una risorsa di reclutamento e reputazione. L'adozione esterna fa del tuo standard quello de facto. Per il governo, dà trasparenza e riuso nel settore pubblico. La regola strategica è semplice: rendi open source la commodity per condividerne il costo e far crescere un ecosistema e tieni chiuso il differenziante per proteggere il vantaggio che finanzia tutto il resto.

## Antipattern e insidie

- **"Gratis significa gratis":** trattare il costo di acquisizione zero come TCO zero, poi finanziare troppo poco gestione e supporto.
- **Cecità alle licenze:** incorporare codice a copyleft forte in un prodotto proprietario distribuito e innescare obblighi che non avevi mai pianificato.
- **Fede nei "molti occhi":** presumere che un progetto aperto sia verificato quando ha un solo manutentore sovraccarico e nessuna revisione di sicurezza.
- **Sicurezza per oscurità:** credere che il sorgente chiuso sia sicuro solo perché gli attaccanti non possono leggerlo.
- **Assolutismo ideologico:** imporre "tutto aperto" o "tutto proprietario" anziché scegliere per componente sul merito e sul TCO.
- **Ignorare la provenienza:** tirare dentro dipendenze senza SBOM, fissaggio delle versioni o verifica della supply chain (capitolo 4.2).
- **Rendere open source i gioielli di famiglia:** rilasciare proprio il codice che ti differenzia, regalando il tuo vantaggio.
- **Fork e dimentica:** fare il fork di un progetto abbandonato senza la capacità di mantenere davvero il fork.

## Modello di maturità

**Livello 1 (Avvio).** I componenti open source e proprietari entrano nel patrimonio ad hoc. Le licenze non sono lette, non c'è inventario né SBOM e la scelta tra modelli è fatta per abitudine o solo per prezzo. Abbandono e rischio di licenza emergono solo quando qualcosa si rompe e ogni team reagisce da solo.

**Livello 2 (Sviluppo).** Alcuni team cominciano pratiche di base: un inventario di componenti e licenze, una grezza visione delle licenze accettabili e un'occasionale analisi di composizione del software. Le decisioni di costruire o comprare e di aperto o chiuso vengono messe per iscritto, ma la disciplina è a macchia di leopardo e incoerente da un team all'altro, quindi una sorpresa di copyleft o di bus factor può ancora scivolare dove l'abitudine non ha preso.

**Livello 3 (Standardizzazione).** Un quadro documentato governa sia il consumo sia la produzione in tutta l'organizzazione. I componenti sono scelti su TCO e salute del progetto, le licenze sono fatte rispettare automaticamente nella pipeline così che le violazioni blocchino una build, le SBOM sono generate come cosa ovvia e una politica esplicita dichiara che cosa l'organizzazione rende open source rispetto a che cosa tiene chiuso. Protezioni di uscita come formati aperti ed escrow del codice sorgente sono standard negli appalti e ogni team segue le stesse regole anziché le proprie.

**Livello 4 (Gestione).** Il programma è misurato e controllato rispetto a valori di riferimento. L'organizzazione segue metriche come la copertura SBOM tra i prodotti, la quota di dipendenze che violano la politica, il tempo medio per correggere una vulnerabilità di dipendenza divulgata, punteggi di bus factor e salute per i progetti critici e il TCO realizzato rispetto alla stima che ha giustificato ogni scelta. Le soglie innescano azione: un componente la cui manutenzione si ferma o la cui latenza di patch deriva oltre l'obiettivo è segnalato per la sostituzione sull'evidenza e le decisioni di aperto o chiuso e di costruire o comprare sono riviste rispetto ai numeri anziché difese per abitudine.

**Livello 5 (Orchestrazione).** La strategia open source è una capacità di business deliberata, integrata nell'organizzazione e continuamente migliorata. L'organizzazione contribuisce ai progetti da cui dipende e a volte ne fa da custode, rende open source il proprio software non differenziante come cosa ovvia e riporta i dati di salute delle dipendenze e di TCO in appalti, sicurezza e pianificazione di prodotto. Riequilibra di routine il proprio portafoglio di software aperto e proprietario, adattandosi agli spostamenti di costo, rischio, sovranità e vantaggio strategico prima che impongano una crisi.

## Spunti di discussione

- Dove nel vostro patrimonio perdere un singolo fornitore o manutentore sarebbe esistenziale, e qual è il vostro piano di uscita?
- Quali dei vostri sistemi sono commodity che potreste rendere open source, e quali sono veri differenziatori da proteggere?
- La vostra organizzazione tratta i "molti occhi" come un vero controllo di sicurezza o un'assunzione non esaminata?
- Per i lettori del settore pubblico: che cosa cambierebbe un predefinito di "denaro pubblico, codice pubblico" nel vostro prossimo appalto?
- Quanto bene i vostri confronti di TCO catturano i costi operativi e di supporto che l'open source sposta su di voi?

## Punti chiave

- **Aperto contro chiuso è definito dalla licenza**, non dal prezzo; conosci la differenza tra libero come libertà e libero come prezzo e tra permissivo e copyleft.
- **Nessun modello è intrinsecamente più sicuro o più economico.** Giudica le pratiche del progetto e il suo TCO pieno, non l'etichetta di apertura.
- **L'apertura è il più forte antidoto al lock-in**, dando verificabilità, portabilità e capacità di fare un fork; il software proprietario offre responsabilità e comodità in cambio di controllo.
- **Decidi per componente sul merito** e mescola i modelli deliberatamente anziché per ideologia.
- **Come produttore, rendi open source la commodity e tieni chiuso il differenziante** e nel governo pesa "denaro pubblico, codice pubblico" per trasparenza, riuso e sovranità.

## Riferimenti e letture di approfondimento

- Eric S. Raymond, *The Cathedral and the Bazaar*
- Nadia Eghbal, *Working in Public: The Making and Maintenance of Open Source Software*
- Karl Fogel, *Producing Open Source Software: How to Run a Successful Free Software Project*
- Adrian Cockcroft e altri, vari titoli O'Reilly su strategia e operazioni open source
- Free Software Foundation, *The Free Software Definition* (e i testi della GNU General Public Licence)
- Open Source Initiative, *The Open Source Definition* ed elenco delle licenze approvate
- Free Software Foundation Europe, materiali della campagna *Public Money, Public Code*
- Yochai Benkler, *The Wealth of Networks*
