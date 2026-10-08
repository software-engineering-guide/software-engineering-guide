# 11.2 Y biblinell ddanfon

## Trosolwg a chymhelliant

Y biblinell ddanfon yw llif y gwaith sy'n troi syniad wedi'i ddilysu'n feddalwedd sy'n rhedeg yn nwylo defnyddwyr (yn ddibynadwy, yn ailadroddadwy, ac yn fesuradwy) ac yna'n bwydo'r data canlyniad sy'n deillio yn ôl i mewn i ddarganfod (pennod 11.1). Dyma'r llwybr diwydiannol o ymrwymiad cod i newid cynhyrchu i effaith fesuredig ar ddefnyddwyr a busnes. Lle mae darganfod yn ateb *beth a pham*, mae danfon yn ateb *sut rydym yn ei ddanfon yn ddiogel, pa mor gyflym, ac a weithiodd mewn gwirionedd*.

Mae'r bennod hon yn fwriadol integreiddiol. Mae'r mecaneg yn byw mewn manylder mewn mannau eraill: strategaeth profi (pennod 2.4), profi ac awtomeiddio proses (pennod 8.5), [integreiddio parhaus](https://en.wikipedia.org/wiki/Continuous_integration) a [chyflenwi parhaus](https://en.wikipedia.org/wiki/Continuous_delivery) (CI/CD) a strategaethau defnyddio (pennod 8.1), seilwaith fel cod (pennod 8.2), dibynadwyedd a SLOs (amcanion lefel gwasanaeth, pennod 9.1), ac arbrofi (pennod 7.4). Yma rydym yn eu cydosod yn un biblinell o'r dechrau i'r diwedd ac, yn hollbwysig, yn atodi'r **metrigau canlyniad** sy'n dweud wrthych a yw'r peiriant cyfan yn cynhyrchu gwerth yn hytrach na chynhyrchu rhyddhadau'n unig.

I dimau mawr, y biblinell ddanfon yw'r buddsoddiad ag effaith uchaf sengl mewn effeithiolrwydd peirianneg. Mae degawd o ymchwil, yn amlycaf y rhaglen DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) a grynhoir yn *Accelerate*, yn dangos bod timau â phiblinellau danfon cyflym, awtomataidd, risg isel yn perfformio'n well ar gynnyrch *a* sefydlogrwydd *a* chanlyniadau sefydliadol. Mae'r gred hanesyddol bod cyflymder a diogelwch yn gyfnewid ei gilydd yn empirig anghywir. Mewn mentrau, piblinell gref yw'r hyn sy'n gadael i gannoedd o beirianwyr integreiddio heb gwympo i mewn i anhrefn uno a theatr ryddhau â llaw. Mewn llywodraeth, mae'n disodli rhyddhadau "byddin fawr" seremoni uchel, chwarterol, popeth-neu-ddim (yn hanesyddol brif achos rhaglenni a fethodd) â newidiadau bach, gwrthdroadwy, archwiliadwy sy'n bodloni rhwymedigaethau rheoli newid *trwy* awtomeiddio yn hytrach nag er gwaethaf hynny.

## Egwyddorion allweddol

- **Awtomeiddiwch bopeth ailadroddadwy.** Mae camau â llaw yn araf, yn dueddol o wallau, ac yn anarchwiliadwy.
- **Bagiau bach, rhyddhadau mynych.** Mae newidiadau bach yn haws eu hadolygu, eu profi, eu danfon, a'u gwrthdroi.
- **Adeiladwch ansawdd i mewn.** Mae profion a giatiau cyflym, awtomataidd yn dal diffygion cyn cynhyrchu, nid wedyn.
- **Gwahanwch ddefnyddio oddi wrth ryddhau.** Danfonwch god yn dywyll; troi nodweddion ymlaen gyda baneri pan fyddant yn barod.
- **Gwnewch bopeth yn wrthdroadwy.** Mae ôl-dröi cyflym ac amlygiad cynyddol yn troi defnyddio o fentar i arbrawf.
- **Y biblinell yw'r ffynhonnell wirionedd.** Os nad yw yn y rheolaeth fersiynau a'r biblinell, ni ddigwyddodd.
- **Mesurwch ganlyniadau, nid dim ond cynnyrch.** Mae cyfrif defnyddio'n gynnyrch; mae metrig wedi symud yn ganlyniad.

## Argymhellion

### Awtomeiddiwch y gyfres brofion a giatio arni

Awtomeiddio profion yw'r sylfaen sy'n gwneud danfon cyflym yn ddiogel. Gweithredwch bortffolio profion cytbwys, gan mwyaf awtomataidd (pennod 2.4): llawer o brofion uned cyflym, llai o brofion integreiddio a chontract, nifer fach o brofion o'r dechrau i'r diwedd, ynghyd â gwiriadau diogelwch (SAST/DAST/SCA: dadansoddiad statig, dynamig, a chyfansoddiad meddalwedd), hygyrchedd, a pherfformiad awtomataidd. Rhedwch nhw fel **giatiau ansawdd** yn y biblinell fel na fydd newid yn cyrraedd cynhyrchu heb basio. Cadwch y gyfres yn gyflym ac yn ddibynadwy: mae cyfres araf neu anwadal yn cael ei osgoi, sy'n trechu ei diben (pennod 8.5). Anelwch at i'r biblinell roi signal pasio/methu clir i ddatblygwr o fewn munudau i ymrwymiad.

### Ymarferwch integreiddio parhaus a chyflenwi parhaus

**Integreiddio parhaus (CI):** mae pob datblygwr yn uno newidiadau bach i mewn i'r brif linell yn fynych (yn ddelfrydol yn ddyddiol), gyda phob uniad yn sbarduno adeiladu a rhediad prawf awtomataidd. Cefnogir hyn orau gan ddatblygu seiliedig-ar-boncyff (pennod 2.6), sy'n cadw canghennau'n fyrhoedlog a'r integreiddio'n barhaus. **Cyflenwi parhaus (CD):** mae pob newid sy'n pasio'r biblinell *bob amser mewn cyflwr rhyddhadwy* ac yn gallu cael ei ddefnyddio ar alw. Mae **defnyddio parhaus** yn mynd gam ymhellach: mae pob newid sy'n pasio'n cael ei ddefnyddio i gynhyrchu'n awtomatig. Dewiswch lefel yr awtomeiddio sy'n briodol i'ch proffil risg; gall amgylcheddau rheoleiddiedig stopio ar gyflenwi parhaus gyda cham dyrchafu wedi'i reoli (pennod 8.1), ond dylent barhau i awtomeiddio popeth hyd at y giât honno.

### Defnyddiwch yn ddiogel gyda strategaethau cynyddol

Datgyplwch **ddefnyddio** (cod yn rhedeg mewn cynhyrchu) oddi wrth **ryddhau** (defnyddwyr yn profi'r newid), a datgelwch newidiadau'n raddol:

- Mae **[baneri nodwedd](https://en.wikipedia.org/wiki/Feature_toggle)** yn gadael i chi ddefnyddio cod yn dywyll a rhyddhau i segmentau ar alw, ac ôl-droi'n syth trwy doglo.
- Mae **rhyddhadau canari** yn llwybro canran fach o draffig at y fersiwn newydd, gan wylio metrigau iechyd cyn ehangu.
- Mae **defnyddiadau glas-gwyrdd** yn cadw dau amgylchedd ac yn newid traffig yn atomig, gydag ôl-dröi ar unwaith.
- Mae **defnyddiadau treiglo** yn disodli achosion yn gynyddrannol.
- Mae **danfon cynyddol** yn cyfuno baneri, canarïod, a dadansoddiad awtomataidd i ddyrchafu neu ôl-droi yn seiliedig ar signalau byw.

Parwch bob strategaeth ag ôl-dröi awtomataidd wedi'i sbarduno gan doriadau SLO neu losgi cyllideb gwallau (y gyfradd y mae methiannau'n treulio'r gyllideb annibynadwyedd a ganiateir; pennod 9.1). Gweler pennod 8.1 am y mecaneg.

### Offeryniwch fetrigau canlyniad: mesurwch y biblinell a'r effaith

Mae piblinell ddanfon sy'n danfon yn gyflym ond yn danfon y peth anghywir yn wastraff cyflym. Mesurwch ar dri lefel:

1. **Llif danfon, y pedwar metrig DORA:**
   - *Amlder defnyddio:* pa mor aml rydych yn rhyddhau i gynhyrchu.
   - *[Amser arwain](https://en.wikipedia.org/wiki/Lead_time) newidiadau:* o ymrwymiad i gynhyrchu.
   - *Cyfradd methiant newid:* canran y rhyddhadau sy'n achosi dirywiad.
   - *Amser adfer defnyddio wedi methu:* pa mor gyflym rydych yn adfer gwasanaeth (gynt MTTR, amser cymedrig i adfer).
   Mae perfformwyr elitaidd yn defnyddio ar alw, gydag amseroedd arwain o dan awr, cyfraddau methiant isel, ac adferiad mewn munudau. Ychwanegwch **fetrigau llif** o feddwl ffrwd werth (amser cylchred, [gwaith ar y gweill](https://en.wikipedia.org/wiki/Work_in_process), effeithlonrwydd llif) i weld lle mae gwaith yn aros.

2. **Dibynadwyedd ac ansawdd, SLIs a SLOs** (dangosyddion ac amcanion lefel gwasanaeth; pennod 9.1): a yw'r gwasanaeth yn bodloni ei dargedau dibynadwyedd a'i ymrwymiadau priodoledd ansawdd (pennod 11.1) ar ôl pob newid?

3. **Canlyniadau busnes a defnyddiwr** (penodau 7.3–7.4): a symudodd y newid y canlyniadau allweddol a'r KPIs a ddiffiniwyd gan ddarganfod? Dyma lle mae rhyddhau'n cwrdd ag arbrawf: danfonwch y tu ôl i faner, mesurwch yn erbyn rheolaeth, a chadwch dim ond yr hyn sy'n ennill.

### Caewch y ddolen yn ôl i ddarganfod

Nid defnyddio yw act olaf y biblinell ddanfon; **tystiolaeth** ydyw. Mae metrigau canlyniad (a gododd actifadu, a ddisgynnodd amser talu allan, a ostyngodd tocynnau cymorth) yn llifo yn ôl i mewn i'r biblinell ddarganfod (pennod 11.1) fel sylfaen ar gyfer y rownd nesaf o fentrau. Pan fydd darganfod a danfon wedi'u huno gan y ddolen adborth hon, mae'r sefydliad yn dod yn system ddysgu: mae rhagdybiaethau'n cael eu danfon, eu mesur, a naill ai eu graddio neu eu gwrthdroi, yn barhaus.

### Gwnewch ddanfon yn archwiliadwy ac wedi'i lywodraethu

Mewn lleoliadau menter a llywodraeth, triniwch y biblinell ei hun fel rheolaeth gydymffurfiaeth. Am fod pob newid yn llifo trwy reolaeth fersiynau a biblinell awtomataidd, rydych yn cael llwybr archwilio anhydraidd "am ddim": pwy newidiodd beth, pa brofion a chymeradwyaethau a'i giatiodd, a phryd y'i defnyddiwyd. Amgodiwch wahaniad dyletswyddau, adolygiadau gofynnol, a gwiriadau polisi fel **polisi fel cod** (rheolau llywodraethu wedi'u mynegi ar ffurf orfodadwy'n fecanyddol, wedi'i reoli gan fersiynau; pennod 8.2) fel bod rheolaeth newid yn cael ei gorfodi'n awtomatig a'i dystiolaethu'n barhaus (penodau 4.6 a 10.2), yn hytrach na'i hailadeiladu â llaw cyn archwiliad.

## Cyfnewidfeydd: manteision ac anfanteision

| Penderfyniad | Manteision | Anfanteision |
|---|---|---|
| **Defnyddio parhaus (awto i gynhyrchu)** | Yr adborth cyflymaf; y bagiau lleiaf; y ffwdan â llaw lleiaf | Angen profion, monitro, ôl-dröi aeddfed; anodd mewn giatiau rheoleiddiedig |
| **Cyflenwi parhaus gyda dyrchafiad â llaw** | Pwynt rheolaeth dynol/cydymffurfiaeth; cyfeillgar i archwiliad | Arafach; risg o fagio newidiadau wrth y giât |
| **Baneri nodwedd** | Gwahaniad defnyddio/rhyddhau; ôl-dröi ar unwaith; targedu | Dyled baner a chymhlethdod cyfuniadol os na chânt eu tocio |
| **Canari / danfon cynyddol** | Yn cyfyngu radiws ffrwydro; dyrchafiad wedi'i yrru gan ddata | Angen arsylwadaeth gref a rheolaeth traffig |
| **Glas-gwyrdd** | Newid ac ôl-dröi ar unwaith | Dyblu cost amgylchedd; mae mudo cyflyrol/data'n dyllog |
| **Proses ryddhau â llaw drwm** | Yn teimlo'n reoledig; yn gyfarwydd i archwilwyr | Araf, tueddol o wallau, anailadroddadwy, wedi'i archwilio'n wael mewn gwirionedd |

Y gred cyfnewid hanesyddol, *ewch yn gyflymach a byddwch yn torri mwy*, yw'r un allweddol i'w hymddeol. Mae'r dystiolaeth yn dangos mai'r arferion sy'n cynyddu cyflymder (awtomeiddio, bagiau bach, profion cyflym, gwrthdroadwyedd) yw'r *un* arferion sy'n cynyddu sefydlogrwydd. Mae'r cyfnewidfeydd go iawn yn ymwneud â **buddsoddiad a graenusrwydd rheolaeth**, nid cyflymder-yn-erbyn-diogelwch.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Beth yw eich proffil risg gwirioneddol, ac a yw'n cyfiawnhau stopio ar gyflenwi parhaus yn hytrach na mynd at ddefnyddio parhaus?** Mae dewis lefel yr awtomeiddio'n benderfyniad go iawn, nid diofyn. Mae defnyddio parhaus yn rhoi'r adborth cyflymaf a'r bagiau lleiaf, ond mae'n gofyn am brofion aeddfed, arsylwadaeth gref, ac ôl-dröi ar unwaith, felly gall cyd-destun rheoleiddiedig stopio'n rhesymegol ar giât dyrchafu wedi'i reoli. Dewch â thystiolaeth: eich cyfradd methiant newid, eich amser adfer, a dibynadwyedd eich cyfres brofion, oherwydd mae'r rheini'n dweud wrthych a yw awto-i-gynhyrchu'n ddiogel heddiw. I fenter a llywodraeth, awtomeiddiwch bopeth hyd at y giât a gwnewch y giât ei hun yn bolisi fel cod, fel bod y cam dynol yn ychwanegu rheolaeth heb ychwanegu ffwdan â llaw. Os na allwch eto ymddiried yn y biblinell i ddal newid gwael, buddsoddwch mewn giatiau ac arsylwadaeth cyn troi'r switsh.

2. **A all eich biblinell gynhyrchu'r dystiolaeth archwilio y byddai rheoleiddiwr yn gofyn amdani, heb i unrhyw un ei hailadeiladu â llaw?** Triniwch y biblinell ei hun fel rheolaeth gydymffurfiaeth. Dylai pob newid gario llwybr anhydraidd o bwy newidiodd beth, pa brofion a chymeradwyaethau a'i giatiodd, a phryd y'i defnyddiwyd, wedi'i gynhyrchu'n awtomatig. Mewn menter a llywodraeth, amgodiwch wahaniad dyletswyddau ac adolygiadau gofynnol fel polisi fel cod fel bod rheolaeth newid yn cael ei gorfodi a'i dystiolaethu'n barhaus yn hytrach na'i chydosod mewn panig cyn archwiliad. Y signal i'w ddwyn: dewiswch newid cynhyrchu diweddar a cheisiwch gynhyrchu ei lwybr cymeradwyo-a-phrawf llawn mewn pum munud. Os na allwch, rydych yn talu am baratoi archwiliad â llaw ac yn cario risg y byddai awtomeiddio'n ei dileu.

3. **Pan fydd rhyddhad yn dechrau dirywio mewn cynhyrchu, beth sy'n sbarduno ôl-dröi, ac a yw'n awtomatig?** Gwrthdroadwyedd yw'r hyn sy'n gwneud cyflymder yn rhesymegol yn hytrach na byrbwyll, felly mae'r sbardun ôl-dröi'n haeddu dyluniad eglur. Penderfynwch a yw toriad SLO neu losgi cyllideb gwallau'n ôl-droi'n awtomatig, neu a oes rhaid i ddynol sylwi, penderfynu, a gweithredu tra bod defnyddwyr yn dioddef. Dewch â'ch ychydig ddigwyddiadau diwethaf a mesurwch y bwlch rhwng "metrig yn dechrau dirywio" a "newid wedi'i wrthdroi"; dyna'ch radiws ffrwydro go iawn. I dimau mawr sy'n danfon lawer gwaith y dydd, nid yw ôl-dröi â llaw'n graddfeydd, ac mae baneri ynghyd â dadansoddiad canari'n gadael i chi ddyrchafu neu wrthdroi ar signalau byw. Os yw'ch ateb yn "mae rhywun yn cael ei fagio ac yn ei ddatrys," rydych yn trin pob defnyddiad fel mentar anwrthdroadwy.

4. **Pan fyddwch yn danfon nodwedd, ydych chi'n mesur a symudodd hi mewn gwirionedd y metrig y bwriadwyd iddi ei symud, neu a ydych yn cyfrif y defnyddiad a symud ymlaen?** Mae piblinell sy'n danfon yn gyflym ond byth yn gwirio effaith yn wastraff cyflym, a'r bwlch rhwng cynnyrch a chanlyniad yw lle mae'r rhan fwyaf o fuddsoddiad danfon yn gollwng yn dawel. I sefydliad mawr, mae cannoedd o ryddhadau'r wythnos yn ei gwneud yn demtasiwn trin amlder defnyddio fel y bwrdd sgorio, ac eto mae amlder yn mesur symudiad, nid gwerth; y tyniad cystadleuol yw bod mesur canlyniad yn costio offeryniaeth, grŵp rheolaeth, a'r ddisgyblaeth i adael nodwedd sy'n colli wedi'i throi i ffwrdd. Dewch â'r llond llaw diwethaf o nodweddion a ddanfonwyd ac, ar gyfer pob un, y metrig targed a ddiffiniwyd gan ddarganfod, y mesur cyn-ac-ar-ôl, a beth wnaethoch pan na symudodd. Mewn portffolios menter a llywodraeth, enwch pwy sy'n adolygu canlyniadau ar batrwm sefydlog a phwy sydd ag awdurdod i ymddeol nodwedd a ddanfonwyd ond na thalodd erioed, oherwydd bod newid nad oes neb yn atebol am ei fesur yn un na fydd neb byth yn ei ddiffodd. Y prawf gonest yw a allwch bwyntio at nodwedd a wrthdroesoch *oherwydd* i'r dystiolaeth ddweud iddi golli.

5. **Faint o amser mae'ch biblinell yn ei gymryd i roi signal pasio/methu i ddatblygwr, ac a ydynt yn ymddiried digon yn y profion i beidio â llwybro o'u cwmpas?** Cyflymder adborth ac ymddiriedaeth yn y gyfres yw'r hyn sy'n gwneud giatiau ansawdd yn giatio go iawn yn hytrach na chael eu hosgoi, ac mae'r ddau'n erydu'n dawel wrth i sylfaen god dyfu. I dîm mawr, mae cyfres sy'n cymryd deugain munud neu'n anwadalu un rhediad mewn deg yn hyfforddi cannoedd o beirianwyr i uno ar goch, analluogi gwiriadau, neu ailrhedeg hyd nes gwyrdd, sy'n tawel ddileu'r diogelwch a gyfiawnhaodd fynd yn gyflym yn y lle cyntaf; y ystyriaethau cystadleuol yw cwmpas a realaeth profion yn erbyn cyflymder a sefydlogrwydd adborth, ac mae gwthio'r naill neu'r llall yn rhy galed yn tanseilio'r llall. Dewch â hyd cyfredol y biblinell, y gyfradd ailredeg anwadal, ac unrhyw dystiolaeth o giatiau'n cael eu hepgor neu eu marcio'n annorfodol. I gyd-destunau menter a llywodraeth lle mae'r giatiau hynny hefyd yn cario gwiriadau SAST, DAST, a pholisi sy'n bodloni cydymffurfiaeth, mae giât wedi'i hosgoi'n risg ansawdd ac yn fwlch archwilio fel ei gilydd, felly mesurwch a yw'r giât wir yn orfodol neu'n gynghorol yn unig. Os na all datblygwyr ddweud pam maent yn ymddiried mewn adeiladwaith gwyrdd, addurn yw'r giât.

6. **Pwy sy'n berchen ar gadw'r llwybr danfon yn gyson ar draws timau a thocio dyled baneri nodwedd, neu a yw pob tîm yn ailddyfeisio ei biblinell ei hun?** Wrth i sefydliad dyfu, mae danfon naill ai'n cydgyfeirio ar ffordd wedi'i phalmentu a rennir neu'n dryllio'n ddwsinau o biblinellau pwrpasol â giatiau anghydnaws, llwybrau archwilio anwastad, a baneri sy'n goroesi eu diben. Mae'r tensiwn yn real: mae ffordd wedi'i phalmentu ganolog yn rhoi cysondeb, llywodraethu, ac economïau graddfa i chi, ond mae mandad sy'n anwybyddu cyfyngiadau gwirioneddol tîm yn magu piblinellau cysgod a chwerwder, felly rhaid i'r ffordd wedi'i phalmentu fod yn ddigon da fel bod timau'n optio i mewn yn wirfoddol. Dewch ag inventori o sawl piblinell wahanol sy'n bodoli heddiw, sut mae creu a dileu baneri'n cael eu llywodraethu, a faint mae amser arwain ac ansawdd archwilio'n amrywio rhwng eich timau gorau a gwaethaf. Mewn lleoliadau menter a llywodraeth, ychwanegwch yr ongl gydymffurfiaeth: mae piblinellau anghyson yn golygu bod tystiolaeth gwahaniad dyletswyddau a rheolaeth newid yn cael ei brofi'n wahanol (neu ddim o gwbl) ym mhob tîm, ac mae un ffordd wedi'i phalmentu wedi'i harchwilio gyda pholisi fel cod yn troi hynny o gambl fesul tîm yn warant sefydliadol. Os nad oes neb yn berchen ar ddileu baneri hen, bydd y dyled cyfuniadol yn y pen draw yn gwneud y system yn anbrofadwy.

## Lens sector

**Cwmni newydd.** Cyflymder yw goroesiad, felly prynwch eich piblinell yn hytrach na'i hadeiladu: gwifrwch ddatblygu seiliedig-ar-boncyff i redwr CI wedi'i westeio, giatiwch bob uniad ar brofion uned cyflym a sganiad diogelwch, a defnyddiwch yn syth i gynhyrchu y tu ôl i wasanaeth baner nodwedd wedi'i westeio. Sgipiwch y tîm platfform a'r offer pwrpasol; eich adnodd prinnaf yw sylw peirianneg, ac mae piblinell y gall un cyffredinolwr sengl ei chynnal yn well nag un ymhelaeth nad oes gan neb amser i'w thrwsio. Trac y pedwar metrig DORA ar ddangosfwrdd syml o'r diwrnod cyntaf fel eich bod yn dysgu'ch llif yn gynnar ac yn gallu dangos i fuddsoddwyr eich bod yn danfon bob dydd heb dorri pethau.

**Busnes bach.** Heb beiriannydd rhyddhau pwrpasol a chyllideb dynn, triniwch ddanfon fel rhywbeth rydych yn ei gydosod o wasanaethau wedi'u rheoli yn hytrach na system rydych yn ei staffio: CI/CD wedi'i reoli, offeryn baner wedi'i westeio, a phlatfform cwmwl sy'n trin cyflwyno ac ôl-dröi i chi. Gwrthsefwch adeiladu seilwaith piblinell pwrpasol na allwch fforddio ei gynnal, a chadwch y llwybr yn ddigon syml fel bod pwy bynnag sydd ar alwad yn gallu ei ddeall dan bwysau. Ffafriwch offer sy'n gwneud danfon cynyddol ac ôl-dröi un-clic ar gael yn syth, oherwydd dyna'r galluoedd sy'n troi defnyddiad brawychus ddydd Gwener yn un arferol.

**Menter.** Y broblem graidd yw cysondeb ar draws llawer o dimau: piblinell ffordd-wedi'i-phalmentu â chymorth gyda giatiau prawf, diogelwch, a pholisi-fel-cod awtomataidd y mae timau'n optio i mewn iddynt yn hytrach na'u hailddyfeisio. Safonwch y rhyngwyneb fel bod metrigau DORA ac SLO'n gymharadwy ar draws y sefydliad, cyllidebwch y gallu platfform sy'n cynnal y ffordd wedi'i phalmentu'n benodol, a rheolwch faneri nodwedd ac atchweliadau amser arwain fel asedau a lywodraethir yn hytrach na llên gwerin fesul tîm. Mae llywodraethu ac archwilio'n dod yn awtomatig pan fydd pob newid yn llifo trwy'r un llwybr, wedi'i reoli gan fersiynau a giatiedig.

**Llywodraeth.** Mae rheolau caffael, tryloywder, ac atebolrwydd cyhoeddus yn siapio'r biblinell, felly ffafriwch gyflenwi parhaus sy'n stopio ar giât dyrchafu awtomataidd sy'n gorfodi gwahaniad dyletswyddau a chymeradwyaethau gofynnol fel polisi fel cod. Gwnewch y biblinell ei hun yn rheolaeth gydymffurfiaeth: mae pob newid yn cario llwybr archwilio anhydraidd sy'n bodloni rhwymedigaethau rheoli newid ac awdurdod-i-weithredu heb ailadeiladu â llaw. Disodlwch ryddhadau "byddin fawr" seremoni uchel â newidiadau bach, gwrthdroadwy, datgyplwyd, fel y gallwch beilota lif sy'n wynebu'r cyhoedd mewn un rhanbarth, mesur cyfraddau gwall a chwblhau, ac ôl-droi mewn munudau os yw'n dirywio.

## Enghreifftiau

**Cwmni newydd.** Mae tîm tri pheiriannydd sy'n danfon offeryn dadansoddeg B2B yn dechrau trwy ddefnyddio â llaw ar brynhawniau Gwener, sy'n golygu rhyddhad brawychus unwaith yr wythnos a phenwythnos o arswyd. Mewn prynhawn maent yn gwifro datblygu seiliedig-ar-boncyff gyda phiblinell GitHub Actions: profion uned cyflym, leinsiwr, a sganiad diogelwch yn giatio pob uniad, ac mae adeiladwaith sy'n pasio'n defnyddio'n syth i gynhyrchu y tu ôl i faneri LaunchDarkly. Mae amlder defnyddio'n neidio o wythnosol i sawl gwaith y dydd, ac am fod pob nodwedd newydd yn danfon yn dywyll ac yn troi ymlaen ar gyfer un cwsmer cyfeillgar yn gyntaf, mae allforio CSV wedi torri'n cael ei ddal a'i doglo i ffwrdd mewn munudau yn lle dod yn ddigwyddiad dydd Llun. Maent yn tracio'r pedwar metrig DORA ar ddangosfwrdd syml fel y gallant ddangos i fuddsoddwyr fod y tîm yn danfon bob dydd heb dorri pethau.

**Menter.** Mae yswiriwr byd-eang yn cyfuno 40 tîm ar biblinell ffordd-wedi'i-phalmentu a rennir (cadwyn offer diofyn a gefnogir, wedi'i chyn-integreiddio y mae timau'n optio i mewn iddi; pennod 8.4): datblygu seiliedig-ar-boncyff, giatiau prawf a diogelwch awtomataidd, a defnyddio canari gydag ôl-dröi awtomataidd ar doriad SLO. Mae amlder defnyddio'n codi o fisol i sawl gwaith y dydd; mae amser arwain yn disgyn o chwe wythnos i lai na diwrnod; mae cyfradd methiant newid yn gostwng oherwydd bod bagiau'n fach a giatiau'n awtomataidd. Yn hollbwysig, mae nodweddion cynnyrch bellach yn danfon y tu ôl i faneri ac yn cael eu mesur yn erbyn rheolaethau, fel y gall yr yswiriwr gysylltu pob rhyddhad â'i effaith ar gyfradd cwblhau dyfynbrisiau, gan gysylltu'r biblinell ddanfon yn uniongyrchol â chanlyniadau allweddol ochr-ddarganfod pennod 11.1.

**Llywodraeth.** Mae asiantaeth gyhoeddus yn disodli rhyddhadau chwarterol "byddin fawr" (pob un yn benwythnos o gamau â llaw ac yn ffynhonnell fynych o doriadau) â phiblinell gyflenwi barhaus sy'n stopio ar giât dyrchafu awtomataidd sy'n gorfodi gwahaniad dyletswyddau a chymeradwyaethau gofynnol fel polisi fel cod. Mae pob newid yn cario llwybr archwilio anhydraidd sy'n bodloni rhwymedigaethau rheoli newid ac ATO (awdurdod i weithredu) yr asiantaeth (pennod 4.6). Mae rhyddhadau'n dod yn fach, yn fynych, ac yn wrthdroadwy; mae amser adfer yn disgyn o ddyddiau i funudau; ac am fod defnyddio wedi'i ddatgyplu oddi wrth ryddhau trwy faneri, gall yr asiantaeth beilota lif budd-daliadau newydd gydag un rhanbarth cyn cyflwyniad cenedlaethol, gan fesur cyfraddau cwblhau a gwall cyn ymrwymo.

## Achos busnes: cymhellion, ROI, a TCO

Mae'r enillion ar fuddsoddiad piblinell ddanfon ymhlith y rhai gorau eu tystiolaeth mewn meddalwedd. Mae amser arwain cyflymach ac amlder defnyddio uwch yn golygu bod syniadau'n cyrraedd defnyddwyr (ac yn dechrau dychwelyd gwerth, neu'n cael eu cywiro) yn gynt. Mae cyfradd methiant newid is ac adferiad cyflymach yn golygu llai o amser segur, llai o ymladd tân, a llai o ddifrod i enw da a rheoleiddiol. Mae ymchwil DORA yn cysylltu'r galluoedd hyn â pherfformiad masnachol a sefydliadol rhagorol, nid dim ond cysur peirianneg. Mae'r effaith cyfansymio'n bwysig: mae tîm sy'n danfon ac yn dysgu'n ddyddiol yn ailadrodd 20–30x yn amlach na thîm sy'n danfon yn fisol, ac mae'r gyfradd ddysgu honno'n benderfynol dros oes cynnyrch.

Ar **[gost gyfan perchnogaeth](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**, mae awtomeiddio'n symud cost o ffwdan â llaw parhaus i fuddsoddiad piblinell un-tro-ynghyd-chynnal. Mae rhyddhad â llaw'n treulio oriau peiriannydd hŷn bob tro, yn graddfeydd yn wael, ac yn cynhyrchu tystiolaeth archwilio wan. Mae piblinell awtomataidd yn amorteiddio'r gost honno, yna'n ei *gostwng* wrth i gyfaint dyfu, tra'n cynhyrchu tystiolaeth gryfach yn barhaus. Mae gwrthdroadwyedd yn gostwng cost methiant ei hun: pan ellir ôl-droi unrhyw newid mewn eiliadau, mae cost ddisgwyliedig defnyddiad gwael yn cwympo, sef yr hyn sy'n gwneud symud yn gyflym yn rhesymegol yn hytrach na byrbwyll.

I wneud yr achos i arweinyddiaeth, mesurwch y llinell sylfaen bresennol gyda'r pedwar metrig DORA a'r oriau â llaw a dreulir fesul rhyddhad, yna meintioli'r ffwdan a ddilëwyd a'r amser segur a osgowyd. Mae cost mabwysiadu'n real, sef peirianneg piblinell, buddsoddiad prawf, a gallu platfform/ffordd-wedi'i-phalmentu (pennod 8.4), ond mae cost *peidio* â buddsoddi'n cael ei thalu'n barhaus mewn adborth araf, risg diwrnod-rhyddhau, llosgi peiriannydd, a phoen archwilio. Y ddadl derfynol yw'r cyswllt darganfod: piblinell ddanfon gyflym, wedi'i mesur yw'r hyn sy'n gwneud mentrau dilysedig y biblinell ddarganfod mewn gwirionedd yn brofadwy mewn cynhyrchu.

## Gwrth-batrymau a pheryglon

- **Mesur cynnyrch, nid canlyniad:** dathlu cyfrifon defnyddio tra bod metrigau targed yn aros yn wastad.
- **Cyfresi profion araf neu anwadal:** giatiau y mae datblygwyr yn dysgu eu hanwybyddu neu eu hosgoi.
- **Rhyddhadau byddin-fawr, anfynych:** bagiau mawr sy'n risglyd, yn anodd eu dadfygio, ac yn anodd eu gwrthdroi.
- **Defnyddio a rhyddhau wedi'u cyfuno:** dim baneri nodwedd, felly mae pob defnyddiad yn fentar anwrthdroadwy sy'n wynebu defnyddwyr.
- **Theatr ryddhau â llaw:** rhestri gwirio â llaw sy'n araf, yn anghyson, ac wedi'u harchwilio'n wael.
- **Piblinell awtomataidd, dim arsylwadaeth:** danfon yn gyflym heb allu i ganfod neu ddiagnosio atchweliadau.
- **Dyled baneri nodwedd:** baneri byth yn cael eu dileu, gan gronni'n gymhlethdod cyfuniadol anbrofadwy.
- **Gemio metrigau DORA:** hollti defnyddiadau i chwyddo amlder yn lle gwella llif.
- **Dim dolen adborth:** canlyniadau byth yn cael eu mesur, felly nid yw danfon byth yn hysbysu'r cylch darganfod nesaf.

## Model aeddfedrwydd

- **Lefel 1, Cychwyn:** Rhyddhadau â llaw, anfynych, seremoni uchel; profi'n bennaf â llaw ac wedi'i redeg â llaw; llwyddiant wedi'i fesur fel "fe'i danfonwyd"; mae ôl-dröi'n boenus ac wedi'i ddyfeisio ar y pryd; dim syniad a rennir o sut y dylai danfon weithio.
- **Lefel 2, Datblygu:** Mae rhai timau'n sefydlu CI gydag adeiladau awtomataidd a rhai profion; mae rhyddhadau wedi'u hamserlennu; mae monitro sylfaenol yn bodoli; mae arferion yn amrywio o dîm i dîm ac nid yw metrigau DORA'n cael eu tracio eto, felly mae danfon yn well mewn pocedi ond yn anghyson ar draws y sefydliad.
- **Lefel 3, Safoni:** Mae piblinell ffordd-wedi'i-phalmentu, ddogfennedig yn cael ei gorfodi ar draws y sefydliad: cyflenwi parhaus gyda giatiau prawf a diogelwch awtomataidd, defnyddio cynyddol gydag ôl-dröi, a gwahaniad dyletswyddau wedi'i orfodi fel polisi fel cod. Mae'r biblinell yn darparu llwybr archwilio anhydraidd, ac mae pob tîm yn dilyn yr un llwybr wedi'i reoli gan fersiynau yn hytrach nag un pwrpasol.
- **Lefel 4, Rheoli:** Mae'r biblinell yn cael ei mesur a'i rheoli yn erbyn llinellau sylfaen. Mae'r pedwar metrig DORA (amlder defnyddio, amser arwain, cyfradd methiant newid, amser adfer), cyflawniad SLO, llosgi cyllideb gwallau, a metrigau llif fel amser cylchred a gwaith-ar-y-gweill yn cael eu tracio yn erbyn targedau, ac mae giatiau ac ôl-dröi'n tanio ar drothwyon mesuredig yn hytrach na barn. Mae dyled baneri, cyfraddau prawf anwadal, ac atchweliadau amser arwain yn cael eu monitro, a gwneir pob penderfyniad mynd neu beidio-mynd ar sail tystiolaeth.
- **Lefel 5, Cerddorfa:** Mae danfon yn cael ei wella'n barhaus ac wedi'i integreiddio â darganfod a chynllunio risg. Mae defnyddio parhaus yn rhedeg lle bo'n briodol gyda danfon cynyddol ac ôl-dröi awtomataidd; mae nodweddion yn danfon fel arbrofion wedi'u mesur y mae eu metrigau canlyniad yn dolennu'n ôl i'r rownd nesaf o fentrau; mae perfformiad DORA elitaidd yn cael ei gynnal ar draws timau trwy'r ffordd wedi'i phalmentu; ac mae'r sefydliad yn ailddiwnio giatiau, trothwyon, a chapasiti'n addasol wrth i lwyth, risg, a chymysgedd cynnyrch newid.

## Syniadau ar gyfer trafod

1. Beth yw eich pedwar metrig DORA cyfredol, a lle mae'r tagfa fwyaf yn eich llif ymrwymiad-i-gynhyrchu?
2. A allwch wahanu defnyddio oddi wrth ryddhau heddiw? Os na allwch, beth fyddai baneri nodwedd yn ei newid ynghylch eich risg?
3. Faint o amser mae'ch cyfres brofion yn ei gymryd, ac a yw datblygwyr yn ymddiried digon ynddi i beidio â'i hosgoi?
4. Pan ddanfonoch chi eich nodwedd ddiwethaf, wnaethoch chi fesur a symudodd hi'r metrig y bwriadwyd iddi ei symud?
5. Mewn cyd-destun rheoleiddiedig, a yw'ch proses rheoli newid yn arafu danfon *neu* a yw'n cael ei orfodi'n awtomatig trwy'r biblinell?
6. Pa faneri nodwedd yn eich sylfaen god ddylai fod wedi cael eu dileu misoedd yn ôl?

## Casgliadau allweddol

- Mae'r biblinell ddanfon yn troi syniadau dilysedig yn feddalwedd sy'n rhedeg, wedi'i mesur, ac yn bwydo canlyniadau yn ôl i ddarganfod (pennod 11.1).
- Awtomeiddiwch y llwybr cyfan: **giatiau prawf** cyflym, **CI/CD**, a **seilwaith fel cod**, gyda'r biblinell fel ffynhonnell wirionedd.
- **Gwahanwch ddefnyddio oddi wrth ryddhau** a defnyddiwch strategaethau cynyddol (baneri, canari, glas-gwyrdd) gydag ôl-dröi awtomataidd.
- Mesurwch ar dri lefel: metrigau **DORA/llif**, **dibynadwyedd/SLOs**, a **chanlyniadau busnes/defnyddiwr**.
- Mae cyflymder a sefydlogrwydd yn **atodolion**, nid cyfnewidfeydd: mae'r arferion sy'n danfon y naill yn danfon y llall.
- Mae'r biblinell hefyd yn **rheolaeth gydymffurfiaeth**: mae awtomeiddio'n cynhyrchu llwybr archwilio anhydraidd, parhaus.
- Mae'r ROI'n gyflym, wedi'i dystiolaethu'n dda (DORA), ac yn cyfansymio; mae prif gost peidio â buddsoddi'n cael ei thalu'n barhaus.

## Cyfeiriadau a darllen pellach

- *Accelerate: The Science of Lean Software and DevOps*, gan Nicole Forsgren, Jez Humble, Gene Kim (metrigau a thystiolaeth DORA).
- *Continuous Delivery*, gan Jez Humble a David Farley (y testun sylfaenol).
- *The DevOps Handbook*, gan Kim, Humble, Debois, Willis.
- *The Phoenix Project*, gan Gene Kim, Kevin Behr, George Spafford (naratif ar lif).
- *Site Reliability Engineering*, gan Beyer, Jones, Petoff, Murphy, gol. (SLIs/SLOs, cyllidebau gwallau).
- *Team Topologies*, gan Matthew Skelton a Manuel Pais (ffyrdd wedi'u palmentu a dyluniad timau danfon).
- *Feature Flags / progressive delivery*, ysgrifau gan Pete Hodgson a chymunedau LaunchDarkly/Split.
- Google DORA, adroddiadau *Accelerate State of DevOps* (blynyddol).
- Kim, Gene, *The Unicorn Project* (golwg profiad-datblygwr ar lif).
- Reinertsen, Donald, *The Principles of Product Development Flow* (maint bagiau, ciwiau, economeg llif).
