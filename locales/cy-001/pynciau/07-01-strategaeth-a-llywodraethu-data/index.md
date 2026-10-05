# 7.1 Strategaeth a llywodraethu data

## Trosolwg a chymhelliant

Strategaeth ddata yw eich cynllun bwriadol ar gyfer trin data fel ased: sut mae'n cael ei gynhyrchu, ei ddisgrifio, ei berchnogi, ei ddiogelu, ei rannu, a'i ddefnyddio i greu gwerth. Mae [llywodraethu data](https://en.wikipedia.org/wiki/Data_governance) yn system weithredu sy'n gwireddu'r strategaeth: y rolau, polisïau, safonau, a rheolaethau sy'n cadw data'n ddibynadwy ac yn gydymffurfiol dros amser. Mewn timau bach, mae'r pryderon hyn yn aml yn ymhlyg, wedi'u cario ym mhennau ychydig o beirianwyr. Ar raddfa sefydliadau datblygwyr mawr, mentrau, ac asiantaethau llywodraeth, mae'r anffurfioldeb hwnnw'n chwalu. Mae cannoedd o dimau'n cynhyrchu miloedd o dablau. Mae dwsinau o systemau'n honni dal cofnod "gwirioneddol" cwsmer. Ac ni all neb ddweud gyda hyder pa rif sy'n gywir mewn cyflwyniad bwrdd neu adroddiad cyhoeddus.

I dimau mawr, nid yw cost llywodraethu data gwael yn haniaethol. Mae rheoleiddwyr yn disgwyl llinach y gellir ei ddangos a rheolaeth dros ddata personol, ariannol, ac iechyd o dan gyfundrefnau fel [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) (Rheoliad Cyffredinol Diogelu Data'r UE), [HIPAA](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act) (Deddf Cludadwyedd ac Atebolrwydd Yswiriant Iechyd UDA), a rheolau penodol i sectorau. Mae mentrau'n wynebu amlygiad ariannol uniongyrchol o fetrigau wedi'u camadrodd, archwiliadau wedi methu, a phlatfformau data dyblyg. Mae asiantaethau llywodraeth yn cario rhwymedigaethau ychwanegol ynghylch cadw cofnodion, mynediad rhyddid gwybodaeth, atebolrwydd cyhoeddus, a thriniaeth deg o ddinasyddion. Ym mhob un o'r lleoliadau hyn, mae data na allwch ymddiried ynddo'n waeth na dim data, oherwydd mae'n gyrru penderfyniadau hyderus ond anghywir.

Mae'r syniad sy'n gyrru cynnydd ar raddfa fawr yn syml: trin data fel cynnyrch. Yn hytrach na bod data'n gynnyrch sgil-effaith cymwysiadau, mae gan bob set ddata bwysig berchennog, rhyngwyneb dogfennedig, gwarantau ansawdd, a defnyddwyr sy'n cael eu trin fel cwsmeriaid. Mae'r bennod hon yn ymdrin â'r meddylfryd cynnyrch hwnnw ochr yn ochr â'r disgyblaethau llywodraethu clasurol: stiwardiaeth, catalogio, [rheoli data meistr](https://en.wikipedia.org/wiki/Master_data_management), ac ansawdd. Mae hefyd yn ymdrin â'r dewisiadau sefydliadol sy'n penderfynu pa fodel sy'n ffitio'ch tîm: [gwe ddata](https://en.wikipedia.org/wiki/Data_mesh) (data datganoledig, wedi'i berchnogi gan barth, wedi'i gyhoeddi fel cynhyrchion), llyn-warws data (rheolaeth a llywodraethu ar arddull warws wedi'u haenu dros [lyn data](https://en.wikipedia.org/wiki/Data_lake) hyblyg), a [warws data](https://en.wikipedia.org/wiki/Data_warehouse) (storfa ganolog lywodraethedig o ddata wedi'i fodelu, yn barod i'w ymholi).

*Gweler hefyd:* pennod 4.5 (preifatrwydd a diogelu data), pennod 7.2 (peirianneg data), a phennod 4.6 (cydymffurfiaeth a llywodraethu).

## Egwyddorion allweddol

- Mae data'n ased parhaol gyda pherchnogion, nid yn sgil-gynnyrch tafladwy o gymwysiadau.
- Mae gan bob set ddata bwysig berchennog enwedig, atebol a chontract dogfennedig.
- Mae llywodraethu'n galluogi defnydd dibynadwy; nid yw'n glwyd fiwrocrataidd sy'n dweud "na" yn unig.
- Dylai fod un ffynhonnell awdurdodol ar gyfer pob endid busnes critigol.
- Mae ansawdd, preifatrwydd, a llinach yn cael eu cynllunio i mewn, nid eu harchwilio i mewn wedyn.
- Mae defnyddwyr data'n gwsmeriaid y mae eu hanghenion yn llunio'r cynnyrch.
- Mae polisïau'n cael eu hamgodio a'u gorfodi'n awtomatig lle bynnag y bo modd, nid eu gadael i ewyllys da.
- Mae perchnogaeth ffederal yn graddio'n well nag un tîm canolog wrth i'r sefydliad dyfu.

## Argymhellion

### Triniwch ddata fel cynnyrch

Rhowch berchennog cynnyrch i bob set ddata sylweddol sy'n atebol am ei addasrwydd i'w ddefnyddio. Mae gan gynnyrch data enw, sgema dogfennedig, disgrifiad o'i ystyr a'i darddiad, cyflymder adnewyddu diffiniedig, a disgwyliadau ansawdd cyhoeddedig. Dylai eich defnyddwyr allu ei ddarganfod, ei ddeall, a dibynnu arno heb ofyn un cwestiwn i'r tîm sy'n ei gynhyrchu. Cymhwyswch yr un ddisgyblaeth â'r un rydych yn ei chymhwyso i APIs meddalwedd: fersiynu, hysbysiadau dirymu, cofnodion newid, a chydnawsedd yn ôl.

### Sefydlwch gontractau data a SLAs

Mae contract data'n gytundeb penodol, y gellir ei wirio gan beiriant, rhwng cynhyrchydd a'i ddefnyddwyr. Mae'n ymdrin â sgema, semanteg, ffresni, cyfaint, a newidiadau a ganiateir. Gorfodwch gontractau yn y biblinell fel bod newid torfol i fyny'r afon yn methu'n gyflym wrth y ffynhonnell, yn hytrach na llygru adroddiadau i lawr yr afon yn dawel wythnosau'n ddiweddarach. Parwch gontractau â chytundebau ac amcanion lefel gwasanaeth. Er enghraifft, "dimensiwn cwsmer wedi'i adnewyddu erbyn 06:00 yn ddyddiol, 99.5% o'r dyddiau, gyda llai na 0.1% o allweddi busnes gwag." Cyhoeddwch y rhain, a rhybuddiwch am doriadau.

### Adeiladwch stiwardiaeth a model gweithredu llywodraethu

Cadwch atebolrwydd ar wahân i weithredu. Mae perchnogion data (arweinwyr busnes yn aml) yn atebol am barth. Mae stiwardiaid data (arbenigwyr pwnc) yn cynnal diffiniadau, yn datrys materion ansawdd, ac yn cymeradwyo mynediad. Mae cyngor llywodraethu data ysgafn yn gosod safonau traws-doriadol ac yn setlo anghydfodau. Cadwch y model yn ffederal: mae tîm galluogi canolog yn darparu offer, safonau, a hyfforddiant, tra bod timau parth yn berchen ar eu data. Mae hyn yn osgoi tagfa canoli llawn a hefyd anhrefn dim llywodraethu o gwbl.

### Buddsoddwch mewn catalog data a llinach

Catalog y gellir chwilio ynddo yw'r drws ffrynt i'ch ystad ddata. Dylai ddal geirfaoedd busnes, sgemâu technegol, perchnogaeth, dosbarthiadau sensitifrwydd, sgorau ansawdd, a llinach o'r dechrau i'r diwedd o'r system ffynhonnell trwy drawsffurfiadau i ddangosfyrddau. Awtomeiddiwch gasglu metadata yn hytrach na dibynnu ar ddogfennaeth â llaw, sy'n pydru'n gyflym. Mae llinach yn hanfodol ar gyfer dadansoddi effaith, ymateb i ddigwyddiadau, archwilio, a cheisiadau rheoleiddiol fel mynediad a dileu gwrthrych data.

### Rheoli data meistr ac un ffynhonnell wirionedd

Ar gyfer endidau craidd (cwsmer, dinesydd, cynnyrch, cyflenwr, gweithiwr), defnyddiwch reoli data meistr i gysoni dyblygiadau a chofnodion gwrthdrawiadol yn un cofnod aur. Dewiswch bensaernïaeth (cofrestrfa, cyfnerthiad, cydfodolaeth, neu ganoledig) yn seiliedig ar pa mor awdurdodol y mae angen i'r hyb fod. Diffiniwch reolau paru a goroesiad yn benodol, a gwnewch nhw'n archwiliadwy. Mae [un ffynhonnell wirionedd](https://en.wikipedia.org/wiki/Single_source_of_truth) yn atal y methiant clasurol lle mae cyllid, gwerthiant, a gweithrediadau i gyd yn adrodd refeniw gwahanol.

### Mesurwch ansawdd data ar draws dimensiynau

Rheolwch ansawdd ar hyd dimensiynau enwedig: cywirdeb, cyflawnrwydd, cysondeb, amseroldeb, dilysrwydd, ac unigrywiaeth. Offerwch biblinellau â phrofion awtomataidd ac arsylwadwyedd data parhaus (gwiriadau ffresni, cyfaint, llithriad sgema, a dosraniad), fel eich bod yn dal anomaleddau cyn i ddefnyddwyr gael eu heffeithio. Triniwch ddigwyddiadau data fel toriadau cynhyrchu, gyda chanfod, trylennu (triage), dadansoddiad achos gwraidd, a phost-mortemau.

### Dosbarthwch, diogelwch, a rheolwch fynediad

Dosbarthwch ddata yn ôl sensitifrwydd, a chymhwyswch reolaethau'n gymesur: amgryptio, mygydu, tocynneiddio, diogelwch lefel-rhes a lefel-colofn, a mynediad lleiafswm-braint a adolygir yn rheolaidd. Cadwch amserlen cadw a dileu sy'n bodloni gofynion lleihau a chyfraith cadw cofnodion fel ei gilydd. Mewn cyd-destunau llywodraeth, cymodwch rwymedigaethau tryloywder â diogelwch preifatrwydd yn fwriadol, yn hytrach nag achos wrth achos.

## Cyfaddawdau: manteision ac anfanteision

| Dull | Manteision | Anfanteision | Ffit gorau |
|---|---|---|---|
| Tîm llywodraethu canoledig | Safonau cyson, atebolrwydd clir | Tagfa, datgysylltiedig o barthau | Sefydliadau bach neu reoledig iawn |
| Llywodraethu ffederal | Yn graddio, arbenigedd parth, perchnogaeth | Angen offer a diwylliant cryf | Mentrau mawr aml-barth |
| Warws data | SQL aeddfed, llywodraethedig, perfformiol | Anhyblyg, drud ar gyfer data anstrwythuredig | Llwythi gwaith trwm ar BI, sefydlog |
| Llyn-warws data | Hyblyg, unedig, yn trin pob math o ddata | Offer iau, ymdrech llywodraethu | Dadansoddeg gymysg a ML |
| Gwe ddata | Perchnogaeth parth, yn graddio'n sefydliadol | Bar aeddfedrwydd uchel, cost cydgysylltu | Sefydliadau mawr iawn, datganoledig |

Mae llywodraethu bob amser yn cyfnewid cyflymder am ymddiriedaeth. Mae llywodraethu ysgafn yn gadael i dimau symud yn gyflym, hyd nes bod archwiliad, toriad, neu gamadroddiad chwithig yn gorfodi cyfrifiad drud. Mae llywodraethu trwm yn diogelu ymddiriedaeth ond gall fygu arbrofi a gwthio timau tuag at systemau cysgodol. Yr ateb parhaol yw amgodio llywodraethu fel cynwal (guardrails) awtomataidd, hunanwasanaeth, fel bod y llwybr cydymffurfiol hefyd yn llwybr hawdd. Yn bensaernïol, mae warysau'n ffafrio symlrwydd llywodraethedig, mae gwe'n ffafrio graddfa sefydliadol, ac mae llynnoedd-warws yn hollti'r gwahaniaeth. Mae'r dewis cywir yn dilyn strwythur eich sefydliad yn llawer mwy nag unrhyw feincnod technegol.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Pa bensaernïaeth ddata (warws, llyn-warws, neu we) sy'n wir yn ffitio sut mae eich sefydliad wedi'i strwythuro, ac a ydych yn onest ynghylch y bar aeddfedrwydd y mae pob un yn ei fynnu?** Mae'r tabl cyfaddawdau'n gwneud y pwynt bod y dewis hwn yn dilyn strwythur sefydliadol, nid meincnodau: mae warws yn gwobrwyo llwythi gwaith trwm ar BI, sefydlog, mae llyn-warws yn trin dadansoddeg gymysg a ML, ac mae gwe'n graddio ar draws llawer o barthau ymreolaethol ond yn mynnu aeddfedrwydd uchel ac offer cryf. I fenter fawr neu asiantaeth lywodraeth gyda dwsinau o barthau, mae neidio i we cyn bod gennych blatfformau hunanwasanaeth a diwylliant llywodraethu'n cynhyrchu anhrefn wedi'i wisgo fel datganoliad. Dewch â signalau pendant: faint o barthau sy'n cynhyrchu data, a yw timau canolog eisoes yn dagfa, ac a oes gan dimau parth y sgil a'r cymhelliant i fod yn berchen ar gynhyrchion. Os nad oes gennych offer ffederal heddiw, gall yr ateb gonest fod yn warws neu lyn-warws llywodraethedig nawr a gwe'n ddiweddarach. Dewiswch y model y gall eich pobl ei weithredu mewn gwirionedd, yna buddsoddwch yn yr aeddfedrwydd sydd ei angen ar gyfer y model nesaf.

2. **A allwch chi anrhydeddu cais dileu o'r dechrau i'r diwedd heddiw, ac a yw eich llinach yn profi ble aeth pob copi o gofnod personol?** O dan GDPR a chyfundrefnau tebyg, mae cais dileu neu fynediad gwrthrych data'n rwymedigaeth gyfreithiol gyda therfynau amser caled, ac mae copïo data'n eang heb linach yn ei gwneud yn amhosibl ei fodloni. Mae timau mawr yn rheolaidd yn gwasgaru data i mewn i farchnadoedd, dyfyniadau, storfeydd cudd, a thaenlenni, felly'r cwestiwn gwirioneddol yw a allwch chi olrhain a chyrraedd pob copi, nid a allwch chi ddileu'r gwreiddiol. Dewch â thystiolaeth: dewiswch un cwsmer neu ddinesydd go iawn a cheisiwch restru pob man y mae eu data'n byw. Os na allwch, mae'r bwlch hwnnw'n risg cydymffurfiaeth ac yn broblem radiws ffrwydrad toriad fel ei gilydd. Dylai'r ateb yrru buddsoddiad mewn llinach awtomataidd a rheolaethau tynnach ar gopïo digyfyngiad, oherwydd mae'n rhaid adeiladu'r llwybr cydymffurfiol cyn i'r cais gyrraedd.

3. **A yw eich llywodraethu'n llwybr hawdd neu'n glwyd y mae pobl yn mynd o'i gwmpas, a ble mae'r systemau cysgodol sy'n profi hynny?** Ateb parhaol y bennod yw amgodio llywodraethu fel cynwal awtomataidd, hunanwasanaeth fel bod y llwybr cydymffurfiol hefyd yn llwybr cyflymaf, oherwydd mae llywodraethu â llaw trwm yn gwthio timau tuag at daenlenni cysgodol a chopïau anllywodraethedig. I fentrau ac asiantaethau, dyma lle mae toriadau, rhifau anghywir, ac archwiliadau wedi methu'n cael eu geni, yn union oherwydd nad oes neb yn eu gwylio. Dewch ag arolwg pendant: pa dimau sy'n cadw eu copïau eu hunain, pa adroddiadau sy'n osgoi'r catalog, a ble mae pobl yn dweud bod y broses swyddogol yn rhy araf. Mae pob system gysgodol yn arwydd bod y llwybr llywodraethedig yn costio mwy na'r ffordd o'i gwmpas. Trwsiwch y ffrithiant yn hytrach na chyhoeddi polisi arall, fel bod defnyddio data ardystiedig a chontractau'n wirioneddol haws na mynd o'u cwmpas.

4. **Pa endid busnes critigol sydd angen ffynhonnell awdurdodol sengl fwyaf, a phwy yn ôl enw sy'n atebol am ei gofnod aur heddiw?** Mae rheoli data meistr yn bodoli i atal cyllid, gwerthiant, a gweithrediadau rhag adrodd cwsmer gwahanol neu ffigwr refeniw gwahanol yr un, ac ar raddfa fawr mae absenoldeb un ffynhonnell awdurdodol yn troi pob rhif traws-barth yn ddadl. Yr ystyriaethau cystadleuol yw pa mor awdurdodol y mae'n rhaid i'r hyb fod (cofrestrfa, cyfnerthiad, cydfodolaeth, neu wedi'i ganoli'n llawn) a faint o resymeg paru a goroesiad rydych chi'n barod i'w hadeiladu a'i harchwilio, gan fod hyb trymach yn costio mwy ond yn datrys mwy o wrthdaro. Dewch â'r endidau sy'n ymddangos yn y rhan fwyaf o adroddiadau (cwsmer, dinesydd, cynnyrch, cyflenwr, gweithiwr), cyfrif o sawl system sy'n honni dal y cofnod gwirioneddol ar gyfer pob un, a'r rheolau paru rydych yn eu defnyddio heddiw, os o gwbl. I fanc neu asiantaeth genedlaethol, enwch y perchennog atebol a'r rheolau goroesiad yn benodol, oherwydd bydd rheoleiddiwr sy'n olrhain ffigwr o adroddiad cyhoeddus yn ôl i'r ffynhonnell yn gofyn pwy benderfynodd pa ddyblyg a enillodd, ac nid yw "neb" yn ateb sy'n goroesi archwiliad.

5. **Sut ydych chi'n gwybod bod set ddata critigol yn addas i'w defnyddio cyn i ddefnyddiwr ddarganfod ei bod wedi torri?** Mewn ystadau anaeddfed, mae ansawdd yn cael ei ddarganfod gan y dadansoddwr y mae ei ddangosfwrdd yn torri neu'r swyddog gweithredol y mae ei rif bwrdd yn anghywir, sef y pwynt canfod mwyaf costus posibl. Mae'r tyndra rhwng cost offeru ansawdd (profion, gwiriadau ffresni a chyfaint, monitro dosraniad a llithriad sgema ar draws dimensiynau enwedig fel cywirdeb, cyflawnrwydd, a dilysrwydd) a chost y digwyddiadau rydych yn eu hatal, ac mae timau'n rheolaidd yn tan-fuddsoddi oherwydd mae'r methiannau'n aros yn anweledig nes eu bod yn troi'n drychinebus. Dewch â'r tri digwyddiad data diwethaf, sut y cawsant eu canfod, a pha mor hir y buont yn rhedeg cyn i unrhyw un sylwi, ynghyd â'r SLAs ansawdd rydych chi'n eu cyhoeddi ac yn rhybuddio arnynt mewn gwirionedd heddiw. Ar gyfer adrodd menter a llywodraeth, cysylltwch bob cynnyrch data critigol â throthwyon ansawdd penodol a thriniwch doriad fel toriad cynhyrchu gyda thrylennu a post-mortem, oherwydd mae ffigwr anghywir mewn ffeilio rheoleiddiol neu ystadegyn cyhoeddus yn cario cost gyfreithiol ac enw da sy'n gorbwyso'r bil monitro o bell ffordd.

6. **A yw eich llywodraethu'n wirioneddol ffederal gyda pherchnogaeth parth, neu'n dîm canolog sy'n cael ei ddal yn atebol am ddata nad yw'n ei ddeall?** Mae'r bennod yn dadlau bod perchnogaeth ffederal gyda galluogi canolog yn graddio lle mae canoli pur yn tagu a datganoli pur yn disgyn i anhrefn, ac eto mae llawer o sefydliadau'n honni ffederaliaeth tra bod tîm canolog bach yn parhau'n atebol yn enwol am filoedd o dablau nad oes ganddo unrhyw wybodaeth barth ohonynt. Mae'r pwysau cystadleuol yn real: mae timau canolog yn rhoi cysondeb ac un gwddf i'w wasgu, tra bod perchnogaeth parth yn rhoi arbenigedd ac atebolrwydd ond yn mynnu bod perchnogion busnes yn derbyn cyfrifoldeb nad ydynt efallai ei eisiau. Dewch â map gonest o bwy sy'n atebol yn erbyn pwy sydd mewn gwirionedd yn cynnal diffiniadau ac yn datrys materion ansawdd ar gyfer eich prif barthau, ac a oes gan stiwardiaid yr awdurdod a'r amser sydd angen y rôl. Mewn menter neu asiantaeth fawr, gwiriwch fod perchnogaeth yn gorwedd gyda phobl sydd â gwybodaeth parth a'r mandad i ddweud na, oherwydd mae llywodraethu wedi'i neilltuo i dîm canolog heb awdurdod yn cynhyrchu polisïau nad oes neb yn eu dilyn a chyngor nad yw'n setlo dim.

## Trwy lens sector

**Cwmni newydd.** Mae cyflymder a goroesiad yn curo proses. Enwch un perchennog ar gyfer pob set ddata graidd a gwnewch un storfa'n ffynhonnell wirionedd sengl ar gyfer endidau fel "cwsmer gweithredol," a hepgorwch gatalogau, cynghorau, a gwe'n gyfan gwbl. Mae contract un dudalen ar gyfer eich llond llaw o dablau critigol (sgema, amser adnewyddu, un disgwyliad ansawdd) yn dod â'r ddadl "pwy rif sy'n iawn" i ben mewn prynhawn. Dibynnwch ar y llywodraethu sydd eisoes wedi'i adeiladu i mewn i'ch warws yn hytrach na staffio swyddogaeth na allwch ei fforddio.

**Busnes bach.** Heb arbenigwr data pwrpasol a chyllideb dynn, triniwch lywodraethu fel hylendid data yn hytrach na phrosiect platfform: gwybyddwch pa ddata personol sydd gennych, ble mae'n byw, a phwy sy'n cael cyffwrdd ag ef. Ffafriwch warws neu declyn BI reoledig sy'n darparu llinach, rheolaeth mynediad, a chadw yn barod, fel eich bod yn prynu llywodraethu wedi'i fewnadeiladu mewn teclynnau rydych eisoes yn eu rhedeg yn lle ei adeiladu. Cadwch unrhyw biblinell bwrpasol ar gyfer yr un set ddata sy'n wirioneddol yrru'r busnes.

**Menter.** Ar raddfa fawr ar draws llawer o dimau, y gwaith yw perchnogaeth ffederal gyda galluogi canolog: catalog a rennir gyda llinach awtomataidd, contractau data gorfodedig, data meistr ar gyfer endidau craidd, a SLAs ansawdd wedi'u mesur yn erbyn llinellau sylfaen. Amgodiwch lywodraethu fel cynwal hunanwasanaeth fel bod y llwybr cydymffurfiol hefyd yn llwybr cyflym, a rheolwch ddata fel portffolio o gynhyrchion gyda pherchnogion enwedig. Fel hyn gall archwilwyr olrhain unrhyw ffigwr o adroddiad yn ôl i ffynhonnell, ac mae grwpiau'n peidio ag ailddyfeisio'r un piblinellau a diffiniadau.

**Llywodraeth.** Mae rheolau caffael, tryloywder, ac atebolrwydd cyhoeddus yn llunio pob dewis. Triniwch ddangosyddion cyhoeddedig fel cynhyrchion data gyda methodoleg ddogfennedig, rhyddhadau wedi'u fersiynu, a giatiau ansawdd, a chymodwch rwymedigaethau rhyddid gwybodaeth a data agored â phreifatrwydd a lleihau'n fwriadol yn hytrach nag achos wrth achos. Mynnwch gludadwyedd data a datgeliad llinach mewn contractau gwerthwyr i osgoi clymu i werthwr, cadwch amserlen cadw a dileu amddiffynadwy, a gadewch i gyngor stiwardiaeth ddal diffiniadau a rennir fel bod "cartref" neu "ddiweithdra" yn golygu'r un peth ar draws pob adran.

## Enghreifftiau

**Cwmni newydd.** Darganfu cwmni SaaS cam-hedyn fod ei daenlen filio, ei declyn gwerthiant, a'i gronfa ddata cynnyrch i gyd yn adrodd cyfrif cwsmeriaid gwahanol, ac ni allai neb ddweud pa un oedd yn gywir ar gyfer y diweddariad buddsoddwyr. Enwodd y tîm pedwar person un perchennog ar gyfer pob set ddata graidd, gwneud y warws yn ffynhonnell sengl ar gyfer "cwsmer gweithredol," ac ysgrifennu contract un dudalen yn disgrifio'r sgema a'r amser adnewyddu dyddiol. Cymerodd brynhawn, a daeth â'r ddadl wythnosol dros ba rif i'w ymddiried iddo ben.

**Menter.** Cyfunodd banc rhyngwladol ddwsinau o gofnodion cwsmeriaid gwrthdrawiadol ar draws ei adrannau manwerthu, benthyca, a chyfoeth yn hyb rheoli data meistr gyda rheolau goroesiad a chofnod aur. Cyhoeddodd pob parth gynhyrchion data gyda chontractau a SLAs ffresni, wedi'u dangos mewn catalog canolog gyda llinach. Gostyngodd amser adrodd rheoleiddiol yn sylweddol, oherwydd gallai archwilwyr bellach olrhain unrhyw ffigwr o adroddiad i ffynhonnell. Ymddeolodd y banc hefyd sawl platfform adrodd dyblyg.

**Llywodraeth.** Mae asiantaeth ystadegau genedlaethol yn trin ei dangosyddion cyhoeddedig fel cynhyrchion data, gyda methodoleg ddogfennedig, rhyddhadau wedi'u fersiynu, a giatiau ansawdd llym. Mae cyngor stiwardiaeth yn cymodi diffiniadau ar draws adrannau, fel bod "diweithdra" neu "cartref" yn golygu'r un peth ym mhobman. Mae dosbarthiad a mynediad rheoledig yn diogelu cyfrinachedd ymatebwyr, tra bod catalog cyhoeddus yn cefnogi rhwymedigaethau tryloywder a rhyddid gwybodaeth.

## Achos busnes: cymhellion, ROI, a TCO

Mae'r cymhelliant dros lywodraethu data'n lleihad risg a chreu gwerth mewn mesur bras gyfartal. Ar ochr y risg, mae costau a osgowyd yn cynnwys dirwyon rheoleiddiol, atebolrwydd toriad, archwiliadau wedi methu, a'r niwed i enw da o gyhoeddi rhifau anghywir. Ar ochr y gwerth, mae data dibynadwy, darganfyddadwy'n cyflymu pob ymdrech dadansoddeg a dysgu peiriant i lawr yr afon, yn lleihau piblinellau dyblyg, ac yn byrhau'r amser o gwestiwn i ateb.

Mae cost mabwysiadu'n real: offer catalog ac ansawdd, amser stiward a pherchennog, a'r newid sefydliadol i wneud i berchnogaeth lynu. Pwyswch TCO (cyfanswm cost perchnogaeth) yn erbyn cost peidio â mabwysiadu, sydd fel arfer yn fwy, dim ond wedi'i guddio. Heb ei fesur, mae'r gost honno'n ymddangos fel dadansoddwyr yn treulio'r rhan fwyaf o'u hamser yn dod o hyd i ddata a'i lanhau, timau'n ailadeiladu'r un piblinellau, a swyddogion gweithredol yn gwneud penderfyniadau ar ffigurau na all neb eu hamddiffyn. Gwnewch yr achos i arweinyddiaeth yn eu hiaith nhw: mae llywodraethu'n troi data o rwymedigaeth gyda risg ddiderfyn yn ased gydag enillion cyfansawdd, ac mae'n rhagofyniad ar gyfer AI dibynadwy. Dechreuwch lle mae'r boen a'r amlygiad rheoleiddiol ar eu huchaf, fel y gallwch ddangos gwerth yn gyflym.

## Gwrth-batrymau a pheryglon

- Llywodraethu gan bwyllgor heb awtomeiddio, gan gynhyrchu polisïau nad oes neb yn eu dilyn.
- Catalogio popeth ar unwaith yn lle'r setiau data sy'n wirioneddol bwysig.
- Prosiectau data meistr sy'n ceisio gwneud gormod ar unwaith ac na fyddant byth yn cyflenwi cofnod aur.
- Trin [ansawdd data](https://en.wikipedia.org/wiki/Data_quality) fel glanhau untro yn hytrach nag arsylwadwyedd parhaus.
- Perchnogaeth wedi'i neilltuo i dîm canolog sy'n brin o wybodaeth barth neu awdurdod.
- Contractau wedi'u dogfennu mewn wicis ond heb eu gorfodi mewn piblinellau.
- Copïo data'n eang heb linach, gan wneud ceisiadau dileu'n amhosibl eu hanrhydeddu.
- Prynu teclyn a'i alw'n strategaeth; mae offer heb fodel gweithredu'n methu.

## Model aeddfedrwydd

1. Cychwyn: Mae data heb ei ddogfennu ac heb berchennog, yn cael ei drin ad hoc ac yn adweithiol. Mae diffiniadau'n gwrthdaro ar draws timau. Darganfyddir ansawdd gan ddefnyddwyr pan fydd adroddiadau'n torri. Nid oes catalog na llinach yn bodoli.
2. Datblygu: Mae arferion sylfaenol yn ymddangos ond yn anghyson ar draws timau. Mae gan rai setiau data berchnogion a dogfennaeth, ac mae catalog rhannol yn bodoli. Mae gwiriadau ansawdd â llaw ac yn adweithiol. Mae polisi llywodraethu wedi'i ysgrifennu ond yn cael ei orfodi'n wan ac yn anghyson.
3. Safoni: Mae perchnogaeth, contractau, a SLAs wedi'u dogfennu a'u gorfodi ledled y sefydliad. Mae gan gynhyrchion data critigol berchnogion enwedig; mae catalog gyda llinach awtomataidd yn cwmpasu prif barthau; mae data meistr yn bodoli ar gyfer endidau craidd; mae llywodraethu'n ffederal gyda galluogi canolog ac yn cael ei gymhwyso'n gyson yn hytrach na fesul tîm.
4. Rheoli: Mae'r ystad yn cael ei mesur a'i rheoli yn erbyn llinellau sylfaen. Olrheinir dimensiynau ansawdd (cywirdeb, cyflawnrwydd, amseroldeb, dilysrwydd, unigrywiaeth) yn erbyn targedau SLA cyhoeddedig; adroddir cyfraddau toriad contract, sylw llinach a chatalog, ffresni, ac amser-i-anrhydeddu cais dileu ar ddangosfyrddau; mae arsylwadwyedd yn rhybuddio ar lithriad sgema ac anomaleddau cyfaint; mae digwyddiadau'n cael trylennu, dadansoddiad achos gwraidd, a phost-mortemau; mae penderfyniadau mynediad a mynd/peidio â mynd yn seiliedig ar fetrigau yn erbyn llinellau sylfaen, nid barn.
5. Trefniannu: Caiff llywodraethu ei wella'n barhaus a'i integreiddio ar draws y sefydliad. Data-fel-cynnyrch yw'r norm ar draws parthau; gorfodir contractau'n awtomatig ac mae newidiadau torfol yn methu'n gyflym; mae cynwal hunanwasanaeth yn amgodio polisi; mae ansawdd a llinach yn bwydo rheoli risg rhagweithiol; ymddiriedir yn ddiffiniadau ledled y fenter ac maent yn cefnogi adrodd rheoledig ac AI. Mae'r sefydliad yn rheolaidd yn ail-gydbwyso perchnogaeth, yn ymddeol platfformau dyblyg, ac yn addasu llywodraethu wrth i'r busnes a rheoleiddio symud.

## Syniadau i'w trafod

- Pa un o'ch endidau busnes sydd angen ffynhonnell wirionedd sengl fwyaf ar frys, a pham mae'n ddarniog heddiw?
- Ble byddai contractau data gorfodedig wedi atal digwyddiad diweddar?
- A yw eich sefydliad wedi'i strwythuro ar gyfer perchnogaeth ffederal, neu a fyddai canoli'n ffitio'n well ar hyn o bryd?
- Sut rydych chi'n cymodi rhwymedigaethau tryloywder llywodraeth â phreifatrwydd a lleihau?
- Pa ganran o amser eich dadansoddwyr a dreulir yn dod o hyd i ddata a'i lanhau, a beth fyddai gwerth ei haneru?
- Pwy sy'n atebol, yn ôl enw, am eich set ddata bwysicaf, ac a ydynt yn gwybod hynny?

## Prif ganfyddiadau

- Triniwch ddata fel cynnyrch gyda pherchnogion, contractau, a SLAs, nid fel gwastraff cymhwysiad.
- Mae llywodraethu ffederal gyda galluogi canolog yn graddio'n well na chanoli pur.
- Mae catalog gyda llinach awtomataidd yn ddrws ffrynt i ystad ddata ddibynadwy.
- Sefydlwch ffynhonnell wirionedd sengl ar gyfer endidau craidd trwy reoli data meistr.
- Rheolwch ansawdd yn barhaus ar draws dimensiynau enwedig gydag arsylwadwyedd ac ymateb i ddigwyddiadau.
- Amgodiwch lywodraethu fel cynwal awtomataidd fel bod y llwybr cydymffurfiol yn llwybr hawdd.
- Dewiswch warws, llyn-warws, neu we i ffitio'ch sefydliad, nid y cyffro.

## Cyfeiriadau a darllen pellach

- DAMA International, "DAMA-DMBOK: Data Management Body of Knowledge."
- Zhamak Dehghani, "Data Mesh: Delivering Data-Driven Value at Scale."
- Ralph Kimball and Margy Ross, "The Data Warehouse Toolkit."
- Piethein Strengholt, "Data Management at Scale."
- David Loshin, "Master Data Management."
- Chad Sanderson a chydweithwyr, ysgrifau ar gontractau data.
- ISO/IEC 38505, "Governance of data."
- ISO 8000, "Data quality" standard series.
