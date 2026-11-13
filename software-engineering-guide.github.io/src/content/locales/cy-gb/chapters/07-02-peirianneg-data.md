# 7.2 Peirianneg data

## Trosolwg a chymhelliant

Mae [peirianneg data](https://en.wikipedia.org/wiki/Data_engineering) yn ddisgyblaeth adeiladu a gweithredu'r piblinellau a'r platfformau sy'n symud data o'r man lle caiff ei gynhyrchu i'r man lle mae'n creu gwerth. Mae'n cwmpasu mewnlifiad o systemau ffynhonnell, trawsnewid i ffurfiau glân a modelwyd, storio mewn fformatau costeffeithiol, cerdorfa'r llif cyfan, a'r arferion dibynadwyedd sy'n cadw'r cyfan yn ddibynadwy. Os yw strategaeth data'n penderfynu pa ddata a ddylai fodoli a phwy sy'n berchen arno, peirianneg data yw'r plymwaith a'r peirianwaith sy'n gwneud iddo lifo.

I dimau mawr, mae'r ddisgyblaeth hon yn sylfaenol. Mae dadansoddeg, [deallusrwydd busnes](https://en.wikipedia.org/wiki/Business_intelligence), arbrofi cynnyrch, [dysgu peiriant](https://en.wikipedia.org/wiki/Machine_learning), ac adrodd rheoleiddiol i gyd yn eistedd i lawr yr afon o biblinellau data. Pan fo'r piblinellau hynny'n fregus, yn araf, neu'n dywyll, mae pob swyddogaeth ddibynnol yn dioddef. Mae dangosfyrddau'n dangos rhifau hen. Mae modelau'n hyfforddi ar nodweddion llygredig. Ni all archwilwyr ailadeiladu sut y cynhyrchwyd ffigur. Ar raddfa menter a llywodraethol, mae piblinellau'n prosesu biliynau o gofnodion ar draws llawer o systemau ffynhonnell, a gall un methiant tawel wthio data anghywir i mewn i benderfyniadau, taliadau, neu ystadegau cyhoeddus.

Mae'r maes wedi tyfu o sgriptiau pwrpasol ac offer [ETL (echdynnu, trawsnewid, llwytho)](https://en.wikipedia.org/wiki/Extract,_transform,_load) monolithig i mewn i'r pentwr data modern: cydrannau modiwlaidd, yn bennaf yn seiliedig ar SQL ar gyfer mewnlifiad, trawsnewid, cerdorfa, a storio, wedi'u cysylltu gan fformatau agored. Mae'r modiwlaredd hon yn rhodd ac yn drap fel ei gilydd. Mae'n eich galluogi i gydosod y teclynnau gorau yn eu dosbarth, ond heb ddisgyblaeth beirianneg mae'n cynhyrchu lledaeniad o swyddi heb eu dogfennu, heb eu profi. Mae'r bennod hon yn ymdrin â'r arferion sy'n cadw piblinellau'n idempotent, yn brofadwy, yn arsylwadwy, ac yn fforddiadwy ar raddfa.

## Egwyddorion allweddol

- Mae piblinellau'n feddalwedd ac yn haeddu rheolaeth fersiynau, profi, adolygu, a CI/CD.
- Ffafriwch drawsnewidiadau idempotent, atgynyrchadwy y gellir eu hailredeg yn ddiogel.
- Gwnewch lifau data'n arsylwadwy: caiff ffresni, cyfaint, sgema, ac ansawdd eu monitro.
- Modelwch ddata'n fwriadol ar gyfer ei ddefnyddwyr yn hytrach na thipio tablau amrwd.
- Dewiswch swp neu ffrydio yn seiliedig ar wir anghenion oedi, nid newydd-deb.
- Optimeiddiwch fformat storio, rhaniad, a chost cyfrifiadura fel pryderon dosbarth cyntaf.
- Gwahanwch fewnlifiad, trawsnewid, a gwasanaethu fel y gall pob un esblygu'n annibynnol.
- Methwch yn uchel ac yn gynnar; mae piblinell wedi torri'n fwy diogel na data anghywir yn dawel.

## Argymhellion

### Dewis ETL neu ELT yn fwriadol

Mae ETL yn trawsnewid data cyn ei lwytho i mewn i'r cyrchfan. Mae [ELT (echdynnu, llwytho, trawsnewid)](https://en.wikipedia.org/wiki/Extract,_load,_transform) yn llwytho data amrwd yn gyntaf ac yn ei drawsnewid y tu mewn i warws neu lyn-warws pwerus. Mae platfformau cwmwl modern wedi gwneud ELT yn ddiofyn, gan fod storio'n rhad a chyfrifiadura'n elastig, ac mae cadw data amrwd yn eich galluogi i ailbrosesu pan fydd rhesymeg yn newid neu fygiau'n ymddangos. Ffafriwch ELT ar gyfer llwythi gwaith dadansoddeg: glaniwch ddata amrwd, di-newid, yna adeiladwch drawsnewidiadau haenog ar ei ben. Cadwch drawsnewid cyn-llwytho ar gyfer achosion lle mae preifatrwydd, cost, neu gyfyngiadau contractiol yn mynnu glanhau neu hidlo cyn i'r data lanio.

### Dylunio piblinellau swp a ffrydio ar gyfer eu hanghenion oedi

Gwasanaethir y rhan fwyaf o anghenion dadansoddeg yn dda gan biblinellau swp wedi'u hamserlennu, sy'n symlach i resymu drostynt, eu profi, a'u hôl-lenwi. Estynnwch am ffrydio dim ond pan fo'r busnes wir angen data oedi isel: canfod twyll, rhybuddio gweithredol, personoli amser-real. Mae ffrydio'n ychwanegu cymhlethdod gwirioneddol ynghylch trefnu, semanteg union-unwaith, data sy'n cyrraedd yn hwyr, a rheoli cyflwr. Lle mae angen y ddau arnoch, ystyriwch benseiernïaethau sy'n uno rhesymeg swp a ffrydio yn hytrach na chynnal dau god-sail gwahanol. Byddwch yn onest am eich gofynion oedi. Mae "amser-real" yn aml yn ddymuniad heb ei archwilio sy'n dyblu eich cost.

### Cerdorfa gyda dibyniaethau penodol

Defnyddiwch gerdorfäwr i fynegi piblinellau fel [graffiau acyclig cyfeiriedig (DAGs)](https://en.wikipedia.org/wiki/Directed_acyclic_graph) o dasgau â dibyniaethau, ailgeisiadau, ac amserlennu penodol. Mae hyn yn rhoi gwelededd i chi i mewn i beth a redodd, beth a fethodd, a beth sydd wedi'i rwystro, ynghyd â'r gallu i ôl-lenwi ac ailredeg yn benderfynadwy. Seiliwch ddibyniaethau ar argaeledd data, nid dim ond amser cloc, fel bod swyddi i lawr yr afon yn aros am ddata i fyny'r afon yn hytrach na thanio ar ddyfaliad. Cadwch resymeg cerdorfa mewn rheolaeth fersiynau, a thriniwch newidiadau DAG fel newidiadau cod.

### Modelu data ar gyfer defnydd

Anaml y mae tablau amrwd yn addas i ddadansoddwyr. Cymhwyswch [fodelu dimensiynol](https://en.wikipedia.org/wiki/Dimensional_modeling), sy'n trefnu ffeithiau a dimensiynau cydymffurfiol mewn [sgemâu seren](https://en.wikipedia.org/wiki/Star_schema), lle mae angen dadansoddeg lywodraethedig, ailddefnyddiadwy, hunanwasanaeth arnoch. Gall tablau eang, di-normaleiddiedig ("un tabl mawr") berfformio'n well ar gyfer patrymau ymholi penodol ac maent yn symlach i rai defnyddwyr, ar draul dyblygu a hyblygrwydd. Haenwch eich trawsnewidiadau: haen lwyfannu amrwd, haen graidd lân a chydymffurfiol, a marchnadoedd sy'n wynebu defnyddwyr. Mae'r gwahaniad hwn yn eich galluogi i drwsio rhesymeg mewn un lle, ac mae'n galluogi defnyddwyr i ddibynnu ar ryngwynebau sefydlog.

### Gwneud piblinellau'n idempotent ac yn brofadwy

Dyluniwch drawsnewidiadau fel bod eu hailredeg yn cynhyrchu'r un canlyniad, yn hytrach na dyblygu neu lygru data, er enghraifft drwy ddefnyddio uwchosodiadau penderfynadwy wedi'u hallweddu ar ddynodwyr busnes a phatrymau trosysgrifo rhaniad. Ysgrifennwch brofion ar sawl lefel: profion uned ar gyfer rhesymeg trawsnewid, profion sgema, a phrofion data sy'n honni disgwyliadau fel uniciaeth, allweddi di-nwl, cyfanrwydd cyfeiriol, ac amrediadau gwerth derbyniol. Rhedwch y rhain mewn CI, fel bod newid gwael yn cael ei ddal cyn iddo gyrraedd data cynhyrchiad.

### Offeryna arsylwadwyedd a dibynadwyedd

Monitrwch bedwar signal craidd iechyd data: ffresni (a yw'n gyfredol), cyfaint (a yw cyfrif rhesi o fewn yr amrediad disgwyliedig), sgema (a yw'r strwythur wedi newid yn annisgwyl), a dosraniad (a yw gwerthoedd wedi gwyro'n anomalaidd). Rhybuddiwch ar dorriadau, a'u llwybro at y tîm perchen. Cadwch lyfrau rhedeg, cylchdroeon galwad-ar-ddyletswydd, ac ôl-drafodaethau di-fai ar gyfer digwyddiadau data, yn union fel y byddech ar gyfer gwasanaethau. Traciwch linach, fel pan fydd rhywbeth yn torri, y gallwch weld yr effaith i lawr yr afon ar unwaith.

### Optimeiddio storio a chost

Defnyddiwch fformatau agored colofnol fel Parquet, neu fformatau tabl agored sy'n cefnogi esblygiad sgema, teithio amser, a diweddariadau effeithlon. Rhannwch ddata yn ôl y colofnau rydych yn hidlo arnynt fwyaf, dyddiad fel arfer, ac osgowch amlhad o ffeiliau bach drwy gywasgu. Gwahanwch ddata poeth ac oer â storio haenog a pholisïau cylchred oes. Monitrwch wariant cyfrifiadura fesul piblinell a fesul ymholiad. Fel arfer daw costau afreolus o sganiau llawn, rhaniadau ar goll, ac ailbrosesu heb derfyn. Trinwch gost fel metrig â pherchnogion, nid syrpreis ar y bil misol.

## Cyfaddawdau: manteision ac anfanteision

| Dewis | Manteision | Anfanteision | Ffit gorau |
|---|---|---|---|
| ELT (trawsnewid yn ei le) | Yn cadw data amrwd, storio rhad, ailbrosesadwy | Ôl troed storio mawr, angen llywodraethu | Dadansoddeg cwmwl |
| ETL (trawsnewid cyn llwytho) | Yn rheoli cost, yn hidlo data sensitif yn gynnar | Yn colli data amrwd, yn anos ei ailbrosesu | Llwythi rheoledig neu gyfyngedig |
| Swp | Syml, profadwy, hawdd ei ôl-lenwi | Oedi uwch | Y rhan fwyaf o ddadansoddeg |
| Ffrydio | Oedi isel, ymateb amser-real | Cymhleth, costus, anodd ei brofi | Twyll, rhybuddio gweithrediadau |
| Sgema seren | Llywodraethedig, ailddefnyddiadwy, cyfeillgar i hunanwasanaeth | Ymdrech fodelu ymlaen llaw | BI a rennir |
| Tabl eang | Cyflym ar gyfer ymholiadau hysbys, syml | Dyblygu, llai hyblyg | Defnydd perfformiad-uchel cul |

Y cyfaddawd amlycaf yw symlrwydd yn erbyn oedi a hyblygrwydd. Mae swp ac ELT gyda sgemâu seren haenog yn rhoi system brofadwy, ôl-lenwadwy, wedi'i deall yn dda sy'n gwasanaethu'r rhan fwyaf o anghenion yn fforddiadwy. Mae dyluniadau ffrydio, amser-real, a hynod ddi-normaleiddiedig yn prynu cyflymder a pherfformiad penodol, ond ar gost serth mewn cymhlethdod gweithredol ac anhawster profi. Mabwysiadwch gymhlethdod dim ond lle mae gofyniad busnes diriaethol yn talu amdano, a chadwch y llwybr syml fel eich diofyn.

## Cwestiynau i'w trafod gyda'ch tîm

1. **A ydych wedi dewis ELT dros ETL yn fwriadol, ac a ydych yn cadw data amrwd, di-newid fel y gallwch ailbrosesu pan fydd rhesymeg yn newid neu fygiau'n ymddangos?** Diofyn y bennod yw ELT: glaniwch ddata amrwd yn rhad, yna adeiladwch drawsnewidiadau haenog, gan fod cadw data amrwd yn eich galluogi i ailredeg popeth pan fydd rheol yn newid neu fyg yn ymddangos wythnosau'n ddiweddarach. Mae dileu data amrwd yn cau'r opsiwn hwnnw ac yn fagl gyffredin, boenus. Mae'r achos cystadleuol dros ETL yn wirioneddol mewn llwythi rheoledig neu gyfyngedig, lle mae preifatrwydd, cost, neu delerau contract yn mynnu hidlo neu fygu cyn i ddata lanio. Dewch â thystiolaeth: pa mor aml y bu angen i chi ailbrosesu hanes, a beth oedd y gost pan na allech chi? Ar gyfer piblinell lywodraethol neu fenter y mae'n rhaid iddi olrhain unrhyw ffigur i'w ffynhonnell, mae cofnodion amrwd di-newid hefyd yn ofyniad archwiliadwyedd, felly mae'r ateb yn llywio eich polisi storio a'ch amddiffynadwyedd cyfreithiol fel ei gilydd.

2. **Pa rai o'r pedwar signal iechyd data rydych chi'n eu monitro go iawn, a phwy sy'n cael ei alw pan fydd un yn torri?** Mae'r bennod yn enwi pedwar signal sy'n werth eu gwylio: ffresni, cyfaint, sgema, a dosraniad. Nid yw llawer o dimau'n monitro'r un ohonynt ac yn dysgu am fethiannau gan weithredwr yn syllu ar ddangosfwrdd hen, sef y synhwyrydd gwaethaf posibl. Ar raddfa menter a llywodraethol, gall un methiant tawel wthio data anghywir i mewn i daliadau, adroddiadau, neu ystadegau cyhoeddus, felly mesurir cost canfod hwyr mewn ymddiriedaeth ac arian, nid dim ond ailwaith. Dewch â'ch amser cymedrig gwirioneddol i ganfod ac enw pwy bynnag sy'n dod o hyd i ddigwyddiadau gyntaf ar hyn o bryd. Os yw'r ateb yn "ddefnyddiwr," mae angen i chi lwybro rhybuddion at y tîm perchen ynghyd â llyfrau rhedeg ac ôl-drafodaethau di-fai, gan drin digwyddiadau data yn union fel terfynau gwasanaeth.

3. **A yw eich dadansoddwyr yn defnyddio marchnadoedd wedi'u modelu, wedi'u profi, ynteu ydych chi'n tipio tablau amrwd arnynt a'i alw'n hunanwasanaeth?** Mae'r bennod yn uniongyrchol: anaml y mae tablau amrwd yn addas i ddadansoddwyr, ac mae haenu trawsnewidiadau i mewn i haen lwyfannu amrwd, craidd cydymffurfiol, a marchnadoedd sy'n wynebu defnyddwyr yn eich galluogi i drwsio rhesymeg unwaith a rhoi rhyngwynebau sefydlog i ddefnyddwyr. Y tyniad cystadleuol yw cyflymder, gan fod modelu gyda sgemâu seren neu dablau eang bwriadol yn costio ymdrech ymlaen llaw ac mae'n demtasiwn ei hepgor. Ond mae tipio data amrwd yn gwthio cost modelu ar bob dadansoddwr yn ailadroddus, gan gynhyrchu rhifau gwahanol ac oriau wedi'u gwastraffu. Dewch â signal: pa gyfran o amser dadansoddwr sy'n mynd tuag at ailffurfio data amrwd, a faint o dimau sydd wedi ailadeiladu'r un uniadau. Os yw'r rhif yn uchel, buddsoddwch mewn haen graidd cydymffurfiol fel bod defnyddwyr yn dibynnu ar ryngwynebau profedig, ailddefnyddiadwy yn lle eu hailddyfeisio.

4. **Ble mae "amser-real" wir yn ennill ei gost, a ble mae'n ddymuniad heb ei archwilio sy'n dawel ddyblu eich baich gweithredol?** Diofyn y bennod yw swp wedi'i amserlennu, sy'n symlach i resymu drosto, ei brofi, a'i ôl-lenwi, gyda ffrydio wedi'i gadw ar gyfer achosion lle mae'r busnes wir angen oedi isel, fel canfod twyll neu rybuddio gweithredol. Y tyniad cystadleuol yw bri a cheisiadau rhanddeiliaid amwys am ddata "byw," sy'n swnio'n rhad mewn cyfarfod cynllunio ac yn troi'n ddrud mewn cynhyrchiad, gan fod ffrydio'n llusgo i mewn drefnu, semanteg union-unwaith, data sy'n cyrraedd yn hwyr, a rheoli cyflwr, ynghyd ag ail god-sail i'w gadw mewn cam â'r rhesymeg swp. Dewch â thystiolaeth i'r drafodaeth: ar gyfer pob piblinell ffrydio rydych yn ei rhedeg neu'n ei chynnig, enwch y penderfyniad y mae'n ei fwydo a'r oedi y mae'r penderfyniad hwnnw wir yn ei oddef, wedi'i fesur mewn munudau neu oriau yn hytrach nag ansoddeiriau. Ar gyfer platfform menter neu lywodraethol mawr, ychwanegwch gost galwad-ar-ddyletswydd a phrofi pob llwybr amser-real, gan fod piblinell ffrydio na all neb ei phrofi na staffio o'i chwmpas rownd-y-cloc yn atebolrwydd dibynadwyedd wedi'i wisgo fel nodwedd, ac mae'r ateb gonest yn aml yn dymchwel gofyniad "amser-real" yn ôl i swp bob awr sy'n gwasanaethu'r un penderfyniad.

5. **Pa rai o'ch piblinellau na ellid eu hailredeg yn ddiogel heddiw, a beth fyddai ei angen i wneud pob trawsnewidiad yn idempotent?** Mae'r bennod yn mynnu trawsnewidiadau idempotent, atgynyrchadwy, gan ddefnyddio uwchosodiadau penderfynadwy wedi'u hallweddu ar ddynodwyr busnes a phatrymau trosysgrifo rhaniad, fel bod ailredeg yn cynhyrchu'r un canlyniad yn hytrach na dyblygu neu lygru data. Y pwysau cystadleuol yw cyflymder cyflenwi, gan fod swydd atodi-yn-unig naïf yn cyrraedd yn gyflymach nag un a ddyluniwyd i fod yn ailredadwy, ac mae cost y llwybr byr hwnnw'n aros yn guddiedig hyd nes bod methiant yn gorfodi ailredeg rhannol am 2yb a rhywun yn cyfrif refeniw ddwywaith. Dewch â rhestr eiddo ddiriaethol: rhestrwch y swyddi a fyddai'n llygru data pe baent yn cael eu hailredeg o bwynt methiant, ac amcangyfrifwch radiws ffrwydrad y gwaethaf. Ar raddfa menter a llywodraethol, lle gall un methiant tawel wthio data anghywir i mewn i daliadau, adroddiadau, neu ystadegau cyhoeddus, nid yw prosesu di-idempotent yn anghyfleus yn unig, mae'n tanseilio'r archwiliadwyedd sy'n eich galluogi i ailbrosesu cyfnod ar ôl newid rheol a dal i olrhain pob ffigur i'w ffynhonnell, felly mae ariannu'r ailwaith i wneud ailredeg yn ddiogel yn gwestiwn rheolaeth, nid dim ond un o daclusrwydd.

6. **A wyddoch chi beth mae'n ei gostio i redeg pob piblinell, pwy sy'n berchen ar y rhif hwnnw, a faint o'ch bil cwmwl sy'n dod o sganiau llawn a rhaniadau ar goll?** Mae'r bennod yn trin fformat storio, rhaniad, a gwariant cyfrifiadura fel pryderon dosbarth cyntaf â pherchnogion, gan rybuddio bod costau afreolus fel arfer yn olrhain yn ôl i sganiau llawn, rhaniadau ar goll, ac ailbrosesu heb derfyn. Yr ystyriaeth gystadleuol yw bod gwaith cost yn teimlo'n llai brys na chyflenwi nodweddion, felly caiff ei ohirio hyd nes y daw'r bil misol yn syrpreis ac mae cyllid yn dechrau gofyn cwestiynau na all peirianneg eu hateb. Dewch â thystiolaeth: gwariant fesul piblinell a fesul ymholiad, y gyfran o gost sy'n dod o sganiau heb eu rhannu, a chyfrif y ffeiliau bach y dylid eu cywasgu. Ar gyfer sefydliad mawr sy'n rhedeg biliynau o gofnodion ar draws llawer o systemau ffynhonnell, mae bil cwmwl heb berchennog yn tyfu heb i unrhyw un tîm deimlo'n gyfrifol, a mewn lleoliadau llywodraethol rhaid cyfiawnhau gwariant cyhoeddus linell wrth linell, felly mae priodoli cost cyfrifiadura i berchennog a enwyd â metrig a olrhainir yn troi traul dywyll yn un a reolir ac yn aml yn datgelu arbedion digon mawr i ariannu'r buddsoddiad platfform nesaf.

## Lens sector

**Cwmni newydd.** Mae cyflymder yn curo pensaernïaeth. Weiriwch fewnlifiad at gysylltydd a reolir, adeiladwch lond llaw o drawsnewidiadau wedi'u rheoli gan fersiynau, a'u rhedeg ar gerdorfäwr ysgafn sy'n ailgeisio ac yn ôl-lenwi ar ei ben ei hun, yn hytrach na chreu swyddi cron â llaw sy'n torri'n dawel dros nos. Cadwch bob model yn idempotent o'r ymrwymiad cyntaf ac ychwanegwch ychydig o brofion rhad ar gyfer allweddi nwl a chyfrifon rhesi, fel bod newid ffynhonnell gwael yn methu yn CI yn lle ymddangos ar ddangosfwrdd dydd Llun y sylfaenydd. Peidiwch â sefydlu ffrydio na phlatfform pwrpasol: eich adnodd prinnaf yw sylw peirianneg.

**Busnes bach.** Heb beiriannydd data pwrpasol, ffafriwch brynu pentwr integredig dros gydosod un. Mae gwasanaeth ELT a reolir ynghyd â warws cwmwl yn rhoi cysylltyddion, amserlennu, a storio i chi heb dîm platfform i'w cynnal. Fframiwch y dewis fel hylendid data yn hytrach na phrosiect piblinell: gwybyddwch pa systemau ffynhonnell sy'n bwydo'ch adroddiadau, cadwch ddata amrwd fel y gellir olrhain ac ailbrosesu rhif anghywir, a dewiswch declynnau y mae eu costau'n rhagweladwy fel na fydd sgan tabl-llawn yn chwythu'r gyllideb fisol.

**Menter.** Y broblem yw cysondeb ar draws llawer o dimau a biliynau o gofnodion o lawer o systemau ffynhonnell. Safonwch y patrwm ELT, y model haenog llwyfannu-craidd-marchnad, a'r pedwar signal iechyd data fel bod grwpiau'n stopio ailddyfeisio piblinellau bregus. Gorfodwch brofion data a CI ar bob model, priodolwch gost cyfrifiadura i dimau perchen, a rhedwch ddigwyddiadau data drwy'r un ddisgyblaeth galwad-ar-ddyletswydd, llyfr rhedeg, ac ôl-drafodaeth ddi-fai ag y byddech yn ei defnyddio ar gyfer gwasanaethau, fel na fydd methiant tawel byth yn cyrraedd dangosfwrdd heb i neb sylwi.

**Llywodraeth.** Mae rheolau caffael, tryloywder, ac atebolrwydd cyhoeddus yn llunio'r biblinell. Glaniwch gofnodion amrwd, di-newid ar gyfer archwiliadwyedd, eu trawsnewid mewn camau haenog wedi'u profi, a chadw llinach lawn fel y gall archwiliwr olrhain unrhyw ffigur cyhoeddedig yn ôl at ei ddogfennau ffynhonnell, gofyniad cyfreithiol yn aml. Mae prosesu idempotent yn eich galluogi i ailbrosesu cyfnod cyflwyno neu adrodd yn ddiogel pan fydd rheol yn newid, ac mae ffafrio fformatau agored a chod trawsnewid cludadwy'n eich cadw rhag cael eich clymu i mewn i un gwerthwr ar draws contract aml-flwyddyn.

## Enghreifftiau

**Cwmni newydd.** Roedd cwmni newydd dadansoddeg deg person wedi tyfu clymau o swyddi cron a dorrai'n dawel dros nos ac weithiau'n cyfrif rhesi ddwywaith pan fyddai peiriannydd yn ailredeg un â llaw. Symudodd y tîm at gysylltydd a reolir ar gyfer mewnlifiad, fframwaith trawsnewid ar gyfer modelau wedi'u rheoli gan fersiynau, a cherdorfäwr ysgafn sy'n ailgeisio ac yn ôl-lenwi ar ei ben ei hun. Gwnaethant bob model yn idempotent ac ychwanegu llond llaw o brofion ar gyfer allweddi nwl a chyfrifon rhesi, fel bod newid ffynhonnell gwael bellach yn methu yn CI yn lle ymddangos ar ddangosfwrdd dydd Llun y sylfaenydd.

**Menter.** Disodlodd manwerthwr byd-eang gannoedd o sgriptiau echdynnu wedi'u hysgrifennu â llaw â phentwr ELT. Mae cysylltyddion a reolir yn glanio data ffynhonnell amrwd, mae fframwaith trawsnewid yn adeiladu modelau wedi'u profi, wedi'u rheoli gan fersiynau mewn llyn-warws, ac mae cerdorfäwr yn rheoli dibyniaethau ag ailgeisiadau ac ôl-lenwadau. Mae profion data'n dal gwyriad sgema o systemau ffynhonnell cyn iddo gyrraedd dangosfyrddau. Torrodd storio colofnol wedi'i rannu gostau ymholi'n sylweddol, gan wella ffresni o ddyddiol i bob awr ar yr un pryd.

**Llywodraeth.** Mae awdurdod treth yn mewnlifo cyflwyniadau a data trydydd parti drwy biblinell lywodraethedig sy'n glanio cofnodion amrwd, di-newid ar gyfer archwiliadwyedd, yna'n eu trawsnewid mewn camau haenog, wedi'u profi. Mae prosesu idempotent yn eu galluogi i ailbrosesu cyfnod cyflwyno'n ddiogel pan fydd rheol yn newid. Mae llinach lawn yn galluogi archwilwyr i olrhain unrhyw ffigur a gyfrifwyd yn ôl at ddogfennau ffynhonnell, gofyniad cyfreithiol ar gyfer atebolrwydd cyhoeddus.

## Achos busnes: cymhellion, ROI, a TCO

Daw ROI peirianneg data ddisgybledig o ddibynadwyedd, cyflymder, a rheolaeth gost. Mae piblinellau dibynadwy'n golygu bod penderfyniadau ac adroddiadau'n gorffwys ar ddata dibynadwy, felly rydych yn osgoi ailwaith drud a niwed enw da rhifau anghywir. Mae piblinellau modiwlaidd, wedi'u profi'n galluogi timau i gyflenwi cynhyrchion data newydd yn gyflymach, gan gyfansymio gwerth pob buddsoddiad dadansoddeg a ML i lawr yr afon. Mae optimeiddio storio a chyfrifiadura'n lleihau'r bil cwmwl yn uniongyrchol, yn aml gan ymylon mawr unwaith y caiff rhaniad a phatrymau ymholi eu trwsio.

Mae cost mabwysiadu'n cynnwys offer platfform, amser peirianneg i adeiladu piblinellau modiwlaidd wedi'u profi, a disgyblaeth trin data fel meddalwedd. Pwyswch hyn yn erbyn cost peidio â mabwysiadu: swyddi pwrpasol bregus na all ond eu hawdur eu deall, llygredigaeth ddata dawel a ddarganfyddir gan weithredwyr, gwariant cwmwl sy'n chwyddo o sganiau tabl-llawn, a dadansoddwyr wedi'u rhwystro'n aros am ddata. I arweinyddiaeth, fframiwch beirianneg data fel y sylfaen sy'n gwneud dadansoddeg, BI, ac AI yn ddibynadwy ac yn fforddiadwy. Tan-fuddsoddwch yma, a byddwch yn cyfyngu ar yr enillion ar bob menter ddata uwch ei phen.

## Gwrth-batrymau a pheryglon

- Piblinellau wedi'u hadeiladu fel sgriptiau untro heb reolaeth fersiynau, profion, nac adolygiad.
- Swyddi di-idempotent sy'n dyblygu neu'n llygru data pan gânt eu hailredeg ar ôl methiant.
- Mabwysiadu ffrydio er bri pan fyddai swp yn bodloni'r gofyniad oedi.
- Tipio tablau amrwd ar ddadansoddwyr a'i alw'n hunanwasanaeth.
- Dim arsylwadwyedd, fel bod methiannau'n cael eu darganfod gan ddefnyddwyr i lawr yr afon.
- Anwybyddu rhaniad a meintio ffeiliau hyd nes y bydd y bil cwmwl yn ffrwydro.
- Cyplu mewnlifiad, trawsnewid, a gwasanaethu fel na all dim newid yn ddiogel.
- Dileu data amrwd, gan ei gwneud yn amhosibl ailbrosesu pan fydd rhesymeg yn newid.

## Model aeddfedrwydd

1. **Cychwyn:** Sgriptiau ad hoc a rhediadau â llaw, heb brofion na monitro. Caiff methiannau eu darganfod gan ddefnyddwyr i lawr yr afon, nid yw swyddi'n ailredadwy'n ddiogel, ac mae costau cwmwl heb eu rheoli na'u priodoli.
2. **Datblygu:** Mae rhai timau wedi mabwysiadu cerdorfäwr ac wedi rhoi trawsnewidiadau sylfaenol mewn rheolaeth fersiynau, ond mae arfer yn anghyson ar draws y sefydliad. Mae profion achlysurol yn bodoli, mae idempotence yn glytiog, ac mae piblinellau wedi torri'n dal i olygu diffodd tanau adweithiol.
3. **Safoni:** Mae ELT gyda model haenog llwyfannu-craidd-marchnad, wedi'i brofi ac wedi'i reoli gan fersiynau, yn safon ddogfennedig a gymhwysir ar draws timau. Gorfodir dibyniaethau wedi'u cerdorfa ag ailgeisiadau ac ôl-lenwadau, profion data'n rhedeg yn CI, a chonfensiynau a rennir ar gyfer modelu sgema-seren a rhaniad ledled y sefydliad yn hytrach na'u gadael i bob grŵp.
4. **Rheoli:** Caiff y platfform ei fesur a'i reoli. Caiff ffresni, cyfaint, sgema, a dosraniad eu monitro â rhybuddion wedi'u llwybro at dimau perchen, a chaiff SLAs piblinell, amser cymedrig i ganfod, cyfraddau llwyddo ansawdd data, a chost cyfrifiadura fesul piblinell a fesul ymholiad eu tracio yn erbyn llinellau sylfaen. Gorfodir trothwyon dychwelyd a lladd ar dystiolaeth, ac mae gan gost a dibynadwyedd berchnogion wedi'u henwi sy'n cael eu dal i dargedau.
5. **Cerdorfa:** Caiff piblinellau eu trin yn llawn fel meddalwedd â CI/CD, contractau data, a chanfod anomaledd awtomataidd sy'n dal gwyriad cyn i ddefnyddwyr wneud hynny. Uneir rhesymeg swp a ffrydio lle mae oedi wir yn talu, caiff y platfform ei wella'n barhaus a bod yn hunanwasanaeth, a chaiff capasiti, haenau storio, a chost eu hailgydbwyso'n addasadwy wrth i lwythi gwaith newid fel bod cynhyrchion data newydd yn cyrraedd yn gyflym ar sylfaen sefydlog.

## Syniadau ar gyfer trafod

- Ble yn eich pentwr y mae "amser-real" wir yn ennill ei gost, a ble mae'n ddymuniad?
- Pa biblinellau na ellid eu hailredeg yn ddiogel heddiw, a beth fyddai ei angen i drwsio hynny?
- Faint o'ch bil data cwmwl sy'n dod o sganiau llawn a rhaniadau ar goll?
- A yw eich dadansoddwyr yn defnyddio marchnadoedd wedi'u modelu neu dablau amrwd, a beth mae hynny'n ei gostio iddynt?
- Beth yw eich amser cymedrig i ganfod digwyddiad data, a phwy sy'n dod o hyd iddo gyntaf?
- A fyddai uno rhesymeg swp a ffrydio'n lleihau eich baich cynnal a chadw neu'n ychwanegu risg?

## Prif negeseuon

- Trinwch biblinellau fel meddalwedd: rheolaeth fersiynau, profion, adolygiad, CI/CD, ac arsylwadwyedd.
- Ffafriwch ELT gyda modelau haenog, wedi'u profi; cadwch ddata amrwd ar gyfer ailbrosesu.
- Dewiswch swp yn ddiofyn a ffrydio dim ond lle mae oedi wir yn talu.
- Gwnewch drawsnewidiadau'n idempotent fel bod ailredeg yn ddiogel.
- Modelwch ddata ar gyfer defnyddwyr â sgemâu seren neu dablau eang bwriadol.
- Monitrwch ffresni, cyfaint, sgema, a dosraniad, a thriniwch ddigwyddiadau data fel terfynau gwasanaeth.
- Optimeiddiwch fformatau storio, rhaniad, a chost cyfrifiadura fel pryderon dosbarth cyntaf.

## Cyfeiriadau a darllen pellach

- Joe Reis a Matt Housley, "Fundamentals of Data Engineering."
- Ralph Kimball a Margy Ross, "The Data Warehouse Toolkit."
- Martin Kleppmann, "Designing Data-Intensive Applications."
- Bill Inmon, "Building the Data Warehouse."
- James Densmore, "Data Pipelines Pocket Reference."
- Nathan Marz a James Warren, "Big Data" (pensaernïaeth Lambda).
- Barr Moses a chydweithwyr, "Data Quality Fundamentals" (arsylwadwyedd data).
