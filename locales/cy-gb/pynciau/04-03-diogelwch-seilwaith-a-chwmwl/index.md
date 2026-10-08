# 4.3 Seilwaith a diogelwch cwmwl

## Trosolwg a chymhelliant

Mae cymwysiadau'n rhedeg ar seilwaith, ac y dyddiau hyn mae'r seilwaith hwnnw i raddau helaeth yn seiliedig ar gwmwl, wedi'i ddiffinio gan feddalwedd, ac yn newid o hyd. Gall un peiriannydd bellach ddarparu cronfa ddata, agor llwybr rhwydwaith, neu ganiatáu caniatâd gydag un gorchymyn, ar raddfa a chyflymder na ragwelodd rheolaeth newid draddodiadol erioed. Dyna'n union pam mai cam-ffurfweddu, nid ecsbloetiadau egsotig, yw prif achos toriadau diogelwch cwmwl. Gall bwced storio cyhoeddus ddamweiniol neu rôl mynediad rhy eang ddatgelu data sefydliad cyfan mewn eiliadau.

I fentrau mawr, mae seilwaith cwmwl yn rhychwantu darparwyr lluosog, miloedd o gyfrifon, a chymysgedd o wasanaethau a reolir, cynwysyddion, a ffwythiannau di-weinydd. Nid perimedr statig yw'r arwyneb ymosod. Casgliad byw, gwasgaredig o adnoddau a hunaniaethau ydyw. I lywodraeth, mae'r un cymhlethdod yn cwrdd â threfnau awdurdodi llym, mandadau preswyliaeth data, a ffiniau dosbarthiad sy'n siapio pob dewis pensaernïol. Yn y ddau achos, mae'r haen hunaniaeth wedi dod yn berimedr newydd: pwy sy'n gallu gwneud beth, i ba adnodd, o dan ba amodau.

