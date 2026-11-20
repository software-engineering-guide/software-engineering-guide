# 12.3 Modelli

Questi modelli sono punti di partenza pronti da copiare e incollare. Portate qualsiasi modello nel vostro wiki, repository o sistema di ticket e compilate i segnaposto tra parentesi quadre. Le note in corsivo e i commenti in linea spiegano che cosa appartiene a ogni sezione; eliminateli una volta compilata la sezione. Tenete i modelli leggeri: un modello che è più rapido da saltare che da completare non sarà usato. Adattate titoli e sezioni alla vostra organizzazione, ma preservate l'intento di ogni parte.

Alcune convenzioni usate di seguito:

- Il testo tra `[parentesi quadre]` è un segnaposto da sostituire.
- Il testo in _corsivo_ o `<!-- commenti -->` è una guida da eliminare.
- Tenete il documento finito il più breve possibile pur rispondendo alle sue domande.

## Registro di decisione architetturale (ADR)

```markdown
# ADR [NNNN]: [Titolo breve della decisione]

- Stato: [Proposta | Accettata | Deprecata | Sostituita da ADR-XXXX]
- Data: [AAAA-MM-GG]
- Decisori: [nomi o ruoli]
- Consultati: [nomi o ruoli]

## Contesto

<!-- Qual è il problema, la forza o il vincolo che guida questa decisione?
     Enunciate fatti e requisiti in modo neutrale. Includete solo ciò che un
     futuro lettore deve sapere per capire perché serviva una decisione. -->

## Decisione

<!-- Enunciate la scelta in una o due frasi chiare: "Faremo ..." -->

## Alternative considerate

<!-- Elencate le opzioni realistiche valutate e perché ciascuna è stata
     scelta o scartata. Qui dovrebbero comparire almeno due alternative. -->

- Opzione A: [sintesi]; scartata perché [motivo].
- Opzione B: [sintesi]; scartata perché [motivo].
- Opzione scelta: [sintesi]; scelta perché [motivo].

## Conseguenze

<!-- Risultati onesti della decisione, sia buoni sia cattivi. -->

- Positive: [benefici ottenuti]
- Negative: [costi, rischi o limiti accettati]
- Seguito: [migrazioni, nuovo lavoro o decisioni che ne derivano]

## Correlati

<!-- Collegamenti a ADR, RFC, ticket o documenti precedenti correlati. -->
```

## RFC / documento di progetto

```markdown
# RFC: [Titolo]

- Autore/i: [nomi]
- Stato: [Bozza | In revisione | Approvata | Respinta | Implementata]
- Revisori: [nomi o ruoli]
- Creata: [AAAA-MM-GG]
- Ultimo aggiornamento: [AAAA-MM-GG]
- Ticket / tracciamento: [collegamento]

## Sintesi

<!-- Un paragrafo: che cosa propone e perché conta. Un lettore dovrebbe
     cogliere l'essenza da questa sezione soltanto. -->

## Problema e motivazione

<!-- Quale problema stiamo risolvendo? Chi ne è interessato? Che cosa
     succede se non facciamo nulla? Includete contesto e vincoli pertinenti. -->

## Obiettivi e non-obiettivi

- Obiettivi: [che aspetto ha il successo, misurabile dove possibile]
- Non-obiettivi: [esplicitamente fuori ambito, per prevenire l'espansione dell'ambito]

## Progetto proposto

<!-- Il cuore del documento. Descrivete l'approccio, l'architettura, il
     modello dei dati, le interfacce e i flussi chiave. Usate diagrammi dove
     chiariscono. Spiegate come funziona, non solo che cos'è. -->

## Alternative considerate

<!-- Altri approcci e perché non sono stati scelti. Mostra al lettore che lo
     spazio di progetto è stato esplorato. -->

## Impatto e rischi

- Sicurezza e privacy: [implicazioni e mitigazioni]
- Prestazioni e scala: [carico atteso e comportamento]
- Operabilità: [monitoraggio, modalità di guasto, rilascio, rollback]
- Costo: [impatto su infrastruttura o licenze]
- Retrocompatibilità: [migrazione e deprecazione]

## Piano di test e di rilascio

<!-- Come la modifica sarà convalidata e rilasciata in sicurezza. -->

## Questioni aperte

<!-- Questioni irrisolte su cui volete il parere dei revisori. -->
```

