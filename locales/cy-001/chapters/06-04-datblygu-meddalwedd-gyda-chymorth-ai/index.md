# 6.4 Datblygu meddalwedd â chymorth AI

## Trosolwg a chymhelliant

Gall cynorthwywyr codio AI bellach gynhyrchu cod, cwblhau swyddogaethau, ysgrifennu profion, esbonio systemau anghyfarwydd, a'ch helpu i [ailffactora](https://en.wikipedia.org/wiki/Code_refactoring). Wedi'u defnyddio'n dda, maent yn cyflymu gwaith rheolaidd. Maent yn gostwng y rhwystr i ieithoedd a fframweithiau anghyfarwydd. Maent yn cymryd y llafur allan o god sylfaenol ailadroddus.

Wedi'u defnyddio'n wael, maent yn achosi niwed gwirioneddol. Gallant orlifo cod bas â chod sy'n edrych yn gredadwy ond sy'n gynnil anghywir. Gallant gyflwyno tyllau diogelwch, creu agoredrwydd trwyddedu, ac erydu sgiliau'r peirianwyr sy'n pwyso arnynt. Mae datblygu â chymorth AI yn declyn cynhyrchedd gwirioneddol ac yn risg wirioneddol ar yr un pryd. Mae'r gwahaniaeth yn gorwedd bron yn gyfan gwbl yn y ddisgyblaeth beirianneg o'i gwmpas.

I dimau mawr, yr her yw cysondeb a diogelwch ar raddfa fawr. Pan fydd cannoedd o ddatblygwyr yn defnyddio cynorthwywyr AI, mae arferion unigol bach yn adio i ganlyniadau sefydliadol. Os yw pawb yn derbyn awgrymiadau'n ddiwrthwynebiad, mae llwyth adolygu a chyfraddau diffygion yn codi. Os darparwch normau clir, rhagosodiadau da, a gwiriad cryf, mae'r un offer yn codi trwybwn heb ostwng ansawdd. Mae stori'r cynhyrchedd hefyd yn fwy manwl na honiadau gwerthwyr. Mae enillion gwirioneddol yn amrywio'n eang yn ôl tasg, a bydd mesur naïf, fel cyfrif awgrymiadau a dderbyniwyd, yn eich camarwain.

Mae lleoliadau menter a llywodraeth yn ychwanegu cyfyngiadau mwy miniog. Ni ellir ymddiried mewn cod sy'n cyffwrdd â systemau rheoleiddiedig, yn trin data sensitif, neu'n rhedeg seilwaith critigol dim ond am fod AI wedi'i gynhyrchu. Mae tarddiad trwyddedu'n bwysig pan all cod a gynhyrchwyd adleisio data hyfforddi o dan drwyddedau cyfyngol. Rhaid i rai sefydliadau gadw cod ffynhonnell ar-safle ac ni allant ei anfon i wasanaethau allanol o gwbl. Mae gosod normau clir, y gellir eu gorfodi, ar gyfer cymorth AI bellach yn rhan o arweinyddiaeth beirianneg gyfrifol. Ymhlith y cynorthwywyr sydd ar gael, mae offer wedi'u hadeiladu ar fodelau Claude Anthropic yn un dewis blaenllaw ochr yn ochr ag eraill; mae'r arferion isod yn berthnasol pa un bynnag a fabwysiadwch.

*Gweler hefyd:* pennod 2.5 (adolygiad cod a chydweithio), pennod 2.4 (strategaeth brofi), a phennod 6.5 (AI cyfrifol a dibynadwy).

## Egwyddorion allweddol

- Y peiriannydd, nid y cynorthwyydd, sy'n atebol am bob llinell a ymrwymir.
- Mae cod a gynhyrchwyd gan AI yn ddrafft i'w adolygu a'i wirio, byth yn gynnyrch gorffenedig i ymddiried ynddo.
- Dylai ymdrech gwirio raddio â risg y cod, nid â pha mor hyderus y mae'r allbwn yn edrych.
- Mesurwch gynhyrchedd yn ôl canlyniadau sy'n bwysig (gwerth a gyflenwyd, ansawdd, amser cylchred), nid yn ôl cyfrifon awgrymiadau.
- Amddiffynnwch rhag risgiau diogelwch a thrwyddedu a gyflwynir drwy god a gynhyrchwyd.
- Cadwch a thyfwch sgil peirianneg ddynol; peidiwch â gadael i gynorthwywyr ei wagio.
- Byddwch yn dryloyw ynghylch lle a sut y defnyddir cymorth AI.

