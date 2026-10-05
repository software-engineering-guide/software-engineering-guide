# 12.3 Templedi

Mae'r templedi hyn yn bwyntiau cychwyn parod i'w copïo-a-gludo. Codwch unrhyw dempled i mewn i'ch wici, ystorfa, neu system docynnau a llenwch y lleoliadau-gadw mewn cromfachau sgwâr. Mae nodiadau italig a sylwadau mewnol yn esbonio beth sy'n perthyn ym mhob adran; dilëwch nhw unwaith y bydd yr adran wedi'i llenwi. Cadwch dempledi'n ysgafn: ni chaiff templed ei ddefnyddio os yw'n gyflymach ei sgipio nag i'w gwblhau. Addaswch benawdau ac adrannau i'ch sefydliad, ond cadwch fwriad pob rhan.

Ychydig o gonfensiynau a ddefnyddir isod:

- Mae testun mewn `[cromfachau sgwâr]` yn lleoliad-gadw i'w ddisodli.
- Mae testun mewn _italig_ neu `<!-- sylwadau -->` yn arweiniad i'w ddileu.
- Cadwch y ddogfen orffenedig mor fyr ag y gall fod tra'n dal i ateb ei chwestiynau.

## Cofnod Penderfyniad Pensaernïol (ADR)

```markdown
# ADR [NNNN]: [Teitl byr y penderfyniad]

- Statws: [Arfaethedig | Derbyniwyd | Anghymeradwywyd | Disodlwyd gan ADR-XXXX]
- Dyddiad: [YYYY-MM-DD]
- Penderfynwyr: [enwau neu rolau]
- Ymgynghorwyd: [enwau neu rolau]

## Cyd-destun

<!-- Beth yw'r broblem, y grym, neu'r cyfyngiad sy'n gyrru'r penderfyniad
     hwn? Nodwch y ffeithiau a'r gofynion yn niwtral. Cynhwyswch ddim ond
     yr hyn y mae angen i ddarllenydd yn y dyfodol ei ddeall pam roedd
     penderfyniad yn angenrheidiol. -->

## Penderfyniad

<!-- Nodwch y dewis mewn un neu ddwy frawddeg glir: "Byddwn yn ..." -->

## Dewisiadau amgen a ystyriwyd

<!-- Rhestrwch y dewisiadau realistig a bwysoch a pham y cafodd pob un
     ei ddewis neu beidio. Dylai o leiaf dau ddewis amgen ymddangos yma. -->

- Opsiwn A: [crynodeb]; gwrthodwyd oherwydd [rheswm].
- Opsiwn B: [crynodeb]; gwrthodwyd oherwydd [rheswm].
- Opsiwn a ddewiswyd: [crynodeb]; dewiswyd oherwydd [rheswm].

## Canlyniadau

<!-- Canlyniadau gonest y penderfyniad, da a drwg. -->

- Cadarnhaol: [manteision a enillwyd]
- Negyddol: [costau, risgiau, neu gyfyngiadau a dderbyniwyd]
- Dilyniant: [mudiadau, gwaith newydd, neu benderfyniadau y mae hyn yn eu sbarduno]

## Cysylltiedig

<!-- Dolenni i ADRs blaenorol, RFCs, tocynnau, neu ddogfennau y mae hyn
     yn ymwneud â nhw. -->
```

## RFC / dogfen ddylunio

