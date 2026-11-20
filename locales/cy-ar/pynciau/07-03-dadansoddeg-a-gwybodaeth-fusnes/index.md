# 7.3 Dadansoddeg a chudd-wybodaeth fusnes

## Trosolwg a chymhelliant

Mae dadansoddeg a chudd-wybodaeth fusnes yn troi data llywodraethedig, wedi'i beiriannu, yn ddealltwriaeth a gweithredu. Yn draddodiadol, mae [cudd-wybodaeth fusnes](https://en.wikipedia.org/wiki/Business_intelligence) (BI) yn golygu'r adrodd, y dangosfyrddau, a'r offer hunanwasanaeth sy'n galluogi pobl i weld beth sy'n digwydd yn y busnes. Dadansoddeg yw'r arfer ehangach o ofyn ac ateb cwestiynau â data, o ddisgrifiadau syml o'r gorffennol i fodelau sy'n argymell beth i'w wneud nesaf. Gyda'i gilydd, dyma sut mae sefydliad yn ei weld ei hun.

I dimau mawr, dyma'r haenen lle mae data naill ai'n ennill ei gadw neu'n dod yn ffynhonnell dryswch. Pan fydd miloedd o weithwyr yn gallu adeiladu eu hadroddiadau eu hunain, y risg yw nid gormod o wybodaeth ond gormod o wybodaeth wrthdrawiadol: tri dangosfwrdd yn dangos tri rhif refeniw gwahanol, pob un yn amddiffynadwy, dim un yn awdurdodol. Mae mentrau mawr yn byw ac yn marw yn ôl y rhifau mewn dogfennau bwrdd a chyflwyniadau rheoleiddiol. Mae asiantaethau llywodraeth yn adrodd i ddeddfwrfeydd, cyrff goruchwylio, a'r cyhoedd. Yn y ddau achos, mae metrig sy'n golygu gwahanol bethau i wahanol bobl yn atebolrwydd. Gall siart sy'n camarwain, hyd yn oed yn ddiniwed, yrru penderfyniadau anghywir costus neu erydu ymddiriedaeth gyhoeddus.

Y syniad allweddol ar gyfer dofi hyn ar raddfa fawr yw'r [haenen semantig](https://en.wikipedia.org/wiki/Semantic_layer): diffiniad canolog, llywodraethedig o fetrigau a dimensiynau y mae pob offeryn ac adroddiad yn tynnu arno, fel bo "cwsmer gweithredol" neu "refeniw misol" yn cael ei gyfrifo un ffordd y cytunwyd arni ym mhobman. O amgylch y syniad hwnnw mae disgyblaethau delweddu gonest, dylunio dangosfwrdd bwriadol, a rheoli'r ymledu y mae hunanwasanaeth yn anochel yn ei gynhyrchu. Mae'r bennod hon yn dangos ichi sut i roi mynediad eang i bobl at ddata heb roi'r gorau i un fersiwn o'r gwirionedd.

## Egwyddorion allweddol

- Dylai fod un diffiniad llywodraethedig o bob metrig pwysig, a ddefnyddir ym mhobman.
- Cydweddwch y math o ddadansoddeg â'r cwestiwn: disgrifio, diagnosio, rhagfynegi, neu ragnodi.
- Mae hunanwasanaeth yn bwerus ond rhaid ei lywodraethu i atal ymledu metrigau.
- Rhaid i siartiau fod yn onest; deall yw'r nod, nid perswadio drwy ystumio.
- Dylai dangosfyrddau yrru penderfyniadau, nid dim ond arddangos data.
- Ardystiwch gynnwys ymddiriedig fel bo defnyddwyr yn gwybod ar beth i ddibynnu.
- Curadwch a diddymwch; nid mwy o ddangosfyrddau sy'n golygu mwy o fewnwelediad.
- Ymgorffolwch ddadansoddeg lle gwneir penderfyniadau, yn hytrach na dim ond mewn porth BI ar wahân.

## Argymhellion

### Deallwch y pedwar math o ddadansoddeg

