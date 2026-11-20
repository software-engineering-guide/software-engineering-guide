# 2.11 Qualità del software

## Panoramica e motivazioni

La [qualità del software](https://en.wikipedia.org/wiki/Software_quality) è quanto bene un sistema soddisfa i bisogni dichiarati e le aspettative ragionevoli. Questo significa più che se funziona: significa se il sistema è affidabile, sicuro, manutenibile, utilizzabile, performante e adatto al proprio scopo nel tempo. La qualità è più ampia del testing. Il testing (capitolo 2.4) è un'attività che rivela i difetti. La qualità è l'intera disciplina del costruire bene la cosa giusta e del sapere, con prove, di averlo fatto. Un sistema può superare ogni test ed essere comunque di bassa qualità se non è manutenibile, accessibile o ben adatto a ciò di cui gli utenti hanno davvero bisogno.

In un grande team la qualità non può vivere nella testa di una persona o nelle abitudini di un team. Centinaia di ingegneri, più prodotti e sistemi di lunga durata hanno bisogno di una definizione condivisa di qualità, di processi espliciti per garantirla e di misure che dicano se sta migliorando o peggiorando. Senza questo, la "qualità" diventa un'aspirazione vaga che perde ogni discussione contro una scadenza, e i difetti si accumulano finché il cambiamento diventa lento e rischioso.

Nei contesti aziendali e governativi la posta sale ancora. I sistemi regolamentati, critici per la sicurezza e rivolti ai cittadini devono dimostrare la qualità, non solo asserirla: processi documentati, evidenze tracciabili e verifica indipendente sono spesso obbligatori. La scarsa qualità porta costi finanziari, legali e reputazionali diretti e, in alcuni ambiti, mette in pericolo le persone. Una disciplina deliberata della qualità, costruita su modelli, processi, misurazione e cultura, è ciò che trasforma la qualità da accidente in risultato gestito.

## Principi chiave

- La qualità è adeguatezza allo scopo più conformità ai requisiti; definisci esplicitamente entrambe.
- La qualità si costruisce dentro, non si testa dentro; la verifica trova i difetti, ma la prevenzione li evita.
- Distingui la [garanzia di qualità](https://en.wikipedia.org/wiki/Quality_assurance) (i nostri processi sono solidi?) dal [controllo di qualità](https://en.wikipedia.org/wiki/Quality_control) (questo prodotto è buono?).
- La verifica chiede "l'abbiamo costruito bene?"; la validazione chiede "abbiamo costruito la cosa giusta?"
- Misura la qualità con un piccolo insieme di metriche significative; tratta le metriche come segnali, non come obiettivi.
- Il costo di un difetto cresce quanto più tardi lo si trova, quindi sposta prima le attività di qualità.
- La qualità è una proprietà dell'intera organizzazione e della sua cultura, non un cancello alla fine.

## Raccomandazioni

### Adotta un modello di qualità condiviso come ISO/IEC 25010

Dai alla tua organizzazione un vocabolario comune per la qualità adottando un modello di qualità del prodotto riconosciuto. [ISO/IEC 25010](https://en.wikipedia.org/wiki/ISO/IEC_25010) definisce caratteristiche tra cui adeguatezza funzionale, efficienza delle prestazioni, compatibilità, usabilità, affidabilità, sicurezza, manutenibilità e portabilità. Usalo per rendere concreta la qualità: per ogni sistema, decidi quali caratteristiche contano di più e che cosa significhi "abbastanza buono" per ciascuna. Queste caratteristiche di qualità del prodotto sono gli stessi **attributi di qualità** che guidano l'architettura (capitolo 3.1). Qualità e architettura sono due viste di un'unica questione, quindi lascia che condividano un unico elenco di priorità anziché due in competizione.

### Separa la garanzia di qualità dal controllo di qualità

Tratta la garanzia di qualità (QA, quality assurance) e il controllo di qualità (QC, quality control) come attività distinte ma complementari. La QA è orientata al processo e preventiva: migliora il modo in cui il lavoro viene fatto, con standard, revisioni, definizioni di completato e formazione, così che i difetti abbiano meno probabilità di comparire in primo luogo. Il QC è orientato al prodotto e di rilevamento: ispeziona i prodotti di lavoro effettivi, come testing, [revisione del codice](https://en.wikipedia.org/wiki/Code_review) e audit, per cogliere i difetti che sono entrati. Un'organizzazione matura investe in entrambe, ma propende per la QA, perché prevenire i difetti costa meno che trovarli e correggerli.

### Conduci processi espliciti di gestione della qualità del software

Fai della qualità un processo gestito, non una speranza silenziosa. Per il lavoro significativo, scrivi un piano di qualità che dichiari le caratteristiche di qualità obiettivo, le attività di garanzia e di controllo, i criteri di accettazione e chi ne risponde. Intrecciale con le pratiche che già hai: la revisione del codice (capitolo 2.5) sia come controllo sia come modo di condividere conoscenza, la strategia di test (capitolo 2.4) come rete di sicurezza automatica e l'[analisi statica](https://en.wikipedia.org/wiki/Static_program_analysis) come ispezione continua. Rivedi regolarmente i dati di qualità e agisci sugli andamenti, anziché reagire solo agli incidenti.

### Pratica verifica e validazione come discipline distinte

La verifica conferma che i prodotti di lavoro soddisfano le loro specifiche, così che gli input giusti a ogni fase producano gli output giusti, attraverso revisioni, analisi statica e test rispetto ai requisiti. La validazione conferma che il sistema finito soddisfa davvero i bisogni degli utenti e l'uso previsto, attraverso test con gli utenti, test di accettazione, progetti pilota e feedback dal campo. Servono entrambe. Un sistema può essere corretto rispetto a una specifica difettosa (verificato ma non valido), oppure può rispondere a un bisogno reale pur contenendo difetti (valido ma non verificato). Negli ambienti regolamentati può essere richiesta una [verifica e validazione](https://en.wikipedia.org/wiki/Verification_and_validation) indipendente (IV&V) da parte di un soggetto separato dagli sviluppatori.

### Misura la qualità con metriche significative

Scegli un piccolo insieme di metriche che riflettano gli esiti di qualità e i loro fattori e osservale nel tempo. Misure utili comprendono densità dei difetti, tasso di difetti sfuggiti (difetti trovati in produzione rispetto a prima del rilascio), tempo medio di rilevamento e di riparazione, tasso di fallimento delle modifiche, segnali di salute del codice come complessità e duplicazione e segnali di validazione come problemi segnalati dagli utenti e conformità di accessibilità. Stai alla larga da metriche di vanità e manipolabili: una metrica che diventa un obiettivo smette di misurare la realtà. Affianca i numeri a segnali qualitativi da revisioni e feedback degli utenti.

### Caratterizza e gestisci i difetti in modo sistematico

Tratta i difetti come dati, non solo come incendi da spegnere. Classificali per gravità, tipo e causa radice. Seguili dalla scoperta alla risoluzione. Cerca schemi per poter prevenire la ricorrenza. Usa tecniche come l'[analisi delle cause radice](https://en.wikipedia.org/wiki/Root_cause_analysis) e la categorizzazione dei difetti per distinguere gli errori isolati dalle debolezze sistemiche. Riporta ciò che impari nella QA, con standard aggiornati, test aggiunti e revisioni migliorate, così che la stessa classe di difetti non ritorni. Un difetto corretto senza capirne la causa è un difetto che hai invitato a tornare.

### Gestisci con deliberazione il costo della qualità

Capisci l'economia della qualità attraverso le categorie classiche: costi di prevenzione (formazione, standard, buon progetto, strumenti), costi di valutazione (revisioni, test, audit) e costi di fallimento (rifacimento interno prima del rilascio, più fallimenti esterni trovati dagli utenti, che costano molto di più). Sposta il tuo investimento verso prevenzione e valutazione precoce, perché ogni euro lì evita molti euro di costo di fallimento più avanti. Rendi visibili questi costi, così che "non abbiamo tempo per la qualità" sia visto per quello che è: una scelta di spendere di più sul fallimento.

### Costruisci una cultura della qualità

Fai della qualità la responsabilità di tutti, posseduta dai team che costruiscono il software, anziché passata a un reparto QA a valle che la ispeziona alla fine. I leader dovrebbero premiare gli esiti di qualità, rendere sicuro segnalare difetti e quasi-incidenti e trattare i dati di qualità come strumento di apprendimento anziché come bastone. Un approccio ai difetti senza colpevolizzazione porta i problemi alla luce presto. Uno basato sulla colpa li nasconde finché diventano costosi.

## Compromessi: vantaggi e svantaggi

| Pratica / scelta | Vantaggi | Svantaggi |
|---|---|---|
| Modello di qualità formale (ISO 25010) | Vocabolario condiviso; priorità esplicite | Onere se applicato in modo dogmatico |
| Forte garanzia di qualità (prevenzione) | Meno difetti; costo totale più basso | Investimento iniziale; più lenta a mostrare il ritorno |
| Forte controllo di qualità (ispezione) | Coglie i difetti che sfuggono | Costoso; trova i difetti tardi |
| V&V indipendente | Alta garanzia; oggettiva | Costosa; più lenta; può sembrare conflittuale |
| Ricche metriche di qualità | Visibilità; allerta precoce | Rischio di manipolazione; onere di misurazione |
| Team QA dedicato | Concentrazione e competenza | Può scaricare la responsabilità dagli sviluppatori |
| Qualità posseduta dai team | Responsabilità; feedback rapido | Richiede disciplina e competenza ovunque |

Il compromesso centrale è tra investimento e garanzia, modellato dal tempismo. La prevenzione costa denaro ora per evitare costi di fallimento più grandi dopo. Quindi il livello di qualità economicamente giusto non è il massimo; è il punto in cui il costo marginale di più garanzia eguaglia il costo di fallimento che evita. Quel punto sta in alto per i sistemi critici per la sicurezza e più in basso per strumenti interni a bassa posta. L'altra tensione ricorrente è la responsabilità. I gruppi QA centrali costruiscono competenza ma possono lasciare che gli sviluppatori scarichino la responsabilità. La qualità posseduta dai team costruisce responsabilità ma richiede competenza e disciplina ovunque.

## Domande da discutere con il tuo team

1. **Quando la stessa classe di difetti compare due volte, conduciamo un'analisi delle cause radice, o la correggiamo semplicemente di nuovo?** Un difetto corretto senza capirne la causa è un difetto che hai invitato a tornare, e in un grande team la stessa causa radice può emergere in molti servizi prima che qualcuno colleghi i punti. Trattare i difetti come dati (classificati per gravità, tipo e causa, poi scavati alla ricerca di schemi) è ciò che separa un team che diventa via via più affidabile da uno che resta occupato a correggere di nuovo lo stesso errore. Porta alla riunione il tuo tracker dei difetti e cerca firme ricorrenti: quanti incidenti recenti condividono una causa che non hai mai affrontato in modo sistemico? La risposta dovrebbe alimentare la prevenzione, così che una causa ricorrente guidi uno standard aggiornato, un nuovo aiuto condiviso, un test aggiunto o una lista di controllo di revisione migliore, perché è così che una correzione in un punto impedisce all'intera classe di ritornare.

2. **È sicuro nel nostro team segnalare un difetto o un quasi-incidente, e che cosa accade alla persona che ne solleva uno?** La qualità è una proprietà della cultura, e un approccio senza colpevolizzazione porta i problemi alla luce presto mentre uno basato sulla colpa li nasconde finché diventano costosi, il che in un sistema regolamentato o rivolto ai cittadini può significare un fallimento pubblico o una sanzione. Questo conta di più su larga scala, dove l'ingegnere più vicino a un rischio è spesso junior e l'incentivo a tacere è forte. Porta segnali onesti: i quasi-incidenti vengono registrati e discussi, o svaniscono? I postmortem indicano cause o indicano persone? L'azione è fare dei dati di qualità uno strumento di apprendimento anziché un bastone, premiare le persone che fanno emergere i problemi e condurre postmortem senza colpevolizzazione, perché non puoi prevenire ciò che il tuo team ha paura di segnalare.

3. **La validazione può davvero fermare un rilascio, e chi detiene quell'autorità quando una scadenza incombe?** Verifica (l'abbiamo costruito bene?) e validazione (abbiamo costruito la cosa giusta?) sono discipline distinte, e la validazione ha peso solo se un controllo di accessibilità fallito, un test di accettazione fallito o una ricerca sugli utenti impietosa possono davvero bloccare il rilascio. Nei contesti aziendali e governativi questo è spesso obbligatorio, a volte attraverso una verifica e validazione indipendente da parte di un soggetto separato dagli sviluppatori, e "l'abbiamo rilasciato comunque" non è una risposta che un organo di vigilanza accetta. Porta gli ultimi rilasci: un segnale di qualità ne ha mai fermato davvero uno, o il cancello cede sempre alla data? Se la validazione non ha mai bloccato un rilascio, è decorazione, e la soluzione è scrivere in anticipo i criteri di accettazione nel piano di qualità, indicare chi possiede la decisione di procedere o meno e dare a quella decisione un'autorità reale, indipendente dalla pressione della consegna.

4. **Conosciamo davvero il nostro costo della scarsa qualità, e stiamo spostando deliberatamente la spesa dal fallimento alla prevenzione?** Il costo della scarsa qualità (COPQ, cost of poor quality) è il denaro perso in rifacimenti interni, incidenti in produzione, correzioni d'emergenza, carico di supporto, utenti persi e penali, ed è quasi sempre più grande della spesa visibile in revisioni e test. In un grande team i costi di fallimento sono sparsi tra canali di incidenti, code di supporto e rifacimenti che nessuno registra come tali, così restano invisibili finché qualcuno li somma. La tensione è che la prevenzione costa denaro ora, in un ciclo di bilancio, per evitare costi di fallimento che arrivano dopo e ricadono sul bilancio di qualcun altro, il che rende lo scambio facile da rinviare per sempre. Porta cifre reali: numero e costo degli incidenti, ore di rifacimento, tasso di difetti sfuggiti e l'attuale ripartizione della spesa tra prevenzione, valutazione e fallimento, poi decidi se la composizione debba spostarsi prima. Per i sistemi aziendali e governativi, dove la maggior parte del costo nel corso della vita cade dopo il primo rilascio, porta il COPQ davanti a chi detiene il bilancio, perché un numero che un organo di vigilanza può vedere è molto più difficile da scambiare di un vago appello alla "qualità".

5. **Quali delle nostre metriche di qualità sono diventate in silenzio obiettivi, e quale comportamento stanno guidando ora?** Una metrica che diventa un obiettivo smette di misurare la realtà: insegui una percentuale di copertura e ottieni test scritti per spostare il numero, non test che colgono i difetti. Su larga scala questo è pericoloso, perché un cruscotto di punta condiviso tra decine di team detta gli incentivi di tutti, e una metrica manipolabile diffonde ovunque la manipolazione insieme. La considerazione contraria è che hai comunque bisogno di misurazione, quindi la risposta raramente è "abbandona la metrica" ma "abbinala a un controsegnale e leggila accanto alle prove qualitative di revisioni e utenti". Porta il tuo attuale insieme di metriche e, per ciascuna, chiediti che cosa potrebbe fare qualcuno sotto pressione per spostarla senza migliorare la qualità e se l'hai già visto accadere. Nei contesti regolamentati e rivolti ai cittadini, diffida in particolare delle metriche di conformità che appaiono verdi mentre la validazione sottostante (accessibilità, esiti reali per gli utenti) non è mai stata davvero esercitata, poiché un auditor finirà per mettere alla prova la realtà dietro il numero.

6. **Chi possiede la qualità qui: i team che scrivono il codice o un gruppo separato alla fine, e quale stiamo davvero finanziando?** La responsabilità plasma tutto ciò che viene a valle, perché un compartimento QA a valle lascia che gli sviluppatori scarichino la responsabilità del codice che scrivono, mentre la qualità posseduta dai team costruisce responsabilità a costo di richiedere competenza e disciplina in ogni team. In un grande team non è un aut aut: lo schema sostenibile è di solito team che possiedono la qualità attraverso revisione del codice e test automatici, sostenuti da un piccolo gruppo centrale che mantiene gli standard, conduce la garanzia di qualità come miglioramento di processo e fa coaching, anziché ispezionare la qualità alla fine. Porta una mappa onesta di dove si svolge oggi il lavoro di qualità, chi ne risponde quando un difetto sfugge e dove stanno davvero bilancio e organico rispetto a dove la retorica dice che vive la qualità. Per le organizzazioni aziendali e governative, aggiungi il requisito di verifica e validazione indipendente: alcuni regimi di garanzia impongono un soggetto separato, quindi decidi con deliberazione quali controlli appartengono ai team di consegna e quali devono restare indipendenti per soddisfare l'audit.

## Lente settoriale

**Startup.** La velocità conta più della cerimonia, quindi indica le due o tre caratteristiche di qualità che proteggono davvero il tuo prodotto, di solito affidabilità e manutenibilità, e lascia che la rifinitura attenda. Possiedi la qualità con tutto il team attraverso revisione del codice e una modesta suite di test automatici anziché montare un gruppo QA separato che non puoi mantenere. Quando la stessa classe di bug compare due volte, spendi venti minuti sulla causa radice e aggiungi un aiuto condiviso più un test, così che la prevenzione resti economica e il tuo tasso di fallimento delle modifiche resti basso mentre ti muovi in fretta.

**Piccola impresa.** Senza uno specialista della qualità dedicato e con un budget ridotto, appoggiati alla qualità incorporata negli strumenti e nelle piattaforme che acquisti anziché a un processo che devi gestire. Quando scegli un software, tratta le evidenze di qualità del fornitore come parte dell'acquisto: postura di sicurezza, accessibilità, reattività del supporto e quanto spesso i loro rilasci si rompono. Segui una manciata di segnali economici e onesti (incidenti in produzione, problemi segnalati dai clienti, tempo di correzione) anziché un elaborato programma di metriche che nessuno saprebbe mantenere.

**Grande impresa.** Il lavoro è la coerenza tra molti team: adotta un modello di qualità condiviso come ISO/IEC 25010, separa la garanzia di qualità (processo) dal controllo di qualità (prodotto) e conduci revisioni del costo della qualità che spostino la spesa verso la prevenzione. Mantieni la qualità posseduta dai team di consegna, sostenuti da un piccolo gruppo centrale che mantiene standard e cruscotti per tasso di difetti sfuggiti, tasso di fallimento delle modifiche e andamenti della salute del codice. Standardizza vocabolario e cancelli così che i gruppi smettano di reinventare la pratica di qualità, lasciando ai team lo spazio di soddisfare quelle soglie a modo proprio.

**Ente pubblico.** Appalti, trasparenza e responsabilità pubblica fissano il quadro, quindi scrivi requisiti di qualità nei contratti e richiedi evidenze di qualità documentate e tracciabili anziché asserzioni. Aspettati una verifica e validazione indipendente da parte di un soggetto separato dagli sviluppatori, una conformità di accessibilità obbligatoria e registri dei difetti con gravità e causa radice tenuti come parte della traccia di audit. Riferisci agli organi di vigilanza le cifre del costo della scarsa qualità (rifacimenti, ricorsi, fallimenti del servizio) e dai alla validazione l'autorità reale di bloccare un rilascio che deluderebbe i cittadini che ne dipendono.

## Esempi

**Startup.** Una startup di cinque persone decide che per il suo prodotto iniziale, affidabilità e manutenibilità sono le caratteristiche di qualità che contano, e lascia che la rifinitura al pixel attenda. La qualità è posseduta dall'intero team: revisione del codice e una modesta suite di test automatici sono i controlli, e non c'è un gruppo QA separato a cui passare i difetti. Quando la stessa classe di bug compare due volte, spendono venti minuti in una rapida occhiata alla causa radice e aggiungono un aiuto condiviso più un test, così che smetta di ripresentarsi anziché essere ricorretta a mano ogni volta. Quella piccola abitudine di prevenzione mantiene basso il loro tasso di fallimento delle modifiche mentre si muovono ancora in fretta.

**Grande impresa.** Una grande società di servizi finanziari adotta ISO/IEC 25010 come vocabolario di qualità e, per ogni prodotto, registra livelli obiettivo di affidabilità, sicurezza e manutenibilità. I team possiedono la qualità: revisione del codice e test automatici sono controlli nella pipeline, mentre un piccolo gruppo centrale conduce la QA mantenendo gli standard e facendo coaching. Un cruscotto di qualità segue tasso di difetti sfuggiti, tasso di fallimento delle modifiche e andamenti della salute del codice. I difetti sono classificati e analizzati per cause radice, e le cause ricorrenti guidano aggiornamenti di librerie condivise e liste di controllo. La leadership rivede trimestralmente i dati del costo della qualità e ha spostato la spesa verso la prevenzione, riducendo sia gli incidenti in produzione sia il costo di correggerli.

**Ente pubblico.** Un'agenzia nazionale che eroga una piattaforma di prestazioni rivolta ai cittadini opera sotto un regime di garanzia che richiede evidenze di qualità documentate. Conduce un processo formale di gestione della qualità con un piano di qualità per rilascio, più una verifica e validazione indipendente da parte di un team separato dagli sviluppatori. La verifica controlla ogni prodotto di lavoro rispetto a requisiti tracciati fino alla policy. La validazione comprende test di conformità di accessibilità e ricerca sugli utenti con cittadini reali, e ciascuna può bloccare un rilascio. I difetti sono seguiti con gravità e causa radice come parte della traccia di audit, e le cifre del costo della scarsa qualità (rifacimenti, ricorsi e fallimenti del servizio) vanno agli organi di vigilanza per giustificare il continuo investimento nella prevenzione.

## Business case: motivazioni, ROI e TCO

Il ritorno della qualità è un costo totale di proprietà più basso e una velocità di consegna costante. Il costo della qualità ha due lati. La spesa buona, prevenzione e valutazione, è visibile e controllabile: progetto, standard, revisioni, test e strumenti. Il costo della scarsa qualità (COPQ) è più grande ma spesso nascosto: rifacimenti interni, incidenti in produzione, correzioni d'emergenza, assistenza ai clienti, utenti persi, sanzioni normative e danno reputazionale. Gli studi che risalgono a "Quality Is Free" di Crosby trovano in modo costante che il costo totale della scarsa qualità supera di gran lunga il costo di prevenirla, e che i difetti diventano molto più costosi quanto più tardi li si coglie: un problema trovato in fase di progetto costa una frazione dello stesso problema trovato in produzione.

Per la leadership, l'argomento non è "spendi di più per la qualità". È "spendi prima per spendere meno in tutto". Quantifica il COPQ dai tuoi dati (numero e costo degli incidenti, ore di rifacimento, tasso di difetti sfuggiti) e mostra come prevenzione e valutazione precoce lo abbassano. Collega la qualità agli esiti di business: l'affidabilità trattiene i clienti, la manutenibilità mantiene economico il cambiamento futuro e sicurezza e accessibilità ti tengono fuori dai guai legali. Nei sistemi aziendali e governativi di lunga durata, dove la maggior parte del costo cade dopo il primo rilascio, le dimensioni di manutenibilità e affidabilità della qualità dominano il costo nel corso della vita. Questo fa dell'investimento precoce nella qualità una delle decisioni con la leva più alta che si possano prendere.

## Antipattern e insidie

- **La qualità come cancello finale:** ispezionare la qualità alla fine anziché costruirla dentro, così che i difetti si trovano quando sono più costosi.
- **Confondere testing e qualità:** presumere che test superati significhino alta qualità, ignorando manutenibilità, usabilità e adeguatezza allo scopo.
- **La QA come compartimento separato:** un team a valle che "possiede la qualità", lasciando che gli sviluppatori scarichino la responsabilità del codice che scrivono.
- **Teatro delle metriche:** inseguire percentuali di copertura o conteggi di difetti come obiettivi, il che invita alla manipolazione e nasconde la qualità reale.
- **Verifica senza validazione:** costruire correttamente la specifica senza mai controllare che la specifica soddisfi bisogni reali.
- **Nessuna analisi delle cause radice:** correggere i difetti uno per uno senza affrontare la causa sistemica, così che la stessa classe ricorra.
- **Ignorare il costo della scarsa qualità:** trattare la qualità come puro costo perché i costi di fallimento sono nascosti e non misurati.

## Modello di maturità

**Livello 1 (Avvio).** La qualità è indefinita e ad hoc. Si regge sulla diligenza individuale, viene controllata soprattutto con test manuali alla fine e i difetti sono gestiti in modo reattivo man mano che emergono. Non c'è modello condiviso, né metriche, né linea tra garanzia e controllo.

**Livello 2 (Sviluppo).** Compaiono pratiche di base: revisione del codice, test automatici e un tracker dei difetti. Alcuni dati di qualità vengono raccolti, ma in modo disomogeneo, e ogni team lo fa a modo suo. La qualità è ancora vista soprattutto come testing, la prevenzione è minima, la verifica avviene e la validazione è informale.

**Livello 3 (Standardizzazione).** L'organizzazione adotta un modello di qualità condiviso (come ISO/IEC 25010), separa QA da QC ed esegue processi di gestione della qualità con piani di qualità e criteri di accettazione, documentati e applicati in modo coerente tra i team. Verifica e validazione sono distinte e deliberate, e i difetti sono classificati e analizzati per cause radice secondo uno schema concordato.

**Livello 4 (Gestione).** La qualità è misurata e controllata rispetto a valori di riferimento. Un piccolo insieme di metriche significative è seguito nel tempo (densità dei difetti, tasso di difetti sfuggiti, tempo medio di rilevamento e riparazione, tasso di fallimento delle modifiche e segnali di salute del codice come complessità e duplicazione) e il costo della qualità è quantificato tra prevenzione, valutazione e fallimento. Cancelli di accettazione e qualità sono fatti rispettare sulla base delle prove anziché delle opinioni, gli andamenti sono rivisti con una cadenza fissa e la validazione può davvero bloccare un rilascio.

**Livello 5 (Orchestrazione).** La qualità è una disciplina migliorata di continuo e posseduta culturalmente, integrata con la pianificazione di business e di rischio. L'enfasi è sulla prevenzione, i dati del costo della qualità guidano dove va l'investimento e i risultati delle cause radice prevengono sistematicamente la ricorrenza. I team possiedono la qualità da un capo all'altro, le metriche alimentano il miglioramento continuo e l'organizzazione adatta la propria pratica di qualità al mutare di prodotti, rischi e normative. Questo si allinea ai livelli più alti dei modelli di maturità del capitolo 10.8.

## Spunti di discussione

- Quali caratteristiche di qualità di ISO/IEC 25010 contano di più per i vostri sistemi, e che cosa è "abbastanza buono" per ciascuna?
- Dove si colloca la vostra organizzazione nella composizione della spesa tra prevenzione, valutazione e fallimento, e dovrebbe spostarsi?
- Distinguete verifica da validazione nella pratica, o le riducete entrambe a "testing"?
- La qualità è posseduta dai team che costruiscono il software, o delegata a un gruppo separato, e che cosa cambierebbe se la spostaste?
- Qual è il vostro vero costo della scarsa qualità, e potreste misurarlo abbastanza bene da sostenere il caso di business?
- Quali delle vostre metriche di qualità sono segnali genuini, e quali sono diventate obiettivi manipolabili?

## Punti chiave

- La qualità è più ampia del testing: è adeguatezza allo scopo più conformità, attraverso caratteristiche come affidabilità, sicurezza e manutenibilità.
- Usa un modello di qualità condiviso (ISO/IEC 25010) così che gli attributi di qualità siano espliciti e allineati all'architettura (capitolo 3.1).
- Separa la garanzia di qualità (prevenire, processo) dal controllo di qualità (rilevare, prodotto) e propendi per la prevenzione.
- Pratica verifica (costruito bene) e validazione (costruita la cosa giusta) come discipline distinte.
- Misura la qualità con poche metriche significative e caratterizza i difetti per gravità e causa radice per prevenirne la ricorrenza.
- Gestisci il costo della qualità: prevenzione e valutazione precoce costano molto meno del fallimento, soprattutto nei sistemi di lunga durata.
- Costruisci una cultura della qualità senza colpevolizzazione in cui i team possiedono la qualità, sostenuti da revisione del codice (capitolo 2.5) e strategia di test (capitolo 2.4).

## Riferimenti e letture di approfondimento

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, area di conoscenza Software Quality.
- ISO/IEC 25010, *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): System and software quality models*.
- Serie ISO/IEC 25000 (SQuaRE), *Software product quality requirements and evaluation*.
- Philip B. Crosby, *Quality Is Free: The Art of Making Quality Certain*.
- W. Edwards Deming, *Out of the Crisis*.
- Capers Jones e Olivier Bonsignour, *The Economics of Software Quality*.
- Gerald Weinberg, *Quality Software Management*.
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (contesto dei processi di garanzia della qualità e V&V).
