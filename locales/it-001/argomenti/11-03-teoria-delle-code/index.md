# 11.3 Teoria delle code

## Panoramica e motivazioni

La [teoria delle code](https://en.wikipedia.org/wiki/Queueing_theory) è lo studio matematico delle file d'attesa. Nell'ingegneria del software è la teoria silenziosa dietro un'enorme quantità di pratica. La reattività dell'assistenza clienti, la pianificazione [kanban](https://en.wikipedia.org/wiki/Kanban_%28development%29) (un metodo a trascinamento che limita il [lavoro in corso](https://en.wikipedia.org/wiki/Work_in_process) per migliorare il flusso), le code di messaggi tra processi, le pipeline di distribuzione continua: sono tutte code e obbediscono tutte alle stesse leggi. Capire quelle leggi permette a un team di ragionare su [tempi di attesa complessivi](https://en.wikipedia.org/wiki/Lead_time), [produttività](https://en.wikipedia.org/wiki/Throughput), capacità e vero costo di far girare i sistemi vicino ai loro limiti, anziché esserne sorpresi in produzione. Questo capitolo sta nella parte sul flusso perché la teoria delle code è la fondazione formale del flusso: spiega *perché* il lavoro aspetta e che cosa riduce davvero l'attesa.

Ecco la motivazione: l'intuizione sulle code è affidabilmente sbagliata e sbagliata in modi costosi. Le persone presumono che un server con un utilizzo del 90% sia "a un 10% dai guai", quando in realtà i tempi di attesa esplodono in modo non lineare man mano che l'utilizzo si avvicina al 100%. Presumono che aggiungere lavoro in corso (WIP) acceleri la consegna, quando allunga i tempi di attesa. Pianificano la capacità attorno alle medie, poi vengono distrutte dalla variabilità. Un po' di teoria delle code sostituisce queste costose intuizioni con un piccolo numero di relazioni robuste, soprattutto la **[legge di Little](https://en.wikipedia.org/wiki/Little%27s_law)**, che valgono allo stesso modo per code di clienti, bacheche di compiti e pipeline CI/CD.

Per i grandi team, l'impresa e il governo, la teoria delle code è un linguaggio condiviso per capacità e flusso, che collega ruoli che altrimenti si parlano addosso. I product manager si preoccupano del tempo di attesa dall'idea al cliente. Gli SRE si preoccupano dell'utilizzo dei server e della latenza. I team DevOps si preoccupano della frequenza di distribuzione. I responsabili del supporto si preoccupano dei tempi di risposta. Sono tutte metriche di coda ed esprimerle in un unico quadro (tasso di arrivo, tasso di servizio, utilizzo, tempo di attesa) permette a un'organizzazione di pianificare la capacità, fissare SLO (obiettivi di livello di servizio) realistici e giustificare l'investimento con la matematica anziché con gli aneddoti.

## Principi chiave

- **Tutto ciò che ha un'attesa è una coda:** ticket, compiti, messaggi e deploy compresi.
- **La legge di Little è l'àncora:** elementi nel sistema = tasso di arrivo × tempo nel sistema (κ = λτ).
- **Utilizzo e tempo di attesa sono non lineari:** l'ultimo 15% di capacità è il più costoso.
- **La variabilità è nemica del flusso:** le medie nascondono il dolore; la varianza crea code.
- **Ridurre il lavoro in corso riduce il tempo di attesa:** l'obiettivo è il flusso, non l'attività frenetica.
- **Misura l'intero flusso:** arrivi, servizio, successi, fallimenti, salti e attese.
- **Un processo è una coda di code:** modella gli stadi, poi ottimizza quello che vincola.

## Raccomandazioni

### Impara la notazione di base e usala in modo coerente

Una manciata di grandezze descrive qualsiasi coda. Standardizzarsi su di esse (le lettere greche sono convenzionali) toglie l'ambiguità tra i team:

- **λ (lambda), tasso di arrivo:** quanto in fretta entrano nuovi elementi.
- **μ (mu), tasso di servizio:** quanto in fretta gli elementi sono gestiti. Poiché "tasso di servizio" è usato in modo ambiguo, vale spesso la pena dividere esplicitamente la produttività in **tasso totale (χ)**, **tasso di successo (α)**, **tasso di fallimento (β)** e **tasso di salto (σ)**, dove χ = α + β + σ.
- **ρ (rho), utilizzo / intensità del traffico = λ / μ:** la sintesi singola più importante. ρ < 1 significa che la coda si svuota; ρ ≥ 1 significa che cresce senza limite.
- **Tempi:** tempo di attesa complessivo (τ, dall'inizio alla fine), tempo di lavoro (φ, elaborazione effettiva), tempo di attesa in coda (ω, in sospeso) e tempo di passo (θ, tra un completamento e l'altro).
- **ε (epsilon), rapporto di errore:** fallimenti ÷ totale.

Nominare esplicitamente fallimenti e *salti* conta nel software: un elemento che viene abbandonato (un cliente che rinuncia, un carrello lasciato, un ticket di lavoro rifiutato) lascia la coda senza essere servito e fingere che sia stato "servito" corrompe le tue metriche. Segui **balking** (decidere di non unirsi), **reneging** (rinunciare dopo l'attesa) e **jockeying** (cambiare coda) come esiti di prim'ordine.

### Ancora la pianificazione alla legge di Little

La legge di Little afferma che il numero medio a lungo termine di elementi in un sistema stabile è pari al tasso medio di arrivo per il tempo medio che ciascun elemento trascorre nel sistema: **κ = λ τ** (classicamente L = λW). È sorprendentemente generale (non richiede alcuna assunzione sulla distribuzione degli arrivi né sull'ordine di servizio), il che ne fa il cavallo di battaglia della pianificazione del flusso. Riarrangiata, ti dice che **tempo di attesa = lavoro in corso ÷ produttività**. È la base matematica di kanban e lean: se vuoi tempi di attesa più brevi e non puoi alzare la produttività, devi abbassare il WIP. Dà anche rapidi controlli di plausibilità. Se 40 ticket sono aperti e ne chiudi 8 al giorno, il ticket medio richiede circa 5 giorni, per quanto occupato si senta chiunque. Il suo unico requisito è la *stabilità*: gli arrivi non devono persistentemente superare le partenze (ρ < 1), altrimenti la coda e le assunzioni della legge crollano.

### Rispetta la non linearità dell'utilizzo

La lezione operativa più importante della teoria delle code è che il tempo di risposta sale bruscamente, non gradualmente, man mano che l'utilizzo si avvicina al 100%. Le *Seven insights into queueing theory* di Bob Wescott catturano vividamente le conseguenze pratiche:

1. Più lento è il centro di servizio, più basso dovrebbe essere il picco di utilizzo che pianifichi.
2. È molto difficile usare l'ultimo 15% di qualsiasi cosa.
3. Più corri vicino al bordo, più alto è il prezzo di sbagliare.
4. La crescita del tempo di risposta è limitata da quanti elementi possono aspettare.
5. Sono medie, non massimi: pianifica per la coda della distribuzione.
6. Diffida dell'effetto di negazione umana tra più centri di servizio.
7. Mostra i piccoli miglioramenti nella loro luce migliore.

L'implicazione di progetto: **prevedi deliberatamente margine.** Puntare al 70–80% di utilizzo per i sistemi sensibili alla latenza non è spreco; è comprare tempi di risposta prevedibili. Questo informa direttamente la pianificazione della capacità e gli SLO (capitoli 3.5 e 9.1).

### Modella i processi come una coda di code

Il lavoro reale fluisce attraverso stadi e un processo a più stadi è semplicemente una coda i cui elementi sono a loro volta in coda a ogni passo. Modellalo così: il tasso di arrivo del processo è il tasso di arrivo dello stadio 1; il tasso di successo del processo è il tasso di successo dell'ultimo stadio; i conteggi di errori e salti del processo sono le somme tra gli stadi. Due forme comuni ricorrono:

- Gli **imbuti**, dove i conteggi degli elementi si riducono a ogni stadio (assunzioni: contatto → colloquio → offerta; acquisti: sfoglia → carrello → paga; consegna: integra → UAT → produzione). Ottimizza lo stadio che conta di più: massimizza gli arrivi in cima all'imbuto, minimizza i salti a metà imbuto (abbandono del carrello) o minimizza gli errori nello stadio finale (cattive distribuzioni in produzione).
- I flussi di scoperta e consegna a **doppio diamante** (scopri → definisci → sviluppa → consegna), che la parte sul flusso di questo libro tratta direttamente (capitolo 11.1).

Trovare e alleviare lo **stadio vincolante** (il collo di bottiglia) è dove il miglioramento del flusso rende; ottimizzare i non vincoli sposta solo la coda.

### Collega le metriche di coda ai KPI che i team già usano

Le grandezze delle code si mappano nettamente sulle metriche di consegna e affidabilità altrove in questo libro, ed è ciò che rende la teoria pratica anziché accademica:

- Il **tempo di attesa di consegna (Dτ)**, "dal concetto al cliente", è una misura di tempo di attesa (τ) e una metrica DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) (capitolo 11.2).
- La **frequenza di distribuzione (Dμ)** è una misura di tasso di servizio.
- Il **tasso di fallimento delle modifiche (Dε)** è un rapporto di errore.
- Il **tempo di ripristino (Rτ)** è un tempo di attesa di ripristino, cioè MTTR (capitolo 9.3).

Distingui i diversi **MTTR** (tempo medio di *risposta*, *riparazione*, *ripristino* e *risoluzione*) perché misurano segmenti diversi della coda degli incidenti e sono abitualmente confusi. Fondare SLI/SLO/SLA (capitolo 9.1) in termini di coda mantiene onesti e confrontabili gli obiettivi.

## Compromessi: vantaggi e svantaggi

| Decisione | Vantaggi | Svantaggi |
|---|---|---|
| **Far girare i sistemi ad alto utilizzo** | Minor costo di hardware per unità | Esplosioni non lineari di latenza; fragili ai picchi |
| **Prevedere ampio margine** | Latenza prevedibile; resiliente alla varianza | Costo a regime più alto; sembra "sottoutilizzato" |
| **Limitare il WIP (kanban)** | Tempi di attesa più brevi; meno cambi di contesto | Sembra più lento; richiede disciplina per mantenere il limite |
| **Modellazione formale delle code** | Decisioni di capacità quantificate; meno sorprese | Curva di apprendimento; i modelli semplificano la realtà disordinata |
| **Solo regole empiriche** | Veloci, senza matematica | Sbagliate proprio dove costa di più (vicino alla capacità) |

Il compromesso ricorrente è **efficienza contro prevedibilità**: spingere in alto l'utilizzo fa risparmiare denaro finché improvvisamente non lo fa più, e a quel punto i costi di latenza, fallimento e lavoro in emergenza fanno impallidire i risparmi. Il contributo della teoria delle code è dirti *dove* sta quel precipizio così che il compromesso sia una scelta, non un incidente.

## Domande da discutere con il tuo team

1. **Qual è il vostro obiettivo esplicito di utilizzo per ogni sistema sensibile alla latenza e chi l'ha approvato?** Il margine è un acquisto deliberato di latenza prevedibile, quindi dovrebbe essere una politica dichiarata, non un incidente di qualunque carico sia capitato di arrivare. Poiché il tempo di risposta sale in modo non lineare, far girare all'85% può già significare latenza di coda elevata, eppure la finanza vede il margine come spreco e spinge in alto l'utilizzo. Portate i numeri: utilizzo attuale, la curva di latenza misurata e il costo del vostro ultimo incidente di latenza, poi mostrate dove sta il precipizio per ogni servizio. Per i sistemi aziendali e governativi con picchi stagionali (stagione delle dichiarazioni, finestre di iscrizione), fissate l'obiettivo rispetto al precipizio del picco, non della media. Se nessuno possiede l'obiettivo di utilizzo, gli incidenti di latenza continueranno a comparire "dal nulla".

2. **Dove nei vostri sistemi una coda è illimitata, senza contropressione per scaricare il carico quando è sopraffatta?** Una coda illimitata non fallisce con grazia; degrada fino al collasso, perché arrivi che superano persistentemente le partenze (rho >= 1) significano che la coda cresce senza limite. Fate l'inventario delle vostre code di messaggi, pool di thread e buffer di richieste e chiedetevi che cosa succede a ciascuno quando il tasso di arrivo supera il tasso di servizio: scarica il carico, applica contropressione o cade? Conta in modo acuto alla scala aziendale, dove un singolo downstream saturo può propagarsi a cascata tra i servizi. Portate il risultato di un test di carico o un incidente passato in cui una coda si è intasata e controllate se il sistema ha rifiutato il lavoro in eccesso o ha cercato di tenerlo tutto. La correzione sono code limitate con contropressione esplicita e timeout derivati dalla legge di Little, così che un sovraccarico scarichi anziché rovesciare.

3. **State modellando il vostro flusso dall'idea alla produzione come una coda di code e i vostri miglioramenti sono puntati sul vero vincolo?** Un processo a più stadi è una coda i cui elementi sono in coda a ogni stadio e ottimizzare qualcosa che non sia lo stadio vincolante sposta solo la coda. Mappate il vostro imbuto di consegna (integra, UAT, produzione, oppure scopri, definisci, sviluppa, consegna) e misurate i tassi di arrivo, servizio, attesa e salto a ogni stadio per trovare dove il lavoro si accumula davvero. I team ottimizzano abitualmente lo stadio che capiscono meglio anziché il collo di bottiglia, il che spende sforzo e non sposta nulla. Portate dati di tempo di attesa per stadio, non sensazioni, perché il collo di bottiglia è spesso uno stato di attesa (revisione, approvazione, disponibilità dell'ambiente) anziché uno stato di lavoro. Una volta che conoscete il vincolo, puntate lì e lasciate in pace i non vincoli.

4. **State usando la legge di Little per fissare i limiti di WIP, o state aggiungendo capacità per curare tempi di attesa che solo più disciplina correggerebbe?** La legge di Little dice che il tempo di attesa è pari al lavoro in corso diviso per la produttività, quindi se non potete alzare la produttività, l'unica leva rimasta per tempi di attesa più brevi è abbassare il WIP, che non costa altro che moderazione. La spinta contraria è reale: limitare il lavoro in corso sembra più lento e inattivo e i dirigenti sotto pressione preferiscono assumere o comprare hardware piuttosto che dire ai team di iniziare meno e finire di più. Portate i numeri duri, elementi aperti attuali e tasso di completamento per stadio e calcolate il tempo di attesa medio implicito, poi confrontatelo con ciò che le persone credono sia; il divario è di solito ampio e imbarazzante. In una grande impresa o ente, una richiesta di assunzione o di acquisto giustificata come correzione del tempo di attesa dovrebbe essere prima messa alla prova con questa aritmetica, perché un aumento di organico che alza il WIP può allungare proprio i tempi di attesa che doveva accorciare.

5. **Pianificate la capacità attorno alle medie, o avete quantificato la variabilità che crea davvero le vostre code?** Le code si formano dalla varianza, non dalla media, quindi due sistemi con identico carico medio possono comportarsi in modo completamente diverso se uno ha arrivi a raffiche o tempi di servizio a coda lunga. La tensione è che le medie sono facili da raccogliere e rassicuranti da riportare, mentre la varianza e la coda sono più difficili da misurare e sgradite in un aggiornamento di stato. Portate la distribuzione, non la media: raffichità degli arrivi, tempi di servizio e di attesa al 95° e 99° percentile e le dimensioni dei lotti che concentrano il lavoro in picchi. Per i sistemi aziendali e governativi con ondate prevedibili (stagione delle dichiarazioni, cicli di paga, finestre di iscrizione, carichi di fine trimestre), pianificate il buffer e l'obiettivo di utilizzo sulla varianza del periodo di picco, perché un progetto dimensionato sulla media annuale fallirà proprio quando il pubblico sta guardando.

6. **Quali delle vostre code contano in silenzio abbandoni e rifiuti come se il lavoro fosse servito e quale domanda insoddisfatta nasconde ciò?** Un elemento che fa balking, reneging o è rifiutato lascia la coda senza essere gestito e registrarlo come "servito" corrompe contemporaneamente la vostra produttività, il vostro rapporto di errore e il vostro piano di capacità. La considerazione contraria è che "chiamate risposte" o "ticket chiusi" appare meglio su una dashboard di "chiamanti che hanno rinunciato", quindi il numero onesto è quello che nessuno si offre di far emergere. Portate il tasso di salto (σ), i conteggi di balking e reneging e la differenza tra carico offerto e carico servito, così che la domanda vera diventi visibile. Conta in modo netto nell'erogazione di servizi pubblici, dove i cittadini che abbandonano una coda telefonica o una domanda di prestazioni sono obblighi non soddisfatti anziché casi risolti e riportarli come gestiti sia travisa le prestazioni sia sottostima la capacità dovuta al pubblico.

## Lente settoriale

**Startup.** Non hai tempo per la modellazione formale delle code e non ne hai bisogno. Cerca per prime le due vittorie più economiche: applica la legge di Little al tuo arretrato per vedere il vero tempo di attesa che il tuo WIP implica e osserva la tua bacheca kanban per lo stadio in cui il lavoro si accumula prima di assumere contro un collo di bottiglia che può non esistere. Tieni l'utilizzo lontano dal precipizio su qualsiasi percorso sensibile alla latenza lasciando margine anziché ottimizzarlo, perché un'interruzione durante un picco di crescita costa molto più di un po' di capacità inattiva.

**Piccola impresa.** Senza uno specialista di code in organico, compra le metriche anziché costruire i modelli. Scegli un help desk, un broker di messaggi o una piattaforma di hosting che già riporta tasso di arrivo, tempo di attesa e abbandono e leggi quei numeri anziché derivarli. Inquadra la decisione come l'osservare due sintomi: attese che salgono in modo non lineare man mano che sei più occupato e clienti che rinunciano prima di essere serviti, poiché un cliente perso è il costo di coda che fa più male a una piccola impresa.

**Grande impresa.** Il lavoro è fare del pensiero in termini di code una disciplina condivisa tra molti team: una notazione concordata (λ, μ, ρ, tempo di attesa), politiche coerenti di WIP e di margine di utilizzo e standard di contropressione così che un downstream saturo non si propaghi a cascata tra i servizi. Fissa SLO e capacità dall'analisi delle code anziché a intuito e gestisci le tue code come portafoglio con valori di riferimento e revisioni così che nessun singolo team giri caldo in isolamento. Incorpora l'analisi nella governance della capacità e nell'audit, così che un obiettivo di margine sia una decisione documentata che qualcuno possiede.

**Ente pubblico.** Appalti, trasparenza e responsabilità pubblica plasmano ogni scelta di capacità. Dimensiona i contact center e i sistemi rivolti ai cittadini sulla varianza del periodo di picco (stagione delle dichiarazioni, finestre di iscrizione), non sulla media annuale, e dota di personale per tenere l'utilizzo lontano dal precipizio quando la domanda sale. Segui balking e reneging come domanda pubblica insoddisfatta anziché nasconderli dentro "chiamate risposte" e giustifica la spesa di capacità con stime di tempo di attesa dalla legge di Little, che danno ad auditor e eletti un caso difendibile e basato sulla matematica anziché un aneddoto.

## Esempi

**Startup.** Un team SaaS di cinque persone che annega in un arretrato di supporto presume di dover assumere un altro operatore. Prima di spendere il denaro, applica la legge di Little: 60 ticket aperti e 12 chiusi al giorno significano che un ticket medio aspetta circa 5 giorni, il che corrisponde alle email arrabbiate. Osservando la bacheca kanban, notano che i ticket si accumulano in attesa dell'ingegneria, non del supporto, quindi limitano il lavoro in corso e instradano le segnalazioni di bug direttamente nello sprint anziché lasciarle in coda. Il tempo di attesa scende sotto i due giorni senza nuove assunzioni e usano il bilancio liberato sul vero collo di bottiglia.

**Grande impresa.** Una piattaforma di pagamenti che dimensiona il suo servizio di autorizzazione misura λ ≈ 850 richieste/secondo e per nodo μ ≈ 200/secondo. Ingenuamente sono ~5 nodi (ρ = 0,85), ma sapendo che ρ = 0,85 significa già una latenza di coda nettamente elevata, il team prevede ρ ≈ 0,65 e usa la legge di Little per prevedere il numero di richieste in volo e fissare profondità delle code e timeout. Gli incidenti di alta stagione che comparivano "dal nulla" spariscono, perché il team non operava più sulla parte ripida della curva.

**Ente pubblico.** Il contact center di un'agenzia fiscale modella il supporto della stagione delle dichiarazioni come una coda: picchi di arrivo (λ), capacità degli operatori (μ) e, fondamentale, il **tasso di salto (σ)** dei cittadini che abbandonano dopo lunghe attese. Seguendo balking e reneging anziché solo "chiamate risposte", la leadership vede la vera domanda insoddisfatta, dota di personale per tenere l'utilizzo lontano dal precipizio durante i picchi e giustifica la capacità aggiuntiva con stime di tempo di attesa dalla legge di Little, un caso difendibile e basato sulla matematica per la spesa pubblica anziché aneddotico.

## Business case: motivazioni, ROI e TCO

La teoria delle code rende prevenendo due errori costosi: il **sovradimensionamento** (pagare capacità inattiva di cui non avevi bisogno) e, molto più dannoso, il **sottodimensionamento vicino al precipizio** (dove piccoli aumenti di carico causano grande latenza, SLA violati, clienti che abbandonano e spesa d'emergenza). Poiché il costo di far girare vicino al 100% di utilizzo è non lineare, i risparmi del "mettiamo solo un po' più di carico" sono piccoli e lo svantaggio è catastrofico, esattamente l'asimmetria che un po' di matematica trasforma in una decisione deliberata. Il ritorno si misura in interruzioni evitate, SLA rispettati, clienti trattenuti che altrimenti avrebbero fatto balking e turni di reperibilità più tranquilli.

Sul **costo totale di proprietà**, il quadro è economico da adottare (è conoscenza, non strumenti) e migliora quasi ogni decisione di capacità, latenza e flusso che una grande organizzazione prende nella vita di un sistema. La legge di Little e i limiti di WIP riducono i tempi di attesa senza comprare nulla (una pura vittoria di processo), mentre la disciplina di utilizzo scambia un costo a regime modesto e prevedibile contro l'eliminazione di fallimenti costosi e imprevedibili. Per presentare il caso alla leadership, traduci un recente incidente di latenza nella curva di utilizzo e mostra come un obiettivo di margine l'avrebbe prevenuto e usa la legge di Little per collegare la riduzione del WIP direttamente a una consegna più rapida.

## Antipattern e insidie

- **Pianificare la capacità attorno alle medie:** ignorare la varianza, che è ciò che crea davvero le code.
- **Girare a caldo:** puntare al 90%+ di utilizzo su sistemi sensibili alla latenza ed essere scioccati dalla latenza di coda.
- **Contare i salti come servizio:** trattare clienti abbandonati o ticket rifiutati come gestiti, corrompendo le metriche.
- **Accumulare WIP:** scambiare l'attività frenetica per produttività e allungare i tempi di attesa.
- **Ottimizzare un non collo di bottiglia:** migliorare stadi che non sono il vincolo e spostare la coda altrove.
- **Confondere gli MTTR:** riportare "ripristino" misurando "riparazione", o viceversa.
- **Code illimitate:** nessuna contropressione, così un sistema sovraccarico degrada fino al collasso anziché scaricare il carico.
- **Medie come massimi:** progettare sulla media ed essere chiamati dalla coda.

## Modello di maturità

- **Livello 1, Avvio:** Le code (ticket, compiti, messaggi, deploy) non sono gestite e sono reattive; la capacità è indovinata; l'utilizzo gira dove cade il carico; i problemi di latenza sorprendono il team e sono affrontati in emergenza a posteriori.
- **Livello 2, Sviluppo:** Pochi team raccolgono metriche di base (produttività, attesa media) ma le leggono come medie e le applicano in modo incoerente; alcuni gruppi limitano il WIP o lasciano margine mentre altri girano a caldo; non c'è notazione condivisa, quindi le pratiche non viaggiano tra i team.
- **Livello 3, Standardizzazione:** Una notazione comune (λ, μ, ρ, tempo di attesa) è documentata e imposta in tutta l'organizzazione; limiti di WIP e obiettivi di margine di utilizzo sono fissati deliberatamente per ogni sistema sensibile alla latenza; i diversi MTTR sono distinti; le code limitate con contropressione sono il predefinito tra i servizi.
- **Livello 4, Gestione:** Le code sono misurate e controllate rispetto a valori di riferimento: tasso di arrivo, tasso di servizio, utilizzo, latenza di coda (p95/p99) e tempo di attesa sono seguiti rispetto a obiettivi e SLO definiti; profondità delle code, timeout e margine sono derivati dalla legge di Little anziché indovinati; balking, reneging e tasso di salto sono contati così che il carico offerto sia distinto dal carico servito; le decisioni di capacità sono riviste su questa evidenza, non a sensazione.
- **Livello 5, Orchestrazione:** Il flusso è modellato di continuo come coda di code; i colli di bottiglia sono identificati e alleviati come pratica continua; capacità, SLO e contropressione si adattano alla domanda e alla varianza che cambiano; le metriche di coda si legano direttamente alle metriche DORA e ai KPI di business e l'organizzazione riequilibra la capacità lungo l'intero flusso man mano che cambiano il carico e il quadro dei rischi.

## Spunti di discussione

1. A che utilizzo girano davvero i vostri sistemi sensibili alla latenza e dove sta il loro precipizio?
2. Applicate la legge di Little al vostro arretrato attuale: quale tempo di attesa implica il vostro WIP ÷ produttività e corrisponde alla realtà?
3. Quali delle vostre code contano in silenzio i "salti" (abbandoni, rifiuti) come se fossero serviti?
4. Dove abbassare il WIP accorcerebbe il tempo di attesa più economicamente che aggiungere capacità?
5. Quale stadio del vostro flusso dall'idea alla produzione è il vero collo di bottiglia e i vostri miglioramenti sono puntati lì?
6. Le vostre dashboard mostrano medie dove è la coda a farvi davvero male?

## Punti chiave

- Code di clienti, bacheche kanban, code di messaggi e pipeline di deploy sono tutte code governate dalle stesse leggi.
- La **legge di Little (κ = λτ)** ancora la pianificazione del flusso: tempo di attesa = WIP ÷ produttività.
- Utilizzo e tempo di attesa sono **non lineari**: prevedi margine; l'ultimo 15% è il più costoso.
- Segui il quadro completo: arrivi, servizio, successi, **fallimenti e salti** e attese; non lasciare che l'abbandono si nasconda.
- Modella i processi come una **coda di code** e correggi il **collo di bottiglia**, non l'attività frenetica.
- Le metriche di coda si mappano direttamente sulle misure **DORA/di flusso** e **SLI/SLO** (capitoli 11.1, 11.2, 9.1), dando all'intera organizzazione un unico linguaggio per capacità e flusso.

## Riferimenti e letture di approfondimento

- Bob Wescott, *Seven Insights into Queueing Theory* (e *The Every Computer Performance Book*).
- John D. C. Little, "A Proof for the Queuing Formula L = λW" (1961): la legge di Little.
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate*: metriche DORA basate sul flusso che si allineano ai KPI di coda.
- Donald Reinertsen, *The Principles of Product Development Flow*: code, dimensione dei lotti ed economia del WIP.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability*: la legge di Little applicata a kanban.
- Joel Parker Henderson, *Queueing Theory*: notazione, KPI e coda di code (github.com/joelparkerhenderson/queueing-theory).
- Dan Slimmon, "The most important thing to understand about queues" (2016).
- Wikipedia: "Queueing theory", "M/M/1 queue", "Little's law", "Markov chain".
