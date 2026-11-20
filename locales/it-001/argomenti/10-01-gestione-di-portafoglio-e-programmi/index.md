# 10.1 Gestione di portafoglio e programmi

## Panoramica e motivazioni

La [gestione di programmi](https://en.wikipedia.org/wiki/Program_management) e di portafoglio è la disciplina di decidere che cosa una grande organizzazione di ingegneria dovrebbe costruire, finanziare quel lavoro nel tempo, ordinarlo tra molti team e orientarlo verso esiti strategici anziché produzioni isolate. Un singolo team può cavarsela con un allineamento informale e un arretrato condiviso. Un'impresa o un ente pubblico che gestisce decine o centinaia di team no. Tutto quel lavoro compete per lo stesso scarso budget, le stesse competenze specialistiche, le stesse piattaforme condivise e la stessa attenzione della leadership. Senza uno strato di portafoglio deliberato, ti ritrovi con un'ottimizzazione locale: ogni team occupato, ogni roadmap plausibile e tuttavia l'insieme che consegna molto meno valore strategico di quanto dovrebbe.

Per i grandi team la posta si compone. Sforzi duplicati, priorità disallineate e dipendenze tra team non gestite tassano in silenzio ogni iniziativa. Una funzionalità che un team potrebbe rilasciare in uno sprint aspetta tre trimestri perché dipende da un team di piattaforma che non ne ha mai sentito parlare. Nel governo il problema è ancora più acuto. Stanziamenti annuali, finanziamenti di capitale pluriennali, diritto degli appalti e responsabilità pubblica significano che un programma mal impostato può vincolare un ente a anni di spesa impegnata sulla cosa sbagliata. Quindi fare bene la [gestione di portafoglio](https://en.wikipedia.org/wiki/Project_portfolio_management) non è onere burocratico. È come una grande organizzazione trasforma la strategia in software rilasciato.

Questo capitolo tratta la gestione di portafoglio e di programmi come una questione di leadership ingegneristica, non solo come una funzione di [ufficio di gestione dei progetti (PMO)](https://en.wikipedia.org/wiki/Project_management_office). L'obiettivo è collegare strategia e obiettivi alle roadmap, dare priorità onestamente sotto vincoli reali, trattare dipendenze e fornitori come rischi di prim'ordine e navigare i cicli di bilancio e di appalto, specialmente i ritmi di finanziamento pluriennali che dominano il lavoro del settore pubblico.

## Principi chiave

- **Esiti anziché produzioni.** Finanzia e misura il cambiamento nel mondo (adozione, costo, affidabilità, risultati di missione), non il volume di funzionalità rilasciate.
- **La strategia deve essere leggibile.** Ogni team dovrebbe poter ricondurre il proprio lavoro a un piccolo numero di obiettivi pubblicati.
- **Dare priorità è sottrarre.** Un portafoglio che dice sì a tutto non ha strategia; il valore sta in ciò che deliberatamente non fai.
- **Le dipendenze sono il vero calendario.** Per le grandi organizzazioni, il costo di coordinamento, non lo sforzo di scrittura del codice, è di solito il vincolo operante.
- **Finanzia team durevoli, non progetti temporanei.** I team stabili e allineati al prodotto superano i bacini di personale riassemblati per progetto.
- **Adegua la cadenza di finanziamento alla cadenza di apprendimento.** Impegna denaro in incrementi che ti permettono di fermarti, cambiare rotta o raddoppiare man mano che arriva l'evidenza.
- **I fornitori sono estensioni del portafoglio, non sono fuori da esso.** Il lavoro di appaltatori e [integratori di sistemi](https://en.wikipedia.org/wiki/Systems_integrator) deve essere governato con la stessa visibilità del lavoro interno.

## Raccomandazioni

### Allinea l'ingegneria a strategia e OKR

Pubblica un piccolo insieme di obiettivi a livello di organizzazione (idealmente da tre a cinque) e fai scendere a cascata in modo leggero. Lascia che i team fissino i propri risultati chiave al servizio di quegli obiettivi condivisi anziché consegnare loro compiti assegnati. Tieni bassa la cascata: due o tre livelli al massimo, o il tessuto connettivo tra strategia e lavoro quotidiano diventa finzione. Rivedi gli obiettivi con una cadenza fissa (di solito trimestrale per i progressi, annuale per gli obiettivi stessi) e ritira o riscrivi apertamente quelli che non contano più. Resisti a trasformare gli [OKR](https://en.wikipedia.org/wiki/OKR) (obiettivi e risultati chiave) in un'arma di valutazione delle prestazioni. Nel momento in cui i risultati chiave guidano i bonus individuali, i team abbassano i propri obiettivi e perdi il segnale.

### Fai roadmap con intento e orizzonti onesti

Tieni le roadmap a più altitudini. Una roadmap di portafoglio mostra temi ed esiti attraverso i trimestri; le roadmap dei team mostrano le consegne a breve termine. Impostale attorno a problemi ed esiti, con una confidenza che cala nel tempo. Gli orizzonti "ora / prossimo / poi" comunicano l'incertezza molto meglio dei [diagrammi di Gantt](https://en.wikipedia.org/wiki/Gantt_chart) datati che implicano una falsa precisione. Rivedi le roadmap con una cadenza regolare e trattale come impegni verso una direzione, non contratti per date specifiche lontane nel futuro.

### Dai priorità con quadri espliciti e compromessi nominati

Scegli un metodo di prioritizzazione leggero e coerente e applicalo in modo uniforme, così da poter confrontare l'intero portafoglio. Le opzioni comuni comprendono il punteggio ponderato (valore, costo, rischio, adattamento strategico), il [costo del ritardo](https://en.wikipedia.org/wiki/Cost_of_delay) (il valore perso per ogni unità di tempo in cui una consegna preziosa aspetta) e la sua variante Weighted-Shortest-Job-First (WSJF) e RICE (portata, impatto, confidenza, sforzo). Nessuna formula decide per te. Il vero valore di un quadro è che costringe le assunzioni a venire allo scoperto, dove i leader possono discuterne. Registra sempre il compromesso che stai facendo (che cosa stai rimandando e perché) così da poter rivedere la decisione quando i fatti cambiano.

### Gestisci le dipendenze tra molti team

Rendi visibili le dipendenze prima che mordano. Tieni una mappa o un registro delle dipendenze che nomini, per ogni iniziativa significativa, che cosa le serve da altri team e per quando. Usa un regolare evento di pianificazione tra team (una sessione di pianificazione trimestrale in grande stanza è comune nei quadri scalati) per far emergere e negoziare le dipendenze apertamente. Meglio ancora, eliminale per progetto: investi in piattaforme self-service, API ben documentate e chiari contratti interni così che i team possano procedere senza aspettarsi a vicenda. Dai a ogni dipendenza trasversale un unico responsabile. Le dipendenze senza responsabile sono dove i programmi slittano in silenzio.

### Governa fornitori, appaltatori e integratori di sistemi

Tratta i partner di consegna esterni come parte del portafoglio. Chiedi la stessa visibilità sui loro arretrati, velocità, qualità e rischi che ti aspetti internamente. Struttura i contratti attorno a esiti e software funzionante consegnato in incrementi, non a volumi di documentazione o persone sedute. Mantieni abbastanza capacità tecnica interna da specificare il lavoro, giudicare la qualità e subentrare se un fornitore fallisce. Non esternalizzare mai la funzione di acquirente esperto. Proteggiti dal [lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in) possedendo i tuoi dati, richiedendo interfacce aperte e insistendo su disposizioni di uscita e transizione fin dal primo giorno.

### Naviga appalti, bilanci e finanziamenti pluriennali

Capisci il ritmo di finanziamento in cui operi e progetta i programmi perché vi si adattino. Nel governo in particolare, gli stanziamenti possono essere annuali mentre i sistemi richiedono anni per essere costruiti, il che crea pressione a spendere prima della fine dell'anno e a sovra-dimensionare l'impegno iniziale. Contrastalo in tre modi: struttura i programmi in incrementi indipendentemente preziosi (contrattualizzazione modulare), cerca l'autorità per un finanziamento incrementale e agile dove le regole lo consentono e costruisci vere stime di costo che separano costruzione, gestione e sostentamento. Coinvolgi presto [appalti](https://en.wikipedia.org/wiki/Procurement), finanza e ufficio legale (plasmano ciò che è possibile molto più di quanto la maggior parte degli ingegneri capisca) e traduci i piani tecnici nelle categorie di bilancio e nei confini degli anni fiscali di cui quelle funzioni hanno bisogno.

## Compromessi: vantaggi e svantaggi

| Approccio | Vantaggi | Svantaggi |
|---|---|---|
| Controllo centralizzato del portafoglio | Forte allineamento strategico; meno duplicazione; compromessi di finanziamento più facili | Decisioni più lente; può soffocare l'autonomia dei team e l'innovazione locale |
| Autonomia decentralizzata dei team | Team rapidi e motivati; competenza locale onorata | Duplicazione; debole coerenza strategica; rischio nascosto tra i team |
| Finanziamento basato sui progetti | Ambito e responsabilità chiari per iniziativa | Ricambio di team; miopia; debole proprietà nel lungo periodo |
| Finanziamento basato su prodotto/team | Proprietà durevole; qualità sostenuta | Più difficile da riallocare; rischio di finanziare sforzi zombie |
| Prioritizzazione per formula | Trasparente, confrontabile, difendibile | Falsa precisione; input manipolabili; può soppiantare il giudizio |
| Programmi pluriennali a prezzo fisso | Stabilità di finanziamento; investimento a lungo orizzonte | Vincola le assunzioni iniziali; costoso correggere la rotta |

La tensione centrale è tra coerenza e velocità. Troppo controllo centrale e l'organizzazione si muove lentamente e demotiva le sue persone migliori. Troppo poco e si frammenta in cento ottimi locali. Le organizzazioni mature centralizzano solo le poche cose che devono essere coerenti (strategia, piattaforme condivise, standard trasversali e il compromesso di finanziamento) e spingono le decisioni di esecuzione il più vicino possibile ai team. La tensione tra stabilità di finanziamento e adattabilità si risolve allo stesso modo: non scegliendone una, ma impegnando denaro in modo incrementale su team durevoli, così che la stabilità delle persone coesista con la flessibilità della direzione.

## Domande da discutere con il tuo team

1. **Quali poche cose devono restare coerenti in tutta l'organizzazione, e quali decisioni dovreste spingere ai team?** La tensione centrale in un portafoglio è coerenza contro velocità e sbagliare il confine è costoso in entrambi i modi. Centralizzate troppo e le decisioni procedono a rilento mentre le vostre persone migliori perdono autonomia; centralizzate troppo poco e vi frammentate in cento ottimi locali con sistemi duplicati e rischio nascosto tra i team. Le organizzazioni mature tengono al centro solo un breve elenco: strategia, piattaforme condivise, standard trasversali e il compromesso di finanziamento. Portate evidenza alla riunione: contate quanti team stanno risolvendo lo stesso problema in modo indipendente e quante recenti decisioni si sono bloccate in attesa dell'approvazione centrale. Se uno dei due numeri è alto, avete tracciato la linea nel posto sbagliato, quindi spostate specifici diritti decisionali anziché discutere di centralizzazione in astratto.

2. **Come finanzierete gli esiti anziché le produzioni senza perdere la responsabilità che il finanziamento a progetto vi dava?** Finanziare team durevoli e allineati al prodotto batte il finanziare progetti temporanei, perché i team stabili sostengono la qualità e possiedono la gestione, non solo la costruzione. Il problema: il finanziamento a progetto dava ai leader un ambito pulito e una chiara linea di responsabilità e il finanziamento persistente dei team può scivolare nel pagare sforzi zombie molto dopo che la loro premessa è fallita. Risolvetelo impegnando denaro in modo incrementale su team durevoli, rivedendo ogni tema con cadenza trimestrale e riallocando la capacità tra i temi anziché sciogliere i team. Portate l'evidenza che conta: per ogni team finanziato, quale esito (adozione, costo, affidabilità, risultato di missione) si è mosso il trimestre scorso e che cosa smettereste di finanziare se il denaro diventasse improvvisamente scarso. Se non sapete nominare l'esito, state ancora finanziando la produzione.

3. **Quanta capacità ingegneristica interna dovete mantenere per restare un acquirente esperto del lavoro di fornitori e integratori di sistemi?** Quando affidate la consegna ad appaltatori o a un integratore di sistemi, conservate la responsabilità, quindi vi serve abbastanza profondità interna da specificare il lavoro, giudicare la qualità e subentrare se il fornitore fallisce. Perdete quella capacità e ottenete un'esternalizzazione a ore: comprate ore anziché esiti e non sapete più dire se siete serviti o catturati. Pesate il costo di trattenere ingegneri senior che non scrivono la maggior parte del codice contro il costo ben più grande del lock-in sul fornitore e di una missione tenuta in ostaggio. Portate segnali concreti: il vostro team sa leggere l'arretrato del fornitore, riprodurre una build e possedere oggi i dati e le interfacce? Insistete su disposizioni di uscita e transizione fin dal primo giorno, perché il momento di negoziare la leva è prima di firmare, non quando il rapporto si guasta.

4. **Quali iniziative state deliberatamente declinando di finanziare in questo ciclo, e ogni team può ricondurre quel no alla strategia?** Dare priorità è sottrarre e un portafoglio che dice in silenzio sì a tutto non ha strategia; si limita a spargere una capacità scarsa troppo sottile per finire qualcosa bene. Per una grande organizzazione il danno è diffuso, perché nessuna singola approvazione sembra sconsiderata, eppure la somma affama le poche scommesse che muoverebbero davvero un obiettivo. La spinta contraria è reale: ogni iniziativa declinata ha uno sponsor che crede sia essenziale e un quadro (punteggio ponderato, costo del ritardo, RICE) non deciderà per voi, fa solo venire allo scoperto le assunzioni dove i leader possono discuterne. Portate l'elenco ordinato, il compromesso esplicito registrato per ogni rinvio e il conteggio delle iniziative in corso rispetto al numero che avete la capacità di finire. Nei contesti aziendali e governativi, aggiungete il costo politico di ogni no e chi detiene l'autorità di farlo valere, perché una decisione di priorità che qualsiasi sponsor può ribaltare salendo di livello non è una decisione, è un suggerimento.

5. **Dove sono oggi le vostre dipendenze tra team, e quali state eliminando per progetto anziché limitarvi a tracciarle?** Per una grande organizzazione, il costo di coordinamento, non lo sforzo di scrittura del codice, è di solito il vincolo operante, quindi una funzionalità che un team potrebbe rilasciare in uno sprint può aspettare tre trimestri un team di piattaforma che non ne ha mai sentito parlare. Tracciare le dipendenze in un registro le rende visibili, ma la visibilità non è risoluzione; la mossa a più alta leva è eliminarle per progetto con piattaforme self-service, API documentate e chiari contratti interni così che i team smettano di aspettarsi a vicenda. Il compromesso è che l'investimento in piattaforma costa capacità vera ora rispetto a ritardi di dipendenza che si compongono in silenzio dopo ed è sempre allettante finanziare la funzionalità visibile anziché la piattaforma invisibile. Portate la mappa delle dipendenze per le vostre iniziative principali, il conteggio delle consegne slittate il trimestre scorso in attesa di un altro team e se ogni dipendenza trasversale ha un unico responsabile. Nei programmi aziendali e governativi in cui decine di team e integratori esterni si intrecciano, nominate la cadenza di pianificazione tra team che li fa emergere presto, perché una dipendenza scoperta al momento dell'integrazione è già un fallimento di calendario.

6. **Il modo in cui avete strutturato finanziamento e contratti corrisponde al ritmo a cui imparate davvero?** Impegnare denaro in grossi blocchi pluriennali vincola le vostre assunzioni più precoci e meno informate, eppure molti regimi di finanziamento, specialmente gli stanziamenti governativi annuali, vi spingono a sovra-dimensionare l'impegno iniziale e a spendere prima della fine dell'anno. La considerazione contraria è che la stabilità del finanziamento permette ai team durevoli di investire sul lungo orizzonte, quindi la risposta non sono contratti minuscoli ma incrementi indipendentemente preziosi finanziati a fasi legate a risultati dimostrati. Portate la forma dei vostri impegni attuali: quanto è impegnato prima che il primo software funzionante sia rilasciato, se le stime di costo separano costruzione, gestione e sostentamento e quanto tardi potete ancora fermare o reindirizzare senza sprecare lo stanziamento. Per i lettori di imprese e governo, appalti e ufficio legale plasmano ciò che è possibile molto più di quanto gli ingegneri si aspettino, quindi coinvolgeteli presto e chiedete esplicitamente quale contrattualizzazione modulare e autorità di finanziamento incrementale le regole già consentono prima di presumere di aver bisogno di un contratto monolitico.

## Lente settoriale

**Startup.** Con una manciata di ingegneri e poca autonomia, i fondatori sono lo strato di portafoglio, quindi tienilo a una lavagna: due o tre esiti pubblicati, lavoro agganciato ad essi e tutto il resto tagliato a vista. Finanzia in scommesse brevi che puoi fermare in settimane anziché impegnarti con un trimestre di anticipo e salta quadri, registri ed eventi di pianificazione che costerebbero più coordinamento di quanto ne risparmino. Il tuo unico vero rischio di portafoglio è la manciata di dipendenze esterne che non puoi evitare, quindi nomina un responsabile per ciascuna.

**Piccola impresa.** Senza un PMO o un responsabile di programma dedicato, la gestione di portafoglio è una conversazione ricorrente tra le persone che già hai, non un ruolo da assumere. Appoggiati al comprare anziché costruire per tutto ciò che è fuori dal tuo nucleo e giudica i fornitori da quanto facilmente potresti lasciarli, poiché il lock-in fa più male quando manca il personale per migrare. Tieni un'unica lista onesta di ciò che finanzi e ciò che deliberatamente non finanzi e rivedila con una cadenza fissa e leggera così che il budget scarso segua i pochi esiti che pagano le bollette.

**Grande impresa.** Su decine o centinaia di team il lavoro è coerenza senza stallo: centralizza solo strategia, piattaforme condivise, standard trasversali e il compromesso di finanziamento e spingi l'esecuzione ai team. Finanzia in modo persistente team durevoli e allineati al prodotto, esegui una revisione di portafoglio trimestrale che rialloca la capacità tra i temi e gestisci le dipendenze attraverso un registro condiviso e una pianificazione tra team. Governance e audit non sono negoziabili a questa scala, quindi rendi il lavoro dei fornitori visibile quanto quello interno e registra il compromesso dietro ogni decisione di priorità.

**Ente pubblico.** Diritto degli appalti, stanziamenti annuali e responsabilità pubblica plasmano ogni mossa. Privilegia la contrattualizzazione modulare rispetto a un'aggiudicazione pluriennale monolitica, finanzia a fasi legate a risultati dimostrati e separa costruzione, gestione e sostentamento nelle tue stime così che il sostentamento non sia mai una sorpresa. Tieni un team interno di acquirente esperto, possiedi i tuoi dati e interfacce e scrivi disposizioni di uscita e transizione in ogni contratto, perché gli obblighi di trasparenza significano che un programma fallito diventa un evento pubblico e verificato anziché una silenziosa cancellazione.

## Esempi

**Startup.** Una startup in fase seed di dodici persone gestisce due piccole squadre e i fondatori fanno da intero strato di portafoglio. Ogni lunedì agganciano il lavoro a soli due esiti pubblicati, attivazione e margine lordo, e tagliano apertamente tutto ciò che non serve né l'uno né l'altro, così una richiesta di integrazione appariscente viene parcheggiata a favore della correzione dell'abbandono nell'onboarding. Finanziano in scommesse brevi anziché impegnarsi un trimestre in anticipo e nominano un responsabile per l'unica dipendenza esterna che non possono evitare, il fornitore di pagamenti, così che non faccia mai slittare in silenzio un lancio.

**Grande impresa.** Una banca globale gestisce più di cento team di consegna tra retail, pagamenti e rischio. Tiene una revisione di portafoglio trimestrale in cui un piccolo gruppo esecutivo alloca il finanziamento a una dozzina di temi strategici, ciascuno guidato da una coppia responsabile: un leader di business, un leader di ingegneria. I team sono finanziati in modo persistente, non per progetto. La revisione trimestrale rialloca la capacità tra i temi anziché sciogliere i team. Un registro condiviso delle dipendenze e un evento di pianificazione trimestrale fanno emergere presto i bisogni tra team. Il risultato: meno slittamenti a sorpresa e la capacità di reindirizzare l'investimento entro un trimestre quando le condizioni di mercato cambiano.

**Ente pubblico.** Un'amministrazione fiscale nazionale che modernizza un sistema di dichiarazione vecchio di decenni rifiuta un unico contratto pluriennale monolitico a favore della contrattualizzazione modulare: una sequenza di incrementi più piccoli e indipendentemente preziosi, ciascuno che consegna software funzionante che i cittadini possono usare. Chiede finanziamenti a fasi legate a risultati dimostrati, il che abbassa il rischio di un grande programma fallito. L'amministrazione mantiene un team tecnico interno come acquirente esperto, possiede tutti i dati e le interfacce e scrive esplicite disposizioni di uscita in ogni contratto con i fornitori, così che nessun singolo integratore possa tenere in ostaggio la missione.

## Business case: motivazioni, ROI e TCO

Il ritorno della gestione di portafoglio viene da tre fonti: spreco evitato, consegna di valore più rapida e meno fallimenti di grandi programmi. Lo spreco evitato sono i sistemi duplicati che non costruisci mai e le iniziative di basso valore che non finanzi mai perché una visione di portafoglio ha reso visibile la ridondanza. Il valore più rapido viene dall'eliminare per progetto le dipendenze così che i team smettano di aspettarsi. Il ritorno più grande, però, è la riduzione del rischio. I grandi programmi software falliscono o sforano gravemente a tassi alti e un singolo fallimento pluriennale evitato può far impallidire l'intero costo della funzione di portafoglio.

Il costo di adozione è reale: ruoli di portafoglio e programma, cadenze di pianificazione, strumenti e il tempo di coordinamento che tutto questo consuma. Il costo del *non* adottare è maggiore ma diffuso, e quindi facile da ignorare: spesa non coordinata, [costo irrecuperabile](https://en.wikipedia.org/wiki/Sunk_cost) in lavoro disallineato e il peso composto dei ritardi di dipendenza su ogni iniziativa. Quando presenti il caso alla leadership, imposta la gestione di portafoglio come il meccanismo che trasforma la loro strategia in consegna e li protegge da fallimenti di grandi programmi che stroncano le carriere. Mostra il [costo totale di proprietà](https://en.wikipedia.org/wiki/Total_cost_of_ownership) su costruzione, gestione e sostentamento pluriennale, non solo sulla costruzione iniziale, perché i leader che finanziano solo la costruzione sono sorpresi in modo affidabile dalla gestione.

## Antipattern e insidie

- **Prioritizzazione HiPPO.** Decisioni guidate dall'opinione della persona meglio pagata anziché dall'evidenza o da un quadro concordato.
- **Roadmap come promessa di date.** Pubblicare date lontane come impegni, poi gestire sul calendario anziché sull'esito.
- **Tutto è priorità uno.** Un portafoglio senza no espliciti, così la capacità scarsa è spalmata troppo sottile per finire qualcosa.
- **Cecità alle dipendenze.** Scoprire le dipendenze tra team al momento dell'integrazione anziché della pianificazione.
- **Esternalizzazione a ore.** Comprare ore di appaltatori anziché esiti e perdere la capacità interna di giudicare la qualità.
- **Spesa da usa-o-perdi.** Corse di bilancio di fine anno che finanziano lavoro di basso valore per evitare di restituire gli stanziamenti.
- **OKR come torre di controllo.** Trasformare gli obiettivi in compiti assegnati e metriche di valutazione, distruggendo il segnale onesto che esistono per fornire.
- **Programmi zombie.** Sforzi pluriennali che continuano a essere finanziati per inerzia molto dopo che la loro premessa è fallita.

## Modello di maturità

**Livello 1: Avvio.** Le priorità sono fissate ad hoc e cambiano con chi chiede più forte. Non c'è visione di portafoglio, quindi le dipendenze emergono come crisi al momento dell'integrazione e i sistemi duplicati passano inosservati. I fornitori sono gestiti per volume di contratto anziché per esiti e il finanziamento segue corse di fine anno.

**Livello 2: Sviluppo.** Esiste un inventario di portafoglio rivisto periodicamente, ma la pratica varia da team a team. Gli obiettivi sono pubblicati ma debolmente collegati al lavoro quotidiano; alcuni team tengono un registro delle dipendenze e gestiscono per esiti pochi fornitori mentre altri non fanno né l'uno né l'altro. Il bilancio è prevedibile ma ancora basato sui progetti, così la responsabilità è più chiara della coerenza strategica.

**Livello 3: Standardizzazione.** La strategia scende a cascata ai team attraverso una struttura OKR bassa e un quadro di prioritizzazione documentato è applicato in tutto il portafoglio. Eventi di pianificazione tra team fanno emergere le dipendenze prima che mordano, i team sono finanziati in modo persistente anziché per progetto e la contrattualizzazione modulare con finanziamento incrementale è la norma dell'intera organizzazione anziché un esperimento locale.

**Livello 4: Gestione.** Il portafoglio è misurato rispetto a valori di riferimento, non solo documentato. I leader seguono il movimento degli esiti per tema finanziato, il costo del ritardo sulle iniziative principali, i tassi di slittamento delle dipendenze, la consegna dei fornitori rispetto agli esiti concordati e la quota di spesa impegnata legata a risultati dimostrati. I compromessi di prioritizzazione e i criteri di chiusura sono fatti rispettare su questa evidenza e la varianza tra previsione ed effettivo su costo e calendario guida ogni decisione di finanziamento anziché il patrocinio.

**Livello 5: Orchestrazione.** Portafoglio, programmi e pianificazione del rischio sono integrati e il portafoglio è continuamente riequilibrato man mano che arriva l'evidenza. Le dipendenze sono in gran parte eliminate per progetto attraverso piattaforme e chiari contratti interni, il lavoro dei fornitori e quello interno condividono un'unica visione di valore e rischio e la cadenza di finanziamento corrisponde alla cadenza di apprendimento così che l'organizzazione fermi, reindirizzi o ridefinisca di routine il lavoro senza drammi.

## Spunti di discussione

- Quanto bassa può essere una cascata di OKR prima che smetta di guidare il lavoro, e quanto profonda prima che diventi finzione?
- Quando una formula di prioritizzazione migliora le decisioni, e quando si limita a ripulire la risposta predeterminata di qualcuno?
- I team di piattaforma dovrebbero essere finanziati da un budget centrale o addebitati ai team consumatori, e come cambia questo i loro incentivi?
- In un contesto governativo, fino a che punto potete spingere il finanziamento incrementale e modulare dentro la vigente legge sugli stanziamenti prima di aver bisogno di un cambiamento legislativo?
- Come mantenete il lavoro dei fornitori visibile quanto quello interno senza affogare nell'onere di reportistica?
- Qual è la risposta giusta quando il prodotto di un team durevole perde rilevanza strategica: ridistribuire le persone, o sciogliere e ricostruire?

## Punti chiave

- La gestione di portafoglio converte la strategia in software consegnato decidendo che cosa finanziare, in che ordine, tra molti team.
- Dai priorità per sottrazione e registra i compromessi; un portafoglio che dice sì a tutto non ha strategia.
- Per le grandi organizzazioni, le dipendenze tra team, non lo sforzo di scrittura del codice, sono di solito il vincolo operante; rendile visibili ed eliminale per progetto.
- Finanzia team durevoli e allineati al prodotto e impegna denaro in modo incrementale così che la stabilità delle persone coesista con la flessibilità della direzione.
- Governa i fornitori come parte del portafoglio, mantieni internamente la funzione di acquirente esperto e proteggiti dal lock-in con proprietà dei dati e clausole di uscita.
- Nel governo, struttura i programmi in incrementi indipendentemente preziosi per adattarsi ai cicli di finanziamento pluriennali e ridurre il rischio di fallimento dei grandi programmi.

## Riferimenti e letture di approfondimento

- Donald G. Reinertsen, *The Principles of Product Development Flow*
- Marty Cagan, *Inspired* ed *Empowered*
- John Doerr, *Measure What Matters*
- Christina Wodtke, *Radical Focus: Achieving Your Most Important Goals with OKRs*
- Mik Kersten, *Project to Product*
- Jez Humble, Joanne Molesky e Barry O'Reilly, *Lean Enterprise*
- Project Management Institute, *The Standard for Portfolio Management*
- Axelos, *Managing Successful Programmes (MSP)*
- U.S. Digital Service, *Digital Services Playbook*
- UK Government Digital Service, *Service Manual* e *Technology Code of Practice*
- U.S. Government Accountability Office, *Agile Assessment Guide*
