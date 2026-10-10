# 5.7 Ontwikkeling van mobiele applicaties

## Overzicht en motivatie

[Mobiele applicatieontwikkeling](https://en.wikipedia.org/wiki/Mobile_app_development) is de discipline van software bouwen voor telefoons en tablets. Voor veel mensen is een telefoon nu de primaire of enige computer die ze bezitten. Dat maakt de mobiele app de voordeur van je dienst, en vaak het oppervlak waarop gebruikers je hele organisatie beoordelen.

Mobiel is een aparte engineeringomgeving, geen kleine versie van web of desktop. Het apparaat draait in een zak, op batterij, over verbindingen die komen en gaan. Schermen zijn klein. Het besturingssysteem bepaalt wat je app mag doen. Er bestaan twee dominante platformen ([iOS](https://en.wikipedia.org/wiki/IOS) van Apple en [Android](https://en.wikipedia.org/wiki/Android_%28operating_system%29) van Google), elk met eigen talen, ontwerpregels en store. Je kunt niet zomaar een update uitrollen wanneer je wilt, want een store beoordeelt die eerst, en gebruikers kiezen wanneer ze installeren. Dit hoofdstuk bouwt voort op frontend-engineering (hoofdstuk 5.6), UX-fundamenten (hoofdstuk 5.1) en toegankelijkheid (hoofdstuk 5.3), en leunt op applicatiebeveiliging (hoofdstuk 4.2) en CI/CD en oplevering (hoofdstuk 8.1).

De relevantie voor onderneming en overheid is hoog. Ondernemingen leveren klant-apps en interne apps voor hun eigen personeel op, vaak beheerd via [mobile device management](https://en.wikipedia.org/wiki/Mobile_device_management) (MDM: centrale software die bedrijfsapparaten configureert en beveiligt). Overheden bouwen burgergerichte apps voor uitkeringen, gezondheid, identiteit en betalingen, en moeten iedereen bedienen, inclusief mensen op oude apparaten en trage verbindingen, onder toegankelijkheidswetten. In beide omgevingen is mobiel een serieuze, langlevende verbintenis, dus behandel het met dezelfde rigueur als elk ander productiesysteem.

## Kernprincipes

- Ontwerp voor het apparaat: klein scherm, batterij en een netwerk dat komt en gaat.
- Neem onderbroken connectiviteit aan. Werk eerst offline en synchroniseer wanneer je kunt.
- Respecteer de ontwerp- en interactieconventies van elk platform.
- Je beheert de releasetiming niet. De store en de gebruiker doen dat.
- Fragmentatie is normaal. Ondersteun een echt bereik aan apparaten en OS-versies.
- Sla data veilig op het apparaat op, want apparaten raken kwijt en worden gestolen.
- Toegankelijkheid is een vereiste, geen afwerking.
- Kies je bouwaanpak voor de hele levensduur van de app, niet alleen de lanceringsdag.

## Aanbevelingen

### Kies de bouwaanpak bewust

Er zijn drie brede aanpakken, en elk past bij andere behoeften.

[Native ontwikkeling](https://en.wikipedia.org/wiki/Mobile_app_development) betekent apart voor elk platform schrijven met zijn eigen tools: Swift voor iOS, Kotlin voor Android. Je krijgt de beste prestaties, de volledigste toegang tot apparaatfuncties en het meest getrouwe platformgevoel, ten koste van het bouwen en onderhouden van twee codebases.

[Cross-platformframeworks](https://en.wikipedia.org/wiki/Cross-platform_software) laten één codebasis beide platformen bedienen. [React Native](https://en.wikipedia.org/wiki/React_Native) gebruikt JavaScript en rendert echte native componenten. [Flutter](https://en.wikipedia.org/wiki/Flutter_%28software%29) gebruikt de taal Dart en tekent zijn eigen widgets. Deze verminderen dubbele inspanning en kunnen oplevering versnellen, maar ze voegen een afhankelijkheid toe van de gezondheid van het framework en kunnen achterlopen op de nieuwste platformfuncties.

Een [progressive web app](https://en.wikipedia.org/wiki/Progressive_web_app) (PWA: een website die kan worden geïnstalleerd en offline kan werken) heeft geen store nodig en wordt direct bijgewerkt, maar heeft beperkte toegang tot sommige apparaatfuncties en een zwakkere aanwezigheid op het beginscherm.

Kies op basis van de vereiste apparaatfuncties, het prestatieprofiel, de onderhoudshorizon, de vaardigheden die je kunt aannemen en het bereik dat je nodig hebt. Een consumentenapp met hoge prestaties kan native rechtvaardigen. Een content-en-formulierenapp met een klein team past mogelijk goed bij cross-platform of een PWA.

### Volg de ontwerprichtlijnen van het platform

Elk platform heeft gepubliceerde, gedetailleerde conventies. Apple levert de [Human Interface Guidelines](https://en.wikipedia.org/wiki/Human_interface_guidelines), en Google levert [Material Design](https://en.wikipedia.org/wiki/Material_Design). Die dekken navigatie, gebaren, typografie, spacing en systeemgedrag. Ze volgen maakt je app vertrouwd, wat de moeite verlaagt die gebruikers besteden aan het leren ervan. Ertegen vechten laat een app vreemd en onhandig aanvoelen. Een cross-platformcodebasis moet nog steeds de conventies per platform eerbiedigen waar ze verschillen, in plaats van het uiterlijk van het ene platform op het andere te forceren.

### Ontwerp voor mobiele beperkingen

Bouw offline-first: laat kerntaken werken zonder verbinding, sla wijzigingen lokaal op en synchroniseer wanneer het netwerk terugkeert. Handel conflicten doordacht af wanneer dezelfde data op twee plekken verandert. Wees zuinig met batterij en data: bundel netwerkaanroepen, vermijd constant locatie- of achtergrondwerk, comprimeer payloads en respecteer de databesparingsinstellingen van de gebruiker. Plan voor fragmentatie, de brede spreiding van schermformaten, apparaatkracht en OS-versies. Kies een ondersteuningsbereik op basis van echte gebruiksdata en test op bescheiden hardware, niet alleen vlaggenschepen. Ontwerp voor kleine schermen met heldere hiërarchie, grote aanraakdoelen en content die zich aanpast aan verschillende formaten en oriëntaties.

### Plan distributie, versiebeheer en updates

Publiceren gaat via de [Apple App Store](https://en.wikipedia.org/wiki/App_Store_%28Apple%29) en [Google Play](https://en.wikipedia.org/wiki/Google_Play), elk met reviewprocessen en beleid die een release kunnen vertragen of afwijzen. Bouw reviewtijd in je planning in en lees het beleid vroeg. Omdat gebruikers kiezen wanneer ze updaten, heb je altijd veel versies tegelijk in het veld. Houd je app achterwaarts compatibel met oudere clients en versioneer je API's (hoofdstuk 2.3) zodat een oude app blijft werken. Zorg voor een manier om een update af te dwingen wanneer het moet, bijvoorbeeld een verplichte updatemelding wanneer een versie onveilig of niet ondersteund is, en gebruik die spaarzaam. Ondernemingen kunnen interne apps ook distribueren via MDM of private kanalen in plaats van de publieke stores.

### Gebruik pushnotificaties en deep links met zorg

[Pushnotificaties](https://en.wikipedia.org/wiki/Push_technology) laten je gebruikers bereiken wanneer je app gesloten is. Gebruik ze voor echte waarde, respecteer de toestemming van de gebruiker en platformrechten en vermijd ruis, want mensen schakelen notificaties uit van apps die te ver gaan. [Deep links](https://en.wikipedia.org/wiki/Deep_linking) sturen een gebruiker direct naar een specifiek scherm vanuit een link of notificatie. Configureer ze zodat een link de juiste plek in de app opent en soepel terugvalt op het web wanneer de app niet is geïnstalleerd.

### Beveilig de app en haar data

Behandel het apparaat als onbetrouwbaar en mogelijk verloren. Sla gevoelige data op in de beveiligde opslag van het platform (de [iOS Keychain](https://en.wikipedia.org/wiki/Keychain_%28software%29) of de Android Keystore), nooit in gewone bestanden. Bied [biometrische authenticatie](https://en.wikipedia.org/wiki/Biometrics) (vingerafdruk of gezicht) om gevoelige acties te ontgrendelen, ondersteund door een toegangscode. Overweeg [certificate pinning](https://en.wikipedia.org/wiki/Public_key_pinning) (controleren dat de server een verwacht certificaat toont) voor verbindingen met hoge waarde, en plan het roteren van die certificaten. Minimaliseer wat je op het apparaat opslaat, bescherm geheimen en volg de bredere richtlijnen in applicatiebeveiliging (hoofdstuk 4.2).

### Bouw een echte test- en leveringspijplijn

Test op echte apparaten, niet alleen [emulators](https://en.wikipedia.org/wiki/Emulator) en simulators, omdat hardware, sensoren en prestaties verschillen. Gebruik een apparatenlab of een cloudapparatenpark om een representatieve spreiding van modellen en OS-versies te dekken. Automatiseer builds, tests, ondertekening en store-indiening via [continuous integration en delivery](https://en.wikipedia.org/wiki/CI/CD) (hoofdstuk 8.1), inclusief bètadistributie aan testers vóór de publieke release. Ondertekeningssleutels en store-inloggegevens veilig beheren is onderdeel van deze pijplijn.

### Maak toegankelijkheid een vereiste

Ondersteun de toegankelijkheidsfuncties van elk platform: schermlezers ([VoiceOver](https://en.wikipedia.org/wiki/VoiceOver) op iOS, [TalkBack](https://en.wikipedia.org/wiki/Google_TalkBack) op Android), dynamische tekstgrootte, voldoende kleurcontrast en grote aanraakdoelen. Label bedieningselementen zodat hulptechnologie ze kan beschrijven. Test met de echte hulpmiddelen, niet alleen met geautomatiseerde controles. Vooral voor de overheid is toegankelijkheid een wettelijk mandaat, en de details staan in toegankelijkheid (hoofdstuk 5.3).

## Afwegingen: voor- en nadelen

| Aanpak | Voordelen | Nadelen |
|---|---|---|
| Native (Swift, Kotlin) | Beste prestaties, volledige apparaattoegang, echt platformgevoel | Twee codebases, hogere kosten, meer personeel |
| React Native | Eén JavaScript-codebasis, echte native componenten, snelle iteratie | Frameworkafhankelijkheid, overbruggingscomplexiteit, achterstand in functies |
| Flutter | Eén codebasis, consistente UI, sterke prestaties | Dart-vaardigheden minder gangbaar, grotere appgrootte, eigen widgetmodel |
| Progressive web app | Geen store, directe updates, één webcodebasis | Beperkte apparaatfuncties, zwakkere aanwezigheid, platformgrenzen |
| Afgedwongen updates | Verwijdert onveilige oude versies snel | Ergert gebruikers bij overmatig gebruik. Kan toegang blokkeren |
| Certificate pinning | Sterke bescherming tegen onderschepping | Breekt als certificaten roteren zonder appupdates |

De terugkerende afweging is bereik en leveringssnelheid tegenover diepte en getrouwheid. Native geeft de rijkste, meest getrouwe ervaring maar kost het meest om te bouwen en te onderhouden. Cross-platform- en PWA-aanpakken besparen inspanning en vergroten bereik, tegen enig verlies aan platformgevoel of apparaattoegang. Voor een klein team dat formulieren en content oplevert is een codebasis delen vaak verstandig. Voor een veeleisende consumentenapp kan native diepte de prijs waard zijn. Besluit met de hele levensduur van de app in het oog, niet alleen de lancering.

## Vragen om met je team te bespreken

1. **Hoe lang ondersteunen we oude clients in het veld, en is onze API geversioneerd om ze werkend te houden?** Omdat gebruikers kiezen wanneer ze updaten, heb je altijd veel versies van de app tegelijk geïnstalleerd, en een backendwijziging die aanneemt dat iedereen actueel is zal de lange staart van oudere clients breken. Besluit je achterwaartse-compatibiliteitsvenster, versioneer je API's zodat een oude app blijft werken en houd een zelden gebruikt verplicht-updatepad voor versies die werkelijk onveilig zijn. Dit telt voor burger-apps van de overheid en personeelsapps van ondernemingen evengoed, waar mensen op oude apparaten niet kunnen of willen upgraden op jouw schema. Neem je huidige versieverdelingsdata mee en vraag wat breekt voor de oudste client die nog echt in gebruik is. Als je die verdeling niet kent, instrumenteer haar dan voordat je je volgende brekende wijziging oplevert.

2. **Wat is onze lat voor het sturen van een pushnotificatie, en wie beslist wat een onderbreking van een gebruiker waard is?** Pushnotificaties bereiken mensen wanneer de app gesloten is, wat ze krachtig en makkelijk te misbruiken maakt, en gebruikers schakelen notificaties uit (of verwijderen de app) van producten die te ver gaan. Spreek af wat telt als echte waarde, hoe gebruikers frequentie en kanaal beheersen en hoe je platformtoestemming eert in plaats van om rechten te zeuren. Zonder gedeelde lat grijpt elk team met een statistiek om te halen naar een push, en degradeert het hele kanaal tot ruis. Neem de notificaties van de afgelopen maand mee en vraag welke de gebruiker je zou hebben bedankt. Als de meeste promotioneel waren, scherp het beleid dan aan voordat het uitschrijfpercentage het voor je doet.

3. **Is onze mobiele leveringspijplijn echt, met ondertekening, een apparatenpark en bètadistributie, of is release een stressvolle handmatige haast?** Mobiel voegt gevaren toe die het web niet heeft: storereview kan een release vertragen of afwijzen, ondertekeningssleutels en store-inloggegevens moeten veilig worden behandeld en hardware en sensoren verschillen genoeg dat emulators echte problemen verbergen. Builds, tests, ondertekening en store-indiening automatiseren via CI/CD, met bètadistributie aan testers en een cloudapparatenpark dat de modellen dekt die je gebruikers werkelijk bij zich dragen, maakt van releases routine in plaats van heldendaden. Besluit wie de pijplijn en de ondertekeningssleutels bezit en hoe storereviewtijd in elk releaseplan wordt gebouwd. Neem het verhaal van je laatste release mee en tel de handmatige stappen. Elk is een plek waar een stressvolle release onder deadline mis kan gaan.

4. **Hebben we native, cross-platform of een progressive web app gekozen voor de hele levensduur van dit product, of alleen voor de lanceringsdag?** De bouwaanpak is de grootste hefboom op kosten en mogelijkheden van een mobiele app voor jaren, en een keuze gemaakt om snel op te leveren kan je vastzetten: native koopt de rijkste apparaattoegang en het platformgevoel tegen de prijs van twee codebases en twee skillsets, terwijl cross-platform en PWA code delen maar een frameworkafhankelijkheid toevoegen of toegang tot sommige apparaatfuncties verliezen. Voor een groot team drijft deze beslissing het aannemen van personeel, het onderhoudsbudget en hoe snel je elke jaarlijkse OS-release kunt overnemen, dus verdient ze een expliciete eigenaar in plaats van een standaard bepaald door wie het eerste prototype schreef. Neem de vereiste apparaatfuncties mee, het prestatieprofiel, de onderhoudshorizon en de vaardigheden die je werkelijk kunt aannemen, en wees eerlijk over welke platformfuncties je onder elke optie zou verspelen. Weeg in omgevingen van onderneming en overheid af of de app een langlevende verbintenis is die personeelsverloop en een decennium platformverandering moet overleven, en leg de beslissing en haar onderbouwing vast zodat een toekomstig team niet hoeft te raden waarom de codebasis eruitziet zoals ze eruitziet.

5. **Welk apparaat- en OS-versie-ondersteuningsbereik hebben onze echte gebruikers nodig, en testen we op de hardware die ze werkelijk bij zich dragen in plaats van de telefoons op onze bureaus?** Fragmentatie is de normale toestand van mobiel: gebruikers beslaan een brede spreiding van schermformaten, apparaatkracht en OS-versies, en een app afgestemd op de vlaggenschepen van het team wordt traag of kapot opgeleverd op de bescheiden hardware die een groot deel van je publiek bezit. Een ondersteuningsbereik vaststellen is een afweging tussen bereik en inspanning, omdat elk ouder model en elke OS-versie die je belooft te ondersteunen de testmatrix en onderhoudslast verbreedt, dus het bereik moet uit echte gebruiksdata komen in plaats van aanname. Neem je apparaat- en OS-versieverdeling mee, de modellen die een cloudapparatenpark of lab momenteel dekt en de prestaties die je op hardware van lage kwaliteit hebt gemeten, niet alleen simulators. Voor burger-apps van de overheid is dit bijna niet onderhandelbaar, omdat je iedereen moet bedienen inclusief mensen op oude apparaten en trage verbindingen onder toegankelijkheidsverplichtingen, en voor ondernemingsvloten moet je de exacte robuuste toestellen testen die het personeel draagt in plaats van een generieke steekproef.

6. **Welke gevoelige data leeft op het apparaat, en is elk stuk beschermd tegen een telefoon die verloren, gestolen of in andermans handen is?** Een mobiel apparaat reist in een zak en raakt kwijt of wordt gestolen, dus elke data of geheim opgeslagen in een gewoon bestand is één verloren telefoon verwijderd van blootstelling, en de schadezone groeit met elke gebruiker. De overwegingen trekken tegen elkaar: data op het apparaat cachen is wat offline-first laat werken en de app snel houdt, maar elk gecachet item is een verplichting die in de beveiligde opslag van het platform moet staan (de iOS Keychain of de Android Keystore), geminimaliseerd moet zijn en idealiter achter biometrie of een toegangscode moet zitten. Neem een inventaris mee van precies wat de app lokaal bewaart, waar elk item is opgeslagen, wat het ontgrendelt en of verbindingen met hoge waarde certificate pinning gebruiken met een werkbaar rotatieplan. Koppel dit in omgevingen van een onderneming aan het mobile-device-managementbeleid en remote wipe, en behandel in overheidsomgevingen persoonsgegevens op het apparaat als privacy- en juridische blootstelling die moet worden gerechtvaardigd, gedocumenteerd en verdedigbaar onder audit.

## Sectorperspectief

**Startup.** Met een piepklein team en weinig runway kun je zelden twee native codebases of twee sets vaardigheden betalen, dus een cross-platformframework of zelfs een PWA die beide stores vanuit één codebasis bereikt wint meestal. Lever offline-first voor de ene kerntaak die ertoe doet, houd elk token in beveiligde opslag in plaats van een gewoon bestand en bouw storereviewtijd in elke release zodat een afwijzing geen lanceringsdatum opblaast. Sla verplichte updates, certificate pinning en een apparatenpark over tot echt gebruik ze rechtvaardigt.

**Kleinbedrijf.** Zonder aparte mobiele specialist en met een krap budget leun je sterk op kopen boven bouwen: een no-codeappbouwer, een white-label-app van je kassa- of boekingsleverancier of een goed gemaakte PWA vanaf je bestaande website verslaat vaak een maatwerkapp die je niet kunt onderhouden. Als je wel een app laat bouwen, bezit dan zelf de ondertekeningssleutels en store-accounts zodat een aannemer je aanwezigheid niet kan gijzelen, en sta in het contract op toegankelijkheid en veilige opslag op het apparaat. Houd de scope bij de een of twee taken die klanten werkelijk op een telefoon doen.

**Grote onderneming.** Op schaal is de app een langlevende verbintenis over veel teams, dus standaardiseer de bouwaanpak, het patroon voor beveiligde opslag, de CI/CD-pijplijn en het API-versiebeleid in plaats van elk product ze opnieuw te laten uitvinden. Interne personeelsapps lopen meestal via mobile device management voor installatie, configuratie, remote wipe en beleid, terwijl klant-apps een apparatenpark nodig hebben dat echt gebruik dekt en geauditeerde toegankelijkheid en beveiliging. Bestuur ondertekeningssleutels, store-inloggegevens en releasetiming centraal zodat een brekende backendwijziging de lange staart van oudere clients nooit laat stranden.

**Overheid.** Aanbestedingsregels, transparantie en publieke verantwoording geven elke keuze vorm. Je moet iedereen bedienen, inclusief mensen op oude apparaten en trage verbindingen, dus toegankelijkheid is een wettelijk mandaat geverifieerd met echte hulpmiddelen en een breed apparaatondersteuningsbereik is bijna niet onderhandelbaar. Geef de voorkeur aan aanpakken en contracten die lock-in bij leveranciers vermijden, data overdraagbaar houden en het publiek laten inzien wat de app met hun data doet, en behandel persoonsgegevens op het apparaat als blootstelling die je onder audit moet rechtvaardigen en documenteren.

## Voorbeelden

**Startup.** Een startup van drie personen die een gewoontetrackingapp bouwde moest zowel iOS als Android bereiken, maar kon zich geen twee native codebases of twee sets vaardigheden veroorloven. Ze kozen een cross-platformframework zodat één klein team naar beide stores kon opleveren, en ontwierpen vanaf het begin offline-first zodat een gebruiker in de metro zonder signaal een gewoonte kon loggen en later synchroniseren. Ze hielden het logintoken in de beveiligde opslag van het platform in plaats van een gewoon bestand, bouwden storereviewtijd in elk releaseplan en testten naast hun eigen toestellen op een paar goedkope oudere telefoons, wat trage prestaties ving die ze anders hadden opgeleverd.

**Grote onderneming.** Een logistiek bedrijf bouwde een interne app voor zijn chauffeurs en magazijnpersoneel. Omdat magazijnen en bezorgroutes wankel signaal hebben, koos het team een offline-first ontwerp: scans en statusupdates worden lokaal opgeslagen en gesynchroniseerd wanneer een verbinding terugkeert. Ze gebruikten een cross-platformframework om met een klein team één codebasis aan beide platformen te leveren. De app wordt gedistribueerd via mobile device management in plaats van de publieke stores, zodat IT installatie, configuratie en beveiligingsbeleid op bedrijfsapparaten beheerst. Gevoelige inloggegevens leven in de beveiligde opslag van het platform, en biometrie ontgrendelt de app. Een cloudapparatenpark test een representatieve spreiding van de robuuste toestellen die het personeel werkelijk draagt.

**Overheid.** Een nationaal agentschap leverde een burgergerichte app voor identiteit en uitkeringen op. Toegankelijkheid was vanaf dag één een harde eis: volledige schermlezerondersteuning, dynamische tekstgrootte en sterk contrast, getest met echte hulpmiddelen om aan de wet te voldoen. Omdat burgers een enorm bereik aan apparaten gebruiken, ondersteunde het team een brede band aan oudere modellen en trage verbindingen en hield kerntaken offline werkend. Gevoelige data blijft in beveiligde apparaatopslag, biometrie beschermt de toegang en verbindingen met hoge waarde gebruiken certificate pinning met een geplande rotatieprocedure. API-versiebeheer houdt oudere geïnstalleerde apps werkend, en een zelden gebruikt verplicht-updatepad bestaat voor beveiligingsreparaties. Storereviewtermijnen zijn in elk releaseplan gebouwd.

## Zakelijke onderbouwing: motivatie, ROI en TCO

Mobiel is waar veel gebruikers je dienst ontmoeten, dus de app beïnvloedt adoptie, tevredenheid en voltooiing van de taken die voor je organisatie tellen. Een snelle, betrouwbare, goed ontworpen app verhoogt het gebruik en vermindert supportlast. Voor ondernemingen kan een interne mobiele app een mobiel personeelsbestand meetbaar productiever maken en papierwerk verminderen. Voor overheden vergroot een bruikbare burger-app de toegang en vermindert ze de vraag naar callcenter en persoonlijk loket.

Qua total cost of ownership (TCO) is de keuze van aanpak de grootste hefboom. Native betekent betalen voor twee codebases en twee skillsets over de hele levensduur van de app. Cross-platform ruilt een deel daarvan tegen een afhankelijkheid die je actueel moet houden. Begroot naast code store-vergoedingen en reviewcycli, een apparatentestlab of cloudpark, doorlopende OS-versieondersteuning naarmate platformen jaarlijks releasen en het beveiligingswerk dat mobiel vraagt. De kosten van onderinvesteren tonen zich in crashes op niet-ondersteunde apparaten, beveiligingsincidenten door onbeschermde data op het apparaat, afgewezen of vertraagde releases en gebruikers die een trage of onhandige app verlaten.

Verbind de app voor het bestuur aan concrete uitkomsten: taakvoltooiing, retentie, personeelsproductiviteit of lagere supportkosten. Prijs de volledige aanpakbeslissing over de levensduur van de app, niet alleen de eerste release, en noem de risico's (beveiliging, toegankelijkheidswetgeving, storeafwijzing) die een serieuze mobiele praktijk vermindert.

## Antipatronen en valkuilen

- **Mobiel behandelen als gekrompen website**: aanraking, gebaren en platformconventies negeren.
- **Een perfect netwerk aannemen**: geen offlineafhandeling, zodat de app breekt zodra het signaal wegvalt.
- **Alleen testen op het nieuwste vlaggenschip**: slechte prestaties verbergen op de apparaten die echte gebruikers dragen.
- **Geheimen in gewone bestanden opslaan**: gevoelige data blootgesteld wanneer een apparaat verloren raakt of gestolen wordt.
- **Notificatieoverbelasting**: te veel pushes, zodat gebruikers de app dempen of verwijderen.
- **Storereviewtijd negeren**: releaseplannen die directe publicatie aannemen en dan uitlopen.
- **Geen verplicht-updatepad**: onveilige oude versies blijven bestaan zonder manier ze buiten dienst te stellen.
- **Batterij en data leegtrekken**: constant achtergrondwerk en praatzieke netwerken die gebruikers merken.
- **Toegankelijkheid als bijgedachte**: gebruikers uitsluiten en, bij de overheid, de wet breken.
- **Eén codebasis gedwongen overal identiek eruit te zien**: een app die op beide platformen vreemd aanvoelt.

## Volwassenheidsmodel

**Niveau 1: Initiëren.** Mobiel is ad hoc en reactief. De app wordt gebouwd als een website, getest op de eigen telefoons van het team en breekt vaak offline. Weinig aandacht gaat naar beveiligde opslag, toegankelijkheid of storereviewtermijnen. Releases zijn een stressvolle handmatige haast, en niemand bezit de bouwaanpak of de ondertekeningssleutels.

**Niveau 2: Ontwikkelen.** Basispraktijken verschijnen, maar zijn inconsistent over teams en producten. Een bouwaanpak wordt gekozen voor een gegeven app, ze volgt platformbasis en wordt op enkele echte apparaten getest, en enige offlineafhandeling en beveiligde opslag bestaan. Builds zijn deels geautomatiseerd en iemand bezit store-indieningen, maar de app van een ander team kan dit alles nog anders doen of helemaal niet.

**Niveau 3: Standaardiseren.** Goede praktijk is gedocumenteerd en organisatiebreed afgedwongen. Offline-first is de standaard, een gedocumenteerd apparaatondersteuningsbereik wordt getest op een apparatenlab of cloudpark en platformontwerprichtlijnen en toegankelijkheid worden gevolgd en geverifieerd met echte hulpmiddelen. Beveiligde opslag, biometrie en API-versiebeheer zijn standaard, CI/CD automatiseert builds, tests, ondertekening en bètadistributie en storereviewtijd wordt in elke release gepland.

**Niveau 4: Beheersen.** Mobiele kwaliteit wordt gemeten en beheerst aan de hand van uitgangswaarden. Crashes, koude-start- en schermrenderprestaties, batterij- en datagebruik en taakvoltooiingspercentages worden continu vastgelegd van echte apparaten en gevolgd tegen doelen, met uitsplitsingen per model en per OS-versie zodat een regressie op hardware van lage kwaliteit wordt gevangen, niet opgeleverd. Toegankelijkheid en beveiliging worden geaudit in plaats van aangenomen, notificatie-uitschrijf- en updateadoptiepercentages worden bewaakt en het ondersteuningsbereik en de bouwaanpak worden op dat bewijs beoordeeld. Beslissingen over stoppen of repareren van een release rusten op de statistieken, niet op hoe de app op de telefoon van de leidinggevende aanvoelde.

**Niveau 5: Orkestreren.** Mobiel wordt continu verbeterd en over de organisatie geïntegreerd, en past zich aan naarmate het apparaatlandschap verschuift. Certificaatrotatie, verplicht-updatepaden en rollback zijn routine, het ondersteuningsbereik en de bouwaanpak worden op bewijs opnieuw afgebakend naarmate platformen jaarlijks releasen en de hele spreiding van gebruikers en apparaten wordt behandeld als eersterangs. Mobiele planning is verbonden met beveiliging, toegankelijkheid, API en leveringspraktijk, zodat een OS-wijziging, een nieuwe apparaatklasse of een beleidsverschuiving als routinewerk wordt opgevangen in plaats van als noodgeval.

## Ideeën voor discussie

- Hoe beslis je tussen native, cross-platform en een progressive web app voor een gegeven product?
- Welk apparaat- en OS-versie-ondersteuningsbereik past bij je echte gebruikersdata, en hoe houd je het actueel?
- Waar is offline-first essentieel in je app, en hoe handel je synchronisatieconflicten af?
- Wanneer is een verplichte update gerechtvaardigd, en hoe voorkom je gebruikers oneerlijk te blokkeren?
- Hoe test je op echte apparaten op een schaal die je gebruikers weerspiegelt?
- Welke gevoelige data leeft op het apparaat, en hoe is elk stuk beschermd?
- Hoe eerbiedig je de conventies van elk platform vanuit een gedeelde codebasis?

## Belangrijkste inzichten

- Kies de bouwaanpak (native, cross-platform of PWA) voor de hele levensduur van de app.
- Volg de ontwerprichtlijnen van het platform zodat de app vertrouwd aanvoelt en de moeite van de gebruiker verlaagt.
- Ontwerp voor mobiele beperkingen: offline-first, zuinig met batterij en data, fragmentatie, kleine schermen.
- Je beheert de releasetiming niet. Plan voor storereview, versiebeheer en verplichte updates.
- Gebruik pushnotificaties en deep links met terughoudendheid en toestemming.
- Beveilig data op het apparaat met beveiligde opslag, biometrie en, waar gerechtvaardigd, certificate pinning.
- Test op echte apparaten en automatiseer de mobiele pijplijn via CI/CD.
- Maak toegankelijkheid een vereiste, wat voor de overheid een wettelijk mandaat is.

## Referenties en verder lezen

- Apple, *Human Interface Guidelines*
- Google, *Material Design* guidelines
- Apple, *App Store Review Guidelines*
- Google, *Google Play developer policies and Android developer documentation*
- OWASP, *Mobile Application Security Verification Standard (MASVS)* and *Mobile Security Testing Guide*
- React Native project documentation
- Flutter project documentation
- Google, *web.dev* guidance on progressive web apps
- U.S. Section 508 and WCAG (Web Content Accessibility Guidelines) references for mobile accessibility
- NIST, *Guidelines on mobile device security and management*
