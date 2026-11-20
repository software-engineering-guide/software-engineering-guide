# 12.6 Roadmap di adozione

Questa appendice è una guida pratica per introdurre le pratiche di questo libro
in modo *incrementale*. L'istruzione singola più importante dell'intera guida,
ripetuta in ogni capitolo, è **adotta in modo incrementale; non fare big-bang**.
Una trasformazione che cerca di cambiare tutto in una volta non cambia nulla in
modo duraturo: esaurisce la benevolenza, sommerge i team e collassa alla prima
crisi. Una trasformazione che parte da un dolore reale, consegna una vittoria
visibile e si compone da lì può muovere un'organizzazione di migliaia di persone
nell'arco di pochi anni.

Questa roadmap vi dà principi di adozione, una sequenza basata sulla maturità dai
primi 90 giorni a oltre due anni, un quadro di prioritizzazione con un esempio
svolto, vittorie rapide dominio per dominio, indicazioni speciali per impresa e
governo, modi per misurare il successo e le modalità di fallimento da evitare.

## Principi di adozione

Questi principi valgono a prescindere da dimensione, settore o maturità di partenza.

- **Parti dal dolore, non da un quadro di riferimento.** Trova la cosa che fa
  più male, che siano rilasci lenti, interruzioni frequenti, audit falliti o
  abbandono del personale, e correggi quella per prima. Il dolore crea la domanda
  e la copertura politica che un mandato dall'alto non può mai creare. Nessuno
  resiste al sollievo.
- **Strade asfaltate anziché mandati.** Rendi il modo raccomandato il modo *più
  facile*. Un golden path più rapido, più sicuro e meglio documentato conquista
  l'adozione per merito; una politica più lenta della scorciatoia verrà aggirata.
  Investi nella strada asfaltata prima di deprecare il sentiero sterrato.
- **Misura gli esiti, non l'attività.** Segui se il cambiamento ha migliorato
  consegna, affidabilità, postura di sicurezza o esiti per gli utenti, non quanti
  team hanno frequentato la formazione o spuntato una casella. Strumenta prima di
  cambiare così da poter provare l'effetto.
- **Assicurati uno sponsor esecutivo e mantienilo.** Un cambiamento duraturo ha
  bisogno di un dirigente responsabile che protegga il finanziamento, rimuova gli
  ostacoli e tenga la linea quando la trasformazione diventa scomoda. Lo sponsor
  non è un evento di lancio; è una relazione continua che devi riconquistare con i
  risultati.
- **Volontari prima dei coscritti.** Comincia con i team che *vogliono* cambiare.
  Il loro successo diventa la storia di riferimento che attira la maggioranza
  riluttante. Forzare per primi i resistenti produce conformità malevola e storie
  di avvertimento.
- **Rendilo reversibile dove puoi.** Preferisci i cambiamenti che puoi pilotare,
  misurare e annullare. Le decisioni reversibili "a porta bidirezionale" possono
  muoversi in fretta; riserva il processo pesante a ciò che è davvero irreversibile.
- **Mostra vittorie presto e spesso.** Rilascia qualcosa di visibile in settimane,
  non in trimestri. Lo slancio è una risorsa; spendi la prima vittoria per
  finanziare la successiva.
- **Incontra i team dove sono.** Una singola asticella di maturità applicata
  uniformemente è ingiusta e demoralizzante. Ordina in base alla prontezza e al
  dolore di ciascun team.

## Sequenza basata sulla maturità

Gli orizzonti qui sotto sono cumulativi: ciascuno si costruisce sul precedente.
Le date sono indicazioni, non scadenze; un'organizzazione grande o fortemente
regolata può far durare ogni fase più a lungo. Lo schema (*stabilizzare, poi
standardizzare, poi scalare, poi sostenere*) vale a prescindere dal ritmo.

### Primi 90 giorni: Stabilizzare e dimostrare

Obiettivo: stabilire un valore di partenza, scegliere uno o due problemi di punta
e consegnare una prima vittoria credibile con un team volenteroso.

- [ ] Nominare uno sponsor esecutivo responsabile e una piccola coalizione guida.
- [ ] Misurare il valore di partenza delle quattro metriche DORA (frequenza di
      distribuzione, tempo di attesa, tasso di fallimento delle modifiche, tempo di
      ripristino) anche se i numeri sono approssimativi.
