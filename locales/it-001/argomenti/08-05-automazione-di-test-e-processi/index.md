# 8.5 Automazione di test e processi

## Panoramica e motivazioni

L'automazione di test e processi è la pratica di sostituire il lavoro ingegneristico e operativo ripetitivo e manuale con flussi affidabili eseguiti dalle macchine. Sul versante dei test, significa [automazione dei test](https://en.wikipedia.org/wiki/Test_automation): suite di test automatizzate che girano in continuo per verificare correttezza, prestazioni e sicurezza. Sul versante dei processi, si estende al macchinario circostante della distribuzione e delle operazioni del software: raccogliere evidenze di conformità, eseguire runbook operativi, correggere problemi noti e far rispettare controlli di governance, sicurezza e costo. L'idea unificante è semplice. Tutto ciò che si fa ripetutamente e in modo prevedibile dovrebbe essere codificato, così che giri in modo coerente, rapido e senza fatica umana.

Per i grandi team, l'automazione è l'unico modo per impedire che qualità e controllo crollino sotto la scala. Il test manuale non riesce a tenere il passo con centinaia di ingegneri che fanno migliaia di modifiche. Diventa un collo di bottiglia e la sua copertura diventa incoerente e inaffidabile. Soffrono anche le procedure operative manuali. Riavviare un servizio, ruotare una credenziale e raccogliere evidenze di audit diventano tutti lenti e soggetti a errori quando persone stanche li fanno sotto pressione su un grande patrimonio. Automatizzare questo lavoro rende ripetibili gli esiti. Libera anche gli ingegneri esperti perché si concentrino sui problemi che richiedono giudizio e che hanno davvero bisogno di intuizione umana.

Nei contesti aziendali e governativi, l'automazione è anche la chiave per rendere sostenibile la conformità. Le organizzazioni regolamentate devono dimostrare di continuo che i controlli sono in atto e che le evidenze sono raccolte. Farlo a mano è costoso, lento e soggetto a lacune. Automatizzare la raccolta di evidenze e l'applicazione dei controlli trasforma la conformità da un'emergenza periodica in una proprietà continua e verificabile del sistema. Questo approccio di "conformità come codice" riduce il costo e rafforza la garanzia che auditor e regolatori richiedono.

## Principi chiave

