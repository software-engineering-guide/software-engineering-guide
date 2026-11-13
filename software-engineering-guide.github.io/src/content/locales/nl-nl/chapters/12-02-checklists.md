# 12.2 Checklists

Deze checklists zijn praktische, kant-en-klare naslagen. Kopieer elke checklist in een pull-requestsjabloon, een wikipagina, een ticket of een vergaderagenda voor een review, en pas de punten aan je context aan. Behandel elk punt als iets wat een persoon kan verifiëren en met ja of nee kan beantwoorden. Een checklist is een geheugensteun en een gedeelde standaard, geen vervanging voor oordeel. Verwijder punten die niet van toepassing zijn en voeg punten toe die je domein vereist.

Richtlijnen om ze goed te gebruiken:

- Houd checklists kort genoeg dat mensen ze werkelijk afmaken. Als een checklist routinematig wordt overgeslagen, is ze te lang of te algemeen.
- Automatiseer elk punt dat een machine kan verifiëren (opmaak, tests, scans) zodat mensen hun aandacht aan oordeelspunten besteden.
- Versioneer je checklists en beoordeel ze periodiek. Een checklist die nooit verandert wordt waarschijnlijk niet gebruikt.
- Onderscheid blokkerende punten van adviserende punten wanneer het onderscheid voor je proces telt.

## Checklist voor codereview

Voor de reviewer die de wijziging van een ander beoordeelt.

- [ ] De wijziging doet wat haar beschrijving en het gekoppelde ticket zeggen dat ze doet.
- [ ] De reikwijdte is gericht op één logische zorg. Niet-gerelateerde wijzigingen zijn afgesplitst.
- [ ] Het ontwerp past in de bestaande architectuur en introduceert geen koppeling die makkelijker te vermijden was.
- [ ] Randgevallen, foutpaden en faalwijzen worden afgehandeld, niet alleen het gelukkige pad.
- [ ] Er bestaan tests, ze zijn betekenisvol en zouden falen als het gedrag terugviel.
- [ ] Naamgeving, structuur en commentaar maken de code begrijpelijk voor een toekomstige lezer.
- [ ] Er zijn geen geheimen, inloggegevens, tokens of persoonsgegevens gecommit.
- [ ] Beveiligingsgevoelige invoer wordt passend gevalideerd, gecodeerd of geparametriseerd.
- [ ] Publieke interfaces, contracten en achterwaartse compatibiliteit blijven behouden of worden bewust geversioneerd.
- [ ] Logging, statistieken en foutrapportage volstaan om de wijziging in productie te beheren.
- [ ] Documentatie, runbooks en configuratie zijn bijgewerkt om bij de wijziging te passen.
- [ ] Feedback is gescheiden in blokkerende punten tegenover suggesties en geformuleerd over de code.

## Checklist voor de auteur van een pull request

Voor de auteur voordat hij of zij om review vraagt.

- [ ] De PR is klein en gericht genoeg om in één zitting zorgvuldig te beoordelen.
- [ ] De beschrijving vermeldt wat er veranderde, waarom en hoe het is geverifieerd.
- [ ] Het gekoppelde ticket, de issue of het ontwerpdocument geeft reviewers de nodige context.
- [ ] Alle geautomatiseerde controles slagen lokaal of in CI (build, lint, opmaak, tests, scans).
- [ ] Nieuw en gewijzigd gedrag wordt door tests gedekt.
- [ ] Mechanische refactors zijn gescheiden van gedragswijzigingen.
- [ ] Zelfreview is voltooid: je hebt je eigen diff regel voor regel gelezen.
- [ ] Er blijft geen debugcode, uitgecommentarieerd blok, geheim of dwaalbestand over.
- [ ] Databasemigraties, feature flags en configuratiewijzigingen zijn gedocumenteerd en omkeerbaar.
- [ ] Brekende wijzigingen worden expliciet benoemd met een migratiepad.
- [ ] Schermafbeeldingen, opnames of voorbeelduitvoer zijn bijgevoegd waar ze de review helpen.
- [ ] De juiste reviewers en eventuele vereiste rolgebonden goedkeurders zijn gevraagd.

