# 1.7 Safonau peirianneg ac eithriadau

## Trosolwg a chymhelliant

Mae **safon beirianneg** yn rheol wedi'i dogfennu a chytuno arni ynghylch sut y gwneir gwaith. Er enghraifft, "rhaid i bob gwasanaeth ddatgelu pwynt terfyn gwiriad-iechyd," neu "rhaid i bob tudalen we gyhoeddus fodloni **[WCAG](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (Web Content Accessibility Guidelines) 2.2 lefel AA**." Nid awgrym yw safon, ac nid confensiwn yn unig. Mae'n ymrwymiad y mae'r sefydliad yn ei ddal ei hun ato, yn ddelfrydol un y gallwch ei wirio. Mae'r bennod hon yn ymdrin â chylchred lawn safonau, sut y mae sefydliad mawr yn eu **hawduro, cyhoeddi, mabwysiadu, gorfodi, a datblygu**, ac, yr un mor bwysig, sut y mae'n trin yr achosion sy'n disgyn yn ddilys y tu allan iddynt trwy **broses eithriadau** lywodraethol (a elwir hefyd yn **broses hepgor**): caniatâd wedi'i dogfennu, wedi'i amser-focsio, i wyro oddi wrth safon am reswm penodedig.

Y cymhelliant yw bod normau anffurfiol yn peidio â gweithio ar raddfa. Pan fo pum peiriannydd yn rhannu un ystafell, mae "sut yr ydym yn gwneud pethau yma" yn teithio trwy sgwrs ac osmosis. Pan fo pum mil o beirianwyr yn ymestyn ar draws dwsinau o dimau, tri chylchfa amser, a degawd o drosiant staff, mae'r wybodaeth ddealledig honno'n dryllio'n gannoedd o arferion lleol anghydnaws. Safonau yw sut yr ydych yn ysgrifennu eich gwersi caled-eu-hennill unwaith, fel bod pob tîm yn eu hetifeddu yn hytrach nag ailddysgu pob un trwy ei doriad ei hun. Maent yn lleihau [llwyth gwybyddol](https://en.wikipedia.org/wiki/Cognitive_load), yn gwneud [adolygiadau cod](https://en.wikipedia.org/wiki/Code_review) yn ymwneud â sylwedd yn hytrach nag arddull, yn gadael i bobl symud rhwng timau, ac yn rhoi rhywbeth pendant i archwilwyr a rheoleiddwyr ei asesu.

Ond mae gan safonau eu modd methiant eu hunain: anhyblygrwydd. Bydd safon nad yw'n derbyn unrhyw eithriadau, yn hwyr neu'n hwyrach, yn blocio gwaith dilys: sbeic, cyfyngiad gwerthwr, achos gwirioneddol newydd na ddychmygodd yr awduron erioed. Yna mae timau naill ai'n dod i stop llwyr neu, yn waeth, yn distaw anwybyddu'r safon, sy'n erydu credadwyedd *pob* safon. Y feddyginiaeth yw'r hen ddihareb "mae'r eithriad yn profi'r rheol." Proses eithriadau weladwy, egwyddorol yw'r hyn sy'n cadw safonau'n gredadwy ac yn ddyngar fel ei gilydd. Mae'r bennod hon yn adeiladu ar wneud penderfyniadau a llywodraethu (pennod 1.5) a chofnodion penderfyniad (pennod 1.6), ac yn bwydo'n uniongyrchol i mewn i safonau ac arddull codio (pennod 2.1), rhestrau gwirio (pennod 12.2), a thempledi (pennod 12.3).

## Egwyddorion allweddol

- **Mae safon yn nodi canlyniad, ac yn rhoi rheswm.** Rheol ynghyd â rhesymeg; heb y *pam*, ni all pobl farnu pryd y mae'n wirioneddol berthnasol.
- **Os na ellir ei wirio, nid yw'n safon eto.** Ffafriwch ddatganiadau y gellir eu profi dros ddyheadau.
- **Mae safonau'n ddogfennau byw.** Cânt eu fersiynu, eu perchnogi, eu dyddio, a'u diwygio, nid eu naddu mewn carreg a'u gadael.
- **Awtomeiddiwch orfodaeth lle gallwch; cadwch adolygiad dynol ar gyfer barn.** Mae peiriannau'n gwirio'r mecanyddol; mae pobl yn gwirio'r ystyrlon.
- **Disgwylir gwyriadau, ac nid ydynt yn gywilyddus, ond rhaid iddynt fod yn weladwy.** Mae hepgoriad gonest yn curo anghydymffurfiad distaw bob tro.
- **Amser-focsiwch bob eithriad.** Mae eithriad parhaol yn ddiffyg yn y safon; dewch ag ef i'r amlwg a thrwsio'r safon.
- **Geiriau ac enghreifftiau dros jargon a gorchmynion.** Mae pobl yn dilyn safonau y maent yn eu deall ac y gallant gopïo ohonynt.

## Argymhellion

### Ysgrifennu safonau sy'n glir, y gellir eu profi, ac wedi'u cyfiawnhau

Mae safon dda yn ddogfen fer, hunangynhwysol gyda siâp rhagweladwy fel bod darllenwyr yn gwybod ble i edrych. Mabwysiadwch un **templed safon** (pennod 12.3) a'i defnyddio ym mhobman. Mae adrannau hanfodol yn cynnwys:

