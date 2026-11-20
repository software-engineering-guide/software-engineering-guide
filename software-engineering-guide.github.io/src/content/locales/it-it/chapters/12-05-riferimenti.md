# 12.5 Riferimenti

Questa sezione consolida l'apparato di riferimento della guida: una tabella di
corrispondenza con il corpo di conoscenze SWEBOK, un indice degli standard e dei
quadri citati in tutto il libro e una bibliografia curata di letture consigliate.
Le fonti di ogni capitolo compaiono anche nella sezione *Riferimenti e letture di
approfondimento* alla fine di ciascun capitolo.

---

# Corrispondenza con SWEBOK

Questa guida è allineata a **SWEBOK V4.0** (Software Engineering Body of
Knowledge) dell'IEEE Computer Society. Tutte e 18 le aree di conoscenza sono
coperte; la tabella mappa ciascuna sui capitoli che la trattano e la guida va poi
ben oltre SWEBOK in IA, dati, UX, DevOps, sostenibilità, flusso e tecnologia di
interesse pubblico.

| Area di conoscenza SWEBOK V4.0 | Capitoli principali |
|---|---|
| 1. Requisiti del software | 2.8, 11.1, 5.1 |
| 2. Architettura del software | 3.1, 3.2, 3.3 |
| 3. Progettazione del software | 2.2, 3.1 |
| 4. Costruzione del software | 2.9, 2.1 |
| 5. Test del software | 2.4, 8.5 |
| 6. Operazioni di ingegneria del software | 9.1, 9.2, 9.3, 8.1 |
| 7. Manutenzione del software | 3.7, 3.6, 10.4 |
| 8. Gestione della configurazione del software | 2.10, 2.6, 8.2 |
| 9. Gestione dell'ingegneria del software | 10.1, 10.6, 10.2 |
| 10. Processo di ingegneria del software | 1.4, 10.7, 10.8 |
| 11. Modelli e metodi di ingegneria del software | 2.12, 3.1, 2.2 |
| 12. Qualità del software | 2.11, 2.4, 3.1 |
| 13. Sicurezza del software | 4.1, 4.2, 4.3, 4.4 |
| 14. Pratica professionale dell'ingegneria del software | 10.5, 1.1, 1.3 |
| 15. Economia dell'ingegneria del software | 10.10, 10.1, 9.4 |
| 16. Fondamenti dell'informatica | 2.13, 3.3, 3.4 |
| 17. Fondamenti matematici | 2.13, 11.3 |
| 18. Fondamenti ingegneristici | 2.13, 3.1 |

---

# Standard e quadri di riferimento

Questa appendice è un indice organizzato degli standard, dei quadri e delle
normative reali citati in tutta la guida. È un ausilio alla navigazione, non un
manuale di conformità: consultate sempre la fonte autorevole e, dove pertinente,
un consulente legale o di audit qualificato per il testo vigente e
l'applicabilità al vostro contesto.

Le voci sono raggruppate per dominio. Ciascuna nomina lo standard o il quadro,
l'ente che lo emette, un ambito in una riga e i capitoli o domini in cui è più
rilevante. Dove un nome è comunemente abbreviato, l'abbreviazione è mostrata. Numeri
di documento e titoli sono dati solo dove ben consolidati; non sono inclusi URL.

## Come usare questa appendice

- Le **normative** (per esempio GDPR, HIPAA) sono legalmente vincolanti nella loro
  giurisdizione e nel loro settore. Fissano obblighi, non solo buona pratica.
- Gli **standard** (per esempio ISO/IEC 27001, WCAG) sono specifiche formali, spesso
  certificabili. Alcuni sono volontari; alcuni sono imposti per legge o per contratto.
- I **quadri** (per esempio NIST CSF, NIST AI RMF) sono indicazioni strutturate,
  di solito volontarie, che adattate al vostro profilo di rischio.
- L'applicabilità dipende da giurisdizione, settore, tipi di dati e termini
  contrattuali. Molte organizzazioni devono soddisfarne diversi contemporaneamente.

## Sicurezza e privacy

