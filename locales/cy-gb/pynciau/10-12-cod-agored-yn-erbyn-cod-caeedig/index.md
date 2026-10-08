# 10.12 Cod agored yn erbyn cod caeedig

## Trosolwg a chymhelliant

Mae bron pob system fodern yn gyfuniad o feddalwedd a ysgrifennoch chi, meddalwedd a brynoch chi, a meddalwedd a gymeroch chi am ddim. Mae dau o'r tri hynny'n dod gyda dewis sylfaenol: a yw'r feddalwedd yn **god agored** neu'n **god caeedig**? Caiff **[meddalwedd cod agored](https://en.wikipedia.org/wiki/Open-source_software) (OSS)** ei ddosbarthu o dan drwydded sy'n rhoi'r hawl i bawb ddefnyddio, astudio, addasu, ac ailddosbarthu'r cod ffynhonnell, y cyfarwyddiadau darllenadwy-i-ddynion sy'n diffinio'r rhaglen. Caiff **meddalwedd cod caeedig**, a elwir hefyd yn **[feddalwedd berchnogol](https://en.wikipedia.org/wiki/Proprietary_software)**, ei ddosbarthu fel cynnyrch gorffenedig y mae ei god ffynhonnell yn cael ei gadw'n breifat gan y gwerthwr. Rydych yn cael yr hawl i'w redeg o dan drwydded, ond nid i archwilio na newid sut mae'n gweithio. Mae categori canol, **[meddalwedd cod-ar-gael](https://en.wikipedia.org/wiki/Source-available_software)**, yn cyhoeddi'r ffynhonnell i'w darllen ond yn cyfyngu defnydd, addasu, neu ailddosbarthu. Mae'n *weladwy* ond nid yn *agored* yn ôl y diffiniad safonol.

Mae dau eglurhad yn bwysig cyn i chi eu cymharu. Yn gyntaf, mae "am ddim" yn amwys. Mae'r gymuned yn gwahaniaethu **rhydd-fel-mewn-rhyddid** (y ryddid i addasu a rhannu, weithiau'n cael ei ysgrifennu "libre") o **rhad-fel-mewn-pris** (dim cost, "gratis"). Mae cod agored yn ymwneud â rhyddid, nid o reidrwydd pris. Yn ail, mae trwyddedau cod agored yn rhannu'n ddwy deulu. Mae **[trwyddedau caniataol](https://en.wikipedia.org/wiki/Permissive_software_license)** (fel [MIT](https://en.wikipedia.org/wiki/MIT_License), BSD, ac Apache 2.0) yn gadael i chi wneud bron unrhyw beth, gan gynnwys mewnblannu'r cod mewn cynnyrch caeedig. Mae **trwyddedau [copyleft](https://en.wikipedia.org/wiki/Copyleft)** (fel [Trwydded Gyhoeddus Gyffredinol GNU](https://en.wikipedia.org/wiki/GNU_General_Public_License), GPL) yn mynnu bod gweithiau deilliadol a ddosberthwch chithau hefyd yn cael eu rhyddhau o dan yr un telerau agored, rheol ddwyochredd a elwir weithiau'n "firaol" gan feirniaid ac yn "share-alike" gan gefnogwyr.

Mae'r bennod hon yn edrych ar y dewis o ddwy ochr. Fel **defnyddiwr**, rydych yn penderfynu a ddylid mabwysiadu cydran cod agored neu berchnogol. Fel **cynhyrchwr**, rydych yn penderfynu a ddylid cod-agor meddalwedd a adeiladoch chi. I fentrau mawr, ac yn enwedig llywodraeth, mae gan y ddau benderfyniad bwysau sydd ymhell y tu hwnt i'r ffeil drwydded. Maent yn cyffwrdd â chaffael (pennod 10.3), sofraniaeth ddigidol (pennod 10.11), diogelwch cadwyn gyflenwi (pennod 4.2), rhyngweithredoldeb (pennod 3.8), a chyfrifiad adeiladu-neu-brynu (pennod 6.1).

## Egwyddorion allweddol

- **Trwydded, nid pris, sy'n diffinio "agored".** Darllenwch y drwydded; mae di-dâl a chod agored yn honiadau gwahanol.
- **Nid yw'r naill fodel na'r llall yn ddiogelach yn gynhenid.** Gall y ddau fod yn ardderchog neu'n esgeulus; mae'r arferion o gwmpas y cod yn bwysicach na'i agoredrwydd.
- **Mae agoredrwydd yn lifer lleihau-dibyniaeth.** Mynediad i ffynhonnell yw'r amddiffyniad eithaf yn erbyn [clymu i werthwr](https://en.wikipedia.org/wiki/Vendor_lock-in).
- **Rydych chi bob amser yn berchen ar y baich gweithredol.** Nid yw caffael am ddim byth yn rhedeg am ddim; mae [cyfanswm cost berchnogaeth](https://en.wikipedia.org/wiki/Total_cost_of_ownership) yn dweud y stori wirioneddol.
- **Mae gwahaniaethwyr yn aros ynghau; gall nwyddau agor.** Cod-agorwch yr hyn nad yw'n eich gwahaniaethu; gwarchodwch yr hyn sydd.
- **Mae gan copyleft ganlyniadau.** Deallwch rwymedigaethau dwyochredd cyn i chi fewnblannu cod copyleft mewn cynnyrch a ddosberthwch.
- **Mae cymuned fyw'n ased; mae ystorfa wedi'i gadael yn rwymedigaeth.** Barnwch y prosiect, nid dim ond y drwydded.

## Argymhellion

### Gwerthuswch gydran ar sail y prosiect, nid dim ond y drwydded

Cyn i chi fabwysiadu unrhyw ddibyniaeth, cod agored neu berchnogol, aseswch ei iechyd: cyflymder rhyddhau, nifer ac amrywiaeth cynhalwyr, ymatebolrwydd i adroddiadau diogelwch, a lled mabwysiadu. Mae gan lyfrgell god-agored un-cynhaliwr a gwerthwr perchnogol bach yr un **risg ffactor-bws** (y perygl y bydd prosiect yn cwympo os yw un neu ychydig o bobl allweddol yn gadael). Ffafriwch gydrannau â sylfaen cyfrannwr eang neu werthwr cadarn yn ariannol, a chofnodwch yr asesiad fel rhan o ddiwydrwydd dyladwy (penodau 10.2, 4.2).

### Darllenwch ac olrheiniwch drwyddedau fel rhwymedigaeth dosbarth cyntaf

Cynhaliwch restr o bob cydran a'i drwydded, a gorfodwch bolisi ar ba deuluoedd trwydded sy'n dderbyniol ar gyfer pa ddefnyddiau. Y gwahaniaeth allweddol yw copyleft. Gellir mewnblannu cod **caniataol** (MIT, Apache 2.0) yn gyffredinol mewn cynhyrchion caeedig yn rhydd. Gall copyleft **cryf** (GPL) eich rhwymo i ryddhau eich gwaith deilliadol dosbarthedig eich hun o dan yr un telerau. Defnyddiwch **ddadansoddiad cyfansoddiad meddalwedd (SCA)** awtomataidd, offer sy'n sganio eich dibyniaethau i adnabod cydrannau, trwyddedau, a gwendidau hysbys, a chynhyrchu **bil deunyddiau meddalwedd (SBOM)**, rhestr ffurfiol o bob cydran mewn cynnyrch (penodau 10.3, 4.2).

### Barnwch ddiogelwch yn ôl arfer, nid yn ôl agoredrwydd

Peidiwch â thybio bod cod agored yn ddiogel oherwydd y **ddadl "llawer o lygaid"** ([Cyfraith Linus](https://en.wikipedia.org/wiki/Linus%27s_law): "gyda digon o lygaid, mae pob bỳg yn fas"). A pheidiwch â thybio bod cod perchnogol yn ddiogel drwy **[ddiogelwch-drwy-dywyllwch](https://en.wikipedia.org/wiki/Security_through_obscurity)** (y gred ddiffygiol bod cuddio ffynhonnell yn cuddio diffygion). Dim ond os yw pobl gymwys yn edrych mewn gwirionedd y mae llawer o lygaid yn helpu, ac mae llawer o brosiectau a ddefnyddir yn eang wedi'u cynnal yn deneuaidd. Mae gan y ddau fodel **risg cadwyn gyflenwi**: cod agored drwy ddibyniaethau wedi'u peryglu neu wedi'u gadael, perchnogol drwy god tywyll a sianeli diweddaru na allwch eu harchwilio. Pinnwch fersiynau, dilyswch darddiad, sganiwch yn barhaus, a monitrwch gynghorion diogelwch ni waeth beth fo'r model (pennod 4.2).

### Dyluniwch ar gyfer ymadael a rhyngweithredoldeb

Ffafriwch gydrannau sy'n siarad safonau agored a fformatau data cludadwy, fel y gallwch eu disodli'n ddiweddarach (penodau 3.8, 10.11). Gyda chod agored rydych yn ennill yr ymadael eithaf: os yw prosiect yn arafu, gallwch ei [fforchio](https://en.wikipedia.org/wiki/Fork_(software_development)) (creu a chynnal eich copi eich hun). Gyda meddalwedd berchnogol, negodwch amddiffyniadau ymlaen llaw: allforio data mewn fformatau agored, APIau wedi'u dogfennu, a **[gwarchodfa cod ffynhonnell](https://en.wikipedia.org/wiki/Source_code_escrow)** (trefniant cyfreithiol lle mae'r gwerthwr yn adneuo ffynhonnell gyda thrydydd parti, i'w ryddhau i chi os yw'r gwerthwr yn methu). Dyluniwch fel na all unrhyw un gydran, o'r naill fath na'r llall, ddal eich system yn wystl.

### Pwyswch gyfanswm cost berchnogaeth, nid pris label

Cymharwch ddewisiadau ar sail **cyfanswm cost berchnogaeth (TCO)**, y gost oes lawn gan gynnwys caffael, integreiddio, gweithredu, cymorth, hyfforddiant, uwchraddiadau, ac amnewid o'r diwedd, yn hytrach na ffioedd trwydded yn unig. Mae cod agored yn aml yn cyfnewid cost trwyddedu am gost weithredol a staffio uwch. Mae meddalwedd berchnogol yn aml yn cyfnewid ffioedd tanysgrifiad rhagweladwy am glymu a llai o reolaeth. Cynhwyswch gost y model ei hun: mae cod agored hunan-gefnogi angen sgil mewnol, tra bod meddalwedd berchnogol angen gallu rheoli-gwerthwr.

### Fel cynhyrchwr, cod-agorwch yr hyn nad yw'n eich gwahaniaethu

Dosbarthwch eich meddalwedd eich hun i'r hyn sy'n rhoi mantais gystadleuol neu genhadaeth i chi a'r hyn sy'n bibellau heb ei wahaniaethu. Cadwch y gwahaniaethwyr yn berchnogol. Ystyriwch god-agor y seilwaith nwyddau, lle gall cymuned rannu cynnal a gwella. I lywodraeth, pwyswch **"arian cyhoeddus, cod cyhoeddus"** (yr egwyddor bod meddalwedd a ariennir gan drethdalwyr yn dylai fod ar gael i'r cyhoedd yn ddiofyn) fel gyrrwr tryloywder, ailddefnydd, a sofraniaeth (penodau 10.5, 10.11). Dewiswch y drwydded yn fwriadol: caniataol i uchafu mabwysiadu, copyleft i gadw'r ecosystem yn agored.

## Cyfaddawdau: manteision ac anfanteision

| Dimensiwn | Cod agored | Caeedig / perchnogol |
|---|---|---|
| **Cost caffael** | Fel arfer yn sero i'w gaffael | Ffi drwydded neu danysgrifiad |
| **Cyfanswm cost berchnogaeth** | Mae cost yn symud i weithrediadau a staff | Mwy rhagweladwy, ond premiwm clymu |
| **Rheolaeth a chyfaddasu** | Llawn: gallwch ddarllen a newid y ffynhonnell | Wedi'i gyfyngu i'r hyn mae'r gwerthwr yn ei ddatgelu |
| **Cymorth ac atebolrwydd** | Cymuned, neu drydydd parti taledig; dim un llwnc i'w dagu | Cymorth contractiol a phlaid atebol glir |
| **Ystum diogelwch** | Archwiliadwy; "llawer o lygaid" os wedi'i gynnal mewn gwirionedd | Wedi'i reoli gan werthwr; dywyll; nid yw tywyllwch yn amddiffyniad |
| **Hirhoedledd / esgeulustod** | Gellir ei fforchio os wedi'i gynnal; gall ddal i wywo | Yn dibynnu ar hyfywedd a map ffordd y gwerthwr |
| **Clymu i werthwr** | Isel: mae ffynhonnell a fformatau agored yn galluogi ymadael | Uchel oni bai ei liniaru gan safonau a gwarchodfa |
| **Ecosystem** | Cymuned agored a rhyngweithredoldeb | Wedi'i guradu, wedi'i integreiddio, weithiau â muriau |

Y tensiwn cylchol yw **rheolaeth yn erbyn cyfleustra ac atebolrwydd**. Mae cod agored yn uchafu rheolaeth, archwiliadwyedd, a rhyddid rhag clymu, ond mae'n gofyn i chi gyflenwi'r gallu, yr integreiddio, a'r cymorth eich hun. Mae meddalwedd berchnogol yn cyflenwi cynnyrch cefnogedig, integredig, atebol gyda chontract i'w orfodi, ond mae'n ildio rheolaeth ac yn gwahodd clymu. Anaml y mae'r datrysiad yn oll-neu-ddim. Mae'r rhan fwyaf o ystadau aeddfed yn cymysgu sylfeini cod agored â systemau perchnogol lle mae cymorth, atebolrwydd, neu allu arbenigol yn cyfiawnhau'r fasnach.

## Cwestiynau i'w trafod gyda'ch tîm

1. **A ydym yn gorfodi polisi trwydded gyda SCA a SBOMau awtomataidd yn y biblinell, yn enwedig i ddal copyleft cryf cyn iddo gael ei gyhoeddi?** Gall mewnblannu llyfrgell GPL mewn cynnyrch perchnogol dosbarthedig eich rhwymo i ryddhau eich ffynhonnell eich hun, ac mae'r syndod hwnnw fel arfer yn dod i'r wyneb yn hwyr, pan fydd yn ddrud i'w ddadwneud. Cynhaliwch restr o bob cydran a'i drwydded, gorfodwch ba deuluoedd trwydded sy'n dderbyniol ar gyfer pa ddefnyddiau, a rhedwch ddadansoddiad cyfansoddiad meddalwedd yn awtomatig fel bod y biblinell yn rhwystro toriadau yn hytrach na chyfreithiwr yn eu dal ar adeg cyhoeddi. Cynhyrchwch SBOM fel mater o drefn. I ystâd fawr neu lywodraethol, mae hyn hefyd yn hylendid cadwyn gyflenwi ac yn aml yn ofyniad caffael. Dewch â'ch rhestr drwydded bresennol, neu'r ffaith nad oes gennych un, a phenderfynwch pwy sy'n berchen ar y polisi.

2. **Pan fyddwn yn mabwysiadu dibyniaeth, a ydym yn asesu iechyd prosiect a ffactor-bws fel diwydrwydd dyladwy?** Mae gan lyfrgell god-agored un-cynhaliwr a gwerthwr perchnogol bach yr un risg: mae'r prosiect yn cwympo os yw un neu ychydig o bobl allweddol yn gadael. Cyn i chi fabwysiadu unrhyw beth, aseswch gyflymder rhyddhau, nifer ac amrywiaeth cynhalwyr, ymatebolrwydd i adroddiadau diogelwch, a lled mabwysiadu, a chofnodwch yr asesiad. Nid yw'r naill fodel na'r llall yn ddiogelach yn ddiofyn; dim ond os yw pobl gymwys yn edrych mewn gwirionedd y mae "llawer o lygaid" yn helpu, ac mae llawer o brosiectau a ddefnyddir yn eang wedi'u cynnal yn deneuaidd. Dewch â'r tri neu bedwar dibyniaeth y mae eich cynnyrch yn dibynnu arnynt fwyaf a gofynnwch, ar gyfer pob un, sawl person fyddai'n rhaid iddo gerdded i ffwrdd cyn iddo ddod yn broblem i chi. Os na allwch ateb, dyna'r asesiad rydych yn ei ddyled i chi'ch hun.

3. **Pan fyddwn yn prynu perchnogol, a ydym yn sicrhau amddiffyniadau ymadael ymlaen llaw?** Mae meddalwedd berchnogol yn cynnig atebolrwydd a chyfleustra yn gyfnewid am reolaeth, a'r gost gudd yw clymu: costau newid sy'n gadael i werthwr godi prisiau neu ddirywio gwasanaeth heb fawr o ddatrysiad. Negodwch yr amddiffyniadau cyn i chi lofnodi, pan fydd gennych o hyd drosoledd: allforio data mewn fformatau agored, APIau wedi'u dogfennu, a gwarchodfa cod ffynhonnell sy'n rhyddhau'r ffynhonnell os yw'r gwerthwr yn methu. Gyda chod agored, eich ymadael yw'r gallu i fforchio; gyda pherchnogol rhaid i chi ysgrifennu'r ymadael i mewn i'r contract. Dewch â'ch systemau perchnogol mwyaf hollbwysig a gofynnwch beth sy'n digwydd mewn gwirionedd os yw'r gwerthwr yn dyblu'r pris neu'n mynd i'r wal. Os yw'r ateb yn "rydym yn sownd," trwsiwch y contract wrth adnewyddu.

4. **Ar gyfer y feddalwedd rydym yn ei hadeiladu ein hunain, sut ydym yn penderfynu beth i god-agor a beth i'w gadw ynghau, a phwy sy'n dal awdurdod i wneud y penderfyniad hwnnw?** Cael hyn yn anghywir mewn un cyfeiriad ac rydych yn rhoi i ffwrdd yr union god sy'n eich gwahaniaethu; ei gael yn anghywir yn y llall ac rydych yn pentyrru pibellau nwyddau y byddai cymuned yn falch o rannu eu cynnal. Mae'r pwysau cystadleuol yn real: mae peirianwyr eisiau'r ochr recriwtio ac enw da o ystorfa gyhoeddus, tra bod cynnyrch a chyfreithiol yn poeni am roi mantais i wrthwynebwyr neu ddatgelu heuristig sensitif-diogelwch. Dewch â dosbarthiad gonest o'ch systemau i seilwaith gwahaniaethol-cenhadaeth yn erbyn seilwaith heb ei wahaniaethu, ac enwch y person neu'r bwrdd sy'n llofnodi rhyddhad, oherwydd mai penderfyniad ad hoc a wneir gan bwy bynnag a wthiodd yr ystorfa yw sut mae gemau'r goron yn gollwng. I fenter fawr mae'r cwestiwn yn strategaeth portffolio, ac i lywodraeth mae'n gwrthdaro â "arian cyhoeddus, cod cyhoeddus," yr egwyddor y dylai meddalwedd a ariennir gan drethdalwyr fod yn gyhoeddus yn ddiofyn, felly penderfynwch ymlaen llaw pa esemptiadau (diogelwch cenedlaethol, canfod twyll, data personol) sy'n cyfiawnhau cadw cod ynghau.

5. **A yw ein cymariaethau adeiladu-neu-brynu'n dal cyfanswm cost berchnogaeth llawn, neu a ydym yn dal i drin ffi drwydded sero fel cost sero?** Y camgymeriad ariannol mwyaf cyffredin gyda chod agored yw darllen "am ddim i'w gaffael" fel "am ddim i'w redeg," yna darganfod bod integreiddio, gweithrediadau, ymateb diogelwch, a chymorth taledig yn crebachu unrhyw drwydded a osgowyd. Y tensiwn yw bod tanysgrifiad perchnogol yn edrych yn ddrud ar yr anfoneb tra'n cuddio premiwm clymu, ac mae cydran agored yn edrych yn rhad ac am ddim ar yr anfoneb tra'n symud cost i'ch staff eich hun. Dewch â model TCO tebyg-i-debyg ar gyfer dau neu dri phenderfyniad real: caffael, integreiddio, gweithrediad, cymorth, hyfforddiant, uwchraddiadau, ymateb diogelwch, ac amnewid o'r diwedd, wedi'i brisio dros yr oes lawn yn hytrach na'r flwyddyn gyntaf. Mewn ystâd menter neu lywodraeth, ychwanegwch gost y model gweithredu ei hun, gan fod cod agored hunan-gefnogi'n mynnu sgil mewnol y mae'n rhaid i chi ei recriwtio a'i gadw, a thrinwch gymhariaeth sy'n hepgor y llinellau hynny fel tystiolaeth, nid dadansoddiad.

6. **A ydym yn barnu diogelwch cydran yn ôl ei harferion, neu a ydym yn dibynnu ar y label agoredrwydd, boed "llawer o lygaid" neu gyfrinachedd cod caeedig?** Mae'r ddau ragosodiad yn faglau: dim ond pan fydd pobl gymwys yn adolygu'r cod mewn gwirionedd y mae "llawer o lygaid" yn eich amddiffyn, ac mae llawer o brosiectau agored a ddefnyddir yn eang yn rhedeg ar un cynhaliwr wedi ymlâdd, tra bod cod caeedig sy'n dibynnu ar ymosodwyr heb ei weld yn ddiogelwch drwy dywyllwch, nid rheolaeth. Mae'r ddadl yn bwysig oherwydd ei bod yn newid ble rydych yn gwario ymdrech diogelwch prin, a'r ateb gonest yw bod gan y ddau fodel risg cadwyn gyflenwi, cod agored drwy ddibyniaethau wedi'u peryglu neu wedi'u gadael a pherchnogol drwy sianeli diweddaru tywyll na allwch eu harchwilio. Dewch â thystiolaeth ar gyfer eich cydrannau mwyaf hollbwysig: pwy sy'n eu hadolygu mewn gwirionedd, pa mor gyflym y caiff cynghorion eu clytio, a yw fersiynau wedi'u pinio a tharddiad wedi'i ddilysu, ac a ydych yn cynhyrchu SBOM. I ystâd fawr neu lywodraethol, cysylltwch hyn â chaffael a rhwymedigaethau sganio parhaus, oherwydd bydd rheoleiddiwr yn gofyn beth a archwilioch chi, nid a oedd y ffynhonnell yn gyhoeddus.

## Lens sector

**Cwmni newydd.** Gyda ychydig o redfa rydych yn adeiladu ar sylfeini cod agored oherwydd na allwch fforddio ffioedd trwydded ac rydych eisiau'r rhyddid i fforchio os yw prosiect yn arafu. Rhedwch sgan dadansoddiad-cyfansoddiad cyn i chi gyhoeddi fel nad yw llyfrgell copyleft-gryf yn dawel yn eich rhwymo i gyhoeddi eich ffynhonnell eich hun, a chadwch eich un gwahaniaethwr gwirioneddol yn gaeedig yn llym. Cod-agorwch offeryn bach, nad yw'n hollbwysig, os yw'n helpu recriwtio, ond peidiwch â staffio baich cynnal na allwch ei gario.

**Busnes bach.** Heb arbenigwr cyfreithiol neu blatfform mewnol, trinwch y drwydded fel risg na chewch ei chamddarllen yn hytrach na phwnc y gallwch feistroli. Ffafriwch offer perchnogol cefnogedig neu ddosbarthiadau cod agored masnachol lle mae gwerthwr yn berchen ar glytiau ac atebolrwydd, oherwydd mae hunan-gefnogi stac na allwch ei weithredu'n ddarbodaeth ffug. Pan fyddwch yn mabwysiadu cydran am ddim, gwiriwch fod ei thrwydded yn caniatáu eich defnydd a bod y prosiect mewn gwirionedd yn cael ei gynnal, nid wedi'i adael.

**Menter.** Ar raddfa fawr, y broblem yw cysondeb ar draws llawer o dimau: polisi trwydded ysgrifenedig, dadansoddiad cyfansoddiad meddalwedd awtomataidd a chynhyrchu SBOM ym mhob piblinell, a phenderfyniadau adeiladu-neu-brynu wedi'u seilio ar TCO yn hytrach nag arferiad fesul tîm. Rheolwch feddalwedd agored a pherchnogol fel un portffolio, safonwch amddiffyniadau ymadael fel fformatau agored a gwarchodfa cod ffynhonnell mewn caffael, ac olrheiniwch iechyd dibyniaethau hollbwysig fel nad yw un prosiect a adawyd yn dod yn ddigwyddiad. Llywodraethwch yr ochr cynhyrchu hefyd, gyda rheol glir ar beth mae'r sefydliad yn ei god-agor yn erbyn ei gadw ynghau.

**Llywodraeth.** Mae rheolau caffael, dyletswyddau tryloywder, ac atebolrwydd cyhoeddus yn siapio pob dewis. Pwyswch "arian cyhoeddus, cod cyhoeddus," yr egwyddor y dylai meddalwedd a ariennir gan drethdalwyr fod yn gyhoeddus yn ddiofyn, i hyrwyddo ailddefnydd ar draws asiantaethau a sofraniaeth ddigidol, tra'n cerfio esemptiadau cul ar gyfer cod sensitif-diogelwch neu ddata-personol. Mynnwch fod unrhyw gyflenwr perchnogol yn darparu allforio data mewn fformatau agored a gwarchodfa cod ffynhonnell fel na all methiant gwerthwr adael gwasanaeth cyhoeddus yn sownd, a chyhoeddwch y ffynhonnell nad yw'n sensitif fel y gall dinasyddion archwilio'r rheolau sy'n eu llywodraethu.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd tri-sylfaenydd yn adeiladu ei gynnyrch cyfan ar sylfeini cod agored (Linux, cronfa ddata cod agored, fframwaith gwe) oherwydd na all fforddio ffioedd trwydded ac mae eisiau'r rhyddid i fforchio os yw prosiect yn arafu. Cyn cyhoeddi, mae un sylfaenydd yn rhedeg sgan dadansoddiad-cyfansoddiad ac yn dal llyfrgell copyleft-gryf a fyddai wedi'u gorfodi i gyhoeddi eu halgorithm paru perchnogol, felly maent yn ei gyfnewid am gyfwerth wedi'i drwyddedu'n ganiataol. Maent yn cadw'r algorithm hwnnw, eu hunig wahaniaethwr, yn gaeedig yn llym, ac yn cod-agor dim ond offeryn logio mewnol bach i adeiladu ewyllys da ac atynnu peirianwyr.

**Menter.** Mae yswiriwr mawr yn rhedeg ei blatfform craidd ar sylfeini cod agored: Linux, cronfa ddata cod agored a ddefnyddir yn eang, a threfnydd cynwysyddion. Ond mae'n prynu cyfres modelu-actwaraidd berchnogol, oherwydd bod arbenigedd parth y gwerthwr, ardystiadau rheoleiddiol, a chontract cymorth yn werth y ffi ac nid oes dewis agored cyfatebol. Mae'n talu tanysgrifiad ar gyfer **cod agored masnachol** (dosbarthiadau wedi'u cefnogi gan werthwr o'r cydrannau agored) i gael atebolrwydd a chlytiau ar y pibellau, tra'n cadw'r algorithm prisio sy'n ei wahaniaethu'n berchnogol ac yn fewnol yn llym. Mae dadansoddiad TCO (pennod 10.10) yn gyrru pob dewis yn hytrach nag ideoleg.

**Llywodraeth.** Mae asiantaeth dreth genedlaethol, o dan bolisi "arian cyhoeddus, cod cyhoeddus," yn adeiladu gwasanaeth cymhwysedd-budd-daliadau newydd ar gydrannau cod agored a safonau agored (pennod 3.8), fel y gall asiantaethau eraill ei ailddefnyddio a dinasyddion archwilio'r rheolau. Mae'n cyhoeddi'r cod nad yw'n sensitif mewn ystorfa gyhoeddus, gan gadw dim ond heuristigau canfod-twyll yn gaeedig am resymau diogelwch. Mae hyn yn lleihau clymu i werthwr ac yn hyrwyddo sofraniaeth ddigidol (pennod 10.11). Mae rheolau caffael (pennod 10.3) yn mynnu bod unrhyw gydran berchnogol yn darparu allforio data mewn fformatau agored a gwarchodfa cod ffynhonnell, i warantu parhad os yw'r cyflenwr yn methu.

## Achos busnes: cymhellion, ROI, a TCO

Y rhan leiaf dibynadwy o'r achos yw apêl ariannol cod agored, ei ddiffyg ffi drwydded, oherwydd bod caffael yn ffracsiwn bach o TCO. Mae'r elw parhaol yn strategol: rhyddid rhag clymu (y gallu i newid neu ollwng cyflenwr heb ail-bensaernïo), archwiliadwyedd ar gyfer diogelwch a chydymffurfiaeth, mabwysiadu cyflymach oherwydd gall peirianwyr roi cynnig arno cyn ymrwymo, a chynnal a rennir o god nwyddau ar draws diwydiant cyfan. Mae'r costau gwrthbwyso'n real. Rhaid i chi gyflenwi integreiddio, gweithrediadau, ymateb diogelwch, ac yn aml gymorth taledig, a gall prosiect heb ei gynnal a ddewiswyd yn wael gostio mwy mewn digwyddiadau nag y byddai unrhyw drwydded wedi'i wneud.

Achos busnes meddalwedd berchnogol yw atebolrwydd a chyfleustra: un gwerthwr sy'n gyfrifol am y cynnyrch, contract cymorth y gallwch ei orfodi, nodweddion integredig, a chyllidebu rhagweladwy. Ei gost gudd yw clymu, y costau newid sy'n gadael i werthwr godi prisiau neu ddirywio gwasanaeth heb fawr o ddatrysiad, ynghyd â dibyniaeth ar hydoddedd a map ffordd y gwerthwr. Mae **modelau busnes** cyffredin yn cymylu'r llinell: **[craidd agored](https://en.wikipedia.org/wiki/Open-core_model)** (sylfaen agored ag ychwanegion taledig perchnogol), **trwyddedu deuol** (yr un cod yn cael ei gynnig o dan drwydded copyleft a thrwydded fasnachol daledig fel ei gilydd), **[meddalwedd fel gwasanaeth](https://en.wikipedia.org/wiki/Software_as_a_service) (SaaS)** (mae'r feddalwedd yn rhedeg fel gwasanaeth wedi'i westeio rydych yn ei rentu, lle gall y ffynhonnell fod yn amherthnasol oherwydd nad ydych byth yn meddu ar y deuaidd), a modelau **cymorth/tanysgrifiad** sy'n gwerthu gwasanaeth o gwmpas cod sydd fel arall am ddim.

I gynhyrchwr, gall ROI **cod-agor eich meddalwedd nad yw'n wahaniaethol eich hun** fod yn sylweddol. Mae cyfranwyr allanol yn lleihau eich llwyth cynnal. Mae'r prosiect yn dod yn ased recriwtio ac enw da. Mae mabwysiadu allanol yn gwneud eich safon y de facto un. I lywodraeth, mae'n cyflenwi tryloywder ac ailddefnydd ar draws y sector cyhoeddus. Mae'r rheol strategol yn syml: cod-agorwch y nwydd i rannu ei gost a thyfu ecosystem, a chadwch y gwahaniaethwr ynghau i amddiffyn y fantais sy'n ariannu popeth arall.

## Gwrth-batrymau a maglau

- **"Mae am ddim yn golygu am ddim":** trin cost caffael sero fel TCO sero, yna tan-ariannu gweithrediad a chymorth.
- **Dallineb trwydded:** mewnblannu cod copyleft-cryf mewn cynnyrch perchnogol dosbarthedig a sbarduno rhwymedigaethau na chynllunioch chi erioed amdanynt.
- **Ffydd mewn "llawer o lygaid":** tybio bod prosiect agored wedi'i archwilio pan fo ganddo un cynhaliwr goramser a dim adolygiad diogelwch.
- **Diogelwch-drwy-dywyllwch:** credu bod cod caeedig yn ddiogel oherwydd yn syml na all ymosodwyr ei ddarllen.
- **Absoliwtiaeth ideolegol:** mynnu "popeth agored" neu "popeth perchnogol" yn lle dewis fesul cydran ar sail teilyngdod a TCO.
- **Anwybyddu tarddiad:** tynnu dibyniaethau heb SBOM, pinio fersiwn, na gwirio cadwyn gyflenwi (pennod 4.2).
- **Cod-agor gemau'r goron:** rhyddhau'r union god sy'n eich gwahaniaethu, gan roi eich mantais i ffwrdd.
- **Fforchio-ac-anghofio:** fforchio prosiect a adawyd heb y gallu i gynnal y fforc mewn gwirionedd.

## Model aeddfedrwydd

**Lefel 1 (Cychwyn).** Mae cydrannau cod agored a pherchnogol yn dod i mewn i'r ystâd yn ad hoc. Nid yw trwyddedau'n cael eu darllen, nid oes rhestr na SBOM, a gwneir y dewis rhwng modelau yn ôl arferiad neu bris yn unig. Dim ond pan fydd rhywbeth yn torri y daw esgeulustod a risg trwydded i'r wyneb, a phob tîm yn ymateb ar ei ben ei hun.

**Lefel 2 (Datblygu).** Mae rhai timau'n dechrau arferion sylfaenol: rhestr cydran a thrwydded, golwg fras ar drwyddedau derbyniol, a dadansoddiad cyfansoddiad meddalwedd achlysurol. Mae penderfyniadau adeiladu-neu-brynu ac agored-neu-gaeedig yn cael eu hysgrifennu i lawr, ond mae'r ddisgyblaeth yn glytiog ac yn anghyson o un tîm i'r llall, felly gall syndod copyleft neu ffactor-bws lithro drwodd o hyd lle nad yw'r arferiad wedi gafael.

**Lefel 3 (Safoni).** Mae fframwaith wedi'i ddogfennu'n llywodraethu defnydd a chynhyrchu fel ei gilydd ar draws y sefydliad. Dewisir cydrannau ar sail TCO ac iechyd prosiect, gorfodir trwyddedau'n awtomatig yn y biblinell fel bod toriadau'n rhwystro adeiladwaith, cynhyrchir SBOMau fel mater o drefn, a datganna polisi eglur beth mae'r sefydliad yn ei god-agor yn erbyn ei gadw ynghau. Mae amddiffyniadau ymadael fel fformatau agored a gwarchodfa cod ffynhonnell yn safonol mewn caffael, ac mae pob tîm yn dilyn yr un rheolau yn hytrach na'i rai ei hun.

**Lefel 4 (Rheoli).** Mae'r rhaglen yn cael ei mesur a'i rheoli yn erbyn llinellau sylfaen. Mae'r sefydliad yn olrhain metrigau fel cwmpas SBOM ar draws cynhyrchion, y gyfran o ddibyniaethau sy'n torri polisi, amser cymedrig i glytio gwendid dibyniaeth a ddatgelwyd, sgorau ffactor-bws ac iechyd ar gyfer prosiectau hollbwysig, a TCO a wireddwyd yn erbyn yr amcangyfrif a gyfiawnhaodd bob dewis. Mae trothwyon yn sbarduno gweithredu: mae cydran y mae ei chynnal yn arafu neu y mae ei goedwedd clytio'n drifftio heibio'r targed yn cael ei fflagio ar gyfer amnewid ar dystiolaeth, ac adolygir penderfyniadau agored-neu-gaeedig ac adeiladu-neu-brynu yn erbyn y rhifau yn hytrach na'u hamddiffyn drwy arferiad.

**Lefel 5 (Cerddorfa).** Mae strategaeth cod agored yn allu busnes bwriadol, wedi'i integreiddio ar draws y sefydliad ac yn cael ei wella'n barhaus. Mae'r sefydliad yn cyfrannu at, ac weithiau'n stiwardio, y prosiectau y mae'n dibynnu arnynt, yn cod-agor ei feddalwedd nad yw'n wahaniaethol fel mater o drefn, ac yn bwydo data iechyd-dibyniaeth a TCO yn ôl i mewn i gaffael, diogelwch, a chynllunio cynnyrch. Mae'n ail-gydbwyso ei bortffolio o feddalwedd agored a pherchnogol yn rheolaidd, gan addasu i newidiadau mewn cost, risg, sofraniaeth, a mantais strategol cyn iddynt orfodi argyfwng.

## Syniadau ar gyfer trafodaeth

- Ble yn eich ystâd fyddai colli un gwerthwr neu gynhaliwr yn fodolaethol, a beth yw eich cynllun ymadael?
- Pa rai o'ch systemau eich hun sy'n nwyddau y gallech eu cod-agor, a pha rai sy'n wahaniaethwyr gwirioneddol i'w hamddiffyn?
- A yw eich sefydliad yn trin "llawer o lygaid" fel rheolaeth ddiogelwch wirioneddol neu dybiaeth heb ei harchwilio?
- I ddarllenwyr sector cyhoeddus: beth fyddai rhagosodiad "arian cyhoeddus, cod cyhoeddus" yn ei newid yn eich caffaeliad nesaf?
- Pa mor dda mae eich cymariaethau TCO'n dal y costau gweithredol a chymorth y mae cod agored yn eu symud arnoch chi?

## Casgliadau allweddol

- **Mae'r drwydded yn diffinio agored yn erbyn caeedig**, nid pris; gwybyddwch y gwahaniaeth rhwng rhydd-fel-mewn-rhyddid a rhad-fel-mewn-pris, a rhwng caniataol a copyleft.
- **Nid yw'r naill fodel na'r llall yn ddiogelach nac yn rhatach yn gynhenid.** Barnwch arferion y prosiect a'i TCO llawn, nid y label agoredrwydd.
- **Agoredrwydd yw'r gwrthwenwyn cryfaf i glymu**, gan gyflenwi archwiliadwyedd, cludadwyedd, a'r gallu i fforchio; mae meddalwedd berchnogol yn cynnig atebolrwydd a chyfleustra yn gyfnewid am reolaeth.
- **Penderfynwch fesul cydran ar sail teilyngdod**, a chymysgwch fodelau'n fwriadol yn hytrach nag yn ôl ideoleg.
- **Fel cynhyrchwr, cod-agorwch y nwydd a chadwch y gwahaniaethwr ynghau**, ac mewn llywodraeth, pwyswch "arian cyhoeddus, cod cyhoeddus" ar gyfer tryloywder, ailddefnydd, a sofraniaeth.

## Cyfeiriadau a darllen pellach

- Eric S. Raymond, *The Cathedral and the Bazaar*
- Nadia Eghbal, *Working in Public: The Making and Maintenance of Open Source Software*
- Karl Fogel, *Producing Open Source Software: How to Run a Successful Free Software Project*
- Adrian Cockcroft and others, various O'Reilly titles on open-source strategy and operations
- Free Software Foundation, *The Free Software Definition* (and the GNU General Public License texts)
- Open Source Initiative, *The Open Source Definition* and approved-license list
- Free Software Foundation Europe, *Public Money, Public Code* campaign materials
- Yochai Benkler, *The Wealth of Networks*
