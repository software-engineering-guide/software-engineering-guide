# 11.3 Theori ciwio

## Trosolwg a chymhelliant

Mae [theori ciwio](https://en.wikipedia.org/wiki/Queueing_theory) yn astudiaeth fathemategol o linellau aros. Mewn peirianneg meddalwedd, dyma'r theori dawel y tu ôl i swm enfawr o ymarfer. Ymatebolrwydd gwasanaeth cwsmeriaid, cynllunio [kanban](https://en.wikipedia.org/wiki/Kanban_%28development%29) (dull tynnu sy'n cyfyngu [gwaith ar y gweill](https://en.wikipedia.org/wiki/Work_in_process) i wella llif), ciwiau negeseuon rhyng-broses, piblinellau defnyddio parhaus: mae'r rhain i gyd yn giwiau, ac maent i gyd yn ufuddhau i'r un deddfau. Mae deall y deddfau hynny'n galluogi tîm i resymu am [amseroedd arwain](https://en.wikipedia.org/wiki/Lead_time), [drwybwn](https://en.wikipedia.org/wiki/Throughput), capasiti, a gwir gost rhedeg systemau ger eu terfynau, yn lle cael eu synnu ganddynt mewn cynhyrchiad. Mae'r bennod hon yn eistedd yn rhan Llif oherwydd bod theori ciwio'n sylfaen ffurfiol llif: mae'n esbonio *pam* mae gwaith yn aros, a beth sy'n lleihau'r aros mewn gwirionedd.

Dyma'r cymhelliant: mae greddf ynghylch ciwiau'n anghywir yn gyson, ac yn anghywir mewn ffyrdd drud. Mae pobl yn tybio bod gweinydd sy'n rhedeg ar 90% defnydd yn "10% oddi wrth drafferth," pan mewn gwirionedd mae amseroedd aros yn ffrwydro'n an-linol wrth i ddefnydd agosáu at 100%. Maent yn tybio bod ychwanegu gwaith ar y gweill (WIP) yn cyflymu cyflenwi, pan mae'n hirhau amseroedd arwain. Maent yn cynllunio capasiti o amgylch cyfartaleddau, yna'n cael eu dinistrio gan amrywioldeb. Mae ychydig o theori ciwio'n disodli'r greddfau costus hyn â nifer bach o gysylltiadau cadarn, yn bwysicaf oll [Deddf Little](https://en.wikipedia.org/wiki/Little%27s_law), sy'n dal ar draws ciwiau cwsmeriaid, byrddau tasgau, a phiblinellau CI/CD fel ei gilydd.

I dimau mawr, mentrau, a llywodraethau, mae theori ciwio'n iaith a rennir ar gyfer capasiti a llif, un sy'n cysylltu rolau sydd fel arall yn siarad heibio i'w gilydd. Mae rheolwyr cynnyrch yn poeni am amser arwain o syniad i gwsmer. Mae SREs yn poeni am ddefnydd gweinydd ac oedi. Mae timau DevOps yn poeni am amlder defnyddio. Mae arweinwyr cymorth yn poeni am amseroedd ymateb. Mae'r rhain i gyd yn fetrigau ciw, ac mae eu mynegi mewn un fframwaith (cyfradd cyrraedd, cyfradd gwasanaeth, defnydd, amser aros) yn galluogi sefydliad i gynllunio capasiti, gosod SLOs realistig (amcanion lefel gwasanaeth), a chyfiawnhau buddsoddiad â mathemateg yn hytrach nag anecdot.

## Egwyddorion allweddol

- **Mae popeth sydd ag aros yn giw:** tocynnau, tasgau, negeseuon, a defnyddiadau yn gynwysedig.
- **Deddf Little yw'r angor:** eitemau yn y system = cyfradd cyrraedd × amser yn y system (κ = λτ).
- **Mae defnydd ac amser aros yn an-linol:** y 15% olaf o gapasiti yw'r drutaf.
- **Amrywioldeb yw gelyn llif:** mae cyfartaleddau'n cuddio'r boen; mae amrywiant yn creu ciwiau.
- **Mae lleihau gwaith ar y gweill yn lleihau amser arwain:** llif, nid prysurdeb, yw'r nod.
- **Mesurwch y llif cyfan:** cyrhaeddiadau, gwasanaeth, llwyddiannau, methiannau, hepgoriadau, ac aros.
- **Mae proses yn giw o giwiau:** modelwch gamau, yna optimeiddiwch yr un cyfyngol.

## Argymhellion

### Dysgu'r nodiant craidd a'i ddefnyddio'n gyson

Mae llond llaw o feintiau'n disgrifio unrhyw giw. Mae safoni arnynt (mae llythrennau Groeg yn arferol) yn dileu amwysedd ar draws timau:

- **λ (lambda), cyfradd cyrraedd:** pa mor gyflym mae eitemau newydd yn dod i mewn.
- **μ (mu), cyfradd gwasanaeth:** pa mor gyflym mae eitemau'n cael eu trin. Gan fod "cyfradd gwasanaeth" yn cael ei defnyddio'n amwys, mae'n aml yn werth hollti drwybwn yn benodol i **gyfradd gyfan (χ)**, **cyfradd lwyddiant (α)**, **cyfradd fethiant (β)**, a **chyfradd hepgor (σ)**, lle χ = α + β + σ.
- **ρ (rho), defnydd / dwyster traffig = λ / μ:** y crynodeb pwysicaf un. Mae ρ < 1 yn golygu bod y ciw'n draenio; mae ρ ≥ 1 yn golygu ei fod yn tyfu heb derfyn.
- **Amseroedd:** amser arwain (τ, dechrau i orffen), amser gwaith (φ, prosesu gwirioneddol), amser aros (ω, yn hongian), ac amser cam (θ, rhwng cwblhau).
- **ε (epsilon), cymhareb gwall:** methiannau ÷ cyfanswm.

Mae enwi methiannau a *hepgoriadau* yn benodol yn bwysig mewn meddalwedd: mae eitem sy'n cael ei gadael (cwsmer sy'n rhoi'r gorau iddi, cart wedi'i adael, tocyn gwaith a wrthodwyd) yn gadael y ciw heb gael ei wasanaethu, ac mae esgus ei fod wedi'i "wasanaethu" yn llygru eich metrigau. Traciwch **wrthod ymuno** (penderfynu peidio ag ymuno), **ildio** (rhoi'r gorau iddi ar ôl aros), a **jocio** (newid ciwiau) fel canlyniadau dosbarth cyntaf.

