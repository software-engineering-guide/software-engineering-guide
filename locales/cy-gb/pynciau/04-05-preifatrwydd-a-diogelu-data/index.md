# 4.5 Preifatrwydd a diogelu data

## Trosolwg a chymhelliant

Mae diogelwch yn amddiffyn data rhag mynediad heb awdurdod. Mae preifatrwydd yn gofyn cwestiwn gwahanol: a ddylech chi fod yn casglu, defnyddio, a chadw'r data hwnnw o gwbl, ac a yw'r bobl y mae'n eu disgrifio'n cael llais? Mae'r ddau'n gorgyffwrdd, ond nid ydynt yr un peth. Gallwch fod yn hollol ddiogel ac eto'n torri preifatrwydd. Rydych chi'n gwneud hynny drwy gronni data nad oes gennych unrhyw fusnes ei ddal, ei ddefnyddio at ddibenion na chytunodd pobl byth iddynt, neu ei symud ar draws ffiniau mewn ffyrdd y mae'r gyfraith yn eu gwahardd. I dimau mawr, mae preifatrwydd yn gyfyngiad dylunio. Mae'n cyffwrdd â phob gwasanaeth sy'n trin gwybodaeth bersonol, sydd heddiw'n golygu bron pob un ohonynt.

Mae'r peryglon yn uchel ac yn cynyddu. Mae rheoleiddio preifatrwydd wedi lledaenu ledled y byd. Mae'n cario dirwyon sy'n graddio gyda refeniw, ac mae'n rhoi hawliau gorfodadwy i unigolion dros eu data. I fentrau, mae camdrin data personol yn gwahodd gweithredu rheoleiddiol, achosion cyfreithiol dosbarth, a cholli ymddiriedaeth cwsmeriaid sy'n ddrud i'w hailadeiladu. I lywodraeth, mae'r ddyletswydd yn drymach fyth. Ni all dinasyddion ddewis darparwr arall ar gyfer eu data treth, iechyd, neu fudd-daliadau, felly mae'r wladwriaeth yn eu had-dalu â dyletswydd gofal arbennig. Ac mae methiannau preifatrwydd yn erydu'r ymddiriedaeth gyhoeddus y mae llywodraeth yn dibynnu arni.

Mae'r bennod hon yn trin preifatrwydd fel disgyblaeth beirianneg. Rydym yn ymdrin â dylunio ar gyfer preifatrwydd o'r cychwyn, lleihau a chadw data'n gyfrifol, dosbarthu a diogelu categorïau sensitif fel [PII](https://en.wikipedia.org/wiki/Personally_identifiable_information) a [PHI](https://en.wikipedia.org/wiki/Protected_health_information), trin caniatâd a sail gyfreithlon, a rheoli'r gofynion trosglwyddo trawsffiniol a phreswyliad sy'n siapio pensaernïaeth fwyfwy.

*Gweler hefyd:* pennod 4.6 (cydymffurfiaeth a llywodraethu), pennod 7.1 (strategaeth a llywodraethu data), a phennod 4.1 (sylfeini a diwylliant diogelwch).

## Egwyddorion allweddol

