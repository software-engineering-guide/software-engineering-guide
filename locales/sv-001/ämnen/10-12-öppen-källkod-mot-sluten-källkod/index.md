# 10.12 Öppen källkod mot sluten källkod

## Översikt och motivation

Nästan varje modernt system är en blandning av programvara ni skrev, programvara ni köpte och programvara ni tog gratis. Två av de tre kommer med ett grundläggande val: är programvaran **öppen källkod** eller **sluten källkod**? **[Programvara med öppen källkod](https://en.wikipedia.org/wiki/Open-source_software) (OSS)** distribueras under en licens som ger alla rätten att använda, studera, ändra och vidaredistribuera källkoden, de människoläsbara instruktioner som definierar programmet. **Programvara med sluten källkod**, även kallad **[proprietär programvara](https://en.wikipedia.org/wiki/Proprietary_software)**, distribueras som en färdig produkt vars källkod leverantören håller privat. Ni får rätten att köra den under en licens, men inte att inspektera eller ändra hur den fungerar. En mellankategori, **[programvara med tillgänglig källkod](https://en.wikipedia.org/wiki/Source-available_software)**, publicerar källkoden för läsning men begränsar användning, ändring eller vidaredistribution. Den är *synlig* men inte *öppen* enligt standarddefinitionen.

Två förtydliganden spelar roll innan ni jämför dem. För det första är "fri" tvetydigt. Gemenskapen skiljer **fri-som-i-frihet** (friheten att ändra och dela, ibland skrivet "libre") från **fri-som-i-pris** (noll kostnad, "gratis"). Öppen källkod handlar om frihet, inte nödvändigtvis pris. För det andra delar sig licenser för öppen källkod i två familjer. **[Permissiva licenser](https://en.wikipedia.org/wiki/Permissive_software_license)** (som [MIT](https://en.wikipedia.org/wiki/MIT_License), BSD och Apache 2.0) låter er göra nästan vad som helst, inklusive att bädda in koden i en sluten produkt. **[Copyleft](https://en.wikipedia.org/wiki/Copyleft)-licenser** (som [GNU General Public License](https://en.wikipedia.org/wiki/GNU_General_Public_License), GPL) kräver att härledda verk ni distribuerar också släpps under samma öppna villkor, en ömsesidighetsregel ibland kallad "viral" av kritiker och "dela-lika" av förespråkare.

Det här kapitlet ser på valet från två sidor. Som **konsument** avgör ni om ni ska anta en komponent med öppen källkod eller en proprietär. Som **producent** avgör ni om ni ska öppna programvara ni byggde. För stora företag och särskilt myndigheter bär båda besluten tyngd långt bortom licensfilen. De rör upphandling (kapitel 10.3), digital suveränitet (kapitel 10.11), leveranskedjesäkerhet (kapitel 4.2), interoperabilitet (kapitel 3.8) och kalkylen bygga-eller-köpa (kapitel 6.1).

## Nyckelprinciper

- **Licensen, inte priset, definierar "öppen."** Läs licensen. Gratis och öppen källkod är olika påståenden.
- **Ingendera modellen är i sig säkrare.** Båda kan vara utmärkta eller vårdslösa. Praxisen kring koden spelar större roll än dess öppenhet.
- **Öppenhet är en hävstång för minskat beroende.** Åtkomst till källkod är det yttersta skyddet mot [leverantörsinlåsning](https://en.wikipedia.org/wiki/Vendor_lock-in).
- **Ni äger alltid driftbördan.** Gratis att skaffa är aldrig gratis att driva. [Total ägandekostnad](https://en.wikipedia.org/wiki/Total_cost_of_ownership) berättar den verkliga historien.
- **Särskiljande förblir slutet, standardvara kan öppnas.** Öppna det som inte särskiljer er. Vakta det som gör det.
- **Copyleft har konsekvenser.** Förstå ömsesidighetsskyldigheter innan ni bäddar in copyleft-kod i en produkt ni distribuerar.
- **En levande gemenskap är en tillgång. Ett övergivet repositorium är en skuld.** Bedöm projektet, inte bara licensen.

## Rekommendationer

### Utvärdera en komponent efter projektet, inte bara licensen

Innan ni antar något beroende, öppen källkod eller proprietärt, bedöm dess hälsa: releasetakt, antal och mångfald av underhållare, lyhördhet för säkerhetsrapporter och bredden på adoptionen. Ett bibliotek med öppen källkod med en enda underhållare och en liten proprietär leverantör bär samma **bussfaktorrisk** (faran att ett projekt kollapsar om en eller några få nyckelpersoner lämnar). Föredra komponenter med en bred bidragsgivarbas eller en finansiellt sund leverantör och registrera bedömningen som en del av due diligence (kapitel 10.2, 4.2).

### Läs och följ licenser som en förstklassig skyldighet

Underhåll en inventering av varje komponent och dess licens och upprätthåll en policy om vilka licensfamiljer som är acceptabla för vilka användningar. Den kritiska skillnaden är copyleft. **Permissiv** kod (MIT, Apache 2.0) kan i allmänhet bäddas in i slutna produkter fritt. **Stark copyleft** (GPL) kan förplikta er att släppa ert eget distribuerade derivat under samma villkor. Använd automatisk **programvarukompositionsanalys (SCA)**, verktyg som skannar era beroenden för att identifiera komponenter, licenser och kända sårbarheter, och generera en **materiallista för programvara (SBOM)**, en formell lista över varje komponent i en produkt (kapitel 10.3, 4.2).

### Bedöm säkerhet efter praxis, inte efter öppenhet

Anta inte att öppen källkod är säker på grund av **"många ögon"-argumentet** ([Linus lag](https://en.wikipedia.org/wiki/Linus%27s_law): "med tillräckligt många ögon är alla buggar triviala"). Och anta inte att proprietär kod är säker genom **[säkerhet genom obskuritet](https://en.wikipedia.org/wiki/Security_through_obscurity)** (den felaktiga tron att dölja källkod döljer brister). Många ögon hjälper bara om kvalificerade människor faktiskt tittar, och många vitt använda projekt är tunt underhållna. Båda modellerna bär **leveranskedjerisk**: öppen källkod genom komprometterade eller övergivna beroenden, proprietär genom ogenomskinlig kod och uppdateringskanaler ni inte kan inspektera. Fäst versioner, verifiera ursprung, skanna kontinuerligt och bevaka rådgivningar oavsett modell (kapitel 4.2).

### Designa för utträde och interoperabilitet

Föredra komponenter som talar öppna standarder och portabla dataformat, så att ni kan ersätta dem senare (kapitel 3.8, 10.11). Med öppen källkod får ni det yttersta utträdet: om ett projekt stannar av kan ni **[förgrena](https://en.wikipedia.org/wiki/Fork_(software_development))** det (skapa och underhålla er egen kopia). Med proprietär programvara, förhandla skydd i förväg: dataexport i öppna format, dokumenterade API:er och **[källkodsdeponering](https://en.wikipedia.org/wiki/Source_code_escrow)** (ett rättsligt arrangemang där leverantören deponerar källkod hos en tredje part, utlämnad till er om leverantören fallerar). Designa så att ingen enskild komponent, av endera slaget, kan hålla ert system som gisslan.

### Väg total ägandekostnad, inte klisterpris

Jämför alternativ på **total ägandekostnad (TCO)**, den fulla livstidskostnaden inklusive anskaffning, integration, drift, support, utbildning, uppgraderingar och eventuell ersättning, snarare än enbart licensavgifter. Öppen källkod byter ofta licenskostnad mot högre drift- och bemanningskostnad. Proprietär programvara byter ofta förutsägbara prenumerationsavgifter mot inlåsning och mindre kontroll. Inkludera kostnaden för själva modellen: självstödjande öppen källkod behöver intern kompetens, medan proprietär programvara behöver leverantörshanteringskapacitet.

### Som producent, öppna det som inte särskiljer er

Klassificera er egen programvara i det som ger konkurrens- eller uppdragsfördel och det som är oskiljande rörmokeri. Behåll det särskiljande proprietärt. Överväg att öppna standardinfrastrukturen, där en gemenskap kan dela underhåll och förbättring. För myndigheter, väg **"offentliga pengar, offentlig kod"** (principen att programvara finansierad av skattebetalarna som standard bör vara offentligt tillgänglig) som en drivkraft för transparens, återanvändning och suveränitet (kapitel 10.5, 10.11). Välj licensen medvetet: permissiv för att maximera adoption, copyleft för att hålla ekosystemet öppet.

## Avvägningar: för- och nackdelar

| Dimension | Öppen källkod | Sluten / proprietär |
|---|---|---|
| **Anskaffningskostnad** | Vanligen noll att skaffa | Licens- eller prenumerationsavgift |
| **Total ägandekostnad** | Kostnad skiftar till drift och personal | Mer förutsägbar, men inlåsningspremie |
| **Kontroll & anpassning** | Full: ni kan läsa och ändra källkoden | Begränsad till det leverantören exponerar |
| **Support & ansvarsskyldighet** | Gemenskap, eller betald tredje part. Ingen enskild att hålla ansvarig | Avtalsenlig support och en tydlig ansvarig part |
| **Säkerhetsställning** | Granskningsbar. "Många ögon" om verkligen underhållen | Leverantörshanterad. Ogenomskinlig. Obskuritet är inte skydd |
| **Livslängd / övergivande** | Kan förgrenas om underhållet. Kan ändå vissna | Beror på leverantörens bärkraft och färdplan |
| **Leverantörsinlåsning** | Låg: källkod och öppna format möjliggör utträde | Hög om inte mildrad av standarder och deponering |
| **Ekosystem** | Öppen gemenskap och interoperabilitet | Kurerat, integrerat, ibland inhägnat |

Den återkommande spänningen är **kontroll mot bekvämlighet och ansvarsskyldighet**. Öppen källkod maximerar kontroll, granskningsbarhet och frihet från inlåsning, men ber er tillhandahålla förmågan, integrationen och supporten själva. Proprietär programvara levererar en stödd, integrerad, ansvarig produkt med ett avtal att upprätthålla, men avstår kontroll och inbjuder till inlåsning. Lösningen är sällan allt-eller-inget. De flesta mogna egendomar blandar grunder med öppen källkod med proprietära system där support, ansvarsskyldighet eller specialiserad förmåga motiverar avvägningen.

## Frågor att diskutera med ditt team

1. **Upprätthåller vi en licenspolicy med automatisk SCA och SBOM:er i pipelinen, särskilt för att fånga stark copyleft innan den levereras?** Att bädda in ett GPL-bibliotek i en distribuerad proprietär produkt kan förplikta er att släppa er egen källkod, och den överraskningen dyker vanligen upp sent, när den är dyr att reda ut. Underhåll en inventering av varje komponent och dess licens, upprätthåll vilka licensfamiljer som är acceptabla för vilka användningar och kör programvarukompositionsanalys automatiskt så att pipelinen blockerar överträdelser i stället för att en jurist fångar dem vid leveranstillfället. Generera en SBOM som en självklarhet. För en stor eller myndighetsegendom är detta också leveranskedjehygien och ofta ett upphandlingskrav. Ta med er nuvarande licensinventering, eller det faktum att ni inte har någon, och avgör vem som äger policyn.

2. **När vi antar ett beroende, bedömer vi projektets hälsa och bussfaktor som due diligence?** Ett bibliotek med öppen källkod med en enda underhållare och en liten proprietär leverantör bär samma risk: projektet kollapsar om en eller några få nyckelpersoner lämnar. Innan ni antar något, bedöm releasetakt, antal och mångfald av underhållare, lyhördhet för säkerhetsrapporter och bredden på adoptionen och registrera bedömningen. Ingendera modellen är säkrare som standard. "Många ögon" hjälper bara om kvalificerade människor faktiskt tittar, och många vitt använda projekt är tunt underhållna. Ta med de tre eller fyra beroenden er produkt mest förlitar sig på och fråga, för vart och ett, hur många personer som skulle behöva gå därifrån innan det blev ert problem. Om ni inte kan svara är det bedömningen ni är skyldiga er själva.

3. **När vi köper proprietärt, säkrar vi utträdesskydd i förväg?** Proprietär programvara erbjuder ansvarsskyldighet och bekvämlighet i utbyte mot kontroll, och den dolda kostnaden är inlåsning: byteskostnader som låter en leverantör höja priser eller försämra tjänsten med liten möjlighet till prövning. Förhandla skydden innan ni skriver under, när ni fortfarande har hävstång: dataexport i öppna format, dokumenterade API:er och källkodsdeponering som släpper källkoden om leverantören fallerar. Med öppen källkod är ert utträde förmågan att förgrena. Med proprietärt måste ni skriva in utträdet i avtalet. Ta med era mest kritiska proprietära system och fråga vad som faktiskt händer om leverantören fördubblar priset eller går under. Om svaret är "vi sitter fast", rätta avtalet vid förnyelse.

4. **För programvaran vi bygger själva, hur avgör vi vad vi ska öppna och vad vi ska hålla stängt, och vem har befogenhet att göra det avgörandet?** Gör det fel åt ena hållet och ni ger bort just den kod som särskiljer er. Gör det fel åt andra hållet och ni hamstrar standardrörmokeri vars underhåll en gemenskap gärna skulle dela. De konkurrerande trycken är verkliga: ingenjörer vill ha rekryterings- och ryktesfördelen av ett publikt repositorium, medan produkt och juridik oroar sig för att ge rivaler en fördel eller exponera en säkerhetskänslig heuristik. Ta med en ärlig klassificering av era system i uppdragsskiljande mot oskiljande infrastruktur och namnge personen eller nämnden som godkänner en release, eftersom ett ad hoc-beslut fattat av den som pushade repositoriet är hur kronjuveler läcker. För ett stort företag är frågan portföljstrategi, och för en myndighet kolliderar den med "offentliga pengar, offentlig kod", principen att skattefinansierad programvara bör vara offentlig som standard, så avgör i förväg vilka undantag (nationell säkerhet, bedrägeriupptäckt, personuppgifter) som motiverar att hålla kod sluten.

5. **Fångar våra bygga-eller-köpa-jämförelser den fulla totala ägandekostnaden, eller behandlar vi fortfarande en nollkronors licensavgift som nollkostnad?** Det vanligaste ekonomiska misstaget med öppen källkod är att läsa "gratis att skaffa" som "gratis att driva", för att sedan upptäcka att integration, drift, säkerhetssvar och betald support överskuggar varje licens ni undvikit. Spänningen är att en proprietär prenumeration ser dyr ut på fakturan medan den döljer en inlåsningspremie, och en öppen komponent ser gratis ut på fakturan medan den skiftar kostnad till er egen personal. Ta med en jämförbar TCO-modell för två eller tre verkliga beslut: anskaffning, integration, drift, support, utbildning, uppgraderingar, säkerhetssvar och eventuell ersättning, prissatta över hela livstiden snarare än första året. I en företags- eller myndighetsegendom, lägg till kostnaden för själva driftmodellen, eftersom självstödjande öppen källkod kräver intern kompetens ni måste rekrytera och behålla, och behandla en jämförelse som utelämnar de raderna som belägg, inte analys.

6. **Bedömer vi säkerheten hos en komponent efter dess praxis, eller lutar vi oss på öppenhetsetiketten, vare sig "många ögon" eller sluten kods hemlighetsfullhet?** Båda standardvalen är fällor: "många ögon" skyddar er bara när kvalificerade människor faktiskt granskar koden, och många vitt använda öppna projekt drivs av en enda utmattad underhållare, medan sluten källkod som förlitar sig på att angripare inte ser den är säkerhet genom obskuritet, inte en kontroll. Debatten spelar roll eftersom den ändrar var ni spenderar knapp säkerhetsinsats, och det ärliga svaret är att båda modellerna bär leveranskedjerisk, öppen källkod genom komprometterade eller övergivna beroenden och proprietär genom ogenomskinliga uppdateringskanaler ni inte kan inspektera. Ta med belägg för era mest kritiska komponenter: vem som faktiskt granskar dem, hur fort rådgivningar patchas, om versioner är fästa och ursprung verifierat och om ni genererar en SBOM. För en stor egendom eller en myndighet, knyt detta till upphandlings- och kontinuerliga skanningsskyldigheter, eftersom en tillsynsmyndighet kommer att fråga vad ni inspekterade, inte om källkoden var publik.

## Sektorsperspektiv

**Startup.** Med lite livslängd bygger du på grunder med öppen källkod eftersom du inte har råd med licensavgifter och du vill ha friheten att förgrena om ett projekt stannar av. Kör en kompositionsanalysskanning innan du levererar så att ett bibliotek med stark copyleft inte i tysthet förpliktar dig att publicera din egen källkod, och håll din enda verkliga särskiljare strikt sluten. Öppna ett litet, icke-kritiskt verktyg om det hjälper rekrytering, men bemanna inte en underhållsbörda du inte kan bära.

**Småföretag.** Utan intern jurist eller plattformsspecialist, behandla licensen som en risk du inte får missförstå snarare än ett ämne du kan bemästra. Föredra stödda proprietära verktyg eller kommersiella distributioner av öppen källkod där en leverantör äger lappar och ansvarsskyldighet, eftersom att självstödja en stack du inte kan driva är en falsk ekonomi. När du antar en gratis komponent, kontrollera att dess licens tillåter din användning och att projektet faktiskt underhålls, inte övergivet.

**Storföretag.** I skala är problemet konsekvens över många team: en skriven licenspolicy, automatisk programvarukompositionsanalys och SBOM-generering i varje pipeline och TCO-baserade bygga-eller-köpa-beslut snarare än teamvanor. Led öppen och proprietär programvara som en portfölj, standardisera utträdesskydd som öppna format och källkodsdeponering i upphandlingen och följ hälsan hos kritiska beroenden så att ett enda övergivet projekt inte blir en incident. Styr även producentsidan, med en tydlig regel för vad organisationen öppnar mot håller stängt.

**Offentlig sektor.** Upphandlingsregler, transparensplikter och offentlig ansvarsskyldighet formar varje val. Väg "offentliga pengar, offentlig kod", principen att skattefinansierad programvara bör vara offentlig som standard, för att främja återanvändning över myndigheter och digital suveränitet, samtidigt som du snävt undantar säkerhetskänslig kod eller kod med personuppgifter. Kräv av varje proprietär leverantör dataexport i öppna format och källkodsdeponering så att ett leverantörsfel inte kan strandsätta en offentlig tjänst och publicera den icke-känsliga källkoden så att medborgare kan granska de regler som styr dem.

## Exempel

**Startup.** Ett startup med tre grundare bygger hela sin produkt på grunder med öppen källkod (Linux, en databas med öppen källkod, ett webbramverk) eftersom det inte har råd med licensavgifter och vill ha friheten att förgrena om ett projekt stannar av. Före leverans kör en grundare en kompositionsanalysskanning och fångar ett bibliotek med stark copyleft som skulle ha tvingat dem att publicera sin proprietära matchningsalgoritm, så de byter ut det mot ett permissivt licensierat motsvarande. De håller den algoritmen, sin enda särskiljare, strikt sluten och öppnar bara ett litet internt loggningsverktyg för att bygga välvilja och attrahera ingenjörer.

**Storföretag.** Ett stort försäkringsbolag driver sin kärnplattform på grunder med öppen källkod: Linux, en vitt använd databas med öppen källkod och en containerorkestrerare. Men det köper en proprietär aktuariemodelleringssvit, eftersom leverantörens domänexpertis, regulatoriska certifieringar och supportavtal är värda avgiften och det inte finns något jämförbart öppet alternativ. Det betalar en prenumeration för **kommersiell öppen källkod** (leverantörsstödda distributioner av de öppna komponenterna) för att få ansvarsskyldighet och lappar på rörmokeriet, medan det håller prissättningsalgoritmen som särskiljer det strikt proprietär och internt. TCO-analys (kapitel 10.10) driver varje val snarare än ideologi.

**Offentlig sektor.** En nationell skattemyndighet, under en policy om "offentliga pengar, offentlig kod", bygger en ny tjänst för bidragsberättigande på komponenter med öppen källkod och öppna standarder (kapitel 3.8), så att andra myndigheter kan återanvända den och medborgare kan granska reglerna. Den publicerar den icke-känsliga koden i ett publikt repositorium och behåller bara bedrägeriupptäcktsheuristik som sluten av säkerhetsskäl. Det minskar leverantörsinlåsning och främjar digital suveränitet (kapitel 10.11). Upphandlingsregler (kapitel 10.3) kräver att varje proprietär komponent tillhandahåller dataexport i öppna format och källkodsdeponering, för att garantera kontinuitet om leverantören fallerar.

## Affärsnytta: motiv, ROI och TCO

Den ekonomiska lockelsen hos öppen källkod, avsaknaden av licensavgift, är den minst pålitliga delen av ärendet, eftersom anskaffning är en liten bråkdel av TCO. De varaktiga avkastningarna är strategiska: frihet från inlåsning (förmågan att byta eller släppa en leverantör utan att omarkitektera), granskningsbarhet för säkerhet och regelefterlevnad, snabbare adoption eftersom ingenjörer kan prova innan de binder sig och delat underhåll av standardkod över en hel bransch. De motverkande kostnaderna är verkliga. Ni måste tillhandahålla integration, drift, säkerhetssvar och ofta betald support, och ett dåligt valt ounderhållet projekt kan kosta mer i incidenter än någon licens hade gjort.

Proprietär programvaras affärsärende är ansvarsskyldighet och bekvämlighet: en enda leverantör ansvarig för produkten, ett supportavtal ni kan upprätthålla, integrerade funktioner och förutsägbar budgetering. Dess dolda kostnad är inlåsning, de byteskostnader som låter en leverantör höja priser eller försämra tjänsten med liten möjlighet till prövning, plus beroende av leverantörens solvens och färdplan. Vanliga **affärsmodeller** suddar ut gränsen: **[open core](https://en.wikipedia.org/wiki/Open-core_model)** (en öppen bas med proprietära betalda tillägg), **dubbel licensiering** (samma kod erbjuden under både en copyleft-licens och en betald kommersiell licens), **[programvara som en tjänst](https://en.wikipedia.org/wiki/Software_as_a_service) (SaaS)** (programvaran körs som en hostad tjänst ni hyr, där källkoden kan vara irrelevant eftersom ni aldrig besitter binären) och **support-/prenumerationsmodeller** som säljer service kring annars fri kod.

För en producent kan ROI på att **öppna er egen icke-särskiljande programvara** vara betydande. Externa bidragsgivare minskar er underhållsbörda. Projektet blir en rekryterings- och ryktestillgång. Extern adoption gör er standard till den de facto. För myndigheter levererar det transparens och återanvändning över den offentliga sektorn. Den strategiska regeln är enkel: öppna standardvaran för att dela dess kostnad och odla ett ekosystem och håll det särskiljande stängt för att skydda den fördel som finansierar allt annat.

## Antimönster och fallgropar

- **"Gratis betyder gratis":** att behandla noll anskaffningskostnad som noll TCO och sedan underfinansiera drift och support.
- **Licensblindhet:** att bädda in kod med stark copyleft i en distribuerad proprietär produkt och utlösa skyldigheter ni aldrig planerat för.
- **Tro på "många ögon":** att anta att ett öppet projekt är granskat när det har en överarbetad underhållare och ingen säkerhetsgranskning.
- **Säkerhet genom obskuritet:** att tro att sluten källkod är säker bara för att angripare inte kan läsa den.
- **Ideologisk absolutism:** att föreskriva "allt öppet" eller "allt proprietärt" i stället för att välja per komponent utifrån meriter och TCO.
- **Att ignorera ursprung:** att dra in beroenden utan SBOM, versionsfästning eller verifiering av leveranskedjan (kapitel 4.2).
- **Att öppna kronjuvelerna:** att släppa just den kod som särskiljer er och ge bort er fördel.
- **Förgrena-och-glöm:** att förgrena ett övergivet projekt utan kapacitet att faktiskt underhålla förgreningen.

## Mognadsmodell

**Nivå 1 (Initiera).** Komponenter med öppen källkod och proprietära kommer in i egendomen ad hoc. Licenser är olästa, det finns ingen inventering eller SBOM och valet mellan modeller görs av vana eller enbart pris. Övergivande och licensrisk dyker upp först när något går sönder, och varje team reagerar på egen hand.

**Nivå 2 (Utveckla).** Vissa team börjar med grundläggande praxis: en komponent- och licensinventering, en grov bild av acceptabla licenser och enstaka programvarukompositionsanalys. Beslut om bygga-eller-köpa och öppet-eller-slutet skrivs ned, men disciplinen är fläckvis och inkonsekvent från ett team till nästa, så en copyleft- eller bussfaktorsöverraskning kan ändå slinka igenom där vanan inte fastnat.

**Nivå 3 (Standardisera).** Ett dokumenterat ramverk styr både konsumtion och produktion i hela organisationen. Komponenter väljs på TCO och projekthälsa, licenser upprätthålls automatiskt i pipelinen så att överträdelser blockerar ett bygge, SBOM:er genereras som en självklarhet och en uttrycklig policy anger vad organisationen öppnar mot håller stängt. Utträdesskydd som öppna format och källkodsdeponering är standard i upphandlingen, och varje team följer samma regler snarare än sina egna.

**Nivå 4 (Hantera).** Programmet mäts och styrs mot utgångslägen. Organisationen följer mått som SBOM-täckning över produkter, andelen beroenden som bryter mot policy, genomsnittlig tid att patcha en offentliggjord beroendesårbarhet, bussfaktor- och hälsopoäng för kritiska projekt och realiserad TCO mot estimatet som motiverade varje val. Trösklar utlöser åtgärd: en komponent vars underhåll stannar av eller vars patchlatens driftar förbi målet flaggas för ersättning på belägg, och beslut om öppet-eller-slutet och bygga-eller-köpa granskas mot talen snarare än försvaras av vana.

**Nivå 5 (Orkestrera).** Strategin för öppen källkod är en medveten affärsförmåga, integrerad i hela organisationen och kontinuerligt förbättrad. Organisationen bidrar till och förvaltar ibland de projekt den beror på, öppnar sin icke-särskiljande programvara som en självklarhet och matar beroendehälsa och TCO-data tillbaka in i upphandling, säkerhet och produktplanering. Den balanserar rutinmässigt om sin portfölj av öppen och proprietär programvara och anpassar sig till skiften i kostnad, risk, suveränitet och strategisk fördel innan de tvingar fram en kris.

## Idéer för diskussion

- Var i er egendom skulle förlusten av en enda leverantör eller underhållare vara existentiell, och vad är er utträdesplan?
- Vilka av era egna system är standardvara ni kunde öppna, och vilka är verkliga särskiljare att skydda?
- Behandlar er organisation "många ögon" som en verklig säkerhetskontroll eller ett ogranskat antagande?
- För läsare i offentlig sektor: vad skulle en standard om "offentliga pengar, offentlig kod" ändra i er nästa upphandling?
- Hur väl fångar era TCO-jämförelser de drift- och supportkostnader öppen källkod skiftar över på er?

## Viktigaste punkter

- **Öppen mot sluten definieras av licensen**, inte av priset. Känn skillnaden mellan fri-som-i-frihet och fri-som-i-pris och mellan permissiv och copyleft.
- **Ingendera modellen är i sig säkrare eller billigare.** Bedöm projektets praxis och dess fulla TCO, inte öppenhetsetiketten.
- **Öppenhet är det starkaste motgiftet mot inlåsning** och ger granskningsbarhet, portabilitet och förmågan att förgrena. Proprietär programvara erbjuder ansvarsskyldighet och bekvämlighet i utbyte mot kontroll.
- **Avgör per komponent utifrån meriter** och blanda modeller medvetet snarare än av ideologi.
- **Som producent, öppna standardvaran och håll det särskiljande stängt**, och i myndigheter, väg "offentliga pengar, offentlig kod" för transparens, återanvändning och suveränitet.

## Referenser och vidare läsning

- Eric S. Raymond, *The Cathedral and the Bazaar*
- Nadia Eghbal, *Working in Public: The Making and Maintenance of Open Source Software*
- Karl Fogel, *Producing Open Source Software: How to Run a Successful Free Software Project*
- Adrian Cockcroft and others, various O'Reilly titles on open-source strategy and operations
- Free Software Foundation, *The Free Software Definition* (and the GNU General Public Licence texts)
- Open Source Initiative, *The Open Source Definition* and approved-licence list
- Free Software Foundation Europe, *Public Money, Public Code* campaign materials
- Yochai Benkler, *The Wealth of Networks*
