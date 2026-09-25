# 6.7 Asiantau deallusrwydd artiffisial a systemau asiantol

## Trosolwg a chymhelliant

Mae **asiant deallusrwydd artiffisial** yn [fodel iaith mawr](https://en.wikipedia.org/wiki/Large_language_model) (LLM) wedi'i lapio mewn dolen: rhoddir nod iddo, gall alw teclynnau, mae'n cadw rhywfaint o gof o'r hyn y mae wedi'i wneud, ac mae'n penderfynu ei gam nesaf ei hun nes bod y nod yn cael ei fodloni neu ei fod yn rhoi'r gorau iddi. Y ddolen honno yw'r gwahaniaeth cyfan rhwng asiant a galwadau syml anogaeth-ac-ymateb pennod 6.3. Mae un alwad yn ateb cwestiwn. Mae asiant yn darllen ei e-bost, yn chwilio cronfa ddata, yn ffeilio tocyn, yn gwirio'r canlyniad, ac yn ceisio eto. Nid yw'r model bellach dim ond yn cynhyrchu testun; mae'n dewis gweithredoedd yn eich systemau.

Mae'r newid hwnnw'n newid y broblem beirianneg. Pan fydd model ond yn ysgrifennu geiriau, mae allbwn gwael yn frawddeg wael. Pan fydd model yn gyrru teclynnau, gall allbwn gwael anfon neges anghywir, dileu cofnod, neu symud arian. Felly deellir [asiant deallus](https://en.wikipedia.org/wiki/Intelligent_agent) orau fel cynlluniwr heb ymddiriedaeth yn eistedd o fewn system ymddiriededig, ac mae'r rhan fwyaf o'ch gwaith yn mynd i mewn i ffinio'r hyn y caiff y cynlluniwr hwnnw ei ganiatáu i'w wneud. Mae'r bennod hon yn adeiladu'n uniongyrchol ar sylfeini LLM pennod 6.3, pryderon ymddiriedaeth ac atebolrwydd pennod 6.5, ac arferion platfform pennod 6.6.

I dimau mawr mae'r peryglon yn sefydliadol yn ogystal â thechnegol. Mae mentrau eisiau asiantau wedi'u gwifro i mewn i systemau mewnol go iawn (tocynnau, cyllid, cofnodion cwsmeriaid), sy'n golygu bod asiantau'n etifeddu rheolaethau mynediad go iawn a rhwymedigaethau rheoli newid go iawn. Mae llywodraeth yn ychwanegu atebolrwydd cyhoeddus: rhaid i weithred ymreolaethol sy'n effeithio ar ddinesydd fod yn eglurhadwy, yn oruchwylladwy, ac yn archwiliadwy ar ôl y ffaith. Mae'r patrwm yn bwerus. Wedi'i ddefnyddio heb ddisgyblaeth, mae'n ffordd gyflym o awtomeiddio camgymeriadau.

## Egwyddorion allweddol

- Mae asiant yn fodel ynghyd â dolen, teclynnau, cof, a nod. Mae'r risg yn byw yn y ddolen, nid yn y rhyddiaith.
- Ffinio ymreolaeth i'r dasg. Rhowch y lleiaf o ryddid sy'n gorffen y gwaith.
- Ffafriwch lif gwaith sefydlog pan fo'r camau'n hysbys. Estynnwch am ymreolaeth agored-ei-ben dim ond pan nad ydynt.
- Triniwch bob teclyn fel arwyneb ymosod a rhowch iddo'r fraint leiaf y gall weithio ag ef.
- Rhowch ddyn yn y ddolen ar gyfer gweithredoedd canlyniadol neu anadferadwy, a gwnewch wrthdroi'n rhad.
- Gwerthuswch ar lwyddiant tasgau, nid ar sut mae'r trawsgrifiad yn darllen.
- Olrheiniwch bob rhediad. Mae gweithred na allwch ei hailadeiladu'n weithred na allwch ei llywodraethu.
- Fel arfer, y dyluniad symlaf sy'n gweithio yw'r un cywir. Yn aml nid yw hwnnw'n asiant o gwbl.

## Argymhellion

### Dechrau gyda llif gwaith, ychwanegu ymreolaeth dim ond lle mae'n rhaid

Y camgymeriad mwyaf cyffredin yw estyn am asiant ymreolaethol pan fyddai piblinell sefydlog yn gwneud y tro. Os ydych chi eisoes yn gwybod y camau (echdynnu meysydd, eu dilysu, chwilio am gofnod, drafftio ateb), ysgrifennwch hynny fel llif gwaith wedi'i gerfio gyda'r model yn llenwi slotiau penodol. Mae ymreolaeth yn ennill ei chadw pan na ellir rhagbennu'r llwybr mewn gwirionedd, er enghraifft ymchwil agored-ei-ben neu drefnu blaenoriaeth ar draws llawer o declynnau posibl. Ffiniwch yr ymreolaeth i'r dasg: capiwch nifer y camau, cyfyngwch y set declynnau i'r hyn sydd angen y nod hwn, a gosodwch amod stopio clir. Rheol dda yw rhoi i'r model union gymaint o ryddid ag y mae'r broblem yn ei fynnu a dim un radd yn fwy.

### Gwneud defnydd o declynnau'n allu craidd, a'i wneud yn ddiogel

Defnydd teclynnau (a elwir hefyd yn alw ffwythiannau) yw'r hyn sy'n troi model yn asiant. Diffiniwch bob teclyn gyda sgema union, dilyswch bob ymresymiad y mae'r model yn ei ddarparu, a chymhwyswch [egwyddor y fraint leiaf](https://en.wikipedia.org/wiki/Principle_of_least_privilege): mae asiant adrodd darllen-yn-unig yn cael credentialau darllen-yn-unig, byth mynediad ysgrifennu y gallai ei gam-ddefnyddio. Rhedwch declynnau y tu mewn i [flwch tywod](https://en.wikipedia.org/wiki/Sandbox_(computer_security)) fel na all alwad wael gyrraedd y tu hwnt i'w radiws ffrwydro. Ffafriwch lawer o declynnau cul, un-pwrpas dros ychydig eang, oherwydd mae teclyn cul yn haws ei resymu, ei ganiatáu, a'i archwilio. Dyma'r un ataliaeth y mae pennod 6.3 yn ei hannog ar gyfer defnydd teclynnau LLM, wedi'i gwneud yn ganolog.

### Defnyddio patrymau ymresymu a chynllunio eglur

Mae asiantau'n gweithio'n well pan fydd eu meddwl wedi'i strwythuro. Mewn patrwm ymresymu-a-gweithredu (a boblogeiddiwyd gan yr ymchwil ReAct), mae'r model yn eiledu rhwng ymresymu am y sefyllfa a chymryd gweithred, yna'n arsylwi'r canlyniad cyn ymresymu eto. Ar gyfer nodau anos, gadewch i'r model gynllunio yn gyntaf (dadelfennu'n is-dasgau) ac yna gweithredu, fel y gallwch archwilio a hyd yn oed gymeradwyo'r cynllun cyn i unrhyw declyn redeg. Cadwch y dolenni hyn yn arsylladwy ac yn haddasadwy. Mae cynllun y gallwch ei ddarllen yn gynllun y gallwch ei stopio.

### Cadw dynion yn y ddolen ar gyfer gweithredoedd canlyniadol

Penderfynwch, fesul teclyn a fesul gweithred, a gaiff y model weithredu ar ei ben ei hun neu a rhaid iddo ofyn yn gyntaf. Gall gweithredoedd gwrthdroadwy, risg-isel (chwilio, drafftio) redeg heb neb yn gwylio. Mae angen giât [dyn-yn-y-ddolen](https://en.wikipedia.org/wiki/Human-in-the-loop) ag awdurdod go iawn i ddweud na ar rai canlyniadol neu anadferadwy (anfon cyfathrebiadau allanol, symud arian, newid data cynhyrchu, penderfynu achos dinesydd). Dyluniwch ar gyfer gwrthdroadwyedd lle bynnag y gallwch: ffafriwch lwyfannu newid dros ei gyflawni, a gwnewch dadwneud yn nodwedd dosbarth-cyntaf fel bod gweithred gamsyniedig yn costio munudau, nid digwyddiad.

### Trin y model diogelwch fel un gwrthwynebus

Mae asiantau'n ehangu'r arwyneb ymosod a ddisgrifir ym mhennod 4.2. Y bygythiad pennaf yw [chwistrelliad anogaeth](https://en.wikipedia.org/wiki/Prompt_injection): cyfarwyddiadau maleisus wedi'u cuddio mewn tudalen we, dogfen, neu e-bost y mae'r asiant yn ei ddarllen ac yn ufuddhau iddo. Yn agos gysylltiedig â hyn mae [problem y dirprwy dryslyd](https://en.wikipedia.org/wiki/Confused_deputy_problem), lle mae ymosodwr yn twyllo asiant breintiedig i gam-ddefnyddio ei fynediad cyfreithlon ei hun, er enghraifft allfudo data trwy declyn y caniateir i'r asiant ei alw. Tybiwch y gall unrhyw gynnwys y mae'r asiant yn ei lyncu fod yn elyniaethus. Gwahanwch gyfarwyddiadau ymddiriededig oddi wrth ddata heb eu hymddiried, cyfyngwch declynnau fel na all asiant wedi'i herwgipio gyrraedd systemau sensitif, a byth peidiwch â gadael i allbwn crai'r model sbarduno gweithred anadferadwy heb ddilysu.

### Gwerthuso ar lwyddiant tasgau ac ail-brofi atchweliad yr an-benderfyniaeth

Barnwch asiantau ar sail a ydynt yn cyflawni'r dasg, nid ar sail a yw'r trawsgrifiad yn swnio'n glyfar. Adeiladwch set werthuso o nodau cynrychioliadol gyda meini prawf llwyddiant y gellir eu gwirio (a gafodd y tocyn y flaenoriaeth gywir, a oedd yr ad-daliad yn cyfateb i'r polisi) a'i rhedeg ar bob newid anogaeth, model, neu declyn. Gan fod asiantau'n an-benderfynol, ychydig y mae un rhediad yn ei brofi: rhedwch bob achos sawl gwaith a thraciwch gyfradd lwyddiant, nid pasio neu fethu. Mae hyn yn ymestyn disgyblaeth gwerthuso all-lein a chysylltiedig pennod 6.3 a 6.2 (peirianneg dysgu peiriant a MLOps) i systemau y mae eu hallbwn yn ddilyniant o weithredoedd.

### Offeryna rhediadau ar gyfer arsylladwyedd, cost, a thrin methiant

Ni allwch lywodraethu'r hyn na allwch ei weld. Olrheiniwch bob rhediad asiant o ben i ben (pennod 6.6): y nod, pob cam ymresymu, pob galwad teclyn gyda'i ymresymiadau a'i ganlyniad, y tocynnau a wariwyd, a'r canlyniad terfynol. Mae'r olrhain hwn yn ddadfygiwr i chi, yn drywydd archwilio, ac yn fesurydd cost ar unwaith. Gosodwch gyllidebau caled ar gamau, amser, a gwariant, oherwydd gall asiant sy'n dolennu losgi hwyrni ac arian yn gyflym. Triniwch fethiant yn eglur: ail-geisiwch wallau teclyn dros dro gyda chiliad, ond canfyddwch ddolenni lle mae'r model yn ailadrodd gweithred aflwyddiannus, a methwch yn ddiogel yn hytrach na chynhyrfu.

## Cyfaddawdau: manteision ac anfanteision

| Dewis | Manteision | Anfanteision | Gorau pan |
|---|---|---|---|
| Llif gwaith sefydlog (model yn llenwi slotiau) | Rhagweladwy, rhad, hawdd ei brofi a'i archwilio | Anhyblyg; yn torri ar lwybrau annisgwyl | Mae'r camau'n hysbys ymlaen llaw |
| Asiant unigol ymreolaethol | Hyblyg; yn trin nodau agored-eu-pen | Anos ei reoli, ei werthuso, a'i ffinio | Ni ellir rhagbennu'r llwybr |
| Cerddorfa aml-asiant | Cyfochredd; rolau arbenigol | Cost cydgysylltu, gwallau'n cyfansymio, gwariant uwch | Mae tasg wir yn dadelfennu'n rannau annibynnol |
| Gweithred heb neb yn gwylio | Cyflym, ychydig o ffrithiant | Mae camgymeriadau'n gweithredu heb wiriad | Mae gweithredoedd yn wrthdroadwy ac yn risg-isel |
| Giât dyn-yn-y-ddolen | Diogelwch, atebolrwydd, gwrthdroadwyedd | Arafach; angen gallu adolygwr | Mae gweithredoedd yn ganlyniadol neu'n anadferadwy |

Y tensiwn canolog yw ymreolaeth yn erbyn rheolaeth. Mae mwy o ymreolaeth yn trin mwy o sefyllfaoedd ond yn mynnu mwy o waliau cadw, mwy o werthuso, a mwy o arian, ac mae'n methu mewn ffyrdd sy'n anos eu rhagweld. Mae dyluniadau aml-asiant yn temtio timau ag ceinder, ac eto mae pob asiant ychwanegol yn ychwanegu traul cydgysylltu a lle arall i wall bach gyfansymio'n ganlyniad anghywir. Datryswch y tensiwn drwy ddechrau gyda'r ymreolaeth leiaf sy'n datrys y broblem ac ychwanegu rhyddid dim ond pan fydd tasg benodol yn eich gorfodi, bob amser wedi'i barru â wal gadw gyfatebol.

## Cwestiynau i'w trafod gyda'ch tîm

1. **A oes gwir angen asiant ar gyfer y nodwedd hon, neu a fyddai llif gwaith sefydlog yn fwy diogel ac yn rhatach?** Mae ymreolaeth yn ddeniadol, ond mae gan y rhan fwyaf o swyddi gamau y gellir eu gwybod ymlaen llaw y mae piblinell wedi'i cherfio'n eu trin gyda llawer llai o risg. I dîm mawr, mae rhagosod tuag at asiantau'n golygu bod pob grŵp yn ysgwyddo beichiau gwerthuso, olrhain, a diogelwch y byddai dyluniad symlach yn eu hosgoi. Dewch â'r dasg benodol a gofynnwch a ellir rhagbennu ei chamau; os gellir, mae asiant yn debygol o fod yn or-beirianneg. Cadwch ymreolaeth agored-ei-ben ar gyfer nodau lle mae'r llwybr wir yn amrywio fesul achos. Dylai'r ateb wthio'r rhan fwyaf o nodweddion tuag at lif gwaith a gadael set fach, fwriadol fel asiantau go iawn.

2. **Ar gyfer pob teclyn y gall ein hasiant ei alw, beth yw'r peth gwaethaf y gallai asiant wedi'i herwgipio ei wneud ag ef, a beth sy'n atal hynny?** Mae ymosodiadau chwistrelliad anogaeth a dirprwy-dryslyd yn troi mynediad cyfreithlon eich asiant ei hun yn eich erbyn, felly'r lens gywir yw un wrthwynebus (pennod 4.2). Cymerwch stoc o bob teclyn, ei gwmpas braint, ac a allai cyfarwyddyd maleisus wedi'i smyglo trwy gynnwys wedi'i lyncu ei gyrraedd. I fentrau sy'n gwifro asiantau i mewn i systemau mewnol, dyma lle mae braint leiaf, blychau tywod, a giatiau dynol ar weithredoedd anadferadwy'n dod yn real. Dewch â'r rhestr declynnau a'r credentialau y mae pob un yn eu dal. Os gellir cyrraedd unrhyw weithred ganlyniadol heb ddilysu neu wiriad dynol, dyna'r peth cyntaf i'w drwsio.

3. **Sut y byddem yn gwybod bod cyfradd lwyddiant asiant wedi gostwng, o gofio bod pob rhediad yn edrych yn gredadwy?** Mae asiantau'n an-benderfynol, felly gall trawsgrifiad sy'n darllen yn dda fod wedi cymryd y weithred anghywir o hyd, ac nid yw un rhediad gwyrdd yn profi dim byd. Gofynnwch a oes gennych set werthuso o nodau â chanlyniadau y gellir eu gwirio, wedi'i rhedeg sawl gwaith fesul achos i gynhyrchu cyfradd lwyddiant yn hytrach na phas sengl. Ar gyfer defnyddiadau risg-uchel neu gyhoeddus, trafodwch sut mae traciau rhediad yn eich galluogi i ailadeiladu union yr hyn a ddigwyddodd pan fydd rhywbeth yn mynd o'i le (penodau 6.5 a 6.6). Os mai'ch unig signal yw cwynion defnyddwyr, rydych chi eisoes yn rhy hwyr. Dylai'r ateb ariannu harnais gwerthuso cyn graddfa, nid ar ei hôl hi ar ôl digwyddiad.

4. **Pa rai o weithredoedd yr asiant hwn sy'n wirioneddol anadferadwy, pwy sy'n dal awdurdod i'w cymeradwyo, ac a oes gennym alluoedd adolygwyr i staffio'r giât honno?** Y demtasiwn yw gadael i'r model weithredu heb neb yn gwylio ym mhobman, ond nid yw giât ddynol yn real ond os yw person a enwir ag awdurdod i ddweud na ar gael pan fydd yr asiant yn gofyn. I dîm mawr, mae ciw cymeradwyo nad oes neb yn berchen arno'n dawel yn dod yn stamp rwber, ac mae'r diogelwch a ddyluniwyd gennych yn anweddu o dan gyfaint. Dewch â'r rhestr lawn o weithredoedd y gall yr asiant eu cymryd, marciwch bob un yn wrthdroadwy neu'n anadferadwy, ac amcangyfrifwch gyfaint dyddiol yr achosion hyder-isel a fyddai'n glanio ar adolygwr. Pwyswch ffrithiant a chost staffio giât yn erbyn radiws ffrwydro camgymeriad heb neb yn gwylio, a ffafriwch ailddylunio gweithred anadferadwy'n un wedi'i llwyfannu, y gellir ei dadwneud, dros ychwanegu adolygwr arall. Mewn lleoliadau menter a llywodraeth, cysylltwch bob gweithred ganlyniadol â swyddog atebol a chofnod rheoli newid, oherwydd mae gweithred ymreolaethol sy'n effeithio ar ddinesydd neu gwsmer na wnaeth unrhyw ddyn ei chymeradwyo yn union y methiant y bydd archwiliad yn ei ganfod.

5. **A ydym yn estyn am ddyluniad aml-asiant oherwydd bod y dasg wir yn dadelfennu, neu oherwydd ei fod yn edrych yn gain?** Mae rhannu gwaith ar draws asiantau arbenigol yn ddeniadol, ac eto mae pob asiant ychwanegol yn ychwanegu traul cydgysylltu a lle arall lle mae gwall bach yn cyfansymio'n ganlyniad anghywir. I sefydliad mawr nid dim ond gwariant a hwyrni yw'r gost: mae system aml-asiant yn llawer anos ei holrhain, ei gwerthuso, a'i rhesymu pan fydd yn methu, felly mae'r baich llywodraethu'n lluosi gyda phob rôl a ychwanegwch. Dewch â'r dasg a dangoswch, yn benodol, pa rannau sy'n rhedeg yn annibynnol ac yn gyfochrog, yna cymharwch y gyfradd lwyddiant a'r gost fesuredig o fersiwn aml-asiant yn erbyn asiant unigol ar yr un set werthuso. Os yw'r asiant unigol yn ennill neu'n cydraddoli, mae'r dyluniad cain yn or-beirianneg. Ar gyfer defnyddiadau reoleiddiedig neu gyhoeddus, cofiwch fod pob asiant yn y gadwyn yn gydran arall y mae'n rhaid i gorff goruchwylio allu ei harchwilio, felly mae strwythur ychwanegol na allwch ei gyfiawnhau'n atebolrwydd ychwanegol.

6. **Beth yw'r cyllidebau caled ar gamau, amser, a gwariant asiant, a sut y byddai asiant sy'n dolennu'n cael ei ddal cyn iddo redeg cost neu hwyrni i fyny?** Gall asiant sy'n ailadrodd gweithred aflwyddiannus losgi arian ac amser heb rybudd, felly mae ymreolaeth di-ffin yn risg ariannol yn ogystal â diogelwch. I dîm mawr sy'n rhedeg llawer o asiantau, gall un ddolen gamymddwyn godi bil cwmwl neu ddihysbyddu terfyn cyfradd sy'n newynu pob llwyth gwaith arall, sy'n gwneud capiau fesul rhediad yn bryder gweithredol a rennir yn hytrach na phroblem un tîm. Dewch â'r cyllidebau cam, amser, a thocyn cyfredol ar gyfer pob asiant, y rhybuddio sy'n tanio pan fydd rhediad yn eu rhagori, a'r canfod dolen sy'n methu'n ddiogel yn hytrach na chynhyrfu. Pwyswch gyllidebau tynn, a allai dorri tasg wir anodd i ffwrdd, yn erbyn rhai llac sy'n gadael cost i redeg yn rhemp. Mewn lleoliadau menter a llywodraeth lle mae'n rhaid rhagolwg a chyfiawnhau gwariant, mae asiant y mae ei gost yn ddi-ffin yn eitem llinell na allwch ei hamddiffyn mewn adolygiad cyllideb neu archwiliad.

## Lens sector

**Cwmni newydd.** Cludwch un asiant cul sy'n cyffwrdd â'ch gwerth craidd, ar fodel wedi'i letya, gyda'r set declynnau leiaf sy'n gwneud y gwaith a chap caled ar gamau a gwariant. Gwrthsefwch y demo aml-asiant: mae eich sylw peirianyddol prin yn cael ei wario'n well yn ffinio ymreolaeth un asiant ac yn olrhain ei rediadau na chydgysylltu rolau na allwch eu cynnal. Cadwch bob gweithred ganlyniadol y tu ôl i un giât "drafftio, byth anfon" fel bod camgymeriad yn costio clic i'w ddadwneud, nid digwyddiad.

**Busnes bach.** Nid oes gennych neb i redeg harnais gwerthuso neu flwch tywod, felly ffafriwch asiantau wedi'u hymgorffori mewn offer rydych chi eisoes yn ymddiried ynddynt, a throwch ymlaen dim ond yr ymreolaeth y gallwch ei goruchwylio â llygad. Triniwch unrhyw asiant a all anfon, talu, neu ddileu ar eich rhan fel rhywbeth i'w gadw i ffwrdd nes bod person yn cadarnhau pob gweithred, oherwydd mae neges awtomataidd anghywir i gwsmer yn costio'r berthynas i chi. Ffafriwch werthwyr sy'n dangos i chi beth wnaeth yr asiant ac yn gadael i chi ddiffodd yr awtomeiddiad.

**Menter.** Y broblem yw llywodraethu asiantau ar draws llawer o dimau: patrymau a rennir ar gyfer ffinio ymreolaeth, credentialau teclyn braint-leiaf, blychau tywod, giatiau dyn-yn-y-ddolen, ac olrhain pen-i-ben fel nad oes unrhyw grŵp yn ailddyfeisio'r waliau cadw. Gwifrwch asiantau i mewn i systemau mewnol o dan yr un rheolaethau mynediad y byddai dyn yn eu dal, giatiwch weithredoedd anadferadwy y tu ôl i gymeradwywyr wedi'u henwi a rheoli newid, a rheolwch y portffolio gyda metrigau cyfradd-lwyddiant, cyllidebau fesul rhediad, a phrofi chwistrelliad gwrthwynebus. Safonwch yr haen olrhain a gwerthuso fel y gellir ailadeiladu ac archwilio ymddygiad unrhyw asiant.

**Llywodraeth.** Mae caffael, tryloywder, ac atebolrwydd cyhoeddus yn ffinio pob dewis. Cadwch asiantau i gasglu ffeithiau a drafftio, a chadwch bob penderfyniad sy'n effeithio ar ddinesydd i ddyn atebol, oherwydd ni ellir dirprwyo cyfrifoldeb am benderfyniad sector-cyhoeddus i fodel. Cofnodwch bob rhediad fel y gall corff goruchwylio weld pa ffynonellau a ymgynghorwyd a beth a wnaed, mynnwch fod gwerthwyr yn datgelu teclynnau a chyfyngiadau'r asiant, a phrofwch trwy set werthuso wrthwynebus fod yr asiant yn gwrthod gweithredu y tu hwnt i'w gylch gwaith ffiniedig.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd dadansoddeg pum person yn adeiladu asiant trefnu blaenoriaeth cymorth. Mae'n darllen tocyn sy'n dod i mewn, yn chwilio'r dogfennau, ac naill ai'n drafftio ateb neu'n llwybro'r tocyn at ddyn, a dyna'r set declynnau gyfan. Y credentialau yw darllen-yn-unig ynghyd ag un gweithred "creu drafft" na fydd byth yn anfon heb i berson glicio anfon. Mae pob rhediad wedi'i olrhain fel y gall y sylfaenwyr weld pam y cafodd tocyn ei lwybro fel y gwnaeth, ac mae set werthuso nosweithiol o hanner cant o docynnau go iawn yn rhedeg yr asiant bum gwaith yr un i dracio cyfradd cywirdeb llwybro. Pan fydd demo aml-asiant clyfar cystadleuydd yn eu temtio, maen nhw'n aros yn un-asiant oherwydd nad yw eu tasg yn dadelfennu.

**Menter.** Mae banc yn adeiladu asiant i helpu staff gweithrediadau gymodi taliadau wedi methu. Mae'n integreiddio â systemau mewnol o dan yr un rheolaethau mynediad sydd gan glerc dynol, wedi'u caniatáu trwy gredentialau gwasanaeth braint-leiaf wedi'u cwmpasu i gymodi yn unig. Gall yr asiant ymchwilio'n rhydd (darllen cyfrifon, chwilio hanes trafodion) ond mae unrhyw weithred sy'n symud arian neu'n golygu cofnod wedi'i llwyfannu ac yn mynnu cymeradwywr dynol wedi'i enwi, gan fodloni rheoli newid. Mae dogfennau wedi'u llyncu'n cael eu trin fel rhai heb eu hymddiried i bylu chwistrelliad anogaeth, mae teclynnau'n rhedeg mewn blwch tywod, ac mae pob rhediad wedi'i olrhain o ben i ben ar gyfer archwilio. Mae set werthuso all-lein yn giatio pob newid model neu anogaeth, ac mae cyllidebau fesul rhediad yn capio camau a gwariant fel na all asiant sy'n dolennu redeg cost neu hwyrni i fyny.

**Llywodraeth.** Mae asiantaeth budd-daliadau'n peilota asiant i helpu gweithwyr achos gasglu'r ffeithiau ar gyfer hawliad: tynnu cofnodion, gwirio rheolau cymhwysedd, a drafftio crynodeb. Mae'r asiantaeth yn tynnu llinell galed: mae'r asiant yn casglu ac yn drafftio, ond mae gweithiwr achos dynol yn gwneud ac yn berchen ar bob penderfyniad sy'n effeithio ar ddinesydd, oherwydd ni ellir dirprwyo atebolrwydd am benderfyniadau sector-cyhoeddus i fodel (pennod 6.5). Mae pob rhediad wedi'i gofnodi'n llawn, gan ddangos pa ffynonellau a ymgynghorwyd a beth a ddrafftiwyd, fel y gall corff goruchwylio archwilio unrhyw achos. Mae ymreolaeth wedi'i ffinio'n fwriadol i ddarllen-a-drafftio, mae teclynnau'n rhai braint-leiaf ac mewn blwch tywod, ac mae set werthuso wrthwynebus yn cadarnhau bod yr asiant yn gwrthod gweithredu y tu hwnt i gasglu ffeithiau.

## Achos busnes: cymhellion, ROI, a TCO

Mae asiantau'n cyflenwi enillion trwy awtomeiddio gwaith aml-gam a arferai fod angen person i glicio rhwng systemau: trefnu blaenoriaeth, cymodi, ymchwil, a gweithrediadau rheolaidd. Mae'r gwerth yn ymddangos fel gwaith wedi'i gwblhau heb ddyn ym mhob cam, amseroedd cylch cyflymach, a staff wedi'u rhyddhau ar gyfer tasgau trwm-o-farn. Gan fod asiantau'n adeiladu ar LLMs a theclynnau presennol, mae'r amser i brototeip gweithredol yn fyr, sef yn union pam mae timau'n gorddylunio.

Dyma lle mae asiantau'n gwahaniaethu oddi wrth nodweddion LLM syml o ran cyfanswm cost perchnogaeth. Ar ben cost casgliad rydych chi'n talu am yr integreiddiadau teclyn, y plymwaith blwch tywod a chaniatâd, y harnais gwerthuso, y stac olrhain ac arsylladwyedd (pennod 6.6), a'r adolygwyr dynol sy'n staffio'r giatiau cymeradwyo. Mae asiant sy'n dolennu neu wedi'i ffinio'n wael yn ychwanegu cost newidiol a all godi heb rybudd, felly mae cyllidebau ar gamau a gwariant yn rhan o'r dyluniad, nid yn ôl-ystyriaeth. Cost peidio â mabwysiadu yw gweithrediadau arafach a llafur â llaw y mae eich cystadleuwyr yn ei awtomeiddio. Cost mabwysiadu'n ddiofal yw gweithred ymreolaethol sy'n anfon y neges anghywir, yn gollwng data, neu'n gwneud penderfyniad diatebolrwydd. Gwnewch yr achos i arweinyddiaeth trwy barru un targed awtomeiddio penodol â chynllun penodol ar gyfer waliau cadw, gwerthuso, a goruchwyliaeth ddynol, a thrwy fod yn onest mai'r waliau cadw yw'r rhan fwyaf o'r gost.

## Gwrth-batrymau a pheryglon

- **Asiant pan fyddai llif gwaith yn gwneud y tro.** Cymryd risg lawn ymreolaeth ar gyfer tasg roedd ei chamau'n hysbys.
- **Teclynnau a chredentialau gor-eang.** Un teclyn "gwneud unrhyw beth" yn lle rhai cul, braint-leiaf.
- **Dallineb chwistrelliad anogaeth.** Bwydo cynnwys heb ei ymddiried i asiant sy'n dal breintiau go iawn.
- **Dim giât ddynol ar weithredoedd anadferadwy.** Gadael i'r model anfon, talu, neu ddileu heb wiriad.
- **Theatr aml-asiant.** Rhannu tasg syml ar draws asiantau, gan dalu cost cydgysylltu am ddim enillion.
- **Gwerthuso seiliedig-ar-deimladau.** Barnu yn ôl sut mae'r trawsgrifiad yn darllen yn lle cyfradd lwyddiant tasgau.
- **Dolenni di-ffin.** Dim cap ar gamau, amser, na gwariant, fel bod asiant sownd yn llosgi arian a hwyrni.
- **Rhediadau heb eu holrhain.** Dim cofnod o'r hyn a wnaeth yr asiant, gan eich gadael yn analluog i ddadfygio, archwilio, na chyfrif.

## Model aeddfedrwydd

- **Lefel 1, Cychwyn:** Mae asiantau'n cael eu prototeipio ad hoc gyda mynediad teclyn eang a dim ffiniau. Barnir llwyddiant gan ddemos, yn adweithiol, ar ôl i rywbeth dorri. Nid oes set werthuso, dim olrhain, a dim giât ddynol ar weithredoedd canlyniadol.
- **Lefel 2, Datblygu:** Mae gan rai asiantau ddolenni wedi'u ffinio a theclynnau braint-leiaf, ac mae olrhain sylfaenol yn bodoli, ond mae arfer yn amrywio o dîm i dîm. Mae set werthuso â llaw yn dal atchweliadau bras mewn ychydig o brosiectau tra nad oes gan eraill unrhyw un. Mae cymeradwyaeth ddynol yn gwarchod y gweithredoedd anadferadwy amlycaf, ac eto mae sylw'n anghyson ac heb ei ddogfennu.
- **Lefel 3, Safoni:** Mae patrymau a rennir yn llywodraethu ymreolaeth, caniatâd teclyn, blychau tywod, a giatiau dyn-yn-y-ddolen, wedi'u dogfennu a'u gorfodi ar draws pob tîm. Mae pob gweithred ganlyniadol wedi'i giatio neu ei dilysu, mae asiantau wedi'u holrhain o ben i ben, ac mae set werthuso awtomataidd gyda sgorio cyfradd-lwyddiant yn rhedeg ar bob newid. Trinnir chwistrelliad anogaeth fel bygythiad sefydlog gydag ymateb diffiniedig.
- **Lefel 4, Rheoli:** Mae'r portffolio asiantau'n cael ei fesur a'i reoli yn erbyn llinellau sylfaen. Caiff cyfradd lwyddiant fesul tasg, cyfradd basio amddiffyn chwistrelliad anogaeth, cost a chyfrif camau fesul rhediad, hwyrni cymeradwyaeth ddynol, a digwyddiadau dolennu neu fethiant eu tracio fel metrigau; gorfodir trothwyon dychwelyd a lladd ar sail y dystiolaeth honno yn hytrach nag ar gwynion. Caiff cyllidebau fesul rhediad ar gamau, amser, a gwariant eu monitro, ac mae atchweliad mewn unrhyw fetrig yn sbarduno gweithred cyn graddfa, nid ar ôl digwyddiad.
- **Lefel 5, Cerddorfa:** Caiff ymreolaeth ei baru â risg tasg gan bolisi a'i haddasu'n barhaus wrth i ganlyniadau ddod i mewn. Mae gwerthuso all-lein a chysylltiedig parhaus yn clymu ymddygiad asiant â chanlyniadau busnes, ac mae'r sefydliad yn rheolaidd yn ymddeol, yn ailgwmpasu, neu'n ail-ganiatáu asiantau wrth i'r darlun risg newid. Mae olrhain, cyllidebau cost, a thraciau archwilio'n unffurf ar draws y portffolio; profir amddiffynfeydd chwistrelliad a dirprwy-dryslyd yn wrthwynebol; mae atebolrwydd am weithredoedd ymreolaethol yn glir ac yn archwiliadwy.

## Syniadau ar gyfer trafodaeth

1. Pa rai o'ch nodweddion LLM presennol sydd wedi dod yn asiantau'n dawel, ac a yw ymreolaeth pob un wedi'i ffinio'n fwriadol?
2. Ar gyfer pob teclyn asiant, beth yw'r ffordd rataf y gallai ymosodwr ei gam-ddefnyddio trwy gynnwys wedi'i chwistrellu, a beth sy'n atal hynny?
3. Ble rydych chi wedi dewis dyluniadau aml-asiant, ac a allwch ddangos bod y gost gydgysylltu wedi talu ar ei ganfed o'i gymharu ag asiant unigol?
4. Pa weithredoedd asiant sy'n wirioneddol anadferadwy, ac a ellid ailddylunio pob un ohonynt i fod yn wrthdroadwy neu wedi'i lwyfannu?
5. Pe bai asiant yn cymryd gweithred niweidiol yfory, a allech ailadeiladu union yr hyn a wnaeth a phwy oedd yn atebol?

## Prif gasgliadau

- Mae asiant yn LLM mewn dolen gyda theclynnau, cof, a nod. Mae'r risg yn byw yn y ddolen a'r teclynnau, nid yn y testun.
- Ffafriwch lif gwaith sefydlog pan fo'r camau'n hysbys; cadwch ymreolaeth ar gyfer nodau gwir agored-eu-pen a'i ffinio'n dynn.
- Defnydd teclynnau yw'r gallu craidd. Rhowch i bob teclyn fraint leiaf, sgema wedi'i ddilysu, a blwch tywod.
- Giatiwch weithredoedd canlyniadol ac anadferadwy y tu ôl i ddyn ag awdurdod go iawn, a dyluniwch ar gyfer gwrthdroi rhad.
- Triniwch asiantau fel rhai gwrthwynebus: amddiffynwch yn erbyn chwistrelliad anogaeth a chamddefnydd dirprwy-dryslyd (pennod 4.2).
- Gwerthuswch ar gyfradd lwyddiant tasgau ar draws llawer o rediadau, ac olrheiniwch bob rhediad ar gyfer dadfygio, rheoli cost, ac archwilio (penodau 6.5 a 6.6).
- Yn aml, yr ateb cywir yw peidio ag adeiladu asiant o gwbl.

## Cyfeiriadau a darllen pellach

- Shunyu Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models*.
- Timo Schick et al., *Toolformer: Language Models Can Teach Themselves to Use Tools*.
- Anthropic, *Building Effective Agents* (canllawiau peirianneg ar lifoedd gwaith yn erbyn asiantau).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications* (gan gynnwys chwistrelliad anogaeth a gormod o asiantaeth).
- Simon Willison, ysgrifennu ar chwistrelliad anogaeth a'r "lethal trifecta" ar gyfer asiantau deallusrwydd artiffisial.
- Norman Hardy, *The Confused Deputy* (y datganiad clasurol o broblem y dirprwy dryslyd).
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Stuart Russell a Peter Norvig, *Artificial Intelligence: A Modern Approach* (asiantau deallus a gweithred resymegol).