## Argymhellion

### Defnyddiwch bâr-raglennu AI fel teclyn drafftio ac archwilio

Cyfeiriwch gynorthwywyr at dasgau lle maent yn disgleirio a lle mae camgymeriadau'n rhad i'w dal: cod sylfaenol ailadroddus, sgaffaldio profion, trawsnewidiadau fformat, esbonio cod anghyfarwydd, ac archwilio dulliau. Triniwch eu hallbwn fel drafft cyntaf. Arhoswch yn sedd y gyrrwr. Darllenwch, deallwch, a golygwch bob awgrym yn hytrach na derbyn ar beilot awtomatig. Mewn parthau anghyfarwydd, defnyddiwch y cynorthwyydd i ddysgu, ond gwiriwch ei honiadau yn erbyn dogfennaeth awdurdodol. Gall cynorthwywyr ddyfeisio APIs a chamddatgan ymddygiad â hyder llwyr.

### Adolygwch, profwch, a gwiriwch god a gynhyrchwyd gan AI fel mewnbwn na ellir ymddiried ynddo

Rhowch yr un craffu i god a gynhyrchwyd gan AI ag y byddech yn ei roi i god gan aelod newydd o'r tîm, neu fwy. Dylai adolygwr dynol ei ddeall yn ddigon da i'w esbonio a'i gynnal. Nid yw "yr AI a'i hysgrifennodd" byth yn ateb derbyniol i "pam mae hyn yn gweithio?" Mynnwch brofion, a gwyliwch am brofion a gynhyrchwyd gan AI sydd ddim ond yn honni ymddygiad cyfredol yn hytrach nag ymddygiad bwriadedig. Rhedwch [ddadansoddiad statig](https://en.wikipedia.org/wiki/Static_program_analysis), sganio diogelwch, a gwiriadau dibyniaeth. Ar gyfer cod risg uchel (dilysu, [cryptograffeg](https://en.wikipedia.org/wiki/Cryptography), rhesymeg ariannol, systemau diogelwch), triniwch allbwn AI fel man cychwyn sy'n mynnu gwiriad dynol arbenigol, byth fel awdurdodol.

### Mesurwch gynhyrchedd yn onest a gosodwch ddisgwyliadau realistig

Hepgorwch fesurau balchder fel cyfradd derbyn neu linellau a gynhyrchwyd. Yn lle hynny, edrychwch ar signalau cyflenwi ac ansawdd dros amser: amser cylchred, cyfradd methiant newid, cyfradd dianc diffygion, ac effeithiolrwydd a adroddwyd gan ddatblygwyr. Mae'r enillion yn real ond yn anwastad: mawr ar gyfer rhai tasgau, dibwys neu negyddol ar gyfer eraill. Gellir colli amser a arbedwyd wrth ysgrifennu cod eto wrth ei adolygu a'i ddadfygio. Gosodwch ddisgwyliadau ag arweinyddiaeth yn unol â hynny, fel bod buddsoddiad yn gorffwys ar dystiolaeth yn hytrach na hyp, ac fel na fydd timau byth o dan bwysau i dderbyn awgrymiadau anniogel dim ond i daro mesur.

### Rheolwch risgiau diogelwch a thrwyddedu