Mae dadansoddeg ddisgrifiadol yn adrodd beth ddigwyddodd. Mae dadansoddeg ddiagnostig yn esbonio pam y digwyddodd. Mae [dadansoddeg ragfynegol](https://en.wikipedia.org/wiki/Predictive_analytics) yn rhagolygu beth sy'n debygol o ddigwydd. Mae [dadansoddeg ragnodol](https://en.wikipedia.org/wiki/Prescriptive_analytics) yn argymell beth i'w wneud yn ei gylch. Mae'r rhan fwyaf o sefydliadau'n gorfuddsoddi mewn dangosfyrddau disgrifiadol ac yn tanfuddsoddi mewn diagnosis a gweithredu. Gwthiwch eich gwaith i fyny'r ysgol hon yn fwriadol. Paru pob metrig pwysig â'r gallu i dyllu i mewn i achosion, a chysylltwch ragfynegiadau â phenderfyniadau ac ymyriadau pendant. Fel hyn mae dadansoddeg yn newid ymddygiad yn hytrach na dim ond ei ddisgrifio.

### Adeiladwch haenen semantig a llywodraethu metrigau

Diffiniwch fetrigau a dimensiynau unwaith, mewn haenen semantig ganolog, a chael pob offeryn BI, llyfr nodiadau, ac adroddiad ymgorfforedig i gyfrifo o'r diffiniadau hynny. Mae hyn yn lladd y broblem glasurol o rifau gwahanol. Mae hefyd yn gwneud rhesymeg metrig yn rheoledig o ran fersiwn, yn brofadwy, ac yn adolygadwy. Llywodraethwch fetrigau fel API: mae gan bob metrig ardystiedig berchennog, diffiniad clir, a chofnod newid. Cadwch fetrigau ardystiedig ar wahân i rai arbrofol, fel bo defnyddwyr yn gwybod beth sy'n awdurdodol.

### Galluogwch hunanwasanaeth o fewn reiliau diogelwch

Rhowch fynediad hunanwasanaeth i ddadansoddwyr a defnyddwyr busnes archwilio data. Ni all timau BI canolog ateb pob cwestiwn, ac mae tagfeydd yn syml yn gwthio pobl at daenlenni. Ond darparwch reiliau diogelwch: setiau data ardystiedig curedig, yr haenen semantig ar gyfer metrigau cyson, templedi, a hyfforddiant. Mae'r nod yn syml: gwnewch y llwybr hawdd ddefnyddio diffiniadau llywodraethedig. Marciwch haenau cynnwys (ardystiedig, wedi'i gefnogi gan dîm, a phersonol) fel nad yw rhyddid i archwilio'n cymryd arno fod yn wirionedd swyddogol.

### Dyluniwch ddangosfyrddau ar gyfer penderfyniadau

Dechreuwch bob dangosfwrdd o'r penderfyniad y mae'n ei gefnogi a'r gynulleidfa sy'n ei wneud. Arweiniwch â'r ychydig fetrigau sy'n bwysig. Darparwch gyd-destun (targedau, tueddiadau, cymariaethau) fel bo'r rhifau'n ddehonglig, a galluogwch dyllu i lawr ar gyfer diagnosis. Gwrthsafwch yr ysfa i wasgu pob siart sydd ar gael i mewn i un dudalen. Mae dangosfwrdd sy'n ateb "ydyn ni ar y trywydd iawn, ac os nad ydym, ble rydw i'n edrych?" yn werth llawer mwy nag un sy'n dangos hanner cant o fetrigau nad oes neb yn gweithredu arnynt.

### Ymarferwch ddelweddu data gonest

Dewiswch fathau o siartiau sy'n ffitio'r data: llinellau ar gyfer tueddiadau dros amser, bariau ar gyfer cymariaethau ar draws categorïau. Osgowch siartiau cylch ar gyfer unrhyw beth y tu hwnt i ychydig o sleisys. Dechreuwch echelinau siart bar ar sero, cadwch raddfeydd yn gyson, ac osgowch echelinau deuol sy'n gweithgynhyrchu cydberthnasau ffug. Defnyddiwch liw'n bwrpasol ac yn hygyrch, nid yn addurniadol. Labelwch yn glir, a dangoswch ansicrwydd lle mae'n bwysig. Mae'r prawf yn syml: a fyddai gwyliwr gwybodus yn cyrraedd yr un casgliad y mae'r data'n ei gefnogi, neu a yw'r dyluniad wedi'i wthio tuag at un gwahanol?

### Curadwch gynnwys a brwydrwch yn erbyn ymledu

