# 6.3 Generatieve AI en LLM-toepassingen

## Overzicht en motivatie

[Generatieve AI](https://en.wikipedia.org/wiki/Generative_artificial_intelligence), en [grote taalmodellen](https://en.wikipedia.org/wiki/Large_language_model) (LLM's) in het bijzonder, kunnen vloeiende tekst, code, samenvattingen en gestructureerde data produceren uit instructies in natuurlijke taal. Dat maakt ze krachtige bouwstenen voor assistenten, zoeken, documentverwerking en automatisering. Maar die sterktes komen met een eigen risicoprofiel. LLM's zijn probabilistisch. Ze kunnen zelfverzekerde onwaarheden produceren ([hallucinaties](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))). Ze zijn gevoelig voor hoe je ze prompt. En ze openen nieuwe aanvalsoppervlakken zoals [prompt-injectie](https://en.wikipedia.org/wiki/Prompt_injection) (kwaadwillende instructies in invoer gesmokkeld om het gedrag van het model te kapen). Dus betrouwbare LLM-applicaties bouwen gaat minder over het model en meer over de engineering eromheen: hoe je context aanlevert, antwoorden grondt in vertrouwde kennis, uitvoer beperkt en kwaliteit evalueert.

Voor grote teams vragen LLM-applicaties om nieuwe patronen die verschillen van zowel traditionele software als klassieke machine learning. Er is vaak geen trainingsstap. In plaats daarvan wordt gedrag gevormd door prompts, opgehaalde context, tooldefinities en vangrails (runtimecontroles die de invoer en uitvoer van het model begrenzen). Dat verschuift de engineeringinspanning naar contextbeheer, retrievalkwaliteit, orkestratie en evaluatie. Ondernemingen die LLM's op schaal adopteren hebben gedeelde patronen nodig zodat niet elk team dezelfde faalwijzen op de harde manier herontdekt.

Overheids- en gereguleerde organisaties staan voor extra eisen. Een LLM die een beleidscitaat verzint of gevoelige data lekt is niet slechts een bug. Het kan een juridisch of veiligheidsincident zijn. Deze omgevingen vragen grounding in gezaghebbende bronnen, strikte uitvoervalidatie, menselijk toezicht voor ingrijpende uitvoer en heldere registraties van wat het systeem werd gevraagd en wat het produceerde. De technieken in dit hoofdstuk (retrieval-augmented generation, vangrails en rigoureuze evaluatie) maken LLM's veilig genoeg om in contexten met hoge inzet te deployen. De Claude-modellen van Anthropic zijn één toonaangevende optie onder meerdere capabele aanbieders. De praktijken hier gelden ongeacht welk model je kiest.

## Kernprincipes

- Grond het model in vertrouwde kennis in plaats van te leunen op wat het memoriseerde.
- Behandel prompts en context als geëngineerde, geversioneerde artefacten, niet als wegwerpstrings.
- Neem aan dat het model fout kan zijn of gemanipuleerd. Valideer uitvoer en beperk acties.
- Geef het model alleen de context en tools die het nodig heeft, niet meer, om fouten en aanvalsoppervlak te verkleinen.
- Evalueer continu met offline testsets, online statistieken en menselijk oordeel.
- Houd mensen in de lus voor ingrijpende uitvoer.
- Ontwerp voor het model als onbetrouwbare component binnen een vertrouwd systeem.

## Aanbevelingen

### Engineer prompts en beheer context bewust

Behandel prompts als code: sla ze op in versiebeheer, beoordeel wijzigingen en test ze tegen een suite voorbeelden. Structureer elke prompt helder: rol en taak, beperkingen, opmaakeisen en voorbeelden waar ze helpen. Behandel het contextvenster (de vaste tekstspanne die het model in één keer kan overwegen) als schaarse bron. Neem de meest relevante informatie op, orden haar doordacht en haal ruis weg, omdat irrelevante of overmatige context de kwaliteit verlaagt en kosten verhoogt. Beheer bij toepassingen met meerdere beurten de gespreksstatus expliciet, geschiedenis samenvattend of inkortend om binnen de limieten te blijven terwijl je behoudt wat ertoe doet. Geef de voorkeur aan heldere instructies en few-shotvoorbeelden (een handvol uitgewerkte demonstraties in de prompt) boven uitgebreide trucs die breken zodra een model verandert.

### Grond antwoorden met retrieval-augmented generation (RAG)

Haal voor kennisintensieve taken relevante documenten op uit een vertrouwd corpus en lever ze als context aan het model, het zeggend alleen uit dat materiaal te antwoorden en zijn bronnen te citeren. RAG houdt kennis actueel zonder hertraining, beperkt antwoorden tot goedgekeurde content en maakt citatie en verificatie mogelijk. Investeer in retrievalkwaliteit: knip documenten verstandig in stukken, kies [embeddings](https://en.wikipedia.org/wiki/Word_embedding) (numerieke vectorrepresentaties die vergelijkbare betekenissen dicht bij elkaar plaatsen) die bij je domein passen en controleer of de opgehaalde passages werkelijk het antwoord bevatten, want een vloeiend antwoord gebouwd op de verkeerde passage is erger dan geen antwoord. En wanneer niets relevants opduikt, laat het systeem dat dan zeggen in plaats van content te verzinnen.

### Bouw agents en toolgebruik met terughoudendheid

LLM's kunnen tools aanroepen (zoeken, databases, rekenmachines, interne API's) en kunnen worden samengesteld tot agents die over meerdere stappen plannen en handelen. Dit voegt echt vermogen toe, maar het vermenigvuldigt ook risico: elke tool is nog een manier waarop een fout of gemanipuleerd model schade kan veroorzaken. Definieer tools met precieze schema's, valideer elk argument, pas minste privilege toe en eis bevestiging of menselijke goedkeuring voor ingrijpende acties zoals communicatie versturen of geld verplaatsen. Houd agentlussen begrensd, observeerbaar en onderbreekbaar. Begin met strak afgebakende tools voor één doel voordat je naar open autonomie grijpt.

### Voeg vangrails toe en valideer uitvoer

Wikkel het model in lagen van verdediging. Filter en detecteer aan de invoerkant prompt-injectie, vooral wanneer onbetrouwbare content (webpagina's, gebruikersdocumenten) in de context komt. Valideer aan de uitvoerkant structuur tegen een schema, controleer beweringen tegen bronnen, filter onveilige of niet-conforme content en wijs af of probeer opnieuw wanneer validatie faalt. Parseer en verifieer voor gestructureerde uitvoer in plaats van de opmaak van het model te vertrouwen. Laat ruwe modeluitvoer nooit onomkeerbare acties triggeren zonder validatie. Behandel hallucinatiebeperking als systeemeigenschap die je bereikt via grounding, citatie, validatie en menselijke review, niet iets wat het model zelf beheert.

### Evalueer offline, online en met mensen

Bouw een evaluatiesuite van representatieve invoer met bekend-goede of volgens rubriek gescoorde uitvoer en draai haar bij elke prompt- of modelwijziging (offline evaluatie). Meet echt gedrag in productie met statistieken als taaksucces, escalatiepercentage en gebruikersfeedback (online evaluatie). Gebruik voor subjectieve kwaliteit menselijke reviewers en, voorzichtig, modelgebaseerde beoordeling. Evaluatie is het vangnet waarmee je prompts en modellen met vertrouwen kunt wijzigen. Zonder haar vlieg je blind.

## Afwegingen: voor- en nadelen

| Keuze | Voordelen | Nadelen | Het best wanneer |
|---|---|---|---|
| Puur prompten | Eenvoudig, snel, goedkoop te wijzigen | Beperkte grounding, kan hallucineren | Brede taken, lage inzet |
| RAG | Actueel, gegrond, citeerbaar | Retrieval is moeilijk goed te krijgen | Kennisrijke, feitelijke taken |
| Agents met tools | Krachtig, kan handelen | Groter aanvalsoppervlak, moeilijker te beheersen | Goed afgebakende automatisering met vangrails |
| Groter, sterker model | Betere kwaliteit en redenering | Hogere kosten en latentie | Complexe taken of taken met hoge inzet |
| Kleiner, goedkoper model | Snel en goedkoop | Zwakker bij moeilijke taken | Groot volume, eenvoudige taken |

De kernspanning is vermogen tegenover controle en kosten. Meer autonomie en grotere modellen leveren meer waarde, maar vragen meer vangrails, meer evaluatie en meer geld. Grounding via RAG verbetert betrouwbaarheid tegen de kosten van retrievalengineering. De juiste balans hangt af van de inzet: toepassingen met hoge inzet neigen naar grounding, validatie en menselijk toezicht, ook als dat meer kost.

## Vragen om met je team te bespreken

1. **Welke lat voor nauwkeurigheid en grounding moet een LLM-functie halen voordat ze het publiek ziet, en wie tekent af?** Een vloeiend antwoord dat de verkeerde bron citeert of een beleid verzint is erger dan geen antwoord, en bij de overheid is een verzonnen citaat een juridisch incident, geen bug. Voor een groot team voorkomt een expliciete lat dat elke groep op gevoel een eigen privédrempel zet. Neem je definitie van "gegrond genoeg" mee: of elke bewering herleidbaar moet zijn tot een opgehaalde, geverifieerde bron, of het systeem moet weigeren wanneer retrieval leeg blijft en wat je adversariële evaluatieset werkelijk dekt. Het signaal om op te letten is of iemand nu een promptwijziging rechtstreeks naar gebruikers kan sturen zonder regressierun. Als de inzet juridisch of veiligheidsgerelateerd is, moet het antwoord de uitvoer met het hoogste risico vóór release door een menselijke reviewer met echt gezag leiden.

2. **Welke van onze LLM-functies zijn stiekem agents, en heeft elke tool minste privilege gekregen en een menselijke poort op onomkeerbare acties?** Elke functie die het model tools laat aanroepen of over meerdere stappen laat handelen is agentterrein ingegaan, en elke tool is nog een manier waarop een fout of gemanipuleerd model schade veroorzaakt. Voor ondernemingen die LLM's aan interne API's bedraden brengt deze vraag risico naar boven dat een etiket "eenvoudige assistent" verbergt. Neem een inventaris mee van elke tool die het model kan aanroepen, haar argumentvalidatie, haar privilegebereik en welke acties (communicatie versturen, geld verplaatsen, dossiers wijzigen) bevestiging vereisen. Bespreek of agentlussen begrensd, observeerbaar en onderbreekbaar zijn. Het antwoord moet bereiken aanscherpen en menselijke goedkeuringspoorten toevoegen waar een ingrijpende of onomkeerbare actie nu zonder bereikbaar is.

3. **Hoe zouden we binnen een dag weten dat onze retrievalkwaliteit is gedaald, gegeven dat een zelfverzekerd antwoord gebouwd op de verkeerde passage er prima uitziet?** RAG maakt antwoorden alleen betrouwbaar wanneer retrieval werkelijk de passage naar boven haalt die het antwoord bevat, en retrieval rot stilletjes naarmate documenten veranderen, stukken verouderen of embeddings van je domein afdrijven. Omdat het model nog steeds vloeiend over slechte context schrijft, klagen gebruikers mogelijk pas wanneer vertrouwen al verloren is. Neem je huidige metingen van retrievallatentie en recall mee, hoe je controleert of opgehaalde passages werkelijk het antwoord bevatten en hoe indexversheid gelijke tred houdt met documentwijzigingen. Bespreek bij toepassingen met hoge inzet of publiek bereik het loggen van opgehaalde bronnen voor audit, zodat je een slecht antwoord kunt herleiden tot zijn slechte passage. Als je helemaal geen retrievalevaluatie hebt, grond je op geloof.

4. **Behandelen we prompts, context en evaluatiesets als geversioneerde, beoordeelde artefacten, of als strings verspreid over notebooks en chatlogs?** Wanneer prompts ongeversioneerd en gedupliceerd over teams uitwaaieren, bereikt een reparatie op de ene plek de andere nooit, en kan niemand reproduceren wat het systeem vorig kwartaal werd gevraagd te doen. Voor een groot team laten een gedeeld promptregister en een regressiesuite die bij elke wijziging draait je een model verwisselen of een instructie bewerken zonder stilletjes een functie twee teams verderop te breken. De concurrerende trek is snelheid, omdat engineers het snelst itereren wanneer ze een prompt plakken en opleveren, dus spreek af waar de lijn ligt tussen snelle experimenten en alles wat gebruikers raakt. Neem mee waar je prompts vandaag werkelijk leven, of een evaluatieset wijzigingen poort en hoe je het retrievalcorpus naast de prompt versioneert. Voeg in omgevingen van onderneming en overheid de auditeis toe: je moet misschien maanden later exact kunnen tonen welke prompt en welke bronnen een gegeven uitvoer produceerden, en een prompt die je niet kunt reconstrueren is een registratie die je niet kunt verdedigen.

5. **Hoe beheersen we inferentiekosten naarmate het volume groeit zonder stilletjes de kwaliteit te degraderen, en wie bezit de modelkeuzebeslissing?** De TCO voor LLM-functies wordt gedomineerd door inferentie per aanroep, en kosten die in een pilot triviaal lijken stapelen zich snel op in productieschaal, wat teams verleidt stilletjes naar een zwakker model te zakken in de hoop dat niemand het kwaliteitsverval merkt. Voor een grote organisatie levert elk team modellen en kostenlimieten op gevoel laten kiezen zowel verrassende rekeningen als inconsistente kwaliteit op. De echte afweging is vermogen tegenover kosten en latentie: een groter model redeneert beter bij moeilijke taken, een kleiner is goedkoper en sneller bij eenvoudige, en caching, routering en retrievalbereik bewegen allemaal het getal. Neem kosten per opgeloste taak mee, kwaliteit per modelklasse op je evaluatieset en waar prompt- of contextopzwelling de tokenuitgaven opblaast. Noem bij begroten in onderneming en overheid wie de modelkeuze en het uitgavenplafond goedkeurt, want een kostenpost die niemand bezit is er een die niemand beheerst wanneer het verkeer verdrievoudigt.

6. **Welke gevoelige data kan het model bereiken, waar gaat die data heen en kunnen we bewijzen dat ze binnen de grenzen bleef?** Elke prompt, opgehaald document en toolresultaat kan persoonlijke of vertrouwelijke data in het model dragen en, bij een gehoste aanbieder, buiten je perimeter, en een lek hier is een juridisch of veiligheidsincident, geen defectticket. Voor een groot team dat LLM's aan interne systemen bedraadt zit het risico verborgen in de leidingen: een retrievalcorpus dat records bevat die een gegeven gebruiker nooit mag zien, of logs die ruwe invoer vastleggen. De spanning is vermogen tegenover blootstelling, aangezien redactie en strakke afbakening de functie kunnen afstompen die je probeert te bouwen. Neem een datastroomkaart mee van wat de context binnenkomt, de bewaar- en trainingsvoorwaarden van de aanbieder en hoe je gevoelige velden redigeert, afbakent en logt. Koppel dit in gereguleerde en publieke omgevingen aan regels voor dataresidentie, archiefbewaarplichten en contractuele grenzen aan hoe een leverancier je data mag gebruiken, want toezicht dat je niet kunt bewijzen is toezicht dat je niet hebt.

## Sectorperspectief

**Startup.** Lever één smalle LLM-functie op die je kernwaarde raakt, gebouwd op een gehost model met retrieval over je eigen content, en houd prompts in git achter een dunne interface zodat je van aanbieder kunt wisselen. Draai vóór elke wijziging een klein evaluatiebestand met echte vragen, filter geplakte gebruikerstekst om prompt-injectie af te stompen en begrens de maandelijkse uitgaven hard. Weersta agents en zelf hosten: een onbegrensde toolaanroeplus die je niet kunt superviseren is een verplichting, geen demo.

**Kleinbedrijf.** Je hebt waarschijnlijk geen ML-specialist, dus koop LLM-functies ingebed in tools die je al gebruikt in plaats van een bouw te bemannen. Formuleer het risico als gewone vraag: waar zou een zelfverzekerd fout antwoord je een klant kosten, en wie controleert de uitvoer voordat die naar buiten gaat. Geef de voorkeur aan leveranciers die hun bronnen tonen, je een mens in de lus laten houden en de AI makkelijk uit te zetten maken wanneer ze zich misdraagt.

**Grote onderneming.** Het probleem is schaal over veel teams: publiceer gedeelde patronen voor RAG, vangrails en toolschema's, plus een gemeenschappelijk evaluatiekader en promptregister zodat elke groep ophoudt dezelfde faalwijzen te herontdekken. Begroot inferentiekosten en menselijke review expliciet, standaardiseer de interfacelaag zodat modellen verwisselbaar blijven en bestuur agents centraal met minste privilege, begrensde lussen en auditlogging. Beheer LLM-functies als portfolio met statistieken en stopcriteria, niet een verstrooiing van pilots.

**Overheid.** Transparantie, aanbestedingsregels en verantwoording geven elke keuze vorm. Grond strikt in goedgekeurde bronnen met citaten, weiger wanneer retrieval leeg blijft en verbied het model wet te stellen die het niet kan citeren. Houd een verantwoordelijke functionaris ingrijpende uitvoer laten beoordelen, log invoer en opgehaalde bronnen voor audit, draai vóór elke release een adversariële evaluatieset en eis bekendmaking van modelbeperkingen en gegevensverwerkingsvoorwaarden in het contract.

## Voorbeelden

**Startup.** Een startup van drie personen in ontwikkelaarstools voegde een chathulp over haar eigen documentatie toe zodat gebruikers konden ophouden basisvragen te mailen. Ze gebruikte RAG zodat elk antwoord een specifieke documentpagina citeerde, instrueerde het model "ik weet het niet zeker, hier is wie je kunt vragen" te zeggen wanneer retrieval leeg bleef en hield haar prompts in git. Vóór elke wijziging draaide ze de prompts tegen een klein bestand echte gebruikersvragen om regressies te vangen, en ze filterde door gebruikers geplakte tekst om prompt-injectie af te stompen. De hulp handelde de gangbare vragen af en gaf de rest stilletjes door aan de gedeelde inbox van de oprichters.

**Grote onderneming.** Een softwarebedrijf bouwde een interne supportassistent over haar productdocumentatie. Het gebruikte [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) zodat antwoorden specifieke documentpagina's citeren, zei het model "ik weet het niet" te zeggen wanneer retrieval faalde en verifieerde dat elke geciteerde bron werkelijk bestond. Prompts stonden in versiebeheer en werden bij elke wijziging getest tegen een suite echte supportvragen. De assistent deflecteerde routinetickets en escaleerde alles met lage zekerheid naar menselijke medewerkers, terwijl online statistieken oplossings- en correctiepercentages volgden.

**Overheid.** Een publieke instantie deployde een LLM-assistent om medewerkers te helpen antwoorden op burgervragen op te stellen. Grounding was strikt: het model kon alleen antwoorden samenstellen uit goedgekeurde richtlijnen met citaten, en het was verboden beleid te stellen dat niet in de opgehaalde bronnen stond. Een verantwoordelijke functionaris beoordeelde elk concept voordat het naar buiten ging. Invoerfiltering beschermde tegen prompt-injectie uit door burgers ingediende documenten, uitvoer werd gelogd voor audit en een evaluatieset van adversariële en randgevalvragen draaide vóór elke release om te bevestigen dat het systeem weigerde te speculeren over juridische kwesties.

## Zakelijke onderbouwing: motivatie, ROI en TCO

LLM-applicaties leveren ROI door taalzwaar werk te automatiseren: vragen beantwoorden, documenten samenvatten, content opstellen en structuur uit ongestructureerde tekst halen. Waarde toont zich als gedeflecteerde tickets, sneller opstellen, minder handmatige review en nieuwe self-servicevermogens. Omdat er vaak geen trainingsstap is, is de tijd tot eerste waarde kort, een grote aantrekkingskracht.

De TCO wordt echter gedomineerd door doorlopende inferentiekosten, retrievalinfrastructuur, evaluatiepijplijnen, vangrailsystemen en menselijke review. Kosten per aanroep lopen op schaal snel op, en een onbewaakte applicatie kan afdrijven naar onveilig of duur gedrag. De kosten van niet adopteren zijn achterblijven in servicekwaliteit en personeelsproductiviteit. De kosten van onzorgvuldig adopteren zijn een publiek hallucinatie-incident of een datalek. Maak de zaak voor het bestuur door een concreet productiviteitsdoel te koppelen aan een concreet veiligheids- en evaluatieplan, en door te begroten voor de vangrails en het menselijk toezicht die de waarde duurzaam houden.

## Antipatronen en valkuilen

- **Vloeiende uitvoer vertrouwen.** Zelfverzekerde, goed geschreven tekst aanzien voor correcte tekst.
- **RAG zonder retrievalevaluatie.** Aannemen dat retrieval werkt en nooit controleren of ze de juiste passages naar boven haalt.
- **Blindheid voor prompt-injectie.** Onbetrouwbare content in prompts voeden zonder verdediging.
- **Onbegrensde agents.** Agents ingrijpende acties laten nemen zonder limieten of menselijke goedkeuring.
- **Geen evaluatiekader.** Prompts en modellen op gevoel wijzigen, zonder regressietesten.
- **Promptwildgroei.** Prompts verspreid, ongeversioneerd en gedupliceerd over teams.
- **Over-automatisering.** Mensen verwijderen uit beslissingen die juridisch of veiligheidsgewicht dragen.

## Volwassenheidsmodel

1. **Initiëren.** Ad hoc prompten in geïsoleerde projecten. Geen grounding, vangrails of evaluatie. Prompts leven waar iemand ze plakte, en hallucinaties worden in productie ontdekt.
2. **Ontwikkelen.** Sommige teams voegen RAG en promptversiebeheer toe, basisuitvoervalidatie en een kleine handmatige evaluatieset, maar praktijken verschillen per team en rusten op individuele kampioenen in plaats van gedeelde verwachting.
3. **Standaardiseren.** Gedocumenteerde patronen voor RAG, vangrails, toolschema's en promptversiebeheer worden organisatiebreed afgedwongen. Geautomatiseerde offline evaluatie draait bij elke prompt- of modelwijziging. Stromen met hoge inzet dragen online statistieken en menselijke review.
4. **Beheersen.** Het portfolio wordt gemeten aan de hand van uitgangswaarden: retrievalrecall, hallucinatie- en weigeringspercentages, dekking van injectieverdediging, kosten en latentie per aanroep en escalatie- en correctiepercentages worden op dashboards gevolgd. Releasepoorten en stopcriteria slaan aan op bewijs in plaats van mening, en een regressierun blokkeert elke wijziging die een statistiek de verkeerde kant op beweegt.
5. **Orkestreren.** Continue offline en online evaluatie is gekoppeld aan bedrijfsuitkomsten. Injectieverdedigingen, agents en grounding zijn bestuurd en observeerbaar. De organisatie schaft LLM-functies routinematig af, stemt ze opnieuw af en bakent ze opnieuw af, en wisselt modellen naarmate kwaliteit, kosten en risico verschuiven.

## Ideeën voor discussie

- Hoe beslis je welke uitvoer menselijke review vereist vóór gebruik?
- Wat is je standaard voor "gegrond genoeg" voordat een antwoord aan gebruikers mag worden getoond?
- Hoe verdedig je tegen prompt-injectie wanneer onbetrouwbare content de context in moet?
- Wanneer is een agent het extra risico waard tegenover een eenvoudiger ontwerp met één aanroep?
- Hoe evalueer je subjectieve kwaliteit op schaal zonder te veel te leunen op modelgebaseerde beoordeling?
- Hoe houd je prompts onderhoudbaar en consistent over veel teams?

## Belangrijkste inzichten

- Betrouwbaarheid komt uit de engineering rond het model: context, grounding, vangrails en evaluatie.
- RAG grondt antwoorden in vertrouwde bronnen en maakt citatie en verificatie mogelijk.
- Behandel het model als onbetrouwbare component. Valideer uitvoer en beperk toolgebruik.
- Geef agents minste privilege, begrensde lussen en menselijke goedkeuring voor ingrijpende acties.
- Evalueer continu offline, online en met mensen. Het is wat verandering veilig maakt.

## Referenties en verder lezen

- Patrick Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*.
- Jason Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Anthropic, *Building Effective Agents* (engineering guidance).
- Louis-François Bouchard and Louie Peters, *Building LLMs for Production*.