## Definition of Done

De gedeelde standaard waaraan een werkitem moet voldoen voordat het als af geldt.

- [ ] Acceptatiecriteria in het ticket zijn allemaal gehaald en demonstreerbaar.
- [ ] Code is door collega's beoordeeld en goedgekeurd door de vereiste reviewers.
- [ ] Geautomatiseerde tests zijn geschreven, slagen en zijn met de wijziging samengevoegd.
- [ ] Code is in de hoofdlijn samengevoegd en deployt schoon via de pijplijn.
- [ ] Er blijven geen bekende defecten open van de afgesproken ernstdrempel.
- [ ] Documentatie, helptekst en runbooks zijn bijgewerkt.
- [ ] Observeerbaarheid is aanwezig: relevante logs, statistieken en alarmen bestaan.
- [ ] Beveiligings- en privacygevolgen zijn overwogen en aangepakt.
- [ ] Toegankelijkheidseisen voor de wijziging zijn gehaald waar gebruikersgericht.
- [ ] Feature flags zijn geconfigureerd en het uitrolplan is afgesproken.
- [ ] De productowner of belanghebbende heeft de uitkomst geaccepteerd.
- [ ] Vervolgwerk is vastgelegd als gevolgde tickets, niet impliciet gelaten.

## Gereedheid voor productielancering / go-live

Voordat een significante wijziging of nieuwe service naar productie gaat.

- [ ] Het uitrolplan is gedocumenteerd, inclusief gefaseerde of canary-stappen en succescriteria.
- [ ] Het rollbackplan is gedocumenteerd, getest en kan snel worden uitgevoerd.
- [ ] Capaciteits- en belastingtests tonen dat het systeem aan verwachte en piekvraag voldoet.
- [ ] Bewaking, dashboards en alarmen zijn live en gevalideerd vóór de lancering.
- [ ] Bereikbaarheidsdekking is gepland en de responders kennen het systeem.
- [ ] Runbooks bestaan voor de meest waarschijnlijke falen en operationele scenario's.
- [ ] Afhankelijkheden, integraties en derden zijn bevestigd klaar en snelheidslimieten zijn begrepen.
- [ ] Beveiligingsreview en vereiste goedkeuringen zijn voltooid.
- [ ] Datamigratie, indien aanwezig, is end-to-end getest met een geverifieerde terugtrekking.
- [ ] Feature flags laten de wijziging uitzetten zonder herdeployment.
- [ ] Juridische, privacy- en complianceaccordering is verkregen waar vereist.
- [ ] Het communicatieplan dekt belanghebbenden, support en klanten.
- [ ] Een go/no-go-beslissing wordt genomen door benoemde eigenaren tegen expliciete criteria.

## Checklist voor beveiligingsreview / dreigingsmodel

Voor het beoordelen van de beveiligingshouding van een wijziging of systeem.

- [ ] Vertrouwensgrenzen en datastromen zijn geïdentificeerd en gedocumenteerd.
- [ ] Authenticatie wordt afgedwongen op elk toegangspunt dat haar vereist.
- [ ] Autorisatiecontroles dwingen minimale rechten af voor elke handeling en resource.
- [ ] Alle externe invoer wordt gevalideerd en uitvoer wordt gecodeerd voor haar bestemming.
- [ ] Geheimen worden opgeslagen in een beheerde kluis, nooit in code of configuratie, en zijn roteerbaar.
- [ ] Data is versleuteld onderweg en in rust zoals de classificatie vereist.
- [ ] Afhankelijkheden worden gescand op bekende kwetsbaarheden en actueel gehouden.
- [ ] Injectie-, deserialisatie- en SSRF-risico's zijn beperkt voor onbetrouwbare invoer.
- [ ] Beveiligingsrelevante gebeurtenissen worden gelogd zonder gevoelige data vast te leggen.
- [ ] Snelheidsbegrenzing, quota en misbruikbescherming bewaken blootgestelde eindpunten.
- [ ] Foutmeldingen lekken geen stacktraces, interne zaken of gevoelig detail.
- [ ] Dreigingen geïdentificeerd via STRIDE of vergelijkbaar zijn vastgelegd met maatregelen of geaccepteerd risico.
- [ ] Beveiligingstesten (SAST, DAST of penetratietesten) zijn gepland of voltooid.

