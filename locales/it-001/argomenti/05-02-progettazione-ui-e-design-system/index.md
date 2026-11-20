# 5.2 Progettazione UI e design system

## Panoramica e motivazioni

La [progettazione dell'interfaccia utente (UI)](https://en.wikipedia.org/wiki/User_interface_design) è il mestiere di dare forma a ciò che le persone vedono e toccano: layout, [tipografia](https://en.wikipedia.org/wiki/Typography), colore, spaziatura, controlli e stati. Un [design system](https://en.wikipedia.org/wiki/Design_system) prende quel mestiere e lo trasforma in una risorsa condivisa, riutilizzabile e governata: un insieme documentato di principi, componenti, schemi e token a cui ogni team attinge, così che l'intero prodotto appaia e si comporti come uno solo. La progettazione UI decide come dovrebbe apparire una schermata. Un design system decide come diecimila schermate tra molti team restino coerenti.

Per una grande organizzazione, il design system è l'investimento singolo a più alta leva nella qualità della UI e nella velocità di consegna. Senza di esso, ogni team reinventa pulsanti, moduli, finestre modali e gestione degli errori, ciascuno leggermente diverso, ciascuno mantenuto separatamente, ciascuno rotto separatamente. Gli utenti pagano questo in confusione e sfiducia; l'azienda lo paga in sforzo duplicato e qualità disomogenea. Un design system trasforma decisioni di design una tantum in capitale riutilizzabile: risolvi una volta in un componente [accessibilità](https://en.wikipedia.org/wiki/Accessibility), [reattività](https://en.wikipedia.org/wiki/Responsive_web_design) e identità di marca e ogni team eredita il risultato.

Impresa ed ente pubblico aggiungono due pressioni specifiche. Primo, la scala: centinaia di applicazioni, molte costruite da fornitori o acquisite per fusioni, devono tutte sembrare un'unica organizzazione. Secondo, longevità e cambiamento: i marchi vengono rinnovati, le agenzie riorganizzate e una singola piattaforma può dover servire più marchi o sotto-agenzie da un'unica base di codice. Un design system ben architettato, con temi e tokenizzazione adeguati, rende affrontabili anziché catastrofici questi cambiamenti radicali.

## Principi chiave

- La coerenza abbassa il [carico cognitivo](https://en.wikipedia.org/wiki/Cognitive_load); un pulsante dovrebbe apparire e comportarsi allo stesso modo ovunque.
- Le decisioni di design sono risorse: catturale una volta come componenti e token riutilizzabili.
- I token sono la fonte di verità per le decisioni visive; i componenti consumano token, mai valori scritti nel codice.
- Accessibilità e reattività sono incorporate nei componenti, non incollate schermata per schermata.
- Un design system è un prodotto con utenti (sviluppatori e designer), non un deliverable una tantum.
- La gerarchia visiva guida l'attenzione: carattere, colore e spazio dovrebbero rendere ovvia l'importanza.
- La governance mantiene coerente un sistema; il contributo lo mantiene vivo.

## Raccomandazioni

### Struttura il sistema a strati: token, componenti, schemi

I design token sono valori nominati e indipendenti dalla piattaforma per colore, spaziatura, tipografia, raggio, elevazione e movimento: le decisioni atomiche. Costruiscili a livelli: una palette primitiva (valori grezzi), token semantici (`color-action-primary`, `space-inset-md`) che portano significato e token a livello di componente dove servono. I componenti consumano i token semantici, così che una singola modifica si propaghi ovunque. Sopra i componenti stanno gli schemi: composizioni collaudate come una tabella di dati, un modulo a più passi o uno stato vuoto. Documenta tutti e tre gli strati in un unico posto, con esempi dal vivo e indicazioni d'uso.

### Fai bene i fondamenti visivi

Imposta una scala tipografica con chiara gerarchia e generosa interlinea per la leggibilità e mantieniti a un insieme limitato di dimensioni e pesi. Definisci il colore come un sistema, con abbastanza contrasto per l'accessibilità (vedi il capitolo sull'accessibilità) e ruoli semantici, anziché tonalità grezze sparse nella UI. Usa una scala di spaziatura e una griglia di layout così che allineamento e ritmo restino coerenti senza congetture schermata per schermata. La gerarchia visiva dovrebbe rendere ovvia a colpo d'occhio l'azione primaria e l'informazione più importante.

### Progetta in modo reattivo e mobile-first

Progetta prima per il più piccolo viewport ragionevole, poi migliora per gli schermi più grandi. Questo ti costringe a dare priorità ai contenuti e ai controlli essenziali. Usa layout fluidi e unità relative così che le interfacce si adattino a qualsiasi schermo, anziché scattare tra pochi breakpoint fissi. Rendi i bersagli di tocco abbastanza grandi e assicurati che le interazioni funzionino con tocco, mouse e tastiera. Negli enti pubblici soprattutto, presumi che una quota significativa dei tuoi utenti sia su dispositivi piccoli, vecchi o economici.

### Fai del passaggio da design a sviluppo e della parità una questione di prim'ordine

Un design system ripaga solo quando la UI rilasciata corrisponde al design previsto e continua a corrispondere. Mira a un'unica fonte di verità: i token esportati dallo strumento di design alimentano direttamente il codice, così che designer e ingegneri facciano riferimento agli stessi valori. Fornisci una libreria di componenti in codice che gli ingegneri useranno davvero, con gli stessi nomi e proprietà dei componenti di design. Usa il test di regressione visiva (confronto automatico dell'interfaccia resa con immagini di riferimento approvate) e controlli di revisione del design per cogliere la deriva. E misura la "parità design-codice" come metrica di salute esplicita: la quota di UI costruita da componenti del sistema rispetto a codice una tantum.

### Supporta temi e white-label su scala aziendale

Progetta l'architettura per più marchi fin dall'inizio se c'è qualche probabilità che ti servano. Poiché i componenti consumano token semantici, un tema è solo un diverso insieme di valori dei token, così che un rinnovo del marchio o un nuovo sotto-marchio diventi una modifica di dati, non una riscrittura del codice. Supporta temi chiari e scuri, modalità ad alto contrasto e personalizzazione del marchio per tenant attraverso lo stesso meccanismo. Tieni la logica specifica del marchio fuori dai componenti e spostala in insiemi di token e configurazione.

### Governa il sistema come un prodotto

Dai al design system un team dedicato, una roadmap, il versionamento, un registro delle modifiche e un canale di supporto. Spiega come i team contribuiscono con nuovi componenti e come vengono rivisti e promossi. Bilancia il controllo centrale (per preservare coerenza e accessibilità) con un modello di contributo (così che il sistema evolva con i bisogni reali anziché diventare un collo di bottiglia). Comunica chiaramente deprecazioni e migrazioni e dai ai team consumatori abbastanza tempo di preavviso.

## Compromessi: vantaggi e svantaggi

| Decisione | Vantaggi | Svantaggi |
|---|---|---|
| Costruire un design system | Coerenza, velocità, accessibilità una volta, rinnovi del marchio più facili | Costo iniziale e continuo, richiede un team dedicato |
| Adottare un sistema pronto all'uso | Partenza rapida, schemi collaudati | Aspetto generico, più difficile adattarlo a marchio e bisogni unici |
| Governance centrale rigorosa | Coerenza, qualità, accessibilità garantite | Può strozzare i team, sembrare burocratica |
| Modello di contributo aperto | Evolve con i bisogni reali, proprietà condivisa | Rischio di deriva e incoerenza senza revisione |
| Tokenizzazione e temi pesanti | Rinnovi economici e supporto multi-marchio | Più astrazione, curva di apprendimento più ripida |

I design system scambiano costo iniziale e di governance con coerenza e velocità a lungo termine. Per un piccolo prodotto con un solo team, l'onere può non ripagare. Per una grande organizzazione con molti team e prodotti di lunga durata, la domanda non è se avere un sistema ma quanto investire e come governarlo. Il rimpianto più comune è sotto-investire in governance e strumenti di parità: il sistema esiste sulla carta, ma i team se ne allontanano in silenzio.

## Domande da discutere con il tuo team

1. **Com'è stratificata la nostra architettura dei token, e ai componenti è vietato usare valori scritti nel codice?** L'intero vantaggio di un design system (rinnovi economici, temi multi-marchio, accessibilità risolta una volta) dipende dai componenti che consumano token semantici come `color-action-primary` anziché tonalità grezze e valori in pixel sparsi nel codice. Decidi ora i livelli: una palette primitiva, token semantici che portano significato e token a livello di componente solo dove servono davvero. La sovra-astrazione è un rischio reale, quindi concorda quanti strati sono troppi e come uno sviluppatore trova in fretta il token giusto. Porta come evidenza di deriva una ricerca dei colori e delle spaziature scritti nel codice nella tua base di codice. Se la logica del marchio è cotta nei componenti, un rinnovo diventa una riscrittura del codice anziché una modifica di configurazione, che è esattamente la catastrofe che la tokenizzazione esiste per prevenire.

2. **Come misuriamo e difendiamo la parità design-codice, e quali strumenti colgono automaticamente la deriva?** Un design system che esiste solo come file di design è un foglio di adesivi: gli ingegneri ricostruiscono comunque tutto e la UI rilasciata diverge lentamente dall'intento. Concorda una metrica di parità esplicita (la quota di UI costruita da componenti del sistema rispetto a codice una tantum) e collega il test di regressione visiva alla CI così che le schermate rese siano confrontate con riferimenti approvati. Conta alla scala aziendale e governativa perché centinaia di applicazioni, molte costruite da fornitori o ereditate per fusioni, devono tutte sembrare un'unica organizzazione. Porta il numero attuale di parità e un elenco dei principali componenti su misura che i team continuano a ricostruire. Se nessuno possiede la metrica o la suite di regressione, la deriva sta già vincendo in silenzio.

3. **Come governiamo contributo, deprecazione e migrazione così che il sistema non strozzi i team né si frammenti?** Un controllo centrale rigoroso garantisce coerenza e accessibilità ma può trasformare il team del design system in un collo di bottiglia che i team aggirano; un contributo aperto mantiene vivo il sistema ma rischia varianti divergenti senza revisione. Decidi il percorso di contributo: come un team propone un nuovo componente, chi lo rivede e come viene promosso. Altrettanto, concorda come comunichi le modifiche che rompono, perché le deprecazioni senza supporto alla migrazione e tempo di preavviso fanno bloccare o forkare i team consumatori. Porta esempi di componenti che i team hanno costruito fuori dal sistema e chiediti perché non hanno contribuito indietro. La risposta di solito rivela se la tua governance è un servizio o un ostacolo.

4. **Come garantiamo che l'accessibilità sia risolta una volta dentro i componenti, e che cosa impedisce a un team di rilasciare un componente inaccessibile una tantum?** L'argomento più forte per un design system è che contrasto del colore, stati del focus, uso da tastiera e semantica per i lettori di schermo vengano risolti una volta ed ereditati ovunque, ma quella promessa crolla nel momento in cui i team scrivono a mano i propri controlli. Per una grande organizzazione è qui che sta il maggior rischio legale e reputazionale, perché un singolo modulo di pagamento o selettore di data inaccessibile può bloccare utenti reali e innescare lamentele in ogni prodotto che l'ha copiato. Pesa l'applicazione centrale (componenti accessibili più un linter o un cancello di revisione che rifiuta il markup grezzo) contro l'autonomia dei team e decidi dove sta la linea rigida. Porta i risultati di un audit di accessibilità, un elenco di componenti con il loro stato di conformità e un conteggio dei controlli su misura che i team hanno ricostruito fuori dal sistema. Nei contesti aziendali e governativi non è un vezzo: obblighi come WCAG, Section 508 ed EN 301 549 rendono la conformità un requisito di appalto e di audit, quindi una libreria di componenti con conformità documentata è essa stessa una risorsa di conformità.

5. **A quanti marchi, tenant e temi deve servire questo sistema, e abbiamo progettato ora lo strato dei token per questo anziché adattarlo dopo?** I temi sono economici se li hai progettati e brutali se no, perché un marchio o un tenant mai previsto rimanda la logica del marchio dentro i componenti e annulla l'intero scopo della tokenizzazione. Per un grande team questa decisione plasma anni di lavoro: una piattaforma che deve servire più marchi, un tema chiaro e scuro, una modalità ad alto contrasto e una personalizzazione del marchio per tenant ha bisogno di uno strato di token semantici abbastanza pulito da far sì che un tema sia solo un diverso insieme di valori. Bilancia quella flessibilità contro la sovra-astrazione, poiché un albero di token che nessuno sa navigare è esso stesso un fallimento. Porta la roadmap di marchi e tenant che puoi prevedere, il numero di temi in uso oggi ed eventuali componenti che già lasciano trapelare logica specifica del marchio. Nei contesti aziendali e governativi, fusioni, acquisizioni e riorganizzazioni di agenzie aggiungono di routine marchi che non avevi pianificato, quindi progettare per il multi-marchio fin dall'inizio è la differenza tra una modifica di dati e una riscrittura pluriennale.

6. **Come migreremo le applicazioni legacy e costruite da fornitori sul sistema, e come è finanziato il team del design system perché sopravviva al prossimo ciclo di bilancio?** Un design system dà il suo ritorno solo quando prodotti reali lo adottano, eppure le applicazioni più difficili da convertire sono quelle vecchie e in outsourcing che ne hanno più bisogno e il team che mantiene il sistema è spesso il primo tagliato quando i bilanci si stringono. Per una grande organizzazione devi decidere tra una migrazione big-bang e una incrementale e come far costruire ai fornitori sui tuoi componenti anziché attorno a essi. Porta un inventario delle applicazioni con il loro attuale punteggio di parità, una stima dello sforzo di migrazione per applicazione e le leve contrattuali che hai sui fornitori. Nei contesti aziendali e governativi, scrivi la conformità al design system nei termini di appalto così che il nuovo lavoro dei fornitori atterri sul sistema per impostazione predefinita e finanzia il team che lo mantiene come infrastruttura condivisa durevole, perché un sistema che perde i suoi custodi in una riorganizzazione deriva di nuovo in frammentazione entro un anno.

## Lente settoriale

**Startup.** Con due o tre ingegneri e nessuna liquidità da spendere, non costruire un sistema governato. Spendi un giorno o due a definire un piccolo insieme di token semantici per colore, spaziatura e carattere, più una dozzina di componenti condivisi, tutti in un unico file a cui l'intero team fa riferimento. Appoggiati a una libreria di primitive pronta all'uso per le parti difficili e non scrivere nulla nel codice così che il tuo primo vero rinnovo del marchio sia una modifica di token anziché una riscrittura.

**Piccola impresa.** Senza un designer dedicato e con un budget ridotto, compra anziché costruire: adotta una libreria di componenti o un UI kit collaudati e dai loro un tema leggero per il tuo marchio. Il tuo obiettivo è un prodotto coerente e accessibile senza dotare di personale un team di design system, quindi privilegia un sistema che includa accessibilità e reattività di serie. Resisti alla voglia di forkarlo, perché una copia personalizzata che non puoi mantenere diventa una passività nel momento in cui il progetto a monte va avanti.

**Grande impresa.** Il problema è la coerenza tra molti team e prodotti di lunga durata, quindi tratta il design system come infrastruttura condivisa governata con un team dedicato, versionamento e una roadmap. Segui la parità design-codice come una metrica vera, collega il test di regressione visiva alla CI e progetta lo strato dei token per più marchi e temi fin dall'inizio. Metti a bilancio esplicitamente il costo di governance e migrazione e gestisci l'adozione come un portafoglio anziché presumere che i team vi derivino da soli.

**Ente pubblico.** Regole sugli appalti, trasparenza e responsabilità pubblica plasmano ogni scelta. La conformità all'accessibilità a standard come WCAG, Section 508 ed EN 301 549 è un requisito di legge, non una preferenza, quindi una libreria di componenti con conformità documentata diventa una risorsa di conformità. Privilegia o estendi un design system pubblico condiviso così che i cittadini incontrino gli stessi schemi tra i servizi, scrivi l'uso del design system nei contratti dei fornitori e pubblica apertamente i tuoi componenti e le indicazioni così che agenzie e fornitori possano adottarli ed esservi tenuti.

## Esempi

**Startup.** Una startup di due ingegneri continuava a ricostruire pulsanti e campi di modulo in modo leggermente diverso a ogni nuova schermata e il prodotto cominciava a sembrare cucito insieme. Anziché un sistema pesante, hanno speso due giorni a definire un piccolo insieme di design token semantici per colore, spaziatura e carattere, più circa una dozzina di componenti condivisi, tutti in un unico file a cui l'intero team faceva riferimento. Poiché nulla era scritto nel codice, quando la loro prima assunta sensibile al design ha proposto una palette più pulita, il rinnovo è stato una modifica di token arrivata in tutta l'app in un pomeriggio anziché una fatica schermata per schermata.

**Grande impresa.** Un'azienda software globale con decine di team di prodotto ha costruito un design system tokenizzato con una libreria condivisa di componenti in codice. I token semantici le hanno permesso di rilasciare un pieno rinnovo del marchio in tutti i prodotti in settimane, anziché una fatica pluriennale per team, perché la modifica era un nuovo insieme di token anziché migliaia di modifiche di colori scritti nel codice. La parità design-codice, seguita come metrica di cruscotto, è salita man mano che i team sostituivano i componenti su misura, il che ha tagliato la manutenzione duplicata della UI.

**Ente pubblico.** Un governo nazionale ha creato un design system comune per i servizi pubblici (componenti condivisi, schemi e accessibilità incorporata) imposto tra le agenzie. Un cittadino che si sposta tra un servizio fiscale, uno sanitario e uno di licenze incontra la stessa intestazione, gli stessi controlli di modulo e gli stessi schemi di errore, il che costruisce fiducia e accorcia la curva di apprendimento. Agenzie e fornitori rilasciano più in fretta e in modo più accessibile perché i problemi difficili sono risolti centralmente e il governo può aggiornare indicazioni o correzioni di accessibilità una volta e farle propagare ovunque.

## Business case: motivazioni, ROI e TCO

Il ROI di un design system viene dal rimuovere la duplicazione e accelerare la consegna. Anziché ogni team che progetta e costruisce gli stessi componenti, compongono da una libreria condivisa, il che accelera in modo misurabile la consegna e libera designer e ingegneri per il lavoro specifico del prodotto. Accessibilità e reattività, risolte una volta nei componenti, ti risparmiano il costo di rimedio per progetto. Rinnovi e temi che prima richiedevano anni ora richiedono settimane.

Sul TCO, il costo di adozione è un team dedicato, strumenti e lo sforzo dei prodotti esistenti per migrare sul sistema. Il costo del non adottare si paga di continuo: costruzione e manutenzione duplicate tra i team, UI incoerenti e inaccessibili che creano rischio di assistenza e legale e rinnovi lenti e costosi. Poiché la duplicazione è distribuita tra i bilanci di molti team, è facile trascurarla: un design system rende visibile quel costo nascosto e lo cattura in un posto solo.

Per presentare il caso alla leadership, quantifica il lavoro duplicato sui componenti tra i team, il guadagno di time-to-market dalla composizione e il costo e la durata del tuo ultimo rinnovo rispetto a ciò che un sistema tokenizzato consentirebbe. Imposta il sistema come infrastruttura condivisa con una metrica di adozione misurabile (percentuale di parità), così che il suo valore possa essere seguito nel tempo anziché solo asserito.

## Antipattern e insidie

- **Design system come foglio di adesivi**: un file di design statico senza componenti in codice, così gli ingegneri ricostruiscono comunque tutto.
- **Valori scritti nel codice ovunque**: colori e spaziature sparsi nel codice, rendendo impossibili temi e rinnovi.
- **Nessuna governance**: il sistema si frammenta man mano che i team aggiungono varianti divergenti; la coerenza si erode.
- **Governance senza contributo**: il team centrale diventa un collo di bottiglia e i team lo aggirano.
- **Ignorare la parità**: la UI in codice deriva dall'intento di design e nessuno misura il divario.
- **Sovra-astrazione**: così tanti token e strati che nessuno sa trovare o usare quello giusto.
- **Logica del marchio cotta nei componenti**: rende il multi-marchio e i temi una riscrittura del codice anziché una modifica di configurazione.
- **Modifiche che rompono senza supporto alla migrazione**: i team consumatori si bloccano o forkano il sistema.

## Modello di maturità

**Livello 1: Avvio.** Ogni team costruisce la propria UI in modo ad hoc e reattivo. Nessun componente condiviso, aspetto e comportamento incoerenti, colori e spaziature scritti nel codice per schermata. Ogni rinnovo del marchio è una fatica manuale schermata per schermata.

**Livello 2: Sviluppo.** Esiste una guida di stile o libreria di componenti condivisa ma è parziale, facoltativa e spesso non sincronizzata tra design e codice. Alcuni team la usano, altri no e le pratiche di base variano molto da team a team.

**Livello 3: Standardizzazione.** Un design system tokenizzato con una libreria in codice mantenuta, documentazione e governance è documentato e fatto rispettare in tutta l'organizzazione. I componenti consumano token semantici, i temi sono supportati e accessibilità e reattività sono incorporate anziché incollate schermata per schermata.

**Livello 4: Gestione.** Il sistema è misurato e controllato con dati rispetto a valori di riferimento. La parità design-codice è seguita come metrica esplicita con obiettivi per prodotto, il test di regressione visiva gira nella CI per cogliere la deriva e la conformità all'accessibilità è misurata rispetto agli standard anziché presunta. I cruscotti di adozione mostrano la copertura dei componenti per team e costo e durata dei rinnovi sono registrati così che il miglioramento sia visibile nel tempo.

**Livello 5: Orchestrazione.** Il design system è un prodotto migliorato di continuo, integrato nell'organizzazione e adattivo al cambiamento. Ha versionamento, una roadmap e un modello di contributo funzionante, così che evolva con i bisogni reali. Rinnovi e nuovi temi sono modifiche di token di routine, i temi multi-marchio e multi-tenant sono normali e il team ritira, ridefinisce e promuove gli schemi sull'evidenza dei dati d'uso, alimentando strumenti di design e pipeline di consegna da un'unica fonte di verità.

## Spunti di discussione

- Come bilanciate la governance centrale contro l'autonomia dei team senza frammentare né strozzare?
- Qual è la metrica giusta per la "parità design-codice", e come la mantenete onesta?
- Quando a un team dovrebbe essere permesso costruire un componente una tantum anziché usare il sistema?
- Come finanziate e dotate di personale un design system perché sopravviva a cicli di bilancio e riorganizzazioni?
- Quanta flessibilità dei temi vale il costo aggiunto di astrazione?
- Come migrate le applicazioni legacy e costruite da fornitori su un sistema condiviso?

## Punti chiave

- Un design system trasforma decisioni di design una tantum in capitale riutilizzabile e governato.
- Strutturalo a strati (token, componenti, schemi), con i componenti che consumano token semantici.
- Incorpora accessibilità e reattività nei componenti così che ogni team le erediti.
- Tratta la parità design-codice come una metrica di salute misurabile, non un'ipotesi.
- La tokenizzazione rende rinnovi e temi multi-marchio una modifica di dati, non una riscrittura.
- Governa il sistema come un prodotto con una roadmap, il versionamento e un modello di contributo.
- Alla scala aziendale e governativa, un sistema condiviso è l'investimento UI a più alta leva disponibile.

## Riferimenti e letture di approfondimento

- Brad Frost, *Atomic Design*
- Alla Kholmatova, *Design Systems: A Practical Guide to Creating Design Languages*
- Josef Müller-Brockmann, *Grid Systems in Graphic Design*
- Robert Bringhurst, *The Elements of Typographic Style*
- Ellen Lupton, *Thinking with Type*
- Luke Wroblewski, *Mobile First*
- Ethan Marcotte, *Responsive Web Design*
- Nathan Curtis, scritti su design token e governance dei design system
- W3C Design Tokens Community Group, specifica del formato
- Design system governativi (per esempio UK Government Design System, U.S. Web Design System) come implementazioni di riferimento
