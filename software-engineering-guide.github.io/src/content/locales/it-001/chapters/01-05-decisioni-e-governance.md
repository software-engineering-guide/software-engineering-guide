# 1.5 Decisioni e governance

## Panoramica e motivazioni

Ogni sistema software è la somma di migliaia di decisioni: quale [database](https://en.wikipedia.org/wiki/Database), quale architettura, quale libreria, se costruire o comprare, quando contrarre un debito e quando ripagarlo. La governance è il modo in cui prendi queste decisioni bene e in modo coerente, coinvolgi le persone giuste senza creare colli di bottiglia e conservi il ragionamento, così che i team futuri non siano condannati a doverlo reimparare. In un piccolo team le decisioni avvengono nella conversazione e vivono nella memoria condivisa. Su larga scala, quella memoria evapora. Le persone se ne vanno, i team si riorganizzano e il "perché" di una scelta critica si perde, lasciando ai successori la scelta tra seguirla ciecamente per culto del cargo o strapparla via alla cieca. Una buona governance è l'ingranaggio che rende le decisioni visibili, deliberate e durature in un'organizzazione grande e mutevole.

La sfida centrale per i grandi team è bilanciare autonomia e allineamento. Se spingi tutte le decisioni verso un comitato centrale, ottieni coerenza, ma a costo di colli di bottiglia paralizzanti e team privati di potere. Se le spingi tutte verso il basso, ottieni velocità, ma a costo del caos: tecnologie incompatibili, sforzi duplicati ed errori ripetuti. La risposta matura non è né centralizzazione né anarchia. È un modello a strati. I team decidono localmente la maggior parte delle cose entro una "strada asfaltata" ben segnalata, mentre un processo leggero e trasparente governa le scelte davvero trasversali e difficili da invertire. L'obiettivo è rendere le buone decisioni l'impostazione predefinita facile e spendere la scarsa attenzione di governance solo dove conta davvero.

Imprese ed enti pubblici portano una posta in gioco più alta. Devono soddisfare auditor, regolatori e organi di vigilanza che pretendono decisioni documentate e difendibili. Lavorano su orizzonti temporali lunghi, dove una cattiva scelta architetturale o un cumulo non gestito di [debito tecnico](https://en.wikipedia.org/wiki/Technical_debt) può gravare su di loro per un decennio. E i loro obblighi di appalto e conformità rendono le decisioni di costruire o comprare particolarmente rilevanti e difficili da invertire. Per queste organizzazioni, un processo decisionale disciplinato e ben registrato non è burocrazia fine a se stessa. È gestione del rischio, memoria istituzionale e fondamento della responsabilità.

## Principi chiave

- Registra le decisioni e il loro ragionamento; una decisione senza motivazione è una passività.
- Spingi le decisioni al livello più basso che ha il contesto, entro chiari paletti.
- Adegua il peso del processo al peso e alla reversibilità della decisione.
- Distingui le decisioni reversibili ("porta a doppio senso") da quelle irreversibili ("porta a senso unico") e governale in modo diverso.
- Preferisci strade asfaltate e valori predefiniti alle approvazioni caso per caso.
- Tratta il debito tecnico come un portafoglio gestito, non come una colpa morale da nascondere.
- Rendi trasparente la governance; un processo decisionale nascosto genera sfiducia e rifacimenti.

## Raccomandazioni

### Adotta gli Architecture Decision Record e un processo RFC proporzionato

Un [Architecture Decision Record](https://en.wikipedia.org/wiki/Architectural_decision) (ADR, registro delle decisioni architetturali) è un breve documento immutabile che cattura una singola decisione importante: il suo contesto, le opzioni valutate, la scelta compiuta e le conseguenze. Conserva gli ADR nel controllo di versione accanto al codice, così che il ragionamento viaggi con il sistema. Per le decisioni che richiedono contributi prima di essere prese, usa un processo [RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (request for comments, richiesta di commenti) leggero: fai circolare una proposta, invita a commentare per un periodo limitato, poi decidi e registra. Mantieni leggeri entrambi. Il valore sta nel pensare e nella traccia durevole, non in modelli elaborati. Insieme, ADR e RFC trasformano il ragionamento tacito e dimenticato in una memoria istituzionale ricercabile.

### Governa con strade asfaltate, non con guardiani

Anziché esaminare ogni decisione una per una, investi in una "strada asfaltata": un insieme di valori predefiniti benedetti e ben supportati, linguaggi approvati, framework, pipeline di rilascio e schemi, che i team possono adottare con poco attrito e molto supporto. I team che restano sulla strada asfaltata hanno bisogno di poca governance, perché la scelta sicura e conforme è anche quella facile. I team con una ragione autentica per lasciarla possono farlo, ma si assumono la responsabilità aggiuntiva e una revisione leggera. Questo modello della "golden path" scala molto meglio di un comitato centrale che approva tutto, perché sposta la governance dal controllo caso per caso a valori predefiniti ben progettati.

### Usa i comitati di revisione architetturale con parsimonia e trasparenza

Un comitato di revisione architetturale, o il suo equivalente, ha un ruolo legittimo per le decisioni più grandi, più trasversali o più irreversibili, e per fissare gli standard che definiscono la strada asfaltata. Mantieni ristretto il suo ambito, pubblici i suoi criteri e rapido e consultivo il suo processo, non un collo di bottiglia obbligatorio per il lavoro di routine. Il compito del comitato è custodire la coerenza e condividere conoscenza, non approvare ogni scelta. Quando un comitato diventa una coda in cui ogni progetto deve attendere, ha fallito. Delega con decisione e riserva la revisione centrale alle poche decisioni che la meritano davvero.

### Fai di costruire, comprare o adottare un'analisi deliberata

Per ogni capacità rilevante, valuta tre strade: costruirla in casa, comprare un prodotto commerciale o adottare una soluzione [open source](https://en.wikipedia.org/wiki/Open-source_software). Costruisci quando la capacità è un vero elemento di differenziazione e centrale per la tua missione. Compra o adotta le capacità indifferenziate che altri fanno meglio. Conta il [costo totale di proprietà](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO), non solo il prezzo iniziale. Comprare comporta costi di licenza, integrazione e [dipendenza dal fornitore](https://en.wikipedia.org/wiki/Vendor_lock-in) (lock-in). Costruire comporta manutenzione e organico perpetui. Adottare l'open source comporta obblighi di supporto e di monitoraggio della sicurezza. Registra la decisione e le sue ipotesi come ADR, così da poterla rivedere quando le circostanze cambiano.

### Gestisci il debito tecnico come un portafoglio

Il debito tecnico non è intrinsecamente negativo. A volte contrarlo per rilasciare prima è la scelta giusta. Ciò che è negativo è il debito non gestito, invisibile, dimenticato. Tieni un inventario esplicito del debito rilevante. Per ogni voce, annota il costo che impone (gli "interessi" continui) e il costo per sanarla. Poi gestiscilo come un portafoglio finanziario. Ripaga il debito ad alto interesse che rallenta il team ogni giorno. Tollera il debito a basso interesse negli angoli stabili. Prendi le decisioni sul debito in modo consapevole anziché per caso. Riserva una frazione stabile della capacità al rimborso del debito, così che non si accumuli mai fino a una crisi.

### Distingui le decisioni reversibili da quelle irreversibili

Non tutte le decisioni meritano la stessa deliberazione. Le decisioni reversibili "a porta a doppio senso" si annullano facilmente, quindi prendile in fretta e a livello locale, dal team, con una propensione all'azione. Tormentarsi su di esse fa perdere tempo e rallenta l'apprendimento. Le decisioni irreversibili o costose da invertire "a porta a senso unico", un contratto di [API](https://en.wikipedia.org/wiki/API) pubblica, un modello di dati su larga scala, un impegno pluriennale con un fornitore, meritano una deliberazione lenta, attenta e senior e una motivazione registrata. Classificare le decisioni in questo modo è una delle abitudini di governance con la leva più alta che hai. Dirige la scarsa attenzione dove rende e sblocca tutto il resto.

## Compromessi: vantaggi e svantaggi

| Approccio di governance | Vantaggi | Svantaggi |
| --- | --- | --- |
| Comitato di revisione centrale per tutto | Massima coerenza e supervisione | Grave collo di bottiglia; toglie potere ai team; lento |
| Strada asfaltata con autonomia locale | Scala, veloce, valore predefinito sicuro, dà potere ai team | Richiede investimento iniziale in piattaforma; qualche deriva fuori strada |
| Piena autonomia dei team, nessuna governance | Veloce, forte responsabilità | Frammentazione, duplicazione, errori ripetuti |
| ADR / RFC | Memoria durevole, decisioni migliori, trasparenza | Onere di scrittura; ignorati se non mantenuti |

| Scelta di approvvigionamento | Vantaggi | Svantaggi |
| --- | --- | --- |
| Costruire | Pieno controllo, si adatta esattamente, può differenziare | Costo perpetuo di manutenzione e organico |
| Comprare | Veloce, supportato, la manutenzione è di altri | Costo di licenza, lock-in, adattamento imperfetto |
| Adottare (open source) | Nessun canone di licenza, ispezionabile, comunità | Onere di supporto e sicurezza a carico tuo |

Il compromesso unificante è tra controllo e velocità, e tra coerenza centrale e autonomia locale. Ogni scelta di governance si colloca su questo spettro. L'impostazione raccomandata, strade asfaltate più delega basata sulla reversibilità, compra deliberatamente gran parte della velocità dell'autonomia mantenendo la coerenza che conta. Lo fa rendendo facile la scelta allineata e riservando il processo pesante alla rara decisione irreversibile.

## Domande da discutere con il tuo team

1. **Chi decide se una data decisione è una porta a senso unico, e come individuerai gli errori di classificazione in entrambe le direzioni?** Classificare le decisioni per reversibilità è una delle abitudini di governance con la leva più alta, e il suo valore crolla se le etichette sono sbagliate: se tratti una scelta reversibile come irreversibile la affoghi nella deliberazione, se tratti una irreversibile come reversibile rilasci un modello di dati o un contratto di API pubblica che non puoi annullare a basso costo. Il rischio opposto è che chi sta più vicino al lavoro possa propendere per la velocità, mentre un comitato centrale può propendere per la cautela. Porta alla discussione esempi concreti: quanto costerebbe davvero, in tempo e denaro, invertire ciascuna decisione, e chi sostiene quel costo. Nei contesti aziendali e governativi, impegni d'appalto e dati su larga scala trasformano molte scelte in porte a senso unico che all'inizio sembravano reversibili. Concorda chi classifica e costruisci l'abitudine di un rapido secondo parere su tutto ciò che è vicino al confine, così che la scarsa attenzione cada dove l'inversione è davvero costosa.

2. **Chi possiede, finanzia e dota di personale la strada asfaltata, e che cosa le impedisce di degenerare in un guardiano?** Una strada asfaltata funziona solo se i valori predefiniti benedetti sono davvero ben supportati e più facili delle alternative, e questo richiede un investimento sostenuto che è facile sottofinanziare. Il compromesso è netto: una strada asfaltata con poche risorse diventa un insieme di obblighi senza supporto, che è esattamente il controllo da guardiano che il modello doveva sostituire, e i team allora la aggirano. Porta prove della salute della strada: tassi di adozione, quanto sono aggiornati gli strumenti approvati, quanto in fretta risponde il team di piattaforma e quanto spesso i team chiedono di uscire dalla strada. Per le organizzazioni grandi e regolamentate, la strada asfaltata è anche il modo in cui la scelta conforme diventa quella facile, quindi finanziarla è un investimento di conformità, non solo una comodità. Decidi un responsabile chiaro e un budget stabile, e misura se i team scelgono la strada perché è davvero il percorso più facile.

3. **Dove i team stanno aggirando la vostra governance, e che cosa vi dice quello shadow IT?** I team eludono il percorso autorizzato quando è più penoso della scorciatoia, quindi uno shadow IT diffuso è meno un problema di disciplina che un verdetto di progettazione sulla vostra governance. Le considerazioni in gioco sono reali: certe elusioni sono avventate, e molte sono un'elusione razionale di un comitato di revisione diventato una coda di settimane. Porta le prove: quali approvazioni vengono saltate, quali strumenti non ufficiali si sono diffusi in silenzio e quanto impiega davvero il percorso ufficiale. Nei contesti aziendali e governativi la posta è più alta, perché gli strumenti non autorizzati possono violare obblighi di audit, sicurezza e appalto che hanno peso legale. Se lo schema mostra persone che aggirano un collo di bottiglia, la soluzione è velocizzare e allargare la strada asfaltata e restringere l'ambito del comitato alle poche decisioni trasversali e irreversibili, non aggiungere altre approvazioni.

4. **Quanta della nostra capacità di consegna va davvero a ripagare il debito tecnico, e sappiamo nominare le voci a più alto interesse da affrontare per prime?** Il debito tecnico si comporta come un interesse composto, una tassa silenziosa su ogni modifica futura, e una grande organizzazione può portarlo per anni prima che qualcuno si accorga che il sistema è diventato lento e fragile da modificare. La pressione contraria è brutale: ogni ora spesa sul debito è un'ora non spesa su funzionalità che la leadership può vedere, quindi il rimborso è la prima cosa che si taglia quando una scadenza si stringe. Porta alla discussione prove reali: un inventario scritto del debito rilevante, una stima onesta del costo continuo che ogni voce impone e del costo per sanarla, e la frazione effettiva della capacità recente andata al rimborso rispetto al lavoro nuovo. Per imprese ed enti pubblici su orizzonti decennali, il debito non gestito finisce per imporre una costosa riscrittura o un rilievo di audit, quindi tratta una quota stabile di rimborso come gestione del rischio e decidi chi la difende quando i tempi slittano.

5. **Quando ci serve il ragionamento dietro una decisione presa due anni fa, riusciamo davvero a trovarlo, e qualcuno tiene viva quella traccia?** Tutto il valore di un ADR è che il ragionamento sopravviva alle persone che lo hanno formulato, e quel valore crolla se gli ADR vengono scritti una volta, mai cercati e lasciati in silenzio diventare obsoleti. La tensione è tra la disciplina di scrittura necessaria per catturare contesto, opzioni e conseguenze nel momento della decisione e la pressione quotidiana di rilasciare e andare avanti. Porta alla discussione verifiche concrete: scegli tre decisioni recenti importanti e vedi se qualcuno riesce a trovare la motivazione registrata in pochi minuti, e controlla se gli ADR superati sono marcati come tali anziché contraddire in silenzio la pratica attuale. Nei contesti aziendali e governativi quella traccia ricercabile è esattamente l'evidenza difendibile che auditor e organi di vigilanza pretendono, quindi decidi dove vivono gli ADR, chi li rivede e che cosa rende una decisione abbastanza importante da essere registrata.

6. **Quando abbiamo riaperto per l'ultima volta una grande decisione di costruire o comprare rispetto alle sue ipotesi originarie, e ci accorgeremmo mai della scadenza di quelle ipotesi?** Le scelte di approvvigionamento sono tra le decisioni più costose e difficili da invertire che prendi, e le ipotesi che le sostengono (i prezzi di un fornitore, il tuo organico, la maturità di un'opzione open source) diventano obsolete in silenzio mentre la decisione resta congelata. Le considerazioni in gioco pesano il costo irrecuperabile e il disagio del cambiare contro il costo crescente del lock-in, di un adattamento imperfetto o di un onere di manutenzione che non vuoi più. Porta l'ADR originale e le sue ipotesi dichiarate, una stima aggiornata del costo totale di proprietà per ogni strada, includendo licenze, integrazione, organico e costo di uscita, e qualsiasi segnale, una variazione di prezzo o un declassamento del supporto, che indichi che una premessa è cambiata. Per gli acquirenti pubblici e regolamentati, regole sugli appalti e contratti pluriennali rendono queste porte a senso unico particolarmente vincolanti, quindi concorda in anticipo i fattori scatenanti e la cadenza che imporranno una nuova decisione deliberata anziché un rinnovo cieco.

## Lente settoriale

**Startup.** Governa quasi nulla e punta forte sulla velocità: per le scelte reversibili a porta a doppio senso, decidi alla scrivania e vai avanti. Riserva la tua unica abitudine di governance alla manciata di porte a senso unico, un modello di dati centrale o un fornitore fondamentale, e cattura ciascuna in un solo paragrafo, così che un futuro collega non debba rimettere tutto in discussione da zero. Salta del tutto comitati di revisione e strade asfaltate, perché alla tua dimensione sono un onere che non puoi permetterti e l'intero team condivide già il contesto.

**Piccola impresa.** Senza un architetto in organico, fai di costruire o comprare la tua domanda di governance centrale e rispondi in base al costo totale di proprietà anziché alla preferenza. Scegli come predefinito comprare o adottare strumenti ben supportati per tutto ciò che non è il tuo elemento di differenziazione, perché la manutenzione perpetua è il costo che puoi permetterti meno di sostenere. Tieni un semplice registro delle decisioni, così che il ragionamento dietro le tue poche scelte rilevanti sopravviva all'uscita di una persona chiave.

**Grande impresa.** Il tuo problema è bilanciare autonomia e allineamento tra molti team, quindi investi in una strada asfaltata finanziata e riserva un comitato di revisione architetturale ristretto e rapido alle decisioni davvero trasversali e irreversibili. Standardizza gli ADR perché il ragionamento diventi memoria istituzionale ricercabile, e gestisci debito tecnico e scelte di approvvigionamento come portafogli con budget stabili. Misura se i team scelgono la strada perché è la più facile e ridimensiona qualsiasi comitato degenerato in una coda.

**Ente pubblico.** Decisioni documentate e difendibili qui non sono opzionali: auditor e organi di vigilanza si aspettano di vedere il ragionamento, le opzioni valutate e le ipotesi dietro ogni scelta rilevante. Conduci costruire o comprare come un'analisi registrata del costo totale di proprietà, rispetta le regole sugli appalti che limitano il lock-in con un unico fornitore e tieni gli ADR come traccia di evidenze pronta per l'audit. Prendi sul serio gli orizzonti temporali lunghi, perché un modello di dati o un impegno con un fornitore preso oggi può vincolare l'organizzazione per un decennio, quindi classificalo come una porta a senso unico e delibera di conseguenza.

## Esempi

**Startup.** Una startup di quattro persone prende la maggior parte delle decisioni in pochi minuti attorno a una scrivania condivisa, e per le scelte reversibili a porta a doppio senso quella velocità è un vero vantaggio, quindi resiste a qualsiasi onere di governance. Ma quando scelgono un database e un modello di dati che sarà doloroso cambiare in seguito (una porta a senso unico), si fermano a scrivere una nota di un solo paragrafo: le opzioni, la scelta e le ipotesi dietro di essa. Un anno dopo, arrivati ai limiti di scalabilità, quell'unica nota li salva dal rimettere la questione in discussione da zero. Governano quasi nulla e riservano la loro unica abitudine leggera alle poche decisioni davvero costose da invertire.

**Grande impresa.** I team di piattaforma di una grande impresa erano paralizzati da un comitato di revisione architetturale che doveva approvare ogni scelta tecnologica, creando code di settimane. L'impresa ha ristrutturato la governance attorno a una strada asfaltata: un catalogo curato di linguaggi, archivi di dati e pipeline approvati e pienamente supportati che i team potevano adottare subito. Gli ADR registravano ogni decisione di deviare, e una revisione rapida e consultiva gestiva solo le scelte fuori strada. L'ambito del comitato si è ridotto alla definizione degli standard e alla manciata di decisioni davvero trasversali. La consegna è accelerata nettamente. La coerenza è addirittura migliorata, perché il percorso facile era ora quello conforme. E l'archivio degli ADR ha dato all'organizzazione una traccia ricercabile del perché le cose fossero state costruite in quel modo.

**Ente pubblico.** Un ministero governativo ha affrontato una grande decisione di costruire o comprare per una piattaforma di gestione dei casi, con rigide regole di appalto e di audit. Anziché decidere per preferenza, ha condotto un'analisi documentata del costo totale di proprietà su tre opzioni: costruire su misura, comprare un prodotto commerciale e adottare una base open source. Ha pesato licenze, integrazione, manutenzione a lungo termine, organico e lock-in, e ha registrato la decisione e le sue ipotesi come ADR. Anni dopo, quando i termini di un fornitore sono cambiati, il ministero ha rivisto quell'ADR, ha scoperto che le ipotesi originarie non reggevano più e ha deciso di nuovo con piena conoscenza del ragionamento precedente, evitando una migrazione cieca e costosa. La motivazione registrata era anche esattamente l'evidenza difendibile che gli auditor richiedevano.

## Business case: motivazioni, ROI e TCO

Le decisioni sono il costo con la leva più alta e la visibilità più bassa nel software. Una sola scelta architetturale o di approvvigionamento sbagliata e irreversibile può imporre anni di zavorra o un rimedio da nove cifre. Governarla bene, poche ore di deliberazione e una traccia scritta, costa quasi nulla al confronto. Il ritorno degli ADR e della delega basata sulla reversibilità viene da due fonti: evitare errori costosi sulle decisioni a porta a senso unico, ed evitare deliberazioni sprecate e rifacimenti su tutto il resto. La motivazione registrata riduce anche drasticamente il costo ricorrente di rimettere in discussione questioni già risolte e dei team che ricostruiscono a ritroso l'intenzione dietro i sistemi ereditati.

Il debito tecnico rende concreto l'argomento del TCO. Il debito non gestito si comporta esattamente come un interesse composto: una tassa crescente su ogni modifica futura, finché il sistema diventa di fatto non mantenibile ed esige una costosa riscrittura. Gestire il debito come un portafoglio, con un'allocazione stabile di capacità per ripagare le voci ad alto interesse, costa molto meno della crisi che altrimenti arriverà. Una buona governance è economica da adottare, perlopiù la disciplina di mettere per iscritto le decisioni e l'investimento iniziale in una strada asfaltata. Saltarla è costoso: si paga in riscritture evitabili, sorprese di lock-in, fallimenti di audit e perdita di memoria istituzionale. Per convincere la leadership, presenta la governance nel suo linguaggio: riduzione del rischio, rifacimenti evitati, consegna più rapida grazie alla strada asfaltata e difendibilità pronta per l'audit. Mostra che l'obiettivo non è più processo ma processo meglio mirato, esame severo solo dove l'inversione è costosa e velocità senza attrito ovunque altrove.

## Antipattern e insidie

- Decisioni non documentate: il ragionamento si perde nel momento in cui le persone che lo hanno formulato se ne vanno.
- Collo di bottiglia del comitato di approvazione: un organo centrale dietro cui ogni progetto deve fare la coda.
- Processo unico per tutti: costringere decisioni banali e reversibili a una revisione pesante.
- Paralisi da analisi: tormentarsi su decisioni a porta a doppio senso facilmente reversibili.
- [Shadow IT](https://en.wikipedia.org/wiki/Shadow_IT): team che eludono del tutto la governance perché il percorso autorizzato è troppo penoso.
- Debito tecnico invisibile: debito mai inventariato, mai ripagato, che si accumula in silenzio.
- Riflessi di costruire tutto o comprare tutto: approvvigionarsi per abitudine anziché per analisi del TCO.
- Teatro della governance: documenti e comitati che esistono per apparenza ma non plasmano le decisioni.

## Modello di maturità

- Livello 1 (Avvio): le decisioni sono ad hoc e non registrate; la governance è assente o un collo di bottiglia generalizzato; il debito tecnico è invisibile e il ragionamento dietro le scelte evapora quando le persone se ne vanno.
- Livello 2 (Sviluppo): alcune decisioni vengono documentate ed esiste qualche revisione, ma la pratica è incoerente tra i team e il processo è spesso sproporzionato rispetto al peso e alla reversibilità della decisione.
- Livello 3 (Standardizzazione): ADR, strada asfaltata, delega basata sulla reversibilità e un inventario del debito sono documentati e fatti rispettare in tutta l'organizzazione, così che la scelta conforme sia l'impostazione predefinita facile e il ragionamento sia ricercabile.
- Livello 4 (Gestione): la governance è misurata rispetto a valori di riferimento: si seguono l'adozione della strada asfaltata, la copertura degli ADR, il tempo di ciclo delle decisioni, il debito come quota della capacità e i tassi di eccezione fuori strada, e le decisioni di ripagare il debito o rivedere l'approvvigionamento sono innescate da quelle prove anziché dalle crisi.
- Livello 5 (Orchestrazione): la governance è regolata di continuo e integrata con la pianificazione di consegna e rischio; l'attenzione è mirata con precisione alle decisioni irreversibili; le scelte di debito e approvvigionamento sono riequilibrate attivamente come portafogli e decise di nuovo sulla base delle prove al mutare delle circostanze.

## Spunti di discussione

- Per le nostre decisioni recenti più importanti, riusciamo a trovare il ragionamento registrato dietro di esse?
- Dove la nostra governance è un collo di bottiglia, e dove è assente quando servirebbe?
- Quali delle nostre decisioni attuali sono porte a senso unico, e le stiamo trattando come tali?
- Quanta capacità destiniamo al rimborso del debito tecnico, ed è sufficiente?
- I nostri team seguono la strada asfaltata perché è davvero il percorso più facile, o la aggirano?
- Quando abbiamo rivisto per l'ultima volta una grande decisione di costruire o comprare rispetto alle sue ipotesi originarie?

## Punti chiave

- Registra le decisioni importanti e la loro motivazione con gli ADR; rendi durevole il ragionamento.
- Governa con strade asfaltate e valori predefiniti, non con un controllo da guardiani caso per caso.
- Adegua il peso del processo al peso e alla reversibilità della decisione; delega le porte a doppio senso, delibera sulle porte a senso unico.
- Analizza costruire, comprare o adottare in base al costo totale di proprietà e registra le ipotesi.
- Gestisci il debito tecnico come un portafoglio esplicito con un'allocazione stabile di rimborso.
- Mantieni la governance trasparente e leggera; dirigi la scarsa attenzione dove l'inversione è costosa.

## Riferimenti e letture di approfondimento

- Michael Nygard, "Documenting Architecture Decisions" (lo schema originale degli ADR)
- Gregor Hohpe, "The Software Architect Elevator" e "37 Things One Architect Knows"
- Lettere agli azionisti di Amazon sulle decisioni di Tipo 1 e Tipo 2 (porta a senso unico e a doppio senso)
- Ward Cunningham, la metafora originale del "debito tecnico"
- Martin Fowler, scritti sul debito tecnico e sull'architettura evolutiva
- Neal Ford, Rebecca Parsons, Patrick Kua, "Building Evolutionary Architectures"
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate" (architettura debolmente accoppiata e autonomia)
- ISO/IEC/IEEE 42010 sulla descrizione dell'architettura