## Checklist voor privacy en gegevensbescherming (in DPIA-stijl)

Voor verwerking die persoonlijke of gevoelige data betreft.

- [ ] De verzamelde persoonsgegevens zijn geïnventariseerd, geclassificeerd en geminimaliseerd tot wat nodig is.
- [ ] De rechtsgrond of bevoegdheid voor elk verwerkingsdoel is gedocumenteerd.
- [ ] Doelbinding wordt afgedwongen: data wordt alleen voor de vermelde doelen gebruikt.
- [ ] Bewaartermijnen zijn gedefinieerd en verwijdering of anonimisering is geautomatiseerd.
- [ ] Rechten van betrokkenen (inzage, correctie, verwijdering, overdraagbaarheid) kunnen worden vervuld.
- [ ] Toestemming, waar erop wordt geleund, is vrij gegeven, specifiek en herroepbaar.
- [ ] Derden en verwerkers zijn gebonden aan adequate gegevensbeschermingsvoorwaarden.
- [ ] Grensoverschrijdende doorgiften hebben een passend juridisch overdrachtsmechanisme.
- [ ] Toegang tot persoonsgegevens is beperkt, gelogd en beoordeeld.
- [ ] Privacyrisico's voor individuen zijn beoordeeld en beperkt of geëscaleerd.
- [ ] Processen voor detectie en melding van datalekken zijn gedefinieerd.
- [ ] Keuzes voor privacy by design en by default zijn voor de functie gedocumenteerd.
- [ ] De functionaris voor gegevensbescherming of privacyreviewer heeft waar vereist goedgekeurd.

## Checklist voor toegankelijkheid (WCAG)

Voor gebruikersgerichte interfaces, afgestemd op de WCAG-principes.

- [ ] Alle content is bereikbaar en bedienbaar met alleen een toetsenbord.
- [ ] De focusvolgorde is logisch en er is een zichtbare focusindicator.
- [ ] Tekstkleurcontrast haalt de doelverhouding (doorgaans 4,5:1 voor lopende tekst).
- [ ] Afbeeldingen en niet-tekstuele content hebben betekenisvolle alternatieve tekst.
- [ ] Formuliervelden hebben bijbehorende labels en heldere foutmeldingen.
- [ ] Koppen, landmarks en structuur zijn semantisch opgemaakt.
- [ ] Interactieve componenten maken de juiste naam, rol en toestand bekend aan hulptechnologie.
- [ ] Content herschikt en blijft bruikbaar bij 200% zoom en op kleine schermen.
- [ ] Tijdslimieten zijn aanpasbaar en beweging of automatisch afspelende content kan worden gepauzeerd.
- [ ] Kleur is niet het enige middel om informatie over te brengen.
- [ ] Media heeft ondertitels en, waar nodig, transcripten of audiodescriptie.
- [ ] De interface is getest met een schermlezer en geautomatiseerde toegankelijkheidstooling.

## Checklist voor API-ontwerpreview

Voordat een API wordt gepubliceerd of gewijzigd.

- [ ] Naamgeving van resources en bewerkingen is consistent en voorspelbaar.
- [ ] Het contract is gespecificeerd in een machineleesbaar schema (bijvoorbeeld OpenAPI).
- [ ] De versioneringsstrategie is gedefinieerd en achterwaartse compatibiliteit wordt behouden of beheerd.
- [ ] Paginering, filteren en sorteren volgen consistente conventies.
- [ ] Foutresponses gebruiken consistente structuur, codes en uitvoerbare berichten.
- [ ] Authenticatie en autorisatie zijn voor elke bewerking gespecificeerd.
- [ ] Invoervalidatie en groottelimieten zijn gedefinieerd en afgedwongen.
- [ ] Idempotentie is gedefinieerd voor bewerkingen waar herhalingen worden verwacht.
- [ ] Snelheidslimieten, quota en throttlinggedrag zijn gedocumenteerd.
- [ ] Timeouts, herhalingen en faalsemantiek zijn duidelijk voor clients.
- [ ] Blootstelling van gevoelige data in responses is geminimaliseerd en onderbouwd.
- [ ] Documentatie bevat voorbeelden voor elke bewerking en elk foutgeval.
- [ ] Uitfaseringsbeleid en afbouwtijdlijnen zijn gedefinieerd.

