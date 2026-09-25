# 10.11 Sofraniaeth ddigidol

## Trosolwg a chymhelliant

Mae [sofraniaeth ddigidol](https://en.wikipedia.org/wiki/Digital_sovereignty) yn radd y mae sefydliad, cenedl, neu floc yn cadw rheolaeth ystyrlon dros ei ddata, ei feddalwedd, a'i seilwaith ei hun. Golyga hynny reolaeth dros ble mae data'n preswylio'n gorfforol, pa gyfreithiau a llywodraethau all orfodi mynediad ato, ac a all systemau critigol barhau i weithredu heb ddibynnu ar bŵer tramor neu werthwr unigol. Mae ganddi sawl dimensiwn: **[sofraniaeth ddata](https://en.wikipedia.org/wiki/Data_sovereignty)** (pa awdurdodaeth a chyfreithiau sy'n llywodraethu'r data), **sofraniaeth weithredol** (y gallu i redeg a gweinyddu systemau heb ganiatâd neu bresenoldeb trydydd parti), **sofraniaeth feddalwedd** (mynediad at ac rheolaeth dros y ffynhonnell a'i heifolyad), a **sofraniaeth cadwyn gyflenwi** (rhyddid rhag tagfannau mewn caledwedd, gwasanaethau, a dibyniaethau). Mae'r bennod hon yn eistedd yn y rhan reoli oherwydd bod sofraniaeth yn y bôn yn benderfyniad strategaeth, caffael, a risg (penodau 10.1–10.3) â chanlyniadau technegol dwfn.

Mae'r cymhelliant wedi symud o fod yn ddamcaniaethol i fod yn frys. Mae [cyfrifiadura cwmwl](https://en.wikipedia.org/wiki/Cloud_computing) wedi crynhoi llawer o seilwaith y byd mewn llond llaw o ddarparwyr, y rhan fwyaf o dan awdurdodaeth un wlad. Mae cyfreithiau alldiriogaethol fel [CLOUD Act](https://en.wikipedia.org/wiki/CLOUD_Act) yr Unol Daleithiau (a all orfodi darparwr i ddatgelu data ni waeth ble y'i storir) yn gwrthdaro â threfniadau fel [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) yr UE, tyndra a grisialwyd gan reol *[Schrems II](https://en.wikipedia.org/wiki/Schrems_II)* a ddirymodd Darian Preifatrwydd UE-UDA. Ychwanegwch sioc ddaearwleidyddol, sancsiynau, a'r risg y byddai darparwr yn cael ei dorri i ffwrdd, a daw dibyniaeth yn wendid strategol, nid dim ond troednodyn rheoli gwerthwr. Sofraniaeth yw'r ddisgyblaeth o benderfynu, yn fwriadol, faint o'r ddibyniaeth honno y gall eich systemau a'ch data mwyaf critigol ei chario'n ddiogel.

I fenter ac yn enwedig llywodraeth, mae'r risg yn uniongyrchol. Rhaid i gwmnïau amlwladol gysoni trefniadau diogelu data anghyson ac osgoi clymu na allai rheoleiddiwr neu ddigwyddiad daearwleidyddol ei droi'n fudo bodolaethol. Mae llywodraethau'n dal data (cofnodion iechyd, treth, amddiffyn, hunaniaeth dinasyddion) y byddai eu datgelu i awdurdodaeth dramor yn gwestiwn diogelwch cenedlaethol ac ymddiriedaeth gyhoeddus. Dyna pam mae cynigion "cwmwl sofran," mentrau fel [Gaia-X](https://en.wikipedia.org/wiki/Gaia-X) yr UE, ac ardystiadau cenedlaethol fel SecNumCloud Ffrainc wedi ymddangos. Nid hunangynhaliaeth yw'r nod. Rheolaeth gymesur wedi'i pharu â sensitifrwydd yr hyn sydd yn y fantol ydyw.

## Egwyddorion allweddol

- **Sbectrwm yw sofraniaeth, nid switsh.** Parwch radd y rheolaeth â sensitifrwydd y data a'r llwyth gwaith.
- **Nid awdurdodaeth yw lleoliad.** Gall data a storir yn lleol fod yn dal yn gyfreithiol hygyrch i lywodraeth dramor; nid yw preswyliad ei hun yn sofraniaeth.
- **Dyluniwch ar gyfer gadael.** Y gallu i adael darparwr yw'r mesur gwiriaf o sofraniaeth.
- **Mae [safonau agored](https://en.wikipedia.org/wiki/Open_standard) a [chod agored](https://en.wikipedia.org/wiki/Open-source_software) yn lleihau dibyniaeth:** offer ymreolaeth strategol ydynt, nid dim ond arbedwyr cost.
- **Rheolwch yr allweddi.** Mae pwy sy'n dal ac yn rheoli allweddi amgryptio yn aml yn bwysicach na ble mae'r beit yn eistedd.
- **Osgowch gyfnewid un clymu am un arall.** Gall un gwerthwr "sofran" unigol fod cyn gaethed â hypergraddiwr.
- **Byddwch yn gymesur.** Mae gan sofraniaeth gostau go iawn; mae gorgylchdroi ym mhobman yn gwastraffu arian ac yn arafu danfoniad.

## Argymhellion

### Dosbarthu data a llwythi gwaith yn ôl sensitifrwydd sofraniaeth

Nid oes angen yr un diogelwch ar bopeth. Dosbarthwch ddata a systemau yn ôl canlyniad mynediad awdurdodaeth dramor neu golli darparwr. Gall llwythi gwaith cyhoeddus a risg-isel eistedd ar seilwaith hyperraddfa byd-eang ar gyfer graddfa a chost. Mae data hynod sensitif (diogelwch cenedlaethol, iechyd, hunaniaeth dinasyddion, cofnodion rheoledig) yn mynnu rheolaethau sofraniaeth cryfach. Y graddoli hwn, yr un rhesymeg seiliedig-ar-risg â dosbarthu data ym mhennod 4.5, yw'r hyn sy'n cadw sofraniaeth yn fforddiadwy, gan ganolbwyntio rheolaethau drud lle maent yn gyfiawn yn hytrach na lleoleiddio popeth.

### Deall awdurdodaeth, nid dim ond preswyliad

Mae **preswyliad data** (y lleoliad ffisegol neu ddaearyddol lle storir data) yn angenrheidiol ond nid yn ddigonol. Yr hyn sy'n bwysig yn gyfreithiol yw *awdurdodaeth*: pa lywodraethau all orfodi datgeliad, ac o dan ba gyfreithiau. Gall set ddata a ddelir mewn canolfan ddata yn y wlad a weithredir gan ddarparwr â phencadlys tramor fod yn dal yn hygyrch o dan gyfraith gwlad gartref y darparwr hwnnw (problem CLOUD Act). Mapiwch amlygiad cyfreithiol pob system: pencadlys y darparwr, cyfreithiau perthnasol, ac unrhyw benderfyniadau digonolrwydd neu fecanweithiau trosglwyddo (Cymalau Contractiol Safonol, Fframwaith Preifatrwydd Data UE-UDA). Yna triniwch y map cyfreithiol hwnnw fel rhan ddosbarth-cyntaf o'r bensaernïaeth (penodau 4.5, 4.6).

### Dylunio ar gyfer cludadwyedd a gwrthdroadwyedd

Y rheolaeth sofraniaeth fwyaf parhaol yw ymadawiad hygred. Ffafriwch safonau agored a fformatau cludadwy (pennod 3.8). Cynwysyddwch lwythi gwaith fel y gallant symud. Cadwch seilwaith fel cod (pennod 8.2) fel y gellir ailadeiladu amgylchedd yn rhywle arall. Osgowch ddibyniaeth ddofn ar wasanaethau perchnogol un darparwr ar gyfer eich systemau mwyaf critigol. Cynhaliwch a phrofwch yn gyfnodol gynllun gadael, escro o ddata a ffurfweddiad ynghyd â llwybr wedi'i ymarfer at ddarparwr amgen, fel bod "gallem adael pe bai'n rhaid i ni" yn ffaith wedi'i dangos, nid gobaith. Dyma'r gwrthwenwyn i **[glymu i werthwr](https://en.wikipedia.org/wiki/Vendor_lock-in)**, y cyflwr o fethu newid darparwyr heb gost neu darfu gwaharddol.

### Defnyddio seilwaith sofran a rheolaeth allweddi lle bo'n gyfiawn

Ar gyfer y radd fwyaf sensitif, mae rheolaethau technegol cryfach yn bodoli: cynigion **cwmwl sofran** (rhanbarthau cwmwl a weithredir gan neu mewn partneriaeth ag endidau o fewn yr awdurdodaeth, weithiau wedi'u hardystio fel SecNumCloud), **[cyfrifiadura cyfrinachol](https://en.wikipedia.org/wiki/Confidential_computing)** (gweithrediad ymddiriededig seiliedig-ar-galedwedd sy'n cadw data wedi'i amgryptio hyd yn oed tra caiff ei brosesu), ac allweddi amgryptio a reolir gan y cwsmer: **dod â'ch allwedd eich hun (BYOK)** ac, yn gryfach, **dal eich allwedd eich hun (HYOK)**, lle nad oes gan y darparwr byth fynediad at yr allweddi sy'n datgloi'r data. Gall rheoli'r allweddi ddarparu llawer o fudd ymarferol sofraniaeth hyd yn oed ar seilwaith a rennir. Mae data na all darparwr ei ddadgryptio yn ddata na all ei ddatgelu'n ystyrlon.

### Ffafrio cod agored ac ecosystemau agored ar gyfer ymreolaeth strategol

Mae meddalwedd cod agored a safonau agored ymysg y trosolion sofraniaeth cryfaf, oherwydd eu bod yn dileu swits-lladd un-gwerthwr. Gellir rhedeg, archwilio, fforchio, a chynnal y ffynhonnell yn annibynnol ar unrhyw un cyflenwr (penodau 10.3, 3.8). Mae polisïau sector cyhoeddus "arian cyhoeddus, cod cyhoeddus" a mentrau fel Gaia-X yn adlewyrchu hyn. Nid yw cod agored yn sofran yn awtomatig. Mae'n dal angen pobl fedrus i'w redeg a'i gynnal, ac mae angen diogelu ei gadwyn gyflenwi (pennod 4.2). Ond mae'n trosi dibyniaeth ar werthwr yn ddibyniaeth ar gymuned a'ch gallu eich hun, sy'n llawer haws ei rheoli.

### Llywodraethu sofraniaeth fel risg gymesur, nid absoliwt

Sefydlwch fframwaith risg sofraniaeth ochr yn ochr â'ch llywodraethu arall (penodau 10.2, 1.5). Aseswch grynhoad a risg awdurdodaethol platfformau mawr. Penderfynwch lefelau sofraniaeth targed fesul haen ddata, a'u pwyso yn erbyn cost, gallu, a chyflymder danfon. Y nod yw safbwynt amddiffynadwy, wedi'i ddogfennu ("mae'r llwythi gwaith hyn yn derbyn dibyniaeth hyperraddfa; mae'r rhain angen rheolaeth o fewn yr awdurdodaeth; dyma'n hystum gadael"), wedi'i adolygu wrth i ddaearwleidyddiaeth a rheoleiddiad newid, nid safiad absoliwt un-tro.

## Cymhareb: manteision ac anfanteision

| Dull | Manteision | Anfanteision |
|---|---|---|
| **Cwmwl hyperraddfa byd-eang** | Graddfa, nodweddion, cost isel, cyflymder | Amlygiad awdurdodaethol; risg crynhoad a chlymu |
| **Cwmwl sofran / darparwr o fewn yr awdurdodaeth** | Rheolaeth gyfreithiol; ffit diogelwch cenedlaethol; ymddiriedaeth | Cost uwch; llai o nodweddion; graddfa lai'n aml; clymu newydd |
| **Rheolaeth allweddi (BYOK/HYOK) ar seilwaith a rennir** | Llawer o'r budd am gost is; yn cadw graddfa | Cymhlethdod gweithredol; risg rheoli allweddi; nid yn absoliwt |
| **Cod agored / hunan-letya** | Archwiliadwyedd, fforchiadwyedd, dim swits-lladd gwerthwr | Angen gallu mewnol; chi sy'n berchen ar y gweithrediadau a'r diogelwch |
| **Mandadau lleoleiddio data** | Cydymffurfiaeth reoleiddiol; sicrwydd gwleidyddol | Costus; yn dryllio data; gall leihau gwytnwch a defnyddioldeb |

Y tyndra diffiniol yw **rheolaeth yn erbyn gallu a chost**. Mae sofraniaeth uchaf (hunan-letya, o fewn yr awdurdodaeth, cod agored, yn gwbl gludadwy) yn aberthu graddfa, nodweddion, a chyflymder platfformau byd-eang. Mae gallu uchaf yn derbyn dibyniaeth ac amlygiad awdurdodaethol. Y datrysiad yw graddoli: talwch am sofraniaeth lle mae'r canlyniad yn ei gyfiawnhau, a chymerwch ddibyniaeth bragmataidd lle nad yw.

## Cwestiynau i'w trafod gyda'ch tîm

1. **A ydym wedi graddoli ein data a'n llwythi gwaith yn ôl sensitifrwydd sofraniaeth, fel bod rheolaethau drud yn glanio dim ond lle maent yn gyfiawn?** Sbectrwm yw sofraniaeth, nid switsh, ac mae lleoleiddio popeth yn llosgi arian, yn colli gallu, a gall hyd yn oed leihau gwytnwch drwy grebachu'ch dewisiadau. Dosbarthwch bob system yn ôl canlyniad mynediad awdurdodaeth dramor neu golli darparwr: gall llwythi gwaith cyhoeddus a risg-isel eistedd ar seilwaith hyperraddfa byd-eang, tra bo diogelwch cenedlaethol, iechyd, neu ddata hunaniaeth dinasyddion yn mynnu rheolaethau cryfach. Dyma'r un rhesymeg seiliedig-ar-risg â dosbarthu data, a dyma sy'n cadw sofraniaeth yn fforddiadwy. Dewch â'ch systemau tlws-y-goron a'u lletyaeth bresennol, a gofynnwch a yw'r diogelwch yn cyfateb i'r sensitifrwydd. Os ydych yn amddiffyn popeth yn gyfartal, mae bron yn sicr eich bod yn gordalu yn rhywle ac yn agored yn rhywle arall.

2. **A yw safonau agored a chod agored yn rhan o'n strategaeth sofraniaeth, ynteu a ydym yn eu trin fel arbedwyr cost yn unig?** Mae ffynhonnell y gallwch ei rhedeg, ei harchwilio, ei fforchio, a'i chynnal yn dileu'r swits-lladd un-gwerthwr, un o'r trosolion ymreolaeth cryfaf sydd gennych. Safonau agored a fformatau cludadwy yw'r hyn sy'n gwneud ymadawiad hygred yn bosibl, a dyma'r mesur gwiriaf o sofraniaeth. Y trap cynilach yw dianc rhag hypergraddiwr dim ond i ddod yn gaeth yn llwyr i un gwerthwr "sofran" heb ymadawiad: rydych wedi cyfnewid un clymu am un arall. Dewch â'ch platfformau mwyaf critigol a gofynnwch pa mor dynn y mae pob un wedi'i rwymo wrth wasanaethau perchnogol un darparwr. Lle mae'r ateb yn "iawn dynn," safonau agored ac amgylcheddau wedi'u cynwysyddu, y gellir eu hailadeiladu, yw'r ffordd rataf o lacio'r afael.

3. **Pwy sy'n berchen ar ein fframwaith risg sofraniaeth, a pha mor aml y byddwn yn ailymweld â'r safiad wrth i gyfraith a daearwleidyddiaeth newid?** Mae safbwynt sofraniaeth a osodwyd unwaith ac na chaiff ei adolygu byth yn dod yn ffuglen yr eiliad y mae rheol, sancsiwn, neu gyfraith newydd yn glanio, ac mae'r sioeau hynny bellach yn cyrraedd yn rheolaidd. Sefydlwch fframwaith byw ochr yn ochr â'ch llywodraethu arall: aseswch grynhoad a risg awdurdodaethol platfformau mawr, gosodwch lefelau sofraniaeth targed fesul haen ddata, a dogfennwch safbwynt amddiffynadwy y gallwch ei ddangos i reoleiddiwr. Enwch y perchennog a'r cadence adolygu. Dewch â'r cwestiwn o sut y byddai sancsiwn neu reol wrthwynebus yn erbyn eich prif ddarparwr yn taro'ch gwasanaethau critigol yr wythnos nesaf; os na all neb ateb, nid yw'r fframwaith yn bodoli eto.

4. **Pwy sy'n dal yr allweddi amgryptio ar gyfer ein data mwyaf sensitif, a allai ein darparwr gael ei orfodi i drosglwyddo'r data hwnnw ar ffurf ddarllenadwy?** Mae preswyliad a hyd yn oed rhanbarth "sofran" yn cyfrif am fach os yw'r gweithredwr yn cadw'r allweddi, oherwydd mae gorchymyn datgelu wedyn yn cyrraedd data wedi'i ddadgryptio ni waeth ble mae'r beitiau'n eistedd. Mae rheoli'r allweddi eich hun, drwy ddod â'ch allwedd eich hun neu'r un gryfach dal eich allwedd eich hun, lle nad yw'r darparwr byth yn eu gweld, yn aml yn darparu'r rhan fwyaf o fudd ymarferol sofraniaeth ar seilwaith a rennir am ffracsiwn o gost adleoli popeth. Yr ystyriaeth gystadleuol yw gweithredol: nid yw rheoli allweddi'n faddeugar, a gall allwedd goll neu wedi'i chamdrin eich cloi allan o'ch data eich hun mor sicr ag unrhyw sancsiwn. Dewch ag arolwg o ba setiau data sydd wedi'u hamgryptio, pwy sy'n dal pob allwedd mewn gwirionedd, a beth yw'ch llwybr adfer os collir allwedd, yna mapiwch hynny yn erbyn eich graddau sofraniaeth. I fenter a llywodraeth, triniwch ddalfa allweddi fel y llinell sy'n penderfynu a yw gorchymyn datgelu tramor yn dychwelyd testun-seiffr neu destun-plaen, a gwnewch hynny'n ofyniad caffael yn hytrach nag ôl-osodiad diweddarach.

5. **A allem mewn gwirionedd adael ein prif ddarparwr o fewn ffrâm amser sy'n bwysig, a phryd wnaethom ei ymarfer ddiwethaf?** Ymadawiad hygred yw'r mesur gwiriaf o sofraniaeth, ac eto mae'r rhan fwyaf o gynlluniau gadael yn byw ar bapur ac erioed wedi cael eu rhedeg, felly mae cludadwyedd yn aros yn obaith yn hytrach na ffaith wedi'i dangos. Y tyndra yw cost a ffocws: mae ymarfer ymadawiad, cadw llwythi gwaith wedi'u cynwysyddu, a dal escro o ddata a ffurfweddiad i gyd yn bwyta sylw peirianyddol y byddai pwysau danfon yn well ganddo ei wario mewn mannau eraill. Dewch â'ch system fwyaf critigol, amcangyfrif gonest o ba mor hir y byddai mudo gorfodol yn ei gymryd, y rhestr o wasanaethau perchnogol y mae'n dibynnu arnynt, a dyddiad eich ymarfer go iawn diwethaf (os o gwbl). I sefydliad mawr neu gyhoeddus sy'n cario rhwymedigaethau gadael aml-flwyddyn mewn contract, mae ymadawiad heb ei ymarfer yn ymrwymiad na allwch efallai ei fodloni'n gyfreithiol, felly triniwch gadence ymarfer fel rhan o gost rhedeg y system, nid ymarfer dewisol.

6. **Ar gyfer pob system tlws-y-goron, a wyddom pa lywodraethau a allai orfodi mynediad ati'n gyfreithlon heddiw, ni waeth ble mae'r data'n eistedd yn gorfforol?** Nid awdurdodaeth yw lleoliad: gall data mewn canolfan ddata yn y wlad fod yn dal yn hygyrch o dan gyfraith gwlad gartref gweithredwr â phencadlys tramor, ac mae timau'n rheolaidd yn camgymryd preswyliad am ddiogelwch cyfreithiol. Y rhan anodd yw bod yr ateb yn mynnu mewnbwn cyfreithiol a chaffael, nid dim ond diagram pensaernïaeth, ac mae'r map yn newid wrth i benderfyniadau digonolrwydd, rheolau, a mecanweithiau trosglwyddo newid. Dewch, ar gyfer pob set ddata critigol, â phencadlys y darparwr, y cyfreithiau sy'n ei gyrraedd, a'r mecanwaith trosglwyddo rydych yn dibynnu arno, a byddwch yn onest lle nad oes neb yn gwybod mewn gwirionedd. Mewn lleoliadau rheoledig a chyhoeddus, mae amlygiad cyfreithiol heb ei fapio ar ddata dinasyddion neu ddiogelwch cenedlaethol yn ganfyddiad sy'n aros i ddigwydd yn yr archwiliad nesaf, felly cyllidebwch y mapio cyfreithiol mor benodol ag y byddwch yn cyllidebu'r seilwaith.

## Lens sector

**Cwmni newydd.** Mae cyflymder a rhediad yn dominyddu, felly prynwch sofraniaeth fel nodwedd denau yn hytrach nag adeiladu stac sofran na allwch ei staffio. Os yw awdurdodaeth cwsmer yn gyfyngiad, defnyddiwch ddewis rhanbarth eich darparwr presennol, daliwch eich allweddi amgryptio eich hun fel na all y gweithredwr ddadgryptio cofnodion sensitif, a chadwch y llwyth gwaith wedi'i gynwysyddu fel ei fod yn aros yn gludadwy. Mae hynny'n cau'r fargen am gost cam-had a heb achosi ailbensaernïaeth nad oes gennych redeg ar ei chyfer.

**Busnes bach.** Heb arbenigwr sofraniaeth a chyllideb dynn, triniwch hyn fel cwestiwn adolygu contract a dewis gwerthwr, nid rhaglen beirianneg. Ffafriwch werthwyr sy'n cynnig rhanbarthau o fewn yr awdurdodaeth, telerau prosesu data tryloyw, ac allweddi a ddelir gan gwsmer fel nodweddion safonol, a darllenwch y cymalau is-brosesydd a datgelu cyn i chi lofnodi. Anaml y mae hunan-letya ar gyfer sofraniaeth yn talu ffordd yma: byddech yn etifeddu'r baich gweithrediadau a diogelwch heb y bobl i'w gario.

**Menter.** Y dasg yw llywodraethu portffolio ar draws llawer o dimau: graddoli data a rennir yn ôl sensitifrwydd sofraniaeth, golwg risg-crynhoad ar faint o lwyth critigol sy'n eistedd ar un darparwr neu un awdurdodaeth, a rheolaeth allweddi, cludadwyedd, ac ymarferion gadael wedi'u safoni fel bod pob grŵp yn stopio gwneud ei fet ei hun heb ei gydgysylltu. Cyllidebwch gost uwch a baich gweithredol yr haen sensitif yn benodol, a chynhaliwch safiad wedi'i ddogfennu, y gellir ei archwilio y gallwch ei ddangos i reoleiddiwr. Rheolwch sofraniaeth fel risg fyw gyda metrigau a chadence adolygu, nid mudo un-tro.

**Llywodraeth.** Mae rheolau caffael, tryloywder, ac atebolrwydd cyhoeddus yn llunio pob dewis. Ffafriwch seilwaith sofran ardystiedig (er enghraifft cymhwyster tebyg i SecNumCloud) a safonau agored a chod agored fel y gellir cynnal y platfform yn annibynnol ar unrhyw gyflenwr unigol, a mynnwch gludadwyedd a datgeliad amlygiad cyfreithiol yn y contract ei hun. Cyhoeddwch ddisgrifiad iaith-blaen o ble mae data dinasyddion yn eistedd a phwy all ei gyrraedd, cadwch reolaethau sofran drud ar gyfer yr haen wir sensitif, a chadwch wasanaethau cyhoeddus llai sensitif ar seilwaith byd-eang rhatach.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd technoleg-iechyd bach yn glanio ei gwsmer ysbyty cyntaf yn yr Almaen, sy'n mynnu bod data cleifion yn aros o dan awdurdodaeth yr UE. Yn lle gor-adeiladu stac sofran na all fforddio, mae'r sylfaenwyr yn defnyddio i ranbarth UE eu darparwr cwmwl presennol, yn dal eu hallweddi amgryptio eu hunain fel na all y darparwr ddadgryptio'r cofnodion sensitif, ac yn cadw'r llwyth gwaith wedi'i gynwysyddu fel ei fod yn aros yn gludadwy. Mae hyn yn prynu'r rhan fwyaf o fudd sofraniaeth y mae'r cwsmer angen am gost y gall tîm cam-had ei chario, ac mae'n cau'r fargen heb ailbensaernïaeth gyfan.

**Menter.** Rhaid i fanc amlwladol gadw data cwsmeriaid penodol o fewn yr UE a thu hwnt i gyrraedd cyfraith datgelu dramor. Yn hytrach na chefnu ar ei ddarparwr cwmwl byd-eang, mae'n graddoli ei ystâd. Mae llwythi gwaith cyffredinol yn aros ar ranbarthau hyperraddfa ar gyfer graddfa. Mae data cwsmer rheoledig yn rhedeg mewn rhanbarthau UE gydag amgryptio **dal eich allwedd eich hun** (ni all y darparwr ei ddadgryptio) a chynllun gadael wedi'i brofi at ddarparwr amgen. Mae hyn yn bodloni rheoleiddwyr ac archwaeth risg-crynhoad y banc ei hun (pennod 10.2) heb fudo cyfan, difaol-i-alluoedd.

**Llywodraeth.** Mae gwasanaeth iechyd cenedlaethol yn dal cofnodion meddygol dinasyddion ac yn barnu bod amlygiad i awdurdodaeth dramor yn annerbyniol. Mae'n caffael cwmwl sofran, sef seilwaith a weithredir gan endid o fewn y wlad o dan ardystiad cenedlaethol (e.e., tebyg i SecNumCloud), gyda chyfrifiadura cyfrinachol ar gyfer y prosesu mwyaf sensitif, ac yn mynnu safonau agored (pennod 3.8) a chydrannau cod agored fel y gellir cynnal y platfform yn annibynnol ar unrhyw gyflenwr unigol. Derbynnir y gost uwch a'r set nodweddion culach fel pris rheolaeth diogelwch cenedlaethol ac ymddiriedaeth gyhoeddus. Yn y cyfamser, mae gwasanaethau llai sensitif (porth gwybodaeth gyhoeddus) yn aros ar seilwaith byd-eang rhatach.

## Achos busnes: cymhellion, ROI, a TCO

Mae economeg sofraniaeth ddigidol yn anghymesur, a fframir orau fel yswiriant yn erbyn digwyddiadau tebygolrwydd-isel, effaith-uchel. Mae'r costau'n weladwy ac yn ailadroddus: mae seilwaith sofran ac o fewn yr awdurdodaeth fel arfer yn ddrutach, yn cynnig llai o wasanaethau a reolir, ac yn mynnu mwy o allu gweithredol mewnol, sydd i gyd yn codi cost perchnogaeth gyfan ac yn gallu arafu danfoniad. Mae'r buddion yn bennaf yn drychinebau a osgowyd: dirwyon rheoleiddiol ac ailbensaernïaeth orfodol ar ôl rheol fel *Schrems II*, colli mynediad sy'n dinistrio busnes os cosbir neu dorrir darparwr i ffwrdd, neu'r niwed enwog a diogelwch cenedlaethol o ddatgeliad tramor o ddata sensitif. Am fod y risgiau cynffon hynny'n ddifrifol ac yn gynyddol gredadwy, mae buddsoddiad cymesur mewn sofraniaeth, yn enwedig rheolaethau rhad-ond-pwerus fel perchnogaeth allweddi, cludadwyedd, a safonau agored, yn aml yn werth disgwyliedig cryf positif, er ei fod yn edrych fel cost bur ar daenlen cyflwr-sefydlog.

Y trap ar y ddwy ochr yw anghymesuredd. Mae *tan*-fuddsoddi'n gadael data a systemau critigol yn agored i un awdurdodaeth neu werthwr heb ymadawiad, gan droi risg y gellir ei reoli'n un bodolaethol. Mae *gor*-fuddsoddi, drwy leoleiddio popeth a gwrthod pob platfform byd-eang, yn llosgi arian, yn colli gallu, ac yn gallu *lleihau* gwytnwch drwy grebachu'ch dewisiadau. I wneud yr achos i arweinyddiaeth, cysylltwch wariant sofraniaeth â graddoli risg data-a-llwyth-gwaith. Meintiolwch grynhoad ac amlygiad awdurdodaethol y systemau tlws-y-goron. Prisiwch y rheolaethau rhad (allweddi, cludadwyedd, ymarferion gadael) sy'n dad-risgio nhw. Cadwch seilwaith sofran drud ar gyfer yr haen sy'n wir ei fynnu.

## Gwrth-batrymau a pheryglon

- **Theatr sofraniaeth:** hysbysebu preswyliad data yn y wlad tra bo darparwr â phencadlys tramor yn cadw mynediad cyfreithiol at y data.
- **Cymysgu amgryptio â sofraniaeth:** amgryptio data ond gadael i'r darparwr ddal yr allweddi, fel y gellir ei orfodi o hyd i ddadgryptio.
- **Gorgylchdroi:** lleoleiddio a hunan-letya popeth am gost ddinistriol a gallu gostyngol, ni waeth beth yw'r sensitifrwydd.
- **Clymu sengl newydd:** dianc rhag hypergraddiwr drwy ddod yn gaeth yn llwyr i un gwerthwr "sofran" heb ymadawiad.
- **Dim ymadawiad wedi'i brofi:** cynllun gadael sy'n bodoli ar bapur ond erioed wedi'i ymarfer, felly mae cludadwyedd heb ei brofi.
- **Anwybyddu'r gadwyn gyflenwi ddynol:** tybio bod cod agored neu hunan-letya'n rhoi sofraniaeth heb y bobl fedrus i'w redeg.
- **Safiad statig:** gosod safbwynt sofraniaeth unwaith ac erioed ei ailymweld wrth i gyfraith a daearwleidyddiaeth newid.

## Model aeddfedrwydd

- **Lefel 1 (Cychwyn):** Mae sofraniaeth heb ei hystyried ac yn adweithiol; mae data a systemau critigol yn eistedd lle bynnag sydd rataf, heb fap o risg awdurdodaethol neu grynhoad a heb berchennog.
- **Lefel 2 (Datblygu):** Ymdrinnir â phreswyliad data ar gyfer y data rheoledig mwyaf amlwg ar rai prosiectau, ond nid ystyrir awdurdodaeth, rheolaeth allweddi, ac ymadawiad yn systematig; mae arferion yn amrywio o dîm i dîm, ac ni archwilir dibyniaeth ar ddarparwyr unigol.
- **Lefel 3 (Safoni):** Graddolir data a llwythi gwaith yn ôl sensitifrwydd sofraniaeth o dan bolisi wedi'i ddogfennu a gymhwysir ar draws y sefydliad; mapir awdurdodaeth; mynnir rheolaeth allweddi, cludadwyedd, a safonau agored ar haenau sensitif; mae cynlluniau gadael yn bodoli ac yn orfodol yn hytrach na dewisol.
- **Lefel 4 (Rheoli):** Mesurir a rheolir y safiad yn erbyn llinellau sylfaen: olrheinir risg crynhoad (cyfran llwythi gwaith critigol ar un darparwr neu awdurdodaeth), gorchudd perchnogaeth allweddi ar draws setiau data sensitif, cyflawnrwydd mapio awdurdodaeth, ac amseroedd ymadawiad wedi'u hymarfer fel metrigau, eu hadrodd i lywodraethu, a'u gorfodi yn erbyn trothwyon, fel bod dibyniaeth sy'n crwydro'n sbarduno gweithredu ar dystiolaeth yn hytrach nag ar ôl sioc.
- **Lefel 5 (Cerddorfa):** Gwellir sofraniaeth yn barhaus a'i integreiddio ar draws y sefydliad: mae'r fframwaith risg byw'n bwydo pensaernïaeth, caffael, a chynllunio risg yn ddiofyn, mae ymadawiadau'n cael eu hymarfer yn rheolaidd, ac mae'r sefydliad yn ailgwmpasu haenau, yn ail-gydbwyso darparwyr, ac yn diwygio ei safiad yn addasol wrth i reolau, sancsiynau, a rheoleiddiad newid.

## Syniadau ar gyfer trafodaeth

1. Ar gyfer eich set ddata fwyaf sensitif, pa lywodraethau a allai orfodi mynediad ati'n gyfreithlon heddiw, ac a wyddoch chi?
2. A yw preswyliad eich data'n sofraniaeth go iawn, neu a yw darparwr â phencadlys tramor yn dal yr allweddi a'r amlygiad cyfreithiol o hyd?
3. A allech mewn gwirionedd adael eich prif ddarparwr cwmwl pe bai'n rhaid i chi, ac a ydych chi erioed wedi'i brofi?
4. Pa rai o'ch llwythi gwaith sydd wir angen seilwaith sofran, a pha rai rydych chi'n eu gor-amddiffyn am gost ddiangen?
5. Ble byddai rheoli eich allweddi amgryptio eich hun yn rhoi'r rhan fwyaf o fudd sofraniaeth i chi am ffracsiwn o'r gost?
6. Sut fyddai sancsiwn, toriad, neu reol gyfreithiol yn erbyn eich prif ddarparwr yn effeithio ar eich gwasanaethau critigol yr wythnos nesaf?

## Casgliadau allweddol

- Mae sofraniaeth ddigidol yn rheolaeth gymesur dros eich data, eich meddalwedd, a'ch seilwaith, ar draws dimensiynau data, gweithredol, meddalwedd, a chadwyn gyflenwi.
- **Nid awdurdodaeth yw lleoliad:** nid yw preswyliad ei hun yn atal mynediad cyfreithiol tramor; mapiwch pwy all orfodi datgeliad.
- **Dyluniwch ar gyfer gadael** a **rheolwch eich allweddi:** cludadwyedd a pherchnogaeth allweddi yw'r rheolaethau â'r trosoledd uchaf a'r gost isaf.
- Mae **safonau agored a chod agored** yn offer ymreolaeth strategol; cadwch **gwmwl sofran** drud ar gyfer yr haen sy'n ei fynnu.
- Llywodraethwch sofraniaeth fel **risg gymesur, fyw** (penodau 10.2, 10.3, 4.5, 4.6, 3.8), gan osgoi tan-ddiogelu a gorgylchdroi dinistriol fel ei gilydd.
- Yr ROI yw yswiriant yn erbyn risgiau cynffon difrifol (rheoleiddiol, daearwleidyddol, a chlymu) wedi'i brisio yn erbyn cost go iawn, ailadroddus.

## Cyfeiriadau a darllen pellach

- Llys Cyfiawnder Ewropeaidd, *Data Protection Commissioner v. Facebook Ireland and Maximillian Schrems* ("Schrems II", 2020).
- Rheoliad (UE) 2016/679, *General Data Protection Regulation (GDPR)*; Rheoliad (UE) 2023/2854, *Data Act*.
- *Clarifying Lawful Overseas Use of Data (CLOUD) Act* yr Unol Daleithiau (2018).
- ANSSI, fframwaith cymhwyster *SecNumCloud* (Ffrainc).
- Gaia-X European Association for Data and Cloud (menter Gaia-X).
- ENISA, adroddiadau ar ddiogelwch cwmwl ac ardystiad seiberddiogelwch UE (EUCS).
- Julia Pohle a Thorsten Thiel, "Digital Sovereignty" (*Internet Policy Review*, 2020).
- Bert Hubert, ysgrifau ar ymreolaeth ddigidol Ewropeaidd a dibyniaeth ar ddarparwyr tramor.
- Kai Zenner ac eraill, dadansoddiadau o bolisi sofraniaeth ddigidol yr UE (ar gyfer cyd-destun; gwiriwch ffynonellau cyfredol).
