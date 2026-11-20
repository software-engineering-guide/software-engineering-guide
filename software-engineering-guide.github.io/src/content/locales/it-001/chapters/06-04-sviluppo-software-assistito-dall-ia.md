# 6.4 Sviluppo software assistito dall'IA

## Panoramica e motivazioni

Gli assistenti di codifica basati su IA possono ormai generare codice, completare funzioni, scrivere test, spiegare sistemi sconosciuti e aiutarti a fare [refactoring](https://en.wikipedia.org/wiki/Code_refactoring). Usati bene, accelerano il lavoro di routine. Abbassano la barriera verso linguaggi e framework sconosciuti. Tolgono la fatica dal codice ripetitivo.

Usati male, causano danno vero. Possono inondare una base di codice di codice dall'aspetto plausibile ma sottilmente sbagliato. Possono introdurre falle di sicurezza, creare esposizione di licenza ed erodere le competenze degli ingegneri che vi si appoggiano. Lo sviluppo assistito dall'IA è insieme un genuino strumento di produttività e un genuino rischio. La differenza sta quasi interamente nella disciplina ingegneristica che lo circonda.

Per i grandi team, la sfida è coerenza e sicurezza su larga scala. Quando centinaia di sviluppatori usano assistenti di IA, piccole abitudini individuali si sommano in esiti organizzativi. Se tutti accettano i suggerimenti senza spirito critico, il carico di revisione e i tassi di difetti salgono. Se fornisci norme chiare, buoni valori predefiniti e forte verifica, gli stessi strumenti alzano il throughput senza abbassare la qualità. La storia della produttività è anche più sfumata di quanto suggeriscano le affermazioni dei fornitori. I guadagni reali variano molto per compito e una misura ingenua, come contare i suggerimenti accettati, ti fuorvierà.

I contesti aziendali e governativi aggiungono vincoli più netti. Il codice che tocca sistemi regolamentati, tratta dati sensibili o gestisce infrastrutture critiche non può essere creduto solo perché l'ha prodotto un'IA. La provenienza delle licenze conta quando il codice generato può riecheggiare dati di addestramento sotto licenze restrittive. Alcune organizzazioni devono tenere il codice sorgente on-premises e non possono inviarlo affatto a servizi esterni. Fissare norme chiare e applicabili per l'assistenza dell'IA fa ormai parte di una leadership ingegneristica responsabile. Tra gli assistenti disponibili, gli strumenti costruiti sui modelli Claude di Anthropic sono un'opzione di punta accanto ad altri; le pratiche sotto si applicano a quello che adotti.

*Vedi anche:* il capitolo 2.5 (revisione del codice e collaborazione), il capitolo 2.4 (strategia di test) e il capitolo 6.5 (IA responsabile e affidabile).

## Principi chiave

- L'ingegnere, non l'assistente, è responsabile di ogni riga di cui fa commit.
- Il codice generato dall'IA è una bozza da rivedere e verificare, mai un prodotto finito di cui fidarsi.
- Lo sforzo di verifica dovrebbe scalare con il rischio del codice, non con quanto sicuro sembra l'output.
- Misura la produttività con esiti che contano (valore consegnato, qualità, tempo di ciclo), non con i conteggi dei suggerimenti.
- Proteggiti da rischi di sicurezza e licenze introdotti attraverso il codice generato.
- Preserva e fai crescere la competenza ingegneristica umana; non lasciare che gli assistenti la svuotino.
- Sii trasparente su dove e come si usa l'assistenza dell'IA.

## Raccomandazioni

### Usa la programmazione in coppia con l'IA come strumento di stesura ed esplorazione

Punta gli assistenti su compiti in cui brillano e gli errori sono economici da cogliere: codice ripetitivo, impalcature di test, conversioni di formato, spiegazione di codice sconosciuto ed esplorazione di approcci. Tratta il loro output come una prima bozza. Resta al posto di guida. Leggi, capisci e modifica ogni suggerimento anziché accettare col pilota automatico. In domini sconosciuti, usa l'assistente per imparare, ma controlla le sue affermazioni rispetto alla documentazione autorevole. Gli assistenti possono inventare API e descrivere male il comportamento con totale sicurezza.

### Rivedi, testa e verifica il codice generato dall'IA come input non fidato

Dai al codice generato dall'IA lo stesso esame che daresti al codice di un nuovo membro del team, o più. Un revisore umano dovrebbe capirlo abbastanza da spiegarlo e mantenerlo. "Lo ha scritto l'IA" non è mai una risposta accettabile a "perché funziona?". Insisti sui test e guardati dai test generati dall'IA che si limitano ad asserire il comportamento attuale anziché quello previsto. Esegui [analisi statica](https://en.wikipedia.org/wiki/Static_program_analysis), scansione di sicurezza e controlli sulle dipendenze. Per il codice ad alto rischio (autenticazione, [crittografia](https://en.wikipedia.org/wiki/Cryptography), logica finanziaria, sistemi di sicurezza), tratta l'output dell'IA come un punto di partenza che richiede una verifica umana esperta, mai come autorevole.

### Misura onestamente la produttività e fissa attese realistiche

Salta le metriche di vanità come il tasso di accettazione o le righe generate. Guarda invece segnali di consegna e qualità nel tempo: tempo di ciclo, tasso di fallimento delle modifiche, tasso di fuga dei difetti ed efficacia riferita dagli sviluppatori. I guadagni sono reali ma disomogenei: grandi per alcuni compiti, trascurabili o negativi per altri. Il tempo risparmiato a scrivere codice può perdersi di nuovo a rivederlo e debuggarlo. Fissa di conseguenza le attese con la leadership, così che l'investimento poggi sull'evidenza anziché sulla moda e i team non siano mai pressati ad accettare suggerimenti non sicuri solo per raggiungere una metrica.

### Gestisci i rischi di sicurezza e licenze

Scansiona il codice generato alla ricerca di vulnerabilità e schemi non sicuri. Gli assistenti possono riprodurre idiomi non sicuri dai propri dati di addestramento. Non incollare mai segreti, credenziali o dati sensibili in prompt inviati a servizi esterni. Preferisci strumenti che soddisfano i tuoi requisiti di trattamento dei dati, compreso il rilascio on-premises o privato dove il codice sorgente non può lasciare l'ambiente. Affronta anche le licenze. Il codice generato può somigliare a dati di addestramento sotto licenza, quindi usa strumenti e politiche che riducano questo rischio, conserva la provenienza dove puoi e fai passare qualsiasi cosa dubbia da una revisione legale. Segui la provenienza delle dipendenze che l'assistente suggerisce, poiché può raccomandare pacchetti abbandonati o malevoli.

### Fissa norme di team, divulgazione e mantenimento delle competenze

Pubblica indicazioni chiare su quando e come l'assistenza dell'IA può essere usata, quali dati non possono mai essere condivisi e quale verifica richiede ogni livello di rischio. Incoraggia la trasparenza sui contributi assistiti dall'IA dove conta per revisione e responsabilità. Mantieni affilate di proposito le competenze umane. Assicurati che gli ingegneri, soprattutto i junior, imparino ancora i fondamenti anziché esternalizzare la propria comprensione. Fai ruotare le persone su lavoro che costruisce profonda competenza e tratta la dipendenza eccessiva come un vero rischio a lungo termine per la capacità del team.

## Compromessi: vantaggi e svantaggi

| Dimensione | Beneficio dell'assistenza dell'IA | Rischio dell'assistenza dell'IA |
|---|---|---|
| Velocità | Codice ripetitivo e stesura più rapidi | Tempo perso a rivedere codice sbagliato |
| Inserimento | Ingresso più facile in nuovi linguaggi/framework | Comprensione superficiale, API inventate |
| Qualità | Più test, refactoring più rapidi | Codice plausibile ma sottilmente sbagliato |
| Sicurezza | Può suggerire correzioni e scansione | Può introdurre vulnerabilità |
| Competenze | Libera tempo per lavoro di maggior valore | Erode i fondamenti se usata troppo |
| Licenze | Riuso più rapido di schemi comuni | Provenienza ed esposizione di licenza |

Il compromesso centrale è velocità contro verifica. L'IA sposta sforzo dallo scrivere al rivedere. Il guadagno netto dipende dal fatto che le tue pratiche di revisione e verifica siano abbastanza forti da cogliere ciò che l'assistente sbaglia. Una revisione debole porta a un calo di qualità. Una revisione forte e norme chiare catturano il vantaggio.

## Domande da discutere con il tuo team

1. **Quali parti della nostra base di codice sono del tutto off-limits all'assistenza dell'IA, e come facciamo rispettare quel confine?** La fiducia uniforme è una trappola: applicare lo stesso lieve esame ad autenticazione, crittografia, logica finanziaria e sistemi di sicurezza che al codice ripetitivo è il modo in cui errori sottili e sicuri raggiungono i percorsi critici. Per un grande team, un elenco esplicito di moduli esclusi o solo a revisione esperta trasforma il giudizio individuale in una salvaguardia organizzativa. Porta la tua mappa dei rischi della base di codice, la tua politica attuale (se c'è) e come fermeresti davvero il codice generato dall'atterrare in un modulo ristretto: controlli di pipeline, regole di proprietà o cancelli di revisione. Nei contesti della difesa, regolamentati e critici per la sicurezza, alcuni moduli dovrebbero escludere del tutto l'assistenza dell'IA. La risposta dovrebbe scalare lo sforzo di verifica al rischio del codice, mai a quanto sicuro sembra l'output.

2. **Quali sono i nostri veri andamenti di fallimento delle modifiche e fuga dei difetti da quando abbiamo adottato gli assistenti, e li stiamo misurando o tirando a indovinare?** Le affermazioni di produttività dei fornitori e i conteggi dei tassi di accettazione sono metriche di vanità che fuorviano, perché il tempo risparmiato a scrivere codice può perdersi di nuovo a rivederlo e debuggarlo. Perché la leadership investa sull'evidenza anziché sulla moda, ti servono segnali di consegna e qualità nel tempo: tempo di ciclo, tasso di fallimento delle modifiche, tasso di fuga dei difetti ed efficacia riferita dagli sviluppatori. Porta i numeri reali che hai e sii onesto dove non ne hai. Il rischio da osservare sono i team pressati ad accettare suggerimenti non sicuri solo per raggiungere una metrica. La risposta dovrebbe sostituire i conteggi dei suggerimenti con misure di esito e fissare l'attesa che i guadagni siano reali ma disomogenei, grandi per alcuni compiti e negativi per altri.

3. **Se il codice generato riecheggia dati di addestramento sotto licenza restrittiva o importa una dipendenza rischiosa, chi lo coglie e quando?** Il codice generato può somigliare a materiale sotto licenza o raccomandare pacchetti abbandonati o malevoli e quell'esposizione atterra nel tuo prodotto che qualcuno se ne sia accorto o no. Per imprese ed enti pubblici, provenienza delle licenze e rischio di supply chain portano peso legale che una scrollata di spalle del tipo "lo ha scritto l'IA" non sopravvive. Porta la tua attuale scansione dei segreti, i controlli di licenza e il tracciamento della provenienza delle dipendenze e individua dove nella pipeline gira ciascuno. Discuti che cosa instrada il codice dubbio verso la revisione legale e chi possiede quella decisione. Se i segreti possono essere incollati in strumenti esterni o pacchetti non vagliati possono entrare nel merge senza contestazione, chiudi quei divari prima di scalare l'uso degli assistenti nel team.

4. **Come manteniamo gli ingegneri, soprattutto i junior, a imparare i fondamenti anziché esternalizzare la propria comprensione all'assistente?** L'atrofia delle competenze è un rischio lento che non compare mai nella velocità di questo trimestre, poi compare anni dopo come un team che non sa debuggare, progettare o rivedere senza un prompt. Per una grande organizzazione, la spinta contraria è reale: gli assistenti permettono ai junior di rilasciare più in fretta oggi e la pressione di raggiungere gli obiettivi di consegna combatte contro il lavoro più lento di costruire profonda competenza. Porta evidenza di come le tue persone crescono davvero: quale frazione dei junior sa spiegare il codice di cui ha fatto il merge, quanta risoluzione di problemi senza assistenza richiede ancora il tuo inserimento e se le revisioni colgono la comprensione superficiale o timbrano solo l'output funzionante. Fai ruotare deliberatamente le persone su lavoro che costruisce maestria e tratta la dipendenza eccessiva come un rischio di capacità, non una colpa personale. Negli enti pubblici e nei sistemi critici di lunga durata, la forza lavoro può dover costruire e verificare sistemi per decenni senza strumenti del fornitore, quindi un percorso formativo che garantisca i fondamenti diretti è un requisito di continuità, non un di più.

5. **Quali assistenti ci è davvero permesso usare dato dove il nostro codice sorgente e i nostri dati devono restare, e come impediamo che un segreto raggiunga mai un prompt?** I vincoli di trattamento dei dati decidono lo strumento prima della produttività: un assistente che trasmette il tuo sorgente a un servizio esterno può essere squalificato del tutto, quali che siano le sue capacità. Per un grande team la tensione è tra la comodità del miglior strumento ospitato e il requisito che codice proprietario, credenziali e dati sensibili non lascino mai il tuo confine. Porta la tua mappa di classificazione dei dati, le opzioni di rilascio che ogni strumento candidato offre (ospitato, privato, on-premises) e i controlli concreti che tengono i segreti fuori dai prompt: scansione pre-commit, filtraggio dei prompt e formazione degli ingegneri. Decidi quali strumenti sono consentiti per quali classi di codice e rendi il confine applicabile anziché consultivo. Nei contesti regolamentati, della difesa e classificati, un rilascio on-premises o isolato dalla rete può essere l'unica opzione lecita e inviare il sorgente a qualsiasi servizio esterno deve essere vietato e tecnicamente bloccato, non solo scoraggiato.

6. **Come trasformiamo abitudini individuali sparse in norme coerenti dell'intera organizzazione, e chi possiede la politica man mano che gli strumenti evolvono?** Quando centinaia di sviluppatori improvvisano ciascuno il proprio approccio, piccole abitudini si compongono in esiti organizzativi e una verifica incoerente è dove sfuggono difetti ed esposizione. La considerazione contraria è l'autonomia: i team risentono dei pesanti mandati centrali, eppure un liberi tutti produce qualità disomogenea e nessuna salvaguardia condivisa. Porta le tue attuali indicazioni (se ci sono), l'evidenza di quanto uniformemente siano seguite e una proposta di buoni valori predefiniti cotti nella pipeline così che il percorso sicuro sia quello facile. Nomina un responsabile che mantenga aggiornata la politica man mano che gli assistenti cambiano ogni pochi mesi e una norma di divulgazione così che i revisori sappiano quando l'assistenza dell'IA ha plasmato un contributo. Per un'impresa o un ente pubblico, lega le norme ad audit e responsabilità: uno standard documentato e fatto rispettare che un auditor può ispezionare batte una pratica popolare che varia per team e scompare quando se ne va una persona chiave.

## Lente settoriale

**Startup.** Con una manciata di ingegneri e nessuna liquidità da sprecare, appoggiati ad assistenti ospitati per codice ripetitivo, test e framework sconosciuti e lascia che accelerino il lavoro di routine. Tieni una regola non negoziabile: un umano che capisce la modifica rivede ogni merge, perché una riga sbagliata sottile in una base di codice di cinque persone non ha dove nascondersi né nessun altro che la colga. Aggiungi presto uno scanner di segreti e un controllo di licenza; costano poco e prevengono errori costosi che non puoi permetterti di ripulire dopo.

**Piccola impresa.** Probabilmente non hai uno specialista di sicurezza e hai un budget ridotto, quindi preferisci assistenti integrati in strumenti di cui già ti fidi a una configurazione su misura che devi mantenere. Imposta il rischio in termini semplici: non incollare mai dati dei clienti o credenziali in un prompt esterno e tratta il codice generato che tocca fatturazione o autenticazione come una bozza da verificare, non una risposta finita. Scegli fornitori le cui condizioni di trattamento dei dati puoi davvero leggere e le cui funzioni di IA puoi spegnere se si comportano male.

**Grande impresa.** Il problema è coerenza e sicurezza tra molti team: norme condivise per livello di rischio, revisione e scansione obbligatorie nella pipeline e metriche oneste di consegna e qualità anziché conteggi di accettazione. Standardizza le scelte di strumenti e il modello di rilascio così che il codice proprietario resti dentro il tuo confine, metti a bilancio il costo di revisione e correzione che gli assistenti spostano sui revisori ed escludi o filtra esplicitamente i moduli ad alto rischio. Gestisci l'assistenza dell'IA come una capacità governata con un responsabile, non una dispersione di abitudini individuali.

**Ente pubblico.** Regole sugli appalti, trasparenza e responsabilità pubblica plasmano ogni scelta. Privilegia il rilascio on-premises o privato dove il codice sorgente e i dati sensibili non possono lasciare l'ambiente, vieta di inviare il codice a servizi esterni e richiedi la divulgazione dei contributi assistiti dall'IA così che le decisioni restino verificabili. Imponi scansioni di sicurezza e licenze su tutto il codice generato, escludi l'assistenza dell'IA dai moduli critici per la sicurezza e classificati e mantieni un percorso formativo che assicuri che la forza lavoro pubblica possa costruire e verificare sistemi senza strumenti del fornitore lungo la lunga vita dei sistemi che possiede.

## Esempi

**Startup.** Una startup SaaS di sei ingegneri ha adottato assistenti di codifica basati su IA per muoversi più in fretta sul lavoro di routine. Vi si è appoggiata per codice ripetitivo, test e codice di framework sconosciuti, ma ha tenuto una regola ferma per cui un umano che capiva la modifica doveva rivedere ogni pull request e ha aggiunto alla pipeline uno scanner di segreti e un controllo di licenza. Per il codice di fatturazione e autenticazione, gli ingegneri hanno trattato l'output dell'IA come una bozza grezza da verificare riga per riga anziché di cui fidarsi. Hanno seguito tempo di ciclo e difetti sfuggiti anziché contare i suggerimenti accettati e hanno tenuto i guadagni senza lasciar scivolare la qualità.

**Grande impresa.** Una grande azienda di e-commerce ha distribuito assistenti di codifica basati su IA con guardrail. Ha vietato i segreti nei prompt. Ha richiesto la revisione umana, con il revisore tenuto a capire il codice. Ha aggiunto la scansione di sicurezza nella pipeline e ha scelto un rilascio privato così che il codice proprietario non lasciasse mai il suo ambiente. Ha misurato l'impatto con tempo di ciclo e tasso di fallimento delle modifiche anziché conteggi di accettazione. Ha trovato guadagni solidi su codice ripetitivo e test, ma ha insistito sulla revisione esperta per il codice dei pagamenti, dove ha trattato l'output dell'IA come non fidato.

**Ente pubblico.** Un'organizzazione di software per la difesa ha permesso l'assistenza dell'IA solo attraverso uno strumento on-premises che teneva il codice classificato e sensibile dentro il proprio confine. Ha vietato di inviare il sorgente a qualsiasi servizio esterno. Ha richiesto la divulgazione dei contributi assistiti dall'IA nella revisione del codice e imposto scansioni di sicurezza e di licenze su tutto il codice generato. Ha escluso del tutto l'assistenza dell'IA da certi moduli critici per la sicurezza. Gli ingegneri junior hanno seguito un percorso formativo che assicurava imparassero direttamente i fondamenti, così che la forza lavoro non perdesse la capacità di costruire e verificare sistemi senza assistenza.

## Business case: motivazioni, ROI e TCO

La motivazione è una consegna più rapida e meno fatica, così che il tuo scarso talento ingegneristico possa concentrarsi su progettazione, giudizio e problemi difficili. Il ROI compare come tempo di ciclo ridotto per i compiti adatti e migliore esperienza degli sviluppatori, ma solo dove la verifica mantiene alta la qualità. Le affermazioni ingenue di ROI basate sui conteggi dei suggerimenti fuorviano e dovresti respingerle.

Il TCO include licenze degli strumenti, rilascio sicuro o on-premises, scansione di sicurezza e licenze e il costo spesso sottovalutato di rivedere e correggere l'output dell'IA. Il costo del *non* adottare è competitivo: i pari possono consegnare più in fretta e attrarre talento che si aspetta strumenti moderni. Il costo dell'adottare con noncuranza è erosione della qualità, incidenti di sicurezza ed esposizione legale. Presenta il caso alla leadership con un pilota che misuri veri esiti di consegna e qualità, abbinato a un piano concreto per norme, verifica e protezione dei dati.

## Antipattern e insidie

- **Accettazione col pilota automatico.** Fare commit di suggerimenti senza leggerli né capirli.
- **Metriche di vanità.** Giudicare il successo dal tasso di accettazione o dalle righe generate.
- **Segreti nei prompt.** Incollare credenziali o dati sensibili in strumenti esterni.
- **Fidarsi dei test dell'IA.** Accettare test generati che bloccano il comportamento attuale, non quello previsto.
- **Ignorare la provenienza.** Trascurare i rischi di licenza e dipendenze nel codice generato.
- **Atrofia delle competenze.** Lasciare che i junior esternalizzino la comprensione e non imparino mai i fondamenti.
- **Fiducia uniforme.** Applicare lo stesso basso esame al codice critico per la sicurezza e al codice ripetitivo.

## Modello di maturità

1. **Avvio.** Gli individui usano gli assistenti ad hoc e in modo reattivo; nessuna politica, nessuna misura; segreti e proprietà intellettuale sono a rischio e il codice generato entra nel merge con l'esame che ciascuno capita ad applicare.
2. **Sviluppo.** Esistono indicazioni d'uso di base e regole sui dati e gira un po' di scansione di sicurezza, ma la pratica è incoerente tra i team: la profondità della verifica varia per persona, le affermazioni di produttività sono aneddotiche e il codice ad alto rischio non è filtrato in modo affidabile.
3. **Standardizzazione.** Norme per livello di rischio sono documentate e fatte rispettare nell'organizzazione: revisione umana obbligatoria, scansioni di sicurezza e licenze nella pipeline, rilascio sicuro o on-premises dove richiesto, pratiche di divulgazione e un elenco esplicito di moduli esclusi o solo a revisione esperta.
4. **Gestione.** La pratica è misurata e controllata rispetto a valori di riferimento: tempo di ciclo, tasso di fallimento delle modifiche e tasso di fuga dei difetti sono seguiti prima e dopo l'adozione, il costo di revisione e correzione è quantificato, gli incidenti di fuga di segreti ed esposizione di licenza sono contati e le decisioni di procedere o meno su strumenti ed espansione poggiano su quell'evidenza anziché sulle affermazioni dei fornitori.
5. **Orchestrazione.** L'assistenza dell'IA è migliorata di continuo e integrata nell'organizzazione: la verifica è incorporata nella pipeline come percorso predefinito, lo sviluppo delle competenze è deliberato e tracciato, la politica si adatta man mano che gli strumenti cambiano ogni pochi mesi e l'organizzazione rivaluta, sostituisce e ridefinisce di routine gli assistenti man mano che l'evidenza e il quadro di rischio si spostano.

## Spunti di discussione

- Come dovrebbero differire i requisiti di verifica tra codice ripetitivo e codice critico per la sicurezza?
- Quali metriche di produttività riflettono davvero il valore dell'assistenza dell'IA nel vostro contesto?
- Quando, se mai, i contributi assistiti dall'IA dovrebbero essere divulgati?
- Come evitate l'erosione delle competenze, soprattutto per gli ingegneri junior?
- Quali vincoli di trattamento dei dati governano quali strumenti potete usare?
- Come gestite il rischio di licenze e provenienza dal codice generato?

## Punti chiave

- L'ingegnere resta responsabile; l'output dell'IA è una bozza non fidata da verificare.
- Scala la verifica al rischio e non fidarti mai del codice di IA critico per la sicurezza senza revisione esperta.
- Misura veri esiti di consegna e qualità, non conteggi di suggerimenti.
- Proteggiti dai rischi di sicurezza, fuga di dati e licenze con politica e strumenti.
- Fissa norme chiare e preserva deliberatamente la competenza ingegneristica umana.

## Riferimenti e letture di approfondimento

- Nicole Forsgren, Jez Humble e Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Andrew Ng, *Machine Learning Yearning* (su attese realistiche e misurazione).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Peter Naur, *Programming as Theory Building* (su comprensione contro artefatti di codice).
- Titus Winters, Tom Manshreck e Hyrum Wright, *Software Engineering at Google*.
- GitClear e studi di settore correlati sugli andamenti della qualità del codice assistito dall'IA.