Sganiwch god a gynhyrchwyd am wendidau a phatrymau anniogel. Gall cynorthwywyr atgynhyrchu idiomau anniogel o'u data hyfforddi. Peidiwch byth â gludo cyfrinachau, manylion mynediad, neu ddata sensitif i mewn i anogiadau a anfonir at wasanaethau allanol. Ffafriwch offer sy'n bodloni eich gofynion trin data, gan gynnwys defnyddio ar-safle neu breifat lle na all cod ffynhonnell adael yr amgylchedd. Ymdriniwch â thrwyddedu hefyd. Gall cod a gynhyrchwyd debygu i ddata hyfforddi wedi'i drwyddedu, felly defnyddiwch offer a pholisïau sy'n lleihau'r risg hon, cadwch darddiad lle gallwch, a llwybrwch unrhyw beth amheus drwy adolygiad cyfreithiol. Traciwch darddiad y dibyniaethau y mae'r cynorthwyydd yn eu hawgrymu, gan y gall argymell pecynnau wedi'u gadael neu faleisus.

### Gosodwch normau tîm, datgeliad, a chynnal sgiliau

Cyhoeddwch ganllawiau clir ar pryd a sut y gellir defnyddio cymorth AI, pa ddata na ellir byth ei rannu, a pha wiriad y mae angen pob lefel risg amdano. Anogwch dryloywder am gyfraniadau â chymorth AI lle mae'n bwysig ar gyfer adolygu ac atebolrwydd. Cadwch sgiliau dynol yn finiog yn fwriadol. Sicrhewch fod peirianwyr, yn enwedig rhai iau, yn dal i ddysgu'r sylfeini yn hytrach na thrydydd-partïo eu dealltwriaeth. Cylchdrowch bobl drwy waith sy'n adeiladu arbenigedd dwfn, a thriniwch orddibyniaeth fel risg tymor hir wirioneddol i allu'r tîm.

## Cyfaddawdau: manteision ac anfanteision

| Dimensiwn | Budd cymorth AI | Risg cymorth AI |
|---|---|---|
| Cyflymder | Cod sylfaenol a drafftio cyflymach | Amser a gollwyd yn adolygu cod anghywir |
| Sefydlu | Mynediad haws i ieithoedd/fframweithiau newydd | Dealltwriaeth arwynebol, APIs wedi'u dyfeisio |
| Ansawdd | Mwy o brofion, ailffactora cyflymach | Cod credadwy ond cynnil anghywir |
| Diogelwch | Gall awgrymu triniaethau a sganio | Gall gyflwyno gwendidau |
| Sgiliau | Rhyddhau amser ar gyfer gwaith gwerth uwch | Erydu sylfeini os gorddefnyddir |
| Trwyddedu | Ailddefnyddio cyflymach o batrymau cyffredin | Agoredrwydd tarddiad a thrwydded |

Y prif gyfaddawd yw cyflymder yn erbyn gwiriad. Mae AI'n symud ymdrech o ysgrifennu i adolygu. Mae'r enillion net yn dibynnu ar a yw eich arferion adolygu a gwirio'n ddigon cryf i ddal yr hyn y mae'r cynorthwyydd yn ei gael yn anghywir. Mae adolygiad gwan yn arwain at ddirywiad ansawdd. Mae adolygiad cryf a normau clir yn dal y fantais.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Pa rannau o'n cod bas sydd oddi ar y ffiniau i gymorth AI yn llwyr, a sut ydym yn gorfodi'r ffin honno?** Mae ymddiriedaeth unffurf yn fagl: mae cymhwyso'r un craffu ysgafn i ddilysu, cryptograffeg, rhesymeg ariannol, a systemau diogelwch ag i god sylfaenol yw sut mae gwallau cynnil, hyderus yn cyrraedd llwybrau critigol. I dîm mawr, mae rhestr eglur o fodiwlau wedi'u heithrio neu adolygiad-arbenigol-yn-unig yn troi barn unigol yn warchodaeth sefydliadol. Dewch â'ch map risg o'r cod bas, eich polisi presennol (os oes un), a sut y byddech mewn gwirionedd yn atal cod a gynhyrchwyd rhag glanio mewn modiwl cyfyngedig: gwiriadau piblinell, rheolau perchnogaeth, neu gatiau adolygu. Mewn lleoliadau amddiffyn, rheoleiddiedig, a diogelwch-critigol, dylai rhai modiwlau eithrio cymorth AI yn llwyr. Dylai'r ateb raddio ymdrech gwirio yn ôl risg y cod, byth yn ôl pa mor hyderus y mae'r allbwn yn edrych.