```markdown
# RFC: [Teitl]

- Awdur(on): [enwau]
- Statws: [Drafft | Dan adolygiad | Cymeradwywyd | Gwrthodwyd | Wedi'i weithredu]
- Adolygwyr: [enwau neu rolau]
- Crëwyd: [YYYY-MM-DD]
- Diweddarwyd ddiwethaf: [YYYY-MM-DD]
- Tocyn / olrhain: [dolen]

## Crynodeb

<!-- Un paragraff: beth mae hyn yn ei gynnig a pham mae'n bwysig. Dylai
     darllenydd ddeall yr hanfod o'r adran hon yn unig. -->

## Problem a chymhelliant

<!-- Pa broblem rydym yn ei datrys? Pwy sy'n cael ei effeithio? Beth
     sy'n digwydd os na wnawn ddim? Cynhwyswch gefndir a chyfyngiadau
     perthnasol. -->

## Nodau a di-nodau

- Nodau: [sut olwg sydd ar lwyddiant, yn fesuradwy lle bo modd]
- Di-nodau: [yn benodol y tu allan i'r cwmpas, i atal ymledu cwmpas]

## Dyluniad arfaethedig

<!-- Craidd y ddogfen. Disgrifiwch y dull, y bensaernïaeth, y model
     data, y rhyngwynebau, a'r llifau allweddol. Defnyddiwch ddiagramau
     lle maent yn eglurhau. Esboniwch sut mae'n gweithio, nid dim ond
     beth ydyw. -->

## Dewisiadau amgen a ystyriwyd

<!-- Dulliau eraill a pham na chawsant eu dewis. Yn dangos i'r
     darllenydd bod y gofod dylunio wedi'i archwilio. -->

## Effaith a risgiau

- Diogelwch a phreifatrwydd: [goblygiadau a lliniariadau]
- Perfformiad a graddfa: [llwyth ac ymddygiad disgwyliedig]
- Gweithredoldeb: [monitro, moddau methiant, cyflwyno, dadwneud]
- Cost: [effaith seilwaith neu drwyddedu]
- Cydnawsedd ôl-weithredol: [mudo a dad-gymeradwyo]

## Cynllun profi a chyflwyno

<!-- Sut y bydd y newid yn cael ei ddilysu a'i ryddhau'n ddiogel. -->

## Cwestiynau agored

<!-- Materion heb eu datrys rydych am i adolygwyr roi barn arnynt. -->
```

## Post-mortem / adolygiad digwyddiad (di-fai)

```markdown
# Post-mortem: [Teitl digwyddiad]

- ID Digwyddiad: [ID]
- Dyddiad y digwyddiad: [YYYY-MM-DD]
- Awduron: [enwau]
- Statws: [Drafft | Terfynol]
- Difrifoldeb: [SEV1 | SEV2 | SEV3]

> Mae'r adolygiad hwn yn ddi-fai. Rydym yn canolbwyntio ar systemau a
> ffactorau cyfrannol, nid ar unigolion. Y nod yw dysgu ac atal
> ailddigwyddiad.

## Crynodeb

<!-- Dwy neu dair brawddeg: beth ddigwyddodd, yr effaith, a'r
     datrysiad, yn ddarllenadwy gan rywun nad yw'n arbenigwr. -->

## Effaith

- Hyd: [amser cychwyn i amser adfer, gyda chylchfa amser]
- Defnyddwyr yr effeithiwyd arnynt: [cwmpas a nifer]
- Effaith fusnes: [refeniw, SLA, enw da, neu arall]

## Amserlin

<!-- Dilyniant ffeithiol o ddigwyddiadau gyda stampiau amser.
     Cynhwyswch ganfod, uwchgyfeirio, camau allweddol, ac adferiad. -->

- [HH:MM] [digwyddiad]
- [HH:MM] [digwyddiad]

## Ffactorau cyfrannol

<!-- Y gadwyn o amodau a arweiniodd at y digwyddiad. Ffafriwch
     "ffactorau cyfrannol" dros un achos gwraidd sengl. -->

## Canfod ac ymateb

- Sut y'i canfuwyd? [rhybudd, adroddiad cwsmer, ac ati]
- Beth helpodd yr ymateb?
- Beth arafodd yr ymateb?

## Beth aeth yn dda

<!-- Cydnabod camau effeithiol a mesurau diogelu a weithiodd. -->

## Eitemau gweithredu

<!-- Penodol, â pherchennog, a dyddiedig. Rhowch sylw i atal, canfod,
     a lliniaru. Olrheiniwch y rhain yn y backlog arferol. -->

| Gweithred | Perchennog | Dyddiad dyledus | Math (atal/canfod/lliniaru) | Tocyn |
|--------|-------|----------|--------------------------------|--------|
| [gweithred] | [enw] | [dyddiad] | [math] | [dolen] |

## Gwersi a ddysgwyd

<!-- Beth ddylai'r sefydliad ehangach ei ddysgu. -->
```