### Angori cynllunio ar Ddeddf Little

Mae Deddf Little yn datgan bod nifer cyfartalog hirdymor yr eitemau mewn system sefydlog yn hafal i'r gyfradd cyrraedd gyfartalog wedi'i lluosi â'r amser cyfartalog y mae pob eitem yn ei dreulio yn y system: **κ = λ τ** (yn glasurol L = λW). Mae'n rhyfeddol o gyffredinol (nid oes angen unrhyw dybiaeth am ddosraniad cyrraedd na threfn gwasanaeth), sy'n ei gwneud yn geffyl gwaith cynllunio llif. Wedi'i had-drefnu, mae'n dweud wrthych fod **amser arwain = gwaith ar y gweill ÷ drwybwn**. Dyna sylfaen fathemategol kanban a lean: os ydych am amseroedd arwain byrrach ac na allwch godi drwybwn, rhaid i chi ostwng WIP. Mae hefyd yn rhoi gwiriadau synnwyr cyffredin cyflym. Os oes 40 tocyn ar agor a'ch bod yn cau 8 y dydd, mae'r tocyn cyfartalog yn cymryd tua 5 diwrnod, ni waeth pa mor brysur y mae unrhyw un yn teimlo. Ei un gofyniad yw *sefydlogrwydd*: rhaid i gyrhaeddiadau beidio â rhagori ar ymadawiadau'n barhaus (ρ < 1), neu bydd y ciw, a thybiaethau'r ddeddf, yn chwalu.

### Parchu an-linoledd defnydd

Y wers weithredol bwysicaf o theori ciwio yw bod amser ymateb yn codi'n serth, nid yn raddol, wrth i ddefnydd agosáu at 100%. Mae *Seven insights into queueing theory* gan Bob Wescott yn dal y canlyniadau ymarferol yn fyw:

1. Po arafaf y ganolfan wasanaeth, yr isaf y defnydd brig y dylech gynllunio ar ei gyfer.
2. Mae'n anodd iawn defnyddio'r 15% olaf o unrhyw beth.
3. Po agosaf y rhedwch at yr ymyl, yr uchaf yw pris bod yn anghywir.
4. Mae twf amser ymateb wedi'i gyfyngu gan faint o eitemau all aros.
5. Cyfartaleddau yw'r rhain, nid uchafswm: cynlluniwch ar gyfer y gynffon.
6. Byddwch yn wyliadwrus o effaith gwadu dynol ar draws sawl canolfan wasanaeth.
7. Dangoswch welliannau bach yn eu goleuni gorau.

Yr oblygiad dylunio: **darparwch le pen yn fwriadol.** Nid gwastraff yw targedu 70–80% o ddefnydd ar gyfer systemau sy'n sensitif i oedi; mae'n prynu amser ymateb rhagweladwy. Mae hyn yn llywio cynllunio capasiti a SLOs yn uniongyrchol (penodau 3.5 a 9.1).

