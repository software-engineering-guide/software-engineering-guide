# 2.7 Dogfennaeth

## Trosolwg a chymhelliant

Mae [dogfennaeth](https://en.wikipedia.org/wiki/Software_documentation) yn wybodaeth ysgrifenedig sy'n gadael i bobl ddefnyddio, gweithredu, a newid meddalwedd heb orfod cydosod dealltwriaeth o'r cod yn unig. Daw mewn sawl genre: sut i ddechrau arni, sut i gyflawni tasg, sut mae system wedi'i strwythuro, sut i ymateb i ddigwyddiad, beth mae [API](https://en.wikipedia.org/wiki/API) yn ei dderbyn a'i ddychwelyd. Mae pob un yn gwasanaethu darllenydd gwahanol ag angen gwahanol. Nid yw dogfennaeth dda'n ddewisol. Dyna'r gwahaniaeth rhwng gwybodaeth sy'n graddadwy ar draws sefydliad mawr a gwybodaeth sy'n byw ym mhennau ychydig o bobl yn unig.

I dimau mawr, dogfennaeth yw eich amddiffyniad gorau yn erbyn risg person-allweddol (y perygl pan fo gwybodaeth hollbwysig yn eistedd gydag un neu ychydig o bobl yn unig) a'ch ffordd gyflymaf o sefydlu newydd-ddyfodiaid. Pan fo cannoedd o beirianwyr yn dibynnu ar systemau na wnaethant eu hadeiladu, a phobl yn ymuno, yn symud, ac yn gadael drwy'r amser, ni all y sefydliad weithredu ond os yw gwybodaeth wedi'i hysgrifennu ac yn hawdd dod o hyd iddi. Mae systemau heb eu dogfennu'n troi'n frau: dim ond eu hawduron a all eu newid yn ddiogel, a phan fo'r awduron hynny'n gadael, mae'r sefydliad yn colli'r gallu i gynnal ei feddalwedd ei hun. Dyna un o'r methiannau mwyaf cyffredin a drud ar raddfa fawr.

Mae cyd-destunau menter a llywodraeth yn codi'r stanciau ymhellach. Mae systemau'n byw am amser hir, felly rhaid i'ch dogfennaeth wasanaethu cynhalwyr am flynyddoedd, hyd yn oed ddegawdau, ar ôl i'r tîm gwreiddiol fynd. Mae cyfundrefnau rheoleiddio ac archwilio'n aml yn mynnu dogfennau penodol fel tystiolaeth o reolaeth: cofnodion pensaernïaeth, [llawlyfrau gweithredu](https://en.wikipedia.org/wiki/Runbook) (gweithdrefnau gweithredol ac ymateb digwyddiadau cam wrth gam), a chofnodion penderfyniadau. Mae systemau sector cyhoeddus a drosglwyddir rhwng gwerthwyr yn dibynnu'n llwyr ar ddogfennaeth i gario gwybodaeth ar draws ffiniau contract. Ac eto mae dogfennaeth yn adnabyddus am bydru, felly'r her go iawn yw ei chadw'n gywir wrth i'r meddalwedd newid.

## Egwyddorion allweddol

- Ysgrifennwch ar gyfer darllenydd penodol ag angen penodol; mae mathau gwahanol o ddogfennaeth yn gwasanaethu dibenion gwahanol.
- Cadwch ddogfennaeth yn agos at y cod a'i thrin fel cod (docs-as-code).
- Mae cywirdeb yn curo cyflawnrwydd; mae ychydig o ddogfennaeth ddibynadwy'n curo llawer sy'n anghywir.
- Cynhyrchwch yr hyn y gellir ei gynhyrchu; peidiwch â chynnal â llaw yr hyn y gall teclyn ei gynhyrchu o'r ffynhonnell wirionedd.
- Ymladdwch bydredd dogfennaeth yn weithredol; mae dogfennau hen yn waeth na dim oherwydd eu bod yn camarwain.
- Gwnewch ddogfennaeth yn ddarganfyddadwy; mae gwybodaeth na ellir dod o hyd iddi'n absennol i bob pwrpas.
- Cofnodwch benderfyniadau a'u rhesymeg, nid dim ond y cyflwr presennol.

## Argymhellion

### Mabwysiadu docs-as-code

Cadwch ddogfennaeth mewn [rheolaeth fersiynau](https://en.wikipedia.org/wiki/Version_control) reit ochr yn ochr â'r cod y mae'n ei ddisgrifio, ysgrifennwch hi mewn marcio testun plaen, a'i hadolygu drwy'r un broses cais tynnu. Mae hynny'n ei chadw'n fersiynedig, yn adolygadwy, ac yn agos at y cod, fel y gallwch ddiweddaru'r ddau gyda'i gilydd. Cyhoeddwch hi drwy biblinell awtomataidd fel bod y fersiwn diweddaraf bob amser ar gael. Mae trin dogfennau fel cod yn dod â'r un ddisgyblaeth sy'n cadw cod yn ddibynadwy: adolygiad, hanes, ac awtomeiddio.

### Strwythuro cynnwys gyda fframwaith Diátaxis

Trefnwch ddogfennaeth yn bedwar math gwahanol, oherwydd nad yw eu cymysgu'n gwasanaethu unrhyw ddarllenydd yn dda: tiwtorialau (wedi'u cyfeirio at ddysgu, ar gyfer newydd-ddyfodiaid), canllawiau sut-i (wedi'u cyfeirio at dasg, ar gyfer nod penodol), cyfeiriadur (wedi'i gyfeirio at wybodaeth, manwl gywir a chyflawn), ac esboniad (wedi'i gyfeirio at ddealltwriaeth, y pam a'r cyd-destun). Cadwch y rhain ar wahân a bydd popeth yn haws i'w ysgrifennu, ei lywio, a'i gynnal, oherwydd bod gan bob tudalen un swydd eglur ac un gynulleidfa eglur.

### Cynnal y dogfennau gweithredol hanfodol

Rhowch [README](https://en.wikipedia.org/wiki/README) eglur i bob ystorfa fel ei drws ffrynt: beth ydyw, sut i'w adeiladu a'i redeg, a ble i fynd nesaf. Ysgrifennwch lawlyfrau gweithredu ar gyfer tasgau gweithredol ac ymateb i ddigwyddiadau, fel y gall unrhyw un ar-alwad weithredu, nid dim ond yr arbenigwyr. Cadwch ddogfennaeth bensaernïaeth sy'n esbonio strwythur y system a'i phrif gydrannau. A darparwch ddogfennaeth sefydlu sy'n gwneud peiriannydd newydd yn gynhyrchiol yn gyflym. Dyma'r dogfennau rydych chi'n eu colli fwyaf pan nad ydynt yno.

### Cynhyrchu dogfennau API a chofnodion newid o'r ffynhonnell wirionedd

Cynhyrchwch eich dogfennaeth cyfeiriadur API o'r contract y gellir ei ddarllen gan beiriant neu anodiadau cod, fel na all lithro oddi wrth y rhyngwyneb gwirioneddol. Cadwch [gofnod newid](https://en.wikipedia.org/wiki/Changelog), yn ddelfrydol wedi'i gynhyrchu o gymitiau strwythuredig neu nodiadau rhyddhau, fel y gall defnyddwyr weld beth sydd wedi newid rhwng fersiynau. Mae awtomeiddio'r rhain yn tynnu'r ddogfennaeth a gynhelir â llaw sydd fwyaf tueddol o bydru oddi ar eich plât ac yn ei chadw'n ddibynadwy.

### Cofnodi penderfyniadau pensaernïaeth

Cipiwch benderfyniadau pensaernïaeth a dylunio arwyddocaol fel cofnodion ysgafn, wedi'u dyddio, sy'n nodi'r cyd-destun, y penderfyniad, a'i ganlyniadau. Mae'r cofnodion penderfyniadau hyn yn diogelu'r rhesymeg a fyddai fel arall yn cael ei cholli, fel y gall cynhalwyr y dyfodol weld pam mae'r system fel y mae yn lle amau penderfyniadau cadarn neu ailadrodd hen gamgymeriadau. Maent yn talu ar eu canfed yn enwedig dros oes hir systemau menter a llywodraeth.

### Ymladd pydredd dogfennaeth yn fwriadol

Triniwch ddogfennaeth hen fel diffyg. Diweddarwch y dogfennau fel rhan o'r un newid sy'n newid ymddygiad, a gwnewch hynny'n ddisgwyliad adolygu. Neilltuwch berchnogaeth fel bod gan bob dogfen bwysig rywun cyfrifol amdani. Adolygwch ddogfennaeth werthfawr am gywirdeb bob hyn a hyn, tocurwch yr hyn sy'n ddarfodedig, a thynnwch neu faneriwch yn glir unrhyw beth nad ydych bellach yn ymddiried ynddo. Y ddogfennaeth sy'n pydru leiaf yw dogfennaeth fyw: wedi'i chynhyrchu neu ei phrofi yn erbyn y system ei hun.

### Buddsoddi mewn rheoli gwybodaeth a darganfyddadwyedd

Gwnewch ddogfennaeth yn hawdd dod o hyd iddi drwy chwiliad da, llywio eglur, a chartref hysbys, fel bod pobl yn gallu lleoli'r hyn sydd ei angen arnynt heb orfod gofyn i rywun. Peidiwch â gadael iddi ddarnio ar draws gormod o wicis ac offer datgysylltiedig. A chipiwch [wybodaeth ymhlyg](https://en.wikipedia.org/wiki/Tacit_knowledge), y ddealltwriaeth anffurfiol sy'n byw mewn edafedd sgwrsio ac ym mhennau pobl, i ffurf barhaol, ddarganfyddadwy cyn iddi lithro ymaith.

## Cymharu: manteision ac anfanteision

| Dull | Manteision | Anfanteision |
|---|---|---|
| Docs-as-code | Wedi'i fersiynu, yn adolygadwy, yn agos at god; pydredd isel | Angen disgyblaeth peiriannydd; llai cyfeillgar i awduron di-dechnegol |
| Wici / cronfa wybodaeth | Hawdd ei olygu; hygyrch i bawb | Yn llithro oddi wrth god; yn darnio; yn pydru'n dawel |
| Dogfennau a gynhyrchir (API, cofnod newid) | Bob amser yn gywir; cynnal a chadw isel | Cyfyngedig i'r hyn y mae'r ffynhonnell yn ei fynegi; angen offer |
| Esboniad wedi'i ysgrifennu â llaw | Cyd-destun cyfoethog a rhesymeg na all peiriannau eu cynhyrchu | Yn llafurus; tueddol o heneiddio |
| Strwythur Diátaxis | Diben eglur fesul tudalen; haws ei lywio a'i gynnal | Ymdrech strwythuro ymlaen llaw; angen disgyblaeth awdur |

Y cyfaddawd canolog yw ymdrech yn erbyn cywirdeb a pharhad. Y ddogfennaeth rataf i'w hysgrifennu, tudalen wici gyflym, hefyd yw'r fwyaf tueddol o bydru a darnio. Mae'r ddogfennaeth fwyaf parhaol, wedi'i chynhyrchu o'r ffynhonnell neu ei hadolygu fel cod, yn costio mwy o ddisgyblaeth ymlaen llaw ond yn aros yn ddibynadwy. Rheol gyffredinol dda: cynhyrchwch yr hyn y gallwch, cadwch weddill yn agos at y cod a'i adolygu fel cod, a chadwch esboniad llafurus wedi'i ysgrifennu â llaw ar gyfer y rhesymeg y gall dynion yn unig ei darparu.

## Cwestiynau i'w trafod gyda'ch tîm

1. **A yw eich dogfennau wedi'u gwahanu yn ôl angen darllenydd, neu a yw tiwtorialau, cyfeiriadur, ac esboniad yn gymysg ar un dudalen?** Mae'r bennod hon yn argymell yr hollt Diátaxis yn diwtorialau, canllawiau sut-i, cyfeiriadur, ac esboniad, ac yn rhestru cymysgu mathau fel gwrth-batrwm nad yw'n gwasanaethu unrhyw ddarllenydd yn dda. Ar raddfa fawr, mae angen tudalennau gwahanol ar newydd-ddyfodiad sy'n dysgu'r system a pheiriannydd ar-alwad sy'n hela ffaith fanwl gywir, ac mae un dudalen gymysg yn arafu'r ddau. Dewch â'r signal: dewiswch eich dogfennau mwyaf ymweledig a gwiriwch a oes gan bob un un swydd eglur ac un gynulleidfa eglur. Ail-strwythurwch y troseddwyr gwaethaf yn fathau gwahanol, fel bod pob tudalen yn haws i'w hysgrifennu, ei llywio, a'i chadw'n gyfredol. Dyna'r strwythur sy'n gwneud dogfennaeth yn gynaliadwy wrth i'r sefydliad dyfu.

2. **A ydych chi'n cipio penderfyniadau pensaernïaeth arwyddocaol gyda'u rhesymeg, neu ddim ond y cyflwr presennol?** Mae'r bennod yn argymell cofnodion penderfyniadau ysgafn, wedi'u dyddio sy'n nodi cyd-destun, penderfyniad, a chanlyniadau, ac yn nodi eu bod yn talu ar eu canfed fwyaf dros oes hir systemau menter a llywodraeth. Hebddynt, ni all cynhaliwr flynyddoedd yn ddiweddarach weld pam mae'r system fel y mae, felly maent yn amau dewisiadau cadarn neu'n ailadrodd hen gamgymeriadau. Dewch â phenderfyniad anodd diweddar y mae ei resymeg bellach yn byw dim ond mewn edefyn sgwrsio neu gof rhywun fel y signal diriaethol. Mabwysiadwch fformat cofnod penderfyniad byr a gwnewch ysgrifennu un yn rhan o unrhyw newid dylunio arwyddocaol. Y rhesymeg yw'n union y wybodaeth y gall dynion yn unig ei darparu ac sy'n pydru gyflymaf pan na chaiff ei ysgrifennu.

3. **A all unrhyw beiriannydd ar-alwad ymateb i ddigwyddiad o'ch llawlyfrau gweithredu yn unig, heb bipio'r person a adeiladodd y system?** Mae'r bennod hon yn enwi llawlyfrau gweithredu fel dogfen weithredol hanfodol fel y gall unrhyw un ar-alwad weithredu, nid dim ond yr arbenigwyr, ac yn disgrifio tîm llywodraeth a allai etifeddu system yn unig oherwydd bod llawlyfrau gweithredu'n cario'r wybodaeth ar draws ffin contract. Risg person-allweddol yw'r methiant y mae hyn yn amddiffyn rhagddo: pan fo'r un arbenigwr yn anghyraeddadwy neu wedi mynd, mae gweithdrefn adfer heb ei dogfennu'n troi digwyddiad arferol yn doriad. Dewch â'r dystiolaeth: cymerwch ddigwyddiad diweddar a gwiriwch a fyddai'r llawlyfr gweithredu ar ei ben ei hun wedi'i ddatrys. Ysgrifennwch a phrofwch lawlyfrau gweithredu ar gyfer y gweithdrefnau y mae pobl yn eu hofni, a thriniwch lawlyfr gweithredu na all sefyll ar ei ben ei hun fel diffyg. Dyna'r gwahaniaeth rhwng adferiad 2 y bore a dwysáu 2 y bore.

4. **Pa rai o'ch cyfeiriaduron API a chofnodion newid sy'n cael eu cynhyrchu o'r ffynhonnell wirionedd, a pha rai sy'n dal i gael eu cynnal â llaw ac yn llithro'n dawel?** Mae'r bennod hon yn dweud wrthych am gynhyrchu dogfennaeth cyfeiriadur o'r contract y gellir ei ddarllen gan beiriant neu anodiadau cod fel na all wyro oddi wrth y rhyngwyneb gwirioneddol, ac mae'n rhestru cynnal â llaw gynnwys y gellir ei gynhyrchu fel gwrth-batrwm. I dîm mawr, mae dogfen API wedi'i hysgrifennu â llaw sy'n llusgo ar ôl y rhyngwyneb gwirioneddol yn waeth na dim: mae pob defnyddiwr sy'n ymddiried ynddi'n ysgrifennu integreiddiad wedi torri, ac mae'r methiant yn ymddangos ymhell o'r dudalen hen a'i hachosodd. Dewch â'r signal diriaethol: samplwch lond llaw o'ch rhyngwynebau mwyaf defnyddiedig a chymharwch y cyfeiriadur cyhoeddedig â'r contract gwirioneddol i weld pa mor bell y mae pob un wedi llithro. Lle rydych yn dod o hyd i lithriad, weiriwch y cyfeiriadur i mewn i'r adeiladu fel ei fod yn ailgynhyrchu ar bob newid, ac ymddeolwch y copi a gedwir â llaw. Mewn lleoliadau menter a llywodraeth, lle mae rhyngwynebau'n cael eu defnyddio ar draws timau, gwerthwyr, a ffiniau contract na welwch byth, mae cyfeiriadur awdurdodol a gynhyrchir yn aml yn unig beth sy'n cadw integryddion rhag adeiladu yn erbyn ffuglen.

5. **Pwy sy'n berchen ar bob dogfen werthfawr, a sut fyddech chi'n sylwi heddiw pe bai un wedi mynd yn hen?** Mae'r bennod yn trin dogfennaeth hen fel diffyg ac yn rhybuddio bod dogfennau heb berchennog yn pydru oherwydd nad yw eu diweddaru'n swydd i unrhyw un, tra bo dogfennau hen a gyflwynir fel rhai cyfredol yn dinistrio ymddiriedaeth yn eich holl ddogfennaeth. Ar raddfa fawr, y perygl nid tudalen unigol anghywir yw ond erydiad araf o hyder: unwaith y bydd darllenwyr yn cael eu llosgi gan gyfarwyddiadau hen, maent yn stopio ymddiried yn y corpws cyfan ac yn mynd yn ôl at dorri ar draws pobl. Dewch â map perchnogaeth o'ch dogfennau mwyaf critigol ac ateb gonest i sut mae pydredd yn cael ei ganfod, boed drwy gadence adolygu, cynhyrchu, profion yn erbyn y system, neu lwc pur. Neilltuwch berchennog wedi'i enwi i bob dogfen sy'n bwysig, a ffafriwch ddogfennaeth fyw sy'n cael ei chynhyrchu neu ei phrofi fel bod henaint yn ymddangos yn fecanyddol yn hytrach na thrwy ddarllenydd cywilyddus. I systemau menter a llywodraeth sy'n goroesi eu timau gwreiddiol, mae dogfennaeth heb berchennog yn atebolrwydd y bydd archwiliwr neu werthwr sy'n etifeddu yn eich codi amdano yn y pen draw.

6. **Pa mor ddarganfyddadwy yw eich dogfennaeth, a faint o wybodaeth hollbwysig sy'n dal i fyw mewn edafedd sgwrsio a phennau pobl yn unig?** Mae'r bennod hon yn dweud bod gwybodaeth na ellir dod o hyd iddi'n absennol i bob pwrpas, yn rhybuddio yn erbyn darnio dogfennau ar draws gormod o wicis ac offer datgysylltiedig, ac yn eich annog i gipio gwybodaeth ymhlyg i ffurf barhaol, ddarganfyddadwy cyn iddi lithro ymaith. Mewn sefydliad mawr mae'r un ffaith yn aml yn cael ei hailddarganfod, ei hailofyn, a'i hailateb gan gant o weithiau oherwydd na all neb ddod o hyd i ble roedd eisoes wedi'i hysgrifennu, ac mae pob ymadawiad yn cymryd cyd-destun na ellir ei ddisodli allan drwy'r drws. Dewch â'r dystiolaeth: cyfrwch faint o gartrefi dogfennaeth ar wahân rydych yn eu cynnal, ceisiwch ddod o hyd i dair ffaith bwysig drwy chwilio yn unig, a nodwch ble roedd yr atebion go iawn yn byw yng nghof rhywun neu neges gladdedig. Cyfunwch tuag at gartref hysbys gyda chwiliad go iawn a llywio eglur, a gwnewch gipio gwybodaeth ymhlyg yn rhan arferol o'r gwaith yn hytrach nag achubiaeth arwrol. Mewn cyd-destunau sector cyhoeddus a llawer eu hallanoli, lle mae systemau'n mynd rhwng gwerthwyr a thimau drwy gontract, gwybodaeth ysgrifenedig ddarganfyddadwy yw'r unig beth sy'n goroesi'r trosglwyddiad.

## Trwy lens sector

**Cwmni newydd.** Gyda llond llaw o beirianwyr a dim redlan i'w sbario, dogfennwch ddim ond yr hyn y byddai toriad 2 y bore neu benodiad newydd ei angen go iawn: README go iawn fesul gwasanaeth, un llawlyfr gweithredu wedi'i brofi ar gyfer y weithdrefn rhyddhau-ac-adfer y mae pawb yn ei hofni, ac ychydig o nodiadau wedi'u dyddio ar y penderfyniadau y byddech fel arall yn eu hanghofio. Cynhyrchwch ddogfennau API o'r contract fel na fyddwch byth yn eu cynnal â llaw. Gwrthsafwch adeiladu platfform dogfennaeth; mae ffolder fersiynedig o farcio wrth ochr y cod yn ddigon hyd nes eich bod yn teimlo poen go iawn.

**Busnes bach.** Heb ysgrifennwr technegol a chyllideb dynn, pwyswch ar y ddogfennaeth y mae eich offer eisoes yn ei chynhyrchu ac ar docs-as-code ysgafn yn hytrach na rhaglen â staff. Fframiwch y dewis fel prynu yn erbyn adeiladu: ffafriwch blatfformau sy'n cynhyrchu eu cyfeiriadur cyfredol eu hunain a chronfa wybodaeth chwiliadwy dros wici y mae'n rhaid i chi ei thendio â llaw. Treuliwch eich ymdrech prin ar y ddwy neu dair dogfen y byddai eu habsenoldeb yn stopio'r busnes, a gadewch i dudalen anghywir neu goll fod y sbardun i drwsio perchnogaeth.

**Menter.** Ar draws llawer o dimau'r broblem yw cysondeb a darganfyddadwyedd: piblinell docs-as-code a rennir, strwythur cyffredin megis Diátaxis, cyfeiriaduron API a chofnodion newid a gynhyrchir, a chofnodion penderfyniadau a gymhwysir yr un ffordd ym mhobman fel nad yw gwybodaeth yn darnio ar draws dwsinau o wicis. Neilltuwch berchnogaeth i bob dogfen werthfawr a mesurwch gywirdeb, nid presenoldeb yn unig. Triniwch gofnodion pensaernïaeth, llawlyfrau gweithredu, a chofnodion penderfyniadau fel tystiolaeth archwilio, a safonwch sut y'u cynhyrchir fel bod adolygiad rheolaeth yn dod o hyd i drywydd wedi'i ddogfennu, amddiffynadwy yn hytrach na sgarmes.

**Llywodraeth.** Mae rheolau caffael ac atebolrwydd cyhoeddus yn gwneud dogfennaeth yn gyflenwad, nid yn gwrteisi. Ysgrifennwch ddogfennaeth bensaernïaeth, llawlyfrau gweithredu, a chofnodion penderfyniadau i gontractau fel arteffactau gorfodol, wedi'u hadolygu am gywirdeb fel bod gwybodaeth yn goroesi trosglwyddiad gwerthwr a system yn gallu cael ei gweithredu gan bwy bynnag sy'n ei hetifeddu. Mynnwch y gall unrhyw weithredwr awdurdodedig ymateb i ddigwyddiad o'r llawlyfr gweithredu yn unig, a chadwch gofnodion penderfyniadau fel cofnod cyhoeddus tryloyw o pam y gwnaed dewisiadau. Nid yw dogfennaeth denau yma'n anghyfleustra preifat; mae'n dod yn beirianneg wrthdro ddrud a gyllidir gan y trethdalwr.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd pump person yn ysgrifennu README go iawn ar gyfer pob gwasanaeth a llawlyfr gweithredu byr ar gyfer yr un weithdrefn rhyddhau-ac-adfer y mae pawb yn ei hofni, fel nad yw toriad 2 y bore'n dibynnu ar ddeffro'r unig sylfaenydd sy'n gwybod y system. Maent yn cynhyrchu dogfennau API o'r contract yn lle eu hysgrifennu â llaw, ac yn nodi ychydig o nodiadau wedi'u dyddio'n esbonio pam y dewison nhw eu cronfa ddata a'u dull dilysu. Mae'n aros yn ysgafn, ond mae'n golygu bod y chweched a'r seithfed penodiad yn sefydlu o ddogfennau yn hytrach na thrwy dorri ar draws pawb.

**Menter.** Mae cwmni meddalwedd mawr yn cadw ei holl ddogfennaeth yn yr un ystorfeydd â'i god, wedi'i hysgrifennu mewn marcio a'i hadolygu mewn ceisiadau tynnu reit ochr yn ochr â'r newidiadau y maent yn eu disgrifio. Mae cyfeiriaduron API'n cael eu cynhyrchu o gontractau gwasanaeth, felly nid ydynt byth yn llithro. Mae cofnodion newid yn cael eu cynhyrchu o gymitiau strwythuredig, ac mae cofnodion penderfyniadau pensaernïaeth yn diogelu'r rhesymeg y tu ôl i ddewisiadau mawr. Mae gwefan ddogfennaeth gyhoeddedig yn adeiladu'n awtomatig ar bob cyfuniad. Mae peirianwyr newydd yn dod yn gynhyrchiol yn gyflym oherwydd bod canllawiau sefydlu a llawlyfrau gweithredu'n gyfredol ac yn ddarganfyddadwy, ac mae peirianwyr ar-alwad yn pwyso ar lawlyfrau gweithredu yn lle pipio'r awduron gwreiddiol.

**Llywodraeth.** Mae asiantaeth genedlaethol yn etifeddu system gan gontractwr sy'n gadael, gan ddibynnu'n llwyr ar ddogfennaeth i gario gwybodaeth ar draws ffin y contract. Am fod y gwerthwr blaenorol wedi cynnal dogfennaeth bensaernïaeth, llawlyfrau gweithredu, a chofnodion penderfyniadau fel cyflenwadau gorfodol, gall y tîm newydd weithredu a newid y system heb yr awduron gwreiddiol. Lle roedd dogfennaeth yn denau, mae'r asiantaeth yn wynebu peirianneg wrthdro ddrud. Mae'r profiad hwnnw'n gyrru polisi newydd: mae dogfennaeth yn gyflenwad contractiol, wedi'i adolygu am gywirdeb yn hytrach na'i drin fel ôl-ystyriaeth, a rhaid i lawlyfrau gweithredu adael i unrhyw weithredwr awdurdodedig ymateb i ddigwyddiadau.

## Achos busnes: cymhellion, ROI, a TCO

Mae dogfennaeth yn talu'n ôl i chi mewn amser sefydlu byrrach, llai o risg person-allweddol, ymateb cyflymach i ddigwyddiadau, a chost newid is dros oes system. Mae peirianwyr newydd yn cyrraedd cynhyrchedd mewn diwrnodau yn hytrach nag wythnosau, staff ar-alwad yn datrys digwyddiadau o lawlyfr gweithredu yn lle dwysáu, cynhalwyr yn newid system yn hyderus flynyddoedd ar ôl iddi gael ei hadeiladu: dyma arbedion mawr, ailadroddol sy'n cyfansymu ar draws sefydliad mawr ac oes system hir.

Beth mae dogfennaeth yn ei gostio? Ymdrech awduro a chynnal a chadw. Beth mae *peidio â* dogfennu'n ei gostio? Rydych yn talu'n barhaus: mewn sefydlu araf, cwestiynau ailadroddus, tagfeydd person-allweddol, adferiad digwyddiadau arafach, ac, yn eithafol, systemau na all neb eu newid yn ddiogel, gan orfodi ailysgrifennu drud neu beirianneg wrthdro. Mewn senarios trosglwyddo gwerthwr ac archwilio, gall dogfennaeth goll gario costau contractiol a chydymffurfiaeth uniongyrchol. I wneud yr achos i'r arweinyddiaeth, rhowch rifau ar amser sefydlu, amser ymateb digwyddiadau, a faint o wybodaeth hollbwysig sy'n eistedd mewn pennau unigol. Yna fframiwch docs-as-code a chynhyrchu fel ffyrdd o gael dogfennaeth barhaol heb faich cynnal a chadw cyfatebol. A phwysleisiwch fod dogfennaeth anghywir yn atebolrwydd, felly rhaid i'r buddsoddiad gynnwys ei chadw'n gyfredol.

## Gwrth-batrymau a pheryglon

- **Dogfennaeth hen wedi'i chyflwyno fel un gyfredol:** yn camarwain darllenwyr ac yn dinistrio ymddiriedaeth ym mhob dogfennaeth.
- **Y wici ysgrifennu-unwaith:** tudalennau a grëwyd ac na chawsant eu diweddaru byth, yn llithro'n dawel oddi wrth realiti.
- **Darniad dogfennaeth:** gwybodaeth wedi'i gwasgaru ar draws llawer o offer a wicis fel na ellir dod o hyd i ddim.
- **Cymysgu mathau dogfennaeth:** tiwtorialau, cyfeiriadur, ac esboniad yn gymysg ar un dudalen, heb wasanaethu unrhyw ddarllenydd yn dda.
- **Cynnal cynnwys y gellir ei gynhyrchu â llaw:** dogfennau API wedi'u hysgrifennu â llaw sy'n anochel wyro oddi wrth y rhyngwyneb gwirioneddol.
- **Gwybodaeth lwythol:** dealltwriaeth hollbwysig a gedwir ym mhennau pobl a hanes sgwrsio'n unig, a gollir pan fyddant yn gadael.
- **Dogfennaeth fel ôl-ystyriaeth:** wedi'i hysgrifennu ar y diwedd, os o gwbl, yn hytrach nag ochr yn ochr â'r newid.
- **Dim perchnogaeth:** dogfennau heb berchennog cyfrifol yn pydru oherwydd nad yw eu diweddaru'n swydd i unrhyw un.

## Model aeddfedrwydd

- **Lefel 1, Cychwyn.** Mae dogfennaeth yn brin, wedi'i gwasgaru, ac yn hen, ac mae gwybodaeth yn byw ym mhennau pobl. Ysgrifennwyd yr hyn sy'n bodoli unwaith ac ni chafodd ei gyffwrdd wedyn, felly mae toriad neu ymadawiad yn golygu peirianneg wrthdro'r system.
- **Lefel 2, Datblygu.** Mae dogfennau allweddol yn bodoli, megis READMEs a rhai llawlyfrau gweithredu, ond fe'u cynhelir yn anghyson ac yn anodd dod o hyd iddynt. Mae rhai timau'n dogfennu'n dda ac eraill prin o gwbl, ac nid oes disgwyliad a rennir ynghylch beth ddylai ystorfa ei gario neu ble dylai fyw.
- **Lefel 3, Safoni.** Mae docs-as-code yn norm ar draws y sefydliad: strwythur cyffredin megis Diátaxis, cyfeiriaduron API a chofnodion newid a gynhyrchir, cofnodion penderfyniadau, a disgwyliad mewn adolygiad bod dogfennau'n newid gyda'r cod y maent yn ei ddisgrifio. Mae gan bob dogfen werthfawr berchennog wedi'i enwi, ac mae un cartref hysbys gyda chwiliad go iawn.
- **Lefel 4, Rheoli.** Caiff dogfennaeth ei mesur, nid dim ond ei phresenoli. Rydych yn olrhain cwmpas y dogfennau hanfodol, cyfradd newid dogfen yn erbyn cyfradd newid cod, amser sefydlu, datrys digwyddiadau o lawlyfrau gweithredu yn unig, a ffresni yn erbyn trothwy henaint diffiniedig, ac rydych yn adolygu'r metrigau hynny yn erbyn llinellau sylfaen. Caiff pydredd ei ddal yn fecanyddol drwy gynhyrchu, profion yn erbyn y system, a gwiriadau dolen a chywirdeb, a chaiff tudalennau hen eu baneru neu eu tocio ar sail tystiolaeth yn hytrach na siawns.
- **Lefel 5, Cerddorfeiddio.** Caiff dogfennaeth ei gwella'n barhaus a'i integreiddio ar draws y sefydliad: yn fyw, wedi'i chynhyrchu neu ei phrofi'n bennaf yn erbyn y system, yn berchen, yn ddarganfyddadwy, ac yn addasol. Mae metrigau'n bwydo'n ôl i mewn i ble rydych yn buddsoddi, caiff gwybodaeth ymhlyg ei chipio fel rhan arferol o'r gwaith, a chaiff y corpws ei ailgydbwyso a'i docio'n weithredol wrth i systemau, timau, a darllenwyr newid.

## Syniadau i'w trafod

- Pa ddogfennaeth, pe bai'n diflannu yfory, fyddai'n brifo'ch sefydliad fwyaf, ac a yw'n bodoli ar hyn o bryd ac yn aros yn gyfredol?
- Sut ydych chi'n gwneud diweddaru dogfennaeth yn rhan naturiol o newid cod yn hytrach na gorchwyl ar wahân?
- Ble gallwch chi ddisodli dogfennaeth wedi'i hysgrifennu â llaw â dogfennaeth a gynhyrchir wedi'i chlymu wrth y ffynhonnell wirionedd?
- Sut ydych chi'n mesur a yw eich dogfennaeth yn gywir ac yn cael ei defnyddio, nid dim ond yn bresennol?
- Sut dylai cynorthwywyr AI newid sut rydych chi'n ysgrifennu, yn cynnal, ac yn chwilio dogfennaeth, a ble gallent gyflwyno cynnwys credadwy-ond-anghywir?
- Sut ydych chi'n cipio gwybodaeth ymhlyg cyn i'r bobl sy'n ei dal adael?

## Prif negeseuon

- Triniwch ddogfennaeth fel cod: wedi'i fersiynu, wedi'i adolygu, yn agos at y ffynhonnell, ac wedi'i gyhoeddi'n awtomatig.
- Strwythurwch gynnwys yn ôl angen darllenydd gan ddefnyddio tiwtorialau, canllawiau sut-i, cyfeiriadur, ac esboniad.
- Cynhaliwch yr hanfodion gwerthfawr: READMEs, llawlyfrau gweithredu, dogfennau pensaernïaeth, sefydlu, a chofnodion penderfyniadau.
- Cynhyrchwch ddogfennau API a chofnodion newid fel na allant lithro oddi wrth y ffynhonnell wirionedd.
- Ymladdwch bydredd â pherchnogaeth, disgwyliadau adolygu, a thocio; mae dogfennaeth anghywir yn waeth na dim.

## Cyfeiriadau a darllen pellach

- Daniele Procida, *Diátaxis* documentation framework
- Andrew Etter, *Modern Technical Writing*
- Anne Gentle, *Docs Like Code*
- Google, *Developer Documentation Style Guide* and Season of Docs guidance (as reference exemplars)
- Michael Nygard, *Documenting Architecture Decisions* (architecture decision records)
- Andrew Hunt and David Thomas, *The Pragmatic Programmer* (on knowledge and documentation)
- *Keep a Changelog* (as a reference convention)