Mae hunanwasanaeth heb guradu'n cynhyrchu miloedd o ddangosfyrddau hen, dyblyg, ac wedi'u gadael. Rhowch reolaeth cylch bywyd ar waith: dilynwch ddefnydd, archifwch gynnwys nas defnyddir, dilëwch ddyblygiadau, ac ail-ardystiwch yr hyn sy'n weddill yn gyfnodol. Gwnewch y catalog ardystiedig yn hawdd i'w ganfod, fel bo pobl yn ailddefnyddio cynnwys ymddiriedig yn hytrach na'i ailadeiladu. Mae set lai o ddangosfyrddau ymddiriedig, wedi'u cynnal yn dda yn drech na fynwent ymledol.

### Ymgorffolwch ddadansoddeg ac adrodd gweithredol

Nid yw pob dadansoddeg yn perthyn mewn porth ar wahân. Ymgorffolwch fetrigau ac adroddiadau perthnasol yn uniongyrchol i mewn i'r cymwysiadau gweithredol lle mae pobl eisoes yn gweithio, megis y CRM (system [rheoli perthynas cwsmeriaid](https://en.wikipedia.org/wiki/Customer_relationship_management)), y system rheoli achosion, neu'r offeryn tocynnau, fel bo mewnwelediad yn cyrraedd pwynt y penderfyniad. Ar gyfer adrodd gweithredol â gofynion oedi neu fformatio llym (anfonebau, cyfriflenni, cyflwyniadau rheoleiddiol), defnyddiwch adrodd wedi'i adeiladu at ddiben. Peidiwch â mestyn dangosfyrddau rhyngweithiol i wneud swydd nad ydynt yn ei ffitio'n dda.

## Cyfaddawdau: manteision ac anfanteision

| Dewis | Manteision | Anfanteision | Ffit gorau |
|---|---|---|---|
| Tîm BI canolog | Cyson, llywodraethedig, wedi'i reoli o ran ansawdd | Tagfa, araf i ymateb | Adrodd rheoledig |
| BI hunanwasanaeth | Cyflym, graddadwy, yn grymuso defnyddwyr | Ymledu, metrigau anghyson | Archwilio eang |
| Haenen semantig | Un gwirionedd, ailddefnyddiadwy, llywodraethedig | Modelu a chynnal a chadw ymlaen llaw | Unrhyw sefydliad y tu hwnt i raddfa fach |
| Dadansoddeg ymgorfforedig | Mewnwelediad ym mhwynt y penderfyniad | Cost peirianneg, anos ei lywodraethu | Llifau gwaith gweithredol |
| Dangosfyrddau cyfoethog | Golwg gynhwysfawr | Llethol, cyfradd gweithredu isel | Anaml yn ddelfrydol |
| Dangosfyrddau â ffocws | Yn gyrru penderfyniadau | Angen disgyblaeth olygyddol | Y rhan fwyaf o achosion defnydd |

Y tyndra craidd yw mynediad yn erbyn cysondeb. Mae cloi BI y tu mewn i dîm canolog yn gwarantu rhifau cyson, ond mae'n llwgu'r sefydliad o atebion amserol ac yn bridio taenlenni cysgod. Mae hunanwasanaeth llawn yn grymuso pawb, ond mae'n lluosi metrigau gwrthdrawiadol a chynnwys hen. Nid oes rhaid ichi ddewis ochr. Cyfunwch fynediad hunanwasanaeth eang ag haenen semantig lywodraethedig ac ardystiad, fel bo pobl yn rhydd i archwilio tra bo'r rhifau pwysig yn aros yn unigryw ac yn ddibynadwy.

## Cwestiynau i'w trafod gyda'ch tîm

1. **A ydych wedi buddsoddi mewn haenen semantig, ac a ydych yn llywodraethu pob metrig ardystiedig fel API â pherchennog, diffiniad, a chofnod newid?** Syniad canolog y bennod yw un diffiniad llywodraethedig o bob metrig y mae pob offeryn, llyfr nodiadau, ac adroddiad ymgorfforedig yn cyfrifo ohono, sy'n lladd y broblem glasurol o dri dangosfwrdd yn dangos tri rhif refeniw. I fentrau sy'n dibynnu ar un ffigur ar gyfer eu dogfennau bwrdd a'u cyflwyniadau rheoleiddiol, ac ar gyfer asiantaethau y mae'n rhaid i'w rhyddhadau cyhoeddus gyfateb i rifau mewnol, mae metrig sy'n gwahaniaethu'n atebolrwydd uniongyrchol. Mae'r cyfaddawd yn real: mae'r haenen semantig angen modelu ymlaen llaw a chynnal a chadw parhaus. Dewch â thystiolaeth: cyfrwch faint o ddiffiniadau o'ch metrig pwysicaf sy'n bodoli heddiw a beth mae cysoni'n ei gostio ar hyn o bryd mewn oriau dadansoddwyr. Os yw'r cyfrif yn fwy nag un, mae'r haenen semantig yn talu amdani ei hun, ac mae llywodraethu metrigau â pherchnogion a chofnodion newid yn ei chadw'n unigryw dros amser.