- **[Preifatrwydd drwy ddyluniad](https://en.wikipedia.org/wiki/Privacy_by_design) ac yn rhagosodedig.** Adeiladwch breifatrwydd i mewn o'r cychwyn, a gwnewch y gosodiad mwyaf gwarchodol o breifatrwydd yn rhagosodiad.
- **[Lleihau data](https://en.wikipedia.org/wiki/Data_minimization).** Casglwch ddim ond yr hyn sydd ei wir angen arnoch, ei gadw dim ond cyhyd ag y mae ei angen arnoch, a'i rannu dim ond fel sy'n angenrheidiol.
- **Cyfyngiad diben.** Defnyddiwch ddata dim ond at y dibenion penodol a ddatgelwyd pan gasglwyd ef.
- **Sail gyfreithlon.** Cael cyfiawnhad cyfreithiol dilys ar gyfer pob gweithgaredd prosesu.
- **Hawliau unigol.** Anrhydeddwch hawliau pobl i gyrchu, cywiro, dileu, a chludo eu data.
- **Tryloywder.** Dywedwch wrth bobl yn blaen beth rydych chi'n ei gasglu, pam, a chyda phwy rydych chi'n ei rannu.
- **Atebolrwydd.** Byddwch yn gallu dangos cydymffurfiaeth, nid dim ond ei honni.

## Argymhellion

### Dylunio ar gyfer preifatrwydd o'r cychwyn

Mae preifatrwydd wedi'i sgriwio ar system orffenedig yn ddrud ac yn anghyflawn. Cyfriwch ef i mewn o'r cychwyn.

- Cynhaliwch **[Asesiadau Effaith Diogelu Data](https://en.wikipedia.org/wiki/Data_protection_impact_assessment) (DPIAs)** ar gyfer systemau a nodweddion newydd sy'n prosesu data personol ar raddfa fawr neu'n cario risg uwch, gan nodi a lliniaru risgiau preifatrwydd cyn adeiladu.
- Gwnewch ragosodiadau'n warchodol o breifatrwydd: optio i mewn yn hytrach nag optio allan ar gyfer prosesu anhanfodol, meysydd data lleiaf posibl, a'r cadw synhwyrol byrraf.
- Cynhwyswch arbenigedd preifatrwydd yn gynnar mewn dylunio, ochr yn ochr â modelu bygythiad diogelwch, fel bod y ddau'n cael eu hystyried ar gam ffin ymddiriedaeth.
- Cynhaliwch **fap neu restr eiddo data**: pa ddata personol sydd gennych, ble mae'n byw, pam, a lle mae'n llifo. Ni allwch ddiogelu na chyfrif am ddata na allwch ei weld.

### Lleihau, cadw, a dileu'n gyfrifol

Mae pob darn o ddata personol sydd gennych yn rhwymedigaeth cymaint ag y mae'n ased.

- **Lleihau casglu:** heriwch bob maes. Os nad oes ei angen arnoch ar gyfer diben datganedig, peidiwch â'i gasglu.
- **Gosodwch amserlenni cadw** yn ôl math data a diben, a'u gorfodi gyda dileu awtomataidd. Mae data a gedwir "rhag ofn" yn ddata sy'n aros i gael ei dorri i mewn iddo neu ei alw dan wŷs.
- **Cefnogwch yr hawl i ddileu:** adeiladwch y gallu i ddod o hyd i ddata unigolyn a'i ddileu ar draws pob system, gan gynnwys copïau wrth gefn a chopïau ar i lawr, o fewn terfynau amser cyfreithiol. Mae hyn yn llawer haws pan gaiff ei ddylunio i mewn na'i sgriwio ymlaen.
- **[Dienwch](https://en.wikipedia.org/wiki/Data_anonymization) neu gyfunwch** ddata ar gyfer dadansoddeg a phrofi fel nad yw data adnabyddadwy'n cael ei ledaenu i amgylcheddau eilaidd.

### Dosbarthu a diogelu data sensitif

Nid yw pob data personol yn cario'r un risg, ac mae rhai categorïau'n cario pwysau cyfreithiol arbennig.

- Dosbarthwch ddata'n haenau, gan wahaniaethu rhwng **PII** (gwybodaeth adnabod personol), **PHI** (gwybodaeth iechyd warchodedig), data ariannol, a chategorïau arbennig (megis hil, crefydd, iechyd, biometreg, neu rywioldeb) sy'n cario diogelwch cyfreithiol uwch.
- Cymhwyswch ddiogelwch cymesur â sensitifrwydd: rheolaethau mynediad cryfach, amgryptio, a monitro ar gyfer yr haenau mwyaf sensitif.
- Defnyddiwch **[docynneiddio](https://en.wikipedia.org/wiki/Tokenization_(data_security))** i ddisodli gwerthoedd sensitif (megis rhifau cerdyn neu ddynodwyr cenedlaethol) â thocynnau anysensitif, gan grebachu'r systemau sy'n cyffwrdd â'r data crai o gwbl ac felly'n crebachu cwmpas cydymffurfiaeth.
- Defnyddiwch **[ffugenwi](https://en.wikipedia.org/wiki/Pseudonymization)** i wahanu dynodwyr oddi wrth weddill cofnod fel bod data'n llai priodoladwy'n uniongyrchol, gan leihau risg tra'n cadw defnyddioldeb.
- Masgiwch ddata sensitif mewn cofnodion, negeseuon gwall, dadansoddeg, ac amgylcheddau anghynhyrchu.

### Trin caniatâd a sail gyfreithlon yn gywir

Mae prosesu data personol yn gofyn am sylfaen gyfreithiol ddilys, a dim ond un o sawl un yw caniatâd.

- Nodwch a dogfennwch y **sail gyfreithlon** ar gyfer pob gweithgaredd prosesu: caniatâd, contract, rhwymedigaeth gyfreithiol, buddiannau hanfodol, tasg gyhoeddus, neu fuddiannau dilys, yn dibynnu ar y drefn berthnasol.
- Lle mai caniatâd yw'r sail, gwnewch ef yn **rhydd ei roi, penodol, gwybodus, ac unamwys**, gyda ffordd hafal o hawdd i'w dynnu'n ôl. Nid yw blychau wedi'u ticio ymlaen llaw a chaniatâd wedi'i fwndelu'n ddilys.
- Cofnodwch ganiatâd: beth y cytunodd y person iddo, pryd, ac ar ba delerau, fel y gallwch ei ddangos.
- Parchwch **gyfyngiad diben**: peidiwch ag ailddefnyddio data at rywbeth anghydnaws â pham y'i casglwyd heb sail newydd.
- Anrhydeddwch signalau fel [Do Not Track](https://en.wikipedia.org/wiki/Do_Not_Track) / [Global Privacy Control](https://en.wikipedia.org/wiki/Global_Privacy_Control) a cheisiadau optio allan lle mae cyfreithiau'n gofyn.

### Rheoli trosglwyddo trawsffiniol a phreswyliad data

Mae ble mae data'n byw ac yn symud yn gorfforol bellach yn bryder pensaernïol o'r radd flaenaf.

- Deallwch ofynion **preswyliad data**: mae rhai awdurdodaethau'n mynnu bod data penodol yn aros o fewn ffiniau cenedlaethol, a rhaid i rywfaint o ddata llywodraethol aros mewn amgylcheddau sofran neu achrededig penodol.
- Ar gyfer **trosglwyddiadau trawsffiniol**, sicrhewch fod mecanwaith cyfreithiol dilys (penderfyniadau digonolrwydd, cymalau contractiol safonol, neu gyfwerth) ar waith ac wedi'i ddogfennu.
- Cynlluniwch ar gyfer preswyliad o'r cychwyn: storio wedi'i binio i ranbarth, lleoleiddio data, a rheolaeth ofalus dros lle mae copïau wrth gefn, cofnodion, a data dadansoddeg yn llifo, gan fod y rhain yn aml yn gollwng data ar draws ffiniau'n ddiarwybod.
- Traciwch is-broseswyr a thrydydd partïon; gall gwerthwr sy'n symud data dramor dorri rhwymedigaethau preswyliad ar eich rhan.

## Cyfaddawdau: manteision ac anfanteision

| Penderfyniad | Manteision | Anfanteision |
|---|---|---|
| Lleihau data ymosodol | Llai o risg, effaith toriad llai, cydymffurfiaeth symlach | Gall gyfyngu dadansoddeg ac opsiynau cynnyrch yn y dyfodol |
| Cadw hirdymor | Hanes cyfoethog ar gyfer dadansoddeg, ML, anghydfodau | Rhwymedigaeth fwy, amlygiad i doriadau, cymhlethdod dileu |
| Tocynneiddio | Crebachu cwmpas cydymffurfiaeth, diogelu data crai | Cymhlethdod system ychwanegol, cronfa docynnau i'w diogelu |
| Rhagosodiadau optio i mewn | Ymddiriedaeth gryfach, cydymffurfiaeth glir | Cyfeintiau data is, metrigau twf anos |
| Preswyliad data rhanbarthol | Yn cwrdd â mandadau cyfreithiol, yn adeiladu ymddiriedaeth sofraniaeth | Cymhlethdod pensaernïol, cost uwch, seilwaith dyblyg |
| Llyn data canoledig | Pŵer dadansoddeg, ffynhonnell unigol | Risg wedi'i chrynhoi, cyfyngiad diben anos |

Y prif densiwn yw rhwng archwaeth busnes am ddata a'r rhwymedigaeth y mae'r data honno'n ei chynrychioli. Mae timau cynnyrch a dadansoddeg yn naturiol eisiau casglu mwy a'i gadw'n hirach. Mae disgyblaeth preifatrwydd yn tynnu'r ffordd arall. Mae'r datrysiad aeddfed yn ail-fframio data fel rhwymedigaeth y mae'n rhaid ei chyfiawnhau, nid ased i'w gronni. Mae'n rhaid i bob penderfyniad casglu a chadw ennill ei le yn erbyn y risg y mae'n ei chreu. Mae preswyliad data'n ychwanegu dimensiwn cost-yn-erbyn-cydymffurfiaeth. Gall diwallu gofynion sofraniaeth luosi seilwaith, ac eto mae'n syml yn anhrafodadwy mewn rhai marchnadoedd a chyd-destunau llywodraethol.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Beth yw eich amserlen gadw ar gyfer pob dosbarth o ddata personol, a beth sy'n gorfodi dileu?** Mae data a gedwir "rhag ofn" yn ddata sy'n aros i gael ei dorri i mewn iddo neu ei alw dan wŷs, felly mae angen oes ddiffiniedig wedi'i chlymu wrth ei ddiben ar bob maes a phob cofnod. Penderfynwch yr amserlen yn ôl math data, yna ei gorfodi gyda dileu awtomataidd yn hytrach na thrystio unrhyw un i gofio. I fentrau mae hyn yn crebachu amlygiad i doriadau a chost storio ar unwaith, ac i lywodraeth mae'n cyd-fynd â rhwymedigaethau statudol i beidio â dal data dinasyddion yn hwy nag y mae'r gyfraith yn ei ganiatáu. Dewch â sampl o'ch cofnodion hynaf a gofynnwch pwy sydd dal eu hangen a than ba sail, oherwydd yn aml does neb yn eu heisiau mewn gwirionedd. Os yw dileu'n â llaw neu ddim yn bodoli, mae data'n cronni am byth ac mae eich rhwymedigaeth yn tyfu'n dawel ar y fantolen.

2. **Pa feysydd sensitif y gallwch eu tocynneiddio neu eu ffugenwi i grebachu risg a chwmpas cydymffurfiaeth fel ei gilydd?** Mae disodli rhifau cerdyn neu ddynodwyr cenedlaethol â thocynnau'n cyfyngu'r gwerthoedd crai i gronfa fach, wedi'i rheoli'n dynn, sy'n torri'n sylweddol ar y systemau sydd o fewn cwmpas ar gyfer archwiliadau fel PCI-DSS. Mae ffugenwi'n gwahanu dynodwyr oddi wrth weddill cofnod, gan leihau risg tra'n cadw'r data'n ddefnyddiol ar gyfer dadansoddeg a phrofi. Penderfynwch pa werthoedd sensitifrwydd uchel sy'n cyfiawnhau cronfa docynnau (cymhlethdod ychwanegol, cronfa i'w diogelu) a pha rai sydd ond angen eu masgio mewn cofnodion ac amgylcheddau anghynhyrchu. Dewch â map o ble mae gwerthoedd sensitif crai'n llifo heddiw, oherwydd mae pob system sy'n cyffwrdd â nhw'n system y mae'n rhaid i chi ei diogelu a'i harchwilio. Ar gyfer data rheoleiddiedig a llywodraethol, mae'r lleihad cwmpas hwn yn un o'r ychydig symudiadau sy'n lleihau cost a risg gyda'i gilydd, felly targedwch eich meysydd mwyaf sensitif yn gyntaf.

3. **Cyn i'ch nodwedd nesaf gael ei rhyddhau, beth sy'n sbarduno Asesiad Effaith Diogelu Data a phwy sy'n ei redeg?** Mae preifatrwydd wedi'i sgriwio ar system orffenedig yn ddrud ac yn anghyflawn, felly mae'n rhaid i DPIA redeg yn gynnar, ochr yn ochr â modelu bygythiad diogelwch, pan allwch chi o hyd newid y dyluniad yn rhad. Penderfynwch y sbardun (prosesu newydd ar raddfa fawr, data categori arbennig, diben newydd) ac enwch bwy sy'n berchen ar yr asesiad fel nad yw'n cwympo drwy'r craciau o dan bwysau cyflenwi. Gall DPIA gwirioneddol ddal gor-gasglu cyn lansio, er enghraifft newid lleoliad manwl-gywir i ddata rhanbarth bras heb golled cynnyrch. Dewch â nodwedd sydd i ddod a cherddwch drwyddi: pa ddata personol y mae'n ei gasglu, pam, ac a yw dyluniad llai ymwthiol yn cyflawni'r un nod. Ar gyfer gwasanaethau llywodraethol na all dinasyddion optio allan ohonynt, mae'r gwiriad cynnar hwn yn rhan o'r ddyletswydd gofal, felly gwnewch ef yn giât, nid yn ôl-feddwl.

4. **Pan fydd data personol yn croesi ffin, gan gynnwys drwy gopïau wrth gefn, cofnodion, ac is-broseswyr, pa fecanwaith cyfreithiol sy'n gorchuddio pob croesiad, ac a allwch ei brofi?** Mae rheolau preswyliad a throsglwyddo bellach yn siapio pensaernïaeth gymaint ag unrhyw ofyniad perfformiad, ac nid y croesiadau amlwg yw'r rhai sy'n dal timau allan yn aml: cofnod a anfonwyd i declyn arsylwi tramor, copi wrth gefn wedi'i ddyblygu i ranbarth rhatach, neu is-broseswr sy'n symud data dramor yn dawel. I sefydliad mawr mae'r pwysau cystadleuol yn wirioneddol, oherwydd mae seilwaith wedi'i binio i ranbarth yn costio mwy ac yn dyblygu gweithrediadau, ac eto gall un trosglwyddiad anghyfreithlon ddirymu mynediad marchnad neu sbarduno gorchymyn gorfodi. Dewch â map llif data cyfredol sy'n enwi pob man y mae data personol yn gorwedd neu'n teithio'n gorfforol, y mecanwaith cyfreithiol ar gyfer pob ffin y mae'n ei chroesi (penderfyniad digonolrwydd, cymalau contractiol safonol, neu gyfwerth), a'r rhestr o is-broseswyr gyda'u lleoliadau. Ar gyfer cyd-destunau llywodraethol a data sofran, triniwch breswyliad fel cyfyngiad pensaernïol caled yn hytrach na chymal contract, gan na ddylai rhai cofnodion byth adael amgylcheddau cenedlaethol achrededig, ac ni all y corff atebol ddirprwyo'r ddyletswydd honno i werthwr.

5. **Pa sail gyfreithlon sy'n cefnogi pob gweithgaredd prosesu, ac a allech chi amddiffyn y dewis hwnnw i reoleiddiwr yfory?** Dim ond un o sawl sylfaen gyfreithiol yw caniatâd, ac mae timau'n aml yn dewis hynny fel rhagosodiad pan fyddai contract, rhwymedigaeth gyfreithiol, tasg gyhoeddus, neu fuddiannau dilys yn fwy gonest a mwy parhaol. Mae hyn yn bwysig ar raddfa fawr oherwydd gall sail wan neu wedi'i dewis yn anghywir ddirymu piblinell gyfan, ac mae datod prosesu nad oedd gennych hawl i'w wneud yn llawer drutach na dewis y sail gywir ymlaen llaw. Pwyswch yr ystyriaethau cystadleuol yn agored: mae caniatâd yn rhoi rheolaeth i unigolion ond gellir ei dynnu'n ôl a rhaid iddo fod yn rhydd ei roi, yn benodol, ac heb ei fwndelu, tra bo sail fel buddiannau dilys yn osgoi blinder caniatâd ond yn mynnu prawf cydbwyso dogfenedig. Dewch â chofrestr sy'n mapio pob gweithgaredd prosesu i'w sail honedig, y dystiolaeth sy'n ei chefnogi, a sut y byddech yn tynnu'n ôl neu'n newid pe herrid chi. Mewn llywodraeth, mae'r rhan fwyaf o brosesu craidd yn gorffwys ar dasg gyhoeddus yn hytrach na chaniatâd, felly byddwch yn fanwl gywir ynghylch lle mae caniatâd dewisol, y gellir ei dynnu'n ôl, yn dechrau, oherwydd mae aneglurdeb rhwng y ddau'n erydu'r ymddiriedaeth nad oes gan ddinasyddion ddewis ond ei hymestyn.

6. **Pe bai person yn arfer ei hawl i gyrchu, dileu, neu gludo heddiw, a allech chi ei fodloni ar draws pob system o fewn y terfyn amser cyfreithiol?** Mae hawliau unigol yn hawdd eu haddo mewn polisi preifatrwydd ac yn anodd eu hanrhydeddu mewn pensaernïaeth a wasgarodd gopïau o ddata personol i gopïau wrth gefn, cachau, storfeydd dadansoddeg, a gwasanaethau ar i lawr. I dîm mawr, dyma'r foment y mae cydymffurfiaeth haniaethol yn dod yn brawf peirianneg concrid, ac mae terfyn amser statudol a gollwyd yn fethiant y mae'n rhaid ei adrodd ac yn signal na allwch chi mewn gwirionedd weld eich data eich hun. Yr ystyriaeth gystadleuol yw cost a chymhlethdod, gan fod adeiladu dileu ac allforio gwirioneddol ar draws systemau'n waith go iawn, ond y dewis arall yw cyflawni â llaw, araf, agored i wallau nad yw'n graddio ac sy'n torri'r gyfraith yn dawel. Dewch â cherdded drwodd gonest o un cais gwirioneddol o'r derbyniad i'r cwblhad, gan gynnwys sut y cyrhaeddir copïau wrth gefn a thrydydd partïon, a'i amseru yn erbyn y terfyn amser cyfreithiol. Ar gyfer gwasanaethau llywodraethol na all pobl eu gadael, triniwch gyflawni hawliau hunanwasanaeth, cyflawn, ac archwiliadwy fel rhan o'r ddyletswydd gofal, nid nodwedd i'w hamserlennu ar gyfer yn ddiweddarach.

## Lens sector

**Cwmni newydd.** Gyda thîm bach a bach o redfa, triniwch breifatrwydd fel yswiriant rhad yn hytrach na rhaglen na allwch ei staffio. Casglwch ddim ond y meysydd sydd eu hangen ar eich nodwedd graidd, cadwch fap data taenlen ysgafn fel y gallwch ateb cais dileu mewn gwirionedd, a chadwch e-byst a thocynnau allan o'ch cofnodion. Mae llif caniatâd clir a dileu gwirioneddol yn costio prynhawn nawr; mae eu hôl-osod ar ôl i'ch cwsmer menter cyntaf neu reoleiddiwr ofyn yn costio llawer mwy, ac mae data a gasglwyd yn ormodol yn rhwymedigaeth nad ydych yn ennill dim drwy ei ddal.

**Busnes bach.** Heb arbenigwr preifatrwydd penodedig a chyllideb dynn, dibynnwch ar y rheolaethau preifatrwydd sydd eisoes wedi'u hadeiladu i mewn i'r offer rydych chi'n eu prynu, a ffafriwch werthwyr sy'n gwneud trin data'n dryloyw a phreswyliad yn glir. Fframiwch y penderfyniad fel prynu yn erbyn adeiladu: bron byth ydych chi'n adeiladu tocynneiddio neu gyflawni hawliau eich hun, felly dewiswch blatfformau sy'n cynnig rheolau cadw, allforio, a dileu yn barod. Gwybyddwch pa ddata personol sydd gennych a lle byddai cofnod anghywir neu goll yn costio cwsmer i chi, ac ysgrifennwch sail gyfreithlon ar gyfer pob defnydd hyd yn oed os yw'r ddogfen yn fyr.

**Menter.** Ar raddfa fawr y broblem yw cysondeb ar draws llawer o dimau: map data a rennir, haenau dosbarthu safonedig, a chadw gorfodedig fel nad oes un grŵp yn dod yn ddolen wan. Cyllidwch y beirianneg ar gyfer dileu traws-system, cronfeydd tocynneiddio, a phensaernïaeth ymwybodol o breswyliad yn benodol, a llywodraethwch is-broseswyr yn ganolog fel na all un gwerthwr dorri rhwymedigaeth drosglwyddo ar eich rhan. Gwnewch DPIAs yn giât yn y broses gyflenwi a mesurwch osgo preifatrwydd, oherwydd bydd archwilwyr a rheoleiddwyr yn gofyn i chi ddangos cydymffurfiaeth, nid dim ond ei honni.

**Llywodraeth.** Mae rheolau caffael, dyletswyddau tryloywder, ac atebolrwydd cyhoeddus yn siapio pob dewis, ac ni all dinasyddion fynd â'u data treth, iechyd, neu fudd-daliadau i unman arall, felly mae'r ddyletswydd gofal wedi'i chynyddu. Piniwch gofnodion sensitif i amgylcheddau cenedlaethol achrededig gan gynnwys copïau wrth gefn a dadansoddeg, rhwymwch bob gwerthwr yn gontractiol i'r un rhwymedigaethau preswyliad a dileu, a dogfennwch sail gyfreithlon (tasg gyhoeddus yn aml) ar gyfer prosesu craidd tra'n cadw defnyddiau dewisol yn gaeth i ganiatâd ar wahân, y gellir ei dynnu'n ôl. Cyhoeddwch ddisgrifiadau iaith blaen o'r hyn rydych chi'n ei gasglu a pham, a gwnewch gyflawni hawliau'n ddibynadwy o fewn amserlenni statudol, oherwydd mae methiant preifatrwydd yma'n erydu'r ymddiriedaeth gyhoeddus y mae'r gwasanaeth yn dibynnu arni.

## Enghreifftiau

**Cwmni newydd.** Mae ap defnyddwyr cam cynnar yn casglu dim ond y data y mae ei angen mewn gwirionedd arno, oherwydd mae pob maes ychwanegol yn rhwymedigaeth y byddai'n well ganddo beidio â'i amddiffyn yn ddiweddarach. Mae'n cadw map data taenlen syml o ble mae data personol yn byw fel y gall ateb cais dileu mewn gwirionedd, yn cadw e-byst a thocynnau allan o'i gofnodion, ac yn gosod rheol gadw sylfaenol i buro data o gyfrifon sydd wedi bod yn segur ers amser maith. Mae adeiladu llif caniatâd clir a dileu gwirioneddol nawr yn costio prynhawn; mae eu hôl-osod ar ôl i'r cwsmer menter neu reoleiddiwr cyntaf ofyn yn costio llawer mwy.

**Menter.** Mae ap defnyddwyr byd-eang yn cynnal DPIA cyn lansio nodwedd argymhelliad newydd ac yn darganfod y byddai'n casglu lleoliad manwl-gywir yn ddiangen; mae'r tîm yn newid i ddata rhanbarth bras, gan leihau risg heb golled cynnyrch. Mae rhifau cerdyn wedi'u tocynneiddio fel mai dim ond cronfa fach, wedi'i rheoli'n dynn, sy'n dal gwerthoedd crai byth, gan dorri cwmpas [PCI](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard) (diwydiant cardiau talu) y cwmni'n ddramatig. Mae rheolau cadw awtomataidd yn puro data cyfrifon anweithredol yn ôl amserlen, ac mae llif hunanwasanaeth yn gadael i ddefnyddwyr allforio a dileu eu data o fewn y terfyn amser cyfreithiol ar draws pob system gan gynnwys copïau wrth gefn.

**Llywodraeth.** Mae gwasanaeth iechyd cenedlaethol yn dosbarthu pob cofnod claf fel PHI a data categori arbennig, gan orfodi rheolaethau mynediad llym, amgryptio, a chofnodi archwilio. Mae polisi preswyliad data'n cadw pob cofnod o fewn ffiniau cenedlaethol, gan gynnwys copïau wrth gefn a dadansoddeg, ac mae pob gwerthwr wedi'i rwymo'n gontractiol i'r un peth. Mae gan ddinasyddion sail gyfreithlon ddogfenedig (tasg gyhoeddus) ar gyfer prosesu craidd, tra bo defnyddiau ymchwil dewisol yn gofyn am ganiatâd ar wahân, y gellir ei dynnu'n ôl, sy'n cael ei gofnodi a'i anrhydeddu. Mae map data'n sail i'r gallu i ymateb i geisiadau cyrchu a dileu o fewn amserlenni statudol.

## Achos busnes: cymhellion, ROI, a TCO

Mae buddsoddiad preifatrwydd yn aml yn cael ei fframio fel cost gydymffurfiaeth bur, ond mae hynny'n ei danbrisio. Mae cyfanswm cost perchnogaeth yn cynnwys prosesau DPIA, offer mapio a rhestru eiddo data, seilwaith tocynneiddio a chadw, a'r beirianneg i gefnogi hawliau unigol a phreswyliad. Pwyswch hynny yn erbyn cost peidio â buddsoddi, sy'n ddifrifol ac yn gynyddol debygol. Mae dirwyon preifatrwydd bellach yn cyrraedd canrannau o refeniw byd-eang, mae achosion dosbarth yn dilyn toriadau mawr, ac mae rheoleiddwyr wedi dangos y byddan nhw'n gweithredu. Y tu hwnt i ddirwyon, mae preifatrwydd wedi'i gamdrin yn dinistrio'r ymddiriedaeth cwsmeriaid sy'n sail i refeniw. Ac mae unioni methiant preifatrwydd ar ôl y ffaith (ôl-osod dileu, datod llifau data anghyfreithlon) yn costio llawer mwy na'i adeiladu i mewn.

Mae gan yr ROI ochr uchaf wirioneddol hefyd. Mae preifatrwydd cryf yn wahaniaethwr cystadleuol, ac mewn marchnadoedd rheoleiddiedig a llywodraethol mae'n rhagofyniad ar gyfer ennill busnes o gwbl. Mae lleihau data'n lleihau amlygiad i doriadau a chost storio'n uniongyrchol, ac mae tocynneiddio'n crebachu cwmpas drud archwiliadau fel PCI-DSS. Wrth wneud yr achos i arweinyddiaeth, cyflwynwch breifatrwydd mewn dwy ffordd: fel rheoli rhwymedigaeth wedi'i addasu i risg gydag amlygiad rheoleiddiol gwirioneddol, a fel ased ymddiriedaeth sy'n agor marchnadoedd. Pwysleisiwch fod preifatrwydd-drwy-ddyluniad yn rhad o'i gymharu â phreifatrwydd-drwy-achos-cyfreithiol, a bod data wedi'i gronni heb ddiben yn rhwymedigaeth sy'n eistedd ar y fantolen, yn aros i gael ei wireddu.

## Gwrth-batrymau a pheryglon

- **Casglu popeth, penderfynu wedyn.** Cronni data heb ddiben, gan uchafu rhwymedigaeth heb fudd.
- **Cadw drwy esgeulustod.** Byth yn dileu unrhyw beth am nad oes amserlen yn bodoli, fel bod data'n cronni am byth.
- **Theatr caniatâd.** Blychau wedi'u ticio ymlaen llaw, caniatâd wedi'i fwndelu, neu batrymau tywyll sy'n gyfreithiol annilys ac yn erydu ymddiriedaeth.
- **Dileu sy'n methu copïau wrth gefn.** Dileu o'r storfa gynradd ond gadael copïau mewn copïau wrth gefn, cofnodion, a dadansoddeg.
- **PII mewn cofnodion a data profi.** Lledaenu data sensitif i amgylcheddau â rheolaeth isel lle mae'n hawdd ei ddatgelu.
- **Anwybyddu llifau data.** Anwybyddu bod cofnodion, copïau wrth gefn, dadansoddeg, ac is-broseswyr yn symud data ar draws ffiniau.
- **Preifatrwydd fel pryder cyfreithiol yn unig.** Ei drin fel gwaith papur yn hytrach na chyfyngiad dylunio peirianneg.
- **Dim map data.** Methu ateb ble mae data personol yn byw, sy'n gwneud ceisiadau hawliau ac ymateb i doriadau'n amhosibl.

## Model aeddfedrwydd

**Lefel 1: Cychwyn.** Trinnir preifatrwydd yn adweithiol, os o gwbl. Casglir data personol yn rhydd heb restr eiddo, lleihad, na therfynau cadw. Mae caniatâd yn ôl-feddwl, nid oes proses ar gyfer ceisiadau cyrchu neu ddileu, ac ni ystyrir lle mae data'n byw'n gorfforol.

**Lefel 2: Datblygu.** Mae arferion sylfaenol yn ymddangos ond yn amrywio yn ôl tîm. Mae polisi preifatrwydd yn bodoli a chaiff caniatâd sylfaenol ei gasglu, gyda pheth ymwybyddiaeth o gadw. Trinnir ceisiadau hawliau â llaw ac yn araf, mae dosbarthiad data'n anffurfiol, a gall un tîm fapio ei ddata tra bo un arall yn casglu'n rhydd. Ni orfodir dim yn gyson ar draws y sefydliad.

**Lefel 3: Safoni.** Mae preifatrwydd drwy ddyluniad wedi'i ddogfennu a'i orfodi ar draws y sefydliad. Mae DPIAs yn rhedeg ar gyfer prosiectau risg uwch, mae data'n cael ei fapio a'i ddosbarthu'n haenau, a gorfodir amserlenni cadw gyda dileu awtomataidd. Dogfennir sail gyfreithlon ar gyfer pob gweithgaredd prosesu, mae mecanweithiau caniatâd dilys ar waith, cyflawnir ceisiadau hawliau o fewn terfynau amser, a chaiff preswyliad ei drin ar gyfer data rheoleiddiedig.

**Lefel 4: Rheoli.** Mesurir a rheolir y rhaglen breifatrwydd yn erbyn llinellau sylfaen. Rydych chi'n tracio amser cyflawni ceisiadau hawliau yn erbyn terfynau amser statudol, sylw polisi cadw ac oedran y cofnodion hynaf, cyfrif meysydd data personol o fewn cwmpas a faint sydd wedi'u tocynneiddio neu eu ffugenwi, cyfraddau cwblhau DPIA ar gyfer nodweddion cymwys, a nifer y llifau trawsffiniol heb eu rheoli a ddarganfuwyd mewn archwiliadau. Mae metrigau'n bwydo trothwyon diffiniedig, fel bod toriad o darged (cais hawliau'n agosáu at ei derfyn amser, trosglwyddiad annisgwyl, drifft cadw) yn sbarduno ymateb dogfenedig yn hytrach na mynd heb ei sylwi.

**Lefel 5: Cydgordio.** Mae preifatrwydd yn gyfyngiad peirianneg rhagosodedig sy'n gwella'n barhaus ac wedi'i integreiddio ar draws y sefydliad. Mae lleihau, tocynneiddio, a chadw awtomataidd yn safonol, mae ceisiadau hawliau'n hunanwasanaeth ac yn gyflawn ar draws pob system gan gynnwys copïau wrth gefn, a chaiff llifau data a phreswyliad eu tracio a'u gorfodi'n barhaus. Mae osgo preifatrwydd yn addasu wrth i reoleiddio, marchnadoedd, a phensaernïaeth newid, gan fwydo gwersi'n ôl i mewn i ddylunio fel bod y llinell sylfaen yn parhau i godi yn hytrach na dim ond dal ei thir.

## Syniadau ar gyfer trafodaeth

1. Sut ydych chi'n datrys y tensiwn rhwng timau dadansoddeg sydd eisiau mwy o ddata a phreifatrwydd sydd eisiau llai?
2. Beth yw pensaernïaeth realistig ar gyfer anrhydeddu dileu ar draws storfeydd cynradd, copïau wrth gefn, a chopïau ar i lawr?
3. Pa sail gyfreithlon sy'n ffitio pob un o'ch gweithgareddau prosesu, ac a allwch chi amddiffyn y dewis?
4. Sut ydych chi'n cadw data personol allan o gofnodion ac amgylcheddau anghynhyrchu heb rwystro dadfygio?
5. Pa ofynion preswyliad data sy'n berthnasol i'ch marchnadoedd, a sut mae copïau wrth gefn a dadansoddeg yn eu cymhlethu?
6. Sut y dylid cyfuno modelu bygythiad preifatrwydd a diogelwch yn un weithgaredd dylunio?

## Casgliadau allweddol

- Mae preifatrwydd yn llywodraethu a ddefnyddiwch ddata personol, a sut y gwnewch hynny; mae'n wahanol i, ac yn ategol i, ddiogelwch.
- Dyluniwch breifatrwydd i mewn o'r cychwyn gyda DPIAs a rhagosodiadau gwarchodol o breifatrwydd.
- Lleihewch gasglu, gorfodwch amserlenni cadw, ac adeiladwch alluoedd dileu gwirioneddol.
- Dosbarthwch PII, PHI, a chategorïau arbennig, a'u diogelu'n gymesur â thocynneiddio a masgio.
- Sefydlwch a dogfennwch sail gyfreithlon; gwnewch ganiatâd yn rhydd ei roi, yn benodol, ac yn ddiddymadwy.
- Triniwch breswyliad data a throsglwyddo trawsffiniol fel cyfyngiadau pensaernïol o'r radd flaenaf.
- Mae data'n rhwymedigaeth yn ogystal ag ased; mae ei gronni heb ddiben yn risg sy'n aros i gael ei wireddu.

## Cyfeiriadau a darllen pellach

- Ann Cavoukian, *Privacy by Design: The 7 Foundational Principles*
- Undeb Ewropeaidd, testun ac arweiniad *General Data Protection Regulation (GDPR)*
- National Institute of Standards and Technology, *Privacy Framework* a *SP 800-122* (Guide to Protecting PII)
- ISO/IEC 27701, *Privacy Information Management*
- Daniel Solove, *Understanding Privacy*
- OECD, *Privacy Guidelines* a *Fair Information Practice Principles (FIPPs)*
- Testun statudol California Consumer Privacy Act (CCPA/CPRA) ac arweiniad rheoleiddiwr