### Modelu prosesau fel ciw o giwiau

Mae gwaith gwirioneddol yn llifo drwy gamau, ac mae proses aml-gam yn syml yn giw y mae ei eitemau eu hunain wedi'u ciwio ym mhob cam. Modelwch ef fel hynny: cyfradd cyrraedd y broses yw cyfradd cyrraedd cam 1; cyfradd lwyddiant y broses yw cyfradd lwyddiant y cam olaf; cyfrifon gwall a hepgor y broses yw'r symiau ar draws camau. Mae dwy siâp cyffredin yn ailddigwydd:

- **Twndisau**, lle mae cyfrifon eitemau'n crebachu bob cam (recriwtio: estyn allan → cyfweliad → cynnig; prynu: pori → cart → talu; cyflenwi: integreiddio → UAT → cynhyrchiad). Optimeiddiwch y cam sy'n bwysicaf: uchafswmwch gyrhaeddiadau brig-twndis, lleihewch hepgoriadau canol-twndis (cadw cartiau), neu leihewch wallau cam-terfynol (defnyddio cynhyrchiad gwael).
- Llifoedd darganfod-a-chyflenwi **diemwnt-dwbl** (darganfod → diffinio → datblygu → cyflenwi), y mae rhan Llif y llyfr hwn yn eu trin yn uniongyrchol (pennod 11.1).

Canfod a rhyddhau'r **cam cyfyngol** (y gwddf potel) yw lle mae gwelliant llif yn talu ar ei ganfed; mae optimeiddio anghyfyngiadau ond yn symud y ciw.

### Cysylltu metrigau ciw â'r DPAau y mae timau eisoes yn eu defnyddio

Mae meintiau ciwio'n mapio'n lân i'r metrigau cyflenwi a dibynadwyedd mewn mannau eraill yn y llyfr hwn, sef yr hyn sy'n gwneud y theori'n ymarferol yn hytrach nag academaidd:

- **Amser arwain cyflenwi (Dτ)**, "cysyniad i gwsmer," yn fesur amser arwain (τ) a metrig DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) (pennod 11.2).
- **Amlder defnyddio (Dμ)** yn fesur cyfradd gwasanaeth.
- **Cyfradd fethiant newid (Dε)** yn gymhareb gwall.
- **Amser i adfer (Rτ)** yn amser arwain adfer, h.y. MTTR (pennod 9.3).

Gwahaniaethwch rhwng y sawl **MTTR** (amser cymedrig i *ymateb*, *drwsio*, *adfer*, a *datrys*) gan eu bod yn mesur segmentau gwahanol o giw digwyddiadau ac fe'u cymysgir yn rheolaidd. Mae seilio SLIs/SLOs/SLAs (pennod 9.1) mewn termau ciw yn cadw targedau'n onest ac yn gymharadwy.

## Cyfaddawdau: manteision ac anfanteision

| Penderfyniad | Manteision | Anfanteision |
|---|---|---|
| **Rhedeg systemau ar ddefnydd uchel** | Cost caledwedd/cost fesul uned is | Ffrwydradau oedi an-linol; bregus i frigau |
| **Darparu lle pen hael** | Oedi rhagweladwy; gwydn i amrywiant | Cost cyflwr-sefydlog uwch; edrych yn "danddefnyddiedig" |
| **Cyfyngu WIP (kanban)** | Amseroedd arwain byrrach; llai o newid cyd-destun | Yn teimlo'n arafach; angen disgyblaeth i ddal y terfyn |
| **Modelu ciw ffurfiol** | Penderfyniadau capasiti wedi'u meintioli; llai o synau | Cromlin ddysgu; mae modelau'n symleiddio realiti anniben |
| **Rheolau bawd yn unig** | Cyflym, dim mathemateg | Anghywir yn union lle mae'n ddrutaf (ger capasiti) |

