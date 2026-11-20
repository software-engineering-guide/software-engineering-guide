# 5.3 Accessibilità

## Panoramica e motivazioni

L'[accessibilità](https://en.wikipedia.org/wiki/Accessibility) (spesso abbreviata in "a11y") è la pratica di costruire software che le persone con disabilità possano percepire, comprendere, navigare e usare. Comprende persone cieche o con ridotta capacità visiva, sorde o con ridotta capacità uditiva, con compromissioni motorie, con differenze cognitive o di apprendimento e persone che affrontano limiti temporanei o situazionali come un braccio rotto, la luce del sole intensa o una stanza rumorosa. Circa una persona su cinque ha una disabilità e tutti traggono beneficio dal design accessibile a un certo punto. Non è un accomodamento di nicchia. È una base di qualità.

Per i grandi team, l'accessibilità deve essere costruita nel sistema, non lasciata alle buone intenzioni dei singoli. Quando molti team rilasciano in un unico prodotto, un singolo componente inaccessibile (un campo di modulo senza etichetta, un indicatore di stato solo a colori, una trappola da tastiera in una finestra modale) può chiudere fuori gli utenti disabili da un intero percorso. Incorporare l'accessibilità in componenti condivisi, design token, pipeline di test e definizioni di completato è l'unico modo di renderla affidabile su larga scala. Adattarla a posteriori è costoso e soggetto a errori. Progettarla dentro è economico e durevole.

Per gli enti pubblici, l'accessibilità è un requisito di legge e un obbligo civico, non un di più. I servizi pubblici devono servire ogni membro del pubblico e i cittadini disabili spesso non hanno un fornitore alternativo: se il sito del governo è inaccessibile, non possono ottenere la propria prestazione, licenza o votare in un altro modo. Leggi e standard in tutto il mondo rendono l'accessibilità obbligatoria per gli enti pubblici e sempre più anche per il settore privato. Questo capitolo tratta l'accessibilità come tre cose insieme: un dovere legale, un dovere etico e semplicemente buon design.

*Vedi anche:* il capitolo 5.2 (progettazione UI e design system), il capitolo 5.6 (ingegneria frontend) e il capitolo 5.1 (fondamenti di UX).

## Principi chiave

