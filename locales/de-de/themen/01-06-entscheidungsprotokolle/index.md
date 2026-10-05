# 1.6 Entscheidungsprotokolle

## Überblick und Motivation

Ein **Entscheidungsprotokoll** ist ein Dokument, das eine wichtige Entscheidung zusammen mit ihrem Kontext und ihren Konsequenzen festhält. Die bekannteste Form ist das **[Architekturentscheidungsprotokoll](https://en.wikipedia.org/wiki/Architectural_decision) (ADR)**, eine kurze, vorzugsweise unveränderliche Notiz, die eine architektonisch bedeutsame Wahl festhält, warum sie getroffen wurde und was aus ihr folgt. Die vollständige Sammlung von Protokollen eines Projekts ist sein **Entscheidungsprotokoll (ADL)**, und die Disziplin, sie zu führen, ist Teil des **Architekturwissensmanagements (AKM)**. Dieses Kapitel baut auf den Entscheidungsfindungs- und Governance-Praktiken aus Kapitel 1.5 auf und konzentriert sich darauf, wie man Entscheidungsprotokolle im großen Maßstab schreibt, speichert und pflegt.

Die Motivation ist einfach und schmerzhaft, auf die harte Tour zu lernen. Bei jedem langlebigen System ist die teuerste Frage "Warum um alles in der Welt wurde das so gebaut?", gestellt Monate oder Jahre später von Menschen, die nicht im Raum waren. Code zeigt *was* das System tut. Tests zeigen, dass es *funktioniert*. Aber keines von beiden erfasst *warum* Sie diesen Weg gegenüber den erwogenen und verworfenen Alternativen gewählt haben. Ohne Entscheidungsprotokolle verdunstet diese Begründung mit Personalwechsel. Teams verhandeln geklärte Fragen neu, machen gute Entscheidungen aus schlechten Gründen rückgängig oder behalten schlechte Entscheidungen aus Angst bei. Ein Entscheidungsprotokoll ist ein günstiger Brief an die Zukunft, der die Begründung bewahrt.

Für große Teams ist dies ebenso sehr ein Koordinationswerkzeug wie eine Gedächtnisstütze. Unternehmen betreiben Dutzende Teams, die überlappende Wahlen treffen. Ein gemeinsames Entscheidungsprotokoll verwandelt die hart erarbeitete Begründung eines Teams in ein wiederverwendbares Gut und verhindert divergente, inkompatible Entscheidungen. In behördlichen und regulierten Umgebungen sind Entscheidungsprotokolle nahezu obligatorisch. Prüfer, Aufsichtsgremien und Nachfolge-Auftragnehmer brauchen alle eine nachvollziehbare Begründung, die architektonisch bedeutsame Anforderungen mit den dagegen getroffenen Wahlen verbindet. Ein gut geführtes Entscheidungsprotokoll ist oft der Unterschied zwischen einem System, das Sie absichern und prüfen können, und einem, bei dem das nicht geht.

## Kernprinzipien

- **Protokollieren Sie das *Warum*, nicht nur das *Was*.** Kontext und verworfene Alternativen sind der Sinn der Sache.
- **Eine Entscheidung pro Protokoll.** Halten Sie jedes Protokoll spezifisch und eigenständig.
- **Klein und leichtgewichtig schlägt umfassend und ungenutzt.** Ein Ein-Seiten-Protokoll, das existiert, schlägt einen Bericht, der nie geschrieben wird.
- **Versehen Sie alles mit Zeitstempeln.** Kosten, Einschränkungen und Zulieferer ändern sich; datieren Sie jede Behauptung.
- **Bevorzugen Sie pragmatisch ein lebendiges Protokoll.** Unveränderlichkeit ist das Ideal; in der Praxis ergänzen Sie mit datierten Notizen.
- **Worte statt Abkürzungen.** "Entscheidungen" lädt zu mehr Beiträgen ein als "ADRs".
- **Machen Sie Entscheidungen auffindbar und, wo möglich, testbar.** Bringen Sie das richtige Protokoll im richtigen Moment ans Licht; sichern Sie es mit Fitnessfunktionen ab.

## Empfehlungen

### Die wesentliche Struktur erfassen

Ein gutes Entscheidungsprotokoll hat ein paar wesentliche Abschnitte. Passen Sie eine bekannte Vorlage an, statt eine zu erfinden:

- **Titel:** eine kurze, im Präsens-Imperativ formulierte Phrase ("[PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) für das Hauptbuch verwenden").
- **Status:** vorgeschlagen, akzeptiert, abgelöst, veraltet.
- **Kontext:** die Situation, Kräfte, Geschäftsprioritäten und Einschränkungen, die diese Entscheidung notwendig machen; schließen Sie die architektonisch bedeutsame Anforderung ein, die sie adressiert.
- **Entscheidung:** die getroffene Wahl, klar formuliert.
- **Konsequenzen:** was leichter und was schwerer wird, ausgelöste Folgeentscheidungen und akzeptierte Risiken.

Beliebte Vorlagen umfassen Michael Nygards (einfach und weit verbreitet), Tyree und Akermans (aufwendiger, mit gewichteten Alternativen), MADR (Markdown Any Decision Records, stark bei Optionen und ihren Vor-/Nachteilen), und Y-Statements (eine ein-satz-strukturierte Form). Standardisieren Sie auf eine pro Organisation, damit Protokolle vergleichbar sind. Siehe Kapitel 12.3 für eine Copy-Paste-Vorlage.

### Protokolle schreiben, die spezifisch, datiert und quasi-unveränderlich sind

Halten Sie jedes Protokoll bei genau einer Entscheidung. Versehen Sie einzelne Behauptungen mit Zeitstempeln, besonders alles, was driftet: Preise, Skalierungszahlen, Zulieferer-Fähigkeiten, Lizenzbedingungen. In der Theorie sollte ein Protokoll unveränderlich sein. Wenn sich eine Entscheidung ändert, schreiben Sie ein *neues* Protokoll, das das alte ablöst und die Geschichte bewahrt. In der Praxis stellen viele Teams fest, dass ein **lebendes Dokument**-Ansatz besser funktioniert: neue Informationen in das bestehende Protokoll einfügen, mit einem Zeitstempel und einer Notiz, dass sie nach der Entscheidung eintrafen. Beide sind legitim. Der unveränderliche Stil ist stärker für Prüfspuren; der lebende Stil ist besser für alltägliches Teamwissen. Wählen Sie bewusst und seien Sie konsistent.

### Protokolle dort speichern, wo die Arbeit ist

Legen Sie Entscheidungsprotokolle in der [Versionskontrolle](https://en.wikipedia.org/wiki/Version_control) neben dem Code ab: ein `decisions/`- (oder `adr/`-) Verzeichnis mit [Markdown](https://en.wikipedia.org/wiki/Markdown)-Dateien, eine pro Entscheidung, benannt mit einer kleingeschriebenen, mit Bindestrichen getrennten Imperativ-Verbphrase (`datenbank-waehlen.md`, `zeitstempel-formatieren.md`). Das gibt Ihnen Geschichte, Prüfung und Diffing kostenlos, und hält die Begründung neben dem, was sie erklärt. Wenn Ihr Team [Wikis](https://en.wikipedia.org/wiki/Wiki), Google Docs oder einen Jira-artigen Tracker bevorzugt, nutzen Sie stattdessen die. Das Werkzeug zählt weit weniger als die Gewohnheit. Ein leichtgewichtiges Kommandozeilenwerkzeug (wie `adr-tools`) kann Protokolle gerüstartig anlegen und indexieren.

### Sie "Entscheidungen" nennen und über Architektur hinaus erweitern

Eine praktische Erkenntnis vieler Teams: Die Bezeichnung zählt. Manche Entwicklerinnen und Führungskräfte sträuben sich gegen das Wort "Architektur", und "Protokoll" kann sich wie nachträglicher Papierkram anfühlen. Das Verzeichnis einfach "Entscheidungen" zu nennen, legt oft einen Schalter um. Teams beginnen, Zulieferer-Wahlen, Planungsentscheidungen, Terminentscheidungen, Daten- und Compliance-Entscheidungen zu protokollieren, alle mit derselben Vorlage. Menschen lernen schneller aus Worten als aus Abkürzungen, und sie tragen mehr bei, wenn die Rahmung "hilf deinen zukünftigen Teamkolleginnen zu denken" statt "reiche das obligatorische Formular ein" lautet.

### Den Lebenszyklus und die Governance definieren

Damit Entscheidungsprotokolle skalieren, vereinbaren Sie den umgebenden Prozess (hier trifft die Governance aus Kapitel 1.5 auf die Praxis):

- **Wer eines aufwerfen darf und was es rechtfertigt:** typischerweise jede informierte Mitwirkende; werfen Sie ein Protokoll auf, wenn zukünftige Entwicklerinnen das *Warum* brauchen werden, und überspringen Sie es bei risikoarmen, eigenständigen oder bereits dokumentierten Wahlen.
- **Lebenszyklus:** ein einfacher Fluss wie *Einleiten → Erforschen → Bewerten → Umsetzen → Pflegen → Auslaufen lassen*, mit Akzeptanzkriterien für den Übergang zwischen Stufen (Problem artikuliert, Alternativen erwogen, Abwägungen dokumentiert, Stakeholder konsultiert).
- **Rollen:** Vorschlagende, Forschende, Prüfende, Genehmigende und eine verantwortliche Pflegerin, die das Protokoll periodisch überprüft (mindestens jährlich) und das eventuelle Auslaufen vorantreibt.
- **Governance:** wie Konsens, Konflikt, Eskalation und Veto funktionieren, und alle Compliance-Einschränkungen. Stützen Sie sich auf Prinzipien wie *Neigung zum Handeln* und *[Nicht-einverstanden-aber-mittragen](https://en.wikipedia.org/wiki/Disagree_and_commit)*, und reservieren Sie schwereren Prozess für unumkehrbare Entscheidungen mit großer Auswirkung ("Ein-Wege-Tür").

### Entscheidungen testbar und auffindbar machen

Ein Entscheidungsprotokoll *dokumentiert* eine Entscheidung; eine **Fitnessfunktion** *sichert* sie ab: eine automatisierte Prüfung, ausgeführt in der [kontinuierlichen Integration](https://en.wikipedia.org/wiki/Continuous_integration) (CI), die verifiziert, dass die Entscheidung noch gilt ("alle Zustandsänderungen müssen Ereignisse aussenden", "kein Modul darf über diese Grenzen hinweg importieren", mit Werkzeugen wie ArchUnit). Das verwandelt Governance von periodischer manueller Prüfung in kontinuierliche, skalierbare Durchsetzung, was besonders wertvoll für regulatorische und Prüfungsziele ist (Kapitel 3.1, 4.6, 8.5). Bringen Sie dann das *richtige* Protokoll im *richtigen* Moment ans Licht. Werkzeuge, die relevante Entscheidungen an eine Pull-Request anhängen, wenn eine Entwicklerin den Code berührt, den sie regeln, schlagen die Hoffnung, dass Menschen einen Dokumentationsordner lesen.

## Abwägungen: Vor- und Nachteile

| Wahl | Vorteile | Nachteile |
|---|---|---|
| **Leichtgewichtige ADRs (Nygard/MADR)** | Schnell zu schreiben, werden tatsächlich geschrieben; wenig Zeremonie | Weniger Strenge für hochriskante, umstrittene Entscheidungen |
| **Schwergewichtige Vorlagen (Tyree-Akerman)** | Gewichtete Alternativen; stark für große, kostspielige Wahlen | Langsamer; kann von Routineprotokollierung abschrecken |
| **Unveränderlich + Ablösung** | Saubere Prüfspur; Geschichte bewahrt | Mehr Protokolle; Leser müssen Ketten verfolgen |
| **Lebendes Dokument (datierte Ergänzungen)** | Einzige aktuelle Wahrheitsquelle; leicht zu pflegen | Schwächere Prüfgeschichte; Risiko stiller Bearbeitungen |
| **Markdown im Repository** | Versioniert, prüfbar, neben dem Code | Weniger freundlich für Nicht-Entwicklerinnen |
| **Wiki/Dokumentationswerkzeug** | Zugänglich für alle Rollen | Geschichte und Prüfung schwächer; driftet vom Code weg |

Die Kernspannung ist **Strenge gegen Adoption**. Das strengste System, das niemand nutzt, protokolliert nichts. Das leichteste System, das jeder nutzt, summiert sich im Wert. Setzen Sie standardmäßig auf leichtgewichtig, und reservieren Sie schwereren Prozess für die wenigen Entscheidungen, die teuer und schwer umzukehren sind.

## Fragen zur Diskussion mit Ihrem Team

1. **Wie erreicht das richtige Entscheidungsprotokoll eine Entwicklerin im Moment, in dem sie den Code berührt, den es regelt, statt in einem Ordner zu sitzen, den niemand öffnet?** Ein Nur-Schreib-Protokoll protokolliert Begründung, die nie Verhalten ändert, was der häufigste Weg ist, wie Entscheidungsprotokolle scheitern: Sie existieren, und niemand liest sie, wenn es zählt. Die konkurrierende Erwägung ist Aufwand, denn Protokolle automatisch ans Licht zu bringen (sie an eine Pull-Request anzuhängen, wenn jemand den geregelten Code bearbeitet) erfordert Werkzeuginvestition, die ein Wiki oder Dokumentationsordner nicht braucht. Bringen Sie Belege in die Diskussion: Als jemand kürzlich eine geklärte Frage rückgängig machte oder neu verhandelte, war das relevante Protokoll in diesem Moment auffindbar, oder vergraben? Für eine große Organisation mit Dutzenden Teams ist Auffindbarkeit das, was die hart erarbeitete Begründung eines Teams in ein wiederverwendbares Gut statt ein privates Archiv verwandelt. Entscheiden Sie, ob Sie Protokolle in der Versionskontrolle neben dem Code speichern und in den Pull-Request-Fluss einbinden, damit das Protokoll dort erscheint, wo die Arbeit geschieht.

2. **Wer ist die verantwortliche Pflegerin für jedes Protokoll, und was verhindert, dass Ihr Protokoll zu selbstbewusster Fehlinformation verkommt?** Der gefährliche Versagensmodus eines Entscheidungsprotokolls ist nicht ein leerer Ordner, es ist ein Ordner voller Protokolle, deren Kosten, Zulieferer-Fähigkeiten und Einschränkungen still vor Jahren veraltet sind. Jedes Protokoll braucht eine verantwortliche Besitzerin, die es in einem Rhythmus überprüft (mindestens jährlich) und Ablösung oder Auslaufen vorantreibt, sonst verrottet das Protokoll zu Folklore, die Menschen selektiv zitieren und wenig vertrauen. Bringen Sie Belege: Wie viele Ihrer Protokolle sind undatiert, wie viele beschreiben einen Zulieferer oder Preis, der sich seitdem geändert hat, und wann wurde jedes zuletzt überprüft? In behördlichen und regulierten Umgebungen ist das schärfer, weil eine unveränderliche, abgelöste Kette genau das ist, worauf Prüfer und Nachfolge-Auftragnehmer für eine nachvollziehbare Begründung angewiesen sind. Entscheiden Sie Ihren Lebenszyklus explizit, versehen Sie einzelne driftende Behauptungen mit Zeitstempeln, und weisen Sie Pflegerinnen zu, damit das Protokoll ein lebendiges Gut bleibt statt ein Friedhof.

3. **Sollten Sie über alle Teams hinweg auf eine Vorlage standardisieren, und wie viel Strenge brauchen Ihre folgenreichsten Entscheidungen tatsächlich?** Vergleichbarkeit ist ein echter Vorteil: Wenn jedes Team dieselbe Form nutzt (Nygard, MADR oder ähnlich), kann ein neues Team drei frühere Protokolle finden und die Begründung an einem Nachmittag übernehmen, statt einen Monat zu debattieren. Die Kernspannung ist Strenge gegen Adoption, denn die schwerste Vorlage, die niemand nutzt, protokolliert nichts, während die leichteste, die jeder nutzt, sich im Wert summiert. Bringen Sie Belege: Werden Protokolle tatsächlich geschrieben, und getrennt davon, wurden große, umstrittene, kostspielige Entscheidungen unteranalysiert, weil die leichtgewichtige Form das Abwägen von Alternativen übersprang? Für Unternehmen, die überlappende Wahlen über Teams hinweg koordinieren, verhindert eine gemeinsame Vorlage plus ein durchsuchbarer Index divergente, inkompatible Entscheidungen. Setzen Sie standardmäßig auf leichtgewichtig für den üblichen Fall, und vereinbaren Sie im Voraus, welche Ein-Wege-Tür-Entscheidungen eine schwerere Form mit gewichteten Alternativen rechtfertigen.

4. **Was rechtfertigt tatsächlich das Aufwerfen eines Entscheidungsprotokolls, und wer hat die Autorität zu sagen, dass eine Wahl keins braucht?** Setzen Sie die Messlatte zu hoch, verdunstet die Begründung hinter folgenreichen Wahlen; setzen Sie sie zu niedrig, füllt sich das Protokoll mit Trivialitäten, die die Protokolle begraben, die Menschen wirklich brauchen. Für eine große Organisation bedeutet eine unklare Schwelle, dass jedes Team seine eigene improvisiert, sodass die Abdeckung ungleichmäßig wird und niemand darauf vertrauen kann, dass ein fehlendes Protokoll eine unwichtige Entscheidung signalisiert. Bringen Sie Belege in die Diskussion: eine Handvoll jüngster Entscheidungen, die protokolliert wurden, aber es nicht hätten sein müssen, und schmerzhafte, die unprotokolliert blieben und Sie später eine Wiederentdeckung kosteten. Vereinbaren Sie einen einfachen Test, etwa zu protokollieren, wann immer eine zukünftige Entwicklerin das *Warum* brauchen wird, und risikoarme, eigenständige oder bereits dokumentierte Wahlen zu überspringen. In regulierten und behördlichen Umgebungen verschiebt sich das Kalkül, denn ein Prüfungsmandat kann ein Protokoll für jede architektonisch bedeutsame Anforderung verlangen, unabhängig davon, ob das Team es für wert hält, sie zu schreiben, benennen Sie also im Voraus, welche Entscheidungen nicht verhandelbar sind.

5. **Sind Ihre Protokolle echte, im Moment der Entscheidung erfasste Begründung, oder nachträglich geschriebener Papierkram, um ein Mandat zu erfüllen?** Ein nachträglich erstelltes Protokoll, um ein Ticket zu schließen, neigt dazu, die gewählte Option zu beschönigen und still die tatsächlich abgewogenen Alternativen wegzulassen, was genau die Information ist, die eine zukünftige Leserin am meisten braucht. Der konkurrierende Druck ist real: Das *Warum* vor oder während einer Entscheidung zu schreiben, fühlt sich langsamer an als zu liefern, und die verworfenen Wege schriftlich zuzugeben, erfordert psychologische Sicherheit, die manchen Teams fehlt. Bringen Sie eine Stichprobe jüngster Protokolle an den Tisch und fragen Sie ehrlich, ob der Kontext und die verworfenen Alternativen wie echte Bedächtigkeit oder wie nachträglich konstruierte Rechtfertigung lesen. Für ein großes Team sind hohle Protokolle schlimmer als keine, weil sie Menschen lehren, dass dem Protokoll nicht vertraut werden kann. In Unternehmens- und Behördenprüfung ist diese Unterscheidung scharf: Aufsichtsgremien und Nachfolge-Auftragnehmer sind auf eine Begründung angewiesen, die widerspiegelt, was wirklich erwogen wurde, und ein Protokoll, das wie Theater liest, untergräbt die Absicherung, für die das Protokoll existiert.

6. **Welche Ihrer folgenreichsten Entscheidungen können Sie mit einer automatisierten Fitnessfunktion absichern, statt darauf zu vertrauen, dass periodische manuelle Prüfung eine Verletzung erwischt?** Ein Entscheidungsprotokoll dokumentiert eine Wahl, aber nur eine automatisierte Prüfung, ausgeführt in kontinuierlicher Integration, verhindert, dass diese Wahl still erodiert, während Dutzende Entwicklerinnen über Jahre den Code berühren. Die Abwägung ist Investition, denn das Schreiben und Pflegen von Fitnessfunktionen (mit Werkzeugen wie ArchUnit) kostet technische Zeit, und viele Entscheidungen, besonders Prozess- oder Zulieferer-Wahlen, sind überhaupt nicht maschinell testbar. Bringen Sie Belege: Welche Grenzentscheidungen (Modulabhängigkeiten, Ereignisaussendung, Datenzugriffsregeln) wurden still verletzt und erst spät in der Prüfung oder in der Produktion erwischt? Für ein Unternehmen mit vielen Teams verwandeln Fitnessfunktionen Governance von einem zentralen Engpass in kontinuierliche Durchsetzung, die skaliert, ohne alle zu verlangsamen. In regulierten und behördlichen Kontexten ist eine automatisierte, immer aktive Prüfung ein weit stärkerer Prüfungsbeleg als eine Unterschrift bei einer Prüfung, denn sie beweist, dass die Entscheidung heute noch gilt, statt dass jemand sie einst genehmigte.

## Branchenperspektive

**Startup.** Beschränken Sie sich auf die Gewohnheit und nichts sonst: einen `decisions/`-Ordner in Ihrem Hauptrepository und eine Zwei-Abschnitt-Notiz (Kontext und Wahl), wann immer Sie eine Entscheidung treffen, die Ihr zukünftiges Ich hinterfragen wird. Überspringen Sie Lebenszyklus, Rollen und Genehmigende vollständig, denn Prozess, den Sie nicht durchhalten können, ist Prozess, den Sie aufgeben werden. Das eine Protokoll, das Ihre erste Neueinstellung davor bewahrt zu fragen, warum das System so gebaut ist, zahlt bereits die ganze Praxis zurück.

**Kleinunternehmen.** Ohne dedizierte Architektin und mit wenig Zeit legen Sie Protokolle dort ab, wo Ihr Team bereits arbeitet, sei es ein Wiki, ein gemeinsames Dokument oder das Repository, statt ein dediziertes Werkzeug zu kaufen. Die Gewohnheit zählt weit mehr als das Werkzeug, senken Sie also die Hürde: Nennen Sie das Verzeichnis "decisions" statt "adr", und erfassen Sie Zulieferer- und Kaufen-versus-Bauen-Wahlen im selben Atemzug wie technische. Wenn Sie sich auf externe Auftragnehmer stützen, ist eine kurze, datierte Notiz darüber, warum Sie einen Zulieferer oder eine Plattform gewählt haben, günstige Versicherung dagegen, in eine Wahl eingesperrt zu werden, die später niemand erklären kann.

**Großunternehmen.** Die Arbeit ist Koordination über viele Teams: Standardisieren Sie auf eine Vorlage, veröffentlichen Sie einen durchsuchbaren teamübergreifenden Index, und untermauern Sie wichtige Grenzentscheidungen mit Fitnessfunktionen, damit Verletzungen den Build scheitern lassen, statt auf Prüfung zu warten. Weisen Sie jedem Protokoll eine verantwortliche Pflegerin mit einem Überprüfungsrhythmus zu, damit das Protokoll ein lebendiges Gut bleibt, statt zu Folklore zu verkommen. Gut gemacht, wird die Begründung eines Teams für eine schwierige Wahl zu einem Gut, das das nächste Team an einem Nachmittag übernimmt, statt es neu zu verhandeln.

**Behörde.** Beschaffungsregeln, Transparenz und öffentliche Rechenschaftspflicht machen Entscheidungsprotokolle nahezu obligatorisch. Verlangen Sie ein unveränderliches, abgelöstes Protokoll für jede architektonisch bedeutsame Anforderung, jedes die Wahl mit dem Mandat oder Compliance-Kontrolle verknüpfend, die sie erfüllt, damit Aufsichtsgremien eine nachvollziehbare Begründung finden statt einer Rekonstruktion. Weil öffentliche Systeme mehrjährige, mehrere Zulieferer umfassende Lebensdauern überspannen, ist ein gut geführtes Protokoll oft das, was einen Nachfolge-Auftragnehmer verstehen lässt, warum das System so geformt ist, wie es ist, und die Arbeit fortzusetzen, ohne geklärten Boden neu zu verhandeln.

## Beispiele

**Startup.** Ein fünfköpfiges Startup fügt seinem Hauptrepository einen einfachen `decisions/`-Ordner hinzu, mit einer Zwei-Abschnitt-Notiz (Kontext und Wahl), wann immer jemand eine Entscheidung trifft, die ihr zukünftiges Ich hinterfragen wird. Es gibt keinen Lebenszyklus, keine Rollen und keine Genehmigenden: nur die Gewohnheit, das *Warum* neben dem Code zu schreiben. Als ihre erste Neueinstellung sechs Monate später beitritt, liest sie den ganzen Ordner in einer Stunde und hört auf zu fragen "Warum ist das so gebaut?". Das leichtgewichtige Protokoll kostet Minuten pro Eintrag und erspart ihnen die Wiederentdeckungssteuer, die lange bevor ein Team groß wird, zubeißt.

**Großunternehmen.** Ein Einzelhändler mit 30 Ingenieurteams standardisiert auf Protokolle im MADR-Format in jedem Repository, plus einen durchsuchbaren zentralen Index. Wenn ein neues Team vor "[Monorepo](https://en.wikipedia.org/wiki/Monorepo) versus Multirepo" steht, finden sie drei frühere Protokolle mit Kontext und Konsequenzen und übernehmen die Begründung an einem Nachmittag statt einen Monat zu debattieren. Wichtige Grenzentscheidungen (Diensteigentum, Datenzugriffsregeln) werden durch ArchUnit-Fitnessfunktionen untermauert, sodass Verletzungen den Build scheitern lassen, statt in der Prüfung erwischt zu werden. Das ist Governance, die skaliert, ohne zentralen Engpass.

**Behörde.** Eine Behörde, die ein Leistungssystem modernisiert, verlangt ein ADR für jede architektonisch bedeutsame Anforderung, jedes die Entscheidung mit dem Mandat oder der Compliance-Kontrolle verknüpfend, die sie erfüllt (Barrierefreiheit, Datenresidenz, Prüfbarkeit). Protokolle sind unveränderlich und werden abgelöst, was ein nachvollziehbares Protokoll erzeugt, das die Aufsichtsprüfung erfüllt. Entscheidend ist auch, dass es einen Nachfolge-Auftragnehmer verstehen lässt, *warum* das System so geformt ist, wie es ist, und Kontinuität über die mehrjährigen, mehrere Zulieferer umfassenden Lebensdauern bewahrt, die typisch für öffentliche Programme sind (Kapitel 4.6, 10.4).

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Ein Entscheidungsprotokoll kostet Minuten zu schreiben und ein paar mehr zu prüfen. Die Rendite sind vermiedene *Neu-Entscheidungs*-Kosten und vermiedene *Falsch-Umkehrungs*-Kosten, beide groß und wiederkehrend bei langlebigen Systemen. Jedes Mal, wenn ein Team eine geklärte Frage neu verhandelt oder eine solide Wahl rückgängig macht, weil sich niemand an die Einschränkung dahinter erinnert, zahlt es in Senior-Ingenieurszeit und oft in einem Vorfall. Ein Entscheidungsprotokoll wandelt diese wiederkehrende Steuer in ein einmaliges Schreiben um.

Bei den **Gesamtbetriebskosten** gehören Entscheidungsprotokolle zu der Dokumentation mit dem höchsten Hebel, die Sie führen können, denn sie zielen auf das personalwechsel-empfindlichste Gut: Begründung. Onboarding ist schneller (Neueinstellungen lesen das *Warum*, nicht nur den Code). Modernisierung ist sicherer (Kapitel 3.6: Sie können wesentliche von beiläufigen Entscheidungen unterscheiden). Prüfungen sind günstiger (der Beleg existiert bereits). Die Kosten, sie *nicht* zu führen, sind auf keinem Dashboard sichtbar und summieren sich still mit jedem Weggang. Um Führungskräften den Fall darzulegen, verweisen Sie auf eine jüngste teure Wiederentdeckung oder eine rückgängig gemachte Entscheidung, die einen Vorfall verursachte, und stellen Sie fest, dass die Korrektur fast nichts kostet einzuführen.

## Anti-Muster und Fallstricke

- **Das *Was* ohne das *Warum* protokollieren:** Kontext und verworfene Alternativen weglassen, den ganzen Sinn der Sache.
- **Nachträglicher Papierkram:** Protokolle geschrieben, um ein Mandat zu erfüllen, nicht um zu denken; sie lesen sich hohl, und niemand vertraut ihnen.
- **Mehr-Entscheidungs-Mega-Dokumente:** eine riesige Seite, die niemand navigieren oder sauber ablösen kann.
- **Undatierte Behauptungen:** Kosten und Einschränkungen, die einst wahr waren, als zeitlos dargestellt.
- **Stille Bearbeitungen:** die Geschichte einer Entscheidung ohne datierte Notiz ändern, die Prüfspur zerstörend.
- **Nur-Schreib-Protokolle:** Protokolle erstellt und nie im Moment ihrer Relevanz ans Licht gebracht, sodass sie Verhalten nicht beeinflussen.
- **Abkürzungswächterei:** auf "ADR" und "Architektur" bestehen und dadurch Beiträge entmutigen.
- **Kein Lebenszyklus:** Protokolle, die nie überprüft, abgelöst oder ausgelaufen lassen werden, zu Fehlinformation verrottend.

## Reifegradmodell

- **Stufe 1 (Beginnen):** Entscheidungen leben in Köpfen, Chat-Threads und Commit-Nachrichten; Erfassung ist reaktiv und ad hoc, und Begründung geht routinemäßig mit Personalwechsel verloren.
- **Stufe 2 (Entwickeln):** Manche Teams führen Protokolle, in unterschiedlichen Formaten und Vorlagen, wann immer sich eine Einzelperson erinnert; die Praxis ist über Teams hinweg uneinheitlich, ohne gemeinsames Protokoll, Benennung oder Prozess.
- **Stufe 3 (Standardisieren):** Eine einzige Vorlage, Speicherung im Repository, und ein definierter Lebenszyklus und Governance (Aufwerf-/Überspring-Kriterien, Rollen, Überprüfungsrhythmus) sind dokumentiert und werden organisationsweit konsistent angewendet; Protokolle werden überprüft und abgelöst statt still bearbeitet.
- **Stufe 4 (Steuern):** Das Entscheidungsprotokoll wird gegen Baselines gemessen: Abdeckung (der Anteil architektonisch bedeutsamer Entscheidungen mit Protokoll), Aktualität (der Anteil der innerhalb ihres Rhythmus überprüften Protokolle, plus die Zahl undatierter oder veralteter Behauptungen) und Auffindbarkeit (wie oft ein relevantes Protokoll tatsächlich die Entwicklerin erreichte, die den geregelten Code änderte). Verantwortliche Pflegerinnen handeln nach diesen Kennzahlen, lösen veraltete Protokolle ab und schließen Abdeckungslücken aufgrund von Belegen statt Anekdoten.
- **Stufe 5 (Orchestrieren):** Ein durchsuchbares teamübergreifendes Entscheidungsprotokoll ist in die tägliche Arbeit integriert: relevante Protokolle erscheinen automatisch bei den Änderungen, die sie regeln, wichtige Entscheidungen werden durch Fitnessfunktionen in kontinuierlicher Integration abgesichert, und das Protokoll speist Onboarding, Modernisierung und Prüfung als lebendiges Gut. Die Organisation verbessert die Praxis selbst kontinuierlich, löst Protokolle ab, lässt sie auslaufen und passt ihren Umfang an, während sich das System und seine Einschränkungen verschieben, und balanciert neu aus, wo sie in Strenge investiert, während das Entscheidungsportfolio wächst.

## Diskussionsideen

1. Was war die letzte Entscheidung, die Ihr Team rückgängig machte oder neu verhandelte, weil sich niemand an die ursprüngliche Begründung erinnerte?
2. Würde die Umbenennung Ihres `adr/`-Verzeichnisses in `decisions/` ändern, wer beiträgt und was protokolliert wird?
3. Welche Ihrer kritischen Entscheidungen könnten heute durch eine automatisierte Fitnessfunktion abgesichert werden?
4. Unveränderlich-und-ablösen oder lebendes Dokument: Was passt zu Ihren Prüfpflichten und Ihrer Kultur, und warum?
5. Wie würde eine Neueinstellung (oder ein Nachfolge-Auftragnehmer) derzeit entdecken, *warum* Ihr System so geformt ist, wie es ist?
6. Was rechtfertigt das Aufwerfen eines Entscheidungsprotokolls in Ihrem Team, und was rechtfertigt, *keins* aufzuwerfen?

## Wichtigste Erkenntnisse

- Ein Entscheidungsprotokoll erfasst eine wichtige Entscheidung mit ihrem **Kontext und ihren Konsequenzen**: das *Warum*, nicht nur das *Was*.
- Halten Sie Protokolle **spezifisch, mit Zeitstempel und leichtgewichtig**; standardisieren Sie auf eine Vorlage (Nygard, MADR oder ähnlich).
- Speichern Sie sie **in der Versionskontrolle neben dem Code**; erwägen Sie, sie "Entscheidungen" zu nennen, um Beiträge zu erweitern.
- Definieren Sie einen **Lebenszyklus und Governance** (Aufwerf-/Überspring-Kriterien, Rollen, Überprüfungsrhythmus); reservieren Sie schweren Prozess für Ein-Wege-Tür-Entscheidungen.
- Machen Sie Entscheidungen im Moment der Änderung **auffindbar** und, wo möglich, über Fitnessfunktionen **testbar**.
- Die Rendite ist vermiedene Wiederentdeckung und Falsch-Umkehrungs-Kosten; der Gesamtbetriebskosten-Fall ist am stärksten, wo Personalwechsel, Modernisierung und Prüfung am meisten zählen. Siehe Kapitel 1.5 (Entscheidungsfindung und Governance) und Kapitel 3.1 (Grundlagen der Architektur).

## Referenzen und weiterführende Literatur

- Michael Nygard, "Documenting Architecture Decisions" (2011): das grundlegende leichtgewichtige ADR.
- MADR: Markdown Any Decision Records-Projekt (adr.github.io/madr).
- Jeff Tyree und Art Akerman, "Architecture Decisions: Demystifying Architecture" (*IEEE Software*, 2005).
- Olaf Zimmermann, "Y-Statements" und "Architectural Decision Making" (ozimmer.ch).
- Joel Parker Henderson, *Architecture Decision Record (ADR)*: Vorlagen, Beispiele und Teamwork-Anleitung (github.com/joelparkerhenderson/architecture-decision-record).
- ThoughtWorks Technology Radar: "Lightweight Architecture Decision Records."
- Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage, *Building Evolutionary Architectures* (Fitnessfunktionen).
- AWS Prescriptive Guidance, "ADR process"; Red Hat, "Why you should use ADRs."
- Wikipedia, "Architectural decision" und "Architecturally significant requirements."
