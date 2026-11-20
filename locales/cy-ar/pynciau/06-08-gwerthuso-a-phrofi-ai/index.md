# 6.8 Gwerthuso a phrofi AI

## Trosolwg a chymhelliant

Mae profi meddalwedd gyffredin yn seiliedig ar dybiaeth gysurus: o gael yr un mewnbwn, mae'r rhaglen yn dychwelyd yr un allbwn, a gallwch chi ddatgan yn union beth ddylai'r allbwn hwnnw fod. Mae deallusrwydd artiffisial yn torri'r dybiaeth honno. Gall model ateb yr un cwestiwn mewn dwy ffordd wahanol, y ddwy'n dderbyniol. Gellir ei raddio ar sbectrwm o anghywir i ddisglair yn hytrach na phasio neu fethu. Ac yn aml nid oes un ateb cywir i'w ddatgan yn ei erbyn. Felly mae disgyblaeth gwerthuso, sef mesur pa mor dda mae model yn ymddwyn ar draws nifer o achosion cynrychioliadol yn hytrach na gwirio un allbwn yn erbyn un gwerth disgwyliedig, yn dod yn asgwrn cefn i unrhyw system AI y gellir ymddiried ynddi. Pan fydd timau'n rhyddhau nodweddion AI sy'n eu codi cywilydd, mae'r achos gwraidd bron bob amser yn golygu nad oedd ganddynt ffordd ddifrifol o fesur ansawdd cyn rhyddhau.

I dimau mawr, gwerthuso yw'r hyn sy'n gwneud newid yn ddiogel. Byddwch yn cyfnewid modelau, yn ailysgrifennu prompiau, yn tiwnio adfer, ac yn ychwanegu teclynnau, a gall pob un o'r newidiadau hynny ddirywio ymddygiad yn dawel yr oeddech yn ei gredu'n gadarn. Heb ffordd ailadroddadwy o fesur ansawdd, mae pob newid yn gamblo a phob atchweliad yn cael ei ddarganfod gan ddefnyddiwr. Mae'r bennod hon yn gydymaith mesur i'r penodau adeiladu: AI cynhyrchiol a chymwysiadau LLM (pennod 6.3), asiantau AI a systemau asiantol (pennod 6.7), a pheirianneg dysgu peiriant a MLOps (pennod 6.2). Mae'n ymestyn eich strategaeth brofi gyffredinol (pennod 2.4) i'r byd tebygolegol.

Mae lleoliadau menter a llywodraeth yn codi'r stanau ymhellach. Mae angen platfform gwerthuso a rennir ar fenter sy'n rhedeg dwsinau o nodweddion AI fel nad yw pob tîm yn ailddyfeisio graddio o'r newydd. Mae angen gwerthuso wedi'i ddogfennu a'i archwiliadwy ar asiantaeth lywodraeth, oherwydd mae'n rhaid i "fe wnaethon ni ei brofi" ddod yn "dyma'r dystiolaeth, y set ddata, y fetrig, a'r cymeradwyaeth." Gwerthuso yw lle mae AI cyfrifol a dibynadwy (pennod 6.5) yn peidio â bod yn ddatganiad gwerth ac yn dod yn rhywbeth y gallwch ei ddangos i reoleiddiwr.

## Egwyddorion allweddol

- Trin gwerthuso fel cynnyrch dosbarth cyntaf, nid meddwl-ar-ôl a fachwyd ymlaen at lansiad.
- Mesur gyda data cynrychioliadol sy'n adlewyrchu defnydd go iawn, nid enghreifftiau teganllyd sy'n gwenieithio'r model.
- Cyfuno gwerthuso all-lein ar gyfer ailadrodd cyflym gyda gwerthuso ar-lein ar gyfer gwirionedd sylfaenol.
- Defnyddio barn ddynol fel eich angor, a chalibro pob graddiwr awtomataidd yn ei erbyn.
- Gwarchod eich setiau gwerthuso rhag halogiad, neu bydd eich rhifau'n dweud celwydd wrthych.
- Gwifrio gwerthusiadau i mewn i integreiddio parhaus fel gatiau, fel na all ansawdd atchwelio'n dawel.
- Parhau i fesur mewn cynhyrchiad, oherwydd mae ansawdd yn drifftio hyd yn oed pan nad yw eich cod.

## Argymhellion

### Mabwysiadu datblygiad wedi'i yrru gan werthuso

Cyn i chi diwnio prompt neu ddewis model, ysgrifennwch y gwerthusiad. Mae hyn yn adlewyrchu datblygiad wedi'i yrru gan brofion: rydych yn diffinio beth mae "da" yn ei olygu mewn termau mesuradwy, yna'n adeiladu tuag ato. Ystyr gwerthusiad yma yw set ddata o fewnbynnau wedi'u paru â dull sgorio sy'n dychwelyd rhif neu radd ar gyfer pob allbwn. Dechreuwch yn fach. Mae ugain achos wedi'u dewis yn ofalus sy'n adlewyrchu bwriad defnyddiwr go iawn yn well na mil ar hap. Tyfwch y set wrth i chi ddysgu lle mae'r system yn methu, gan ychwanegu pob methiant cynhyrchiad yn ôl fel achos parhaol fel na all yr un camgymeriad ddychwelyd yn ddisylw.

Mae datblygiad wedi'i yrru gan werthuso yn newid ymddygiad tîm. Pan fydd y diffiniad o dda wedi'i ysgrifennu i lawr ac yn rhedadwy, mae dadleuon ynghylch a helpodd newid yn dod yn rhywbeth y gellir ei wirio yn hytrach na mater o chwaeth. Gwnewch y set werthuso yn arteffact adolygedig mewn rheolaeth fersiynau, wrth ymyl y prompiau a'r cod y mae'n eu mesur.