| Standard / quadro | Ente emittente | Ambito (una riga) | Capitoli / domini principali |
| --- | --- | --- | --- |
| ISO/IEC 27001 | ISO / IEC | Requisiti per un Sistema di Gestione della Sicurezza delle Informazioni (ISMS). | 4.1–4.6 Sicurezza e conformità |
| ISO/IEC 27002 | ISO / IEC | Indicazioni e insieme di controlli a supporto di ISO/IEC 27001. | 4.1–4.4 Sicurezza |
| ISO/IEC 27017 / 27018 | ISO / IEC | Controlli di sicurezza specifici per il cloud (27017) e protezione delle PII nel cloud (27018). | 4.3 Sicurezza di infrastruttura e cloud; 4.5 Privacy |
| NIST Cybersecurity Framework (CSF) | National Institute of Standards and Technology | Quadro volontario organizzato attorno a Govern, Identify, Protect, Detect, Respond, Recover. | 4.1, 4.4 Fondamenti e operazioni di sicurezza |
| NIST SP 800-53 | National Institute of Standards and Technology | Catalogo di controlli di sicurezza e privacy per i sistemi informativi. | 4.3, 4.6 Sicurezza cloud e conformità |
| NIST SP 800-63 | National Institute of Standards and Technology | Linee guida su identità digitale e garanzia di autenticazione. | 4.2, 4.3 Sicurezza applicativa e di infrastruttura |
| OWASP Top Ten | Open Worldwide Application Security Project | I rischi di sicurezza più critici delle applicazioni web, aggiornati periodicamente. | 4.2 Sicurezza applicativa |
| OWASP ASVS | Open Worldwide Application Security Project | Requisiti e test graduati per verificare la sicurezza applicativa. | 2.4, 4.2 Test e sicurezza applicativa |
| OWASP SAMM | Open Worldwide Application Security Project | Modello di maturità per costruire e valutare un programma di sicurezza del software. | 4.1 Fondamenti e cultura della sicurezza |
| STRIDE | Nato in Microsoft | Tassonomia di modellazione delle minacce per classificarle. | 4.2 Sicurezza applicativa |
| MITRE ATT&CK | MITRE | Base di conoscenza di tattiche e tecniche degli avversari per rilevamento e difesa. | 4.4 Operazioni di sicurezza |
| SLSA | Open Source Security Foundation (OpenSSF) | Quadro graduato per integrità e provenienza della supply chain del software. | 4.2, 8.1, 10.3 Supply chain e consegna |
| SBOM (SPDX / CycloneDX) | Linux Foundation (SPDX); OWASP (CycloneDX) | Formati standard per le distinte dei materiali del software. | 4.2, 10.3 Sicurezza applicativa e licenze |
| PCI DSS | PCI Security Standards Council | Requisiti di sicurezza per il trattamento dei dati delle carte di pagamento. | 4.2, 4.5, 4.6 Sicurezza, privacy, conformità |

## Conformità e governo

### Stati Uniti

| Normativa / quadro | Ente emittente | Ambito (una riga) | Capitoli / domini principali |
| --- | --- | --- | --- |
| HIPAA | US Dept. of Health and Human Services | Salvaguardie per le informazioni sanitarie protette (PHI). | 4.5, 4.6 Privacy e conformità |
| SOX (Sarbanes-Oxley Act) | US Congress / SEC | Requisiti di rendicontazione finanziaria e di controllo interno per le società quotate. | 4.6, 10.2 Conformità e audit |
| FISMA | US Congress | Requisiti di programma di sicurezza delle informazioni per le agenzie federali. | 4.3, 4.6 Sicurezza cloud e conformità |
| FedRAMP | US General Services Administration / FedRAMP PMO | Autorizzazione di sicurezza standardizzata per i servizi cloud usati dalle agenzie federali. | 4.3, 4.6 Sicurezza cloud e conformità |
| NIST SP 800-171 | National Institute of Standards and Technology | Protezione delle informazioni non classificate controllate (CUI) nei sistemi non federali. | 4.6 Conformità (supply chain della difesa) |
| CMMC | US Department of Defence | Certificazione della maturità di cybersicurezza degli appaltatori della difesa. | 4.6 Conformità (difesa) |
| FIPS 140-3 | National Institute of Standards and Technology | Requisiti di sicurezza per i moduli crittografici. | 4.3 Sicurezza di infrastruttura e cloud |
| CCPA / CPRA | State of California | Diritti di privacy dei consumatori e obblighi delle imprese in California. | 4.5 Privacy e protezione dei dati |

### Unione Europea e Regno Unito

