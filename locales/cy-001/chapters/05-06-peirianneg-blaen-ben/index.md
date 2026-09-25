# 5.6 Peirianneg Frontend

## Trosolwg a chymhelliant

Peirianneg frontend yw'r ddisgyblaeth o adeiladu haen meddalwedd sy'n wynebu'r cleient: y cod sy'n rhedeg yn y porwr neu ar y ddyfais ac yn troi dyluniadau, cynnwys, a data yn rhyngwyneb gweithredol. Mae'n cwmpasu dewisiadau fframwaith a phensaernïaeth, strategaeth rendro, rheoli cyflwr, perfformiad, a chydnerthedd ar draws yr amrywiaeth enfawr o borwyr, dyfeisiau, ac amodau rhwydwaith yn y byd go iawn. Y frontend yw lle mae'r holl waith uwch-lif (UX, dylunio, cynnwys, hygyrchedd, rhyngwladoli) naill ai'n cyrraedd y defnyddiwr yn llwyddiannus neu'n chwalu.

I dimau mawr, mae'r frontend yn heriol mewn ffordd unigryw, oherwydd ei fod yn agored i amgylchedd nad yw'r sefydliad yn ei reoli. Mae porwyr, dyfeisiau, cysylltiadau, a gosodiadau defnyddwyr yn amrywio'n wyllt, ac mae'r platfform (y we) yn esblygu'n barhaus. Ar raddfa, mae dewisiadau pensaernïol yn cronni. Mae fframwaith a ddewisir heddiw'n cyfyngu recriwtio, perfformiad, a chynhaliadwyedd am flynyddoedd, ac mae miloedd o benderfyniadau bach am faint pecyn a rendro'n cyfrannu at y profiad y mae defnyddwyr yn ei gael mewn gwirionedd. Safonau a rennir, llyfrgelloedd cydran, cyllidebau perfformiad, a phatrymau pensaernïol yw'r hyn sy'n atal llawer o dimau annibynnol rhag cynhyrchu cyfanwaith araf, anghyson, bregus.

Mae perthnasedd i fentrau a llywodraeth yn ddifrifol. Mae mentrau'n cynnal cymwysiadau hirhoedlog lle mae hirhoedledd a chynhaliadwyedd fframwaith yn bwysicach na newydd-deb, a lle mae'n rhaid i lawer o dimau ryngweithredu. Mae llywodraethau'n gwasanaethu'r cyhoedd cyfan, gan gynnwys pobl ar hen ddyfeisiau, cysylltiadau araf neu fesuredig, a thechnolegau cynorthwyol. Mae hynny'n gwneud perfformiad, [gwelliant graddol](https://en.wikipedia.org/wiki/Progressive_enhancement), a chydnerthedd yn fwy na sglein dewisol; nhw yw'r gwahaniaeth rhwng gwasanaeth sy'n gweithio i bawb ac un sy'n eithrio'r rhai lleiaf breintiedig. Mae gwasanaeth llywodraeth sydd ond yn gweithio ar y ffôn diweddaraf gyda chysylltiad cyflym yn methu â'i fandad.

## Egwyddorion allweddol

- Mae'r frontend yn rhedeg mewn amgylchedd nad ydych yn ei reoli; dyluniwch ar gyfer amrywioldeb a methiant.
- Dewiswch dechnoleg ddiflas, barhaol ar gyfer systemau hirhoedlog; optimeiddiwch ar gyfer cynhaliadwyedd a recriwtio.
- Mae perfformiad yn nodwedd ac, i lawer o ddefnyddwyr, yn rhagofyniad ar gyfer mynediad.
- Gwelliant graddol: cyflenwch brofiad craidd gweithredol yn gyntaf, yna haenwch welliannau.
- Anfonwch lai o god; y cod cyflymaf a mwyaf dibynadwy yw'r cod nad ydych yn ei lansio.
- Parwch strategaeth rendro â math o gynnwys ac angen defnyddiwr, nid â ffasiwn.
- Cydnerthedd: dylai'r rhyngwyneb ddirywio'n osgeiddig, nid torri, pan fydd pethau'n mynd o chwith.
- Mae safonau a nodweddion platfform yn goroesi fframweithiau; pwyswch ar y platfform.

## Argymhellion

### Dewis fframweithiau ar gyfer hirhoedledd a ffit, nid hyp

