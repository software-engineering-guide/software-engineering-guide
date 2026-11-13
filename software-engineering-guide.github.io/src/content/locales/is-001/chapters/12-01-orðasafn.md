# 12.1 Orðasafn

Þetta orðasafn skilgreinir hugtök og skammstafanir sem notuð eru um alla
handbókina. Færslurnar eru flokkaðar í stafrófsröð eftir ensku uppflettiorðunum,
sem þú rekst á í verkfærum og skjölum. Íslensk jafngildi standa innan sviga þar
sem rótgróið jafngildi er til. Þar sem færsla hefur algenga skammstöfun er hún
sýnd innan sviga. Skilgreiningar eru viljandi hnitmiðaðar. Líttu í viðkomandi
kafla fyrir ítarlegri umfjöllun.

## A

**[ABAC (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control)** (aðgangsstýring byggð á eigindum): Heimildarlíkan sem veitir aðgang út frá metnum eigindum notanda, auðlindar, aðgerðar og umhverfis (til dæmis deild, öryggisheimild, tími dags) frekar en föstum hlutverkum. Það býður fínkorna, stefnudrifna stjórn á kostnað meiri flækju en RBAC.

**[Accessibility (a11y)](https://en.wikipedia.org/wiki/Computer_accessibility)** (aðgengi): Sú venja að hanna og smíða hugbúnað þannig að fólk með fötlun geti skynjað hann, skilið, rötað um hann og átt samskipti við hann. Tölustafaskammstöfunin „a11y“ stytir 11 stafina milli „a“ og „y.“

**ADR (Architecture Decision Record)** (arkitektúrákvörðunarskrá): Stutt, útgáfustýrt skjal sem fangar eina mikilvæga arkitektúr- eða tækniákvörðun, samhengi hennar, kostina sem voru íhugaðir og afleiðingar hennar. ADR skapa endingargóða, rýnanlega sögu um hvers vegna kerfi er eins og það er.

**Aggregate** (samstæða): Í Domain-Driven Design þyrping lénshluta sem er meðhöndluð sem ein eining fyrir gagnabreytingar, þar sem einn hlutur starfar sem rót samstæðunnar og framfylgir óbreytum. Samstæður skilgreina samræmis- og færslumörk.

**[API (Application Programming Interface)](https://en.wikipedia.org/wiki/API)** (forritunarviðmót): Skilgreindur samningur sem einn hugbúnaðarhluti notar til að biðja um þjónustu eða gögn frá öðrum. Vel hönnuð API fela útfærsluatriði og veita stöðug, útgáfustýrð viðmót.

**API-first** (API fyrst): Þróunaraðferð þar sem API-samningurinn er hannaður og samþykktur fyrir útfærslu, svo notendur og veitendur geti unnið samhliða gegn sameiginlegri forskrift.

**arc42**: Opin, sniðmátsbyggð uppbygging til að skjalfesta hugbúnaðararkitektúr, skipulögð í tólf hluta sem ná yfir samhengi, skorður, byggingareiningar, keyrslutíma, útsetningu og ákvarðanir.

**[ARIA (Accessible Rich Internet Applications)](https://en.wikipedia.org/wiki/WAI-ARIA)**: W3C-forskrift sem skilgreinir hlutverk, ástönd og eiginleika sem gera kvika og sérsniðna vefíhluti skiljanlega hjálpartækni eins og skjálesurum.

**ASR (Architecturally Significant Requirement)** (arkitektúrmikilvæg krafa): Krafa sem hefur mælanleg, víðtæk áhrif á arkitektúr, svo sem afkasta-, aðgengis-, öryggis- eða regluverksskorða. ASR knýja afdrifaríkustu hönnunarákvarðanirnar.

**ASVS (Application Security Verification Standard)**: OWASP-staðall sem veitir flokkaðan gátlista öryggiskrafna og prófana til að hanna, smíða og staðfesta örugg forrit.

**[Autoscaling](https://en.wikipedia.org/wiki/Autoscaling)** (sjálfskölun): Sjálfvirk stilling á fjölda keyrandi reikntilvika (eða stærð þeirra) til að bregðast við álagi, svo afkastageta fylgi eftirspurn án handvirkrar íhlutunar. Hún er viðbót við yfirvegaða afkastagetuáætlun, en kemur ekki í staðinn fyrir hana.

**[Availability](https://en.wikipedia.org/wiki/Availability)** (aðgengi, rekstrartími): Hlutfall tímans sem kerfi er í rekstri og getur afgreitt beiðnir, oft sett fram í „nínum“ (til dæmis 99,9%). Það er kjarnaáreiðanleikamarkmið fest í SLO og SLA.

## B

**Backpressure** (bakþrýstingur): Flæðistýringarbúnaður þar sem íhlutur undir álagi gefur framleiðendum uppstreymis merki um að hægja á sér, sem kemur í veg fyrir ótakmarkaðar biðraðir og dómínóbilun. Hann er miðlægur í áreiðanlegum straumkerfum og skilaboðadrifnum kerfum.

**[BDD (Behaviour-Driven Development)](https://en.wikipedia.org/wiki/Behavior-driven_development)** (hegðunardrifin þróun): Samvinnuvenja sem setur kröfur fram sem áþreifanleg, mannlæsileg dæmi um hegðun (oft á Given/When/Then formi) sem þjóna einnig sem sjálfvirkar samþykktarprófanir.

**BFF (Backend for Frontend)** (bakendi fyrir framenda): Arkitektúrmynstur þar sem sérstök bakendaþjónusta er smíðuð fyrir tiltekinn framenda eða biðlaragerð, sem sníður gagnamótun og samantekt að þörfum þess biðlara.

**[BI (Business Intelligence)](https://en.wikipedia.org/wiki/Business_intelligence)** (viðskiptagreind): Verkfærin, ferlin og venjurnar til að safna, samþætta og greina viðskiptagögn til að styðja skýrslugjöf, mælaborð og ákvarðanatöku.

**Blameless postmortem** (eftirmálsrýni án sakbendingar): Atvikarýni sem beinist að kerfislægum orsökum og námi frekar en sök einstaklinga, á þeirri forsendu að fólk hegði sér skynsamlega miðað við upplýsingarnar og hvatana sem það hafði.

**[Blue-green deployment](https://en.wikipedia.org/wiki/Blue-green_deployment)** (blár-grænn útsetning): Útgáfuaðferð sem rekur tvö eins framleiðsluumhverfi („blátt“ og „grænt“), beinir umferð að öðru á meðan hitt er uppfært, sem gerir nánast samstundis skiptingu og afturköllun mögulega.

**[BM25](https://en.wikipedia.org/wiki/Okapi_BM25)**: Víða notað röðunarfall fyrir textaleit sem metur hve vel skjal passar fyrirspurn með tíðni orða, andhverfri skjalatíðni og lengd skjals. Það er sjálfgefin orðaröðun í mörgum leitarvélum.

**Bounded context** (afmarkað samhengi): Í Domain-Driven Design skýr mörk innan sem tiltekið lénslíkan og alltumlykjandi tungumál þess gilda samræmt. Það kemur í veg fyrir að hugtök blandist milli ólíkra hluta stórs kerfis.

**Build cache** (smíðaskyndiminni): Geymsla áður reiknaðra smíðaúttaka, lykluð með inntökunum sem framleiddu þau, svo óbreytt vinna sé endurnýtt frekar en endursmíðuð. Sameiginlegt fjarlægt smíðaskyndiminni leyfir heilu teymi og CI þess að endurnýta niðurstöður hvers annars.

**[Bus factor](https://en.wikipedia.org/wiki/Bus_factor)** (rútufaktor): Fjöldi fólks sem þyrfti að tapast (myndlíkingin „keyrð yfir af rútu“) áður en verkefni stöðvast vegna skorts á nauðsynlegri þekkingu. Lágur rútufaktor gefur til kynna samþjappaða, óskjalfesta sérfræðiþekkingu og skipulagsáhættu.

## C

**[Cache eviction policy](https://en.wikipedia.org/wiki/Cache_replacement_policies)** (útskúfunarstefna skyndiminnis): Reglan sem skyndiminni notar til að ákveða hvaða færslu á að fjarlægja þegar það er fullt, svo sem síst nýlega notað (LRU) eða sjaldnast notað (LFU). Stefnan mótar nýtingarhlutfall og þar með gildi skyndiminnisins.

**[Cache invalidation](https://en.wikipedia.org/wiki/Cache_invalidation)** (ógilding skyndiminnis): Vandinn að fjarlægja eða uppfæra skyndigögn þegar undirliggjandi uppspretta breytist, svo lesendur sjái ekki úrelt gildi. Hann er frægur sem eitt erfiðasta vandamál tölvunarfræði.

**[Cache stampede](https://en.wikipedia.org/wiki/Cache_stampede)** (skyndiminnisstormur): Bilunarháttur þar sem margir biðlarar missa af skyndiminni fyrir sama lykil samtímis og berja allir á upprunann saman, sem yfirbugar hann. Beiðnasamruni og dreifð fyrning koma í veg fyrir hann. Einnig kallað thundering herd.

**Canary release** (kanarí-útgáfa): Útsetningartækni sem útsetur nýja útgáfu fyrir litlu hlutmengi notenda eða umferðar fyrst, vaktar fyrir vandamálum og víkkar síðan útgáfuna stigvaxandi ef mælikvarðar haldast heilbrigðir.

**[CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem)** (CAP-setningin): Regla sem segir að dreift gagnaver geti tryggt í mesta lagi tvennt af Consistency (samræmi), Availability (aðgengi) og Partition tolerance (skiptingarþol) samtímis. Því skiptingar eru óumflýjanlegar vega hönnuðir í raun samræmi gegn aðgengi meðan á þeim stendur.

**[C4 model](https://en.wikipedia.org/wiki/C4_model)** (C4-líkanið): Létt aðferð til að sjóngera hugbúnaðararkitektúr á fjórum óhlutstigum: System Context, Containers, Components og Code.

**[CD (Continuous Delivery / Continuous Deployment)](https://en.wikipedia.org/wiki/Continuous_delivery)** (samfelld afhending / samfelld útsetning): Samfelld afhending heldur hugbúnaði í útgáfuhæfu ástandi svo hægt sé að útsetja hann hvenær sem er með handvirkri samþykkt. Samfelld útsetning gefur sjálfvirkt út hverja breytingu sem stenst leiðsluna.

**[CDN (Content Delivery Network)](https://en.wikipedia.org/wiki/Content_delivery_network)** (efnisdreifinet): Landfræðilega dreift net jaðarþjóna sem geyma og afgreiða efni nálægt notendum, sem dregur úr töf og léttir á upprunainnviðum.

**Chain-of-thought prompting** (hugsanakeðjuprompt): Prompttækni sem biður tungumálslíkan að vinna sig gegnum millirökhugsunarskref áður en það gefur lokasvar, sem bætir frammistöðu á fjölþrepa vandamálum á kostnað lengri, hægari úttaks.

**[CI (Continuous Integration)](https://en.wikipedia.org/wiki/Continuous_integration)** (samfelld samþætting): Sú venja að sameina breytingar forritara oft í sameiginlega aðallínu, þar sem hver sameining er staðfest með sjálfvirkri smíði og prófasafni til að greina samþættingarvandamál snemma.

**[CI/CD](https://en.wikipedia.org/wiki/CI/CD)**: Sameinaða leiðslan fyrir samfellda samþættingu og samfellda afhendingu/útsetningu sem sjálfvirknivæðir smíði, prófanir og útgáfu hugbúnaðar.

**CMMC (Cybersecurity Maturity Model Certification)**: Áætlun bandaríska varnarmálaráðuneytisins sem vottar netöryggisþroska verktaka sem meðhöndla alríkissamningsupplýsingar og stýrðar óleynilegar upplýsingar.

**[Cohesion](https://en.wikipedia.org/wiki/Cohesion_(computer_science))** (samheldni): Mælikvarðinn á hve vel þættirnir inni í einingu eiga saman og þjóna einum, vel skilgreindum tilgangi. Mikil samheldni, pöruð við litla tengingu, er aðalsmerki viðhaldanlegrar hönnunar.

**Context window** (samhengisgluggi): Hámarksmagn texta, mælt í tókum, sem tungumálslíkan getur tekið til greina í einu, yfir inntak og úttak. Hann er knappt fjárhagsáætlun sem prompt- og samhengishönnun verður að stýra yfirvegað.

**[Conway's Law](https://en.wikipedia.org/wiki/Conway's_law)** (lögmál Conways): Sú athugun að bygging kerfis hneigist til að spegla samskiptabyggingu skipulagsheildarinnar sem smíðar það. „Öfuga Conway-hreyfingin“ mótar teymi viljandi til að framleiða æskilegan arkitektúr.

**Core Web Vitals**: Safn notendamiðaðra vefafkastamælikvarða skilgreint af Google (svo sem Largest Contentful Paint, Interaction to Next Paint og Cumulative Layout Shift) sem mæla hleðslu, gagnvirkni og sjónrænan stöðugleika.

**[Cost of delay](https://en.wikipedia.org/wiki/Cost_of_delay)** (kostnaður seinkunar): Hagfræðilegi kostnaðurinn af því að hafa ekki eitthvað tilbúið enn, settur fram sem glatað verðmæti á tímaeiningu. Að gera hann skýran breytir forgangsröðun úr skoðun í reikning og styður röðunarreglur eins og vegna stystu-vinnu-fyrst.

**[Coupling](https://en.wikipedia.org/wiki/Coupling_(computer_programming))** (tenging): Mælikvarðinn á innbyrðis ósjálfstæði eininga eða þjónusta. Lítil tenging takmarkar gárandi áhrif breytinga og er miðlægt markmið góðs arkitektúrs.

**CQRS (Command Query Responsibility Segregation)** (aðgreining skipana- og fyrirspurnaábyrgðar): Mynstur sem aðgreinir líkanið sem notað er til að breyta ástandi (skipanir) frá líkaninu sem notað er til að lesa ástand (fyrirspurnir), sem leyfir hvoru að vera fínstillt og skalað óháð.

**[CVE (Common Vulnerabilities and Exposures)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)**: Opinber skrá yfir birta öryggisveikleika, hver með einkvæmt auðkenni svo verkfæri og teymi geti vísað til sama galla ótvírætt.

**CWV**: Sjá Core Web Vitals.

## D

**[DAST (Dynamic Application Security Testing)](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)** (kvik öryggisprófun forrita): Öryggisprófun sem kannar keyrandi forrit utan frá, án aðgangs að frumkóða, til að finna veikleika sem birtast á keyrslutíma.

**Data-ink ratio** (gagnableksshlutfall): Meginregla frá Edward Tufte sem segir að rit ætti að eyða mestu bleki sínu í gögnin sjálf og litlu í skraut, með því að fjarlægja hnitanet, ramma og ruslrit sem upplýsa ekki.

**[Data mesh](https://en.wikipedia.org/wiki/Data_mesh)** (gagnavefur): Valddreifður gagnaarkitektúr og rekstrarlíkan sem lítur á gögn sem vöru í eigu lénsteyma, studd af sjálfsafgreiðsluvettvangsinnviðum og samtaka stjórnarháttum.

**[Data visualisation](https://en.wikipedia.org/wiki/Data_and_information_visualization)** (gagnasýn): Sú venja að kóða gögn í sjónrænt form (staðsetningu, lengd, lit og þess háttar) svo mynstur, samanburður og þróun verði skynjanleg og ákvarðanir betur upplýstar.

**[DDD (Domain-Driven Design)](https://en.wikipedia.org/wiki/Domain-driven_design)** (lénsdrifin hönnun): Nálgun á hugbúnaðarhönnun sem miðar líkanið á viðskiptalénið, með sameiginlegu alltumlykjandi tungumáli, afmörkuðum samhengjum og byggingareiningum eins og hlutum, gildishlutum og samstæðum.

**Design tokens** (hönnunartók): Nefnd, vettvangshlutlaus gildi (litir, bil, leturgerð og þess háttar) sem kóða hönnunarákvarðanir svo hægt sé að deila þeim samræmt yfir hönnunarkerfi og margar vörur.

**DevEx / DevX (Developer Experience)** (upplifun forritara): Heildargæði daglegra samskipta forritara við verkfæri, vettvanga og ferli, sem nær yfir núning, endurgjafarhraða og hugræna byrði.

**[DevOps](https://en.wikipedia.org/wiki/DevOps)**: Menning og safn venja sem sameina hugbúnaðarþróun og rekstur til að stytta afhendingarlotur, auka útsetningartíðni og bæta áreiðanleika gegnum sjálfvirkni og sameiginlegt eignarhald.

**DORA (DevOps Research and Assessment)**: Rannsóknaráætlun og fjórir víða notaðir afhendingarmælikvarðar hennar (útsetningartíðni, leiðtími breytinga, bilunarhlutfall breytinga og tími til að endurheimta þjónustu) notaðir til að bera saman frammistöðu hugbúnaðarafhendingar.

**DPIA (Data Protection Impact Assessment)** (persónuverndarmat): Skipulagt mat, krafist samkvæmt GDPR fyrir áhættusama vinnslu, sem greinir og dregur úr persónuverndaráhættu áður en verkefni heldur áfram.

**Drift (configuration)** (rek (stillinga)): Hægfara frávik raunverulegs ástands kerfis frá yfirlýstu eða ætluðu ástandi þess, algengt af völdum handvirkra breytinga. Innviðir sem kóði og GitOps stefna að því að greina og leiðrétta það.

**Drift (model)** (rek (líkans)): Í vélnámi, hnignun líkansframmistöðu með tímanum þegar tölfræðilegir eiginleikar inntaksgagna (gagnarek) eða sambandið sem er líkanað (hugtakarek) breytast.

**[DR (Disaster Recovery)](https://en.wikipedia.org/wiki/Disaster_recovery)** (hamfarabati): Stefnan, verklagið og innviðirnir til að endurheimta þjónustu og gögn eftir meiriháttar truflandi atburð, yfirleitt stýrt af RTO- og RPO-markmiðum.

**[DRY (Don't Repeat Yourself)](https://en.wikipedia.org/wiki/Don't_repeat_yourself)** (endurtaktu þig ekki): Hönnunarregla sem segir að hver þekkingarbútur skuli hafa eina, yfirvalds framsetningu, sem dregur úr tvítekningu og hættu á ósamræmdum uppfærslum.

## E

**East-west traffic** (austur-vestur umferð): Netumferð milli þjónusta innan kerfis eða gagnavers, öfugt við norður-suður umferð milli kerfisins og ytri biðlara. Þjónustuvefur stýrir yfirleitt austur-vestur umferð.

**[Edge computing](https://en.wikipedia.org/wiki/Edge_computing)** (jaðarútreikningur): Að keyra útreikning og geymslu nálægt þar sem gögn eru framleidd eða notuð frekar en á miðlægum stað, til að skera töf og bandvídd. Efnisdreifinet eru snemmbúið, útbreitt form.

**[Elasticity](https://en.wikipedia.org/wiki/Elasticity_(cloud_computing))** (teygjanleiki): Geta kerfis til að afla og sleppa auðlindum sjálfvirkt til að bregðast við breytilegri eftirspurn, svo afkastageta fylgi álagi náið.

**[ELT (Extract, Load, Transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform)**: Gagnasamþættingarmynstur sem hleður hrágögnum í markgeymslu fyrst og umbreytir þeim þar, með því að nýta stærð nútíma vöruhúsa og vatnshúsa.

**[Embedding](https://en.wikipedia.org/wiki/Word_embedding)** (vigurinnfelling): Framsetning texta, mynda eða annarra gagna sem þéttur tölulegur vigur, staðsettur svo svipuð atriði sitja nærri hvort öðru. Innfellingar knýja merkingarleit og vigurleit og endurheimtuaukinni framleiðslu.

**[EN 301 549](https://en.wikipedia.org/wiki/EN_301_549)**: Evrópski staðallinn sem tilgreinir aðgengiskröfur fyrir upplýsingatæknivörur og -þjónustu, vísað til í innkaupum hins opinbera um allt ESB og samstilltur WCAG.

**Error budget** (villufjárhagsáætlun): Leyfða magn óáreiðanleika samkvæmt SLO yfir tímabil. Þegar það er uppurið forgangsraða teymi áreiðanleikavinnu fram yfir nýja eiginleika. Hún sættir spennuna milli hraða og stöðugleika.

**[ETL (Extract, Transform, Load)](https://en.wikipedia.org/wiki/Extract,_transform,_load)**: Gagnasamþættingarmynstur sem dregur gögn úr uppsprettum, umbreytir þeim í markform og hleður þeim í áfangastað eins og vöruhús.

**[EU AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act)** (gervigreindarlög ESB): Reglugerð Evrópusambandsins sem flokkar gervigreindarkerfi eftir áhættu og leggur samsvarandi skyldur á, bannar tiltekna notkun og regluverkar áhættusöm kerfi mikið.

**[Eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency)** (endanlegt samræmi): Samræmislíkan í dreifðum kerfum þar sem afrit geta tímabundið vikið en renna saman í sama ástand þegar uppfærslur hætta að berast.

## F

**[Feature flag / feature toggle](https://en.wikipedia.org/wiki/Feature_toggle)** (eiginleikarofi): Búnaður til að kveikja eða slökkva á virkni á keyrslutíma án endurútsetningar, notaður fyrir stigvaxandi útgáfur, tilraunir og rekstrarstjórn.

**Feature store** (eiginleikageymsla): Miðlægt kerfi til að skilgreina, geyma og afgreiða sérvalda vélnámseiginleika samræmt bæði fyrir þjálfun og ályktun, sem dregur úr tvítekningu og skekkju milli þjálfunar og afgreiðslu.

**[FedRAMP (Federal Risk and Authorisation Management Program)](https://en.wikipedia.org/wiki/FedRAMP)**: Áætlun bandarískra stjórnvalda sem staðlar öryggismat, heimildarveitingu og samfellda vöktun fyrir skýjaþjónustur notaðar af alríkisstofnunum.

**Few-shot prompting** (prompt með fáum dæmum): Að veita tungumálslíkani handfylli unninna dæma í promptinu til að sýna æskilegt verk og úttakssnið, öfugt við zero-shot prompt, sem gefur leiðbeiningar án dæma.

**FinOps** (fjármálarekstur skýs): Agi og menningarvenja sem færir fjárhagslega ábyrgð á breytileg skýjaútgjöld og gefur verkfræði-, fjármála- og viðskiptateymum sameiginlegt eignarhald á kostnaði og verðmæti.

**[FISMA (Federal Information Security Modernisation Act)](https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act)**: Bandarísk löggjöf sem krefst þess að alríkisstofnanir innleiði, skjalfesti og vakti upplýsingaöryggisáætlanir, framkvæmd að mestu gegnum leiðsögn NIST.

**Flow efficiency** (flæðishagkvæmni): Hlutfall heildarleiðtíma sem vinnuatriði ver í að vera virkt unnið frekar en að bíða, reiknað sem virðisaukatími deilt með heildarleiðtíma. Flest kerfi eru furðu lág, oft undir 15 prósentum.

**Four-eyes principle** (fjögurra augna reglan): Stýring sem krefst þess að mikilvæg aðgerð sé rýnd eða samþykkt af að minnsta kosti tveimur manneskjum, sem dregur úr hættu á villu eða misferli.

**[Fuzz testing (fuzzing)](https://en.wikipedia.org/wiki/Fuzzing)** (ruglprófun): Sjálfvirk prófunartækni sem matar forrit á afbrigðilegu, handahófskenndu eða óvæntu inntaki til að afhjúpa hrun, öryggisgalla og jaðartilfellagalla.

## G

**[GDPR (General Data Protection Regulation)](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)** (persónuverndarreglugerðin): Reglugerð Evrópusambandsins sem stýrir vinnslu persónuupplýsinga, veitir einstaklingum réttindi og leggur skyldur á ábyrgðaraðila og vinnsluaðila, með miklum viðurlögum fyrir vanfylgni.

**GitOps**: Rekstrarlíkan sem notar Git sem einu sannleiksuppsprettu fyrir yfirlýsandi innviði og forrit, þar sem sjálfvirkni jafnar lifandi kerfi stöðugt við innsent ástand.

**Golden path / paved road** (gullin slóð / troðin slóð): Vel studd, ákveðin sjálfgefin leið til að smíða og senda hugbúnað innan skipulagsheildar, hönnuð til að gera örugga, samræmda, áreiðanlega valið auðveldasta.

**Golden record** (gullskrá): Í stofngagnastjórnun, einstaka, sætta, yfirvalds útgáfan af viðskiptahlut (svo sem viðskiptavini) sett saman úr mörgum upprunakerfum gegnum pörunar- og lifunarreglur.

**[Gradual typing](https://en.wikipedia.org/wiki/Gradual_typing)** (stigvaxandi tegundun): Tegundakerfisnálgun sem leyfir stöðugum og kviku tegundum að sambúa í einum kóðagrunni, svo hægt sé að bæta við tegundum stigvaxandi við kvikt tegundað forrit. Tegundaábendingar og valkvæðir tegundaathugarar eru algeng dæmi.

**[GraphQL](https://en.wikipedia.org/wiki/GraphQL)**: Fyrirspurnarmál og keyrsluumhverfi fyrir API sem leyfir biðlurum að biðja um nákvæmlega þau gögn sem þeir þurfa í einu kalli, með sterkt tegundað skema.

**[gRPC](https://en.wikipedia.org/wiki/gRPC)**: Hraðvirkt, samningsfyrst fjarkallarammaverk sem notar HTTP/2 og, venjulega, Protocol Buffers fyrir skilvirk samskipti milli þjónusta.

## H

**Hermetic build** (hermetísk smíði): Smíði sem veltur aðeins á skýrt yfirlýstum inntökum og er einangruð frá hýsilumhverfinu, svo hún framleiðir sama úttak hvar sem er. Hermetík er grunnur endurtakanlegra smíða og áreiðanlegs skyndiminnis.

**[HSM (Hardware Security Module)](https://en.wikipedia.org/wiki/Hardware_security_module)** (vélbúnaðaröryggiseining): Innsiglisheld vélbúnaðareining sem býr til, geymir og notar dulritunarlykla, sem veitir sterkari lyklavernd en eingöngu hugbúnaðarlausnir.

**[HIPAA (Health Insurance Portability and Accountability Act)](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)**: Bandarísk löggjöf sem, meðal annars, setur kröfur um verndun varinna heilbrigðisupplýsinga (PHI) og stýrir notkun þeirra og birtingu.

**Horizontal scaling** (lárétt skölun): Að auka afkastagetu með því að bæta við fleiri tilvikum eða hnútum („að skala út“) frekar en að gera stakan hnút öflugri. Hún undirstrikar flest stór, seigluð arkitektúr.

## I

**[IaC (Infrastructure as Code)](https://en.wikipedia.org/wiki/Infrastructure_as_code)** (innviðir sem kóði): Sú venja að skilgreina og útvega innviði gegnum vélalæsilega, útgáfustýrða stillingu frekar en handvirk ferli, sem gerir endurtakanleika og rýni mögulega.

**[IAM (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_management)** (auðkenna- og aðgangsstýring): Rammaverk stefna og tækni sem tryggir að réttu auðkennin hafi réttan aðgang að réttu auðlindunum á réttum tímum.

**IDP / IdP**: „IDP“ táknar almennt Internal Developer Platform (innri forritaravettvang), sjálfsafgreiðsluverkfærislagið sem dregur innviði saman fyrir vöruteymi. „IdP“ táknar Identity Provider (auðkennaveitu), þjónustu sem auðkennir notendur og gefur út fullyrðingar. Samhengi aðgreinir þau tvö.

**[Idempotency](https://en.wikipedia.org/wiki/Idempotence)** (eins-áhrifa): Eiginleiki þar sem að framkvæma aðgerð oft hefur sömu áhrif og að framkvæma hana einu sinni, nauðsynlegur fyrir örugga endurtilraun í dreifðum kerfum og API.

**[i18n (Internationalisation)](https://en.wikipedia.org/wiki/Internationalization_and_localization)** (alþjóðavæðing): Að hanna og smíða hugbúnað svo hægt sé að laga hann að ólíkum tungumálum, svæðum og menningarvenjum án verkfræðibreytinga. Tölustafaskammstöfunin stytir 18 stafina milli „i“ og „n.“

**Immutable artefact** (óbreytanleg afurð): Smíðaúttak sem, eftir að það er framleitt og útgáfumerkt, er aldrei breytt. Hver breyting skilar nýrri útgáfu. Óbreytanleiki gerir útgáfur endurtakanlegar og leyfir þér að smíða einu sinni og kynna sömu afurð yfir umhverfi.

**InnerSource**: Beiting opinna þróunarvenja (gagnsæis, sameiginlegra geymslna og þverteymisframlags) innan einnar skipulagsheildar.

**IaC drift**: Sjá Drift (configuration).

**[Inverted index](https://en.wikipedia.org/wiki/Inverted_index)** (andhverf vísitala): Kjarnagagnabygging leitarvélar, sem varpar hverju orði á listann yfir skjöl sem innihalda það, svo hægt sé að svara fyrirspurnum án þess að skanna hvert skjal.

**[ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001)**: Alþjóðlegur staðall sem tilgreinir kröfur fyrir upplýsingaöryggisstjórnunarkerfi (ISMS), sem veitir vottanlegt rammaverk til að stýra upplýsingaöryggisáhættu.

**ISO/IEC 42001**: Alþjóðlegur staðall sem tilgreinir kröfur fyrir gervigreindarstjórnunarkerfi, sem gefur skipulagsheildum vottanlegt rammaverk til að stýra þróun og notkun gervigreindar á ábyrgan hátt.

## J

**[JWT (JSON Web Token)](https://en.wikipedia.org/wiki/JSON_Web_Token)**: Samþjappað, undirritað (og valkvæmt dulkóðað) tókasnið notað til að bera fullyrðingar milli aðila, algengt fyrir auðkenningu og heimild í vef- og API-kerfum.

## K

**[Kanban](https://en.wikipedia.org/wiki/Kanban_(development))**: Straumlínuvinnuflæðisaðferð sem sjónræðir vinnu á borði, takmarkar vinnu í gangi og stýrir flæði til að bæta afköst og fyrirsjáanleika.

**[KISS (Keep It Simple, Stupid)](https://en.wikipedia.org/wiki/KISS_principle)** (hafðu það einfalt): Hönnunarregla sem kýs einföldustu lausnina sem mætir þörfinni, á þeim forsendum að óþörf flækja auki kostnað og áhættu.

**KMS (Key Management Service)** (lyklastjórnunarþjónusta): Kerfi til að búa til, geyma, snúa og stýra aðgangi að dulritunarlyklum, oft studd af vélbúnaðaröryggiseiningum.

**[KPI (Key Performance Indicator)](https://en.wikipedia.org/wiki/Performance_indicator)** (lykilárangursvísir): Magngreinanlegur mælikvarði notaður til að rekja framvindu í átt að tilteknu viðskipta- eða rekstrarmarkmiði.

## L

**Lakehouse** (vatnshús): Gagnaarkitektúr sem sameinar ódýra, sveigjanlega geymslu gagnavatns við stjórnun, færslur og afkastaeiginleika gagnavöruhúss.

**[Lead time](https://en.wikipedia.org/wiki/Lead_time)** (leiðtími): Liðinn tími frá því að breyting er beðin um (eða innsend) þar til hún er afhent í framleiðslu. Kjarna DORA-afhendingarmælikvarði.

**[Least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)** (minnstu réttindi): Öryggisregla sem veitir hverjum notanda, ferli eða kerfi aðeins lágmarksaðganginn sem þarf til að sinna hlutverki sínu, sem takmarkar tjón af öryggisbroti eða villu.

**[Little's Law](https://en.wikipedia.org/wiki/Little's_law)** (lögmál Littles): Niðurstaða úr biðraðakenningu sem segir að meðalfjöldi atriða í stöðugu kerfi jafngildi meðalkomuhraða margfölduðum með meðaltíma sem hvert atriði ver í kerfinu. Það tengir vinnu í gangi, afköst og leiðtíma.

**[LLM (Large Language Model)](https://en.wikipedia.org/wiki/Large_language_model)** (stórt tungumálslíkan): Vélnámslíkan þjálfað á mjög stórum textasöfnum til að spá fyrir um og búa til tungumál, fært um verk eins og samantekt, þýðingu og kóðagerð.

**[l10n (Localisation)](https://en.wikipedia.org/wiki/Language_localisation)** (staðfærsla): Að laga alþjóðavæddan hugbúnað að tilteknu svæði, þar á meðal þýðingu, snið og menningarvenjur. Tölustafaskammstöfunin stytir 10 stafina milli „l“ og „n.“

## M

**[MDM (Master Data Management)](https://en.wikipedia.org/wiki/Master_data_management)** (stofngagnastjórnun): Agi og verkfæri til að búa til og viðhalda einstakri, yfirvalds, samræmdri sýn á kjarnaviðskiptahluti (svo sem viðskiptavini eða vörur) yfir kerfi.

**MITRE ATT&CK**: Sérvalinn, opinber þekkingargrunnur um raunverulega taktík og tækni andstæðinga, víða notaður til að skipuleggja rauðliðsæfingar, leiða greiningarverkfræði og lýsa ógnum á sameiginlegum orðaforða.

**Mean Time to Recovery (MTTR)** (meðaltími til endurheimtar): Meðaltíminn sem tekur að endurheimta þjónustu eftir bilun. Algengur áreiðanleika- og atvikastjórnunarmælikvarði.

**[Mob programming](https://en.wikipedia.org/wiki/Mob_programming)** (hópforritun): Venja þar sem heilt teymi vinnur saman að sama verki í sömu tölvu, skiptist á um hver skrifar, til að deila þekkingu og taka ákvarðanir sameiginlega.

**[MLOps (Machine Learning Operations)](https://en.wikipedia.org/wiki/MLOps)** (vélnámsrekstur): Safn venja sem útsetja, vakta og viðhalda vélnámslíkönum í framleiðslu áreiðanlega og skilvirkt, sem víkkar DevOps-meginreglur yfir vélnámslífsferilinn.

**[Monorepo](https://en.wikipedia.org/wiki/Monorepo)** (einsgeymsla): Ein útgáfustýringargeymsla sem heldur kóða margra verkefna eða allrar skipulagsheildarinnar, sem gerir sameiginleg verkfæri og óskiptanlegar þververkefnabreytingar mögulegar á kostnað sérhæfðra skölunarverkfæra.

**mTLS (mutual TLS)** (gagnkvæmt TLS): Stilling Transport Layer Security þar sem báðir aðilar leggja fram og staðfesta skírteini, svo hvor auðkennir hinn. Það er sjálfgefið fyrir umferð milli þjónusta í þjónustuvef og zero-trust netum. Sjá einnig [gagnkvæma auðkenningu](https://en.wikipedia.org/wiki/Mutual_authentication).

**[Mutation testing](https://en.wikipedia.org/wiki/Mutation_testing)** (stökkbreytingarprófun): Tækni sem kynnir viljandi smáar villur („stökkbreytingar“) í kóða til að athuga hvort prófasafnið greini þær, sem mælir raunverulega virkni safnsins.

## N

**[NDCG (Normalised Discounted Cumulative Gain)](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)**: Röðunargæðamælikvarði sem umbunar að setja mjög viðeigandi niðurstöður nærri toppi niðurstöðulista, staðlaður svo einkunnir séu samanburðarhæfar yfir fyrirspurnir. Hann er undirstaða mats á leitarviðeigni.

**[NIST (National Institute of Standards and Technology)](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)**: Bandarísk alríkisstofnun þar sem sérrit og rammaverk eru víða vísaðir staðlar fyrir netöryggi, persónuvernd og gervigreind.

**NIST AI RMF (AI Risk Management Framework)**: Valkvætt NIST-rammaverk til að bera kennsl á, meta og stýra áhættu tengdri gervigreindarkerfum yfir lífsferil þeirra, skipulagt í kringum aðgerðirnar Govern, Map, Measure og Manage.

**[NIST SP 800-53](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53)**: NIST-skrá yfir öryggis- og persónuverndarstýringar fyrir alríkisupplýsingakerfi, víða notuð sem grunnlína langt umfram ríkisgeirann.

**NIST SP 800-171**: NIST-rit sem tilgreinir kröfur um vernd stýrðra óleynilegra upplýsinga (CUI) í kerfum utan alríkis, miðlægt fyrir reglufylgni varnarmálaverktaka.

**[NFR (Non-Functional Requirement)](https://en.wikipedia.org/wiki/Non-functional_requirement)** (óvirk krafa): Krafa sem lýsir hvernig kerfi ætti að hegða sér (eiginleikum þess eins og afköstum, öryggi, áreiðanleika eða nothæfi) frekar en hvaða virkni það sinnir.

**North-south traffic** (norður-suður umferð): Netumferð milli kerfis og ytri biðlara þess (inn og út úr gagnaveri eða klasa), öfugt við austur-vestur umferð milli innri þjónusta. API-gátt stýrir yfirleitt norður-suður umferð.

## O

**Observability** (sýnileiki): Mælikvarðinn á hve vel innra ástand kerfis má álykta út frá ytri úttökum þess, yfirleitt náð gegnum fjarmælingar: mælikvarða, skrár og rakningar.

**[OKR (Objectives and Key Results)](https://en.wikipedia.org/wiki/OKR)** (markmið og lykilniðurstöður): Markmiðasetningarrammaverk sem parar eigindlegt markmið við fáar mælanlegar lykilniðurstöður til að samstilla og einbeita skipulagsheild.

**OpenTelemetry (OTel)**: Seljandahlutlaus, opinn staðall og verkfærasafn til að búa til, safna og flytja út fjarmælingagögn (rakningar, mælikvarða og skrár) úr hugbúnaði.

**OPA (Open Policy Agent)**: Opin, almenn stefnuvél sem metur stefnur (skrifaðar í Rego-málinu) til að framfylgja heimildar- og stillingarreglum yfir staflann, sem gerir stefnu-sem-kóða mögulega.

**OSPO (Open Source Program Office)** (skrifstofa opins hugbúnaðar): Skipulagshlutverk sem samhæfir stefnu, stjórnarhætti, reglufylgni og samfélagsþátttöku varðandi opinn hugbúnað og stýrir bæði notkun og framlagi.

**[OWASP (Open Worldwide Application Security Project)](https://en.wikipedia.org/wiki/OWASP)**: Sjálfseignarsamfélag sem framleiðir víða notuð, frjálst aðgengileg forritaöryggisgögn, þar á meðal OWASP Top Ten og ASVS.

## P

**[PACELC](https://en.wikipedia.org/wiki/PACELC_theorem)**: Útvíkkun á CAP-setningunni sem segir að ef Skipting (Partition) er til skiptir kerfi Aðgengi (Availability) á móti Samræmi (Consistency), Annars (Else, í venjulegum rekstri) skiptir það Töf (Latency) á móti Samræmi.

**[PCI DSS (Payment Card Industry Data Security Standard)](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)**: Öryggisstaðall viðhaldið af greiðslukortaiðnaðinum sem tilgreinir kröfur fyrir skipulagsheildir sem geyma, vinna eða senda korthafagögn.

**[Penetration testing](https://en.wikipedia.org/wiki/Penetration_test)** (innbrotsprófun): Heimiluð, hermd árás á kerfi af hæfum prófurum til að finna og sýna nýtanlega veikleika áður en raunverulegir árásaraðilar gera það, afhent sem forgangsraðaðar, framkvæmanlegar niðurstöður.

**[PII (Personally Identifiable Information)](https://en.wikipedia.org/wiki/Personal_data)** (persónugreinanlegar upplýsingar): Upplýsingar sem geta greint tiltekinn einstakling, annaðhvort einar eða sameinaðar öðrum gögnum. Meðhöndlun þeirra er stýrt af persónuverndarlögum og innri stefnu.

**Platform engineering** (vettvangsverkfræði): Agi að smíða og reka innri sjálfsafgreiðsluvettvanga og gullnar slóðir sem draga úr hugrænni byrði og flýta vöruteymum.

**POUR**: Fjórar leiðandi meginreglur Web Content Accessibility Guidelines: efni verður að vera Perceivable (skynjanlegt), Operable (nothæft), Understandable (skiljanlegt) og Robust (sterkt).

**Production readiness review** (framleiðsluviðbúnaðarrýni): Skipulögð athugun, keyrð áður en þjónusta fer í loftið eða tekur við bakvaktareignarhaldi, sem staðfestir að hún uppfylli staðla fyrir sýnileika, áreiðanleika, öryggi, keyrsluhandbækur og rekstrarstuðning.

**[Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering)** (promptverkfræði): Sú venja að hanna og fínpússa leiðbeiningar, samhengi og dæmi sem gefin eru tungumálslíkani til að fá áreiðanlegt, hágæða úttak, meðhöndluð sem útgáfustýrður, prófaður verkfræðiagi frekar en tilraun og villa.

**[Prompt injection](https://en.wikipedia.org/wiki/Prompt_injection)** (promptinnspýting): Árás þar sem smíðað inntak veldur því að tungumálslíkan hunsar ætlaðar leiðbeiningar sínar og fylgir leiðbeiningum árásaraðilans í staðinn, gervigreindartímabils hliðstæða innspýtingargalla. Hún er miðlæg öryggisáhætta LLM-forrita.

**Property-based testing** (eiginleikabyggð prófun): Prófunartækni sem athugar að yfirlýstir eiginleikar haldi yfir mörg sjálfvirkt mynduð inntök, frekar en að treysta aðeins á handvalin dæmi.

**Pull request (PR) / merge request (MR)** (beiðni um sameiningu): Fyrirhugað safn breytinga sent til rýni og umræðu áður en það er sameinað í sameiginlega grein, aðaleining kóðarýni í flestum vinnuflæðum.

**Purple team** (fjólublátt lið): Samvinnuæfing þar sem sóknar- (rauð) og varnar- (blá) öryggisteymi vinna saman í rauntíma, svo árásir og greiningarnar sem ætlað er að grípa þær séu stilltar gegn hvor annarri.

## Q

**Quality gate** (gæðahlið): Sjálfvirkur athugunarpunktur í leiðslu sem verður að standast (til dæmis að mæta þekju-, öryggis- eða afkastaþröskuldum) áður en breyting getur haldið áfram.

**[Quorum](https://en.wikipedia.org/wiki/Quorum_(distributed_computing))** (ályktunarbær fjöldi): Í dreifðum kerfum lágmarksfjöldi hnúta sem verða að vera sammála til að aðgerð (svo sem lestur eða skrif) teljist árangursrík, notaður til að viðhalda samræmi þrátt fyrir bilanir.

## R

**[RACI](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)**: Ábyrgðarúthlutunarlíkan sem merkir hvern þátttakanda í verki eða ákvörðun sem Responsible (framkvæmir), Accountable (ber ábyrgð), Consulted (ráðgjafi) eða Informed (upplýstur).

**[RAG (Retrieval-Augmented Generation)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)** (endurheimtuaukin framleiðsla): Tækni sem grundar úttak tungumálslíkans með því að sækja fyrst viðeigandi skjöl eða gögn og veita þau sem samhengi, sem bætir nákvæmni og dregur úr ofskynjun.

**[RBAC (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control)** (hlutverkabyggð aðgangsstýring): Heimildarlíkan sem úthlutar réttindum á hlutverk og hlutverkum á notendur, sem einfaldar umsjón með því að stýra aðgangi á hlutverkastigi.

**[Red team](https://en.wikipedia.org/wiki/Red_team)** (rauðliðar): Hópur sem hermir raunsæjan andstæðing, oft gegn heilli skipulagsheild og án viðvörunar til varnaraðila, til að prófa greiningu og viðbrögð frekar en bara að telja upp veikleika. Andstæða: blátt (varnar-) lið.

**[Reference data](https://en.wikipedia.org/wiki/Reference_data)** (tilvísunargögn): Stýrðir, hægt breytilegir kóðalistar og flokkanir notaðar til að flokka önnur gögn, svo sem landakóðar, gjaldmiðlar og stöðugildi. Að stýra þeim sem sameiginlegum, útgáfustýrðum orðaforða heldur kerfum samræmdum.

**Rego**: Yfirlýsandi stefnumálið sem Open Policy Agent notar til að setja fram reglur fyrir heimildar- og stillingarákvarðanir.

**[REST (Representational State Transfer)](https://en.wikipedia.org/wiki/REST)**: Arkitektúrstíll fyrir netforrit sem notar ástandslausar aðgerðir yfir HTTP á vistfangahæfum auðlindum, metinn fyrir einfaldleika og breið verkfæri.

**[Reverse proxy](https://en.wikipedia.org/wiki/Reverse_proxy)** (öfugur milliþjónn): Þjónn sem situr fyrir framan eina eða fleiri bakendaþjónustur og áframsendir beiðnir biðlara til þeirra, sem veitir yfirleitt TLS-lúkningu, álagsjöfnun, skyndiminni og einn inngangspunkt.

**[RFC (Request for Comments)](https://en.wikipedia.org/wiki/Request_for_Comments)** (beiðni um athugasemdir): Skrifleg tillaga send til endurgjafar fyrir mikilvæga tæknilega ákvörðun eða breytingu, sem ýtir undir gagnsæi og sameiginlegt eignarhald. (Hugtakið nefnir líka útgáfuröð internetstaðla.)

**[ROI (Return on Investment)](https://en.wikipedia.org/wiki/Return_on_investment)** (ávöxtun fjárfestingar): Mælikvarði á verðmæti fengið af fjárfestingu miðað við kostnað hennar, notaður til að réttlæta og forgangsraða verkfræði- og tækniákvörðunum.

**[RPA (Robotic Process Automation)](https://en.wikipedia.org/wiki/Robotic_process_automation)** (ferlisjálfvirkni með vélmennum): Hugbúnaðar„vélmenni“ sem sjálfvirknivæða endurtekin, reglubyggð verk með því að vinna með núverandi notendaviðmót og kerfi eins og manneskja myndi gera.

**RPO (Recovery Point Objective)** (endurheimtarpunktsmarkmið): Hámarks ásættanlegt gagnatap mælt í tíma (til dæmis „allt að fimm mínútur“), sem skilgreinir hve oft verður að vernda gögn.

**RTO (Recovery Time Objective)** (endurheimtartímamarkmið): Hámarks ásættanleg lengd til að endurheimta þjónustu eftir truflun, sem leiðir hönnun og fjárfestingu hamfarabata.

## S

**Saga**: Mynstur til að stýra gagnasamræmi milli þjónusta í dreifðri færslu með því að raða staðbundnum færslum og gefa út jöfnunaraðgerðir þegar þrep bilar.

**[SAFe (Scaled Agile Framework)](https://en.wikipedia.org/wiki/Scaled_agile_framework)**: Rammaverk til að beita lipurri og straumlínuvenjum yfir stór fyrirtæki, samhæfir mörg teymi. Metið fyrir byggingu og gagnrýnt fyrir mögulegan þunga.

**[SAST (Static Application Security Testing)](https://en.wikipedia.org/wiki/Static_application_security_testing)** (stöðug öryggisprófun forrita): Öryggisprófun sem greinir frumkóða, bætakóða eða tvíundarskrár án þess að keyra þær til að finna veikleika snemma í þróun.

**SBOM (Software Bill of Materials)** (hugbúnaðarefnisskrá): Formleg, vélalæsileg skrá yfir íhluti og ósjálfstæði í hugbúnaði, notuð til að stýra aðfangakeðju- og veikleikaáhættu.

**SCA (Software Composition Analysis)** (hugbúnaðarsamsetningargreining): Verkfæri sem bera kennsl á opna og þriðju aðila íhluti í kóðagrunni og flagga þekktum veikleikum og leyfisáhættu.

**[Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development))**: Lipurt rammaverk sem skipuleggur vinnu í fastlengdar lotur (spretti) með skilgreindum hlutverkum, atburðum og afurðum til að afhenda verðmætisáfanga.

**[Section 508](https://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)**: Bandarísk lög sem krefjast þess að alríkisstofnanir geri rafræna og upplýsingatækni sína aðgengilega fólki með fötlun, í reynd samstillt WCAG.

**Semantic search** (merkingarleit): Leit sem passar á merkingu frekar en nákvæm lykilorð, yfirleitt með því að bera saman innfellingar fyrirspurnar og skjala. Hún er oft sameinuð orðaleit í blendingsnálgun.

**[Service mesh](https://en.wikipedia.org/wiki/Service_mesh)** (þjónustuvefur): Sérstakt innviðalag, yfirleitt útfært með hliðarvögnum, sem sinnir samskiptamálum milli þjónusta eins og gagnkvæmu TLS, endurtilraunum, tímamörkum, umferðarskiptingu og sýnileika og heldur þeim utan forritskóða.

**Sidecar** (hliðarvagn): Hjálparferli eða gámur útsettur við hlið aðalforritstilviks til að veita stuðningsgetu (svo sem þjónustuvefsmilliþjón) án þess að breyta forritinu sjálfu.

**[SIEM (Security Information and Event Management)](https://en.wikipedia.org/wiki/Security_information_and_event_management)** (öryggisupplýsinga- og atburðastjórnun): Kerfi sem safnar saman og fylgnigreinir öryggisskrár og atburði yfir umhverfi til að gera greiningu, viðvaranir og rannsókn mögulega.

**[SLA (Service Level Agreement)](https://en.wikipedia.org/wiki/Service-level_agreement)** (þjónustustigssamningur): Formleg skuldbinding milli þjónustuveitanda og viðskiptavina hans sem tilgreinir væntanleg þjónustustig og afleiðingar þess að missa af þeim.

**SLI (Service Level Indicator)** (þjónustustigsvísir): Magnbundinn mælikvarði á einhvern þátt þjónustugæða, svo sem beiðnitöf eða villuhlutfall, sem nærir SLO.

**SLO (Service Level Objective)** (þjónustustigsmarkmið): Markgildi eða bil fyrir SLI sem skilgreinir æskilegt áreiðanleikastig og myndar grunn villufjárhagsáætlana.

**SLSA (Supply-chain Levels for Software Artifacts)**: Rammaverk stigskiptra öryggiskrafna til að bæta heilleika og uppruna hugbúnaðarafurða gegnum smíða- og útgáfuferlið.

**SOAR (Security Orchestration, Automation, and Response)**: Verkfæri og venjur sem sjálfvirknivæða og samhæfa öryggisrekstur, svo sem flokkunar- og viðbragðsleikjaáætlanir, til að bæta hraða og samræmi.

**SOC 2 (System and Organisation Controls 2)**: Úttektarrammaverk og skýrsla, byggð á AICPA Trust Services Criteria, sem metur stýringar þjónustuskipulagsheildar fyrir öryggi, aðgengi, vinnsluheilleika, trúnað og persónuvernd.

**[SOLID](https://en.wikipedia.org/wiki/SOLID)**: Fimm hlutbundnar hönnunarreglur (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation og Dependency Inversion) sem stuðla að viðhaldanlegum, sveigjanlegum kóða.

**[SOX (Sarbanes-Oxley Act)](https://en.wikipedia.org/wiki/Sarbanes-Oxley_Act)**: Bandarísk löggjöf sem setur kröfur um fjárhagsskýrslugjöf og innri stýringar í opinberum fyrirtækjum, með afleiðingum fyrir upplýsingatæknikerfin sem styðja fjárhagsgögn.

**SPACE**: Rammaverk til að mæla framleiðni forritara yfir fimm víddir: Satisfaction and well-being (ánægju og vellíðan), Performance (frammistöðu), Activity (virkni), Communication and collaboration (samskipti og samstarf) og Efficiency and flow (skilvirkni og flæði), sem varar við einmælikvarðamælingum.

**[SRE (Site Reliability Engineering)](https://en.wikipedia.org/wiki/Site_reliability_engineering)** (áreiðanleikaverkfræði): Agi sem beitir hugbúnaðarverkfræðinálgunum á rekstur, notar SLO, villufjárhagsáætlanir og sjálfvirkni til að reka áreiðanleg kerfi í stærð.

**SSDF (Secure Software Development Framework)**: Rammaverk NIST (SP 800-218) um háleitar öruggar þróunarvenjur, sem nær yfir að undirbúa skipulagsheildina, vernda hugbúnað, framleiða vel tryggðan hugbúnað og bregðast við veikleikum.

**[Static analysis](https://en.wikipedia.org/wiki/Static_program_analysis)** (stöðugreining): Að skoða frumkóða, bætakóða eða tvíundarskrár án þess að keyra þær til að finna galla, stílbrot og öryggisgalla, yfirleitt gegnum sniðgreina, tegundaathuga og sérhæfða greina tengda við ritilinn og leiðsluna.

**[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)**: Ógnarlíkanaflokkun sem flokkar ógnir sem Spoofing (gervi), Tampering (átroðning), Repudiation (afneitun), Information disclosure (upplýsingaleka), Denial of service (þjónustuneitun) og Elevation of privilege (réttindahækkun).

## T

**[TCO (Total Cost of Ownership)](https://en.wikipedia.org/wiki/Total_cost_of_ownership)** (heildareignarkostnaður): Fullur líftímakostnaður kerfis eða ákvörðunar, þar á meðal kaup, rekstur, viðhald og endanleg niðurlagning, ekki bara upphafsverð.

**[TDD (Test-Driven Development)](https://en.wikipedia.org/wiki/Test-driven_development)** (prófdrifin þróun): Venja að skrifa misheppnaða sjálfvirka prófun áður en kóðann sem lætur hana standast, endurbæta síðan, í stuttum endurteknum lotum til að knýja hönnun og tryggja þekju.

**[Technical debt](https://en.wikipedia.org/wiki/Technical_debt)** (tæknileg skuld): Gefinn framtíðarkostnaður af því að velja fljótlega lausn núna fram yfir betri sem tæki lengri tíma, sem verður að stýra yfirvegað frekar en safna ómeðvitað.

**TF-IDF (Term Frequency-Inverse Document Frequency)**: Klassískt vigtunarkerfi sem metur mikilvægi orðs fyrir skjal eftir því hve oft það birtist þar, vegið upp af því hve algengt það er yfir allt safnið. Það undirstrikar mikið af orðaleitarröðun.

**[Theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints)** (skorðukenningin): Stjórnunaraðferð sem heldur því fram að afköst kerfis séu takmörkuð af einum flöskuhálsi hverju sinni, svo umbótafyrirhöfn ætti að beinast að þeirri skorðu þar til hún færist annað.

**[Threat modelling](https://en.wikipedia.org/wiki/Threat_model)** (ógnarlíkanagerð): Skipulögð venja að bera kennsl á, telja upp og forgangsraða mögulegum ógnum við kerfi svo hægt sé að hanna varnir inn snemma.

**Toil** (leiðindavinna): Í SRE, handvirk, endurtekin, sjálfvirknivæðanleg rekstrarvinna sem skalast línulega með þjónustu og veitir ekkert varanlegt verðmæti. Að draga úr henni frelsar afkastagetu fyrir verkfræði.

**Trunk-based development** (stofnþróun): Frumkóðastýringarvenja þar sem forritarar samþætta litlar breytingar oft í eina sameiginlega grein, sem lágmarkar langlífar greinar og sameiningarsársauka.

**[Type inference](https://en.wikipedia.org/wiki/Type_inference)** (tegundaályktun): Málseiginleiki sem leiðir tegundir segða sjálfvirkt út og gefur mikið af öryggi stöðugrar tegundunar án þess að krefjast þess að hver tegund sé skrifuð út í höndunum.

**[Type system](https://en.wikipedia.org/wiki/Type_system)** (tegundakerfi): Safn reglna sem tungumál notar til að úthluta og athuga tegundir, sem grípur heila flokka villna áður en forritið keyrir og skjalfestir ásetning. Tegundakerfi ná frá kviku til stöðugs og frá veiku til sterks.

## U

**Ubiquitous language** (alltumlykjandi tungumál): Í Domain-Driven Design, sameiginlegur, nákvæmur orðaforði notaður samræmt af forriturum og lénssérfræðingum og endurspeglaður beint í kóðanum og líkönunum.

**[UAT (User Acceptance Testing)](https://en.wikipedia.org/wiki/Acceptance_testing)** (notendasamþykktarprófun): Prófun framkvæmd af notendum eða fulltrúum þeirra til að staðfesta að kerfi mæti viðskiptaþörfum áður en það er samþykkt til útgáfu.

**[UX / UI (User Experience / User Interface)](https://en.wikipedia.org/wiki/User_experience)** (notendaupplifun / notendaviðmót): Notendaupplifun eru heildargæði samskipta manneskju við vöru. Notendaviðmót er sértæka sjónræna og gagnvirka yfirborðið sem þau samskipti eiga sér stað gegnum.

## V

**[Value object](https://en.wikipedia.org/wiki/Value_object)** (gildishlutur): Í Domain-Driven Design, óbreytanlegur hlutur skilgreindur alfarið af eigindum sínum frekar en sérstakri auðkenningu, svo sem peningaupphæð eða dagsetningabil.

**[Value stream mapping](https://en.wikipedia.org/wiki/Value-stream_mapping)** (verðmætastraumskortlagning): Tækni til að teikna hvert þrep frá hugmynd til afhents verðmætis, sem aðgreinir virðisaukatíma frá biðtíma, svo flöskuhálsar, afhendingar og endurvinnslulykkjur verði sýnilegar og bætanlegar.

**[Vector database](https://en.wikipedia.org/wiki/Vector_database)** (vigurgagnagrunnur): Gagnageymsla fínstillt fyrir að skrá og leita í margvíðum innfellingarvigrum eftir líkindum, algengur burðarás merkingarleitar og endurheimtuauknir framleiðslu.

**Vertical scaling** (lóðrétt skölun): Að auka afkastagetu með því að gera stakan hnút öflugri („að skala upp“), sem er einfalt en að lokum afmarkað af stærstu tiltæku vél.

**[VCS (Version Control System)](https://en.wikipedia.org/wiki/Version_control)** (útgáfustýringarkerfi): Verkfæri, svo sem Git, sem skráir breytingar á skrám yfir tíma svo hægt sé að rýna sögu, viðhalda greinum og samhæfa vinnu.

**[Vulnerability scanning](https://en.wikipedia.org/wiki/Vulnerability_scanner)** (veikleikaskönnun): Sjálfvirk skoðun kerfa, gáma eða kóða gegn gagnagrunnum þekktra veikleika og rangstillinga. Hún er víð og ódýr og er viðbót við dýpt handvirkrar innbrotsprófunar.

## W

**[WCAG (Web Content Accessibility Guidelines)](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines)**: W3C-safn alþjóðlega viðurkenndra leiðbeininga, skipulagt í kringum POUR-meginreglurnar og samræmisstigin A, AA og AAA, til að gera vefefni aðgengilegt.

**Wardley map** (Wardley-kort): Sjónræn stefnutækni sem staðsetur getu eftir verðmæti hennar fyrir notendur og þróunarþroska, til að upplýsa smíða/kaupa og fjárfestingarákvarðanir.

**Work in progress (WIP) limit** (mörk á vinnu í gangi): Þak á hve mörg atriði mega vera á tilteknu þrepi vinnuflæðis í einu, kjarna Kanban-venja sem bætir flæði með því að afhjúpa flöskuhálsa og hemja aukakostnað of mikillar samhliða vinnu.

**WSJF (Weighted Shortest Job First)** (vegin stysta-vinna-fyrst): Forgangsröðunaraðferð sem raðar vinnu með því að deila kostnaði seinkunar hennar með áætluðum lengd, svo stystu, tímanæmustu, verðmætustu atriðin séu gerð fyrst.

## X

**[XSS (Cross-Site Scripting)](https://en.wikipedia.org/wiki/Cross-site_scripting)** (þverlénaskriftun): Vefveikleiki þar sem árásaraðili sprautar inn illgjörnum skriftum sem keyra í vöfrum annarra notenda, sem getur stolið gögnum eða rænt lotum.

## Y

**[YAGNI (You Aren't Gonna Need It)](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it)** (þú munt ekki þurfa á því að halda): Regla sem ráðleggur gegn því að smíða virkni á ágiskun, á þeim forsendum að fyrirséðar þarfir raungerist oft ekki og bæti við kostnaði og flækju.

## Z

**[Zero trust](https://en.wikipedia.org/wiki/Zero_trust_security_model)** (núlltraust): Öryggislíkan sem gerir ekki ráð fyrir óbeinu trausti byggðu á netstaðsetningu og staðfestir stöðugt hverja aðgangsbeiðni gegn auðkenni, tæki og samhengi, samkvæmt viðkvæðinu „treystu aldrei, staðfestu alltaf.“
