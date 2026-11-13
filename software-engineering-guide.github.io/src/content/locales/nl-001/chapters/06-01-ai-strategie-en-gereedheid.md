# 6.1 AI-strategie en gereedheid

## Overzicht en motivatie

[Kunstmatige intelligentie](https://en.wikipedia.org/wiki/Artificial_intelligence) is van onderzoeksnieuwtje uitgegroeid tot een kernvermogen dat grote organisaties nu geacht worden verantwoord en op schaal in te zetten. Voor ondernemingen en overheidsinstanties is de echte vraag niet langer of AI iets indrukwekkends kan doen in een demo. Het is of een specifieke investering een echt probleem beter oplost dan de alternatieven, jarenlang veilig kan worden beheerd en audit, aanbesteding en publieke toetsing kan overleven. AI-strategie is de discipline van beslissen waar je AI toepast, waar je het vermijdt en welke fundamenten je nodig hebt voordat het eerste model productie bereikt.

Voor grote teams verhogen schaal en traagheid de inzet. Een slecht geformuleerd initiatief kan budgetten verbranden, getalenteerde engineers afleiden en vertrouwen bij toezichthouders en burgers eroderen wanneer het publiekelijk faalt. Een goed gekozen initiatief kan sleurwerk automatiseren, inzicht boven water halen uit data die je nooit eerder kon bereiken en vaardige mensen vrijmaken voor werk met hogere waarde. Het verschil is zelden het model zelf. Het komt neer op hoe goed je het probleem formuleert, hoe gereed je data en talent zijn en hoe eerlijk je businesscase is.

Overheids- en gereguleerde contexten voegen meer beperkingen toe. Publieke organen moeten uitgaven rechtvaardigen, transparantie garanderen, onwettige discriminatie vermijden en verantwoording afleggen aan gekozen functionarissen en het publiek. Aanbestedingsregels kunnen lock-in bij één leverancier verbieden, uitlegbaarheid eisen en vereisen dat leveranciers modelgedrag openbaar maken. Behandel hier compliance, controleerbaarheid en exitopties als eersterangs eisen, niet als bijgedachten.

## Kernprincipes

- Begin bij een probleem dat het oplossen waard is, niet bij een technologie op zoek naar een toepassing.
- Geef de voorkeur aan de eenvoudigste aanpak die aan de behoefte voldoet. AI is één optie onder veel, en vaak niet de beste.
- Behandel gereedheid van data, talent en platformvolwassenheid als voorwaarden, niet als parallelle werkstromen die je later uitzoekt.
- Neem beslissingen over bouwen of kopen expliciet en herzie ze naarmate de markt en je vermogens veranderen.
- Kwantificeer de total cost of ownership, inclusief beheer, bewaking en uiteindelijke vervanging, niet alleen de licentie of de pilot.
- Ontwerp vanaf dag één voor exit: vermijd architecturen die wisselen van leverancier of model onbetaalbaar duur maken.
- Behandel in gereguleerde en publieke omgevingen transparantie, aanbestedingscompliance en verantwoording als ontwerpbeperkingen.
- Meet de kosten van *niet* handelen naast de kosten van handelen.

## Aanbevelingen

### Formuleer het probleem voordat je een technologie kiest

Schrijf een probleemstelling van één pagina. Noem de beslissing of taak die je wilt verbeteren, de huidige uitgangswaarde, de meetbare uitkomst die je wilt en wat er gebeurt wanneer het systeem het fout heeft. Vraag dan of het probleem überhaupt bij AI past. Is er genoeg relevante data? Is de taak patroongebaseerd in plaats van regelgebaseerd? Kun je probabilistische antwoorden verdragen? Kan een mens de uitvoer controleren? Veel problemen worden beter opgelost met deterministische software, beter procesontwerp of simpelweg betere datahygiëne. Schrijf expliciet op waar AI *niet* goed past: bijvoorbeeld beslissingen die bij wet perfect uitlegbaar moeten zijn, of waar de kosten van een zeldzame fout catastrofaal zijn en onmogelijk te vangen.

### Gebruik een beslisboom van bouwen, kopen, fine-tunen en prompten

Beweeg van goedkoopst en snelst naar duurst en meest beheerst:

1. **Prompt een bestaand gehost model.** Als een algemeen model (zoals Claude van Anthropic, of vergelijkbare aanbiedingen van andere aanbieders) het probleem oplost met zorgvuldig prompten en retrieval, doe dat dan eerst. Laagste kosten, snelste iteratie, geen trainingsinfrastructuur.
2. **Vul aan met retrieval of tools.** Als het gat kennis of acties is, voeg dan [retrieval-augmented generation](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (RAG) toe, dat relevante documenten op querytijd ophaalt en als context aan het model geeft, en toolgebruik voordat je de modelgewichten aanraakt.
3. **Fine-tune of pas aan.** Als prompten de benodigde nauwkeurigheid, toon of opmaak niet consistent kan bereiken, [fine-tune](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)) dan een kleiner model op je data: dat wil zeggen een voorgetraind model verder trainen op jouw voorbeelden om het te specialiseren. Dit koopt controle tegen de kosten van een [MLOps](https://en.wikipedia.org/wiki/MLOps)-pijplijn (machine learning operations).
4. **Koop een gespecialiseerd product.** Voor goed gedefinieerde domeinen (documentverwerking, fraudescoring) kan een volwassen leveranciersproduct alles verslaan wat je bouwt.
5. **Bouw van nul.** Reserveer het trainen van [foundation models](https://en.wikipedia.org/wiki/Foundation_model) (grote modellen voorgetraind op brede data en aanpasbaar aan veel taken) voor organisaties met unieke data, diep talent en strategische redenen. Voor bijna alle ondernemingen en instanties is dit de verkeerde keuze.

### Stel voorwaarden voor data, talent en platform vast

Audit je data op beschikbaarheid, kwaliteit, labeling, herkomst en rechtsgrond voor gebruik. Bevestig dat je het recht hebt ze voor AI te gebruiken, inclusief alle persoonlijke of derdendata. Beoordeel talent eerlijk: je hebt datawetenschappers nodig, en ook ML-engineers, data-engineers, productmanagers die probabilistische systemen begrijpen en reviewers die uitvoer kunnen evalueren. Zet voordat je opschaalt een platformbasis op: experimenttracking, een modelregister (het systeem van registratie voor getrainde modelversies en hun goedkeuringsstatus), bewaking en beveiligde serving, zodat elk nieuw gebruiksgeval de operaties niet opnieuw uitvindt.

### Ga bewust om met gereguleerde en overheidscontexten

Betrek aanbesteding, juristen en risicoteams vroeg. Eis dat leveranciers de herkomst van modellen, trainingsdatapraktijken, evaluatieresultaten en bekende beperkingen bekendmaken. Geef de voorkeur aan contracten die overdraagbaarheid van je data en prompts verlenen, en vermijd bedrijfseigen formaten die je vastzetten. Publiceer waar passend het doel en de waarborgen van publiek gerichte AI-systemen, en geef mensen een kanaal om geautomatiseerde beslissingen te betwisten. Sluit aan op erkende raamwerken (zie hoofdstuk 6.5) zodat audits een gedocumenteerd, verdedigbaar proces vinden.

### Bereken de total cost of ownership en bewaak tegen lock-in

Modelleer de kosten over de volledige levenscyclus: inferentie of licenties, datapijplijnen, menselijke review, bewaking, hertraining, incidentrespons en buitengebruikstelling. Vergelijk ze met de kosten van de status quo en van de alternatieven. Verminder lock-in door het model achter een interne interface te zetten, prompts en evaluatiedatasets overdraagbaar te houden en af en toe een tweede aanbieder te testen.

## Afwegingen: voor- en nadelen

| Aanpak | Voordelen | Nadelen | Het best wanneer |
|---|---|---|---|
| Gehost model prompten | Snel, goedkoop, geen infra, makkelijk te wisselen | Minder controle, kosten per aanroep, vragen over datadeling | Prototypes, brede taken, onzekere eisen |
| Retrievalaanvulling | Grondt antwoorden in je data, bij te werken | Retrievalkwaliteit is moeilijk, voegt infra toe | Kennisrijke taken |
| Kleiner model fine-tunen | Controle, lagere kosten per aanroep op schaal, on-prem-optie | Vraagt MLOps, data en onderhoud | Stabiele, grootvolume, gespecialiseerde taken |
| Een product kopen | Bewezen, ondersteund, snel tot waarde | Licentiekosten, lock-in, beperkte pasvorm | Goed gedefinieerde standaardproblemen |
| Foundation model bouwen | Maximale controle en onderscheid | Enorme kosten, zeldzaam talent, hoog risico | Bijna nooit, buiten frontier-laboratoria |

De dominante afweging is controle tegenover kosten en snelheid. Prompten geeft je de meeste snelheid en flexibiliteit maar de minste controle. Bouwen geeft je de meeste controle maar vraagt middelen die weinig organisaties zouden moeten uitgeven. De meeste grote teams horen in het midden te leven: eerst prompten en ophalen, selectief fine-tunen en kopen voor standaardbehoeften. Lock-in ruilt kortetermijngemak tegen langetermijnrisico, en dat telt vooral bij de overheid, waar meerjarige exitverplichtingen gangbaar zijn.

## Vragen om met je team te bespreken

1. **Waar staat elk van onze drie topkandidaten voor gebruiksgevallen op de ladder van prompten, dan ophalen, dan fine-tunen, dan kopen, dan bouwen, en welk bewijs zou het een trede verplaatsen?** Dit telt omdat de meeste verspilde AI-uitgaven komen van een trede te hoog beginnen: een model trainen terwijl zorgvuldig prompten had gewerkt. Voor een groot team voorkomt de ladder als gedeelde standaard afspreken dat elke groep een dure pijplijn opnieuw uitvindt. Neem de probleemstelling van één pagina voor elke kandidaat mee, de huidige uitgangswaarde en een eerlijke lezing of het gat kennis is (retrieval), consistentie (fine-tunen) of een opgelost standaardprobleem (kopen). Voeg in omgevingen van onderneming en overheid de aanbestedings- en auditkosten van elke trede toe, aangezien een gefinetuned model een MLOps-last meesleept die een gehoste aanroep niet heeft. Het antwoord moet je in de kamer ten minste één te ruim afgebakend project laten schrappen of terugschalen.

2. **Wat is ons concrete exitplan voor de leverancier of het model waarvan we het meest afhangen, en hebben we het werkelijk getest?** Lock-in is goedkoop te accepteren en duur terug te draaien, en bij de overheid kun je meerjarige exitverplichtingen dragen die je niet kunt nakomen als je nooit hebt gerepeteerd. Neem de lijst bedrijfseigen functies mee waarop je leunt, of prompts en evaluatiedatasets overdraagbaar zijn en hoe het model achter een interne interface zit (of niet). Het signaal om op te letten is of iemand ooit je evaluatiesuite tegen een tweede aanbieder heeft gedraaid. Zo niet, dan is je exitplan een hoop, geen plan. Als het eerlijke antwoord is dat wisselen maanden zou duren en kerncode herschrijven, behandel dat dan als ontwerpdefect om nu te repareren, geen brug om later over te steken.

3. **Wat zegt een eerlijke gereedheidsscorekaart over onze datarechten, en welke gebruiksgevallen diskwalificeert ze vandaag?** Datagereedheid overslaan is het falen dat pilots stilletjes laat zinken: het model werkt, maar je had nooit de rechtsgrond om de data te gebruiken, of ze is niet gelabeld en zonder herkomst. Voor een grote organisatie leggen persoonlijke en derdendata toestemmings- en contractuele grenzen op die per jurisdictie en per dataset verschillen. Neem een audit mee van beschikbaarheid, kwaliteit, labeling, herkomst en rechtsgrond voor elke kandidaat, en wees bereid sommige gebruiksgevallen als geblokkeerd te markeren tot de datafundamenten bestaan. In gereguleerde en publieke omgevingen is een onbruikbare rechtsgrond geen vertraging maar een harde stop, en het gereedheidswerk financieren moet een expliciete regel in het plan zijn in plaats van een bijgedachte.

4. **Hoe weten we dat een live AI-gebruiksgeval werkelijk werkt, en welk bewijs zou ons het doen stopzetten?** De meeste AI-portfolio's verzamelen zombies: pilots die live gingen, iemand imponeerden en nu eeuwig draaien zonder dat iemand controleert of ze hun kosten nog verdienen. Spreek de uitgangswaarde en de succesmaatstaf af vóór de lancering, stel dan een expliciete stopdrempel vast, zodat de beslissing om te stoppen vooraf wordt genomen in plaats van in het moment verdedigd. Neem de huidige statistiek mee, de kosten van menselijk toezicht per uitkomst en de afdrijving die je sinds de lancering hebt gezien. Noem bij portfolio's van onderneming en overheid wie elk systeem volgens vast ritme beoordeelt en wie de bevoegdheid heeft het buiten dienst te stellen. Een gebruiksgeval waarvoor niemand verantwoordelijk is voor de review is er een dat niemand ooit uitzet.

5. **Waar blijft een mens in de lus, wat kost dat toezicht en hebben we het werkelijk begroot?** De goedkoopst ogende AI-gebruiksgevallen zijn degene die stilletjes volledige automatisering aannemen en dan kosten lekken door de review, correctie en escalatie die de realiteit terugdwingt. Besluit bewust welke beslissingen een persoon moet bevestigen, welke het model alleen mag nemen en welke het nooit mag nemen, en prijs dan de menselijke tijd die dat impliceert. Neem het volume lage-zekerheidsgevallen mee, de kosten van een fout antwoord en het huidige escalatiepad. Koppel in gereguleerde en publieke omgevingen elke geautomatiseerde beslissing aan een verantwoordelijke functionaris en een beroepsroute, want toezicht dat je niet kunt beschrijven is toezicht dat je niet hebt.

6. **Hebben we het talent en het platform om te draaien wat we voorstellen, of nemen we stilletjes capaciteit aan die we missen?** Ambitieuze AI-plannen falen minder op het model dan op de onglamoureuze fundamenten: niemand om de pijplijn te onderhouden, niemand die uitvoer kan evalueren, geen platform om op te deployen. Stem elk kandidaat-gebruiksgeval af op de vaardigheden en infrastructuur die het werkelijk nodig heeft, en wees eerlijk waar het gat een aanwerving is, een partner of een reden om niet te bouwen. Neem een inventaris mee van wie elk systeem in productie kan bezitten, op welk platform het zal draaien en welke vermogens je zou moeten kopen. Voeg voor een grote of publieke organisatie de doorlooptijden van aanbesteding en werving toe, aangezien een plan dat afhangt van talent dat je in het relevante venster niet kunt werven een plan is om te weinig te leveren.

## Sectorperspectief

**Startup.** Snelheid en overleven domineren. Kies één smal gebruiksgeval dat je kernwaarde raakt, lever het op een gehost model achter een dunne interface en begrens de uitgaven hard. Vermijd infrastructuur bouwen of modellen trainen: je schaarste middel is engineeringaandacht, en een gefinetunede pijplijn die je niet kunt onderhouden is een verplichting, geen gracht. Houd wisselen goedkoop zodat je een snel bewegende markt kunt volgen.

**Kleinbedrijf.** Je hebt waarschijnlijk geen datawetenschappers en een krap budget, dus behandel AI als iets wat je ingebed koopt in tools die je al gebruikt, niet als programma dat je bemant. Formuleer gereedheid als vraag over datahygiëne en privacy in plaats van een machine-learningproject: weet welke klantdata je bezit, wat je ermee mag doen en waar een fout geautomatiseerd antwoord je een klant zou kosten. Geef de voorkeur aan leveranciers die de AI optioneel, transparant en makkelijk uit te zetten maken.

**Grote onderneming.** Het probleem is portfoliogovernance over veel teams: een gedeelde ladder van bouwen of kopen, consistente gereedheidsbeoordelingen en analyse van lock-in en totale kosten zodat groepen ophouden dure pijplijnen opnieuw uit te vinden. Begroot de MLOps- en menselijketoezichtlast expliciet, standaardiseer de interfacelaag zodat aanbieders verwisselbaar blijven en beheer AI-gebruiksgevallen als portfolio met heldere statistieken en stopcriteria in plaats van een verstrooiing van pilots.

**Overheid.** Transparantie, aanbestedingsregels en verantwoording geven elke keuze vorm. Geef de voorkeur aan systemen die officiële bronnen citeren in plaats van beleid te genereren, houd een mens verantwoordelijk voor ingrijpende beslissingen en eis in contracten overdraagbaarheid van data en bekendmaking van modelbeperkingen. Publiceer een beschrijving in gewone taal en een beroepsroute, eer alle meerjarige exitverplichtingen die je ondertekent en houd AI buiten definitieve beoordelingsbeslissingen die bij een verantwoordelijke functionaris moeten liggen.

## Voorbeelden

**Startup.** Een planningsstartup van vijf personen wilde een natuurlijke-taalfunctie "boek een vergadering voor me" toevoegen zonder haar twee engineers van het kernproduct te halen. Ze koos het kleinste probleem dat telde, een verzoek omzetten in een voorgestelde tijd, en leverde het op met een gehost model achter een dunne interne API zodat ze later van aanbieder kon wisselen. Het team stelde een hard maandelijks uitgavenplafond in, volgde of gebruikers de voorgestelde tijden accepteerden en sprak af een gefinetuned model alleen te heroverwegen als het volume het extra werk ooit rechtvaardigde.

**Grote onderneming.** Een multinationale verzekeraar wilde schadetriage versnellen. In plaats van een maatwerkmodel te trainen kaderde ze het probleem smal (inkomende claims routeren en samenvatten), prototypte met een gehost model plus retrieval over haar polisdocumenten en mat tegen menselijke afhandeltijd en nauwkeurigheid. Pas nadat de waarde bewezen was fine-tunede ze een kleiner model voor het claimtype met het hoogste volume om kosten per aanroep te verlagen. Ze hield het model achter een interne API om van aanbieder te kunnen wisselen, en modelleerde een TCO over drie jaar die menselijke review van lage-zekerheidsgevallen omvatte.

**Overheid.** Een nationale belastingdienst overwoog een AI-assistent om medewerkers te helpen burgervragen te beantwoorden. Omdat die antwoorden wettelijke verplichtingen raakten, stond de dienst op transparantie: het systeem kon alleen officiële richtlijnen met bronvermelding naar boven halen, nooit beleid verzinnen, en een mens beoordeelde elke geautomatiseerde suggestie voordat die verzonden werd. Aanbesteding eiste dat de leverancier modelbeperkingen bekendmaakte en overdraagbaarheid van data verleende, en de dienst publiceerde een beschrijving van het systeem in gewone taal en een beroepsroute. Ze hield AI helemaal buiten definitieve beoordelingsbeslissingen, die voorbehouden bleven aan verantwoordelijke functionarissen.

## Zakelijke onderbouwing: motivatie, ROI en TCO

AI-strategie bestaat om je te helpen twee spiegelbeeldige falen te vermijden: te veel investeren in AI die nooit loont, en te weinig investeren terwijl concurrenten of zusterinstanties vooruitlopen. ROI komt uit bespaarde arbeid, verkorte doorlooptijd, lagere foutpercentages en mogelijk gemaakte nieuwe vermogens. Meet deze tegen een echte uitgangswaarde en corrigeer voor de echte kosten van menselijk toezicht, dat zelden verdwijnt.

De TCO moet de onglamoureuze kostenposten omvatten: datapijplijnen, bewaking, hertraining naarmate de wereld afdrijft, beveiligingsreview en uiteindelijke buitengebruikstelling. Een pilot die goedkoop lijkt kan duur worden zodra hij jarenlang op schaal draait. Presenteer ook de kosten van *niet* adopteren: tragere dienstverlening, hogere handmatige kosten en strategische afdrijving. Maak de zaak voor het bestuur met een portfolioblik: een paar bets met hoge zekerheid, heldere successtatistieken, stopcriteria voor falen en een gereedheidsbeoordeling die toont dat de fundamenten voor data en talent bestaan. Vraag leiders gereedheid expliciet te financieren. Sla je het over, dan garandeer je duur herwerk.

## Antipatronen en valkuilen

- **Oplossing op zoek naar een probleem.** AI kopen omdat peers het deden en dan een gebruiksgeval zoeken.
- **Datagereedheid overslaan.** Modellen lanceren op data die niet beschikbaar, niet gelabeld of juridisch onbruikbaar is.
- **Demogedreven beslissingen.** Je vastleggen op een gelikte demo zonder evaluatie van productiekwaliteit.
- **De menselijke lus negeren.** Volledige automatisering aannemen en review onderbegroten, waar de meeste kosten zich verbergen.
- **Stille lock-in.** Diep bouwen op de bedrijfseigen functies van één leverancier zonder exitplan.
- **Operaties onderschatten.** Deployment behandelen als finish in plaats van als start van een onderhoudsverplichting.
- **Compliance als bijgedachte.** Transparantie en controleerbaarheid achteraf aanbrengen, tegen een veelvoud van de kosten.

## Volwassenheidsmodel

1. **Initiëren.** Ad hoc experimenten, geen gedeelde strategie, beslissingen gedreven door hype en individueel enthousiasme.
2. **Ontwikkelen.** Probleemformulering bestaat voor sommige projecten. Een eerste platformbasis verschijnt. Bouwen of kopen wordt besproken maar inconsistent.
3. **Standaardiseren.** Een portfolio van AI-gebruiksgevallen met heldere statistieken, een gedocumenteerde beslisboom, gereedheidsbeoordelingen en analyse van lock-in en TCO, consistent toegepast over teams.
4. **Beheersen.** Het portfolio wordt gemeten: gereedheid, ROI, TCO en kosten van menselijk toezicht worden gevolgd tegen uitgangswaarden. Stopcriteria worden afgedwongen op bewijs. Lever- en kwaliteitsimpact drijven elke go/no-go-beslissing.
5. **Orkestreren.** AI-strategie is geïntegreerd met bedrijfs- en risicoplanning. Gereedheid wordt continu onderhouden. De organisatie schaft AI-systemen routinematig af, vervangt ze en bakent ze opnieuw af op basis van bewijs, het portfolio herbalancerend naarmate de markt en het risicobeeld verschuiven.

## Ideeën voor discussie

- Hoe beslis je wanneer een probleem werkelijk ongeschikt is voor AI, en wie heeft de bevoegdheid nee te zeggen?
- Welke gereedheidsdrempel moet een project van pilot naar productie poorten?
- Hoeveel lock-in is acceptabel in ruil voor snellere time to value?
- Hoe moeten transparantieverplichtingen bij de overheid de keuze tussen bouwen en kopen vormgeven?
- Hoe houd je TCO-schattingen eerlijk wanneer leveranciers en enthousiastelingen prikkels hebben ze te laag te schatten?
- Wie bezit het AI-portfolio, en hoe worden beslissingen om te stoppen genomen?

## Belangrijkste inzichten

- Strategie begint met een echt probleem en een eerlijke uitgangswaarde, niet met een technologie.
- Geef de voorkeur aan de eenvoudigste optie: eerst prompten, dan ophalen, dan fine-tunen, dan kopen, en zelden van nul bouwen.
- Gereedheid van data, talent en platform zijn voorwaarden. Ze financieren is onderdeel van het plan.
- Gereguleerde en overheidscontexten vereisen transparantie, aanbestedingscompliance en exitopties door ontwerp.
- Modelleer de volledige TCO en de kosten van nietsdoen, en bewaak vanaf de eerste architectuurbeslissing tegen lock-in bij leveranciers.

## Referenties en verder lezen

- Ajay Agrawal, Joshua Gans, and Avi Goldfarb, *Prediction Machines: The Simple Economics of Artificial Intelligence*.
- Eric Siegel, *The AI Playbook: Mastering the Rare Art of Machine Learning Deployment*.
- Andriy Burkov, *The Hundred-Page Machine Learning Book*.
- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- Organisation for Economic Co-operation and Development, *OECD AI Principles*.
- Thomas H. Davenport, *The AI Advantage: How to Put the Artificial Intelligence Revolution to Work*.
