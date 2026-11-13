# 4.8 Cryptograffeg a rheoli allweddi

## Trosolwg a chymhelliant

Mae bron pob system rydych chi'n ei hadeiladu eisoes yn dibynnu ar [gryptograffeg](https://en.wikipedia.org/wiki/Cryptography), sef y practis o ddiogelu gwybodaeth gan ddefnyddio technegau mathemategol fel mai dim ond y partïon a fwriadwyd all ei darllen neu ymddiried ynddi. Mae eich traffig gwe'n teithio ar sianeli wedi'u hamgryptio, mae eich cyfrineiriau wedi'u hasio, mae eich diweddariadau meddalwedd wedi'u llofnodi, ac mae data eich cwsmeriaid yn eistedd wedi'i amgryptio ar ddisg. Y newyddion da i'r rhan fwyaf o beirianwyr yw nad ydych yn cael eich gofyn i ddyfeisio dim o hyn. Nid y fathemateg yw'r rhan anodd. Defnyddio blociau adeiladu a wiriwyd yn gywir yw'r rhan anodd, ac yn anad dim, rheoli'r allweddi y mae'r blociau adeiladu hynny'n dibynnu arnynt.

Mae'r bennod hon wedi'i hysgrifennu ar gyfer peirianwyr nad ydynt yn gryptograffwyr, sef bron pob un ohonom. Mae angen digon o ddealltwriaeth arnoch i wneud dewisiadau doeth, i wybod beth mae pob teclyn yn ei warantu, ac i osgoi'r camgymeriadau sy'n troi algorithmau cryf yn gysur ffug. Mae pennod 4.3 (seilwaith a diogelwch cwmwl) yn crybwyll amgryptio a rheoli allweddi wrth fynd heibio; yma rydym yn mynd yn ddyfnach i mewn i beth i'w amgryptio, sut, a sut i redeg cylchred oes yr allwedd sy'n ei wneud yn wirioneddol.

I fentrau mawr, mae cryptograffeg yn lledaenu ar draws miloedd o wasanaethau, tystysgrifau, ac allweddi, a gall un dystysgrif ddiedig neu allwedd goll ddymchwel system dyngedfennol neu ollwng storfa ddata. I lywodraethau, mae cryptograffeg yn aml yn orfodol, wedi'i dilysu, a'i harchwilio, gyda rheolau dosbarthu data sy'n pennu'n union pa allweddi sy'n diogelu pa gyfrinachau a phwy sy'n cael eu dal. Yn y ddau leoliad, yr un yw'r methiant sy'n ailadrodd: algorithmau da wedi'u dinistrio gan reoli allweddi esgeulus.

## Egwyddorion allweddol

- **Peidiwch â chreu eich cryptograffeg eich hun.** Defnyddiwch lyfrgelloedd a wiriwyd yn eang a safon algorithmau. Mae cynlluniau newydd yn methu mewn ffyrdd na fydd ond arbenigwyr yn eu dal.
- **Mae algorithmau'n rhan hawdd; allweddi yw'r rhan anodd.** Cylchred oes allwedd yw lle mae'r rhan fwyaf o fethiannau byd go iawn yn byw.
- **Gwybyddwch beth mae pob elfen sylfaenol yn ei warantu.** Mae cyfrinachedd, cyfanrwydd, a dilysrwydd yn briodweddau gwahanol sy'n gofyn am declynnau gwahanol.
- **Amgryptiwch wrth gludo ac wrth orffwys yn ddiofyn.** Gwnewch ddiogelu'n safon, nid yn ddewis.
- **Gwahanwch gadwraeth allweddi oddi wrth fynediad data.** Ni ddylai pwy bynnag sy'n rheoli allwedd allu darllen y data y mae'n ei ddiogelu yn awtomatig.
- **Cynlluniwch ar gyfer newid.** Mae algorithmau'n gwanhau, allweddi'n gollwng, a safonau'n esblygu. Adeiladwch ar gyfer cylchdroi a mudo o'r diwrnod cyntaf.
- **Ffafriwch weithrediadau wedi'u dilysu lle mae'n bwysig.** Ar gyfer gwaith rheoledig a llywodraethol, dewiswch fodylau â dilysiad cydnabyddedig.

## Argymhellion

### Peidiwch â chreu eich cryptograffeg eich hun

Dyma'r rheol aur, ac mae'n werth ei nodi'n gyntaf. Peidiwch byth â dylunio eich algorithm amgryptio eich hun, dyfeisio eich protocol eich hun, na gweithredu elfen sylfaenol â llaw o bapur. Mae cryptograffeg sy'n gweithio'n edrych yn syml ac yn cuddio moddau methiant cynnil (sianeli ochr amseru, oraclau padio, hapusrwydd gwan) nad ydynt ond yn goroesi blynyddoedd o adolygiad arbenigol. Defnyddiwch lyfrgelloedd sefydledig fel modiwl cryptograffig safonol eich platfform neu lyfrgell uchel ei pharch, a defnyddiwch nhw ar y lefel uchaf o haniaeth sydd ar gael. Estynnwch am foddau amgryptio dilysedig a rhyngwynebau "hawdd" sy'n gwneud y dewis diogel yn ddiofyn, yn hytrach na chydosod darnau lefel-isel eich hun.

### Paru'r elfen sylfaenol â'r warant sydd ei hangen arnoch

Mae gwahanol declynnau'n rhoi gwahanol warantau, ac mae drysu rhyngddynt yn gamgymeriad cyffredin a pheryglus. Dysgwch y tair prif deulu.

