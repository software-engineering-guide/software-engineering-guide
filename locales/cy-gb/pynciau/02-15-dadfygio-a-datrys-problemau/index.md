# 2.15 Dadfygio a datrys problemau

## Trosolwg a chymhelliant

Dadfygio yw'r gwaith disgybledig o ganfod pam mae system yn gwneud rhywbeth na ddylai, a datrys problemau yw'r un sgil wedi'i throi ar system gynhyrchu sy'n rhedeg dan bwysau amser. Mae'r ddau'n [ddull gwyddonol](https://en.wikipedia.org/wiki/Scientific_method) wedi'i gymhwyso i ddiffygion: rydych chi'n arsylwi ymddygiad syndod, yn ffurfio damcaniaeth am ei achos, yn dylunio arbrawf a fyddai'n cadarnhau neu'n gwrthbrofi hynny, ac yn gadael i'r dystiolaeth, nid eich greddf, ddweud wrthych beth i'w newid. Wedi'i wneud fel hyn, mae dadfygio'n sgil beirianyddol y gellir ei ddysgu a'i haddysgu. Wedi'i wneud fel llên gwerin, mae'n dod yn ofergoeliaeth: newid llinellau ar hap, ailgychwyn gweinyddion, a gobeithio.

I dîm mawr, mae'r gwahaniaeth yn ddrud. Gall un diffyg caled dynnu peirianwyr o sawl gwasanaeth i mewn, treulio oriau ar-alwad, ac arafu rhyddhad. Pan fydd pob person yn dadfygio yn ôl greddf, nid yw'r ymdrech honno'n cyfansymu, oherwydd ni all neb atgynhyrchu na esbonio'r hyn a geisiodd unrhyw un arall. Pan fydd y tîm yn rhannu dull (atgynhyrchu yn gyntaf, ynysu trwy chwilio, dal y nam mewn prawf sy'n methu, yna trwsio), mae'r un ymdrech yn troi'n broses ailadroddadwy a chyfres atchweliad sy'n tyfu. Mae dadfygio'n cysylltu'n dynn â strategaeth brofi Pennod 2.4, ag ansawdd meddalwedd Pennod 2.11, ac ag arferion adeiladu Pennod 2.9 sy'n gwneud cod yn ddiagnosadwy yn y lle cyntaf.

Mewn lleoliadau menter a llywodraeth, mae'r risgiau'n codi. Mae diffygion menter yn croesi ffiniau gwasanaeth a thîm, felly'n anaml y bydd y person sy'n gweld y symptom yn berchen ar yr achos. Mae systemau llywodraeth yn ychwanegu cyfyngiadau nad yw'r rhan fwyaf o beirianwyr byth yn eu cyfarfod: amgylcheddau bwlch-aer neu gyfyngedig lle na allwch gysylltu dadfygiwr â chynhyrchu, adeiladau atgynyrchadwy y mae'n rhaid eu diagnosio o arteffactau, a llwybrau archwilio y mae'n rhaid iddynt gofnodi beth a newidioch a pham. Yn y tri, yr un yw'r nod: disodli dyfalu â thystiolaeth.

## Egwyddorion allweddol

- **Atgynhyrchwch cyn i chi ddamcaniaethu.** Mae nam na allwch ei sbarduno ar alw yn si, nid yn ddiffyg.
- **Mae dadfygio'n brofi damcaniaeth.** Nodwch beth rydych chi'n ei gredu, yna dyluniwch yr arbrawf rhataf a allai eich profi'n anghywir.
- **Darllenwch y gwall a'r olrhaid pentwr yn gyntaf.** Mae'r system fel arfer yn dweud wrthych ble y torrodd cyn i chi newid llinell.
- **Chwiliwch ofod y broblem, peidiwch â'i sganio.** Haneriwch y rhanbarth amheus ar bob cam yn hytrach na darllen o'r brig i'r gwaelod.
- **Lleihau i'r isafswm.** Diosgwch yr achos i lawr nes mai dim ond y sbardun hanfodol sy'n weddill.
- **Un newid ar y tro.** Mae golygiadau gwn-magnel yn dinistrio'r dystiolaeth a fyddai wedi dweud wrthych pa newid oedd yn bwysig.
- **Daliwch y nam mewn prawf sy'n methu cyn i chi ei drwsio.** Dim ond pan fydd y prawf hwnnw'n troi'n wyrdd ac yn aros yn wyrdd y profir y trwsiad.
- **Dewch o hyd i'r achos gwraidd, nid y symptom agosaf.** Mae clwt sy'n cuddio'r symptom yn gadael i'r diffyg ddychwelyd.

## Argymhellion

### Atgynhyrchwch y diffyg yn ddibynadwy cyn newid unrhyw beth

Eich gwaith cyntaf yw atgynhyrchiad dibynadwy: cyfres o gamau neu achos wedi'i awtomeiddio sy'n sbarduno'r nam ar alw. Heboch ef ni allwch ddweud trwsiad go iawn oddi wrth gyd-ddigwyddiad, oherwydd gall y symptom ddod a mynd am resymau na wnaethoch chi eu rheoli erioed. Peniwch i lawr y mewnbynnau, yr amgylchedd, y fersiynau, a'r amseriad. Os yw'r nam yn ysbeidiol, heliwch am y newidyn cudd sy'n gwneud iddo ymddangos (cofnod data penodol, ffin cloc, cais cydamserol) nes bod yr atgynhyrchiad yn ddibynadwy. Atgynhyrchiad dibynadwy yw'r arteffact mwyaf gwerthfawr un mewn dadfygio, oherwydd bod popeth wedi hynny'n dod yn fesuradwy.

### Darllenwch y gwall, y logiau, a'r olrhaid pentwr cyn i chi gyffwrdd â chod

Cyn i chi ffurfio un ddamcaniaeth, darllenwch yr hyn y mae'r system eisoes wedi'i ddweud wrthych. Mae'r [olrhaid pentwr](https://en.wikipedia.org/wiki/Stack_trace) (y cofnod o'r gadwyn alwadau ar adeg y methiant) fel arfer yn enwi'r ffeil, y llinell, a'r dilyniant a fethodd. Mae neges yr eithriad, y llinellau log o'i gwmpas, a'r gwerthoedd yn y cwmpas yn culhau'r chwiliad cyn i chi newid unrhyw beth. Mae peirianwyr yn gwastraffu oriau'n damcaniaethu am achosion y mae'r olrhaid eisoes wedi'u diystyru ar y llinell gyntaf. Triniwch yr allbwn gwall fel y tyst cyntaf, ei ddarllen yn ofalus ac yn llawn, a dim ond wedyn penderfynu beth i'w ymchwilio.

### Ynyswch trwy chwiliad deuaidd o ofod y broblem

Peidiwch â sganio'r cod o'r brig i'r gwaelod. Chwiliwch ef. Defnyddiwch [chwiliad deuaidd](https://en.wikipedia.org/wiki/Binary_search_algorithm): dewch o hyd i bwynt lle mae'r cyflwr yn dal yn dda a phwynt lle mae eisoes yn ddrwg, yna gwiriwch y canolbwynt, ac ailadroddwch, gan haneru'r rhanbarth amheus bob tro. Mae hyn yn troi chwiliad mil o linellau'n ddeg cwestiwn. Pan ymddangosodd yr atchweliad dros ystod o gyflwyniadau, cymhwyswch yr un syniad i hanes gyda deubisiad: mae `git bisect` yn cerdded yr ystod cyflwyniadau, a byddwch yn marcio pob adolygiad yn dda neu'n ddrwg nes ei fod yn enwi'r union newid a gyflwynodd y diffyg. Awtomeiddiwch y prawf da-neu-ddrwg a bydd y deubisiad yn rhedeg ei hun.

### Lleihewch i enghraifft atgynyrchadwy leiafswm

Unwaith y gallwch sbarduno'r nam, ei grebachu. Mae [enghraifft atgynyrchadwy leiafswm](https://en.wikipedia.org/wiki/Minimal_reproducible_example) yn fewnbwn a llwybr cod lleiaf sy'n dal i fethu: tynnwch ddata, nodweddion, a chamau nes bod unrhyw dynnu pellach yn gwneud i'r nam ddiflannu. Nid gwaith prysur yw lleihau; mae pob elfen rydych chi'n ei dileu'n achos rydych chi wedi'i ddiystyru, felly mae'r achos lleiafswm yn aml yn pwyntio'n syth at y diffyg. Pan fydd y mewnbwn yn fawr neu wedi'i strwythuro, awtomeiddiwch y crebachu gyda [dadfygio delta](https://en.wikipedia.org/wiki/Delta_debugging), algorithm sy'n tynnu talpiau o fewnbwn methedig yn systematig i ddod o hyd i'r is-set fethedig leiafswm. Mae atgynhyrchiad bach, hunangynhwysol hefyd yn adroddiad nam gorau posibl i'w roi i dîm arall.

### Offerynnwch â logiau, yna defnyddiwch ddadfygiwr rhyngweithiol

Paru'r teclyn â'r nam. Mae logio ac offerynnu wedi'i dargedu orau pan fydd angen i chi weld ymddygiad dros amser, ar draws prosesau, neu mewn amgylchedd na allwch ei atal. Mae dadfygiwr rhyngweithiol, sy'n gadael i chi osod pwyntiau torri, camu llinell wrth linell, ac archwilio cyflwr byw, orau pan allwch redeg y cod yn lleol ac angen gwylio un weithrediad yn agos. Ychwanegwch offerynnu fel arbrawf bwriadol wedi'i glymu wrth ddamcaniaeth, nid fel datganiadau argraffu gwasgaredig, a'i dynnu neu ei ddyrchafu'n logio strwythuredig parhaol unwaith y bydd y nam wedi'i ddatrys. Mewn cynhyrchu, pwyswch ar ddadfygio wedi'i yrru gan arsylladwyedd: mae digwyddiadau cardinaledd uchel ac olrhain dosbarthedig (Pennod 9.2) yn gadael i chi ddilyn un cais ar draws sawl gwasanaeth, sydd yn aml yr unig ffordd i ddadfygio system ddosbarthedig na allwch gysylltu dadfygiwr â hi.

### Ysgrifennwch brawf sy'n methu sy'n dal y nam cyn i chi ei drwsio

Cyn i chi ysgrifennu'r trwsiad, ysgrifennwch brawf sy'n methu oherwydd y nam. Mae hyn yn gwneud tri pheth ar unwaith: mae'n profi eich bod chi mewn gwirionedd yn deall yr achos, mae'n diffinio'n union beth mae "wedi'i drwsio" yn ei olygu, ac mae'n dod yn warchodwr parhaol. Yna gwnewch y trwsiad a gwylio'r prawf yn troi'n wyrdd. Mae'r prawf hwnnw bellach yn ymuno â'ch cyfres fel gwarchodwr [profi atchweliad](https://en.wikipedia.org/wiki/Regression_testing), fel na all yr un diffyg ddychwelyd heb sylw. Mae'r arfer hwn yn cysylltu dadfygio'n uniongyrchol â'ch strategaeth brofi (Pennod 2.4): mae pob nam caled a ddatryswch yn gadael y gyfres yn gryfach nag y'i cafwyd, ac mae prawf ansefydlog yn cael yr un driniaeth (atgynhyrchu'r ansicrwydd, yna gwarchod yn ei erbyn) yn hytrach nag anodiad ailgynnig.

### Dewch o hyd i'r achos gwraidd, a chadwch y dadansoddiad yn ddi-fai

Nid yw trwsio'r symptom yn drwsio'r nam. Olrheiniwch y methiant yn ôl i'w wir darddiad, gan ofyn pam ar bob haen nes i chi gyrraedd achos y gallwch ei dynnu yn hytrach na'i fasgio. Ar gyfer diffygion a gyrhaeddodd gynhyrchu, cynhaliwch ddadansoddiad achos gwraidd di-fai fel rhan o reoli digwyddiadau (Pennod 9.3): canolbwyntiwch ar amodau'r system a'r broses a adawodd i'r nam gael ei anfon a goroesi, byth ar yr unigolyn a ysgrifennodd y llinell. Mae bai'n gyrru gwybodaeth dan ddaear, ac mae dadfygio'n rhedeg ar wybodaeth. Yr allbwn yw trwsiad a newid i sut mae'r dosbarth o ddiffyg yn cael ei ddal yn gynharach y tro nesaf, y ddau.

## Cyfaddawdau: manteision ac anfanteision

| Dull | Manteision | Anfanteision |
|---|---|---|
| Logio ac offerynnu | Yn gweithio mewn cynhyrchu a systemau dosbarthedig; yn dal ymddygiad dros amser | Sŵn, cost, a lledaeniad logiau; gall aflonyddu ar namau amseru |
| Dadfygiwr rhyngweithiol | Archwiliad cyflwr byw, manwl gywir; cyflym ar gyfer namau lleol | Diwerth mewn cynhyrchu cyfyngedig neu fwlch-aer; gall guddio namau cydamseroldeb |
| Disgyblaeth atgynhyrchu-yn-gyntaf | Yn troi dyfalu'n fesuriad; yn galluogi prawf sy'n methu | Araf ar y dechrau; mae rhai namau'n wirioneddol anodd eu sbarduno |
| Chwiliad deuaidd a deubisiad | Ynysu cyflym, hyd yn oed mewn cod anghyfarwydd | Angen prawf da-neu-ddrwg dibynadwy; anodd pan fydd namau'n rhyngweithio |
| Lleihau trwy ddadfygio delta | Yn crebachu mewnbynnau enfawr yn awtomatig i'r sbardun | Cost sefydlu; yn tybio bod y methiant yn benderfynol |
| Trwsio'r symptom nawr | Yn adfer gwasanaeth yn gyflym dan bwysau | Yn gadael i'r achos gwraidd ddychwelyd; yn cronni dyled |

Y tensiwn canolog yw cyflymder yn erbyn sicrwydd. Dan ddigwyddiad cynhyrchu efallai y bydd angen i chi atal y gwaedu'n gyntaf (ail-rolio neu glwt symptom) i adfer gwasanaeth, ac mae hynny'n gyfreithlon. Y camgymeriad yw stopio yno. Datryswch y tensiwn trwy wahanu'r ddau waith: lliniaru'n gyflym i amddiffyn defnyddwyr, yna atgynhyrchu, dod o hyd i'r achos gwraidd, ac ychwanegu'r gwarchodwr atchweliad cyn i chi ystyried y diffyg ar gau. Mae trwsiad symptom heb ddilyniant yn nam rydych chi wedi cytuno i'w gyfarfod eto.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Pan fydd rhywun yn taro nam caled, beth yw'r peth cyntaf maen nhw'n ei wneud, ac ai atgynhyrchu neu ddyfalu ydyw?** Mae'r ateb gonest yn datgelu a oes gan eich tîm ddull a rennir neu ystafell yn llawn llên gwerin breifat. Gofynnwch i bobl adrodd eu diffyg anodd diwethaf yn uchel: a gawsant atgynhyrchiad dibynadwy yn gyntaf, neu a ddechreuon nhw newid cod ac ailgychwyn pethau? Gall tîm sy'n atgynhyrchu yn gyntaf drosglwyddo nam rhwng pobl, oherwydd bod yr atgynhyrchiad yn teithio; ni all tîm sy'n dyfalu wneud hynny, oherwydd bod pob ymgais yn anailadroddadwy. Mae hyn yn bwysicach wrth i'r tîm dyfu, gan fod y person sy'n gweld symptom yn gynyddol nid y person a all ei drwsio. Os yw'r arfer diofyn yn ddyfalu, cytunwch ar atgynhyrchu-yn-gyntaf fel norm a gwnewch atgynhyrchiad glân yn bris mynediad i docyn nam.

2. **A yw'r namau rydym yn eu trwsio'n dychwelyd, ac a fyddem yn gwybod pe baent yn gwneud hynny?** Mae diffyg sy'n dychwelyd yn ddiffyg na chafodd ei achos gwraidd erioed ei dynnu ac na chafodd ei drwsiad erioed ei warchod gan brawf. Tynnwch eich chwarter diwethaf o ddigwyddiadau a thocynnau a ailagorwyd a chyfrwch faint oedd yn ailadroddiadau neu'n gefndryd agos o namau cynharach. Mae pob ailadroddiad yn dystiolaeth bod y tîm wedi clytio symptom, wedi hepgor y prawf sy'n methu, neu wedi stopio'r dadansoddiad achos gwraidd yn rhy fuan. Y trwsiad yw rheol: ni chaiff unrhyw nam ei gau nes bod prawf sy'n methu ar yr hen ymddygiad yn pasio ar yr un newydd ac yn ymuno â'r gyfres. Dewch â un nam ailddigwyddol diweddar a gofynnwch pa warchodwr a fyddai wedi'i ddal, oherwydd dyna'r hyn roeddech chi'n ei golli.

3. **A allwn ni ddadfygio ein systemau cynhyrchu o gwbl, o ystyried sut y caniateir i ni gyffwrdd â nhw?** Mewn amgylcheddau menter, ac yn enwedig llywodraeth, yn aml ni allwch gysylltu dadfygiwr, ni allwch atgynhyrchu gyda data go iawn, ac ni allwch newid system sy'n rhedeg heb lwybr archwilio. Os mai'ch unig dechneg ddadfygio yw dadfygiwr rhyngweithiol lleol, rydych chi'n ddall yn union lle mae'r namau anoddaf yn byw. Gofynnwch pa dystiolaeth y mae methiant cynhyrchu mewn gwirionedd yn ei adael ar ôl: logiau strwythuredig, llwybrau olrhain dosbarthedig (Pennod 9.2), dympiau craidd, neu arteffactau adeiladu atgynyrchadwy. Penderfynwch nawr beth sy'n rhaid i chi ei ddal yn ddiofyn fel bod digwyddiad yn y dyfodol yn ddiagnosadwy, oherwydd ni allwch ychwanegu offerynnu at fethiant sydd eisoes wedi digwydd. Mewn lleoliadau rheoledig, cadarnhewch fod yr un llwybr hefyd yn bodloni eich rhwymedigaethau archwilio.

4. **Pan fydd digwyddiad cynhyrchu'n ein gorfodi i atal y gwaedu'n gyflym, sut ydym yn sicrhau bod yr achos gwraidd yn dal i gael ei ddarganfod wedyn?** Dan ddigwyddiad, mae ail-rolio neu glwt symptom yn symudiad cyntaf cywir i amddiffyn defnyddwyr, ond y perygl yw bod y tocyn yn cau'r eiliad y daw'r gwasanaeth yn ôl a bod y diffyg sylfaenol byth yn cael ei ddiagnosio. I dîm mawr dyma lle mae dyled yn cronni'n anweledig, oherwydd bod yr un dosbarth o fethiant yn ailymddangos ar wasanaeth gwahanol gyda pheiriannydd ar-alwad gwahanol fisoedd yn ddiweddarach. Dewch â'ch ychydig ddigwyddiadau difrifoldeb-un diwethaf a gwiriwch bob un: a ddilynodd atgynhyrchiad, dadansoddiad achos gwraidd, a gwarchodwr atchweliad y lliniaru, neu a orffennodd y stori gyda "gwasanaeth wedi'i adfer"? Cytunwch ar reol glir bod digwyddiad wedi'i liniaru'n aros ar agor nes bod yr achos gwraidd wedi'i ddeall a'i warchod, ac enwch pwy sy'n berchen ar y dilyniant hwnnw. Mewn lleoliadau menter a llywodraeth, cysylltwch hyn â'ch proses rheoli digwyddiadau (Pennod 9.3) fel bod yr adolygiad ôl-ddigwyddiad yn gam gofynnol, archwiliadwy yn hytrach na chwrteisi sy'n llithro pan fydd y tân nesaf yn dechrau.

5. **Faint o fethiant y gallwn ni mewn gwirionedd ei ailadeiladu ar ôl y ffaith, a phwy benderfynodd beth rydym yn ei ddal yn ddiofyn?** Ni allwch atodi offerynnu at fethiant sydd eisoes wedi digwydd, felly mae diagnosadwyedd unrhyw ddigwyddiad wedi'i osod ymlaen llaw gan y logiau, y llwybrau olrhain, y metrigau, a'r dympiau a ddewisoch eu hallyrru. Yr ystyriaeth gystadleuol yw cost a sŵn: nid yw digwyddiadau cardinaledd uchel ac olrhain llawn yn rhad ac am ddim, ac mae gor-logio'n claddu'r signal wrth chwyddo storfa ac, mewn cyd-destunau rheoledig, eich amlygiad cadw data. Dewch â digwyddiad diweddar go iawn a gofynnwch pa dystiolaeth a adawodd ar ôl, yna gweithiwch yn ôl i'r hyn y byddech chi wedi dymuno ei ddal a beth fyddai'n ei gostio i'w gadw. Penderfynwch yn fwriadol pa signalau sydd ymlaen yn ddiofyn o'i gymharu â phrofi neu optio i mewn, a chofnodwch y penderfyniad hwnnw fel ei fod yn bolisi, nid yn ddamwain. Ar gyfer system fenter neu lywodraeth, ychwanegwch pwy sy'n atebol am y gyllideb arsylladwyedd honno ac a yw'r llwybr a ddaliwyd hefyd yn bodloni rhwymedigaethau archwilio, preifatrwydd, a phreswyliad data.

6. **A ydym yn trin dadfygio fel sgil a ddysgir, y gellir ei fesur, neu a yw peirianwyr newydd yn ei amsugno trwy osmosis?** Gellir dysgu dadfygio, ac eto nid yw'r rhan fwyaf o dimau byth yn ei addysgu'n benodol, felly mae peirianwyr iau'n etifeddu pa lên gwerin bynnag sydd agosaf atynt, ac mae'r dull atgynhyrchu-yn-gyntaf yn lledaenu'n anwastad neu ddim o gwbl. Y tensiwn yw bod addysgu bwriadol (paru ar namau caled, ysgrifennu canfyddiadau ôl-ddigwyddiad, olrhain metrigau) yn costio amser uwch sydd bob amser yn teimlo ei angen mewn man arall. Dewch â dau rif i'r drafodaeth: eich cyfradd diffyg ailadroddus a'ch amser-i-ddiagnosio, oherwydd os na allwch eu mesur ni allwch ddweud a yw eich dull yn gwella neu'n dirywio. Ystyriwch a yw sefydlu'n cynnwys ymarfer dadfygio go iawn ac a yw canfyddiadau achos gwraidd mewn gwirionedd yn bwydo canfyddiad cynharach. Mewn sefydliad mawr neu gyhoeddus, mae arfer dadfygio wedi'i ddogfennu a'i fesur hefyd yn dod yn dystiolaeth o drylwyredd peirianyddol y mae archwilwyr, rheoleiddwyr, a chyrff goruchwylio'n cynyddol yn disgwyl ei weld.

## Lens sector

**Cwmni newydd.** Gyda llond llaw o beirianwyr a dim slac, eich nod yw gwneud namau'n rhad i'w hatgynhyrchu ac yn amhosibl eu hanghofio, nid adeiladu proses drom. Pwyswch ar `git bisect`, atgynhyrchiad lleol cyflym, ac un prawf sy'n methu i bob nam a drwsir, oherwydd bod yr arfer hwnnw'n costio munudau ac yn eich atal rhag talu eto am yr un diffyg tra rydych chi'n ceisio anfon. Hepgorwch bost-mortemau ffurfiol, ond peidiwch byth â hepgor y prawf atchweliad: dyma'r un arteffact sy'n ddigon bach i'w fforddio bob amser ac yn ddigon gwerthfawr i'w gadw bob amser.

**Busnes bach.** Mae'n debyg nad oes gennych arbenigwr dibynadwyedd neu arsylladwyedd penodedig a chyllideb offer dynn, felly ffafriwch yr hyn y mae eich stac eisoes yn ei roi i chi: olrhaid pentwr darllenadwy, logiau strwythuredig, a'r olrhain sydd wedi'i adeiladu i mewn i'r fframweithiau a'r gwasanaethau a gynhelir rydych chi wedi'u prynu. Pan fyddwch chi'n gwerthuso platfform newydd, pwyswch pa mor ddiagnosadwy y mae'n gwneud methiannau, oherwydd bod teclyn rhad sy'n cuddio beth aeth o'i le'n costio llawer mwy i chi mewn amser dyfalu na'r drwydded a arbedwyd. Mae atgynhyrchu-yn-gyntaf ac un-newid-ar-y-tro yn ddisgyblaethau am ddim sy'n talu ar ei ganfed gyflymaf pan nad oes gan neb oriau i'w sbario.

**Menter.** Mae eich namau caled yn croesi ffiniau gwasanaeth a thîm, felly'n anaml y bydd y person sy'n gweld y symptom yn berchen ar yr achos, ac mae dull a rennir yn bwysicach na sgil unrhyw unigolyn. Safonwch atgynhyrchu-yn-gyntaf, ynysu chwiliad deuaidd, prawf sy'n methu cyn y trwsiad, a phost-mortemau di-fai ar draws timau, a buddsoddwch mewn olrhain dosbarthedig (Pennod 9.2) fel y gellir dilyn un cais ar draws gwasanaethau. Rheolwch ddadfygio fel gallu a fesurir: olrheiniwch gyfradd diffyg ailadroddus ac amser-i-ddiagnosio, a bwydwch ganfyddiadau achos gwraidd yn ôl i ganfyddiad cynharach fel nad yw'r un dosbarth o fethiant yn teithio o amgylch eich map gwasanaeth.

**Llywodraeth.** Mae rheolau caffael, amgylcheddau cyfyngedig, ac atebolrwydd cyhoeddus yn siapio sut y cewch ddadfygio o gwbl. Yn aml ni allwch gysylltu dadfygiwr â chynhyrchu na chopïo data dinasyddion i liniadur, felly dyluniwch ar gyfer diagnosis o'r hyn a ganiateir: adeiladau atgynyrchadwy, cofnodion synthetig mewn amgáead ynysig, a logiau a llwybrau olrhain strwythuredig wedi'u dal yn ddiofyn. Cofnodwch bob cam diagnostig a phob newid yn y llwybr archwilio, a mynnwch fod gwerthwyr yn datgelu digon o delemetreg ac atgynyrchadwyedd adeiladu i chi ymchwilio i fethiannau'n annibynnol yn hytrach na dibynnu ar air y cyflenwr.

## Enghreifftiau

**Cwmni newydd.** Mae tîm o bedwar peiriannydd yn dal i weld talu'n methu ar gyfer cyfran o ddefnyddwyr, ond byth wrth brofi. Yn lle dyfalu, mae un peiriannydd yn dal atgynhyrchiad dibynadwy trwy ailchwarae union bwn cais methedig, yna'n darllen yr olrhaid pentwr roedden nhw wedi bod yn ei anwybyddu, sy'n pwyntio at alwad dosrannu dyddiad. Mae `git bisect` cyflym ar draws cyflwyniadau'r wythnos yn enwi'r newid a newidiodd lyfrgell dyddiad. Maent yn ysgrifennu prawf sy'n methu gyda'r stamp amser troseddol, yn trwsio'r dosrannwr, yn gwylio'r prawf yn troi'n wyrdd, ac yn ei gadw yn y gyfres. Mae'r ymchwiliad cyfan yn cymryd prynhawn oherwydd iddynt atgynhyrchu cyn iddynt ddamcaniaethu, ac nid yw'r nam byth yn dychwelyd.

**Menter.** Mae platfform taliadau'n gweld terfynau amser ysbeidiol na all yr un tîm eu hesbonio, oherwydd bod y symptom yn ymddangos wrth dalu ond bod yr achos yn byw dri gwasanaeth i ffwrdd. Mae peirianwyr ar-alwad yn defnyddio olrhain dosbarthedig (Pennod 9.2) i ddilyn un cais methedig ar draws ffiniau gwasanaeth a dod o hyd i alwad i lawr yr afon sy'n achlysurol yn cloi'n farw dan lwyth cydamserol, [cyflwr ras](https://en.wikipedia.org/wiki/Race_condition) clasurol lle mae'r canlyniad yn dibynnu ar amseru anlwcus rhwng edafedd. Maent yn ei atgynhyrchu gyda phrawf llwyth, yn ei ddal mewn prawf integreiddio sy'n methu, yn trwsio'r cloi, ac yn cynnal post-mortem di-fai (Pennod 9.3) sy'n ychwanegu ystod olrhain a rhybudd fel bod y digwyddiad nesaf yn cael ei ddal mewn munudau, nid dyddiau.

**Llywodraeth.** Mae asiantaeth fudd-daliadau'n rhedeg ei system achosion mewn amgylchedd bwlch-aer lle na all peirianwyr gysylltu dadfygiwr â chynhyrchu na chopïo data dinasyddion i'w gliniaduron. Mae diffyg cyfrifo'n ymddangos mewn cysoni. Mae'r tîm yn dadfygio o'r hyn y mae'r amgylchedd yn ei ganiatáu: logiau strwythuredig, adeiladwaith atgynyrchadwy y gallant ei sefydlu mewn amgáead prawf ynysig, a chofnodion synthetig sy'n ail-greu'r achos methedig. Cofnodir pob cam diagnostig yn y llwybr archwilio, mae'r trwsiad yn cael ei anfon gyda phrawf methu-yna-pasio fel tystiolaeth, ac mae'r dadansoddiad achos gwraidd yn bwydo gwiriad cyn-ryddhau newydd. Gan i'r atgynhyrchiad ddefnyddio data synthetig, ni adawodd unrhyw gofnod dinesydd y ffin erioed.

## Achos busnes: cymhellion, ROI, a TCO

Mae'r enillion ar ddadfygio disgybledig yn cael eu mesur mewn oriau peiriannydd nad ydynt yn cael eu treulio'n dyfalu ac mewn diffygion nad ydynt yn ailddigwydd. Gall nam ysbeidiol heb ei ddiagnosio dreulio dyddiau o amser uwch ac uwchgyfeiriadau ar-alwad ailadroddus; mae dull atgynhyrchu-yn-gyntaf yn troi hynny'n dasg wedi'i ffinio, y gellir ei dirprwyo, ac mae'r arfer prawf-sy'n-methu'n atal yr un diffyg rhag eich bilio eto y chwarter nesaf. Ar draws sefydliad mawr, mae effaith gyfansoddi peidio ag ail-dalu byth am yr un nam yn sylweddol, ac mae'n gwella'n uniongyrchol y gyfradd methiant newid a'r amser cyfartalog i adfer y mae arweinyddiaeth eisoes yn eu holrhain.

Mae cyfanswm cost perchnogaeth yn bennaf yn hyfforddiant ac offer, ac mae'n gymedrol. Mae angen confensiynau a rennir arnoch (atgynhyrchu'n gyntaf, un newid ar y tro, prawf sy'n methu cyn y trwsiad), dadfygwyr ac olrhain sydd eisoes yn gyffredin yn y gadwyn offer, a'r buddsoddiad arsylladwyedd a ddisgrifir ym Mhennod 9.2. Y gost fwy, gudd, yw'r dewis arall: diwylliant o ofergoeliaeth lle mae peirianwyr yn cymhwyso newidiadau gwn-magnel, mae symptomau'n cael eu clytio ac yn dychwelyd, ac mae llwyth ar-alwad yn tyfu heb derfyn. Mae lleihau llafur diflas ar-alwad ar ei ben ei hun yn aml yn cyfiawnhau'r buddsoddiad, a mynegir yr achos i arweinyddiaeth symlaf fel llai o ddigwyddiadau ailadroddus ac adferiad cyflymach am gost un-tro mewn arferion ac offerynnu.

## Gwrth-batrymau a pheryglon

- **Dadfygio gwn-magnel:** newid llawer o bethau ar unwaith, fel nad yw hyd yn oed trwsiad yn dysgu dim i chi am yr achos.
- **Trwsio heb atgynhyrchu:** cyhoeddi buddugoliaeth ar nam na fuoch chi erioed yn gallu ei sbarduno ar alw.
- **Anwybyddu'r allbwn gwall:** damcaniaethu am achosion y mae'r olrhaid pentwr eisoes wedi'u diystyru.
- **Clytio symptomau:** tawelu'r symptom tra bod yr achos gwraidd yn goroesi i ddychwelyd.
- **Lledaeniad datganiadau argraffu:** allbwn dadfygio gwasgaredig wedi'i adael yn y cod, gan ychwanegu sŵn yn lle arbrawf wedi'i glymu wrth ddamcaniaeth.
- **Hepgor y prawf atchweliad:** trwsio'r nam ond gadael dim gwarchodwr, fel y gall ddychwelyd yn dawel.
- **Ailgynnig profion ansefydlog:** cuddio ansicrwydd penderfyniadol ag ailgynigion yn lle dadfygio'r cyflwr ras sylfaenol neu [heisenbug](https://en.wikipedia.org/wiki/Heisenbug), nam sy'n newid neu'n diflannu'r eiliad y ceisiwch ei arsylwi.
- **Post-mortemau wedi'u gyrru gan fai:** cosbi'r awdur, sy'n gyrru dan ddaear y wybodaeth y mae dadfygio'n dibynnu arni.

## Model aeddfedrwydd

- **Lefel 1, Cychwyn:** Mae dadfygio'n llên gwerin ac yn adwaith unigol. Mae peirianwyr yn dyfalu, yn cymhwyso newidiadau gwn-magnel, ac yn ailgychwyn pethau. Trwsir namau wrth y symptom, mae atgynyrchiadau'n brin, ac mae'r un diffygion yn ailddigwydd. Prin y gellir diagnosio cynhyrchu, ac ni all neb drosglwyddo nam i unrhyw un arall oherwydd nad oes unrhyw ymgais yn ailadroddadwy.
- **Lefel 2, Datblygu:** Mae rhai peirianwyr yn atgynhyrchu'n ddibynadwy, yn darllen olrhaidau pentwr, ac yn defnyddio dadfygwyr, ond mae'r arfer yn anghyson ac yn amrywio o berson i berson a thîm i dîm. Mae logio'n bodoli ond mae'n swnllyd ac heb ei strwythuro. Weithiau mae trwsiadau'n cael eu hanfon gyda phrawf sy'n methu, yn aml nid ydynt, a dim ond pan fydd rhywun yn mynnu y mae dadansoddiad achos gwraidd yn digwydd.
- **Lefel 3, Safoni:** Mae atgynhyrchu-yn-gyntaf, ynysu chwiliad deuaidd, un newid ar y tro, a phrawf sy'n methu cyn y trwsiad yn normau tîm wedi'u dogfennu ac wedi'u gorfodi ar draws y sefydliad. Mae deubisiad a lleihau dadfygio delta'n arfer cyffredin. Mae gan gynhyrchu logio ac olrhain strwythuredig (Pennod 9.2), ac mae post-mortemau di-fai (Pennod 9.3) yn ymateb safonol i bob diffyg a ddihangodd.
- **Lefel 4, Rheoli:** Mae'r arfer dadfygio'n cael ei fesur a'i reoli yn erbyn llinellau sylfaen. Mae cyfradd diffyg ailadroddus, amser-i-ddiagnosio, cyfrif tocynnau a ailagorwyd, a chyfran y trwsiadau a anfonwyd gyda phrawf atchweliad yn cael eu holrhain fesul tîm a'u hadolygu ar gyflymder. Trinir atgynhyrchu a chwblhau achos gwraidd fel giatiau yn hytrach na bwriadau da, ac mae tueddiadau yn erbyn y llinell sylfaen yn gyrru lle rydych chi'n buddsoddi mewn offer, hyfforddiant, ac arsylladwyedd.
- **Lefel 5, Cydgordio:** Mae dadfygio'n sgil a ddysgir, wedi'i integreiddio ag ansawdd (Pennod 2.11) a rheoli digwyddiadau (Pennod 9.3), ac mae'r ddolen gyfan yn addasu'n barhaus. Mae arsylladwyedd wedi'i ddylunio i mewn fel bod y rhan fwyaf o namau cynhyrchu'n ddiagnosadwy heb ddadfygiwr, mae pob nam a ddatryswyd yn cryfhau'r gyfres atchweliad, ac mae canfyddiadau achos gwraidd yn bwydo canfyddiad cynharach fel bod dosbarthiadau o ddiffyg yn cael eu hatal yn hytrach na'u hail-ddiagnosio. Mae'r sefydliad yn ailgydbwyso ymdrech wrth i'w systemau a'i foddau methiant esblygu, ac mae'r gyfradd diffyg ailadroddus yn parhau i ostwng.

## Syniadau ar gyfer trafodaeth

1. Pa gyfran o'ch namau diweddar a gafodd eu hatgynhyrchu'n ddibynadwy cyn i unrhyw un newid cod, a beth mae'r gyfran honno'n ei ddweud am eich dull?
2. Pan fydd atchweliad yn ymddangos, a yw eich tîm yn estyn am ddeubisiad, neu'n darllen cod â llaw nes bod rhywun yn ei sylwi?
3. Pa mor ddiagnosadwy yw eich system gynhyrchu heddiw, a beth fyddech chi'n ei roi i fod wedi dal am fethiant sydd eisoes wedi digwydd?
4. A yw eich trwsiadau'n cael eu hanfon yn gyson gyda phrawf methu-yna-pasio, ac os na, ble mae'r ddisgyblaeth honno'n chwalu?
5. Sut rydych chi'n trin profion ansefydlog: dadfygio'r ansicrwydd penderfyniadol, neu ei bapuro drosto ag ailgynigion?
6. A yw dadfygio'n cael ei addysgu'n fwriadol i beirianwyr newydd, neu a ydynt yn cael eu gadael i amsugno llên gwerin trwy osmosis?

## Prif gasgliadau

- Mae dadfygio'n brofi damcaniaeth: atgynhyrchwch yn ddibynadwy, darllenwch y gwall a'r olrhaid pentwr, yna ynyswch trwy chwiliad deuaidd a deubisiad yn hytrach na sganio.
- Lleihewch y methiant i enghraifft atgynyrchadwy leiafswm, gan ddefnyddio dadfygio delta ar gyfer mewnbynnau mawr, oherwydd mae pob elfen a dynnwyd yn achos a ddiystyrwyd.
- Parwch y teclyn â'r nam: offerynnu ac olrhain ar gyfer cynhyrchu a systemau dosbarthedig (Pennod 9.2), dadfygwyr rhyngweithiol ar gyfer ymchwiliad lleol.
- Ysgrifennwch brawf sy'n methu sy'n dal y nam cyn i chi ei drwsio, fel bod y trwsiad wedi'i brofi a bod y diffyg wedi'i warchod yn ei erbyn am byth (Pennod 2.4).
- Dewch o hyd i'r achos gwraidd a'i dynnu, cynhaliwch post-mortemau di-fai (Pennod 9.3), a thriniwch ddadfygio fel sgil y gellir ei ddysgu, nid llên gwerin.
- Newidiwch un peth ar y tro; mae newidiadau gwn-magnel a chlytiau symptom yn dinistrio tystiolaeth ac yn gwahodd y nam yn ôl.

## Cyfeiriadau a darllen pellach

- David J. Agans, *Debugging: The 9 Indispensable Rules for Finding Even the Most Elusive Software and Hardware Problems*
- Andreas Zeller, *Why Programs Fail: A Guide to Systematic Debugging*
- Andreas Zeller a Ralf Hildebrandt, "Simplifying and Isolating Failure-Inducing Input" (algorithm dadfygio delta)
- Brian W. Kernighan a Rob Pike, *The Practice of Programming* (pennod ar ddadfygio)
- Andrew Hunt a David Thomas, *The Pragmatic Programmer* (y penodau ar ddadfygio a datganiadau haeriad)
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction* (y bennod ddadfygio)
- John Regehr, "Reducers Are Fuzzers" ac ysgrifennu cysylltiedig ar leihau achosion prawf
- Charity Majors, Liz Fong-Jones, a George Miranda, *Observability Engineering* (dadfygio cynhyrchu gyda thelemetreg cardinaledd uchel ac olrhain)
- Betsy Beyer, Chris Jones, Jennifer Petoff, a Niall Richard Murphy, goln., *Site Reliability Engineering* (post-mortemau di-fai a dadfygio cynhyrchu)
