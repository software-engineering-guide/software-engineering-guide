# 6.6 Seilwaith a gweithrediadau AI

## Trosolwg a chymhelliant

Seilwaith a gweithrediadau AI yw'r ddisgyblaeth o ddarparu, amserlennu, a rhedeg y systemau cyfrifiadura, storio, a gwasanaethu arbenigol y mae llwythi gwaith AI yn eu mynnu, gan wneud hynny'n gost-effeithiol, yn ddibynadwy, ac yn arsylladwy. Mae AI modern yn ddrud i'w redeg. Mae hyfforddi a gwasanaethu modelau mawr yn mynnu cyflymyddion prin ([GPUau](https://en.wikipedia.org/wiki/Graphics_processing_unit) a [TPUau](https://en.wikipedia.org/wiki/Tensor_Processing_Unit)), rhwydweithio band-lled uchel, storio fector graddfa-fawr ar gyfer adalw (mynegeio data fel fectorau rhifiadol fel y gellir dod o hyd i eitemau tebyg yn gyflym), a haenau gwasanaethu wedi'u tiwnio ar gyfer oedi a thrwygyrch. Mae cael y seilwaith hwn yn iawn yn wahaniaeth rhwng AI sy'n graddio'n gynaliadwy ac AI sy'n bwyta cyllideb yn dawel tra'n tanberfformio.