### Gwahanu gwerthuso all-lein ac ar-lein, a defnyddio'r ddau

Mae gwerthuso all-lein yn rhedeg set ddata sefydlog trwy eich system mewn lleoliad rheoledig, yn gyflym, yn rhad, ac yn ailadroddadwy, fel y gallwch gymharu fersiynau cyn i unrhyw beth gael ei ryddhau. Mae gwerthuso ar-lein yn mesur y system fyw gyda defnyddwyr go iawn trwy fetrigau fel cwblhau tasgau, cyfradd uwchgyfeirio, adborth bawd-i-fyny a bawd-i-lawr, ac canlyniadau busnes i lawr yr afon. Mae all-lein yn dweud wrthych a yw newid yn debygol o fod yn ddiogel; mae ar-lein yn dweud wrthych a wnaeth weithio go iawn. Mae angen y ddau arnoch, oherwydd nid yw setiau all-lein byth yn dal realiti'n llawn ac mae signalau ar-lein yn cyrraedd yn rhy hwyr i fod yn unig warchodwr i chi.

Cysylltwch y ddau yn ddolen. Pan fydd metrigau ar-lein yn gostwng neu ddefnyddwyr yn fflagio ateb gwael, dalgáu'r achos hwnnw, ei labelu, a'i blygu i mewn i'r set all-lein. Cyfeiriwch arbrofion trwy'r un cymhariaeth reoledig a ddefnyddiwch ar gyfer unrhyw newid cynnyrch, sy'n diriogaeth dadansoddeg cynnyrch ac arbrofi (pennod 7.4). Mae prawf A/B sy'n dangos bod model newydd yn codi llwyddiant tasgau'n werth mwy nag unrhyw sgôr all-lein, ac eto'r sgôr all-lein a'ch galluogodd i feiddio rhedeg y prawf.

### Adeiladu setiau gwerthuso cynrychioliadol a gwarchod rhag halogiad

Mae eich gwerthusiad cyn onested â'i ddata yn unig. Adeiladwch setiau data aur, casgliadau curadwyd o fewnbynnau gydag allbynnau disgwyliedig wedi'u gwirio neu rwbrigau sgorio, sy'n adlewyrchu dosraniad go iawn yr hyn mae defnyddwyr yn ei ofyn: yr achosion cyffredin, yr achosion prin-ond-hanfodol, yr achosion gwrthwynebus, a'r rhai y mae eich system yn eu cael yn anghywir ar hyn o bryd. Haenwch nhw fel y gallwch ddarllen ansawdd fesul segment yn hytrach na chuddio categori sy'n methu y tu mewn i gyfartaledd gweddol. Cael arbenigwyr parth i wirio'r atebion disgwyliedig, oherwydd mae set aur wedi'i hadeiladu ar atebion anghywir yn waeth na dim un o gwbl.

Yna diogelwch y data hwnnw rhag halogiad. Mae halogiad set-brawf yn digwydd pan fydd eich enghreifftiau gwerthuso'n gollwng i mewn i ddata hyfforddi model neu i mewn i'r prompt ei hun, fel bod y model yn ymddangos yn perfformio'n dda oherwydd ei fod i bob pwrpas wedi gweld yr atebion. Dyma pam y gall model sgorio'n ddisglair ar feincnod cyhoeddus a baglu ar eich traffig go iawn. Cadwch ran o'ch data gwerthuso'n breifat a byth ei anfon at drydydd parti na allwch ymddiried ynddo. Adnewyddwch setiau dros amser. Gwyliwch am y gollyngiad mwy cynnil lle mae datblygwyr yn tiwnio prompiau â llaw yn erbyn y set werthuso nes bod y sgôr yn ddiystyr, math o orgymhwyso i'r prawf yn hytrach na gwelliant gwirioneddol. Cadwch set ffres ychwanegol nad ydych ond yn edrych arni'n achlysurol.

### Dewis metrigau sy'n ffitio'r dasg

