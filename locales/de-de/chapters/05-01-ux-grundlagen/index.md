# 5.1 UX-Grundlagen

## Überblick und Motivation

[User Experience](https://en.wikipedia.org/wiki/User_experience) (UX) handelt davon, Menschen zu verstehen (ihre Ziele, ihre Kontexte, ihre Einschränkungen) und dann Software so zu formen, dass sie ihnen hilft, mit der geringsten Reibung erfolgreich zu sein. Es ist keine Dekoration, die Sie am Ende anwenden. Es ist eine Arbeitsweise, die vor der ersten Codezeile beginnt und lange nach der Veröffentlichung fortdauert. Dieses Kapitel deckt die Forschungs-, Modellierungs-, und [Design-Thinking](https://en.wikipedia.org/wiki/Design_thinking)-Praktiken ab, die einer großen Organisation erlauben, Produktentscheidungen aus Evidenz statt aus Vermutungen zu treffen.

Für große Teams ist UX ebenso sehr ein Koordinationsproblem wie ein Handwerk. Wenn Dutzende Squads in ein geteiltes Produkt ausliefern, häufen sich unpassende mentale Modelle, duplizierte Abläufe, und widersprüchliche Terminologie zu einem verwirrenden Ganzen, das kein einzelnes Team besitzt. Eine geteilte UX-Grundlage, gebaut aus gemeinsamen Personas, vereinbarten Journey-Maps, und einer dokumentierten [Informationsarchitektur](https://en.wikipedia.org/wiki/Information_architecture), gibt jedem Team dieselbe Karte der Nutzerin, damit sich ihre separaten Entscheidungen zu einer kohärenten Erfahrung summieren. Ohne sie optimiert jedes Team lokal, und das Produkt als Ganzes ergibt keinen Sinn.

Unternehmen und Behörden erhöhen die Einsätze. Unternehmenssoftware hat oft gefangene Nutzerinnen, die nicht weggehen können, schlechte UX wird also in Training, Support-Tickets, Fehlern, und verlorener Produktivität bezahlt statt darin, dass Menschen gehen. Behördendienste erreichen oft die gesamte Öffentlichkeit, einschließlich Menschen in Krisen, auf alten Geräten, mit geringem digitalem Vertrauen, oder ohne alternative Anbieterin. Hier ist UX-Qualität eine Frage von Gerechtigkeit und bürgerlichem Vertrauen: ein schlecht gestalteter Leistungsantrag kann jemandem Essen oder Wohnraum verweigern, nicht weil sie nicht berechtigt sind, sondern weil sie das Formular nicht ausfüllen konnten.

## Kernprinzipien

- Gestalten Sie für echte Menschen, die echte Aufgaben unter echten Bedingungen erledigen, nicht für eine idealisierte Nutzerin auf einer schnellen Verbindung mit voller Aufmerksamkeit.
- Forschung reduziert Risiko. Der günstigste Zeitpunkt, eine falsche Annahme zu entdecken, ist bevor Sie darauf aufgebaut haben.
- Nutzerinnen können Ihnen nicht zuverlässig sagen, was sie tun werden; beobachten Sie Verhalten, nicht nur geäußerte Präferenz.
- Konzentrieren Sie sich auf die Aufgabe, die die Nutzerin zu erledigen versucht, nicht das Feature, das Sie ausliefern wollen.
- Konsistenz ist ein Feature: ein kohärentes mentales Modell über das Produkt hinweg senkt kognitive Last.
- [Barrierefreiheit](https://en.wikipedia.org/wiki/Accessibility) und Inklusion sind von Anfang an Teil guter UX, kein späterer Compliance-Durchgang.
- Qualitative und quantitative Methoden beantworten unterschiedliche Fragen; nutzen Sie beide.
- Kleine, häufige Forschung schlägt seltene, schwergewichtige Studien.

## Empfehlungen

### Kontinuierliche, gemischt-methodische Forschung etablieren

Zielen Sie auf eine leichtgewichtige, aber kontinuierliche Forschungspraxis statt gelegentlicher großer Studien. Interviews offenbaren Motivationen und mentale Modelle. [Usability-Testen](https://en.wikipedia.org/wiki/Usability_testing) offenbart, wo Designs zusammenbrechen; fünf bis acht Teilnehmerinnen pro Runde bringen die meisten schweren Probleme zutage. Umfragen messen Einstellungen im Maßstab, können aber nicht das "Warum" erklären. Analytics und Instrumentierung zeigen, was Menschen tatsächlich über die gesamte Population hinweg tun. Paaren Sie eine qualitative Methode (Warum) mit einer quantitativen (Wie viele), damit Funde sowohl erklärt als auch bemessen sind. Und behalten Sie ein Forschungsarchiv, damit Erkenntnisse durchsuchbar und über Teams hinweg wiederverwendbar bleiben, statt in den Folien eines Squads verloren zu gehen.

### Nutzerinnen mit Personas, Journey-Maps, und Jobs-to-be-done modellieren

Bauen Sie eine kleine Menge evidenzbasierter Personas, die Ziele, Kontexte, und Einschränkungen erfassen, keine demografischen Karikaturen. Rahmen Sie Bedürfnisse als Jobs-to-be-done, das zugrundeliegende Ergebnis, das eine Nutzerin zu erreichen versucht, statt ein Feature ("wenn ich meinen Job verliere, will ich schnell verstehen, für welche Unterstützung ich qualifiziert bin, damit ich weiter Miete zahlen kann"). Das hält den Fokus auf Ergebnissen statt Features. Journey-Maps kartieren die gesamte Erfahrung über Kanäle und Zeit hinweg, Lücken und Übergaben offenlegend, die kein einzelner Bildschirm offenbart. Für Dienste mit schwerem Back-Stage-Betrieb (Call-Center, Fallbearbeiterinnen, Erfüllung) nutzen Sie [Service-Blueprints](https://en.wikipedia.org/wiki/Service_blueprint), um die Front-Stage-Erfahrung mit den Systemen und Mitarbeiterinnen dahinter zu verbinden.

### Die Informationsarchitektur absichtlich gestalten

Informationsarchitektur (IA) ist, wie Inhalt, Features, und Navigation strukturiert und beschriftet sind. Nutzen Sie [Card Sorting](https://en.wikipedia.org/wiki/Card_sorting) und Tree-Testing, um diese Struktur aus den mentalen Modellen der Nutzerinnen abzuleiten statt aus Ihrem Organigramm. Ein häufiges Scheitern in großen Organisationen ist, interne Abteilungsgrenzen als oberste Navigationsebene freizulegen. Etablieren Sie ein kontrolliertes Vokabular, damit dasselbe Konzept überall denselben Namen hat. [Interaktionsdesign](https://en.wikipedia.org/wiki/Interaction_design) definiert dann das Moment-zu-Moment-Verhalten: Zustände, Feedback, Fehlerwiederherstellung, und den Fluss zwischen Schritten.

### Design Thinking pragmatisch anwenden

Das Double-Diamond-Modell (divergieren, dann konvergieren, um das richtige Problem zu definieren, dann divergieren und konvergieren, um die richtige Lösung zu gestalten) ist ein nützlicher Rahmen. Behandeln Sie es jedoch als Denkweise, nicht als starren getorten Prozess. In der Praxis führen Sie enge Schleifen: eine Hypothese rahmen, skizzieren, mit einer Handvoll Nutzerinnen testen, und binnen Tagen lernen. Sparen Sie die schwerere Entdeckung für wirklich neuartige oder hochriskante Probleme. Und hüten Sie sich vor "Innovationstheater", wo Workshops Klebezettel produzieren, aber keine ausgelieferte Änderung.

### UX in die Lieferung integrieren

Betten Sie Designerinnen und Forscherinnen in Lieferteams ein, statt eine separate "UX-Abteilung" zu betreiben, die Spezifikationen über eine Mauer reicht. Machen Sie Forschungsfunde zu einem ständigen Input für Priorisierung. Setzen Sie UX-Qualitätstore, wie Usability-Benchmarks und Barrierefreiheitsprüfungen, in die Definition von fertig. Und verfolgen Sie Ergebniskennzahlen (Aufgabenerfolg, Zeit auf Aufgabe, Fehlerrate, Zufriedenheit) direkt neben Ihren Lieferkennzahlen.

## Abwägungen: Vor- und Nachteile

| Ansatz | Vorteile | Nachteile |
|---|---|---|
| Kontinuierliche Entdeckungsforschung | Erwischt Probleme früh, baut geteiltes Verständnis | Laufende Kosten, braucht Rekrutierungspipeline und geschultes Personal |
| Schwergewichtige Vorabforschung | Tiefe Einsicht vor großer Investition | Langsam, kann Lernen verzögern, das nur Ausliefern offenbart |
| Nur-Analytics-Entscheidungen | Skaliert, objektiv, günstig einmal instrumentiert | Erklärt Was, aber nicht Warum; blind für Nicht-Nutzerinnen und Randfälle |
| Personas und Journey-Maps | Richten viele Teams auf ein Modell der Nutzerin aus | Veralten, können zu Fiktion werden, wenn nicht mit Daten aufgefrischt |
| Eingebettete Designerinnen | Schnelles Feedback, geteilter Besitz | Schwerer, Handwerk über viele Teams hinweg konsistent zu halten |

Jede Organisation balanciert Forschungsinvestition gegen Liefergeschwindigkeit. Der Fehler ist, das als Entweder-oder zu behandeln. Die produktive Haltung ist proportional: geben Sie mehr Entdeckung für Entscheidungen aus, die teuer umzukehren sind (Kern-IA, primäre Abläufe, Plattformwahlen), und weniger für Details, die Sie später leicht ändern können. Die Kosten der Forschung sind fast immer klein neben den Kosten, das Falsche gut zu bauen.

## Fragen zur Diskussion mit Ihrem Team

1. **Wer besitzt die geteilte Informationsarchitektur und das kontrollierte Vokabular, und was geschieht, wenn ein Team abweichen will?** Im Maßstab ist das häufigste Scheitern, jedem Squad zu erlauben, seine eigene Organigramm-Struktur und eigene Namen für dasselbe Konzept freizulegen, sodass das Produkt mit drei Worten für ein Ding und Navigation endet, die Abteilungen statt Nutzeraufgaben spiegelt. Entscheiden Sie jetzt, ob IA und Vokabular zentral besessen sind, aus Card Sorting und Tree-Testing abgeleitet statt aus interner Politik, und wie ein Team eine Änderung beantragt. Das zählt mehr in Unternehmen und Behörden, weil gefangene Nutzerinnen nicht weggehen können, Inkohärenz wird also in Training, Support-Tickets, und Fehlern statt in Abwanderung bezahlt. Bringen Sie die aktuelle Liste doppelter Begriffe und widersprüchlicher Abläufe als Beleg. Wenn Sie keine Besitzerin benennen können, ist das Ihr erster Aktionspunkt.

2. **Was ist unsere Rekrutierungspipeline für Forschungsteilnehmerinnen, und erreicht sie unterstützte-digitale, niedrig-vertrauensvolle, und nicht-digitale Nutzerinnen?** Kontinuierliche Entdeckung funktioniert nur, wenn Sie jede Woche echte Nutzerinnen vor sich bekommen können, und die schwersten Menschen zu rekrutieren sind oft jene, die den Dienst am meisten brauchen: Menschen in Krisen, auf alten Geräten, oder die normalerweise auf Hilfe angewiesen sind. Nur selbstbewusste, vernetzte Freiwillige zu testen gibt Ihnen eine schmeichelhafte, aber falsche Lesart, besonders für öffentliche Dienste, wo Zugangsgerechtigkeit der ganze Sinn ist. Einigen Sie sich, wer Rekrutierung führt, welche Anreize Sie bieten, und wie Sie unterstützte-digitale Sitzungen beobachten, ohne zur Last einer verletzlichen Person beizutragen. Bringen Sie die Teilnehmerinnen-Demografie Ihrer letzten drei Studien und prüfen Sie sie gegen Ihre echte Nutzerbasis. Wenn sie zu leicht erreichbaren Nutzerinnen tendieren, beheben Sie die Pipeline, bevor Sie den Funden vertrauen.

3. **Welche UX-Qualitätstore gehören in unsere Definition von fertig, und wie verhindern wir, dass sie zu Theater werden?** Designerinnen und Forscherinnen einzubetten zahlt sich nur aus, wenn Forschung ein ständiger Input für Priorisierung ist und wenn Usability- und Barrierefreiheitsprüfungen tatsächlich eine Story am Ausliefern hindern, keine Folie, der jeder zunickt und die er ignoriert. Wählen Sie konkrete Ergebniskennzahlen, die Sie neben Lieferkennzahlen verfolgen: Aufgabenerfolg, Zeit auf Aufgabe, Fehlerrate, und Zufriedenheit. Das Risiko ist Forschung, die betrieben wird, um bereits getroffene Entscheidungen zu rechtfertigen, einigen Sie sich also, wer einen Start bei einem UX-Tor mit Veto belegen kann und welcher Beleg die Meinung einer Führungskraft überschreibt. Bringen Sie ein jüngstes Feature und fragen Sie, ob seine Forschung die Entscheidung änderte oder sie nur dekorierte. Wenn Funde nie eine Roadmap bewegen, sind Ihre Tore kosmetisch.

4. **Wie verhindern wir, dass unsere Personas, Journey-Maps, und IA zu Fiktion verfallen, sobald die Forschung, die sie produzierte, ein Jahr alt ist?** Geteilte Modelle sind, was Dutzenden Teams erlaubt, auf eine kohärente Erfahrung hin zu gestalten, aber sie funktionieren nur, solange sie noch echte Nutzerinnen beschreiben, und in dem Moment, in dem eine Persona zu einem Artefakt wird, das Menschen zitieren, um Argumente zu gewinnen, statt einer Zusammenfassung von Evidenz, richtet sie aktiven Schaden an. Entscheiden Sie, wer die Auffrischung jedes Modells besitzt, in welchem Takt, und gegen welche Daten (frische Interviews, Analytics, Support-Themen), und einigen Sie sich auf ein sichtbares "zuletzt validiert"-Datum, damit veraltete Modelle offensichtlich sind. Die konkurrierende Überlegung sind Kosten: alles kontinuierlich aufzufrischen ist verschwenderisch, binden Sie die Auffrischungsfrequenz also daran, wie schnell sich dieser Teil der Nutzerbasis oder der Journey tatsächlich ändert. Bringen Sie die Herkunft Ihrer aktuellen Top-Personas und fragen Sie, wann jede zuletzt gegen eine echte Nutzerin geprüft wurde. In Unternehmen und Behörden, wo sich eine gefangene oder öffentliche Nutzerbasis langsam, aber folgenreich verschiebt (eine alternde Bevölkerung, eine neue Leistung, ein Geräteübergang), kann ein Modell, das still veraltet, jahrelange Investition auf Nutzerinnen lenken, die nicht mehr existieren.

5. **Wo lebt Barrierefreiheit in unserem Prozess, und können wir beweisen, dass eine Veröffentlichung sie erfüllt, bevor sie ausliefert, statt nach einer Beschwerde?** Barrierefreiheit als späten Compliance-Durchgang zu behandeln ist sowohl das häufigste Scheitern als auch das teuerste, weil das Nachrüsten von Semantik, Fokusreihenfolge, und Kontrast in eine gebaute Oberfläche weit mehr kostet, als sie einzubauen. Entscheiden Sie, welchen Standard Sie sich selbst auferlegen (zum Beispiel WCAG, die Web Content Accessibility Guidelines), ob Konformität ein blockierendes Tor in der Definition von fertig ist, und wer rechenschaftspflichtig ist, wenn ein unzugängliches Feature in Produktion gelangt. Die Spannung ist Geschwindigkeit gegen Inklusion, und Teams unter Terminendruck werden still die Prüfungen fallen lassen, die nicht durchgesetzt werden. Bringen Sie Ihre letzte Prüfung, die automatisierte und manuelle Abdeckung dahinter, und die Anzahl der Barrierefreiheitsprobleme, die nach statt vor der Veröffentlichung gefunden wurden. Besonders für Behörden ist das keine optionale Höflichkeit: es ist oft eine gesetzliche Pflicht und eine Frage von Gerechtigkeit, denn ein öffentlicher Dienst, der behinderte oder unterstützte-digitale Nutzerinnen ausschließt, hat an seinem Kernzweck versagt, nicht an einem sekundären.

6. **Wenn unsere Analytics und unsere qualitative Forschung sich widersprechen, wie entscheiden wir, welcher wir glauben, und wer schlichtet?** Große Organisationen häufen sowohl Dashboards an, die zeigen, was Tausende Nutzerinnen tun, als auch Interviews, die erklären, warum eine Handvoll sich so verhält, und die beiden werden routinemäßig in entgegengesetzte Richtungen zeigen: ein Ablauf mit hoher Abschlussrate, der Menschen still demütigt, oder ein Feature, das Nutzerinnen in Sitzungen loben, aber im Maßstab nie berühren. Einigen Sie sich im Voraus, wie Sie triangulieren, welche Frage jede Methode zu beantworten vertraut ist (Analytics für Ausmaß und Reichweite, Forschung für Ursache und Bedeutung), und wer die Autorität hat, die Entscheidung zu fällen, wenn sie in Konflikt geraten. Das Risiko ist Rosinenpickerei, welche Quelle auch immer den bereits gewählten Plan schmeichelt. Bringen Sie eine konkrete jüngste Meinungsverschiedenheit und gehen Sie durch, wie sie tatsächlich gelöst wurde. In Unternehmens- und öffentlichen Umgebungen sind die Einsätze geschärft, weil Analytics systematisch genau die Menschen unterzählt, die am meisten zählen: Nicht-Nutzerinnen, Abbrecherinnen, und jene auf assistiver Technologie erscheinen selten im Funnel, allein Zahlen zu vertrauen kann die Ausgeschlossenen also unsichtbar machen.

## Branchenperspektive

**Startup.** Sie haben keine Forscherin und keine Zeit für ein Archiv, machen Sie Forschung also zu einer Gründergewohnheit: sitzen Sie einen Nachmittag neben fünf echten Nutzerinnen, bevor Sie das Nächste bauen. Überspringen Sie formale Personas und Journey-Maps; ein geteiltes Verständnis der einen Aufgabe, die Sie lösen, wöchentlich durch Beobachtung aufgefrischt, schlägt Dokumentation, die niemand pflegt. Ihr Vorteil ist, dass das ganze Team eine Erkenntnis am selben Tag aufnehmen kann, an dem sie erscheint, schützen Sie diese Geschwindigkeit also und widerstehen Sie Zeremonie.

**Kleinunternehmen.** Ohne UX-Spezialistin und mit engem Budget, stützen Sie sich auf die Konventionen, die Ihre Nutzerinnen bereits kennen, statt Ihre eigenen zu erfinden, und kaufen Sie Werkzeuge mit vernünftigen Standards statt Abläufe von Grund auf zu gestalten. Machen Sie die günstige, wertvolle Forschung selbst: eine Handvoll Usability-Sitzungen über einen Videoanruf und eine Lektüre Ihrer Support-Tickets bringen die meisten schweren Probleme zutage. Behandeln Sie Barrierefreiheitsgrundlagen (Kontrast, Beschriftungen, Tastaturzugang) als selbstverständlich, die Sie von einer guten Komponentenbibliothek bekommen, statt als Projekt, das Sie besetzen.

**Großunternehmen.** Das Kernproblem ist Kohärenz über viele Teams, investieren Sie also in die geteilten Grundlagen: besessene Personas, gepflegte Journey-Maps, ein kontrolliertes Vokabular, und eine dokumentierte Informationsarchitektur, auf die hin Squads gestalten statt um sie herum. Betten Sie Designerinnen und Forscherinnen in Lieferteams ein, aber steuern Sie Handwerk zentral, damit das Produkt nicht in inkonsistente Dialekte zerbricht. Finanzieren Sie ein Forschungsarchiv und Qualitätstore in der Definition von fertig, und verfolgen Sie UX-Ergebniskennzahlen als Portfolio, damit die lokale Optimierung keines einzelnen Teams das Ganze degradiert.

**Behörde.** Barrierefreiheit und Zugangsgerechtigkeit sind Pflichten, keine Präferenzen, halten Sie Veröffentlichungen also an einen veröffentlichten Standard und forschen Sie mit der gesamten Bandbreite der Öffentlichkeit, einschließlich unterstützter-digitaler, niedrig-vertrauensvoller, und nicht-digitaler Nutzerinnen. Beschaffung und Transparenz formen Lieferung: veröffentlichen Sie Ihre Designprinzipien und Forschungsmethoden, strukturieren Sie Dienste um die Lebensereignisse der Bürgerinnen statt um interne Abteilungen, und behalten Sie Testbeleg für Prüfungen. Weil Nutzerinnen oft keine alternative Anbieterin haben, verweigert ein Ablauf, den sie nicht abschließen können, einen Dienst, behandeln Sie den Abschluss durch die am schwersten erreichbare Nutzerin also als das echte Erfolgsmaß.

## Beispiele

**Startup.** Ein vierköpfiges Startup, das ein Terminplanungswerkzeug für kleine Kliniken baute, hatte starke Meinungen darüber, was Rezeptionistinnen brauchten, aber keine Evidenz. Bevor sie mehr Features schrieben, saßen die Gründerinnen einen Nachmittag lang neben fünf Rezeptionistinnen und beobachteten sie bei der Arbeit. Sie lernten, dass der echte Schmerz nicht Buchungsgeschwindigkeit war, sondern Doppelbuchungen, verursacht durch eine verwirrende Kalenderansicht, etwas, das niemand in früheren Verkaufsgesprächen zu erwähnen dachte. Das Produkt um diese eine Aufgabe herum neu zu rahmen, und Fixes mit denselben fünf Menschen über eine Woche zu skizzieren und zu testen, verwandelte eine stockende Testphase in ihre ersten zahlenden Kundinnen.

**Großunternehmen.** Eine multinationale Bank konsolidierte sieben regionale interne Kreditvergabewerkzeuge in eine Plattform. Statt Feature-Sets zu verschmelzen, führte das Team Journey-Mapping und Service-Blueprinting mit Kreditsachbearbeiterinnen über Regionen hinweg durch. Sie fanden, dass die "regionalen Unterschiede", die jeder annahm, größtenteils inkonsistente Terminologie und Bildschirmreihenfolge waren, keine echten Prozessunterschiede. Eine vereinheitlichte IA und geteiltes Vokabular verkürzten die Trainingszeit für Kreditsachbearbeiterinnen erheblich und reduzierten Bearbeitungsfehler, weil das Personal jetzt ein mentales Modell teilte.

**Behörde.** Eine nationale Steuerbehörde, die ihren Online-Einreichungsdienst neu gestaltete, führte moderiertes Usability-Testen mit Steuerzahlerinnen über Altersgruppen, Geräte, und digitale-Vertrauens-Ebenen hinweg durch, plus unterstützte-digitale Beobachtung von Menschen, die normalerweise auf Hilfe angewiesen sind. Testen offenbarte, dass jargonbeladene Abschnittsüberschriften Menschen dazu brachten, abzubrechen oder falsch einzureichen. Inhalt um die Jobs-to-be-done der Steuerzahlerinnen herum neu zu rahmen, und die IA um Lebensereignisse statt interne Steuercodes herum neu zu strukturieren, erhöhte erfolgreichen Selbstbedienungsabschluss und reduzierte Call-Center-Volumen, direkt die Bedienungskosten senkend, während Zugangsgerechtigkeit verbessert wurde.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Die Rendite von UX kommt von drei Hebeln: mehr Erfolg (mehr Nutzerinnen schließen wertvolle Aufgaben ab), niedrigere Bedienungskosten (weniger Support-Kontakte, weniger Training, weniger Fehler), und weniger Nacharbeit (falsche Richtungen erwischen, bevor sie gebaut sind). In Unternehmensumgebungen, wo Nutzerinnen gefangen sind, zeigt sich die Auszahlung als Produktivität und weniger Fehler statt Konversion; ein paar Sekunden gespart pro Transaktion, über Tausende Angestellte, verdichtet sich zu großen jährlichen Einsparungen.

Gesamtbetriebskosten müssen die Kosten der Übernahme gegen die Kosten der Nicht-Übernahme abwägen. Die Übernahmekosten sind leicht zu sehen: Forscherinnen und Designerinnen, Rekrutierung und Anreize für Teilnehmerinnen, Werkzeug, und Zeit im Zeitplan. Die Kosten der Nicht-Übernahme sind größer, aber schwerer zu erkennen: abgebrochene Transaktionen, Support- und Trainingsaufwand, teure späte Neugestaltungen, gescheiterte Starts, und Reputations- oder rechtliche Exposition, wenn öffentliche Dienste Menschen ausschließen. Weil sich diese Kosten über Support-, Trainings-, und Betriebsbudgets verteilen statt über die Produktlinie, unterschätzt die Führung sie oft.

Um den Fall gegenüber der Führung zu machen, verbinden Sie UX mit Kennzahlen, die Führungskräfte bereits verfolgen: Abschluss- und Konversionsraten, Kosten pro Transaktion, Support-Ticket-Volumen, Trainingstage, und Fehler- und Nacharbeitsraten. Führen Sie ein kleines, instrumentiertes Pilotprojekt durch, das ein messbares Vorher-Nachher zeigt, extrapolieren Sie dann über das Portfolio. Forschung als Risikoreduktion bei irreversiblen Entscheidungen zu rahmen tendiert dazu, bei Finanz- und Governance-Stakeholdern zu resonieren.

## Anti-Muster und Fallstricke

- **HiPPO-getriebenes Design**: Entscheidungen, getroffen von der Meinung der bestbezahlten Person statt Evidenz.
- **Forschungstheater**: Studien, betrieben, um bereits getroffene Entscheidungen zu rechtfertigen, Funde ignoriert.
- **Personas als Fiktion**: erfundene Profile, nie gegen echte Nutzerinnen validiert, genutzt um Argumente zu gewinnen.
- **Organigramm als IA**: Navigation, die interne Abteilungen statt Nutzeraufgaben spiegelt.
- **Big-Bang-Forschung**: seltene, teure Studien, die zu spät ankommen, um irgendetwas zu ändern.
- **Nur den Happy Path testen**: Fehlerzustände, Randfälle, und Nutzerinnen unter Stress ignorieren.
- **Design als letzter Anstrich**: UX erst einbringen, um einen fertigen Build "schön aussehen" zu lassen.
- **Unterstützte und nicht-digitale Nutzerinnen ignorieren**: nur für selbstbewusste, vernetzte Nutzerinnen gestalten.

## Reifegradmodell

**Stufe 1: Beginnen.** Keine dedizierte UX-Praxis. Entscheidungen werden nach Meinung und dem Instinkt der bestbezahlten Person getroffen. Forschung, falls sie überhaupt geschieht, ist Ad-hoc und reaktiv, ausgelöst durch einen Start, der schlecht lief. Abläufe und Terminologie sind über Teams hinweg inkonsistent, und niemand besitzt die Gesamterfahrung.

**Stufe 2: Entwickeln.** Manche Teams haben Designerinnen und führen gelegentliche Usability-Tests durch, und ein paar Personas oder Journey-Maps existieren, aber die Praxis variiert stark zwischen Squads und wird nicht gepflegt. UX wird als Phase statt kontinuierliche Disziplin behandelt, und wird oft unter Zeitplandruck übergangen. Gute Arbeit geschieht in Inseln, summiert sich aber nicht über das Produkt.

**Stufe 3: Standardisieren.** Kontinuierliche gemischt-methodische Forschung speist Priorisierung, und geteilte Personas, Journey-Maps, und eine kontrolliertes-Vokabular-IA sind dokumentiert und über Teams hinweg genutzt. UX-Qualitätstore, einschließlich Usability-Benchmarks und Barrierefreiheitsprüfungen, sitzen in der Definition von fertig und werden organisationsweit durchgesetzt. Ein durchsuchbares Forschungsarchiv hält Erkenntnisse wiederverwendbar statt in den Folien eines Squads gefangen.

**Stufe 4: Steuern.** Die Praxis wird gegen Baselines gemessen statt nur ausgeführt. Sie verfolgen Aufgabenerfolg, Zeit auf Aufgabe, Fehlerrate, Zufriedenheit, und Barrierefreiheitskonformität als vereinbarte Kennzahlen, setzen Ziele, und beobachten sie über Veröffentlichungen. Forschungsteilnehmerinnen-Stichproben werden gegen die echte Nutzerbasis geprüft, damit Funde repräsentativ sind, Qualitätstore berichten Bestehensraten statt Meinungen, und die Kosten der Forschung werden gegen gemessene Reduktionen bei Support-Kontakten, Training, und Nacharbeit abgewogen. Entscheidungen auszuliefern oder zurückzuhalten ruhen auf Beleg gegen diese Baselines.

**Stufe 5: Orchestrieren.** Forschung ist kontinuierlich, ergebnisgebunden, und mit Produkt-, Geschäfts-, und Risikoplanung über die Organisation hinweg integriert. Teams führen kontrollierte Experimente durch, schließen die Schleife von Einsicht zu ausgelieferter Änderung zu gemessener Wirkung, und ziehen Nutzermodelle zurück oder rahmen sie neu, während sich die Population und ihre Journeys verschieben. Die UX-Grundlage passt sich kontinuierlich an: Personas, Journeys, IA, und Standards werden auf Evidenz aufgefrischt, und die Organisation balanciert neu, wo sie in Entdeckung investiert, während sich Reversibilität und Risiko ändern.

## Diskussionsideen

- Wie viel Entdeckung ist "genug", bevor man sich auf eine Richtung festlegt, und wer entscheidet?
- Wie halten Sie Personas und Journey-Maps lebendig, statt sie zu veralteten Artefakten werden zu lassen?
- Wenn quantitative Analytics und qualitative Forschung sich widersprechen, welcher vertrauen Sie, und warum?
- Wie sollte eine große Organisation einen zentralen UX-Standard mit der Autonomie jedes Teams balancieren?
- Was ist der richtige Weg, Dienste zu erforschen, die von Menschen in Krisen genutzt werden, ohne zu ihrer Last beizutragen?
- Wie messen Sie den ROI von Forschung, die einen Fehler verhindert, den Sie deshalb nie machten?

## Wichtigste Erkenntnisse

- UX ist eine Arbeitsweise von Anfang an, keine Dekoration am Ende.
- Kombinieren Sie qualitative Methoden (Warum) mit quantitativen Methoden (Wie viele).
- Modellieren Sie Nutzerinnen mit evidenzbasierten Personas, Journey-Maps, Jobs-to-be-done, und Service-Blueprints.
- Strukturieren Sie Information um die mentalen Modelle der Nutzerinnen, nicht das Organigramm.
- Behandeln Sie Design Thinking als pragmatische Denkweise mit engen Lernschleifen, nicht als starren Prozess.
- Die Kosten der Forschung sind klein verglichen mit den Kosten, das Falsche zu bauen.
- In Unternehmen und Behörden übersetzt sich UX-Qualität direkt in Produktivität, Bedienungskosten, und Zugangsgerechtigkeit.

## Referenzen und weiterführende Literatur

- Don Norman, *The Design of Everyday Things*
- Steve Krug, *Don't Make Me Think*
- Erika Hall, *Just Enough Research*
- Kim Goodwin, *Designing for the Digital Age*
- Louis Rosenfeld, Peter Morville, und Jorge Arango, *Information Architecture: For the Web and Beyond*
- Clayton Christensen et al., *Competing Against Luck* (Jobs-to-be-done)
- Alan Cooper, *The Inmates Are Running the Asylum*
- Jakob Nielsen, *Usability Engineering*
- UK Government Digital Service, *Service Manual* und *Design Principles*
- U.S. General Services Administration, *18F Methods* und die *U.S. Web Design System*-Forschungsleitlinien
- Nielsen Norman Group, Forschungsmethoden-Artikel und Berichte
