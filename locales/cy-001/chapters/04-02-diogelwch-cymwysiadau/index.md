# 4.2 Diogelwch cymwysiadau

## Trosolwg a chymhelliant

Diogelwch cymwysiadau yw lle mae bygythiadau haniaethol yn cwrdd â chod concrid. Mae'r rhan fwyaf o doriadau sy'n cyrraedd y penawdau'n olrhain yn ôl i ddiffyg ar haen cymhwysiad: chwistrelliad, llif dilysu wedi torri, cyfrinach a ddatgelwyd, neu ddibyniaeth wedi'i pheryglu. I dimau mawr sy'n cyflenwi llawer o wasanaethau, nid gwybod bod y diffygion hyn yn bodoli yw'r rhan anodd. Eu hatal yn gyson ar draws ystorfa god eang a ysgrifennwyd gan filoedd o ddwylo dros lawer o flynyddoedd yw'r rhan anodd.

I fentrau, mae diogelwch cymwysiadau'n fater o ymddiriedaeth cwsmeriaid a rhwymedigaeth reoleiddiol. Gall diffyg mewn llif mewngofnodi neu lwybr talu sbarduno twyll, dirwyon, a datgeliad toriad gorfodol. Mae systemau llywodraeth yn wynebu'r un risgiau technegol gyda data risg uwch: cymhwysedd budd-daliadau, cofnodion treth, data cyfiawnder troseddol, a seilwaith cenedlaethol. Yn y ddau leoliad, y cymhwysiad yw'r drws ffrynt, ac mae ymosodwyr yn ei brofi'n gyson ac yn awtomatig.

Mae'r bennod hon yn ymdrin â'r arferion sy'n cadw cymwysiadau'n gydnerth: gwybod amddiffyn yn erbyn dosbarthiadau gwendid cyffredin, dilysu mewnbwn ac amgodio allbwn, cael dilysu ac awdurdodi'n gywir, rheoli cyfrinachau, a diogelu'r gadwyn gyflenwi meddalwedd sydd fwyfwy'n penderfynu eich arwyneb ymosod go iawn.

