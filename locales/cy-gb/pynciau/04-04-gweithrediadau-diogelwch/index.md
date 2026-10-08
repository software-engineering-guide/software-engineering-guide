# 4.4 Gweithrediadau diogelwch

## Trosolwg a chymhelliant

Mae atal yn angenrheidiol, ond nid yw byth yn ddigon. Mae gwrthwynebwyr penderfynol, gwendidau newydd, a chamgymeriad dynol plaen yn golygu y bydd rhai bygythiadau'n llithro heibio'ch amddiffynfeydd. Gweithrediadau diogelwch yw'r ddisgyblaeth o'u canfod yn gyflym, ymateb yn dda, a bwydo'r hyn a ddysgwch yn ôl i mewn i amddiffynfeydd cryfach. Dyma'r gwahaniaeth rhwng digwyddiad a gynhwysir mewn munudau ac un sy'n crawni am fisoedd cyn i unrhyw un sylwi.

Mewn sefydliad mawr, mae'n rhaid i weithrediadau diogelwch weithio ar raddfa a chyflymder. Mae miloedd o wasanaethau'n cynhyrchu moroedd o logiau. Datgelir cannoedd o wendidau newydd bob wythnos. Nid yw defnyddio byth yn stopio. Ni all gweithrediadau â llaw, crefftus ymdopi o gwbl. Yr ateb yw plannu diogelwch i mewn i'r biblinell gyflenwi ([DevSecOps](https://en.wikipedia.org/wiki/DevSecOps)), awtomeiddio canfod ac ymateb, ac adeiladu'r cyhyr i drin digwyddiadau'n bwyllog pan fyddant yn digwydd. I lywodraeth, mae gweithrediadau diogelwch hefyd yn cario rhwymedigaethau statudol: terfynau amser adrodd digwyddiadau gorfodol, datgeliad gwendidau cydgysylltiedig, a thrylwyredd fforensig a all wrthsefyll gwyliadwriaeth gyfreithiol.