## Model bygythiad (seiliedig ar STRIDE)

```markdown
# Model bygythiad: [Enw system neu nodwedd]

- Awdur(on): [enwau]
- Dyddiad: [YYYY-MM-DD]
- Adolygwyr: [cyswllt diogelwch, perchnogion]
- Cwmpas: [beth sy'n cael ei gwmpasu a beth nad yw]

## Trosolwg system

<!-- Disgrifiad byr o'r system, ei phwrpas, a'i defnyddwyr. -->

## Asedau

<!-- Beth sy'n werth ei ddiogelu: data, manylion mynediad,
     ymarferoldeb, enw da. Nodwch sensitifrwydd pob un. -->

## Ffiniau ymddiriedaeth a llif data

<!-- Disgrifiwch neu ddiagramwch gydrannau, storfeydd data, endidau
     allanol, a'r ffiniau lle mae ymddiriedaeth yn newid. -->

## Bygythiadau (STRIDE)

<!-- Ar gyfer pob elfen, ystyriwch gategorïau STRIDE. Cofnodwch bob
     bygythiad credadwy, ei risg, a'r lliniariad neu'r risg a
     dderbyniwyd. -->

| Bygythiad | Categori STRIDE | Elfen yr effeithiwyd arni | Risg (I/C/U) | Lliniariad | Statws |
|--------|-----------------|------------------|--------------|------------|--------|
| [bygythiad] | Ffugio | [elfen] | [risg] | [rheolaeth] | [agored/wedi'i liniaru/derbyniwyd] |
| [bygythiad] | Ymyrryd | [elfen] | [risg] | [rheolaeth] | [statws] |
| [bygythiad] | Gwadu | [elfen] | [risg] | [rheolaeth] | [statws] |
| [bygythiad] | Datgelu gwybodaeth | [elfen] | [risg] | [rheolaeth] | [statws] |
| [bygythiad] | Gwadu gwasanaeth | [elfen] | [risg] | [rheolaeth] | [statws] |
| [bygythiad] | Dyrchafu breintiau | [elfen] | [risg] | [rheolaeth] | [statws] |

## Tybiaethau a dibyniaethau

<!-- Tybiaethau diogelwch y dibynnir arnynt a rheolaethau allanol yr
     ymddirir ynddynt. -->

## Materion agored a dilyniant

<!-- Bygythiadau sydd angen gwaith pellach, wedi'u holrhain fel
     tocynnau. -->
```

## Llyfr rhedeg

```markdown
# Llyfr rhedeg: [Enw tasg neu senario]

- Gwasanaeth: [enw gwasanaeth]
- Perchennog: [tîm]
- Adolygwyd ddiwethaf: [YYYY-MM-DD]
- Rhybuddion cysylltiedig: [enwau rhybudd]

## Pwrpas

<!-- Pryd i ddefnyddio'r llyfr rhedeg hwn a beth mae'n ei gyflawni. -->

## Rhagofynion

<!-- Mynediad, offer, a chaniatâd sydd eu hangen cyn dechrau. -->

## Canfod / symptomau

<!-- Yr hyn y mae'r gweithredwr yn ei arsylwi: rhybuddion, llofnodion
     gwall, dangosfyrddau. -->

## Diagnosis

<!-- Gwiriadau cam-wrth-gam i gadarnhau'r broblem a chulhau'r achos.
     Cynhwyswch y gorchmynion, ymholiadau, neu ddolenni dangosfwrdd
     union. -->

1. [cam a chanlyniad disgwyliedig]
2. [cam a chanlyniad disgwyliedig]

## Datrysiad

<!-- Camau pendant, wedi'u trefnu i drwsio neu liniaru. Nodwch unrhyw
     gam sy'n risgus neu'n anwrthdroadwy, a sut i wirio llwyddiant. -->

1. [cam]
2. [gwirio adferiad]

## Dadwneud

<!-- Sut i ddadwneud y camau os yw'r datrysiad yn gwaethygu pethau. -->

## Uwchgyfeirio

<!-- Pwy i gysylltu â nhw a phryd i uwchgyfeirio. Cysylltiadau
     ar-alwad eilaidd, tîm perchen, a gwerthwr. -->

## Cyfeiriadau

<!-- Dangosfyrddau, llyfrau rhedeg cysylltiedig, dogfennau
     pensaernïaeth. -->
```