- Automatizza il lavoro ripetuto, prevedibile e basato su regole; riserva lo sforzo umano al giudizio.
- Rendi i test automatici veloci, affidabili e deterministici, o saranno ignorati.
- Esegui i test in parallelo e anticipali così che il riscontro resti rapido man mano che la suite cresce.
- Codifica le procedure operative come [runbook](https://en.wikipedia.org/wiki/Runbook) come codice così che siano versionate, testabili ed eseguibili.
- Preferisci un'automazione ben integrata a script fragili che si agganciano ai sistemi dall'esterno.
- Genera automaticamente l'evidenza di conformità come sottoprodotto dei normali flussi di lavoro.
- Tieni un umano nel ciclo per le azioni ad alto rischio; automatizza prima il sicuro e il routinario.

## Raccomandazioni

### Costruisci un'infrastruttura di test veloce, affidabile e parallela

Una suite di test ha valore solo se gli ingegneri si fidano di essa e restituisce un riscontro in fretta. Investi in un'infrastruttura di test che esegua le suite in parallelo su molti worker, così che il tempo totale di orologio resti basso anche quando il numero di test cresce fino alle migliaia. Struttura la suite come una piramide: molti [test unitari](https://en.wikipedia.org/wiki/Unit_testing) veloci, meno test di integrazione e un piccolo numero di test da capo a capo. In questo modo la maggior parte del riscontro arriva in secondi. Elimina senza pietà i test instabili. Un test che fallisce in modo intermittente è peggio di nessun test, perché addestra gli ingegneri a ignorare i fallimenti. Fornisci ambienti di test effimeri e a richiesta così che i test di integrazione e da capo a capo girino su infrastruttura realistica e isolata.

### Automatizza rilascio, conformità e raccolta di evidenze

Estendi l'automazione oltre i test al flusso di rilascio e conformità. Fai produrre automaticamente alla pipeline gli artefatti di cui gli auditor hanno bisogno: registrazioni di chi ha approvato una modifica, quali test sono girati e sono passati, che cosa hanno trovato le scansioni di sicurezza ed esattamente quale artefatto è stato distribuito. Tratta i controlli come codice, così che i controlli richiesti siano fatti rispettare in modo uniforme e i loro risultati registrati. Questa "conformità come codice" trasforma la raccolta di evidenze da una corsa manuale prima di un audit in una registrazione continua e sempre aggiornata. Rende anche osservabile in qualsiasi momento la postura di conformità del sistema.

### Adotta ChatOps e runbook come codice

Codifica le procedure operative come runbook eseguibili tenuti nel controllo di versione, anziché come documenti in prosa che si fanno obsoleti. Dove una procedura è sicura e ben compresa, collegala a un'automazione che possa eseguirla a richiesta. ChatOps porta queste operazioni in un'interfaccia di chat condivisa, così che gli operatori innescano e osservano azioni automatizzate in una conversazione trasparente, collaborativa e registrata. Questo rende le operazioni visibili all'intero team e crea una registrazione automatica di ciò che è stato fatto. Abbassa anche la barriera perché ingegneri meno esperti eseguano le procedure in sicurezza, dato che l'automazione codifica i passi corretti.

### Implementa con cura la correzione automatica

Per i problemi ricorrenti e ben compresi, costruisci una correzione automatica che rilevi una condizione e applichi una soluzione nota, come riavviare un processo fallito, scalare sotto carico, svuotare un disco pieno o far passare un componente su un altro. Parti da correzioni a basso rischio e alta confidenza. Richiedi conferma umana per qualsiasi cosa con raggio d'impatto significativo. La correzione automatica riduce il tempo medio di ripristino ed elimina la fatica ripetitiva da allarmi. Ma deve poggiare su un solido rilevamento e includere salvaguardie, perché un'automazione che agisce su un falso segnale può amplificare un incidente. Registra ogni azione automatica, così che gli operatori mantengano piena visibilità e possano intervenire.

### Colloca correttamente la robotic process automation (RPA)

La [robotic process automation](https://en.wikipedia.org/wiki/Robotic_process_automation) guida interfacce utente e applicazioni esistenti per automatizzare compiti, imitando i clic e le battute di tasti che farebbe un umano. L'RPA ha un posto legittimo come ponte per sistemi preesistenti o di terze parti che non espongono API e non possono essere integrati in altro modo. Usala in modo pragmatico per questi casi, ma conosci i suoi limiti. L'automazione guidata dall'interfaccia è intrinsecamente fragile: si rompe ogni volta che l'interfaccia cambia e non risolve la sottostante mancanza di integrazione. Dove sono disponibili una vera API o un'integrazione, preferiscile. Tratta l'RPA come una soluzione tampone tattica, non come una fondazione strategica, e pianifica di sostituirla man mano che i sistemi si modernizzano.

### Automatizza i controlli di governance, sicurezza e costo

Codifica i controlli organizzativi come verifiche automatiche che girano in continuo: politica come codice per i guardrail dell'infrastruttura, scansione di sicurezza automatica nelle pipeline e rilevamento automatico di anomalie di costo e risorse inattive. Automatizzare la governance rende i controlli uniformi e inaggirabili e scala a un volume di modifiche che la revisione manuale non potrebbe mai coprire. Lo stesso approccio che fa rispettare una politica di sicurezza può segnalare una bolletta cloud fuori controllo o un'etichetta richiesta mancante. La governance passa da un audit manuale periodico a un guardrail automatico continuo.

## Compromessi: vantaggi e svantaggi

| Scelta | Vantaggi | Svantaggi | Adatto a |
|---|---|---|---|
| Test automatici estesi | Riscontro rapido e coerente; abilita il cambiamento | Costo di costruzione e manutenzione; rischio di instabilità | Tutti i team su larga scala |
| Conformità come codice | Evidenza continua e pronta per l'audit | Ingegneria iniziale per codificare i controlli | Organizzazioni regolamentate |
| Runbook come codice + ChatOps | Operazioni ripetibili, visibili e registrate | Sforzo per codificare e mantenere | Team con un vero carico operativo |
| Correzione automatica | Ripristino più rapido; meno fatica | Rischio se il rilevamento è sbagliato | Problemi ricorrenti e ben compresi |
| RPA (automazione dell'interfaccia) | Fa da ponte tra sistemi senza API | Fragile; maschera le lacune di integrazione | Sistemi preesistenti come soluzione tampone |
| Governance automatizzata | Controlli uniformi e inaggirabili | Sforzo di stesura e regolazione delle politiche | Grandi patrimoni governati |

Il compromesso centrale è investimento iniziale contro fatica e rischio continui. L'automazione costa sempre sforzo per essere costruita e mantenuta. Un'automazione costruita male, che siano test instabili, RPA fragile o correzioni innescate da cattivi segnali, può essere peggio di nessuna, perché erode la fiducia o amplifica i fallimenti. La disciplina è triplice: automatizza ciò che è davvero ripetibile e affidabile, investi nel rendere affidabile quell'automazione e tieni gli umani nel ciclo dove giudizio o alto rischio lo richiedono. Fatta bene, l'automazione ripaga molte volte. Fatta con noncuranza, diventa essa stessa una passività.

## Domande da discutere con il tuo team

1. **I vostri test di integrazione e da capo a capo girano su ambienti realistici ed effimeri, o su una macchina di staging condivisa per cui tutti litigano?** Ambienti isolati a richiesta per ogni pull request permettono ai test di integrazione e da capo a capo di esercitare un'infrastruttura realistica senza che i team si blocchino a vicenda o inquinino lo stato condiviso. Un unico ambiente di staging condiviso diventa un collo di bottiglia e una fonte di fallimenti instabili e dipendenti dall'ordine man mano che più team vi si accalcano. Decidete se potete avviare ambienti effimeri, quanto costano e quali test ne hanno davvero bisogno rispetto a un rapido sostituto in memoria. Portate dati: quanto spesso lo staging è conteso, quanti fallimenti risalgono a interferenze dell'ambiente condiviso e il tempo di orologio attuale per lo strato di integrazione. La risposta plasma sia l'affidabilità dei vostri test sia quanto in fretta gli strati superiori della piramide restituiscono riscontro.

2. **Le procedure operative sono codificate come runbook come codice e rese disponibili tramite ChatOps, o vivono ancora come prosa che si fa obsoleta?** I runbook codificati e sotto controllo di versione sono testabili ed eseguibili e farli girare attraverso un'interfaccia di chat condivisa rende ogni azione visibile e registrata automaticamente. Questo abbassa la barriera perché un ingegnere reperibile meno esperto agisca in sicurezza, perché l'automazione codifica i passi corretti anziché affidarsi alla memoria tribale. Decidete quali procedure sono sicure e ben comprese abbastanza da collegare per prime e come mantenete l'umano in grado di intervenire. Per un grande patrimonio questa trasparenza fa anche da registro di audit di chi ha fatto che cosa e quando. Portate i vostri runbook attuali, annotate quali sono obsoleti e individuate le due o tre procedure più eseguite da codificare per prime.

3. **Nella vostra pipeline, quali scansioni di sicurezza e controlli di politica bloccano un merge e quali si limitano ad avvisare?** Vale la pena costruire la governance automatizzata solo se i controlli sono inaggirabili, perché un controllo che si limita ad avvisare viene ignorato sotto pressione di scadenza esattamente come una politica in un wiki. Decidete, controllo per controllo, che cosa blocca e che cosa avvisa: una vulnerabilità critica o un'etichetta di cifratura mancante probabilmente blocca, mentre un rilievo di stile a gravità minore potrebbe avvisare. Su larga scala è così che fate rispettare in modo uniforme i guardrail di sicurezza e costo su un volume di modifiche che nessuna revisione manuale potrebbe coprire. Portate il vostro inventario attuale dei controlli e segnate ciascuno come bloccante o consultivo, poi discutete il tasso di falsi positivi, perché un controllo bloccante rumoroso addestra le persone a pretendere eccezioni. La linea tra bloccare e avvisare è dove la vostra governance ha o non ha i denti.

4. **Quali correzioni automatiche siamo disposti a lasciar agire senza che un umano confermi prima, e qual è il raggio d'impatto se il rilevamento è sbagliato?** La correzione automatica taglia i tempi di ripristino e la fatica da allarmi, ma una correzione innescata da un falso segnale può trasformare un piccolo intoppo in un'interruzione completa, quindi la decisione su che cosa gira senza sorveglianza è una decisione di rischio, non di comodità. Pesate le spinte in competizione: l'azione senza sorveglianza è la più rapida ma la più rischiosa, mentre la conferma con umano nel ciclo è più sicura ma reintroduce il ritardo e la fatica che stavate cercando di rimuovere. Portate le correzioni candidate classificate per frequenza e per raggio d'impatto nel caso peggiore, il tasso storico di falsi positivi del rilevamento dietro ciascuna e se ogni azione è registrata e reversibile. Per un grande patrimonio aziendale o governativo, aggiungete un'autorità formale di modifica e un piano di rollback per qualsiasi cosa tocchi dati di produzione o servizi rivolti ai cittadini, perché una correzione automatica che non può essere verificata né annullata è una che un regolatore vi costringerà a spegnere.

5. **Come finanziamo e assegniamo la responsabilità per mantenere la nostra automazione così che non decada in una passività?** Test, runbook, controlli di politica e bot RPA marciscono tutti man mano che i sistemi circostanti cambiano e un'automazione trascurata è peggio di nessuna: un runbook obsoleto dà falsa fiducia in una crisi e un bot RPA rotto lascia cadere lavoro in silenzio. La tensione è che la manutenzione compete con il lavoro sulle funzionalità per gli stessi ingegneri ed è invisibile finché qualcosa si rompe, quindi è la prima cosa tagliata sotto pressione di scadenza. Portate l'inventario attuale delle risorse di automazione, l'arretrato di test instabili e bot rotti e una stima onesta delle ore di ingegneria che già vanno in manutenzione rispetto a quelle messe a bilancio. In un contesto aziendale o governativo, nominate il responsabile per ogni automazione critica e finanziate la sua manutenzione come voce esplicita, perché auditor e revisioni degli incidenti chiederanno chi era responsabile quando un controllo non mantenuto è fallito in silenzio.

6. **Per ogni sistema preesistente che automatizziamo con RPA, qual è il piano concreto e l'innesco per ritirare quell'RPA a favore di una vera integrazione?** L'RPA è un ponte legittimo per sistemi che non espongono API, ma un ponte senza piano di uscita si indurisce in silenzio in un'infrastruttura permanente e fragile che si rompe a ogni cambio di interfaccia e radica proprio la lacuna di integrazione che doveva colmare. Il compromesso è reale: l'RPA dà valore in fretta e a basso costo adesso, mentre una vera integrazione via API costa di più all'inizio ma è durevole, quindi la disciplina è trattare l'RPA come un prestito datato, non un acquisto. Portate l'elenco dei bot RPA in produzione, i sistemi da cui ciascuno dipende, quanto spesso ciascuno si rompe e se uno sforzo di modernizzazione o integrazione è davvero finanziato e pianificato per il sistema sottostante. Per i patrimoni aziendali e governativi che portano applicazioni centrali vecchie di decenni, legate ogni bot RPA a una tappa nominata di modernizzazione, perché un'RPA diventata in silenzio critica senza data di ritiro è debito tecnico che si compone ogni anno in cui l'interfaccia che raschia continua a cambiare.

## Lente settoriale

**Startup.** Con due o tre ingegneri e nessun tempo per costruire infrastruttura, mantieni una piccola e rapida piramide di test che gira in un paio di minuti a ogni modifica e tratta qualsiasi test instabile come un vero bug da correggere o cancellare in quella settimana. Salta strumenti pesanti di conformità e politica come codice di cui non hai ancora bisogno e codifica solo le tue due o tre correzioni operative più eseguite come semplici script innescati dalla chat. Automatizza ciò che rimuove la fatica quotidiana e resisti a costruire macchinario di governance prima di avere un problema di governance.

**Piccola impresa.** Senza uno specialista di test o di piattaforma dedicato, appoggiati all'automazione incorporata negli strumenti che già paghi: gli esecutori di test integrati del servizio CI, i suoi componenti aggiuntivi di scansione e ambienti gestiti anziché una costruzione su misura di infrastruttura di test. Imposta la scelta tra comprare e costruire attorno a una manutenzione che puoi sostenere in modo realistico, perché una pipeline personalizzata ingegnosa che nessuno sa mantenere è un esito peggiore di una più semplice e ospitata. Usa l'RPA con parsimonia e solo dove uno strumento di un fornitore fa da ponte a un sistema che non puoi integrare in altro modo.

**Grande impresa.** Tra molti team l'obiettivo è dei controlli uniformi e inaggirabili a una scala che la revisione manuale non può coprire: infrastruttura di test parallela condivisa con ambienti effimeri, guardrail di politica come codice ed evidenza di conformità generata automaticamente da ogni esecuzione della pipeline. Standardizza le interfacce così che i team riusino strumenti di correzione e runbook anziché reinventare ciascuno script fragili e gestisci l'automazione come un portafoglio posseduto e finanziato con chiari budget di manutenzione. Bada che un controllo che in un team si limita ad avvisare non sia trattato come bloccante in un altro, perché un'applicazione incoerente mina la garanzia che stai pagando.

**Ente pubblico.** Regole di appalto, obblighi di trasparenza e mandati di monitoraggio continuo rendono la conformità come codice quasi essenziale: ogni esecuzione della pipeline dovrebbe registrare i controlli verificati, le scansioni eseguite e le approvazioni concesse come evidenza a prova di manomissione e pronta per l'audit. Privilegia un'automazione aperta e portabile rispetto al lock-in proprietario così che un contratto futuro possa passare a un altro fornitore e tieni un umano responsabile per qualsiasi correzione che tocchi servizi rivolti ai cittadini. Dove un sistema vecchio di decenni impone l'RPA, documentala come ponte deliberato e temporaneo con un piano pubblico di modernizzazione e tieni i controlli di governance alla base di sicurezza obbligatoria a ogni modifica.

## Esempi

**Startup.** Una startup di sette persone mantiene una piramide di test snella di perlopiù test unitari veloci più pochi test di integrazione, tutti eseguiti in parallelo così che l'intera suite finisca in meno di tre minuti a ogni pull request. Quando un test comincia a essere instabile, lo trattano come un vero bug e lo correggono o lo cancellano in quella settimana, perché con un team così piccolo una singola build rossa ignorata erodererebbe la fiducia nell'intera suite. Codificano anche le loro due correzioni operative più comuni, riavviare un worker bloccato e svuotare un disco pieno, come piccoli script innescati da Slack, così chiunque sia reperibile può eseguirli in sicurezza senza chiamare l'unico ingegnere che li ha scritti.

**Grande impresa.** Una grande azienda di e-commerce gestisce una suite di decine di migliaia di test, parallelizzata su una flotta di worker così che l'intera suite si completi in minuti. Ambienti effimeri si avviano per ogni pull request per test di integrazione realistici. Le operazioni passano per ChatOps: gli ingegneri reperibili innescano runbook codificati dalla chat e i fallimenti comuni come un servizio sovraccarico sono corretti automaticamente, con l'azione registrata per la revisione. La pipeline raccoglie automaticamente evidenza di scansioni di sicurezza e approvazioni, così l'audit annuale attinge a una registrazione sempre aggiornata anziché a una caccia manuale alle evidenze.

**Ente pubblico.** Un'agenzia pubblica soggetta a rigorosi requisiti di monitoraggio continuo implementa la conformità come codice. Ogni esecuzione della pipeline registra i controlli verificati, le scansioni eseguite e le approvazioni concesse, producendo evidenza a prova di manomissione che soddisfa gli auditor su richiesta. Poiché uno dei suoi sistemi centrali è un'applicazione vecchia di decenni senza API, l'agenzia usa l'RPA come ponte deliberato per automatizzare l'inserimento dati in esso mentre procede uno sforzo di modernizzazione, con un piano esplicito di ritirare l'RPA una volta che esiste una vera integrazione. I controlli di governance automatizzati fanno rispettare la base di sicurezza obbligatoria a ogni modifica dell'infrastruttura.

## Business case: motivazioni, ROI e TCO

Il ROI dell'automazione di test e processi compare come tempo di ingegneria recuperato, distribuzione più rapida e sicura, ripristino degli incidenti più veloce e costo di conformità drasticamente inferiore. Il test automatico abilita il cambiamento rapido e sicuro che sostiene le prestazioni di consegna. Operazioni e correzione automatiche tagliano la fatica e il fermo che prosciugano team e budget. La conformità come codice può trasformare un audit da settimane di preparazione manuale in una query di routine, un risparmio sia finanziario sia reputazionale.

Il confronto sul TCO pesa il costo reale e continuo di costruire e mantenere l'automazione contro il costo del non automatizzare. Test e operazioni manuali non costano soltanto le ore spese. Costano anche i difetti che sfuggono, gli incidenti che durano a lungo, gli audit che consumano personale specialistico e l'esaurimento di ingegneri che fanno fatica ripetitiva. Per la leadership, l'argomento è diretto: l'automazione converte la spesa operativa ricorrente e il rischio in un investimento una tantum più manutenzione che scala e rende continue anziché episodiche qualità e conformità. Va detta con chiarezza una cautela. L'automazione deve essere mantenuta e affidabile; un'automazione non finanziata e trascurata decade in una passività.

## Antipattern e insidie

- **Test instabili tollerati.** I fallimenti intermittenti distruggono la fiducia e addestrano gli ingegneri a ignorare i risultati rossi.
- **Automatizzare un processo rotto.** Automatizzare un cattivo flusso di lavoro fa solo accadere il pasticcio più in fretta; correggi prima il processo.
- **RPA come strategia.** Affidarsi a un'automazione fragile dell'interfaccia come soluzione permanente maschera e radica le lacune di integrazione.
- **Correzione senza rilevamento solido.** Le correzioni automatiche innescate da cattivi segnali possono amplificare un incidente.
- **Runbook come prosa obsoleta.** Procedure che vivono in documenti non aggiornati danno falsa fiducia in una crisi.
- **Evidenza di conformità raccolta a mano.** Le cacce manuali periodiche alle evidenze sono costose e lasciano lacune tra un audit e l'altro.
- **Nessun umano nel ciclo per le azioni ad alto rischio.** La piena automazione di operazioni pericolose rimuove il giudizio che previene i disastri.

## Modello di maturità

**Livello 1, Avvio.** Test e operazioni sono in gran parte manuali e reattivi. La copertura è ad hoc, le procedure vivono nella testa delle persone o in documenti obsoleti, la correzione avviene a mano durante gli incidenti e l'evidenza di conformità è assemblata in una corsa prima di ogni audit.

**Livello 2, Sviluppo.** Esistono test automatici ma sono lenti, instabili o eseguiti in modo incoerente e le pratiche variano molto tra i team. Esistono alcuni script operativi e runbook in sacche isolate, ma la correzione è ancora manuale e la governance è fatta rispettare da una revisione periodica anziché da controlli continui.

**Livello 3, Standardizzazione.** Un'infrastruttura di test veloce, parallela e affidabile è lo standard documentato dell'intera organizzazione. Runbook come codice e ChatOps sono in uso generale, l'evidenza di conformità è generata automaticamente dalle esecuzioni della pipeline e i controlli di governance girano come verifiche automatiche fatte rispettare e applicate in modo coerente tra i team.

**Livello 4, Gestione.** L'automazione stessa è misurata e controllata rispetto a valori di riferimento. Segui tasso di test instabili, tempo di orologio della suite, tempo medio di ripristino per gli incidenti corretti automaticamente, quota di controlli con evidenza automatica e tassi di falsi positivi sui controlli bloccanti e tieni ogni metrica a un obiettivo concordato. Le decisioni su correzione e copertura sono guidate da questi dati e ogni azione automatica è registrata così che andamenti e regressioni siano visibili anziché indovinati.

**Livello 5, Orchestrazione.** L'automazione è continuamente migliorata e integrata nell'organizzazione. La correzione automatica gestisce gli incidenti di routine con salvaguardie provate, la conformità è continua e sempre pronta per l'audit e le catene di strumenti di test, operazioni e governance si adattano al mutare dei sistemi, con i ponti RPA attivamente ritirati man mano che le integrazioni maturano. Gli umani si concentrano sul giudizio mentre le macchine gestiscono il ripetibile e l'intero sistema si riequilibra sull'evidenza.

## Spunti di discussione

- Quali procedure operative sono sicure da automatizzare del tutto, e quali devono mantenere un umano nel ciclo?
- Come mantenete veloce e priva di instabilità una grande suite di test man mano che cresce?
- Dove l'RPA è un ponte giustificato per i vostri sistemi preesistenti, e qual è il piano per ritirarla?
- Quali controlli potreste convertire per primi da audit manuale a conformità continua come codice?
- Come costruite fiducia nella correzione automatica senza rischiare incidenti amplificati?
- Come finanziate la manutenzione continua che l'automazione richiede così che non decada in una passività?

## Punti chiave

- Automatizza il ripetuto, il prevedibile e il basato su regole; riserva lo sforzo umano a giudizio e decisioni ad alto rischio.
- Rendi i test automatici veloci, paralleli e affidabili ed elimina senza pietà l'instabilità.
- Codifica le operazioni come runbook come codice e rendile disponibili tramite ChatOps per visibilità e registrazione.
- Genera automaticamente l'evidenza di conformità così che gli audit attingano a una registrazione continua e aggiornata.
- Usa l'RPA solo come ponte deliberato e temporaneo per sistemi senza API e pianifica il suo ritiro.
- Fai rispettare governance, sicurezza e controlli di costo come verifiche automatiche continue, con umani che sorvegliano le azioni rischiose.

## Riferimenti e letture di approfondimento

- Lisa Crispin e Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*.
- Jez Humble e David Farley, *Continuous Delivery*.
- Betsy Beyer, Chris Jones, Jennifer Petoff e Niall Richard Murphy (a cura di), *Site Reliability Engineering* (vedi il capitolo sull'eliminazione della fatica).
- Gene Kim, Jez Humble, Patrick Debois e John Willis, *The DevOps Handbook*.
- Nicole Forsgren, Jez Humble e Gene Kim, *Accelerate*.
- NIST Special Publication 800-53 e 800-137 (monitoraggio continuo).
- Documentazione di Open Policy Agent (politica come codice).
