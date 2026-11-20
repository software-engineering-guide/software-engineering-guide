# 9.1 Site reliability engineering

## Panoramica e motivazioni

La [site reliability engineering](https://en.wikipedia.org/wiki/Site_reliability_engineering) (SRE) applica le pratiche dell'ingegneria del software alla gestione dei sistemi in produzione. Anziché trattare le operazioni come lavoro manuale guidato da ticket e tenuto separato dallo sviluppo, l'SRE tratta l'affidabilità come un problema ingegneristico che risolvi con codice, misurazione e chiari obiettivi di servizio. L'idea centrale, resa popolare da Google ma ormai diffusa, è semplice: le persone che tengono in funzione i sistemi dovrebbero spendere la maggior parte del tempo a costruire automazione e a migliorare i sistemi, non a fronteggiare a mano gli stessi guasti ancora e ancora.

Per i grandi team questo conta perché la scala alza sia il valore dell'affidabilità sia il costo di sbagliarla. Quando un servizio supporta milioni di utenti o migliaia di consumatori interni, un'ora di fermo significa ricavi persi, transazioni mancate e fiducia erosa. Le operazioni manuali che vanno bene per una manciata di server crollano sotto centinaia di servizi e [deployment continuo](https://en.wikipedia.org/wiki/Continuous_deployment). L'SRE ti dà un linguaggio condiviso per l'affidabilità, un modo per rendere esplicito il compromesso tra rilasciare funzionalità e mantenere stabili le cose e un modo per tenere quella linea in modo coerente tra molti team.

I contesti aziendali e governativi aggiungono ulteriore peso. Le industrie regolamentate come banche, sanità e servizi pubblici portano spesso impegni legali o contrattuali di disponibilità, requisiti di audit e poca tolleranza per interruzioni che colpiscono i cittadini o la sicurezza. I servizi digitali governativi pubblicano sempre più apertamente i propri obiettivi di affidabilità e i dati di prestazione. L'SRE ti dà un modo rigoroso e basato sull'evidenza di definire che cosa significhi "abbastanza affidabile", misurarlo onestamente e difendere le priorità ingegneristiche davanti alla leadership e agli organi di controllo con dati anziché opinioni.

*Vedi anche:* capitolo 9.2 (osservabilità e monitoraggio), capitolo 9.3 (gestione degli incidenti) e capitolo 3.5 (scalabilità, prestazioni e resilienza).

## Principi chiave

- **L'affidabilità è la funzionalità più importante.** Un sistema che non funziona non vale nulla per quante funzionalità abbia, ma l'affidabilità perfetta non è né raggiungibile né vale il suo costo.
- **Definisci l'affidabilità con obiettivi misurabili.** Indicatori (SLI), obiettivi (SLO) e accordi (SLA) di livello di servizio trasformano aspettative vaghe in numeri su cui tutti possono concordare.
- **Il 100 per cento è l'obiettivo sbagliato.** Gli utenti non sanno distinguere tra un sistema molto affidabile e uno perfettamente affidabile, quindi punta a "abbastanza affidabile" e spendi il budget restante in velocità.
- **I budget di errore allineano gli incentivi.** Il divario tra l'SLO e il 100 per cento è un budget di rischio che sviluppatori e operatori condividono, sostituendo le discussioni con l'aritmetica.
- **La fatica operativa (toil) è il nemico.** Il lavoro operativo ripetitivo, manuale e automatizzabile dovrebbe essere misurato, limitato ed eliminato sistematicamente.
- **Automatizza deliberatamente.** L'automazione è come un piccolo team gestisce un grande sistema; investirci è un'attività ingegneristica di prim'ordine.
- **Apprendimento senza colpe.** I fallimenti sono trattati come occasioni per migliorare sistemi e processi, non per punire gli individui.

## Raccomandazioni

### Definisci SLI, SLO e SLA deliberatamente

Parti dalla prospettiva dell'utente. Un **[indicatore di livello di servizio](https://en.wikipedia.org/wiki/Service-level_indicator)** è una misura quantitativa del comportamento di un servizio, come la proporzione di richieste servite in meno di 300 millisecondi o la frazione di risposte riuscite. Scegli un piccolo numero di SLI che riflettano davvero la soddisfazione degli utenti: disponibilità, latenza, correttezza e freschezza sono comuni. Un **[obiettivo di livello di servizio](https://en.wikipedia.org/wiki/Service-level_objective)** è un valore o intervallo obiettivo per un SLI, per esempio "il 99,9 per cento delle richieste riesce su una finestra mobile di 28 giorni". Un **[accordo di livello di servizio](https://en.wikipedia.org/wiki/Service-level_agreement)** è un contratto con conseguenze (rimborsi, penali) collegate a un livello promesso. Mantieni i tuoi SLO più severi dei tuoi SLA, così ottieni un avviso prima di violare un impegno. Pubblica i tuoi SLO, rivedili ogni trimestre e trattali come documenti vivi che si stringono o si allentano man mano che impari.

### Adotta i budget di errore e falli rispettare

Il budget di errore è `100% meno l'SLO`. Se il tuo SLO è il 99,9 per cento, il tuo budget è lo 0,1 per cento di inaffidabilità per finestra, circa 43 minuti al mese. Spendilo in rischio pianificato: rilasci aggressivi, esperimenti e prove di guasto controllate. Quando il budget è sano, i team possono rilasciare in fretta. Quando si esaurisce, la politica dovrebbe spostare automaticamente le priorità verso il lavoro di affidabilità e sospendere le modifiche rischiose finché il sistema non si riprende. Il potere del budget di errore è che lo concordi in anticipo, così toglie emozione e politica dal momento di un'interruzione.

### Misura e riduci la fatica operativa

La fatica operativa (toil) è lavoro operativo manuale, ripetitivo, automatizzabile, tattico e che cresce in proporzione al sistema. Segui la percentuale di tempo SRE spesa in fatica e fissa un tetto, comunemente attorno al 50 per cento, così che almeno metà del tuo tempo di ingegneria vada in miglioramenti durevoli. Tieni un arretrato di progetti di riduzione della fatica, dai priorità per frequenza per costo e festeggia l'eliminazione di un compito ricorrente quanto il rilascio di una nuova funzionalità. Un **mandato di automazione** lo rende esplicito: qualsiasi procedura manuale che esegui più di un dato numero di volte diventa candidata all'automazione o a strumenti self-service.

### Pianifica la capacità e prevedi la domanda

Modella il carico atteso da andamenti storici, lanci pianificati e proiezioni di business. Combina previsioni di crescita organica con eventi una tantum come campagne di marketing, scadenze fiscali o periodi di iscrizione alle prestazioni che contano molto nel governo. Mantieni margine sopra il picco, fai test di carico per verificare le tue assunzioni e automatizza la scalatura dove puoi mantenendo un [piano di capacità](https://en.wikipedia.org/wiki/Capacity_planning) rivisto da persone per i grandi impegni. Segui i tempi di consegna della predisposizione così che una carenza non ti colga mai di sorpresa.

### Tratta l'affidabilità come una funzionalità con un costo reale

Ogni "nove" in più di disponibilità di solito costa molto più in ridondanza, test e sofisticazione operativa del precedente. Rendi esplicito il costo dei nove, così che i responsabili di prodotto scelgano l'obiettivo a occhi aperti. Progetta per un degrado graduale, così che i fallimenti parziali diano un servizio ridotto anziché interruzioni totali. Investi in ridondanza e failover in proporzione all'SLO, non in modo uniforme su ogni componente.

### Scegli un modello organizzativo SRE

Non esiste un'unica struttura corretta. Un team SRE **centralizzato** ti dà coerenza, competenza profonda e strumenti condivisi, ma può diventare un collo di bottiglia o una discarica per i problemi altrui. Un modello **incorporato** colloca gli SRE dentro i team di prodotto per una stretta collaborazione, ma rischia incoerenza e isolamento. Molte grandi organizzazioni usano un ibrido: un team centrale di piattaforma e standard più ingegneri di affidabilità incorporati, con un chiaro modello di ingaggio che definisce quando un servizio si qualifica per il supporto SRE e quale soglia di prontezza alla produzione deve prima superare.

## Compromessi: vantaggi e svantaggi

| Decisione | Vantaggi | Svantaggi |
|---|---|---|
| SLO severi (più nove) | Maggiore fiducia degli utenti, rispetta i contratti | Costo crescente, consegna delle funzionalità più lenta |
| SLO larghi (meno nove) | Rilasci più rapidi, costo inferiore | Rischio di abbandono degli utenti e penali SLA |
| SRE centralizzato | Coerenza, competenza condivisa | Colli di bottiglia, distanza dal prodotto |
| SRE incorporato | Stretta collaborazione, contesto | Incoerenza, difficile da dotare di personale |
| Forte investimento in automazione | Scala, riduce la fatica | Costo iniziale, l'automazione può a sua volta fallire |

L'ingegneria dell'affidabilità riguarda in realtà lo spendere con saggezza risorse finite. Inseguire un nove in più che gli utenti non riescono nemmeno a percepire spreca denaro che potrebbe finanziare funzionalità o abbassare i prezzi. Andare dall'altra parte e investire troppo poco in un sistema i cui guasti causano danni reali è negligente. Il quadro del budget di errore esiste proprio per rendere questo compromesso visibile e negoziabile anziché implicito e conflittuale. Il compromesso sul modello organizzativo è altrettanto reale: la risposta giusta dipende da dimensione dell'azienda, maturità ingegneristica e uniformità dei tuoi servizi.

## Domande da discutere con il tuo team

1. **Quale esatto SLI riflette ciò che i vostri utenti sentono davvero, e potete mostrare che non è una metrica di vanità?** Scegliete l'indicatore sbagliato e ogni dashboard appare verde mentre gli utenti soffrono, che è la trappola dell'SLI di vanità di cui questo capitolo avverte. Portate dati veri alla discussione: misurate lo stesso percorso utente da un vero percorso di richiesta (dall'accesso alla dashboard, dal checkout alla conferma) anziché dalla CPU del server o da un controllo di salute del backend. Per un grande team, un cattivo SLI si propaga: decine di servizi lo ereditano, gli allarmi scattano sulla cosa sbagliata e il budget di errore smette di significare qualcosa. Nei contesti aziendali e governativi in cui un SLA comporta rimborsi o impatto sui cittadini, il vostro SLI è l'evidenza che difendete davanti agli auditor, quindi deve risalire direttamente al successo visibile all'utente. Se non riuscite a tracciare una linea dal numero all'esperienza di un utente, sostituite il numero.

2. **Che cosa deve provare un servizio prima che il vostro team SRE lo prenda in reperibilità, e chi dice no?** Senza una soglia di prontezza alla produzione, un team SRE centrale diventa una discarica per ogni servizio instabile e affoga nel debito tecnico altrui. Scrivete i criteri di ingresso: un SLO posseduto, runbook funzionanti, allarmi azionabili, margine di capacità e un percorso dimostrato di distribuzione e rollback. Per una grande organizzazione questo modello di ingaggio è ciò che impedisce al team di affidabilità di diventare un collo di bottiglia che rallenta tutti. Nei contesti regolamentati la revisione di prontezza fa anche da controllo che potete mostrare agli organi di controllo. Decidete chi detiene l'autorità di rifiutare l'inserimento, perché una soglia che nessuno fa rispettare non è una soglia e la risposta cambia se l'SRE scala o crolla sotto il dolore ereditato.

3. **Con quanto anticipo pre-predisponete per il vostro singolo più grande picco prevedibile, e conoscete il vostro tempo di consegna della predisposizione?** Presumere che l'elasticità del cloud sia istantanea e infinita invita carenze durante i picchi che contano di più e quei picchi (scadenze fiscali, finestre di iscrizione, eventi di saldi) sono i momenti in cui il fallimento è più visibile e più costoso. Portate i numeri: carico di picco storico, crescita prevista, il multiplo a cui fate test di carico e il vero tempo di consegna per acquisire grande capacità riservata o istanze specializzate. Per i servizi governativi stagionali il picco può essere diverse volte il carico normale e politicamente impossibile da mancare, quindi pre-predisporre settimane prima batte sperare che la scalatura automatica tenga il passo. La risposta dovrebbe fissare un calendario concreto: quando fate i test di carico, quando bloccate la capacità e chi possiede la decisione di procedere.

4. **Quando il vostro budget di errore si esaurisce, che cosa succede davvero, e chi ha titolo per farlo rispettare?** Un budget di errore su cui non si agisce mai quando è esaurito è solo decorazione e il momento di un'interruzione è il peggiore per negoziare la politica da zero. La spinta contraria è reale: un lancio impegnato, una scadenza di ricavi o un annuncio pubblico premeranno con forza contro un congelamento delle modifiche rischiose. Portate i dati sul tasso di consumo, il testo della politica concordata in anticipo e una registrazione delle ultime volte in cui il budget è stato violato, così da vedere se il congelamento ha davvero retto. Per un grande team il budget allinea gli incentivi solo se ogni gruppo eredita la stessa applicazione, quindi decidete in anticipo chi firma una deroga e come quell'eccezione è registrata. Nei contesti aziendali e governativi in cui un SLA comporta penali o impatto sui cittadini, la traccia delle deroghe diventa un artefatto di audit, quindi nominate ora il responsabile anziché improvvisare quando il budget è già andato.

5. **Quale frazione della settimana del vostro team SRE è fatica operativa, e quello è un numero misurato o una sensazione?** La fatica che nessuno conta si espande in silenzio finché il team spende tutto il tempo a fronteggiare emergenze e nessuno a costruire miglioramenti durevoli, che è esattamente la trappola da cui l'SRE esiste per sfuggire. La tensione è che misurare la fatica è esso stesso lavoro e gli ingegneri sotto pressione di scadenza resistono a registrare dove vanno le loro ore. Portate un campione onesto: una o due settimane di tempo tracciato rispetto a una definizione condivisa di fatica (manuale, ripetitiva, automatizzabile, tattica e crescente col sistema), più l'arretrato di progetti di automazione ordinati per frequenza per costo. Per una grande organizzazione un tetto del 50 per cento significa qualcosa solo se riportato e difeso team per team, quindi concordate chi rivede il numero e che cosa succede quando un team lo sfora. Nei contesti regolamentati e governativi, limitare la fatica libera specialisti scarsi per il lavoro di controllo e audit che le operazioni manuali soffocano, quindi trattate la cifra della fatica come un segnale di capacità che la leadership dovrebbe vedere.

6. **Quale modello organizzativo SRE gestite, e quale evidenza vi direbbe che ha smesso di adattarsi?** Un team centralizzato dà coerenza e strumenti condivisi ma può diventare un collo di bottiglia; un modello incorporato dà contesto ma deriva verso l'incoerenza; l'ibrido su cui si assestano la maggior parte delle grandi organizzazioni richiede un chiaro modello di ingaggio o eredita le debolezze di entrambi. Portate i segnali che rivelano tensione: quanto aspettano i servizi per il supporto SRE, quanto varia la pratica di affidabilità tra i team e se gli ingegneri incorporati si sentono tagliati fuori da una comunità professionale. La risposta giusta dipende da dimensione dell'azienda, maturità ingegneristica e uniformità dei servizi, quindi rivedetela man mano che queste cambiano anziché trattare la prima scelta come permanente. Per un'impresa o un ente con molti team e rigorosi requisiti di uniformità, un gruppo centrale di standard e piattaforma più ingegneri di affidabilità incorporati di solito bilancia coerenza e contesto locale, ma solo se il modello di ingaggio e la soglia di prontezza alla produzione sono scritti e qualcuno li possiede.

## Lente settoriale

**Startup.** Con una manciata di ingegneri e nessun margine per un team di affidabilità dedicato, scegli un singolo SLO sul percorso utente che conta di più e condividi la reperibilità con l'intero team. Appoggiati ai servizi gestiti del tuo fornitore cloud e al monitoraggio integrato anziché costruire un'infrastruttura di osservabilità e scrivi brevi postmortem in un documento condiviso così che le correzioni restino. La velocità conta più del processo qui: un SLO largo che fai davvero rispettare batte uno elaborato che nessuno guarda.

**Piccola impresa.** Senza uno specialista che gestisca l'affidabilità, trattala come una disciplina che compri attraverso la tua piattaforma: monitoraggio di uptime ospitato, database gestiti e strumenti per pagine di stato anziché uno stack su misura. Fissa uno o due SLO legati alle transazioni che pagano le bollette e decidi onestamente quali fallimenti ti costerebbero un cliente. Compra resilienza dove costa meno che costruirla e mantieni l'onere operativo abbastanza leggero da far sì che i tuoi ingegneri esistenti possano portarlo accanto al lavoro sulle funzionalità.

**Grande impresa.** La sfida è la coerenza tra molti team: un vocabolario SLO condiviso, una politica comune sul budget di errore e una soglia di prontezza alla produzione che ogni servizio supera prima che l'SRE lo prenda in reperibilità. Un gruppo centrale di piattaforma e standard più ingegneri di affidabilità incorporati mantiene uniforme la pratica senza diventare un collo di bottiglia e la governance richiede budget di errore riportati e fatti rispettare allo stesso modo ovunque. Metti a bilancio esplicitamente l'infrastruttura di osservabilità e l'investimento in automazione e gestisci l'affidabilità come un portafoglio con metriche che la leadership può vedere.

**Ente pubblico.** I servizi pubblici portano spesso obiettivi di disponibilità pubblicati, impegni statutari e obblighi di audit, quindi gli SLO e le decisioni sul budget di errore diventano registrazioni che difendi davanti agli organi di controllo. Le regole di appalto possono vincolare quale monitoraggio e hosting puoi usare e le aspettative di trasparenza ti spingono a pubblicare i dati di affidabilità su una dashboard di stato pubblica. Pianifica con settimane di anticipo gli estremi picchi stagionali come scadenze fiscali e finestre di iscrizione alle prestazioni e mantieni una cultura del postmortem senza colpe così che i fallimenti pubblici guidino il miglioramento del sistema anziché la colpa individuale.

## Esempi

**Startup.** Una startup di dieci persone gestisce una singola app web e condivide la reperibilità tra tre ingegneri. Anziché costruire un team di affidabilità che non può permettersi, sceglie un SLO significativo: il 99,5 per cento di successo sul flusso dall'accesso alla dashboard, misurato da vere richieste degli utenti. Quando un'API di terze parti instabile comincia a mangiare quel budget, il team spende un venerdì ad aggiungere un nuovo tentativo e una cache anziché rilasciare la funzionalità successiva, poi scrive un postmortem di due paragrafi in un documento condiviso così che la correzione resti.

**Grande impresa.** Un'azienda globale di pagamenti fissa un SLO di disponibilità del 99,99 per cento per la sua API delle transazioni, il che dà un budget di errore di circa quattro minuti al mese. Un team SRE centrale di piattaforma possiede [osservabilità](https://en.wikipedia.org/wiki/Observability_(software)) condivisa, strumenti per gli incidenti e la politica sul budget di errore, mentre ingegneri di affidabilità incorporati lavorano dentro ogni gruppo di prodotto. Quando una nuova funzionalità antifrode brucia metà del budget mensile in una settimana, la politica concordata in anticipo congela i rilasci non critici finché il lavoro di affidabilità non ripristina il margine. I dirigenti lo accettano senza discussione, perché hanno ratificato la politica in anticipo.

**Ente pubblico.** Un'amministrazione fiscale nazionale gestisce un servizio online di dichiarazione con estremi picchi stagionali attorno alla scadenza annuale. Il suo team SRE prevede la domanda dagli anni precedenti più i cambiamenti di popolazione e politica, fa test di carico a diverse volte il picco normale e pre-predispone la capacità con settimane di anticipo. Gli SLO pubblici di disponibilità e latenza delle pagine vanno su una dashboard di stato. Una cultura del [postmortem](https://en.wikipedia.org/wiki/Postmortem_documentation) senza colpe (rivedere i fallimenti per migliorare i sistemi anziché attribuire colpa individuale) e un mandato di automazione tagliano costantemente gli interventi manuali che un tempo dominavano la stagione delle dichiarazioni, liberando il personale per migliorare il sistema anziché accudirlo a ogni scadenza.

## Business case: motivazioni, ROI e TCO

Il ritorno dell'SRE viene da tre fonti: fermo evitato, meno lavoro operativo e distribuzione sicura più rapida. Il fermo per un grande servizio può costare da migliaia a milioni all'ora in ricavi persi, penali e rimedi, quindi anche modesti guadagni di affidabilità ripagano rapidamente un team. La riduzione della fatica trasforma un costo manuale ricorrente in un investimento una tantum in automazione, così che il costo totale di proprietà cali al crescere della scala anziché salire in proporzione. I budget di errore permettono al business di rilasciare più in fretta quando l'affidabilità è sana, catturando il valore delle funzionalità che operazioni troppo caute lascerebbero sul tavolo.

Il costo di adozione è reale. L'SRE richiede ingegneri qualificati, infrastruttura di osservabilità e un cambiamento culturale che compete con le scadenze delle funzionalità. Ma il costo del non adottare è più alto su larga scala: organico operativo illimitato, interruzioni imprevedibili, esaurimento e abbandono del personale e danno reputazionale difficile da quantificare ma facile da subire. Per presentare il caso alla leadership, imposta l'SRE come gestione del rischio con ritorni misurabili. Presenta il costo attuale di incidenti e operazioni manuali, gli obiettivi SLO legati agli impegni di business e la riduzione prevista di entrambi. Ancora l'argomento sul budget di errore come strumento di governance che dà alla leadership una leva sul compromesso tra affidabilità e velocità.

## Antipattern e insidie

- **SRE come operazioni rinominate.** Rinominare un team di operazioni senza il tempo di ingegneria, il mandato di automazione e l'autorità di opporsi non cambia nulla.
- **Puntare al 100 per cento.** Inseguire l'affidabilità perfetta spreca denaro e blocca la consegna per guadagni che gli utenti non possono percepire.
- **SLI di vanità.** Misurare la CPU del server anziché il successo visibile all'utente dà numeri che sembrano buoni mentre gli utenti soffrono.
- **Budget di errore senza denti.** Un budget che non viene mai fatto rispettare quando è esaurito è solo decorazione.
- **Fatica senza misurazione.** Se non segui la fatica, consuma in silenzio il team finché non avviene alcun lavoro di miglioramento.
- **SRE come discarica.** I team centralizzati che ereditano ogni servizio instabile senza una soglia di prontezza affogano nel debito tecnico altrui.
- **Ignorare i tempi di consegna della capacità.** Presumere che l'elasticità del cloud sia istantanea e infinita invita carenze durante i picchi che contano di più.

## Modello di maturità

**Livello 1, Avvio.** Le operazioni sono manuali e reattive. Non ci sono SLO formali, l'affidabilità è una questione di opinione e gli stessi incidenti si ripetono mentre domina il fronteggiare le emergenze. Qualsiasi automazione è incidentale e nessuno possiede l'affidabilità come questione ingegneristica.

**Livello 2, Sviluppo.** Alcuni servizi hanno SLI e SLO di base e un monitoraggio e allarmi rudimentali, ma la pratica varia molto tra i team. La fatica è riconosciuta ma non misurata, l'automazione è ad hoc e i postmortem avvengono in modo incoerente. L'affidabilità migliora nelle sacche in cui gli individui la spingono, non perché l'organizzazione lo richieda.

**Livello 3, Standardizzazione.** SLI, SLO e una politica sul budget di errore sono documentati e applicati in modo coerente tra i team. La fatica è definita e seguita, la pianificazione della capacità è di routine, esiste un modello di ingaggio SRE con revisioni di prontezza alla produzione e l'automazione è un filone di lavoro finanziato anziché un progetto collaterale. La pratica di affidabilità è scritta e fatta rispettare in tutta l'organizzazione.

**Livello 4, Gestione.** Il programma di affidabilità è misurato e controllato con dati rispetto a valori di riferimento. Tasso di consumo del budget di errore, percentuale di fatica, raggiungimento degli SLO, tempo medio di ripristino e tempi di consegna della predisposizione sono seguiti come metriche, rivisti con una cadenza fissa e usati per tenere i team ai loro obiettivi. Le violazioni del budget innescano il congelamento concordato, la capacità è prevista rispetto a modelli di domanda e ogni decisione di procedere o meno poggia sull'evidenza anziché sull'opinione.

**Livello 5, Orchestrazione.** L'ingegneria dell'affidabilità è integrata nell'organizzazione e continuamente migliorata. La politica sul budget di errore è automatizzata e rispettata ovunque, la maggior parte delle operazioni è self-service, la capacità è predisposta in modo proattivo e i dati di affidabilità guidano compromessi adattivi tra velocità e stabilità. L'organizzazione ridefinisce di routine gli SLO, ritira la fatica e riequilibra l'investimento in affidabilità man mano che si spostano attività e quadro di rischio.

## Spunti di discussione

- Come dovrebbe un'organizzazione fissare i suoi primi SLO quando non ha dati storici di affidabilità a cui ancorarli?
- Quando il budget di errore è esaurito ma un grande lancio è impegnato, chi ha l'autorità di derogare al congelamento e come viene registrata quella decisione?
- Un SRE centralizzato, incorporato o ibrido è giusto per la vostra organizzazione, e che cosa innescherebbe un cambiamento?
- Come valutate un nove in più di disponibilità rispetto alle funzionalità che lo stesso investimento potrebbe finanziare?
- Che cosa conta come fatica nel vostro contesto, e dov'è il confine tra preziosa valutazione manuale e ripetizione eliminabile?
- Come dovrebbero differire gli obiettivi di affidabilità tra servizi governativi rivolti ai cittadini e strumenti aziendali interni?

## Punti chiave

- L'SRE applica l'ingegneria del software alle operazioni, trattando l'affidabilità come una funzionalità misurabile e finanziabile.
- SLI, SLO e SLA trasformano l'affidabilità da opinione in numeri concordati; mantieni gli SLO più severi degli SLA.
- Il budget di errore allinea sviluppatori e operatori rendendo esplicito e negoziato in anticipo il compromesso tra affidabilità e velocità.
- Misura e limita la fatica e tratta l'automazione come ingegneria di prim'ordine così che le operazioni scalino in modo sub-lineare.
- Pianifica la capacità dalle previsioni di domanda e rispetta i tempi di consegna della predisposizione, specialmente per i picchi stagionali.
- Scegli deliberatamente un modello organizzativo SRE e definisci un chiaro modello di ingaggio e una soglia di prontezza alla produzione.

## Riferimenti e letture di approfondimento

- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy, *Site Reliability Engineering: How Google Runs Production Systems*
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne, *The Site Reliability Workbook: Practical Ways to Implement SRE*
- David N. Blank-Edelman (a cura di), *Seeking SRE: Conversations About Running Production Systems at Scale*
- Thomas A. Limoncelli, Strata R. Chalup, Christina J. Hogan, *The Practice of Cloud System Administration*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