## README gwasanaeth / cofnod catalog gwasanaeth

```markdown
# [Enw gwasanaeth]

- Tîm perchen: [tîm]
- Ar-alwad: [dolen cylchdro]
- Haen / hollbwysigrwydd: [Haen 1 | 2 | 3]
- Ystorfa: [dolen]
- Statws: [Gweithredol | Anghymeradwywyd]

## Beth mae'n ei wneud

<!-- Un paragraff ar gyfrifoldeb y gwasanaeth a'i ddefnyddwyr. -->

## Pensaernïaeth

<!-- Cydrannau allweddol, dibyniaethau (i fyny'r afon ac i lawr yr
     afon), a dolen i'r ddogfen ddylunio neu ddiagram. -->

## Rhyngwynebau

- APIs / pwyntiau terfyn: [dolen i'r fanyleb]
- Digwyddiadau a gyhoeddir / a ddefnyddir: [pynciau]
- Storfeydd data: [cronfeydd data, storfeydd cudd, bwcedi]

## Amser rhedeg a defnyddio

- Amgylcheddau: [dev, llwyfannu, cynhyrchu]
- Sut i ddefnyddio: [dolen biblinell a phroses]
- Ffurfweddiad a fflagiau nodwedd: [ble a sut]

## Arsylwadaeth

- Dangosfyrddau: [dolenni]
- Rhybuddion: [dolenni]
- Logiau: [ble i ddod o hyd iddynt]
- SLOs: [dolen]

## Gweithrediadau

- Llyfrau rhedeg: [dolenni]
- Tasgau cyffredin: [graddio, ailgychwyn, llenwi-nôl]
- Materion a chyfyngiadau hysbys: [nodiadau]

## Dechrau arni (ar gyfer cyfranwyr newydd)

<!-- Sut i adeiladu, profi, a rhedeg yn lleol. -->

## Cysylltiadau

- Slack / sianel sgwrsio: [dolen]
- Uwchgyfeirio: [llwybr]
```

## Polisi SLO / cyllideb gwallau

