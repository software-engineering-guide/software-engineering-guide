# 4.1 Sylfeini a diwylliant diogelwch

## Trosolwg a chymhelliant

Nid nodwedd rydych yn ei bolltio ymlaen ar y diwedd yw diogelwch, ac nid gwaith un tîm arbenigol sy'n eistedd ar wahân i beirianneg yw. Mewn sefydliad mawr, priodwedd o sut mae'r system gyfan wedi'i dylunio, ei hadeiladu, ei gweithredu, a'i llywodraethu yw diogelwch. Pan fydd miloedd o beirianwyr yn traddodi cod ar draws cannoedd o wasanaethau, y ddolen wannaf sy'n penderfynu faint o niwed y gall digwyddiad ei wneud. Gall un bwced storio wedi'i gamffurfweddu, dibyniaeth heb ei chlytio, neu gyfrif gwasanaeth â gormod o freintiau ddatgelu miliynau o gofnodion. Sylfeini a diwylliant yw'r hyn sy'n atal hynny rhag digwydd ar raddfa.

I fentrau, mae'r peryglon yn ariannol ac yn enw da: costau toriad, dirwyon rheoleiddiol, cwsmeriaid coll, a phrisiadau isel. I lywodraeth, maent yn ymestyn i ddiogelwch cenedlaethol, ymddiriedaeth gyhoeddus, a pharhad gwasanaethau hanfodol. Mae'r ddau leoliad yn rhannu gwirionedd caled: ni allwch orfodi diogelwch yn bur drwy reolaethau a giatiau. Rhaid iddo gael ei fewnoli gan y bobl sy'n gwneud y gwaith. Mae diwylliant lle mae peirianwyr yn deall bygythiadau, yn teimlo perchnogaeth, ac yn cael eu gwobrwyo am godi pryderon yn cynhyrchu canlyniadau llawer gwell na diwylliant sy'n pwyso ar dîm diogelwch gorweithiog yn chwarae gôl-geidwad.

