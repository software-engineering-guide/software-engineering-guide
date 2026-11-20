# 12.2 Liste di controllo

Queste liste di controllo sono riferimenti rapidi, pratici e pronti all'uso. Copiate qualsiasi lista in un modello di pull request, in una pagina wiki, in un ticket o nell'ordine del giorno di una riunione di revisione e adattate le voci al vostro contesto. Trattate ogni voce come qualcosa che una persona può verificare e a cui può rispondere sì o no. Una lista di controllo è un aiuto della memoria e uno standard condiviso, non un sostituto del giudizio; eliminate le voci che non si applicano e aggiungete quelle che il vostro dominio richiede.

Indicazioni per usarle bene:

- Tenete le liste abbastanza corte da essere davvero completate. Se una lista è abitualmente saltata, è troppo lunga o troppo generica.
- Automatizzate qualsiasi voce che una macchina può verificare (formattazione, test, scansioni) così che gli umani spendano attenzione sulle voci di giudizio.
- Versionate le vostre liste e rivedetele periodicamente. Una lista che non cambia mai probabilmente non viene usata.
- Distinguete le voci bloccanti da quelle consultive quando la distinzione conta per il vostro processo.

## Lista di controllo per la revisione del codice

Per il revisore che esamina la modifica di qualcun altro.

- [ ] La modifica fa ciò che dicono la sua descrizione e il ticket collegato.
- [ ] L'ambito è focalizzato su una singola questione logica; le modifiche non correlate sono separate.
- [ ] Il progetto si inserisce nell'architettura esistente e non introduce un accoppiamento facilmente evitabile.
- [ ] Casi limite, percorsi di errore e modalità di guasto sono gestiti, non solo il percorso felice.
- [ ] Esistono test, sono significativi e fallirebbero se il comportamento regredisse.
- [ ] Nomi, struttura e commenti rendono il codice comprensibile a un futuro lettore.
- [ ] Nessun segreto, credenziale, token o dato personale è stato committato.
- [ ] L'input sensibile alla sicurezza è convalidato, codificato o parametrizzato in modo appropriato.
- [ ] Interfacce pubbliche, contratti e retrocompatibilità sono preservati o versionati intenzionalmente.
- [ ] Log, metriche e segnalazione degli errori sono adeguati a gestire la modifica in produzione.
- [ ] Documentazione, runbook e configurazione sono aggiornati in modo coerente con la modifica.
- [ ] Il riscontro è separato in questioni bloccanti e suggerimenti ed è formulato sul codice.

## Lista di controllo per l'autore della pull request

Per l'autore prima di chiedere la revisione.

- [ ] La PR è abbastanza piccola e focalizzata da essere rivista con cura in una sola seduta.
- [ ] La descrizione dichiara che cosa è cambiato, perché e come è stato verificato.
- [ ] Il ticket, la segnalazione o il documento di progetto collegato dà ai revisori il contesto necessario.
- [ ] Tutti i controlli automatici passano in locale o in CI (build, lint, formato, test, scansioni).
- [ ] Il comportamento nuovo e modificato è coperto da test.
- [ ] Le rifattorizzazioni meccaniche sono separate dalle modifiche di comportamento.
- [ ] L'autorevisione è completa: avete letto il vostro diff riga per riga.
- [ ] Non restano codice di debug, blocchi commentati, segreti o file vaganti.
- [ ] Migrazioni di database, feature flag e modifiche di configurazione sono documentate e reversibili.
- [ ] Le modifiche incompatibili sono segnalate esplicitamente con un percorso di migrazione.
- [ ] Schermate, registrazioni o output di esempio sono inclusi dove aiutano la revisione.
- [ ] Sono richiesti i revisori giusti e gli eventuali approvatori per ruolo richiesti.

## Definition of Done

Lo standard condiviso che un elemento di lavoro deve soddisfare prima di essere considerato completo.

