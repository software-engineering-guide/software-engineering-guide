# 6.6 Infrastruttura e operazioni per l'IA

## Panoramica e motivazioni

Infrastruttura e operazioni per l'IA è la disciplina di predisporre, pianificare e gestire i sistemi specializzati di calcolo, archiviazione ed erogazione che i carichi di IA richiedono, facendolo in modo economico, affidabile e osservabile. L'IA moderna è costosa da gestire. Addestrare ed erogare grandi modelli richiede acceleratori scarsi ([GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit) e [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit)), reti ad alta larghezza di banda, archiviazione vettoriale su larga scala per il recupero (indicizzare i dati come vettori numerici così che elementi simili si trovino in fretta) e strati di erogazione regolati per latenza e throughput. Far bene questa infrastruttura è la differenza tra un'IA che scala in modo sostenibile e una che consuma in silenzio un budget consegnando meno del promesso.

Per i grandi team, i problemi centrali sono scala, scarsità e costo. Gli acceleratori sono limitati e cari, quindi pianificazione e utilizzo contano enormemente. Le GPU inattive sono denaro bruciato e un'inferenza raggruppata male moltiplica il costo per richiesta. Le applicazioni ricche di recupero hanno bisogno di [database vettoriali](https://en.wikipedia.org/wiki/Vector_database) che restino veloci man mano che crescono. Le applicazioni di IA generativa hanno bisogno di versionamento dei prompt, pipeline di valutazione e osservabilità (a volte chiamata LLMOps) per operare in sicurezza e migliorare nel tempo. Senza infrastruttura condivisa e disciplina operativa, ogni team combatte le stesse battaglie e i costi si avvitano.

Le organizzazioni governative e regolamentate aggiungono requisiti su sovranità dei dati, sicurezza e spesa prevedibile. Possono aver bisogno di un rilascio on-premises o in cloud sovrano così che dati sensibili e modelli non lascino mai confini controllati. Devono prevedere e giustificare la spesa per l'infrastruttura e soddisfare standard di sicurezza e disponibilità. Le decisioni sull'infrastruttura di IA in questi contesti hanno conseguenze pluriennali, quindi prendile pensando a appalti, sicurezza e uscita.

## Principi chiave

- Tratta il calcolo con acceleratori come una risorsa scarsa e costosa da pianificare e usare, non da accaparrare.
- Ottimizza il costo per unità di lavoro utile, non la capacità grezza.
- Dimensiona modelli e hardware al compito; l'opzione più grande è raramente la più economica.
- Progetta l'erogazione per latenza e throughput con batching e caching come tecniche di prim'ordine.
- Rendi osservabili i sistemi di IA: segui costo, latenza, qualità ed errori di continuo.
- Versiona e valuta prompt e modelli con lo stesso rigore del codice.
- Pianifica la portabilità ed evita il lock-in nelle scelte di infrastruttura ed erogazione.

## Raccomandazioni

### Pianifica e controlla il calcolo con acceleratori

Prevedi separatamente la domanda per addestramento e inferenza, poiché hanno forme diverse. L'addestramento è a raffiche e pianificabile; l'inferenza è continua e sensibile alla latenza. Usa scheduler e quote per condividere le scarse GPU e TPU tra i team, dai priorità ai carichi e spingi in alto l'utilizzo. Misura l'utilizzo e tratta l'inattività cronica come un problema da correggere. Mescola capacità riservata per il carico di base con capacità on-demand o spot per le raffiche per controllare il costo. Considera se acceleratori più economici o più piccoli, o l'inferenza su CPU per modelli leggeri, basterebbero. Scegli tra cloud, on-premises e ibrido in base al costo alla tua scala, alle esigenze di sovranità dei dati e agli schemi di raffica e mantieni un percorso di uscita.

### Costruisci l'infrastruttura di recupero: embedding e database vettoriali