2. **Beth yw ein tueddiadau gwirioneddol methiant newid a dianc diffygion ers i ni fabwysiadu cynorthwywyr, ac a ydym yn eu mesur neu'n dyfalu?** Mae honiadau cynhyrchedd gwerthwyr a chyfrifon cyfradd dderbyn yn fesurau balchder sy'n camarwain, gan y gellir colli amser a arbedwyd wrth ysgrifennu cod eto wrth ei adolygu a'i ddadfygio. I arweinyddiaeth fuddsoddi ar dystiolaeth yn hytrach na hyp, mae angen signalau cyflenwi ac ansawdd dros amser arnoch: amser cylchred, cyfradd methiant newid, cyfradd dianc diffygion, ac effeithiolrwydd a adroddwyd gan ddatblygwyr. Dewch â pha rifau gwirioneddol bynnag sydd gennych, a byddwch yn onest lle nad oes gennych ddim. Y risg i'w gwylio yw timau o dan bwysau i dderbyn awgrymiadau anniogel dim ond i daro mesur. Dylai'r ateb ddisodli cyfrifon awgrymiadau â mesurau canlyniad, a gosod disgwyliadau bod yr enillion yn real ond yn anwastad, yn fawr ar gyfer rhai tasgau ac yn negyddol ar gyfer eraill.

3. **Os yw cod a gynhyrchwyd yn adleisio data hyfforddi wedi'i drwyddedu'n gyfyngol neu'n tynnu i mewn ddibyniaeth beryglus, pwy sy'n ei ddal a phryd?** Gall cod a gynhyrchwyd debygu i ddeunydd wedi'i drwyddedu neu argymell pecynnau wedi'u gadael neu faleisus, ac mae'r agoredrwydd hwnnw'n glanio yn eich cynnyrch p'un a sylwodd unrhyw un ai peidio. I fentrau a llywodraeth, mae tarddiad trwyddedu a risg cadwyn gyflenwi'n cario pwysau cyfreithiol nad yw ysgwyd ysgwyddau "yr AI a'i hysgrifennodd" yn ei oroesi. Dewch â'ch sganio cyfrinachau presennol, gwiriadau trwydded, ac olrhain tarddiad dibyniaethau, a nodwch lle yn y biblinell y mae pob un yn rhedeg. Trafodwch beth sy'n llwybro cod amheus i adolygiad cyfreithiol a phwy sy'n berchen ar y penderfyniad hwnnw. Os gellir gludo cyfrinachau i offer allanol neu os gall pecynnau heb eu gwirio uno heb eu herio, caewch y bylchau hynny cyn graddio defnydd cynorthwyydd ar draws y tîm.

4. **Sut ydym yn cadw peirianwyr, yn enwedig rhai iau, yn dysgu'r sylfeini yn hytrach na thrydydd-partïo eu dealltwriaeth i'r cynorthwyydd?** Mae dirywiad sgiliau'n risg araf nad yw byth yn ymddangos yng nghyflymder y chwarter hwn, yna'n ymddangos flynyddoedd yn ddiweddarach fel tîm na all ddadfygio, dylunio, nac adolygu heb anogiad. I sefydliad mawr, mae'r tyniad cystadleuol yn real: mae cynorthwywyr yn caniatáu i beirianwyr iau ryddhau'n gyflymach heddiw, ac mae'r pwysau i daro targedau cyflenwi'n ymladd yn erbyn gwaith arafach adeiladu arbenigedd dwfn. Dewch â thystiolaeth ar sut mae eich pobl mewn gwirionedd yn tyfu: pa gyfran o beirianwyr iau all esbonio'r cod a unwyd ganddynt, faint o ddatrys problemau heb gymorth y mae eich sefydlu'n dal ei angen, ac a yw adolygiadau'n dal dealltwriaeth arwynebol neu ddim ond yn stampio'n rwber allbwn sy'n gweithio. Cylchdrowch bobl yn fwriadol drwy waith sy'n adeiladu meistrolaeth, a thriniwch orddibyniaeth fel risg gallu, nid methiant personol. Mewn llywodraeth a systemau critigol hirhoedlog, efallai y bydd angen i'r gweithlu adeiladu a gwirio systemau am ddegawdau heb offer gwerthwr, felly mae llwybr hyfforddi sy'n gwarantu sylfeini uniongyrchol yn ofyniad parhad, nid rhywbeth braf i'w gael.