- [ ] Eseguire una valutazione leggera rispetto ai modelli di maturità del
      capitolo 12.4 per trovare i divari maggiori.
- [ ] Scegliere uno o due team pilota che si *offrono volontari* e hanno un dolore reale.
- [ ] Correggere un problema molto visibile da un capo all'altro (per esempio
      automatizzare la distribuzione di un team, o aggiungere SLO a un servizio critico).
- [ ] Mettere in piedi un registro condiviso delle decisioni (ADR) e un posto dove
      pubblicare i risultati.
- [ ] Concordare come misurerete il successo *prima* di cambiare qualsiasi cosa.

### Entro 6 mesi: Standardizzare lo schema vincente

Obiettivo: trasformare il successo del pilota in uno schema ripetibile e
documentato e offrirlo come strada asfaltata alla prossima coorte di team.

- [ ] Pubblicare il golden path del pilota come modelli, pipeline e documentazione riusabili.
- [ ] Istituire un team di piattaforma o abilitante (anche virtuale) che possieda e
      sostenga la strada asfaltata.
- [ ] Estendere lo schema da tre a cinque team in più, dando priorità per impatto e prontezza.
- [ ] Introdurre cancelli automatici di qualità e sicurezza (linting, test,
      SAST/SCA) nella pipeline condivisa come predefiniti, non come aggiunte.
- [ ] Avviare una pratica di revisione degli incidenti senza colpe e pubblicare
      internamente i postmortem.
- [ ] Istituire un leggero forum di governance (revisione dell'architettura,
      cura della strada asfaltata) che sblocca anziché sorvegliare il cancello.

### Entro 12 mesi: Scalare in tutta l'organizzazione

Obiettivo: rendere la strada asfaltata il predefinito per la maggior parte del
nuovo lavoro e cominciare a ritirare le peggiori pratiche legacy.

- [ ] Ampliare il mandato del team di piattaforma; pubblicare un catalogo dei servizi e schede di valutazione.
- [ ] Fissare valori di riferimento a livello di organizzazione: SLO per i servizi
      di livello 1, controlli di sicurezza in ogni pipeline, controlli di
      accessibilità nelle build front-end.
- [ ] Seguire i tassi di adozione per team e rendere visibili i dati.
- [ ] Avviare una modernizzazione deliberata dei sistemi legacy a più alto rischio
      usando i pattern strangler-fig e branch-by-abstraction.
- [ ] Integrare la misurazione nella pianificazione: i team rivedono le tendenze
      DORA e di affidabilità nel normale ritmo operativo.
- [ ] Investire nell'abilitazione (formazione interna, mentoring, comunità di
      pratica) così che la capacità si diffonda più in fretta dei mandati.

### Oltre 2 anni: Sostenere e migliorare di continuo

Obiettivo: le pratiche sono "come lavoriamo", non un programma, e l'organizzazione
le migliora senza spinta centrale.

- [ ] Ritirare il programma di trasformazione come iniziativa nominata; incorporare
      il suo lavoro nella normale governance e nelle operazioni di piattaforma.