## Checklist voor review van architectuurbeslissingen (ADR)

Voor het beoordelen van een voorgesteld architectuurbeslissingsrecord.

- [ ] De context en het op te lossen probleem zijn helder vermeld.
- [ ] De beslissing is ondubbelzinnig vermeld als één enkele keuze.
- [ ] Minstens twee realistische alternatieven zijn overwogen en vergeleken.
- [ ] Gevolgen, zowel positief als negatief, zijn gedocumenteerd.
- [ ] Niet-functionele impact (prestaties, beveiliging, kosten, beheerbaarheid) is behandeld.
- [ ] De beslissing sluit aan op bestaande principes en eerdere ADR's, of vervangt ze expliciet.
- [ ] Getroffen teams en belanghebbenden zijn geraadpleegd.
- [ ] De omkeerbaarheid en de kosten van verandering zijn beoordeeld.
- [ ] Aannames en beperkingen zijn expliciet gemaakt.
- [ ] De status (voorgesteld, geaccepteerd, vervangen) is vastgesteld en gedateerd.
- [ ] De beslissing is vindbaar en gelinkt vanuit relevante systemen.
- [ ] Vervolgacties of migraties zijn vastgelegd als gevolgd werk.

## Checklist voor incidentrespons

Tijdens een actief productie-incident.

- [ ] Roep het incident uit en wijs één incidentcommandant aan.
- [ ] Beoordeel en communiceer ernst, reikwijdte en klantimpact.
- [ ] Open een speciaal communicatiekanaal en incidentrecord.
- [ ] Wijs heldere rollen toe: commandant, communicatieleider en operationeel leider.
- [ ] Geef prioriteit aan beperking en dienst herstellen boven grondoorzaakanalyse.
- [ ] Plaats volgens een vast ritme regelmatige statusupdates aan belanghebbenden.
- [ ] Leg een tijdlijn van gebeurtenissen, acties en beslissingen vast terwijl ze gebeuren.
- [ ] Escaleer naar extra responders of leveranciers wanneer nodig.
- [ ] Breng juridische zaken, beveiliging en compliance op de hoogte als data of regelgeving betrokken is.
- [ ] Verifieer de reparatie en bevestig dat het systeem volledig is hersteld.
- [ ] Sluit het incident formeel en communiceer de oplossing.
- [ ] Plan de schuldvrije nabeschouwing voordat mensen uiteengaan.

## Checklist voor nabeschouwing

Voor de retrospectieve review na een incident.

- [ ] De review is schuldvrij en richt zich op systemen en bijdragende factoren.
- [ ] Een feitelijke tijdlijn met tijdstempels van het incident is gedocumenteerd.
- [ ] Klant- en bedrijfsimpact is gekwantificeerd (duur, reikwijdte, kosten).
- [ ] Detectie is geanalyseerd: hoe en wanneer het probleem werd opgemerkt.
- [ ] Respons is geanalyseerd: wat hielp en wat het herstel vertraagde.
- [ ] Bijdragende oorzaken zijn geïdentificeerd, niet slechts één grondoorzaak.
- [ ] Wat goed ging is vastgelegd, evenals wat fout ging.
- [ ] Actiepunten zijn specifiek, toegewezen aan eigenaren en hebben vervaldata.
- [ ] Actiepunten behandelen preventie, detectie en beperking.
- [ ] Vervolgpunten worden tot voltooiing gevolgd in de normale achterstand.
- [ ] De nabeschouwing wordt breed gedeeld zodat anderen ervan kunnen leren.
- [ ] Systemische patronen over incidenten heen worden periodiek beoordeeld.

