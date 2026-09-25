# 2.3 APIs a dylunio rhyngwynebau

## Trosolwg a chymhelliant

Mae [API](https://en.wikipedia.org/wiki/API) (rhyngwyneb rhaglennu cymwysiadau) yn gontract y mae un darn o feddalwedd yn cynnig gallu i'r llall drwyddo. Dyma lle mae timau, systemau, a sefydliadau'n cyfarfod, a dyma'r peth mwyaf parhaol a drud i'w gael yn anghywir. Gallwch ailffactora llofnod ffwythiant mewnol yn rhydd. Mae API cyhoeddedig yn wahanol: mae'n addewid i ddefnyddwyr efallai na fyddwch byth yn cyfarfod â nhw, ac mae ei dorri'n eu torri nhw. Wrth i sefydliadau hollti [monolithau](https://en.wikipedia.org/wiki/Monolithic_application) yn wasanaethau ac agor galluoedd i bartneriaid a'r cyhoedd, mae'r API'n dod yn brif wyneb cynnyrch a'r prif risg integreiddio.

I dimau mawr, APIs yw'r hyn sy'n galluogi pobl i weithio'n annibynnol. Mae rhyngwyneb wedi'i ddylunio'n dda'n gadael i chi newid eich mewnolion heb gydgysylltu â phob defnyddiwr, sef holl bwynt ffin gwasanaeth. Mae un wedi'i ddylunio'n wael yn gollwng manylion mewnol, yn gorfodi defnyddio ar yr un pryd, ac yn troi set o wasanaethau'n fonolith dosbarthedig: gwasanaethau wedi'u hollti ar wahân ond wedi'u cyplu cymaint fel bod yn rhaid eu hadeiladu a'u defnyddio gyda'i gilydd. Mae dylunio eich API'n penderfynu'n uniongyrchol pa mor annibynnol y gall eich timau symud.

Mewn lleoliadau menter a llywodraethol, mae APIs hefyd yn cario rhwymedigaethau cydymffurfiaeth, diogelwch, a hirhoedledd. Efallai y bydd yn ofynnol i API sector cyhoeddus ddilyn [safonau agored](https://en.wikipedia.org/wiki/Open_standard), aros yn sefydlog am flynyddoedd, a gwasanaethu datblygwyr allanol na allwch gydgysylltu â nhw. Mae APIs menter yn sail i integreiddiadau partner gyda lefelau gwasanaeth cytundebol. Mae hyn oll yn codi'r bar ar ddisgyblaeth fersiynu, [ôl-gydnawsedd](https://en.wikipedia.org/wiki/Backward_compatibility), llywodraethu, a phrofiad datblygwr.

## Egwyddorion allweddol

- Dyluniwch y contract yn gyntaf. Mae'r rhyngwyneb yn benderfyniad cynnyrch bwriadol, nid yn sgil-gynnyrch gweithredu.
- Optimeiddiwch ar gyfer profiad y defnyddiwr, nid eich cyfleustra eich hun.
- Triniwch ôl-gydnawsedd fel addewid. Mae angen fersiwn newydd a llwybr mudo ar gyfer newidiadau sy'n torri.
- Gwnewch y peth hawdd yn gywir: rhagosodiadau synhwyrol, gwallau rhagweladwy, confensiynau cyson.
- Dyluniwch ar gyfer methiant. Mae [idempotens](https://en.wikipedia.org/wiki/Idempotence) (mae gan gais wedi'i ailadrodd yr un effaith ag un unigol), ailgeisiadau, tudaleniad, a [chyfyngu cyfradd](https://en.wikipedia.org/wiki/Rate_limiting) yn bryderon dosbarth cyntaf, nid yn ôl-feddyliau.
- Dewiswch arddull y protocol i ffitio'r rhyngweithiad, nid y ffasiwn.
- Llywodraethwch APIs fel cynhyrchion, gyda pherchnogion, cylchoedd bywyd, a dogfennaeth.

## Argymhellion

### Gweithio'n API-yn-gyntaf ac wedi'i yrru gan gontract

Diffiniwch ac adolygwch gontract yr API, gan gynnwys ei adnoddau, ei weithrediadau, ei sgemâu, a semanteg gwallau, cyn ysgrifennu'r gweithrediad. Defnyddiwch fanyleb ddarllenadwy gan beiriant, fel y gall y contract gynhyrchu dogfennaeth, stybiau cleient a gweinydd, gweinyddwyr ffug, a dilysu. Nawr gall defnyddwyr ddechrau integreiddio yn erbyn y ffug tra byddwch chi'n adeiladu, a daw'r contract yn ffynhonnell gwirionedd unigol y mae'r ddwy ochr yn profi yn ei herbyn.

### Dewis arddull y rhyngweithiad yn fwriadol

Dewiswch rhwng [REST](https://en.wikipedia.org/wiki/REST) (trosglwyddiad cyflwr cynrychioliadol), [GraphQL](https://en.wikipedia.org/wiki/GraphQL), [gRPC](https://en.wikipedia.org/wiki/GRPC), a [negeseua wedi'i yrru gan ddigwyddiadau](https://en.wikipedia.org/wiki/Event-driven_architecture) yn seiliedig ar y rhyngweithiad, nid dewis personol. Defnyddiwch REST ar gyfer rhyngwynebau sy'n canolbwyntio ar adnoddau, yn eang ryngweithredol, ac yn gacheadwy. Defnyddiwch GraphQL pan fydd angen darlleniadau hyblyg, cyfansawdd dros graff cyfoethog ar gleientiaid amrywiol. Defnyddiwch gRPC ar gyfer galwadau perfformiad uchel, teip cryf rhwng gwasanaethau mewnol. Defnyddiwch negeseua wedi'i yrru gan ddigwyddiadau ar gyfer llifau gwaith anghydamserol, datgysylltiedig ac ar gyfer lledaenu newidiadau cyflwr. Mae llawer o systemau mawr yn defnyddio sawl arddull ar unwaith, pob un lle mae'n ffitio.

### Fersiynu a dadfeddiannu'n ddisgybledig

Mabwysiadwch strategaeth fersiynu eglur a pholisi dadfeddiannu cyhoeddedig: sut rydych chi'n dosbarthu newidiadau, pa mor hir rydych chi'n cefnogi hen fersiynau, a sut rydych chi'n hysbysu defnyddwyr. Tynnwch linell glir rhwng newidiadau ôl-gydnaws (ychwanegu meysydd dewisol, pwyntiau terfyn newydd) a newidiadau sy'n torri (dileu neu ailenwi meysydd, newid mathau neu semanteg). Peidiwch byth ag ailddefnyddio ystyr maes presennol. Rhowch ffenestri gorgyffwrdd i ddefnyddwyr fudo, a chyfathrebwch amserlenni ymhell ymlaen llaw.

### Gwneud semanteg gwallau'n gyson ac yn ddarllenadwy gan beiriant

Dychwelwch wallau strwythuredig, rhagweladwy: codau sefydlog darllenadwy gan beiriant, negeseuon darllenadwy gan bobl, a digon o gyd-destun i weithredu arno, heb ollwng manylion mewnol sensitif. Defnyddiwch yr un semanteg statws ar draws pob pwynt terfyn, fel y gall cleientiaid drin gwallau'n unffurf. Dogfennwch bob gwall y gallai defnyddiwr ddod ar ei draws.

### Adeiladu idempotens, tudaleniad, a chyfyngu cyfradd i mewn

Gwnewch weithrediadau ysgrifennu'n ddiogel i'w hailgeisio drwy gefnogi allweddi idempotens, fel nad yw cleient sy'n ailgeisio ar ôl amser allan yn codi tâl ddwywaith nac yn creu ddwywaith. Tudaleniwch bob pwynt terfyn rhestr o'r diwrnod cyntaf, a ffafriwch dudaleniad seiliedig ar gyrchwr ar gyfer setiau data mawr neu sy'n newid. Cymhwyswch a dogfennwch derfynau cyfradd, a dychwelwch gyflwr terfyn cyfredol i gleientiaid fel y gallant gilio'n raenus.

### Llywodraethu APIs a buddsoddi mewn profiad datblygwr

Triniwch bob API fel cynnyrch, gyda pherchennog, cylch bywyd, a chofnod catalog. Sefydlwch adolygiad dylunio neu fwrdd safonau-API fel bod rhyngwynebau'n aros yn gyson ar draws timau. Buddsoddwch mewn profiad datblygwr: dogfennau cyfeirio cywir, cyflwyniadau cyflym, enghreifftiau, blwch tywod, a chofnod newid. Mewn ecosystem fawr, mae porth neu gatalog sy'n gwneud APIs yn ddarganfyddadwy'n hanfodol.

## Cyfaddawdau: manteision ac anfanteision

| Arddull | Gorau ar gyfer | Manteision | Anfanteision |
|---|---|---|---|
| REST / HTTP | APIs cyhoeddus, sy'n canolbwyntio ar adnoddau | Hollbresennol, cacheadwy, syml, rhyngweithredol | Nôl gormod neu ry ychydig o ddata; llawer o deithiau cylch; contractau llac oni bai eu bod wedi'u nodi |
| GraphQL | Darlleniadau hyblyg ar gyfer cleientiaid amrywiol | Ymholiadau wedi'u pennu gan y cleient; un pwynt terfyn; sgema cryf | Cymhlethdod cachio a chyfyngu cyfradd; risgiau cost ymholiad; cymhlethdod gweinydd |
| gRPC | Galwadau perfformiad uchel mewnol | Cyflym, cryno, teip cryf, ffrydio | Cefnogaeth porwr wael; llai darllenadwy gan bobl; offer trymach |
| Wedi'i yrru gan ddigwyddiadau | Llifau gwaith anghydamserol, datgysylltiedig | Cyplu llac; graddadwy; gwydn | Anos rhesymu yn ei gylch; cysondeb yn y pen draw; cymhlethdod gweithredol |

Mae strategaethau fersiynu'n cyfnewid sefydlogrwydd yn erbyn cynnal a chadw. Mae cefnogi llawer o hen fersiynau'n amddiffyn defnyddwyr, ond mae'n lluosi'r cod y mae'n rhaid i chi ei gynnal a'i brofi. Mae ôl-gydnawsedd yn cyfnewid eich rhyddid eich hun am sefydlogrwydd i ddefnyddwyr, fel arfer y cyfnewid cywir ar gyfer API a ddefnyddir yn eang. Y darlun mawr: telir cost penderfyniad API gwael gan bob defnyddiwr dros holl oes y rhyngwyneb. Felly mae'n werth treulio mwy o ymdrech ddylunio ar y ffin nag mewn bron unrhyw le arall.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Sut ydych chi'n dosbarthu newid fel ôl-gydnaws yn erbyn un sy'n torri, a pha wiriad awtomataidd sy'n dal toriad tawel cyn iddo gael ei ryddhau?** Mae'r bennod hon yn tynnu llinell galed: mae ychwanegu meysydd dewisol a phwyntiau terfyn newydd yn ddiogel, tra bo dileu neu ailenwi meysydd, newid mathau, neu ailddefnyddio ystyr maes yn torri defnyddwyr. Mewn tîm mawr, ni all y person sy'n gwneud y newid weld pob defnyddiwr yn aml, felly gall addasiad "bach" dorri partneriaid nad ydych byth yn siarad â nhw'n dawel. Dewch â'r signal cadarn i'r cyfarfod: a ydych chi'n rhedeg gwiriadau cydnawsedd contract awtomataidd yn CI yn erbyn y fanyleb gyhoeddedig, neu a ydych chi'n dibynnu ar rywun yn cofio'r rheol. Mewn lleoliadau menter a llywodraethol, lle mae newid sy'n torri'n gorfodi mudo cydgysylltiedig ar draws pob partner ac a all rychwantu newidiadau gwerthwr a gweinyddiaeth, mae'r gost yn graddio gyda nifer y defnyddwyr. Penderfynwch y rheolau dosbarthu a chysylltu giât gydnawsedd, fel bod newid anghydnaws yn methu'r adeiladwaith yn hytrach nag integreiddiad.

2. **Pa gyntefigion dibynadwyedd, allweddi idempotens, tudaleniad, a chyfyngu cyfradd, sy'n orfodol ar bob pwynt terfyn newydd o'r diwrnod cyntaf?** Mae'r bennod yn mynnu bod y rhain yn bryderon dosbarth cyntaf, oherwydd mae ôl-osod allwedd idempotens ar bwynt terfyn codi tâl byw neu ychwanegu tudaleniad at restr sydd eisoes yn cael ei rhyddhau'n newid sy'n torri ynddo'i hun. Mae ecosystem fawr yn chwyddo hyn: mae pwynt terfyn sy'n gweithio mewn profi'n cwympo o dan gyfaint data go iawn, ac mae ysgrifeniad nad yw'n idempotent yn troi un chwythiad rhwydwaith yn daliadau dyblyg. Dewch â'r dystiolaeth o ba bwyntiau terfyn cyfredol sy'n eu heisiau a beth fyddai storm ailgeisio'n ei wneud. Gwnewch y rhagosodiadau'n anhrafodadwy ar gyfer pwyntiau terfyn newydd: tudaleniad cyrchwr ar bob rhestr, allweddi idempotens ar bob ysgrifeniad, terfynau cyfradd dogfennedig sy'n dychwelyd eu cyflwr cyfredol. Mae hynny'n trosi mudo gorfodol yn y dyfodol yn arferiad dylunio un-tro.

3. **A ydych chi'n dylunio ac yn adolygu'r contract yn wirioneddol cyn ysgrifennu'r gweithrediad, neu a yw'r rhyngwyneb yn gollwng allan o'r cod?** Mae'r argymhelliad API-yn-gyntaf yn gofyn am fanyleb ddarllenadwy gan beiriant, wedi'i hadolygu ymlaen llaw, sy'n cynhyrchu dogfennau, stybiau, a ffugion ac sy'n gadael i ddefnyddwyr integreiddio yn erbyn ffug tra byddwch chi'n adeiladu. Pan fydd y contract yn dilyn y gweithrediad, mae'r rhyngwyneb yn datgelu strwythur cronfa ddata fewnol ac yn newid bob tro y mae'r gweithrediad yn newid, sef y prif wrth-batrwm yn y bennod hon. Y signal i'w archwilio: a all defnyddiwr ddechrau integreiddio yn erbyn eich ffug heddiw, neu a oes rhaid iddynt aros am gefndir sy'n rhedeg. Ar gyfer APIs cyhoeddus a phartner, lle mae'r rhyngwyneb yn wyneb y cynnyrch a'r peth drutaf i'w gael yn anghywir, mae treulio diwrnod ar y contract yn arbed wythnosau o gynnwrf cefnogaeth. Gwnewch adolygiad contract yn gam gorfodol cyn i weithredu ddechrau.

4. **Pan fydd angen i ddau dîm ddatgelu'r un gallu, pa arddull rhyngweithiad sy'n ennill, a phwy sydd â'r awdurdod i wrthod pedwerydd protocol?** Mae'r bennod hon yn dweud wrthych am ddewis REST, GraphQL, gRPC, neu negeseua wedi'i yrru gan ddigwyddiadau yn ôl addasrwydd rhyngweithiad, ond ar raddfa fawr y risg wirioneddol yw bod pob tîm yn dewis ei ffefryn ei hun a bod defnyddwyr yn wynebu confensiwn gwahanol ar bob pwynt terfyn. Mae sefydliad mawr yn talu am y chwalfa honno mewn llyfrgelloedd cleient, pyrth, monitro, a'r baich gwybyddol ar bob integreiddiwr sydd bellach yn dysgu pedwar idiom yn lle un. Dewch â'r rhestr o brotocolau sydd eisoes mewn cynhyrchiad, y rhyngweithiad y dewiswyd pob un i'w wasanaethu, a'r defnyddwyr sy'n rhychwantu mwy nag un. Mae'r ystyriaeth gystadleuol yn wirioneddol: mae rhagosodiad a rennir yn lleihau gwasgariad, ac eto mae mandad anhyblyg yn gorfodi problemau siâp-gRPC i mewn i dwll siâp-REST. Enwch y corff safonau neu'r adolygiad pensaernïaeth sy'n berchen ar y broses eithriad, oherwydd mewn ystadau menter a llywodraethol mae amlder arddulliau'n dod yn dreth barhaol ar integreiddio ac yn broblem galed i'w gwrthdroi unwaith y bydd partneriaid yn dibynnu ar bob un.

5. **Beth yw ein polisi dadfeddiannu cyhoeddedig, ac a allwn ni brofi ein bod ni mewn gwirionedd yn anrhydeddu'r ffenest gefnogaeth rydym yn ei hysbysebu?** Mae'r bennod yn trin fersiynu a dadfeddiannu fel disgyblaeth: polisi ysgrifenedig ar gyfer pa mor hir mae hen fersiynau'n byw, sut mae defnyddwyr yn cael eu hysbysu, a pha orgyffwrdd y maent yn ei gael i fudo. Mae addewid na allwch ei orfodi'n waeth na dim, oherwydd mae ecosystem fawr yn cynnwys defnyddwyr nad ydych byth yn siarad â nhw a fydd yn parhau i alw fersiwn wedi'i ymddeol nes ei fod yn torri mewn cynhyrchiad. Dewch â'r dystiolaeth i'r drafodaeth: faint o fersiynau byw rydych chi'n eu cario heddiw, y defnydd gwirioneddol ar bob un, a allwch weld pa ddefnyddwyr sy'n dal i alw pwynt terfyn wedi'i ddadfeddiannu, a pha mor bell ymlaen llaw y cyhoeddwyd eich machlud diwethaf. Y pwysau cystadleuol yw cost cynnal a chadw yn erbyn sefydlogrwydd defnyddwyr, ac mae'r ddau'n wirioneddol. Ar gyfer partneriaid menter dan lefelau gwasanaeth cytundebol ac APIs sector cyhoeddus sy'n gorfod goroesi ar draws gweinyddiaethau a newidiadau gwerthwr, mae'r ffenest gefnogaeth yn ymrwymiad a all bara'n hwy na'r tîm a'i gwnaeth, felly penderfynwch pwy sy'n berchen arni a sut y profir bod machlud yn ddiogel cyn iddo ddigwydd.

6. **Sut ydym ni'n gwybod bod ein profiad datblygwr yn dda, neu a ydym ni'n ei ragdybio am fod yr API'n gweithio i ni?** Mae'r bennod hon yn fframio pob API fel cynnyrch y mae ei fabwysiadu'n dibynnu ar ddogfennau cyfeirio cywir, cyflwyniadau cyflym, enghreifftiau, blwch tywod, cofnod newid, a chatalog darganfyddadwy. Mae timau'n camgymryd yn rheolaidd "mae'r API'n gweithredu" am "mae'r API'n ddefnyddiadwy", ac mae'r bwlch yn ymddangos fel tocynnau cefnogaeth, integreiddiadau wedi methu, a defnyddwyr sy'n rhoi'r gorau iddi'n dawel. Dewch â signalau mesuradwy yn hytrach na barn: amser-i'r-alwad-lwyddiannus-gyntaf ar gyfer integreiddiwr newydd, cyfaint tocynnau cefnogaeth fesul pwynt terfyn, pa mor hen yw'r dogfennau cyhoeddedig o gymharu â'r contract byw, ac a all rhywun newydd hunan-wasanaethu o'r porth heb e-bostio'ch tîm. Y tensiwn yw bod dogfennaeth a phyrth yn costio ymdrech wirioneddol sy'n cystadlu â chyflenwi nodweddion, ac eto mewn ecosystem fawr mae profiad datblygwr gwael yn gwthio cost integreiddio ar gannoedd o ddefnyddwyr ar unwaith. Mewn llywodraeth, lle mae API agored yn gwasanaethu datblygwyr allanol na allwch gydgysylltu â nhw ac mae tryloywder yn aml yn orfodol, mae rhyngwyneb defnyddiadwy, wedi'i ddogfennu'n dda, darganfyddadwy'n rhan o'r rhwymedigaeth atebolrwydd cyhoeddus, nid yn rhywbeth braf i'w gael.

## Lens sector

**Cwmni newydd.** Gyda dau neu dri pheiriannydd a dim amser ar gyfer defod, cadwch y contract yn ysgafn ond yn real: un fanyleb ddarllenadwy gan beiriant y gall eich cwsmeriaid partner-dylunio cyntaf integreiddio yn ei herbyn tra byddwch chi'n adeiladu. Peidiwch â sefydlu porth API, catalog, na bwrdd llywodraethu eto, ond cloi'r ddau arferiad sy'n boenus i'w hychwanegu'n ddiweddarach, allweddi idempotens ar ysgrifeniadau a thudaleniad seiliedig ar gyrchwr ar restrau, oherwydd mae eu hôl-osod ar bwynt terfyn byw'n newid sy'n torri na allwch ei fforddio. Ffafriwch un arddull rhyngweithiad, bron bob amser REST, fel nad ydych yn cario unrhyw wasgariad protocol i mewn i'ch blwyddyn gyntaf.

**Busnes bach.** Heb arbenigwr API penodedig a chyllideb dynn, dibynnwch ar declynnau sy'n cynhyrchu dogfennau, ffugion, a stybiau cleient o fanyleb fel y gall generalydd gynnal y rhyngwyneb heb arbenigedd protocol dwfn. Pwyswch brynu yn erbyn adeiladu'n galed: mae porth parod neu blatfform rheoli-API'n rhoi cyfyngu cyfradd, allweddi, a phorth datblygwr i chi y byddech chi fel arall yn eu llaw-rolio. Cadwch yr wyneb yn fach a'r confensiynau'n gyson, gan fod pob pwynt terfyn ychwanegol a phob fformat gwall un-tro'n rhywbeth y mae'n rhaid i dîm tenau ei gefnogi am byth.

**Menter.** Ar draws llawer o dimau ymreolaethol, y broblem ganolog yw cysondeb heb ddod yn dagfa: canllaw arddull a rennir, adolygiad safonau-API, catalog sy'n gwneud rhyngwynebau'n ddarganfyddadwy, a gwiriadau ôl-gydnawsedd awtomataidd yn CI fel bod toriad tawel yn methu'r adeiladwaith yn hytrach nag integreiddiad. Llywodraethwch bob API fel cynnyrch gyda pherchennog enwedig, cylch bywyd, a pholisi dadfeddiannu cyhoeddedig, a mesurwch fabwysiadu, baich cefnogaeth, ac amlder newidiadau sy'n torri fel bod y portffolio'n aros yn iach. Safonwch yr arddulliau rhyngweithiad a'r rheolau fersiynu ar draws y sefydliad, oherwydd ar y raddfa hon gwasgariad yw'r rhagosodiad drud.

**Llywodraeth.** Mae rheolau caffael, mandadau safonau agored, ac atebolrwydd cyhoeddus yn siapio pob dewis. Cyhoeddwch y contract yn agored, dilynwch y safonau agored gorfodol, a darparwch flwch tywod a dogfennau cyfeirio fel y gall datblygwyr allanol na allwch gydgysylltu â nhw hunan-wasanaethu. Triniwch ôl-gydnawsedd tymor hir fel gofyniad polisi, gan fod yn rhaid i integreiddiadau oroesi ar draws gweinyddiaethau a newidiadau gwerthwr, a gwnewch newidiadau sy'n torri'n brin, wedi'u llywodraethu'n drwm, ac wedi'u cyhoeddi ymhell ymlaen llaw. Cadwch yr API a'i ddogfennaeth yn ddigon tryloyw i wrthsefyll craffu cyhoeddus ac archwiliol, ac osgowch fformatau perchnogol a fyddai'n dal gweinyddiaeth y dyfodol yn gaeth.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd cam-hadau sy'n cyflenwi ei API cyhoeddus cyntaf yn ysgrifennu'r contract fel manyleb ddarllenadwy gan beiriant cyn codio, fel y gall ei ddau gwsmer partner-dylunio integreiddio yn erbyn ffug tra bod y cefndir yn dal i gael ei adeiladu. Hyd yn oed gydag ond llond llaw o ddefnyddwyr, mae'n ychwanegu allweddi idempotens at y pwynt terfyn codi tâl a thudaleniad seiliedig ar gyrchwr at bob rhestr, oherwydd byddai eu hôl-osod unwaith y bydd partneriaid yn dibynnu ar yr API'n golygu newid sy'n torri na all ei fforddio. Mae'r contract ymlaen llaw'n costio diwrnod ac yn arbed wythnosau o gynnwrf cefnogaeth.

**Menter.** Mae cwmni taliadau mawr yn datgelu API REST cyhoeddus i filoedd o fasnachwyr. Mae pob pwynt terfyn ysgrifennu'n derbyn allwedd idempotens, fel nad yw ailgais rhwydwaith byth yn creu tâl dyblyg. Mae pob pwynt terfyn rhestr yn defnyddio tudaleniad seiliedig ar gyrchwr. Mae gwallau'n cario codau sefydlog wedi'u dogfennu mewn cyfeirnod cyhoeddus. Mae polisi dadfeddiannu ffurfiol yn gwarantu ffenest gefnogaeth hir ar gyfer unrhyw fersiwn, gydag hysbysiad ymlaen llaw a chanllawiau mudo. Mae'r ddisgyblaeth hon yn fantais gystadleuol: mae integreiddwyr yn ymddiried na fydd yr API'n torri odanynt.

**Llywodraeth.** Mae gwasanaeth digidol cenedlaethol yn cyhoeddi API agored ar gyfer data dinasyddion, gan ddilyn safonau agored gorfodol a phroses ddylunio API-yn-gyntaf. Mae'r contract wedi'i bennu a'i adolygu cyn yr adeiladu, wedi'i gyhoeddi mewn catalog API llywodraethol canolog, ac yn cael ei wasanaethu gyda blwch tywod, fel y gall datblygwyr trydydd parti, na ellir eu cydgysylltu'n unigol, integreiddio ar eu pen eu hunain. Mae ôl-gydnawsedd tymor hir yn ofyniad polisi, oherwydd bod yn rhaid i integreiddiadau oroesi ar draws gweinyddiaethau a newidiadau gwerthwr. Felly mae newidiadau sy'n torri'n brin ac wedi'u llywodraethu'n drwm.

## Achos busnes: cymhellion, ROI, a TCO

Mae dylunio API da'n lleihau cost integreiddio, sy'n aml y gost fwyaf wrth gysylltu systemau a sefydlu partneriaid. Gydag API eglur, sefydlog, wedi'i ddogfennu'n dda, mae defnyddwyr yn integreiddio mewn dyddiau heb un tocyn cefnogaeth. Mae un gwael yn cynhyrchu baich cefnogaeth diddiwedd, integreiddiadau wedi methu, a niwed i enw da. Pan fo'r API ei hun yn gynnyrch, mae profiad datblygwr yn gyrru mabwysiadu a refeniw'n uniongyrchol.

Y gost gudd fwyaf yw newidiadau sy'n torri. Mae pob newid sy'n torri'n gorfodi mudo cydgysylltiedig ar draws pob defnyddiwr, timau mewnol a phartneriaid allanol fel ei gilydd, ac mae'r gost gyfan yn graddio gyda nifer y defnyddwyr a pha mor anodd yw hi iddynt symud gyda'i gilydd. Mae buddsoddi ymlaen llaw mewn dylunio contract-yn-gyntaf, ôl-gydnawsedd, a disgyblaeth fersiynu'n osgoi'r digwyddiadau mudo drud, ar draws y sefydliad hyn. Wrth siarad ag arweinyddiaeth, fframiwch ansawdd API fel y pwynt trosoledd ar gyfer ymreolaeth tîm, twf ecosystem partner, ac osgoi mudiadau gorfodol drud. Traciwch amser integreiddio, cyfaint tocynnau cefnogaeth, ac amlder newidiadau sy'n torri fel eich tystiolaeth.

## Gwrth-batrymau a pheryglon

- **APIs gweithredu-yn-gyntaf:** mae'r rhyngwyneb yn gollwng strwythur cronfa ddata fewnol ac yn newid bob tro mae'r gweithrediad yn newid.
- **Newidiadau sy'n torri'n dawel:** mae ailddefnyddio maes neu dynhau dilysu heb godi fersiwn yn torri defnyddwyr yn annisgwyl.
- **Rhyngwynebau siaradus:** dyluniadau sy'n gofyn am lawer o deithiau cylch ar gyfer un weithred resymegol, gan niweidio perfformiad a defnyddioldeb.
- **Confensiynau anghyson:** mae pob pwynt terfyn yn dyfeisio ei enwi, ei fformat gwall, a'i dudaleniad ei hun, fel na all cleientiaid gyffredinoli.
- **Dim tudaleniad na chyfyngu cyfradd:** pwyntiau terfyn sy'n gweithio mewn profi ac yn cwympo o dan gyfaint data neu lwyth go iawn.
- **Ysgrifeniadau nad ydynt yn idempotent:** mae ailgeisiadau'n achosi dyblygiadau; mae un chwythiad rhwydwaith yn llygru data.
- **Ymlediad fersiynau:** gormod o fersiynau byw heb ddadfeddiannu, gan luosi cynnal a chadw nes ei fod yn anreolus.
- **Dogfennau fel ôl-feddwl:** cyfeirnodau heb eu dogfennu neu wedi dyddio sy'n gwthio holl gost integreiddio ar ddefnyddwyr.

## Model aeddfedrwydd

- **Lefel 1, Cychwyn:** Mae APIs yn dod i'r amlwg o weithrediad fel sgil-gynnyrch; nid oes confensiynau a rennir; mae'r rhyngwyneb yn gollwng strwythur cronfa ddata fewnol; mae newidiadau sy'n torri'n gyffredin, heb eu cyhoeddi, ac yn cael eu darganfod pan fydd integreiddiad defnyddiwr yn methu.
- **Lefel 2, Datblygu:** Mae rhai timau'n dilyn confensiynau REST sylfaenol, yn fersiynu'n anffurfiol, ac yn llaw-ysgrifennu dogfennau, ond mae'r arfer yn anghyson ar draws timau; mae idempotens, tudaleniad, a chyfyngu cyfradd yn ymddangos ar rai pwyntiau terfyn ac nid eraill; mae defnyddwyr yn dal i ddysgu chwiwiau pob API fesul achos.
- **Lefel 3, Safoni:** Mae dylunio contract-yn-gyntaf gyda manylebau darllenadwy gan beiriant wedi'i ddogfennu a'i orfodi ar draws y sefydliad; mae polisi dadfeddiannu cyhoeddedig, semanteg gwallau gyson, ac idempotens gorfodol, tudaleniad cyrchwr, a chyfyngu cyfradd yn berthnasol i bob pwynt terfyn newydd; mae canllaw arddull a rennir ac adolygiad safonau-API'n cadw rhyngwynebau'n gyson ar draws timau.
- **Lefel 4, Rheoli:** Mae'r portffolio API'n cael ei fesur a'i reoli yn erbyn llinellau sylfaen: mae gwiriadau ôl-gydnawsedd awtomataidd yn giatio pob newid yn CI, ac rydych chi'n tracio amser-i'r-alwad-lwyddiannus-gyntaf, cyfaint tocynnau cefnogaeth fesul pwynt terfyn, amlder newidiadau sy'n torri, cyfrif fersiynau byw, a defnydd fesul pwynt terfyn fel bod penderfyniadau dadfeddiannu a dylunio'n gorffwys ar dystiolaeth yn hytrach na barn. Mae pob API'n gynnyrch llywodraethedig mewn catalog gyda pherchennog enwedig, ac mae metrigau'n sbarduno gweithredu pan fydd gwasanaeth yn drifftio o'i dargedau.
- **Lefel 5, Cydgordio:** Mae strategaeth API'n cael ei gwella'n barhaus a'i hintegreiddio ar draws y sefydliad; mae'r catalog, y porth, y rheolau fersiynu, a'r giatiau cydnawsedd yn gweithio fel un system; mae'r sefydliad yn rheolaidd yn ymddeol, yn cyfuno, ac yn ailgwmpasu rhyngwynebau yn seiliedig ar fabwysiadu a chost fesuredig; mae safonau arddull-rhyngweithiad a fersiynu'n addasu wrth i'r ecosystem, partneriaid, a thechnoleg newid, ac mae newidiadau sy'n torri'n brin ac wedi'u rheoli'n dda.

## Syniadau ar gyfer trafodaeth

- Sut ydych chi'n penderfynu pryd mae API mewnol yn ddigon sefydlog i'w gyhoeddi'n allanol?
- Beth yw'r ffenest gefnogaeth gywir ar gyfer fersiynau wedi'u dadfeddiannu yn eich cyd-destun, a phwy sy'n talu amdani?
- Ble ddylai GraphQL neu gRPC ddisodli REST yn fewnol, a ble fydden nhw'n ychwanegu mwy o gymhlethdod na gwerth?
- Sut ydych chi'n gorfodi cysondeb API ar draws llawer o dimau ymreolaethol heb ddod yn dagfa?
- Sut ddylai APIs y gall AI eu defnyddio a rhyngwynebau teclyn asiant newid eich confensiynau dylunio?
- Pa wiriadau awtomataidd sy'n gallu dal newidiadau sydd heb ôl-gydnawsedd cyn iddynt gael eu rhyddhau?

## Casgliadau allweddol

- Dyluniwch y contract yn gyntaf; mae'r API'n gynnyrch ac yn addewid hirhoedlog.
- Mae ôl-gydnawsedd yn amddiffyn defnyddwyr; mae angen fersiynau newydd a llwybrau mudo ar gyfer newidiadau sy'n torri.
- Dewiswch REST, GraphQL, gRPC, neu ddigwyddiadau yn ôl addasrwydd rhyngweithiad, nid ffasiwn.
- Adeiladwch idempotens, tudaleniad, cyfyngu cyfradd, a gwallau cyson i mewn o'r diwrnod cyntaf.
- Llywodraethwch APIs fel cynhyrchion gyda pherchnogion, catalogau, a phrofiad datblygwr cryf.

## Cyfeiriadau a darllen pellach

- Roy Fielding, *Architectural Styles and the Design of Network-based Software Architectures* (traethawd ymchwil)
- Arnaud Lauret, *The Design of Web APIs*
- Mike Amundsen, *RESTful Web APIs* a *Design and Build Great Web APIs*
- Sam Newman, *Building Microservices*
- Manyleb OpenAPI; JSON Schema (fel safonau cyfeirio)
- Martin Kleppmann, *Designing Data-Intensive Applications*
