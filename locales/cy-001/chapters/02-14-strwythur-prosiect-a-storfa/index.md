# 2.14 Strwythur prosiect ac ystorfa

## Trosolwg a chymhelliant

Strwythur prosiect ac ystorfa yw trefniadaeth ffisegol sylfaen cod: y ffolderi, y ffeiliau, a'r confensiynau enwi sy'n penderfynu ble mae unrhyw beth penodol yn byw. Mae *ystorfa* (a elwir yn aml yn "repo") yn gynhwysydd [dan reolaeth fersiynau](https://en.wikipedia.org/wiki/Version_control) sy'n dal ffeiliau prosiect a'u hanes. Mae *prosiect*, a elwir weithiau'n *ateb* pan fydd yn grwpio sawl cydran gysylltiedig, yn uned resymegol o feddalwedd rydych yn ei hadeiladu. Strwythur yw'r map a ddefnyddiwch i ddod o hyd i'r meddalwedd hwnnw, ei ddeall, a'i newid.

Ar dîm bach, gall un person ddal y cynllun cyfan yn eu pen. Ar dîm mawr, gyda channoedd neu filoedd o beirianwyr, symudiadau aml rhwng timau, a chontractwyr yn ymuno ac yn gadael, mae pob ystorfa sydd wedi'i threfnu'n wahanol yn codi treth wybyddol newydd. Pan agorwch ystorfa anghyfarwydd, dylech allu dyfalu ble mae'r ffynhonnell, y profion, y ddogfennaeth, a'r ffurfweddiad defnyddio'n byw, heb ddarllen llawlyfr. Pan fydd pob ystorfa'n ateb y cwestiynau hynny yn yr un ffordd, mae symudedd yn rhad a sefydlu'n gyflym. Pan fo pob ystorfa'n bluen eira, mae pob newid cyd-destun yn troi'n brosiect ymchwil bach.

Mewn lleoliadau mentrau a llywodraethol, mae strwythur cyson hefyd yn fater rheolaeth a sicrwydd. Mae angen i archwilwyr, adolygwyr diogelwch, a chynhalwyr hirdymor, sy'n aml yn gweithio flynyddoedd ar ôl i'r awduron gwreiddiol adael, allu dod o hyd yn ddibynadwy i ddogfennau manyleb, ffeiliau trwyddedu, polisïau diogelwch, a diffiniadau adeiladu. Mae cynllun rhagweladwy hefyd yn gadael i offer awtomataidd (sganwyr, dadansoddwyr dibyniaeth, gwiriadau cydymffurfiaeth) weithio yn yr un ffordd ar draws portffolio cyfan o systemau. Felly mae'r bennod hon yn trin strwythur fel confensiwn rydych yn ei benderfynu unwaith ac yn ei gymhwyso ym mhobman. Mae'n gysylltiedig yn agos â safonau ac arddull codio (pennod 2.1), rheolaeth fersiynau a rheolaeth ffynhonnell (pennod 2.6), a dogfennaeth (pennod 2.7).

## Egwyddorion allweddol

- Dilynwch *[egwyddor y syndod lleiaf](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)*: dylai'r cynllun gyfateb i'r hyn y byddai peiriannydd profiadol yn ei ddisgwyl, fel nad oes dim i'w gofio.
- Mae cysondeb ar draws ystorfeydd yn curo cyfrwystra lleol; mae cynllun sy'n ddigon unffurf ym mhobman yn werth mwy na'r cynllun perffaith mewn un lle.
- Y [README](https://en.wikipedia.org/wiki/README) yw'r drws ffrynt; dylai newydd-ddyfodiad allu ymgynefino ohono ar ei ben ei hun.
- Gwnewch strwythur yn hunan-ddisgrifiadol drwy enwi, fel bod ffolderi a ffeiliau'n cyhoeddi eu diben.
- Gorfodwch strwythur â sgaffaldwaith a themledau, nid ag ewyllys a sylwadau adolygu.
- Gwahanwch bryderon yn ffisegol: mae ffynhonnell, profion, dogfennau, adeiladu, a defnyddio yn perthyn i leoedd gwahanol, rhagweladwy.
- Trefnwch ddibyniaethau fel eu bod yn llifo mewn un cyfeiriad, o graidd sefydlog tuag at ymylon anwadal.

## Argymhellion

### Mabwysiadwch gynllun lefel-uchaf cyson

Diffiniwch set safonol o ffolderi lefel-uchaf y mae pob ystorfa'n ei defnyddio lle bo'n berthnasol, a dogfennwch ddiben pob un. Mae confensiwn cyffredin, niwtral-o-werthwr yn cynnwys: ffolder ffynhonnell (yn aml `src`) ar gyfer cod cynhyrchu; ffolder profi (yn aml `test` neu `tests`) ar gyfer profion awtomataidd; ffolder `docs` ar gyfer dogfennaeth; ffolder `build` ar gyfer diffiniadau ac allbynnau adeiladu; ffolder `deploy` ar gyfer defnyddio a *[seilwaith fel cod](https://en.wikipedia.org/wiki/Infrastructure_as_code)* (diffiniadau darllenadwy-gan-beiriant o weinyddion, rhwydweithiau, a gwasanaethau, a drafodir ym mhennod 8.2); ffolder `scripts` ar gyfer awtomeiddio ac offer datblygwr; ffolder `examples` ar gyfer samplau y gellir eu rhedeg; a ffolder `spec` neu `specification` ar gyfer gofynion a manylebau dylunio. Nid oes angen pob ffolder ar bob ystorfa, ond lle mae pryder yn bodoli, dylai fyw yn y lle disgwyliedig gyda'r enw disgwyliedig.

### Gwnewch y README yn bwynt mynediad

Mynnwch ffeil README yng ngwraidd yr ystorfa fel yr unig bwynt cychwyn canonaidd. Dylai ddatgan beth yw'r prosiect, sut i'w adeiladu a'i redeg, sut i redeg y profion, ble i ddod o hyd i ddogfennaeth ddyfnach, pwy sy'n berchen arno, a sut i gyfrannu. Nid y README yw'r set ddogfennaeth gyfan; dyma'r mynegai sy'n pwyntio at y gweddill (pennod 2.7). Triniwch README coll neu hen fel diffyg, oherwydd dyma'r peth cyntaf y bydd pob peiriannydd newydd, archwiliwr, neu integreiddiwr yn ei ddarllen.

### Safonwch ffeiliau golygydd a ffurfweddiad

Gwiriwch ffurfweddiad golygydd ac offer a rennir i mewn i'r ystorfa fel bod pob cyfrannwr yn cael ymddygiad cyson yn awtomatig. Mae ffeil `.editorconfig` (ffeil syml, niwtral-o-olygydd sy'n diffinio rheolau gofod gwyn, mewnoliad, a diweddu llinellau) yn cadw fformatio sylfaenol yn unffurf ar draws gwahanol olygyddion a systemau gweithredu. Ychwanegwch ffeil anwybyddu ar gyfer y system rheolaeth fersiynau (fel na chaiff allbynnau adeiladu ac arteffactau lleol eu hymrwymo byth), ynghyd â'r ffurfweddiadau fformatiwr a chysonwr a rennir a ddisgrifir ym mhennod 2.1. Mae'r ffeiliau hyn yn gwneud confensiynau'r ystorfa'n weithredol, nid dim ond wedi'u dogfennu.

### Diffiniwch gonfensiynau enwi a ffolderi

Cytunwch ar gonfensiynau ar gyfer enwi ffolderi a ffeiliau (cesio, gwahanwyr, unigol yn erbyn lluosog, ac ôl-ddodiaid gofynnol fel y rhai sy'n nodi profion) a'u cymhwyso'n unffurf. Dylai enwau ddatgelu bwriad a chyfateb i eirfa'r parth a ddefnyddir mewn mannau eraill yn y sefydliad. Mae'r nod yn syml: dylai llwybr gyfleu ystyr, fel bod darllen enw ffolder neu ffeil yn dweud wrthych beth sydd y tu mewn heb ei agor.

### Trefnwch haenau a dibyniaethau'n fwriadol

Strwythurwch y sylfaen cod fel bod ei haenau pensaernïol yn ymddangos yng nghynllun y ffolder, ac fel bod dibyniaethau'n llifo mewn un cyfeiriad synhwyrol. Ni ddylai polisi lefel-uwch ddibynnu ar fanylder lefel-isel. Dylai cod sefydlog, a rennir, eistedd lle gall llawer o fodylau ei gyrraedd heb greu cylchoedd. Pan fyddwch yn gwneud yr haenu'n ffisegol, wedi'i adlewyrchu yn y goeden gyfeiriaduron, mae peirianwyr yn fwy tebygol o'i barchu, ac mae troseddau'n haws eu canfod mewn adolygiad ac mewn gwiriadau dibyniaeth awtomataidd.

### Gorfodwch strwythur â sgaffaldwaith a themledau

Darparwch *[sgaffaldwaith](https://en.wikipedia.org/wiki/Scaffold_%28programming%29)*, cynhyrchu awtomataidd o brosiect cychwynnol, fel bod ystorfeydd newydd yn dechrau eisoes yn gywir. Mae *templed* neu *cookiecutter* (sgerbwd prosiect paramedredig sy'n cynhyrchu ystorfa barod o atebion i ychydig o anogeion) yn amgodio'r cynllun safonol, y README, y ffeiliau ffurfweddu, a'r sefydliad [CI](https://en.wikipedia.org/wiki/Continuous_integration) mewn un lle. Pan fydd peirianwyr yn creu gwasanaethau newydd o dempled a rennir, mae cysondeb yn dod yn ddiofyn yn hytrach na dyhead, ac mae gwelliannau i'r templed yn llifo drwodd i brosiectau'r dyfodol.

### Cadwch strwythur yn gyson ar draws llawer o ystorfeydd wrth raddfa

Triniwch y cynllun ei hun fel safon lywodraethedig: wedi'i chynnal yn ganolog fel unrhyw safon beirianyddol arall (pennod 1.7), a'i fersiynu fel cod (pennod 2.6). Cyhoeddwch ef, darparwch y templedau sy'n ei weithredu, a chaniatáu gwyriadau dim ond drwy broses eithriad ddogfennedig, fel bod "y safon" yn cadw ei hystyr. Ar raddfa portffolio, mae bron holl werth strwythur yn dod o'i unffurfiaeth ar draws ystorfeydd, felly drifft yw'r prif risg i'w reoli.

### Gadewch i strwythur lywio'r dewis rhwng monorepo ac aml-ystorfa

Cysylltwch strwythur â'r penderfyniad ffin-ystorfa a drafodir ym mhennod 2.6. Mae angen confensiwn mewnol clir ar *[fonorepo](https://en.wikipedia.org/wiki/Monorepo)* (un ystorfa'n dal llawer o brosiectau) i wahanu prosiectau a'u cod a rennir, fel bod y goeden sengl yn aros yn llywiadwy. Mae angen cysondeb traws-ystorfa cryf ar ddull *aml-ystorfa* (llawer o ystorfeydd bach, un fesul prosiect neu wasanaeth), fel bod pob ystorfa'n teimlo'n gyfarwydd er ei bod yn sefyll ar ei phen ei hun. Beth bynnag y dewis, strwythur dogfennedig, wedi'i dempledu yw'r hyn sy'n cadw llywio'n rhagweladwy. Mae'r dewis ffin yn newid ble rydych yn cymhwyso'r confensiwn, nid a oes angen un arnoch.

## Cyfaddawdau: manteision ac anfanteision

| Dewis | Manteision | Anfanteision |
|---|---|---|
| Cynllun safonol llym ar draws y sefydliad | Cynefindra ar unwaith; peirianwyr cludadwy; offer unffurf | Ffit gwael achlysurol i brosiectau anghyffredin; angen llywodraethu |
| Rhyddid cynllun fesul tîm | Optimeiddio lleol; hunanreolaeth uchel | Chwalfa; newid cyd-destun drud; offer anghyson |
| Sgaffaldwaith a themledau | Ystorfeydd cywir-yn-ddiofyn; newidiadau'n lledaenu | Cynnal templedau; risg o ddrifft o ystorfeydd a gynhyrchwyd |
| Hierarchaeth ffolder ddwfn, haenog | Strwythur amlwg; ffiniau clir | Baich llywio; llwybrau hir; risg gor-beirianneg |
| Cynllun gwastad, bas | Hawdd sganio; ychydig o seremoni | Gwahaniad gwael; yn chwalu wrth i'r prosiect dyfu |

Y cyfaddawd amlycaf yw unffurfiaeth yn erbyn hunanreolaeth. Mae un cynllun safonol yn dileu ffrithiant i'r llawer o beirianwyr sy'n symud rhwng sylfeini cod, ar draul y prosiect achlysurol nad yw ei anghenion yn ffitio'r mold yn dwt. Mewn sefydliad mawr, mae'r enillion cyfunol o gynefindra bron bob amser yn drymach na'r golled leol honno. Dyna pam mai'r osgo a argymhellir yw safon ragosodedig gryf ynghyd â llwybr eithriad dogfennedig (pennod 1.7), yn hytrach nag unffurfiaeth anhyblyg neu ryddid heb ei reoli. Cyfaddawd eilaidd yw dyfnder yn erbyn symlrwydd: digon o strwythur i wahanu pryderon gwirioneddol, ond nid cymaint fel bod llywio'n troi'n daith drwy ffolderi gwag.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Pan fydd peiriannydd yn symud i un o'n hystorfeydd anghyfarwydd, faint o amser cyn y gallant ddod o hyd i'r profion, y ffurfweddiad defnyddio, a'r perchennog?** Dyma'r dreth lywio y mae strwythur yn bodoli i'w dileu, ac ar raddfa portffolio caiff ei thalu filoedd o weithiau'r flwyddyn mewn cynyddiadau bach sy'n adio i amser peirianyddol difrifol a gollir. Pwynt egwyddor y syndod lleiaf yw y dylai peiriannydd profiadol allu dyfalu ble mae ffynhonnell, profion, dogfennau, a defnyddio'n byw heb ddarllen llawlyfr, felly'r prawf gonest yw a yw'r dyfaliad hwnnw'n llwyddo ar draws eich ystorfeydd. Dewch â rhif gwirioneddol i'r cyfarfod: amserwch eich hunain yn ymgynefino mewn dwy neu dair ystorfa fewnol anghyfarwydd, neu dynnwch ddata sefydlu ar ba mor hir mae ymunwyr newydd yn ei gymryd i wneud newid cyntaf. Os yw'r ateb yn cael ei fesur mewn diwrnodau o ymchwil yn hytrach na munudau o adnabyddiaeth, rydych wedi meintioli cost ystorfeydd pluen-eira, ac mae'n cyfiawnhau'r buddsoddiad un-tro mewn cynllun safonol y mae pob ystorfa'n ei rannu.

2. **A yw ein haenau pensaernïol yn ymddangos yn y goeden ffolderi, neu a yw cylchoedd dibyniaeth yn cuddio y tu mewn i gynllun gwastad?** Mae strwythur yn ymwneud â mwy na darganfyddadwyedd: pan fyddwch yn gwneud haenu'n ffisegol, mae peirianwyr yn ei barchu a gall adolygwyr a gwiriadau dibyniaeth awtomataidd ganfod troseddau, tra bod pentwr gwastad yn gadael i gyplu amhriodol a chylchoedd ymgripio i mewn heb eu sylwi nes bod newid yn beryglus. Ar system fawr, hirhoedlog, dyma'r hyn sy'n cadw polisi lefel-uwch rhag dibynnu'n dawel ar fanylder lefel-isel, ac mae'n union y math o erydiad sy'n rhad i'w atal ac yn ddrud i'w ddadwneud. Dewch â'ch graff dibyniaeth neu redwch wiriad cyflym: a oes cylchoedd, ac a yw unrhyw beth sefydlog yn dibynnu ar rywbeth anwadal? Dylai'r ateb eich gwthio i adlewyrchu haenau mewn cyfeiriaduron ac i ychwanegu gwiriadau cyfeiriad-dibyniaeth awtomataidd, fel bod y ffiniau'n weladwy yn y goeden ac yn cael eu gorfodi yn y biblinell yn hytrach na byw dim ond ym model meddyliol rhywun.

3. **A yw ein hystorfeydd newydd yn dechrau'n gywir o dempled, neu a ydym yn dibynnu ar dudalen wici a bwriadau da?** Strwythur a orfodir gan sgaffaldwaith yw'r diofyn; mae strwythur a ddisgrifir mewn dogfen yn drifftio, oherwydd bod realiti'n dilyn yr hyn sy'n cynhyrchu ystorfeydd, nid yr hyn y mae tudalen yn dweud y dylent edrych yn debyg iddo. I sefydliad mawr neu reoleiddiedig mae hyn hefyd yn fater sicrwydd: pan gynhyrchir pob ystorfa o dempled a rennir, mae sganwyr diogelwch, dadansoddwyr dibyniaeth, ac archwilwyr yn dod o hyd i'r drwydded, y polisi diogelwch, y fanyleb, a'r diffiniad adeiladu yn yr un lle bob tro, ar draws gwerthwyr ac ar draws blynyddoedd. Dewch â'r dystiolaeth: faint o'ch ystorfeydd diweddar a sgaffaldiwyd o'r templed safonol yn erbyn eu cydosod â llaw, a pha mor bell mae'r rhai wedi'u templedu wedi drifftio ers hynny? Y gweithred yw gwneud y templed yr unig ffordd hawdd o gychwyn ystorfa, ei lywodraethu fel safon wedi'i fersiynu gyda llwybr eithriad dogfennedig, a chanfod drifft yn awtomatig, oherwydd unffurfiaeth yw lle mae bron holl werth strwythur yn byw.

4. **A ydym wedi penderfynu a yw ein safon yn rhychwantu monorepo neu lawer o ystorfeydd ar wahân, ac a yw'r un confensiwn wir yn dal ar y ddwy ochr i'r ffin honno?** Mae'r dewis ffin-ystorfa'n newid ble rydych yn cymhwyso'r confensiwn, nid a oes angen un arnoch, ac mae ei gael yn anghywir yn golygu naill ai goeden anferth na all neb ei llywio neu wasgariad o ystorfeydd sydd pob un yn teimlo'n estron. Mae angen confensiwn mewnol clir ar fonorepo i wahanu prosiectau a'u cod a rennir fel bod y goeden sengl yn aros yn llywiadwy, tra bod angen cysondeb traws-ystorfa cryf ar ddull aml-ystorfa fel bod pob ystorfa unigol yn dal i deimlo'n gyfarwydd. Dewch â'r arolwg cyfredol: faint o ystorfeydd sydd gennych, sut mae cod a rennir wedi'i wahanu y tu mewn i unrhyw fonorepo, a phrawf amserol o a all peiriannydd ddod o hyd i brosiect y tu mewn i'r goeden fawr mor gyflym â dod o hyd i un mewn ystorfa unigol. Ar gyfer menter fawr neu raglen lywodraethol lle mae gwahanol werthwyr yn cyflenwi ystorfeydd ar wahân, penderfynwch yn fwriadol pa rannau o'r confensiwn sy'n gyffredinol a pha rai sy'n benodol i'r ffin, oherwydd rhaid i archwilwyr ac offer platfform weithio yn yr un ffordd p'un a yw'r cod yn cyrraedd fel un goeden neu hanner cant.

5. **Pwy sy'n berchen ar ein safon strwythur, a beth sy'n digwydd mewn gwirionedd pan nad yw prosiect wir yn ei ffitio?** Ar raddfa portffolio mae bron holl werth strwythur yn dod o unffurfiaeth, felly'r risgiau gwirioneddol yw safon ddi-berchennog sy'n pydru a llwybr eithriad mor annelwig fel bod pob tîm yn dawel yn dyfeisio ei gynllun ei hun. Mae'r tyndra rhwng unffurfiaeth anhyblyg nad yw'n ffitio unrhyw brosiect anghyffredin a rhyddid heb ei reoli sy'n chwalu popeth, a'r ateb iach yw diofyn cryf ynghyd â phroses eithriad ddogfennedig, archwiliadwy dan berchennog enwebedig a'i fersiynu fel cod. Dewch â'r dystiolaeth: a oes perchennog atebol sengl, dogfen safon wedi'i fersiynu gyda log newid, cofnod o eithriadau a roddwyd a pham, a chyfrif o wyriadau heb eu dogfennu y gallwch ddod o hyd iddynt yn y gwyllt. Mewn lleoliadau mentrau a llywodraethol mae eithriad na chofnododd neb yn fwlch rheolaeth, felly clymwch bob gwyriad wrth gyfiawnhad ysgrifenedig a dyddiad adolygu, a sicrhewch fod contractau caffael sy'n mynnu'r cynllun hefyd yn enwi pwy sy'n cael cymeradwyo ymadawiadau ohono.

6. **A yw ein README a'n ffeiliau ffurfweddu a wiriwyd i mewn yn gwneud ein confensiynau'n weithredol, neu a ydynt yn addurniadol?** README yw'r drws ffrynt, a'r `.editorconfig`, ffeil anwybyddu, a ffurfweddiad cysonwr a wiriwyd i mewn yw'r hyn sy'n gwneud confensiynau'n hunanorfodol, ac eto dyma'r pethau cyntaf i heneiddio a'r olaf y bydd unrhyw un yn eu sylwi arnynt nes na all archwiliwr neu ymunwr newydd gael y prosiect i adeiladu. Mae'r tyndra rhwng README tenau sy'n aros yn gyfredol a README trylwyr sy'n drifftio, a rhwng ymddiried mewn pobl i fformatio cod yn gywir a gadael i ffurfweddiad a rennir ei orfodi'n awtomatig. Dewch â sampl: tynnwch bum ystorfa a gwiriwch faint o READMEs sy'n datgan beth yw'r prosiect, sut i'w adeiladu, ei brofi, a'i redeg, a phwy sy'n berchen arno, a faint sy'n cario'r ffeiliau ffurfweddu a rennir yn hytrach na dibynnu ar arferion unigol. I sefydliad mawr neu reoleiddiedig, lle mae integreiddwyr, adolygwyr diogelwch, a chynhalwyr hirdymor yn darllen y README cyn dim byd arall, triniwch ddrws ffrynt coll neu hen fel diffyg dan berchennog, a gwiriwch bresenoldeb ffeiliau ffurfweddu'n awtomatig fel nad yw cydymffurfiaeth yn dibynnu ar ewyllys da.

## Trwy lens sector

**Cwmni newydd.** Cyflymder sy'n ennill, felly cytunwch ar un cynllun syml, digon gwastad ar gyfer eich ystorfa gyntaf (src, test, docs, scripts, README wedi'i lenwi, `.editorconfig`, a ffeiliau anwybyddu) a'i gadw fel templed ysgafn yr un prynhawn. Cynhyrchwch yr ail wasanaeth ohono fel bod y ddwy ystorfa'n teimlo'n gyfarwydd ac contractwr newydd yn sefydlu mewn oriau yn hytrach na pheiriannu-gwrthdro pluen eira. Gwrthsefwch hierarchaethau dwfn a llywodraethu trwm nad oes eu hangen arnoch eto; y dychweliad cyfan yma yw bod dau sylfaenydd a chontractwr yn rhannu un map.

**Busnes bach.** Heb arbenigwr platfform a chyllideb dynn, mabwysiadwch y cynllun confensiynol y mae eich iaith neu fframwaith eisoes yn ei dybio yn hytrach na dyfeisio un, fel bod offer parod a phenodiad newydd yn cyrraedd wedi'u cyn-hyfforddi arno. Prynwch sgaffaldwaith (cynhyrchydd fframwaith neu dempled cookiecutter) yn hytrach nag adeiladu eich un eich hun, a threuliwch eich ymdrech brin yn cadw README wedi'i lenwi'n gyfredol. Y README hwnnw yw'r yswiriant rhataf sydd gennych ar gyfer y diwrnod y bydd yr un person a wyddai'r cynllun yn symud ymlaen.

**Menter.** Ar draws llawer o dimau a channoedd o ystorfeydd y nod yw unffurfiaeth: cyhoeddwch safon strwythur wedi'i fersiynu, cynhyrchwch bob gwasanaeth newydd o dempledau a rennir, canfyddwch ddrifft yn awtomatig, a chaniatáu gwyriadau dim ond drwy broses eithriad ddogfennedig. Am fod pob ystorfa'n edrych yr un fath, mae peiriannydd a ailbenodwyd i dîm newydd yn gynhyrchiol o fewn oriau ac mae sganwyr diogelwch a dibyniaeth portffolio-eang yn dod o hyd i'r drwydded, y polisi diogelwch, a'r diffiniad adeiladu yn yr un lle bob tro. Cyllidebwch gynnal templedau a chanfod drifft yn benodol, oherwydd dyna'r cynhaliaeth sy'n cadw'r safon yn ystyrlon wrth raddfa.

**Llywodraeth.** Mae caffael, tryloywder, ac atebolrwydd hirdymor yn siapio'r cynllun, felly mynnwch strwythur cyffredin yn y safonau cyflenwi sy'n rhwymo pob gwerthwr. Mynnwch ffolder `specification` yn cysylltu cod â gofynion cymeradwyedig, ffeil drwydded a pholisi diogelwch yn y gwraidd, a ffolder `deploy` yn dal y diffiniadau seilwaith-fel-cod, fel bod archwilwyr yn lleoli arteffactau cydymffurfiaeth yn yr un ffordd ym mhob system. Am fod contractwyr o wahanol werthwyr i gyd yn dilyn un map, mae cynnal ar ôl i gontract ddod i ben yn costio llawer llai, ac mae'r cyhoedd yn ennill llwybr amddiffynadwy, archwiliadwy o ofyniad i god sy'n rhedeg.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd tri pherson yn cytuno ar gynllun safonol syml ar gyfer ei ystorfa gyntaf (src, test, docs, scripts, README wedi'i lenwi, .editorconfig, a ffeiliau anwybyddu) ac yn ei gadw fel templed ysgafn. Pan fyddant yn troi eu hail wasanaeth fis yn ddiweddarach, maent yn ei gynhyrchu o'r templed hwnnw, fel bod y ddwy ystorfa eisoes yn teimlo'n gyfarwydd a'r contractwr newydd yn sefydlu mewn prynhawn. Maent yn gwrthsefyll hierarchaethau ffolder dwfn nad oes eu hangen arnynt eto, gan gadw'r goeden yn ddigon gwastad i'w sganio ar un olwg. Un prynhawn o osod oedd y gost, ac mae'n eu harbed rhag y gwasgariad pluen-eira a fyddai fel arall yn gwneud pob ystorfa dyfodol yn brosiect ymchwil bach.

**Menter.** Mae manwerthwr amlwladol yn rhedeg cannoedd o wasanaethau ar draws sawl iaith. Mae ei dîm platfform yn cyhoeddi safon strwythur-ystorfa wedi'i fersiynu a set o dempledau prosiect sy'n ei gweithredu. Mae pob gwasanaeth newydd yn cael ei gynhyrchu o dempled, felly mae'n cyrraedd gyda'r ffolderi safonol `src`, `test`, `docs`, `deploy`, a `scripts`, README wedi'i lenwi, `.editorconfig`, ffeiliau anwybyddu, a phiblinell CI weithredol. Am fod pob ystorfa'n edrych yr un fath, mae peiriannydd a ailbenodwyd i dîm newydd yn gynhyrchiol o fewn oriau, ac mae sganwyr diogelwch a dibyniaeth sefydliad-eang yn rhedeg yn unffurf oherwydd eu bod bob amser yn dod o hyd i ffeiliau lle maent yn eu disgwyl.

**Llywodraeth.** Mae asiantaeth genedlaethol sy'n moderneiddio systemau etifeddol yn mynnu cynllun ystorfa cyffredin fel rhan o'i safonau cyflenwi ar gyfer pob gwerthwr. Rhaid i bob ystorfa gynnwys ffolder `specification` yn cysylltu cod â gofynion cymeradwyedig, README dogfennedig, ffeil drwydded a pholisi diogelwch yn y gwraidd, a ffolder `deploy` yn dal y diffiniadau seilwaith-fel-cod (pennod 8.2). Am fod contractwyr o wahanol werthwyr i gyd yn dilyn yr un strwythur, gall archwilwyr yr asiantaeth leoli arteffactau cydymffurfiaeth yn yr un ffordd ym mhob system, ac mae cynnal hirdymor ar ôl i gontract ddod i ben yn costio llawer llai oherwydd bod cynhalwyr sy'n cyrraedd eisoes yn gwybod y map.

## Achos busnes: cymhellion, ROI, a TCO

Mae cost mabwysiadu safon strwythur yn bennaf yn un-tro: cytuno ar y cynllun, adeiladu'r templedau, a dogfennu'r confensiwn. Mae'r gost gylchol yn isel, wedi'i chrynhoi mewn cynnal templedau a llywodraethu eithriadau. Mae cost *peidio â* chael safon yn gylchol ac yn cyfansymio: mae pob peiriannydd sy'n agor ystorfa anghyfarwydd yn talu treth lywio, mae pob sefydlu'n rhedeg yn arafach, ac mae'n rhaid ffurfweddu offer awtomataidd fesul ystorfa oherwydd nad oes dim lle rydych yn ei ddisgwyl. Ar draws sefydliad mawr, mae'r ffrithiannau bach hyn yn lluosi'n golledion difrifol o amser peirianyddol.

Mae'r enillion yn ymddangos fel sefydlu cyflymach, symudedd rhatach rhwng timau, signal uwch o offer portffolio-eang, ac, mewn lleoliadau rheoleiddiedig, cost archwilio a chynnal-hirdymor is, oherwydd bod arteffactau bob amser i'w canfod. Mae *cyfanswm cost perchnogaeth* (TCO, sef cost oes lawn adeiladu, rhedeg, a chynnal system) yn gostwng fwyaf mewn systemau hirhoedlog, lle nad yw'r cynhalwyr sy'n elwa o strwythur rhagweladwy fel arfer yn awduron a'i creodd. I wneud yr achos i arweinyddiaeth, fframiwch strwythur fel safon cost-isel, trosoledd-uchel sy'n gwella cynhyrchiant datblygwyr a pharodrwydd archwilio, a rhowch rif ar gost anghysondeb heddiw gan ddefnyddio data amser-sefydlu a'r ymdrech a dreulir yn hela am bethau mewn ystorfeydd anghyfarwydd.

## Gwrthbatrymau a pheryglon

- **Yr ystorfa bluen eira:** pob ystorfa wedi'i threfnu'n wahanol, felly rhaid ailddysgu pob un o'r dechrau.
- **Y README coll neu hen:** dim drws ffrynt, gan orfodi newydd-ddyfodiaid i beirianneg-wrthdro sut i adeiladu a rhedeg y prosiect.
- **Strwythur drwy ddogfen, nid drwy dempled:** mae tudalen wici'n disgrifio'r cynllun safonol, ond nid oes dim yn ei gynhyrchu na'i orfodi, felly mae realiti'n drifftio i ffwrdd ohono.
- **Drifft templed:** mae ystorfeydd a gynhyrchwyd o dempled yn gwahaniaethu dros amser ac ni fydd gwelliannau i'r templed byth yn eu cyrraedd.
- **Hierarchaeth wedi'i gor-beirianyddu:** nythau dwfn o ffolderi bron-yn-wag sy'n ychwanegu seremoni heb gynorthwyo llywio.
- **Pryderon cymysg:** ffynhonnell, profion, allbynnau adeiladu, a chyfrinachau wedi'u cymysgu heb wahaniad clir.
- **Allbynnau adeiladu ac arteffactau lleol wedi'u hymrwymo:** ffeiliau a gynhyrchwyd wedi'u gwirio i mewn oherwydd na chafodd rheolau anwybyddu eu gosod erioed, gan lygru hanes a gwahaniaethau.
- **Troseddau haen wedi'u cuddio gan strwythur gwastad:** dim ffiniau ffisegol, felly mae cylchoedd dibyniaeth a chyplu amhriodol yn ymgripio i mewn heb eu sylwi.

## Model aeddfedrwydd

- **Lefel 1 (Cychwyn):** Mae pob ystorfa'n cael ei threfnu ad hoc gan ei hawduron, gan ymateb i beth bynnag sydd ei angen ar y foment; mae cynlluniau'n amrywio'n eang; mae READMEs ar goll neu'n annibynadwy; rhaid arwain newydd-ddyfodiaid drwy bob ystorfa â llaw.
- **Lefel 2 (Datblygu):** Mae confensiynau sylfaenol yn bodoli'n anffurfiol ac mae llawer o ystorfeydd yn debyg i'w gilydd; mae rhai timau'n cadw cynllun cychwynnol eu hunain; ond nid oes safon awdurdodol, dim sgaffaldwaith a rennir, ac mae strwythur yn drifftio'n amlwg o un tîm i'r llall.
- **Lefel 3 (Safoni):** Gorfodir safon strwythur ddogfennedig, wedi'i fersiynu ar draws y sefydliad; cynhyrchir ystorfeydd newydd o dempledau a rennir sy'n cario cynllun safonol, README, ffeiliau ffurfweddu, a CI; mae gwyriadau'n mynd drwy broses eithriad ddogfennedig yn hytrach na digwydd yn dawel.
- **Lefel 4 (Rheoli):** Mesurir a rheolir cydymffurfiaeth â'r safon â data: mae gwiriadau awtomataidd yn adrodd pa gyfran o ystorfeydd sy'n cyfateb i'r cynllun, pa mor bell mae ystorfeydd wedi'u templedu wedi drifftio, cyflawnrwydd README, a throseddau cyfeiriad-dibyniaeth, y cyfan yn cael eu holrhain yn erbyn llinellau sylfaen; mesurir amseroedd sefydlu a llywio; cofnodir ac adolygir eithriadau, a chymeradwyir newidiadau templed ar y dystiolaeth yn hytrach na barn.
- **Lefel 5 (Cerddorfa):** Mae strwythur yn cael ei wella'n barhaus ac yn addasol: mae gwelliannau templed yn lledaenu'n awtomatig i ystorfeydd presennol, mae llywodraethu strwythur wedi'i integreiddio â diogelwch, cydymffurfiaeth, ac offer platfform, ac mae'r safon yn esblygu'n fwriadol wrth i ieithoedd, pensaernïaethau, a'r portffolio newid, gan gadw unffurfiaeth yn uchel tra bod y sefydliad yn newid o'i amgylch.

## Syniadau ar gyfer trafodaeth

- Pa ffolderi lefel-uchaf ddylai fod yn wirioneddol gyffredinol ar draws eich sefydliad, a pha rai ddylai fod yn ddewisol?
- Sut ydych chi'n cadw ystorfeydd a gynhyrchwyd o dempled rhag drifftio i ffwrdd ohono dros amser?
- Ble mae'r llinell rhwng hierarchaeth haenog, ddefnyddiol a seremoni ffolder wedi'i gor-beirianyddu?
- Sut ddylai eich safon strwythur wahaniaethu, os o gwbl, rhwng dull monorepo ac aml-ystorfa?
- Beth yw'r broses eithriad gywir ar gyfer prosiect nad yw ei anghenion gwirioneddol yn ffitio'r cynllun safonol?
- Faint o'ch strwythur y gellir ei wirio'n awtomatig, a beth sy'n dal i ddibynnu ar adolygiad dynol?
- Pwy sy'n berchen ar y safon strwythur a'i themledau, a sut mae newidiadau'n cael eu cynnig a'u cyflwyno?

## Prif negeseuon

- Trefnwch bob ystorfa fel y gall unrhyw beiriannydd lywio unrhyw sylfaen cod yn ôl disgwyliad, gan ddilyn egwyddor y syndod lleiaf.
- Mabwysiadwch gynllun lefel-uchaf cyson (ffynhonnell, profi, dogfennau, adeiladu, defnyddio, sgriptiau, enghreifftiau, manyleb) a gwnewch y README yn bwynt mynediad.
- Gwiriwch ffurfweddiad golygydd ac offer i mewn (fel `.editorconfig`) fel bod confensiynau'n weithredol, nid dim ond wedi'u hysgrifennu i lawr.
- Gorfodwch strwythur â sgaffaldwaith a themledau fel bod ystorfeydd newydd yn gywir yn ddiofyn.
- Wrth raddfa, mae'r gwerth mewn unffurfiaeth: llywodraethwch y safon, rheolwch ddrifft, a chaniatáu gwyriadau dim ond drwy eithriad dogfennedig.

## Cyfeiriadau a darllen pellach

- Robert C. Martin, *Clean Architecture: A Craftsman's Guide to Software Structure and Design*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Andrew Hunt a David Thomas, *The Pragmatic Programmer*
- Titus Winters, Tom Manshreck, a Hyrum Wright (goln.), *Software Engineering at Google*
- Scott Chacon a Ben Straub, *Pro Git*
- Dogfennaeth prosiect EditorConfig (fel safon gyfeirio ar gyfer ffurfweddiad golygydd)