Paru eich mesur â siâp yr allbwn. Ar gyfer dosbarthu a thynnu, lle mae label cywir, mae metrigau clasurol yn berthnasol: [manwl gywirdeb ac adalw](https://en.wikipedia.org/wiki/Precision_and_recall) (o'r eitemau a fflagiwyd gennych, faint oedd yn gywir, ac o'r eitemau cywir, faint a ddaethoch o hyd iddynt), y [sgôr-F](https://en.wikipedia.org/wiki/F-score) sy'n eu cydbwyso, a chywirdeb cydweddu union. Ar gyfer unrhyw beth lle mae tebygolrwydd hyderus yn bwysig, mesurwch [calibradau](https://en.wikipedia.org/wiki/Calibration_(statistics)), p'un a yw hyder datganedig o 80 y cant yn gywir tua 80 y cant o'r amser, oherwydd mae model wedi'i galibro'n dda sy'n gwybod pryd mae'n ansicr yn llawer mwy diogel na model gorhyderus.

Mae allbynnau cynhyrchiol yn anos. Mae metrigau seiliedig ar gyfeirnod fel [BLEU](https://en.wikipedia.org/wiki/BLEU) a ROUGE, a adeiladwyd yn wreiddiol ar gyfer cyfieithu peirianyddol a chrynhoi, yn cymharu testun a gynhyrchwyd yn erbyn testun cyfeirnod trwy gyfrif geiriau ac ymadroddion sy'n gorgyffwrdd. Maen nhw'n rhad ac yn ailadroddadwy, ac maen nhw'n ddirprwyon gwan ar gyfer ansawdd: maen nhw'n gwobrwyo gorgyffwrdd wyneb ac yn cosbi ateb cywir wedi'i eirio'n wahanol i'r cyfeirnod. Defnyddiwch nhw fel signalau atchweliad bras, nid fel eich diffiniad o dda. Ar gyfer tasgau penagored, mae sgorio seiliedig ar rwbrig yn gweithio'n well: diffiniwch feini prawf eglur (a yw'n seiliedig ar dystiolaeth, yn gyflawn, yn ddiogel, ac wedi'i fformatio'n gywir) a sgoriwch bob un. Mae rwbrigau'n gwneud ansawdd goddrychol yn ddarllenadwy ac yn adolygadwy.

### Defnyddio LLM-fel-barnwr, ond ei galibro yn erbyn pobl

Nid yw graddio allbwn cynhyrchiol â llaw yn graddfeuo, felly mae timau'n cynyddu defnyddio [model iaith mawr](https://en.wikipedia.org/wiki/Large_language_model) cryf fel barnwr awtomataidd, gan ei brompio â'r mewnbwn, yr allbwn, a rwbrig, a gofyn iddo sgorio. Mae'r dull LLM-fel-barnwr hwn yn gyflym ac yn rhyfeddol o alluog, ac mae'n cario rhagfarnau go iawn y mae'n rhaid i chi eu rheoli. Mae barnwyr yn tueddu i ffafrio atebion hirach, ffafrio'r opsiwn cyntaf a ddangosir mewn cymhariaeth barau (rhagfarn safle), gwobrwyo eu harddull ysgrifennu eu hunain, a gellir eu dylanwadu gan resymu llyfn ond anghywir. Os na ellir eu gwirio, mae barnwr rhagfarnllyd yn rhoi rhifau hyderus, manwl gywir, anghywir i chi.

Calibrwch y barnwr yn erbyn labeli dynol. Cael pobl i raddio sampl, yna gwiriwch pa mor dda mae'r model barnwr yn cytuno â nhw, a pharhau i diwnio prompt y barnwr nes bod cytundeb yn ddigon uchel i ymddiried ynddo. Lleihau rhagfarnau hysbys yn fwriadol: hapddosbarthu trefn opsiynau, rheoli am hyd, a gofyn am sgôr wedi'i angori mewn rwbrig gyda rhesymau yn hytrach na rhif noeth. Trin y barnwr fel offeryn mesur sydd angen ailgalibradau cyfnodol, nid oracl sefydlog. Wrth adeiladu'r barnwr, rhagosodwch i'r model mwyaf galluog sydd ar gael, oherwydd mai riwl wan yw barnwr gwan.

### Cadw pobl yn y ddolen ar gyfer y gwirionedd sylfaenol

Mae gwerthuso dynol yn parhau i fod yr angor y mae pob metrig awtomataidd yn cael ei fesur yn ei erbyn, felly buddsoddwch mewn ei wneud yn dda. Ysgrifennwch ganllawiau anodi eglur, hyfforddwch eich anodwyr, a mesurwch gytundeb rhwng anodwyr, sef y graddau y mae adolygwyr annibynnol yn rhoi'r un radd i'r un achos. Mae cytundeb isel fel arfer yn golygu bod eich rwbrig yn amwys, nid bod eich adolygwyr yn ddiofal, felly trwsiwch y rwbrig. Ar gyfer parthau risg uchel, defnyddiwch arbenigwyr cymwysedig, nid gweithwyr torf sy'n brin o'r cyd-destun i farnu ateb cyfreithiol neu feddygol.

### Tîm coch ar gyfer diogelwch a chadernid gwrthwynebus

Mae setiau gwerthuso safonol yn mesur a yw'r system yn gwneud y peth cywir ar fewnbynnau rhesymol. Mae [timio coch](https://en.wikipedia.org/wiki/Red_team), sef ymosod yn fwriadol ar eich system eich hun i ddarganfod lle mae'n camymddwyn, yn mesur beth sy'n digwydd o dan bwysau. Profwch am chwistrelliad prompt, dianc o gaethiwed, cynnwys anniogel, gollyngiadau preifatrwydd, ac allbynnau rhagfarnllyd. Gwnewch hyn yn siwt ailadroddadwy, nid ymarfer un-tro: trowch bob ymosodiad llwyddiannus yn achos atchweliad parhaol fel bod gwendid a drwsiwyd yn aros wedi'i drwsio. Mae'r gwaith hwn yn cysylltu'n uniongyrchol ag AI cyfrifol a dibynadwy (pennod 6.5), ac mewn lleoliadau rheoledig dyma'n aml y dystiolaeth sy'n bodloni adolygiad diogelwch.

### Gwerthuso asiantau yn ôl llwyddiant tasg o ddechrau i ddiwedd

Ni ellir barnu asiantau sy'n cynllunio ac yn gweithredu dros lawer o gamau un allbwn ar y tro. Yr hyn sy'n bwysig yw a lwyddodd y dasg gyfan: a wnaeth yr asiant archebu'r cyfarfod, datrys y tocyn, neu gwblhau'r llif gwaith yn gywir ac yn ddiogel. Adeiladwch werthusiadau lefel-tasg mewn amgylchedd tywod lle gall yr asiant weithredu yn erbyn ffitwyr realistig ond diogel, a sgoriwch ganlyniadau terfynol ynghyd â'r llwybr, sef y dilyniant o gamau a galwadau teclyn a gymerodd i gyrraedd yno. Mae ateb cywir a gyrhaeddwyd trwy lwybr peryglus neu wastraffus yn dal yn broblem. Mae hyn yn hanfodol i asiantau AI a systemau asiantol (pennod 6.7), lle gall un cam anghywir gael canlyniadau go iawn.

### Gwifrio gwerthusiadau i mewn i CI a monitro cynhyrchiad

Gwnewch werthuso'n awtomatig. Rhedwch eich siwt all-lein mewn [integreiddio parhaus](https://en.wikipedia.org/wiki/Continuous_integration) (CI) ar bob newid prompt, model, neu adfer, a gatiwch gyfuniadau arno yn union fel y gatiwch ar brofion uned, arfer sydd wedi'i wreiddio yn eich strategaeth brofi ehangach (pennod 2.4). Gan fod sgorau'n swnllyd, gatiwch ar drothwyon a thueddiadau yn hytrach na mynnu rhediad perffaith, a methwch yr adeilad pan fydd metrig allweddol yn syrthio o dan ei lawr neu'n atchwelio y tu hwnt i ymyl gosodedig. Yna parhau i wylio mewn cynhyrchiad: monitro signalau ansawdd, dosraniadau allbwn, a drifft mewnbwn fel eich bod yn dal y dirywiad araf y mae profion all-lein yn ei golli, sy'n clymu i mewn i arferion arsylladwyedd peirianneg dysgu peiriant a MLOps (pennod 6.2). Gall model a oedd yn gywir wrth lansio ddirywio wrth i'r byd y mae'n ei ddisgrifio newid oddi tano.

## Cyfaddawdau: manteision ac anfanteision

| Dull gwerthuso | Manteision | Anfanteision | Gorau pan |
|---|---|---|---|
| Gwerthuso dynol | Ffyddlondeb uchaf, yn dal cynildeb | Araf, costus, anodd graddfeuo | Gwirionedd sylfaenol, risg uchel, calibro barnwyr |
| LLM-fel-barnwr | Cyflym, rhad, yn graddfeuo i setiau mawr | Rhagfarnllyd, angen calibradau | Rhediadau all-lein aml ar allbwn cynhyrchiol |
| Metrigau seiliedig ar gyfeirnod (BLEU, ROUGE) | Rhad, penderfynadwy, ailadroddadwy | Dirprwy gwan ar gyfer ansawdd go iawn | Signalau atchweliad bras, nid dyfarniadau terfynol |
| Metrigau clasurol (manwl gywirdeb, adalw, sgôr-F) | Gwrthrychol, deallus dda | Dim ond yn ffitio tasgau â labeli cywir | Dosbarthu, tynnu, adfer |
| Meincnodau cyhoeddus | Cymaradwy ar draws modelau, dim sefydlu | Halogiad, ffit gwael i'ch tasg | Rhestr fer modelau cynnar, nid gatiau rhyddhau |
| Gwerthuso ar-lein (A/B, adborth) | Yn adlewyrchu defnyddwyr a chanlyniadau go iawn | Araf, yn cyrraedd ar ôl amlygiad | Cadarnhau bod newid wedi helpu go iawn |

Y tyndra canolog yw cyflymder yn erbyn ffyddlondeb. Gwerthuso dynol yw'r mwyaf dibynadwy a'r lleiaf graddfeuadwy; mae graddio awtomataidd yn wrthdro. Yr ateb yw eu haenu: defnyddio dulliau cyflym, rhad ar gyfer ailadrodd cyson, angori'r dulliau hynny wrth farn ddynol trwy galibradau rheolaidd, a chadw adolygiad dynol llawn ar gyfer y penderfyniadau risg uchaf a chan wirio bod eich metrigau rhad yn dal i olrhain realiti. Ail dyndra yw cyfleustra all-lein yn erbyn gwirionedd ar-lein. Mae setiau all-lein yn eich galluogi i symud yn gyflym ond byth yn adlewyrchu cynhyrchiad yn llawn, felly triniwch sgôr all-lein cryf fel caniatâd i redeg prawf ar-lein gofalus, nid fel prawf eich bod wedi gorffen.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Beth yw ein bar ar gyfer "digon da," a phwy sy'n berchen ar y set werthuso sy'n ei diffinio?** Mae gan bob nodwedd AI drothwy ansawdd ymhlyg, a phan fydd yn aros yn ymhlyg, mae pob peiriannydd yn gosod ei un ei hun yn ôl teimlad ac mae anghydfodau'n cael eu setlo gan bwy bynnag sydd hynaf yn yr ystafell. Mae ysgrifennu'r bar i lawr fel set werthuso rhedadwy gyda sgorau targed fesul segment yn troi'r anghydfodau hynny'n gwestiynau mesuradwy. Dewch â'ch diffiniad cyfredol o lwyddiant, y data y tu ôl iddo, a chyfrif gonest o bwy sy'n ei gynnal go iawn, oherwydd mae set werthuso heb berchennog yn pydru mor gyflym ag unrhyw god heb ei ofalu. Penderfynwch a yw'r bar yn amrywio yn ôl haen risg, gan y dylai ateb cyfreithiol cyhoeddus glirio bar uwch na chymorth ysgogi mewnol. Dylai'r ateb ddweud wrthych a all unrhyw un ar hyn o bryd ryddhau newid AI heb ddim mesur rhwng nhw a defnyddwyr.

2. **Sut ydyn ni'n gwybod bod ein rhifau gwerthuso'n onest yn hytrach na wedi'u halogi neu orgymhwyso?** Dim ond os yw'n rhagfynegi ansawdd byd go iawn mae sgôr yn ddefnyddiol, ac mae yna lawer o ffyrdd iddo beidio â gwneud hynny bellach: data meincnod yn gollwng i mewn i hyfforddiant, datblygwyr yn tiwnio prompiau yn erbyn y set brawf nes bod y rhif yn ddiystyr, neu set ddata aur wedi'i adeiladu ar atebion na chawsant erioed eu gwirio. Dewch â thystiolaeth am o ble y daeth eich data gwerthuso, faint ohono sy'n breifat, a pha mor aml y caiff ei adnewyddu. Trafodwch a ydych yn cadw daliad-yn-ôl ffres nad ydych ond yn edrych arno'n anaml, fel bod gennych o leiaf un rhif nad oes neb wedi bod yn optimeiddio yn ei erbyn. Os na allwch esbonio pam y byddai eich sgorau'n dal i sefyll ar ddata na chafodd y model erioed ddylanwad arno, rydych yn mesur eich adlewyrchiad eich hun.

3. **Ble mae pobl yn aros yn y ddolen, a sut ydyn ni'n cadw ein barnwyr awtomataidd wedi'u calibro iddyn nhw?** Mae LLM-fel-barnwr a metrigau cyfeirnod yn eich galluogi i raddio ar raddfa, ac maen nhw'n drifftio oddi wrth farn ddynol mewn ffyrdd sy'n anweledig oni bai eich bod yn gwirio. Dewch â'ch cyfradd gytundeb gyfredol rhwng graddio awtomataidd ac adolygiad dynol, pa mor ddiweddar y gwnaethoch ei fesur, a pha ragfarnau (hyd, safle, arddull) rydych wedi'u profi. Penderfynwch pa benderfyniadau sydd angen graddiwr dynol beth bynnag yw'r gost, sef fel arfer y risg uchaf a'r rhai a ddefnyddir i ailgalibradu'r barnwr awtomataidd. Siaradwch am ansawdd anodi hefyd, oherwydd mae barnwr wedi'i galibro yn erbyn labeli dynol anghyson yn etifeddu'r anghysondeb hwnnw. Dylai'r ateb gynhyrchu amserlen ar gyfer ailgalibradu, nid bendith un-tro.

4. **Pa newidiadau AI sy'n cael eu gatio ar werthuso heddiw, a pha rai sy'n dal i gyrraedd defnyddwyr ar hyder rhywun yn unig?** Mae gât sy'n rhedeg ar rai newidiadau ond nid ar eraill yn rhoi rhith diogelwch i chi wrth adael i'r atchweliadau go iawn lithro trwy'r llwybr heb ei atal: newid prompt tawel, tiwnio adfer, cynnydd fersiwn model na feddyliodd unrhyw un ei fod yn cyfrif fel newid. I dîm mawr, mae'r perygl yn tyfu gyda nifer y bobl sy'n gallu cyffwrdd â phrompt, oherwydd mae pob llwybr heb ei atal yn ffordd o ryddhau atchweliad na welodd unrhyw set ddata erioed. Dewch â'r rhestr o fathau o newidiadau sy'n sbarduno'r siwt all-lein ar hyn o bryd mewn integreiddio parhaus, y rhai nad ydynt, a'r digwyddiadau diweddaraf a olrhaniwyd yn ôl at newid heb ei atal. Penderfynwch pa drothwy a thuedd mae'r gât yn eu gorfodi, gan fod sgôr swnllyd yn mynnu llawr ac ymyl atchweliad yn hytrach na mynnu rhediad perffaith. Mewn lleoliadau menter a llywodraeth, clymwch y gât wrth y cofnod rhyddhau ei hun, fel bod y dystiolaeth bod newid wedi'i fesur yn rhan o'r trywydd archwilio ac nid yn sgrinlun a gymerwyd unwaith gan rywun.

5. **Faint ydyn ni'n ei wario ar werthuso, ac a yw'r gwariant hwnnw'n cyfateb i risg pob nodwedd?** Nid yw gwerthuso'n rhad ac am ddim: mae llafur anodi, y cyfrifiadura y mae barnwyr awtomataidd yn ei losgi ar bob rhediad, a'r gwaith sefydlog o gadw setiau data aur yn gynrychioliadol i gyd yn costio arian go iawn, ac mae tîm nad yw byth yn enwi'r costau hynny'n tueddu naill ai i danfuddsoddi mewn nodwedd risg uchel neu i orblatio un i'w daflu. Y tyniad cystadleuol yw rhwng ffyddlondeb a chyllideb, oherwydd mai'r dull mwyaf dibynadwy, adolygiad dynol arbenigol, yw hefyd y lleiaf graddfeuadwy, felly ni allwch fforddio ei wneud ym mhobman a rhaid i chi benderfynu ble mae'n ennill ei bris. Dewch â'r gost gyfredol fesul rhediad gwerthuso, oriau anodi fesul nodwedd, a haen risg onest ar gyfer pob system fel bod modd i'r ystafell weld i ble mae'r arian yn mynd o'i gymharu â ble mae'r perygl yn byw. I fenter, dyma'r ddadl gryfaf dros blatfform gwerthuso a rennir sy'n amorteiddio anodi a chyfrifiadura ar draws llawer o dimau; i asiantaeth lywodraeth, dylai'r haen risg fapio'n uniongyrchol i ddyfnder y dystiolaeth y bydd corff goruchwylio'n ei ofyn yn ddiweddarach.

6. **Pan fydd model gwell yn cyrraedd, pa mor gyflym allwn ni brofi a yw'n helpu, a phwy sy'n cael gwneud y newid?** Mae gwerth siwt werthuso'n cael ei wireddu fwyaf miniog ar y diwrnod y bydd model cryfach yn rhyddhau, oherwydd gall tîm sy'n gallu rhedeg ei setiau data aur a'i siwt timio coch yn erbyn y model newydd mewn prynhawn fabwysiadu gwelliannau y bydd tîm sy'n graddio â llaw yn eu colli am fisoedd. Y tyndra yw rhwng cyflymder a gofal: rydych am symud y diwrnod y bydd model gwell yn ymddangos, ac ni allwch adael i gyfnewidiad ddirywio'n dawel categori o atebion y mae eich sgôr cyfartalog yn ei guddio. Dewch â'r amser y mae'n ei gymryd ar hyn o bryd i redeg cymhariaeth all-lein lawn yn erbyn darparwr newydd, a yw eich setiau gwerthuso'n gludadwy ar draws modelau, a'r segmentau lle byddai atchweliad yn bwysicaf. Mewn lleoliadau rheoledig a chyhoeddus, enwch pwy sy'n dal yr awdurdod i gymeradwyo newid model a pha dystiolaeth ddogfennedig sydd ei angen arnynt, oherwydd mae cyfnewid heb ei ddogfennu o'r model y tu ôl i benderfyniad sy'n wynebu dinasyddion yn union y math o newid y bydd archwiliwr yn gofyn i chi ei gyfiawnhau.

## Lens sector

**Cwmni newydd.** Adeiladwch y gwerthusiad onest lleiaf y gallwch a gadewch iddo dyfu gyda'r cynnyrch. Mae taenlen o ugain i bedwar deg achos go iawn, pob un ag ateb disgwyliedig wedi'i wirio, wedi'i redeg gan sgript cyn pob cyfuniad, yn curo unrhyw feincnod cyhoeddus ar gyfer eich cornel ac yn costio bron dim. Hepgorwch y platfform a rennir a'r LLM-fel-barnwr nes bod graddio â llaw wir yn brifo, ond plygwch bob methiant a adroddwyd gan ddefnyddiwr yn ôl i mewn i'r set o'r diwrnod cyntaf, oherwydd dyna'r reflecs sy'n atal yr un cywilydd ddwywaith.

**Busnes bach.** Mae'n debyg nad oes gennych arbenigwr gwerthuso ac rydych yn prynu eich AI wedi'i fewnblannu mewn teclynnau, felly eich gwaith chi yw mynnu tystiolaeth yn hytrach na'i hadeiladu. Gofynnwch i bob gwerthwr sut y gwnaethant fesur ansawdd, a ydynt yn profi ar ddata sy'n debyg i'ch un chi, a sut y byddech yn sylwi ar atchweliad ar ôl diweddariad na ddewisoch chi. Cadwch set fach breifat o'ch achosion go iawn eich hun i wirio'r teclyn eich hun, gan fod ateb awtomataidd anghywir sy'n cyrraedd cwsmer yn costio llawer mwy i chi na'r munudau y mae'r gwiriad hwnnw'n eu cymryd.

**Menter.** Y wobr yw platfform gwerthuso a rennir fel nad yw dwsin o dimau'n ailddyfeisio graddio'n unigol: storfa gyffredin ar gyfer setiau data aur, siwtiau all-lein wedi'u gatio mewn integreiddio parhaus, prompiau barnwr-LLM cofrestredig gyda'u sgorau calibradau, a metrigau ar-lein fesul nodwedd. Haenwch lywodraethu ar ei ben gyda haenau risg sy'n gosod y bar gofynnol a'r cymeradwyaeth cyn rhyddhau, fel bod nodwedd risg uchel yn clirio gât uwch na chymorth mewnol. Mae'r platfform yn amorteiddio anodi a chyfrifiadura ar draws timau, sef y ddadl gryfaf dros adeiladu un yn hytrach na gadael i bob grŵp fyrfyfyrio.

**Llywodraeth.** Mae'n rhaid i werthuso fod yn archwiliadwy, nid dim ond wedi'i wneud, felly archifwch fersiwn y set ddata, y metrigau, enw'r adolygydd, a'r cymeradwyaeth fel tystiolaeth atebolrwydd ar gyfer pob rhyddhad. Dylai siwt timio coch brofi bod y system yn gwrthod dyfeisio polisi neu ddweud cyfraith absennol o'i ffynonellau, a dylai caffael fynnu bod gwerthwyr yn datgelu sut y gwnaethant werthuso'r model a rhoi cludadwyedd eich data gwerthuso. Pan fydd corff goruchwylio'n gofyn sut ydych chi'n gwybod bod y teclyn yn ddiogel, rhaid i'r ateb fod yn gofnod dyddiedig, nid sicrwydd.

## Enghreifftiau

**Cwmni newydd.** Dechreuodd cwmni pedwar person yn adeiladu cynorthwyydd adolygu contractau AI gyda thaenlen o bedwar deg cymal go iawn, pob un wedi'i labelu gan eu cyfreithiwr mewnol â'r risg y dylai ei fflagio. Rhedodd pob newid prompt yn erbyn y set honno mewn sgript cyn cyfuno, a'r sgôr yn cael ei argraffu yn y cais tynnu. Pan fyddai defnyddwyr yn fflagio cymal a gollwyd, aeth yn syth i mewn i'r daenlen, felly tyfodd y set gyda'r cynnyrch. Wrth i'r cyfaint godi, ychwanegwyd LLM-fel-barnwr ganddynt i raddio ansawdd esboniad, ond dim ond ar ôl gwirio ei fod yn cytuno â'r cyfreithiwr ar sampl. Roedd rhad, preifat, ac onest yn curo unrhyw feincnod cyhoeddus ar gyfer eu cornel.

**Menter.** Rhedodd banc mawr ddwsin o nodweddion AI ar draws cymorth, chwilio, a theclynnau mewnol, ac roedd pob tîm wedi bod yn graddio'n wahanol. Adeiladasant blatfform gwerthuso a rennir: lle cyffredin i storio setiau data aur, rhedeg siwtiau all-lein mewn CI, cofrestru prompiau barnwr-LLM gyda'u sgorau calibradau, a olrhain metrigau ar-lein fesul nodwedd. Eisteddodd llywodraethu ar ei ben, gyda haenau risg oedd yn gosod y bar gofynnol a'r cymeradwyaeth angenrheidiol cyn rhyddhau. Ni allai nodwedd esbonio twyll newydd gael ei rhyddhau nes bod ei set werthuso wedi'i hadolygu, ei siwt timio coch wedi pasio, a'i pherchennog atebol wedi arwyddo'r canlyniadau. Golygai ailddefnyddio'r platfform fod timau'n dadlau am eu parth, nid am sut i fesur.

**Llywodraeth.** Defnyddiodd asiantaeth iechyd cyhoeddus gynorthwyydd i helpu staff ateb cwestiynau budd-daliadau o arweiniad cymeradwy. Gan y gallai ateb anghywir effeithio ar gymhwysedd rhywun, roedd yn rhaid i werthuso fod yn archwiliadwy. Rhedodd pob rhyddhad set werthuso ddogfennedig yn cwmpasu cwestiynau cyffredin, achosion ffiniol, a phrompiau gwrthwynebus, ac archifwyd y canlyniadau, fersiwn y set ddata, y metrigau, ac enw'r adolygydd fel tystiolaeth atebolrwydd. Gwiriodd siwt timio coch fod y system yn gwrthod dyfeisio polisi neu ddweud cyfraith absennol o'i ffynonellau. Pan ofynnodd corff goruchwylio sut roedd yr asiantaeth yn gwybod bod y teclyn yn ddiogel, y cofnod dyddiedig oedd yr ateb, nid sicrwydd.

## Achos busnes: cymhellion, ROI, a TCO

Mae gwerthuso'n talu amdano'i hun trwy wneud pob buddsoddiad AI arall yn fwy diogel ac yn gyflymach. Mae ei enillion ar fuddsoddiad (ROI) yn ymddangos fel llai o ddigwyddiadau cynhyrchiad, ailadrodd cyflymach oherwydd gall timau newid prompiau a modelau'n hyderus, a'r gallu i fabwysiadu modelau gwell y diwrnod y byddant yn cyrraedd oherwydd gallwch brofi a ydynt yn helpu. Y ffordd fwyaf clir o'i werthfawrogi yw cost ei absenoldeb: gall un rhithdyb gyhoeddus, allbwn rhagfarnllyd, neu gollyngiad data gostio llawer mwy mewn adfer, colli ymddiriedaeth, ac amlygiad rheoleiddiol na blynyddoedd o seilwaith gwerthuso. Dyma'r gwahaniaeth rhwng darganfod atchweliad mewn CI am ddim a'i ddarganfod yn y papur newydd.

Mae cyfanswm cost perchnogaeth (TCO) yn real ac yn werth ei enwi. Rydych yn talu am lafur anodi, am y cyfrifiadura y mae barnwyr awtomataidd yn ei ddefnyddio, ac am y gwaith parhaus o gadw setiau gwerthuso'n gynrychioliadol wrth i ddefnydd newid. Ar raddfa menter, mae platfform a rennir yn amorteiddio'r rhan fwyaf o hyn ar draws llawer o dimau, sef y ddadl gryfaf dros adeiladu un yn hytrach na gadael i bob grŵp fyrfyfyrio. Gwnewch yr achos i arweinyddiaeth trwy baru risg concrid (cost un ateb cyhoeddus gwael yn eich parth) gyda gallu concrid (y cyflymder i fabwysiadu pob model newydd yn ddiogel), a thrwy fframio gwerthuso fel y rheolaeth sy'n galluogi'r sefydliad i symud yn gyflym heb symud yn ddi-hid.

## Gwrth-batrymau a pheryglon

- **Rhyddhau seiliedig ar deimlad.** Barnu newidiadau AI trwy roi cynnig ar ychydig o brompiau â llaw, heb ddata a heb sgôr ailadroddadwy.
- **Theatr feincnod.** Ymddiried mewn sgôr feincnod gyhoeddus gref fel prawf bod y system yn ffitio'ch tasg, gan anwybyddu halogiad ac anghyfateb dosraniad.
- **Gorgymhwyso i'r set werthuso.** Tiwnio prompiau yn erbyn yr un set sefydlog nes bod y rhif yn uchel ac yn ddiystyr, heb ddaliad-yn-ôl ffres.
- **Barnwyr heb eu calibro.** Defnyddio LLM-fel-barnwr ac ymddiried yn ei sgorau heb erioed wirio cytundeb â graddwyr dynol.
- **Addoli metrigau.** Optimeiddio BLEU neu ROUGE fel petai'n ansawdd, a rhyddhau atebion gwaeth sy'n digwydd gorgyffwrdd â'r testun cyfeirnod.
- **Timio coch un-tro.** Ymosod ar y system unwaith cyn lansio a byth yn troi canfyddiadau'n brofion atchweliad parhaol.
- **Hyder all-lein yn unig.** Credu bod sgôr all-lein dda yn golygu bod y nodwedd yn gweithio, heb ddim mesuriad ar-lein o ganlyniadau go iawn.
- **Setiau gwerthuso amddifad.** Setiau data heb berchennog, nad ydynt byth yn amsugno methiannau cynhyrchiad ac yn araf beidio ag adlewyrchu realiti.

## Model aeddfedrwydd

- **Lefel 1, Cychwyn:** Barnir newidiadau AI â llaw ar ychydig o enghreifftiau, yn adweithiol, pan fydd rhywun yn digwydd poeni. Nid oes set ddata, dim sgôr ailadroddadwy, a dim gât. Darganfyddir atchweliadau gan ddefnyddwyr, ac ni all neb ddweud a yw'r system yn well neu'n waeth na'r mis diwethaf.
- **Lefel 2, Datblygu:** Mae rhai timau'n cadw setiau data aur bach ac yn eu rhedeg â llaw cyn newidiadau mawr, ac mae ychydig o sgorau clasurol neu seiliedig ar gyfeirnod yn bodoli. Mae adolygiad dynol yn digwydd ar gyfer nodweddion pwysig, ond mae graddio'n anghyson ar draws timau, nid yw gwerthuso'n awtomataidd nac wedi'i gatio, ac mae pob grŵp yn ei wneud yn wahanol.
- **Lefel 3, Safoni:** Mae siwtiau all-lein yn rhedeg mewn integreiddio parhaus ar bob newid prompt, model, neu adfer ac yn gatio cyfuniadau, gan ddilyn un arfer dogfennedig ar draws y sefydliad. Mae LLM-fel-barnwr wedi'i galibro yn erbyn labeli dynol, mae timio coch yn siwt ailadroddadwy, ac mae setiau data'n cael eu perchen, eu fersiynu, a'u bwydo gan fethiannau cynhyrchiad, gyda halogiad yn cael ei warchod yn weithredol.
- **Lefel 4, Rheoli:** Mae gwerthuso'n cael ei fesur a'i reoli gyda data yn erbyn llinellau sylfaen. Olrheinir cyfraddau cytundeb barnwr-i-ddynol, cyfraddau pasio timio coch, sgorau fesul segment, llwyddiant tasgau ar-lein, a drifft dros amser, ac mae cyfuniadau'n gatio ar drothwyon ac ymylon atchweliad yn hytrach nag un rhediad perffaith. Mae cost anodi a chyfrifiadura fesul rhediad wedi'u cyllidebu fesul nodwedd, mae ailgalibradau'n digwydd ar amserlen, ac mae pob canlyniad yn cario perchennog atebol a chymeradwyaeth.
- **Lefel 5, Cydgordio:** Mae platfform gwerthuso a rennir yn gwasanaethu'r sefydliad cyfan, ac mae gwerthuso all-lein ac ar-lein yn ffurfio dolen barhaus wedi'i chlymu wrth ganlyniadau busnes. Profir modelau newydd yn erbyn setiau gwerthuso cludadwy'r diwrnod y byddant yn cyrraedd, mae'r portffolio'n addasu wrth i ddefnydd a risg newid, mae tystiolaeth gwerthuso'n archwiliadwy ar gyfer rheoleiddwyr a goruchwyliaeth, ac mae gwersi o fethiannau un tîm yn llifo i mewn i setiau data pob tîm.

## Syniadau ar gyfer trafodaeth

1. Sut ydych chi'n penderfynu pryd mae sgôr all-lein yn ddigon cryf i gyfiawnhau arbrawf ar-lein, a phryd nad yw?
2. Beth yw'r gymhareb gywir o werthuso dynol i raddio awtomataidd ar gyfer eich proffil risg, a pha mor aml y dylech ei hailystyried?
3. Pan fydd meincnod cyhoeddus a'ch set werthuso breifat yn anghytuno ynghylch pa fodel sy'n well, pa un ydych chi'n ymddiried ynddo a pham?
4. Sut ydych chi'n cadw set werthuso'n gynrychioliadol wrth i ymddygiad defnyddwyr newid, heb adael iddi chwyddo'n rhywbeth rhy araf i'w redeg mewn CI?
5. Beth sy'n perthyn i siwt timio coch ar gyfer eich parth, a phwy sy'n gymwys i ddylunio'r ymosodiadau?
6. Sut ydych chi'n gwerthuso llwybr asiant, nid yn unig ei ateb terfynol, heb foddi yng nghost graddio pob cam?

## Prif gasgliadau

- Mae gwerthuso AI yn wahanol i brofi meddalwedd oherwydd nad yw allbynnau'n benderfynadwy ac anaml y ceir un ateb cywir, felly rydych yn mesur ansawdd ar draws achosion cynrychioliadol yn lle datgan gwerthoedd union.
- Ymarferwch ddatblygiad wedi'i yrru gan werthuso: diffiniwch ansawdd mesuradwy'n gyntaf, yna adeiladu tuag ato, a phlygwch bob methiant cynhyrchiad yn ôl i mewn i'r set.
- Haenwch ddulliau yn ôl cyflymder a ffyddlondeb: graddio awtomataidd rhad ar gyfer ailadrodd cyson, barn ddynol fel yr angor, a chalibradau i'w cadw'n alinedig.
- Gwarchodwch rhag halogiad a gorgymhwyso, neu bydd eich rhifau'n eich gwenieithio tra bo'r system go iawn yn siomi defnyddwyr.
- Gwifriwch werthuso all-lein i mewn i CI fel gât a pharhau i fesur ansawdd a drifft mewn cynhyrchiad, oherwydd gall model a oedd yn dda wrth lansio ddirywio.

## Cyfeiriadau a darllen pellach

- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Lianmin Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*.
- Kishore Papineni et al., *BLEU: A Method for Automatic Evaluation of Machine Translation*.
- Chin-Yew Lin, *ROUGE: A Package for Automatic Evaluation of Summaries*.
- Percy Liang et al., *Holistic Evaluation of Language Models (HELM)*.
- Deep Ganguli et al., *Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- National Institute of Standards and Technology, *AI Risk Management Framework*.