Y cyfaddawd sy'n ailddigwydd yw effeithlonrwydd yn erbyn rhagweladwyedd: mae gwthio defnydd i fyny'n arbed arian nes yn sydyn nad yw'n gwneud hynny, ac ar y pwynt hwnnw mae costau oedi, methiant, a diffodd tanau'n gorbwyso'r arbedion. Cyfraniad theori ciwio yw dweud wrthych ble mae'r clogwyn hwnnw fel bod y cyfaddawd yn ddewis, nid yn ddamwain.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Beth yw eich targed defnydd penodol ar gyfer pob system sy'n sensitif i oedi, a phwy a'i cymeradwyodd?** Mae lle pen yn bryniant bwriadol o oedi rhagweladwy, felly dylai fod yn bolisi datganedig, nid damwain o ba lwyth bynnag a ddigwyddodd gyrraedd. Gan fod amser ymateb yn codi'n an-linol, gall rhedeg ar 85% olygu oedi cynffon uwch yn barod, ac eto mae cyllid yn gweld lle pen fel gwastraff ac yn gwthio defnydd i fyny. Dewch â'r rhifau: defnydd cyfredol, y gromlin oedi a fesurwyd, a chost eich digwyddiad oedi diwethaf, yna dangoswch ble mae'r clogwyn ar gyfer pob gwasanaeth. Ar gyfer systemau menter a llywodraethol â brigau tymhorol (tymor cyflwyno, ffenestri cofrestru), gosodwch y targed oddi ar y clogwyn ar gyfer y brig, nid y cyfartaledd. Os nad oes neb yn berchen ar y targed defnydd, bydd digwyddiadau oedi'n parhau i ymddangos "o unman."

2. **Ble yn eich systemau mae ciw heb ei gyfyngu, heb ôl-bwysedd i ollwng llwyth pan gaiff ei orlethu?** Nid yw ciw heb ei gyfyngu'n methu'n osgeiddig; mae'n dirywio i mewn i gwymp, gan fod cyrhaeddiadau'n rhagori ar ymadawiadau'n barhaus (rho >= 1) yn golygu bod y ciw'n tyfu heb derfyn. Cymerwch restr eiddo o'ch ciwiau negeseuon, pyllau edau, a byfferau ceisiadau, a gofynnwch beth sy'n digwydd ym mhob un pan fydd cyfradd cyrraedd yn rhagori ar gyfradd gwasanaeth: a yw'n gollwng llwyth, yn cymhwyso ôl-bwysedd, neu'n cwympo? Mae hyn yn bwysig yn ddifrifol ar raddfa menter, lle gall un llifeiriant dirlawn i lawr yr afon gascadio ar draws gwasanaethau. Dewch â chanlyniad prawf llwyth neu ddigwyddiad blaenorol lle bagiodd ciw i fyny, a gwiriwch a wrthododd y system waith gormodol neu a geisiodd ddal y cyfan. Yr ateb yw ciwiau wedi'u cyfyngu ag ôl-bwysedd penodol a therfynau amser wedi'u tarddu o Ddeddf Little, fel bod gorlwyth yn gollwng yn hytrach na dymchwel.

3. **A ydych yn modelu eich llif syniad-i-gynhyrchiad fel ciw o giwiau, ac a yw eich gwelliannau wedi'u hanelu at y gwir gyfyngiad?** Mae proses aml-gam yn giw y mae ei eitemau wedi'u ciwio ym mhob cam, ac mae optimeiddio unrhyw beth heblaw'r cam cyfyngol ond yn symud y ciw. Mapiwch eich twndis cyflenwi (integreiddio i UAT i gynhyrchiad, neu ddarganfod i ddiffinio i ddatblygu i gyflenwi) a mesurwch gyfraddau cyrraedd, gwasanaeth, aros, a hepgor ym mhob cam i ganfod lle mae gwaith yn pentyrru go iawn. Mae timau'n aml yn optimeiddio'r cam y maent yn ei ddeall orau yn hytrach na'r gwddf potel, sy'n treulio ymdrech ac yn symud dim byd. Dewch â data amser-aros fesul cam, nid teimlad, gan mai cyflwr aros (adolygiad, cymeradwyaeth, argaeledd amgylchedd) yw'r gwddf potel yn aml yn hytrach na chyflwr gwaith. Unwaith y byddwch yn gwybod y cyfyngiad, anelwch yno a gadewch yr anghyfyngiadau ar eu pen eu hunain.

4. **A ydych yn defnyddio Deddf Little i osod terfynau WIP, ynteu ydych chi'n ychwanegu capasiti i wella amseroedd arwain na fyddai ond mwy o ddisgyblaeth yn eu trwsio?** Mae Deddf Little yn dweud bod amser arwain yn hafal i waith ar y gweill wedi'i rannu â drwybwn, felly os na allwch godi drwybwn, yr unig lifer sy'n weddill ar gyfer amseroedd arwain byrrach yw gostwng WIP, nad yw'n costio dim ond hunanataliaeth. Mae'r tyniad cystadleuol yn wirioneddol: mae cyfyngu gwaith ar y gweill yn teimlo'n arafach ac yn segur, a byddai rheolwyr o dan bwysau'n well ganddynt gyflogi neu brynu caledwedd na dweud wrth dimau i ddechrau llai a gorffen mwy. Dewch â'r rhifau caled, eitemau agored cyfredol a chyfradd gwblhau fesul cam, a chyfrifwch yr amser arwain cyfartalog ymhlyg, yna cymharwch ef â'r hyn y mae pobl yn credu ydyw; mae'r bwlch fel arfer yn fawr ac yn chwithig. Mewn menter neu asiantaeth fawr, dylid profi cais recriwtio neu gaffael a gyfiawnheir fel ateb amser arwain yn erbyn yr arithmeteg hon yn gyntaf, gan y gall cynnydd mewn niferoedd staff sy'n codi WIP hirhoi'r union amseroedd arwain roedd i fod i'w byrhau.

