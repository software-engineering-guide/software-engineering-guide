# 3.9 Peirianneg systemau

## Trosolwg a chymhelliant

Mae [peirianneg systemau](https://en.wikipedia.org/wiki/Systems_engineering) yn ddisgyblaeth peiriannu system gymhleth gyfan o'r dechrau i'r diwedd, fel bod ei holl rannau'n gweithio gyda'i gilydd i ateb angen go iawn. Mae'r rhannau'n cynnwys llawer mwy na meddalwedd. Mae system fodern fel arfer yn cyfuno meddalwedd, caledwedd, pobl, data, a phrosesau, ac mae'n rhaid iddi weithredu mewn byd go iawn anniben. Mae peirianneg systemau'n cadw'r rhain i gyd wedi'u halinio ar hyd oes gyfan y system.

Mae hyn yn wahanol i bensaernïaeth meddalwedd. Mae pensaernïaeth meddalwedd (pennod 3.1) yn penderfynu sut mae cydrannau meddalwedd wedi'u strwythuro a sut maen nhw'n siarad â'i gilydd. Mae peirianneg systemau'n eistedd un lefel yn uwch. Mae'n gofyn beth y mae'n rhaid i'r system gyfan ei wneud, sut mae meddalwedd, caledwedd, a gweithredwyr dynol yn rhannu'r gwaith, a sut y byddwch yn profi bod y peth gorffenedig yn gweithio. Ei gartref proffesiynol yw [INCOSE](https://en.wikipedia.org/wiki/International_Council_on_Systems_Engineering), y Cyngor Rhyngwladol ar Beirianneg Systemau, a'i safon angor yw [ISO/IEC/IEEE 15288](https://en.wikipedia.org/wiki/ISO/IEC_15288), sy'n diffinio'r prosesau ar gyfer oes system.

Mae hyn yn bwysig ar gyfer rhaglenni mentrau a llywodraeth mawr am fod eu systemau'n fawr, yn hirhoedlog, ac yn hanfodol o ran diogelwch neu genhadaeth. Mae platfform amddiffyn, system draffig awyr, neu gytser lloerennau'n cyfuno caledwedd wedi'i deilwra, rhannau trydydd parti, meddalwedd wedi'i mewnblannu a chwmwl, a gweithredwyr dynol, ac ni all yr un tîm ddal y cyfan yn eu pennau. Rydych hefyd yn aml yn adeiladu [system o systemau](https://en.wikipedia.org/wiki/System_of_systems): llawer o systemau annibynnol, pob un yn ddefnyddiol ar ei ben ei hun, y mae'n rhaid iddynt gydweithredu i gyflenwi gallu mwy.

Mae'r bennod hon yn cysylltu â gofynion meddalwedd (pennod 2.8), sylfeini pensaernïaeth (pennod 3.1), modelau a dulliau meddalwedd (pennod 2.12), rhyngweithredu a safonau agored (pennod 3.8), a rheoli prosiect (pennod 10.6).

## Egwyddorion allweddol

- **Peiriannwch y cyfan, nid y rhannau.** Mae system yn llwyddo neu'n methu fel cyfan, felly gall optimeiddio un is-system ar ei ben ei hun wneud y cyfan yn waeth.
- **Dilynwch y cylch bywyd.** Mae gan system oes o gysyniad cyntaf i ymddeoliad terfynol. Cynlluniwch ar gyfer y cyfan, nid dim ond yr adeiladu.
- **Traciwch bob gofyniad.** Dylai pob angen fapio i ofyniad, elfen cynllun, a phrawf. Os na allwch ei olrhain, ni allwch ei brofi.
- **Rheolwch ryngwynebau'n fwriadus.** Mae'r rhan fwyaf o fethiannau'n digwydd wrth y ffiniau rhwng rhannau, felly mae rhyngwynebau'n haeddu perchnogaeth a rheolaeth eglur.
- **Gwiriwch a dilyswch ar wahân.** Mae adeiladu'r peth yn gywir (gwiriad) ac adeiladu'r peth cywir (dilysu) yn gwestiynau gwahanol, ac mae angen y ddau ateb arnoch.
- **Disgwyliwch ymddygiad ymddangosiadol.** Mae cyfuno rhannau'n creu ymddygiad nad yw'r un rhan unigol yn ei ddangos. Mae rhywfaint ohono'n bwrpasol, a rhywfaint yn syrpreis annymunol.
- **Cyd-beiriannwch galedwedd a meddalwedd.** Pan fydd y ddau'n rhai teilwredig, mae penderfyniadau yn y naill yn cyfyngu'r llall, felly cynlluniwch nhw gyda'i gilydd.

## Argymhellion

### Rheolwch gylch bywyd llawn y system

Triniwch y system fel un sydd ag oes gyfan, a chynlluniwch bob cam. Mae cylch bywyd cyffredin yn rhedeg: **cysyniad** (deall yr angen ac archwilio opsiynau), **gofynion** (nodi'n union beth y mae'n rhaid i'r system ei wneud), **cynllun** (penderfynu'r bensaernïaeth a'r rhannau), **integreiddio** (dod â'r rhannau at ei gilydd), **gwiriad a dilysu** (profi ei fod yn gweithio a'i fod y system gywir), **gweithrediad** (ei redeg a'i gynnal), a **ymddeoliad** (ei ddadgomisiynu'n ddiogel, gan gynnwys data a gwaredu). Mae ISO/IEC/IEEE 15288 yn rhoi fframwaith proses i chi ar gyfer hyn. Nid oes angen i'r camau fod yn rhaeadr anhyblyg; gallwch ailadrodd, prototeipio, a chyflenwi cynyddrannau. Y pwynt yw eich bod yn mynd i'r afael yn ymwybodol â phob cam, gan gynnwys y rhai drud diweddarach y mae cynlluniau cynnar yn aml yn eu hanwybyddu.

### Cofnodwch anghenion rhanddeiliaid a dyrannwch ofynion gyda thraceadwyedd

Dechreuwch o'r bobl sy'n poeni am y system: defnyddwyr, gweithredwyr, perchnogion, rheoleiddwyr, a'r cyhoedd. Casglwch eu **hanghenion** mewn iaith blaen, yna trowch yr anghenion hynny'n **ofynion** peirianyddol sy'n benodol ac yn brofadwy (gweler pennod 2.8). Nesaf daw **dyrannu gofynion**: neilltuo pob gofyniad ar lefel system i is-system benodol, fel eich bod yn gwybod pa ran sy'n gyfrifol am ei fodloni. Cadwch **fatrics [traceadwyedd](https://en.wikipedia.org/wiki/Requirements_traceability)**, cofnod byw sy'n cysylltu pob angen â'i ofyniad, â'r elfen cynllun sy'n ei fodloni, ac â'r prawf sy'n ei wirio. Mae'n gadael i chi brofi ar unrhyw adeg fod pob angen wedi'i gwmpasu a bod pob rhan yn bodoli am reswm.

### Rheolwch ryngwynebau'n benodol

Mae rhyngwynebau'n lle mae rhannau'n cwrdd, ac yn lle mae systemau'n torri amlaf. Gall rhyngwyneb fod yn gysylltydd ffisegol, protocol rhwydwaith, fformat data, neu weithdrefn ddynol. Ar gyfer pob un, ysgrifennwch **Ddogfen Rheoli Rhyngwyneb** (ICD): manyleb y cytunwyd arni o sut yn union mae dau ran yn cysylltu ac yn cyfnewid gwybodaeth. Rhowch berchennog clir ar bob ochr i bob rhyngwyneb. Mae dibynnu ar fanylebau a rennir, wedi'u cyhoeddi yn hytrach na chysylltyddion untro yn gwneud integreiddio'n llawer haws, sef y ddadl rhyngweithredu ym mhennod 3.8. Rhewwch ryngwynebau'n gynnar lle gallwch, oherwydd mae newid hwyr yn tonni i mewn i bob rhan sy'n ei gyffwrdd.

### Integreiddiwch ac yna gwiriwch a dilyswch

Mae **integreiddio system** yn cyfuno is-systemau i'r cyfan gweithredol, fel arfer mewn camau yn hytrach nag i gyd ar unwaith, fel eich bod yn dod o hyd i broblemau tra eu bod yn dal yn fach. Ar ôl integreiddio daw **[gwiriad a dilysu](https://en.wikipedia.org/wiki/Verification_and_validation)** (V&V), dau wiriad gwahanol. Mae **gwiriad** yn gofyn: a wnaethom adeiladu'r system yn gywir, hynny yw a yw'n bodloni ei gofynion penodedig? Rydych yn gwirio drwy arolygu, dadansoddi, arddangos, a phrofi. Mae **dilysu** yn gofyn: a wnaethom adeiladu'r system gywir, hynny yw a yw'n bodloni anghenion go iawn y rhanddeiliaid mewn defnydd go iawn? Gall system lwyddo mewn gwiriad (mae'n bodloni'r fanyleb) ac eto methu dilysu (roedd y fanyleb yn anghywir). Cynlluniwch y ddau'n gynnar, ac ysgrifennwch ofynion a rhyngwynebau fel y gellir eu gwirio yn y lle cyntaf.

### Mabwysiadwch beirianneg systemau seiliedig ar fodel

Cynhyrchodd peirianneg systemau traddodiadol fynyddoedd o ddogfennau a ddrifftiodd allan o gysoni. Mae **[peirianneg systemau seiliedig ar fodel](https://en.wikipedia.org/wiki/Model-based_systems_engineering)** (MBSE) yn disodli'r pentwr hwnnw ag un model ffurfiol, a rennir, o'r system, y crëir golygfeydd ac adroddiadau ohono. Yr iaith fodelu gyffredin yw **[SysML](https://en.wikipedia.org/wiki/Systems_Modeling_Language)** (Systems Modeling Language), iaith graffigol ar gyfer disgrifio gofynion, strwythur, ymddygiad, a chyfyngiadau system. Am fod popeth yn byw mewn un model cysylltiedig, mae newid yn diweddaru ym mhobman, ac mae traceadwyedd yn dod yn ymholiad yn hytrach na helfa â llaw. Mae MBSE yn cysylltu â'r syniadau modelu ym mhennod 2.12. Mabwysiadwch ef yn raddol, gan ddechrau gyda'r rhannau risg uchaf lle mae model a rennir yn talu ffordd gyflymaf.

### Cymhwyswch feddwl systemau i ymddygiad ymddangosiadol

Ymarferwch [feddwl systemau](https://en.wikipedia.org/wiki/Systems_thinking): rhesymwch am y cyfan a'r perthnasoedd rhwng rhannau, nid dim ond y rhannau fesul un. Dyma sut rydych yn rhagweld **[ymddygiad ymddangosiadol](https://en.wikipedia.org/wiki/Emergence)**: priodweddau sy'n ymddangos dim ond pan fydd rhannau'n cyfuno ac nad yw'r un rhan unigol yn eu dangos. Yn aml, pwrpas y system yw'r ymddangosiad da (mae haid o ddroniau'n cwmpasu ardal na allai'r un drôn unigol ei chwmpasu). Y methiant syrpreis yw'r ymddangosiad drwg (mae dwy is-system ddiogel yn rhyngweithio i greu cyflwr peryglus). Ni allwch brofi ymddangosiad allan o system na wnaethoch chi ei modelu erioed, felly defnyddiwch efelychiad a dadansoddiad perygl strwythuredig i ddod o hyd iddo cyn gweithrediad.

### Cyd-beiriannwch galedwedd a meddalwedd

Pan fydd system yn cynnwys caledwedd deilwredig, peiriannwch y caledwedd a'r meddalwedd gyda'i gilydd, arfer o'r enw **[cyd-ddylunio caledwedd/meddalwedd](https://en.wikipedia.org/wiki/Hardware/software_co-design)**. Mae penderfyniadau'n rhwymo ei gilydd: mae'r caledwedd yn gosod amseru, cof, a therfynau pŵer y mae'n rhaid i'r meddalwedd fyw ynddynt, ac mae anghenion y meddalwedd yn siapio'r hyn y mae'n rhaid i'r caledwedd ei ddarparu. Mae amseroedd arwain caledwedd hir hefyd yn gyrru'r amserlen. Penderfynwch yn gynnar pa swyddogaethau sy'n byw mewn caledwedd a pha rai mewn meddalwedd, ac ailedrychwch ar y rhaniad hwnnw wrth i gyfyngiadau ddod i'r amlwg.

## Cyfaddawdau: manteision ac anfanteision

| Dull | Manteision | Anfanteision / cost |
|---|---|---|
| Trylwyredd peirianneg systemau llawn | Llai o syrpreisys hwyr, traceadwyedd cryf, mwy diogel ac archwiliadwy | Cost ymlaen llaw uchel, dechrau arafach, proses drwm |
| Dull ysgafn / meddalwedd yn unig | Cyflym, rhad, hyblyg ar gyfer cwmpas bach | Yn methu ar systemau mawr aml-ddisgyblaeth, yn colli rhyngwynebau ac ymddangosiad |
| Seiliedig ar fodel (MBSE) | Un ffynhonnell wirionedd, traceadwyedd hawdd, golygfeydd cyson | Cost offer a hyfforddiant, newid diwylliannol, cromlin ddysgu |
| Peirianneg systemau seiliedig ar ddogfennau | Cyfarwydd, cost offer isel, hawdd ei rannu | Mae dogfennau'n drifftio allan o gysoni, mae traceadwyedd â llaw ac yn dueddol o wallau |

Y cyfaddawd canolog yw trylwyredd yn erbyn cyflymder. Mae peirianneg systemau lawn yn llwytho ymdrech ymlaen llaw i gysyniad, gofynion, a gwaith rhyngwyneb. Mae'r ymdrech honno'n ad-dalu ei hun sawl gwaith drosodd ar systemau mawr, hirhoedlog, hanfodol o ran diogelwch, lle gall nam a ddarganfyddir mewn gweithrediad gostio miloedd o weithiau mwy na'r un nam a ddarganfyddir mewn gofynion. Ar gynnyrch bach, byrhoedlog, meddalwedd yn unig, mae'r trylwyredd hwnnw'n orbrofion. Parwch bwysau eich proses â maint, hyd oes, a risg y system. Y modd methiant yw cymhwyso arferion prosiect tafladwy i system a fydd yn rhedeg am ddeg mlynedd ar hugain ac yn cario risg byd go iawn.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Ble ydych chi wedi adeiladu'n union yr hyn a fynnodd y fanyleb ac eto wedi cyflenwi'r system anghywir, a beth fyddai wedi ei ddal?** Mae gwiriad (a wnaethom ei adeiladu'n gywir) a dilysu (a wnaethom adeiladu'r peth cywir) yn ateb cwestiynau gwahanol, a gall system lwyddo ym mhob prawf gwiriad tra'n methu dilysu oherwydd bod y fanyleb ei hun yn anghywir. Ar raglenni mawr caiff y ddau eu cwympo i mewn i "brofi", felly nid oes neb yn dilysu yn erbyn angen gweithredwr go iawn tan yn hwyr, pan fydd trwsio'n costio miloedd o weithiau mwy na newid gofyniad. Dewch ag enghraifft o'r gorffennol lle bodlonodd y system a gyflenwyd ei gofynion ac eto colli'r angen gwirioneddol, a gofynnwch pa weithgaredd dilysu (efelychiad gyda gweithredwyr go iawn, prototeip cynnar yn y maes) fyddai wedi ei ddatgelu'n gynt. Cynlluniwch y ddau wiriad o'r dechrau, ac ysgrifennwch ofynion a rhyngwynebau fel y gellir eu gwirio o gwbl. Mae'r gwahaniaeth yn penderfynu ble rydych yn treulio ymdrech adolygu prin.

2. **Sut ydych chi'n hela am ymddygiad ymddangosiadol drwg cyn i'r system fod mewn gweithrediad, nid wedyn?** Gall cyfuno is-systemau diogel greu cyflyrau peryglus nad yw'r un rhan unigol yn eu dangos, ac ni allwch brofi ymddangosiad allan o system na wnaethoch chi ei modelu erioed. Ar gyfer rhaglen hanfodol o ran diogelwch neu genhadaeth, y rhyngweithiad syrpreis yw'r un sy'n anafu rhywun neu'n methu'r genhadaeth, felly mae'n rhaid ei ganfod cyn gweithrediad byw. Dewch â'ch dull o fodelu'r cyfan (efelychiad, dadansoddiad perygl strwythuredig, model SysML sy'n cwmpasu rhyngweithiadau) a gofynnwch pa ymddygiadau traws-is-system rydych mewn gwirionedd wedi'u harchwilio yn hytrach na'u tybio i ffwrdd. Yn aml, pwrpas y system yw'r ymddangosiad da ac mae'n werth dylunio tuag ato; y methiant y mae'n rhaid i chi beiriannu yn ei erbyn yw'r ymddangosiad drwg. Os mai'ch unig strategaeth integreiddio yw gwifro'r rhannau at ei gilydd a gweld beth sy'n digwydd, rydych yn cynllunio i ddarganfod ymddangosiad mewn cynhyrchu.

3. **Pryd mae'n rhaid rhewi'r penderfyniadau caledwedd amser arwain hir, a sut mae'r terfyn amser hwnnw'n gyrru eich amserlen feddalwedd?** Pan fydd system yn cynnwys caledwedd deilwredig, mae'n rhaid cyd-beiriannu'r ddau: mae'r sglodyn yn gosod terfynau amseru, cof, a phŵer y mae'r meddalwedd yn byw ynddynt, ac mae amseroedd arwain caledwedd yn aml yn dominyddu'r amserlen gyfan. Mae timau sy'n trin meddalwedd fel rhywbeth y gellir ei wahanu'n optimeiddio'n lleol ac yna'n gwrthdaro â chyfyngiadau caledwedd wrth integreiddio, gan golli misoedd. Dewch ag amseroedd arwain caledwedd a'r dyddiad y mae'n rhaid penderfynu rhaniad swyddogaeth caledwedd/meddalwedd erbyn hynny, ac ailedrychwch ar y rhaniad hwnnw wrth i gyfyngiadau ddod i'r amlwg yn hytrach na'i rewi'n ddall. Y cynharaf y byddwch yn penderfynu pa swyddogaethau sy'n byw mewn silicon a pha rai mewn meddalwedd, y lleiaf o wrthdroeon drud rydych yn eu hwynebu. Mae rhyngwynebau rhwng y ddau'n haeddu Dogfen Rheoli Rhyngwyneb a pherchennog ar bob ochr, oherwydd mae newid hwyr yno'n tonni drwy bopeth sy'n ei gyffwrdd.

4. **A allwch chi olrhain un angen rhanddeiliad yr holl ffordd i'r gofyniad, yr elfen cynllun, a'r prawf sy'n ei brofi, a phwy sy'n cadw'r cyswllt hwnnw'n fyw?** Traceadwyedd yw'r hyn sy'n gadael i chi ddangos ar unrhyw adeg fod pob angen wedi'i gwmpasu a bod pob rhan yn bodoli am reswm, ac eto ar raglen fawr mae'r matrics yn pydru'r eiliad nad oes neb yn berchen arno. Mae'r tyniad cystadleuol yn real: mae peirianwyr yn profi traceadwyedd fel baich biwrocrataidd, ac mae matrics a gynhelir â llaw'n drifftio allan o ddyddiad yn gynt na newid y cynllun. Dewch ag un edefyn gwirioneddol o raglen gyfredol a cheisiwch ei gerdded o'r dechrau i'r diwedd yn yr ystafell, o angen rhanddeiliad wedi'i enwi, i'r gofyniad a ddyrannwyd, i'r is-system a'r elfen cynllun sy'n ei fodloni, i'r prawf gwiriad, a nodwch ble mae'r gadwyn yn torri. Penderfynwch pwy sy'n berchen ar y matrics ac a ddylai fyw mewn model lle mae traceadwyedd yn ymholiad yn hytrach na helfa â llaw. Ar gyfer rhaglenni mentrau a llywodraeth, mae'r matrics hefyd yn arteffact archwilio y mae rheoleiddwyr ac awdurdodau caffael yn ei fynnu, felly mae cadwyn doredig yn gwneud mwy na arafu peirianneg; gall atal ardystiad neu daliad.

5. **A yw dull seiliedig ar fodel yn werth ei gost offer a diwylliant i chi, neu a fyddai'n dod yn silff-nwyddau drud?** Mae peirianneg systemau seiliedig ar ddogfennau'n gyfarwydd ac yn rhad i'w offeru, ond mae ei ddogfennau'n drifftio allan o gysoni a'i draceadwyedd â llaw ac yn dueddol o wallau; mae MBSE yn disodli'r pentwr ag un model cysylltiedig, am bris offer, hyfforddiant, a newid diwylliannol gwirioneddol. Mae'r naill begwn a'r llall yn ddrud: hepgorwch MBSE ar raglen fawr aml-ddisgyblaeth a byddwch yn talu mewn syrpreisys integreiddio, ei fabwysiadu heb y ddisgyblaeth i gadw'r model yn gyfredol ac mae'n pydru'n silff-nwyddau gwaeth na dim model o gwbl. Dewch â darlleniad gonest o'ch aeddfedrwydd offer, pwy ar y tîm sy'n gallu mewn gwirionedd awduro a chynnal model SysML, a pha un is-system risg uchel a allai beilota'r dull lle mae model a rennir yn talu ffordd gyflymaf. Penderfynwch yn raddol yn hytrach na gorchymyn y sefydliad cyfan ar unwaith. Ar gyfer menter fawr neu raglen lywodraeth gyda llawer o gyflenwyr, pwyswch a yw model a rennir yr unig ffordd realistig o gadw gofynion, rhyngwynebau, a phrofion yn gyson ar draws contractwyr sydd fel arall yn cyfnewid dogfennau hen.

6. **A yw eich cynllun cylch bywyd o ddifrif yn ariannu gweithrediad ac ymddeoliad, neu a yw'n stopio'n dawel ar lansiad?** Y camau sy'n dominyddu cost gyfan system hirhoedlog, ei rhedeg am ddegawdau a'i dadgomisiynu'n ddiogel, yw'r rhai y mae cynlluniau cynnar yn eu hanwybyddu'n rheolaidd, oherwydd mae'r pwysau bob amser i gyflenwi. Yr ystyriaeth gystadleuol yw bod arian a sylw brinnaf yn union pan fydd y camau diweddarach hyn yn teimlo bellaf i ffwrdd, felly caiff gweithrediad, cynnal a chadw, mudo data, a gwaredu eu gohirio nes eu bod yn dod yn sgrialu drud, peryglus. Dewch â'r cynllun cylch bywyd cyfredol a gwiriwch a yw'n enwi perchnogion, cyllidebau, a meini prawf ymadael ar gyfer gweithrediad ac ymddeoliad, neu a yw'n trin lansiad fel y llinell derfyn. Gofynnwch beth sy'n digwydd i'r data a'r caledwedd ar ddiwedd oes, a phwy sy'n talu am y blynyddoedd o gynnal a chadw rhwng hynny. Ar gyfer systemau mentrau a llywodraeth y mae'n rhaid iddynt redeg am ugain neu ddeg mlynedd ar hugain ac yna ymddeol o dan graffu cyhoeddus, gall dadgomisiynu heb ei gynllunio dorri rhwymedigaethau rheoleiddiol, amgylcheddol, neu gadw cofnodion, felly mae ymddeoliad yn perthyn yn y cynllun a'r gyllideb o'r adolygiad cysyniad cyntaf.

## Lens sector

**Cwmni newydd.** Ni all tîm bach redeg rhaglen beirianneg systemau ffurfiol ac ni ddylai geisio gwneud hynny, ond gall barhau i drin cadarnwedd, ap, a chwmwl fel un system yn hytrach na thri phrosiect ar wahân. Ysgrifennwch un ddogfen rhyngwyneb fer sy'n pinio sut mae'r rhannau'n siarad, cadwch dabl syml sy'n cysylltu pob angen cwsmer â'r rhan sy'n ei fodloni, a hepgorwch y broses drwm. Eich adnodd prinnaf yw sylw peirianyddol, felly treuliwch ymdrech traceadwyedd dim ond lle byddai rhagdybiaeth anghywir wrth ffin yn torri'r cynnyrch yn dawel yn y maes.

**Busnes bach.** Heb beiriannydd systemau penodedig a chyllideb dynn, pwyswch ar safonau cyhoeddedig ac is-systemau a brynir yn hytrach nag integreiddio pwrpasol y mae'n rhaid i chi ei ddylunio a'i wirio'ch hun. Ffafriwch werthwyr sy'n datgelu manylebau rhyngwyneb clir fel bod y rhannau'n ffitio heb gysylltydd pwrpasol y mae'n rhaid i chi fod yn berchen arno am byth. Fframiwch y dewis adeiladu-yn-erbyn-prynu o amgylch pa ryngwynebau y gallwch eu rheoli a'u gwirio'n realistig dros oes y cynnyrch, a phrynwch y gweddill.

**Menter.** Ar raddfa fawr y broblem yw cysondeb ar draws llawer o dimau a chyflenwyr: proses cylch bywyd a rennir wedi'i halinio ag ISO/IEC/IEEE 15288, Dogfen Rheoli Rhyngwyneb a pherchennog wedi'i enwi ar gyfer pob ffin cyflenwr, a thraceadwyedd o'r dechrau i'r diwedd fel nad yw un newid cydran yn sbarduno sgrialu ar draws y rhaglen gyfan. Buddsoddwch mewn MBSE lle mae model a rennir yn cadw gofynion, rhyngwynebau, a phrofion wedi'u halinio ar draws contractwyr. Llywodraethwch y broses fel bod gwiriad a dilysu'n aros yn wahanol a bod pob gofyniad wedi'i ddyrannu i ran gyfrifol.

**Llywodraeth.** Mae rheolau caffael, tryloywder, ac atebolrwydd cyhoeddus yn siapio pob dewis. Nodwch broses beirianneg systemau, traceadwyedd, a thystiolaeth V&V yn y contract, mynnwch fod cyflenwyr yn cyflenwi dogfennau rheoli rhyngwyneb ac arteffactau cylch bywyd y gallwch eu harchwilio, a chadwch ddilysiad diogelwch a chenhadaeth ar gyfer adolygiad annibynnol gyda gweithredwyr go iawn cyn unrhyw drosglwyddiad byw. Cynlluniwch ac ariannwch weithrediad ac ymddeoliad yn benodol, oherwydd mae rhaglen gyhoeddus yn atebol am y cylch bywyd llawn, gan gynnwys dadgomisiynu diogel a chadw cofnodion.

## Enghreifftiau

**Cwmni newydd.** Ni all cwmni newydd caledwedd pedwar person sy'n adeiladu synhwyrydd cysylltiedig fforddio rhaglen beirianneg systemau ffurfiol, ond mae'n dal i drin y cynnyrch fel un system o gadarnwedd, ap symudol, a chefnwlad cwmwl yn hytrach na thri phrosiect ar wahân. Maen nhw'n ysgrifennu un ddogfen rhyngwyneb fer sy'n pinio sut mae'r ddyfais, yr ap, a'r gweinydd yn siarad (fformatau neges, unedau, codau gwall) ac yn cadw tabl syml sy'n cysylltu pob angen cwsmer â'r rhan sy'n ei fodloni. Pan fydd sglodyn synhwyrydd rhatach yn gorfodi newid cadarnwedd, mae'r rhyngwyneb a rennir hwnnw'n dangos ar unwaith beth y mae'n rhaid i'r ap a'r cefnwlad ei addasu, felly nid yw cyfnewid cydran yn torri'r cynnyrch yn dawel yn y maes.

**Menter.** Mae gweithgynhyrchwr modurol byd-eang yn adeiladu platfform cerbyd trydan newydd: system o feddalwedd (rheoli batri, cymorth gyrrwr, adloniant), caledwedd (moduron, synwyryddion, sglodion), a ffactorau dynol, ynghyd â llawer o gyflenwyr, pob un yn cyflenwi is-systemau. Mae'r cwmni'n rhedeg rhaglen beirianneg systemau. Mae anghenion rhanddeiliaid yn bwydo gofynion wedi'u dyrannu, mae gan bob rhyngwyneb cyflenwr Ddogfen Rheoli Rhyngwyneb, ac mae model SysML yn clymu gofynion i'r cynllun i'r profion. Pan fydd cyflenwr cell batri'n newid cydran, mae'r model traceadwyedd yn dangos yn union pa ofynion, rhyngwynebau, a phrofion yr effeithir arnynt, felly caiff y newid ei gynnwys yn hytrach na sbarduno sgrialu ar draws y rhaglen gyfan.

**Llywodraeth.** Mae awdurdod mordwyo awyr cenedlaethol yn moderneiddio ei system rheoli traffig awyr, system o systemau hanfodol o ran diogelwch sy'n rhychwantu radarau, gorsafoedd gwaith rheolwyr, cyfathrebiadau, a meddalwedd, wedi'i weithredu rownd y cloc. Mae'r rhaglen yn dilyn ISO/IEC/IEEE 15288 ar draws y cylch bywyd llawn. Mae gwiriad yn profi bod pob is-system yn bodloni ei fanyleb, ac mae dilysu drwy efelychiad gyda rheolwyr go iawn yn profi bod y system integredig yn cefnogi gweithrediadau diogel cyn i unrhyw draffig byw ddibynnu arni. Mae V&V trylwyr yn gadael i'r awdurdod drosglwyddo mewn camau, gyda cefn wrth gefn ar bob cam, oherwydd yma mae methiant ymddangosiadol heb ei brofi'n ddigwyddiad diogelwch cyhoeddus.

## Achos busnes: cymhellion, ROI, a TCO

Y cymhelliant yw bod namau'n dod yn esbonyddol ddrytach po hwyraf y byddwch yn dod o hyd iddynt. Mae gwall gofyniad a ddelir yn ystod cam y gofynion yn costio bron dim i'w drwsio. Gall yr un gwall a ddelir mewn gweithrediad gostio miloedd o weithiau mwy, ac ar system hanfodol o ran diogelwch gall gostio bywydau, galwadau'n ôl, neu genhadaeth a fethodd. Mae peirianneg systemau'n symud darganfod namau i mewn i'r camau cynnar rhad.

Ar gyfer **enillion ar fuddsoddiad** (ROI, gwerth a enillwyd o'i gymharu â chost a wariwyd), yr enillion yw ailwaith a osgowyd, llai o fethiannau integreiddio, a rhaglenni sy'n taro amserlen a chyllideb yn hytrach na goramser. Mae astudiaethau diwydiant o raglenni mawr yn dod o hyd dro ar ôl tro fod ymdrech peirianneg systemau gref yn cydberthyn â goramserau llai. Ar gyfer **cyfanswm cost perchnogaeth** (TCO, cost oes lawn adeiladu, rhedeg, ac ymddeol system), mae peirianneg systemau'n cyfrif am y camau gweithrediad ac ymddeoliad sy'n dominyddu cost hirdymor ond y mae prosiectau achlysurol yn eu hanwybyddu. Mae dylunio ar gyfer cynhaliadwyedd, rhyngwynebau, a gwaredu o'r dechrau'n gostwng cost y degawdau y mae'r system yn eu treulio mewn gwasanaeth. Gweler rheoli prosiect (pennod 10.6).

## Gwrth-batrymau a pheryglon

- **Cynllun mawr ymlaen llaw heb ailadrodd.** Trin y cylch bywyd fel rhaeadr unffordd anhyblyg, fel eich bod yn dysgu bod y gofynion yn anghywir dim ond ar ôl adeiladu popeth.
- **Gofynion heb draceadwyedd.** Pentwr o ofynion nad oes neb yn eu cysylltu â chynllun neu brofion, felly ni allwch brofi cwmpas na chyfiawnhau unrhyw ran.
- **Anwybyddu rhyngwynebau.** Tybio y bydd is-systemau jyst yn ffitio at ei gilydd, yna colli misoedd wrth integreiddio i anghydweddiadau ffin nad oedd neb yn berchen arnynt.
- **Gwiriad heb ddilysu.** Profi bod y system yn bodloni ei fanyleb tra byth yn gwirio a oedd y fanyleb yn cyfateb i anghenion go iawn, yna cyflenwi'r system anghywir.
- **Trin meddalwedd fel rhywbeth ar wahân.** Timau meddalwedd yn optimeiddio'n lleol tra'n anwybyddu cyfyngiadau caledwedd, amseru, a gweithredwyr dynol.
- **MBSE fel silff-nwyddau.** Adeiladu model unwaith, yna gadael iddo bydru allan o gysoni fel ei fod yn dod yn waeth na dim model.
- **Hepgor cynllunio ymddeoliad.** Dim cynllun ar gyfer dadgomisiynu, mudo data, na gwaredu, felly mae diwedd oes yn dod yn sgrialu drud, peryglus.

## Model aeddfedrwydd

**Lefel 1: Cychwyn.** Mae peirianneg systemau'n achlysurol ac yn ymatebol. Mae gofynion yn byw mewn dogfennau gwasgaredig, darganfyddir rhyngwynebau wrth integreiddio, ac mae gwiriad yn ddim ond beth bynnag o brofi sy'n digwydd cael ei wneud. Mae rhaglenni mawr yn rheolaidd yn goramser ac yn synnu'r tîm yn hwyr.

**Lefel 2: Datblygu.** Mae arferion sylfaenol yn bodoli ar raglenni mawr. Caiff gofynion eu cofnodi a'u llinellu sylfaen, mae gan ryngwynebau allweddol ddogfennau rheoli, ac mae cynllun gwiriad. Mae arfer yn anghyson rhwng timau ac yn dibynnu ar unigolion yn hytrach na dull a rennir.

**Lefel 3: Safoni.** Mae peirianneg systemau'n ddisgyblaeth ddogfennedig, ar draws y sefydliad wedi'i halinio ag ISO/IEC/IEEE 15288 ac wedi'i gorfodi ar draws timau. Cynlluniir y cylch bywyd llawn, cynhelir traceadwyedd o'r dechrau i'r diwedd, rheolir rhyngwynebau'n ffurfiol, ac mae gwiriad a dilysu'n wahanol ac wedi'u cynllunio. Defnyddir MBSE ar raglenni cymhleth.

**Lefel 4: Rheoli.** Caiff peirianneg systemau ei mesur a'i rheoli gyda data. Mae'r sefydliad yn olrhain metrigau yn erbyn llinellau sylfaen: anwadalrwydd gofynion a chwmpas traceadwyedd, namau rhyngwyneb a ddarganfyddir wrth integreiddio, cyfraddau llwyddiant gwiriad a dilysu, a gollyngiad namau fesul cam cylch bywyd (faint o namau sy'n dianc o bob cam i'w dal wedyn ar gost uwch). Mae adolygiadau'n llywio rhaglenni ar y rhifau hyn, ac mae trothwyon yn sbarduno gweithredu cywiro yn hytrach nag ymladd tân ar ôl y ffaith.

**Lefel 5: Cyfluniadu.** Caiff peirianneg systemau ei gwella'n barhaus a'i integreiddio ar draws y sefydliad. Mae model MBSE byw yn un ffynhonnell wirionedd, mae traceadwyedd wedi'i awtomeiddio, mae efelychiad yn rhagweld ymddygiad ymddangosiadol cyn adeiladu, ac mae metrigau o raglenni'r gorffennol yn bwydo'r nesaf. Caiff caledwedd a meddalwedd eu cyd-beiriannu fel mater o drefn, ac mae'r broses yn addasu wrth i raglenni, cyflenwyr, a risgiau symud.

## Syniadau i'w trafod

- Ble mae'r llinell rhwng peirianneg systemau a phensaernïaeth meddalwedd yn eich sefydliad, a phwy sy'n berchen ar y gofod rhyngddynt?
- Ar eich rhaglen fwyaf, a allwch chi olrhain un angen rhanddeiliad yr holl ffordd i'r prawf sy'n ei wirio? Os na, beth fyddai ei angen?
- Pa rai o'ch methiannau diweddar a ddigwyddodd wrth ryngwyneb, a phwy oedd yn berchen arno?
- A fyddai MBSE'n talu ffordd i chi, neu a fyddai'n dod yn silff-nwyddau drud o ystyried eich diwylliant a'ch offer?
- A yw eich cynllun cylch bywyd o ddifrif yn mynd i'r afael â gweithrediad ac ymddeoliad, neu a yw'n stopio'n dawel ar lansiad?

## Prif gasgliadau

- Mae peirianneg systemau'n peiriannu'r system gyfan (meddalwedd, caledwedd, pobl, a phrosesau) o'r dechrau i'r diwedd, ac mae'n wahanol i bensaernïaeth meddalwedd.
- Cynlluniwch y cylch bywyd llawn, o gysyniad drwy ofynion, cynllun, integreiddio, V&V, gweithrediad, ac ymddeoliad.
- Traciwch bob angen i ofyniad, elfen cynllun, a phrawf, a dyrannwch bob gofyniad i ran gyfrifol.
- Rheolwch ryngwynebau'n benodol gyda pherchnogaeth a dogfennau rheoli clir, oherwydd ffiniau yw lle mae systemau'n torri.
- Mae gwiriad (ei adeiladu'n gywir) a dilysu (adeiladu'r peth cywir) yn wiriadau gwahanol, ac mae angen y ddau arnoch.
- Defnyddiwch MBSE a SysML ar gyfer un ffynhonnell wirionedd gysylltiedig, a defnyddiwch feddwl systemau i ragweld ymddygiad ymddangosiadol.
- Parwch bwysau eich proses â maint, hyd oes, a risg y system.

## Cyfeiriadau a darllen pellach

- INCOSE, *INCOSE Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities*
- ISO/IEC/IEEE 15288, *Systems and Software Engineering: System Life Cycle Processes*
- ISO/IEC/IEEE 29148, *Systems and Software Engineering: Requirements Engineering*
- Sanford Friedenthal, Alan Moore, and Rick Steiner, *A Practical Guide to SysML: The Systems Modeling Language*
- NASA, *NASA Systems Engineering Handbook* (NASA/SP-2016-6105)
- Andrew P. Sage and William B. Rouse, *Handbook of Systems Engineering and Management*
- Dennis M. Buede and William D. Miller, *The Engineering Design of Systems: Models and Methods*
- Donella H. Meadows, *Thinking in Systems: A Primer*
- Eberhardt Rechtin and Mark W. Maier, *The Art of Systems Architecting*
- U.S. Department of Defense, *Defense Acquisition Guidebook* (systems engineering guidance)