- [ ] Trattare la strada asfaltata come un prodotto con la propria roadmap, utenti
      e metriche di soddisfazione (sondaggi sull'esperienza degli sviluppatori).
- [ ] Gestire debito tecnico e modernizzazione come portafoglio permanente, non
      come spinta una tantum.
- [ ] Eseguire rivalutazioni periodiche della maturità e alzare gli standard man
      mano che il pavimento sale.
- [ ] Guardarsi dalla regressione: mantenere lo sponsor, continuare a misurare e
      rinfrescare le pratiche man mano che evolvono tecnologia e minacce.

## Un quadro di prioritizzazione

Avrete sempre più miglioramenti da fare che capacità di farli. Date priorità con
un modello semplice e difendibile anziché con la voce più forte della stanza.

Assegnate un punteggio a ogni iniziativa candidata su tre dimensioni:

- **Impatto (1–5):** Quanto migliorerà un esito reale (velocità di consegna,
  affidabilità, sicurezza, costo o valore per l'utente) e per quanti team o utenti?
- **Sforzo (1–5):** Quanto lavoro, coordinamento e perturbazione servono per
  consegnarla? (Più alto = più sforzo.)
- **Peso del rischio (0,5–2,0):** Un moltiplicatore per urgenza ed esposizione.
  Sicurezza, conformità e questioni di sicurezza fisica portano un peso più alto; le
  cose carine da avere ne portano meno.

Un utile punteggio di ordinamento è:

```
Priorità = (Impatto × Peso del rischio) ÷ Sforzo
```

Ordinate per priorità decrescente. Sequenziate le voci in cima, ma tenete sempre
in corso almeno una "vittoria rapida" veloce e a basso sforzo per sostenere lo
slancio e rivedete i punteggi ogni trimestre man mano che le condizioni cambiano.

### Esempio svolto

| Iniziativa | Impatto | Sforzo | Peso del rischio | Priorità | Sequenza |
|---|---|---|---|---|---|
| Automatizzare la distribuzione per il servizio principale per ricavi | 5 | 2 | 1,5 | 3,75 | Ora |
| Aggiungere SLO e allerta ai servizi di livello 1 | 4 | 2 | 1,5 | 3,00 | Ora |
| Introdurre SAST/SCA nella pipeline condivisa | 4 | 2 | 2,0 | 4,00 | Ora |
| Estendere un sistema di design a tutti i front-end | 4 | 5 | 1,0 | 0,80 | Più tardi |
| Migrare i batch mainframe al cloud | 5 | 5 | 1,5 | 1,50 | A fasi |
| Standardizzare gli ADR tra i team | 3 | 1 | 1,0 | 3,00 | Ora (vittoria rapida) |
| Adottare un nuovo linguaggio di programmazione in tutta l'organizzazione | 2 | 5 | 0,5 | 0,20 | Rinviare |

In questo esempio, il lavoro sulla pipeline di sicurezza è in cima all'elenco per
il suo alto peso del rischio e lo sforzo modesto, mentre il cambio di linguaggio
in tutta l'organizzazione finisce in fondo nonostante l'entusiasmo, perché il suo
impatto è basso e il suo sforzo e la sua perturbazione sono alti. Il quadro rende
esplicito e discutibile quel compromesso, che è il suo vero valore.

## Vittorie rapide dominio per dominio

Ogni parte del libro ha un primo passo a basso costo e ad alto segnale. Partite da qui.

| Parte | Vittoria rapida "parti da qui" |
|---|---|
| **Fondamenti (cultura, team, processo)** | Adottate ADR leggeri ed eseguite una retrospettiva senza colpe; rendete visibili decisioni e apprendimento. |
| **Mestiere della programmazione** | Attivate un formattatore automatico e un linter in CI come predefiniti imposti, così che lo stile smetta di essere un tema di revisione. |
| **Architettura** | Scrivete una decisione architetturale di una pagina e un diagramma di contesto C4 per il vostro sistema più importante. |
| **Sicurezza** | Aggiungete scansione delle dipendenze (SCA) e dei segreti alla pipeline; abilitatele prima per un repository critico. |
| **UX / design** | Eseguite tre economici test di usabilità sul vostro flusso a più alto traffico; correggete il problema principale che osservate. |
| **IA / ML** | Scrivete un inquadramento del problema di una pagina e un controllo di prontezza dei dati prima di qualsiasi lavoro sul modello; definite come valuterete il successo. |
| **Dati / analisi** | Definite un'unica metrica "stella polare" concordata e una dashboard affidabile; ritirate una in conflitto. |
| **DevOps / piattaforma** | Portate un team a una pipeline di build-test-distribuzione completamente automatica e documentatela come modello. |
| **Operazioni / affidabilità** | Definite gli SLI e uno SLO per il vostro percorso utente più critico; allertate sui sintomi, non sulle cause. |
| **Impresa / governo** | Mappate i vostri controlli attuali su un quadro (NIST CSF, ISO 27001 o SOC 2) e automatizzate l'evidenza per un controllo. |

## Indicazioni speciali per l'impresa

Le grandi organizzazioni consolidate portano scala, molti team, un profondo
legacy e un pesante onere di gestione del cambiamento. Adattate la roadmap di conseguenza.

- **Federate, non centralizzate tutto.** Un singolo team centrale non può servire
  centinaia di team di prodotto. Usate un team di piattaforma per fornire strade
  asfaltate e team abilitanti per fare da guida, mentre i team di prodotto
  mantengono la titolarità. (Vedi Team Topologies.)
- **Rispettate la legge di Conway.** La vostra architettura rispecchierà il vostro
  organigramma. Se volete servizi disaccoppiati, vi servono team disaccoppiati e
  autorizzati; riorganizzate deliberatamente anziché combattere contro la venatura.
- **Trattate il legacy come un portafoglio.** Non potete modernizzare tutto.
  Ordinate i sistemi legacy per rischio e valore di business e applicate la
  migrazione strangler-fig ai pochi che contano; congelate o dismettete
  deliberatamente il resto.
- **La gestione del cambiamento è lavoro vero.** Su larga scala comunicazione,
  formazione e allineamento degli incentivi non sono onere: sono la trasformazione.
  Mettete a bilancio esplicitamente abilitazione, comunità di pratica ed
  evangelizzazione interna.
- **Diffidate del riflesso del mandato.** Le grandi organizzazioni ricorrono per
  impostazione predefinita a promemoria di politica. Resistete. Un mandato senza
  strada asfaltata produce spunta-caselle; una strada asfaltata senza mandato
  produce adozione genuina.
- **Allineate incentivi e finanziamento.** Passate dal finanziamento a progetto a
  team di prodotto durevoli così che i miglioramenti sopravvivano oltre la data di
  fine di un progetto. Premiate gli esiti, non la produzione.

## Indicazioni speciali per il governo

Le organizzazioni del settore pubblico aggiungono cicli di appalto, cancelli di
conformità, gestione degli appaltatori, finanziamenti pluriennali e obblighi di
trasparenza. Sono input di progetto, non scuse.

- **Progettate per l'ATO fin dal primo giorno.** I cancelli di autorizzazione a
  operare e di monitoraggio continuo (secondo NIST RMF / 800-37) possono dominare
  i tempi. Incorporate presto nella pipeline controlli di sicurezza e raccolta di
  evidenze così che la conformità sia continua, non un affannarsi tardivo e bloccante.
- **Acquistate in modo incrementale.** Gli appalti pluriennali big-bang
  istituzionalizzano il fallimento big-bang di cui questo libro mette in guardia.
  Preferite contratti modulari, aggiudicazioni più piccole e capitolati basati
  sugli esiti che permettono di iterare.
- **Gestite fornitori e integratori come parte del team.** Gran parte
  dell'ingegneria governativa è consegnata da appaltatori. Scrivete strade
  asfaltate, cancelli di qualità e requisiti di trasparenza nei contratti e
  assicurate che conoscenza e codice passino al governo per evitare lock-in e
  rischio di bus factor.
- **Pianificate attorno ai cicli di finanziamento.** Gli stanziamenti pluriennali
  e annuali limitano ciò a cui potete impegnarvi. Ordinate il lavoro così che ogni
  incremento finanziato consegni valore autonomo e non vi lasci bloccati a metà
  trasformazione se i finanziamenti si spostano.
- **Accessibilità e linguaggio semplice sono obblighi di legge.** Section 508, ADA,
  WCAG e mandati di linguaggio semplice sono requisiti, non miglioramenti.
  Incorporate controlli di accessibilità nelle pipeline e la revisione dei
  contenuti nel flusso di lavoro.
- **La trasparenza è una funzionalità.** FOIA, mandati open source ("denaro
  pubblico, codice pubblico") e standard di servizio pubblicati significano che il
  vostro lavoro è soggetto all'esame pubblico. Progettate per esso: registri
  chiari, aperti dove appropriato e dati di prestazione pubblicati onestamente.
- **Seguite pattern collaudati del settore pubblico.** Il U.S. Digital Services
  Playbook, il GOV.UK Service Standard e USWDS codificano lezioni duramente
  conquistate; adottateli anziché reinventare.

## Misurare il successo dell'adozione

Misurate sia gli indicatori *anticipatori* (segnali precoci che il cambiamento sta
attecchendo) sia quelli *ritardati* (gli esiti che vi interessano in definitiva).
Osservate la tendenza, non una singola lettura, e non lasciate mai che una
metrica diventi un obiettivo da manipolare.

| Tipo | Indicatore | Che cosa vi dice |
|---|---|---|
| Anticipatore | Numero di team sulla strada asfaltata | Quanto in fretta si diffonde l'adozione |
| Anticipatore | Copertura dei cancelli della pipeline (test, SAST, a11y) | Quanto qualità e sicurezza si sono radicate |
| Anticipatore | Punteggi del sondaggio sull'esperienza degli sviluppatori | Se la strada asfaltata aiuta davvero |
| Anticipatore | Percentuale di decisioni catturate come ADR | Se la cultura della scrittura e dell'apprendimento è reale |
| Ritardato | Frequenza di distribuzione (DORA) | Produttività di consegna |
| Ritardato | Tempo di attesa per le modifiche (DORA) | Velocità dal commit alla produzione |
| Ritardato | Tasso di fallimento delle modifiche (DORA) | Qualità del processo di consegna |
| Ritardato | Tempo di ripristino del servizio (DORA) | Resilienza operativa |
| Ritardato | Tendenza di frequenza e gravità degli incidenti | Miglioramento dell'affidabilità nel tempo |
| Ritardato | Rilievi di audit / fallimenti dei controlli | Postura di conformità |
| Ritardato | Fidelizzazione e abbandono del personale | Se la cultura sta migliorando |

Le quattro metriche DORA sono le misure di esito tra i settori più convalidate
per la consegna; trattate il miglioramento su tutte e quattro insieme come segnale
principale e guardatevi dal migliorarne una sacrificandone un'altra.

## Modalità di fallimento comuni e come evitarle

| Modalità di fallimento | Che aspetto ha | Come evitarla |
|---|---|---|
| **Rilascio big-bang** | Cambiare tutto per tutti insieme; il programma collassa sotto il proprio peso. | Ordinare per dolore e prontezza; pilotare, dimostrare, poi scalare. |
| **Mandato senza strada asfaltata** | La politica richiede il nuovo modo, ma il nuovo modo è più lento; i team si conformano sulla carta e lo aggirano. | Costruire *prima* il percorso più facile e migliore; guadagnare l'adozione per merito. |
| **Culto cargo di un quadro** | Copiare SAFe, il modello Spotify o la struttura di un'altra organizzazione senza il loro contesto. | Partire dal proprio dolore e dai propri principi; adattare, non trapiantare. |
| **Misurare l'attività, non gli esiti** | Festeggiare la formazione completata e le caselle spuntate mentre consegna e affidabilità non si muovono. | Strumentare gli esiti (DORA, incidenti, valore per l'utente) fin dall'inizio. |
| **Trasformazione che parte dallo strumento** | Comprare una piattaforma e aspettarsi che la cultura segua. | Guidare con pratiche e strade asfaltate; gli strumenti le servono, non viceversa. |
| **Perdere lo sponsor** | Il paladino esecutivo se ne va o si disimpegna; il programma si blocca. | Istituzionalizzare il cambiamento nella normale governance; costruire una coalizione, non un singolo punto di fallimento. |
| **Metriche di vanità e manipolazione** | I numeri di copertura o velocità salgono mentre la qualità scende. | Usare le metriche come segnali con misure di bilanciamento; mai come uniche obiettivi. |
| **Far bollire l'oceano sul legacy** | Cercare di modernizzare tutto, non consegnando nulla. | Ordinare per rischio e valore; strozzare i pochi critici, congelare il resto. |
| **Fatica da trasformazione** | Cambiamento senza fine e senza ritorno visibile; i team si disimpegnano. | Rilasciare vittorie precoci; proteggere il ritmo sostenibile; lasciare che il programma finisca e diventi lavoro normale. |
| **Ignorare l'organigramma** | La nuova architettura combatte la struttura dei team esistente. | Applicare la manovra di Conway inversa: modellare i team sull'architettura che si vuole. |

## La versione più breve possibile

Se non ricordate nient'altro di questa appendice:

1. Trovate il dolore maggiore e correggetelo con un team volenteroso.
2. Trasformate quella correzione in una strada asfaltata che sia davvero più facile del vecchio modo.
3. Misurate l'esito, mostrate la vittoria e usatela per finanziare il passo successivo.
4. Ripetete, allargando il cerchio, finché la strada asfaltata è semplicemente come lavorate.
5. Mantenete lo sponsor, continuate a misurare e non fate mai big-bang.

Vedi il **capitolo 12.4** per i modelli di maturità che ancorano le valutazioni e
il **capitolo 12.2** per le liste di controllo di lancio, revisione e audit che
rendono operativo ogni passo.
