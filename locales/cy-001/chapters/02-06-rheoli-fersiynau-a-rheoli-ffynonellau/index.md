# 2.6 Rheolaeth fersiynau a rheoli ffynhonnell

## Trosolwg a chymhelliant

Meddyliwch am [reolaeth fersiynau](https://en.wikipedia.org/wiki/Version_control) fel system gofnodion eich sylfaen god. Mae'n dal pob newid, gan gynnwys pwy a'i gwnaeth, pryd, a pham, ac mae'n gadael i lawer o bobl weithio ar yr un feddalwedd heb ysgrifennu dros ei gilydd. I sefydliad mawr, mae'n llawer mwy na chopi wrth gefn. Dyma'r sylfaen y mae cydweithredu, [integreiddio parhaus](https://en.wikipedia.org/wiki/Continuous_integration) (CI), archwilio, a rheoli rhyddhau i gyd yn gorwedd arni. Mae'r dewisiadau a wnewch am gangheniad, strwythur ystorfa, a disgyblaeth cyflwyno'n siapio pa mor gyflym y gall eich tîm symud, a pha mor ddiogel.

I dimau mawr, mae rheoli ffynhonnell yn broblem gydgysylltu ar raddfa mewn gwirionedd. Pan fydd cannoedd o beirianwyr yn gwthio newidiadau i mewn i god a rennir, mae angen strategaeth arnynt sy'n cadw cyfuniadau'n fach, yn cadw'r brif linell yn rhyddhadwy, ac yn cadw hanes yn ddarllenadwy. Mae tîm sy'n integreiddio'n barhaus yn llifo'n llyfn. Mae tîm sy'n gadael i ganghennau wyro am wythnosau'n gwegian o un argyfwng integreiddio i'r llall. Mae strwythur eich ystorfa, un ystorfa fawr neu lawer, hefyd yn siapio sut mae timau'n rhannu cod ac yn cydgysylltu.

Mae lleoliadau menter a llywodraeth yn ychwanegu ychydig o ofynion pellach: olrheiniadwyedd, rheolaeth mynediad, a chadw. Efallai y bydd angen i newid gysylltu ag eitem waith gymeradwy at ddibenion archwilio. Ni ddylai cyfrinachau byth fynd i mewn i hanes. Rhaid i fynediad at ystorfa barchu ffiniau diogelwch. Yma, mae eich arferion rheolaeth fersiynau'n dod yn rhan o fframwaith rheolaeth y sefydliad, a gall camgymeriad fel cyfrinach a ollyngwyd neu hanes na ellir ei archwilio gael canlyniadau difrifol.

## Egwyddorion allweddol

- Integreiddiwch newidiadau bach yn aml; gwyriad hir yw gwraidd poen cyfuno.
- Cadwch y brif linell yn rhyddhadwy bob amser.
- Dogfennaeth yw hanes; ysgrifennwch gyflwyniadau ar gyfer y darllenydd yn y dyfodol sy'n gorfod deall pam.
- Peidiwch byth â chyflwyno cyfrinachau; trinwch unrhyw gyfrinach sy'n cyrraedd hanes fel un wedi'i chyfaddawdu.
- Awtomeiddiwch orfodi hylendid (bachau, gwiriadau CI) yn hytrach na dibynnu ar ddisgyblaeth yn unig.
- Dewiswch strwythur ystorfa (mono neu poly) yn ôl sut mae timau'n rhannu cod ac yn cydgysylltu mewn gwirionedd, nid yn ôl ffasiwn.
- Cysylltwch newidiadau â'u rhesymeg (eitemau gwaith, tocynnau, neu benderfyniadau) er mwyn olrheiniadwyedd.

## Argymhellion

### Ffafrio datblygu seiliedig ar gefn gyda changhennau byrhoedlog

Gogwyddwch tuag at [ddatblygu seiliedig ar gefn](https://en.wikipedia.org/wiki/Trunk-based_development): integreiddiwch i brif linell a rennir yn aml, gan ddefnyddio canghennau nodwedd byrhoedlog wedi'u mesur mewn oriau neu ddyddiau, nid wythnosau. Mae canghennau byr yn cadw cyfuniadau'n fach a integreiddio'n barhaus, ac mae'r arferiad hwnnw'n gysylltiedig yn gryf â pherfformiad cyflenwi uchel. Pan nad yw gwaith wedi'i orffen eto, peidiwch â'i barcio ar gangen hirhoedlog. Defnyddiwch [faneri nodwedd](https://en.wikipedia.org/wiki/Feature_toggle), switshis amser rhedeg sy'n cuddio gwaith heb ei orffen, fel y gallwch ei gyfuno'n ddiogel yn lle hynny. Cadwch ganghennau rhyddhau hirhoedlog ar gyfer cefnogaeth aml-fersiwn wirioneddol, a mynd i mewn gan wybod y gost gynnal a chadw y maent yn ei chario.

### Dewis model cangheniad sy'n addas i gyflymder rhyddhau

Parwch eich [model cangheniad](https://en.wikipedia.org/wiki/Branching_(version_control)) â sut rydych yn rhyddhau mewn gwirionedd. Os ydych yn defnyddio'n barhaus, mae datblygu seiliedig ar gefn gyda changheniad lleiafswm yn eich gwasanaethu'n dda. Os ydych yn lansio rhyddhadau wedi'u fersiynu i gwsmeriaid, neu'n cefnogi sawl fersiwn fyw ar unwaith, efallai y bydd angen canghennau rhyddhau ac ôl-borthio arnoch. Cadwch draw o fodelau trwm gyda llawer o ganghennau hirhoedlog oni bai bod eich model rhyddhau wir yn eu mynnu, oherwydd maent yn lluosi gorbenion cyfuno a chynnal a chadw.

### Penderfynu monoystorfa yn erbyn amlystorfa yn fwriadol

Estynnwch am [fonoystorfa](https://en.wikipedia.org/wiki/Monorepo), un ystorfa sengl sy'n dal llawer o brosiectau, pan fydd timau'n rhannu cod yn helaeth, angen newidiadau atomig traws-brosiect, ac eisiau offer a gwelededd unedig. Yn gyfnewid, rydych yn derbyn yr angen am offer adeiladu ar raddfa fawr a rheolaethau mynediad. Estynnwch am amlystorfeydd, ystorfeydd ar wahân fesul prosiect neu wasanaeth, pan fydd timau a gwasanaethau'n wirioneddol annibynnol, eisiau mynediad a chylchoedd rhyddhau ynysig, a heb angen newidiadau atomig traws-ystorfa. Yn gyfnewid, rydych yn derbyn cost cydgysylltu newidiadau sy'n rhychwantu ystorfeydd. Mae'r ddau'n gweithio ar raddfa. Y dewis anghywir ar gyfer eich patrwm cyplu sy'n creu ffrithiant cyson.

### Gorfodi hylendid cyflwyniadau a chyflwyniadau confensiynol

Gofynnwch am negeseuon cyflwyno sy'n esbonio pam y gwnaed newid, nid dim ond beth. Mabwysiadwch gonfensiwn fel cyflwyniadau confensiynol fel bod negeseuon wedi'u strwythuro a'u dosrannu gan beiriant, sy'n eich galluogi i awtomeiddio cofnodion newid a fersiynu. Cadwch gyflwyniadau'n atomig, un newid rhesymegol yr un, fel bod hanes yn aros yn ddwy-rannadwy ac yn hawdd ei ddadwneud. Gadewch i fachau a gwiriadau CI orfodi fformat negeseuon a hylendid sylfaenol, yn hytrach na dibynnu ar gof.

### Cadw deuaidd mawr a chod a gynhyrchir allan o hanes cyffredin

Peidiwch â chyflwyno asedau deuaidd mawr yn syth i'r prif hanes, oherwydd maent yn chwyddo pob clôn am byth. Defnyddiwch fecanwaith storio ffeiliau mawr neu ystorfa arteffactau yn lle hynny. Fel rheol, osgowch gyflwyno cod a gynhyrchir hefyd; ei gynhyrchu yn yr adeilad. Pan fydd yn rhaid i chi gyflwyno arteffact a gynhyrchwyd mewn gwirionedd, ynyswch ef a'i farcio'n glir fel nad yw'n llygru adolygiadau a gwahaniaethau.

### Atal cyfrinachau rhag mynd i mewn i'r ystorfa byth

Rhowch sganio cyfrinachau awtomataidd yn eich bachau cyn-cyflwyno a CI fel bod manylion adnabod yn cael eu blocio cyn iddynt lanio o gwbl. Rhowch system rheoli cyfrinachau briodol i beirianwyr, fel nad oes byth angen iddynt godio manylyn adnabod yn galed yn y lle cyntaf. A thriniwch unrhyw gyfrinach sy'n cyrraedd hanes fel un wedi'i chyfaddawdu: cylchdrowch hi ar unwaith. Unwaith y bydd cyfrinach wedi'i gwthio a'i chlonio, mae ei thynnu o hanes yn anodd ac yn annibynadwy.

### Sefydlu rheolaeth mynediad ac olrheiniadwyedd

Sefydlwch fynediad ystorfa i barchu ffiniau diogelwch a'r [egwyddor lleiaf braint](https://en.wikipedia.org/wiki/Principle_of_least_privilege). Cysylltwch gyflwyniadau neu geisiadau tynnu ag eitemau gwaith, fel bod pob newid yn olrhain yn ôl at ei resymeg, sy'n helpu cyd-destun peirianneg dydd-i-ddydd ac archwilio ill dau. Amddiffynnwch eich canghennau allweddol â gwiriadau ac adolygiadau gofynnol, fel nad oes dim yn cyfuno heb glirio'r giatiau y cytunwyd arnynt.

## Cyfaddawdau: manteision ac anfanteision

| Dewis | Manteision | Anfanteision |
|---|---|---|
| Datblygu seiliedig ar gefn | Integreiddio parhaus; cyfuniadau bach; llif uchel | Angen baneri nodwedd a disgyblaeth; llai o ynysu |
| Canghennau nodwedd hirhoedlog | Ynysu cryf gwaith ar y gweill | Cyfuniadau poenus; integreiddio wedi'i oedi; drifft |
| Monoystorfa | Newidiadau atomig traws-brosiect; offer a rennir; gwelededd | Angen offer adeiladu ar raddfa fawr; rheolaeth mynediad bras yn ddiofyn |
| Amlystorfa | Rhyddhadau annibynnol; mynediad ynysig; offer syml fesul ystorfa | Newidiadau traws-ystorfa anodd; gorbenion cydgysylltu fersiwn |
| Cyflwyniadau confensiynol | Cofnodion newid a fersiynu awtomataidd; hanes cyson | Confensiwn ymlaen llaw; angen gorfodi |

Y cyfaddawd mawr yma yw amlder integreiddio yn erbyn ynysu. Mae canghennau hirhoedlog yn teimlo'n fwy diogel am fod eich gwaith yn eistedd ar wahân ar ei ben ei hun, ond yr union ynysu hwnnw sy'n achosi'r cyfuniadau drud a'r syrpreisys integreiddio'n ddiweddarach. Mae datblygu seiliedig ar gefn yn rhoi'r gorau i'r teimlad hwnnw o ynysu yn gyfnewid am integreiddio parhaus, rhad, ac yn gofyn i chi ddod â baneri nodwedd a disgyblaeth. Mae'r penderfyniad monoystorfa/amlystorfa'n masnachu hwylustod traws-brosiect yn erbyn annibyniaeth tîm. Dewiswch yr un sy'n paru â pha mor dynn y mae eich cod wedi'i gyplu mewn gwirionedd.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Pa wiriadau sy'n rhaid pasio cyn i unrhyw beth gyfuno i'ch prif linell warchodedig, ac a yw'r brif linell honno wir yn rhyddhadwy bob amser?** Mae'r bennod hon yn trin prif linell rhyddhadwy fel egwyddor graidd ac yn galw prif linell heb ei gwarchod, lle mae cod toredig neu heb ei adolygu'n cyrraedd y gangen y mae pawb yn dibynnu arni, yn wrth-batrwm. Ar dîm mawr mae prif linell goch yn rhwystro pawb ar unwaith, felly mae'r giât rydych yn ei mynnu'n briodwedd diogelwch a rennir, nid un bersonol. Dewch â'r dystiolaeth: beth mae eich diogelwch cangen yn ei orfodi mewn gwirionedd heddiw, a pha mor aml y mae'r brif linell wedi torri ar hyn o bryd. Penderfynwch ar y set ofynnol, profion sy'n pasio, sganiau diogelwch, ac adolygiad, a gwnewch y brif linell yn rhyddhadwy drwy bolisi yn hytrach na thrwy obaith. Dyna'r giât sy'n gadael i lawer o bobl integreiddio'n barhaus heb ofn.

2. **A yw mabwysiadu cyflwyniadau confensiynol yn werth gorbenion y confensiwn i'ch tîm, o ystyried yr hyn y mae'n ei awtomeiddio?** Mae'r bennod yn argymell negeseuon cyflwyno strwythuredig, y gellir eu dosrannu gan beiriant, yn union am eu bod yn eich galluogi i awtomeiddio cofnodion newid a fersiynu, ac mae'n gofyn am gyflwyniadau atomig fel bod hanes yn aros yn ddwy-rannadwy ac yn ddadwneadwy. Mae'r cyfaddawd yn real: rydych yn talu confensiwn ymlaen llaw ac angen gorfodi, yn gyfnewid am nodiadau rhyddhau a gynhyrchir a hanes dibynadwy. Dewch â'r signal o beth rydych yn ei wneud â llaw heddiw, fel ysgrifennu cofnodion newid â llaw neu hela am ba gyflwyniad a gyflwynodd atchweliad. Os ydych yn rhyddhau'n aml neu'n cynnal sawl fersiwn, mae'r awtomeiddio fel arfer yn talu amdano'i hun; os ydych yn anaml yn torri rhyddhadau, gall confensiwn ysgafnach fod yn ddigon. Gadewch i fachau a CI orfodi'r fformat fel nad yw'n dibynnu ar gof.

3. **A ydych wedi derbyn y gost weithredol y mae eich strwythur ystorfa'n ei mynnu, boed yn offer monoystorfa neu'n gydgysylltu traws-ystorfa?** Mae'r bennod hon yn dweud bod monoystorfa ac amlystorfa'n gweithio ar raddfa, a mai'r dewis anghywir ar gyfer eich patrwm cyplu sy'n creu ffrithiant cyson. Mae angen offer adeiladu ar raddfa fawr a rheolaeth mynediad manylach ar fonoystorfa, tra bo amlystorfeydd yn gwneud unrhyw newid sy'n rhychwantu ystorfeydd yn brosiect cydgysylltu gyda risg gwyriad fersiwn. Dewch â'r signal diriaethol: pa mor aml y mae eich newidiadau'n croesi ffiniau prosiect, ac a all eich offer adeiladu a mynediad gario'r strwythur sydd gennych. Os yw newidiadau atomig traws-brosiect yn gyffredin, buddsoddwch mewn offer monoystorfa; os yw timau a gwasanaethau'n wirioneddol annibynnol, derbyniwch gost cydgysylltu traws-ystorfa yn fwriadol. Y pwynt yw paru strwythur â pha mor dynn y mae eich cod wedi'i gyplu mewn gwirionedd, yna cyllido'r offer y mae'r strwythur hwnnw'n ei fynnu.

4. **Pe bai manylyn adnabod byw yn cael ei gyflwyno i ystorfa brysur ar hyn o bryd, pa mor gyflym y byddech yn ei ganfod, ac a yw cylchdroi'n wirioneddol awtomatig yn hytrach na gobaith?** Mae'r bennod hon yn trin unrhyw gyfrinach sy'n cyrraedd hanes fel un wedi'i chyfaddawdu ac yn rhybuddio bod ei thynnu'n ddiweddarach yn anodd ac yn annibynadwy, felly atal a chylchdroi cyflym yw'r unig amddiffynfeydd gwirioneddol. I dîm mawr mae'r amlygiad yn cronni: mae cyfrinach a wthiwyd i ystorfa a rennir yn cael ei chlonio ar ddwsinau o beiriannau a'i drychu i mewn i gaches CI o fewn munudau, felly mae ymateb dynol araf yn gwarantu toriad. Yr ystyriaeth gystadleuol yw ffrithiant: mae sganio cyn-cyflwyno ymosodol a chylchdroi gorfodol yn arafu pobl ac yn cynhyrchu positifau ffug, felly rhaid i chi diwnio'r rheolaethau yn hytrach na'u diffodd. Dewch â'r dystiolaeth: a yw sganio cyfrinachau'n rhedeg mewn bachau cyn-cyflwyno a CI ill dau, eich amser cymedrig i ganfod a chylchdroi gollyngiad hysbys, ac a oes gan beirianwyr hyd yn oed system rheoli cyfrinachau sy'n dileu'r temtasiwn i godio'n galed. Mewn lleoliadau menter a llywodraeth, cysylltwch hyn â'ch proses ddigwyddiad a'ch rheolau cadw, oherwydd mae manylyn adnabod a ollyngwyd mewn hanes archwiliadwy yn ddigwyddiad diogelwch a chydymffurfiaeth ill dau, a bydd y rheoleiddiwr yn gofyn pwy oedd yn gwybod a pha mor gyflym y gweithredon nhw.

5. **A yw eich canghennau'n wirioneddol fyrhoedlog, a lle nad ydynt, pam mae gwaith heb ei orffen wedi'i barcio ar gangen yn lle ei guddio y tu ôl i faner nodwedd?** Mae'r bennod yn gogwyddo'n galed tuag at ddatblygu seiliedig ar gefn oherwydd mai gwyriad hir yw gwraidd poen cyfuno, ac mae'n cynnig baneri nodwedd fel y mecanwaith sy'n gadael i chi gyfuno gwaith anghyflawn yn ddiogel yn lle ei ynysu am wythnosau. Ar dîm mawr mae hon yn briodwedd gydgysylltu, nid dewisiadau personol: mae pob cangen sy'n para am wythnosau'n dod yn fforc breifat o realiti y mae'n rhaid i rywun ei gymodi yn y pen draw, ac mae cost y cymodi hwnnw'n tyfu gyda nifer y staff. Yr ystyriaeth gystadleuol yw bod baneri nodwedd yn cario eu cost eu hunain, gan gynnwys cymhlethdod amser rhedeg, cyfuniadau profi, a baneri henaidd y mae'n rhaid eu diddymu. Dewch â'r data: dosbarthiad gwirioneddol oesoedd eich canghennau, pa mor aml y mae integreiddio'n cynhyrchu gwrthdrawiadau neu syrpreisys, a faint o ganghennau hirhoedlog sy'n bodoli ar hyn o bryd a pham. I sefydliad mawr neu reoleiddiedig, ychwanegwch y darlun rhyddhau, gan y gall cefnogaeth aml-fersiwn wirioneddol gyfiawnhau canghennau rhyddhau hirhoedlog gydag ôl-borthio disgybledig, ac mae hynny'n benderfyniad gwahanol i barcio gwaith nodwedd dydd-i-ddydd oddi ar y brif linell.

6. **A ellir olrhain pob newid yn eich hanes yn ôl at ei awdur a'i resymeg o fewn y ffiniau diogelwch cywir, ac a fyddai hynny'n gwrthsefyll archwiliad?** Mae'r bennod hon yn trin rheolaeth mynediad, lleiaf braint, a chysylltu newidiadau ag eitemau gwaith fel rhan o fframwaith rheolaeth y sefydliad, nid sglein dewisol. I dîm mawr, olrheiniadwyedd yw'r hyn sy'n troi ffrwd anhryloyw o gyflwyniadau'n rhywbeth y gallwch resymu drosto yn ystod digwyddiad neu adolygiad cydymffurfiaeth, a ffiniau mynediad yw'r hyn sy'n atal un cyfrif wedi'i gyfaddawdu rhag cyrraedd cod na ddylai byth ei gyffwrdd. Yr ystyriaeth gystadleuol yw cyflymder datblygwr: mae dolenni eitem waith gorfodol, caniatâd manwl, ac adolygiadau gofynnol yn ychwanegu seremoni y gallai tîm bach, cyflym symud ei hepgor yn rhesymol. Dewch â'r dystiolaeth: a yw canghennau gwarchodedig yn mynnu'r gwiriadau a'r adolygiadau rydych yn eu hawlio, a yw cyflwyniadau'n cyfeirio at eitemau gwaith cymeradwy mewn gwirionedd, a sut mae mynediad yn mapio i'ch ffiniau diogelwch gwirioneddol heddiw. Mewn cyd-destunau menter a llywodraeth, cysylltwch hyn â dosbarthiad, cadw, a rhwymedigaethau archwilio, oherwydd mae hanes na ellir ei archwilio neu ganiatâd mynediad rhy eang yn dod yn ganfyddiad a all atal rhaglen neu fethu achrediad.

## Lens sector

**Cwmni newydd.** Cyflymder a goroesiad sy'n ennill. Defnyddiwch un ystorfa, gweithiwch yn seiliedig ar gefn, cyfunwch ganghennau byrhoedlog sawl gwaith y dydd, a chuddiwch waith heb ei orffen y tu ôl i faneri nodwedd syml yn hytrach na changhennau hir. Trowch sganio cyfrinachau ymlaen o'r cyflwyniad cyntaf un, oherwydd gall allwedd a ollyngwyd mewn ystorfa gyhoeddus suddo cwmni heb dîm diogelwch i'w chynnwys. Hepgorwch fodelau cangheniad cywrain a phroses drwm; mae prif gangen warchodedig a negeseuon cyflwyno ystyrlon yn ddigon o ddisgyblaeth i symud yn gyflym.

**Busnes bach.** Heb arbenigwr platfform neu DevOps pwrpasol a chyllideb dynn, prynwch y rhagosodiadau a reolir yn hytrach na'u hadeiladu. Mae darparwr Git wedi'i letya'n rhoi i chi ddiogelwch cangen, adolygiadau gofynnol, a sganio cyfrinachau yn syth o'r bocs, felly pwyswch ar y rheiny yn hytrach na hunan-letya gweinydd na allwch ei gynnal. Fframiwch y penderfyniad fel hylendid data: gwybyddwch pa ystorfeydd sy'n dal ffurfweddiad sensitif, cadwch fanylion adnabod yng nghyfrinachwr y darparwr, a gadewch i'r platfform orfodi'r ychydig reolau sydd eu gwir angen arnoch.

**Menter.** Y broblem galed yw cysondeb ar draws llawer o dimau. Safonwch ddiogelwch cangen, confensiynau cyflwyno, a sganio cyfrinachau fel polisi ar draws y sefydliad fel bod grwpiau'n stopio'u hailddyfeisio, a gwnewch y dewis monoystorfa-yn-erbyn-amlystorfa'n fwriadol fesul patrwm cyplu, gan gyllido'r offer adeiladu ar raddfa fawr neu'r cydgysylltu traws-ystorfa y mae'n ei fynnu. Cyfeiriwch newidiadau at yr adolygwyr cywir â rheolau perchnogaeth cod, cysylltwch gyflwyniadau ag eitemau gwaith er mwyn olrheiniadwyedd, a thriniwch hylendid rheolaeth fersiynau fel rheolaeth lywodraethedig gyda pherchnogion a metrigau yn hytrach na mater o arferiad unigol.

**Llywodraeth.** Mae rheolau caffael, tryloywder, ac atebolrwydd cyhoeddus yn siapio'r cyfan. Mynnwch fod pob cyflwyniad yn cyfeirio at eitem waith gymeradwy, rheolwch fynediad fesul ffin dosbarthiad, a gwnewch sganio cyfrinachau a chylchdroi ar unwaith yn orfodol o dan broses ddigwyddiad wedi'i dogfennu. Cefnogwch sawl fersiwn wedi'u defnyddio â changhennau rhyddhau hirhoedlog ac ôl-borthio disgybledig lle na all pob safle uwchraddio ar unwaith, a chadwch hanes yn archwiliadwy ac wedi'i gadw fel y gellir ateb ceisiadau achrediad, rhyddid gwybodaeth, a goruchwyliaeth heb sgrialu.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd tri pherson yn gweithio'n seiliedig ar gefn o arferiad ac o reidrwydd fel ei gilydd, gan gyfuno canghennau byrhoedlog i mewn i main sawl gwaith y dydd a chuddio nodweddion hanner-orffenedig y tu ôl i faneri syml. Maent yn troi sganio cyfrinachau ymlaen yn CI o'r cyflwyniad cyntaf, oherwydd gallai allwedd API a ollyngwyd mewn ystorfa gyhoeddus suddo cwmni nad oes ganddo dîm diogelwch i gynnwys y canlyniadau. Mae un ystorfa, prif gangen warchodedig, a negeseuon cyflwyno ystyrlon yn rhoi digon o ddisgyblaeth iddynt symud yn gyflym heb faglu dros eu hanes eu hunain.

**Menter.** Mae cwmni technoleg mawr yn rhedeg monoystorfa gyda channoedd o wasanaethau a llyfrgelloedd a rennir. Mae offer adeiladu ar raddfa fawr a rheolau perchnogaeth cod yn cyfeirio pob newid at yr adolygwyr cywir. Gall un cyflwyniad ddiweddaru llyfrgell a rennir a phob defnyddiwr ar unwaith yn atomig, gan osgoi'r problemau gwyriad fersiwn sy'n poeni ystorfeydd dosbarthedig. Mae datblygu seiliedig ar gefn â baneri nodwedd yn cadw'r brif linell yn rhyddhadwy, ac mae sganio cyfrinachau'n blocio manylion adnabod ar amser cyflwyno ar draws yr ystorfa gyfan.

**Llywodraeth.** Mae contractwr amddiffyn cenedlaethol yn cadw at olrheiniadwyedd llym. Rhaid i bob cyflwyniad gyfeirio at eitem waith gymeradwy. Mae diogelwch cangen yn mynnu sganiau diogelwch sy'n pasio ac adolygiad annibynnol, ac mae mynediad wedi'i reoli'n dynn fesul ffin dosbarthiad. Mae sganio cyfrinachau'n orfodol, ac mae unrhyw fanylyn adnabod sydd wedi'i amlygu'n sbarduno cylchdroi ar unwaith o dan broses ddigwyddiad. Mae canghennau rhyddhau hirhoedlog yn cefnogi sawl fersiwn wedi'u defnyddio ar draws safleoedd na all bob un uwchraddio ar unwaith, gydag ôl-borthio disgybledig o gywiriadau diogelwch.

## Achos busnes: cymhellion, ROI, a TCO

Mae rheoli ffynhonnell cadarn bron yn ddi-gost i'w fabwysiadu ac yn ddrud i fynd hebddo. Mae datblygu seiliedig ar gefn ac integreiddio parhaus ymhlith yr arferion sy'n gysylltiedig gryfaf â pherfformiad cyflenwi meddalwedd uchel, sydd yn ei dro'n cydberthyn â chanlyniadau sefydliadol gwell. Mae hanes glân, olrheiniadwy'n torri'r amser y mae'n ei gymryd i ddiagnosio digwyddiadau a bodloni archwiliadau, ac mae cangheniad disgybledig yn eich arbed rhag cost gylchol, heb ei chyllidebu, argyfyngau integreiddio a marathonau cyfuno.

Y risg fwyaf anghymesur yw cyfrinachau mewn rheolaeth fersiynau. Gall un manylyn adnabod a ollyngwyd achosi toriad y mae ei gost yn crebachu unrhyw fuddsoddiad offer, ac mae hanes yn gwneud i ollyngiadau o'r fath aros o gwmpas. Mae eu hatal yn rhad; nid yw glanhau ar eu hôl. Mae dewisiadau strwythur gwael yn ymddangos fel ffrithiant cronig: mae pob newid traws-ystorfa'n dod yn brosiect cydgysylltu, neu mae pob adeilad monoystorfa'n dod yn dagfa. I wneud yr achos i arweinyddiaeth, cysylltwch eich strategaeth gangheniad â metrigau cyflenwi ac amser diagnosio digwyddiadau, a fframiwch sganio cyfrinachau a rheolaeth mynediad fel rheolaethau cost isel yn erbyn risg toriad ac archwilio cost uchel.

## Gwrth-batrymau a pheryglon

- **Canghennau gwyriedig hirhoedlog:** wythnosau o waith ynysig sy'n cyfuno i mewn i ddigwyddiadau integreiddio poenus, peryglus.
- **Cyfrinachau mewn hanes:** manylion adnabod wedi'u codio'n galed sy'n parhau mewn clonau am byth ac sy'n gofyn am gylchdroi ar ôl eu hamlygu.
- **Cyflwyno deuaidd mawr i'r prif hanes:** chwyddo pob clôn yn barhaol ac arafu pob gweithred.
- **Negeseuon cyflwyno di-ystyr:** "fix", "wip", "changes" sy'n dinistrio gwerth hanes fel dogfennaeth.
- **Cyflwyno cod a gynhyrchwyd fel pe bai wedi'i ysgrifennu â llaw:** gwahaniaethau swnllyd, gwrthdrawiadau cyfuno, a dryswch ynghylch ffynhonnell y gwir.
- **Strwythur ystorfa anghywir ar gyfer y cyplu:** amlystorfeydd ar gyfer cod wedi'i gyplu'n dynn, neu fonoystorfeydd heb offer ar raddfa fawr.
- **Prif linell heb ei gwarchod:** dim gwiriadau gofynnol, felly mae cod toredig neu heb ei adolygu'n cyrraedd y gangen y mae pawb yn dibynnu arni.

## Model aeddfedrwydd

- **Lefel 1, Cychwyn:** Ad hoc ac adweithiol. Mae cangheniad yn fyrfyfyr, mae canghennau'n para am wythnosau, mae negeseuon cyflwyno'n dweud "fix" neu "wip", nid oes sganio cyfrinachau, ac mae integreiddio'n gwegian o un argyfwng cyfuno i'r llall.
- **Lefel 2, Datblygu:** Mae arferion sylfaenol yn ymddangos ond yn amrywio fesul tîm. Mae model cangheniad a chonfensiynau negeseuon yn bodoli mewn mannau, ac eto mae canghennau'n dal i fyw'n rhy hir, mae gorfodi'n rhannol, mae sganio cyfrinachau'n dameidiog, ac fe etifeddwyd strwythur ystorfa yn hytrach na'i ddewis.
- **Lefel 3, Safoni:** Mae arferion wedi'u dogfennu a'u gorfodi ar draws y sefydliad: datblygu seiliedig ar gefn â changhennau byr, prif linell warchodedig sy'n rhyddhadwy bob amser, confensiynau cyflwyno gorfodedig, sganio cyfrinachau mewn bachau a CI ill dau, mynediad lleiaf braint, a dewis monoystorfa neu amlystorfa bwriadol.
- **Lefel 4, Rheoli:** Mesurir a rheolir arferion ffynhonnell â data. Rydych yn tracio oes cangen, amlder integreiddio, cyfradd torri prif linell, amser cymedrig i ganfod a chylchdroi cyfrinach a ollyngwyd, ac olrheiniadwyedd newid-i-eitem-waith yn erbyn llinellau sylfaen cytunedig, ac rydych yn gweithredu pan fydd y rhifau'n drifftio yn hytrach nag aros am y digwyddiad nesaf.
- **Lefel 5, Cydgysylltu:** Gwellir ac integreiddir arferion yn barhaus ar draws y sefydliad. Mae cangheniad, strwythur ystorfa, ac offer yn addasu wrth i dimau a chyplu cod newid, mae awtomeiddio'n gorfodi hylendid o'r dechrau i'r diwedd, ac mae data rheolaeth fersiynau'n bwydo penderfyniadau cyflenwi, diogelwch, a risg ar draws y sefydliad.

## Syniadau ar gyfer trafodaeth

- A yw oes cangen eich tîm yn wirioneddol fyr, ac os na, beth sy'n atal integreiddio parhaus?
- A yw eich dewis monoystorfa neu amlystorfa'n paru â pha mor gyplog yw eich cod mewn gwirionedd?
- Sut ydych chi'n trin deuaidd mawr ac arteffactau a gynhyrchwyd heddiw, a beth mae'n ei gostio i chi?
- Beth fyddai'n digwydd pe bai manylyn adnabod byw yn cael ei gyflwyno nawr, a pha mor gyflym y byddech yn ei ganfod a'i gylchdroi?
- Faint o ddisgyblaeth neges-gyflwyno ac olrheiniadwyedd sy'n werth ei gorfodi ar gyfer eich cyd-destun?
- Sut mae baneri nodwedd yn newid eich strategaeth gangheniad, a pha risgiau newydd y maent yn eu cyflwyno?

## Prif negeseuon

- Integreiddiwch yn aml â changhennau byrhoedlog; mae gwyriad hir yn achosi'r boen y mae'n ymddangos ei fod yn ei osgoi.
- Cadwch y brif linell yn rhyddhadwy ac wedi'i gwarchod gan wiriadau gofynnol.
- Peidiwch byth â gadael i gyfrinachau fynd i mewn i hanes; sganiwch yn awtomatig a chylchdrowch ar unwaith os digwydd hynny.
- Dewiswch fonoystorfa neu amlystorfa yn ôl eich anghenion cyplu a chydgysylltu gwirioneddol.
- Triniwch hanes cyflwyno fel dogfennaeth, gyda chyflwyniadau ystyrlon, confensiynol, atomig.

## References and further reading

- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Jez Humble and David Farley, *Continuous Delivery*
- Scott Chacon and Ben Straub, *Pro Git*
- Paul Hammant and others, writings on trunk-based development
- Conventional Commits specification (as a reference standard)
- Martin Fowler, articles on branching patterns and continuous integration
