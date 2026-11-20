# 3.9 Ingegneria dei sistemi

## Panoramica e motivazioni

L'[ingegneria dei sistemi](https://en.wikipedia.org/wiki/Systems_engineering) è la disciplina che progetta un intero sistema complesso da un capo all'altro, così che tutte le sue parti lavorino insieme per soddisfare un bisogno reale. Le parti comprendono molto più del software. Un sistema moderno combina di solito software, hardware, persone, dati e processi e deve operare in un mondo reale disordinato. L'ingegneria dei sistemi mantiene tutto questo allineato per l'intera vita del sistema.

È diversa dall'architettura del software. L'architettura del software (capitolo 3.1) decide come i componenti software sono strutturati e come dialogano tra loro. L'ingegneria dei sistemi sta un livello più in alto. Si chiede che cosa il sistema nel suo insieme debba fare, come software, hardware e operatori umani si dividono il lavoro e come proverai che la cosa finita funziona. La sua casa professionale è [INCOSE](https://en.wikipedia.org/wiki/International_Council_on_Systems_Engineering), l'International Council on Systems Engineering, e il suo standard di riferimento è la [ISO/IEC/IEEE 15288](https://en.wikipedia.org/wiki/ISO/IEC_15288), che definisce i processi per la vita di un sistema.

Questo conta per i grandi programmi aziendali e governativi perché i loro sistemi sono grandi, di lunga durata e critici per la sicurezza o per la missione. Una piattaforma di difesa, un sistema di traffico aereo o una costellazione di satelliti fonde hardware su misura, componenti di terze parti, software embedded e cloud e operatori umani, e nessun singolo team può tenere il tutto in testa. Spesso si costruisce anche un [sistema di sistemi](https://en.wikipedia.org/wiki/System_of_systems): molti sistemi indipendenti, ciascuno utile da solo, che devono cooperare per fornire una capacità più grande.

Questo capitolo si collega ai requisiti del software (capitolo 2.8), ai fondamenti dell'architettura (capitolo 3.1), ai modelli e metodi del software (capitolo 2.12), all'interoperabilità e agli standard aperti (capitolo 3.8) e alla gestione dei progetti (capitolo 10.6).

## Principi chiave

- **Progetta il tutto, non le parti.** Un sistema ha successo o fallisce come insieme, quindi ottimizzare un sottosistema in isolamento può peggiorare il tutto.
- **Segui il ciclo di vita.** Un sistema ha una vita dal primo concetto al ritiro finale. Pianificala tutta, non solo la costruzione.
- **Traccia ogni requisito.** Ogni bisogno dovrebbe corrispondere a un requisito, a un elemento di progetto e a un test. Se non puoi tracciarlo, non puoi provarlo.
- **Gestisci le interfacce di proposito.** La maggior parte dei fallimenti avviene ai confini tra le parti, quindi le interfacce meritano proprietà e controllo espliciti.
- **Verifica e convalida separatamente.** Costruire la cosa nel modo giusto (verifica) e costruire la cosa giusta (convalida) sono domande diverse, e servono entrambe le risposte.
- **Aspettati comportamento emergente.** Combinare le parti crea comportamenti che nessuna parte mostra da sola. Alcuni sono lo scopo, altri sono una brutta sorpresa.
- **Co-progetta hardware e software.** Quando entrambi sono su misura, le decisioni dell'uno vincolano l'altro, quindi pianificali insieme.

## Raccomandazioni

### Gestisci l'intero ciclo di vita del sistema

Tratta il sistema come dotato di una vita intera e pianifica ogni fase. Un ciclo di vita comune procede così: **concetto** (capire il bisogno ed esplorare le opzioni), **requisiti** (dichiarare con precisione che cosa il sistema deve fare), **progetto** (decidere l'architettura e le parti), **integrazione** (mettere insieme le parti), **verifica e convalida** (provare che funziona ed è il sistema giusto), **esercizio** (farlo funzionare e mantenerlo) e **ritiro** (dismetterlo in sicurezza, compresi dati e smaltimento). La ISO/IEC/IEEE 15288 ti dà un quadro di processi per questo. Le fasi non devono essere una cascata rigida; puoi iterare, fare prototipi e consegnare incrementi. Il punto è affrontare consapevolmente ogni fase, comprese quelle successive e costose che i piani iniziali spesso ignorano.

### Cattura i bisogni degli stakeholder e alloca i requisiti con tracciabilità

Parti dalle persone a cui il sistema sta a cuore: utenti, operatori, proprietari, regolatori e pubblico. Raccogli i loro **bisogni** in linguaggio semplice, poi trasformali in **requisiti** ingegnerizzati, specifici e verificabili (vedi capitolo 2.8). Segue l'**allocazione dei requisiti**: assegnare ogni requisito di livello di sistema a un sottosistema specifico, così da sapere quale parte è responsabile di soddisfarlo. Tieni una matrice di **[tracciabilità](https://en.wikipedia.org/wiki/Requirements_traceability)**, un registro vivo che collega ogni bisogno al suo requisito, all'elemento di progetto che lo soddisfa e al test che lo verifica. Ti permette di provare in qualsiasi momento che ogni bisogno è coperto e che ogni parte esiste per una ragione.

### Gestisci le interfacce in modo esplicito

Le interfacce sono dove le parti si incontrano, e dove i sistemi si rompono più spesso. Un'interfaccia può essere un connettore fisico, un protocollo di rete, un formato di dati o una procedura umana. Per ognuna, scrivi un **Interface Control Document** (ICD): una specifica concordata di come esattamente due parti si connettono e si scambiano informazioni. Dai a ogni interfaccia un chiaro responsabile da ciascun lato. Appoggiarsi a specifiche condivise e pubblicate anziché a connettori una tantum rende l'integrazione molto più facile, ed è l'argomento di interoperabilità del capitolo 3.8. Congela presto le interfacce dove puoi, perché una modifica tardiva si ripercuote su ogni parte che le tocca.

### Integra, poi verifica e convalida

L'**integrazione di sistema** combina i sottosistemi nel tutto funzionante, di solito per fasi anziché tutto insieme, così da trovare i problemi mentre sono ancora piccoli. Dopo l'integrazione viene la **[verifica e convalida](https://en.wikipedia.org/wiki/Verification_and_validation)** (V&V), due controlli distinti. La **verifica** chiede: abbiamo costruito il sistema nel modo giusto, cioè soddisfa i requisiti specificati? Si verifica attraverso ispezione, analisi, dimostrazione e test. La **convalida** chiede: abbiamo costruito il sistema giusto, cioè soddisfa i bisogni reali degli stakeholder nell'uso reale? Un sistema può superare la verifica (rispetta la specifica) eppure fallire la convalida (la specifica era sbagliata). Pianifica entrambe presto e scrivi requisiti e interfacce in modo che possano essere verificati fin dall'inizio.

### Adotta l'ingegneria dei sistemi basata su modelli

L'ingegneria dei sistemi tradizionale produceva montagne di documenti che si disallineavano. L'**[ingegneria dei sistemi basata su modelli](https://en.wikipedia.org/wiki/Model-based_systems_engineering)** (MBSE) sostituisce quella pila con un unico modello formale e condiviso del sistema, da cui vengono generate viste e rapporti. Il linguaggio di modellazione comune è **[SysML](https://en.wikipedia.org/wiki/Systems_Modeling_Language)** (Systems Modelling Language), un linguaggio grafico per descrivere requisiti, struttura, comportamento e vincoli di un sistema. Poiché tutto vive in un unico modello connesso, una modifica si aggiorna ovunque e la tracciabilità diventa una query anziché un inseguimento manuale. L'MBSE si collega alle idee di modellazione del capitolo 2.12. Adottala gradualmente, partendo dalle parti a più alto rischio dove un modello condiviso rende più in fretta.

### Applica il pensiero sistemico al comportamento emergente

Pratica il [pensiero sistemico](https://en.wikipedia.org/wiki/Systems_thinking): ragiona sul tutto e sulle relazioni tra le parti, non solo sulle parti una alla volta. È così che anticipi il **[comportamento emergente](https://en.wikipedia.org/wiki/Emergence)**: proprietà che compaiono solo quando le parti si combinano e che nessuna parte mostra da sola. La buona emergenza è spesso lo scopo del sistema (uno sciame di droni copre un'area che nessun drone da solo potrebbe). La cattiva emergenza è il fallimento a sorpresa (due sottosistemi sicuri interagiscono creando uno stato pericoloso). Non puoi eliminare con i test l'emergenza da un sistema che non hai mai modellato, quindi usa simulazione e analisi strutturata dei pericoli per trovarla prima dell'esercizio.

### Co-progetta hardware e software

Quando un sistema include hardware su misura, progetta insieme hardware e software, una pratica chiamata **[co-progettazione hardware/software](https://en.wikipedia.org/wiki/Hardware/software_co-design)**. Le decisioni si vincolano a vicenda: l'hardware fissa i limiti di tempi, memoria e alimentazione entro cui il software deve vivere e i bisogni del software plasmano ciò che l'hardware deve fornire. I lunghi tempi di consegna dell'hardware guidano anche il calendario. Decidi presto quali funzioni vivono nell'hardware e quali nel software e riesamina quella ripartizione man mano che emergono i vincoli.

## Compromessi: vantaggi e svantaggi

| Approccio | Vantaggi | Svantaggi / costo |
|---|---|---|
| Piena rigorosità dell'ingegneria dei sistemi | Meno sorprese tardive, forte tracciabilità, più sicuro e verificabile | Alto costo iniziale, partenza più lenta, processo pesante |
| Approccio leggero / solo software | Veloce, economico, flessibile per ambiti piccoli | Cede sui grandi sistemi multi-disciplina, perde interfacce ed emergenza |
| Basato su modelli (MBSE) | Unica fonte di verità, tracciabilità facile, viste coerenti | Costo di strumenti e formazione, cambio di cultura, curva di apprendimento |
| Ingegneria dei sistemi basata su documenti | Familiare, basso costo di strumenti, facile da condividere | I documenti si disallineano, tracciabilità manuale e soggetta a errori |

Il compromesso centrale è rigore contro velocità. La piena ingegneria dei sistemi anticipa lo sforzo su concetto, requisiti e lavoro sulle interfacce. Quello sforzo si ripaga molte volte sui sistemi grandi, di lunga durata e critici per la sicurezza, dove un difetto trovato in esercizio può costare migliaia di volte più dello stesso difetto trovato nei requisiti. Su un prodotto piccolo, di breve durata e solo software, quel rigore è eccessivo. Adegua il peso del tuo processo a dimensione, durata e rischio del sistema. La modalità di fallimento è applicare abitudini da progetto usa e getta a un sistema che girerà per trent'anni e porterà rischio nel mondo reale.

## Domande da discutere con il tuo team

1. **Dove avete costruito esattamente ciò che la specifica richiedeva e rilasciato comunque il sistema sbagliato, e che cosa l'avrebbe colto?** Verifica (l'abbiamo costruito bene) e convalida (abbiamo costruito la cosa giusta) rispondono a domande diverse, e un sistema può superare ogni test di verifica fallendo la convalida perché la specifica stessa era sbagliata. Nei grandi programmi le due vengono ridotte a "testing", così nessuno convalida rispetto al bisogno reale dell'operatore fino a tardi, quando una correzione costa migliaia di volte più di una modifica ai requisiti. Porta un esempio passato in cui il sistema consegnato rispettava i requisiti ma mancava il bisogno reale e chiediti quale attività di convalida (una simulazione con operatori reali, un prototipo precoce sul campo) l'avrebbe fatto emergere prima. Pianifica entrambi i controlli fin dall'inizio e scrivi requisiti e interfacce in modo che possano essere verificati. La distinzione decide dove spendi il tuo scarso sforzo di revisione.

2. **Come cercate il cattivo comportamento emergente prima che il sistema sia in esercizio, non dopo?** Combinare sottosistemi sicuri può creare stati pericolosi che nessuna parte mostra da sola, e non puoi eliminare con i test l'emergenza da un sistema che non hai mai modellato. Per un programma critico per la sicurezza o per la missione, l'interazione a sorpresa è quella che ferisce qualcuno o fa fallire la missione, quindi va trovata prima dell'esercizio reale. Porta il tuo approccio alla modellazione del tutto (simulazione, analisi strutturata dei pericoli, un modello SysML che catturi le interazioni) e chiediti quali comportamenti tra sottosistemi hai davvero esplorato rispetto a quali hai dato per scontati. La buona emergenza è spesso lo scopo del sistema e vale la pena progettare verso di essa; la cattiva emergenza è il fallimento contro cui devi ingegnerizzare. Se la tua unica strategia di integrazione è collegare le parti e vedere che cosa succede, stai pianificando di scoprire l'emergenza in produzione.

3. **Quando devono essere congelate le decisioni hardware a lungo tempo di consegna, e come quella scadenza guida il vostro calendario software?** Quando un sistema include hardware su misura, i due devono essere co-progettati: il chip fissa i tetti di tempi, memoria e alimentazione entro cui vive il software, e i tempi di consegna dell'hardware dominano spesso l'intero calendario. I team che trattano il software come separabile ottimizzano localmente e poi si scontrano con i vincoli hardware all'integrazione, perdendo mesi. Porta i tempi di consegna dell'hardware e la data entro cui deve essere decisa la ripartizione delle funzioni tra hardware e software e riesamina quella ripartizione man mano che emergono i vincoli anziché congelarla alla cieca. Prima decidi quali funzioni vivono nel silicio e quali nel software, meno inversioni costose affronti. Le interfacce tra i due meritano un Interface Control Document e un responsabile da ciascun lato, perché una modifica tardiva lì si ripercuote su tutto ciò che le tocca.

4. **Potete tracciare un singolo bisogno di stakeholder fino al requisito, all'elemento di progetto e al test che lo prova, e chi tiene vivo quel collegamento?** La tracciabilità è ciò che ti permette di mostrare in qualsiasi momento che ogni bisogno è coperto e ogni parte esiste per una ragione, eppure in un grande programma la matrice marcisce nell'istante in cui nessuno la possiede. La spinta contraria è reale: gli ingegneri vivono la tracciabilità come burocrazia, e una matrice mantenuta a mano si disallinea più in fretta di quanto cambi il progetto. Porta un filo autentico da un programma in corso e prova a percorrerlo da un capo all'altro nella stanza, da un bisogno di stakeholder nominato, al requisito allocato, al sottosistema e all'elemento di progetto che lo soddisfa, al test di verifica, e nota dove la catena si spezza. Decidi chi possiede la matrice e se dovrebbe vivere in un modello dove la tracciabilità è una query anziché un inseguimento manuale. Per i programmi aziendali e governativi, la matrice è anche l'artefatto di audit che regolatori e autorità di acquisizione richiedono, quindi una catena spezzata fa più che rallentare l'ingegneria; può bloccare la certificazione o il pagamento.

5. **Un approccio basato su modelli vale il suo costo di strumenti e di cultura per voi, o diventerebbe costosa shelfware?** L'ingegneria dei sistemi basata su documenti è familiare ed economica da strumentare, ma i suoi documenti si disallineano e la sua tracciabilità è manuale e soggetta a errori; l'MBSE sostituisce la pila con un unico modello connesso, al prezzo di strumenti, formazione e un vero cambio di cultura. Entrambi gli estremi sono costosi: salta l'MBSE su un grande programma multi-disciplina e paghi in sorprese di integrazione, adottala senza la disciplina di tenere aggiornato il modello e marcisce in shelfware peggio di nessun modello. Porta una lettura onesta della maturità dei tuoi strumenti, di chi nel team può davvero redigere e mantenere un modello SysML e di quale singolo sottosistema ad alto rischio potrebbe fare da pilota dell'approccio, dove un modello condiviso rende più in fretta. Decidi gradualmente anziché imporre tutta l'organizzazione in una volta. Per un grande programma aziendale o governativo con molti fornitori, valuta se un modello condiviso sia l'unico modo realistico per mantenere coerenti requisiti, interfacce e test tra appaltatori che altrimenti si scambiano documenti vecchi.

6. **Il vostro piano del ciclo di vita finanzia seriamente esercizio e ritiro, o si ferma in silenzio al lancio?** Le fasi che dominano il costo totale di un sistema di lunga durata, farlo funzionare per decenni e dismetterlo in sicurezza, sono quelle che i piani iniziali ignorano di routine, perché la pressione è sempre di rilasciare. La considerazione contraria è che denaro e attenzione sono più scarsi proprio quando queste fasi successive sembrano più lontane, quindi esercizio, manutenzione, migrazione dei dati e smaltimento vengono rinviati finché diventano una corsa costosa e rischiosa. Porta il piano attuale del ciclo di vita e controlla se nomina responsabili, bilanci e criteri di uscita per esercizio e ritiro, o se tratta il lancio come il traguardo. Chiediti che cosa succede a dati e hardware a fine vita e chi paga gli anni di manutenzione nel frattempo. Per i sistemi aziendali e governativi che devono funzionare per vent'anni o trent'anni e poi ritirarsi sotto il controllo pubblico, una dismissione non pianificata può violare obblighi normativi, ambientali o di conservazione dei registri, quindi il ritiro appartiene al piano e al bilancio fin dalla prima revisione del concetto.

## Lente settoriale

**Startup.** Un team minuscolo non può condurre un programma formale di ingegneria dei sistemi e non dovrebbe provarci, ma può comunque trattare firmware, app e cloud come un solo sistema anziché tre progetti separati. Scrivi un breve documento di interfaccia che fissi come le parti dialogano, tieni una semplice tabella che collega ogni bisogno del cliente alla parte che lo soddisfa e salta il processo pesante. La tua risorsa più scarsa è l'attenzione ingegneristica, quindi spendi sforzo di tracciabilità solo dove un'ipotesi sbagliata a un confine romperebbe in silenzio il prodotto sul campo.

**Piccola impresa.** Senza un ingegnere di sistemi dedicato e con un budget ridotto, appoggiati a standard pubblicati e a sottosistemi acquistati anziché a un'integrazione su misura che devi progettare e verificare da solo. Privilegia i fornitori che espongono chiare specifiche di interfaccia così che le parti si incastrino senza un connettore personalizzato che dovresti possedere per sempre. Imposta la scelta tra costruire e comprare attorno a quali interfacce puoi realisticamente controllare e verificare per la vita del prodotto e compra il resto.

**Grande impresa.** Su larga scala il problema è la coerenza tra molti team e fornitori: un processo di ciclo di vita condiviso allineato alla ISO/IEC/IEEE 15288, un Interface Control Document e un responsabile nominato per ogni confine con i fornitori e una tracciabilità da capo a capo così che la modifica di un componente non scateni una corsa a livello di programma. Investi nell'MBSE dove un modello condiviso mantiene allineati requisiti, interfacce e test tra gli appaltatori. Governa il processo così che verifica e convalida restino distinte e ogni requisito sia allocato a una parte responsabile.

**Ente pubblico.** Regole sugli appalti, trasparenza e responsabilità pubblica plasmano ogni scelta. Specifica nel contratto il processo di ingegneria dei sistemi, la tracciabilità e le evidenze di V&V, richiedi ai fornitori di consegnare documenti di controllo delle interfacce e artefatti del ciclo di vita che puoi verificare e riserva la convalida di sicurezza e di missione a una revisione indipendente con operatori reali prima di qualsiasi passaggio in esercizio. Pianifica e finanzia esplicitamente esercizio e ritiro, perché un programma pubblico risponde dell'intero ciclo di vita, compresi dismissione sicura e conservazione dei registri.

## Esempi

**Startup.** Una startup hardware di quattro persone che costruisce un sensore connesso non può permettersi un programma formale di ingegneria dei sistemi, ma tratta comunque il prodotto come un solo sistema di firmware, app mobile e backend cloud anziché tre progetti separati. Scrive un breve documento di interfaccia che fissa come dispositivo, app e server dialogano (formati dei messaggi, unità, codici di errore) e tiene una semplice tabella che collega ogni bisogno del cliente alla parte che lo soddisfa. Quando un chip sensore più economico impone una modifica al firmware, quell'interfaccia condivisa mostra subito che cosa app e backend devono adeguare, così che la sostituzione di un componente non rompa in silenzio il prodotto sul campo.

**Grande impresa.** Un costruttore automobilistico globale realizza una nuova piattaforma di veicolo elettrico: un sistema di software (gestione della batteria, assistenza alla guida, infotainment), hardware (motori, sensori, chip) e fattori umani, più molti fornitori che consegnano ciascuno dei sottosistemi. L'azienda conduce un programma di ingegneria dei sistemi. I bisogni degli stakeholder alimentano requisiti allocati, ogni interfaccia con i fornitori ha un Interface Control Document e un modello SysML lega requisiti a progetto e a test. Quando un fornitore di celle per batterie cambia un componente, il modello di tracciabilità mostra esattamente quali requisiti, interfacce e test sono interessati, così che la modifica sia contenuta anziché innescare una corsa a livello di programma.

**Ente pubblico.** Un'autorità nazionale di navigazione aerea modernizza il proprio sistema di gestione del traffico aereo, un sistema di sistemi critico per la sicurezza che comprende radar, postazioni dei controllori, comunicazioni e software, in funzione giorno e notte. Il programma segue la ISO/IEC/IEEE 15288 lungo l'intero ciclo di vita. La verifica prova che ogni sottosistema rispetta la propria specifica e la convalida attraverso simulazione con controllori reali prova che il sistema integrato sostiene operazioni sicure prima che qualsiasi traffico reale ne dipenda. Una rigorosa V&V permette all'autorità di passare in esercizio per fasi, con ripiego a ogni passo, perché qui un fallimento emergente non testato è un evento di sicurezza pubblica.

## Business case: motivazioni, ROI e TCO

La motivazione è che i difetti diventano esponenzialmente più costosi quanto più tardi li trovi. Un errore di requisito colto nella fase dei requisiti costa quasi nulla da correggere. Lo stesso errore colto in esercizio può costare migliaia di volte di più e, in un sistema critico per la sicurezza, può costare vite, richiami o una missione fallita. L'ingegneria dei sistemi sposta la scoperta dei difetti nelle fasi iniziali, economiche.

Per il **ritorno sull'investimento** (ROI, il valore ottenuto rispetto al costo speso), il vantaggio è ridurre rilavorazioni, meno fallimenti di integrazione e programmi che rispettano calendario e budget anziché sforare. Gli studi di settore sui grandi programmi trovano ripetutamente che un forte sforzo di ingegneria dei sistemi è correlato a sforamenti più piccoli. Per il **costo totale di proprietà** (TCO, il costo complessivo nel corso della vita di costruire, far funzionare e ritirare un sistema), l'ingegneria dei sistemi tiene conto delle fasi di esercizio e ritiro che dominano il costo a lungo termine ma che i progetti ad hoc ignorano. Progettare fin dall'inizio per manutenibilità, interfacce e smaltimento abbassa il costo dei decenni che il sistema passa in servizio. Vedi la gestione dei progetti (capitolo 10.6).

## Antipattern e insidie

- **Grande progettazione anticipata senza iterazione.** Trattare il ciclo di vita come una cascata rigida a senso unico, così scopri che i requisiti erano sbagliati solo dopo aver costruito tutto.
- **Requisiti senza tracciabilità.** Una pila di requisiti che nessuno collega a progetto o test, così non puoi provare la copertura né giustificare alcuna parte.
- **Ignorare le interfacce.** Dare per scontato che i sottosistemi si incastrino da soli, poi perdere mesi all'integrazione per disallineamenti ai confini che nessuno possedeva.
- **Verifica senza convalida.** Provare che il sistema rispetta la propria specifica senza mai controllare che la specifica corrispondesse ai bisogni reali, poi rilasciare il sistema sbagliato.
- **Trattare il software come separato.** Team software che ottimizzano localmente ignorando vincoli hardware, tempi e operatori umani.
- **MBSE come shelfware.** Costruire un modello una volta, poi lasciarlo marcire disallineato così che diventi peggio di nessun modello.
- **Saltare la pianificazione del ritiro.** Nessun piano per dismissione, migrazione dei dati o smaltimento, così il fine vita diventa una corsa costosa e rischiosa.

## Modello di maturità

**Livello 1: Avvio.** L'ingegneria dei sistemi è ad hoc e reattiva. I requisiti vivono in documenti sparsi, le interfacce sono scoperte all'integrazione e la verifica è qualsiasi test capiti di fare. I grandi programmi sforano regolarmente e sorprendono il team tardi.

**Livello 2: Sviluppo.** Esistono pratiche di base sui programmi principali. I requisiti sono catturati e fissati come riferimento, le interfacce chiave hanno documenti di controllo ed esiste un piano di verifica. La pratica è incoerente tra i team e dipende dai singoli anziché da un metodo condiviso.

**Livello 3: Standardizzazione.** L'ingegneria dei sistemi è una disciplina documentata, di tutta l'organizzazione, allineata alla ISO/IEC/IEEE 15288 e fatta rispettare tra i team. L'intero ciclo di vita è pianificato, la tracciabilità è mantenuta da capo a capo, le interfacce sono controllate formalmente e verifica e convalida sono distinte e pianificate. L'MBSE è usata sui programmi complessi.

**Livello 4: Gestione.** L'ingegneria dei sistemi è misurata e controllata con dati. L'organizzazione segue metriche rispetto a valori di riferimento: volatilità dei requisiti e copertura della tracciabilità, difetti di interfaccia trovati all'integrazione, tassi di superamento di verifica e convalida e fuga di difetti per fase del ciclo di vita (quanti difetti sfuggono a ogni fase per essere colti più tardi a costo maggiore). Le revisioni governano i programmi su questi numeri e le soglie innescano azioni correttive anziché interventi a posteriori.

**Livello 5: Orchestrazione.** L'ingegneria dei sistemi è migliorata di continuo e integrata nell'organizzazione. Un modello MBSE vivo è l'unica fonte di verità, la tracciabilità è automatizzata, la simulazione prevede il comportamento emergente prima della costruzione e le metriche dei programmi passati alimentano il successivo. Hardware e software sono co-progettati come prassi e il processo si adatta al mutare di programmi, fornitori e rischi.

## Spunti di discussione

- Dov'è il confine tra ingegneria dei sistemi e architettura del software nella vostra organizzazione, e chi possiede lo spazio tra i due?
- Sul vostro programma più grande, potete tracciare un singolo bisogno di stakeholder fino al test che lo verifica? Se no, che cosa servirebbe?
- Quali dei vostri recenti fallimenti sono avvenuti a un'interfaccia, e chi la possedeva?
- L'MBSE rimarrebbe redditizia per voi, o diventerebbe costosa shelfware data la vostra cultura e i vostri strumenti?
- Il vostro piano del ciclo di vita affronta seriamente esercizio e ritiro, o si ferma in silenzio al lancio?

## Punti chiave

- L'ingegneria dei sistemi progetta l'intero sistema (software, hardware, persone e processi) da un capo all'altro ed è distinta dall'architettura del software.
- Pianifica l'intero ciclo di vita, dal concetto ai requisiti, al progetto, all'integrazione, alla V&V, all'esercizio e al ritiro.
- Traccia ogni bisogno a un requisito, a un elemento di progetto e a un test e alloca ogni requisito a una parte responsabile.
- Gestisci le interfacce in modo esplicito con chiara proprietà e documenti di controllo, perché i confini sono dove i sistemi si rompono.
- Verifica (costruito bene) e convalida (costruita la cosa giusta) sono controlli diversi, e servono entrambi.
- Usa MBSE e SysML per un'unica fonte di verità connessa e usa il pensiero sistemico per anticipare il comportamento emergente.
- Adegua il peso del processo a dimensione, durata e rischio del sistema.

## Riferimenti e letture di approfondimento

- INCOSE, *INCOSE Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities*
- ISO/IEC/IEEE 15288, *Systems and Software Engineering: System Life Cycle Processes*
- ISO/IEC/IEEE 29148, *Systems and Software Engineering: Requirements Engineering*
- Sanford Friedenthal, Alan Moore e Rick Steiner, *A Practical Guide to SysML: The Systems Modeling Language*
- NASA, *NASA Systems Engineering Handbook* (NASA/SP-2016-6105)
- Andrew P. Sage e William B. Rouse, *Handbook of Systems Engineering and Management*
- Dennis M. Buede e William D. Miller, *The Engineering Design of Systems: Models and Methods*
- Donella H. Meadows, *Thinking in Systems: A Primer*
- Eberhardt Rechtin e Mark W. Maier, *The Art of Systems Architecting*
- U.S. Department of Defense, *Defense Acquisition Guidebook* (guida all'ingegneria dei sistemi)
