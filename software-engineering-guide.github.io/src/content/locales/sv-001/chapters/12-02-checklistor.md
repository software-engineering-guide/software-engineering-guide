# 12.2 Checklistor

De här checklistorna är praktiska, färdiga snabbreferenser. Kopiera valfri checklista till en mall för pull requests, en wikisida, ett ärende eller en dagordning för ett granskningsmöte och anpassa punkterna efter ert sammanhang. Behandla varje punkt som något en person kan verifiera och besvara med ja eller nej. En checklista är ett minnesstöd och en gemensam standard, inte en ersättning för omdöme. Ta bort punkter som inte gäller och lägg till punkter som er domän kräver.

Råd för att använda dem väl:

- Håll checklistor tillräckligt korta för att människor faktiskt fyller i dem. Om en checklista rutinmässigt hoppas över är den för lång eller för allmän.
- Automatisera varje punkt en maskin kan verifiera (formatering, tester, skanningar) så att människor lägger uppmärksamheten på omdömespunkterna.
- Versionshantera era checklistor och granska dem periodvis. En checklista som aldrig ändras används sannolikt inte.
- Skilj blockerande punkter från rådgivande när skillnaden spelar roll för er process.

## Checklista för kodgranskning

För granskaren som går igenom någon annans ändring.

- [ ] Ändringen gör det som dess beskrivning och länkade ärende säger att den gör.
- [ ] Omfattningen är fokuserad på en enda logisk angelägenhet. Orelaterade ändringar är utbrutna.
- [ ] Designen passar den befintliga arkitekturen och inför ingen koppling som är enkel att undvika.
- [ ] Kantfall, felvägar och felmoder hanteras, inte bara den glada vägen.
- [ ] Tester finns, är meningsfulla och skulle misslyckas om beteendet regredierade.
- [ ] Namngivning, struktur och kommentarer gör koden begriplig för en framtida läsare.
- [ ] Inga hemligheter, inloggningsuppgifter, tokens eller personuppgifter är incheckade.
- [ ] Säkerhetskänsliga indata valideras, kodas eller parametriseras på lämpligt sätt.
- [ ] Publika gränssnitt, kontrakt och bakåtkompatibilitet bevaras eller versionshanteras avsiktligt.
- [ ] Loggning, mått och felrapportering räcker för att driva ändringen i produktion.
- [ ] Dokumentation, körböcker och konfiguration är uppdaterade så att de matchar ändringen.
- [ ] Återkoppling är uppdelad i blockerande frågor mot förslag och formulerad om koden.

## Checklista för pull request-författaren

För författaren innan granskning begärs.

- [ ] PR:en är liten och fokuserad nog för att granskas noggrant i ett sammanhang.
- [ ] Beskrivningen anger vad som ändrats, varför och hur det verifierats.
- [ ] Det länkade ärendet, problemet eller designdokumentet ger granskare nödvändigt sammanhang.
- [ ] Alla automatiserade kontroller passerar lokalt eller i CI (bygge, lint, format, tester, skanningar).
- [ ] Nytt och ändrat beteende täcks av tester.
- [ ] Mekaniska refaktoreringar är åtskilda från beteendeändringar.
- [ ] Självgranskningen är klar: du har läst din egen diff rad för rad.
- [ ] Ingen felsökningskod, utkommenterade block, hemligheter eller överblivna filer återstår.
- [ ] Databasmigreringar, funktionsflaggor och konfigurationsändringar är dokumenterade och reversibla.
- [ ] Brytande ändringar lyfts fram uttryckligen med en migreringsväg.
- [ ] Skärmbilder, inspelningar eller exempelutdata finns med där de underlättar granskningen.
- [ ] Rätt granskare och eventuella obligatoriska rollbaserade godkännare är begärda.

## Definition av klart (Definition of Done)

Den gemensamma standard ett arbetsobjekt måste möta innan det anses vara slutfört.

