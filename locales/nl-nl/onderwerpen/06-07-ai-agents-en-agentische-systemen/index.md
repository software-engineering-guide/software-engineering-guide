# 6.7 AI-agents en agentische systemen

## Overzicht en motivatie

Een **AI-agent** is een [groot taalmodel](https://en.wikipedia.org/wiki/Large_language_model) (LLM) verpakt in een lus: het krijgt een doel, kan tools aanroepen, houdt wat geheugen bij van wat het heeft gedaan en bepaalt zelf zijn volgende stap tot het doel is bereikt of het opgeeft. Die lus is het hele verschil tussen een agent en de gewone prompt-responsaanroepen van hoofdstuk 6.3. Een enkele aanroep beantwoordt een vraag. Een agent leest zijn e-mail, doorzoekt een database, dient een ticket in, controleert het resultaat en probeert opnieuw. Het model produceert niet langer alleen tekst. Het kiest acties in jouw systemen.

Die verschuiving verandert het engineeringprobleem. Wanneer een model alleen woorden schrijft, is een slechte uitvoer een slechte zin. Wanneer een model tools aanstuurt, kan een slechte uitvoer een verkeerd bericht sturen, een record verwijderen of geld verplaatsen. Een [intelligente agent](https://en.wikipedia.org/wiki/Intelligent_agent) wordt dus het best begrepen als onbetrouwbare planner binnen een vertrouwd systeem, en het meeste van je werk gaat naar het begrenzen van wat die planner mag doen. Dit hoofdstuk bouwt direct voort op de LLM-fundamenten van hoofdstuk 6.3, de zorgen over vertrouwen en verantwoording van hoofdstuk 6.5 en de platformpraktijken van hoofdstuk 6.6.

Voor grote teams is de inzet net zo organisatorisch als technisch. Ondernemingen willen agents bedraad in echte interne systemen (ticketing, financiën, klantdossiers), wat betekent dat agents echte toegangscontroles en echte verplichtingen voor wijzigingsbeheer erven. De overheid voegt publieke verantwoording toe: een autonome actie die een burger raakt moet achteraf uitlegbaar, overziend en controleerbaar zijn. Het patroon is krachtig. Zonder discipline ingezet is het een snelle manier om fouten te automatiseren.

## Kernprincipes

- Een agent is een model plus een lus, tools, geheugen en een doel. Het risico leeft in de lus, niet in het proza.
- Begrens autonomie tot de taak. Geef de kleinste hoeveelheid vrijheid waarmee het werk gedaan wordt.
- Geef de voorkeur aan een vaste workflow wanneer de stappen bekend zijn. Grijp alleen naar open autonomie wanneer ze dat niet zijn.
- Behandel elke tool als aanvalsoppervlak en geef haar het minste privilege waarmee ze kan werken.
- Zet een mens in de lus voor ingrijpende of onomkeerbare acties, en maak terugdraaien goedkoop.
- Evalueer op taaksucces, niet op hoe het transcript leest.
- Trace elke run. Een actie die je niet kunt reconstrueren is een actie die je niet kunt besturen.
- Het eenvoudigste ontwerp dat werkt is meestal het juiste. Vaak is dat helemaal geen agent.

## Aanbevelingen

### Begin met een workflow, voeg alleen autonomie toe waar het moet

De gangbaarste fout is naar een autonome agent grijpen wanneer een vaste pijplijn zou volstaan. Als je de stappen al kent (velden extraheren, valideren, een record opzoeken, een antwoord opstellen), schrijf dat dan als georkestreerde workflow met het model dat specifieke slots vult. Autonomie verdient haar plek wanneer het pad werkelijk niet vooraf kan worden bepaald, bijvoorbeeld open onderzoek of triage over veel mogelijke tools. Begrens de autonomie tot de taak: begrens het aantal stappen, beperk de toolset tot wat dit doel nodig heeft en stel een duidelijke stopvoorwaarde. Een goede regel is het model precies zoveel vrijheid te geven als het probleem eist en geen graad meer.

### Maak toolgebruik het kernvermogen, en maak het veilig

Toolgebruik (ook functieaanroepen genoemd) is wat een model tot agent maakt. Definieer elke tool met een precies schema, valideer elk argument dat het model levert en pas het [principe van minste privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) toe: een alleen-lezen rapportageagent krijgt alleen-lezen inloggegevens, nooit schrijftoegang die ze zou kunnen misbruiken. Draai tools in een [sandbox](https://en.wikipedia.org/wiki/Sandbox_(computer_security)) zodat een slechte aanroep niet voorbij zijn schadezone reikt. Geef de voorkeur aan veel smalle tools voor één doel boven een paar brede, omdat een smalle tool makkelijker te beredeneren, van rechten te voorzien en te auditen is. Dit is dezelfde terughoudendheid die hoofdstuk 6.3 aanraadt voor LLM-toolgebruik, hier centraal gemaakt.

### Gebruik expliciete redeneer- en planningspatronen

Agents werken beter wanneer hun denken gestructureerd is. In een reason-and-act-patroon (gepopulariseerd door het ReAct-onderzoek) wisselt het model af tussen redeneren over de situatie en een actie ondernemen, en observeert dan het resultaat voordat het opnieuw redeneert. Laat het model voor moeilijkere doelen eerst plannen (opdelen in deeltaken) en dan uitvoeren, zodat je het plan kunt inspecteren en zelfs goedkeuren voordat enige tool draait. Houd deze lussen observeerbaar en onderbreekbaar. Een plan dat je kunt lezen is een plan dat je kunt stoppen.

### Houd mensen in de lus voor ingrijpende acties

Besluit per tool en per actie of het model alleen mag handelen of eerst moet vragen. Omkeerbare acties met lage inzet (zoeken, opstellen) kunnen onbeheerd draaien. Ingrijpende of onomkeerbare (externe communicatie versturen, geld verplaatsen, productiedata wijzigen, over de zaak van een burger beslissen) hebben een [human-in-the-loop](https://en.wikipedia.org/wiki/Human-in-the-loop)-poort nodig met echt gezag om nee te zeggen. Ontwerp waar mogelijk voor omkeerbaarheid: geef de voorkeur aan een wijziging klaarzetten boven haar vastleggen, en maak ongedaan maken een eersterangs functie zodat een verkeerde actie minuten kost, geen incident.

### Behandel het beveiligingsmodel als vijandig

Agents verbreden het aanvalsoppervlak beschreven in hoofdstuk 4.2. De hoofddreiging is [prompt-injectie](https://en.wikipedia.org/wiki/Prompt_injection): kwaadwillende instructies verborgen in een webpagina, document of e-mail die de agent leest en gehoorzaamt. Nauw verwant is het [confused-deputyprobleem](https://en.wikipedia.org/wiki/Confused_deputy_problem), waarbij een aanvaller een bevoorrechte agent misleidt zijn eigen legitieme toegang te misbruiken, bijvoorbeeld data weglekken via een tool die de agent mag aanroepen. Neem aan dat alle content die de agent inneemt vijandig kan zijn. Scheid vertrouwde instructies van onbetrouwbare data, beperk tools zodat een gekaapte agent gevoelige systemen niet kan bereiken en laat ruwe modeluitvoer nooit een onomkeerbare actie triggeren zonder validatie.

### Evalueer op taaksucces en regressietest het niet-determinisme

Beoordeel agents op of ze de taak volbrengen, niet op of het transcript slim klinkt. Bouw een evaluatieset van representatieve doelen met controleerbare succescriteria (kreeg het ticket de juiste prioriteit, kwam de terugbetaling overeen met het beleid) en draai die bij elke prompt-, model- of toolwijziging. Omdat agents niet-deterministisch zijn bewijst één run weinig: draai elk geval meerdere keren en volg een succespercentage, niet geslaagd of gefaald. Dit breidt de offline en online evaluatiediscipline van hoofdstuk 6.3 en 6.2 (machine-learningengineering en MLOps) uit naar systemen waarvan de uitvoer een reeks acties is.

### Instrumenteer runs voor observeerbaarheid, kosten en foutafhandeling

Je kunt niet besturen wat je niet kunt zien. Trace elke agentrun van begin tot eind (hoofdstuk 6.6): het doel, elke redeneerstap, elke toolaanroep met argumenten en resultaat, de bestede tokens en de uiteindelijke uitkomst. Deze tracing is tegelijk je debugger, je auditspoor en je kostenmeter. Stel harde budgetten in op stappen, tijd en uitgaven, want een agent die loopt kan snel latentie en geld verbranden. Handel falen expliciet af: probeer tijdelijke toolfouten opnieuw met backoff, maar detecteer lussen waarin het model een falende actie herhaalt, en faal veilig in plaats van te rammelen.

## Afwegingen: voor- en nadelen

| Keuze | Voordelen | Nadelen | Het best wanneer |
|---|---|---|---|
| Vaste workflow (model vult slots) | Voorspelbaar, goedkoop, makkelijk te testen en auditen | Rigide. Breekt op onvoorziene paden | Stappen vooraf bekend zijn |
| Autonome enkele agent | Flexibel. Handelt open doelen af | Moeilijker te beheersen, evalueren en begrenzen | Het pad niet vooraf kan worden bepaald |
| Multi-agentorkestratie | Parallellisme. Gespecialiseerde rollen | Coördinatiekosten, oplopende fouten, hogere uitgaven | Een taak werkelijk uiteenvalt in onafhankelijke delen |
| Onbeheerde actie | Snel, weinig wrijving | Fouten worden uitgevoerd zonder controle | Acties omkeerbaar zijn en lage inzet hebben |
| Human-in-the-loop-poort | Veiligheid, verantwoording, omkeerbaarheid | Langzamer. Vraagt reviewercapaciteit | Acties ingrijpend of onomkeerbaar zijn |

De centrale spanning is autonomie tegenover controle. Meer autonomie handelt meer situaties af maar vraagt meer vangrails, meer evaluatie en meer geld, en faalt op manieren die moeilijker te voorspellen zijn. Multi-agentontwerpen verleiden teams met elegantie, maar elke extra agent voegt coördinatie-overhead toe en nog een plek waar een kleine fout oploopt tot een fout resultaat. Los de spanning op door te beginnen met de minste autonomie die het probleem oplost en vrijheid alleen toe te voegen wanneer een concrete taak je ertoe dwingt, altijd gekoppeld aan een passende vangrail.

## Vragen om met je team te bespreken

1. **Heeft deze functie werkelijk een agent nodig, of zou een vaste workflow veiliger en goedkoper zijn?** Autonomie is verleidelijk, maar de meeste taken hebben kenbare stappen die een georkestreerde pijplijn met veel minder risico afhandelt. Voor een groot team betekent standaard agents dat elke groep evaluatie-, tracing- en beveiligingslasten op zich neemt die een eenvoudiger ontwerp zou vermijden. Neem de specifieke taak mee en vraag of de stappen vooraf kunnen worden bepaald. Als dat kan, is een agent waarschijnlijk over-engineering. Reserveer open autonomie voor doelen waar het pad werkelijk per geval verschilt. Het antwoord moet de meeste functies naar een workflow duwen en een kleine, bewuste set als echte agents laten.

2. **Wat is voor elke tool die onze agent kan aanroepen het ergste dat een gekaapte agent ermee kan doen, en wat belet dat?** Prompt-injectie en confused-deputy-aanvallen keren de eigen legitieme toegang van de agent tegen je, dus de juiste lens is vijandig (hoofdstuk 4.2). Maak een inventaris van elke tool, haar privilegebereik en of een kwaadwillende instructie gesmokkeld via ingenomen content haar kan bereiken. Voor ondernemingen die agents in interne systemen bedraden is dit waar minste privilege, sandboxing en menselijke poorten op onomkeerbare acties echt worden. Neem de lijst tools mee en de inloggegevens die elke houdt. Als enige ingrijpende actie bereikbaar is zonder validatie of menselijke controle, is dat het eerste om te repareren.

3. **Hoe zouden we weten dat het succespercentage van een agent daalde, gegeven dat elke run plausibel oogt?** Agents zijn niet-deterministisch, dus een transcript dat goed leest kan toch de verkeerde actie hebben genomen, en één groene run bewijst niets. Vraag of je een evaluatieset hebt van doelen met controleerbare uitkomsten, per geval vaak gedraaid om een succespercentage te produceren in plaats van één geslaagd. Bespreek voor toepassingen met hoge inzet of publiek bereik hoe runtraces je laten reconstrueren wat er precies gebeurde als er iets misgaat (hoofdstuk 6.5 en 6.6). Als je enige signaal gebruikersklachten zijn, ben je al te laat. Het antwoord moet een evaluatiekader financieren vóór opschalen, niet na een incident.

4. **Welke van de acties van deze agent zijn echt onomkeerbaar, wie heeft het gezag ze goed te keuren en hebben we de reviewercapaciteit om die poort te bemannen?** De verleiding is het model overal onbeheerd te laten handelen, maar een menselijke poort is alleen echt als een benoemd persoon met gezag om nee te zeggen beschikbaar is wanneer de agent erom vraagt. Voor een groot team wordt een goedkeuringswachtrij die niemand bezit stilletjes een rubberen stempel, en verdampt de veiligheid die je ontwierp onder volume. Neem de volledige lijst acties mee die de agent kan nemen, markeer elk als omkeerbaar of onomkeerbaar en schat het dagelijkse volume lage-zekerheidsgevallen dat bij een reviewer zou landen. Weeg de wrijving en bemanningskosten van een poort af tegen de schadezone van een onbeheerde fout, en geef de voorkeur aan een onomkeerbare actie herontwerpen tot een klaargezette, ongedaan te maken actie boven nog een reviewer toevoegen. Koppel in omgevingen van onderneming en overheid elke ingrijpende actie aan een verantwoordelijke functionaris en een registratie van wijzigingsbeheer, want een autonome actie die een burger of klant raakt en die geen mens goedkeurde is precies het falen dat een audit zal vinden.

5. **Grijpen we naar een multi-agentontwerp omdat de taak werkelijk uiteenvalt, of omdat het elegant oogt?** Werk verdelen over gespecialiseerde agents is verleidelijk, maar elke extra agent voegt coördinatie-overhead toe en nog een plek waar een kleine fout oploopt tot een fout resultaat. Voor een grote organisatie zijn de kosten niet alleen uitgaven en latentie: een multi-agentsysteem is veel moeilijker te tracen, evalueren en te beredeneren wanneer het faalt, dus de governancelast vermenigvuldigt zich met elke rol die je toevoegt. Neem de taak mee en toon concreet welke delen onafhankelijk en parallel draaien, vergelijk dan het gemeten succespercentage en de kosten van een multi-agentversie met een enkele agent op dezelfde evaluatieset. Als de enkele agent wint of gelijkspeelt, is het elegante ontwerp over-engineering. Onthoud voor gereguleerde of publieke deployments dat elke agent in de keten nog een component is die een toezichtsorgaan moet kunnen inspecteren, dus toegevoegde structuur die je niet kunt rechtvaardigen is toegevoegde aansprakelijkheid.

6. **Wat zijn de harde budgetten op de stappen, tijd en uitgaven van een agent, en hoe zou een lopende agent worden gevangen voordat hij kosten of latentie opjaagt?** Een agent die een falende actie herhaalt kan zonder waarschuwing geld en tijd verbranden, dus onbegrensde autonomie is net zo goed een financieel als een veiligheidsrisico. Voor een groot team dat veel agents draait kan één misdragende lus een cloudrekening opjagen of een snelheidslimiet uitputten die elke andere werklast uithongert, wat limieten per run een gedeelde operationele zorg maakt in plaats van het probleem van één team. Neem de huidige stap-, tijd- en tokenbudgetten voor elke agent mee, de alarmering die afgaat wanneer een run ze overschrijdt en de lusdetectie die veilig faalt in plaats van te rammelen. Weeg strakke budgetten, die een legitiem moeilijke taak kunnen afkappen, af tegen losse die kosten laten weglopen. In omgevingen van onderneming en overheid waar uitgaven moeten worden voorspeld en gerechtvaardigd is een agent met onbegrensde kosten een post die je niet kunt verdedigen in een begrotingsreview of een audit.

## Sectorperspectief

**Startup.** Lever één smalle agent op die je kernwaarde raakt, op een gehost model, met de kleinste toolset die het werk doet en een hard plafond op stappen en uitgaven. Weersta de multi-agentdemo: je schaarse engineeringaandacht wordt beter besteed aan de autonomie van één agent begrenzen en haar runs tracen dan rollen coördineren die je niet kunt onderhouden. Houd elke ingrijpende actie achter één "opstellen, nooit versturen"-poort zodat een fout een klik kost om ongedaan te maken, geen incident.

**Kleinbedrijf.** Je hebt niemand om een evaluatiekader of sandbox te draaien, dus geef de voorkeur aan agents ingebed in tools die je al vertrouwt en zet alleen de autonomie aan die je met het oog kunt superviseren. Behandel elke agent die namens jou kan versturen, betalen of verwijderen als iets om uit te houden tot een persoon elke actie bevestigt, want een fout geautomatiseerd bericht aan een klant kost je de relatie. Geef de voorkeur aan leveranciers die je laten zien wat de agent deed en je de automatisering laten uitzetten.

**Grote onderneming.** Het probleem is agents besturen over veel teams: gedeelde patronen voor autonomie begrenzen, tool-inloggegevens met minste privilege, sandboxing, human-in-the-loop-poorten en tracing van begin tot eind zodat geen groep de vangrails opnieuw uitvindt. Bedraad agents in interne systemen onder dezelfde toegangscontroles die een mens zou hebben, poort onomkeerbare acties achter benoemde goedkeurders en wijzigingsbeheer en beheer het portfolio met succespercentages, budgetten per run en adversarieel injectietesten. Standaardiseer de trace- en evaluatielaag zodat het gedrag van elke agent kan worden gereconstrueerd en geaudit.

**Overheid.** Aanbesteding, transparantie en publieke verantwoording begrenzen elke keuze. Houd agents bij feiten verzamelen en opstellen, en reserveer elke beslissing die een burger raakt voor een verantwoordelijke mens, omdat verantwoordelijkheid voor een beslissing van de publieke sector niet aan een model kan worden gedelegeerd. Log elke run zodat een toezichtsorgaan kan zien welke bronnen zijn geraadpleegd en wat is gedaan, eis dat leveranciers de tools en beperkingen van de agent bekendmaken en bewijs met een adversariële evaluatieset dat de agent weigert te handelen buiten haar begrensde opdracht.

## Voorbeelden

**Startup.** Een analytics-startup van vijf personen bouwt een supporttriage-agent. Ze leest een binnenkomend ticket, doorzoekt de documentatie en stelt óf een antwoord op óf routeert het ticket naar een mens, en dat is de hele toolset. De inloggegevens zijn alleen-lezen plus één "concept maken"-actie die nooit verstuurt zonder dat een persoon op verzenden klikt. Elke run wordt getraced zodat de oprichters kunnen zien waarom een ticket ergens heen werd gerouteerd, en een nachtelijke evaluatieset van vijftig echte tickets draait de agent elk vijf keer om een routeringsnauwkeurigheidspercentage te volgen. Wanneer de slimme multi-agentdemo van een concurrent hen verleidt, blijven ze bij een enkele agent omdat hun taak niet uiteenvalt.

**Grote onderneming.** Een bank bouwt een agent om operationele medewerkers te helpen mislukte betalingen af te stemmen. Ze integreert met interne systemen onder dezelfde toegangscontroles die een menselijke medewerker heeft, verleend via service-inloggegevens met minste privilege die alleen tot afstemming zijn afgebakend. De agent mag vrij onderzoeken (grootboeken lezen, transactiegeschiedenis doorzoeken) maar elke actie die geld verplaatst of een record bewerkt wordt klaargezet en vereist een benoemde menselijke goedkeurder, wat aan wijzigingsbeheer voldoet. Ingenomen documenten worden als onbetrouwbaar behandeld om prompt-injectie af te stompen, tools draaien gesandboxt en elke run wordt van begin tot eind getraced voor audit. Een offline evaluatieset poort elke model- of promptwijziging, en budgetten per run begrenzen stappen en uitgaven zodat een lopende agent geen kosten of latentie kan opjagen.

**Overheid.** Een uitkeringsinstantie pilot een agent om dossierbehandelaars te helpen de feiten voor een aanvraag samen te stellen: records ophalen, geschiktheidsregels controleren en een samenvatting opstellen. De instantie trekt een harde lijn: de agent verzamelt en stelt op, maar een menselijke dossierbehandelaar neemt en bezit elke beslissing die een burger raakt, omdat verantwoording voor beslissingen van de publieke sector niet aan een model kan worden gedelegeerd (hoofdstuk 6.5). Elke run wordt volledig gelogd en toont welke bronnen zijn geraadpleegd en wat is opgesteld, zodat een toezichtsorgaan elke zaak kan auditen. Autonomie is bewust begrensd tot lezen en opstellen, tools hebben minste privilege en zijn gesandboxt en een adversariële evaluatieset bevestigt dat de agent weigert te handelen buiten feiten verzamelen.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Agents leveren rendement door werk in meerdere stappen te automatiseren dat vroeger een persoon nodig had om tussen systemen te klikken: triage, afstemming, onderzoek en routineoperaties. De waarde toont zich als werk voltooid zonder mens bij elke stap, snellere doorlooptijden en medewerkers vrijgemaakt voor oordeelzware taken. Omdat agents voortbouwen op bestaande LLM's en tools is de tijd tot een werkend prototype kort, wat precies de reden is dat teams te veel bouwen.

De total cost of ownership is waar agents van gewone LLM-functies verschillen. Bovenop inferentiekosten betaal je voor de toolintegraties, de sandboxing en rechtenleidingen, het evaluatiekader, de tracing- en observeerbaarheidsstack (hoofdstuk 6.6) en de menselijke reviewers die de goedkeuringspoorten bemannen. Een lopende of slecht begrensde agent voegt een variabele kost toe die zonder waarschuwing kan pieken, dus budgetten op stappen en uitgaven zijn onderdeel van het ontwerp, geen bijgedachte. De kosten van niet adopteren zijn tragere operaties en handmatig sleurwerk dat je concurrenten automatiseren. De kosten van onzorgvuldig adopteren zijn een autonome actie die het verkeerde bericht stuurt, data lekt of een onverantwoorde beslissing neemt. Maak de zaak voor het bestuur door één concreet automatiseringsdoel te koppelen aan een concreet plan voor vangrails, evaluatie en menselijk toezicht, en wees eerlijk dat de vangrails het grootste deel van de kosten zijn.

## Antipatronen en valkuilen

- **Agent waar een workflow volstond.** De volle risico's van autonomie nemen voor een taak waarvan de stappen kenbaar waren.
- **Te brede tools en inloggegevens.** Eén "doe alles"-tool in plaats van smalle tools met minste privilege.
- **Blindheid voor prompt-injectie.** Onbetrouwbare content voeden aan een agent die echte privileges houdt.
- **Geen menselijke poort op onomkeerbare acties.** Het model laten versturen, betalen of verwijderen zonder controle.
- **Multi-agenttheater.** Een eenvoudige taak over agents splitsen en coördinatiekosten betalen zonder winst.
- **Evaluatie op gevoel.** Beoordelen aan hoe het transcript leest in plaats van taaksuccespercentage.
- **Onbegrensde lussen.** Geen limiet op stappen, tijd of uitgaven, zodat een vastgelopen agent geld en latentie verbrandt.
- **Niet-getracete runs.** Geen registratie van wat de agent deed, zodat je niet kunt debuggen, auditen of verantwoorden.

## Volwassenheidsmodel

- **Niveau 1, Initiëren:** Agents worden ad hoc geprototypet met brede toegang tot tools en zonder grenzen. Succes wordt beoordeeld aan demo's, reactief, nadat iets brak. Er is geen evaluatieset, geen tracing en geen menselijke poort op ingrijpende acties.
- **Niveau 2, Ontwikkelen:** Sommige agents hebben begrensde lussen en tools met minste privilege, en basistracing bestaat, maar de praktijk varieert per team. Een handmatige evaluatieset vangt grove regressies in enkele projecten terwijl andere er geen hebben. Menselijke goedkeuring bewaakt de meest voor de hand liggende onomkeerbare acties, maar de dekking is ongelijk en ongedocumenteerd.
- **Niveau 3, Standaardiseren:** Gedeelde patronen besturen autonomie, toolrechten, sandboxing en human-in-the-loop-poorten, gedocumenteerd en afgedwongen in elk team. Elke ingrijpende actie wordt gepoort of gevalideerd, agents worden van begin tot eind getraced en een geautomatiseerde evaluatieset met succespercentagescoring draait bij elke wijziging. Prompt-injectie wordt behandeld als permanente dreiging met een gedefinieerde respons.
- **Niveau 4, Beheersen:** Het agentportfolio wordt gemeten en beheerst aan de hand van uitgangswaarden. Succespercentage per taak, slaagpercentage van injectieverdediging, kosten en aantal stappen per run, goedkeuringslatentie van mensen en lus- of faalincidenten worden als statistieken gevolgd. Drempels voor terugdraaien en stopzetten worden afgedwongen op dat bewijs in plaats van klachten. Budgetten per run op stappen, tijd en uitgaven worden bewaakt, en een regressie in enige statistiek triggert actie vóór schaal, niet na een incident.
- **Niveau 5, Orkestreren:** Autonomie wordt bij beleid afgestemd op taakrisico en continu bijgesteld naarmate resultaten binnenkomen. Doorlopende offline en online evaluatie koppelt agentgedrag aan bedrijfsuitkomsten, en de organisatie schaft agents routinematig af, bakent ze opnieuw af of geeft ze nieuwe rechten naarmate het risicobeeld verschuift. Tracing, kostenbudgetten en auditsporen zijn uniform over het portfolio. Verdedigingen tegen injectie en confused deputy worden adversarieel getest. Verantwoording voor autonome acties is helder en controleerbaar.

## Ideeën voor discussie

1. Welke van je huidige LLM-functies zijn stilletjes agents geworden, en is de autonomie van elk met opzet begrensd?
2. Wat is voor elke agenttool de goedkoopste manier waarop een aanvaller haar kan misbruiken via geïnjecteerde content, en wat belet dat?
3. Waar heb je multi-agentontwerpen gekozen, en kun je aantonen dat de coördinatiekosten zich terugbetaalden tegenover een enkele agent?
4. Welke agentacties zijn echt onomkeerbaar, en zou elk ervan kunnen worden herontworpen tot omkeerbaar of klaargezet?
5. Als een agent morgen een schadelijke actie nam, kon je dan precies reconstrueren wat hij deed en wie verantwoordelijk was?

## Belangrijkste inzichten

- Een agent is een LLM in een lus met tools, geheugen en een doel. Het risico leeft in de lus en de tools, niet in de tekst.
- Geef de voorkeur aan een vaste workflow wanneer de stappen bekend zijn. Reserveer autonomie voor werkelijk open doelen en begrens haar strak.
- Toolgebruik is het kernvermogen. Geef elke tool minste privilege, een gevalideerd schema en een sandbox.
- Poort ingrijpende en onomkeerbare acties achter een mens met echt gezag, en ontwerp voor goedkoop terugdraaien.
- Behandel agents als vijandig: verdedig tegen prompt-injectie en confused-deputymisbruik (hoofdstuk 4.2).
- Evalueer op taaksuccespercentage over veel runs, en trace elke run voor debuggen, kostenbeheersing en audit (hoofdstuk 6.5 en 6.6).
- Vaak is het juiste antwoord helemaal geen agent bouwen.

## Referenties en verder lezen

- Shunyu Yao et al., *ReAct: Synergising Reasoning and Acting in Language Models*.
- Timo Schick et al., *Toolformer: Language Models Can Teach Themselves to Use Tools*.
- Anthropic, *Building Effective Agents* (engineering guidance on workflows versus agents).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications* (including prompt injection and excessive agency).
- Simon Willison, writing on prompt injection and the "lethal trifecta" for AI agents.
- Norman Hardy, *The Confused Deputy* (the classic statement of the confused-deputy problem).
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach* (intelligent agents and rational action).
