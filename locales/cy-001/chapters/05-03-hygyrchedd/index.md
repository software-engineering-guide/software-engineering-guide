# 5.3 Hygyrchedd

## Trosolwg a chymhelliant

Mae [hygyrchedd](https://en.wikipedia.org/wiki/Accessibility) (a elwir yn aml yn fyr fel "a11y") yn arfer o adeiladu meddalwedd y gall pobl ag anableddau ei chanfod, ei deall, ei llywio, a'i defnyddio. Mae hynny'n cynnwys pobl sy'n ddall neu â golwg isel, sy'n fyddar neu'n drwm eu clyw, sydd â nam symudedd, sydd â gwahaniaethau gwybyddol neu ddysgu, ac sy'n wynebu cyfyngiadau dros dro neu sefyllfaol fel braich wedi torri, heulwen llachar, neu ystafell swnllyd. Mae gan tua un o bob pump o bobl anabledd, ac mae pawb yn elwa o ddyluniad hygyrch ar ryw adeg. Nid cymhwysiad cilfachol yw hyn. Mae'n linell sylfaen o ansawdd.

I dimau mawr, mae'n rhaid i hygyrchedd gael ei adeiladu i mewn i'r system, nid ei adael i fwriadau da unigolion. Pan fydd llawer o dimau'n cyflenwi i mewn i un cynnyrch, gall un cydran anhygyrch (maes ffurflen heb label, dangosydd statws lliw-yn-unig, trap bysellfwrdd mewn modal) gau defnyddwyr anabl allan o daith gyfan. Adeiladu hygyrchedd i mewn i gydrannau a rennir, tocynnau dylunio, piblinellau profi, a diffiniadau o "wedi'i wneud" yw'r unig ffordd o'i gwneud yn ddibynadwy ar raddfa. Mae ei ôl-osod ar ôl y ffaith yn ddrud ac yn dueddol i wallau. Mae ei ddylunio i mewn yn rhad ac yn barhaus.

I lywodraeth, mae hygyrchedd yn ofyniad cyfreithiol ac yn rhwymedigaeth ddinesig, nid yn beth braf i'w gael. Rhaid i wasanaethau cyhoeddus wasanaethu pob aelod o'r cyhoedd, ac yn aml nid oes gan ddinasyddion anabl ddarparwr amgen: os yw gwefan y llywodraeth yn anhygyrch, ni allant gael eu budd-dal, eu trwydded, na phleidleisio mewn unrhyw ffordd arall. Mae cyfreithiau a safonau ledled y byd yn gwneud hygyrchedd yn orfodol i gyrff cyhoeddus, ac yn gynyddol i'r sector preifat hefyd. Mae'r bennod hon yn trin hygyrchedd fel tri pheth ar unwaith: dyletswydd gyfreithiol, dyletswydd foesegol, a dylunio da yn syml.

*Gweler hefyd:* pennod 5.2 (dylunio UI a systemau dylunio), pennod 5.6 (peirianneg blaen), a phennod 5.1 (sylfeini UX).

## Egwyddorion allweddol

- Mae hygyrchedd yn briodoledd ansawdd sylfaenol, fel diogelwch a pherfformiad, nid yn nodwedd ddewisol.
- Yr egwyddorion POUR: rhaid i ryngwynebau fod yn Ganfyddadwy, yn Weithredadwy, yn Ddealladwy, ac yn Gadarn (Perceivable, Operable, Understandable, Robust).
- [HTML semantig](https://en.wikipedia.org/wiki/Semantic_HTML) yn gyntaf; defnyddiwch [ARIA](https://en.wikipedia.org/wiki/WAI-ARIA) dim ond i lenwi bylchau gwirioneddol, byth fel dirprwy dros elfennau brodorol.
- Rhaid i bopeth y gellir ei ddefnyddio gyda llygoden fod yn ddefnyddiadwy gyda bysellfwrdd yn unig.
- Peidiwch â chyfleu gwybodaeth trwy liw, siâp, neu safle yn unig.
- Nid yw teclynnau awtomataidd ond yn dal cyfran fach o faterion; mae profi â llaw a phrofi [technoleg gynorthwyol](https://en.wikipedia.org/wiki/Assistive_technology) yn hanfodol.
- Mae dyluniad hygyrch yn ddyluniad gwell i bawb (yr ["effaith ymyl gostwng,"](https://en.wikipedia.org/wiki/Curb_cut) lle mae nodweddion a adeiladwyd ar gyfer pobl anabl yn elwa pob defnyddiwr).
- Dylunio a phrofi gyda phobl anabl, nid dim ond ar eu cyfer.

## Argymhellion

### Dylunio ac adeiladu yn ôl WCAG, gan dargedu'r safon gyfredol

Y [Canllawiau Hygyrchedd Cynnwys Gwe](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) yw'r cyfeirbwynt rhyngwladol. Mae WCAG 2.1 a 2.2 wedi'u trefnu o dan y pedair egwyddor POUR, gyda meini prawf llwyddiant profadwy ar lefelau cydymffurfiaeth A, AA, ac AAA. Targedwch Lefel AA fel eich llinell sylfaen; dyna mae'r rhan fwyaf o gyfreithiau'n cyfeirio ato. Mae WCAG 2.2 yn ychwanegu meini prawf ar gyfer gweladwyedd ffocws, maint targed, a lleihau baich gwybyddol. Mae WCAG 3.0 yn olynydd sy'n dod i'r amlwg, wedi'i strwythuro'n wahanol ac yn dal i gael ei ddatblygu. Cadwch lygad arno, ond adeiladwch yn ôl 2.2 AA heddiw. Trinwch y canllawiau fel llawr, nid nenfwd: nid yw pasio pob maen prawf yn gwarantu profiad gwirioneddol ddefnyddiadwy.

### Defnyddio HTML semantig ac ARIA cywir

Daw elfennau HTML brodorol (botymau, dolenni, rheolyddion ffurflenni, penawdau, rhestrau, tirnodau) gyda semanteg hygyrchedd, ymddygiad bysellfwrdd, a chefnogaeth technoleg gynorthwyol wedi'u hadeiladu i mewn. Defnyddiwch nhw'n gyntaf. Ewch at rolau, cyflyrau, a phriodweddau ARIA (Accessible Rich Internet Applications) dim ond i ddisgrifio teclynnau pwrpasol nad yw HTML yn gallu eu mynegi, a dilynwch Arferion Awduro ARIA. Mae rheol gyntaf ARIA yn syml: peidiwch â defnyddio ARIA os bydd elfen frodorol yn gwneud y tro. Mae ARIA anghywir yn waeth na dim byd: mae'n camarwain [darllenwyr sgrin](https://en.wikipedia.org/wiki/Screen_reader) yn weithredol. Rhowch strwythur pennawd rhesymegol i'r dudalen, labeli ystyrlon, testun amgen ar gyfer delweddau, is-deitlau a thrawsgrifiadau ar gyfer cyfryngau, a chysylltiad rhaglennol rhwng pob label a'i reolydd.

### Gwarantu gweithredadwyedd bysellfwrdd a thechnoleg gynorthwyol

Rhaid i bob elfen ryngweithiol fod yn hygyrch ac yn weithredadwy gyda'r bysellfwrdd yn unig, mewn trefn resymegol, gyda dangosydd ffocws gweladwy clir. Osgowch drapiau bysellfwrdd. Rheolwch ffocws yn fwriadol pan fydd cynnwys yn newid: symudwch ffocws i ddeialog pan fydd yn agor, dychwelwch ef pan fydd y ddeialog yn cau, a chyhoeddwch ddiweddariadau dynamig trwy ranbarthau byw. Profwch gyda thechnolegau cynorthwyol go iawn, gan gynnwys darllenwyr sgrin ar ddesg a symudol, chwyddhad sgrin, rheolaeth lais, a mynediad switsh. A pharchwch ddewisiadau defnyddwyr fel llai o symudiad a chyferbyniad uwch.

### Profi gyda theclynnau awtomataidd, adolygiad â llaw, a defnyddwyr go iawn

Mae sganwyr hygyrchedd awtomataidd yn werthfawr, a dylent redeg yn y biblinell ar bob newid. Ond mae astudiaethau'n dangos yn gyson mai dim ond lleiafrif o faterion go iawn maen nhw'n eu dal, tua thraean. Mae angen barn ddynol ar gyfer y gweddill: teithiau bysellfwrdd, profi darllenydd sgrin, gwiriadau cyferbyniad, a gofyn a yw'r cynnwys yn wirioneddol ddealladwy. Yn bwysicach na dim, cynhwyswch bobl ag anableddau mewn profi defnyddioldeb. Adeiladwch feini prawf derbyn hygyrchedd i mewn i'r diffiniad o "wedi'i wneud", fel bod materion yn cael eu dal fesul stori yn hytrach nag mewn archwiliad cyn lansio.

### Gwneud hygyrchedd yn sefydliadol, nid yn arwrol

Pobwch hygyrchedd i mewn i'r system ddylunio fel bod cydrannau'n cael eu cyflenwi'n hygyrch yn ddiofyn. Cynigiwch hyfforddiant fel bod dylunwyr, peirianwyr, awduron cynnwys, a rheolwyr cynnyrch pob un yn gwybod am beth maen nhw'n gyfrifol. Sefydlwch safon hygyrchedd, perchennog neu ganolfan ragoriaeth, a phroses unioni. Cyhoeddwch ddatganiad hygyrchedd a rhowch ffordd i ddefnyddwyr adrodd ar rwystrau. A chaffaelwch yn hygyrch: mynnwch fod gwerthwyr a chydrannau trydydd parti yn cydymffurfio, ac yn darparu tystiolaeth (fel adroddiad cydymffurfiaeth hygyrchedd).

## Cyfaddawdau: manteision ac anfanteision

| Dull | Manteision | Anfanteision |
|---|---|---|
| Adeiladu hygyrchedd i mewn o'r cychwyn | Rhataf, parhaus, gwell i bawb | Angen hyfforddiant a disgyblaeth ymlaen llaw |
| Ôl-osod / unioni yn ddiweddarach | Yn gohirio ymdrech, yn dadflocio lansiad cyflym | Llawer drutach, bregus, amlygiad cyfreithiol yn y cyfamser |
| Profi awtomataidd yn unig | Cyflym, rhad, yn dal atchweliadau mewn CI | Yn colli ~dwy ran o dair o faterion; hyder ffug |
| Profi â llaw + technoleg gynorthwyol | Yn dal rhwystrau defnyddioldeb go iawn | Arafach, angen profwyr a dyfeisiau medrus |
| Profi gyda defnyddwyr anabl | Gwirionedd sylfaenol ar brofiad go iawn | Ymdrech a chost recriwtio, rhaid ei wneud yn barchus |

Y prif gyfaddawd yw disgyblaeth ymlaen llaw yn erbyn cost ohiriedig. Mae hygyrchedd wedi'i adeiladu i mewn yn rhad ac yn gwella ansawdd i bawb; mae hygyrchedd wedi'i ôl-osod dan bwysau cyfreithiol yn ddrud, yn anghyflawn, ac yn straen. Yn y tymor hir nid oes cyfaddawd go iawn yn erbyn "cyflymder": yn syml, nid yw meddalwedd anhygyrch yn gweithio i un rhan o bump o'ch defnyddwyr. Diffyg yw hwnnw, nid arbediad.

## Cwestiynau i'w trafod gyda'ch tîm

1. **A yw atchweliadau hygyrchedd yn methu ein hadeilad yn yr un ffordd â phrawf wedi torri, ac os nad ydynt, pam lai?** Nid yw sganwyr awtomataidd ond yn dal tua thraean o faterion, ond mae'r rhai maen nhw'n eu dal (labeli coll, methiannau cyferbyniad, rheolyddion heb label) yn rhad i'w dal mewn CI ac yn ddrud i'w canfod mewn archwiliad cyn lansio. Trin atchweliad fel methiant adeiladu yw'r hyn sy'n symud hygyrchedd o ymdrech unigol arwrol i briodoledd system ddibynadwy, sef yr unig beth sy'n gweithio pan fydd llawer o dimau'n cyflenwi i mewn i un cynnyrch. Penderfynwch pa wiriadau sy'n rhwystro, pa rai sy'n gynghorol, a phwy sy'n gallu diystyru methiant. Dewch â chanlyniadau eich sganiwr cyfredol a'ch diffiniad o "wedi'i wneud" i'r cyfarfod. Os na chaiff meini prawf hygyrchedd eu hysgrifennu i mewn i'r diffiniad o "wedi'i wneud" fesul stori, byddant yn cael eu dad-flaenoriaethu'r eiliad y bydd terfyn amser yn tynhau.

2. **Beth yw ein rheol ar gyfer teclynnau pwrpasol, a phwy sy'n adolygu'r ARIA cyn iddo gael ei gyflenwi?** Daw elfennau HTML brodorol ag ymddygiad bysellfwrdd a chefnogaeth technoleg gynorthwyol am ddim, ac mae ARIA anghywir yn waeth na dim byd oherwydd ei fod yn camarwain darllenwyr sgrin yn weithredol. Cytunwch mai HTML semantig yw'r rhagosodiad a bod angen taith bysellfwrdd a darllenydd sgrin cyn uno ar unrhyw declyn pwrpasol (dewislen wedi'i deilwra, dewisydd dyddiad, neu fodal), gan ddilyn Arferion Awduro ARIA. Mae hyn yn bwysicaf ar gyfer y cydrannau rhyngweithiol y mae llawer o dimau'n eu hailddefnyddio, oherwydd gall un modal wedi torri gyda thrap bysellfwrdd gau defnyddwyr anabl allan o daith gyfan. Dewch â rhestr o'ch teclynnau pwrpasol a gofynnwch pa rai sydd wedi'u profi gyda darllenydd sgrin go iawn. Mae unrhyw rai nad ydynt wedi bod yn atebolrwydd sy'n cuddio yn eich cod a rennir.

3. **Beth yw ein polisi ar orgaeau hygyrchedd, ac a oes unrhyw un yn credu eu bod yn ateb go iawn?** Mae gorgaeau'n cael eu marchnata fel sgript un-llinell sy'n gwneud safle'n gydymffurfiol, ac maen nhw'n demtasiwn pan ddaw pwysau cyfreithiol a therfyn amser yn nesu. Nid ydynt yn cyflenwi cydymffurfiaeth wirioneddol, gallant waethygu'r profiad i ddefnyddwyr technoleg gynorthwyol, ac i'r llywodraeth maen nhw'n gadael y ddyletswydd gyfreithiol sylfaenol heb ei bodloni. Penderfynwch yn benodol y byddwch yn buddsoddi mewn marcio semantig, cefnogaeth bysellfwrdd, a phrofi gyda phobl anabl yn hytrach na phrynu teclyn sy'n papuro dros y broblem. Dewch â chost tanysgrifiad gorgae a'i gymharu â adeiladu hygyrchedd i mewn i'ch cydrannau a'ch piblinell unwaith. Mae fframio hyn yn gynnar yn atal penderfyniad caffael mewn panig yn ddiweddarach sy'n gwario arian ac yn trwsio dim.

4. **A yw pobl anabl yn rhan o'n dyluniad a'n profi, neu a ydym ni'n dal i ddylunio ar gyfer defnyddiwr dychmygol y buom yn ei ddyfeisio?** Mae sganwyr awtomataidd a hyd yn oed archwiliadau arbenigol yn dweud wrthych a yw'r marcio'n cydymffurfio; nid ydynt yn dweud wrthych a all defnyddiwr dall gwblhau eich talu mewn gwirionedd neu a all person â anabledd gwybyddol ddeall eich negeseuon gwall. Cynnwys cyfranogwyr anabl yw'r unig ffynhonnell gwirionedd sylfaenol, ac mae'n newid yr hyn a adeiladwch, ond mae'n codi cwestiynau go iawn ynghylch sut rydych chi'n recriwtio'n deg, sut rydych chi'n talu pobl am eu hamser, a sut rydych chi'n osgoi trin un cyfranogwr fel llefarydd dros bob anabledd. Dewch â'ch rhestr ymchwil gyfredol, eich arferion recriwtio a thalu, a chyfrif gonest o sawl astudiaeth yn y flwyddyn ddiwethaf a gynhwysodd gyfranogwyr anabl. I sefydliad mawr, panel cylchol gyda thâl teg a chwmpas ar draws anghenion golwg, clyw, symudedd, a gwybyddol yw'r hyn sy'n troi hyn o ystum untro yn fewnbwn dibynadwy; mewn llywodraeth, mae cynnwys y cyhoedd rydych chi'n eu gwasanaethu'n aml yn rhan o'r rhwymedigaeth gyfreithiol a dinesig, nid yn gonfensiwn dewisol.

5. **Pan fyddwn yn prynu neu'n mewnblannu cydran trydydd parti, a ydym yn mynnu prawf o hygyrchedd, a phwy sy'n ei wirio?** Nid yw llawer o'r hyn sy'n cael ei gyflenwi mewn cynnyrch mawr wedi'i ysgrifennu i mewn-tŷ: dewisydd dyddiad o lyfrgell, teclyn taliadau mewn iframe, pecyn siartio, modiwl SaaS cyfan. Gall un gydran anhygyrch wedi'i mewnblannu fethu taith gyfan ni waeth pa mor lân yw eich cod eich hun, ac unwaith y bydd wedi'i weirio i mewn, mae ei ddisodli'n ddrud. Penderfynwch fod hygyrchedd yn ofyniad caffael, bod yn rhaid i werthwyr ddarparu adroddiad cydymffurfiaeth hygyrchedd (dogfen fel VPAT sy'n nodi sut mae cynnyrch yn mesur yn erbyn WCAG), a bod rhywun technegol yn dilysu'r honiad yn hytrach na'i ffeilio. Dewch â rhestr o'ch cydrannau trydydd parti a gofynnwch pa rai sydd â thystiolaeth gydymffurfiaeth gyfredol a chredadwy. Mewn caffael menter a llywodraeth, ysgrifennwch gydymffurfiaeth WCAG 2.2 AA a hawl i unioni i mewn i'r contract, oherwydd mae addewid a wnaed cyn llofnodi'n llawer rhatach i'w orfodi na rhwystr a ddarganfyddir ar ôl mynd yn fyw.

6. **Beth yw ein lefel gydymffurfiaeth darged, pwy sy'n ei pherchen, a sut rydym yn ei chadw'n gyfredol wrth i safonau symud?** WCAG 2.2 AA yw'r llawr heddiw ac mae'r rhan fwyaf o gyfreithiau'n cyfeirio ato, ond ychwanegodd 2.2 feini prawf nad yw llawer o dimau wedi'u mabwysiadu, ac mae WCAG 3.0 ar y ffordd gyda strwythur gwahanol. Heb berchennog penodedig, mae'r safon yn drifftio: mae timau gwahanol yn targedu fersiynau gwahanol, nid oes neb yn olrhain y bwlch, ac mae cydymffurfiaeth yn pydru'n dawel rhwng archwiliadau. Penderfynwch yn union pa fersiwn a lefel rydych chi'n adeiladu iddynt, pwy sydd ag awdurdod i'w chodi, a sut mae meini prawf newydd yn cyrraedd y system ddylunio a'r diffiniad o "wedi'i wneud". Dewch â'ch targed datganedig cyfredol, tystiolaeth o ble mae timau'n ei fodloni mewn gwirionedd, a map ffordd byr ar gyfer mabwysiadu meini prawf 2.2 rydych chi wedi'u hepgor. I sefydliad mawr neu gyhoeddus, mae perchennog hygyrchedd neu ganolfan ragoriaeth, datganiad hygyrchedd cyhoeddedig, a chynllun dogfennedig ar gyfer y fersiwn safonol nesaf yn beth sy'n eich galluogi i ateb rheoleiddiwr neu lys gyda thystiolaeth yn hytrach na bwriadau da.

## Lens sector

**Cwmni newydd.** Mae cyflymder o'ch plaid yma, oherwydd mae hygyrchedd rataf pan fydd y sylfaen god yn fach. Ychwanegwch sganiwr awtomataidd i CI a thaith bysellfwrdd i'ch rhestr wirio cais tynnu o'r sbrint gyntaf, a phwyswch ar HTML semantig fel eich bod yn cael cefnogaeth bysellfwrdd a darllenydd sgrin am ddim. Hepgorwch orgaeau ac offer trwm; y wobr yw, pan fydd tîm caffael cwsmer yn gofyn am adroddiad cydymffurfiaeth ganol gwerthiant, y gallwch ateb mewn diwrnodau yn lle sgramblo.

**Busnes bach.** Heb arbenigwr hygyrchedd a chyllideb dynn, prynwch hygyrchedd yn hytrach na'i adeiladu: dewiswch blatfform, thema, neu lyfrgell cydrannau sydd eisoes yn cydymffurfio ac yn datgan hynny, a ffafriwch werthwyr sy'n cyhoeddi datganiad hygyrchedd. Ymdriniwch â'r pethau sylfaenol gwerth uchel eich hun gydag offer am ddim, gwiriadau bysellfwrdd-yn-unig, gwiriwr cyferbyniad, a labeli clir ar bob maes, oherwydd bod y rheiny'n dal y methiannau sydd amlaf yn eithrio cwsmeriaid. Triniwch lif awtomataidd anghywir neu anniddefnyddiadwy fel cwsmer coll, gan fod busnes bach yn brin o gynnig sianel gynorthwyol i syrthio'n ôl arni.

**Menter.** Ar raddfa, y gwaith yw gwneud hygyrchedd yn briodoledd system ar draws llawer o dimau. Cyflenwch gydrannau hygyrch yn ddiofyn yn y system ddylunio, giatiwch atchweliadau yn CI, a sefydlwch berchennog neu ganolfan ragoriaeth gyda phroses unioni a hyfforddiant ar gyfer dylunwyr, peirianwyr, ac awduron cynnwys. Olrheinwch gydymffurfiaeth dros amser fel metrig, ysgrifennwch gydymffurfiaeth WCAG i mewn i gaffael, a rheolwch gydrannau trydydd parti fel portffolio fel na all un teclyn wedi'i fewnblannu fethu taith a rennir yn dawel.

**Llywodraeth.** Mae hygyrchedd yn fandad cyfreithiol ac yn ddyletswydd ddinesig, gan nad oes gan ddinasyddion anabl yn aml ddarparwr amgen ar gyfer budd-dal, trwydded, neu bleidlais. Adeiladwch yn ôl y safon y mae eich awdurdodaeth yn ei chyfeirio (er enghraifft Section 508, EN 301 549, neu'r European Accessibility Act wedi'i fapio i WCAG 2.2 AA), cyhoeddwch ddatganiad hygyrchedd gyda llwybr i adrodd ar rwystrau, a phrofwch gyda'r cyhoedd anabl rydych chi'n eu gwasanaethu. Gwrthodwch orgaeau fel dirprwy dros gydymffurfiaeth wirioneddol, a mynnwch fod gwerthwyr yn darparu tystiolaeth gredadwy a hawl i unioni yn y contract.

## Enghreifftiau

**Cwmni newydd.** Ychwanegodd cwmni newydd tri pherson yn adeiladu offeryn recriwtio sganiwr hygyrchedd i'w hadeilad a thaith bysellfwrdd gyflym i'w rhestr wirio cais tynnu o'r sbrint gyntaf un, gan resymu ei bod yn rhatach aros yn hygyrch na'i drwsio'n ddiweddarach. Pan ofynnodd tîm caffael cwsmer maint canolig am adroddiad cydymffurfiaeth hygyrchedd yn ystod cylch gwerthu, roedd y cwmni newydd eisoes yn defnyddio HTML semantig, wedi labelu pob maes, a chanddo ffocws gweladwy ym mhobman, felly atebasant mewn diwrnodau yn lle sgramblo. Enillodd y parodrwydd hwnnw fargen a gollodd cystadleuydd ar yr un gofyniad.

**Menter.** Wynebodd manwerthwr mawr achos cyfreitha dosbarth oherwydd na allai cwsmeriaid dall gwblhau talu gyda darllenydd sgrin. Y tu hwnt i'r setliad a'r ffioedd cyfreithiol, bu'n rhaid i'r cwmni unioni o dan amserlen a oruchwyliwyd gan lys. Wedi hynny ailadeiladodd hygyrchedd i mewn i'w system ddylunio a'i biblinell CI, ychwanegodd brofi darllenydd sgrin i'r diffiniad o "wedi'i wneud", a hyfforddodd ei dimau. Gwellodd y broses dalu wedi'i hailadeiladu, hygyrch drosiad hefyd a lleihaodd gysylltiadau cymorth i bawb: helpodd y trwsiadau a helpodd ddefnyddwyr darllenydd sgrin (labeli clir, negeseuon gwall, trefn resymegol) bob defnyddiwr.

**Llywodraeth.** Roedd gofyn yn gyfreithiol i asiantaeth budd-daliadau cyhoeddus fodloni WCAG 2.1 AA ar gyfer ei chais ar-lein. Datgelodd profi cynnar gyda defnyddwyr dall a golwg isel, defnyddwyr bysellfwrdd-yn-unig, a defnyddwyr â anableddau gwybyddol fod dangosydd "maes gofynnol" lliw-yn-unig, dewisydd dyddiad anhygyrch, a gwallau dilysu heb eu cyhoeddi yn rhwystro pobl rhag gorffen. Roedd trwsio'r rhain, trwy farcio semantig, ffocws gweladwy, cyhoeddiadau gwall rhanbarth byw, a chymorth [iaith blaen](https://en.wikipedia.org/wiki/Plain_language), yn galluogi dinasyddion anabl i wneud cais ar eu pen eu hunain am y tro cyntaf. Lleihaodd hynny'r dibyniaeth ar gymorth wyneb yn wyneb a gostyngodd y gost o wasanaethu, tra'n bodloni'r mandad cyfreithiol.

## Achos busnes: cymhellion, ROI, a TCO

Mae'r achos busnes yn dibynnu ar gyrhaeddiad marchnad, risg gyfreithiol, cost gwasanaethu, ac ansawdd. Mae gan bobl anabl a'u teuluoedd bŵer gwariant sylweddol; mae eu heithrio yn ei golli. Mae gwasanaethau hygyrch yn lleihau'r angen am sianeli cynorthwyol drud (cymorth ffôn a wyneb yn wyneb), sy'n arbediad gweithredol uniongyrchol, yn enwedig ar gyfer llywodraeth. Ac oherwydd bod gwelliannau hygyrchedd (labeli clir, cefnogaeth bysellfwrdd, cynnwys darllenadwy, marcio cadarn) yn helpu pawb, maen nhw fel arfer yn codi cwblhad a boddhad cyffredinol.

O ran TCO, mae'r gost fabwysiadu yn hyfforddiant, offer, ac adeiladu hygyrchedd i mewn i gydrannau a phiblinellau, y cyfan yn gymedrol pan fyddwch chi'n ei wneud o'r cychwyn. Mae'r gost o beidio â mabwysiadu'n ddifrifol ac yn dod o sawl cyfeiriad: atebolrwydd cyfreithiol (achosion cyfreithiol, setliadau, unioni a orchmynnwyd gan lys, cosbau rheoleiddiol), y gost lawer uwch o ôl-osod dan bwysau terfyn amser, niwed i enw da, a chost barhaus gwasanaethu defnyddwyr sydd wedi'u heithrio trwy sianeli drutach. Mae ôl-osod fel arfer yn costio sawl gwaith yn fwy na phe bai wedi'i ddylunio i mewn.

I wneud yr achos i arweinyddiaeth, arweiniwch gyda'r rhwymedigaeth gyfreithiol lle mae'n berthnasol (mae'n anemwn i lywodraeth ac yn gynyddol i'r sector preifat). Yna mesurwch y boblogaeth y gellir ei chyrraedd rydych chi'n ei heithrio, cost sianel gynorthwyol yr eithrio hwnnw, ac enillion "ymyl gostwng" i bob defnyddiwr. Safleuwch hygyrchedd fel rheoli risg ynghyd ag ansawdd, nid elusen.

## Gwrth-batrymau a pheryglon

- **Hygyrchedd fel blwch ticio cyn-lansio**: archwiliad ar y diwedd yn lle arfer parhaus, gan warantu ailweithio drud munud olaf.
- **"Cawl div"**: marcio anseantig gyda thrinwyr clicio ar elfennau generig, yn anweledig i dechnoleg gynorthwyol.
- **Camddefnydd ARIA**: bolltio ARIA ar farcio wedi torri, sy'n camarwain darllenwyr sgrin yn fwy na marcio plaen.
- **Gwybodaeth lliw-yn-unig**: statws yn cael ei ddangos gan liw yn unig, yn anweledig i ddefnyddwyr dall lliw.
- **Ffocws anweledig**: tynnu amlinellau ffocws er mwyn estheteg, gan adael defnyddwyr bysellfwrdd yn sownd.
- **Trapiau bysellfwrdd**: modalau a theclynnau sy'n dal neu'n colli ffocws.
- **Hunanfodlonrwydd sgan awtomataidd**: pasio sganiwr a chymryd yn ganiataol bod y cynnyrch yn hygyrch.
- **Gorgaeau hygyrchedd**: teclynnau "trwsiad un-llinell" trydydd parti nad ydynt yn cyflenwi cydymffurfiaeth wirioneddol a all waethygu'r profiad.
- **Eithrio defnyddwyr anabl o ymchwil**: dylunio ar gyfer defnyddiwr anabl dychmygol yn lle profi gyda rhai go iawn.

## Model aeddfedrwydd

**Lefel 1: Cychwyn.** Dim arfer hygyrchedd. Ni ddarganfyddir materion ond pan fydd defnyddiwr yn cwyno neu achos cyfreithiol yn cyrraedd, ac mae'r ymateb yn adweithiol. Mae'r marcio'n anseantig ac heb ei brofi, ac nid oes neb yn berchen ar y broblem.

**Lefel 2: Datblygu.** Mae ymwybyddiaeth yn bodoli ac mae rhai timau'n gweithredu arni: sganiwr awtomataidd mewn adeilad fan hyn, taith bysellfwrdd fan draw, archwiliad cyn-lansio cyn rhyddhad mawr. Mae'r arfer yn sylfaenol ac yn anghyson ar draws timau, mae hygyrchedd yn dal yn rhestr wirio cam-hwyr, ac fe'i dad-flaenoriaethir yn aml o dan bwysau amserlen.

**Lefel 3: Safoni.** WCAG 2.2 AA yw'r safon ddogfennedig, wedi'i gorfodi ar draws y sefydliad. Mae hygyrchedd wedi'i adeiladu i mewn i'r system ddylunio fel bod cydrannau'n cael eu cyflenwi'n hygyrch yn ddiofyn, wedi'i brofi'n awtomataidd ac â llaw, ac wedi'i ysgrifennu i mewn i'r diffiniad o "wedi'i wneud". Mae timau'n cael eu hyfforddi, mae perchennog neu ganolfan ragoriaeth yn bodoli, ac mae proses unioni wedi'i diffinio.

**Lefel 4: Rheoli.** Mae hygyrchedd yn cael ei fesur a'i reoli gyda data yn erbyn llinellau sylfaen. Mae'r sefydliad yn olrhain metrigau cydymffurfiaeth dros amser (cyfraddau pasio sganiwr, cyfrif rhwystrau agored fesul difrifoldeb, cwmpas profi darllenydd sgrin o deithiau critigol, ac amser-i-unioni), yn eu hadrodd fesul tîm ar ddangosfwrdd, ac yn trin atchweliadau fel methiannau adeiladu yn hytrach na rhybuddion cynghorol. Gosodir targedau yn erbyn llinell sylfaen ac adolygir cynnydd, fel bod tîm sy'n llithro'n weladwy cyn i archwiliad ei ganfod.

**Lefel 5: Cydgysylltu.** Mae hygyrchedd yn cael ei wella a'i integreiddio'n barhaus ar draws y sefydliad. Mae pobl anabl yn rhan o ymchwil a phrofi ar sail gylchol, ac mae hygyrchedd wedi'i ymgorffori mewn caffael, tocynnau dylunio, a CI. Mae'r sefydliad yn addasu wrth i safonau symud (mabwysiadu meini prawf WCAG newydd a pharatoi ar gyfer WCAG 3.0), ac mae'n dylanwadu ar werthwyr a phartneriaid fel bod y gadwyn gyflenwi gyfan yn cydymffurfio.

## Syniadau ar gyfer trafodaeth

- Sut rydych chi'n cadw hygyrchedd rhag cael ei ddad-flaenoriaethu pan fydd terfynau amser yn tynhau?
- Beth yw'r cymysgedd cywir o brofi awtomataidd, â llaw, a defnyddiwr ar gyfer eich proffil risg?
- Sut ddylai cydymffurfiaeth hygyrchedd gael ei ysgrifennu i mewn i gontractau gwerthwyr a chaffael?
- Sut rydych chi'n ymdrin â'r bwlch rhwng cydymffurfiaeth WCAG a defnyddioldeb gwirioneddol i bobl anabl?
- Sut ddylai timau baratoi ar gyfer WCAG 3.0 tra'n adeiladu yn ôl 2.2 heddiw?
- Sut rydych chi'n recriwtio a thalu cyfranogwyr anabl yn deg ac yn barchus ar gyfer ymchwil?

## Prif gasgliadau

- Mae hygyrchedd yn briodoledd ansawdd sylfaenol ac, i lywodraeth, yn ofyniad cyfreithiol.
- Dylunio yn ôl WCAG 2.2 AA fel llawr; defnyddio'r egwyddorion POUR fel model meddyliol.
- HTML semantig yn gyntaf; ARIA dim ond i lenwi bylchau go iawn, wedi'i wneud yn gywir.
- Mae teclynnau awtomataidd yn dal tua thraean o faterion; mae profi â llaw a thechnoleg gynorthwyol yn hanfodol.
- Profi gyda phobl anabl, nid dim ond ar eu cyfer.
- Mae adeiladu hygyrchedd i mewn yn rhad ac yn barhaus; mae ôl-osod yn ddrud ac yn fregus.
- Mae dyluniad hygyrch yn ddyluniad gwell i bawb: mae'r effaith ymyl gostwng yn wirioneddol.

## Cyfeiriadau a darllen pellach

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2* a dogfennau Understanding/Techniques ategol
- W3C, *WAI-ARIA Authoring Practices Guide*
- Deunyddiau cyflwyniadol a thiwtorial Menter Hygyrchedd Gwe W3C (WAI)
- Laura Kalbag, *Accessibility for Everyone*
- Sarah Horton a Whitney Quesenbery, *A Web for Everyone*
- Regine Gilbert, *Inclusive Design for a Digital World*
- Safonau Section 508 yr UD a chanllawiau Section508.gov
- Safon Ewropeaidd EN 301 549 a'r European Accessibility Act
- Canllawiau hygyrchedd llywodraeth (e.e. llawlyfr hygyrchedd UK GDS)
- WebAIM, ymchwil ac erthyglau gan gynnwys y dadansoddiadau hygyrchedd blynyddol
