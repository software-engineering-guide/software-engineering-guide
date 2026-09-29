# 5.3 Barrierefreiheit

## Überblick und Motivation

[Barrierefreiheit](https://en.wikipedia.org/wiki/Accessibility) (oft "a11y" abgekürzt) ist die Praxis, Software zu bauen, die Menschen mit Behinderungen wahrnehmen, verstehen, navigieren, und nutzen können. Das umfasst Menschen, die blind sind oder eingeschränktes Sehen haben, die taub oder schwerhörig sind, die motorische Beeinträchtigungen haben, die kognitive oder Lernunterschiede haben, und die vorübergehenden oder situativen Einschränkungen gegenüberstehen wie einem gebrochenen Arm, hellem Sonnenlicht, oder einem lauten Raum. Ungefähr eine von fünf Personen hat eine Behinderung, und jeder profitiert irgendwann von barrierefreiem Design. Das ist keine Nischen-Anpassung. Es ist ein Qualitätsgrundstandard.

Für große Teams muss Barrierefreiheit ins System eingebaut werden, nicht individuellen guten Absichten überlassen. Wenn viele Teams in ein Produkt ausliefern, kann eine einzelne unzugängliche Komponente (ein unbeschriftetes Formularfeld, ein Nur-Farbe-Statusindikator, eine Tastaturfalle in einem Modal) behinderte Nutzerinnen von einer gesamten Journey aussperren. Barrierefreiheit in geteilte Komponenten, Design-Tokens, Testpipelines, und Definitionen von fertig einzubauen ist der einzige Weg, sie im Maßstab zuverlässig zu machen. Sie im Nachhinein nachzurüsten ist teuer und fehleranfällig. Sie einzubauen ist günstig und dauerhaft.

Für Behörden ist Barrierefreiheit eine gesetzliche Anforderung und eine bürgerliche Pflicht, kein Nice-to-have. Öffentliche Dienste müssen jedem Mitglied der Öffentlichkeit dienen, und behinderte Bürgerinnen haben oft keine alternative Anbieterin: falls die Regierungswebsite unzugänglich ist, können sie ihre Leistung, Lizenz, oder Stimme nicht auf andere Weise bekommen. Gesetze und Standards weltweit machen Barrierefreiheit für öffentliche Stellen verpflichtend, und zunehmend auch für den Privatsektor. Dieses Kapitel behandelt Barrierefreiheit als drei Dinge gleichzeitig: eine rechtliche Pflicht, eine ethische Pflicht, und einfach gutes Design.

*Siehe auch:* Kapitel 5.2 (UI-Design und Designsysteme), Kapitel 5.6 (Frontend-Entwicklung), und Kapitel 5.1 (UX-Grundlagen).

## Kernprinzipien

- Barrierefreiheit ist ein Grundqualitätsattribut, wie Sicherheit und Performance, kein optionales Feature.
- Die POUR-Prinzipien: Oberflächen müssen Perceivable (wahrnehmbar), Operable (bedienbar), Understandable (verständlich), und Robust (robust) sein.
- [Semantisches HTML](https://en.wikipedia.org/wiki/Semantic_HTML) zuerst; nutzen Sie [ARIA](https://en.wikipedia.org/wiki/WAI-ARIA) nur, um echte Lücken zu füllen, nie als Ersatz für native Elemente.
- Alles mit einer Maus Nutzbare muss allein mit einer Tastatur nutzbar sein.
- Vermitteln Sie Information nicht allein durch Farbe, Form, oder Position.
- Automatisierte Werkzeuge erwischen nur einen Bruchteil der Probleme; manuelles und [assistives-Technologie](https://en.wikipedia.org/wiki/Assistive_technology)-Testen sind essentiell.
- Barrierefreies Design ist besseres Design für alle (der ["Bordstein-Effekt"](https://en.wikipedia.org/wiki/Curb_cut), wo Features, gebaut für behinderte Menschen, alle Nutzerinnen begünstigen).
- Gestalten und testen Sie mit behinderten Menschen, nicht nur für sie.

## Empfehlungen

### Nach WCAG gestalten und bauen, auf den aktuellen Standard zielend

Die [Web Content Accessibility Guidelines](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) sind die internationale Referenz. WCAG 2.1 und 2.2 sind unter den vier POUR-Prinzipien organisiert, mit testbaren Erfolgskriterien auf den Konformitätsstufen A, AA, und AAA. Zielen Sie auf Stufe AA als Ihre Grundlage; das ist, was die meisten Gesetze referenzieren. WCAG 2.2 fügt Kriterien für Fokussichtbarkeit, Zielgröße, und Reduktion kognitiver Last hinzu. WCAG 3.0 ist ein aufkommender Nachfolger, anders strukturiert und noch in Entwicklung. Behalten Sie es im Auge, aber bauen Sie heute nach 2.2 AA. Behandeln Sie die Richtlinien als Boden, nicht Decke: jedes Kriterium zu bestehen garantiert keine wirklich nutzbare Erfahrung.

### Semantisches HTML und korrektes ARIA nutzen

Native HTML-Elemente (Buttons, Links, Formularsteuerelemente, Überschriften, Listen, Landmarken) kommen mit eingebauter Barrierefreiheitssemantik, Tastaturverhalten, und assistiver-Technologie-Unterstützung. Nutzen Sie sie zuerst. Greifen Sie zu ARIA-(Accessible Rich Internet Applications)-Rollen, -Zuständen, und -Eigenschaften nur, um benutzerdefinierte Widgets zu beschreiben, die HTML nicht ausdrücken kann, und folgen Sie den ARIA Authoring Practices. Die erste Regel von ARIA ist einfach: nutzen Sie kein ARIA, wenn ein natives Element ausreicht. Inkorrektes ARIA ist schlimmer als keines: es führt [Screenreader](https://en.wikipedia.org/wiki/Screen_reader) aktiv in die Irre. Geben Sie der Seite eine logische Überschriftenstruktur, bedeutsame Beschriftungen, alternativen Text für Bilder, Untertitel und Transkripte für Medien, und eine programmatische Verbindung zwischen jeder Beschriftung und ihrem Steuerelement.

### Tastatur- und assistive-Technologie-Bedienbarkeit garantieren

Jedes interaktive Element muss allein mit der Tastatur erreichbar und bedienbar sein, in logischer Reihenfolge, mit einem klar sichtbaren Fokusindikator. Vermeiden Sie Tastaturfallen. Verwalten Sie Fokus absichtlich, wenn sich Inhalt ändert: bewegen Sie Fokus zu einem Dialog, wenn er sich öffnet, geben Sie ihn zurück, wenn der Dialog schließt, und kündigen Sie dynamische Updates durch Live-Regionen an. Testen Sie mit echten assistiven Technologien, einschließlich Screenreadern auf Desktop und Mobil, Bildschirmvergrößerung, Sprachsteuerung, und Switch-Zugang. Und respektieren Sie Nutzerpräferenzen wie reduzierte Bewegung und erhöhten Kontrast.

### Mit automatisierten Werkzeugen, manueller Prüfung, und echten Nutzerinnen testen

Automatisierte Barrierefreiheitsscanner sind wertvoll, und sie sollten bei jeder Änderung in der Pipeline laufen. Aber Studien zeigen konsistent, dass sie nur eine Minderheit der echten Probleme erwischen, ungefähr ein Drittel. Der Rest braucht menschliches Urteilsvermögen: Tastatur-Durchgänge, Screenreader-Testen, Kontrastprüfungen, und die Frage, ob der Inhalt tatsächlich verständlich ist. Am wichtigsten von allem, beziehen Sie Menschen mit Behinderungen ins Usability-Testen ein. Bauen Sie Barrierefreiheits-Akzeptanzkriterien in die Definition von fertig, damit Probleme pro Story erwischt werden statt in einer Vor-Start-Prüfung.

### Barrierefreiheit organisatorisch machen, nicht heldenhaft

Backen Sie Barrierefreiheit ins Designsystem, damit Komponenten standardmäßig barrierefrei ausliefern. Bieten Sie Training, damit Designerinnen, Ingenieurinnen, Inhaltsautorinnen, und Produktmanagerinnen jeweils wissen, wofür sie verantwortlich sind. Etablieren Sie einen Barrierefreiheitsstandard, eine Besitzerin oder ein Center of Excellence, und einen Behebungsprozess. Veröffentlichen Sie eine Barrierefreiheitserklärung und geben Sie Nutzerinnen einen Weg, Barrieren zu melden. Und beschaffen Sie barrierefrei: fordern Sie von Anbieterinnen und Drittkomponenten Konformität, und Beleg dafür (wie einen Barrierefreiheits-Konformitätsbericht).

## Abwägungen: Vor- und Nachteile

| Ansatz | Vorteile | Nachteile |
|---|---|---|
| Barrierefreiheit von Anfang an einbauen | Günstigst, dauerhaft, besser für alle | Braucht Vorab-Training und Disziplin |
| Nachträglich nachrüsten/beheben | Verschiebt Aufwand, schaltet schnellen Start frei | Weit teurer, brüchig, rechtliche Exposition in der Zwischenzeit |
| Nur automatisiertes Testen | Schnell, günstig, erwischt Regressionen in CI | Verpasst ~zwei Drittel der Probleme; falsches Vertrauen |
| Manuelles + assistive-Technologie-Testen | Erwischt echte Usability-Barrieren | Langsamer, braucht geschulte Testerinnen und Geräte |
| Testen mit behinderten Nutzerinnen | Bodenwahrheit über echte Erfahrung | Rekrutierungsaufwand und Kosten, muss respektvoll geschehen |

Die zentrale Abwägung ist Vorab-Disziplin gegen aufgeschobene Kosten. Eingebaute Barrierefreiheit ist günstig und verbessert Qualität für alle; unter rechtlichem Druck nachgerüstete Barrierefreiheit ist teuer, unvollständig, und stressig. Auf lange Sicht gibt es keine echte Abwägung gegen "Geschwindigkeit": unzugängliche Software funktioniert einfach nicht für ein Fünftel Ihrer Nutzerinnen. Das ist ein Defekt, keine Ersparnis.

## Fragen zur Diskussion mit Ihrem Team

1. **Lassen Barrierefreiheitsregressionen unseren Build scheitern, wie ein kaputter Test es täte, und wenn nicht, warum nicht?** Automatisierte Scanner erwischen nur ungefähr ein Drittel der Probleme, aber die, die sie erwischen (fehlende Beschriftungen, Kontrastfehlschläge, unbeschriftete Steuerelemente), sind günstig in CI zu erwischen und teuer in einer Vor-Start-Prüfung zu finden. Eine Regression als Build-Fehlschlag zu behandeln ist, was Barrierefreiheit von heldenhaftem individuellem Aufwand zu einer zuverlässigen Systemeigenschaft bewegt, was das Einzige ist, das funktioniert, wenn viele Teams in ein Produkt ausliefern. Entscheiden Sie, welche Prüfungen blockierend sind, welche beratend, und wer einen Fehlschlag überschreiben kann. Bringen Sie Ihre aktuellen Scanner-Ergebnisse und Ihre Definition von fertig zum Treffen. Wenn Barrierefreiheitskriterien nicht pro Story in die Definition von fertig geschrieben sind, werden sie depriorisiert, sobald ein Termin sich strafft.

2. **Was ist unsere Regel für benutzerdefinierte Widgets, und wer prüft das ARIA, bevor es ausliefert?** Native HTML-Elemente kommen kostenlos mit Tastaturverhalten und assistiver-Technologie-Unterstützung, und inkorrektes ARIA ist schlimmer als keines, weil es Screenreader aktiv in die Irre führt. Einigen Sie sich, dass semantisches HTML der Standard ist und dass jedes benutzerdefinierte Widget (ein maßgeschneidertes Dropdown, Datumsauswahl, oder Modal) einen Tastatur- und Screenreader-Durchgang vor dem Merge braucht, den ARIA Authoring Practices folgend. Das zählt am meisten für die interaktiven Komponenten, die viele Teams wiederverwenden, denn ein kaputtes Modal mit einer Tastaturfalle kann behinderte Nutzerinnen von einer gesamten Journey aussperren. Bringen Sie eine Liste Ihrer benutzerdefinierten Widgets und fragen Sie, welche mit einem echten Screenreader getestet wurden. Alle, die es nicht wurden, sind Haftungen, versteckt in geteiltem Code.

3. **Was ist unsere Richtlinie zu Barrierefreiheits-Overlays, und glaubt irgendjemand, sie seien ein echter Fix?** Overlays werden als Ein-Zeilen-Skript vermarktet, das eine Seite konform macht, und sie sind verlockend, wenn rechtlicher Druck ankommt und ein Termin droht. Sie liefern keine echte Konformität, sie können die Erfahrung für assistive-Technologie-Nutzerinnen verschlechtern, und für Behörden lassen sie die zugrundeliegende rechtliche Pflicht unerfüllt. Entscheiden Sie explizit, dass Sie in semantisches Markup, Tastaturunterstützung, und Testen mit behinderten Menschen investieren werden statt ein Widget zu kaufen, das über das Problem tapeziert. Bringen Sie die Kosten eines Overlay-Abonnements und vergleichen Sie sie gegen Barrierefreiheit einmal in Ihre Komponenten und Pipeline einzubauen. Das früh zu rahmen verhindert eine panische spätere Beschaffungsentscheidung, die Geld ausgibt und nichts behebt.

4. **Sind behinderte Menschen Teil unseres Designs und Testens, oder gestalten wir noch immer für eine imaginierte Nutzerin, die wir erfanden?** Automatisierte Scanner und selbst Expertenprüfungen sagen Ihnen, ob Markup konform ist; sie sagen Ihnen nicht, ob eine blinde Nutzerin Ihren Checkout tatsächlich abschließen kann oder eine Person mit kognitiver Behinderung Ihre Fehlermeldungen verstehen kann. Behinderte Teilnehmerinnen einzubeziehen ist die einzige Quelle von Bodenwahrheit, und es ändert, was Sie bauen, aber es wirft echte Fragen auf, wie Sie fair rekrutieren, wie Sie Menschen für ihre Zeit entschädigen, und wie Sie vermeiden, eine Teilnehmerin als Sprecherin für jede Behinderung zu behandeln. Bringen Sie Ihre aktuelle Forschungsliste, Ihre Rekrutierungs- und Bezahlungspraktiken, und eine ehrliche Zählung, wie viele Studien im letzten Jahr behinderte Teilnehmerinnen einschlossen. Für eine große Organisation ist ein wiederkehrendes Panel mit fairer Entschädigung und Abdeckung über Seh-, Hör-, motorische, und kognitive Bedürfnisse, was das von einer Einmal-Geste zu einem verlässlichen Input macht; in Behörden ist die Einbeziehung der Öffentlichkeit, der Sie dienen, oft Teil der rechtlichen und bürgerlichen Pflicht, keine optionale Nettigkeit.

5. **Wenn wir eine Drittkomponente kaufen oder einbetten, fordern wir Beleg für Barrierefreiheit, und wer prüft ihn?** Viel von dem, was in einem großen Produkt ausliefert, ist nicht intern geschrieben: eine Datumsauswahl aus einer Bibliothek, ein Zahlungswidget in einem iframe, ein Diagrammpaket, ein ganzes SaaS-Modul. Eine einzelne unzugängliche eingebettete Komponente kann eine gesamte Journey scheitern lassen, egal wie sauber Ihr eigener Code ist, und sobald sie eingebunden ist, ist Ersetzen teuer. Entscheiden Sie, dass Barrierefreiheit eine Beschaffungsanforderung ist, dass Anbieterinnen einen Barrierefreiheits-Konformitätsbericht liefern müssen (ein Dokument wie ein VPAT, das angibt, wie ein Produkt gegen WCAG abschneidet), und dass jemand Technisches die Behauptung validiert statt sie abzulegen. Bringen Sie ein Inventar Ihrer Drittkomponenten und fragen Sie, welche aktuellen, glaubwürdigen Konformitätsbeleg haben. In Unternehmens- und Behördenbeschaffung schreiben Sie WCAG-2.2-AA-Konformität und ein Recht auf Behebung in den Vertrag, denn ein vor der Unterzeichnung gemachtes Versprechen ist weit günstiger durchzusetzen als eine nach dem Go-Live entdeckte Barriere.

6. **Was ist unsere Ziel-Konformitätsstufe, wer besitzt sie, und wie halten wir sie aktuell, während sich Standards bewegen?** WCAG 2.2 AA ist der heutige Boden, und die meisten Gesetze referenzieren es, aber 2.2 fügte Kriterien hinzu, die viele Teams nicht übernommen haben, und WCAG 3.0 kommt mit einer anderen Struktur. Ohne benannte Besitzerin driftet der Standard: unterschiedliche Teams zielen auf unterschiedliche Versionen, niemand verfolgt die Lücke, und Konformität verrottet still zwischen Prüfungen. Entscheiden Sie die exakte Version und Stufe, nach der Sie bauen, wer die Autorität hat, sie anzuheben, und wie neue Kriterien das Designsystem und die Definition von fertig erreichen. Bringen Sie Ihr aktuelles erklärtes Ziel, Beleg dafür, wo Teams es tatsächlich erfüllen, und eine kurze Roadmap zur Übernahme übersprungener 2.2-Kriterien. Für eine große oder öffentliche Organisation sind eine Barrierefreiheitsbesitzerin oder ein Center of Excellence, eine veröffentlichte Barrierefreiheitserklärung, und ein dokumentierter Plan für die nächste Standardversion, was Ihnen erlaubt, einer Regulatorin oder einem Gericht mit Beleg statt guten Absichten zu antworten.

## Branchenperspektive

**Startup.** Geschwindigkeit begünstigt Sie hier, weil Barrierefreiheit am günstigsten ist, wenn die Codebasis klein ist. Fügen Sie einen automatisierten Scanner zu CI und einen Tastatur-Durchgang zu Ihrer Pull-Request-Checkliste vom ersten Sprint an hinzu, und stützen Sie sich auf semantisches HTML, damit Sie Tastatur- und Screenreader-Unterstützung kostenlos bekommen. Überspringen Sie Overlays und schweres Werkzeug; die Auszahlung ist, dass Sie, wenn das Beschaffungsteam einer Kundin mitten im Verkauf nach einem Konformitätsbericht fragt, in Tagen statt hektisch antworten können.

**Kleinunternehmen.** Ohne Barrierefreiheitsspezialistin und mit engem Budget, kaufen Sie Barrierefreiheit statt sie zu bauen: wählen Sie eine Plattform, ein Theme, oder eine Komponentenbibliothek, die bereits konform ist und das angibt, und bevorzugen Sie Anbieterinnen, die eine Barrierefreiheitserklärung veröffentlichen. Decken Sie die wertvollen Grundlagen selbst mit kostenlosen Werkzeugen ab, Nur-Tastatur-Prüfungen, einem Kontrastprüfer, und klaren Beschriftungen auf jedem Feld, denn das erwischt die Fehlschläge, die am häufigsten Kundinnen ausschließen. Behandeln Sie einen falschen oder unnutzbaren automatisierten Ablauf als verlorene Kundin, denn ein Kleinunternehmen bietet selten einen unterstützten Kanal als Rückfall.

**Großunternehmen.** Im Maßstab ist die Arbeit, Barrierefreiheit zu einer Systemeigenschaft über viele Teams zu machen. Liefern Sie standardmäßig barrierefreie Komponenten im Designsystem, torwächten Sie Regressionen in CI, und stellen Sie eine Besitzerin oder ein Center of Excellence mit einem Behebungsprozess und Training für Designerinnen, Ingenieurinnen, und Inhaltsautorinnen auf. Verfolgen Sie Konformität über Zeit als Kennzahl, schreiben Sie WCAG-Konformität in Beschaffung, und verwalten Sie Drittkomponenten als Portfolio, damit kein eingebettetes Widget still eine geteilte Journey scheitern lässt.

**Behörde.** Barrierefreiheit ist ein gesetzliches Mandat und eine bürgerliche Pflicht, denn behinderte Bürgerinnen haben oft keine alternative Anbieterin für eine Leistung, Lizenz, oder Stimme. Bauen Sie nach dem Standard, den Ihre Rechtsprechung zitiert (zum Beispiel Section 508, EN 301 549, oder der European Accessibility Act, auf WCAG 2.2 AA abgebildet), veröffentlichen Sie eine Barrierefreiheitserklärung mit einem Weg, Barrieren zu melden, und testen Sie mit der behinderten Öffentlichkeit, der Sie dienen. Lehnen Sie Overlays als Ersatz für echte Konformität ab, und fordern Sie von Anbieterinnen glaubwürdigen Beleg und ein Recht auf Behebung im Vertrag.

## Beispiele

**Startup.** Ein dreiköpfiges Startup, das ein Einstellungswerkzeug baute, fügte vom allerersten Sprint an einen Barrierefreiheitsscanner zu seinem Build und einen schnellen Tastatur-Durchgang zu seiner Pull-Request-Checkliste hinzu, argumentierend, es sei günstiger, barrierefrei zu bleiben als es später zu beheben. Als das Beschaffungsteam einer mittelgroßen Kundin während eines Verkaufszyklus nach einem Barrierefreiheits-Konformitätsbericht fragte, nutzte das Startup bereits semantisches HTML, beschriftete jedes Feld, und hatte überall sichtbaren Fokus, es antwortete also in Tagen statt hektisch. Diese Bereitschaft gewann einen Deal, den eine Konkurrentin an derselben Anforderung verlor.

**Großunternehmen.** Eine große Einzelhändlerin sah sich einer Sammelklage gegenüber, weil blinde Kundinnen den Checkout nicht mit einem Screenreader abschließen konnten. Über die Vergleichszahlung und Anwaltskosten hinaus musste das Unternehmen unter einem gerichtlich überwachten Zeitplan beheben. Danach baute es Barrierefreiheit zurück in sein Designsystem und die CI-Pipeline, fügte Screenreader-Testen zur Definition von fertig hinzu, und schulte seine Teams. Der neu gebaute, barrierefreie Checkout verbesserte auch Konversion und reduzierte Support-Kontakte für alle: die Fixes, die Screenreader-Nutzerinnen halfen (klare Beschriftungen, Fehlermeldungen, logische Reihenfolge), halfen allen Nutzerinnen.

**Behörde.** Eine Behörde für öffentliche Leistungen war gesetzlich verpflichtet, WCAG 2.1 AA für ihren Online-Antrag zu erfüllen. Frühes Testen mit blinden und sehbehinderten Nutzerinnen, Nur-Tastatur-Nutzerinnen, und Nutzerinnen mit kognitiven Behinderungen offenbarte, dass ein Nur-Farbe-"Pflichtfeld"-Indikator, eine unzugängliche Datumsauswahl, und unangekündigte Validierungsfehler Menschen daran hinderten, fertig zu werden. Das durch semantisches Markup, sichtbaren Fokus, Live-Regionen-Fehlerankündigungen, und [einfache-Sprache](https://en.wikipedia.org/wiki/Plain_language)-Hilfe zu beheben, erlaubte behinderten Bürgerinnen, zum ersten Mal selbstständig zu beantragen. Das reduzierte Abhängigkeit von persönlicher Hilfe und senkte Bedienungskosten, während das gesetzliche Mandat erfüllt wurde.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Der Geschäftsfall ruht auf Marktreichweite, rechtlichem Risiko, Bedienungskosten, und Qualität. Behinderte Menschen und ihre Familien kontrollieren bedeutsame Kaufkraft; sie auszuschließen verwirkt sie. Barrierefreie Dienste reduzieren den Bedarf an teuren unterstützten Kanälen (Telefon- und persönliche Hilfe), was eine direkte operative Ersparnis ist, besonders für Behörden. Und weil Barrierefreiheitsverbesserungen (klare Beschriftungen, Tastaturunterstützung, lesbarer Inhalt, robustes Markup) allen helfen, erhöhen sie typischerweise Gesamtabschluss und Zufriedenheit.

Bei Gesamtbetriebskosten sind die Übernahmekosten Training, Werkzeug, und der Einbau von Barrierefreiheit in Komponenten und Pipelines, alles bescheiden, wenn Sie es von Anfang an tun. Die Kosten der Nicht-Übernahme sind schwerwiegend und kommen aus mehreren Richtungen: rechtliche Haftung (Klagen, Vergleiche, gerichtlich angeordnete Behebung, regulatorische Strafen), die weit höheren Kosten der Nachrüstung unter Terminendruck, Reputationsschaden, und die laufenden Kosten, ausgeschlossene Nutzerinnen über teurere Kanäle zu bedienen. Nachrüstung kostet typischerweise ein Vielfaches dessen, was Einbauen gekostet hätte.

Um den Fall gegenüber der Führung zu machen, führen Sie mit der rechtlichen Pflicht, wo sie gilt (sie ist für Behörden und zunehmend für den Privatsektor nicht verhandelbar). Dann quantifizieren Sie die adressierbare Population, die Sie ausschließen, die unterstützte-Kanal-Kosten dieses Ausschlusses, und die "Bordstein"-Gewinne für alle Nutzerinnen. Positionieren Sie Barrierefreiheit als Risikomanagement plus Qualität, nicht Wohltätigkeit.

## Anti-Muster und Fallstricke

- **Barrierefreiheit als Vor-Start-Häkchen**: eine Prüfung am Ende statt kontinuierlicher Praxis, teure Last-Minute-Nacharbeit garantierend.
- **"Div-Suppe"**: nicht-semantisches Markup mit Klick-Handlern auf generischen Elementen, unsichtbar für assistive Technologie.
- **ARIA-Missbrauch**: ARIA auf kaputtes Markup schrauben, was Screenreader mehr in die Irre führt als schlichtes Markup es täte.
- **Nur-Farbe-Information**: Status allein durch Farbe gezeigt, unsichtbar für farbenblinde Nutzerinnen.
- **Unsichtbarer Fokus**: Fokus-Umrisse aus ästhetischen Gründen entfernen, Tastaturnutzerinnen strandend.
- **Tastaturfallen**: Modals und Widgets, die Fokus einfangen oder verlieren.
- **Automatisierte-Scan-Selbstzufriedenheit**: einen Scanner bestehen und annehmen, das Produkt sei barrierefrei.
- **Barrierefreiheits-Overlays**: Drittanbieter-"Ein-Zeilen-Fix"-Widgets, die keine echte Konformität liefern und die Erfahrung verschlechtern können.
- **Behinderte Nutzerinnen von Forschung ausschließen**: für eine imaginierte behinderte Nutzerin gestalten statt mit echten zu testen.

## Reifegradmodell

**Stufe 1: Beginnen.** Keine Barrierefreiheitspraxis. Probleme werden nur entdeckt, wenn eine Nutzerin sich beschwert oder eine Klage ankommt, und Reaktion ist reaktiv. Markup ist nicht-semantisch und ungetestet, und niemand besitzt das Problem.

**Stufe 2: Entwickeln.** Bewusstsein existiert, und manche Teams handeln darauf: ein automatisierter Scanner in einem Build hier, ein Tastatur-Durchgang dort, eine Vor-Start-Prüfung vor einer großen Veröffentlichung. Praxis ist grundlegend und über Teams hinweg inkonsistent, Barrierefreiheit ist noch eine Spätphasen-Checkliste, und wird häufig unter Zeitplandruck depriorisiert.

**Stufe 3: Standardisieren.** WCAG 2.2 AA ist der dokumentierte Standard, organisationsweit durchgesetzt. Barrierefreiheit ist ins Designsystem eingebaut, damit Komponenten standardmäßig barrierefrei ausliefern, automatisch und manuell getestet, und in die Definition von fertig geschrieben. Teams sind geschult, eine Besitzerin oder ein Center of Excellence existiert, und ein Behebungsprozess ist definiert.

**Stufe 4: Steuern.** Barrierefreiheit wird mit Daten gegen Baselines gemessen und gesteuert. Die Organisation verfolgt Konformitätskennzahlen über Zeit (Scanner-Bestehensraten, die Anzahl offener Barrieren nach Schweregrad, Screenreader-Testabdeckung kritischer Journeys, und Zeit-bis-zur-Behebung), berichtet sie pro Team auf einem Dashboard, und behandelt Regressionen als Build-Fehlschläge statt beratende Warnungen. Ziele werden gegen eine Baseline gesetzt und Fortschritt wird überprüft, damit ein rutschendes Team sichtbar ist, bevor eine Prüfung es findet.

**Stufe 5: Orchestrieren.** Barrierefreiheit wird kontinuierlich verbessert und über die Organisation integriert. Behinderte Menschen sind wiederkehrend Teil von Forschung und Testen, und Barrierefreiheit ist in Beschaffung, Design-Tokens, und CI eingebettet. Die Organisation passt sich an, während sich Standards bewegen (neue WCAG-Kriterien übernehmend und sich auf WCAG 3.0 vorbereitend), und sie beeinflusst Anbieterinnen und Partnerinnen, damit die ganze Lieferkette konform ist.

## Diskussionsideen

- Wie verhindern Sie, dass Barrierefreiheit depriorisiert wird, wenn Termine sich straffen?
- Was ist der richtige Mix aus automatisiertem, manuellem, und Nutzertesten für Ihr Risikoprofil?
- Wie sollte Barrierefreiheitskonformität in Anbieterverträge und Beschaffung geschrieben werden?
- Wie handhaben Sie die Lücke zwischen WCAG-Konformität und echter Nutzbarkeit für behinderte Menschen?
- Wie sollten sich Teams auf WCAG 3.0 vorbereiten, während sie heute nach 2.2 bauen?
- Wie rekrutieren und entschädigen Sie behinderte Teilnehmerinnen fair und respektvoll für Forschung?

## Wichtigste Erkenntnisse

- Barrierefreiheit ist ein Grundqualitätsattribut und, für Behörden, eine gesetzliche Anforderung.
- Gestalten Sie nach WCAG 2.2 AA als Boden; nutzen Sie die POUR-Prinzipien als mentales Modell.
- Semantisches HTML zuerst; ARIA nur, um echte Lücken zu füllen, korrekt gemacht.
- Automatisierte Werkzeuge erwischen ungefähr ein Drittel der Probleme; manuelles und assistive-Technologie-Testen sind essentiell.
- Testen Sie mit behinderten Menschen, nicht nur für sie.
- Barrierefreiheit einzubauen ist günstig und dauerhaft; nachzurüsten ist teuer und brüchig.
- Barrierefreies Design ist besseres Design für alle: der Bordstein-Effekt ist echt.

## Referenzen und weiterführende Literatur

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2* und unterstützende Understanding/Techniques-Dokumente
- W3C, *WAI-ARIA Authoring Practices Guide*
- W3C Web Accessibility Initiative (WAI), einführende und Tutorial-Materialien
- Laura Kalbag, *Accessibility for Everyone*
- Sarah Horton und Whitney Quesenbery, *A Web for Everyone*
- Regine Gilbert, *Inclusive Design for a Digital World*
- U.S. Section 508 Standards und Section508.gov-Leitlinien
- Europäischer Standard EN 301 549 und der European Accessibility Act
- Behörden-Barrierefreiheitsleitlinien (z. B. UK GDS Accessibility Manual)
- WebAIM, Forschung und Artikel einschließlich der jährlichen Barrierefreiheitsanalysen
