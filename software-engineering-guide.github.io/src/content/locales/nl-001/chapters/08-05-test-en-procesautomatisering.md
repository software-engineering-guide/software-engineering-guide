# 8.5 Test- en procesautomatisering

## Overzicht en motivatie

Test- en procesautomatisering is de praktijk van repetitief, handmatig engineering- en operationeel werk vervangen door betrouwbare, machinaal uitgevoerde workflows. Aan de testkant betekent dit [testautomatisering](https://en.wikipedia.org/wiki/Test_automation): geautomatiseerde testsuites die continu draaien om correctheid, prestaties en beveiliging te verifiëren. Aan de procesinkant strekt het zich uit tot de omringende machinerie van softwarelevering en -beheer: complianceonderbouwing verzamelen, operationele runbooks uitvoeren, bekende problemen herstellen en governance-, beveiligings- en kostenmaatregelen afdwingen. Het verenigende idee is eenvoudig. Alles wat herhaaldelijk en voorspelbaar wordt gedaan moet worden gecodeerd, zodat het consistent, snel en zonder menselijk sleurwerk draait.

Voor grote teams is automatisering de enige manier om kwaliteit en controle niet te laten instorten onder schaal. Handmatig testen kan niet bijbenen met honderden engineers die duizenden wijzigingen maken. Het wordt een knelpunt, en haar dekking wordt inconsistent en onbetrouwbaar. Handmatige operationele procedures lijden ook. Een service herstarten, een inloggegeven roteren en auditbewijs verzamelen worden allemaal traag en foutgevoelig wanneer vermoeide mensen ze onder druk over een groot landschap doen. Dit werk automatiseren maakt uitkomsten herhaalbaar. Het maakt ook bekwame engineers vrij voor de oordeelzware problemen die werkelijk menselijk inzicht nodig hebben.

In contexten van onderneming en overheid is automatisering ook de sleutel om compliance houdbaar te maken. Gereguleerde organisaties moeten continu aantonen dat maatregelen aanwezig zijn en bewijs wordt verzameld. Dit met de hand doen is duur, traag en gevoelig voor gaten. Het verzamelen van bewijs en afdwingen van maatregelen automatiseren verandert compliance van een periodieke brandoefening in een continue, verifieerbare eigenschap van het systeem. Deze "compliance as code"-aanpak vermindert zowel kosten als versterkt de zekerheid die auditors en toezichthouders vereisen.

## Kernprincipes

- Automatiseer werk dat herhaald, voorspelbaar en regelgebaseerd is. Bewaar menselijke inspanning voor oordeel.
- Maak geautomatiseerde tests snel, betrouwbaar en deterministisch, anders worden ze genegeerd.
- Draai tests parallel en verschuif ze eerder zodat feedback snel blijft naarmate de suite groeit.
- Codeer operationele procedures als [runbooks](https://en.wikipedia.org/wiki/Runbook)-as-code zodat ze geversioneerd, testbaar en uitvoerbaar zijn.
- Geef de voorkeur aan goed geïntegreerde automatisering boven brosse scripts die van buitenaf aan systemen worden vastgeschroefd.
- Genereer complianceonderbouwing automatisch als bijproduct van normale workflows.
- Houd een mens in de lus voor acties met hoog risico. Automatiseer eerst het veilige en routinematige.

## Aanbevelingen

### Bouw snelle, betrouwbare, parallelle testinfrastructuur

Een testsuite is alleen waardevol als engineers haar vertrouwen en ze snel feedback geeft. Investeer in testinfrastructuur die suites parallel over veel workers draait, zodat de totale kloktijd laag blijft ook als het aantal tests tot in de duizenden groeit. Structureer de suite als piramide: veel snelle [unittests](https://en.wikipedia.org/wiki/Unit_testing), minder integratietests en een klein aantal end-to-endtests. Dan komt de meeste feedback in seconden. Elimineer onbetrouwbare tests meedogenloos. Een intermitterend falende test is erger dan geen test, omdat ze engineers traint falen te negeren. Bied kortlevende, op aanvraag beschikbare testomgevingen zodat integratie- en end-to-endtests tegen realistische, geïsoleerde infrastructuur draaien.

### Automatiseer release, compliance en bewijsverzameling

Breid automatisering voorbij testen uit naar de release- en complianceworkflow. Laat de pijplijn automatisch de artefacten produceren die auditors nodig hebben: registraties van wie een wijziging goedkeurde, welke tests draaiden en slaagden, wat beveiligingsscans vonden en precies welk artefact werd gedeployd. Behandel maatregelen als code, zodat vereiste controles uniform worden afgedwongen en hun resultaten worden gelogd. Deze "compliance as code" verandert bewijs verzamelen van een handmatige haast voor een audit in een continu, altijd actueel overzicht. Het maakt de compliancehouding van het systeem ook op elk moment waarneembaar.

### Neem ChatOps en runbooks-as-code aan

Codeer operationele procedures als uitvoerbare runbooks in versiebeheer, in plaats van als proza-documenten die verouderen. Waar een procedure veilig en goed begrepen is, bedraad haar in automatisering die haar op aanvraag kan uitvoeren. ChatOps brengt deze operaties in een gedeelde chatinterface, zodat operators geautomatiseerde acties triggeren en observeren in een transparant, samenwerkend, gelogd gesprek. Dit maakt operaties zichtbaar voor het hele team en creëert een automatisch overzicht van wat is gedaan. Het verlaagt ook de drempel voor minder ervaren engineers om procedures veilig uit te voeren, omdat de automatisering de juiste stappen codeert.

### Implementeer geautomatiseerd herstel zorgvuldig

Bouw voor goed begrepen, terugkerende problemen geautomatiseerd herstel dat een toestand detecteert en een bekende oplossing toepast, zoals een mislukt proces herstarten, opschalen onder belasting, een volle schijf opruimen of een component failoveren. Begin met herstel met laag risico en hoge zekerheid. Eis menselijke bevestiging voor alles met aanzienlijke schadezone. Geautomatiseerd herstel verkort de gemiddelde hersteltijd en elimineert repetitieve alarmmoeheid. Maar het moet op degelijke detectie zijn gebouwd en waarborgen bevatten, want automatisering die op een vals signaal handelt kan een incident versterken. Log elke geautomatiseerde actie, zodat operators volledig zicht houden en kunnen ingrijpen.

### Plaats robotic process automation (RPA) correct

[Robotic process automation](https://en.wikipedia.org/wiki/Robotic_process_automation) bedient bestaande gebruikersinterfaces en applicaties om taken te automatiseren, de klikken en toetsaanslagen van een mens nabootsend. RPA heeft een legitieme plek als brug voor legacy- of derdensystemen die geen API blootstellen en op geen andere manier kunnen worden geïntegreerd. Gebruik haar pragmatisch voor zulke gevallen, maar ken haar grenzen. Op de UI gebaseerde automatisering is inherent broos: ze breekt wanneer de interface verandert, en ze pakt het onderliggende gebrek aan integratie niet aan. Geef waar een degelijke API of integratie beschikbaar is daaraan de voorkeur. Behandel RPA als tactische noodoplossing, niet als strategisch fundament, en plan haar te vervangen naarmate systemen moderniseren.

### Automatiseer governance-, beveiligings- en kostenmaatregelen

Codeer organisatiemaatregelen als geautomatiseerde controles die continu draaien: policy-as-code voor infrastructuurvangrails, geautomatiseerde beveiligingsscanning in pijplijnen en geautomatiseerde detectie van kostenanomalieën en ongebruikte bronnen. Governance automatiseren maakt maatregelen uniform en niet te omzeilen, en schaalt naar een volume aan wijziging dat handmatige review nooit kon dekken. Dezelfde aanpak die een beveiligingsbeleid afdwingt kan een op hol geslagen cloudrekening of een ontbrekende vereiste tag markeren. Governance verschuift van een periodieke handmatige audit naar een continue geautomatiseerde vangrail.

## Afwegingen: voor- en nadelen

| Keuze | Voordelen | Nadelen | Past het best bij |
|---|---|---|---|
| Brede geautomatiseerde tests | Snelle, consistente feedback. Maakt wijziging mogelijk | Bouw- en onderhoudskosten. Risico op onbetrouwbaarheid | Alle teams op schaal |
| Compliance as code | Continu, auditklaar bewijs | Engineering vooraf om maatregelen te coderen | Gereguleerde organisaties |
| Runbooks-as-code + ChatOps | Herhaalbare, zichtbare, gelogde operaties | Inspanning om te coderen en te onderhouden | Teams met echte ops-last |
| Geautomatiseerd herstel | Sneller herstel. Minder sleurwerk | Risico als detectie fout is | Goed begrepen terugkerende problemen |
| RPA (UI-automatisering) | Overbrugt systemen zonder API | Broos. Maskeert integratiegaten | Legacysystemen als noodoplossing |
| Geautomatiseerde governance | Uniforme, niet te omzeilen maatregelen | Inspanning voor beleid schrijven en afstemmen | Grote, bestuurde landschappen |

De centrale afweging is investering vooraf tegenover doorlopend sleurwerk en risico. Automatisering kost altijd inspanning om te bouwen en te onderhouden. Slecht gebouwde automatisering, of dat nu onbetrouwbare tests zijn, brosse RPA of herstel getriggerd door slechte signalen, kan erger zijn dan geen, omdat ze vertrouwen erodeert of falen versterkt. De discipline is drieledig: automatiseer het werkelijk herhaalbare en betrouwbare, investeer erin die automatisering betrouwbaar te maken en houd mensen in de lus waar oordeel of hoog risico dat eist. Goed gedaan betaalt automatisering zich vele malen terug. Onzorgvuldig gedaan wordt ze zelf een verplichting.

## Vragen om met je team te bespreken

1. **Draaien je integratie- en end-to-endtests tegen realistische, kortlevende omgevingen, of tegen een gedeelde stagingbak waar iedereen om vecht?** Geïsoleerde omgevingen op aanvraag per pull request laten integratie- en end-to-endtests realistische infrastructuur oefenen zonder dat teams elkaar blokkeren of gedeelde toestand vervuilen. Eén gedeelde stagingomgeving wordt een knelpunt en een bron van onbetrouwbare, volgordeafhankelijke falen naarmate meer teams erop zitten. Besluit of je kortlevende omgevingen kunt opzetten, wat ze kosten en welke tests ze werkelijk nodig hebben tegenover een snel in-geheugensubstituut. Neem data mee: hoe vaak staging wordt betwist, hoeveel falen terug te voeren zijn op interferentie in gedeelde omgevingen en de huidige kloktijd voor de integratielaag. Het antwoord bepaalt zowel je testbetrouwbaarheid als hoe snel de hogere lagen van de piramide feedback geven.

2. **Zijn operationele procedures gecodeerd als runbooks-as-code en aangeboden via ChatOps, of leven ze nog als proza dat veroudert?** Gecodeerde runbooks in versiebeheer zijn testbaar en uitvoerbaar, en ze via een gedeelde chatinterface draaien maakt elke actie zichtbaar en automatisch gelogd. Dat verlaagt de drempel voor een minder ervaren bereikbare engineer om veilig te handelen, omdat de automatisering de juiste stappen codeert in plaats van op stamkennis te leunen. Besluit welke procedures veilig en goed genoeg begrepen zijn om eerst te bedraden, en hoe je de mens in staat houdt in te grijpen. Voor een groot landschap dient deze transparantie ook als auditregistratie van wie wat wanneer deed. Neem je huidige runbooks mee, noteer welke verouderd zijn en identificeer de twee of drie meest uitgevoerde procedures om eerst te coderen.

3. **Welke beveiligingsscans en beleidscontroles blokkeren in je pijplijn een merge, en welke waarschuwen alleen?** Geautomatiseerde governance is alleen de moeite waard te bouwen als de maatregelen niet te omzeilen zijn, omdat een controle die alleen waarschuwt onder deadlinedruk wordt genegeerd net als een wikibeleid. Besluit, maatregel voor maatregel, wat blokkeert en wat waarschuwt: een kritieke kwetsbaarheid of een ontbrekende versleutelingstag blokkeert waarschijnlijk, terwijl een bevinding van lage ernst over stijl kan waarschuwen. Op schaal is dit hoe je beveiligings- en kostenvangrails uniform afdwingt over een volume wijziging dat geen handmatige review kan dekken. Neem je huidige controle-inventaris mee en markeer elke als blokkerend of adviserend, bespreek dan het percentage valse positieven, want een luidruchtige blokkerende controle traint mensen uitzonderingen te eisen. De lijn tussen blokkeren en waarschuwen is waar je governance tanden heeft of niet.

4. **Welke geautomatiseerde herstelacties zijn we bereid zonder menselijke bevestiging te laten handelen, en wat is de schadezone als de detectie fout is?** Geautomatiseerd herstel verkort de hersteltijd en alarmmoeheid, maar een reparatie getriggerd door een vals signaal kan een kleine hapering in een volledige uitval veranderen, dus de beslissing wat onbeheerd draait is een risicobeslissing, geen gemak. Weeg de concurrerende trekken: onbeheerde actie is het snelst maar het riskantst, terwijl bevestiging door een mens in de lus veiliger is maar de vertraging en het sleurwerk herintroduceert die je wilde wegnemen. Neem de kandidaatherstelacties mee gerangschikt naar frequentie en naar schadezone in het slechtste geval, het historische percentage valse positieven van de detectie erachter en of elke actie gelogd en omkeerbaar is. Voeg voor een groot landschap van onderneming of overheid een formeel wijzigingsgezag en rollbackplan toe voor alles wat productiedata of burgergerichte diensten raakt, want een autoherstel dat niet kan worden geaudit of ongedaan gemaakt is er een dat een toezichthouder je zal dwingen uit te zetten.

5. **Hoe financieren en wijzen we eigenaarschap toe voor het onderhouden van onze automatisering zodat ze niet verwordt tot een verplichting?** Tests, runbooks, beleidscontroles en RPA-bots verrotten allemaal naarmate de systemen eromheen veranderen, en verwaarloosde automatisering is erger dan geen: een verouderd runbook geeft valse zekerheid in een crisis en een kapotte RPA-bot laat stilletjes werk vallen. De spanning is dat onderhoud met functiewerk om dezelfde engineers strijdt en onzichtbaar is tot iets breekt, dus het is het eerste dat onder deadlinedruk wordt geschrapt. Neem de huidige inventaris van automatiseringsbezittingen mee, de achterstand aan onbetrouwbare tests en kapotte bots en een eerlijke schatting van de engineeruren die al naar onderhoud gaan tegenover wat is begroot. Noem in een omgeving van onderneming of overheid de verantwoordelijke eigenaar voor elke kritieke automatisering en financier haar onderhoud als expliciete post, want auditors en incidentreviews zullen vragen wie verantwoordelijk was toen een onderhouden maatregel stilletjes faalde.

6. **Wat is voor elk legacysysteem dat we met RPA automatiseren het concrete plan en de trigger om die RPA te vervangen door een echte integratie?** RPA is een legitieme brug voor systemen die geen API blootstellen, maar een brug zonder uitgangsplan verhardt stilletjes tot permanente, brosse infrastructuur die bij elke UI-wijziging breekt en het integratiegat verankert dat ze moest overbruggen. De afweging is echt: RPA levert nu snel en goedkoop waarde, terwijl een degelijke API-integratie vooraf meer kost maar duurzaam is, dus de discipline is RPA te behandelen als een gedateerde lening, geen aankoop. Neem de lijst RPA-bots in productie mee, de systemen waarvan elk afhangt, hoe vaak elk breekt en of een moderniserings- of integratie-inspanning voor het onderliggende systeem werkelijk gefinancierd en ingepland is. Koppel voor landschappen van onderneming en overheid met decennia oude kernapplicaties elke RPA-bot aan een benoemde moderniseringsmijlpaal, want RPA die stilletjes kritiek is geworden zonder vervangingsdatum is technische schuld die elk jaar oploopt dat de interface die ze schraapt blijft veranderen.

## Sectorperspectief

**Startup.** Met twee of drie engineers en geen tijd om infrastructuur te bouwen houd je een kleine, snelle testpiramide die bij elke wijziging in een paar minuten draait, en behandel je elke onbetrouwbare test als echte bug om die week te repareren of te verwijderen. Sla zware compliancetooling en policy-as-code over die je nog niet nodig hebt, en codeer alleen je twee of drie meest uitgevoerde operationele reparaties als eenvoudige scripts getriggerd vanuit chat. Automatiseer wat dagelijks sleurwerk wegneemt en weersta governancemachinerie bouwen voordat je een governanceprobleem hebt.

**Kleinbedrijf.** Zonder aparte test- of platformspecialist leun je op automatisering ingebakken in tools die je al betaalt: de ingebouwde testrunners van de CI-dienst, haar scanning-add-ons en beheerde omgevingen in plaats van een maatwerktestinfrastructuur te bouwen. Formuleer de keuze tussen kopen en bouwen rond onderhoud dat je realistisch kunt volhouden, want een slimme maatwerkpijplijn die niemand kan onderhouden is een slechtere uitkomst dan een eenvoudiger gehoste. Gebruik RPA spaarzaam en alleen waar een leveranciertool een systeem overbrugt dat je op geen andere manier kunt integreren.

**Grote onderneming.** Over veel teams is het doel uniforme, niet te omzeilen maatregelen op een schaal die handmatige review niet kan dekken: gedeelde parallelle testinfrastructuur met kortlevende omgevingen, policy-as-code-vangrails en complianceonderbouwing automatisch gegenereerd uit elke pijplijnrun. Standaardiseer de interfaces zodat teams herstel- en runbooktooling hergebruiken in plaats van elk brosse scripts opnieuw uit te vinden, en beheer automatisering als bezeten, gefinancierd portfolio met heldere onderhoudsbudgetten. Let erop dat een controle die in het ene team slechts waarschuwt in een ander niet als blokkerend wordt behandeld, want inconsistente afdwinging ondermijnt de zekerheid waarvoor je betaalt.

**Overheid.** Aanbestedingsregels, transparantieplichten en mandaten voor continue bewaking maken compliance as code bijna essentieel: elke pijplijnrun moet de gecontroleerde maatregelen, uitgevoerde scans en verleende goedkeuringen vastleggen als sabotagebestendig, auditklaar bewijs. Geef de voorkeur aan open, overdraagbare automatisering boven bedrijfseigen lock-in zodat een toekomstig contract naar een andere leverancier kan verhuizen, en houd een mens verantwoordelijk voor elk herstel dat burgergerichte diensten raakt. Waar een decennia oud systeem RPA afdwingt, documenteer haar als bewuste, tijdelijke brug met een publiek moderniseringsplan, en houd governancecontroles bij elke wijziging aan de verplichte beveiligingsbasis.

## Voorbeelden

**Startup.** Een startup van zeven personen houdt een slanke testpiramide van vooral snelle unittests plus een paar integratietests, allemaal parallel draaiend zodat de volledige suite bij elke pull request in minder dan drie minuten klaar is. Wanneer een test begint te flaken, behandelen ze het als echte bug en repareren of verwijderen ze haar die week, omdat met zo'n klein team één genegeerde rode build het vertrouwen in de hele suite zou eroderen. Ze coderen ook hun twee meest gangbare operationele reparaties, een vastgelopen worker herstarten en een volle schijf opruimen, als kleine scripts getriggerd vanuit Slack, zodat wie bereikbaar is ze veilig kan draaien zonder de ene engineer op te roepen die ze schreef.

**Grote onderneming.** Een groot e-commercebedrijf draait een testsuite van tienduizenden tests, geparalleliseerd over een vloot workers zodat de volledige suite in minuten klaar is. Kortlevende omgevingen worden per pull request opgezet voor realistisch integratietesten. Operaties lopen via ChatOps: bereikbare engineers triggeren gecodeerde runbooks vanuit chat, en gangbare falen zoals een overbelaste service worden automatisch hersteld, met de actie gelogd voor review. De pijplijn verzamelt beveiligingsscan- en goedkeuringsbewijs automatisch, zodat de jaarlijkse audit put uit een altijd actueel overzicht in plaats van een handmatige bewijsjacht.

**Overheid.** Een publieke instantie onderworpen aan strikte eisen voor continue bewaking implementeert compliance as code. Elke pijplijnrun legt de gecontroleerde maatregelen, de uitgevoerde scans en de verleende goedkeuringen vast, wat sabotagebestendig bewijs produceert dat auditors op aanvraag tevredenstelt. Omdat een van haar kernsystemen een decennia oude applicatie zonder API is, gebruikt de instantie RPA als bewuste brug om data-invoer ernaartoe te automatiseren terwijl een moderniseringsinspanning vordert, met een expliciet plan om de RPA te vervangen zodra een degelijke integratie bestaat. Geautomatiseerde governancecontroles dwingen de verplichte beveiligingsbasis af bij elke infrastructuurwijziging.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Het ROI van test- en procesautomatisering toont zich als teruggewonnen engineeringtijd, snellere en veiligere oplevering, sneller incidentherstel en dramatisch lagere compliancekosten. Geautomatiseerd testen maakt de snelle, zelfverzekerde wijziging mogelijk die leveringsprestaties onderbouwt. Geautomatiseerde operaties en herstel snijden het sleurwerk en de downtime weg die teams en budgetten uitputten. Compliance as code kan een audit van weken handmatige voorbereiding omzetten in een routinequery, een besparing die zowel financieel als reputationeel is.

De TCO-vergelijking weegt de echte, doorlopende kosten van automatisering bouwen en onderhouden af tegen de kosten van niet automatiseren. Handmatig testen en operaties kosten niet slechts de bestede uren. Ze kosten ook de defecten die ontsnappen, de incidenten die lang duren, de audits die specialistisch personeel verbruiken en de burn-out van engineers die repetitief sleurwerk doen. Voor leiderschap is het argument eenvoudig: automatisering zet terugkerende operationele uitgaven en risico om in een investering van eenmalig-plus-onderhoud die schaalt, en maakt kwaliteit en compliance continu in plaats van episodisch. Eén kanttekening is het eerlijk noemen waard. Automatisering moet worden onderhouden en vertrouwd. Ongefinancierde, verwaarloosde automatisering verwordt tot een verplichting.

## Antipatronen en valkuilen

- **Getolereerde onbetrouwbare tests.** Intermitterende falen vernietigen vertrouwen en trainen engineers rode resultaten te negeren.
- **Een kapot proces automatiseren.** Een slechte workflow automatiseren laat de rommel alleen sneller gebeuren. Repareer eerst het proces.
- **RPA als strategie.** Op brosse UI-automatisering leunen als permanente oplossing maskeert en verankert integratiegaten.
- **Herstel zonder degelijke detectie.** Geautomatiseerde reparaties getriggerd door slechte signalen kunnen een incident versterken.
- **Runbooks als verouderd proza.** Procedures die in verouderde documenten leven geven valse zekerheid in een crisis.
- **Complianceonderbouwing handmatig verzameld.** Periodieke handmatige bewijsjachten zijn duur en laten gaten tussen audits.
- **Geen mens in de lus voor acties met hoog risico.** Gevaarlijke operaties volledig automatiseren neemt het oordeel weg dat rampen voorkomt.

## Volwassenheidsmodel

**Niveau 1, Initiëren.** Testen en operaties zijn grotendeels handmatig en reactief. Dekking is ad hoc, procedures leven in hoofden van mensen of verouderde documenten, herstel gebeurt met de hand tijdens incidenten en complianceonderbouwing wordt in een haast samengesteld vóór elke audit.

**Niveau 2, Ontwikkelen.** Geautomatiseerde tests bestaan maar zijn traag, onbetrouwbaar of draaien inconsistent, en praktijken verschillen sterk tussen teams. Enkele operationele scripts en runbooks bestaan in zakken, maar herstel is nog handmatig en governance wordt afgedwongen door periodieke review in plaats van continue controles.

**Niveau 3, Standaardiseren.** Snelle, parallelle, betrouwbare testinfrastructuur is de gedocumenteerde organisatiebrede standaard. Runbooks-as-code en ChatOps zijn in algemeen gebruik, complianceonderbouwing wordt automatisch gegenereerd uit pijplijnruns en governancemaatregelen draaien als afgedwongen geautomatiseerde controles consistent toegepast over teams.

**Niveau 4, Beheersen.** De automatisering zelf wordt gemeten en beheerst aan de hand van uitgangswaarden. Je volgt het percentage onbetrouwbare tests, de kloktijd van de suite, de gemiddelde hersteltijd voor automatisch herstelde incidenten, het aandeel maatregelen met geautomatiseerd bewijs en percentages valse positieven op blokkerende controles, en je houdt elke statistiek aan een afgesproken doel. Herstel- en dekkingsbeslissingen worden door deze data gedreven, en elke geautomatiseerde actie wordt gelogd zodat trends en regressies zichtbaar zijn in plaats van geraden.

**Niveau 5, Orkestreren.** Automatisering wordt continu verbeterd en over de organisatie geïntegreerd. Geautomatiseerd herstel handelt routine-incidenten af met bewezen waarborgen, compliance is continu en altijd auditklaar, en de test-, ops- en governancetoolchains passen zich aan naarmate systemen veranderen, met RPA-bruggen actief afgeschaft naarmate integraties rijpen. Mensen richten zich op oordeel terwijl machines het herhaalbare afhandelen, en het hele systeem herbalanceert op bewijs.

## Ideeën voor discussie

- Welke operationele procedures zijn veilig om volledig te automatiseren, en welke moeten een mens in de lus houden?
- Hoe houd je een grote testsuite snel en vrij van onbetrouwbare tests naarmate ze groeit?
- Waar is RPA een gerechtvaardigde brug voor je legacysystemen, en wat is het plan om haar af te schaffen?
- Welke maatregelen zou je het eerst van handmatige audit naar continue compliance as code kunnen omzetten?
- Hoe bouw je vertrouwen in geautomatiseerd herstel zonder versterkte incidenten te riskeren?
- Hoe financier je het doorlopende onderhoud dat automatisering vereist zodat ze niet verwordt tot een verplichting?

## Belangrijkste inzichten

- Automatiseer het herhaalde, voorspelbare en regelgebaseerde. Bewaar menselijke inspanning voor oordeel en beslissingen met hoog risico.
- Maak geautomatiseerde tests snel, parallel en betrouwbaar, en elimineer onbetrouwbaarheid meedogenloos.
- Codeer operaties als runbooks-as-code en bied ze aan via ChatOps voor zichtbaarheid en registratie.
- Genereer complianceonderbouwing automatisch zodat audits putten uit een continu, actueel overzicht.
- Gebruik RPA alleen als bewuste, tijdelijke brug voor systemen zonder API, en plan haar afschaffing.
- Dwing governance-, beveiligings- en kostenmaatregelen af als continue geautomatiseerde controles, met mensen die toezien op de riskante acties.

## Referenties en verder lezen

- Lisa Crispin and Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*.
- Jez Humble and David Farley, *Continuous Delivery*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering* (see the chapter on eliminating toil).
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate*.
- NIST Special Publication 800-53 and 800-137 (continuous monitoring).
- Open Policy Agent documentation (policy as code).