- [ ] Acceptanskriterierna i ärendet är alla uppfyllda och kan demonstreras.
- [ ] Koden är kamratgranskad och godkänd av de obligatoriska granskarna.
- [ ] Automatiserade tester är skrivna, godkända och sammanslagna med ändringen.
- [ ] Koden är sammanslagen i huvudgrenen och driftsätts rent genom flödet.
- [ ] Inga kända defekter över den överenskomna allvarlighetströskeln är öppna.
- [ ] Dokumentation, hjälptexter och körböcker är uppdaterade.
- [ ] Observerbarhet finns på plats: relevanta loggar, mått och larm finns.
- [ ] Säkerhets- och integritetskonsekvenser har beaktats och hanterats.
- [ ] Tillgänglighetskraven för ändringen är uppfyllda där den är användarvänd.
- [ ] Funktionsflaggor är konfigurerade och utrullningsplanen är överenskommen.
- [ ] Produktägaren eller intressenten har accepterat utfallet.
- [ ] Allt uppföljningsarbete är fångat som spårade ärenden, inte lämnat underförstått.

## Produktionslansering / beredskap för go-live

Innan en betydande ändring eller en ny tjänst levereras till produktion.

- [ ] Utrullningsplanen är dokumenterad, inklusive stegvisa eller kanariesteg och framgångskriterier.
- [ ] Återställningsplanen är dokumenterad, testad och kan genomföras snabbt.
- [ ] Kapacitets- och belastningstester visar att systemet klarar förväntad och maximal efterfrågan.
- [ ] Övervakning, paneler och larm är live och validerade före lanseringen.
- [ ] Jourtäckning är schemalagd och de som svarar känner systemet.
- [ ] Körböcker finns för de mest sannolika fel- och driftscenarierna.
- [ ] Beroenden, integrationer och tredje parter är bekräftat redo och ratebegränsningar är förstådda.
- [ ] Säkerhetsgranskning och obligatoriska godkännanden är klara.
- [ ] Datamigrering, om någon, är testad från början till slut med en verifierad reträtt.
- [ ] Funktionsflaggor gör det möjligt att stänga av ändringen utan omdriftsättning.
- [ ] Juridiska, integritets- och efterlevnadsgodkännanden är inhämtade där de krävs.
- [ ] Kommunikationsplanen täcker intressenter, support och kunder.
- [ ] Ett go/no-go-beslut fattas av namngivna ägare mot uttryckliga kriterier.

## Säkerhetsgranskning / checklista för hotmodell

För att bedöma säkerhetsläget hos en ändring eller ett system.

- [ ] Förtroendegränser och dataflöden är identifierade och dokumenterade.
- [ ] Autentisering upprätthålls vid varje ingångspunkt som kräver det.
- [ ] Auktoriseringskontroller upprätthåller minsta behörighet för varje åtgärd och resurs.
- [ ] All extern indata valideras, och utdata kodas för sin mottagare.
- [ ] Hemligheter lagras i ett hanterat valv, aldrig i kod eller konfiguration, och kan roteras.
- [ ] Data är krypterad under överföring och i vila så som klassificeringen kräver.
- [ ] Beroenden skannas efter kända sårbarheter och hålls aktuella.
- [ ] Injektions-, deserialiserings- och SSRF-risker är mildrade för opålitlig indata.
- [ ] Säkerhetsrelevanta händelser loggas utan att känsliga data registreras.
- [ ] Ratebegränsning, kvoter och missbruksskydd vaktar exponerade ändpunkter.
- [ ] Felmeddelanden läcker inte stackspår, interna detaljer eller känslig information.
- [ ] Hot identifierade via STRIDE eller liknande är registrerade med åtgärder eller accepterad risk.
- [ ] Säkerhetstestning (SAST, DAST eller penetrationstestning) är planerad eller klar.

## Checklista för integritet och dataskydd (DPIA-stil)

För behandling som omfattar personuppgifter eller känsliga uppgifter.

- [ ] De insamlade personuppgifterna är inventerade, klassificerade och minimerade till det som behövs.
- [ ] Den rättsliga grunden eller befogenheten för varje behandlingsändamål är dokumenterad.
- [ ] Ändamålsbegränsning upprätthålls: data används bara för de angivna ändamålen.
- [ ] Lagringsperioder är definierade och radering eller anonymisering är automatiserad.
- [ ] Registrerades rättigheter (tillgång, rättelse, radering, portabilitet) kan uppfyllas.
- [ ] Samtycke, där man förlitar sig på det, är frivilligt, specifikt och kan återkallas.
- [ ] Tredje parter och biträden är bundna av adekvata dataskyddsvillkor.
- [ ] Gränsöverskridande överföringar har en lämplig rättslig överföringsmekanism.
- [ ] Åtkomst till personuppgifter är begränsad, loggad och granskad.
- [ ] Integritetsrisker för individer är bedömda och mildrade eller eskalerade.
- [ ] Processer för att upptäcka och anmäla dataintrång är definierade.
- [ ] Val om inbyggt dataskydd och dataskydd som standard är dokumenterade för funktionen.
- [ ] Dataskyddsombudet eller integritetsgranskaren har godkänt där det krävs.

