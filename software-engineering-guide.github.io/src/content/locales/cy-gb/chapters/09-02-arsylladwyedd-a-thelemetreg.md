# 9.2 Arsylladwyedd a thelemetreg

## Trosolwg a chymhelliant

Mae [telemetreg](https://en.wikipedia.org/wiki/Telemetry) yn ddata y mae system yn ei allyrru am ei hymddygiad ei hun: y metrigau, y cofnodion, y traciau, a'r digwyddiadau a gesglir o feddalwedd sy'n rhedeg. Mae monitro'n ateb cwestiynau roeddech eisoes yn gwybod i'w gofyn o'r delemetreg honno. A yw'r ddisg yn llawn? A yw'r gyfradd wallau uwchben trothwy? A yw'r gwasanaeth i fyny? Mae [arsylladwyedd](https://en.wikipedia.org/wiki/Observability_(software)) yn ehangach. Y gallu yw i ofyn cwestiynau newydd am gyflwr mewnol system o'r tu allan, heb ryddhau cod newydd, fel y gallwch ddeall ymddygiad na wnaethoch erioed ei ragweld. Wrth i systemau dyfu'n bensaernïaeth ddosbarthedig, [microwasanaeth](https://en.wikipedia.org/wiki/Microservices), a [phensaernïaeth wedi'i sbarduno gan ddigwyddiadau](https://en.wikipedia.org/wiki/Event-driven_architecture), y methiannau sy'n brifo fwyaf yw'r rhai na welodd neb yn dod, ac arsylladwyedd yw'r hyn sy'n gadael i chi eu datrys. Mae monitro'n dweud wrthych fod rhywbeth o'i le. Mae arsylladwyedd yn eich helpu i ddarganfod pam.

I dimau mawr, mae'r gwahaniaeth hwn yn benderfynol. Gallech ddeall monolith drwy ddarllen cofnodion ar un peiriant. Mae platfform modern yn rhychwantu cannoedd o wasanaethau, llawer o dimau, sawl rhanbarth, a dibyniaethau trydydd parti, lle gall un cais defnyddiwr gyffwrdd dwsinau o gydrannau. Nid oes yr un person yn dal y system gyfan yn ei ben. Daw telemetreg o ansawdd uchel, wedi'i rhannu, yn feinwe gyswllt sy'n gadael i unrhyw beiriannydd ddilyn cais ar draws ffiniau, alinio symptomau ar draws gwasanaethau, a rhesymu am system nad oes neb yn berchen arni'n llawn. Hebddi, mae digwyddiadau'n llusgo ymlaen, mae bai'n hedfan rhwng timau, ac mae achosion gwraidd yn aros yn guddiedig.

Mae systemau menter a llywodraeth yn codi'r stanciau gyda chydymffurfiaeth, archwiliadwyedd, ac atebolrwydd cyhoeddus. Gall rheoleiddwyr fynnu tystiolaeth o bwy a gafodd fynediad at beth a phryd. Mae angen telemetreg ar dimau diogelwch i ganfod ymyriadau. Rhaid i wasanaethau sy'n wynebu dinasyddion ddangos eu bod yn cyrraedd eu hymrwymiadau perfformiad cyhoeddedig. Mae arsylladwyedd da yn gwasanaethu'r rhain i gyd ar unwaith: mae'n declyn peirianneg, yn reolaeth ddiogelwch, ac yn fecanwaith atebolrwydd, i gyd mewn un. Mae safoni ar offeryniaeth agored yn osgoi clymu i asiantau perchnogol un gwerthwr, sy'n bwysig dros ben pan fo'n rhaid i systemau bara degawdau a goroesi cylchoedd caffael.

*Gweler hefyd:* pennod 9.1 (peirianneg dibynadwyedd safle a SLOs), pennod 9.3 (rheoli digwyddiadau), a phennod 3.3 (systemau dosbarthedig).

## Egwyddorion allweddol

- **Offeryna ar gyfer cwestiynau anhysbys.** Dyluniwch delemetreg fel y gallwch ymchwilio i fethiannau newydd, y tu hwnt i'r rhai a ragwelsoch.
- **Tri philer, un stori.** Mae metrigau, cofnodion, a thraciau'n olygfeydd cydategol; mae eu gwerth yn lluosi pan gânt eu cydberthyn, nid eu seilo.
- **Strwythurwch bopeth.** Mae telemetreg strwythuredig, y gellir ei phrosesu gan beiriant, gyda meysydd cyson yn curo testun rhydd y gall dynion yn unig ei ddarllen.
- **Cydberthynwch gyda dynodwyr a rennir.** Mae IDs trac a chais wedi'u lledaenu ym mhobman yn gadael i chi bwytho un digwyddiad ar draws gwasanaethau.
- **Rhybuddiwch am symptomau, nid achosion.** Bipiwch bobl am broblemau y gall defnyddwyr eu gweld; gadewch i ddangosfyrddau ac ymchwiliad ddatgelu'r achos sylfaenol.
- **Rhaid i bob bip fod yn weithredadwy.** Mae rhybudd nad oes angen unrhyw weithred ddynol arno'n sŵn sy'n erydu ymddiriedaeth ac yn achosi blinder.
- **Mae cardinalrwydd uchel yn nodwedd.** Y gallu i sleisio yn ôl defnyddiwr, cais, rhanbarth, a fersiwn yw'r hyn sy'n gwneud dadfygio mewn cynhyrchiad yn bosibl.
- **Byddwch berchen ar eich offeryniaeth.** Safonwch ar delemetreg agored, niwtral o ran gwerthwr fel eich bod yn rheoli eich data ac yn gallu newid cefndiroedd.

## Argymhellion

### Adeiladu ar y tri philer a thu hwnt

Mae **metrigau** yn gyfresi amser rhifiadol, yn rhad i'w storio ac yn ddelfrydol ar gyfer dangosfyrddau, tueddiadau, a throthwyon rhybuddio. Mae **cofnodion** yn gofnodion arwahanol, wedi'u stampio ag amser, o ddigwyddiadau, yn gyfoethog o fanylion ac yn hanfodol ar gyfer ymchwiliad fforensig. Mae **[traciau](https://en.wikipedia.org/wiki/Tracing_(software))** yn dilyn un cais wrth iddo symud drwy wasanaethau, gan ddangos oedi a dibyniaethau ar draws y graff galwadau dosbarthedig. Y tu hwnt i'r rhain, ystyriwch **ddigwyddiadau** (newidiadau cyflwr ystyrlon megis defnyddiadau), **proffiliau** (lle mae cod yn treulio CPU a chof), ac [**monitro defnyddwyr go iawn**](https://en.wikipedia.org/wiki/Real_user_monitoring) o brofiad y cleient go iawn. Nid oes unrhyw biler sengl yn ddigon ar ei ben ei hun. Y nod yw symud yn hyblyg rhyngddynt yn ystod ymchwiliad.

### Safoni ar OpenTelemetry a chofnodi strwythuredig

Mabwysiadwch [OpenTelemetry](https://en.wikipedia.org/wiki/OpenTelemetry) fel y safon niwtral o ran gwerthwr ar gyfer cynhyrchu a chasglu metrigau, cofnodion, a thraciau. Mae'n gwahanu offeryniaeth oddi wrth y cefndir dadansoddi, felly gallwch newid gwerthwyr heb ail-offeryna cannoedd o wasanaethau. Mae'r priodwedd honno'n hanfodol ar gyfer systemau menter a llywodraeth hirhoedlog. Allyrrwch gofnodion fel cofnodion strwythuredig (er enghraifft JSON) gydag enwau maes cyson ar gyfer stamp amser, difrifoldeb, gwasanaeth, a dynodwyr. Lledaenwch ID trac neu gydberthyniad o'r ymyl drwy bob galwad i lawr yr afon, a chynhwyswch ef ym mhob llinell gofnod ac esiamplydd metrig, fel bod y tri philer yn cysylltu'n awtomatig.

### Dylunio rhybuddio ar gyfer gweithredadwyedd a sŵn isel

Mae eich athroniaeth rybuddio'n penderfynu a yw ar-alwad yn gynaliadwy. Rhybuddiwch yn bennaf am symptomau y mae defnyddwyr yn eu teimlo, wedi'u mynegi fel cyfraddau llosgi SLO ([amcan lefel gwasanaeth](https://en.wikipedia.org/wiki/Service-level_objective)). Bipiwch pan fyddwch yn llosgi drwy'ch cyllideb gwallau (y diffyg a ganiateir o'r amcan hwnnw) yn ddigon cyflym i'w thorri, gan ddefnyddio rhybuddion cyfradd llosgi aml-ffenestr i gydbwyso canfod cyflym yn erbyn larymau ffug. Cadwch bipio ar gyfer problemau sydd angen gweithred ddynol ar unwaith, a chyfeiriwch bopeth arall at docynnau neu ddangosfyrddau. Tocurwch rybuddion sy'n tanio heb angen gweithred, yn ddidostur, oherwydd bod blinder rhybuddio'n brif achos digwyddiadau go iawn a gollwyd a llosgi-allan ar-alwad. Dylai pob rhybudd gysylltu â llawlyfr gweithredu.

### Modelu iechyd gyda dangosfyrddau a monitro SLO

Adeiladwch ddangosfyrddau o gwmpas model iechyd eglur, nid wal o bob metrig sydd gennych. Mae fframwaith cychwynnol da yn "y pedwar arwydd euraidd": oedi, traffig, gwallau, a dirlawnder. Crëwch ddangosfyrddau lefel gwasanaeth sy'n dangos statws SLO a chyllideb gwallau sy'n weddill ar gip, ynghyd â dangosfyrddau lefel uwch sy'n modelu iechyd system a thaith defnyddiwr gyffredinol. Curadwch nhw'n fwriadol, oherwydd bod dangosfyrddau sy'n dangos popeth yn cyfleu dim. Cadwch nhw'n agos at y rhybuddion a'r llawlyfrau gweithredu, fel bod ymatebwyr yn symud yn gyflym o signal i gyd-destun i weithred.

### Galluogi dadfygio mewn cynhyrchiad gyda chardinalrwydd uchel

Mae'r problemau cynhyrchu anoddaf yn taro sleisen gul: un cwsmer, un rhanbarth, un fersiwn API, un math dyfais. I'w hymchwilio mae angen telemetreg **cardinalrwydd uchel** arnoch, y gallu i grwpio a hidlo yn ôl meysydd sydd â llawer o werthoedd gwahanol megis ID defnyddiwr neu ID cais. Mae digwyddiadau eang, wedi'u priodoli'n gyfoethog sy'n cario llawer o ddimensiynau fesul cofnod yn gadael i chi ofyn cwestiynau mympwyol wedi'r ffaith. Cadwch ddigon o gardinalrwydd a ffyddlondeb samplu i ynysu allanolion, a ffafriwch draciau wedi'u cysylltu ag esiamplyddion fel bod pigyn ar fetrig yn eich arwain yn syth at geisiadau araf cynrychioliadol.

### Rheoli cost, cadw, a samplu

Mae cyfaint telemetreg yn tyfu gyda'r system a gall droi'n draul sylweddol. Gosodwch bolisïau cadw yn ôl dosbarth data: cadwch ddata cydraniad uchel yn fyr a chyfansymiau'n hwy. Cymhwyswch samplu deallus i draciau, wedi'i ogwyddo tuag at gadw gwallau a cheisiadau araf, fel eich bod yn dal gafael ar y gynffon ddiddorol heb dalu am bob llwyddiant arferol. Adolygwch eich gwariant telemetreg yn rheolaidd, oherwydd gall costau arsylladwyedd heb eu rheoli gystadlu â'r seilwaith y maent yn ei arsylwi.

## Cymharu: manteision ac anfanteision

| Penderfyniad | Manteision | Anfanteision |
|---|---|---|
| Digwyddiadau cardinalrwydd uchel | Dadfygio pwerus, gofyn unrhyw beth | Cost storio ac ymholi uwch |
| Samplu ymosodol | Cost is, llai o sŵn | Gall golli digwyddiadau prin |
| Rhybuddio ar sail symptomau | Llai o bipiau, yn weithredadwy | Angen SLOs da i weithio'n dda |
| Safon OpenTelemetry | Niwtral o ran gwerthwr, cludadwy | Ymdrech mudo, offer sy'n aeddfedu |
| Cadw cofnodion hir | Fforensig ac archwiliad gwell | Cost storio, dinoethiad preifatrwydd |

Mae penderfyniadau arsylladwyedd yn dod i lawr i dyndra rhwng ffyddlondeb a chost. Mae dal popeth ar gydraniad llawn yn rhoi trosolwg ôl-syllol perffaith i chi, ond ar raddfa mae'n ddrud dros ben. Torrwch yn ymosodol a byddwch yn arbed arian, ond efallai y byddwch yn taflu ymaith yr un cofnod a fyddai wedi esbonio toriad. Mae haenau samplu a chadw'n ffordd y mae timau aeddfed yn cerdded y llinell hon, gan gadw gwallau ac allanolion tra'n teneuo data arferol. Mae'r cyfaddawd rhybuddio rhwng sensitifrwydd a sŵn: mae gormod o rybuddion yn achosi blinder a digwyddiadau a gollwyd, mae rhy ychydig yn gadael i broblemau ffestro. Mae rhybuddio ar sail symptomau, wedi'i yrru gan SLO, yn datrys llawer o hyn, ond dim ond os oes gennych SLOs ystyrlon ar waith.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Beth yw eich cynllun i symud gwasanaethau etifeddol i OpenTelemetry, a sut ydych chi'n osgoi talu am ddwy stac offeryniaeth yn ystod y trawsnewid?** Offeryniaeth niwtral o ran gwerthwr yw'r briodwedd sy'n gadael i chi newid cefndiroedd heb ail-offeryna cannoedd o wasanaethau, ac mae'n bwysicaf ar gyfer y systemau menter a llywodraeth hirhoedlog sy'n goroesi unrhyw gontract gwerthwr unigol. Y mudo yw lle mae bwriadau da'n stolio: mae ystadau hanner-offerynedig yn gadael bylchau yn union lle mae cais yn croesi o wasanaeth newydd i un hen, gan dorri'r trac o'r dechrau i'r diwedd. Dewch ag arolwg i'r drafodaeth: pa wasanaethau sy'n allyrru data asiant perchnogol, pa rai sy'n allyrru OpenTelemetry, a ble mae cyd-destun trac yn cael ei ollwng ar y ffin. Penderfynwch drefn sy'n dilyn llwybrau cais go iawn yn hytrach na siartiau sefydliadol, a chyllidwch ar gyfer y ffenestr lle rydych yn rhedeg y ddau gasglwr. Mae'r ateb yn penderfynu a ydych chi mewn gwirionedd yn berchen ar eich telemetreg ynteu'n dal wedi'ch clymu i asiantau un gwerthwr.

2. **Pryd wnaethoch chi archwilio pob rhybudd ddiwethaf am weithredadwyedd, a faint o bipiau y mis diwethaf nad oedd angen unrhyw weithred ddynol arnynt?** Mae blinder rhybuddio'n brif achos digwyddiadau go iawn a gollwyd a llosgi-allan ar-alwad, felly nid yw bip nad oes angen gweithred yn sŵn diniwed, mae'n erydu'n weithredol yr ymateb rydych yn dibynnu arno. Dewch â'r derbynebau: tynnwch bipiau'r mis diwethaf, marciwch bob un fel un a weithredwyd neu a anwybyddwyd, a chyfrwch faint a fapiodd at lawlyfr gweithredu. I dîm mawr sy'n rhychwantu llawer o wasanaethau, mae rhybuddion swnllyd gan un tîm yn dad-sensiteiddio'r ar-alwad a rennir i bawb. Gosodwch safon fod pob bip yn cysylltu â llawlyfr gweithredu ac yn clymu at gyfradd llosgi SLO, yna dilëwch y gweddill yn ddidostur. Dylai canlyniad yr archwiliad hwn dorri eich cyfaint bipio'n uniongyrchol a dweud wrthych pa wasanaethau nad oes ganddynt SLO ystyrlon y tu ôl i'w rhybuddion.

3. **Beth yw eich strategaeth samplu traciau, a pha mor hyderus ydych chi ei bod yn cadw'r gwallau a'r gynffon araf?** Mae cyfaint telemetreg yn tyfu gyda'r system a gall cost arsylladwyedd heb ei reoli gystadlu â'r seilwaith y mae'n ei arsylwi, felly byddwch yn samplu, a'r cwestiwn yw a ydych yn samplu'n ddeallus. Mae dinoethi cardinalrwydd neu samplu'n ddall yn tynnu union y cofnodion sydd eu hangen i ddadfygio'r problemau cul sy'n taro un cwsmer, un rhanbarth, neu un fersiwn API. Dewch â'ch haenau cadw a'ch rheolau samplu presennol: a ydych yn gogwyddo tuag at gadw gwallau a cheisiadau araf, gan ddefnyddio traciau wedi'u cysylltu ag esiamplyddion fel bod pigyn metrig yn arwain at gais araf cynrychioliadol? Ar gyfer systemau a archwilir ac sydd wedi'u rhwymo gan breifatrwydd, cysoni cadw â rheolau lleihau data fel nad ydych yn pentyrru data personol i ddadfygio. Mae'r ateb yn gosod ble rydych yn gwario cyllideb telemetreg ac a fydd eich toriad mawr nesaf yn esboniadwy neu'n ddirgelwch.

4. **Pa rai o'ch SLOs sy'n ymrwymiadau taith defnyddiwr go iawn, a pha rai sy'n fetrigau dirprwy nad oes neb y tu allan i'r tîm perchennog yn eu credu?** Dim ond pan fo'r symptomau'n mapio at bethau y mae defnyddwyr yn eu teimlo go iawn y mae rhybuddio ar sail symptomau'n gweithio, felly mae rhybudd wedi'i weirio at drothwy CPU neu darged argaeledd wedi'i ddyfeisio'n bipio pobl am broblemau nad ydynt o bwys efallai, tra'n aros yn dawel am rai sydd o bwys. I sefydliad mawr, mae SLOs hefyd yn gontract sy'n gadael i dimau annibynnol rannu cylchdro ar-alwad heb ailddadlau difrifoldeb yn ystod pob digwyddiad. Dewch â chatalog SLO cyfredol, y daith defnyddiwr y bwriedir i bob amcan ei ddiogelu, a thoriadau'r chwarter diwethaf gydag a wnaeth cwsmeriaid gwyno go iawn. Mewn lleoliadau menter a llywodraeth, clymwch y SLOs mwyaf gweladwy at yr ymrwymiadau perfformiad cyhoeddedig y mae'r gwasanaeth yn cael ei ddal iddynt, fel bod yr un signal cyfradd llosgi sy'n bipio peiriannydd hefyd yn dystiolaeth y byddech yn ei ddangos i reoleiddiwr neu gorff goruchwylio. Dylai'r drafodaeth ymddeol y metrigau dirprwy a'ch gadael gyda rhestr fer o amcanion y byddai person nad yw'n beiriannydd yn eu hadnabod fel addewidion i ddefnyddwyr.

5. **Pwy sy'n berchen ar lywodraethu data telemetreg, ac a allwch brofi bod data personol yn cael ei olygu cyn iddo lanio yn eich cefndir arsylladwyedd?** Mae digwyddiadau cardinalrwydd uchel a chadw cofnodion hir yn union y nodweddion sy'n gwneud dadfygio'n bosibl, ac union y rhai sy'n troi storfa arsylladwyedd yn gopi heb ei reoli o ddata personol eich defnyddwyr. Mae'r tyniad cystadleuol yn real: mae peirianwyr eisiau priodoleddau cyfoethocach a chadw hirach, tra bo preifatrwydd a chyfreithiol eisiau lleihau data a hydoedd oes byrrach. Dewch â map llif data sy'n dangos pa feysydd sy'n cario data personol neu sensitif, ble mae golygu neu docenoli'n digwydd yn y biblinell, a beth yw eich haenau cadw fesul dosbarth data. Ar gyfer systemau a reoleiddir a chyhoeddus, enwch y perchennog atebol, mapiwch gadw at y sail gyfreithlon a'r rheolau lleihau data rydych yn gweithredu odanynt, a byddwch yn barod i ddangos i archwiliwr fod mynediad at y delemetreg ei hun wedi'i gofnodi a'i reoli. Mae'r ateb yn penderfynu a yw eich platfform arsylladwyedd yn ased ynteu'n doriad sefydlog sy'n aros i gael ei ddarganfod.

6. **Pan fo digwyddiad yn croesi gwasanaethau sawl tîm, a yw eich telemetreg yn gadael i un ymatebwr ddilyn y cais o'r dechrau i'r diwedd, ynteu a yw'r trywydd yn torri ym mhob ffin perchnogaeth?** Addewid llawn telemetreg gydberthynol, wedi'i lledaenu ag IDs, yw y gall un peiriannydd resymu am system nad oes neb yn berchen arni'n llawn, ac mae'r addewid hwnnw'n cwympo yn union ar y ffin lle mae cyd-destun trac yn cael ei ollwng neu lle mae dau dîm yn defnyddio dynodwyr ac offer anghydnaws. Pwyswch y tyniad tuag at ymreolaeth fesul tîm wrth ddewis offer arsylladwyedd yn erbyn cost a rennir ystad ddarniog lle mae pob trosgyfnewidiad yn ben marw yn ystod toriad. Dewch ag amserlen digwyddiad traws-dîm diweddar a marciwch ble collodd yr ymatebwr y trywydd, ynghyd ag arolwg o ba wasanaethau sy'n lledaenu ID cydberthyniad cyffredin a pha rai nad ydynt. I fenter fawr neu blatfform llywodraeth wedi'i gydosod o lawer o werthwyr a systemau hirhoedlog, penderfynwch faint rydych yn ei orfodi'n ganolog, safon cyd-destun trac a rennir a chynllun ID cyffredin, yn erbyn beth rydych yn ei adael i dimau, oherwydd bod yn rhaid i'r cydrannau rydych yn eu hail-gaffael dros ddegawdau ryng-weithredu o hyd ar yr un cais. Mae'r ateb yn dweud wrthych a fydd eich digwyddiad traws-dîm nesaf yn ymchwiliad cydgysylltiedig neu'n rownd o bwyntio bysedd.

## Trwy lens sector

**Cwmni newydd.** Gyda llond llaw o wasanaethau a dim dwylo sbâr, offerynwch gydag OpenTelemetry o'r diwrnod cyntaf a rhyddhewch gofnodion JSON strwythuredig sy'n cario un ID cais o'r dechrau i'r diwedd. Mae'r buddsoddiad bach hwnnw'n troi "mae'r rhaglen yn araf" yn drac y gallwch ei ddarllen, ac mae'n eich cadw'n rhydd i symud o haen rad ac am ddim i gefndir taledig yn ddiweddarach heb ail-offeryna. Hepgorwch ddangosfyrddau cywrain a pheirianwaith SLO hyd nes bod gennych ddefnyddwyr y gallwch fesur eu profiad go iawn.

**Busnes bach.** Nid oes gennych arbenigwr arsylladwyedd a chyllideb dynn, felly pwyswch ar gefndir wedi'i reoli lle mae offeryniaeth, storio, a dangosfyrddau'n dod wedi'u bwndelu yn hytrach nag ymgynnull eich stac eich hun. Mae'r penderfyniad prynu-yn-erbyn-adeiladu'n ffafrio prynu bron bob tro yma; gwell treulio eich sylw prin ar y ddwy neu dair rhybudd arwydd euraidd sy'n dweud wrthych fod y gwasanaeth i lawr nag ar redeg piblinell delemetreg. Gosodwch derfyn cadw caled fel na all cost telemetreg dawelu goddiweddyd y seilwaith y mae'n ei wylio.

**Menter.** Y gwaith yw llywodraethu ar draws llawer o dimau: safon OpenTelemetry a rennir, cynllun ID cydberthyniad cyffredin, a dangosfyrddau SLO wedi'u curadu fel y gall un ymatebwr ddilyn cais ar draws dwsinau o wasanaethau. Rheolwch delemetreg fel canolfan gost gyda haenau cadw a pholisi samplu, safonwch rybuddio ar gyfraddau llosgi SLO i gadw ar-alwad a rennir yn gynaliadwy, a thocurwch rybuddion swnllyd yn ganolog fel nad yw blinder un tîm yn dad-sensiteiddio pawb. Triniwch yr haen offeryniaeth fel seilwaith niwtral o ran gwerthwr sy'n goroesi unrhyw gontract cefndir unigol.

**Llywodraeth.** Mae rheolau caffael, tryloywder, ac atebolrwydd cyhoeddus yn llywio'r dyluniad. Safonwch ar offeryniaeth agored fel bod system y disgwylir iddi redeg am ddegawdau'n goroesi ail-gaffael gan wahanol werthwyr heb gael ei dal yn wystl i asiantau perchnogol, a mynnwch y gludadwyedd honno yn y contract. Defnyddiwch gofnodion archwilio strwythuredig i ddangos pwy gafodd fynediad at ba gofnod a phryd, golygwch neu docenolwch ddata personol cyn iddo gyrraedd y storfa delemetreg, a chysonwch gadw â chyfraith lleihau data. Cyhoeddwch ddangosfyrddau SLO ar gyfer gwasanaethau sy'n wynebu dinasyddion fel bod yr un signalau y mae eich peirianwyr yn eu gwylio hefyd yn dystiolaeth weladwy o'r ymrwymiadau rydych yn cael eich dal iddynt.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd pedwar person yn rhyddhau cefn symudol ac yn parhau i gael cwynion amwys "mae'r rhaglen yn araf" na all eu hatgynhyrchu. Mae'r tîm yn ychwanegu OpenTelemetry at ei lond llaw o wasanaethau ac yn newid i gofnodion JSON strwythuredig gydag ID cais wedi'i gario o'r rhaglen drwy bob naid. Mae'r adroddiad araf nesaf yn datrys mewn munudau: mae un trac yn dangos mynegai cronfa ddata coll ar dabl archebion o dan ymholiad penodol. Am iddynt ddewis offeryniaeth agored yn gynnar, maent yn ddiweddarach yn symud o haen rad ac am ddim i gefndir taledig heb ail-offeryna dim byd.

**Menter.** Mae platfform e-fasnach mawr yn offeryna pob gwasanaeth gydag OpenTelemetry, gan ledaenu ID trac o borwr y cwsmer drwy dalu, taliad, stoc, a chludo. Pan fo trosi'n gostwng, mae peiriannydd ar-alwad yn dechrau o rybudd cyfradd llosgi SLO, yn agor arwyddion euraidd dangosfwrdd talu, yn sylwi ar oedi uwch mewn un rhanbarth, ac yn dilyn trac esiamplydd at alwad cronfa ddata araf mewn un gwasanaeth. Mae priodoleddau cardinalrwydd uchel yn dangos bod y broblem wedi'i chyfyngu i un categori cynnyrch, sy'n llywio ateb wedi'i dargedu mewn munudau yn hytrach nag oriau.

**Llywodraeth.** Mae gwasanaeth iechyd cenedlaethol yn rhedeg platfform cofnodion cleifion o dan reolau archwilio a phreifatrwydd caeth. Mae cofnodion strwythuredig yn cipio pwy gafodd fynediad at ba gofnod a phryd, gan fwydo monitro diogelwch ac adrodd cydymffurfiaeth fel ei gilydd, tra bo meysydd adnabod personol yn cael eu golygu neu eu tocenoli mewn telemetreg. Mae dangosfyrddau SLO cyhoeddus yn dangos argaeledd ac oedi ar gyfer archebu apwyntiadau sy'n wynebu dinasyddion. Drwy safoni ar offeryniaeth agored, mae'r asiantaeth yn osgoi clymu perchnogol ar draws system y disgwylir iddi redeg am ddegawdau a chael ei hail-gaffael gan wahanol werthwyr dros ei hoes.

## Achos busnes: cymhellion, ROI, a TCO

Y prif enillion ar arsylladwyedd yw gostyngiad dramatig yn yr amser mae'n ei gymryd i ganfod a datrys digwyddiadau. I wasanaeth lle mae amser segur yn ddrud, mae torri'r amser cymedrig i ddatrys o oriau i funudau'n talu am yr offer sawl gwaith drosodd mewn un digwyddiad mawr. Mae arsylladwyedd hefyd yn arbed amser peirianneg y byddech chi fel arall yn ei dreulio'n dyfalu, yn atgynhyrchu namau, ac yn dadlau ynghylch pa dîm sydd ar fai, ac mae'n byrhau'r ddolen adborth sy'n gadael i dimau ryddhau'n hyderus. Mae'r gwerth diogelwch a chydymffurfiaeth yn real hefyd: mae'r un delemetreg yn cefnogi canfod ymyriadau a thystiolaeth archwilio.

Mae cyfanswm cost perchnogaeth yn cynnwys ymdrech offeryniaeth, costau storio ac ymholi telemetreg, a'r ddisgyblaeth i guradu signal o sŵn. Mae'r costau hyn yn weladwy ac yn ailadroddol, sy'n temtio arweinyddiaeth i dan-fuddsoddi. Mae cost peidio â mabwysiadu'n fwy ond yn anoddach i'w weld: toriadau estynedig, problemau perfformiad heb eu diagnosio, digwyddiadau diogelwch a ddarganfyddir yn hwyr neu byth, a pheirianwyr yn llosgi allan ar rybuddion na allant wneud dim yn eu cylch. Gwnewch yr achos gyda data digwyddiad diriaethol. Dangoswch yr amser datrys ac effaith fusnes toriadau diweddar, a rhagamcanwch y gostyngiad y byddai telemetreg well yn ei gyflenwi. Mae fframio arsylladwyedd fel yswiriant sydd hefyd yn cyflymu cyflenwi, yn hytrach na chanolfan gost bur, yn ennill y ddadl.

## Gwrth-batrymau a pheryglon

- **Rhybuddio am bopeth.** Mae bipio am bob anghysondeb yn hyfforddi ymatebwyr i anwybyddu rhybuddion, felly mae digwyddiadau go iawn yn llithro drwodd.
- **Bipio ar sail achos.** Mae rhybuddio am achosion mewnol yn hytrach na symptomau defnyddiwr yn boddi ar-alwad â sŵn ac yn colli methiannau newydd.
- **Cofnodion heb eu strwythuro.** Mae cofnodion testun rhydd na ellir eu hymholi na'u cydberthyn yn gorfodi grepio araf, â llaw yn ystod digwyddiadau.
- **Tri philer wedi'u seilo.** Mae metrigau, cofnodion, a thraciau mewn offer datgysylltiedig heb IDs a rennir yn atal dilyn digwyddiad o'r dechrau i'r diwedd.
- **Gwasgariad dangosfyrddau.** Mae cannoedd o ddangosfyrddau heb eu curadu'n golygu nad oes neb yn gwybod pa un sy'n dangos a yw'r system yn iach.
- **Cwymp cardinalrwydd.** Mae dinoethi meysydd cardinalrwydd uchel i arbed cost yn tynnu union y data sydd ei angen i ddadfygio problemau cul.
- **Clymu i werthwr.** Mae asiantau perchnogol ym mhobman yn gwneud newid cefndiroedd yn ddrud dros ben ac yn dal eich data'n wystl.

## Model aeddfedrwydd

**Lefel 1, Cychwyn.** Mae arsylladwyedd yn ad hoc ac yn adweithiol. Mae gwiriadau amser i fyny sylfaenol a chofnodion heb eu strwythuro'n byw ar beiriannau unigol, mae dadfygio'n golygu mewngofnodi i weinyddion i grepio, ac nid oes telemetreg a rennir. Mae rhybuddion yn swnllyd, yn seiliedig ar achos, ac yn aml yn cael eu hanwybyddu, felly mae digwyddiadau go iawn yn dod i'r wyneb drwy gwynion defnyddwyr yn hytrach na signalau.

**Lefel 2, Datblygu.** Mae arferion sylfaenol yn ymddangos ond yn amrywio fesul tîm. Mae rhai gwasanaethau'n gwthio metrigau a chofnodion i le canolog, mae ychydig o ddangosfyrddau a rhybuddion trothwy'n bodoli, ond mae cofnodion ond yn hanner-strwythuredig ac mae traciau'n absennol neu'n rhannol. Mae cydberthyn ar draws gwasanaethau'n llafurus â llaw, ac mae a all peiriannydd ddilyn cais o'r dechrau i'r diwedd yn dibynnu ar ba dimau sy'n digwydd bod yn ymwneud.

**Lefel 3, Safoni.** Mae offeryniaeth wedi'i dogfennu a'i gorfodi ar draws y sefydliad. OpenTelemetry ar draws gwasanaethau gydag ID trac neu gydberthyniad wedi'i ledaenu, cofnodi strwythuredig gydag enwau maes cyson, traciad dosbarthedig, dangosfyrddau arwydd euraidd wedi'u curadu, a rhybuddio symptomau ar sail SLO yw'r safon y mae pob tîm yn ei dilyn. Mae pob bip yn cysylltu â llawlyfr gweithredu ac yn clymu at SLO, ac mae ar-alwad yn gynaliadwy yn hytrach na ffynhonnell llosgi-allan.

**Lefel 4, Rheoli.** Mesurir a rheolir yr ystad arsylladwyedd ei hun yn erbyn llinellau sylfaen. Rydych yn olrhain sylwedd offeryniaeth a chyfradd lledaenu cyd-destun trac ar draws gwasanaethau, y gyfran o bipiau a weithredwyd yn erbyn a anwybyddwyd, amser cymedrig i ganfod a datrys, cyflawniad SLO a llosgi cyllideb gwallau, a chost telemetreg fesul gwasanaeth yn erbyn cyllideb. Gyrrir bylchau a sŵn rhybuddio i lawr gyda data tuag at dargedau eglur, gwirir ffyddlondeb samplu fel bod cofnodion gwallau a'r gynffon araf yn goroesi, a gwneir penderfyniadau bwrw ymlaen neu beidio ar gwmpas a chadw ar sail tystiolaeth yn hytrach na barn.

**Lefel 5, Cerddorfeiddio.** Caiff arsylladwyedd ei wella'n barhaus a'i integreiddio ar draws y sefydliad. Mae telemetreg gardinalrwydd uchel, gyfoethog o ddigwyddiadau'n galluogi ymchwiliad ad hoc o unrhyw sleisen, mae rhybuddio wedi'i yrru gan gyfradd llosgi SLO gyda sŵn lleiaf, ac mae samplu a chadw'n addasu i gost a risg sy'n newid. Mae telemetreg yn bwydo cynllunio capasiti, canfod diogelwch, a phenderfyniadau cynnyrch fel mater o drefn, ac mae'r platfform yn ail-diwnio ei signalau, cyllidebau, a chwmpas ei hun wrth i'r system, y darlun bygythiad, a'r rhwymedigaethau rheoliadol newid.

## Syniadau i'w trafod

- Ble mae'r cydbwysedd cywir rhwng ffyddlondeb telemetreg a chost ar gyfer eich gwasanaethau mwyaf critigol?
- Sut ydych chi'n penderfynu beth sy'n haeddu bip yn erbyn tocyn yn erbyn cofnod dangosfwrdd yn unig?
- Beth yw eich strategaeth ar gyfer lledaenu IDs cydberthyniad ar draws timau nad ydynt yn rhannu sylfaen god na chylch rhyddhau?
- Sut ydych chi'n cadw pŵer dadfygio cardinalrwydd uchel wrth fodloni gofynion preifatrwydd a lleihau data?
- A ddylai offer arsylladwyedd gael ei orfodi'n ganolog neu ei ddewis fesul tîm, a beth yw'r canlyniadau naill ffordd?
- Sut byddech chi'n dangos i archwilwyr fod eich telemetreg yn gyflawn ac yn amlwg-ymyrryd?

## Prif negeseuon

- Mae monitro'n canfod problemau hysbys; mae arsylladwyedd yn gadael i chi ymchwilio i rai anhysbys heb ryddhau cod newydd.
- Mae metrigau, cofnodion, a thraciau werthfawrocaf pan gânt eu cydberthyn drwy ddynodwyr a rennir, nid eu seilo.
- Safonwch ar OpenTelemetry a chofnodi strwythuredig i aros yn niwtral o ran gwerthwr ac yn gludadwy ar draws bywydau system hir.
- Rhybuddiwch am symptomau y gall defnyddwyr eu gweld drwy gyfraddau llosgi SLO, gwnewch bob bip yn weithredadwy, a thocurwch sŵn yn ddidrugaredd.
- Curadwch ddangosfyrddau o gwmpas model iechyd eglur megis yr arwyddion euraidd yn hytrach na dangos pob metrig.
- Telemetreg gardinalrwydd uchel, gyfoethog o ddigwyddiadau yw'r hyn sy'n gwneud dadfygio problemau cynhyrchu cul yn bosibl.

## Cyfeiriadau a darllen pellach

- Charity Majors, Liz Fong-Jones, George Miranda, *Observability Engineering: Achieving Production Excellence*
- Cindy Sridharan, *Distributed Systems Observability*
- Betsy Beyer et al., *Site Reliability Engineering* (chapters on monitoring and alerting)
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud*
- OpenTelemetry project, specification and documentation (Cloud Native Computing Foundation)
- Google, *The Four Golden Signals* (Site Reliability Engineering, monitoring chapter)
