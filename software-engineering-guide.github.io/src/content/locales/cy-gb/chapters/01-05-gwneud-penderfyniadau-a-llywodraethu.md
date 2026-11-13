# 1.5 Gwneud penderfyniadau a llywodraethu

## Trosolwg a chymhelliant

Mae pob system feddalwedd yn swm miloedd o benderfyniadau: pa [gronfa ddata](https://en.wikipedia.org/wiki/Database), pa bensaernïaeth, pa lyfrgell, a ddylid adeiladu neu brynu, pryd i gymryd dyled ymlaen a phryd i'w thalu i lawr. Llywodraethu yw sut rydych chi'n gwneud y penderfyniadau hyn yn dda ac yn gyson, yn cynnwys y bobl gywir heb greu tagfeydd, ac yn cadw'r rhesymeg fel nad yw timau'r dyfodol yn dynghedig i'w hail-ddysgu. Mewn tîm bach, mae penderfyniadau'n digwydd mewn sgwrs ac yn byw mewn cof a rennir. Ar raddfa fawr, mae'r cof hwnnw'n anweddu. Mae pobl yn gadael, mae timau'n ad-drefnu, ac mae'r "pam" y tu ôl i ddewis hollbwysig yn cael ei golli, gan adael olynwyr naill ai i'w gargo-gwlt neu ei rwygo allan yn ddall. Y peirianwaith sy'n gwneud penderfyniadau'n weladwy, yn fwriadol, ac yn barhaol ar draws sefydliad mawr a newidiol yw llywodraethu da.

Yr her ganolog i dimau mawr yw cydbwyso ymreolaeth yn erbyn cyfuniad. Gwthiwch bob penderfyniad i fyny i fwrdd canolog, a chewch gysondeb, ond ar draul tagfeydd anafus a thimau wedi'u dad-rymuso. Gwthiwch bob penderfyniad i lawr, a chewch gyflymder, ond ar draul anhrefn: technolegau anghydnaws, ymdrech ddyblyg, a chamgymeriadau ailadroddus. Nid canoli nac anarchiaeth yw'r ateb aeddfed. Model haenog ydyw. Mae timau'n penderfynu'r rhan fwyaf o bethau'n lleol o fewn "ffordd wedi'i phalmantu" wedi'i marcio'n dda, tra bod proses ysgafn, dryloyw'n llywodraethu'r dewisiadau sy'n wirioneddol draws-dorri ac yn anodd eu gwrthdroi. Y nod yw gwneud penderfyniadau da yn rhagosodiad hawdd, a gwario sylw llywodraethu prin dim ond lle mae'n wirioneddol bwysig.

Mae mentrau a llywodraeth yn cario peryglon uwch. Rhaid iddynt fodloni archwilwyr, rheoleiddwyr, a chyrff goruchwylio sy'n mynnu penderfyniadau wedi'u dogfennu, amddiffynadwy. Maent yn gweithio ar orwelion amser hir, lle gall dewis pensaernïol gwael neu bentwr heb ei reoli o [ddyled dechnegol](https://en.wikipedia.org/wiki/Technical_debt) eu llethu am ddegawd. Ac mae eu rhwymedigaethau caffael a chydymffurfiaeth yn gwneud penderfyniadau adeiladu-yn-erbyn-prynu yn arbennig o ganlyniadol ac anodd eu gwrthdroi. I'r sefydliadau hyn, nid biwrocratiaeth er ei mwyn ei hun yw gwneud penderfyniadau disgybledig, wedi'i gofnodi'n dda. Rheoli risg, cof sefydliadol, a sylfaen atebolrwydd ydyw.

## Egwyddorion allweddol

- Cofnodwch benderfyniadau a'u rhesymeg; mae penderfyniad heb resymeg yn rwymedigaeth.
- Gwthiwch benderfyniadau i'r lefel isaf sydd â'r cyd-destun, o fewn cynwaliau clir.
- Cyfatebwch bwysau'r broses i bwysau a gwrthdroadwyedd y penderfyniad.
- Gwahaniaethwch benderfyniadau gwrthdroadwy ("drws dwy-ffordd") oddi wrth rai anwrthdroadwy ("drws un-ffordd") a'u llywodraethu'n wahanol.
- Ffafriwch ffyrdd wedi'u palmantu a rhagosodiadau dros gymeradwyaethau achos-wrth-achos.
- Trinwch ddyled dechnegol fel portffolio wedi'i reoli, nid methiant moesol i'w guddio.
- Gwnewch lywodraethu'n dryloyw; mae gwneud penderfyniadau cudd yn magu drwgymddiried ac ailwaith.

## Argymhellion

### Mabwysiadwch Gofnodion Penderfyniad Pensaernïol a phroses RFC o'r maint cywir

Mae [Cofnod Penderfyniad Pensaernïol](https://en.wikipedia.org/wiki/Architectural_decision) (ADR) yn ddogfen fer, anghyfnewidiol sy'n dal un penderfyniad arwyddocaol: ei gyd-destun, y dewisiadau a ystyriwyd, y dewis a wnaed, a'r canlyniadau. Storiwch ADRau mewn rheolaeth fersiynau ochr yn ochr â'r cod, fel bod y rhesymeg yn teithio gyda'r system. Ar gyfer penderfyniadau sydd angen mewnbwn cyn eu gwneud, defnyddiwch broses [RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (cais am sylwadau) ysgafn: cylchredwch gynnig, gwahoddwch sylwadau am gyfnod cyfyngedig, yna penderfynwch a chofnodwch. Cadwch y ddau'n ysgafn. Y gwerth sydd yn y meddwl a'r cofnod parhaol, nid mewn templedi cywrain. Gyda'i gilydd, mae ADRau ac RFCau'n troi rhesymeg dawel, angof yn gof sefydliadol y gellir chwilio ynddo.

### Llywodraethwch drwy ffyrdd wedi'u palmantu, nid ceidwaid giât

Yn hytrach nag adolygu pob penderfyniad fesul un, buddsoddwch mewn "ffordd wedi'i phalmantu": set o ragosodiadau bendigedig, wedi'u cefnogi'n dda, ieithoedd cymeradwy, fframweithiau, piblinellau defnyddio, a phatrymau, y gall timau eu mabwysiadu gyda dim fawr o ffrithiant a llawer o gymorth. Nid oes angen fawr o lywodraethu ar dimau sy'n aros ar y ffordd wedi'i phalmantu, oherwydd bod y dewis diogel, cydymffurfiol hefyd yn un hawdd. Gall timau â rheswm gwirioneddol dros ei gadael wneud hynny, ond maent yn cymryd cyfrifoldeb ychwanegol ac adolygiad ysgafn. Mae'r model "llwybr euraidd" hwn yn graddio'n well o lawer na bwrdd canolog yn cymeradwyo popeth, oherwydd ei fod yn symud llywodraethu o geidwadaeth giât achos-wrth-achos i ragosodiadau wedi'u dylunio'n dda.

### Defnyddiwch fyrddau adolygu pensaernïol yn gynnil ac yn dryloyw

Mae gan fwrdd adolygu pensaernïol, neu ei gyfwerth, rôl gyfreithlon ar gyfer y penderfyniadau mwyaf, mwyaf traws-dorri, neu fwyaf anwrthdroadwy, ac ar gyfer gosod y safonau sy'n diffinio'r ffordd wedi'i phalmantu. Cadwch ei gwmpas yn gul, ei feini prawf wedi'u cyhoeddi, a'i broses yn gyflym ac yn gynghorol, nid yn dagfa orfodol ar gyfer gwaith rheolaidd. Swydd y bwrdd yw stiwardio cydlyniant a rhannu gwybodaeth, nid cymeradwyo pob dewis. Pan fydd bwrdd yn dod yn giw y mae'n rhaid i bob prosiect aros ynddi, mae wedi methu. Dirprwywch yn ymosodol, a chadwch adolygiad canolog ar gyfer y ychydig benderfyniadau sy'n wirioneddol ei haeddu.

### Gwnewch adeiladu-yn-erbyn-prynu-yn-erbyn-mabwysiadu'n ddadansoddiad bwriadol

Ar gyfer unrhyw allu arwyddocaol, pwyswch dri llwybr: ei adeiladu'n fewnol, prynu cynnyrch masnachol, neu fabwysiadu ateb [cod agored](https://en.wikipedia.org/wiki/Open-source_software). Adeiladwch pan fo'r gallu'n wahaniaethwr gwirioneddol ac yn greiddiol i'ch cenhadaeth. Prynwch neu mabwysiadwch y galluoedd heb eu gwahaniaethu y mae eraill yn eu gwneud yn well. Cyfrifwch [gyfanswm cost berchnogaeth](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO), nid dim ond y pris o flaen llaw. Mae prynu'n achosi costau trwyddedu, integreiddio, a [chlymu](https://en.wikipedia.org/wiki/Vendor_lock-in). Mae adeiladu'n achosi cynnal a staffio parhaus. Mae mabwysiadu cod agored yn achosi rhwymedigaethau cymorth ac olrhain diogelwch. Cofnodwch y penderfyniad a'i ragdybiaethau fel ADR, fel y gallwch ei ailymweld pan fydd amgylchiadau'n newid.

### Rheolwch ddyled dechnegol fel portffolio

Nid yw dyled dechnegol yn wael yn gynhenid. Weithiau, ei chymryd ymlaen i gyhoeddi'n gynt yw'r dewis cywir. Yr hyn sy'n wael yw dyled heb ei rheoli, anweledig, angof. Cadwch restr eglur o ddyled arwyddocaol. Ar gyfer pob eitem, nodwch y gost y mae'n ei gosod (y "llog" parhaus) a'r gost i'w thrwsio. Yna rheolwch hi fel portffolio ariannol. Talwch i lawr ddyled log-uchel sy'n arafu'r tîm bob dydd. Goddefwch ddyled log-isel mewn corneli sefydlog. Gwnewch benderfyniadau dyled yn ymwybodol yn hytrach na ar hap. Neilltuwch ffracsiwn sefydlog o allu i dalu i lawr ddyled, fel na fydd byth yn cyfansoddi'n argyfwng.

### Gwahaniaethwch benderfyniadau gwrthdroadwy oddi wrth rai anwrthdroadwy

Nid yw pob penderfyniad yn haeddu'r un myfyrdod. Mae penderfyniadau "drws dwy-ffordd" gwrthdroadwy'n hawdd eu dadwneud, felly gwnewch nhw'n gyflym ac yn lleol, gan y tîm, gyda thuedd tuag at weithredu. Mae poeni yn eu cylch yn gwastraffu amser ac yn arafu dysgu. Mae penderfyniadau "drws un-ffordd" anwrthdroadwy neu ddrud-i-wrthdroi, contract [API](https://en.wikipedia.org/wiki/API) cyhoeddus, model data ar raddfa fawr, ymrwymiad gwerthwr aml-flwyddyn, yn haeddu myfyrdod araf, gofalus, uwch a rhesymeg wedi'i chofnodi. Mae dosbarthu penderfyniadau fel hyn yn un o'r arferion llywodraethu â'r trosoledd uchaf sydd gennych. Mae'n anelu craffu prin lle mae'n talu ar ei ganfed, ac yn dad-rwystro popeth arall.

## Cyfaddawdau: manteision ac anfanteision

| Dull llywodraethu | Manteision | Anfanteision |
| --- | --- | --- |
| Bwrdd adolygu canolog ar gyfer popeth | Cysondeb a goruchwyliaeth uchaf | Tagfa ddifrifol; yn dad-rymuso timau; araf |
| Ffordd wedi'i phalmantu ag ymreolaeth leol | Yn graddio, yn gyflym, rhagosodiad diogel, yn grymuso timau | Angen buddsoddiad platfform o flaen llaw; rhai'n crwydro oddi ar y ffordd |
| Ymreolaeth tîm llawn, dim llywodraethu | Cyflym, perchnogaeth uchel | Darniad, dyblygu, camgymeriadau ailadroddus |
| ADRau / RFCau | Cof parhaol, penderfyniadau gwell, tryloywder | Baich ysgrifennu; wedi'u hanwybyddu os na chânt eu cynnal |

| Dewis cyflenwi | Manteision | Anfanteision |
| --- | --- | --- |
| Adeiladu | Rheolaeth lawn, yn ffitio'n union, gall wahaniaethu | Cost cynnal a staffio parhaus |
| Prynu | Cyflym, wedi'i gefnogi, mae rhywun arall yn ei gynnal | Cost drwyddedu, clymu, ffit amherffaith |
| Mabwysiadu (cod agored) | Dim ffi drwydded, archwiliadwy, cymuned | Mae'r baich cymorth a diogelwch yn disgyn arnoch chi |

Y cyfaddawd unifiedol yw rheolaeth yn erbyn cyflymder, a chysondeb canolog yn erbyn ymreolaeth leol. Mae pob dewis llywodraethu'n eistedd ar y sbectrwm hwn. Mae'r ystum a argymhellir, ffyrdd wedi'u palmantu ynghyd â dirprwyo yn seiliedig ar wrthdroadwyedd, yn prynu'n fwriadol y rhan fwyaf o gyflymder ymreolaeth tra'n cadw'r cysondeb sy'n bwysig. Mae'n gwneud hyn drwy wneud y dewis alinedig yn un hawdd, a chadw proses drwm ar gyfer y penderfyniad anwrthdroadwy prin.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Pwy sy'n penderfynu a yw penderfyniad penodol yn ddrws un-ffordd, a sut y byddwch yn dal camddosbarthiadau i'r ddau gyfeiriad?** Dosbarthu penderfyniadau yn ôl gwrthdroadwyedd yw un o'r arferion llywodraethu â'r trosoledd uchaf, ac mae ei werth yn cwympo os ydych chi'n labelu pethau'n anghywir: triniwch ddewis gwrthdroadwy fel un anwrthdroadwy a byddwch yn ei foddi mewn myfyrdod, triniwch un anwrthdroadwy fel un gwrthdroadwy a byddwch yn cyhoeddi model data neu gontract API cyhoeddus na allwch ei ddadwneud yn rhad. Y risg gystadleuol yw y gall y person agosaf at y gwaith fod â thuedd tuag at gyflymder, tra gall bwrdd canolog fod â thuedd tuag at ofal. Dewch ag enghreifftiau pendant i'r drafodaeth: beth fyddai'n ei gostio mewn gwirionedd, mewn amser ac arian, i wrthdroi pob penderfyniad, a phwy sy'n dwyn y gost honno. Mewn lleoliadau menter a llywodraeth, mae ymrwymiadau caffael a data ar raddfa fawr yn troi llawer o ddewisiadau'n ddrysau un-ffordd a oedd yn edrych yn wrthdroadwy o'r dechrau. Cytunwch ar bwy sy'n dosbarthu, ac adeiladwch arfer o farn eilaidd gyflym ar unrhyw beth ger y ffin, fel bod craffu prin yn glanio lle mae gwrthdroi'n wirioneddol ddrud.

2. **Pwy sy'n berchen, yn ariannu, ac yn staffio'r ffordd wedi'i phalmantu, a beth sy'n atal iddi bydru i mewn i geidwad giât?** Dim ond os yw'r rhagosodiadau bendigedig wedi'u cefnogi'n dda mewn gwirionedd a'n haws na'r dewisiadau eraill y mae ffordd wedi'i phalmantu'n gweithio, ac mae hynny'n mynnu buddsoddiad parhaus sy'n hawdd ei dan-ariannu. Mae'r cyfaddawd yn llym: mae ffordd wedi'i phalmantu heb ddigon o adnoddau'n dod yn set o fandadau heb gymorth, sef yn union y ceidwadaeth giât roedd y model wedi'i olygu i'w disodli, ac mae timau wedyn yn llywio o'i chwmpas. Dewch â thystiolaeth o iechyd y ffordd: cyfraddau mabwysiadu, pa mor gyfredol yw'r offer cymeradwy, pa mor gyflym mae'r tîm platfform yn ymateb, a pha mor aml mae timau'n ffeilio i fynd oddi ar y ffordd. I sefydliadau mawr a rheoledig, y ffordd wedi'i phalmantu hefyd yw sut mae'r dewis cydymffurfiol yn dod yn un hawdd, felly mae ei ariannu'n fuddsoddiad cydymffurfiaeth, nid dim ond cyfleustra. Penderfynwch ar berchennog clir a chyllideb sefydlog, a mesurwch a yw timau'n dewis y ffordd oherwydd ei bod yn wirioneddol y llwybr hawsaf.

3. **Ble mae timau'n llywio o gwmpas eich llywodraethu, a beth mae'r TG cysgod hwnnw'n ei ddweud wrthych?** Mae timau'n osgoi'r llwybr a gymeradwywyd pan fo'n fwy poenus na'r ffordd-o-gwmpas, felly mae TG cysgod eang yn llai o broblem disgyblaeth a mwy o ddyfarniad dylunio ar eich llywodraethu. Mae'r ystyriaethau cystadleuol yn real: mae rhywfaint o osgoi'n fyrbwyll, ac mae llawer ohono'n osgoi rhesymegol o fwrdd adolygu sydd wedi dod yn giw aml-wythnos. Dewch â'r dystiolaeth: pa gymeradwyaethau sy'n cael eu hepgor, pa offer answyddogol sydd wedi lledaenu'n dawel, a pha mor hir mae'r llwybr swyddogol yn ei gymryd mewn gwirionedd. Mewn cyd-destunau menter a llywodraeth, mae'r peryglon yn uwch, oherwydd gall offer heb eu cymeradwyo dorri rhwymedigaethau archwilio, diogelwch, a chaffael sy'n cario pwysau cyfreithiol. Os yw'r patrwm yn dangos pobl yn llywio o gwmpas tagfa, y datrysiad yw cyflymu a lledu'r ffordd wedi'i phalmantu a chrebachu cwmpas y bwrdd i'r ychydig benderfyniadau traws-dorri, anwrthdroadwy, nid ychwanegu mwy o gymeradwyaethau.

4. **Faint o'n gallu cyflenwi sy'n mynd mewn gwirionedd i dalu i lawr ddyled dechnegol, ac a allwn ni enwi'r eitemau log-uchaf y dylai eu targedu'n gyntaf?** Mae dyled dechnegol yn ymddwyn fel llog cyfansawdd, treth dawel ar bob newid yn y dyfodol, a gall sefydliad mawr ei chario am flynyddoedd cyn i unrhyw un sylwi bod y system wedi dod yn araf ac yn frau i'w haddasu. Mae'r pwysau cystadleuol yn ddi-flewyn-ar-dafod: mae pob awr a dreulir ar ddyled yn awr na chaiff ei threulio ar nodweddion y gall arweinyddiaeth eu gweld, felly talu i lawr yw'r peth cyntaf i'w dorri pan fydd terfyn amser yn tynhau. Dewch â thystiolaeth real i'r drafodaeth, rhestr ysgrifenedig o ddyled arwyddocaol, amcangyfrif gonest o'r gost barhaus y mae pob eitem yn ei gosod a'r gost i'w thrwsio, a'r ffracsiwn gwirioneddol o allu diweddar a aeth i dalu i lawr o'i gymharu â gwaith newydd. I fentrau a chyrff llywodraethol ar orwelion amser degawd-hir, mae dyled heb ei rheoli yn y pen draw yn gorfodi ailysgrifennu drud neu ganfyddiad archwilio, felly trinwch ddyraniad talu-i-lawr sefydlog fel rheoli risg a phenderfynwch pwy sy'n ei warchod pan fydd amserlenni'n llithro.

5. **Pan fydd angen i ni wybod y rhesymeg y tu ôl i benderfyniad a wnaed ddwy flynedd yn ôl, a allwn ni ei ganfod mewn gwirionedd, ac a oes unrhyw un yn cadw'r cofnod hwnnw'n fyw?** Gwerth cyfan Cofnod Penderfyniad Pensaernïol yw bod y rhesymeg yn goroesi'r bobl a'i gwnaeth, ac mae'r gwerth hwnnw'n cwympo os yw ADRau'n cael eu hysgrifennu unwaith, byth eu chwilio, ac yn dawel yn drifftio allan o ddyddiad. Mae'r tensiwn rhwng y ddisgyblaeth ysgrifennu sydd ei angen i ddal cyd-destun, dewisiadau, a chanlyniadau ar adeg y penderfyniad, a'r pwysau dyddiol i gyhoeddi a symud ymlaen. Dewch â phrofion pendant i'r drafodaeth: dewiswch dri phenderfyniad diweddar pwysig a gweld a all unrhyw un ddod o hyd i'r rhesymeg wedi'i chofnodi mewn munudau, a gwiriwch a yw ADRau a ddisodlwyd wedi'u marcio felly yn hytrach na'n dawel wrthddweud arferion cyfredol. Mewn lleoliadau menter a llywodraeth, dyna'n union y cofnod y gellir chwilio ynddo yw'r dystiolaeth amddiffynadwy y mae archwilwyr a chyrff goruchwylio'n ei mynnu, felly penderfynwch ble mae ADRau'n byw, pwy sy'n eu hadolygu, a beth sy'n gwneud penderfyniad yn ddigon arwyddocaol i'w gofnodi.

6. **Pryd wnaethom ni ailagor diwethaf benderfyniad adeiladu-yn-erbyn-prynu mawr yn erbyn ei ragdybiaethau gwreiddiol, a fyddem ni hyd yn oed yn sylwi pan fydd y rhagdybiaethau hynny'n dod i ben?** Mae dewisiadau cyflenwi ymhlith y penderfyniadau mwyaf drud ac anodd eu gwrthdroi y byddwch yn eu gwneud, ac mae'r rhagdybiaethau y tu ôl iddynt (prisio gwerthwr, eich staffio eich hun, aeddfedrwydd dewis cod agored) yn dawel yn heneiddio tra bod y penderfyniad yn aros yn rhewedig yn ei le. Mae'r ystyriaethau cystadleuol yn pwyso'r gost suddedig a'r aflonyddwch o newid yn erbyn cost gynyddol clymu, ffit amherffaith, neu faich cynnal nad ydych chi ei eisiau mwyach. Dewch â'r ADR gwreiddiol a'i ragdybiaethau datganedig, amcangyfrif cyfanswm cost berchnogaeth cyfredol ar gyfer pob llwybr gan gynnwys trwyddedu, integreiddio, staffio, a chost ymadael, ac unrhyw signal, newid pris neu ddadraddio cymorth, bod rhagosodiad wedi symud. I brynwyr llywodraeth a rheoledig, mae rheolau caffael a chontractau aml-flwyddyn yn gwneud y drysau un-ffordd hyn yn arbennig o rwymol, felly cytunwch ymlaen llaw ar y sbardunau a'r cyflymder a fydd yn gorfodi ail-benderfyniad bwriadol yn hytrach nag adnewyddiad dall.

## Lens sector

**Cwmni newydd.** Llywodraethwch bron dim byd a phwysleisiwch gyflymder yn galed: ar gyfer dewisiadau drws dwy-ffordd gwrthdroadwy, penderfynwch wrth y ddesg a symud ymlaen. Cadwch eich un arfer llywodraethu ar gyfer y llond dwrn o ddrysau un-ffordd, model data craidd neu werthwr sylfaenol, a dalwch bob un mewn un paragraff fel nad yw cyd-weithiwr yn y dyfodol yn ei ailddadlau o'r dechrau. Hepgorwch fyrddau adolygu a ffyrdd wedi'u palmantu'n gyfan gwbl, oherwydd ar eich maint chi maent yn faich na allwch ei fforddio a'r tîm cyfan eisoes yn rhannu'r cyd-destun.

**Busnes bach.** Heb bensaer ar staff, gwnewch adeiladu-yn-erbyn-prynu'n gwestiwn llywodraethu canolog a'i ateb ar sail cyfanswm cost berchnogaeth yn hytrach na hoffter. Rhagosodwch brynu neu fabwysiadu offer wedi'u cefnogi'n dda ar gyfer unrhyw beth nad yw'n eich gwahaniaethwr craidd, oherwydd cynnal parhaus yw'r gost sydd leiaf y gallwch fforddio ei chario. Cadwch un log penderfyniad ysgafn fel bod y rhesymeg y tu ôl i'ch ychydig ddewisiadau canlyniadol yn goroesi person allweddol yn gadael.

**Menter.** Eich problem yw cydbwyso ymreolaeth yn erbyn cyfuniad ar draws llawer o dimau, felly buddsoddwch mewn ffordd wedi'i phalmantu wedi'i hariannu a chadwch fwrdd adolygu pensaernïol cul, cyflym ar gyfer y penderfyniadau sy'n wirioneddol draws-dorri ac anwrthdroadwy. Safonwch ADRau fel bod rhesymeg yn dod yn gof sefydliadol y gellir chwilio ynddo, a rheolwch ddyled dechnegol a dewisiadau cyflenwi fel portffolios â chyllidebau sefydlog. Mesurwch a yw timau'n dewis y ffordd oherwydd ei bod yn haws, a chrebachwch unrhyw fwrdd sydd wedi pydru'n giw.

**Llywodraeth.** Nid yw penderfyniadau wedi'u dogfennu, amddiffynadwy'n ddewisol yma: mae archwilwyr a chyrff goruchwylio'n disgwyl gweld y rhesymeg, y dewisiadau a bwyswyd, a'r rhagdybiaethau y tu ôl i bob dewis canlyniadol. Rhedwch adeiladu-yn-erbyn-prynu fel dadansoddiad cyfanswm cost berchnogaeth wedi'i gofnodi, anrhydeddwch reolau caffael sy'n cyfyngu clymu unig-ffynhonnell, a chadwch ADRau fel y trywydd tystiolaeth parod-ar-gyfer-archwiliad. Trinwch orwelion amser hir o ddifrif, oherwydd gall model data neu ymrwymiad gwerthwr a wneir heddiw rwymo'r sefydliad am ddegawd, felly dosbarthwch ef fel drws un-ffordd a myfyriwch yn unol â hynny.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd pedwar person yn gwneud y rhan fwyaf o benderfyniadau mewn munudau ar draws desg a rennir, ac ar gyfer dewisiadau drws dwy-ffordd gwrthdroadwy mae'r cyflymder hwnnw'n fantais real, felly maent yn gwrthsefyll unrhyw faich llywodraethu. Ond pan fyddant yn dewis cronfa ddata a model data a fydd yn boenus i'w newid yn ddiweddarach (drws un-ffordd), maent yn oedi i ysgrifennu nodyn un-paragraff: y dewisiadau, y dewis, a'r rhagdybiaethau y tu ôl iddo. Flwyddyn yn ddiweddarach, wrth daro terfynau graddio, mae'r un nodyn hwnnw'n eu harbed rhag ailddadlau'r cwestiwn o'r dechrau. Maent yn llywodraethu bron dim byd, ac yn cadw eu un arfer ysgafn ar gyfer y ychydig benderfyniadau sy'n wirioneddol ddrud i'w gwrthdroi.

**Menter.** Roedd timau platfform menter fawr wedi'u parlysu gan fwrdd adolygu pensaernïol y bu'n rhaid iddo gymeradwyo pob dewis technoleg, gan greu ciwiau aml-wythnos. Ad-drefnodd y fenter lywodraethu o gwmpas ffordd wedi'i phalmantu: catalog wedi'i guradu o ieithoedd, storfeydd data, a phiblinellau cymeradwy, wedi'u cefnogi'n llawn, y gallai timau eu mabwysiadu ar unwaith. Cofnododd ADRau unrhyw benderfyniad i wyro, a thriniodd adolygiad cyflym, cynghorol ddim ond dewisiadau oddi ar y ffordd. Crebachodd cwmpas y bwrdd i osod safonau a'r llond dwrn o benderfyniadau sy'n wirioneddol draws-dorri. Cyflymodd cyflenwi'n sylweddol. Gwellodd cysondeb mewn gwirionedd, oherwydd bod y llwybr hawdd bellach yn un cydymffurfiol. Ac roedd archif yr ADR yn rhoi cofnod y gellid chwilio ynddo i'r sefydliad o pam yr adeiladwyd pethau fel yr oeddent.

**Llywodraeth.** Wynebodd adran lywodraethol benderfyniad mawr adeiladu-yn-erbyn-prynu ar gyfer platfform rheoli achosion o dan reolau caffael ac archwilio llym. Yn hytrach na phenderfynu drwy hoffter, rhedodd ddadansoddiad cyfanswm cost berchnogaeth wedi'i ddogfennu ar draws tri dewis: adeiladu wedi'i deilwra, prynu cynnyrch masnachol, a mabwysiadu sylfaen cod agored. Pwysodd drwyddedu, integreiddio, cynnal hirdymor, staffio, a chlymu, a chofnododd y penderfyniad a'i ragdybiaethau fel ADR. Flynyddoedd yn ddiweddarach, pan newidiodd telerau gwerthwr, ailymwelodd yr adran â'r ADR hwnnw, canfod nad oedd ei ragdybiaethau gwreiddiol yn dal, ac ailbenderfynu gyda gwybodaeth lawn o'r rhesymeg flaenorol, gan osgoi mudo dall a drud. Roedd y rhesymeg wedi'i chofnodi hefyd yn union y dystiolaeth amddiffynadwy yr oedd archwilwyr yn ei mynnu.

## Achos busnes: cymhellion, ROI, a TCO

Penderfyniadau yw'r gost â'r trosoledd uchaf a'r gwelededd isaf mewn meddalwedd. Gall un dewis pensaernïol neu gyflenwi gwael, anwrthdroadwy osod blynyddoedd o lusgo neu adferiad naw-ffigwr. Mae ei lywodraethu'n dda, ychydig oriau o fyfyrdod a chofnod ysgrifenedig, yn costio bron dim byd o'i gymharu. Daw'r elw ar ADRau a dirprwyo yn seiliedig ar wrthdroadwyedd o ddwy ffynhonnell: osgoi camgymeriadau drud ar y penderfyniadau drws-un-ffordd, ac osgoi myfyrdod gwastraffus ac ailwaith ar bopeth arall. Mae rhesymeg wedi'i chofnodi hefyd yn torri'r gost gylchol o ailddadlau cwestiynau setledig ac o dimau'n peirianneg-wrthdroi bwriad y tu ôl i systemau a etifeddwyd.

Mae dyled dechnegol yn gwneud y ddadl TCO'n gyngrët. Mae dyled heb ei rheoli'n ymddwyn yn union fel llog cyfansawdd: treth gynyddol ar bob newid yn y dyfodol, nes bod y system yn dod yn effeithiol amhosibl ei chynnal ac yn mynnu ailysgrifennu drud. Mae rheoli dyled fel portffolio, gyda dyraniad gallu sefydlog i dalu i lawr yr eitemau log-uchel, yn llawer rhatach na'r argyfwng terfynol. Mae llywodraethu da'n rhad i'w fabwysiadu, gan mwyaf disgyblaeth ysgrifennu penderfyniadau i lawr a'r buddsoddiad o flaen llaw mewn ffordd wedi'i phalmantu. Mae ei hepgor yn ddrud: rydych yn talu mewn ailysgrifennu y gellid ei osgoi, synau clymu, methiannau archwilio, a chof sefydliadol coll. I ddarbwyllo arweinyddiaeth, fframiwch lywodraethu yn eu hiaith nhw: lleihau risg, ailwaith a osgowyd, cyflenwi cyflymach drwy'r ffordd wedi'i phalmantu, ac amddiffynadwyedd parod-ar-gyfer-archwiliad. Dangoswch nad mwy o broses yw'r nod ond proses wedi'i hanelu'n well, craffu trwm dim ond lle mae gwrthdroi'n ddrud, a chyflymder di-ffrithiant ym mhobman arall.

## Gwrth-batrymau a maglau

- Penderfyniadau heb eu dogfennu: rhesymeg wedi'i cholli'r eiliad y mae'r bobl a'i gwnaeth yn gadael.
- Tagfa bwrdd cymeradwyo: corff canolog y mae'n rhaid i bob prosiect giwio y tu ôl iddo.
- Proses un-maint: gorfodi penderfyniadau gwrthdroadwy dibwys drwy adolygiad trwm.
- Parlys dadansoddi: poeni am benderfyniadau drws-dwy-ffordd sy'n hawdd eu gwrthdroi.
- [TG cysgod](https://en.wikipedia.org/wiki/Shadow_IT): timau'n osgoi llywodraethu'n gyfan gwbl oherwydd bod y llwybr a gymeradwywyd yn rhy boenus.
- Dyled dechnegol anweledig: dyled na chafodd erioed ei rhestru, byth wedi'i thalu i lawr, yn dawel yn cyfansoddi.
- Adweithiau adeiladu-popeth neu brynu-popeth: cyflenwi yn ôl arferiad yn hytrach na dadansoddiad TCO.
- Theatr llywodraethu: dogfennau a byrddau sy'n bodoli er golwg ond nad ydynt yn siapio penderfyniadau.

## Model aeddfedrwydd

- Lefel 1 (Cychwyn): Mae penderfyniadau'n ad hoc ac heb eu cofnodi; mae llywodraethu naill ai'n absennol neu'n dagfa flanced; mae dyled dechnegol yn anweledig ac mae'r rhesymeg y tu ôl i ddewisiadau'n anweddu pan fydd pobl yn gadael.
- Lefel 2 (Datblygu): Mae rhai penderfyniadau'n cael eu dogfennu ac mae rhywfaint o adolygiad yn bodoli, ond mae'r arfer yn anghyson ar draws timau ac mae'r broses yn aml wedi'i chamgyfateb i bwysau a gwrthdroadwyedd y penderfyniad.
- Lefel 3 (Safoni): Mae ADRau, ffordd wedi'i phalmantu, dirprwyo yn seiliedig ar wrthdroadwyedd, a rhestr ddyled wedi'u dogfennu a'u gorfodi ar draws y sefydliad, fel bod y dewis cydymffurfiol yn rhagosodiad hawdd a'r rhesymeg y gellir chwilio ynddi.
- Lefel 4 (Rheoli): Caiff llywodraethu ei fesur yn erbyn llinellau sylfaen: olrhëir mabwysiadu ffordd-wedi'i-phalmantu, cwmpas ADR, amser cylchred penderfyniad, dyled fel cyfran o allu, a chyfraddau eithriad oddi-ar-y-ffordd, a chaiff penderfyniadau i dalu i lawr ddyled neu ailymweld â chyflenwi eu sbarduno gan y dystiolaeth honno yn hytrach nag argyfwng.
- Lefel 5 (Cerddorfa): Caiff llywodraethu ei diwnio'n barhaus a'i integreiddio â chynllunio cyflenwi a risg; anelir craffu'n union at benderfyniadau anwrthdroadwy; caiff dewisiadau dyled a chyflenwi eu hail-gydbwyso'n weithredol fel portffolios a'u hail-benderfynu ar dystiolaeth wrth i amgylchiadau symud.

## Syniadau ar gyfer trafodaeth

- Ar gyfer ein penderfyniadau diweddar pwysicaf, a allwn ni ddod o hyd i'r rhesymeg wedi'i chofnodi y tu ôl iddynt?
- Ble mae ein llywodraethu'n dagfa, a ble mae'n absennol pan fo ei angen?
- Pa rai o'n penderfyniadau cyfredol sy'n ddrysau un-ffordd, ac a ydym yn eu trin felly?
- Faint o'n gallu sy'n mynd i dalu i lawr ddyled dechnegol, ac a yw'n ddigon?
- A yw ein timau'n dilyn y ffordd wedi'i phalmantu oherwydd ei bod yn wirioneddol y llwybr hawsaf, neu'n llywio o'i chwmpas?
- Pryd wnaethom ni ailymweld diwethaf â phenderfyniad adeiladu-yn-erbyn-prynu mawr yn erbyn ei ragdybiaethau gwreiddiol?

## Casgliadau allweddol

- Cofnodwch benderfyniadau arwyddocaol a'u rhesymeg ag ADRau; gwnewch resymeg yn barhaol.
- Llywodraethwch drwy ffyrdd wedi'u palmantu a rhagosodiadau, nid ceidwadaeth giât achos-wrth-achos.
- Cyfatebwch bwysau proses i bwysau a gwrthdroadwyedd penderfyniad; dirprwywch ddrysau dwy-ffordd, myfyriwch ar ddrysau un-ffordd.
- Dadansoddwch adeiladu-yn-erbyn-prynu-yn-erbyn-mabwysiadu ar sail cyfanswm cost berchnogaeth, a chofnodwch y rhagdybiaethau.
- Rheolwch ddyled dechnegol fel portffolio eglur gyda dyraniad talu-i-lawr sefydlog.
- Cadwch lywodraethu'n dryloyw ac yn ysgafn; anelwch graffu prin lle mae gwrthdroi'n ddrud.

## Cyfeiriadau a darllen pellach

- Michael Nygard, "Documenting Architecture Decisions" (the original ADR pattern)
- Gregor Hohpe, "The Software Architect Elevator" and "37 Things One Architect Knows"
- Amazon shareholder letters on Type 1 vs Type 2 (one-way vs two-way door) decisions
- Ward Cunningham, the original "technical debt" metaphor
- Martin Fowler, writings on technical debt and evolutionary architecture
- Neal Ford, Rebecca Parsons, Patrick Kua, "Building Evolutionary Architectures"
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate" (loosely coupled architecture and autonomy)
- ISO/IEC/IEEE 42010 on architecture description