## Postmortem / revisione di un incidente (senza colpe)

```markdown
# Postmortem: [Titolo dell'incidente]

- ID incidente: [ID]
- Data dell'incidente: [AAAA-MM-GG]
- Autori: [nomi]
- Stato: [Bozza | Finale]
- Gravità: [SEV1 | SEV2 | SEV3]

> Questa revisione è senza colpe. Ci concentriamo su sistemi e fattori
> contribuenti, non sulle persone. L'obiettivo è imparare e prevenire la
> ricorrenza.

## Sintesi

<!-- Due o tre frasi: che cosa è successo, l'impatto e la risoluzione,
     leggibili da un non esperto. -->

## Impatto

- Durata: [ora di inizio fino all'ora di ripristino, con fuso orario]
- Utenti interessati: [ambito e numero]
- Impatto sul business: [ricavi, SLA, reputazione o altro]

## Cronologia

<!-- Sequenza di eventi con data e ora, fattuale. Includete rilevamento,
     escalation, azioni chiave e ripristino. -->

- [HH:MM] [evento]
- [HH:MM] [evento]

## Fattori contribuenti

<!-- La catena di condizioni che ha portato all'incidente. Preferite
     "fattori contribuenti" a una singola causa radice. -->

## Rilevamento e risposta

- Come è stato rilevato? [allarme, segnalazione del cliente, ecc.]
- Che cosa ha aiutato la risposta?
- Che cosa ha rallentato la risposta?

## Che cosa è andato bene

<!-- Riconoscete le azioni efficaci e le salvaguardie che hanno funzionato. -->

## Azioni

<!-- Specifiche, con responsabile e con scadenza. Affrontate prevenzione,
     rilevamento e mitigazione. Seguitele nel normale arretrato. -->

| Azione | Responsabile | Scadenza | Tipo (prevenire/rilevare/mitigare) | Ticket |
|--------|--------------|----------|------------------------------------|--------|
| [azione] | [nome] | [data] | [tipo] | [collegamento] |

## Lezioni apprese

<!-- Che cosa l'organizzazione più ampia dovrebbe portarsi via. -->
```

## Modello di minaccia (basato su STRIDE)

```markdown
# Modello di minaccia: [Nome del sistema o della funzionalità]

- Autore/i: [nomi]
- Data: [AAAA-MM-GG]
- Revisori: [contatto di sicurezza, responsabili]
- Ambito: [che cosa è e che cosa non è coperto]

## Panoramica del sistema

<!-- Breve descrizione del sistema, del suo scopo e dei suoi utenti. -->

## Beni

<!-- Che cosa vale la pena proteggere: dati, credenziali, funzionalità,
     reputazione. Annotate la sensibilità di ciascuno. -->

## Confini di fiducia e flusso dei dati

<!-- Descrivete o diagrammate componenti, archivi di dati, entità esterne e i
     confini in cui la fiducia cambia. -->

## Minacce (STRIDE)

<!-- Per ogni elemento, considerate le categorie STRIDE. Registrate ogni
     minaccia credibile, il suo rischio e la mitigazione o il rischio accettato. -->

| Minaccia | Categoria STRIDE | Elemento interessato | Rischio (B/M/A) | Mitigazione | Stato |
|----------|------------------|----------------------|-----------------|-------------|-------|
| [minaccia] | Spoofing | [elemento] | [rischio] | [controllo] | [aperta/mitigata/accettata] |
| [minaccia] | Tampering | [elemento] | [rischio] | [controllo] | [stato] |
| [minaccia] | Repudiation | [elemento] | [rischio] | [controllo] | [stato] |
| [minaccia] | Information disclosure | [elemento] | [rischio] | [controllo] | [stato] |
| [minaccia] | Denial of service | [elemento] | [rischio] | [controllo] | [stato] |
| [minaccia] | Elevation of privilege | [elemento] | [rischio] | [controllo] | [stato] |

## Assunzioni e dipendenze

<!-- Assunzioni di sicurezza su cui ci si appoggia e controlli esterni di cui ci si fida. -->

## Questioni aperte e seguito

<!-- Minacce che richiedono ulteriore lavoro, seguite come ticket. -->
```

## Runbook