Mae'r bennod hon yn gosod allan y modelau meddwl a'r arferion diwylliannol sy'n sail i bob pennod ddiogelwch arall yn y canllaw hwn. Mae'n ymdrin â gwneud diogelwch yn waith i bawb, [modelu bygythiad](https://en.wikipedia.org/wiki/Threat_model), y cylch bywyd datblygu diogel, egwyddorion pensaernïol sylfaenol fel [amddiffyn mewn dyfnder](https://en.wikipedia.org/wiki/Defense_in_depth_(computing)) ac [ymddiriedaeth sero](https://en.wikipedia.org/wiki/Zero_trust_security_model), a sut i flaenoriaethu gwaith diogelwch yn ôl risg go iawn yn hytrach nag ofn neu ffasiwn.

*Gweler hefyd:* mae pennod 4.2 (diogelwch cymwysiadau), pennod 4.3 (diogelwch seilwaith a chwmwl), pennod 4.4 (gweithrediadau diogelwch), a phennod 4.6 (cydymffurfiaeth a llywodraethu) yn adeiladu ar y sylfeini hyn.

## Egwyddorion allweddol

- **Gwaith i bawb yw diogelwch.** Mae pob peiriannydd, rheolwr cynnyrch, a gweithredwr yn berchen ar ddiogelwch yr hyn a adeiladant. Mae'r tîm diogelwch yn galluogi, yn cynghori, ac yn archwilio; nid yw'n gwneud, ac ni all wneud, y gwaith ar ei ben ei hun.
- **Tybiwch doriad.** Dyluniwch fel pe bai ymosodwyr eisoes y tu mewn. Lleihewch yr hyn y gall cydran wedi'i pheryglu ei gyrraedd.
- **Amddiffyn mewn dyfnder.** Nid oes yr un rheolaeth sengl yn ddigonol. Haenwch reolaethau annibynnol fel nad yw methiant un yn golygu methiant pob un.
- **[Y fraint leiaf](https://en.wikipedia.org/wiki/Principle_of_least_privilege).** Rhowch y mynediad lleiaf sydd ei angen, am yr amser lleiaf, a'i ddiddymu'n awtomatig pan na fydd ei angen mwyach.
- **Symud i'r chwith.** Canfyddwch a thrwsiwch broblemau mor gynnar â phosibl, pan fyddant rataf i'w hunioni.
- **Blaenoriaethu yn ôl risg.** Treuliwch ymdrech lle mae'r cyfuniad o debygolrwydd ac effaith uchaf, wedi'i lywio gan y driawd CIA (cyfrinachedd, cywirdeb, ac argaeledd), nid ar beth bynnag a wnaeth y newyddion yr wythnos hon.
- **Dysgu di-fai.** Triniwch ddigwyddiadau diogelwch a phethau-a-fu-bron-â-digwydd fel cyfleoedd dysgu, nid achlysuron cosb.

## Argymhellion

### Sefydlwch raglen hyrwyddwyr diogelwch

Mewnblannwch hyrwyddwr diogelwch penodedig ym mhob tîm peirianneg. Nid arbenigwyr diogelwch amser-llawn yw hyrwyddwyr. Peirianwyr ydynt gyda hyfforddiant ychwanegol a llinell uniongyrchol i'r tîm diogelwch canolog. Maent yn adolygu cynlluniau, yn trïo canfyddiadau, yn ateb cwestiynau cydweithwyr, ac yn cario cyd-destun diogelwch i mewn i gynllunio. Mae hyn yn graddio arbenigedd diogelwch ar draws y sefydliad heb gyflogi arbenigwr ar gyfer pob tîm, ac mae'n adeiladu ymddiriedaeth, am fod y cyngor yn dod gan gyfoeswr sydd wir yn adnabod y sylfaen god.

Rhowch gefnogaeth go iawn i hyrwyddwyr: fforwm rheolaidd i rannu'r hyn a ddysgant, cyllideb ar gyfer hyfforddiant a chynadleddau, cydnabyddiaeth mewn adolygiadau perfformiad, ac amser wedi'i neilltuo o'u hymrwymiadau traddodi. Mae rhaglen hyrwyddwyr sy'n bodoli ar bapur yn unig yn cynhyrchu dim.

### Ymarferwch fodelu bygythiad yn rheolaidd

Modelu bygythiad yw'r arferiad disgybledig o ofyn "beth allai fynd o'i le?" cyn i chi adeiladu. Gwnewch hynny ar gyfer gwasanaethau newydd, nodweddion mawr, ac unrhyw newid i ffiniau ymddiriedaeth. Cadwch ef yn ddigon ysgafn fel ei fod mewn gwirionedd yn digwydd yn aml.

- Mae **[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)** yn rhestr wirio ymarferol wedi'i mapio i briodweddau diogelwch: Spoofing (dilysu), Tampering (cywirdeb), Repudiation (di-wadiad), Information disclosure (cyfrinachedd), Denial of service (argaeledd), ac Elevation of privilege (awdurdodi). Ewch drwy bob llif data a gofyn sut mae pob categori'n berthnasol.
- Mae **PASTA** (Process for Attack Simulation and Threat Analysis) yn ddull saith cam trymach, risg-ganolog sy'n clymu bygythiadau technegol wrth effaith fusnes; defnyddiwch ef ar gyfer systemau gwerth uchel.
- Mae **[coed ymosodiad](https://en.wikipedia.org/wiki/Attack_tree)** yn dadelfennu nod ("dwyn data cwsmeriaid") yn y camau canghennog y byddai ymosodwr yn eu cymryd, gan eich helpu i ganfod a thocio llwybrau.

Cadwch fodelau bygythiad fel dogfennau byw wrth ochr y cod, ac ail-ymwelwch â nhw pryd bynnag y bydd y bensaernïaeth yn newid.

### Adeiladwch gylch bywyd datblygu meddalwedd diogel

Plethwch ddiogelwch i mewn i bob cyfnod yn hytrach na'i drin fel giât derfynol:

- **Gofynion:** dalgrynhowch ofynion diogelwch a phreifatrwydd ochr yn ochr â rhai swyddogaethol.
- **Dylunio:** modelwch fygythiad ac adolygwch ffiniau ymddiriedaeth.
- **Gweithredu:** gorfodwch safonau codio diogel, adolygiad cod, a sganio cyfrinachau cyn-ymrwymo.
- **Profi:** rhedwch [SAST](https://en.wikipedia.org/wiki/Static_application_security_testing) (profi diogelwch cymhwysiad statig), [DAST](https://en.wikipedia.org/wiki/Dynamic_application_security_testing) (profi diogelwch cymhwysiad dynamig), a sganio dibyniaeth yn y biblinell (gweler pennod 4.4).
- **Rhyddhau:** gwiriwch darddiad, llofnodwch arteffactau, a gwiriwch ffurfweddiad.
- **Gweithredu:** monitrwch, clytiwch, ac ymatebwch.

Nid pentyrru'r holl waith yn gynharach a llethu peirianwyr yw pwynt symud-i'r-chwith. Ei bwynt yw dal y mathau o nam sy'n llawer rhatach i'w trwsio'n gynnar.

### Mabwysiadwch egwyddorion pensaernïaeth ymddiriedaeth-sero

Mae diogelwch perimedr traddodiadol yn tybio bod popeth y tu mewn i'r rhwydwaith yn ddibynadwy. Mae'r rhagdybiaeth honno'n methu'r eiliad y bydd ymosodwr yn cael troedle. Mae ymddiriedaeth sero'n disodli ymddiriedaeth rhwydwaith ymhlyg â gwiriad eglur, parhaus: dilyswch ac awdurdodwch bob cais yn seiliedig ar hunaniaeth, cyflwr dyfais, a chyd-destun, ni waeth o ble y daw ar y rhwydwaith. Cyfunwch hunaniaeth gref, awdurdodi braint-leiaf, microrannu, ac [amgryptio](https://en.wikipedia.org/wiki/Encryption) ym mhobman. Taith yw ymddiriedaeth sero, nid cynnyrch, felly ewch ato gam ar y tro.

### Blaenoriaethwch yn ôl risg gan ddefnyddio'r triawd CIA

Fframiwch bob ased a rheolaeth o amgylch **Cyfrinachedd**, **Cywirdeb**, ac **Argaeledd**. Nid oes angen yr un amddiffyniad ar bob data: mae gan dudalen farchnata gyhoeddus a chronfa ddata o gofnodion iechyd anghenion cyfrinachedd hollol wahanol. Dosbarthwch eich asedau, amcangyfrifwch debygolrwydd ac effaith perygl, a phwyntiwch ymdrech ddiogelwch brin at y cyfuniadau risg uchaf. Ysgrifennwch eich penderfyniadau risg fel y gall eraill eu hadolygu a'u hamddiffyn yn ddiweddarach.

## Cyfaddawdau: manteision ac anfanteision

| Dull | Manteision | Anfanteision |
|---|---|---|
| Tîm diogelwch canolog yn berchen ar bopeth | Arbenigedd dwfn, safonau cyson | Tagfa, peirianwyr yn datgysylltu, ddim yn graddadwy |
| Diogelwch dosbarthedig (hyrwyddwyr) | Graddadwy, adeiladu perchnogaeth, adborth cyflymach | Angen buddsoddiad, sgil anghyson, angen cydgysylltu |
| Modelu bygythiad trwm ymlaen llaw ar gyfer popeth | Trylwyr, yn dal diffygion dylunio | Yn arafu traddodi, gall droi'n flwch ticio |
| Modelu bygythiad ysgafn, wedi'i dargedu at risg | Cyflym, wedi'i ffocysu ar yr hyn sy'n bwysig | Gall golli bygythiadau mewn systemau "risg isel" |
| Giatiau llym yn rhwystro rhyddhadau | Yn gorfodi cydymffurfiaeth | Ffrithiant, yn annog llwybrau osgoi |

Y tensiwn canolog yw rhwng cyflymder a sicrwydd. Pwyswch yn rhy bell tuag at giatiau a rheolaeth ganolog, a chreu ffrithiant y mae peirianwyr yn mynd o'i gwmpas, gan feithrin TG cysgod a chwerwder. Pwyswch yn rhy bell tuag at ymreolaeth heb gefnogaeth, a chewch ddiogelwch anghyson, heb ei archwilio. Yr ateb cynaliadwy yw diwylliant cryf gyda chledrau amddiffyn galluogol: awtomataidd lle gallwch, dynol lle mae angen barn, a bob amser wedi'i esbonio yn hytrach na dim ond wedi'i orfodi.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Pa rai o'ch systemau sy'n haeddu modelu bygythiad trwm, a phwy sy'n penderfynu'r haen?** Mewn ystâd fawr ni allwch redeg dadansoddiad PASTA saith cam ar bob gwasanaeth, felly mae angen rheol eglur arnoch ar gyfer pryd mae pas STRIDE 30 munud yn ddigon a phryd mae system werth uchel yn haeddu modelu dwfn, wedi'i yrru gan effaith fusnes. Angorwch y penderfyniad yn eich dosbarthiad CIA: mae systemau'n dal cofnodion rheoledig, llifoedd talu, neu resymeg dilysu ar y brig, ac nid yw tudalen farchnata gyhoeddus. Ar gyfer gwaith menter a llywodraeth, bydd archwiliwr yn gofyn i chi amddiffyn pam y modelwyd system benodol fel y gwnaed, felly ysgrifennwch y meini prawf haenu i lawr ac enwch y perchennog sy'n eu cymhwyso. Dewch â'ch dosbarthiad ased presennol a rhestr o wasanaethau heb fodel bygythiad i'r cyfarfod, gan mai'r bwlch rhyngddynt yw eich risg go iawn. Os na allwch gytuno ar y bar, byddwch yn diofyn i fodelu popeth yn ysgafn neu ddim byd yn ddwfn, ac mae'r ddau'n eich siomi.

2. **Pan fydd hyrwyddwr diogelwch a therfyn amser traddodi'n gwrthdaro, pwy sy'n gallu mewn gwirionedd atal y rhyddhad?** Dim ond os yw'r hyrwyddwr yn cario awdurdod go iawn, nid dim ond hyfforddiant ychwanegol a bwriadau da, y mae rhaglen hyrwyddwyr yn newid canlyniadau. Penderfynwch ymlaen llaw a all hyrwyddwr rwystro llong, a ydynt yn uwch-gyfeirio i'r tîm AppSec canolog, a pha ddifrifoldeb canfyddiad sy'n cyfiawnhau atal traddodi yn erbyn ei olrhain. Mae hyn yn bwysicaf o dan bwysau, pan fydd rheolwr cynnyrch eisiau hepgor nam dylunio'r wythnos cyn lansio, sef yn union pan mae diffygion heb eu trin drutaf i'w trwsio. Dewch ag enghraifft ddiweddar lle cyfarfu pryder diogelwch â therfyn amser ac olrheiniwch pwy benderfynodd a sut, gan fod y stori honno'n datgelu eich gwir lwybr uwch-gyfeirio. Os yw'r ateb gonest mai traddodi sydd bob amser yn ennill, mae eich hyrwyddwyr yn addurniadol a dylech drwsio'r cymhelliad cyn ychwanegu mwy ohonynt.

3. **Beth mae "tybio toriad" mewn gwirionedd yn ei newid yn eich adolygiad dylunio nesaf?** Mae'r egwyddor yn hawdd cytuno â hi ac yn anodd ei gweithredu, felly pinniwch hi i ymrwymiadau penodol: pa ffiniau ymddiriedaeth y byddwch yn eu tynhau, ble y byddwch yn ychwanegu microrannu, a sut y byddwch yn crebachu'r hyn y gall un cyfrif gwasanaeth wedi'i beryglu ei gyrraedd. I dîm mawr, yr elw yw lleihau radiws effaith, fel na all ymosodwr sy'n glanio mewn un gwasanaeth droi at y siop ddata y tu ôl iddo. Mewn lleoliadau menter a llywodraeth mae hyn hefyd yn siapio eich penderfyniadau braint-leiaf a chredadwyaeth fyr-oes, sy'n rhad i'w dylunio i mewn ac yn boenus i'w hôl-ffitio. Dewch â diagram gwasanaeth go iawn a gofynnwch beth mae ymosodwr yn ei wneud ar ôl iddynt berchen ar yr haen we, yna ymrwymwch i ddau newid cyfyngu'r chwarter hwn. Mae cytundeb amwys bod toriadau'n digwydd yn ddiwerth oni bai ei fod yn symud caniatâd, rheol rhwydwaith, neu oes credadwyaeth.

4. **Sut fyddwch chi'n gwybod bod eich diwylliant diogelwch mewn gwirionedd yn gwella, a pha fetrig fyddech chi'n ei amddiffyn i'r bwrdd?** Mae cyfraddau cwblhau hyfforddiant a chyfrifon tocynnau'n hawdd eu casglu ac yn agos at ddiwerth, gan eu bod yn mesur gweithgarwch yn hytrach na lleihad risg, ac mae sefydliad mawr yn boddi ynddynt. Dewch â metrigau canlyniad y byddech mewn gwirionedd yn betio cyllideb arnynt: amser canolrifol i unioni canfyddiadau difrifoldeb uchel, cyfran y gwasanaethau'n cario model bygythiad cyfredol, cyfran y digwyddiadau a ddalwyd cyn cynhyrchu, a chyfradd adroddiadau hunan-adroddedig o bethau-a-fu-bron-â-digwydd, a ddylai godi wrth i ymddiriedaeth dyfu yn hytrach na gostwng. Yr ystyriaeth gystadleuol yw y gellir gemio pob metrig da, felly parwch bob un â gwrth-fetrig ac adolygwch y duedd yn hytrach na'r ciplun. Dewch â'ch dangosfwrdd presennol a gofynnwch pa rifau fyddai'n newid pe bai diogelwch mewn gwirionedd yn gwaethygu; mae unrhyw un na fyddai'n newid yn addurniad. Mewn lleoliadau menter a llywodraeth bydd rheoleiddiwr neu bwyllgor archwilio'n gofyn am dystiolaeth bod rheolaethau'n gweithio, felly dewiswch fetrigau y gallwch eu hamddiffyn o dan graffu yn hytrach na rhai sy'n dim ond edrych yn wyrdd.

5. **Beth mewn gwirionedd sy'n digwydd y tro nesaf y bydd peiriannydd yn adrodd camgymeriad, ac a yw eich proses yn ddi-fai mewn ymarfer neu ar y sleid yn unig?** Dysgu di-fai yw'r egwyddor a broffesir amlaf ac a fyw leiaf, am mai'r digwyddiad difrifol cyntaf sy'n profi a yw arweinyddiaeth wir yn ei feddwl. Penderfynwch ymlaen llaw sut rydych yn gwahanu atebolrwydd am drwsio problem oddi wrth gosb am ei hachosi, a phwy sy'n rhedeg yr adolygiad ôl-ddigwyddiad fel ei fod yn aros am systemau wedi torri yn hytrach nag unigolion wedi'u henwi. Mae'r tensiwn yn real: mae rhanddeiliaid eisiau i rywun gael ei ddal yn gyfrifol, ac eto mae cosbi'r adroddwr yn gwarantu bod y camgymeriad nesaf yn aros yn guddiedig nes iddo droi'n doriad. Dewch â'ch dau adolygiad digwyddiad diwethaf a gwiriwch a oedden nhw'n beio person neu reolaeth, ac a ddiolchwyd i'r peiriannydd a gododd yr larwm neu a gafodd ei ddiystyru'n dawel. I lywodraeth a mentrau rheoledig, mae rheolau datgelu toriad gorfodol yn codi'r peryglon ymhellach, gan y bydd diwylliant sy'n cuddio camgymeriadau hefyd yn colli'r terfynau amser adrodd sy'n cario cosbau cyfreithiol.

6. **Pwy sy'n berchen ar ffrithiant eich offer symud-i'r-chwith, ac a ydych yn ei brynu, ei adeiladu, neu'n boddi ynddo?** Dadansoddi statig a dynamig awtomataidd, sganio dibyniaeth, a sganio cyfrinachau yw asgwrn cefn cylch bywyd datblygu diogel, ond mae piblinell sy'n boddi peirianwyr â chanlyniadau positif ffug yn eu dysgu i anwybyddu allbwn diogelwch, sy'n waeth na dim sganio o gwbl. Penderfynwch pwy sy'n tiwnio'r offer, pwy sy'n trïo'r canfyddiadau, ac a ydych yn prynu platfform integredig neu'n cydosod sganwyr cod agored y byddwch wedyn yn gorfod eu cynnal eich hunain. Yr ystyriaethau cystadleuol yw cwmpas yn erbyn sŵn a rheolaeth yn erbyn cost: mae sganiwr rhad sy'n gweiddi blaidd yn llosgi'r ymddiriedaeth y treuliodd rhaglen hyrwyddwyr flynyddoedd yn ei hadeiladu. Dewch â'ch cyfradd bositif ffug bresennol, y cyfartaledd amser mae peirianwyr yn aros ar wiriad sy'n rhwystro, a'r rhestr o dimau sydd wedi analluogi giât yn dawel. Mewn mentrau a llywodraethau mawr, ychwanegwch yr ongl gaffael a gwasgariad offer, gan fod deg tîm bob un yn prynu eu sganiwr eu hunain yn cynhyrchu cwmpas anghyson na all unrhyw archwiliwr ei gymodi.

## Lens sector

**Cwmni newydd.** Heb dîm diogelwch a rhedfa fach, diwylliant yw eich unig reolaeth fforddiadwy. Gwnewch fwrdd gwyn modelu bygythiad 30 munud yn arferiad cyn unrhyw nodwedd sy'n cyffwrdd â dilysu neu daliadau, trowch fraint leiaf ac MFA ymlaen ym mhobman am eu bod yn costio dim, a chadwch sianel ddi-fai lle gall unrhyw un fflagio pryder. Osgowch broses ac offer trwm; ni all y peirianwyr sefydlu ei gynnal, a'r ddisgyblaeth rydych yn ei adeiladu nawr yw'r hyn sy'n galluogi prynwyr menter i ymddiried ynoch yn ddiweddarach.

**Busnes bach.** Nid oes gennych arbenigwr diogelwch pwrpasol a chyllideb dynn, felly pwyswch ar ddiofynion diogel yn yr offer rydych eisoes yn eu prynu yn hytrach na sefydlu eich piblinell eich hun. Ffafriwch blatfformau wedi'u rheoli sy'n gorfodi MFA, clytio, a braint leiaf i chi, a thriniwch ddiogelwch fel cwestiwn hylendid data: gwybyddwch pa ddata sensitif sydd gennych a phwy all ei gyrraedd. Pan fydd rhaid i chi ddewis adeiladu yn erbyn prynu, prynwch, gan fod rheolaeth wedi'i rheoli rydych yn ei chadw'n gyfredol yn curo un bwrpasol rydych yn gadael iddi bydru.

**Menter.** Ar raddfa cannoedd o wasanaethau a miloedd o beirianwyr, yr her yw cysondeb a llywodraethu ar draws llawer o dimau. Rhedwch raglen hyrwyddwyr diogelwch, safonwch haenau modelu bygythiad wedi'u clymu i ddosbarthiad CIA, a darparwch dempledi ffordd-balmantog a gwiriadau piblinell awtomataidd fel bod pob tîm yn etifeddu diofynion da. Olrheiniwch fetrigau unioni a chwmpas yn erbyn llinellau sylfaen, a chadwch drywydd archwilio sy'n dangos pam y modelwyd a rheolwyd pob system fel y gwnaed.

**Llywodraeth.** Mae rheolau caffael, rhwymedigaethau tryloywder, ac atebolrwydd cyhoeddus yn siapio pob dewis. Mae egwyddorion ymddiriedaeth-sero a chredadwyaeth fyr-oes yn aml wedi'u gorfodi gan bolisi gweithredol, a rhaid i chi allu dangos i archwiliwr resymeg risg-seiliedig, dogfennedig ar gyfer ble aeth cyllideb caledu. Blaenoriaethwch y systemau'n dal y cofnodion dinesydd mwyaf sensitif yn gyntaf, cyhoeddwch y mesurau diogelwch lle mae gan y cyhoedd hawl i wybod, a mynnwch fod gwerthwyr yn datgelu cyfyngiadau yn hytrach na derbyn blychau du di-dryloyw.

## Enghreifftiau

**Cwmni newydd.** Nid oes gan gwmni newydd deg-person dîm diogelwch na chyllideb ar gyfer un, felly mae'r ddau beiriannydd sylfaenu'n gwneud modelu bygythiad yn arferiad bwrdd gwyn 30 munud cyn unrhyw nodwedd sy'n cyffwrdd â dilysu neu daliadau, gan ofyn beth allai fynd o'i le a phwy fyddai eisiau hynny. Maent yn mabwysiadu ychydig arferion sylfaenol sy'n costio dim: braint leiaf ar bob rôl cwmwl, MFA ar bob cyfrif, a sianel ddi-fai lle gall unrhyw un godi pryder heb ofn o fai. Pan fyddant yn ddiweddarach yn codi rownd ac yn gofyn prynwyr menter sut maent yn trin diogelwch, mae'r diwylliant cynnar hwnnw'n eu galluogi i ateb yn onest yn lle sgramblo i ddyfeisio un.

**Menter.** Mae banc byd-eang gyda 6,000 o beirianwyr yn rhedeg rhaglen hyrwyddwyr diogelwch gydag un hyrwyddwr wedi'i hyfforddi fesul sgwad. Mae hyrwyddwyr yn mynychu gild misol, yn cwblhau hyfforddiant chwarterol, ac yn arwain modelu bygythiad ar gyfer pob gwasanaeth newydd gan ddefnyddio STRIDE. Mae'r tîm AppSec canolog yn cynnal templedi ffordd-balmantog a gwiriadau piblinell awtomataidd. Dros ddwy flynedd, syrthiodd yr amser canolrifol i unioni canfyddiadau difrifoldeb uchel o 45 diwrnod i 9, a daliodd modelu bygythiad ar gam dylunio nam awdurdodi mewn API taliadau cyn iddo gyrraedd cynhyrchu, gan osgoi digwyddiad y byddai'n rhaid ei adrodd yn ôl pob tebyg.

**Llywodraeth.** Mae asiantaeth dreth genedlaethol sy'n moderneiddio systemau etifeddol yn mabwysiadu egwyddorion ymddiriedaeth-sero wedi'u gorfodi gan bolisi gweithredol. Mae pob galwad gwasanaeth mewnol wedi'i ddilysu â chredadwyaeth fyr-oes ac wedi'i awdurdodi fesul cais; nid yw segmentau rhwydwaith bellach yn rhoi ymddiriedaeth. Mae'r asiantaeth yn modelu bygythiad pob gwasanaeth sy'n wynebu dinasyddion yn erbyn coed ymosodiad wedi'u gwreiddio yn "allfudo cofnodion trethdalwyr" a "newid ffeilio." Mae blaenoriaethu risg-seiliedig, wedi'i alinio â lefelau effaith CIA, yn canolbwyntio cyllideb caledu ar y systemau'n dal y cofnodion mwyaf sensitif yn gyntaf.

## Achos busnes: cymhellion, ROI, a TCO

Mae cost adeiladu diwylliant diogelwch yn real: amser hyrwyddwyr, hyfforddiant, offer, a llusgiad cymedrol gwneud modelu bygythiad ac adolygiadau. Ond mae'r gost honno'n fach wrth ochr cost peidio â'i wneud. Mae'r toriad data mawr cyfartalog yn rhedeg i'r miliynau unwaith y byddwch yn cyfrif ymchwiliad, hysbysiad, unioni, dirwyon rheoleiddiol, amlygiad cyfreithiol, a busnes coll. Mae toriadau llywodraeth yn ychwanegu tarfu cenhadaeth ac erydiad ymddiriedaeth gyhoeddus nad yw unrhyw anfoneb yn ei ddal yn llawn.

Daw'r elw ar fuddsoddiad diogelwch o dri lle: **digwyddiadau a osgowyd** (y toriad na ddigwydd byth), **cost unioni is** (mae diffygion a drwsir ar adeg dylunio'n costio ffracsiwn o'r rhai a drwsir mewn cynhyrchu), a **thraddodi cyflymach** (mae ffyrdd palmantog a gwiriadau awtomataidd yn caniatáu i dimau draddodi'n hyderus yn lle aros am adolygiad â llaw). Pan wnewch yr achos i arweinyddiaeth, fframiwch ddiogelwch fel rheolaeth risg gyda thag pris, nid fel daioni haniaethol. Dangoswch y golled ddisgwyliedig (tebygolrwydd wedi'i luosi ag effaith) o'r risgiau uchaf, y gost i'w lleihau, a'r risg sy'n dal i aros. Mae cyfarwyddwyr yn ariannu lleihad risg y gallant ei fesur.

## Gwrth-batrymau a pheryglon

- **Theatr diogelwch.** Rheolaethau sy'n edrych yn drawiadol ond yn lleihau dim risg go iawn, wedi'u mabwysiadu i fodloni archwiliad yn hytrach nag amddiffyn unrhyw beth.
- **Y tîm diogelwch fel giât ar y diwedd.** Darganfod diffygion dylunio'r wythnos cyn lansio, pan fyddant ddrutaf i'w trwsio a mwyaf tebygol o gael eu hepgor.
- **Diwylliant bai.** Mae cosbi'r peiriannydd sy'n adrodd camgymeriad yn gwarantu bod y camgymeriad nesaf yn aros yn guddiedig.
- **Modelu bygythiad blwch-ticio.** Llenwi templed nad oes neb yn ei ddarllen, gan gynhyrchu dogfennau wedi'u datgysylltu oddi wrth y bensaernïaeth go iawn.
- **Rheolaethau un-maint-i-bawb.** Cymhwyso'r un broses drwm i wefan gyhoeddus a system daliadau, gan wastraffu ymdrech a meithrin chwerwder.
- **Blaenoriaethu wedi'i yrru gan ofn.** Erlid pa fregusrwydd bynnag sy'n tueddu yn y newyddion yn hytrach na'r hyn sydd mewn gwirionedd yn bygwth eich asedau.
- **Hyrwyddwyr mewn enw yn unig.** Enwi hyrwyddwyr heb roi amser, hyfforddiant, nac awdurdod iddynt.

## Model aeddfedrwydd

**Lefel 1: Cychwyn.** Mae diogelwch yn adweithiol ac yn ganolog. Mae adolygiadau'n digwydd yn hwyr os o gwbl, ac nid oes modelu bygythiad. Mae digwyddiadau'n gyrru trwsiadau achlysurol. Mae peirianwyr yn gweld diogelwch fel problem rhywun arall, ac nid oes safon a rennir yn bodoli.

**Lefel 2: Datblygu.** Mae tîm diogelwch yn bodoli ac yn diffinio safonau, ond mae'r arfer yn anghyson ar draws timau. Mae rhywfaint o fodelu bygythiad yn digwydd ar brosiectau mawr a dim ar rai eraill. Mae hyfforddiant sylfaenol ar gael. Caiff diogelwch ei ganfod o hyd fel giât, ac mae symud-i'r-chwith yn ddyheadol yn hytrach na go iawn.

**Lefel 3: Safoni.** Mae hyrwyddwyr diogelwch wedi'u mewnblannu ym mhob tîm. Mae modelu bygythiad yn rwtîn ar gyfer gwasanaethau newydd, wedi'i haenu yn erbyn dosbarthiad CIA, ac mae'r cylch bywyd datblygu diogel wedi'i ddogfennu a'i orfodi ar draws y sefydliad. Mae blaenoriaethu risg-seiliedig yn llywio'r gwaith, safonau codio diogel a gwiriadau piblinell yw'r ffordd balmantog ddiofyn, ac mae adolygiadau ôl-ddigwyddiad di-fai'n norm.

**Lefel 4: Rheoli.** Caiff canlyniadau diogelwch eu mesur a'u rheoli yn erbyn llinellau sylfaen. Mae'r sefydliad yn olrhain amser canolrifol i unioni canfyddiadau difrifoldeb uchel, cwmpas model bygythiad, cyfran y digwyddiadau a ddalwyd cyn cynhyrchu, a chyfraddau adrodd pethau-a-fu-bron-â-digwydd, wedi'u dadansoddi fesul tîm. Mae awdurdod hyrwyddwyr i atal rhyddhad wedi'i ddiffinio ac wedi'i arfer mewn gwirionedd. Mae penderfyniadau risg wedi'u meintioli fel tebygolrwydd wedi'i luosi ag effaith, wedi'u cofnodi, a'u hadolygu ar gyfnod sefydlog, fel bod bylchau rheolaeth yn dod i'r amlwg fel data yn hytrach na syrpreisau.

**Lefel 5: Cydgordio.** Mae diogelwch mewn gwirionedd yn waith i bawb ac wedi'i integreiddio â chynllunio traddodi, risg, a busnes. Mae modelu bygythiad a dylunio diogel yn arferiadol ac yn ysgafn, ac mae egwyddorion ymddiriedaeth-sero i raddau helaeth wedi'u gwireddu. Mae metrigau'n gyrru gwelliant parhaus, mae'r sefydliad yn dysgu o bethau-a-fu-bron-â-digwydd ar draws timau, ac mae rheolaethau'n addasu'n awtomatig wrth i'r darlun bygythiad a'r bensaernïaeth newid.

## Syniadau ar gyfer trafodaeth

1. Sut ydych chi'n mesur a yw diwylliant diogelwch mewn gwirionedd yn gwella, y tu hwnt i gyfrif cwblhad hyfforddiant?
2. Ble mae'r ffin gywir rhwng yr hyn y mae hyrwyddwyr diogelwch yn ei drin a'r hyn y mae'r tîm canolog yn berchen arno?
3. Sut ydych chi'n cadw modelu bygythiad yn werthfawr heb adael iddo droi'n flwch ticio biwrocrataidd?
4. A yw pensaernïaeth ymddiriedaeth-sero lawn yn realistig ar gyfer eich ystâd etifeddol, ac os nad yw, beth yw'r isset ymarferol?
5. Sut y dylid blaenoriaethu gwaith diogelwch yn erbyn traddodi nodweddion pan fo'r ddau'n cystadlu am yr un peirianwyr?
6. Pa gymhellion sy'n mewn gwirionedd yn newid ymddygiad peirianwyr tuag at berchnogaeth diogelwch?

## Casgliadau allweddol

- Priodwedd ddiwylliannol o sefydliadau mawr yw diogelwch, nid tasg wedi'i dirprwyo i un tîm.
- Mae hyrwyddwyr diogelwch yn graddio arbenigedd a pherchnogaeth ar draws peirianneg.
- Mae modelu bygythiad (STRIDE, PASTA, coed ymosodiad) yn dod â diffygion dylunio i'r wyneb yn gynnar ac yn rhad.
- Mae SDLC diogel a meddylfryd symud-i'r-chwith yn dal diffygion pan fyddant rataf.
- Amddiffyn mewn dyfnder, braint leiaf, ac ymddiriedaeth sero yw'r egwyddorion pensaernïol sylfaenol.
- Mae'r triawd CIA a blaenoriaethu risg-seiliedig yn cyfeirio ymdrech brin at ble mae bwysicaf.
- Mae cost adeiladu diwylliant diogelwch yn llawer llai na chost y toriadau y mae'n eu hatal.

## Cyfeiriadau a darllen pellach

- Adam Shostack, *Threat Modeling: Designing for Security*
- Ross Anderson, *Security Engineering: A Guide to Building Dependable Distributed Systems*
- Michael Howard a Steve Lipner, *The Security Development Lifecycle*
- Betsy Beyer et al. (Google), *Building Secure and Reliable Systems*
- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- National Institute of Standards and Technology, *Secure Software Development Framework (SSDF), SP 800-218*
- OWASP, arweiniad *Threat Modeling* a *Security Champions*