5. **A ydych yn cynllunio capasiti o amgylch cyfartaleddau, ynteu a ydych wedi meintioli'r amrywioldeb sy'n creu eich ciwiau go iawn?** Mae ciwiau'n ffurfio o amrywiant, nid o'r cymedr, felly gall dwy system â llwyth cyfartalog union yr un fath ymddwyn yn gwbl wahanol os oes gan un ohonynt gyrhaeddiadau byrstiog neu amseroedd gwasanaeth cynffon-hir. Y tyndra yw bod cyfartaleddau'n hawdd eu casglu ac yn galonogol i'w hadrodd, tra bo'r amrywiant a'r gynffon yn anos eu mesur ac yn amhoblogaidd mewn diweddariad statws. Dewch â'r dosraniad, nid y cymedr: byrstiadwyedd cyrraedd, amseroedd gwasanaeth ac aros y 95fed a'r 99fed canradd, a meintiau'r bathau sy'n crynhoi gwaith i frigau. Ar gyfer systemau menter a llywodraethol â chynyddiadau rhagweladwy (tymor cyflwyno, rhediadau cyflogres, ffenestri cofrestru, llwythi diwedd-chwarter), cynlluniwch y byffer a'r targed defnydd oddi ar amrywiant cyfnod-brig, gan y bydd dyluniad wedi'i feintio i'r cyfartaledd blynyddol yn methu yn union pan fydd y cyhoedd yn gwylio.

6. **Pa rai o'ch ciwiau sy'n cyfrif gadawiadau a gwrthodiadau'n dawel fel pe bai'r gwaith wedi'i wasanaethu, a pha alw heb ei ddiwallu y mae hynny'n ei guddio?** Mae eitem sy'n gwrthod ymuno, yn ildio, neu'n cael ei gwrthod yn gadael y ciw heb gael ei thrin, ac mae ei chofnodi fel "wedi'i wasanaethu" yn llygru eich drwybwn, eich cymhareb gwall, a'ch cynllun capasiti ar unwaith. Yr ystyriaeth gystadleuol yw bod "galwadau a atebwyd" neu "docynnau a gaewyd" yn edrych yn well ar ddangosfwrdd na "galwyr a roddodd y gorau iddi," felly'r rhif gonest yw'r un nad oes neb yn gwirfoddoli ei ddatgelu. Dewch â'r gyfradd hepgor (σ), cyfrifon gwrthod ymuno ac ildio, a'r gwahaniaeth rhwng llwyth a gynigiwyd a llwyth a wasanaethwyd, fel bod y galw gwirioneddol yn dod yn weladwy. Mae hyn yn bwysig yn ddirfawr mewn cyflenwi gwasanaeth llywodraethol, lle mae dinasyddion sy'n gadael ciw ffôn neu gais budd-daliadau yn ymrwymiadau heb eu diwallu yn hytrach nag achosion wedi'u datrys, ac mae eu hadrodd fel rhai a drinnir yn camddatgan perfformiad ac yn tanddatgan y capasiti y mae'r cyhoedd yn ei haeddu.

## Lens sector

**Cwmni newydd.** Nid oes gennych amser ar gyfer modelu ciw ffurfiol na'i angen. Estynnwch am y ddwy fuddugoliaeth rataf yn gyntaf: cymhwyswch Ddeddf Little i'ch ôl-restr i weld y gwir amser arwain y mae eich WIP yn ei awgrymu, a gwyliwch eich bwrdd kanban am y cam lle mae gwaith yn pentyrru cyn i chi gyflogi yn erbyn gwddf potel na all fodoli. Cadwch ddefnydd oddi ar y clogwyn ar unrhyw lwybr sy'n sensitif i oedi drwy adael lle pen yn hytrach na'i diwnio, gan fod terfyn gwasanaeth yn ystod brig twf yn costio llawer mwy na thipyn o gapasiti segur.