```markdown
# Runbook: [Nome del compito o dello scenario]

- Servizio: [nome del servizio]
- Responsabile: [team]
- Ultima revisione: [AAAA-MM-GG]
- Allarmi correlati: [nomi degli allarmi]

## Scopo

<!-- Quando usare questo runbook e che cosa ottiene. -->

## Prerequisiti

<!-- Accessi, strumenti e permessi necessari prima di cominciare. -->

## Rilevamento / sintomi

<!-- Ciò che l'operatore osserva: allarmi, firme di errore, dashboard. -->

## Diagnosi

<!-- Controlli passo passo per confermare il problema e restringere la causa.
     Includete i comandi, le query o i collegamenti alle dashboard esatti. -->

1. [passo e risultato atteso]
2. [passo e risultato atteso]

## Risoluzione

<!-- Passi concreti e ordinati per correggere o mitigare. Annotate ogni passo
     rischioso o irreversibile e come verificare il successo. -->

1. [passo]
2. [verificare il ripristino]

## Rollback

<!-- Come annullare le azioni se la risoluzione peggiora le cose. -->

## Escalation

<!-- Chi contattare e quando portare in alto. Reperibilità secondaria, team
     responsabile e contatti dei fornitori. -->

## Riferimenti

<!-- Dashboard, runbook correlati, documenti di architettura. -->
```

## README del servizio / voce del catalogo dei servizi

```markdown
# [Nome del servizio]

- Team responsabile: [team]
- Reperibilità: [collegamento al turno]
- Livello / criticità: [Livello 1 | 2 | 3]
- Repository: [collegamento]
- Stato: [Attivo | Deprecato]

## Che cosa fa

<!-- Un paragrafo sulla responsabilità del servizio e sui suoi consumatori. -->

## Architettura

<!-- Componenti chiave, dipendenze (a monte e a valle) e un collegamento al
     documento di progetto o al diagramma. -->

## Interfacce

- API / endpoint: [collegamento alla specifica]
- Eventi pubblicati / consumati: [argomenti]
- Archivi di dati: [database, cache, bucket]

## Esecuzione e distribuzione

- Ambienti: [dev, staging, prod]
- Come distribuire: [collegamento alla pipeline e processo]
- Configurazione e feature flag: [dove e come]

## Osservabilità

- Dashboard: [collegamenti]
- Allarmi: [collegamenti]
- Log: [dove trovarli]
- SLO: [collegamento]

## Operazioni

- Runbook: [collegamenti]
- Compiti comuni: [scalatura, riavvio, backfill]
- Problemi noti e limiti: [note]

## Per cominciare (per i nuovi contributori)

<!-- Come costruire, testare ed eseguire in locale. -->

## Contatti

- Canale Slack / chat: [collegamento]
- Escalation: [percorso]
```

## Politica di SLO / budget di errore

```markdown
# Politica di SLO e budget di errore: [Nome del servizio o del percorso]

- Responsabile: [team]
- Data di entrata in vigore: [AAAA-MM-GG]
- Cadenza di revisione: [per esempio trimestrale]

## Indicatori di livello di servizio (SLI)

<!-- Definite ogni SLI con precisione: la grandezza misurata, come è misurata
     e da dove (idealmente dal punto di vista dell'utente). -->

| SLI | Definizione | Fonte dei dati |
|-----|-------------|----------------|
| Disponibilità | [per esempio richieste riuscite / richieste totali] | [fonte] |
| Latenza | [per esempio proporzione di richieste sotto X ms] | [fonte] |

## Obiettivi (SLO)

| SLI | Obiettivo | Finestra di misurazione |
|-----|-----------|-------------------------|
| Disponibilità | [per esempio 99,9%] | [per esempio 28 giorni mobili] |
| Latenza | [per esempio 95% sotto 300 ms] | [28 giorni mobili] |

## Budget di errore

<!-- L'inaffidabilità consentita: 100% meno l'obiettivo, sulla finestra.
     Enunciate il budget in termini concreti (per esempio minuti/mese). -->

- Budget: [margine derivato]

## Politica quando il budget è esaurito

<!-- Le conseguenze concordate. Rendetele concrete e applicabili. -->

- [per esempio Congelare i rilasci di funzionalità non critiche finché il budget si ripristina.]
- [per esempio Dare priorità al lavoro sull'affidabilità nel prossimo ciclo di pianificazione.]
- [per esempio Portare in escalation alla leadership di ingegneria se violato per due finestre consecutive.]

## Politica quando il budget è sano

<!-- Quale rischio extra il team può assumere, per esempio rilasci più rapidi. -->

## Allerta

<!-- Allarmi sul tasso di consumo e soglie legati a questo SLO. -->
```