5. **Pa gynorthwywyr y caniateir i ni eu defnyddio mewn gwirionedd o ystyried lle mae'n rhaid i'n cod ffynhonnell a'n data aros, a sut ydym yn atal cyfrinach rhag cyrraedd anogiad byth?** Mae cyfyngiadau trin data'n penderfynu'r teclyn cyn i gynhyrchedd wneud: gall cynorthwyydd sy'n ffrydio eich ffynhonnell i wasanaeth allanol gael ei ddiarddel yn llwyr, beth bynnag yw ei alluoedd. I dîm mawr, mae'r tyndra rhwng cyfleustra'r teclyn gwestiedig gorau a'r gofyniad na fydd cod perchnogol, manylion mynediad, a data sensitif byth yn gadael eich ffin. Dewch â'ch map dosbarthu data, y dewisiadau defnyddio y mae pob teclyn ymgeisiol yn eu cynnig (gwestiedig, preifat, ar-safle), a'r rheolaethau pendant sy'n cadw cyfrinachau allan o anogiadau: sganio cyn-ymrwymo, hidlo anogiadau, a hyfforddiant peirianwyr. Penderfynwch pa offer a ganiateir ar gyfer pa ddosbarthiadau o god, a gwnewch y ffin yn orfodadwy yn hytrach na chynghorol. Mewn lleoliadau rheoleiddiedig, amddiffyn, a dosbarthedig, efallai mai defnyddio ar-safle neu wedi'i ynysu'n llwyr yw'r unig opsiwn cyfreithlon, a rhaid gwahardd anfon ffynhonnell i unrhyw wasanaeth allanol a'i rwystro'n dechnegol, nid dim ond ei anghymell.

6. **Sut ydym yn troi arferion unigol gwasgaredig yn normau cyson ar draws y sefydliad, a phwy sy'n berchen ar y polisi wrth i offer esblygu?** Pan fydd cannoedd o ddatblygwyr bob un yn byrfyfyrio eu dull eu hunain, mae arferion bach yn cyfansymio'n ganlyniadau sefydliadol, a dyna lle mae gwiriad anghyson yn caniatáu i ddiffygion ac agoredrwydd lithro drwodd. Yr ystyriaeth gystadleuol yw annibyniaeth: mae timau'n casáu mandadau canolog trwm, ac eto mae rhyddid-i-bawb yn cynhyrchu ansawdd anwastad a dim gwarchodaeth a rennir. Dewch â'ch canllawiau presennol (os oes rhai), tystiolaeth o ba mor unffurf y'u dilynir, a chynnig ar gyfer rhagosodiadau da wedi'u pobi i mewn i'r biblinell fel mai'r llwybr diogel yw'r llwybr hawdd. Enwch berchennog sy'n cadw'r polisi'n gyfredol wrth i gynorthwywyr newid bob ychydig fisoedd, a norm datgelu fel bod adolygwyr yn gwybod pryd y llywiodd cymorth AI gyfraniad. I fenter neu gorff cyhoeddus, clymwch y normau wrth archwilio ac atebolrwydd: mae safon wedi'i dogfennu, wedi'i gorfodi y gall archwiliwr ei harchwilio'n curo arfer gwerin sy'n amrywio fesul tîm ac yn diflannu pan fydd person allweddol yn gadael.

## Lens sector

