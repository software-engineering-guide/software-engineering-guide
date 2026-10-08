# 1.6 Cofnodion penderfyniadau

## Trosolwg a chymhelliant

Mae **cofnod penderfyniad** yn ddogfen sy'n dal penderfyniad pwysig ynghyd â'i gyd-destun a'i ganlyniadau. Y ffurf fwyaf adnabyddus yw'r **[cofnod penderfyniad pensaernïaeth](https://en.wikipedia.org/wiki/Architectural_decision) (ADR)**, nodyn byr, yn ddiofyn anghyfnewidiol, sy'n cofnodi un dewis pensaernïol arwyddocaol, pam y gwnaed ef, a'r hyn sy'n dilyn ohono. Set gyflawn cofnodion prosiect yw ei **log penderfyniadau (ADL)**, ac mae'r ddisgyblaeth o'u cadw'n rhan o **reolaeth gwybodaeth bensaernïol (AKM)**. Mae'r bennod hon yn adeiladu ar arferion gwneud penderfyniadau a llywodraethu pennod 1.5, gan ganolbwyntio ar sut rydych chi'n ysgrifennu, storio, a chynnal cofnodion penderfyniadau ar raddfa.

Mae'r cymhelliant yn syml, ac yn boenus i'w ddysgu'r ffordd galed. Ar unrhyw system hirhoedlog, y cwestiwn drutaf yw "pam ar y ddaear y cafodd ei adeiladu fel hyn?", a ofynnir fisoedd neu flynyddoedd yn ddiweddarach gan bobl nad oeddent yn yr ystafell. Mae cod yn dangos *beth* y mae'r system yn ei wneud. Mae profion yn dangos ei bod *yn gweithio*. Ond nid yw'r naill na'r llall yn dal *pam* y dewisoch chi'r llwybr hwn dros y dewisiadau eraill y gwnaethoch chi eu hystyried a'u gwrthod. Heb gofnodion penderfyniadau, mae'r rhesymeg honno'n anweddu gyda throsiant staff. Mae timau'n ailymladd cwestiynau a benderfynwyd eisoes, yn gwrthdroi penderfyniadau da am resymau gwael, neu'n cadw penderfyniadau gwael allan o ofn. Mae cofnod penderfyniad yn llythyr rhad at y dyfodol sy'n cadw'r rhesymeg.

I dimau mawr, mae hyn yn declyn cydgysylltu gymaint ag y mae'n gymorth cof. Mae mentrau'n rhedeg dwsinau o dimau'n gwneud dewisiadau sy'n gorgyffwrdd. Mae log penderfyniadau a rennir yn troi rhesymeg tîm a enillwyd yn galed yn ased y gellir ei ailddefnyddio, ac yn atal penderfyniadau anghyson, anghydnaws. Mewn lleoliadau llywodraeth a rheoleiddiedig, mae cofnodion penderfyniadau bron yn orfodol. Mae angen ar archwilwyr, cyrff goruchwylio, a chontractwyr olynol i gyd resymeg olrheiniadwy sy'n cysylltu gofynion pensaernïol arwyddocaol â'r dewisiadau a wnaed yn eu herbyn. Mae log penderfyniadau wedi'i gadw'n dda yn aml yn wahaniaeth rhwng system y gallwch ei sicrhau a'i harchwilio ac un na allwch.

## Egwyddorion allweddol

- **Cofnodwch y *pam*, nid dim ond y *beth*.** Cyd-destun a dewisiadau eraill a wrthodwyd yw'r pwynt.
- **Un penderfyniad fesul cofnod.** Cadwch bob cofnod yn benodol ac yn hunangynhwysol.
- **Mae bach ac ysgafn yn curo cynhwysfawr a heb ei ddefnyddio.** Mae cofnod un dudalen sy'n bodoli'n curo adroddiad nad yw byth yn cael ei ysgrifennu.
- **Rhowch stamp amser ar bopeth.** Mae costau, cyfyngiadau, a gwerthwyr yn newid; dyddiwch bob honiad.
- **Ffafriwch log byw, yn bragmatig.** Anghyfnewidedd yw'r ddelfryd; yn ymarferol, diwygiwch gyda nodiadau dyddiedig.
- **Geiriau dros dalfyriadau.** Mae "penderfyniadau" yn gwahodd mwy o gyfraniad na "ADRs."
- **Gwnewch benderfyniadau'n hawdd dod o hyd iddynt ac, lle bo modd, yn brofadwy.** Dewch â'r cofnod cywir i'r amlwg ar yr eiliad gywir; sicrhewch ef gyda swyddogaethau ffitrwydd.

## Argymhellion

### Dal y strwythur hanfodol

Mae gan gofnod penderfyniad da ychydig o adrannau hanfodol. Addaswch dempled hysbys yn hytrach na dyfeisio un:

- **Teitl:** ymadrodd gorchmynnol byr, amser presennol ("Defnyddiwch [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) ar gyfer y llyfr cyfrifon").
- **Statws:** cynigiedig, derbyniedig, wedi'i ddisodli, wedi'i ddad-gymeradwyo.
- **Cyd-destun:** y sefyllfa, y grymoedd, y blaenoriaethau busnes, a'r cyfyngiadau sy'n gwneud y penderfyniad hwn yn angenrheidiol; cynhwyswch y gofyniad pensaernïol arwyddocaol y mae'n mynd i'r afael ag ef.
- **Penderfyniad:** y dewis a wnaed, wedi'i nodi'n blaen.
- **Canlyniadau:** beth sy'n dod yn haws a beth sy'n dod yn anos, penderfyniadau dilynol a sbardunwyd, a risgiau a dderbyniwyd.

Mae templedi poblogaidd yn cynnwys un Michael Nygard (syml ac wedi'i fabwysiadu'n eang), un Tyree ac Akerman (mwy manwl, gyda dewisiadau eraill wedi'u pwysoli), MADR (Markdown Any Decision Records, cryf ar opsiynau a'u manteision/anfanteision), a datganiadau-Y (ffurf strwythuredig un frawddeg). Safonwch ar un fesul sefydliad, fel bod cofnodion yn gymaradwy. Gweler pennod 12.3 am dempled copïo-a-gludo.

### Ysgrifennu cofnodion sy'n benodol, wedi'u dyddio, ac yn go anghyfnewidiol

Cadwch bob cofnod am union un penderfyniad. Rhowch stamp amser ar honiadau unigol, yn enwedig unrhyw beth sy'n llithro: prisio, rhifau graddio, galluoedd gwerthwr, telerau trwydded. Mewn theori, dylai cofnod fod yn anghyfnewidiol. Pan fydd penderfyniad yn newid, rydych chi'n ysgrifennu cofnod *newydd* sy'n disodli'r hen un, gan gadw hanes. Yn ymarferol, mae llawer o dimau'n gweld bod dull **dogfen fyw** yn gweithio'n well: mewnosod gwybodaeth newydd i'r cofnod presennol gyda stamp dyddiad a nodyn ei bod wedi cyrraedd ar ôl y penderfyniad. Mae'r ddau'n ddilys. Mae'r arddull anghyfnewidiol yn gryfach ar gyfer llwybrau archwilio; mae'r arddull fyw'n well ar gyfer gwybodaeth tîm bob dydd. Dewiswch yn fwriadus, a byddwch yn gyson.

### Storio cofnodion lle mae'r gwaith

Rhowch gofnodion penderfyniadau mewn [rheolaeth fersiynau](https://en.wikipedia.org/wiki/Version_control) ochr yn ochr â'r cod: cyfeiriadur `decisions/` (neu `adr/`) o ffeiliau [Markdown](https://en.wikipedia.org/wiki/Markdown), un fesul penderfyniad, wedi'u henwi ag ymadrodd berf gorchmynnol llythrennau bach, wedi'u gwahanu â chysylltnod (`choose-database.md`, `format-timestamps.md`). Mae hyn yn rhoi hanes, adolygiad, a chymharu i chi am ddim, ac yn cadw'r rhesymeg wrth ymyl yr hyn y mae'n ei egluro. Os yw eich tîm yn ffafrio [wicis](https://en.wikipedia.org/wiki/Wiki), Google Docs, neu olrheiniwr fel Jira, defnyddiwch y rheini yn lle hynny. Mae'r teclyn yn bwysig llawer llai na'r arferiad. Gall teclyn llinell orchymyn ysgafn (fel `adr-tools`) sgaffaldio a mynegeio cofnodion.

### Enwch nhw'n "benderfyniadau," ac ehangu y tu hwnt i bensaernïaeth

Mewnwelediad ymarferol o lawer o dimau: mae'r label yn bwysig. Mae rhai datblygwyr a rheolwyr yn gwrthwynebu'r gair "pensaernïaeth," a gall "cofnod" deimlo fel papurwaith ôl-ddigwyddiad. Yn aml mae ailenwi'r cyfeiriadur yn syml yn "penderfyniadau" yn troi swits. Mae timau'n dechrau cofnodi dewisiadau gwerthwyr, penderfyniadau cynllunio, penderfyniadau amserlennu, penderfyniadau data a chydymffurfiaeth, i gyd gyda'r un templed. Mae pobl yn dysgu'n gyflymach o eiriau nag o dalfyriadau, ac maent yn cyfrannu mwy pan fo'r fframio yn "helpu eich cyd-dimwyr yn y dyfodol i feddwl" yn hytrach na "llenwi'r ffurflen orfodol."

### Diffinio'r cylch bywyd a llywodraethu

Er mwyn i gofnodion penderfyniadau raddio, cytunwch ar y broses gyfagos (dyma lle mae llywodraethu pennod 1.5 yn cwrdd ag arfer):

- **Pwy all godi un, a beth sy'n ei gyfiawnhau:** fel arfer unrhyw gyfrannwr gwybodus; codwch gofnod pan fydd datblygwyr yn y dyfodol angen y *pam*, a'i hepgor ar gyfer dewisiadau risg isel, hunangynhwysol, neu eisoes wedi'u dogfennu.
- **Cylch bywyd:** llif syml fel *Cychwyn → Ymchwilio → Gwerthuso → Gweithredu → Cynnal → Machludo*, gyda meini prawf derbyn i symud rhwng camau (problem wedi'i mynegi, dewisiadau eraill wedi'u hystyried, cyfaddawdau wedi'u dogfennu, rhanddeiliaid wedi'u hymgynghori).
- **Rolau:** cynigydd, ymchwilydd, adolygydd, cymeradwywr, a chynhaliwr atebol sy'n adolygu'r cofnod yn gyfnodol (o leiaf yn flynyddol) ac yn gyrru machludo yn y pen draw.
- **Llywodraethu:** sut mae consensws, gwrthdaro, uwchgyfeirio, a feto'n gweithio, ac unrhyw gyfyngiadau cydymffurfiaeth. Pwyswch ar egwyddorion fel *tuedd tuag at weithredu* a *[anghytuno-ac-ymrwymo](https://en.wikipedia.org/wiki/Disagree_and_commit)*, a chadwch broses drymach ar gyfer penderfyniadau anwrthdroadwy, radiws-ffrwydro-uchel ("drws un-ffordd").

### Gwneud penderfyniadau'n brofadwy ac yn hawdd dod o hyd iddynt

Mae cofnod penderfyniad yn *dogfennu* penderfyniad; mae **swyddogaeth ffitrwydd** yn ei *sicrhau*: gwiriad awtomataidd, wedi'i redeg mewn [integreiddio parhaus](https://en.wikipedia.org/wiki/Continuous_integration) (CI), sy'n gwirio bod y penderfyniad yn dal i sefyll ("rhaid i bob newid cyflwr allyrru digwyddiadau," "ni chaiff unrhyw fodiwl fewnforio ar draws y ffiniau hyn," gan ddefnyddio teclynnau fel ArchUnit). Mae hyn yn troi llywodraethu o adolygiad â llaw cyfnodol yn orfodaeth barhaus, raddadwy, sy'n arbennig o werthfawr ar gyfer nodau rheoleiddiol ac archwilio (penodau 3.1, 4.6, 8.5). Yna dewch â'r cofnod *cywir* i'r amlwg ar yr eiliad *gywir*. Mae offer sy'n atodi penderfyniadau perthnasol i gais tynnu, pan fydd datblygwr yn cyffwrdd â'r cod y maent yn ei lywodraethu, yn curo gobeithio bod pobl yn darllen ffolder dogfennau.

## Cyfaddawdau: manteision ac anfanteision

| Dewis | Manteision | Anfanteision |
|---|---|---|
| **ADRs ysgafn (Nygard/MADR)** | Cyflym i'w hysgrifennu, yn cael eu hysgrifennu mewn gwirionedd; seremoni isel | Llai o drylwyredd ar gyfer penderfyniadau goblygiadau uchel, dadleuol |
| **Templedi trwm (Tyree-Akerman)** | Dewisiadau eraill wedi'u pwysoli; cryf ar gyfer dewisiadau mawr, costus | Arafach; gall atal cofnodi arferol |
| **Anghyfnewidiol + disodli** | Llwybr archwilio glân; hanes wedi'i gadw | Mwy o gofnodion; rhaid i ddarllenwyr olrhain cadwyni |
| **Dogfen fyw (diwygiadau dyddiedig)** | Un ffynhonnell wirionedd gyfredol; hawdd ei chynnal | Stori archwilio wannach; risg o olygiadau tawel |
| **Markdown yn yr ystorfa** | Wedi'i fersiynu, yn adolygadwy, wrth ymyl y cod | Llai cyfeillgar i rai nad ydynt yn ddatblygwyr |
| **Teclyn wici / dogfennau** | Hygyrch i bob rôl | Hanes ac adolygiad gwannach; yn crwydro o'r cod |

Y tyndra craidd yw **trylwyredd yn erbyn mabwysiadu**. Nid yw'r system fwyaf trylwyr nad oes neb yn ei defnyddio'n cofnodi dim. Mae'r system ysgafnaf y mae pawb yn ei defnyddio'n cronni gwerth. Rhagosodwch i fod yn ysgafn, a chadwch broses drymach ar gyfer y penderfyniadau prin sy'n ddrud ac yn anodd eu gwrthdroi.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Sut y bydd y cofnod penderfyniad cywir yn cyrraedd datblygwr ar yr eiliad y maen nhw'n cyffwrdd â'r cod y mae'n ei lywodraethu, yn hytrach nag eistedd mewn ffolder nad oes neb yn ei agor?** Mae log ysgrifennu-yn-unig yn cofnodi rhesymeg nad yw byth yn newid ymddygiad, sef y ffordd fwyaf cyffredin y mae cofnodion penderfyniadau'n methu: maen nhw'n bodoli, ac nid oes neb yn eu darllen pan fo hynny'n bwysig. Yr ystyriaeth sy'n cystadlu yw ymdrech, oherwydd mae dod â chofnodion i'r amlwg yn awtomatig (eu hatodi i gais tynnu pan fydd rhywun yn golygu'r cod a lywodraethir) yn cymryd buddsoddiad offer nad yw wici neu ffolder dogfennau'n ei wneud. Dewch â thystiolaeth i'r drafodaeth: pan wnaeth rhywun wrthdroi neu ailymladd cwestiwn a benderfynwyd yn ddiweddar, a oedd y cofnod perthnasol yn hawdd dod o hyd iddo bryd hynny, neu wedi'i gladdu? I sefydliad mawr sy'n rhedeg dwsinau o dimau, gallu dod o hyd i wybodaeth yw'r hyn sy'n troi rhesymeg tîm a enillwyd yn galed yn ased y gellir ei ailddefnyddio yn hytrach nag archif breifat. Penderfynwch a ddylid storio cofnodion mewn rheolaeth fersiynau wrth ymyl y cod a'u gwifro i mewn i lif y cais tynnu, fel bod y cofnod yn ymddangos lle mae'r gwaith yn digwydd.

2. **Pwy yw'r cynhaliwr atebol ar gyfer pob cofnod, a beth sy'n atal eich log rhag pydru'n gamwybodaeth hyderus?** Nid ffolder wag yw modd methiant peryglus log penderfyniadau, ond ffolder yn llawn cofnodion y mae eu costau, galluoedd gwerthwr, a chyfyngiadau wedi mynd yn hen yn dawel flynyddoedd yn ôl. Mae angen perchennog atebol ar bob cofnod sy'n ei adolygu ar rythm (o leiaf yn flynyddol) ac yn gyrru disodli neu fachludo, neu mae'r log yn pydru'n chwedloniaeth y mae pobl yn ei dyfynnu'n ddetholus ac yn ymddiried ynddi ychydig. Dewch â thystiolaeth: faint o'ch cofnodion sydd heb ddyddiad, faint sy'n disgrifio gwerthwr neu bris sydd wedi newid ers hynny, a phryd yr adolygwyd pob un ddiwethaf. Mewn lleoliadau llywodraeth a rheoleiddiedig mae hyn yn fwy miniog, oherwydd cadwyn anghyfnewidiol, wedi'i disodli yw'n union yr hyn y mae archwilwyr a chontractwyr olynol yn dibynnu arno ar gyfer rhesymeg olrheiniadwy. Penderfynwch eich cylch bywyd yn benodol, rhowch stamp amser ar honiadau unigol sy'n llithro, a phenodwch gynhalwyr, fel bod y log yn aros yn ased byw yn hytrach na mynwent.

3. **A ddylech chi safoni ar un templed ar draws pob tîm, a faint o drylwyredd sydd wir angen ar eich penderfyniadau goblygiadau uchaf?** Mae cymaroldeb yn fantais go iawn: pan fydd pob tîm yn defnyddio'r un siâp (Nygard, MADR, neu debyg), gall tîm newydd ddod o hyd i dri chofnod blaenorol a mabwysiadu'r rhesymeg mewn prynhawn yn hytrach na mis o ddadlau. Y tyndra craidd yw trylwyredd yn erbyn mabwysiadu, oherwydd nid yw'r templed trymaf nad oes neb yn ei ddefnyddio'n cofnodi dim, tra bo'r un ysgafnaf y mae pawb yn ei ddefnyddio'n cronni gwerth. Dewch â thystiolaeth: a yw cofnodion mewn gwirionedd yn cael eu hysgrifennu, ac ar wahân, a oes unrhyw benderfyniadau mawr, dadleuol, costus wedi'u tananalysu oherwydd bod y ffurf ysgafn wedi hepgor pwyso dewisiadau eraill? I fentrau sy'n cydgysylltu dewisiadau sy'n gorgyffwrdd ar draws timau, mae templed a rennir ynghyd â mynegai y gellir chwilio ynddo'n atal penderfyniadau anghyson, anghydnaws. Rhagosodwch i fod yn ysgafn ar gyfer yr achos cyffredin, a chytunwch ymlaen llaw pa benderfyniadau drws-un-ffordd sy'n cyfiawnhau ffurf drymach gyda dewisiadau eraill wedi'u pwysoli.

4. **Beth sy'n cyfiawnhau codi cofnod penderfyniad mewn gwirionedd, a phwy sydd â'r awdurdod i ddweud nad oes angen un ar ddewis?** Gosodwch y bar yn rhy uchel ac mae'r rhesymeg y tu ôl i ddewisiadau canlyniadol yn anweddu; gosodwch ef yn rhy isel ac mae'r log yn llenwi â phethau dibwys sy'n claddu'r cofnodion y mae pobl wir eu hangen. I sefydliad mawr, mae trothwy aneglur yn golygu bod pob tîm yn byrfyfyrio ei un ei hun, felly mae sylw'n dod yn anwastad ac ni all neb ymddiried nad yw cofnod coll yn arwyddo penderfyniad dibwys. Dewch â thystiolaeth i'r drafodaeth: llond llaw o benderfyniadau diweddar a gofnodwyd ond nad oedd angen hynny, a rhai poenus a aeth heb eu cofnodi ac a gostiodd ail-ddarganfyddiad i chi'n ddiweddarach. Cytunwch ar brawf syml, fel cofnodi pryd bynnag y bydd datblygwr yn y dyfodol angen y *pam* a hepgor dewisiadau risg isel, hunangynhwysol, neu eisoes wedi'u dogfennu. Mewn lleoliadau rheoleiddiedig a llywodraeth mae'r cyfrifiad yn newid, oherwydd gall mandad archwilio ei gwneud yn ofynnol cael cofnod ar gyfer pob gofyniad pensaernïol arwyddocaol p'un a yw'r tîm yn barnu ei fod yn werth ei ysgrifennu ai peidio, felly enwch pa benderfyniadau sydd heb eu trafod ymlaen llaw.

5. **A yw eich cofnodion yn rhesymeg go iawn a ddaliwyd ar eiliad y penderfyniad, neu'n bapurwaith a ysgrifennwyd wedyn i fodloni mandad?** Mae cofnod a gynhyrchwyd ar ôl y ffaith i gau tocyn yn tueddu i olchi'r opsiwn a ddewiswyd ac yn dawel yn hepgor y dewisiadau eraill a bwyswyd mewn gwirionedd, sef yn union y wybodaeth sydd fwyaf ei hangen ar ddarllenydd yn y dyfodol. Mae'r pwysau sy'n cystadlu'n real: mae ysgrifennu'r *pam* cyn neu yn ystod penderfyniad yn teimlo'n arafach na chyflenwi, ac mae cyfaddef y llwybrau a wrthodwyd yn ysgrifenedig yn cymryd diogelwch seicolegol sydd ar goll gan rai timau. Dewch â sampl o gofnodion diweddar i'r bwrdd a gofynnwch yn onest a yw'r cyd-destun a'r dewisiadau eraill a wrthodwyd yn darllen fel trafodaeth go iawn neu fel cyfiawnhad wedi'i ôl-osod. I dîm mawr, mae cofnodion gwag yn waeth na dim, oherwydd maen nhw'n dysgu pobl na ellir ymddiried yn y log. Mewn archwiliad menter a llywodraeth mae'r gwahaniaeth hwn yn finiog: mae cyrff goruchwylio a chontractwyr olynol yn dibynnu ar resymeg sy'n adlewyrchu'r hyn a ystyriwyd mewn gwirionedd, ac mae cofnod sy'n darllen fel theatr yn tanseilio'r sicrwydd y mae'r log yn bodoli i'w ddarparu.

6. **Pa un o'ch penderfyniadau goblygiadau uchaf y gallwch chi ei sicrhau â swyddogaeth ffitrwydd awtomataidd, yn hytrach nag ymddiried y bydd adolygiad â llaw cyfnodol yn dal toriad?** Mae cofnod penderfyniad yn dogfennu dewis, ond dim ond gwiriad awtomataidd sy'n rhedeg mewn integreiddio parhaus sy'n atal y dewis hwnnw rhag erydu'n dawel wrth i ddwsinau o ddatblygwyr gyffwrdd â'r cod dros flynyddoedd. Y cyfaddawd yw buddsoddiad, oherwydd mae ysgrifennu a chynnal swyddogaethau ffitrwydd (gyda theclynnau fel ArchUnit) yn costio amser peirianneg, ac nid yw llawer o benderfyniadau, yn enwedig dewisiadau proses neu werthwr, yn brofadwy'n fecanyddol o gwbl. Dewch â thystiolaeth: pa benderfyniadau ffiniol (dibyniaethau modiwl, allyrru digwyddiadau, rheolau mynediad data) sydd wedi'u torri'n dawel a'u dal dim ond yn hwyr mewn adolygiad neu mewn cynhyrchiad. I fenter sy'n rhedeg llawer o dimau, mae swyddogaethau ffitrwydd yn troi llywodraethu o dagfa ganolog yn orfodaeth barhaus sy'n graddio heb arafu pawb. Mewn cyd-destunau rheoleiddiedig a llywodraeth, mae gwiriad awtomataidd, bob amser ymlaen yn dystiolaeth archwilio llawer cryfach na llofnod ar adolygiad, oherwydd mae'n profi bod y penderfyniad yn dal i sefyll heddiw yn hytrach na bod rhywun wedi'i gymeradwyo unwaith.

## Golwg sector

**Startup.** Cadwch ef i'r arferiad a dim byd arall: ffolder `decisions/` yn eich prif ystorfa, a nodyn dwy adran (cyd-destun a dewis) pryd bynnag y byddwch chi'n gwneud galwad y bydd eich hunan yn y dyfodol yn ei chwestiynu. Hepgorwch gylch bywyd, rolau, a chymeradwywyr yn llwyr, oherwydd proses na allwch ei chynnal yw proses y byddwch chi'n ei gadael. Mae'r un cofnod sy'n arbed eich cyflogai cyntaf rhag gofyn pam mae'r system wedi'i hadeiladu fel hyn eisoes yn talu am yr arfer cyfan.

**Busnes bach.** Heb bensaer pwrpasol ac ychydig o amser, rhowch gofnodion lle mae eich tîm eisoes yn gweithio, boed hynny'n wici, dogfen a rennir, neu'r ystorfa, yn hytrach na phrynu teclyn pwrpasol. Mae'r arferiad yn bwysig llawer mwy na'r offer, felly gostyngwch y rhwystr: enwch y cyfeiriadur yn `decisions` yn hytrach nag `adr`, a daliwch ddewisiadau gwerthwr a phrynu-yn-erbyn-adeiladu yn yr un gwynt â rhai technegol. Pan fyddwch chi'n pwyso ar gontractwyr allanol, mae cofnod byr, dyddiedig o pam y dewisoch chi werthwr neu blatfform yn yswiriant rhad yn erbyn cael eich cloi i mewn i ddewis na all neb ei egluro'n ddiweddarach.

**Menter.** Cydgysylltu ar draws llawer o dimau yw'r gwaith: safonwch ar un templed, cyhoeddwch fynegai traws-dîm y gellir chwilio ynddo, a chefnogwch benderfyniadau ffiniol allweddol â swyddogaethau ffitrwydd fel bod toriadau'n methu'r adeiladwaith yn hytrach nag aros am adolygiad. Penodwch gynhaliwr atebol i bob cofnod gyda rhythm adolygu, fel bod y log yn aros yn ased byw yn hytrach na phydru'n chwedloniaeth. Wedi'i wneud yn dda, mae rhesymeg un tîm ar ddewis anodd yn dod yn ased y mae'r tîm nesaf yn ei fabwysiadu mewn prynhawn yn hytrach nag ailymladd.

**Llywodraeth.** Mae rheolau caffael, tryloywder, ac atebolrwydd cyhoeddus yn gwneud cofnodion penderfyniadau bron yn orfodol. Mynnwch gofnod anghyfnewidiol, wedi'i ddisodli ar gyfer pob gofyniad pensaernïol arwyddocaol, pob un yn cysylltu'r dewis â'r mandad neu'r rheolydd cydymffurfiaeth y mae'n ei fodloni, fel bod cyrff goruchwylio'n dod o hyd i resymeg olrheiniadwy yn hytrach nag ailadeiladiad. Gan fod systemau cyhoeddus yn rhychwantu oes aml-flwyddyn, aml-werthwr, mae log wedi'i gadw'n dda yn aml yn caniatáu i gontractwr olynol ddeall pam mae'r system wedi'i siapio fel y mae a pharhau â'r gwaith heb ailymladd tir a benderfynwyd eisoes.

## Enghreifftiau

**Startup.** Mae startup pum person yn ychwanegu ffolder plaen `decisions/` at ei brif ystorfa, gyda nodyn dwy adran (cyd-destun a dewis) pryd bynnag y bydd rhywun yn gwneud galwad y bydd eu hunain yn y dyfodol yn ei chwestiynu. Nid oes cylch bywyd, dim rolau, a dim cymeradwywyr: dim ond yr arferiad o ysgrifennu'r *pam* wrth ymyl y cod. Pan fydd eu cyflogai cyntaf yn ymuno chwe mis yn ddiweddarach, mae hi'n darllen y ffolder cyfan mewn awr ac yn stopio gofyn "pam mae hyn wedi'i adeiladu fel hyn?" Mae'r log ysgafn yn costio munudau fesul cofnod ac yn eu harbed rhag y dreth ail-ddarganfod sy'n brathu ymhell cyn i dîm dyfu'n fawr.

**Menter.** Mae manwerthwr gyda 30 tîm peirianneg yn safoni ar gofnodion fformat MADR ym mhob ystorfa, ynghyd â mynegai canolog y gellir chwilio ynddo. Pan fydd tîm newydd yn wynebu "[monorepo](https://en.wikipedia.org/wiki/Monorepo) yn erbyn multirepo," maen nhw'n dod o hyd i dri chofnod blaenorol gyda chyd-destun a chanlyniadau, ac yn mabwysiadu'r rhesymeg mewn prynhawn yn hytrach na mis o ddadlau. Cefnogir penderfyniadau ffiniol allweddol (perchnogaeth gwasanaeth, rheolau mynediad data) gan swyddogaethau ffitrwydd ArchUnit, fel bod toriadau'n methu'r adeiladwaith yn hytrach na chael eu dal mewn adolygiad. Dyna lywodraethu sy'n graddio heb dagfa ganolog.

**Llywodraeth.** Mae asiantaeth sy'n moderneiddio system budd-daliadau'n ei gwneud yn ofynnol cael ADR ar gyfer pob gofyniad pensaernïol arwyddocaol, pob un yn cysylltu'r penderfyniad â'r mandad neu'r rheolydd cydymffurfiaeth y mae'n ei fodloni (hygyrchedd, preswyliad data, archwiliadwyedd). Mae cofnodion yn anghyfnewidiol ac wedi'u disodli, gan gynhyrchu log olrheiniadwy sy'n bodloni adolygiad goruchwylio. Yn hollbwysig, mae hefyd yn caniatáu i gontractwr olynol ddeall *pam* mae'r system wedi'i siapio fel y mae, gan gadw parhad ar draws yr oes aml-flwyddyn, aml-werthwr sy'n nodweddiadol o raglenni cyhoeddus (penodau 4.6, 10.4).

## Achos busnes: cymhellion, ROI, a TCO

Mae cofnod penderfyniad yn costio munudau i'w ysgrifennu ac ychydig mwy i'w adolygu. Y ffordd yw osgoi cost *ail-benderfynu* ac osgoi cost *gwrthdroi anghywir*, ac mae'r ddau'n fawr ac yn ailadroddus ar systemau hirhoedlog. Bob tro y bydd tîm yn ailymladd cwestiwn a benderfynwyd eisoes, neu'n gwrthdroi dewis cadarn oherwydd nad oedd neb yn cofio'r cyfyngiad y tu ôl iddo, maen nhw'n talu mewn amser peiriannydd hŷn ac yn aml mewn digwyddiad. Mae log penderfyniadau'n trosi'r dreth ailadroddus honno'n ysgrifeniad untro.

O ran **cyfanswm cost perchnogaeth**, mae cofnodion penderfyniadau ymhlith y ddogfennaeth â'r trosoledd uchaf y gallwch ei chadw, oherwydd maen nhw'n targedu'r ased mwyaf sensitif i drosiant: rhesymeg. Mae sefydlu'n gyflymach (mae cyflogeion newydd yn darllen y *pam*, nid dim ond y cod). Mae moderneiddio'n fwy diogel (pennod 3.6: gallwch ddweud pa benderfyniadau sy'n hanfodol o'r rhai damweiniol). Mae archwiliadau'n rhatach (mae'r dystiolaeth eisoes yn bodoli). Mae cost *peidio â*'u cadw'n anweledig ar unrhyw ddangosfwrdd, ac mae'n cronni'n dawel gyda phob ymadawiad. I wneud yr achos i arweinyddiaeth, cyfeiriwch at ail-ddarganfyddiad drud diweddar, neu benderfyniad wedi'i wrthdroi a achosodd ddigwyddiad, a nodwch fod y datrysiad bron yn ddi-gost i'w sefydlu.

## Gwrth-batrymau a pheryglon

- **Cofnodi *beth* heb *pam*:** hepgor cyd-destun a dewisiadau eraill a wrthodwyd, sef y pwynt cyfan.
- **Papurwaith ôl-ddigwyddiad:** cofnodion a ysgrifennwyd i fodloni mandad, nid i feddwl; maen nhw'n darllen yn wag ac nid oes neb yn ymddiried ynddynt.
- **Dogfennau anferth aml-benderfyniad:** un dudalen enfawr na all neb lywio na'i disodli'n lân.
- **Honiadau heb ddyddiad:** costau a chyfyngiadau a oedd yn wir unwaith, wedi'u cyflwyno fel rhai bythol.
- **Golygiadau tawel:** newid hanes penderfyniad heb nodyn dyddiedig, gan ddinistrio'r llwybr archwilio.
- **Logiau ysgrifennu-yn-unig:** cofnodion a grëwyd ac na ddaethant byth i'r amlwg ar yr eiliad y maen nhw'n berthnasol, felly nid ydynt yn dylanwadu ar ymddygiad.
- **Gwylio giât talfyriad:** mynnu "ADR" a "pensaernïaeth" ac felly'n annog llai o gyfraniad.
- **Dim cylch bywyd:** cofnodion nad ydynt byth yn cael eu hadolygu, eu disodli, na'u machludo, gan bydru'n gamwybodaeth.

## Model aeddfedrwydd

- **Lefel 1 (Cychwyn):** Mae penderfyniadau'n byw ym mhennau pobl, edafedd sgwrsio, a negeseuon ymrwymo; mae dal yn adweithiol ac yn ad hoc, ac mae rhesymeg yn cael ei cholli'n rheolaidd gyda throsiant staff.
- **Lefel 2 (Datblygu):** Mae rhai timau'n cadw cofnodion, mewn fformatau a thempledi amrywiol, pryd bynnag y bydd unigolyn yn cofio; mae'r arfer yn anghyson ar draws timau, heb log, enwi, na phroses a rennir.
- **Lefel 3 (Safoni):** Mae templed sengl, storio yn yr ystorfa, a chylch bywyd a llywodraethu wedi'u diffinio (meini prawf codi/hepgor, rolau, rhythm adolygu) wedi'u dogfennu ac yn cael eu cymhwyso'n gyson ar draws y sefydliad; mae cofnodion yn cael eu hadolygu a'u disodli yn hytrach na'u golygu'n dawel.
- **Lefel 4 (Rheoli):** Mae'r log penderfyniadau'n cael ei fesur yn erbyn llinellau sylfaen: sylw (cyfran y penderfyniadau pensaernïol arwyddocaol sy'n cario cofnod), ffresni (cyfran y cofnodion a adolygwyd o fewn eu rhythm, ynghyd â chyfrif honiadau heb ddyddiad neu hen), a gallu dod o hyd i wybodaeth (pa mor aml y cyrhaeddodd cofnod perthnasol y datblygwr a newidiodd y cod a lywodraethwyd mewn gwirionedd). Mae cynhalwyr atebol yn gweithredu ar y mesurau hyn, gan ddisodli cofnodion hen a chau bylchau sylw ar sail tystiolaeth yn hytrach nag anecdot.
- **Lefel 5 (Cydgysylltu):** Mae log penderfyniadau traws-dîm y gellir chwilio ynddo wedi'i integreiddio i waith bob dydd: mae cofnodion perthnasol yn dod i'r amlwg yn awtomatig ar y newidiadau y maent yn eu llywodraethu, mae penderfyniadau allweddol yn cael eu sicrhau gan swyddogaethau ffitrwydd mewn integreiddio parhaus, ac mae'r log yn bwydo sefydlu, moderneiddio, ac archwilio fel ased byw. Mae'r sefydliad yn gwella'r arfer ei hun yn barhaus, gan ymddeol, disodli, ac ailgwmpasu cofnodion wrth i'r system a'i chyfyngiadau newid, ac yn ailgydbwyso lle mae'n buddsoddi trylwyredd wrth i bortffolio'r penderfyniadau dyfu.

## Syniadau ar gyfer trafodaeth

1. Beth oedd y penderfyniad diwethaf a wrthdrowyd neu a ailymladdwyd gan eich tîm oherwydd nad oedd neb yn cofio'r rhesymeg wreiddiol?
2. A fyddai ailenwi eich cyfeiriadur `adr/` yn `decisions/` yn newid pwy sy'n cyfrannu a beth sy'n cael ei gofnodi?
3. Pa un o'ch penderfyniadau critigol y gellid ei sicrhau gan swyddogaeth ffitrwydd awtomataidd heddiw?
4. Anghyfnewidiol-a-disodli neu ddogfen fyw: pa un sy'n gweddu i'ch rhwymedigaethau archwilio a'ch diwylliant, a pham?
5. Sut y byddai cyflogai newydd (neu gontractwr olynol) yn darganfod ar hyn o bryd *pam* mae eich system wedi'i siapio fel y mae?
6. Beth sy'n cyfiawnhau codi cofnod penderfyniad ar eich tîm, a beth sy'n cyfiawnhau *peidio â* chodi un?

## Prif negeseuon

- Mae cofnod penderfyniad yn dal un penderfyniad pwysig gyda'i **gyd-destun a'i ganlyniadau**: y *pam*, nid dim ond y *beth*.
- Cadwch gofnodion yn **benodol, wedi'u stampio ag amser, ac yn ysgafn**; safonwch ar un templed (Nygard, MADR, neu debyg).
- Storiwch nhw **mewn rheolaeth fersiynau wrth ymyl y cod**; ystyriwch eu henwi'n "penderfyniadau" i ehangu cyfraniad.
- Diffiniwch **gylch bywyd a llywodraethu** (meini prawf codi/hepgor, rolau, rhythm adolygu); cadwch broses drwm ar gyfer penderfyniadau drws-un-ffordd.
- Gwnewch benderfyniadau'n **hawdd dod o hyd iddynt** ar eiliad y newid ac, lle bo modd, yn **brofadwy** drwy swyddogaethau ffitrwydd.
- Y ROI yw osgoi cost ail-ddarganfod a gwrthdroi anghywir; mae'r achos TCO gryfaf lle mae trosiant, moderneiddio, ac archwilio bwysicaf. Gweler pennod 1.5 (gwneud penderfyniadau a llywodraethu) a phennod 3.1 (sylfeini pensaernïaeth).

## Cyfeiriadau a darllen pellach

- Michael Nygard, "Documenting Architecture Decisions" (2011): yr ADR ysgafn sylfaenol.
- MADR: prosiect Markdown Any Decision Records (adr.github.io/madr).
- Jeff Tyree ac Art Akerman, "Architecture Decisions: Demystifying Architecture" (*IEEE Software*, 2005).
- Olaf Zimmermann, "Y-Statements" and "Architectural Decision Making" (ozimmer.ch).
- Joel Parker Henderson, *Architecture Decision Record (ADR)*: templedi, enghreifftiau, ac arweiniad gwaith tîm (github.com/joelparkerhenderson/architecture-decision-record).
- ThoughtWorks Technology Radar: "Lightweight Architecture Decision Records."
- Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage, *Building Evolutionary Architectures* (swyddogaethau ffitrwydd).
- AWS Prescriptive Guidance, "ADR process"; Red Hat, "Why you should use ADRs."
- Wikipedia, "Architectural decision" and "Architecturally significant requirements."
