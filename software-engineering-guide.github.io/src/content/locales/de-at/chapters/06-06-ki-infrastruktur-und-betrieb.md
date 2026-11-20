# 6.6 KI-Infrastruktur und -Betrieb

## Überblick und Motivation

KI-Infrastruktur und -Betrieb ist die Disziplin, die spezialisierte Rechen-, Speicher-, und Serving-Systeme bereitzustellen, zu planen, und zu betreiben, die KI-Workloads fordern, kosteneffektiv, verlässlich, und beobachtbar. Moderne KI ist teuer zu betreiben. Training und Serving großer Modelle fordern knappe Beschleuniger ([GPUs](https://en.wikipedia.org/wiki/Graphics_processing_unit) und [TPUs](https://en.wikipedia.org/wiki/Tensor_Processing_Unit)), Hochbandbreiten-Netzwerk, großmaßstäblichen Vektorspeicher für Retrieval (Daten als numerische Vektoren indizieren, damit ähnliche Elemente schnell gefunden werden können), und Serving-Schichten, getunt für Latenz und Durchsatz. Diese Infrastruktur richtig hinzubekommen ist der Unterschied zwischen KI, die nachhaltig skaliert, und KI, die still ein Budget verbraucht, während sie unterliefert.

Für große Teams sind die Kernprobleme Maßstab, Knappheit, und Kosten. Beschleuniger sind begrenzt und teuer, Terminierung und Auslastung zählen also enorm. Ungenutzte GPUs sind verbranntes Geld, und schlecht gebündelte Inferenz vervielfacht Kosten pro Anfrage. Retrieval-schwere Anwendungen brauchen [Vektordatenbanken](https://en.wikipedia.org/wiki/Vector_database), die schnell bleiben, während sie wachsen. Generative-KI-Anwendungen brauchen Prompt-Versionierung, Evaluationspipelines, und Beobachtbarkeit (manchmal LLMOps genannt), um sicher zu operieren und sich über Zeit zu verbessern. Ohne geteilte Infrastruktur und Betriebsdisziplin kämpft jedes Team dieselben Schlachten, und Kosten spiralieren.

Behörden und regulierte Organisationen fügen Anforderungen um Datensouveränität, Sicherheit, und vorhersagbare Ausgaben hinzu. Sie brauchen möglicherweise On-Premises- oder souveräne-Cloud-Bereitstellung, damit sensible Daten und Modelle kontrollierte Grenzen nie verlassen. Sie müssen Infrastrukturausgaben vorhersagen und rechtfertigen, und Sicherheits- und Verfügbarkeitsstandards erfüllen. KI-Infrastrukturentscheidungen in diesen Umgebungen tragen mehrjährige Konsequenzen, treffen Sie sie also mit Beschaffung, Sicherheit, und Ausstieg im Sinn.

## Kernprinzipien

- Behandeln Sie Beschleuniger-Rechenleistung als knappe, teure Ressource, die terminiert und ausgelastet werden muss, nicht gehortet.
- Optimieren Sie Kosten pro nützlicher Arbeitseinheit, nicht Rohkapazität.
- Bemessen Sie Modelle und Hardware passend zur Aufgabe; die größte Option ist selten die kosteneffektivste.
- Gestalten Sie Serving für Latenz und Durchsatz mit Bündelung und Caching als erstklassige Techniken.
- Machen Sie KI-Systeme beobachtbar: verfolgen Sie Kosten, Latenz, Qualität, und Fehler kontinuierlich.
- Versionieren und evaluieren Sie Prompts und Modelle mit derselben Strenge wie Code.
- Planen Sie für Portabilität und vermeiden Sie Lock-in bei Infrastruktur- und Serving-Wahlen.

## Empfehlungen

### Beschleuniger-Rechenleistung planen und kontrollieren

Prognostizieren Sie Nachfrage für Training und Inferenz separat, denn sie haben unterschiedliche Formen. Training ist stoßweise und terminierbar; Inferenz ist kontinuierlich und latenzempfindlich. Nutzen Sie Scheduler und Quoten, um knappe GPUs und TPUs über Teams zu teilen, Workloads zu priorisieren, und Auslastung hochzutreiben. Messen Sie Auslastung und behandeln Sie chronische Untätigkeit als zu behebendes Problem. Mischen Sie reservierte Kapazität für Grundlast mit On-Demand- oder Spot-Kapazität für Stöße, um Kosten zu kontrollieren. Erwägen Sie, ob günstigere oder kleinere Beschleuniger, oder CPU-Inferenz für leichtgewichtige Modelle, ausreichen würden. Wählen Sie zwischen Cloud, On-Premises, und Hybrid basierend auf Kosten in Ihrem Maßstab, Datensouveränitätsbedürfnissen, und Stoßmustern, und behalten Sie einen Ausstiegspfad.

### Retrieval-Infrastruktur bauen: Embeddings und Vektordatenbanken

Für Retrieval-augmentierte Anwendungen richten Sie Infrastruktur ein, um [Embeddings](https://en.wikipedia.org/wiki/Word_embedding) (numerische Vektorrepräsentationen, die ähnliche Elemente nahe beieinander platzieren) zu generieren und sie in einer Vektordatenbank zu speichern, die schnelle [Approximate-Nearest-Neighbor-Suche](https://en.wikipedia.org/wiki/Nearest_neighbor_search) (die ähnlichsten Vektoren finden, ohne jeden einzelnen erschöpfend zu vergleichen) in Ihrem Maßstab unterstützt. Planen Sie für drei Dinge: die Kosten und Latenz der Embedding-Generierung, Index-Frische, während sich Dokumente ändern, und die Betriebslast, Indizes konsistent zu halten. Evaluieren Sie, ob eine dedizierte Vektordatenbank, eine vektorfähige Erweiterung einer existierenden Datenbank, oder ein verwalteter Dienst am besten zu Ihrem Maßstab und Ihrer Lock-in-Toleranz passt. Überwachen Sie Retrieval-Latenz und -Recall, denn Retrieval-Qualität bestimmt direkt Anwendungsqualität.

### Model-Serving optimieren: Bündelung, Caching, und Latenz

Serving ist, wo Inferenzkosten und Nutzererfahrung entschieden werden. Nutzen Sie **Bündelung**, um mehrere Anfragen zusammen zu verarbeiten und Beschleuniger-Durchsatz zu erhöhen, Bündelgröße gegen Latenz balancierend. Nutzen Sie **Caching** aggressiv: cachen Sie identische oder semantisch ähnliche Anfragen, cachen Sie Embeddings, und nutzen Sie Prompt- oder Präfix-Caching, wo die Plattform es unterstützt, um erneutes Berechnen geteilten Kontexts zu vermeiden. Setzen Sie klare Latenzziele, und messen Sie Schwanzlatenz, nicht nur Durchschnitte. Routen Sie Anfragen an richtig bemessene Modelle: ein kleines Modell für einfache Fälle, ein größeres nur bei Bedarf. Autoskalieren Sie Serving nach Nachfrage, und Lasttesten Sie vor dem Start, damit Sie Ihre Kapazitäts- und Kostenkurve kennen.

### LLMOps praktizieren: Prompt-Versionierung, Evaluationspipelines, und Beobachtbarkeit

Behandeln Sie Prompts als versionierte Artefakte in Quellkontrolle, mit Prüfung und der Fähigkeit, zurückzurollen. Bauen Sie Evaluationspipelines, die Offline-Testsuiten automatisch durchführen, wann immer sich Prompts oder Modelle ändern, damit Sie Regressionen vor der Veröffentlichung erwischen. Instrumentieren Sie Produktion umfassend: protokollieren Sie Eingaben, Ausgaben, Latenz, Token-Nutzung, Kosten, und Fehler, mit Stichprobenahme und Datenschutz-Schutzmaßnahmen. Verfolgen Sie Qualitätssignale und Nutzerinnenfeedback online. Diese Beobachtbarkeit erlaubt Ihnen, Degradation zu erwischen, Kosten zu kontrollieren, Fehlschläge zu debuggen, und Systeme sicher zu verbessern: das Betriebsrückgrat generativer KI in Produktion.

### Kosten unnachgiebig und beobachtbar verwalten

Weisen Sie KI-Ausgaben Teams und Anwendungsfällen zu, damit Kosten sichtbar und besessen sind. Setzen Sie Budgets und Alarme, überwachen Sie Kosten pro Anfrage und pro Ergebnis, und überprüfen Sie regelmäßig die größten Kostentreiber. Ziehen Sie die Hebel, die Sie haben: Modell-Richtig-Bemessen, Caching, Bündelung, Prompt- und Kontext-Trimmen, und die günstigste Bereitstellung wählen, die Anforderungen erfüllt. KI-Kosten können auf überraschende Weisen mit Nutzung skalieren, kontinuierliche Kostenbeobachtbarkeit ist also essentiell, um unangenehme Überraschungen zu vermeiden.

## Abwägungen: Vor- und Nachteile

| Entscheidung | Option A | Option B | Abwägung |
|---|---|---|---|
| Rechenstandort | Cloud | On-Premises | Elastizität und niedrige Vorabkosten gegen Kontrolle, Souveränität, und stationäre Ökonomie |
| Kapazität | Reserviert | On-Demand/Spot | Vorhersagbare Kosten gegen Flexibilität und Unterbrechungsrisiko |
| Bündelgröße | Große Bündel | Kleine Bündel | Durchsatz und Kosten gegen Latenz |
| Modellgröße | Großes Modell | Kleines Modell | Qualität gegen Kosten und Geschwindigkeit |
| Vektorspeicher | Dedizierte Datenbank | Existierende Datenbankerweiterung | Performance im Maßstab gegen Einfachheit und weniger Systeme |
| Caching | Aggressiv | Minimal | Niedrigere Kosten und Latenz gegen Frische und Komplexität |

Die dominante Abwägung ist Kosten gegen Latenz und Qualität. Bündelung, Caching, und kleinere Modelle senken Kosten, können aber Latenz hinzufügen oder Qualität reduzieren. Die richtige Balance hängt von der Toleranz Ihrer Anwendung ab. On-Premises versus Cloud tauscht Kontrolle und stationäre Ökonomie gegen Elastizität und niedriges Commitment, eine Entscheidung, stark geformt von Datensouveränitätsbedürfnissen und Maßstab.

## Fragen zur Diskussion mit Ihrem Team

1. **Was sind unsere Kosten pro nützlichem Ergebnis heute, und welcher Hebel würde sie am meisten bewegen?** Rohkapazität und Pro-Anfrage-Durchschnitte verbergen die Zahl, die zählt: was es kostet, eine echte Werteinheit zu liefern, und wie das mit Nutzung skaliert. Für ein großes Team ist die Lücke zwischen einem optimierten und einem unoptimierten Deployment oft mehrfach in Ausgaben, diese Frage verwandelt also eine vage Sorge über die Rechnung in eine gerankte Liste von Fixes. Bringen Sie aktuelle Kostenzuweisung nach Team und Anwendungsfall, Pro-Anfrage- und Pro-Ergebnis-Trends, und die größten Kostentreiber. Diskutieren Sie die Hebel in Reihenfolge der Auszahlung: Modell-Richtig-Bemessen, Caching (einschließlich Präfix- und semantisches Caching), Bündelung, und Prompt- oder Kontext-Trimmen. In Behörden fügen Sie den Druck hinzu, mehrjährige Ausgaben vorherzusagen und zu rechtfertigen. Die Antwort sollte jedem Top-Kostentreiber eine Besitzerin und einen Hebel zuweisen, kein Achselzucken.

2. **Wenn unsere aktuelle Inferenz-Anbieterin morgen ihren Preis verdoppelte oder ausfiele, wie schnell könnten wir wechseln?** Stilles Lock-in ist leicht zu bauen und schmerzhaft zu entkommen, und Serving-Stacks sind, wo es sich am tiefsten versteckt. Für Unternehmen und besonders Behörden ist Portabilität eine Beschaffungs- und Kontinuitätsanforderung, keine Nettigkeit. Bringen Sie Ihre Architektur: ob Modelle hinter einer internen Schnittstelle sitzen, ob Prompts und Evaluationssuiten portabel sind, und wie viel anbieterspezifisches Serving-Verhalten Sie brauchen. Das zu beobachtende Signal ist, ob jemals jemand Ihre Evaluationssuite gegen eine zweite Anbieterin oder ein zweites Deployment-Ziel durchgeführt hat. Wenn Wechseln Monate dauern und Kernpfade neu schreiben würde, behandeln Sie das als Designfehler, jetzt zu adressieren, denn souveräne und On-Premises-Optionen könnten mit wenig Vorwarnung verpflichtend werden.

3. **Was ist unsere Beschleuniger-Auslastung gerade jetzt, und wie viel verbrennen ungenutzte GPUs und ungebündelte Inferenz?** Beschleuniger sind knapp und teuer, chronische Untätigkeit und Pro-Anfrage-Serving drainieren also still Budgets, die mehr Fähigkeit finanzieren könnten. Für eine große Organisation, die GPUs über Teams teilt, legt diese Frage offen, ob Terminierung, Quoten, und Prioritäten Auslastung tatsächlich hoch halten oder ob gehortete, ungenutzte Hardware die Norm ist. Bringen Sie echte Auslastungszahlen, Ihre Bündelungs- und Caching-Haltung, und Ihre Schwanzlatenz-Messungen, nicht nur Durchschnitte, denn Nutzerinnen fühlen den langsamen Schwanz. Diskutieren Sie, ob Trainings- und Inferenznachfrage separat prognostiziert werden, gegeben ihre unterschiedlichen Formen, und ob ein kleineres Modell oder CPU-Inferenz für leichtgewichtige Fälle ausreichen würde. Die Antwort sollte auf spezifische Untätigkeitskapazität zeigen, zurückzugewinnen, und spezifische Anfragen zu bündeln oder an ein richtig bemessenes Modell zu routen.

4. **Wenn eine Prompt- oder Modelländerung ausliefert, was hindert eine stille Qualitäts- oder Kostenregression daran, Nutzerinnen zu erreichen?** Ein Serving-Stack kann bei Latenz und Uptime gesund aussehen, während die Antworten, die er zurückgibt, still schlechter werden oder ein neuer Prompt Token-Nutzung pro Anfrage verdoppelt. Für ein großes Team, wo viele Gruppen Prompts unabhängig bearbeiten und Modelle tauschen, ist eine ungetortete Änderung ein wartender Produktionsvorfall, und der Explosionsradius wächst mit jedem Team auf der geteilten Plattform. Bringen Sie Ihre Evaluationsabdeckung: welche Prompts und Modelle haben Offline-Testsuiten, ob diese Suiten automatisch bei jeder Änderung laufen, welche Qualitäts- und Kostenschwellen eine Veröffentlichung torwächten, und wie schnell Sie zurückrollen können. Diskutieren Sie, ob Prompts in Quellkontrolle mit Prüfung leben, oder ob jemand immer noch einen Live-System-Prompt von Hand bearbeiten kann. In Unternehmens- und Behördenumgebungen binden Sie jede Änderung an eine Prüfspur und eine benannte Genehmigerin, denn eine Regulatorin, die fragt "wer änderte das und was testeten Sie", braucht eine Antwort, die aufgezeichnet ist, nicht erinnert.

5. **Wie entscheiden wir zwischen Cloud, On-Premises, und souveränem Deployment, und haben wir die echte stationäre Ökonomie bepreist statt das Pilotprojekt?** Die Rechenstandort-Wahl setzt Ihre Kostenkurve, Ihre Datensouveränitätshaltung, und Ihre Ausstiegsoptionen für Jahre, doch sie wird oft an der Cloud-Rechnung eines Pilotprojekts getroffen, die nichts wie Produktion im Maßstab aussieht. Für eine große Organisation ist elastische Cloud-Kapazität günstig zu starten und kann zur größten einzelnen Zeile werden, sobald Inferenz kontinuierlich läuft, während On-Premises niedriges Commitment gegen Kontrolle und stationäre Ökonomie tauscht. Bringen Sie prognostizierte Trainings- und Inferenzvolumina, den Break-even-Punkt, wo reservierte oder besessene Hardware On-Demand schlägt, Ihre Datenresidenz- und Sicherheitseinschränkungen, und die Stoßmuster, die für Hybrid sprechen. In Behörden und regulierten Umgebungen wägen Sie souveräne-Cloud- oder On-Premises-Anforderungen ab, die mit wenig Vorwarnung verpflichtend werden könnten, und bestätigen Sie, dass die Architektur Modelle hinter einer internen Schnittstelle hält, damit ein erzwungener Umzug keine Kernpfade neu schreibt.

6. **Besitzen wir tatsächlich unsere KI-Ausgaben, und kann jedes Team die Kosten sehen und dafür verantworten, die es treibt?** KI-Kosten skalieren mit Nutzung auf Weisen, die Menschen überraschen, und ohne Zuweisung landet die Rechnung als eine undurchsichtige Zahl, für die sich kein Team verantwortlich fühlt, zu schrumpfen. In einer großen Organisation ist Kosten, die niemand besitzt, Kosten, die niemand optimiert, die Frage ist also, ob Ausgaben Teams und Anwendungsfällen mit Budgets, Alarmen, und Pro-Ergebnis-Trends markiert sind, oder ob sie nur entdeckt werden, wenn Finanz eskaliert. Bringen Sie Ihr Kostenzuweisungsmodell, die größten Treiber nach Team, und die Hebel, die jede Besitzerin kontrolliert: Richtig-Bemessen, Caching, Bündelung, und Kontext-Trimmen. Für Unternehmens- und Behördenbudgets fügen Sie die Disziplin hinzu, mehrjährige Infrastrukturausgaben vorherzusagen und zu rechtfertigen, denn eine öffentliche Stelle, die ihre Rechenrechnung nicht Zeile für Zeile erklären kann, wird sie in einer Überprüfung schwer verteidigen können.

## Branchenperspektive

**Startup.** Besitzen Sie keine Infrastruktur, die Sie vermeiden können. Rufen Sie eine gehostete Inferenz-API auf, routen Sie einfache Anfragen an ein kleines günstiges Modell und reservieren Sie ein größeres für schwere Fälle, und cachen Sie aggressiv, damit wiederholte Prompts nichts kosten. Nutzen Sie eine verwaltete Vektordatenbank statt Ihre eigene zu betreiben, halten Sie Prompts in Git mit einem kurzen Evaluationsskript vor jeder Änderung, und protokollieren Sie Kosten pro Anfrage, damit eine außer Kontrolle geratene Rechnung erscheint, bevor sie wehtut. Ihre knappste Ressource ist Engineering-Aufmerksamkeit, kaufen Sie also Betreibbarkeit und halten Sie Wechsel günstig.

**Kleinunternehmen.** Ohne Plattformteam, behandeln Sie Serving, Retrieval, und Beobachtbarkeit als Dinge, die Sie in bereits genutzten Werkzeugen kaufen, keine Systeme, die Sie besetzen. Bevorzugen Sie verwaltete Inferenz und verwaltete Vektorsuche mit transparenter, vorhersagbarer Preisgestaltung, und setzen Sie von Tag eins eine harte Ausgabendecke und einen Abrechnungsalarm. Rahmen Sie die Entscheidung ehrlich als Kaufen versus Bauen: GPUs oder einen Vektorindex zu betreiben zahlt sich in Ihrem Volumen selten aus, und ein kleines Modell hinter einer gehosteten API erfüllt üblicherweise das Bedürfnis mit einem Bruchteil des Aufwands.

**Großunternehmen.** Das Problem ist eine geteilte, Paved-Road-Plattform über viele Teams: gepoolte Beschleuniger mit Schedulern, Quoten, und Prioritäten, um Auslastung hochzutreiben, Standard-Bündelung und -Caching, Richtig-Bemessen-Router, und Kosten, jedem Team und Anwendungsfall zugewiesen. Torwächten Sie Prompt- und Modelländerungen mit automatisierten Evaluationssuiten, standardisieren Sie die Schnittstellenschicht, damit Anbieterinnen und Deployment-Ziele austauschbar bleiben, und verwalten Sie Kosten pro Ergebnis als erstklassige Kennzahl statt dass jede Gruppe kostspielige, ungenutzte Infrastruktur neu erfindet.

**Behörde.** Datensouveränität, Sicherheit, und vorhersagbare Ausgaben formen jede Wahl. Bevorzugen Sie On-Premises- oder souveräne-Cloud-Bereitstellung, damit sensible Daten und Modelle innerhalb kontrollierter Grenzen bleiben, terminieren Sie knappe GPUs über Abteilungen mit Quoten, die Sie in Beschaffung rechtfertigen können, und prognostizieren Sie Kapazität, um mehrjährige Ausgaben Zeile für Zeile zu verteidigen. Versionieren und evaluieren Sie Prompts und Modelle mit einer aufgezeichneten Prüfspur, behalten Sie umfassende Beobachtbarkeit über Kosten und Qualität, und halten Sie Modelle hinter einer internen Schnittstelle, damit ein erzwungener Umzug zu einer neuen Anbieterin oder einer souveränen Plattform Sie nicht strandet.

## Beispiele

**Startup.** Ein kleines Startup, das ein KI-Schreib-Feature betreibt, hielt seine Rechnung vernünftig, ohne GPUs zu besitzen. Es rief eine gehostete Inferenz-API auf, routete einfache Anfragen an ein günstigeres kleines Modell und sparte das größere für schwere Fälle, und cachte Antworten auf wiederholte Prompts. Es speicherte seine Prompts in Git mit einem kurzen Evaluationsskript, das vor jeder Änderung lief, nutzte eine verwaltete Vektordatenbank für Retrieval, damit es keine betreiben musste, und protokollierte Kosten pro Anfrage, damit die Gründerinnen Ausgaben steigen sehen konnten, bevor sie zur Überraschung wurden.

**Großunternehmen.** Eine Medienfirma, die ein hochverkehr-LLM-Feature betreibt, senkte Inferenzkosten erheblich. Sie routete einfache Anfragen an ein kleines Modell und reservierte ein größeres Modell für schwere. Sie cachte Antworten auf wiederholte Abfragen und aktivierte Präfix-Caching für ihren geteilten System-Prompt. Sie führte GPUs durch einen geteilten Scheduler, um Auslastung hoch zu halten, versionierte alle Prompts in Git mit einer automatisierten Evaluationssuite, die Änderungen torwächtete, und instrumentierte Kosten pro Anfrage, damit jedes Produktteam seine Ausgaben besaß.

**Behörde.** Eine nationale Behörde mit strikten Datensouveränitätsregeln deployte ihre KI-Systeme On-Premises, damit sensible Daten und Modelle nie ihre kontrollierte Umgebung verließen. Sie terminierte knappe GPUs über Abteilungen mit Quoten und Prioritäten, prognostizierte Kapazität, um mehrjährige Beschaffung zu rechtfertigen, und baute eine Vektorsuchplattform für Retrieval über offizielle Dokumente. Prompts und Modelle wurden versioniert und vor Veröffentlichung evaluiert. Umfassende Beobachtbarkeit verfolgte Kosten und Qualität, und die Architektur hielt Modelle hinter einer internen Schnittstelle, um einen Ausstiegspfad zu bewahren und Lock-in zu vermeiden.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Die Motivation für disziplinierte KI-Infrastruktur ist unkompliziert. KI im Maßstab ist kostspielig, und die Lücke zwischen einem optimierten und einem unoptimierten Deployment ist oft mehrfach in Ausgaben. ROI kommt aus höherer Beschleuniger-Auslastung, niedrigeren Kosten pro Anfrage durch Bündelung und Caching, richtig bemessenen Modellen, und dem Vermeiden von Überprovisionierung. Beobachtbarkeit und Evaluationspipelines zahlen sich aus, indem sie kostspielige Vorfälle verhindern und sichere Iteration ermöglichen.

Gesamtbetriebskosten umspannen Beschleuniger-Rechenleistung (die größte Zeile für viele Workloads), Vektorspeicher, Serving-Infrastruktur, Netzwerk, und das Plattform- und Betriebspersonal, sie zu betreiben. Wägen Sie das gegen die Kosten der Nicht-Investition ab: außer Kontrolle geratene Inferenzrechnungen, schlechte Latenz, die Übernahme untergräbt, und Unfähigkeit zu skalieren. Für Behörden fügen Sie die Kosten hinzu, Souveränitäts- oder Sicherheitsanforderungen zu verfehlen. Machen Sie den Fall gegenüber der Führung, indem Sie Kosten-pro-Ergebnis-Trends und eine Paved-Road-Plattform zeigen, die vielen Teams erlaubt, KI effizient zu deployen, statt dass jedes kostspielige, ungenutzte Infrastruktur baut.

## Anti-Muster und Fallstricke

- **Ungenutzte Beschleuniger.** Knappe GPUs Teams widmen, die sie unterausgelastet lassen.
- **Keine Bündelung oder Caching.** Jede Anfrage individuell bedienen und geteilten Kontext erneut berechnen.
- **Standardmäßig größtes Modell.** Ein teures Modell nutzen, wo ein kleines ausreichen würde.
- **Kostenblindheit.** Keine Zuweisung, Budgets, oder Pro-Anfrage-Kostensichtbarkeit, bis die Rechnung ankommt.
- **Unversionierte Prompts.** Prompts in Produktion ändern ohne Versionierung oder Evaluationstor.
- **Schwanzlatenz-Vernachlässigung.** Durchschnittslatenz optimieren, während Nutzerinnen unter langsamen Schwänzen leiden.
- **Stilles Lock-in.** Tief auf dem Serving-Stack einer Anbieterin bauen, ohne Portabilität.

## Reifegradmodell

1. **Beginnen.** Ad-hoc-GPU-Zuweisung, reagierend auf wer auch immer am lautesten fragt, keine Bündelung oder Caching, keine Kostensichtbarkeit, bis die Rechnung ankommt, Prompts live und unversioniert bearbeitet, minimale Überwachung.
2. **Entwickeln.** Manche Teams übernehmen geteilte Terminierung, Caching, und versionskontrollierte Prompts, aber Praxis ist über die Organisation hinweg inkonsistent: eine Gruppe bündelt und evaluiert, während eine andere immer noch jede Anfrage individuell bedient und Prompts von Hand ändert.
3. **Standardisieren.** Eine dokumentierte Paved-Road-Plattform ist organisationsweit durchgesetzt: geteilte Terminierung mit Quoten und Prioritäten, Standard-Bündelung, -Caching, und -Richtig-Bemessen, Vektorinfrastruktur für Retrieval, automatisierte Evaluationspipelines, die jede Prompt- oder Modelländerung torwächten, und Kostenzuweisung an Teams und Anwendungsfälle.
4. **Steuern.** Die Plattform wird gegen Baselines gemessen und gesteuert: Beschleuniger-Auslastung, Kosten pro nützlichem Ergebnis, Schwanzlatenz, Retrieval-Recall, und Pro-Änderung-Qualitätsregressionen werden mit Alarmen und Schwellen verfolgt, Kosten sind von jedem Team besessen, und Go-oder-No-go bei einer Änderung wird auf Beleg statt Intuition entschieden.
5. **Orchestrieren.** Infrastruktur verbessert sich kontinuierlich und passt sich an: Routing, Bündelung, und Skalierung tunen sich selbst zu Live-Kosten- und Qualitätssignalen, Kapazität wird über Teams und zwischen Cloud-, On-Premises-, und souveränen Zielen neu balanciert, während sich Nachfrage und Einschränkungen verschieben, Portabilität wird geprobt, und Infrastrukturplanung ist mit Produkt, Sicherheit, und Beschaffung integriert.

## Diskussionsideen

- Wie treiben Sie Beschleuniger-Auslastung hoch, ohne Priorität-Workloads verhungern zu lassen?
- Wo ist die richtige Bündelungs- und Caching-Balance für Ihre Latenzanforderungen?
- Wann rechtfertigt On-Premises- oder souveränes Deployment seine Kosten über Cloud?
- Wie weisen Sie KI-Ausgaben über viele Teams zu und kontrollieren sie?
- Was sollte eine Prompt- oder Modelländerung vom Erreichen der Produktion torwächten?
- Wie halten Sie Serving-Infrastruktur portabel genug, um Anbieterinnen zu wechseln?

## Wichtigste Erkenntnisse

- Beschleuniger sind knapp und teuer; terminieren, teilen, und nutzen Sie sie absichtlich.
- Bündelung, Caching, und Modell-Richtig-Bemessen sind die primären Hebel für Kosten und Latenz.
- Retrieval-Anwendungen brauchen gut betriebene Embedding- und Vektorsuch-Infrastruktur.
- LLMOps (Prompt-Versionierung, Evaluationspipelines, und Beobachtbarkeit) ist das Betriebsrückgrat generativer KI.
- Verwalten Sie Kosten beobachtbar und bewahren Sie Portabilität, um Lock-in zu vermeiden.

## Referenzen und weiterführende Literatur

- Chip Huyen, *Designing Machine Learning Systems*
- Google, *Site Reliability Engineering* (Beyer, Jones, Petoff, Murphy, Herausgeber)
- Jared Kaplan et al., *Scaling Laws for Neural Language Models*
- Reza Yazdani Aminabadi et al., *DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale*
- Woosuk Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention* (vLLM)
- Andriy Burkov, *Machine Learning Engineering*
