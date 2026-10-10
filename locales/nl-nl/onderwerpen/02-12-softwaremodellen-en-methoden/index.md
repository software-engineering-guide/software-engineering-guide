# 2.12 Softwaremodellen en -methoden

## Overzicht en motivatie

Een softwaremodel is een bewuste vereenvoudiging van een systeem, gebouwd om een specifieke vraag te beantwoorden. Een methode is een gedisciplineerde manier om software te produceren, inclusief de modellen die ze onderweg gebruikt. Samen vormen ze een kennisgebied van de Software Engineering Body of Knowledge (SWEBOK), omdat ze de mentale gereedschappen zijn waarmee je over een systeem redeneert voor, tijdens en na het bouwen. Een UML-klassendiagram ([Unified Modelling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language)), een [entiteit-relatiediagram](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) (ERD), een [toestandsmachine](https://en.wikipedia.org/wiki/Finite-state_machine), een [formele specificatie](https://en.wikipedia.org/wiki/Formal_specification) en een wegwerpprototype zijn allemaal modellen. [Waterval](https://en.wikipedia.org/wiki/Waterfall_model), [prototyping](https://en.wikipedia.org/wiki/Software_prototyping), formele ontwikkeling en [agile](https://en.wikipedia.org/wiki/Agile_software_development) zijn allemaal methoden.

Waarom zou je modellen gebruiken? Omdat het menselijk werkgeheugen klein is en softwaresystemen groot zijn. Niemand kan een systeem van honderdduizend regels in zijn hoofd houden, dus tekenen we plaatjes en schrijven we abstracties die één facet tegelijk tonen: de data, de besturingsstroom, de toestanden, de interacties. Een model is nooit bedoeld om getrouw te zijn aan de code. Het is bedoeld om geschikt te zijn voor een beslissing. Een goed model toont precies wat je nodig hebt om iets te beslissen, en verbergt al het andere.

In grote teams gaat het in werkelijkheid om coördinatie en communicatie. Wanneer honderden engineers, architecten, analisten en auditors aan één systeem werken, zijn gedeelde modellen de gemeenschappelijke grond waar ze over ontwerp, vereisten en risico onderhandelen. Zie modelleren dus als gereedschap met een taak. Het loont wanneer een model goedkoper is dan de fout die het voorkomt. Het wordt verspilling wanneer je het tekent om het tekenen, het lang bewaart nadat het verouderd is, of het verder uitwerkt dan de beslissing waarvoor het bedoeld was. Modelleren sluit nauw aan op softwarevereisten (hoofdstuk 2.8), ontwerpprincipes voor software (hoofdstuk 2.2), architectuur en haar notaties zoals C4 en arc42 (hoofdstuk 3.1) en agile werkwijzen (hoofdstuk 10.7).

## Kernprincipes

- Elk model heeft een doel. Als je de beslissing die een model onderbouwt niet kunt noemen, teken het dan niet.
- Abstractie is de kernhandeling van modelleren: neem op wat voor het doel telt, laat de rest weg.
- Consistentie telt binnen en tussen modellen. Tegenstrijdige modellen zijn erger dan geen.
- Modellen zijn eerst communicatieartefacten. Hun publiek bepaalt hun notatie en detail.
- Geef de voorkeur aan het lichtste model dat de vraag beantwoordt. Uitwerking heeft draagkosten.
- Een model is zo goed als zijn analyse. Een ongecontroleerd model is een niet-geteste aanname.
- Kies de methode naar de onzekerheid, het risico en de gevolgen van falen van het probleem.

## Aanbevelingen

### Modelleer met abstractie, doel en consistentie

Begin elk model met het benoemen van zijn doel en publiek. Abstraheer dan meedogenloos naar dat doel: een sequentiediagram bedoeld om een race condition op te lossen moet timing en berichten tonen, niet elk veld. Houd je modellen consistent met elkaar, zodat de entiteiten in een ERD, de klassen in een klassendiagram en de zelfstandige naamwoorden in de vereisten allemaal overeenkomen, en consistent met de werkelijkheid, wat betekent dat je een model bijwerkt of verwijdert wanneer het systeem verder gaat. Een verouderd model dat mensen vertrouwen is een gevaar. Een verouderd model dat iedereen negeert is verspilling die nog steeds aandacht kost.

### Kies structurele of gedragsmodellen passend bij de vraag

Gebruik structurele modellen om te tonen waaruit een systeem bestaat en hoe de delen zich verhouden: klassendiagrammen, componentdiagrammen en entiteit-relatiediagrammen voor datastructuur. Gebruik gedragsmodellen om te tonen wat een systeem over de tijd doet: toestandsmachines voor objecten met betekenisvolle levenscycli, sequentiediagrammen voor interacties tussen componenten en activiteitendiagrammen voor werkstromen en bedrijfsprocessen. Kies de ene notatie die de beslissing voor je neus blootlegt. De meeste systemen hebben maar een handvol diagramtypen nodig, selectief getekend, niet de volledige UML-catalogus op alles toegepast.

### Analyseer modellen, teken ze niet alleen

Een model verdient zijn plek door analyse, niet alleen door tekenen. Controleer een toestandsmachine op onbereikbare toestanden, ontbrekende overgangen en deadlock. Controleer een ERD op normalisatieproblemen en verweesde relaties. Loop een sequentiediagram langs de vereisten om ontbrekende foutpaden te vinden. Beoordeel je modellen met de domeinexperts die kunnen zien wat er fout is. En waar de kosten van falen hoog zijn, grijp dan naar door tools ondersteunde analyse (modelcheckers, consistentiecheckers, simulatie) in plaats van het op het oog te doen.

### Pas heuristische methoden toe als standaard

De meeste software wordt gebouwd met heuristische methoden: op ervaring gebaseerde, iteratieve aanpakken die modellen informeel gebruiken en resultaten beoordelen aan verwachtingen in plaats van aan bewijzen. Voor de meeste bedrijfs- en overheidssystemen is dat precies goed: vereisten evolueren en een defect is meestal herstelbaar. Heuristische methoden passen vanzelf bij agile (hoofdstuk 10.7): modelleer net genoeg om het team af te stemmen, bouw dan en leer.

### Bewaar formele methoden voor kernen met zware gevolgen

[Formele methoden](https://en.wikipedia.org/wiki/Formal_methods) drukken specificaties uit in wiskunde en gebruiken verificatie, hetzij bewijs hetzij uitputtende [modelchecking](https://en.wikipedia.org/wiki/Model_checking), om eigenschappen vast te stellen. Ze kosten echte vaardigheid en tijd, en lonen juist waar falen catastrofaal of onomkeerbaar is: veiligheidskritieke besturing, cryptografische protocollen, kernen van financiële afwikkeling en dergelijke. Pas ze toe op de kleine kritieke kern, niet op het hele systeem. En merk op dat formele specificatie alleen, zelfs zonder volledig bewijs, vaak waarde toevoegt simpelweg doordat ze je dwingt precies te zijn.

### Gebruik prototyping om onzekerheid weg te nemen

Wanneer vereisten of haalbaarheid onduidelijk zijn, bouw dan een prototype om te leren en besluit dan, met opzet, of je het laat evolueren of weggooit. Wegwerpprototypes verkennen een vraag goedkoop en worden daarna verwijderd. Evolutionaire prototypes worden het product en moeten op productiestandaard worden gebouwd. De klassieke fout is een wegwerpprototype per ongeluk in productie te laten glippen. Benoem het type van het prototype dus voordat je het bouwt.

### Stem de methode af op risico, niet op mode

Kies methoden naar de onzekerheid van het probleem en de gevolgen van falen. Hoge onzekerheid pleit voor prototyping en agile iteratie. Zware gevolgen pleiten voor formele analyse en rigoureuze verificatie. Een systeem met beide heeft een kritieke formele kern binnen een verder agile omhulsel nodig. Wat je ook doet, neem een methode niet aan alleen omdat ze prestigieus is of omdat een leverancier haar verkoopt.

## Afwegingen: voor- en nadelen

| Model of methode | Goed toegepast | Faalwijze |
|---|---|---|
| Structurele modellen (UML, ERD) | Gedeeld beeld van delen en data | Diagramwildgroei. Afdrijving van de code |
| Gedragsmodellen (toestand, sequentie, activiteit) | Leggen timing, toestanden en randgevallen bloot | Te gedetailleerde diagrammen die niemand leest |
| Heuristische methoden | Snel, flexibel, passen bij de meeste systemen | Ongedisciplineerd. Verborgen aannames |
| Formele methoden | Bewijsbare eigenschappen voor kritieke kernen | Hoge kosten. Verkeerd toegepast op het hele systeem |
| Prototyping | Goedkoop leren. Neemt risico vroeg weg | Wegwerpcode bevorderd tot productie |
| Agile methoden | Past zich aan veranderende vereisten aan | Slaat modelleren over dat voor moeilijke problemen nodig is |

De terugkerende spanning is die tussen rigueur en snelheid. Te weinig modelleren brengt verborgen aannames in productie. Te veel modelleren verbrandt moeite aan diagrammen die nooit een beslissing onderbouwen en wegrotten zodra de code verandert. Er is geen vaste dosis die dit oplost, alleen een regel van evenredigheid: investeer in een model of methode in verhouding tot de onzekerheid die ze oplost en de kosten van een verkeerde beslissing. Een betalingsengine en een marketingmicrosite verdienen een andere behandeling.

## Vragen om met je team te bespreken

1. **Analyseren we onze modellen, of tekenen we ze alleen en gaan we door?** Een model verdient zijn plek door analyse, niet door te bestaan: een toestandsmachine die je nooit controleert op onbereikbare toestanden of ontbrekende overgangen is een niet-geteste aanname verkleed als diagram. In een groot team is dit waar echte defecten zich verbergen, want een plausibel ogend plaatje wordt vertrouwd juist wanneer niemand het langs de vereisten heeft gelopen om het ontbrekende foutpad of de verweesde relatie te vinden. Neem je belangrijkste gedragsmodel mee naar de vergadering en probeer het kapot te maken: welke overgang is niet gedefinieerd, welke toestand heeft geen uitgang, welke sequentie heeft geen time-out? Waar de kosten van falen hoog zijn, moet het antwoord je richting door tools ondersteunde analyse duwen (modelcheckers, consistentiecheckers, simulatie) in plaats van op het oog, want de hele reden om een kritieke kern te modelleren is de fout op een whiteboard te vinden in plaats van in productie.

2. **Wanneer twee van onze modellen het oneens zijn, welke wint, en wie merkt de tegenstrijdigheid op?** Consistentie telt binnen en tussen modellen, en tegenstrijdige modellen zijn erger dan geen, omdat mensen op beide handelen. In een groot systeem drijven de entiteiten in het datamodel, de klassen in het ontwerp en de zelfstandige naamwoorden in de vereisten stilletjes uit elkaar naarmate verschillende teams verschillende artefacten bijwerken, en het eerste teken is vaak een productiebug waarbij twee componenten het oneens waren over wat iets is. Neem een voorbeeld mee: kies een kernconcept en controleer of het ERD, de code en de vereisten werkelijk overeenkomen over zijn vorm en levenscyclus. Zo niet, besluit dan welk artefact gezaghebbend is en wie verantwoordelijk is de andere gelijk te houden, en wees bereid een model te verwijderen in plaats van een verouderd model het team te laten blijven voorliegen.

3. **Welke kern in ons systeem verliest echt geld of schaadt iemand als hij fout is, en krijgt die de rigueur die hij verdient?** De centrale zet van dit hoofdstuk is de methode afstemmen op risico: heuristische en agile methoden voor de herstelbare meerderheid, formele specificatie en verificatie voor de kleine kern met zware gevolgen en goedkope prototyping voor het werkelijk onzekere. De faalwijzen zijn symmetrisch en beide duur: formele methoden toepassen op een marketingmicrosite verbrandt geld, en een afwikkelingsengine of een stel geschiktheidsregels behandelen als gewoon agile werk nodigt het catastrofale, onomkeerbare defect uit. Neem een kaart van je systeem mee en markeer waar een fout catastrofaal tegenover herstelbaar is, en waar vereisten zeker tegenover onbekend zijn. Het antwoord moet je modelleerinvestering concentreren waar het geld en de dubbelzinnigheid zitten, en haar overal elders expliciet onthouden, zodat een kritieke formele kern binnen een verder agile omhulsel kan zitten zonder dat de ene methode in het gebied van de andere lekt.

4. **Hoeveel modelleren we voordat we code schrijven, en verandert die dosis met de onzekerheid voor ons?** Big design up front en helemaal geen ontwerp zijn beide faalwijzen, en de juiste dosis ligt ertussen, bepaald door hoeveel onzekerheid een model werkelijk wegneemt. In een groot team loopt de druk beide kanten op: een governanceproces kan een volledige set diagrammen eisen voor enige code, wat beslissingen vastlegt die met de minste informatie zijn genomen, terwijl leveringsdruk een team kan duwen de ene toestandsmachine over te slaan die een kostbaar randgeval had gevangen. Neem je laatste twee projecten mee en sorteer de modellen die je produceerde in die welke een echte beslissing onderbouwden en die welke alleen werden getekend omdat een sjabloon erom vroeg. Wees in programma's van onderneming en overheid, waar een fasepoort of goedkeuringscommissie vaak vooraf documenten voorschrijft, klaar om te pleiten voor modelleren dat het risico volgt in plaats van een vaste opleveringslijst, zodat de betalingskern haar rigueur krijgt en het interne rapportagehulpmiddel niet verdrinkt in diagrammen die niemand leest.

5. **Hebben we een gedeelde notatie en één thuis voor onze modellen afgesproken, of vindt elk team de zijne uit?** Modellen zijn eerst communicatieartefacten, en hun waarde stort in wanneer een toestandsmachine getekend in de tool van het ene team niet kan worden gelezen, gevonden of vertrouwd door het team dat haar erft. Voor honderden engineers zijn de concurrerende overwegingen echt: een voorgeschreven notatie en repository kopen consistentie en vindbaarheid, maar leggen ook een leerkost op en kunnen mensen naar zware tools duwen terwijl een gefotografeerd whiteboard zou volstaan. Neem voorbeelden mee van waar een model werkelijk leefde (een wiki, een diagramtool, een presentatie, iemands laptop) en vraag wie het zes maanden later kon vinden en begrijpen. In omgevingen van onderneming en regulering scherpt de auditinvalshoek dit aan: een auditor die het actuele datamodel niet kan vinden of een beslissing niet kan herleiden naar een gedocumenteerde toestandsmachine zal het systeem als ongedocumenteerd behandelen, dus spreek een kleine gedeelde notatie en een duurzame locatie af, en accepteer lichte vastlegging boven ceremonie waar de gevolgen laag zijn.

6. **Besluiten we voordat we een prototype bouwen met opzet of het wegwerp of evolutionair is, en houden we ons aan die keuze?** De klassieke, dure fout is een wegwerpprototype dat stilletjes in productie glipt omdat het goed demonstreerde en niemand van tevoren zijn type benoemde. De spanning is echt: wegwerpprototypes kopen het goedkoopst mogelijke leren en moeten worden verwijderd, terwijl evolutionaire prototypes het product worden en vanaf de eerste regel op productiestandaard moeten worden gebouwd, en de twee verwarren verspilt ofwel herwerk ofwel brengt fragiele code in een rol waarvoor ze nooit was ontworpen. Neem een recent prototype mee en vraag wat er werd besloten voordat het werd gebouwd, wie de bevoegdheid had het te promoveren of weg te gooien en of dat besluit de leveringsdruk overleefde. Behandel in overheids- en andere verantwoordingsplichtige settings, waar een burgergericht systeem transparantie- en betrouwbaarheidsverplichtingen draagt, onbedoelde promotie als falen van een beheersmaatregel: leg het lot van het prototype vooraf vast, en maak het weggooien van een geslaagd wegwerpprototype tot een gevierde uitkomst in plaats van verspilling die je moet vermijden.

## Sectorperspectief

**Startup.** Modelleer op een whiteboard, fotografeer het en ga verder. Je schaarsste middel is engineeringaandacht, dus grijp pas naar een model wanneer het goedkoper is dan de fout die het voorkomt: een abonnementstoestandsmachine voordat je de randgevallen van de facturering codeert, geen volledige UML-catalogus voor een product dat volgende maand kan pivoteren. Blijf heuristisch en agile, houd formele methoden helemaal van tafel en behandel elk prototype als wegwerp tenzij je bewust anders besluit.

**Kleinbedrijf.** Je hebt waarschijnlijk niemand wiens taak formeel modelleren is, dus leun op de modellen die al zijn ingebed in de tools en frameworks die je koopt in plaats van een eigen modelleerpraktijk op te zetten. Kader de paar modellen die je wel tekent rond concrete beslissingen: een eenvoudige schets van het datamodel om af te spreken welke klantdata je bewaart, een toestandsdiagram voor de ene werkstroom die je een klant kost wanneer hij breekt. Geef de voorkeur aan een gekocht product met een bewezen datamodel boven het zelf bouwen en documenteren van het jouwe, en houd wat je tekent licht genoeg dat één persoon het kan onderhouden.

**Grote onderneming.** Het kernprobleem is coördinatie over veel teams, dus gedeelde modellen worden de gemeenschappelijke grond: een afgesproken datamodel, een consistente notatie en een thuis waar het ERD, de C4-diagrammen en de toestandsmachines kunnen worden gevonden en vertrouwd. Standaardiseer een kleine notatie en dwing consistentie af zodat de entiteiten in de vereisten, het ontwerp en de database niet tussen teams uit elkaar drijven. Bewaar formele specificatie en modelchecking voor de kernen met zware gevolgen (afwikkeling, reconciliatie, toegangsbeheer), financier de specialistische vaardigheid die dat vraagt en houd een auditspoor bij van elk gedocumenteerd model terug naar de beslissing die het rechtvaardigde.

**Overheid.** Regels vastgelegd in wetgeving moeten herleidbaar zijn naar de wet, en daar verdient formele specificatie haar kosten: specificeer geschiktheids- of beoordelingslogica precies, verifieer kerneigenschappen en laat auditors elke uitkomst herleiden naar de regel die haar produceerde. Aanbesteding voegt eigen gewicht toe, aangezien documenten en modellen vaak contractuele opleveringen zijn, dus spreek af welke modellen werkelijk beslissingsdragend zijn in plaats van alleen geproduceerd om aan een checklist te voldoen. Publiceer beschrijvingen in gewone taal van hoe belangrijke systemen werken, en gebruik wegwerpprototyping om burgergerichte intake met echte gebruikers te testen voordat je je aan een productiebouw verbindt.

## Voorbeelden

**Startup.** Een kleine startup die een product voor abonnementsfacturering bouwt, schetst de levenscyclus van het abonnement (proef, actief, achterstallig, geannuleerd, heractiveerd) als toestandsmachine op een whiteboard voordat ze code schrijft. Terwijl ze het diagram doorlopen, merken ze op dat ze nooit definieerden wat er gebeurt wanneer de betaling van een achterstallig account eindelijk binnenkomt, een randgeval dat echte klanten in limbo zou hebben achtergelaten. Dat model van vijf minuten bespaart een productiekopzorg, en ze fotograferen het in plaats van een zware diagramtool te onderhouden. Overal elders blijven ze agile en modelleren ze net genoeg om af te stemmen, want op hun schaal is een defect herstelbaar en zouden formele methoden pure kosten zijn.

**Grote onderneming.** Een wereldwijde bank bouwt een nieuw betalingsplatform. Het team gebruikt een entiteit-relatiediagram om het gedeelde datamodel over de rekening-, grootboek- en berichtenteams af te spreken, en C4-diagrammen (hoofdstuk 3.1) om te tonen hoe de services in elkaar passen. Ze modelleren de transactielevenscyclus (in behandeling, vereffend, afgewikkeld, teruggedraaid, betwist) als expliciete toestandsmachine, en analyse toont dat er een overgang voor gedeeltelijke terugdraaiingen ontbreekt. Het gat wordt op een whiteboard hersteld in plaats van in productie. Sequentiediagrammen lopen de afwikkelingsstroom langs de vereisten (hoofdstuk 2.8) om ontbrekende time-out- en herhaalpaden bloot te leggen. De dagelijkse oplevering is agile, maar het kernalgoritme voor reconciliatie, waar een fout echt geldverlies betekent, krijgt een formele specificatie en wordt voor de implementatie modelgechecked. Modelleren is geconcentreerd waar het geld en de dubbelzinnigheid zitten, en overal elders licht gehouden.

**Overheid.** Een nationale belastingdienst moderniseert de beoordeling van uitkeringen. Omdat geschiktheidsregels in wet zijn vastgelegd en worden geaudit, schrijft het team een formele specificatie van de regels als zuivere transformaties en verifieert kerneigenschappen, zoals dat geen aanvrager zowel geschikt als ongeschikt is en elke zaak tot een besluit komt, zodat auditors uitkomsten kunnen herleiden naar de wet. Naast de formele kern bouwt het team een wegwerpprototype van het burgergerichte intakeformulier om met echte gebruikers te testen. Ze leren dat een wizard met meerdere stappen fouten vermindert, gooien dan het prototype weg en bouwen de intake opnieuw op productiestandaard. Activiteitendiagrammen documenteren het volledige proces van de zaakbehandelaar voor training en audit. De regels met zware gevolgen krijgen formele rigueur, de onzekere gebruikerservaring krijgt goedkope prototyping, en geen van beide methoden wordt toegepast waar de andere thuishoort.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Het rendement van modelleren komt uit het eerder vinden van defecten, waar ze veel goedkoper te herstellen zijn. Een tegenstrijdigheid gevonden op een whiteboard kost minuten. Dezelfde tegenstrijdigheid gevonden in productie kan een storing, een herwerkprogramma of, in gereguleerde domeinen, een juridische aansprakelijkheid kosten. Modellen verlagen ook de total cost of ownership door als duurzame communicatie te dienen. Een systeem dat zijn auteurs overleeft, het normale geval in onderneming en overheid, is veel goedkoper te onderhouden wanneer zijn datamodel, toestandsmachines en sleutelstromen nauwkeurig zijn gedocumenteerd.

De kosten zijn echt en je moet ze wegen. Modellen kosten tijd om te bouwen, vaardigheid om goed te bouwen en doorlopende inspanning om actueel te houden. Formele methoden voegen specialistische arbeid toe. Het break-evenpunt wordt bepaald door onzekerheid en gevolgen. Waar beide laag zijn, vernietigt zwaar modelleren waarde en winnen agile heuristieken. Waar een van beide hoog is, loont gericht modelleren, en voor de kritieke kern formele verificatie, vele malen door de dure klasse van falen te voorkomen. Koppel modelleerinvestering om het bestuur te overtuigen aan specifieke risico's die zijn weggenomen en aan de onderhoudbaarheid van langlevende systemen. En volg of modellen werkelijk worden geraadpleegd, want een ongebruikt model is pure kost.

## Antipatronen en valkuilen

- **Modelleren om het modelleren:** diagrammen produceren omdat een proces erom vraagt, niet omdat ze een beslissing onderbouwen.
- **Verouderde modellen vertrouwd als waarheid:** diagrammen die niet meer bij de code passen maar waarop nog wordt vertrouwd.
- **Big design up front:** uitputtende modellen geproduceerd vóór enige code, wat beslissingen vastlegt die met de minste informatie zijn genomen.
- **Diagramwildgroei:** elk UML-type uniform toegepast, waardoor de paar nuttige gezichtspunten verdrinken in ruis.
- **Formele methoden overal:** dure verificatie toepassen op code waar de gevolgen van falen het niet rechtvaardigen.
- **Onbedoelde promotie van prototypes:** een wegwerpprototype dat stilletjes als product wordt opgeleverd.
- **Notatie boven inhoud:** ruziën over UML-correctheid in plaats van of het model de vraag beantwoordt.

## Volwassenheidsmodel

- **Niveau 1 (Initiëren):** Modelleren is ad hoc of afwezig en puur reactief. Er wordt geen methode benoemd. Modellen, als ze al worden getekend, zijn inconsistent, ongeanalyseerd en verlaten zodra de vergadering eindigt.
- **Niveau 2 (Ontwikkelen):** Sommige teams tekenen gangbare diagrammen en volgen een benoemde methode, maar de praktijk is ongelijk over de organisatie: modellen worden vaak ceremonieel geproduceerd, drijven af van de code en worden zelden op defecten geanalyseerd.
- **Niveau 3 (Standaardiseren):** Een gedeelde notatie, een gedocumenteerde gids voor methodekeuze en consistentieregels zijn gedefinieerd en organisatiebreed gehandhaafd. Modellen worden gekozen naar doel, gelijkgehouden met het systeem, op defecten beoordeeld, en de methode wordt afgestemd op het risico van elk probleem.
- **Niveau 4 (Beheersen):** Modelleren wordt gemeten en beheerst aan de hand van uitgangswaarden. Teams volgen hoeveel defecten analyse vóór de implementatie vangt, hoe ver modellen van de code afdrijven, of elk model werkelijk is geraadpleegd voor een echte beslissing en het herwerk en de doorlooptijd die zijn bespaard tegenover een gedefinieerde uitgangswaarde. Methodekeuze is gekalibreerd op gemeten onzekerheid en gevolgen, en kritieke kernen worden formeel geverifieerd tegen afgesproken dekkingsdoelen.
- **Niveau 5 (Orkestreren):** Modelleren en methodekeuze worden continu verbeterd en zijn geïntegreerd met oplevering en risicoplanning over de organisatie. Investering past zich aan naarmate onzekerheid en gevolgen verschuiven, modellen worden routinematig op bewijs actueel gehouden, afgebouwd of verdiept, en formele, heuristische en prototypingmethoden worden samengesteld zodat elk precies zit waar het loont.

## Ideeën voor discussie

- Welke modellen onderbouwden in je laatste project een echte beslissing, en welke werden alleen getekend omdat een proces erom vroeg?
- Waar in je systemen zou een formele specificatie zichzelf terugbetalen, en waar zou ze verspilling zijn?
- Hoe besluit je of een prototype wegwerp of evolutionair is, en dwing je dat besluit af?
- Hoe voorkom je dat modellen uit de pas met de code lopen, of accepteer je dat sommige beter kunnen worden verwijderd?
- Wat is in jouw context de juiste hoeveelheid modelleren vóór code, en hoe verandert die met onzekerheid?
- Welk gedragsmodel (toestand, sequentie of activiteit) zou je meest recente productie-incident hebben gevangen?

## Belangrijkste inzichten

- Een model is een doelgerichte abstractie. Als je de beslissing die het onderbouwt niet kunt noemen, teken het dan niet.
- Stem structurele en gedragsmodellen af op de specifieke vraag en houd ze consistent en actueel.
- Analyseer modellen. Een ongecontroleerd model is een niet-geteste aanname.
- Heuristische en agile methoden passen bij de meeste systemen. Bewaar formele methoden voor kernen met zware gevolgen.
- Gebruik prototypes om onzekerheid weg te nemen en besluit vooraf of ze wegwerp of evolutionair zijn.
- Investeer in modelleren in verhouding tot de onzekerheid die het oplost en de kosten van een verkeerde beslissing.

## Referenties en verder lezen

- IEEE Computer Society, *SWEBOK Guide (Software Engineering Body of Knowledge), Version 4.0*, Software Engineering Models and Methods knowledge area
- Martin Fowler, *UML Distilled: A Brief Guide to the Standard Object Modelling Language*
- Grady Booch, James Rumbaugh, Ivar Jacobson, *The Unified Modelling Language User Guide*
- Frederick P. Brooks, *The Mythical Man-Month* and *No Silver Bullet: Essence and Accident in Software Engineering*
- Daniel Jackson, *Software Abstractions: Logic, Language, and Analysis* (the Alloy modelling language)
- Leslie Lamport, *Specifying Systems* (TLA+)
- Simon Brown, *Software Architecture for Developers* (the C4 model)
- David Harel, *Statecharts: A Visual Formalism for Complex Systems*
