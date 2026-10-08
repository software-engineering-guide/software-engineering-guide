# 2.11 Ansawdd meddalwedd

## Trosolwg a chymhelliant

Mae [ansawdd meddalwedd](https://en.wikipedia.org/wiki/Software_quality) yn ymwneud â pha mor dda y mae system yn diwallu anghenion datganedig a disgwyliadau rhesymol. Mae hynny'n golygu mwy na p'un a yw'n gweithio: mae'n golygu a yw'r system yn ddibynadwy, yn ddiogel, yn hawdd ei chynnal, yn ddefnyddiadwy, yn perfformio'n dda, ac yn addas i'w phwrpas dros amser. Mae ansawdd yn ehangach na phrofi. Mae profi (pennod 2.4) yn un gweithgaredd sy'n datgelu diffygion. Ansawdd yw'r ddisgyblaeth gyfan o adeiladu'r peth iawn yn dda, a gwybod, gyda thystiolaeth, eich bod wedi gwneud hynny. Gall system basio pob prawf a dal i fod o ansawdd isel os yw'n anodd ei chynnal, yn anhygyrch, neu'n wael ei haddasrwydd i'r hyn y mae defnyddwyr wir ei angen.

Mewn tîm mawr, ni all ansawdd fyw ym mhen un person nac arferion un tîm. Mae angen diffiniad a rennir o ansawdd, prosesau eglur ar gyfer ei sicrhau, a mesuriadau sy'n dweud wrthych a yw'n gwella neu'n gwaethygu, ar gannoedd o beirianwyr, cynhyrchion lluosog, a systemau hirhoedlog. Heb hynny, mae "ansawdd" yn dod yn ddyhead amwys sy'n colli pob dadl yn erbyn terfyn amser, ac mae diffygion yn pentyrru hyd nes bod newid yn araf ac yn beryglus.

Mewn lleoliadau menter a llywodraeth, mae'r stanciau'n codi'n uwch. Mae'n rhaid i systemau rheoleiddiedig, hanfodol-i-ddiogelwch, sy'n wynebu dinasyddion ddangos ansawdd, nid ei honni yn unig: mae prosesau dogfennedig, tystiolaeth olrheiniadwy, a gwirio annibynnol yn aml yn orfodol. Mae ansawdd gwael yn cario cost ariannol, cyfreithiol, ac enw da uniongyrchol, ac mewn rhai meysydd mae'n peryglu pobl. Disgyblaeth ansawdd fwriadol, wedi'i hadeiladu o fodelau, prosesau, mesur, a diwylliant, yw'r hyn sy'n troi ansawdd o ddamwain yn ganlyniad wedi'i reoli.

## Egwyddorion allweddol

- Ansawdd yw addasrwydd i'r pwrpas ynghyd â chydymffurfiaeth â gofynion; diffiniwch y ddau'n benodol.
- Adeiledir ansawdd i mewn, ni chaiff ei brofi i mewn; mae gwirio'n dod o hyd i ddiffygion, ond mae atal yn eu hosgoi.
- Gwahaniaethwch [sicrwydd ansawdd](https://en.wikipedia.org/wiki/Quality_assurance) (a yw ein prosesau'n gadarn?) o [reolaeth ansawdd](https://en.wikipedia.org/wiki/Quality_control) (a yw'r cynnyrch hwn yn dda?).
- Mae gwirio'n gofyn "a wnaethom ei adeiladu'n gywir?"; mae dilysu'n gofyn "a wnaethom adeiladu'r peth iawn?"
- Mesurwch ansawdd gyda set fach o fetrigau ystyrlon; triniwch fetrigau fel signalau, nid targedau.
- Mae cost diffyg yn codi po hwyraf y'i canfyddir, felly symudwch weithgareddau ansawdd yn gynharach.
- Mae ansawdd yn briodwedd o'r sefydliad cyfan a'i ddiwylliant, nid giât ar y diwedd.

## Argymhellion

### Mabwysiadwch fodel ansawdd a rennir megis ISO/IEC 25010

Rhowch eirfa gyffredin ar gyfer ansawdd i'ch sefydliad drwy fabwysiadu model ansawdd cynnyrch cydnabyddedig. Mae [ISO/IEC 25010](https://en.wikipedia.org/wiki/ISO/IEC_25010) yn diffinio nodweddion gan gynnwys addasrwydd swyddogaethol, effeithlonrwydd perfformiad, cydnawsedd, defnyddiadwyedd, dibynadwyedd, diogelwch, cynaliadwyedd, a chludadwyedd. Defnyddiwch ef i wneud ansawdd yn gonglfeiniol: ar gyfer pob system, penderfynwch pa nodweddion sy'n bwysicaf a beth mae "digon da" yn ei olygu ar gyfer pob un. Mae'r nodweddion ansawdd cynnyrch hyn yr un peth â'r **priodoleddau ansawdd** sy'n gyrru pensaernïaeth (pennod 3.1). Dau olwg ar un pryder yw ansawdd a phensaernïaeth, felly gadewch iddynt rannu un rhestr o flaenoriaethau yn hytrach na dwy sy'n cystadlu.

### Gwahanwch sicrwydd ansawdd oddi wrth reolaeth ansawdd

Triniwch sicrwydd ansawdd (QA) a rheolaeth ansawdd (QC) fel gweithgareddau gwahanol ond cyflenwol. Mae QA yn broses-ganolog ac yn ataliol: mae'n gwella'r ffordd y caiff gwaith ei wneud, drwy safonau, adolygiadau, diffiniadau o "wedi'i gwblhau", a hyfforddiant, fel bod diffygion yn llai tebygol o ymddangos yn y lle cyntaf. Mae QC yn gynnyrch-ganolog ac yn dditectif: mae'n archwilio gwaith gwirioneddol, megis profi, [adolygiad cod](https://en.wikipedia.org/wiki/Code_review), ac archwiliadau, i ddal diffygion a lwyddodd i fynd i mewn. Mae sefydliad aeddfed yn buddsoddi yn y ddau, ond yn pwyso tuag at QA, oherwydd bod atal diffygion yn rhatach na dod o hyd iddynt a'u trwsio.

### Rhedwch brosesau rheoli ansawdd meddalwedd eglur

Gwnewch ansawdd yn broses reoledig, nid yn obaith tawel. Ar gyfer gwaith sylweddol, ysgrifennwch gynllun ansawdd sy'n nodi'r nodweddion ansawdd targed, y gweithgareddau sicrwydd a rheolaeth, y meini prawf derbyn, a phwy sy'n atebol. Plethwch ef i mewn i arferion sydd gennych eisoes: adolygiad cod (pennod 2.5) fel rheolaeth a ffordd o rannu gwybodaeth, strategaeth brofi (pennod 2.4) fel y rhwyd ddiogelwch awtomataidd, a [dadansoddiad statig](https://en.wikipedia.org/wiki/Static_program_analysis) fel arolygiad parhaus. Adolygwch y data ansawdd yn rheolaidd a gweithredwch ar dueddiadau, yn hytrach nag ymateb i ddigwyddiadau'n unig.

### Ymarferwch wirio a dilysu fel disgyblaethau gwahanol

Mae gwirio'n cadarnhau bod gwaith yn cwrdd â'i fanylebau, fel bod y mewnbynnau cywir i bob cam yn cynhyrchu'r allbynnau cywir, drwy adolygiadau, dadansoddiad statig, a phrofi yn erbyn gofynion. Mae dilysu'n cadarnhau bod y system orffenedig mewn gwirionedd yn diwallu anghenion defnyddwyr a'i defnydd bwriadedig, drwy brofi defnyddwyr, profi derbyn, treialon, ac adborth maes. Mae angen y ddau arnoch. Gall system fod yn gywir yn erbyn manyleb ddiffygiol (wedi'i gwirio ond heb fod yn ddilys), neu gall ymdrin ag angen go iawn tra'n dal i gynnwys diffygion (yn ddilys ond heb ei gwirio). Mewn amgylcheddau rheoleiddiedig, gall fod angen [gwirio a dilysu](https://en.wikipedia.org/wiki/Verification_and_validation) annibynnol (IV&V) gan barti ar wahân i'r datblygwyr.

### Mesurwch ansawdd gyda metrigau ystyrlon

Dewiswch set fach o fetrigau sy'n adlewyrchu canlyniadau ansawdd a'u sbardunau, a'u gwylio dros amser. Mae mesurau defnyddiol yn cynnwys dwysedd diffygion, cyfradd dianc diffygion (diffygion a ganfuwyd mewn cynhyrchu o'i gymharu â chyn rhyddhau), amser cyfartalog i ganfod ac i atgyweirio, cyfradd methiant newid, signalau iechyd cod megis cymhlethdod a dyblygu, a signalau dilysu megis materion wedi'u hadrodd gan ddefnyddwyr a chydymffurfiaeth hygyrchedd. Osgowch fetrigau gwagedd a rhai y gellir eu twyllo: mae metrig sy'n dod yn darged yn stopio mesur realiti. Paru'r rhifau â signalau ansoddol o adolygiadau ac adborth defnyddwyr.