## Tillgänglighet (WCAG), checklista

För användarvända gränssnitt, anpassad till WCAG-principerna.

- [ ] Allt innehåll kan nås och hanteras enbart med tangentbord.
- [ ] Fokusordningen är logisk och en synlig fokusindikator finns.
- [ ] Textens färgkontrast uppfyller målkvoten (typiskt 4,5:1 för brödtext).
- [ ] Bilder och icke-textuellt innehåll har meningsfull alternativtext.
- [ ] Formulärfält har tillhörande etiketter och tydliga felmeddelanden.
- [ ] Rubriker, landmärken och struktur är semantiskt uppmärkta.
- [ ] Interaktiva komponenter exponerar korrekt namn, roll och tillstånd för hjälpmedelsteknik.
- [ ] Innehållet omflödar och förblir användbart vid 200 % zoom och på små skärmar.
- [ ] Tidsgränser är justerbara, och rörelse eller automatiskt spelande innehåll kan pausas.
- [ ] Färg är inte det enda sättet att förmedla information.
- [ ] Media har undertexter och, där det behövs, transkriptioner eller syntolkning.
- [ ] Gränssnittet är testat med en skärmläsare och automatiserade tillgänglighetsverktyg.

## Checklista för granskning av API-design

Innan ett API publiceras eller ändras.

- [ ] Namngivning av resurser och operationer är konsekvent och förutsägbar.
- [ ] Kontraktet är specificerat i ett maskinläsbart schema (till exempel OpenAPI).
- [ ] Versioneringsstrategin är definierad och bakåtkompatibilitet bevaras eller hanteras.
- [ ] Paginering, filtrering och sortering följer konsekventa konventioner.
- [ ] Felsvar använder konsekvent struktur, koder och handlingsbara meddelanden.
- [ ] Autentisering och auktorisering är specificerade för varje operation.
- [ ] Indatavalidering och storleksgränser är definierade och upprätthålls.
- [ ] Idempotens är definierad för operationer där omförsök förväntas.
- [ ] Ratebegränsningar, kvoter och strypningsbeteende är dokumenterade.
- [ ] Timeouter, omförsök och felsemantik är tydliga för klienter.
- [ ] Exponering av känsliga data i svar är minimerad och motiverad.
- [ ] Dokumentationen innehåller exempel för varje operation och felfall.
- [ ] Policy för utfasning och tidslinjer för avveckling är definierade.

## Checklista för granskning av arkitekturbeslut (ADR)

För att granska en föreslagen arkitekturbeslutslogg.

- [ ] Sammanhanget och problemet som löses är tydligt angivna.
- [ ] Beslutet är entydigt angivet som ett enda val.
- [ ] Minst två realistiska alternativ övervägdes och jämfördes.
- [ ] Konsekvenser, både positiva och negativa, är dokumenterade.
- [ ] Icke-funktionella effekter (prestanda, säkerhet, kostnad, driftbarhet) behandlas.
- [ ] Beslutet stämmer med befintliga principer och tidigare ADR, eller ersätter dem uttryckligen.
- [ ] Berörda team och intressenter konsulterades.
- [ ] Reversibilitet och kostnad för förändring är bedömda.
- [ ] Antaganden och begränsningar är gjorda uttryckliga.
- [ ] Statusen (föreslagen, accepterad, ersatt) är satt och daterad.
- [ ] Beslutet är sökbart och länkat från relevanta system.
- [ ] Eventuella uppföljningsåtgärder eller migreringar är fångade som spårat arbete.

## Checklista för incidentrespons

Under en pågående produktionsincident.

