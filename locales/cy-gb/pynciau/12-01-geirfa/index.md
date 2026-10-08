# 12.1 Geirfa

Mae'r eirfa hon yn diffinio termau ac acronymau a ddefnyddir ledled y llawlyfr. Trefnir
y cofnodion yn nhrefn yr wyddor. Lle mae gan gofnod acronym cyffredin, dangosir ef mewn
cromfachau. Mae'r diffiniadau'n fwriadol gryno; ymgynghorwch â'r bennod berthnasol am
driniaeth lawnach.

## A

**[ABAC (Attribute-Based Access Control)](https://en.wikipedia.org/wiki/Attribute-based_access_control)**: Model awdurdodi sy'n rhoi mynediad yn seiliedig ar briodoleddau a werthusir o'r defnyddiwr, yr adnodd, y weithred, a'r amgylchedd (er enghraifft, adran, clirdrwydded, amser y dydd) yn hytrach na rolau sefydlog. Mae'n cynnig rheolaeth fanwl, wedi'i gyrru gan bolisi, ar draul mwy o gymhlethdod na RBAC.

**[Accessibility (a11y)](https://en.wikipedia.org/wiki/Computer_accessibility)**: Yr arfer o ddylunio ac adeiladu meddalwedd fel y gall pobl ag anableddau ei chanfod, ei deall, symud drwyddi, a rhyngweithio â hi. Mae'r rhifenw "a11y" yn talfyrru'r 11 llythyren rhwng "a" ac "y."

**ADR (Architecture Decision Record)**: Dogfen fer, wedi'i fersiynu, sy'n cofnodi un penderfyniad pensaernïol neu dechnegol arwyddocaol, ei gyd-destun, yr opsiynau a ystyriwyd, a'i ganlyniadau. Mae ADRs yn creu hanes parhaol, adolygadwy o pam mae system fel y mae.

**Aggregate**: Yn Domain-Driven Design, clwstwr o wrthrychau parth a drinnir fel un uned ar gyfer newidiadau data, gydag un endid yn gweithredu fel gwreiddyn yr agregyn sy'n gorfodi'r rheolau anghyfnewidiol (invariants). Mae agregynnau'n diffinio ffiniau cysondeb a thrafodiad.

**[API (Application Programming Interface)](https://en.wikipedia.org/wiki/API)**: Contract diffiniedig y mae un darn o feddalwedd yn ei ddefnyddio i ofyn am wasanaethau neu ddata gan un arall. Mae APIs wedi'u dylunio'n dda yn cuddio manylion gweithredu ac yn darparu rhyngwynebau sefydlog, wedi'u fersiynu.

**API-first**: Dull datblygu lle mae contract yr API yn cael ei ddylunio a'i gytuno cyn gweithredu, fel y gall defnyddwyr a darparwyr weithio ochr yn ochr yn erbyn manyleb a rennir.

**arc42**: Strwythur agored, seiliedig ar dempled, ar gyfer dogfennu pensaernïaeth meddalwedd, wedi'i drefnu'n ddeuddeg adran sy'n cwmpasu cyd-destun, cyfyngiadau, blociau adeiladu, amser rhedeg, defnyddio, a phenderfyniadau.

**[ARIA (Accessible Rich Internet Applications)](https://en.wikipedia.org/wiki/WAI-ARIA)**: Manyleb W3C sy'n diffinio rolau, cyflyrau, a phriodoleddau sy'n gwneud cydrannau gwe deinamig a chwsm yn ddealladwy i dechnolegau cynorthwyol fel darllenwyr sgrin.

**ASR (Architecturally Significant Requirement)**: Gofyniad sydd ag effaith fesuradwy, eang ar bensaernïaeth, megis cyfyngiad perfformiad, argaeledd, diogelwch, neu reoleiddiol. Mae ASRs yn gyrru'r penderfyniadau dylunio mwyaf o ganlyniad.

**ASVS (Application Security Verification Standard)**: Safon OWASP sy'n darparu rhestr wirio raddedig o ofynion a phrofion diogelwch ar gyfer dylunio, adeiladu, a gwirio cymwysiadau diogel.

**[Autoscaling](https://en.wikipedia.org/wiki/Autoscaling)**: Yr addasiad awtomatig o nifer yr enghreifftiau cyfrifiadurol sy'n rhedeg (neu eu maint) mewn ymateb i lwyth, fel bod capasiti'n dilyn y galw heb ymyrraeth â llaw. Mae'n ategu, ond nid yn disodli, gynllunio capasiti bwriadol.

**[Availability](https://en.wikipedia.org/wiki/Availability)**: Y gyfran o amser y mae system yn weithredol ac yn gallu gwasanaethu ceisiadau, a fynegir yn aml mewn "naw" (er enghraifft, 99.9%). Mae'n darged dibynadwyedd craidd a godeiddir mewn SLOs ac SLAs.

## B

**Backpressure**: Mecanwaith rheoli llif lle mae cydran dan lwyth yn arwyddo i gynhyrchwyr uwch-lif arafu, gan atal ciwiau diderfyn a methiant rhaeadrol. Mae'n ganolog i systemau ffrydio a gyrrir gan negeseuon dibynadwy.

**[BDD (Behavior-Driven Development)](https://en.wikipedia.org/wiki/Behavior-driven_development)**: Arfer cydweithredol sy'n mynegi gofynion fel enghreifftiau pendant, darllenadwy o ymddygiad (yn aml ar ffurf Given/When/Then) sydd hefyd yn gwasanaethu fel profion derbyn awtomataidd.

**BFF (Backend for Frontend)**: Patrwm pensaernïol lle mae gwasanaeth cefn pwrpasol yn cael ei adeiladu ar gyfer math penodol o ffryntolwg neu gleient, gan deilwra siapio a chasglu data i anghenion y cleient hwnnw.

**[BI (Business Intelligence)](https://en.wikipedia.org/wiki/Business_intelligence)**: Yr offer, y prosesau, a'r arferion ar gyfer casglu, integreiddio, a dadansoddi data busnes i gefnogi adrodd, dangosfyrddau, a gwneud penderfyniadau.

**Blameless postmortem**: Adolygiad digwyddiad sy'n canolbwyntio ar achosion systemig a dysgu yn hytrach na bai unigolion, ar y sail bod pobl yn gweithredu'n rhesymol o ystyried y wybodaeth a'r cymhellion oedd ganddynt.

**[Blue-green deployment](https://en.wikipedia.org/wiki/Blue-green_deployment)**: Strategaeth ryddhau sy'n rhedeg dau amgylchedd cynhyrchu unfath ("glas" a "gwyrdd"), gan gyfeirio traffig i un tra bod y llall yn cael ei ddiweddaru, gan alluogi trosglwyddo ac ôl-droi bron yn syth.

**[BM25](https://en.wikipedia.org/wiki/Okapi_BM25)**: Ffwythiant graddio a ddefnyddir yn eang ar gyfer chwilio testun llawn sy'n sgorio pa mor dda y mae dogfen yn cyfateb i ymholiad gan ddefnyddio amlder term, amlder dogfen gwrthdro, a hyd dogfen. Dyma'r rhagosodiad graddio geiriadurol mewn llawer o beiriannau chwilio.

**Bounded context**: Yn Domain-Driven Design, ffin benodol y mae model parth penodol a'i iaith hollbresennol yn berthnasol yn gyson o'i mewn. Mae'n atal cysyniadau rhag cael eu cymysgu ar draws gwahanol rannau o system fawr.

**Build cache**: Storfa o allbynnau adeiladu a gyfrifwyd yn flaenorol, wedi'u mynegeio yn ôl y mewnbynnau a'u cynhyrchodd, fel bod gwaith heb newid yn cael ei ailddefnyddio yn hytrach na'i ailadeiladu. Mae storfa adeiladu bell a rennir yn caniatáu i dîm cyfan a'i CI ailddefnyddio canlyniadau ei gilydd.

**[Bus factor](https://en.wikipedia.org/wiki/Bus_factor)**: Nifer y bobl y byddai angen eu colli (yn drosiadol, "cael eu taro gan fws") cyn i brosiect stopio oherwydd diffyg gwybodaeth hanfodol. Mae ffactor bws isel yn arwyddo arbenigedd crynodedig, heb ei ddogfennu, a risg sefydliadol.

## C

**[Cache eviction policy](https://en.wikipedia.org/wiki/Cache_replacement_policies)**: Y rheol y mae storfa'n ei defnyddio i benderfynu pa gofnod i'w dynnu pan fydd yn llawn, megis y lleiaf a ddefnyddiwyd yn ddiweddar (LRU) neu'r lleiaf a ddefnyddiwyd yn aml (LFU). Mae'r polisi'n siapio'r gyfradd trawiad ac, felly, werth y storfa.

**[Cache invalidation](https://en.wikipedia.org/wiki/Cache_invalidation)**: Y broblem o dynnu neu ddiweddaru data wedi'i storio unwaith y bydd y ffynhonnell sylfaenol yn newid, fel nad yw darllenwyr yn gweld gwerthoedd hen. Dyma un o'r problemau anoddaf mewn cyfrifiadura, yn ôl y sôn.

**[Cache stampede](https://en.wikipedia.org/wiki/Cache_stampede)**: Modd methiant lle mae llawer o gleientiaid yn methu'r storfa ar gyfer yr un allwedd ar unwaith ac i gyd yn taro'r tarddiad gyda'i gilydd, gan ei orlwytho. Mae cyfuno ceisiadau a darfod camosodedig yn ei atal. Fe'i gelwir hefyd yn "thundering herd".

**Canary release**: Techneg ddefnyddio sy'n dangos fersiwn newydd i is-set fach o ddefnyddwyr neu draffig yn gyntaf, yn monitro am broblemau, ac yna'n ehangu'r lansiad yn raddol os yw'r metrigau'n aros yn iach.

**[CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem)**: Egwyddor sy'n nodi na all storfa ddata ddosbarthedig warantu mwy na dau o Gysondeb, Argaeledd, a Goddefiant Rhaniad ar unwaith; gan fod rhaniadau'n anochel, mae dylunwyr i bob pwrpas yn cyfnewid cysondeb yn erbyn argaeledd yn ystod rhaniad.

**[C4 model](https://en.wikipedia.org/wiki/C4_model)**: Dull ysgafn o weledoli pensaernïaeth meddalwedd ar bedwar lefel haniaeth: Cyd-destun System, Cynwysyddion, Cydrannau, a Chod.

**[CD (Continuous Delivery / Continuous Deployment)](https://en.wikipedia.org/wiki/Continuous_delivery)**: Mae Traddodiad Parhaus yn cadw meddalwedd mewn cyflwr y gellir ei ryddhau fel y gellir ei ddefnyddio ar unrhyw adeg gydag ardystiad â llaw; mae Defnyddio Parhaus yn rhyddhau pob newid sy'n pasio'r biblinell yn awtomatig.

**[CDN (Content Delivery Network)](https://en.wikipedia.org/wiki/Content_delivery_network)**: Rhwydwaith daearyddol wasgaredig o weinyddion ymyl sy'n storio ac yn gwasanaethu cynnwys yn agos at ddefnyddwyr, gan dorri oedi a llacio seilwaith tarddiad.

**Chain-of-thought prompting**: Techneg annog sy'n gofyn i fodel iaith weithio drwy gamau rhesymu canolradd cyn rhoi ateb terfynol, gan wella perfformiad ar broblemau aml-gam ar draul allbwn hirach, arafach.

**[CI (Continuous Integration)](https://en.wikipedia.org/wiki/Continuous_integration)**: Yr arfer o uno newidiadau datblygwyr yn aml i mewn i brif linell a rennir, gyda phob uniad yn cael ei ddilysu gan adeiladwaith a set brofion awtomataidd i ganfod problemau integreiddio yn gynnar.

**[CI/CD](https://en.wikipedia.org/wiki/CI/CD)**: Y biblinell gyfun o Integreiddio Parhaus a Thraddodiad/Defnyddio Parhaus sy'n awtomeiddio adeiladu, profi, a rhyddhau meddalwedd.

**CMMC (Cybersecurity Maturity Model Certification)**: Rhaglen gan Adran Amddiffyn UDA sy'n ardystio aeddfedrwydd seiberddiogelwch contractwyr sy'n trin gwybodaeth contract ffederal a gwybodaeth ddiddosbarth reoledig.

**[Cohesion](https://en.wikipedia.org/wiki/Cohesion_(computer_science))**: Y graddau y mae'r elfennau o fewn modiwl yn perthyn i'w gilydd ac yn gwasanaethu un pwrpas wedi'i ddiffinio'n dda. Mae cydlyniant uchel, ynghyd â chyplu isel, yn nodwedd o ddyluniad y gellir ei gynnal.

**Context window**: Y swm mwyaf o destun, wedi'i fesur mewn tocynnau, y gall model iaith ei ystyried ar unwaith, gan gwmpasu ei fewnbwn a'i allbwn. Mae'n gyllideb brin y mae'n rhaid i ddylunio anogiadau a chyd-destun ei rheoli'n fwriadol.

**[Conway's Law](https://en.wikipedia.org/wiki/Conway's_law)**: Yr arsylwad bod strwythur system yn tueddu i adlewyrchu strwythur cyfathrebu'r sefydliad sy'n ei hadeiladu. Mae'r "symudiad Conway gwrthdro" yn siapio timau'n fwriadol i gynhyrchu pensaernïaeth ddymunol.

**Core Web Vitals**: Set o fetrigau perfformiad gwe canolbwyntiedig ar y defnyddiwr a ddiffinnir gan Google (megis Largest Contentful Paint, Interaction to Next Paint, a Cumulative Layout Shift) sy'n mesur llwytho, rhyngweithredd, a sefydlogrwydd gweledol.

**[Cost of delay](https://en.wikipedia.org/wiki/Cost_of_delay)**: Cost economaidd peidio â chael rhywbeth wedi'i orffen eto, a fynegir fel gwerth a gollwyd fesul uned o amser. Mae ei wneud yn benodol yn troi blaenoriaethu o farn yn rhifyddeg, ac mae'n sail i reolau dilyniannu megis "weighted shortest job first".

**[Coupling](https://en.wikipedia.org/wiki/Coupling_(computer_programming))**: Graddau'r rhyngddibyniaeth rhwng modiwlau neu wasanaethau. Mae cyplu llac yn cyfyngu ar effaith crych newid ac yn nod canolog o bensaernïaeth dda.

**CQRS (Command Query Responsibility Segregation)**: Patrwm sy'n gwahanu'r model a ddefnyddir i newid cyflwr (gorchmynion) oddi wrth y model a ddefnyddir i ddarllen cyflwr (ymholiadau), gan ganiatáu i bob un gael ei optimeiddio a'i raddio'n annibynnol.

**[CVE (Common Vulnerabilities and Exposures)](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures)**: Catalog cyhoeddus o wendidau diogelwch a ddatgelwyd, pob un wedi'i neilltuo ag adnabyddydd unigryw fel y gall offer a thimau gyfeirio at yr un diffyg yn ddiamwys.

**CWV**: Gweler Core Web Vitals.

## D

**[DAST (Dynamic Application Security Testing)](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)**: Profi diogelwch sy'n archwilio cymhwysiad sy'n rhedeg o'r tu allan, heb fynediad i'r cod ffynhonnell, i ddod o hyd i wendidau sy'n ymddangos ar adeg rhedeg.

**Data-ink ratio**: Egwyddor gan Edward Tufte sy'n dal y dylai siart wario'r rhan fwyaf o'i inc ar y data ei hun ac ychydig ar addurniad, gan gael gwared ar linellau grid, borderi, a "chartjunk" nad ydynt yn hysbysu.

**[Data mesh](https://en.wikipedia.org/wiki/Data_mesh)**: Pensaernïaeth ddata ddatganoledig a model gweithredu sy'n trin data fel cynnyrch sy'n eiddo i dimau parth, wedi'i gefnogi gan seilwaith platfform hunanwasanaeth a llywodraethu ffederal.

**[Data visualization](https://en.wikipedia.org/wiki/Data_and_information_visualization)**: Yr arfer o godio data ar ffurf weledol (safle, hyd, lliw, ac ati) fel bod patrymau, cymariaethau, a thueddiadau'n dod yn ganfyddadwy a phenderfyniadau'n cael eu llywio'n well.

**[DDD (Domain-Driven Design)](https://en.wikipedia.org/wiki/Domain-driven_design)**: Dull o ddylunio meddalwedd sy'n canoli'r model ar y parth busnes, gan ddefnyddio iaith hollbresennol a rennir, cyd-destunau ffiniedig, a blociau adeiladu megis endidau, gwrthrychau gwerth, ac agregynnau.

**Design tokens**: Gwerthoedd wedi'u henwi, annibynnol ar blatfform (lliwiau, bylchu, teipograffeg, ac ati) sy'n codeiddio penderfyniadau dylunio fel y gellir eu rhannu'n gyson ar draws system ddylunio a sawl cynnyrch.

**DevEx / DevX (Developer Experience)**: Ansawdd cyffredinol rhyngweithiad dydd-i-ddydd datblygwr ag offer, platfformau, a phrosesau, gan gwmpasu ffrithiant, cyflymder adborth, a llwyth gwybyddol.

**[DevOps](https://en.wikipedia.org/wiki/DevOps)**: Diwylliant a set o arferion sy'n uno datblygu meddalwedd a gweithrediadau i fyrhau cylchoedd traddodi, cynyddu amlder defnyddio, a gwella dibynadwyedd drwy awtomeiddio a pherchnogaeth a rennir.

**DORA (DevOps Research and Assessment)**: Rhaglen ymchwil a'i phedwar metrig traddodi a ddefnyddir yn eang (amlder defnyddio, amser arwain ar gyfer newidiadau, cyfradd methiant newid, ac amser adfer gwasanaeth) a ddefnyddir i feincnodi perfformiad traddodi meddalwedd.

**DPIA (Data Protection Impact Assessment)**: Asesiad strwythuredig, sy'n ofynnol o dan GDPR ar gyfer prosesu risg uchel, sy'n adnabod ac yn lliniaru risgiau preifatrwydd cyn i brosiect fwrw ymlaen.

**Drift (configuration)**: Gwyriad graddol cyflwr gwirioneddol system oddi wrth ei chyflwr datganedig neu fwriadedig, a achosir yn aml gan newidiadau â llaw; nod Infrastructure as Code a GitOps yw ei ganfod a'i gywiro.

**Drift (model)**: Mewn dysgu peiriant, dirywiad perfformiad model dros amser wrth i briodweddau ystadegol data mewnbwn (gwyriad data) neu'r berthynas a fodelir (gwyriad cysyniad) newid.

**[DR (Disaster Recovery)](https://en.wikipedia.org/wiki/Disaster_recovery)**: Y strategaeth, y gweithdrefnau, a'r seilwaith ar gyfer adfer gwasanaeth a data ar ôl digwyddiad tarfu mawr, a lywodraethir fel arfer gan dargedau RTO ac RPO.

**[DRY (Don't Repeat Yourself)](https://en.wikipedia.org/wiki/Don't_repeat_yourself)**: Egwyddor ddylunio sy'n nodi y dylai fod gan bob darn o wybodaeth un cynrychiolaeth awdurdodol, gan leihau dyblygu a'r risg o ddiweddariadau anghyson.

## E

**East-west traffic**: Traffig rhwydwaith rhwng gwasanaethau y tu mewn i system neu ganolfan ddata, yn wahanol i draffig gogledd-de rhwng y system a chleientiaid allanol. Mae rhwyll gwasanaeth fel arfer yn llywodraethu traffig dwyrain-gorllewin.

**[Edge computing](https://en.wikipedia.org/wiki/Edge_computing)**: Rhedeg cyfrifiadaeth a storfa'n agos at le mae data'n cael ei gynhyrchu neu ei ddefnyddio yn hytrach nag mewn lleoliad canolog, i dorri oedi a lled band. Mae rhwydweithiau traddodi cynnwys yn ffurf gynnar, eang o hyn.

**[Elasticity](https://en.wikipedia.org/wiki/Elasticity_(cloud_computing))**: Gallu system i gaffael a rhyddhau adnoddau'n awtomatig mewn ymateb i alw sy'n newid, fel bod capasiti'n dilyn llwyth yn agos.

**[ELT (Extract, Load, Transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform)**: Patrwm integreiddio data sy'n llwytho data crai i mewn i storfa darged yn gyntaf ac yn ei drawsffurfio yno, gan ddefnyddio maint warysau a llynnoedd tŷ modern.

**[Embedding](https://en.wikipedia.org/wiki/Word_embedding)**: Cynrychiolaeth o destun, delweddau, neu ddata arall fel fector rhifiadol dwys, wedi'i leoli fel bod eitemau tebyg yn eistedd yn agos at ei gilydd. Mae embeddiadau'n pweru chwilio semantig a fector ac atgynhyrchu wedi'i atgyfnerthu drwy adalw.

**[EN 301 549](https://en.wikipedia.org/wiki/EN_301_549)**: Y safon Ewropeaidd sy'n nodi gofynion hygyrchedd ar gyfer cynhyrchion a gwasanaethau ICT, y cyfeirir ati mewn caffael sector cyhoeddus ledled yr UE ac sydd wedi'i halinio â WCAG.

**Error budget**: Y swm caniataol o annibynadwyedd a ganiateir gan SLO dros gyfnod; pan gaiff ei ddihysbyddu, mae timau'n blaenoriaethu gwaith dibynadwyedd dros nodweddion newydd. Mae'n cysoni'r tyndra rhwng cyflymder a sefydlogrwydd.

**[ETL (Extract, Transform, Load)](https://en.wikipedia.org/wiki/Extract,_transform,_load)**: Patrwm integreiddio data sy'n echdynnu data o ffynonellau, ei drawsffurfio i siâp targed, ac yn ei lwytho i mewn i gyrchfan megis warws.

**[EU AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act)**: Rheoliad yr Undeb Ewropeaidd sy'n dosbarthu systemau AI yn ôl risg ac yn gosod rhwymedigaethau yn unol â hynny, gan wahardd rhai defnyddiau a rheoleiddio systemau risg uchel yn drwm.

**[Eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency)**: Model cysondeb mewn systemau dosbarthedig lle gall copïau ddargyfeirio dros dro ond yn cydgyfeirio i'r un cyflwr unwaith y bydd diweddariadau'n peidio â lledaenu.

## F

**[Feature flag / feature toggle](https://en.wikipedia.org/wiki/Feature_toggle)**: Mecanwaith i alluogi neu analluogi swyddogaeth ar adeg rhedeg heb ailddefnyddio, a ddefnyddir ar gyfer lansiadau graddol, arbrofi, a rheolaeth weithredol.

**Feature store**: System ganolog ar gyfer diffinio, storio, a gwasanaethu nodweddion dysgu peiriant curedig yn gyson ar gyfer hyfforddi a chasgliad fel ei gilydd, gan leihau dyblygu a sgiwio hyfforddi/gwasanaethu.

**[FedRAMP (Federal Risk and Authorization Management Program)](https://en.wikipedia.org/wiki/FedRAMP)**: Rhaglen gan lywodraeth UDA sy'n safoni asesu diogelwch, awdurdodi, a monitro parhaus ar gyfer gwasanaethau cwmwl a ddefnyddir gan asiantaethau ffederal.

**Few-shot prompting**: Darparu model iaith â llond llaw o enghreifftiau wedi'u gweithio yn yr anogiad i ddangos y dasg a fformat yr allbwn a ddymunir, yn wahanol i anogi "zero-shot", sy'n rhoi cyfarwyddiadau heb enghreifftiau.

**FinOps**: Disgyblaeth ac arfer diwylliannol sy'n dod ag atebolrwydd ariannol i wariant cwmwl amrywiol, gan roi perchnogaeth a rennir dros gost a gwerth i dimau peirianneg, cyllid, a busnes.

**[FISMA (Federal Information Security Modernization Act)](https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act)**: Deddfwriaeth UDA sy'n ei gwneud yn ofynnol i asiantaethau ffederal weithredu, dogfennu, a monitro rhaglenni diogelwch gwybodaeth, a weithredir yn bennaf drwy ganllawiau NIST.

**Flow efficiency**: Y gyfran o gyfanswm amser arwain y mae eitem waith yn ei threulio'n cael ei gweithio'n weithredol yn hytrach nag yn aros, a gyfrifir fel amser ychwanegu gwerth wedi'i rannu â chyfanswm yr amser arwain. Mae'r rhan fwyaf o systemau'n rhyfeddol o isel, yn aml o dan 15 y cant.

**Four-eyes principle**: Rheolaeth sy'n ei gwneud yn ofynnol i weithred arwyddocaol gael ei hadolygu neu ei chymeradwyo gan o leiaf ddau berson, gan leihau'r siawns o wall neu gamymddwyn.

**[Fuzz testing (fuzzing)](https://en.wikipedia.org/wiki/Fuzzing)**: Techneg brofi awtomataidd sy'n bwydo mewnbynnau camffurfiedig, ar hap, neu annisgwyl i raglen i ddatgelu chwalfeydd, gwendidau diogelwch, a diffygion achosion ymyl.

## G

**[GDPR (General Data Protection Regulation)](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)**: Rheoliad yr Undeb Ewropeaidd sy'n llywodraethu prosesu data personol, gan roi hawliau i unigolion a gosod rhwymedigaethau ar reolwyr a phroseswyr, gyda chosbau sylweddol am beidio â chydymffurfio.

**GitOps**: Model gweithredu sy'n defnyddio Git fel yr unig ffynhonnell gwirionedd ar gyfer seilwaith a chymwysiadau datganiadol, gydag awtomeiddiad yn cysoni'r system fyw â'r cyflwr ymrwymedig yn barhaus.

**Golden path / paved road**: Ffordd ragosodedig, gefnogol, ddiffiniedig o adeiladu a rhyddhau meddalwedd o fewn sefydliad, wedi'i dylunio i wneud y dewis diogel, cydymffurfiol, dibynadwy yr un hawsaf.

**Golden record**: Mewn rheolaeth data feistr, y fersiwn unigol, cymodedig, awdurdodol o endid busnes (megis cwsmer) a gasglwyd o sawl system ffynhonnell drwy reolau paru a goroesiad.

**[Gradual typing](https://en.wikipedia.org/wiki/Gradual_typing)**: Dull system deipio sy'n gadael i deipio statig a deinamig gyd-fodoli mewn un sylfaen god, fel y gellir ychwanegu teipiau'n gynyddrannol at raglen a deipir yn ddeinamig. Mae awgrymiadau teip a gwiriwyr teip dewisol yn enghreifftiau cyffredin.

**[GraphQL](https://en.wikipedia.org/wiki/GraphQL)**: Iaith ymholi ac amser rhedeg ar gyfer APIs sy'n gadael i gleientiaid ofyn am yn union y data sydd ei angen arnynt mewn un alwad, gan ddefnyddio sgema a deipir yn gryf.

**[gRPC](https://en.wikipedia.org/wiki/gRPC)**: Fframwaith galwad gweithdrefn bell perfformiad uchel, contract-yn-gyntaf, sy'n defnyddio HTTP/2 a, fel arfer, Protocol Buffers ar gyfer cyfathrebu gwasanaeth-i-wasanaeth effeithlon.

## H

**Hermetic build**: Adeiladwaith sy'n dibynnu ar fewnbynnau a ddatganwyd yn benodol yn unig ac sydd wedi'i ynysu oddi wrth yr amgylchedd gwesteiwr, fel ei fod yn cynhyrchu'r un allbwn ym mhobman. Mae hermetigrwydd yn sylfaen i adeiladweithiau atgynhyrchadwy a storio parod dibynadwy.

**[HSM (Hardware Security Module)](https://en.wikipedia.org/wiki/Hardware_security_module)**: Dyfais caledwedd sy'n gwrthsefyll ymyrryd sy'n cynhyrchu, storio, a defnyddio allweddi cryptograffig, gan ddarparu amddiffyniad allweddi cryfach na dulliau meddalwedd yn unig.

**[HIPAA (Health Insurance Portability and Accountability Act)](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act)**: Deddfwriaeth UDA sy'n, ymhlith pethau eraill, gosod gofynion ar gyfer diogelu gwybodaeth iechyd warchodedig (PHI) ac yn llywodraethu ei defnydd a'i datgeliad.

**Horizontal scaling**: Cynyddu capasiti drwy ychwanegu mwy o enghreifftiau neu nodau ("graddio allan") yn hytrach na gwneud un nod yn fwy pwerus. Mae'n sylfaen i'r rhan fwyaf o benseiniau graddfa fawr, gwydn.

## I

**[IaC (Infrastructure as Code)](https://en.wikipedia.org/wiki/Infrastructure_as_code)**: Yr arfer o ddiffinio a darparu seilwaith drwy ffurfweddiad darllenadwy gan beiriant, wedi'i reoli gan fersiwn, yn hytrach na phrosesau â llaw, gan alluogi ailadroddadwyedd ac adolygiad.

**[IAM (Identity and Access Management)](https://en.wikipedia.org/wiki/Identity_management)**: Y fframwaith o bolisïau a thechnolegau sy'n sicrhau bod gan yr hunaniaethau cywir y mynediad cywir i'r adnoddau cywir ar yr adegau cywir.

**IDP / IdP**: Mae "IDP" fel arfer yn dynodi Internal Developer Platform, y haen offer hunanwasanaeth sy'n haniaethu seilwaith ar gyfer timau cynnyrch; mae "IdP" yn dynodi Identity Provider, gwasanaeth sy'n dilysu defnyddwyr ac yn cyhoeddi honiadau. Mae cyd-destun yn datrys yr amwysedd rhwng y ddau.

**[Idempotency](https://en.wikipedia.org/wiki/Idempotence)**: Priodwedd lle mae cyflawni gweithred sawl gwaith yn cael yr un effaith â'i chyflawni unwaith, sy'n hanfodol ar gyfer ailgeisiadau diogel mewn systemau dosbarthedig ac APIs.

**[i18n (Internationalization)](https://en.wikipedia.org/wiki/Internationalization_and_localization)**: Dylunio ac adeiladu meddalwedd fel y gellir ei haddasu i wahanol ieithoedd, rhanbarthau, a chonfensiynau diwylliannol heb newidiadau peirianneg. Mae'r rhifenw'n talfyrru'r 18 llythyren rhwng "i" ac "n."

**Immutable artefact**: Allbwn adeiladu na chaiff, unwaith y'i cynhyrchir a'i fersiynu, ei addasu byth; mae unrhyw newid yn cynhyrchu fersiwn newydd. Mae anghyfnewidioldeb yn gwneud rhyddhadau'n atgynhyrchadwy ac yn caniatáu adeiladu unwaith a dyrchafu'r un arteffact ar draws amgylcheddau.

**InnerSource**: Cymhwyso arferion datblygu cod agored (tryloywder, ystorfeydd a rennir, a chyfraniad traws-dîm) o fewn un sefydliad.

**IaC drift**: Gweler Drift (configuration).

**[Inverted index](https://en.wikipedia.org/wiki/Inverted_index)**: Prif strwythur data peiriant chwilio, sy'n mapio pob term i'r rhestr o ddogfennau sy'n ei gynnwys, fel y gellir ateb ymholiadau heb sganio pob dogfen.

**[ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001)**: Safon ryngwladol sy'n nodi gofynion ar gyfer System Rheoli Diogelwch Gwybodaeth (ISMS), gan ddarparu fframwaith y gellir ei ardystio ar gyfer rheoli risg diogelwch gwybodaeth.

**ISO/IEC 42001**: Safon ryngwladol sy'n nodi gofynion ar gyfer System Rheoli AI, gan roi fframwaith y gellir ei ardystio i sefydliadau ar gyfer llywodraethu datblygu a defnyddio AI yn gyfrifol.

## J

**[JWT (JSON Web Token)](https://en.wikipedia.org/wiki/JSON_Web_Token)**: Fformat tocyn cryno, wedi'i lofnodi (ac yn ddewisol wedi'i amgryptio) a ddefnyddir i gyfleu hawliadau rhwng partïon, yn gyffredin ar gyfer dilysu ac awdurdodi mewn systemau gwe ac API.

## K

**[Kanban](https://en.wikipedia.org/wiki/Kanban_(development))**: Dull llif gwaith cynnil sy'n gweledoli gwaith ar fwrdd, yn cyfyngu ar waith ar y gweill, ac yn rheoli llif i wella cynnyrch a rhagweladwyedd.

**[KISS (Keep It Simple, Stupid)](https://en.wikipedia.org/wiki/KISS_principle)**: Egwyddor ddylunio sy'n ffafrio'r ateb symlaf sy'n diwallu'r angen, ar y sail bod cymhlethdod diangen yn cynyddu cost a risg.

**KMS (Key Management Service)**: System ar gyfer creu, storio, cylchdroi, a rheoli mynediad at allweddi cryptograffig, wedi'i chefnogi'n aml gan fodiwlau diogelwch caledwedd.

**[KPI (Key Performance Indicator)](https://en.wikipedia.org/wiki/Performance_indicator)**: Mesur meintiol a ddefnyddir i olrhain cynnydd tuag at amcan busnes neu weithredol penodol.

## L

**Lakehouse**: Pensaernïaeth ddata sy'n cyfuno storfa hyblyg, cost isel llyn data â nodweddion rheoli, trafodion, a pherfformiad warws data.

**[Lead time](https://en.wikipedia.org/wiki/Lead_time)**: Yr amser a dreulir o newid yn cael ei ofyn amdano (neu ei ymrwymo) i'w draddodi i gynhyrchu; metrig traddodi craidd DORA.

**[Least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege)**: Egwyddor ddiogelwch sy'n rhoi i bob defnyddiwr, proses, neu system y mynediad lleiaf sydd ei angen i gyflawni ei swyddogaeth, gan gyfyngu'r difrod o gyfaddawd neu wall.

**[Little's Law](https://en.wikipedia.org/wiki/Little's_law)**: Canlyniad o theori ciwio sy'n nodi bod nifer cyfartalog yr eitemau mewn system sefydlog yn hafal i'r gyfradd gyfartalog o gyrraedd wedi'i lluosi â'r amser cyfartalog y mae pob eitem yn ei dreulio yn y system. Mae'n cysylltu gwaith ar y gweill, cynnyrch, ac amser arwain.

**[LLM (Large Language Model)](https://en.wikipedia.org/wiki/Large_language_model)**: Model dysgu peiriant wedi'i hyfforddi ar gorpora testun mawr iawn i ragfynegi a chynhyrchu iaith, sy'n gallu cyflawni tasgau megis crynhoi, cyfieithu, a chynhyrchu cod.

**[l10n (Localization)](https://en.wikipedia.org/wiki/Language_localisation)**: Addasu meddalwedd rhyngwladol i leoliad penodol, gan gynnwys cyfieithu, fformatio, a chonfensiynau diwylliannol. Mae'r rhifenw'n talfyrru'r 10 llythyren rhwng "l" ac "n."

## M

**[MDM (Master Data Management)](https://en.wikipedia.org/wiki/Master_data_management)**: Y ddisgyblaeth a'r offer ar gyfer creu a chynnal golwg unigol, awdurdodol, cyson o endidau busnes craidd (megis cwsmeriaid neu gynhyrchion) ar draws systemau.

**MITRE ATT&CK**: Cronfa wybodaeth gyhoeddus, guredig o dactegau a thechnegau gwrthwynebwyr byd go iawn, a ddefnyddir yn eang i gynllunio ymarferion tîm coch, llywio peirianneg canfod, a disgrifio bygythiadau mewn geirfa a rennir.

**Mean Time to Recovery (MTTR)**: Yr amser cyfartalog a gymerir i adfer gwasanaeth ar ôl methiant; metrig dibynadwyedd a rheoli digwyddiadau cyffredin.

**[Mob programming](https://en.wikipedia.org/wiki/Mob_programming)**: Arfer lle mae tîm cyfan yn gweithio gyda'i gilydd ar yr un dasg wrth yr un cyfrifiadur, gan gylchdroi pwy sy'n teipio, i rannu gwybodaeth a gwneud penderfyniadau ar y cyd.

**[MLOps (Machine Learning Operations)](https://en.wikipedia.org/wiki/MLOps)**: Y set o arferion sy'n defnyddio, monitro, a chynnal modelau dysgu peiriant mewn cynhyrchu'n ddibynadwy ac yn effeithlon, gan ymestyn egwyddorion DevOps i gylch bywyd ML.

**[Monorepo](https://en.wikipedia.org/wiki/Monorepo)**: Un ystorfa rheolaeth fersiynau sy'n dal cod ar gyfer sawl prosiect neu'r sefydliad cyfan, gan alluogi offer a rennir a newidiadau traws-brosiect atomig ar draul offer graddio arbenigol.

**mTLS (mutual TLS)**: Ffurfweddiad o Transport Layer Security lle mae'r ddau barti'n cyflwyno ac yn gwirio tystysgrifau, fel bod pob un yn dilysu'r llall. Mae'n rhagosodiad ar gyfer traffig gwasanaeth-i-wasanaeth mewn rhwyll gwasanaeth a rhwydweithiau ymddiriedaeth sero. Gweler hefyd [mutual authentication](https://en.wikipedia.org/wiki/Mutual_authentication).

**[Mutation testing](https://en.wikipedia.org/wiki/Mutation_testing)**: Techneg sy'n cyflwyno namau bach ("mutantiaid") i god yn fwriadol i wirio a yw'r set brofion yn eu canfod, gan fesur effeithiolrwydd gwirioneddol y set.

## N

**[NDCG (Normalized Discounted Cumulative Gain)](https://en.wikipedia.org/wiki/Discounted_cumulative_gain)**: Metrig ansawdd graddio sy'n gwobrwyo gosod canlyniadau perthnasol iawn yn agos at frig rhestr canlyniadau, wedi'i normaleiddio fel bod sgoriau'n gymaradwy ar draws ymholiadau. Mae'n hanfod o werthuso perthnasedd chwilio.

**[NIST (National Institute of Standards and Technology)](https://en.wikipedia.org/wiki/National_Institute_of_Standards_and_Technology)**: Asiantaeth ffederal UDA y mae ei Chyhoeddiadau Arbennig a'i fframweithiau'n safonau y cyfeirir atynt yn eang ar gyfer seiberddiogelwch, preifatrwydd, ac AI.

**NIST AI RMF (AI Risk Management Framework)**: Fframwaith NIST gwirfoddol ar gyfer adnabod, asesu, a rheoli risgiau sy'n gysylltiedig â systemau AI ar draws eu cylch bywyd, wedi'i drefnu o amgylch y swyddogaethau Llywodraethu, Mapio, Mesur, a Rheoli.

**[NIST SP 800-53](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53)**: Catalog NIST o reolyddion diogelwch a phreifatrwydd ar gyfer systemau gwybodaeth ffederal, a ddefnyddir yn eang fel llinell sylfaen ymhell y tu hwnt i lywodraeth.

**NIST SP 800-171**: Cyhoeddiad NIST sy'n nodi gofynion ar gyfer diogelu gwybodaeth ddiddosbarth reoledig (CUI) mewn systemau anffederal, sy'n ganolog i gydymffurfiaeth contractwyr amddiffyn.

**[NFR (Non-Functional Requirement)](https://en.wikipedia.org/wiki/Non-functional_requirement)**: Gofyniad sy'n disgrifio sut y dylai system ymddwyn (ei hansoddau megis perfformiad, diogelwch, dibynadwyedd, neu ddefnyddioldeb) yn hytrach na pha swyddogaethau y mae'n eu cyflawni.

**North-south traffic**: Traffig rhwydwaith rhwng system a'i chleientiaid allanol (i mewn ac allan o'r ganolfan ddata neu'r clwstwr), yn wahanol i draffig dwyrain-gorllewin rhwng gwasanaethau mewnol. Mae porth API fel arfer yn llywodraethu traffig gogledd-de.

## O

**Observability**: Y graddau y gellir casglu cyflwr mewnol system o'i hallbynnau allanol, a gyflawnir fel arfer drwy delemetreg: metrigau, cofnodion, ac olrheiniadau.

**[OKR (Objectives and Key Results)](https://en.wikipedia.org/wiki/OKR)**: Fframwaith gosod nodau sy'n paru amcan ansoddol â nifer bach o ganlyniadau allweddol mesuradwy i alinio a chanolbwyntio sefydliad.

**OpenTelemetry (OTel)**: Safon a chyfarpar agored, niwtral o ran gwerthwr, ar gyfer cynhyrchu, casglu, ac allforio data telemetreg (olrheiniadau, metrigau, a chofnodion) o feddalwedd.

**OPA (Open Policy Agent)**: Peiriant polisi cod agored, diben cyffredinol sy'n gwerthuso polisïau (wedi'u hysgrifennu yn iaith Rego) i orfodi rheolau awdurdodi a ffurfweddiad ar draws y stac, gan alluogi polisi fel cod.

**OSPO (Open Source Program Office)**: Swyddogaeth sefydliadol sy'n cydgysylltu strategaeth, llywodraethu, cydymffurfiaeth, ac ymgysylltiad cymunedol cod agored, gan reoli defnydd a chyfraniad fel ei gilydd.

**[OWASP (Open Worldwide Application Security Project)](https://en.wikipedia.org/wiki/OWASP)**: Cymuned ddielw sy'n cynhyrchu adnoddau diogelwch cymwysiadau am ddim, a ddefnyddir yn eang, gan gynnwys yr OWASP Top Ten a'r ASVS.

## P

**[PACELC](https://en.wikipedia.org/wiki/PACELC_theorem)**: Estyniad o theorem CAP sy'n nodi, os oes Rhaniad, bod system yn cyfnewid Argaeledd yn erbyn Cysondeb, Neu Fel Arall (mewn gweithrediad arferol) mae'n cyfnewid Oedi yn erbyn Cysondeb.

**[PCI DSS (Payment Card Industry Data Security Standard)](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard)**: Safon ddiogelwch a gynhelir gan y diwydiant cardiau talu sy'n nodi gofynion ar gyfer sefydliadau sy'n storio, prosesu, neu drosglwyddo data deiliad cerdyn.

**[Penetration testing](https://en.wikipedia.org/wiki/Penetration_test)**: Ymosodiad awdurdodedig, efelychiadol ar system gan brofwyr medrus i ddod o hyd i wendidau y gellir eu hecsbloetio a'u dangos cyn i ymosodwyr gwirioneddol wneud hynny, wedi'i draddodi fel canfyddiadau blaenoriaethedig, gweithredadwy.

**[PII (Personally Identifiable Information)](https://en.wikipedia.org/wiki/Personal_data)**: Gwybodaeth a all adnabod unigolyn penodol, naill ai ar ei ben ei hun neu wedi'i chyfuno â data arall; llywodraethir ei thrin gan gyfreithiau preifatrwydd a pholisi mewnol.

**Platform engineering**: Y ddisgyblaeth o adeiladu a gweithredu platfformau hunanwasanaeth mewnol a llwybrau euraidd sy'n lleihau llwyth gwybyddol ac yn cyflymu timau cynnyrch.

**POUR**: Pedair egwyddor arweiniol y Web Content Accessibility Guidelines: rhaid i gynnwys fod yn Ganfyddadwy (Perceivable), yn Weithredadwy (Operable), yn Ddealladwy (Understandable), ac yn Gadarn (Robust).

**Production readiness review**: Gwiriad strwythuredig, a redir cyn i wasanaeth fynd yn fyw neu gymryd perchnogaeth ar-alwad, sy'n cadarnhau ei fod yn bodloni safonau ar gyfer arsylladwyedd, dibynadwyedd, diogelwch, llawlyfrau gweithredu, a chymorth gweithredol.

**[Prompt engineering](https://en.wikipedia.org/wiki/Prompt_engineering)**: Yr arfer o ddylunio a mireinio'r cyfarwyddiadau, y cyd-destun, a'r enghreifftiau a roddir i fodel iaith i gael allbwn dibynadwy, o ansawdd uchel, a drinnir fel disgyblaeth beirianneg wedi'i fersiynu, wedi'i phrofi yn hytrach na chynnig a chamgymeriad.

**[Prompt injection](https://en.wikipedia.org/wiki/Prompt_injection)**: Ymosodiad lle mae mewnbwn wedi'i grefftio'n achosi i fodel iaith anwybyddu ei gyfarwyddiadau bwriadedig a dilyn rhai'r ymosodwr yn lle hynny, cyfatebiaeth oes-AI o ddiffygion chwistrelliad. Mae'n risg diogelwch canolog cymwysiadau LLM.

**Property-based testing**: Techneg brofi sy'n gwirio bod priodweddau datganedig yn dal ar draws llawer o fewnbynnau a gynhyrchwyd yn awtomatig, yn hytrach na dibynnu ar enghreifftiau a ddewiswyd â llaw yn unig.

**Pull request (PR) / merge request (MR)**: Set arfaethedig o newidiadau a gyflwynir i'w hadolygu a'u trafod cyn cael eu huno i gangen a rennir, prif uned adolygu cod yn y rhan fwyaf o lifau gwaith.

**Purple team**: Ymarfer cydweithredol lle mae timau diogelwch ymosodol (coch) ac amddiffynnol (glas) yn gweithio gyda'i gilydd mewn amser real, fel bod ymosodiadau a'r canfyddiadau a fwriedir i'w dal yn cael eu tiwnio yn erbyn ei gilydd.

## Q

**Quality gate**: Pwynt gwirio awtomataidd mewn piblinell y mae'n rhaid ei basio (er enghraifft, cyrraedd trothwyon gorchudd, diogelwch, neu berfformiad) cyn y gall newid symud ymlaen.

**[Quorum](https://en.wikipedia.org/wiki/Quorum_(distributed_computing))**: Mewn systemau dosbarthedig, y nifer lleiaf o nodau y mae'n rhaid iddynt gytuno i weithred (megis darllen neu ysgrifennu) gael ei hystyried yn llwyddiannus, a ddefnyddir i gynnal cysondeb er gwaethaf methiannau.

## R

**[RACI](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)**: Model neilltuo cyfrifoldeb sy'n labelu pob cyfranogwr mewn tasg neu benderfyniad fel Cyfrifol, Atebol, Ymgynghorwyd ag ef, neu Wybodwyd iddo.

**[RAG (Retrieval-Augmented Generation)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)**: Techneg sy'n seilio allbwn model iaith drwy adfer dogfennau neu ddata perthnasol yn gyntaf a'u darparu fel cyd-destun, gan wella cywirdeb a lleihau rhithdybio.

**[RBAC (Role-Based Access Control)](https://en.wikipedia.org/wiki/Role-based_access_control)**: Model awdurdodi sy'n neilltuo caniatâd i rolau a rolau i ddefnyddwyr, gan symleiddio gweinyddiaeth drwy reoli mynediad ar lefel y rôl.

**[Red team](https://en.wikipedia.org/wiki/Red_team)**: Grŵp sy'n efelychu gwrthwynebwr realistig, yn aml yn erbyn sefydliad cyfan a heb rybuddio amddiffynwyr, i brofi canfod ac ymateb yn hytrach na dim ond rhestru gwendidau. Cyferbynner â thîm glas (amddiffynnol).

**[Reference data](https://en.wikipedia.org/wiki/Reference_data)**: Rhestrau côd a dosbarthiadau rheoledig, sy'n newid yn araf, a ddefnyddir i gategoreiddio data arall, megis codau gwlad, arianbethau, a gwerthoedd statws. Mae ei lywodraethu fel geirfa a rennir, wedi'i fersiynu yn cadw systemau'n gyson.

**Rego**: Yr iaith bolisi ddatganiadol a ddefnyddir gan Open Policy Agent i fynegi rheolau ar gyfer penderfyniadau awdurdodi a ffurfweddiad.

**[REST (Representational State Transfer)](https://en.wikipedia.org/wiki/REST)**: Arddull bensaernïol ar gyfer cymwysiadau rhwydweithiedig sy'n defnyddio gweithrediadau di-gyflwr dros HTTP ar adnoddau cyfeiriadwy, a werthfawrogir am symlrwydd ac offer eang.

**[Reverse proxy](https://en.wikipedia.org/wiki/Reverse_proxy)**: Gweinydd sy'n eistedd o flaen un neu fwy o wasanaethau cefn ac yn anfon ceisiadau cleientiaid ymlaen atynt, gan ddarparu terfyniad TLS, cydbwyso llwyth, storio parod, a phwynt mynediad sengl yn gyffredin.

**[RFC (Request for Comments)](https://en.wikipedia.org/wiki/Request_for_Comments)**: Cynnig ysgrifenedig a gylchredir am adborth cyn penderfyniad neu newid technegol arwyddocaol, gan feithrin tryloywder a pherchnogaeth a rennir. (Mae'r term hefyd yn enwi cyfres ddogfennau safonau Rhyngrwyd.)

**[ROI (Return on Investment)](https://en.wikipedia.org/wiki/Return_on_investment)**: Mesur o'r gwerth a enillir o fuddsoddiad o'i gymharu â'i gost, a ddefnyddir i gyfiawnhau a blaenoriaethu penderfyniadau peirianneg a thechnoleg.

**[RPA (Robotic Process Automation)](https://en.wikipedia.org/wiki/Robotic_process_automation)**: "Robotiaid" meddalwedd sy'n awtomeiddio tasgau ailadroddus, wedi'u seilio ar reolau, drwy ryngweithio â rhyngwynebau defnyddiwr a systemau presennol fel y byddai person.

**RPO (Recovery Point Objective)**: Y swm mwyaf derbyniol o golled data a fesurir mewn amser (er enghraifft, "hyd at bum munud"), sy'n diffinio pa mor aml y mae'n rhaid diogelu data.

**RTO (Recovery Time Objective)**: Y cyfnod mwyaf derbyniol i adfer gwasanaeth ar ôl tarfiad, gan lywio dylunio a buddsoddiad adfer trychineb.

## S

**Saga**: Patrwm ar gyfer rheoli cysondeb data ar draws gwasanaethau mewn trafodiad dosbarthedig drwy ddilyniannu trafodion lleol a chyhoeddi gweithredoedd iawndal pan fydd cam yn methu.

**[SAFe (Scaled Agile Framework)](https://en.wikipedia.org/wiki/Scaled_agile_framework)**: Fframwaith ar gyfer cymhwyso arferion ystwyth a chynnil ar draws mentrau mawr, gan gydgysylltu llawer o dimau; a werthfawrogir am strwythur ac a feirniedir am drymder posibl.

**[SAST (Static Application Security Testing)](https://en.wikipedia.org/wiki/Static_application_security_testing)**: Profi diogelwch sy'n dadansoddi cod ffynhonnell, bytgod, neu ddeuaidd heb eu gweithredu i ddod o hyd i wendidau'n gynnar mewn datblygiad.

**SBOM (Software Bill of Materials)**: Rhestr ffurfiol, ddarllenadwy gan beiriant o'r cydrannau a'r dibyniaethau mewn darn o feddalwedd, a ddefnyddir i reoli risg cadwyn gyflenwi a gwendidau.

**SCA (Software Composition Analysis)**: Offer sy'n adnabod cydrannau cod agored a thrydydd parti mewn sylfaen god ac yn baneri gwendidau hysbys a risgiau trwyddedu.

**[Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development))**: Fframwaith ystwyth sy'n trefnu gwaith yn ailadroddiadau hyd sefydlog (sbrintiau) gyda rolau, digwyddiadau, ac arteffactau diffiniedig i draddodi cynnydd o werth.

**[Section 508](https://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)**: Cyfraith UDA sy'n ei gwneud yn ofynnol i asiantaethau ffederal wneud eu technoleg electronig a gwybodaeth yn hygyrch i bobl ag anableddau, sydd, mewn ymarfer, wedi'i halinio â WCAG.

**Semantic search**: Chwilio sy'n paru ar ystyr yn hytrach nag allweddeiriau union, fel arfer drwy gymharu embeddiadau'r ymholiad a'r dogfennau. Fe'i cyfunir yn aml â chwilio geiriadurol mewn dull hybrid.

**[Service mesh](https://en.wikipedia.org/wiki/Service_mesh)**: Haen seilwaith bwrpasol, a weithredir fel arfer gyda dirprwyon sidecar, sy'n trin pryderon cyfathrebu gwasanaeth-i-wasanaeth megis TLS dwyochrog, ailgeisiadau, terfynau amser, symud traffig, ac arsylladwyedd, gan eu cadw allan o god y cymhwysiad.

**Sidecar**: Proses neu gynhwysydd cynorthwyol a ddefnyddir ochr yn ochr ag enghraifft brif gymhwysiad i ddarparu galluoedd cefnogol (megis dirprwy rhwyll gwasanaeth) heb newid y cymhwysiad ei hun.

**[SIEM (Security Information and Event Management)](https://en.wikipedia.org/wiki/Security_information_and_event_management)**: System sy'n cydgasglu a chydberthyn cofnodion a digwyddiadau diogelwch ar draws amgylchedd i alluogi canfod, rhybuddio, ac ymchwilio.

**[SLA (Service Level Agreement)](https://en.wikipedia.org/wiki/Service-level_agreement)**: Ymrwymiad ffurfiol rhwng darparwr gwasanaeth a'i gwsmeriaid sy'n nodi lefelau gwasanaeth disgwyliedig a chanlyniadau eu methu.

**SLI (Service Level Indicator)**: Mesur meintiol o ryw agwedd ar ansawdd gwasanaeth, megis oedi cais neu gyfradd gwall, sy'n bwydo i mewn i SLOs.

**SLO (Service Level Objective)**: Gwerth neu ystod targed ar gyfer SLI sy'n diffinio'r lefel ddymunol o ddibynadwyedd, gan ffurfio sail cyllidebau gwall.

**SLSA (Supply-chain Levels for Software Artifacts)**: Fframwaith o ofynion diogelwch graddedig ar gyfer gwella uniondeb a tharddiad arteffactau meddalwedd drwy'r broses adeiladu a rhyddhau.

**SOAR (Security Orchestration, Automation, and Response)**: Offer ac arferion sy'n awtomeiddio ac yn cydgysylltu gweithrediadau diogelwch, megis llyfrau chwarae didoli ac ymateb, i wella cyflymder a chysondeb.

**SOC 2 (System and Organization Controls 2)**: Fframwaith archwilio ac adroddiad, wedi'i seilio ar Feini Prawf Gwasanaethau Ymddiriedaeth AICPA, sy'n asesu rheolyddion sefydliad gwasanaeth ar gyfer diogelwch, argaeledd, uniondeb prosesu, cyfrinachedd, a phreifatrwydd.

**[SOLID](https://en.wikipedia.org/wiki/SOLID)**: Pum egwyddor dylunio gwrthrych-gyfeiriedig (Cyfrifoldeb Unigol, Agored/Caeedig, Amnewid Liskov, Gwahanu Rhyngwyneb, a Gwrthdroi Dibyniaeth) sy'n hyrwyddo cod y gellir ei gynnal ac sy'n hyblyg.

**[SOX (Sarbanes-Oxley Act)](https://en.wikipedia.org/wiki/Sarbanes-Oxley_Act)**: Deddfwriaeth UDA sy'n sefydlu gofynion ar gyfer adrodd ariannol a rheolyddion mewnol mewn cwmnïau cyhoeddus, gydag oblygiadau ar gyfer y systemau TG sy'n cefnogi data ariannol.

**SPACE**: Fframwaith ar gyfer mesur cynnyrch datblygwyr ar draws pum dimensiwn: Boddhad a lles, Perfformiad, Gweithgarwch, Cyfathrebu a chydweithio, ac Effeithlonrwydd a llif, gan rybuddio yn erbyn mesurau un metrig.

**[SRE (Site Reliability Engineering)](https://en.wikipedia.org/wiki/Site_reliability_engineering)**: Disgyblaeth sy'n cymhwyso dulliau peirianneg meddalwedd at weithrediadau, gan ddefnyddio SLOs, cyllidebau gwall, ac awtomeiddio i redeg systemau dibynadwy ar raddfa.

**SSDF (Secure Software Development Framework)**: Fframwaith NIST (SP 800-218) o arferion datblygu diogel lefel uchel, sy'n cwmpasu paratoi'r sefydliad, diogelu meddalwedd, cynhyrchu meddalwedd wedi'i diogelu'n dda, ac ymateb i wendidau.

**[Static analysis](https://en.wikipedia.org/wiki/Static_program_analysis)**: Archwilio cod ffynhonnell, bytgod, neu ddeuaidd heb eu gweithredu i ddod o hyd i ddiffygion, torriadau arddull, a gwendidau diogelwch, fel arfer drwy linwyr, gwiriwyr teip, a dadansoddwyr pwrpasol wedi'u gwifro i mewn i'r golygydd a'r biblinell.

**[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)**: Tacsonomeg modelu bygythiad sy'n categoreiddio bygythiadau fel Ffugio (Spoofing), Ymyrryd (Tampering), Gwadu (Repudiation), Datgelu gwybodaeth (Information disclosure), Gwadu gwasanaeth (Denial of service), a Dyrchafiad braint (Elevation of privilege).

## T

**[TCO (Total Cost of Ownership)](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**: Cost oes lawn system neu benderfyniad, gan gynnwys caffael, gweithredu, cynnal, ac ymddeoliad terfynol, nid dim ond y pris cychwynnol.

**[TDD (Test-Driven Development)](https://en.wikipedia.org/wiki/Test-driven_development)**: Arfer o ysgrifennu prawf awtomataidd sy'n methu cyn y cod sy'n ei basio, ac yna ailffactora, mewn cylchoedd byr, ailadroddus i lywio dyluniad a sicrhau gorchudd.

**[Technical debt](https://en.wikipedia.org/wiki/Technical_debt)**: Cost dyfodol ymhlyg dewis ateb hwylus nawr dros un gwell a fyddai'n cymryd yn hwy, sy'n rhaid ei reoli'n fwriadol yn hytrach na'i gronni'n anymwybodol.

**TF-IDF (Term Frequency-Inverse Document Frequency)**: Cynllun pwysoli clasurol sy'n sgorio pwysigrwydd term i ddogfen yn ôl pa mor aml y mae'n ymddangos ynddi, wedi'i wrthbwyso gan pa mor gyffredin ydyw ar draws y corpws cyfan. Mae'n sail i lawer o raddio chwilio geiriadurol.

**[Theory of constraints](https://en.wikipedia.org/wiki/Theory_of_constraints)**: Dull rheoli sy'n dal bod cynnyrch system wedi'i gyfyngu gan un tagfa ar unrhyw adeg, felly dylai ymdrechion gwella ganolbwyntio ar y cyfyngiad hwnnw nes iddo symud i rywle arall.

**[Threat modelling](https://en.wikipedia.org/wiki/Threat_model)**: Arfer strwythuredig o adnabod, rhestru, a blaenoriaethu bygythiadau posibl i system fel y gellir dylunio amddiffynfeydd yn gynnar.

**Toil**: Yn SRE, gwaith gweithredol â llaw, ailadroddus, y gellir ei awtomeiddio sy'n graddio'n llinol â gwasanaeth ac nad yw'n darparu gwerth parhaol; mae ei leihau'n rhyddhau capasiti ar gyfer peirianneg.

**Trunk-based development**: Arfer rheoli ffynhonnell lle mae datblygwyr yn integreiddio newidiadau bach yn aml i mewn i un gangen a rennir, gan leihau canghennau hirhoedlog a phoen uno.

**[Type inference](https://en.wikipedia.org/wiki/Type_inference)**: Nodwedd iaith sy'n didynnu mathau mynegiadau'n awtomatig, gan roi llawer o ddiogelwch teipio statig heb fod angen ysgrifennu pob math â llaw.

**[Type system](https://en.wikipedia.org/wiki/Type_system)**: Y set o reolau y mae iaith yn eu defnyddio i neilltuo a gwirio mathau, gan ddal dosbarthiadau cyfan o wall cyn i'r rhaglen redeg a dogfennu bwriad. Mae systemau teipio'n amrywio o ddeinamig i statig ac o wan i gryf.

## U

**Ubiquitous language**: Yn Domain-Driven Design, geirfa a rennir, fanwl gywir a ddefnyddir yn gyson gan ddatblygwyr ac arbenigwyr parth, ac a adlewyrchir yn uniongyrchol yn y cod a'r modelau.

**[UAT (User Acceptance Testing)](https://en.wikipedia.org/wiki/Acceptance_testing)**: Profi a gyflawnir gan ddefnyddwyr terfynol neu eu cynrychiolwyr i gadarnhau bod system yn diwallu anghenion busnes cyn ei derbyn i'w rhyddhau.

**[UX / UI (User Experience / User Interface)](https://en.wikipedia.org/wiki/User_experience)**: Profiad Defnyddiwr yw ansawdd cyffredinol rhyngweithiad person â chynnyrch; Rhyngwyneb Defnyddiwr yw'r wyneb gweledol a rhyngweithiol penodol y mae'r rhyngweithiad hwnnw'n digwydd drwyddo.

## V

**[Value object](https://en.wikipedia.org/wiki/Value_object)**: Yn Domain-Driven Design, gwrthrych anghyfnewidiol a ddiffinnir yn gyfan gwbl gan ei briodoleddau yn hytrach na hunaniaeth wahanol, megis swm ariannol neu ystod dyddiadau.

**[Value stream mapping](https://en.wikipedia.org/wiki/Value-stream_mapping)**: Techneg ar gyfer tynnu llun pob cam o syniad i werth a draddodwyd, gan wahaniaethu rhwng amser ychwanegu gwerth ac amser aros, fel bod tagfeydd, trosglwyddiadau, a dolenni ailwaith yn dod yn weladwy ac yn wellach.

**[Vector database](https://en.wikipedia.org/wiki/Vector_database)**: Storfa ddata wedi'i optimeiddio ar gyfer mynegeio a chwilio fectorau embedding uchel-ddimensiwn yn ôl tebygrwydd, asgwrn cefn cyffredin i chwilio semantig ac atgynhyrchu wedi'i atgyfnerthu drwy adalw.

**Vertical scaling**: Cynyddu capasiti drwy wneud un nod yn fwy pwerus ("graddio i fyny"), sy'n syml ond yn y pen draw wedi'i gyfyngu gan y peiriant mwyaf sydd ar gael.

**[VCS (Version Control System)](https://en.wikipedia.org/wiki/Version_control)**: Teclyn, megis Git, sy'n cofnodi newidiadau i ffeiliau dros amser fel y gellir adolygu hanes, cynnal canghennau, a chydgysylltu gwaith.

**[Vulnerability scanning](https://en.wikipedia.org/wiki/Vulnerability_scanner)**: Archwiliad awtomataidd o systemau, cynwysyddion, neu god yn erbyn cronfeydd data o wendidau a chamffurfweddiadau hysbys. Mae'n eang ac yn rhad, ac yn ategu dyfnder profi treiddiad â llaw.

## W

**[WCAG (Web Content Accessibility Guidelines)](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines)**: Set o ganllawiau W3C, a gydnabyddir yn rhyngwladol, wedi'u trefnu o amgylch egwyddorion POUR a lefelau cydymffurfiaeth A, AA, ac AAA, ar gyfer gwneud cynnwys gwe yn hygyrch.

**Wardley map**: Techneg strategaeth weledol sy'n lleoli galluoedd yn ôl eu gwerth i ddefnyddwyr a'u haeddfedrwydd esblygiadol, i lywio penderfyniadau adeiladu/prynu a buddsoddi.

**Work in progress (WIP) limit**: Cap ar sawl eitem a gaiff fod mewn cam penodol o lif gwaith ar unwaith, arfer Kanban craidd sy'n gwella llif drwy ddatgelu tagfeydd a chyfyngu ar orbenion gormod o waith cyfochrog.

**WSJF (Weighted Shortest Job First)**: Dull blaenoriaethu sy'n dilyniannu gwaith drwy rannu ei gost oedi â'i hyd amcangyfrifedig, fel bod yr eitemau byrraf, mwyaf sensitif i amser, a gwerth uchaf yn cael eu gwneud yn gyntaf.

## X

**[XSS (Cross-Site Scripting)](https://en.wikipedia.org/wiki/Cross-site_scripting)**: Gwendid gwe lle mae ymosodwr yn chwistrellu sgriptiau maleisus sy'n gweithredu ym mhorwyr defnyddwyr eraill, gan bosibl ddwyn data neu herwgipio sesiynau.

## Y

**[YAGNI (You Aren't Gonna Need It)](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it)**: Egwyddor sy'n cynghori yn erbyn adeiladu swyddogaeth ar sail dyfalu, ar y sail bod anghenion a ragwelir yn aml yn methu â deunyddio ac yn ychwanegu cost a chymhlethdod.

## Z

**[Zero trust](https://en.wikipedia.org/wiki/Zero_trust_security_model)**: Model diogelwch sy'n tybio dim ymddiriedaeth ymhlyg yn seiliedig ar leoliad rhwydwaith ac sy'n gwirio pob cais mynediad yn barhaus yn erbyn hunaniaeth, dyfais, a chyd-destun, gan ddilyn yr arwyddair "peidiwch byth ag ymddiried, gwiriwch bob amser."