- **Teitl ac adnabyddwr:** enw sefydlog a rhif cyfeirnod ar gyfer dyfynnu.
- **Statws:** drafft, gweithredol, wedi'i ddisodli, neu wedi ymddeol, gyda dyddiad.
- **Y rheol:** wedi'i nodi fel canlyniad, yn glir ac yn ddiamwys ("rhaid," "dylai," "gall," wedi'u defnyddio'n fwriadol, yn ôl confensiynau **RFC 2119** ar gyfer geiriau allweddol gofyniad).
- **Rhesymeg:** *pam* y mae'r rheol hon yn bodoli; y gost neu'r risg y mae'n ei hatal.
- **Enghreifftiau:** enghraifft gydymffurfiol ac un anghydymffurfiol; mae'r diriaethol yn curo'r haniaethol.
- **Sut y'i gwirir:** y prawf awtomataidd, rheol linter, neu gam adolygu sy'n ei ddilysu.
- **Perchennog a dyddiad adolygu:** pwy sy'n ei chynnal a phryd yr ailedrychir arni nesaf.

Y meysydd rhesymeg a "sut y'i gwirir" yw'r hyn sy'n gwahanu safon go iawn oddi wrth ddymuniad. Os na allwch ddweud pam y mae rheol yn bodoli, cwestiynwch a ddylai. Os na allwch ddweud sut y dilysir cydymffurfiaeth, caiff y rheol ei chymhwyso'n anghyson a'i digio.

### Paru pob safon â rhestr wirio arfer da