- L'accessibilità è un attributo di qualità di base, come sicurezza e prestazioni, non una funzionalità facoltativa.
- I principi POUR: le interfacce devono essere Percepibili, Utilizzabili, Comprensibili e Robuste.
- Prima l'[HTML semantico](https://en.wikipedia.org/wiki/Semantic_HTML); usa [ARIA](https://en.wikipedia.org/wiki/WAI-ARIA) solo per colmare divari genuini, mai come sostituto degli elementi nativi.
- Tutto ciò che è utilizzabile con un mouse deve essere utilizzabile con la sola tastiera.
- Non trasmettere informazioni solo con colore, forma o posizione.
- Gli strumenti automatici colgono solo una frazione dei problemi; i test manuali e con [tecnologie assistive](https://en.wikipedia.org/wiki/Assistive_technology) sono essenziali.
- Il design accessibile è un design migliore per tutti (l'["effetto taglio del marciapiede"](https://en.wikipedia.org/wiki/Curb_cut), in cui le funzionalità costruite per le persone disabili beneficiano tutti gli utenti).
- Progetta e testa con le persone disabili, non solo per loro.

## Raccomandazioni

### Progetta e costruisci secondo WCAG, puntando allo standard corrente

Le [Web Content Accessibility Guidelines](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) sono il riferimento internazionale. WCAG 2.1 e 2.2 sono organizzate sotto i quattro principi POUR, con criteri di successo testabili ai livelli di conformità A, AA e AAA. Punta al Livello AA come base; è ciò che la maggior parte delle leggi richiama. WCAG 2.2 aggiunge criteri per visibilità del focus, dimensione dei bersagli e riduzione del carico cognitivo. WCAG 3.0 è un successore emergente, strutturato in modo diverso e ancora in sviluppo. Tienilo d'occhio, ma costruisci oggi per 2.2 AA. Tratta le linee guida come un pavimento, non un soffitto: superare ogni criterio non garantisce un'esperienza davvero utilizzabile.

### Usa HTML semantico e ARIA corretto

Gli elementi HTML nativi (pulsanti, link, controlli di modulo, intestazioni, elenchi, riferimenti di struttura) vengono con semantica di accessibilità, comportamento da tastiera e supporto delle tecnologie assistive integrati. Usali per primi. Ricorri ai ruoli, stati e proprietà ARIA (Accessible Rich Internet Applications) solo per descrivere widget personalizzati che l'HTML non può esprimere e segui le ARIA Authoring Practices. La prima regola di ARIA è semplice: non usare ARIA se basta un elemento nativo. ARIA scorretto è peggio di nessuno: fuorvia attivamente i [lettori di schermo](https://en.wikipedia.org/wiki/Screen_reader). Dai alla pagina una struttura logica di intestazioni, etichette significative, testo alternativo per le immagini, sottotitoli e trascrizioni per i media e un collegamento programmatico tra ogni etichetta e il suo controllo.

### Garantisci l'utilizzabilità da tastiera e con tecnologie assistive

Ogni elemento interattivo deve essere raggiungibile e utilizzabile con la sola tastiera, in un ordine logico, con un indicatore di focus chiaramente visibile. Evita le trappole da tastiera. Gestisci il focus deliberatamente quando il contenuto cambia: sposta il focus su una finestra di dialogo quando si apre, restituiscilo quando si chiude e annuncia gli aggiornamenti dinamici attraverso regioni live. Testa con tecnologie assistive reali, compresi lettori di schermo su desktop e mobile, ingrandimento dello schermo, controllo vocale e accesso a interruttore. E rispetta le preferenze dell'utente come movimento ridotto e contrasto aumentato.

### Testa con strumenti automatici, revisione manuale e utenti reali

Gli scanner di accessibilità automatici sono preziosi e dovrebbero girare nella pipeline a ogni modifica. Ma gli studi mostrano in modo costante che colgono solo una minoranza dei problemi reali, circa un terzo. Il resto richiede il giudizio umano: percorsi da tastiera, test con lettore di schermo, controlli di contrasto e chiedersi se il contenuto sia davvero comprensibile. Soprattutto, includi persone con disabilità nei test di usabilità. Incorpora criteri di accettazione di accessibilità nella definizione di completato, così che i problemi siano colti per storia anziché in un audit pre-lancio.

### Rendi l'accessibilità organizzativa, non eroica

Incorpora l'accessibilità nel design system così che i componenti arrivino accessibili per impostazione predefinita. Offri formazione così che designer, ingegneri, autori di contenuti e product manager sappiano ciascuno di che cosa sono responsabili. Stabilisci uno standard di accessibilità, un responsabile o un centro di eccellenza e un processo di rimedio. Pubblica una dichiarazione di accessibilità e dai agli utenti un modo di segnalare le barriere. E acquista in modo accessibile: richiedi a fornitori e componenti di terze parti di essere conformi e di fornire evidenza (come un rapporto di conformità all'accessibilità).

## Compromessi: vantaggi e svantaggi

| Approccio | Vantaggi | Svantaggi |
|---|---|---|
| Costruire l'accessibilità dentro fin dall'inizio | Il più economico, durevole, migliore per tutti | Richiede formazione e disciplina iniziali |
| Adattare / rimediare dopo | Rinvia lo sforzo, sblocca un lancio rapido | Molto più costoso, fragile, esposizione legale nel frattempo |
| Solo test automatici | Veloci, economici, colgono le regressioni nella CI | Perdono circa due terzi dei problemi; falsa sicurezza |
| Test manuali + con tecnologie assistive | Colgono vere barriere di usabilità | Più lenti, richiedono tester esperti e dispositivi |
| Test con utenti disabili | Verità di fondo sull'esperienza reale | Sforzo e costo di reclutamento, da fare con rispetto |

Il compromesso centrale è disciplina iniziale contro costo differito. L'accessibilità incorporata costa poco e migliora la qualità per tutti; l'accessibilità adattata sotto pressione legale è costosa, incompleta e stressante. Nel lungo periodo non c'è un vero compromesso con la "velocità": il software inaccessibile semplicemente non funziona per un quinto dei tuoi utenti. È un difetto, non un risparmio.

## Domande da discutere con il tuo team

1. **Le regressioni di accessibilità fanno fallire la nostra build come lo fa un test rotto, e se no, perché?** Gli scanner automatici colgono solo circa un terzo dei problemi, ma quelli che colgono (etichette mancanti, fallimenti di contrasto, controlli senza etichetta) sono economici da cogliere nella CI e costosi da trovare in un audit pre-lancio. Trattare una regressione come fallimento della build è ciò che sposta l'accessibilità da sforzo eroico individuale a proprietà affidabile del sistema, che è l'unica cosa che funziona quando molti team rilasciano in un unico prodotto. Decidi quali controlli sono bloccanti, quali consultivi e chi può scavalcare un fallimento. Porta alla riunione i risultati attuali dello scanner e la tua definizione di completato. Se i criteri di accessibilità non sono scritti nella definizione di completato per storia, saranno depriorizzati nel momento in cui una scadenza si stringe.

2. **Qual è la nostra regola per i widget personalizzati, e chi rivede l'ARIA prima che venga rilasciata?** Gli elementi HTML nativi vengono con comportamento da tastiera e supporto delle tecnologie assistive gratis e ARIA scorretto è peggio di nessuno perché fuorvia attivamente i lettori di schermo. Concorda che l'HTML semantico è il predefinito e che qualsiasi widget personalizzato (un menu a discesa su misura, un selettore di data o una finestra modale) richiede un percorso da tastiera e con lettore di schermo prima del merge, seguendo le ARIA Authoring Practices. Conta di più per i componenti interattivi che molti team riutilizzano, perché un'unica finestra modale rotta con una trappola da tastiera può chiudere fuori gli utenti disabili da un intero percorso. Porta un elenco dei tuoi widget personalizzati e chiediti quali sono stati testati con un vero lettore di schermo. Quelli che non lo sono sono passività nascoste nel codice condiviso.

3. **Qual è la nostra politica sugli overlay di accessibilità, e qualcuno crede che siano una vera soluzione?** Gli overlay sono commercializzati come uno script di una riga che rende conforme un sito e fanno gola quando arriva la pressione legale e una scadenza incombe. Non danno una vera conformità, possono peggiorare l'esperienza per gli utenti di tecnologie assistive e per gli enti pubblici lasciano non soddisfatto il dovere legale di fondo. Decidi esplicitamente che investirai in markup semantico, supporto da tastiera e test con persone disabili anziché comprare un widget che copre il problema. Porta il costo di un abbonamento a un overlay e confrontalo con il costo di incorporare l'accessibilità una volta in componenti e pipeline. Impostarlo presto previene una decisione di appalto in preda al panico più avanti che spende denaro e non risolve nulla.

4. **Le persone disabili fanno parte della nostra progettazione e dei nostri test, o stiamo ancora progettando per un utente immaginario che ci siamo inventati?** Scanner automatici e persino audit di esperti ti dicono se il markup è conforme; non ti dicono se un utente cieco può davvero finire il tuo checkout o se una persona con una disabilità cognitiva può capire i tuoi messaggi di errore. Coinvolgere partecipanti disabili è l'unica fonte di verità di fondo e cambia ciò che costruisci, ma solleva questioni reali su come reclutare con equità, come compensare le persone per il loro tempo e come evitare di trattare un partecipante come portavoce di ogni disabilità. Porta il tuo attuale elenco di ricerca, le tue pratiche di reclutamento e pagamento e un conto onesto di quanti studi nell'ultimo anno hanno incluso partecipanti disabili. Per una grande organizzazione, un panel ricorrente con compenso equo e copertura di esigenze visive, uditive, motorie e cognitive è ciò che trasforma questo da gesto una tantum in un input affidabile; negli enti pubblici, coinvolgere il pubblico che servi fa spesso parte dell'obbligo legale e civico, non di una cortesia facoltativa.

5. **Quando compriamo o incorporiamo un componente di terze parti, richiediamo prova di accessibilità, e chi la controlla?** Gran parte di ciò che viene rilasciato in un grande prodotto non è scritta internamente: un selettore di data da una libreria, un widget di pagamento in un iframe, un pacchetto di grafici, un intero modulo SaaS. Un singolo componente incorporato inaccessibile può far fallire un intero percorso per quanto sia pulito il tuo codice e una volta collegato, sostituirlo è costoso. Decidi che l'accessibilità è un requisito di appalto, che i fornitori devono fornire un rapporto di conformità all'accessibilità (un documento come un VPAT che dichiara come un prodotto si misura rispetto a WCAG) e che qualcuno di tecnico convalida l'affermazione anziché archiviarla. Porta un inventario dei tuoi componenti di terze parti e chiediti quali hanno evidenza di conformità aggiornata e credibile. Negli acquisti aziendali e governativi, scrivi nel contratto la conformità WCAG 2.2 AA e un diritto al rimedio, perché una promessa fatta prima di firmare è molto più economica da far rispettare di una barriera scoperta dopo l'entrata in funzione.

6. **Qual è il nostro livello di conformità obiettivo, chi lo possiede e come lo manteniamo aggiornato man mano che gli standard si muovono?** WCAG 2.2 AA è il pavimento di oggi e la maggior parte delle leggi vi fa riferimento, ma la 2.2 ha aggiunto criteri che molti team non hanno adottato e WCAG 3.0 sta arrivando con una struttura diversa. Senza un responsabile nominato, lo standard deriva: team diversi puntano a versioni diverse, nessuno segue il divario e la conformità marcisce in silenzio tra un audit e l'altro. Decidi la versione e il livello esatti a cui costruisci, chi ha l'autorità di alzarli e come i nuovi criteri raggiungono il design system e la definizione di completato. Porta il tuo attuale obiettivo dichiarato, l'evidenza di dove i team lo soddisfano davvero e una breve roadmap per adottare i criteri 2.2 che hai saltato. Per un'organizzazione grande o pubblica, un responsabile o centro di eccellenza dell'accessibilità, una dichiarazione di accessibilità pubblicata e un piano documentato per la prossima versione dello standard sono ciò che ti permette di rispondere a un regolatore o a un tribunale con evidenze anziché buone intenzioni.

## Lente settoriale

**Startup.** Qui la velocità ti favorisce, perché l'accessibilità è più economica quando la base di codice è piccola. Aggiungi uno scanner automatico alla CI e un percorso da tastiera alla tua lista di controllo delle pull request fin dal primo sprint e appoggiati all'HTML semantico per ottenere gratis supporto da tastiera e lettore di schermo. Salta overlay e strumenti pesanti; il vantaggio è che quando l'ufficio appalti di un cliente chiede un rapporto di conformità a metà vendita, puoi rispondere in giorni anziché in affanno.

**Piccola impresa.** Senza uno specialista di accessibilità e con un budget ridotto, compra l'accessibilità anziché costruirla: scegli una piattaforma, un tema o una libreria di componenti già conforme e che lo dichiari e preferisci i fornitori che pubblicano una dichiarazione di accessibilità. Copri tu stesso le basi di alto valore con strumenti gratuiti, controlli solo da tastiera, un verificatore di contrasto ed etichette chiare su ogni campo, perché colgono i fallimenti che più spesso escludono i clienti. Tratta un flusso automatico sbagliato o inutilizzabile come un cliente perso, poiché una piccola impresa raramente offre un canale assistito a cui ripiegare.

**Grande impresa.** Su larga scala il lavoro è fare dell'accessibilità una proprietà del sistema tra molti team. Rilascia componenti accessibili per impostazione predefinita nel design system, filtra le regressioni nella CI e istituisci un responsabile o centro di eccellenza con un processo di rimedio e formazione per designer, ingegneri e autori di contenuti. Segui la conformità nel tempo come metrica, scrivi la conformità WCAG negli appalti e gestisci i componenti di terze parti come portafoglio così che un widget incorporato non possa far fallire in silenzio un percorso condiviso.

**Ente pubblico.** L'accessibilità è un mandato di legge e un dovere civico, poiché i cittadini disabili spesso non hanno un fornitore alternativo per una prestazione, una licenza o il voto. Costruisci allo standard che la tua giurisdizione cita (per esempio Section 508, EN 301 549 o lo European Accessibility Act mappato su WCAG 2.2 AA), pubblica una dichiarazione di accessibilità con un percorso per segnalare le barriere e testa con il pubblico disabile che servi. Respingi gli overlay come sostituto della vera conformità e richiedi ai fornitori di fornire evidenza credibile e un diritto al rimedio nel contratto.

## Esempi

**Startup.** Una startup di tre persone che costruisce uno strumento di selezione del personale ha aggiunto uno scanner di accessibilità alla build e un rapido percorso da tastiera alla lista di controllo delle pull request fin dal primissimo sprint, ragionando che fosse più economico restare accessibili che correggere dopo. Quando l'ufficio appalti di un cliente di medie dimensioni ha chiesto un rapporto di conformità all'accessibilità durante un ciclo di vendita, la startup usava già HTML semantico, aveva etichettato ogni campo e aveva un focus visibile ovunque, quindi ha risposto in giorni anziché in affanno. Quella prontezza ha vinto un affare che un concorrente ha perso sullo stesso requisito.

**Grande impresa.** Un grande rivenditore ha affrontato una class action perché i clienti ciechi non riuscivano a completare il checkout con un lettore di schermo. Oltre all'accordo e alle spese legali, l'azienda ha dovuto rimediare con una tempistica sorvegliata dal tribunale. Poi ha ricostruito l'accessibilità nel proprio design system e nella pipeline CI, ha aggiunto i test con lettore di schermo alla definizione di completato e ha formato i suoi team. Il checkout ricostruito e accessibile ha anche migliorato la conversione e ridotto i contatti con l'assistenza per tutti: le correzioni che aiutavano gli utenti di lettori di schermo (etichette chiare, messaggi di errore, ordine logico) aiutavano tutti gli utenti.

**Ente pubblico.** Un'agenzia di prestazioni pubbliche era legalmente tenuta a soddisfare WCAG 2.1 AA per la propria domanda online. I primi test con utenti ciechi e ipovedenti, utenti solo da tastiera e utenti con disabilità cognitive hanno rivelato che un indicatore di "campo obbligatorio" solo a colori, un selettore di data inaccessibile e errori di convalida non annunciati stavano impedendo alle persone di finire. Correggerli, con markup semantico, focus visibile, annunci degli errori in regioni live e aiuto in [linguaggio semplice](https://en.wikipedia.org/wiki/Plain_language), ha permesso ai cittadini disabili di fare domanda da soli per la prima volta. Questo ha ridotto la dipendenza dall'aiuto di persona e abbassato il costo di servizio, soddisfacendo il mandato di legge.

## Business case: motivazioni, ROI e TCO

Il business case poggia su portata di mercato, rischio legale, costo di servizio e qualità. Le persone disabili e le loro famiglie controllano un significativo potere d'acquisto; escluderle significa rinunciarvi. I servizi accessibili riducono il bisogno di costosi canali assistiti (aiuto telefonico e di persona), il che è un risparmio operativo diretto, specialmente per gli enti pubblici. E poiché i miglioramenti di accessibilità (etichette chiare, supporto da tastiera, contenuti leggibili, markup robusto) aiutano tutti, di solito alzano completamento e soddisfazione complessivi.

Sul TCO, il costo di adozione è formazione, strumenti e incorporare l'accessibilità in componenti e pipeline, tutto modesto quando lo fai fin dall'inizio. Il costo del non adottare è grave e viene da diverse direzioni: responsabilità legale (cause, accordi, rimedio imposto dal tribunale, sanzioni normative), la spesa molto più alta di adattare sotto pressione di scadenza, danno reputazionale e il costo continuo di servire gli utenti esclusi attraverso canali più costosi. Adattare di solito costa diverse volte ciò che avrebbe costato progettare dentro.

Per presentare il caso alla leadership, parti dall'obbligo legale dove si applica (è non negoziabile per gli enti pubblici e sempre più per il settore privato). Poi quantifica la popolazione indirizzabile che stai escludendo, il costo di canale assistito di quell'esclusione e i guadagni da "taglio del marciapiede" per tutti gli utenti. Posiziona l'accessibilità come gestione del rischio più qualità, non beneficenza.

## Antipattern e insidie

- **Accessibilità come casella pre-lancio**: un audit alla fine anziché una pratica continua, garantendo costose rilavorazioni dell'ultimo minuto.
- **"Zuppa di div"**: markup non semantico con gestori di clic su elementi generici, invisibile alle tecnologie assistive.
- **Uso scorretto di ARIA**: incollare ARIA su markup rotto, che fuorvia i lettori di schermo più di un markup semplice.
- **Informazione solo a colori**: stato mostrato solo dal colore, invisibile agli utenti daltonici.
- **Focus invisibile**: rimuovere i contorni del focus per estetica, lasciando in secca gli utenti da tastiera.
- **Trappole da tastiera**: finestre modali e widget che intrappolano o perdono il focus.
- **Autocompiacimento da scansione automatica**: superare uno scanner e presumere che il prodotto sia accessibile.
- **Overlay di accessibilità**: widget di terze parti da "correzione in una riga" che non danno una vera conformità e possono peggiorare l'esperienza.
- **Escludere gli utenti disabili dalla ricerca**: progettare per un utente disabile immaginario anziché testare con quelli reali.

## Modello di maturità

**Livello 1: Avvio.** Nessuna pratica di accessibilità. I problemi sono scoperti solo quando un utente si lamenta o arriva una causa e la risposta è reattiva. Il markup è non semantico e non testato e nessuno possiede il problema.

**Livello 2: Sviluppo.** Esiste consapevolezza e alcuni team agiscono: uno scanner automatico in una build qui, un percorso da tastiera là, un audit pre-lancio prima di un grande rilascio. La pratica è di base e incoerente tra i team, l'accessibilità è ancora una lista di controllo di fine corsa ed è spesso depriorizzata sotto pressione di calendario.

**Livello 3: Standardizzazione.** WCAG 2.2 AA è lo standard documentato, fatto rispettare in tutta l'organizzazione. L'accessibilità è incorporata nel design system così che i componenti arrivino accessibili per impostazione predefinita, testati in modo automatico e manuale e scritti nella definizione di completato. I team sono formati, esiste un responsabile o centro di eccellenza ed è definito un processo di rimedio.

**Livello 4: Gestione.** L'accessibilità è misurata e controllata con dati rispetto a valori di riferimento. L'organizzazione segue metriche di conformità nel tempo (tassi di superamento dello scanner, numero di barriere aperte per gravità, copertura con lettore di schermo dei percorsi critici e tempo di rimedio), le riporta per team su un cruscotto e tratta le regressioni come fallimenti della build anziché avvisi consultivi. Gli obiettivi sono fissati rispetto a un riferimento e i progressi sono rivisti, così che un team che arretra sia visibile prima che un audit lo trovi.

**Livello 5: Orchestrazione.** L'accessibilità è migliorata di continuo e integrata nell'organizzazione. Le persone disabili fanno parte di ricerca e test in modo ricorrente e l'accessibilità è incorporata in appalti, design token e CI. L'organizzazione si adatta al mutare degli standard (adottando nuovi criteri WCAG e preparandosi a WCAG 3.0) e influenza fornitori e partner così che l'intera filiera sia conforme.

## Spunti di discussione

- Come evitate che l'accessibilità sia depriorizzata quando le scadenze si stringono?
- Qual è il giusto mix di test automatici, manuali e con utenti per il vostro profilo di rischio?
- Come dovrebbe la conformità all'accessibilità essere scritta nei contratti con i fornitori e negli appalti?
- Come gestite il divario tra conformità WCAG e vera usabilità per le persone disabili?
- Come dovrebbero i team prepararsi a WCAG 3.0 mentre costruiscono oggi per la 2.2?
- Come reclutate e compensate con equità e rispetto i partecipanti disabili alla ricerca?

## Punti chiave

- L'accessibilità è un attributo di qualità di base e, per gli enti pubblici, un requisito di legge.
- Progetta secondo WCAG 2.2 AA come pavimento; usa i principi POUR come modello mentale.
- Prima l'HTML semantico; ARIA solo per colmare veri divari, fatta correttamente.
- Gli strumenti automatici colgono circa un terzo dei problemi; i test manuali e con tecnologie assistive sono essenziali.
- Testa con le persone disabili, non solo per loro.
- Costruire l'accessibilità dentro è economico e durevole; adattarla è costoso e fragile.
- Il design accessibile è un design migliore per tutti: l'effetto taglio del marciapiede è reale.

## Riferimenti e letture di approfondimento

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2* e documenti di supporto Understanding/Techniques
- W3C, *WAI-ARIA Authoring Practices Guide*
- W3C Web Accessibility Initiative (WAI), materiali introduttivi e tutorial
- Laura Kalbag, *Accessibility for Everyone*
- Sarah Horton e Whitney Quesenbery, *A Web for Everyone*
- Regine Gilbert, *Inclusive Design for a Digital World*
- Standard U.S. Section 508 e indicazioni di Section508.gov
- Standard europeo EN 301 549 e European Accessibility Act
- Indicazioni governative sull'accessibilità (per esempio il manuale sull'accessibilità del UK GDS)
- WebAIM, ricerche e articoli comprese le analisi annuali sull'accessibilità
