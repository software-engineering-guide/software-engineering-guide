# 2.7 Dokumentation

## Überblick und Motivation

[Dokumentation](https://en.wikipedia.org/wiki/Software_documentation) ist das schriftliche Wissen, das Menschen erlaubt, Software zu nutzen, zu betreiben, und zu ändern, ohne Verständnis allein aus dem Code zusammensetzen zu müssen. Sie kommt in vielen Genres: wie man loslegt, wie man eine Aufgabe erledigt, wie ein System strukturiert ist, wie man auf einen Vorfall reagiert, was eine [API](https://en.wikipedia.org/wiki/API) akzeptiert und zurückgibt. Jedes dient einer anderen Leserin mit einem anderen Bedürfnis. Gute Dokumentation ist nicht optional. Sie ist der Unterschied zwischen Wissen, das über eine große Organisation skaliert, und Wissen, das nur in ein paar Köpfen lebt.

Für große Teams ist Dokumentation Ihre beste Verteidigung gegen Schlüsselpersonenrisiko (die Gefahr, wenn kritisches Wissen bei nur einer oder wenigen Personen sitzt) und Ihr schnellster Weg, Neueinstellungen einzubinden. Wenn Hunderte Ingenieurinnen von Systemen abhängen, die sie nicht gebaut haben, und Menschen ständig beitreten, wechseln, und gehen, kann die Organisation nur funktionieren, wenn Wissen aufgeschrieben und leicht zu finden ist. Undokumentierte Systeme werden zerbrechlich: Nur ihre Autoren können sie sicher ändern, und wenn diese Autoren gehen, verliert die Organisation die Fähigkeit, ihre eigene Software zu pflegen. Das ist eines der häufigsten und teuersten Versagen im großen Maßstab.

Unternehmens- und Behördenkontexte erhöhen die Einsätze weiter. Systeme leben lange, Ihre Dokumentation muss also Pflegenden Jahre, sogar Jahrzehnte dienen, nachdem das ursprüngliche Team gegangen ist. Regulatorische und Prüfungsregime schreiben oft spezifische Dokumente als Kontrollbeleg vor: Architekturprotokolle, [Runbooks](https://en.wikipedia.org/wiki/Runbook) (schrittweise betriebliche und Vorfallreaktionsverfahren), und Entscheidungsprotokolle. Öffentliche Systeme, zwischen Zulieferern übergeben, verlassen sich vollständig auf Dokumentation, um Wissen über Vertragsgrenzen hinweg zu tragen. Und doch ist Dokumentation berüchtigt anfällig für Verfall, die echte Herausforderung ist also, sie genau zu halten, während sich die Software ändert.

## Kernprinzipien

- Schreiben Sie für eine spezifische Leserin mit einem spezifischen Bedürfnis; verschiedene Dokumentationstypen dienen verschiedenen Zwecken.
- Halten Sie Dokumentation nah am Code und behandeln Sie sie als Code (Docs-as-Code).
- Genauigkeit schlägt Vollständigkeit; eine kleine Menge vertrauenswürdiger Dokumentation schlägt eine große, die falsch ist.
- Generieren Sie, was generiert werden kann; pflegen Sie nicht von Hand, was ein Werkzeug aus der Wahrheitsquelle produzieren kann.
- Bekämpfen Sie Dokumentationsverfall aktiv; veraltete Dokumentation ist schlimmer als keine, weil sie irreführt.
- Machen Sie Dokumentation auffindbar; unauffindbares Wissen ist effektiv abwesend.
- Protokollieren Sie Entscheidungen und ihre Begründung, nicht nur den aktuellen Zustand.

## Empfehlungen

### Docs-as-Code übernehmen

Halten Sie Dokumentation in der [Versionskontrolle](https://en.wikipedia.org/wiki/Version_control) direkt neben dem Code, den sie beschreibt, schreiben Sie sie in Klartext-Markup, und prüfen Sie sie durch denselben Pull-Request-Prozess. Das hält sie versioniert, prüfbar, und nah am Code, damit Sie beide zusammen aktualisieren können. Veröffentlichen Sie sie durch eine automatisierte Pipeline, damit die neueste Version immer verfügbar ist. Dokumentation als Code zu behandeln bringt dieselbe Disziplin, die Code vertrauenswürdig hält: Prüfung, Geschichte, und Automatisierung.

### Inhalt mit dem Diátaxis-Framework strukturieren

Organisieren Sie Dokumentation in vier eigenständige Typen, denn sie zu mischen dient keiner Leserin gut: Tutorials (lernorientiert, für Neulinge), Anleitungen (aufgabenorientiert, für ein spezifisches Ziel), Referenz (informationsorientiert, präzise und vollständig), und Erklärung (verständnisorientiert, das Warum und der Kontext). Halten Sie diese getrennt, und alles wird leichter zu schreiben, zu navigieren, und zu pflegen, weil jede Seite eine klare Aufgabe und ein klares Publikum hat.

### Die wesentlichen operativen Dokumente pflegen

Geben Sie jedem Repository eine klare [README](https://en.wikipedia.org/wiki/README) als Haustür: was es ist, wie man es baut und ausführt, und wohin man als Nächstes geht. Schreiben Sie Runbooks für operative Aufgaben und Vorfallreaktion, damit jeder im Bereitschaftsdienst handeln kann, nicht nur die Expertinnen. Halten Sie Architekturdokumentation, die die Struktur und Schlüsselkomponenten des Systems erklärt. Und bieten Sie Onboarding-Dokumentation, die eine neue Ingenieurin schnell produktiv macht. Das sind die Dokumente, die Ihnen am meisten fehlen, wenn sie nicht da sind.

### API-Dokumentation und Änderungsprotokolle aus der Wahrheitsquelle generieren

Generieren Sie Ihre API-Referenzdokumentation aus dem maschinenlesbaren Vertrag oder Code-Annotationen, damit sie nicht von der tatsächlichen Schnittstelle abdriften kann. Führen Sie ein [Änderungsprotokoll](https://en.wikipedia.org/wiki/Changelog), idealerweise generiert aus strukturierten Commits oder Release-Notizen, damit Konsumenten sehen können, was sich zwischen Versionen geändert hat. Diese zu automatisieren nimmt die verfallsanfälligste, von Hand gepflegte Dokumentation von Ihrem Teller und hält sie vertrauenswürdig.

### Architekturentscheidungen protokollieren

Erfassen Sie bedeutsame architektonische und Designentscheidungen als leichtgewichtige, datierte Protokolle, die den Kontext, die Entscheidung, und ihre Konsequenzen nennen. Diese Entscheidungsprotokolle bewahren die Begründung, die sonst verloren ginge, damit zukünftige Pflegende sehen können, warum das System so ist, wie es ist, statt es infrage zu stellen oder alte Fehler zu wiederholen. Sie zahlen sich besonders über die langen Lebensdauern von Unternehmens- und Behördensystemen aus.

### Dokumentationsverfall bewusst bekämpfen

Behandeln Sie veraltete Dokumentation als Fehler. Aktualisieren Sie die Dokumentation als Teil derselben Änderung, die Verhalten ändert, und machen Sie das zu einer Prüfungserwartung. Weisen Sie Eigentümerschaft zu, damit jedes wichtige Dokument jemanden Verantwortlichen hat. Überprüfen Sie hochwertige Dokumentation gelegentlich auf Genauigkeit, stutzen Sie, was veraltet ist, und entfernen oder kennzeichnen Sie klar alles, dem Sie nicht mehr vertrauen. Die Dokumentation, die am wenigsten verfällt, ist lebendige Dokumentation: generiert oder gegen das System selbst getestet.

### In Wissensmanagement und Auffindbarkeit investieren

Machen Sie Dokumentation auffindbar durch gute Suche, klare Navigation, und ein bekanntes Zuhause, damit Menschen finden können, was sie brauchen, ohne jemanden fragen zu müssen. Lassen Sie sie nicht über zu viele unverbundene Wikis und Werkzeuge zersplittern. Und erfassen Sie [stillschweigendes Wissen](https://en.wikipedia.org/wiki/Tacit_knowledge), das informelle Verständnis, das in Chat-Threads und Köpfen lebt, in dauerhafter, auffindbarer Form, bevor es entgleitet.

## Abwägungen: Vor- und Nachteile

| Ansatz | Vorteile | Nachteile |
|---|---|---|
| Docs-as-Code | Versioniert, prüfbar, nah am Code; geringer Verfall | Erfordert Ingenieursdisziplin; weniger freundlich für nicht-technische Autoren |
| Wiki/Wissensbasis | Leicht zu bearbeiten; für alle zugänglich | Driftet vom Code weg; zersplittert; verfällt still |
| Generierte Dokumentation (API, Änderungsprotokoll) | Immer genau; geringe Wartung | Beschränkt auf das, was die Quelle ausdrückt; braucht Werkzeug |
| Handgeschriebene Erklärung | Reicher Kontext und Begründung, die Maschinen nicht produzieren können | Arbeitsintensiv; anfällig für Veralten |
| Diátaxis-Struktur | Klarer Zweck pro Seite; leichter zu navigieren und pflegen | Vorabstrukturierungsaufwand; erfordert Autorendisziplin |

Die zentrale Abwägung ist Aufwand gegen Genauigkeit und Dauerhaftigkeit. Die günstigste Dokumentation zu schreiben, eine schnelle Wiki-Seite, ist auch die verfalls- und zersplitterungsanfälligste. Die dauerhafteste Dokumentation, generiert aus der Quelle oder wie Code geprüft, kostet mehr Vorabdisziplin, bleibt aber vertrauenswürdig. Eine gute Faustregel: Generieren Sie, was Sie können, halten Sie den Rest nah am Code und wie Code geprüft, und sparen Sie arbeitsintensive handgeschriebene Erklärung für die Begründung auf, die nur Menschen liefern können.

## Fragen zur Diskussion mit Ihrem Team

1. **Sind Ihre Dokumente nach Leserbedürfnis getrennt, oder vermischen sich Tutorials, Referenz, und Erklärung auf einer Seite?** Dieses Kapitel empfiehlt die Diátaxis-Aufteilung in Tutorials, Anleitungen, Referenz, und Erklärung, und listet das Mischen von Typen als Anti-Muster, das keiner Leserin gut dient. Im großen Maßstab brauchen eine Neuling, die das System lernt, und eine Bereitschaftsdienst-Ingenieurin, die eine präzise Tatsache sucht, verschiedene Seiten, und eine einzige gemischte Seite verlangsamt beide. Bringen Sie das Signal: Wählen Sie Ihre meistbesuchten Dokumente und prüfen Sie, ob jedes eine klare Aufgabe und ein klares Publikum hat. Strukturieren Sie die schlimmsten Übeltäter in eigenständige Typen um, damit jede Seite leichter zu schreiben, zu navigieren, und aktuell zu halten ist. Diese Struktur ist es, was Dokumentation wartbar hält, während die Organisation wächst.

2. **Erfassen Sie bedeutsame Architekturentscheidungen mit ihrer Begründung, oder nur den aktuellen Zustand?** Das Kapitel empfiehlt leichtgewichtige, datierte Entscheidungsprotokolle, die Kontext, Entscheidung, und Konsequenzen nennen, und stellt fest, dass sie sich am meisten über die langen Lebensdauern von Unternehmens- und Behördensystemen auszahlen. Ohne sie kann eine Pflegerin Jahre später nicht sehen, warum das System so ist, wie es ist, sie stellt also solide Wahlen infrage oder wiederholt alte Fehler. Bringen Sie eine jüngste schwierige Entscheidung, deren Begründung jetzt nur in einem Chat-Thread oder jemandes Erinnerung lebt, als konkretes Signal. Übernehmen Sie ein kurzes Entscheidungsprotokollformat und machen Sie das Schreiben eines Teils jeder bedeutsamen Designänderung. Die Begründung ist genau das Wissen, das nur Menschen liefern können und das am schnellsten verfällt, wenn ungeschrieben.

3. **Kann irgendeine Bereitschaftsdienst-Ingenieurin allein aus Ihren Runbooks auf einen Vorfall reagieren, ohne die Person zu alarmieren, die das System gebaut hat?** Dieses Kapitel benennt Runbooks als essentielles operatives Dokument, damit jeder im Bereitschaftsdienst handeln kann, nicht nur die Expertinnen, und beschreibt ein Behördenteam, das ein System nur erben konnte, weil Runbooks das Wissen über eine Vertragsgrenze trugen. Schlüsselpersonenrisiko ist das Versagen, gegen das dies schützt: Wenn die eine Expertin unerreichbar oder weg ist, verwandelt ein undokumentiertes Wiederherstellungsverfahren einen Routinevorfall in einen Ausfall. Bringen Sie die Belege: Nehmen Sie einen jüngsten Vorfall und prüfen Sie, ob das Runbook allein ihn gelöst hätte. Schreiben und testen Sie Runbooks für die Verfahren, die Menschen fürchten, und behandeln Sie ein Runbook, das nicht für sich stehen kann, als Fehler. Das ist der Unterschied zwischen einer 2-Uhr-morgens-Wiederherstellung und einer 2-Uhr-morgens-Eskalation.

4. **Welche Ihrer API-Referenzen und Änderungsprotokolle werden aus der Wahrheitsquelle generiert, und welche werden noch von Hand gepflegt und driften still?** Dieses Kapitel sagt Ihnen, Referenzdokumentation aus dem maschinenlesbaren Vertrag oder Code-Annotationen zu generieren, damit sie nicht von der tatsächlichen Schnittstelle abweichen kann, und listet das Handpflegen generierbaren Inhalts als Anti-Muster. Für ein großes Team ist eine handgeschriebene API-Dokumentation, die hinter der echten Schnittstelle zurückbleibt, schlimmer als keine: jede Konsumentin, die ihr vertraut, schreibt eine kaputte Integration, und der Fehler taucht weit weg von der veralteten Seite auf, die ihn verursachte. Bringen Sie das konkrete Signal: Nehmen Sie eine Stichprobe Ihrer meistgenutzten Schnittstellen und diffen Sie die veröffentlichte Referenz gegen den echten Vertrag, um zu sehen, wie weit jede gedriftet ist. Wo Sie Drift finden, verdrahten Sie die Referenz in den Build, damit sie bei jeder Änderung neu generiert wird, und mustern Sie die handgepflegte Kopie aus. In Unternehmens- und Behördenumgebungen, wo Schnittstellen über Teams, Zulieferer, und Vertragsgrenzen hinweg konsumiert werden, die Sie nie sehen, ist eine autoritative generierte Referenz oft das Einzige, was Integratoren davon abhält, gegen Fiktion zu bauen.

5. **Wer besitzt jedes hochwertige Dokument, und wie würden Sie heute bemerken, wenn eines veraltet wäre?** Das Kapitel behandelt veraltete Dokumentation als Fehler und warnt, dass unbesessene Dokumente verfallen, weil sie zu aktualisieren niemandes Aufgabe ist, während veraltete Dokumentation, als aktuell präsentiert, Vertrauen in all Ihre Dokumentation zerstört. Im großen Maßstab ist die Gefahr nicht eine einzige falsche Seite, sondern die langsame Erosion von Vertrauen: sobald Leserinnen einmal von veralteten Anweisungen verbrannt wurden, hören sie auf, dem ganzen Korpus zu vertrauen, und kehren zum Unterbrechen von Menschen zurück. Bringen Sie eine Eigentümerschaftskarte Ihrer kritischsten Dokumente und eine ehrliche Antwort darauf, wie Verfall erkannt wird, ob durch Überprüfungsrhythmus, Generierung, Tests gegen das System, oder reinen Zufall. Weisen Sie jedem wichtigen Dokument eine benannte Besitzerin zu, und bevorzugen Sie lebendige Dokumentation, die generiert oder getestet wird, damit sich Veralten mechanisch zeigt statt durch eine verlegene Leserin. Für Unternehmens- und Behördensysteme, die ihre ursprünglichen Teams überleben, ist unbesessene Dokumentation eine Verbindlichkeit, die Ihnen eine Prüferin oder ein erbender Zulieferer schließlich in Rechnung stellen wird.

6. **Wie auffindbar ist Ihre Dokumentation, und wie viel kritisches Wissen lebt noch nur in Chat-Threads und Köpfen?** Dieses Kapitel sagt, unauffindbares Wissen sei effektiv abwesend, warnt davor, Dokumentation über zu viele unverbundene Wikis und Werkzeuge zu zersplittern, und drängt Sie, stillschweigendes Wissen in dauerhafter, auffindbarer Form zu erfassen, bevor es entgleitet. In einer großen Organisation wird dieselbe Tatsache oft hundertmal neu entdeckt, neu gefragt, und neu beantwortet, weil niemand finden kann, wo sie bereits geschrieben wurde, und jeder Weggang nimmt unersetzlichen Kontext mit zur Tür hinaus. Bringen Sie die Belege: Zählen Sie, wie viele separate Dokumentationszuhause Sie pflegen, versuchen Sie, drei wichtige Tatsachen allein durch Suche zu finden, und notieren Sie, wo sich herausstellte, dass die echten Antworten in jemandes Erinnerung oder einer vergrabenen Nachricht lebten. Konsolidieren Sie zu einem bekannten Zuhause mit echter Suche und klarer Navigation, und machen Sie das Erfassen stillschweigenden Wissens zu einem routinemäßigen Teil der Arbeit statt einer heldenhaften Rettung. In öffentlichen und stark ausgelagerten Kontexten, wo Systeme vertraglich zwischen Zulieferern und Teams wandern, ist auffindbares schriftliches Wissen das Einzige, was die Übergabe überlebt.

## Branchenperspektive

**Startup.** Mit einer Handvoll Ingenieurinnen und keiner Reichweite zu verschwenden dokumentieren Sie nur, was ein 2-Uhr-morgens-Ausfall oder eine Neueinstellung tatsächlich bräuchte: eine echte README pro Dienst, ein getestetes Runbook für das Bereitstellen-und-Wiederherstellen-Verfahren, das alle fürchten, und ein paar datierte Notizen zu den Entscheidungen, die Sie sonst vergessen würden. Generieren Sie API-Dokumentation aus dem Vertrag, damit Sie sie nie von Hand pflegen. Widerstehen Sie dem Bau einer Dokumentationsplattform; ein versionierter Ordner mit Markup neben dem Code reicht, bis Sie echten Schmerz spüren.

**Kleinunternehmen.** Ohne technische Autorin und mit knappem Budget stützen Sie sich auf die Dokumentation, die Ihre Werkzeuge bereits generieren, und auf leichtgewichtiges Docs-as-Code statt eines besetzten Programms. Rahmen Sie die Wahl als Kaufen versus Bauen: Bevorzugen Sie Plattformen, die ihre eigene aktuelle Referenz und durchsuchbare Wissensbasis produzieren, gegenüber einem Wiki, das Sie von Hand pflegen müssen. Verbringen Sie Ihren knappen Aufwand auf die zwei oder drei Dokumente, deren Abwesenheit das Geschäft stoppen würde, und lassen Sie eine falsche oder fehlende Seite der Auslöser sein, Eigentümerschaft zu korrigieren.

**Großunternehmen.** Über viele Teams hinweg ist das Problem Konsistenz und Auffindbarkeit: eine gemeinsame Docs-as-Code-Pipeline, eine gemeinsame Struktur wie Diátaxis, generierte API-Referenzen und Änderungsprotokolle, und Entscheidungsprotokolle, überall gleich angewendet, damit Wissen nicht über Dutzende Wikis zersplittert. Weisen Sie jedem hochwertigen Dokument Eigentümerschaft zu und messen Sie Genauigkeit, nicht nur Präsenz. Behandeln Sie Architekturprotokolle, Runbooks, und Entscheidungsprotokolle als Prüfungsbeleg, und standardisieren Sie, wie sie produziert werden, damit eine Kontrollprüfung eine dokumentierte, begründbare Spur findet statt Hektik.

**Behörde.** Beschaffungsregeln und öffentliche Rechenschaftspflicht machen Dokumentation zu einem Liefergegenstand, keiner Höflichkeit. Schreiben Sie Architekturdokumentation, Runbooks, und Entscheidungsprotokolle als vorgeschriebene Artefakte in Verträge, geprüft auf Genauigkeit, damit Wissen einen Zulieferer-Übergang überlebt und ein System von wem auch immer es erbt betrieben werden kann. Verlangen Sie, dass jede autorisierte Betreiberin allein aus dem Runbook auf einen Vorfall reagieren kann, und halten Sie Entscheidungsprotokolle als transparentes öffentliches Protokoll dafür, warum Wahlen getroffen wurden. Dünne Dokumentation ist hier keine private Unannehmlichkeit; sie wird zu kostspieligem, vom Steuerzahler finanziertem Zurückentwickeln.

## Beispiele

**Startup.** Ein fünfköpfiges Startup schreibt eine echte README für jeden Dienst und ein kurzes Runbook für das eine Bereitstellen-und-Wiederherstellen-Verfahren, das alle fürchten, damit ein 2-Uhr-morgens-Ausfall nicht davon abhängt, den einen Gründer zu wecken, der das System kennt. Sie generieren API-Dokumentation aus dem Vertrag, statt sie von Hand zu schreiben, und notieren ein paar datierte Notizen, die erklären, warum sie ihre Datenbank und ihren Authentifizierungsansatz wählten. Es bleibt leichtgewichtig, aber es bedeutet, dass die sechste und siebte Neueinstellung sich aus Dokumenten einarbeiten statt jeden zu unterbrechen.

**Großunternehmen.** Ein großes Softwareunternehmen hält seine gesamte Dokumentation in denselben Repositorys wie seinen Code, geschrieben in Markup und in Pull-Requests geprüft, direkt neben den Änderungen, die sie beschreiben. API-Referenzen werden aus Dienstverträgen generiert, sodass sie nie driften. Änderungsprotokolle werden aus strukturierten Commits generiert, und Architekturentscheidungsprotokolle bewahren die Begründung hinter wichtigen Wahlen. Eine veröffentlichte Dokumentationsseite baut automatisch bei jeder Zusammenführung. Neue Ingenieurinnen werden schnell produktiv, weil Onboarding-Leitfäden und Runbooks aktuell und auffindbar sind, und Bereitschaftsdienst-Ingenieurinnen stützen sich auf Runbooks statt die ursprünglichen Autoren zu alarmieren.

**Behörde.** Eine nationale Behörde erbt ein System von einem scheidenden Auftragnehmer und verlässt sich vollständig auf Dokumentation, um Wissen über die Vertragsgrenze zu tragen. Weil der vorherige Zulieferer Architekturdokumentation, Runbooks, und Entscheidungsprotokolle als vorgeschriebene Liefergegenstände pflegte, kann das neue Team das System ohne die ursprünglichen Autoren betreiben und modifizieren. Wo Dokumentation dünn war, steht die Behörde vor kostspieligem Zurückentwickeln. Diese Erfahrung treibt eine neue Politik an: Dokumentation ist ein vertraglicher Liefergegenstand, geprüft auf Genauigkeit statt als nachträglicher Gedanke behandelt, und Runbooks müssen jeder autorisierten Betreiberin erlauben, auf Vorfälle zu reagieren.

## Geschäftsnutzen: Motivation, ROI und Gesamtbetriebskosten

Dokumentation zahlt sich in kürzerer Onboarding-Zeit, geringerem Schlüsselpersonenrisiko, schnellerer Vorfallreaktion, und niedrigeren Änderungskosten über die Lebensdauer eines Systems aus. Neue Ingenieurinnen, die in Tagen statt Wochen Produktivität erreichen, Bereitschaftsdienstpersonal, das Vorfälle aus einem Runbook löst statt zu eskalieren, Pflegende, die ein System Jahre nach seinem Bau selbstbewusst ändern: Das sind große, wiederkehrende Einsparungen, die sich über eine große Organisation und eine lange Systemlebensdauer summieren.

Was kostet Dokumentation? Verfassungs- und Wartungsaufwand. Was kostet es, *nicht* zu dokumentieren? Sie zahlen kontinuierlich: in langsamem Onboarding, wiederholten Fragen, Schlüsselpersonen-Engpässen, langsamerer Vorfallwiederherstellung, und im Extremfall Systemen, die niemand sicher ändern kann, teure Neuschreibungen oder Zurückentwickeln erzwingend. In Zulieferer-Übergangs- und Prüfungsszenarien kann fehlende Dokumentation direkte vertragliche und Compliance-Kosten tragen. Um Führungskräften den Fall darzulegen, setzen Sie Zahlen auf Onboarding-Zeit, Vorfallreaktionszeit, und wie viel kritisches Wissen in einzelnen Köpfen sitzt. Rahmen Sie dann Docs-as-Code und Generierung als Wege, dauerhafte Dokumentation ohne entsprechende Wartungslast zu bekommen. Und betonen Sie, dass ungenaue Dokumentation eine Verbindlichkeit ist, die Investition muss also einschließen, sie aktuell zu halten.

## Anti-Muster und Fallstricke

- **Veraltete Dokumentation, als aktuell präsentiert:** irreführt Leserinnen und zerstört Vertrauen in alle Dokumentation.
- **Das Einmal-Schreiben-Wiki:** Seiten, erstellt und nie aktualisiert, still von der Realität abdriftend.
- **Dokumentationszersplitterung:** Wissen verstreut über viele Werkzeuge und Wikis, sodass nichts gefunden werden kann.
- **Dokumentationstypen mischen:** Tutorials, Referenz, und Erklärung auf einer Seite durcheinandergewürfelt, keiner Leserin gut dienend.
- **Generierbaren Inhalt von Hand pflegen:** manuell geschriebene API-Dokumentation, die unweigerlich von der tatsächlichen Schnittstelle abweicht.
- **Stammeswissen:** kritisches Verständnis nur in Köpfen und Chat-Geschichte gehalten, verloren, wenn sie gehen.
- **Dokumentation als nachträglicher Gedanke:** am Ende geschrieben, wenn überhaupt, statt neben der Änderung.
- **Keine Eigentümerschaft:** Dokumente ohne verantwortliche Besitzerin verfallen, weil sie zu aktualisieren niemandes Aufgabe ist.

## Reifegradmodell

- **Stufe 1, Beginnen.** Dokumentation ist spärlich, verstreut, und veraltet, und Wissen lebt in Köpfen. Was existiert, wurde einmal geschrieben und nie wieder angefasst, sodass ein Ausfall oder ein Weggang Zurückentwickeln des Systems bedeutet.
- **Stufe 2, Entwickeln.** Schlüsseldokumente existieren, wie READMEs und ein paar Runbooks, aber sie werden uneinheitlich gepflegt und sind schwer zu finden. Manche Teams dokumentieren gut und andere kaum, und es gibt keine gemeinsame Erwartung darüber, was ein Repository tragen oder wo es leben sollte.
- **Stufe 3, Standardisieren.** Docs-as-Code ist die Norm über die Organisation: eine gemeinsame Struktur wie Diátaxis, generierte API-Referenzen und Änderungsprotokolle, Entscheidungsprotokolle, und eine Erwartung in der Prüfung, dass sich Dokumentation mit dem Code ändert, den sie beschreibt. Jedes hochwertige Dokument hat eine benannte Besitzerin, und es gibt ein bekanntes Zuhause mit echter Suche.
- **Stufe 4, Steuern.** Dokumentation wird gemessen, nicht nur präsent. Sie verfolgen Abdeckung der wesentlichen Dokumente, Dokumentänderungsrate gegen Codeänderungsrate, Onboarding-Zeit, Vorfalllösung allein aus Runbooks, und Aktualität gegen eine definierte Veraltungsschwelle, und Sie überprüfen diese Kennzahlen gegen Baselines. Verfall wird mechanisch erwischt durch Generierung, Tests gegen das System, und Link- und Genauigkeitsprüfungen, und veraltete Seiten werden aufgrund von Belegen markiert oder gestutzt statt durch Zufall.
- **Stufe 5, Orchestrieren.** Dokumentation wird kontinuierlich verbessert und über die Organisation integriert: lebendig, größtenteils generiert oder gegen das System getestet, besessen, auffindbar, und adaptiv. Kennzahlen speisen zurück, wo Sie investieren, stillschweigendes Wissen wird als Routineaufgabe erfasst, und der Korpus wird aktiv neu ausbalanciert und gestutzt, während sich Systeme, Teams, und Leserinnen ändern.

## Diskussionsideen

- Welche Dokumentation würde, wenn sie morgen verschwände, Ihrer Organisation am meisten schaden, und existiert sie derzeit und bleibt aktuell?
- Wie machen Sie das Aktualisieren von Dokumentation zu einem natürlichen Teil der Codeänderung statt einer separaten Pflichtaufgabe?
- Wo können Sie handgeschriebene Dokumentation durch generierte Dokumentation ersetzen, gebunden an die Wahrheitsquelle?
- Wie messen Sie, ob Ihre Dokumentation genau und genutzt ist, nicht nur präsent?
- Wie sollten KI-Assistenten ändern, wie Sie Dokumentation schreiben, pflegen, und durchsuchen, und wo könnten sie plausibel-aber-falschen Inhalt einführen?
- Wie erfassen Sie stillschweigendes Wissen, bevor die Menschen, die es halten, gehen?

## Wichtigste Erkenntnisse

- Behandeln Sie Dokumentation als Code: versioniert, geprüft, nah an der Quelle, und automatisch veröffentlicht.
- Strukturieren Sie Inhalt nach Leserbedürfnis mit Tutorials, Anleitungen, Referenz, und Erklärung.
- Pflegen Sie die hochwertigen Grundlagen: READMEs, Runbooks, Architekturdokumentation, Onboarding, und Entscheidungsprotokolle.
- Generieren Sie API-Dokumentation und Änderungsprotokolle, damit sie nicht von der Wahrheitsquelle abdriften können.
- Bekämpfen Sie Verfall mit Eigentümerschaft, Prüfungserwartungen, und Stutzen; ungenaue Dokumentation ist schlimmer als keine.

## Referenzen und weiterführende Literatur

- Daniele Procida, *Diátaxis*-Dokumentationsframework
- Andrew Etter, *Modern Technical Writing*
- Anne Gentle, *Docs Like Code*
- Google, *Developer Documentation Style Guide* und Season-of-Docs-Leitfaden (als Referenzbeispiele)
- Michael Nygard, *Documenting Architecture Decisions* (Architekturentscheidungsprotokolle)
- Andrew Hunt und David Thomas, *The Pragmatic Programmer* (zu Wissen und Dokumentation)
- *Keep a Changelog* (als Referenzkonvention)
