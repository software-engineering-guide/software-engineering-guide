# 5.7 Datblygu rhaglenni symudol

## Trosolwg a chymhelliant

Mae [datblygu rhaglenni symudol](https://en.wikipedia.org/wiki/Mobile_app_development) yn ddisgyblaeth adeiladu meddalwedd ar gyfer ffonau a thabledi. I lawer o bobl, ffôn bellach yw'r unig gyfrifiadur, neu'r prif un, sydd ganddynt. Mae hynny'n gwneud y rhaglen symudol yn ddrws ffrynt i'ch gwasanaeth, ac yn aml yn wyneb y mae defnyddwyr yn barnu eich sefydliad cyfan wrtho.

Mae symudol yn amgylchedd peirianneg gwahanol, nid fersiwn fach o'r we neu'r bwrdd gwaith. Mae'r ddyfais yn rhedeg mewn poced, ar fatri, dros gysylltiadau sy'n dod ac yn mynd. Mae sgriniau'n fach. Mae'r system weithredu'n rheoli'r hyn y caiff eich rhaglen ei wneud. Mae dau brif blatfform yn bodoli ([iOS](https://en.wikipedia.org/wiki/IOS) gan Apple ac [Android](https://en.wikipedia.org/wiki/Android_%28operating_system%29) gan Google), pob un â'i ieithoedd, ei reolau dylunio, a'i siop ei hun. Ni allwch ryddhau diweddariad pryd bynnag y mynnwch, oherwydd bod siop yn ei adolygu'n gyntaf, a defnyddwyr sy'n dewis pryd i'w osod. Mae'r bennod hon yn adeiladu ar beirianneg blaen (pennod 5.6), sylfeini UX (pennod 5.1), a hygyrchedd (pennod 5.3), ac yn pwyso ar ddiogelwch rhaglenni (pennod 4.2) ac integreiddio a chyflenwi parhaus (pennod 8.1).

Mae perthnasedd menter a llywodraeth yn uchel. Mae mentrau'n rhyddhau rhaglenni cwsmeriaid a rhaglenni mewnol i'w gweithlu eu hunain, yn aml wedi'u rheoli drwy [reoli dyfeisiau symudol](https://en.wikipedia.org/wiki/Mobile_device_management) (MDM: meddalwedd ganolog sy'n ffurfweddu ac yn diogelu dyfeisiau cwmni). Mae llywodraethau'n adeiladu rhaglenni sy'n wynebu dinasyddion ar gyfer budd-daliadau, iechyd, hunaniaeth, a thaliadau, ac mae'n rhaid iddynt wasanaethu pawb, gan gynnwys pobl ar hen ddyfeisiau a chysylltiadau araf, o dan gyfreithiau hygyrchedd. Yn y ddau leoliad, mae symudol yn ymrwymiad difrifol, hirhoedlog, felly triniwch ef gyda'r un trylwyredd ag y byddech unrhyw system gynhyrchu arall.

## Egwyddorion allweddol

- Dylunio ar gyfer y ddyfais: sgrin fach, batri, a rhwydwaith sy'n dod ac yn mynd.
- Tybio cysylltedd ysbeidiol; gweithio all-lein yn gyntaf a chydweddu pan allwch.
- Parchu confensiynau dylunio a rhyngweithio pob platfform.
- Nid ydych yn rheoli amseriad rhyddhau; y siop a'r defnyddiwr sy'n gwneud hynny.
- Mae dryllio'n normal; cefnogwch ystod go iawn o ddyfeisiau a fersiynau system weithredu.
- Storiwch ddata'n ddiogel ar y ddyfais, oherwydd bod dyfeisiau'n cael eu colli a'u dwyn.
- Mae hygyrchedd yn ofyniad, nid yn gyffyrddiad terfynol.
- Dewiswch eich dull adeiladu ar gyfer bywyd cyfan y rhaglen, nid dim ond diwrnod lansio.

## Argymhellion

### Dewis y dull adeiladu yn fwriadol

Mae tri dull eang, a phob un yn addas i wahanol anghenion.

Mae [datblygu brodorol](https://en.wikipedia.org/wiki/Mobile_app_development) yn golygu ysgrifennu ar wahân ar gyfer pob platfform gan ddefnyddio ei offer ei hun: Swift ar gyfer iOS, Kotlin ar gyfer Android. Rydych yn cael y perfformiad gorau, y mynediad llawnaf at nodweddion dyfais, a'r teimlad platfform mwyaf ffyddlon, ar draul adeiladu a chynnal dwy sylfaen god.

Mae [fframweithiau traws-blatfform](https://en.wikipedia.org/wiki/Cross-platform_software) yn caniatáu i un sylfaen god dargedu'r ddau blatfform. Mae [React Native](https://en.wikipedia.org/wiki/React_Native) yn defnyddio JavaScript ac yn rendro cydrannau brodorol go iawn. Mae [Flutter](https://en.wikipedia.org/wiki/Flutter_%28software%29) yn defnyddio'r iaith Dart ac yn tynnu ei declynnau ei hun. Mae'r rhain yn lleihau ymdrech ddyblyg a gallant gyflymu cyflenwi, ond maent yn ychwanegu dibyniaeth ar iechyd y fframwaith a gallant lusgo ar ôl nodweddion platfform mwyaf newydd.

Nid oes angen siop ar [ap gwe blaengar](https://en.wikipedia.org/wiki/Progressive_web_app) (PWA: gwefan y gellir ei gosod a all weithio all-lein) ac mae'n diweddaru ar unwaith, ond mae ganddo fynediad cyfyngedig at rai nodweddion dyfais a phresenoldeb gwannach ar y sgrin gartref.

Dewiswch ar sail y nodweddion dyfais sydd eu hangen, y proffil perfformiad, y gorwel cynnal a chadw, y sgiliau y gallwch eu recriwtio, a'r cyrhaeddiad sydd ei angen arnoch. Gall rhaglen ddefnyddwyr perfformiad uchel gyfiawnhau brodorol. Gall rhaglen gynnwys-a-ffurflenni gyda thîm bach ffitio'n dda gyda thraws-blatfform neu PWA.

### Dilyn canllawiau dylunio'r platfform

Mae gan bob platfform gonfensiynau manwl, cyhoeddedig. Mae Apple yn darparu'r [Canllawiau Rhyngwyneb Dynol](https://en.wikipedia.org/wiki/Human_interface_guidelines), ac mae Google yn darparu [Material Design](https://en.wikipedia.org/wiki/Material_Design). Mae'r rhain yn cwmpasu llywio, ystumiau, teipograffeg, bylchu, ac ymddygiadau system. Mae eu dilyn yn gwneud i'ch rhaglen deimlo'n gyfarwydd, sy'n gostwng yr ymdrech y mae defnyddwyr yn ei threulio'n ei dysgu. Mae ymladd yn eu herbyn yn gwneud i raglen deimlo'n estron ac yn lletchwith. Mae angen i sylfaen god traws-blatfform barchu confensiynau penodol i bob platfform lle maent yn wahanol, yn hytrach na gorfodi golwg un platfform ar y llall.

### Dylunio ar gyfer cyfyngiadau symudol

Adeiladwch all-lein-yn-gyntaf: gadewch i dasgau craidd weithio heb gysylltiad, storiwch newidiadau'n lleol, a chydweddwch pan ddaw'r rhwydwaith yn ôl. Trafodwch wrthdrawiadau'n feddylgar pan fo'r un data'n newid mewn dau le. Byddwch yn ddarbodus â batri a data: swpiwch alwadau rhwydwaith, osgowch waith lleoliad neu gefndir cyson, cywasgwch bytiau data, a pharchwch osodiadau arbed-data'r defnyddiwr. Cynlluniwch ar gyfer dryllio, y lledaeniad eang o feintiau sgrin, pŵer dyfais, a fersiynau system weithredu. Dewiswch ystod gefnogaeth ar sail data defnydd go iawn, a phrofwch ar galedwedd cymedrol, nid dim ond y prif fodelau. Dyluniwch ar gyfer sgriniau bach gyda hierarchaeth eglur, targedau cyffwrdd mawr, a chynnwys sy'n addasu i feintiau a chyfeiriadedd gwahanol.

### Cynllunio dosbarthu, fersiynu, a diweddaru

Mae cyhoeddi'n mynd drwy [Apple App Store](https://en.wikipedia.org/wiki/App_Store_%28Apple%29) a [Google Play](https://en.wikipedia.org/wiki/Google_Play), pob un â phrosesau adolygu a pholisïau a all oedi neu wrthod rhyddhad. Adeiladwch amser adolygu i mewn i'ch amserlen, a darllenwch y polisïau'n gynnar. Gan fod defnyddwyr yn dewis pryd i ddiweddaru, byddwch bob amser â llawer o fersiynau yn y maes ar unwaith. Cadwch eich rhaglen yn ôl-gydnaws â chleientiaid hŷn, a fersiynwch eich APIs (pennod 2.3) fel bod hen raglen yn parhau i weithio. Darparwch ffordd i orfodi diweddariad pan fo'n rhaid, er enghraifft anogaeth diweddariad gorfodol pan fo fersiwn yn anniogel neu heb ei chefnogi, a defnyddiwch hyn yn gynnil. Gall mentrau hefyd ddosbarthu rhaglenni mewnol drwy MDM neu sianeli preifat yn hytrach na'r siopau cyhoeddus.

### Defnyddio hysbysiadau gwthio a dolenni dwfn yn ofalus

Mae [hysbysiadau gwthio](https://en.wikipedia.org/wiki/Push_technology) yn eich galluogi i gyrraedd defnyddwyr pan fo'ch rhaglen ar gau. Defnyddiwch nhw ar gyfer gwerth go iawn, parchwch ganiatâd y defnyddiwr a chaniatâd y platfform, ac osgowch sŵn, oherwydd bod pobl yn analluogi hysbysiadau o raglenni sy'n gor-fentro. Mae [dolenni dwfn](https://en.wikipedia.org/wiki/Deep_linking) yn anfon defnyddiwr yn syth i sgrin benodol o ddolen neu hysbysiad. Ffurfweddwch nhw fel bod dolen yn agor y lle cywir yn y rhaglen, ac yn cwympo'n ôl i'r we'n rasol pan nad yw'r rhaglen wedi'i gosod.

### Diogelu'r rhaglen a'i data

Triniwch y ddyfais fel un heb ymddiriedaeth a phosibl ei cholli. Storiwch ddata sensitif yn storfa ddiogel y platfform (y [Gadwyn Allweddi iOS](https://en.wikipedia.org/wiki/Keychain_%28software%29) neu'r Android Keystore), byth mewn ffeiliau plaen. Cynigiwch [ddilysu biometrig](https://en.wikipedia.org/wiki/Biometrics) (bys neu wyneb) i ddatgloi gweithredoedd sensitif, wedi'i gefnogi gan god pasio. Ystyriwch [binio tystysgrifau](https://en.wikipedia.org/wiki/Public_key_pinning) (gwirio bod y gweinydd yn cyflwyno'r dystysgrif ddisgwyliedig) ar gyfer cysylltiadau gwerth uchel, a chynlluniwch ar gyfer cylchdroi'r tystysgrifau hynny. Lleihewch yr hyn a storiwch ar y ddyfais, diogelwch gyfrinachau, a dilynwch y canllawiau ehangach yn niogelwch rhaglenni (pennod 4.2).

### Adeiladu piblinell profi a chyflenwi go iawn

Profwch ar ddyfeisiau go iawn, nid dim ond [efelychwyr](https://en.wikipedia.org/wiki/Emulator) a chynghreiriau, oherwydd bod caledwedd, synwyryddion, a pherfformiad yn wahanol. Defnyddiwch labordy dyfeisiau neu fferm ddyfeisiau cwmwl i gwmpasu lledaeniad cynrychioliadol o fodelau a fersiynau system weithredu. Awtomeiddiwch adeiladau, profion, llofnodi, a chyflwyno i siopau drwy [integreiddio a chyflenwi parhaus](https://en.wikipedia.org/wiki/CI/CD) (pennod 8.1), gan gynnwys dosbarthu beta i brofwyr cyn rhyddhau cyhoeddus. Mae rheoli allweddi llofnodi a manylion siop yn ddiogel yn rhan o'r biblinell hon.

### Gwneud hygyrchedd yn ofyniad

Cefnogwch nodweddion hygyrchedd pob platfform: darllenwyr sgrin ([VoiceOver](https://en.wikipedia.org/wiki/VoiceOver) ar iOS, [TalkBack](https://en.wikipedia.org/wiki/Google_TalkBack) ar Android), meintio testun dynamig, cyferbyniad lliw digonol, a thargedau cyffwrdd mawr. Labelwch reolyddion fel y gall technoleg gynorthwyol eu disgrifio. Profwch gyda'r offer cynorthwyol go iawn, nid dim ond gwiriadau awtomataidd. I lywodraeth yn arbennig, mae hygyrchedd yn fandad cyfreithiol, ac mae'r manylion yn byw yn hygyrchedd (pennod 5.3).

## Cymharu: manteision ac anfanteision

| Dull | Manteision | Anfanteision |
|---|---|---|
| Brodorol (Swift, Kotlin) | Perfformiad gorau, mynediad dyfais llawn, teimlad platfform gwir | Dwy sylfaen god, cost uwch, mwy o staff |
| React Native | Un sylfaen god JavaScript, cydrannau brodorol go iawn, ailadrodd cyflym | Dibyniaeth fframwaith, cymhlethdod pontio, oedi nodweddion |
| Flutter | Un sylfaen god, UI cyson, perfformiad cryf | Sgiliau Dart yn llai cyffredin, maint rhaglen fwy, model teclyn ei hun |
| Ap gwe blaengar | Dim siop, diweddariadau ar unwaith, un sylfaen god gwe | Nodweddion dyfais cyfyngedig, presenoldeb gwannach, cyfyngiadau platfform |
| Diweddariadau gorfodol | Yn tynnu hen fersiynau anniogel yn gyflym | Yn poeni defnyddwyr os gorddefnyddir; gall rwystro mynediad |
| Binio tystysgrifau | Amddiffyniad cryf yn erbyn rhyng-gipio | Yn torri os yw tystysgrifau'n cylchdroi heb ddiweddariadau rhaglen |

Y cyfaddawd sy'n ailddigwydd yw cyrhaeddiad a chyflymder cyflenwi yn erbyn dyfnder a ffyddlondeb. Mae brodorol yn rhoi'r profiad cyfoethocaf, mwyaf ffyddlon ond yn costio fwyaf i'w adeiladu a'i gynnal. Mae dulliau traws-blatfform a PWA yn arbed ymdrech ac yn ehangu cyrhaeddiad, ar rywfaint o gost mewn teimlad platfform neu fynediad dyfais. I dîm bach sy'n rhyddhau ffurflenni a chynnwys, mae rhannu sylfaen god yn aml yn ddoeth. I raglen ddefnyddwyr fanwl-ofynnol, gall dyfnder brodorol fod yn werth y pris. Penderfynwch gyda golwg ar fywyd cyfan y rhaglen, nid dim ond y lansiad.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Am ba hyd rydym yn cefnogi hen gleientiaid yn y maes, ac a yw ein API wedi'i fersiynu i'w cadw i weithio?** Gan fod defnyddwyr yn dewis pryd i ddiweddaru, byddwch bob amser â llawer o fersiynau o'r rhaglen wedi'u gosod ar unwaith, a bydd newid cefn sy'n tybio bod pawb yn gyfredol yn torri'r gynffon hir o hen gleientiaid. Penderfynwch eich ffenestr ôl-gydnawsedd, fersiynwch eich APIs fel bod hen raglen yn parhau i weithio, a chadwch lwybr diweddaru gorfodol prin ei ddefnydd ar gyfer fersiynau sydd wir yn anniogel. Mae hyn yn bwysig i raglenni dinasyddion llywodraeth a rhaglenni gweithlu menter fel ei gilydd, lle na all pobl ar hen ddyfeisiau, neu ni fyddant, uwchraddio ar eich amserlen chi. Dewch â'ch data dosbarthiad fersiwn presennol a gofynnwch beth sy'n torri i'r cleient hynaf sy'n dal mewn defnydd go iawn. Os nad ydych yn gwybod y dosbarthiad hwnnw, offerynnwch ef cyn i chi ryddhau eich newid torri nesaf.

2. **Beth yw ein bar ar gyfer anfon hysbysiad gwthio, a phwy sy'n penderfynu beth sy'n werth torri ar draws defnyddiwr?** Mae hysbysiadau gwthio'n cyrraedd pobl pan fo'r rhaglen ar gau, sy'n eu gwneud yn bwerus ac yn hawdd eu camddefnyddio, ac mae defnyddwyr yn analluogi hysbysiadau (neu'n dileu'r rhaglen) o gynhyrchion sy'n gor-fentro. Cytunwch ar beth sy'n cyfrif fel gwerth go iawn, sut mae defnyddwyr yn rheoli amledd a sianel, a sut rydych yn parchu caniatâd y platfform yn hytrach na swnian am ganiatâd. Heb far a rennir, bydd pob tîm sydd â metrig i'w daro'n estyn am wthiad, a bydd y sianel gyfan yn dirywio'n sŵn. Dewch â hysbysiadau'r mis diwethaf a anfonoch a gofynnwch am ba rai y byddai'r defnyddiwr wedi diolch i chi. Os oedd y rhan fwyaf yn hyrwyddo, tynhewch y polisi cyn i'r gyfradd optio allan wneud hynny drosoch.

3. **A yw ein piblinell gyflenwi symudol yn real, yn cwmpasu llofnodi, fferm ddyfeisiau, a dosbarthu beta, neu a yw rhyddhau'n sgarmes â llaw sy'n peri straen?** Mae symudol yn ychwanegu peryglon nad oes gan y we: gall adolygiad siop oedi neu wrthod rhyddhad, mae'n rhaid trafod allweddi llofnodi a manylion siop yn ddiogel, ac mae caledwedd a synwyryddion yn wahanol ddigon fel bod efelychwyr yn cuddio problemau go iawn. Mae awtomeiddio adeiladau, profion, llofnodi, a chyflwyno i siopau drwy CI/CD, gyda dosbarthu beta i brofwyr a fferm ddyfeisiau cwmwl sy'n cwmpasu'r modelau y mae eich defnyddwyr yn eu cario go iawn, yn troi rhyddhadau o arwriaeth yn drefn arferol. Penderfynwch pwy sy'n berchen ar y biblinell a'r allweddi llofnodi, a sut mae amser adolygu siop wedi'i adeiladu i mewn i bob cynllun rhyddhad. Dewch â stori eich rhyddhad diwethaf a chyfrwch y camau â llaw. Mae pob un yn fan lle gall rhyddhad llawn straen fynd o chwith dan derfyn amser.

4. **A ydym wedi dewis brodorol, traws-blatfform, neu ap gwe blaengar ar gyfer bywyd cyfan y cynnyrch hwn, neu ddim ond ar gyfer diwrnod lansio?** Y dull adeiladu yw'r ysgogiad mwyaf sengl ar gost a gallu rhaglen symudol dros flynyddoedd, a gall dewis a wnaed i ryddhau'n gyflym eich trapio: mae brodorol yn prynu'r mynediad dyfais a'r teimlad platfform cyfoethocaf ar bris dwy sylfaen god a dau set sgiliau, tra bo traws-blatfform a PWA yn rhannu cod ond yn ychwanegu dibyniaeth fframwaith neu'n colli mynediad at rai nodweddion dyfais. I dîm mawr, mae'r penderfyniad hwn yn llywio recriwtio, y gyllideb cynnal a chadw, a pha mor gyflym y gallwch fabwysiadu pob rhyddhad blynyddol o system weithredu, felly mae'n haeddu perchennog eglur yn hytrach na diofyn a osodwyd gan bwy bynnag a ysgrifennodd y prototeip cyntaf. Dewch â'r nodweddion dyfais sydd eu hangen, y proffil perfformiad, y gorwel cynnal a chadw, a'r sgiliau y gallwch eu recriwtio go iawn, a byddwch yn onest ynghylch pa nodweddion platfform y byddech yn eu colli o dan bob opsiwn. Mewn lleoliadau menter a llywodraeth, pwyswch a yw'r rhaglen yn ymrwymiad hirhoedlog sy'n rhaid iddo oroesi trosiant staff a degawd o newid platfform, a chofnodwch y penderfyniad a'i resymeg fel nad yw tîm y dyfodol yn cael ei adael i ddyfalu pam mae'r sylfaen god yn edrych fel y mae.

5. **Pa ystod cefnogaeth dyfais a fersiwn system weithredu sydd angen ar ein defnyddwyr go iawn, ac a ydym yn profi ar y caledwedd y maent yn ei gario go iawn yn hytrach na'r ffonau ar ein desgiau?** Dryllio yw'r cyflwr normal ar gyfer symudol: mae defnyddwyr yn rhychwantu lledaeniad eang o feintiau sgrin, pŵer dyfais, a fersiynau system weithredu, a bydd rhaglen a diwniwyd ar brif fodelau'r tîm yn rhyddhau'n araf neu wedi torri ar y caledwedd cymedrol y mae llawer o'ch cynulleidfa'n berchen arno. Mae gosod ystod gefnogaeth yn gyfaddawd rhwng cyrhaeddiad ac ymdrech, oherwydd mae pob model hŷn a fersiwn system weithredu rydych yn addo eu cefnogi'n ehangu'r matrics profi a'r baich cynnal a chadw, felly rhaid i'r ystod ddod o ddata defnydd go iawn yn hytrach na thybiaeth. Dewch â'ch dosbarthiad dyfais a fersiwn system weithredu, y modelau y mae fferm neu labordy dyfeisiau cwmwl yn eu cwmpasu ar hyn o bryd, a'r perfformiad rydych wedi'i fesur ar galedwedd pen isel, nid dim ond cynghreiriau. I raglenni dinasyddion llywodraeth mae hyn bron yn anfargeiniadwy, oherwydd bod yn rhaid i chi wasanaethu pawb gan gynnwys pobl ar hen ddyfeisiau a chysylltiadau araf o dan rwymedigaethau hygyrchedd, ac i fflydoedd menter dylech brofi'r union ddolenni llaw gwydn y mae staff yn eu cario yn hytrach na sampl generig.

6. **Pa ddata sensitif sy'n byw ar y ddyfais, ac a yw pob darn wedi'i ddiogelu yn erbyn ffôn sydd wedi'i golli, ei ddwyn, neu yn nwylo rhywun arall?** Mae dyfais symudol yn teithio mewn poced ac yn cael ei cholli neu ei dwyn, felly mae unrhyw ddata neu gyfrinach a storir mewn ffeil blaen un ffôn ar goll i ffwrdd o gael ei ddatgelu, ac mae radiws y ffrwydrad yn tyfu gyda phob defnyddiwr. Mae'r ystyriaethau'n tynnu yn erbyn ei gilydd: mae storio data dros dro ar y ddyfais yn yr hyn sy'n gwneud i all-lein-yn-gyntaf weithio ac yn cadw'r rhaglen yn gyflym, ac eto mae pob eitem storio dros dro'n atebolrwydd sy'n rhaid iddi eistedd yn storfa ddiogel y platfform (y Gadwyn Allweddi iOS neu'r Android Keystore), cael ei lleihau, ac yn ddelfrydol cael ei giatio y tu ôl i fiometreg neu god pasio. Dewch ag arolwg o'r union beth y mae'r rhaglen yn ei barhau'n lleol, ble mae pob eitem wedi'i storio, beth sy'n ei ddatgloi, ac a yw cysylltiadau gwerth uchel yn defnyddio binio tystysgrifau gyda chynllun cylchdroi ymarferol. Mewn lleoliadau menter, cysylltwch hyn â pholisi rheoli dyfeisiau symudol a dileu o bell, ac mewn lleoliadau llywodraeth triniwch ddata personol ar-ddyfais fel dinoethiad preifatrwydd a chyfreithiol y mae'n rhaid ei gyfiawnhau, ei ddogfennu, a'i amddiffyn dan archwiliad.

## Trwy lens sector

**Cwmni newydd.** Gyda thîm bach ac ychydig o redlan, anaml y gallwch fforddio dwy sylfaen god frodorol neu ddau set sgiliau, felly mae fframwaith traws-blatfform neu hyd yn oed PWA sy'n cyrraedd y ddwy siop o un sylfaen god fel arfer yn ennill. Rhyddhewch all-lein-yn-gyntaf ar gyfer yr un dasg graidd sy'n bwysig, cadwch unrhyw docyn mewn storfa ddiogel yn hytrach na ffeil blaen, ac adeiladwch amser adolygu siop i mewn i bob rhyddhad fel nad yw gwrthodiad yn chwythu dyddiad lansio. Hepgorwch ddiweddariadau gorfodol, binio tystysgrifau, a fferm ddyfeisiau hyd nes bod defnydd go iawn yn eu cyfiawnhau.

**Busnes bach.** Heb arbenigwr symudol pwrpasol a chyllideb dynn, pwyswch yn drwm tuag at brynu yn hytrach nag adeiladu: adeiladwr rhaglen dim-cod, rhaglen label-gwyn gan eich gwerthwr pwynt-gwerthu neu archebu, neu PWA wedi'i wneud yn dda o'ch gwefan bresennol yn aml yn curo rhaglen bwrpasol na allwch ei chynnal. Os byddwch yn comisiynu rhaglen, byddwch berchen ar yr allweddi llofnodi a'r cyfrifon siop eich hun fel na all contractwr ddal eich presenoldeb yn wystl, a mynnwch hygyrchedd a storio diogel ar-ddyfais yn y contract. Cadwch y cwmpas i'r un neu ddwy dasg y mae cwsmeriaid yn eu gwneud go iawn ar ffôn.

**Menter.** Ar raddfa fawr, mae'r rhaglen yn ymrwymiad hirhoedlog ar draws sawl tîm, felly safonwch y dull adeiladu, y patrwm storio diogel, y biblinell CI/CD, a'r polisi fersiynu API yn hytrach na gadael i bob cynnyrch eu hail-ddyfeisio. Mae rhaglenni gweithlu mewnol fel arfer yn llifo drwy reoli dyfeisiau symudol ar gyfer gosod, ffurfweddu, dileu o bell, a pholisi, tra bo angen fferm ddyfeisiau ar raglenni cwsmeriaid sy'n cwmpasu defnydd go iawn a hygyrchedd a diogelwch wedi'u harchwilio. Llywodraethwch allweddi llofnodi, manylion siop, ac amseriad rhyddhau'n ganolog fel na fydd newid cefn torri byth yn gadael y gynffon hir o gleientiaid hŷn yn sownd.

**Llywodraeth.** Mae rheolau caffael, tryloywder, ac atebolrwydd cyhoeddus yn llywio pob dewis. Rhaid i chi wasanaethu pawb, gan gynnwys pobl ar hen ddyfeisiau a chysylltiadau araf, felly mae hygyrchedd yn fandad cyfreithiol wedi'i wirio gydag offer cynorthwyol go iawn, ac mae ystod gefnogaeth dyfais eang bron yn anfargeiniadwy. Ffafriwch ddulliau a chontractau sy'n osgoi clymu i werthwr, yn cadw data'n gludadwy, ac yn gadael i'r cyhoedd archwilio beth mae'r rhaglen yn ei wneud â'u data, a thriniwch ddata personol ar-ddyfais fel dinoethiad y mae'n rhaid i chi ei gyfiawnhau a'i ddogfennu dan archwiliad.

## Enghreifftiau

**Cwmni newydd.** Roedd yn rhaid i gwmni newydd tri pherson oedd yn adeiladu rhaglen olrhain arferion gyrraedd iOS ac Android fel ei gilydd ond ni allent fforddio dwy sylfaen god frodorol na dau set sgiliau. Dewisant fframwaith traws-blatfform fel y gallai un tîm bach ryddhau i'r ddwy siop, a dyluniwyd all-lein-yn-gyntaf o'r cychwyn fel y gallai defnyddiwr gofnodi arferiad ar y trên tanddaearol heb signal a chydweddu'n ddiweddarach. Cadwon nhw'r tocyn mewngofnodi yn storfa ddiogel y platfform yn hytrach na ffeil blaen, adeiladu amser adolygu siop i mewn i bob cynllun rhyddhad, a phrofi ar rai ffonau hŷn rhad ochr yn ochr â'u rhai eu hunain, a ddaliodd berfformiad araf y byddent fel arall wedi'i ryddhau.

**Menter.** Adeiladodd cwmni logisteg raglen fewnol ar gyfer ei yrwyr a staff warws. Gan fod gan warysau a llwybrau dosbarthu signal clytiog, dewisodd y tîm gynllun all-lein-yn-gyntaf: mae sganiau a diweddariadau statws yn arbed yn lleol ac yn cydweddu pan ddaw cysylltiad yn ôl. Defnyddiwyd fframwaith traws-blatfform i wasanaethu un sylfaen god i'r ddau blatfform gyda thîm bach. Mae'r rhaglen yn cael ei dosbarthu drwy reoli dyfeisiau symudol yn hytrach na'r siopau cyhoeddus, felly mae TG yn rheoli gosod, ffurfweddu, a pholisi diogelwch ar ddyfeisiau'r cwmni. Mae manylion sensitif yn byw yn storfa ddiogel y platfform, ac mae biometreg yn datgloi'r rhaglen. Mae fferm ddyfeisiau cwmwl yn profi lledaeniad cynrychioliadol o'r dolenni llaw gwydn y mae staff yn eu cario go iawn.

**Llywodraeth.** Rhyddhaodd asiantaeth genedlaethol raglen sy'n wynebu dinasyddion ar gyfer hunaniaeth a budd-daliadau. Roedd hygyrchedd yn ofyniad caled o'r diwrnod cyntaf: cefnogaeth darllenydd sgrin lawn, meintio testun dynamig, a chyferbyniad cryf, wedi'u profi gydag offer cynorthwyol go iawn i fodloni'r gyfraith. Gan fod dinasyddion yn defnyddio ystod enfawr o ddyfeisiau, cefnogodd y tîm fand eang o hen fodelau a chysylltiadau araf, a chadwodd dasgau craidd yn gweithio all-lein. Mae data sensitif yn aros mewn storfa ddyfais ddiogel, mae biometreg yn diogelu mynediad, ac mae cysylltiadau gwerth uchel yn defnyddio binio tystysgrifau gyda phroses gylchdroi wedi'i chynllunio. Mae fersiynu API yn cadw hen raglenni wedi'u gosod i weithio, ac mae llwybr diweddaru gorfodol prin ei ddefnydd yn bodoli ar gyfer atgyweiriadau diogelwch. Mae amserlenni adolygu siop wedi'u hadeiladu i mewn i bob cynllun rhyddhad.

## Achos busnes: cymhellion, ROI, a TCO

Symudol yw lle mae llawer o ddefnyddwyr yn cyfarfod â'ch gwasanaeth, felly mae'r rhaglen yn effeithio ar fabwysiadu, boddhad, a chwblhau'r tasgau sy'n bwysig i'ch sefydliad. Mae rhaglen gyflym, ddibynadwy, wedi'i dylunio'n dda yn cynyddu defnydd ac yn lleihau baich cymorth. I fentrau, gall rhaglen symudol fewnol wneud gweithlu symudol yn fesuradwy fwy cynhyrchiol a thorri gwaith papur. I lywodraethau, mae rhaglen ddinesydd ddefnyddiadwy'n ehangu mynediad ac yn lleihau galw canolfan alwadau ac wyneb yn wyneb.

Ar gyfanswm cost perchnogaeth (TCO), dewis y dull yw'r ysgogiad mwyaf. Mae brodorol yn golygu talu am ddwy sylfaen god a dau set sgiliau dros fywyd cyfan y rhaglen. Mae traws-blatfform yn cyfnewid peth o hynny am ddibyniaeth y mae'n rhaid i chi ei chadw'n gyfredol. Y tu hwnt i god, cyllidwch am ffioedd siop a chylchoedd adolygu, labordy profi dyfeisiau neu fferm gwmwl, cefnogaeth fersiwn system weithredu barhaus wrth i blatfformau ryddhau'n flynyddol, a'r gwaith diogelwch y mae symudol yn ei fynnu. Mae cost tan-fuddsoddi'n ymddangos fel chwalfeydd ar ddyfeisiau na chefnogir, digwyddiadau diogelwch o ddata ar-ddyfais heb ei ddiogelu, rhyddhadau a wrthodwyd neu a oedwyd, a defnyddwyr sy'n gadael rhaglen araf neu lletchwith.

I wneud yr achos i'r arweinyddiaeth, cysylltwch y rhaglen â chanlyniadau diriaethol: cwblhau tasgau, cadw defnyddwyr, cynhyrchiant gweithlu, neu gost cymorth is. Prisiwch y penderfyniad dull llawn dros fywyd y rhaglen, nid dim ond y rhyddhad cyntaf, ac enwch y risgiau (diogelwch, cyfraith hygyrchedd, gwrthodiad siop) y mae arfer symudol difrifol yn eu lleihau.

## Gwrth-batrymau a pheryglon

- **Trin symudol fel gwefan wedi'i chrebachu**: anwybyddu cyffwrdd, ystumiau, a chonfensiynau platfform.
- **Tybio rhwydwaith perffaith**: dim triniaeth all-lein, felly mae'r rhaglen yn torri'r eiliad y mae signal yn diflannu.
- **Profi dim ond ar y prif fodel diweddaraf**: cuddio perfformiad gwael ar y dyfeisiau y mae defnyddwyr go iawn yn eu cario.
- **Storio cyfrinachau mewn ffeiliau plaen**: data sensitif wedi'i ddinoethi pan fo dyfais ar goll neu wedi'i dwyn.
- **Gorlwytho hysbysiadau**: gormod o wthiadau, felly mae defnyddwyr yn tewi neu'n dileu'r rhaglen.
- **Anwybyddu amser adolygu siop**: cynlluniau rhyddhau sy'n tybio cyhoeddi ar unwaith ac wedyn yn llithro.
- **Dim llwybr diweddaru gorfodol**: mae hen fersiynau anniogel yn parhau heb ffordd i'w hymddeol.
- **Draenio batri a data**: gwaith cefndir cyson a rhwydweithio siaradus y mae defnyddwyr yn sylwi arno.
- **Hygyrchedd fel ôl-ystyriaeth**: eithrio defnyddwyr ac, i lywodraeth, torri'r gyfraith.
- **Un sylfaen god wedi'i gorfodi i edrych yn union yr un fath ym mhobman**: rhaglen sy'n teimlo'n estron ar y ddau blatfform.

## Model aeddfedrwydd

**Lefel 1: Cychwyn.** Mae symudol yn ad hoc ac yn adweithiol. Mae'r rhaglen wedi'i hadeiladu fel gwefan, wedi'i phrofi ar ffonau'r tîm ei hun, ac yn aml yn torri all-lein. Ychydig o feddwl a roddir i storio diogel, hygyrchedd, neu amserlenni adolygu siop. Mae rhyddhadau'n sgarmes â llaw sy'n peri straen, ac nid oes neb yn berchen ar y dull adeiladu na'r allweddi llofnodi.

**Lefel 2: Datblygu.** Mae arferion sylfaenol yn ymddangos, ond maent yn anghyson ar draws timau a chynhyrchion. Dewisir dull adeiladu ar gyfer rhaglen benodol, mae'n dilyn sylfeini'r platfform ac fe'i profir ar ychydig o ddyfeisiau go iawn, ac mae rhywfaint o driniaeth all-lein a storio diogel yn bodoli. Mae adeiladau'n rhannol wedi'u hawtomeiddio ac mae rhywun yn berchen ar gyflwyniadau siop, ac eto gall rhaglen tîm arall wneud hyn i gyd yn wahanol o hyd neu ddim o gwbl.

**Lefel 3: Safoni.** Mae arfer da wedi'i ddogfennu a'i orfodi ar draws y sefydliad. All-lein-yn-gyntaf yw'r diofyn, profir ystod gefnogaeth dyfais ddogfennedig ar labordy dyfeisiau neu fferm gwmwl, a dilynir canllawiau dylunio platfform a hygyrchedd ac fe'u gwirir gydag offer cynorthwyol go iawn. Mae storio diogel, biometreg, a fersiynu API yn safonol, mae CI/CD yn awtomeiddio adeiladau, profion, llofnodi, a dosbarthu beta, ac mae amser adolygu siop wedi'i gynllunio i mewn i bob rhyddhad.

**Lefel 4: Rheoli.** Mesurir a rheolir ansawdd symudol yn erbyn llinellau sylfaen. Caiff chwalfeydd, perfformiad cychwyn oer a rendro sgrin, defnydd batri a data, a chyfraddau cwblhau tasgau eu cipio'n barhaus o ddyfeisiau go iawn a'u holrhain yn erbyn targedau, gyda dadansoddiadau fesul model a fersiwn system weithredu fel bod dirywiad ar galedwedd pen isel yn cael ei ddal, nid ei ryddhau. Archwilir hygyrchedd a diogelwch yn hytrach na'u tybio, monitrir cyfraddau optio allan hysbysiadau a mabwysiadu diweddariadau, ac adolygir yr ystod gefnogaeth a'r dull adeiladu ar sail y dystiolaeth hon. Mae penderfyniadau lladd neu drwsio ar gyfer rhyddhad yn gorffwys ar y metrigau, nid ar sut roedd y rhaglen yn teimlo ar ffôn yr arweinydd.

**Lefel 5: Cerddorfeiddio.** Caiff symudol ei wella'n barhaus a'i integreiddio ar draws y sefydliad, ac mae'n addasu wrth i dirwedd y dyfeisiau newid. Mae cylchdroi tystysgrifau, llwybrau diweddaru gorfodol, a dadwneud yn drefn arferol, ailgwmpesir yr ystod gefnogaeth a'r dull adeiladu ar sail tystiolaeth wrth i blatfformau ryddhau'n flynyddol, a thrinnir lledaeniad cyfan y defnyddwyr a'r dyfeisiau fel dosbarth cyntaf. Mae cynllunio symudol wedi'i gysylltu â diogelwch, hygyrchedd, API, ac arfer cyflenwi, fel bod newid system weithredu, haen ddyfais newydd, neu newid polisi'n cael ei amsugno fel gwaith arferol yn hytrach nag argyfwng.

## Syniadau i'w trafod

- Sut rydych chi'n penderfynu rhwng brodorol, traws-blatfform, ac ap gwe blaengar ar gyfer cynnyrch penodol?
- Pa ystod cefnogaeth dyfais a fersiwn system weithredu sy'n ffitio'ch data defnyddwyr go iawn, a sut rydych chi'n ei gadw'n gyfredol?
- Ble mae all-lein-yn-gyntaf yn hanfodol yn eich rhaglen, a sut byddwch chi'n trafod gwrthdrawiadau cydweddu?
- Pryd mae diweddariad gorfodol yn gyfiawn, a sut ydych chi'n osgoi rhwystro defnyddwyr yn annheg?
- Sut byddwch chi'n profi ar ddyfeisiau go iawn ar raddfa sy'n adlewyrchu eich defnyddwyr?
- Pa ddata sensitif sy'n byw ar y ddyfais, a sut mae pob darn wedi'i ddiogelu?
- Sut ydych chi'n parchu confensiynau pob platfform o sylfaen god a rennir?

## Prif negeseuon

- Dewiswch y dull adeiladu (brodorol, traws-blatfform, neu PWA) ar gyfer bywyd cyfan y rhaglen.
- Dilynwch ganllawiau dylunio'r platfform fel bod y rhaglen yn teimlo'n gyfarwydd ac yn gostwng ymdrech y defnyddiwr.
- Dyluniwch ar gyfer cyfyngiadau symudol: all-lein-yn-gyntaf, batri a data darbodus, dryllio, sgriniau bach.
- Nid ydych yn rheoli amseriad rhyddhau; cynlluniwch ar gyfer adolygiad siop, fersiynu, a diweddariadau gorfodol.
- Defnyddiwch hysbysiadau gwthio a dolenni dwfn gyda hunanataliaeth a chaniatâd.
- Diogelwch ddata ar-ddyfais gyda storio diogel, biometreg, ac, lle bo'n gyfiawn, binio tystysgrifau.
- Profwch ar ddyfeisiau go iawn ac awtomeiddiwch y biblinell symudol drwy CI/CD.
- Gwnewch hygyrchedd yn ofyniad, sydd i lywodraeth yn fandad cyfreithiol.

## Cyfeiriadau a darllen pellach

- Apple, *Human Interface Guidelines*
- Google, *Material Design* guidelines
- Apple, *App Store Review Guidelines*
- Google, *Google Play developer policies and Android developer documentation*
- OWASP, *Mobile Application Security Verification Standard (MASVS)* and *Mobile Security Testing Guide*
- React Native project documentation
- Flutter project documentation
- Google, *web.dev* guidance on progressive web apps
- U.S. Section 508 and WCAG (Web Content Accessibility Guidelines) references for mobile accessibility
- NIST, *Guidelines on mobile device security and management*