Per le applicazioni con generazione aumentata dal recupero, metti in piedi infrastruttura per generare [embedding](https://en.wikipedia.org/wiki/Word_embedding) (rappresentazioni vettoriali numeriche che collocano elementi simili vicini) e memorizzarli in un database vettoriale che supporti una rapida [ricerca approssimata del vicino più prossimo](https://en.wikipedia.org/wiki/Nearest_neighbor_search) (trovare i vettori più simili senza confrontarli tutti in modo esaustivo) alla tua scala. Pianifica tre cose: costo e latenza della generazione di embedding, freschezza dell'indice man mano che i documenti cambiano e l'onere operativo di mantenere coerenti gli indici. Valuta se un database vettoriale dedicato, un'estensione con capacità vettoriali di un database esistente o un servizio gestito si adatti meglio alla tua scala e tolleranza al lock-in. Monitora latenza e richiamo del recupero, perché la qualità del recupero determina direttamente la qualità dell'applicazione.

### Ottimizza l'erogazione dei modelli: batching, caching e latenza

L'erogazione è dove si decidono costo di inferenza ed esperienza utente. Usa il **batching** per elaborare insieme più richieste e alzare il throughput degli acceleratori, bilanciando dimensione del lotto e latenza. Usa il **caching** con decisione: metti in cache richieste identiche o semanticamente simili, metti in cache gli embedding e sfrutta il caching di prompt o prefisso dove la piattaforma lo supporta per evitare di ricalcolare contesto condiviso. Fissa chiari obiettivi di latenza e misura la latenza di coda, non solo le medie. Instrada le richieste a modelli dimensionati correttamente: un modello piccolo per i casi facili, uno più grande solo quando serve. Scala automaticamente l'erogazione sulla domanda e fai test di carico prima del lancio così da conoscere la tua capacità e la tua curva di costo.

### Pratica l'LLMOps: versionamento dei prompt, pipeline di valutazione e osservabilità

Tratta i prompt come artefatti versionati nel controllo dei sorgenti, con revisione e capacità di ripristino. Costruisci pipeline di valutazione che eseguano automaticamente insiemi di test offline ogni volta che prompt o modelli cambiano, così da cogliere le regressioni prima del rilascio. Strumenta la produzione in modo completo: registra input, output, latenza, uso di token, costo ed errori, con campionamento e salvaguardie di privacy. Segui online i segnali di qualità e il feedback degli utenti. Questa osservabilità ti permette di cogliere il degrado, controllare il costo, debuggare i fallimenti e migliorare i sistemi in sicurezza: la spina dorsale operativa dell'IA generativa in produzione.

### Gestisci il costo senza tregua e in modo osservabile

Attribuisci la spesa per l'IA a team e casi d'uso così che il costo sia visibile e posseduto. Fissa budget e allarmi, monitora il costo per richiesta e per esito e rivedi regolarmente i maggiori fattori di costo. Tira le leve che hai: dimensionamento del modello, caching, batching, sfoltimento di prompt e contesto e scelta del rilascio più economico che soddisfi i requisiti. I costi dell'IA possono scalare con l'uso in modi sorprendenti, quindi l'osservabilità continua del costo è essenziale per evitare sgradite sorprese.

## Compromessi: vantaggi e svantaggi

| Decisione | Opzione A | Opzione B | Compromesso |
|---|---|---|---|
| Luogo del calcolo | Cloud | On-premises | Elasticità e basso costo iniziale contro controllo, sovranità ed economia a regime |
| Capacità | Riservata | On-demand/spot | Costo prevedibile contro flessibilità e rischio di interruzione |
| Dimensione del lotto | Lotti grandi | Lotti piccoli | Throughput e costo contro latenza |
| Dimensione del modello | Modello grande | Modello piccolo | Qualità contro costo e velocità |
| Archivio vettoriale | Database dedicato | Estensione di database esistente | Prestazioni su larga scala contro semplicità e meno sistemi |
| Caching | Aggressivo | Minimo | Costo e latenza più bassi contro freschezza e complessità |

Il compromesso dominante è costo contro latenza e qualità. Batching, caching e modelli più piccoli tagliano il costo ma possono aggiungere latenza o ridurre la qualità. L'equilibrio giusto dipende dalla tolleranza della tua applicazione. On-premises contro cloud scambia controllo ed economia a regime contro elasticità e basso impegno, una decisione fortemente plasmata da esigenze di sovranità dei dati e dalla scala.

## Domande da discutere con il tuo team

1. **Qual è oggi il nostro costo per esito utile, e quale leva lo muoverebbe di più?** La capacità grezza e le medie per richiesta nascondono il numero che conta: quanto costa consegnare una vera unità di valore e come scala con l'uso. Per un grande team, il divario tra un rilascio ottimizzato e uno non ottimizzato è spesso di diverse volte in spesa, quindi questa domanda trasforma una vaga preoccupazione per la bolletta in un elenco ordinato di correzioni. Porta l'attuale attribuzione dei costi per team e caso d'uso, gli andamenti per richiesta e per esito e i maggiori fattori di costo. Discuti le leve in ordine di resa: dimensionamento del modello, caching (compreso il caching di prefisso e semantico), batching e sfoltimento di prompt o contesto. Negli enti pubblici, aggiungi la pressione di prevedere e giustificare la spesa pluriennale. La risposta dovrebbe assegnare a ogni principale fattore di costo un responsabile e una leva, non una scrollata di spalle.

2. **Se il nostro attuale fornitore di inferenza raddoppiasse il prezzo o andasse giù domani, quanto in fretta potremmo cambiare?** Il lock-in silenzioso è facile da costruire e doloroso da lasciare e gli stack di erogazione sono dove si nasconde più a fondo. Per le imprese e soprattutto per gli enti pubblici, la portabilità è un requisito di appalto e di continuità, non un vezzo. Porta la tua architettura: se i modelli stanno dietro un'interfaccia interna, se prompt e suite di valutazione sono portabili e quanto comportamento di erogazione specifico del fornitore dai per scontato. Il segnale da osservare è se qualcuno ha mai eseguito la tua suite di valutazione contro un secondo fornitore o un secondo obiettivo di rilascio. Se cambiare richiedesse mesi e riscrivere percorsi centrali, trattalo come un difetto di progetto da affrontare ora, poiché le opzioni sovrane e on-premises possono diventare obbligatorie con poco preavviso.

3. **Qual è il nostro utilizzo degli acceleratori in questo momento, e quanto stanno bruciando le GPU inattive e l'inferenza non raggruppata?** Gli acceleratori sono scarsi e costosi, quindi l'inattività cronica e l'erogazione per singola richiesta drenano in silenzio budget che potrebbero finanziare più capacità. Per una grande organizzazione che condivide le GPU tra team, questa domanda espone se pianificazione, quote e priorità tengono davvero alto l'utilizzo o se l'hardware accaparrato e sottoutilizzato è la norma. Porta numeri reali di utilizzo, la tua posizione su batching e caching e le tue misure di latenza di coda, non solo le medie, poiché gli utenti sentono la coda lenta. Discuti se la domanda di addestramento e di inferenza è prevista separatamente, date le loro forme diverse, e se un modello più piccolo o l'inferenza su CPU basterebbero per i casi leggeri. La risposta dovrebbe indicare specifica capacità inattiva da recuperare e specifiche richieste da raggruppare o instradare a un modello dimensionato correttamente.

4. **Quando una modifica di prompt o modello viene rilasciata, che cosa impedisce a una regressione silenziosa di qualità o di costo di raggiungere gli utenti?** Uno stack di erogazione può sembrare sano su latenza e uptime mentre le risposte che restituisce peggiorano in silenzio o un nuovo prompt raddoppia l'uso di token per richiesta. Per un grande team in cui molti gruppi modificano prompt e cambiano modelli in modo indipendente, una modifica non filtrata è un incidente di produzione in attesa di accadere e il raggio d'impatto cresce con ogni team sulla piattaforma condivisa. Porta la tua copertura di valutazione: quali prompt e modelli hanno insiemi di test offline, se quegli insiemi girano automaticamente a ogni modifica, quali soglie di qualità e costo filtrano un rilascio e quanto in fretta puoi ripristinare. Discuti se i prompt vivono nel controllo dei sorgenti con revisione, o se qualcuno può ancora modificare a mano un prompt di sistema dal vivo. Nei contesti aziendali e governativi, lega ogni modifica a una traccia di audit e a un approvatore nominato, perché un regolatore che chiede "chi ha cambiato questo e che cosa avete testato" ha bisogno di una risposta registrata, non ricordata.

5. **Come decidiamo tra cloud, on-premises e rilascio sovrano, e abbiamo prezzato la vera economia a regime anziché il pilota?** La scelta del luogo del calcolo fissa la tua curva di costo, la tua postura di sovranità dei dati e le tue opzioni di uscita per anni, eppure è spesso fatta sulla bolletta cloud di un pilota che non somiglia per nulla alla produzione su larga scala. Per una grande organizzazione, la capacità elastica del cloud è economica da avviare e può diventare la singola voce maggiore una volta che l'inferenza gira in continuo, mentre l'on-premises scambia basso impegno con controllo ed economia a regime. Porta i volumi previsti di addestramento e inferenza, il punto di pareggio in cui l'hardware riservato o posseduto batte l'on-demand, i tuoi vincoli di residenza dei dati e sicurezza e gli schemi di raffica che argomentano per l'ibrido. Nei contesti governativi e regolamentati, pesa i requisiti di cloud sovrano o on-premises che possono diventare obbligatori con poco preavviso e conferma che l'architettura tenga i modelli dietro un'interfaccia interna così che uno spostamento forzato non riscriva i percorsi centrali.

6. **Possediamo davvero la nostra spesa per l'IA, e ogni team può vedere e rispondere del costo che guida?** Il costo dell'IA scala con l'uso in modi che sorprendono le persone e senza attribuzione la bolletta arriva come un unico numero opaco che nessun team si sente responsabile di ridurre. In una grande organizzazione, il costo che nessuno possiede è un costo che nessuno ottimizza, quindi la domanda è se la spesa è etichettata a team e casi d'uso con budget, allarmi e andamenti per esito, o se viene scoperta solo quando la finanza fa escalation. Porta il tuo modello di attribuzione dei costi, i maggiori fattori per team e le leve che ogni responsabile controlla: dimensionamento, caching, batching e sfoltimento del contesto. Per i bilanci aziendali e governativi, aggiungi la disciplina di prevedere e giustificare la spesa pluriennale per l'infrastruttura, poiché un ente pubblico che non sa spiegare la propria bolletta di calcolo voce per voce farà fatica a difenderla in revisione.

## Lente settoriale

**Startup.** Non possedere alcuna infrastruttura che puoi evitare. Chiama un'API di inferenza ospitata, instrada le richieste facili a un modello piccolo ed economico e riserva uno più grande ai casi difficili e usa il caching in modo aggressivo così che i prompt ripetuti non costino nulla. Usa un database vettoriale gestito anziché gestirne uno tuo, tieni i prompt in git con un breve script di valutazione prima di ogni modifica e registra il costo per richiesta così che una bolletta fuori controllo compaia prima di far male. La tua risorsa più scarsa è l'attenzione ingegneristica, quindi compra operabilità e tieni economico il cambio.

**Piccola impresa.** Senza un team di piattaforma, tratta erogazione, recupero e osservabilità come cose che compri dentro strumenti che già usi, non sistemi da dotare di personale. Privilegia inferenza gestita e ricerca vettoriale gestita con prezzi trasparenti e prevedibili e fissa un tetto di spesa rigido e un allarme di fatturazione dal primo giorno. Imposta onestamente la decisione come comprare contro costruire: gestire GPU o un indice vettoriale raramente ripaga al tuo volume e un modello piccolo dietro un'API ospitata di solito soddisfa il bisogno a una frazione dello sforzo.

**Grande impresa.** Il problema è una piattaforma condivisa da strada asfaltata tra molti team: acceleratori in pool con scheduler, quote e priorità per spingere in alto l'utilizzo, batching e caching standard, router di dimensionamento e costo attribuito a ogni team e caso d'uso. Filtra le modifiche di prompt e modello con suite di valutazione automatiche, standardizza lo strato di interfaccia così che fornitori e obiettivi di rilascio restino sostituibili e gestisci il costo per esito come metrica di prim'ordine anziché lasciare che ogni gruppo reinventi infrastruttura costosa e sottoutilizzata.

**Ente pubblico.** Sovranità dei dati, sicurezza e spesa prevedibile plasmano ogni scelta. Privilegia il rilascio on-premises o in cloud sovrano così che dati sensibili e modelli restino dentro confini controllati, pianifica le scarse GPU tra i dipartimenti con quote che puoi giustificare negli appalti e prevedi la capacità per difendere voce per voce la spesa pluriennale. Versiona e valuta prompt e modelli con una traccia di audit registrata, mantieni un'osservabilità completa su costo e qualità e tieni i modelli dietro un'interfaccia interna così che uno spostamento forzato verso un nuovo fornitore o una piattaforma sovrana non ti lasci in secca.

## Esempi

**Startup.** Una piccola startup che gestiva una funzionalità di scrittura con IA ha tenuto sensata la bolletta senza possedere GPU. Ha chiamato un'API di inferenza ospitata, instradato le richieste facili a un modello piccolo più economico e riservato quello più grande ai casi difficili e messo in cache le risposte ai prompt ripetuti. Ha memorizzato i propri prompt in git con un breve script di valutazione eseguito prima di ogni modifica, ha usato un database vettoriale gestito per il recupero così da non doverne gestire uno e ha registrato il costo per richiesta così che i fondatori potessero vedere la spesa salire prima che diventasse una sorpresa.

**Grande impresa.** Un'azienda di media che gestiva una funzionalità LLM ad alto traffico ha tagliato in modo sostanziale i costi di inferenza. Ha instradato le richieste facili a un modello piccolo e riservato un modello più grande a quelle difficili. Ha messo in cache le risposte alle query ripetute e abilitato il caching di prefisso per il proprio prompt di sistema condiviso. Ha fatto girare le GPU attraverso uno scheduler condiviso per tenere alto l'utilizzo, versionato tutti i prompt in git con una suite di valutazione automatica che filtrava le modifiche e strumentato il costo per richiesta così che ogni team di prodotto possedesse la propria spesa.

**Ente pubblico.** Un'agenzia nazionale con rigorose regole di sovranità dei dati ha distribuito i propri sistemi di IA on-premises così che dati sensibili e modelli non lasciassero mai il proprio ambiente controllato. Ha pianificato le scarse GPU tra i dipartimenti con quote e priorità, previsto la capacità per giustificare gli appalti pluriennali e costruito una piattaforma di ricerca vettoriale per il recupero sui documenti ufficiali. Prompt e modelli erano versionati e valutati prima del rilascio. Un'osservabilità completa seguiva costo e qualità e l'architettura teneva i modelli dietro un'interfaccia interna per preservare un percorso di uscita ed evitare il lock-in.

## Business case: motivazioni, ROI e TCO

La motivazione per una disciplinata infrastruttura di IA è semplice. L'IA su larga scala è costosa e il divario tra un rilascio ottimizzato e uno non ottimizzato è spesso di diverse volte in spesa. Il ROI viene da maggior utilizzo degli acceleratori, minor costo per richiesta attraverso batching e caching, modelli dimensionati correttamente ed evitare il sovradimensionamento. Osservabilità e pipeline di valutazione ripagano prevenendo costosi incidenti e permettendo un'iterazione sicura.

Il TCO copre calcolo con acceleratori (la voce maggiore per molti carichi), archiviazione vettoriale, infrastruttura di erogazione, rete e il personale di piattaforma e operazioni per gestirla. Pesalo contro il costo del non investire: bollette di inferenza fuori controllo, scarsa latenza che mina l'adozione e incapacità di scalare. Per gli enti pubblici, aggiungi il costo di fallire i requisiti di sovranità o sicurezza. Presenta il caso alla leadership mostrando gli andamenti del costo per esito e una piattaforma da strada asfaltata che permetta a molti team di distribuire l'IA in modo efficiente, anziché ciascuno costruire infrastruttura costosa e sottoutilizzata.

## Antipattern e insidie

- **Acceleratori inattivi.** Dedicare scarse GPU a team che le lasciano sottoutilizzate.
- **Nessun batching né caching.** Erogare ogni richiesta singolarmente e ricalcolare il contesto condiviso.
- **Modello più grande per default.** Usare un modello costoso dove ne basterebbe uno piccolo.
- **Cecità al costo.** Nessuna attribuzione, budget o visibilità del costo per richiesta finché arriva la bolletta.
- **Prompt non versionati.** Cambiare i prompt in produzione senza versionamento né cancello di valutazione.
- **Trascurare la latenza di coda.** Ottimizzare la latenza media mentre gli utenti soffrono le code lente.
- **Lock-in silenzioso.** Costruire a fondo sullo stack di erogazione di un fornitore senza portabilità.

## Modello di maturità

1. **Avvio.** Allocazione di GPU ad hoc che reagisce a chi chiede più forte, nessun batching né caching, nessuna visibilità del costo finché arriva la bolletta, prompt modificati dal vivo e non versionati, monitoraggio minimo.
2. **Sviluppo.** Alcuni team adottano pianificazione condivisa, caching e prompt sotto controllo di versione, ma la pratica è incoerente nell'organizzazione: un gruppo raggruppa e valuta mentre un altro eroga ancora ogni richiesta singolarmente e cambia i prompt a mano.
3. **Standardizzazione.** Una piattaforma da strada asfaltata documentata è fatta rispettare nell'organizzazione: pianificazione condivisa con quote e priorità, batching, caching e dimensionamento standard, infrastruttura vettoriale per il recupero, pipeline di valutazione automatiche che filtrano ogni modifica di prompt o modello e attribuzione dei costi a team e casi d'uso.
4. **Gestione.** La piattaforma è misurata e controllata rispetto a valori di riferimento: utilizzo degli acceleratori, costo per esito utile, latenza di coda, richiamo del recupero e regressioni di qualità per modifica sono seguiti con allarmi e soglie, il costo è posseduto da ogni team e le decisioni di procedere o meno su una modifica sono prese sull'evidenza anziché sull'intuito.
5. **Orchestrazione.** L'infrastruttura migliora e si adatta di continuo: instradamento, batching e scalatura si regolano da soli sui segnali dal vivo di costo e qualità, la capacità è riequilibrata tra team e tra obiettivi cloud, on-premises e sovrani man mano che domanda e vincoli si spostano, la portabilità è provata e la pianificazione dell'infrastruttura è integrata con prodotto, sicurezza e appalti.

## Spunti di discussione

- Come spingete in alto l'utilizzo degli acceleratori senza affamare i carichi prioritari?
- Dov'è il giusto equilibrio tra batching e caching per i vostri requisiti di latenza?
- Quando il rilascio on-premises o sovrano giustifica il proprio costo rispetto al cloud?
- Come attribuite e controllate la spesa per l'IA tra molti team?
- Che cosa dovrebbe filtrare una modifica di prompt o modello dal raggiungere la produzione?
- Come mantenete l'infrastruttura di erogazione abbastanza portabile da cambiare fornitore?

## Punti chiave

- Gli acceleratori sono scarsi e costosi; pianificali, condividili e usali deliberatamente.
- Batching, caching e dimensionamento dei modelli sono le leve primarie per costo e latenza.
- Le applicazioni di recupero hanno bisogno di infrastruttura di embedding e ricerca vettoriale ben gestita.
- L'LLMOps (versionamento dei prompt, pipeline di valutazione e osservabilità) è la spina dorsale operativa dell'IA generativa.
- Gestisci il costo in modo osservabile e preserva la portabilità per evitare il lock-in.

## Riferimenti e letture di approfondimento

- Chip Huyen, *Designing Machine Learning Systems*.
- Google, *Site Reliability Engineering* (a cura di Beyer, Jones, Petoff, Murphy).
- Jared Kaplan et al., *Scaling Laws for Neural Language Models*.
- Reza Yazdani Aminabadi et al., *DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale*.
- Woosuk Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention* (vLLM).
- Andriy Burkov, *Machine Learning Engineering*.