**Busnes bach.** Heb arbenigwr ciwio ar y staff, prynwch y metrigau yn hytrach na chodi'r modelau. Dewiswch ddesg gymorth, brocer negeseuon, neu blatfform cynnal sydd eisoes yn adrodd cyfradd cyrraedd, amser aros, a gadael, a darllenwch y rhifau hynny yn lle eu tarddu eich hun. Fframiwch y penderfyniad fel gwylio am ddau symptom: aros sy'n dringo'n an-linol wrth i chi fynd yn brysurach, a chwsmeriaid sy'n rhoi'r gorau iddi cyn cael eu gwasanaethu, gan mai cwsmer a gollwyd yw'r gost ciw sy'n brifo busnes bach fwyaf.

**Menter.** Y gwaith yw gwneud meddwl ciw yn ddisgyblaeth a rennir ar draws llawer o dimau: un nodiant y cytunwyd arno (λ, μ, ρ, amser arwain), polisïau WIP a lle-pen-defnydd cyson, a safonau ôl-bwysedd fel na all llifeiriant dirlawn i lawr yr afon gascadio ar draws gwasanaethau. Gosodwch SLOs a chapasiti o ddadansoddiad ciwio yn hytrach na dyfalu, a rheolwch eich ciwiau fel portffolio â llinellau sylfaen ac adolygiadau fel na fydd unrhyw un tîm yn rhedeg yn boeth ar ei ben ei hun. Pobwch y dadansoddiad i mewn i lywodraethu capasiti ac archwilio, fel bod targed lle pen yn benderfyniad dogfennedig y mae rhywun yn berchen arno.

**Llywodraeth.** Mae caffael, tryloywder, ac atebolrwydd cyhoeddus yn llunio pob dewis capasiti. Meintiwch ganolfannau cyswllt a systemau sy'n wynebu dinasyddion oddi ar amrywiant cyfnod-brig (tymor cyflwyno, ffenestri cofrestru), nid y cyfartaledd blynyddol, a staffiwch i gadw defnydd oddi ar y clogwyn pan fydd galw'n cynyddu. Traciwch wrthod ymuno ac ildio fel galw cyhoeddus heb ei ddiwallu yn hytrach na'i guddio y tu mewn i "alwadau a atebwyd," a chyfiawnhewch wariant capasiti ag amcangyfrifon Deddf Little o amser aros, sy'n rhoi achos amddiffynadwy, wedi'i gefnogi'n fathemategol i archwilwyr a swyddogion etholedig yn hytrach nag anecdot.

## Enghreifftiau

**Cwmni newydd.** Mae tîm SaaS pum person sy'n boddi mewn ôl-restr gymorth yn tybio bod angen iddynt gyflogi asiant arall. Cyn gwario'r arian, maent yn cymhwyso Deddf Little: mae 60 tocyn agored a 12 wedi'u cau y dydd yn golygu bod tocyn cyfartalog yn aros tua 5 diwrnod, sy'n cyfateb i'r negeseuon e-bost dig. Wrth wylio eu bwrdd kanban, maent yn sylwi bod tocynnau'n pentyrru wrth aros am beirianneg, nid am gymorth, felly maent yn cyfyngu gwaith ar y gweill ac yn llwybro adroddiadau bygiau'n syth i mewn i'r sbrint yn lle gadael iddynt giwio. Mae amser arwain yn gostwng i lai na deuddydd heb gyflogaeth newydd, ac maent yn defnyddio'r gyllideb rydd ar y gwddf potel go iawn yn lle hynny.

**Menter.** Mae platfform taliadau sy'n meintio'i wasanaeth awdurdodi'n mesur λ ≈ 850 cais/eiliad a μ ≈ 200/eiliad fesul nod. Yn naïf mae hynny'n ~5 nod (ρ = 0.85), ond gan wybod bod ρ = 0.85 eisoes yn golygu oedi cynffon uwch yn siarp, mae'r tîm yn darparu i ρ ≈ 0.65 ac yn defnyddio Deddf Little i ragfynegi cyfrifon ceisiadau ar-hediad a gosod dyfnderoedd ciw a therfynau amser. Mae digwyddiadau tymor-brig a arferai ymddangos "o unman" yn diflannu, gan nad oedd y tîm bellach yn gweithredu ar ran serth y gromlin.

**Llywodraeth.** Mae canolfan gyswllt asiantaeth dreth yn modelu cymorth tymor-cyflwyno fel ciw: brigau cyrraedd (λ), capasiti asiant (μ), ac, yn hollbwysig, **cyfradd hepgor (σ)** dinasyddion sy'n gadael ar ôl daliadau hir. Trwy dracio gwrthod ymuno ac ildio yn hytrach na dim ond "galwadau a atebwyd," mae arweinyddiaeth yn gweld y galw gwirioneddol heb ei ddiwallu, yn staffio i gadw defnydd oddi ar y clogwyn yn ystod brigau, ac yn cyfiawnhau'r capasiti ychwanegol ag amcangyfrifon Deddf Little o amser aros, achos amddiffynadwy, wedi'i gefnogi'n fathemategol ar gyfer gwariant cyhoeddus yn hytrach nag un anecdotaidd.

