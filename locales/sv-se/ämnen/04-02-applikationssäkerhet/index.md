# 4.2 Applikationssäkerhet

## Översikt och motivation

Applikationssäkerhet är där abstrakta hot möter konkret kod. De flesta intrång som når rubrikerna går att spåra till en brist i applikationslagret: en injektion, ett trasigt autentiseringsflöde, en exponerad hemlighet eller ett komprometterat beroende. För stora team som levererar många tjänster är det svåra inte att veta att dessa brister finns. Det är att förhindra dem konsekvent över en vidsträckt kodbas skriven av tusentals händer under många år.

För företag är applikationssäkerhet en fråga om kundförtroende och regulatorisk skyldighet. En brist i ett inloggningsflöde eller en betalningsväg kan utlösa bedrägeri, viten och obligatorisk anmälan av intrång. Myndighetssystem möter samma tekniska risker med data av högre insats: bidragsberättigande, skatteregister, rättsväsendets data och nationell infrastruktur. I båda sammanhangen är applikationen ytterdörren, och angripare sonderar den ständigt och automatiskt.

Det här kapitlet behandlar de praxis som håller applikationer motståndskraftiga: att känna till och försvara sig mot de vanliga sårbarhetsklasserna, validera indata och koda utdata, få autentisering och auktorisering rätt, hantera hemligheter och säkra den leveranskedja för programvara som alltmer avgör din verkliga angreppsyta.

*Se även:* kapitel 4.1 (säkerhetens grunder, hotmodellering och livscykeln för säker utveckling), kapitel 10.3 (leveranskedja för öppen källkod och licensiering) och kapitel 10.2 (SBOM, risk och säkring).

## Nyckelprinciper