| Normativa / standard | Ente emittente | Ambito (una riga) | Capitoli / domini principali |
| --- | --- | --- | --- |
| GDPR | Unione Europea | Regolamento completo sul trattamento dei dati personali. | 4.5, 4.6 Privacy e conformità |
| UK GDPR / Data Protection Act 2018 | Regno Unito | Il regime di protezione dei dati del Regno Unito dopo la Brexit. | 4.5, 4.6 Privacy e conformità |
| eIDAS | Unione Europea | Quadro per identificazione elettronica e servizi fiduciari. | 4.2, 4.3 Sicurezza |
| Direttiva NIS2 | Unione Europea | Obblighi di cybersicurezza per i soggetti essenziali e importanti. | 4.4, 4.6 Operazioni di sicurezza e conformità |
| DORA (Digital Operational Resilience Act) | Unione Europea | Requisiti di resilienza operativa per il settore finanziario. | 9.1, 10.2 Affidabilità e audit |
| EU AI Act | Unione Europea | Regolamentazione basata sul rischio dei sistemi di IA (vedi governance dell'IA più avanti). | 6.1, 6.5 Strategia IA e IA responsabile |

## Accessibilità

| Standard | Ente emittente | Ambito (una riga) | Capitoli / domini principali |
| --- | --- | --- | --- |
| WCAG (2.1 / 2.2) | World Wide Web Consortium (W3C) | Linee guida per contenuti web accessibili, con livelli di conformità A/AA/AAA. | 5.3 Accessibilità; 5.1–5.6 UX e frontend |
| WAI-ARIA | World Wide Web Consortium (W3C) | Ruoli, stati e proprietà per applicazioni internet ricche accessibili. | 5.3, 5.6 Accessibilità e frontend |
| Section 508 | US Access Board / legge federale USA | Requisiti di accessibilità per le ICT federali USA, allineati a WCAG. | 5.3 Accessibilità (governo USA) |
| EN 301 549 | ETSI / CEN / CENELEC | Requisiti europei di accessibilità per gli appalti ICT, allineati a WCAG. | 5.3 Accessibilità (settore pubblico UE) |
| ADA (Americans with Disabilities Act) | US Congress | Legge sui diritti civili che vieta la discriminazione per disabilità, applicata ai servizi digitali. | 5.3 Accessibilità |
| ISO/IEC 40500 | ISO / IEC | Adozione internazionale di WCAG 2.0 come standard formale. | 5.3 Accessibilità |

## Governance dell'IA

| Quadro / normativa | Ente emittente | Ambito (una riga) | Capitoli / domini principali |
| --- | --- | --- | --- |
| NIST AI Risk Management Framework (AI RMF) | National Institute of Standards and Technology | Quadro volontario per governare, mappare, misurare e gestire il rischio dell'IA. | 6.1, 6.5 Strategia IA e IA responsabile |
| ISO/IEC 42001 | ISO / IEC | Requisiti per un Sistema di Gestione dell'IA (AIMS). | 6.1, 6.5 Governance dell'IA |
| ISO/IEC 23894 | ISO / IEC | Indicazioni sulla gestione del rischio specifica dell'IA. | 6.5 IA responsabile e affidabile |
| EU AI Act | Unione Europea | Obblighi legali a livelli di rischio per fornitori e utilizzatori di sistemi di IA. | 6.1, 6.3, 6.5 Applicazioni e governance dell'IA |
| OECD AI Principles | Organisation for Economic Co-operation and Development | Principi basati sui valori per un'IA affidabile, influenti sulla politica. | 6.5, 10.5 IA responsabile ed etica |

## Qualità e processo

| Standard / quadro | Ente emittente | Ambito (una riga) | Capitoli / domini principali |
| --- | --- | --- | --- |
| ISO/IEC 25010 | ISO / IEC | Modello di qualità del prodotto software (idoneità funzionale, affidabilità, sicurezza, ecc.). | 2.2, 2.4 Progettazione e test |
| ISO/IEC/IEEE 12207 | ISO / IEC / IEEE | Processi del ciclo di vita del software. | 1.4, 10.1 Modi di lavorare e gestione dei programmi |
| ISO 9001 | ISO | Requisiti per un Sistema di Gestione della Qualità generale. | 10.2 Rischio, audit e garanzia |
| CMMI | ISACA / CMMI Institute | Modello di maturità per capacità e miglioramento dei processi. | 10.1, 10.2 Gestione dei programmi e garanzia |
| Metriche DORA | DevOps Research and Assessment (Google Cloud) | Quattro metriche chiave di prestazione della consegna per i team software. | 8.1, 8.4, 9.1 Consegna, piattaforma, affidabilità |
| Quadro SPACE | Ricercatori Microsoft / GitHub | Modello multidimensionale per misurare la produttività degli sviluppatori. | 1.3, 8.4 Crescita ed esperienza dello sviluppatore |
| ITIL | AXELOS / PeopleCert | Quadro di pratiche di gestione dei servizi IT. | 9.1, 9.3 Affidabilità e gestione degli incidenti |

## Architettura

| Standard / quadro | Ente emittente | Ambito (una riga) | Capitoli / domini principali |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010 | ISO / IEC / IEEE | Standard per la descrizione dell'architettura e i punti di vista. | 2.7, 3.1 Documentazione e fondamenti dell'architettura |
| TOGAF | The Open Group | Quadro di enterprise architecture e metodo di sviluppo. | 3.1, 10.1 Architettura e gestione di portafoglio |
| C4 model | Comunità (Simon Brown) | Approccio a quattro livelli per visualizzare l'architettura del software. | 2.7, 3.1 Documentazione e architettura |
| arc42 | Comunità (Starke / Hruschka) | Modello per strutturare la documentazione dell'architettura. | 2.7, 3.1 Documentazione e architettura |
| ADR | Pratica della comunità | Registri leggeri delle decisioni architetturali significative. | 1.5, 2.7, 3.1 Decisioni e documentazione |

## Cloud e DevOps

| Standard / quadro | Ente emittente | Ambito (una riga) | Capitoli / domini principali |
| --- | --- | --- | --- |
| CIS Benchmarks | Centre for Internet Security | Basi di configurazione sicura basate sul consenso per sistemi e cloud. | 4.3, 8.2 Sicurezza di infrastruttura e IaC |
| Panorama e progetti CNCF | Cloud Native Computing Foundation | Ecosistema e standard per il calcolo cloud-native (per esempio Kubernetes). | 8.3 Container e cloud-native |
| OCI (Open Container Initiative) | Open Container Initiative (Linux Foundation) | Standard aperti per i formati di immagine e di runtime dei container. | 8.3 Container e cloud-native |
| OpenTelemetry | Cloud Native Computing Foundation | Standard neutrale rispetto ai fornitori per la telemetria (tracce, metriche, log). | 9.2 Osservabilità e monitoraggio |
| Open Policy Agent (OPA) | Cloud Native Computing Foundation | Motore di politiche di uso generale per la politica come codice. | 4.6, 8.2, 8.3 Conformità, IaC, orchestrazione |
| Pratiche SRE | Google (ampiamente adottate) | Approccio basato su SLI/SLO/budget di errore per gestire servizi affidabili. | 9.1 Site reliability engineering |
| FinOps Framework | FinOps Foundation | Pratiche per la gestione finanziaria del cloud e la responsabilità dei costi. | 9.4 Costi, sostenibilità, software verde |

## Dati

| Standard / quadro | Ente emittente | Ambito (una riga) | Capitoli / domini principali |
| --- | --- | --- | --- |
| DAMA-DMBOK | DAMA International | Corpo di conoscenze che organizza le discipline della gestione dei dati. | 7.1 Strategia e governance dei dati |
| ISO/IEC 38505 | ISO / IEC | Governance dei dati come bene organizzativo. | 7.1 Governance dei dati |
| ISO 8000 | ISO | Standard di qualità dei dati e dei dati anagrafici. | 7.1, 7.2 Governance e ingegneria dei dati |
| Data mesh | Comunità (Zhamak Dehghani) | Approccio decentralizzato e orientato al dominio ai dati come prodotto. | 7.1, 7.2 Strategia e ingegneria dei dati |
| DCAM | EDM Council | Modello di valutazione delle capacità di gestione dei dati. | 7.1 Strategia e governance dei dati |

## Note su ambito e cambiamento

Standard e normative evolvono. I numeri di versione (per esempio WCAG 2.1 contro
2.2, o gli anni di revisione ISO) e i cataloghi di controlli cambiano nel tempo e
continuano a emergere nuove leggi (come le normative di settore su IA e
resilienza). Trattate questa appendice come una mappa di partenza: confermate
versione, giurisdizione e applicabilità correnti prima di affidarvi a qualsiasi
voce per una decisione di conformità o di appalto. Dove i capitoli della guida e
questa appendice differiscono nei dettagli, governa sempre il documento di fonte
autorevole.


---

# Letture consigliate

Questa appendice è un elenco di letture curato e annotato che copre ogni dominio
della guida. Privilegia le opere che hanno plasmato la pratica su larga scala:
classici riconosciuti, riferimenti rigorosi e gli standard e i rapporti rispetto a
cui sono misurati i grandi team, le imprese e i team governativi.

Ogni voce dà titolo e autore/i, seguiti da una frase sul perché conta. L'elenco è
organizzato secondo le parti del libro. Leggete in modo selettivo: scegliete le
due o tre opere più vicine al vostro dolore attuale, non l'intero scaffale. Dove
un'opera attraversa più domini, è collocata dove è più utile; molte appartengono a
più parti.

Una nota sugli standard: enti come NIST, OWASP, W3C/WCAG, ISO e il programma DORA
pubblicano documenti vivi che sono rivisti periodicamente. Citate e leggete la
versione corrente; le annotazioni qui sotto descrivono il loro scopo duraturo.

## Fondamenti: cultura, persone e processo

- **Accelerate: The Science of Lean Software and DevOps**. Nicole Forsgren, Jez Humble, Gene Kim. Il fondamento di ricerca che mostra come le prestazioni di consegna predicano le prestazioni organizzative e che definisce le metriche (ora dette DORA) per misurarle.
- **The Phoenix Project**. Gene Kim, Kevin Behr, George Spafford. Un romanzo aziendale che rende intuitivi flusso, lavoro in corso e le "Tre Vie" di DevOps per leader e scettici allo stesso modo.
- **Team Topologies: Organising Business and Technology Teams for Fast Flow**. Matthew Skelton e Manuel Pais. Un vocabolario pratico (team allineati al flusso, di piattaforma, abilitanti e di sottosistema complicato) per progettare organizzazioni che producono buon software.
- **An Elegant Puzzle: Systems of Engineering Management**. Will Larson. Quadri collaudati sul campo per dimensionare i team, gestire la crescita organizzativa e prendere le decisioni ricorrenti della leadership ingegneristica.
- **Staff Engineer: Leadership Beyond the Management Track**. Will Larson. Definisce gli archetipi staff-plus e il percorso di leadership tecnica per chi vuole impatto senza diventare dirigente.
- **The Manager's Path**. Camille Fournier. Una guida per stadi da tech lead a dirigente che ancora le scale di carriera e il passaggio alla gestione.
- **The Staff Engineer's Path**. Tanya Reilly. Un compagno della letteratura staff-plus concentrato sul lavoro quotidiano di leadership tecnica, influenza e guida senza autorità.
- **Peopleware: Productive Projects and Teams**. Tom DeMarco e Timothy Lister. La persistente tesi che i problemi centrali del software siano sociologici, non tecnici.
- **The Mythical Man-Month**. Frederick P. Brooks Jr. L'origine della legge di Brooks e della distinzione tra complessità essenziale e accidentale che governa ancora organico e pianificazione.
- **The Fearless Organisation: Creating Psychological Safety in the Workplace**. Amy C. Edmondson. Il fondamento di ricerca della cultura senza colpe e della sicurezza che rende possibile imparare dal fallimento.
- **Thinking, Fast and Slow**. Daniel Kahneman. Il resoconto definitivo dei pregiudizi cognitivi, essenziale per colloqui strutturati, calibrazione e decisioni oneste.

## Mestiere della programmazione e qualità del codice

- **The Pragmatic Programmer: Your Journey to Mastery**. Andrew Hunt e David Thomas. Il catalogo fondativo di abitudini professionali (DRY, ortogonalità, tracer bullet) che definisce che cosa significhi artigianato.
- **Refactoring: Improving the Design of Existing Code**. Martin Fowler. Il catalogo canonico di trasformazioni che preservano il comportamento e la disciplina del miglioramento continuo del codice sostenuto da test.
- **Clean Code: A Handbook of Agile Software Craftsmanship**. Robert C. Martin. Uno standard molto usato (e dibattuto) per nomi, funzioni e leggibilità che plasma le aspettative di revisione di molti team.
- **Code Complete**. Steve McConnell. Un manuale completo e documentato di pratiche di costruzione che resta una base accurata per la qualità della programmazione.
- **Test-Driven Development: By Example**. Kent Beck. L'introduzione originale e pratica al ciclo rosso-verde-rifattorizza e alla progettazione che parte dai test.
- **Working Effectively with Legacy Code**. Michael Feathers. La cassetta degli attrezzi definitiva per aggiungere test a codice che non ne ha e modificarlo in sicurezza, indispensabile per i sistemi di lunga vita.
- **Growing Object-Oriented Software, Guided by Tests**. Steve Freeman e Nat Pryce. Una dimostrazione svolta di TDD da fuori a dentro, mocking ed evoluzione di un progetto attraverso i test.
- **A Philosophy of Software Design**. John Ousterhout. Un trattamento acuto e con opinioni di complessità, moduli profondi e occultamento dell'informazione che sfida in modo produttivo parte dell'ortodossia del "clean code".

## Architettura e sistemi

- **Designing Data-Intensive Applications**. Martin Kleppmann. Il miglior riferimento moderno sui compromessi di archiviazione, replicazione, partizionamento, consistenza ed elaborazione di flussi su larga scala.
- **Fundamentals of Software Architecture: An Engineering Approach**. Mark Richards e Neal Ford. Una rassegna ampia e aggiornata di stili architetturali, caratteristiche e del ruolo e del processo decisionale dell'architetto.
- **Software Architecture: The Hard Parts**. Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani. Un trattamento centrato sulle decisioni dei compromessi dell'architettura distribuita, della granularità dei servizi e della titolarità dei dati.
- **Building Evolutionary Architectures**. Neal Ford, Rebecca Parsons, Patrick Kua. Introduce le funzioni di idoneità e un'architettura progettata per cambiare in sicurezza nel tempo.
- **Domain-Driven Design: Tackling Complexity in the Heart of Software**. Eric Evans. L'origine di bounded context, linguaggio ubiquo e aggregati: il vocabolario della progettazione moderna dei servizi.
- **Building Microservices: Designing Fine-Grained Systems**. Sam Newman. Il riferimento per scomposizione, confini dei servizi, distribuzione e implicazioni organizzative dei microservizi.
- **Monolith to Microservices**. Sam Newman. Un catalogo di pattern per la scomposizione incrementale, come strangler fig e branch by abstraction, senza una rischiosa riscrittura big-bang.
- **Patterns of Enterprise Application Architecture**. Martin Fowler. Il riferimento a pattern nominati (repository, unit of work e altri) che ha dato un linguaggio condiviso ai sistemi aziendali.
- **Enterprise Integration Patterns**. Gregor Hohpe e Bobby Woolf. Il catalogo definitivo dei pattern di messaggistica alla base delle architetture a eventi e asincrone.
- **Release It! Design and Deploy Production-Ready Software**. Michael T. Nygard. La fonte di circuit breaker, bulkhead e altri pattern di stabilità per sistemi che sopravvivono alla vera produzione.
- **Design Patterns: Elements of Reusable Object-Oriented Software**. Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides ("Gang of Four"). Il catalogo storicamente decisivo dei pattern orientati agli oggetti e un vocabolario di progetto condiviso.

## Sicurezza, privacy e fiducia

- **Threat Modelling: Designing for Security**. Adam Shostack. La guida pratica e completa a STRIDE e alla modellazione strutturata delle minacce come pratica ingegneristica di routine.
- **Security Engineering: A Guide to Building Dependable Distributed Systems**. Ross Anderson. Il riferimento enciclopedico su come falliscono i sistemi reali e su come costruirne di resistenti agli attacchi.
- **The Tangled Web: A Guide to Securing Modern Web Applications**. Michal Zalewski. Un giro rigoroso del modello di sicurezza del browser e dei modi sottili in cui le piattaforme web tradiscono assunzioni ingenue.
- **Cryptography Engineering**. Niels Ferguson, Bruce Schneier, Tadayoshi Kohno. Una guida da professionisti per usare correttamente la crittografia ed evitare gli errori comuni e pericolosi.
- **Building Secure and Reliable Systems**. Heather Adkins et al. (Google). La sintesi di Google di sicurezza e affidabilità come proprietà intrecciate progettate fin dall'inizio.
- **Zero Trust Networks**. Evan Gilman e Doug Barth. Un chiaro trattamento di principi e meccanica dell'architettura di rete del non-fidarsi-mai, verificare-sempre.
- **OWASP Top 10**. OWASP Foundation. La base condivisa dei rischi di sicurezza più critici delle applicazioni web, citata da politiche e audit in tutto il mondo.
- **OWASP Application Security Verification Standard (ASVS)**. OWASP Foundation. Una lista di controllo a livelli e verificabile di requisiti di sicurezza adatta a contratti e criteri di accettazione.
- **NIST SP 800-53: Security and Privacy Controls for Information Systems and Organisations**. NIST. Il catalogo di controlli al centro della sicurezza federale USA e base dell'autorizzazione FedRAMP e FISMA.
- **NIST Cybersecurity Framework (CSF)**. NIST. La struttura identifica-proteggi-rileva-rispondi-ripristina, largamente adottata, per organizzare un programma di sicurezza.
- **NIST SP 800-207: Zero Trust Architecture**. NIST. La definizione di riferimento e le architetture di riferimento che ancorano la maggior parte dei programmi zero-trust aziendali e governativi.

## UX, UI e design di prodotto

- **The Design of Everyday Things**. Don Norman. Il testo fondativo su affordance, significanti, riscontro e progettazione centrata sull'uomo, che si applica ben oltre gli oggetti fisici.
- **Don't Make Me Think, Revisited**. Steve Krug. La concisa e duratura tesi dell'usabilità autoevidente e del valore di test di usabilità economici e frequenti.
- **About Face: The Essentials of Interaction Design**. Alan Cooper, Robert Reimann, David Cronin. Il riferimento completo su progettazione dell'interazione, persona e progettazione guidata dagli obiettivi.
- **Design Systems: A Practical Guide**. Alla Kholmatova. Un resoconto concreto della costruzione di sistemi di componenti coerenti e riusabili e del linguaggio condiviso che li sostiene.
- **Refactoring UI**. Adam Wathan e Steve Schoger. Una guida pratica, guidata dagli esempi, alla rifinitura visiva per ingegneri che progettano interfacce senza formazione formale.
- **Letting Go of the Words: Writing Web Content that Works**. Ginny Redish. La guida definitiva a una progettazione dei contenuti in linguaggio semplice e centrata sul compito.
- **Inclusive Design Patterns / Accessibility for Everyone**. Heydon Pickering; Laura Kalbag. Compagni pratici per costruire interfacce che funzionano per l'intera gamma delle abilità umane.
- **A Web for Everyone: Designing Accessible User Experiences**. Sarah Horton e Whitney Quesenbery. Un ponte guidato dai principi tra standard di accessibilità e buona esperienza utente.
- **Web Content Accessibility Guidelines (WCAG) 2.2**. W3C. Lo standard di riferimento internazionale (percepibile, utilizzabile, comprensibile, robusto) dietro la maggior parte delle leggi sull'accessibilità.
- **U.S. Web Design System (USWDS)**. Governo USA. Un esempio funzionante di sistema di design accessibile e basato su standard, costruito per servizi pubblici su larga scala.

## Intelligenza artificiale e machine learning

- **Designing Machine Learning Systems**. Chip Huyen. La principale guida pratica per costruire sistemi di ML in produzione da un capo all'altro: dati, feature, distribuzione e monitoraggio.
- **Reliable Machine Learning: Applying SRE Principles to ML in Production**. Cathy Chen et al. Estende la disciplina SRE (SLO, monitoraggio, risposta agli incidenti) ai sistemi di machine learning.
- **Deep Learning**. Ian Goodfellow, Yoshua Bengio, Aaron Courville. Il riferimento accademico standard per teoria e metodi alla base delle moderne reti neurali.
- **AI Engineering: Building Applications with Foundation Models**. Chip Huyen. Una guida aggiornata per progettare, valutare e gestire applicazioni costruite su grandi modelli di fondazione.
- **Weapons of Maths Destruction**. Cathy O'Neil. Un vivido argomento per la responsabilità algoritmica e i danni reali dei modelli non esaminati, essenziale per l'IA del settore pubblico.
- **Interpretable Machine Learning**. Christoph Molnar. Un riferimento completo e liberamente disponibile sui metodi di spiegabilità per modelli e previsioni.
- **NIST AI Risk Management Framework (AI RMF 1.0)**. NIST. Il quadro di riferimento per governare, mappare, misurare e gestire il rischio dell'IA, sempre più citato in politiche e appalti.

## Dati, analisi e conoscenza

- **The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modelling**. Ralph Kimball e Margy Ross. Il riferimento canonico su schemi a stella e modellazione dimensionale per l'analisi.
- **Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing**. Ron Kohavi, Diane Tang, Ya Xu. La guida autorevole per condurre esperimenti che danno risultati affidabili e azionabili su larga scala.
- **Fundamentals of Data Engineering**. Joe Reis e Matt Housley. Una mappa neutrale rispetto ai fornitori del moderno ciclo di vita dei dati e delle pratiche ingegneristiche che vi stanno dietro.
- **Data Mesh: Delivering Data-Driven Value at Scale**. Zhamak Dehghani. Il testo fondativo dell'approccio orientato al dominio e centrato sul prodotto per organizzare i dati su larga scala.
- **Storytelling with Data**. Cole Nussbaumer Knaflic. Una guida pratica a una visualizzazione dei dati onesta e chiara e a comunicare le intuizioni ai decisori.
- **The Visual Display of Quantitative Information**. Edward R. Tufte. L'opera fondativa su integrità grafica, data-ink ed etica del mostrare i dati con onestà.
- **DAMA-DMBOK: Data Management Body of Knowledge**. DAMA International. Il quadro di riferimento completo per governance, cura, qualità e catalogazione dei dati.
- **The Book of Why**. Judea Pearl e Dana Mackenzie. Un'introduzione leggibile all'inferenza causale, vitale per passare dalla correlazione a decisioni difendibili.

## Automazione, DevOps e ingegneria di piattaforma

- **The DevOps Handbook**. Gene Kim, Jez Humble, Patrick Debois, John Willis. Il manuale completo che traduce le "Tre Vie" in pratiche concrete di flusso, riscontro e apprendimento continuo.
- **Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation**. Jez Humble e David Farley. Il testo fondativo su pipeline di distribuzione, automazione e rilascio del software in sicurezza e spesso.
- **Infrastructure as Code: Managing Servers in the Cloud**. Kief Morris. Il riferimento sul trattare l'infrastruttura come software: moduli, test, immutabilità e deriva.
- **Team Topologies**. Matthew Skelton e Manuel Pais. (Vedi Fondamenti.) Essenziale anche qui per dare forma ai team di piattaforma e all'esperienza dello sviluppatore che forniscono.
- **Kubernetes Patterns**. Bilgin Ibryam e Roland Huß. Un catalogo di pattern riusabili per progettare applicazioni cloud-native su Kubernetes.
- **Software Engineering at Google**. Titus Winters, Tom Manshreck, Hyrum Wright. Come pratiche ingegneristiche quali test, revisione, strumenti e gestione delle dipendenze scalano a decine di migliaia di ingegneri nell'arco di decenni.
- **The Twelve-Factor App**. Adam Wiggins (Heroku). Il conciso e influente manifesto per costruire servizi portabili, scalabili e cloud-native.
- **DORA State of DevOps Report**. DORA / Google Cloud (annuale). Il programma di ricerca continuo dietro le quattro metriche chiave di consegna e le capacità che guidano le prestazioni.

## Operazioni, affidabilità e osservabilità

- **Site Reliability Engineering: How Google Runs Production Systems**. Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (a cura di). Il testo fondativo che definisce SLI, SLO, budget di errore e la disciplina di ingegnerizzare l'affidabilità.
- **The Site Reliability Workbook**. Betsy Beyer et al. (a cura di). Il compagno pratico con esempi concreti, SLO svolti e indicazioni di implementazione.
- **Observability Engineering**. Charity Majors, Liz Fong-Jones, George Miranda. La definizione moderna di osservabilità, dati ad alta cardinalità e il debug degli sconosciuti-sconosciuti in produzione.
- **Implementing Service Level Objectives**. Alex Hidalgo. Una guida accurata e pratica per progettare, misurare e usare bene SLO e budget di errore.
- **Release It!**. Michael T. Nygard. (Vedi Architettura.) Fondativo anche qui per i pattern di stabilità in produzione e per gestire sistemi resilienti.
- **The Art of Capacity Planning**. Arun Kejariwal e John Allspaw. Un approccio basato sui dati per prevedere la domanda e pianificare la capacità di sistemi in crescita.
- **Chaos Engineering: System Resiliency in Practice**. Casey Rosenthal e Nora Jones. Il trattamento definitivo dell'iniettare deliberatamente guasti per costruire fiducia nella resilienza del sistema.
- **Google SRE Book, Chapter on Postmortems**. Google. Il modello molto imitato di postmortem senza colpe e di apprendimento dagli incidenti.

## Impresa, governo e interesse pubblico

- **Working in Public: The Making and Maintenance of Open Source Software**. Nadia Eghbal. Lo studio essenziale di come l'open source si sostenga davvero e dell'onere dei manutentori dietro le dipendenze su cui contano le imprese.
- **Recoding America: Why Government Is Failing in the Digital Age and How We Can Do Better**. Jennifer Pahlka. Un resoconto lucido del perché fallisce la tecnologia del settore pubblico e di come una riforma centrata sulla consegna possa correggerla.
- **Digital Transformation at Scale: Why the Strategy Is Delivery**. Andrew Greenway et al. Lezioni dal UK Government Digital Service sul trasformare i servizi pubblici consegnando, non pianificando.
- **Project to Product**. Mik Kersten. Il Flow Framework per spostare le grandi imprese dal finanziamento a progetto a flussi di valore di prodotto durevoli.
- **Escaping the Build Trap**. Melissa Perri. Come le organizzazioni scambiano la produzione per l'esito e come la gestione del prodotto lo corregge, con rilevanza diretta per la governance di portafoglio e programmi.
- **U.S. Digital Services Playbook**. U.S. Digital Service. Un conciso insieme di mosse per consegnare servizi digitali governativi efficaci e centrati sull'utente.
- **GOV.UK Service Manual and Service Standard**. UK Government Digital Service. Uno standard pubblicato e funzionante per costruire buoni servizi pubblici, molto imitato da altri governi.
- **NIST SP 800-37: Risk Management Framework**. NIST. Il quadro di processo dietro l'autorizzazione a operare (ATO) e il monitoraggio continuo nei sistemi federali USA.
- **The FinOps Foundation Framework**. FinOps Foundation. Il modello di riferimento per visibilità, ottimizzazione e responsabilità dei costi cloud tra finanza e ingegneria.

## Come usare questo elenco

- **Partite dal vostro dolore.** Se le distribuzioni sono lente e spaventose, leggete *Accelerate*, *Continuous Delivery* e i rapporti *DORA* prima di qualsiasi altra cosa.
- **Leggete per il decennio, non per lo sprint.** Preferite le opere che spiegano principi duraturi a quelle legate a una specifica versione di uno strumento.
- **Verificate l'edizione corrente degli standard.** NIST, OWASP, WCAG, ISO e DORA rivedono le loro pubblicazioni; lavorate sempre dall'ultimo rilascio e annotate la versione nelle vostre politiche.
- **Costruite uno scaffale condiviso.** Un team che ha letto in comune due o tre di questi libri discute meno e decide più in fretta, perché condivide un vocabolario e un insieme di punti di riferimento.
- **Vedi anche il capitolo 12.5** per l'indice completo di standard e quadri di riferimento e il **capitolo 12.6** per come ordinare l'adozione delle pratiche che queste opere descrivono.