Mae'r bennod hon yn ymdrin â phlannu diogelwch i mewn i'r biblinell, rheoli gwendidau a phatsio, ymateb i ddigwyddiadau a chynnal fforensig, rhedeg canfod drwy [SIEM](https://en.wikipedia.org/wiki/Security_information_and_event_management) a SOAR, a dilysu amddiffynfeydd drwy dimoedd coch a phorffor a [phrofi treiddiad](https://en.wikipedia.org/wiki/Penetration_test).

## Egwyddorion allweddol

- **Awtomeiddiwch y drefn arferol.** Mae peiriannau'n trin sganio, cydberthyn, ac ymateb ailadroddus fel bod bodau dynol yn canolbwyntio ar farn.
- **Symudwch ddiogelwch i mewn i'r biblinell.** Mae profi a giatiau'n byw yn [CI/CD](https://en.wikipedia.org/wiki/CI/CD) (integreiddio parhaus a chyflenwi parhaus), gan roi adborth cyflym lle mae peirianwyr eisoes yn gweithio.
- **Tybiwch dor a pharatowch.** Ymarferwch ymateb i ddigwyddiadau cyn bod eu hangen arnoch; nid y digwyddiad yw'r amser i fyrfyfyrio.
- **Mesurwch a lleihau amser.** Y cyfartaledd amser i ganfod a'r cyfartaledd amser i ymateb yw'r metrigau sy'n bwysicaf.
- **Dysgu di-fai.** Mae pob digwyddiad ac agos-fethiant yn dod yn wers sy'n caledu'r system, nid yn chwiliad am rywun i'w gosbi.
- **Dilyswch amddiffynfeydd yn wrthwynebus.** Profwch eich diogelwch fel y byddai ymosodwyr gwirioneddol yn ei wneud, yna trwsiwch yr hyn y maent yn ei ganfod.
- **Cynnyrch yw peirianneg canfod.** Triniwch reolau canfod fel cod: wedi'i reoli gan fersiwn, wedi'i brofi, ac yn cael ei wella'n barhaus.

## Argymhellion

### Adeiladwch DevSecOps i mewn i'r biblinell

Integreiddiwch brofi diogelwch awtomataidd yn uniongyrchol i mewn i integreiddio a chyflenwi parhaus fel bod adborth yn cyrraedd peirianwyr o fewn munudau:

- Mae **[SAST](https://en.wikipedia.org/wiki/Static_application_security_testing)** (Profi Diogelwch Cymhwysiad Statig) yn dadansoddi cod ffynhonnell am batrymau bregus wrth iddo gael ei gyflwyno.
- Mae **[DAST](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)** (Profi Diogelwch Cymhwysiad Dynamig) yn profi'r cymhwysiad sy'n rhedeg am ddiffygion y gellir eu hecsbloetio.
- Mae **SCA** (Dadansoddiad Cyfansoddiad Meddalwedd) yn baneru dibyniaethau y gwyddys eu bod yn fregus.
- Mae **sganio IaC** yn gwirio seilwaith-fel-cod am ffurfweddiadau anniogel cyn iddynt gael eu defnyddio.
- Mae **sganio cyfrinachau** yn rhwystro credlythyrau rhag mynd i mewn i'r ystorfa.

Tiwniwch yr offer hyn yn ddidostur i reoli canlyniadau ffug-gadarnhaol. Anwybyddir sganiwr sy'n gweiddi blaidd. Gosodwch giatiau seiliedig ar risg: rhwystrwch ar ganfyddiadau difrifoldeb uchel, hyder uchel, ac olrheiniwch y gweddill heb atal cyflenwi. Rydych eisiau signal cyflym, dibynadwy, nid wal o sŵn.

### Rheolwch wendidau a phatsio'n systematig

Mae llif cyson o wendidau'n galw am broses systematig, wedi'i blaenoriaethu, nid panig ffres gyda phob penawd.

- Cynhaliwch restr eiddo gywir fel eich bod yn gwybod beth y gallai unrhyw wendid penodol effeithio arno.
- Blaenoriaethwch unioni yn ôl risg wirioneddol: cyfunwch ddifrifoldeb, ecsbloetiadwyedd (a yw'n cael ei ecsbloetio yn y byd go iawn?), amlygiad, a hanfodolrwydd asedau yn hytrach na phatsio yn ôl sgôr crai yn unig.
- Diffiniwch a gorfodwch **SLAau unioni** (cytundebau lefel gwasanaeth) yn ôl haen ddifrifoldeb, a mesurwch gydymffurfiad.
- Awtomeiddiwch batsio lle gallwch yn ddiogel, yn enwedig ar gyfer seilwaith a dibyniaethau.
- Rhedwch raglen **datgeliad gwendidau cydgysylltiedig** gyda sianel gymeriant glir ac, lle bo'n briodol, [wobr nam](https://en.wikipedia.org/wiki/Bug_bounty_program), fel y gall ymchwilwyr allanol adrodd diffygion yn gyfrifol yn hytrach na'u tywallt yn gyhoeddus.

### Paratowch ar gyfer, a rhedwch, ymateb i ddigwyddiadau

Pan fydd digwyddiad yn taro, mae proses wedi'i hymarfer yn werth mwy nag unrhyw declyn.

- Cynhaliwch **gynllun ymateb i ddigwyddiadau** gyda rolau diffiniedig (cadlywydd digwyddiad, arweinydd cyfathrebu, ymchwilwyr), dosbarthiadau difrifoldeb, a llwybrau dwysáu.
- Sefydlwch gamau clir: **paratoi, canfod a dadansoddi, cynnwys, difa, adferiad, ac adolygiad ôl-ddigwyddiad.**
- Cadwch dystiolaeth yn briodol ar gyfer **[fforensig](https://en.wikipedia.org/wiki/Digital_forensics)**: dalgnwch logiau, cof, a delweddau disg gyda chadwyn ddogfennedig o gadwraeth fel bod canfyddiadau'n dal dŵr yn gyfreithiol a bod y dadansoddiad yn gadarn.
- Cynlluniwch **gyfathrebiadau tor diogelwch** ymlaen llaw: pwy sy'n hysbysu cwsmeriaid, rheoleiddwyr, a'r cyhoedd, ar ba amserlen, gyda chyfraniad cyfreithiol a chysylltiadau cyhoeddus. Mae clociau rheoleiddiol (yn aml 72 awr neu lai) yn dechrau tician wrth ddarganfod.
- Rhedwch **ymarferion bwrdd** yn rheolaidd fel bod y tîm yn gwybod y cynllun cyn argyfwng gwirioneddol, a chynhaliwch adolygiadau ôl-ddigwyddiad di-fai sy'n cynhyrchu gwelliannau diriaethol.

### Gweithredwch ganfod gyda SIEM a SOAR, a pheirianna ganfod

Dewch â'ch signalau diogelwch at ei gilydd a gweithredwch arnynt ar raddfa.

- Defnyddiwch **SIEM** (Rheoli Gwybodaeth a Digwyddiadau Diogelwch) i gasglu a chydberthyn logiau a digwyddiadau ar draws yr ystad, gan ddod â phatrymau amheus i'r wyneb.
- Defnyddiwch **SOAR** (Cydgysylltu, Awtomeiddio, ac Ymateb Diogelwch) i awtomeiddio llyfrau chwarae didoli ac ymateb: cyfoethogi rhybuddion, ynysu gwesteiwyr, analluogi credlythyrau, ac agor achosion heb aros am fod dynol ar gyfer camau arferol.
- Ymarferwch **beirianneg canfod**: triniwch reolau canfod fel cod wedi'i reoli gan fersiwn, wedi'i brofi, wedi'i alinio â fframwaith fel [MITRE ATT&CK](https://en.wikipedia.org/wiki/MITRE_ATT%26CK), mesurwch eu cyfraddau gwir-gadarnhaol a ffug-gadarnhaol, a gwellwch gwmpas technegau gwrthwynebwyr gwirioneddol yn barhaus.
- Sicrhewch logio cynhwysfawr, gwrth-ymyrryd ar draws cymwysiadau a seilwaith; ni allwch ganfod yr hyn nad ydych yn ei logio.

### Dilyswch amddiffynfeydd gyda thimoedd coch a phorffor a phrofi treiddiad

Profi eich amddiffynfeydd fel y byddai ymosodwr yn ei wneud yw'r unig ffordd o wybod eu bod yn gweithio mewn gwirionedd.

- Mae **profi treiddiad** yn darparu asesiad canolbwyntiedig, pwynt-mewn-amser o systemau penodol, yn aml ar gyfer cydymffurfiaeth.
- Mae **[tîm coch](https://en.wikipedia.org/wiki/Red_team)** yn efelychu gwrthwynebydd realistig sy'n ymlid amcanion ar draws eich amgylchedd, gan brofi canfod ac ymateb yn ogystal ag atal.
- Mae **tîm porffor** yn dod ag ymosodwyr (coch) ac amddiffynwyr (glas) at ei gilydd yn gydweithredol fel bod pob ymosodiad efelychiedig yn gwella canfodiadau a rheolaethau ar unwaith, gan droi ymarfer yn allu parhaol.
- Bwydwch bob canfyddiad yn ôl i mewn i beirianneg canfod, unioni, a hyfforddiant.

## Cyfaddawdau: manteision ac anfanteision

| Penderfyniad | Manteision | Anfanteision |
|---|---|---|
| Giatiau piblinell rhwystrol | Yn atal materion hysbys rhag cael eu cyflenwi | Ffrithiant, mae ffug-gadarnhaol yn rhwystro timau |
| Sganio anrhwystrol | Ffrithiant isel, cyflenwi cyflym | Gall materion gael eu cyflenwi; angen disgyblaeth i'w trwsio |
| SOC mewnol | Cyd-destun dwfn, rheolaeth lawn | Drud, anodd ei staffio 24/7 |
| Canfod/ymateb a reolir | Sylw 24/7, arbenigedd wrth law | Llai o gyd-destun, dibyniaeth ar werthwr |
| Patsio awtomataidd | Cyflym, yn cau ffenestri'n gyflym | Risg o newidiadau sy'n torri |
| Timio coch aml | Dilysiad realistig, yn dod o hyd i fylchau gwirioneddol | Drud, dwys o ran adnoddau |
| Rhaglen gwobr nam | Darganfyddiad torfol, cwmpas da | Baich didoli, costau taliad, sŵn |

Y tyndra craidd yw cyflymder yn erbyn sicrwydd, a chwmpas yn erbyn cost. Mae giatiau rhwystrol a phatsio awtomataidd yn macsimeiddio sicrwydd ond yn ychwanegu ffrithiant a risg. Mae dulliau anrhwystrol yn symud yn gyflymach ond yn dibynnu ar ddilyn drwodd. Mae canfod rownd-y-cloc yn hanfodol ar raddfa ond eto'n ddrud i'w adeiladu'n fewnol, sy'n gwthio llawer o sefydliadau tuag at fodelau hybrid. Mae'r llwybr cynaliadwy'n awtomeiddio'r drefn hyder uchel, yn cadw sylw dynol ar gyfer barn wirioneddol, ac yn parhau i diwnio'r cydbwysedd gan ddefnyddio canlyniadau mesuredig yn hytrach nag ofn.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Beth yw eich SLAau unioni yn ôl difrifoldeb, a beth sy'n eu gorfodi mewn gwirionedd?** Mae llif cyson o wendidau angen proses systematig, wedi'i blaenoriaethu, nid panig ffres gyda phob penawd, ac mae SLAau yn ôl haen ddifrifoldeb yn sut rydych yn cadw'r cyflymder. Penderfynwch eich clociau (er enghraifft, critigol mewn dyddiau, uchel mewn wythnosau) ac, yr un mor bwysig, sut rydych yn mesur cydymffurfiad a phwy sy'n atebol pan fydd terfyn amser yn llithro. Blaenoriaethwch yn ôl risg wirioneddol, gan gyfuno difrifoldeb ag ecsbloetiadwyedd yn y byd go iawn, amlygiad, a hanfodolrwydd asedau, yn hytrach na phatsio yn ôl sgôr CVSS crai yn unig. Dewch â'ch ôl-groniad cyfredol o ganfyddiadau agored wedi'u trefnu yn ôl oed a difrifoldeb, oherwydd mae materion critigol heb eu patsio y tu hwnt i'w ffenestr yn dystiolaeth sy'n bwysig. Os nad oes gan yr SLA orfodaeth na pherchennog, dymuniad ydyw, ac mae sganio heb unioni'n dim ond adeiladu dyled archwilio ac ymdeimlad ffug o ddiogelwch.

2. **Pan fydd digwyddiad yn taro am 2am, pwy yw'r cadlywydd digwyddiad a pha mor gyflym mae'r cloc rheoleiddiol yn dechrau?** Mae proses wedi'i hymarfer yn werth mwy nag unrhyw declyn, felly mae angen rolau wedi'u henwi (cadlywydd digwyddiad, arweinydd cyfathrebu, ymchwilwyr), lefelau difrifoldeb diffiniedig, a llwybrau dwysáu wedi'u hysgrifennu i lawr cyn yr argyfwng. Mae clociau rheoleiddiol yn aml yn rhedeg 72 awr neu lai ac yn dechrau wrth ddarganfod, felly penderfynwch ymlaen llaw pwy sy'n hysbysu cwsmeriaid, rheoleiddwyr, a'r cyhoedd, a chadarnhewch fod cyfreithiol a chysylltiadau cyhoeddus yn rhan o'r ddolen. Mae'n rhaid i gadw tystiolaeth fforensig gyda chadwyn ddogfennedig o gadwraeth ddigwydd cyn i unrhyw un ailadeiladu gwesteiwr a beryglwyd, neu byddwch yn colli'r gallu i ddeall neu brofi beth ddigwyddodd. Dewch â dyddiad eich ymarfer bwrdd diwethaf, oherwydd os oedd hynny amser maith yn ôl neu byth, mae eich cynllun heb ei brofi. I dimau llywodraeth, mae terfynau amser adrodd statudol yn gwneud hyn yn anorfod, felly ymarferwch y llwybr hysbysu, nid dim ond yr ymateb technegol.

3. **Pa gamau ymateb arferol y byddwch yn caniatáu i SOAR eu cymryd heb fod dynol yn y ddolen?** Mae awtomeiddio'n luosogiad grym sy'n caniatáu i dîm main gwmpasu ystad fawr, a'r metrig sy'n bwysig yw'r cyfartaledd amser i ymateb, y gall llyfrau chwarae awtomataidd ei dorri o oriau i funudau. Penderfynwch pa gamau hyder uchel (ynysu gwesteiwr, dirymu credlythyr, agor achos) rydych yn ymddiried i redeg yn awtomatig, a pha rai angen barn ddynol yn gyntaf. Y risg yw ffug-gadarnhaol yn sbarduno gweithred aflonyddgar, felly cysylltwch awtomeiddio ag ansawdd canfod a thiwniwch yn ddidostur, oherwydd anwybyddir system sy'n gweiddi blaidd. Dewch â'ch cyfaint rhybudd cyfredol a'ch cyfradd ffug-gadarnhaol, oherwydd mae'r rhifau hynny'n dweud wrthych pa lyfrau chwarae sy'n ddiogel i'w hawtomeiddio heddiw. Os yw pob cam ymateb yn aros am fod dynol, ni fyddwch yn cadw i fyny ar raddfa, a bydd amser preswyl, sy'n gyrru cost torion, yn aros yn uchel.

4. **Pa ganfyddiadau piblinell sy'n rhwystro rhyddhad, pa rai sy'n cael eu holrhain yn unig, a phwy sy'n cadw'r gyfradd ffug-gadarnhaol yn ddigon isel fel bod peirianwyr yn dal i ymddiried yn y giât?** Anwybyddir sganiwr sy'n gweiddi blaidd, ac unwaith y bydd peirianwyr yn colli ffydd mewn giât maen nhw'n lobïo i'w symud yn llwyr, felly mae gwerth DevSecOps yn gorffwys ar ansawdd signal yn hytrach na chwmpas crai. Mae'r tyndra'n wirioneddol: rhwystrwch ar ormod o ychydig a bydd cod bregus yn cael ei gyflenwi; rhwystrwch ar ormod a byddwch yn ychwanegu ffrithiant, yn arafu cyflenwi, ac yn llosgi ewyllys da. Dewch â'r cyfraddau gwir-gadarnhaol a ffug-gadarnhaol ar gyfer pob sganiwr (SAST, DAST, SCA, IaC, a sganio cyfrinachau), pa mor aml mae timau'n diystyru neu'n atal giât, ac oedran y canfyddiadau rydych ond yn eu holrhain heb eu trwsio. I fenter neu gorff llywodraeth sy'n rhedeg cannoedd o biblinellau, gosodwch y polisi rhwystro-yn-erbyn-olrhain yn ganolog a'i diwnio â data, oherwydd mae giatiau sy'n gwahaniaethu'n fympwyol o dîm i dîm yn creu bylchau archwilio ac ymdeimlad bod diogelwch yn fympwyol.

5. **Pa mor hyderus ydych chi bod eich canfodiadau'n dal i orchuddio'r technegau y byddai ymosodwr gwirioneddol yn eu defnyddio, a phwy sy'n berchen arnynt fel cod wedi'i brofi, wedi'i reoli gan fersiwn?** Mae canfodiadau'n dirywio'n dawel wrth i'ch amgylchedd a'ch gwrthwynebwyr esblygu, felly gall set reolau a edrychai'n gynhwysfawr y llynedd golli cwmpas ymhell cyn i ddigwyddiad ddatgelu'r bwlch o'r diwedd. Trin canfodiadau fel cod, wedi'i reoli gan fersiwn, wedi'i brofi, ac wedi'i fapio i fframwaith fel MITRE ATT&CK, yw'r hyn sy'n gwahanu arfer peirianneg oddi wrth bentwr o rybuddion hen, ac eto mae'n cystadlu am yr un amser dadansoddwr prin â didoli byw. Dewch â'ch map cwmpas ATT&CK cyfredol, cyfradd wir-gadarnhaol a ffug-gadarnhaol fesuredig eich prif ganfodiadau, a chanlyniadau eich ymarfer tîm porffor diwethaf, gan mai profi coch-a-glas cydweithredol yw'r ffordd gyflymaf o brofi pa ganfodiadau sydd wir yn tanio. Mewn lleoliadau menter a llywodraeth lle gall fframwaith fod yn orfodol, cysylltwch bob canfyddiad â pherchennog wedi'i enwi a chyflymder adolygu, oherwydd cwmpas nad oes neb yn ei gynnal yw cwmpas rydych yn darganfod eich bod wedi'i golli dim ond ar ôl y tor.

6. **A ydych yn adeiladu canfod ac ymateb yn fewnol, yn prynu canfod ac ymateb a reolir, neu'n cyfuno'r ddau, ac a ydych wedi prisio beth mae sylw rownd-y-cloc gwirioneddol yn ei gostio?** Mae amser preswyl yn gyrru cost torion, felly'r oriau heb eu gorchuddio (nosweithiau, penwythnosau, gwyliau) yw'n union pryd mae ymwthiwr heb ei ganfod yn gwneud y difrod mwyaf, ac eto mae staffio canolfan gweithrediadau diogelwch 24/7 yn fewnol yn ddrud ac yn anodd ei gynnal. Y cyfnewid yw cyd-destun a rheolaeth yn erbyn cost a chyflymder i sylw: mae tîm mewnol yn adnabod eich ystad yn ddwfn ond yn araf ac yn ddrud i'w adeiladu, tra bod darparwr a reolir yn rhoi arbenigedd ar unwaith rownd y cloc am bris cyd-destun teneuach a dibyniaeth ar werthwr. Dewch â'ch oriau sylw cyfredol, eich cyfartaledd amser i ganfod ac ymateb yn ystod oriau y tu allan, eich cyfaint rhybudd, a darlleniad gonest o a allwch recriwtio a chadw'r dadansoddwyr y mae canolfan a redir yn fewnol eu hangen. I lywodraeth a mentrau rheoledig, pwyswch breswylfa data, cliriad personél, a rhwymedigaethau adrodd statudol y mae'n rhaid i'r darparwr allu eu bodloni, a chadarnhewch fod y contract yn cadw'r trylwyredd fforensig a'r gadwyn gadwraeth y mae achosion cyfreithiol yn eu mynnu.

## Trwy lens sector

**Cwmni newydd.** Mae cyflymder a goroesiad yn dod yn gyntaf, felly prynwch ddiogelwch fel sgil-gynnyrch o offer rydych eisoes yn eu rhedeg yn hytrach na staffio gweithrediadau. Weiriwch sganwyr rhad ac am ddim i mewn i CI i rwystro gollyngiadau cyfrinachau a dibyniaethau y gwyddys eu bod yn fregus adeg cyflwyno, anfonwch logiau ymlaen i wasanaeth a reolir cost isel gyda llond dwrn o rybuddion gwerth uchel, ac ysgrifennwch gynllun digwyddiad un dudalen (pwy i'w ffonio, sut i gylchdroi credlythyrau, cipiwch ddelwedd cyn i chi ailadeiladu) cyn bod ei angen arnoch byth. Eich adnodd prinnaf yw sylw peirianneg, felly awtomeiddiwch y drefn arferol a gwrthsefwch sefydlu canolfan weithrediadau diogelwch na allwch ei chadw i redeg.

**Busnes bach.** Heb arbenigwr diogelwch pwrpasol a chyllideb dynn, dibynnwch ar ganfod ac ymateb a reolir ac ar y nodweddion diogelwch sydd eisoes wedi'u hadeiladu i mewn i'ch platfformau. Triniwch batsio a rhestr eiddo fel yr arferion trosoledd uchaf: gwybyddwch beth rydych yn ei redeg, cadwch ef yn gyfredol, a gorfodwch derfyn amser unioni syml yn ôl difrifoldeb. Ffafriwch werthwyr sy'n trin monitro rownd-y-cloc, cymeriant datgeliad cydgysylltiedig, a dalgnu fforensig ar eich rhan, ac ymarferwch yr un peth na allwch ei allanoli, sef penderfynu pwy sy'n datgan digwyddiad a phwy sy'n siarad â chwsmeriaid.

**Menter.** Yr her yw cysondeb ar draws llawer o dimau a channoedd o biblinellau: polisi giât rhwystro-yn-erbyn-olrhain a rennir, SLAau unioni a orfodir ar draws y sefydliad, platfform SIEM a SOAR gyda chanfodiadau mesuredig, a thimio porffor sy'n troi pob ymarfer yn gwmpas newydd. Rheolwch weithrediadau diogelwch fel portffolio gyda dangosfyrddau ar gyfer cyfartaledd amser i ganfod ac ymateb, cydymffurfiad SLA, a chywirdeb canfod, a phenderfynwch yn fwriadol lle mae dyfnder mewnol yn curo graddfa a reolir. Cyllidebwch gost goruchwyliaeth ddynol didoli a thiwnio'n benodol, oherwydd mae awtomeiddio'n symud ymdrech yn hytrach na'i dileu.

**Llywodraeth.** Mae rheolau caffael, tryloywder, ac atebolrwydd cyhoeddus yn siapio pob dewis. Mae terfynau amser adrodd digwyddiadau statudol a datgeliad gwendidau cydgysylltiedig yn rhwymedigaethau yn hytrach na dewisiadau, felly ymarferwch y llwybr hysbysu i'r awdurdod cenedlaethol mor ofalus â'r ymateb technegol, a chadwch dystiolaeth fforensig o dan gadwyn gadwraeth sy'n gwrthsefyll gwyliadwriaeth gyfreithiol. Ffafriwch gontractau sy'n cadw rhesymeg canfod a data'n gludadwy, mynnwch fod unrhyw ddarparwr a reolir yn bodloni gofynion preswylfa a chliriad, a disgwyliwch i asesiadau tîm coch a sganio parhaus fwydo proses awdurdodi y gall y cyhoedd ymddiried ynddi.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd heb ganolfan weithrediadau diogelwch yn weirio sganwyr rhad ac am ddim i mewn i'w biblinell CI fel bod gollyngiadau cyfrinachau a dibyniaethau y gwyddys eu bod yn fregus yn cael eu dal adeg cyflwyno, gan rwystro dim ond ar ganfyddiadau hyder uchel fel nad yw'r ddau beiriannydd yn boddi mewn sŵn. Maen nhw'n ysgrifennu cynllun digwyddiad un dudalen cyn bod ei angen arnynt: pwy i'w ffonio, sut i gylchdroi credlythyrau, a chipio delwedd o westeiwr a beryglwyd cyn ei ailadeiladu fel y gallant ddysgu beth ddigwyddodd. Maen nhw'n anfon logiau ymlaen i wasanaeth a reolir cost isel ac yn gosod ychydig rybuddion ar y digwyddiadau a fyddai mewn gwirionedd yn arwyddo tor, fel bod problem yn ymddangos mewn oriau yn hytrach na'r misoedd mae'n ei gymryd i sylwi ar hap.

**Menter.** Mae cwmni meddalwedd-fel-gwasanaeth yn rhedeg SAST, SCA, IaC, a sganio cyfrinachau ym mhob piblinell, gan rwystro dim ond ar ganfyddiadau difrifoldeb uchel, hyder uchel ac olrhain y gweddill ar ddangosfwrdd gyda SLAau unioni. Mae SIEM yn bwydo platfform SOAR sy'n ynysu gwesteiwyr yn awtomatig ac yn dirymu credlythyrau ar rybuddion hyder uchel, gan dorri'r cyfartaledd amser i ymateb o oriau i funudau. Mae ymarferion tîm porffor chwarterol yn erbyn technegau MITRE ATT&CK yn cynhyrchu rheolau canfod newydd yn uniongyrchol, gan gau bylchau cwmpas yn gyson.

**Llywodraeth.** Mae asiantaeth ffederal yn gweithredu canolfan weithrediadau diogelwch (SOC) gydag adrodd digwyddiadau gorfodol i awdurdod seiber cenedlaethol o fewn terfynau amser statudol. Mae'n rhedeg rhaglen ddatgeliad gwendidau cydgysylltiedig gyda sianel gymeriant gyhoeddus fel sy'n ofynnol gan bolisi, ac yn cadw tystiolaeth fforensig o dan weithdrefnau cadwyn gadwraeth llym sy'n addas ar gyfer achosion cyfreithiol. Mae asesiadau tîm coch blynyddol a sganio gwendidau parhaus yn bwydo awdurdodiad parhaus yr asiantaeth a'i SLAau unioni seiliedig ar risg.

## Achos busnes: cymhellion, ROI, a TCO

Mae bron popeth am yr achos dros weithrediadau diogelwch yn dod i lawr i amser preswyl: po hiraf y mae ymosodwr yn mynd heb ei ganfod, y mwyaf mae'r tor yn ei gostio. Mae astudiaethau'n dangos yn gyson bod digwyddiadau a gynhwysir yn gyflym yn costio llawer llai na'r rhai sy'n llusgo am fisoedd. Mae cyfanswm cost perchnogaeth yn cynnwys offer (SIEM, SOAR, sganwyr), staffio neu wasanaethau a reolir ar gyfer canfod ac ymateb, a'r amser i adeiladu ac ymarfer prosesau digwyddiadau. Yn erbyn hynny mae cost peidio â buddsoddi: tor a ddarganfyddir yn hwyr, yn lledaenu ar draws systemau, yn denu dirwyon rheoleiddiol, hysbysiadau gorfodol, achosion cyfreithiol, a niwed i enw da, y cyfan wedi'i waethygu gan anhrefn ymateb heb ei ymarfer.

Daw'r ROI o ganfod ac ymateb cyflymach, awtomeiddio sy'n caniatáu i dîm main orchuddio ystad fawr, a gwelliannau atal a fwydir yn ôl o bob digwyddiad ac ymarfer. Mae DevSecOps yn arbennig yn talu ar ei ganfed drwy ddal materion yn y biblinell lle maent yn rhad, yn hytrach nag mewn cynhyrchiad lle maent yn ddrud ac yn gyhoeddus. Pan fyddwch yn gwneud yr achos i arweinyddiaeth, rhowch rifau ar eich cyfartaledd amser cyfredol i ganfod ac ymateb, dangoswch sut mae'r rheini'n cysylltu ag amser preswyl a chost, a fframiwch awtomeiddio fel lluosogiad grym sy'n osgoi tyfu niferoedd staff yn gyfochrog â'r ystad. I lywodraeth, pwysleisiwch fod rhwymedigaethau adrodd a datgelu statudol yn gwneud gweithrediadau aeddfed yn anorfod.

## Gwrth-batrymau a pheryglon

- **Blinder rhybudd.** Cynifer o rybuddion fel bod dadansoddwyr yn diystyru ac yn colli'r un gwirioneddol.
- **Sganio heb unioni.** Cynhyrchu canfyddiadau nad oes neb yn eu trwsio, gan greu ymdeimlad ffug o ddiogelwch a dyled archwilio.
- **Dim cynllun digwyddiad.** Byrfyfyrio yn ystod argyfwng, gwastraffu munudau critigol a chamdrin tystiolaeth.
- **Dinistrio tystiolaeth.** Ailadeiladu gwesteiwr a beryglwyd cyn dal fforensig, gan golli'r gallu i ddeall neu brofi beth ddigwyddodd.
- **Diwylliant bai mewn adolygiadau.** Cosbi ymatebwyr fel bod y digwyddiad nesaf yn cael ei guddio neu ei drin yn amddiffynnol.
- **Profi treiddiad cydymffurfiaeth-yn-unig.** Un prawf blynyddol i fodloni archwilydd, gyda chanfyddiadau'n cael eu hanwybyddu hyd y flwyddyn nesaf.
- **Giatiau rhwystrol â ffug-gadarnhaol uchel.** Erydu ymddiriedaeth hyd nes bod peirianwyr yn mynnu bod y giatiau'n cael eu tynnu'n gyfan gwbl.
- **Canfodiadau gosod-ac-anghofio.** Rheolau sy'n dirywio wrth i'r amgylchedd a'r gwrthwynebwyr esblygu, gan golli cwmpas yn dawel.

## Model aeddfedrwydd

**Lefel 1, Cychwyn.** Mae gweithrediadau diogelwch yn ad hoc ac yn adweithiol. Mae profi diogelwch â llaw ac yn brin, ac nid oes logio canolog na SIEM. Nid oes cynllun digwyddiad yn bodoli, felly caiff ymateb ei fyrfyfyrio ar y pryd. Dim ond pan fydd penawd yn gorfodi hynny y digwydd patsio, ac ni chaiff amddiffynfeydd eu profi'n wrthwynebus byth.

**Lefel 2, Datblygu.** Mae arferion sylfaenol yn ymddangos ond yn anghyson ar draws timau. Mae rhai piblinellau'n rhedeg sganwyr tra bod eraill yn rhedeg dim, ac mae logio canolog yn bodoli mewn clytiau. Mae cynllun digwyddiad sylfaenol wedi'i ddogfennu ond anaml yn cael ei ymarfer, mae patsio'n dilyn amserlenni llac, ac mae prawf treiddiad blynyddol yn bodloni cydymffurfiaeth heb newid llawer. Mae cwmpas a thrylwyredd yn dibynnu ar ba dîm rydych yn ei ofyn.

**Lefel 3, Safoni.** Mae arferion wedi'u dogfennu a'u gorfodi ar draws y sefydliad. Cymhwysir sganio DevSecOps llawn gyda giatiau seiliedig ar risg yn gyson, mae SIEM yn cydberthyn digwyddiadau, ac mae llyfrau chwarae SOAR cychwynnol yn rhedeg. Mae ymateb i ddigwyddiadau'n cael ei ymarfer gydag ymarferion bwrdd ac adolygiadau di-fai, mae SLAau unioni yn ôl difrifoldeb yn cael eu gorfodi gyda pherchnogion wedi'u henwi, ac mae datgeliad gwendidau cydgysylltiedig a thimio coch rheolaidd yn norm yn hytrach na'r eithriad.

**Lefel 4, Rheoli.** Mesurir a rheolir gweithrediadau yn erbyn llinellau sylfaen. Olrheinir y cyfartaledd amser i ganfod ac ymateb, cydymffurfiad SLA yn ôl haen ddifrifoldeb, cwmpas sganio, cyfraddau gwir-gadarnhaol a ffug-gadarnhaol canfod, ac amser preswyl ar ddangosfyrddau ac adolygir ar gyflymder. Mae canfodiadau'n cario manwl gywirdeb ac adalw mesuredig wedi'u mapio i MITRE ATT&CK, mae penderfyniadau awtomeiddio wedi'u giatio ar ddata ffug-gadarnhaol yn hytrach na gobaith, ac mae metrig sy'n drifftio y tu hwnt i'w linell sylfaen yn sbarduno ymateb diffiniedig yn hytrach na mynd heb ei sylwi.

**Lefel 5, Cyd-drefnu.** Gwellir gweithrediadau diogelwch yn barhaus, wedi'u hintegreiddio ar draws y sefydliad, ac yn addasol. Mae peirianneg canfod, timio porffor, unioni, ac adolygiad digwyddiadau'n bwydo un ddolen sy'n addasu i dechnegau gwrthwynebwyr newydd wrth iddynt ymddangos. Mae llyfrau chwarae awtomataidd yn trin y drefn arferol ar draws yr ystad gyfan fel bod bodau dynol yn canolbwyntio ar farn, cynllunnir diogelwch ochr yn ochr â chyflenwi a risg, ac mae pob digwyddiad ac ymarfer yn caledu'r system yn fesuradwy tra bod y metrigau craidd yn parhau i dueddu i lawr.

## Syniadau ar gyfer trafodaeth

1. Pa ganfyddiadau piblinell ddylai rwystro rhyddhad, a pha rai ddylai gael eu holrhain yn unig?
2. Adeiladu SOC mewnol, defnyddio canfod ac ymateb a reolir, neu gyfuno'r ddau, a pham?
3. Sut rydych yn cadw rheolau canfod rhag dirywio wrth i'ch amgylchedd esblygu?
4. Pa mor ymosodol ddylai patsio gael ei awtomeiddio o ystyried risg newidiadau sy'n torri?
5. Sut olwg sydd ar adolygiad ôl-ddigwyddiad gwirioneddol ddi-fai yn eich diwylliant chi?
6. Sut rydych yn mesur a yw timio coch a phorffor mewn gwirionedd yn gwella eich amddiffynfeydd?

## Prif negeseuon

- Mae atal yn methu yn y pen draw; mae gweithrediadau'n bodoli i ganfod ac ymateb yn gyflym.
- Plannwch SAST, DAST, SCA, IaC, a sganio cyfrinachau yn y biblinell gyda giatiau seiliedig ar risg.
- Blaenoriaethwch batsio yn ôl ecsbloetiadwyedd gwirioneddol a hanfodolrwydd asedau, o dan SLAau gorfodedig.
- Ymarferwch ymateb i ddigwyddiadau, cadwch dystiolaeth fforensig, a chynlluniwch gyfathrebiadau tor diogelwch ymlaen llaw.
- Defnyddiwch SIEM a SOAR i gydberthyn ac awtomeiddio; triniwch ganfodiadau fel cod wedi'i beiriannu, wedi'i brofi.
- Dilyswch amddiffynfeydd gyda phrofi treiddiad, timio coch, a thimio porffor cydweithredol.
- Mae amser preswyl yn gyrru cost torion, felly'r cyfartaledd amser i ganfod ac ymateb yw'r metrigau sy'n bwysig.

## Cyfeiriadau a darllen pellach

- National Institute of Standards and Technology, *SP 800-61: Computer Security Incident Handling Guide*
- National Institute of Standards and Technology, *SP 800-40: Guide to Enterprise Patch Management*
- MITRE, *ATT&CK Framework*
- Anton Chuvakin and others, *Logging and Log Management* / llenyddiaeth SIEM
- Jim Bird, *DevOpsSec: Securing Software through Continuous Delivery*
- Richard Bejtlich, *The Practice of Network Security Monitoring*
- FIRST, canllawiau *Coordinated Vulnerability Disclosure* a manyleb *CVSS*