- [ ] I criteri di accettazione nel ticket sono tutti soddisfatti e dimostrabili.
- [ ] Il codice è rivisto dai pari e approvato dai revisori richiesti.
- [ ] I test automatici sono scritti, superati e uniti insieme alla modifica.
- [ ] Il codice è unito alla linea principale e si distribuisce senza problemi attraverso la pipeline.
- [ ] Non restano aperti difetti noti della soglia di gravità concordata.
- [ ] Documentazione, testi di aiuto e runbook sono aggiornati.
- [ ] L'osservabilità è in atto: esistono log, metriche e allarmi pertinenti.
- [ ] Le implicazioni di sicurezza e privacy sono state considerate e affrontate.
- [ ] I requisiti di accessibilità per la modifica sono soddisfatti dove è rivolta all'utente.
- [ ] I feature flag sono configurati e il piano di rilascio è concordato.
- [ ] Il responsabile di prodotto o lo stakeholder ha accettato l'esito.
- [ ] Qualsiasi lavoro successivo è catturato come ticket tracciati, non lasciato implicito.

## Prontezza al lancio in produzione / go-live

Prima di rilasciare in produzione una modifica significativa o un nuovo servizio.

- [ ] Il piano di rilascio è documentato, compresi i passi a fasi o canary e i criteri di successo.
- [ ] Il piano di rollback è documentato, testato e può essere eseguito rapidamente.
- [ ] Capacità e test di carico mostrano che il sistema soddisfa la domanda attesa e di picco.
- [ ] Monitoraggio, dashboard e allarmi sono attivi e convalidati prima del lancio.
- [ ] La copertura di reperibilità è pianificata e chi risponde conosce il sistema.
- [ ] Esistono runbook per gli scenari di guasto e operativi più probabili.
- [ ] Dipendenze, integrazioni e terze parti sono confermate pronte e i limiti di frequenza sono compresi.
- [ ] La revisione di sicurezza e le approvazioni richieste sono complete.
- [ ] La migrazione dei dati, se presente, è testata da un capo all'altro con un ritiro verificato.
- [ ] I feature flag permettono di disattivare la modifica senza una ridistribuzione.
- [ ] Le approvazioni legali, di privacy e di conformità sono ottenute dove richiesto.
- [ ] Il piano di comunicazione copre stakeholder, supporto e clienti.
- [ ] Una decisione di procedere o fermarsi è presa da responsabili nominati rispetto a criteri espliciti.

## Lista di controllo per revisione di sicurezza / modello di minaccia

Per valutare la postura di sicurezza di una modifica o di un sistema.

- [ ] Confini di fiducia e flussi di dati sono identificati e documentati.
- [ ] L'autenticazione è imposta su ogni punto di ingresso che la richiede.
- [ ] I controlli di autorizzazione fanno rispettare il minimo privilegio per ogni azione e risorsa.
- [ ] Tutto l'input esterno è convalidato e l'output è codificato per la sua destinazione.
- [ ] I segreti sono archiviati in una cassaforte gestita, mai nel codice o nella configurazione, e sono ruotabili.
- [ ] I dati sono cifrati in transito e a riposo come richiede la classificazione.
- [ ] Le dipendenze sono scansionate per vulnerabilità note e mantenute aggiornate.
- [ ] I rischi di iniezione, deserializzazione e SSRF sono mitigati per l'input non fidato.
- [ ] Gli eventi rilevanti per la sicurezza sono registrati senza registrare dati sensibili.
- [ ] Limitazione della frequenza, quote e protezioni dall'abuso difendono gli endpoint esposti.
- [ ] I messaggi di errore non rivelano stack trace, interni o dettagli sensibili.
- [ ] Le minacce individuate tramite STRIDE o simili sono registrate con mitigazioni o rischio accettato.
- [ ] I test di sicurezza (SAST, DAST o test di penetrazione) sono pianificati o completati.

## Lista di controllo per privacy e protezione dei dati (stile DPIA)

Per i trattamenti che coinvolgono dati personali o sensibili.

- [ ] I dati personali raccolti sono inventariati, classificati e ridotti al necessario.
- [ ] La base giuridica o l'autorità per ogni finalità di trattamento è documentata.
- [ ] La limitazione della finalità è fatta rispettare: i dati sono usati solo per le finalità dichiarate.
- [ ] I periodi di conservazione sono definiti e la cancellazione o anonimizzazione è automatizzata.
- [ ] I diritti degli interessati (accesso, rettifica, cancellazione, portabilità) possono essere soddisfatti.
- [ ] Il consenso, dove usato come base, è libero, specifico e revocabile.
- [ ] Terze parti e responsabili del trattamento sono vincolati da adeguati termini di protezione dei dati.
- [ ] I trasferimenti transfrontalieri hanno un adeguato meccanismo legale di trasferimento.
- [ ] L'accesso ai dati personali è ristretto, registrato e rivisto.
- [ ] I rischi per la privacy delle persone sono valutati e mitigati o portati in escalation.
- [ ] I processi di rilevamento e notifica delle violazioni dei dati sono definiti.
- [ ] Le scelte di privacy fin dalla progettazione e per impostazione predefinita sono documentate per la funzionalità.
- [ ] Il responsabile della protezione dei dati o il revisore della privacy ha approvato dove richiesto.