### Nodweddwch a rheolwch ddiffygion yn systematig

Triniwch ddiffygion fel data, nid tanau i'w diffodd yn unig. Dosbarthwch nhw yn ôl difrifoldeb, math, a phrif achos. Olrheiniwch nhw o ddarganfyddiad i ddatrysiad. Chwiliwch am batrymau fel y gallwch atal ailddigwyddiad. Defnyddiwch dechnegau megis [dadansoddiad prif achos](https://en.wikipedia.org/wiki/Root_cause_analysis) a chategoreiddio diffygion i wahaniaethu rhwng camgymeriadau untro a gwendidau systemig. Bwydwch yr hyn a ddysgwch yn ôl i QA, drwy safonau wedi'u diweddaru, profion ychwanegol, ac adolygiadau gwell, fel na ddaw'r un dosbarth o ddiffyg yn ôl. Mae diffyg sydd wedi'i drwsio heb ddeall ei achos yn ddiffyg rydych wedi'i wahodd yn ôl.

### Rheolwch gost ansawdd yn fwriadol

Deallwch economeg ansawdd drwy'r categorïau clasurol: costau atal (hyfforddiant, safonau, cynllun da, offer), costau arfarnu (adolygiadau, profi, archwiliadau), a chostau methiant (ailwaith mewnol cyn rhyddhau, ynghyd â methiannau allanol a ganfyddir gan ddefnyddwyr, sy'n costio llawer mwy). Symudwch eich buddsoddiad tuag at atal ac arfarnu cynnar, oherwydd mae pob doler yno'n osgoi llawer o ddoleri o gost methiant yn ddiweddarach. Gwnewch y costau hyn yn weladwy, fel bod "nid oes gennym amser ar gyfer ansawdd" yn cael ei weld am yr hyn ydyw: dewis i wario mwy ar fethiant yn lle hynny.

