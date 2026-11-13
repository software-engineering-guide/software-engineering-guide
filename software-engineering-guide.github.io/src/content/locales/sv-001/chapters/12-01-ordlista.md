# 12.1 Ordlista

Den här ordlistan definierar termer och akronymer som används genom hela boken.
Posterna är grupperade alfabetiskt efter de engelska nyckelorden, som är de ni
möter i verktyg och dokumentation. Svenska motsvarigheter står inom parentes där
en etablerad sådan finns. Där en post har en vanlig akronym visas den inom
parentes. Definitionerna är medvetet kortfattade. Se det aktuella kapitlet för
en fylligare behandling.

## A

**[ABAC (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control)** (attributbaserad åtkomstkontroll): En auktoriseringsmodell som beviljar åtkomst utifrån utvärderade attribut hos användaren, resursen, åtgärden och miljön (till exempel avdelning, behörighetsnivå, tid på dygnet) snarare än fasta roller. Den ger finkornig, policydriven kontroll till priset av större komplexitet än RBAC.

**[Accessibility (a11y)](https://en.wikipedia.org/wiki/Computer_accessibility)** (tillgänglighet): Praxisen att utforma och bygga programvara så att personer med funktionsnedsättning kan uppfatta, förstå, navigera i och interagera med den. Numeronymen "a11y" förkortar de 11 bokstäverna mellan "a" och "y."

**ADR (Architecture Decision Record)** (arkitekturbeslutslogg): Ett kort, versionshanterat dokument som fångar ett enskilt betydande arkitektur- eller tekniskt beslut, dess sammanhang, de alternativ som övervägdes och dess konsekvenser. ADR skapar en varaktig, granskningsbar historik över varför ett system ser ut som det gör.

**Aggregate** (aggregat): Inom Domain-Driven Design ett kluster av domänobjekt som behandlas som en enhet för dataändringar, där en entitet fungerar som aggregatrot och upprätthåller invarianter. Aggregat definierar konsistens- och transaktionsgränser.

**[API (Application Programming Interface)](https://en.wikipedia.org/wiki/API)** (applikationsprogrammeringsgränssnitt): Ett definierat kontrakt genom vilket en programvara begär tjänster eller data från en annan. Väl utformade API:er döljer implementationsdetaljer och erbjuder stabila, versionshanterade gränssnitt.

**API-first**: Ett utvecklingssätt där API-kontraktet utformas och överenskoms före implementationen, så att konsumenter och leverantörer kan arbeta parallellt mot en gemensam specifikation.

**arc42**: En öppen, mallbaserad struktur för att dokumentera programvaruarkitektur, organiserad i tolv avsnitt som täcker sammanhang, begränsningar, byggblock, körtid, driftsättning och beslut.

**[ARIA (Accessible Rich Internet Applications)](https://en.wikipedia.org/wiki/WAI-ARIA)**: En W3C-specifikation som definierar roller, tillstånd och egenskaper som gör dynamiska och anpassade webbkomponenter begripliga för hjälpmedelsteknik som skärmläsare.

**ASR (Architecturally Significant Requirement)** (arkitekturellt signifikant krav): Ett krav som har en mätbar, vittgående effekt på arkitekturen, som en prestanda-, tillgänglighets-, säkerhets- eller regulatorisk begränsning. ASR driver de mest konsekvensfulla designbesluten.

**ASVS (Application Security Verification Standard)**: En OWASP-standard som ger en graderad checklista över säkerhetskrav och tester för att utforma, bygga och verifiera säkra applikationer.

**[Autoscaling](https://en.wikipedia.org/wiki/Autoscaling)** (automatisk skalning): Den automatiska justeringen av antalet körande beräkningsinstanser (eller deras storlek) som svar på last, så att kapaciteten följer efterfrågan utan manuellt ingripande. Den kompletterar, men ersätter inte, medveten kapacitetsplanering.

**[Availability](https://en.wikipedia.org/wiki/Availability)** (tillgänglighet): Den andel av tiden ett system är i drift och kan betjäna förfrågningar, ofta uttryckt i "nior" (till exempel 99,9 %). Det är ett centralt tillförlitlighetsmål som fastställs i SLO:er och SLA:er.

## B

**Backpressure** (mottryck): En flödeskontrollmekanism där en komponent under last signalerar uppströms producenter att sakta ned, vilket förhindrar obegränsade köer och kaskadfel. Den är central för tillförlitliga ström- och meddelandedrivna system.

**[BDD (Behaviour-Driven Development)](https://en.wikipedia.org/wiki/Behavior-driven_development)** (beteendedriven utveckling): En samarbetsbaserad praxis som uttrycker krav som konkreta, läsbara exempel på beteende (ofta i formen Given/When/Then) som dubblerar som automatiserade acceptanstester.

**BFF (Backend for Frontend)**: Ett arkitekturmönster där en dedikerad backend-tjänst byggs för en specifik frontend eller klienttyp och skräddarsyr dataformning och aggregering efter den klientens behov.

**[BI (Business Intelligence)](https://en.wikipedia.org/wiki/Business_intelligence)** (affärsanalys): Verktygen, processerna och praxisen för att samla in, integrera och analysera affärsdata för att stödja rapportering, paneler och beslutsfattande.

**Blameless postmortem** (skuldfri efterhandsgranskning): En incidentgranskning som fokuserar på systemiska orsaker och lärande snarare än individuell skuld, utifrån premissen att människor handlar rimligt givet den information och de incitament de hade.

**[Blue-green deployment](https://en.wikipedia.org/wiki/Blue-green_deployment)** (blågrön driftsättning): En releasestrategi som kör två identiska produktionsmiljöer ("blå" och "grön"), dirigerar trafik till den ena medan den andra uppdateras och möjliggör nästan omedelbar övergång och återställning.

**[BM25](https://en.wikipedia.org/wiki/Okapi_BM25)**: En vitt använd rankningsfunktion för fulltextsökning som poängsätter hur väl ett dokument matchar en fråga utifrån termfrekvens, inverterad dokumentfrekvens och dokumentlängd. Den är standardvalet för lexikal rankning i många sökmotorer.

**Bounded context** (avgränsad kontext): Inom Domain-Driven Design en uttrycklig gräns inom vilken en viss domänmodell och dess allmänt delade språk gäller konsekvent. Den hindrar begrepp från att blandas ihop i olika delar av ett stort system.

**Build cache** (byggcache): Ett lager av tidigare beräknade byggresultat, nycklade på de indata som producerade dem, så att oförändrat arbete återanvänds i stället för att byggas om. En delad fjärrbyggcache låter ett helt team och dess CI återanvända varandras resultat.

**[Bus factor](https://en.wikipedia.org/wiki/Bus_factor)** (bussfaktor): Antalet personer som skulle behöva försvinna (metaforiskt "bli påkörda av en buss") innan ett projekt stannar av för brist på nödvändig kunskap. En låg bussfaktor signalerar koncentrerad, odokumenterad expertis och organisatorisk risk.

## C

**[Cache eviction policy](https://en.wikipedia.org/wiki/Cache_replacement_policies)** (utkastningspolicy för cache): Regeln en cache använder för att avgöra vilken post som tas bort när den är full, som minst nyligen använd (LRU) eller minst frekvent använd (LFU). Policyn formar träffgraden och därmed cachens värde.

**[Cache invalidation](https://en.wikipedia.org/wiki/Cache_invalidation)** (cacheinvalidering): Problemet att ta bort eller uppdatera cachade data när den underliggande källan ändras, så att läsare inte ser föråldrade värden. Det är ökänt som ett av databehandlingens svåraste problem.

**[Cache stampede](https://en.wikipedia.org/wiki/Cache_stampede)**: Ett felläge där många klienter missar cachen för samma nyckel samtidigt och alla träffar ursprunget tillsammans och överväldigar det. Sammanslagning av förfrågningar och förskjuten utgång förhindrar det. Kallas också thundering herd.

**Canary release** (kanarierelease): En driftsättningsteknik som först exponerar en ny version för en liten delmängd användare eller trafik, bevakar problem och sedan gradvis breddar utrullningen om måtten förblir friska.

**[CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem)** (CAP-satsen): En princip som säger att ett distribuerat datalager högst kan garantera två av konsistens, tillgänglighet och partitionstolerans samtidigt. Eftersom partitioner är oundvikliga väger konstruktörer i praktiken konsistens mot tillgänglighet under dem.

**[C4 model](https://en.wikipedia.org/wiki/C4_model)** (C4-modellen): Ett lättviktigt sätt att visualisera programvaruarkitektur på fyra abstraktionsnivåer: systemkontext, containrar, komponenter och kod.

**[CD (Continuous Delivery / Continuous Deployment)](https://en.wikipedia.org/wiki/Continuous_delivery)** (kontinuerlig leverans / kontinuerlig driftsättning): Kontinuerlig leverans håller programvaran i releasebart skick så att den kan driftsättas när som helst med ett manuellt godkännande. Kontinuerlig driftsättning släpper automatiskt varje ändring som klarar flödet.

**[CDN (Content Delivery Network)](https://en.wikipedia.org/wiki/Content_delivery_network)** (innehållsleveransnätverk): Ett geografiskt distribuerat nätverk av kantservrar som cachar och levererar innehåll nära användarna, vilket minskar latens och avlastar ursprungsinfrastruktur.

**Chain-of-thought prompting**: En promptteknik som ber en språkmodell arbeta sig igenom mellanliggande resonemangssteg innan den ger ett slutligt svar, vilket förbättrar prestandan på flerstegsproblem till priset av längre, långsammare utdata.

**[CI (Continuous Integration)](https://en.wikipedia.org/wiki/Continuous_integration)** (kontinuerlig integrering): Praxisen att ofta slå ihop utvecklares ändringar i en gemensam huvudgren, där varje sammanslagning valideras av ett automatiserat bygge och en testsvit för att upptäcka integrationsproblem tidigt.

**[CI/CD](https://en.wikipedia.org/wiki/CI/CD)**: Det kombinerade flödet av kontinuerlig integrering och kontinuerlig leverans/driftsättning som automatiserar bygge, test och release av programvara.

**CMMC (Cybersecurity Maturity Model Certification)**: Ett program från USA:s försvarsdepartement som certifierar cybersäkerhetsmognaden hos entreprenörer som hanterar federal avtalsinformation och kontrollerad oklassificerad information.

**[Cohesion](https://en.wikipedia.org/wiki/Cohesion_(computer_science))** (sammanhållning): Graden i vilken elementen inuti en modul hör ihop och tjänar ett enda, väldefinierat syfte. Hög sammanhållning, parad med låg koppling, är ett kännetecken för underhållbar design.

**Context window** (kontextfönster): Den största textmängd, mätt i tokens, som en språkmodell kan beakta på en gång, omfattande både indata och utdata. Det är en knapp budget som prompt- och kontextdesign måste hantera medvetet.

**[Conway's Law](https://en.wikipedia.org/wiki/Conway's_law)** (Conways lag): Iakttagelsen att ett systems struktur tenderar att spegla kommunikationsstrukturen i den organisation som bygger det. Den "omvända Conway-manövern" formar medvetet team för att producera en önskad arkitektur.

**Core Web Vitals**: En uppsättning användarcentrerade webbprestandamått definierade av Google (som Largest Contentful Paint, Interaction to Next Paint och Cumulative Layout Shift) som mäter inladdning, interaktivitet och visuell stabilitet.

**[Cost of delay](https://en.wikipedia.org/wiki/Cost_of_delay)** (fördröjningskostnad): Den ekonomiska kostnaden för att något ännu inte är klart, uttryckt som förlorat värde per tidsenhet. Att göra den uttrycklig förvandlar prioritering från åsikt till aritmetik och ligger under sekvenseringsregler som viktat kortaste jobb först.

**[Coupling](https://en.wikipedia.org/wiki/Coupling_(computer_programming))** (koppling): Graden av ömsesidigt beroende mellan moduler eller tjänster. Lös koppling begränsar ringeffekten av förändring och är ett centralt mål för god arkitektur.

**CQRS (Command Query Responsibility Segregation)**: Ett mönster som skiljer modellen som används för att ändra tillstånd (kommandon) från modellen som används för att läsa tillstånd (frågor), så att var och en kan optimeras och skalas oberoende.

**[CVE (Common Vulnerabilities and Exposures)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)**: En offentlig katalog över offentliggjorda säkerhetssårbarheter, var och en tilldelad en unik identifierare så att verktyg och team kan hänvisa till samma brist entydigt.

**CWV**: Se Core Web Vitals.

## D

**[DAST (Dynamic Application Security Testing)](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)** (dynamisk applikationssäkerhetstestning): Säkerhetstestning som undersöker en körande applikation utifrån, utan tillgång till källkod, för att hitta sårbarheter som uppträder vid körtid.

**Data-ink ratio**: En princip från Edward Tufte som säger att ett diagram bör lägga det mesta av sitt bläck på själva datan och lite på dekoration, och ta bort rutnät, ramar och diagramskräp som inte informerar.

**[Data mesh](https://en.wikipedia.org/wiki/Data_mesh)**: En decentraliserad dataarkitektur och driftmodell som behandlar data som en produkt ägd av domänteam, stödd av självbetjäningsplattformsinfrastruktur och federerad styrning.

**[Data visualisation](https://en.wikipedia.org/wiki/Data_and_information_visualization)** (datavisualisering): Praxisen att koda data i visuell form (position, längd, färg och liknande) så att mönster, jämförelser och trender blir urskiljbara och beslut bättre underbyggda.

**[DDD (Domain-Driven Design)](https://en.wikipedia.org/wiki/Domain-driven_design)** (domändriven design): Ett förhållningssätt till programvarudesign som centrerar modellen på affärsdomänen och använder ett delat allmänt språk, avgränsade kontexter och byggstenar som entiteter, värdeobjekt och aggregat.

**Design tokens**: Namngivna, plattformsoberoende värden (färger, avstånd, typografi och liknande) som kodar designbeslut så att de kan delas konsekvent över ett designsystem och flera produkter.

**DevEx / DevX (Developer Experience)** (utvecklarupplevelse): Den samlade kvaliteten på en utvecklares dagliga interaktion med verktyg, plattformar och processer, omfattande friktion, återkopplingsfart och kognitiv belastning.

**[DevOps](https://en.wikipedia.org/wiki/DevOps)**: En kultur och en uppsättning praxis som förenar programvaruutveckling och drift för att förkorta leveranscykler, öka driftsättningsfrekvens och förbättra tillförlitlighet genom automation och delat ägarskap.

**DORA (DevOps Research and Assessment)**: Ett forskningsprogram och dess fyra vitt använda leveransmått (driftsättningsfrekvens, ledtid för ändringar, ändringsmisslyckandefrekvens och tid till återställning av tjänsten) som används för att jämföra programvaruleveransens prestanda.

**DPIA (Data Protection Impact Assessment)** (konsekvensbedömning avseende dataskydd): En strukturerad bedömning, krävd enligt GDPR för högriskbehandling, som identifierar och mildrar integritetsrisker innan ett projekt går vidare.

**Drift (configuration)** (konfigurationsdrift): Den gradvisa divergensen mellan ett systems faktiska tillstånd och dess deklarerade eller avsedda tillstånd, vanligen orsakad av manuella ändringar. Infrastruktur som kod och GitOps syftar till att upptäcka och korrigera den.

**Drift (model)** (modelldrift): Inom maskininlärning försämringen av modellprestanda över tid när indatas statistiska egenskaper (datadrift) eller det samband som modelleras (konceptdrift) förändras.

**[DR (Disaster Recovery)](https://en.wikipedia.org/wiki/Disaster_recovery)** (katastrofåterställning): Strategin, rutinerna och infrastrukturen för att återställa tjänst och data efter en större störande händelse, vanligen styrd av RTO- och RPO-mål.

**[DRY (Don't Repeat Yourself)](https://en.wikipedia.org/wiki/Don't_repeat_yourself)**: En designprincip som säger att varje kunskapsbit bör ha en enda, auktoritativ representation, vilket minskar duplicering och risken för inkonsekventa uppdateringar.

## E

**East-west traffic** (öst-västtrafik): Nätverkstrafik mellan tjänster inuti ett system eller ett datacenter, i motsats till nord-sydtrafik mellan systemet och externa klienter. Ett tjänstenät styr typiskt öst-västtrafik.

**[Edge computing](https://en.wikipedia.org/wiki/Edge_computing)** (kantberäkning): Att köra beräkning och lagring nära där data produceras eller konsumeras snarare än på en central plats, för att minska latens och bandbredd. Innehållsleveransnätverk är en tidig, utbredd form.

**[Elasticity](https://en.wikipedia.org/wiki/Elasticity_(cloud_computing))** (elasticitet): Ett systems förmåga att automatiskt skaffa och frigöra resurser som svar på varierande efterfrågan, så att kapaciteten följer lasten tätt.

**[ELT (Extract, Load, Transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform)**: Ett dataintegrationsmönster som laddar rådata till ett målförråd först och transformerar den där, och utnyttjar skalan hos moderna lager och lakehouses.

**[Embedding](https://en.wikipedia.org/wiki/Word_embedding)** (inbäddning): En representation av text, bilder eller andra data som en tät numerisk vektor, placerad så att liknande poster hamnar nära varandra. Inbäddningar driver semantisk sökning, vektorsökning och retrieval-augmented generation.

**[EN 301 549](https://en.wikipedia.org/wiki/EN_301_549)**: Den europeiska standard som anger tillgänglighetskrav för IKT-produkter och -tjänster, refererad av offentlig upphandling över hela EU och anpassad till WCAG.

**Error budget** (felbudget): Den tillåtna mängden otillförlitlighet som ett SLO medger över en period. När den är förbrukad prioriterar team tillförlitlighetsarbete framför nya funktioner. Den förlikar spänningen mellan fart och stabilitet.

**[ETL (Extract, Transform, Load)](https://en.wikipedia.org/wiki/Extract,_transform,_load)**: Ett dataintegrationsmönster som extraherar data från källor, transformerar den till en målform och laddar den till ett mål som ett lager.

**[EU AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act)** (EU:s AI-förordning): Europeiska unionens reglering som klassificerar AI-system efter risk och ställer krav därefter, förbjuder vissa användningar och reglerar högriskssystem kraftigt.

**[Eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency)** (slutlig konsistens): En konsistensmodell i distribuerade system där repliker tillfälligt kan divergera men konvergerar till samma tillstånd när uppdateringarna slutar spridas.

## F

**[Feature flag / feature toggle](https://en.wikipedia.org/wiki/Feature_toggle)** (funktionsflagga): En mekanism för att slå på eller av funktionalitet vid körtid utan omdriftsättning, använd för gradvisa utrullningar, experimentering och operativ kontroll.

**Feature store**: Ett centraliserat system för att definiera, lagra och servera kurerade maskininlärningsfunktioner (features) konsekvent både för träning och inferens, vilket minskar duplicering och skillnaden mellan träning och drift.

**[FedRAMP (Federal Risk and Authorisation Management Program)](https://en.wikipedia.org/wiki/FedRAMP)**: Ett amerikanskt statligt program som standardiserar säkerhetsbedömning, auktorisering och kontinuerlig övervakning för molntjänster som används av federala myndigheter.

**Few-shot prompting**: Att förse en språkmodell med en handfull genomarbetade exempel i prompten för att visa den önskade uppgiften och utdataformatet, i motsats till zero-shot prompting, som ger instruktioner utan exempel.

**FinOps**: En disciplin och kulturell praxis som för in ekonomisk ansvarsskyldighet i variabla molnkostnader och ger teknik, ekonomi och verksamhet delat ägarskap av kostnad och värde.

**[FISMA (Federal Information Security Modernisation Act)](https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act)**: Amerikansk lagstiftning som kräver att federala myndigheter inför, dokumenterar och övervakar informationssäkerhetsprogram, i stor utsträckning operationaliserad genom NIST-vägledning.

**Flow efficiency** (flödeseffektivitet): Den andel av den totala ledtiden ett arbetsobjekt tillbringar med att aktivt bearbetas snarare än att vänta, beräknad som värdeskapande tid delad med total ledtid. De flesta system är förvånansvärt låga, ofta under 15 procent.

**Four-eyes principle** (fyraögonprincipen): En kontroll som kräver att en betydande åtgärd granskas eller godkänns av minst två personer, vilket minskar risken för fel eller förskingring.

**[Fuzz testing (fuzzing)](https://en.wikipedia.org/wiki/Fuzzing)**: En automatiserad testteknik som matar ett program med felformade, slumpmässiga eller oväntade indata för att avslöja krascher, säkerhetsbrister och kantfallsdefekter.

## G

**[GDPR (General Data Protection Regulation)](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)** (dataskyddsförordningen): Europeiska unionens reglering av behandling av personuppgifter, som ger individer rättigheter och ålägger personuppgiftsansvariga och biträden skyldigheter, med kännbara sanktioner vid bristande efterlevnad.

**GitOps**: En driftmodell som använder Git som enda sanningskälla för deklarativ infrastruktur och applikationer, där automation kontinuerligt avstämmer det levande systemet mot det incheckade tillståndet.

**Golden path / paved road** (upptrampad stig): Ett väl stött, tydligt uttalat standardsätt att bygga och leverera programvara inom en organisation, utformat för att göra det säkra, efterlevande, tillförlitliga valet till det enklaste.

**Golden record** (gyllene post): Inom masterdatahantering den enda, avstämda, auktoritativa versionen av en affärsentitet (som en kund), sammansatt från flera källsystem genom matchnings- och överlevnadsregler.

**[Gradual typing](https://en.wikipedia.org/wiki/Gradual_typing)** (gradvis typning): Ett typsystemsförhållningssätt som låter statisk och dynamisk typning samexistera i en kodbas, så att typer kan läggas till stegvis i ett dynamiskt typat program. Typtips och valfria typkontrollanter är vanliga exempel.

**[GraphQL](https://en.wikipedia.org/wiki/GraphQL)**: Ett frågespråk och en körtid för API:er som låter klienter begära exakt de data de behöver i ett enda anrop, med ett starkt typat schema.

**[gRPC](https://en.wikipedia.org/wiki/gRPC)**: Ett högpresterande, kontraktsförst-ramverk för fjärrproceduranrop som använder HTTP/2 och typiskt Protocol Buffers för effektiv kommunikation mellan tjänster.

## H

**Hermetic build** (hermetiskt bygge): Ett bygge som bara beror på uttryckligen deklarerade indata och är isolerat från värdmiljön, så att det producerar samma utdata överallt. Hermetiskhet är grunden för reproducerbara byggen och tillförlitlig cachning.

**[HSM (Hardware Security Module)](https://en.wikipedia.org/wiki/Hardware_security_module)** (hårdvarusäkerhetsmodul): En manipuleringsskyddad hårdvaruenhet som genererar, lagrar och använder kryptografiska nycklar och ger starkare nyckelskydd än enbart programvarubaserade lösningar.

**[HIPAA (Health Insurance Portability and Accountability Act)](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)**: Amerikansk lagstiftning som bland annat ställer krav på skydd av skyddad hälsoinformation (PHI) och reglerar dess användning och utlämnande.

**Horizontal scaling** (horisontell skalning): Att öka kapaciteten genom att lägga till fler instanser eller noder ("skala ut") snarare än att göra en enskild nod kraftfullare. Den ligger under de flesta storskaliga, motståndskraftiga arkitekturer.

## I

**[IaC (Infrastructure as Code)](https://en.wikipedia.org/wiki/Infrastructure_as_code)** (infrastruktur som kod): Praxisen att definiera och tillhandahålla infrastruktur genom maskinläsbar, versionshanterad konfiguration snarare än manuella processer, vilket möjliggör upprepbarhet och granskning.

**[IAM (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_management)** (identitets- och åtkomsthantering): Ramverket av policyer och tekniker som säkerställer att rätt identiteter har rätt åtkomst till rätt resurser vid rätt tidpunkter.

**IDP / IdP**: "IDP" betecknar vanligen en intern utvecklarplattform (Internal Developer Platform), självbetjäningsverktygslagret som abstraherar infrastruktur för produktteam. "IdP" betecknar en identitetsleverantör (Identity Provider), en tjänst som autentiserar användare och utfärdar intyg. Sammanhanget skiljer de två åt.

**[Idempotency](https://en.wikipedia.org/wiki/Idempotence)** (idempotens): En egenskap där att utföra en operation flera gånger har samma effekt som att utföra den en gång, avgörande för säkra omförsök i distribuerade system och API:er.

**[i18n (Internationalisation)](https://en.wikipedia.org/wiki/Internationalization_and_localization)** (internationalisering): Att utforma och bygga programvara så att den kan anpassas till olika språk, regioner och kulturella konventioner utan tekniska ändringar. Numeronymen förkortar de 18 bokstäverna mellan "i" och "n."

**Immutable artefact** (oföränderlig artefakt): Ett byggresultat som, när det väl producerats och versionshanterats, aldrig ändras. Varje ändring ger en ny version. Oföränderlighet gör releaser reproducerbara och låter er bygga en gång och befordra samma artefakt mellan miljöer.

**InnerSource**: Tillämpningen av utvecklingspraxis från öppen källkod (transparens, delade förvar och bidrag över teamgränser) inom en enskild organisation.

**IaC drift**: Se Drift (configuration).

**[Inverted index](https://en.wikipedia.org/wiki/Inverted_index)** (inverterat index): En sökmotors kärndatastruktur, som kopplar varje term till listan över dokument som innehåller den, så att frågor kan besvaras utan att skanna varje dokument.

**[ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001)**: En internationell standard som anger krav på ett ledningssystem för informationssäkerhet (ISMS) och ger ett certifierbart ramverk för att hantera informationssäkerhetsrisk.

**ISO/IEC 42001**: En internationell standard som anger krav på ett ledningssystem för AI och ger organisationer ett certifierbart ramverk för att styra utveckling och användning av AI ansvarsfullt.

## J

**[JWT (JSON Web Token)](https://en.wikipedia.org/wiki/JSON_Web_Token)**: Ett kompakt, signerat (och valfritt krypterat) tokenformat som används för att förmedla påståenden mellan parter, vanligen för autentisering och auktorisering i webb- och API-system.

## K

**[Kanban](https://en.wikipedia.org/wiki/Kanban_(development))**: En lean-arbetsflödesmetod som visualiserar arbete på en tavla, begränsar pågående arbete och hanterar flöde för att förbättra genomströmning och förutsägbarhet.

**[KISS (Keep It Simple, Stupid)](https://en.wikipedia.org/wiki/KISS_principle)**: En designprincip som föredrar den enklaste lösning som möter behovet, med motiveringen att onödig komplexitet ökar kostnad och risk.

**KMS (Key Management Service)** (nyckelhanteringstjänst): Ett system för att skapa, lagra, rotera och kontrollera åtkomst till kryptografiska nycklar, ofta understött av hårdvarusäkerhetsmoduler.

**[KPI (Key Performance Indicator)](https://en.wikipedia.org/wiki/Performance_indicator)** (nyckeltal): Ett kvantifierbart mått som används för att följa framsteg mot ett specifikt affärs- eller operativt mål.

## L

**Lakehouse**: En dataarkitektur som kombinerar den billiga, flexibla lagringen hos en datasjö med hanterings-, transaktions- och prestandafunktionerna hos ett datalager.

**[Lead time](https://en.wikipedia.org/wiki/Lead_time)** (ledtid): Den förflutna tiden från att en ändring begärs (eller checkas in) till att den levereras till produktion. Ett centralt DORA-leveransmått.

**[Least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)** (minsta behörighet): En säkerhetsprincip som ger varje användare, process eller system bara den minimiåtkomst som krävs för att utföra sin funktion och begränsar skadan från komprometterande eller fel.

**[Little's Law](https://en.wikipedia.org/wiki/Little's_law)** (Littles lag): Ett resultat från köteori som säger att det genomsnittliga antalet poster i ett stabilt system är lika med den genomsnittliga ankomsttakten multiplicerad med den genomsnittliga tid varje post tillbringar i systemet. Den kopplar pågående arbete, genomströmning och ledtid.

**[LLM (Large Language Model)](https://en.wikipedia.org/wiki/Large_language_model)** (stor språkmodell): En maskininlärningsmodell tränad på mycket stora textkorpusar för att förutsäga och generera språk, med förmåga till uppgifter som sammanfattning, översättning och kodgenerering.

**[l10n (Localisation)](https://en.wikipedia.org/wiki/Language_localisation)** (lokalisering): Att anpassa internationaliserad programvara till en specifik lokal, inklusive översättning, formatering och kulturella konventioner. Numeronymen förkortar de 10 bokstäverna mellan "l" och "n."

## M

**[MDM (Master Data Management)](https://en.wikipedia.org/wiki/Master_data_management)** (masterdatahantering): Disciplinen och verktygen för att skapa och underhålla en enda, auktoritativ, konsekvent bild av centrala affärsentiteter (som kunder eller produkter) över system.

**MITRE ATT&CK**: En kurerad, offentlig kunskapsbas över verkliga motståndartaktiker och -tekniker, vitt använd för att planera red team-övningar, styra detekteringsingenjörskap och beskriva hot i ett gemensamt ordförråd.

**Mean Time to Recovery (MTTR)**: Den genomsnittliga tid det tar att återställa tjänst efter ett fel. Ett vanligt tillförlitlighets- och incidenthanteringsmått.

**[Mob programming](https://en.wikipedia.org/wiki/Mob_programming)**: En praxis där ett helt team arbetar tillsammans med samma uppgift vid samma dator och roterar vem som skriver, för att dela kunskap och fatta beslut kollektivt.

**[MLOps (Machine Learning Operations)](https://en.wikipedia.org/wiki/MLOps)**: Den uppsättning praxis som tillförlitligt och effektivt driftsätter, övervakar och underhåller maskininlärningsmodeller i produktion och utvidgar DevOps-principer till ML-livscykeln.

**[Monorepo](https://en.wikipedia.org/wiki/Monorepo)**: Ett enda versionshanteringsförvar som rymmer koden för många projekt eller hela organisationen och möjliggör delade verktyg och atomära ändringar över projekt, till priset av specialiserade skalningsverktyg.

**mTLS (mutual TLS)**: En konfiguration av Transport Layer Security där båda parter presenterar och verifierar certifikat, så att var och en autentiserar den andra. Det är standard för trafik mellan tjänster i ett tjänstenät och i nolltillitsnätverk. Se även [ömsesidig autentisering](https://en.wikipedia.org/wiki/Mutual_authentication).

**[Mutation testing](https://en.wikipedia.org/wiki/Mutation_testing)** (mutationstestning): En teknik som medvetet för in små fel ("mutanter") i kod för att kontrollera om testsviten upptäcker dem och därmed mäta svitens verkliga effektivitet.

## N

**[NDCG (Normalised Discounted Cumulative Gain)](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)**: Ett rankningskvalitetsmått som belönar att mycket relevanta resultat placeras nära toppen av en resultatlista, normaliserat så att poäng är jämförbara över frågor. Det är ett stapelmått i utvärdering av sökrelevans.

**[NIST (National Institute of Standards and Technology)](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)**: En amerikansk federal myndighet vars specialpublikationer och ramverk är vitt refererade standarder för cybersäkerhet, integritet och AI.

**NIST AI RMF (AI Risk Management Framework)**: Ett frivilligt NIST-ramverk för att identifiera, bedöma och hantera risker förknippade med AI-system genom hela livscykeln, organiserat kring funktionerna Govern, Map, Measure och Manage.

**[NIST SP 800-53](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53)**: En NIST-katalog över säkerhets- och integritetskontroller för federala informationssystem, vitt använd som baslinje långt utanför staten.

**NIST SP 800-171**: En NIST-publikation som anger krav för att skydda kontrollerad oklassificerad information (CUI) i icke-federala system, central för försvarsentreprenörers efterlevnad.

**[NFR (Non-Functional Requirement)](https://en.wikipedia.org/wiki/Non-functional_requirement)** (icke-funktionellt krav): Ett krav som beskriver hur ett system ska bete sig (dess kvaliteter som prestanda, säkerhet, tillförlitlighet eller användbarhet) snarare än vilka funktioner det utför.

**North-south traffic** (nord-sydtrafik): Nätverkstrafik mellan ett system och dess externa klienter (in och ut ur datacentret eller klustret), i motsats till öst-västtrafik mellan interna tjänster. En API-gateway styr typiskt nord-sydtrafik.

## O

**Observability** (observerbarhet): Graden i vilken ett systems inre tillstånd kan härledas ur dess yttre utdata, typiskt uppnådd genom telemetri: mått, loggar och spår.

**[OKR (Objectives and Key Results)](https://en.wikipedia.org/wiki/OKR)** (mål och nyckelresultat): Ett målsättningsramverk som parar ett kvalitativt mål med några få mätbara nyckelresultat för att linjera och fokusera en organisation.

**OpenTelemetry (OTel)**: En leverantörsneutral, öppen standard och verktygsuppsättning för att generera, samla in och exportera telemetridata (spår, mått och loggar) från programvara.

**OPA (Open Policy Agent)**: En allmän policymotor med öppen källkod som utvärderar policyer (skrivna i språket Rego) för att upprätthålla auktoriserings- och konfigurationsregler genom hela stacken och möjliggör policy som kod.

**OSPO (Open Source Program Office)** (kontor för öppen källkod): En organisatorisk funktion som samordnar strategi, styrning, efterlevnad och gemenskapsengagemang kring öppen källkod och hanterar både konsumtion och bidrag.

**[OWASP (Open Worldwide Application Security Project)](https://en.wikipedia.org/wiki/OWASP)**: En ideell gemenskap som producerar vitt använda, fritt tillgängliga resurser för applikationssäkerhet, inklusive OWASP Top Ten och ASVS.

## P

**[PACELC](https://en.wikipedia.org/wiki/PACELC_theorem)**: En utvidgning av CAP-satsen som säger att om det finns en partition (Partition) väger ett system tillgänglighet (Availability) mot konsistens (Consistency), annars (Else, i normal drift) väger det latens (Latency) mot konsistens (Consistency).

**[PCI DSS (Payment Card Industry Data Security Standard)](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)**: En säkerhetsstandard som underhålls av betalkortsbranschen och anger krav för organisationer som lagrar, behandlar eller överför kortinnehavardata.

**[Penetration testing](https://en.wikipedia.org/wiki/Penetration_test)** (penetrationstestning): En auktoriserad, simulerad attack mot ett system av skickliga testare för att hitta och demonstrera utnyttjningsbara sårbarheter innan verkliga angripare gör det, levererad som prioriterade, handlingsbara fynd.

**[PII (Personally Identifiable Information)](https://en.wikipedia.org/wiki/Personal_data)** (personuppgifter): Information som kan identifiera en specifik individ, antingen ensam eller i kombination med andra data. Dess hantering styrs av integritetslagar och intern policy.

**Platform engineering** (plattformsteknik): Disciplinen att bygga och driva interna självbetjäningsplattformar och upptrampade stigar som minskar kognitiv belastning och påskyndar produktteam.

**POUR**: De fyra vägledande principerna i Web Content Accessibility Guidelines: innehåll måste vara Perceivable (möjligt att uppfatta), Operable (hanterbart), Understandable (begripligt) och Robust.

**Production readiness review** (granskning av produktionsberedskap): En strukturerad kontroll, körd innan en tjänst går live eller tar över jouransvar, som bekräftar att den möter standarder för observerbarhet, tillförlitlighet, säkerhet, körböcker och operativt stöd.

**[Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering)** (promptteknik): Praxisen att utforma och förfina de instruktioner, det sammanhang och de exempel som ges till en språkmodell för att få pålitliga utdata av hög kvalitet, behandlad som en versionshanterad, testad ingenjörsdisciplin snarare än försök och misstag.

**[Prompt injection](https://en.wikipedia.org/wiki/Prompt_injection)** (promptinjektion): En attack där utformade indata får en språkmodell att ignorera sina avsedda instruktioner och följa angriparens i stället, AI-erans motsvarighet till injektionsbrister. Det är en central säkerhetsrisk för LLM-applikationer.

**Property-based testing** (egenskapsbaserad testning): En testteknik som kontrollerar att angivna egenskaper gäller över många automatiskt genererade indata, i stället för att bara förlita sig på handplockade exempel.

**Pull request (PR) / merge request (MR)**: En föreslagen uppsättning ändringar som skickas in för granskning och diskussion innan den slås ihop i en delad gren, den primära enheten för kodgranskning i de flesta arbetsflöden.

**Purple team**: En samarbetsövning där offensiva (röda) och defensiva (blå) säkerhetsteam arbetar tillsammans i realtid, så att attacker och de detekteringar som ska fånga dem finjusteras mot varandra.

## Q

**Quality gate** (kvalitetsgrind): En automatiserad kontrollpunkt i ett flöde som måste passeras (till exempel uppfylla täcknings-, säkerhets- eller prestandatrösklar) innan en ändring kan gå vidare.

**[Quorum](https://en.wikipedia.org/wiki/Quorum_(distributed_computing))** (kvorum): I distribuerade system det minsta antal noder som måste vara överens för att en operation (som en läsning eller skrivning) ska anses lyckad, använt för att bibehålla konsistens trots fel.

## R

**[RACI](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)**: En ansvarsfördelningsmodell som märker varje deltagare i en uppgift eller ett beslut som Responsible (utförande), Accountable (ansvarig), Consulted (konsulterad) eller Informed (informerad).

**[RAG (Retrieval-Augmented Generation)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)**: En teknik som förankrar en språkmodells utdata genom att först hämta relevanta dokument eller data och förse dem som kontext, vilket förbättrar noggrannheten och minskar hallucinationer.

**[RBAC (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control)** (rollbaserad åtkomstkontroll): En auktoriseringsmodell som tilldelar behörigheter till roller och roller till användare, vilket förenklar administrationen genom att hantera åtkomst på rollnivå.

**[Red team](https://en.wikipedia.org/wiki/Red_team)**: En grupp som emulerar en realistisk motståndare, ofta mot en hel organisation och utan förvarning till försvararna, för att testa detektering och respons snarare än att bara räkna upp sårbarheter. Kontrast: ett blått (defensivt) team.

**[Reference data](https://en.wikipedia.org/wiki/Reference_data)** (referensdata): Kontrollerade, långsamt föränderliga kodlistor och klassificeringar som används för att kategorisera andra data, som landskoder, valutor och statusvärden. Att styra dem som ett delat, versionshanterat ordförråd håller system konsekventa.

**Rego**: Det deklarativa policyspråk som Open Policy Agent använder för att uttrycka regler för auktoriserings- och konfigurationsbeslut.

**[REST (Representational State Transfer)](https://en.wikipedia.org/wiki/REST)**: En arkitekturstil för nätverksanslutna applikationer som använder tillståndslösa operationer över HTTP på adresserbara resurser, uppskattad för enkelhet och bred verktygsstöd.

**[Reverse proxy](https://en.wikipedia.org/wiki/Reverse_proxy)** (omvänd proxy): En server som sitter framför en eller flera backend-tjänster och vidarebefordrar klientförfrågningar till dem, och vanligen tillhandahåller TLS-terminering, lastbalansering, cachning och en gemensam ingångspunkt.

**[RFC (Request for Comments)](https://en.wikipedia.org/wiki/Request_for_Comments)**: Ett skriftligt förslag som cirkuleras för återkoppling före ett betydande tekniskt beslut eller en ändring och främjar transparens och delat ägarskap. (Termen betecknar också dokumentserien för internetstandarder.)

**[ROI (Return on Investment)](https://en.wikipedia.org/wiki/Return_on_investment)** (avkastning på investering): Ett mått på det värde som uppnås av en investering i förhållande till dess kostnad, använt för att motivera och prioritera tekniska och teknologiska beslut.

**[RPA (Robotic Process Automation)](https://en.wikipedia.org/wiki/Robotic_process_automation)** (robotiserad processautomation): Programvaruroboter som automatiserar repetitiva, regelbaserade uppgifter genom att interagera med befintliga användargränssnitt och system som en människa skulle.

**RPO (Recovery Point Objective)** (mål för återställningspunkt): Den största godtagbara mängden dataförlust mätt i tid (till exempel "upp till fem minuter"), vilket definierar hur ofta data måste skyddas.

**RTO (Recovery Time Objective)** (mål för återställningstid): Den längsta godtagbara tiden för att återställa en tjänst efter en störning, vägledande för design och investering i katastrofåterställning.

## S

**Saga**: Ett mönster för att hantera datakonsistens över tjänster i en distribuerad transaktion genom att sekvensera lokala transaktioner och utfärda kompenserande åtgärder när ett steg misslyckas.

**[SAFe (Scaled Agile Framework)](https://en.wikipedia.org/wiki/Scaled_agile_framework)**: Ett ramverk för att tillämpa agil och lean praxis över stora företag och samordna många team. Uppskattat för struktur och kritiserat för potentiell tyngd.

**[SAST (Static Application Security Testing)](https://en.wikipedia.org/wiki/Static_application_security_testing)** (statisk applikationssäkerhetstestning): Säkerhetstestning som analyserar källkod, bytekod eller binärer utan att köra dem för att hitta sårbarheter tidigt i utvecklingen.

**SBOM (Software Bill of Materials)** (materialförteckning för programvara): En formell, maskinläsbar inventering av komponenterna och beroendena i en programvara, använd för att hantera leveranskedje- och sårbarhetsrisk.

**SCA (Software Composition Analysis)** (programvarukompositionsanalys): Verktyg som identifierar komponenter med öppen källkod och från tredje part i en kodbas och flaggar kända sårbarheter och licensrisker.

**[Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development))**: Ett agilt ramverk som organiserar arbete i iterationer med fast längd (sprintar) med definierade roller, händelser och artefakter för att leverera värdeinkrement.

**[Section 508](https://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)**: En amerikansk lag som kräver att federala myndigheter gör sin elektroniska teknik och informationsteknik tillgänglig för personer med funktionsnedsättning, i praktiken anpassad till WCAG.

**Semantic search** (semantisk sökning): Sökning som matchar på betydelse snarare än exakta nyckelord, typiskt genom att jämföra inbäddningar av frågan och dokumenten. Den kombineras ofta med lexikal sökning i ett hybridupplägg.

**[Service mesh](https://en.wikipedia.org/wiki/Service_mesh)** (tjänstenät): Ett dedikerat infrastrukturlager, vanligen implementerat med sidecar-proxyer, som hanterar frågor kring kommunikation mellan tjänster som ömsesidig TLS, omförsök, timeouter, trafikflytt och observerbarhet och håller dem utanför applikationskoden.

**Sidecar**: En hjälpprocess eller -container som driftsätts vid sidan av en huvudapplikationsinstans för att ge stödfunktioner (som en tjänstenätsproxy) utan att ändra själva applikationen.

**[SIEM (Security Information and Event Management)](https://en.wikipedia.org/wiki/Security_information_and_event_management)**: Ett system som aggregerar och korrelerar säkerhetsloggar och händelser över en miljö för att möjliggöra detektering, larm och utredning.

**[SLA (Service Level Agreement)](https://en.wikipedia.org/wiki/Service-level_agreement)** (servicenivåavtal): Ett formellt åtagande mellan en tjänsteleverantör och dess kunder som anger förväntade servicenivåer och konsekvenserna av att missa dem.

**SLI (Service Level Indicator)** (servicenivåindikator): Ett kvantitativt mått på någon aspekt av tjänstekvalitet, som begäranslatens eller felfrekvens, som matar SLO:er.

**SLO (Service Level Objective)** (servicenivåmål): Ett målvärde eller intervall för en SLI som definierar önskad tillförlitlighetsnivå och utgör grunden för felbudgetar.

**SLSA (Supply-chain Levels for Software Artifacts)**: Ett ramverk av graderade säkerhetskrav för att förbättra integritet och ursprung hos programvaruartefakter genom bygg- och releaseprocessen.

**SOAR (Security Orchestration, Automation, and Response)**: Verktyg och praxis som automatiserar och samordnar säkerhetsoperationer, som triage och responsspelböcker, för att förbättra fart och konsekvens.

**SOC 2 (System and Organisation Controls 2)**: Ett revisionsramverk och en rapport, baserad på AICPA:s Trust Services Criteria, som bedömer en tjänsteorganisations kontroller för säkerhet, tillgänglighet, behandlingsintegritet, konfidentialitet och integritet.

**[SOLID](https://en.wikipedia.org/wiki/SOLID)**: Fem objektorienterade designprinciper (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation och Dependency Inversion) som främjar underhållbar, flexibel kod.

**[SOX (Sarbanes-Oxley Act)](https://en.wikipedia.org/wiki/Sarbanes-Oxley_Act)**: Amerikansk lagstiftning som fastställer krav på finansiell rapportering och interna kontroller i börsnoterade företag, med konsekvenser för de IT-system som stöder finansiella data.

**SPACE**: Ett ramverk för att mäta utvecklarproduktivitet över fem dimensioner: Satisfaction and well-being (nöjdhet och välbefinnande), Performance, Activity, Communication and collaboration samt Efficiency and flow, med varning mot mått baserade på ett enda tal.

**[SRE (Site Reliability Engineering)](https://en.wikipedia.org/wiki/Site_reliability_engineering)** (platsförlitlighetsteknik): En disciplin som tillämpar programvaruingenjörskunskap på drift och använder SLO:er, felbudgetar och automation för att köra tillförlitliga system i skala.

**SSDF (Secure Software Development Framework)**: NIST:s ramverk (SP 800-218) av övergripande praxis för säker utveckling, omfattande att förbereda organisationen, skydda programvara, producera välsäkrad programvara och svara på sårbarheter.

**[Static analysis](https://en.wikipedia.org/wiki/Static_program_analysis)** (statisk analys): Att granska källkod, bytekod eller binärer utan att köra dem för att hitta defekter, stilöverträdelser och säkerhetsbrister, typiskt genom lintrar, typkontrollanter och dedikerade analysatorer kopplade till editorn och flödet.

**[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)**: En hotmodelleringstaxonomi som kategoriserar hot som Spoofing (förfalskning av identitet), Tampering (manipulering), Repudiation (förnekande), Information disclosure (informationsläckage), Denial of service (överbelastning) och Elevation of privilege (behörighetseskalering).

## T

**[TCO (Total Cost of Ownership)](https://en.wikipedia.org/wiki/Total_cost_of_ownership)** (total ägandekostnad): Den fulla livstidskostnaden för ett system eller beslut, inklusive anskaffning, drift, underhåll och slutlig avveckling, inte bara det initiala priset.

**[TDD (Test-Driven Development)](https://en.wikipedia.org/wiki/Test-driven_development)** (testdriven utveckling): En praxis att skriva ett misslyckat automatiserat test före koden som får det att passera och sedan refaktorera, i korta upprepade cykler för att driva design och säkerställa täckning.

**[Technical debt](https://en.wikipedia.org/wiki/Technical_debt)** (teknisk skuld): Den underförstådda framtida kostnaden av att välja en snabb lösning nu framför en bättre som skulle ta längre tid, vilken måste hanteras medvetet snarare än samlas omedvetet.

**TF-IDF (Term Frequency-Inverse Document Frequency)**: Ett klassiskt viktningsschema som poängsätter en terms betydelse för ett dokument efter hur ofta den förekommer där, balanserat mot hur vanlig den är i hela korpusen. Det ligger under mycket av den lexikala sökrankningen.

**[Theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints)** (begränsningsteori): Ett ledningssätt som hävdar att ett systems genomströmning vid varje tidpunkt begränsas av en enda flaskhals, så förbättringsinsatser bör fokusera på den begränsningen tills den flyttar sig någon annanstans.

**[Threat modelling](https://en.wikipedia.org/wiki/Threat_model)** (hotmodellering): En strukturerad praxis att identifiera, räkna upp och prioritera potentiella hot mot ett system så att försvar kan utformas tidigt.

**Toil** (slit): Inom SRE manuellt, repetitivt, automatiserbart operativt arbete som skalar linjärt med en tjänst och inte ger något bestående värde. Att minska det frigör kapacitet för ingenjörsarbete.

**Trunk-based development** (trunk-baserad utveckling): En källkodshanteringspraxis där utvecklare ofta integrerar små ändringar i en enda delad gren och minimerar långlivade grenar och sammanslagningssmärta.

**[Type inference](https://en.wikipedia.org/wiki/Type_inference)** (typinferens): En språkfunktion som härleder uttrycks typer automatiskt och ger mycket av den statiska typningens säkerhet utan att kräva att varje typ skrivs ut för hand.

**[Type system](https://en.wikipedia.org/wiki/Type_system)** (typsystem): Den uppsättning regler ett språk använder för att tilldela och kontrollera typer, vilket fångar hela klasser av fel innan programmet körs och dokumenterar avsikt. Typsystem sträcker sig från dynamiska till statiska och från svaga till starka.

## U

**Ubiquitous language** (allmänt delat språk): Inom Domain-Driven Design ett delat, precist ordförråd som används konsekvent av utvecklare och domänexperter och speglas direkt i koden och modellerna.

**[UAT (User Acceptance Testing)](https://en.wikipedia.org/wiki/Acceptance_testing)** (användaracceptanstestning): Testning utförd av slutanvändare eller deras företrädare för att bekräfta att ett system möter affärsbehoven innan det godtas för release.

**[UX / UI (User Experience / User Interface)](https://en.wikipedia.org/wiki/User_experience)** (användarupplevelse / användargränssnitt): Användarupplevelse är den samlade kvaliteten på en persons interaktion med en produkt. Användargränssnitt är den specifika visuella och interaktiva yta genom vilken den interaktionen sker.

## V

**[Value object](https://en.wikipedia.org/wiki/Value_object)** (värdeobjekt): Inom Domain-Driven Design ett oföränderligt objekt som helt definieras av sina attribut snarare än en särskild identitet, som ett penningbelopp eller ett datumintervall.

**[Value stream mapping](https://en.wikipedia.org/wiki/Value-stream_mapping)** (värdeflödeskartläggning): En teknik för att rita upp varje steg från idé till levererat värde och skilja värdeskapande tid från väntetid, så att flaskhalsar, överlämningar och omarbetsslingor blir synliga och förbättringsbara.

**[Vector database](https://en.wikipedia.org/wiki/Vector_database)** (vektordatabas): Ett datalager optimerat för att indexera och söka högdimensionella inbäddningsvektorer efter likhet, en vanlig ryggrad i semantisk sökning och retrieval-augmented generation.

**Vertical scaling** (vertikal skalning): Att öka kapaciteten genom att göra en enskild nod kraftfullare ("skala upp"), vilket är enkelt men i slutändan begränsat av den största tillgängliga maskinen.

**[VCS (Version Control System)](https://en.wikipedia.org/wiki/Version_control)** (versionshanteringssystem): Ett verktyg, som Git, som registrerar ändringar i filer över tid så att historik kan granskas, grenar kan underhållas och arbete kan samordnas.

**[Vulnerability scanning](https://en.wikipedia.org/wiki/Vulnerability_scanner)** (sårbarhetsskanning): Automatiserad inspektion av system, containrar eller kod mot databaser över kända svagheter och felkonfigurationer. Den är bred och billig och kompletterar djupet hos manuell penetrationstestning.

## W

**[WCAG (Web Content Accessibility Guidelines)](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines)**: En W3C-uppsättning internationellt erkända riktlinjer, organiserade kring POUR-principerna och efterlevnadsnivåerna A, AA och AAA, för att göra webbinnehåll tillgängligt.

**Wardley map**: En visuell strategiteknik som placerar förmågor efter deras värde för användare och deras evolutionära mognad, för att informera beslut om att bygga eller köpa och om investeringar.

**Work in progress (WIP) limit** (WIP-gräns): En begränsning av hur många poster som får finnas i ett givet steg av ett arbetsflöde samtidigt, en central Kanban-praxis som förbättrar flödet genom att blottlägga flaskhalsar och hejda overheaden av för mycket parallellt arbete.

**WSJF (Weighted Shortest Job First)** (viktat kortaste jobb först): En prioriteringsmetod som sekvenserar arbete genom att dela dess fördröjningskostnad med dess uppskattade varaktighet, så att de kortaste, mest tidskänsliga och mest värdefulla posterna görs först.

## X

**[XSS (Cross-Site Scripting)](https://en.wikipedia.org/wiki/Cross-site_scripting)**: En webbsårbarhet där en angripare injicerar skadliga skript som körs i andra användares webbläsare och potentiellt stjäl data eller kapar sessioner.

## Y

**[YAGNI (You Aren't Gonna Need It)](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it)**: En princip som avråder från att bygga funktionalitet på spekulation, med motiveringen att förväntade behov ofta aldrig materialiseras och tillför kostnad och komplexitet.

## Z

**[Zero trust](https://en.wikipedia.org/wiki/Zero_trust_security_model)** (nolltillit): En säkerhetsmodell som inte antar något implicit förtroende utifrån nätverksplats och kontinuerligt verifierar varje åtkomstbegäran mot identitet, enhet och kontext, enligt maximen "lita aldrig, verifiera alltid."