I dimau mawr, y problemau craidd yw graddfa, prinder, a chost. Mae cyflymyddion yn gyfyngedig a drud, felly mae amserlennu a defnydd yn bwysig dros ben. Mae GPUau segur yn arian wedi'i losgi, ac mae differiad wedi'i swp-brosesu'n wael yn lluosi cost fesul cais. Mae angen [cronfeydd data fector](https://en.wikipedia.org/wiki/Vector_database) sy'n aros yn gyflym wrth iddynt dyfu ar gymwysiadau trwm-eu-hadalw. Mae angen fersiynu anogiadau, piblinellau gwerthuso, ac arsylladwyedd (a elwir weithiau'n LLMOps) ar gymwysiadau AI cynhyrchiadol i weithredu'n ddiogel a gwella dros amser. Heb seilwaith a rennir a disgyblaeth weithredol, mae pob tîm yn ymladd yr un brwydrau a chostau'n chwyrlio.

Mae llywodraeth a sefydliadau rheoledig yn ychwanegu gofynion o gwmpas sofraniaeth ddata, diogelwch, a gwariant rhagfynegadwy. Efallai y bydd angen iddynt ddefnyddio ar-safle neu gwmwl-sofran fel na fydd data sensitif a modelau byth yn gadael ffiniau rheoledig. Rhaid iddynt ragamcanu a chyfiawnhau gwariant seilwaith, a bodloni safonau diogelwch ac argaeledd. Mae penderfyniadau seilwaith AI yn y lleoliadau hyn yn cario canlyniadau aml-flwyddyn, felly gwnewch nhw gan gadw caffael, diogelwch, a gadael mewn cof.

## Egwyddorion allweddol

- Triniwch gyfrifiadura cyflymyddion fel adnodd prin, drud i'w amserlennu a'i ddefnyddio, nid ei bentyrru.
- Optimeiddiwch gost fesul uned ddefnyddiol o waith, nid capasiti crai.
- Maintiwch fodelau a chaledwedd yn briodol i'r dasg; anaml y bydd y dewis mwyaf yn y mwyaf cost-effeithiol.
- Dyluniwch wasanaethu ar gyfer oedi a thrwygyrch gyda swp-brosesu a chadw storfa gudd fel technegau dosbarth-cyntaf.
- Gwnewch systemau AI yn arsylladwy: olrheiniwch gost, oedi, ansawdd, a gwallau'n barhaus.
- Fersiynwch a gwerthuswch anogiadau a modelau â'r un trylwyredd â chod.
- Cynlluniwch ar gyfer cludadwyedd ac osgowch glymu mewn dewisiadau seilwaith a gwasanaethu.

## Argymhellion

### Cynllunio a rheoli cyfrifiadura cyflymyddion

Rhagamcanwch alw ar gyfer hyfforddi a differiad ar wahân, gan fod ganddynt siapiau gwahanol. Mae hyfforddi'n bwrslyd ac yn amserlenadwy; mae differiad yn barhaus ac yn sensitif i oedi. Defnyddiwch amserlennwyr a chwotâu i rannu GPUau a TPUau prin ar draws timau, blaenoriaethu llwythi gwaith, a gyrru defnydd i fyny. Mesurwch ddefnydd a thriniwch segurdod cronig fel problem i'w thrwsio. Cymysgwch gapasiti a gadwyd ar gyfer llwyth sylfaenol â chapasiti ar-alw neu sbot ar gyfer byrstiau i reoli cost. Ystyriwch a fyddai cyflymyddion rhatach neu lai, neu ddifferiad CPU ar gyfer modelau ysgafn, yn ddigon. Dewiswch rhwng cwmwl, ar-safle, a hybrid yn seiliedig ar gost ar eich graddfa, anghenion sofraniaeth ddata, a phatrymau byrstio, a chadwch lwybr gadael.

### Adeiladu seilwaith adalw: mewnblaniadau a chronfeydd data fector

Ar gyfer cymwysiadau adalw-estynedig, sefydlwch seilwaith i gynhyrchu [mewnblaniadau](https://en.wikipedia.org/wiki/Word_embedding) (cynrychioliadau fector rhifiadol sy'n gosod eitemau tebyg yn agos at ei gilydd) a'u storio mewn cronfa ddata fector sy'n cefnogi [chwilio cymydog-agosaf brasamcanol](https://en.wikipedia.org/wiki/Nearest_neighbor_search) cyflym (dod o hyd i'r fectorau mwyaf tebyg heb gymharu pob un yn helaeth) ar eich graddfa. Cynlluniwch ar gyfer tri pheth: cost ac oedi cynhyrchu mewnblaniadau, ffresni'r mynegai wrth i ddogfennau newid, a baich gweithredol cadw mynegeion yn gyson. Gwerthuswch a yw cronfa ddata fector bwrpasol, estyniad fector-alluog o gronfa ddata bresennol, neu wasanaeth a reolir yn gweddu orau i'ch graddfa a'ch goddefgarwch clymu. Monitrwch oedi a chofio adalw, oherwydd bod ansawdd adalw'n penderfynu ansawdd cymhwysiad yn uniongyrchol.

### Optimeiddio gwasanaethu model: swp-brosesu, storfa gudd, ac oedi

Gwasanaethu yw lle penderfynir cost differiad a phrofiad defnyddiwr. Defnyddiwch **swp-brosesu** i brosesu sawl cais gyda'i gilydd a chodi trwygyrch cyflymydd, gan gydbwyso maint swp yn erbyn oedi. Defnyddiwch **storfa gudd** yn ymosodol: cadwch geisiadau union yr un fath neu debyg yn semantig, cadwch fewnblaniadau, a manteisiwch ar storio gudd anogiad neu ragddodiad lle mae'r platfform yn ei gefnogi i osgoi ailgyfrifo cyd-destun a rennir. Gosodwch dargedau oedi clir, a mesurwch oedi cynffon, nid dim ond cyfartaleddau. Llwybrwch geisiadau at fodelau â'r maint priodol: model bach ar gyfer achosion hawdd, un mwy dim ond pan fo angen. Hunanraddiwch wasanaethu yn ôl galw, a phrofwch lwyth cyn lansio fel eich bod yn gwybod eich capasiti a'ch cromlin gost.

### Ymarfer LLMOps: fersiynu anogiadau, piblinellau gwerthuso, ac arsylladwyedd

Triniwch anogiadau fel arteffactau wedi'u fersiynu mewn rheolaeth ffynhonnell, gydag adolygiad a'r gallu i wrthdroi. Adeiladwch biblinellau gwerthuso sy'n rhedeg cyfresi prawf all-lein yn awtomatig pryd bynnag y bydd anogiadau neu fodelau'n newid, fel eich bod yn dal atchweliadau cyn rhyddhau. Offerynwch gynhyrchiad yn gynhwysfawr: cofnodwch fewnbynnau, allbynnau, oedi, defnydd tocynnau, cost, a gwallau, gyda samplu a diogelwyr preifatrwydd. Olrheiniwch signalau ansawdd ac adborth defnyddwyr ar-lein. Mae'r arsylladwyedd hwn yn eich galluogi i ddal dirywiad, rheoli cost, dad-fygio methiannau, a gwella systemau'n ddiogel: asgwrn cefn gweithredol AI cynhyrchiadol mewn cynhyrchiad.

### Rheoli cost yn ddiflino ac yn arsylladwy

Priodolwch wariant AI i dimau ac achosion defnydd fel bod cost yn weladwy ac yn eiddo i rywun. Gosodwch gyllidebau a rhybuddion, monitrwch gost fesul cais a fesul canlyniad, ac adolygwch y gyrwyr cost mwyaf yn rheolaidd. Tynnwch y trosolion sydd gennych: maintio modelau'n briodol, storfa gudd, swp-brosesu, tocio anogiad a chyd-destun, a dewis y defnydd rhataf sy'n bodloni gofynion. Gall costau AI raddio â defnydd mewn ffyrdd annisgwyl, felly mae arsylladwyedd cost parhaus yn hanfodol i osgoi synnau annymunol.

## Cymhareb: manteision ac anfanteision

| Penderfyniad | Opsiwn A | Opsiwn B | Cyfaddawd |
|---|---|---|---|
| Lleoliad cyfrifiadura | Cwmwl | Ar-safle | Hyblygrwydd a chost isel ymlaen llaw yn erbyn rheolaeth, sofraniaeth, ac economeg cyflwr-sefydlog |
| Capasiti | Wedi'i gadw | Ar-alw/sbot | Cost ragfynegadwy yn erbyn hyblygrwydd a risg tarfu |
| Maint swp | Swpiau mawr | Swpiau bach | Trwygyrch a chost yn erbyn oedi |
| Maint model | Model mawr | Model bach | Ansawdd yn erbyn cost a chyflymder |
| Storfa fector | Cronfa ddata bwrpasol | Estyniad cronfa ddata bresennol | Perfformiad ar raddfa yn erbyn symlrwydd a llai o systemau |
| Storfa gudd | Ymosodol | Lleiaf posibl | Cost ac oedi is yn erbyn ffresni a chymhlethdod |

Y cyfaddawd amlycaf yw cost yn erbyn oedi ac ansawdd. Mae swp-brosesu, storfa gudd, a modelau llai'n torri cost ond gallant ychwanegu oedi neu leihau ansawdd. Mae'r cydbwysedd cywir yn dibynnu ar oddefgarwch eich cymhwysiad. Mae ar-safle yn erbyn cwmwl yn cyfnewid rheolaeth ac economeg cyflwr-sefydlog yn erbyn hyblygrwydd ac ymrwymiad isel, penderfyniad a lunnir yn drwm gan anghenion sofraniaeth ddata a graddfa.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Beth yw ein cost fesul canlyniad defnyddiol heddiw, a pha drosol fyddai'n ei symud fwyaf?** Mae capasiti crai a chyfartaleddau fesul-cais yn cuddio'r rhif sy'n bwysig: beth mae'n ei gostio i ddanfon un uned wirioneddol o werth, a sut mae hynny'n graddio â defnydd. I dîm mawr, mae'r bwlch rhwng defnydd wedi'i optimeiddio ac un heb ei optimeiddio yn aml sawl gwaith yn fwy o ran gwariant, felly mae'r cwestiwn hwn yn troi pryder amwys am y bil yn rhestr raddedig o drwsiadau. Dewch â phriodoliad cost cyfredol fesul tîm ac achos defnydd, tueddiadau fesul-cais a fesul-canlyniad, a'r gyrwyr cost mwyaf. Trafodwch y trosolion yn nhrefn eu had-daliad: maintio modelau'n briodol, storfa gudd (gan gynnwys storfa gudd ragddodiad a semantig), swp-brosesu, a thocio anogiad neu gyd-destun. Mewn llywodraeth, ychwanegwch y pwysau i ragamcanu a chyfiawnhau gwariant aml-flwyddyn. Dylai'r ateb ddyrannu perchennog a throsol i bob prif yrrwr cost, nid codi ysgwyddau.

2. **Pe bai ein darparwr differiad presennol yn dyblu ei bris neu'n mynd i lawr yfory, pa mor gyflym y gallem newid?** Mae clymu tawel yn hawdd ei adeiladu ac yn boenus i ddianc rhagddo, a stacau gwasanaethu yw'r lle mae'n cuddio ddyfnaf. I fentrau ac yn enwedig llywodraeth, mae cludadwyedd yn ofyniad caffael a pharhad, nid moethusrwydd. Dewch â'ch pensaernïaeth: a yw modelau'n eistedd y tu ôl i ryngwyneb mewnol, a yw anogiadau a chyfresi gwerthuso'n gludadwy, a faint o ymddygiad gwasanaethu penodol-i-ddarparwr rydych yn dibynnu arno. Y signal i'w wylio yw a yw unrhyw un erioed wedi rhedeg eich cyfres werthuso yn erbyn ail ddarparwr neu ail darged defnyddio. Os byddai newid yn cymryd misoedd ac ailysgrifennu llwybrau craidd, triniwch hynny fel diffyg dylunio i'w drin nawr, gan y gallai opsiynau sofran ac ar-safle ddod yn orfodol heb fawr o rybudd.

3. **Beth yw ein defnydd cyflymyddion ar hyn o bryd, a faint mae GPUau segur a differiad heb ei swp-brosesu'n ei losgi?** Mae cyflymyddion yn brin a drud, felly mae segurdod cronig a gwasanaethu fesul-cais yn draenio cyllidebau'n dawel a allai ariannu mwy o allu. I sefydliad mawr sy'n rhannu GPUau ar draws timau, mae'r cwestiwn hwn yn datgelu a yw amserlennu, cwotâu, a blaenoriaethau mewn gwirionedd yn cadw defnydd yn uchel neu a yw caledwedd wedi'i bentyrru, heb ei ddefnyddio'n ddigonol, yn norm. Dewch â rhifau defnydd go iawn, eich ystum swp-brosesu a storfa gudd, a'ch mesuriadau oedi-cynffon, nid dim ond cyfartaleddau, gan fod defnyddwyr yn teimlo'r gynffon araf. Trafodwch a ragamcanir galw hyfforddi a differiad ar wahân, o gofio eu siapiau gwahanol, ac a fyddai model llai neu ddifferiad CPU'n ddigon ar gyfer achosion ysgafn. Dylai'r ateb bwyntio at gapasiti segur penodol i'w adfeddiannu a cheisiadau penodol i'w swp-brosesu neu eu llwybro at fodel â'r maint priodol.

4. **Pan fydd newid anogiad neu fodel yn cael ei ddanfon, beth sy'n atal atchweliad ansawdd neu gost tawel rhag cyrraedd defnyddwyr?** Gall stac gwasanaethu edrych yn iach o ran oedi ac amser i fyny tra bo'r atebion mae'n eu dychwelyd yn gwaethygu'n dawel neu anogiad newydd yn dyblu defnydd tocynnau fesul cais. I dîm mawr lle mae llawer o grwpiau'n golygu anogiadau ac yn cyfnewid modelau'n annibynnol, mae newid heb ei giatio'n ddigwyddiad cynhyrchiad yn aros i ddigwydd, ac mae radiws y ffrwydrad yn tyfu gyda phob tîm ar y platfform a rennir. Dewch â'ch gorchudd gwerthuso: pa anogiadau a modelau sydd â chyfresi prawf all-lein, a yw'r cyfresi hynny'n rhedeg yn awtomatig ar bob newid, pa drothwyon ansawdd a chost sy'n giatio rhyddhad, a pha mor gyflym y gallwch wrthdroi. Trafodwch a yw anogiadau'n byw mewn rheolaeth ffynhonnell gydag adolygiad, ynteu a all rhywun o hyd olygu anogiad system byw â llaw. Mewn lleoliadau menter a llywodraeth, cysylltwch bob newid â llwybr archwilio a chymeradwywr a enwir, oherwydd bod angen ateb wedi'i gofnodi, nid ei gofio, ar reoleiddiwr sy'n gofyn "pwy newidiodd hyn a beth wnaethoch chi ei brofi."

5. **Sut ydym yn penderfynu rhwng defnydd cwmwl, ar-safle, a sofran, ac a ydym wedi prisio economeg cyflwr-sefydlog go iawn yn hytrach na'r peilot?** Mae'r dewis lleoliad-cyfrifiadura'n gosod eich cromlin gost, eich ystum sofraniaeth ddata, a'ch opsiynau gadael am flynyddoedd, ac eto fe'i gwneir yn aml ar fil cwmwl peilot nad yw'n edrych fel dim byd tebyg i gynhyrchiad ar raddfa. I sefydliad mawr, mae capasiti cwmwl elastig yn rhad i ddechrau ac fe all ddod yn linell sengl fwyaf unwaith y bydd differiad yn rhedeg yn barhaus, tra bo ar-safle'n cyfnewid ymrwymiad isel am reolaeth ac economeg cyflwr-sefydlog. Dewch â chyfeintiau hyfforddi a differiad wedi'u rhagamcanu, y pwynt hafal-cost lle mae caledwedd a gadwyd neu berchnogol yn curo ar-alw, eich cyfyngiadau preswyliad diogelwch data, a'r patrymau byrstio sy'n dadlau dros hybrid. Mewn lleoliadau llywodraeth a rheoledig, pwyswch ofynion cwmwl-sofran neu ar-safle a allai ddod yn orfodol heb fawr o rybudd, a chadarnhewch fod y bensaernïaeth yn cadw modelau y tu ôl i ryngwyneb mewnol fel na fydd symudiad gorfodol yn ailysgrifennu llwybrau craidd.

6. **A ydym mewn gwirionedd yn berchen ar ein gwariant AI, a all pob tîm weld a bod yn atebol am y gost y mae'n ei yrru?** Mae cost AI'n graddio â defnydd mewn ffyrdd sy'n synnu pobl, a heb briodoliad mae'r bil yn glanio fel un rhif afloyw nad yw'r un tîm yn teimlo'n gyfrifol am ei leihau. Mewn sefydliad mawr, mae cost nad oes neb yn berchen arni'n gost nad oes neb yn ei optimeiddio, felly'r cwestiwn yw a yw gwariant wedi'i dagio i dimau ac achosion defnydd gyda chyllidebau, rhybuddion, a thueddiadau fesul-canlyniad, ynteu a gaiff ei ddarganfod dim ond pan fydd cyllid yn ei uwchgyfeirio. Dewch â'ch model priodoli cost, y gyrwyr mwyaf fesul tîm, a'r trosolion y mae pob perchennog yn eu rheoli: maintio'n briodol, storfa gudd, swp-brosesu, a thocio cyd-destun. Ar gyfer cyllidebau menter a llywodraeth, ychwanegwch y ddisgyblaeth o ragamcanu a chyfiawnhau gwariant seilwaith aml-flwyddyn, gan y bydd corff cyhoeddus na all esbonio ei fil cyfrifiadura linell wrth linell yn ei chael yn anodd ei amddiffyn mewn adolygiad.

## Lens sector

**Cwmni newydd.** Peidiwch â bod yn berchen ar unrhyw seilwaith y gallwch ei osgoi. Galwch API differiad wedi'i letya, llwybrwch geisiadau hawdd at fodel bach rhad a chadwch un mwy ar gyfer achosion anodd, a chadwch storfa gudd yn ymosodol fel nad yw anogiadau a ailadroddir yn costio dim. Defnyddiwch gronfa ddata fector a reolir yn hytrach na gweithredu'ch un eich hun, cadwch anogiadau mewn git gyda sgript werthuso fer cyn pob newid, a chofnodwch gost fesul cais fel bod bil rhemp yn ymddangos cyn iddo frifo. Eich adnodd prinnaf yw sylw peirianyddol, felly prynwch weithredadwyedd a chadwch newid yn rhad.

**Busnes bach.** Heb dîm platfform, triniwch wasanaethu, adalw, ac arsylladwyedd fel pethau rydych yn eu prynu y tu mewn i offer rydych eisoes yn eu defnyddio, nid systemau rydych yn eu staffio. Ffafriwch ddifferiad a reolir a chwilio fector a reolir gyda phrisio tryloyw, rhagfynegadwy, a gosodwch gap gwariant caled a rhybudd bilio o'r dydd cyntaf. Fframiwch y penderfyniad fel prynu-yn-erbyn-adeiladu'n onest: anaml y mae gweithredu GPUau neu fynegai fector yn talu ar eich cyfaint, ac mae model bach y tu ôl i API wedi'i letya fel arfer yn bodloni'r angen am ffracsiwn o'r ymdrech.

**Menter.** Y broblem yw platfform ffordd-balmantog a rennir ar draws llawer o dimau: cyflymyddion cyfun gydag amserlennwyr, cwotâu, a blaenoriaethau i yrru defnydd i fyny, swp-brosesu a storfa gudd safonol, llwybrwyr maintio priodol, a chost wedi'i phriodoli i bob tîm ac achos defnydd. Giatiwch newidiadau anogiad a model â chyfresi gwerthuso awtomataidd, safonwch yr haen ryngwyneb fel bod darparwyr a thargedau defnyddio'n aros y gellir eu cyfnewid, a rheolwch gost fesul canlyniad fel metrig dosbarth-cyntaf yn hytrach na phob grŵp yn ailddyfeisio seilwaith drud, heb ei ddefnyddio'n ddigonol.

**Llywodraeth.** Mae sofraniaeth ddata, diogelwch, a gwariant rhagfynegadwy'n llunio pob dewis. Ffafriwch ddefnydd ar-safle neu gwmwl-sofran fel bod data sensitif a modelau'n aros y tu mewn i ffiniau rheoledig, amserlennwch GPUau prin ar draws adrannau gyda chwotâu y gallwch eu cyfiawnhau mewn caffael, a rhagamcanwch gapasiti i amddiffyn gwariant aml-flwyddyn linell wrth linell. Fersiynwch a gwerthuswch anogiadau a modelau â llwybr archwilio wedi'i gofnodi, cadwch arsylladwyedd cynhwysfawr dros gost ac ansawdd, a chadwch fodelau y tu ôl i ryngwyneb mewnol fel na fydd symudiad gorfodol i ddarparwr newydd neu blatfform sofran yn eich gadael yn sownd.

## Enghreifftiau

**Cwmni newydd.** Cadwodd cwmni newydd bach sy'n rhedeg nodwedd ysgrifennu AI ei fil yn synhwyrol heb fod yn berchen ar unrhyw GPUau. Galwodd API differiad wedi'i letya, llwybrodd geisiadau hawdd at fodel bach rhatach a chadw'r un mwy ar gyfer achosion anodd, a chadwodd atebion i anogiadau a ailadroddwyd mewn storfa gudd. Storiodd ei anogiadau mewn git gyda sgript werthuso fer a redodd cyn pob newid, defnyddiodd gronfa ddata fector a reolir ar gyfer adalw fel na fu'n rhaid iddo weithredu un ei hun, a chofnododd gost fesul cais fel y gallai'r sylfaenwyr weld gwariant yn dringo cyn iddo ddod yn syndod.

**Menter.** Torrodd cwmni cyfryngau sy'n rhedeg nodwedd LLM traffig-uchel gostau differiad yn sylweddol. Llwybrodd geisiadau hawdd at fodel bach a chadw model mwy ar gyfer rhai anodd. Cadwodd atebion i ymholiadau a ailadroddwyd mewn storfa gudd a galluogodd storio gudd rhagddodiad ar gyfer ei anogiad system a rennir. Rhedodd GPUau drwy amserlennwr a rennir i gadw defnydd yn uchel, fersiynodd bob anogiad mewn git gyda chyfres werthuso awtomataidd yn giatio newidiadau, ac offerynnodd gost fesul cais fel bod pob tîm cynnyrch yn berchen ar ei wariant ei hun.

**Llywodraeth.** Defnyddiodd asiantaeth genedlaethol â rheolau sofraniaeth ddata llym ei systemau AI ar-safle fel na fyddai data sensitif a modelau byth yn gadael ei hamgylchedd rheoledig. Amserlennodd GPUau prin ar draws adrannau gyda chwotâu a blaenoriaethau, rhagamcanodd gapasiti i gyfiawnhau caffael aml-flwyddyn, ac adeiladodd blatfform chwilio-fector ar gyfer adalw dros ddogfennau swyddogol. Fersiynwyd a gwerthuswyd anogiadau a modelau cyn rhyddhau. Olrheiniodd arsylladwyedd cynhwysfawr gost ac ansawdd, a chadwodd y bensaernïaeth fodelau y tu ôl i ryngwyneb mewnol i gadw llwybr gadael ac osgoi clymu.

## Achos busnes: cymhellion, ROI, a TCO

Mae'r cymhelliant dros seilwaith AI disgybledig yn syml. Mae AI ar raddfa'n gostus, ac mae'r bwlch rhwng defnydd wedi'i optimeiddio ac un heb ei optimeiddio yn aml sawl gwaith yn fwy o ran gwariant. Daw ROI o ddefnydd cyflymydd uwch, cost is fesul cais drwy swp-brosesu a storfa gudd, modelau â'r maint priodol, ac osgoi gor-ddarparu. Mae piblinellau arsylladwyedd a gwerthuso'n talu ar eu canfed drwy atal digwyddiadau costus a galluogi ailadrodd diogel.

Mae TCO'n rhychwantu cyfrifiadura cyflymyddion (y llinell fwyaf i lawer o lwythi gwaith), storio fector, seilwaith gwasanaethu, rhwydweithio, a'r staff platfform a gweithrediadau i'w redeg. Pwyswch hyn yn erbyn cost peidio â buddsoddi: biliau differiad rhemp, oedi gwael sy'n tanseilio mabwysiadu, ac anallu i raddio. I lywodraeth, ychwanegwch gost methu â bodloni gofynion sofraniaeth neu ddiogelwch. Gwnewch yr achos i arweinyddiaeth drwy ddangos tueddiadau cost-fesul-canlyniad a phlatfform ffordd-balmantog sy'n galluogi llawer o dimau i ddefnyddio AI yn effeithlon, yn hytrach na phob un yn adeiladu seilwaith drud, heb ei ddefnyddio'n ddigonol.

## Gwrth-batrymau a pheryglon

- **Cyflymyddion segur.** Neilltuo GPUau prin i dimau sy'n eu gadael heb eu defnyddio'n ddigonol.
- **Dim swp-brosesu na storfa gudd.** Gwasanaethu pob cais yn unigol ac ailgyfrifo cyd-destun a rennir.
- **Y model mwyaf yn ddiofyn.** Defnyddio model drud lle byddai un bach yn gwneud y tro.
- **Dallineb cost.** Dim priodoliad, cyllidebau, na gwelededd cost fesul-cais hyd nes i'r bil gyrraedd.
- **Anogiadau heb eu fersiynu.** Newid anogiadau mewn cynhyrchiad heb fersiynu na giât werthuso.
- **Esgeuluso oedi-cynffon.** Optimeiddio oedi cyfartalog tra bo defnyddwyr yn dioddef cynffonnau araf.
- **Clymu tawel.** Adeiladu'n ddwfn ar stac gwasanaethu un darparwr heb gludadwyedd.

## Model aeddfedrwydd

1. **Cychwyn.** Dyraniad GPU ad hoc yn ymateb i bwy bynnag sy'n gofyn uchaf, dim swp-brosesu na storfa gudd, dim gwelededd cost hyd nes i'r bil gyrraedd, anogiadau'n cael eu golygu'n fyw heb eu fersiynu, monitro lleiafswm.
2. **Datblygu.** Mae rhai timau'n mabwysiadu amserlennu a rennir, storfa gudd, ac anogiadau dan reolaeth fersiwn, ond mae'r arfer yn anghyson ar draws y sefydliad: mae un grŵp yn swp-brosesu ac yn gwerthuso tra bo un arall yn dal i wasanaethu pob cais yn unigol ac yn newid anogiadau â llaw.
3. **Safoni.** Gorfodir platfform ffordd-balmantog, wedi'i ddogfennu ar draws y sefydliad: amserlennu a rennir gyda chwotâu a blaenoriaethau, swp-brosesu safonol, storfa gudd, a maintio priodol, seilwaith fector ar gyfer adalw, piblinellau gwerthuso awtomataidd sy'n giatio pob newid anogiad neu fodel, a phriodoliad cost i dimau ac achosion defnydd.
4. **Rheoli.** Mesurir a rheolir y platfform yn erbyn llinellau sylfaen: olrheinir defnydd cyflymydd, cost fesul canlyniad defnyddiol, oedi cynffon, cofio adalw, ac atchweliadau ansawdd fesul-newid gyda rhybuddion a throthwyon, mae cost yn eiddo i bob tîm, a phenderfynir mynd-neu-beidio ar newid yn seiliedig ar dystiolaeth yn hytrach na greddf.
5. **Cerddorfa.** Mae seilwaith yn gwella ac yn addasu'n barhaus: mae llwybro, swp-brosesu, a graddio'n eu tiwnio'u hunain i signalau cost ac ansawdd byw, ailgydbwyswir capasiti ar draws timau a rhwng targedau cwmwl, ar-safle, a sofran wrth i alw a chyfyngiadau newid, ymarferir cludadwyedd, ac integreiddir cynllunio seilwaith â chynnyrch, diogelwch, a chaffael.

## Syniadau ar gyfer trafodaeth

- Sut ydych chi'n gyrru defnydd cyflymydd i fyny heb newynu llwythi gwaith blaenoriaeth?
- Ble mae'r cydbwysedd swp-brosesu a storfa gudd cywir ar gyfer eich gofynion oedi?
- Pryd mae defnydd ar-safle neu sofran yn cyfiawnhau ei gost dros gwmwl?
- Sut ydych chi'n priodoli ac yn rheoli gwariant AI ar draws llawer o dimau?
- Beth ddylai giatio newid anogiad neu fodel rhag cyrraedd cynhyrchiad?
- Sut ydych chi'n cadw seilwaith gwasanaethu'n ddigon cludadwy i newid darparwyr?

## Casgliadau allweddol

- Mae cyflymyddion yn brin a drud; amserlennwch, rhannwch, a'u defnyddio'n fwriadol.
- Swp-brosesu, storfa gudd, a maintio model priodol yw'r prif drosolion ar gyfer cost ac oedi.
- Mae angen seilwaith mewnblaniadau a chwilio fector wedi'i weithredu'n dda ar gymwysiadau adalw.
- LLMOps (fersiynu anogiadau, piblinellau gwerthuso, ac arsylladwyedd) yw asgwrn cefn gweithredol AI cynhyrchiadol.
- Rheolwch gost yn arsylladwy a chadwch gludadwyedd i osgoi clymu.

## Cyfeiriadau a darllen pellach

- Chip Huyen, *Designing Machine Learning Systems*.
- Google, *Site Reliability Engineering* (Beyer, Jones, Petoff, Murphy, goln.).
- Jared Kaplan et al., *Scaling Laws for Neural Language Models*.
- Reza Yazdani Aminabadi et al., *DeepSpeed Inference: Enabling Efficient Inference of Transformer Models at Unprecedented Scale*.
- Woosuk Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention* (vLLM).
- Andriy Burkov, *Machine Learning Engineering*.