- **Mae cryptograffeg [allwedd gymesur](https://en.wikipedia.org/wiki/Symmetric-key_algorithm)** yn defnyddio un allwedd gyfrinachol a rennir i amgryptio a datgryptio fel ei gilydd. Mae'n gyflym ac yn diogelu **cyfrinachedd**, ond rhaid i'r ddau barti eisoes rannu'r allwedd. AES yw'r ceffyl gwaith safonol.
- **Mae cryptograffeg [allwedd gyhoeddus](https://en.wikipedia.org/wiki/Public-key_cryptography)** yn defnyddio pâr allweddi wedi'u cysylltu'n fathemategol: allwedd gyhoeddus y gall unrhyw un ei dal ac allwedd breifat rydych yn ei chadw'n gyfrinachol. Mae'n datrys dosbarthu allweddi ac yn galluogi **llofnodion digidol**, sy'n profi **dilysrwydd** (pwy a'i hanfonodd) a **chyfanrwydd** (na chafodd ei newid).
- Mae [ffwythiant hasio cryptograffig](https://en.wikipedia.org/wiki/Cryptographic_hash_function) yn cynhyrchu ôl bys maint sefydlog o ddata ac yn darparu gwirio **cyfanrwydd**. Mae hasio'n unffordd ac nid yw'n amgryptio. Ar gyfer storio cyfrineiriau, defnyddiwch ffwythiant hasio cyfrinair araf, wedi'i heli, byth hasyn cyflym plaen (gweler pennod 4.2 ar ddiogelwch cymwysiadau).

Y wers ymarferol: mae amgryptio'n cuddio data ond nid yw'n profi pwy a'i hanfonodd, ac mae hasyn yn canfod ymyrryd ond nid yw'n cuddio dim byd. Mae'r rhan fwyaf o systemau go iawn yn eu cyfuno, sef yn union pam y dylech chi bwyso ar lyfrgelloedd sy'n bwndelu'r rhain yn gywir.

### Amgryptio wrth gludo gyda TLS cyfredol

Diogelwch pob naid rhwydwaith gyda [Diogelwch Haen Gludiant](https://en.wikipedia.org/wiki/Transport_Layer_Security) (TLS), y protocol sy'n diogelu data wrth iddo symud rhwng systemau. Mynnwch fersiynau TLS modern, analluogwch rai anghyfredol, dewiswch siwtiau seiffr cryf, a dilyswch dystysgrifau'n briodol yn hytrach nag analluogi gwiriadau er mwyn "gwneud iddo weithio." Amgryptiwch draffig gwasanaeth-i-wasanaeth mewnol hefyd, nid dim ond yr ymyl gyhoeddus, gan fod ystum dim-ymddiriedaeth yn tybio bod y rhwydwaith mewnol yn elyniaethus. Awtomeiddiwch gyhoeddi ac adnewyddu tystysgrifau fel bod TLS yn ddiofyn diymdrech ym mhobman.

### Amgryptio wrth orffwys gydag amgryptio amlen

Amgryptiwch ddata wedi'i storio'n ddiofyn: cronfeydd data, storio gwrthrychau, wrth gefn, a chofnodion. Y patrwm safonol yw **amgryptio amlen**, lle mae **allwedd amgryptio data (DEK)** yn amgryptio'r data gwirioneddol, ac mae **allwedd amgryptio allwedd (KEK)** a ddelir mewn gwasanaeth rheoli allweddi yn amgryptio'r DEK. Mae hyn yn caniatáu i chi gylchdroi'r brif allwedd heb ailamgryptio terabeitiau o ddata, ac mae'n cadw'r allwedd wraidd bwerus y tu mewn i ffin galedwyd. Storiwch ddim ond y DEK wedi'i lapio wrth ymyl y data, a'i ôl-gyrchu a'i ddadlapio adeg defnyddio.

### Rhedeg cylchred oes yr allwedd yn fwriadol

Cylchred oes allwedd yw'r rhan wirioneddol anodd o gryptograffeg, a lle mae'r rhan fwyaf o doriadau i mewn a therfynau gwasanaeth yn tarddu. Rheolwch bob cam yn fwriadol:

- **Cynhyrchu:** creu allweddi o ffynhonnell ar hap gref, ar gryfder priodol.
- **Dosbarthu:** cael allweddi i'r systemau sydd eu hangen heb eu datgelu mewn cod, ffeiliau ffurfweddu, neu sgwrs.
- **Cylchdroi:** amnewid allweddi ar amserlen, a gallu cylchdroi'n gyflym pan amheuir perygl.
- **Dirymu:** dirymu allwedd neu dystysgrif a beryglwyd yn gyflym, a sicrhau bod systemau'n parchu'r dirymiad.
- **Dinistrio:** ymddeol deunydd allwedd hen yn ddiogel fel na ellir ei adfer.

Defnyddiwch **wasanaeth rheoli allweddi (KMS)** i ganoli hyn, a defnyddiwch [fodiwl diogelwch caledwedd](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM), dyfais wrthsefyll ymyrraeth sy'n cynhyrchu ac yn gwarchod allweddi fel na fyddant byth yn gadael mewn testun plaen, ar gyfer eich allweddi sicrwydd uchaf. Gwahanwch pwy sy'n gallu rheoli allweddi oddi wrth bwy sy'n gallu darllen y data a ddiogelir, fel bod cadwraeth allweddi'n gorfodi gwahanu dyletswyddau. Mae hyn yn cysylltu'n uniongyrchol â rheolau dosbarthu a chadwraeth data ym mhennod 4.5 (preifatrwydd a diogelu data).

### Gwahaniaethu rhwng rheoli cyfrinachau a rheoli allweddi

Mae'r rhain yn gorgyffwrdd ond nid ydynt yr un peth. Mae **rheoli allweddi** yn llywodraethu allweddi cryptograffig a'u cylchred oes, fel arfer y tu mewn i KMS neu HSM sy'n cyflawni gweithrediadau cryptograffig ar eich rhan fel na fydd yr allwedd amrwd byth yn gadael. Mae **rheoli cyfrinachau** yn llywodraethu tystlythyrau cymwysiadau (cyfrineiriau cronfa ddata, tocynnau API, tystysgrifau) y mae angen i wasanaethau eu hôl-gyrchu a'u defnyddio mewn testun plaen, fel arfer o gladdgell cyfrinachau gyda mynediad byrhoedlog, wedi'i archwilio. Defnyddiwch KMS ar gyfer allweddi, rheolwr cyfrinachau ar gyfer tystlythyrau, a byth peidiwch â gludo'r naill na'r llall i mewn i god ffynhonnell neu ffeiliau amgylchedd sydd wedi'u gwirio i mewn i reolaeth fersiynau.

### Awtomeiddio PKI a chylchredau oes tystysgrifau

Mae **seilwaith allwedd gyhoeddus (PKI)** yn system o awdurdodau tystysgrifau, tystysgrifau, a chadwyni ymddiriedaeth sy'n clymu allweddi cyhoeddus wrth hunaniaethau. Ar raddfa, y risg PKI amlycaf yw'r diediad tystysgrif syfrdanol sy'n dymchwel gwasanaeth. Cynhaliwch restr eiddo o bob tystysgrif, monitrwch ddiediadau, ac awtomeiddiwch gyhoeddi ac adnewyddu fel nad oes rhaid i unrhyw ddyn gofio. Mae tystysgrifau byrhoedlog a adnewyddir yn awtomatig yn fwy diogel na rhai hirhoedlog a feithrinir â llaw, gan fod awtomeiddio'n dileu'r pwynt methiant sengl dynol. Mae protocolau safonol yma'n cefnogi rhyngweithredu ar draws gwerthwyr (pennod 3.8 ar ryngweithredu a safonau agored).

### Adeiladu ar gyfer heini cryptograffig a mudo ôl-cwantwm

Mae algorithmau'n gwanhau dros amser, a safonau'n symud. Mae **heini cryptograffig** yn golygu dylunio systemau fel y gallwch gyfnewid algorithmau a meintiau allweddi heb ailysgrifennu poenus: haniaethwch gryptograffeg y tu ôl i ryngwyneb bach, fersiynwch eich data wedi'i amgryptio fel eich bod yn gwybod pa algorithm a'i cynhyrchodd, a chadwch restr eiddo gryptograffig o beth rydych yn ei ddefnyddio a ble. Mae hyn yn bwysig nawr oherwydd [cryptograffeg ôl-cwantwm](https://en.wikipedia.org/wiki/Post-quantum_cryptography), y teulu newydd o algorithmau a ddyluniwyd i wrthsefyll cyfrifiaduron cwantwm y dyfodol. Gall gwrthwynebwyr gasglu data wedi'i amgryptio heddiw i'w ddatgryptio'n ddiweddarach, felly mae angen cynllun mudo ar gyfrinachau hirhoedlog. Nid oes angen i chi banicio, ond dylech wybod eich rhestr eiddo a bod yn barod i fabwysiadu'r algorithmau ôl-cwantwm safonedig wrth i blatfformau eu rhyddhau.

### Ffafrio gweithrediadau wedi'u dilysu lle bo angen

Ar gyfer systemau rheoledig a llywodraethol, nid yw defnyddio algorithm cryf yn ddigon; rhaid dilysu'r gweithrediad. **FIPS 140** (Federal Information Processing Standard 140) yw safon UDA ar gyfer dilysu modiwlau cryptograffig, ac mae llawer o gontractau'n mynnu cryptograffeg wedi'i dilysu gan FIPS. Gall gwaith llywodraethol hefyd ddilyn arweiniad cenedlaethol fel siwt Algorithm Diogelwch Cenedlaethol Masnachol (CNSA) yr NSA ar gyfer systemau dosbarthedig. Gwiriwch pa gyfundrefn sy'n berthnasol cyn i chi adeiladu, gan fod ôl-osod modylau wedi'u dilysu'n hwyr yn ddrud. Mae hyn yn cysylltu â thystiolaeth cydymffurfiaeth a llywodraethu (pennod 4.6).

## Cyfaddawdau: manteision ac anfanteision

| Penderfyniad | Manteision | Anfanteision |
|---|---|---|
| KMS a reolir gan ddarparwr | Hawdd, integredig, baich gweithredol isel | Y darparwr sy'n dal cadwraeth; llai o reolaeth uniongyrchol |
| Allweddi a reolir gan gwsmer / HSM | Cadwraeth lawn, yn bodloni mandadau llym | Gorbenion gweithredol, risg o golli allweddi |
| Tystysgrifau byrhoedlog awtomataidd | Dim diediadau syfrdanol, dirymu cyflym | Angen buddsoddiad awtomeiddio ymlaen llaw |
| Tystysgrifau hirhoedlog | Syml, llai o rannau symudol | Mae diediadau a reolir gan bobl yn achosi terfynau gwasanaeth |
| Amgryptio amlen | Cylchdroi allweddi rhad, yn diogelu'r brif allwedd | Mwy o rannau symudol i'w deall |
| Heini cryptograffig ymlaen llaw | Mudiadau rhad yn y dyfodol | Ymdrech haniaeth a dylunio ychwanegol nawr |
| Mabwysiadu ôl-cwantwm cynnar | Yn gwarchod cyfrinachau hirhoedlog | Offer anaeddfed, allweddi mwy, rhywfaint o risg |

Y tyndra canolog yw rheolaeth yn erbyn baich gweithredol. Mae dal eich allweddi eich hun mewn HSM yn rhoi cadwraeth uchafswm ac yn bodloni'r mandadau llymaf, ond mae'n mynnu arbenigedd ac yn creu risg drychinebus newydd: collwch yr allwedd a chollwch y data, yn anadferadwy. Mae gwasanaethau a reolir gan ddarparwr yn dileu'r baich hwnnw ond yn gosod cadwraeth gyda'r darparwr. Datryswch ef drwy haenu: defnyddiwch wasanaethau wedi'u rheoli â diofynion synhwyrol ar gyfer y rhan fwyaf o systemau, a chadwch allweddi a reolir gan gwsmer ac HSMs ar gyfer y data dosbarthiad uchaf lle mae'r rheolaeth ychwanegol yn werth y gost a'r risg.

## Cwestiynau i'w trafod gyda'ch tîm

1. **A oes gennych restr eiddo gyflawn o'ch allweddi, tystysgrifau, a'r algorithmau rydych yn dibynnu arnynt?** Ni allwch gylchdroi, mudo, nac archwilio'r hyn na allwch ei weld, ac mae'r rhan fwyaf o sefydliadau'n darganfod bod ganddynt lawer mwy o ddeunydd cryptograffig wedi'i wasgaru ar draws gwasanaethau nag y mae unrhyw un yn ei olrhain. Rhestr eiddo yw'r rhagofyniad ar gyfer pob penderfyniad diweddarach: mae monitro diediad tystysgrifau, cylchdroi allweddi, cwmpasu FIPS, a chynllunio ôl-cwantwm i gyd yn dibynnu arni. Dewch â rhestr o'ch tystysgrifau presennol a'u dyddiadau diedig, a gofynnwch pwy sy'n berchen ar bob un a beth sy'n torri pan fydd yn dod i ben. Ar gyfer stad fawr, yr ateb gonest fel arfer yw nad oes un ffynhonnell wirionedd yn bodoli, ac mae adeiladu un yn gam cyntaf o'r trosoledd mwyaf. Os na allwch restru eich cryptograffeg heddiw, mae heini a chylchdroi'n ddyheadau, nid yn alluoedd.

2. **A allwch chi gylchdroi neu ddirymu allwedd a beryglwyd yn gyflym, ac a ydych erioed wedi ei hymarfer?** Cylchdroi a dirymu yw'r rhannau o gylchred oes yr allwedd sydd ond yn bwysig o dan bwysau, ac mae timau'n aml yn darganfod yn ystod digwyddiad fod allwedd wedi'i chodio'n galed mewn dwsin o leoedd neu nad yw dirymu'n lledaenu go iawn. Penderfynwch eich amser targed i gylchdroi allwedd a dirymu tystysgrif, yna ymarferwch cyn bod ei angen arnoch. Dewch â stori eich datguddiad tystlythyr diwethaf a cherddwch drwy'r hyn oedd angen ar gyfer cylchdroi'n ymarferol. I systemau menter a llywodraethol, gall cylchdroi heb ei ymarfer olygu dewis rhwng datguddiad estynedig a therfyn gwasanaeth hunanachosedig. Os na phrofwyd cylchdroi erioed, tybiwch nad yw'n gweithio.

3. **Ble mae cadwraeth allweddi'n eistedd, ac a yw'n gorfodi gwahanu dyletswyddau?** Ni ddylai pwy bynnag all reoli allwedd a phwy bynnag all ddarllen y data y mae'n ei ddiogelu fod yr un person, gan fod cyfuno'r pwerau hynny'n trechu diben amgryptio wrth orffwys yn dawel. Mae'r dewis hwn hefyd yn llywio a ydych yn defnyddio allweddi a reolir gan ddarparwr, allweddi a reolir gan gwsmer, neu HSMs, pob un â rheolaeth wahanol a risg weithredol wahanol. Dewch â'ch polisïau allwedd presennol a gwiriwch a all unrhyw hunaniaeth sengl weinyddu allwedd a chael mynediad at y testun plaen y tu ôl iddi, sy'n fwlch tawel cyffredin. Ar gyfer data rheoledig a dosbarthedig, gall rheolau cadwraeth gael eu pennu gan ddosbarthiad data (pennod 4.5) a chan fandad. Os na chaiff cadwraeth a mynediad eu gwahanu, mae eich amgryptio'n eich diogelu llai nag y mae'r dangosfwrdd yn ei awgrymu.

4. **Sut y byddech chi'n adfer pe bai'r brif allwedd sy'n diogelu eich amgryptio amlen yn cael ei cholli neu ei dinistrio?** Mae allweddi a reolir gan gwsmer ac HSMs yn rhoi cadwraeth i chi, ond maent yn rhoi modd methiant trychinebus newydd i chi: collwch yr allwedd amgryptio allwedd a daw pob allwedd amgryptio data y mae'n ei lapio'n barhaol annarllenadwy, ynghyd â'r data y tu ôl iddynt. Pwyswch hyn yn erbyn y risg wrthgyferbyniol o wrth-gefn rhy eang sy'n ail-greu'n dawel yr union broblem gadwraeth roeddech yn ceisio'i datrys. Dewch â'ch trefniadau wrth-gefn a chadw mewn ymddiriedaeth allweddi presennol, radiws ffrwydrad pob prif allwedd, a thystiolaeth bod adferiad wedi'i berfformio go iawn yn hytrach na dim ond ei ddogfennu. Ar gyfer ystadau menter a llywodraethol, cysylltwch hyn â'ch rheolau dosbarthu data: mae'r allweddi mwyaf sensitif yn aml yn gwahardd copïau achlysurol, felly mae'n rhaid dylunio adferiad yn fwriadol, ei brofi ar amserlen, a'i gysoni ag unrhyw ofyniad rheoleiddiol i brofi bod deunydd allwedd wedi'i ymddeol wedi'i ddinistrio.

5. **Pa mor barod yw eich systemau ar gyfer mudo ôl-cwantwm, a pha gyfrinachau hirhoedlog y byddech chi'n eu mudo gyntaf?** Gall gwrthwynebwyr gasglu traffig ac archifau wedi'u hamgryptio heddiw a'u datgryptio pan fydd cyfrifiaduron cwantwm yn aeddfedu, felly mae unrhyw gyfrinach y mae'n rhaid iddi aros yn gyfrinachol am flynyddoedd eisoes wedi'i datgelu i ddyfodol na allwch ei weld. Y pwysau cystadleuol yw bod offer ôl-cwantwm yn dal i fod yn ifanc, mae'r allweddi'n fwy, ac mae symud yn rhy gynnar yn peryglu betio ar algorithm sy'n symud cyn iddo setlo. Dewch â'ch rhestr eiddo gryptograffig, rhestr o gyfrinachau wedi'u graddio yn ôl pa mor hir y mae'n rhaid iddynt aros yn gyfrinachol, ac asesiad gonest o a all eich pensaernïaeth gyfnewid algorithmau heb ailysgrifennu. Ar gyfer gwaith llywodraethol a rheoledig, mae cofnodion â mandadau cyfrinachedd aml-ddegawd yn gwneud hyn yn ddiriaethol yn hytrach na damcaniaethol, ac efallai y bydd caffael yn fuan yn mynnu cynllun mudo wedi'i ddogfennu a chefnogaeth i'r algorithmau ôl-cwantwm safonedig.

6. **Pan fo rheoleiddio'n mynnu cryptograffeg wedi'i dilysu, a wyddoch chi'n union pa fodylau sydd o fewn cwmpas ac a ydynt yn cymhwyso?** Nid yw defnyddio algorithm cryf yr un peth â defnyddio gweithrediad wedi'i ddilysu, ac mae timau'n aml yn darganfod yn hwyr nad yw llyfrgell, amser rhedeg iaith, neu wasanaeth cwmwl wedi'i gwmpasu gan y ffin FIPS 140 y mae contract yn ei fynnu. Y tyndra yw y gall modylau wedi'u dilysu fod ar ei hôl hi o gymharu â llyfrgelloedd cyfredol o ran nodweddion a chyflymder, felly mae eu dewis yn cyfyngu ar eich pentwr mewn ffyrdd sy'n bwysig ar gyfer peirianneg. Dewch â rhestr o'r modylau cryptograffig y mae pob system reoledig yn eu galw go iawn, y tystysgrifau dilysu sy'n eu cwmpasu, a'r mandad penodol (FIPS 140, CNSA, neu reol sector) sy'n berthnasol. Ar gyfer rhaglenni menter a llywodraethol, penderfynwch hyn cyn i chi adeiladu, gan fod ôl-osod modylau wedi'u dilysu ac ail-awdurdodi system wedi'r ffaith yn ddrud, yn araf, ac yn aml yn gorfodi ailddylunio'r union gydrannau roeddech yn credu oedd wedi'u gorffen.

## Lens sector

**Cwmni newydd.** Pwyswch yn llwyr ar ddiofynion a wiriwyd eich platfform a threuliwch ddim amser peirianneg ar gryptograffeg bwrpasol. Trowch ymlaen amgryptio wedi'i reoli wrth orffwys, terfynwch TLS gyda thystysgrifau a adnewyddir yn awtomatig, hasiwch gyfrineiriau gyda ffwythiant araf safonol, a chadwch gyfrinachau yn rheolwr cyfrinachau'r platfform yn hytrach na'r ystorfa. Eich un penderfyniad dylunio yw rhyngwyneb tenau o amgylch y llond llaw o feysydd rydych yn eu hamgryptio yn y cymhwysiad, fel nad yw symud oddi wrth allweddi a reolir gan ddarparwr yn y dyfodol yn ailysgrifennu.

**Busnes bach.** Nid oes gennych gryptograffydd a fawr o awydd gweithredu HSM, felly prynwch gadwraeth yn hytrach na'i hadeiladu: defnyddiwch y KMS a'r rheolwr cyfrinachau a reolir gan ddarparwr sy'n dod gyda'ch offer cwmwl neu SaaS. Fframiwch y gwaith fel hylendid, hynny yw, dim allweddi mewn cod, amgryptio wedi'i droi ymlaen ym mhobman yn ddiofyn, a diediadau tystysgrifau'n cael eu monitro fel nad oes dim yn dod i ben ar syrpreis. Cadwch allweddi a reolir gan gwsmer ar gyfer y data prin y mae contract neu reoleiddiwr yn wirioneddol yn eu mynnu ar eu cyfer.

**Menter.** Y broblem yw graddfa a chysondeb ar draws miloedd o wasanaethau, tystysgrifau, ac allweddi. Rhedwch KMS canolog gydag amgryptio amlen, awtomeiddiwch gylchred oes lawn y dystysgrif fel na chaiff unrhyw ddiediad ei feithrin â llaw, a chynhaliwch un rhestr eiddo gryptograffig sy'n bwydo cylchdroi, cwmpasu FIPS, a chynllunio ôl-cwantwm. Gwahanwch gadwraeth allweddi oddi wrth fynediad data fel rheolaeth ledled y sefydliad, a gwnewch amgryptio'n allu platfform y mae pob tîm yn ei etifeddu yn hytrach na thasg y mae pob tîm yn ei hailddyfeisio.

**Llywodraeth.** Mae caffael, dilysu, ac archwilio'n llunio pob dewis. Defnyddiwch fodylau wedi'u dilysu gan FIPS 140 a dilynwch arweiniad cenedlaethol fel CNSA ar gyfer systemau dosbarthedig, cysylltwch gadwraeth allweddi â dosbarthiad data fel bod yr allweddi mwyaf sensitif yn eistedd gyda phersonél wedi'u clirio o dan wahanu dyletswyddau llym, a chynhyrchwch dystiolaeth barhaus o gryptograffeg wedi'i dilysu ar gyfer awdurdodiad parhaus. Dogfennwch gynllun mudo ôl-cwantwm ar gyfer cofnodion y mae'n rhaid iddynt aros yn gyfrinachol am ddegawdau, a mynnwch fod gwerthwyr yn datgelu pa fodylau sydd wedi'u dilysu cyn i chi ymrwymo.

## Enghreifftiau

**Cwmni newydd.** Mae tîm bach sy'n adeiladu ap tracio iechyd yn pwyso'n llwyr ar ddiofynion a wiriwyd. Maent yn terfynu TLS gyda thystysgrifau a adnewyddir yn awtomatig, yn galluogi amgryptio wrth orffwys ar eu cronfa ddata a'u storio gwrthrychau a reolir gyda KMS y darparwr, ac yn hasio cyfrineiriau gyda ffwythiant araf, wedi'i heli o lyfrgell safonol. Yn hytrach na hysgrifennu unrhyw gryptograffeg eu hunain, maent yn defnyddio galwad amgryptio dilysedig lefel-uchel ar gyfer yr un maes y mae'n rhaid iddynt ei amgryptio yn y cymhwysiad. Mae cyfrinachau'n byw yn rheolwr cyfrinachau'r platfform, byth yn yr ystorfa. Mae'n costio ychydig brynhawniau ac yn dileu categori cyfan o gamgymeriadau trychinebus.

**Menter.** Mae banc byd-eang yn rhedeg KMS canolog a fflyd o HSMs, gyda rhestr eiddo gryptograffig sy'n olrhain pob allwedd a thystysgrif ar draws miloedd o wasanaethau. Mae amgryptio amlen yn diogelu data cwsmeriaid, gydag allweddi data wedi'u lapio gan brif allweddi sy'n cylchdroi ar amserlen tra bo'r data'n aros yn ei le. Mae cyhoeddi ac adnewyddu tystysgrifau wedi'u hawtomeiddio'n llawn ar ôl i derfyn gwasanaeth wynebu'r cyhoedd eu dysgu am gost un dystysgrif ddiedig. Mae gweinyddwyr allweddi'n dîm ar wahân i beirianwyr cymwysiadau, felly mae cadwraeth yn gorfodi gwahanu dyletswyddau, ac mae haen heini cryptograffig yn caniatáu iddynt ddechrau treialu algorithmau ôl-cwantwm ar gyfer archifau hirhoedlog.

**Llywodraeth.** Mae asiantaeth genedlaethol sy'n trin cofnodion dosbarthedig yn defnyddio modylau cryptograffig wedi'u dilysu gan FIPS 140 yn unig ac yn dilyn arweiniad CNSA yr NSA ar gyfer ei systemau dosbarthiad uchaf. Cynhyrchir a delir allweddi mewn HSMs nad ydynt byth yn rhyddhau deunydd allwedd testun plaen, ac mae cadwraeth wedi'i chysylltu â dosbarthiad data fel bod yr allweddi mwyaf sensitif yn eistedd gyda phersonél wedi'u clirio o dan wahanu dyletswyddau llym. Mae tystysgrifau'n rhedeg ar PKI mewnol a reolir gyda chylchredau oes awtomataidd, ac mae tystiolaeth barhaus o gryptograffeg wedi'i dilysu'n bwydo awdurdodiad parhaus yr asiantaeth. Mae cynllun mudo ôl-cwantwm wedi'i ddogfennu'n diogelu cofnodion y mae'n rhaid iddynt aros yn gyfrinachol am ddegawdau.

## Achos busnes: cymhellion, ROI, a TCO

Mae cryptograffeg yn faes arall lle mae buddsoddiad cymedrol yn atal colledion trychinebus, safon-pennawd. Mae cyfanswm cost perchnogaeth yn cynnwys KMS neu HSM, offer rheoli cyfrinachau a thystysgrifau, a'r amser peirianneg i ddylunio cylchredau oes a chadw rhestr eiddo'n gyfredol. Mae'r costau hyn yn wirioneddol ond yn gyfyngedig. Cost eu hepgor yw toriad i ddata heb ei amgryptio, terfyn gwasanaeth aml-awr o dystysgrif ddiedig, neu golled ddata anadferadwy o allwedd a gamdrinnir, pob un yn cario dirwyon rheoleiddiol, costau hysbysu, a niwed enw da parhaus.

Daw'r ROI cryfaf o awtomeiddio ac ailddefnyddio. Mae cylchredau oes tystysgrifau awtomataidd yn dileu'r terfyn gwasanaeth hunanachosedig mwyaf cyffredin. Mae rheoli allweddi canolog â diofynion synhwyrol yn golygu bod pob gwasanaeth newydd yn etifeddu amgryptio wrth gludo ac wrth orffwys heb ymdrech fesul tîm, gan droi cryptograffeg o dreth ailadroddus i alluogrwydd platfform. Ar gyfer gwaith rheoledig a llywodraethol, mae modylau wedi'u dilysu a thystiolaeth awtomataidd hefyd yn gostwng cost archwiliadau ac awdurdodi. Pan fyddwch yn gwneud yr achos i arweinyddiaeth, fframiwch ef yn blaen: mae'r algorithmau'n rhad ac am ddim ac wedi'u profi, mae'r risg yn byw mewn rheoli allweddi a gweithrediadau tystysgrifau, a bod buddsoddiad bach, awtomataidd yno'n atal y methiannau drud.

## Gwrth-batrymau a pheryglon

- **Creu eich cryptograffeg eich hun.** Algorithmau pwrpasol neu brotocolau a adeiladwyd â llaw sy'n methu mewn ffyrdd cynnil, arbenigwr-yn-unig.
- **Allweddi a chyfrinachau wedi'u codio'n galed.** Tystlythyrau wedi'u gludo i god ffynhonnell, ffeiliau ffurfweddu, neu sgwrs, lle maent yn gollwng ac na ellir eu cylchdroi.
- **Amgryptio heb ddisgyblaeth allwedd.** Troi amgryptio ymlaen ond gadael mynediad allwedd yn agored led y pen neu byth yn cylchdroi.
- **Drysu hasio ag amgryptio.** Trin hasyn fel un gwrthdroadwy, neu storio cyfrineiriau â hasyn cyflym yn lle un araf, wedi'i heli.
- **Rwlét tystysgrifau.** Dim rhestr eiddo, dim monitro diediad, a therfynau gwasanaeth syfrdanol cyfnodol pan fydd tystysgrif yn dod i ben.
- **Cadwraeth allwedd a mynediad data wedi'u cyfuno.** Un hunaniaeth a all reoli allwedd a darllen y data y mae'n ei ddiogelu fel ei gilydd.
- **Dim cynllun cylchdroi.** Allweddi na chawsant erioed eu cylchdroi ac na ellir eu cylchdroi'n gyflym o dan bwysau.
- **Cryptograffeg heb heini.** Algorithmau wedi'u gwifro mor ddwfn fel bod eu cyfnewid yn mynnu ailysgrifennu, gan rwystro unrhyw fudo yn y dyfodol.
- **Anwybyddu mandadau dilysu.** Defnyddio algorithmau cryf mewn modylau heb eu dilysu lle mae angen dilysiad FIPS neu debyg.

## Model aeddfedrwydd

- **Lefel 1, Cychwyn:** Mae amgryptio'n anghyson ac yn aml yn absennol, wedi'i gymhwyso'n adweithiol pan fydd rhywun yn sylwi ar fwlch. Mae allweddi a chyfrinachau wedi'u codio'n galed neu'n cael eu rhannu'n anffurfiol dros sgwrs a ffeiliau ffurfweddu. Nid oes rhestr eiddo, dim cylchdroi, ac mae tystysgrifau'n dod i ben ar syrpreis, ac mae timau weithiau'n ysgrifennu eu cryptograffeg eu hunain.
- **Lefel 2, Datblygu:** Mae TLS ac amgryptio wrth orffwys wedi'u troi ymlaen ar gyfer y systemau mawr, ac mae KMS neu reolwr cyfrinachau'n bodoli, ond mae mabwysiadu'n anwastad ac yn amrywio fesul tîm. Caiff rhai tystysgrifau eu monitro tra nad yw eraill, mae cylchdroi'n â llaw ac yn brin, a does dim rhestr eiddo gryptograffig gyflawn yn clymu popeth at ei gilydd.
- **Lefel 3, Safoni:** Amgryptio wrth gludo ac wrth orffwys yw'r diofyn dogfennedig a orfodir ledled y sefydliad. Mae allweddi'n byw mewn KMS gyda chylchdroi wedi'i amserlennu ac amgryptio amlen, mae cadwraeth allweddi wedi'i gwahanu oddi wrth fynediad data, mae cylchredau oes tystysgrifau wedi'u hawtomeiddio, cynhelir rhestr eiddo gryptograffig, a defnyddir modylau wedi'u dilysu lle bynnag y mae rheoleiddio'n ei fynnu.
- **Lefel 4, Rheoli:** Caiff yr ystad gryptograffig ei mesur a'i rheoli yn erbyn llinellau sylfaen. Rydych yn tracio amser arwain diediad tystysgrifau, canran yr allweddi a gylchdrowyd ar amserlen, amser cymedrig i ddirymu allwedd a beryglwyd, canfyddiadau cyfrinachau-mewn-cod fesul cyfnod, a chwmpas rhestr eiddo, ac rydych yn adolygu'r metrigau hyn yn erbyn targedau. Caiff cylchdroi a dirymu eu hymarfer ar gadence gydag amseriadau wedi'u cofnodi, ac mae gwyriadau'n sbarduno gweithred gywiro yn hytrach na mynd heb sylw.
- **Lefel 5, Cerdorfa:** Mae cryptograffeg yn alluogrwydd platfform y mae pob gwasanaeth yn ei etifeddu'n ddiofyn, ac fe'i gwellir a'i integreiddir yn barhaus ar draws y sefydliad. Mae cylchdroi a dirymu'n gyflym ac yn cael eu hymarfer yn rheolaidd, mae HSMs yn diogelu'r allweddi sicrwydd uchaf, ac mae heini cryptograffig ynghyd â chynllun mudo ôl-cwantwm gweithredol yn cadw'r ystad yn addasadwy wrth i algorithmau a mandadau newid. Cynhyrchir tystiolaeth cydymffurfiaeth yn awtomatig ac mae'n bwydo awdurdodiad parhaus.

## Syniadau ar gyfer trafod

1. Pa systemau yn eich ystad sy'n cyfiawnhau allweddi a reolir gan gwsmer neu HSMs o ystyried eu cost weithredol a'u risg colled drychinebus?
2. Sut y byddech chi'n adeiladu ac yn cynnal un ffynhonnell wirionedd ar gyfer pob allwedd a thystysgrif sydd gennych?
3. Beth yw eich amser realistig i gylchdroi allwedd a beryglwyd heddiw, a beth sy'n ei wneud yn araf?
4. Ble mae eich pensaernïaeth yn gwneud cyfnewid algorithm cryptograffig yn anodd, a sut y byddech chi'n trwsio hynny cyn mudo gorfodol?
5. Pa rai o'ch cyfrinachau hirhoedlog fyddai'n bwysig pe bai gwrthwynebydd yn eu casglu nawr ac yn eu datgryptio flynyddoedd yn ddiweddarach?
6. A yw cyfrinachau ac allweddi byth yn dod i ben mewn cod, ffurfweddiad, neu gofnodion, a sut y byddech chi'n gwybod?

## Prif negeseuon

- **Peidiwch â chreu eich cryptograffeg eich hun.** Defnyddiwch lyfrgelloedd a wiriwyd ac algorithmau safonol ar y haniaeth ddiogel uchaf.
- **Mae algorithmau'n hawdd; mae rheoli allweddi'n anodd.** Cylchred oes allwedd (cynhyrchu, dosbarthu, cylchdroi, dirymu, dinistrio) yw lle mae methiannau gwirioneddol yn byw.
- **Gwybyddwch eich gwarantau:** mae amgryptio cymesur a chyhoeddus yn diogelu cyfrinachedd, mae llofnodion yn profi dilysrwydd a chyfanrwydd, ac mae hasio'n canfod ymyrryd ond nid yw'n amgryptio.
- **Amgryptiwch wrth gludo gyda TLS cyfredol ac wrth orffwys gydag amgryptio amlen**, fel y diofyn ar gyfer pob system.
- **Gwahanwch gadwraeth allweddi oddi wrth fynediad data**, defnyddiwch KMS ar gyfer allweddi a rheolwr cyfrinachau ar gyfer tystlythyrau, a pheidiwch byth â chodio'r naill na'r llall yn galed.
- **Awtomeiddiwch gylchredau oes tystysgrifau** i ladd y terfyn gwasanaeth diediad-syfrdanol, a chadwch restr eiddo gryptograffig.
- **Adeiladwch ar gyfer heini cryptograffig** a dechreuwch gynllun mudo ôl-cwantwm ar gyfer cyfrinachau hirhoedlog.
- **Ffafriwch weithrediadau wedi'u dilysu** (FIPS 140 ac arweiniad cenedlaethol perthnasol) lle mae rheoleiddio neu ddosbarthiad yn ei fynnu.

## Cyfeiriadau a darllen pellach

- Sefydliad Cenedlaethol Safonau a Thechnoleg, *FIPS 140-3: Security Requirements for Cryptographic Modules*.
- Sefydliad Cenedlaethol Safonau a Thechnoleg, *SP 800-57: Recommendation for Key Management*.
- Sefydliad Cenedlaethol Safonau a Thechnoleg, *SP 800-131A: Transitioning the Use of Cryptographic Algorithms and Key Lengths*.
- Sefydliad Cenedlaethol Safonau a Thechnoleg, safonau cryptograffeg ôl-cwantwm (FIPS 203, 204, a 205).
- Niels Ferguson, Bruce Schneier, a Tadayoshi Kohno, *Cryptography Engineering*.
- Jean-Philippe Aumasson, *Serious Cryptography*.
- David Wong, *Real-World Cryptography*.
- Internet Engineering Task Force, *RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3*.
- Prosiect Diogelwch Cymwysiadau Gwe Agored, *Cryptographic Storage Cheat Sheet* a *Transport Layer Protection Cheat Sheet*.
- Asiantaeth Diogelwch Cenedlaethol, arweiniad *Commercial National Security Algorithm (CNSA) Suite*.