Dewiswch dechnoleg frontend yn seiliedig ar y broblem, y tîm, y gorwel cynnal a chadw, a'r farchnad recriwtio, nid ar beth sy'n dueddol. Ar gyfer systemau menter a llywodraeth hirhoedlog, ffafriwch dechnolegau aeddfed, wedi'u cefnogi'n dda gyda phyllau talent mawr, arferion rhyddhau sefydlog, a llwybrau uwchraddio clir. Pwyswch gyfanswm cost cyfnewid fframwaith: mae ailysgrifennu'n ddrud ac yn beryglus. Ffafriwch ddulliau sy'n pwyso ar [safonau gwe](https://en.wikipedia.org/wiki/Web_standards) fel bod eich buddsoddiad yn goroesi trosiant fframwaith, ac ynysu cod sy'n benodol i fframwaith y tu ôl i ffiniau fel nad yw'r cymhwysiad yn wystl i gylchred bywyd un llyfrgell.

### Paru strategaeth rendro â'r angen

Mae'r prif strategaethau rendro'n addas i wahanol gynnwys, pob un yn ei ffordd ei hun. Mae rendro ochr-weinydd (SSR) yn cynhyrchu paentiad cyntaf cyflym a SEO da ([optimeiddio peiriannau chwilio](https://en.wikipedia.org/wiki/Search_engine_optimization)) ac yn gweithio heb JavaScript cleient, gan weddu tudalennau trwm ar gynnwys a rhai sy'n wynebu'r cyhoedd. Mae [cynhyrchu safle statig](https://en.wikipedia.org/wiki/Static_site_generator) (SSG) yn rhag-rendro ar amser adeiladu ar gyfer cyflymder a chacheadwyedd mwyaf, yn ddelfrydol ar gyfer cynnwys sy'n newid yn anaml. Mae rendro ochr-cleient (CSR) yn addas ar gyfer profiadau tebyg-i-ap, hynod ryngweithiol y tu ôl i ddilysu. Mae ffrydio a hydradiad graddol yn anfon ac yn actifadu'r dudalen yn gynyddrannol fel bod defnyddwyr yn gweld ac yn defnyddio cynnwys yn gynt. Mae llawer o systemau mawr yn cymysgu'r rhain fesul llwybr yn hytrach na dewis un yn fyd-eang. Rheolwch gyflwr yn fwriadol: cadwch gyflwr gweinydd, cyflwr URL, a chyflwr UI lleol yn wahanol, ac osgowch organoli popeth i mewn i un storfa fyd-eang drwm.

### Trin perfformiad fel disgyblaeth â chyllideb, wedi'i mesur

Mabwysiadwch gyllidebau perfformiad (terfynau penodol ar faint pecyn, nifer y ceisiadau, a metrigau allweddol) a'u gorfodi yn CI fel bod atchweliadau'n methu'r adeilad. Traciwch y Core Web Vitals (llwytho, rhyngweithedd, a sefydlogrwydd gweledol) gan ddefnyddio monitro defnyddwyr go iawn o ddyfeisiau a rhwydweithiau gwirioneddol, nid dim ond profion labordy ar beiriannau cyflym. Lleihewch JavaScript yn ymosodol: cod-hollti a [llwytho'n ddiog](https://en.wikipedia.org/wiki/Lazy_loading) fel bod defnyddwyr ond yn lawrlwytho'r hyn sydd ei angen ar olwg benodol, gohiriwch waith nad yw'n hanfodol, a ffafriwch alluoedd platfform dros lyfrgelloedd trwm. Optimeiddiwch ddelweddau a ffontiau, storfa'n effeithiol, a mesurwch ar ddyfeisiau isel-ben cynrychioliadol a chysylltiadau araf.

### Adeiladu â gwelliant graddol a chydnerthedd

Dechreuwch o linell sylfaen sy'n gweithio â HTML semantig a JavaScript lleiafswm neu ddim o gwbl, yna gwellwch ar gyfer cleientiaid galluog. Mae hyn yn sicrhau bod y dasg graidd yn parhau'n bosibl pan fydd sgriptiau'n methu llwytho, dyfais yn hen, neu rwydwaith yn ansefydlog, realiti cyffredin yn hytrach nag achos ymyl. Trinwch wallau'n osgeiddig: dangoswch gyflyrau defnyddiol ar gyfer llwytho, gwag, gwall, ac amodau all-lein yn hytrach na sgriniau gwag neu droellwyr diddiwedd. Ar gyfer gwasanaethau y mae pobl yn dibynnu arnynt, ystyriwch dechnegau all-lein-yn-gyntaf fel bod yr ap yn parhau'n ddefnyddiadwy drwy gysylltedd ysbeidiol, gan gydweddu pan fydd y cysylltiad yn dychwelyd.

### Sicrhau cydnawsedd traws-borwr, traws-ddyfais, a chynorthwyol

Profwch ar draws y porwyr, dyfeisiau, a thechnolegau cynorthwyol sydd gan eich defnyddwyr mewn gwirionedd, wedi'i lywio gan ddadansoddeg go iawn yn hytrach na pheiriannau'r tîm ei hun. Defnyddiwch welliant graddol a chanfod nodweddion yn hytrach na thybio bod nodweddion platfform diweddaraf ar gael ym mhobman. Adeiladwch yn [ymatebol](https://en.wikipedia.org/wiki/Responsive_web_design) (gweler pennod y system ddylunio) fel bod un sylfaen god yn gwasanaethu ffonau i gyfrifiaduron bwrdd gwaith. Integreiddiwch hygyrchedd a rhyngwladoli i mewn i bensaernïaeth frontend o'r cychwyn, nid fel camau diweddarach.

### Llywodraethu'r frontend fel seilwaith a rennir

Darparwch lyfrgelloedd cydran a rennir, meddalwedd leinio, fformatio, ac offer adeiladu fel bod timau'n gyson ac yn gynhyrchiol. Sefydlwch ganllawiau pensaernïol (sut i strwythuro cymwysiadau, rheoli cyflwr, a hollti pecynnau) a chyllidebau perfformiad wedi'u gorfodi yn CI. Ar gyfer frontendau mawr iawn, ystyriwch bensaernïaeth fodiwlaidd neu micro-frontend sy'n gadael i dimau ddefnyddio'n annibynnol, ond pwyswch y cymhlethdod a'r gost berfformiad ychwanegol yn ofalus, gan nad ydynt yn rhad ac am ddim.

## Cyfaddawdau: manteision ac anfanteision

| Penderfyniad | Manteision | Anfanteision |
|---|---|---|
| Fframwaith aeddfed poblogaidd | Pwll talent mawr, sefydlog, wedi'i gefnogi | Gall gario pwysau etifeddol; arafach i fabwysiadu'r nodweddion diweddaraf |
| Fframwaith diweddaraf | Nodweddion modern, enillion perfformiad | Risg cyfnewid, pwll talent bach, hirhoedledd ansicr |
| SSR / SSG | Paentiad cyntaf cyflym, SEO, yn gweithio heb JS | Cymhlethdod gweinydd neu adeiladu, heriau storfa |
| CSR (SPA) | Rhyngweithedd cyfoethog, teimlad tebyg-i-ap | Llwytho cyntaf araf, dibynnol ar JS, cost SEO a chydnerthedd |
| JavaScript cleient trwm | Nodweddion cyfoethog | Perfformiad gwael ar ddyfeisiau isel-ben, bregus |
| Gwelliant graddol | Cydnerth, cynhwysol, yn gweithio ym mhobman | Mwy o ymdrech ddylunio i ddiffinio llinell sylfaen weithredol |
| Micro-frontends | Defnyddio tîm annibynnol, graddfa | Cymhlethdod, dibyniaethau dyblyg, gorbenion perfformiad |

Y cyfaddawd sy'n ailddigwydd yw cyfoeth a chyfleustra datblygwyr yn erbyn cyrhaeddiad, perfformiad, a chydnerthedd. Mae dulliau trwm-ochr-cleient yn bleserus i'w hadeiladu a'u harddangos ar beiriannau cyflym, ond maent yn eithrio defnyddwyr ar ddyfeisiau a rhwydweithiau gwan. I gynulleidfaoedd menter ac yn enwedig llywodraeth, gogwyddwch y cydbwysedd tuag at berfformiad, gwelliant graddol, a pharhaustod, oherwydd bod cost eithrio defnyddwyr yn uchel ac yn aml yn anhrafodadwy.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Sut ydym yn ynysu cod sy'n benodol i fframwaith fel nad yw'r cymhwysiad yn wystl i gylchred bywyd un llyfrgell?** Ar gyfer systemau menter a llywodraeth hirhoedlog, cyfnewid fframwaith yw'r draul osgoiadwy fwyaf: mae ailysgrifennu'n ddrud ac yn beryglus, ac mae llyfrgell dueddol heddiw'n cyfyngu recriwtio a chynnal a chadw am flynyddoedd. Mae pwyso ar safonau gwe a rhoi cod sy'n benodol i fframwaith y tu ôl i ffiniau clir yn golygu bod eich rhesymeg fusnes a'ch cynnwys yn goroesi'r trosiant fframwaith nesaf. Penderfynwch ble mae'r gwniadau hynny a fyddai peiriannydd newydd yn gallu gwahaniaethu rhwng cod platfform a chod fframwaith. Dewch ag amcangyfrif o beth gostiodd eich mudo fframwaith diwethaf, neu beth fydd yr un sy'n agosáu yn ei gostio. Os yw eich rhesymeg graidd wedi'i weldio i APIs un llyfrgell, prisiwch y cyplu hwnnw cyn i chi amddiffyn dewis y fframwaith.

2. **A ydym yn paru strategaeth rendro fesul llwybr, neu'n gorfodi un strategaeth ar y cynnyrch cyfan?** Mae rendro ochr-weinydd yn rhoi paentiad cyntaf cyflym ac yn gweithio heb JavaScript cleient ar gyfer cynnwys cyhoeddus, mae cynhyrchu statig yn uchafu cyflymder ar gyfer tudalennau sy'n newid yn anaml, ac mae rendro cleient yn addas ar gyfer wynebau rhyngweithiol tebyg-i-ap y tu ôl i fewngofnodi. Mae gorfodi un yn fyd-eang naill ai'n arafu tudalennau cyhoeddus â JavaScript trwm neu'n gor-beiriannu tudalen gynnwys syml. Mae hwn yn gwestiwn cyrhaeddiad i lywodraeth, lle mae gwasanaeth sydd ond yn gweithio ar ôl i becyn mawr lwytho'n eithrio defnyddwyr ar hen ddyfeisiau a chysylltiadau araf. Dewch â'ch prif lwybrau a labelwch bob un â'r strategaeth y mae'n ei defnyddio mewn gwirionedd heddiw. Os oes angen JavaScript ar dudalen sy'n wynebu'r cyhoedd i ddangos ei chynnwys, penderfynwch a yw hynny'n ddewis bwriadol neu'n ddamwain.

3. **Pa mor ddisgybledig yw ein rheolaeth cyflwr, ac a ydym yn organoli popeth i mewn i un storfa fyd-eang drwm?** Mae cadw cyflwr gweinydd, cyflwr URL, a chyflwr UI lleol yn wahanol yn atal y cyplu a'r stormydd ail-rendro sy'n gwneud frontendau mawr yn araf ac yn fregus, ac eto'r rhagosodiad temtasiwn yw taflu popeth i mewn i un storfa fyd-eang. Mae hyn yn cronni ar raddfa, lle mae llawer o dimau'n cyffwrdd ag un storfa a rennir yn creu dibyniaethau cudd a pherfformiad anrhagweladwy. Cytunwch ble mae pob math o gyflwr yn perthyn a beth nad yw'n perthyn yn y storfa fyd-eang. Dewch â chydran sy'n ail-rendro yn fwy nag y dylai a olrheinio pam. Os mai'r ateb yw storfa ganolog wedi chwyddo, penderfynwch ar y ffiniau cyn i'r cyplu galedu.

4. **Beth yw ein cyllidebau perfformiad, a ydynt yn methu'r adeilad yn CI, ac a ydynt yn cael eu mesur ar y dyfeisiau sydd gan ein defnyddwyr mewn gwirionedd?** Dymuniad yw cyllideb nad oes neb yn ei gorfodi, ac mae cyllideb a fesurir dim ond ar liniaduron cyflym y tîm yn disgrifio defnyddiwr nad yw'n bodoli. I sefydliad mawr, cyllidebau yw'r unig fecanwaith sy'n cadw maint pecyn a'r Core Web Vitals dan reolaeth wrth i ddwsinau o dimau ychwanegu nodweddion at wyneb a rennir, oherwydd ni all unrhyw adolygydd unigol ddal pob atchweliad â llygad. Y pwysau cystadleuol yw cyflymder cyflenwi: mae methiant adeiladu caled dros ychydig gilobeitiau'n teimlo'n rhwystrol nes i chi brisio'r gadawiad y mae'n ei atal. Dewch â'ch cyllidebau cyfredol, data monitro defnyddwyr go iawn o ddyfeisiau isel-ben a chysylltiadau araf, a'r rhestr o ryddhadau lle llithrodd atchweliad drwodd. Mewn llywodraeth, lle mae'r mandad yn gwasanaethu'r cyhoedd cyfan gan gynnwys pobl ar hen ffonau a data mesuredig, clymwch y gyllideb i'r degfed araf o'ch defnyddwyr yn hytrach na'r canolrif, a gwnewch giât CI yn anhrafodadwy.

5. **Pa rai o'n gwasanaethau sy'n gorfod parhau i weithio heb JavaScript cleient, ac a ydym wedi profi'r llwybr hwnnw mewn gwirionedd?** Mae gwelliant graddol yn hawdd ei hawlio ac yn hawdd ei dorri'n dawel, oherwydd mai'r llwybr wedi'i wella yw'r un y mae datblygwyr yn ei ddefnyddio bob dydd tra bo'r llinell sylfaen yn pydru heb ei brofi. Mae penderfynu ar hyn yn fwriadol yn bwysig ar raddfa, gan y bydd llawer o dimau sy'n lansio i un platfform pob un yn tybio bod sgriptiau bob amser yn llwytho oni bai bod safon a rennir yn dweud fel arall, a gall un ddibyniaeth galed dorri'r dasg graidd i unrhyw un y mae eu pecyn yn methu. Mae'r cyfaddawd yn real: mae llinell sylfaen ddi-JavaScript sy'n gweithio'n costio ymdrech ddylunio ac yn cyfyngu sut rydych yn adeiladu rhyngweithedd. Dewch â'ch teithiau defnyddiwr critigol, prawf sy'n llwytho pob un â sgriptiau wedi'u hanalluogi neu wedi methu, a thystiolaeth o pa mor aml y mae sgriptiau'n methu llwytho mewn gwirionedd yn y maes. Ar gyfer gwasanaeth cyhoeddus, nid yw ffurflen fudd-daliadau neu dreth sy'n cwympo pan fydd un sgript yn cyrraedd terfyn amser yn brofiad dirywiedig, mae'n ddinesydd na all gwblhau rhwymedigaeth gyfreithiol, felly triniwch y llinell sylfaen fel gofyniad cydymffurfiaeth, nid moethusrwydd.

6. **Pryd mae micro-frontends yn wirioneddol yn talu am eu cymhlethdod, a phwy sy'n penderfynu cyn i dîm estyn am un?** Mae defnyddio tîm annibynnol yn ddeniadol, ond mae micro-frontends yn cario cymhlethdod system ddosbarthedig, dibyniaethau dyblyg, a threth berfformiad y mae defnyddwyr yn ei thalu mewn llwythiadau arafach. Heb bwynt penderfynu a rennir, mae timau uchelgeisiol yn eu mabwysiadu er cyfleustra sefydliadol ymhell cyn i'r raddfa gyfiawnhau'r gost, ac mae'r cynnyrch cyfan yn etifeddu'r gorbenion. Yr ystyriaeth gystadleuol yw ymreolaeth: gall timau sy'n lansio ar un sylfaen god a rennir rwystro ei gilydd, ac ar raddfa wirioneddol mae'r cyplu hwnnw'n broblem ddrud ynddo'i hun. Dewch â nifer y timau sy'n cyffwrdd â'r wyneb, y gwrthdaro defnyddio rydych yn ei brofi mewn gwirionedd heddiw, ac amcangyfrif wedi'i fesur o ddyblygiad y llwyth y byddai hollt yn ei gyflwyno. Ar gyfer platfformau menter a llywodraeth, lle mae penderfyniadau pensaernïol yn clymu llawer o dimau am flynyddoedd a rhaid iddynt oroesi archwiliad a throsglwyddiad, mynnwch drothwy penodol, wedi'i ddogfennu a pherchennog sy'n cymeradwyo'r symud, yn hytrach na gadael i bob tîm benderfynu ar ei ben ei hun.

## Lens sector

**Cwmni newydd.** Mae cyflymder a chyrhaeddiad ill dau'n bwysig pan fo pob cofrestriad yn cyfrif, felly gwrthsefwch yr ap tudalen-sengl trwm ar gyfer tudalennau cyhoeddus. Rendrwch eich llif marchnata a chofrestru ar ochr y gweinydd fel eu bod yn llwytho'n gyflym ar y ffonau canolig a'r data anwastad y mae eich cwsmeriaid cynnar yn eu defnyddio, a chadwch ryngweithedd ochr-cleient ar gyfer yr ap y tu ôl i fewngofnodi. Gosodwch un gyllideb maint pecyn syml yn CI fel na all ddibyniaeth ddiofal chwyddo'r dudalen yn dawel, a phwyswch ar safonau gwe i gadw sylfaen god fach yn gynaliadwy wrth i chi recriwtio.

**Busnes bach.** Heb arbenigwr frontend pwrpasol a chyllideb dynn, ffafriwch fframwaith prif ffrwd wedi'i gefnogi'n dda neu adeiladwr gwefan wedi'i letya dros unrhyw beth pwrpasol, fel eich bod yn recriwtio o bwll talent mawr ac yn prynu cynnal a chadw yn hytrach na'i staffio. Fframiwch y dewis fel parhaustod: yr opsiwn rhataf yw'r un nad ydych yn cael eich gorfodi i'w ailysgrifennu mewn dwy flynedd. Mynnwch dudalennau cyflym, cyfeillgar i symudol a marcio hygyrch yn syth o'r bocs, gan fod talu allan araf neu doredig yn costio i chi gwsmeriaid na allwch fforddio eu colli.

**Menter.** Y broblem yw cysondeb ar draws llawer o dimau: llyfrgell gydran a rennir, patrymau pensaernïol cytunedig, meddalwedd leinio ac offer adeiladu, a chyllidebau perfformiad wedi'u gorfodi yn CI fel na all unrhyw dîm ddirywio'r cyfan yn dawel. Dewiswch fframweithiau ar gyfer hirhoedledd a recriwtio yn hytrach na newydd-deb, ynyswch god sy'n benodol i fframwaith y tu ôl i ffiniau i oroesi'r mudo nesaf, a pharwch strategaeth rendro fesul wyneb. Rheolwch y frontend fel seilwaith a rennir gyda monitro defnyddwyr go iawn, llywodraethu, a chofnod archwiliadwy o pam y gwnaed pob dewis pensaernïol.

**Llywodraeth.** Rydych yn gwasanaethu'r cyhoedd cyfan, gan gynnwys pobl ar hen ddyfeisiau, cysylltiadau araf neu fesuredig, a thechnolegau cynorthwyol, felly mae gwelliant graddol a pherfformiad yn rwymedigaethau, nid sglein. Gwnewch linell sylfaen ddi-JavaScript sy'n gweithio yn rheol galed ar gyfer gwasanaethau sy'n wynebu dinasyddion, cyllidebwch dudalennau i'r defnyddwyr arafaf yn hytrach na'r canolrif, a chadwch y dasg graidd yn gwblhadwy pan fydd sgript yn methu. Mae caffael a thryloywder yn berthnasol: ffafriwch dechnoleg barhaol, sy'n pwyso ar safonau sy'n osgoi clymu i un gwerthwr, dogfennwch y gofynion hygyrchedd a pherfformiad mewn contractau, a byddwch yn gallu dangos bod y gwasanaeth yn gweithio i'r defnyddiwr lleiaf breintiedig, nid dim ond y ddyfais arddangos.

## Enghreifftiau

**Cwmni newydd.** Cafodd cwmni newydd cam-had ei demtio i adeiladu ei wefan farchnata a'i lif cofrestru fel ap tudalen-sengl trwm, ond siopwyr yn aml ar ffonau canolig dros ddata symudol anwastad oedd eu cwsmeriaid targed. Yn lle hynny, gwnaeth y ddau sylfaenydd rendro'r tudalennau cyhoeddus ar ochr y gweinydd fel eu bod yn llwytho'n gyflym ac yn gweithio cyn i unrhyw JavaScript redeg, a chadwyd rhyngweithedd ochr-cleient ar gyfer yr ap y tu ôl i fewngofnodi. Gosodon nhw gyllideb maint pecyn syml yn CI fel na allai ddibyniaeth ddiofal chwyddo'r dudalen yn dawel. Gwellodd y llwyth cyntaf cyflym, main gofrestriadau mewn ffordd fesuradwy, a chadwodd pwyso ar safonau gwe eu sylfaen god fach yn hawdd ei chynnal wrth iddynt recriwtio.

**Menter.** Moderneiddiodd cwmni gwasanaethau ariannol set eang o gymwysiadau mewnol a chwsmeriaid drwy safoni ar fframwaith aeddfed, llyfrgell gydran a rennir, a chyllidebau perfformiad wedi'u gorfodi yn CI. Dewiswyd strategaeth rendro fesul wyneb: tudalennau wedi'u rendro ar y gweinydd, cacheadwy ar gyfer marchnata a chynnwys cyhoeddus, a chymhwysiad wedi'i rendro ar y cleient y tu ôl i fewngofnodi ar gyfer dangosfyrddau rhyngweithiol. Daliodd cyllidebau pecyn a monitro defnyddwyr go iawn atchweliadau cyn rhyddhau, gan gadw amseroedd llwytho'n gyflym ar draws timau niferus y cwmni a lleihau'r risg cyfnewid fframwaith a oedd wedi gorfodi ailysgrifennu drud o'r blaen.

**Llywodraeth.** Adeiladodd tîm gwasanaeth digidol cenedlaethol wasanaethau sy'n wynebu dinasyddion gyda gwelliant graddol yn rheol galed: mae pob gwasanaeth yn gweithio â HTML semantig a rendro gweinydd yn gyntaf, a JavaScript ond yn gwella. Mae hyn yn gwarantu bod y gwasanaeth yn gweithredu ar hen ffonau, cysylltiadau gwledig araf, a thechnolegau cynorthwyol, poblogaethau na all llywodraeth eu heithrio. Mae cyllidebau perfformiad yn cadw tudalennau'n ysgafn a chyflym ar ddyfeisiau isel-ben, ac mae dirywiad graddol yn golygu na fydd sgript wedi methu byth yn rhwystro rhywun rhag cwblhau cais budd-daliadau. Y canlyniad yw gwasanaeth sy'n gyflym, yn gydnerth, yn hygyrch, ac yn ddefnyddiadwy gan y cyhoedd cyfan.

## Achos busnes: cymhellion, ROI, a TCO

Mae dewisiadau peirianneg frontend yn gyrru refeniw, cyrhaeddiad, a chost. Mae perfformiad yn gysylltiedig yn uniongyrchol â throsiant, ymgysylltiad, a chwblhau tasgau. Mae profiadau cyflymach yn well o gryn dipyn na rhai arafach mewn ffordd fesuradwy, ac i ddefnyddwyr ar ddyfeisiau gwan, perfformiad yw'r llinell rhwng defnyddio'r gwasanaeth a'i adael. Mae gwelliant graddol a chefnogaeth traws-ddyfais yn ehangu'r gynulleidfa y gellir ei chyrraedd, sydd i lywodraeth yn fandad ac i fenter yn gyfran farchnad. Mae dewisiadau fframwaith a phensaernïaeth cadarn yn lleihau amlder a chost ailysgrifennu, y draul osgoiadwy fwyaf mewn peirianneg frontend.

O ran TCO, costau mabwysiadu yw disgyblaeth cyllidebau perfformiad a phrofi, yr ymdrech o welliant graddol, a'r buddsoddiad mewn offer a llyfrgelloedd cydran a rennir. Telir cost peidio â mabwysiadu mewn profiadau araf sy'n colli defnyddwyr a refeniw, eithrio defnyddwyr dyfeisiau isel-ben a thechnoleg gynorthwyol (gyda risg gyfreithiol mewn llywodraeth), cymwysiadau bregus sy'n torri yn y maes, a chyfnewid a ailysgrifennu fframwaith drud wedi'i yrru gan erlid tueddiadau. Mae problemau frontend yn ymddangos fel gadawiad gwasgaredig a llwyth cefnogaeth yn hytrach nag un eitem llinell, felly maent yn hawdd tan-fuddsoddi ynddynt.

I wneud yr achos i arweinyddiaeth, cysylltwch Core Web Vitals ac amseroedd llwytho â thwndis trosi a chwblhau, meintioli'r defnyddwyr a eithrir gan ddulliau trwm-ochr-cleient, a phrisio cost ailysgrifennu yn y gorffennol neu sy'n agosáu yn erbyn sefydlogrwydd pensaernïaeth barhaol, sy'n pwyso ar safonau. Fframiwch gyllidebau perfformiad a gwelliant graddol fel lleihad risg ac ehangiad cyrhaeddiad.

## Gwrth-batrymau a pheryglon

- **Erlid fframwaith:** ailysgrifennu ar y llyfrgell ddiweddaraf, gan ysgwyddo cyfnewid heb fudd i'r defnyddiwr.
- **Profiadau JavaScript-yn-unig:** nid oes dim yn gweithio nes i becyn mawr lwytho a rhedeg, gan eithrio llawer o ddefnyddwyr.
- **Profi ar ddyfeisiau cyflym yn unig:** mae lliniaduron blaenllaw'r tîm yn cuddio'r profiad defnyddiwr go iawn.
- **Anwybyddu maint pecyn:** twf dibyniaeth di-derfyn nes bod tudalennau'n araf ym mhobman.
- **Dim cyllideb berfformiad:** mae atchweliadau'n cronni'n dawel ryddhad wrth ryddhad.
- **Methiannau sgrin wag:** dim cyflyrau llwytho, gwag, gwall, nac all-lein; mae cais wedi methu'n torri'r dudalen.
- **Cyflwr byd-eang wedi'i organoli:** popeth mewn un storfa, gan greu cyplu a stormydd ail-rendro.
- **Micro-frontends cynamserol:** cymhlethdod system ddosbarthedig a llwythi dyblyg heb y raddfa i'w cyfiawnhau.
- **Esgeuluso hygyrchedd a rhyngwladoli mewn pensaernïaeth:** eu bolltio ymlaen yn ddiweddarach am gost uchel.

## Model aeddfedrwydd

**Lefel 1: Cychwyn.** Frontend ad hoc wedi'i adeiladu fesul tîm heb safonau a rennir. Cod trwm-ochr-cleient, dim cyllidebau perfformiad, wedi'i brofi ond ar ddyfeisiau'r tîm ei hun. Dewisiadau fframwaith wedi'u gwneud yn ôl hoffter neu hyp, a gall sgript wedi methu adael defnyddwyr yn syllu ar sgrin wag.

**Lefel 2: Datblygu.** Mae rhai timau'n mabwysiadu offer a llyfrgell gydran a rennir, ond mae'r ymarfer yn anghyson ar draws y sefydliad. Mesurir perfformiad yn achlysurol yn hytrach na'i gyllidebu neu ei orfodi. Mae strategaeth rendro'n aml yn unffurf ni waeth beth yw'r math o gynnwys, ac mae profi traws-ddyfais yn gyfyngedig ac â llaw.

**Lefel 3: Safoni.** Dewisir fframwaith a phensaernïaeth yn fwriadol ar gyfer hirhoedledd, ac mae'r dewisiadau'n cael eu dogfennu a'u gorfodi ar draws y sefydliad. Mae strategaeth rendro'n cael ei pharu fesul wyneb, mae gwelliant graddol a dirywiad graddol yn safon, ac mae llyfrgelloedd cydran a rennir, meddalwedd leinio, ac offer adeiladu'n berthnasol i bob tîm. Mae traws-borwr, hygyrchedd, a rhyngwladoli wedi'u hadeiladu i mewn yn hytrach na'u bolltio ymlaen.

**Lefel 4: Rheoli.** Mesurir a rheolir y frontend â data. Gorfodir cyllidebau perfformiad yn CI fel bod atchweliadau'n methu'r adeilad, a thraciwyd Core Web Vitals â monitro defnyddwyr go iawn o ddyfeisiau isel-ben a chysylltiadau araf gwirioneddol yn erbyn llinellau sylfaen penodol. Adroddir ac adolygir maint pecyn, sylw cyflwr gwall ac all-lein, a chyfran y defnyddwyr a wasanaethir ar y cysylltiadau arafaf, fel bod penderfyniadau'n gorwedd ar dystiolaeth yn hytrach na barn.

**Lefel 5: Cydgysylltu.** Gwellir perfformiad, cydnerthedd, a chyrhaeddiad yn barhaus a'u clymu i ganlyniadau busnes ar draws y sefydliad cyfan. Mae'r frontend yn pwyso ar safonau gwe ar gyfer parhaustod, yn ynysu dibyniaethau fframwaith fel bod mudo'n rhad, ac yn esblygu pensaernïaeth yn addasol wrth i ddyfeisiau, y platfform, a data defnyddwyr go iawn symud. Mae'r cyhoedd cyfan a phob dyfais yn ddosbarth cyntaf, ac mae ymarfer frontend wedi'i integreiddio â dylunio, hygyrchedd, a chynllunio cynnyrch yn hytrach na'i drin fel pryder ar wahân.

## Syniadau ar gyfer trafodaeth

- Sut ydych chi'n penderfynu pryd mae mudo fframwaith yn werth ei gost a'i risg?
- Pa Core Web Vitals a chyllidebau pecyn ddylai fod yn drothwyon methu-adeiladu caled?
- Ble mae gwelliant graddol yn hanfodol, a ble mae ap ochr-cleient yn dderbyniol?
- Sut ydych chi'n cadw pensaernïaeth frontend yn gyson ar draws llawer o dimau ymreolaethol?
- Pryd mae micro-frontends yn wirioneddol yn talu am eu cymhlethdod?
- Sut ddylai profi dyfais go iawn a rhwydwaith araf gael eu hadeiladu i mewn i'r biblinell?

## Prif negeseuon

- Mae'r frontend yn rhedeg mewn amgylchedd nad ydych yn ei reoli: dyluniwch ar gyfer amrywioldeb a methiant.
- Dewiswch dechnoleg barhaol, wedi'i chefnogi'n dda ar gyfer systemau hirhoedlog; pwyswch ar safonau gwe.
- Parwch strategaeth rendro (SSR, SSG, CSR, ffrydio) â chynnwys ac angen, wedi'i gymysgu'n aml fesul llwybr.
- Triniwch berfformiad fel disgyblaeth â chyllideb, wedi'i mesur, wedi'i gorfodi yn CI â data defnyddwyr go iawn.
- Adeiladwch â gwelliant graddol fel bod y profiad craidd yn gweithio ym mhobman.
- Lansiwch lai o JavaScript; cod-holltwch, llwythwch yn ddiog, a ffafriwch alluoedd platfform.
- I lywodraeth yn enwedig, mae perfformiad a chydnerthedd yn rhagofynion ar gyfer mynediad teg.

## References and further reading

- Jeremy Keith, *Resilient Web Design*
- Aaron Gustafson, *Adaptive Web Design* (progressive enhancement)
- Steve Souders, *High Performance Web Sites*
- Ilya Grigorik, *High Performance Browser Networking*
- Addy Osmani, writings on performance, code-splitting, and the cost of JavaScript
- Google, *Web Vitals* and web.dev performance guidance
- MDN Web Docs, web platform and progressive enhancement references
- Alex Russell, essays on the cost of JavaScript and device diversity
- UK Government Digital Service, progressive enhancement and frontend guidance
- WHATWG HTML Living Standard and W3C web platform specifications