*Gweler hefyd:* pennod 4.1 (sylfeini diogelwch, modelu bygythiad, a'r cylch bywyd datblygu diogel), pennod 10.3 (cadwyn gyflenwi cod agored a thrwyddedu), a phennod 10.2 (SBOMs, risg, a sicrwydd).

## Egwyddorion allweddol

- **Byth peidiwch ag ymddiried mewn mewnbwn.** Triniwch bob data sy'n croesi ffin ymddiriedaeth fel gelyniaethus hyd nes ei ddilysu.
- **Diofynion diogel.** Dylai'r llwybr diogel fod y llwybr hawdd; dylai ymddygiad anniogel fynnu ymdrech fwriadus, weladwy.
- **Methu ar gau.** Pan na all gwiriad diogelwch gwblhau, gwrthodwch fynediad yn hytrach na'i ganiatáu.
- **Amddiffyn mewn dyfnder ar haen y cymhwysiad.** Cyfunwch ddilysu, amgodio, paramedreiddio, ac amddiffyniadau fframwaith; peidiwch â dibynnu ar un yn unig.
- **Braint leiaf ar gyfer hunaniaethau a thocynnau.** Cwmpaswch dystysgrifau'n gul a gwnewch iddynt ddod i ben yn gyflym.
- **Eich dibyniaethau yw eich cod.** Rydych yn gyfrifol am ddiogelwch popeth rydych yn ei gyflenwi, gan gynnwys cydrannau trydydd parti a chod agored.
- **Safonau dros fyrfyfyrio.** Defnyddiwch fframweithiau wedi'u profi fel [OWASP](https://en.wikipedia.org/wiki/OWASP) (Open Worldwide Application Security Project) ASVS yn hytrach na dyfeisio'ch rheolyddion diogelwch eich hun.

## Argymhellion

### Gwybyddwch ac amddiffynnwch yn erbyn OWASP Top 10, gwiriwch gydag ASVS

Yr OWASP Top 10 yw rhestr sylfaen y diwydiant o'r risgiau cymhwysiad gwe mwyaf critigol: rheolaeth mynediad wedi torri, methiannau cryptograffig, chwistrelliad, cynllun anniogel, camffurfweddiad diogelwch, cydrannau bregus, methiannau dilysu, methiannau uniondeb data, methiannau cofnodi, a ffugio cais ochr-weinydd. Triniwch ef fel gwybodaeth ofynnol i bob peiriannydd, nid dim ond cyfeirnod cydymffurfiaeth i'w ffeilio i ffwrdd.

Ar gyfer safon drylwyr, brofadwy, mabwysiadwch **Safon Dilysu Diogelwch Cymwysiadau OWASP (ASVS)**. Mae ASVS yn diffinio gofynion diogelwch ar dair lefel sicrwydd, gan roi rheolyddion concrid, archwiliadwy i chi ddylunio a phrofi yn eu herbyn. Dewiswch y lefel sy'n ffitio risg pob cymhwysiad, a gwiriwch yn eu herbyn.

### Dilyswch fewnbwn ac amgodiwch allbwn

Mae diffygion chwistrelliad yn aros ymysg y rhai mwyaf niweidiol yn union oherwydd eu bod mor hawdd eu cyflwyno. Amddiffynnwch gyda rheolyddion haenog:

- **Dilyswch fewnbwn** yn erbyn rhestrau caniatáu llym (math disgwyliedig, hyd, fformat, ystod). Gwrthodwch yn hytrach na glanhau lle gallwch.
- **Defnyddiwch ymholiadau paramedreiddiedig** a [gosodiadau parod](https://en.wikipedia.org/wiki/Prepared_statement) ar gyfer pob mynediad cronfa ddata; byth peidiwch â llunio SQL drwy gydgadwyno llinynnau. Defnyddiwch adeiladwyr ymholiad diogel ac ORMs (mapwyr gwrthrych-perthynol) yn gywir.
- **Amgodiwch allbwn** yn gyd-destunol. Mae angen amgodio gwahanol ar HTML, priodoleddau HTML, JavaScript, URLau, a CSS. Dibynnwch ar ddianc awtomatig y fframwaith a deallwch ei derfynau.
- **Atalwch [sgriptio traws-safle](https://en.wikipedia.org/wiki/Cross-site_scripting) (XSS)** gydag amgodio allbwn ynghyd â Pholisi Diogelwch Cynnwys cryf fel ail haen.
- **Atalwch chwistrelliad gorchymyn a thempled** trwy osgoi cregyn-alw gyda data heb ei ymddiried a thrwy ddefnyddio templedi di-resymeg neu wedi'u sandbocsio.

### Cael dilysu ac awdurdodi'n gywir

Mae dilysu'n profi pwy yw defnyddiwr. Mae awdurdodi'n penderfynu beth y cânt ei wneud. Mae'r ddau'n methu'n aml, felly cewch nhw'n gywir.

- Ffafriwch brotocolau sefydledig: **[OAuth 2.0](https://en.wikipedia.org/wiki/OAuth)** ar gyfer awdurdodiad dirprwyedig a **[OpenID Connect](https://en.wikipedia.org/wiki/OpenID_Connect) (OIDC)** ar gyfer dilysu. Peidiwch â'u hadeiladu o'r dechrau.
- Gorfodwch **[ddilysu aml-ffactor](https://en.wikipedia.org/wiki/Multi-factor_authentication) (MFA)**, yn enwedig ar gyfer mynediad breintiedig a gweinyddol.
- Storiwch gyfrineiriau dim ond fel hasau wedi'u halltu gan ddefnyddio algorithm modern, araf, cof-galed (fel [Argon2](https://en.wikipedia.org/wiki/Argon2) neu [bcrypt](https://en.wikipedia.org/wiki/Bcrypt)). Byth peidiwch â storio na chofnodi tystysgrifau testun plaen.
- Rheolwch **sesiynau'n** ofalus: cynhyrchwch docynnau cryptograffig cryf, gosodwch fflagiau cwci diogel a HttpOnly, cylchdrowch ar newid braint, a gwnewch i sesiynau segur ddod i ben.
- Gorfodwch **awdurdodiad ar y gweinydd ar gyfer pob cais**, gan wirio bod y prifathro dilysedig yn berchen ar neu'n cael mynediad i'r adnodd penodol. Mae awdurdodiad lefel-gwrthrych wedi torri (cael mynediad i gofnod defnyddiwr arall drwy newid ID) yn un o'r diffygion API mwyaf cyffredin a difrifol.
- Canoli rhesymeg awdurdodi lle mae'n ymarferol fel bod polisi'n gyson ac yn archwiliadwy.

### Rheolwch gyfrinachau a chylchdrowch allweddi

Mae cyfrinachau wedi'u codio'n galed mewn cod ffynhonnell yn achos parhaus o doriadau. Adeiladwch arferiad disgybledig o amgylch rheoli cyfrinachau:

- Storiwch gyfrinachau mewn rheolwr cyfrinachau neu gladdgell benodedig, byth mewn ffynhonnell, ffeiliau ffurfweddu, neu newidynnau amgylchedd a wiriwyd i mewn i reolaeth fersiynau.
- Sganiwch ymrwymiadau ac ystorfeydd am gyfrinachau a ollyngwyd yn awtomatig, a blociwch gyfuniadau sy'n eu cyflwyno.
- Cylchdrowch allweddi a thystysgrifau'n rheolaidd ac yn syth ar unrhyw ddatgeliad a amheuir. Ffafriwch dystysgrifau byrhoedlog, a gyhoeddir yn awtomatig dros rai statig, hirhoedlog.
- Cymhwyswch fraint leiaf i bob cyfrinach: cwmpaswch hi i'n union yr hyn sydd ei angen arni.
- Amgryptiwch gyfrinachau yn eu gorffwys ac ar dramwy, ac archwiliwch fynediad iddynt.

### Diogelwch y gadwyn gyflenwi meddalwedd

Mae cymwysiadau modern wedi'u cydosod yn bennaf o gydrannau trydydd parti, sy'n gwneud y gadwyn gyflenwi'n arwyneb ymosod cynradd.

- Cynhaliwch **[Fil Deunyddiau Meddalwedd](https://en.wikipedia.org/wiki/Software_bill_of_materials) (SBOM)** ar gyfer pob cymhwysiad fel eich bod yn gwybod yn union beth rydych yn ei gyflenwi a gallwch ymateb yn gyflym pan fydd gwendid newydd yn glanio.
- Sganiwch ddibyniaethau'n barhaus (Dadansoddiad Cyfansoddiad Meddalwedd, neu SCA) a datrys cydrannau gwybyddus-fregus yn brydlon.
- Pinio a gwiriwch fersiynau dibyniaeth; defnyddiwch ffeiliau clo a chofrestrfeydd ymddiriedig.
- Mabwysiadwch **SLSA** (Supply-chain Levels for Software Artifacts) i godi uniondeb adeiladu, a chynhyrchwch dystebau **tarddiad** yn disgrifio sut y cafodd arteffactau eu hadeiladu.
- **Llofnodwch arteffactau** a gwiriwch lofnodion cyn defnyddio fel y gallwch ymddiried mai'r hyn rydych wedi'i adeiladu sy'n rhedeg.
- Diogelwch y system adeiladu ei hun; gall biblinell CI wedi'i pheryglu chwistrellu cod maleisus i mewn i bob defnyddiwr i lawr yr afon.

## Cyfaddawdau: manteision ac anfanteision

| Penderfyniad | Manteision | Anfanteision |
|---|---|---|
| Prynu/mabwysiadu darparwr hunaniaeth (OIDC) | Wedi'i brofi mewn brwydr, MFA wedi'i adeiladu i mewn, llai o god i'w ddiogelu | Dibyniaeth gwerthwr, ymdrech integreiddio, cost |
| Adeiladu dilysiad pwrpasol | Rheolaeth lawn, dim dibyniaeth allanol | Hynod hawdd ei gael yn anghywir, cynnal a chadw uchel |
| Dilysu rhestr caniatáu llym | Yn blocio dosbarthiadau gwendid cyfan | Gall dorri achosion ymyl dilys, mwy o waith ymlaen llaw |
| Tystysgrifau byrhoedlog | Ffenestr toriad fach, dad-alluogi awtomatig | Angen seilwaith cyhoeddi cadarn |
| Diweddariadau dibyniaeth ymosodol | Llai o wendidau gwybyddus | Chwyrndroad, newidiadau torri posibl, baich profi |
| SBOM + llofnodi + tarddiad | Ymateb digwyddiad cyflym, ymddiriedaeth wiriadwy | Buddsoddiad offer a phroses, newid diwylliannol |

Y cyfaddawd cylchol yw trylwyredd ymlaen llaw yn erbyn amlygiad parhaus. Mae adeiladu dilysiad pwrpasol neu hepgor hylendid dibyniaeth yn teimlo'n gyflymach heddiw ac yn eich costio'n aruthrol wedyn. Mae mabwysiadu safonau wedi'u profi a rheolyddion cadwyn gyflenwi awtomataidd yn costio ymdrech nawr, ond mae'n troi risg diderfyn, anrhagweladwy'n un rheoledig, wedi'i ffinio. I dimau mawr, y lluosydd awtomeiddio sy'n bwysicaf: mae rheolydd a gymhwysir unwaith mewn templed ffordd-arwyn yn amddiffyn pob gwasanaeth sy'n ei ddefnyddio.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Pa reolyddion ASVS y byddwch yn eu pobi i mewn i'ch fframwaith ffordd-arwyn fel bod peirianwyr yn eu cael am ddim?** Y symudiad â'r trosoledd uchaf i dîm mawr yw gwneud y llwybr diogel yn ddiofyn, fel bod rheolydd a ysgrifennwyd unwaith mewn fframwaith a rennir yn amddiffyn pob gwasanaeth sy'n ei fabwysiadu. Penderfynwch pa ofynion ASVS (ymholiadau paramedreiddiedig, amgodio allbwn, fflagiau sesiwn diogel, gwiriadau awdurdodi ochr-weinydd) sy'n perthyn yn y templed yn hytrach nag yng nghof pob peiriannydd. Ar gyfer portffolios mentrau a llywodraeth, penderfynwch hefyd pa gymwysiadau sydd angen ASVS Lefel 2 yn erbyn Lefel 3, a chysylltwch hynny â sensitifrwydd y data y mae pob un yn ei gyffwrdd. Dewch â rhestr o'ch gwasanaethau a nodwch pa rai sydd eisoes yn etifeddu'r diofynion hyn a pha rai sy'n ailweithredu diogelwch â llaw, oherwydd dyna lle mae chwistrelliad a rheolaeth mynediad wedi torri'n cuddio. Os yw diofynion diogel yn byw dim ond ar dudalen wici, cânt eu hepgor o dan bwysau cyflenwi, felly rhowch nhw mewn cod.

2. **Sut byddwch chi'n dod o hyd i awdurdodiad lefel-gwrthrych wedi torri ac yn ei drwsio ar draws pob API, nid dim ond y rhai newydd?** Mae cael mynediad i gofnod defnyddiwr arall drwy newid ID yn un o'r diffygion API mwyaf cyffredin a difrifol, ac mae'n cuddio mewn pwyntiau terfyn hŷn sy'n rhagflaenu eich safonau cyfredol. Awdurdodiad ochr-weinydd ar bob cais a phob gwrthrych yw'r rheol, ond y rhan anodd yw gwirio ei fod yn dal ar draws ystorfa god eang, degawdau oed a ysgrifennwyd gan lawer o ddwylo. Penderfynwch a fyddwch yn canoli rhesymeg awdurdodi, ychwanegu profion awtomataidd sy'n ceisio mynediad traws-denant, neu redeg profi wedi'i dargedu yn erbyn eich APIau risg uchaf yn gyntaf. Dewch â'ch rhestr o bwyntiau terfyn sy'n datgelu dynodwyr gwrthrych a'u graddio yn ôl sensitifrwydd yr hyn y maent yn ei ddychwelyd. Heb ysgubiad bwriadus, byddwch yn parhau i gyflenwi'r diffyg hwn ac yn ei ddarganfod dim ond pan fydd ymchwilydd neu ymosodwr yn gwneud hynny.

3. **Beth yw eich cynllun ar gyfer y gwendid dibyniaeth eang nesaf: pa mor gyflym allwch chi ddod o hyd i a thrwsio pob gwasanaeth yr effeithir arno?** Pan fydd diffyg critigol yn glanio mewn llyfrgell boblogaidd, mae'r cwmnïau ag SBOM cywir yn adnabod gwasanaethau yr effeithir arnynt o fewn oriau tra bo eraill yn treulio wythnosau'n chwilio, ac mae'r bwlch cyflymder hwnnw'n penderfynu faint o ddifrod rydych yn ei gymryd. Penderfynwch nawr a fyddwch yn cynhyrchu Bil Deunyddiau Meddalwedd ar gyfer pob arteffact, a yw sganio dibyniaeth yn rhedeg ym mhob piblinell, a phwy sy'n berchen ar y penderfyniad clytio brys. Ar gyfer prynwyr rheoledig a llywodraeth, mae SBOMs a tharddiad wedi'i lofnodi fwyfwy'n amod ar gyfer gwneud busnes, felly mae'r parodrwydd hwn hefyd yn diogelu refeniw. Dewch â'r ateb gonest i ymarfer diogelu: dewiswch lyfrgell rydych yn ei defnyddio'n eang ac amserwch pa mor hir mae'n ei gymryd i restru pob gwasanaeth sy'n ei chyflenwi. Os yw'r ateb yn cael ei fesur mewn dyddiau, buddsoddwch mewn rhestr eiddo a llofnodi cyn i'r digwyddiad nesaf eich gorfodi i wneud hynny.

4. **Sut byddwch chi'n symud o gyfrinachau statig, hirhoedlog i dystysgrifau byrhoedlog, a gyhoeddir yn awtomatig, a pha systemau sy'n blocio hynny heddiw?** Mae cyfrinachau wedi'u codio'n galed a hirhoedlog yn achos toriad parhaus, ac mae'r ateb, tystysgrifau byrhoedlog a gyhoeddir ar alw, yn dibynnu ar seilwaith cyhoeddi na all hen systemau ei ddefnyddio'n aml. I dîm mawr y perygl yw mabwysiadu anwastad: mae platfform modern yn cylchdroi allweddi bob awr tra bod gwasanaeth etifeddol yn dal i gyflenwi cyfrinair cronfa ddata statig mewn ffeil ffurfweddu. Penderfynwch pa lwythi gwaith all ddefnyddio rheolwr cyfrinachau neu system hunaniaeth-llwyth-gwaith nawr, pa rai sydd angen buddsoddiad yn gyntaf, a phwy sy'n berchen ar y llawlyfr cylchdroi y foment yr amheuir bod allwedd wedi'i gollwng. Dewch â rhestr eiddo o bob tystysgrif sydd ar waith, ei hoes, ei radiws ffrwydro os caiff ei ddatgelu, ac a fyddai sganio ymrwymiadau'n ei ddal cyn cyfuno. Mewn lleoliadau mentrau a llywodraeth, cysylltwch hyn ag archwiliad: mae archwilwyr fwyfwy'n disgwyl tystiolaeth o gylchdroi, mynediad wedi'i gwmpasu, a chofnodi mynediad ar gyfer pob cyfrinach, ac mae tystysgrif statig na allwch ei chylchdroi heb amser segur yn ganfyddiad sy'n aros i gael ei ysgrifennu i fyny.

5. **Ble ydych chi'n dal i redeg dilysiad cartref neu anghyson, a beth yw'r cynllun i gyfuno ar brotocolau wedi'u profi?** Mae adeiladu dilysiad yn un o'r ffyrdd hawsaf o gyflwyno diffygion cynnil, y gellir eu hecsbloetio, ac eto mae gan y rhan fwyaf o ystadau mawr o leiaf un llif mewngofnodi etifeddol sy'n rhagflaenu'r penderfyniad i safoni ar OAuth 2.0 ac OIDC. Mae'r pwysau cystadleuol yn real: mae mudo hen lif yn peryglu torri defnyddwyr ac integreiddiadau presennol, tra bod ei adael yn ei le'n cadw targed gwerth uchel dan ei amddiffyn. Penderfynwch a fyddwch yn cyfuno ar un darparwr hunaniaeth, yn gorfodi MFA yn unffurf, ac yn gosod terfyn amser i ymddeol pob llif pwrpasol, neu'n derbyn eithriadau wedi'u dogfennu gyda rheolyddion iawndal. Dewch â map o bob llwybr dilysu yn y fflyd, pa rai sy'n gorfodi MFA, pa rai sy'n storio cyfrineiriau gyda hash cof-galed modern, a pha rai sy'n bwrpasol. Ar gyfer portffolios mentrau a llywodraeth, ychwanegwch yr ongl cydymffurfiaeth: mae safonau fel NIST SP 800-63 yn gosod disgwyliadau concrid ar gyfer sicrwydd hunaniaeth, ac ni fydd llif cartref na all eu dangos yn goroesi archwiliad na adolygiad awdurdod-i-weithredu.

6. **Sut ydych chi'n gwirio bod y rheolyddion hyn mewn gwirionedd yn dal mewn cynhyrchu, ac a allwch chi ei brofi gyda thystiolaeth yn hytrach na honiad?** Nid yw ysgrifennu diofyn diogel yr un fath â gwybod bod pob gwasanaeth yn dal i'w anrhydeddu, ac mae rheolyddion yn pydru'n dawel wrth i god newid, eithriadau bentyrru, a phwyntiau terfyn newydd gyflenwi. I dîm mawr y cwestiwn yw cwmpas: pa wasanaethau sy'n rhedeg dadansoddiad statig, sganio dibyniaeth, a phrofi deinamig neu dreiddiad, a sut ydych chi'n gwybod nad y rhai sy'n eu hepgor yw eich cymwysiadau risg uchaf? Penderfynwch beth sy'n orfodol yn y biblinell yn erbyn cyfnodol, pwy sy'n trioli'r canfyddiadau, a pha dystiolaeth rydych yn ei chadw i ddangos bod rheolydd wedi'i brofi ac yn llwyddo ar ddyddiad penodol. Dewch â'ch map cwmpas cyfredol, eich amser cymedrig i unioni yn ôl difrifoldeb, a'r rhestr o gymwysiadau heb brawf diweddar. Mewn cyd-destunau rheoledig a llywodraeth, nid yw'r dystiolaeth hon yn ddewisol: mae archwilwyr, swyddogion awdurdodi, ac ymchwilwyr toriad i gyd yn gofyn am brawf bod rheolyddion wedi'u gwirio, ac anaml y mae polisi heb gofnodion prawf yn eu bodloni.

## Lens sector

**Cwmni newydd.** Gyda dau neu dri pheiriannydd a dim arbenigwr diogelwch, eich trosoledd yw etifeddu diogelwch yn hytrach na'i adeiladu: mabwysiadwch ddarparwr hunaniaeth OIDC wedi'i reoli, pwyswch ar fframwaith y mae ei ORM yn paramedreiddio ymholiadau'n ddiofyn, a chadwch gyfrinachau yn rheolwr cyfrinachau eich platfform yn hytrach na ffeiliau `.env` y gallai cyd-weithiwr eu hymrwymo'n ddamweiniol. Trowch ymlaen sganio dibyniaeth awtomataidd sy'n agor ceisiadau tynnu clytio, a thriniwch hynny fel digon am y tro. Peidiwch ag adeiladu dilysiad neu gryptograffeg pwrpasol, oherwydd gall un ymholiad wedi'i chwistrellu neu un allwedd wedi'i gollwng ddod â'r cwmni i ben cyn iddo gael cwsmeriaid.

**Busnes bach.** Mae'n debyg nad oes gennych arbenigwr diogelwch cymwysiadau a bod gennych gyllideb dynn, felly prynwch reolyddion wedi'u mewnblannu yn yr offer a'r platfformau rydych eisoes yn talu amdanynt yn hytrach na staffio swyddogaeth benodedig. Dewiswch ddarparwr hunaniaeth wedi'i westeio gydag MFA wedi'i gynnwys, cronfa ddata wedi'i rheoli sy'n eich llywio tuag at fynediad paramedreiddiedig, a gwesteiwr ystorfa sy'n sganio ymrwymiadau am gyfrinachau a ollyngwyd yn syth o'r bocs. Canolbwyntiwch eich sylw prin ar sylfeini OWASP Top 10 sy'n achosi'r rhan fwyaf o doriadau byd-go-iawn, a ffafriwch werthwyr sy'n cyflenwi diofynion diogel na allwch eu diffodd yn ddamweiniol.

**Menter.** Ar draws llawer o dimau'r her yw cysondeb: pobwch reolyddion ASVS i mewn i fframweithiau ffordd-arwyn fel bod pob gwasanaeth newydd yn etifeddu ymholiadau paramedreiddiedig, amgodio allbwn, sesiynau diogel, ac awdurdodiad ochr-weinydd am ddim. Rhedwch SBOMs cywir a sganio dibyniaeth ar draws y fflyd fel bod y gwendid llyfrgell eang nesaf yn fater o oriau, nid wythnosau, a chanolwch bolisi awdurdodi fel bod mynediad traws-denant yn dod yn brofadwy. Safonwch ar un darparwr hunaniaeth gydag MFA wedi'i orfodi, a rheolwch ddiogelwch cymwysiadau fel portffolio llywodraethol gyda lefelau ASVS wedi'u graddio yn ôl risg a thystiolaeth wedi'i harchwilio.

**Llywodraeth.** Mae rheolau caffael, tryloywder, ac atebolrwydd cyhoeddus yn siapio'r rheolyddion y mae'n rhaid i chi eu dangos, nid dim ond eu gweithredu. Gwiriwch wasanaethau sy'n wynebu dinasyddion yn erbyn OWASP ASVS ar lefel sy'n cyfateb i sensitifrwydd data, llofnodwch bob arteffact a ddefnyddir a thystiwch ei darddiad yn ôl SLSA i fodloni mandadau cadwyn gyflenwi, a chyhoeddwch dystysgrifau byrhoedlog o gladdgell ganolog gyda chofnodi mynediad llawn. Disgwyliwch ddangos i archwilwyr a swyddogion awdurdodi gadwyn ddogfennedig o gadwraeth o ffynhonnell i gynhyrchu, ac aliniwch sicrwydd hunaniaeth â safonau cyhoeddedig fel NIST SP 800-63.

## Enghreifftiau

**Cwmni newydd.** Mae tîm SaaS tri pheiriannydd yn hepgor adeiladu ei fewngofnodi ei hun ac yn mabwysiadu darparwr OIDC wedi'i reoli ar ddiwrnod cyntaf, gan ennill MFA ac ailosodiadau cyfrinair diogel heb ysgrifennu cod critigol o ran diogelwch na all fforddio ei gael yn anghywir. Mae'n dibynnu ar ORM y fframwaith fel bod ymholiadau'n baramedreiddiedig yn ddiofyn, yn cadw cyfrinachau yn rheolwr cyfrinachau'r platfform yn hytrach nag mewn ffeiliau `.env` y gallai cyd-weithiwr eu hymrwymo'n ddamweiniol, ac yn troi ymlaen sganio dibyniaeth awtomataidd sy'n agor cais tynnu pan fydd angen clytio llyfrgell. Nid yw dim o hyn yn arafu'r tîm, ac mae'n golygu nad yw un allwedd a gollwyd neu un ymholiad wedi'i chwistrellu'n dod â'r cwmni i ben cyn iddo gael cwsmeriaid.

**Menter.** Mae platfform manwerthu sy'n gwasanaethu degau o filiynau o siopwyr yn safoni dilysiad ar OIDC drwy un darparwr hunaniaeth, gan orfodi MFA i staff a dilysiad cam-i-fyny ar gyfer newidiadau cyfrif gwerth uchel. Mae pob mynediad cronfa ddata'n mynd trwy ORM wedi'i ffurfweddu i baramedreiddio ymholiadau, ac mae Polisi Diogelwch Cynnwys yn cefnogi amgodio allbwn. Ar ôl gwendid a gyhoeddwyd yn eang mewn llyfrgell gofnodi boblogaidd, mae SBOM y cwmni'n gadael iddo adnabod pob gwasanaeth yr effeithir arno o fewn oriau a'u clytio mewn dau ddiwrnod, tra bod cystadleuwyr heb restrau eiddo wedi treulio wythnosau'n chwilio.

**Llywodraeth.** Mae asiantaeth budd-daliadau ffederal yn adeiladu gwasanaethau sy'n wynebu dinasyddion wedi'u gwirio yn erbyn OWASP ASVS Lefel 2, gyda Lefel 3 ar gyfer y cydrannau sy'n trin y cofnodion mwyaf sensitif. Mae cyfrinachau'n byw mewn claddgell ganolog yn cyhoeddi tystysgrifau byrhoedlog; mae sganio ymrwymiadau'n blocio unrhyw allwedd a ollyngwyd. Mae pob arteffact a ddefnyddir wedi'i lofnodi a'i darddiad wedi'i dystio yn ôl SLSA, gan fodloni mandad ffederal ar gyfer cadwynau cyflenwi meddalwedd gwiriadwy a rhoi cadwyn cadwraeth glir i archwilwyr o ffynhonnell i gynhyrchu.

## Achos busnes: cymhellion, ROI, a TCO

Mae gwariant diogelwch cymwysiadau'n prynu i lawr y categori mwyaf tebygol a drutaf o doriad. Mae'r gost gyfanswm perchnogaeth yn cynnwys offer (sganwyr, rheolwyr cyfrinachau, darparwyr hunaniaeth), amser peiriannydd i unioni canfyddiadau, a ffrithiant ysgafn diofynion diogel. Yn erbyn hynny, pwyswch gost ei hepgor: mae toriadau chwistrelliad a rheolaeth mynediad wedi torri'n rheolaidd yn datgelu miliynau o gofnodion, gan sbarduno dirwyon rheoleiddiol, hysbysiad gorfodol, colledion twyll, sbrintiau unioni, a niwed i enw da sy'n atal refeniw am flynyddoedd.

Mae'r ROI ar ei gryfaf pan fydd rheolyddion wedi'u hawtomeiddio a'u hailddefnyddio. Mae un integreiddiad hunaniaeth wedi'i ffurfweddu'n dda, un haen ymholiad wedi'i galedu mewn fframwaith a rennir, ac un biblinell sy'n blocio dibyniaethau bregus yn amddiffyn y fflyd gyfan am gost ymylol fesul gwasanaeth. Mae rheolyddion cadwyn gyflenwi'n arbennig wedi mynd o ddewisol i hanfodol: gall dibyniaeth wedi'i pheryglu droi pob un o'ch cwsmeriaid yn ddioddefwr, ac mae rheoleiddwyr a phrynwyr mentrau fwyfwy'n mynnu SBOMs a tharddiad wedi'i lofnodi fel amod ar gyfer gwneud busnes. Pan fyddwch yn gwneud yr achos i arweinyddiaeth, cysylltwch y buddsoddiad â risgiau penodol, wedi'u henwi ac â gofynion caffael a chydymffurfiaeth sy'n blocio refeniw os byddwch yn methu eu bodloni.

## Gwrth-batrymau a pheryglon

- **Rholio'ch cryptograffeg neu ddilysiad eich hun.** Bron bob amser yn cynhyrchu diffygion cynnil, y gellir eu hecsbloetio.
- **Dilysu ochr-cleient yn unig.** Yn cael ei osgoi'n ddibwys; mae'n rhaid i'r gweinydd ailddilysu popeth.
- **Glanhau rhestr rwystro.** Ceisio strippio nodau "gwael" yn hytrach na chaniatáu-restru rhai da; mae ymosodwyr yn dod o hyd i'r bylchau.
- **Cyfrinachau mewn ffeiliau ffynhonnell neu amgylchedd.** Yr achos mwyaf cyffredin sengl o ollyngiadau tystysgrif.
- **Anwybyddu awdurdodiad ar fynediad gwrthrych.** Tybio y gall defnyddiwr dilysedig gael mynediad i unrhyw wrthrych y gall ddyfalu ei ID.
- **Dibyniaethau gosod-ac-anghofio.** Byth diweddaru cydrannau trydydd parti nes bod toriad yn ei orfodi.
- **Trin y Top 10 fel y llinell derfyn.** Mae'n llawr, nid safon gynhwysfawr; defnyddiwch ASVS am ddyfnder.
- **Cofnodi data sensitif.** Mae cyfrineiriau, tocynnau, a PII (gwybodaeth adnabyddadwy'n bersonol) mewn cofnodion yn dod yn doriad sy'n aros i ddigwydd.

## Model aeddfedrwydd

**Lefel 1: Cychwyn.** Mae diogelwch cymwysiadau'n dibynnu ar wybodaeth datblygwr unigol ac yn ymateb dim ond ar ôl digwyddiadau. Dim rheolyddion safonol. Mae cyfrinachau'n eistedd mewn ffynhonnell. Anaml y caiff dibyniaethau eu diweddaru. Mae dilysiad yn bwrpasol ac yn achlysurol, a chanfyddir diffygion chwistrelliad neu reolaeth mynediad wedi torri drwy lwc yn hytrach na thrwy broses.

**Lefel 2: Datblygu.** Mae arferion sylfaenol yn ymddangos ond yn amrywio o dîm i dîm. Mae ymwybyddiaeth OWASP Top 10 yn lledaenu, mae rhai amddiffyniadau lefel-fframwaith ar waith, ac mae rheolwr cyfrinachau'n bodoli ond caiff ei ddefnyddio'n anwastad. Mae sganio dibyniaeth yn rhedeg yn achlysurol. Mae systemau newydd yn mabwysiadu darparwr hunaniaeth safonol, tra bod gwasanaethau hŷn yn cadw eu llifoedd mewngofnodi cartref heb eu cyffwrdd.

**Lefel 3: Safoni.** Caiff rheolyddion eu dogfennu a'u gorfodi ar draws y sefydliad. Gosodir gofynion seiliedig ar ASVS fesul haen risg, mae ymholiadau paramedreiddiedig ac amgodio allbwn yn norm, a mynnir darparwr hunaniaeth canolog gydag MFA. Rheolir a sganir cyfrinachau'n awtomatig, cynhyrchir SBOMs, ac mae sganio dibyniaeth yn rhedeg ym mhob piblinell.

**Lefel 4: Rheoli.** Caiff yr arfer ei fesur a'i reoli yn erbyn llinellau sylfaen. Caiff cwmpas sganio a phrofi, amser cymedrig i unioni yn ôl difrifoldeb, cyfran y gwasanaethau sy'n etifeddu diofynion ffordd-arwyn, oedran cylchdroi tystysgrif a chyfrinach, a chydymffurfiaeth ASVS eu holrhain oll ar ddangosfyrddau. Caiff eithriadau eu cofnodi gyda dyddiadau dod i ben, mae gwyriad o'r llinell sylfaen yn sbarduno gweithredu, a chaiff rhyddhadau eu giatio ar drothwyon diogelwch diffiniedig yn hytrach na galwadau barn.

**Lefel 5: Cyfluniadu.** Caiff diogelwch ei wella'n barhaus a'i integreiddio ar draws y sefydliad. Mae diofynion diogel wedi'u hadeiladu i mewn i fframweithiau ffordd-arwyn fel bod y llwybr diogel yn awtomatig, defnyddir tystysgrifau byrhoedlog ym mhobman, ac mae sicrwydd cadwyn gyflenwi llawn gyda llofnodi a tharddiad (SLSA) yn safonol. Mae gwiriad yn barhaus, mae ymateb i wendidau newydd yn gyflym ac wedi'i fesur, ac mae pob digwyddiad yn bwydo'n ôl i mewn i'r templedi a rennir fel bod un trwsiad yn caledu'r fflyd gyfan.

## Syniadau i'w trafod

1. Ble ddylai rhesymeg awdurdodi fyw i fod yn gyson ac yn gynhaliadwy ar draws llawer o wasanaethau?
2. Pa mor ymosodol y dylech ddiweddaru dibyniaethau o ystyried y cyfaddawd rhwng amlygiad a chwyrndroad?
3. Pa lefel ASVS sy'n briodol ar gyfer pob dosbarth cymhwysiad yn eich portffolio?
4. Sut ydych chi'n dileu cyfrinachau hirhoedlog heb greu seilwaith cyhoeddi bregus?
5. Beth fyddai ei angen ar eich sefydliad i gynhyrchu a defnyddio SBOMs a tharddiad ar gyfer pob arteffact?
6. Sut ydych chi'n atal diofynion diogel rhag cael eu hanalluogi o dan bwysau cyflenwi?

## Prif gasgliadau

- Mae'r OWASP Top 10 yn wybodaeth hanfodol; mae ASVS yn darparu'r safon brofadwy.
- Haenwch ddilysu mewnbwn, paramedreiddio, ac amgodio allbwn i drechu chwistrelliad a XSS.
- Defnyddiwch brotocolau wedi'u profi (OAuth 2.0, OIDC) a gorfodwch MFA; byth peidiwch ag adeiladu dilysiad o'r dechrau.
- Gorfodwch awdurdodiad ochr-weinydd ar gyfer pob cais a phob gwrthrych.
- Cadwch gyfrinachau allan o ffynhonnell, eu rheoli'n ganolog, a'u cylchdroi i dystysgrifau byrhoedlog.
- Mae'r gadwyn gyflenwi'n arwyneb ymosod cynradd; defnyddiwch SBOMs, SCA, llofnodi, a tharddiad (SLSA).
- Mae rheolyddion awtomataidd, ailddefnyddiadwy'n amddiffyn y fflyd gyfan am gost ymylol fesul gwasanaeth.

## Cyfeiriadau a darllen pellach

- OWASP, *Top 10 Web Application Security Risks*
- OWASP, *Application Security Verification Standard (ASVS)*
- OWASP, *Cheat Sheet Series* (Input Validation, Authentication, Authorization, Secrets Management)
- Dafydd Stuttard and Marcus Pinto, *The Web Application Hacker's Handbook*
- Aaron Parecki, *OAuth 2.0 Simplified*
- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines*
- Cloud Native Computing Foundation and OpenSSF, *SLSA framework* and *Supply-chain Security guidance*