```markdown
# Polisi SLO a chyllideb gwallau: [Enw gwasanaeth neu daith]

- Perchennog: [tîm]
- Dyddiad dod i rym: [YYYY-MM-DD]
- Amlder adolygu: [e.e. chwarterol]

## Dangosyddion lefel gwasanaeth (SLIs)

<!-- Diffiniwch bob SLI yn union: y maint a fesurir, sut y'i mesurir,
     ac o ble (yn ddelfrydol o safbwynt y defnyddiwr). -->

| SLI | Diffiniad | Ffynhonnell ddata |
|-----|-----------|-------------|
| Argaeledd | [e.e. ceisiadau llwyddiannus / cyfanswm ceisiadau] | [ffynhonnell] |
| Oedi | [e.e. cyfran o geisiadau o dan Xms] | [ffynhonnell] |

## Amcanion (SLOs)

| SLI | Targed | Ffenestr fesur |
|-----|--------|--------------------|
| Argaeledd | [e.e. 99.9%] | [e.e. 28 diwrnod treiglo] |
| Oedi | [e.e. 95% o dan 300ms] | [28 diwrnod treiglo] |

## Cyllideb gwallau

<!-- Yr annibynadwyedd a ganiateir: 100% minws y targed, dros y
     ffenestr. Nodwch y gyllideb mewn termau pendant (e.e. munudau/mis). -->

- Cyllideb: [lwfans a ddeilliwyd]

## Polisi pan fydd y gyllideb wedi'i disbyddu

<!-- Y canlyniadau y cytunwyd arnynt. Gwnewch nhw'n bendant ac yn
     orfodadwy. -->

- [e.e. Rhewi rhyddhadau nodwedd anghritigol nes bod y gyllideb yn adfer.]
- [e.e. Blaenoriaethu gwaith dibynadwyedd yn y cylch cynllunio nesaf.]
- [e.e. Uwchgyfeirio i arweinyddiaeth peirianneg os torrir dwy ffenestr yn olynol.]

## Polisi pan fydd y gyllideb yn iach

<!-- Pa risg ychwanegol y gall y tîm ei chymryd, e.e. cyflwyniadau
     cyflymach. -->

## Rhybuddio

<!-- Rhybuddion cyfradd-losgi a throthwyon wedi'u clymu i'r SLO hwn. -->
```

## Cofnod cofrestr risg

```markdown
## Risg: [Teitl risg byr]

- ID Risg: [ID]
- Dyddiad codwyd: [YYYY-MM-DD]
- Perchennog: [enw neu rôl sy'n gyfrifol am reoli'r risg hon]
- Categori: [diogelwch | gweithredol | cydymffurfiaeth | ariannol | traddodi | gwerthwr]
- Statws: [Agored | Wrthi'n lliniaru | Derbyniwyd | Wedi cau]

### Disgrifiad

<!-- Nodwch y risg fel: achos -> digwyddiad -> canlyniad. Beth allai
     ddigwydd, a pham mae'n bwysig. -->

### Asesiad

- Tebygolrwydd: [Isel | Canolig | Uchel]
- Effaith: [Isel | Canolig | Uchel]
- Sgôr gyffredinol: [wedi'i deillio o debygolrwydd x effaith]

### Rheolaethau presennol

<!-- Beth sydd eisoes yn lleihau'r risg hon heddiw. -->

### Cynllun lliniaru

<!-- Camau arfaethedig i leihau tebygolrwydd neu effaith, gyda
     pherchnogion a dyddiadau. Os yn derbyn y risg, cofnodwch pwy a'i
     derbyniodd a pham. -->

| Gweithred | Perchennog | Dyddiad dyledus | Statws |
|--------|-------|----------|--------|
| [gweithred] | [enw] | [dyddiad] | [statws] |

### Adolygiad

- Dyddiad adolygu nesaf: [YYYY-MM-DD]
- Penderfyniad / nodiadau: [unrhyw ymgymeradwyaeth derbyn neu newid]
```

## Un-dudalen prosiect / briff cynnyrch

```markdown
# [Enw prosiect neu gynnyrch]: un-dudalen

- Noddwr: [enw]
- Arweinydd: [enw]
- Dyddiad: [YYYY-MM-DD]
- Statws: [Syniad | Cymeradwywyd | Ar y gweill | Wedi'i anfon]

## Problem

<!-- Un paragraff: y broblem gwsmer neu fusnes, a thystiolaeth ei bod
     yn wirioneddol ac yn werth ei datrys. -->

## Cynulleidfa

<!-- Pwy sydd â'r broblem hon a phwy sy'n elwa o'i datrys. -->

## Datrysiad arfaethedig

<!-- Disgrifiad byr o'r hyn y byddwn yn ei adeiladu neu ei newid.
     Cadwch ef ar lefel bwriad, nid manylion gweithredu. -->

## Pam nawr

<!-- Y rheswm dros wneud hyn nawr yn hytrach nag yn ddiweddarach. -->

## Metrigau llwyddiant

<!-- Sut y byddwn yn gwybod ei fod wedi gweithio. Ffafriwch ganlyniadau
     mesuradwy. -->

- [metrig a tharged]

## Cwmpas

- O fewn cwmpas: [beth wnawn ni]
- Y tu allan i'r cwmpas: [beth na wnawn ni]

## Risgiau a chwestiynau agored

<!-- Prif ansicrwyddau a dibyniaethau. -->

## Cynllun bras a cherrig milltir

<!-- Camau lefel-uchel ac amseriad bras. -->

## Cost ac adnoddau

<!-- Pobl, amser, a chyllideb sydd eu hangen. -->
```

