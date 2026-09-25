# 2.8 Gofynion meddalwedd

## Trosolwg a chymhelliant

Mae [gofyniad meddalwedd](https://en.wikipedia.org/wiki/Software_requirements) yn ddatganiad o allu neu amod y mae'n rhaid i system ei ddarparu, ei fodloni, neu ei feddu er mwyn bod yn dderbyniol i'w rhanddeiliaid. Mae [peirianneg gofynion](https://en.wikipedia.org/wiki/Requirements_engineering), y gwaith disgybledig o ennyn, dadansoddi, manylu, dilysu, a rheoli'r datganiadau hynny, yn eistedd yn union ar flaen y gadwyn werth. Mae popeth i lawr yr afon, o bensaernïaeth i god i [brofi derbyn](https://en.wikipedia.org/wiki/Acceptance_testing), yn ymgais i fodloni gofynion. Felly pan fo gofynion yn anghywir, yn anghyflawn, neu'n amwys, mae'r holl ymdrech a dreulir yn adeiladu'r peth anghywir yn gywir yn wastraff pur, a dyma'r gwastraff drutaf sy'n bodoli, oherwydd mai dyna'r hwyraf i chi ei ddarganfod. Mae maes gwybodaeth Gofynion Meddalwedd y [Corff Gwybodaeth Peirianneg Meddalwedd](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) (SWEBOK) yn trin hyn fel disgyblaeth beirianyddol go iawn, nid rhagarweiniad clercol i'r gwaith go iawn.

I dimau mawr, gofynion yw'r ddealltwriaeth a rennir sy'n galluogi llawer o bobl i adeiladu un system gydlynol. Gall un datblygwr gadw'r bwriad yn ei ben; ni all cannoedd o bobl ar draws llawer o dimau. Mae gofynion yn dod yn gontract rhwng y rhai sydd angen gallu a'r rhai sy'n ei adeiladu, y sail ar gyfer rhannu gwaith ar draws timau, a'r llathen fesur ar gyfer barnu pryd mae rhywbeth yn "wneud." Maent yn cysylltu'n uniongyrchol â darganfod (pennod 11.1), lle mae problemau a chyfleoedd yn wynebu; â sylfeini UX (pennod 5.1), lle byddwch yn deall anghenion defnyddwyr; ag APIs a dylunio rhyngwyneb (pennod 2.3), lle mae rhwymedigaethau rhyngwyneb yn cael eu sefydlu; â phensaernïaeth a phriodweddau ansawdd (pennod 3.1), lle mae gofynion an-swyddogaethol yn gyrru strwythur; a rheoli prosiect (pennod 10.6), lle cynllunnir cwmpas, cost, ac amserlen o'u cwmpas.

Mewn lleoliadau menter a llywodraeth, mae gofynion yn cario pwysau cyfreithiol, contractiol, a diogelwch. Rhaid i system reoledig ddangos bod pob rhwymedigaeth orfodol (hygyrchedd, preifatrwydd, diogelwch, cadw cofnodion, rheolaeth ariannol) wedi'i dal fel gofyniad, ei weithredu, a'i wirio â thystiolaeth. Adeiledir caffaeliadau llywodraeth yn aml o gwmpas manyleb gofynion, ac mae taliad, archwiliad, ac ardystiad i gyd yn dibynnu ar olrhain pob gofyniad i'r dystiolaeth y cafodd ei fodloni. Yma, mae gofynion yn fwy nag arfer da: dyma asgwrn cefn atebolrwydd.

## Egwyddorion allweddol

- Mae gofyniad yn mynegi angen neu gyfyngiad, nid ateb; mae'n dweud beth a pham, nid sut.
- Rhaid i bob gofyniad fod yn angenrheidiol, yn ddiamwys, yn wiriadwy, yn ymarferol, ac yn olrheiniadwy.
- Darganfyddir a thrafodir gofynion gyda rhanddeiliaid, nid eu dyfeisio ar wahân.
- Mae gofynion an-swyddogaethol a chyfyngiadau'n llunio pensaernïaeth cymaint â swyddogaethedd.
- Mae gofynion yn esblygu; rheolwch newid yn fwriadol yn hytrach na'i rewi neu ei anwybyddu.
- Olrheiniadwyedd, o angen i ofyniad i ddyluniad i brawf i dystiolaeth, yw meinwe gysylltiol atebolrwydd.
- Mae'r lefel gywir o ffurfioldeb yn dibynnu ar risg, graddfa, a chyd-destun rheoleiddiol, nid arferiad.

## Argymhellion

### Diffinio gofynion yn glir a'u categoreiddio

Enwch y categorïau'n fwriadol. Mae **[gofynion swyddogaethol](https://en.wikipedia.org/wiki/Functional_requirement)** yn nodi beth y mae'n rhaid i'r system ei wneud: yr ymddygiadau, y trawsffurfiadau, a'r gwasanaethau y mae'n eu darparu. Mae **[gofynion an-swyddogaethol](https://en.wikipedia.org/wiki/Non-functional_requirement)** (priodweddau ansawdd) yn nodi pa mor dda y mae'n rhaid iddi eu gwneud: perfformiad, argaeledd, diogelwch, defnyddioldeb, hygyrchedd, cynhaladwyedd, a mwy; mae'r rhain yn rhwymo'n dynn wrth bensaernïaeth (pennod 3.1). Y **cyfyngiadau** yw ffiniau anhrafodadwy'r ateb: technolegau gorfodol, safonau, cyllidebau, rheolau cyfreithiol, neu ryngwynebau i systemau presennol. A gwahanwch **ofynion busnes** (pam mae'r sefydliad eisiau'r system) oddi wrth **ofynion defnyddiwr** (beth mae angen i ddefnyddwyr ei gyflawni) oddi wrth **ofynion system** (beth felly y mae'n rhaid i'r meddalwedd ei wneud). Cymysgwch y lefelau hyn gyda'i gilydd a bydd dryswch cwmpas yn dilyn yn fuan.

### Ennyn o ffynonellau go iawn, nid rhagdybiaethau

Darganfyddiad gweithredol yw ennyn. Tynnwch ofynion o randdeiliaid drwy gyfweliadau, gweithdai, arsylwi, [prototeipiau](https://en.wikipedia.org/wiki/Software_prototyping), a dadansoddiad o systemau a dogfennau presennol. Olrheiniwch bob rhanddeiliad perthnasol, gan gynnwys y rhai hawdd eu hanghofio: gweithredwyr, archwilwyr, staff cymorth, a phobl yr effeithir arnynt gan y system nad ydynt byth yn ei defnyddio'n uniongyrchol. Cysylltwch ennyn â'r biblinell ddarganfod (pennod 11.1) ac ymchwil UX (pennod 5.1), fel bod dymuniadau a nodwyd yn olrhain yn ôl i'r anghenion sylfaenol. Cofnodwch ffynhonnell a rhesymeg pob gofyniad, oherwydd gwybod pam mae gofyniad yn bodoli yw'n union yr hyn sy'n eich galluogi i'w newid yn ddiogel yn ddiweddarach.

### Dadansoddi, trafod, a blaenoriaethu

Mae anghenion crai a ennynnwyd yn gwrthdaro, yn gorgyffwrdd, ac yn adio i fyny i fwy nag sy'n ymarferol. Dadansoddiad yw sut y byddwch yn eu cysoni: dosbarthu gofynion, canfod gwrthdaro, pwyso ymarferoldeb a risg, a thrafod blaenoriaethau gyda rhanddeiliaid. Blaenoriaethwch yn agored, dyweder gyda gwahaniaethau rhaid/dylai/gallai neu raddio gwerth-yn-erbyn-cost, fel eich bod, pan fo amser yn brin, yn torri'r cwmpas cywir. A modelwch y gofynion lle bynnag y mae model yn ychwanegu eglurder: llifoedd proses, diagramau cyflwr, modelau data, a diffiniadau rhyngwyneb yn dod â bylchau i'r wyneb y mae rhyddiaith yn eu cuddio.

### Manylu ar y lefel gywir o ffurfioldeb

Ysgrifennwch ofynion i lawr mewn ffurf sy'n gweddu i'r risg a'r gynulleidfa. Gall system lywodraeth risg-uchel fynnu manyleb ffurfiol wedi'i strwythuro i safon fel IEEE 29148; gall tîm cynnyrch cyflym-symudol ddal gofynion fel [straeon defnyddiwr](https://en.wikipedia.org/wiki/User_story) gyda meini prawf derbyn mewn ôl-groniad. P'un bynnag, dylai pob gofyniad fod yn atomig, yn wiriadwy, ac yn rhydd o eiriau llithrig fel "cyflym," "cyfeillgar i ddefnyddwyr," neu "ac ati." Ynghlymwch feini prawf derbyn, fel eich bod yn diffinio sut i wirio gofyniad ar yr un pryd ag y byddwch yn ei ysgrifennu. A chadwch un ffynhonnell awdurdodol, yn hytrach na gadael i ofynion wasgaru ar draws negeseuon e-bost, tocynnau, a sleidiau.

### Dilysu cyn adeiladu

Mae dilysu'n cadarnhau bod y gofynion rydych wedi'u manylu'r rhai cywir a'u bod yn crogi gyda'i gilydd. Adolygwch nhw gyda rhanddeiliaid, ewch trwy senarios, a lle gallwch, defnyddiwch brototeipiau i wneud datganiadau haniaethol yn goncrit. Mae dilysu'n rhatach nag unrhyw gywiro diweddarach: mae diffyg a ddelir mewn adolygiad gofynion yn costio ffracsiwn o'r un diffyg a ddelir mewn cynhyrchiad.

### Rheoli gofynion a chynnal olrheiniadwyedd

Mae gofynion yn newid. Eich gwaith chi yw rheoli'r newid hwnnw, nid ei wrthsefyll. Sefydlwch broses newid: pwyswch bob newid arfaethedig am effaith, cost, ac effaith i lawr yr afon cyn i chi ei dderbyn. Llinellwch sylfaen gofynion ar bwyntiau y cytunwyd arnynt a'u fersiynu. Cadwch **[olrheiniadwyedd ddwyffordd](https://en.wikipedia.org/wiki/Requirements_traceability)** sy'n cysylltu pob gofyniad ymlaen â dyluniad, cod, a phrofion, ac yn ôl â'r angen y daeth ohono. Mae olrheiniadwyedd yn ateb y ddau gwestiwn y mae timau mawr yn byw wrthynt: os yw'r angen hwn yn newid, beth y mae'n effeithio arno; ac ar gyfer y nodwedd hon a ddanfonwyd, pa angen a'i cyfiawnhaodd? Mewn cyd-destunau rheoledig, estynnwch yr olrhain yr holl ffordd at dystiolaeth dderbyn (canlyniadau prawf, cofnodion archwilio, cymeradwyaethau) fel y gallwch ddangos cydymffurfiaeth yn hytrach na dim ond ei honni.

### Addasu i gyd-destunau ystwyth a chynllun-yrredig

Mewn rhaglenni cynllun-yrredig a rheoledig, byddwch yn manylu ac yn llinellu sylfaen gofynion yn eithaf cynnar, gyda rheolaeth newid ffurfiol. Mewn cyd-destunau ystwyth, mae gofynion yn byw fel ôl-groniad blaenoriaethedig, esblygol, wedi'i ymhelaethu ychydig cyn gweithredu a'i ddilysu'n barhaus drwy feddalwedd sy'n gweithio. Yr un yw'r gweithgareddau sylfaenol yn y ddau achos; dim ond yr amseriad, y ffurfioldeb, a'r arteffactau sy'n wahanol. Mae sefydliadau mawr yn aml yn cyfuno'r ddau: maent yn manylu ac yn olrhain rhwymedigaethau sefydlog, risg-uchel yn ffurfiol, tra'n ymhelaethu ymddygiad cynnyrch yn ailadroddus. Dewiswch y cydbwysedd yn ôl risg, nid ideoleg.

## Cymhareb: manteision ac anfanteision

| Dull | Gorau ar gyfer | Manteision | Anfanteision |
|---|---|---|---|
| Manyleb ffurfiol ymlaen llaw | Contractau risg-uchel, rheoledig, cwmpas-sefydlog | Olrheiniadwyedd gref; sail dderbyn glir; archwiliadwy | Araf i newid; risg o or-fanylu cyn dysgu |
| Ôl-groniad ystwyth | Cynhyrchion esblygol gyda rhanddeiliaid ymgysylltiedig | Adborth cyflym; yn addasu i ddysgu; llai o wastraff ar gwmpas na adeiladwyd | Olrheiniadwyedd hirdymor gwannach; anos ei archwilio a'i gontractio |
| Hybrid (cyfyngiadau ffurfiol + ymddygiad ystwyth) | Mentrau â rhwymedigaethau cymysg | Trylwyredd lle mae'n bwysig, hyblygrwydd mewn mannau eraill | Angen barn ynghylch pa rannau yw pa un |

Y tyndra canolog yw rhwng sefydlogrwydd a dysgu. Mae sefydlogi gofynion yn gynnar yn prynu i chi sail dderbyn gadarn ac archwiliadwyedd, ond yn costio i chi'r gallu i addasu i'r hyn a ddysgwch wrth adeiladu. Mae eu gohirio'n prynu addasrwydd, ond yn costio olrheiniadwyedd hirdymor ac eglurder contractiol. Mae buddsoddi mwy mewn peirianneg gofynion hefyd yn cyfnewid cyflymder tymor-byr am lai o ailwaith yn ddiweddarach: cyfnewid sy'n talu ar ei ganfed wrth i raddfa system, hydoedd oes, a chanlyniad methiant godi. Mae'r prosiectau mwyaf a'r rhai mwyaf rheoledig yn eistedd yn gadarn ar yr ochr buddsoddiad-uchel. Nid yw teclyn mewnol risg-isel.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Pwy sy'n cyfrif fel rhanddeiliad ar gyfer ein system risg-uchaf, a pha rai rydym yn eu gadael allan bob amser hyd nes derbyn?** Ar raglen fawr anaml y bydd y bobl a gaiff eu sgipio'n ddefnyddwyr amlwg: dyma'r gweithredwyr sy'n rhedeg y peth am 3am, yr archwilwyr sy'n gorfod ei ardystio, y staff cymorth sy'n delio â'r methiannau, a'r di-ddefnyddwyr yr effeithir arnynt nad ydynt byth yn mewngofnodi ond y mae eu data gennych. Eu colli a byddwch yn darganfod eu gofynion ar yr eiliad drutaf, yn ystod derbyn neu ar ôl i reoleiddiwr ofyn. Dewch â map rhanddeiliaid pendant i'r cyfarfod a'i brofi dan straen: ar gyfer pob rhwymedigaeth orfodol (hygyrchedd, preifatrwydd, cadw cofnodion, diogelwch) enwch y person sy'n berchen arni a'r gofyniad sy'n ei dal. Os na allwch enwi perchennog, rydych wedi darganfod bwlch, a'r trwsiad yw ychwanegu'r rhanddeiliad hwnnw at ennyn nawr yn hytrach nag ôl-osod eu hanghenion i mewn i bensaernïaeth sefydlog yn ddiweddarach.

2. **Pan fo gofyniad yn newid, a allwn ateb beth y mae'n effeithio arno cyn i ni gymeradwyo'r newid?** Dyma'r prawf ymarferol o a yw'ch olrheiniadwyedd ddwyffordd yn real neu'n addurniadol. Mewn system fawr neu reoledig gall un newid rheol dreiddio i mewn i ddyluniad, cod, profion, a thystiolaeth dderbyn, ac mae ei gymeradwyo'n ddall yn ffordd o ddanfon system sy'n edrych yn gydymffurfiol ond yn torri'n dawel reol yr arferai ei bodloni. Dewch â chais newid diweddar a cheisiwch ei olrhain ymlaen yn y cyfarfod: os yw'n cymryd prynhawn o archeoleg, nid yw'ch olrheiniadwyedd yn gwneud ei gwaith. Dylai'r ateb ail-lunio'ch proses newid, fel bod asesiad effaith yn ymholiad cyflym yn erbyn olrhain byw yn hytrach na helfa â llaw, ac fel bod llinellau sylfaen a fersiynu'n rhoi pwynt sefydlog i chi newid yn ei erbyn.

3. **Ble mae ffynhonnell awdurdodol unigol ein gofynion yn byw, a faint o'r gwirionedd sy'n wasgaredig y tu allan iddi?** Mae ymledu gofynion (y fanyleb go iawn yn byw ar draws negeseuon e-bost, tocynnau, sleidiau, a chof rhywun) yn un o'r methiannau mwyaf cyffredin mewn timau mawr, ac mae'n angheuol mewn systemau a archwilir lle mae'n rhaid i chi ddangos beth y cytunwyd arno. Penderfynwch, yn uchel, pa system gofnod sy'n ganonaidd, a thriniwch unrhyw beth a nodir mewn mannau eraill fel drafft nes iddo lanio yno gyda'i ffynhonnell a'i resymeg ynghlwm. Dewch â thystiolaeth: cyfrifwch faint o anghydfodau cwmpas diweddar a ddaeth i lawr i ddau berson yn dyfynnu fersiynau "terfynol" gwahanol. Os yw'r cyfrif yn fwy na sero, y weithred yw cyfnerthu i un ffynhonnell ac ysgrifennu'r rhesymeg ar gyfer pob gofyniad i lawr, oherwydd gwybod pam mae gofyniad yn bodoli yw'n union yr hyn sy'n eich galluogi i'w newid neu ei ollwng yn ddiogel yn ddiweddarach.

4. **A yw ein gofynion an-swyddogaethol yn cael eu dal yn ddigon cynnar i yrru pensaernïaeth, ynteu a ydym yn dal i'w darganfod ar ôl i'r strwythur gael ei sefydlu?** Mae rhwymedigaethau perfformiad, argaeledd, diogelwch, a hygyrchedd yn llunio pensaernïaeth yn fwy na'r rhan fwyaf o nodweddion, ac ar raglen fawr dyma'r gofynion sy'n dod i'r wyneb yn rhy hwyr amlaf, unwaith y bo'r strwythur a fyddai'n gorfod eu bodloni eisoes wedi'i arllwys mewn concrit. Mae'r tyniad cystadleuol yn real: ymddygiad swyddogaethol yw'r hyn y mae rhanddeiliaid yn gofyn amdano'n uchel ac yn ei ddangos yn dda, tra bo gofyniad "ymateb is-eiliad o dan lwyth brig" neu "gydymffurfiaeth hygyrchedd WCAG" yn anweledig hyd nes iddo gael ei dorri. Dewch â'r rhestr bresennol o ofynion an-swyddogaethol ar gyfer eich system risg-uchaf, y pwynt yn yr amserlen yr ysgrifennwyd pob un, ac a wnaeth pensaernïaeth (pennod 3.1) eu derbyn fel gyrwyr penodol neu eu casglu drwy ddyfaliad. Mewn lleoliadau menter a llywodraeth, ychwanegwch y rhwymedigaethau ansawdd gorfodol (amgryptio, cadw cofnodion, cyfraith hygyrchedd) a gwiriwch fod pob un yn ofyniad ysgrifenedig, mesuradwy a drosglwyddwyd i ddylunio yn hytrach na rhagdybiaeth, oherwydd mae ôl-osod priodwedd ansawdd ar ôl derbyn yn lle mae cyllidebau ac amserlenni'n marw'n dawel.

5. **Pa lefel o ffurfioldeb sy'n gywir ar gyfer pob system sy'n eiddo i ni, ac a ydym yn ei dewis yn ôl risg neu arferiad?** Mae un sefydliad mawr fel arfer yn rhedeg amrywiaeth o systemau, o declyn mewnol tafladwy i blatfform rheoledig bywyd-neu-ddiogelwch, ac mae cymhwyso un seremoni i bob un naill ai'n claddu'r gwaith risg-isel mewn papurwaith neu'n gadael y gwaith risg-uchel wedi'i danfanylu. Y tyndra yw rhwng archwiliadwyedd a sail dderbyn gadarn manyleb ffurfiol ymlaen llaw ac adborth cyflym a gwastraff gostyngedig ôl-groniad esblygol, a'r ateb gonest i'r rhan fwyaf o fentrau yw cyfuniad bwriadol: ffurfioli ac olrhain y rhwymedigaethau sefydlog, risg-uchel tra'n ymhelaethu ymddygiad cynnyrch yn ailadroddus. Dewch â rhestr fer o'ch systemau wedi'u graddio yn ôl canlyniad methiant, amlygiad rheoleiddiol, a chyfradd newid, ac ar gyfer pob un enwch y ffurfioldeb a ddefnyddiwch mewn gwirionedd yn erbyn y ffurfioldeb y mae'r risg yn ei fynnu. Ar gyfer rhaglen lywodraeth wedi'i hangori i gais tendr a safon fel IEEE 29148, mae'r ffurfioldeb yn cael ei ddeddfu'n rhannol gan y contract, felly'r drafodaeth yw ble y gallwch haenu ymhelaethu ystwyth ar ei ben heb dorri'r olrheiniadwyedd y mae'r archwiliad yn dibynnu arni.

6. **A ellir gwirio pob gofyniad yn ein system risg-uchaf, ac a yw pob un yn cario meini prawf derbyn a ysgrifennwyd yr eiliad y cafodd y gofyniad ei ysgrifennu?** Nid gofyniad yw gofyniad na allwch ei wirio, dymuniad ydyw, ac mae geiriau llithrig fel "cyflym," "diogel," neu "cyfeillgar i ddefnyddwyr" yn pasio adolygiad yn union am na all neb eu methu. I dîm mawr mae hyn yn bwysig ddwywaith drosodd: mae gofynion na ellir eu gwirio'n cynhyrchu anghydfodau cwmpas wrth dderbyn, ac maent yn ei gwneud yn amhosibl dweud pryd mae nodwedd wir wedi'i gwneud. Yr ystyriaeth gystadleuol yw cyflymder, gan fod ynghlymu maen prawf mesuradwy a dull gwirio wrth bob gofyniad yn arafach ymlaen llaw na sgrifennu rhyddiaith, ond dyma'r amddiffyniad rhataf yn erbyn yr ailwaith hwyr drutaf. Dewch â sampl o ofynion diweddar a phrofwch bob un yn erbyn bar syml: a yw'n atomig, a yw'n fesuradwy, ac a yw'n enwi sut y caiff ei wirio. Mewn cyd-destunau rheoledig a llywodraeth, estynnwch y prawf at dystiolaeth: nid ystyrir bod gofyniad heb dystiolaeth dderbyn olrheiniedig, sy'n pasio, wedi'i ddanfon, ni waeth beth mae'r meddalwedd yn ymddangos ei fod yn ei wneud, felly meini prawf derbyn yw hedyn y cofnod cydymffurfiaeth y bydd yn rhaid i chi ei gynhyrchu yn y pen draw.

## Lens sector

**Cwmni newydd.** Gyda thîm bach ac ychydig o redeg, cadwch ofynion mor ysgafn ag y gallwch ddianc ag ef: straeon defnyddiwr gyda meini prawf derbyn mewn un ôl-groniad a rennir, nid dogfen fanyleb. Y ddisgyblaeth sy'n talu ar ei ganfed hyd yn oed yma yw siarad â defnyddwyr go iawn cyn i chi adeiladu a chofnodi ffynhonnell a rhesymeg pob stori, fel bod yr wythnos y byddech wedi'i gwastraffu'n adeiladu'r nodwedd anghywir yn wythnos rydych yn ei harbed. Sgipiwch olrheiniadwyedd ffurfiol, ond byth peidiwch â sgipio'r sgwrs sy'n dweud wrthych beth yw'r angen go iawn.

**Busnes bach.** Yn debygol nid oes gennych ddadansoddwr busnes na arbenigwr gofynion, felly mae'r gwaith yn syrthio i bwy bynnag sydd agosaf at y cwsmer, ac mae'r cwestiwn prynu-yn-erbyn-adeiladu'n dominyddu. Fframiwch ofynion fel rhestr fer, flaenoriaethedig o'r canlyniadau sydd eu hangen arnoch, yna ei defnyddio i werthuso offer parod yn hytrach na manylu adeiladu pwrpasol. Byddwch yn llym am wahanu'r angen sylfaenol oddi wrth restr nodweddion gwerthwr, oherwydd bod gofyniad wedi'i ysgrifennu fel "mae angen cynnyrch X arnom" yn cau allan yn dawel ddewisiadau rhatach a fyddai wedi bodloni'r angen go iawn.

**Menter.** Mae graddfa'n troi gofynion yn gontract sy'n galluogi llawer o dimau i adeiladu un system gydlynol, felly'r flaenoriaeth yw proses safonol wedi'i chymhwyso'n gyson: categorïau diffiniedig, olrheiniadwyedd ddwyffordd o angen i brawf, un ffynhonnell awdurdodol, a newid dan reolaeth gyda llinellau sylfaen. Gwahanwch ofynion busnes, defnyddiwr, a system yn benodol a throsglwyddwch ofynion an-swyddogaethol i bensaernïaeth fel gyrwyr, fel na fydd rhwymedigaethau cwmpas ac ansawdd yn gwasgaru ar draws timau. Cyfunwch fanyleb ffurfiol ar gyfer rhwymedigaethau sefydlog, risg-uchel ag ymhelaethu ystwyth ymddygiad cynnyrch, a llywodraethwch y cydbwysedd yn ôl risg yn hytrach nag yn ôl dewis unrhyw dîm.

**Llywodraeth.** Mae rheolau caffael yn aml yn adeiladu'r contract cyfan o gwmpas manyleb gofynion, wedi'i strwythuro'n aml i safon fel IEEE 29148, felly mae manylder a chyflawnrwydd yn gontractiol, nid yn ddewisol. Cynhaliwch fatrics olrheiniadwyedd gofynion sy'n cysylltu pob gofyniad â dyluniad, achosion prawf, a thystiolaeth dderbyn, oherwydd bod taliad gwerthwr, archwiliad, a'r awdurdod i weithredu i gyd yn dibynnu ar orchudd wedi'i ddangos. Mae tryloywder ac atebolrwydd cyhoeddus yn codi'r bar ymhellach: rhaid i rwymedigaethau gorfodol ar gyfer hygyrchedd, preifatrwydd, a chadw cofnodion bob un ymddangos fel gofyniad penodol, gwiriadwy, ac yn syml, nid yw gofyniad heb dystiolaeth olrheiniedig, sy'n pasio, wedi'i ddanfon.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd pedwar person sy'n adeiladu ap amserlennu'n dal gofynion fel straeon defnyddiwr gyda meini prawf derbyn mewn ôl-groniad a rennir, nid manyleb ffurfiol. Cyn ysgrifennu'r nodwedd cydamseru calendr, mae'r sylfaenydd yn treulio prynhawn yn siarad â phum cwsmer darpar ac yn dysgu mai'r angen go iawn yw osgoi archebion dwbl ar draws dau declyn, nid y cydamseru yr oeddent wedi'i ragdybio. Mae'r un sgwrs honno'n ail-fframio'r stori ac yn arbed wythnos o adeiladu'r peth anghywir. Hyd yn oed ar y raddfa hon maent yn ysgrifennu ffynhonnell a rhesymeg pob stori i lawr, fel bod modd, pan fo blaenoriaethau'n newid, ollwng neu ail-weithio cwmpas heb ail-ddadlau pam yr oedd yn bodoli.

**Menter.** Mae banc rhyngwladol yn disodli ei blatfform tarddu benthyciadau. Mae'r tîm gofynion yn gwahanu gofynion busnes (lleihau amser cymeradwyo, bodloni rheoliadau benthyca), gofynion defnyddiwr (mae angen i swyddogion benthyciadau gymharu cynigion mewn un olygfa), a gofynion system (rhaid i'r platfform integreiddio â thair system graidd). Delir gofynion an-swyddogaethol (ymateb is-eiliad ar gyfer ymholiadau cyffredin, argaeledd 99.95%, amgryptio data personol) yn benodol a'u trosglwyddo i bensaernïaeth (pennod 3.1) fel gyrwyr. Olrheinir pob gofyniad drwy'r ôl-groniad i brofion derbyn awtomataidd. Felly pan fo rheoleiddiwr yn gofyn sut y gorfodir rheol fenthyca benodol, mae'r tîm yn dilyn yr olrhain o'r rheol i'r prawf sy'n ei gwirio.

**Llywodraeth.** Mae asiantaeth genedlaethol yn caffael system cymhwysedd budd-daliadau drwy gais tendr ffurfiol. Angorir y contract i fanyleb gofynion wedi'i strwythuro i IEEE 29148, yn gorchuddio rheolau cymhwysedd swyddogaethol, cydymffurfiaeth hygyrchedd orfodol, cyfyngiadau preifatrwydd a chadw cofnodion, a rheolaethau diogelwch. Mae matrics olrheiniadwyedd gofynion yn cysylltu pob gofyniad ag elfennau dyluniad, achosion prawf, a thystiolaeth dderbyn. Mae taliadau gwerthwr a'r awdurdod i weithredu (y gymeradwyaeth ffurfiol i redeg y system mewn cynhyrchiad) ill dau'n dibynnu ar orchudd wedi'i ddangos. Yn syml, nid ystyrir bod gofyniad heb dystiolaeth dderbyn olrheiniedig, sy'n pasio, wedi'i ddanfon, ni waeth beth mae'r meddalwedd yn ymddangos ei fod yn ei wneud.

## Achos busnes: cymhellion, ROI, a TCO

Mae'r ddadl economaidd dros beirianneg gofynion yn gorffwys ar gost trwsio diffygion yn hwyr. Mae astudiaethau diwydiant yn canfod yn gyson mai diffygion gofynion yw ymysg yr achosion mwyaf cyffredin a drutaf o fethiant prosiect, a bod cost trwsio diffyg yn dringo o urddiad maint o'r cyfnod gofynion i gynhyrchiad. Felly mae arian a dreulir yn egluro ac yn dilysu gofynion yn drosoledd go iawn: mae buddsoddiad cymedrol yn gynnar yn eich arbed rhag adeiladu, profi, a gweithredu'r peth anghywir.

Mae cost perchnogaeth gyfan gofynion yn cynnwys yr ymdrech barhaus o ennyn, manylu, offer, a rheoli newid ar draws oes gyfan y system; nid yw'n gost un-tro. Yn ei erbyn mae cost gofynion gwael: ailwaith, anghydfodau cwmpas, gorfynd amserlen, derbyn wedi methu, cosbau contractiol, ac, mewn lleoliadau rheoledig, dirwyon neu golli awdurdodiad. I arweinyddiaeth, fframiwch aeddfedrwydd gofynion fel lleihau risg a rhagfynegadwyedd. Olrheiniwch anwadalrwydd gofynion, tarddiad diffygion, a chyfran y gwaith a ddanfonwyd sy'n olrheiniadwy i angen dilysedig, a chysylltwch hyn â rhagolygu rheoli prosiect (pennod 10.6). Nid yw'r elw'n ymddangos fel nodwedd. Mae'n ymddangos fel y methiannau a'r ailwaith na ddigwyddodd byth.

## Gwrth-batrymau a pheryglon

- **Atebion wedi'u cuddio fel gofynion:** manylu technoleg neu gynllun sgrin a ddewiswyd yn lle'r angen sylfaenol, gan gau allan ddewisiadau gwell.
- **Iaith amwys:** "cyflym," "diogel," "greddfol" heb faen prawf mesuradwy, gan wneud y gofyniad yn amhosibl ei wirio.
- **[Aur-blatio](https://en.wikipedia.org/wiki/Gold_plating_(software_engineering)):** dal gofynion nad oes eu hangen ar unrhyw randdeiliad mewn gwirionedd, gan chwyddo cwmpas a chost.
- **Gofynion an-swyddogaethol coll:** darganfod rhwymedigaethau perfformiad, diogelwch, neu hygyrchedd dim ond ar ôl i bensaernïaeth gael ei sefydlu.
- **Ymledu gofynion:** y gwirionedd wedi'i wasgaru ar draws negeseuon e-bost, tocynnau, a sleidiau heb ffynhonnell awdurdodol.
- **Newid wedi'i rewi neu heb ei reoli:** naill ai gwrthod pob newid neu dderbyn pob newid heb asesiad effaith.
- **Dim olrheiniadwyedd:** anallu i ateb beth y mae newid yn effeithio arno neu pam mae nodwedd yn bodoli, sy'n angheuol mewn systemau a archwilir.
- **Parlys dadansoddi:** manylu diddiwedd sy'n oedi dysgu o feddalwedd sy'n gweithio.
- **Rhanddeiliaid wedi'u hanwybyddu:** gweithredwyr, archwilwyr, a di-ddefnyddwyr yr effeithir arnynt wedi'u gadael allan hyd nes derbyn.

## Model aeddfedrwydd

- **Lefel 1, Cychwyn.** Mae gofynion yn ymhlyg neu ar lafar, wedi'u dal yn anghyson ac yn adweithiol. Mae anghydfodau cwmpas ac ailwaith yn gyffredin; nid oes olrheiniadwyedd, dim meini prawf derbyn, a dim proses ddiffiniedig.
- **Lefel 2, Datblygu.** Mae rhai timau'n ysgrifennu gofynion i lawr ac yn eu holrhain fesul prosiect, gyda blaenoriaethu sylfaenol a thrin newid ad hoc. Mae arferion yn bodoli ond yn amrywio yn ôl tîm a pherson, felly mae categorïau, ffurfioldeb, ac ansawdd yn anghyson ar draws y sefydliad.
- **Lefel 3, Safoni.** Dogfennir a gorfodir proses ofynion safonol drwy'r sefydliad: categorïau diffiniedig, arferion ennyn a dilysu, meini prawf derbyn ynghlwm adeg awduro, un ffynhonnell awdurdodol, ac olrheiniadwyedd ddwyffordd o angen i brawf, wedi'i haddasu'n gyson i gyd-destun ystwyth neu gynllun-yrredig.
- **Lefel 4, Rheoli.** Mesurir a rheolir y broses â data. Olrheinir anwadalrwydd gofynion, tarddiad diffygion, gorchudd olrheiniadwyedd, a chyfran y gwaith a ddanfonwyd sy'n olrheiniadwy i angen dilysedig yn erbyn llinellau sylfaen; mae olrheiniadwyedd yn ymestyn at dystiolaeth dderbyn a chydymffurfiaeth; ac mae metrigau gofynion yn bwydo rhagolygu prosiect (pennod 10.6), fel bod penderfyniadau newid ac ansawdd yn gorffwys ar dystiolaeth yn hytrach na barn.
- **Lefel 5, Cerddorfa.** Gwellir arfer gofynion yn barhaus a'i integreiddio ar draws y sefydliad. Cyweirir ffurfioldeb yn addasol yn ôl risg a chanlyniad, mae offer ennyn ac olrheiniadwyedd yn cysylltu â darganfod, pensaernïaeth, a danfoniad, ac mae'r sefydliad yn defnyddio ei hanes mesur ei hun i atal diffygion gofynion sy'n ailadrodd cyn iddynt gyrraedd cod.

## Syniadau ar gyfer trafodaeth

- Sut ydych chi'n gwahaniaethu rhwng gofyniad gwirioneddol ac ateb cynamserol pan fo rhanddeiliad uwch yn ei ddatgan fel ateb?
- Pa lefel o ffurfioldeb gofynion sy'n gywir ar gyfer eich system risg-uchaf yn erbyn eich un risg-isaf, a phwy sy'n penderfynu?
- Sut ydych chi'n cadw olrheiniadwyedd ddwyffordd yn gyfredol mewn ôl-groniad ystwyth cyflym-symudol heb iddi ddod yn faich biwrocrataidd?
- Pa ofynion an-swyddogaethol sy'n cael eu darganfod yn rhy hwyr amlaf yn eich sefydliad, a pham?
- Mewn rhaglen reoledig, beth sy'n cyfansoddi tystiolaeth dderbyn ddigonol i ddangos bod gofyniad wedi'i fodloni?
- Sut ddylai offer ennyn a manylu â chymorth AI newid eich arfer gofynion, a pha risgiau newydd y maent yn eu cyflwyno?

## Casgliadau allweddol

- Mae gofynion yn nodi anghenion a chyfyngiadau, nid atebion; rhaid iddynt fod yn angenrheidiol, yn ddiamwys, yn wiriadwy, ac yn olrheiniadwy.
- Gwahanwch ofynion swyddogaethol, an-swyddogaethol, a chyfyngiadol, a'r lefelau busnes, defnyddiwr, a system.
- Ennynwch o randdeiliaid go iawn, dadansoddwch a blaenoriaethwch, manylwch ar ffurfioldeb priodol, dilyswch cyn adeiladu, a rheolwch newid.
- Olrheiniadwyedd ddwyffordd o angen i dystiolaeth dderbyn yw asgwrn cefn atebolrwydd, yn enwedig mewn lleoliadau rheoledig.
- Mae cyd-destunau ystwyth a chynllun-yrredig yn rhannu'r un gweithgareddau; maent yn wahanol o ran amseriad, ffurfioldeb, ac arteffactau, felly dewiswch yn ôl risg.
- Telir cost gofynion gwael yn hwyr ac fe'i lluosir; mae buddsoddi'n gynnar yn drosoledd yn erbyn ailwaith a derbyn wedi methu.

## Cyfeiriadau a darllen pellach

- IEEE ac ISO/IEC, *Guide to the Software Engineering Body of Knowledge (SWEBOK)*, maes gwybodaeth Gofynion Meddalwedd
- Karl Wiegers a Joy Beatty, *Software Requirements*
- ISO/IEC/IEEE 29148, *Systems and software engineering: Life cycle processes: Requirements engineering*
- Suzanne Robertson a James Robertson, *Mastering the Requirements Process*
- Dean Leffingwell, *Agile Software Requirements*
- Mike Cohn, *User Stories Applied*
- Ian Sommerville, *Software Engineering* (penodau peirianneg gofynion)
