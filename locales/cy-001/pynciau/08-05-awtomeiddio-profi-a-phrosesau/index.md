# 8.5 Awtomeiddio profi a phrosesau

## Trosolwg a chymhelliant

Awtomeiddio profi a phrosesau yw'r arfer o ddisodli gwaith peirianneg a gweithredol ailadroddus, â llaw, â llifoedd gwaith dibynadwy, wedi'u gweithredu gan beiriant. O ran profi, mae hyn yn golygu [awtomeiddio profi](https://en.wikipedia.org/wiki/Test_automation): cyfresi prawf awtomataidd sy'n rhedeg yn barhaus i wirio cywirdeb, perfformiad, a diogelwch. O ran y broses, mae'n ymestyn i'r peiriannau cyfagos o gyflenwi meddalwedd a gweithrediadau: casglu tystiolaeth gydymffurfiaeth, gweithredu llyfrau rhedeg gweithredol, unioni problemau hysbys, a gorfodi rheolaethau llywodraethu, diogelwch, a chost. Mae'r syniad unedig yn syml. Dylai unrhyw beth a wneir yn ailadroddus ac yn ragweladwy gael ei godeiddio, fel ei fod yn rhedeg yn gyson, yn gyflym, a heb lafur dynol.

I dimau mawr, awtomeiddio yw'r unig ffordd i atal ansawdd a rheolaeth rhag chwalu o dan raddfa. Ni all profi â llaw gadw i fyny â channoedd o beirianwyr yn gwneud miloedd o newidiadau. Mae'n dod yn dagfa, ac mae ei sylw'n dod yn anghyson ac yn annibynadwy. Mae gweithdrefnau gweithredol â llaw yn dioddef hefyd. Mae ailgychwyn gwasanaeth, cylchdroi credential, a chasglu tystiolaeth archwilio i gyd yn dod yn araf ac yn agored i wallau pan fydd dynion blinedig yn eu gwneud dan bwysau ar draws ystad fawr. Mae awtomeiddio'r gwaith hwn yn gwneud canlyniadau'n ailadroddadwy. Mae hefyd yn rhyddhau peirianwyr medrus i ganolbwyntio ar y problemau trwm-o-farn sydd wirioneddol angen mewnwelediad dynol.

Mewn cyd-destunau menter a llywodraeth, awtomeiddio hefyd yw'r allwedd i wneud cydymffurfiaeth yn gynaliadwy. Rhaid i sefydliadau reoleiddiedig ddangos yn barhaus fod rheolaethau ar waith a bod tystiolaeth yn cael ei chasglu. Mae gwneud hyn â llaw yn ddrud, yn araf, ac yn agored i fylchau. Mae awtomeiddio casglu tystiolaeth a gorfodi rheolaethau'n troi cydymffurfiaeth o ymarfer tân cyfnodol i eiddo parhaus, y gellir ei wirio o'r system. Mae'r dull "cydymffurfiaeth fel cod" hwn yn lleihau cost ac yn cryfhau'r sicrwydd y mae archwilwyr a rheoleiddwyr yn ei fynnu.

## Egwyddorion allweddol

- Awtomeiddio gwaith sy'n cael ei ailadrodd, yn rhagweladwy, ac yn seiliedig ar reolau; cadwch ymdrech ddynol ar gyfer barn.
- Gwneud profion awtomataidd yn gyflym, yn ddibynadwy, ac yn benderfynol, neu byddant yn cael eu hanwybyddu.
- Rhedeg profion yn gyfochrog a'u symud yn gynharach fel bod adborth yn aros yn gyflym wrth i'r gyfres dyfu.
- Codeiddio gweithdrefnau gweithredol fel [llyfrau rhedeg](https://en.wikipedia.org/wiki/Runbook)-fel-cod fel eu bod wedi'u fersiynu, yn brofadwy, ac yn weithredadwy.
- Ffafrio awtomeiddio wedi'i integreiddio'n dda dros sgriptiau brau sy'n cael eu bolltio ar systemau o'r tu allan.
- Cynhyrchu tystiolaeth gydymffurfiaeth yn awtomatig fel is-gynnyrch llifoedd gwaith arferol.
- Cadw dyn yn y ddolen ar gyfer gweithredoedd risg-uchel; awtomeiddio'r diogel a'r rheolaidd yn gyntaf.

## Argymhellion

### Adeiladu seilwaith profi cyflym, dibynadwy, cyfochrog

Dim ond os yw peirianwyr yn ymddiried ynddi ac mae'n dychwelyd adborth yn gyflym y mae cyfres brawf yn werthfawr. Buddsoddwch mewn seilwaith profi sy'n rhedeg cyfresi'n gyfochrog ar draws llawer o weithwyr, fel bod cyfanswm amser wal-clog yn aros yn isel wrth i nifer y profion dyfu i'r miloedd. Strwythurwch y gyfres fel pyramid: llawer o [brofion uned](https://en.wikipedia.org/wiki/Unit_testing) cyflym, llai o brofion integreiddio, a nifer fach o brofion pen-i-ben. Yna mae'r rhan fwyaf o adborth yn cyrraedd mewn eiliadau. Dilëwch brofion sigledig yn ddidostur. Mae prawf sy'n methu bob hyn a hyn yn waeth na dim prawf, oherwydd mae'n hyfforddi peirianwyr i anwybyddu methiannau. Darparwch amgylcheddau profi darfodus, ar-alwad fel bod profion integreiddio a phen-i-ben yn rhedeg yn erbyn seilwaith realistig, ynysig.

### Awtomeiddio rhyddhau, cydymffurfiaeth, a chasglu tystiolaeth

Estynnwch awtomeiddio y tu hwnt i brofi i mewn i'r llif gwaith rhyddhau a chydymffurfiaeth. Gwnewch i'r biblinell gynhyrchu'r arteffactau y mae eu hangen ar archwilwyr yn awtomatig: cofnodion o bwy gymeradwyodd newid, pa brofion a redodd ac a lwyddodd, beth ganfu sganiau diogelwch, ac yn union pa arteffact a ddefnyddiwyd. Triniwch reolaethau fel cod, fel bod gwiriadau gofynnol yn cael eu gorfodi'n unffurf a'u canlyniadau'n cael eu cofnodi. Mae'r "cydymffurfiaeth fel cod" hwn yn troi casglu tystiolaeth o ras wyllt â llaw cyn archwiliad yn gofnod parhaus, cyfoes bob amser. Mae hefyd yn gwneud ystum cydymffurfiaeth y system yn arsylladwy ar unrhyw eiliad.

### Mabwysiadu ChatOps a llyfrau rhedeg-fel-cod

Codeiddiwch weithdrefnau gweithredol fel llyfrau rhedeg gweithredadwy a gedwir mewn rheolaeth fersiynau, yn hytrach na dogfennau rhyddiaith sy'n crwydro'n hen ffasiwn. Lle mae gweithdrefn yn ddiogel ac yn cael ei deall yn dda, gwifrwch hi i mewn i awtomeiddio a all ei rhedeg ar alwad. Mae ChatOps yn dod â'r gweithrediadau hyn i mewn i ryngwyneb sgwrsio a rennir, fel bod gweithredwyr yn sbarduno ac yn arsylwi gweithredoedd awtomataidd mewn sgwrs dryloyw, gydweithredol, wedi'i chofnodi. Mae hyn yn gwneud gweithrediadau'n weladwy i'r tîm cyfan ac yn creu cofnod awtomatig o'r hyn a wnaed. Mae hefyd yn gostwng y rhwystr i beirianwyr llai profiadol redeg gweithdrefnau'n ddiogel, oherwydd mae'r awtomeiddio'n amgodio'r camau cywir.

### Gweithredu unioni awtomataidd yn ofalus

Ar gyfer problemau ailadroddus, wedi'u deall yn dda, adeiladwch unioni awtomataidd sy'n canfod amod ac yn cymhwyso trwsiad hysbys, fel ailgychwyn proses wedi methu, graddio i fyny o dan lwyth, clirio disg llawn, neu fethu drosodd gydran. Dechreuwch gyda thrwsiadau risg-isel, hyder-uchel. Mynnwch gadarnhad dynol ar gyfer unrhyw beth â radiws ffrwydro sylweddol. Mae unioni awtomataidd yn lleihau amser cymedrig i adfer ac yn dileu blinder rhybudd ailadroddus. Ond rhaid ei adeiladu ar ganfod cadarn a chynnwys mesurau diogelu, oherwydd gall awtomeiddio sy'n gweithredu ar signal ffug ehangu digwyddiad. Cofnodwch bob gweithred awtomataidd, fel bod gweithredwyr yn cadw gwelededd llawn ac yn gallu camu i mewn.

### Gosod awtomeiddio proses robotig (RPA) yn gywir

Mae [awtomeiddio proses robotig](https://en.wikipedia.org/wiki/Robotic_process_automation) yn gyrru rhyngwynebau defnyddiwr a chymwysiadau presennol i awtomeiddio tasgau, gan ddynwared y cliciau a'r trawiadau bysellau y byddai dyn yn eu perfformio. Mae gan RPA le cyfreithlon fel pont ar gyfer systemau etifeddol neu drydydd parti nad ydynt yn dinoethi API ac na ellir eu hintegreiddio unrhyw ffordd arall. Defnyddiwch ef yn bragmataidd ar gyfer achosion o'r fath, ond gwybyddwch ei gyfyngiadau. Mae awtomeiddio wedi'i yrru gan UI yn frau yn ei hanfod: mae'n torri pryd bynnag y bydd y rhyngwyneb yn newid, ac nid yw'n mynd i'r afael â'r diffyg integreiddio sylfaenol. Lle mae API neu integreiddiad priodol ar gael, ffafriwch hwnnw. Triniwch RPA fel mesur dros dro tactegol, nid sylfaen strategol, a chynlluniwch i'w ddisodli wrth i systemau foderneiddio.

### Awtomeiddio rheolaethau llywodraethu, diogelwch, a chost

Amgodiwch reolaethau sefydliadol fel gwiriadau awtomataidd sy'n rhedeg yn barhaus: polisi-fel-cod ar gyfer waliau cadw seilwaith, sganio diogelwch awtomataidd mewn piblinellau, a chanfod awtomataidd o anomaleddau cost ac adnoddau segur. Mae awtomeiddio llywodraethu'n gwneud rheolaethau'n unffurf ac amhosibl eu hosgoi, ac mae'n graddio i gyfaint newid na allai adolygiad â llaw byth ei gwmpasu. Gall yr un dull sy'n gorfodi polisi diogelwch fflagio bil cwmwl sy'n rhedeg yn rhemp neu dag gofynnol coll. Mae llywodraethu'n symud o archwiliad â llaw cyfnodol i wal gadw awtomataidd barhaus.

## Cyfaddawdau: manteision ac anfanteision

| Dewis | Manteision | Anfanteision | Ffit gorau |
|---|---|---|---|
| Profi awtomataidd eang | Adborth cyflym, cyson; yn galluogi newid | Cost adeiladu a chynnal; risg sigledd | Pob tîm ar raddfa |
| Cydymffurfiaeth fel cod | Tystiolaeth barhaus, parod-i-archwilio | Peirianneg ymlaen llaw i godeiddio rheolaethau | Sefydliadau reoleiddiedig |
| Llyfrau rhedeg-fel-cod + ChatOps | Gweithrediadau ailadroddadwy, gweladwy, wedi'u cofnodi | Ymdrech i godeiddio a chynnal | Timau â llwyth gweithrediadau go iawn |
| Unioni awtomataidd | Adferiad cyflymach; llai o lafur | Risg os yw canfod yn anghywir | Materion ailadroddus wedi'u deall yn dda |
| RPA (awtomeiddio UI) | Yn pontio systemau heb API | Brau; yn cuddio bylchau integreiddio | Systemau etifeddol fel mesur dros dro |
| Llywodraethu awtomataidd | Rheolaethau unffurf, amhosibl eu hosgoi | Ymdrech awduro a thiwnio polisi | Ystadau mawr, wedi'u llywodraethu |

Y cyfaddawd canolog yw buddsoddiad ymlaen llaw yn erbyn llafur a risg parhaus. Mae awtomeiddio bob amser yn costio ymdrech i'w adeiladu a'i gynnal. Gall awtomeiddio a adeiladwyd yn wael, boed hynny'n brofion sigledig, RPA brau, neu unioni wedi'i sbarduno gan signalau gwael, fod yn waeth na dim, oherwydd mae'n erydu ymddiriedaeth neu'n ehangu methiannau. Mae'r ddisgyblaeth yn deirran: awtomeiddio'r hyn sy'n wirioneddol ailadroddus a dibynadwy, buddsoddi mewn gwneud yr awtomeiddio hwnnw'n ddibynadwy, a chadw dynion yn y ddolen lle mae barn neu risg uchel yn ei fynnu. Wedi'i wneud yn dda, mae awtomeiddio'n talu'n ôl sawl gwaith drosodd. Wedi'i wneud yn ddiofal, mae'n dod yn atebolrwydd ei hun.

## Cwestiynau i'w trafod gyda'ch tîm

1. **A yw eich profion integreiddio a phen-i-ben yn rhedeg yn erbyn amgylcheddau realistig, darfodus, neu yn erbyn blwch llwyfannu a rennir y mae pawb yn ymladd drosto?** Mae amgylcheddau ynysig ar-alwad fesul cais tynnu'n gadael i brofion integreiddio a phen-i-ben ymarfer seilwaith realistig heb i dimau rwystro'i gilydd na llygru cyflwr a rennir. Mae un amgylchedd llwyfannu a rennir yn dod yn dagfa ac yn ffynhonnell methiannau sigledig, dibynnol-ar-drefn wrth i fwy o dimau bentyrru arno. Penderfynwch a allwch chi godi amgylcheddau darfodus, faint maen nhw'n ei gostio, a pha brofion sydd wir angen amdanynt yn hytrach na dirprwy cof-mewnol cyflym. Dewch â data: pa mor aml y mae llwyfannu'n cael ei gystadlu, faint o fethiannau sy'n olrhain i ymyrraeth amgylchedd a rennir, a'r amser wal-clog cyfredol ar gyfer yr haen integreiddio. Mae'r ateb yn siapio eich dibynadwyedd profi a pha mor gyflym mae haenau uwch y pyramid yn dychwelyd adborth.

2. **A yw gweithdrefnau gweithredol wedi'u codeiddio fel llyfrau rhedeg-fel-cod ac wedi'u harddangos trwy ChatOps, neu a ydynt yn dal i fyw fel rhyddiaith sy'n crwydro'n hen ffasiwn?** Mae llyfrau rhedeg wedi'u codeiddio, wedi'u rheoli fersiynau'n brofadwy ac yn weithredadwy, ac mae eu rhedeg trwy ryngwyneb sgwrsio a rennir yn gwneud pob gweithred yn weladwy ac wedi'i chofnodi'n awtomatig. Mae hynny'n gostwng y rhwystr i beiriannydd ar-alwad llai profiadol weithredu'n ddiogel, oherwydd mae'r awtomeiddio'n amgodio'r camau cywir yn hytrach na dibynnu ar gof llwythol. Penderfynwch pa weithdrefnau sy'n ddiogel ac yn cael eu deall yn ddigon da i'w gwifro yn gyntaf, a sut rydych chi'n cadw'r dyn yn gallu camu i mewn. I ystad fawr mae'r tryloywder hwn hefyd yn gofnod archwilio o bwy wnaeth beth a phryd. Dewch â'ch llyfrau rhedeg presennol, nodwch pa rai sy'n hen, a nodwch y ddwy neu dair gweithdrefn sy'n cael eu rhedeg fwyaf i'w codeiddio yn gyntaf.

3. **Yn eich piblinell, pa sganiau diogelwch a gwiriadau polisi sy'n rhwystro cyfuniad, a pha rai sydd ond yn rhybuddio?** Mae'n werth adeiladu llywodraethu awtomataidd dim ond os yw'r rheolaethau'n amhosibl eu hosgoi, oherwydd mae gwiriad sydd ond yn rhybuddio'n cael ei anwybyddu dan bwysau terfyn amser yn union fel polisi wici. Penderfynwch, reolaeth wrth reolaeth, beth sy'n rhwystro a beth sy'n rhybuddio: mae gwendid critigol neu dag amgryptio coll yn debygol o rwystro, tra gallai canfyddiad arddull llai difrifol rybuddio. Ar raddfa, dyma sut rydych chi'n gorfodi waliau cadw diogelwch a chost yn unffurf ar draws cyfaint o newid na allai unrhyw adolygiad â llaw ei gwmpasu. Dewch â'ch rhestr eiddo gwiriadau presennol a marciwch bob un fel rhwystrol neu gynghorol, yna trafodwch y gyfradd positif ffug, oherwydd mae gwiriad rhwystrol swnllyd yn hyfforddi pobl i fynnu eithriadau. Y llinell rhwng rhwystro a rhybuddio yw lle mae gan eich llywodraethu ddannedd neu beidio.

4. **Pa unioni awtomataidd rydym yn barod i adael iddo weithredu heb i ddyn gadarnhau'n gyntaf, a beth yw'r radiws ffrwydro os yw'r canfod yn anghywir?** Mae unioni awtomataidd yn lleihau amser adfer a blinder rhybudd, ond gall trwsiad wedi'i sbarduno gan signal ffug droi pigyn bach yn doriad gwasanaeth llawn, felly mae'r penderfyniad ynghylch beth sy'n rhedeg heb neb yn gwylio'n benderfyniad risg, nid un cyfleustra. Pwyswch y tynfeydd cystadleuol: mae gweithred heb neb yn gwylio'n gyflymaf ond fwyaf risgus, tra bod cadarnhad dyn-yn-y-ddolen yn fwy diogel ond yn ailgyflwyno'r oedi a'r llafur roeddech chi'n ceisio eu tynnu i ffwrdd. Dewch â'r unioni ymgeisiol wedi'u graddio yn ôl amlder a radiws ffrwydro achos gwaethaf, cyfradd bositif ffug hanesyddol y canfod y tu ôl i bob un, ac a yw pob gweithred wedi'i chofnodi ac yn wrthdroadwy. I fenter fawr neu ystad llywodraeth, ychwanegwch awdurdod newid ffurfiol a chynllun dychwelyd ar gyfer unrhyw beth sy'n cyffwrdd â data cynhyrchu neu wasanaethau sy'n wynebu dinasyddion, oherwydd mae hunan-unioni na ellir ei archwilio na'i ddadwneud yn un y bydd rheoleiddiwr yn eich gorfodi i'w ddiffodd.

5. **Sut rydym yn ariannu ac yn dyrannu perchnogaeth ar gyfer cynnal ein hawtomeiddio fel nad yw'n pydru'n atebolrwydd?** Mae profion, llyfrau rhedeg, gwiriadau polisi, a bots RPA i gyd yn pydru wrth i'r systemau o'u cwmpas newid, ac mae awtomeiddio esgeulus yn waeth na dim: mae llyfr rhedeg hen yn rhoi hyder ffug mewn argyfwng ac mae bot RPA wedi torri'n gollwng gwaith yn dawel. Y tensiwn yw bod cynnal yn cystadlu â gwaith nodweddion am yr un peirianwyr, ac mae'n anweledig nes bod rhywbeth yn torri, felly dyma'r peth cyntaf i'w dorri dan bwysau terfyn amser. Dewch â'r rhestr eiddo gyfredol o asedau awtomeiddio, yr ôl-groniad profion sigledig a bots wedi torri, ac amcangyfrif gonest o oriau peiriannydd sydd eisoes yn mynd i gynnal o'i gymharu â'r hyn sydd wedi'i gyllidebu. Mewn lleoliad menter neu lywodraeth, enwch y perchennog atebol ar gyfer pob awtomeiddio critigol a chyllidebwch ei gynnal fel eitem llinell benodol, oherwydd bydd archwilwyr ac adolygiadau digwyddiad yn gofyn pwy oedd yn gyfrifol pan fethodd rheolaeth heb ei chynnal yn dawel.

6. **Ar gyfer pob system etifeddol rydym yn ei hawtomeiddio ag RPA, beth yw'r cynllun a'r sbardun penodol i ymddeol yr RPA hwnnw o blaid integreiddiad go iawn?** Mae RPA yn bont gyfreithlon ar gyfer systemau nad ydynt yn dinoethi API, ond mae pont heb gynllun ymadael yn caledu'n dawel yn seilwaith parhaol, brau sy'n torri ar bob newid UI ac yn gwreiddio'r union fwlch integreiddio roedd i fod i'w bontio. Mae'r cyfaddawd yn real: mae RPA yn cyflenwi gwerth yn gyflym ac yn rhad nawr, tra bod integreiddiad API priodol yn costio mwy ymlaen llaw ond yn wydn, felly'r ddisgyblaeth yw trin RPA fel benthyciad wedi'i ddyddio, nid pryniant. Dewch â'r rhestr o bots RPA mewn cynhyrchiad, y systemau y mae pob un yn dibynnu arnynt, pa mor aml y mae pob un yn torri, ac a yw ymdrech moderneiddio neu integreiddio wedi'i hariannu a'i hamserlennu mewn gwirionedd ar gyfer y system sylfaenol. Ar gyfer ystadau menter a llywodraeth sy'n cario cymwysiadau craidd degawdau oed, clymwch bob bot RPA wrth garreg filltir moderneiddio wedi'i henwi, oherwydd mae RPA sydd wedi dod yn dawel yn hollbwysig heb ddyddiad ymddeol yn ddyled dechnegol sy'n cyfansymio bob blwyddyn y mae'r rhyngwyneb y mae'n ei grafu'n parhau i newid.

## Lens sector

**Cwmni newydd.** Gyda dau neu dri pheiriannydd a dim amser i adeiladu seilwaith, cadwch byramid profi bach, cyflym sy'n rhedeg mewn ychydig funudau ar bob newid, a thriniwch unrhyw brawf sigledig fel gwall go iawn i'w drwsio neu ei ddileu'r wythnos honno. Hepgorwch offer cydymffurfiaeth trwm a pholisi-fel-cod nad oes eu hangen arnoch eto, a chodeiddiwch ddim ond eich dwy neu dair trwsiad gweithredol sy'n cael eu rhedeg fwyaf fel sgriptiau syml wedi'u sbarduno o sgwrs. Awtomeiddiwch yr hyn sy'n dileu llafur dyddiol, a gwrthsefwch adeiladu peiriannau llywodraethu cyn bod gennych broblem lywodraethu.

**Busnes bach.** Heb arbenigwr profi neu blatfform penodedig, pwyswch ar awtomeiddio wedi'i bobi i mewn i offer rydych chi eisoes yn talu amdanynt: rhedwyr profi mewnol gwasanaeth CI, ei ychwanegion sganio, ac amgylcheddau wedi'u rheoli yn hytrach nag adeiladwaith seilwaith-profi pwrpasol. Fframiwch y dewis prynu-yn-erbyn-adeiladu o amgylch cynnal y gallwch ei gynnal mewn gwirionedd, oherwydd mae piblinell bwrpasol glyfar na all neb ei chynnal yn ganlyniad gwaeth na un letyol plaen. Defnyddiwch RPA yn gynnil a dim ond lle mae offeryn gwerthwr yn pontio system na allwch ei integreiddio unrhyw ffordd arall.

**Menter.** Ar draws llawer o dimau'r nod yw rheolaethau unffurf, amhosibl eu hosgoi ar raddfa na all adolygiad â llaw ei gwmpasu: seilwaith profi cyfochrog a rennir gydag amgylcheddau darfodus, waliau cadw polisi-fel-cod, a thystiolaeth gydymffurfiaeth wedi'i chynhyrchu'n awtomatig o bob rhediad piblinell. Safonwch y rhyngwynebau fel bod timau'n ailddefnyddio offer unioni a llyfrau rhedeg yn hytrach na phob un yn ailddyfeisio sgriptiau brau, a rheolwch awtomeiddio fel portffolio wedi'i berchnogi, wedi'i ariannu gyda chyllidebau cynnal clir. Gwyliwch nad yw gwiriad sydd ond yn rhybuddio mewn un tîm yn cael ei drin fel rhwystrol mewn tîm arall, oherwydd mae gorfodaeth anghyson yn tanseilio'r sicrwydd rydych chi'n talu amdano.

**Llywodraeth.** Mae rheolau caffael, dyletswyddau tryloywder, a mandadau monitro parhaus yn gwneud cydymffurfiaeth fel cod yn agos at hanfodol: dylai pob rhediad piblinell gofnodi'r rheolaethau a wiriwyd, y sganiau a berfformiwyd, a'r cymeradwyaethau a roddwyd fel tystiolaeth wrth-ymyrryd, barod-i-archwilio. Ffafriwch awtomeiddio agored, cludadwy dros glymu perchnogol fel y gall contract yn y dyfodol symud at gyflenwr arall, a chadwch ddyn yn atebol am unrhyw unioni sy'n cyffwrdd â gwasanaethau sy'n wynebu dinasyddion. Lle mae system ddegawdau oed yn gorfodi RPA, dogfennwch ef fel pont fwriadol, dros dro gyda chynllun moderneiddio cyhoeddus, a chadwch wiriadau llywodraethu at y llinell sylfaen ddiogelwch orfodol ar bob newid.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd saith person yn cadw pyramid profi tenau o'r rhan fwyaf o brofion uned cyflym ynghyd ag ychydig o brofion integreiddio, i gyd yn rhedeg yn gyfochrog fel bod y gyfres lawn yn gorffen mewn llai na thri munud ar bob cais tynnu. Pan fydd prawf yn dechrau sigledu, maen nhw'n ei drin fel gwall go iawn ac yn ei drwsio neu'n ei ddileu'r wythnos honno, oherwydd gyda thîm mor fach byddai un adeiladwaith coch wedi'i anwybyddu'n erydu ymddiriedaeth yn y gyfres gyfan. Maen nhw hefyd yn codeiddio'u dwy drwsiad weithredol fwyaf cyffredin, ailgychwyn gweithiwr sownd a chlirio disg llawn, fel sgriptiau bach wedi'u sbarduno o Slack, fel y gall pwy bynnag sydd ar alwad eu rhedeg yn ddiogel heb bagio'r un peiriannydd a'u hysgrifennodd.

**Menter.** Mae cwmni e-fasnach mawr yn rhedeg cyfres brawf o ddegau o filoedd o brofion, wedi'u cyfochri ar draws fflyd o weithwyr fel bod y gyfres lawn yn cwblhau mewn munudau. Mae amgylcheddau darfodus yn codi fesul cais tynnu ar gyfer profi integreiddio realistig. Mae gweithrediadau'n rhedeg trwy ChatOps: mae peirianwyr ar-alwad yn sbarduno llyfrau rhedeg wedi'u codeiddio o sgwrs, ac mae methiannau cyffredin fel gwasanaeth wedi'i orlwytho'n cael eu hunioni'n awtomatig, gyda'r weithred wedi'i chofnodi ar gyfer adolygiad. Mae'r biblinell yn casglu tystiolaeth sganio diogelwch a chymeradwyaeth yn awtomatig, fel bod yr archwiliad blynyddol yn tynnu ar gofnod cyfoes bob amser yn hytrach na hela tystiolaeth â llaw.

**Llywodraeth.** Mae asiantaeth gyhoeddus sy'n ddarostyngedig i ofynion monitro parhaus llym yn gweithredu cydymffurfiaeth fel cod. Mae pob rhediad piblinell yn cofnodi'r rheolaethau a wiriwyd, y sganiau a berfformiwyd, a'r cymeradwyaethau a roddwyd, gan gynhyrchu tystiolaeth wrth-ymyrryd sy'n bodloni archwilwyr ar alwad. Gan fod un o'i systemau craidd yn gymhwysiad degawdau oed heb API, mae'r asiantaeth yn defnyddio RPA fel pont fwriadol i awtomeiddio mewnbynnu data iddo tra bod ymdrech moderneiddio'n mynd rhagddi, gyda chynllun penodol i ymddeol yr RPA unwaith y bydd integreiddiad priodol yn bodoli. Mae gwiriadau llywodraethu awtomataidd yn gorfodi'r llinell sylfaen ddiogelwch orfodol ar bob newid seilwaith.

## Achos busnes: cymhellion, ROI, a TCO

Mae ROI awtomeiddio profi a phrosesau'n ymddangos fel amser peiriannydd wedi'i adennill, cyflenwi cyflymach a mwy diogel, adferiad digwyddiadau cyflymach, a chost cydymffurfiaeth is yn ddramatig. Mae profi awtomataidd yn galluogi'r newid cyflym, hyderus sy'n sail i berfformiad cyflenwi. Mae gweithrediadau ac unioni awtomataidd yn torri'r llafur a'r amser segur sy'n draenio timau a chyllidebau. Gall cydymffurfiaeth fel cod droi archwiliad o wythnosau o baratoi â llaw yn ymholiad rheolaidd, arbediad sy'n ariannol ac yn enw-da fel ei gilydd.

Mae'r cymhariaeth TCO yn pwyso cost real, barhaus adeiladu a chynnal awtomeiddio yn erbyn cost peidio ag awtomeiddio. Nid dim ond yr oriau a dreulir y mae profi a gweithrediadau â llaw yn eu costio. Maent hefyd yn costio'r diffygion sy'n dianc, y digwyddiadau sy'n rhedeg yn hir, yr archwiliadau sy'n bwyta staff arbenigol, a llosgi allan peirianwyr sy'n gwneud llafur ailadroddus. I arweinyddiaeth, mae'r ddadl yn syml: mae awtomeiddio'n trawsnewid treuliad a risg gweithredol ailadroddus yn fuddsoddiad unwaith-a-chynnal sy'n graddio, ac mae'n gwneud ansawdd a chydymffurfiaeth yn barhaus yn hytrach nag yn achlysurol. Mae un rhybudd yn werth ei nodi'n glir. Rhaid cynnal ac ymddiried mewn awtomeiddio; mae awtomeiddio heb ei ariannu, esgeulus yn pydru'n atebolrwydd.

## Gwrth-batrymau a pheryglon

- **Profion sigledig wedi'u goddef.** Mae methiannau ysbeidiol yn dinistrio ymddiriedaeth ac yn hyfforddi peirianwyr i anwybyddu canlyniadau coch.
- **Awtomeiddio proses wedi torri.** Mae awtomeiddio llif gwaith gwael ond yn gwneud i'r llanast ddigwydd yn gyflymach; trwsiwch y broses yn gyntaf.
- **RPA fel strategaeth.** Mae dibynnu ar awtomeiddio UI brau fel ateb parhaol yn cuddio ac yn gwreiddio bylchau integreiddio.
- **Unioni heb ganfod cadarn.** Gall trwsiadau awtomataidd wedi'u sbarduno gan signalau gwael ehangu digwyddiad.
- **Llyfrau rhedeg fel rhyddiaith hen.** Mae gweithdrefnau sy'n byw mewn dogfennau hen ffasiwn yn rhoi hyder ffug mewn argyfwng.
- **Tystiolaeth gydymffurfiaeth wedi'i chasglu â llaw.** Mae helfeydd tystiolaeth â llaw cyfnodol yn ddrud ac yn gadael bylchau rhwng archwiliadau.
- **Dim dyn yn y ddolen ar gyfer gweithredoedd risg-uchel.** Mae awtomeiddio llawn o weithrediadau peryglus yn dileu'r farn sy'n atal trychinebau.

## Model aeddfedrwydd

**Lefel 1, Cychwyn.** Mae profi a gweithrediadau'n bennaf â llaw ac yn adweithiol. Mae sylw'n ad hoc, mae gweithdrefnau'n byw ym mhennau pobl neu ddogfennau hen, mae unioni'n digwydd â llaw yn ystod digwyddiadau, a chaiff tystiolaeth gydymffurfiaeth ei chasglu ar ras cyn pob archwiliad.

**Lefel 2, Datblygu.** Mae profion awtomataidd yn bodoli ond yn araf, yn sigledig, neu'n rhedeg yn anghyson, ac mae arferion yn amrywio'n eang rhwng timau. Mae rhai sgriptiau gweithredol a llyfrau rhedeg yn bodoli mewn pocedi, ond mae unioni'n dal yn â llaw ac mae llywodraethu'n cael ei orfodi trwy adolygiad cyfnodol yn hytrach na gwiriadau parhaus.

**Lefel 3, Safoni.** Mae seilwaith profi cyflym, cyfochrog, dibynadwy'n safon ddogfennedig ar draws y sefydliad. Mae llyfrau rhedeg-fel-cod a ChatOps mewn defnydd cyffredinol, mae tystiolaeth gydymffurfiaeth yn cael ei chynhyrchu'n awtomatig o rediadau piblinell, ac mae rheolaethau llywodraethu'n rhedeg fel gwiriadau awtomataidd wedi'u gorfodi, wedi'u cymhwyso'n gyson ar draws timau.

**Lefel 4, Rheoli.** Caiff yr awtomeiddio ei hun ei fesur a'i reoli yn erbyn llinellau sylfaen. Rydych chi'n tracio cyfradd profion sigledig, amser wal-clog cyfres, amser cymedrig i adfer ar gyfer digwyddiadau wedi'u hunioni'n awtomatig, cyfran y rheolaethau â thystiolaeth awtomataidd, a chyfraddau positif ffug ar wiriadau rhwystrol, ac rydych chi'n dal pob metrig i darged y cytunwyd arno. Caiff penderfyniadau unioni a sylw eu gyrru gan y data hwn, ac mae pob gweithred awtomataidd wedi'i chofnodi fel bod tueddiadau ac atchweliadau'n weladwy yn hytrach nag yn cael eu dyfalu.

**Lefel 5, Cerddorfa.** Caiff awtomeiddio ei wella'n barhaus a'i integreiddio ar draws y sefydliad. Mae unioni awtomataidd yn trin digwyddiadau rheolaidd gyda mesurau diogelu profedig, mae cydymffurfiaeth yn barhaus ac yn barod-i-archwilio bob amser, ac mae'r cadwyni offer profi, gweithrediadau, a llywodraethu'n addasu wrth i systemau newid, gyda phontydd RPA yn cael eu hymddeol yn weithredol wrth i integreiddiadau aeddfedu. Mae dynion yn canolbwyntio ar farn tra bod peiriannau'n trin yr ailadroddadwy, ac mae'r system gyfan yn ail-gydbwyso ar dystiolaeth.

## Syniadau ar gyfer trafodaeth

- Pa weithdrefnau gweithredol sy'n ddiogel i'w hawtomeiddio'n llawn, a pha rai sy'n rhaid cadw dyn yn y ddolen?
- Sut rydych chi'n cadw cyfres brawf fawr yn gyflym ac yn rhydd o sigledd wrth iddi dyfu?
- Ble mae RPA yn bont gyfiawnadwy ar gyfer eich systemau etifeddol, a beth yw'r cynllun i'w ymddeol?
- Pa reolaethau y gallech eu trosi o archwiliad â llaw i gydymffurfiaeth barhaus fel cod yn gyntaf?
- Sut rydych chi'n adeiladu ymddiriedaeth mewn unioni awtomataidd heb risgio digwyddiadau wedi'u hehangu?
- Sut rydych chi'n ariannu'r cynnal parhaus y mae awtomeiddio'n ei fynnu fel nad yw'n pydru'n atebolrwydd?

## Prif gasgliadau

- Awtomeiddio'r ailadroddus, y rhagweladwy, a'r seiliedig-ar-reolau; cadwch ymdrech ddynol ar gyfer barn a phenderfyniadau risg-uchel.
- Gwneud profion awtomataidd yn gyflym, yn gyfochrog, ac yn ddibynadwy, a dileu sigledd yn ddidostur.
- Codeiddio gweithrediadau fel llyfrau rhedeg-fel-cod a'u harddangos trwy ChatOps ar gyfer gwelededd a chofnod.
- Cynhyrchu tystiolaeth gydymffurfiaeth yn awtomatig fel bod archwiliadau'n tynnu ar gofnod parhaus, cyfoes.
- Defnyddio RPA dim ond fel pont fwriadol, dros dro ar gyfer systemau heb API, a chynllunio ei ymddeoliad.
- Gorfodi rheolaethau llywodraethu, diogelwch, a chost fel gwiriadau awtomataidd parhaus, gyda dynion yn goruchwylio'r gweithredoedd risgus.

## Cyfeiriadau a darllen pellach

- Lisa Crispin a Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*.
- Jez Humble a David Farley, *Continuous Delivery*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, a Niall Richard Murphy (goln.), *Site Reliability Engineering* (gweler y bennod ar ddileu llafur).
- Gene Kim, Jez Humble, Patrick Debois, a John Willis, *The DevOps Handbook*.
- Nicole Forsgren, Jez Humble, a Gene Kim, *Accelerate*.
- NIST Special Publication 800-53 a 800-137 (monitro parhaus).
- Dogfennaeth Open Policy Agent (polisi fel cod).
