# 8.1 CI/CD a thraddodi

## Trosolwg a chymhelliant

Mae [integreiddio parhaus](https://en.wikipedia.org/wiki/Continuous_integration) a [thraddodiad parhaus](https://en.wikipedia.org/wiki/Continuous_delivery) (CI/CD) yn wead cysylltiol rhwng ysgrifennu cod a'i osod o flaen defnyddwyr yn ddiogel. Mae integreiddio parhaus yn golygu bod pob newid yn cael ei uno'n aml i mewn i brif linell a rennir, yna'n cael ei adeiladu a'i brofi'n awtomatig, fel bod problemau integreiddio'n ymddangos o fewn munudau yn hytrach nag ar ddiwedd cylchred rhyddhau hir. Mae traddodiad parhaus yn golygu bod pob newid sy'n pasio'r biblinell yn cael ei gadw mewn cyflwr defnyddiadwy, fel bod rhyddhau i gynhyrchu'n dod yn benderfyniad busnes yn hytrach na sgrialu peirianneg. Mae [defnyddio parhaus](https://en.wikipedia.org/wiki/Continuous_deployment) yn mynd gam ymhellach ac yn rhyddhau pob newid sy'n pasio'n awtomatig, heb unrhyw gât ddynol.

I dimau mawr, mae'r gwahaniaethau hyn yn bwysig yn aruthrol. Pan fydd cannoedd o beirianwyr yn ymrwymo i systemau sy'n gorgyffwrdd, mae cost integreiddio â llaw a phrofi â llaw yn tyfu'n an-llinol. Piblinell a rennir, wedi'i hawtomeiddio yw'r unig ffordd ymarferol o roi adborth cyflym, dibynadwy i lawer o gyfranwyr ac o gadw newid un tîm rhag torri un arall yn dawel. Mae'r biblinell yn dod yn unig ffynhonnell wirionedd ynghylch a yw'r meddalwedd yn iach, ac mae'n gorfodi cysondeb na all unrhyw faint o ddogfennaeth na bwriadau da ei warantu ar raddfa.

Mae cyd-destunau menter a llywodraeth yn ychwanegu un dimensiwn arall: archwiliadwyedd a rheolaeth newid. Mae angen tystiolaeth ar reoleiddwyr, swyddogion diogelwch, ac archwilwyr fod newidiadau wedi'u hadolygu, eu profi, a'u cymeradwyo, a bod yr arteffact sy'n rhedeg mewn cynhyrchu yn union yr un un a adeiladwyd ac a wiriwyd. Mae piblinell CI/CD wedi'i dylunio'n dda yn troi'r rhwymedigaethau cydymffurfio hyn o faich papurau'n sgil-gynnyrch awtomatig o'r llif gwaith peirianneg arferol. Wedi'i wneud yn dda, mae traddodiad yn dod yn gyflymach ac yn fwy diogel ar yr un pryd, sef y canlyniad sy'n bwysicaf i arweinyddiaeth.

*Gweler hefyd:* pennod 8.4 (peirianneg platfform a phrofiad datblygwr), pennod 8.5 (awtomeiddio profi a phroses), a phennod 7.4 (dadansoddeg cynnyrch ac arbrofi) ar gyfer yr arferion [fflag nodwedd](https://en.wikipedia.org/wiki/Feature_toggle) (switshys amser rhedeg sy'n amlygu ymarferoldeb i ddefnyddwyr heb ailddefnyddio) ac arbrofi y mae traddodiad blaengar (rhyddhau newid yn raddol tra'n monitro ei fetrigau iechyd yn awtomatig) yn eu galluogi.

## Egwyddorion allweddol

- Integreiddiwch newidiadau bach yn aml; canghennau hirhoedlog yw gelyn integreiddio parhaus.
- Adeiladwch yr arteffact unwaith a dyrchafwch yr union arteffact drwy bob amgylchedd.
- Gwnewch y biblinell yn gât awdurdodol: os yw'n wyrdd, mae'r newid yn ddanfonadwy; os yw'n goch, mae gwaith yn stopio nes ei drwsio.
- Optimeiddiwch yn ddiflino ar gyfer adborth cyflym fel bod datblygwyr yn aros mewn llif a namau'n cael eu dal tra bo cyd-destun yn ffres.
- Awtomeiddiwch bopeth sy'n cael ei ailadrodd, gan gynnwys profion, sganiau diogelwch, darpariaeth, a defnyddio.
- Triniwch ddiffiniadau piblinell fel cod wedi'i reoli fersiwn sy'n destun adolygiad, nid fel ffurfweddiad consol clicadwy.
- Dyluniwch ar gyfer rhyddhadau diogel, gwrthdroadwy fel y gellir dadwneud unrhyw ddefnyddiad yn gyflym.
- Gwahanwch ddefnyddio (gosod y cod) oddi wrth ryddhau (ei amlygu i ddefnyddwyr) gan ddefnyddio fflagiau nodwedd.

## Argymhellion

### Dyluniwch y biblinell fel cyfres o gatiau ansawdd

Strwythurwch y biblinell yn gamau sy'n symud o rad a chyflym i ddrud a thrylwyr: crynhoi a phrofion uned yn gyntaf, yna profion integreiddio, sganio trwydded a diogelwch, ac yn olaf defnyddio i lwyfannu a chynhyrchu. Mae pob cam yn gât y mae'n rhaid i newid ei phasio. Trefnwch y gatiau fel bod y gwiriadau cyflymaf, mwyaf tebygol o fethu'n rhedeg gyntaf, sy'n rhoi adborth i ddatblygwyr yn y cyfnod byrraf posibl. Cadwch ddolen adborth cam-ymrwymo o dan ddeg munud lle bynnag y gallwch. Y tu hwnt i hynny, mae datblygwyr yn newid cyd-destun ac mae cynhyrchiant yn gostwng.

### Adeiladwch unwaith, dyrchafwch ym mhobman

Cynhyrchwch un arteffact anghyfnewidiol yn y cam adeiladu a dyrchafwch yr union arteffact hwnnw drwy brofi, llwyfannu, a chynhyrchu. Byth peidiwch ag ailadeiladu fesul amgylchedd, oherwydd gall ailadeiladu gyflwyno gwahaniaethau'n dawel. Dylai ffurfweddiad sy'n amrywio yn ôl amgylchedd gael ei chwistrellu ar amser defnyddio, nid ei bobi i mewn i adeiladau ar wahân. Dyma hefyd yr hyn sy'n gadael i chi ddweud wrth archwiliwr, gyda sicrwydd, mai'r deuaidd mewn cynhyrchu yw'r un a basiodd bob gât.

### Gwnewch y biblinell yn bwynt gorfodi ar gyfer polisi

Amgodiwch wiriadau gofynnol (cymeradwyaeth adolygiad cod, trothwyon sylw prawf, canlyniadau sgan diogelwch, ymrwymiadau wedi'u llofnodi) yn uniongyrchol i'r biblinell a rheolau amddiffyn cangen. Mae polisi â llaw sy'n byw mewn wici'n cael ei osgoi'n rheolaidd o dan bwysau terfyn amser. Mae polisi wedi'i amgodio yn y biblinell yn cael ei gymhwyso'n unffurf ac yn awtomatig i bob newid.

### Cadwch y brif linell yn ryddhadwy bob amser

Defnyddiwch ddatblygu seiliedig-ar-foncyff, sy'n integreiddio'r holl waith i mewn i un gangen a rennir gydag ychydig neu ddim canghennau hirhoedlog, neu defnyddiwch ganghennau nodwedd byrhoedlog, a dibynnwch ar fflagiau nodwedd i guddio gwaith anghyflawn yn hytrach na changhennau hirhoedlog. Mae hyn yn cadw gwrthdrawiadau uno'n fach ac yn cadw'r brif linell bob amser mewn cyflwr defnyddiadwy, sef y rhagofyniad ar gyfer traddodiad parhaus gwirioneddol.

### Dewiswch strategaethau defnyddio'n fwriadol

Cyfatebwch y strategaeth ddefnyddio â risg a phromedr ffrwydro'r gwasanaeth:

- Mae defnyddiadau **treiglo** yn disodli enghreifftiau'n raddol ac yn rhagosodiad synhwyrol ar gyfer gwasanaethau di-gyflwr.
- Mae **[glas-gwyrdd](https://en.wikipedia.org/wiki/Blue-green_deployment)** yn cynnal dau amgylchedd unfath ac yn newid traffig ar unwaith, gan roi llwybr dychwelyd ar unwaith.
- Mae rhyddhadau **canari** yn llwybro canran fach o draffig i'r fersiwn newydd, yn gwylio metrigau iechyd, ac yn ehangu dim ond os yw'r signalau'n dda.
- Mae **fflagiau nodwedd** yn datgysylltu rhyddhau oddi wrth ddefnyddio, gan adael i chi alluogi ymarferoldeb ar gyfer defnyddwyr neu garfannau penodol heb ailddefnyddio.

### Mabwysiadwch draddodiad blaengar gyda dadwneud awtomatig

Mae traddodiad blaengar yn cyfuno rhyddhadau canari â dadansoddiad awtomataidd o fetrigau megis cyfradd gwall, oedi, a dirlawnder. Diffiniwch feini prawf iechyd gwrthrychol ymlaen llaw, yna gadewch i'r system ddyrchafu neu ddadwneud yn awtomatig yn seiliedig ar y signalau hynny. Mae dadwneud awtomatig yn tynnu'r petruster dynol sy'n troi digwyddiad bach yn un mawr.

### Darparwch reolaeth rhyddhau a rheolaeth newid ar gyfer amgylcheddau rheoledig

Mewn lleoliadau rheoledig, cadwch gofnod rheoli-newid ysgafn ond gwirioneddol. Daliwch yn awtomatig pwy gymeradwyodd bob newid, pa brofion a redwyd, a pha arteffact a ddefnyddiwyd. Defnyddiwch brosesau cynghori newid ar gyfer newidiadau risg-uchel gwirioneddol, ond eu cadw ar gyfer yr achosion hynny. Mae llwybro pob newid arferol drwy fwrdd wythnosol yn dinistrio gwerth awtomeiddio. Anelwch yn hytrach at fathau newid safonol, wedi'u cymeradwyo ymlaen llaw sy'n llifo drwy'r biblinell heb seremoni.

## Cyfaddawdau: manteision ac anfanteision

| Dull | Manteision | Anfanteision | Y ffit gorau |
|---|---|---|---|
| Traddodiad parhaus (gât rhyddhau â llaw) | Mae busnes yn rheoli amseriad; cryf ar gyfer ffenestri rhyddhau rheoledig | Yn gofyn am ddisgyblaeth i gadw'r brif linell yn ddanfonadwy | Mentrau â ffenestri newid |
| Defnyddio parhaus (cwbl awtomatig) | Adborth cyflymaf; y bagiau lleiaf | Yn mynnu profion ac arsylwadaeth aeddfed | Timau ymddiriedaeth-uchel, amlder-uchel |
| Glas-gwyrdd | Dadwneud ar unwaith; model meddyliol syml | Yn dyblu cost amgylchedd yn ystod y newid | Gwasanaethau critigol angen dychwelyd cyflym |
| Canari + traddodiad blaengar | Yn cyfyngu promedr ffrwydro; wedi'i yrru gan ddata | Cymhleth i'w adeiladu; angen metrigau da | Systemau wyneb-defnyddiwr graddfa fawr |
| Fflagiau nodwedd | Yn datgysylltu defnyddio o ryddhau | Dyled fflag os na chânt eu glanhau | Timau sy'n anfon gwaith anghyflawn yn ddiogel |

Y cyfaddawd canolog yw cyflymder yn erbyn rheolaeth, ond mae hynny'n aml yn ddewis ffug. Mae awtomeiddio aeddfed yn cyflenwi'r ddau: mae rhyddhadau'n gyflymach oherwydd eu bod yn llai, ac yn fwy diogel oherwydd bod pob un wedi'i wirio a'i wrthdroi. Y gost wirioneddol yw'r buddsoddiad ymlaen llaw mewn sylw prawf, arsylwadaeth, a pheirianneg piblinell, ynghyd â'r ddisgyblaeth barhaus i'w cadw'n iach. Mae sefydliadau sy'n cynilo ar y buddsoddiad hwnnw'n cael y cyflymder heb y diogelwch, sy'n waeth na phroses â llaw araf.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Beth yw eich targed ar gyfer amser adborth cam-ymrwymo, a beth sy'n cael ei dorri pan fydd y set brofion yn tyfu y tu hwnt i ddeg munud?** Mae cam-ymrwymo araf yn lladd integreiddio parhaus yn dawel, oherwydd bod datblygwyr yn stopio aros am wyrdd ac yn dechrau bagio newidiadau. Penderfynwch y rhif nawr (mae'r bennod hon yn dadlau dros lai na deg munud) a phenderfynwch y mecanwaith ar gyfer ei gynnal: gweithwyr paralel, pyramid prawf llym, a symud gwiriadau integreiddio araf i gam diweddarach. Ar raddfa menter mae hyn yn benderfyniad platfform, gan fod cannoedd o beirianwyr yn rhannu'r un biblinell a phob munud a ychwanegir yn lluosi ar draws pob ymrwymiad. Dewch â data gwirioneddol i'r cyfarfod: hyd biblinell p50 a p95 cyfredol, y deg prawf arafaf, a pha mor aml y mae pobl yn ailredeg yn hytrach nag aros. Os na allwch nodi'r targed a'i amddiffyn â rhifau, mae eich piblinell yn drifftio tuag at broses swp mewn gwisg CI.

2. **Pa strategaeth ddefnyddio y mae pob gwasanaeth yn ei defnyddio, a phwy sy'n atebol am y dewis hwnnw?** Nid yw treiglo, glas-gwyrdd, a chanari yn gyfnewidiadwy: maent yn masnachu cost, cyflymder dadwneud, a chymhlethdod yn wahanol, ac mae'r dewis cywir yn dibynnu ar bromedr ffrwydro'r gwasanaeth. Mae glas-gwyrdd yn prynu dadwneud ar unwaith am bris amgylchedd wedi'i ddyblu yn ystod y newid, sy'n werth chweil ar gyfer system daliadau ac yn wastraffus ar gyfer dangosfwrdd mewnol. Mae canari'n cyfyngu amlygiad ond yn mynnu metrigau iechyd da a mwy o beirianneg biblinell. Ar gyfer ystâd fawr neu reoledig, mae gadael hyn i arferiad pob tîm yn cynhyrchu anghysondeb sy'n ymddangos yn ystod digwyddiad, felly cytunwch ar ragosodiadau fesul haen gwasanaeth a chofnodwch y penderfyniad. Dewch â'ch catalog gwasanaeth a thagiwch bob gwasanaeth â'i strategaeth, ei lwybr dadwneud, a'r person sy'n berchen ar yr alwad honno.

3. **Sut ydych chi'n profi bod yr arteffact mewn cynhyrchu yn union yr un a basiodd bob gât?** Adeiladu unwaith a dyrchafu'r union arteffact yw'r gêm gyfan ar gyfer archwiliadwyedd, ac mae'n torri'r foment y mae unrhyw un yn ailadeiladu fesul amgylchedd neu'n clytio blwch sy'n rhedeg. Mewn lleoliadau menter a llywodraeth bydd archwiliwr yn gofyn i chi olrhain deuaidd sy'n rhedeg yn ôl i'w ymrwymiad, ei adolygiad, a'i gymeradwyaethau, ac rydych am i'r ateb hwnnw gymryd eiliadau, nid wythnos. Penderfynwch sut rydych yn ei orfodi: arteffactau anghyfnewidiol, delweddau wedi'u llofnodi, dilysu llofnod ar amser defnyddio, a ffurfweddiad wedi'i chwistrellu ar amser defnyddio yn hytrach na'i bobi i mewn i adeiladau ar wahân. Dewch â'r bylchau cyfredol i'r bwrdd, megis unrhyw gam sy'n ailadeiladu, unrhyw lwybr clyt-poeth â llaw, ac unrhyw le lle mae ffurfweddiad yn fforchio'r arteffact. Mae'r ateb yn penderfynu a yw eich tystiolaeth gydymffurfio'n sgil-gynnyrch o'r biblinell neu'n sgrialu â llaw cyn pob archwiliad.

4. **Pan fydd y brif linell yn mynd yn goch, beth sy'n stopio mewn gwirionedd, a sut ydych chi'n trin profion pigog?** Nid yw piblinell yn gât awdurdodol ond os yw adeiladwaith coch yn wir yn atal gwaith, eto mae llawer o sefydliadau'n goddef prif linell wedi torri'n barhaus a backlog o fethiannau ysbeidiol yn dawel, sy'n hyfforddi datblygwyr i ailredeg nes gwyrdd ac i anfon ar ben methiannau. I dîm mawr mae'r pydredd hwn yn cyfansymio, oherwydd mae pig un tîm sy'n cael ei anwybyddu'n dod yn esgus pawb i osgoi'r gât, ac mae ymddiriedaeth yn y biblinell yn llawer rhatach i'w chynnal nag i'w hailadeiladu. Pwyswch y tyniadau cystadleuol: mae rheol stopio-llym yn diogelu ansawdd ond gall rwystro cannoedd o beirianwyr ar un ymrwymiad gwael, tra bo polisi goddefgar yn cadw trwybwn ac yn erydu'r gât. Dewch â thystiolaeth i'r drafodaeth: eich amser coch prif linell cyfredol, nifer y profion cwarantîn neu bigog, y gyfradd ailredeg, a pha mor aml y mae newidiadau'n uno dros wiriad sy'n methu. Mewn lleoliadau menter a llywodraeth, enwch pwy sy'n berchen ar driage pig a phwy sydd ag awdurdod i rewi uno, oherwydd bydd archwilwyr yn dod o hyd i gât nad oes neb yn atebol am ei gorfodi wedi'i gorddiystyru'n rheolaidd.

5. **Beth yw eich cylchred oes ar gyfer fflagiau nodwedd, a phwy sy'n gyfrifol am eu hymddeol?** Fflagiau yw'r hyn sy'n gadael i chi wahanu defnyddio oddi wrth ryddhau a chuddio gwaith anghyflawn, ond mae pob fflag yn gangen yn eich cod na chaiff ei glanhau ar ei ben ei hun, ac mae fflagiau heb eu rheoli'n cronni'n gymhlethdod amodol na fydd neb yn meiddio ei gyffwrdd. Mewn ystâd fawr mae'r ddyled hon yn beryglus, oherwydd gall fflag hen gatio trwsiad diogelwch yn dawel neu droi llwybrau cod heb eu profi i gynhyrchu, ac mae'r person a'i creodd wedi symud ymlaen yn aml. Cydbwyswch y tensiwn: prynodd fflagiau i chi draddodiad diogel, cynyddrannol, felly nid llai o fflagiau yw'r nod ond cylchred oes ddisgybledig gyda pherchennog, disgwyliad dod-i-ben, ac offer sy'n amlygu rhai hen. Dewch â'r rhestr eiddo gyfredol i'r cyfarfod: faint o fflagiau sy'n fyw, pa mor hen yw'r hynaf, pa rai nad oes ganddynt berchennog, ac a yw unrhyw fflag hirhoedlog bellach yn gweithredu fel ffurfweddiad parhaol sy'n perthyn yn rhywle arall. Ar gyfer amgylcheddau rheoledig, ychwanegwch pwy all newid fflag mewn cynhyrchu ac a yw'r newid hwnnw'n cael ei gofnodi â'r un trylwyredd â defnyddiad, gan fod trosi fflag yn rhyddhad hyd yn oed pan na fydd y biblinell byth yn rhedeg.

6. **Ble mae'r ffin rhwng traddodiad parhaus â gât ddynol a defnyddio parhaus llawn, a phwy sy'n gosod y trothwyon dadwneud?** Mae traddodiad parhaus yn cadw person mewn rheolaeth dros amseriad rhyddhau, sy'n addas ar gyfer ffenestri newid statudol a systemau promedr-ffrwydro-uchel, tra bo defnyddio parhaus yn anfon pob newid sy'n pasio'n awtomatig ac yn mynnu profion aeddfed, arsylwadaeth, a dadwneud awtomatig i fod yn ddiogel. Ar gyfer sefydliad mawr neu reoledig anaml y mae'r ateb yn unffurf: gall eich gwefan farchnata ddefnyddio'n barhaus tra bo eich craidd taliadau'n cadw gât ddynol wedi'i dogfennu, ac mae tynnu'r llinell honno fesul haen gwasanaeth yn atal ffrithiant diangen ac awtomeiddio anghyfrifol fel ei gilydd. Yr ystyriaethau cystadleuol yw cyflymder a maint bagiau yn erbyn rheolaeth ac archwiliadwyedd, ynghyd â chost peirianneg y metrigau iechyd y mae dadwneud awtomatig yn eu mynnu. Dewch â'r dystiolaeth: cyfradd methiant-newid fesul gwasanaeth, amser adfer cyfartalog, cyflymder rhyddhau cyfredol, a'r signalau gwrthrychol (cyfradd gwall, oedi, dirlawnder) y byddech yn eu hymddiried i ddyrchafu neu ddadwneud heb ddyn. Mewn lleoliadau llywodraeth a menter, cysylltwch bob haen â phwy sy'n berchen ar y trothwyon dadwneud a phwy sy'n arwyddo unrhyw symudiad o ryddhad wedi'i gatio i awtomeiddiad llawn, fel bod y penderfyniad yn fwriadol yn hytrach na drifftiol.

## Lens sector

**Busnes newydd.** Pwyswch ar CI/CD wedi'i reoli o ddiwrnod un: rhedwr wedi'i westeio, un biblinell, un ddelwedd anghyfnewidiol, a defnyddio awtomatig i lwyfannu ar uno. Peidiwch ag adeiladu seilwaith piblinell y bydd yn rhaid i chi ei gynnal wedyn. Mae fflagiau nodwedd yn gadael i ddau neu dri pheiriannydd uno gwaith hanner-orffenedig yn ddiogel ac anfon sawl gwaith y dydd, ac mae defnyddiad cynhyrchu un-clic ynghyd â diffodd fflag cyflym yn cynrychioli'r holl reolaeth newid sydd ei angen arnoch hyd nes bo graddfa'n gorfodi mwy.

**Busnes bach.** Heb beiriannydd platfform neu ryddhau penodedig, ffafriwch y biblinell y mae eich gwesteiwr ffynhonnell yn ei rhoi i chi (Actions adeiledig neu gyfatebol) a'i strategaeth ddefnyddio ragosodedig dros unrhyw beth pwrpasol. Fframiwch y dewis prynu-yn-erbyn-adeiladu'n onest: mae piblinell wedi'i reoli a llwyfan gwesteia â dadwneud adeiledig yn costio llai na'r oriau peiriannydd y mae gosodiad pwrpasol yn eu treulio. Cadwch yr hanfodion, sef adeiladu unwaith, dyrchafu'r un arteffact, a dychweliad hawdd, a sgipiwch y peirianwaith traddodiad blaengar hyd nes bo cyfaint yn ei gyfiawnhau.

**Menter.** Y broblem graidd yw cysondeb ar draws llawer o dimau: safonwch dempled biblinell a rennir sy'n gorfodi adolygiad, sganio, arteffactau anghyfnewidiol wedi'u llofnodi, a strategaethau defnyddio fesul haen, fel nad yw ansawdd yn amrywio fesul tîm. Triniwch ddiffiniadau piblinell fel cod wedi'i adolygu, daliwch dystiolaeth rheoli-newid yn awtomatig, a rheolwch fflagiau nodwedd a throthwyon dadwneud fel asedau wedi'u llywodraethu yn hytrach nag arferiad preifat pob tîm. Yr enillion yw traddodiad cyflymach a thystiolaeth archwilio wedi'i chynhyrchu fel sgil-gynnyrch yn lle sgrialu chwarterol.

**Llywodraeth.** Mae rheolau caffael, ffenestri newid statudol, ac atebolrwydd cyhoeddus yn siapio'r biblinell. Ffafriwch draddodiad parhaus â gât rhyddhau ddynol wedi'i dogfennu dros awtomeiddiad llawn ar gyfer systemau canlyniadol, dosbarthwch waith arferol fel newidiadau safonol wedi'u cymeradwyo ymlaen llaw, a chadwch lwybr dadwneud ar unwaith (glas-gwyrdd neu ganari awtomataidd) ar gyfer gwasanaethau y mae dinasyddion yn dibynnu arnynt yn ystod ffenestri blynyddol cul. Sicrhewch fod y biblinell yn cofnodi pwy gymeradwyodd bob newid, pa brofion a redwyd, a pha arteffact a ddefnyddiwyd, fel bod rhwymedigaethau tryloywder ac archwilio'n cael eu bodloni gan y llif gwaith arferol yn hytrach na phapurau â llaw.

## Enghreifftiau

**Busnes newydd.** Mae busnes newydd SaaS pedwar person yn cysylltu un biblinell GitHub Actions sy'n rhedeg profion uned, yn adeiladu un ddelwedd Docker, ac yn defnyddio'r un ddelwedd honno i lwyfannu'n awtomatig ar bob uno i main. Mae defnyddiad cynhyrchu'n un clic, ac mae'r sylfaenwyr yn pwyso ar fflagiau nodwedd fel y gallant uno gwaith hanner-orffenedig y tu ôl i fflag yn lle cadw cangen yn fyw am wythnosau. Pan fydd rhyddhad gwael yn llithro drwodd, maent yn diffodd y fflag mewn eiliadau ac yn ei drwsio'n dawel, sy'n cadw eu tîm bach yn anfon sawl gwaith y dydd heb berson gweithrediadau penodedig.

**Menter.** Mae banc byd-eang yn cyfuno dwsinau o swyddi Jenkins penodol-i-dîm i mewn i dempled biblinell safonedig y mae pob tîm cynnyrch yn ei etifeddu. Mae'r templed yn gorfodi dadansoddiad statig, sganio dibyniaeth, ac arteffact anghyfnewidiol wedi'i lofnodi, ac mae'n defnyddio drwy ganari â dadwneud awtomataidd wedi'i allweddu i drothwyon cyfradd-gwall ac oedi. Gan fod yr un arteffact yn cael ei ddyrchafu o brawf i gynhyrchu a bod pob gât yn cael ei chofnodi, gall archwilwyr y banc olrhain unrhyw ddeuaidd cynhyrchu yn ôl i'w ymrwymiad, ei adolygiad, a'i gymeradwyaeth mewn eiliadau, gan ddisodli ymarfer casglu tystiolaeth â llaw chwarterol.

**Llywodraeth.** Mae asiantaeth dreth genedlaethol sy'n moderneiddio system ffeilio'n mabwysiadu traddodiad parhaus â gât rhyddhau ddynol benodol, fel y gall barchu ffenestri newid statudol yn ystod tymor ffeilio. Caiff newidiadau arferol eu dosbarthu fel newidiadau safonol wedi'u cymeradwyo ymlaen llaw sy'n llifo'n awtomatig i lwyfannu. Mae rhyddhad cynhyrchu'n mynnu un gymeradwyaeth ddogfennedig y mae'r biblinell yn ei chofnodi. Mae defnyddiad glas-gwyrdd yn rhoi llwybr dadwneud ar unwaith i'r asiantaeth os yw nam yn cyrraedd cynhyrchu, sy'n hanfodol pan fo miliynau o ddinasyddion yn dibynnu ar y gwasanaeth yn ystod ffenestr flynyddol gul.

## Achos busnes: cymhellion, ROI, a TCO

Mae'r enillion ar fuddsoddiad CI/CD yn ymddangos fel amser blaenori is ar gyfer newidiadau, cyfradd methiant-newid is, ac adferiad cyflymach pan fydd digwyddiadau'n digwydd: y metrigau y mae ymchwil yn eu cysylltu'n gyson â pherfformiad traddodi a chanlyniadau sefydliadol fel ei gilydd. Mae rhyddhadau cyflymach, llai'n torri baich cydgysylltu sy'n treulio capasiti peirianneg ar raddfa, ac mae dilysu awtomataidd yn torri'r gwaith drud, sy'n draenio morâl o ddiffodd tanau namau cynhyrchu.

Mae cyfanswm cost perchnogaeth yn pwyso cost mabwysiadu yn erbyn cost peidio â mabwysiadu. Mae costau mabwysiadu'n cynnwys adeiladu a chynnal piblinellau, tyfu sylw prawf, a buddsoddi mewn arsylwadaeth a staff platfform. Mae cost peidio â mabwysiadu'n fwy ond yn llai gweladwy: rhyddhadau â llaw araf, poen integreiddio, digwyddiadau cynhyrchu sy'n niweidio enw da, ac, mewn lleoliadau rheoledig, archwiliadau a fethodd ac adfer. I arweinyddiaeth, gorau po fwyaf y mae'r ddadl wedi'i fframio o ran lleihau risg a chapasiti. Mae awtomeiddio'n trosi amser prin peiriannydd uwch o slafdod rhyddhau ailadroddol yn waith cynnyrch, tra'n gwneud toriadau'n brinnach ac yn fyrrach.

## Gwrth-batrymau a pheryglon

- **Piblinellau plu eira.** Mae pob tîm yn adeiladu piblinell unigryw â llaw, felly ni ellir rhannu gwelliannau a thrwsiadau ac mae ansawdd yn amrywio'n wyllt.
- **Ailadeiladu fesul amgylchedd.** Mae ailadeiladu ar gyfer pob cam yn torri'r warant "adeiladu unwaith" ac yn gadael i wahaniaethau cynnil gyrraedd cynhyrchu.
- **Adeiladwaith coch wedi'i anwybyddu.** Mae goddef prif linell wedi torri'n barhaus yn dinistrio ymddiriedaeth yn y biblinell ac yn normaleiddio anfon ar ben methiannau.
- **Profion pigog heb eu trin.** Mae methiannau ysbeidiol yn hyfforddi datblygwyr i ailredeg nes gwyrdd, gan drechu pwrpas y gât.
- **Theatr cymeradwyo â llaw.** Mae bwrdd cynghori newid sy'n stampio rwber popeth yn ychwanegu oedi heb ychwanegu diogelwch.
- **Dyled fflag.** Mae fflagiau nodwedd nad ydynt byth yn cael eu tynnu'n cronni'n gymhlethdod amodol na ellir ei gynnal.
- **Defnyddio'n hafal i ryddhau.** Mae cyplu'r ddau'n golygu bod pob newid wyneb-defnyddiwr yn mynnu ailddefnyddiad risgus.

## Model aeddfedrwydd

**Lefel 1: Cychwyn.** Mae adeiladau a defnyddiadau i raddau helaeth â llaw, ad hoc, ac adweithiol. Mae integreiddio'n digwydd yn hwyr, mae rhyddhadau'n anfynych ac yn straenus, mae dadwneud yn golygu ailddefnyddio hen fersiwn â llaw, ac nid oes syniad a rennir o gât biblinell.

**Lefel 2: Datblygu.** Mae adeiladau a phrofion uned awtomataidd yn rhedeg ar bob ymrwymiad, ond mae arferion yn amrywio fesul tîm. Mae defnyddiadau wedi'u sgriptio ond dal wedi'u sbarduno a'u goruchwylio â llaw, mae rhai amgylcheddau'n gyson, a gellir ailadeiladu arteffactau o hyd fesul cam. Lle mae piblinell yn bodoli mae'n aml yn blu eira na ellir ei rannu.

**Lefel 3: Safoni.** Caiff templed biblinell safonedig, wedi'i ddogfennu ei orfodi ar draws timau. Mae'n dyrchafu un arteffact anghyfnewidiol drwy bob amgylchedd, yn cymhwyso gatiau ansawdd a diogelwch awtomataidd, yn amgodio gwiriadau gofynnol megis cymeradwyaeth adolygiad a chanlyniadau sgan, ac yn dal cofnodion newid yn awtomatig. Dewisir strategaethau defnyddio megis canari neu las-gwyrdd yn fwriadol fesul haen gwasanaeth.

**Lefel 4: Rheoli.** Caiff traddodiad ei fesur a'i reoli yn erbyn llinellau sylfaen. Mae'r sefydliad yn olrhain amser blaenori ar gyfer newidiadau, amlder defnyddio, cyfradd methiant-newid, ac amser adfer cyfartalog, ynghyd â hyd biblinell p50 a p95, cyfraddau prawf pigog ac ailredeg, ac oedran fflag nodwedd. Caiff trothwyon dadwneud eu gosod o ddata cyfradd-gwall, oedi, a dirlawnder a arsylwyd, gorfodir gatiau ar sail tystiolaeth yn hytrach nag arferiad, ac mae gan bob metrig berchennog sy'n gweithredu pan fydd yn drifftio o'r targed.

**Lefel 5: Cerddorfa.** Mae traddodiad yn gwella'n barhaus ac wedi'i integreiddio ar draws y sefydliad. Mae traddodiad blaengar â dadwneud awtomataidd, wedi'i yrru gan fetrigau yn norm, mae rhyddhad wedi'i ddatgysylltu o ddefnyddio drwy fflagiau wedi'u llywodraethu'n dda, a chynhyrchir tystiolaeth gydymffurfio'n awtomatig fel sgil-gynnyrch. Mae'r biblinell yn addasu wrth i'r ystâd newid, ac mae metrigau traddodi'n bwydo cynllunio busnes a risg fel bod buddsoddiad yn llifo i'r gwelliannau â'r trosoledd uchaf.

## Syniadau ar gyfer trafodaeth

- Ble mae'r ffin gywir rhwng traddodiad parhaus â gât ddynol a defnyddio parhaus llawn ar gyfer eich systemau mwyaf critigol?
- Sut ydych chi'n cadw proses rheoli-newid orfodol yn ystyrlon heb ei throi'n theatr stampio rwber?
- Pa fetrigau iechyd gwrthrychol ddylai lywodraethu dadwneud awtomataidd, a phwy sy'n berchen ar eu trothwyon?
- Sut ddylai timau platfform gydbwyso templedi piblinell safonedig yn erbyn anghenion dilys timau â gofynion anarferol?
- Beth yw eich polisi a'ch offer ar gyfer ymddeol fflagiau nodwedd cyn iddynt ddod yn ddyled?
- Sut ydych chi'n mesur a yw traddodiad cyflymach yn wir yn gwella canlyniadau busnes yn hytrach na dim ond anfon mwy?

## Casgliadau allweddol

- Mae CI, CD, a defnyddio parhaus yn wahanol; dewiswch lefel yr awtomeiddio sy'n cyfateb â'ch goddefgarwch risg a'ch aeddfedrwydd.
- Adeiladwch yr arteffact unwaith a dyrchafwch yr union arteffact drwy bob amgylchedd.
- Dyluniwch y biblinell fel gatiau ansawdd wedi'u trefnu wedi'u hoptimeiddio ar gyfer adborth cyflym, a'i thrin fel y penderfyniad traddodi awdurdodol.
- Dewiswch strategaethau defnyddio'n fwriadol, a mabwysiadwch draddodiad blaengar gyda dadwneud awtomataidd i gyfyngu promedr ffrwydro.
- Datgysylltwch ryddhau oddi wrth ddefnyddio â fflagiau nodwedd, a rheolwch ddyled fflag.
- Mewn amgylcheddau rheoledig, daliwch dystiolaeth rheoli-newid yn awtomatig yn hytrach na thrwy bapurau â llaw.

## Cyfeiriadau a darllen pellach

- Jez Humble and David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*.
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Gene Kim, Kevin Behr, and George Spafford, *The Phoenix Project*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering*.
- Pete Hodgson, "Feature Toggles (Feature Flags)" (essay).
- ITIL (Information Technology Infrastructure Library), change management guidance.