**Cwmni newydd.** Â llond llaw o beirianwyr a dim rhedfa i'w gwastraffu, pwyswch ar gynorthwywyr gwestiedig ar gyfer cod sylfaenol, profion, a fframweithiau anghyfarwydd, a gadewch iddynt gyflymu gwaith rheolaidd. Cadwch un rheol na ellir ei negodi: mae person dynol sy'n deall y newid yn adolygu pob uniad, gan nad oes gan linell anghywir gynnil mewn cod bas pum person unlle i guddio ac neb arall i'w dal. Ychwanegwch sganiwr cyfrinachau a gwiriad trwydded yn gynnar; maent yn rhad ac maent yn atal camgymeriadau drud na allwch fforddio eu glanhau'n nes ymlaen.

**Busnes bach.** Yn ôl pob tebyg nid oes gennych arbenigwr diogelwch a chyllideb dynn, felly ffafriwch gynorthwywyr wedi'u mewnosod mewn offer rydych eisoes yn ymddiried ynddynt dros osodiad pwrpasol y mae'n rhaid i chi ei gynnal. Fframiwch y risg mewn termau plaen: peidiwch byth â gludo data cwsmeriaid neu fanylion mynediad i mewn i anogiad allanol, a thriniwch god a gynhyrchwyd sy'n cyffwrdd â bilio neu ddilysu fel drafft i'w wirio, nid ateb gorffenedig. Dewiswch werthwyr y gallwch mewn gwirionedd ddarllen eu telerau trin data a diffodd eu nodweddion AI os ydynt yn camymddwyn.

**Menter.** Y broblem yw cysondeb a diogelwch ar draws llawer o dimau: normau a rennir yn ôl lefel risg, adolygu a sganio gorfodol yn y biblinell, a mesurau cyflenwi-ac-ansawdd gonest yn hytrach na chyfrifon derbyn. Safonwch y dewisiadau offer a'r model defnyddio fel bod cod perchnogol yn aros y tu mewn i'ch ffin, cyllidebwch y gost adolygu a chywiro y mae cynorthwywyr yn ei symud ar adolygwyr, a hepgorwch neu gatiwch fodiwlau risg uchel yn benodol. Rheolwch gymorth AI fel gallu wedi'i lywodraethu ag perchennog, nid gwasgariad o arferion unigol.

**Llywodraeth.** Mae rheolau caffael, tryloywder, ac atebolrwydd cyhoeddus yn llunio pob dewis. Ffafriwch ddefnyddio ar-safle neu breifat lle na all cod ffynhonnell a data sensitif adael yr amgylchedd, gwaherddwch anfon cod i wasanaethau allanol, a mynnwch ddatgeliad cyfraniadau â chymorth AI fel bod penderfyniadau'n aros yn archwiliadwy. Mynnwch sganiau diogelwch a thrwyddedu ar bob cod a gynhyrchwyd, hepgorwch gymorth AI o fodiwlau diogelwch-critigol a dosbarthedig, a chadwch lwybr hyfforddi sy'n sicrhau y gall y gweithlu cyhoeddus adeiladu a gwirio systemau heb offer gwerthwr dros oes hir y systemau y mae'n berchen arnynt.

## Enghreifftiau

**Cwmni newydd.** Mabwysiadodd cwmni newydd SaaS chwe pheiriannydd gynorthwywyr codio AI i symud yn gyflymach ar waith rheolaidd. Pwysodd arnynt ar gyfer cod sylfaenol, profion, a chod fframwaith anghyfarwydd, ond cadwodd reol gadarn bod yn rhaid i berson dynol a ddeallai'r newid adolygu pob cais tynnu, ac ychwanegodd sganiwr cyfrinachau a gwiriad trwydded i'r biblinell. Ar gyfer y cod bilio a dilysu, trin peirianwyr allbwn AI fel drafft bras i'w wirio linell wrth linell yn hytrach nag ymddiried ynddo. Gwylion nhw amser cylchred a diffygion a ddihangodd yn hytrach na chyfrif awgrymiadau a dderbyniwyd, a chadwon nhw'r enillion heb adael i ansawdd lithro.