## Checklist voor gereedheid van bereikbaarheid

Voordat iemand een bereikbaarheidsdienst begint.

- [ ] De responder heeft toegang tot alle systemen, dashboards en tools die hij of zij nodig heeft.
- [ ] Alarmering bereikt de responder betrouwbaar en is getest.
- [ ] Escalatiepaden en secundaire bereikbaarheidscontacten zijn bekend en actueel.
- [ ] Runbooks bestaan voor de meest voorkomende en ernstigste alarmen.
- [ ] De responder heeft onboarding of meelopen voor deze systemen voltooid.
- [ ] Recente wijzigingen, lopende incidenten en bekende problemen zijn overgedragen.
- [ ] Alarmdrempels zijn afgestemd om ruis en valse oproepen te minimaliseren.
- [ ] De responder weet hoe een incident uit te roepen en de commandant te bereiken.
- [ ] Toegang tot productie is mogelijk vanuit de werkomgeving van de responder.
- [ ] Communicatiekanalen en contacten van belanghebbenden zijn gedocumenteerd.
- [ ] Het bereikbaarheidsrooster is gepubliceerd en de dekking heeft geen gaten.
- [ ] Vergoeding, verwachtingen en belastinglimieten voor bereikbaarheid zijn helder.

## Checklist voor SLO-definitie

Bij het definiëren van een service level objective.

