# 2.10 Rheolaeth ffurfweddiad meddalwedd

## Trosolwg a chymhelliant

Mae [rheolaeth ffurfweddiad meddalwedd](https://en.wikipedia.org/wiki/Software_configuration_management) (SCM) yn ddisgyblaeth adnabod cydrannau system feddalwedd, rheoli sut maent yn newid, cofnodi cyflwr pob newid, a gwirio bod yr hyn a adeiladwyd ac a draddodwyd yn cyfateb i'r hyn a fwriadwyd. Mae'n ateb cwestiwn sy'n swnio'n syml ond sy'n mynd yn anodd ar raddfa fawr: beth yn union sydd yn y rhyddhad hwn, sut y cyrhaeddodd yno, a phwy a'i cymeradwyodd? Mae [SWEBOK](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) yn trin SCM fel maes gwybodaeth sylfaenol am reswm clir: mae angen ffurfweddiad sefydlog, hysbys ar bob gweithgaredd peirianneg arall i weithio yn ei erbyn.

Mewn tîm mawr, SCM yw'r meinwe gysylltiol sy'n cadw miloedd o rannau symudol yn gydlynol. Mae cod ffynhonnell, llyfrgelloedd, delweddau cynhwysydd, diffiniadau seilwaith, data ffurfweddiad, dogfennaeth, ac arteffactau prawf i gyd yn newid ar eu clociau eu hunain, ac mae system a draddodwyd yn gyfuniad penodol o fersiynau penodol o bob un ohonynt. Heb reolaeth ffurfweddiad fwriadol, mae'r cyfuniad hwnnw'n anhysbys ac ni ellir ei atgynhyrchu. Ni allwch ailgreu rhyddhad blaenorol, olrhain nam i'r newid a'i hachosodd, na dweud yn hyderus beth sy'n rhedeg mewn cynhyrchu.

Mae lleoliadau menter a llywodraeth yn codi'r stanciau. Mae'n rhaid i raglenni rheoleiddiedig a sector cyhoeddus ddangos bod newidiadau wedi'u hawdurdodi, eu hadolygu, a'u cofnodi; bod adeiladwaith a draddodwyd yn olrhain yn ôl at ofynion a ffynhonnell gymeradwy; ac na ddaeth dim i mewn i'r system yn ddi-reolaeth. Yma mae SCM yr un mor llawer yn system dystiolaeth ag yn un beirianneg. Mae [rheolaeth fersiynau](https://en.wikipedia.org/wiki/Version_control) (pennod 2.6) yn rheoli hanes ffynhonnell; mae SCM yn llywodraethu'r ffurfweddiad cyfan a'r broses reoledig y mae'n newid drwyddi. Mae'n gysylltiedig yn agos â [seilwaith fel cod](https://en.wikipedia.org/wiki/Infrastructure_as_code) (pennod 8.2), piblinellau traddodi (pennod 8.1), ac archwilio a sicrwydd (pennod 10.2).

## Egwyddorion allweddol

- Mae popeth sy'n penderfynu ymddygiad system yn [eitem ffurfweddiad](https://en.wikipedia.org/wiki/Configuration_item) dan reolaeth, nid dim ond cod ffynhonnell.
- Mae [llinell sylfaen](https://en.wikipedia.org/wiki/Baseline_(configuration_management)) yn bwynt cyfeirio hysbys, cytunedig; gwneir newidiadau yn erbyn llinellau sylfaen yn fwriadol, nid yn achlysurol.
- Mae newid yn cael ei reoli a'i gofnodi, nid ei atal; y nod yw newid awdurdodedig, olrheiniadwy.
- Mae cyfrifo statws yn golygu y gallwch bob amser ateb beth sydd mewn ffurfweddiad a beth yw ei hanes newid.
- Mae archwiliadau'n gwirio bod y system a adeiladwyd ac a draddodwyd yn cyfateb i'r ffurfweddiad cofnodedig a'r gofynion cymeradwy.
- Nid yw atgynhyrchadwyedd yn destun trafodaeth: rhaid gallu ailadeiladu unrhyw fersiwn a ryddhawyd o fewnbynnau rheoledig.
- Awtomeiddiwch adnabod, cofnodi, a gwirio; nid yw cadw cyfrifon â llaw'n graddio ac nid yw'n goroesi archwiliad.

## Argymhellion

### Diffiniwch y broses SCM a neilltuwch berchnogaeth

Ysgrifennwch gynllun SCM sy'n dweud beth sydd dan reolaeth ffurfweddiad, sut mae eitemau'n cael eu hadnabod, sut mae newidiadau'n cael eu cynnig a'u cymeradwyo, a sut mae statws yn cael ei gofnodi a'i archwilio. Neilltuwch berchnogaeth glir, fel rheolwr ffurfweddiad neu dîm atebol, fel nad yw SCM yn swydd i bawb ac felly'n swydd i neb. Graddiwch y broses yn ôl y risg: mae angen rheolaeth ysgafn ar declyn mewnol bach, tra bo angen byrddau a chofnodion ffurfiol ar system ddiogelwch-critigol neu reoleiddiedig. Angorwch y cynllun mewn safon gydnabyddedig fel IEEE 828 fel y gall archwilwyr a phartneriaid ei ddilyn.

### Adnabyddwch eitemau ffurfweddiad a sefydlwch linellau sylfaen

Rhestrwch yr eitemau ffurfweddiad sy'n penderfynu sut mae'r system yn ymddwyn: ffynhonnell, dibyniaethau, sgriptiau adeiladu, delweddau cynhwysydd, diffiniadau seilwaith, data ffurfweddiad, sgemâu, a dogfennau allweddol. Rhowch bob un adnabyddwr sefydlog a chynllun fersiynu. Gosodwch linellau sylfaen ar bwyntiau ystyrlon (fersiwn a ryddhawyd, set ofynion gymeradwy, adeiladwaith ardystiedig) fel bod gennych gyfeirbwynt cytunedig i newid yn ei erbyn ac i ddychwelyd ato. Mae llinell sylfaen yn anghyfnewidiol: unwaith y byddwch yn ei datgan, nid ydych yn ei golygu. Dim ond drwy ei disodli â llinell sylfaen newydd a grëwyd drwy'r broses newid y gwnewch chi hynny.

### Rheolwch newid drwy broses ddiffiniedig a byrddau priodol

Llwybrwch newidiadau i eitemau rheoledig drwy lwybr diffiniedig: cynnig, asesiad effaith, cymeradwyaeth, gweithrediad, a gwirio. Ar gyfer eitemau risg uwch, defnyddiwch [fwrdd rheoli newid](https://en.wikipedia.org/wiki/Change_control_board) (CCB) sy'n pwyso cost, risg, ac amserlen cyn iddo awdurdodi newid. Meintiolwch y bwrdd yn briodol: giât awtomataidd ysgafn ar gyfer newidiadau cod rheolaidd, a CCB ffurfiol traws-swyddogaethol ar gyfer newidiadau sy'n cyffwrdd â llinellau sylfaen, rhyngwynebau, neu ymddygiad rheoleiddiedig. Cofnodwch bob penderfyniad a'r rhesymeg y tu ôl iddo, a chysylltwch benderfyniadau ffurfweddiad arwyddocaol â chofnodion penderfyniad (pennod 1.6) fel bod y rhesymeg yn goroesi.

### Cynhaliwch gyfrifo statws ffurfweddiad

Cadwch gofnod cywir, y gellir ymholi ynddo, o bob eitem ffurfweddiad: ei fersiwn cyfredol, pa linell sylfaen y mae'n perthyn iddi, a'r ceisiadau newid a gymhwyswyd iddi. Y cyfrifo statws hwn sy'n eich galluogi i ateb, ar unrhyw eiliad, beth sydd mewn rhyddhad a sut y cyrhaeddodd yno. Cynhyrchwch y cofnod yn awtomatig o'ch offer cofnod (rheolaeth fersiynau, piblinell, cofrestrfa arteffactau) yn hytrach na chynnal taenlen gyfochrog sy'n drifftio oddi wrth realiti. Y cofnod hwn yw asgwrn cefn olrheinadwyedd o ofyniad i newid i adeiladwaith i ddefnyddio.

### Cynhaliwch archwiliadau ffurfweddiad

Gwiriwch ddau beth ar amserlen reolaidd. Mae archwiliad ffurfweddiad swyddogaethol yn cadarnhau bod y ffurfweddiad yn perfformio yn y ffordd y mae ei ofynion yn ei phennu. Mae archwiliad ffurfweddiad ffisegol yn cadarnhau bod yr arteffactau a draddodwyd yn cyfateb i'r ffurfweddiad cofnodedig: bod yr adeiladwaith wedi dod o'r ffynhonnell a'r dibyniaethau cofnodedig ac nad yw'n cynnwys dim heb ei gyfrif. Awtomeiddiwch gymaint o hyn ag y gallwch: mae [adeiladau atgynhyrchadwy](https://en.wikipedia.org/wiki/Reproducible_builds), swm-wiriadau arteffactau, biliau deunyddiau meddalwedd (SBOMs), a thystiadau tarddiad yn troi archwilio o arolygiad â llaw yn wiriad parhaus.

### Rheolwch ryddhadau a thraddodiad fel digwyddiadau rheoledig

Triniwch ryddhad fel llinell sylfaen benodol, wedi'i hadnabod, a draddodwyd drwy broses ailadroddadwy. Fersiynwch eich rhyddhadau'n benodol, cynhyrchwch faniffest neu fil deunyddiau sy'n disgrifio'n union beth sydd wedi'i gynnwys, a chofnodwch y mapio o ryddhad i adolygiad ffynhonnell i arteffact wedi'i ddefnyddio. Llofnodwch a swm-wiriwch arteffactau a ryddhawyd fel y gall unrhyw un i lawr yr afon wirio eu cyfanrwydd. Cysylltwch reoli rhyddhadau â'r biblinell draddodi (pennod 8.1) fel bod dyrchafiad drwy amgylcheddau ei hun yn cael ei reoli, ei gofnodi, a'i wrthdroi.

### Dewiswch ac integreiddiwch offer SCM

Pwyswch ar offer sy'n awtomeiddio adnabod, rheoli, cyfrifo, ac archwilio yn hytrach na dibynnu ar ddisgyblaeth yn unig: rheolaeth fersiynau ar gyfer ffynhonnell, cofrestrfeydd arteffact a delwedd ar gyfer deuolion, piblinell anghyfnewidiol ar gyfer adeiladau, seilwaith fel cod ar gyfer amgylcheddau, ac offer dibyniaeth a SBOM ar gyfer tarddiad. Cysylltwch nhw fel bod un newid yn llifo'n olrheiniadwy o ymrwymiad i ryddhad wedi'i ddefnyddio. Yr hyn rydych ar ei ôl yw cadwyn offer lle mae'r cofnod ffurfweddiad yn sgil-gynnyrch gwneud y gwaith, nid tasg glercol ar wahân.

## Cyfaddawdau: manteision ac anfanteision

| Dewis | Manteision | Anfanteision |
|---|---|---|
| Byrddau rheoli newid ffurfiol | Awdurdodiad cryf a llwybr archwilio; risg wedi'i phwyso cyn newid | Trwybwn arafach; baich os cymhwysir i newidiadau rheolaidd |
| Giatiau awtomataidd ysgafn | Llif cyflym; baich isel; yn graddio i lawer o newidiadau | Gwannach ar gyfer llinellau sylfaen risg-uchel; llai o ystyriaeth |
| Llinellau sylfaen anghyfnewidiol llym | Pwyntiau cyfeirio atgynhyrchadwy, archwiliadwy | Angen disgyblaeth ac offer; ffrithiant os gorddefnyddir |
| Cyfrifo statws awtomataidd | Cofnod cywir, cyfredol bob amser; parod ar gyfer archwiliad | Buddsoddiad offer ac integreiddio ymlaen llaw |
| Cofnodion ffurfweddiad â llaw | Syml i'w cychwyn; dim angen offer | Yn drifftio oddi wrth realiti; yn methu ar raddfa fawr ac o dan archwiliad |

Y prif gyfaddawd yw rheolaeth yn erbyn llif. Mae rheolaeth newid drwm yn rhoi sicrwydd cryf ond yn arafu traddodiad. Mae rheolaeth ysgafn yn llifo'n gyflym ond yn gwanhau olrheinadwyedd. Nid yw'r ateb yn ddewis un yn fyd-eang; mae'n haenu rheolaeth yn ôl risg: awtomeiddiwch newidiadau rheolaidd drwy giatiau cyflym, a chadwch fyrddau ffurfiol a llinellau sylfaen anghyfnewidiol ar gyfer yr eitemau lle mae awdurdodiad ac archwiliadwyedd wir yn bwysig. Yr ail gyfaddawd yw buddsoddiad offer ymlaen llaw yn erbyn cost glercol barhaus a risg archwilio. Mae cyfrifo awtomataidd yn costio mwy i'w sefydlu ac yn llawer llai i fyw ag ef.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Beth yn union sy'n perthyn ar ein rhestr eitemau ffurfweddiad, a phwy sy'n berchen ar y penderfyniad pan fo rhywbeth newydd yn ymddangos?** Dim ond yn gweithio y mae SCM os yw'r rhestr o eitemau rheoledig yn cyfateb i'r set o bethau sydd wir yn penderfynu ymddygiad, ac ar system fawr mae'r set honno'n fwy na'r hyn y mae'r rhan fwyaf o dimau'n ei feddwl: ffynhonnell, dibyniaethau, sgriptiau adeiladu, delweddau cynhwysydd, diffiniadau seilwaith, sgemâu, baneri nodwedd, a'r data ffurfweddiad sy'n newid yn dawel yr hyn y mae'r feddalwedd yn ei wneud. Os nad oes neb yn berchen ar y rhestr, mae'n mynd yn hen, ac mae'r eitem a'ch trawodd yn gynhyrchu'n troi allan i fod yr un peth nad oedd neb wedi meddwl ei reoli. Dewch â'ch stocrestr gyfredol i'r cyfarfod a chwiliwch am eitemau sy'n penderfynu ymddygiad ac sydd ar goll ohoni. Neilltuwch berchennog atebol (rheolwr ffurfweddiad neu dîm penodedig) fel bod ychwanegu eitem newydd yn benderfyniad bwriadol, nid damwain, oherwydd nid yw SCM sy'n swydd i bawb yn swydd i neb.

2. **A allwn brofi bod arteffact a ddefnyddiwyd wedi dod o'r ffynhonnell a'r biblinell rydym yn meddwl y daeth ohonynt, ac a fyddai'r prawf hwnnw'n goroesi ymyrraeth?** Atgynhyrchadwyedd ac olrheinadwyedd yw holl bwynt SCM, a fersiwn miniog y cwestiwn yw a allwch gysylltu'r deuol sy'n rhedeg yn ôl â chomit penodol a rhediad adeiladu penodol gyda thystiolaeth, nid haeriad. Mewn system reoleiddiedig neu werth-uchel dyma hefyd eich amddiffyniad cadwyn-gyflenwad: mae tystiadau tarddiad wedi'u llofnodi, swm-wiriadau arteffactau, a bil deunyddiau meddalwedd yn troi "rydym eithaf sicr" yn rhywbeth y gall archwiliwr neu ymatebwr digwyddiad ei wirio. Dewch â'ch rhyddhad diwethaf a cheisiwch ei gerdded yn ôl o'r arteffact a ddefnyddiwyd i'r newid cymeradwy. Os yw unrhyw naid yn hawliad â llaw yn hytrach na chyswllt cofnodedig, y gellir ei wirio, dyna lle gall ymosodwr neu gamgymeriad gonest lithro rhywbeth i mewn heb ei sylwi, ac mae ei gau'n golygu gwifro llofnodi a tharddiad i mewn i'r biblinell fel bod y cofnod yn sgil-gynnyrch traddodiad.

3. **A oes unrhyw un yn gallu golygu rhyddhad yn ei le heddiw, a beth fyddai hynny'n ei wneud i'n gallu i ymddiried ynddo?** Dim ond os yw'n anghyfnewidiol y mae llinell sylfaen yn ddefnyddiol: y foment y gellir golygu "y rhyddhad" ar ôl y ffaith, ni allwch mwyach ei atgynhyrchu na dibynnu arno fel cyfeirbwynt, ac mae pob archwiliad i lawr yr afon yn dod yn archaeoleg. Y methiant clasurol yw ffurfweddiad wedi'i olygu'n uniongyrchol mewn cynhyrchu neu dag wedi'i symud yn dawel, sef yn union y llwybr byr sy'n teimlo'n ddiniwed ac sy'n gwneud rhyddhad yn amhosibl ei ailadeiladu'n ddiweddarach. Dewch â'r ateb gonest i'r cyfarfod: pwy sydd â'r mynediad i newid llinell sylfaen wedi'i defnyddio heb fynd drwy'r broses newid, ac a yw wedi digwydd? Y datrysiad yw gwneud llinellau sylfaen yn wirioneddol anghyfnewidiol a llwybro pob newid drwy gynnig, asesiad effaith, cymeradwyaeth, a gwirio, gan haenu'r trylwyredd fel bod newidiadau rheolaidd yn llifo drwy giatiau awtomataidd cyflym tra bo newidiadau llinell sylfaen a rheoleiddiedig yn mynd at fwrdd.

4. **A yw ein cyfrifo statws ffurfweddiad yn cael ei gynhyrchu'n awtomatig o'n hoffer cofnod, neu ei gynnal â llaw, a pha mor bell y mae wedi drifftio oddi wrth yr hyn sydd wedi'i ddefnyddio mewn gwirionedd?** Y cyfrifo statws yw'r cofnod sy'n eich galluogi i ateb, ar unrhyw eiliad, beth sydd mewn rhyddhad a sut y cyrhaeddodd yno, ac ar system fawr dim ond yn ddibynadwy y mae'r cofnod hwnnw os yw'n disgyn allan o'r gwaith yn hytrach na chael ei deipio i mewn i daenlen gyfochrog. Y dynfa gystadleuol yw bod cofrestr wedi'i chadw â llaw'n teimlo'n rhad i'w chychwyn ac yn hyblyg, tra bo ei hawtomeiddio'n golygu integreiddio rheolaeth fersiynau, y biblinell, a chofrestrfa'r arteffactau fel bod y cofnod yn dod yn sgil-gynnyrch traddodiad. Dewch â'r gofrestr rydych yn dibynnu arni heddiw, dewiswch dri rhyddhad diweddar ar hap, a gwiriwch a yw'r fersiynau, y llinellau sylfaen, a'r ceisiadau newid cofnodedig yn cyfateb i'r hyn y mae'r offer yn dweud a ryddhawyd. Ar gyfer rhaglen fenter neu lywodraeth, nid problem daclusrwydd yw cofnod statws sy'n gwyro oddi wrth realiti, mae'n ganfyddiad archwilio sy'n aros i ddigwydd, oherwydd mae archwiliwr sy'n dal un bwlch yn peidio ag ymddiried yn y cyfrif cyfan ac yn gofyn i chi ei ailadeiladu â llaw.

5. **A yw ein rheolaeth newid wedi'i haenu yn ôl risg, neu a yw'r un lefel o seremoni'n llywodraethu pob newid ni waeth beth mae'n ei gyffwrdd?** Mae rheolaeth a llif yn tynnu yn erbyn ei gilydd: mae bwrdd rheoli newid ffurfiol yn pwyso cost, risg, ac amserlen cyn iddo awdurdodi newid, ond mae cymhwyso'r seremoni honno i newid cod rheolaidd dim ond yn ychwanegu oedi, tra bo gwthio llinell sylfaen a rennir neu lif taliadau rheoleiddiedig drwy giât awtomataidd gyflym yn dileu ystyriaeth yn union lle mae ei angen. Mae'r moddau methiant yn gymesur, trymder unffurf y mae pobl yn dysgu ei osgoi, neu lacrwydd unffurf sy'n gadael i newid risg-uchel lithro drwodd heb ei archwilio. Dewch â sampl o newidiadau'r chwarter diwethaf wedi'u trefnu yn ôl yr hyn a gyffyrddwyd gan bob un, a gwiriwch a oedd y trylwyredd a dderbyniodd yn wir yn cyfateb i'w risg. Mewn lleoliad rheoleiddiedig neu sector cyhoeddus, enwch pa ddosbarthiadau eitem sy'n gorfod cyrraedd bwrdd traws-swyddogaethol a pha rai a all lifo drwy giatiau awtomataidd, a chofnodwch yr haenu hwnnw'n benodol, oherwydd nid yw "rydym yn defnyddio barn" yn rheolaeth y gall archwiliwr neu gorff trosolwg ei gwirio.

6. **Pryd wnaethom ni redeg archwiliad ffurfweddiad swyddogaethol a ffisegol ddiwethaf, a faint o'r dystiolaeth fyddai'n gofnod byw yn hytrach nag ailadeiladwaith?** Mae archwiliad ffurfweddiad swyddogaethol yn cadarnhau bod y system yn perfformio yn y ffordd y mae ei gofynion yn ei phennu, ac mae archwiliad ffurfweddiad ffisegol yn cadarnhau bod yr arteffactau a draddodwyd yn cyfateb i'r ffurfweddiad cofnodedig ac nad ydynt yn cynnwys dim heb ei gyfrif; eu hepgor ac rydych yn ymddiried bod eich llinellau sylfaen a'ch cyfrifo statws yn onest heb erioed wirio. Y tyndra yw cost: mae archwiliadau â llaw'n araf ac yn boenus, sef yn union pam mae timau'n eu gohirio, a'r ffordd allan yw awtomeiddio'r gwiriadau ag adeiladau atgynhyrchadwy, swm-wiriadau arteffactau, biliau deunyddiau meddalwedd, a thystiadau tarddiad fel bod gwirio'n dod yn barhaus. Dewch â'ch rhyddhad diweddaraf a cheisiwch gynhyrchu, ar y pryd, yr olrhain gofyniad-i-newid-i-adeiladwaith-i-ddefnyddio a'r prawf arteffact-i-ffynhonnell. Ar gyfer rhaglenni menter a llywodraeth, dyma'r trywydd tystiolaeth y mae ardystio a throsolwg yn ei fynnu, felly'r cwestiwn gonest yw a fyddai archwiliad yfory'n cael ei ateb o gofnodion sydd gennych eisoes neu o ymarfer archaeoleg na allwch ei fforddio.

## Lens sector

**Startup.** Cadwch SCM yn ysgafn ond yn wirioneddol. Rhowch ffynhonnell, diffiniadau seilwaith, a data ffurfweddiad mewn rheolaeth fersiynau, a gwnewch bob rhyddhad yn adeiladwaith wedi'i dagio a gynhyrchwyd gan un biblinell yn hytrach nag arteffact wedi'i gydosod â llaw. Hepgorwch fyrddau rheoli newid a llinellau sylfaen ffurfiol, sy'n ormodedd ar eich maint, ond peidiwch byth â gadael i unrhyw un olygu ffurfweddiad yn uniongyrchol mewn cynhyrchu, oherwydd yr un llwybr byr hwnnw yw'r hyn sy'n gwneud rhyddhad yn amhosibl ei atgynhyrchu pan fo cwsmer yn taro nam ddydd Mawrth nesaf.

**Busnes bach.** Heb reolwr ffurfweddiad a chyllideb dynn, pwyswch ar offer sy'n rhoi SCM bron am ddim i chi: platfform rheolaeth fersiynau wedi'i letya, ei biblinell adeiledig, a chofrestrfa arteffact, fel bod y cofnod ffurfweddiad yn sgil-gynnyrch yn hytrach na swydd y mae'n rhaid i chi ei staffio. Prynwch y gallu hwn wedi'i mewnadeiladu mewn offer rydych eisoes yn talu amdanynt yn lle adeiladu proses bwrpasol. Treuliwch eich sylw prin ar y ddau arferiad sydd bwysicaf, rhyddhadau wedi'u tagio, atgynhyrchadwy a chadw ffurfweddiad sy'n newid ymddygiad allan o olygiadau cynhyrchu â llaw.

**Menter.** Y broblem yw cysondeb ar draws llawer o dimau: cynllun SCM a rennir, tacsonomeg eitem-ffurfweddiad gyffredin, rheolaeth newid wedi'i haenu, a chyfrifo statws wedi'i gynhyrchu'n awtomatig o reolaeth fersiynau, cofrestrfa'r arteffactau, a'r biblinell. Cadwch fyrddau rheoli newid ffurfiol a llinellau sylfaen anghyfnewidiol ar gyfer llifau platfform a rennir a rheoleiddiedig, gadewch i newidiadau rheolaidd lifo drwy giatiau awtomataidd, a safonwch darddiad wedi'i lofnodi a SBOMs fel y gellir olrhain rhyddhad unrhyw dîm a gall unrhyw archwiliwr ymholi cofnod byw yn lle comisiynu ailadeiladwaith.

**Llywodraeth.** Mae rheolau caffael, tryloywder, ac atebolrwydd cyhoeddus yn siapio'r broses. Dilynwch gynllun SCM ffurfiol wedi'i alinio â safon gydnabyddedig fel IEEE 828, llinell-sylfaenwch eitemau ffurfweddiad ar gerrig milltir cytundebol, a llwybrwch bob newid i linell sylfaen reoledig drwy fwrdd sy'n cofnodi effaith, penderfyniad, a rhesymeg. Mynnwch fod arteffactau a draddodwyd yn atgynhyrchadwy o fewnbynnau rheoledig, wedi'u swm-wirio, ac yn olrheiniadwy o'r dechrau i'r diwedd o ofyniad cymeradwy i adeiladwaith a draddodwyd, oherwydd dyna'n union yw'r trywydd tystiolaeth ddogfennedig y mae ardystio, archwilio, a throsolwg cyhoeddus yn ei fynnu.

## Enghreifftiau

**Startup.** Mae startup chwe-pherson yn cadw ei SCM yn ysgafn ond yn wirioneddol: mae ffynhonnell, diffiniadau seilwaith, a data ffurfweddiad i gyd yn byw mewn rheolaeth fersiynau, ac mae pob rhyddhad yn adeiladwaith wedi'i dagio, wedi'i fersiynu a gynhyrchwyd gan yr un biblinell yn hytrach na'i gydosod â llaw. Pan fo cwsmer yn adrodd nam a ymddangosodd ddydd Mawrth diwethaf, maent yn olrhain yr arteffact a ddefnyddiwyd yn ôl at yr union gomit mewn munudau yn lle dyfalu. Maent yn hepgor byrddau rheoli newid a llinellau sylfaen ffurfiol, a fyddai'n ormodedd ar eu maint, ond maent yn gwrthod gadael i unrhyw un olygu ffurfweddiad yn uniongyrchol mewn cynhyrchu, oherwydd yr un llwybr byr hwnnw yw'r hyn sy'n gwneud rhyddhad yn amhosibl ei atgynhyrchu'n ddiweddarach.

**Menter.** Mae cwmni gwasanaethau ariannol mawr yn rhoi pob arteffact y gellir ei ddefnyddio, diffiniadau seilwaith, a data ffurfweddiad dan reolaeth ffurfweddiad. Mae pob rhyddhad yn llinell sylfaen anghyfnewidiol, wedi'i fersiynu gyda bil deunyddiau meddalwedd wedi'i gynhyrchu, ac mae pob arteffact wedi'i ddefnyddio'n cario tystiad tarddiad wedi'i lofnodi sy'n ei gysylltu ag adolygiad ffynhonnell penodol a rhediad piblinell. Mae newidiadau cymhwysiad rheolaidd yn llifo drwy giatiau piblinell awtomataidd, tra bo newidiadau i linellau sylfaen platfform a rennir neu lifau taliadau rheoleiddiedig yn mynd at fwrdd rheoli newid. Mae cyfrifo statws yn cael ei gynhyrchu'n awtomatig o reolaeth fersiynau, cofrestrfa'r arteffactau, a'r biblinell, fel bod archwilwyr yn ymholi cofnod byw yn lle gofyn am ailadeiladwaith.

**Llywodraeth.** Mae rhaglen amddiffyn yn dilyn cynllun SCM ffurfiol wedi'i alinio ag IEEE 828. Mae eitemau ffurfweddiad wedi'u rhestru a'u llinell-sylfaenu ar gerrig milltir cytundebol, ac mae bwrdd rheoli newid yn awdurdodi pob newid i linell sylfaen reoledig, gan gofnodi effaith, penderfyniad, a rhesymeg. Mae archwiliadau ffurfweddiad swyddogaethol yn cadarnhau bod y system a draddodwyd yn bodloni gofynion penodedig, ac mae archwiliadau ffurfweddiad ffisegol yn cadarnhau bod arteffactau a draddodwyd yn cyfateb i'r ffurfweddiad cofnodedig yn union. Mae rhyddhadau'n atgynhyrchadwy o fewnbynnau rheoledig, wedi'u swm-wirio, ac yn olrheiniadwy o'r dechrau i'r diwedd, o ofyniad cymeradwy drwy gais newid i adeiladwaith a draddodwyd, sef yn union y trywydd tystiolaeth y mae ardystio a throsolwg yn ei fynnu.

## Achos busnes: cymhellion, ROI, a TCO

Mae SCM yn bodoli i reoli risg a chost ar draws oes system. Daw'r enillion o atgynhyrchadwyedd ac olrheinadwyedd: gallwch ailgreu unrhyw ryddhad, olrhain namau i'r newidiadau a'u hachosodd, ac ateb cwestiynau archwilio o gofnodion yn lle archaeoleg. Mae hynny'n crebachu amser diagnosis digwyddiad, yn lleihau cost a hyd archwiliadau, ac yn atal y dosbarth drud o fethiant lle nad oes neb yn gallu dweud beth sy'n rhedeg na sut i'w ailadeiladu.

Mae cyfanswm cost perchnogaeth yn ffafrio awtomeiddio. Mae cofnodion ffurfweddiad â llaw'n rhad i'w cychwyn ac yn gynyddol ddrud i'w cynnal, ac maent yn methu'n union pan fo eu hangen fwyaf, yn ystod digwyddiad neu archwiliad, oherwydd eu bod wedi drifftio oddi wrth realiti. Mae adnabod, cyfrifo, ac archwilio awtomataidd yn costio mwy ymlaen llaw ond yn troi'r cofnod ffurfweddiad yn sgil-gynnyrch bron-am-ddim o'r biblinell draddodi. I wneud yr achos i arweinyddiaeth, fframiwch SCM fel y rheolaeth sy'n gwneud rhyddhadau'n atgynhyrchadwy a newidiadau'n archwiliadwy, a phwyswch ef yn erbyn cost rhyddhadau na ellir eu hatgynhyrchu, archwiliadau hirfaith, a risg cydymffurfiaeth newid di-reolaeth.

## Gwrthbatrymau a pheryglon

- **Ffurfweddiad drwy wybodaeth lwythol:** mae cynnwys gwirioneddol rhyddhad yn byw dim ond ym mhen peiriannydd, nid mewn unrhyw gofnod.
- **Llinellau sylfaen nadwy:** mae "y rhyddhad" yn cael ei olygu yn ei le, fel na ellir ei atgynhyrchu na'i ymddiried ynddo fel cyfeirbwynt mwyach.
- **Data ffurfweddiad di-reolaeth:** mae cod dan reolaeth fersiynau ond mae'r ffurfweddiad sy'n newid ei ymddygiad yn cael ei olygu ad hoc mewn cynhyrchu.
- **Theatr rheoli newid:** bwrdd sy'n stampio popeth â rwber, gan ychwanegu oedi heb ychwanegu craffter gwirioneddol.
- **Cyfrifo statws â llaw:** taenlen o fersiynau sy'n gwyro'n dawel oddi wrth yr hyn sydd wedi'i ddefnyddio mewn gwirionedd.
- **Adeiladau na ellir eu hatgynhyrchu:** rhyddhadau na ellir eu hailadeiladu o fewnbynnau rheoledig, fel bod archwiliadau ac ailadeiladau'n dod yn ddyfalu.
- **Rhyddhadau na ellir eu holrhain:** dim mapio o arteffact wedi'i ddefnyddio yn ôl i adolygiad ffynhonnell, cais newid, a chymeradwyaeth.

## Model aeddfedrwydd

- **Lefel 1 (Cychwyn):** Mae SCM yn ad hoc ac yn adweithiol. Dim ond ffynhonnell sy'n cael ei rheoli; mae rhyddhadau'n cael eu cydosod â llaw; nid oes llinellau sylfaen, dim cofnod dibynadwy o'r hyn sydd wedi'i ddefnyddio, a dim ffordd o atgynhyrchu adeiladwaith blaenorol.
- **Lefel 2 (Datblygu):** Mae arferion sylfaenol yn bodoli ond yn amrywio o dîm i dîm. Mae rhai systemau'n diffinio eitemau ffurfweddiad a phroses newid ac yn fersiynu eu rhyddhadau, mae llinellau sylfaen yn bodoli yma ac acw, ond mae cofnodion yn rhannol â llaw ac mae trylwyredd y rheolaeth yn anghyson ar draws y sefydliad.
- **Lefel 3 (Safoni):** Mae arferion wedi'u dogfennu a'u gorfodi ar draws y sefydliad. Mae tacsonomeg eitem-ffurfweddiad gyffredin, llinellau sylfaen anghyfnewidiol, rheolaeth newid wedi'i haenu, a chyfrifo statws wedi'u sefydlu ac wedi'u hawtomeiddio i raddau helaeth; mae rhyddhadau'n atgynhyrchadwy ac yn olrheiniadwy, ac mae archwiliadau'n cael eu cefnogi gan offer yn hytrach na chof.
- **Lefel 4 (Rheoli):** Mae SCM yn cael ei fesur a'i reoli â data. Mae cyfradd atgynhyrchadwyedd, sylw olrheinadwyedd o ofyniad i arteffact wedi'i ddefnyddio, amser arwain newid drwy bob haen reolaeth, digwyddiadau drifft ffurfweddiad, a chanfyddiadau archwilio'n cael eu tracio yn erbyn llinellau sylfaen a thargedau. Mae gwyriadau'n sbarduno cywiro, ac mae pob penderfyniad ewch-neu-na'n gorffwys ar y dystiolaeth hon yn hytrach nag ar haeriad.
- **Lefel 5 (Cydgysylltu):** Mae SCM yn cael ei wella'n barhaus a'i integreiddio ar draws y sefydliad. Wedi'i awtomeiddio'n llawn a'i wirio'n barhaus ag adeiladau atgynhyrchadwy, SBOMs, tystiadau tarddiad, a chyfrifo statws byw, mae'r broses wedi'i gwau i mewn i draddodiad, diogelwch, ac archwilio, ac mae'n addasu wrth i risg a chanlyniadau traddodi symud, gan ymddeol ac ailgwmpasu rheolaethau ar sail tystiolaeth.

## Syniadau ar gyfer trafodaeth

- A allwch atgynhyrchu eich rhyddhad diwethaf yn union o fewnbynnau rheoledig heddiw, a faint o amser y byddai'n ei gymryd?
- Pa eitemau ffurfweddiad sy'n penderfynu ymddygiad ond nad ydynt mewn gwirionedd dan reolaeth, yn enwedig data ffurfweddiad a seilwaith?
- A yw eich rheolaeth newid wedi'i haenu yn ôl risg, neu a yw'n ychwanegu baich unffurf neu lacrwydd unffurf ym mhobman?
- Ble mae eich cofnod ffurfweddiad yn byw, a pha mor bell y mae wedi drifftio oddi wrth yr hyn sydd wedi'i ddefnyddio mewn gwirionedd?
- Pa dystiolaeth y gallech ei chynhyrchu mewn archwiliad yfory, a faint ohoni fyddai'n ailadeiladwaith yn hytrach na chofnod?
- Sut mae adeiladau atgynhyrchadwy, SBOMs, a tharddiad yn newid yr hyn y gall eich archwiliadau ei wirio'n awtomatig?

## Prif gasgliadau

- Mae SCM yn rheoli'r ffurfweddiad cyfan (cod, dibyniaethau, seilwaith, a data ffurfweddiad), nid dim ond ffynhonnell.
- Mae llinellau sylfaen yn bwyntiau cyfeirio anghyfnewidiol; mae newid yn cael ei awdurdodi a'i gofnodi yn eu herbyn, nid ei atal.
- Rhaid i gyfrifo statws eich galluogi i ateb, ar unrhyw eiliad, beth sydd mewn rhyddhad a sut y cyrhaeddodd yno.
- Mae archwiliadau'n gwirio bod yr hyn a adeiladwyd ac a draddodwyd yn cyfateb i'r ffurfweddiad cofnodedig a'r gofynion cymeradwy.
- Haenwch reolaeth yn ôl risg ac awtomeiddiwch adnabod, cyfrifo, ac archwilio fel bod y cofnod yn sgil-gynnyrch traddodiad.

## Cyfeiriadau a darllen pellach

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, maes gwybodaeth Rheolaeth Ffurfweddiad Meddalwedd
- IEEE Std 828, *Standard for Configuration Management in Systems and Software Engineering*
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (proses rheolaeth ffurfweddiad)
- Jez Humble a David Farley, *Continuous Delivery*
- Bob Aiello a Leslie Sachs, *Configuration Management Best Practices: Practical Methods that Work in the Real World*
- Canllawiau NIST ar ddiogelwch cadwyn gyflenwi meddalwedd, biliau deunyddiau meddalwedd (SBOM), a tharddiad arteffact
- CNCF a safonau agored ar gyfer tarddiad adeiladu a thystiad (fel fframweithiau cyfeirnod)
