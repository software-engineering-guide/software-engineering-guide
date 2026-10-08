# 8.2 Seilwaith fel cod a ffurfweddiad

## Trosolwg a chymhelliant

Ystyr [seilwaith fel cod](https://en.wikipedia.org/wiki/Infrastructure_as_code) (IaC) yw diffinio a darparu seilwaith (rhwydweithiau, gweinyddion, cronfeydd data, cydbwyswyr llwyth, caniatâd) trwy ffeiliau diffiniad y gellir eu darllen gan beiriant yn hytrach na chliciau consol â llaw neu sgriptiau ad hoc. Mae [rheolaeth ffurfweddiad](https://en.wikipedia.org/wiki/Configuration_management) yn ymestyn yr un syniad i osodiadau a chyflwr systemau unwaith y byddant yn bodoli. Gyda'i gilydd maent yn troi seilwaith o arteffact bregus, wedi'i lunio â llaw yn gynnyrch wedi'i reoli gan fersiynau, adolygadwy, atgynyrchiadwy o'r un ddisgyblaeth beirianneg a ddefnyddiwch ar gyfer cod cymwysiadau.

I dimau mawr, nid cyfleustra yw IaC ond angenrheidrwydd. Pan fydd angen amgylcheddau ar gannoedd o beirianwyr a bod yn rhaid i filoedd o adnoddau aros yn gyson ar draws rhanbarthau a chyfrifon, ni all darparu â llaw gadw i fyny ac ni all aros yn gywir. Mae seilwaith wedi'i ffurfweddu gan bobl yn drifftio, yn hwyr neu'n hwyrach, i mewn i weinyddion "pluen eira" unigryw nad oes neb yn eu deall yn llawn ac na ellir eu hailadeiladu'n ddibynadwy ar ôl methiant. Mae codeiddio seilwaith yn ei wneud yn gyson, yn archwiliadwy, ac yn waredadwy. Gellir ailgreu unrhyw amgylchedd o'i ddiffiniad, ac mae unrhyw newid yn wahaniaeth adolygadwy.

Mae sefydliadau menter a llywodraeth yn ennill un fantais bendant arall: llywodraethu gorfodadwy. Gellir mewnblannu gofynion diogelwch a chydymffurfiaeth, fel amgryptio yn ei orffwysfa, segmentu rhwydwaith, rhanbarthau cymeradwy, a thagio ar gyfer dyraniad cost, yn uniongyrchol i mewn i'r cod a'u gwirio'n awtomatig cyn i unrhyw beth gael ei ddarparu. Yn lle archwilio seilwaith wedi'r digwyddiad a hela toriadau, rydych yn cadw seilwaith anghydymffurfiol rhag bodoli erioed. Mae'r symudiad hwn o ganfod i atal yw'r prif reswm y mae IaC wedi dod yn sylfaenol i arfer platfform modern.

## Egwyddorion allweddol

- Ffafriwch ddiffiniadau datganiadol sy'n disgrifio cyflwr dymunol dros sgriptiau gorchmynnol sy'n disgrifio camau.
- Cadwch bob diffiniad seilwaith mewn rheolaeth fersiynau, wedi'i adolygu fel unrhyw god arall.
- Triniwch seilwaith fel anhydraidd: disodli yn hytrach na newid yn ei le.
- Gwnewch ddarparu'n idempotent fel bod cymhwyso'r un diffiniad dro ar ôl tro'n cynhyrchu'r un canlyniad.
- Canfyddwch a chysonwch ddrifft, yr amgylchedd byw'n gwyro oddi wrth ei ddiffiniad datganedig, yn barhaus; y cod, nid y system fyw, yw'r ffynhonnell wirionedd.
- Cyfansoddwch seilwaith o fodylau ailddefnyddiadwy, wedi'u fersiynu yn hytrach na chopïo a gludo.
- Amgodiwch bolisi fel cod, rheolau sefydliadol wedi'u mynegi fel cod y gellir ei wirio gan beiriant, fel bod cledrau diogelwch yn awtomatig, nid yn gynghorol.
- Cadwch gyfrinachau allan o ddiffiniadau; cyfeiriwch atynt o reolwr cyfrinachau pwrpasol.

## Argymhellion

### Dewiswch offeryn datganiadol a'i strwythuro o gwmpas modylau

Mabwysiadwch offeryn IaC datganiadol, fel [Terraform](https://en.wikipedia.org/wiki/Terraform_(software)), Pulumi, neu opsiwn brodorol-cwmwl fel CloudFormation, a safonwch arno ar draws y sefydliad fel eich bod yn osgoi tirwedd offer wedi'i dryllio. Y prif arfer pensaernïol yw modylaredd: adeiladwch fodylau bach, wedi'u dogfennu'n dda, wedi'u fersiynu sy'n dal patrymau cyffredin (rhwydwaith cydymffurfiol, cronfa ddata galedwyd, gwasanaeth safonol). Yna mae timau'n cyfansoddi amgylcheddau o'r modylau hyn yn hytrach na llunio adnoddau crai. Mae hyn yn lledaenu diofynion da a gosodiadau diogelwch yn awtomatig ac yn lleihau dyblygu'n ddramatig.

### Rheolwch gyflwr yn fwriadol

Mae offer datganiadol yn tracio'r mapio rhwng cod ac adnoddau go iawn mewn ffeil gyflwr. Storiwch gyflwr o bell mewn cefn-ben a rennir, wedi'i amgryptio, wedi'i reoli-mynediad, a defnyddiwch gloi fel na all newidiadau cydamserol ei lygru. Peidiwch byth â chadw cyflwr ar liniadur, a pheidiwch byth â'i olygu â llaw ac eithrio fel gweithred adfer moddion olaf. Mae cyflwr yn sensitif, oherwydd gall gynnwys metadata adnoddau a chyfrinachau, felly amddiffynnwch ef yn unol â hynny.

### Adeiladwch seilwaith anhydraidd gyda delweddau euraidd

Yn hytrach na phatsio gweinyddion sy'n rhedeg, pobwch "ddelwedd euraidd" wedi'i fersiynu (peiriant neu ddelwedd cynhwysydd wedi'i chyn-ffurfweddu, wedi'i galedu) a defnyddiwch achosion ffres ohoni. Pan fydd angen newid neu batsh arnoch, adeiladwch ddelwedd newydd a'i chyflwyno, gan ymddeol yr hen achosion. Mae hyn yn dileu drifft ffurfweddiad, yn gwneud ôl-dröi'n ddibwys, ac yn cadw pob achos yn union yr un fath ac yn olrheiniadwy i adeiladwaith hysbys-dda. Dylai piblinellau delwedd awtomataidd gynnwys caledu a sganio diogelwch, fel bod cydymffurfiaeth wedi'i hadeiladu i mewn ar lefel y ddelwedd.

### Canfyddwch a chysonwch ddrifft ffurfweddiad

Mae drifft yn digwydd pan fydd yr amgylchedd byw'n gwyro oddi wrth ei ddiffiniad, fel arfer oherwydd bod rhywun wedi gwneud newid brys â llaw. Rhedwch ganfod drifft rheolaidd sy'n cymharu cyflwr gwirioneddol â chyflwr datganedig a fflagio'r gwahaniaethau. Triniwch ddrifft fel diffyg: cysonwch trwy ddiweddaru'r cod a'i ail-gymhwyso, nid trwy adael y newid â llaw yn ei le. Ar gyfer systemau sydd angen gorfodaeth ffurfweddiad barhaus, defnyddiwch offeryn rheolaeth ffurfweddiad sy'n cydgyfeirio gwesteion yn barhaus at eu cyflwr datganedig.

### Mabwysiadwch GitOps a defnyddio wedi'i seilio ar dynnu

Yn y model GitOps, mae ystorfa Git yn dal cyflwr dymunol datganedig y system, ac mae asiant awtomataidd sy'n rhedeg y tu mewn i'r amgylchedd targed yn tynnu'r cyflwr hwnnw'n barhaus ac yn cysoni'r system fyw i gyfateb. Mae hyn yn troi'r model gwthio traddodiadol wyneb i waered. Nid oes angen credadau sefydlog ar unrhyw system allanol i newid yr amgylchedd, oherwydd mae'r amgylchedd yn tynnu ei ffurfweddiad ei hun. Mae GitOps yn rhoi llwybr archwilio cyflawn i chi (mae pob newid yn ymrwymiad), ôl-dröi hawdd (gwrthdroi'r ymrwymiad), a chywiro drifft cryf (mae'r asiant yn ail-ddatgan y cyflwr dymunol yn barhaus). Mae'n bwerus yn arbennig ar gyfer [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) ac ar gyfer sefydliadau sydd eisiau ffynhonnell wirionedd sengl, adolygadwy.

### Gorfodwch gledrau gyda pholisi fel cod

Mynegwch reolau sefydliadol, fel rhanbarthau a ganiateir, amgryptio gorfodol, tagiau gofynnol, ac amlygiad cyhoeddus gwaharddedig, fel polisïau y gellir eu gwirio gan beiriant gan ddefnyddio offeryn fel Open Policy Agent (OPA) neu injan bolisi brodorol-platfform fel Sentinel. Rhedwch y gwiriadau hyn yn y biblinell cyn darparu, fel bod toriadau'n cael eu rhwystro'n awtomatig. Mae polisi fel cod yn troi bwriad tîm diogelwch yn rheolaeth weithredadwy, wedi'i chymhwyso'n unffurf, ac mae'n graddfeydd i filoedd o newidiadau mewn ffordd na allai adolygiad â llaw byth ei wneud.

## Cyfnewidfeydd: manteision ac anfanteision

| Dewis | Manteision | Anfanteision | Ffit gorau |
|---|---|---|---|
| IaC datganiadol (Terraform/Pulumi) | Atgynyrchiadwy, adolygadwy, drifft-ganfodadwy | Tro dysgu; cymhlethdod rheoli cyflwr | Bron pob tîm ar raddfa fawr |
| Sgriptiau gorchmynnol | Cyfarwydd; hyblyg ar gyfer un-tro | Nid yn idempotent; anodd ei archwilio a'i ailadrodd | Achosion cul, dros dro |
| Anhydraidd + delweddau euraidd | Dim drifft; ôl-dröi dibwys | Baich piblinell adeiladu delwedd | Fflydoedd sydd angen cysondeb |
| Rheolaeth ffurfweddiad hydraidd | Rheolaeth barhaus manwl | Risg drifft; cydgyfeirio arafach | Gwesteion etifeddiaeth neu hirhoedlog |
| GitOps (wedi'i seilio ar dynnu) | Llwybr archwilio cryf; hunanwellhau | Angen asiant mewn-clwstwr a disgyblaeth Git | Kubernetes a brodorol-cwmwl |
| Polisi fel cod | Cledrau awtomatig, unffurf | Ymdrech ysgrifennu polisi ymlaen llaw | Amgylcheddau rheoleiddiedig |

Y prif densiwn yw rhwng hyblygrwydd a rheolaeth. Mae dulliau â llaw a gorchmynnol yn teimlo'n gyflymach ar gyfer un newid, ond maent yn cronni anghysondeb cudd sy'n dod yn analluogol ar raddfa fawr. Mae seilwaith datganiadol, anhydraidd, wedi'i lywodraethu gan bolisi'n gofyn am fwy o fuddsoddiad ymlaen llaw a symudiad diwylliannol go iawn, gan fod yn rhaid i beirianwyr stopio gwneud newidiadau consol cyflym, ond mae'n talu'r buddsoddiad hwnnw'n ôl lawer gwaith drosodd mewn dibynadwyedd, archwiliadwyedd, a'r gallu i ailadeiladu unrhyw beth ar alw.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Pwy sy'n berchen ar y llyfrgell modylau a rennir, a sut mae gwelliant mewn modiwl yn cyrraedd pob tîm sy'n ei ddefnyddio?** Nid yw modylau ond yn talu ar eu canfed os yw trwsiadau a diofynion caledwyd yn lledaenu, ac mae hynny'n gofyn am berchnogaeth glir a fersiynu go iawn, nid ffolder y mae pawb yn copïo ohono. Penderfynwch pwy sy'n cynnal y modylau rhwydwaith-cydymffurfiol a chronfa-ddata-galedwyd, sut rydych yn eu fersiynu (fersiynu semantig gyda log newid), a sut mae timau'n tynnu uwchraddiadau heb ymarfer tân. Ar raddfa fawr dyma'r gwahaniaeth rhwng trwsio camffurfweddiad unwaith a'i hela ar draws mil o adnoddau wedi'u golygu â llaw. Dewch â thystiolaeth: faint o gopïau gwahanol o'r un patrwm sy'n bodoli heddiw, faint o amser mae trwsiad diogelwch yn ei gymryd i gyrraedd pob amgylchedd, ac a yw timau'n pinio fersiynau modylau neu'n eu harnofio. Os na all patsh critigol gyrraedd yr ystâd gyfan mewn dyddiau, mae eich modylaredd yn gosmetig.

2. **Beth yw eich patrwm canfod drifft, a beth sy'n digwydd mewn gwirionedd pan ganfyddir drifft?** Drifft yw'r amgylchedd byw'n gwyro'n dawel oddi wrth ei gyflwr datganedig, fel arfer o newid consol brys, ac mae goddef hynny'n troi eich cod yn ffuglen. Penderfynwch pa mor aml rydych yn cymharu cyflwr gwirioneddol â chyflwr datganedig (mae bob nos yn ddiofyn rhesymol) a, yn bwysicach, penderfynwch yr ymateb: cysonwch trwy ddiweddaru'r cod a'i ail-gymhwyso, byth trwy adael y newid â llaw yn ei le. Mewn lleoliadau rheoleiddiedig mae hyn yn ofyniad rheolaeth, oherwydd bod angen i archwilwyr fod â'r cyflwr datganedig yn cyfateb i realiti'n barhaus. Dewch â'ch rhifau cyfredol: faint o adnoddau sy'n drifftio bob wythnos, am ba mor hir maent yn aros wedi drifftio, ac a oes unrhyw un yn atebol am eu cau. Triniwch bob drifft fel diffyg â pherchennog, neu mae'r warant ffynhonnell-wirionedd yn erydu hyd nes nad oes neb yn ymddiried yn y cod.

3. **A ydych wedi symud i GitOps a chysoni wedi'i seilio ar dynnu, neu a yw system allanol yn dal i ddal credadau sefydlog i newid cynhyrchu?** Yn y model tynnu mae asiant y tu mewn i'r amgylchedd targed yn cysoni'r system fyw i Git yn barhaus, sy'n dileu'r angen i unrhyw system allanol ddal mynediad ysgrifennu, ac mae'n ail-ddatgan y cyflwr dymunol fel bod drifft yn hunangywiro. Dyna osgo diogelwch ac archwilio cryf, gan fod pob newid yn ymrwymiad ac nid oes angen credadau cynhyrchu sefydlog ar unrhyw weithredwr. Mae'r gost yn real: asiant mewn-clwstwr i'w redeg a disgyblaeth Git lym, felly pwyswch hynny yn erbyn eich awtomeiddio wedi'i seilio ar wthio cyfredol. Dewch â'r rhestr o bwy a beth all newid cynhyrchu'n uniongyrchol ar hyn o bryd, a pha lwybr archwilio y mae'r newidiadau hynny'n ei adael. Ar gyfer Kubernetes ac amgáuau sicrwydd-uchel mae'r symudiad hwn fel arfer yn werth chweil; ar gyfer llond llaw o adnoddau statig gall fod yn ormod.

4. **Sut mae cyflwr eich seilwaith yn cael ei storio, ei gloi, a'i reoli-mynediad, a beth sy'n digwydd ar y diwrnod y caiff ei lygru neu ei golli?** Cyflwr yw'r map rhwng eich cod a'r adnoddau go iawn, felly gall ffeil gyflwr wedi'i cholli neu wedi'i difrodi adael offeryn yn ddall i adnoddau a greodd a themtio rhywun i ailgymhwyso dinistriol. I dîm mawr mae'r risg yn lluosi, oherwydd bod angen cefn-ben o bell, wedi'i amgryptio, wedi'i gloi ar lawer o beirianwyr sy'n cymhwyso yn erbyn cyflwr a rennir fel na all rhediadau cydamserol daro ei gilydd. Pwyswch gyfleustra un cyflwr mawr yn erbyn y radiws ffrwydro y mae'n ei greu, ac ystyriwch hollti cyflwr fesul amgylchedd neu fesul parth fel na all un camgymeriad sengl ddymchwel popeth. Dewch â'r ffeithiau: ble mae cyflwr yn byw heddiw, a yw cloi'n cael ei orfodi, pwy all ei ddarllen (gall gynnwys cyfrinachau), ac a ydych erioed wedi ymarfer adferiad. Mewn lleoliadau menter a llywodraeth, triniwch y cefn-ben cyflwr fel ased sensitif, wedi'i reoli-mynediad gyda'i wrth-gopi, log archwilio, a llyfr rhedeg adferiad ei hun, oherwydd mae ei golli'n golli eich cofnod o'r hyn sy'n bodoli.

5. **Pan fydd argyfwng gwirioneddol yn mynnu newid â llaw, beth yw'r llwybr torri-gwydr cymeradwy, a sut mae'r newid hwnnw'n cael ei blygu'n ôl i mewn i god?** Mae pob arfer IaC aeddfed yn y pen draw yn cwrdd â'r digwyddiad 3 y bore lle nad yw aros am biblinell yn dderbyniol, a'r cwestiwn gonest nid yw a yw newidiadau â llaw byth yn digwydd ond sut rydych yn eu cyfyngu. Penderfynwch ymlaen llaw pwy sy'n cael osgoi'r biblinell, beth mae ganddynt hawl i'w gyffwrdd, sut mae'r weithred yn cael ei chofnodi, a'r dyddiad cau y mae'n rhaid i'r newid gael ei gysoni i mewn i god neu ei wrthdroi erbyn hynny. Heb y cytundeb hwnnw, mae'r eithriad brys yn tawel ddod yn arferiad bob dydd ac mae ClickOps yn dychwelyd trwy'r drws cefn. Dewch â thystiolaeth: faint o newidiadau y tu allan i'r sianel a ddigwyddodd y chwarter diwethaf, am ba mor hir arhosodd pob un heb ei gysoni, ac a wnaeth canfod drifft eu dal mewn gwirionedd. I gyrff rheoleiddiedig a chyhoeddus, mae gweithdrefn torri-gwydr ddogfennedig gyda chofnodi awtomatig yn aml yn ofyniad rheolaeth, oherwydd mae archwilwyr yn disgwyl bod argyfyngau'n bosibl ac y bydd pob un yn gadael llwybr ac yn dychwelyd y system i'w chyflwr datganedig.

6. **Faint o'ch llinell sylfaen diogelwch a chydymffurfiaeth sy'n cael ei fynegi fel polisi sy'n rhwystro newid gwael yn awtomatig, yn erbyn rheolau sy'n byw mewn dogfen ac yn dibynnu ar i rywun eu cofio?** Mae cledrau wedi'u hysgrifennu fel rhyddiaith mewn wici'n cael eu torri'n rheolaidd, oherwydd eu bod yn dibynnu ar bob peiriannydd yn eu darllen a'u cymhwyso o dan bwysau dyddiad cau, tra bod yr un rheolau wedi'u mynegi fel polisi fel cod yn gwrthod newid anghydymffurfiol cyn iddo gael ei ddarparu erioed. I sefydliad mawr dyma'r unig ffordd y mae bwriad tîm diogelwch yn graddfeydd i filoedd o newidiadau heb ddod yn dagfa adolygu. Pwyswch gost ymlaen llaw ysgrifennu a chynnal polisïau yn erbyn cost ailadroddus adolygiad â llaw ac adferiad wedi'r digwyddiad, a phenderfynwch pa reolaethau (amgryptio, rhanbarthau cymeradwy, tagiau gorfodol, dim amlygiad cyhoeddus) sy'n ddigon anhrafodadwy i'w gorfodi fel giatiau caled. Dewch â'r rhestr o'ch rheolau llinell sylfaen cyfredol a marciwch pa rai sydd wedi'u hawtomeiddio yn erbyn cynghorol, ynghyd â pha mor aml y caiff pob un ei dorri mewn gwirionedd. Mewn cyd-destunau menter a llywodraeth, mae polisi awtomataidd yn trosi archwiliad o wythnosau o gasglu tystiolaeth â llaw yn ymholiad yn erbyn rheolaethau gorfodedig, ac mae'n troi cydymffurfiaeth o ganfod yn atal.

## Lens sector

**Cwmni newydd.** Mae cyflymder yn ennill, felly rhowch eich stac cyfan mewn un ystorfa ddatganiadol (mae Terraform yn ddiofyn cyffredin), cadwch gyflwr mewn cefn-ben wedi'i reoli, wedi'i amgryptio, a llwybrwch bob newid trwy gais tynnu hyd yn oed gyda thîm o dri. Sgipiwch y peiriannau platfform trwm: dim tîm modylau canolog, dim injan bolisi eto, dim ond rheolaeth fersiynau a'r ddisgyblaeth i beidio byth â chlicio yn y consol. Mae hynny ar ei ben ei hun yn rhoi amgylcheddau atgynyrchiadwy i chi y gallwch eu tynnu i lawr i arbed arian a'u hailadeiladu ar gyfer y dangosiad nesaf.

**Busnes bach.** Heb arbenigwr platfform pwrpasol, dibynnwch ar wasanaethau a reolir a pha IaC bynnag y mae eich darparwr cwmwl neu werthwr eisoes yn ei gefnogi yn hytrach na chodi offer pwrpasol na allwch ei gynnal. Ffafriwch brynu platfform wedi'i westeio y mae ei ddiofynion synhwyrol (amgryptio, wrth-gopïau, patsio) wedi'u trin i chi dros adeiladu piblinell delwedd euraidd nad oes gennych neb i'w rhedeg. Fframiwch y nod yn gul: cael eich llond llaw o adnoddau critigol i mewn i god fel y gallwch eu hailadeiladu ar ôl methiant neu gontractwr sy'n gadael.

**Menter.** Y broblem graidd yw cysondeb ar draws llawer o dimau, cyfrifon, a rhanbarthau, felly buddsoddwch mewn llyfrgell modylau a rennir wedi'i fersiynu, cyflwr wedi'i gloi o bell, a pholisi fel cod wedi'i orfodi yn y biblinell. Mae tîm platfform canolog yn cyhoeddi modylau a chledrau caledwyd tra bo timau cynnyrch yn hunanwasanaethu o'u mewn, ac mae canfod drifft yn rhedeg yn barhaus fel bod miloedd o adnoddau'n aros mewn cyflwr hysbys. Cyllidebwch gost barhaus cynnal modylau a pholisïau, oherwydd daw eu gwerth o drwsiad neu ddiofyn caledwyd yn lledaenu ym mhobman ar unwaith.

**Llywodraeth.** Mae rheolau caffael, achrediad, ac atebolrwydd cyhoeddus yn eich gwthio tuag at seilwaith anhydraidd, ymrwymiadau wedi'u llofnodi, a chysoni GitOps y tu mewn i amgáu achrededig, fel nad oes gan unrhyw weithredwr gredadau sefydlog i newid cynhyrchu. Amgodiwch y llinell sylfaen diogelwch ofynnol i mewn i ddelweddau euraidd a pholisi fel cod, a gadewch i hanes yr ymrwymiadau wasanaethu fel tystiolaeth archwilio ymhlyg-ymyrryd, ar gael yn barhaus. Ffafriwch offer agored, cludadwy dros fformatau perchnogol sy'n eich dal, a gwnewch y weithdrefn torri-gwydr a'i chofnodi'n eglur fel bod newidiadau brys yn dal i fodloni gofynion rheoli ffurfweddiad.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd pum person yn diffinio ei osodiad AWS cyfan, sef y VPC, y gronfa ddata, a'r gwasanaeth cynhwysydd, mewn un ystorfa Terraform gyda chyflwr wedi'i gadw mewn cefn-ben S3 wedi'i amgryptio a chloi trwy DynamoDB. Mae pob newid yn mynd trwy gais tynnu, felly gall hyd yn oed peiriannydd ar-alwad unigol weld yn union beth fydd yn newid cyn rhedeg cymhwyso. Pan fydd angen amgylchedd llwyfannu ffres arnynt ar gyfer dangosiad mawr, maent yn copïo modiwl bach ac yn ei godi mewn munudau, ac yn ei dynnu i lawr yr un mor gyflym i gadw'r bil cwmwl yn isel.

**Menter.** Mae manwerthwr rhyngwladol yn rheoli seilwaith ar draws sawl cyfrif cwmwl a rhanbarth. Mae tîm platfform canolog yn cyhoeddi modylau Terraform wedi'u fersiynu ar gyfer rhwydweithiau cydymffurfiol, cronfeydd data, a fframwaith gwasanaeth, ac yn gorfodi polisïau OPA sy'n gwrthod unrhyw adnodd sy'n brin o dagiau amgryptio neu ddyraniad cost. Mae timau cynnyrch yn darparu eu hamgylcheddau eu hunain yn hunanwasanaethol, ond mae pob newid yn llifo trwy'r biblinell, lle mae polisi'n cael ei wirio'n awtomatig. Mae canfod drifft yn rhedeg bob nos ac yn agor tocynnau ar gyfer unrhyw newid â llaw, gan gadw miloedd o adnoddau'n barhaus mewn cyflwr hysbys, cydymffurfiol.

**Llywodraeth.** Mae asiantaeth amddiffyn sy'n gweithredu mewn amgylchedd sicrwydd-uchel yn adeiladu delweddau euraidd caledwyd sy'n mewnblannu'r llinell sylfaen diogelwch ofynnol, ac yn defnyddio dim ond achosion anhydraidd o'r delweddau hynny. Mae'r holl seilwaith wedi'i ddatgan yn Git a'i gysoni gan asiant GitOps y tu mewn i'r amgáu achrededig, fel nad oes gan unrhyw weithredwr gredadau sefydlog i newid cynhyrchu'n uniongyrchol. Mae pob newid yn ymrwymiad wedi'i lofnodi. Mae hyn yn rhoi hanes cyflawn, ymhlyg-ymyrryd i archwilwyr ac yn bodloni gofynion monitro-parhaus a rheoli-ffurfweddiad heb gasglu tystiolaeth â llaw.

## Achos busnes: cymhellion, ROI, a TCO

Daw ROI IaC o gyflymder, dibynadwyedd, a lleihau risg. Gellir creu amgylcheddau a arferai gymryd wythnosau o ddarparu â llaw wedi'i yrru gan docyn mewn munudau, sy'n rhyddhau peirianwyr ac yn cyflymu prosiectau. Mae atgynyrchioldeb yn torri amser adfer ar ôl methiannau, oherwydd gellir ailadeiladu unrhyw amgylchedd o god. Mae gorfodaeth polisi awtomataidd yn lleihau amlder a chost digwyddiadau diogelwch a chanfyddiadau archwiliad, a all fod yn sylweddol i sefydliadau rheoleiddiedig.

Ar y ledger TCO, mae costau mabwysiadu'n cynnwys offer, hyfforddiant, adeiladu llyfrgell modiwl a pholisi, a'r ddisgyblaeth i stopio gwneud newidiadau â llaw. Mae cost peidio â mabwysiadu'n serthach ac yn cyfansymio dros amser: seilwaith pluen eira nad oes neb yn gallu ei ailadeiladu, darparu araf, tueddol o wallau, camffurfweddiadau diogelwch sy'n arwain at doriadau, ac archwiliadau sy'n treulio wythnosau o ymdrech â llaw. I arweinyddiaeth, fframiwch IaC fel trosi seilwaith o rwymedigaeth heb ei reoli'n ased wedi'i lywodraethu, atgynyrchiadwy, ac fel y mecanwaith sy'n gwneud diogelwch a chydymffurfiaeth yn awtomatig yn hytrach nag yn ddyhead.

## Gwrth-batrymau a pheryglon

- **ClickOps mewn cynhyrchu.** Mae gwneud newidiadau â llaw yn y consol yn gwarantu drifft ac yn dinistrio atgynyrchioldeb.
- **Cyfrinachau mewn cod.** Mae codio credadau'n galed mewn ffeiliau diffiniad yn eu gollwng i mewn i hanes fersiynau a chyflwr.
- **Diffiniadau monolithig, heb eu modyleiddio.** Mae un ffurfweddiad enfawr nad oes neb yn mentro ei newid yn dod mor fregus â'r gosodiad â llaw a ddisodlodd.
- **Cyflwr heb ei reoli.** Mae ffeiliau cyflwr lleol neu heb eu cloi'n arwain at lygredd a seilwaith coll.
- **Drifft yn cael ei oddef.** Mae gadael newidiadau â llaw yn eu lle'n erydu'r warant ffynhonnell-wirionedd hyd nes bod y cod yn ffuglen.
- **Polisi fel dogfennaeth.** Mae rheolau sy'n byw mewn wici yn hytrach na gwiriad awtomataidd yn cael eu torri'n rheolaidd.
- **Lledaeniad copïo-gludo.** Mae dyblygu ffurfweddiad ar draws timau'n golygu nad yw trwsiadau a gwelliannau byth yn lledaenu.

## Model aeddfedrwydd

**Lefel 1: Cychwyn.** Mae seilwaith yn cael ei ddarparu â llaw trwy'r consol a sgriptiau ad hoc. Mae amgylcheddau'n anghyson, heb eu dogfennu, ac ni ellir eu hatgynhyrchu'n ddibynadwy, ac mae adferiad ar ôl methiant yn araf ac yn ansicr.

**Lefel 2: Datblygu.** Mae rhywfaint o seilwaith wedi'i godeiddio, ond mae arferion yn amrywio yn ôl tîm. Mae rheolaeth cyflwr yn anghyson, mae drifft yn gyffredin, mae cyfrinachau weithiau'n gollwng i mewn i ddiffiniadau, a gorfodir polisi, os o gwbl, trwy adolygiad â llaw.

**Lefel 3: Safoni.** IaC datganiadol yw'r safon ddogfennedig ar draws y sefydliad, wedi'i adeiladu o fodylau a rennir, wedi'u fersiynu gyda chyflwr wedi'i reoli, o bell, wedi'i gloi. Mae polisi fel cod yn gorfodi cledrau yn y biblinell, cyfeirir at gyfrinachau o reolwr pwrpasol, ac mae canfod drifft yn rhedeg ar batrwm rheolaidd.

**Lefel 4: Rheoli.** Mae'r arfer yn cael ei fesur yn erbyn llinellau sylfaen. Rydych yn tracio cyfradd drifft ac amser cymedrig i gysoni, mabwysiadu fersiwn modiwl ar draws timau, toriadau polisi wedi'u rhwystro yn erbyn rhai a ddihangodd, amser arwain darparu, a chyfran yr adnoddau sydd mewn gwirionedd o dan god. Mae'r metrigau hyn yn giatio newidiadau ac yn llywio lle rydych yn buddsoddi, felly mae penderfyniadau'n gorffwys ar dystiolaeth yn hytrach nag anecdot.

**Lefel 5: Cerddorfa.** Mae seilwaith yn anhydraidd ac wedi'i yrru gan GitOps, yn hunanwellhau yn erbyn drifft, gyda thystiolaeth gydymffurfiaeth yn cael ei chynhyrchu'n awtomatig. Mae'r llyfrgell modiwl a pholisi'n gwella'n barhaus o ddefnydd go iawn a digwyddiadau, ac mae arfer seilwaith wedi'i integreiddio â chynllunio diogelwch, cost, a danfon fel bod yr ystâd gyfan yn addasu wrth i ofynion newid.

## Syniadau ar gyfer trafod

- Lle dylai'r llinell orwedd rhwng modylau a lywodraethir yn ganolog ac ymreolaeth tîm i ddiffinio seilwaith pwrpasol?
- Sut rydych yn trin y newid argyfwng gwirioneddol y mae'n rhaid iddo osgoi'r biblinell, heb normaleiddio ClickOps?
- Beth yw'r strategaeth gywir ar gyfer rheoli a diogelu cyflwr ar draws llawer o gyfrifon a thimau?
- Pryd mae rheolaeth ffurfweddiad hydraidd yn dal i fod yn gyfiawn yn erbyn seilwaith cwbl anhydraidd?
- Sut rydych yn cadw'r llyfrgell polisi-fel-cod yn unol â gofynion diogelwch a rheoleiddiol sy'n esblygu?
- Sut olwg sydd ar lwybr mudo realistig ar gyfer seilwaith etifeddiaeth sy'n rhagflaenu IaC?

## Casgliadau allweddol

- Diffiniwch seilwaith yn ddatganiadol, ei fersiynu, a'i drin fel cod adolygadwy, atgynyrchiadwy.
- Adeiladwch o fodylau bach, wedi'u fersiynu i ledaenu diofynion da a dileu dyblygu.
- Ffafriwch seilwaith anhydraidd a delweddau euraidd i ddileu drifft a symleiddio ôl-dröi.
- Rheolwch gyflwr yn fwriadol a chadwch gyfrinachau allan o ddiffiniadau.
- Mabwysiadwch GitOps am lwybr archwilio cryf a chysoni hunanwellhau.
- Gorfodwch gledrau gyda pholisi fel cod fel bod cydymffurfiaeth yn cael ei hatal rhag bodoli, nid ei harchwilio wedi'r digwyddiad.

## Cyfeiriadau a darllen pellach

- Kief Morris, *Infrastructure as Code: Dynamic Systems for the Cloud Age*.
- Yevgeniy Brikman, *Terraform: Up & Running*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, a Niall Richard Murphy (gol.), *Site Reliability Engineering*.
- Gene Kim, Jez Humble, Patrick Debois, a John Willis, *The DevOps Handbook*.
- Weaveworks, ysgrifau sylfaenol "GitOps" (Alexis Richardson et al.).
- Dogfennaeth Open Policy Agent a'r iaith bolisi Rego.
- NIST Special Publication 800-53, rheolaethau diogelwch a phreifatrwydd (teulu rheolaeth ffurfweddiad).