## Voce del registro dei rischi

```markdown
## Rischio: [Titolo breve del rischio]

- ID rischio: [ID]
- Data di segnalazione: [AAAA-MM-GG]
- Responsabile: [nome o ruolo incaricato di gestire questo rischio]
- Categoria: [sicurezza | operativo | conformità | finanziario | consegna | fornitore]
- Stato: [Aperto | In mitigazione | Accettato | Chiuso]

### Descrizione

<!-- Enunciate il rischio come: causa -> evento -> conseguenza. Che cosa
     potrebbe accadere e perché conta. -->

### Valutazione

- Probabilità: [Bassa | Media | Alta]
- Impatto: [Basso | Medio | Alto]
- Valutazione complessiva: [derivata da probabilità x impatto]

### Controlli attuali

<!-- Che cosa riduce già oggi questo rischio. -->

### Piano di mitigazione

<!-- Azioni pianificate per ridurre probabilità o impatto, con responsabili e
     date. Se si accetta il rischio, registrate chi l'ha accettato e perché. -->

| Azione | Responsabile | Scadenza | Stato |
|--------|--------------|----------|-------|
| [azione] | [nome] | [data] | [stato] |

### Revisione

- Data della prossima revisione: [AAAA-MM-GG]
- Decisione / note: [eventuale approvazione di accettazione o modifica]
```

## Scheda di progetto / breve di prodotto

```markdown
# [Nome del progetto o del prodotto]: scheda di una pagina

- Sponsor: [nome]
- Responsabile: [nome]
- Data: [AAAA-MM-GG]
- Stato: [Idea | Approvato | In corso | Rilasciato]

## Problema

<!-- Un paragrafo: il problema del cliente o del business e l'evidenza che sia
     reale e valga la pena risolverlo. -->

## Pubblico

<!-- Chi ha questo problema e chi trae beneficio dal risolverlo. -->

## Soluzione proposta

<!-- Una breve descrizione di ciò che costruiremo o cambieremo. Tenetela al
     livello dell'intento, non del dettaglio di implementazione. -->

## Perché ora

<!-- La ragione per farlo ora anziché più tardi. -->

## Metriche di successo

<!-- Come sapremo che ha funzionato. Preferite esiti misurabili. -->

- [metrica e obiettivo]

## Ambito

- Nell'ambito: [che cosa faremo]
- Fuori ambito: [che cosa non faremo]

## Rischi e questioni aperte

<!-- Principali incertezze e dipendenze. -->

## Piano di massima e tappe

<!-- Fasi di alto livello e tempi approssimativi. -->

## Costi e risorse

<!-- Persone, tempo e bilancio richiesti. -->
```

## Note di passaggio di consegne della reperibilità

```markdown
# Passaggio di consegne della reperibilità: [AAAA-MM-GG]

- Uscente: [nome]
- Entrante: [nome]
- Servizio/i: [nomi]

## Stato generale

<!-- Una riga: tranquillo, rumoroso o problema in corso. -->

## Incidenti aperti

<!-- Qualsiasi incidente attivo o risolto di recente che il prossimo addetto
     deve conoscere, con collegamenti. -->

- [incidente, stato e che cosa resta]

## Modifiche in corso o pianificate

<!-- Distribuzioni, migrazioni, finestre di manutenzione o esperimenti in
     corso che potrebbero causare allarmi. -->

## Allarmi rumorosi o instabili

<!-- Allarmi scattati e il loro vero significato, così che la persona
     successiva non sia fuorviata. Annotate eventuali silenziamenti
     temporanei e la loro scadenza. -->

## Voci da osservare

<!-- Metriche o sistemi che tendono in una direzione preoccupante. -->

## Seguiti in sospeso

<!-- Compiti passati al turno successivo, con collegamenti ai ticket. -->

## Note

<!-- Qualsiasi altra cosa utile: stranezze di accesso, problemi dei fornitori, contesto. -->
```

## Richiesta di modifica (per il controllo delle modifiche regolato)