- [ ] Deklarera incidenten och utse en enda incidentledare.
- [ ] Bedöm och kommunicera allvarlighet, omfattning och kundpåverkan.
- [ ] Öppna en dedikerad kommunikationskanal och ett incidentregister.
- [ ] Tilldela tydliga roller: ledare, kommunikationsansvarig och driftansvarig.
- [ ] Prioritera mildring och återställning av tjänsten framför grundorsaksanalys.
- [ ] Posta regelbundna statusuppdateringar till intressenter enligt en fast takt.
- [ ] Fånga en tidslinje över händelser, åtgärder och beslut medan de sker.
- [ ] Eskalera till ytterligare respondenter eller leverantörer vid behov.
- [ ] Underrätta juridik, säkerhet och regelefterlevnad om data eller reglering berörs.
- [ ] Verifiera rättelsen och bekräfta att systemet har återhämtat sig fullt ut.
- [ ] Stäng incidenten formellt och kommunicera lösningen.
- [ ] Schemalägg den skuldfria efterhandsgranskningen innan människor skingras.

## Checklista för efterhandsgranskning

För den retrospektiva granskningen efter en incident.

- [ ] Granskningen är skuldfri och fokuserar på system och bidragande faktorer.
- [ ] En faktabaserad, tidsstämplad tidslinje över incidenten är dokumenterad.
- [ ] Kund- och affärspåverkan är kvantifierad (varaktighet, omfattning, kostnad).
- [ ] Upptäckten är analyserad: hur och när problemet märktes.
- [ ] Responsen är analyserad: vad som hjälpte och vad som fördröjde återhämtningen.
- [ ] Bidragande orsaker är identifierade, inte bara en enda grundorsak.
- [ ] Vad som gick bra är dokumenterat, liksom vad som gick fel.
- [ ] Åtgärdspunkter är specifika, tilldelade ägare och har förfallodatum.
- [ ] Åtgärdspunkter adresserar förebyggande, upptäckt och mildring.
- [ ] Uppföljningspunkter spåras till slutförande i den vanliga backloggen.
- [ ] Efterhandsgranskningen delas brett så att andra kan lära av den.
- [ ] Systemiska mönster över incidenter granskas periodvis.

## Checklista för jourberedskap

Innan någon tar ett jourpass.

- [ ] Den som svarar har åtkomst till alla system, paneler och verktyg hen behöver.
- [ ] Larm når den som svarar pålitligt och är testade.
- [ ] Eskaleringsvägar och sekundära jourkontakter är kända och aktuella.
- [ ] Körböcker finns för de vanligaste och allvarligaste larmen.
- [ ] Den som svarar har genomfört introduktion eller skuggning för dessa system.
- [ ] Nyliga ändringar, pågående incidenter och kända problem är överlämnade.
- [ ] Larmtrösklar är trimmade för att minimera brus och falska larm.
- [ ] Den som svarar vet hur man deklarerar en incident och når ledaren.
- [ ] Åtkomst till produktion är möjlig från den som svarars arbetsmiljö.
- [ ] Kommunikationskanaler och intressentkontakter är dokumenterade.
- [ ] Jourschemat är publicerat och täckningen har inga luckor.
- [ ] Ersättning, förväntningar och arbetsbelastningsgränser för jour är tydliga.

## Checklista för SLO-definition

När ett servicenivåmål definieras.

- [ ] Användarresan eller förmågan som SLO:n skyddar är tydligt identifierad.
- [ ] Servicenivåindikatorer (SLI) är definierade som tydliga, mätbara storheter.
- [ ] SLI:er mäts ur användarens perspektiv där det är möjligt.
- [ ] Målet är satt på en nivå användare faktiskt behöver, inte 100 %.
- [ ] Mätfönstret (till exempel rullande 28 dagar) är specificerat.
- [ ] Felbudgeten härledd ur målet är beräknad och förstådd.
- [ ] En policy definierar vad som händer när felbudgeten är förbrukad.
- [ ] Datakällor för SLI:erna är pålitliga och instrumenterade.
- [ ] Larm är knutna till förbränningstakt, inte bara tröskelbrott.
- [ ] Ägare och intressenter är överens om att SLO:n är realistisk och meningsfull.
- [ ] SLO:n är dokumenterad och synlig på en panel.
- [ ] Ett schema finns för att granska och revidera SLO:er när tjänsten utvecklas.

