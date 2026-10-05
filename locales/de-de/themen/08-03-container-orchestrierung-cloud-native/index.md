# 8.3 Container, Orchestrierung, und Cloud-Native

## Überblick und Motivation

Ein [Container](https://en.wikipedia.org/wiki/OS-level_virtualization) verpackt eine Anwendung zusammen mit ihren Abhängigkeiten in eine einzelne, portable, isolierte Einheit. Er läuft auf dieselbe Weise auf einem Laptop, in einer Testumgebung, und in Produktion. Orchestrierungsplattformen, am prominentesten [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes), terminieren und verwalten große Zahlen von Containern über Flotten von Maschinen. Sie handhaben Platzierung, Skalierung, Gesundheit, Netzwerk, und Erholung. [Cloud-Native](https://en.wikipedia.org/wiki/Cloud-native_computing) ist der breitere Architekturstil, auf diesen Grundlagen gebaut: Anwendungen, gestaltet als lose gekoppelte, unabhängig deploybare, horizontal skalierbare Dienste, die eine dynamische, selbstheilende Infrastruktur annehmen.

Für große Teams lösen Container und Orchestrierung ein schweres Problem. Sie müssen viele Dienste, von vielen Teams gebaut, verlässlich und effizient auf geteilter Infrastruktur betreiben. Container geben jedem Team einen konsistenten Verpackungs- und Laufzeitvertrag, was die "funktioniert auf meiner Maschine"-Klasse von Fehlschlägen ausmustert. Orchestrierung versteckt individuelle Maschinen hinter einem gemeinsamen Substrat, damit Teams auf eine Plattform statt auf Server deployen. Diese Standardisierung ist, was Ihnen erlaubt, Hunderte oder Tausende Dienste zu betreiben, ohne dass jedes Team Deployment, Skalierung, und Resilienz neu erfindet.

Unternehmens- und Behördenübernehmerinnen gewinnen Portabilität, Resilienz, und einen Weg weg von Lock-in. Im Gegenzug erben sie echte Komplexität und neue Sicherheitsverantwortlichkeiten. Eine Container-Plattform ist mächtig genau, weil sie programmierbar und dynamisch ist, was bedeutet, Sie müssen sie sorgfältig verwalten. Image-Herkunft, Multi-Tenant-Isolation, Netzwerkrichtlinie, und Kosten werden alle Plattformebene-Anliegen. Übernehmerinnen im öffentlichen Sektor fügen zunehmend Souveränitätsanforderungen hinzu: Kontrolle darüber, wo Daten residieren und wer darauf zugreifen kann. Das macht die Fähigkeit, konsistente Workloads über gewählte Umgebungen zu betreiben, zu einer strategischen Fähigkeit, nicht nur einem technischen Detail.

## Kernprinzipien

- Verpacken Sie Anwendungen als kleine, einzweckige, unveränderliche Container-Images.
- Praktizieren Sie Image-Hygiene: minimale Basis-Images, gepinnte Versionen, auf Schwachstellen gescannt, und signiert.
- Gestalten Sie Anwendungen zustandslos und horizontal skalierbar, wo möglich, Zustand externalisierend.
- Behandeln Sie das Gewünschter-Zustand-Modell der Orchestrierungsplattform als Quelle der Wahrheit und lassen Sie es sich selbst heilen.
- Setzen Sie Isolation und geringstes Privileg zwischen Mandantinnen, Workloads, und Namespaces durch.
- Folgen Sie den [Twelve-Factor](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology)-Prinzipien, einer Methodik zum Bau wegwerfbarer, konfigurationsexternalisierter, horizontal skalierbarer Apps, und erweitern Sie sie für die Realitäten verteilter Systeme.
- Machen Sie Kosten zu einem erstklassigen, sichtbaren Engineering-Anliegen, keinem Nachgedanken.
- Bevorzugen Sie portable, standardbasierte Abstraktionen, um strategische Flexibilität zu bewahren.

## Empfehlungen

### Strenge Image-Hygiene praktizieren

Das Container-Image ist Ihre fundamentale Einheit von Vertrauen und Deployment, behandeln Sie es also so. Beginnen Sie mit minimalen, vertrauenswürdigen Basis-Images, um die Angriffsfläche zu schrumpfen. Pinnen Sie Abhängigkeits- und Basis-Image-Versionen für Reproduzierbarkeit. Scannen Sie jedes Image auf bekannte Schwachstellen in der Build-Pipeline, und blockieren Sie die mit kritischen Funden. Signieren Sie Images und verifizieren Sie Signaturen zur Deploy-Zeit, damit nur genehmigte, unmodifizierte Images laufen. Behalten Sie ein kuratiertes internes Register gehärteter Basis-Images, aus denen Teams bauen. Das verbreitet gute Sicherheitsstandards automatisch.

### Kubernetes-Muster nutzen statt sie neu zu erfinden

Kubernetes belohnt Teams, die seine etablierten Muster übernehmen, und bestraft Teams, die gegen sein Modell kämpfen. Nutzen Sie deklarative Manifeste für gewünschten Zustand. Fügen Sie Gesundheitsprüfungen hinzu, damit die Plattform ungesunde Instanzen erkennen und ersetzen kann. Setzen Sie Ressourcenanfragen und -limits, damit die Schedulerin Workloads sicher packen kann. Nutzen Sie horizontale Autoskalierung für elastische Nachfrage. Für operative Logik, die kontinuierlich laufen muss, wie eine Datenbank verwalten, Zertifikate rotieren, oder benutzerdefinierte Ressourcen versöhnen, nutzen Sie das Operator-Muster, das menschliches operatives Wissen in Software kodiert, die Zustand beobachtet und handelt. Widerstehen Sie dem Drang, maßgeschneiderte Orchestrierung auf der Plattform zu bauen. Bevorzugen Sie die nativen Konstrukte.

### Multi-Tenancy absichtlich gestalten

Wenn viele Teams einen Cluster teilen, ist Isolation eine Sicherheits- und Verlässlichkeitsanforderung, keine Nettigkeit. Nutzen Sie Namespaces als Mandantinnengrenzen. Setzen Sie Ressourcenquoten durch, damit keine Mandantin andere verhungern lassen kann. Wenden Sie Netzwerkrichtlinien an, um Traffic auf das explizit Erlaubte zu beschränken. Nutzen Sie [rollenbasierte Zugriffskontrolle](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC), um zu begrenzen, was jedes Team tun kann. Für Workloads mit stärkeren Isolationsbedürfnissen erwägen Sie separate Cluster oder stärkeres Sandboxing. Entscheiden Sie früh, ob Ihr Modell weiche Multi-Tenancy ist (vertrauenswürdige interne Teams) oder harte Multi-Tenancy (gegenseitig misstrauende Workloads), denn die zwei fordern sehr unterschiedliche Kontrollen.

### Cloud-native bauen, Twelve-Factor und darüber hinaus

Die Twelve-Factor-Methodik, mit ihren expliziten Abhängigkeiten, Konfiguration in der Umgebung, zustandslosen Prozessen, Wegwerfbarkeit, und so weiter, bleibt eine exzellente Baseline für Dienste, die auf einer dynamischen Plattform gedeihen. Erweitern Sie sie für die zusätzlichen Realitäten verteilter Systeme. Gestalten Sie für partiellen Fehlschlag. Machen Sie Operationen idempotent und wiederholbar. Exponieren Sie Gesundheit und Telemetrie. Behandeln Sie Beobachtbarkeit als eingebautes Feature statt Add-on. Externalisieren Sie allen Zustand zu verwalteten Datendiensten, damit Anwendungsinstanzen wegwerfbar und horizontal skalierbar bleiben.

### Multi-Cloud-, Hybrid-, und souveräne Strategien pragmatisch planen

Portabilität ist wertvoll, aber verfolgen Sie sie mit klaren Augen. Standardisieren Sie auf portablen Abstraktionen wie Containern, Kubernetes, und offenen APIs, damit Workloads sich bewegen können, falls nötig. Aber vermeiden Sie die Falle, jeden verwalteten Dienst abzulehnen, was echte Produktivität für hypothetische Portabilität tauscht. Für Hybrid- und Souveränitätsanforderungen gestalten Sie so, dass dieselben Workloads und Pipelines in einer gewählten Region, einem privaten Rechenzentrum, oder einer souveränen Cloud laufen können, die Rechtsprechungs- und Datenresidenzregeln erfüllt. Machen Sie die Souveränitäts- und Residenzgrenzen in Architektur und Richtlinie explizit.

### Kosten mit FinOps sichtbar machen

In elastischen Cloud-Umgebungen sind Kosten eine direkte Konsequenz von Engineering-Entscheidungen, geben Sie Ingenieurinnen also Sichtbarkeit und Rechenschaftspflicht. Taggen Sie Ressourcen für Kostenzuweisung. Weisen Sie Ausgaben Teams und Diensten zu. Zeigen Sie Kostendaten neben Performance-Kennzahlen. Bemessen Sie Workloads richtig, nutzen Sie Autoskalierung, um Nachfrage zu passen, und gewinnen Sie ungenutzte Ressourcen zurück. Etablieren Sie eine FinOps-Praxis, die Engineering, Finanz, und Produkt zusammenbringt, damit Cloud-Ausgaben eine geteilte, kontinuierliche Verantwortung werden statt einer vierteljährlichen Überraschung.

## Abwägungen: Vor- und Nachteile

| Wahl | Vorteile | Nachteile | Beste Passung |
|---|---|---|---|
| Kubernetes | Mächtig, portabel, riesiges Ökosystem | Steile Komplexität; Betriebslast | Viele Dienste im Maßstab |
| Verwalteter Container-Dienst | Weniger Ops-Last; schnellerer Start | Etwas Lock-in; weniger Kontrolle | Teams, die Einfachheit wollen |
| Einzelner geteilter Cluster | Effiziente Ressourcennutzung | Schwerere Isolation; Explosionsradius | Vertrauenswürdige interne Mandantinnen |
| Cluster pro Mandantin | Starke Isolation | Höhere Kosten und Overhead | Misstrauende oder regulierte Workloads |
| Multi-Cloud-Portabilität | Flexibilität; vermeidet Lock-in | Kleinster-gemeinsamer-Nenner-Dienste | Strategische Risikominderung |
| Tiefe Einzel-Cloud-verwaltete-Dienste | Maximale Produktivität | Anbieterabhängigkeit | Geschwindigkeitsfokussierte Teams |

Die übergreifende Abwägung ist Fähigkeit gegen Komplexität. Kubernetes und Cloud-native-Architekturen liefern Elastizität, Resilienz, und Geschwindigkeit. Aber sie legen eine substantielle Betriebs- und kognitive Last auf, die kleine Teams routinemäßig unterschätzen. Genauso tauscht volle [Multi-Cloud](https://en.wikipedia.org/wiki/Multicloud)-Portabilität Produktivität gegen Optionalität. Die richtige Antwort hängt von Maßstab und Risiko ab. Große Organisationen mit vielen Teams und starken Governance-Bedürfnissen rechtfertigen üblicherweise die Investition. Kleinere Bemühungen sind oft besser von verwalteten Diensten bedient, die die Komplexität verstecken.

## Fragen zur Diskussion mit Ihrem Team

1. **Signieren Sie Images und verifizieren Signaturen zur Deploy-Zeit, und blockiert eine kritische Schwachstelle tatsächlich den Build?** Das Image ist Ihre Vertrauenseinheit, die Lieferkette darum herum verdient also harte Tore, keine Warnungen. Entscheiden Sie, ob nur signierte, verifizierte Images laufen können, ob Scanning kritische Funde blockiert oder nur protokolliert, und wer das kuratierte Register gehärteter Basis-Images pflegt, aus denen Teams bauen. Für Unternehmens- und Behörden-Workloads ist das häufig eine Compliance-Anforderung, und es ist auch Ihre beste Verteidigung gegen eine vergiftete Abhängigkeit, die Produktion erreicht. Bringen Sie den aktuellen Zustand: welcher Anteil laufender Images kommt aus Ihrer gehärteten Basis, wie viele tragen ungepatchte kritische CVEs, und kann aktuell irgendein unsigniertes Image terminiert werden. Wenn ein kritischer Fund kein Deploy stoppt, ist Ihre Scannerin Dekoration.

2. **Wie verhindern Ressourcenanfragen, -limits, und -quoten, dass eine Workload ihre Nachbarn verhungern lässt, ohne teure Kapazität ungenutzt zu lassen?** Auf einem geteilten Cluster kann eine Workload ohne Limits alles um sie herum abstürzen oder drosseln, und zu großzügig gesetzte Quoten verschwenden die Auslastungsgewinne, die die Plattform rechtfertigen. Entscheiden Sie vernünftige Standards, wer sie tunt, und wie Sie Workloads ohne gesetzte Anfragen überhaupt erwischen. Im Maßstab ist das sowohl eine Verlässlichkeits- als auch eine Kostenkontrolle, denn Richtig-Bemessen ist, wo ein Großteil der FinOps-Ersparnis lebt. Bringen Sie Daten: aktuelle Cluster-Auslastung, wie oft Workloads evakuiert oder gedrosselt werden, und welche Namespaces keine Quoten haben. Das Ziel ist dichtes, sicheres Bin-Packing, behandeln Sie fehlende Limits also als Fehler, den die Plattform ablehnt.

3. **Welcher Zustand darf innerhalb eines Containers leben, und wohin geht alles andere?** Cloud-native Resilienz hängt von wegwerfbaren Instanzen ab, die die Plattform nach Belieben neu terminieren kann, und das hält nur, wenn wichtiger Zustand in verwalteten Datendiensten lebt statt auf der lokalen Disk des Containers. Entscheiden Sie die Regel explizit, denn Zustand, versehentlich in einem Container gespeichert, wird zu Datenverlust bei der nächsten Neuterminierung. Für Teams, die ältere Anwendungen migrieren, ist das oft der schwerste Teil, denn Legacy-Dienste nehmen ein stabiles lokales Dateisystem an. Bringen Sie ein Inventar: welche Dienste lokalen Zustand schreiben, welche sich auf klebrige Sitzungen oder Node-Affinität verlassen, und was es bräuchte, jede zu externalisieren. Bis Zustand extern ist, haben Sie Container, die elastisch aussehen, aber tatsächlich nicht bewegt werden können.

4. **Wenn viele Teams einen Cluster teilen, ist Ihr Isolationsmodell absichtlich als weiche oder harte Multi-Tenancy gewählt, und passen die Kontrollen zu dieser Wahl?** Namespaces trennen vertrauenswürdige interne Teams, aber sie enthalten keine Workload, die aktiv feindlich oder kompromittiert ist, und weiche Mandantschaft zu behandeln, als wäre sie hart, ist ein wartender Sicherheitsvorfall. Entscheiden Sie pro Workload, ob Mandantinnen nur faire Teilung brauchen oder angenommen werden müssen, einander zu misstrauen, passen Sie dann die Kontrollen: Namespaces, Quoten, Netzwerkrichtlinien, und RBAC für den weichen Fall, separate Cluster oder stärkeres Sandboxing für den harten Fall. Für eine große Organisation treibt diese Entscheidung Kosten direkt, denn ein Cluster pro Mandantin ist weit teurer als geteilte Namespaces, Sie wollen also das Isolationsbudget nur ausgeben, wo das Bedrohungsmodell es fordert. Bringen Sie das Mandantinneninventar: welche Workloads heute einen Cluster teilen, welche regulierten oder extern zugewandten Traffic handhaben, und wo Netzwerkrichtlinie noch standardmäßig-erlaubt ist. In Unternehmens- und Behördenumgebungen ist misstrauende Workloads unter weicher Mandantschaft zu mischen genau der Befund, den eine Prüferin markieren wird, benennen Sie die Grenze also, bevor sie es tun.

5. **Wie viel bezahlen Sie für Multi-Cloud-Portabilität, und werden Sie sie je tatsächlich nutzen?** Auf Containern, Kubernetes, und offenen APIs zu standardisieren hält Workloads beweglich, aber jeden verwalteten Dienst abzulehnen, um diese Option zu bewahren, tauscht echte, tägliche Produktivität gegen Portabilität, die die Organisation vielleicht nie ausübt. Entscheiden Sie, wo Portabilität eine echte Anforderung ist, wie eine Souveränitäts- oder Ausstiegspflicht, die Sie unterzeichnet haben, versus wo sie eine Trostdecke ist, die jedes Team verlangsamt. Die konkurrierende Überlegung ist Geschwindigkeit: tiefe verwaltete Dienste liefern Features schneller, und Kleinster-gemeinsamer-Nenner-Architektur ist eine stehende Steuer auf jedes Team. Bringen Sie den Beleg: welche verwalteten Dienste Sie vermieden haben und was das an Engineering-Zeit kostete, ob Sie je eine Workload zwischen Anbieterinnen bewegt haben, und was Ihre Verträge tatsächlich verpflichten. Für Behörden- und regulierte Übernehmerinnen können Datenresidenz- und souveräne-Cloud-Regeln Portabilität nicht verhandelbar machen, gestalten Sie also so, dass dieselben Manifeste und Pipelines in einer souveränen Region und einer privaten Enklave laufen, aber seien Sie ehrlich, dass das eine Compliance-Kostenposition ist, keine kostenlose Versicherung.

6. **Kann jedes Team sehen, was es ausgibt, und besitzt irgendjemand die Rechnung, bevor sie zur Überraschung wird?** In einer elastischen Plattform sind Kosten eine direkte Ausgabe von Engineering-Entscheidungen, doch ohne Kostenzuweisungs-Tags und sichtbare Dashboards häufen sich Ausgaben in einem geteilten Pool an, für den sich niemand verantwortlich fühlt, bis Finanz eskaliert. Entscheiden Sie, wie Sie Kosten Teams und Diensten zuweisen, wer sie prüft, und ob Ingenieurinnen Kosten neben Performance-Kennzahlen sehen oder nur einmal pro Quartal davon hören. Die Spannung ist zwischen Rechenschaftspflicht und Reibung: drücken Sie Kosten zu hart, und jede Entscheidung wird eine Budgetverhandlung, ignorieren Sie sie, und ungenutzte, überdimensionierte Workloads verdichten sich still. Bringen Sie die Zahlen: aktuelle Ausgaben nach Team, wie viel Kapazität ungenutzt oder überdimensioniert sitzt, und wie schnell eine außer Kontrolle geratene Workload bemerkt würde. Für Unternehmens- und Behördenbudgets sind unzugewiesene Cloud-Ausgaben sowohl ein Governance-Fehlschlag als auch ein echtes finanzielles Risiko, richten Sie also eine FinOps-Praxis ein, die Engineering, Finanz, und Produkt in dasselbe Gespräch bringt statt im Nachhinein zu versöhnen.

## Branchenperspektive

**Startup.** Greifen Sie zu einem verwalteten Container-Dienst statt eines selbstgehosteten Kubernetes-Clusters: mit ein paar Diensten und keiner Plattform-Ingenieurin sind Control Planes eine Ablenkung, die Sie sich nicht leisten können. Verpacken Sie kleine Images aus einer minimalen Basis, pinnen Sie Versionen, fügen Sie einen Schwachstellenscan zum Build hinzu, und schieben Sie allen Zustand in eine verwaltete Datenbank, damit Instanzen wegwerfbar bleiben. Überspringen Sie Namespaces, Operatoren, und Multi-Cloud-Portabilität, bis Sie tatsächlich die Dienste und die Leute haben, sie zu rechtfertigen.

**Kleinunternehmen.** Ohne dedizierte Plattformspezialistin und mit engem Budget, stützen Sie sich schwer auf verwaltete Dienste und lassen Sie die Anbieterin die Orchestrierung betreiben, die Sie sonst besetzen müssten. Behandeln Sie Container-Grundlagen als Ihren Sicherheitsboden: minimale Images, Versionspinning, und ein Scan in der Pipeline geben den meisten Schutz für wenig Aufwand. Bevorzugen Sie, eine unterstützte Plattform zu kaufen, über eine zu bauen, und behalten Sie genug Portabilität, Standard-Container und offene APIs, damit Sie nicht gefangen sind, falls sich Preisgestaltung oder Bedingungen ändern.

**Großunternehmen.** Die Aufgabe ist Plattform-Governance über viele Teams: ein zentrales Plattformteam, das gehärtete Basis-Images, Signierungs- und Scanning-Tore, Namespace-Mandantschaft mit Quoten, Netzwerkrichtlinie, und RBAC liefert, plus Kostenzuweisungs-Tags und ein FinOps-Dashboard. Standardisieren Sie den Deployment-Vertrag, damit Hunderte Dienste gleich operieren, und verwalten Sie Sicherheit, Multi-Tenancy, und Kosten zentral, während sich Teams Deployment selbst bedienen. Finanzieren Sie das Plattformteam angemessen, denn eine unterressourcierte Plattform wird der Engpass, auf den die ganze Organisation wartet.

**Behörde.** Souveränität, Datenresidenz, und öffentliche Rechenschaftspflicht formen die Architektur. Betreiben Sie Workloads auf Standard-Containern und Kubernetes, damit dieselben Pipelines in einer souveränen Region und einer akkreditierten On-Premises-Enklave laufen, und kodieren Sie Residenz- und Zugriffsgrenzen als Richtlinie statt Konvention. Ziehen Sie Images aus einem internen gehärteten Register, wenden Sie harte Multi-Tenancy auf die sensibelsten Daten an, und behalten Sie die Portabilität, die Ihnen Resilienz und Verhandlungshebel gibt, denn Beschaffungsregeln verbieten oft Ein-Anbieter-Lock-in.

## Beispiele

**Startup.** Ein sechsköpfiges Startup verpackt seine zwei Dienste als kleine Container-Images, aus einer minimalen Basis gebaut, und betreibt sie auf einem verwalteten Container-Dienst statt einem selbstgehosteten Kubernetes-Cluster, damit niemand Control Planes babysitten muss. Sie pinnen Basis-Image-Versionen und fügen einen Schwachstellenscan zu ihrem Build hinzu, aber sie überspringen absichtlich die schwereren Orchestrierungsfeatures, bis sie tatsächlich mehr als eine Handvoll Dienste haben. Zustand lebt in einer verwalteten Postgres-Datenbank, was die Container wegwerfbar hält und der Plattform erlaubt, sie ohne Datenverlust neu zu starten oder zu skalieren.

**Großunternehmen.** Eine Telekommunikationsfirma betreibt mehrere Hundert [Microservices](https://en.wikipedia.org/wiki/Microservices) auf geteilten Kubernetes-Clustern. Ein Plattformteam stellt gehärtete Basis-Images bereit, setzt Image-Signierung und Schwachstellentore durch, und isoliert Geschäftseinheiten in Namespaces mit Quoten, Netzwerkrichtlinien, und RBAC. Kostenzuweisungs-Tags und ein FinOps-Dashboard weisen jeder Produktlinie Ausgaben zu, und Autoskalierung bemisst Kapazität richtig zur Nachfrage. Produktteams deployen Dutzende Male am Tag auf eine konsistente Plattform ohne Server zu verwalten. Die Firma behält zentrale Kontrolle über Sicherheit und Kosten.

**Behörde.** Ein nationaler Gesundheitsdienst muss Bürgerinnendaten innerhalb nationaler Grenzen und unter nationaler rechtlicher Kontrolle halten. Er betreibt seine Workloads auf einer souveränen Cloud-Region, Standard-Container und Kubernetes nutzend, damit dieselben Pipelines und Manifeste auch in einer On-Premises akkreditierten Umgebung für die sensibelsten Daten laufen. Datenresidenz- und Zugriffsgrenzen sind als Richtlinie kodiert, Images werden aus einem internen gehärteten Register gezogen, und harte Multi-Tenancy isoliert sensible Workloads. Portabilität über die souveräne Region und die private Enklave gibt dem Dienst Resilienz und Verhandlungshebel ohne Compliance zu opfern.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Der ROI von Containern und Orchestrierung kommt aus höherer Ressourcenauslastung, schnelleren und verlässlicheren Deployments, elastischer Skalierung, die Ausgaben zu Nachfrage passt, und verbesserter Resilienz durch Selbstheilung. Auf einer gemeinsamen Plattform zu standardisieren reduziert duplizierten Aufwand über Teams und beschleunigt Onboarding, denn jeder Dienst folgt demselben Deployment- und Betriebsvertrag.

Die TCO-Analyse muss ehrlich über die Betriebslast sein. Übernahmekosten umfassen Plattform-Engineering-Personal, Training, Sicherheitswerkzeug für Images und Cluster, und den laufenden Aufwand, die Plattform selbst zu betreiben. Die Kosten der Nicht-Übernahme umfassen inkonsistentes maßgeschneidertes Deployment über Teams, schlechte Auslastung teurer Infrastruktur, brüchige manuelle Skalierung, und Schwierigkeit, Resilienz- und Souveränitätsanforderungen zu erfüllen. Für die Führung ruht der Fall auf Maßstab. Unter einer bestimmten Anzahl Dienste zahlt sich die Komplexität möglicherweise nicht aus, und ein verwalteter Dienst ist klüger. Aber im Unternehmens- und Behördenmaßstab ist eine verwaltete Cloud-native-Plattform typischerweise die kosteneffektivste und resilienteste Grundlage, vorausgesetzt Sie finanzieren das Plattformteam, sie richtig zu betreiben.

## Anti-Muster und Fallstricke

- **Fette, ungescannte Images.** Aufgeblähte Images, aus nicht vertrauenswürdigen Basen gebaut, tragen unnötige Schwachstellen und verlangsamen alles.
- **Kubernetes für alles.** Eine komplexe Orchestriererin für eine Handvoll einfacher Dienste zu übernehmen kauft Komplexität ohne Auszahlung.
- **Ressourcenlimits ignorieren.** Ohne Anfragen und Limits kann eine Workload ihre Nachbarn verhungern lassen oder zum Absturz bringen.
- **Weiche Mandantschaft für feindliche Workloads.** Sich allein auf Namespaces zu verlassen, misstrauende Mandantinnen zu isolieren, ist ein wartender Sicherheitsvorfall.
- **Zustandsbehaftete Container aus Versehen.** Wichtigen Zustand innerhalb wegwerfbarer Container zu speichern führt bei Neuterminierung zu Datenverlust.
- **Kostenblindheit.** Cloud-Ausgaben als fixen Overhead zu behandeln statt als Engineering-Ausgabe führt zu außer Kontrolle geratenen Rechnungen.
- **Portabilitätstheater.** Alle verwalteten Dienste abzulehnen, um Portabilität zu bewahren, die die Organisation nie tatsächlich nutzen wird.

## Reifegradmodell

**Stufe 1: Beginnen.** Container werden ad hoc genutzt, falls überhaupt. Images werden von Hand gebaut und ungescannt, Deployment ist manuell und reaktiv, und es gibt keine geteilte Plattform, Kostensichtbarkeit, oder Isolationsmodell.

**Stufe 2: Entwickeln.** Teams containerisieren Anwendungen und übernehmen eine Orchestriererin, aber Praktiken variieren zwischen Gruppen. Image-Scanning, Ressourcenlimits, und Signierung sind inkonsistent, und Kosten und Multi-Tenancy werden nicht systematisch verwaltet.

**Stufe 3: Standardisieren.** Eine standardisierte Plattform ist über die Organisation dokumentiert und durchgesetzt: gehärtete Basis-Images, Signierungs- und Scanning-Tore, Namespace-basierte Mandantschaft mit Quoten und Netzwerkrichtlinie, RBAC, und Kostenzuweisung. Cloud-native- und Twelve-Factor-Muster sind die erwartete Norm statt einer lokalen Wahl.

**Stufe 4: Steuern.** Die Plattform wird gegen Baselines gemessen und gesteuert. Sie verfolgen Cluster-Auslastung, den Anteil laufender Images, aus der gehärteten Basis gebaut, ungepatchte kritische Schwachstellen, Deployment-Frequenz und Änderungsfehlschlagsrate, Evakuierungs- und Drosselungsraten, und Kosten pro Team und Dienst gegen Budget. Tore werden auf diesem Beleg durchgesetzt: fehlende Ressourcenlimits und unsignierte Images werden automatisch abgelehnt, und Drift vom Standard löst Aktion aus statt einer Warnung.

**Stufe 5: Orchestrieren.** Die Plattform ist selbstbedienend und selbstheilend, über die Organisation integriert und adaptiv. FinOps bemisst und gewinnt Kapazität kontinuierlich richtig, portable Architektur unterstützt Hybrid- und Souveränitätsanforderungen, und die Plattform verbessert sich kontinuierlich aus gemessener Nutzung, Komponenten ausmusternd und ersetzend, während sich Workloads, Kosten, und das Risikobild verschieben.

## Diskussionsideen

- Bei welchem Maßstab hört die Übernahme von Kubernetes auf, Komplexität um ihrer selbst willen zu sein, und beginnt sich auszuzahlen?
- Wo ist die richtige Grenze zwischen weicher und harter Multi-Tenancy für Ihre Workloads?
- Wie viel sollten Sie in Multi-Cloud-Portabilität investieren gegen die Produktivität tiefer verwalteter Dienste?
- Wie geben Sie Ingenieurinnen echte Kostenrechenschaftspflicht, ohne jede Entscheidung zu einer Budgetverhandlung zu machen?
- Was ist Ihr Governance-Modell für Basis-Images, und wer pflegt das gehärtete Register?
- Wie formen Souveränitäts- und Datenresidenzanforderungen Ihre Plattformarchitektur?

## Wichtigste Erkenntnisse

- Container standardisieren Verpackung und Laufzeit; Orchestrierung standardisiert Betrieb im Maßstab.
- Image-Hygiene, gemeint minimale, gepinnte, gescannte, signierte Images, ist grundlegende Sicherheit.
- Nutzen Sie native Kubernetes-Muster und Operatoren statt maßgeschneiderte Orchestrierung zu bauen.
- Wählen Sie ein Multi-Tenancy-Modell absichtlich, basierend darauf, wie sehr sich die Workloads gegenseitig vertrauen.
- Folgen Sie Twelve-Factor und erweitern Sie es für verteilte-System-Realitäten wie partiellen Fehlschlag und Beobachtbarkeit.
- Behandeln Sie Kosten als Engineering-Ausgabe und verwalten Sie sie kontinuierlich durch FinOps.

## Referenzen und weiterführende Literatur

- Adam Wiggins, *The Twelve-Factor App* (Methodik)
- Brendan Burns, Joe Beda, und Kelsey Hightower, *Kubernetes Up & Running*
- Bilgin Ibryam und Roland Huß, *Kubernetes Patterns*
- Cornelia Davis, *Cloud Native Patterns*
- J.R. Storment und Mike Fuller, *Cloud FinOps*
- Liz Rice, *Container Security*
- Cloud Native Computing Foundation (CNCF), Cloud-native-Definition und -Landschaft