### Adeiladwch ddiwylliant ansawdd

Gwnewch ansawdd yn gyfrifoldeb i bawb, wedi'i berchen gan y timau sy'n adeiladu'r meddalwedd, yn hytrach na'i drosglwyddo i adran QA i lawr yr afon sy'n ei arolygu ar y diwedd. Dylai arweinwyr wobrwyo canlyniadau ansawdd, ei gwneud yn ddiogel i adrodd diffygion a namau bron-a-fu, a thrin data ansawdd fel offeryn dysgu yn hytrach na ffon. Mae dull di-fai o drin diffygion yn dod â phroblemau i'r amlwg yn gynnar. Mae un sy'n beio'n eu cuddio hyd nes eu bod yn ddrud.

## Cyfaddawdau: manteision ac anfanteision

| Arfer / dewis | Manteision | Anfanteision |
|---|---|---|
| Model ansawdd ffurfiol (ISO 25010) | Geirfa a rennir; blaenoriaethau eglur | Baich os cymhwysir yn ddogmatig |
| Sicrwydd ansawdd trwm (atal) | Llai o ddiffygion; cost gyfanswm is | Buddsoddiad ymlaen llaw; arafach i ddangos elw |
| Rheolaeth ansawdd trwm (arolygu) | Yn dal diffygion sy'n llithro drwodd | Costus; yn dod o hyd i ddiffygion yn hwyr |
| V&V annibynnol | Sicrwydd uchel; gwrthrychol | Costus; arafach; gall deimlo'n wrthwynebus |
| Metrigau ansawdd cyfoethog | Gwelededd; rhybudd cynnar | Risg twyllo; baich mesur |
| Tîm QA pwrpasol | Ffocws ac arbenigedd | Gall ddadlwytho cyfrifoldeb oddi wrth ddatblygwyr |
| Ansawdd-yn-eiddo-i-dimau | Perchnogaeth; adborth cyflym | Angen disgyblaeth a sgil drwyddi draw |

Y prif gyfaddawd yw buddsoddiad yn erbyn sicrwydd, wedi'i siapio gan amseriad. Mae atal yn costio arian nawr i osgoi costau methiant mwy yn ddiweddarach. Felly nid y lefel uchaf o ansawdd yw'r un gywir yn economaidd; y pwynt cywir yw lle mae cost ymylol mwy o sicrwydd yn hafal i'r gost methiant y mae'n ei osgoi. Mae'r pwynt hwnnw'n uchel ar gyfer systemau hanfodol-i-ddiogelwch ac yn is ar gyfer offer mewnol risg isel. Y tyndra arall sy'n ailymddangos yw perchnogaeth. Mae grwpiau QA canolog yn adeiladu arbenigedd ond gallant adael i ddatblygwyr ddadlwytho cyfrifoldeb. Mae ansawdd sy'n eiddo i dimau'n adeiladu perchnogaeth ond yn galw am sgil a disgyblaeth ym mhobman.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Pan fo'r un dosbarth o ddiffyg yn ymddangos ddwywaith, ydym ni'n rhedeg dadansoddiad prif achos, neu a ydym ni'n ei drwsio eto yn unig?** Mae diffyg sydd wedi'i drwsio heb ddeall ei achos yn ddiffyg rydych wedi'i wahodd yn ôl, ac mewn tîm mawr gall yr un prif achos ymddangos ar draws llawer o wasanaethau cyn i unrhyw un gysylltu'r dotiau. Trin diffygion fel data (wedi'u dosbarthu yn ôl difrifoldeb, math, ac achos, yna'u cloddio am batrymau) yw'r hyn sy'n gwahaniaethu tîm sy'n dod yn gynyddol fwy dibynadwy oddi wrth un sy'n aros yn brysur yn ail-drwsio'r un camgymeriad. Dewch â'ch tracwr diffygion i'r cyfarfod a chwiliwch am lofnodion sy'n ailymddangos: faint o ddigwyddiadau diweddar sy'n rhannu achos na wnaethoch fynd i'r afael ag ef yn systemig erioed? Dylai'r ateb fwydo atal, fel bod achos sy'n ailddigwydd yn gyrru safon wedi'i diweddaru, cynorthwyydd a rennir newydd, prawf ychwanegol, neu restr wirio adolygu well, oherwydd dyna sut mae trwsiad mewn un lle'n atal y dosbarth cyfan rhag dychwelyd.