## Nodiadau trosglwyddo ar-alwad

```markdown
# Trosglwyddo ar-alwad: [YYYY-MM-DD]

- Yn gadael: [enw]
- Yn dod i mewn: [enw]
- Gwasanaeth(au): [enwau]

## Statws cyffredinol

<!-- Un llinell: tawel, swnllyd, neu fater parhaus. -->

## Digwyddiadau agored

<!-- Unrhyw ddigwyddiadau gweithredol neu wedi'u datrys yn ddiweddar y
     mae'n rhaid i'r ymatebwr nesaf wybod amdanynt, gyda dolenni. -->

- [digwyddiad, statws, a beth sy'n weddill]

## Newidiadau parhaus neu arfaethedig

<!-- Defnyddiadau, mudiadau, ffenestri cynnal a chadw, neu arbrofion
     ar waith a allai achosi rhybuddion. -->

## Rhybuddion swnllyd neu bigog

<!-- Rhybuddion a danwyd a'u gwir ystyr, fel nad yw'r person nesaf yn
     cael ei gamarwain. Nodwch unrhyw dawelu dros dro a'u dod-i-ben. -->

## Eitemau i'w gwylio

<!-- Metrigau neu systemau'n tueddu i gyfeiriad sy'n peri pryder. -->

## Dilyniannau ar y gweill

<!-- Tasgau wedi'u trosglwyddo i'r shifft nesaf, gyda dolenni i
     docynnau. -->

## Nodiadau

<!-- Unrhyw beth arall defnyddiol: nodweddion mynediad rhyfedd,
     materion gwerthwr, cyd-destun. -->
```

## Cais newid (ar gyfer rheolaeth newid reoledig)

```markdown
# Cais newid: [Teitl newid]

- ID Newid: [ID]
- Ceisiwr: [enw]
- Dyddiad cyflwyno: [YYYY-MM-DD]
- Math: [Safonol | Arferol | Argyfwng]
- Blaenoriaeth: [Isel | Canolig | Uchel]
- Statws: [Cyflwynwyd | Cymeradwywyd | Gwrthodwyd | Wedi'i weithredu | Wedi cau]

## Disgrifiad o'r newid

<!-- Beth sy'n newid a pham. Cyfeiriwch at y tocyn neu'r gofyniad. -->

## Systemau a chydrannau yr effeithir arnynt

<!-- Gwasanaethau, data, amgylcheddau, a defnyddwyr yr effeithir
     arnynt. -->

## Cyfiawnhad ac effaith fusnes

<!-- Y rheswm dros y newid a'r effaith o beidio â'i wneud. -->

## Asesiad risg

- Lefel risg: [Isel | Canolig | Uchel]
- Effaith bosibl os yw'r newid yn methu: [disgrifiad]
- Effaith ar ddiogelwch, preifatrwydd, neu gydymffurfiaeth: [disgrifiad]

## Cynllun gweithredu

<!-- Camau wedi'u trefnu, partïon cyfrifol, ac amseriad. -->

## Cynllun profi a dilysu

<!-- Sut y bydd llwyddiant yn cael ei wirio cyn ac ar ôl y newid. -->

## Cynllun tynnu-nôl / dadwneud

<!-- Sut i wrthdroi'r newid os yw'n methu, a'r amser adfer. -->

## Amserlen

- Ffenestr arfaethedig: [dechrau a diwedd, gyda chylchfa amser]
- Amser segur disgwyliedig: [hyd neu ddim]

## Cymeradwyaethau

| Rôl | Enw | Penderfyniad | Dyddiad |
|------|------|----------|------|
| Perchennog newid | [enw] | [cymeradwyo/gwrthod] | [dyddiad] |
| Adolygydd technegol | [enw] | [cymeradwyo/gwrthod] | [dyddiad] |
| Bwrdd cynghori newid | [enw] | [cymeradwyo/gwrthod] | [dyddiad] |

## Adolygiad ôl-weithredu

<!-- Canlyniad, materion a wynebwyd, ac a oedd angen tynnu-nôl. -->
```

