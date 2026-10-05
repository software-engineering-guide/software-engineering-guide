# 2.16 Peirianneg perfformiad

## Trosolwg a chymhelliant

Peirianneg perfformiad yw'r grefft o wneud cod yn ddigon cyflym, yn fwriadol, gan ddefnyddio mesuriad yn hytrach na greddf. Mae'r bennod hon yn gweithio ar lefel cod a chydrannau: ffwythiannau, dolenni, strwythurau data, ymholiadau, dyraniadau, a'r ffordd y mae un gwasanaeth yn treulio ei amser. Mae'n gyd-destun i bennod 3.5, sy'n ymdrin â pherfformiad ar lefel system (graddio allan, cydbwyso llwyth, capasiti, a chydnerthedd). Pan fo system yn araf, mae pennod 3.5 yn gofyn faint o beiriannau sydd eu hangen arnoch; mae'r bennod hon yn gofyn pam mae un peiriant yn gwneud cymaint o waith yn y lle cyntaf. Fel arfer bydd angen y ddau arnoch, a lefel y cod yw lle mae swm syfrdanol o gost ac oedi'n cuddio mewn gwirionedd.

I dimau mawr, mae'r ddisgyblaeth hon yn bwysig oherwydd bod perfformiad yn dirywio'n dawel. Nid un comit sengl sy'n gwneud gwasanaeth yn araf, ond mil o rai bach, pob un yn ychwanegu galwad cronfa ddata neu ddolen ddiderfyn. Heb ddull a rennir ar gyfer mesur, cyllidebu, a phorthi perfformiad, dim ond pan fydd cwsmer yn cwyno neu lansiad yn toddi y byddwch yn darganfod y pydredd. Mae dull yn troi perfformiad o ymladdiad tân arwrol yn briodwedd arferol rydych yn ei diogelu.

I fentrau, mae perfformiad yn arian: mae cod cyflymach yn golygu llai o beiriannau, biliau cwmwl is, a'r gallu i fodloni [cytundeb lefel gwasanaeth](https://en.wikipedia.org/wiki/Service-level_agreement) (SLA) ar oedi heb ddarparu gormod. I lywodraeth, mae perfformiad yn fynediad: mae tudalen sy'n llwytho ar hen ffôn dros gysylltiad symudol gwan yn wahaniaeth rhwng dinesydd yn cwblhau hawliad budd-daliadau a rhoi'r gorau iddi. Mae angen tystiolaeth meincnod y gellir ei hatgynhyrchu ar systemau cyhoeddus hefyd, oherwydd bydd cyrff caffael a goruchwylio'n gofyn i chi brofi'r rhifau, nid dim ond eu haeru.

## Egwyddorion allweddol

- **Mesurwch cyn i chi optimeiddio.** Nid yw'r tagfa bron byth lle rydych chi'n dyfalu. Proffiliwch, yna gweithredwch.
- **Osgowch optimeiddio cynamserol.** Mae rhybudd Donald Knuth yn dal: mae optimeiddio cod nad yw'n bwysig yn costio eglurder ac yn prynu dim.
- **Diffiniwch "digon cyflym" fel rhif.** Mae cyllideb perfformiad gyda tharged a phersentil yn troi barn yn basio neu fethu.
- **Mae cyfartaledd yn dweud celwydd; mae persentiliau'n dweud y gwir.** Y gynffon (p99) yw'r hyn y mae defnyddwyr yn ei deimlo, nid y cymedr.
- **Mae enillion algorithmig yn curo mân-diwnio.** Mae dosbarth cymhlethdod gwell yn rhagori ar unrhyw faint o gyfrwystra ffactor cyson.
- **Mae oedi a thrwybwn yn nodau gwahanol.** Gall gwella un waethygu'r llall; gwybyddwch pa un rydych chi'n ei brynu.
- **Meincnodwch yn onest neu ddim o gwbl.** Mae cynhesu, amrywiant, a llwyth gwaith cynrychioliadol yn gwahanu rhifau go iawn oddi wrth ffuglen.
- **Porthwch berfformiad mewn CI, gwyliwch ef mewn cynhyrchiad.** Mae atchweliadau a ddelir cyn uno'n rhad; wedi'u dal gan ddefnyddwyr, yn ddrud.

## Argymhellion

### Mesurwch yn gyntaf, a phroffiliwch cyn i chi gyffwrdd â llinell