## Lista di controllo per l'accessibilità (WCAG)

Per le interfacce rivolte all'utente, allineata ai principi WCAG.

- [ ] Tutto il contenuto è raggiungibile e utilizzabile solo con una tastiera.
- [ ] L'ordine del focus è logico ed è presente un indicatore di focus visibile.
- [ ] Il contrasto cromatico del testo soddisfa il rapporto obiettivo (tipicamente 4,5:1 per il testo del corpo).
- [ ] Immagini e contenuti non testuali hanno un testo alternativo significativo.
- [ ] I campi dei moduli hanno etichette associate e messaggi di errore chiari.
- [ ] Titoli, punti di riferimento e struttura sono marcati semanticamente.
- [ ] I componenti interattivi espongono nome, ruolo e stato corretti alle tecnologie assistive.
- [ ] Il contenuto si riorganizza e resta utilizzabile a zoom del 200% e su schermi piccoli.
- [ ] I limiti di tempo sono regolabili e il movimento o i contenuti a riproduzione automatica possono essere messi in pausa.
- [ ] Il colore non è l'unico mezzo per trasmettere informazioni.
- [ ] I contenuti multimediali hanno sottotitoli e, dove serve, trascrizioni o audiodescrizione.
- [ ] L'interfaccia è testata con un lettore di schermo e strumenti automatici di accessibilità.

## Lista di controllo per la revisione del design delle API

Prima di pubblicare o modificare un'API.

- [ ] La denominazione di risorse e operazioni è coerente e prevedibile.
- [ ] Il contratto è specificato in uno schema leggibile da macchina (per esempio OpenAPI).
- [ ] La strategia di versionamento è definita e la retrocompatibilità è preservata o gestita.
- [ ] Paginazione, filtraggio e ordinamento seguono convenzioni coerenti.
- [ ] Le risposte di errore usano struttura, codici e messaggi azionabili coerenti.
- [ ] Autenticazione e autorizzazione sono specificate per ogni operazione.
- [ ] Convalida dell'input e limiti di dimensione sono definiti e fatti rispettare.
- [ ] L'idempotenza è definita per le operazioni in cui sono attesi ritentativi.
- [ ] Limiti di frequenza, quote e comportamento di throttling sono documentati.
- [ ] Timeout, ritentativi e semantica dei fallimenti sono chiari ai client.
- [ ] L'esposizione di dati sensibili nelle risposte è ridotta al minimo e giustificata.
- [ ] La documentazione include esempi per ogni operazione e caso di errore.
- [ ] La politica di deprecazione e le scadenze di dismissione sono definite.

## Lista di controllo per la revisione di una decisione architetturale (ADR)

Per rivedere un registro di decisione architetturale proposto.

- [ ] Il contesto e il problema da risolvere sono enunciati con chiarezza.
- [ ] La decisione è enunciata senza ambiguità come una singola scelta.
- [ ] Almeno due alternative realistiche sono state considerate e confrontate.
- [ ] Le conseguenze, positive e negative, sono documentate.
- [ ] Gli impatti non funzionali (prestazioni, sicurezza, costo, operabilità) sono affrontati.
- [ ] La decisione si allinea ai principi esistenti e agli ADR precedenti, o li sostituisce esplicitamente.
- [ ] I team e gli stakeholder interessati sono stati consultati.
- [ ] La reversibilità e il costo del cambiamento sono valutati.
- [ ] Assunzioni e vincoli sono resi espliciti.
- [ ] Lo stato (proposto, accettato, sostituito) è fissato e datato.
- [ ] La decisione è reperibile e collegata dai sistemi pertinenti.
- [ ] Eventuali azioni successive o migrazioni sono catturate come lavoro tracciato.

## Lista di controllo per la risposta agli incidenti

Durante un incidente attivo in produzione.

