# 1.6 Registri delle decisioni

## Panoramica e motivazioni

Un **registro delle decisioni** (decision record) è un documento che cattura una decisione importante insieme al suo contesto e alle sue conseguenze. La forma più nota è il **[registro delle decisioni architetturali](https://en.wikipedia.org/wiki/Architectural_decision) (ADR, architecture decision record)**, una breve nota, immutabile per preferenza, che registra una scelta architetturalmente significativa, perché è stata fatta e che cosa ne consegue. L'insieme completo dei registri di un progetto è il suo **registro storico delle decisioni (ADL, decision log)**, e la disciplina di tenerli fa parte della **gestione della conoscenza architetturale (AKM, architecture knowledge management)**. Questo capitolo si basa sulle pratiche di decisione e governance del capitolo 1.5, concentrandosi su come scrivere, conservare e mantenere i registri delle decisioni su larga scala.

La motivazione è semplice, e dolorosa da imparare a proprie spese. In qualsiasi sistema di lunga durata, la domanda più costosa è "perché diavolo è stato costruito così?", posta mesi o anni dopo da persone che non erano nella stanza. Il codice mostra *che cosa* fa il sistema. I test mostrano che *funziona*. Ma nessuno dei due cattura *perché* hai scelto questa strada rispetto alle alternative che hai considerato e scartato. Senza registri delle decisioni, quel ragionamento evapora con il ricambio del personale. I team rimettono in discussione questioni già risolte, ribaltano buone decisioni per cattive ragioni o conservano cattive decisioni per timore. Un registro delle decisioni è una lettera economica al futuro che conserva il ragionamento.

Per i grandi team è uno strumento di coordinamento tanto quanto un aiuto alla memoria. Le imprese hanno decine di team che prendono scelte sovrapposte. Un registro condiviso delle decisioni trasforma il ragionamento faticosamente conquistato da un team in una risorsa riutilizzabile e previene decisioni divergenti e incompatibili. Nel settore pubblico e negli ambienti regolamentati, i registri delle decisioni sono quasi obbligatori. Auditor, organi di vigilanza e collaboratori esterni subentranti hanno tutti bisogno di una motivazione tracciabile che colleghi i requisiti architetturalmente significativi alle scelte fatte per soddisfarli. Un registro delle decisioni ben tenuto è spesso la differenza tra un sistema che si può garantire e sottoporre ad audit e uno che non si può.

## Principi chiave

- **Registra il *perché*, non solo il *che cosa*.** Contesto e alternative scartate sono il punto centrale.
- **Una decisione per registro.** Mantieni ogni registro specifico e autosufficiente.
- **Piccolo e leggero batte completo e inutilizzato.** Un registro di una pagina che esiste batte un rapporto che non viene mai scritto.
- **Data ogni cosa.** Costi, vincoli e fornitori cambiano; metti la data a ogni affermazione.
- **Preferisci un registro vivo, in modo pragmatico.** L'immutabilità è l'ideale; nella pratica, correggi con note datate.
- **Parole al posto delle abbreviazioni.** "Decisioni" invita a contribuire più di "ADR".
- **Rendi le decisioni reperibili e, dove possibile, verificabili.** Porta in superficie il registro giusto al momento giusto; garantiscilo con fitness function.

## Raccomandazioni

### Cattura la struttura essenziale

Un buon registro delle decisioni ha poche sezioni essenziali. Adatta un modello noto anziché inventarne uno:

- **Titolo:** una breve frase imperativa al presente ("Usare [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) per il libro mastro").
- **Stato:** proposta, accettata, superata, deprecata.
- **Contesto:** la situazione, le forze in campo, le priorità di business e i vincoli che rendono necessaria questa decisione; includi il requisito architetturalmente significativo a cui risponde.
- **Decisione:** la scelta compiuta, enunciata in modo chiaro.
- **Conseguenze:** che cosa diventa più facile e che cosa più difficile, le decisioni successive innescate e i rischi accettati.

Tra i modelli più diffusi ci sono quello di Michael Nygard (semplice e ampiamente adottato), quello di Tyree e Akerman (più elaborato, con alternative ponderate), MADR (Markdown Any Decision Records, forte su opzioni e relativi pro e contro) e le Y-statement (una forma strutturata di una sola frase). Standardizzati su uno solo per organizzazione, così che i registri siano confrontabili. Vedi il capitolo 12.3 per un modello da copiare e incollare.

### Scrivi registri specifici, datati e quasi immutabili

Mantieni ogni registro su esattamente una decisione. Data le singole affermazioni, soprattutto tutto ciò che deriva nel tempo: prezzi, numeri di scalabilità, capacità dei fornitori, termini di licenza. In teoria un registro dovrebbe essere immutabile. Quando una decisione cambia, scrivi un *nuovo* registro che sostituisce il vecchio, conservando la storia. Nella pratica, molti team trovano che funzioni meglio un approccio da **documento vivo**: inserire nuove informazioni nel registro esistente con una data e una nota che indichi che sono arrivate dopo la decisione. Entrambi sono legittimi. Lo stile immutabile è più forte per le tracce di audit; lo stile vivo è migliore per la conoscenza quotidiana del team. Scegli con deliberazione e sii coerente.

### Conserva i registri dove si lavora

Metti i registri delle decisioni nel [controllo di versione](https://en.wikipedia.org/wiki/Version_control) accanto al codice: una cartella `decisions/` (o `adr/`) di file [Markdown](https://en.wikipedia.org/wiki/Markdown), uno per decisione, con un nome formato da una locuzione verbale imperativa, in minuscolo e separata da trattini (`choose-database.md`, `format-timestamps.md`). Questo ti dà gratis storia, revisione e confronto delle differenze, e tiene la motivazione accanto a ciò che spiega. Se il tuo team preferisce le [wiki](https://en.wikipedia.org/wiki/Wiki), Google Docs o un tracker in stile Jira, usa quelli. Lo strumento conta molto meno dell'abitudine. Un leggero strumento da riga di comando (come `adr-tools`) può creare lo scheletro dei registri e indicizzarli.

### Chiamali "decisioni" e allarga oltre l'architettura

Una constatazione pratica emersa da molti team: l'etichetta conta. Alcuni sviluppatori e manager si irritano alla parola "architettura", e "registro" può sembrare scartoffie compilate a posteriori. Rinominare la cartella semplicemente "decisions" spesso fa scattare un interruttore. I team iniziano a registrare scelte di fornitori, decisioni di pianificazione, di calendario, di dati e di conformità, tutte con lo stesso modello. Le persone imparano più in fretta dalle parole che dalle abbreviazioni, e contribuiscono di più quando l'impostazione è "aiuta i tuoi futuri colleghi a ragionare" anziché "compila il modulo obbligatorio".

### Definisci il ciclo di vita e la governance

Perché i registri delle decisioni scalino, concorda il processo circostante (è qui che la governance del capitolo 1.5 incontra la pratica):

- **Chi può avviarne uno e che cosa lo giustifica:** tipicamente qualsiasi contributore informato; avvia un registro quando gli sviluppatori futuri avranno bisogno del *perché*, e saltalo per scelte a basso rischio, autosufficienti o già documentate.
- **Ciclo di vita:** un flusso semplice come *Avvio → Ricerca → Valutazione → Attuazione → Manutenzione → Dismissione*, con criteri di accettazione per passare da una fase all'altra (problema articolato, alternative considerate, compromessi documentati, stakeholder consultati).
- **Ruoli:** proponente, ricercatore, revisore, approvatore e un responsabile della manutenzione che rivede il registro periodicamente (almeno una volta l'anno) e guida l'eventuale dismissione.
- **Governance:** come funzionano consenso, conflitto, escalation e veto, e gli eventuali vincoli di conformità. Appoggiati a principi come la *propensione all'azione* e il *[disagree and commit](https://en.wikipedia.org/wiki/Disagree_and_commit)* (dissentire e impegnarsi), e riserva il processo più pesante alle decisioni irreversibili e ad ampio raggio d'impatto ("porta a senso unico").

### Rendi le decisioni verificabili e reperibili

Un registro delle decisioni *documenta* una decisione; una **fitness function** la *garantisce*: un controllo automatico, eseguito nell'[integrazione continua](https://en.wikipedia.org/wiki/Continuous_integration) (CI), che verifica che la decisione sia ancora valida ("ogni cambiamento di stato deve emettere eventi", "nessun modulo può importare oltre questi confini", con strumenti come ArchUnit). Questo trasforma la governance da revisione manuale periodica in applicazione continua e scalabile, particolarmente preziosa per gli obiettivi normativi e di audit (capitoli 3.1, 4.6, 8.5). Poi porta in superficie il registro *giusto* al momento *giusto*. Strumenti che allegano le decisioni pertinenti a una pull request, quando uno sviluppatore tocca il codice che governano, battono la speranza che le persone leggano una cartella di documentazione.

## Compromessi: vantaggi e svantaggi

| Scelta | Vantaggi | Svantaggi |
|---|---|---|
| **ADR leggeri (Nygard/MADR)** | Rapidi da scrivere, vengono davvero scritti; poca cerimonia | Meno rigore per decisioni ad alta posta e controverse |
| **Modelli pesanti (Tyree-Akerman)** | Alternative ponderate; forti per scelte grandi e costose | Più lenti; possono scoraggiare la registrazione di routine |
| **Immutabile + sostituzione** | Traccia di audit pulita; storia conservata | Più registri; i lettori devono seguire le catene |
| **Documento vivo (correzioni datate)** | Unica fonte di verità aggiornata; facile da mantenere | Traccia di audit più debole; rischio di modifiche silenziose |
| **Markdown nel repository** | Versionato, rivedibile, accanto al codice | Meno amichevole per chi non è sviluppatore |
| **Wiki / strumento documentale** | Accessibile a tutti i ruoli | Storia e revisione più deboli; si allontana dal codice |

La tensione di fondo è tra **rigore e adozione**. Il sistema più rigoroso che nessuno usa non registra nulla. Il sistema più leggero che tutti usano aumenta di valore nel tempo. Adotta come predefinito il leggero e riserva il processo più pesante alle poche decisioni costose e difficili da invertire.

## Domande da discutere con il tuo team

1. **Come arriverà il registro giusto a uno sviluppatore nel momento in cui tocca il codice che governa, anziché restare in una cartella che nessuno apre?** Un registro in sola scrittura registra ragionamenti che non cambiano mai i comportamenti, ed è il modo più comune in cui i registri delle decisioni falliscono: esistono, e nessuno li legge quando conta. La considerazione contraria è lo sforzo, perché portare in superficie i registri in modo automatico (allegandoli a una pull request quando qualcuno modifica il codice governato) richiede un investimento in strumenti che una wiki o una cartella di documenti non richiede. Porta alla discussione prove: quando qualcuno ha di recente ribaltato o rimesso in discussione una questione risolta, il registro pertinente era reperibile in quel momento, o sepolto? Per una grande organizzazione con decine di team, la reperibilità è ciò che trasforma il ragionamento faticosamente conquistato da un team in una risorsa riutilizzabile anziché in un archivio privato. Decidi se conservare i registri nel controllo di versione accanto al codice e collegarli al flusso delle pull request, così che il registro compaia dove si svolge il lavoro.

2. **Chi è il responsabile della manutenzione di ciascun registro, e che cosa impedisce al vostro archivio di degenerare in disinformazione sicura di sé?** La modalità di fallimento pericolosa di un registro storico delle decisioni non è una cartella vuota, è una cartella piena di registri i cui costi, capacità dei fornitori e vincoli sono diventati obsoleti in silenzio anni fa. Ogni registro ha bisogno di un responsabile che lo rivede con una cadenza (almeno annuale) e guida la sostituzione o la dismissione, altrimenti l'archivio marcisce in folklore che le persone citano a proprio comodo e di cui si fidano poco. Porta prove: quanti dei tuoi registri sono privi di data, quanti descrivono un fornitore o un prezzo nel frattempo cambiato e quando ciascuno è stato rivisto per l'ultima volta. Nei contesti pubblici e regolamentati la questione è più acuta, perché una catena immutabile di registri superati è esattamente ciò su cui auditor e collaboratori esterni subentranti contano per una motivazione tracciabile. Decidi esplicitamente il tuo ciclo di vita, data le singole affermazioni che derivano nel tempo e assegna i responsabili, così che l'archivio resti una risorsa viva anziché un cimitero.

3. **Dovete standardizzare su un unico modello per tutti i team, e quanto rigore richiedono davvero le vostre decisioni ad alta posta?** La confrontabilità è un vero beneficio: quando ogni team usa la stessa forma (Nygard, MADR o simili), un nuovo team può trovare tre registri precedenti e adottarne il ragionamento in un pomeriggio anziché in un mese di dibattito. La tensione di fondo è tra rigore e adozione, perché il modello più pesante che nessuno usa non registra nulla, mentre il più leggero che tutti usano aumenta di valore nel tempo. Porta prove: i registri vengono effettivamente scritti e, separatamente, qualche decisione grande, controversa e costosa è stata analizzata poco perché la forma leggera saltava la ponderazione delle alternative? Per le imprese che coordinano scelte sovrapposte tra i team, un modello condiviso più un indice ricercabile previene decisioni divergenti e incompatibili. Adotta come predefinito il leggero per il caso comune e concorda in anticipo quali decisioni a porta a senso unico meritano una forma più pesante con alternative ponderate.

4. **Che cosa giustifica davvero l'avvio di un registro delle decisioni, e chi ha l'autorità di dire che una scelta non ne ha bisogno?** Se poni l'asticella troppo in alto, il ragionamento dietro le scelte importanti evapora; se la poni troppo in basso, l'archivio si riempie di banalità che seppelliscono i registri di cui le persone hanno davvero bisogno. Per una grande organizzazione, una soglia poco chiara significa che ogni team improvvisa la propria, quindi la copertura diventa disomogenea e nessuno può fidarsi che un registro mancante segnali una decisione poco importante. Porta alla discussione prove: una manciata di decisioni recenti che sono state registrate senza averne bisogno e alcune dolorose che non sono state registrate e che poi ti sono costate una riscoperta. Concorda un test semplice, come registrare ogni volta che uno sviluppatore futuro avrà bisogno del *perché* e saltare le scelte a basso rischio, autosufficienti o già documentate. Nei contesti regolamentati e pubblici il calcolo cambia, perché un mandato di audit può richiedere un registro per ogni requisito architetturalmente significativo indipendentemente dal fatto che il team lo ritenga utile, quindi indica fin dall'inizio quali decisioni non sono negoziabili.

5. **I vostri registri sono ragionamento genuino catturato nel momento della decisione, o scartoffie scritte dopo per soddisfare un mandato?** Un registro prodotto a posteriori per chiudere un ticket tende a ripulire l'opzione scelta e a omettere in silenzio le alternative effettivamente ponderate, che è precisamente l'informazione di cui un futuro lettore ha più bisogno. La pressione contraria è reale: scrivere il *perché* prima o durante una decisione sembra più lento del rilasciare, e ammettere per iscritto le strade scartate richiede una sicurezza psicologica che certi team non hanno. Porta al tavolo un campione di registri recenti e chiediti onestamente se contesto e alternative scartate si leggano come vera deliberazione o come giustificazione ricostruita. Per un grande team, i registri vuoti sono peggio di nessun registro, perché insegnano alle persone che l'archivio non è affidabile. Negli audit aziendali e governativi questa distinzione è netta: organi di vigilanza e collaboratori esterni subentranti dipendono da una motivazione che rifletta ciò che è stato davvero considerato, e un registro che si legge come teatro mina la garanzia che l'archivio esiste per fornire.

6. **Quali delle vostre decisioni ad alta posta potete garantire con una fitness function automatica, anziché confidare che una revisione manuale periodica individui una violazione?** Un registro delle decisioni documenta una scelta, ma solo un controllo automatico eseguito nell'integrazione continua impedisce che quella scelta si eroda in silenzio mentre decine di sviluppatori toccano il codice nel corso degli anni. Il compromesso è l'investimento, perché scrivere e mantenere fitness function (con strumenti come ArchUnit) costa tempo di ingegneria, e molte decisioni, soprattutto scelte di processo o di fornitore, non sono affatto verificabili in modo meccanico. Porta prove: quali decisioni di confine (dipendenze tra moduli, emissione di eventi, regole di accesso ai dati) sono state violate in silenzio e individuate solo tardi in revisione o in produzione. Per un'impresa con molti team, le fitness function trasformano la governance da collo di bottiglia centrale in applicazione continua che scala senza rallentare tutti. Nei contesti regolamentati e pubblici, un controllo automatico sempre attivo è un'evidenza di audit molto più forte di una firma su una revisione, perché prova che la decisione regge ancora oggi, non che qualcuno l'abbia approvata una volta.

## Lente settoriale

**Startup.** Limitati all'abitudine e a nient'altro: una cartella `decisions/` nel repository principale e una nota di due sezioni (contesto e scelta) ogni volta che prendi una decisione che il tuo io futuro metterà in discussione. Salta del tutto ciclo di vita, ruoli e approvatori, perché un processo che non riesci a sostenere è un processo che abbandonerai. Il singolo registro che risparmia al tuo primo assunto di chiedere perché il sistema è costruito così ripaga già l'intera pratica.

**Piccola impresa.** Senza un architetto dedicato e con poco tempo, metti i registri dove il tuo team già lavora, che sia una wiki, un documento condiviso o il repository, anziché comprare uno strumento dedicato. L'abitudine conta molto più degli strumenti, quindi abbassa la barriera: chiama la cartella `decisions` anziché `adr` e cattura le scelte sui fornitori e su costruire o comprare nello stesso respiro di quelle tecniche. Quando ti appoggi a collaboratori esterni, un breve registro datato del perché hai scelto un fornitore o una piattaforma è un'assicurazione economica contro il restare vincolati a una scelta che nessuno saprà più spiegare.

**Grande impresa.** Il lavoro è il coordinamento tra molti team: standardizza su un unico modello, pubblica un indice ricercabile tra i team e sostieni le decisioni chiave sui confini con fitness function, così che le violazioni facciano fallire la build anziché attendere la revisione. Assegna a ogni registro un responsabile con una cadenza di revisione, così che l'archivio resti una risorsa viva anziché degenerare in folklore. Se fatto bene, il ragionamento di un team su una scelta difficile diventa una risorsa che il team successivo adotta in un pomeriggio anziché rimettere in discussione.

**Ente pubblico.** Regole sugli appalti, trasparenza e responsabilità pubblica rendono i registri delle decisioni quasi obbligatori. Richiedi un registro immutabile e superato per ogni requisito architetturalmente significativo, ciascuno con il collegamento tra la scelta e il mandato o il controllo di conformità che soddisfa, così che gli organi di vigilanza trovino una motivazione tracciabile anziché una ricostruzione. Poiché i sistemi pubblici attraversano cicli di vita pluriennali e con più fornitori, un archivio ben tenuto è spesso ciò che permette a un collaboratore esterno subentrante di capire perché il sistema abbia la forma che ha e di continuare il lavoro senza rimettere in discussione terreno già risolto.

## Esempi

**Startup.** Una startup di cinque persone aggiunge una semplice cartella `decisions/` al repository principale, con una nota di due sezioni (contesto e scelta) ogni volta che qualcuno prende una decisione che il proprio io futuro metterà in discussione. Nessun ciclo di vita, nessun ruolo, nessun approvatore: solo l'abitudine di scrivere il *perché* accanto al codice. Quando, sei mesi dopo, arriva la prima assunta, legge l'intera cartella in un'ora e smette di chiedersi "perché è costruito così?". L'archivio leggero costa minuti per voce e risparmia la tassa di riscoperta che morde molto prima che un team diventi grande.

**Grande impresa.** Un rivenditore con 30 team di ingegneria standardizza su registri in formato MADR in ogni repository, più un indice centrale ricercabile. Quando un nuovo team si trova davanti a "[monorepo](https://en.wikipedia.org/wiki/Monorepo) contro multirepo", trova tre registri precedenti con contesto e conseguenze e ne adotta il ragionamento in un pomeriggio anziché in un mese di dibattito. Le decisioni chiave sui confini (responsabilità dei servizi, regole di accesso ai dati) sono sostenute da fitness function ArchUnit, così che le violazioni facciano fallire la build anziché essere colte in revisione. È una governance che scala senza un collo di bottiglia centrale.

**Ente pubblico.** Un'agenzia che modernizza un sistema di prestazioni richiede un ADR per ogni requisito architetturalmente significativo, ciascuno con il collegamento tra la decisione e il mandato o il controllo di conformità che soddisfa (accessibilità, residenza dei dati, verificabilità). I registri sono immutabili e superati, e producono un archivio tracciabile che soddisfa la revisione di vigilanza. Soprattutto, permette anche a un collaboratore esterno subentrante di capire *perché* il sistema abbia la forma che ha, preservando la continuità lungo i cicli di vita pluriennali e con più fornitori tipici dei programmi pubblici (capitoli 4.6, 10.4).

## Business case: motivazioni, ROI e TCO

Un registro delle decisioni costa minuti da scrivere e qualcuno in più da rivedere. Il ritorno è il costo evitato di *nuova decisione* e il costo evitato di *inversione sbagliata*, entrambi grandi e ricorrenti nei sistemi di lunga durata. Ogni volta che un team rimette in discussione una questione risolta, o ribalta una scelta valida perché nessuno ricordava il vincolo che stava dietro, paga in tempo di ingegneri senior e spesso in un incidente. Un registro storico delle decisioni converte quella tassa ricorrente in una scrittura una tantum.

Sul **costo totale di proprietà**, i registri delle decisioni sono tra la documentazione con la leva più alta che si possa tenere, perché prendono di mira la risorsa più sensibile al ricambio: la motivazione. L'inserimento è più rapido (i nuovi assunti leggono il *perché*, non solo il codice). La modernizzazione è più sicura (capitolo 3.6: si distinguono le decisioni essenziali da quelle accidentali). Gli audit sono più economici (le evidenze esistono già). Il costo di *non* tenerli è invisibile su qualsiasi cruscotto e si accumula in silenzio a ogni partenza. Per sostenere il caso con la leadership, indica una recente riscoperta costosa, o una decisione ribaltata che ha causato un incidente, e nota che il rimedio costa quasi nulla da istituire.

## Antipattern e insidie

- **Registrare il *che cosa* senza il *perché*:** omettere contesto e alternative scartate, il punto centrale.
- **Scartoffie a posteriori:** registri scritti per soddisfare un mandato, non per ragionare; si leggono come vuoti e nessuno si fida.
- **Mega-documenti con più decisioni:** un'unica pagina gigante che nessuno riesce a navigare né a sostituire con pulizia.
- **Affermazioni senza data:** costi e vincoli che erano veri una volta, presentati come senza tempo.
- **Modifiche silenziose:** cambiare la storia di una decisione senza una nota datata, distruggendo la traccia di audit.
- **Archivi in sola scrittura:** registri creati e mai portati in superficie nel momento in cui sono pertinenti, quindi non influenzano i comportamenti.
- **Guardiania delle abbreviazioni:** insistere su "ADR" e "architettura" scoraggiando così i contributi.
- **Nessun ciclo di vita:** registri mai rivisti, sostituiti o dismessi, che degenerano in disinformazione.

## Modello di maturità

- **Livello 1 (Avvio):** le decisioni vivono nelle teste delle persone, nelle conversazioni in chat e nei messaggi di commit; la cattura è reattiva e ad hoc e la motivazione si perde regolarmente con il ricambio del personale.
- **Livello 2 (Sviluppo):** alcuni team tengono registri, in formati e modelli vari, ogni volta che qualcuno se ne ricorda; la pratica è incoerente tra i team, senza archivio, nomi o processo condivisi.
- **Livello 3 (Standardizzazione):** un unico modello, la conservazione nel repository e un ciclo di vita e una governance definiti (criteri di avvio e di esclusione, ruoli, cadenza di revisione) sono documentati e applicati in modo coerente in tutta l'organizzazione; i registri sono rivisti e sostituiti anziché modificati in silenzio.
- **Livello 4 (Gestione):** l'archivio delle decisioni è misurato rispetto a valori di riferimento: copertura (la quota di decisioni architetturalmente significative che hanno un registro), freschezza (la quota di registri rivisti entro la propria cadenza, più il numero di affermazioni senza data o obsolete) e reperibilità (quanto spesso un registro pertinente è arrivato davvero allo sviluppatore che ha modificato il codice governato). I responsabili della manutenzione agiscono su queste metriche, sostituendo i registri obsoleti e colmando i vuoti di copertura sulla base delle prove anziché degli aneddoti.
- **Livello 5 (Orchestrazione):** un archivio ricercabile delle decisioni tra i team è integrato nel lavoro quotidiano: i registri pertinenti emergono automaticamente sulle modifiche che governano, le decisioni chiave sono garantite da fitness function nell'integrazione continua e l'archivio alimenta inserimento, modernizzazione e audit come risorsa viva. L'organizzazione migliora di continuo la pratica stessa, ritirando, sostituendo e ridefinendo l'ambito dei registri al mutare del sistema e dei suoi vincoli, e riequilibrando dove investe rigore man mano che cresce il portafoglio di decisioni.

## Spunti di discussione

1. Qual è l'ultima decisione che il tuo team ha ribaltato o rimesso in discussione perché nessuno ricordava il ragionamento originale?
2. Rinominare la cartella `adr/` in `decisions/` cambierebbe chi contribuisce e che cosa viene registrato?
3. Quali delle tue decisioni critiche potrebbero essere garantite oggi da una fitness function automatica?
4. Immutabile con sostituzione o documento vivo: quale si adatta ai tuoi obblighi di audit e alla tua cultura, e perché?
5. Come scoprirebbe oggi un nuovo assunto (o un collaboratore esterno subentrante) *perché* il vostro sistema ha la forma che ha?
6. Che cosa giustifica l'avvio di un registro delle decisioni nel tuo team, e che cosa giustifica il *non* avviarlo?

## Punti chiave

- Un registro delle decisioni cattura una decisione importante con il suo **contesto e le sue conseguenze**: il *perché*, non solo il *che cosa*.
- Mantieni i registri **specifici, datati e leggeri**; standardizzati su un unico modello (Nygard, MADR o simili).
- Conservali **nel controllo di versione accanto al codice**; valuta di chiamarli "decisioni" per allargare i contributi.
- Definisci un **ciclo di vita e una governance** (criteri di avvio e di esclusione, ruoli, cadenza di revisione); riserva il processo pesante alle decisioni a porta a senso unico.
- Rendi le decisioni **reperibili** nel momento della modifica e, dove possibile, **verificabili** tramite fitness function.
- Il ROI è il costo evitato di riscoperta e di inversione sbagliata; il caso del TCO è più forte dove ricambio, modernizzazione e audit contano di più. Vedi il capitolo 1.5 (decisioni e governance) e il capitolo 3.1 (fondamenti dell'architettura).

## Riferimenti e letture di approfondimento

- Michael Nygard, "Documenting Architecture Decisions" (2011): il fondamentale ADR leggero.
- MADR: progetto Markdown Any Decision Records (adr.github.io/madr).
- Jeff Tyree e Art Akerman, "Architecture Decisions: Demystifying Architecture" (*IEEE Software*, 2005).
- Olaf Zimmermann, "Y-Statements" e "Architectural Decision Making" (ozimmer.ch).
- Joel Parker Henderson, *Architecture Decision Record (ADR)*: modelli, esempi e indicazioni per il lavoro di squadra (github.com/joelparkerhenderson/architecture-decision-record).
- ThoughtWorks Technology Radar: "Lightweight Architecture Decision Records".
- Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage, *Building Evolutionary Architectures* (fitness function).
- AWS Prescriptive Guidance, "ADR process"; Red Hat, "Why you should use ADRs".
- Wikipedia, "Architectural decision" e "Architecturally significant requirements".