2. **Ble mae'r llinell rhwng rhyddid hunanwasanaeth ac ymledu metrigau, a pha reiliau diogelwch sy'n cadw'r llwybr hawdd yn un llywodraethedig?** Mae'r bennod yn dadlau na ddylech ddewis rhwng BI canolog wedi'i gloi'n dynn a hunanwasanaeth di-ffrwyn: mae timau canolog yn dod yn dagfeydd sy'n gwthio pobl at daenlenni, tra bo hunanwasanaeth llawn yn lluosi metrigau gwrthdrawiadol a dangosfyrddau hen. Y datrysiad yw mynediad eang ar ben setiau data ardystiedig, yr haenen semantig, templedi, a haenau cynnwys clir (ardystiedig, wedi'i gefnogi gan dîm, personol) fel nad yw archwilio'n cymryd arno fod yn wirionedd swyddogol. Dewch â signalau pendant: faint o ddangosfyrddau sy'n bodoli, faint sy'n cael eu defnyddio mewn gwirionedd, ac a all defnyddwyr wahaniaethu cynnwys ymddiriedig oddi wrth arbrofion. Os na allant ddweud, dylai ardystio a rheolaeth cylch bywyd (dilyn defnydd, archifo'r hyn nas defnyddir, ail-ardystio'r gweddill) ddod yn arfer sefydlog, oherwydd mae set ymddiriedig lai'n drech na fynwent ymledol.

3. **A yw eich siartiau'n ddigon gonest i oroesi archwiliad, a phwy sy'n gwirio bod y dyluniad yn cefnogi'r casgliad y mae'r data mewn gwirionedd yn ei gyfiawnhau?** Mae'r bennod yn gosod prawf clir: a fyddai gwyliwr gwybodus yn cyrraedd yr un casgliad y mae'r data'n ei gefnogi, neu a yw'r dyluniad wedi'i wthio i le arall? Enwir echelinau wedi'u torri, echelinau deuol sy'n gweithgynhyrchu cydberthynas ffug, a chylchoedd 3D fel peryglon. Ar gyfer rhyddhadau llywodraeth i ddinasyddion a chyflwyniadau rheoledig, mae siart sy'n camarwain yn ddiniwed yn erydu ymddiriedaeth gyhoeddus neu'n gwahodd canfyddiad, felly mae gonestrwydd yma'n bryder llywodraethu, nid dim ond chwaeth. Dewch ag enghraifft lle camarweiniodd siart yn eich sefydliad ei gynulleidfa, a phenderfynwch a oes angen safonau delweddu arnoch (echelinau bar sy'n dechrau ar sero, graddfeydd cyson, ansicrwydd wedi'i ddangos) wedi'u gorfodi ar gynnwys a gyhoeddir. Dylai'r ateb osod disgwyliadau adolygu ar gyfer unrhyw beth sy'n gadael yr adeilad.

4. **Pa un o'ch dangosfyrddau sy'n mewn gwirionedd yn newid penderfyniad, a beth yw eich maen prawf ar gyfer diddymu un nad yw'n gwneud hynny?** Mae'r bennod yn mynnu y dylai dangosfwrdd ddechrau o'r penderfyniad y mae'n ei gefnogi, eto mae'r rhan fwyaf o sefydliadau mawr yn cronni dangosfyrddau balchder a wylir ac na weithredir arnynt byth, gan gael eu camgymryd am ddiwylliant data-yrredig. Mae hyn yn bwysig ar raddfa fawr oherwydd bod pob dangosfwrdd yn cario cost gudd: rhaid ei gynnal, cadw ei fetrigau'n gyson â'r haenen semantig, ac mae ei bresenoldeb yn gwanhau sylw oddi wrth yr adroddiadau sydd mewn gwirionedd yn gyrru gweithredu. Y tyndra cystadleuol yw bod pobl yn teimlo'n fwy diogel â mwy o welededd, ac nid oes unrhyw dîm yn hoffi cael ei ddangosfwrdd wedi'i archifo. Dewch â thelemetreg defnydd (pwy sy'n agor pob dangosfwrdd, pa mor aml, ac a yw unrhyw weithred i lawr yr afon yn dilyn) a rhestr onest o'r penderfyniadau y mae eich dangosfyrddau gorau i fod i'w llywio. I fentrau mawr mae hyn yn bwydo curadu portffolio a rheoli cost trwyddedau; i asiantaeth lywodraeth, mae hefyd yn ateb cwestiynau goruchwylio ynghylch a yw gwariant adrodd yn cynhyrchu gwerth gweithredol mesuradwy yn hytrach na sgriniau nad oes neb yn eu darllen.