- [ ] Dichiarate l'incidente e assegnate un unico responsabile dell'incidente.
- [ ] Valutate e comunicate gravità, ambito e impatto sui clienti.
- [ ] Aprite un canale di comunicazione dedicato e una registrazione dell'incidente.
- [ ] Assegnate ruoli chiari: responsabile, responsabile delle comunicazioni e responsabile delle operazioni.
- [ ] Date priorità alla mitigazione e al ripristino del servizio rispetto all'analisi della causa radice.
- [ ] Pubblicate aggiornamenti di stato regolari agli stakeholder con una cadenza stabilita.
- [ ] Catturate una cronologia di eventi, azioni e decisioni man mano che accadono.
- [ ] Portate in escalation verso ulteriori addetti o fornitori quando serve.
- [ ] Avvisate ufficio legale, sicurezza e conformità se sono coinvolti dati o normative.
- [ ] Verificate la correzione e confermate che il sistema si è ripristinato completamente.
- [ ] Chiudete formalmente l'incidente e comunicate la risoluzione.
- [ ] Pianificate il postmortem senza colpe prima che le persone si disperdano.

## Lista di controllo per il postmortem

Per la revisione retrospettiva dopo un incidente.

- [ ] La revisione è senza colpe e si concentra su sistemi e fattori contribuenti.
- [ ] Una cronologia fattuale e con data e ora dell'incidente è documentata.
- [ ] L'impatto su clienti e business è quantificato (durata, ambito, costo).
- [ ] Il rilevamento è analizzato: come e quando il problema è stato notato.
- [ ] La risposta è analizzata: che cosa ha aiutato e che cosa ha rallentato il ripristino.
- [ ] Sono individuate le cause contribuenti, non solo un'unica causa radice.
- [ ] È registrato ciò che è andato bene, oltre a ciò che è andato male.
- [ ] Le azioni sono specifiche, assegnate a responsabili e hanno scadenze.
- [ ] Le azioni affrontano prevenzione, rilevamento e mitigazione.
- [ ] Le voci successive sono seguite fino al completamento nel normale arretrato.
- [ ] Il postmortem è condiviso ampiamente così che gli altri possano imparare da esso.
- [ ] Gli schemi sistemici tra gli incidenti sono rivisti periodicamente.

## Lista di controllo per la prontezza alla reperibilità

Prima che qualcuno prenda un turno di reperibilità.

- [ ] Chi risponde ha accesso a tutti i sistemi, dashboard e strumenti di cui ha bisogno.
- [ ] L'allerta raggiunge chi risponde in modo affidabile ed è testata.
- [ ] I percorsi di escalation e i contatti di reperibilità secondaria sono noti e aggiornati.
- [ ] Esistono runbook per gli allarmi più comuni e più gravi.
- [ ] Chi risponde ha completato l'inserimento o l'affiancamento per questi sistemi.
- [ ] Modifiche recenti, incidenti in corso e problemi noti sono passati di consegna.
- [ ] Le soglie di allarme sono regolate per ridurre al minimo rumore e falsi allarmi.
- [ ] Chi risponde sa come dichiarare un incidente e raggiungere il responsabile.
- [ ] L'accesso alla produzione è possibile dall'ambiente di lavoro di chi risponde.
- [ ] Canali di comunicazione e contatti degli stakeholder sono documentati.
- [ ] Il calendario della reperibilità è pubblicato e la copertura non ha buchi.
- [ ] Compenso, aspettative e limiti di carico per la reperibilità sono chiari.

## Lista di controllo per la definizione degli SLO

Quando si definisce un obiettivo di livello di servizio.

- [ ] Il percorso utente o la capacità che lo SLO protegge è identificato con chiarezza.
- [ ] Gli indicatori di livello di servizio (SLI) sono definiti come grandezze chiare e misurabili.
- [ ] Gli SLI sono misurati dal punto di vista dell'utente dove possibile.
- [ ] L'obiettivo è fissato a un livello di cui gli utenti hanno davvero bisogno, non al 100%.
- [ ] La finestra di misurazione (per esempio 28 giorni mobili) è specificata.
- [ ] Il budget di errore derivato dall'obiettivo è calcolato e compreso.
- [ ] Una politica definisce che cosa succede quando il budget di errore è esaurito.
- [ ] Le fonti di dati per gli SLI sono affidabili e strumentate.
- [ ] L'allerta è legata al tasso di consumo, non solo alle violazioni di soglia.
- [ ] Responsabili e stakeholder concordano che lo SLO è realistico e significativo.
- [ ] Lo SLO è documentato e visibile su una dashboard.
- [ ] Esiste un calendario per rivedere e rivedere gli SLO man mano che il servizio evolve.

