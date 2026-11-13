# 10.10 Economeg peirianneg meddalwedd

## Trosolwg a chymhelliant

Economeg peirianneg meddalwedd yw'r ddisgyblaeth o wneud penderfyniadau peirianyddol yn nhermau gwerth a chost, o dan ansicrwydd, dros amser. Dyma'r rhesymu sy'n ateb y cwestiynau y mae arweinyddiaeth yn eu gofyn go iawn. A yw hyn yn werth ei adeiladu? Pa un o'r tri dewis hyn sy'n rhoi'r elw gorau? Faint fydd yn ei gostio i ni berchen ar y system hon am y degawd nesaf, nid dim ond i'w rhyddhau'r chwarter hwn? A ddylem dalu i lawr y [dyled dechnegol](https://en.wikipedia.org/wiki/Technical_debt) hwn nawr, neu ei ohirio a thalu'r llog? Mae pob map ffordd, caffael, buddsoddiad platfform, a rhaglen foderneiddio, yn y bôn, yn ddadl economaidd. Mae'r bennod hon yn enwi'r ddisgyblaeth sy'n gwneud y dadleuon hynny'n eglur, yn gymharadwy, ac yn amddiffynadwy.

I un tîm, gall rhesymu economaidd aros yn anffurfiol, oherwydd bod cost galwad anghywir yn fach ac yn cael ei chywiro'n gyflym. I fenter neu sefydliad llywodraeth, mae'r risg yn fawr, arian pobl eraill ydyw, a chraffir ar y penderfyniadau gan gyllid, archwilwyr, a'r cyhoedd. Bydd rhaglen sy'n edrych yn rhad am fod rhywun wedi cyfrif dim ond cost yr adeiladu, gan anwybyddu'r blynyddoedd o weithredu, trwyddedu, cymorth, a'r amnewid yn y pen draw, yn chwythu ei chyllideb gyda dibynadwyedd digalon. Ni ellir herio, cymharu, na dwyn i gyfrif gynnig sy'n addo elw ond byth yn nodi ei ragdybiaethau. Mae economeg peirianneg meddalwedd yn rhoi i chi iaith feintiol a rennir, fel bod cyfalaf prin yn llifo at y gwaith sy'n creu'r gwerth mwyaf.

Y bennod hon yw asgwrn cefn dadansoddol rhesymu [elw-ar-fuddsoddiad](https://en.wikipedia.org/wiki/Return_on_investment) (ROI) a [chost-perchnogaeth-cyfan](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO) a ddefnyddir drwy'r llawlyfr hwn i gyd. Mae rheoli portffolio a rhaglenni (pennod 10.1) yn penderfynu *beth* i'w ariannu; mae'r bennod hon yn cyflenwi'r dull economaidd ar gyfer *sut* i benderfynu. Mae'n cysylltu â chaffael (pennod 10.3), lle mae'r cyfrifiadau hyn yn cyfiawnhau dewisiadau prynu-yn-erbyn-adeiladu a chontract; â chost, FinOps (gweithrediadau ariannol, sef rheolaeth ddisgybledig o wariant cwmwl ac amser rhedeg), a meddalwedd werdd (pennod 9.4), sy'n troi economeg cost-rhedeg yn ymarfer gweithredol; â'r biblinell ddarganfod a chanlyniadau (pennod 11.1), lle ffurfir a phrofir rhagdybiaethau gwerth; â dyled dechnegol mewn penderfynu a llywodraethu (pennod 1.5); a chynnal a chadw meddalwedd (pennod 3.7), lle mae'r gynffon hir o gost perchnogaeth yn glanio go iawn.

## Egwyddorion allweddol

- **Mae gwerth a chost ill dau'n amcangyfrifon.** Trinwch bob rhif fel ystod gyda rhagdybiaethau, nid ffaith. Mae ansicrwydd gonest yn drech na manylder ffug.
- **Mae gan arian werth amser.** Mae doler heddiw'n werth mwy na doler y flwyddyn nesaf; disgowntiwch lifoedd arian y dyfodol cyn cymharu dewisiadau.
- **Penderfynwch yn ôl cost perchnogaeth gyfan, nid pris prynu.** Y blaendal yw'r adeiladu; y morgais yw gweithredu, cymorth, a chynnal.
- **Dim ond costau a buddion y dyfodol sy'n bwysig i benderfyniad.** Mae [costau suddedig](https://en.wikipedia.org/wiki/Sunk_cost) wedi mynd; anwybyddwch nhw wrth ddewis beth i'w wneud nesaf.
- **Mae gan bob dewis [gost cyfle](https://en.wikipedia.org/wiki/Opportunity_cost).** Y gymhariaeth berthnasol yw bob amser y defnydd amgen gorau o'r un arian, pobl, ac amser.
- **Mae gan oedi bris.** Mae [cost oedi](https://en.wikipedia.org/wiki/Cost_of_delay), y gwerth a gollir tra bo penderfyniad neu draddodiad yn aros, yn aml y rhif mwyaf a'r un a anwybyddir fwyaf yn y model.
- **Gwnewch yr achos busnes yn ffugadwy.** Nodwch y rhagdybiaethau mor glir fel y gall realiti brofi'n ddiweddarach a ydynt yn gywir neu'n anghywir.

## Argymhellion

### Seilio penderfyniadau ar sylfeini economaidd

Adeiladwch eirfa a rennir cyn i chi adeiladu taenlenni. Gwahaniaethwch *werth* (y budd y mae rhanddeiliad yn ei ennill) oddi wrth *gost* (yr hyn a ddefnyddir i'w gynhyrchu), a mynegwch y ddau fel *llifoedd arian*, arian yn symud i mewn neu allan ar adegau penodol. Am fod taliad y flwyddyn nesaf yn werth llai nag un heddiw, cymhwyswch *[werth amser arian](https://en.wikipedia.org/wiki/Time_value_of_money)*: disgowntiwch lifoedd arian y dyfodol i werth presennol gan ddefnyddio cyfradd ddisgowntio sy'n adlewyrchu eich [cost cyfalaf](https://en.wikipedia.org/wiki/Cost_of_capital) neu gyfradd swyddogol. Cymhariaeth strwythuredig o ffrydiau llif arian dewisiadau cystadleuol dros orwel diffiniedig yw *cynnig* wedyn. Mynnwch fod pob cynnig sylweddol yn nodi ei orwel, ei gyfradd ddisgowntio, a'i ragdybiaethau ar un dudalen, fel bod adolygwyr yn dadlau am sylwedd yn hytrach na pheiriannu'r fathemateg yn ôl.

### Penderfynu'n benodol o dan ansicrwydd a risg

Gwneir penderfyniadau meddalwedd gyda gwybodaeth anghyflawn. Esgus fel arall yw'r camgymeriad. Modelwch ansicrwydd yn hytrach na'i guddio. Defnyddiwch amcangyfrifon tri phwynt (optimistig, tebygol, pesimistig) yn lle rhifau sengl, a chyfrifwch *[werth disgwyliedig](https://en.wikipedia.org/wiki/Expected_value)* trwy bwysoli canlyniadau yn ôl eu tebygolrwydd. Ar gyfer dewisiadau o ganlyniad, rhedwch [ddadansoddiad sensitifrwydd](https://en.wikipedia.org/wiki/Sensitivity_analysis): amrywiwch y ddau neu dri mewnbwn sy'n bwysicaf a gweld a yw'r argymhelliad yn troi. Gwahaniaethwch *risg* (ods meintiol) oddi wrth *ansicrwydd* dwfn (ods anhysbys), a ffafriwch ddewisiadau sy'n cadw hyblygrwydd pan fo ansicrwydd yn uchel. Mae ymrwymiad graddol sy'n eich galluogi i stopio, troi, neu ddyblu i lawr ar ôl dysgu yn aml yn werth mwy na bet rataf popeth-neu-ddim-byd.

### Paru'r dull penderfynu â chyd-destunau er-elw a chyhoeddus

Mae sefydliadau er-elw fel arfer yn optimeiddio elw ariannol, gan ddefnyddio [gwerth presennol net](https://en.wikipedia.org/wiki/Net_present_value) (NPV), ROI, ac adennill, yn erbyn cost cyfalaf. Mae cyrff dielw a'r sector cyhoeddus yn optimeiddio gwerth cenhadaeth, canlyniadau gwasanaeth, tegwch, a stiwardiaeth arian cyhoeddus, ac ni allant leihau pob budd i refeniw. Defnyddiwch yr un peirianwaith dadansoddol yn y ddau leoliad, ond dewiswch y ffwythiant amcan yn onest. Mewn llywodraeth, mynnir yn aml [ddadansoddiad cost-budd](https://en.wikipedia.org/wiki/Cost%E2%80%93benefit_analysis) a chost-effeithiolrwydd, cyfraddau disgowntio swyddogol, a chostio oes gyfan. Ariannwch yr hyn y gellir ei ariannu, ac ar gyfer y gweddill defnyddiwch feini prawf anariannol penodol, wedi'u dogfennu, yn hytrach na'u smyglo i mewn fel ffactorau twyllo. Yn y ddau fyd, yr un yw'r ddisgyblaeth: gwneud yr amcan a'r cyfaddawdau'n weladwy.

### Amcangyfrif cost gyda mwy nag un dull

Nid oes yr un dull amcangyfrif sengl yn hygred ar ei ben ei hun, felly triongli. Cyfunwch *gyfatebiaeth* (cymharu â gwaith blaenorol tebyg), *farn arbenigol* (mewnbwn strwythuredig gan beirianwyr profiadol, e.e. Delphi band-lled neu boker cynllunio), *ddadelfeniad* (torri gwaith i lawr a chodi amcangyfrifon i fyny, o'r gwaelod i fyny), a *modelau paramedrig* (wedi'u gyrru gan fformiwla, fel [COCOMO II](https://en.wikipedia.org/wiki/COCOMO), wedi'u calibro i'ch data). Lle bo gennych drwygyrch empirig, ffafriwch ddata llif hanesyddol dros feintioli dyfaliadol. Bob amser mynegwch amcangyfrifon fel ystodau gyda hyder, ailamcangyfrifwch wrth i chi ddysgu, a gwahanwch yr amcangyfrif o *ymdrech* oddi wrth yr ymrwymiad i *ddyddiad*. Cymysgu'r ddau hynny yw sut mae amcangyfrifon yn dod yn addewidion toredig.

### Cyfrifo TCO, ROI, NPV, ac adennill yn gyson

Mabwysiadwch becyn offer bach, safonol a'i gymhwyso'n unffurf, fel bod dewisiadau'n gymharadwy ar draws y portffolio. Mae *cost perchnogaeth gyfan* yn crynhoi pob cost ar draws yr oes gyfan: adeiladu, defnyddio, trwyddedu, gweithredu, cynnal, diogelu, ac ymddeol. Mae *ROI* yn mynegi budd net fel canran o gost. Mae *gwerth presennol net (NPV)* yn disgowntio pob llif arian yn y dyfodol i heddiw ac yn eu crynhoi; mae NPV positif yn golygu bod y dewis yn creu gwerth ar eich cyfradd ddisgowntio. Yr amser i adennill y traul cychwynnol yw *[cyfnod adennill](https://en.wikipedia.org/wiki/Payback_period)*. Mae'n syml a greddfol, ond yn ddall i bopeth ar ôl toriad-hafal ac i werth amser arian, felly defnyddiwch ef ochr yn ochr ag NPV yn unig. Safonwch y gorwel a'r gyfradd ddisgowntio ar draws dewisiadau a gymherir, neu mae'r gymhariaeth yn ddiystyr.

### Prisio dyled dechnegol a chost oedi

Gwnewch ddwy gost sy'n arferol anweledig yn benodol. Mae *dyled dechnegol* yn ymddwyn fel dyled ariannol: mae llwybrau byr yn benthyca cyflymder nawr ac yn codi llog yn ddiweddarach, fel traddodiad arafach, mwy o ddiffygion, a chost weithredu uwch. Amcangyfrifwch y llog, faint y mae'r ddyled yn ei drethu ar bob rhyddhad yn y dyfodol, fel bod y dewis o'i chodi neu ei thalu'n ôl yn dod yn benderfyniad economaidd yn hytrach nag un moesol (gweler penodau 1.5 a 3.7). Mae *cost oedi* yn werth a gollir am bob uned amser y mae peth gwerthfawr yn hwyr. Mae ei feintioli'n troi greddfau amwys "dylem frysio" yn flaenoriaethu go iawn, yn fwyaf uniongyrchol drwy ddilyniannu Swydd-Fyrraf-Bwysicaf-yn-Gyntaf wedi'i Bwysoli (Weighted-Shortest-Job-First). Mae timau sy'n prisio oedi'n stopio optimeiddio ar gyfer defnydd ac yn dechrau optimeiddio ar gyfer gwerth.

### Gwerthfawrogi anghyffyrddadwyau ac adeiladu'r achos busnes

Mae llawer o'r buddion mwyaf yn gwrthsefyll ffigwr doler glir: risg lai, ystum diogelwch gwell, cynhyrchedd datblygwyr, ymddiriedaeth brand, canlyniadau cenhadaeth, opsiynolrwydd. Mae esgus eu bod yn sero yn tueddu pob penderfyniad tuag at y gwrthrychol. Gwerthfawrogwch nhw beth bynnag. Ariannwch drwy ddirprwyon lle bônt hygred (cost toriad a osgowyd, oriau a arbedwyd wedi'u lluosi â chyfradd lwythog). Lle na allwch, sgoriwch nhw'n benodol yn erbyn meini prawf a enwir a'u cario ochr yn ochr â'r model ariannol. Cydosodwch y cyfan yn *achos busnes*: y broblem, y dewisiadau a ystyriwyd (gan gynnwys peidio-gwneud-dim), y costau a'r buddion dros y gorwel, y rhagdybiaethau a'r risgiau allweddol, yr argymhelliad, a'r mesurau y byddwch yn barnu'n ddiweddarach a weithiodd. Cadwch ef yn fyw, ac ailymwelwch ag ef yn erbyn y ffigyrau go iawn fel bod eich sefydliad yn dysgu amcangyfrif yn well.

## Cymhareb: manteision ac anfanteision

| Dull | Manteision | Anfanteision |
|---|---|---|
| Modelu meintiol manwl (NPV, TCO) | Trylwyr, cymharadwy, archwiliadwy; yn gorfodi rhagdybiaethau i'r amlwg | Yn cymryd amser; manylder ffug os yw'r mewnbynnau'n wan; gall eithrio'r hyn na fesurir |
| Hewristigau ysgafn (adennill, cost oedi) | Cyflym, greddfol, hawdd ei gyfathrebu | Yn anwybyddu gwerth amser neu gostau cynffon hir; garw ar gyfer ymrwymiadau mawr |
| Amcangyfrifon rhif sengl | Syml, pendant, hawdd cynllunio o'u cwmpas | Yn cuddio ansicrwydd; yn dod yn addewidion ffug; yn cosbi gonestrwydd |
| Ystodau a gwerth disgwyliedig | Gonest am risg; yn cefnogi penderfyniadau graddol | Anos ei gyfathrebu; gall deimlo'n osgoi i randdeiliaid sy'n dymuno un rhif |
| Ariannu anghyffyrddadwyau drwy ddirprwyon | Yn cadw buddion mawr yn y model; yn galluogi cyfaddawdau | Mae dirprwyon yn ddadleuol; risg o gynhyrchu rhifau cyfleus |
| Dadansoddiad TCO oes-gyfan llawn | Yn atal synnau adeiladu-rhad-rhedeg-drud | Angen data cost rhedeg nad oes gan lawer o dimau'n gynnar |

Y tyndra sy'n dychwelyd yw rhwng trylwyredd a chyflymder. Mae modelu ariannol trwm yn gwella penderfyniadau mawr, anwrthdroadwy, drud, ond mae'n cael ei wastraffu, hyd yn oed yn niweidiol, ar rai bach, gwrthdroadwy, lle nad yw ond yn golchi ateb rhagbenderfynedig gydag awdurdod taenlen. Mae sefydliadau aeddfed yn maintio'r dadansoddiad yn briodol i'r risg: dadl cost-oedi un dudalen ar gyfer nodwedd arferol, achos busnes NPV-a-TCO llawn ar gyfer platfform neu gaffael aml-flwyddyn. Yr ail dyndra yw rhwng manylder a gonestrwydd. Mae rhif sengl hyderus yn haws gweithredu arno ond yn aml yn anghywir. Mae ystod yn wirioneddol ond yn anos ymrwymo iddi. Y datrysiad yw penderfynu gydag ystodau a gwerth disgwyliedig, yna ymrwymo i gynyddrannau graddol, fel eich bod yn cadw'r opsiwn i gywiro cwrs wrth i dystiolaeth gyrraedd.

## Cwestiynau i'w trafod gyda'ch tîm

1. **A ydym yn gwahanu'r amcangyfrif ymdrech oddi wrth yr ymrwymiad dyddiad, ac a ydym yn triongli amcangyfrifon yn hytrach nag ymddiried mewn un rhif?** Mae rhif sengl hyderus yn hawdd cynllunio o'i gwmpas ac yn aml yn anghywir, a'r eiliad y mae amcangyfrif ymdrech seiliedig ar ystod yn caledu'n ddyddiad sefydlog, cosbir gonestrwydd a daw'r amcangyfrif yn addewid toredig. Trionglwch: cyfunwch gyfatebiaeth, barn arbenigol, dadelfeniad, a thrwygyrch hanesyddol, a ffafriwch ddata llif go iawn dros feintioli dyfaliadol. Mynegwch amcangyfrifon fel ystodau gyda hyder, ac ailamcangyfrifwch wrth i chi ddysgu. I raglen fawr o dan graffu cyllid ac archwilio, dyma'r gwahaniaeth rhwng rhagolwg amddiffynadwy a rhif na all neb ei herio. Dewch ag amcangyfrif diweddar a lithrodd a gofynnwch a oedd yn amcangyfrif ymdrech a reolwyd i galendr.

2. **A ydym yn prisio cost oedi a'i defnyddio i ddilyniannu gwaith, neu'n dal i optimeiddio ar gyfer defnydd?** Mae cost oedi, y gwerth a gollir am bob uned amser y mae peth gwerthfawr yn hwyr, yn aml y rhif mwyaf a'r un a anwybyddir fwyaf yn y model. Mae timau nad ydynt byth yn ei brisio'n optimeiddio ar gyfer cadw pawb yn brysur, sy'n newynu'r gwaith gwerth-uchaf yn dawel. Meintiolwch hi a dilyniannwch gyda Swydd-Fyrraf-Bwysicaf-yn-Gyntaf wedi'i Bwysoli fel bod y gwaith sy'n colli'r gwerth mwyaf wrth aros yn mynd yn gyntaf. Mae hyn yn ad-drefnu mapiau ffordd ac yn ail-fframio "dylem frysio" fel blaenoriaethu go iawn. Dewch â dau neu dri menter ar y gweill ac amcangyfrifwch beth mae pob un yn ei gostio fesul wythnos o oedi; os na allwch, dyna'r bwlch i'w gau.

3. **A yw ein hachosion busnes yn penderfynu ar TCO oes-gyfan yn erbyn llinell sylfaen peidio-gwneud-dim, ac a yw'r trylwyredd wedi'i faintio i'r risg?** Blaendal yw adeiladu; morgais yw gweithredu, trwyddedu, cymorth, ac amnewid yn y pen draw, a bydd rhaglen sy'n cyfrif dim ond cost adeiladu'n chwythu ei chyllideb gyda dibynadwyedd digalon. Dylai pob cynnig difrifol gymharu dewisiadau (gan gynnwys peidio-gwneud-dim) dros orwel safonol ar gyfradd ddisgowntio a rennir, a nodi ei ragdybiaethau ar un dudalen fel bod adolygwyr yn dadlau sylwedd yn hytrach na rhifyddeg. Maintiwch yr ymdrech yn briodol: dadl cost-oedi un dudalen ar gyfer nodwedd arferol, achos NPV-a-TCO llawn ar gyfer platfform neu gaffael aml-flwyddyn. Mae modelu trwm o benderfyniad bach, gwrthdroadwy yn golchi ateb rhagbenderfynedig gydag awdurdod taenlen yn unig. Dewch â phenderfyniad diweddar a gofynnwch a oedd cost rhedeg, nid pris label, wedi ei yrru.

4. **Pa gyfradd ddisgowntio a ddefnyddiwn i gymharu dewisiadau dros amser, ac a ydym wedi profi a yw'r argymhelliad yn goroesi cyfradd wahanol?** Mae gwerth amser arian yn golygu nad yw doler ym mlwyddyn pump yn ddoler heddiw, ac eto mae llawer o gynigion naill ai'n hepgor disgowntio'n gyfan gwbl neu'n claddu cyfradd na chytunodd neb arni. Safonwch un gyfradd ac un gorwel ar draws dewisiadau a gymherir, neu mae'r gymhariaeth yn rhifyddeg wedi'i gwisgo fel mewnwelediad. Yr ystyriaeth gystadleuol yw bod y gyfradd ei hun yn ddadleuol: rhy isel a byddwch yn gwenieithio megaprosiectau hirdymor, rhy uchel a byddwch yn newynu buddsoddiadau sy'n talu'n ôl yn araf. Dewch â'r gyfradd a ddefnyddiwyd gennych, o ble y daeth (eich cost cyfalaf, neu gyfradd swyddogol a gyhoeddwyd), a dadansoddiad sensitifrwydd sy'n dangos ar ba gyfradd mae'r argymhelliad yn troi. I gyllid menter ac yn arbennig llywodraeth, mae'r gyfradd yn aml yn orfodol, er enghraifft cyfradd brisio swyddogol, ac mae cyfradd heb ei dogfennu neu anghyson yn union yr hyn y bydd archwiliwr yn ei herio gyntaf.

5. **Pan fo menter yn tanberfformio, a ydym yn penderfynu ar sail gwerth disgwyliedig y dyfodol ac yn anwybyddu'r hyn a wariwyd eisoes, ac a ydym wedi strwythuro ariannu fel y gallwn ei stopio mewn gwirionedd?** Mae costau suddedig wedi mynd, ond maent yn arfer tyniad pwerus: mae timau'n amddiffyn ymdrechion sy'n methu yn ôl yr arian a dywalltwyd eisoes yn hytrach na'r gwerth sydd o hyd o'u blaenau. Mae'r pwysau cystadleuol yn real, oherwydd bod stopio'n edrych fel cyfaddef gwastraff ac yn cario cost wleidyddol, felly rhaid adeiladu'r ddisgyblaeth i mewn i sut y byddwch yn ariannu yn hytrach na'i gadael i sut mae unrhyw un yn teimlo yn y foment. Ffafriwch ymrwymiadau graddol sy'n werthfawr yn annibynnol ac sy'n eich galluogi i stopio, troi, neu ddyblu i lawr ar ôl pob cynyddrant, yn lle un bet anwrthdroadwy. Dewch ag ymdrech ar y gweill sydd ar ei hôl hi, y gost sy'n weddill i'w gorffen wedi'i osod yn erbyn y budd disgwyliedig sy'n weddill, a'r pwynt lle mae'r giât ariannu nesaf yn disgyn. Mewn portffolio menter neu lywodraeth, enwch pwy sy'n dal awdurdod i atal rhaglen ac a yw'r strwythur ariannu'n rhoi pwynt penderfynu go iawn iddynt, oherwydd mae ymrwymiad heb giât yn ymrwymiad na all neb ei stopio.

6. **A ydym yn onest am ein ffwythiant amcan, ac a ydym yn gwerthfawrogi anghyffyrddadwyau'n benodol yn hytrach na'u trin fel sero?** Mae rhai o'r buddion mwyaf, risg lai, ystum diogelwch, cynhyrchedd datblygwyr, canlyniadau cenhadaeth, ac opsiynolrwydd, yn gwrthsefyll ffigwr doler glir, ac mae esgus eu bod yn sero'n tueddu pob penderfyniad tuag at y gwrthrychol a'r tymor byr. Y risg gystadleuol yw'r camgymeriad gwrthwyneb: cynhyrchu rhif cyfleus a gwisgo dyfaliad mewn manylder ffug. Penderfynwch yn fwriadol pa fuddion y byddwch yn eu hariannu drwy ddirprwyon hygred (toriad a osgowyd, oriau a arbedwyd wedi'u lluosi â chyfradd lwythog) a pha rai y byddwch yn eu sgorio yn erbyn meini prawf anariannol a enwir ac a gerir ochr yn ochr â'r model. Dewch â phenderfyniad diweddar lle bu anghyffyrddadwy'n bwysig a gofynnwch a gafodd ei brisio, ei sgorio, neu ei ollwng yn dawel. I gorff sector cyhoeddus mae hyn hyd yn oed yn siarpach: ni ellir lleihau gwerth cenhadaeth, tegwch, a stiwardiaeth arian cyhoeddus i gyd i refeniw, felly dewiswch y ffwythiant amcan yn agored a dogfennwch y meini prawf anariannol yn hytrach na'u smyglo i mewn fel ffactorau twyllo.

## Lens sector

**Cwmni newydd.** Gyda misoedd o redeg, y rhif economaidd dominyddol yw cost oedi: mae pob wythnos y mae eich ychydig beirianwyr yn ei threulio oddi ar y cynnyrch craidd yn refeniw a dysgu wedi'u gohirio. Cadwch y dadansoddiad i un dudalen a ffafriwch brynu galluoedd cyffredin dros eu hadeiladu, fel bod sylw peirianyddol prin yn aros ar y gwahaniaethwr. Sgipiwch fodelau NPV cywrain; mae cymhariaeth oes-gyfan bras a chap gwariant caled yn ddigon i ddal y trap adeiladu-rhad-rhedeg-drud cyn iddo frathu.

**Busnes bach.** Nid oes gennych ddadansoddwr ariannol, felly cadwch y dull yn syml ac yn onest: cymharwch gost gyflawn perchen ar bob dewis, tanysgrifiad ynghyd â'r oriau staff y mae'n eu bwyta, yn erbyn peidio â gwneud dim. Mae'r alwad prynu-yn-erbyn-adeiladu bron bob amser yn ffafrio prynu, oherwydd bod system na allwch ei chynnal yn dod yn gost rhedeg heb ei chyllidebu sy'n tyfu'n dawel. Barnwch fuddsoddiadau ar adennill byr, greddfol yn hytrach na modelau wedi'u disgowntio, a gwyliwch am brisio fesul sedd sy'n edrych yn rhad nes i chi raddio.

**Menter.** Yr her yw cymharadwyedd ar draws llawer o dimau a phortffolio hir: safonwch un gyfradd ddisgowntio, un gorwel, ac un pecyn offer (NPV, TCO, cost oedi) fel y gellir graddio cynigion cystadleuol ar yr un sail. Prisiwch log dyled-dechnegol a chost oedi'n benodol, oherwydd ar raddfa maent yn gwneud i gostau adeiladu penawdau ymddangos yn fach. Gwnewch achosion busnes yn ddogfennau byw a adolygir yn erbyn y ffigyrau go iawn, fel bod cywirdeb amcangyfrif yn gwella a bod cyllid ac archwiliad yn gallu gweld pam y llifodd cyfalaf lle y gwnaeth.

**Llywodraeth.** Mynnir yn aml ddadansoddiad cost-budd, cyfradd ddisgowntio swyddogol, a chostio oes gyfan, a'r amcan yw gwerth cyhoeddus yn hytrach na refeniw, felly ariannwch yr hyn y gellwch ei ariannu'n hygred a sgoriwch y gweddill yn erbyn meini prawf penodol, cyhoeddedig. Nodwch bob rhagdybiaeth yn agored yn erbyn llinell sylfaen peidio-gwneud-dim, oherwydd bydd archwilwyr a'r cyhoedd yn eu profi. Strwythurwch ariannu'n gynyddrannau sy'n werthfawr yn annibynnol fel bod buddion pob cam yn cael eu gwireddu a'u mesur cyn ymrwymo i'r nesaf, ac fel y gellir stopio rhaglen heb adael arian cyhoeddus suddedig yn sownd.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd chwe pherson gyda naw mis o redeg yn dadlau a ddylai adeiladu ei system filio ei hun neu dalu am un wedi'i letya. Ar un dudalen, mae'r sylfaenwyr yn cymharu'r ddau ddewis dros orwel deunaw mis: mae'r adeiladu'n edrych yn rhatach ar bapur ond yn costio tri mis-peiriannydd ymlaen llaw, ac mae cost oedi (refeniw wedi'i ohirio tra nad yw'r peirianwyr hynny'n rhyddhau'r cynnyrch craidd) yn gwneud i'r ffi danysgrifiad edrych yn fach. Maent yn prynu'r bilio wedi'i letya, yn amddiffyn eu hamser peirianyddol prin ar gyfer y gwahaniaethwr, ac yn ailymweld â'r penderfyniad dim ond os yw pris neu gyfaint yn newid y fathemateg.

**Menter.** Mae manwerthwr yn pwyso ailblatfformio ei stac e-fasnach yn erbyn parhau i glytio'r un presennol. Mae'r tîm peirianneg-a-chyllid yn adeiladu model pum mlynedd ar gyfradd ddisgowntio gorfforaethol, gan gymharu tri dewis (peidio-gwneud-dim, ailffactora cynyddrannol, ac ailblatfformio llawn) ar TCO ar draws adeiladu, cost rhedeg cwmwl, trwyddedu, a chymorth. Maent yn meintioli log dyled-dechnegol y statws quo (cyfraddau digwyddiadau'n codi a chadence rhyddhau'n arafu) a chost oedi nodweddion na all yr un stac hen eu cefnogi. Mae'r ailblatfformio'n dangos cost ymlaen llaw uwch ond NPV positif erbyn blwyddyn tri a chost rhedeg is wedi hynny. Mae dadansoddiad sensitifrwydd yn cadarnhau bod yr argymhelliad yn dal oni bai fod prisiau cwmwl yn codi'n sydyn. Maent yn ei ariannu mewn camau wedi'u clymu i gerrig milltir yn hytrach nag fel un ymrwymiad anwrthdroadwy.

**Llywodraeth.** Mae'n ofynnol i asiantaeth sy'n moderneiddio system budd-daliadau gyflwyno dadansoddiad cost-budd gan ddefnyddio'r gyfradd ddisgowntio swyddogol a chostio oes gyfan. Am mai canlyniadau cenhadaeth yw'r prif fuddion (gwasanaeth cyflymach, mwy cywir, mwy teg), mae'r tîm yn ariannu'r hyn y gall ei ariannu'n hygred (llai o lwyth canolfan alwadau, llai o daliadau anghywir, twyll a osgowyd) ac yn sgorio'r gweddill yn erbyn meini prawf gwerth-cyhoeddus penodol yn hytrach na dyfeisio ffigyrau doler. Mae'r achos busnes yn cyflwyno llinell sylfaen peidio-gwneud-dim, yn nodi ei ragdybiaethau'n agored ar gyfer archwiliad, ac yn strwythuro ariannu'n gynyddrannau sy'n werthfawr yn annibynnol, fel bod buddion pob cam yn cael eu gwireddu a'u mesur cyn ymrwymo i'r nesaf.

## Achos busnes: cymhellion, ROI, a TCO

Dyraniad cyfalaf gwell yw'r elw ar ymarfer economeg peirianneg meddalwedd: mae arian, pobl, ac amser yn llifo at y gwaith sy'n creu'r gwerth mwyaf. Mae'r mecanwaith yn driphlyg. Yn gyntaf, gwastraff a osgowyd: gwrthodir cynigion sy'n methu prawf NPV neu TCO gonest cyn iddynt fwyta blynyddoedd o wariant. Yn ail, dilyniannu gwell: mae prisio cost oedi'n symud y gwaith gwerth-uchaf ymlaen, gan gyfansymio elw ar draws y portffolio. Yn drydydd, llai o synnau drud: mae costio oes gyfan yn atal y methiant clasurol o ariannu adeiladu rhad a chael eich cornelu gan rediad drud.

Mae cost yr ymarfer yn fach: amser dadansoddwr i adeiladu modelau, y ddisgyblaeth i nodi rhagdybiaethau, a'r gwaith diwylliannol o gael arweinwyr i benderfynu ar rifau wedi'u disgowntio, oes-gyfan yn hytrach na phrisiau penawdau. Mae cost *peidio* ag ymarfer hyn yn fwy ond yn wasgaredig. Rydych yn gwerthfawrogi'r gwrthrychol a'r tymor byr yn ormodol yn systematig, yn tan-brisio dyled ac oedi, ac yn darganfod costau rhedeg dim ond ar ôl iddynt fod yn anochel. Fframiwch y ddisgyblaeth i arweinyddiaeth fel y rheolaeth ansawdd ar bob penderfyniad buddsoddi arall. Nid yw'n ychwanegu llinell wariant newydd gymaint â gwneud pob llinell wariant bresennol yn atebol. Mae un rhaglen werth-isel a osgowyd, neu un rhagolwg TCO cywir sy'n atal ffrwydrad cost rhedeg, yn talu am yr ymarfer cyfan sawl gwaith drosodd.

## Gwrth-batrymau a pheryglon

- **Pris prynu fel cost gyfan.** Penderfynu ar sail y ffi adeiladu neu drwydded gan anwybyddu blynyddoedd o weithredu, cymorth, ac amnewid yn y pen draw.
- **Ymrwymiad cost-suddedig.** Parhau ag ymdrech sy'n methu oherwydd arian a wariwyd eisoes yn hytrach na gwerth disgwyliedig y dyfodol.
- **Theatr manylder.** Taenlenni deg-degolyn wedi'u hadeiladu ar fewnbynnau a ddyfalwyd, gan roi awdurdod ffug i gasgliad rhagbenderfynedig.
- **Anwybyddu gwerth amser arian.** Cymharu llifoedd arian tymor-agos a phell-yn-y-dyfodol fel pe bai doler ym mlwyddyn pump yn hafal i ddoler heddiw.
- **Anghyffyrddadwyau fel sero.** Eithrio risg, diogelwch, cynhyrchedd, a gwerth cenhadaeth am eu bod yn anodd eu prisio, gan duedd pob penderfyniad tuag at yr hyn a fesurir.
- **Amcangyfrif fel addewid.** Trin amcangyfrif ymdrech seiliedig ar ystod fel ymrwymiad dyddiad-sefydlog, yna ei reoli i galendr.
- **Dyled dechnegol heb ei phrisio.** Cymryd llwybrau byr heb unrhyw gyfrif o'r llog, hyd nes bod y dreth gyfansymio ar draddodiad yn dod yn argyfwng.
- **Dallineb cost-oedi.** Optimeiddio ar gyfer defnydd tîm a chost uned tra'n anwybyddu'r gwerth llawer mwy a gollir i hwyrni.

## Model aeddfedrwydd

**Lefel 1 (Cychwyn).** Cyfiawnheir penderfyniadau gan bris pennawd a theimlad reddfol, yn adweithiol ac fesul achos. Dim disgowntio, dim TCO, dim rhagdybiaethau wedi'u nodi. Mae amcangyfrifon yn rhifau sengl a drinnir fel addewidion. Mae dyled dechnegol a chost oedi'n anweledig yn unrhyw fodel.

**Lefel 2 (Datblygu).** Mae buddsoddiadau mwy'n cario achos busnes bras gyda rhai costau a buddion, ac ystyrir rhai costau rhedeg. Ymddengys adennill syml neu ROI, ond cymhwysir gwerth amser arian a chostio oes-gyfan yn anwastad ac yn amrywio o dîm i dîm. Weithiau mae gan amcangyfrifon ystodau, er bod yr arfer yn anghyson.

**Lefel 3 (Safoni).** Mae pecyn offer economaidd safonol (NPV, TCO, ROI, cost oedi) gyda chyfradd ddisgowntio a gorwel a rennir wedi'i ddogfennu a'i gymhwyso'n gyson ar draws y portffolio. Modelir ansicrwydd ag ystodau a gwerth disgwyliedig. Amcangyfrifir a blaenoriaethir dyled dechnegol. Mae achosion busnes yn cymharu llinell sylfaen peidio-gwneud-dim, yn nodi eu rhagdybiaethau, ac yn archwiliadwy.

**Lefel 4 (Rheoli).** Mesurir rhagolygon yn erbyn ffigyrau go iawn a'u rheoli â data. Olrheinir cywirdeb amcangyfrif, ROI a wireddwyd, cost rhedeg yn erbyn rhagamcan, a chanlyniadau cost-oedi yn erbyn llinellau sylfaen, ac mae amrywiant sylweddol yn sbarduno adolygiad. Mae achosion busnes yn cario mesurau llwyddiant a meini prawf terfynu diffiniedig a orfodir ar dystiolaeth yn hytrach na theimlad, a dilysir rhagdybiaethau cyfradd-ddisgowntio a sensitifrwydd yn erbyn canlyniadau hanesyddol, fel bod y rhifau'n cael eu rheoli yn hytrach na dim ond eu cynhyrchu.

**Lefel 5 (Cerddorfa).** Mae rhesymu economaidd yn barhaus, wedi'i galibro, ac wedi'i integreiddio â chynllunio portffolio, caffael, a risg. Mae achosion busnes yn ddogfennau byw a adolygir wrth i dystiolaeth gyrraedd, ac mae cywirdeb amcangyfrif yn gwella dros amser oherwydd bod canlyniadau'n bwydo'n ôl. Mae cost oedi'n gyrru dilyniannu, gwerthfawrogir anghyffyrddadwyau'n benodol, ac mae ariannu graddol yn cadw opsiynolrwydd, fel bod y sefydliad yn ail-gydbwyso cyfalaf yn addasol tuag at y gwaith sy'n creu'r gwerth mwyaf wrth i amodau newid.

## Syniadau ar gyfer trafodaeth

- Faint o drylwyredd ariannol sy'n werth ei gymhwyso i benderfyniad gwrthdroadwy, cost-isel cyn i'r dadansoddiad gostio mwy na'r penderfyniad?
- Pa gyfradd ddisgowntio y dylai eich sefydliad ei defnyddio, a faint mae'r argymhelliad yn newid pan fyddwch yn ei hamrywio?
- Pryd mae ariannu anghyffyrddadwy'n fewnwelediad gwirioneddol, a phryd mae'n gynhyrchu rhif cyfleus?
- Sut ydych chi'n prisio'r llog ar ddyled dechnegol yn ddigon argyhoeddiadol i arweinyddiaeth ariannu ei thalu'n ôl?
- Mewn lleoliad sector cyhoeddus, sut ydych chi'n pwyso tegwch a chanlyniadau cenhadaeth sy'n gwrthsefyll ariannu yn erbyn dewisiadau ag elw ariannol glanach?
- A ddylid ailymweld ag achosion busnes yn erbyn y ffigyrau go iawn, a phwy sy'n atebol pan fo'r gwerth a wireddwyd yn gwyro oddi wrth y rhagolwg?

## Casgliadau allweddol

- Mae economeg peirianneg meddalwedd yn gwneud cyfaddawdau gwerth-a-chost yn benodol, yn gymharadwy, ac yn amddiffynadwy: dyma asgwrn cefn dadansoddol rhesymu ROI a TCO a ddefnyddir drwy'r llawlyfr hwn i gyd.
- Penderfynwch ar gost perchnogaeth gyfan ar draws yr oes gyfan, nid pris prynu, a disgowntiwch lifoedd arian y dyfodol fel bod gwerth amser arian yn cael ei barchu.
- Trinwch amcangyfrifon fel ystodau o dan ansicrwydd, trionglwch gost â sawl dull, a byth peidiwch â gadael i amcangyfrif ymdrech galedu'n addewid dyddiad-sefydlog.
- Prisiwch y costau sy'n arferol anweledig, dyled dechnegol fel llog a chost oedi fel gwerth a gollir, oherwydd maent yn aml y rhifau mwyaf yn y model.
- Gwerthfawrogwch anghyffyrddadwyau'n benodol yn hytrach na'u trin fel sero, a dewiswch ffwythiant amcan er-elw neu gyhoeddus yn onest.
- Adeiladwch achosion busnes byw sy'n nodi rhagdybiaethau a dewisiadau gan gynnwys peidio-gwneud-dim, maintiwch y trylwyredd i'r risg, ac ailymwelwch â rhagolygon yn erbyn y ffigyrau go iawn fel bod y sefydliad yn dysgu amcangyfrif yn well.

## Cyfeiriadau a darllen pellach

- Barry W. Boehm, *Software Engineering Economics*
- Barry W. Boehm et al., *Software Cost Estimation with COCOMO II*
- IEEE Computer Society, *SWEBOK Guide* (maes gwybodaeth Economeg Peirianneg Meddalwedd)
- Donald G. Reinertsen, *The Principles of Product Development Flow* (cost oedi, WSJF)
- Steve McConnell, *Software Estimation: Demystifying the Black Art*
- Douglas W. Hubbard, *How to Measure Anything: Finding the Value of Intangibles in Business*
- Ward Cunningham, "The WyCash Portfolio Management System" (y trosiad dyled-dechnegol)
- Philippe Kruchten, Robert Nord, ac Ipek Ozkaya, *Managing Technical Debt*
- Mark Schwartz, *The Art of Business Value* a *A Seat at the Table*
- Swyddfa Rheoli a Chyllideb yr Unol Daleithiau, Circular A-94 (canllawiau a chyfraddau disgowntio ar gyfer dadansoddiad cost-budd)
- HM Treasury, *The Green Book: Central Government Guidance on Appraisal and Evaluation*