**Menter.** Cyflwynodd cwmni e-fasnach mawr gynorthwywyr codio AI â chanllawiau diogelwch. Gwaharddodd gyfrinachau mewn anogiadau. Mynnodd adolygiad dynol, gyda disgwyl i'r adolygydd ddeall y cod. Ychwanegodd sganio diogelwch yn y biblinell a dewisodd ddefnyddio preifat fel na fyddai cod perchnogol byth yn gadael ei amgylchedd. Mesurodd effaith drwy amser cylchred a chyfradd methiant newid yn hytrach na chyfrifon derbyn. Canfu enillion cadarn ar god sylfaenol a phrofion, ond mynnodd adolygiad arbenigol ar gyfer cod taliadau, lle triniodd allbwn AI fel na ellid ymddiried ynddo.

**Llywodraeth.** Caniataodd sefydliad meddalwedd amddiffyn gymorth AI dim ond drwy declyn ar-safle a gadwodd god dosbarthedig a sensitif y tu mewn i'w ffin. Gwaharddodd anfon ffynhonnell i unrhyw wasanaeth allanol. Mynnodd ddatgeliad cyfraniadau â chymorth AI mewn adolygiad cod a mynnodd sganiau diogelwch a thrwyddedu ar bob cod a gynhyrchwyd. Hepgorodd gymorth AI yn llwyr o rai modiwlau diogelwch-critigol. Dilynodd peirianwyr iau lwybr hyfforddi a sicrhaodd eu bod yn dysgu sylfeini'n uniongyrchol, fel na fyddai'r gweithlu'n colli'r gallu i adeiladu a gwirio systemau heb gymorth.

## Achos busnes: cymhellion, ROI, a TCO

Y cymhelliad yw cyflenwi cyflymach a llai o lafur, fel y gall eich talent peirianneg prin ganolbwyntio ar ddylunio, barn, a phroblemau anodd. Mae ROI'n ymddangos fel amser cylchred llai ar gyfer tasgau addas a phrofiad datblygwr gwell, ond dim ond lle mae gwiriad yn cadw ansawdd yn uchel. Mae honiadau ROI naïf wedi'u seilio ar gyfrifon awgrymiadau'n gamarweiniol, a dylech eu gwrthod.

Mae TCO'n cynnwys trwyddedu offer, defnyddio diogel neu ar-safle, sganio diogelwch a thrwyddedu, a chost aml-ei-thanamcangyfrif adolygu a chywiro allbwn AI. Mae cost *peidio â* mabwysiadu'n gystadleuol: gall cymheiriaid gyflenwi'n gyflymach a denu talent sy'n disgwyl offer modern. Cost mabwysiadu'n ddifeddwl yw erydiad ansawdd, digwyddiadau diogelwch, ac agoredrwydd cyfreithiol. Gwnewch yr achos i arweinyddiaeth â pheilot sy'n mesur canlyniadau cyflenwi ac ansawdd gwirioneddol, wedi'i barau â chynllun pendant ar gyfer normau, gwiriad, a diogelu data.

## Gwrth-batrymau a pheryglon

- **Derbyn peilot awtomatig.** Ymrwymo awgrymiadau heb eu darllen na'u deall.
- **Mesurau balchder.** Barnu llwyddiant yn ôl cyfradd dderbyn neu linellau a gynhyrchwyd.
- **Cyfrinachau mewn anogiadau.** Gludo manylion mynediad neu ddata sensitif i mewn i offer allanol.
- **Ymddiried mewn profion AI.** Derbyn profion a gynhyrchwyd sy'n cloi ymddygiad cyfredol i mewn, nid ymddygiad bwriadedig.
- **Anwybyddu tarddiad.** Anwybyddu risgiau trwydded a dibyniaeth mewn cod a gynhyrchwyd.
- **Dirywiad sgiliau.** Gadael i beirianwyr iau drydydd-partïo dealltwriaeth a byth ddysgu sylfeini.
- **Ymddiriedaeth unffurf.** Cymhwyso'r un craffu isel i god diogelwch-critigol ag i god sylfaenol.

## Model aeddfedrwydd