- [ ] De gebruikersreis of het vermogen dat de SLO beschermt is helder geïdentificeerd.
- [ ] Service level indicators (SLI's) zijn gedefinieerd als heldere, meetbare grootheden.
- [ ] SLI's worden waar mogelijk gemeten vanuit het perspectief van de gebruiker.
- [ ] Het doel is gesteld op een niveau dat gebruikers werkelijk nodig hebben, niet 100%.
- [ ] Het meetvenster (bijvoorbeeld voortschrijdend 28 dagen) is gespecificeerd.
- [ ] Het foutbudget afgeleid van het doel is berekend en begrepen.
- [ ] Een beleid definieert wat er gebeurt wanneer het foutbudget is uitgeput.
- [ ] Databronnen voor de SLI's zijn betrouwbaar en geïnstrumenteerd.
- [ ] Alarmering is gekoppeld aan verbrandingssnelheid, niet alleen aan drempelschendingen.
- [ ] Eigenaren en belanghebbenden zijn het eens dat de SLO realistisch en betekenisvol is.
- [ ] De SLO is gedocumenteerd en zichtbaar op een dashboard.
- [ ] Er bestaat een schema om SLO's te beoordelen en te herzien naarmate de service evolueert.

## Checklist voor CI/CD-pijplijn

Voor een continuous-integration- en opleveringspijplijn.

- [ ] Elke commit triggert een geautomatiseerde build- en testrun.
- [ ] De pijplijn faalt snel en rapporteert resultaten helder aan auteurs.
- [ ] Linting, opmaak en statische analyse draaien automatisch.
- [ ] Unit-, integratie- en relevante end-to-endtests draaien in de pijplijn.
- [ ] Beveiligings- en afhankelijkheidsscans draaien bij elke build.
- [ ] Buildartefacten zijn geversioneerd, onveranderlijk en opgeslagen in een register.
- [ ] Geheimen worden veilig geïnjecteerd en nooit in logs afgedrukt.
- [ ] Deployments zijn geautomatiseerd en herhaalbaar over omgevingen.
- [ ] Een deploymentstrategie (canary, blue-green, rolling) is gedefinieerd en wordt gebruikt.
- [ ] Rollback is geautomatiseerd of één gedocumenteerde handeling.
- [ ] Pijplijnrechten volgen minimale rechten en zijn controleerbaar.
- [ ] Pijplijnconfiguratie wordt als code in versiebeheer opgeslagen.
- [ ] Buildherkomst en een software bill of materials worden geproduceerd waar vereist.

## Checklist voor review van infrastructure as code

Voor het beoordelen van infrastructuur gedefinieerd als code.

- [ ] Wijzigingen worden volledig in code uitgedrukt en via de pijplijn toegepast.
- [ ] Een plan of dry-run-uitvoer wordt beoordeeld vóór het toepassen.
- [ ] Toestand wordt veilig opgeslagen met vergrendeling om gelijktijdige wijzigingen te voorkomen.
- [ ] Resources volgen conventies voor naamgeving, tagging en eigenaarschap.
- [ ] IAM-rollen en -beleid met minimale rechten worden gebruikt, zonder jokertekens waar vermijdbaar.
- [ ] Netwerkblootstelling is geminimaliseerd. Geen onbedoelde publieke toegang.
- [ ] Geheimen en gevoelige waarden worden uit een kluis gerefereerd, niet hardgecodeerd.
- [ ] Versleuteling is aangezet voor opslag, databases en transport.
- [ ] Wijzigingen zijn idempotent en veilig om opnieuw toe te passen.
- [ ] De schadezone is begrepen. Destructieve wijzigingen worden benoemd.
- [ ] De kostenimpact van de wijziging is overwogen.
- [ ] Modules zijn herbruikbaar, geversioneerd en getest.
- [ ] Driftdetectie is aanwezig om wijzigingen buiten de pijplijn te vangen.

## Checklist voor release van AI-/ML-modellen

Voordat een machine-learningmodel naar productie wordt uitgebracht.

- [ ] Het beoogde gebruik, de reikwijdte en de beperkingen van het model zijn gedocumenteerd.
- [ ] Herkomst, licenties en toestemming van trainings- en evaluatiedata zijn geverifieerd.
- [ ] Data en model zijn geversioneerd en reproduceerbaar.
- [ ] Prestaties zijn geëvalueerd op representatieve, achtergehouden testdata.
- [ ] Eerlijkheid en bias zijn beoordeeld over relevante subgroepen.
- [ ] Het model is geëvalueerd tegen de zittende of een basislijn.
- [ ] Faalwijzen, randgevallen en gedrag buiten de verdeling zijn begrepen.
- [ ] Risico's van veiligheid, misbruik en schadelijke uitvoer zijn beoordeeld en beperkt.
- [ ] Bewaking op drift, datakwaliteit en prestatievermindering is aanwezig.
- [ ] Een rollback of terugval naar een eerder model of regelgebaseerd pad bestaat.
- [ ] Menselijk toezicht of beroep is voorzien voor ingrijpende beslissingen.
- [ ] Privacyreview dekt trainingsdata en invoer en uitvoer van inferentie.
- [ ] Een modelkaart of gelijkwaardige documentatie is voor belanghebbenden gepubliceerd.

## Checklist voor kwaliteit van datapijplijnen

Voor een datapijplijn die analytics of producten voedt.

- [ ] Bronschema's worden gevalideerd en schemawijzigingen worden gedetecteerd.
- [ ] Inname handelt late, dubbele en records in verkeerde volgorde correct af.
- [ ] Datakwaliteitscontroles (volledigheid, uniekheid, bereiken) draaien automatisch.
- [ ] Mislukte records worden in quarantaine gezet en zichtbaar gemaakt, niet stilletjes laten vallen.
- [ ] Transformaties worden getest met representatieve en randgevalsinvoer.
- [ ] De pijplijn is idempotent en veilig om na falen opnieuw te draaien.
- [ ] Versheid en latentie van uitvoer worden bewaakt tegen verwachtingen.
- [ ] Herkomst is gedocumenteerd zodat afnemers weten waar data vandaan komt.
- [ ] Persoonlijke en gevoelige data is geclassificeerd, gemaskeerd of passend beperkt.
- [ ] Backfills en herverwerking worden ondersteund en zijn gedocumenteerd.
- [ ] Alarmering meldt falen en kwaliteitsschendingen aan eigenaren.
- [ ] Bewaar- en verwijderbeleid wordt op opgeslagen data afgedwongen.
- [ ] Downstreamafnemers en SLA's zijn gedocumenteerd.

## Checklist voor open-sourceinname en licentiereview

Voordat een open-sourcecomponent wordt overgenomen.

- [ ] De licentie van de component is geïdentificeerd en staat op de goedgekeurde lijst.
- [ ] Licentieverplichtingen (naamsvermelding, copyleft, mededelingen) zijn begrepen en nagekomen.
- [ ] Licentiecompatibiliteit met je distributiemodel is bevestigd.
- [ ] Het project wordt actief onderhouden en heeft een gezonde gemeenschap.
- [ ] Bekende kwetsbaarheden zijn gecontroleerd en de versie is actueel.
- [ ] De afhankelijkheid en haar transitieve afhankelijkheden zijn geïnventariseerd.
- [ ] Beveiligingshouding en eerdere incidentgeschiedenis zijn beoordeeld.
- [ ] De component vervult een echte behoefte zonder significante duplicatie.
- [ ] De uitstapkosten en vervangbaarheid van de component zijn overwogen.
- [ ] De component is vastgelegd in de software bill of materials.
- [ ] Een benoemde eigenaar is verantwoordelijk voor het volgen van updates en adviezen.
- [ ] Beleid voor teruggeven en interne forks wordt gevolgd als er wijzigingen zijn.

## Checklist voor risico bij leveranciers / derden

Voordat een externe leverancier of dienst wordt aangenomen.

- [ ] De bedrijfsbehoefte en de data waartoe de leverancier toegang krijgt zijn helder gedefinieerd.
- [ ] De beveiligingshouding van de leverancier is beoordeeld (certificeringen, audits, vragenlijst).
- [ ] Gegevensverwerkingsvoorwaarden, eigendom en verwijdering bij vertrek zijn contractueel helder.
- [ ] De subverwerkers en datalocaties van de leverancier zijn bekendgemaakt en aanvaardbaar.
- [ ] Naleving van relevante regelgeving is geverifieerd.
- [ ] Uptime-, ondersteunings- en SLA-toezeggingen zijn gedocumenteerd.
- [ ] Verplichtingen en termijnen voor melding van inbreuken staan in het contract.
- [ ] Toegang is beperkt tot minimale rechten en intrekbaar.
- [ ] Bedrijfscontinuïteit en de impact van uitval van de leverancier zijn beoordeeld.
- [ ] Een uitstap- en datamigratieplan bestaat om afhankelijkheid te vermijden.
- [ ] Kosten, verlengingsvoorwaarden en prijswijzigingsclausules zijn begrepen.
- [ ] De leverancier is met een reviewdatum aan het risicoregister toegevoegd.

## Checklist voor gereedheid voor overheidscompliance (in ATO-/FedRAMP-stijl)

Voor systemen die formele toestemming om te opereren vereisen.

- [ ] De systeemgrens en datastromen zijn gedefinieerd en gediagrammeerd.
- [ ] Data is gecategoriseerd naar impactniveau en gevoeligheid.
- [ ] De toepasselijke maatregelenbasislijn is gekozen en op maat gemaakt.
- [ ] Een systeembeveiligingsplan documenteert hoe elke maatregel is geïmplementeerd.
- [ ] Maatregelen zijn geïmplementeerd, onderbouwd en aan het plan gekoppeld.
- [ ] Continue bewaking en kwetsbaarheidsscannen zijn operationeel.
- [ ] Een actie- en mijlpalenplan volgt openstaande bevindingen tot herstel.
- [ ] Toegangscontrole, auditlogging en identiteitsbeheer voldoen aan de eisen.
- [ ] Versleuteling gebruikt goedgekeurde algoritmen en gevalideerde modules.
- [ ] Een incidentresponsplan is gedocumenteerd en getest.
- [ ] Een continuïteits- en rampenherstelplan is gedocumenteerd en getest.
- [ ] Een onafhankelijke beoordeling of audit van maatregelen is voltooid.
- [ ] De autoriserende functionaris heeft de risicobeoordeling die nodig is om toestemming te verlenen.
- [ ] Triggers voor heroverweging en het doorlopende autorisatieritme zijn gedefinieerd.