Y rheol hynaf yn y maes hwn yw'r un a anwybyddir fwyaf: dewch o hyd i'r tagfa cyn i chi optimeiddio. Estynnwch am [broffiliwr](https://en.wikipedia.org/wiki/Profiling_(computer_programming)), teclyn sy'n samplu neu'n offeryno rhaglen sy'n rhedeg i ddangos lle mae'n treulio amser a chof. Proffiliwch CPU (pa ffwythiannau sy'n llosgi cylchoedd), cof a dyraniad (beth sy'n cael ei ddyrannu a pha mor aml, gan fod cyfnewid dyraniadau'n gyrru seibiannau casglu sbwriel), ac I/O (amser a dreulir yn aros am ddisg, rhwydwaith, neu gronfa ddata). Mae [graff fflam](https://en.wikipedia.org/wiki/Flame_graph), delweddiad wedi'i bentyrru lle mae pob blwch yn ffwythiant a'i led yn amser a dreuliwyd, yn gwneud y gost drechol yn amlwg ar unwaith: chwiliwch am y blychau lletaf, nid y pentyrrau dyfnaf. Optimeiddiwch y gost fwyaf yn gyntaf, ail-fesurwch, a stopiwch pan gyrhaeddwch y gyllideb. Mae hyn yn cysylltu ag arferion arsylladwyedd pennod 9.2, oherwydd mae proffil cynhyrchiad yn curo unrhyw ddyfaliad a wneir o liniadur.

Gwarchodwch yn erbyn y gwrthwyneb hefyd. Llinell lawn Knuth yw mai optimeiddio cynamserol yw gwraidd llawer o ddrygioni, a bwriadai hynny am yr aneffeithlonrwydd bach sy'n eich temtio i aberthu cod darllenadwy am gyflymder dychmygol. Ysgrifennwch y fersiwn eglur yn gyntaf, mesurwch, a dim ond optimeiddiwch y cod y mae'r proffiliwr yn ei gyhuddo.

### Diffinio beth mae "digon cyflym" yn ei olygu gyda chyllidebau perfformiad

Nid rhinwedd yn yr haniaethol yw cyflymder; targed ydyw rydych naill ai'n ei fodloni neu'n ei fethu. Gosodwch **gyllideb perfformiad**: terfyn diriaethol megis "oedi talu p99 o dan 300ms" neu "mae'r pwynt terfyn hwn yn dyrannu o dan 1MB fesul cais." Cysylltwch ef â rhywbeth y mae defnyddwyr neu'r busnes yn ei deimlo, a mynegwch ef fel **persentil**, nid cyfartaledd, oherwydd mae'r cymedr yn cuddio'r gynffon araf lle mae defnyddwyr go iawn yn byw. Os yw 1% o geisiadau'n cymryd 5 eiliad, gall eich cyfartaledd edrych yn iawn tra bod cyfran ystyrlon o gwsmeriaid yn dioddef. Mae cyllidebau'n rhoi diffiniad a rennir, na ellir dadlau yn ei erbyn, o 'wedi'i orffen' i dîm a llinell y mae atchweliad yn ei chroesi'n weladwy.

### Estyn am effeithlonrwydd algorithmig cyn micro-optimeiddio

Daw'r enillion mwyaf, rhataf o [effeithlonrwydd algorithmig](https://en.wikipedia.org/wiki/Algorithmic_efficiency), sut mae'r gwaith yn tyfu wrth i'r mewnbwn dyfu, a ddisgrifir gyda [nodiant Big O](https://en.wikipedia.org/wiki/Big_O_notation) (ffordd o ddosbarthu cyfradd twf, fel bod trefnu O(n log n) yn graddio'n well o lawer nag un O(n sgwâr)). Mae dolen nythog sy'n anweledig ar ddeg eitem yn dod yn drychineb ar ddeng mil. Cyn i chi diwnio ffwythiant poeth â llaw, gofynnwch a yw'n gwneud gormod o waith yn sylfaenol: ymholiad N+1 damweiniol, sgan llinol a ddylai fod yn chwiliad hash, neu waith ailadroddus y gellid ei femoeiddio. Mae hyn yn cysylltu â sylfeini algorithmig pennod 2.13. Ni all unrhyw faint o diwnio ffactor cyson achub y dosbarth cymhlethdod anghywir.

### Gwahaniaethu oedi oddi wrth drwybwn, a pharchu'r gynffon

**Oedi** yw pa mor hir mae un weithred yn ei gymryd; **trwybwn** yw sawl gweithred sy'n cwblhau fesul uned amser. Nid ydynt yn nod cyffelyb, a gall optimeiddio un niweidio'r llall. Mae bathu'n gwella trwybwn ond yn ychwanegu oedi at yr eitem gyntaf yn y bathiad; mae ychwanegu gweithwyr cyfochrog yn codi trwybwn ond gall waethygu oedi'r gynffon drwy gystadleuaeth. Penderfynwch pa un y mae eich defnyddwyr ei angen mewn gwirionedd. A gwyliwch y gynffon bob amser: oedi p95 a p99, y 5% a'r 1% arafaf o geisiadau, oherwydd ar raddfa mae defnyddiwr yn gwneud llawer o geisiadau ac yn taro'r gynffon yn aml. Adroddwch bersentiliau, rhybuddiwch arnynt, a chyllidebwch ar eu cyfer.

### Gwybod terfynau cyfochredd