Mae safonau'n diffinio'r cyrchfan. Mae **rhestr wirio arfer da**, rhestr fer, drefnus o gamau neu eitemau pendant i'w cadarnhau, yn helpu pobl i gyrraedd yno ac yn eu galluogi i hunanwirio cyn adolygiad. Mae llawlyfrau peirianneg y sector cyhoeddus yn defnyddio'r patrwm hwn yn helaeth. Mae **[NHS Cymru](https://en.wikipedia.org/wiki/NHS_Wales)** ac **Iechyd a Gofal Digidol Cymru (DHCW)** yn cyhoeddi safonau peirianneg gyda rhestrau gwirio ymarferol, ac mae **[UK Government Digital Service](https://en.wikipedia.org/wiki/Government_Digital_Service) (GDS)** yn paru ei Safon Gwasanaeth a'i Cod Ymarfer Technoleg â chanllawiau gweithredadwy'r Llawlyfr Gwasanaeth. Y rhestr wirio yw'r safon wedi'i gwneud yn ddefnyddiadwy: "A ydych wedi ychwanegu archwiliad hygyrchedd? A ydych wedi profi gyda darllenydd sgrin? A ydych wedi cwmpasu llywio bysellfwrdd-yn-unig?" Gweler pennod 12.2 am y patrwm rhestr wirio yn llawn.

### Cyhoeddi safonau lle mae pobl eisoes yn gweithio, a'u cadw'n hygyrch

Storiwch safonau mewn **[rheolaeth fersiynau](https://en.wikipedia.org/wiki/Version_control)** (ystorfa ffynhonnell) fel Markdown, wedi'u rendro i safle mewnol y gellir chwilio ynddo, fel eu bod yn cael hanes, adolygiad trwy geisiadau tynnu, a diffs am ddim, yr un ddadl ag ar gyfer cofnodion penderfyniad (pennod 1.6). Un catalog, un templed, un blwch chwilio. Mae dod i'r amlwg yr un mor bwysig â storio. Cysylltwch y safon berthnasol o'r templed cais tynnu, neges gwall y linter, a sgaffaldiau'r gwasanaeth, fel bod y rheol gywir yn ymddangos ar foment y gwaith yn hytrach nag mewn ffolder na fydd neb yn ymweld ag ef.

### Gorfodi trwy awtomeiddio yn gyntaf, adolygiad dynol yn ail

Mae dwy ffordd o orfodi safon, ac mae sefydliadau aeddfed yn defnyddio'r ddwy'n fwriadol:

- **Gorfodaeth awtomataidd:** [llinteriaid](https://en.wikipedia.org/wiki/Lint_(software)), fformatwyr, [dadansoddiad statig](https://en.wikipedia.org/wiki/Static_program_analysis), polisi-fel-cod (er enghraifft, **Open Policy Agent (OPA)**), giatiau **[integreiddio parhaus](https://en.wikipedia.org/wiki/Continuous_integration) (CI)**, a **swyddogaethau ffitrwydd pensaernïaeth** (profion awtomataidd sy'n honni bod priodwedd dylunio'n dal i fod yn wir). Mae awtomeiddio'n gyson, diflino, ar unwaith, ac anwadadwy, sy'n ei wneud yn ddelfrydol ar gyfer mwyafrif mecanyddol y safonau (fformatio, enwi, rheolau dibyniaeth, metadata gofynnol).
- **Adolygiad dynol:** adolygiad cod, byrddau adolygu pensaernïaeth, ac adolygiad diogelwch, wedi'u cadw ar gyfer yr hyn na all peiriannau ei farnu: a yw haniaeth yn gadarn, a yw cyfaddawd yn ddoeth, a yw *bwriad* safon yn cael ei fodloni hyd yn oed pan fo'i lythyren yn lletchwith.

Y rheol bawd: **awtomeiddiwch yr hyn y gellir ei wirio, a threuliwch sylw dynol prin ar farn.** Mae pob safon y gallwch ei symud o adolygiad i CI yn rhyddhau adolygwyr i wneud y meddwl na all ond hwy ei wneud.

### Llywodraethu gwyriadau â phroses eithriadau/hepgor wedi'i dogfennu

Nid oes unrhyw safon yn ffitio pob achos, felly dyluniwch y ddihangfa'n fwriadol. Mae proses eithriadau dda yn nodi:

- **Pwy all ganiatáu hepgoriad:** awdurdod wedi'i enwi, atebol, cymesur â'r risg (arweinydd technegol ar gyfer gwyriad arddull risg-isel; bwrdd pensaernïaeth neu ddiogelwch ar gyfer hepgoriad rheolaeth-ddiogelwch). Mae hyn yn cysylltu'n uniongyrchol â model llywodraethu pennod 1.5.
- **Beth y mae'n rhaid ei gofnodi:** y safon y gwyrir oddi wrthi, y rheswm penodol, y cwmpas, y rheolaethau iawnderol neu'r camau lliniaru, a'r risg a dderbyniwyd. Cofnodwch hyn fel cofnod penderfyniad (pennod 1.6) fel bod y rhesymeg wedi'i chadw.
- **Dod i ben gorfodol:** mae pob hepgoriad **wedi'i amser-focsio** gyda dyddiad gorffen penodol. Dyma'r rheol bwysicaf oll: mae'n atal eithriad dros dro rhag dod yn bolisi parhaol yn ddistaw.
- **Adolygiad cyfnodol:** mae perchennog yn adolygu hepgoriadau agored ar gyfradd reolaidd ac naill ai'n eu hadnewyddu gyda chyfiawnhad newydd, yn eu cau pan fo'r gwaith yn cydymffurfio, neu, os yw'r un eithriad yn parhau i ailddigwydd, yn trin hynny fel tystiolaeth bod y *safon ei hun* yn anghywir ac yn ei diwygio.

Y pwynt olaf hwn yw calon "mae'r eithriad yn profi'r rheol." Nid methiant disgyblaeth yw llif cyson o hepgoriadau yn erbyn un safon. Data ydyw. Mae'n dweud wrthych fod y safon wedi'i chamraddnodi, a'r ateb yw datblygu'r safon, nid parhau i ganiatáu eithriadau.

### Trin safonau fel dogfennau byw gyda pherchnogaeth glir

Rhowch **berchennog** i bob safon (rôl, nid person yn unig) sy'n atebol am ei chadw'n gyfredol, a **chyfradd adolygu** (o leiaf yn flynyddol). Darparwch lwybr ysgafn i unrhyw un gynnig newid trwy gais tynnu neu **[RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (cais am sylwadau)**, cynnig ysgrifenedig a gylchredir am adborth cyn ei fabwysiadu. Fersiynwch safonau, dad-argymhellwch hwy'n benodol, a chyhoeddwch newidiadau. Mae catalog safonau na ddiwygir byth yn pydru'n lên gwerin y mae pobl yn ei ddyfynnu'n ddetholus ac yn ymddiried ynddo ychydig.

## Cyfaddawdau: manteision ac anfanteision

| Dewis | Manteision | Anfanteision |
|---|---|---|
| **Llawer o safonau manwl** | Cysondeb, sefydlu hawdd, parod-ar-gyfer-archwiliad | Anhyblygrwydd; baich cynnal a chadw; gall ragori ar arfer |
| **Ychydig o safonau lefel-uchel** | Hyblyg; cynnal isel | Anghysondeb; mwy o ailddadlau fesul tîm |
| **Gorfodaeth awtomataidd** | Cyson, ar unwaith, diflino, graddadwy | Cost ymlaen llaw; canlyniadau ffug-gadarnhaol; dall i fwriad |
| **Gorfodaeth adolygiad dynol** | Yn barnu bwriad a chynildeb | Araf, anghyson, tagfa ar raddfa |
| **Llym, dim eithriadau** | Neges syml; dim byd i'w gemio | Yn blocio gwaith dilys; yn gyrru anghydymffurfiad distaw |
| **Proses eithriadau lywodraethol** | Yn cadw safonau'n gredadwy ac yn ddyngar | Angen llywodraethu, cofnodion, a dilyniant |

Y tyndra canolog yw **cysondeb yn erbyn hyblygrwydd**. Mae safon yn bodoli i ddileu amrywiad; mae proses eithriadau'n bodoli i dderbyn yr amrywiad sy'n wirioneddol gyfiawn. Gogwyddwch ormod tuag at anhyblygrwydd a bydd pobl yn osgoi eich safonau. Gogwyddwch ormod tuag at lacrwydd a bydd y safonau'n golygu dim. Y broses eithriadau yw'r falf pwysau sy'n gadael i chi ddal llinell gadarn *a* aros yn onest am realiti.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Sawl safon yw'r nifer cywir ar gyfer eich graddfa, ac a yw eich rhai chi'n drifftio tuag at anhyblygrwydd neu tuag at anghysondeb?** Mae'r catalog ei hun yn gyfaddawd: mae llawer o safonau manwl yn prynu cysondeb, sefydlu hawdd, a pharodrwydd-archwilio ar draul anhyblygrwydd a baich cynnal a chadw, tra bo ychydig o safonau lefel-uchel yn aros yn hyblyg ond yn gadael i bob tîm ailddadlau'r un cwestiynau. I fenter fawr neu gorff llywodraeth, mae'r maint cywir yn dibynnu ar faint o amrywiad y gallwch ei oddef mewn gwirionedd o'i gymharu â faint sydd angen ei bennu i'ch archwilwyr a'ch sefydlu. Dewch â thystiolaeth: sawl safon weithredol sydd gennych, sawl un a adolygwyd y llynedd, a pha mor aml y mae timau'n ailddadlau pethau y gallai safon fod wedi'u setlo. Mae catalog sy'n rhagori ar arfer yn dod yn lên gwerin, ac mae un rhy denau'n gwthio cost ar bob tîm. Penderfynwch yn fwriadol beth sy'n haeddu safon, a thoriwch y rhai nad ydynt bellach yn ennill eu cadw.

2. **Ble mae llythyren safon yn pasio'n awtomatig tra bo'i bwriad yn cael ei dorri'n ddistaw, a sut y byddwch yn dal hynny?** Mae awtomeiddio'n gyson, yn ddiflino, ac yn ddall i fwriad, sy'n golygu y gall gwiriad linter neu bolisi droi'n wyrdd tra bo'r nod gwirioneddol (haniaeth gadarn, cyfaddawd doeth, tudalen wirioneddol hygyrch) yn cael ei golli. Y rheol bawd yw awtomeiddio'r hyn y gellir ei wirio a threulio adolygiad dynol prin ar farn, a'r rhan anodd yw cytuno pa safonau sydd â bwriad na all unrhyw giât CI ei honni. Dewch ag enghreifftiau: safonau y mae pobl yn eu bodloni i'r llythyren tra'n trechu'r pwrpas, megis pwynt terfyn gwiriad-iechyd sy'n adrodd yn iach tra bo'r gwasanaeth wedi torri, neu god sy'n pasio'r fformatiwr ond yn cuddio ystyr. Mewn lleoliadau rheoledig, mae bwriad yn bwysicaf ar gyfer rheolaethau diogelwch a diogelwch, lle gall blwch ticio gwyrdd guddio risg go iawn. Penderfynwch pa safonau sy'n cadw adolygydd dynol yn benodol i farnu bwriad, a geiriwch y safonau hynny o amgylch y canlyniad fel bod y peiriant a'r adolygydd fel ei gilydd yn anelu at yr un targed.

3. **Pwy sy'n berchen ar y ddolen adborth hepgoriad-i-safon, ac ar ba bwynt y mae eithriad sy'n ailddigwydd yn eich gorfodi i newid y rheol?** Mae llif cyson o hepgoriadau yn erbyn un safon yn ddata, nid yn ddiffyg disgyblaeth, ac mae'r signal yn mynd yn wastraff oni bai bod rhywun yn atebol am ei ddarllen a gweithredu arno. Yr ystyriaeth gystadleuol yw bod diwygio safon yn waith go iawn, felly mae'n aros yn haws parhau i stampio hepgoriadau'n rwber na thrwsio'r rheol gamraddnodedig oddi tanynt. Dewch â'r ffigurau: pa safonau sy'n cynhyrchu'r mwyaf o eithriadau, a yw hepgoriadau mewn gwirionedd wedi'u hamser-focsio a'u hadolygu ar gyfradd reolaidd, a sawl un a ddaeth yn ddistaw yn barhaol. Ar gyfer safonau critigol-ddiogelwch a chritigol-ddiogelwch mewn menter a llywodraeth, rhaid i hepgoriad gofnodi rheolaethau iawnderol, cam lliniaru, y risg a dderbyniwyd, a therfyn amser caled, neu bydd gwyriad dros dro'n dod yn bolisi heb ei ddogfennu sy'n dod i'r amlwg yn yr archwiliad nesaf. Penodwch berchennog i adolygu hepgoriadau agored, gosodwch drothwy lle mae eithriadau ailadroddus yn sbarduno diwygiad safonau, a thriniwch eithriad parhaol fel diffyg yn y safon i'w drwsio.

4. **A yw'r safon gywir yn ymddangos ar foment y gwaith, neu a yw'n byw mewn ffolder na fydd neb yn ei agor?** Caiff safon na all neb ddod o hyd iddi ei gorfodi trwy lwc, ac ar raddfa nid herfeiddiad yw'r rhan fwyaf o anghydymffurfiad ond anwybodaeth: ni wyddai peiriannydd erioed fod y rheol yn bodoli neu ni allai ddod o hyd iddi pan oedd yn bwysig. Yr ystyriaeth gystadleuol yw ymdrech, gan fod dod â safon i'r amlwg yn y templed cais tynnu, neges gwall y linter, a sgaffaldiau'r gwasanaeth yn costio gwaith integreiddio go iawn nad yw un safle canolog yn ei wneud. Dewch â thystiolaeth am hygyrchedd-darganfod: sut y mae peirianwyr mewn gwirionedd yn dod o hyd i safonau heddiw, a all cyflogai newydd ddod o hyd i'r rheol hygyrchedd neu ddiogelwch sy'n llywodraethu ei dasg mewn llai na munud, a pha mor aml y mae adolygwyr yn dyfynnu safon na welodd yr awdur yn syml. I fenter fawr neu gorff llywodraeth, mae archwilwyr fwyfwy yn gofyn nid yn unig a yw safon yn bodoli ond a gafodd ei chyfleu a'i bod yn hygyrch adeg y penderfyniad, felly triniwch ddod-i'r-amlwg fel rhan o'r safon, nid fel ôl-ystyriaeth, a mesurwch a all pobl gyrraedd y rheol pan fo'i hangen arnynt.

5. **Pwy sy'n berchen ar bob safon weithredol, pryd yr adolygwyd hi ddiwethaf, a sut y byddech yn adnabod y rhai sydd wedi pydru'n ddistaw yn lên gwerin?** Mae safonau'n dadfeilio'n ddistaw: mae rheol a ysgrifennwyd dair blynedd yn ôl ar gyfer fframwaith nad ydych bellach yn ei ddefnyddio yn dal i eistedd yn y catalog, wedi'i ddyfynnu'n ddetholus ac wedi'i ymddiried ynddo ychydig, gan lusgo credadwyedd y safonau sy'n dal yn gywir. I sefydliad mawr, cost perchnogaeth yw'r gyfradd adolygu ei hun, sy'n teimlo fel gorbenion nes bod toriad neu archwiliad yn dinoethi safon nad yw bellach yn cyfateb i realiti. Dewch â'r ffigurau i'r drafodaeth: sawl safon sydd â pherchennog wedi'i enwi (rôl, nid unigolyn a adawodd yn unig), sawl un a adolygwyd y llynedd, sawl un sydd wedi'i dad-argymell yn ffurfiol o'i gymharu â bod ond yn hen, a pha rai a ddyfynnir fwyaf a lleiaf. Mewn lleoliadau menter a llywodraeth, mae archwiliwr yn disgwyl i bob safon fod wedi'i fersiynu, ei dyddio, ac yn amlwg gyfredol, felly cytunwch ar gyfradd adolygu leiaf, penodwch berchennog atebol i bob safon, ac ymddeolwch y rhai nad ydynt bellach yn ennill eu cadw cyn iddynt danseilio ymddiriedaeth yn y gweddill.

6. **A yw'r awdurdod i ganiatáu hepgoriad mewn gwirionedd yn gymesur â risg y safon a hepgorir?** Nid yr un penderfyniad yw gwyriad arddull a gwyriad rheolaeth-ddiogelwch, ac eto mae llawer o sefydliadau naill ai'n cyfeirio'r ddau at fwrdd trwm (sy'n dod â gwaith dilys i stop llwyr) neu'n gadael i'r ddau lithro trwy un arweinydd technegol (sy'n gadael i risg ddifrifol gael ei derbyn gan rywun heb y mandad i'w derbyn). Y tyndra yw cyflymder yn erbyn atebolrwydd: mae gormod o ffrithiant cymeradwyo'n gyrru anghydymffurfiad distaw, tra bo rhy ychydig yn golygu bod gwyriadau canlyniadol yn cael eu chwifio trwodd mewn edefyn sgwrsio. Dewch â map o'ch safonau i'w hawdurdodau cymeradwyo, ynghyd â sampl o hepgoriadau a ganiatawyd yn ddiweddar, a gwiriwch a wnaeth unrhyw un hepgor rheolaeth critigol-ddiogelwch neu gritigol-ddiogelwch heb y bwrdd cyfatebol, rheolaeth iawnderol, camau lliniaru, a derbyniad risg wedi'i gofnodi. I fenter a llywodraeth, mae hwn yn gwestiwn gwahanu-dyletswyddau y mae rheoleiddwyr yn ei graffu'n uniongyrchol, felly cydiwch bob dosbarth o safon wrth awdurdod wedi'i enwi sy'n gymesur â'i risg, a sicrhewch fod y person sy'n derbyn risg mewn gwirionedd yn atebol am y canlyniadau.

## Lens sector

**Cwmni newydd.** Cadwch y catalog yn fach iawn: ysgrifennwch i lawr ddim ond y llond llaw o reolau y byddai eu habsenoldeb yn eich brifo mewn gwirionedd, megis ffurfweddiad fformatiwr, gofyniad gwiriad-iechyd, a thudalennau llywiadwy-bysellfwrdd, a gorfodwch bob un â gwiriad linter neu CI yn hytrach na chyfarfod adolygu. Hepgorwch y bwrdd hepgoriadau'n gyfan gwbl; mae TODO wedi'i ddyddio yn y cod a nodyn un-llinell yn y cais tynnu yn eithriad amser-focsiedig perffaith dda ar y raddfa hon. Eich adnodd prinnaf yw sylw peirianyddol, felly gwrthwynebwch awduro safonau ar gyfer problemau nad oes gennych eto.

**Busnes bach.** Heb berchennog safonau pwrpasol a chyllideb dynn, prynwch eich safonau yn hytrach na'u hadeiladu: mabwysiadwch linellau sylfaen cyhoeddedig megis Safon Gwasanaeth UK GDS, canllawiau diogelwch OWASP, neu reolau lint a argymhellir gan eich fframwaith, a phwyswch ar y gwiriadau sydd eisoes wedi'u hadeiladu i mewn i'ch offer a CI a gynhelir. Cadwch un dudalen fer o reolau lleol ar gyfer y pethau prin sy'n wirioneddol benodol i chi. Mae pwy bynnag sy'n arwain peirianneg yn caniatáu ac yn cofnodi eithriadau yn y tocyn, gyda dyddiad dod i ben, fel bod hyd yn oed proses ysgafn yn aros yn onest.

**Menter.** Y gwaith yw llywodraethu ar draws llawer o dimau: un catalog, un templed, rhesymeg ac enghreifftiau ar gyfer pob safon, a pholisi-fel-cod sy'n methu'r biblinell ar gyfer y mwyafrif mecanyddol. Rhedwch broses hepgor y mae ei hawdurdod cymeradwyo'n gymesur â risg, amser-focsiwch bob eithriad, adolygwch hepgoriadau agored ar gyfradd reolaidd, a chloddiwch hepgoriadau ailadroddus fel y signal bod angen i safon newid. Mesurwch gyfran y safonau a orfodir yn awtomatig a chyfaint ac oedran hepgoriadau agored, ac adroddwch y ddau i'r swyddogaeth lywodraethu fel bod safonau'n aros yn system a reolir yn hytrach na mynwent.

**Llywodraeth.** Cyhoeddwch eich safonau peirianneg yn agored yn nhraddodiad DHCW a GDS, a pharwch bob un â rhestr wirio y mae timau'n ei chwblhau cyn asesiad gwasanaeth, fel bod cydymffurfiaeth yn weladwy i'r cyhoedd ac i gyrff goruchwylio. Gwnewch berchennog uwch cyfrifol wedi'i enwi yn awdurdod ar gyfer hepgoriadau canlyniadol, a mynnwch fod pob eithriad yn cofnodi'r maen prawf penodol, y rheolaeth iawnderol neu'r camau lliniaru dros dro, cynllun unioni, a therfyn amser caled. Mae rheolau caffael a thryloywder yn golygu bod eich safonau a'ch gwyriadau fel ei gilydd yn dod yn rhan o'r cofnod cyhoeddus, felly triniwch archwiliadwyedd ac olrheiniadwyedd fel gofynion dylunio o'r dechrau.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd saith-person yn cadw union dair safon ysgrifenedig (ffurfweddiad fformatiwr a rennir, gofyniad pwynt terfyn gwiriad-iechyd, a "rhaid i bob tudalen gyhoeddus fod yn llywiadwy-bysellfwrdd"), pob un wedi'i gorfodi gan wiriad linter neu CI yn hytrach na chyfarfod adolygu. Pan fo angen i un peiriannydd gyflenwi prototeip taflu-i-ffwrdd sy'n torri'r rheol gwiriad-iechyd, does dim bwrdd hepgoriadau: mae'n gadael TODO wedi'i ddyddio yn y cod a nodyn un-llinell yn y cais tynnu yn dweud pam a phryd y bydd yn ei drwsio. Dyna eithriad amser-focsiedig ar raddfa cwmni newydd, yn onest ac yn weladwy heb orbenion proses. Mae'r tri gwiriad yn talu amdanynt eu hunain trwy gadw adolygiad cod yn ymwneud â sylwedd yn hytrach nag arddull.

**Menter.** Mae banc byd-eang yn cynnal llawlyfr peirianneg mewnol o oddeutu deugain o safonau gweithredol, pob un mewn un templed gyda rhesymeg, enghreifftiau, a rhestr wirio arfer da wedi'i chysylltu. Gorfodir tua 70% yn awtomatig: fformatio, polisi dibyniaeth, metadata gwasanaeth gorfodol, a rheolaethau diogelwch wedi'u hamgodio fel polisi-fel-cod sy'n methu'r biblinell CI. Mae angen i dîm taliadau gyflenwi ar gronfa ddata nad yw eto'n cefnogi nodwedd amgryptio orfodol. Yn hytrach na blocio'r rhyddhad, maent yn ffeilio hepgoriad yn enwi'r safon, y rheolaeth iawnderol ([amgryptio](https://en.wikipedia.org/wiki/Encryption) lefel-cymhwysiad), a therfyn amser 90 diwrnod. Mae'r bwrdd diogelwch yn ei ganiatáu ac yn ei gofnodi. Naw deg diwrnod yn ddiweddarach, mae'r adolygiad yn canfod bod y llwyfan bellach yn cefnogi'r nodwedd yn frodorol, a chaiff yr hepgoriad ei gau. Daliodd y safon, cyflenwyd y gwaith, ac mae'r gwyriad yn hollol olrheiniadwy ar gyfer yr archwiliad nesaf.

**Llywodraeth.** Mae asiantaeth iechyd genedlaethol wedi'i modelu ar ddull DHCW a GDS yn cyhoeddi ei safonau peirianneg yn agored, pob un wedi'i pharu â rhestr wirio y mae timau'n ei chwblhau cyn asesiad gwasanaeth. Mae hygyrchedd i WCAG 2.2 AA yn safon galed, wedi'i gorfodi gan archwiliad awtomataidd yn CI ynghyd ag asesiad llawlyfr. Ni all system glinigol etifeddol fodloni un maen prawf hygyrchedd ar unwaith heb beryglu ymarferoldeb critigol-i-ddiogelwch-cleifion. Mae'r tîm yn gofyn am eithriad amser-focsiedig. Mae perchennog uwch cyfrifol wedi'i enwi yn ei ganiatáu, ac yn cofnodi'r maen prawf penodol, y cam lliniaru dros dro (llinell ffôn mynediad-cynorthwyedig), y cynllun unioni, a therfyn amser chwe mis, gan greu'n union y dystiolaeth olrheiniadwy, adolygadwy y mae cyrff goruchwylio'n ei mynnu (penodau 4.6, 10.4).

## Achos busnes: cymhellion, ROI, a TCO

Mae safon yn costio'r amser i'w hysgrifennu, awtomeiddio ei gwiriad, a'i chynnal. Telir yr elw bob tro y mae'r gwiriad yn rhedeg, a bob tro nad oes rhaid i beiriannydd stopio a dadlau cwestiwn wedi'i setlo. Mae safonau'n trosi cost penderfyniad ailadroddus, wedi'i ddosbarthu yn gost awduro un-tro, yr un economeg â chofnodion penderfyniad (pennod 1.6), wedi'i chwyddo gan fod safon yn llywodraethu miloedd o achosion yn y dyfodol, nid un dewis yn y gorffennol.

O ran **cyfanswm cost perchnogaeth (TCO)**, cost oes lawn adeiladu, rhedeg, a chynnal system, mae safonau'n gostwng yr eitemau llinell mwyaf: sefydlu (mae cyflogeion newydd yn etifeddu cysondeb yn hytrach na'i beirianyddu'n wrthol), cynnal a chadw (mae cod unffurf yn rhatach i'w newid), a sicrwydd (mae archwiliadau'n rhatach pan fo cydymffurfiaeth yn wiriadwy-gan-beiriant a'r gwyriadau eisoes wedi'u dogfennu). Mae'r broses eithriadau'n amddiffyn yr ROI hwnnw rhag ei brif fygythiad: safonau'n dadfeilio'n lên gwerin a anwybyddir. Mae proses hepgor gredadwy'n cadw'r safonau'n ymddiriedol, a'r safonau ymddiriedol yw'r rhai y mae pobl mewn gwirionedd yn eu dilyn. Mae cost hepgor hyn i gyd yn anweladwy ar unrhyw ddangosfwrdd. Mae'n ymddangos fel sefydlu araf, ansawdd anghyson, a chanfyddiadau archwilio, ac mae'n cyfansymio gyda phob tîm newydd a phob ymadawiad.

## Gwrth-batrymau a pheryglon

- **Rheolau heb resymeg:** mae safon na fydd neb yn ei deall yn safon na all neb ei chymhwyso'n gywir na'i herio'n onest.
- **Safonau dyheadol, na ellir eu gwirio:** mae "dylai cod fod yn gynaliadwy" yn werth, nid yn safon; ni ellir ei gorfodi na'i herio.
- **Dim proses eithriadau:** yn gorfodi dewis ffug rhwng blocio gwaith dilys a goddef anghydymffurfiad distaw.
- **Eithriadau parhaol:** hepgoriadau heb derfyn amser sy'n ddistaw ddod yn bolisi go iawn, heb ei ddogfennu.
- **Hepgoriadau heb gofnodion:** gwyriadau a ganiateir mewn coridor neu edefyn sgwrsio, yn anweladwy i'r archwiliad nesaf a'r peiriannydd nesaf.
- **Anwybyddu'r signal:** caniatáu'r un eithriad dro ar ôl tro yn hytrach na'i ddarllen fel prawf bod angen i'r safon newid.
- **Gorfodaeth-trwy-nagio:** dibynnu ar adolygwyr i ddal yr hyn y dylai linter ei ddal, gan wastraffu barn ar y mecanyddol.
- **Mynwent safonau:** catalog a ysgrifennwyd unwaith, heb ei berchen gan neb, na adolygwyd erioed, wedi'i ddyfynnu'n ddetholus, wedi'i ymddiried gan ychydig.
- **Ceidwadaeth jargon:** safonau wedi'u hysgrifennu ar gyfer eu hawduron yn hytrach na'u darllenwyr, heb enghreifftiau i'w copïo.

## Model aeddfedrwydd

- **Lefel 1 (Cychwyn):** Mae safonau'n wybodaeth lwythol ym mhennau peirianwyr hŷn, wedi'u cymhwyso'n adweithiol. Mae gorfodaeth yn nagio adolygiad-cod digyswllt; mae gwyriadau'n anweladwy; mae "sut yr ydym yn ei wneud" yn amrywio yn ôl tîm a phwy a adolygodd y newid.
- **Lefel 2 (Datblygu):** Mae rhai safonau wedi'u hysgrifennu i lawr, mewn fformatau anghyson a lleoliadau gwasgaredig, ac mae mabwysiadu'n amrywio'n eang o dîm i dîm. Mae gorfodaeth yn bennaf yn llawlyfr. Mae eithriadau'n digwydd yn anffurfiol, heb gofnodion na dyddiadau dod i ben.
- **Lefel 3 (Safoni):** Un catalog, un templed, rhesymeg ac enghreifftiau ar gyfer pob safon, a rhestrau gwirio arfer da, wedi'u cymhwyso'n gyson ar draws timau. Gorfodaeth awtomataidd ar gyfer y mwyafrif mecanyddol. Proses eithriadau wedi'i dogfennu gyda chymeradwywyr wedi'u henwi, rhesymeg wedi'i chofnodi, a hepgoriadau wedi'u hamser-focsio.
- **Lefel 4 (Rheoli):** Mesurir system y safonau yn erbyn llinellau sylfaen. Rydych yn olrhain cyfran y safonau a orfodir yn awtomatig o'i chymharu ag adolygiad dynol, cyfaint hepgoriadau fesul safon, amser-i-gau, a sawl hepgoriad a ddaeth i ben tra'n dal yn agored, ac rydych yn adrodd y rhain i'r swyddogaeth lywodraethu. Mae awdurdod cymeradwyo'n gymesur â risg ac wedi'i archwilio; gorfodir cyfradd adolygu a therfyn amser ar sail tystiolaeth yn hytrach na hyfrydwch; caiff safon y mae ei chyfradd hepgor yn croesi trothwy cytunedig ei fflagio ar gyfer diwygiad.
- **Lefel 5 (Cyfundrefnu):** Daw safonau i'r amlwg ar foment y gwaith ac fe'u gorfodir gan bolisi-fel-cod a swyddogaethau ffitrwydd. Cloddir hepgoriadau fel signal fel bod eithriadau ailadroddus yn gyrru safonau i ddatblygu'n barhaus, ac ailgydbwyir y catalog wrth i arfer symud. Mae safonau, rhestrau gwirio, a hepgoriadau'n un system fyw addasol wedi'i hintegreiddio ar draws sefydlu, cyflenwi, ac archwilio.

## Syniadau ar gyfer trafodaeth

1. Pa rai o'ch safonau y gallwch eu nodi gyda rheol y gellir ei phrofi *a* rhesymeg glir, a pha rai sydd mewn gwirionedd yn ddyheadau yn unig?
2. Pa gyfran o'ch safonau a orfodir yn awtomatig o'i chymharu ag adolygydd yn sylwi? Beth fyddai ei angen i symud deg yn rhagor i mewn i CI?
3. Ble mae gwyriadau'n digwydd heddiw, ac a fyddech chi hyd yn oed yn gwybod? A ydynt wedi'u cofnodi a'u hamser-focsio, neu'n ddistaw?
4. Pwy sy'n cael caniatáu hepgoriad yn erbyn eich safon fwyaf critigol-ddiogelwch neu gritigol-ddiogelwch, ac a yw'r awdurdod hwnnw'n gymesur â'r risg?
5. Edrychwch ar eich safon a hepgorwyd fwyaf. A yw'n broblem ddisgyblaeth, neu a yw'r safon yn syml yn anghywir?
6. Pryd yr adolygwyd pob safon weithredol ddiwethaf, a phwy sy'n berchen arni? Pa rai sydd wedi dod yn ddistaw yn lên gwerin?

## Casgliadau allweddol

- Mae safon beirianneg yn **rheol wedi'i nodi fel canlyniad, gyda rhesymeg, enghreifftiau, a ffordd o'i gwirio**: os na ellir ei gwirio, nid yw'n safon eto.
- Parwch bob safon â **rhestr wirio arfer da** fel y gall pobl hunanwirio, gan ddilyn patrwm llawlyfr y sector cyhoeddus (NHS Cymru / DHCW, UK GDS).
- Storiwch safonau mewn **rheolaeth fersiynau**, cadwch hwy'n **fyw** gyda pherchnogion wedi'u henwi a dyddiadau adolygu, a dewch â hwy i'r amlwg ar foment y gwaith.
- **Awtomeiddiwch yr hyn y gellir ei wirio** gyda llinteriaid, polisi-fel-cod, a swyddogaethau ffitrwydd; cadwch **adolygiad dynol** ar gyfer barn.
- Llywodraethwch wyriadau â **phroses eithriadau/hepgor wedi'i dogfennu, wedi'i hamser-focsio**: cymeradwywr wedi'i enwi, rhesymeg wedi'i chofnodi, dod i ben gorfodol, adolygiad cyfnodol.
- Mae eithriad sy'n ailddigwydd yn **signal i drwsio'r safon**, nid ond i barhau i ganiatáu hepgoriadau: "mae'r eithriad yn profi'r rheol." Gweler penodau 1.5 (llywodraethu), 1.6 (cofnodion penderfyniad), 2.1 (safonau codio), 12.2 (rhestrau gwirio), a 12.3 (templedi).

## Cyfeiriadau a darllen pellach

- UK Government Digital Service, *Government Service Standard*, *Technology Code of Practice*, and *GOV.UK Service Manual*.
- NHS Digital / NHS England, *Service Standard* and engineering guidance.
- Digital Health and Care Wales (DHCW) / NHS Wales, published engineering standards and good-practice checklists.
- Scott Bradner, *RFC 2119: Key Words for Use in RFCs to Indicate Requirement Levels* (IETF, 1997).
- World Wide Web Consortium (W3C), *Web Content Accessibility Guidelines (WCAG) 2.2*.
- Neal Ford, Rebecca Parsons, and Patrick Kua, *Building Evolutionary Architectures* (fitness functions as automated governance).
- Torin Sandall et al., *Open Policy Agent* documentation (policy-as-code).
- GitLab, *The GitLab Handbook*: a public example of living, version-controlled organizational standards.
- Google, *Software Engineering at Google* (Winters, Manshreck, Wright): standards, readability, and automated enforcement at scale.
- Atul Gawande, *The Checklist Manifesto*: the case for checklists as professional practice.