- **Lita aldrig på indata.** Behandla all data som korsar en förtroendegräns som fientlig tills den är validerad.
- **Säkra standardvärden.** Den säkra vägen bör vara den lätta vägen. Osäkert beteende bör kräva medveten, synlig ansträngning.
- **Fallera stängt.** När en säkerhetskontroll inte kan slutföras, neka åtkomst snarare än att tillåta den.
- **Försvar på djupet i applikationslagret.** Kombinera validering, kodning, parametrisering och ramverksskydd. Förlita dig inte på ett.
- **Minsta behörighet för identiteter och tokens.** Avgränsa uppgifter snävt och låt dem löpa ut snabbt.
- **Dina beroenden är din kod.** Du ansvarar för säkerheten i allt du levererar, inklusive tredjeparts- och öppen källkodskomponenter.
- **Standarder framför improvisation.** Använd beprövade ramverk som [OWASP](https://en.wikipedia.org/wiki/OWASP):s (Open Worldwide Application Security Project) ASVS i stället för att uppfinna egna säkerhetskontroller.

## Rekommendationer

### Känn till och försvara OWASP Top 10, verifiera med ASVS

OWASP Top 10 är branschens basta lista över de mest kritiska riskerna för webbapplikationer: trasig åtkomstkontroll, kryptografiska fel, injektion, osäker design, säkerhetsfelkonfiguration, sårbara komponenter, autentiseringsfel, dataintegritetsfel, loggningsfel och serversidig förfalskning av begäran (SSRF). Behandla den som obligatorisk kunskap för varje ingenjör, inte bara en regelefterlevnadsreferens att arkivera.

För en rigorös, testbar standard, anta **OWASP Application Security Verification Standard (ASVS)**. ASVS definierar säkerhetskrav på tre säkringsnivåer och ger dig konkreta, granskningsbara kontroller att designa och testa mot. Välj den nivå som passar varje applikations risk och verifiera mot den.

### Validera indata och koda utdata

Injektionsbrister förblir bland de mest skadliga just för att de är så lätta att introducera. Försvara dig med lagerindelade kontroller:

- **Validera indata** mot strikta tillåtlistor (förväntad typ, längd, format, intervall). Avvisa snarare än sanera där du kan.
- **Använd parametriserade frågor** och [förberedda satser](https://en.wikipedia.org/wiki/Prepared_statement) för all databasåtkomst. Bygg aldrig SQL genom strängsammanfogning. Använd säkra frågebyggare och ORM (objekt-relationsmappare) korrekt.
- **Koda utdata** kontextuellt. HTML, HTML-attribut, JavaScript, URL:er och CSS kräver var och en olika kodning. Lita på ramverkets automatiska undantagshantering och förstå dess gränser.
- **Förhindra [skriptinjektion mellan webbplatser](https://en.wikipedia.org/wiki/Cross-site_scripting) (XSS)** med utdatakodning plus en stark Content Security Policy som andra lager.
- **Förhindra kommando- och mallinjektion** genom att undvika att anropa skalet med opålitlig data och genom att använda logiklösa eller isolerade mallar.

### Få autentisering och auktorisering rätt

Autentisering bevisar vem en användare är. Auktorisering avgör vad de får göra. Båda fallerar ofta, så få dem rätt.

- Föredra etablerade protokoll: **[OAuth 2.0](https://en.wikipedia.org/wiki/OAuth)** för delegerad auktorisering och **[OpenID Connect](https://en.wikipedia.org/wiki/OpenID_Connect) (OIDC)** för autentisering. Bygg inte dessa från grunden.
- Upprätthåll **[flerfaktorsautentisering](https://en.wikipedia.org/wiki/Multi-factor_authentication) (MFA)**, särskilt för privilegierad och administrativ åtkomst.
- Lagra lösenord bara som saltade hashar med en modern, långsam, minneskrävande algoritm (som [Argon2](https://en.wikipedia.org/wiki/Argon2) eller [bcrypt](https://en.wikipedia.org/wiki/Bcrypt)). Lagra eller logga aldrig uppgifter i klartext.
- Hantera **sessioner** noggrant: generera kryptografiskt starka tokens, sätt flaggorna secure och HttpOnly på cookies, rotera vid behörighetsändring och låt overksamma sessioner löpa ut.
- Upprätthåll **auktorisering på servern för varje begäran** och kontrollera att den autentiserade huvudmannen äger eller får komma åt den specifika resursen. Trasig auktorisering på objektnivå (att komma åt en annan användares post genom att ändra ett ID) är ett av de vanligaste och allvarligaste API-felen.
- Centralisera auktoriseringslogik där det är praktiskt så att policy är konsekvent och granskningsbar.

### Hantera hemligheter och rotera nycklar

Hårdkodade hemligheter i källkod är en ständig orsak till intrång. Bygg en disciplinerad vana kring hemlighetshantering:

- Lagra hemligheter i en dedikerad hemlighetshanterare eller ett valv, aldrig i källkod, konfigurationsfiler eller miljövariabler som checkats in i versionshantering.
- Skanna incheckningar och repositorier efter läckta hemligheter automatiskt och blockera sammanslagningar som introducerar dem.
- Rotera nycklar och uppgifter regelbundet och omedelbart vid varje misstänkt exponering. Föredra kortlivade, automatiskt utfärdade uppgifter framför långlivade statiska.
- Tillämpa minsta behörighet på varje hemlighet: avgränsa den till exakt det den behöver.
- Kryptera hemligheter i vila och under överföring och granska åtkomst till dem.

### Säkra leveranskedjan för programvara

Moderna applikationer sätts mestadels ihop av tredjepartskomponenter, vilket gör leveranskedjan till en primär angreppsyta.

- Underhåll en **[programvarumaterialförteckning](https://en.wikipedia.org/wiki/Software_bill_of_materials) (SBOM)** för varje applikation så att du vet exakt vad du levererar och kan svara snabbt när en ny sårbarhet landar.
- Skanna beroenden kontinuerligt (Software Composition Analysis, eller SCA) och åtgärda kända sårbara komponenter omgående.
- Fäst och verifiera beroendeversioner. Använd låsfiler och betrodda register.
- Anta **SLSA** (Supply-chain Levels for Software Artifacts) för att höja byggintegriteten och generera **proveniens**-attesteringar som beskriver hur artefakter byggdes.
- **Signera artefakter** och verifiera signaturer före driftsättning så att du kan lita på att det som körs är det du byggde.
- Säkra själva byggsystemet. En komprometterad CI-pipeline kan injicera skadlig kod i varje konsument nedströms.

## Avvägningar: för- och nackdelar

| Beslut | Fördelar | Nackdelar |
|---|---|---|
| Köp/anta identitetsleverantör (OIDC) | Beprövad, MFA inbyggt, mindre kod att säkra | Leverantörsberoende, integrationsinsats, kostnad |
| Bygg egen autentisering | Full kontroll, inget externt beroende | Extremt lätt att göra fel, högt underhåll |
| Strikt validering med tillåtlista | Blockerar hela sårbarhetsklasser | Kan bryta legitima gränsfall, mer arbete i förväg |
| Kortlivade uppgifter | Litet intrångsfönster, automatisk återkallelse | Kräver robust utfärdandeinfrastruktur |
| Aggressiva beroendeuppdateringar | Färre kända sårbarheter | Omsättning, potentiella brytande ändringar, testbörda |
| SBOM + signering + proveniens | Snabb incidenthantering, verifierbart förtroende | Verktygs- och processinvestering, kulturförändring |

Den återkommande avvägningen är rigor i förväg mot löpande exponering. Att bygga egen autentisering eller hoppa över beroendehygien känns snabbare i dag och kostar enormt senare. Att anta beprövade standarder och automatiserade leveranskedjekontroller kostar insats nu, men förvandlar en obegränsad, oförutsägbar risk till en hanterad, begränsad. För stora team spelar automationsmultiplikatorn störst roll: en kontroll tillämpad en gång i en mall på upptrampad stig skyddar varje tjänst som använder den.

## Frågor att diskutera med ditt team

1. **Vilka ASVS-kontroller ska ni baka in i ert ramverk på upptrampad stig så att ingenjörer får dem gratis?** Den mest hävstångsstarka åtgärden för ett stort team är att göra den säkra vägen till standard, så att en kontroll skriven en gång i ett gemensamt ramverk skyddar varje tjänst som antar det. Besluta vilka ASVS-krav (parametriserade frågor, utdatakodning, säkra sessionsflaggor, auktoriseringskontroller på serversidan) som hör hemma i mallen snarare än i varje ingenjörs minne. För företags- och myndighetsportföljer, besluta också vilka applikationer som behöver ASVS nivå 2 mot nivå 3 och knyt det till känsligheten i den data var och en rör. Ta med en lista över era tjänster och markera vilka som redan ärver dessa standardvärden och vilka som implementerar säkerhet för hand, eftersom de handrullade är där injektion och trasig åtkomstkontroll gömmer sig. Om säkra standardvärden bor enbart på en wikisida kommer de att hoppas över under leveranstryck, så lägg dem i kod.

2. **Hur ska ni hitta och rätta trasig auktorisering på objektnivå över varje API, inte bara de nya?** Att komma åt en annan användares post genom att ändra ett ID är ett av de vanligaste och allvarligaste API-felen, och det gömmer sig i äldre ändpunkter som föregår era nuvarande standarder. Auktorisering på serversidan för varje begäran och varje objekt är regeln, men det svåra är att verifiera att den håller över en vidsträckt, flera år gammal kodbas skriven av många händer. Besluta om ni ska centralisera auktoriseringslogik, lägga till automatiska tester som försöker åtkomst över tenants eller köra riktad testning mot era mest riskfyllda API:er först. Ta med er inventering av ändpunkter som exponerar objektidentifierare och rangordna dem efter känsligheten i det de returnerar. Utan en medveten genomgång fortsätter ni leverera denna brist och upptäcker den först när en forskare eller en angripare gör det.

3. **Vilken är er plan för nästa utbredda beroendesårbarhet: hur snabbt kan ni hitta och patcha varje berörd tjänst?** När en kritisk brist landar i ett populärt bibliotek identifierar företag med en korrekt SBOM berörda tjänster på timmar medan andra tillbringar veckor med att leta, och den hastighetsklyftan avgör hur mycket skada ni tar. Besluta nu om ni producerar en programvarumaterialförteckning för varje artefakt, om beroendeskanning körs i varje pipeline och vem som äger beslutet om akut patch. För reglerade köpare och myndighetsköpare är SBOM och signerad proveniens alltmer ett villkor för att göra affärer, så den här beredskapen skyddar också intäkter. Ta med det ärliga svaret från en övning: välj ett bibliotek ni använder brett och ta tid på hur lång tid det tar att lista varje tjänst som levererar det. Om svaret mäts i dagar, investera i inventering och signering innan nästa incident tvingar er.

4. **Hur ska ni gå från långlivade statiska hemligheter till kortlivade, automatiskt utfärdade uppgifter, och vilka system blockerar det i dag?** Hårdkodade och långlivade hemligheter är en ständig orsak till intrång, och åtgärden, kortlivade uppgifter utfärdade på begäran, beror på en utfärdandeinfrastruktur som äldre system ofta inte kan använda. För ett stort team är faran ojämn användning: en modern plattform roterar nycklar varje timme medan en äldre tjänst fortfarande levererar ett statiskt databaslösenord i en konfigurationsfil. Besluta vilka arbetslaster som kan konsumera en hemlighetshanterare eller ett system för arbetslastidentitet nu, vilka som behöver investering först och vem som äger rotationskörboken i samma stund en nyckel misstänks ha läckt. Ta med en inventering av varje uppgift i bruk, dess livslängd, dess sprängradie om den exponeras och om incheckningsskanning skulle fånga den före sammanslagning. I företags- och myndighetssammanhang, knyt detta till revision: granskare förväntar sig alltmer belägg för rotation, avgränsad åtkomst och åtkomstloggning för varje hemlighet, och en statisk uppgift ni inte kan rotera utan driftstopp är ett fynd som väntar på att skrivas ned.

5. **Var kör ni fortfarande hemmabyggd eller inkonsekvent autentisering, och vad är planen för att konsolidera på beprövade protokoll?** Att bygga autentisering är ett av de lättaste sätten att introducera subtila, utnyttjningsbara brister, men de flesta stora egendomar bär åtminstone ett äldre inloggningsflöde som föregår beslutet att standardisera på OAuth 2.0 och OIDC. De konkurrerande trycken är verkliga: att migrera ett gammalt flöde riskerar att bryta befintliga användare och integrationer, medan att lämna det kvar håller ett högvärdigt mål underförsvarat. Besluta om ni konsoliderar på en enda identitetsleverantör, upprätthåller MFA enhetligt och sätter en deadline för att avveckla varje skräddarsytt flöde, eller accepterar dokumenterade undantag med kompenserande kontroller. Ta med en karta över varje autentiseringsväg i flottan, vilka som upprätthåller MFA, vilka som lagrar lösenord med en modern minneskrävande hash och vilka som är skräddarsydda. För företags- och myndighetsportföljer, lägg till regelefterlevnadsvinkeln: standarder som NIST SP 800-63 sätter konkreta förväntningar på identitetssäkring, och ett hemmabyggt flöde som inte kan visa dem kommer inte att överleva en revision eller en granskning av tillstånd att driva.

6. **Hur verifierar ni att dessa kontroller faktiskt håller i produktion, och kan ni bevisa det med belägg snarare än påstående?** Att skriva ett säkert standardvärde är inte detsamma som att veta att varje tjänst fortfarande respekterar det, och kontroller ruttnar i tysthet när kod ändras, undantag hopar sig och nya ändpunkter levereras. För ett stort team handlar frågan om täckning: vilka tjänster kör statisk analys, beroendeskanning och dynamisk testning eller penetrationstestning, och hur vet ni att de som hoppar över dem inte är era mest riskfyllda applikationer? Besluta vilken verifiering som är obligatorisk i pipelinen mot periodisk, vem som triagerar fynden och vilka belägg ni behåller för att visa att en kontroll testades och klarades ett givet datum. Ta med er nuvarande täckningskarta, er mediantid att åtgärda per allvarlighetsgrad och listan över applikationer utan nyligt test. I reglerade och offentliga sammanhang är dessa belägg inte valfria: revisorer, godkännande tjänstemän och intrångsutredare frågar alla efter bevis för att kontroller verifierades, och en policy utan testregister tillfredsställer dem sällan.

## Sektorsperspektiv

**Startup.** Med två eller tre ingenjörer och ingen säkerhetsspecialist är din hävstång att ärva säkerhet snarare än bygga den: anta en hanterad OIDC-identitetsleverantör, lita på ett ramverk vars ORM parametriserar frågor som standard och håll hemligheter i din plattforms hemlighetshanterare snarare än `.env`-filer en kollega av misstag kan checka in. Slå på automatisk beroendeskanning som öppnar patch-pull requests och behandla det som tillräckligt för tillfället. Bygg inte egen autentisering eller kryptografi, eftersom en enda injicerad fråga eller en läckt nyckel kan göra slut på företaget innan det har kunder.

**Småföretag.** Du har sannolikt ingen applikationssäkerhetsspecialist och en snäv budget, så köp kontroller inbäddade i de verktyg och plattformar du redan betalar för i stället för att bemanna en dedikerad funktion. Välj en hostad identitetsleverantör med MFA inkluderat, en hanterad databas som styr dig mot parametriserad åtkomst och en repositoriumvärd som skannar incheckningar efter läckta hemligheter direkt. Koncentrera din knappa uppmärksamhet på grunderna i OWASP Top 10 som orsakar de flesta verkliga intrång, och föredra leverantörer som levererar säkra standardvärden du inte kan stänga av tillfälligt.

**Storföretag.** Över många team är utmaningen konsekvens: baka in ASVS-kontroller i ramverk på upptrampad stig så att varje ny tjänst ärver parametriserade frågor, utdatakodning, säkra sessioner och auktorisering på serversidan gratis. Kör korrekta SBOM och beroendeskanning över hela flottan så att nästa utbredda biblioteksbrist blir en fråga om timmar, inte veckor, och centralisera auktoriseringspolicy så att åtkomst över tenants blir testbar. Standardisera på en identitetsleverantör med upprätthållen MFA och hantera applikationssäkerhet som en styrd portfölj med risknivåindelade ASVS-nivåer och granskade belägg.

**Offentlig sektor.** Upphandlingsregler, transparens och offentlig ansvarsskyldighet formar de kontroller du måste visa, inte bara implementera. Verifiera medborgarvända tjänster mot OWASP ASVS på en nivå som matchar datans känslighet, signera varje driftsatt artefakt och attestera dess proveniens enligt SLSA för att uppfylla krav på leveranskedjan och utfärda kortlivade uppgifter från ett centralt valv med full åtkomstloggning. Förvänta dig att visa revisorer och godkännande tjänstemän en dokumenterad förvaringskedja från källkod till produktion, och justera identitetssäkringen efter publicerade standarder som NIST SP 800-63.

## Exempel

**Startup.** Ett SaaS-team på tre ingenjörer hoppar över att bygga egen inloggning och antar en hanterad OIDC-leverantör från dag ett, vilket ger MFA och säkra lösenordsåterställningar utan att skriva säkerhetskritisk kod de inte har råd att göra fel. Det litar på ramverkets ORM så att frågor är parametriserade som standard, håller hemligheter i plattformens hemlighetshanterare snarare än i `.env`-filer en kollega av misstag kan checka in och slår på automatisk beroendeskanning som öppnar en pull request när ett bibliotek behöver patchas. Inget av detta bromsar teamet, och det betyder att en läckt nyckel eller en injicerad fråga inte gör slut på företaget innan det har kunder.

**Storföretag.** En detaljhandelsplattform som betjänar tiotals miljoner kunder standardiserar autentisering på OIDC genom en enda identitetsleverantör och upprätthåller MFA för personal och stegvis autentisering för kontoändringar av högt värde. All databasåtkomst går genom ett ORM konfigurerat att parametrisera frågor, och en Content Security Policy backar upp utdatakodningen. Efter en vitt uppmärksammad sårbarhet i ett populärt loggningsbibliotek låter företagets SBOM det identifiera varje berörd tjänst inom timmar och patcha dem på två dagar, medan konkurrenter utan inventeringar tillbringade veckor med att leta.

**Offentlig sektor.** En federal bidragsmyndighet bygger medborgarvända tjänster verifierade mot OWASP ASVS nivå 2, med nivå 3 för komponenterna som hanterar de känsligaste registren. Hemligheter bor i ett centralt valv som utfärdar kortlivade uppgifter, och incheckningsskanning blockerar varje läckt nyckel. Varje driftsatt artefakt signeras och dess proveniens attesteras enligt SLSA, vilket uppfyller ett federalt krav på verifierbara leveranskedjor för programvara och ger revisorer en tydlig förvaringskedja från källkod till produktion.

## Affärsnytta: motiv, ROI och TCO

Utgifter för applikationssäkerhet köper ned den mest sannolika och dyraste kategorin av intrång. Den totala ägandekostnaden inkluderar verktyg (skannrar, hemlighetshanterare, identitetsleverantörer), ingenjörstid för att åtgärda fynd och den milda friktionen av säkra standardvärden. Mot det, väg kostnaden för att hoppa över det: injektions- och trasig-åtkomstkontroll-intrång exponerar rutinmässigt miljontals poster och utlöser regulatoriska viten, obligatorisk underrättelse, bedrägeriförluster, åtgärdssprintar och anseendeskada som trycker ned intäkterna i åratal.

Avkastningen är starkast när kontroller är automatiserade och återanvända. En välkonfigurerad identitetsintegration, ett härdat frågelager i ett gemensamt ramverk och en pipeline som blockerar sårbara beroenden skyddar hela flottan till marginalkostnad per tjänst. Kontroller i leveranskedjan i synnerhet har gått från valfria till nödvändiga: ett komprometterat beroende kan göra var och en av dina kunder till offer, och tillsynsmyndigheter och företagsköpare kräver alltmer SBOM och signerad proveniens som villkor för att göra affärer. När du driver ärendet inför ledningen, knyt investeringen till specifika, namngivna risker och till upphandlings- och regelefterlevnadskrav som blockerar intäkter om du inte uppfyller dem.

## Antimönster och fallgropar

- **Att rulla egen kryptografi eller autentisering.** Ger nästan alltid subtila, utnyttjningsbara brister.
- **Enbart validering på klientsidan.** Trivialt kringgådd. Servern måste validera om allt.
- **Sanering med svartlista.** Att försöka rensa bort "dåliga" tecken i stället för att tillåtlista goda. Angripare hittar luckorna.
- **Hemligheter i källkod eller miljöfiler.** Den enskilt vanligaste orsaken till uppgiftsläckor.
- **Att ignorera auktorisering vid objektåtkomst.** Att anta att en autentiserad användare får komma åt vilket objekt som helst vars ID de kan gissa.
- **Beroenden som sätts och glöms.** Att aldrig uppdatera tredjepartskomponenter tills ett intrång tvingar fram det.
- **Att behandla Top 10 som mållinjen.** Den är ett golv, inte en heltäckande standard. Använd ASVS för djup.
- **Att logga känslig data.** Lösenord, tokens och PII (personuppgifter) i loggar är ett intrång som väntar på att hända.

## Mognadsmodell

**Nivå 1: Initiera.** Applikationssäkerhet beror på enskilda utvecklares kunskap och reagerar först efter incidenter. Inga standardkontroller. Hemligheter ligger i källkod. Beroenden uppdateras sällan. Autentisering är skräddarsydd och ad hoc, och injektions- eller trasig-åtkomstkontroll-brister hittas av en slump snarare än genom process.

**Nivå 2: Utveckla.** Grundläggande praxis dyker upp men varierar team för team. Kännedom om OWASP Top 10 sprids, vissa skydd på ramverksnivå finns på plats och en hemlighetshanterare finns men används ojämnt. Beroendeskanning körs ibland. Nya system antar en standardidentitetsleverantör, medan äldre tjänster behåller sina hemmabyggda inloggningsflöden orörda.

**Nivå 3: Standardisera.** Kontroller är dokumenterade och upprätthållna i hela organisationen. ASVS-baserade krav sätts per risknivå, parametriserade frågor och utdatakodning är normen och en central identitetsleverantör med MFA krävs. Hemligheter hanteras och skannas automatiskt, SBOM produceras och beroendeskanning körs i varje pipeline.

**Nivå 4: Hantera.** Praktiken mäts och styrs mot utgångslägen. Skanning och testtäckning, mediantid att åtgärda per allvarlighetsgrad, andelen tjänster som ärver standardvärden på upptrampad stig, ålder på uppgifts- och hemlighetsrotation och ASVS-efterlevnad följs alla på paneler. Undantag loggas med utgångsdatum, avvikelse från utgångsläget utlöser åtgärd och releaser grindas på definierade säkerhetströsklar snarare än omdömesbeslut.

**Nivå 5: Orkestrera.** Säkerhet förbättras kontinuerligt och är integrerad i hela organisationen. Säkra standardvärden är inbyggda i ramverk på upptrampad stig så att den säkra vägen är automatisk, kortlivade uppgifter används överallt och full säkring av leveranskedjan med signering och proveniens (SLSA) är standard. Verifiering är kontinuerlig, svar på nya sårbarheter är snabbt och mätt och varje incident matas tillbaka in i de gemensamma mallarna så att en enda rättelse härdar hela flottan.

## Idéer för diskussion

1. Var bör auktoriseringslogik bo för att vara både konsekvent och underhållbar över många tjänster?
2. Hur aggressivt bör ni uppdatera beroenden med tanke på avvägningen mellan exponering och omsättning?
3. Vilken ASVS-nivå är lämplig för varje klass av applikation i er portfölj?
4. Hur eliminerar ni långlivade hemligheter utan att skapa skör utfärdandeinfrastruktur?
5. Vad skulle det krävas för att er organisation ska producera och konsumera SBOM och proveniens för varje artefakt?
6. Hur hindrar ni säkra standardvärden från att stängas av under leveranstryck?

## Viktigaste punkter

- OWASP Top 10 är nödvändig kunskap. ASVS ger den testbara standarden.
- Lagra indatavalidering, parametrisering och utdatakodning för att besegra injektion och XSS.
- Använd beprövade protokoll (OAuth 2.0, OIDC) och upprätthåll MFA. Bygg aldrig autentisering från grunden.
- Upprätthåll auktorisering på serversidan för varje begäran och varje objekt.
- Håll hemligheter utanför källkod, hantera dem centralt och rotera mot kortlivade uppgifter.
- Leveranskedjan är en primär angreppsyta. Använd SBOM, SCA, signering och proveniens (SLSA).
- Automatiserade, återanvändbara kontroller skyddar hela flottan till marginalkostnad per tjänst.

## Referenser och vidare läsning

- OWASP, *Top 10 Web Application Security Risks*
- OWASP, *Application Security Verification Standard (ASVS)*
- OWASP, *Cheat Sheet Series* (Input Validation, Authentication, Authorisation, Secrets Management)
- Dafydd Stuttard and Marcus Pinto, *The Web Application Hacker's Handbook*
- Aaron Parecki, *OAuth 2.0 Simplified*
- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines*
- Cloud Native Computing Foundation and OpenSSF, *SLSA framework* and *Supply-chain Security guidance*
