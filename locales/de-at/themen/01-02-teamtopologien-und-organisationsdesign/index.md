# 1.2 Teamtopologien und Organisationsdesign

## Überblick und Motivation

Wie Sie Menschen in Teams aufteilen, bestimmt, welche Software Sie bauen können und wie schnell Sie sie bauen können. Das ist keine Metapher. Es ist eine nahezu mechanische Folge, bekannt als [Conways Gesetz](https://en.wikipedia.org/wiki/Conway%27s_law): Organisationen entwerfen Systeme, die ihre eigenen Kommunikationsstrukturen widerspiegeln. Wenn drei Teams einen [Compiler](https://en.wikipedia.org/wiki/Compiler) bauen, erhalten Sie einen Drei-Pass-Compiler. Wenn Ihre Zahlungslogik über ein Frontend-Team, ein Backend-Team und ein Datenbankteam verteilt ist, braucht jede Zahlungsänderung eine dreiseitige Koordination. Für eine kleine Organisation ist das handhabbar. Für eine große wird die Form des Organigramms zur dominanten Einschränkung Ihrer Technik, Ihrer Architektur, Ihrer Liefergeschwindigkeit und Ihrer Qualität. Das Gestalten der Teamstruktur ist also eine erstklassige technische Tätigkeit, kein nachträglicher HR-Gedanke.

Teamtopologien geben Ihnen ein bewusstes Vokabular für dieses Design. Statt Struktur zufällig durch Umstrukturierungen und Personalzahlen wachsen zu lassen, wählen reife Organisationen Teamtypen und Interaktionsmodi absichtlich und überdenken diese Wahl, während sich System und Geschäft weiterentwickeln. Das Ziel ist, die [kognitive Last](https://en.wikipedia.org/wiki/Cognitive_load) jedes Teams niedrig zu halten, also die Gesamtmenge, die ein Team im Kopf behalten muss, um effektiv zu sein, damit Teams ihre Domäne durchgängig besitzen und einen stetigen Wertfluss liefern können, ohne ständig auf andere zu warten.

Für Unternehmen und Behörden ist diese Disziplin entscheidend. Große Organisationen wuchern natürlich in tiefe Hierarchien, gemeinsame Dienste mit langen Warteschlangen und Übergabeketten, die aus einer Zweitagesänderung ein Zweimonatsprojekt machen. Behörden fügen Beschaffungsgrenzen, Auftragnehmerteams und vorgeschriebene [Funktionstrennungen](https://en.wikipedia.org/wiki/Separation_of_duties) hinzu, die die Verantwortung weiter zersplittern. Explizites Topologiedesign ist, wie diese Organisationen Fluss zurückgewinnen: Teams an Wertströme ausrichten, Plattformen bauen, die kognitive Last reduzieren, und Interaktionsmuster wählen, die Abhängigkeiten sichtbar und beabsichtigt statt verborgen und ständig machen.

## Kernprinzipien

- Conways Gesetz ist unausweichlich; gestalten Sie Teams so, dass sie zur gewünschten Softwaretechnik passen (das "umgekehrte Manöver").
- Optimieren Sie auf die kognitive Last des Teams, nicht auf die maximale Auslastung einzelner Personen.
- Bevorzugen Sie stream-ausgerichtete Teams, die einen Wertausschnitt durchgängig besitzen.
- Plattformen existieren, um die kognitive Last stream-ausgerichteter Teams zu reduzieren, nicht um Zugang zu bewachen.
- Machen Sie Teaminteraktionen explizit und wenige: Zusammenarbeit, X-als-Service oder Befähigung.
- Minimieren Sie Abhängigkeiten; jede teamübergreifende Übergabe ist eine Warteschlange und ein Risiko.
- Teamstruktur ist ein lebendiges Design, das sich weiterentwickeln muss, während sich System und Geschäft ändern.

## Empfehlungen

### Die vier grundlegenden Teamtypen nutzen

Teamtopologien definieren vier Teamtypen, die die meisten Bedürfnisse abdecken. Stream-ausgerichtete Teams sind der Standard: Jedes besitzt einen kontinuierlichen Arbeitsfluss für ein bestimmtes Produkt, einen Dienst oder eine Nutzerreise, durchgängig. Plattformteams liefern interne Produkte (Rechenleistung, Bereitstellung, Datenpipelines, Identität), die stream-ausgerichtete Teams im Selbstbedienungsmodus konsumieren, was ihre kognitive Last senkt. Befähigungsteams sind Spezialisten (Testen, Sicherheit, Beobachtbarkeit), die stream-ausgerichtete Teams coachen, eine Fähigkeit aufzubauen, und sich dann zurückziehen. Complicated-Subsystem-Teams besitzen Komponenten, die tiefes Spezialwissen erfordern (eine Preis-Engine, ein [Video-Codec](https://en.wikipedia.org/wiki/Video_codec), ein kryptografisches Modul), bei denen es keinen Sinn ergibt, dass jedes Team dieses Wissen hält. Die meisten Ihrer Teams sollten stream-ausgerichtet sein; die anderen drei Typen existieren, um sie zu unterstützen.

### Das umgekehrte Conway-Manöver anwenden

Da Software die Struktur Ihrer Organisation widerspiegelt, gestalten Sie Ihre Teams so, dass sie die gewünschte Software hervorbringen. Wollen Sie lose gekoppelte Dienste mit klaren Grenzen? Bilden Sie lose gekoppelte Teams mit klaren Verantwortungsgrenzen. Wollen Sie eine Zahlungsfähigkeit, die nach ihrem eigenen Zeitplan ausgeliefert wird? Bilden Sie ein Zahlungsteam, das sie von vorn bis hinten besitzt. Bekämpfen Sie Conways Gesetz nicht mit heldenhafter Koordination. Zeichnen Sie die Teamgrenzen neu, damit die gewünschte Architektur zum Weg des geringsten Widerstands wird.

### Kognitive Last explizit steuern

Ein Team kann nur so viel meistern. Kognitive Last umfasst die Domänenkomplexität, die Technologien, die Betriebslast und die Breite der Stakeholder. Wenn ein Team zu viele unzusammenhängende Dienste besitzt, brechen Qualität und Geschwindigkeit beide zusammen. Begrenzen Sie also die Verantwortlichkeiten jedes Teams auf eine Domäne, die es wirklich meistern kann, und nutzen Sie Plattformen und Befähigungsteams, um unspezifische Komplexität von seinem Teller zu nehmen. Halten Sie Teams bei etwa fünf bis neun Personen: klein genug, um leicht zu kommunizieren und sozusagen von ein paar Pizzen ernährt zu werden.

### Interaktionsmodi bewusst wählen

Beschränken Sie Teaminteraktionen auf drei Modi. Zusammenarbeit ist enge, hochbandbreitige Arbeit zwischen zwei Teams für einen festgelegten Zeitraum; sie ist mächtig für Entdeckung, aber teuer, halten Sie sie also vorübergehend. X-als-Service ist eine saubere Anbieter-Konsumenten-Beziehung mit einer klar definierten Schnittstelle, ideal für Plattformkonsum im großen Maßstab. Befähigung ist, wenn ein Team einem anderen beim Lernen hilft, was Befähigungsteams tun. Benennen Sie den Modus für jede wichtige teamübergreifende Beziehung, und lesen Sie lang anhaltende Zusammenarbeit zwischen denselben zwei Teams als Signal, dass ihre Grenze am falschen Ort liegt.

### Ein Betriebsmodell für übergreifende Funktionen wählen

Sicherheit, Daten, Design und ähnliche Disziplinen können auf drei Arten organisiert werden: zentralisiert (ein Team besitzt sie für alle), föderiert (Spezialisten teilzeit eingebettet, koordiniert über eine Gilde) oder eingebettet (ein dedizierter Spezialist in jedem stream-ausgerichteten Team). Zentralisierung gibt Ihnen Konsistenz und Tiefe, wird aber zum Engpass. Einbettung gibt Ihnen Geschwindigkeit und Kontext, riskiert aber Inkonsistenz und Duplikation. Föderation (oft ein Nabe-und-Speiche- oder [Community-of-Practice](https://en.wikipedia.org/wiki/Community_of_practice)-Modell) liegt zwischen den beiden. Wählen Sie je Funktion und je Maßstab. Die meisten großen Organisationen landen für diese Disziplinen bei Föderation, mit einem kleinen zentralen Kern, der Standards setzt.

### In InnerSource investieren

[InnerSource](https://en.wikipedia.org/wiki/Inner_source) bringt [Open-Source](https://en.wikipedia.org/wiki/Open-source_software)-Zusammenarbeitsmuster ins Innere der Organisation: gemeinsame interne Repositorys, veröffentlichte Beitragsrichtlinien, [Code-Review](https://en.wikipedia.org/wiki/Code_review) über Teamgrenzen hinweg und klare Maintainer. Wenn ein Team eine Änderung an der Komponente eines anderen Teams braucht, kann es die Änderung direkt beisteuern, statt ein Ticket einzureichen und in einer Warteschlange zu warten. Das entlastet teamübergreifende Abhängigkeiten, ohne Verantwortung aufzulösen, und verbreitet Wissen und Standards natürlich über eine große Belegschaft.

## Abwägungen: Vor- und Nachteile

| Modell für übergreifende Funktionen | Vorteile | Nachteile |
| --- | --- | --- |
| Zentralisiert (ein Team für alle) | Konsistenz, tiefes Fachwissen, klare Standards | Engpass, Warteschlangen, Verlust des Produktkontexts |
| Föderiert (Nabe-und-Speiche, Gilden) | Balanciert Konsistenz und Geschwindigkeit; teilt Wissen | Erfordert Koordinationsdisziplin; Rechenschaftspflicht kann verschwimmen |
| Eingebettet (Spezialist pro Team) | Schnell, kontextreich, hohe Verantwortung | Duplikation, Inkonsistenz, schwer im großen Maßstab zu besetzen |

| Teamtyp | Am besten für | Risiko bei Übernutzung |
| --- | --- | --- |
| Stream-ausgerichtet | Die meiste Produkt- und Dienstlieferung | Keines; dies sollte dominieren |
| Plattform | Reduzierung gemeinsamer kognitiver Last | Wird zum Elfenbeinturm-Wächter |
| Befähigung | Vorübergehende Verbreitung einer Fähigkeit | Wird zu einer dauerhaften Abhängigkeit |
| Complicated-Subsystem | Wirklich tiefe Spezialdomänen | Wird als Ausrede genutzt, um gewöhnliche Arbeit zu horten |

Die wiederkehrende Abwägung ist Autonomie gegen Konsistenz. Vollständig autonome Teams bewegen sich schnell, driften aber bei Standards, Werkzeugen und Sicherheitshaltung auseinander. Vollständig zentralisierte Kontrolle hält Dinge konsistent, erdrosselt aber den Fluss. Gutes Topologiedesign findet die Naht: Autonomie für stream-ausgerichtete Lieferung, plus dünne zentrale Standards und ausgebaute Plattformen (gut unterstützte Standardwerkzeuge, die die konforme Wahl zur einfachen machen) für die Dinge, die wirklich konsistent sein müssen.

## Fragen zur Diskussion mit Ihrem Team

1. **Welche konkreten Signale sagen Ihnen, dass die kognitive Last eines Teams zu hoch ist, bevor die Qualität zusammenbricht?** "Begrenzen Sie jedes Team auf eine Domäne, die es meistern kann" ist leicht zu sagen und schwer ohne Belege umzusetzen, denn kognitive Last bleibt unsichtbar, bis Lieferung und Zuverlässigkeit sich verschlechtern. Achten Sie auf messbare Symptome: die Zahl unzusammenhängender Dienste oder Repositorys, die ein Team besitzt, wie lange Onboarding dauert, wie viele Domänen eine einzelne Ingenieurin in einer Woche wechseln muss, und steigende Vorfallraten in den Randbereichen der Zuständigkeit eines Teams. Für eine große Organisation zählt das, weil überlastete Teams still zu Engpässen werden, die kein Umstrukturierungsdiagramm vorhersagt. Bringen Sie diese Zahlen in die Diskussion ein, plus das eigene Gefühl des Teams dafür, was es im Kopf behalten kann und was nicht. Wenn die Signale Überlastung anzeigen, besteht der Schritt darin, unspezifische Arbeit auf eine Plattform oder ein Befähigungsteam abzuwälzen, nicht mehr Heldentum zu fordern.

2. **Ist eine Umstrukturierung hier wirklich die Störung wert, oder befeuern Sie eine Umstrukturierungssucht?** Grenzen für das umgekehrte Conway-Manöver neu zu ziehen ist mächtig, und jede Umstrukturierung zerstört auch die Stabilität, die Teams brauchen, um sich zu formen, und setzt hart erarbeitetes Domänenwissen zurück. Die konkurrierenden Erwägungen sind die laufende Koordinationssteuer der aktuellen Struktur gegen die einmaligen Kosten und den Moralschaden einer Änderung. In Unternehmens- und Behördenumgebungen machen Beschaffungsgrenzen, Auftragnehmerteams und vorgeschriebene Funktionstrennungen Umstrukturierungen langsamer und teurer, die Messlatte sollte also höher liegen. Bringen Sie Belege für abhängigkeitsbedingte Verzögerung: wie viele Initiativen darauf warten, dass ein anderes Team liefert, und für wie lange. Strukturieren Sie um, wenn dieses Warten strukturell und groß ist, und widerstehen Sie der Umschichtung, wenn der Schmerz vorübergehend ist oder günstiger durch InnerSource-Beiträge und klarere Schnittstellen gelöst werden könnte.

3. **Für Sicherheit, Daten und Design: Welches Ereignis wird Sie dazu bringen, zwischen eingebettet, föderiert und zentralisiert zu wechseln?** Die Empfehlung des Kapitels lautet, je Funktion und je Maßstab zu wählen, und die schwierigere Disziplin ist, im Voraus zu entscheiden, welches Wachstum oder Risiko Sie diese Wahl überdenken lässt. Ein Modell, das für fünfzig Ingenieurinnen passt, kann bei fünfhundert zum Engpass oder zur Konsistenzkatastrophe werden, und besonders Unternehmen und Behörden müssen benennen, welche Standards ein kleiner zentraler Kern immer halten wird. Bringen Sie die aktuellen Wartezeiten und Konsistenzlücken für jede Funktion mit: ein zentrales Sicherheitsteam mit mehrwöchigen Prüfungswarteschlangen ist ein Signal zu föderieren, während eingebettete Spezialisten, die inkompatible Datenmodelle produzieren, ein Signal sind, einen zentralen Standardkern hinzuzufügen. Entscheiden Sie den Auslöser jetzt, etwa eine Schwelle für Warteschlangenlänge oder einen Prüfungsbefund, damit die Änderung zu einer geplanten Evolution wird statt einer Krisenreaktion. Die Antwort bestimmt, wo Sie in ausgebaute Pfade und Fürsprecher investieren gegenüber einem zentralen Knotenpunkt.

4. **Wie werden Sie wissen, ob Ihr Plattformteam wirklich kognitive Last senkt oder still zum Wächter wird?** Eine Plattform existiert, um die konforme, verlässliche Wahl durch Selbstbedienung zur einfachen zu machen, und dasselbe Team kann abdriften zum Vorschreiben von Werkzeugen, zum Handprüfen jeder Anfrage und zum Hinzufügen genau der Reibung, die es beseitigen sollte. Für eine große Organisation entscheidet dieser Unterschied, ob sich die Plattforminvestition auszahlt oder zu einem zentralen Engpass wird, hinter dem jedes stream-ausgerichtete Team wartet. Die konkurrierenden Erwägungen sind Konsistenz und Kontrolle auf der einen Seite gegen Konsumentenautonomie und Fluss auf der anderen. Bringen Sie Belege, die ein Konsument anerkennen würde: wie lange es dauert, bis ein stream-ausgerichtetes Team sich eine neue Umgebung oder Pipeline selbst bedient, ohne ein Ticket einzureichen, das Verhältnis von Selbstbedienungsaktionen zu menschlich vermittelten, und Plattformakzeptanz gemessen an Teams, die sie wählen, statt Teams, die dazu gezwungen werden. In Unternehmens- und Behördenumgebungen bestehen Sie darauf, dass die Plattform Prüfungs- und Compliance-Belege automatisch erzeugt statt durch manuelle Tore, denn eine Plattform, die Funktionstrennungsregeln erfüllt, indem sie eine menschliche Prüferin einfügt, hat den Engpass neu erschaffen, den sie beseitigen sollte.

5. **Welche Ihrer teamübergreifenden Beziehungen haben sich zu dauerhafter Zusammenarbeit verfestigt, und was würde jede in eine saubere Servicegrenzfläche oder eine neu gezogene Grenze verwandeln?** Zusammenarbeitsmodus soll intensiv und vorübergehend sein, und ein Pairing, das nie endet, ist normalerweise ein Signal, dass Verantwortung am falschen Ort liegt oder dass die Schnittstelle zwischen zwei Teams nie explizit gemacht wurde. Das zählt im großen Maßstab, weil unbenannte, dauerhafte Zusammenarbeit ist, wo sich Koordinationskosten verstecken: Sie erscheint auf keinem Organigramm, besteuert aber jede Änderung, die die beiden Teams berühren. Die konkurrierenden Erwägungen sind der Entdeckungswert des Nahbleibens gegen den Fluss, den Sie gewinnen, wenn Sie die Beziehung in einen X-als-Service-Vertrag mit definierter Schnittstelle verwandeln, oder indem Sie die Verantwortung in ein einziges Team zusammenführen. Bringen Sie die Liste der Teampaare, die seit mehr als einem Quartal kontinuierlich zusammenarbeiten, die Änderungen, die in den letzten Monaten beide Teams erforderten, und ob eine stabile Schnittstelle zwischen ihnen niedergeschrieben werden könnte. Für Unternehmens- und Behördenkontexte, wo Auftragnehmergrenzen und Beschaffungslose eine Übergabe jahrelang einfrieren können, benennen Sie, welche Beziehungen Sie mit einer Schnittstelle und InnerSource-Beiträgen umwandeln können und welche vertraglich fixiert sind und als explizite Abhängigkeiten verwaltet werden müssen.

6. **Wenn ein Befähigungsteam einem anderen Team hilft, eine Fähigkeit aufzubauen, wie werden Sie wissen, dass es erfolgreich war und sich zurückziehen kann, statt zu einer dauerhaften Abhängigkeit zu werden?** Befähigungsteams sollen ein stream-ausgerichtetes Team coachen, Testen, Sicherheit oder Beobachtbarkeit zu meistern, und dann weiterziehen, und ohne eine explizite Austrittsbedingung verhärtet sich die Coaching-Beziehung zu einem dauerhaften Dienst, den das stream-ausgerichtete Team nie wirklich aufnimmt. Für eine große Organisation ist das der Unterschied zwischen einer Fähigkeit, die sich über Dutzende Teams verbreitet, und einem neuen gemeinsamen Engpass, der sich jedes Jahr schlechter skaliert. Die konkurrierenden Erwägungen sind die Tiefe und Konsistenz, die ein Spezialistenteam bietet, gegen die Autonomie und durchgängige Verantwortung, die Sie in stream-ausgerichtete Teams einbauen wollen. Bringen Sie Belege für Fähigkeitstransfer: ob das empfangende Team die Arbeit jetzt ohne Anwesenheit des Befähigungsteams handhabt, wie vielen Teams eine feste Befähigungsgruppe gleichzeitig verpflichtet ist, und wie lange jedes Engagement über seine vorgesehene Übergabe hinaus gelaufen ist. In Unternehmens- und Behördenumgebungen, wo eine knappe Spezialistenfähigkeit hinter einem einzigen zentralen Team oder einem einzigen Vertrag sitzen kann, entscheiden Sie im Voraus, wie Sie Fähigkeitstransfer und Fürsprecher finanzieren, damit sich Fachwissen in Lieferteams verbreitet, statt hinter einer Warteschlange verschlossen zu bleiben, auf die jede Prüfung und jede Veröffentlichung warten muss.

## Branchenperspektive

**Startup.** Mit einer Handvoll Ingenieurinnen und wenig Reichweite ist die richtige Topologie ein einziges stream-ausgerichtetes Team, das das gesamte Produkt besitzt, und die Disziplin besteht darin, sich zu weigern, Silos zu schaffen, bevor Sie sie brauchen. Widerstehen Sie der Versuchung, eine einsame "DevOps"- oder "QA"-Person einzustellen, die zum Tor wird; falten Sie diese Fähigkeiten als eingebettete Fähigkeit in das eine Team. Halten Sie Conways Gesetz für sich arbeiten, indem Sie die Organisation flach halten, damit die Architektur so einfach und veränderbar bleibt wie das Team.

**Kleinunternehmen.** Sie werden kein dediziertes Plattform- oder Befähigungsteam besetzen, kaufen Sie also die Plattform: Nutzen Sie verwaltete Cloud-Dienste, gehostete Pipelines und fertige Sicherheitswerkzeuge, um unspezifische kognitive Last von Ihren ein oder zwei Teams zu nehmen. Betrachten Sie übergreifende Belange wie Sicherheit und Daten als Dinge, die Sie konfigurieren und konsumieren, statt als Funktion, die Sie bauen. Reservieren Sie jede maßgeschneiderte Verantwortung für das eine komplizierte Teilsystem, das Sie wirklich differenziert, und lassen Sie Anbieter den Rest tragen.

**Großunternehmen.** Im großen Maßstab ist das Problem Koordinationskosten über viele Teams, machen Sie Topologie also zu einem expliziten, geregelten Design: eine gemeinsame Taxonomie der vier Teamtypen, benannte Interaktionsmodi, eine ausgebaute Plattform und InnerSource, um teamübergreifende Warteschlangen zu entlasten. Verfolgen Sie abhängigkeitsbedingte Verzögerung und Team-kognitive-Last als Portfoliokennzahlen, und führen Sie Umstrukturierungen als bewusste Evolutionen mit hoher Messlatte durch statt als jährlichen Reflex. Ein dünner zentraler Kern hält die Standards, die konsistent sein müssen, während stream-ausgerichtete Teams Autonomie über die Lieferung behalten.

**Behörde.** Beschaffungsregeln, Auftragnehmergrenzen und vorgeschriebene Funktionstrennungen zersplittern Verantwortung, gestalten Sie Topologie also so, dass sie diese Zwänge durch Werkzeuge und klare Schnittstellen statt menschliche Übergaben erfüllt. Bevorzugen Sie föderierte Modelle mit einem kleinen Standardkern und einer Plattform, die Prüfungs- und Compliance-Belege automatisch erzeugt, damit Funktionstrennung durch Pipelines statt Prüfungswarteschlangen durchgesetzt wird. Dokumentieren Sie Teamgrenzen, Interaktionsmodi und das Betriebsmodell offen, damit Struktur für Prüfer, Aufsichtsgremien und die Öffentlichkeit, die sie finanziert, transparent ist.

## Beispiele

**Startup.** Ein zehnköpfiges Startup hat ein einziges stream-ausgerichtetes Team, das das gesamte Produkt durchgängig besitzt, was in seinem Maßstab genau richtig ist: keine Übergaben, keine Koordinationssteuer, alle teilen denselben Kontext. Probleme beginnen, als sie eine dedizierte "DevOps-Person" und eine separate "QA-Person" einstellen und versehentlich funktionale Silos neu erschaffen, sodass jede Veröffentlichung jetzt auf zwei Personen wartet. Sie korrigieren den Kurs, indem sie diese Einstellungen als eingebettete Plattform- und Testfähigkeit innerhalb des einen Teams behandeln, statt als Tore, durch die Arbeit gehen muss. Bei dieser Größe ist die günstigste Topologie die, die alle in einem einzigen Fluss hält.

**Großunternehmen.** Der Checkout eines großen Einzelhändlers ließ sich nur langsam ändern, weil Frontend-, Backend- und Erfüllungslogik über drei funktional organisierte Teams verteilt waren, was jede Änderung durch drei Backlogs zwang. Durch Anwendung des umgekehrten Conway-Manövers strukturierten sie sich in stream-ausgerichtete Teams um Kundenreisen ("Stöbern", "Warenkorb und Checkout", "Nach dem Kauf"), von denen jedes seinen Ausschnitt von vorn bis hinten besaß, unterstützt von einem Plattformteam, das Bereitstellung und Beobachtbarkeit als Service lieferte. Checkout-Änderungen, die früher ein Quartal dauerten, wurden jetzt in Tagen ausgeliefert, weil die Koordination, die früher über Teams verlief, jetzt innerhalb eines einzigen geschah.

**Behörde.** Eine staatliche Steuerbehörde betrieb ein zentrales Sicherheitsteam, das jede Veröffentlichung prüfte und eine mehrwöchige Warteschlange schuf, die kritische Korrekturen verzögerte. Sie wechselten zu einem föderierten Modell: Eine kleine zentrale Sicherheitsfunktion setzte Standards und lieferte einen "ausgebauten Pfad" vorab genehmigter, automatisch gescannter Pipelines, während Sicherheitsfürsprecher, teilzeit in jedem Lieferteam eingebettet, die täglichen Entscheidungen handhabten. Die Plattform erzeugte Compliance-Belege automatisch. Vorgeschriebene Funktionstrennungsanforderungen wurden weiterhin erfüllt, aber durch Werkzeuge und klare Schnittstellen statt einen menschlichen Engpass, was die Veröffentlichungsvorlaufzeit dramatisch verkürzte und gleichzeitig die Prüfungsbereitschaft verbesserte.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Sie zahlen für schlechtes Teamdesign in Koordinationsaufwand, und dieser Aufwand wächst schneller als linear mit der Zahl der Teams, die sich für eine typische Änderung synchronisieren müssen. Jede Übergabe ist eine Warteschlange mit Wartezeit, ein Kontexttransfer, der Informationen verliert, und eine neue Gelegenheit zum Missverständnis. Wenn eine routinemäßige Änderung drei Teams braucht, um ihre Roadmaps abzustimmen, sind die echten Kosten nicht die Summe ihrer Arbeit; es sind die weit größeren Kosten von Terminplanung, Warten und Nacharbeit. Zeichnen Sie Grenzen neu, sodass die meisten Änderungen in die Verantwortung eines einzigen Teams passen, und dieser Aufwand verschwindet einfach.

Die Einführungskosten sind real. Umstrukturierungen sind störend, und der Aufbau von Plattformen und InnerSource-Praktiken erfordert Vorabinvestition, bevor sich die Auszahlung einstellt. Aber die Kosten des Nichteinführens summieren sich. Organisationen, die Struktur zufällig wachsen lassen, häufen Übergabeketten, gemeinsame Engpassteams mit quartalslangen Warteschlangen und Architekturen an, die vom Organigramm versteinert sind. Um Führungskräften den Fall darzulegen, messen Sie abhängigkeitsbedingte Verzögerung: wie viele aktive Initiativen darauf warten, dass ein anderes Team liefert, und für wie lange. Plattform- und Topologieinvestitionen zahlen sich normalerweise aus, indem sie dieses Warten in Fluss verwandeln, was sich als kürzere Vorlaufzeiten und höherer Durchsatz zeigt, ohne Personal hinzuzufügen.

## Anti-Muster und Fallstricke

- Conways Gesetz ignorieren: eine Architektur entwerfen, die die Organisationsstruktur nicht liefern kann.
- Funktionale Silos: getrennte Frontend-, Backend-, QA- und Betriebsteams, die für jede Änderung koordinieren müssen.
- Gemeinsamer-Dienst-Engpass: ein zentrales Team, hinter dem jedes Projekt warten muss.
- Plattform als Wächter: ein Plattformteam, das vorschreibt statt dient und Reibung hinzufügt statt sie zu beseitigen.
- Kognitive Überlastung: Teams, die ausufernde, unzusammenhängende Systeme besitzen, die sie nicht meistern können.
- Dauerhafte "Zusammenarbeit": zwei Teams, dauerhaft verstrickt, ein Signal für eine falsch platzierte Grenze.
- Umstrukturierungssucht: ständiges Umschichten, das die Stabilität zerstört, die Teams brauchen, um sich zu formen.

## Reifegradmodell

- **Stufe 1, Beginnen.** Teams bilden sich durch Zufall, Personalzahlen oder Althierarchie; niemand benennt Teamtypen oder Interaktionsmodi; funktionale Silos und Engpässe bei gemeinsamen Diensten sind überall, und Abhängigkeiten bleiben verborgen, bis sie eine Veröffentlichung blockieren.
- **Stufe 2, Entwickeln.** Einige stream-ausgerichtete Teams existieren und eine erste Plattform- oder InnerSource-Anstrengung erscheint, aber das Muster wird ungleich angewendet: ein paar Teams besitzen ihren Ausschnitt durchgängig, während andere noch hinter zentralen Funktionen warten, und kognitive Last wird anekdotisch besprochen statt gesteuert.
- **Stufe 3, Standardisieren.** Die vier Teamtypen und die drei Interaktionsmodi sind dokumentiert und werden bewusst in der ganzen Organisation genutzt; Plattformen und InnerSource entlasten teamübergreifende Abhängigkeiten; ein Betriebsmodell für Sicherheit, Daten und Design ist gewählt und niedergeschrieben, und neue Teams werden nach diesen Standards gebildet statt durch Improvisation.
- **Stufe 4, Steuern.** Topologie wird gegen Baselines gemessen und gesteuert: Teams verfolgen kognitive Last, abhängigkeitsbedingte Verzögerung (Initiativen, die darauf warten, dass ein anderes Team liefert, und für wie lange), Plattform-Selbstbedienungsquoten und -akzeptanz, Dauer der Interaktionsmodi und Liefer-Fluss-Kennzahlen wie Vorlaufzeit und Änderungshäufigkeit. Schwellen lösen Maßnahmen aus, zum Beispiel eine Warteschlangenlänge, die eine Funktion zur Föderation zwingt, oder eine dauerhafte Zusammenarbeit, die eine falsch platzierte Grenze markiert, sodass Entscheidungen auf Belegen statt Meinungen ruhen.
- **Stufe 5, Orchestrieren.** Teamdesign wird kontinuierlich verbessert und in Architektur-, Produkt- und Risikoplanung integriert; die Organisation formt Grenzen um, während sich System und Geschäft weiterentwickeln, beendet Befähigungseinsätze, sobald Fähigkeit übertragen wurde, und balanciert Plattforminvestition neu aus, während sich kognitive Last verschiebt, und hält schnellen Fluss als eine adaptive, dauerhafte Eigenschaft statt eine einmalige Umstrukturierung.

## Diskussionsideen

- Wie viele Teams müssen für eine typische Änderung koordinieren, und warum?
- Welche unserer Teams tragen zu viel kognitive Last, und was könnte eine Plattform abnehmen?
- Wo bekämpfen wir Conways Gesetz, statt Grenzen neu zu ziehen?
- Dienen unsere Plattformteams stream-ausgerichteten Teams, oder bewachen sie sie?
- Sollten Sicherheit, Daten und Design für uns gerade jetzt zentralisiert, föderiert oder eingebettet sein?
- Welche "vorübergehenden" Zusammenarbeiten sind still zu dauerhaften Abhängigkeiten geworden?

## Wichtigste Erkenntnisse

- Organisationsstruktur bestimmt Architektur und Liefergeschwindigkeit; gestalten Sie sie bewusst.
- Nutzen Sie die vier Teamtypen, mit stream-ausgerichtet als Standard und den übrigen zur Unterstützung.
- Wenden Sie das umgekehrte Conway-Manöver an, um die gewünschte Architektur zum einfachen Weg zu machen.
- Steuern Sie kognitive Last; begrenzen Sie jedes Team auf eine Domäne, die es meistern kann.
- Begrenzen und benennen Sie teamübergreifende Interaktionsmodi; behandeln Sie anhaltende Abhängigkeiten als Grenzdefekte.
- Wählen Sie zentralisierte, föderierte oder eingebettete Modelle für übergreifende Funktionen je nach Maßstab, und nutzen Sie InnerSource, um Warteschlangen zu entlasten.

## Referenzen und weiterführende Literatur

- Matthew Skelton und Manuel Pais, "Team Topologies: Organizing Business and Technology Teams for Fast Flow"
- Melvin Conway, "How Do Committees Invent?" (der Ursprung von Conways Gesetz)
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate"
- Will Larson, "An Elegant Puzzle: Systems of Engineering Management"
- Sam Newman, "Building Microservices" (zur Ausrichtung von Diensten an Teams)
- Danese Cooper und Klaas-Jan Stol, "Adopting InnerSource", und die InnerSource-Commons-Muster
- Frederick Brooks, "The Mythical Man-Month" (Kommunikationsaufwand)
