# 8.3 Cynwysyddion, cerdorfa, a brodorol-cwmwl

## Trosolwg a chymhelliant

Mae [cynhwysydd](https://en.wikipedia.org/wiki/OS-level_virtualization) yn pecynnu cymhwysiad ynghyd â'i ddibyniaethau yn un uned gludadwy, ynysig. Mae'n rhedeg yr un ffordd ar liniadur, mewn amgylchedd profi, ac mewn cynhyrchiad. Mae platfformau cerdorfa, yn fwyaf amlwg [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes), yn amserlennu ac yn rheoli niferoedd mawr o gynwysyddion ar draws fflydoedd o beiriannau. Maent yn trin gosodiad, graddio, iechyd, rhwydweithio, ac adfer. [Brodorol-cwmwl](https://en.wikipedia.org/wiki/Cloud-native_computing) yw'r arddull bensaernïol ehangach sydd wedi'i hadeiladu ar y sylfeini hyn: cymwysiadau wedi'u dylunio fel gwasanaethau wedi'u cyplu'n rhydd, y gellir eu defnyddio'n annibynnol, ac y gellir eu graddio'n llorweddol, sy'n tybio seilwaith dynamig, hunanwella.

I dimau mawr, mae cynwysyddion a cherdorfa'n datrys un broblem anodd. Mae angen i chi redeg llawer o wasanaethau, wedi'u hadeiladu gan lawer o dimau, yn ddibynadwy ac yn effeithlon ar seilwaith a rennir. Mae cynwysyddion yn rhoi contract pecynnu a chynamser cyson i bob tîm, sy'n ymddeol dosbarth o fethiannau "mae'n gweithio ar fy mheiriant i." Mae cerdorfa'n cuddio peiriannau unigol y tu ôl i sylfaen gyffredin, felly mae timau'n defnyddio i blatfform yn hytrach na gweinyddion. Y safoniad hwn sy'n caniatáu i chi weithredu cannoedd neu filoedd o wasanaethau heb i bob tîm ailddyfeisio defnyddio, graddio, a gwydnwch.

Mae mabwysiadwyr menter a llywodraeth yn ennill cludadwyedd, gwydnwch, a llwybr i ffwrdd o glymu-i-werthwr. Yn gyfnewid am hynny, maent yn etifeddu cymhlethdod go iawn a chyfrifoldebau diogelwch newydd. Mae platfform cynwysyddion yn bwerus yn union oherwydd ei fod yn rhaglenadwy a dynamig, sy'n golygu bod yn rhaid i chi ei lywodraethu'n ofalus. Mae tarddiad delwedd, ynysu amlfeddiannaeth, polisi rhwydwaith, a chost i gyd yn dod yn bryderon ar lefel platfform. Mae mabwysiadwyr sector cyhoeddus fwyfwy'n ychwanegu gofynion sofraniaeth: rheolaeth dros ble mae data'n preswylio a phwy sy'n gallu ei gyrchu. Mae hynny'n gwneud y gallu i redeg llwythi gwaith cyson ar draws amgylcheddau dewisedig yn allu strategol, nid dim ond manylyn technegol.

## Egwyddorion allweddol

- Pecynnwch gymwysiadau fel delweddau cynhwysydd bach, un-pwrpas, anfewidiol.
- Ymarferwch hylendid delweddau: delweddau sylfaen minimalaidd, fersiynau wedi'u pinio, wedi'u sganio am wendidau, ac wedi'u llofnodi.
- Dyluniwch gymwysiadau i fod yn ddi-gyflwr ac yn raddadwy'n llorweddol lle bo modd, gan allanoli cyflwr.
- Triniwch fodel cyflwr-dymunol y platfform cerdorfa fel y ffynhonnell wirionedd a gadewch iddo hunanwella.
- Gorfodwch ynysu a braint-leiaf rhwng tenantiaid, llwythi gwaith, a pharthau enwau.
- Dilynwch egwyddorion [deuddeg-ffactor](https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology), methodoleg ar gyfer adeiladu apiau tafladwy, wedi'u hallanoli o ran ffurfweddiad, ac y gellir eu graddio'n llorweddol, a'u hymestyn ar gyfer realiti systemau dosbarthedig.
- Gwnewch gost yn bryder peirianneg dosbarth cyntaf, gweladwy, nid ôl-ystyriaeth.
- Ffafriwch haniaethau cludadwy, seiliedig ar safonau i gadw hyblygrwydd strategol.

## Argymhellion

### Ymarfer hylendid delweddau trylwyr

Y ddelwedd gynhwysydd yw eich uned sylfaenol o ymddiriedaeth a defnyddio, felly triniwch hi felly. Dechreuwch o ddelweddau sylfaen minimalaidd, dibynadwy i leihau'r arwyneb ymosod. Piniwch fersiynau dibyniaeth a delwedd sylfaen ar gyfer atgynhyrchiadwyedd. Sganiwch bob delwedd am wendidau hysbys yn y biblinell adeiladu, a rhwystrwch y rhai â chanfyddiadau critigol. Llofnodwch ddelweddau a gwiriwch lofnodion adeg defnyddio, fel mai dim ond delweddau cymeradwy, heb eu haddasu sy'n rhedeg. Cadwch gofrestr fewnol wedi'i churadu o ddelweddau sylfaen wedi'u caledu y mae timau'n adeiladu ohonynt. Mae hynny'n lledaenu rhagosodiadau diogelwch da yn awtomatig.

### Defnyddiwch batrymau Kubernetes yn hytrach na'u hailddyfeisio

Mae Kubernetes yn gwobrwyo timau sy'n mabwysiadu ei batrymau sefydledig, ac mae'n cosbi timau sy'n ymladd yn erbyn ei fodel. Defnyddiwch fanifestau datganiadol ar gyfer cyflwr dymunol. Ychwanegwch brofion iechyd fel y gall y platfform ganfod a disodli enghreifftiau afiach. Gosodwch geisiadau a therfynau adnoddau fel y gall yr amserlennydd bacio llwythi gwaith yn ddiogel. Defnyddiwch awto-raddio llorweddol ar gyfer galw elastig. Ar gyfer rhesymeg weithredol y mae'n rhaid iddi redeg yn barhaus, fel rheoli cronfa ddata, cylchdroi tystysgrifau, neu gysoni adnoddau pwrpasol, defnyddiwch y patrwm gweithredwr, sy'n amgodio gwybodaeth weithredol ddynol i mewn i feddalwedd sy'n gwylio cyflwr ac yn gweithredu. Gwrthsefwch yr ysfa i adeiladu cerdorfa bwrpasol ar ben y platfform. Ffafriwch y strwythurau brodorol.

### Cynllunio amlfeddiannaeth yn fwriadus

Pan fydd llawer o dimau'n rhannu clwstwr, mae ynysu'n ofyniad diogelwch a dibynadwyedd, nid moethusrwydd. Defnyddiwch barthau enwau fel ffiniau tenantiaeth. Gorfodwch gwotâu adnoddau fel na all unrhyw denant lwgu eraill. Cymhwyswch bolisïau rhwydwaith i gyfyngu traffig i'r hyn a ganiateir yn benodol. Defnyddiwch [reolaeth mynediad seiliedig ar rôl](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC) i gyfyngu'r hyn y gall pob tîm ei wneud. Ar gyfer llwythi gwaith ag anghenion ynysu cryfach, ystyriwch glystyrau ar wahân neu focsio tywod cryfach. Penderfynwch yn gynnar ai amlfeddiannaeth feddal (timau mewnol dibynadwy) neu amlfeddiannaeth galed (llwythi gwaith sy'n anymddiried yn ei gilydd) yw eich model, oherwydd mae'r ddau'n gofyn am reolyddion gwahanol iawn.

### Adeiladu'n frodorol-cwmwl, deuddeg-ffactor a thu hwnt

Mae'r fethodoleg deuddeg-ffactor, gyda'i dibyniaethau penodol, ffurfweddiad yn yr amgylchedd, prosesau di-gyflwr, tafladwyedd, ac yn y blaen, yn parhau i fod yn linell sylfaen ragorol ar gyfer gwasanaethau sy'n ffynnu ar blatfform dynamig. Ymestynnwch hi ar gyfer realiti ychwanegol systemau dosbarthedig. Cynlluniwch ar gyfer methiant rhannol. Gwnewch weithrediadau'n ddiddymol ac yn ailgeisiadwy. Datgelwch iechyd a thelemetreg. Triniwch arsylledd fel nodwedd adeiledig yn hytrach nag ychwanegiad. Allanolwch bob cyflwr i wasanaethau data wedi'u rheoli, fel bod enghreifftiau cymhwysiad yn aros yn dafladwy ac yn raddadwy'n llorweddol.

### Cynllunio strategaethau amlgwmwl, hybrid, a sofran yn bragmatig

Mae cludadwyedd yn werthfawr, ond dilynwch ef gyda llygaid clir. Safonwch ar haniaethau cludadwy fel cynwysyddion, Kubernetes, ac APIs agored, fel y gall llwythi gwaith symud os oes angen. Ond osgowch y fagl o wrthod pob gwasanaeth wedi'i reoli, sy'n masnachu cynhyrchedd go iawn am gludadwyedd damcaniaethol. Ar gyfer gofynion hybrid a sofran, cynlluniwch fel y gall yr un llwythi gwaith a phiblinellau redeg mewn rhanbarth dewisedig, canolfan ddata breifat, neu gwmwl sofran sy'n bodloni rheolau awdurdodaeth a phreswyliad data. Gwnewch y ffiniau sofraniaeth a phreswyliad yn benodol mewn pensaernïaeth a pholisi.

### Gwneud cost yn weladwy gyda FinOps

Mewn amgylcheddau cwmwl elastig, mae cost yn ganlyniad uniongyrchol i benderfyniadau peirianneg, felly rhowch welededd ac atebolrwydd i beirianwyr. Tagiwch adnoddau ar gyfer dyrannu cost. Priodolwch wariant i dimau a gwasanaethau. Dangoswch ddata cost ochr yn ochr â mesurau perfformiad. Meintiwch lwythi gwaith yn gywir, defnyddiwch awto-raddio i gyfateb i alw, ac adenillwch adnoddau segur. Sefydlwch arfer FinOps sy'n dwyn peirianneg, cyllid, a chynnyrch ynghyd, fel bod gwariant cwmwl yn dod yn gyfrifoldeb a rennir, parhaus yn hytrach na syndod chwarterol.

## Cyfaddawdau: manteision ac anfanteision

| Dewis | Manteision | Anfanteision | Y ffit orau |
|---|---|---|---|
| Kubernetes | Pwerus, cludadwy, ecosystem enfawr | Cymhlethdod serth; baich gweithredol | Llawer o wasanaethau ar raddfa |
| Gwasanaeth cynhwysydd wedi'i reoli | Llai o faich gweithredol; dechrau cyflymach | Rhywfaint o glymu-i-werthwr; llai o reolaeth | Timau sydd am symlrwydd |
| Clwstwr sengl a rennir | Defnydd effeithlon o adnoddau | Ynysu anos; radiws ffrwydro | Tenantiaid mewnol dibynadwy |
| Clwstwr fesul tenant | Ynysu cryf | Cost a gorbenion uwch | Llwythi gwaith anymddiriedus neu reoleiddiedig |
| Cludadwyedd amlgwmwl | Hyblygrwydd; yn osgoi clymu-i-werthwr | Gwasanaethau'r rhannydd cyffredin isaf | Lliniaru risg strategol |
| Gwasanaethau wedi'u rheoli'n ddwfn, un cwmwl | Cynhyrchedd mwyaf | Dibyniaeth ar werthwr | Timau sy'n canolbwyntio ar gyflymder |

Y cyfaddawd cyffredinol yw gallu yn erbyn cymhlethdod. Mae pensaernïaethau Kubernetes a brodorol-cwmwl yn cyflenwi elastigedd, gwydnwch, a chyflymder. Ond maent yn gosod baich gweithredol a gwybyddol sylweddol y mae timau bach yn rheolaidd yn ei danamcangyfrif. Yn yr un modd, mae ymlid cludadwyedd [amlgwmwl](https://en.wikipedia.org/wiki/Multicloud) llawn yn masnachu cynhyrchedd am ddewisoldeb. Mae'r ateb cywir yn dibynnu ar raddfa a risg. Mae sefydliadau mawr gyda llawer o dimau ac anghenion llywodraethu cryf fel arfer yn cyfiawnhau'r buddsoddiad. Mae ymdrechion llai yn aml yn cael eu gwasanaethu'n well gan wasanaethau wedi'u rheoli sy'n cuddio'r cymhlethdod.

## Cwestiynau i'w trafod gyda'ch tîm

1. **A ydych chi'n llofnodi delweddau ac yn gwirio llofnodion adeg defnyddio, ac a yw gwendid critigol yn rhwystro'r adeiladwaith mewn gwirionedd?** Y ddelwedd yw eich uned ymddiriedaeth, felly mae'r gadwyn gyflenwi o'i chwmpas yn haeddu giatiau caled, nid rhybuddion. Penderfynwch a all dim ond delweddau wedi'u llofnodi, wedi'u gwirio redeg, a yw sganio'n rhwystro canfyddiadau critigol neu'n eu cofnodi'n unig, a phwy sy'n cynnal y gofrestr guradedig o ddelweddau sylfaen wedi'u caledu y mae timau'n adeiladu ohonynt. Ar gyfer llwythi gwaith menter a llywodraeth mae hyn yn aml yn ofyniad cydymffurfiaeth, ac mae hefyd yn amddiffyniad gorau yn erbyn dibyniaeth wenwynig yn cyrraedd cynhyrchiad. Dewch â'r cyflwr presennol: pa gyfran o ddelweddau sy'n rhedeg sy'n dod o'ch sylfaen galedu, faint sy'n cario CVEs critigol heb eu clytio, ac a ellir amserlennu unrhyw ddelwedd heb ei llofnodi ar hyn o bryd. Os nad yw canfyddiad critigol yn stopio defnyddiad, addurn yn unig yw eich sganiwr.

2. **Sut mae ceisiadau, terfynau, a chwotâu adnoddau'n atal un llwyth gwaith rhag llwgu ei gymdogion, heb adael capasiti drud yn segur?** Ar glwstwr a rennir, gall llwyth gwaith heb derfynau chwalu neu dagu popeth o'i gwmpas, ac mae cwotâu wedi'u gosod yn rhy hael yn gwastraffu'r enillion defnydd sy'n cyfiawnhau'r platfform. Penderfynwch ar ragosodiadau synhwyrol, pwy sy'n eu diwnio, a sut rydych chi'n dal llwythi gwaith heb unrhyw geisiadau wedi'u gosod o gwbl. Ar raddfa mae hyn yn rheolydd dibynadwyedd a rheolydd cost, oherwydd meintio cywir yw lle mae llawer o'r arbedion FinOps yn byw. Dewch â data: defnydd clwstwr presennol, pa mor aml y mae llwythi gwaith yn cael eu troi allan neu eu tagu, a pha barthau enwau nad oes ganddynt gwotâu. Y nod yw pacio bin dwys, diogel, felly triniwch derfynau coll fel diffyg y mae'r platfform yn ei wrthod.

3. **Pa gyflwr y caniateir iddo fyw y tu mewn i gynhwysydd, ac i ble mae popeth arall yn mynd?** Mae gwydnwch brodorol-cwmwl yn dibynnu ar enghreifftiau tafladwy y gall y platfform eu hailamserlennu ar ewyllys, a dim ond os yw cyflwr pwysig yn byw mewn gwasanaethau data wedi'u rheoli yn hytrach nag ar ddisg leol y cynhwysydd y mae hynny'n dal. Penderfynwch y rheol yn benodol, oherwydd mae cyflwr wedi'i storio mewn cynhwysydd drwy ddamwain yn dod yn golled data ar yr ailamserlennu nesaf. I dimau sy'n mudo hen gymwysiadau, dyma'n aml y rhan anoddaf, gan fod gwasanaethau etifeddol yn tybio system ffeiliau leol sefydlog. Dewch ag arolwg: pa wasanaethau sy'n ysgrifennu cyflwr lleol, pa rai sy'n dibynnu ar sesiynau gludiog neu affinedd nod, a beth fyddai ei angen i allanoli pob un. Hyd nes bod cyflwr yn allanol, mae gennych chi gynwysyddion sy'n edrych yn elastig ond na ellir eu symud mewn gwirionedd.

4. **Pan fydd llawer o dimau'n rhannu clwstwr, a yw eich model ynysu wedi'i ddewis yn fwriadus fel amlfeddiannaeth feddal neu galed, ac a yw'r rheolyddion yn cyfateb i'r dewis hwnnw?** Mae parthau enwau'n gwahanu timau mewnol dibynadwy, ond nid ydynt yn cynnwys llwyth gwaith sy'n weithredol elyniaethus neu wedi'i beryglu, ac mae trin amlfeddiannaeth feddal fel pe bai'n galed yn ddigwyddiad diogelwch sy'n aros i ddigwydd. Penderfynwch fesul llwyth gwaith ai dim ond angen rhannu teg sydd ar denantiaid neu a ddylid tybio eu bod yn anymddiried yn ei gilydd, yna cyfatebwch y rheolyddion: parthau enwau, cwotâu, polisïau rhwydwaith, ac RBAC ar gyfer yr achos meddal, clystyrau ar wahân neu focsio tywod cryfach ar gyfer yr achos caled. I sefydliad mawr mae'r penderfyniad hwn yn gyrru cost yn uniongyrchol, oherwydd mae clwstwr fesul tenant yn llawer drutach na pharthau enwau a rennir, felly rydych chi eisiau gwario'r gyllideb ynysu dim ond lle mae'r model bygythiad yn ei fynnu. Dewch ag arolwg tenantiaid: pa lwythi gwaith sy'n rhannu clwstwr heddiw, pa rai sy'n trin traffig rheoleiddiedig neu sy'n wynebu'n allanol, a ble mae polisi rhwydwaith yn dal yn ganiataol-yn-ddiofyn. Mewn lleoliadau menter a llywodraeth, mae cymysgu llwythi gwaith anymddiriedus o dan amlfeddiannaeth feddal yn union y canfyddiad y bydd archwiliwr yn ei nodi, felly enwch y ffin cyn iddyn nhw wneud hynny.

5. **Faint rydych chi'n ei dalu am gludadwyedd amlgwmwl, ac a fyddwch chi byth yn ei ddefnyddio mewn gwirionedd?** Mae safoni ar gynwysyddion, Kubernetes, ac APIs agored yn cadw llwythi gwaith yn symudadwy, ond mae gwrthod pob gwasanaeth wedi'i reoli i gadw'r opsiwn hwnnw'n masnachu cynhyrchedd go iawn, dyddiol am gludadwyedd na fydd y sefydliad efallai byth yn ei ymarfer. Penderfynwch ble mae cludadwyedd yn ofyniad gwirioneddol, fel rhwymedigaeth sofraniaeth neu ymadael rydych chi wedi'i llofnodi, yn erbyn lle mae'n flanced gysur sy'n arafu pob tîm. Yr ystyriaeth sy'n cystadlu yw cyflymder: mae gwasanaethau wedi'u rheoli'n ddwfn yn cyflenwi nodweddion yn gyflymach, ac mae pensaernïaeth y rhannydd cyffredin isaf yn dreth sefydlog ar bob tîm. Dewch â'r dystiolaeth: pa wasanaethau wedi'u rheoli rydych chi wedi'u hosgoi a beth gostiodd hynny mewn amser peirianneg, a ydych chi erioed wedi symud llwyth gwaith rhwng darparwyr, a beth mae eich contractau'n ei orfodi mewn gwirionedd. I fabwysiadwyr llywodraeth a reoleiddir, gall rheolau preswyliad data a chwmwl sofran wneud cludadwyedd yn ddi-drafod, felly cynlluniwch fel bod yr un manifestau a phiblinellau'n rhedeg mewn rhanbarth sofran ac amgaead preifat, ond byddwch yn onest mai cost gydymffurfiaeth yw hyn yn hytrach nag yswiriant am ddim.

6. **A all pob tîm weld beth mae'n ei wario, ac a oes unrhyw un yn berchen ar y bil cyn iddo ddod yn syndod?** Ar blatfform elastig, mae cost yn allbwn uniongyrchol i benderfyniadau peirianneg, ac eto heb dagiau dyrannu cost a dangosfyrddau gweladwy, mae gwariant yn cronni i gronfa a rennir nad oes neb yn teimlo'n gyfrifol amdani nes bod cyllid yn uwchgyfeirio. Penderfynwch sut rydych chi'n priodoli cost i dimau a gwasanaethau, pwy sy'n ei adolygu, ac a yw peirianwyr yn gweld cost wrth ymyl mesurau perfformiad neu ddim ond yn clywed amdano unwaith y chwarter. Mae'r tyndra rhwng atebolrwydd a ffrithiant: gwthiwch gost yn rhy galed ac mae pob penderfyniad yn dod yn drafodaeth gyllideb, ei anwybyddu a bydd llwythi gwaith segur, gorddimensiwn yn cronni'n dawel. Dewch â'r rhifau: gwariant presennol fesul tîm, faint o gapasiti sy'n eistedd yn segur neu'n orddimensiwn, a pha mor gyflym y byddai llwyth gwaith rhemp yn cael ei sylwi. Ar gyfer cyllidebau menter a llywodraeth, mae gwariant cwmwl heb ei briodoli'n fethiant llywodraethu ac yn risg ariannol go iawn, felly sefydlwch arfer FinOps sy'n rhoi peirianneg, cyllid, a chynnyrch yn yr un sgwrs yn hytrach na chysoni ar ôl y ffaith.

## Golwg sector

**Startup.** Estynnwch am wasanaeth cynhwysydd wedi'i reoli yn hytrach na chlwstwr Kubernetes hunan-westeiedig: gyda dau neu dri gwasanaeth a dim peiriannydd platfform, mae awyrennau rheoli'n dynfa na allwch ei fforddio. Pecynnwch ddelweddau bach o sylfaen minimalaidd, piniwch fersiynau, ychwanegwch un sgan wendidau i'r adeiladwaith, a gwthiwch bob cyflwr i mewn i gronfa ddata wedi'i rheoli fel bod enghreifftiau'n aros yn dafladwy. Hepgorwch barthau enwau, gweithredwyr, a chludadwyedd amlgwmwl hyd nes bod gennych chi mewn gwirionedd y gwasanaethau a'r bobl i'w cyfiawnhau.

**Busnes bach.** Heb arbenigwr platfform pwrpasol a chyllideb dynn, pwyswch yn drwm ar wasanaethau wedi'u rheoli a gadewch i'r darparwr redeg y gerdorfa y byddai'n rhaid i chi fel arall ei staffio. Triniwch hanfodion cynwysyddion fel eich llawr diogelwch: mae delweddau minimalaidd, pinio fersiynau, a sgan yn y biblinell yn rhoi'r rhan fwyaf o'r amddiffyniad am ychydig o ymdrech. Ffafriwch brynu platfform sy'n cael ei gefnogi dros adeiladu un, a chadwch ddigon o gludadwyedd, cynwysyddion safonol ac APIs agored, fel nad ydych chi'n cael eich dal os bydd prisio neu delerau'n newid.

**Menter.** Llywodraethu platfform ar draws llawer o dimau yw'r dasg: tîm platfform canolog yn cyflenwi delweddau sylfaen wedi'u caledu, giatiau llofnodi a sganio, tenantiaeth parth enwau gyda chwotâu, polisi rhwydwaith, ac RBAC, ynghyd â thagiau dyrannu cost a dangosfwrdd FinOps. Safonwch y contract defnyddio fel bod cannoedd o wasanaethau'n gweithredu yr un ffordd, a rheolwch ddiogelwch, amlfeddiannaeth, a chost yn ganolog tra bo timau'n hunanwasanaethu defnyddio. Ariannwch y tîm platfform yn iawn, oherwydd mae platfform heb ddigon o adnoddau'n dod yn dagfa y mae'r sefydliad cyfan yn aros amdani.

**Llywodraeth.** Mae sofraniaeth, preswyliad data, ac atebolrwydd cyhoeddus yn siapio'r bensaernïaeth. Rhedwch lwythi gwaith ar gynwysyddion safonol a Kubernetes fel bod yr un piblinellau'n rhedeg mewn rhanbarth sofran ac amgaead ar-safle achrededig, ac amgodiwch ffiniau preswyliad a mynediad fel polisi yn hytrach na chonfensiwn. Tynnwch ddelweddau o gofrestr fewnol wedi'i chaledu, cymhwyswch amlfeddiannaeth galed i'r data mwyaf sensitif, a chadwch y cludadwyedd sy'n rhoi gwydnwch a phŵer negodi i chi, gan fod rheolau caffael yn aml yn gwahardd clymu-i-werthwr-sengl.

## Enghreifftiau

**Startup.** Mae startup chwe pherson yn pecynnu ei ddau wasanaeth fel delweddau cynhwysydd bach wedi'u hadeiladu o sylfaen minimalaidd, ac yn eu rhedeg ar wasanaeth cynhwysydd wedi'i reoli yn hytrach na chlwstwr Kubernetes hunan-westeiedig, fel nad oes rhaid i neb warchod awyrennau rheoli. Maen nhw'n pinio fersiynau delwedd sylfaen ac yn ychwanegu sgan wendidau at eu hadeiladwaith, ond maen nhw'n fwriadol yn hepgor y nodweddion cerdorfa trymach hyd nes bod ganddyn nhw mewn gwirionedd fwy na llond llaw o wasanaethau. Mae cyflwr yn byw mewn cronfa ddata Postgres wedi'i rheoli, sy'n cadw'r cynwysyddion yn dafladwy ac yn caniatáu i'r platfform eu hailgychwyn neu eu graddio heb unrhyw golled ddata.

**Menter.** Mae cwmni telathrebu'n rhedeg sawl cant o [ficrowasanaethau](https://en.wikipedia.org/wiki/Microservices) ar glystyrau Kubernetes a rennir. Mae tîm platfform yn darparu delweddau sylfaen wedi'u caledu, yn gorfodi llofnodi delweddau a giatiau gwendidau, ac yn ynysu unedau busnes yn barthau enwau gyda chwotâu, polisïau rhwydwaith, ac RBAC. Mae tagiau dyrannu cost a dangosfwrdd FinOps yn priodoli gwariant i bob llinell gynnyrch, ac mae awto-raddio'n meintio capasiti i'r galw'n gywir. Mae timau cynnyrch yn defnyddio ddwsinau o weithiau'r dydd i blatfform cyson heb reoli gweinyddion. Mae'r cwmni'n cadw rheolaeth ganolog dros ddiogelwch a chost.

**Llywodraeth.** Rhaid i wasanaeth iechyd cenedlaethol gadw data dinasyddion o fewn ffiniau cenedlaethol ac o dan reolaeth gyfreithiol genedlaethol. Mae'n rhedeg ei lwythi gwaith ar ranbarth cwmwl sofran gan ddefnyddio cynwysyddion safonol a Kubernetes, fel bod yr un piblinellau a manifestau hefyd yn rhedeg mewn amgylchedd achrededig ar-safle ar gyfer y data mwyaf sensitif. Amgodir ffiniau preswyliad data a mynediad fel polisi, tynnir delweddau o gofrestr fewnol wedi'i chaledu, ac mae amlfeddiannaeth galed yn ynysu llwythi gwaith sensitif. Mae cludadwyedd ar draws y rhanbarth sofran a'r amgaead preifat yn rhoi gwydnwch a phŵer negodi i'r gwasanaeth heb aberthu cydymffurfiaeth.

## Achos busnes: cymhellion, ROI, a TCO

Daw ROI cynwysyddion a cherdorfa o ddefnydd uwch o adnoddau, defnyddiadau cyflymach a mwy dibynadwy, graddio elastig sy'n cyfateb gwariant i alw, a gwydnwch gwell drwy hunanwella. Mae safoni ar blatfform cyffredin yn lleihau ymdrech ddyblyg ar draws timau ac yn cyflymu sefydlu, oherwydd mae pob gwasanaeth yn dilyn yr un contract defnyddio a gweithredol.

Rhaid i'r dadansoddiad TCO fod yn onest am y baich gweithredol. Mae costau mabwysiadu'n cynnwys staff peirianneg platfform, hyfforddiant, offer diogelwch ar gyfer delweddau a chlystyrau, a'r ymdrech barhaus o redeg y platfform ei hun. Mae cost peidio â mabwysiadu'n cynnwys defnyddio pwrpasol anghyson ar draws timau, defnydd gwael o seilwaith drud, graddio â llaw brau, ac anhawster bodloni gofynion gwydnwch a sofraniaeth. I arweinyddiaeth, mae'r achos yn gorffwys ar raddfa. O dan nifer penodol o wasanaethau, efallai na fydd y cymhlethdod yn talu ar ei ganfed, a gwasanaeth wedi'i reoli sy'n ddoethach. Ond ar raddfa menter a llywodraeth, sylfaen platfform brodorol-cwmwl wedi'i llywodraethu fel arfer yw'r un fwyaf cost-effeithiol a gwydn, ar yr amod eich bod chi'n ariannu'r tîm platfform i'w redeg yn iawn.

## Gwrth-batrymau a pheryglon

- **Delweddau tew, heb eu sganio.** Mae delweddau chwyddedig wedi'u hadeiladu o sylfeini heb eu hymddiried yn cario gwendidau diangen ac yn arafu popeth.
- **Kubernetes at bopeth.** Mae mabwysiadu cerdorfäwr cymhleth ar gyfer llond llaw o wasanaethau syml yn prynu cymhlethdod heb enillion.
- **Anwybyddu terfynau adnoddau.** Heb geisiadau a therfynau, gall un llwyth gwaith lwgu neu chwalu ei gymdogion.
- **Tenantiaeth feddal ar gyfer llwythi gwaith elyniaethus.** Mae dibynnu ar barthau enwau yn unig i ynysu tenantiaid anymddiriedus yn ddigwyddiad diogelwch sy'n aros i ddigwydd.
- **Cynwysyddion â chyflwr drwy ddamwain.** Mae storio cyflwr pwysig y tu mewn i gynwysyddion tafladwy'n arwain at golled ddata ar ailamserlennu.
- **Dallineb cost.** Mae trin gwariant cwmwl fel gorbenion sefydlog yn hytrach nag allbwn peirianneg yn arwain at filiau rhemp.
- **Theatr gludadwyedd.** Gwrthod pob gwasanaeth wedi'i reoli i gadw cludadwyedd na fydd y sefydliad byth yn ei ddefnyddio mewn gwirionedd.

## Model aeddfedrwydd

**Lefel 1: Cychwyn.** Defnyddir cynwysyddion yn ad hoc, os o gwbl. Mae delweddau'n cael eu hadeiladu â llaw ac heb eu sganio, mae defnyddio â llaw ac yn adweithiol, ac nid oes platfform a rennir, gwelededd cost, na model ynysu.

**Lefel 2: Datblygu.** Mae timau'n cynhwysyddu cymwysiadau ac yn mabwysiadu cerdorfäwr, ond mae arferion yn amrywio rhwng grwpiau. Mae sganio delweddau, terfynau adnoddau, a llofnodi'n anghyson, ac ni chaiff cost ac amlfeddiannaeth eu llywodraethu'n systematig.

**Lefel 3: Safoni.** Mae platfform safonol wedi'i ddogfennu a'i orfodi ar draws y sefydliad: delweddau sylfaen wedi'u caledu, giatiau llofnodi a sganio, tenantiaeth yn seiliedig ar barthau enwau gyda chwotâu a pholisi rhwydwaith, RBAC, a dyraniad cost. Mae patrymau brodorol-cwmwl a deuddeg-ffactor yn norm disgwyliedig yn hytrach na dewis lleol.

**Lefel 4: Rheoli.** Mae'r platfform yn cael ei fesur a'i reoli yn erbyn llinellau sylfaen. Rydych chi'n olrhain defnydd clwstwr, cyfran y delweddau sy'n rhedeg wedi'u hadeiladu o'r sylfaen galedu, gwendidau critigol heb eu clytio, amlder defnyddio a chyfradd methiant newid, cyfraddau troi allan a thagu, a chost fesul tîm a gwasanaeth yn erbyn cyllideb. Gorfodir giatiau ar y dystiolaeth hon: gwrthodir terfynau adnoddau coll a delweddau heb eu llofnodi'n awtomatig, ac mae llithriad o'r safon yn sbarduno gweithredu yn hytrach na rhybudd.

**Lefel 5: Cydgysylltu.** Mae'r platfform yn hunanwasanaeth ac yn hunanwella, wedi'i integreiddio ar draws y sefydliad ac yn addasol. Mae FinOps yn meintio ac yn adennill capasiti'n gywir yn barhaus, mae pensaernïaeth gludadwy'n cefnogi gofynion hybrid a sofran, ac mae'r platfform yn gwella'n barhaus o ddefnydd wedi'i fesur, gan ymddeol a disodli cydrannau wrth i lwythi gwaith, cost, a'r darlun risg newid.

## Syniadau ar gyfer trafodaeth

- Ar ba raddfa mae mabwysiadu Kubernetes yn stopio bod yn gymhlethdod er ei fwyn ei hun ac yn dechrau talu ar ei ganfed?
- Ble mae'r ffin gywir rhwng amlfeddiannaeth feddal a chaled ar gyfer eich llwythi gwaith?
- Faint ddylech chi ei fuddsoddi mewn cludadwyedd amlgwmwl yn erbyn cynhyrchedd gwasanaethau wedi'u rheoli'n ddwfn?
- Sut rydych chi'n rhoi atebolrwydd cost go iawn i beirianwyr heb droi pob penderfyniad yn drafodaeth gyllideb?
- Beth yw eich model llywodraethu ar gyfer delweddau sylfaen, a phwy sy'n cynnal y gofrestr galedu?
- Sut mae gofynion sofraniaeth a phreswyliad data'n siapio pensaernïaeth eich platfform?

## Prif negeseuon

- Mae cynwysyddion yn safoni pecynnu a chynamser; mae cerdorfa'n safoni gweithrediad ar raddfa.
- Mae hylendid delweddau, sef delweddau minimalaidd, wedi'u pinio, wedi'u sganio, wedi'u llofnodi, yn ddiogelwch sylfaenol.
- Defnyddiwch batrymau a gweithredwyr Kubernetes brodorol yn hytrach nag adeiladu cerdorfa bwrpasol.
- Dewiswch fodel amlfeddiannaeth yn fwriadus yn seiliedig ar faint mae'r llwythi gwaith yn ymddiried yn ei gilydd.
- Dilynwch ddeuddeg-ffactor a'i ymestyn ar gyfer realiti systemau dosbarthedig fel methiant rhannol ac arsylledd.
- Triniwch gost fel allbwn peirianneg a'i reoli'n barhaus drwy FinOps.

## Cyfeiriadau a darllen pellach

- Adam Wiggins, *The Twelve-Factor App* (methodoleg).
- Brendan Burns, Joe Beda, a Kelsey Hightower, *Kubernetes Up & Running*.
- Bilgin Ibryam a Roland Huß, *Kubernetes Patterns*.
- Cornelia Davis, *Cloud Native Patterns*.
- J.R. Storment a Mike Fuller, *Cloud FinOps*.
- Liz Rice, *Container Security*.
- Cloud Native Computing Foundation (CNCF), diffiniad a thirwedd brodorol-cwmwl.
