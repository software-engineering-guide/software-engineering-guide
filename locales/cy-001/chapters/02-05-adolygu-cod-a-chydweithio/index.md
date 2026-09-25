# 2.5 Adolygiad cod a chydweithio

## Trosolwg a chymhelliant

Mae [adolygiad cod](https://en.wikipedia.org/wiki/Code_review) yn arfer o gael rhywun heblaw'r awdur i archwilio newid cyn iddo uno. Mae'n un o'r gweithgareddau ansawdd a rhannu gwybodaeth â'r trosoledd uchaf sydd gan sefydliad meddalwedd, ac i dimau mawr mae hefyd yn brif fecanwaith cydgysylltu a diwylliant. Mae adolygu'n dal namau, yn lledaenu gwybodaeth o'r cod-sylfaen, yn gorfodi safonau, ac yn mentora peirianwyr, ond dim ond pan wnewch ef yn dda. Wedi'i wneud yn wael, mae'n dod yn dagfa, yn ffynhonnell ffrithiant, neu'n stamp rwber sy'n rhoi sicrwydd ffug.

I dimau mawr, adolygu yw lle mae gwaith unigol yn cwrdd â pherchnogaeth gyfunol. Yn aml dyma'r prif bwynt cyswllt rhwng peirianwyr sydd fel arall yn gweithio ar eu pen eu hunain, felly mae ei normau'n siapio sut mae'r sefydliad cyfan yn cydweithio. Mae adolygu'n lledaenu gwybodaeth fel na ddeellir unrhyw ran o'r system gan un person yn unig, sy'n lleihau risg y ["ffactor bws"](https://en.wikipedia.org/wiki/Bus_factor) (y perygl pan fo gwybodaeth yn gorwedd gyda rhy ychydig o bobl) sy'n poeni systemau mawr, hirhoedlog. Mae hefyd yn creu llwybr archwilio o bwy newidiodd beth a phwy a'i cymeradwyodd.

Mewn cyd-destunau menter a llywodraeth, mae gan adolygu ddimensiwn cydymffurfiaeth yn aml. Mae [gwahanu dyletswyddau](https://en.wikipedia.org/wiki/Separation_of_duties) (nid oes un person yn rheoli newid sensitif cyfan), cymeradwyaethau gorfodol, ac olrheiniadwyedd yn rheolaethau a fynnir yn aml. Efallai y bydd angen adolygiad ar newid sy'n cyffwrdd systemau sensitif gan rolau penodol, ac mae'r cofnod adolygu'n dod yn dystiolaeth archwilio. Eich her yw bodloni'r rheolaethau hyn tra'n cadw adolygu'n gyflym ac yn adeiladol, yn lle ei droi'n seremoni.

## Egwyddorion allweddol

- Adolygwch i wella'r newid ac i rannu gwybodaeth, nid i ddangos eich hun.
- Mae newidiadau bach yn cael adolygiadau gwell, felly cadwch geisiadau tynnu (PRs) yn ffocysedig ac o faint rhesymol.
- Mae hwyrni adolygu'n gost i'r tîm cyfan. Mae trosiant cyflym yn cadw pawb i symud.
- Awtomeiddiwch y pethau mecanyddol (arddull, profion, sganiau diogelwch) fel bod pobl yn adolygu dyluniad a chywirdeb.
- Gwahanwch faterion sy'n rhwystro oddi wrth awgrymiadau a dewisiadau, a byddwch yn eglur pa un yw pa un.
- Beirniadwch y cod, nid y person. Mae normau adborth yn penderfynu a yw adolygu'n adeiladu ymddiriedaeth neu'n ei erydu.
- Yr awdur sy'n gyfrifol am wneud newid yn hawdd i'w adolygu.

## Argymhellion

### Gwnewch geisiadau tynnu'n fach a wedi'u disgrifio'n dda

Cadwch bob newid yn ffocysedig ar un pryder rhesymegol ac yn ddigon bach i'w adolygu'n ofalus. Mae PRs mawr yn cael adolygiadau bas. Rhowch ddisgrifiad eglur o beth a newidiwyd, pam, a sut y'i gwiriwyd, fel bod gan yr adolygydd gyd-destun. Rhannwch ailffactora mecanyddol a newidiadau ymddygiad yn PRs ar wahân, fel bod pob un yn hawdd ei ddeall. Y disgrifiad da yw cyfraniad pwysicaf yr awdur i ansawdd adolygu.

### Sefydlwch safonau a rhestrau gwirio adolygu

Nodwch yn glir beth y dylai adolygwyr chwilio amdano: cywirdeb, cydweddiad dyluniad, digonolrwydd profion, goblygiadau diogelwch, darllenadwyedd, a chydymffurfiad â safonau. Mae rhestr wirio ysgafn yn cadw adolygiadau'n gyson ac yn atal dimensiynau pwysig rhag llithro drwodd, heb droi adolygu'n ticio blychau. Diffiniwch beth sydd angen ei adolygu, pwy all gymeradwyo, ac unrhyw gymeradwyaethau rôl-seiliedig sydd eu hangen ar gyfer meysydd sensitif.

### Gosodwch a monitrwch normau hwyrni adolygu

Cytunwch ar drosiant targed, er enghraifft ymateb o fewn diwrnod gwaith, a gwnewch adolygu'n rhan ddosbarth cyntaf o'r dydd yn hytrach na rhywbeth a wasgir i mewn ar y diwedd. Mae ciwiau adolygu hir yn stopio cyflenwi ac yn temtio peirianwyr i newidiadau rhy fawr, wedi'u bagio. Monitrwch amser-i-adolygiad-cyntaf ac amser-i-uno, a thrinwch hwyrni parhaus fel problem broses i'w thrwsio, nid diffyg personol.

### Awtomeiddiwch bopeth mecanyddol

Rhedwch fformatio, [leintio](https://en.wikipedia.org/wiki/Lint_(software)), profion, a sganio diogelwch a dibyniaeth mewn [integreiddio parhaus](https://en.wikipedia.org/wiki/Continuous_integration) (CI), fel nad yw adolygwyr byth yn treulio sylw arnynt. Cadwch adolygiad dynol ar gyfer y pethau na all peiriannau eu barnu: a yw'r dyluniad yn gywir, a yw'r dull yn cyd-fynd â'r system, a yw'r profion yn ystyrlon, ac a fydd y cod yn dal i wneud synnwyr yn ddiweddarach.

### Defnyddiwch raglennu mewn parau a rhaglennu torf lle maent yn addas

Defnyddiwch [raglennu mewn parau](https://en.wikipedia.org/wiki/Pair_programming), lle mae dau beiriannydd yn ysgrifennu cod gyda'i gilydd ar un orsaf waith, ar gyfer gwaith cymhleth neu risg uchel, sefydlu, a throsglwyddo gwybodaeth. Mae'n adolygu parhaus, ac mae'n aml yn dileu'r angen am gam adolygu ar wahân. Defnyddiwch [raglennu torf](https://en.wikipedia.org/wiki/Mob_programming) (*mob programming*), lle mae'r tîm cyfan yn gweithio ar un dasg ar y tro, ar gyfer penderfyniadau dyluniad critigol neu i ledaenu gwybodaeth am faes anodd ar draws y tîm. Meddyliwch am y rhain fel cyflenwadau i adolygu anghydamserol, wedi'u dewis yn ôl cyd-destun, nid disodliadau i'w gorfodi ym mhobman.

### Mabwysiadwch adolygu awtomataidd a gyda chymorth deallusrwydd artiffisial yn ofalus

Defnyddiwch declynnau adolygu awtomataidd a chynorthwywyr deallusrwydd artiffisial i ddal materion cyffredin, awgrymu gwelliannau, ac ysgafnhau baich yr adolygydd, ond trinwch eu hallbwn fel mewnbwn, nid awdurdod. Mae adolygu deallusrwydd artiffisial yn dda am faterion wynebol a chysondeb, ac yn wael am farn dyluniad dwfn a chyd-destun system. Cadwch berson yn atebol am bob cymeradwyaeth, yn enwedig ar gyfer newidiadau sensitif o ran diogelwch a pherthnasol i gydymffurfiaeth.

### Gosodwch normau adborth adeiladol

Gosodwch normau sy'n cadw adborth yn benodol, yn garedig, ac wedi'i ffocysu ar y cod. Anogwch adolygwyr i ofyn cwestiynau yn hytrach na chyhoeddi gorchmynion, i esbonio'r rhesymeg y tu ôl i gais, ac i ganmol gwaith da. Marciwch bryderon sy'n rhwystro ac awgrymiadau dewisol yn eglur (er enghraifft, drwy ragflaenu nodiadau nad ydynt yn rhwystro). Mae'r normau hyn yn penderfynu a yw adolygu'n cryfhau'r tîm neu'n magu dicter.

## Cyfaddawdau: manteision ac anfanteision

| Dull | Manteision | Anfanteision |
|---|---|---|
| Adolygiad PR anghydamserol | Hyblyg; wedi'i ddogfennu; yn graddio ar draws parthau amser | Hwyrni; yn colli naws; gall deimlo'n wrthwynebus |
| Rhaglennu mewn parau | Adolygu parhaus; trosglwyddo gwybodaeth cyflym; ansawdd uchel | Dau berson ar un dasg; blinedig; anos ei amserlennu |
| Rhaglennu torf | Aliniad tîm cyfan; yn lledaenu gwybodaeth ddwfn | Drud yn gyfanredol; nid ar gyfer gwaith arferol |
| Aml-adolygydd gorfodol | Sicrwydd cryf; cyfeillgar i gydymffurfiaeth | Arafach; yn gwasgaru cyfrifoldeb; pwysau ciw |
| Adolygu â chymorth deallusrwydd artiffisial | Cyflym, diflino ar faterion cyffredin; yn lleihau baich | Yn colli cyd-destun system; hyder ffug os ymddiriedir gormod ynddo |

Y tyndra craidd yw trylwyredd yn erbyn cyflymder. Mae adolygiad dyfnach yn dal mwy, ond mae'n arafu cyflenwi a gall rwystredigo awduron. Mae adolygiad cyflymach yn cadw llif, ond mae'n mentro bod yn arwynebol. Y ffordd drwodd yw cydweddu dyfnder adolygu â risg newid, fel bod newidiadau dibwys yn cael adolygiad ysgafn a newidiadau peryglus yn cael un dwfn, ac awtomeiddio'r gwaith mecanyddol i ffwrdd fel bod ymdrech ddynol yn canolbwyntio lle mae'n bwysig.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Beth sy'n cyfrif fel rhy fawr ar gyfer un cais tynnu, ac a ydych yn gwahanu ailffactora mecanyddol oddi wrth newidiadau ymddygiad?** Mae'r bennod hon yn nodi'n glir bod PRs mawr yn cael adolygiadau bas a bod yr awdur yn berchen ar addasrwydd i'w adolygu, ac mae'n gofyn i chi wahanu ailffactora oddi wrth newidiadau ymddygiad fel bod pob un yn hawdd ei ddeall. Ar dîm mawr mae PR anferth yn gwarantu stamp rwber, sy'n rhoi sicrwydd ffug tra'n gadael namau go iawn drwodd. Dewch â'r dystiolaeth: eich dosbarthiad o feintiau PR a sut mae dyfnder adolygu'n gostwng wrth i wahaniaethau dyfu. Cytunwch ar norm maint ymarferol ac arferiad o lanio ailffactora pur ar wahân i newidiadau rhesymeg, fel y gall adolygydd ddal pob newid yn ei ben mewn gwirionedd. Mae'r un ddisgyblaeth honno'n codi ansawdd pob adolygiad sy'n dilyn.

2. **Sut ydych chi'n gwahaniaethu gwrthwynebiad sy'n rhwystro oddi wrth awgrym dewisol, ac a yw'r confensiwn hwnnw mewn gwirionedd yn cael ei ddefnyddio?** Mae'r bennod yn gofyn i chi wahanu materion sy'n rhwystro oddi wrth ddewisiadau a bod yn eglur pa un yw pa un, ac mae'n fflagio rhwystro ar sail dewis fel gwrth-batrwm erydol. Heb gonfensiwn a rennir, mae barn arddull adolygydd yn darllen fel newid gofynnol, sy'n magu dicter ac yn arafu cyflenwi ar draws y tîm cyfan. Dewch ag enghreifftiau o adolygiadau diweddar lle gwnaeth dewis atal uniad fel y signal diriaethol. Mabwysiadwch farciwr ysgafn, er enghraifft rhagddodiad sy'n tagio nodiadau nad ydynt yn rhwystro, fel bod awduron yn gwybod ar unwaith beth sy'n rhaid ei newid o'i gymharu â beth sy'n awgrym. Mae hynny'n cadw adolygu wedi'i ffocysu ar gywirdeb a dyluniad yn hytrach na chwaeth.

3. **Pwy sy'n rhaid iddo gymeradwyo newidiadau i god sensitif o ran diogelwch neu berthnasol i gydymffurfiaeth, a sut mae'r llwybro hwnnw'n cael ei orfodi?** Mae'r bennod hon yn disgrifio cymeradwyaethau rôl-seiliedig, rheolau perchnogaeth cod, a gwahanu dyletswyddau lle nad oes un person yn rheoli newid sensitif cyfan, gyda'r gymeradwyaeth wedi'i chofnodi fel tystiolaeth archwilio. Mewn lleoliadau menter a llywodraeth mae'r rhain yn rheolaethau a fynnir, a'r risg yw eu bod naill ai'n cael eu hepgor neu'n troi'n dagfa sy'n rhewi cyflenwi. Dewch â'r signal: pa fodiwlau sy'n sensitif, ac a yw rheolau perchnogaeth ar hyn o bryd yn llwybro'r newidiadau hynny'n awtomatig at yr cymeradwywyr cywir. Amgodiwch y llwybro mewn ffurfweddiad perchnogaeth cod a'i baru â gwiriadau awtomataidd a newidiadau bach, fel bod y rheolaeth yn cael ei bodloni heb giw gwarchod dynol. Penderfynwch hyn yn fwriadol yn hytrach na darganfod y bwlch yn ystod archwiliad.

4. **Pa darged hwyrni adolygu rydych chi mewn gwirionedd wedi cytuno arno, ac a ydych chi'n ei fesur a'i orfodi, neu ai dyhead yn unig ydyw?** Mae'r bennod yn trin hwyrni adolygu fel cost i'r tîm cyfan ac yn gofyn i chi fonitro amser-i-adolygiad-cyntaf ac amser-i-uno, gan drin oedi parhaus fel problem broses yn hytrach na diffyg personol. Ar dîm mawr mae ciw adolygu heb berchennog yn trethu pawb yn dawel: mae awduron yn bagio newidiadau mwy i osgoi'r aros, mae'r newidiadau hynny wedyn yn cael adolygiadau bas, ac mae amser arwain cyflenwi'n drifftio i fyny heb un euog. Yr ystyriaeth gystadleuol yw y gall targed hwyrni caled wthio adolygwyr i sgimio, felly rhaid cydbwyso cyflymder a dyfnder yn hytrach na'u masnachu'n ddall. Dewch â'r dystiolaeth: eich dosbarthiad cyfredol o amser-i-adolygiad-cyntaf, sut mae'n amrywio yn ôl tîm ac yn ôl maint newid, a ble mae adolygiadau'n eistedd hiraf. Mewn lleoliadau menter a llywodraeth, clymwch y targed wrth y metrigau llif y mae arweinyddiaeth eisoes yn eu holrhain, gan fod rheolaeth aml-adolygydd orfodol heb norm hwyrni'n dod yn dagfa sy'n rhewi cyflenwi ac yn temtio pobl i osgoi'r rheolaeth yn gyfan gwbl.

5. **Ar gyfer pa fathau o newid rydych chi'n ymddiried mewn adolygu awtomataidd a chymorth deallusrwydd artiffisial, a ble mae'n rhaid i berson aros yn atebol?** Mae'r bennod yn dweud y dylid trin allbwn adolygu deallusrwydd artiffisial fel mewnbwn, nid awdurdod: cryf ar faterion wynebol a chysondeb, gwan ar farn dyluniad dwfn a chyd-destun system, gyda pherson yn atebol am bob cymeradwyaeth. Heb ffin eglur, mae tîm mawr yn drifftio i mewn i orymddiried, lle mae sylw bot gwyrdd yn darllen fel adolygiad wedi'i basio ac mae risgiau dyluniad a diogelwch go iawn yn llithro drwodd dan hyder ffug. Y dynfa gystadleuol yw bod adolygu deallusrwydd artiffisial mewn gwirionedd yn ysgafnhau baich ac yn dal namau cyffredin yn ddiflino, felly mae ei wahardd yn gwastraffu trosoledd. Dewch â'r dystiolaeth: ble mae awgrymiadau awtomataidd wedi dal materion go iawn, ble maent wedi cynhyrchu sŵn, a pha fathau o newid (sensitif o ran diogelwch, perthnasol i gydymffurfiaeth, pensaernïol) na fyddech byth yn gadael i beiriant eu llofnodi ar ei ben ei hun. Ar gyfer gwaith menter a llywodraeth, enwch pwy sy'n dal atebolrwydd am gymeradwyaeth pan oedd cynorthwyydd deallusrwydd artiffisial yn y ddolen, gan y bydd archwiliad yn gofyn pwy adolygodd newid, ac nid yw "y teclyn a wnaeth" yn ateb y bydd rheoleiddiwr yn ei dderbyn.

6. **Ble dylai paru neu raglennu torf ddisodli adolygu anghydamserol, a sut ydych chi'n defnyddio adolygu i leihau risg ffactor bws yn fwriadol?** Mae'r bennod yn fframio rhaglennu mewn parau a rhaglennu torf fel adolygu parhaus a ddewiswyd yn ôl cyd-destun, ac mae'n enwi adolygu fel y mecanwaith sy'n lledaenu gwybodaeth fel na ddeellir unrhyw ran o'r system gan un person yn unig. Wedi'i adael yn oblygedig, mae gwybodaeth yn crynhoi: mae'r un arbenigwr yn adolygu pob newid i is-system, mae adolygu'n troi'n stamp rwber am na all neb arall eu herio, ac mae risg ffactor bws yn tyfu'n union lle mae'r system fwyaf critigol. Yr ystyriaeth gystadleuol yw cost, gan fod rhaglennu torf yn gwario amser y tîm cyfan a bod paru'n clymu dau beiriannydd, felly ni allwch ei orfodi ym mhobman. Dewch â'r dystiolaeth: pa fodiwlau sydd ag un adolygydd credadwy yn unig, ble mae sefydlu'n stopio, a ble byddai maes anodd yn elwa o sesiwn fyw dros edafedd sylwadau. Mewn sefydliad mawr neu gyhoeddus, trinwch ledaeniad gwybodaeth bwriadol fel rheoli risg, gan fod system hirhoedlog y mae ei rhannau critigol yn dibynnu ar un person yn atebolrwydd gweithredol a pharhad, nid anghyfleustra staffio yn unig.

## Trwy lens sector

**Cwmni newydd.** Gyda thri neu bedwar peiriannydd, cadwch adolygu'n ysgafn: cymeradwyaeth un cydweithiwr ar gais tynnu bach, gwiriadau mecanyddol yn CI, a dim ail adolygydd gorfodol a fyddai'n stopio uniad. Y nod go iawn yw llai o gydymffurfiaeth na sicrhau bod mwy nag un person yn deall pob rhan o'r system, felly parwch ar y darnau peryglus a thriniwch hynny fel sefydlu. Peidiwch ag adeiladu llwybro perchnogaeth cod trwm y byddwch yn ei dyfu allan ohono cyn bo hir; mae norm a rennir o newidiadau bach, wedi'u disgrifio'n dda yn prynu'r rhan fwyaf o'r budd am fron dim cost.

**Busnes bach.** Nid oes gennych arbenigwr offer adolygu yn debygol, felly pwyswch ar yr hyn y mae eich platfform lletya (er enghraifft gwasanaeth Git rheoledig) yn ei roi allan o'r bocs yn hytrach nag adeiladu awtomeiddio pwrpasol. Prynwch yr integreiddiadau leintio, profi, a sganio diogelwch yn lle eu cynnal, fel bod eich ychydig beirianwyr yn gwario eu munudau adolygu prin ar ddyluniad a chywirdeb. Cadwch un rheol syml, mae pob newid yn cael un pâr arall o lygaid, a gwrthsefwch ychwanegu proses nad oes gennych neb i'w chynnal.

**Menter.** Yr her yw cysondeb ar draws llawer o dimau: safonau a rennir, rheolau perchnogaeth cod sy'n llwybro newidiadau sensitif at y cymeradwywyr cywir, a chymeradwyaethau rôl-seiliedig wedi'u cofnodi fel tystiolaeth archwilio. Awtomeiddiwch y gwiriadau mecanyddol ar draws y sefydliad fel bod adolygu dynol yn canolbwyntio ar ddyluniad, ac olrheiniwch hwyrni adolygu fel metrig llif fel nad yw rheolaethau aml-adolygydd gorfodol yn dawel yn dod yn dagfeydd. Cydweddwch ddyfnder adolygu â risg newid gyda pholisi wedi'i ddogfennu, fel bod newidiadau dibwys yn aros yn gyflym tra bo rhai risg uchel yn cael gwahanu dyletswyddau a chraffu dyfnach.

**Llywodraeth.** Mae rheoli newid yn aml yn orfodol: pob newid cynhyrchiad wedi'i adolygu a'i gymeradwyo gan rywun heblaw'r awdur, gyda'r cofnod wedi'i gadw fel tystiolaeth archwilio i fodloni gofynion gwahanu dyletswyddau. Ffafriwch lwybr tryloyw, olrheiniadwy o bwy a'i hawdurodd, pwy a'i cymeradwyodd, a pha wiriadau a basiodd, a buddsoddwch mewn awtomeiddio a newidiadau bach, aml fel nad yw'r rheolaeth yn rhewi cyflenwi. Lle caffaelir offer adolygu, mynnwch gofnodion archwilio y gellir eu hallforio ac osgowch glymu i mewn i un gwerthwr, gan fod yn rhaid i'r dystiolaeth oroesi unrhyw un gwerthwr sengl a sefyll craffu cyhoeddus.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd pedwar peiriannydd yn cadw pob cais tynnu'n fach ac yn gofyn am gymeradwyaeth un cydweithiwr cyn uno, llai er cydymffurfiaeth na sicrhau nad un person yn unig sy'n deall rhan o'r system. Mae CI'n rhedeg y fformatiwr a'r profion, fel bod y bobl yn gwario eu hychydig funudau adolygu ar ddyluniad a chywirdeb yn hytrach nag agor bylchau. Pan fydd y tîm yn taro darn anodd o'r llif taliadau, mae dau ohonynt yn paru arno yn lle cyfnewid sylwadau anghydamserol, sydd hefyd yn dyblu fel sefydlu ar gyfer y penodiad diweddaraf.

**Menter.** Mae cwmni meddalwedd mawr yn mynnu o leiaf un adolygiad cymeradwyol ar bob newid, ynghyd ag ail gymeradwyaeth ar gyfer newidiadau i fodiwlau sensitif o ran diogelwch a nodwyd gan reolau perchnogaeth cod. Mae CI'n trin pob gwiriad arddull a phrawf, fel bod adolygwyr yn canolbwyntio ar ddyluniad a chywirdeb. Mae'r tîm yn olrhain amser-i-adolygiad-cyntaf ac yn trin canolrif sy'n codi fel signal i ailgydbwyso llwyth gwaith. Mae peirianwyr newydd yn cael eu sefydlu drwy baru, sy'n byrhau eu llwybr tuag at gyfrannu'n annibynnol.

**Llywodraeth.** Mae asiantaeth genedlaethol sy'n gweithredu dan ofynion rheoli newid llym yn mynnu bod pob newid cynhyrchiad yn cael ei adolygu a'i gymeradwyo gan rywun heblaw'r awdur, gyda'r gymeradwyaeth wedi'i chofnodi ar gyfer archwilio. I gadw'r rheolaeth hon rhag dod yn dagfa, mae'r asiantaeth yn buddsoddi mewn gwiriadau awtomataidd a newidiadau bach, aml, ac yn gosod norm ymateb adolygu'r un diwrnod. Mae'r llwybr adolygu, sy'n cwmpasu pwy a'i hawdurodd, pwy a'i cymeradwyodd, a pha wiriadau a basiodd, yn dod yn rhan o'r dystiolaeth gydymffurfiaeth ar gyfer pob rhyddhad, gan fodloni gofynion gwahanu dyletswyddau heb rewi cyflenwi.

## Achos busnes: cymhellion, ROI, a TCO

Mae adolygiad cod yn talu'n ôl i chi mewn tair arian cyfred: namau a ddaliwyd cyn cynhyrchiad, gwybodaeth wedi'i lledaenu ar draws y tîm, a safonau wedi'u cynnal yn awtomatig dros amser. Mae dal nam mewn adolygiad yn llawer rhatach na'i ddal mewn cynhyrchiad, ac mae'r budd rhannu gwybodaeth yn lleihau risg person-allweddol a all fel arall gostio'n ddrud i sefydliad pan fydd rhywun yn gadael. Mae adolygu hefyd yn fecanwaith trosglwyddo diwylliannol sy'n cadw tîm sy'n tyfu'n gydlynol.

Cost adolygu yw amser peiriannydd a rhywfaint o hwyrni, y mae'r ddau'n hydrin gydag arferion da. Mae cost *peidio* ag adolygu, neu adolygu'n wael, yn cynnwys namau cynhyrchiad, gwybodaeth mewn seilos, cod anghyson, ac, mewn lleoliadau rheoledig, archwiliadau wedi methu a chanfyddiadau cydymffurfiaeth. Mae gan adolygu gor-drwm ei gost go iawn ei hun hefyd: ciwiau hir, bagiau rhy fawr, peirianwyr wedi'u digalonni. I wneud yr achos i arweinyddiaeth, cysylltwch arferion adolygu â chyfradd methiant newid, amser arwain cyflenwi, a chyflymder sefydlu, ac olrheiniwch hwyrni adolygu fel metrig llif eglur.

## Gwrth-batrymau a pheryglon

- **Y stamp rwber:** cymeradwyaethau heb archwiliad go iawn, yn rhoi sicrwydd ffug ac yn bodloni dim ond llythyren rheolaeth.
- **Y PR anferth:** miloedd o linellau na ellir ond eu sgimio, gan warantu adolygiad bas.
- **Adolygu manion-yn-unig:** canolbwyntio ar drifialau tra'n colli dyluniad a chywirdeb, yn aml am nad yw gwiriadau mecanyddol wedi'u hawtomeiddio.
- **Adolygu fel gwarchod giât:** defnyddio adolygu i honni tra-arglwyddiaeth neu rwystro eraill, gan wenwyno cydweithio.
- **Y ciw araf:** adolygiadau sy'n eistedd am ddiwrnodau, yn stopio cyflenwi ac yn annog bagio.
- **Gorymddiried mewn adolygu deallusrwydd artiffisial:** trin awgrymiadau awtomataidd fel rhai awdurdodol a gollwng barn ddynol ar newidiadau peryglus.
- **Rhwystro ar sail dewis:** cyflwyno barn arddull bersonol fel newidiadau gofynnol heb eu gwahaniaethu oddi wrth namau go iawn.

## Model aeddfedrwydd

- **Lefel 1, Cychwyn:** Mae adolygu'n ad hoc ac yn adweithiol. Fe'i hepgorir yn aml neu fe'i gwneir yn anghyson, mae materion mecanyddol yn dominyddu'r sylwadau, nid yw normau adborth wedi'u gosod, ac mae unrhyw lwybr cymeradwyo'n ddigwyddiadol yn hytrach na bwriadol.
- **Lefel 2, Datblygu:** Mae arferion adolygu sylfaenol yn bodoli ond yn amrywio o dîm i dîm. Mae adolygu'n ofynnol mewn rhai mannau ac yn araf neu'n ddewisol mewn eraill, mae awtomeiddio'n rhannol, ac mae maint ac ansawdd cais tynnu'n siglo'n eang heb ddisgwyliad a rennir.
- **Lefel 3, Safoni:** Mae safonau wedi'u dogfennu a'u gorfodi ar draws y sefydliad. PRs bach, ffocysedig, fformatio, leintio, profion, a sganio diogelwch awtomataidd yn CI, rhestrau gwirio clir, confensiwn rhwystro-yn-erbyn-awgrym eglur, a rheolau perchnogaeth cod sy'n llwybro newidiadau sensitif at y cymeradwywyr cywir.
- **Lefel 4, Rheoli:** Mesurir a rheolir adolygu yn erbyn llinellau sylfaen. Olrheinir amser-i-adolygiad-cyntaf, amser-i-uno, dyfnder adolygu yn erbyn risg newid, cyfradd dianc namau, a chyfradd methiant newid; trinnir hwyrni parhaus fel problem broses; ac mae'r data'n gyrru ble i ailgydbwyso llwyth adolygwyr a ble mae rheolaethau'n arafu cyflenwi heb ychwanegu sicrwydd.
- **Lefel 5, Cydgysylltu:** Gwellir adolygu'n barhaus a'i integreiddio ar draws y sefydliad. Mae dyfnder yn addasu i risg newid, defnyddir paru, rhaglennu torf, a chymorth deallusrwydd artiffisial yn fwriadol gyda pherson yn atebol, rheolir lledaeniad gwybodaeth a risg ffactor bws yn fwriadol, ac mae adolygu'n gwella ansawdd, llif cyflenwi, a sefydlu mewn ffordd fesuradwy.

## Syniadau ar gyfer trafodaeth

- Beth yw'r targed hwyrni adolygu cywir ar gyfer eich tîm, a beth sy'n eich atal rhag ei daro?
- Sut ydych chi'n cydweddu dyfnder adolygu â risg newid heb ychwanegu biwrocratiaeth?
- Ble mae paru neu raglennu torf yn perfformio'n well nag adolygu anghydamserol yn eich cyd-destun chi?
- Faint y dylid ymddiried mewn adolygu â chymorth deallusrwydd artiffisial, a ar gyfer pa fathau o newidiadau?
- Sut ydych chi'n cadw adborth adolygu'n adeiladol wrth i'r tîm dyfu ac amrywio?
- Sut ydych chi'n bodloni gofynion cymeradwyo cydymffurfiaeth heb greu tagfeydd?

## Casgliadau allweddol

- Cadwch geisiadau tynnu'n fach a wedi'u disgrifio'n dda; yr awdur sy'n berchen ar addasrwydd i'w adolygu.
- Awtomeiddiwch y mecanyddol fel bod pobl yn adolygu dyluniad, cywirdeb, a phrofion.
- Olrheiniwch a rheolwch hwyrni adolygu fel cost llif i'r tîm cyfan.
- Cydweddwch ddyfnder adolygu â risg newid, a gwahaniaethwch faterion sy'n rhwystro oddi wrth ddewisiadau.
- Defnyddiwch baru, rhaglennu torf, a chymorth deallusrwydd artiffisial fel cyflenwadau sy'n cyd-fynd â chyd-destun, gan gadw person yn atebol.

## Cyfeiriadau a darllen pellach

- Karl Wiegers, *Peer Reviews in Software: A Practical Guide*
- Google, *Engineering Practices: How to Do a Code Review* (fel esiampl gyfeirnodol)
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Kent Beck, *Extreme Programming Explained* (ar raglennu mewn parau)
- Woody Zuill, ysgrifau ar raglennu torf
- Michael Lopp, *Managing Humans* (ar gydweithio peirianneg)