Mae'r bennod hon yn ymdrin â sut i ddiogelu'r sylfaen honno: [rheoli hunaniaeth a mynediad](https://en.wikipedia.org/wiki/Identity_management) (IAM), [segmentu rhwydwaith](https://en.wikipedia.org/wiki/Network_segmentation), [amgryptio](https://en.wikipedia.org/wiki/Encryption) a [rheoli allweddi](https://en.wikipedia.org/wiki/Key_management), diogelwch cynwysyddion a llwythi gwaith [di-weinydd](https://en.wikipedia.org/wiki/Serverless_computing), a'r rheolaeth osgo barhaus sy'n cadw ystad cwmwl sy'n symud yn gyflym rhag crwydro i berygl.

## Egwyddorion allweddol

- **Hunaniaeth yw'r perimedr.** Mae penderfyniadau mynediad yn dibynnu ar hunaniaeth gref ac awdurdodi manwl, nid lleoliad rhwydwaith.
- **Y fraint leiaf, bob amser.** Mae pob hunaniaeth, dynol neu beiriannol, yn cael y caniatâd lleiaf sydd ei angen, a dim mwy.
- **Segmentwch i gyfyngu.** Rhannwch rwydweithiau a llwythi gwaith fel na all toriad diogelwch mewn un ardal ledaenu'n rhydd.
- **Amgryptiwch ym mhobman.** Diogelwch ddata ar dramwy ac wrth orffwys yn ddiofyn, gyda allweddi wedi'u rheoli'n dda.
- **Anghyfnewidiol a datganiadol.** Diffiniwch seilwaith fel cod (IaC), defnyddiwch yn anghyfnewidiol, a thrinwch grwydro fel diffyg.
- **Gwirio parhaus.** Nid archwiliad un-tro yw osgo; sganiwch a gorfodwch yn barhaus.
- **Diogel yn ôl ffurfweddiad diofyn.** Dylai cyflwr diofyn unrhyw adnodd fod wedi'i gloi i lawr, nid ar agor.

## Argymhellion

### Dylunio rheoli hunaniaeth a mynediad yn fwriadol

IAM yw'r rhan bwysicaf o ddiogelwch cwmwl, a'r un a gaiff ei chamreoli amlaf.

- Defnyddiwch **[reolaeth mynediad seiliedig ar rôl](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC)** i ganiatáu caniatâd yn ôl swyddogaeth swydd, a **[rheolaeth mynediad seiliedig ar briodoledd](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC)** lle mae angen penderfyniadau manylach, ymwybodol o gyd-destun (yn seiliedig ar dagiau, amgylchedd, dosbarthiad data, neu amser).
- Dilëwch dystlythyrau statig hirhoedlog o blaid tocynnau byrhoedlog, a gyhoeddir yn awtomatig, a ffederasiwn hunaniaeth llwyth gwaith.
- Gorfodwch [MFA](https://en.wikipedia.org/wiki/Multi-factor_authentication) (dilysu aml-ffactor) ar gyfer pob mynediad dynol a mynnwch ddilysu cryf ar gyfer gweithredoedd breintiedig.
- Cymhwyswch y fraint leiaf yn drylwyr: dechreuwch o sero ac ychwanegwch ganiatâd yn fwriadol. Adolygwch a thocio caniatâd nas defnyddiwyd yn rheolaidd; mae mynediad yn tueddu i gronni.
- Gwahanwch ddyletswyddau fel na all yr un hunaniaeth sengl wneud a chymeradwyo newidiadau sensitif ill dau.
- Defnyddiwch gyfrifon neu brosiectau pwrpasol i greu ffiniau caled rhwng amgylcheddau (cynhyrchu, llwyfannu, datblygu) a rhwng unedau busnes.

### Segmentu rhwydweithiau a micro-segmentu llwythi gwaith

Mae rhwydweithiau gwastad yn gadael i ymosodwyr grwydro i'r ochr unwaith y maen nhw i mewn. Rhannwch a chyfyngwch.

- Segmentwch ar lefel y rhwydwaith yn haenau a pharthau, gan ganiatáu dim ond y traffig y mae gwir angen pob haen amdano.
- Cymhwyswch **ficro-segmentu** fel bod llwythi gwaith unigol ond yn cyfathrebu â'r cymheiriaid penodol y mae eu hangen arnynt, wedi'i orfodi gan bolisi ymwybodol o hunaniaeth yn hytrach na rheolau is-rwyd eang.
- Diofynnwch i wrthod traffig dwyrain-gorllewin; mynnwch reolau caniatáu eglur.
- Rhowch storfeydd data sensitif mewn is-rwydi preifat heb ddim datguddiad rhyngrwyd uniongyrchol, i'w cyrraedd trwy lwybrau a reolir yn unig.
- Defnyddiwch gysylltedd preifat i wasanaethau a reolir yn lle llwybro dros y rhyngrwyd gyhoeddus lle bo hynny'n bosibl.

### Amgryptio data a rheoli allweddi'n briodol

Nid yw amgryptio byth yn gryfach na'r rheolaeth allweddi y tu ôl iddo.

- Amgryptiwch **ar dramwy** gyda [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Diogelwch Haen Drafnidiaeth) cyfredol ym mhobman, gan gynnwys traffig gwasanaeth-i-wasanaeth mewnol.
- Amgryptiwch **wrth orffwys** yn ddiofyn ar gyfer pob storfa, cronfa ddata, a chefnogion.
- Rheolwch allweddi gyda **Gwasanaeth Rheoli Allweddi (KMS)**, a defnyddiwch [Fodwl Diogelwch Caledwedd](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM) ar gyfer yr allweddi sicrwydd uchaf a ar gyfer gofynion rheoleiddiol.
- Cylchdrowch allweddi ar amserlen a chefnogwch gylchdroi cyflym ar amheuaeth o gyfaddawdu.
- Rheolwch ac archwiliwch pwy all ddefnyddio a rheoli allweddi ar wahân i bwy all gyrchu'r data, fel bod dalfa allweddi'n gorfodi gwahanu dyletswyddau.
- Ystyriwch allweddi a reolir gan gwsmeriaid lle mae rheoleiddio neu ymddiriedaeth gontractiol yn ei gwneud yn ofynnol i'r sefydliad ddal yr allweddi yn hytrach na'r darparwr.

### Diogelu cynwysyddion, Kubernetes, a di-weinydd

Mae pob model cyfrifiadura'n dod â'i risgiau ei hun.

- **Cynwysyddion:** adeiladwch o ddelweddau sylfaen isafswm, dibynadwy; sganiwch ddelweddau am wendidau cyn defnyddio; rhedwch fel dim-gwraidd; gwnewch systemau ffeiliau'n ddarllen-yn-unig lle bo hynny'n bosibl; a pheidiwch byth â phobi cyfrinachau i mewn i ddelweddau.
- **[Kubernetes](https://en.wikipedia.org/wiki/Kubernetes):** galluogwch RBAC a chwmpaswch gyfrifon gwasanaeth yn dynn; cymhwyswch bolisïau rhwydwaith ar gyfer micro-segmentu; defnyddiwch reolwyr derbyn a pheiriannau polisi i orfodi safonau; cyfyngwch gynwysyddion breintiedig; ynyswch lwythi gwaith sensitif; a chadwch yr awyren reoli a'r nodau wedi'u clytio.
- **Di-weinydd:** cymhwyswch y fraint leiaf i rôl gweithredu pob ffwythiant (ffynhonnell gyffredin o or-ganiatáu); dilyswch bob mewnbwn digwyddiad; rheolwch gyfrinachau trwy storfa gyfrinach y platfform; a monitrwch batrymau galw anghyffredin.

Beth bynnag yw'r model, cadwch yr amser rhedeg wedi'i glytio a'r delweddau'n ffres. Nid yw cynhwysydd yn fwy diogel na'r feddalwedd sydd ynddo.

### Rheoli osgo diogelwch cwmwl yn barhaus

Mae'r cwmwl yn newid yn llawer rhy gyflym i archwiliadau â llaw cyfnodol allu dal i fyny.

- Mabwysiadwch offer **Rheoli Osgo Diogelwch Cwmwl (CSPM)** i ganfod cam-ffurfweddiadau, datguddiad cyhoeddus, a thoriadau polisi'n barhaus ar draws cyfrifon.
- Diffiniwch bolisi diogelwch fel cod a'i orfodi ar adeg defnyddio fel bod ffurfweddiadau gwael yn cael eu rhwystro cyn iddynt lanio.
- Ffafriwch atal (cynwal diogelwch sy'n atal cam-ffurfweddu) dros ganfod (rhybuddion ar ôl y ffaith), a chyfunwch y ddau.
- Cynhaliwch restr eiddo gywir o adnoddau a hunaniaethau; ni allwch ddiogelu'r hyn na allwch ei weld.
- Traciwch ac unionwch grwydro rhwng seilwaith-fel-cod datganedig a'r cyflwr rhedeg gwirioneddol.

## Cyfaddawdau: manteision ac anfanteision

| Penderfyniad | Manteision | Anfanteision |
|---|---|---|
| RBAC | Syml, dealladwy, hawdd ei archwilio | Bras, ffrwydrad rolau ar raddfa fawr |
| ABAC | Manwl, ymwybodol o gyd-destun, yn graddio gyda thagiau | Cymhleth i'w ddylunio a rhesymu amdano |
| Allweddi a reolir gan ddarparwr (KMS) | Hawdd, integredig, baich gweithredol isel | Y darparwr sy'n dal dalfa; llai o reolaeth |
| Allweddi/HSM a reolir gan gwsmeriaid | Rheolaeth lawn, yn bodloni mandadau llym | Baich gweithredol, risg colli allweddi |
| Cynwal diogelwch ataliol | Yn atal cam-ffurfweddu cyn iddo ddigwydd | Gall rwystro gwaith dilys, angen tiwnio |
| CSPM canfyddol yn unig | Hyblyg, di-rwystro | Gall niwed ddigwydd cyn canfod |
| Micro-segmentu | Cyfyngiant cryf ar symudiad ochrol | Cymhlethdod gweithredol, gwasgariad polisi |

Y prif gyfaddawd yw rheolaeth yn erbyn baich gweithredol. Mae rheolaethau tynnach (allweddi a reolir gan gwsmeriaid, micro-segmentu llym, ABAC) yn lleihau risg, ond maent yn mynnu arbenigedd a chynnal a chadw y mae timau bach yn ei chael hi'n anodd eu cynnal. Mae'r lefel gywir yn dibynnu ar ba mor sensitif yw'r data a pha reoliadau sy'n berthnasol. Mae dull pragmatig yn haenu diofynion diogel cryf i bawb, yna'n cadw trylwyredd ychwanegol ar gyfer y systemau risg uchaf, ac mae'n ffafrio cynwal diogelwch awtomataidd sy'n gwneud y dewis diogel yn ddiofyn yn hytrach na disgyblaeth â llaw.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Ble byddwch chi'n tynnu ffiniau caled cyfrif neu brosiect, a beth sy'n perthyn y tu mewn i bob un?** Mae cyfrifon a phrosiectau pwrpasol yn creu'r cyfyngiant cryfaf y mae'r cwmwl yn ei gynnig, fel na all cyfaddawdu mewn datblygu gyrraedd cynhyrchu ac na all un uned fusnes gyffwrdd â data uned arall. Penderfynwch eich cynllun ffiniau cyn i'ch ystad dyfu i filoedd o gyfrifon, oherwydd mae ôl-osod ynysiad ar strwythur gwastad yn araf ac yn beryglus. I waith menter a llywodraeth, mae'r ffiniau hyn hefyd yn mapio'n lân i wahanu amgylchedd, dosbarthiad data, a therfynau radiws ffrwydrad y mae archwilwyr yn disgwyl eu gweld. Dewch â diagram cyfredol o ba lwythi gwaith sy'n rhannu cyfrif heddiw a nodwch lle mae un rôl rhy eang yn rhychwantu cynhyrchu a di-gynhyrchu. Os yw data sensitif yn eistedd yn yr un cyfrif â llwythi gwaith arbrofol, dyna'r ffin i'w thrwsio gyntaf.

2. **Beth yw eich safon ar gyfer pwy all reoli allweddi yn erbyn pwy all gyrchu'r data wedi'i amgryptio?** Nid yw amgryptio'n gryfach na rheolaeth allweddi, ac mae gwahanu dalfa allweddi oddi wrth fynediad data'n troi eich KMS yn bwynt gorfodi ar gyfer gwahanu dyletswyddau. Penderfynwch pwy sy'n cael creu, cylchdroi, a defnyddio allweddi, a gwnewch yn siŵr nad yw'r set honno'n gorgyffwrdd â'r bobl sy'n gallu darllen y data y mae'r allweddi hynny'n ei ddiogelu. I systemau a reoleiddir a llywodraeth, mae hyn yn aml yn gyrru'r dewis rhwng allweddi a reolir gan ddarparwr ac allweddi a reolir gan gwsmeriaid neu HSMs, sy'n cario mwy o reolaeth a mwy o risg weithredol o golli allweddi. Dewch â'ch polisïau allweddi cyfredol a gwiriwch a all yr un hunaniaeth sengl reoli allwedd a darllen y data y tu ôl iddi ill dau, oherwydd dyna fwlch tawel cyffredin. Os na chaiff dalfa a mynediad eu rhannu, mae amgryptio wrth orffwys yn eich diogelu llai nag y mae'r dangosfwrdd yn ei awgrymu.

3. **Sut fyddwch chi'n gwneud diofynion diogel yn anochel yn eich parth glanio yn hytrach na dim ond yn cael eu hargymell?** Cam-ffurfweddu, nid ecsbloetiadau egsotig, yw prif achos toriadau diogelwch cwmwl, a'r ateb yw cynwal diogelwch ataliol sy'n rhwystro cronfa ddata gyhoeddus neu fwced heb ei amgryptio cyn iddo lanio, nid rhybuddion ar ôl y ffaith. Penderfynwch pa bolisïau y byddwch yn eu gorfodi ar adeg defnyddio (dim storio cyhoeddus, amgryptio ymlaen yn ddiofyn, tagiau gorfodol) a pha rai y byddwch ond yn eu canfod a'u hadrodd. I dîm mawr, mae amgodio'r rhain i mewn i barthau glanio a thempledi seilwaith-fel-cod yn golygu bod pob cyfrif newydd yn etifeddu diogelwch heb ymdrech fesul tîm, gan droi diogelwch o dreth ailadroddus yn fuddsoddiad un-tro. Dewch â'ch canfyddiadau cam-ffurfweddu o'r mis diwethaf a gofynnwch pa rai y byddai cynwal diogelwch ataliol wedi'u hatal yn llwyr. Os nad yw eich rheolaeth osgo ond yn ganfyddol, gall niwed ddigwydd cyn i unrhyw un weld y rhybudd, felly symudwch y gwiriadau effaith uchaf i atal.

4. **Sut ydych chi'n dileu tystlythyrau statig hirhoedlog heb dorri'r awtomeiddio sy'n dibynnu arnynt yn dawel?** Mae allweddi mynediad wedi'u mewnblannu nad ydynt byth yn dod i ben ymhlith achosion mwyaf cyffredin toriadau diogelwch cwmwl, oherwydd mae un allwedd wedi'i gollwng mewn sgript, log, neu ystorfa'n rhoi mynediad parhaus i ymosodwr. Y tyniad sy'n cystadlu yw gweithredol: mae swyddi CI etifeddol, tasgau cron, ac integreiddiadau trydydd parti yn aml yn tybio bod allwedd statig yn bodoli, ac mae ei throi drosodd i docynnau byrhoedlog neu ffederasiwn hunaniaeth llwyth gwaith yn cymryd amser peirianneg nad oedd neb wedi'i amserlennu. I dîm mawr, mae llwybr mudo a rennir (cyhoeddi tocynnau'n awtomatig, gosod safon dod i ben, a rhybuddio ar unrhyw allwedd hirhoedlog newydd) yn atal pob grŵp rhag dyfeisio ei ateb gwannach ei hun. Dewch â rhestr eiddo o bob tystlythyr statig sy'n cael ei ddefnyddio, ei oedran, ei radiws ffrwydrad, ac a all y system y mae'n ei bwydo dderbyn hunaniaeth ffederal heddiw. Mewn lleoliadau menter a llywodraeth, cysylltwch y dyddiad cau â chylchoedd archwilio ac awdurdodi, oherwydd tystlythyr sy'n goroesi'r person a'i creodd yw'n union y canfyddiad sy'n stelio awdurdodiad parhaus.

5. **Pan fydd adnodd wedi'i gam-ffurfweddu neu allwedd wedi'i chyfaddawdu, pa mor gyflym allwch chi ei ganfod, ei gyfyngu, a'i unioni, ac a ydych chi wedi mesur hynny?** Nid yw bwced cyhoeddus neu rôl rhy eang yn fwy peryglus na'r ffenestr y mae'n aros ar agor, felly'r amser cymedrig i ganfod ac unioni yw'r ffigur sy'n gwir gyfyngu eich datguddiad. Y tensiwn yw rhwng cynwal diogelwch ataliol sy'n atal y camgymeriad ar adeg defnyddio a rheolaeth osgo ganfyddol sy'n dal beth sy'n llithro trwodd, ac mae angen ffigurau gonest arnoch ar gyfer y ddau yn hytrach na thybiaeth gysurus fod cynwal diogelwch yn cwmpasu popeth. Dewch â'ch canfyddiadau cam-ffurfweddu a chrwydro o'r chwarter diwethaf gyda stampiau amser, yr amser canolrifol o gyflwyno i unioni, a'r cofnod ymarfer ar gyfer cylchdroi cyfaddawdu allwedd. I ystadau menter a llywodraeth sy'n rhychwantu miloedd o gyfrifon, cytunwch pwy sy'n berchen ar unioni ar gyfer canfyddiad nad oes gan unrhyw dîm berchnogaeth amlwg arno, oherwydd mae rhybudd heb ymatebwr atebol yn rhybudd sy'n heneiddio'n ddigwyddiad.

6. **Sut fyddwch chi'n cadw osgo diogelwch yn gyson ar draws cymylau, cyfrifon, a thimau lluosog heb arafu pawb i grafiad?** Mae ystadau aml-gwmwl ac aml-gyfrif yn dryllio'n gyflym: mae gan bob darparwr ei fodel IAM ei hun, ei ddiofynion ei hun, a'i offer osgo ei hun, felly mae polisi a orfodir mewn un lle'n dod i ben yn dawel mewn lle arall. Y cyfaddawd yw rhwng rheolaeth ganolog sy'n gwarantu cysondeb ac ymreolaeth leol sy'n gadael i dimau symud yn gyflym, ac mae pwyso'n rhy bell i unrhyw gyfeiriad naill ai'n tagu traddodi neu'n gadael safonau i grwydro. Dewch â'ch map sylw cyfredol: pa gyfrifon sy'n etifeddu cynwal diogelwch parth glanio, pa rai sy'n ddi-reolaeth, a lle mae'r un rheolaeth yn cael ei mynegi dair ffordd wahanol ar draws darparwyr. I sefydliad mawr neu gyhoeddus, ychwanegwch yr ongl archwilio, oherwydd mae archwilwyr yn disgwyl un safon y gellir ei hamddiffyn wedi'i chymhwyso ym mhobman, ac mae rheolaeth sy'n bodoli yn eich prif gwmwl ond nid yn eich un eilaidd yn fwlch y bydd ymosodwr neu asesydd penderfynol yn ei ganfod yn gyntaf.

## Trwy lygaid pob sector

**Busnes newydd.** Mae cyflymder a goroesi'n ennill, felly pwyswch yn llwyr ar ddiofynion diogel sy'n cael eu rhyddhau am ddim: amgryptio wrth orffwys ymlaen, storio'n breifat oni bai bod dynol yn ei agor, MFA ar y cyfrif gwraidd, a hunaniaeth llwyth gwaith adeiledig y darparwr yn lle allweddi mynediad wedi'u gludo. Peidiwch â chodi platfform CSPM na llunio micro-segmentu â llaw na allwch ei gynnal; mae un cynwal diogelwch sy'n rhwystro cronfa ddata sydd wedi'i hagor i'r rhyngrwyd yn prynu'r rhan fwyaf o'r diogelwch am brynhawn o waith. Cadwch bopeth mewn seilwaith-fel-cod o'r cychwyn fel bod caledu'n graddio gyda chi yn hytrach na dod yn ailysgrifennu diweddarach.

**Busnes bach.** Heb beiriannydd diogelwch pwrpasol a chyllideb dynn, ffafriwch wasanaethau a reolir y mae eu diofynion eisoes wedi'u caledu a lle mae rheolaeth allweddi'n cael ei thrin i chi, yn hytrach nag adeiladu eich disgyblaeth KMS eich hun. Trinwch ddiogelwch cwmwl fel cwestiwn hylendid ffurfweddiad: gwybyddwch pa fwcedi a chronfeydd data sy'n bodoli, cadwch nhw'n breifat, mynnwch MFA, a throwch ymlaen wiriadau osgo brodorol y darparwr sy'n dod heb gost ychwanegol. Pan fyddwch chi'n prynu offer, ffafriwch rai sy'n fflagio datguddiad cyhoeddus a storio heb ei amgryptio yn syth o'r bocs, oherwydd mae'r ddau gamgymeriad hynny'n achosi'r rhan fwyaf o doriadau y gellir eu hosgoi.

**Menter.** Y broblem wirioneddol yw cysondeb ar draws miloedd o gyfrifon a llawer o dimau, felly gwaith platfform yw'r gwaith: parthau glanio sy'n darparu pob cyfrif wedi'i galedu, cynwal diogelwch wedi'u gorfodi fel polisi-fel-cod, a CSPM yn sganio'n barhaus am grwydro. Safonwch y model IAM, y rheolau dalfa allweddi, a'r llinell sylfaen segmentu fel bod grwpiau'n stopio ailddyfeisio fersiynau gwannach, a mesurwch osgo ar draws yr ystad yn hytrach nag ymddiried yng ngair pob tîm. Cyllidebwch y beirianneg barhaus i gadw polisïau'n gyfredol wrth i ddarparwyr ychwanegu gwasanaethau ac wrth i'r ystad dyfu.

**Llywodraeth.** Mae rheolau caffael, mandadau preswyliaeth data, a threfnau awdurdodi'n siapio pob dewis, felly mae rheolaethau diogelwch yn dyblu fel tystiolaeth archwilio. Ffafriwch reolaeth allweddi wedi'i dilysu gan FIPS gyda dalfa wedi'i gwahanu oddi wrth fynediad data, rhanbarthau ynysig sy'n cadw data o fewn ffiniau cenedlaethol, a delweddau cynhwysydd wedi'u llofnodi, wedi'u sganio gyda rheolaeth derbyn lem. Cyhoeddwch y mesurau diogelu y gallwch, bwydwch reolaeth osgo barhaus yn uniongyrchol i mewn i awdurdodiad parhaus, a mynnwch fod gwerthwyr yn datgelu eu diofynion ffurfweddiad ac yn cefnogi'r rheolaethau segmentu a dalfa allweddi y mae eich ffiniau dosbarthiad yn eu mynnu.

## Enghreifftiau

**Busnes newydd.** Mae busnes newydd bach yn rhedeg popeth mewn un cyfrif cwmwl ac ni all staffio tîm platfform, felly mae'n pwyso ar ddiofynion sy'n cael eu rhyddhau'n ddiogel: amgryptio wrth orffwys ymlaen yn ddiofyn, bwcedi storio'n breifat oni bai bod dynol yn eu hagor yn benodol, a mynnir MFA ar y cyfrif gwraidd. Yn lle allweddi mynediad hirhoedlog wedi'u gludo i mewn i CI, mae'n defnyddio hunaniaeth llwyth gwaith adeiledig y darparwr fel bod y biblinell yn cael tystlythyrau byrhoedlog yn awtomatig. Mae un cynwal diogelwch am ddim sy'n fflagio unrhyw gronfa ddata sydd wedi'i hagor i'r rhyngrwyd yn eu harbed rhag y camgymeriad cwmwl mwyaf cyffredin a drutaf, am gost un prynhawn i'w sefydlu.

**Menter.** Mae cwmni cyfryngau sy'n rhedeg miloedd o gyfrifon ar draws dau ddarparwr cwmwl yn gorfodi patrwm parth glanio: darperir pob cyfrif o dempled gydag amgryptio-wrth-orffwys ymlaen yn ddiofyn, dim mynediad cyhoeddus ar storio, tagiau gorfodol, a llinell sylfaen o bolisïau cynwal diogelwch. Mae CSPM yn sganio'n barhaus am grwydro, ac mae ffederasiwn hunaniaeth llwyth gwaith wedi dileu allweddi hirhoedlog ar gyfer systemau CI. Pan fydd datblygwr yn ceisio agor cronfa ddata i'r rhyngrwyd yn ddamweiniol, mae polisi ataliol yn rhwystro'r newid ac yn ffeilio tocyn yn awtomatig.

**Llywodraeth.** Mae asiantaeth gyfagos i amddiffyn yn gweithredu mewn rhanbarth cwmwl ynysig gyda phreswyliaeth data wedi'i gorfodi gan bolisi fel nad oes data'n gadael ffiniau cenedlaethol. Mae'r allweddi mwyaf sensitif yn byw mewn HSMs wedi'u dilysu gan FIPS (Federal Information Processing Standards), gyda dalfa allweddi wedi'i gwahanu oddi wrth fynediad data i orfodi gwahanu dyletswyddau. Mae clystyrau Kubernetes yn defnyddio polisïau rhwydwaith llym a rheolaethau derbyn; caiff pob delwedd gynhwysydd ei sganio a'i llofnodi cyn y caniateir iddi redeg. Mae rheolaeth osgo barhaus yn bwydo'n uniongyrchol i mewn i dystiolaeth awdurdodiad parhaus yr asiantaeth.

## Achos busnes: cymhellion, ROI, a TCO

Diogelwch seilwaith cwmwl yw'r man lle mae buddsoddiad bach yn atal colledion trychinebus, o safon penawdau. Mae cyfanswm cost perchnogaeth yn cynnwys offer CSPM, gwasanaethau rheoli allweddi, yr amser peirianneg i ddylunio IAM a segmentu braint leiaf, a'r ymdrech barhaus i gadw polisïau'n gyfredol. Mae'r costau hyn yn real ond yn wylaidd. Cost eu hepgor yw un adnodd wedi'i gam-ffurfweddu'n datgelu cronfa ddata gwsmeriaid gyfan, ynghyd â'r dirwyon rheoleiddiol, costau hysbysu, a niwed brand parhaol sy'n dilyn. Mae toriadau cam-ffurfweddu cwmwl ymhlith y digwyddiadau mwyaf cyffredin ac y gellir eu hatal fwyaf yn y diwydiant.

Mae awtomeiddio ac ailddefnyddio'n chwyddo'r ROI. Amgodiwch ddiofynion diogel i mewn i barthau glanio a thempledi seilwaith-fel-cod, ac mae pob cyfrif a llwyth gwaith newydd yn etifeddu diogelwch heb ymdrech fesul tîm, gan droi diogelwch o dreth â llaw ailadroddus yn fuddsoddiad platfform un-tro. I lywodraeth a mentrau a reoleiddir, mae rheolaeth osgo gref hefyd yn gostwng cost archwiliadau ac awdurdodiad parhaus trwy gynhyrchu tystiolaeth yn awtomatig. Pan fyddwch chi'n gwneud yr achos i arweinyddiaeth, pwysleisiwch fod yr haen hunaniaeth a ffurfweddiad bellach yn brif fector toriad, bod cam-ffurfweddu'n atalladwy, a bod cynwal diogelwch yn torri'r risg a ffrithiant adolygu â llaw ill dau.

## Gwrth-batrymau a pheryglon

- **Caniatâd cerdyn gwyllt.** Caniatáu mynediad `*` eang 'i gael pethau i weithio' a byth yn ei dynhau.
- **Allweddi statig hirhoedlog.** Allweddi mynediad wedi'u mewnblannu mewn sgriptiau a CI nad ydynt byth yn dod i ben ac yn y pen draw'n gollwng.
- **Rhwydweithiau gwastad.** Dim segmentu, fel bod un gwesteiwr wedi'i gyfaddawdu'n cyrraedd popeth.
- **Cyhoeddus trwy ddamwain.** Storio a chronfeydd data wedi'u datgelu i'r rhyngrwyd trwy osodiadau diofyn neu ddiofal.
- **Amgryptio heb ddisgyblaeth allweddi.** Galluogi amgryptio ond gadael mynediad allweddi ar agor led y pen neu byth yn cylchdroi.
- **Cyfrinachau wedi'u pobi i mewn i ddelweddau.** Tystlythyrau wedi'u mewnblannu mewn delweddau cynhwysydd sy'n lledaenu i bobman y mae'r ddelwedd yn rhedeg.
- **Rolau di-weinydd â gormod o ganiatâd.** Ffwythiannau wedi'u caniatáu llawer mwy nag sydd eu hangen arnynt am fod cwmpasu wedi'i hepgor.
- **Osgo archwilio-yn-unig.** Canfod cam-ffurfweddiadau ar ôl y ffaith yn lle eu hatal ar adeg defnyddio.
- **Anwybyddu crwydro.** Gadael i'r amgylchedd rhedeg wyro oddi wrth seilwaith-fel-cod hyd nes nad oes neb yn gwybod y cyflwr gwirioneddol.

## Model aeddfedrwydd

**Lefel 1: Cychwyn.** Darpariaeth â llaw wedi'i yrru gan bwy bynnag sydd angen adnodd. Caniatâd cerdyn gwyllt eang ac allweddi statig hirhoedlog. Rhwydweithiau gwastad heb segmentu. Amgryptio wedi'i gymhwyso'n anghyson, os o gwbl. Dim rheolaeth osgo; mae cam-ffurfweddiadau'n dod i'r amlwg dim ond ar ôl i ddigwyddiad orfodi'r cwestiwn.

**Lefel 2: Datblygu.** Mae rhai rolau IAM ac MFA'n ymddangos, ac mae amgryptio wrth orffwys wedi'i droi ymlaen ar gyfer y prif storfeydd, ond mae'r arfer yn amrywio o dîm i dîm. Mae haenau rhwydwaith sylfaenol yn bodoli heb ddiofyn-i-wrthod. Mae adolygiadau ffurfweddiad yn digwydd yn gyfnodol ac â llaw. Mae seilwaith wedi'i ddiffinio'n rhannol fel cod, felly mae caledu'n dibynnu ar ba grŵp a ddarparodd y cyfrif.

**Lefel 3: Safoni.** Mae RBAC ac ABAC braint-leiaf gyda thystlythyrau byrhoedlog wedi'u dogfennu a'u gorfodi ledled y sefydliad. Mae segmentu'n defnyddio diofyn-i-wrthod dwyrain-gorllewin. Mae amgryptio ar dramwy ac wrth orffwys ymlaen yn ddiofyn, gydag allweddi mewn KMS ar amserlen gylchdroi a dalfa wedi'i gwahanu oddi wrth fynediad data. Mae caledu cynwysyddion a Kubernetes yn safonol, ac mae CSPM yn rhedeg yn erbyn polisïau diffiniedig sy'n cael eu cymhwyso'n gyson ar draws pob cyfrif.

**Lefel 4: Rheoli.** Mesurir yr osgo, nid yw'n cael ei dybio. Rydych yn tracio metrigau a enwir yn erbyn llinellau sylfaen a thargedau: cyfran yr hunaniaethau o fewn eu llinell sylfaen braint leiaf, amser cymedrig i ganfod ac unioni cam-ffurfweddiadau a chrwydro, sylw cynwal diogelwch a CSPM ar draws cyfrifon, cydymffurfiad cylchdroi allweddi, a chyfrif y tystlythyrau hirhoedlog sy'n goroesi. Trefnir canfyddiadau yn ôl radiws ffrwydrad, mae gan unioni berchennog ac amcan lefel gwasanaeth, ac mae data tueddiad ar y ffigurau hyn yn gyrru lle mae'r ymdrech galedu nesaf yn mynd.

**Lefel 5: Cydgordio.** Pobir diofynion diogel i mewn i barthau glanio a seilwaith-fel-cod fel bod pob adnodd yn cael ei eni wedi'i galedu, ac mae'r rheolaethau'n addasu wrth i'r ystad a'r darlun bygythiad newid. Mae micro-segmentu'n defnyddio polisi ymwybodol o hunaniaeth; mae allweddi a reolir gan gwsmeriaid a HSMs yn diogelu'r systemau sicrwydd uchaf gyda gwahaniad dalfa. Mae cynwal diogelwch ataliol yn rhwystro cam-ffurfweddu ar adeg defnyddio, caiff crwydro ei ganfod a'i unioni'n awtomatig, ac mae tystiolaeth osgo'n bwydo awdurdodiad parhaus yn awtomatig. Mae diogelwch wedi'i integreiddio â thraddodi a chynllunio risg, ac mae'r sefydliad yn rheolaidd yn ymddeol ac yn ailgwmpasu rheolaethau wrth i ddarparwyr, gwasanaethau, a rheoliadau newid.

## Syniadau i'w trafod

1. Ble mae ABAC yn werth ei gymhlethdod o'i gymharu â glynu wrth RBAC yn eich amgylchedd?
2. Sut ydych chi'n dileu tystlythyrau hirhoedlog heb dorri awtomeiddio etifeddol?
3. Beth yw'r rhaniad cywir rhwng cynwal diogelwch ataliol a rheolaeth osgo ganfyddol?
4. Pa systemau sy'n cyfiawnhau allweddi a reolir gan gwsmeriaid neu HSMs o ystyried eu cost weithredol?
5. Sut ydych chi'n atal caniatâd braint-leiaf rhag cronni'n dawel yn ôl i or-fraint?
6. Sut ddylai cymhlethdod aml-gwmwl newid eich dull o osgo a pholisi cyson?

## Casgliadau allweddol

- Hunaniaeth yw'r perimedr newydd; buddsoddwch mewn IAM braint-leiaf gyda thystlythyrau byrhoedlog.
- Segmentwch rwydweithiau a micro-segmentwch lwythi gwaith i gyfyngu cyfaddawdu.
- Amgryptiwch ar dramwy ac wrth orffwys yn ddiofyn, a rheolwch allweddi gyda KMS/HSM a gwahaniad dalfa.
- Caledwch gynwysyddion, Kubernetes, a di-weinydd; cadwch amseroedd rhedeg a delweddau wedi'u clytio.
- Ffafriwch gynwal diogelwch ataliol dros ganfod ar ôl y ffaith, a rheolwch osgo'n barhaus.
- Pobwch ddiofynion diogel i mewn i barthau glanio a seilwaith-fel-cod fel bod diogelwch yn graddio'n awtomatig.
- Cam-ffurfweddu, nid ecsbloetiadau egsotig, yw prif achos toriadau diogelwch cwmwl, ac mae'n atalladwy.

## Cyfeiriadau a darllen pellach

- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- Center for Internet Security, *CIS Benchmarks* (cloud providers, Kubernetes, Docker)
- Cloud Security Alliance, *Cloud Controls Matrix* and *Security Guidance for Cloud Computing*
- NIST, *SP 800-190: Application Container Security Guide*
- Liz Rice, *Container Security*
- Marco Lancini and others, *Cloud security posture and detection* engineering literature
- Provider Well-Architected security pillars (as vendor-neutral architectural guidance)