## Lista di controllo per la pipeline CI/CD

Per una pipeline di integrazione e consegna continue.

- [ ] Ogni commit innesca una build e un'esecuzione di test automatiche.
- [ ] La pipeline fallisce in fretta e riporta chiaramente i risultati agli autori.
- [ ] Linting, formattazione e analisi statica girano automaticamente.
- [ ] Test unitari, di integrazione e end-to-end pertinenti girano nella pipeline.
- [ ] Scansione di sicurezza e delle dipendenze gira a ogni build.
- [ ] Gli artefatti di build sono versionati, immutabili e archiviati in un registro.
- [ ] I segreti sono iniettati in modo sicuro e mai stampati nei log.
- [ ] Le distribuzioni sono automatiche e ripetibili tra gli ambienti.
- [ ] La strategia di distribuzione (canary, blue-green, rolling) è definita e usata.
- [ ] Il rollback è automatico o un'unica azione documentata.
- [ ] I permessi della pipeline seguono il minimo privilegio e sono verificabili.
- [ ] La configurazione della pipeline è archiviata nel controllo di versione come codice.
- [ ] Provenienza della build e distinta dei materiali del software sono prodotte dove richiesto.

## Lista di controllo per la revisione dell'infrastruttura come codice

Per rivedere l'infrastruttura definita come codice.

- [ ] Le modifiche sono espresse interamente nel codice e applicate attraverso la pipeline.
- [ ] Un piano o l'output di una prova a vuoto è rivisto prima dell'applicazione.
- [ ] Lo stato è archiviato in modo sicuro con blocco per prevenire modifiche concorrenti.
- [ ] Le risorse seguono convenzioni di denominazione, etichettatura e titolarità.
- [ ] Sono usati ruoli e politiche IAM a minimo privilegio, senza caratteri jolly dove evitabile.
- [ ] L'esposizione di rete è ridotta al minimo; nessun accesso pubblico involontario.
- [ ] Segreti e valori sensibili sono referenziati da una cassaforte, non scritti nel codice.
- [ ] La cifratura è abilitata per archiviazione, database e transito.
- [ ] Le modifiche sono idempotenti e sicure da riapplicare.
- [ ] Il raggio d'azione è compreso; le modifiche distruttive sono segnalate.
- [ ] L'impatto sui costi della modifica è considerato.
- [ ] I moduli sono riusabili, versionati e testati.
- [ ] Il rilevamento della deriva è in atto per cogliere modifiche fuori banda.

## Lista di controllo per il rilascio di un modello IA/ML

Prima di rilasciare in produzione un modello di machine learning.

- [ ] L'uso previsto, l'ambito e i limiti del modello sono documentati.
- [ ] Provenienza, licenza e consenso dei dati di addestramento e di valutazione sono verificati.
- [ ] Dati e modello sono versionati e riproducibili.
- [ ] Le prestazioni sono valutate su dati di test rappresentativi e tenuti da parte.
- [ ] Equità e pregiudizio sono valutati tra i sottogruppi pertinenti.
- [ ] Il modello è valutato rispetto a quello in uso o a una base di riferimento.
- [ ] Modalità di guasto, casi limite e comportamento fuori distribuzione sono compresi.
- [ ] Rischi di sicurezza, abuso e output dannosi sono valutati e mitigati.
- [ ] Il monitoraggio di deriva, qualità dei dati e degrado delle prestazioni è in atto.
- [ ] Esiste un rollback o un ripiego su un modello precedente o su un percorso basato su regole.
- [ ] Supervisione umana o ricorso sono previsti per le decisioni di conseguenza.
- [ ] La revisione della privacy copre i dati di addestramento e gli input e output di inferenza.
- [ ] Una scheda del modello o documentazione equivalente è pubblicata per gli stakeholder.

## Lista di controllo per la qualità delle pipeline di dati

Per una pipeline di dati che alimenta analisi o prodotti.