Pan fyddwch yn cyfochri, cofiwch [ddeddf Amdahl](https://en.wikipedia.org/wiki/Amdahl%27s_law): mae'r cyflymiad o ychwanegu prosesyddion wedi'i gapio gan y gyfran o'r gwaith y mae'n rhaid iddo redeg yn gyfresol. Os yw 10% o swydd yn gynhenid gyfresol, ni fydd unrhyw nifer o greiddiau'n mynd â chi y tu hwnt i gyflymiad 10x. Mae cydamseredd (strwythuro gwaith fel y gall tasgau wneud cynnydd yn annibynnol) a chyfochredd (eu gweithredu'n wirioneddol ar yr un pryd) yn ychwanegu cymhlethdod go iawn, o gyflyrau ras i orbenion cydgysylltu. Mesurwch y gyfran gyfresol cyn i chi dybio y bydd mwy o edafedd yn eich achub, a byddwch yn onest bod y fersiwn gywir symlaf yn ddigon cyflym yn aml.

### Defnyddio storfa-dros-dro a lleoliad data, a pharchu eu costau

Mae [storfa-dros-dro](https://en.wikipedia.org/wiki/Cache_(computing)), stôr cyflym o ganlyniadau a gyfrifwyd yn ddiweddar neu'n ddrud, yr offeryn perfformiad mwyaf pwerus sydd gennych a'r un mwyaf peryglus. Mae sylw ffraeth Phil Karlton mai'r ddwy broblem anodd mewn gwyddoniaeth gyfrifiadurol yw dirymu storfa-dros-dro ac enwi pethau yn rhybudd: mae storfa-dros-dro hen yn gweini atebion anghywir, a rhesymeg dirymu yw lle mae namau cynnil yn magu. Storiwch-dros-dro yn fwriadol, gosodwch ddyddiadau dod i ben, a gwybyddwch eich stori gywirdeb cyn i chi optimeiddio'r gyfradd taro. Ar y lefel isaf, mae [lleoliad cyfeirio](https://en.wikipedia.org/wiki/Locality_of_reference), cadw data a ddefnyddir gyda'i gilydd yn agos at ei gilydd mewn cof, yn manteisio ar hierarchaeth storfa-dros-dro'r CPU ac yn gallu gwneud cod sawl gwaith yn gyflymach heb newid algorithmig, drwy droi methiannau storfa-dros-dro yn drawiadau. Mae araeau cyfagos yn curo strwythurau sy'n dilyn pwyntyddion am y rheswm hwn. Mae hyn yn croestorri â dewisiadau cynllun data ym mhennod 3.4.

### Meincnodi'n onest a drwgdybio microfeincnodau

Mae meincnod sy'n dweud celwydd yn waeth na dim un, oherwydd mae'n rhoi hyder ffug. Cynheswch cyn i chi fesur, fel eich bod yn amseru ymddygiad cyflwr sefydlog yn hytrach na chychwyn unwaith a chrynhoi ar-y-pryd. Rhedwch lawer o ailadroddau ac adroddwch yr amrywiant, nid un rhif lwcus sengl. Defnyddiwch lwyth gwaith cynrychioliadol gyda meintiau a dosraniadau data realistig, oherwydd mae microfeincnod ar fewnbwn tegan yn aml yn mesur gallu'r crynhoydd i ddileu eich prawf yn hytrach na chyflymder go iawn y cod. Byddwch yn wyliadwrus o'r trapiau clasurol: gwerth y mae'r optimeiddiwr yn profi nas defnyddir ac yn ei dynnu, dolen y mae'r amser rhedeg yn ei chodi allan, neu storfa-dros-dro sy'n gynnes yn y meincnod ac yn oer mewn cynhyrchiad. Pan fo amheuaeth, mesurwch y llwybr cyfan, nid y ffwythiant ynysig.

### Porthi perfformiad mewn CI ac arsylwi arno mewn cynhyrchiad

Gwnewch berfformiad yn briodwedd y mae'r biblinell yn ei diogelu. Ychwanegwch brofion perfformiad at strategaeth pennod 2.4, gyda phyrth atchweliad sy'n methu'r adeiladwaith pan fydd meincnod neu gyllideb allweddol yn gwaethygu y tu hwnt i drothwy. Mae hyn yn dal y creep araf cyn iddo uno. Yna caewch y ddolen mewn cynhyrchiad gyda thelemetreg pennod 9.2: traciwch bersentiliau oedi go iawn, cyfraddau dyraniad, ac ymholiadau araf yn erbyn eich cyllidebau, oherwydd mae traffig cynhyrchiad yn dod o hyd i'r achosion na wnaeth eich meincnodau erioed eu dychmygu.

## Cyfaddawdau: manteision ac anfanteision

| Dull | Manteision | Anfanteision |
|---|---|---|
| Optimeiddio nawr, ar sail greddf | Yn teimlo'n gynhyrchiol; ennill lwcus achlysurol | Fel arfer yn diwnio'r cod anghywir; yn ychwanegu cymhlethdod heb ennill |
| Mesur yn gyntaf, yna optimeiddio | Yn targedu'r tagfa go iawn; yn seiliedig ar dystiolaeth | Yn gofyn am offer a disgyblaeth; yn arafach i ddechrau |
| Storio-dros-dro | Enillion mawr o ran oedi a thrwybwn | Namau dirymu; data hen; cost cof |
| Mwy o gyfochredd | Trwybwn uwch ar waith cyfochrog | Nenfwd Amdahl; cystadleuaeth; namau cydamseredd |
| Micro-optimeiddio | Yn gwasgu ffactorau cyson | Nenfwd bach; yn niweidio darllenadwyedd; yn aml yn sŵn |
| Gwelliant algorithmig | Mae enillion yn graddio gyda maint mewnbwn | Yn gofyn am ddadansoddiad; weithiau ailysgrifennu mwy |
| Pyrth perfformiad CI | Yn atal atchweliadau'n gynnar ac yn rhad | Mae meincnodau ansefydlog yn erydu ymddiriedaeth; angen amgylchedd sefydlog |

Y tyndra canolog yw ymdrech yn erbyn enillion, a'r datrysiad yw mesuriad. Mae gan waith perfformiad enillion sy'n lleihau'n sydyn: gallai'r ateb cyntaf a arweinir gan broffil haneru oedi, gallai'r degfed grafu canran tra'n dyblu cymhlethdod cod. Rydych yn ei ddatrys drwy wrthod optimeiddio heb rif yn eich llaw a chyllideb i'w chyrraedd. Mesurwch i ddod o hyd i'r ateb sy'n werth ei wneud, a stopiwch yr eiliad y byddwch yn clirio'r gyllideb yn hytrach na hela cyflymder er ei fwyn ei hun.

## Cwestiynau i'w trafod gyda'ch tîm

1. **A oes gennych gyllideb perfformiad ysgrifenedig ar gyfer eich llwybrau beirniadol, ac a yw wedi'i mynegi fel persentil?** Mae gan lawer o dimau ymdeimlad annelwig y dylai pethau fod yn "gyflym" ond dim rhif y gallai unrhyw un fethu yn ei erbyn, sy'n golygu nad yw perfformiad yn swydd i neb nes iddo dorri. Mae cyllideb fel "p99 o dan 300ms" yn gwneud y targed yn ddiriaethol, yn rhoi rhywbeth i adolygwyr ei orfodi, ac yn troi atchweliad yn ddigwyddiad gweladwy yn hytrach na llithriad araf. Mae'n bwysicaf ar dimau mawr, lle mae oedi'n cropian i mewn drwy lawer o ddwylo a lle nad oes un awdur sengl yn gweld y gost gronnol. Dewch â'ch data oedi presennol a gofynnwch a ydych yn adrodd cyfartaleddau, sy'n eich gwenieithu, neu bersentiliau, sy'n dweud y gwir. Os na allwch ddweud beth mae "digon cyflym" yn ei olygu fel rhif, dyna'r peth cyntaf i'w drwsio.

2. **Pan wnaethoch chi optimeiddio rhywbeth ddiwethaf, wnaeth proffiliwr ddweud wrthych ble i edrych, neu wnaethoch chi ddyfalu?** Mae'n enwog bod y tagfa yn rhywle heblaw lle mae peirianwyr profiadol yn ei ddisgwyl, ac mae amser a dreulir yn diwnio'r cod anghywir yn amser a gollir ddwywaith, unwaith yn y gwaith ac unwaith yn y cymhlethdod a ychwanegwyd. Mae diwylliant sy'n proffilio'n gyntaf yn treulio ei ymdrech lle mae'n talu ar ei ganfed ac yn gadael cod eglur i lonydd. Gofynnwch i'ch tîm gofio'r tri ateb perfformiad diwethaf ac a ddechreuodd pob un o fesuriad neu o deimlad. Ystyriwch a allwch broffilio mewn cynhyrchiad, neu amgylchedd llwyfannu realistig, oherwydd gall proffil liniadur gamarwain yn ddifrifol. Mae'r ateb yn datgelu a yw eich gwaith perfformiad yn beirianneg neu'n chwedloniaeth.

3. **Beth sy'n atal atchweliad perfformiad rhag cyrraedd cynhyrchiad heddiw?** Ar dîm sy'n tyfu, mae'r ateb gonest yn aml yn "gŵyn cwsmer," sy'n golygu mai defnyddwyr yw eich prawf atchweliad. Mae porth CI sy'n methu'r adeiladwaith pan fydd meincnod neu gyllideb yn gwaethygu yn dal y broblem tra ei bod hi'n rhad i'w thrwsio a'r awdur yn dal i gofio'r newid. Trafodwch a yw eich meincnodau'n ddigon sefydlog i borthi arnynt, oherwydd bydd prawf perfformiad ansefydlog sy'n gweiddi blaidd yn cael ei anwybyddu neu ei analluogi. Siaradwch am beth rydych yn ei wylio mewn cynhyrchiad hefyd, gan fod rhai atchweliadau'n ymddangos dim ond o dan draffig a data go iawn. Y nod yw gwneud perfformiad yn briodwedd y mae'r system yn ei hamddiffyn yn awtomatig, nid un rydych yn ei hailddarganfod mewn digwyddiad.

4. **A ydych yn optimeiddio ar gyfer oedi neu drwybwn ar bob llwybr beirniadol, ac a yw unrhyw un wedi ysgrifennu'r dewis hwnnw i lawr?** Mae'r rhain yn nodau gwahanol sy'n tynnu i gyfeiriadau dirgroes: mae bathu a gweithwyr cyfochrog yn codi trwybwn ond gallant ychwanegu oedi at geisiadau unigol, felly mae tîm sy'n optimeiddio yn ôl greddf yn aml yn prynu'r echel anghywir ac yn gwneud i ddefnyddwyr aros i arbed amser peiriant nad oedd unrhyw un yn brin ohono. Ar dîm mawr mae'r perygl yn lluosi, oherwydd mae un grŵp yn diwnio gwasanaeth a rennir ar gyfer trwybwn swmp tra bod un arall yn dibynnu arno ar gyfer oedi rhyngweithiol, ac nid oes yr un ohonynt yn gwybod targed y llall. Dewch â phatrwm defnydd gwirioneddol pob llwybr (cais rhyngweithiol yn erbyn bathiad cefndir), yr oedi persentil presennol, a'r trwybwn cynaliadwy sydd ei angen arnoch, yna penderfynwch yr echel yn benodol yn lle gadael i ddiofyn ymddangos. Ar gyfer system fenter neu lywodraeth o dan SLA, enwch ba fetrig y mae'r cytundeb wedi'i ysgrifennu yn ei erbyn, oherwydd gall optimeiddio'r echel na fesurir dorri contract tra bod eich dangosfyrddau'n edrych yn iach.

5. **Sut ydych chi'n gwybod bod eich meincnodau'n mesur gwaith go iawn yn hytrach na'r optimeiddiwr yn dileu eich prawf?** Mae meincnod sy'n dweud celwydd yn waeth na dim un, oherwydd mae'n rhoi hyder ffug i'r tîm ac yna mae atchweliad yn cael ei lansio beth bynnag. Mae timau'n rheolaidd yn adrodd un rhif lwcus sengl o redeg oer ar fewnbwn tegan, sy'n mesur cychwyn, crynhoi ar-y-pryd, a gallu'r crynhoydd i ddileu cod nas defnyddir yn hytrach na'r ymddygiad y mae defnyddwyr yn ei daro mewn gwirionedd. Dewch â meincnod enghreifftiol a'i groesholi: a yw'n cynhesu, yn rhedeg llawer o ailadroddau, yn adrodd amrywiant, yn defnyddio meintiau a dosraniadau data cynrychioliadol, ac yn trechu dileu cod marw ar ei ganlyniad. Y dynfa gystadleuol yw bod meincnodau gonest yn arafach i'w hysgrifennu a'u rhedeg na microfeincnodau cyflym, felly cytunwch lle mae brasamcanion rhad yn dderbyniol a lle rydych yn mynnu trylwyredd. Mewn cyd-destun cyhoeddus neu reoledig lle bydd cyrff caffael a goruchwylio'n gofyn i chi atgynhyrchu'r rhifau, cofnodwch y ddyfais, y llwyth gwaith, a'r amgylchedd ochr yn ochr â'r canlyniad fel y gellir gwirio'r honiad yn hytrach na'i haeru'n unig.

6. **Pan fydd gwaith perfformiad yn cystadlu â nodweddion am yr un peirianwyr, sut ydych chi'n penderfynu, a phwy sy'n dal yr awdurdod cyllideb?** Mae gan berfformiad enillion sy'n lleihau'n sydyn, felly gallai'r ateb cyntaf a arweinir gan broffil haneru oedi tra bod y degfed yn crafu canran am ddwbl y cymhlethdod cod, a heb reol mae'r llais uchaf neu'r dyddiad cau agosaf yn ennill. Mae'r ystyriaethau cystadleuol yn real: mae dyled perfformiad heb ei thrwsio'n cronni'n dawel ac yn dod yn ddrutach i'w hôl-ffitio, ac eto mae hela cyflymder y tu hwnt i'r gyllideb yn newynu'r map ffordd ac yn ychwanegu cymhlethdod sy'n arafu gwaith yn y dyfodol. Dewch â statws cyllideb presennol pob llwybr beirniadol, cost amcangyfrifedig y status quo mewn peiriannau neu drosi a gollwyd, a'r elw ymylol o'r optimeiddiad nesaf, fel bod y cyfaddawd yn cael ei wneud ar dystiolaeth yn hytrach na phwysau. Ar gyfer rhaglen fenter neu lywodraeth fawr, enwch pwy sy'n berchen ar y gyllideb perfformiad a phwy all awdurdodi gwario amser peirianneg yn ei herbyn, oherwydd mae targed nad oes neb yn atebol am ei amddiffyn yn un sy'n erydu'n dawel.

## Trwy lens sector

**Cwmni newydd.** Mae cyflymder cyflenwi'n curo proses, felly gwrthwynebwch ailysgrifennu a fframweithiau perfformiad mawreddog. Treuliwch un prynhawn gyda phroffiliwr ar y llwybr y mae defnyddwyr yn cwyno amdano mewn gwirionedd, trwsiwch y gost fwyaf (yn aml ymholiad N+1 neu sgan llinol damweiniol), ac ychwanegwch un gyllideb persentil ysgafn i CI fel na all yr ennill atchwelyd yn dawel. Cadwch optimeiddio dwfn ar gyfer y foment y mae rhif go iawn, nid teimlad, yn dweud bod y cod yn rhy araf.

**Busnes bach.** Heb arbenigwr perfformiad a chyllideb dynn, dibynnwch ar y teclynnau rydych eisoes yn talu amdanynt: y proffiliwr yn eich amser rhedeg, persentiliau oedi yn eich dangosfwrdd cynnal, a'r dadansoddwr ymholiad wedi'i adeiladu i mewn yn eich cronfa ddata. Gosodwch un neu ddau gyllideb blaen wedi'u cysylltu â rhywbeth y mae cwsmeriaid yn ei deimlo, megis amser llwytho tudalen neu dalu, a thriniwch doriad fel signal i brynu haen gyflymach neu drwsio'r ymholiad gwaethaf yn hytrach na lansio prosiect diwnio na allwch ei staffio.

**Menter.** Ar raddfa fflyd, mae perfformiad yn gost uniongyrchol, felly llywodraethwch ef fel disgyblaeth a rennir: teclynnau proffilio safonol, cyllidebau persentil wedi'u cysylltu â metrigau busnes, a phyrth atchweliad CI wedi'u cymhwyso'n gyson fel nad yw creep araf un tîm sengl yn chwyddo'r bil cwmwl cyfan. Traciwch oedi, dyraniad, a thrwybwn yn erbyn llinellau sylfaen ar draws gwasanaethau, a chadwch dystiolaeth feincnod y gellir ei hatgynhyrchu, oherwydd mae gostyngiad CPU o 30% ar fflyd fawr yn gynilion sy'n ailddigwydd sy'n werth ei archwilio a'i amddiffyn yn erbyn cosbau SLA.

**Llywodraeth.** Mae perfformiad yn warant mynediad: mae tudalen sy'n llwytho ar hen ffôn dros gysylltiad gwan yn penderfynu a yw dinesydd yn cwblhau hawliad budd-daliadau. Gosodwch gyllidebau penodol yn erbyn dyfeisiau lefel isel realistig a rhwydweithiau wedi'u tagfau'n fwriadol, a chyhoeddwch ganlyniadau meincnod y gellir eu hatgynhyrchu sy'n cofnodi'r ddyfais, y rhwydwaith, a'r llwyth gwaith, fel y gall cyrff caffael a goruchwylio wirio'r rhifau yn hytrach na'u derbyn ar ffydd. Ffafriwch fesuriad tryloyw, archwiliadwy dros haeriadau gwerthwyr, a dalier gwerthwyr i'r un dystiolaeth y gellir ei hatgynhyrchu.

## Enghreifftiau

**Cwmni newydd.** Mae tîm SaaS bach yn sylwi bod eu dangosfwrdd yn teimlo'n ddiog ac yn cael eu temtio i'w ailysgrifennu mewn fframwaith cyflymach. Yn lle hynny maent yn treulio prynhawn gyda phroffiliwr a graff fflam, sy'n dangos bod 70% o amser y cais yn bwynt terfyn sengl yn cyhoeddi un ymholiad cronfa ddata fesul rhes, y patrwm N+1 clasurol. Maent yn ei ddisodli ag un ymholiad wedi'i fathu, mae oedi'n gostwng o 1.2 eiliad i 90 milieiliad, ac maent yn ychwanegu cyllideb p99 o 200ms at feincnod CI ysgafn fel na all yr ateb atchwelyd yn dawel. Dim ailysgrifennu, un prynhawn, ennill degwaith.

**Menter.** Mae llwyfan manwerthu'n rhedeg miloedd o achosion, a chaiff ei fil cwmwl ei ddominyddu gan un gwasanaeth argymell. Mae ymgyrch broffilio'n canfod cyfnewid dyraniad trwm sy'n achosi seibiannau casglu sbwriel aml, ynghyd â storfa-dros-dro â chyfradd taro wael. Mae diwnio strwythurau data ar gyfer lleoliad a thrwsio allweddi'r storfa-dros-dro yn torri CPU fesul cais 40%, sy'n caniatáu i'r tîm redeg yr un traffig ar 40% yn llai o beiriannau. Mae'r cynilion yn talu am yr ymdrech beirianneg mewn wythnosau, ac mae SLA oedi p99 a dorrwyd yn achlysurol nawr yn dal yn gyfforddus, gan osgoi cosbau contractiol.

**Llywodraeth.** Mae'n rhaid i awdurdod treth cenedlaethol wasanaethu dinasyddion ar hen ddyfeisiau a chysylltiadau gwledig araf. Mae'r tîm yn gosod cyllideb benodol: mae'n rhaid i'r dudalen ffeilio ddod yn rhyngweithiol mewn llai na 3 eiliad ar ffôn lefel isel dros broffil 3G wedi'i dagfa. Maent yn proffilio'r dudalen, yn torri'r gwaith sy'n rhwystro rhyngweithio, ac yn cyhoeddi canlyniadau meincnod y gellir eu hatgynhyrchu, gan gofnodi'r ddyfais, y rhwydwaith, a'r llwyth gwaith, fel y gall cyrff goruchwylio ac archwilwyr hygyrchedd wirio'r honiad yn hytrach na'i dderbyn ar ffydd. Nid trosol cost yw perfformiad yma ond gwarant mynediad sy'n cadw'r gwasanaeth yn ddefnyddiadwy i bawb.

## Achos busnes: cymhellion, ROI, a TCO

Mae'r elw ar beirianneg perfformiad yn ymddangos mewn tri llyfr cyfrifon. Y cyntaf yw cost seilwaith: mae cod cyflymach yn gwneud yr un gwaith ar lai o beiriannau, ac ar gyfer fflyd fawr mae gostyngiad CPU o 30% yn gynilion uniongyrchol, sy'n ailddigwydd ac sy'n gwneud i'r ymdrech beirianneg unwaith edrych yn fach. Yr ail yw refeniw a boddhad: mae oedi'n cydberthyn â throsi, gadael, ac ymddiriedaeth defnyddwyr, felly mae crafu'r gynffon yn drosol twf, nid tasg hylendid yn unig. Y trydydd yw risg a osgowyd: mae torri SLA'n cario cosbau, ac mae lansiad sy'n toddi o dan lwyth yn cario niwed i enw da a chost ymladd tân.

Mae cyfanswm cost perchnogaeth yn gymedrol ac wedi'i lwytho'n gynnar. Rydych yn buddsoddi mewn teclynnau proffilio, amgylchedd meincnodi sefydlog, a phyrth CI, ynghyd â'r ddisgyblaeth i ysgrifennu cyllidebau a darllen proffiliau. Y gost fwy, guddiedig yw'r dewis arall: mae dyled perfformiad yn cronni'n dawel, ac mae ôl-ffitio cyflymder i mewn i system araf ar ôl lansio'n llawer drutach na'i diogelu'n barhaus. Gwnewch yr achos i arweinyddiaeth yn eu unedau eu hunain. Trosiwch oedi yn gyfraddau trosi neu gwblhau dinasyddion, trosiwch CPU yn wariant cwmwl misol, a throsiwch borth atchweliad yn ddigwyddiadau a osgowyd. Y ddadl gryfaf yw bod perfformiad yn rhad i'w ddiogelu comit wrth gomit ac yn ddinistriol i'w adfer ar ôl iddo bydru.

## Gwrth-batrymau a pheryglon

- **Optimeiddio heb broffilio.** Diwnio cod nad yw'n dagfa tra bod y gost go iawn yn aros heb ei chyffwrdd.
- **Optimeiddio cynamserol.** Aberthu eglurder am gyflymder dychmygol na fyddai'r proffiliwr byth wedi'i nodi.
- **Adrodd cyfartaleddau.** Cuddio cynffon boenus y tu ôl i gymedr cyfforddus; mae defnyddwyr yn teimlo p99, nid y cyfartaledd.
- **Theatr microfeincnodi.** Rhifau o lwyth gwaith tegan y mae'r optimeiddiwr wedi'i ddileu hanner, heb gynhesu na amrywiant wedi'i adrodd.
- **Storfa-dros-dro heb stori dirymu.** Hela cyfradd taro tra'n gweini data hen neu anghywir.
- **Tybio bod mwy o edafedd yn helpu.** Anwybyddu deddf Amdahl a'r gyfran gyfresol, yna boddi mewn cystadleuaeth.
- **Dim porth atchweliad.** Gadael i ddefnyddwyr fod y prawf perfformiad oherwydd nad oes dim yn CI yn gwarchod y gyllideb.
- **Optimeiddio'r echel anghywir.** Prynu trwybwn gyda bathu pan oedd defnyddwyr angen oedi isel, neu i'r gwrthwyneb.

## Model aeddfedrwydd

- **Lefel 1, Cychwyn:** Dim ond pan fydd rhywbeth yn torri y caiff perfformiad ei drin. Dim cyllidebau, dim arferiad proffilio, dim meincnodau. Mae optimeiddio'n ddyfalu wedi'i yrru gan reddf, a chyfartaleddau yw'r unig fetrig y mae unrhyw un yn ei adrodd.
- **Lefel 2, Datblygu:** Mae rhai timau'n proffilio yn ystod digwyddiadau ac yn cadw ychydig o feincnodau, ond mae'r arfer yn anghyson ac yn dibynnu ar frwdfrydedd unigol. Mae cyllidebau'n bodoli'n anffurfiol ar gyfer llwybr beirniadol neu ddau, ac mae persentiliau'n ymddangos ar rai dangosfyrddau, ond nid oes dim yn porthi atchweliad cyn iddo gael ei lansio ac mae pob tîm yn ailddyfeisio ei ddull ei hun.
- **Lefel 3, Safoni:** Mae gan lwybrau beirniadol gyllidebau persentil ysgrifenedig, a phroffilio yw'r cam cyntaf disgwyliedig, wedi'i ddogfennu cyn i unrhyw un optimeiddio. Mae CI yn cynnwys profion perfformiad gyda phyrth atchweliad, mae rheolau meincnodi gonest (cynhesu, amrywiant, data cynrychioliadol) wedi'u hysgrifennu i lawr a'u gorfodi ar draws y sefydliad, ac mae pob tîm yn dilyn yr un dull yn hytrach na'i un ei hun.
- **Lefel 4, Rheoli:** Mae'r sefydliad yn mesur perfformiad fel priodwedd wedi'i rheoli. Caiff persentiliau oedi, trwybwn, cyfraddau dyraniad, a chyfrifon ymholiad araf eu holrhain yn erbyn llinellau sylfaen penodol mewn cynhyrchiad a CI, caiff atchweliadau eu meintioli yn erbyn trothwyon yn hytrach na'u dadlau, a chysylltir cyllidebau â metrigau busnes megis trosi neu wariant cwmwl fel bod toriad yn ysgogi penderfyniad wedi'i seilio ar ddata. Mae tystiolaeth feincnod y gellir ei hatgynhyrchu ac wedi'i chofnodi gyda'i dyfais, ei llwyth gwaith, a'i hamgylchedd ar gyfer archwiliad.
- **Lefel 5, Cydgysylltu:** Caiff perfformiad ei wella'n barhaus a'i integreiddio ar draws y sefydliad. Mae cyllidebau, proffilio, meincnodi gonest, a dadansoddi graff fflam yn sgiliau arferol, mae pyrth atchweliad yn sefydlog ac yn ymddiriedol, ac mae data cynhyrchiad a CI'n cau'r ddolen yn awtomatig. Mae'r sefydliad yn addasu cyllidebau wrth i draffig, caledwedd, a blaenoriaethau busnes newid, yn ailgydbwyso ymdrech tuag at y llwybrau lle mae'r elw uchaf, ac yn amddiffyn perfformiad fel priodwedd sefydlog yn hytrach nag ymgyrch gyfnodol.

## Syniadau ar gyfer trafodaeth

1. Pa un o'ch llwybrau beirniadol sydd â chyllideb ysgrifenedig, seiliedig ar bersentil heddiw, a pha rai sy'n cael eu diogelu gan obaith yn unig?
2. Pryd wnaeth proffiliwr eich synnu ddiwethaf, a beth ddysgodd hynny i chi am ble rydych chi'n tybio bod amser yn mynd?
3. A yw eich meincnodau'n cynhesu, yn adrodd amrywiant, ac yn defnyddio data cynrychioliadol, neu a ydynt yn mesur yr optimeiddiwr?
4. Ble rydych chi'n gwario peiriannau i orchuddio cod y gallai ymgyrch broffilio ei wneud yn rhatach?
5. Ar gyfer eich llwyth gwaith mwyaf cyfochrog, beth yw'r gyfran gyfresol, ac a yw deddf Amdahl yn capio'r cyflymiad rydych yn ei hela?
6. Pe bai cydweithiwr yn uno newid a ddyblodd oedi p99, pa mor hir cyn i unrhyw un sylwi, a sut y byddent yn dod o hyd i hynny?

## Prif negeseuon

- Mesurwch cyn i chi optimeiddio; anaml y mae'r tagfa lle rydych chi'n dyfalu, ac mae optimeiddio cynamserol yn costio eglurder heb ennill.
- Diffiniwch "digon cyflym" fel cyllideb persentil, oherwydd mae cyfartaleddau'n cuddio'r gynffon lle mae defnyddwyr go iawn yn byw.
- Ffafriwch enillion algorithmig (dosbarth Big O gwell) dros fân-diwnio, a gwybyddwch a oes angen oedi neu drwybwn arnoch.
- Parchwch derfynau cyfochredd (deddf Amdahl) a pheryglon storio-dros-dro (dirymu a data hen).
- Meincnodwch yn onest gyda chynhesu, amrywiant, a llwythi gwaith cynrychioliadol, a drwgdybiwch ficrofeincnodau.
- Porthwch berfformiad mewn CI (pennod 2.4) ac arsylwch arno mewn cynhyrchiad (pennod 9.2); ychwanegwch at y farn lefel system ym mhennod 3.5.
- Mae perfformiad yn gost i fentrau, yn fynediad i lywodraethau, ac yn rhad i'w ddiogelu'n barhaus ond yn ddrud i'w ôl-ffitio.

## Cyfeiriadau a darllen pellach

- Brendan Gregg, *Systems Performance: Enterprise and the Cloud* (profiling, flame graphs, and method).
- Brendan Gregg, *BPF Performance Tools* (practical observability and profiling on Linux).
- Donald E. Knuth, "Structured Programming with go to Statements" (*ACM Computing Surveys*, 1974): the source of the premature-optimization maxim.
- Donald E. Knuth, *The Art of Computer Programming* (algorithmic analysis and complexity).
- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein, *Introduction to Algorithms* (Big O and algorithmic efficiency).
- Gene M. Amdahl, "Validity of the Single Processor Approach to Achieving Large-Scale Computing Capabilities" (1967): the origin of Amdahl's law.
- Ulrich Drepper, "What Every Programmer Should Know About Memory" (the memory hierarchy and data locality).
- Martin Kleppmann, *Designing Data-Intensive Applications* (latency, throughput, and tail behavior in systems).
- Aleksey Shipilev, "JMH and the pitfalls of microbenchmarking" (honest benchmarking practice on managed runtimes).
- Ilya Grigorik, *High Performance Browser Networking* (client-side and network performance for low-bandwidth users).
