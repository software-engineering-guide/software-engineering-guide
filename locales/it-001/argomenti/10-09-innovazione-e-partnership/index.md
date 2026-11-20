# 10.9 Innovazione e partnership

## Panoramica e motivazioni

Una partnership di innovazione è una collaborazione deliberata tra la tua organizzazione e una parte esterna (una startup, un fornitore, un'università, un laboratorio di ricerca, un [consorzio](https://en.wikipedia.org/wiki/Consortium) o un ente pubblico) per sviluppare una capacità che nessuno dei due costruirebbe con la stessa efficacia da solo. Va da accordi leggeri (pilot, ricerca congiunta, collaborazione open source) ad accordi profondi (co-sviluppo, [joint venture](https://en.wikipedia.org/wiki/Joint_venture), [venture capital aziendale](https://en.wikipedia.org/wiki/Corporate_venture_capital) e le formali procedure di appalto di "partenariato per l'innovazione" ora scritte nel diritto pubblico). Il filo comune è condividere rischio, conoscenza e ricompensa per arrivare a un'innovazione più in fretta o a meno di quanto lo sforzo interno o un acquisto a scaffale permetterebbe. Questo capitolo sta nella parte sulla gestione perché decidere quando e come fare partnership per l'innovazione è una decisione di portafoglio e di appalto (capitoli 10.1, 10.3) tanto quanto tecnica.

Ecco la motivazione. Nessuna grande organizzazione può costruire tutto, quindi la domanda "costruire o comprare" (capitolo 6.1) ha una cruciale terza opzione: *fare partnership*. Quando una capacità è troppo nuova per essere comprata a scaffale, troppo lontana dal nucleo per essere costruita bene internamente o troppo rischiosa per essere finanziata da soli, una partnership può trasformare una scommessa incerta in una condivisa e a fasi. Le partnership importano anche talento, tecnologia e pensiero fresco che le organizzazioni consolidate faticano a far crescere da sole, il classico antidoto al problema di innovazione dell'incumbent. Fatte bene, estendono portata e velocità. Fatte male, producono "purgatorio dei pilot" (pilot che riescono ma non raggiungono mai la produzione), [proprietà intellettuale](https://en.wikipedia.org/wiki/Intellectual_property) (PI) che trapela e dipendenza da un partner i cui incentivi divergono dai tuoi.

Per impresa e governo la posta e i meccanismi sono distintivi. Le imprese usano bracci di venture aziendale, acceleratori e accordi di co-sviluppo per restare vicine alla tecnologia emergente. I governi hanno costruito strumenti formali allo stesso scopo. La procedura di appalto di *partenariato per l'innovazione* dell'Unione europea permette a un acquirente pubblico di sviluppare e poi acquistare una soluzione non ancora esistente. Il programma statunitense [Small Business Innovation Research](https://en.wikipedia.org/wiki/Small_Business_Innovation_Research) (SBIR) e i meccanismi di sfida e premio finanziano l'innovazione esterna per le missioni pubbliche. I programmi "GovTech" abbinano enti e startup. Esistono proprio perché gli appalti normali (capitolo 10.3) comprano ciò che già esiste, mentre le missioni pubbliche hanno sempre più bisogno di ciò che non esiste ancora.

## Principi chiave

- **Fai partnership quando non puoi né comprare né costruire bene da solo.** È la terza opzione, scelta deliberatamente.
- **Allinea prima gli incentivi.** Una partnership funziona solo se entrambi i lati vincono dallo stesso esito.
- **Distribuisci il rischio a fasi.** Finanzia in incrementi legati a tappe convalidate, non con un grande impegno.
- **Risolvi in anticipo PI, dati e uscita.** Le conversazioni più dure costano meno prima di firmare.
- **Proteggi il nucleo; apri i margini.** Condividi abbastanza per collaborare, non abbastanza per svuotarti.
- **Porta deliberatamente i pilot in produzione.** Un pilot che non può scalare è una dimostrazione, non una partnership.
- **Gestisci la relazione, non solo il contratto.** Fiducia e governance la portano, non le carte.

## Raccomandazioni

### Scegli il modello di partnership adatto all'obiettivo

Obiettivi diversi richiedono strutture diverse; scegli la più leggera che lo raggiunge:

- **Pilot e [prove di concetto](https://en.wikipedia.org/wiki/Proof_of_concept):** test economici e a tempo della tecnologia di una startup o di un fornitore contro un problema reale.
- **Accordi di co-sviluppo / sviluppo congiunto:** costruzione condivisa di una specifica capacità, con contributi definiti e ripartizione della PI.
- **Partnership di ricerca:** con università o laboratori, per capacità ancora pre-prodotto.
- **Venture capital aziendale (CVC) e acceleratori:** partecipazioni al capitale o programmi a coorte per restare vicini a tecnologia e talenti emergenti.
- **Consorzi e collaborazione open source:** investimento condiviso in infrastruttura non distintiva (capitolo 10.3).
- **Strumenti pubblici di innovazione:** partenariati per l'innovazione dell'UE, SBIR/STTR, sfide e premi e programmi GovTech per missioni in cui la soluzione deve essere creata.

### Allinea gli incentivi e governa la relazione

La causa più comune di fallimento delle partnership sono incentivi disallineati travestiti da contratto allineato. Prima di fissare una struttura, chiedi che cosa ogni parte vuole davvero (ricavi, accesso al mercato, un cliente di riferimento, risultati di ricerca, impatto di missione) e conferma che lo *stesso* esito fa vincere entrambi i lati. Poi governa attivamente la relazione: una roadmap condivisa, revisioni congiunte regolari, chiari diritti decisionali e responsabili nominati su ciascun lato (si applicano gli ADR, cioè i registri delle decisioni architetturali, e le discipline di governance dei capitoli 1.5–1.6). Le partnership vivono o muoiono su fiducia e comunicazione molto più che sulle clausole del contratto.

### Risolvi PI, dati, sicurezza e uscita prima di firmare

Le conversazioni che più vorresti rimandare sono esattamente quelle da fare per prime: chi possiede la proprietà intellettuale, chi può usare i dati, come gli obblighi di sicurezza e conformità passano al partner e come ciascun lato esce. Una proprietà della PI irrisolta avvelena un co-sviluppo altrimenti riuscito. Una condivisione di dati non gestita crea esposizione di privacy e sicurezza (capitoli 4.5, 4.3). Nessun piano di uscita crea lock-in. Tratta un partner come parte della tua supply chain ai fini di rischio e garanzia (capitolo 10.2), compresa la revisione di sicurezza di terze parti.

### Finanzia a fasi e batti il purgatorio dei pilot

Finanzia le partnership di innovazione come i buoni investitori finanziano le startup: a fasi, ogni tranche rilasciata contro tappe convalidate (la disciplina di scoperta del capitolo 11.1). Questo limita il tuo svantaggio sulle molte scommesse che non andranno a buon fine preservando il vantaggio sulle poche che lo faranno. La trappola specifica dell'impresa è il *purgatorio dei pilot*: un cimitero di pilot riusciti che non raggiungono mai la produzione perché nessuno possiede il percorso verso la scala, il budget o il lavoro di integrazione. Progetta il percorso di produzione fin dall'inizio. Nomina il responsabile interno che renderà operativo un pilot riuscito e tratta "questo può scalare nel nostro patrimonio?" come una domanda di filtro, non un ripensamento.

### Proteggi il nucleo mentre apri i margini

Fai partnership più liberamente sulla capacità non distintiva e sulla ricerca precompetitiva e proteggi le tue vere fonti di vantaggio. Condividi abbastanza contesto, dati e accesso perché il partner riesca. Ma struttura la relazione in modo da non trasferire il tuo valore centrale né diventare dipendente da una singola parte esterna per qualcosa di critico per la missione (rischio di concentrazione, capitolo 10.2). L'obiettivo è importare innovazione ai margini senza svuotare il centro.

## Compromessi: vantaggi e svantaggi

| Approccio | Vantaggi | Svantaggi |
|---|---|---|
| **Partnership (co-sviluppo)** | Rischio condiviso; talento/tecnologia importati; più rapido del costruire | Complessità di PI/incentivi; costo di coordinamento; dipendenza |
| **Costruire internamente** | Pieno controllo e PI; adattamento profondo | Lento; può mancare di talento/novità; costo opportunità |
| **Comprare a scaffale** | Rapido, provato, supportato | Compra solo ciò che esiste; commoditizzato, nessun vantaggio |
| **Capitale / CVC** | Vicino alla tecnologia emergente; potenziale di crescita | Distrazione; orizzonti disallineati; onere di governance |
| **Procedure pubbliche di innovazione (partenariato UE, SBIR)** | Sviluppare legalmente ciò che non esiste ancora; adattamento alla missione | Complessità procedurale; cicli lunghi; onere amministrativo |

La tensione che definisce è **apertura contro protezione**. Le partnership di innovazione richiedono di condividere conoscenza, dati e accesso, eppure la stessa apertura può far trapelare il vantaggio o creare dipendenza. La soluzione è un ambito deliberato, essere generosi ai margini non distintivi e disciplinati sul nucleo, più un impegno a fasi, così che fiducia e valore siano provati prima che l'esposizione si approfondisca.

## Domande da discutere con il tuo team

1. **Finanziamo le partnership di innovazione come un portafoglio a fasi con un tasso di fallimento deliberatamente alto, o scommettiamo in grande su ciascuna?** Le buone partnership si comportano come scommesse di venture: la maggior parte fallisce, poche ripagano tutto e il modo di sopravvivere a quella matematica è finanziare a tranche rilasciate contro tappe convalidate. Un singolo grande impegno iniziale toglie la vostra opzione di andarvene a basso costo, che è il principale vantaggio del fare partnership rispetto al costruire. Per un'impresa o un ente che gestisce più partnership insieme, fissate un budget esplicito che si aspetti che la maggior parte dei pilot finisca e pochi scalino. Portate la spesa per le partnership dell'anno scorso, quante scommesse avete finanziato e quante hanno raggiunto la produzione. Se ogni partnership è stata un impegno big-bang senza fasi, state portando uno svantaggio che avreste potuto limitare.

2. **Prima di firmare, abbiamo confermato che entrambi i lati vincono dallo stesso esito, e chi governa la relazione dopo?** La causa più comune di fallimento delle partnership sono incentivi disallineati travestiti da contratto allineato. Chiedete che cosa ogni parte vuole davvero (ricavi, un cliente di riferimento, risultati di ricerca, impatto di missione) e confermate che lo stesso risultato fa riuscire entrambi i lati. Poi decidete chi governa la relazione dopo la firma: responsabili nominati su ciascun lato, una roadmap condivisa e revisioni congiunte regolari, perché le partnership vivono di fiducia e comunicazione molto più che di clausole. Registrate i diritti decisionali come fareste con una decisione architetturale. Venite con l'incentivo effettivo di ciascuna parte scritto in modo semplice e se non puntano allo stesso esito, correggete la struttura prima di impegnarvi.

3. **Trattiamo i partner come parte della nostra supply chain per sicurezza e rischio di concentrazione?** Un partner con accesso ai vostri dati e sistemi è una terza parte e le sue debolezze diventano le vostre. Eseguite la stessa revisione di sicurezza e due diligence che applicate a qualsiasi fornitore e risolvete diritti sui dati, obblighi di sicurezza e uscita prima che il lavoro cominci, perché sono le conversazioni più economiche prima di firmare e le più velenose dopo. Attenzione al rischio di concentrazione: una capacità critica per la missione vincolata a un singolo partner esterno è una dipendenza, non una partnership. Portate una mappa di a che cosa ogni partner può accedere e che cosa si romperebbe se fallisse o se ne andasse. Se un singolo partner detiene qualcosa che non potreste sostituire, progettate ora l'uscita.

4. **Per ogni pilot che finanziamo, chi possiede il percorso verso la produzione, e quale integrazione e budget richiede davvero scalare?** Il purgatorio dei pilot è il fallimento tipico dell'innovazione nelle grandi organizzazioni: pilot che riescono tecnicamente, impressionano uno sponsor e poi muoiono perché nessuno possedeva il lavoro poco scintillante di scalarli nel patrimonio. La spinta contraria è reale, poiché nominare un responsabile della produzione e riservare in anticipo il budget di integrazione sembra prematuro quando la maggior parte dei pilot fallirà comunque, eppure senza di esso anche i vincitori si bloccano. Portate il conteggio dei pilot eseguiti l'anno scorso, quanti hanno raggiunto la produzione e per i sopravvissuti il costo di integrazione e il responsabile interno per nome. Per un'impresa, l'ostacolo è di solito l'integrazione nel patrimonio e l'adattamento alla piattaforma; per un ente, è l'appalto successivo e la voce di bilancio che devono esistere prima che il pilot finisca, o il prototipo riuscito non ha dove atterrare.

5. **Che cosa siamo esattamente disposti a condividere, e dov'è la linea che protegge il nostro vantaggio centrale?** Le partnership funzionano solo se condividete abbastanza contesto, dati e accesso perché il partner riesca e la stessa apertura può far trapelare proprio la capacità che vi differenzia. La tensione è genuina: un ambito troppo stretto e il partner non può consegnare, uno troppo largo e consegnate il vostro vantaggio o create una dipendenza che non potete sciogliere. Portate un inventario esplicito di che cosa è non distintivo e sicuro da aprire, che cosa è nucleo e resta protetto e quali insiemi di dati portano limiti di privacy o contrattuali alla condivisione. In un'impresa questa linea dovrebbe corrispondere alla vostra strategia di rischio di concentrazione e PI; nel governo, aggiungete gli obblighi di trasparenza e di equa concorrenza che possono richiedere di condividere più apertamente con tutti gli offerenti pur proteggendo i dati dei cittadini ed evitando il lock-in sul fornitore.

6. **Abbiamo abbinato ogni partnership al modello più leggero che raggiunge l'obiettivo, compresi gli strumenti pubblici di innovazione a nostra disposizione?** La struttura porta costo e rischio reali e i team spesso ricorrono per default a un veicolo pesante (capitale, una joint venture, un accordo di co-sviluppo pluriennale) quando un pilot a tempo o un accordo di ricerca risponderebbe alla domanda a minor costo. Pesate onere di coordinamento, onere di governance e difficoltà di uscita di ogni modello rispetto a quanta certezza vi serve davvero prima di impegnarvi. Portate l'obiettivo enunciato in modo semplice (ricavi, capacità, accesso ai talenti, esito di missione), la struttura più breve che potrebbe metterlo alla prova e il costo di uscita della struttura che state proponendo. Per un ente pubblico, è anche una questione legale: strumenti come la procedura di partenariato per l'innovazione dell'UE, i premi SBIR/STTR e i premi per sfide esistono proprio per permettervi di sviluppare e poi comprare ciò che non esiste ancora e scegliere quello giusto mantiene l'appalto lecito, competitivo e verificabile.

## Lente settoriale

**Startup.** Fai partnership per prendere in prestito ciò che non puoi permetterti di costruire: hardware, scienza di dominio, distribuzione o un cliente di riferimento. Tieni ogni accordo a tempo e economico da lasciare e la tua risorsa più scarsa è l'attenzione ingegneristica e un impegno di co-sviluppo che non puoi dotare di personale affonderà l'azienda più in fretta della capacità mancante. Risolvi PI e proprietà dei clienti per iscritto prima del primo sprint, poiché regalare il tuo nucleo in una partnership iniziale è un errore che non puoi ricomprare.

**Piccola impresa.** Senza un braccio di venture aziendale né un team di innovazione, tratta il fare partnership come una scorciatoia tra comprare e costruire anziché una strategia: trova un fornitore, un laboratorio o un'università locale disposto a eseguire un piccolo pilot a pagamento su un problema concreto. Attenzione al rischio di concentrazione, perché un singolo partner che detiene una capacità da cui dipendi è una minaccia più grande per una piccola impresa che per una grande. Preferisci partner che ti lasciano possedere i tuoi dati e in grado di andartene senza riscrivere le tue operazioni.

**Grande impresa.** Il compito è la governance di portafoglio tra molti team: un manuale condiviso di partnership che copra scelta del modello, finanziamento a fasi legato a tappe, termini di PI, dati e uscita, revisione di sicurezza di terze parti e un responsabile della produzione nominato per ogni pilot. Standardizza l'interfaccia e lo strato di integrazione così che un pilot riuscito abbia dove atterrare e gestisci le partnership come un libro di opzioni a fasi con un tasso di fallimento deliberatamente alto anziché una dispersione di annunci. Metti a bilancio esplicitamente il lavoro di scalatura, perché il purgatorio dei pilot è dove il denaro dell'innovazione aziendale sparisce in silenzio.

**Ente pubblico.** Regole di appalto, trasparenza e responsabilità pubblica plasmano ogni partnership. Usa gli strumenti formali costruiti per questo (la procedura di partenariato per l'innovazione dell'UE, SBIR/STTR, sfide e premi) così da poter finanziare lecitamente fornitori che sviluppino ciò che non esiste ancora, poi acquistare il migliore su larga scala. Mantieni equa la concorrenza e verificabile il processo, insisti su termini di PI e dati che prevengano il lock-in su un singolo fornitore e pubblica abbastanza dell'accordo da soddisfare l'esame pubblico proteggendo i dati dei cittadini.

## Esempi

**Startup.** Una startup di dati climatici di quattro persone manca dell'hardware dei sensori e della scienza di dominio per convalidare da sola i propri modelli, quindi fa partnership con un laboratorio universitario per un pilot di ricerca congiunta a tempo. Risolvono prima i termini: il laboratorio pubblica la scienza, la startup tiene il proprio software e le relazioni con i clienti e ogni fase di finanziamento dipende dal raggiungere una tappa condivisa e concordata. Poiché la startup nomina un fondatore come responsabile di trasformare qualsiasi risultato promettente in una funzionalità rilasciabile, il pilot produce un vero incremento di prodotto anziché un articolo che prende polvere.

**Grande impresa.** Un'azienda di logistica vuole una capacità di ottimizzazione dei percorsi che nessun fornitore vende e che il suo team non può costruire in fretta. Conduce una partnership di co-sviluppo a fasi con una startup di IA: un pilot a pagamento su dati veri (anonimizzati), finanziamento legato a tappe, una chiara ripartizione della PI (la startup tiene il proprio modello centrale; l'azienda possiede l'integrazione e i propri dati) e un responsabile interno nominato incaricato di scalare un pilot riuscito in produzione. Poiché il percorso di produzione è progettato fin dall'inizio, il pilot sfugge al purgatorio dei pilot e viene rilasciato. La struttura a fasi limita la perdita sui pilot precedenti che non sono andati a buon fine.

**Ente pubblico.** Un ente dei trasporti ha bisogno di un sistema di previsione della congestione che non esiste ancora. Anziché comprare la cosa sbagliata o tentare di costruirlo internamente, usa una procedura di partenariato per l'innovazione in stile UE (o, negli Stati Uniti, un premio SBIR) per finanziare diversi fornitori che sviluppino prototipi concorrenti, poi acquista il migliore su larga scala, comprando lecitamente un'innovazione che doveva essere creata. Salvaguardie di interesse pubblico si applicano per tutto il tempo: trasparenza, equa concorrenza, accessibilità e chiari diritti su PI e dati che impediscono all'ente di restare vincolato a un solo fornitore (capitoli 10.3, 10.5).

## Business case: motivazioni, ROI e TCO

Il ritorno delle partnership di innovazione è **opzionalità e velocità**. Per il costo di un pilot a fasi, compri una vera opzione su una capacità che non avresti potuto comprare né costruire con la stessa rapidità e puoi andartene a basso costo se la scommessa fallisce. Confrontalo con il costruire, che impegna il costo pieno in anticipo contro una capacità interna incerta e con il comprare, che non può acquisire ciò che non esiste ancora. Fare partnership ha spesso il miglior ritorno corretto per il rischio quando la capacità è nuova, non centrale o troppo rischiosa da finanziare da soli. Anche il talento e la tecnologia importati si compongono: le organizzazioni che fanno bene le partnership restano più vicine alla frontiera di quelle che solo costruiscono o comprano.

Sul **costo totale di proprietà**, i costi visibili sono coordinamento, governance e le molte scommesse che non ripagano. I costi nascosti sono fuga di PI, esposizione di sicurezza e dipendenza quando le partnership sono strutturate con noncuranza. Finanziare a fasi e risolvere in anticipo PI, dati e uscita è ciò che tiene sotto controllo il TCO. Il più grande costo silenzioso è il *purgatorio dei pilot*, denaro vero speso in pilot che non scalano mai, ed è per questo che il percorso di produzione e un responsabile interno incaricato appartengono al business case fin dal primo giorno. Per presentare il caso alla leadership, imposta le partnership come un portafoglio di opzioni economiche e a fasi sulla capacità, messo a bilancio esplicitamente per un alto tasso di fallimento e pochi guadagni fuori scala, con una regola ferma: nessun pilot è finanziato senza un responsabile nominato per scalarlo.

## Antipattern e insidie

- **Purgatorio dei pilot:** un cimitero di pilot riusciti che non raggiungono mai la produzione.
- **Teatro dell'innovazione:** partnership annunciate per l'immagine, senza vera intenzione di integrazione.
- **PI irrisolta:** rimandare le questioni di proprietà finché avvelenano una collaborazione funzionante.
- **Disallineamento degli incentivi:** un contratto firmato che maschera parti che vogliono esiti diversi.
- **Fuga del nucleo:** condividere ai margini capacità o dati davvero distintivi.
- **Dipendenza da un solo partner:** capacità critica per la missione vincolata a una singola parte esterna.
- **Impegno big-bang:** finanziare una grande partnership in una sola tranche anziché a fasi per tappa.
- **Contratto al posto della relazione:** affidarsi alle clausole per fare il lavoro che governance e fiducia devono fare.

## Modello di maturità

- **Livello 1, Avvio.** L'innovazione è solo costruire o comprare; le partnership esterne sono ad hoc, guidate dalle personalità e reattive; PI, incentivi e scalatura sono risolti caso per caso e i pilot raramente raggiungono la produzione.
- **Livello 2, Sviluppo.** Girano alcuni pilot, legami di ricerca e collaborazioni con fornitori e poche persone hanno imparato a finanziare a fasi e a risolvere i termini, ma la pratica è incoerente da team a team; il purgatorio dei pilot è comune e dipende da chi guida l'accordo.
- **Livello 3, Standardizzazione.** Un manuale deliberato di partnership è documentato e fatto rispettare in tutta l'organizzazione: scelta del modello, finanziamento a fasi legato a tappe, termini di PI/dati/uscita, responsabili di produzione nominati e revisione di sicurezza di terze parti sono applicati in modo coerente a ogni partnership.
- **Livello 4, Gestione.** Le partnership sono misurate rispetto a valori di riferimento: tasso di conversione da pilot a produzione, costo e tempo per scommessa a fasi, tasso di fallimento del portafoglio rispetto a pochi guadagni fuori scala, esposizione di uscita e concentrazione e PI realizzata. I cancelli di tappa sono fatti rispettare su quell'evidenza e le decisioni di procedere o meno e di scalatura sono guidate dalle metriche anziché dal patrocinio.
- **Livello 5, Orchestrazione.** Il fare partnership è integrato con strategia di portafoglio, appalti e rischio e continuamente migliorato; l'organizzazione è un partner di scelta che apre in modo adattivo i margini giusti, ritira e ridefinisce le partnership man mano che si sposta la frontiera e converte in modo affidabile l'innovazione esterna in capacità rilasciata.

## Spunti di discussione

1. Per la vostra ultima decisione "costruire o comprare", "fare partnership" era davvero sul tavolo?
2. Quanti dei vostri pilot hanno raggiunto la produzione l'anno scorso, e chi possedeva il percorso verso la scala?
3. I vostri contratti di partnership risolvono PI, diritti sui dati e uscita prima che il lavoro cominci?
4. Dove potreste condividere ai margini un vantaggio centrale senza rendervene conto?
5. Qualche capacità critica per la missione dipende da un singolo partner esterno?
6. In un contesto del settore pubblico, quali strumenti di innovazione (partenariati UE, SBIR, sfide) si adattano alla vostra missione?

## Punti chiave

- La partnership di innovazione è la terza opzione deliberata oltre costruire e comprare: collaborare per condividere rischio, conoscenza e ricompensa.
- **Scegli il modello adatto all'obiettivo**, dai pilot al co-sviluppo alle procedure pubbliche di innovazione (partenariati per l'innovazione dell'UE, SBIR).
- **Allinea gli incentivi, risolvi in anticipo PI/dati/uscita** e governa la relazione, non solo il contratto.
- **Finanzia a fasi** e progetta dentro il percorso di produzione per sfuggire al **purgatorio dei pilot**.
- **Proteggi il nucleo; apri i margini:** importa innovazione senza far trapelare vantaggio né creare dipendenza.
- Il ROI è opzionalità e velocità; vedi i capitoli 10.3 (appalti), 10.1 (portafoglio), 10.2 (rischio di terze parti) e 6.1 (costruire/comprare/fare partnership per l'IA).

## Riferimenti e letture di approfondimento

- Henry Chesbrough, *Open Innovation* e *Open Business Models*.
- Clayton Christensen, *The Innovator's Dilemma* (perché gli incumbent faticano a innovare internamente).
- Unione europea, Direttiva 2014/24/UE, la procedura di appalto di *partenariato per l'innovazione*.
- U.S. Small Business Administration, programma *Small Business Innovation Research (SBIR/STTR)*.
- Vijay Govindarajan e Chris Trimble, *The Other Side of Innovation* (eseguire l'innovazione, battere il purgatorio dei pilot).
- Ronald Adner, *The Wide Lens* (ecosistemi di innovazione e dipendenze dai partner).
- Risorse GovTech e di innovazione del settore pubblico (per esempio GDS, USDS, Public Digital); vedi il capitolo 10.3.
