# 1.2 Topologie dei team e progettazione organizzativa

## Panoramica e motivazioni

Il modo in cui dividi le persone in team determina quale software puoi costruire e con quale rapidità. Non è una metafora. È una conseguenza quasi meccanica nota come [legge di Conway](https://en.wikipedia.org/wiki/Conway%27s_law): le organizzazioni progettano sistemi che rispecchiano le proprie strutture di comunicazione. Se tre team costruiscono un [compilatore](https://en.wikipedia.org/wiki/Compiler), ottieni un compilatore a tre passate. Se la logica dei pagamenti è divisa tra un team frontend, un team backend e un team database, ogni modifica ai pagamenti richiede un coordinamento a tre. Per una piccola organizzazione è gestibile. Per una grande, la forma dell'organigramma diventa il vincolo dominante su ingegneria, architettura, velocità di consegna e qualità. Progettare la struttura dei team è quindi un'attività ingegneristica di prim'ordine, non un ripensamento delle risorse umane.

Le topologie dei team ti offrono un vocabolario deliberato per questa progettazione. Invece di lasciare che la struttura si accumuli per caso attraverso riorganizzazioni e assunzioni, le organizzazioni mature scelgono di proposito tipi di team e modalità di interazione, e le rivedono man mano che il sistema e il business evolvono. L'obiettivo è mantenere basso il [carico cognitivo](https://en.wikipedia.org/wiki/Cognitive_load) di ogni team, cioè la quantità complessiva che un team deve tenere in testa per essere efficace, così che i team possano possedere il proprio dominio da un capo all'altro e consegnare un flusso costante di valore senza dover aspettare continuamente gli altri.

Per le imprese e gli enti pubblici questa disciplina è decisiva. Le grandi organizzazioni tendono naturalmente a espandersi in gerarchie profonde, servizi condivisi con lunghe code e catene di passaggi che trasformano una modifica di due giorni in un progetto di due mesi. Gli enti pubblici aggiungono confini d'appalto, team di collaboratori esterni e [separazioni dei compiti](https://en.wikipedia.org/wiki/Separation_of_duties) obbligatorie che frammentano ulteriormente la responsabilità. Una progettazione esplicita della topologia è il modo in cui queste organizzazioni riconquistano il flusso: allineare i team ai flussi di valore, costruire piattaforme che riducono il carico cognitivo e scegliere schemi di interazione che rendano le dipendenze visibili e intenzionali anziché nascoste e costanti.

## Principi chiave

- La legge di Conway è inevitabile; progetta i team in modo che corrispondano all'ingegneria del software che vuoi (la "manovra inversa").
- Ottimizza per il carico cognitivo del team, non per la massima utilizzazione dei singoli.
- Preferisci team allineati al flusso, che possiedono da un capo all'altro una porzione di valore.
- Le piattaforme esistono per ridurre il carico cognitivo dei team allineati al flusso, non per fare da guardiani.
- Rendi le interazioni tra team esplicite e poche: collaborazione, X-as-a-service o facilitazione.
- Riduci al minimo le dipendenze; ogni passaggio tra team è una coda e un rischio.
- La struttura dei team è un progetto vivo che deve evolvere con il cambiare del sistema e del business.

## Raccomandazioni

### Usa i quattro tipi fondamentali di team

Le topologie dei team definiscono quattro tipi di team che coprono la maggior parte delle esigenze. I team allineati al flusso sono la scelta predefinita: ciascuno possiede da un capo all'altro un flusso continuo di lavoro per uno specifico prodotto, servizio o percorso utente. I team di piattaforma forniscono prodotti interni (calcolo, rilascio, pipeline di dati, identità) che i team allineati al flusso consumano in autonomia, abbassandone il carico cognitivo. I team abilitanti sono specialisti (test, sicurezza, osservabilità) che affiancano i team allineati al flusso per costruire una capacità, poi si fanno da parte. I team di sottosistema complicato possiedono componenti che richiedono una competenza specialistica profonda (un motore di prezzi, un [codec video](https://en.wikipedia.org/wiki/Video_codec), un modulo crittografico), dove non ha senso che ogni team abbia quella conoscenza. La maggior parte dei tuoi team dovrebbe essere allineata al flusso; gli altri tre tipi esistono per sostenerli.

### Applica la manovra inversa di Conway

Poiché il software rispecchia la struttura della tua organizzazione, plasma i tuoi team in modo da produrre il software che vuoi. Vuoi servizi debolmente accoppiati con confini chiari? Crea team debolmente accoppiati con chiari confini di responsabilità. Vuoi una capacità di pagamento che rilascia secondo i propri tempi? Costituisci un team dei pagamenti che la possieda dal frontend al backend. Non combattere la legge di Conway con un coordinamento eroico. Ridisegna i confini tra i team in modo che l'architettura che desideri diventi la strada di minor resistenza.

### Gestisci il carico cognitivo in modo esplicito

Un team può padroneggiare solo una certa quantità di cose. Il carico cognitivo comprende la complessità del dominio, le tecnologie, il peso operativo e l'ampiezza degli stakeholder. Quando un team possiede troppi servizi non correlati, qualità e velocità crollano entrambe. Delimita quindi le responsabilità di ogni team a un dominio che può davvero padroneggiare, e usa piattaforme e team abilitanti per togliergli di dosso la complessità indifferenziata. Mantieni i team intorno a cinque-nove persone: abbastanza piccoli da comunicare con facilità e da poter essere sfamati, per così dire, con un paio di pizze.

### Scegli le modalità di interazione in modo deliberato

Limita le interazioni tra team a tre modalità. La collaborazione è un lavoro stretto e a larga banda tra due team per un periodo definito; è potente per la scoperta, ma costosa, quindi mantienila temporanea. X-as-a-service è un rapporto pulito tra fornitore e consumatore con un'interfaccia ben definita, ideale per il consumo di piattaforma su larga scala. La facilitazione è un team che aiuta un altro a imparare, ed è ciò che fanno i team abilitanti. Dai un nome alla modalità di ogni rapporto importante tra team, e leggi una collaborazione di lunga durata tra gli stessi due team come un segnale che il loro confine è nel posto sbagliato.

### Scegli un modello operativo per le funzioni trasversali

Sicurezza, dati, design e discipline simili possono essere organizzati in tre modi: centralizzato (un team ne risponde per tutti), federato (specialisti inseriti a tempo parziale, che si coordinano tramite una gilda) o integrato (uno specialista dedicato dentro ogni team allineato al flusso). Il modello centralizzato dà coerenza e profondità, ma diventa un collo di bottiglia. Quello integrato dà velocità e contesto, ma rischia incoerenza e duplicazione. Quello federato (spesso un modello hub-and-spoke o di [comunità di pratica](https://en.wikipedia.org/wiki/Community_of_practice)) sta nel mezzo. Scegli per ogni funzione e per ogni scala. La maggior parte delle grandi organizzazioni approda al federato per queste discipline, con un piccolo nucleo centrale che definisce gli standard.

### Investi nell'inner source

L'[inner source](https://en.wikipedia.org/wiki/Inner_source) porta all'interno dell'organizzazione gli schemi di collaborazione dell'[open source](https://en.wikipedia.org/wiki/Open-source_software): repository interni condivisi, linee guida di contribuzione pubblicate, [revisione del codice](https://en.wikipedia.org/wiki/Code_review) oltre i confini dei team e manutentori chiari. Quando un team ha bisogno di una modifica al componente di un altro team, può contribuire direttamente con la modifica invece di aprire un ticket e aspettare in coda. Questo allenta le dipendenze tra team senza dissolvere la responsabilità, e diffonde naturalmente conoscenza e standard in una grande popolazione ingegneristica.

## Compromessi: vantaggi e svantaggi

| Modello per le funzioni trasversali | Vantaggi | Svantaggi |
| --- | --- | --- |
| Centralizzato (un team per tutti) | Coerenza, competenza profonda, standard chiari | Collo di bottiglia, code, perdita del contesto di prodotto |
| Federato (hub-and-spoke, gilde) | Bilancia coerenza e velocità; condivide conoscenza | Richiede disciplina di coordinamento; la responsabilità può sfumare |
| Integrato (uno specialista per team) | Veloce, ricco di contesto, forte responsabilità | Duplicazione, incoerenza, difficile da dotare di personale su larga scala |

| Tipo di team | Ideale per | Rischio se usato in eccesso |
| --- | --- | --- |
| Allineato al flusso | La maggior parte della consegna di prodotti e servizi | Nessuno; deve dominare |
| Di piattaforma | Ridurre il carico cognitivo condiviso | Diventa un guardiano chiuso nella torre d'avorio |
| Abilitante | Diffondere temporaneamente una capacità | Si trasforma in una dipendenza permanente |
| Di sottosistema complicato | Domini specialistici davvero profondi | Usato come scusa per accaparrarsi lavoro ordinario |

Il compromesso ricorrente è tra autonomia e coerenza. I team completamente autonomi si muovono in fretta, ma divergono negli standard, negli strumenti e nella postura di sicurezza. Un controllo completamente centralizzato mantiene la coerenza, ma strangola il flusso. Una buona progettazione della topologia trova la linea di giuntura: autonomia per la consegna allineata al flusso, più standard centrali sottili e piattaforme a strada asfaltata (strumenti predefiniti ben supportati che rendono facile la scelta conforme) per le cose che devono davvero essere coerenti.

## Domande da discutere con il tuo team

1. **Quali segnali concreti ti diranno che il carico cognitivo di un team è troppo alto, prima che la qualità crolli?** "Delimita ogni team a un dominio che può padroneggiare" è facile da dire e difficile da mettere in pratica senza prove, perché il carico cognitivo resta invisibile finché consegne e affidabilità non peggiorano. Osserva sintomi misurabili: il numero di servizi o repository non correlati che un team possiede, quanto dura l'inserimento, su quanti domini un singolo ingegnere deve cambiare contesto in una settimana e l'aumento degli incidenti negli angoli di competenza del team. Per una grande organizzazione questo conta perché i team sovraccarichi diventano in silenzio colli di bottiglia che nessun organigramma prevede. Porta questi numeri alla discussione, insieme alla percezione del team stesso di ciò che può e non può tenere in testa. Se i segnali dicono sovraccarico, la mossa è scaricare il lavoro indifferenziato su una piattaforma o su un team abilitante, non pretendere altri eroismi.

2. **Una riorganizzazione vale davvero il disagio, qui, o stai alimentando una dipendenza da riorganizzazioni?** Ridisegnare i confini per applicare la manovra inversa di Conway è potente, e ogni riorganizzazione distrugge anche la stabilità di cui i team hanno bisogno per amalgamarsi e azzera la conoscenza del dominio conquistata a fatica. Le considerazioni in gioco sono la tassa di coordinamento continua della struttura attuale contro il costo una tantum e il colpo al morale del cambiarla. Nei contesti aziendali e governativi, confini d'appalto, team di collaboratori esterni e separazioni dei compiti obbligatorie rendono le riorganizzazioni più lente e costose, quindi l'asticella dovrebbe essere più alta. Porta prove del ritardo causato dalle dipendenze: quante iniziative sono bloccate in attesa di un altro team, e per quanto tempo. Riorganizza quando quell'attesa è strutturale e grande, e resisti al rimescolamento quando il dolore è temporaneo o sarebbe più economico risolverlo con contributi inner source e interfacce più chiare.

3. **Per sicurezza, dati e design, quale evento ti farà passare tra modello integrato, federato e centralizzato?** La raccomandazione del capitolo è scegliere per funzione e per scala, e la disciplina più difficile è decidere in anticipo quale crescita o rischio ti farà rivedere quella scelta. Un modello adatto a cinquanta ingegneri può diventare un collo di bottiglia o un disastro di coerenza a cinquecento, e le imprese e gli enti pubblici in particolare devono nominare gli standard che un piccolo nucleo centrale terrà sempre. Porta i tempi di coda attuali e i divari di coerenza per ciascuna funzione: un team centrale di sicurezza con code di revisione di settimane è un segnale per federare, mentre specialisti integrati che producono modelli di dati incompatibili sono un segnale per aggiungere un nucleo centrale di standard. Decidi ora il fattore scatenante, come una soglia di lunghezza della coda o un rilievo di audit, in modo che il cambiamento diventi un'evoluzione pianificata anziché una reazione di crisi. La risposta determina dove investire in strade asfaltate e referenti rispetto a un hub centrale.

4. **Come saprai se il tuo team di piattaforma sta davvero abbassando il carico cognitivo o sta diventando in silenzio un guardiano?** Una piattaforma esiste per rendere facile la scelta conforme e affidabile attraverso il self-service, e lo stesso team può scivolare nell'imporre strumenti, rivedere a mano ogni richiesta e aggiungere l'attrito che doveva eliminare. Per una grande organizzazione questa distinzione decide se l'investimento nella piattaforma si ripaga o si trasforma in un collo di bottiglia centrale dietro cui ogni team allineato al flusso fa la coda. Le considerazioni in gioco sono coerenza e controllo da un lato, autonomia dei consumatori e flusso dall'altro. Porta prove che un consumatore riconoscerebbe: quanto tempo impiega un team allineato al flusso ad avere in autonomia un nuovo ambiente o una pipeline senza aprire un ticket, il rapporto tra azioni in self-service e azioni mediate da persone e l'adozione della piattaforma misurata in team che la scelgono anziché team che vi sono forzati. Nei contesti aziendali e governativi, pretendi che la piattaforma generi automaticamente evidenze di audit e conformità anziché tramite passaggi manuali, perché una piattaforma che rispetta le regole di separazione dei compiti inserendo un revisore umano ha ricreato il collo di bottiglia che era stata finanziata per eliminare.

5. **Quali dei tuoi rapporti tra team si sono assestati in una collaborazione permanente, e che cosa trasformerebbe ciascuno in un'interfaccia di servizio pulita o in un confine ridisegnato?** La modalità di collaborazione è pensata per essere intensa e temporanea, e un affiancamento che non finisce mai è di solito un segnale che la responsabilità è nel posto sbagliato o che l'interfaccia tra due team non è mai stata resa esplicita. Su larga scala questo conta perché la collaborazione stabile e senza nome è dove si nasconde il costo di coordinamento: non compare in nessun organigramma, eppure grava su ogni modifica che i due team toccano. Le considerazioni in gioco sono il valore di scoperta dello stare vicini contro il flusso che si guadagna trasformando il rapporto in un contratto X-as-a-service con un'interfaccia definita, o fondendo la responsabilità in un unico team. Porta l'elenco delle coppie di team che collaborano di continuo da più di un trimestre, le modifiche che negli ultimi mesi hanno richiesto entrambi i team e se un'interfaccia stabile tra loro potrebbe essere messa per iscritto. Per i contesti aziendali e governativi, dove confini tra collaboratori esterni e lotti d'appalto possono congelare un passaggio per anni, indica quali rapporti puoi convertire con un'interfaccia e contributi inner source e quali sono fissati per contratto e vanno gestiti come dipendenze esplicite.

6. **Quando un team abilitante aiuta un altro team a costruire una capacità, come saprai che ha avuto successo e può farsi da parte anziché diventare una dipendenza permanente?** I team abilitanti devono affiancare un team allineato al flusso finché non padroneggia test, sicurezza o osservabilità, e poi passare oltre; senza una condizione di uscita esplicita, il rapporto di affiancamento si indurisce in un servizio stabile che il team allineato al flusso non assorbe mai davvero. Per una grande organizzazione è la differenza tra diffondere una capacità su decine di team e creare un nuovo collo di bottiglia condiviso che scala peggio ogni anno. Le considerazioni in gioco sono la profondità e la coerenza che offre un team specialistico contro l'autonomia e la responsabilità da un capo all'altro che stai cercando di costruire nei team allineati al flusso. Porta prove del trasferimento di capacità: se il team ricevente ora svolge il lavoro senza la presenza del team abilitante, a quanti team è assegnato contemporaneamente un gruppo abilitante di dimensioni fisse e per quanto tempo ogni impegno è andato oltre il passaggio di consegne previsto. Nei contesti aziendali e governativi, dove una competenza specialistica scarsa può stare dietro un unico team centrale o un unico contratto, decidi in anticipo come finanzi il trasferimento di capacità e i referenti, così che la competenza si diffonda nei team di consegna anziché restare chiusa dietro una coda che ogni audit e ogni rilascio devono attendere.

## Lente settoriale

**Startup.** Con una manciata di ingegneri e poca liquidità, la giusta topologia è un unico team allineato al flusso che possiede l'intero prodotto, e la disciplina sta nel rifiutarsi di creare compartimenti stagni prima che servano. Resisti alla tentazione di assumere un singolo "DevOps" o "QA" che diventa un cancello; integra quelle competenze nell'unico team come capacità incorporata. Fai lavorare la legge di Conway a tuo favore mantenendo piatta l'organizzazione, così che l'architettura resti semplice e modificabile quanto il team.

**Piccola impresa.** Non avrai un team di piattaforma o abilitante dedicato, quindi compra la piattaforma: usa servizi cloud gestiti, pipeline ospitate e strumenti di sicurezza già pronti per togliere il carico cognitivo indifferenziato dal tuo team o dai tuoi due team. Imposta le questioni trasversali come sicurezza e dati come cose che configuri e consumi, non come una funzione che costruisci. Riserva la responsabilità su misura al solo sottosistema complicato che ti differenzia davvero, e lascia che i fornitori portino il resto.

**Grande impresa.** Su larga scala il problema è il costo di coordinamento tra molti team, quindi rendi la topologia una progettazione esplicita e governata: una tassonomia condivisa dei quattro tipi di team, modalità di interazione con un nome, una piattaforma a strada asfaltata e l'inner source per ridurre le code tra team. Segui il ritardo dovuto alle dipendenze e il carico cognitivo dei team come metriche di portafoglio, e conduci le riorganizzazioni come evoluzioni deliberate con un'asticella alta anziché come un riflesso annuale. Un sottile nucleo centrale detiene gli standard che devono essere coerenti, mentre i team allineati al flusso mantengono l'autonomia sulla consegna.

**Ente pubblico.** Regole sugli appalti, confini tra collaboratori esterni e separazioni dei compiti obbligatorie frammentano la responsabilità, quindi progetta la topologia per rispettare questi vincoli tramite strumenti e interfacce chiare anziché passaggi umani. Privilegia modelli federati con un piccolo nucleo di standard e una piattaforma che genera automaticamente evidenze di audit e conformità, così che la separazione dei compiti sia imposta dalle pipeline anziché dalle code di revisione. Documenta apertamente i confini tra i team, le modalità di interazione e il modello operativo, in modo che la struttura sia trasparente per auditor, organi di vigilanza e per il pubblico che la finanzia.

## Esempi

**Startup.** Una startup di dieci persone ha un unico team allineato al flusso che possiede l'intero prodotto da un capo all'altro, ed è esattamente giusto alla sua scala: niente passaggi, nessuna tassa di coordinamento, tutti con lo stesso contesto. I guai iniziano quando assumono un "DevOps" dedicato e un "QA" separato e ricreano per sbaglio compartimenti funzionali, così che ogni rilascio ora aspetta due persone. Correggono la rotta trattando quelle assunzioni come una capacità incorporata di piattaforma e test dentro l'unico team, anziché come cancelli che il lavoro deve attraversare. A questa dimensione, la topologia più economica è quella che tiene tutti in un unico flusso.

**Grande impresa.** Il checkout di un grande rivenditore era lento da modificare perché la logica di frontend, backend ed evasione ordini era divisa tra tre team organizzati per funzione, costringendo ogni modifica a passare per tre backlog. Applicando la manovra inversa di Conway, si sono riorganizzati in team allineati al flusso attorno ai percorsi dei clienti ("navigazione", "carrello e checkout", "post-acquisto"), ciascuno proprietario della propria porzione dal frontend al backend, sostenuti da un team di piattaforma che offriva rilascio e osservabilità come servizio. Le modifiche al checkout che prima richiedevano un trimestre hanno iniziato a uscire in pochi giorni, perché il coordinamento che prima attraversava i team ora avveniva dentro uno solo.

**Ente pubblico.** Un'agenzia fiscale governativa gestiva un team centrale di sicurezza che rivedeva ogni rilascio, creando una coda di settimane che ritardava le correzioni critiche. È passata a un modello federato: una piccola funzione centrale di sicurezza definiva gli standard e offriva una "strada asfaltata" di pipeline pre-approvate e scansionate automaticamente, mentre referenti per la sicurezza, inseriti a tempo parziale in ogni team di consegna, gestivano le decisioni quotidiane. La piattaforma generava automaticamente le evidenze di conformità. I requisiti obbligatori di separazione dei compiti restavano soddisfatti, ma tramite strumenti e interfacce chiare anziché un collo di bottiglia umano, il che ha ridotto drasticamente il tempo di consegna dei rilasci migliorando al tempo stesso la prontezza all'audit.

## Business case: motivazioni, ROI e TCO

La scarsa progettazione dei team si paga in costi generali di coordinamento, e quei costi crescono più che linearmente con il numero di team che devono sincronizzarsi per una modifica tipica. Ogni passaggio è una coda con tempo di attesa, un trasferimento di contesto che perde informazioni e una nuova occasione di fraintendimento. Quando una modifica di routine richiede che tre team allineino le proprie roadmap, il costo reale non è la somma del loro lavoro; è il costo molto più grande di pianificazione, attesa e rifacimento. Ridisegna i confini in modo che la maggior parte delle modifiche stia dentro la responsabilità di un solo team, e quei costi generali semplicemente spariscono.

Il costo di adozione è reale. Le riorganizzazioni sono dirompenti, e costruire piattaforme e pratiche inner source richiede un investimento iniziale prima che arrivi il ritorno. Ma il costo del non adottare si accumula. Le organizzazioni che lasciano accumulare la struttura per caso ammassano catene di passaggi, team condivisi a collo di bottiglia con code di un trimestre e architetture fossilizzate dall'organigramma. Per sostenere il caso con la leadership, misura il ritardo dovuto alle dipendenze: quante iniziative attive sono bloccate in attesa di un altro team, e per quanto tempo. Gli investimenti in piattaforma e topologia di solito si ripagano trasformando quell'attesa in flusso, il che si vede come tempi di consegna più brevi e throughput più alto senza aggiungere personale.

## Antipattern e insidie

- Ignorare la legge di Conway: progettare un'architettura che la struttura organizzativa non può realizzare.
- Compartimenti funzionali: team separati di frontend, backend, QA e operations che devono coordinarsi per qualsiasi modifica.
- Collo di bottiglia dei servizi condivisi: un team centrale dietro cui ogni progetto deve fare la coda.
- Piattaforma come guardiano: un team di piattaforma che impone anziché servire, aggiungendo attrito invece di rimuoverlo.
- Sovraccarico cognitivo: team che possiedono sistemi estesi e non correlati che non riescono a padroneggiare.
- "Collaborazione" permanente: due team perennemente intrecciati, segno di un confine collocato male.
- Dipendenza da riorganizzazioni: rimescolare di continuo, distruggendo la stabilità di cui i team hanno bisogno per amalgamarsi.

## Modello di maturità

- **Livello 1, Avvio.** I team si formano per caso, per organico o per gerarchia ereditata; nessuno dà un nome ai tipi di team o alle modalità di interazione; compartimenti funzionali e colli di bottiglia dei servizi condivisi sono ovunque e le dipendenze restano nascoste finché non bloccano un rilascio.
- **Livello 2, Sviluppo.** Esistono alcuni team allineati al flusso e compare un primo sforzo di piattaforma o inner source, ma lo schema è applicato in modo disomogeneo: pochi team possiedono la propria porzione da un capo all'altro mentre altri fanno ancora la coda dietro funzioni centrali, e il carico cognitivo è discusso in modo aneddotico anziché gestito.
- **Livello 3, Standardizzazione.** I quattro tipi di team e le tre modalità di interazione sono documentati e usati con deliberazione in tutta l'organizzazione; piattaforme e inner source allentano le dipendenze tra team; si sceglie e si scrive un modello operativo per sicurezza, dati e design, e i nuovi team si formano secondo questi standard anziché per improvvisazione.
- **Livello 4, Gestione.** La topologia è misurata e controllata rispetto a valori di riferimento: i team seguono il carico cognitivo, il ritardo dovuto alle dipendenze (iniziative bloccate in attesa di un altro team e per quanto tempo), i rapporti di self-service della piattaforma e la sua adozione, la durata delle modalità di interazione e metriche di flusso di consegna come tempo di consegna e frequenza dei cambiamenti. Le soglie innescano azioni, per esempio una lunghezza di coda che costringe una funzione a federarsi o una collaborazione stabile che segnala un confine collocato male, così le decisioni poggiano su prove anziché su opinioni.
- **Livello 5, Orchestrazione.** La progettazione dei team è migliorata di continuo e integrata con la pianificazione di architettura, prodotto e rischio; l'organizzazione rimodella i confini man mano che sistema e business evolvono, conclude gli interventi abilitanti una volta trasferita la capacità e riequilibra gli investimenti in piattaforma al variare del carico cognitivo, mantenendo il flusso veloce come proprietà adattiva e stabile anziché come riorganizzazione una tantum.

## Spunti di discussione

- Per una modifica tipica, quanti team devono coordinarsi, e perché?
- Quali dei nostri team portano troppo carico cognitivo, e che cosa potrebbe scaricare una piattaforma?
- Dove stiamo combattendo la legge di Conway invece di ridisegnare i confini?
- I nostri team di piattaforma servono i team allineati al flusso o li tengono sotto controllo come guardiani?
- Sicurezza, dati e design dovrebbero essere centralizzati, federati o integrati per noi in questo momento?
- Quali collaborazioni "temporanee" sono diventate in silenzio dipendenze permanenti?

## Punti chiave

- La struttura organizzativa determina architettura e velocità di consegna; progettala con deliberazione.
- Usa i quattro tipi di team, con quello allineato al flusso come predefinito e gli altri a supporto.
- Applica la manovra inversa di Conway per rendere facile la strada verso l'architettura desiderata.
- Gestisci il carico cognitivo; delimita ogni team a un dominio che può padroneggiare.
- Limita e dai un nome alle modalità di interazione tra team; tratta le dipendenze persistenti come difetti di confine.
- Scegli modelli centralizzati, federati o integrati per le funzioni trasversali in base alla scala, e usa l'InnerSource per ridurre le code.

## Riferimenti e letture di approfondimento

- Matthew Skelton e Manuel Pais, "Team Topologies: Organizing Business and Technology Teams for Fast Flow"
- Melvin Conway, "How Do Committees Invent?" (l'origine della legge di Conway)
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate"
- Will Larson, "An Elegant Puzzle: Systems of Engineering Management"
- Sam Newman, "Building Microservices" (sull'allineamento dei servizi ai team)
- Danese Cooper e Klaas-Jan Stol, "Adopting InnerSource", e gli schemi di InnerSource Commons
- Frederick Brooks, "The Mythical Man-Month" (costo di comunicazione)