- [ ] Gli schemi dei dati sorgente sono convalidati e le modifiche di schema sono rilevate.
- [ ] L'ingestione gestisce correttamente record in ritardo, duplicati e fuori ordine.
- [ ] I controlli di qualità dei dati (completezza, unicità, intervalli) girano automaticamente.
- [ ] I record falliti sono messi in quarantena e resi visibili, non scartati in silenzio.
- [ ] Le trasformazioni sono testate con input rappresentativi e di casi limite.
- [ ] La pipeline è idempotente e sicura da rieseguire dopo un guasto.
- [ ] Freschezza e latenza degli output sono monitorate rispetto alle aspettative.
- [ ] La provenienza (lineage) è documentata così che i consumatori sappiano da dove vengono i dati.
- [ ] I dati personali e sensibili sono classificati, mascherati o ristretti in modo appropriato.
- [ ] Backfill e rielaborazione sono supportati e documentati.
- [ ] L'allerta avvisa i responsabili di guasti e violazioni di qualità.
- [ ] Le politiche di conservazione e cancellazione sono fatte rispettare sui dati archiviati.
- [ ] I consumatori a valle e gli SLA sono documentati.

## Lista di controllo per l'accoglimento open source e la revisione delle licenze

Prima di adottare un componente open source.

- [ ] La licenza del componente è identificata ed è nell'elenco approvato.
- [ ] Gli obblighi di licenza (attribuzione, copyleft, avvisi) sono compresi e rispettati.
- [ ] La compatibilità della licenza con il vostro modello di distribuzione è confermata.
- [ ] Il progetto è attivamente mantenuto e ha una comunità sana.
- [ ] Le vulnerabilità note sono controllate e la versione è aggiornata.
- [ ] La dipendenza e le sue dipendenze transitive sono inventariate.
- [ ] La postura di sicurezza e la storia degli incidenti passati sono riviste.
- [ ] Il componente soddisfa un bisogno reale senza duplicazione significativa.
- [ ] Il costo di uscita e la sostituibilità del componente sono considerati.
- [ ] Il componente è registrato nella distinta dei materiali del software.
- [ ] Un responsabile nominato è incaricato di seguire aggiornamenti e avvisi.
- [ ] Le politiche di contributo a monte e di fork interni sono rispettate se modificato.

## Lista di controllo per il rischio di fornitori e terze parti

Prima di inserire un fornitore o servizio esterno.

- [ ] L'esigenza di business e i dati a cui il fornitore accederà sono definiti con chiarezza.
- [ ] La postura di sicurezza del fornitore è valutata (certificazioni, audit, questionario).
- [ ] Termini di trattamento dei dati, titolarità e cancellazione all'uscita sono chiari nel contratto.
- [ ] I sub-responsabili e le ubicazioni dei dati del fornitore sono divulgati e accettabili.
- [ ] La conformità alle normative pertinenti è verificata.
- [ ] Disponibilità, supporto e impegni SLA sono documentati.
- [ ] Obblighi e tempi di notifica delle violazioni sono nel contratto.
- [ ] L'accesso è limitato al minimo privilegio e revocabile.
- [ ] La continuità operativa e l'impatto di un fallimento del fornitore sono valutati.
- [ ] Esiste un piano di uscita e di migrazione dei dati per evitare il lock-in.
- [ ] Costi, termini di rinnovo e clausole di variazione del prezzo sono compresi.
- [ ] Il fornitore è aggiunto al registro dei rischi con una data di revisione.

## Lista di controllo per la prontezza alla conformità governativa (stile ATO / FedRAMP)

Per i sistemi che richiedono un'autorizzazione formale a operare.

- [ ] Il confine del sistema e i flussi di dati sono definiti e diagrammati.
- [ ] I dati sono categorizzati per livello di impatto e sensibilità.
- [ ] La base dei controlli applicabile è selezionata e adattata.
- [ ] Un piano di sicurezza del sistema documenta come è implementato ogni controllo.
- [ ] I controlli sono implementati, documentati con evidenza e mappati sul piano.
- [ ] Monitoraggio continuo e scansione delle vulnerabilità sono operativi.
- [ ] Un piano di azione e tappe segue i rilievi aperti fino alla correzione.
- [ ] Controllo degli accessi, registrazione degli audit e gestione delle identità soddisfano i requisiti.
- [ ] La cifratura usa algoritmi approvati e moduli convalidati.
- [ ] Un piano di risposta agli incidenti è documentato e testato.
- [ ] Un piano di contingenza e di disaster recovery è documentato e testato.
- [ ] Una valutazione indipendente o un audit dei controlli è completato.
- [ ] Il funzionario autorizzante dispone della valutazione del rischio necessaria per concedere l'autorizzazione.
- [ ] Gli inneschi di riautorizzazione e la cadenza di autorizzazione continua sono definiti.
