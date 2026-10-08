# 2.9 Adeiladu meddalwedd

## Trosolwg a chymhelliant

Mae [adeiladu meddalwedd](https://en.wikipedia.org/wiki/Software_construction) yn lle mae dyluniad yn dod yn god sy'n rhedeg. Dyma'r gwaith manwl o godio, gwirio, [profi unedau](https://en.wikipedia.org/wiki/Unit_testing), [profi integreiddio](https://en.wikipedia.org/wiki/Integration_testing), a [dadfygio](https://en.wikipedia.org/wiki/Debugging). Mae Canllaw [Corff Gwybodaeth Peirianneg Meddalwedd](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) (SWEBOK) yn trin adeiladu fel maes gwybodaeth ynddo'i hun, a hynny am reswm da: dyma lle mae'r rhan fwyaf o'ch gwaith dydd-i-ddydd yn digwydd. Mae'r dewisiadau a wnewch linell wrth linell (sut rydych yn cynnwys cymhlethdod, sut rydych yn trin gwallau, pa mor ddarllenadwy y gadewch bethau) yn penderfynu a all system gael ei deall, ei newid, a'i thrystio am flynyddoedd i ddod.

Ar dîm mawr, mae adeiladu'n ymdrech grŵp, nid un unigol. Mae cannoedd o beirianwyr yn ysgrifennu i mewn i sylfaen god a rennir a fydd yn goroesi amser unrhyw un person ar y tîm. Felly nid "a yw'n gweithio ar fy mheiriant heddiw" yw'r bar. "A all dieithryn newid hyn yn ddiogel mewn pum mlynedd" ydyw. Mae adeiladu'n cysylltu i fyny â gofynion (pennod 2.8) a dyluniad (pennod 2.2), sy'n dweud wrthych beth i'w adeiladu a'i siâp. Mae'n cysylltu i'r ochr â safonau codio (pennod 2.1), profi (pennod 2.4), ac adolygiad cod (pennod 2.5), sy'n siapio sut mae'r gwaith yn cael ei fynegi, ei wirio, a'i archwilio. Mae adeiladu da yn troi dyluniad cadarn yn ased y gellir ei gynnal. Mae adeiladu gwael yn troi hyd yn oed dyluniad da yn rhwymedigaeth.

Mewn lleoliadau mentrau a llywodraethol, mae adeiladu'n cario pwysau ychwanegol. Mae'r systemau hyn yn hirhoedlog, yn drwm-reoleiddiedig, ac yn aml yn ddiogelwch-dyngedfennol neu'n ddinesydd-dyngedfennol. Nid moethusrwydd yw [codio amddiffynnol](https://en.wikipedia.org/wiki/Defensive_programming), trin gwallau disgybledig, a chod sy'n amlwg gywir yma; gofynion ar gyfer sicrwydd, archwiliad, a pharhad ar draws degawdau a throsiant staff ydynt. Y nod yw cod sy'n cyfleu ei fwriad, yn gwrthsefyll methiant, ac y gellir ei wirio. Nid yw cod sydd ond yn rhedeg yn ddigon.

## Egwyddorion allweddol

- Lleihewch gymhlethdod uwchlaw popeth; prif elyn adeiladu ar raddfa fawr yw cod nad oes neb yn ei ddeall yn llawn.
- Rhagwelwch newid; adeiladwch fel bod addasiadau tebygol y dyfodol yn lleol ac yn rhad.
- Adeiladwch ar gyfer gwiriad; ysgrifennwch god y mae ei gywirdeb yn hawdd ei wirio â phrofion, adolygiad, a rhesymu.
- Ailddefnyddiwch yn fwriadol; adeiladwch ar gydrannau presennol dibynadwy yn hytrach nag ailddyfeisio, ond osgowch gyplu i'r haniaethiadau anghywir.
- Dilynwch safonau; mae cysondeb ar draws sylfaen god yn lleihau cost wybyddol pob newid yn y dyfodol.
- Triniwch wallau a chyflyrau annilys yn amlwg; gwnewch foddau methiant yn weladwy yn hytrach na thawel.
- Cadwch god yn ddarllenadwy; cyfathrebu â chynhalwyr y dyfodol yw adeiladu yn gyntaf a'r crynhoydd yn ail.

## Argymhellion

### Lleihewch gymhlethdod fel y ddisgyblaeth graidd

Gwnewch leihau cymhlethdod, hanfodol a damweiniol fel ei gilydd, yn nod canolog. Ysgrifennwch ffwythiannau a modylau bach, un-diben. Ffafriwch enwau clir dros driciau clyfar. Cadwch nythu'n fas a llif rheolaeth yn llinellol. Lleoleiddiwch benderfyniadau fel nad yw deall un darn o god yn eich gorfodi i ddal y system gyfan yn eich pen. Cymhlethdod yw'r hyn sy'n gwneud sylfeini cod mawr yn araf i'w newid ac yn beryglus i'w cyffwrdd, felly pwyswch bob dewis yn ôl a yw'n ychwanegu cymhlethdod neu'n ei dynnu i ffwrdd. Cymhwyswch egwyddorion dylunio pennod 2.2 ar y raddfa fach hefyd: mae cydlyniant uchel, cyplu isel, a [gwahaniad pryderon](https://en.wikipedia.org/wiki/Separation_of_concerns) clir yr un mor bwysig mewn un ffwythiant ag mewn pensaernïaeth.

### Adeiladwch ar gyfer newid a gwiriad

Meddyliwch ymlaen llaw am y newidiadau mwyaf tebygol o ddod (rheolau busnes newydd, integreiddiadau newydd, rheoliadau newydd) a'u hynysu y tu ôl i ryngwynebau sefydlog fel bod newid yn aros yn lleol. Ar yr un pryd, ysgrifennwch god sy'n hawdd ei wirio: [ffwythiannau pur](https://en.wikipedia.org/wiki/Pure_function) (mae'r un mewnbynnau bob amser yn cynhyrchu'r un allbwn, heb sgil-effeithiau) lle gallwch, cyflwr cudd lleiafswm, a dibyniaethau wedi'u gwneud yn amlwg fel y gall profion eu disodli. Mae cod sy'n anodd ei brofi fel arfer yn god sy'n anodd ei ddeall a'i newid. Mae profadwyedd (pennod 2.4) yn signal dylunio, nid dim ond pryder sicrwydd ansawdd.

### Ailddefnyddiwch yn fwriadol a safonwch

Estynnwch am lyfrgelloedd a chydrannau mewnol wedi'u cynnal yn dda, dibynadwy cyn ailysgrifennu rhesymeg sylfaenol, a'u defnyddio drwy ryngwynebau clir (pennod 2.3). Adeiladwch gydrannau y gellir eu hailddefnyddio dim ond pan fo achos defnydd gwirioneddol ail yn bodoli, oherwydd mae cyffredinoli'n rhy gynnar yn ffurf ei hun o gymhlethdod. Cymhwyswch safonau ac arddull codio eich sefydliad (pennod 2.1) yn unffurf, yn ddelfrydol wedi'u gorfodi gan fformatwyr a [chysonwyr](https://en.wikipedia.org/wiki/Lint_(software)) awtomataidd, fel bod y sylfaen god gyfan yn darllen fel pe bai un awdur gofalus wedi'i hysgrifennu.

### Ymarferwch raglennu amddiffynnol gyda barn

Dilyswch fewnbynnau ar ffiniau ymddiriedaeth (ceisiadau allanol, I/O ffeiliau a rhwydwaith, mewnbwn defnyddiwr) a thriniwch unrhyw ddata sy'n croesi'r ffiniau hynny fel gelyniaethus nes ei brofi fel arall. Y tu mewn i fodwl sydd wedi'i brofi'n dda, fodd bynnag, peidiwch â mygu pob llinell mewn gwiriadau dianghenraid sy'n cuddio'r rhesymeg ac yn atal methiannau gwirioneddol. Mae'r rheol yn syml: amddiffynnwch ar y ffiniau, ymddiriedwch oddi mewn iddynt. Defnyddiwch [gadarnhadiadau](https://en.wikipedia.org/wiki/Assertion_(software_development)) i ddogfennu a gorfodi priodweddau digyfnewid na ddylent fyth fod yn anwir mewn rhaglen gywir. Defnyddiwch [eithriadau](https://en.wikipedia.org/wiki/Exception_handling) a thrin gwallau ar gyfer amodau a all ddigwydd yn ddilys adeg rhedeg. Cadwch y ddau ar wahân: mae cadarnhadiadau'n gwarchod tybiaethau'r rhaglennydd, mae trin gwallau'n rheoli methiant disgwyliedig.

### Triniwch wallau'n amlwg a methwch yn ddiogel

Ar gyfer pob gwall, penderfynwch yn fwriadol beth i'w wneud: adfer, ailgynnig, lledaenu, neu fethu'n gyflym. Peidiwch byth â llyncu eithriad yn dawel na anwybyddu gwall a ddychwelwyd; mae methiant wedi'i atal yn dychwelyd fel diffyg dirgel yn ddiweddarach. Cadwch gyd-destun yn eich negeseuon gwall a'ch cofnodion fel y gellir cael diagnosis ar fethiannau. Mewn systemau diogelwch-dyngedfennol a dinesydd-dyngedfennol, methwch i mewn i gyflwr diogel, hysbys yn hytrach na pharhau mewn un llygredig. Rhowch cymaint o feddwl i lwybr y gwall ag i'r llwybr hapus, oherwydd mewn cynhyrchu llwybr y gwall yw lle mae ymddiriedaeth yn cael ei hennill neu ei cholli.

### Adeiladwch ansawdd i mewn yn ystod adeiladu

Adeiladir ansawdd i mewn, ni chaiff ei archwilio i mewn wedyn. Ysgrifennwch brofion uned ochr yn ochr â'r cod, rhedwch [ddadansoddiad statig](https://en.wikipedia.org/wiki/Static_program_analysis) a chysonwyr yn barhaus, a chadwch ffwythiannau'n ddigon bach i resymu amdanynt. Defnyddiwch enwau a strwythur hunan-esboniadol fel y gall eich sylwadau esbonio pam, nid beth. [Ailffactorwch](https://en.wikipedia.org/wiki/Code_refactoring) wrth fynd i gadw'r cod yn drigadwy. Mae adolygiad cod (pennod 2.5) yn wargefn dynol, ond mae angen i'r rhan fwyaf o'r ansawdd fod yno cyn i'r adolygiad hyd yn oed ddechrau.

### Dewiswch a safonwch offer adeiladu

Safonwch y gadwyn offer (crynhoyddion, systemau adeiladu, fformatwyr, cysonwyr, dadansoddwyr statig, dadfygwyr, rheolwyr dibyniaeth, a ffurfweddiadau IDE) fel bod pob peiriannydd yn gweithio mewn amgylchedd cyson, ailadroddadwy. Weiriwch yr offer hyn i mewn i'r biblinell fel nad yw gwiriadau ansawdd yn ddewisol. Dewch ag offer codio a gynorthwyir gan AI i mewn yn fwriadol, a thriniwch eu hallbwn fel drafft sy'n rhaid iddo basio'r un safonau, adolygiad, a phrofion ag unrhyw god arall.

## Cyfaddawdau: manteision ac anfanteision

| Arfer | Manteision | Anfanteision |
|---|---|---|
| Lleihau cymhlethdod ymosodol | Darllenadwy, newidiadwy, cyfradd diffyg isel | Gall deimlo'n araf; peryglon gor-haniaethu os cymhwysir yn anghywir |
| Gwiriadau amddiffynnol helaeth | Yn dal cyflyrau gwael yn gynnar, ffiniau cadarn | Yn llanast y rhesymeg; gall guddio gwallau gwirioneddol os gorwneir |
| Cadarnhadiadau ar gyfer priodweddau digyfnewid | Yn dogfennu ac yn gorfodi tybiaethau | Wedi'u hanalluogi mewn rhai adeiladau cynhyrchu; nid trin gwallau |
| Ailddefnyddio trwm o lyfrgelloedd | Llai o god i'w berchen; cyflenwi cyflymach | Risg dibyniaeth, cyplu, amlygiad cadwyn-gyflenwi |
| Safonau a chysoni llym | Sylfaen god unffurf, ffrithiant-isel | Gosod ymlaen llaw; gall deimlo'n anhyblyg i unigolion |
| Adeiladu ar gyfer profadwyedd | Cod y gellir ei wirio, ei newid | Gall ychwanegu anuniongyrchedd y bydd rhai'n ei weld fel seremoni |

Y cyfaddawd canolog mewn adeiladu yw cyflymder tymor-byr yn erbyn newidioldeb tymor-hir. Mae torri corneli (hepgor trin gwallau, goddef cymhlethdod, anwybyddu safonau) yn teimlo'n gyflymach ar y pryd, ac mae bron bob amser yn ddrutach dros oes y system. Y methiant gwrthgyferbyniol yw gor-beirianneg: gormod o amddiffynoldeb, haniaethu dyfaliedig, a chyffredinoledd nad oes ei angen ar neb. Mae adeiladu medrus yn byw yn y canol: mor syml â phosibl, mor amddiffynnol ag y mae'r ffiniau'n ei fynnu, a dim mwy.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Beth yw ein diffiniad cyffredin, pendant o "rhy gymhleth," a lle rydym yn ei orfodi cyn uno?** "Lleihau cymhlethdod" yw disgyblaeth ganolog adeiladu, ond fel slogan mae'n colli pob dadl i derfyn amser. Ar dîm mawr lle mae cannoedd o bobl yn ysgrifennu i mewn i un sylfaen god, mae'n rhaid i gymhlethdod fod yn fesuradwy, felly cytunwch ar signalau y gwnewch chi wir weithredu arnynt: hyd ffwythiant, dyfnder nythu, cymhlethdod cyclomatig, a nifer y pethau y mae'n rhaid i ddarllenydd eu dal yn eu pen i ddeall un newid. Dewch â'ch trosedd waethaf i'r cyfarfod a gofynnwch a fyddai eich adolygiad cyfredol wedi ei ddal. Dylai'r ateb droi'n giât biblinell neu'n eitem rhestr wirio adolygu, oherwydd mae trothwy a orfodir gan offeryn yn werth mwy nag egwyddor a orfodir gan ewyllys, ac mae'n arbed eich cyflogai nesaf rhag y cynyddiad araf o god na all neb ei gyffwrdd yn ddiogel.

2. **Yn ein cynhyrchu, a yw ein llwybrau gwall yn ymddwyn fel y gwnaethom eu dylunio, a phryd wnaethom ddiwethaf ymarfer un yn fwriadol?** Mae cyngor adeiladu'n dweud rhowch cymaint o feddwl i lwybr y gwall ag i'r llwybr hapus, eto llwybr y gwall fel arfer yw'r cod lleiaf profedig sydd gennych, ac mewn system ddinesydd-dyngedfennol neu ddiogelwch-dyngedfennol dyma lle mae ymddiriedaeth yn cael ei hennill neu ei cholli. Mae eithriad a atalwyd neu god dychwelyd a anwybyddwyd yn troi'n ddiffyg dirgel wythnosau'n ddiweddarach, ac mae "methu i mewn i gyflwr diogel" yn addewid na allwch ei chadw os na wnaethoch chi erioed ei wylio'n digwydd. Dewch â'ch hanes digwyddiadau: faint o doriadau gwasanaeth blaenorol a olrheiniwyd yn ôl at wall a lyncwyd neu lwybr adfer heb ei brofi? Y gweithred yw profi methiant yn fwriadol (chwistrellu'r cerdyn a wrthodwyd, yr amser allan, y mewnbwn wedi'i gamffurfio) a mynnu bod pob gwall yn cael ei drin, ei gofnodi â chyd-destun, neu ei ledaenu, byth wedi'i ollwng yn dawel.

3. **Pa rannau o'n sylfaen god sy'n anodd eu profi, a beth mae'r anhawster hwnnw'n ei ddweud wrthym am y dyluniad?** Mae cod sy'n gwrthsefyll profi bron bob amser yn god sy'n cuddio cyflwr, yn cyplu i'r dibyniaethau anghywir, neu'n gwneud gormod, felly mae profadwyedd yn signal dylunio, nid ôl-ystyriaeth sicrwydd ansawdd. Ar system fenter hirhoedlog mae hyn yn bwysig oherwydd bod y modylau sy'n boenus i'w profi heddiw yn rhai y bydd dieithryn yn ofni eu newid mewn pum mlynedd. Dewch â'r dosbarth neu'r gwasanaeth y mae eich tîm yn ofni ysgrifennu profion ar ei gyfer a gofynnwch pam: a yw'r cyflwr wedi'i guddio, a yw'r dibyniaethau'n amhosibl eu disodli, a yw'r ffwythiant yn gwneud tair swydd? Dylai'r ateb yrru ailffactora tuag at ffwythiannau pur, dibyniaethau amlwg, ac unedau bach un-diben, oherwydd mae gwneud y cod yn wirioadwy yr un gwaith â'i wneud yn ddealladwy ac yn rhad i'w newid.

4. **Pryd rydym yn ailddefnyddio llyfrgell allanol yn erbyn adeiladu'r gallu ein hunain, a phwy sy'n berchen ar y risg cadwyn-gyflenwi rydym yn ei chymryd ymlaen?** Mae estyn am lyfrgell ddibynadwy'n gyflymach nag ailddyfeisio rhesymeg sylfaenol, eto mae pob dibyniaeth a ychwanegwch yn god nad ydych yn ei reoli, na allwch ei archwilio'n hawdd, ac y mae'n rhaid i chi ei glytio'r diwrnod y caiff ei gyfaddawdu. Ar dîm mawr y perygl yw bod cant o beirianwyr pob un yn tynnu eu dibyniaethau trosiannol eu hunain nes na all neb ddweud beth mae'r sylfaen god yn ei redeg mewn gwirionedd. Dewch â'ch arolwg dibyniaeth a gofynnwch dri pheth pendant: faint o lyfrgelloedd sydd heb eu cynnal, faint sy'n cario gwendidau hysbys, a faint sy'n lapio rhesymeg ddigon syml i'w berchen yn llwyr. Mae'r ystyriaeth wrthgyferbyniol yn wirioneddol, oherwydd mae ysgrifennu eich cryptograffeg neu drin dyddiad eich hun bron bob amser yn waeth na llyfrgell brofedig mewn brwydr, felly'r nod yw polisi ailddefnyddio bwriadol yn hytrach nag osgoi cyffredinol. Mewn lleoliadau mentrau a llywodraethol, ychwanegwch yr ongl gaffael a chydymffurfiaeth trwydded, gan y gall dibyniaeth heb ei gwirio gario trwydded sy'n anghydnaws â'ch rhwymedigaethau neu darddiad na fydd unrhyw archwiliwr yn ei dderbyn.

5. **Sut rydym yn dal cod a gynhyrchwyd gan AI i'r un safonau adeiladu â chod a ysgrifennwyd gan bobl, ac a allwn ni ddweud y ddau ar wahân pan fo'n bwysig?** Mae cynorthwywyr codio AI yn cynhyrchu drafftiau credadwy'n gyflym, a'r demtasiwn yw trin eu hallbwn fel gorffenedig oherwydd ei fod yn crynhoi ac yn edrych yn idiomatig. Rheol y bennod yw bod cod a gynhyrchwyd yn pasio'r un adolygiad, profion, a safonau ag unrhyw beth arall, ac mae'n rhaid i dîm mawr wneud y rheol honno'n weithredol yn hytrach na dyheadol. Dewch ag enghreifftiau o newidiadau a gynorthwywyd gan AI a gyflenwyd yn ddiweddar a gofynnwch a oedd gan bob un brofion, a glirodd ddadansoddiad statig, ac a gafodd ei ddeall yn wirioneddol gan y person a'i cyflwynodd, neu a gafodd ei chwifio drwodd ar ymddiriedaeth. Y pwysau gwrthgyferbyniol yw cyflymder, oherwydd mae'r cynorthwywyr hyn yn wirioneddol gynhyrchiol ac mae arafu pob awgrym i gropian yn taflu'r budd i ffwrdd. Mewn cyd-destunau rheoleiddiedig a llywodraethol, ychwanegwch yr ongl darddiad ac atebolrwydd, oherwydd efallai y bydd yn rhaid i chi dystio pwy sy'n gyfrifol am linell o god ac a yw darn a gynhyrchwyd yn cario cwestiwn trwyddedu neu hawlfraint na allwch ei ateb.

6. **A yw ein cadwyn offer adeiladu wir wedi'i safoni a'i gorfodi yn y biblinell, neu a yw unigolion yn dal i weithio mewn setiadau anghydnaws?** Mae cadwyn offer a rennir o fformatiwr, cysonwr, dadansoddwr statig, system adeiladu, a rheolwr dibyniaeth yn gadael i beiriannydd symud yn hyderus ar draws gwasanaethau anghyfarwydd, oherwydd mae'r cod yn darllen fel un llais a'r gwiriadau'n union yr un fath ym mhobman. Pan fydd yn drifftio, mae pob tîm yn ailddyfeisio ei ffurfweddiad ei hun, treulir amser adolygu'n dadlau am arddull, ac mae diffygion y byddai dadansoddwr un tîm wedi'u dal yn llithro drwodd ar un tîm arall. Dewch â'r rhestr o ystorfeydd nad ydynt yn rhedeg y gwiriadau safonol ar bob ymrwymiad a gofynnwch pam wnaeth pob un ddewis peidio. Y tyndra yw y gall un gosodiad gorfodol deimlo'n anhyblyg i dimau ag anghenion wir wahanol, felly penderfynwch ble mae unffurfiaeth yn werth y ffrithiant a lle mae eithriad dogfennedig yn iawn. I fenter fawr neu gorff cyhoeddus, clymwch hyn wrth ailadroddadwyedd ac archwiliad, oherwydd mae adeiladu na allwch ei ailadrodd beit wrth beit o gadwyn offer reoledig yn un na allwch ei amddiffyn i asesydd flynyddoedd yn ddiweddarach.

## Trwy lens sector

**Cwmni newydd.** Cyflymder sy'n ennill, felly rhowch fformatiwr a chysonwr a rennir yn eu lle o'r diwrnod cyntaf, dilyswch fewnbynnau ar eich un ffin allanol, a chadwch y cod mewnol yn lân yn hytrach nag amddiffynnol ar bob llinell. Hepgorwch haniaethu dyfaliedig a phroses drwm: gyda dau neu dri pheiriannydd mae'r tîm cyfan yn dal y sylfaen god yn eu pennau, a'r perygl gwirioneddol yw cymhlethdod sy'n goroesi'r cof a rennir hwnnw. Dibynnwch ar lyfrgelloedd dibynadwy ar gyfer unrhyw beth sylfaenol fel eich bod yn ysgrifennu cyn lleied o god ag y gallwch ei berchen yn dda.

**Busnes bach.** Heb beiriannydd adeiladu penodedig a chyllideb dynn, ffafriwch gonfensiynau y mae eich offer presennol yn eu gorfodi am ddim: fformatiwr a chysonwr sy'n dod gyda'r iaith, rhagosodiadau synhwyrol, a set fach o reolau y gall pawb eu cofio. Prynwch neu fabwysiadwch lyfrgelloedd wedi'u cynnal yn dda yn hytrach nag adeiladu seilwaith na allwch ei staffio i'w gynnal. Treuliwch eich disgyblaeth gyfyngedig ar y ddau beth sy'n brifo fwyaf pan esgeulusir hwy, dilysu mewnbwn ar y ffin ac byth llyncu gwall yn dawel.

**Menter.** Gyda channoedd o beirianwyr yn ysgrifennu i mewn i god a rennir, y flaenoriaeth yw unffurfiaeth a gorfodaeth: cadwyn offer safonol wedi'i weirio i mewn i'r biblinell, giatiau dadansoddiad statig, a rheolau dilysu ffin a gymhwysir ym mhobman fel bod pobl yn symud yn hyderus rhwng gwasanaethau. Rheolwch risg dibyniaeth a chadwyn-gyflenwi fel proses lywodraethedig yn hytrach nag byrfyfyrio fesul tîm, a defnyddiwch gadarnhadiadau i amgodio priodweddau digyfnewid parth sy'n rhaid dal ar draws pob tîm. Triniwch safonau adeiladu fel y swbstrad sy'n cadw sylfaen god yn drigadwy ar draws degawdau a throsiant staff.

**Llywodraeth.** Mae systemau hirhoedlog, dinesydd-dyngedfennol yn gwneud adeiladu disgybledig yn fater sicrwydd ac atebolrwydd. Ynyswch reolau anwadal fel deddfwriaeth y tu ôl i ryngwynebau sefydlog fel bod newid yn aros yn lleol ac yn olrheiniadwy at ofynion, methwch i mewn i gyflyrau diogel, hysbys yn hytrach na pharhau mewn un llygredig, a chyflenwch bob modwl â phrofion sy'n dyblu fel tystiolaeth archwilio. Mae rhwymedigaethau caffael a thryloywder yn golygu bod yn rhaid i'ch cadwyn offer, dibyniaethau, a thrin gwallau gael eu dogfennu'n ddigon da fel y gall gwas sifil sy'n cyrraedd flynyddoedd yn ddiweddarach, neu archwiliwr allanol, wirio bod y cod yn gywir.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd tri pheiriannydd yn weirio fformatiwr a chysonwr a rennir o'r diwrnod cyntaf ac yn eu rhedeg ar bob ymrwymiad, fel bod y sylfaen god yn darllen fel un llais hyd yn oed wrth iddynt ychwanegu contractwyr. Maent yn dilysu mewnbynnau ar eu ffin API ac yn trin popeth o'r tu allan fel gelyniaethus, ond yn cadw'r rhesymeg fewnol yn lân yn hytrach na'i mygu mewn gwiriadau dianghenraid. Pan fydd bachyn gwe taliad yn dechrau methu, mae'r ateb yn gyflym oherwydd na chafodd unrhyw eithriad ei lyncu'n dawel erioed ac mae'r neges wall yn cario digon o gyd-destun i bwyntio'n syth at yr achos. Cymerodd y gosodiad cyfan brynhawn ac arbedodd iddynt y cynyddiad araf o gymhlethdod a fyddai wedi gwneud wythnos gyntaf eu cyflogai nesaf yn druenus.

**Menter.** Mae cwmni taliadau byd-eang yn gorfodi cadwyn offer a rennir ar draws cannoedd o beirianwyr: fformatio a chysoni awtomataidd ar bob ymrwymiad, giatiau dadansoddiad statig yn y biblinell, a rheol bod pob mewnbwn allanol yn cael ei ddilysu ar ffiniau gwasanaeth. Mae rhesymeg parth yn defnyddio cadarnhadiadau i orfodi priodweddau digyfnewid megis "mae cofnod cyfrifiadau bob amser yn cydbwyso," tra bod amodau adeg-rhedeg fel cerdyn a wrthodwyd yn cael eu trin fel canlyniadau amlwg, wedi'u cofnodi. Am fod y safonau'n unffurf ac na chaiff gwallau eu llyncu'n dawel byth, mae peirianwyr yn symud yn hyderus ar draws gwasanaethau anghyfarwydd, a gellir cael diagnosis ar ddigwyddiadau cynhyrchu'n syth o'r cofnodion.

**Llywodraeth.** Mae asiantaeth dreth genedlaethol yn adeiladu system asesu hirhoedlog y disgwylir iddi redeg am ddegawdau dan ddeddfwriaeth sy'n newid. Mae adeiladu'n ynysu pob rheol dreth y tu ôl i ryngwyneb sefydlog, fel bod newidiadau deddfwriaethol blynyddol yn aros yn lleol ac yn olrheiniadwy at ofynion (pennod 2.8). Mae dilysiad amddiffynnol yn gwarchod pob mewnbwn sy'n wynebu dinasyddion. Mae llwybrau gwall yn methu i mewn i gyflwr diogel nad yw byth yn cyhoeddi asesiad anghywir yn dawel. Mae pob modwl yn cael ei gyflenwi â phrofion uned fel tystiolaeth archwilio. Am fod yr adeiladu wedi'i safoni a'i ddogfennu'n dda, gall gweision sifil newydd gynnal yn ddiogel god a ysgrifennwyd gan ragflaenwyr a adawodd amser maith yn ôl.

## Achos busnes: cymhellion, ROI, a TCO

Y dychweliad ar adeiladu disgybledig yw'r gallu parhaol i newid meddalwedd yn rhad ac yn ddiogel, a dyna lle mae'r rhan fwyaf o gyfanswm cost perchnogaeth system yn cael ei benderfynu. Mae astudiaethau economeg meddalwedd yn dangos yn gyson mai cynnal yw'r rhan fwyaf o gost oes system, a bod cost cynnal yn cael ei dominyddu gan pa mor ddealladwy a newidiadwy yw'r cod. Mae lleihau cymhlethdod, trin gwallau'n amlwg, a dilyn safonau'n gostwng yn uniongyrchol gost pob newid yn y dyfodol a phob digwyddiad cynhyrchu.

Mae'r gost i'w fabwysiadu'n gymedrol ac yn bennaf ymlaen llaw: gosod y safonau, weirio'r cysonwyr a'r dadansoddwyr, ac adeiladu'r arferiad o ysgrifennu cod gwirioadwy, amddiffynnol. Mae cost esgeulustod, ar y llaw arall, yn cyfansymio. Mae cymhlethdod yn cronni i mewn i god sy'n araf i'w newid ac yn beryglus i'w gyffwrdd. Mae gwallau tawel yn troi'n ddigwyddiadau cynhyrchu drud. Mae arddull anghyson yn lluosi ymdrech pob adolygiad a phob sefydlu. I wneud yr achos i arweinyddiaeth, cysylltwch ansawdd adeiladu â chyfradd methiant newid, amser cyfartalog i adfer, cyfradd dianc diffygion, ac amser sefydlu, mae pob un ohonynt yn cael eu gwella'n uniongyrchol gan ddisgyblaeth adeiladu.

## Gwrthbatrymau a pheryglon

- **Cripian cymhlethdod:** cronni cod clyfar, nythog-ddwfn, neu wasgarog nes nad oes neb yn ei ddeall.
- **Llyncu gwallau'n dawel:** blociau dal gwag a chodau dychwelyd wedi'u hanwybyddu sy'n troi methiannau'n ddirgelion y dyfodol.
- **Gor-wneud rhaglennu amddiffynnol:** gwiriadau dianghenraid ym mhobman sy'n claddu'r rhesymeg ac yn cuddio diffygion gwirioneddol.
- **Drysu cadarnhadiadau â thrin gwallau:** defnyddio cadarnhadiadau ar gyfer amodau adeg-rhedeg, neu eithriadau ar gyfer priodweddau digyfnewid rhaglennydd.
- **Adeiladu copïo-gludo:** dyblygu rhesymeg yn hytrach nag ailddefnyddio, fel bod yn rhaid gwneud cywiriadau mewn llawer o leoedd.
- **Cyffredinoledd ddyfaliedig:** adeiladu haniaethiadau a ffurfweddadwyedd ar gyfer anghenion nad ydynt byth yn cyrraedd.
- **Anwybyddu safonau:** pob peiriannydd yn codio yn ei ffordd ei hun, gan luosi baich gwybyddol ar draws y sylfaen god.
- **Adeiladu heb ei brofi:** ysgrifennu cod heb brofion cyfeiliornol, gan ohirio gwiriad i gyfnod nad yw byth yn dod.

## Model aeddfedrwydd

- **Lefel 1 (Cychwyn):** Mae adeiladu'n ad hoc ac yn adweithiol; mae cymhlethdod a thrin gwallau'n amrywio yn ôl unigolyn; ychydig o safonau sy'n bodoli, ac mae methiannau tawel yn gyffredin.
- **Lefel 2 (Datblygu):** Mae safonau codio, fformatwyr, a chysonwyr yn bodoli, a disgwylir trin gwallau sylfaenol a phrofi unedau, ond mae'r arfer yn anghyson ac mae pob tîm yn ei gymhwyso'n wahanol.
- **Lefel 3 (Safoni):** Mae lleihau cymhlethdod, dilysu ffin, trin gwallau'n amlwg, a phrofadwyedd wedi'u dogfennu a'u gorfodi ar draws y sefydliad, yn y biblinell ac mewn adolygiad, fel bod y sylfaen god gyfan yn darllen fel pe bai un awdur gofalus wedi'i hysgrifennu.
- **Lefel 4 (Rheoli):** Mesurir ansawdd adeiladu yn erbyn llinellau sylfaen; mae'r tîm yn olrhain cymhlethdod cyclomatig, cyfradd dianc diffygion, cyfradd methiant newid, sylw profion llwybr-gwall, a chanfyddiadau adolygiad cod, ac yn gweithredu ar y tueddiadau yn hytrach na barn.
- **Lefel 5 (Cerddorfa):** Mae adeiladu'n cael ei wella'n barhaus a'i integreiddio ar draws y sefydliad; mae patrymau amddiffynnol, safonau, a metrigau'n bwydo'n ôl i mewn i ailffactora ac offer; mae offer a gynorthwyir gan AI'n rhedeg dan yr un giatiau ansawdd, ac mae'r arfer yn addasu wrth i ieithoedd, rheoliadau, a risgiau newid.

## Syniadau ar gyfer trafodaeth

- Ble mae cymhlethdod damweiniol yn cronni fwyaf yn eich sylfaen god, a pha arferion adeiladu sy'n ei greu?
- Beth yw rheol wirioneddol eich tîm ar gyfer ble i ddilysu mewnbynnau a ble i ymddiried ynddynt?
- A yw eich peirianwyr yn gwahaniaethu rhwng cadarnhadiadau a thrin gwallau, ac a yw'r gwahaniaeth hwnnw'n gyson?
- Faint o'ch ansawdd sy'n cael ei adeiladu i mewn yn ystod adeiladu yn erbyn ei ddal yn ddiweddarach mewn adolygiad neu brofi?
- Sut ydych chi'n penderfynu pryd i ailddefnyddio llyfrgell yn erbyn adeiladu, o ystyried risg cadwyn-gyflenwi?
- Sut ddylai cod a gynhyrchwyd gan AI gael ei ddal i'r un safonau adeiladu â chod a ysgrifennwyd gan bobl?

## Prif negeseuon

- Adeiladu yw lle mae dyluniad yn dod yn god y gellir ei gynnal; lleihau cymhlethdod yw ei ddisgyblaeth ganolog.
- Adeiladwch ar gyfer newid a gwiriad: mae cod y gellir ei brofi, y gellir ei newid yn god y gellir ei ddeall.
- Amddiffynnwch ar ffiniau ymddiriedaeth, ymddiriedwch oddi mewn iddynt, a byth llyncu gwallau'n dawel.
- Defnyddiwch gadarnhadiadau ar gyfer priodweddau digyfnewid a thrin gwallau ar gyfer amodau adeg-rhedeg disgwyliedig; peidiwch â'u drysu.
- Safonwch offer ac arddull, ailddefnyddiwch yn fwriadol, ac adeiladwch ansawdd i mewn yn hytrach na'i archwilio wedyn.

## Cyfeiriadau a darllen pellach

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, maes gwybodaeth Adeiladu Meddalwedd
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt a David Thomas, *The Pragmatic Programmer*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code*
- John Ousterhout, *A Philosophy of Software Design*