2. **Ydy hi'n ddiogel yn ein tîm ni adrodd diffyg neu nam bron-a-fu, a beth sy'n digwydd i'r person sy'n ei godi?** Mae ansawdd yn briodwedd o ddiwylliant, ac mae dull di-fai'n dod â phroblemau i'r amlwg yn gynnar tra bod un sy'n beio'n eu cuddio hyd nes eu bod yn ddrud, a all olygu methiant cyhoeddus neu gosb mewn system reoleiddiedig neu sy'n wynebu dinasyddion. Mae hyn yn bwysicaf ar raddfa, lle mae'r peiriannydd agosaf at risg yn aml yn iau a'r cymhelliant i aros yn dawel yn gryf. Dewch â signalau gonest: a yw namau bron-a-fu'n cael eu cofnodi a'u trafod, neu'n diflannu? A yw ôl-drafodaethau'n enwi achosion neu'n enwi pobl? Y weithred yw gwneud data ansawdd yn offeryn dysgu yn hytrach na ffon, gwobrwyo'r bobl sy'n dwyn problemau i'r amlwg, a chynnal ôl-drafodaethau di-fai, oherwydd ni allwch atal yr hyn y mae eich tîm yn ofni ei adrodd.

3. **All dilysu wirioneddol atal rhyddhad, a phwy sy'n dal yr awdurdod hwnnw pan fo terfyn amser yn agosáu?** Mae gwirio (a wnaethom ei adeiladu'n gywir?) a dilysu (a wnaethom adeiladu'r peth iawn?) yn ddisgyblaethau gwahanol, ac nid oes gan ddilysu ddannedd ond os gall gwiriad hygyrchedd a fethodd, brawf derbyn a fethodd, neu ymchwil defnyddwyr damniol wirioneddol atal rhyddhau. Mewn lleoliadau menter a llywodraeth mae hyn yn aml yn orfodol, weithiau drwy wirio a dilysu annibynnol gan barti ar wahân i'r datblygwyr, ac nid yw "fe wnaethom ei ryddhau beth bynnag" yn ateb y mae corff goruchwylio'n ei dderbyn. Dewch â'ch ychydig ryddhadau diwethaf: a wnaeth unrhyw signal ansawdd erioed wirioneddol atal un, neu a yw'r giât wastad yn ildio i'r dyddiad? Os na wnaeth dilysu erioed atal rhyddhad, addurniad ydyw, a'r ateb yw ysgrifennu meini prawf derbyn i'r cynllun ansawdd ymlaen llaw, enwi pwy sy'n berchen ar y penderfyniad mynd/peidio-â-mynd, a rhoi awdurdod go iawn i'r penderfyniad hwnnw'n annibynnol ar y pwysau cyflenwi.

4. **Ydym ni wir yn gwybod ein cost ansawdd gwael, ac ydym ni'n symud gwariant yn fwriadol o fethiant tuag at atal?** Cost ansawdd gwael (COPQ) yw'r arian a gollir i ailwaith mewnol, digwyddiadau cynhyrchu, trwsiadau brys, llwyth cymorth, defnyddwyr coll, a chosbau, ac mae bron bob amser yn fwy na'r gwariant gweladwy ar adolygiadau a phrofi. Mewn tîm mawr mae'r costau methiant wedi'u gwasgaru ar draws sianeli digwyddiadau, ciwiau cymorth, ac ailwaith nad oes neb yn ei gofnodi fel ailwaith, felly maent yn aros yn anweledig hyd nes bod rhywun yn eu hadio i fyny. Y tyndra yw bod atal yn costio arian nawr, mewn cylch cyllideb, i osgoi costau methiant sy'n glanio'n ddiweddarach ac yn glanio ar gyllideb rhywun arall, sy'n gwneud y fasnach yn hawdd ei gohirio am byth. Dewch â ffigurau go iawn: nifer a chost digwyddiadau, oriau ailwaith, cyfradd diffygion sy'n dianc, a'r rhaniad presennol o wariant ar draws atal, arfarnu, a methiant, yna penderfynwch a ddylai'r cymysgedd symud yn gynharach. I systemau menter a llywodraeth, lle mae'r rhan fwyaf o gost oes yn glanio ar ôl y rhyddhad cyntaf, rhowch COPQ o flaen y bobl sy'n dal y gyllideb, oherwydd mae rhif y gall corff goruchwylio ei weld yn llawer anoddach ei fasnachu i ffwrdd nag apêl amwys at "ansawdd".

5. **Pa rai o'n metrigau ansawdd sydd wedi dod yn dargedau'n dawel, a pha ymddygiad y maent yn ei yrru nawr?** Mae metrig sy'n dod yn darged yn stopio mesur realiti: ymlidiwch ganran gwmpas a chewch brofion wedi'u hysgrifennu i symud y rhif, nid profion sy'n dal diffygion. Ar raddfa mae hyn yn beryglus, oherwydd mae dangosfwrdd pennawd a rennir ar draws dwsinau o dimau'n gosod y cymhellion i bob un ohonynt, ac mae metrig y gellir ei dwyllo'n lledaenu'r twyllo ym mhobman ar unwaith. Yr ystyriaeth gystadleuol yw bod angen mesur o hyd arnoch, felly'r ateb yn anaml yw "gollwng y metrig" ond "ei baru â gwrth-signal a'i ddarllen ochr yn ochr â thystiolaeth ansoddol o adolygiadau a defnyddwyr". Dewch â'ch set metrigau presennol a, chyda phob un, gofynnwch beth y gallai rhywun dan bwysau ei wneud i'w symud heb wella ansawdd, ac a ydych wedi gweld hynny'n digwydd. Mewn lleoliadau rheoleiddiedig a rhai sy'n wynebu dinasyddion, byddwch yn arbennig o wyliadwrus o fetrigau cydymffurfiaeth sy'n edrych yn wyrdd tra na chafodd y dilysu sylfaenol (hygyrchedd, canlyniadau defnyddwyr go iawn) ei ymarfer erioed yn wirioneddol, gan y bydd archwiliwr yn y pen draw yn profi'r realiti y tu ôl i'r rhif.

6. **Pwy sy'n berchen ar ansawdd yma: y timau sy'n ysgrifennu'r cod, neu grŵp ar wahân ar y diwedd, a phwy rydym ni mewn gwirionedd yn ei adnoddi?** Mae perchnogaeth yn siapio popeth i lawr yr afon, oherwydd mae seilo QA i lawr yr afon yn gadael i ddatblygwyr ddadlwytho cyfrifoldeb am y cod y maent yn ei ysgrifennu, tra bo ansawdd sy'n eiddo i dimau'n adeiladu perchnogaeth ar draul galw am sgil a disgyblaeth ym mhob tîm. Mewn tîm mawr nid yw hyn yn naill-neu-arall: y patrwm cynaliadwy fel arfer yw timau'n berchen ar ansawdd drwy adolygiad cod a phrofion awtomataidd, wedi'u cefnogi gan grŵp canolog bach sy'n cynnal safonau, yn rhedeg sicrwydd ansawdd fel gwelliant proses, ac yn hyfforddi, yn hytrach nag arolygu ansawdd i mewn ar y diwedd. Dewch â map gonest o ble mae gwaith ansawdd yn digwydd ar hyn o bryd, pwy sy'n atebol pan fo diffyg yn dianc, a ble mae cyllideb a phenrhifau staff wir yn eistedd o'i gymharu â ble mae'r rhethreg yn dweud bod ansawdd yn byw. I sefydliadau menter a llywodraeth, ychwanegwch y gofyniad gwirio a dilysu annibynnol: mae rhai cyfundrefnau sicrwydd yn mynnu parti ar wahân, felly penderfynwch yn fwriadol pa reolaethau sy'n perthyn i'r timau cyflenwi a pha rai sy'n gorfod aros yn annibynnol i fodloni archwilio.

## Golwg sector

**Cwmni newydd.** Mae cyflymder yn bwysicach na seremoni, felly enwch y ddwy neu dair nodwedd ansawdd sydd wir yn amddiffyn eich cynnyrch, fel arfer dibynadwyedd a chynaliadwyedd, a gadewch i'r caboli aros. Perchennwch ansawdd ar draws y tîm cyfan gydag adolygiad cod a chyfres brofion awtomataidd gymedrol yn hytrach na chodi grŵp QA ar wahân na allwch ei staffio. Pan fo'r un dosbarth o wall yn ymddangos ddwywaith, treuliwch ugain munud ar brif achos ac ychwanegwch un cynorthwyydd a rennir ynghyd â phrawf, fel bod atal yn aros yn rhad a'ch cyfradd methiant newid yn aros yn isel tra rydych yn symud yn gyflym.

**Busnes bach.** Heb arbenigwr ansawdd pwrpasol a chyllideb dynn, dibynnwch ar ansawdd sydd wedi'i adeiladu i mewn i'r offer a'r platfformau rydych yn eu prynu yn hytrach na phroses y mae'n rhaid i chi ei rhedeg. Wrth ddewis meddalwedd, triniwch dystiolaeth ansawdd y gwerthwr fel rhan o'r pryniant: ystum diogelwch, hygyrchedd, ymatebolrwydd cymorth, a pha mor aml y mae eu rhyddhadau'n torri. Olrheiniwch lond llaw o signalau rhad, gonest (digwyddiadau cynhyrchu, materion wedi'u hadrodd gan gwsmeriaid, amser i drwsio) yn hytrach na rhaglen fetrigau gywrain nad oes gennych neb i'w chynnal.

**Menter.** Y gwaith yw cysondeb ar draws llawer o dimau: mabwysiadwch fodel ansawdd a rennir megis ISO/IEC 25010, gwahanwch sicrwydd ansawdd (proses) oddi wrth reolaeth ansawdd (cynnyrch), a rhedwch adolygiadau cost ansawdd sy'n symud gwariant tuag at atal. Cadwch ansawdd yn eiddo i'r timau cyflenwi, wedi'u cefnogi gan grŵp canolog bach sy'n cynnal safonau a dangosfyrddau ar gyfer cyfradd dianc diffygion, cyfradd methiant newid, a thueddiadau iechyd cod. Safonwch yr eirfa a'r giatiau fel bod grwpiau'n stopio ailddyfeisio arfer ansawdd, tra'n gadael lle i dimau fodloni'r bariau hynny yn eu ffordd eu hunain.

**Llywodraeth.** Mae caffael, tryloywder, ac atebolrwydd cyhoeddus yn gosod y fframwaith, felly ysgrifennwch ofynion ansawdd i mewn i gontractau a mynnwch dystiolaeth ansawdd ddogfennedig, olrheiniadwy yn hytrach na honiadau. Disgwyliwch wirio a dilysu annibynnol gan barti ar wahân i'r datblygwyr, cydymffurfiaeth hygyrchedd orfodol, a chofnodion diffygion gyda difrifoldeb a phrif achos wedi'u cadw fel rhan o'r llwybr archwilio. Adroddwch ffigurau cost ansawdd gwael (ailwaith, apeliadau, methiannau gwasanaeth) i gyrff goruchwylio, a rhowch awdurdod go iawn i ddilysu atal rhyddhad a fyddai'n siomi'r dinasyddion sy'n dibynnu arno.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd pum person yn penderfynu, ar gyfer ei gynnyrch cynnar, mai dibynadwyedd a chynaliadwyedd yw'r nodweddion ansawdd sy'n bwysig, ac yn gadael i'r caboli perffaith-picsel aros. Mae ansawdd yn eiddo i'r tîm cyfan: adolygiad cod a chyfres brofion awtomataidd gymedrol yw'r rheolaethau, ac nid oes grŵp QA ar wahân i drosglwyddo diffygion iddo. Pan fo'r un dosbarth o wall yn ymddangos ddwywaith, maent yn treulio ugain munud ar olwg brif achos gyflym ac yn ychwanegu un cynorthwyydd a rennir ynghyd â phrawf, fel ei fod yn stopio ailddigwydd yn hytrach na chael ei ail-drwsio â llaw bob tro. Mae'r arfer bach hwnnw o atal yn cadw eu cyfradd methiant newid yn isel tra maent yn dal i symud yn gyflym.

**Menter.** Mae cwmni gwasanaethau ariannol mawr yn mabwysiadu ISO/IEC 25010 fel ei eirfa ansawdd ac, ar gyfer pob cynnyrch, yn cofnodi lefelau targed ar gyfer dibynadwyedd, diogelwch, a chynaliadwyedd. Mae timau'n berchen ar ansawdd: mae adolygiad cod a phrofion awtomataidd yn rheolaethau yn y biblinell, tra bo grŵp canolog bach yn rhedeg QA drwy gynnal safonau a hyfforddi. Mae dangosfwrdd ansawdd yn olrhain cyfradd dianc diffygion, cyfradd methiant newid, a thueddiadau iechyd cod. Mae diffygion yn cael eu dosbarthu a'u prif-achosi, ac mae achosion sy'n ailddigwydd yn gyrru diweddariadau i lyfrgelloedd a rennir a rhestrau gwirio. Mae arweinyddiaeth yn adolygu data cost ansawdd yn chwarterol ac wedi symud gwariant tuag at atal, gan dorri digwyddiadau cynhyrchu a chost eu trwsio ill dau.

**Llywodraeth.** Mae asiantaeth genedlaethol sy'n darparu platfform budd-daliadau sy'n wynebu dinasyddion yn gweithio o dan gyfundrefn sicrwydd sy'n mynnu tystiolaeth ansawdd ddogfennedig. Mae'n rhedeg proses rheoli ansawdd ffurfiol gyda chynllun ansawdd fesul rhyddhad, ynghyd â gwirio a dilysu annibynnol gan dîm ar wahân i'r datblygwyr. Mae gwirio'n gwirio pob gwaith yn erbyn gofynion wedi'u holrhain i bolisi. Mae dilysu'n cynnwys profi cydymffurfiaeth hygyrchedd ac ymchwil defnyddwyr gyda dinasyddion go iawn, a gall y naill neu'r llall atal rhyddhad. Caiff diffygion eu holrhain gyda difrifoldeb a phrif achos fel rhan o'r llwybr archwilio, ac mae ffigurau cost ansawdd gwael (ailwaith, apeliadau, a methiannau gwasanaeth) yn mynd i gyrff goruchwylio i gyfiawnhau buddsoddiad parhaus mewn atal.

## Achos busnes: cymhellion, ROI, a TCO

Yr elw ar ansawdd yw cost gyfanswm berchnogaeth is a chyflymder cyflenwi cyson. Mae gan gost ansawdd ddwy ochr. Mae'r gwariant da, atal ac arfarnu, yn weladwy ac yn reoladwy: cynllun, safonau, adolygiadau, profi, ac offer. Mae cost ansawdd gwael (COPQ) yn fwy ond yn aml wedi'i guddio: ailwaith mewnol, digwyddiadau cynhyrchu, trwsiadau brys, cymorth cwsmeriaid, defnyddwyr coll, cosbau rheoleiddiol, a niwed i enw da. Mae astudiaethau'n mynd yn ôl at "Quality Is Free" Crosby wedi darganfod yn gyson bod cyfanswm cost ansawdd gwael yn llawer mwy na chost ei atal, a bod diffygion yn tyfu'n llawer drutach po hwyraf y'u daliwch: mae mater a ganfyddir mewn cynllun yn costio ffracsiwn o'r un mater a ganfyddir mewn cynhyrchu.

I arweinyddiaeth, nid "gwariwch fwy ar ansawdd" yw'r ddadl. "Gwariwch yn gynharach i wario llai yn gyffredinol" ydyw. Meintiolwch COPQ o'ch data eich hun (nifer a chost digwyddiadau, oriau ailwaith, cyfradd diffygion sy'n dianc) a dangoswch sut mae atal ac arfarnu cynnar yn ei ostwng. Cysylltwch ansawdd â chanlyniadau busnes: mae dibynadwyedd yn cadw cwsmeriaid, mae cynaliadwyedd yn cadw newid dyfodol yn rhad, ac mae diogelwch a hygyrchedd yn eich cadw allan o drafferth gyfreithiol. Mewn systemau menter a llywodraeth hirhoedlog, lle mae'r rhan fwyaf o'r gost yn glanio ar ôl y rhyddhad cyntaf, mae dimensiynau cynaliadwyedd a dibynadwyedd ansawdd yn dominyddu cost oes. Mae hynny'n gwneud buddsoddiad ansawdd cynnar yn un o'r penderfyniadau lifer-uchaf y gallwch eu gwneud.

## Gwrth-batrymau a pheryglon

- **Ansawdd fel giât derfynol:** arolygu ansawdd i mewn ar y diwedd yn hytrach na'i adeiladu i mewn, fel bod diffygion yn cael eu darganfod pan fyddant ddrutaf.
- **Drysu profi ag ansawdd:** tybio bod pasio profion yn golygu ansawdd uchel, gan anwybyddu cynaliadwyedd, defnyddiadwyedd, ac addasrwydd i'r pwrpas.
- **QA fel seilo ar wahân:** tîm i lawr yr afon sy'n "berchen ar ansawdd", gan adael i ddatblygwyr ddadlwytho cyfrifoldeb am y cod y maent yn ei ysgrifennu.
- **Theatr fetrigau:** ymlid canrannau cwmpas neu gyfrifon diffygion fel targedau, sy'n gwahodd twyllo ac yn cuddio ansawdd go iawn.
- **Gwirio heb ddilysu:** adeiladu'r fanyleb yn gywir heb byth wirio bod y fanyleb yn diwallu anghenion go iawn.
- **Dim dadansoddiad prif achos:** trwsio diffygion yn unigol heb fynd i'r afael â'r achos systemig, fel bod yr un dosbarth yn ailddigwydd.
- **Anwybyddu cost ansawdd gwael:** trin ansawdd fel cost bur oherwydd bod costau methiant wedi'u cuddio a heb eu mesur.

## Model aeddfedrwydd

**Lefel 1 (Cychwyn).** Mae ansawdd yn ddiffiniedig ac yn ad hoc. Mae'n dibynnu ar ddiwydrwydd unigol, caiff ei wirio'n bennaf drwy brofi â llaw ar y diwedd, a chaiff diffygion eu trin yn adweithiol wrth iddynt ymddangos. Nid oes model a rennir, dim metrigau, a dim llinell rhwng sicrwydd a rheolaeth.

**Lefel 2 (Datblygu).** Mae arferion sylfaenol yn ymddangos: adolygiad cod, profion awtomataidd, a thracwr diffygion. Caiff rhywfaint o ddata ansawdd ei gasglu, ond yn anghyson, a phob tîm yn ei wneud ei ffordd ei hun. Mae ansawdd yn dal i gael ei weld yn bennaf fel profi, mae atal yn fach, mae gwirio'n digwydd, ac mae dilysu'n anffurfiol.

**Lefel 3 (Safoni).** Mae'r sefydliad yn mabwysiadu model ansawdd a rennir (megis ISO/IEC 25010), yn gwahanu QA oddi wrth QC, ac yn rhedeg prosesau rheoli ansawdd gyda chynlluniau ansawdd a meini prawf derbyn, wedi'u dogfennu a'u cymhwyso'n gyson ar draws timau. Mae gwirio a dilysu'n wahanol ac yn fwriadol, a chaiff diffygion eu dosbarthu a'u prif-achosi i gynllun cytûn.

**Lefel 4 (Rheoli).** Caiff ansawdd ei fesur a'i reoli yn erbyn llinellau sylfaen. Caiff set fach o fetrigau ystyrlon eu holrhain dros amser (dwysedd diffygion, cyfradd dianc diffygion, amser cyfartalog i ganfod ac atgyweirio, cyfradd methiant newid, a signalau iechyd cod megis cymhlethdod a dyblygu), a chaiff cost ansawdd ei meintioli ar draws atal, arfarnu, a methiant. Caiff giatiau derbyn ac ansawdd eu gorfodi ar dystiolaeth yn hytrach na barn, caiff tueddiadau eu hadolygu ar gadence penodol, a gall dilysu wirioneddol atal rhyddhad.

**Lefel 5 (Cerddorfa).** Mae ansawdd yn ddisgyblaeth sy'n cael ei gwella'n barhaus, yn eiddo i'r diwylliant, ac wedi'i integreiddio â chynllunio busnes a risg. Atal yw'r pwyslais, mae data cost ansawdd yn arwain ble mae buddsoddiad yn mynd, ac mae canfyddiadau prif achos yn atal ailddigwydd yn systematig. Mae timau'n berchen ar ansawdd o ben i ben, mae metrigau'n bwydo gwelliant parhaus, ac mae'r sefydliad yn addasu ei arfer ansawdd wrth i gynhyrchion, risgiau, a rheoleiddio newid. Mae hyn yn alinio â lefelau uwch y modelau aeddfedrwydd ym mhennod 10.8.

## Syniadau ar gyfer trafodaeth

- Pa nodweddion ansawdd ISO/IEC 25010 sy'n bwysicaf i'ch systemau, a beth yw "digon da" ar gyfer pob un?
- Ble mae eich sefydliad yn eistedd ar y cymysgedd gwariant atal-arfarnu-methiant, ac a ddylai symud?
- Ydych chi'n gwahaniaethu gwirio oddi wrth ddilysu yn ymarferol, neu'n cwympo'r ddau i mewn i "brofi"?
- A yw ansawdd yn eiddo i'r timau sy'n adeiladu meddalwedd, neu'n cael ei ddirprwyo i grŵp ar wahân, a beth fyddai'n newid pe baech yn ei symud?
- Beth yw eich cost wir o ansawdd gwael, ac a allech ei mesur yn ddigon da i wneud yr achos busnes?
- Pa rai o'ch metrigau ansawdd sy'n signalau go iawn, a pha rai sydd wedi dod yn dargedau y gellir eu twyllo?

## Prif gasgliadau

- Mae ansawdd yn ehangach na phrofi: addasrwydd i'r pwrpas ynghyd â chydymffurfiaeth ydyw, ar draws nodweddion fel dibynadwyedd, diogelwch, a chynaliadwyedd.
- Defnyddiwch fodel ansawdd a rennir (ISO/IEC 25010) fel bod priodoleddau ansawdd yn eglur ac yn alinio â phensaernïaeth (pennod 3.1).
- Gwahanwch sicrwydd ansawdd (atal, proses) oddi wrth reolaeth ansawdd (canfod, cynnyrch), a phwyswch tuag at atal.
- Ymarferwch wirio (ei adeiladu'n gywir) a dilysu (adeiladu'r peth iawn) fel disgyblaethau gwahanol.
- Mesurwch ansawdd gyda ychydig o fetrigau ystyrlon, a nodweddwch ddiffygion yn ôl difrifoldeb a phrif achos i atal ailddigwydd.
- Rheolwch gost ansawdd: mae atal ac arfarnu cynnar yn llawer rhatach na methiant, yn enwedig mewn systemau hirhoedlog.
- Adeiladwch ddiwylliant ansawdd di-fai lle mae timau'n berchen ar ansawdd, wedi'u cefnogi gan adolygiad cod (pennod 2.5) a strategaeth brofi (pennod 2.4).

## Cyfeiriadau a darllen pellach

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Quality knowledge area.
- ISO/IEC 25010, *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): System and software quality models*.
- ISO/IEC 25000 series (SQuaRE), *Software product quality requirements and evaluation*.
- Philip B. Crosby, *Quality Is Free: The Art of Making Quality Certain*.
- W. Edwards Deming, *Out of the Crisis*.
- Capers Jones and Olivier Bonsignour, *The Economics of Software Quality*.
- Gerald Weinberg, *Quality Software Management*.
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (quality assurance and V&V process context).
