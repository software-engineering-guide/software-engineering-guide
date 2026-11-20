# 10.8 Modelli di maturità

## Panoramica e motivazioni

Un [modello di maturità](https://en.wikipedia.org/wiki/Maturity_model) è un modo strutturato di valutare quanto sia capace e coerente la tua pratica in un dato dominio e di descrivere un percorso per migliorarla. Definisce una piccola scala di livelli. In basso, il lavoro è ad hoc e reattivo. In alto, è misurato, gestito e continuamente ottimizzato. Ogni gradino ha caratteristiche osservabili rispetto a cui puoi controllare.

I modelli di maturità trasformano una domanda vaga ("siamo bravi in questo?") in una risposta ripetibile ("siamo al livello 2 qui, al livello 4 là e questo è ciò che richiederebbe il livello 3"). Questo libro usa un modello a cinque livelli in ogni capitolo e li consolida nel capitolo 12.4. Questo capitolo tratta della disciplina stessa: come funzionano i modelli, quando aiutano e come fuorviano.

La ragione per cui contano è semplice. Le grandi organizzazioni non possono migliorare ciò che non vedono. Tra decine di team, la capacità varia enormemente e in modo invisibile. Alcuni team hanno ottimi test e sicurezza debole; altri il contrario. Un modello di maturità ti dà un vocabolario condiviso e un metro comune, così che le lacune diventino confrontabili, l'investimento possa essere ordinato per priorità e il progresso possa essere seguito nel tempo anziché semplicemente asserito. Esempi noti comprendono il CMMI ([Capability Maturity Model Integration](https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration), per il processo), il modello DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) (prestazioni di consegna del software), OWASP SAMM (Software Assurance Maturity Model) e BSIMM (Building Security In Maturity Model) per la sicurezza del software, TMMi (Test Maturity Model integration, per i test), il modello Agile Fluency e i modelli di maturità della gestione dei dati, più innumerevoli scorecard interne.

Per impresa e soprattutto governo, i modelli di maturità portano un peso particolare. Gli appalti governativi hanno da tempo usato i livelli di valutazione CMMI come qualifica dei fornitori e quadri come il CMMC statunitense ([Cybersecurity Maturity Model Certification](https://en.wikipedia.org/wiki/Cybersecurity_Maturity_Model_Certification)) legano la maturità della cybersicurezza direttamente all'idoneità per il lavoro nella difesa. Questo dà ai modelli di maturità veri denti. Crea anche il rischio centrale di questo capitolo: quando un livello diventa un cancello o un obiettivo, le persone ottimizzano per la valutazione anziché per la capacità sottostante. Usati bene, i modelli di maturità sono uno specchio. Usati male, sono teatro.

## Principi chiave

- **La maturità è un mezzo, non un fine.** L'obiettivo è capacità ed esiti, non un numero di livello.
- **Valuta per imparare, non per segnare.** Un'autovalutazione onesta batte una valutazione lusinghiera.
- **Più alto non è sempre meglio.** L'obiettivo giusto dipende da rischio, contesto e costo.
- **Misura per dominio, non un solo voto globale.** La capacità è disomogenea; un singolo numero la nasconde.
- **Dai priorità prima alle lacune di più bassa maturità e più alto rischio.**
- **Guardati dalla [legge di Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law).** Quando un livello è un obiettivo, smette di misurare la capacità.
- **Rivaluta periodicamente.** La maturità deriva man mano che cambiano persone, sistemi e minacce.

## Raccomandazioni

### Scegli il modello giusto per il dominio

Adegua il modello alla capacità che vuoi migliorare e preferisci modelli consolidati e basati sull'evidenza a quelli inventati dove esistono:

- **Processo e consegna:** CMMI (maturità di processo ampia), il modello di capacità DORA (prestazioni di consegna, fondato sulla ricerca, capitolo 11.2).
- **Sicurezza:** OWASP SAMM e BSIMM (pratiche di sicurezza del software), CMMC (cybersicurezza della difesa).
- **Test e qualità:** TMMi.
- **Agile e modi di lavorare:** il modello Agile Fluency (capitolo 10.7).
- **Dati:** modelli di maturità della gestione dei dati (DMM, DCAM).

Per l'uso interno, una semplice scala a quattro o cinque livelli applicata per capacità (come fa questo libro) è spesso più azionabile di un pesante quadro esterno. Riserva i modelli formali e valutati a dove sono richiesti per contratto.

### Valuta onestamente e per capacità

Esegui valutazioni che producano la verità, non il conforto. Coinvolgi le persone che fanno il lavoro. Raccogli evidenza anziché opinioni. Dai un punteggio a ogni capacità separatamente, così che il quadro rifletta la realtà: forte qui, debole là. Un'autovalutazione usata per guidare il miglioramento vale più di una valutazione esterna usata per guadagnare un distintivo, perché la prima premia la franchezza e la seconda premia la presentazione. Il capitolo 12.4 fornisce un'autovalutazione consolidata su ogni dominio di questo libro; usala come strumento di partenza.

### Usa la maturità per dare priorità, non per punire

L'output di una valutazione è un arretrato di miglioramento ordinato per priorità, non una pagella per la colpa. Combina la maturità con il rischio. Una capacità di livello 1 in un'area a basso rischio può andare bene. Una capacità di livello 2 in un'area critica per la sicurezza o la conformità è urgente. Dirigi l'investimento sulle lacune in cui bassa maturità incontra alto rischio e collega il lavoro agli esiti (capitolo 11.1) così che il miglioramento sia misurato dai risultati, non dal salire la scala fine a sé stesso.

### Fissa deliberatamente i livelli obiettivo: più alto non è gratis

Ogni livello in più costa sforzo e spesso aggiunge peso di processo. L'obiettivo giusto raramente è "livello 5 ovunque". È il livello in cui la capacità in più giustifica ancora il costo in più per il rischio di quel dominio. Le capacità regolamentate e critiche per la sicurezza possono davvero aver bisogno dei gradini più alti e l'audit richiede spesso almeno un livello 3 "definito". Molte altre sono ben servite al livello 3 e non farebbero che accumulare burocrazia spingendosi oltre. Decidi gli obiettivi per capacità e smetti di salire quando smette il ritorno corretto per il rischio.

### Guardati dal teatro della maturità

L'unica modalità di fallimento che distrugge il valore dei modelli di maturità è ottimizzare per il punteggio. Osserva valutazioni che assegnano voti generosi, evidenza assemblata solo per la valutazione o dichiarazioni di "livello 5" che gli incidenti di produzione smentiscono. Tieni la valutazione legata al comportamento osservabile e agli esiti reali. Ruota o controlla esternamente i tuoi valutatori. Tratta un autopunteggio sospettosamente alto come un cattivo odore. Nel momento in cui il livello diventa l'obiettivo, il modello smette di dirti la verità.

## Compromessi: vantaggi e svantaggi

| Approccio | Vantaggi | Svantaggi |
|---|---|---|
| **Modelli formali valutati (CMMI, CMMC)** | Confrontabili, riconosciuti per contratto, rigorosi | Costosi; invitano alla manipolazione; possono irrigidire il processo |
| **Scorecard interne leggere** | Rapide, azionabili, basso onere | Meno confrontabili all'esterno; facili da distorcere |
| **Modelli di capacità basati sull'evidenza (DORA)** | Legati a esiti reali; sostenuti dalla ricerca | Ambito più ristretto; richiede vere metriche |
| **Un solo voto di maturità complessivo** | Semplice da comunicare | Nasconde la capacità disomogenea; fuorvia |
| **Valutazione per capacità** | Accurata, priorità azionabili | Più sforzo; nessun numero di punta unico |

La tensione centrale è **valutazione come specchio contro valutazione come obiettivo**. Lo stesso modello che aiuta un team a vedersi con chiarezza diventa controproducente nell'istante in cui un livello è legato a ricompensa, idoneità o status. Più un livello conta, più energia fluisce nell'apparenza della maturità anziché nella sostanza.

## Domande da discutere con il tuo team

1. **Dovremmo tenere un'autovalutazione interna sincera separata da qualsiasi livello valutato per contratto, e chi possiede ciascuna?** Quando un livello CMMC o CMMI condiziona i ricavi, la valutazione e la verità divergono, perché l'energia fluisce verso il superare anziché il migliorare. Per una grande impresa o un fornitore governativo, quel divario è dove si nasconde il rischio: superate l'audit e restate esposti. Tenete due libri di proposito. Tenete la valutazione formale per l'idoneità e tenete una scorecard interna franca che nessuno è premiato per gonfiare. Nominate un responsabile per ciascuna e trattate qualsiasi distanza tra le due come un segnale da indagare, non da coprire. Portate alla riunione incidenti recenti, quasi incidenti e decadimento dopo la valutazione come evidenza di quale libro dice la verità.

2. **Per ogni dominio, stiamo adottando un modello consolidato e basato sull'evidenza o inventando una nostra scorecard, ed è la scelta giusta?** I modelli consolidati (DORA per la consegna, SAMM o BSIMM per la sicurezza, TMMi per i test) portano ricerca e confrontabilità esterna che una griglia fatta in casa non può eguagliare. Una semplice scala interna a quattro livelli è più veloce e azionabile ed è spesso la scelta migliore per l'orientamento interno. La trappola è inventare un quadro su misura pesante che ha tutta la cerimonia di un modello formale e nessuna base di evidenza. Decidete per dominio: riservate i modelli formali valutati a dove un contratto li richiede, usate modelli basati sull'evidenza dove esistono e si adattano e tenete una semplice scala per capacità per tutto il resto. Portate l'elenco dei domini, segnate quale modello ciascuno usa oggi e mettete in discussione ogni scorecard inventata.

3. **Chi conduce le nostre valutazioni, come coglieremmo voti generosi e con che frequenza rivalutiamo?** Una valutazione che si dà il voto da sola si lusinga e la maturità deriva man mano che cambiano persone, sistemi e minacce, quindi una valutazione vecchia di due anni è spesso finzione. Ruotate i valutatori o portate un controllo esterno di buon senso e trattate un autopunteggio sospettosamente alto come un cattivo odore da inseguire, non una vittoria da festeggiare. Fissate una cadenza di rivalutazione legata a quanto in fretta cambia ogni dominio: la sicurezza più spesso della, diciamo, documentazione. Raccogliete evidenza e coinvolgete le persone che fanno il lavoro anziché raccogliere opinioni dai manager. Se la vostra risposta è che un team si valuta da solo una volta all'anno senza controllo incrociato, state misurando il conforto, non la capacità.

4. **Quale livello di maturità obiettivo ha davvero bisogno ciascuna capacità, e dove spingersi più in alto comprerebbe solo peso di processo?** Più alto non è gratis: ogni livello in più costa sforzo e di solito aggiunge cerimonia, quindi un obiettivo generale di livello 5 ovunque drena un budget di miglioramento finito in burocrazia che alcuni domini non ripagheranno mai. Per una grande organizzazione l'obiettivo giusto varia per capacità, perché un'area a basso rischio ferma al livello 2 può essere perfettamente sicura mentre un'area critica per la sicurezza o la conformità allo stesso livello è un'emergenza. Portate una valutazione del rischio per capacità, una stima onesta di quanto il gradino successivo costi in sforzo e processo e qualsiasi soglia di audit o contrattuale, poiché molti audit richiedono almeno un livello 3 definito. Nei contesti aziendali e governativi, alcune capacità regolamentate hanno davvero bisogno dei gradini più alti mentre la maggior parte è ben servita al livello 3, quindi decidete gli obiettivi deliberatamente, capacità per capacità e smettete di salire quando smette il ritorno corretto per il rischio.

5. **L'ultima volta che abbiamo alzato un livello di maturità, l'esito che doveva proteggere è davvero migliorato, o si è mosso solo il punteggio?** Un livello che sale mentre incidenti, tempo di consegna o tassi di difetti restano piatti è la legge di Goodhart in azione: una volta che il numero diventa l'obiettivo, smette di misurare la capacità. Per un grande team questo passa facilmente, perché una valutazione riuscita sembra un progresso anche quando la produzione racconta un'altra storia. Legate il livello di ogni capacità a una vera metrica di esito prima di investire, poi portate alla discussione l'evidenza prima e dopo: incidenti per trimestre, tasso di fallimento delle modifiche, tempo di ripristino, qualunque cosa la capacità esista per migliorare. Nei portafogli aziendali e governativi in cui un livello valutato condiziona l'idoneità, il divario è pericoloso, perché il livello può salire su evidenza assemblata mentre la pratica sottostante decade in silenzio e la prima prova è una violazione, un'interruzione o un audit fallito.

6. **Comunichiamo un unico voto di maturità di punta o un quadro per capacità, e i livelli sono mai legati a ricompensa, classifica o status del team?** Un singolo numero complessivo è facile da presentare alla leadership e nasconde esattamente la disomogeneità che conta, perché una forte consegna può mascherare una capacità di sicurezza di livello 1; una mappa di calore per capacità richiede più lavoro ma mostra dove bassa maturità incontra alto rischio. La domanda più dura è come i punteggi vengono usati, perché nel momento in cui un livello è legato alla ricompensa o alla classifica di un team, la rendicontazione onesta muore e lo sforzo fluisce nell'apparenza della maturità anziché nella sostanza. Portate la mappa di calore e un resoconto franco di ogni posto in cui un livello alimenta oggi una valutazione delle prestazioni, una decisione di bilancio o una scorecard di fornitore. Per imprese e fornitori governativi, dove i livelli valutati possono condizionare ricavi e idoneità, siate espliciti su quali voti portano conseguenze e quali esistono solo per orientare, perché un quadro di maturità che le persone sono premiate per gonfiare smette di descrivere la realtà.

## Lente settoriale

**Startup.** Un modello valutato pesante è un onere che non puoi permetterti su una breve autonomia. Esegui un'autovalutazione di un'ora su una scala semplice attraverso una manciata di capacità, correggi solo la lacuna a più bassa maturità che blocca qualcosa di concreto (diciamo, il questionario di sicurezza del tuo primo cliente aziendale) e lascia stare il resto. La valutazione dovrebbe costare un pomeriggio, non un consulente e il suo output è una singola prossima azione anziché un punteggio uniformemente alto di cui non hai bisogno né che puoi finanziare.

**Piccola impresa.** Senza un valutatore dedicato e con un budget stretto, prendi in prestito un modello pubblico leggero anziché commissionare un quadro su misura: una breve lista di controllo di consegna o di sicurezza che puoi autovalutare. Trattala come una conversazione annuale su dove un punto debole ti costerebbe un cliente, non come un programma permanente. Tienila economica e franca, perché un punteggio lusinghiero che hai pagato un fornitore per produrre vale meno di uno sincero che hai fatto tu stesso in un pomeriggio.

**Grande impresa.** Il valore è una scorecard condivisa per capacità applicata in modo coerente su molti team, così che le lacune diventino confrontabili e il budget di miglioramento fluisca dove bassa maturità incontra alto rischio. Guardati con decisione dal teatro della maturità una volta che i livelli alimentano budget o status: ruota o controlla esternamente i valutatori e gestisci i risultati come una mappa di calore che orienta l'investimento sulla strada asfaltata (capitolo 4.2) anziché una classifica che ordina i team e uccide la rendicontazione onesta.

**Ente pubblico.** Un livello di maturità è qui spesso un cancello letterale: CMMC per il lavoro nella difesa, una valutazione CMMI come qualifica del fornitore. Raggiungi il livello richiesto con capacità genuina e tieni un'autovalutazione interna franca separata dalla valutazione formale così che la soglia dell'audit non diventi mai in silenzio il tetto. Documenta l'evidenza in modo trasparente per i valutatori e tratta qualsiasi distanza tra il livello certificato e la pratica reale come rischio responsabile da chiudere, non carta da archiviare.

## Esempi

**Startup.** Una startup SaaS di dieci persone esegue un'autovalutazione di un'ora rispetto a una semplice scala a quattro livelli che copre consegna, test, sicurezza e reperibilità. Trova consegna e test al livello 3 ma la sicurezza ferma al livello 1, il che conta perché sta per firmare il suo primo cliente aziendale con un questionario di sicurezza. Così i fondatori spendono il mese successivo ad alzare solo la sicurezza a un livello 2 difendibile e lasciano stare il resto, anziché inseguire un punteggio uniformemente alto di cui non hanno bisogno né che possono ancora permettersi.

**Grande impresa.** Un'azienda di servizi finanziari valuta i suoi 40 team con una scorecard leggera per capacità (consegna, test, sicurezza, osservabilità, reperibilità). La mappa di calore rivela che la maturità della sicurezza resta più indietro dove l'esposizione normativa è più alta, quindi il team di piattaforma finanzia per primi per quei team strumenti di sicurezza sulla strada asfaltata (capitolo 4.2). Poiché la valutazione è usata per dare priorità all'investimento anziché per classificare i team, i manager riportano onestamente. La rivalutazione un anno dopo mostra un movimento reale e, cosa cruciale, meno incidenti di sicurezza, non solo punteggi più alti.

**Ente pubblico.** Un appaltatore della difesa deve raggiungere un livello CMMC richiesto per concorrere al lavoro e un integratore di sistemi detiene una valutazione CMMI come qualifica contrattuale. Qui il livello di maturità è un cancello letterale verso i ricavi. La versione ben gestita tratta il livello richiesto come soglia di capacità genuina e tiene un'autovalutazione interna franca separata dalla valutazione formale. La versione mal gestita assembla evidenza per la valutazione e lascia decadere la pratica reale il giorno dopo, superando l'audit pur restando esposta.

## Business case: motivazioni, ROI e TCO

Il ritorno della valutazione della maturità viene da un **investimento diretto**. I budget di miglioramento sono finiti. Spesi alla cieca, finanziano ciò che è più rumoroso. Una valutazione della maturità ti mostra dove la capacità è più debole rispetto al rischio, così che la stessa spesa compri più riduzione del rischio e più miglioramento degli esiti. La valutazione stessa è economica, solo giorni di revisione strutturata e basata sull'evidenza, rispetto al costo di programmi di miglioramento mal allocati o, peggio, di una lacuna di capacità non rilevata che emerge come violazione, interruzione o audit fallito.

Sul **costo totale di proprietà**, la disciplina è a basso costo quando la tieni leggera e ad alto costo quando si indurisce in burocrazia di valutazione. Il costo nascosto dominante è il *teatro della maturità*: lo sforzo speso a produrre l'apparenza di maturità non restituisce nulla e può mascherare un rischio vero, che è un ROI negativo. Per presentare il caso alla leadership, presenta la maturità come una lente di rischio e di investimento, una mappa di calore che trasforma "migliorare tutto" in "migliorare per prime queste tre cose" e metti esplicitamente a bilancio contro la tentazione di inseguire i livelli fine a sé stessi. Dove un livello è richiesto per contratto (CMMC, CMMI), il ROI è diretto: è il prezzo dell'idoneità e l'obiettivo è raggiungerlo con vera capacità anziché con una costosa finzione.

## Antipattern e insidie

- **Il livello come obiettivo:** inseguire un numero anziché la capacità che deve rappresentare.
- **Teatro della maturità:** assemblare evidenza per una valutazione mentre la pratica reale decade.
- **Un solo voto globale:** un singolo punteggio di maturità che nasconde una pericolosa disomogeneità.
- **Più alto è sempre meglio:** spingere ogni capacità al livello 5 a prescindere da rischio o costo.
- **Valuta una volta, mai più:** una valutazione una tantum trattata come verità permanente.
- **Classificare i team per dare la colpa:** usare la maturità per punire, il che uccide la rendicontazione onesta.
- **Culto del modello:** seguire la cerimonia di un pesante quadro oltre il punto di utilità.
- **Ignorare gli esiti:** salire la scala mentre consegna, affidabilità o sicurezza non migliorano.

## Modello di maturità

- **Livello 1, Avvio.** Nessuna nozione condivisa di maturità; la capacità è presunta, disomogenea e non misurata; qualsiasi valutazione è reattiva, innescata da un incidente o da una richiesta di audit anziché pianificata.
- **Livello 2, Sviluppo.** Pochi team conducono valutazioni ad hoc rispetto a una qualche scala, ma modello, cadenza e rigore variano da team a team; i risultati sono usati in modo incoerente e l'evidenza è scarsa, quindi segnare per apparenza è un rischio sempre presente.
- **Livello 3, Standardizzazione.** Un unico modello per capacità e una cadenza di valutazione sono documentati e applicati in tutta l'organizzazione; le valutazioni sono basate sull'evidenza, coinvolgono le persone che fanno il lavoro e alimentano un arretrato di miglioramento ordinato per priorità anziché una pagella.
- **Livello 4, Gestione.** La maturità è misurata e controllata con dati: il livello di ogni capacità è seguito rispetto a un valore di riferimento, legato a una metrica di esito (incidenti, tempo di consegna, tasso di fallimento delle modifiche) e rivalutato con una cadenza fissata, così che deriva e voti generosi emergano come numeri anziché opinioni e gli obiettivi siano fissati deliberatamente per dominio rispetto a rischio e costo.
- **Livello 5, Orchestrazione.** La valutazione è integrata nell'organizzazione e continuamente migliorata: maturità, rischio ed esiti informano l'investimento come un unico quadro adattivo, gli obiettivi sono riequilibrati man mano che si spostano minacce e contesto, i valutatori sono ruotati o controllati esternamente come cosa ovvia e la pratica ritira attivamente la cerimonia che non si guadagna più il costo.

## Spunti di discussione

1. Quali delle vostre capacità state presumendo siano mature senza evidenza?
2. Dove la vostra più bassa maturità coincide con il vostro più alto rischio, ed è lì che va il vostro budget di miglioramento?
3. Qualche livello di maturità nella vostra organizzazione è un obiettivo o un cancello? Che comportamento ha prodotto?
4. Qual è il giusto livello obiettivo per ciascuna capacità, e dove salire ancora aggiungerebbe solo burocrazia?
5. I vostri team riporterebbero onestamente la propria maturità, o il modo in cui usate i punteggi punisce la franchezza?
6. L'ultima volta che avete "migliorato la maturità", gli esiti sono davvero cambiati?

## Punti chiave

- Un modello di maturità valuta la capacità rispetto a una scala di livelli e descrive un percorso per migliorare: uno specchio, non un trofeo.
- Scegli modelli consolidati e basati sull'evidenza per dominio (CMMI, DORA, SAMM/BSIMM, CMMC); una scala leggera per capacità è spesso la più azionabile.
- **Valuta onestamente, per capacità** e usa i risultati per **dare priorità in base al rischio**, non per classificare o dare la colpa.
- **Più alto non è sempre meglio:** fissa deliberatamente i livelli obiettivo rispetto a rischio e costo.
- Guardati dal **teatro della maturità** e dalla **legge di Goodhart**: un livello che diventa un obiettivo smette di misurare la capacità.
- Vedi il capitolo 12.4 per l'autovalutazione consolidata di maturità di questo libro e la sezione di maturità di ogni capitolo.

## Riferimenti e letture di approfondimento

- CMMI Institute / ISACA, *Capability Maturity Model Integration (CMMI)*.
- Watts Humphrey, *Managing the Software Process* (origini della maturità del processo software).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (pensiero per capacità, non per livello di maturità, sulla consegna).
- OWASP, *Software Assurance Maturity Model (SAMM)*; BSIMM (*Building Security In Maturity Model*).
- U.S. Department of Defense, *Cybersecurity Maturity Model Certification (CMMC)*.
- TMMi Foundation, *Test Maturity Model integration*.
- James Shore e Diana Larsen, *The Agile Fluency Model*.
- Martin Fowler, "Maturity Model" (bliki), su usi e abusi.
