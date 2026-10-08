# 2.2 Egwyddorion cynllunio meddalwedd

## Trosolwg a chymhelliant

Mae egwyddorion cynllunio meddalwedd yn hewristigau ar gyfer trefnu cod fel y gallwch ei ddeall, ei newid, a'i ymestyn dros amser. Maent yn cynnwys acronymau enwedig ([SOLID](https://en.wikipedia.org/wiki/SOLID) ar gyfer pum egwyddor gynllunio [gwrthrych-gyfeiriedig](https://en.wikipedia.org/wiki/Object-oriented_programming), [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) ar gyfer peidiwch-ag-ailadrodd-eich-hun, [KISS](https://en.wikipedia.org/wiki/KISS_principle) ar gyfer cadwch-bethau'n-syml, [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it) ar gyfer ni-fyddwch-ei-angen), cysyniadau strwythurol ([cyplysu](https://en.wikipedia.org/wiki/Coupling_(computer_programming)), [cydlyniad](https://en.wikipedia.org/wiki/Cohesion_(computer_science)), [gwahanu pryderon](https://en.wikipedia.org/wiki/Separation_of_concerns)), [patrymau cynllunio](https://en.wikipedia.org/wiki/Software_design_pattern) wedi'u catalogio, dulliau modelu lefel uwch fel [Cynllunio wedi'i Yrru gan Barth](https://en.wikipedia.org/wiki/Domain-driven_design) (modelu meddalwedd yn iaith y parth busnes), a'r dewis rhwng arddulliau gwrthrych-gyfeiriedig, [gweithredol](https://en.wikipedia.org/wiki/Functional_programming), a [data-ganolog](https://en.wikipedia.org/wiki/Data-oriented_design). Nid yw'r un o'r rhain yn gyfreithiau. Profiad wedi'i gywasgu ydynt, ac mae'n rhaid i chi eu cymhwyso â barn.

I dimau mawr, cydgysylltu yw gwerth egwyddorion a rennir. Pan fydd cannoedd o beirianwyr yn gweithio ar yr un system, mae angen geirfa gyffredin arnynt ar gyfer trafodaethau cynllunio a set gyffredin o ragosodiadau fel bod modiwlau a ysgrifennwyd yn annibynnol yn ffitio gyda'i gilydd. Cynllunio da yw'r hyn sy'n gadael i lawer o bobl newid system yn gyfochrog heb wrthdrawiadau cyson. Dyma hefyd yr hyn sy'n cadw system yn newidiadwy ddegawd yn ddiweddarach, oes arferol systemau menter a llywodraeth, ymhell wedi cyfnod eu hawduron gwreiddiol.

Nid cofio egwyddorion ar y cof yw'r sgil hanfodol. Gwybod pryd mae pob un yn eich camarwain yw hynny. Mae gan bob egwyddor fodd methiant: gall DRY gynhyrchu'r haniaeth anghywir, gall SOLID gynhyrchu anuniongyrchedd diangen, gall YAGNI lwgu ehangadwyedd sydd wir ei angen arnoch. Mae'r bennod hon yn trin egwyddorion fel offer gyda maes cymhwysedd, ac mae'n pwysleisio cyplysu a chydlyniad fel y priodoleddau dyfnach y mae'r acronymau'n ceisio eu gwasanaethu.

## Egwyddorion allweddol

- Rheolwch gyplysu a chydlyniad yn gyntaf; mae'r rhan fwyaf o egwyddorion enwedig yn ffyrdd anuniongyrchol o wella'r ddau briodoledd hyn.
- Optimeiddiwch ar gyfer newid: mae cynllunio da'n lleihau cost y newidiadau y bydd wir eu hangen arnoch eu gwneud.
- Ffafriwch y cynllun symlaf sy'n gweithio nawr, ond cadwch ffiniau lle mae newid yn debygol.
- Mae dyblygu'n rhatach na'r haniaeth anghywir; arhoswch nes bod y patrwm yn glir.
- Gwnewch ddibyniaethau'n benodol a'u pwyntio tuag at bethau sefydlog.
- Modelwch y parth yn iaith y parth; aliniwch ffiniau meddalwedd â ffiniau busnes.
- Dewiswch baradeimau i ffitio'r broblem, nid ideoleg; mae'r rhan fwyaf o systemau mawr yn gymysgedd pragmataidd.

## Argymhellion

### Defnyddiwch SOLID fel lens, nid rhestr wirio

Cymhwyswch gyfrifoldeb-unigol i gadw modiwlau'n gydlynol, gwrthdroad-dibyniaeth i bwyntio dibyniaethau at haniaethau lle mae ffin yn wirioneddol bodoli, ac agored-caeedig lle mae pwyntiau ymestyn yn real. Peidiwch â chynhyrchu rhyngwynebau, ffatrïoedd, a haenau dim ond i fodloni'r acronym pan nad oes ond un gweithrediad ac nid oes un arall yn y golwg. Mae gan anuniongyrchedd gost, ac rydych yn ei thalu ar bob darlleniad.

### Cymhwyswch DRY i wybodaeth, nid i destun

Mae DRY yn ymwneud â pheidio â dyblygu un darn awdurdodol o *wybodaeth*. Nid yw'n ymwneud â dileu llinellau sydd ond yn edrych yn debyg. Dylai dau ddarn o god sy'n edrych yn debyg ond sy'n newid am resymau gwahanol aros ar wahân. Ffafriwch ychydig o ddyblygu dros haniaeth a rennir yn gynamserol sy'n cyplysu pethau anghysylltiedig. Tynnwch yr haniaeth allan unwaith y bydd y patrwm gwirioneddol wedi ymddangos ddwywaith neu deirgwaith.

### Gadewch i KISS a YAGNI wrthsefyll dyfalu

Adeiladwch ar gyfer y gofynion sydd gennych, nid y rhai rydych yn eu dychmygu. Osgowch gyffredinolrwydd dyfaledig, fel fframweithiau y gellir eu ffurfweddu, systemau ategyn, a phwyntiau ymestyn nad oes neb wedi gofyn amdanynt. Y gwrthbwysau yw bod rhywfaint o hyblygrwydd yn wirioneddol yn rhatach i'w adeiladu i mewn yn gynnar, fel rhyngwyneb sefydlog neu wnïad glân. Mae YAGNI yn dadlau yn erbyn *gweithrediad* dyfaledig, nid yn erbyn ffiniau ystyriol.

### Cynlluniwch ar gyfer cyplysu isel a chydlyniad uchel yn benodol

Gwnewch i bob modiwl wneud un peth wedi'i ddiffinio'n dda (cydlyniad), a dibynnu ar cyn lleied o fodiwlau eraill â phosibl, drwy ryngwynebau cul (cyplysu isel). Wrth adolygu cynllun, gofynnwch pa newidiadau sy'n tonni ar draws ffiniau modiwlau. Y tonnau hynny yw'r mesur gwirioneddol o gyplysu. Yr un syniad wedi'i gymhwyso i haenau a phryderon traws-doriadol yw gwahanu pryderon.

### Defnyddiwch batrymau cynllunio fel geirfa, cymhwyswch wrth-batrymau fel rhybuddion

Mae patrymau'n enwau a rennir defnyddiol ar gyfer datrysiadau cylchol. Trowch at un pan fydd y broblem yn wirioneddol yn cyfateb iddo. Peidiwch â gorfodi patrymau i edrych yn soffistigedig, oherwydd mae cod trwm ar batrymau'n aml yn arwydd o oreirianeg. Dysgwch yr [wrth-batrymau](https://en.wikipedia.org/wiki/Anti-pattern) cyffredin (gwrthrychau duw, modelau diwaed lle mae'n amhriodol, peli mawr o fwd, monolithau dosbarthedig) fel labeli diagnostig.

### Mabwysiadwch Gynllunio wedi'i Yrru gan Barth lle mae'r parth yn gymhleth

Ar gyfer systemau â rheolau busnes cyfoethog, defnyddiwch offer tactegol a strategol DDD: iaith hollbresennol a rennir ag arbenigwyr parth, cyd-destunau ffiniedig sy'n cerfio'r system yn ddarnau wedi'u modelu'n annibynnol, a mapiau cyd-destun sy'n disgrifio sut mae'r darnau hynny'n perthyn. Mae cyd-destunau ffiniedig yn arbennig o werthfawr ar raddfa fenter, oherwydd maent yn alinio perchnogaeth tîm â ffiniau model. Mae DDD yn ormod ar gyfer systemau [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) (creu, darllen, diweddaru, dileu) syml.

### Dewiswch baradeimau yn ôl ffit

Defnyddiwch gyfeiriadedd gwrthrych ar gyfer amgapsiwleiddio ymddygiad â chyflwr a modelu parthau. Defnyddiwch arddull weithredol ar gyfer trawsffurfiadau, cydamseroldeb, a rhagweladwyedd trwy [anghyfnewidioldeb](https://en.wikipedia.org/wiki/Immutable_object). Defnyddiwch gynllunio data-ganolog lle mae perfformiad ac ymddygiad storfa gudd yn dominyddu. Mae systemau mawr yn cymysgu'r tri. Gwnewch y dewis fesul cydran, a chadwch y ffiniau rhwng arddulliau'n lân.

## Cyfaddawdau: manteision ac anfanteision

| Egwyddor / dull | Wedi'i gymhwyso'n dda | Modd methiant |
|---|---|---|
| SOLID | Gwniadau clir lle mae newid yn digwydd; unedau profadwy | Amlder rhyngwynebau a haenau; anuniongyrchedd heb wobr |
| DRY | Ffynhonnell wirionedd sengl ar gyfer gwybodaeth wirioneddol | Haniaeth anghywir yn cyplysu cod anghysylltiedig |
| KISS / YAGNI | Systemau tenau, dealladwy | Gwniadau heb eu cynllunio'n ddigonol; ôl-ffitiadau drud o hyblygrwydd sydd ei angen |
| Patrymau cynllunio | Geirfa a rennir; strwythurau profedig | Cwlt-cargo patrymau; cymhlethdod damweiniol |
| Cynllunio wedi'i Yrru gan Barth | Modelau a thimau wedi'u halinio; cymhlethdod wedi'i ddofi | Seremoni drwm ar barthau syml; ffiniau cyd-destun anghywir eu lleoliad |
| Gweithredol / anghyfnewidiol | Rhagweladwyedd; cydamseroldeb mwy diogel | Ffit lletchwith ar gyfer problemau sydd â chyflwr yn gynhenid; syrpreisys perfformiad |

Y tyndra cylchol yw rhwng tan-gynllunio a gor-gynllunio. Mae systemau tan-gynlluniedig yn cronni cyplysu ac yn mynd yn anhyblyg. Mae systemau gor-gynlluniedig yn boddi mewn haniaeth y mae'n rhaid i rywun ei ddeall a'i chynnal. Nid pwynt sefydlog yw'r ateb. Disgyblaeth ydyw: gohirio penderfyniadau hyd nes bod gennych ddigon o wybodaeth, tra'n cadw'r gwniadau sy'n gadael i chi newid eich meddwl.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Beth yw eich trothwy pendant ar gyfer tynnu allan haniaeth a rennir, a sut ydych yn atal DRY rhag cynhyrchu'r un anghywir?** Mae'r bennod hon yn blaen bod dyblygu'n rhatach na'r haniaeth anghywir, ac y dylech aros nes bod y patrwm wedi ymddangos ddwywaith neu deirgwaith cyn ei dynnu allan. Ar dîm mawr, y perygl yw bod rhywun yn ffactora dau ddarn tebyg yr olwg yn fodiwl a rennir ar draws ffiniau timau, ac wedyn mae pob newid dyfodol i un galwr yn tonni i mewn i'r llall. Y signal i'w ddwyn yw a yw'r dyblygion yn newid am yr un rheswm neu ddim ond yn edrych yn debyg ar hyn o bryd. Cytunwch ar reol tri, a mynnwch fod haniaeth ymgeisiol wedi newid gyda'i gilydd mewn gwirionedd cyn i chi gyplysu'r galwyr. Mae'r cytundeb sengl hwnnw'n atal dosbarth o gyplysu sy'n ddrud i'w ddatod unwaith y bydd llawer o dimau'n dibynnu arno.

2. **Sut ydych chi'n gwneud cyplysu a chydlyniad yn weladwy mewn adolygiad cynllunio yn lle eu gadael i deimlad perfeddol?** Mae'r egwyddorion allweddol yn rhoi cyplysu a chydlyniad uwchlaw pob acronym, ac yn diffinio cyplysu fel y newidiadau sy'n tonni ar draws ffiniau modiwlau. Nid yw greddf yn graddio ar draws cannoedd o beirianwyr sydd bob un ond yn gweld eu cornel eu hunain o'r system. Dewch â thystiolaeth y gall peiriant ei chynhyrchu: graffiau dibyniaeth, a data cyd-newid sy'n dangos pa fodiwlau sy'n cael eu golygu gyda'i gilydd yn barhaus yn yr un ymrwymiadau. Ychwanegwch gwestiwn adolygu penodol sy'n gofyn pa ffiniau modiwl y mae newid yn eich gorfodi i'w croesi. Pan fydd dau fodiwl bob amser yn newid gyda'i gilydd, dyna'ch ciw naill ai i'w cyfuno neu i drwsio'r ffin rhyngddynt.

3. **Ble mae'r llinell yn eich systemau rhwng parth cyfoethog digon i gyfiawnhau Cynllunio wedi'i Yrru gan Barth ac ap CRUD plaen lle mae'n ormod?** Mae'r bennod yn argymell cyd-destunau ffiniedig DDD yn union oherwydd eu bod yn alinio perchnogaeth tîm â ffiniau model, ac yn rhybuddio bod DDD yn ormod ar gyfer systemau creu-darllen-diweddaru-dileu syml ac yn dirywio'n seremoni heb fodelu gwirioneddol. Mae cael hyn yn anghywir mewn unrhyw gyfeiriad yn ddrud: mae DDD trwm ar barth tenau'n claddu ap syml mewn seremoni, tra bod model a rennir, gwasgaredig ar draws llawer o dimau'n gorfodi cydgysylltu traws-dîm cyson. Dewch â'r signalau sydd wir yn penderfynu: dwysedd rheolau busnes, a faint o dimau sydd angen bod yn berchen ar ddarnau'n annibynnol. Cadwch y peirianwaith strategol ar gyfer y craidd cymhleth, a gadewch i'r ymylon syml aros yn syml. Mae hynny'n eich cadw'n glir o theatr DDD a phêl fawr o fwd fel ei gilydd.

4. **Pryd mae haniaeth, rhyngwyneb, neu batrwm cynllunio'n werth yr anuniongyrchedd y mae'n ei ychwanegu, a phwy sydd â'r awdurdod i alw cynllun yn oreiriennig?** Mae'r bennod hon yn benodol bod gan anuniongyrchedd gost rydych yn ei thalu ar bob darlleniad, a bod cynhyrchu rhyngwynebau, ffatrïoedd, a haenau i fodloni SOLID neu i edrych yn soffistigedig yn fodd methiant. Ar dîm mawr mae'r pwysau'n rhedeg y ffordd arall: mae adolygwyr yn caniatáu haniaeth ychwanegol drwodd oherwydd ei bod yn edrych yn ddisgybledig, ac nid oes neb eisiau bod y person sy'n dadlau dros lai o strwythur. Mae'r ystyriaeth gystadleuol yn real, oherwydd mae rhai gwniadau'n wirioneddol ennill eu cadw ac mae eu tynnu'n ddiweddarach yn ddrud. Dewch â thystiolaeth bendant i'r drafodaeth: sawl gweithrediad sydd gan ryngwyneb mewn gwirionedd heddiw, pa mor aml y mae'r pwynt ymestyn wedi ystwytho erioed, a sawl ffeil y mae'n rhaid i ddarllenydd eu hagor i ddilyn un llwybr cod. Cytunwch fod un gweithrediad heb un arall yn y golwg yn rheswm rhagosodedig i'w mewnlinellu, ac enwch pwy all labelu cynllun yn oreiriennig heb i hynny ddarllen fel sarhad. Mewn systemau menter a llywodraeth sy'n goroesi eu hawduron am ddegawd, mae anuniongyrchedd diangen yn dreth y mae pob cynhaliwr yn y dyfodol yn ei thalu, felly triniwch "beth mae'r haniaeth hon yn ei brynu i ni" fel cwestiwn adolygu sefydlog, nid her bersonol.

5. **Sut ydych chi'n penderfynu pa baradeim y mae pob cydran yn ei ddefnyddio, gwrthrych-gyfeiriedig, gweithredol, neu ddata-ganolog, a sut ydych chi'n cadw'r ffiniau rhyngddynt yn lân?** Mae'r bennod yn dadlau bod systemau mawr yn gymysgedd pragmataidd ac y dylech ddewis fesul cydran yn ôl ffit, gan ddefnyddio cyfeiriadedd gwrthrych ar gyfer parthau â chyflwr, arddull weithredol ar gyfer trawsffurfiadau a chydamseroldeb, a chynllunio data-ganolog lle mae perfformiad ac ymddygiad storfa gudd yn dominyddu. Heb ei reoli, mae dewis paradeim yn dod yn fater o bwy bynnag a ysgrifennodd y modiwl gyntaf, ac mae cyflwr newidiol yn gollwng i mewn i'r hyn a ddylai fod yn drawsffurfiadau pur, neu mae purdeb gweithredol yn ymladd problem sydd â chyflwr yn gynhenid. Y dystiolaeth sy'n werth ei dwyn yw ble mae eich poen gwirioneddol: pa gydrannau sy'n anodd eu profi oherwydd cyflwr cudd, pa lwybrau poeth sydd wedi'u cyfyngu gan storfa gudd, a ble mae'r arddull gyfredol yn gorfodi gweithdrefnau amgen lletchwith. Penderfynwch y paradeim rhagosodedig ar gyfer pob haen yn fwriadol ac ysgrifennwch i lawr ble mae'r gwniadau rhwng arddulliau'n disgyn, fel nad yw craidd gweithredol ac ymyl orchmynnol yn gwaedu i mewn i'w gilydd. Ar gyfer system reoledig neu lywodraeth lle mae'n rhaid i gyfrifiad fod yn archwiliadwy ac yn atgynhyrchadwy ar gyfer cyfnod penodol, mae craidd gweithredol, anghyfnewidiol yn aml yn ofyniad cydymffurfiaeth yn hytrach na blas, a dylai'r cyfyngiad hwnnw yrru'r ffin yn hytrach na'i ddilyn.

6. **Sut ydych chi'n atal yr egwyddorion hyn rhag caledu'n ddogma, a ble ydych chi'n cofnodi'r rhesymeg y tu ôl i benderfyniad cynllunio fel y gall tîm yn y dyfodol ei ailymweld?** Mae gan bob egwyddor yn y bennod hon faes cymhwysedd a modd methiant, ac mae'r fframio cyfan yn eu trin fel offer i'w cymhwyso â barn yn hytrach na chyfreithiau i'w gorfodi. Ar dîm mawr mae egwyddor yn dawel yn dod yn rheol: mae DRY yn gwahardd unrhyw ddyblygu, mae SOLID yn mynnu rhyngwyneb fesul dosbarth, a chaiff eithriadau pragmataidd eu blocio mewn adolygiad gan bobl sy'n dyfynnu'r acronym yn hytrach na'r canlyniad. Y tyndra yw bod rhywfaint o gysondeb yn wirioneddol yn helpu cannoedd o beirianwyr i gydgysylltu, felly ni allwch ddim ond datgan bod pob egwyddor yn ddewisol. Dewch ag enghreifftiau lle mae dilyn egwyddor i'r llythyren wedi cynhyrchu cynllun gwaeth, a dewch â'r cofnodion penderfyniad, os oes rhai, sy'n esbonio pam mae ffin neu haniaeth benodol yn bodoli. Cytunwch fod egwyddorion yn ragosodiadau y gall peiriannydd wyro oddi wrthynt gyda rheswm wedi'i gofnodi, a chapiwch ddewisiadau cynllunio o ganlyniad mewn cofnod penderfyniad pensaernïaeth byr fel bod y tîm nesaf yn etifeddu'r rhesymeg ac nid dim ond y cod. Mewn systemau menter a sector cyhoeddus, lle mae'r awduron gwreiddiol wedi hen fynd ac archwiliadau'n gofyn pam mae'r system wedi'i llunio fel y mae, mae'r trywydd ysgrifenedig hwnnw'n wahaniaeth rhwng cynllun y gall timau'r dyfodol ei newid yn ddiogel ac un y maent ofn ei gyffwrdd.

## Trwy lens sector

**Cwmni newydd.** Ffafriwch y cynllun symlaf sy'n cyflenwi a chadwch un modiwl wedi'i ffactora'n dda hyd nes bod ail achos defnydd gwirioneddol yn gorfodi gwniad. Eich adnodd prinnaf yw sylw peirianneg, felly mae rhyngwynebau cynamserol, haenau, a fframweithiau dyfaledig yn gost bur. Dilynwch y rheol tri cyn tynnu allan unrhyw haniaeth a rennir, a gadewch i YAGNI ladd y pwyntiau ymestyn nad oes neb wedi gofyn amdanynt eto.

**Busnes bach.** Heb bensaer pwrpasol a chyllideb dynn, dibynnwch ar y cynllun sydd eisoes wedi'i bobi i mewn i'r fframweithiau a'r llyfrgelloedd rydych yn eu prynu yn hytrach na dyfeisio'ch patrymau eich hun. Cadwch ymdrech cynllunio pwrpasol ar gyfer y llond llaw o reolau sy'n wirioneddol yn eich busnes chi, a chadwch bopeth arall yn confensiynol fel y gall contractwr neu recriwt newydd ei ddarllen. Mae ychydig o ddyblygu rydych yn ei ddeall yn well na haniaeth glyfar dim ond ei hawdur sy'n gallu ei chynnal.

**Menter.** Cydgysylltu ar draws llawer o dimau yw gwobr egwyddorion a rennir: geirfa gyffredin ar gyfer adolygu cynllunio, a chyd-destunau ffiniedig sy'n alinio ffiniau model â pherchnogaeth tîm fel bod grwpiau'n esblygu'n annibynnol. Rheolwch gyplysu a chydlyniad yn benodol â data dibyniaeth a chyd-newid, a chofnodwch benderfyniadau cynllunio o ganlyniad fel bod systemau'n aros yn newidiadwy ymhell ar ôl i'w hawduron symud ymlaen. Gwarchodwch yn gyfartal yn erbyn yr haniaeth anghywir sy'n cyplysu timau a'r oreirianeg sy'n trethu pob darllenydd.

**Llywodraeth.** Mae archwiliadwyedd ac atgynhyrchadwyedd yn aml yn pennu'r cynllun. Mae craidd anghyfnewidiol, gweithredol yn gadael i chi atgynhyrchu cyfrifiad hanesyddol yn union ar gyfer cyfnod penodol, rhywbeth na all graff gwrthrych dryslyd gyda chyflwr newidiol cudd ei warantu. Ffafriwch gontractau cyhoeddedig penodol dros dablau a rennir ar ffiniau cyd-destun, a chadwch y cynllun a'i gofnodion penderfyniad yn ddarllenadwy i archwilwyr ac i ba bynnag dîm sy'n etifeddu'r system ddegawd yn ddiweddarach.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd tri pheiriannydd sy'n adeiladu ei gynnyrch cyntaf yn gwrthsefyll yr ysfa i hollti pob nodwedd yn haenau o ryngwynebau a ffatrïoedd, gan gadw un modiwl wedi'i ffactora'n dda hyd nes bod ail achos defnydd gwirioneddol yn ymddangos. Pan fydd yr un rhesymeg yn ymddangos y trydydd tro ar draws llifau cofrestru a bilio, maent yn tynnu allan un ffwythiant bach a rennir yn hytrach na fframwaith dyfaledig. Mae hyn yn cadw'r sylfaen god yn ddigon bach y gall unrhyw un ohonynt ei ddal yn ei ben, ac mae'r ychydig wniadau y maent yn eu tynnu'n disgyn lle mae'r cynnyrch yn fwyaf tebygol o newid.

**Menter.** Mae platfform yswiriant mawr yn modelu polisi, hawliadau, a bilio fel cyd-destunau ffiniedig ar wahân, pob un yn eiddo i dîm pwrpasol gyda'i fodel data a ffin gwasanaeth ei hun. Lle mae'r cyd-destunau'n cyfarfod, fel pan fydd hawliad yn cyfeirio at bolisi, maent yn siarad trwy gontractau cyhoeddedig penodol yn hytrach na thablau cronfa ddata a rennir. Mae hyn yn gadael i'r tri thîm esblygu'n annibynnol, ac mae'r iaith hollbresennol yn cadw sgyrsiau ag ysgrifenwyr risg ac actwarïaid yn fanwl gywir. Roedd fersiwn cynharach wedi rhannu un model gwasgaredig sengl, a gofynnai pob newid am gydgysylltu traws-dîm.

**Llywodraeth.** Mae system brosesu treth genedlaethol yn ffafrio craidd data-ganolog, gweithredol yn fwriadol ar gyfer ei pheiriant cyfrifo. Mynegir rheolau treth fel trawsffurfiadau pur dros gofnodion mewnbwn anghyfnewidiol, sy'n eu gwneud yn archwiliadwy, yn brofadwy, ac yn atgynhyrchadwy ar gyfer blwyddyn dreth benodol. Cedwir y rhannau gorchmynnol, â chyflwr (llif gwaith, hysbysiadau) ar yr ymylon. Gall archwilwyr bwyntio at fersiwn rheol benodol ac atgynhyrchu unrhyw gyfrifiad hanesyddol yn union, sy'n ofyniad cyfreithiol na allai graff gwrthrych dryslyd gyda chyflwr newidiol cudd ei warantu.

## Achos busnes: cymhellion, ROI, a TCO

Mae ansawdd cynllunio'n fuddsoddiad yn *newidiadwyedd* system, ac mae newidiadwyedd yn dominyddu cyfanswm cost perchnogaeth. Mae'r rhan fwyaf o gost system yn glanio ar ôl ei rhyddhad cyntaf, mewn addasu ac ymestyn. Mae systemau wedi'u cynllunio'n dda'n cadw cost newid yn fras wastad dros amser. Mae rhai wedi'u cynllunio'n wael yn gweld cost pob newid yn dringo hyd nes bod y system yn dod yn effeithiol anaddasadwy ac yn gorfod cael ei hailysgrifennu, y canlyniad mwyaf costus o bob un.

Sgil a disgyblaeth adolygu, gan mwyaf, yw cost mabwysiadu: dysgu'r egwyddorion, a threulio amser cynllunio ymlaen llaw. Cronni araf [dyled dechnegol](https://en.wikipedia.org/wiki/Technical_debt), cyflymder cyflenwi'n gostwng, cyfraddau diffygion yn codi, ac ailysgrifennu drud yn y pen draw yw cost peidio â'u mabwysiadu. I wneud yr achos i arweinyddiaeth, cysylltwch ddisgyblaeth cynllunio â rhagweladwyedd cyflenwi ac osgoi rhaglenni ailysgrifennu, ac olrheiniwch ddangosyddion arweiniol fel cyfradd methiant newid a'r amser i weithredu nodweddion cymaradwy dros amser. Gwyliwch am y methiant gwrthgyferbyniol hefyd: mae gorfuddsoddi mewn cynllunio ar gyfer dyfodolau ansicr hefyd yn dinistrio gwerth. Felly'r ddadl yw dros gynllunio *priodol*, wedi'i galibro i ba mor debygol a chostus yw newid yn y dyfodol.

## Gwrth-batrymau a pheryglon

- **Cyffredinolrwydd dyfaledig:** adeiladu ehangadwyedd ar gyfer gofynion dychmygol nad ydynt byth yn cyrraedd.
- **Yr haniaeth anghywir:** gorfodi cod anghysylltiedig gyda'i gilydd i fodloni DRY, gan greu cyplysu sy'n waeth na dyblygu.
- **Cwlt-cargo patrymau:** cymhwyso patrymau cynllunio er eu mwyn eu hunain, gan ychwanegu anuniongyrchedd heb fudd.
- **Gwrthrychau diwaed neu wrthrychau duw:** modelau heb ymddygiad, neu wrthrychau sy'n gwneud popeth; mae'r ddau'n arwyddo cyfrifoldebau anghywir eu lleoliad.
- **Monolith dosbarthedig:** gwasanaethau wedi'u hollti'n ffisegol ond yn dal wedi'u cyplysu'n dynn, gan gyfuno costau'r ddau ddull.
- **Pêl fawr o fwd:** dim strwythur amlwg; mae pob newid yn peryglu popeth.
- **Theatr DDD:** mabwysiadu'r eirfa a strwythur y ffolderi heb y modelu parth sy'n rhoi gwerth iddo.

## Model aeddfedrwydd

- **Lefel 1, Cychwyn:** Mae cynllunio'n ad hoc ac yn adweithiol; mae cyplysu'n cronni'n ddigyfyngiad; mae egwyddorion yn anhysbys neu'n cael eu galw fel sloganau, ac mae haniaethau'n ymddangos neu'n diflannu yn ôl arferiad unigol.
- **Lefel 2, Datblygu:** Mae timau'n gwybod yr egwyddorion ac yn eu cymhwyso, ond yn anghyson ac yn aml yn ddogmatig; mae rhai grwpiau'n rheoli cyplysu a chydlyniad yn fwriadol tra nad yw eraill, ac nid oes geirfa a rennir ar draws y sefydliad.
- **Lefel 3, Safoni:** Mae geirfa gynllunio a rennir, rheol tri ar gyfer tynnu haniaethau allan, dadansoddiad cyplysu a chydlyniad, a chyd-destunau ffiniedig wedi'u halinio â thimau wedi'u dogfennu a'u disgwyl ledled y sefydliad, wedi'u cymhwyso'n gyson mewn adolygiad cynllunio yn hytrach na'u gadael i chwaeth unigol.
- **Lefel 4, Rheoli:** Mae iechyd cynllunio'n cael ei fesur yn erbyn llinellau sylfaen: olrheinir data cyplysu a chyd-newid, cyfradd methiant newid, a'r amser i weithredu nodweddion cymaradwy dros amser, fel bod haniaethau a ffiniau'n cael eu hychwanegu, eu cadw, neu eu dileu ar sail tystiolaeth, a chaiff goreirianeg a'r haniaeth anghywir eu dal gan ddata yn hytrach na barn.
- **Lefel 5, Trefniannu:** Caiff disgyblaeth cynllunio ei hintegreiddio â chynllunio cyflenwi a risg ar draws y sefydliad; cymhwysir egwyddorion yn fanwl ac â moddau methiant hysbys; mae dewisiadau paradeim a ffin yn fwriadol ac yn cael eu hailymweld yn barhaus, ac mae'r sefydliad yn rheolaidd yn ailffactora, yn ailgwmpasu, ac yn ymddeol haniaethau wrth i'r parth a'r dystiolaeth symud.

## Syniadau i'w trafod

- Sut ydych chi'n gwahaniaethu rhwng gwniad angenrheidiol a chyffredinolrwydd dyfaledig cyn bod gennych y gofyniad yn y dyfodol?
- Pryd mae DRY wedi arwain eich tîm at yr haniaeth anghywir, a sut wnaethoch chi ei adnabod?
- Ble ddylai ffiniau cyd-destun-ffiniedig ddisgyn, a pha mor agos ddylent adlewyrchu siart y sefydliad?
- Faint o gynllunio ddylai ragflaenu cod yn eich cyd-destun chi, a sut ydych chi'n cofnodi'r penderfyniadau?
- Pa rannau o'ch system fyddai'n elwa o arddull fwy gweithredol neu ddata-ganolog?
- Sut ydych chi'n atal egwyddorion cynllunio rhag caledu'n ddogma sy'n gwrthsefyll eithriadau pragmataidd?

## Prif ganfyddiadau

- Cyplysu a chydlyniad yw'r priodoleddau sy'n bwysig; moddau i'r dibenion hynny yw'r acronymau.
- Mae gan bob egwyddor fodd methiant; gwybyddwch pryd mae pob un yn camarwain.
- Ffafriwch ychydig o ddyblygu dros haniaeth gynamserol neu anghywir.
- Defnyddiwch DDD a chyd-destunau ffiniedig i alinio parthau cymhleth â pherchnogaeth tîm.
- Dewiswch baradeimau yn ôl ffit; mae systemau mawr yn gymysgedd pragmataidd.
- Cynlluniwch ar gyfer y newidiadau y bydd eu gwir angen arnoch, gan osgoi tan-gynllunio a gor-gynllunio fel ei gilydd.

## Cyfeiriadau a darllen pellach

- Robert C. Martin, *Clean Architecture* and *Agile Software Development, Principles, Patterns, and Practices*
- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code* and *Patterns of Enterprise Application Architecture*
- David L. Parnas, *On the Criteria to Be Used in Decomposing Systems into Modules*
- Sandi Metz, *Practical Object-Oriented Design*