1. **Cychwyn.** Mae unigolion yn defnyddio cynorthwywyr yn ad hoc ac yn adweithiol; dim polisi, dim mesur; mae cyfrinachau a phiau deallusol mewn perygl, ac mae cod a gynhyrchwyd yn uno â pha graffu bynnag y mae'n digwydd i bob person ei gymhwyso.
2. **Datblygu.** Mae canllawiau defnydd sylfaenol a rheolau data'n bodoli, ac mae rhywfaint o sganio diogelwch yn rhedeg, ond mae arfer yn anghyson ar draws timau: mae dyfnder gwiriad yn amrywio yn ôl person, mae honiadau cynhyrchedd yn anecdotaidd, ac ni chaiff cod risg uchel ei gatio'n ddibynadwy.
3. **Safoni.** Mae normau yn ôl lefel risg wedi'u dogfennu a'u gorfodi ar draws y sefydliad: adolygiad dynol gorfodol, sganiau diogelwch a thrwyddedu yn y biblinell, defnyddio diogel neu ar-safle lle bo angen, arferion datgelu, a rhestr eglur o fodiwlau wedi'u heithrio neu adolygiad-arbenigol-yn-unig.
4. **Rheoli.** Mae'r arfer yn cael ei fesur a'i reoli yn erbyn llinellau sylfaen: caiff amser cylchred, cyfradd methiant newid, a chyfradd dianc diffygion eu tracio cyn ac ar ôl mabwysiadu, meintiolir cost adolygu a chywiro, cyfrifir digwyddiadau gollyngiad cyfrinachau ac agoredrwydd trwydded, ac mae penderfyniadau bwrw-ymlaen-neu-beidio ar offer ac ehangu'n gorffwys ar y dystiolaeth honno yn hytrach nag ar honiadau gwerthwyr.
5. **Cyd-drefnu.** Mae cymorth AI'n cael ei wella'n barhaus ac wedi'i integreiddio ar draws y sefydliad: mae gwiriad wedi'i adeiladu i mewn i'r biblinell fel y llwybr diofyn, mae datblygu sgiliau'n fwriadol ac wedi'i tracio, mae polisi'n addasu wrth i offer newid bob ychydig fisoedd, ac mae'r sefydliad yn ail-werthuso, yn disodli, ac yn ailgwmpasu cynorthwywyr yn rheolaidd wrth i'r dystiolaeth a'r darlun risg newid.

## Syniadau i'w trafod

- Sut y dylai gofynion gwiriad wahaniaethu rhwng cod sylfaenol a chod diogelwch-critigol?
- Pa fesurau cynhyrchedd sydd mewn gwirionedd yn adlewyrchu gwerth o gymorth AI yn eich cyd-destun?
- Pryd, os byth, y dylid datgelu cyfraniadau â chymorth AI?
- Sut ydych yn atal erydiad sgiliau, yn enwedig ar gyfer peirianwyr iau?
- Pa gyfyngiadau trin data sy'n llywodraethu pa offer y gallwch eu defnyddio?
- Sut ydych yn rheoli risg trwyddedu a tharddiad o god a gynhyrchwyd?

## Prif gasgliadau

- Mae'r peiriannydd yn parhau'n atebol; drafft na ellir ymddiried ynddo i'w wirio yw allbwn AI.
- Graddiwch wiriad yn ôl risg, a byth ymddiried mewn cod AI diogelwch-critigol heb adolygiad arbenigol.
- Mesurwch ganlyniadau cyflenwi ac ansawdd gwirioneddol, nid cyfrifon awgrymiadau.
- Amddiffynnwch rhag risgiau diogelwch, gollyngiad data, a thrwyddedu â pholisi ac offer.
- Gosodwch normau clir a chadwch sgil peirianneg ddynol yn fwriadol.

## Cyfeiriadau a darllen pellach

- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Andrew Ng, *Machine Learning Yearning* (on realistic expectations and measurement).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Peter Naur, *Programming as Theory Building* (on understanding versus code artifacts).
- Titus Winters, Tom Manshreck, and Hyrum Wright, *Software Engineering at Google*.
- GitClear and related industry studies on AI-assisted code quality trends.