5. **A ydych chi wedi gorfuddsoddi mewn disgrifio'r gorffennol pan fo'r gwerth mewn diagnosis, rhagfynegiad, a rhagnodiad, a beth fyddai'n symud un metrig allweddol i fyny'r ysgol honno?** Mae'r bennod yn fframio pedwar math o ddadansoddeg (disgrifiadol, diagnostig, rhagfynegol, rhagnodol) ac yn rhybuddio bod y rhan fwyaf o sefydliadau'n pentyrru dangosfyrddau disgrifiadol tra'n tanfuddsoddi yn y diagnosis a'r gweithredu sydd mewn gwirionedd yn newid canlyniadau. I dîm mawr, mae aros yn sownd wrth ddisgrifio'n golygu bod dadansoddwyr yn treulio eu hamser yn ail-adrodd yr hyn y mae pawb eisoes yn ei wybod, tra bo'r cwestiwn anoddach o pam y digwyddodd a beth i'w wneud nesaf yn aros heb ei ateb. Y tyndra yw bod gwaith diagnostig a rhagfynegol angen peirianneg data ddyfnach, llywodraethu model, a sgil dadansoddwyr, felly mae'n haws cyllido dangosfwrdd arall. Dewch â'r hollt presennol o'ch ymdrech ddadansoddol ar draws y pedwar math ac un metrig lle byddai tyllu i mewn i achosion neu ragolygu'n newid penderfyniad yn amlwg. Mewn menter mae hyn yn cysylltu dadansoddeg â margin a risg; mewn asiantaeth gyhoeddus, rhaid i waith rhagfynegol a rhagnodol (er enghraifft rhagolygu galw am wasanaeth) hefyd gario mesurau diogelu esboniadwyedd a thegwch cyn iddo lywio penderfyniadau am ddinasyddion.

6. **Ble mae angen i fewnwelediad gyrraedd y tu mewn i'r offer y mae pobl eisoes yn gweithio ynddynt, a ble ddylech ddefnyddio adrodd gweithredol wedi'i adeiladu at ddiben yn lle dangosfwrdd?** Mae'r bennod yn gwahaniaethu BI rhyngweithiol oddi wrth ddadansoddeg ymgorfforedig ac oddi wrth adrodd gweithredol wedi'i adeiladu at ddiben megis anfonebau, cyfriflenni, a chyflwyniadau rheoleiddiol, ac yn rhybuddio yn erbyn mestyn dangosfwrdd i wneud swydd nad yw'n ei ffitio'n dda. Mae hyn yn bwysig i dimau mawr oherwydd anaml y mae staff rheng flaen yn gadael eu CRM neu system rheoli achosion i ymgynghori â phorth BI ar wahân, felly mae mewnwelediad sy'n byw mewn porth yn unig yn mynd heb ei ddefnyddio ar foment y penderfyniad. Yr ystyriaethau cystadleuol yw cost peirianneg a llywodraethu: mae ymgorffori metrigau mewn cymwysiadau gweithredol yn anoddach i'w adeiladu ac yn anoddach ei gadw'n gyson â diffiniadau ardystiedig, tra bo adrodd pixel-berffaith angen oedi a fformatio llym na all yr offeryn dangosfwrdd eu gwarantu. Dewch â map o ble mae penderfyniadau mewn gwirionedd yn cael eu gwneud a pha rai ohonynt sydd ar hyn o bryd angen i rywun newid offer i ddod o hyd i'r rhif. I fenter, mae hyn yn llunio ble i fuddsoddi ymdrech beirianneg; i asiantaeth lywodraeth, mae gan gyflwyniadau statudol a datganiadau sy'n wynebu dinasyddion yn aml reolau fformatio a chadw cyfreithiol sy'n gwneud adrodd wedi'i adeiladu at ddiben yn orfodol yn hytrach na dewisol.

