# 2.12 Modelau a dulliau meddalwedd

## Trosolwg a chymhelliant

Symleiddiad bwriadol o system yw model meddalwedd, wedi'i adeiladu i ateb cwestiwn penodol. Ffordd ddisgybledig o gynhyrchu meddalwedd yw dull, gan gynnwys y modelau y mae'n eu defnyddio ar hyd y ffordd. Gyda'i gilydd maent yn ffurfio maes gwybodaeth Corff Gwybodaeth Peirianneg Meddalwedd (SWEBOK), oherwydd dyma'r offer meddyliol rydych yn eu defnyddio i resymu am system cyn, yn ystod, ac ar ôl i chi ei hadeiladu. Mae diagram dosbarth UML ([Iaith Fodelu Unedig](https://en.wikipedia.org/wiki/Unified_Modeling_Language)), [diagram perthynas-endid](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) (ERD), [peiriant cyflwr](https://en.wikipedia.org/wiki/Finite-state_machine), [manyleb ffurfiol](https://en.wikipedia.org/wiki/Formal_specification), a phrototeip taflu-i-ffwrdd i gyd yn fodelau. Mae [Waterfall](https://en.wikipedia.org/wiki/Waterfall_model), [prototeipio](https://en.wikipedia.org/wiki/Software_prototyping), datblygu ffurfiol, ac [ystwyth](https://en.wikipedia.org/wiki/Agile_software_development) i gyd yn ddulliau.

Pam trafferthu â modelau o gwbl? Oherwydd bod cof gwaith dynol yn fach a systemau meddalwedd yn fawr. Ni all neb ddal system can mil o linellau yn ei ben, felly rydym yn tynnu lluniau ac yn ysgrifennu haniaethau sy'n dangos un agwedd ar y tro: y data, llif rheolaeth, y cyflyrau, y rhyngweithiadau. Nid yw model byth i fod yn ffyddlon i'r cod; mae i fod yn addas ar gyfer penderfyniad. Mae model da'n dangos yn union yr hyn sydd angen i chi ei benderfynu am rywbeth, ac yn cuddio popeth arall.

Ar dimau mawr, cydgysylltu a chyfathrebu yw'r risg gwirioneddol. Pan fydd cannoedd o beirianwyr, penseiri, dadansoddwyr, ac archwilwyr yn gweithio ar un system, modelau a rennir yw'r tir cyffredin lle maent yn negodi dyluniad, gofynion, a risg. Felly meddyliwch am fodelu fel offeryn sydd â swydd i'w gwneud. Mae'n talu ar ei ganfed pan fo model yn rhatach na'r camgymeriad y mae'n ei atal. Mae'n dod yn wastraff pan fyddwch yn ei dynnu er ei fwyn ei hun, yn ei gadw ymhell wedi iddo fynd yn hen, neu'n ei ymhelaethu y tu hwnt i'r penderfyniad yr oedd i fod i'w wasanaethu. Mae modelu'n cysylltu'n dynn â gofynion meddalwedd (pennod 2.8), egwyddorion dylunio meddalwedd (pennod 2.2), pensaernïaeth a'i nodiannau megis C4 ac arc42 (pennod 3.1), a ffyrdd ystwyth o weithio (pennod 10.7).

## Egwyddorion allweddol

- Mae gan bob model bwrpas; os na allwch enwi'r penderfyniad y mae model yn ei hysbysu, peidiwch â'i dynnu.
- Haniaeth yw prif weithred modelu: cynhwyswch yr hyn sy'n bwysig ar gyfer y pwrpas, hepgorwch y gweddill.
- Mae cysondeb yn bwysig o fewn ac ar draws modelau; mae modelau gwrthddweud yn waeth na dim.
- Mae modelau'n arteffactau cyfathrebu yn gyntaf; mae eu cynulleidfa'n penderfynu eu nodiant a'u manylder.
- Ffafriwch y model ysgafnaf sy'n ateb y cwestiwn; mae gan ymhelaethu gost cario.
- Mae model cystal â'i ddadansoddiad yn unig; mae model heb ei wirio yn dybiaeth heb ei brofi.
- Dewiswch y dull i gyfateb ansicrwydd y broblem, ei risg, a chanlyniad methiant.

## Argymhellion

### Modelwch ag haniaeth, pwrpas, a chysondeb

Dechreuwch bob model drwy enwi ei bwrpas a'i gynulleidfa. Yna haniaethwch yn ddidrugaredd tuag at y pwrpas hwnnw: dylai diagram dilyniant sydd i fod i ddatrys cyflwr ras ddangos amseriad a negeseuon, nid pob maes. Cadwch eich modelau'n gyson â'i gilydd, fel bod yr endidau mewn ERD, y dosbarthiadau mewn diagram dosbarth, a'r enwau yn y gofynion i gyd yn cytuno, ac yn gyson â realiti, sy'n golygu eich bod yn diweddaru neu'n dileu model pan fydd y system yn symud ymlaen. Mae model hen y mae pobl yn ymddiried ynddo'n berygl. Mae model hen y mae pawb yn ei anwybyddu'n wastraff sy'n dal i gostio sylw.

### Dewiswch fodelau strwythurol neu ymddygiadol i gyfateb y cwestiwn

Defnyddiwch fodelau strwythurol i ddangos beth mae system wedi'i wneud ohono a sut mae'r rhannau'n perthyn: diagramau dosbarth, diagramau cydran, a diagramau perthynas-endid ar gyfer strwythur data. Defnyddiwch fodelau ymddygiadol i ddangos beth mae system yn ei wneud dros amser: peiriannau cyflwr ar gyfer gwrthrychau â chylchoedd oes ystyrlon, diagramau dilyniant ar gyfer rhyngweithiadau ar draws cydrannau, a diagramau gweithgaredd ar gyfer llifau gwaith a phrosesau busnes. Dewiswch yr un nodiant sy'n amlygu'r penderfyniad sydd o'ch blaen. Nid oes angen ond llond dwrn o fathau diagram ar y rhan fwyaf o systemau, wedi'u tynnu'n ddetholus, nid y catalog UML llawn wedi'i gymhwyso i bopeth.

### Dadansoddwch fodelau, peidiwch â'u tynnu'n unig

Mae model yn ennill ei le drwy ddadansoddiad, nid dim ond drwy dynnu. Gwiriwch beiriant cyflwr am gyflyrau na ellir eu cyrraedd, trosiadau coll, ac argyfwng. Gwiriwch ERD am broblemau normaleiddio a pherthnasoedd amddifad. Cerddwch ddiagram dilyniant yn erbyn y gofynion i ddod o hyd i lwybrau gwall coll. Adolygwch eich modelau gyda'r arbenigwyr parth a all sbotio beth sy'n anghywir. A lle mae cost methiant yn uchel, estynnwch am ddadansoddiad wedi'i gefnogi gan declyn (gwiriwyr model, gwiriwyr cysondeb, efelychiad) yn hytrach na'i lygadu.

### Cymhwyswch ddulliau heuristig fel y rhagosodiad

Adeiladir y rhan fwyaf o feddalwedd â dulliau heuristig: dulliau seiliedig ar brofiad, ailadroddol sy'n defnyddio modelau'n anffurfiol ac yn barnu canlyniadau yn erbyn disgwyliadau yn hytrach na phrofion. Ar gyfer y rhan fwyaf o systemau busnes a llywodraeth, mae hynny'n union gywir: mae gofynion yn esblygu, ac mae nam fel arfer yn adferadwy. Mae dulliau heuristig yn paru'n naturiol ag ystwyth (pennod 10.7): modelwch ddigon i gysoni'r tîm, yna adeiladwch a dysgwch.

### Cadwch ddulliau ffurfiol ar gyfer craidd canlyniad-uchel

Mae [dulliau ffurfiol](https://en.wikipedia.org/wiki/Formal_methods) yn mynegi manylebau mewn mathemateg ac yn defnyddio dilysu, boed brawf neu [wirio model](https://en.wikipedia.org/wiki/Model_checking) trylwyr, i sefydlu priodweddau. Maent yn costio sgil ac amser gwirioneddol, ac maent yn talu ar ei ganfed yn union lle mae methiant yn drychinebus neu'n anwrthdroadwy: rheolaeth ddiogelwch-argyfyngus, protocolau cryptograffig, craidd setliad ariannol, a'r fath. Cymhwyswch nhw i'r craidd critigol bach, nid y system gyfan. A sylwch fod manyleb ffurfiol yn unig, hyd yn oed heb brawf llawn, yn aml yn ychwanegu gwerth dim ond drwy eich gorfodi i fod yn union.

### Defnyddiwch brototeipio i ymddeol ansicrwydd

Pan fo gofynion neu ymarferoldeb yn aneglur, adeiladwch brototeip i ddysgu, yna penderfynwch, yn fwriadol, a ddylid ei esblygu neu ei daflu. Mae prototeipiau taflu-i-ffwrdd yn archwilio cwestiwn yn rhad ac yna'n cael eu dileu. Mae prototeipiau esblygol yn dod yn gynnyrch a rhaid iddynt gael eu hadeiladu i safonau cynhyrchu. Y methiant clasurol yw gadael i brototeip taflu-i-ffwrdd lithro i mewn i gynhyrchu drwy ddamwain. Felly enwch fath y prototeip cyn i chi ei adeiladu.

### Cyfatebwch y dull â risg, nid ffasiwn

Dewiswch ddulliau yn ôl ansicrwydd y broblem a chanlyniad methiant. Mae ansicrwydd uchel yn ffafrio prototeipio ac ailadrodd ystwyth. Mae canlyniad uchel yn ffafrio dadansoddiad ffurfiol a dilysu trylwyr. Mae angen craidd ffurfiol critigol o fewn amlen ystwyth fel arall ar system â'r ddau. Beth bynnag a wnewch, peidiwch â mabwysiadu dull dim ond oherwydd ei fod yn fri neu oherwydd bod gwerthwr yn ei werthu.

## Cyfaddawdau: manteision ac anfanteision

| Model neu ddull | Wedi'i gymhwyso'n dda | Modd methiant |
|---|---|---|
| Modelau strwythurol (UML, ERD) | Llun a rennir o rannau a data | Ymledu diagram; drifft o'r cod |
| Modelau ymddygiadol (cyflwr, dilyniant, gweithgaredd) | Amlygu amseriad, cyflyrau, ac achosion ymyl | Diagramau gor-fanwl nad oes neb yn eu darllen |
| Dulliau heuristig | Cyflym, hyblyg, yn addas ar gyfer y rhan fwyaf o systemau | Anddisgybledig; tybiaethau cudd |
| Dulliau ffurfiol | Priodweddau profadwy ar gyfer creiddiau critigol | Cost uchel; wedi'u camgymhwyso i'r system gyfan |
| Prototeipio | Dysgu rhad; yn ymddeol risg yn gynnar | Cod taflu-i-ffwrdd wedi'i ddyrchafu i gynhyrchu |
| Dulliau ystwyth | Yn addasu i ofynion sy'n newid | Yn sgipio modelu sydd ei angen ar gyfer problemau anodd |

Y tensiwn ailadroddol yw rhwng trylwyredd a chyflymder. Mae rhy ychydig o fodelu'n anfon tybiaethau cudd i gynhyrchu. Mae gormod o fodelu'n llosgi ymdrech ar ddiagramau nad ydynt byth yn hysbysu penderfyniad ac yn pydru y foment y mae'r cod yn newid. Nid oes dos sefydlog sy'n trwsio hyn, dim ond rheol cyfrannedd: buddsoddwch mewn model neu ddull yn gyfrannol â'r ansicrwydd y mae'n ei ddatrys a chost cael y penderfyniad yn anghywir. Mae peiriant taliadau a microwefan farchnata'n haeddu triniaeth wahanol.

## Cwestiynau i'w trafod gyda'ch tîm

1. **A ydym yn dadansoddi ein modelau, neu ai dim ond eu tynnu a symud ymlaen a wnawn?** Mae model yn ennill ei le drwy ddadansoddiad, nid drwy fodoli: mae peiriant cyflwr na wiriwch byth am gyflyrau na ellir eu cyrraedd na throsiadau coll yn dybiaeth heb ei phrofi wedi'i gwisgo fyny fel diagram. Ar dîm mawr dyma lle mae namau gwirioneddol yn cuddio, oherwydd bod llun sy'n edrych yn gredadwy'n cael ei ymddiried ynddo'n union pan nad oes neb wedi'i gerdded yn erbyn y gofynion i ddod o hyd i'r llwybr gwall coll neu'r berthynas amddifad. Dewch â'ch model ymddygiadol pwysicaf i'r cyfarfod a cheisiwch ei dorri: pa drosiad sy'n annelwig, pa gyflwr nad oes ganddo allanfa, pa ddilyniant nad oes ganddo derfyn amser? Lle mae cost methiant yn uchel, dylai'r ateb eich gwthio tuag at ddadansoddiad wedi'i gefnogi gan declyn (gwiriwyr model, gwiriwyr cysondeb, efelychiad) yn hytrach na llygadu, oherwydd mai holl reswm modelu craidd critigol yw dod o hyd i'r diffyg ar fwrdd gwyn yn hytrach nag mewn cynhyrchu.

2. **Pan fydd dau o'n modelau'n anghytuno, pa un sy'n ennill, a phwy sy'n sylwi ar y gwrthddweud?** Mae cysondeb yn bwysig o fewn ac ar draws modelau, ac mae modelau gwrthddweud yn waeth na dim, oherwydd bod pobl yn gweithredu ar y ddau. Ar system fawr mae'r endidau yn y model data, y dosbarthiadau yn y dyluniad, a'r enwau yn y gofynion yn drifftio ar wahân yn dawel wrth i wahanol dimau ddiweddaru gwahanol arteffactau, a'r arwydd cyntaf yn aml yw bwg cynhyrchu lle mae dau gydran yn anghytuno ynghylch beth yw peth. Dewch ag enghraifft: dewiswch gysyniad craidd a gwiriwch a yw'r ERD, y cod, a'r gofynion mewn gwirionedd yn cytuno ar ei siâp a'i gylchred oes. Os nad ydynt, penderfynwch pa arteffact sy'n awdurdodol a phwy sy'n gyfrifol am gadw'r lleill mewn cam, a byddwch yn barod i ddileu model yn hytrach na gadael i un hen barhau i gelwydda wrth y tîm.

3. **Pa graidd yn ein system, os yw'n anghywir, sy'n colli arian gwirioneddol neu'n niweidio rhywun, ac a yw'n cael y trylwyredd y mae'n ei haeddu?** Y symudiad canolog yn y bennod hon yw cyfateb y dull â risg: dulliau heuristig ac ystwyth ar gyfer y mwyafrif adferadwy, manyleb ffurfiol a dilysu ar gyfer y craidd canlyniad-uchel bach, a phrototeipio rhad ar gyfer yr hyn sy'n wir ansicr. Mae'r moddau methiant yn symetrig ac yn ddrud i'r ddau: mae cymhwyso dulliau ffurfiol at ficrowefan farchnata'n llosgi arian, ac mae trin peiriant setliad neu set rheolau cymhwysedd fel gwaith ystwyth cyffredin yn gwahodd y nam trychinebus, anwrthdroadwy. Dewch â map o'ch system a marciwch lle mae gwall yn drychinebus yn erbyn adferadwy, a lle mae gofynion yn sicr yn erbyn anhysbys. Dylai'r ateb ganolbwyntio eich buddsoddiad modelu lle mae'r arian a'r amwysedd, a'i atal yn benodol ym mhobman arall, fel y gall craidd ffurfiol critigol eistedd o fewn amlen ystwyth fel arall heb i'r un o'r dulliau ollwng i diriogaeth y llall.

4. **Faint o fodelu rydym yn ei wneud cyn ysgrifennu cod, ac a yw'r dos hwnnw'n newid gyda'r ansicrwydd sydd o'n blaenau?** Mae dyluniad mawr ymlaen llaw a dim dyluniad o gwbl yn ddau fodd methiant, ac mae'r dos cywir yn eistedd rhyngddynt, wedi'i lywodraethu gan faint o ansicrwydd y mae model yn wir yn ei ymddeol. Ar dîm mawr mae'r pwysau'n rhedeg y ddwy ffordd: gall proses lywodraethu fynnu set lawn o ddiagramau cyn unrhyw god, gan gloi penderfyniadau a wnaed gyda'r wybodaeth leiaf, tra gall pwysau traddodi wthio tîm i sgipio'r un peiriant cyflwr a fyddai wedi dal achos ymyl costus. Dewch â'ch dau brosiect diwethaf a didolwch y modelau a gynhyrchoch yn rhai a hysbysodd benderfyniad gwirioneddol a rhai a dynnwyd dim ond oherwydd bod templed yn gofyn amdanynt. Mewn rhaglenni menter a llywodraeth, lle mae gât gam neu fwrdd cymeradwyo'n aml yn mynnu dogfennau ymlaen llaw, dewch yn barod i ddadlau dros fodelu sy'n olrhain risg yn hytrach na rhestr gyflenwi sefydlog, fel bod y craidd taliadau'n cael ei drylwyredd a'r teclyn adrodd mewnol ddim yn boddi mewn diagramau nad oes neb yn eu darllen.

5. **A ydym wedi cytuno ar nodiant a rennir a chartref sengl ar gyfer ein modelau, neu a yw pob tîm yn dyfeisio ei un ei hun?** Mae modelau'n arteffactau cyfathrebu yn gyntaf, ac mae eu gwerth yn dymchwel pan na all peiriant cyflwr wedi'i dynnu yn nheclyn un tîm gael ei ddarllen, ei ganfod, neu ei ymddiried ynddo gan y tîm sy'n ei etifeddu. I gannoedd o beirianwyr mae'r ystyriaethau cystadleuol yn wirioneddol: mae nodiant a storfa orfodol yn prynu cysondeb a darganfyddadwyedd, ond maent hefyd yn gosod cost dysgu ac yn gallu gwthio pobl tuag at offer trwm pan fyddai bwrdd gwyn wedi'i ffotograffu'n gwasanaethu. Dewch ag enghreifftiau o le'r oedd model wir yn byw (wici, teclyn diagram, cyflwyniad sleidiau, gliniadur rhywun) a gofynnwch pwy allai ddod o hyd iddo a'i ddeall chwe mis yn ddiweddarach. Mewn lleoliadau menter a reoledig mae'r ongl archwilio'n hogi hyn: bydd archwiliwr na all leoli'r model data cyfredol na olrhain penderfyniad yn ôl i beiriant cyflwr wedi'i ddogfennu yn trin y system fel un heb ei dogfennu, felly cytunwch ar nodiant a rennir bach a lleoliad parhaus, a derbyniwch ddal ysgafn dros seremoni lle bynnag y mae'r canlyniad yn isel.

6. **Cyn i ni adeiladu prototeip, a ydym yn penderfynu'n fwriadol ai taflu-i-ffwrdd neu esblygol ydyw, ac a ydym yn dal ein hunain i'r dewis hwnnw?** Y methiant clasurol, drud yw prototeip taflu-i-ffwrdd sy'n llithro'n dawel i mewn i gynhyrchu oherwydd ei fod wedi arddangos yn dda ac nid oedd neb wedi enwi ei fath ymlaen llaw. Mae'r tensiwn yn wirioneddol: mae prototeipiau taflu-i-ffwrdd yn prynu'r dysgu rhataf posibl a dylent gael eu dileu, tra bo prototeipiau esblygol yn dod yn gynnyrch a rhaid iddynt gael eu hadeiladu i safonau cynhyrchu o'r llinell gyntaf, ac mae drysu'r ddau naill ai'n gwastraffu ailwaith neu'n anfon cod bregus i rôl na chafodd ei beiriannu ar ei chyfer erioed. Dewch â phrototeip diweddar a gofynnwch beth benderfynwyd cyn iddo gael ei adeiladu, pwy oedd yn dal awdurdod i'w ddyrchafu neu ei daflu, ac a wnaeth y penderfyniad hwnnw oroesi pwysau traddodi. Mewn llywodraeth a lleoliadau atebol eraill, lle mae system wyneb-yn-wyneb-â-dinasyddion yn cario rhwymedigaethau tryloywder a dibynadwyedd, triniwch ddyrchafiad damweiniol fel methiant rheolaeth: penderfynwch dynged y prototeip ymlaen llaw, a gwnewch daflu i ffwrdd taflu-i-ffwrdd llwyddiannus yn ganlyniad dathliedig yn hytrach na gwastraff i'w osgoi.

## Lens sector

**Busnes newydd.** Modelwch ar fwrdd gwyn, tynnwch ffotograff ohono, a symud ymlaen. Eich adnodd prinnaf yw sylw peirianneg, felly estynnwch am fodel dim ond pan fo'n rhatach na'r camgymeriad y mae'n ei atal: peiriant cyflwr tanysgrifiad cyn i chi godio'r achosion ymyl bilio, nid catalog UML llawn ar gyfer cynnyrch a all droi mis nesaf. Arhoswch yn heuristig ac yn ystwyth, cadwch ddulliau ffurfiol yn gyfan gwbl oddi ar y bwrdd, a thriniwch bob prototeip fel taflu-i-ffwrdd oni bai eich bod yn penderfynu fel arall yn ymwybodol.

**Busnes bach.** Mae'n debyg nad oes gennych chi neb y mae ei swydd yn fodelu ffurfiol, felly pwyswch ar y modelau sydd eisoes wedi'u hymgorffori yn yr offer a'r fframweithiau rydych yn eu prynu yn hytrach na sefydlu arfer modelu eich hun. Fframiwch y ychydig fodelau rydych chi'n eu tynnu o amgylch penderfyniadau pendant: braslun model data syml i gytuno pa ddata cwsmer sydd gennych, diagram cyflwr ar gyfer yr un llif gwaith sy'n eich colli cwsmer pan fydd yn torri. Ffafriwch gynnyrch a brynwyd â model data profedig dros adeiladu a dogfennu eich un chi, a chadwch beth bynnag a dynnwch yn ddigon ysgafn i un person ei gynnal.

**Menter.** Y broblem graidd yw cydgysylltu ar draws llawer o dimau, felly mae modelau a rennir yn dod yn dir cyffredin: model data y cytunwyd arno, nodiant cyson, a chartref lle gellir dod o hyd i'r ERD, diagramau C4, a'r peiriannau cyflwr a'u hymddiried ynddynt. Safonwch nodiant bach a gorfodwch gysondeb fel nad yw'r endidau yn y gofynion, y dyluniad, a'r gronfa ddata'n drifftio ar wahân rhwng timau. Cadwch fanyleb ffurfiol a gwirio model ar gyfer y creiddiau canlyniad-uchel (setliad, cysoni, rheoli mynediad), ariannwch y sgil arbenigol y mae hynny'n ei fynnu, a chadwch lwybr archwilio o bob model wedi'i ddogfennu yn ôl i'r penderfyniad a'i cyfiawnhaodd.

**Llywodraeth.** Rhaid i reolau a osodwyd mewn cyfraith fod yn olrheiniadwy i statud, a dyma lle mae manyleb ffurfiol yn ennill ei chost: nodwch resymeg cymhwysedd neu asesu'n union, dilyswch briodweddau allweddol, a gadewch i archwilwyr olrhain pob canlyniad yn ôl i'r rheol a'i cynhyrchodd. Mae caffael yn ychwanegu ei bwysau ei hun, gan fod dogfennau a modelau'n aml yn gyflenwadau cytundebol, felly cytunwch pa fodelau sy'n wir yn dwyn penderfyniad yn hytrach na chael eu cynhyrchu dim ond i fodloni rhestr wirio. Cyhoeddwch ddisgrifiadau iaith blaen o sut mae systemau canlyniadol yn gweithio, a defnyddiwch brototeipio taflu-i-ffwrdd i brofi mewnbwn wyneb-yn-wyneb-â-dinasyddion â defnyddwyr gwirioneddol cyn ymrwymo i adeiladu cynhyrchu.

## Enghreifftiau

**Busnes newydd.** Mae busnes newydd bach sy'n adeiladu cynnyrch bilio tanysgrifiad yn braslunio cylchred oes y tanysgrifiad (prawf, gweithredol, hwyr-dalu, wedi'i ganslo, wedi'i ailactifadu) fel peiriant cyflwr ar fwrdd gwyn cyn ysgrifennu cod. Wrth gerdded y diagram, maent yn sylwi na wnaethant erioed ddiffinio beth sy'n digwydd pan fydd taliad cyfrif hwyr-dalu o'r diwedd yn clirio, achos ymyl a fyddai wedi gadael cwsmeriaid gwirioneddol yn sownd mewn limbo. Mae'r model pum munud hwnnw'n arbed cur pen cynhyrchu, ac maent yn ei ffotograffu yn hytrach na chynnal teclyn diagram trwm. Ym mhobman arall maent yn aros yn ystwyth ac yn modelu dim ond digon i gysoni, oherwydd ar eu graddfa mae nam yn adferadwy a byddai dulliau ffurfiol yn gost bur.

**Menter.** Mae banc byd-eang yn adeiladu platfform taliadau newydd. Mae'r tîm yn defnyddio diagram perthynas-endid i gytuno ar y model data a rennir ar draws y timau cyfrifon, cyfrifiadau, a negesu, a diagramau C4 (pennod 3.1) i ddangos sut mae'r gwasanaethau'n cyd-fynd. Maent yn modelu cylchred oes y trafodiad (yn hongian, wedi clirio, wedi setlo, wedi'i wrthdroi, dan ddadl) fel peiriant cyflwr eglur, ac mae dadansoddiad yn datgelu ei fod yn colli trosiad ar gyfer gwrthdroadau rhannol. Caiff y bwlch ei drwsio ar fwrdd gwyn yn hytrach na mewn cynhyrchu. Mae diagramau dilyniant yn cerdded y llif setliad yn erbyn y gofynion (pennod 2.8) i amlygu llwybrau terfyn amser ac ailgeisio coll. Mae traddodi bob dydd yn ystwyth, ond mae'r algorithm cysoni craidd, lle mae gwall yn golygu colli arian gwirioneddol, yn cael manyleb ffurfiol ac yn cael ei wirio fel model cyn gweithredu. Mae modelu wedi'i ganolbwyntio lle mae'r arian a'r amwysedd, ac yn ysgafn ym mhobman arall.

**Llywodraeth.** Mae asiantaeth dreth genedlaethol yn moderneiddio asesu budd-daliadau. Gan fod rheolau cymhwysedd wedi'u gosod mewn cyfraith ac wedi'u harchwilio, mae'r tîm yn ysgrifennu manyleb ffurfiol o'r rheolau fel trawsffurfiadau pur ac yn dilysu priodweddau allweddol, megis nad oes hawlydd yn gymwys ac yn anghymwys ar yr un pryd a bod pob achos yn cyrraedd penderfyniad, fel y gall archwilwyr olrhain canlyniadau yn ôl i statud. Ochr yn ochr â'r craidd ffurfiol, mae'r tîm yn adeiladu prototeip taflu-i-ffwrdd o'r ffurflen mewnbwn wyneb-yn-wyneb-â-dinasyddion i'w brofi â defnyddwyr gwirioneddol. Maent yn dysgu bod dewin aml-gam yn lleihau gwallau, yna'n taflu'r prototeip ac yn ailadeiladu'r mewnbwn i safonau cynhyrchu. Mae diagramau gweithgaredd yn dogfennu'r broses gweithiwr achos benagen ar gyfer hyfforddiant ac archwiliad. Mae'r rheolau canlyniad-uchel yn cael trylwyredd ffurfiol; mae'r profiad defnyddiwr ansicr yn cael prototeipio rhad; nid yw'r un dull yn cael ei gymhwyso lle mae'r llall yn perthyn.

## Achos busnes: cymhellion, ROI, a TCO

Daw'r enillion ar fodelu o ddod o hyd i namau'n gynharach, lle maent yn llawer rhatach i'w trwsio. Mae gwrthddweud a ganfyddir ar fwrdd gwyn yn costio munudau. Gall yr un gwrthddweud a ganfyddir mewn cynhyrchu gostio toriad, rhaglen ailwaith, neu, mewn parthau rheoledig, atebolrwydd cyfreithiol. Mae modelau hefyd yn gostwng cyfanswm cost perchnogaeth drwy wasanaethu fel cyfathrebu parhaus. Mae system sy'n goroesi ei hawduron, yr achos arferol mewn menter a llywodraeth, yn llawer rhatach i'w chynnal pan fo'i model data, ei pheiriannau cyflwr, a'i llifau allweddol wedi'u dogfennu'n gywir.

Mae'r costau'n wirioneddol, a rhaid i chi eu pwyso. Mae modelau'n cymryd amser i'w hadeiladu, sgil i'w hadeiladu'n dda, ac ymdrech barhaus i'w cadw'n gyfredol; mae dulliau ffurfiol yn ychwanegu llafur arbenigol. Caiff y pwynt torri-hyd yn oed ei lywodraethu gan ansicrwydd a chanlyniad. Lle mae'r ddau'n isel, mae modelu trwm yn dinistrio gwerth ac mae heuristics ystwyth yn ennill. Lle mae'r naill neu'r llall yn uchel, mae modelu targededig, a, ar gyfer y craidd critigol, dilysu ffurfiol, yn talu ar ei ganfed lawer gwaith drosodd drwy atal y dosbarth drud o fethiant. I wneud yr achos i arweinyddiaeth, cysylltwch fuddsoddiad modelu â risgiau penodol a ymddeolwyd ac â chynhaliadwyedd systemau hirhoedlog. A dilynwch a yw modelau'n cael eu hymgynghori mewn gwirionedd, oherwydd mae model heb ei ddefnyddio'n gost bur.

## Gwrth-batrymau a pheryglon

- **Modelu er ei fwyn ei hun:** cynhyrchu diagramau oherwydd bod proses yn eu mynnu, nid oherwydd eu bod yn hysbysu penderfyniad.
- **Modelau hen wedi'u hymddiried fel gwirionedd:** diagramau nad ydynt yn cyfateb i'r cod bellach ond y dibynnir arnynt o hyd.
- **Dyluniad mawr ymlaen llaw:** modelau trylwyr wedi'u cynhyrchu cyn unrhyw god, gan gloi penderfyniadau a wnaed gyda'r wybodaeth leiaf.
- **Ymledu diagram:** pob math UML wedi'i gymhwyso'n unffurf, gan foddi'r ychydig olygfeydd defnyddiol mewn sŵn.
- **Dulliau ffurfiol ym mhobman:** cymhwyso dilysu drud i god lle nad yw canlyniad methiant yn ei gyfiawnhau.
- **Dyrchafiad prototeip damweiniol:** prototeip taflu-i-ffwrdd wedi'i anfon yn dawel fel y cynnyrch.
- **Nodiant dros sylwedd:** dadlau am gywirdeb UML yn lle a yw'r model yn ateb y cwestiwn.

## Model aeddfedrwydd

- **Lefel 1 (Cychwyn):** Mae modelu'n ad hoc neu'n absennol ac yn bur adweithiol; ni enwir unrhyw ddull; mae modelau, pan gânt eu tynnu o gwbl, yn anghyson, heb eu dadansoddi, ac wedi'u gadael cyn gynted ag y mae'r cyfarfod yn dod i ben.
- **Lefel 2 (Datblygu):** Mae rhai timau'n tynnu diagramau cyffredin ac yn dilyn dull a enwyd, ond mae'r ymarfer yn anwastad ar draws y sefydliad: caiff modelau eu cynhyrchu'n aml yn seremonïol, yn drifftio o'r cod, ac anaml y cânt eu dadansoddi am namau.
- **Lefel 3 (Safoni):** Diffinnir a gorfodir nodiant a rennir, canllaw dewis-dull wedi'i ddogfennu, a rheolau cysondeb ar draws y sefydliad; dewisir modelau yn ôl pwrpas, cânt eu cadw mewn cam â'r system, eu hadolygu am namau, a chyfatebir y dull i risg pob problem.
- **Lefel 4 (Rheoli):** Caiff modelu ei fesur a'i reoli yn erbyn llinellau sylfaen; mae timau'n olrhain faint o namau y mae dadansoddiad yn eu dal cyn gweithredu, pa mor bell y mae modelau'n drifftio o'r cod, a gafodd pob model ei ymgynghori mewn gwirionedd ar gyfer penderfyniad gwirioneddol, a'r ailwaith ac amser cylchred a arbedwyd o gymharu â llinell sylfaen ddiffiniedig; caiff dewis dull ei galibro yn ôl ansicrwydd a chanlyniad wedi'u mesur, a chaiff creiddiau critigol eu dilysu'n ffurfiol yn erbyn targedau sylw y cytunwyd arnynt.
- **Lefel 5 (Cerddorfa):** Caiff modelu a dewis dull eu gwella'n barhaus a'u hintegreiddio â thraddodi a chynllunio risg ar draws y sefydliad; mae buddsoddiad yn addasu wrth i ansicrwydd a chanlyniad newid, caiff modelau eu cadw'n rheolaidd yn gyfredol, eu hymddeol, neu eu dyfnhau ar sail tystiolaeth, a chyfansoddir dulliau ffurfiol, heuristig, a phrototeipio fel bod pob un yn eistedd yn union lle mae'n talu ar ei ganfed.

## Syniadau ar gyfer trafodaeth

- Ar gyfer eich prosiect diwethaf, pa fodelau a hysbysodd benderfyniad gwirioneddol, a pha rai a dynnwyd dim ond oherwydd bod proses yn eu mynnu?
- Ble yn eich systemau y byddai manyleb ffurfiol yn talu amdani ei hun, a lle byddai'n wastraff?
- Sut ydych chi'n penderfynu a yw prototeip yn daflu-i-ffwrdd neu'n esblygol, ac a ydych chi'n gorfodi'r penderfyniad hwnnw?
- Sut ydych chi'n cadw modelau rhag drifftio allan o gam â'r cod, neu a ydych chi'n derbyn y dylid dileu rhai yn lle hynny?
- Beth yw'r swm cywir o fodelu cyn cod yn eich cyd-destun, a sut mae'n newid gydag ansicrwydd?
- Pa fodel ymddygiadol (cyflwr, dilyniant, neu weithgaredd) a fyddai wedi dal eich digwyddiad cynhyrchu mwyaf diweddar?

## Casgliadau allweddol

- Mae model yn haniaeth bwrpasol; os na allwch enwi'r penderfyniad y mae'n ei hysbysu, peidiwch â'i dynnu.
- Cyfatebwch fodelau strwythurol ac ymddygiadol â'r cwestiwn penodol, a chadwch nhw'n gyson a chyfredol.
- Dadansoddwch fodelau; mae model heb ei wirio yn dybiaeth heb ei brofi.
- Mae dulliau heuristig ac ystwyth yn addas ar gyfer y rhan fwyaf o systemau; cadwch ddulliau ffurfiol ar gyfer creiddiau canlyniad-uchel.
- Defnyddiwch brototeipiau i ymddeol ansicrwydd, a phenderfynwch ymlaen llaw ai taflu-i-ffwrdd neu esblygol ydynt.
- Buddsoddwch mewn modelu'n gyfrannol â'r ansicrwydd y mae'n ei ddatrys a chost cael y penderfyniad yn anghywir.

## Cyfeiriadau a darllen pellach

- IEEE Computer Society, *SWEBOK Guide (Software Engineering Body of Knowledge), Version 4.0*, Software Engineering Models and Methods knowledge area
- Martin Fowler, *UML Distilled: A Brief Guide to the Standard Object Modeling Language*
- Grady Booch, James Rumbaugh, Ivar Jacobson, *The Unified Modeling Language User Guide*
- Frederick P. Brooks, *The Mythical Man-Month* and *No Silver Bullet: Essence and Accident in Software Engineering*
- Daniel Jackson, *Software Abstractions: Logic, Language, and Analysis* (the Alloy modeling language)
- Leslie Lamport, *Specifying Systems* (TLA+)
- Simon Brown, *Software Architecture for Developers* (the C4 model)
- David Harel, *Statecharts: A Visual Formalism for Complex Systems*
