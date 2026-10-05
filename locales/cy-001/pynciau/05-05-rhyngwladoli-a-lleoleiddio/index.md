# 5.5 Rhyngwladoli a lleoleiddio

## Trosolwg a chymhelliant

[Rhyngwladoli](https://en.wikipedia.org/wiki/Internationalization_and_localization) (i18n) yw'r gwaith peirianneg o adeiladu meddalwedd fel y gellir ei haddasu i unrhyw iaith, rhanbarth, a diwylliant heb newid y cod. Lleoleiddio (l10n) yw'r gwaith sy'n dilyn: addasu cynnyrch mewn gwirionedd ar gyfer locale penodol trwy gyfieithu testun, fformatio dyddiadau a rhifau, addasu cynllun, ac ystyried disgwyliadau diwylliannol. Mae'r ddau'n wahanol. Gwneir rhyngwladoli unwaith, yn y bensaernïaeth. Gwneir lleoleiddio sawl gwaith, yn y cynnwys. Ewch â'r bensaernïaeth yn iawn ymlaen llaw a bydd pob lleoleiddio'n rhad. Ei chael yn anghywir a bydd pob un yn dod yn ôl-osodiad poenus, tueddol o gamgymeriadau.

I dimau mawr, mae i18n yn benderfyniad pensaernïol sylfaenol. Mae'n cyffwrdd â phob haen: storio data, trin llinynnau, cynllun, a phiblinellau cynnwys. Os na wnewch chi ei sefydlu'n gynnar a'i orfodi trwy lyfrgelloedd a rennir a rheolau lint, bydd timau'n codio llinynnau Saesneg yn galed, yn cyfuno darnau wedi'u cyfieithu, ac yn tybio sgriptiau Lladin. Rhaid dadwneud y ddyled honno cyn y gall y cynnyrch fynd i mewn i unrhyw farchnad newydd. Mae fframwaith i18n a rennir a llif gwaith lleoleiddio'n gadael i ddwsinau o dimau ryddhau cynnyrch mewn llawer o ieithoedd heb i bob un ailddyfeisio'r plymwaith.

Mae perthnasedd menter a llywodraeth yn uniongyrchol. Rhaid i fentrau rhyngwladol wasanaethu cwsmeriaid a gweithwyr ar draws gwledydd, ieithoedd, a threfnau rheoleiddiol. Rhaid i lywodraethau wasanaethu poblogaethau amrywiol yn ieithyddol. Mae llawer o wledydd yn swyddogol amlieithog, ac mae'n ofynnol yn gyfreithiol i lawer ddarparu gwasanaethau mewn ieithoedd lluosog, gan gynnwys sgriptiau [de-i-chwith](https://en.wikipedia.org/wiki/Bidirectional_text) ac ieithoedd brodorol neu leiafrifol. I wasanaethau cyhoeddus, mater tegwch a chyfreithiol yw mynediad iaith: mae dinesydd na all ddarllen yr unig iaith sydd ar gael i bob pwrpas yn cael ei wadu'r gwasanaeth.

## Egwyddorion allweddol

- Rhyngwladolwch y bensaernïaeth unwaith; lleoleiddiwch y cynnwys sawl gwaith.
- Peidiwch byth â chodio testun sy'n wynebu defnyddwyr yn galed; allanoli pob llinyn i adnoddau a reolir.
- Defnyddiwch [Unicode](https://en.wikipedia.org/wiki/Unicode) (UTF-8) ym mhobman; tybiwch y gall testun fod mewn unrhyw sgript.
- Peidiwch byth â chyfuno darnau wedi'u cyfieithu; mae gramadeg a threfn geiriau'n wahanol yn ôl iaith.
- Cynlluniwch ar gyfer ehangu testun, sgriptiau de-i-chwith, a rheolau lluosog a chenedl cymhleth.
- Fformatiwch ddyddiadau, rhifau, arian cyfred, ac enwau yn ôl locale, nid cod.
- Gwahanwch gynnwys y gellir ei gyfieithu oddi wrth god fel na fydd cyfieithwyr byth yn cyffwrdd â'r ffynhonnell.
- Mae lleoleiddio'n ddiwylliannol, nid dim ond ieithyddol: mae lliwiau, delweddaeth, ac enghreifftiau'n bwysig.

## Argymhellion

### Adeiladu pensaernïaeth rhyngwladoli gadarn

Storiwch a phroseswch bob testun fel Unicode (UTF-8) o ben i ben (cronfa ddata, API, a rhyngwyneb) fel y gellir cynrychioli unrhyw sgript. Allanolwch bob llinyn sy'n wynebu defnyddwyr i ffeiliau adnoddau neu gatalog negeseuon wedi'i allweddu gan ddynodwr, byth wedi'i fewnblannu mewn cod neu farcio. Cynrychiolwch locale fel iaith ynghyd â rhanbarth (a sgript lle bo angen) fel y gallwch wahaniaethu, er enghraifft, rhwng amrywiadau un iaith ar draws gwledydd. Cadwch resymeg fformatio mewn llyfrgell rhyngwladoli sydd wedi'i phrofi'n dda yn hytrach na llunio fformatio dyddiad, rhif, ac arian cyfred â llaw. Storiwch ddata mewn ffurfiau niwtral, diamwys (stampiau amser UTC, codau gwlad ac arian cyfred ISO, unedau sylfaenol) a fformatiwch dim ond yn yr haen gyflwyno.

### Trin cymhlethdod iaith yn gywir

Peidiwch â thybio hyd testun; caniatewch le hael oherwydd mae cyfieithiadau'n aml yn llawer hirach na Saesneg, a dyluniwch gynlluniau sy'n ailffrydio yn hytrach na thocio neu orgyffwrdd. Cefnogwch sgriptiau dwyffyrdd (de-i-chwith) trwy ddefnyddio priodweddau cynllun rhesymegol yn hytrach na ffisegol a drychu'r rhyngwyneb lle bo hynny'n briodol. Defnyddiwch reolau lluosog y locale trwy eich llyfrgell i18n (mae gan ieithoedd rhwng un a chwe ffurf luosog) yn lle rhesymeg unigol/lluosog naïf. Trinwch genedl a chytundeb gramadegol lle mae'r iaith yn ei fynnu. Peidiwch byth ag adeiladu brawddegau trwy gyfuno; defnyddiwch dempledi negeseuon llawn, paramedredig fel bod cyfieithwyr yn rheoli trefn geiriau.

### Sefydlu llif gwaith lleoleiddio a rheoli cyfieithu

Trinwch leoleiddio fel piblinell barhaus, nid swp cyn-lansio. Echdynnwch linynnau'n awtomatig, gwthiwch nhw i [system rheoli cyfieithu](https://en.wikipedia.org/wiki/Translation_management_system), a thynnwch gyfieithiadau wedi'u cwblhau'n ôl, gorau po fwyaf wedi'u hintegreiddio â CI fel bod llinynnau newydd yn cael eu fflagio a fersiynau wedi'u lleoleiddio'n aros mewn cydamseriad. Rhowch gyd-destun i gyfieithwyr: lluniau sgrin, disgrifiadau, terfynau nod, a geirfa a chanllaw arddull fesul iaith i gadw terminoleg a thôn yn gyson. Defnyddiwch [gof cyfieithu](https://en.wikipedia.org/wiki/Translation_memory) i ailddefnyddio gwaith blaenorol a thorri cost. Penderfynwch yn fwriadol lle mae [cyfieithu peirianyddol](https://en.wikipedia.org/wiki/Machine_translation) yn dderbyniol (cynnwys risg isel, cyfaint uchel) a lle mae angen cyfieithu ac adolygu dynol (cyfreithiol, meddygol, diogelwch, hollbwysig i frand). [Ffug-leoleiddiwch](https://en.wikipedia.org/wiki/Pseudolocalization) yn gynnar, gan ddisodli llinynnau â lleoliadau wedi'u hymestyn, acennog, i ddal llinynnau wedi'u codio'n galed, tocio, a namau amgodio cyn i gyfieithu go iawn ddechrau.

### Lleoleiddio fformatau, diwylliant, a chynnwys, nid dim ond geiriau

Fformatiwch ddyddiadau, amseroedd, rhifau, arian cyfred, cyfeiriadau, rhifau ffôn, ac enwau fesul locale, gan barchu confensiynau lleol (trefn dyddiad, gwahanyddion degol a grwpio, lleoliad arian cyfred, trefn enwau). Addaswch ddelweddaeth, eiconau, lliwiau, enghreifftiau, a throsiadau i ystyr diwylliannol lleol, gan fod symbolau a lliwiau'n cario cysylltiadau gwahanol ar draws diwylliannau. Ystyriwch wahaniaethau cynnwys cyfreithiol a rheoleiddiol lleol. Gwahaniaethwch rhwng cysondeb byd-eang (brand, swyddogaeth graidd) ac addasiad rhanbarthol (cynnwys, enghreifftiau, cydymffurfiaeth) a phenderfynwch yn eglur pa elfennau sy'n sefydlog a pha rai sy'n hyblyg.

### Llywodraethu i18n fel seilwaith a rennir

Darparwch lyfrgell i18n a rennir, rheolau lint allanoli llinynnau, a mecanwaith datrys locale safonol fel na all timau godio testun yn galed ar ddamwain. Sefydlwch berchnogaeth ar y biblinell leoleiddio a geirfaoedd. Profwch mewn locales lluosog yn CI, gan gynnwys locale de-i-chwith a ffug-locale testun hir, fel bod atchweliadau'n cael eu dal yn awtomatig.

## Cyfaddawdau: manteision ac anfanteision

| Penderfyniad | Manteision | Anfanteision |
|---|---|---|
| Rhyngwladoli o'r diwrnod cyntaf | Mynediad marchnad rhad yn ddiweddarach, dim ôl-osod | Cost ymlaen llaw hyd yn oed cyn bod angen ail locale |
| Ôl-osod i18n yn ddiweddarach | Gohirio cost os yw'r angen byd-eang yn ansicr | Drud a pheryglus iawn i ddadwneud rhagdybiaethau wedi'u codio'n galed |
| Cyfieithu dynol | Ansawdd uchel, cywir yn ddiwylliannol | Arafach a mwy costus |
| Cyfieithu peirianyddol | Cyflym, rhad, yn graddio i gyfaint enfawr | Risg ansawdd a chywirdeb; anaddas ar gyfer cynnwys risg uchel |
| Piblinell leoleiddio barhaus | Mae locales yn aros mewn cydamseriad, dim gwasgfa lansio | Buddsoddiad offer a phroses |
| Addasiad diwylliannol dwfn fesul rhanbarth | Ffit ac ymddiriedaeth leol well | Mwy o amrywiadau cynnwys i'w hadeiladu a'u cynnal |

Y cyfaddawd tyngedfennol yw pryd i fuddsoddi mewn rhyngwladoli. Mae ôl-osod i18n i mewn i gynnyrch sy'n llawn cod wedi'i godio'n galed, wedi'i gyfuno, sy'n tybio Lladin yn un o'r ffurfiau mwyaf drud o ddyled dechnegol i'w had-dalu. I unrhyw sefydliad ag uchelgeisiau rhyngwladol neu amlieithog credadwy, sy'n cynnwys i bob pwrpas pob menter fawr a llywodraeth amlieithog, mae rhyngwladoli'r bensaernïaeth yn gynnar yn llawer rhatach nag ôl-osod, er bod yr elw wedi'i ohirio.

## Cwestiynau i'w trafod gyda'ch tîm

1. **A ydym yn gorfodi allanoli llinynnau â rheolau lint, ac a yw ffug-leoleiddio'n rhedeg yn CI cyn unrhyw gyfieithu go iawn?** Mae'r ddyled sy'n gwneud rhyngwladoli'n ddrud (llinynnau Saesneg wedi'u codio'n galed, darnau brawddeg wedi'u cyfuno, rhagdybiaethau sgript Lladin) yn cronni'n dawel oni bai bod offer yn ei atal ar adeg ymrwymo. Mae rheolau lint sy'n fflagio testun defnyddiwr wedi'i godio'n galed, ynghyd â ffug-locale testun hir, acennog yn rhedeg yn CI, yn dal tocio, gorgyffwrdd, a namau amgodio tra eu bod yn rhad i'w trwsio. Dyma'r hyn sy'n gadael i ddwsinau o dimau ryddhau un cynnyrch mewn llawer o ieithoedd heb i bob un ailddyfeisio'r plymwaith na dadwneud rhagdybiaethau ar ddyddiad cau'n ddiweddarach. Dewch â chwiliad am linynnau wedi'u codio'n galed a gofynnwch a allai unrhyw dîm ryddhau un ar ddamwain heddiw. Os na fyddai dim yn y biblinell yn ei ddal, dyna'r bwlch i'w gau gyntaf.

2. **Lle rydym yn storio data canonaidd, ac a yw fformatio wedi'i gyfyngu i'r haen gyflwyno?** Mae storio stampiau amser fel UTC, gwledydd ac arian cyfred fel codau ISO, a symiau mewn unedau sylfaenol yn golygu y gall unrhyw locale eu fformatio'n gywir wrth yr ymyl, tra bo rhesymeg fformatio wedi'i phobi i mewn i'r haen ddata'n cynhyrchu namau sy'n boenus i'w dadwneud. Cytunwch fod dyddiadau, rhifau, arian cyfred, cyfeiriadau, ac enwau'n cael eu fformatio dim ond wrth gyflwyno, trwy lyfrgell sydd wedi'i phrofi'n dda yn hytrach na chod wedi'i lunio â llaw. Mae hyn yn bwysig i fentrau rhyngwladol a llywodraethau amlieithog lle mae'n rhaid i ddinesydd weld trefn dyddiad gywir, gwahanyddion degol, a threfn enwau yn ei gonfensiwn ei hun. Dewch ag enghraifft o werth y mae eich system yn ei storio eisoes wedi'i fformatio ac olrheiniwch beth sy'n torri pan fydd locale newydd ei angen yn wahanol. Os yw data a chyflwyniad wedi'u clymu, penderfynwch sut rydych chi'n eu datod cyn ychwanegu locales.

3. **Ble'n union mae cyfieithu peirianyddol yn dderbyniol, a sut mae ein piblinell leoleiddio'n cael ei chadw'n barhaus yn hytrach na swp?** Mae cyfieithu peirianyddol yn gyflym ac yn rhad ar gyfer cynnwys risg isel, cyfaint uchel ond yn anaddas ar gyfer testun cyfreithiol, meddygol, diogelwch, neu hollbwysig i frand lle mae camgyfieithiad yn achosi niwed go iawn, felly mae angen i'r ffin fod yn bolisi eglur, nid dyfaliad fesul tîm. Yn yr un modd, mae trin lleoleiddio fel swp cyn-lansio'n gwarantu gwasgfa gyfieithu, tra bo echdynnu llinynnau'n awtomatig a chydamseru trwy system rheoli cyfieithu'n cadw pob locale yn gyfredol. Penderfynwch pwy sy'n berchen ar y biblinell, y geirfaoedd, a'r porth adolygu dynol ar gyfer llinynnau risg uchel. Dewch â rhyddhad diweddar a gofynnwch pa mor hir y cymerodd ei linynnau newydd i ymddangos ym mhob iaith. Os yw locales yn crwydro allan o gydamseriad rhwng rhyddhadau, mae eich piblinell yn swp mewn cuddwisg.

4. **A ydym yn profi locale de-i-chwith a ffug-locale testun hir yn awtomatig, neu a ydym yn tawel dybio sgriptiau Lladin a chynlluniau hyd-Saesneg?** Cefnogaeth ddwyffyrdd (de-i-chwith) ac ehangu testun yw'r rhagdybiaethau sy'n torri fwyaf gweladwy mewn marchnad newydd: rhyngwynebau drych na chawsant erioed eu drychu, a botymau sy'n tocio unwaith y bydd Almaeneg neu Ffinneg yn rhedeg ddeugain y cant yn hirach na Saesneg. Y tyniad sy'n cystadlu yw cyflymder, gan fod adeiladu ar briodweddau cynllun rhesymegol yn hytrach na ffisegol a gwifro ffug-locale acennog i mewn i integreiddio parhaus (CI) yn costio ymdrech cyn bod unrhyw gwsmer go iawn ei angen. Dewch â llun sgrin o'ch sgriniau prysuraf wedi'u rendro mewn locale de-i-chwith ac mewn ffug-locale wedi'i ymestyn, a chyfrwch yr gorgyffyrddiadau, labeli wedi'u torri, a saethau sownd. I fenter ryngwladol neu lywodraeth y mae'n ofynnol yn gyfreithiol iddi wasanaethu iaith de-i-chwith neu leiafrifol, nid diffyg cosmetig yw cynllun na all ddrychu, mae'n farchnad neu'n rhwymedigaeth statudol na allwch ei bodloni heb ailadeiladu.

5. **Pa rannau o'r cynnyrch sy'n sefydlog yn fyd-eang a pha rai sy'n hyblyg yn ôl rhanbarth, a phwy sydd â'r awdurdod i benderfynu?** Mae lleoleiddio'n ddiwylliannol, nid dim ond ieithyddol, felly gall lliwiau, delweddaeth, enghreifftiau, teitlau anrhydeddus, a hyd yn oed pa nodweddion a gynigir amrywio yn ôl marchnad, ac eto mae pob amrywiad rhanbarthol rydych yn ei ganiatáu'n arteffact arall i'w adeiladu, ei gyfieithu, ei adolygu, a'i gynnal am byth. Y tensiwn yw rhwng ffit lleol, sy'n adeiladu ymddiriedaeth a throsi, a chysondeb, sy'n cadw'r brand yn gydlynol a'r baich cynnal a chadw'n gyfyngedig. Dewch â rhestr bendant o'r hyn y byddai locale newydd arfaethedig yn ei newid y tu hwnt i linynnau wedi'u cyfieithu, a phrisiwch gynhaliaeth barhaus pob amrywiad, nid dim ond ei adeiladu cyntaf. Mewn menter fawr mae angen perchennog wedi'i enwi ar y penderfyniad hwn fel na all timau rhanbarthol fforchio'r cynnyrch ad hoc, ac mewn llywodraeth rhaid iddo barchu rheolau cynnwys cyfreithiol a hygyrchedd sy'n amrywio yn ôl awdurdodaeth ac nad ydynt yn ddewisol.

6. **I ba locales rydym yn ymrwymo mewn gwirionedd, sut rydym yn cadw terminoleg yn gyson ar eu traws, a pha dystiolaeth sy'n gyrru'r rhestr honno?** Mae ychwanegu iaith yn hawdd ei addo ac yn ddrud i'w gynnal, oherwydd mae angen geirfa, canllaw arddull, adolygiad dynol ar gyfer llinynnau risg uchel, a thrin lluosog a chenedl cywir y mae rhesymeg unigol-neu-luosog naïf yn ei gael yn anghywir yn y rhan fwyaf o ieithoedd. Yr ystyriaethau sy'n cystadlu yw cyrhaeddiad yn erbyn cost: gall marchnad neu boblogaeth a wasanaethir yn wael fod yn waeth nag un na wasanaethir o gwbl. Dewch â'r boblogaeth neu'r incwm y tu ôl i bob locale ymgeisiol, y sylw rheolau lluosog a fformatio y mae eich llyfrgell yn ei ddarparu ar ei gyfer, a phwy sy'n berchen ar ei eirfa. I fenter ryngwladol, y gyrrwr yw marchnad y gellir ei chyrraedd a chost cymorth fesul iaith, tra i lywodraeth mae'n rhwymedigaeth mynediad iaith gyfreithiol a thegwch, wedi'i feintioli gan nifer y trigolion sydd ond yn gallu trafod yn yr iaith honno.

## Trwy lygaid pob sector

**Busnes newydd.** Gwnewch y dewisiadau pensaernïol rhad ar y diwrnod cyntaf a stopiwch yno: UTF-8 o ben i ben, pob llinyn sy'n wynebu defnyddwyr mewn catalog negeseuon, a dyddiadau, rhifau, ac arian cyfred wedi'u fformatio trwy lyfrgell ymwybodol o locale. Mae'r rhain bron yn ddi-gost tra byddwch yn rhyddhau mewn un iaith ac yn arbed ailysgrifennu pan fydd eich cwsmer mawr cyntaf eisiau ail iaith. Peidiwch â chodi piblinell gyfieithu na chefnogi locales nad oes neb yn talu amdanynt eto; cadwch y drws ar agor, nid y tŷ cyfan wedi'i ddodrefnu.

**Busnes bach.** Heb arbenigwr rhyngwladoli a chyllideb dynn, pwyswch ar y nodweddion i18n sydd eisoes yn eich fframwaith a gwasanaeth rheoli cyfieithu wedi'i westeio yn hytrach nag adeiladu piblinellau eich hun. Defnyddiwch gyfieithu peirianyddol ar gyfer cynnwys risg isel, cyfaint uchel a thalwch am gyfieithu dynol dim ond lle byddai camgymeriad yn costio cwsmer i chi neu'n torri rheol, fel testun cyfreithiol, diogelwch, neu filio. Ymrwymwch i locale dim ond pan fydd marchnad benodol yn cyfiawnhau'n glir y gost gyfieithu ac adolygu barhaus.

**Menter.** Y broblem yw llywodraethu ar draws llawer o dimau: llyfrgell i18n a rennir, rheolau lint sy'n gwrthod llinynnau wedi'u codio'n galed, piblinell leoleiddio barhaus gyda chof cyfieithu a geirfaoedd fesul iaith, a CI aml-locale sy'n cynnwys ffug-locale de-i-chwith a thestun hir. Rhedwch leoleiddio fel seilwaith a rennir gyda pherchennog clir fel bod grwpiau'n stopio ailddyfeisio'r plymwaith neu'n crwydro allan o gydamseriad. Mesurwch sylw iaith, ansawdd lleoleiddio, ac amser i lansio locale newydd, a rheolwch y portffolio locale yn erbyn y ffigurau hynny yn hytrach na lansio marchnadoedd ad hoc.

**Llywodraeth.** Mae mynediad iaith yn aml yn rhwymedigaeth gyfreithiol, sy'n cwmpasu ieithoedd swyddogol, sgriptiau de-i-chwith, ac ieithoedd brodorol neu leiafrifol, felly mae tryloywder a thegwch yn siapio pob dewis. Adeiladwch fframwaith i18n a rennir a llif gwaith cyfieithu ar draws asiantaethau, mynnwch adolygiad dynol ar gyfer terminoleg gyfreithiol a diogelwch, a chyhoeddwch eirfaoedd fel bod termau'n aros yn gyson rhwng gwasanaethau. Dylai caffael fynnu cefnogaeth locale, de-i-chwith, a hygyrchedd mewn contractau, a'r boblogaeth a wasanaethir ym mhob iaith yw'r fetrig sy'n cyfiawnhau'r gwariant i'r cyhoedd.

## Enghreifftiau

**Busnes newydd.** Fe wnaeth busnes newydd bach a oedd yn rhyddhau yn Saesneg yn unig wneud ychydig o ddewisiadau pensaernïol rhad o hyd ar y diwrnod cyntaf: UTF-8 ym mhobman, pob llinyn sy'n wynebu defnyddwyr wedi'i dynnu i mewn i gatalog negeseuon yn lle ei godio'n galed, a dyddiadau ac arian cyfred wedi'u fformatio trwy lyfrgell ymwybodol o locale. Fe gostiodd bron ddim iddyn nhw tra bod ganddyn nhw un iaith. Flwyddyn yn ddiweddarach, pan ofynnodd eu darpar gwsmer mwyaf am fersiwn Ffrangeg ac Almaeneg, ymarfer cyfieithu a roddwyd i gontractwr oedd ychwanegu'r locales hynny'n bennaf, nid ailysgrifennu, a chaeasant y fargen mewn wythnosau yn hytrach na'i gohirio am chwarter o waith peirianneg.

**Menter.** Fe wnaeth cwmni e-fasnach byd-eang ryngwladoli ei blatfform yn gynnar: UTF-8 trwyddi draw, llinynnau wedi'u hallanoli, llyfrgell fformatio ymwybodol o locale, a phiblinell leoleiddio barhaus gyda chof cyfieithu a geirfaoedd fesul iaith. Daeth mynd i mewn i farchnad newydd yn bennaf yn ymarfer cynnwys (cyfieithu, adolygu, addasu delweddaeth) yn hytrach na phrosiect peirianneg, gan adael i'r cwmni lansio mewn locales newydd mewn wythnosau. Roedd cefnogaeth de-i-chwith wedi'i hadeiladu ar briodweddau cynllun rhesymegol yn golygu bod angen ychydig iawn o waith rhyngwyneb newydd ar farchnadoedd Arabeg a Hebraeg.

**Llywodraeth.** Fe wnaeth llywodraeth genedlaethol yr oedd yn ofynnol yn gyfreithiol iddi gyflenwi gwasanaethau mewn sawl iaith swyddogol, gan gynnwys sgript de-i-chwith ac ieithoedd lleiafrifol, adeiladu fframwaith i18n a rennir a llif gwaith cyfieithu a ddefnyddir ar draws asiantaethau. Fe wnaeth ffug-leoleiddio yn CI ddal llinynnau wedi'u codio'n galed a thocio cyn lansio; cadwodd geirfa a rennir derminoleg gyfreithiol yn gyson ar draws gwasanaethau ac ieithoedd. Gall dinasyddion gwblhau trafodion treth, iechyd, a budd-daliadau yn eu hiaith eu hunain gyda fformatio dyddiad, rhif, ac enw cywir, gan fodloni deddf mynediad iaith a gwella tegwch i siaradwyr ieithoedd nad ydynt yn rhai'r mwyafrif.

## Achos busnes: cymhellion, ROI, a TCO

ROI rhyngwladoli yw mynediad marchnad a chyflymder. Gall cynnyrch sydd wedi'i ryngwladoli'n dda fynd i mewn i wledydd a marchnadoedd iaith newydd yn gyflym ac yn rhad, gan droi pob locale newydd yn incwm cynyddrannol neu gyrhaeddiad dinasyddion yn hytrach na phrosiect mawr. Mae ansawdd lleoleiddio'n gyrru trosiad, ymddiriedaeth, a chost cymorth ym mhob marchnad: mae defnyddwyr yn trafod mwy ac yn cysylltu â chymorth lai pan fydd y cynnyrch yn siarad eu hiaith yn gywir ac yn parchu eu confensiynau.

O ran TCO, cost mabwysiadu yw'r peirianneg ymlaen llaw i ryngwladoli, ynghyd â chostau cyfieithu a phiblinell parhaus. Cost peidio â mabwysiadu yw'r ôl-osod drud: dadwneud llinynnau wedi'u codio'n galed, cyfuno, namau amgodio, a rhagdybiaethau cynllun ar draws sylfaen god gyfan, yn aml ar ddyddiad cau wedi'i yrru gan farchnad neu ofyniad cyfreithiol. Mae lleoleiddio gwael yn cario costau cudd hefyd: gwerthiannau coll mewn marchnadoedd a wasanaethir yn wael, baich cymorth o fformatau dryslyd, a niwed cyfreithiol neu enw da o gynnwys risg uchel wedi'i gamgyfieithu. Mae lleoleiddio parhaus yn osgoi gwasgfeydd cyfieithu cyn-lansio drud.

I wneud yr achos i arweinyddiaeth, fframiwch rhyngwladoli fel opsiwn ar farchnadoedd y dyfodol. Mae'n fuddsoddiad gwylaidd ymlaen llaw sy'n gostwng cost ac amser pob mynediad marchnad yn y dyfodol yn ddramatig. I lywodraeth, y gyrrwr yw rhwymedigaeth mynediad iaith gyfreithiol a thegwch, wedi'i feintioli gan y boblogaeth a wasanaethir ym mhob iaith.

## Gwrth-batrymau a pheryglon

- **Llinynnau wedi'u codio'n galed:** testun defnyddiwr wedi'i bobi i mewn i god, gan orfodi newidiadau cod fesul locale.
- **Cyfuno llinynnau:** adeiladu brawddegau o ddarnau, sy'n torri gramadeg a threfn geiriau.
- **Rhagdybiaethau nad ydynt yn Unicode:** namau amgodio, [mojibake](https://en.wikipedia.org/wiki/Mojibake) (testun wedi'i gymysgu o amgodiadau nod anghyson), ac anallu i gynrychioli sgriptiau.
- **Tybio hyd testun Saesneg:** cynlluniau sy'n tocio neu'n gorgyffwrdd pan gânt eu cyfieithu.
- **Anwybyddu de-i-chwith:** defnyddio cynllun chwith/de ffisegol na all ddrychu.
- **Lluosogi naïf:** rhesymeg unigol/lluosog sy'n anghywir yn y rhan fwyaf o ieithoedd.
- **Fformatio dall i locale:** fformatau dyddiad, rhif, ac arian cyfred wedi'u codio'n galed.
- **Cyfieithu heb gyd-destun:** cyfieithwyr yn dyfalu ystyr, gan gynhyrchu gwallau.
- **Lleoleiddio swp, munud olaf:** gwasgfa cyn-lansio yn lle piblinell barhaus.
- **Byddardod tôn diwylliannol:** delweddaeth, lliwiau, neu enghreifftiau sy'n tramgwyddo neu'n drysu'n lleol.

## Model aeddfedrwydd

**Lefel 1: Cychwyn.** Un iaith, llinynnau wedi'u codio'n galed, rhagdybiaethau nad ydynt yn Unicode, a thestun wedi'i adeiladu trwy gyfuno. Mae rhyngwladoli'n adweithiol: mae unrhyw locale newydd yn golygu newid cod, a chaiff namau amgodio a chynllun eu darganfod trwy ddamwain mewn cynhyrchu.

**Lefel 2: Datblygu.** Mae rhai llinynnau wedi'u hallanoli a defnyddir Unicode mewn mannau, ond mae'r arfer yn anghyson ar draws timau. Mae lleoleiddio'n ymdrech â llaw, swp, cyn-lansio, a chaiff fformatio, trin lluosog, a chefnogaeth de-i-chwith eu trin yn wahanol (neu ddim o gwbl) o un tîm i'r llall.

**Lefel 3: Safoni.** Mae pensaernïaeth i18n a rennir a llyfrgell fformatio ymwybodol o locale yn safon wedi'i ddogfennu, wedi'i gorfodi ledled y sefydliad. Gwirir allanoli llinynnau gan reolau lint, mae system rheoli cyfieithu a phiblinell barhaus ar waith gyda geirfaoedd a chof cyfieithu, a rhedir ffug-leoleiddio yn ogystal â phrofi aml-locale (gan gynnwys locale de-i-chwith a locale testun hir) yn CI.

**Lefel 4: Rheoli.** Mesurir a rheolir y rhaglen leoleiddio yn erbyn llinellau sylfaen. Mae timau'n tracio sylw iaith, ansawdd lleoleiddio a chyfraddau diffyg, oedi cydamseru llinynnau o ymrwymo i ryddhad wedi'i gyfieithu, namau tocio a rendro de-i-chwith a ddelir fesul rhyddhad, cost cyfieithu fesul locale, ac amser i lansio locale newydd, ac mae'r metrigau hyn yn borth i ryddhadau ac yn gyrru lle i fuddsoddi mewn adolygiad dynol yn erbyn cyfieithu peirianyddol.

**Lefel 5: Cydgordio.** Caiff rhyngwladoli a lleoleiddio eu gwella'n barhaus a'u hintegreiddio ar draws y sefydliad. Mae lleoleiddio'n barhaus, dewisir cyfieithu peirianyddol a dynol yn fwriadol fesul dosbarth cynnwys, ac mae addasu diwylliannol yn systematig. Mae'r sefydliad yn ychwanegu, yn ymddeol, ac yn ailgwmpasu locales mewn ymateb i dystiolaeth marchnad a thegwch, ac mae locales newydd yn lansio'n gyflym gydag ansawdd uchel heb ôl-osod.

## Syniadau i'w trafod

- Pa mor gynnar ddylai cynnyrch ryngwladoli os yw galw rhyngwladol yn ansicr?
- Ble mae cyfieithu peirianyddol yn dderbyniol, a ble mae'n rhaid i bobl adolygu?
- Sut ydych chi'n cadw terminoleg yn gyson ar draws llawer o ieithoedd a thimau?
- Faint o addasiad diwylliannol rhanbarthol sy'n werth y cynnal a chadw amrywiad ychwanegol?
- Sut ddylid blaenoriaethu a phrofi cefnogaeth de-i-chwith ac ieithoedd lleiafrifol?
- Sut ydych chi'n rhoi digon o gyd-destun i gyfieithwyr heb arafu'r biblinell?

## Casgliadau allweddol

- Rhyngwladolwch y bensaernïaeth unwaith; lleoleiddiwch gynnwys sawl gwaith.
- Defnyddiwch Unicode ym mhobman, allanolwch bob llinyn, a pheidiwch byth â chyfuno cyfieithiadau.
- Cynlluniwch ar gyfer ehangu testun, sgriptiau de-i-chwith, a rheolau lluosog a fformatio penodol i locale.
- Rhedwch biblinell leoleiddio barhaus gyda chof cyfieithu, geirfaoedd, a chyd-destun.
- Ffug-leoleiddiwch yn gynnar yn CI i ddal namau i18n cyn cyfieithu go iawn.
- Mae lleoleiddio'n ddiwylliannol, nid dim ond ieithyddol.
- Mae rhyngwladoli cynnar yn llawer rhatach nag ôl-osod; i lywodraeth mae'n ofyniad tegwch cyfreithiol.

## Cyfeiriadau a darllen pellach

- The Unicode Consortium, *The Unicode Standard* and Common Locale Data Repository (CLDR)
- W3C Internationalization (i18n) Activity, techniques and best practices
- Richard Ishida, W3C internationalization articles and tutorials
- Bert Esselink, *A Practical Guide to Localization*
- John Yunker, *Beyond Borders: Web Globalization Strategies*
- Unicode Technical Standard #35 (locale data markup) and ICU library documentation
- IETF BCP 47 language tags
- Government multilingual service and language-access guidance
- Nielsen Norman Group and W3C articles on RTL, text expansion, and localization UX