## Trwy lens sector

**Cwmni newydd.** Diffiniwch eich llond dwrn o fetrigau craidd unwaith, hyd yn oed mewn offeryn ysgafn, fel na fydd y ddogfen fwrdd a'r dangosfwrdd cynnyrch byth yn anghytuno. Hepgorwch blatfform haenen-semantig trwm: mae un ffynhonnell diffiniadau a rennir ac un rhestr fer o ddangosfyrddau ymddiriedig yn ddigon tra bo'r tîm yn fach. Mae cyflymder yn bwysicach na sglein yma, felly ffafriwch offeryn BI wedi'i gynnal y gallwch ei bwyntio at eich warws heddiw dros unrhyw beth y byddai'n rhaid ichi ei adeiladu.

**Busnes bach.** Heb arbenigwr BI penodedig, pwyswch ar ddadansoddeg sydd eisoes wedi'i hymgorffori yn yr offer sy'n eiddo i chi, megis eich CRM neu feddalwedd cyfrifeg, yn hytrach na sefydlu platfform ar wahân. Fframiwch y dewis fel prynu yn erbyn adeiladu a gadewch i brynu ennill yn ddiofyn; eich risg yw diwylliant taenlen lle mae pob person yn cario rhif "refeniw" gwahanol, felly cytunwch ar y diffiniadau prin sy'n bwysig ac ysgrifennwch nhw i lawr. Ffafriwch offer sy'n gwneud adroddiadau ardystiedig yn hawdd eu rhannu ac yn anodd eu fforchio'n ddamweiniol.

**Menter fawr.** Y broblem graidd yw cysondeb ar draws llawer o dimau: buddsoddwch mewn haenen semantig lywodraethedig, ardystiwch gynnwys ymddiriedig, a rheolwch ymledu dangosfyrddau fel cylch bywyd parhaus â pherchnogion, dilyn defnydd, ac ailardystiad. Triniwch bob metrig ardystiedig fel API â diffiniad, perchennog, a chofnod newid, a gwahanwch gynnwys ardystiedig oddi wrth un arbrofol fel na fydd hunanwasanaeth yn cymryd arno fod yn wirionedd swyddogol. Cyllidebwch yr ymdrech fodelu a churadu'n benodol, oherwydd ar raddfa fawr y dewis arall yw dadansoddwyr yn cysoni rhifau gwahanol yn ddiddiwedd.

**Llywodraeth.** Rhaid i ffigurau a gyhoeddir gyfateb i rai mewnol a goroesi archwiliad cyhoeddus a deddfwrfaol, felly mae haenen semantig lywodraethedig a safonau delweddu gorfodedig (echelinau sy'n dechrau ar sero, graddfeydd gonest, ansicrwydd wedi'i ddangos) yn ofynion atebolrwydd, nid manteision cwrtais. Gall rheolau caffael gyfyngu pa offer BI y gallwch eu prynu a mynnu cludadwyedd data, felly osgowch glymu i rhesymeg metrig berchnogol un gwerthwr. Cadwch ryddhadau cyhoeddus ardystiedig ar wahân i ddadansoddiad arbrofol, a rhowch siartiau i ddinasyddion sy'n ddigon gonest fel bo gwyliwr gwybodus yn cyrraedd y casgliad y mae'r data mewn gwirionedd yn ei gyfiawnhau.

## Enghreifftiau

**Cwmni newydd.** Mewn marchnad gam gynnar, roedd y ddau sylfaenydd bob un yn cadw taenlen "refeniw misol," ac ni fyddai'r rhifau byth yn cyfateb yn union pan fyddent yn paratoi'r ddogfen fwrdd. Diffinion nhw'r metrig unwaith mewn haenen semantig fach, pwyntio un offeryn BI ati, a marcio un rhestr fer o ddangosfyrddau fel y rhai ymddiriedig y dylai pawb eu defnyddio. Aeth adrodd o gysoni nos Sul i ddolen y gallent ei hagor â hyder.

**Menter fawr.** Roedd cwmni telathrebu'n dioddef gan gyllid, marchnata, a gweithrediadau bob un yn adrodd cyfrifon "tanysgrifiwr gweithredol" gwahanol. Cyflwynodd haenen semantig sy'n diffinio pob metrig craidd unwaith, mudo dangosfyrddau i gyfrifo ohoni, ac ardystio set curedig o adroddiadau ymddiriedig tra'n archifo miloedd o rai hen. Peidiodd adrodd i'r bwrdd â bod yn ymarfer cysoni, a chododd mabwysiad hunanwasanaeth oherwydd bod pobl yn ymddiried yn y rhifau.

