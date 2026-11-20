# 5.1 Fondamenti di UX

## Panoramica e motivazioni

L'[esperienza utente](https://en.wikipedia.org/wiki/User_experience) (UX) riguarda il capire le persone (i loro obiettivi, i loro contesti, i loro vincoli) e poi dare forma al software perché le aiuti a riuscire con il minimo attrito. Non è una decorazione da applicare alla fine. È un modo di lavorare che comincia prima della prima riga di codice e continua ben oltre il rilascio. Questo capitolo tratta le pratiche di ricerca, modellazione e [design thinking](https://en.wikipedia.org/wiki/Design_thinking) che permettono a una grande organizzazione di prendere decisioni di prodotto dall'evidenza anziché da congetture.

Per i grandi team, la UX è tanto un problema di coordinamento quanto un mestiere. Quando decine di squadre rilasciano in un unico prodotto condiviso, modelli mentali disallineati, flussi duplicati e terminologia contraddittoria si accumulano in un insieme confuso che nessun team singolo possiede. Una base di UX condivisa, costruita su persona comuni, mappe del percorso concordate e un'[architettura dell'informazione](https://en.wikipedia.org/wiki/Information_architecture) documentata, dà a ogni team la stessa mappa dell'utente, così che le loro decisioni separate si sommino in un'esperienza coerente. Senza di essa, ogni team ottimizza localmente e il prodotto nel suo complesso non ha senso.

Impresa ed ente pubblico alzano la posta. Il software aziendale ha spesso utenti vincolati che non possono andarsene, quindi la cattiva UX si paga in formazione, ticket di assistenza, errori e produttività persa anziché in persone che se ne vanno. I servizi pubblici raggiungono spesso l'intera popolazione, comprese persone in crisi, con dispositivi vecchi, con poca fiducia digitale o senza alcun fornitore alternativo. Qui la qualità della UX è una questione di equità e fiducia civica: una domanda di prestazioni progettata male può negare a qualcuno cibo o alloggio, non perché non ne abbia diritto, ma perché non ha potuto finire il modulo.

## Principi chiave

- Progetta per persone reali che svolgono compiti reali in condizioni reali, non per un utente idealizzato con una connessione veloce e piena attenzione.
- La ricerca riduce il rischio. Il momento più economico per scoprire un'ipotesi sbagliata è prima di averci costruito sopra.
- Gli utenti non sanno dirti in modo affidabile che cosa faranno; osserva il comportamento, non solo la preferenza dichiarata.
- Concentrati sul compito che l'utente sta cercando di svolgere, non sulla funzionalità che vuoi rilasciare.
- La coerenza è una funzionalità: un modello mentale coerente in tutto il prodotto abbassa il carico cognitivo.
- [Accessibilità](https://en.wikipedia.org/wiki/Accessibility) e inclusione fanno parte della buona UX fin dall'inizio, non di un passaggio di conformità successivo.
- I metodi qualitativi e quantitativi rispondono a domande diverse; usali entrambi.
- Una ricerca piccola e frequente batte studi rari e pesanti.

## Raccomandazioni

### Stabilisci una ricerca continua a metodi misti

Mira a una pratica di ricerca leggera ma continua anziché a grandi studi occasionali. Le interviste rivelano motivazioni e modelli mentali. I [test di usabilità](https://en.wikipedia.org/wiki/Usability_testing) rivelano dove i progetti cedono; da cinque a otto partecipanti per ciclo fanno emergere la maggior parte dei problemi gravi. I sondaggi misurano gli atteggiamenti su larga scala ma non possono spiegare il "perché". Analisi e strumentazione mostrano che cosa le persone fanno davvero nell'intera popolazione. Abbina un metodo qualitativo (perché) a uno quantitativo (quanti), così che i risultati siano sia spiegati sia dimensionati. E tieni un archivio della ricerca, così che le intuizioni restino ricercabili e riutilizzabili tra i team anziché perdersi nelle diapositive di una sola squadra.

### Modella gli utenti con persona, mappe del percorso e jobs-to-be-done

Costruisci un piccolo insieme di persona basate sull'evidenza che catturino obiettivi, contesti e vincoli, non caricature demografiche. Imposta i bisogni come jobs-to-be-done, il risultato di fondo che un utente sta cercando di ottenere anziché una funzionalità ("quando perdo il lavoro, voglio capire in fretta a quale sostegno ho diritto, così da continuare a pagare l'affitto"). Questo mantiene l'attenzione sugli esiti anziché sulle funzionalità. Le mappe del percorso tracciano l'intera esperienza attraverso i canali e nel tempo, esponendo divari e passaggi di consegne che nessuna schermata singola rivela. Per i servizi con pesanti operazioni back-stage (call center, operatori di pratiche, evasione degli ordini), usa i [service blueprint](https://en.wikipedia.org/wiki/Service_blueprint) per collegare l'esperienza front-stage ai sistemi e al personale che stanno dietro.

### Progetta deliberatamente l'architettura dell'informazione

L'architettura dell'informazione (IA) è come contenuti, funzionalità e navigazione sono strutturati ed etichettati. Usa il [card sorting](https://en.wikipedia.org/wiki/Card_sorting) e il tree testing per ricavare quella struttura dai modelli mentali degli utenti anziché dal tuo organigramma. Un fallimento comune nelle grandi organizzazioni è esporre i confini dei dipartimenti interni come navigazione di primo livello. Stabilisci un vocabolario controllato così che lo stesso concetto abbia lo stesso nome ovunque. La [progettazione dell'interazione](https://en.wikipedia.org/wiki/Interaction_design) poi definisce il comportamento momento per momento: stati, feedback, ripristino dagli errori e flusso tra i passi.

### Applica il design thinking in modo pragmatico

Il modello del doppio diamante (divergere poi convergere per definire il problema giusto, poi divergere e convergere per progettare la soluzione giusta) è una cornice utile. Trattalo però come una mentalità, non un processo rigido a cancelli. Nella pratica, conduci cicli stretti: formula un'ipotesi, abbozza, testa con una manciata di utenti e impara in pochi giorni. Riserva la scoperta più pesante ai problemi davvero nuovi o ad alto rischio. E guardati dal "teatro dell'innovazione", dove i workshop producono post-it ma nessuna modifica rilasciata.

### Integra la UX nella consegna

Inserisci designer e ricercatori nei team di consegna anziché gestire un "dipartimento UX" separato che passa le specifiche oltre un muro. Fai dei risultati della ricerca un input stabile della prioritizzazione. Metti cancelli di qualità UX, come benchmark di usabilità e controlli di accessibilità, nella definizione di completato. E segui le metriche di esito (successo del compito, tempo sul compito, tasso di errore, soddisfazione) proprio accanto alle tue metriche di consegna.

## Compromessi: vantaggi e svantaggi

| Approccio | Vantaggi | Svantaggi |
|---|---|---|
| Ricerca di scoperta continua | Coglie presto i problemi, costruisce comprensione condivisa | Costo continuo, richiede una pipeline di reclutamento e personale competente |
| Ricerca pesante in anticipo | Intuizione profonda prima di un grande investimento | Lenta, può ritardare l'apprendimento che solo il rilascio rivela |
| Decisioni solo da analisi | Scala, oggettive, economiche una volta strumentate | Spiegano che cosa ma non perché; cieche ai non utenti e ai casi limite |
| Persona e mappe del percorso | Allineano molti team su un modello dell'utente | Invecchiano, possono diventare finzione se non aggiornate con i dati |
| Designer inseriti nei team | Feedback rapido, responsabilità condivisa | Più difficile mantenere coerente il mestiere tra molti team |

Ogni organizzazione bilancia investimento nella ricerca e velocità di consegna. L'errore è trattarlo come un aut aut. La posizione produttiva è proporzionale: spendi più scoperta sulle decisioni costose da invertire (IA centrale, flussi primari, scelte di piattaforma) e meno sui dettagli che puoi cambiare facilmente dopo. Il costo della ricerca è quasi sempre piccolo rispetto al costo di costruire bene la cosa sbagliata.

## Domande da discutere con il tuo team

1. **Chi possiede l'architettura dell'informazione e il vocabolario controllato condivisi, e che cosa succede quando un team vuole discostarsi?** Su larga scala il fallimento più comune è lasciare che ogni squadra esponga la propria struttura da organigramma e i propri nomi per lo stesso concetto, così il prodotto finisce con tre parole per una cosa e una navigazione che rispecchia i dipartimenti anziché i compiti degli utenti. Decidi ora se IA e vocabolario sono posseduti centralmente, ricavati da card sorting e tree testing anziché da politica interna e come un team richiede una modifica. Conta di più nei contesti aziendali e governativi perché gli utenti vincolati non possono andarsene, quindi l'incoerenza si paga in formazione, ticket di assistenza ed errori anziché in abbandono. Porta come evidenza l'elenco attuale di termini duplicati e flussi in conflitto. Se non sai nominare un responsabile, quello è il tuo primo punto d'azione.

2. **Qual è la nostra pipeline di reclutamento dei partecipanti alla ricerca, e raggiunge utenti con assistenza digitale, poco sicuri e non digitali?** La scoperta continua funziona solo se puoi mettere davanti a utenti reali ogni settimana e le persone più difficili da reclutare sono spesso quelle che più hanno bisogno del servizio: persone in crisi, con dispositivi vecchi o che di solito si affidano ad aiuto. Testare solo volontari sicuri e connessi ti dà una lettura lusinghiera ma falsa, specialmente per i servizi pubblici dove l'equità di accesso è il punto. Concorda chi gestisce il reclutamento, che incentivi offri e come osservi le sessioni con assistenza digitale senza aggiungere onere a una persona vulnerabile. Porta la demografia dei partecipanti dei tuoi ultimi tre studi e confrontala con la tua effettiva base di utenti. Se pende verso utenti facili da raggiungere, correggi la pipeline prima di fidarti dei risultati.

3. **Quali cancelli di qualità UX appartengono alla nostra definizione di completato, e come evitiamo che diventino teatro?** Inserire designer e ricercatori ripaga solo se la ricerca è un input stabile della prioritizzazione e se i controlli di usabilità e accessibilità bloccano davvero il rilascio di una storia, non una presentazione che tutti approvano con un cenno e ignorano. Scegli metriche di esito concrete da seguire accanto alle metriche di consegna: successo del compito, tempo sul compito, tasso di errore e soddisfazione. Il rischio è una ricerca condotta per giustificare decisioni già prese, quindi concorda chi può porre il veto a un lancio su un cancello UX e quale evidenza prevale sull'opinione di un dirigente. Porta una funzionalità recente e chiediti se la sua ricerca ha cambiato la decisione o l'ha solo decorata. Se i risultati non spostano mai una roadmap, i tuoi cancelli sono cosmetici.

4. **Come evitiamo che persona, mappe del percorso e IA decadano in finzione una volta che la ricerca che le ha prodotte ha un anno?** I modelli condivisi sono ciò che permette a decine di team di progettare verso un'unica esperienza coerente, ma funzionano solo finché descrivono ancora utenti reali e nel momento in cui una persona diventa un artefatto che le persone citano per vincere discussioni anziché una sintesi dell'evidenza, fa danno attivo. Decidi chi possiede l'aggiornamento di ciascun modello, con quale cadenza e rispetto a quali dati (interviste fresche, analisi, temi dell'assistenza) e concorda una data visibile di "ultima convalida" così che i modelli vecchi siano ovvi. La considerazione contraria è il costo: aggiornare tutto di continuo è uno spreco, quindi lega la frequenza di aggiornamento a quanto in fretta quella parte della base di utenti o del percorso cambia davvero. Porta la provenienza delle tue persona principali attuali e chiediti quando ciascuna è stata controllata per l'ultima volta con un utente reale. Nelle imprese e negli enti pubblici, dove una base di utenti vincolata o pubblica si sposta lentamente ma con conseguenze (una popolazione che invecchia, una nuova prestazione, una transizione di dispositivi), un modello che deriva in silenzio può indirizzare anni di investimento verso utenti che non esistono più.

5. **Dove vive l'accessibilità nel nostro processo, e possiamo provare che un rilascio la soddisfa prima che esca anziché dopo una lamentela?** Trattare l'accessibilità come un passaggio di conformità tardivo è sia il fallimento più comune sia il più costoso, perché adattare semantica, ordine del focus e contrasto a un'interfaccia già costruita costa molto più che progettarli dentro. Decidi a quale standard vi tenete (per esempio WCAG, le Web Content Accessibility Guidelines), se la conformità è un cancello bloccante nella definizione di completato e chi risponde quando una funzionalità inaccessibile raggiunge la produzione. La tensione è velocità contro inclusione e i team sotto scadenza lasceranno cadere in silenzio i controlli che non sono fatti rispettare. Porta il tuo ultimo audit, la copertura automatica e manuale che lo sostiene e il numero di problemi di accessibilità trovati dopo il rilascio anziché prima. Per gli enti pubblici soprattutto non è cortesia facoltativa: è spesso un dovere legale e una questione di equità, poiché un servizio pubblico che esclude gli utenti disabili o con assistenza digitale ha fallito nel suo scopo di fondo, non in uno secondario.

6. **Quando le nostre analisi e la nostra ricerca qualitativa discordano, come decidiamo a quale credere, e chi arbitra?** Le grandi organizzazioni accumulano sia cruscotti che mostrano che cosa fanno migliaia di utenti sia interviste che spiegano perché una manciata si comporta in un certo modo e i due indicheranno di routine direzioni opposte: un flusso con alto completamento che in silenzio umilia le persone, o una funzionalità che gli utenti lodano nelle sessioni ma non toccano mai su larga scala. Concorda in anticipo come triangoli, a quale domanda ciascun metodo è creduto di rispondere (analisi per grandezza e portata, ricerca per causa e significato) e chi ha l'autorità di decidere quando confliggono. Il rischio è scegliere a piacere la fonte che lusinga il piano già scelto. Porta un recente disaccordo concreto e ripercorri come è stato davvero risolto. Nei contesti aziendali e pubblici la posta è più acuta perché le analisi sottostimano sistematicamente proprio le persone che contano di più: non utenti, chi abbandona e chi usa tecnologie assistive raramente compaiono nel funnel, quindi fidarsi dei soli numeri può rendere invisibili gli esclusi.

## Lente settoriale

**Startup.** Non hai un ricercatore né tempo per un archivio, quindi fai della ricerca un'abitudine dei fondatori: siediti accanto a cinque utenti reali per un pomeriggio prima di costruire la prossima cosa. Salta persona e mappe del percorso formali; una comprensione condivisa dell'unico compito che stai risolvendo, aggiornata guardando le persone ogni settimana, batte una documentazione che nessuno mantiene. Il tuo vantaggio è che l'intero team può assorbire un'intuizione lo stesso giorno in cui compare, quindi proteggi quella velocità e resisti alla cerimonia.

**Piccola impresa.** Senza uno specialista di UX e con un budget ridotto, appoggiati alle convenzioni che i tuoi utenti già conoscono anziché inventare le tue e compra strumenti con valori predefiniti sensati anziché progettare i flussi da zero. Fai tu stesso la ricerca economica e di alto valore: una manciata di sessioni di usabilità in videochiamata e una lettura dei tuoi ticket di assistenza faranno emergere la maggior parte dei problemi gravi. Tratta le basi dell'accessibilità (contrasto, etichette, accesso da tastiera) come requisiti minimi che ottieni da una buona libreria di componenti anziché un progetto per cui dotare di personale.

**Grande impresa.** Il problema centrale è la coerenza tra molti team, quindi investi nelle fondamenta condivise: persona possedute, mappe del percorso mantenute, un vocabolario controllato e un'architettura dell'informazione documentata verso cui le squadre progettano anziché attorno. Inserisci designer e ricercatori nei team di consegna, ma governa il mestiere centralmente così che il prodotto non si frammenti in dialetti incoerenti. Finanzia un archivio della ricerca e cancelli di qualità nella definizione di completato e segui le metriche di esito UX come portafoglio così che l'ottimizzazione locale di un singolo team non degradi l'insieme.

**Ente pubblico.** Accessibilità ed equità di accesso sono doveri, non preferenze, quindi tieni i rilasci a uno standard pubblicato e fai ricerca con l'intera gamma del pubblico, compresi utenti con assistenza digitale, poco sicuri e non digitali. Appalti e trasparenza plasmano la consegna: pubblica i tuoi principi di design e i metodi di ricerca, struttura i servizi attorno agli eventi della vita dei cittadini anziché ai dipartimenti interni e conserva le evidenze dei test per l'audit. Poiché gli utenti spesso non hanno un fornitore alternativo, un flusso che non possono completare nega un servizio, quindi tratta il completamento da parte dell'utente più difficile da raggiungere come la vera misura del successo.

## Esempi

**Startup.** Una startup di quattro persone che costruisce uno strumento di prenotazione per piccoli ambulatori aveva opinioni forti su ciò di cui avevano bisogno i receptionist, ma nessuna evidenza. Prima di scrivere altre funzionalità, i fondatori si sono seduti accanto a cinque receptionist per un pomeriggio ciascuno e li hanno guardati lavorare. Hanno scoperto che il vero dolore non era la velocità di prenotazione ma le doppie prenotazioni causate da una vista calendario confusa, qualcosa che nessuno aveva pensato di menzionare nelle precedenti chiamate di vendita. Riformulare il prodotto attorno a quel solo compito, abbozzando e testando correzioni con le stesse cinque persone nell'arco di una settimana, ha trasformato una prova che si arenava nei loro primi clienti paganti.

**Grande impresa.** Una banca multinazionale ha consolidato sette strumenti interni regionali di erogazione dei prestiti in un'unica piattaforma. Anziché unire gli insiemi di funzionalità, il team ha condotto mappatura del percorso e service blueprint con i sottoscrittori di più regioni. Hanno scoperto che le "differenze regionali" che tutti davano per scontate erano per lo più terminologia incoerente e ordine delle schermate, non vere differenze di processo. Un'IA unificata e un vocabolario condiviso hanno tagliato in modo sostanziale i tempi di formazione dei sottoscrittori e ridotto gli errori di elaborazione, perché il personale ora condivideva un unico modello mentale.

**Ente pubblico.** Un'autorità fiscale nazionale che riprogetta il proprio servizio di dichiarazione online ha condotto test di usabilità moderati con contribuenti di età, dispositivi e livelli di fiducia digitale diversi, più osservazione con assistenza digitale di persone che di solito si affidano ad aiuto. I test hanno rivelato che i titoli di sezione carichi di gergo facevano abbandonare o compilare male. Riformulare i contenuti attorno ai jobs-to-be-done dei contribuenti e ristrutturare l'IA attorno agli eventi della vita anziché ai codici fiscali interni ha aumentato il completamento riuscito in autonomia e ridotto il volume del call center, abbassando direttamente il costo di servizio e migliorando l'equità di accesso.

## Business case: motivazioni, ROI e TCO

Il ritorno della UX viene da tre leve: più successo (più utenti completano compiti di valore), minor costo di servizio (meno contatti con l'assistenza, meno formazione, meno errori) e meno rilavorazione (cogliere le direzioni sbagliate prima che vengano costruite). Nei contesti aziendali dove gli utenti sono vincolati, il vantaggio compare come produttività e meno errori anziché conversione; pochi secondi risparmiati per transazione, su migliaia di dipendenti, si compongono in grandi risparmi annui.

Il costo totale di proprietà deve pesare il costo di adottare contro il costo di non adottare. I costi di adozione sono facili da vedere: ricercatori e designer, reclutamento e incentivi per i partecipanti, strumenti e tempo nel calendario. Il costo del non adottare è maggiore ma più difficile da individuare: transazioni abbandonate, onere di assistenza e formazione, costose riprogettazioni tardive, lanci falliti ed esposizione reputazionale o legale quando i servizi pubblici escludono persone. Poiché questi costi sono distribuiti tra bilanci di assistenza, formazione e operazioni anziché sulla linea di prodotto, la leadership spesso li sottovaluta.

Per presentare il caso alla leadership, lega la UX a metriche che i dirigenti già seguono: tassi di completamento e conversione, costo per transazione, volume di ticket di assistenza, giorni di formazione e tassi di errore e rilavorazione. Conduci un piccolo pilota strumentato che mostri un prima e dopo misurabile, poi estrapola sul portafoglio. Impostare la ricerca come riduzione del rischio sulle decisioni irreversibili tende a risuonare con gli stakeholder di finanza e governance.

## Antipattern e insidie

- **Design guidato dall'HiPPO**: decisioni prese dall'opinione della persona meglio pagata anziché dall'evidenza.
- **Teatro della ricerca**: studi condotti per giustificare decisioni già prese, risultati ignorati.
- **Persona come finzione**: profili inventati mai convalidati rispetto a utenti reali, usati per vincere discussioni.
- **Organigramma come IA**: navigazione che rispecchia i dipartimenti interni anziché i compiti degli utenti.
- **Ricerca big-bang**: studi rari e costosi che arrivano troppo tardi per cambiare qualcosa.
- **Testare solo il percorso felice**: ignorare stati di errore, casi limite e utenti sotto stress.
- **Design come ultima mano di vernice**: portare la UX solo per far "sembrare bella" una build finita.
- **Ignorare gli utenti con assistenza e non digitali**: progettare solo per utenti sicuri e connessi.

## Modello di maturità

**Livello 1: Avvio.** Nessuna pratica UX dedicata. Le decisioni sono prese dall'opinione e dall'istinto della persona meglio pagata. La ricerca, se avviene, è ad hoc e reattiva, innescata da un lancio andato male. Flussi e terminologia sono incoerenti tra i team e nessuno possiede l'esperienza complessiva.

**Livello 2: Sviluppo.** Alcuni team hanno designer e conducono occasionali test di usabilità ed esistono poche persona o mappe del percorso, ma la pratica varia molto tra le squadre e non è mantenuta. La UX è trattata come una fase anziché come una disciplina continua ed è spesso aggirata sotto la pressione del calendario. Il buon lavoro avviene a chiazze ma non si somma nel prodotto.

**Livello 3: Standardizzazione.** Una ricerca continua a metodi misti alimenta la prioritizzazione e persona condivise, mappe del percorso e un'IA a vocabolario controllato sono documentate e usate tra i team. I cancelli di qualità UX, compresi benchmark di usabilità e controlli di accessibilità, stanno nella definizione di completato e sono fatti rispettare nell'organizzazione. Un archivio della ricerca ricercabile mantiene riutilizzabili le intuizioni anziché intrappolate nelle diapositive di una sola squadra.

**Livello 4: Gestione.** La pratica è misurata rispetto a valori di riferimento anziché semplicemente eseguita. Segui successo del compito, tempo sul compito, tasso di errore, soddisfazione e conformità all'accessibilità come metriche concordate, fissi obiettivi e le osservi nel corso dei rilasci. I campioni di partecipanti alla ricerca sono controllati rispetto alla base reale di utenti così che i risultati siano rappresentativi, i cancelli di qualità riportano tassi di superamento anziché opinioni e il costo della ricerca è pesato rispetto alle riduzioni misurate di contatti con l'assistenza, formazione e rilavorazione. Le decisioni di rilasciare o fermare poggiano sull'evidenza rispetto a quei riferimenti.

**Livello 5: Orchestrazione.** La ricerca è continua, legata agli esiti e integrata con la pianificazione di prodotto, business e rischio nell'organizzazione. I team conducono esperimenti controllati, chiudono il ciclo da intuizione a modifica rilasciata a effetto misurato e ritirano o ridefiniscono i modelli di utenti man mano che la popolazione e i suoi percorsi cambiano. La base di UX si adatta di continuo: persona, percorsi, IA e standard sono aggiornati sull'evidenza e l'organizzazione riequilibra dove investe la scoperta al mutare di reversibilità e rischio.

## Spunti di discussione

- Quanta scoperta è "abbastanza" prima di impegnarsi in una direzione, e chi decide?
- Come mantenete vive persona e mappe del percorso anziché lasciarle diventare artefatti stantii?
- Quando analisi quantitative e ricerca qualitativa discordano, a quale credete e perché?
- Come dovrebbe una grande organizzazione bilanciare uno standard UX centrale con l'autonomia di ciascun team?
- Qual è il modo giusto di fare ricerca su servizi usati da persone in crisi senza aggiungere al loro onere?
- Come misurate il ROI di una ricerca che previene un errore che quindi non avete mai fatto?

## Punti chiave

- La UX è un modo di lavorare fin dall'inizio, non decorazione alla fine.
- Combina i metodi qualitativi (perché) con quelli quantitativi (quanti).
- Modella gli utenti con persona basate sull'evidenza, mappe del percorso, jobs-to-be-done e service blueprint.
- Struttura l'informazione attorno ai modelli mentali degli utenti, non all'organigramma.
- Tratta il design thinking come una mentalità pragmatica con cicli di apprendimento stretti, non un processo rigido.
- Il costo della ricerca è piccolo rispetto al costo di costruire la cosa sbagliata.
- Nelle imprese e negli enti pubblici, la qualità della UX si traduce direttamente in produttività, costo di servizio ed equità di accesso.

## Riferimenti e letture di approfondimento

- Don Norman, *The Design of Everyday Things*
- Steve Krug, *Don't Make Me Think*
- Erika Hall, *Just Enough Research*
- Kim Goodwin, *Designing for the Digital Age*
- Louis Rosenfeld, Peter Morville e Jorge Arango, *Information Architecture: For the Web and Beyond*
- Clayton Christensen et al., *Competing Against Luck* (jobs-to-be-done)
- Alan Cooper, *The Inmates Are Running the Asylum*
- Jakob Nielsen, *Usability Engineering*
- UK Government Digital Service, *Service Manual* e *Design Principles*
- U.S. General Services Administration, *18F Methods* e le indicazioni di ricerca dello *U.S. Web Design System*
- Nielsen Norman Group, articoli e rapporti sui metodi di ricerca