```markdown
# Richiesta di modifica: [Titolo della modifica]

- ID modifica: [ID]
- Richiedente: [nome]
- Data di presentazione: [AAAA-MM-GG]
- Tipo: [Standard | Normale | Emergenza]
- Priorità: [Bassa | Media | Alta]
- Stato: [Presentata | Approvata | Respinta | Implementata | Chiusa]

## Descrizione della modifica

<!-- Che cosa cambia e perché. Citate il ticket o il requisito. -->

## Sistemi e componenti interessati

<!-- Servizi, dati, ambienti e utenti coinvolti. -->

## Giustificazione e impatto sul business

<!-- La ragione della modifica e l'impatto del non farla. -->

## Valutazione del rischio

- Livello di rischio: [Basso | Medio | Alto]
- Impatto potenziale se la modifica fallisce: [descrizione]
- Impatto su sicurezza, privacy o conformità: [descrizione]

## Piano di implementazione

<!-- Passi ordinati, responsabili e tempi. -->

## Piano di test e di convalida

<!-- Come il successo sarà verificato prima e dopo la modifica. -->

## Piano di ritiro / rollback

<!-- Come invertire la modifica se fallisce e il tempo di ripristino. -->

## Calendario

- Finestra proposta: [inizio e fine, con fuso orario]
- Interruzione prevista: [durata o nessuna]

## Approvazioni

| Ruolo | Nome | Decisione | Data |
|-------|------|-----------|------|
| Responsabile della modifica | [nome] | [approva/respinge] | [data] |
| Revisore tecnico | [nome] | [approva/respinge] | [data] |
| Comitato consultivo delle modifiche | [nome] | [approva/respinge] | [data] |

## Revisione post-implementazione

<!-- Esito, problemi incontrati e se è stato necessario il ritiro. -->
```

## Schema di valutazione d'impatto sulla protezione dei dati (DPIA)

```markdown
# Valutazione d'impatto sulla protezione dei dati: [Nome dell'attività di trattamento]

- Valutatore: [nome]
- Data: [AAAA-MM-GG]
- Revisori: [DPO / contatto privacy]
- Stato: [Bozza | Rivista | Approvata]

## 1. Descrizione del trattamento

<!-- Quali dati personali sono trattati, come, da chi e per quale finalità.
     Includete i flussi di dati dalla raccolta alla cancellazione. -->

- Interessati: [a chi si riferiscono i dati]
- Categorie di dati: [tipi di dati personali, annotate eventuali categorie particolari]
- Finalità: [perché i dati sono trattati]
- Destinatari e responsabili del trattamento: [chi riceve o gestisce i dati]
- Periodo di conservazione: [per quanto i dati sono conservati e metodo di cancellazione]
- Trasferimenti internazionali: [destinazioni e meccanismo di trasferimento]

## 2. Necessità e proporzionalità

<!-- Il trattamento è necessario per la finalità? È l'opzione meno invasiva?
     Qual è la base giuridica o l'autorità? -->

- Base giuridica / autorità: [base per ogni finalità]
- Minimizzazione dei dati: [perché ogni campo è necessario]
- Giustificazione di accuratezza e conservazione: [note]
- Come sono supportati i diritti degli interessati: [accesso, cancellazione, ecc.]

## 3. Consultazione

<!-- Stakeholder e, dove pertinente, interessati consultati. -->

## 4. Rischi per le persone

<!-- Individuate i rischi per la privacy e valutate ciascuno. -->

| Rischio per le persone | Probabilità | Gravità | Complessivo |
|------------------------|-------------|---------|-------------|
| [per esempio accesso non autorizzato a dati sensibili] | [B/M/A] | [B/M/A] | [valutazione] |

## 5. Misure per ridurre il rischio

<!-- Per ogni rischio, la mitigazione e il rischio residuo dopo di essa. -->

| Rischio | Misura | Rischio residuo | Accettato da |
|---------|--------|-----------------|--------------|
| [rischio] | [controllo] | [B/M/A] | [nome] |

## 6. Esito e approvazione

- Rischio residuo accettabile: [Sì | No]
- Misure approvate da: [nome, ruolo]
- Consultazione con l'autorità di controllo richiesta: [Sì | No]
- Data di revisione: [AAAA-MM-GG]
```
