# 10.7 Agile

## Panoramica e motivazioni

L'[agile](https://en.wikipedia.org/wiki/Agile_software_development) è una mentalità per consegnare software (e valore) in modo iterativo, incrementale e in stretta collaborazione con le persone che lo useranno. Codificato nel *Manifesto per lo sviluppo agile del software* del 2001, si capisce meglio non come un processo ma come un insieme di **valori e principi**: dare priorità a individui e interazioni, software funzionante, collaborazione con il cliente e risposta al cambiamento, rispetto ai predefiniti pesanti di piani, contratti e documentazione che li hanno preceduti. Quadri come [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)), [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)) ed [Extreme Programming](https://en.wikipedia.org/wiki/Extreme_programming) (XP) sono *implementazioni* di quella mentalità. Sono punti di partenza utili, ma non la mentalità stessa. Questo capitolo completa il capitolo 1.4 (modi di lavorare, che passa in rassegna i metodi in generale) approfondendo l'Agile in particolare.

L'Agile è guidato dalla stessa forza che anima le pipeline di scoperta e consegna (capitoli 11.1–11.2): i requisiti del software si *scoprono*, non sono del tutto noti in anticipo e il mondo cambia più in fretta di quanto un lungo piano possa assorbire. La consegna big-bang, che pianifica tutto prima, produce ripetutamente sistemi in ritardo, fuori budget e, peggio di tutto, sbagliati, perché tutto l'apprendimento arriva alla fine, quando è più costoso agire. La scommessa centrale dell'Agile è semplice: brevi cicli di costruzione di software vero e funzionante e di ottenimento di riscontri veri battono lunghi cicli di speculazione. Fatto bene, riduce il rischio di continuo anziché rimandarlo.

Per i grandi team, le imprese e i governi, l'Agile è insieme potente e di frequente storpiato. Le imprese lo adottano su centinaia di team e spesso lo riducono a rituale ("ora facciamo gli stand-up") senza cambiare come si prendono le decisioni o come si misura il valore. Il governo ha abbracciato l'Agile deliberatamente, perché una consegna iterativa e centrata sull'utente riduce dimostrabilmente il rischio dei grandi programmi pubblici: lo U.S. Digital Service e il suo *Digital Services Playbook*, il Government Digital Service del Regno Unito e il suo Service Standard e le riforme degli appalti agili sono nati in parte in risposta a fallimenti di alto profilo della [cascata](https://en.wikipedia.org/wiki/Waterfall_model). Il premio è reale. Così lo è la modalità di fallimento dell'"agile solo di nome".

## Principi chiave

- **Dai valore ai quattro valori del Manifesto** (persone, software funzionante, collaborazione e capacità di risposta) più che agli artefatti di processo.
- **Consegna software funzionante di frequente** in piccoli incrementi; il software funzionante è la misura primaria del progresso.
- **Accogli il cambiamento**, anche tardivo; l'adattabilità è una funzionalità, non un fallimento.
- **Costruisci attorno a team motivati, autorizzati e auto-organizzati.**
- **Collabora di continuo con utenti e stakeholder.**
- **Rifletti e migliora** con una cadenza regolare.
- **Sostieni un ritmo umano** e l'eccellenza tecnica: la velocità senza maestria crolla.

## Raccomandazioni

### Ancorati a valori e principi, non alle cerimonie

La singola raccomandazione Agile più importante è partire dal *perché*. Un team che tiene uno stand-up quotidiano, una revisione dello sprint e una retrospettiva, ma si impegna comunque su un ambito fisso a una data fissa, nasconde le cattive notizie e non cambia mai il piano, non è agile. È una cascata con riunioni. Usa i dodici principi come lista di controllo per una genuina agilità. Consegni software funzionante spesso? Puoi accogliere un cambiamento nella prossima iterazione? Il team decide *come* fare il lavoro? Il cliente è davvero nel ciclo? Se le cerimonie non producono quegli esiti, correggi gli esiti, non le cerimonie.

### Scegli un quadro come punto di partenza, non come religione

Scegli un quadro che si adatti al lavoro e adattalo:

- **Scrum:** sprint a tempo, un arretrato prioritizzato e ruoli definiti (product owner, scrum master, sviluppatori). Buono per la consegna di funzionalità con un chiaro product owner; debole quando il lavoro è molto guidato dalle interruzioni.
- **Kanban:** flusso continuo con espliciti limiti di lavoro in corso e un sistema a trazione. Buono per supporto, operazioni e arrivi imprevedibili (e fondato direttamente sulla teoria del flusso e delle code, vedi i capitoli 11.2, 11.3). Limitare il WIP accorcia il tempo di consegna ([legge di Little](https://en.wikipedia.org/wiki/Little%27s_law)).
- **Extreme Programming (XP):** pratiche ingegneristiche tra cui [sviluppo guidato dai test](https://en.wikipedia.org/wiki/Test-driven_development), [programmazione in coppia](https://en.wikipedia.org/wiki/Pair_programming), [integrazione continua](https://en.wikipedia.org/wiki/Continuous_integration), refactoring, piccoli rilasci. La spina dorsale tecnica che rende sostenibile qualsiasi quadro.
- **Scrumban** e miscele: combinazioni pragmatiche su cui molti team maturi convergono.

I quadri sono impalcature. Tieni ciò che aiuta, lascia ciò che non lo fa e non lasciare mai che "lo dice il quadro" prevalga su "i principi dicono perché".

### Insisti sull'eccellenza tecnica

L'Agile senza disciplina ingegneristica degrada in fretta in una veloce produzione di codice non mantenibile, "dark scrum", in cui i team sprintano fino a una palude di difetti e [debito tecnico](https://en.wikipedia.org/wiki/Technical_debt). Le pratiche XP non sono extra opzionali. Integrazione continua (capitolo 8.1), test automatici (capitolo 2.4), refactoring, sviluppo trunk-based (capitolo 2.6) e progetto pulito (capitolo 2.2) sono ciò che permette a un team di continuare a cambiare il software a basso costo, che è l'intera premessa dell'agilità. Il ritmo sostenibile conta per la stessa ragione: team esauriti non possono sostenere qualità né capacità di risposta.

### Scala con cura e preferisci il descalare

I quadri di scalatura, come SAFe (Scaled Agile Framework), LeSS, Nexus e Scrum@Scale, coordinano molti team verso obiettivi condivisi. Possono aiutare, ma portano un avvertimento (che riecheggia il capitolo 1.4): i pesanti quadri di scalatura spesso reintroducono proprio il comando e controllo e l'onere di pianificazione che l'Agile doveva rimuovere. Prima di adottare un grande quadro, prova il *descalare*. Organizzati attorno a team indipendenti e allineati al flusso con chiara proprietà e dipendenze minime tra team (capitolo 1.2), così da aver bisogno fin dall'inizio di meno macchinario di coordinamento. Dove il coordinamento è davvero richiesto, aggiungi la struttura più leggera che funziona e collegala agli esiti (OKR, obiettivi e risultati chiave, capitolo 11.1), non alla produzione.

### Rendi reale l'agilità in impresa e governo

La consegna adattiva e i vincoli istituzionali possono coesistere, ma serve un progetto deliberato:

- **Governance ibrida:** un nucleo di consegna adattivo dentro un guscio predittivo di finanziamento e conformità (capitolo 10.6), così che l'iterazione soddisfi anziché combattere la supervisione.
- **Appalti agili:** contratti modulari e basati sugli esiti e incrementi più brevi anziché un solo megacontratto a ambito fisso; è qui che l'Agile del settore pubblico più spesso riesce o fallisce.
- **Conformità man mano:** costruisci audit, accessibilità (capitolo 5.3) e sicurezza (capitolo 4.1) nell'incremento tramite automazione e funzioni di idoneità (controlli automatici che verificano di continuo proprietà architetturali e di qualità; capitoli 8.5, 1.6), non un cancello tardivo.
- **Vero accesso agli utenti:** il più difficile e il più importante. I team hanno bisogno di un contatto genuino con cittadini o clienti, che regole di appalto e di sicurezza spesso ostacolano.

### Migliora di continuo, e dicendolo sul serio

La retrospettiva è il motore di miglioramento dell'Agile ed è inutile se non produce cambiamento. Conduci retrospettive che generino un piccolo numero di azioni concrete e possedute e portale davvero a termine prima della successiva. Misura gli esiti (la modifica ha mosso un risultato chiave? vedi il capitolo 11.1) e il flusso (i tempi di consegna si accorciano? vedi i capitoli 11.2, 11.3). Non misurare la velocità: è un segnale di capacità che diventa una bugia nel momento in cui lo usi come obiettivo di produttività.

## Compromessi: vantaggi e svantaggi

| Decisione | Vantaggi | Svantaggi |
|---|---|---|
| **Agile (adattivo)** | Riscontro rapido; assorbe il cambiamento; valore precoce e continuo | Più difficile fissare in anticipo ambito/costo; richiede cliente coinvolto e disciplina |
| **Cascata (predittivo)** | Ambito prevedibile; adatto a contratti/audit | Riscontro tardivo; rischio big-bang; scarso adattamento a requisiti incerti |
| **Scrum** | Cadenza, ruoli, focus; largamente compreso | Onere di cerimonia; fatica con il lavoro guidato dalle interruzioni |
| **Kanban** | Flusso, limiti WIP, flessibile; ottimo per le operazioni | Meno struttura; richiede disciplina per tenere i limiti |
| **Scalatura pesante (SAFe)** | Coordina molti team; familiare alle grandi organizzazioni | Può reintrodurre comando e controllo; pesante di cerimonie |
| **Descalare / autonomia dei team** | Meno onere di coordinamento; team più veloci | Richiede basso accoppiamento e forte piattaforma/proprietà |

La tensione che definisce è **adattabilità contro prevedibilità** e il classico errore di lettura è che l'Agile significhi "nessun piano". Non è così. Significa pianificare di continuo e impegnarsi su *esiti e cadenza* lasciando flettere l'*ambito*. L'altra trappola ricorrente è trattare l'Agile *solo* come processo (cerimonie) o *solo* come ingegneria (XP). Ha bisogno di entrambi.

## Domande da discutere con il tuo team

1. **Nel vostro contesto aziendale o governativo, i vostri contratti sono modulari e basati sugli esiti, o la consegna è chiusa dentro un solo megacontratto a ambito fisso?** Gli appalti agili sono dove l'agilità del settore pubblico più spesso riesce o fallisce, perché un singolo contratto a prezzo fisso e ambito fisso impone la cascata a prescindere da come i team di consegna chiamino le proprie riunioni. Contratti modulari e basati sugli esiti con incrementi più brevi lasciano flettere l'ambito verso un nucleo prezioso dentro un finanziamento fisso, che è esattamente lo schema dietro i moderni successi del settore pubblico e l'antidoto ai passati fallimenti big-bang. Portate evidenza: guardate i vostri contratti attuali e chiedetevi se un fornitore è pagato per software funzionante dimostrato o per un ambito fisso firmato anni fa. La risposta dovrebbe plasmare come strutturate il prossimo appalto molto più di quale quadro i vostri team adottano internamente. Non potete essere adattivi nella consegna mentre il contratto impone un go-live lontano e tutto o niente.

2. **Audit, accessibilità e sicurezza sono incorporati in ogni incremento attraverso l'automazione, o aggiunti come cancello tardivo?** La conformità man mano è ciò che permette alla consegna adattiva di coesistere con i vincoli istituzionali: costruite i controlli nell'incremento tramite automazione e funzioni di idoneità anziché serbarli per una corsa prima del rilascio. Un cancello di conformità tardivo reintroduce il rischio big-bang che l'Agile esiste per rimuovere, perché i problemi costosi emergono alla fine quando sono più difficili da correggere. Portate evidenza: per il vostro ultimo incremento, controllate se accessibilità, sicurezza ed evidenza di audit sono state verificate automaticamente nella pipeline o rimandate a una revisione manuale prima del lancio. La risposta dovrebbe spingere queste proprietà in controlli automatici continui, così che la supervisione sia soddisfatta dall'atto di costruire anziché da una fase separata. È anche ciò che mantiene onesto un programma regolamentato tra un audit e l'altro anziché solo nelle settimane prima di uno.

3. **Come sapreste se i vostri team stanno sprintando verso il debito tecnico, e che cosa protegge un ritmo sostenibile sotto la pressione del lancio?** L'Agile senza disciplina ingegneristica degrada in dark scrum, in cui i team sprintano veloci in una palude di difetti e codice non mantenibile e team esauriti non possono sostenere qualità né capacità di risposta. Le pratiche XP (integrazione continua, test automatici, refactoring, sviluppo trunk-based) sono ciò che permette a un team di continuare a cambiare il software a basso costo, che è l'intera premessa dell'agilità, quindi non sono extra opzionali da scambiare quando si avvicina una data. Portate evidenza: seguite se i tempi di consegna si accorciano o si allungano, se i tassi di difetti salgono e se il team sta lavorando in silenzio più ore per rispettare ogni sprint. La risposta dovrebbe rendere non negoziabili eccellenza tecnica e ritmo umano, perché la velocità comprata sacrificando la maestria crolla in poche iterazioni. Misurate flusso ed esiti, mai la velocità come obiettivo, perché nel momento in cui fate di un segnale di capacità un obiettivo di produttività diventa una bugia.

4. **Prima di ricorrere a un pesante quadro di scalatura, avete provato a ridurre le dipendenze tra team che creano fin dall'inizio il bisogno di coordinarsi?** Questo conta di più per una grande organizzazione, perché il riflesso quando molti team devono rilasciare insieme è comprare un quadro come SAFe, LeSS o Scrum@Scale e il pesante macchinario di scalatura spesso reintroduce di contrabbando il comando e controllo e l'onere di pianificazione che l'Agile esiste per rimuovere. La considerazione contraria è reale: parte del coordinamento è davvero richiesto e descalare in team indipendenti e allineati al flusso richiede basso accoppiamento, chiara proprietà e una piattaforma abbastanza matura da lasciare i team servirsi da soli, che potreste non avere ancora. Portate evidenza alla discussione: mappate le dipendenze effettive che costringono i team ad aspettarsi a vicenda e chiedetevi quante sopravvivrebbero a una deliberata riprogettazione dei confini dei team e della proprietà dei servizi. Nei programmi aziendali e governativi, dove un organigramma di decine di team è comune, la domanda onesta è se state aggiungendo struttura di coordinamento per compensare un'architettura e un disegno dei team che potreste invece semplificare, così da aver bisogno di meno coordinamento affatto.

5. **I vostri team hanno un contatto genuino e ripetuto con i cittadini o i clienti per cui costruiscono, o il riscontro arriva filtrato da intermediari?** La collaborazione con il cliente è uno dei quattro valori del Manifesto e le iterazioni prive di vero contatto con gli utenti ottimizzano in silenzio la cosa sbagliata, che è il fallimento più costoso che l'Agile dovrebbe prevenire. La tensione è che l'accesso diretto è difficile da organizzare su larga scala ed è spesso ostacolato proprio dalle regole di appalto, privacy e sicurezza che le organizzazioni grandi e pubbliche devono rispettare, quindi la strada facile è sostituire un intermediario: un analista di business, un comitato di stakeholder o la presentazione di ricerca del trimestre scorso. Portate evidenza: per i vostri ultimi incrementi, contate quanti sono stati convalidati con un utente vero che usava davvero il software e quanti poggiavano sull'opinione di qualcuno su ciò che gli utenti vogliono. Per un servizio governativo, aggiungete se i vostri test di usabilità hanno raggiunto le persone più colpite, compresi gli utenti di tecnologie assistive e chi ha poca fiducia digitale, perché un servizio pubblico che funziona solo per la maggioranza sicura di sé ha mancato il proprio obbligo di responsabilità anche se ogni cerimonia è girata in orario.

6. **I vostri team sono finanziati e governati attorno a esiti e cadenza, o attorno a un ambito fisso che impone in silenzio la cascata dietro le cerimonie?** Questa è la differenza tra vera agilità e falso agile ed è decisa sopra il team, in come il denaro viene rilasciato e come si riporta il successo, non nel fatto che gli stand-up avvengano. La spinta contraria è che le funzioni di finanza, portafoglio e supervisione sono costruite per approvare un ambito fisso rispetto a un budget fisso anni in anticipo e chiedere loro di finanziare un esito con ambito flessibile sembra una perdita di controllo a cui resisteranno. Portate evidenza: ricostruite come è stata finanziata un'iniziativa attuale e su che cosa riporta e controllate se i team sono misurati su esiti consegnati e flusso o su punti storia e aderenza a un ambito firmato molto tempo fa. Nei contesti aziendali e governativi, collegatelo direttamente al guscio di finanziamento e conformità (capitolo 10.6): se il denaro è impegnato su un go-live lontano e tutto o niente, i team non possono essere adattivi per quanto fedelmente eseguano i rituali e la correzione appartiene al modello di governance anziché ai team di consegna.

## Lente settoriale

**Startup.** Vivi i valori e salta il dibattito sul quadro. Rilascia ogni settimana una fetta funzionante a utenti veri, stai abbastanza vicino a fondatori e primi clienti da ricevere riscontro ogni giorno e accogli un cambio di direzione nel momento in cui l'evidenza dice che la scommessa attuale è sbagliata. La tua risorsa più scarsa è l'attenzione ingegneristica, quindi proteggi l'eccellenza tecnica (integrazione continua, test automatici, sviluppo trunk-based) anche sotto pressione di lancio, perché quella disciplina è ciò che ti tiene in grado di cambiare rotta a basso costo la settimana prossima.

**Piccola impresa.** Senza un coach agile e con un budget stretto, tratta l'Agile come una manciata di abitudini anziché un programma di trasformazione da dotare di personale: un breve ciclo settimanale, una bacheca visibile con limiti di lavoro in corso e un miglioramento concreto ogni settimana che porti davvero a termine. Appoggiati al Kanban, che richiede poca cerimonia e si adatta al lavoro guidato dalle interruzioni e adotta le pratiche incorporate negli strumenti che già compri anziché montare un processo pesante. Giudica lo sforzo da se rilasci software utile ai clienti più spesso, non da quanto imiti da vicino lo Scrum.

**Grande impresa.** Il problema è coordinare molti team senza reintrodurre comando e controllo. Privilegia il descalare, cioè ridurre le dipendenze tra team attraverso un disegno dei team allineato al flusso e una solida piattaforma, prima di adottare un pesante quadro di scalatura. Finanzia e governa attorno a esiti (OKR) e cadenza anziché ambito annuale fisso e punti storia, rendi non negoziabili in tutti i team le pratiche ingegneristiche in stile XP e gestisci la consegna come un portafoglio con metriche di flusso e misure di esito così che i gruppi migliorino sull'evidenza anziché sul rituale.

**Ente pubblico.** Regole di appalto, trasparenza e responsabilità pubblica plasmano ogni scelta. Struttura contratti modulari e basati sugli esiti con incrementi più brevi anziché un solo megacontratto a ambito fisso, poiché gli appalti agili sono dove l'agilità del settore pubblico più spesso riesce o fallisce. Costruisci audit, accessibilità e sicurezza in ogni incremento attraverso l'automazione così che la supervisione sia soddisfatta dall'atto di costruire, pubblica i progressi e l'evidenza di valore pubblico agli organi di controllo e lotta per un genuino accesso ai cittadini (compresi gli utenti di tecnologie assistive) a ogni iterazione, perché è il vincolo che più spesso viene negoziato via.

## Esempi

**Startup.** Una startup di cinque persone salta il dibattito sulle cerimonie e vive direttamente i valori Agile. Rilascia ogni settimana una fetta funzionante a utenti veri, sta abbastanza vicina a fondatori e primi clienti da ricevere riscontro ogni giorno e accoglie un cambio di direzione la settimana successiva quando l'evidenza dice che la scommessa attuale è sbagliata. Il team rifiuta di scambiare l'eccellenza tecnica con la velocità, quindi integrazione continua, test automatici e sviluppo trunk-based sono non negoziabili anche sotto pressione di lancio e ogni retrospettiva del venerdì produce un cambiamento concreto che il team porta davvero a termine prima della successiva. Non segue mai la velocità come obiettivo, misurando invece se il lavoro rilasciato ha mosso l'attivazione e se i tempi di consegna si accorciano.

**Grande impresa.** La trasformazione di un'azienda di telecomunicazioni con 60 team inizialmente "fa Scrum" ma non vede miglioramenti. I team ricevono ancora un ambito annuale fisso e riportano sulla velocità. Un azzeramento rifocalizza sui principi: OKR trimestrali sostituiscono i mandati di funzionalità, i team sono riorganizzati per ridurre le dipendenze tra team (descalare) e le pratiche XP (CI, TDD, sviluppo trunk-based) sono rese non negoziabili. I tempi di consegna calano, i difetti scendono e, cosa cruciale, l'attività comincia a misurare gli esiti anziché i punti storia, collegando la consegna Agile alla pipeline di scoperta (capitolo 11.1).

**Ente pubblico.** Un team di servizi digitali ricostruisce una domanda di prestazioni rivolta ai cittadini usando l'Agile dentro un guscio di governance ibrido: incrementi di due settimane che consegnano software funzionante e testato con utenti; accessibilità e sicurezza incorporate in ogni incremento; e appalti modulari che sostituiscono un singolo contratto a prezzo fisso. Veri test di usabilità con i cittadini (compresi utenti di tecnologie assistive) a ogni iterazione colgono problemi che il vecchio processo a cascata avrebbe rilasciato. Il programma consegna presto un servizio utilizzabile e mostra un valore pubblico misurabile agli organi di controllo. È lo schema dietro i moderni successi del settore pubblico e l'antidoto ai passati fallimenti big-bang.

## Business case: motivazioni, ROI e TCO

Il ritorno dell'Agile viene da **riduzione del rischio e realizzazione del valore più rapida**. Consegnando software funzionante presto e spesso, i team trasformano di continuo l'incertezza in evidenza, cogliendo i fallimenti di cosa-sbagliata e non-funzionerà finché sono economici, anziché a un go-live lontano e costoso. La ricerca dietro la moderna consegna (i risultati DORA, [DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment), nel capitolo 11.2) mostra che le pratiche che l'Agile promuove (piccoli lotti, rilasci frequenti, riscontro rapido, eccellenza tecnica) si correlano con una consegna migliore *e* stabilità *e* prestazioni organizzative. Anche i primi incrementi cominciano prima a restituire valore, migliorando tempi e dimensione complessiva del ROI rispetto a un rilascio big-bang che non restituisce nulla fino alla fine.

Sul **[costo totale di proprietà](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**, l'Agile abbassa il costo del cambiamento lungo la vita di un sistema, a patto che la disciplina ingegneristica sia reale. Il suo rischio dominante è il *falso agile*: cerimonia senza principio né maestria, che aggiunge onere di riunioni senza consegnare alcun beneficio e può essere peggio di una cascata onesta. Quindi il business case è condizionato. Il ROI è alto quando adotti l'Agile come mentalità più ingegneria e circa zero (o negativo) quando lo adotti come rituale. Presenta il caso alla leadership impostando l'Agile come riduzione continua del rischio e misura degli esiti, non come "andare più in fretta" e insistendo che l'investimento includa le pratiche tecniche, non solo nuove riunioni.

## Antipattern e insidie

- **Agile falso / culto del cargo:** cerimonie eseguite mentre decisioni, finanziamento e mentalità restano a cascata.
- **Velocità come produttività:** trasformare una stima di capacità in un obiettivo, il che la corrompe ([legge di Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law)).
- **Dark scrum:** sprintare senza eccellenza tecnica verso codice non mantenibile e pieno di difetti.
- **Retrospettive senza cambiamento:** riflessione che non produce azioni completate.
- **Ambito fisso *e* data *e* costo:** chiamarlo agile mentre la qualità assorbe in silenzio la pressione.
- **Cliente assente:** nessun riscontro vero degli utenti, così le iterazioni ottimizzano la cosa sbagliata.
- **Culto del quadro:** "lo dice SAFe/Scrum" che prevale su principi e giudizio del team.
- **Scalare prima di descalare:** aggiungere pesanti quadri di coordinamento anziché ridurre le dipendenze.

## Modello di maturità

- **Livello 1, Avvio.** Consegna a cascata o ad hoc; rilasci big-bang; il lavoro è reattivo e pesante di piani, senza riscontro iterativo né un senso condiviso del perché l'Agile potrebbe aiutare.
- **Livello 2, Sviluppo.** Alcuni team adottano cerimonie Agile (stand-up, sprint, retrospettive), ma la pratica è incoerente nell'organizzazione: mentalità e disciplina ingegneristica restano indietro rispetto ai rituali, la velocità è trattata come produzione e l'ambito è ancora fissato in anticipo.
- **Livello 3, Standardizzazione.** Valori e principi guidano genuinamente il lavoro in tutta l'organizzazione, documentati e attesi da ogni team: l'eccellenza tecnica in stile XP (CI, test automatici, refactoring, sviluppo trunk-based) è pratica standard, i team si auto-organizzano, i clienti sono coinvolti a ogni iterazione e le retrospettive producono cambiamento concreto e completato.
- **Livello 4, Gestione.** La consegna è misurata e controllata rispetto a valori di riferimento: i team seguono tempo di consegna, frequenza di distribuzione, tasso di fallimento delle modifiche e tasso di fuga dei difetti (le metriche di flusso e stabilità in stile DORA), insieme a misure di esito legate ai risultati chiave e confrontano ciascuna con un valore di riferimento noto. Le azioni delle retrospettive sono seguite fino al completamento, i segnali di ritmo sostenibile come straordinari ed esaurimento sono monitorati e la velocità non è mai usata come obiettivo di produttività. Le decisioni di procedere o meno poggiano su questa evidenza anziché sull'opinione.
- **Livello 5, Orchestrazione.** La consegna adattiva è integrata con la pianificazione di business e di rischio nell'organizzazione: gli esiti (OKR) guidano finanziamento e cadenza, un disegno dei team a bassa dipendenza (descalare) minimizza l'onere di coordinamento e la governance ibrida soddisfa la supervisione senza rallentare la consegna. Il miglioramento continuo è culturale anziché cerimoniale e l'organizzazione ridefinisce, riorganizza i team e riequilibra di routine il proprio portafoglio man mano che si spostano evidenza e quadro di rischio.

## Spunti di discussione

1. Valutate il vostro team rispetto ai dodici principi Agile: dove siete agili nella cerimonia ma non nella sostanza?
2. La velocità è usata nel vostro team come previsione o come obiettivo, e che cosa ha fatto al comportamento?
3. Quali pratiche tecniche XP mancano, e come si manifesta la loro assenza in difetti o cambiamenti lenti?
4. Prima di adottare un quadro di scalatura, potreste ridurre invece le dipendenze tra team?
5. Nel vostro contesto, che cosa blocca specificamente il vero accesso agli utenti a ogni iterazione, e come potreste rimuoverlo?
6. Qual è stato l'ultimo cambiamento concreto che una retrospettiva ha davvero prodotto?

## Punti chiave

- L'Agile è una **mentalità di valori e principi**, non un insieme di cerimonie; i quadri sono punti di partenza, non l'obiettivo.
- Consegna **software funzionante di frequente**, accogli il cambiamento e autorizza **team auto-organizzati**.
- **L'eccellenza tecnica (pratiche XP) non è negoziabile.** L'agilità senza di essa diventa un veloce decadimento.
- **Scala con cura; preferisci il descalare.** Riduci le dipendenze prima di aggiungere quadri di coordinamento.
- In impresa e governo, combina **consegna adattiva con governance ibrida e appalti agili** e lotta per un vero accesso agli utenti.
- Il ROI è **riduzione continua del rischio e valore più precoce**, ma solo quando l'Agile è reale, non rituale. Vedi i capitoli 1.4, 11.1, 11.2, 10.6 e 11.3.

## Riferimenti e letture di approfondimento

- Kent Beck et al., *Manifesto for Agile Software Development* e i suoi dodici principi (agilemanifesto.org, 2001).
- Ken Schwaber e Jeff Sutherland, *The Scrum Guide*.
- Kent Beck, *Extreme Programming Explained: Embrace Change*.
- David J. Anderson, *Kanban: Successful Evolutionary Change for Your Technology Business*.
- Mike Cohn, *User Stories Applied* e *Succeeding with Agile*.
- Jeff Patton, *User Story Mapping*.
- Stephen Denning, *The Age of Agile*.
- Matthew Skelton e Manuel Pais, *Team Topologies* (disegno dei team e descalare).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (evidenza per le pratiche agile/DevOps).
- U.S. Digital Service, *Digital Services Playbook*; UK Government, *Government Service Standard*.
