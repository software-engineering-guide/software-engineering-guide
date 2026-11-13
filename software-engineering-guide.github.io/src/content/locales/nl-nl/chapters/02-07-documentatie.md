# 2.7 Documentatie

## Overzicht en motivatie

[Documentatie](https://en.wikipedia.org/wiki/Software_documentation) is de schriftelijke kennis waarmee mensen software kunnen gebruiken, beheren en wijzigen zonder begrip uit de code alleen te hoeven puzzelen. Ze komt in veel genres: hoe je begint, hoe je een taak volbrengt, hoe een systeem is gestructureerd, hoe je op een incident reageert, wat een [API](https://en.wikipedia.org/wiki/API) accepteert en teruggeeft. Elk dient een andere lezer met een andere behoefte. Goede documentatie is niet optioneel. Het is het verschil tussen kennis die schaalt over een grote organisatie en kennis die in de hoofden van een paar mensen leeft.

Voor grote teams is documentatie je beste verdediging tegen sleutelpersoonrisico (het gevaar dat kritieke kennis bij slechts één of enkele mensen zit) en je snelste manier om nieuwkomers in te werken. Wanneer honderden engineers afhangen van systemen die ze niet bouwden, en mensen voortdurend komen, verhuizen en vertrekken, kan de organisatie alleen functioneren als kennis is opgeschreven en makkelijk te vinden is. Ongedocumenteerde systemen worden fragiel: alleen hun auteurs kunnen ze veilig wijzigen, en wanneer die auteurs vertrekken, verliest de organisatie het vermogen haar eigen software te onderhouden. Dat is een van de meest voorkomende en dure falen op schaal.

Omgevingen van onderneming en overheid verhogen de inzet verder. Systemen leven lang, dus je documentatie moet onderhouders jaren, zelfs decennia na het vertrek van het oorspronkelijke team dienen. Regelgevings- en auditregimes eisen vaak specifieke documenten als bewijs van beheersing: architectuurregisters, [runbooks](https://en.wikipedia.org/wiki/Runbook) (stapsgewijze operationele en incidentresponsprocedures) en besluitenlogboeken. Publieke systemen die tussen leveranciers worden overgedragen, leunen volledig op documentatie om kennis over contractgrenzen te dragen. En toch is documentatie berucht gevoelig voor verrotting, dus de echte uitdaging is haar accuraat te houden naarmate de software verandert.

## Kernprincipes

- Schrijf voor een specifieke lezer met een specifieke behoefte. Verschillende soorten documentatie dienen verschillende doelen.
- Houd documentatie dicht bij de code en behandel haar als code (docs-as-code).
- Nauwkeurigheid wint van volledigheid. Een kleine hoeveelheid betrouwbare documentatie wint van een grote hoeveelheid die fout is.
- Genereer wat gegenereerd kan worden. Onderhoud niet met de hand wat een tool uit de bron van waarheid kan produceren.
- Bestrijd documentatieverrotting actief. Verouderde documentatie is erger dan geen omdat ze misleidt.
- Maak documentatie vindbaar. Onvindbare kennis is in feite afwezig.
- Leg beslissingen en hun motivering vast, niet alleen de huidige toestand.

## Aanbevelingen

### Neem docs-as-code aan

Houd documentatie in [versiebeheer](https://en.wikipedia.org/wiki/Version_control) direct naast de code die ze beschrijft, schrijf haar in platte-tekstopmaak en beoordeel haar via hetzelfde pull-requestproces. Zo blijft ze geversioneerd, beoordeelbaar en dicht bij de code, zodat je beide samen kunt bijwerken. Publiceer haar via een geautomatiseerde pipeline zodat de nieuwste versie altijd beschikbaar is. Documentatie als code behandelen brengt dezelfde discipline die code betrouwbaar houdt: review, geschiedenis en automatisering.

### Structureer inhoud met het Diátaxis-raamwerk

Organiseer documentatie in vier verschillende typen, omdat ze mengen geen lezer goed dient: tutorials (leergericht, voor nieuwkomers), how-to-gidsen (taakgericht, voor een specifiek doel), referentie (informatiegericht, nauwkeurig en compleet) en uitleg (begripsgericht, het waarom en de context). Houd deze gescheiden en alles wordt makkelijker te schrijven, te navigeren en te onderhouden, omdat elke pagina één duidelijke taak en één duidelijk publiek heeft.

### Onderhoud de essentiële operationele documenten

Geef elke repository een duidelijke [README](https://en.wikipedia.org/wiki/README) als voordeur: wat het is, hoe je het bouwt en draait en waar je daarna heen moet. Schrijf runbooks voor operationele taken en incidentrespons, zodat iedereen die bereikbaarheidsdienst heeft kan handelen, niet alleen de experts. Houd architectuurdocumentatie bij die de structuur en sleutelcomponenten van het systeem uitlegt. En bied onboardingdocumentatie die een nieuwe engineer snel productief maakt. Dit zijn de documenten die je het meest mist wanneer ze er niet zijn.

### Genereer API-documentatie en changelogs uit de bron van waarheid

Genereer je API-referentiedocumentatie uit het machineleesbare contract of de code-annotaties, zodat ze niet kan afdrijven van de werkelijke interface. Houd een [changelog](https://en.wikipedia.org/wiki/Changelog) bij, bij voorkeur gegenereerd uit gestructureerde commits of releasenotities, zodat afnemers kunnen zien wat er tussen versies veranderde. Deze automatiseren haalt de meest verrottingsgevoelige met de hand onderhouden documentatie van je bord en houdt haar betrouwbaar.

### Leg architectuurbeslissingen vast

Leg belangrijke architectuur- en ontwerpbeslissingen vast als lichte, gedateerde registers die de context, de beslissing en de gevolgen benoemen. Deze besluitenlogboeken bewaren de motivering die anders verloren zou gaan, zodat toekomstige onderhouders kunnen zien waarom het systeem is zoals het is in plaats van het in twijfel te trekken of oude fouten te herhalen. Ze betalen zich vooral uit over de lange levensduur van systemen van ondernemingen en overheden.

### Bestrijd documentatieverrotting bewust

Behandel verouderde documentatie als defect. Werk de documentatie bij als onderdeel van dezelfde wijziging die gedrag verandert, en maak dat een reviewverwachting. Wijs eigenaarschap toe zodat elk belangrijk document iemand heeft die er verantwoordelijk voor is. Beoordeel waardevolle documentatie af en toe op nauwkeurigheid, snoei wat verouderd is en verwijder of markeer duidelijk alles wat je niet meer vertrouwt. De documentatie die het minst verrot is levende documentatie: gegenereerd of getest tegen het systeem zelf.

### Investeer in kennisbeheer en vindbaarheid

Maak documentatie vindbaar via goede zoekfunctie, heldere navigatie en een bekend thuis, zodat mensen kunnen vinden wat ze nodig hebben zonder iemand te hoeven vragen. Laat haar niet versplinteren over te veel losstaande wiki's en tools. En leg [impliciete kennis](https://en.wikipedia.org/wiki/Tacit_knowledge) vast, het informele begrip dat in chatthreads en hoofden van mensen leeft, in duurzame, vindbare vorm voordat die wegglipt.

## Afwegingen: voor- en nadelen

| Aanpak | Voordelen | Nadelen |
|---|---|---|
| Docs-as-code | Geversioneerd, beoordeelbaar, dicht bij de code. Weinig verrotting | Vraagt discipline van engineers. Minder vriendelijk voor niet-technische auteurs |
| Wiki / kennisbank | Makkelijk te bewerken. Toegankelijk voor iedereen | Drijft weg van de code. Versplintert. Verrot stilletjes |
| Gegenereerde documentatie (API, changelog) | Altijd nauwkeurig. Weinig onderhoud | Beperkt tot wat de bron uitdrukt. Vraagt tooling |
| Met de hand geschreven uitleg | Rijke context en motivering die machines niet kunnen produceren | Arbeidsintensief. Gevoelig voor veroudering |
| Diátaxis-structuur | Duidelijk doel per pagina. Makkelijker te navigeren en te onderhouden | Structureringsinspanning vooraf. Vraagt discipline van auteurs |

De centrale afweging is inspanning tegenover nauwkeurigheid en duurzaamheid. De goedkoopste documentatie om te schrijven, een snelle wikipagina, is ook de meest verrottingsgevoelige en versplinterende. De duurzaamste documentatie, gegenereerd uit de bron of beoordeeld als code, kost vooraf meer discipline maar blijft betrouwbaar. Een goede vuistregel: genereer wat je kunt, houd de rest dicht bij de code en beoordeeld als code, en bewaar arbeidsintensieve met de hand geschreven uitleg voor de motivering die alleen mensen kunnen geven.

## Vragen om met je team te bespreken

1. **Zijn je documenten gescheiden naar behoefte van de lezer, of lopen tutorials, referentie en uitleg door elkaar op één pagina?** Dit hoofdstuk beveelt de Diátaxis-splitsing aan in tutorials, how-to-gidsen, referentie en uitleg, en noemt het mengen van typen een antipatroon dat geen lezer goed dient. Op schaal hebben een nieuwkomer die het systeem leert en een engineer met bereikbaarheidsdienst die een precies feit zoekt verschillende pagina's nodig, en een enkele gemengde pagina vertraagt beide. Neem het signaal mee: kies je meest bezochte documenten en controleer of elk één duidelijke taak en één duidelijk publiek heeft. Herstructureer de ergste overtreders in aparte typen, zodat elke pagina makkelijker te schrijven, te navigeren en actueel te houden is. Die structuur is wat documentatie onderhoudbaar maakt naarmate de organisatie groeit.

2. **Leg je belangrijke architectuurbeslissingen vast met hun motivering, of alleen de huidige toestand?** Het hoofdstuk beveelt lichte, gedateerde besluitenlogboeken aan die context, beslissing en gevolgen benoemen, en merkt op dat ze zich het meest uitbetalen over de lange levensduur van systemen van ondernemingen en overheden. Zonder ze kan een onderhouder jaren later niet zien waarom het systeem is zoals het is, dus ze trekken gezonde keuzes in twijfel of herhalen oude fouten. Neem een recente moeilijke beslissing mee waarvan de redenering nu alleen in een chatthread of het geheugen van iemand leeft als concreet signaal. Neem een kort formaat voor besluitenlogboeken aan en maak het schrijven van een logboek deel van elke belangrijke ontwerpwijziging. De motivering is precies de kennis die alleen mensen kunnen geven en die het snelst verrot wanneer ze niet is opgeschreven.

3. **Kan elke engineer met bereikbaarheidsdienst op een incident reageren vanuit je runbooks alleen, zonder de persoon op te pagen die het systeem bouwde?** Dit hoofdstuk noemt runbooks een essentieel operationeel document zodat iedereen met bereikbaarheidsdienst kan handelen, niet alleen de experts, en beschrijft een overheidsteam dat een systeem alleen kon erven omdat runbooks de kennis over een contractgrens droegen. Sleutelpersoonrisico is het falen waartegen dit beschermt: wanneer de ene expert onbereikbaar of weg is, verandert een ongedocumenteerde herstelprocedure een routine-incident in een storing. Neem het bewijs mee: neem een recent incident en controleer of het runbook alleen het had opgelost. Schrijf en test runbooks voor de procedures waar mensen tegenop zien, en behandel een runbook dat niet op zichzelf kan staan als defect. Dat is het verschil tussen een herstel om 2 uur 's nachts en een escalatie om 2 uur 's nachts.

4. **Welke van je API-referenties en changelogs worden gegenereerd uit de bron van waarheid, en welke worden nog met de hand onderhouden en driften stilletjes weg?** Dit hoofdstuk zegt je referentiedocumentatie te genereren uit het machineleesbare contract of code-annotaties, zodat ze niet kan afwijken van de werkelijke interface, en noemt het met de hand onderhouden van genereerbare inhoud een antipatroon. Voor een groot team is een met de hand geschreven API-document dat achterloopt op de echte interface erger dan geen: elke afnemer die erop vertrouwt schrijft een kapotte integratie, en het falen verschijnt ver van de verouderde pagina die het veroorzaakte. Neem het concrete signaal mee: neem een handvol van je meest gebruikte interfaces en vergelijk de gepubliceerde referentie met het echte contract om te zien hoe ver elk is afgedreven. Waar je afdrijving vindt, koppel je de referentie aan de build zodat ze bij elke wijziging opnieuw wordt gegenereerd, en pensioneer je de met de hand bijgehouden kopie. In omgevingen van onderneming en overheid, waar interfaces worden gebruikt over teams, leveranciers en contractgrenzen die je nooit ziet, is een gezaghebbende gegenereerde referentie vaak het enige wat integrators ervan weerhoudt tegen fictie te bouwen.

5. **Wie bezit elk waardevol document, en hoe zou je vandaag merken dat er een verouderd was geraakt?** Het hoofdstuk behandelt verouderde documentatie als defect en waarschuwt dat documenten zonder eigenaar verrotten omdat het bijwerken niemands taak is, terwijl verouderde documentatie die als actueel wordt gepresenteerd het vertrouwen in al je documentatie vernietigt. Op schaal is het gevaar niet één foute pagina maar de langzame erosie van vertrouwen: zodra lezers zijn gebrand door verouderde instructies, houden ze op het hele corpus te vertrouwen en gaan ze terug naar het onderbreken van mensen. Neem een eigenaarschapskaart van je meest kritieke documenten mee en een eerlijk antwoord op hoe verrotting wordt gedetecteerd, door beoordelingscadans, generatie, tests tegen het systeem of puur geluk. Wijs een benoemde eigenaar toe aan elk document dat ertoe doet, en geef de voorkeur aan levende documentatie die wordt gegenereerd of getest zodat veroudering mechanisch zichtbaar wordt in plaats van via een beschaamde lezer. Voor systemen van ondernemingen en overheden die hun oorspronkelijke teams overleven is documentatie zonder eigenaar een verplichting waarvoor een auditor of een erfgenamende leverancier je uiteindelijk zal belasten.

6. **Hoe vindbaar is je documentatie, en hoeveel kritieke kennis leeft nog alleen in chatthreads en hoofden van mensen?** Dit hoofdstuk zegt dat onvindbare kennis in feite afwezig is, waarschuwt tegen het versplinteren van documenten over te veel losstaande wiki's en tools en dringt erop aan impliciete kennis vast te leggen in duurzame, vindbare vorm voordat die wegglipt. In een grote organisatie wordt hetzelfde feit honderden keren herontdekt, opnieuw gevraagd en opnieuw beantwoord omdat niemand kan vinden waar het al was opgeschreven, en elk vertrek neemt onvervangbare context de deur uit. Neem het bewijs mee: tel hoeveel aparte documentatiebakens je onderhoudt, probeer drie belangrijke feiten alleen via zoeken te vinden en let op waar de echte antwoorden bleken te leven in iemands geheugen of een begraven bericht. Consolideer naar een bekend thuis met echte zoekfunctie en heldere navigatie, en maak het vastleggen van impliciete kennis een routinematig onderdeel van het werk in plaats van een heldhaftige redding. In publieke en sterk uitbestede contexten, waar systemen via contract tussen leveranciers en teams worden overgedragen, is vindbare geschreven kennis het enige wat de overdracht overleeft.

## Sectorperspectief

**Startup.** Met een handvol engineers en geen runway te verspillen documenteer je alleen wat een storing om 2 uur 's nachts of een nieuwe aanwerving werkelijk nodig zou hebben: een echte README per service, één geteste runbook voor de deploy-en-herstelprocedure waar iedereen tegenop ziet en een paar gedateerde notities over de beslissingen die je anders zou vergeten. Genereer API-documentatie uit het contract zodat je haar nooit met de hand onderhoudt. Weersta het bouwen van een documentatieplatform. Een geversioneerde map met opmaak naast de code is genoeg tot je echte pijn voelt.

**Kleinbedrijf.** Zonder technisch schrijver en met een krap budget leun je op de documentatie die je tools al genereren en op lichte docs-as-code in plaats van een bemand programma. Formuleer de keuze als kopen tegenover bouwen: geef de voorkeur aan platforms die hun eigen actuele referentie en doorzoekbare kennisbank produceren boven een wiki die je met de hand moet verzorgen. Besteed je schaarse inspanning aan de twee of drie documenten waarvan de afwezigheid het bedrijf zou stilleggen, en laat een foute of ontbrekende pagina de trigger zijn om eigenaarschap te repareren.

**Grote onderneming.** Over veel teams zijn het probleem consistentie en vindbaarheid: een gedeelde docs-as-code-pipeline, een gemeenschappelijke structuur zoals Diátaxis, gegenereerde API-referenties en changelogs en besluitenlogboeken die overal op dezelfde manier worden toegepast, zodat kennis niet versplintert over tientallen wiki's. Wijs eigenaarschap toe voor elk waardevol document en meet nauwkeurigheid, niet alleen aanwezigheid. Behandel architectuurregisters, runbooks en besluitenlogboeken als auditbewijs en standaardiseer hoe ze worden geproduceerd, zodat een beheersingsreview een gedocumenteerd, verdedigbaar spoor vindt in plaats van een haastklus.

**Overheid.** Aanbestedingsregels en publieke verantwoording maken documentatie tot een oplevering, geen beleefdheid. Schrijf architectuurdocumentatie, runbooks en besluitenlogboeken in contracten als verplichte artefacten, beoordeeld op nauwkeurigheid zodat kennis een leverancierswissel overleeft en een systeem kan worden bediend door wie het erft. Eis dat elke bevoegde operator op een incident kan reageren vanuit het runbook alleen, en bewaar besluitenlogboeken als transparant openbaar verslag van waarom keuzes werden gemaakt. Dunne documentatie hier is geen privéongemak. Het wordt kostbaar reverse engineering gefinancierd door de belastingbetaler.

## Voorbeelden

**Startup.** Een startup van vijf personen schrijft een echte README voor elke service en een kort runbook voor de ene deploy-en-herstelprocedure waar iedereen tegenop ziet, zodat een storing om 2 uur 's nachts niet afhangt van het wakker maken van de enige oprichter die het systeem kent. Ze genereren API-documentatie uit het contract in plaats van haar met de hand te schrijven, en noteren een paar gedateerde aantekeningen die uitleggen waarom ze hun database en hun authenticatieaanpak kozen. Het blijft licht, maar het betekent dat de zesde en zevende aanwerving inwerken vanuit documenten in plaats van door iedereen te onderbreken.

**Grote onderneming.** Een groot softwarebedrijf houdt al zijn documentatie in dezelfde repositories als zijn code, geschreven in opmaak en beoordeeld in pull requests naast de wijzigingen die ze beschrijven. API-referenties worden gegenereerd uit servicecontracten, zodat ze nooit afdrijven. Changelogs worden gegenereerd uit gestructureerde commits, en architectuurbesluitenlogboeken bewaren de redenering achter grote keuzes. Een gepubliceerde documentatiesite bouwt automatisch bij elke samenvoeging. Nieuwe engineers worden snel productief omdat onboardinggidsen en runbooks actueel en vindbaar zijn, en engineers met bereikbaarheidsdienst leunen op runbooks in plaats van de oorspronkelijke auteurs op te pagen.

**Overheid.** Een nationale dienst erft een systeem van een vertrekkende aannemer en hangt volledig af van documentatie om kennis over de contractgrens te dragen. Omdat de vorige leverancier architectuurdocumentatie, runbooks en besluitenlogboeken als verplichte opleveringen onderhield, kan het nieuwe team het systeem bedienen en wijzigen zonder de oorspronkelijke auteurs. Waar de documentatie dun was, staat de dienst voor kostbaar reverse engineering. Die ervaring drijft een nieuw beleid: documentatie is een contractuele oplevering, beoordeeld op nauwkeurigheid in plaats van behandeld als bijzaak, en runbooks moeten elke bevoegde operator in staat stellen op incidenten te reageren.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Documentatie betaalt zich terug in kortere inwerktijd, minder sleutelpersoonrisico, snellere incidentrespons en lagere kosten van verandering over de levensduur van een systeem. Nieuwe engineers die in dagen in plaats van weken productief worden, personeel met bereikbaarheidsdienst dat incidenten oplost uit een runbook in plaats van te escaleren, onderhouders die een systeem jaren nadat het is gebouwd met vertrouwen wijzigen: dit zijn grote, terugkerende besparingen die zich opstapelen over een grote organisatie en een lange systeemlevensduur.

Wat kost documentatie? Schrijf- en onderhoudsinspanning. Wat kost *niet* documenteren? Je betaalt continu: in trage onboarding, herhaalde vragen, sleutelpersoonknelpunten, tragere incidentherstel en, in het uiterste geval, systemen die niemand veilig kan wijzigen, wat dure herschrijvingen of reverse engineering afdwingt. In scenario's van leverancierswissel en audit kan ontbrekende documentatie directe contractuele en compliancekosten dragen. Zet om het bestuur te overtuigen cijfers op inwerktijd, incidentresponstijd en hoeveel kritieke kennis in individuele hoofden zit. Formuleer docs-as-code en generatie dan als manieren om duurzame documentatie te krijgen zonder bijpassende onderhoudslast. En benadruk dat onnauwkeurige documentatie een verplichting is, dus de investering moet het actueel houden omvatten.

## Antipatronen en valkuilen

- **Verouderde documentatie gepresenteerd als actueel:** misleidt lezers en vernietigt het vertrouwen in alle documentatie.
- **De eenmalig geschreven wiki:** pagina's die worden gemaakt en nooit bijgewerkt, stilletjes afdrijvend van de werkelijkheid.
- **Documentatieversplintering:** kennis verspreid over veel tools en wiki's zodat niets te vinden is.
- **Documentatietypen mengen:** tutorials, referentie en uitleg door elkaar op één pagina, wat geen lezer goed dient.
- **Genereerbare inhoud met de hand onderhouden:** met de hand geschreven API-documentatie die onvermijdelijk afwijkt van de werkelijke interface.
- **Tribale kennis:** kritiek begrip dat alleen in hoofden van mensen en chatgeschiedenis wordt bewaard en verloren gaat wanneer ze vertrekken.
- **Documentatie als bijzaak:** aan het eind geschreven, zo al, in plaats van naast de wijziging.
- **Geen eigenaarschap:** documenten zonder verantwoordelijke eigenaar verrotten omdat bijwerken niemands taak is.

## Volwassenheidsmodel

- **Niveau 1, Initiëren.** Documentatie is schaars, verspreid en verouderd, en kennis leeft in hoofden van mensen. Wat bestaat werd eenmaal geschreven en nooit meer aangeraakt, dus een storing of een vertrek betekent het systeem via reverse engineering reconstrueren.
- **Niveau 2, Ontwikkelen.** Sleuteldocumenten bestaan, zoals README's en een paar runbooks, maar ze worden inconsistent onderhouden en zijn moeilijk te vinden. Sommige teams documenteren goed en andere nauwelijks, en er is geen gedeelde verwachting over wat een repository moet dragen of waar het moet leven.
- **Niveau 3, Standaardiseren.** Docs-as-code is de norm in de organisatie: een gemeenschappelijke structuur zoals Diátaxis, gegenereerde API-referenties en changelogs, besluitenlogboeken en een verwachting in review dat documenten veranderen met de code die ze beschrijven. Elk waardevol document heeft een benoemde eigenaar, en er is één bekend thuis met echte zoekfunctie.
- **Niveau 4, Beheersen.** Documentatie wordt gemeten, niet alleen aanwezig. Je volgt dekking van de essentiële documenten, documentwijzigingspercentage tegenover codewijzigingspercentage, inwerktijd, incidentoplossing uit runbooks alleen en versheid tegen een gedefinieerde verouderingsdrempel, en je beoordeelt die statistieken tegen uitgangswaarden. Verrotting wordt mechanisch opgevangen via generatie, tests tegen het systeem en link- en nauwkeurigheidscontroles, en verouderde pagina's worden op bewijs gemarkeerd of gesnoeid in plaats van bij toeval.
- **Niveau 5, Orkestreren.** Documentatie wordt continu verbeterd en is over de organisatie geïntegreerd: levend, grotendeels gegenereerd of getest tegen het systeem, bezeten, vindbaar en adaptief. Statistieken voeden terug waar je investeert, impliciete kennis wordt vastgelegd als routinematig onderdeel van het werk en het corpus wordt actief herbalanceerd en gesnoeid naarmate systemen, teams en lezers veranderen.

## Ideeën voor discussie

- Welke documentatie zou, als ze morgen verdween, je organisatie het meest pijn doen, en bestaat ze nu en blijft ze actueel?
- Hoe maak je het bijwerken van documentatie een natuurlijk onderdeel van het wijzigen van code in plaats van een aparte klus?
- Waar kun je met de hand geschreven documentatie vervangen door gegenereerde documentatie gekoppeld aan de bron van waarheid?
- Hoe meet je of je documentatie nauwkeurig en gebruikt is, niet alleen aanwezig?
- Hoe moeten AI-assistenten veranderen hoe je documentatie schrijft, onderhoudt en doorzoekt, en waar zouden ze aannemelijke maar foute inhoud kunnen introduceren?
- Hoe leg je impliciete kennis vast voordat de mensen die haar bezitten vertrekken?

## Belangrijkste inzichten

- Behandel documentatie als code: geversioneerd, beoordeeld, dicht bij de bron en automatisch gepubliceerd.
- Structureer inhoud naar behoefte van de lezer met tutorials, how-to-gidsen, referentie en uitleg.
- Onderhoud de essentiële zaken met hoge waarde: README's, runbooks, architectuurdocumentatie, onboarding en besluitenlogboeken.
- Genereer API-documentatie en changelogs zodat ze niet kunnen afwijken van de bron van waarheid.
- Bestrijd verrotting met eigenaarschap, reviewverwachtingen en snoeien. Onnauwkeurige documentatie is erger dan geen.

## Referenties en verder lezen

- Daniele Procida, *Diátaxis* documentation framework
- Andrew Etter, *Modern Technical Writing*
- Anne Gentle, *Docs Like Code*
- Google, *Developer Documentation Style Guide* and Season of Docs guidance (as reference exemplars)
- Michael Nygard, *Documenting Architecture Decisions* (architecture decision records)
- Andrew Hunt and David Thomas, *The Pragmatic Programmer* (on knowledge and documentation)
- *Keep a Changelog* (as a reference convention)