## Amlinelliad Asesiad Effaith Diogelu Data (DPIA)

```markdown
# Asesiad Effaith Diogelu Data: [Enw'r gweithgaredd prosesu]

- Aseswr: [enw]
- Dyddiad: [YYYY-MM-DD]
- Adolygwyr: [Swyddog Diogelu Data / cyswllt preifatrwydd]
- Statws: [Drafft | Wedi'i adolygu | Cymeradwywyd]

## 1. Disgrifiad o'r prosesu

<!-- Pa ddata personol sy'n cael ei brosesu, sut, gan bwy, ac at ba
     bwrpas. Cynhwyswch lifau data o gasglu hyd at ddileu. -->

- Gwrthrychau data: [pwy mae'r data amdanynt]
- Categorïau data: [mathau o ddata personol, nodwch unrhyw gategorïau arbennig]
- Pwrpasau: [pam mae'r data'n cael ei brosesu]
- Derbynwyr a phroseswyr: [pwy sy'n derbyn neu'n trin y data]
- Cyfnod cadw: [pa mor hir y cedwir data a'r dull dileu]
- Trosglwyddiadau rhyngwladol: [cyrchfannau a mecanwaith trosglwyddo]

## 2. Angenrheidrwydd a chymesuredd

<!-- A yw'r prosesu'n angenrheidiol ar gyfer y pwrpas? Ai dyma'r opsiwn
     lleiaf ymwthiol? Beth yw'r sail neu'r awdurdod cyfreithlon? -->

- Sail / awdurdod cyfreithlon: [sail ar gyfer pob pwrpas]
- Lleihau data: [pam mae pob maes yn angenrheidiol]
- Cywirdeb a chyfiawnhad cadw: [nodiadau]
- Sut y cefnogir hawliau gwrthrych data: [mynediad, dileu, ac ati]

## 3. Ymgynghoriad

<!-- Rhanddeiliaid, a lle bo'n berthnasol wrthrychau data, wedi'u
     hymgynghori. -->

## 4. Risgiau i unigolion

<!-- Nodwch risgiau preifatrwydd a rhowch sgôr i bob un. -->

| Risg i unigolion | Tebygolrwydd | Difrifoldeb | Cyffredinol |
|---------------------|-----------|----------|---------|
| [e.e. mynediad heb awdurdod at ddata sensitif] | [I/C/U] | [I/C/U] | [sgôr] |

## 5. Mesurau i leihau risg

<!-- Ar gyfer pob risg, y lliniariad a'r risg weddilliol ar ei ôl. -->

| Risg | Mesur | Risg weddilliol | Derbyniwyd gan |
|------|---------|---------------|-------------|
| [risg] | [rheolaeth] | [I/C/U] | [enw] |

## 6. Canlyniad a chymeradwyaeth derfynol

- Risg weddilliol yn dderbyniol: [Ydy | Nac ydy]
- Mesurau wedi'u cymeradwyo gan: [enw, rôl]
- Angen ymgynghori ag awdurdod goruchwylio: [Ydy | Nac ydy]
- Dyddiad adolygu: [YYYY-MM-DD]
```
