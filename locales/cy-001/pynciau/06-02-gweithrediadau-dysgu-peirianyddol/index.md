# 6.2 Peirianneg dysgu peiriant (MLOps)

## Trosolwg a chymhelliant

Peirianneg dysgu peiriant, a elwir fel arfer yn [MLOps](https://en.wikipedia.org/wiki/MLOps), yw'r ddisgyblaeth o gymryd [dysgu peiriant](https://en.wikipedia.org/wiki/Machine_learning) allan o lyfrau nodiadau ac arbrofion a'i roi mewn systemau cynhyrchu dibynadwy, arsylladwy, cynaliadwy. Mae meddalwedd traddodiadol yn ymddwyn fel y mae ei god yn dweud y bydd. Mae system DP (dysgu peiriant) yn ymddwyn fel y mae ei chod, ei data, a'i pharamedrau model wedi'u dysgu gyda'i gilydd yn dweud y bydd. Mae hynny'n gwneud systemau DP yn anos i'w profi, yn anos i'w hatgynhyrchu, ac yn dueddol o fethu'n dawel wrth i'r byd ddrifftio i ffwrdd o'r data y cawsant eu hyfforddi arno. Mae MLOps yn dwyn trylwyredd peirianneg meddalwedd (rheolaeth fersiynau, profi, traddodiad parhaus, a monitro) i'r realiti tair-rhan hwn o god ynghyd â data a modelau.

I dimau mawr, MLOps yw'r hyn sy'n gwahanu model unwaith-yn-unig sy'n disgleirio mewn demo oddi wrth fflyd o fodelau y gall llawer o dimau eu hadeiladu, eu defnyddio, a'u gweithredu'n ddiogel. Heb blatfformau ac arferion a rennir, mae pob tîm yn ailddyfeisio piblinellau data, dolenni hyfforddi, a defnyddio, a chi'n dod i ben â systemau bregus na all neb eu hatgynhyrchu chwe mis yn ddiweddarach. Mae mentrau'n dibynnu ar MLOps i raddio ar draws dwsinau o fodelau, bodloni amcanion lefel gwasanaeth, a bodloni archwilwyr sy'n gofyn sut y cynhyrchwyd rhagfynegiad penodol.

Mewn llywodraeth a diwydiannau rheoledig, mae MLOps yn aml yn ofyniad cydymffurfiaeth wedi'i guddio. Atgynhyrchadwyedd, llinach, a fersiynu yw'r hyn sy'n caniatáu i asiantaeth ateb cwestiwn arwyddocaol yn gyfreithiol: pa fodel yn union, wedi'i hyfforddi ar ba ddata, gyda pha god, a gynhyrchodd y penderfyniad a effeithiodd ar ddinesydd? Mae arfer MLOps aeddfed yn cadw'r cwestiwn hwnnw'n atebadwy flynyddoedd yn ddiweddarach, sy'n beirianneg dda ac yn amddiffyniad cyfreithiol fel ei gilydd.

*Gweler hefyd:* pennod 8.1 (CI/CD a chyflenwi), pennod 9.2 (arsylladwyedd a monitro), a phennod 6.6 (seilwaith a gweithrediadau AI).

## Egwyddorion allweddol

- Trinnwch ddata, cod, a modelau fel arteffactau wedi'u fersiynu ar y cyd; mae newid unrhyw un yn newid ymddygiad y system.
- Awtomeiddiwch y llwybr o ddata i fodel wedi'i hyfforddi i ddefnyddio fel ei fod yn ailadroddadwy ac yn archwiliadwy.
- Gwnewch bob model yn olrheiniadwy i'r union ddata, cod, a ffurfweddiad a'i cynhyrchodd.
- Gwerthuswch fodelau yn erbyn data cynrychioliadol, wedi'i gadw'n ôl, cyn defnyddio, a pharhewch i werthuso wedyn.
- Tybiwch fod modelau'n dirywio; monitrwch am ddrifft (y dargyfeiriad graddol o ddata byw neu berthnasoedd mewnbwn-allbwn oddi wrth yr hyn yr hyfforddwyd y model arno), problemau ansawdd data, a phydredd perfformiad o'r diwrnod cyntaf.
- Ffafriwch biblinellau diflas, atgynhyrchadwy dros arbrofion clyfar, anatgynhyrchadwy.
- Gwahanwch bryderon cyflymder arbrofi a dibynadwyedd cynhyrchu, a phontiwch nhw'n fwriadol.

## Argymhellion

### Rheoli'r cylch bywyd DP cyfan yn benodol

Diffiniwch ac offrynwch bob cam: mewngludo a dilysu data, [peirianneg nodweddion](https://en.wikipedia.org/wiki/Feature_engineering), hyfforddi, gwerthuso, defnyddio, a monitro. Gwnewch y ffiniau rhwng camau'n benodol fel y gellir profi, ailgeisio, ac archwilio pob un. Osgowch y methiant cyffredin lle mae model yn cael ei hyfforddi mewn llyfr nodiadau ad hoc a'i daflu dros y wal i weithrediadau. Yn lle hynny, lapiwch y cylch bywyd mewn piblinell gerddorfaol y gall unrhyw beiriannydd awdurdodedig ei rhedeg o siec-allan lân.

### Defnyddio storfeydd nodweddion, olrhain arbrofion, a chofrestrfeydd model

Mae **storfa nodweddion** yn canoli diffiniadau nodweddion fel bod yr un trawsnewidiadau'n rhedeg mewn hyfforddi a gwasanaethu fel ei gilydd. Mae hyn yn dileu sgiw hyfforddi-gwasanaethu (anghysondebau rhwng sut y cyfrifir nodweddion ar gyfer hyfforddi yn erbyn ar gyfer rhagfynegiadau byw), ac mae'n gadael i dimau ailddefnyddio nodweddion yn hytrach na'u hail-gyfrifo. Mae **olrhain arbrofion** yn cofnodi paramedrau, fersiwn cod, fersiwn data, a metrigau pob rhediad hyfforddi, fel bod canlyniadau'n gymharadwy ac yn atgynhyrchadwy. Mae **cofrestrfa model** yn system gofnod ar gyfer modelau wedi'u hyfforddi, yn dal fersiynau, llinach, canlyniadau gwerthuso, statws cymeradwyo, a cham defnyddio. Gyda'i gilydd, mae'r rhain yn gadael i chi ateb "beth newidiodd?" pan fydd ymddygiad yn symud, a hyrwyddo neu ddychwelyd modelau drwy gamau a lywodraethir.

### Gwneud data a modelau'n atgynhyrchadwy ac wedi'u fersiynu gyda llinach

Fersiynwch eich setiau data, nid dim ond eich cod. Defnyddiwch storfa y gellir ei chyfeirio yn ôl cynnwys neu declynnau fersiynu data fel bod rhediad hyfforddi'n cyfeirio at gipolwg anghyfnewidiol. Pinniwch god gydag ymrwymiadau git, a phinniwch amgylcheddau gyda dibyniaethau wedi'u cloi a delweddau cynhwysydd. Daliwch linach o'r dechrau i'r diwedd: pa ddata crai a fwydodd pa nodweddion, pa nodweddion a chod a gynhyrchodd pa fodel, a lle mae'r model hwnnw wedi'i ddefnyddio. Pan fydd digwyddiad neu archwiliad yn taro, mae llinach yn troi hunllef fforensig yn ymholiad syml. Cofnodwch ar hap (hadau) a chaledwedd lle bynnag y mae canlyniadau'n dibynnu arnynt.

### Dewis patrymau defnyddio i gyd-fynd â'r llwyth gwaith

- Mae sgorio **swp** yn rhedeg ar amserlen dros setiau data mawr; symlaf i'w weithredu, goddefgar o oedi, delfrydol ar gyfer adroddiadau a phenderfyniadau cyfnodol.
- Mae gwasanaethu **ar-lein (amser real)** yn ymateb i geisiadau unigol o fewn cyllidebau oedi tynn; mae angen adalw nodweddion oedi isel a chynllunio capasiti gofalus.
- Mae **ffrydio** yn sgorio digwyddiadau'n barhaus wrth iddynt gyrraedd; addas ar gyfer canfod twyll a monitro lle mae ffresni'n hollbwysig.
- Mae **ymyl (edge)** yn rhedeg modelau ar ddyfeisiau neu galedwedd ar-safle am resymau oedi, preifatrwydd, cysylltedd, neu sofraniaeth data, yn gyffredin mewn cyd-destunau llywodraeth a maes.

Dewiswch y patrwm symlaf sy'n bodloni'r gofyniad, a dyluniwch eich cyflwyniad gyda defnyddiadau cysgod, caneri, a dychwelyd ar unwaith.

### Monitro am ddrifft, dirywiad, ac ansawdd data

Offrynwch fewnbynnau ac allbynnau mewn cynhyrchu. Gwyliwch am **ddrifft data** (dosraniadau mewnbwn yn symud), **[drifft cysyniad](https://en.wikipedia.org/wiki/Concept_drift)** (y berthynas rhwng mewnbynnau a'r targed yn newid), methiannau **ansawdd data** (gwerthoedd nwl, newidiadau sgema, ffynonellau i fyny'r afon wedi torri), a **dirywiad perfformiad** wedi'i fesur yn erbyn gwirionedd sylfaen wedi'i oedi lle mae gennych un. Gosodwch drothwyon rhybudd, ysgrifennwch lawlyfrau rhedeg, a chysylltwch fonitro â'ch sbardunau ail-hyfforddi. Dirywiad tawel yw'r modd methiant DP clasurol, a monitro yw eich unig amddiffyniad yn ei erbyn.

## Cyfaddawdau: manteision ac anfanteision

| Penderfyniad | Opsiwn A | Opsiwn B | Cyfaddawd |
|---|---|---|---|
| Patrwm gwasanaethu | Swp | Ar-lein | Symlrwydd a chost yn erbyn ffresni ac oedi |
| Cyfrifo nodweddion | Storfa nodweddion | Piblinellau fesul model | Cysondeb ac ailddefnydd yn erbyn gorbenion sefydlu |
| Platfform | Prynu platfform MLOps a reolir | Cydosod offer cod agored | Cyflymder a chymorth yn erbyn hyblygrwydd a chlymu-i-werthwr |
| Ail-hyfforddi | Wedi'i drefnu | Wedi'i sbarduno gan ddrifft | Rhagweladwyedd yn erbyn ymatebolrwydd a chymhlethdod |
| Trylwyredd atgynhyrchadwyedd | Fersiynu data llawn | Olrhain ysgafn | Cryfder archwilio yn erbyn storio ac ymdrech |

Y cyfaddawd trosfwaol yw buddsoddiad nawr yn erbyn breuder yn ddiweddarach. Mae seilwaith atgynhyrchadwyedd a monitro trwm yn costio ymdrech ymlaen llaw, ond maent yn atal cost lawer mwy methiannau anesboniadwy, modelau anatgynhyrchadwy, ac ymddiriedaeth wedi'i erydu. Mae platfformau a reolir yn cyflymu timau ond gallant greu clymu-i-werthwr; mae staciau cod agored yn cynnig rheolaeth am bris gwaith integreiddio. Mae sefydliadau mawr fel arfer yn elwa o dîm platfform a rennir sy'n cuddio'r cymhlethdod hwn y tu ôl i ddiofynion ffordd-wedi'i-phalmantu.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Sut fyddem yn dysgu bod model wedi'i ddefnyddio wedi dirywio'n dawel cyn i gwsmer neu ddinesydd gael ei niweidio, a phwy sy'n berchen ar y rhybudd hwnnw?** Pydredd tawel yw'r modd methiant DP clasurol: mae'r cod yn dal i redeg, mae'r model yn dal i ddychwelyd sgoriau hyderus, a mae ansawdd yn llithro wrth i'r byd ddrifftio oddi wrth y data hyfforddi. I dîm mawr sy'n rhedeg llawer o fodelau, mae angen ateb hyn fesul model, nid unwaith ar gyfer y fflyd, oherwydd bod gan bob un ei broffil drifft ei hun a'i oedi gwirionedd sylfaen ei hun. Dewch â'ch monitorau presennol ar gyfer drifft data, drifft cysyniad, a thoriadau ansawdd data, y trothwyon rhybudd, a'r llawlyfr rhedeg sy'n dweud pwy sy'n ymateb. Mewn cyd-destunau rheoledig lle mae labeli'n cyrraedd wythnosau'n hwyr, trafodwch signalau dirprwy y gallwch eu gwylio yn y cyfamser, oherwydd mae aros am wirionedd sylfaen wedi'i oedi yn golygu aros i ddarganfod niwed. Os na enwir un perchennog ar gyfer rhybudd drifft model, mae'r model hwnnw'n effeithiol heb ei fonitro.

2. **Pe bai archwilydd yn gofyn i ni atgynhyrchu rhagfynegiad penodol o ddeunaw mis yn ôl, a allem ei wneud mewn gwirionedd o'r dechrau i'r diwedd?** Atgynhyrchadwyedd yw'r gofyniad cydymffurfiaeth sy'n cuddio y tu mewn i beirianneg dda: mae'n caniatáu i asiantaeth ateb pa fodel yn union, wedi'i hyfforddi ar ba ddata, gyda pha god, a gynhyrchodd benderfyniad a effeithiodd ar rywun. Dewch ag enghraifft wirioneddol a cheisiwch ei holrhain: y cipolwg data anghyfnewidiol, yr ymrwymiad git, y dibyniaethau wedi'u cloi a'r ddelwedd gynhwysydd, yr hadau a gofnodwyd, a'r llinach o ddata crai drwy nodweddion i'r model wedi'i ddefnyddio. Y signal yw a yw unrhyw gyswllt yn y gadwyn honno ar goll neu'n llaw. Ar gyfer diwydiannau llywodraeth a rheoledig, penderfynwch y cyfnod cadw y mae'r gyfraith mewn gwirionedd yn ei ofyn a chadarnhewch fod eich storfa'n cadw llinach yn atebadwy dros y ffenestr gyfan honno, gan fod bwlch yn troi ymholiad rheolaidd yn argyfwng fforensig.

3. **Beth yw ein rheol ar gyfer hyrwyddo model i gynhyrchu a'i ddychwelyd, ac a orfodir hi gan y gofrestrfa neu dim ond gan ymddiriedaeth?** Hyrwyddo heb ei lywodraethu yw sut mae arbrofion llyfr nodiadau yn gollwng i mewn i gynhyrchu a sut mae model gwael yn parhau oherwydd na all neb ei wrthdroi'n lân. I lawer o dimau, y gwahaniaeth rhwng aeddfed a bregus yw a yw'r gofrestrfa fodelau'n giatio hyrwyddo gyda chymeradwyaeth a gwerthusiad gorfodol, neu a all peiriannydd wthio pwysau â llaw. Dewch â'ch llwybr hyrwyddo presennol, eich mecanwaith dychwelyd, a thystiolaeth bod defnyddiadau cysgod neu ganeri'n rhedeg mewn gwirionedd cyn traffig llawn. Trafodwch a yw ail-hyfforddi wedi'i drefnu neu wedi'i sbarduno gan ddrifft, ac a yw modelau wedi'u hail-hyfforddi'n pasio giatiau dilysu cyn defnyddio, oherwydd mae ail-hyfforddi ar ddata byw heb ddilysu yn chwyddo drifft neu wenwyno. Dylai'r ateb gael ei orfodi yn y platfform, nid mewn tudalen wici y mae pobl yn cael eu hymddiried i'w dilyn.

4. **Ydym yn adeiladu ein platfform MLOps ar offer cod agored, yn prynu un a reolir, neu'n cyfuno'r ddau, a phwy sydd wedi pwyso'r clymu-i-werthwr?** Mae'r dewis hwn yn gosod y nenfwd ar ba mor gyflym y bydd pob model yn y dyfodol yn cael ei ddefnyddio a faint o reolaeth rydych yn ei chadw dros eich data a'ch piblinellau. Mae platfform a reolir yn cael timau i gynhyrchu'n gyflym ac yn cario cymorth, ond gall ddal eich diffiniadau nodweddion, cofnodion llinach, ac arteffactau model mewn fformat perchnogol na allwch adael yn hawdd; mae stac cod agored wedi'i gydosod yn eich cadw'n gludadwy am bris llafur integreiddio a chynnal go iawn. Dewch â chost gyfan perchnogaeth pob llwybr (trwydded neu adeiladu, storio, cyfrifiadura ar gyfer ail-hyfforddi, a staff y platfform i'w weithredu), darlleniad gonest o gapasiti eich tîm i redeg seilwaith, a phrawf ymadael diriaethol: a allech allforio eich cofrestrfa, storfa nodweddion, a llinach ac ailadeiladu mewn man arall? Mewn cyd-destunau menter a llywodraeth, ychwanegwch gyfyngiadau caffael a rheolau sofraniaeth data, gan fod platfform sy'n storio data hyfforddi mewn rhanbarth neu fformat y mae eich rheoleiddiwr yn ei wahardd wedi'i ddiarddel ni waeth pa mor gyfleus ydyw.

5. **A ddylai ein storfa nodweddion a'n cofrestrfa fodelau fod yn un platfform canolog neu wedi'u ffedereiddio fesul tîm, a beth mae sgiw hyfforddi-gwasanaethu'n ei gostio i ni heddiw?** Mae canoli diffiniadau nodweddion yn dileu'r sgiw lle caiff nodwedd ei chyfrifo un ffordd mewn hyfforddi ac un ffordd arall mewn gwasanaethu, sy'n ffynhonnell dawel a drud o golli cywirdeb, ond gall un platfform ddod yn dagfa sy'n arafu pob tîm. Mae ffedereiddio'n rhoi ymreolaeth i dimau tra'n lluosi'r plymwaith a'r siawns y bydd dau dîm yn diffinio'r un nodwedd yn anghyson. Dewch â thystiolaeth o ble mae sgiw eisoes wedi'ch brathu, faint o dimau sy'n ailddefnyddio nodweddion yn erbyn eu hailadeiladu, a'r diofynion ffordd-wedi'i-phalmantu y gallai tîm platfform a rennir eu cynnig. I sefydliad mawr, pwyswch fudd llywodraethu un system gofnod archwiliadwy yn erbyn cost gyflenwi ciw canolog, ac mewn cyd-destunau rheoledig ffafriwch y llinach ganolog sy'n gadael i archwilydd olrhain unrhyw ragfynegiad i'r union god nodwedd a'i cynhyrchodd.

6. **Ydym wedi paru patrwm defnyddio pob model â'i anghenion oedi, ffresni, a sofraniaeth gwirioneddol, neu wedi diofynnu popeth i un siâp?** Mae swp, ar-lein, ffrydio, ac ymyl i gyd yn cario cost weithredol a chymhlethdod gwahanol iawn, a mae dewis yr un anghywir naill ai'n gorwario ar seilwaith amser-real nad oedd erioed ei angen ar adroddiad nosweithiol neu'n llwgu sgoriwr twyll o'r ffresni y mae'n dibynnu arno. Penderfynwch fesul llwyth gwaith pa batrwm y mae'r gofyniad mewn gwirionedd yn ei gyfiawnhau, a gwrthsefwch safoni ar yr opsiwn mwyaf cymhleth am ei fod yn teimlo'n fodern. Dewch â'r gyllideb oedi, y cyfaint, cost ateb hen, a'r oedi gwirionedd sylfaen ar gyfer pob model. Mewn cyd-destunau llywodraeth a maes, pwyswch ddefnyddio ymyl ac ar-safle'n fwriadol, oherwydd gall rheolau sofraniaeth data neu gysylltedd ysbeidiol orfodi modelau ar galedwedd lleol, a mae'r dewis hwnnw'n ail-siapio sut rydych yn fersiynu, monitro, a dychwelyd pob model a wthiwch yno.

## Lens sector

**Cwmni newydd.** Eich adnodd prinnaf yw sylw peirianyddol, felly cadwch MLOps yn ysgafn a'i brynu. Trac arbrofion mewn teclyn wedi'i letya syml, pinniwch bob model wedi'i ddefnyddio i'w gipolwg data hyfforddi ac ymrwymiad cod mewn git, ac ychwanegwch un gwiriad drifft rhad yn hytrach na phlatfform. Hepgorwch y storfa nodweddion a phiblinellau pwrpasol nes bod ail neu drydydd model yn gwneud yr ailddefnydd yn werth chweil; bydd stac bregus na allwch ei gynnal yn eich suddo'n gynt na gallu coll.

**Busnes bach.** Mae'n debyg nad oes gennych arbenigwr platfform DP a chyllideb dynn, felly triniwch MLOps fel rhywbeth wedi'i blannu yn yr offer rydych eisoes yn eu rhedeg yn hytrach na system rydych yn ei staffio. Ffafriwch wasanaeth a reolir sy'n trin fersiynu, defnyddio, a monitro ar eich rhan, a fframiwch y ddisgyblaeth fel cwestiwn hylendid data ac atgynhyrchadwyedd: gwybod pa fodel a data a gynhyrchodd ganlyniad penodol, a chadw'r gallu i ddychwelyd. Ffafriwch werthwyr sy'n gadael i chi allforio eich data a'ch modelau fel bod newid diweddarach yn parhau'n bosibl.

**Menter.** Y broblem yw graddfa ar draws dwsinau o fodelau a llawer o dimau: storfa nodweddion a rennir, olrhain arbrofion, a chofrestrfa fodelau gyda hyrwyddo a lywodraethir fel bod grwpiau'n stopio ailddyfeisio piblinellau. Cyllidwch dîm platfform sy'n cynnig diofynion ffordd-wedi'i-phalmantu, safonwch linach a monitro fel bod pob model yn archwiliadwy a phob digwyddiad yn esboniadwy, a rheolwch adeiladu-yn-erbyn-prynu a chlymu-i-werthwr yn fwriadol y tu ôl i ryngwyneb sy'n cadw'r offer sylfaenol yn gyfnewidiadwy. Gorfodwch giatiau dilysu a dychwelyd yn y platfform, nid mewn confensiwn.

**Llywodraeth.** Mae atgynhyrchadwyedd, llinach, a fersiynu'n ofynion cydymffurfiaeth wedi'u cuddio, felly triniwch nhw fel dosbarth-cyntaf o'r diwrnod cyntaf. Fersiynwch yr union set ddata a chod y tu ôl i bob model wedi'i ddefnyddio, cadwch y llinach honno am y cyfnod sy'n ofynnol yn gyfreithiol, a byddwch yn gallu atgynhyrchu unrhyw ragfynegiad hanesyddol a effeithiodd ar ddinesydd. Cadwch berson dynol yn adolygu penderfyniadau canlyniadol, pwyswch ddefnyddio ymyl ac ar-safle lle mae rheolau sofraniaeth data'n ei ofyn, a mynnwch fod unrhyw blatfform gwerthwr yn caniatáu cludadwyedd lawn i'ch data, nodweddion, a llinach.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd dadansoddeg bach yn rhyddhau ei fodel rhagfynegi cwsmeriaid coll cyntaf gydag un gwyddonydd data a sefydliad ysgafn. Roedd yn trac arbrofion mewn teclyn wedi'i letya syml, yn pinnio pob model wedi'i ddefnyddio i'w gipolwg data hyfforddi ac ymrwymiad cod mewn git, ac yn ychwanegu swydd wythnosol sylfaenol a oedd yn cymharu mewnbynnau diweddar â'r dosraniad hyfforddi. Pan newidiodd ffynhonnell ddata ei fformat dyddiad a dechreuodd rhagfynegiadau ddrifftio, daliodd y gwiriad syml hwnnw ef mewn diwrnodau yn hytrach nag ar ôl galwad cwsmer dig, a gallai'r tîm atgynhyrchu'r model da diwethaf a dychwelyd.

**Menter.** Mae banc manwerthu'n rhedeg dwsinau o fodelau credyd a thwyll. Fe safonodd ar storfa nodweddion a rennir ar draws timau, gwasanaeth olrhain arbrofion, a chofrestrfa fodelau gyda giatiau cymeradwyo gorfodol. Mae pob model mewn cynhyrchu'n olrhain yn ôl i'w gipolwg data hyfforddi a'i ymrwymiad cod. Caiff modelau twyll eu defnyddio fel sgorwyr ffrydio; mae modelau credyd yn rhedeg mewn swp. Mae haen fonitro'n gwylio drifft mewnbwn ac yn rhybuddio pan fydd sgema ffynhonnell ddata'n newid, a wnaeth unwaith ddal ffrwd i fyny'r afon wedi torri cyn iddi lygru penderfyniadau.

**Llywodraeth.** Mae asiantaeth budd-daliadau cyhoeddus yn defnyddio model DP i flaenoriaethu adolygiadau achos. Am fod y penderfyniadau hynny'n effeithio ar fynediad dinasyddion at wasanaethau, mae'r asiantaeth yn fersiynu'r union set ddata a chod y tu ôl i bob model wedi'i ddefnyddio, yn cadw'r llinach hon am y cyfnod sy'n ofynnol yn gyfreithiol, ac yn gallu atgynhyrchu unrhyw ragfynegiad hanesyddol ar alw. Caiff modelau eu defnyddio mewn swp gyda pherson dynol yn adolygu achosion wedi'u fflagio, a mae monitor drifft yn gorfodi ail-werthusiad gorfodol pryd bynnag y bydd y boblogaeth sy'n dod i mewn yn symud, fel na chaiff y model byth ei gymhwyso'n dawel y tu allan i'r amodau y'i dilyswyd ar eu cyfer.

## Achos busnes: cymhellion, ROI, a TCO

Mae MLOps yn talu amdano'i hun drwy droi arbrofion bregus yn asedau dibynadwy. Daw ROI o amser-i-gynhyrchu cyflymach ar gyfer modelau newydd, llai o ddigwyddiadau drud, llai o seilwaith dyblyg, a'r gallu i weithredu llawer o fodelau gyda thîm platfform bach. Gall storfa nodweddion a chofrestrfa a rennir dorri amser cyflenwi fesul model yn ddramatig, oherwydd bod timau'n stopio ailadeiladu'r un plymwaith.

Mae TCO'n cwmpasu adeiladu neu drwyddedu platfform, storio ar gyfer data a modelau wedi'u fersiynu, cyfrifiadura ar gyfer ail-hyfforddi, a'r staff i weithredu'r cyfan. Pwyswch hynny yn erbyn cost peidio â mabwysiadu: modelau na allwch eu hatgynhyrchu neu eu harchwilio, methiannau tawel sy'n niweidio cwsmeriaid neu ddinasyddion, a chanfyddiadau rheoleiddiol. Mewn cyd-destunau rheoledig, gall cost model anesboniadwy mewn archwiliad orbwyso'r buddsoddiad MLOps cyfan. Gwnewch yr achos i arweinyddiaeth drwy fframio MLOps fel lleihad risg a chyflymu cyflenwi, nid gorbenion: ffordd wedi'i phalmantu y bydd pob model yn y dyfodol yn teithio arni.

## Gwrth-batrymau a phethau i'w hosgoi

- **Neidiau llyfr-nodiadau-i-gynhyrchu.** Defnyddio modelau wedi'u hyfforddi mewn llyfrau nodiadau heb eu llywodraethu heb atgynhyrchadwyedd.
- **Sgiw hyfforddi-gwasanaethu.** Cod nodwedd gwahanol mewn hyfforddi a gwasanaethu, gan achosi colled cywirdeb dawel.
- **Dim fersiynu data.** Fersiynu cod ond nid data, fel na ellir atgynhyrchu rhediadau.
- **Defnyddio ac anghofio.** Rhyddhau model heb fonitro, gan ddarganfod dirywiad dim ond pan fydd defnyddwyr yn cwyno.
- **Ail-hyfforddi ar beilot awtomatig.** Ail-hyfforddi'n awtomatig ar ddata byw heb ddilysu, gan chwyddo drifft neu wenwyno.
- **Seilwaith unwaith-yn-unig.** Pob tîm yn adeiladu ei biblinell ei hun, gan luosi cost a breuder.
- **Anwybyddu labeli wedi'u hoedi.** Tybio y gallwch fesur cywirdeb ar unwaith pan fydd gwirionedd sylfaen yn cyrraedd wythnosau'n ddiweddarach.

## Model aeddfedrwydd

1. **Cychwyn.** Adeiledir modelau ad hoc mewn llyfrau nodiadau; defnyddio â llaw; dim fersiynu data na modelau; dim monitro; mae atgynhyrchu rhagfynegiad blaenorol yn ddyfalu.
2. **Datblygu.** Mae rhywfaint o olrhain arbrofion a chofrestrfa fodelau'n ymddangos, ond mae arferion yn amrywio fesul tîm; mae defnyddio'n lled-awtomataidd; mae monitro sylfaenol yn cwmpasu ychydig o fodelau; mae fersiynu data'n rhannol a mae gan y llinach fylchau.
3. **Safoni.** Mae platfform a rennir gyda storfa nodweddion, cofrestrfa, piblinellau atgynhyrchadwy, a llinach o'r dechrau i'r diwedd wedi'i ddogfennu a'i orfodi'n sefydliad-eang; mae monitro am ddrifft ac ansawdd data'n rhedeg ar draws modelau; mae hyrwyddo a dychwelyd yn dilyn llwybr a lywodraethir y mae pob tîm yn ei ddefnyddio.
4. **Rheoli.** Mesurir y fflyd yn erbyn llinellau sylfaen: olrheinir cyfraddau drifft, toriadau ansawdd data, cywirdeb model yn erbyn gwirionedd sylfaen wedi'i oedi, sgiw hyfforddi-gwasanaethu, amser-i-gynhyrchu, a chost weithredu fesul model fel metrigau; gorfodir trothwyon rhybudd a giatiau dilysu ar dystiolaeth, ac adolygir iechyd pob model ar gadence sefydlog gyda pherchennog a enwir.
5. **Cerddorfa.** Caiff y cylch bywyd ei awtomeiddio'n llawn, yn archwiliadwy, ac yn addasol; mae ail-hyfforddi wedi'i sbarduno gan ddrifft yn rhedeg y tu ôl i giatiau dilysu; mae ffyrdd hunanwasanaeth wedi'u palmantu'n gadael i dimau ryddhau'n ddiogel; mae gwerthusiad parhaus yn clymu perfformiad model wrth fetrigau busnes, a mae'r platfform yn integreiddio â chyflenwi, risg, a chydymffurfiaeth fel bod modelau'n cael eu hymddeol, eu disodli, a'u hail-gwmpasu'n rheolaidd wrth i ddata ac amodau symud.

## Syniadau ar gyfer trafodaeth

- Sut ydych chi'n cydbwyso rhyddid arbrofi ag atgynhyrchadwyedd cynhyrchu?
- Beth yw'r sbardun ail-hyfforddi cywir (amserlen, drifft, neu bydredd perfformiad) ar gyfer eich achosion defnydd?
- Am ba mor hir y mae'n rhaid i chi gadw data a llinach model, a beth sy'n gyrru'r gofyniad hwnnw?
- A ddylai storfeydd nodweddion a chofrestrfeydd fod yn blatfformau canolog neu wedi'u ffedereiddio fesul tîm?
- Sut ydych chi'n monitro cywirdeb pan fydd labeli gwirionedd sylfaen yn cyrraedd gydag oedi hir?
- Pryd mae defnyddio ymyl yn werth ei gymhlethdod gweithredol ychwanegol?

## Casgliadau allweddol

- Daw ymddygiad DP o god ynghyd â data a modelau; fersiynwch a llywodraethwch y tri gyda'i gilydd.
- Storfeydd nodweddion, olrhain arbrofion, a chofrestrfeydd yw asgwrn cefn DP atgynhyrchadwy.
- Mae llinach yn gwneud modelau'n archwiliadwy a digwyddiadau'n esboniadwy: hanfodol mewn cyd-destunau rheoledig.
- Dewiswch swp, ar-lein, ffrydio, neu ymyl i gyd-fynd ag anghenion oedi, ffresni, a sofraniaeth.
- Mae modelau'n dirywio; nid yw monitro am ddrifft, ansawdd data, a phydredd yn opsiynol.

## Cyfeiriadau a darllen pellach

- Chip Huyen, *Designing Machine Learning Systems*.
- Andriy Burkov, *Machine Learning Engineering*.
- D. Sculley et al., *Hidden Technical Debt in Machine Learning Systems*.
- Mark Treveil et al., *Introducing MLOps*.
- Valliappa Lakshmanan, Sara Robinson, a Michael Munn, *Machine Learning Design Patterns*.
- Emmanuel Ameisen, *Building Machine Learning Powered Applications*.