## Checklista för CI/CD-flöde

För ett flöde för kontinuerlig integrering och leverans.

- [ ] Varje incheckning utlöser ett automatiserat bygge och en testkörning.
- [ ] Flödet misslyckas snabbt och rapporterar resultat tydligt till författare.
- [ ] Linting, formatering och statisk analys körs automatiskt.
- [ ] Enhets-, integrations- och relevanta helhetstester körs i flödet.
- [ ] Säkerhets- och beroendeskanning körs vid varje bygge.
- [ ] Byggartefakter är versionshanterade, oföränderliga och lagrade i ett register.
- [ ] Hemligheter injiceras säkert och skrivs aldrig ut i loggar.
- [ ] Driftsättningar är automatiserade och upprepbara över miljöer.
- [ ] Driftsättningsstrategi (kanarie, blågrön, rullande) är definierad och används.
- [ ] Återställning är automatiserad eller en enda dokumenterad åtgärd.
- [ ] Flödesbehörigheter följer minsta behörighet och är granskningsbara.
- [ ] Flödeskonfigurationen lagras i versionshantering som kod.
- [ ] Byggursprung och en materialförteckning för programvara produceras där det krävs.

## Checklista för granskning av infrastruktur som kod

För att granska infrastruktur definierad som kod.

- [ ] Ändringar uttrycks helt i kod och tillämpas genom flödet.
- [ ] En plan eller torrkörningsutdata granskas före tillämpning.
- [ ] Tillstånd lagras säkert med låsning för att förhindra samtidiga ändringar.
- [ ] Resurser följer konventioner för namngivning, märkning och ägarskap.
- [ ] IAM-roller och -policyer med minsta behörighet används, utan jokertecken där det går att undvika.
- [ ] Nätverksexponeringen är minimerad. Ingen oavsiktlig offentlig åtkomst.
- [ ] Hemligheter och känsliga värden refereras från ett valv, inte hårdkodade.
- [ ] Kryptering är aktiverad för lagring, databaser och överföring.
- [ ] Ändringar är idempotenta och säkra att tillämpa på nytt.
- [ ] Sprängradien är förstådd. Destruktiva ändringar lyfts fram.
- [ ] Ändringens kostnadspåverkan är beaktad.
- [ ] Moduler är återanvändbara, versionshanterade och testade.
- [ ] Driftdetektering finns på plats för att fånga ändringar utanför flödet.

## Checklista för release av AI/ML-modell

Innan en maskininlärningsmodell släpps till produktion.

- [ ] Modellens avsedda användning, omfattning och begränsningar är dokumenterade.
- [ ] Ursprung, licensiering och samtycke för tränings- och utvärderingsdata är verifierade.
- [ ] Data och modell är versionshanterade och reproducerbara.
- [ ] Prestanda utvärderas på representativa, undanhållna testdata.
- [ ] Rättvisa och bias bedöms över relevanta undergrupper.
- [ ] Modellen utvärderas mot den befintliga eller en baslinje.
- [ ] Felmoder, kantfall och beteende utanför fördelningen är förstådda.
- [ ] Säkerhets-, missbruks- och skadliga-utdata-risker är bedömda och mildrade.
- [ ] Övervakning av drift, datakvalitet och prestandaförsämring finns på plats.
- [ ] En återställning eller reserv till en tidigare modell eller regelbaserad väg finns.
- [ ] Mänsklig tillsyn eller överklagande tillhandahålls för konsekvensfulla beslut.
- [ ] Integritetsgranskningen täcker träningsdata samt inferensens indata och utdata.
- [ ] Ett modellkort eller motsvarande dokumentation publiceras för intressenter.

## Checklista för datapipelinens kvalitet

För en datapipeline som matar analys eller produkter.