## Achos busnes: cymhellion, ROI, a TCO

Mae theori ciwio'n talu ar ei ganfed drwy atal dau gamgymeriad drud: **gorddarpariaeth** (talu am gapasiti segur nad oedd ei angen arnoch) a, llawer mwy niweidiol, **tan-ddarpariaeth ger y clogwyn** (lle mae cynnydd bach mewn llwyth yn achosi oedi mawr, SLAs wedi'u torri, cwsmeriaid wedi'u colli, a gwariant brys). Gan fod cost rhedeg yn agos at 100% o ddefnydd yn an-linol, mae'r arbedion o "jyst ychwanegu ychydig mwy o lwyth" yn fach a'r anfantais yn drychinebus, yn union yr anghymesuredd y mae ychydig o fathemateg yn ei droi'n benderfyniad bwriadol. Mesurir yr enillion mewn terfynau gwasanaeth a osgowyd, SLAs a fodlonwyd, cwsmeriaid a gadwyd a fyddai fel arall wedi gwrthod ymuno, a chylchdroeon galwad-ar-ddyletswydd tawelach.

O ran cyfanswm cost perchnogaeth, mae'r fframwaith yn rhad i'w fabwysiadu (gwybodaeth ydyw, nid offer) ac mae'n gwella bron pob penderfyniad capasiti, oedi, a llif y mae sefydliad mawr yn ei wneud dros oes system. Mae Deddf Little a therfynau WIP yn lleihau amseroedd arwain heb brynu dim byd (buddugoliaeth broses bur), tra bo disgyblaeth defnydd yn cyfnewid cost cyflwr-sefydlog cymedrol, rhagweladwy am ddileu methiannau drud, annisgwyl. I wneud yr achos i arweinyddiaeth, trosiwch ddigwyddiad oedi diweddar i mewn i'r gromlin ddefnydd a dangoswch sut y byddai targed lle pen wedi'i atal, a defnyddiwch Ddeddf Little i gysylltu gostyngiad WIP yn uniongyrchol â chyflenwi cyflymach.

## Gwrth-batrymau a pheryglon

- **Cynllunio capasiti o amgylch cyfartaleddau:** anwybyddu amrywiant, sef yr hyn sy'n creu ciwiau go iawn.
- **Rhedeg yn boeth:** targedu 90%+ o ddefnydd ar systemau sy'n sensitif i oedi a chael sioc gan oedi cynffon.
- **Cyfrif hepgoriadau fel gwasanaeth:** trin cwsmeriaid a adawyd neu docynnau a wrthodwyd fel rhai a drinnir, gan lygru metrigau.
- **Pentyrru WIP:** camgymryd prysurdeb am drwybwn a hirhoi amseroedd arwain.
- **Optimeiddio anwddf-potel:** gwella camau nad ydynt yn gyfyngiad a symud y ciw i rywle arall.
- **Drysu'r MTTRs:** adrodd "adferiad" tra'n mesur "trwsio," neu i'r gwrthwyneb.
- **Ciwiau heb eu cyfyngu:** dim ôl-bwysedd, fel bod system orlwythog yn dirywio i mewn i gwymp yn lle gollwng llwyth.
- **Cyfartaleddau fel uchafswm:** dylunio i'r cymedr a chael eich galw gan y gynffon.

## Model aeddfedrwydd

