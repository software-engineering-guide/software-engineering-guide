# 9.1 Peirianneg dibynadwyedd safle

## Trosolwg a chymhelliant

Mae [peirianneg dibynadwyedd safle](https://en.wikipedia.org/wiki/Site_reliability_engineering) (SRE) yn cymhwyso arferion peirianneg meddalwedd at redeg systemau cynhyrchu. Yn lle trin gweithrediadau fel gwaith â llaw, wedi'i yrru gan docynnau ac ar wahân i ddatblygu, mae SRE yn trin dibynadwyedd fel problem beirianneg rydych yn ei datrys â chod, mesuriad, ac amcanion gwasanaeth clir. Mae'r syniad craidd, a boblogeiddiwyd gan Google ond sydd bellach yn eang, yn syml: dylai'r bobl sy'n cadw systemau i redeg dreulio'r rhan fwyaf o'u hamser yn adeiladu awtomeiddio a gwella systemau, nid yn diffodd tanau'r un methiannau â llaw dro ar ôl tro.

I dimau mawr, mae hyn o bwys oherwydd bod graddfa'n codi gwerth dibynadwyedd a chost cael pethau'n anghywir fel ei gilydd. Pan fydd un gwasanaeth yn cynnal miliynau o ddefnyddwyr neu filoedd o ddefnyddwyr mewnol, mae awr o amser segur yn golygu refeniw a gollwyd, trafodion a gollwyd, ac ymddiriedaeth wedi'i erydu. Mae gweithrediadau â llaw sy'n gweithio'n iawn i lond dwrn o weinyddwyr yn chwalu o dan gannoedd o wasanaethau a [defnyddio parhaus](https://en.wikipedia.org/wiki/Continuous_deployment). Mae SRE yn rhoi iaith a rennir i chi ar gyfer dibynadwyedd, ffordd o wneud y cyfaddawd rhwng rhyddhau nodweddion a chadw pethau'n sefydlog yn benodol, a ffordd o ddal y llinell honno'n gyson ar draws llawer o dimau.

Mae cyd-destunau menter a llywodraeth yn ychwanegu pwysau pellach. Mae diwydiannau rheoledig fel bancio, gofal iechyd, a gwasanaethau cyhoeddus yn aml yn cario ymrwymiadau argaeledd cyfreithiol neu gontractiol, gofynion archwilio, ac ychydig o oddefgarwch ar gyfer toriadau gwasanaeth sy'n effeithio ar ddinasyddion neu ddiogelwch. Mae gwasanaethau digidol llywodraethol yn fwyfwy yn cyhoeddi eu targedau dibynadwyedd a'u data perfformiad yn agored. Mae SRE yn rhoi ffordd drylwyr, wedi'i seilio ar dystiolaeth i chi ddiffinio beth mae "digon dibynadwy" yn ei olygu, ei fesur yn onest, ac amddiffyn blaenoriaethau peirianneg i arweinwyr a chyrff goruchwylio â data yn hytrach na barn.

*Gweler hefyd:* pennod 9.2 (arsylwadaeth a monitro), pennod 9.3 (rheoli digwyddiadau), a phennod 3.5 (graddadwyedd, perfformiad, a chydnerthedd).

## Egwyddorion allweddol

- **Dibynadwyedd yw'r nodwedd bwysicaf.** Mae system nad yw'n gweithio'n ddiwerth ni waeth faint o nodweddion sydd ganddi, ond nid yw dibynadwyedd perffaith yn gyraeddadwy nac yn werth ei gost.
- **Diffiniwch ddibynadwyedd ag amcanion mesuradwy.** Mae dangosyddion lefel gwasanaeth (SLIs), amcanion (SLOs), a chytundebau (SLAs) yn troi disgwyliadau amwys yn rifau y gall pawb gytuno arnynt.
- **100 y cant yw'r targed anghywir.** Ni all defnyddwyr ddweud y gwahaniaeth rhwng system ddibynadwy iawn ac un berffaith ddibynadwy, felly anelwch at "ddigon dibynadwy" a gwariwch y gyllideb sy'n weddill ar gyflymder.
- **Mae cyllidebau gwall yn alinio cymhellion.** Mae'r bwlch rhwng yr SLO a 100 y cant yn gyllideb ar gyfer risg y mae datblygwyr a gweithredwyr yn ei rhannu, gan ddisodli dadleuon ag arithmetig.
- **Trafferth yw'r gelyn.** Dylid mesur, capio, a dileu'n systematig waith gweithredol ailadroddus, â llaw, y gellir ei awtomeiddio.
- **Awtomeiddiwch yn fwriadol.** Awtomeiddio yw sut mae tîm bach yn gweithredu system fawr; mae buddsoddi ynddo'n weithgaredd peirianneg dosbarth cyntaf.
- **Dysgu di-fai.** Trinir methiannau fel cyfleoedd i wella systemau a phrosesau, nid i gosbi unigolion.

## Argymhellion

### Diffiniwch SLIs, SLOs, ac SLAs yn fwriadol

Dechreuwch o safbwynt y defnyddiwr. Mae **[dangosydd lefel gwasanaeth](https://en.wikipedia.org/wiki/Service-level_indicator)** yn fesur meintiol o ymddygiad gwasanaeth, fel cyfran y ceisiadau a wasanaethwyd mewn llai na 300 milieiliad neu'r gyfran o ymatebion llwyddiannus. Dewiswch nifer fach o SLIs sy'n adlewyrchu bodlonrwydd defnyddwyr yn wirioneddol: mae argaeledd, oedi, cywirdeb, a ffresni'n rhai cyffredin. Mae **[amcan lefel gwasanaeth](https://en.wikipedia.org/wiki/Service-level_objective)** yn werth targed neu ystod ar gyfer SLI, er enghraifft "mae 99.9 y cant o geisiadau'n llwyddo dros ffenestr dreiglol 28-diwrnod." Mae **[cytundeb lefel gwasanaeth](https://en.wikipedia.org/wiki/Service-level_agreement)** yn gontract â chanlyniadau (ad-daliadau, cosbau) ynghlwm wrth lefel a addawyd. Cadwch eich SLOs yn fwy llym na'ch SLAs, fel eich bod yn cael rhybudd cyn i chi dorri ymrwymiad. Cyhoeddwch eich SLOs, eu hadolygu bob chwarter, a'u trin fel dogfennau byw sy'n tynhau neu'n llacio wrth i chi ddysgu.

### Mabwysiadwch gyllidebau gwall a'u gorfodi

Y gyllideb wall yw `100% minws yr SLO`. Os yw'ch SLO yn 99.9 y cant, mae eich cyllideb yn 0.1 y cant o annibynadwyedd fesul ffenestr, tua 43 munud y mis. Gwariwch hi ar risg gynlluniedig: rhyddhau ymosodol, arbrofion, a phrofion methiant rheoledig. Pan fydd y gyllideb yn iach, gall timau ryddhau'n gyflym. Pan fydd yn dod i ben, dylai'r polisi symud blaenoriaethau'n awtomatig tuag at waith dibynadwyedd a rhoi'r gorau i newidiadau risgus nes i'r system adfer. Grym y gyllideb wall yw eich bod yn cytuno arni ymlaen llaw, felly mae'n cymryd yr emosiwn a'r wleidyddiaeth allan o eiliad toriad gwasanaeth.

### Mesurwch a lleihau trafferth

Trafferth yw gwaith gweithredol sy'n â llaw, ailadroddus, y gellir ei awtomeiddio, tactegol, ac sy'n tyfu gam yn gam â'r system. Olrheiniwch y ganran o amser SRE a dreulir ar drafferth a gosodwch nenfwd, yn gyffredin tua 50 y cant, fel bod o leiaf hanner eich amser peirianneg yn mynd tuag at welliannau parhaol. Cadwch gronfa waith o brosiectau lleihau trafferth, blaenoriaethwch yn ôl amlder wedi'i luosi â chost, a dathlwch ladd tasg gyson gymaint â rhyddhau nodwedd newydd. Mae **mandad awtomeiddio** yn gwneud hyn yn benodol: mae unrhyw weithdrefn â llaw rydych yn ei chyflawni mwy na nifer penodedig o weithiau'n dod yn ymgeisydd ar gyfer awtomeiddio neu offer hunanwasanaeth.

### Cynlluniwch gapasiti a rhagolygwch alw

Modelwch eich llwyth disgwyliedig o duedd hanesyddol, lansiadau cynlluniedig, a rhagolygon busnes. Cyfunwch ragolygon twf organig â digwyddiadau untro fel ymgyrchoedd marchnata, terfynau amser treth, neu gyfnodau cofrestru budd-daliadau sydd o bwys mawr mewn llywodraeth. Cadwch le anadlu uwchben y brig, prawf-lwythwch i wirio eich rhagdybiaethau, ac awtomeiddiwch raddio lle gallwch tra'n cadw [cynllun capasiti](https://en.wikipedia.org/wiki/Capacity_planning) wedi'i adolygu gan berson ar gyfer ymrwymiadau mawr. Olrheiniwch amseroedd arwain ar gyfer darparu fel na fydd prinder byth yn eich dal yn ddiarwybod.

### Triniwch ddibynadwyedd fel nodwedd â chost go iawn

Mae pob "naw" ychwanegol o argaeledd fel arfer yn costio llawer mwy mewn dilyffethair, profi, a soffistigedigrwydd gweithredol na'r un o'i flaen. Gwnewch gost y nawiau'n benodol, fel bod perchnogion cynnyrch yn dewis y targed â'u llygaid ar agor. Cynlluniwch ar gyfer dirywiad graenus, fel bod methiannau rhannol yn rhoi gwasanaeth wedi'i leihau yn hytrach na thoriadau llwyr. Buddsoddwch mewn dilyffethair ac ymgymryd dros fethiant mewn cyfrannedd â'r SLO, nid yn gyfartal ar draws pob cydran.

### Dewiswch fodel sefydliadol SRE

Nid oes un strwythur cywir. Mae tîm SRE **canolog** yn rhoi cysondeb, arbenigedd dwfn, ac offer a rennir i chi, ond gall ddod yn dagfa neu'n dip ar gyfer problemau pobl eraill. Mae model **wedi'i ymgorffori** yn gosod peirianwyr SRE y tu mewn i dimau cynnyrch ar gyfer cydweithio agos, ond mae'n peryglu anghysondeb ac ynysigrwydd. Mae llawer o sefydliadau mawr yn defnyddio hybrid: tîm platfform a safonau canolog ynghyd â pheirianwyr dibynadwyedd wedi'u hymgorffori, gyda model ymgysylltu clir sy'n diffinio pryd mae gwasanaeth yn cymhwyso ar gyfer cymorth SRE a pha far parodrwydd cynhyrchu y mae'n rhaid iddo ei glirio yn gyntaf.

## Cyfaddawdau: manteision ac anfanteision

| Penderfyniad | Manteision | Anfanteision |
|---|---|---|
| SLOs llym (mwy o nawiau) | Ymddiriedaeth defnyddwyr uwch, yn bodloni contractau | Cost gynyddol, cyflenwi nodweddion arafach |
| SLOs llac (llai o nawiau) | Rhyddhau cyflymach, cost is | Risg o golli defnyddwyr a chosbau SLA |
| SRE canolog | Cysondeb, arbenigedd a rennir | Tagfeydd, pellter oddi wrth y cynnyrch |
| SRE wedi'i ymgorffori | Cydweithio agos, cyd-destun | Anghysondeb, anodd ei staffio |
| Buddsoddiad awtomeiddio trwm | Yn graddio, yn lleihau trafferth | Cost ymlaen llaw, gall awtomeiddio ei hun fethu |

Mae peirianneg dibynadwyedd yn ymwneud go iawn â gwario adnoddau meidraidd yn ddoeth. Mae mynd ar drywydd naw ychwanegol na all defnyddwyr hyd yn oed ei ganfod yn gwastraffu arian a allai ariannu nodweddion neu ostwng prisiau. Ewch y ffordd arall ac tan-fuddsoddwch mewn system y mae ei methiannau'n achosi niwed go iawn, ac mae hynny'n esgeulus. Mae'r fframwaith cyllideb wall yn bodoli'n union i wneud y cyfaddawd hwn yn weladwy ac yn negodadwy yn hytrach nag ymhlyg ac ymrafaelgar. Mae'r cyfaddawd model sefydliadol yr un mor real: mae'r ateb cywir yn dibynnu ar faint y cwmni, aeddfedrwydd peirianneg, a pha mor unffurf yw eich gwasanaethau.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Pa SLI union sy'n adlewyrchu'r hyn y mae eich defnyddwyr yn ei deimlo mewn gwirionedd, ac a allwch ddangos nad yw'n fetrig gwagedd?** Dewiswch y dangosydd anghywir a bydd pob dangosfwrdd yn edrych yn wyrdd tra bo defnyddwyr yn dioddef, sef y fagl SLI-gwagedd y mae'r bennod hon yn rhybuddio yn ei chylch. Dewch â data go iawn i'r drafodaeth: mesurwch yr un daith defnyddiwr o lwybr cais go iawn (mewngofnodi i ddangosfwrdd, talu i gadarnhad) yn hytrach na CPU gweinydd neu wiriad iechyd cefnfilwr. I dîm mawr, mae un SLI gwael yn lledaenu: mae dwsinau o wasanaethau'n ei etifeddu, mae rhybuddion yn tanio ar y peth anghywir, ac mae'r gyllideb wall yn peidio â golygu unrhyw beth. Mewn lleoliadau menter a llywodraeth lle mae SLA yn cario ad-daliadau neu effaith ddinesig, eich SLI yw'r dystiolaeth rydych yn ei hamddiffyn i archwilwyr, felly mae'n rhaid iddo olrhain yn uniongyrchol at lwyddiant gweladwy i'r defnyddiwr. Os na allwch dynnu llinell o'r rhif at brofiad defnyddiwr, disodlwch y rhif.

2. **Beth mae'n rhaid i wasanaeth ei brofi cyn i'ch tîm SRE ei gymryd ar-alwad, a phwy sy'n dweud na?** Heb far parodrwydd cynhyrchu, mae tîm SRE canolog yn dod yn dip ar gyfer pob gwasanaeth ansefydlog ac yn boddi mewn dyled dechnegol pobl eraill. Ysgrifennwch y meini prawf mynediad i lawr: SLO â pherchennog, llyfrau rhedeg gweithredol, rhybuddion gweithredadwy, lle anadlu capasiti, a llwybr rhyddhau-ac-ôl-droi wedi'i ddangos. I sefydliad mawr, dyma'r model ymgysylltu sy'n atal y tîm dibynadwyedd rhag dod yn dagfa sy'n arafu pawb. Mewn lleoliadau rheoledig, mae'r adolygiad parodrwydd yn dyblu fel rheolaeth y gallwch ei dangos i gyrff goruchwylio. Penderfynwch pwy sy'n dal yr awdurdod i wrthod sefydlu, oherwydd nid yw bar nad oes neb yn ei orfodi'n far, ac mae'r ateb yn newid a yw SRE'n graddio neu'n chwalu o dan boen a etifeddwyd.

3. **Pa mor bell ymlaen llaw ydych chi'n darparu ymlaen llaw ar gyfer eich brig unigol mwyaf rhagweladwy, ac a ydych yn gwybod eich amser arwain darparu?** Mae tybio bod hyblygrwydd cwmwl yn syth a diderfyn yn gwahodd prinderau yn ystod yr union frigau sydd o bwys fwyaf, ac mae'r brigau hynny (terfynau amser treth, ffenestri cofrestru, digwyddiadau gwerthu) yn eiliadau pan fo methiant fwyaf gweladwy a drutaf. Dewch â'r rhifau: llwyth brig hanesyddol, twf rhagfynegol, y lluosydd rydych yn prawf-lwytho iddo, a'r amser arwain go iawn i gaffael capasiti wedi'i gadw mawr neu enghreifftiau arbenigol. I wasanaethau tymhorol llywodraethol, gall y brig fod sawl gwaith y llwyth arferol ac mae'n wleidyddol amlwg, felly mae darparu ymlaen llaw wythnosau ymlaen yn curo gobeithio y bydd hunan-raddio'n dal i fyny. Dylai'r ateb osod calendr penodol: pryd rydych yn prawf-lwytho, pryd rydych yn cloi capasiti, a phwy sy'n berchen ar y penderfyniad i fynd.

4. **Pan fydd eich cyllideb wall yn dod i ben, beth sy'n digwydd mewn gwirionedd, a phwy sydd â'r sefyll i'w gorfodi?** Mae cyllideb wall na weithredir arni byth pan gaiff ei disbyddu'n addurn yn unig, ac eiliad toriad gwasanaeth yw'r amser gwaethaf i drafod y polisi o'r cychwyn. Mae'r tyniad cystadleuol yn real: bydd lansiad ymrwymedig, terfyn amser refeniw, neu gyhoeddiad cyhoeddus yn gwasgu'n galed yn erbyn rhewi newidiadau risgus. Dewch â data cyfradd llosgi, testun y polisi y cytunwyd arno ymlaen llaw, a chofnod o'r ychydig weithiau diwethaf y torrwyd y gyllideb, fel y gallwch weld a arhosodd y rhew mewn gwirionedd. I dîm mawr, dim ond os yw pob grŵp yn etifeddu'r un gorfodaeth y mae'r gyllideb yn alinio cymhellion, felly penderfynwch ymlaen llaw pwy sy'n awdurdodi diystyriad a sut caiff yr eithriad hwnnw ei gofnodi. Mewn lleoliadau menter a llywodraeth lle mae SLA yn cario cosbau neu effaith ddinesig, mae'r llwybr diystyru'n dod yn arteffact archwilio, felly enwch y perchennog atebol nawr yn hytrach na byrfyfyrio pan fydd y gyllideb eisoes wedi mynd.

5. **Pa gyfran o wythnos eich tîm SRE sy'n drafferth, ac a yw hynny'n rhif wedi'i fesur neu'n deimlad?** Mae trafferth nad oes neb yn ei gyfrif yn ehangu'n dawel nes bod y tîm yn treulio'i holl amser yn diffodd tanau a dim byd yn adeiladu gwelliannau parhaol, sef union y fagl y mae SRE'n bodoli i ddianc rhagddi. Y tyndra yw bod mesur trafferth ei hun yn waith, ac mae peirianwyr o dan bwysau terfyn amser yn gwrthsefyll cofnodi lle mae eu horiau'n mynd. Dewch â sampl onest: wythnos neu ddwy o amser wedi'i olrhain yn erbyn diffiniad a rennir o drafferth (â llaw, ailadroddus, y gellir ei awtomeiddio, tactegol, ac yn graddio gyda'r system), ynghyd â chronfa waith o brosiectau awtomeiddio wedi'u rhestru yn ôl amlder wedi'i luosi â chost. I sefydliad mawr, dim ond os caiff ei adrodd a'i amddiffyn dîm wrth dîm y mae nenfwd 50 y cant yn golygu rhywbeth, felly cytunwch pwy sy'n adolygu'r rhif a beth sy'n digwydd pan fydd tîm yn ei dorri. Mewn cyd-destunau rheoledig a llywodraethol, mae capio trafferth yn rhyddhau arbenigwyr prin ar gyfer y gwaith rheolaeth ac archwilio y mae gweithrediadau â llaw yn eu gwthio allan, felly triniwch y ffigwr trafferth fel signal capasiti y dylai arweinwyr ei weld.

6. **Pa fodel sefydliadol SRE ydych chi'n ei redeg, a pha dystiolaeth fyddai'n dweud wrthych ei fod wedi peidio â ffitio?** Mae tîm canolog yn rhoi cysondeb ac offer a rennir ond gall ddod yn dagfa; mae model wedi'i ymgorffori'n rhoi cyd-destun ond yn crwydro i mewn i anghysondeb; mae angen model ymgysylltu clir ar yr hybrid y mae'r rhan fwyaf o sefydliadau mawr yn setlo arno neu mae'n etifeddu gwendidau'r ddau. Dewch â'r signalau sy'n datgelu straen: pa mor hir mae gwasanaethau'n aros am gymorth SRE, faint mae arfer dibynadwyedd yn amrywio rhwng timau, ac a yw peirianwyr wedi'u hymgorffori'n teimlo eu bod wedi'u torri i ffwrdd oddi wrth gymuned broffesiynol. Mae'r ateb cywir yn dibynnu ar faint y cwmni, aeddfedrwydd peirianneg, a pha mor unffurf yw eich gwasanaethau, felly ail-ymwelwch ag ef wrth i'r rheini newid yn hytrach na thrin y dewis cyntaf fel un parhaol. I fenter neu gorff llywodraethol â llawer o dimau a gofynion unffurfiaeth llym, mae grŵp safonau-a-phlatfform canolog ynghyd â pheirianwyr dibynadwyedd wedi'u hymgorffori fel arfer yn cydbwyso cysondeb yn erbyn cyd-destun lleol, ond dim ond os yw'r model ymgysylltu a'r bar parodrwydd cynhyrchu wedi'u hysgrifennu i lawr a bod rhywun yn berchen arnynt.

## Trwy lens sector

**Cwmni newydd.** Gyda llond dwrn o beirianwyr a dim lle anadlu ar gyfer tîm dibynadwyedd pwrpasol, dewiswch un SLO ar y daith defnyddiwr sydd bwysicaf a rhannwch ar-alwad ar draws y tîm cyfan. Pwyswch ar wasanaethau a reolir eich darparwr cwmwl a monitro adeiledig yn hytrach nag adeiladu seilwaith arsylwadaeth, ac ysgrifennwch ôl-drafodion byr mewn dogfen a rennir fel bod atgyweiriadau'n glynu. Mae cyflymder o bwys mwy na phroses yma: mae SLO llac rydych yn ei orfodi mewn gwirionedd yn curo un cywrain nad oes neb yn ei wylio.

**Busnes bach.** Heb arbenigwr i redeg dibynadwyedd, triniwch ef fel disgyblaeth rydych yn prynu i mewn iddi drwy eich platfform: monitro amser gweithredu wedi'i westeio, cronfeydd data wedi'u rheoli, ac offer tudalen statws yn lle stac pwrpasol. Gosodwch un neu ddau SLO wedi'u clymu wrth y trafodion sy'n talu'r biliau, a phenderfynwch yn onest pa fethiannau fyddai'n costio cwsmer i chi. Prynwch gydnerthedd lle mae'n rhatach na'i adeiladu, a chadwch y baich gweithredol yn ddigon ysgafn fel y gall eich peirianwyr presennol ei gario ochr yn ochr â gwaith nodweddion.

**Menter.** Yr her yw cysondeb ar draws llawer o dimau: geirfa SLO a rennir, polisi cyllideb wall cyffredin, a bar parodrwydd cynhyrchu y mae pob gwasanaeth yn ei glirio cyn i SRE ei gymryd ar-alwad. Mae grŵp platfform-a-safonau canolog ynghyd â pheirianwyr dibynadwyedd wedi'u hymgorffori'n cadw arfer yn unffurf heb ddod yn dagfa, ac mae angen i lywodraethu adrodd a gorfodi cyllidebau gwall yr un ffordd ym mhobman. Cyllidebwch y seilwaith arsylwadaeth a'r buddsoddiad awtomeiddio'n benodol, a rheolwch ddibynadwyedd fel portffolio â metrigau y gall arweinwyr eu gweld.

**Llywodraeth.** Mae gwasanaethau cyhoeddus yn aml yn cario targedau argaeledd a gyhoeddwyd, ymrwymiadau statudol, a rhwymedigaethau archwilio, felly mae penderfyniadau SLO a chyllideb wall yn dod yn gofnodion rydych yn eu hamddiffyn i gyrff goruchwylio. Gall rheolau caffael gyfyngu pa fonitro a lletya y gallwch eu defnyddio, ac mae disgwyliadau tryloywder yn eich gwthio i gyhoeddi data dibynadwyedd ar ddangosfwrdd statws cyhoeddus. Cynlluniwch ar gyfer brigau tymhorol eithafol fel terfynau amser treth a ffenestri cofrestru budd-daliadau wythnosau ymlaen llaw, a chadwch ddiwylliant ôl-drafod di-fai fel bod methiannau cyhoeddus yn gyrru gwelliant system yn hytrach na bai unigol.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd deg person yn rhedeg un ap gwe ac yn rhannu ar-alwad ar draws tri pheiriannydd. Yn hytrach nag adeiladu tîm dibynadwyedd na all ei fforddio, mae'n dewis un SLO ystyrlon: 99.5 y cant o lwyddiant ar y llif mewngofnodi-i-ddangosfwrdd, wedi'i fesur o geisiadau defnyddwyr go iawn. Pan fydd API trydydd parti anghyson yn dechrau bwyta'r gyllideb honno, mae'r tîm yn treulio dydd Gwener yn ychwanegu ailgais a chatsh yn lle rhyddhau'r nodwedd nesaf, yna'n ysgrifennu ôl-drafod dau baragraff mewn dogfen a rennir fel bod yr atgyweiriad yn glynu.

**Menter.** Mae cwmni taliadau byd-eang yn gosod SLO argaeledd o 99.99 y cant ar gyfer ei API trafodion, sy'n rhoi cyllideb wall o tua phedwar munud y mis. Mae tîm platfform SRE canolog yn berchen ar [arsylwadaeth](https://en.wikipedia.org/wiki/Observability_(software)) a rennir, offer digwyddiadau, a'r polisi cyllideb wall, tra bo peirianwyr dibynadwyedd wedi'u hymgorffori'n gweithio y tu mewn i bob grŵp cynnyrch. Pan fydd nodwedd canfod twyll newydd yn llosgi hanner y gyllideb fisol mewn wythnos, mae'r polisi y cytunwyd arno ymlaen llaw yn rhewi rhyddhau nad ydynt yn hanfodol nes bod gwaith dibynadwyedd yn adfer lle anadlu. Mae uwch-swyddogion yn derbyn hyn heb ddadlau, oherwydd fe wnaethant gadarnhau'r polisi ymlaen llaw.

**Llywodraeth.** Mae awdurdod treth cenedlaethol yn rhedeg gwasanaeth ffeilio ar-lein â brigau tymhorol eithafol o amgylch y terfyn amser blynyddol. Mae ei dîm SRE yn rhagfynegi galw o flynyddoedd blaenorol ynghyd â newidiadau poblogaeth a pholisi, yn prawf-lwytho i sawl gwaith y brig arferol, ac yn darparu capasiti ymlaen llaw wythnosau ynghynt. Mae SLOs wynebu'r cyhoedd ar gyfer argaeledd ac oedi tudalen yn mynd i fyny ar ddangosfwrdd statws. Mae diwylliant [ôl-drafod](https://en.wikipedia.org/wiki/Postmortem_documentation) di-fai (adolygu methiannau i wella systemau yn hytrach na phriodoli bai unigol) a mandad awtomeiddio'n torri'n gyson yr ymyriadau â llaw a arferai ddominyddu tymor ffeilio, gan ryddhau staff i wella'r system yn hytrach na'i nyrsio drwy bob terfyn amser.

## Achos busnes: cymhellion, ROI, a TCO

Daw'r enillion ar SRE o dair ffynhonnell: amser segur a osgowyd, llai o lafur gweithredol, a chyflenwi diogel cyflymach. Gall amser segur ar gyfer gwasanaeth mawr gostio miloedd i filiynau'r awr mewn refeniw a gollwyd, cosbau, ac adferiad, felly mae hyd yn oed enillion dibynadwyedd cymedrol yn talu am dîm yn gyflym. Mae lleihau trafferth yn troi cost â llaw gyson yn fuddsoddiad awtomeiddio untro, felly mae cyfanswm cost perchnogaeth yn gostwng wrth i raddfa dyfu yn hytrach na dringo gam yn gam ag ef. Mae cyllidebau gwall yn caniatáu i'r busnes ryddhau'n gyflymach pan fydd dibynadwyedd yn iach, gan ddal gwerth nodweddion y byddai gweithrediadau gorofalus yn ei adael ar y bwrdd.

Mae cost mabwysiadu'n real. Mae angen peirianwyr medrus ar SRE, seilwaith arsylwadaeth, a newid diwylliannol sy'n cystadlu â therfynau amser nodweddion. Ond mae cost peidio â mabwysiadu'n uwch ar raddfa: pennaeth-rifau gweithredol diderfyn, toriadau gwasanaeth annisgwyl, llosgi a threuliant staff, a difrod enw da sy'n anodd ei feintioli ond yn hawdd ei ddioddef. I wneud yr achos i arweinwyr, fframiwch SRE fel rheolaeth risg â dychweliadau mesuradwy. Cyflwynwch gost gyfredol digwyddiadau a gweithrediadau â llaw, y targedau SLO wedi'u clymu wrth ymrwymiadau busnes, a'r lleihad rhagfynegol yn y ddau. Angorwch y ddadl ar y gyllideb wall fel arf llywodraethu sy'n rhoi lifer i arweinwyr dros y cyfaddawd dibynadwyedd-yn-erbyn-cyflymder.

## Gwrth-batrymau a phethau i'w hosgoi

- **SRE fel gweithrediadau wedi'u hail-frandio.** Nid yw ailenwi tîm gweithrediadau heb yr amser peirianneg, mandad awtomeiddio, ac awdurdod i wrthsefyll yn newid dim.
- **Anelu at 100 y cant.** Mae mynd ar drywydd dibynadwyedd perffaith yn gwastraffu arian ac yn rhwystro cyflenwi ar gyfer enillion na all defnyddwyr eu canfod.
- **SLIs gwagedd.** Mae mesur CPU gweinydd yn lle llwyddiant gweladwy i'r defnyddiwr yn rhoi rhifau sy'n edrych yn dda tra bo defnyddwyr yn dioddef.
- **Cyllidebau gwall heb ddannedd.** Mae cyllideb na chaiff ei gorfodi byth pan gaiff ei disbyddu'n addurn yn unig.
- **Trafferth heb fesuriad.** Os na fyddwch yn olrhain trafferth, mae'n bwyta'r tîm yn dawel nes na fydd unrhyw waith gwella'n digwydd.
- **SRE fel dip.** Mae timau canolog sy'n etifeddu pob gwasanaeth ansefydlog heb far parodrwydd yn boddi mewn dyled dechnegol pobl eraill.
- **Anwybyddu amseroedd arwain capasiti.** Mae tybio bod hyblygrwydd cwmwl yn syth a diderfyn yn gwahodd prinderau yn ystod yr union frigau sydd o bwys fwyaf.

## Model aeddfedrwydd

**Lefel 1, Cychwyn.** Mae gweithrediadau'n â llaw ac yn adweithiol. Nid oes SLOs ffurfiol, mae dibynadwyedd yn fater o farn, ac mae'r un digwyddiadau'n ailddigwydd tra bo diffodd tanau'n dominyddu. Mae unrhyw awtomeiddio'n achlysurol, ac nid oes neb yn berchen ar ddibynadwyedd fel pryder peirianneg.

**Lefel 2, Datblygu.** Mae gan rai gwasanaethau SLIs ac SLOs sylfaenol a monitro a rhybuddio elfennol, ond mae'r arfer yn amrywio'n eang rhwng timau. Cydnabyddir trafferth ac eto ni chaiff ei fesur, mae awtomeiddio'n achlysurol, a digwydd ôl-drafodion yn anghyson. Mae dibynadwyedd yn gwella yn y pocedi lle mae unigolion yn ei wthio, nid am fod y sefydliad yn ei fynnu.

**Lefel 3, Safoni.** Mae SLIs, SLOs, a pholisi cyllideb wall wedi'u dogfennu a'u cymhwyso'n gyson ar draws timau. Mae trafferth wedi'i ddiffinio a'i olrhain, mae cynllunio capasiti'n rwtin, mae model ymgysylltu SRE ag adolygiadau parodrwydd cynhyrchu'n bodoli, ac mae awtomeiddio'n ffrwd waith a ariennir yn hytrach na phrosiect ochr. Mae arfer dibynadwyedd wedi'i ysgrifennu i lawr a'i orfodi ledled y sefydliad.

**Lefel 4, Rheoli.** Mesurir a rheolir y rhaglen ddibynadwyedd â data yn erbyn llinellau sylfaen. Olrheinir cyfradd llosgi cyllideb wall, canran trafferth, cyrhaeddiad SLO, amser cymedrig i adfer, ac amseroedd arwain darparu fel metrigau, wedi'u hadolygu ar rythm sefydlog, ac wedi'u defnyddio i ddal timau i'w targedau. Mae torri cyllideb yn sbarduno'r rhew y cytunwyd arno, rhagfynegir capasiti yn erbyn modelau galw, ac mae pob penderfyniad mynd neu beidio â mynd yn seiliedig ar dystiolaeth yn hytrach na barn.

**Lefel 5, Cydgordio.** Mae peirianneg dibynadwyedd wedi'i integreiddio ar draws y sefydliad ac yn cael ei gwella'n barhaus. Mae polisi cyllideb wall wedi'i awtomeiddio a'i barchu ym mhobman, mae'r rhan fwyaf o weithrediadau'n hunanwasanaeth, darperir capasiti'n rhagweithiol, ac mae data dibynadwyedd yn gyrru cyfaddawdau addasol rhwng cyflymder a sefydlogrwydd. Mae'r sefydliad yn arferol yn ail-gwmpasu SLOs, yn ymddeol trafferth, ac yn ail-gydbwyso buddsoddiad dibynadwyedd wrth i'r darlun busnes a risg newid.

## Syniadau i'w trafod

- Sut dylai sefydliad osod ei SLOs cyntaf pan nad oes ganddo ddata dibynadwyedd hanesyddol i'w hangori?
- Pan fydd y gyllideb wall wedi'i disbyddu ond lansiad mawr wedi'i ymrwymo, pwy sydd ag awdurdod i ddiystyru'r rhew, a sut caiff y penderfyniad hwnnw ei gofnodi?
- A yw model SRE canolog, wedi'i ymgorffori, neu hybrid yn iawn i'ch sefydliad, a beth fyddai'n sbarduno newid?
- Sut ydych yn gwerthfawrogi naw ychwanegol o argaeledd yn erbyn y nodweddion y gallai'r un buddsoddiad eu hariannu?
- Beth sy'n cyfrif fel trafferth yn eich cyd-destun chi, a ble mae'r llinell rhwng barn â llaw werthfawr ac ailadrodd y gellir ei ddileu?
- Sut dylai targedau dibynadwyedd wahaniaethu rhwng gwasanaethau llywodraethol sy'n wynebu dinasyddion ac offer menter mewnol?

## Casgliadau allweddol

- Mae SRE yn cymhwyso peirianneg meddalwedd at weithrediadau, gan drin dibynadwyedd fel nodwedd fesuradwy, ariannadwy.
- Mae SLIs, SLOs, ac SLAs yn troi dibynadwyedd o farn yn rifau y cytunwyd arnynt; cadwch SLOs yn fwy llym na SLAs.
- Mae'r gyllideb wall yn alinio datblygwyr a gweithredwyr drwy wneud y cyfaddawd dibynadwyedd-yn-erbyn-cyflymder yn benodol ac wedi'i negodi ymlaen llaw.
- Mesurwch a chapiwch drafferth, a thriniwch awtomeiddio fel peirianneg dosbarth cyntaf fel bod gweithrediadau'n graddio is-linol.
- Cynlluniwch gapasiti o ragolygon galw a pharchwch amseroedd arwain darparu, yn enwedig ar gyfer brigau tymhorol.
- Dewiswch fodel sefydliadol SRE yn fwriadol a diffiniwch far ymgysylltu a pharodrwydd cynhyrchu clir.

## Cyfeiriadau a darllen pellach

- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy, *Site Reliability Engineering: How Google Runs Production Systems*
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne, *The Site Reliability Workbook: Practical Ways to Implement SRE*
- David N. Blank-Edelman (editor), *Seeking SRE: Conversations About Running Production Systems at Scale*
- Thomas A. Limoncelli, Strata R. Chalup, Christina J. Hogan, *The Practice of Cloud System Administration*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