- [ ] Källdataschemas valideras och schemaändringar upptäcks.
- [ ] Inläsningen hanterar sena, duplicerade och osorterade poster korrekt.
- [ ] Datakvalitetskontroller (fullständighet, unikhet, intervall) körs automatiskt.
- [ ] Misslyckade poster sätts i karantän och lyfts fram, släpps inte tyst.
- [ ] Transformationer testas med representativa indata och kantfallsindata.
- [ ] Pipelinen är idempotent och säker att köra om efter fel.
- [ ] Utdatas färskhet och latens övervakas mot förväntningar.
- [ ] Ursprung (lineage) är dokumenterat så att konsumenter vet var data kommer från.
- [ ] Personuppgifter och känsliga data är klassificerade, maskerade eller begränsade på lämpligt sätt.
- [ ] Efterfyllnad och ombearbetning stöds och är dokumenterade.
- [ ] Larm underrättar ägare om fel och kvalitetsbrott.
- [ ] Policyer för lagring och radering upprätthålls på lagrade data.
- [ ] Efterföljande konsumenter och SLA:er är dokumenterade.

## Checklista för intag av öppen källkod och licensgranskning

Innan en komponent med öppen källkod tas i bruk.

- [ ] Komponentens licens är identifierad och finns på den godkända listan.
- [ ] Licensskyldigheter (erkännande, copyleft, meddelanden) är förstådda och uppfyllda.
- [ ] Licenskompatibilitet med er distributionsmodell är bekräftad.
- [ ] Projektet underhålls aktivt och har en frisk gemenskap.
- [ ] Kända sårbarheter är kontrollerade och versionen är aktuell.
- [ ] Beroendet och dess transitiva beroenden är inventerade.
- [ ] Säkerhetsläget och tidigare incidenthistorik är granskade.
- [ ] Komponenten fyller ett verkligt behov utan betydande duplicering.
- [ ] Utträdeskostnaden och utbytbarheten för komponenten är beaktade.
- [ ] Komponenten är registrerad i materialförteckningen för programvara.
- [ ] En namngiven ägare ansvarar för att följa uppdateringar och säkerhetsmeddelanden.
- [ ] Policyer för bidrag tillbaka och interna förgreningar följs om den modifieras.

## Checklista för leverantörs-/tredjepartsrisk

Innan en extern leverantör eller tjänst tas in.

- [ ] Affärsbehovet och de data leverantören får åtkomst till är tydligt definierade.
- [ ] Leverantörens säkerhetsläge är bedömt (certifieringar, revisioner, frågeformulär).
- [ ] Villkor för databehandling, ägarskap och radering vid utträde är avtalsmässigt tydliga.
- [ ] Leverantörens underbiträden och dataplatser är redovisade och godtagbara.
- [ ] Efterlevnad av relevanta regleringar är verifierad.
- [ ] Åtaganden om drifttid, support och SLA är dokumenterade.
- [ ] Skyldigheter och tidsfrister för intrångsanmälan finns i avtalet.
- [ ] Åtkomst är avgränsad till minsta behörighet och kan återkallas.
- [ ] Verksamhetskontinuitet och konsekvenserna av leverantörens fel är bedömda.
- [ ] En utträdes- och datamigreringsplan finns för att undvika inlåsning.
- [ ] Kostnader, förnyelsevillkor och klausuler om prisändringar är förstådda.
- [ ] Leverantören läggs till i riskregistret med ett granskningsdatum.

## Beredskapschecklista för myndighetsefterlevnad (ATO / FedRAMP-stil)

För system som kräver formellt tillstånd att drivas.

- [ ] Systemgränsen och dataflödena är definierade och illustrerade.
- [ ] Data är kategoriserad efter konsekvensnivå och känslighet.
- [ ] Den tillämpliga kontrollbaslinjen är vald och anpassad.
- [ ] En systemsäkerhetsplan dokumenterar hur varje kontroll implementeras.
- [ ] Kontroller är implementerade, belagda och kopplade till planen.
- [ ] Kontinuerlig övervakning och sårbarhetsskanning är i drift.
- [ ] En åtgärds- och milstolpeplan spårar öppna fynd till åtgärd.
- [ ] Åtkomstkontroll, revisionsloggning och identitetshantering möter kraven.
- [ ] Kryptering använder godkända algoritmer och validerade moduler.
- [ ] En incidentresponsplan är dokumenterad och testad.
- [ ] En kontinuitets- och katastrofåterställningsplan är dokumenterad och testad.
- [ ] En oberoende bedömning eller revision av kontrollerna är genomförd.
- [ ] Den beslutande tjänstemannen har den riskbedömning som behövs för att bevilja tillstånd.
- [ ] Utlösare för förnyat tillstånd och takten för löpande tillstånd är definierade.