**Llywodraeth.** Adeiladodd adran iechyd cyhoeddus ddangosfyrddau ardystiedig sy'n tynnu o haenen semantig lywodraethedig, fel bo cyfrifon achosion a chyfraddau'n cael eu cyfrifo'n union yr un fath ar draws gwneud penderfyniadau mewnol a rhyddhadau cyhoeddus. Mae safonau delweddu'n cadw siartiau a gyhoeddir i ddinasyddion yn onest (echelinau'n dechrau ar sero, bandiau ansicrwydd clir), sy'n diogelu ymddiriedaeth gyhoeddus. Mae adroddiadau ymgorfforedig yn arddangos metrigau lleol y tu mewn i'r offer rheoli achosion y mae staff rheng flaen eisoes yn eu defnyddio.

## Achos busnes: cymhellion, ROI, a TCO

Daw ROI dadansoddeg a BI a redir yn dda o benderfyniadau cyflymach, gwell ac o dorri gwastraff. Pan fydd pobl yn ymddiried mewn un set o rifau, mae cyfarfodydd yn peidio â bod yn ddadleuon am pa daenlen sy'n gywir ac yn dod yn drafodaethau am beth i'w wneud. Mae hunanwasanaeth yn lleihau'r ôl-groniad ar dimau canolog, ac mae haenen semantig yn atal cost ailadroddus cysoni metrigau gwahanol. Mae dangosfyrddau gonest, wedi'u canolbwyntio ar benderfyniadau'n codi'r gyfradd y mae mewnwelediad yn troi'n weithredu.

Mae cost mabwysiadu'n cynnwys trwyddedu platfform BI, adeiladu a chynnal yr haenen semantig, ymdrech guradu, a hyfforddiant. Pwyswch ef yn erbyn cost peidio â mabwysiadu: dadansoddwyr a chyfarwyddwyr yn gwastraffu oriau'n cysoni ffigurau gwrthdrawiadol, penderfyniadau a wneir ar siartiau camarweiniol, pentwr o ddangosfyrddau heb eu cynnal, ac, mewn lleoliadau cyhoeddus, ymddiriedaeth wedi'i herydu pan fydd rhifau a gyhoeddwyd yn gwrthddweud ei gilydd. I arweinyddiaeth, mae'r ddadl yn syml. Mae haenen semantig lywodraethedig ynghyd â hunanwasanaeth curedig yn wahaniaeth rhwng data'n ased y mae pawb yn ymddiried ynddo a ffynhonnell barhaol o ddryswch ac ailwaith.

## Gwrthbatrymau a pheryglon

- Pob tîm yn cyfrifo metrigau allweddol yn ei ffordd ei hun, gan gynhyrchu rhifau gwrthdrawiadol.
- Dangosfyrddau wedi'u hadeiladu i arddangos popeth yn hytrach na chefnogi penderfyniad.
- Siartiau camarweiniol (echelinau wedi'u torri, echelinau deuol, cylchoedd 3D) sy'n ystumio casgliadau.
- Trin hunanwasanaeth fel dewis arall yn lle llywodraethu yn hytrach na'i ategu.
- Miloedd o ddangosfyrddau hen, dyblyg heb reolaeth cylch bywyd.
- Dangosfyrddau balchder nad oes neb yn gweithredu arnynt, wedi'u camgymryd am ddiwylliant data-yrredig.
- Mestyn BI rhyngweithiol i gynhyrchu dogfennau rheoleiddiol pixel-berffaith.
- Dim ardystiad, felly ni all defnyddwyr wahaniaethu cynnwys ymddiriedig oddi wrth arbrofion.

## Model aeddfedrwydd

1. **Cychwyn.** Caiff adroddiadau eu hadeiladu ad hoc mewn taenlenni, caiff metrigau eu diffinio'n anghyson, ac mae siartiau'n aml yn gamarweiniol. Nid oes haenen semantig, dim ardystiad, a dim curadu, felly rhifau gwahanol yw'r norm.
2. **Datblygu.** Mae offeryn BI ar waith gyda rhai dangosfyrddau a rennir, ond mae diffiniadau metrig yn dal i wahaniaethu ar draws timau. Mae hunanwasanaeth heb ei reoli ac mae ymledu'n dechrau; gall ychydig o grwpiau fodelu metrigau'n ofalus, ond mae'r arfer yn anghyson ac ni chaiff dim ei orfodi ar draws y sefydliad.
3. **Safoni.** Mae haenen semantig yn diffinio metrigau craidd unwaith, wedi'i dogfennu a'i gorfodi ar draws pob offeryn ac adroddiad. Caiff cynnwys ardystiedig ei wahaniaethu oddi wrth un arbrofol, mae hunanwasanaeth yn gweithredu o fewn reiliau diogelwch, caiff safonau delweddu eu cyhoeddi, ac mae rheolaeth cylch bywyd cynnwys yn arfer sefydlog yn hytrach na glanhau achlysurol.
4. **Rheoli.** Caiff yr ystad ddadansoddol ei mesur yn erbyn llinellau sylfaen. Caiff defnydd dangosfwrdd ei ddilyn a chaiff cynnwys nas defnyddir ei feintioli a'i ddiddymu ar gyflymder; caiff nifer y diffiniadau gwahanol o fetrigau allweddol ei fonitro tuag at un; caiff cydymffurfiaeth adolygu siart, mabwysiad hunanwasanaeth, ac amser-i-ateb eu dilyn; a chaiff cost cysoni ac amser arwain newid metrig eu mesur fel bo gwyriad oddi wrth y diffiniadau ardystiedig yn cael ei ddal a'i gywiro ar dystiolaeth.
5. **Cydgysylltu.** Caiff metrigau eu llywodraethu fel APIs â pherchnogion a chofnodion newid, mae dadansoddeg yn rhychwantu o ddisgrifiadol i ragnodol ac yn cysylltu â gweithredu pendant, a chaiff adroddiadau eu hymgorffori ym mhwyntiau'r penderfyniad. Mae'r sefydliad yn ymddiried mewn un fersiwn o'r gwirionedd ym mhobman, yn ffrwyno ymledu'n weithredol, ac yn ailgwmpasu ac yn ail-ardystio ei ddadansoddeg yn barhaus wrth i'r busnes a'i gwestiynau newid.

## Syniadau i'w trafod

- Faint o wahanol ddiffiniadau o'ch metrig pwysicaf sy'n bodoli heddiw?
- Pa un o'ch dangosfyrddau sy'n mewn gwirionedd yn newid penderfyniad, a pha rai sydd ond yn cael eu gwylio?
- Ble mae siart yn eich sefydliad wedi camarwain ei gynulleidfa, yn ddiniwed neu beidio?
- A ydych chi wedi gorfuddsoddi mewn disgrifio'r gorffennol o'i gymharu â diagnosio a gweithredu?
- Beth fyddai haenen ardystio ar gyfer cynnwys yn ei wneud i ymddiriedaeth ac ailddefnydd yn eich sefydliad?
- Sut rydych yn cydbwyso angen dinasyddion neu reoleiddwyr am siartiau gonest â'r tyniad tuag at rai perswadiol?

## Prif negeseuon

- Diffiniwch bob metrig pwysig unwaith mewn haenen semantig lywodraethedig a ddefnyddir ym mhobman.
- Gwthiwch ddadansoddeg i fyny'r ysgol o ddisgrifiadol i ddiagnostig, rhagfynegol, a rhagnodol.
- Galluogwch hunanwasanaeth o fewn reiliau diogelwch; ardystiwch gynnwys ymddiriedig.
- Dyluniwch ddangosfyrddau o amgylch penderfyniadau, nid o amgylch data sydd ar gael.
- Gwnewch bob siart yn onest; deall yw'r nod, nid perswadio.
- Curadwch yn ddidostur a diddymwch gynnwys hen i frwydro yn erbyn ymledu.
- Ymgorffolwch ddadansoddeg ym mhwynt y penderfyniad, a defnyddiwch adrodd gweithredol wedi'i adeiladu at ddiben.

## Cyfeiriadau a darllen pellach

- Edward Tufte, "The Visual Display of Quantitative Information."
- Stephen Few, "Show Me the Numbers" a "Information Dashboard Design."
- Cole Nussbaumer Knaflic, "Storytelling with Data."
- Alberto Cairo, "How Charts Lie."
- Ralph Kimball a Margy Ross, "The Data Warehouse Toolkit."
- Darrell Huff, "How to Lie with Statistics."
- Benn Stancil ac eraill, ysgrifau ar yr haenen semantig a storfeydd metrigau.