- **Lefel 1, Cychwyn:** Mae ciwiau (tocynnau, tasgau, negeseuon, defnyddiadau) heb eu rheoli ac yn adweithiol; dyfelir capasiti; mae defnydd yn rhedeg lle bynnag y mae llwyth yn glanio; mae problemau oedi'n synnu'r tîm ac yn cael eu diffodd fel tân wedi'r ffaith.
- **Lefel 2, Datblygu:** Mae ychydig o dimau'n casglu metrigau sylfaenol (drwybwn, aros cyfartalog) ond yn eu darllen fel cyfartaleddau ac yn eu cymhwyso'n anghyson; mae rhai grwpiau'n cyfyngu WIP neu'n gadael lle pen tra bo eraill yn rhedeg yn boeth; nid oes nodiant a rennir, felly nid yw'r arferion yn teithio ar draws timau.
- **Lefel 3, Safoni:** Mae nodiant cyffredin (λ, μ, ρ, amser arwain) wedi'i ddogfennu a'i orfodi ledled y sefydliad; gosodir terfynau WIP a thargedau lle-pen-defnydd yn fwriadol ar gyfer pob system sy'n sensitif i oedi; gwahaniaethir rhwng y sawl MTTR; ciwiau wedi'u cyfyngu ag ôl-bwysedd yw'r diofyn ar draws gwasanaethau.
- **Lefel 4, Rheoli:** Caiff y ciwiau eu mesur a'u rheoli yn erbyn llinellau sylfaen: caiff cyfradd cyrraedd, cyfradd gwasanaeth, defnydd, oedi cynffon (p95/p99), ac amser arwain eu tracio i dargedau ac SLOs diffiniedig; mae dyfnderoedd ciw, terfynau amser, a lle pen wedi'u tarddu o Ddeddf Little yn hytrach na'u dyfalu; cyfrifir gwrthod ymuno, ildio, a chyfradd hepgor fel bod llwyth a gynigiwyd yn cael ei wahaniaethu oddi wrth lwyth a wasanaethwyd; adolygir penderfyniadau capasiti ar y dystiolaeth hon, nid ar deimlad.
- **Lefel 5, Cerdorfa:** Modelir llif yn barhaus fel ciw o giwiau; adnabyddir a rhyddheir gyddfau potel fel ymarfer parhaus; mae capasiti, SLOs, ac ôl-bwysedd yn addasu i alw ac amrywiant sy'n newid; mae metrigau ciw'n clymu'n uniongyrchol â DORA a DPAau busnes, ac mae'r sefydliad yn ailgydbwyso capasiti ar draws y llif cyfan wrth i'r darlun llwyth a risg newid.

## Syniadau ar gyfer trafod

1. Ar ba ddefnydd y mae eich systemau sy'n sensitif i oedi'n rhedeg go iawn, a ble mae eu clogwyn?
2. Cymhwyswch Ddeddf Little i'ch ôl-restr gyfredol: pa amser arwain y mae eich WIP ÷ drwybwn yn ei awgrymu, ac a yw'n cyfateb i realiti?
3. Pa rai o'ch ciwiau sy'n cyfrif "hepgoriadau" (gadawiadau, gwrthodiadau) yn dawel fel pe baent wedi'u gwasanaethu?
4. Ble byddai gostwng WIP yn byrhau amser arwain yn rhatach nag ychwanegu capasiti?
5. Pa gam yn eich llif syniad-i-gynhyrchiad yw'r gwir wddf potel, ac a yw eich gwelliannau wedi'u hanelu yno?
6. A yw eich dangosfyrddau'n dangos cyfartaleddau lle mai'r gynffon sy'n eich brifo go iawn?

## Prif negeseuon

- Mae ciwiau cwsmeriaid, byrddau kanban, ciwiau negeseuon, a phiblinellau defnyddio i gyd yn giwiau a lywodraethir gan yr un deddfau.
- Mae **Deddf Little (κ = λτ)** yn angori cynllunio llif: amser arwain = WIP ÷ drwybwn.
- Mae defnydd ac amser aros yn **an-linol**: darparwch le pen; y 15% olaf yw'r drutaf.
- Traciwch y darlun llawn: cyrhaeddiadau, gwasanaeth, llwyddiannau, **methiannau a hepgoriadau**, ac aros; peidiwch â gadael i adael guddio.
- Modelwch brosesau fel **ciw o giwiau** a thrwsiwch y **gwddf potel**, nid y gwaith prysur.
- Mae metrigau ciw'n mapio'n uniongyrchol i fesurau **DORA/llif** a **SLI/SLO** (penodau 11.1, 11.2, 9.1), gan roi un iaith i'r sefydliad cyfan ar gyfer capasiti a llif.

## Cyfeiriadau a darllen pellach

- Bob Wescott, *Seven Insights into Queueing Theory* (a *The Every Computer Performance Book*).
- John D. C. Little, "A Proof for the Queuing Formula L = λW" (1961): Deddf Little.
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate*: metrigau DORA seiliedig ar lif sy'n cyd-fynd â DPAau ciw.
- Donald Reinertsen, *The Principles of Product Development Flow*: ciwiau, maint bathau, ac economeg WIP.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability*: Deddf Little wedi'i chymhwyso i kanban.
- Joel Parker Henderson, *Queueing Theory*: nodiant, DPAau, a chiw-o-giwiau (github.com/joelparkerhenderson/queueing-theory).
- Dan Slimmon, "The most important thing to understand about queues" (2016).
- Wikipedia: "Queueing theory," "M/M/1 queue," "Little's law," "Markov chain."
