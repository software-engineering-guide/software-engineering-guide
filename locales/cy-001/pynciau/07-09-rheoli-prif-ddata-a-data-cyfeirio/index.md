# 7.9 Rheoli data meistr a data cyfeirio

## Trosolwg a chymhelliant

Gofynnwch i bum system faint o gwsmeriaid sydd gan y sefydliad, a chewch bum rhif gwahanol. Mae un yn cyfrif cyfeiriadau e-bost, mae un yn cyfrif contractau, mae un yn cyfrif mewngofnodion, ac mae dwy'n anghytuno ynghylch ai'r un cwmni yw "Acme Corp" ac "ACME Corporation". [Rheoli data meistr](https://en.wikipedia.org/wiki/Master_data_management) (MDM) yw'r ddisgyblaeth o gymodi'r endidau craidd y mae eich busnes yn eu rhannu ( cwsmer, cynnyrch, cyflenwr, cyflogai, lleoliad ) yn un fersiwn awdurdodol y gall pob system ymddiried ynddi.

Dechreuwch drwy ddidoli eich data'n dri math, oherwydd mae angen triniaeth wahanol arnynt. Mae data meistr yn disgrifio enwau'r busnes: y bobl, y lleoedd, a'r pethau y mae llawer o brosesau'n cyfeirio atynt. Data cyfeirio yw'r eirfa reoledig y mae'r prosesau hynny'n ei defnyddio: codau arian cyfred, codau gwlad, rhestrau uned-mesur, categorïau cynnyrch. Mae data trafodiad yn cofnodi'r berfau: archeb wedi'i gosod, taliad wedi'i wneud, llwyth wedi'i anfon. Mae data meistr a data cyfeirio'n gyfaint is na thrafodion ond yn cael eu cyfeirio atynt ym mhobman, felly mae gwall ynddynt yn heintio popeth i lawr yr afon.

Mae cost cael hyn yn anghywir yn ddiriaethol. Pan fydd yr un cwsmer yn bodoli fel pedwar cofnod ychydig yn wahanol, rydych yn postio pedwar catalog, ni allwch weld un berthynas sy'n werth ei chadw, ac mae eich ffigur refeniw-fesul-cwsmer yn anghywir yn dawel. [Cofnod aur](https://en.wikipedia.org/wiki/Single_source_of_truth), yr un fersiwn ddibynadwy o endid wedi'i chydosod o lawer o ffynonellau, yw'r hyn sy'n disodli'r copïau anghyson hynny, fel bod pob integreiddiad yn stopio ail-ddatrys yr un broblem baru.

I fentrau sy'n cymodi systemau a gronnwyd dros ddegawdau o dwf a chaffael, MDM yw'r gwahaniaeth rhwng golwg gydlynol ar gwsmeriaid a threth cymodi barhaol. I lywodraeth, mae'r peryglon yn codi: gall dinesydd sy'n ymddangos fel tri pherson gwahanol mewn tair asiantaeth gael ei wrthod budd-dal, ei drethu ddwywaith, neu ei golli rhwng adrannau. Mae'r bennod hon yn ategu strategaeth a llywodraethu data (pennod 7.1), sy'n gosod perchnogaeth a pholisi; modelu data a'r haen semantig (pennod 7.7), sy'n diffinio beth mae endidau'n ei olygu; ac ansawdd data ac arsylladwyedd (pennod 7.8), sy'n cadw cofnodion yn lân dros amser.

## Egwyddorion allweddol

- Didolwch eich data'n feistr, cyfeirio, a thrafodiad; mae angen triniaeth wahanol ar bob un.
- Un cofnod aur fesul endid go iawn, wedi'i gydosod yn fwriadol, nid ei ddarganfod ar hap.
- Dewiswch arddull bensaernïaeth MDM i ffitio eich anghenion rheolaeth ac oedi, nid ffasiwn.
- Rheolau busnes yw paru a goroesiad, felly ysgrifennwch nhw i lawr a gadewch i stiwardiaid eu tiwnio.
- Eirfa a rennir yw data cyfeirio; fersiynwch a chyhoeddwch ef fel API.
- Llywodraethu a stiwardiaeth yw peiriant MDM; dim ond yr offer yw'r feddalwedd.
- Lledaenwch gofnodion aur fel digwyddiadau fel bod systemau i lawr yr afon yn aros yn gyfredol, nid yn hen.
- Mesurwch MDM yn ôl penderfyniadau wedi'u gwella a dyblygiadau wedi'u dileu, nid yn ôl cofnodion wedi'u llwytho.

## Argymhellion

### Dosbarthwch ddata meistr, cyfeirio, a thrafodiad yn gyntaf

Ni allwch reoli'r hyn nad ydych wedi'i ddidoli, felly dechreuwch drwy ddosbarthu eich parthau data. Prawf defnyddiol ar gyfer data meistr yw a yw gwerth anghywir yn lledaenu: os yw un cyfeiriad gwael yn ymledu i mewn i filio, cludo, a hysbysiadau cyfreithiol, rydych yn edrych ar ddata meistr. Mae hyn yn llywio eich buddsoddiad: rydych yn adeiladu peiriant paru ar gyfer yr endid cwsmer, nid eitemau llinell archeb. Enwch y parthau'n benodol, rhestrwch nhw yn ôl faint o boen y mae eu dyblygu'n ei achosi, a dechreuwch gyda'r un neu ddau sy'n brifo fwyaf, fel arfer cwsmer a chynnyrch am eu bod yn cyffwrdd refeniw'n uniongyrchol.

### Dewiswch arddull bensaernïaeth MDM yn fwriadol

Mae pedair arddull bensaernïaeth gyffredin, ac mae'r un gywir yn dibynnu ar faint o awdurdod y gallwch ei ganoli a pha mor gyflym y mae'n rhaid i newidiadau ledaenu. Mae'r arddull cofrestrfa'n gadael data yn y systemau ffynhonnell ac yn adeiladu dim ond mynegai o ddynodwyr wedi'u paru, fel y gall ateb "mae'r pum cofnod hyn yr un cwsmer" heb symud unrhyw ddata; mae'n rhad ac yn risg isel, ond yn ddarllen-yn-unig, felly ni all drwsio'r ffynonellau. Mae'r arddull cyfuno'n tynnu copïau i mewn i hyb canolog ac yn eu huno'n gofnodion aur ar gyfer adrodd, ond nid yw'n gwthio cywiriadau'n ôl, felly mae'r ffynonellau'n aros yn flêr. Mae'r arddull cydfodolaeth yn mynd ymhellach: mae'n cydamseru gwerthoedd wedi'u glanhau'n ôl i'r systemau ffynhonnell, fel bod y ffynonellau'n gwella dros amser tra'n dal i weithredu'n annibynnol. Mae'r arddull hyb canolog neu drafodiadol yn gwneud yr hyb MDM ei hun yn system y cofnod, lle mae endidau'n cael eu creu a'u golygu'n uniongyrchol a phob system arall yn defnyddio ohono; mae hyn yn rhoi'r cysondeb a'r rheolaeth cryfaf, ac mae'n anoddaf i'w fabwysiadu am ei fod yn newid ble mae gwaith yn digwydd. Mae llawer o sefydliadau'n symud o gofrestrfa sy'n profi gwerth tuag at gydfodolaeth wrth i ymddiriedaeth dyfu, ac yn rhedeg mwy nag un arddull ar draws parthau gwahanol.

### Parwch, unwch, a gosodwch reolau goroesiad yn benodol

Calon MDM yw penderfynu pryd mae dau gofnod yn disgrifio'r un peth go iawn. Dyma [gysylltu cofnodion](https://en.wikipedia.org/wiki/Record_linkage), sy'n anaml mor syml â pharu allwedd union oherwydd bod data go iawn yn llawn camsillafiadau, byrfoddau, a meysydd coll. Mae paru penderfynol yn defnyddio rheolau union ar feysydd dewisedig (yr un ID treth, neu'r un e-bost ynghyd â chod post). Mae paru tebygolaidd yn sgorio tebygrwydd ar draws llawer o feysydd gan ddefnyddio [paru llinynnau bras](https://en.wikipedia.org/wiki/Approximate_string_matching) a phwysau, fel y gellir barnu bod "Bob Smith, 12 Main St" a "Robert Smith, 12 Main Street" yn debygol o baru uwchlaw trothwy. Gelwir penderfynu pa gofnodion sy'n cyfeirio at yr un endid yn ddatrys hunaniaeth, ac mae'n pweru popeth o olygfeydd cwsmer i ganfod twyll.

Unwaith y bydd cofnodion yn paru, rhaid i chi benderfynu pa werthoedd sy'n goroesi i mewn i'r cofnod aur. Rheolau busnes yw'r rheolau goroesiad hyn, felly gwnewch nhw'n benodol: ffafriwch y gwerth mwyaf diweddar ar gyfer rhif ffôn, y gwerth mwyaf cyflawn ar gyfer cyfeiriad, y ffynhonnell fwyaf dibynadwy ar gyfer enw cyfreithiol. Gosodwch fand trothwy lle mae parau'n cael eu huno'n awtomatig, band is lle maent yn cael eu gwrthod yn awtomatig, a band canol lle mae dynol yn penderfynu, sef lle mae stiwardiaeth yn byw. Cadwch bob uniad yn wrthdroadwy ac wedi'i gofnodi, oherwydd mae uniad anghywir sy'n cyfuno dau gwsmer go iawn yn waeth nag un a gollwyd.

### Trinwch ddata cyfeirio fel eirfa a rennir, wedi'i fersiynu

Data cyfeirio yw'r eirfa a rennir y mae eich systemau'n ei siarad, ac mae eirfa sy'n crwydro'n achosi camaliniad distaw: pan fydd un system yn defnyddio cod gwlad ISO "GB" ac un arall yn defnyddio "UK," mae uniadau'n methu ac mae cyfrifon yn gwahaniaethu. Cynhaliwch bob rhestr gyfeirio mewn un lle a lywodraethir, cyhoeddwch ef ar gyfer pob defnyddiwr, ac, yn hollbwysig, fersiynwch ef. Mae codau'n cael eu hychwanegu, eu tynnu'n ôl, eu rhannu, a'u huno dros amser, ac os byddwch yn trosysgrifo'r rhestr yn ei lle, rydych yn torri adroddiadau hanesyddol a oedd yn gywir o dan yr hen godau.

Trinwch set ddata gyfeirio fel API gyda chytundeb. Cyhoeddwch ef gyda dyddiadau dilys fel y gall defnyddiwr ofyn "beth oedd y codau rhanbarth dilys ar y dyddiad hwn," cadwch godau wedi'u tynnu'n ôl yn hytrach na'u dileu, a chofnodwch y mapio pan fydd cod yn newid ystyr. Ffafriwch safonau allanol cydnabyddedig lle maent yn bodoli, megis codau gwlad ac arian cyfred ISO, oherwydd mae safonau'n rhoi rhyngweithredu i chi am ddim ac yn cysylltu â disgyblaeth safonau agored pennod 3.8.

### Modelwch hierarchaethau a pherthnasoedd, nid dim ond cofnodion gwastad

Nid pentwr o resi annibynnol yw data meistr; mae'n we o berthnasoedd. Mae cwsmer yn perthyn i aelwyd ac i riant corfforaethol. Mae cynnyrch yn cronni i fyny i mewn i gategori a brand. Mae'r hierarchaethau hyn yn cario ystyr busnes go iawn: cronnwch werthiannau yn ôl rhiant corfforaethol ac mae'r darlun yn newid yn llwyr o gronni yn ôl cyfrif unigol. Modelwch y perthnasoedd hyn yn benodol fel bod defnyddwyr yn eu croesi'n gyson yn lle bod pob tîm yn dyfeisio ei gronniad ei hun.

Gwyliwch am yr achos lle mae angen sawl hierarchaeth ar endid ar unwaith. Gall cynnyrch gronni un ffordd ar gyfer cyllid a ffordd arall ar gyfer masnacheiddio, ac mae'r ddwy'n ddilys, felly cefnogwch sawl hierarchaeth wedi'i henwi yn hytrach na gorfodi un goeden wir. Mae perthnasoedd rhwng parthau'n bwysig hefyd, megis pa gyflenwr sy'n darparu pa gynnyrch.

### Cysylltwch gofnodion aur â'r haen semantig ac ansawdd data

Y cofnodion aur y mae MDM yn eu cynhyrchu yw'r endidau dibynadwy y mae'r haen semantig ym mhennod 7.7 yn cyfeirio atynt wrth ddiffinio metrigau: dim ond pan fydd "cwsmer" yn ddiamwys y mae "cwsmeriaid gweithredol" yn golygu unrhyw beth. Bwydwch eich cofnodion aur i mewn i'r haen semantig fel bod pob metrig yn cyfrif yr un endidau wedi'u dad-ddyblygu, wedi'u datrys.

Mae MDM ac ansawdd data (pennod 7.8) yn ddwy ochr i'r un geiniog: mae gwiriadau ansawdd yn canfod y dyblygiadau, y gwerthoedd nwl, a'r toriadau fformat y mae MDM wedyn yn eu datrys, ac mae paru MDM yn dod â phroblemau ansawdd na welodd y gwiriadau i'r wyneb. Rhedwch fonitro ansawdd parhaus ar eich data meistr yn benodol: cyfraddau dyblygu, dosraniadau hyder paru, cyflawnrwydd meysydd allweddol, a maint y ciw adolygu, fel bod crwydro'n dod i'r wyneb cyn i ddefnyddwyr ei weld.

### Lledaenwch gofnodion aur drwy ddigwyddiadau

Nid yw cofnod aur nad oes unrhyw system i lawr yr afon yn ei weld o help i neb. Y patrwm cryfaf yw lledaeniad wedi'i yrru gan ddigwyddiadau: pan fydd endid yn cael ei greu, ei uno, neu ei gywiro, mae'r hyb MDM yn cyhoeddi digwyddiad newid, ac mae systemau sy'n tanysgrifio'n diweddaru eu copi lleol. Mae hyn yn adeiladu ar [bensaernïaeth wedi'i gyrru gan ddigwyddiadau](https://en.wikipedia.org/wiki/Event-driven_architecture) a phatrymau ffrydio pennod 7.2, gan gadw dwsinau o systemau'n gyson heb gydamseriadau swp dros nos brau sy'n gadael pawb ddiwrnod yn hen.

Cyhoeddwch y digwyddiadau gyda digon o gyd-destun i fod yn ddefnyddiol: dynodwr yr endid, beth newidiodd, y gwerthoedd goroesol newydd, a fersiwn fel y gall defnyddwyr drefnu diweddariadau a chanfod rhai y gwnaethant eu colli. Gwnewch ddefnyddwyr yn idempotent fel nad yw ailchwarae digwyddiad yn gwneud niwed, a chynigiwch API ar gyfer systemau na allant danysgrifio. Mae'r egwyddor o bensaernïaeth a storio data (pennod 3.4) yn berthnasol: cynlluniwch i'r cofnod aur lifo, oherwydd nid yw un nad oes neb yn ei ddefnyddio ond yn daenlen ddrud.

### Neilltuwch stiwardiaeth a llywodraethu cyn offer

Mae MDM yn methu fel prosiect technoleg ac yn llwyddo fel un llywodraethu. Y rôl allweddol yw'r [stiward data](https://en.wikipedia.org/wiki/Data_steward), person sy'n atebol am ansawdd a rheolau parth penodol, sy'n datrys parau amwys, yn tiwnio rheolau goroesiad, ac yn cyflafareddu pan fydd dwy adran yn anghytuno ynghylch beth mae "cyflenwr" yn ei olygu. Mae stiwardiaid fel arfer yn bobl fusnes gyda gwybodaeth barth ddofn, nid peirianwyr, ac mae angen awdurdod amser go iawn arnynt wedi'i neilltuo, oherwydd mae stiwardiaeth ran-amser heb fandad yn cynhyrchu union y crwydro yr oedd MDM i fod i'w atal.

Lapiwch y stiwardiaid yn strwythurau llywodraethu pennod 7.1: perchennog data'n atebol am bob parth, cyngor i setlo anghydfodau traws-barth, a pholisïau clir ar gyfer pwy sy'n cael creu neu uno cofnodion meistr. Dogfennwch y penderfyniadau, oherwydd mae'r rheolau ar gyfer paru cwsmer yn wybodaeth sefydliadol y mae'n rhaid iddi oroesi trosiant staff. Mae offer yn gwasanaethu'r llywodraethu; mae prynu platfform MDM cyn enwi eich stiwardiaid yn brynu peiriant heb yrrwr.

## Cyfaddawdau: manteision ac anfanteision

| Arddull MDM | Manteision | Anfanteision |
|---|---|---|
| Cofrestrfa (mynegai'n unig) | Rhad, risg isel, ffynonellau heb eu cyffwrdd | Darllen-yn-unig; ni all drwsio data ffynhonnell |
| Cyfuno (copïau canolog) | Cofnodion glân ar gyfer dadansoddeg yn gyflym | Ffynonellau'n aros yn flêr; dim ysgrifennu'n ôl |
| Cydfodolaeth (cydamseru'n ôl i'r ffynonellau) | Ffynonellau'n gwella; rheolaeth gytbwys | Mwy o integreiddio; gwrthdrawiadau cydamseru i'w rheoli |
| Hyb canolog / trafodiadol | Cysondeb a rheolaeth cryfaf | Cost uchaf; yn newid ble mae gwaith yn digwydd |
| Paru penderfynol | Rhagweladwy, esboniadwy, archwiliadwy | Yn colli camsillafiadau, amrywiadau, a data blêr |
| Paru tebygolaidd | Yn dal amrywiad go iawn | Angen tiwnio; uniadau anghywir os yn ddi-ofal |

Y prif densiwn mewn MDM yw rheolaeth yn erbyn tarfu. Y harddulliau sy'n rhoi'r data glanaf, mwyaf cyson (cydfodolaeth a hybiau canolog) yw'n union y rhai sy'n tarfu fwyaf ar sut mae systemau ffynhonnell a'u perchnogion yn gweithio, a dyna lle mae rhaglenni MDM yn stolio. Y llwybr pragmataidd yw ennill ymddiriedaeth gydag arddull risg isel a symud tuag at reolaeth gryfach dim ond lle mae'r achos busnes yn glir. Mae'r cyfaddawd paru'n rhedeg yn gyfochrog: mae rheolau penderfynol yn archwiliadwy ond yn frau, mae sgorio tebygolaidd yn bwerus ond mae angen stiwardiaeth a goddefgarwch am uniad anghywir achlysurol. Mae'r rhan fwyaf o raglenni aeddfed yn cymysgu'r ddau.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Pa barthau data meistr sydd wir yn achosi poen i ni, ac a ydym wedi'u rhestru yn ôl cost yn hytrach na'u trin i gyd ar unwaith?** Mae llawer o raglenni MDM yn cwympo o dan eu huchelgais eu hunain, gan geisio meistroli pob endid yn y fenter ar unwaith a chyflenwi dim am ddwy flynedd. Y symudiad cynhyrchiol yw dod o hyd i'r un neu ddau barth lle mae dyblygu a gwrthdaro'n costio arian neu ymddiriedaeth go iawn i chi, fel arfer cwsmer neu gynnyrch, a meintioli'r gost honno: y postiadau gwastraffedig, yr oriau cymodi, y ffigurau refeniw anghywir, y canfyddiadau archwilio. Dewch ag enghreifftiau pendant o'r un endid yn ymddangos sawl ffordd ar draws eich systemau, a gadewch i'r rhestriad honno ddweud wrthych ble i ddechrau, oherwydd mae buddugoliaeth gul, fesuradwy'n adeiladu'r hygrededd sydd ei angen arnoch i ehangu.

2. **Pwy sy'n berchen ar bob parth data meistr, ac a oes gan ein stiwardiaid yr awdurdod a'r amser i wneud y gwaith go iawn?** Mae offer MDM heb stiwardiaeth wedi'i grymuso'n gar heb yrrwr, a'r modd methiant mwyaf cyffredin yw enwi stiward ar sleid tra'n rhoi dim mandad go iawn a dim oriau wedi'u neilltuo iddynt. Mae angen arbenigedd parth, awdurdod penderfynu, ac amser wedi'i warchod ar y bobl sy'n datrys parau amwys ac yn setlo anghydfodau "beth sy'n cyfrif fel cwsmer". Dewch â'ch siart sefydliadol a gofynnwch, ar gyfer eich prif barth, pwy'n union sy'n penderfynu pryd mae dau gofnod yr un person a phwy sy'n cyflafareddu pan fydd gwerthiant a chyllid yn anghytuno. Os na allwch enwi'r person hwnnw a phwyntio at eu hamser neilltuedig, rydych wedi dod o hyd i'r bwlch a fydd yn suddo'r rhaglen.

3. **Pan fyddwn yn uno dau gofnod yn gofnod aur, allwn ni esbonio a gwrthdroi'r penderfyniad, a o ble mae'r gwerthoedd goroesol yn dod?** Rheolau busnes yw rheolau goroesiad nad yw'r rhan fwyaf o dimau erioed wedi'u hysgrifennu i lawr, sy'n golygu bod uniadau'n digwydd ar hap trefn llwytho neu ddiofynion offer, ac mae uniad anghywir sy'n cyfuno dau gwsmer go iawn yn boenus i'w ddadwneud. Dewch â chofnod wedi'i uno go iawn ac olrheiniwch bob maes goroesol yn ôl i'w ffynhonnell a'i reol: pam y cyfeiriad hwn, pam yr enw hwn, pam y rhif ffôn hwn. Cadarnhewch fod pob uniad wedi'i gofnodi a'n wrthdroadwy, a bod band canol o barau ansicr yn mynd at ddynol yn hytrach na chael eu huno'n awtomatig. Os na allwch esbonio cofnod aur penodol, ni all eich stiwardiaid ei amddiffyn i archwiliwr na chwsmer a gamwybodwyd.

4. **Pa arddull bensaernïaeth MDM sy'n ffitio pob parth rydym yn bwriadu ei feistroli, ac a allwn amddiffyn y dewis hwnnw yn erbyn y tarfu y mae'n ei osod ar berchnogion systemau ffynhonnell?** Mae'r arddull rydych yn ei ddewis yn penderfynu faint y gallwch lanhau'r data a faint rydych yn tarfu ar y timau sy'n berchen ar y ffynonellau, ac mae dewis yn ôl ffasiwn neu draethiad gwerthwr yn hytrach na realiti rheolaeth-yn-erbyn-tarfu yw sut mae rhaglenni'n stolio hanner ffordd. Mae cofrestrfa'n profi gwerth yn rhad ond byth yn trwsio ffynhonnell; mae hyb canolog yn rhoi'r cysondeb cryfaf ond yn adleoli ble mae cofnodion yn cael eu creu, sy'n newid sefydliadol wedi'i guddio fel un technegol. Dewch, ar gyfer pob parth ymgeisiol, â darlleniad gonest ar faint o awdurdod sydd gennych mewn gwirionedd dros berchnogion y ffynhonnell, pa mor ffres y mae'n rhaid i gopïau i lawr yr afon fod, a beth y byddai ysgrifennu'n ôl yn ei dorri mewn llifau gwaith presennol. Mewn lleoliadau menter a llywodraeth, ychwanegwch gost mudo a rheoli newid symud system y cofnod, oherwydd bydd y timau y mae eu gwaith dyddiol yn symud yn gwrthwynebu hyb na chawsant eu hymgynghori amdano, ac mae cyflwyniad cydfodolaeth wedi'i stolio'n ddrutach na chofrestrfa gymedrol sy'n cyflenwi.

5. **Sut rydym yn tiwnio'r trothwyon paru, ac a ydym wedi cytuno pa gyfradd o uniadau anghywir a pharau coll y gallwn fyw â nhw ym mhob parth?** Mae pob peiriant paru tebygolaidd yn cyfnewid uniadau anghywir (cyfuno dau endid go iawn) yn erbyn parau coll (gadael un endid wedi'i hollti), ac mae'r cydbwysedd yn benderfyniad busnes, nid diofyn a adawodd rhywun yn yr offer. Gosodwch y bandiau uno-awtomatig a gwrthod-awtomatig yn rhy eang a byddwch yn llygru cofnodion aur yn dawel; gosodwch nhw'n rhy gul a bydd y ciw adolygu dynol yn tyfu'n gyflymach nag y gall stiwardiaid ei glirio. Dewch â'r dosraniad hyder presennol, maint ac oedran y ciw adolygu, a sampl o wallau o'r ddau fath fel y gall yr ystafell weld gwir gost pob cyfeiriad. Mewn parth hunaniaeth llywodraeth, gwyrwch yn galed tuag at barau coll ac adolygiad dynol, oherwydd gall uniad anghywir wrthod budd-dal neu ddatgelu data un dinesydd i un arall, ac mae cost apêl ac archwilio'r gwall hwnnw'n gwneud i gost dyblygiad y mae stiward yn ei ddatrys yr wythnos nesaf ymddangos yn fach.

6. **Sut mae systemau i lawr yr afon yn dysgu bod cofnod aur wedi newid, a pha mor hen y gall pob un fod cyn i benderfyniad fynd o chwith?** Mae cofnod aur wedi'i ddatrys yn berffaith nad oes unrhyw system yn ei ddefnyddio'n daenlen ddrud, ac mae'r mecanwaith lledaenu, boed yn ddigwyddiadau newid, API tanysgrifio, neu swp nos, yn gosod yn dawel pa mor gyfredol yw pob penderfyniad dibynnol. Mae lledaeniad wedi'i yrru gan ddigwyddiadau'n cadw dwsinau o ddefnyddwyr bron yn amser real ond mae'n mynnu defnyddwyr idempotent a digwyddiadau wedi'u fersiynu; mae cydamseriad nos yn symlach ond yn gadael pawb ddiwrnod yn hen, a all fod yn iawn ar gyfer rhestr farchnata ac yn beryglus ar gyfer gwiriad twyll. Dewch â rhestr y systemau sy'n defnyddio, y ffresni y mae pob un ei angen mewn gwirionedd, a sut mae defnyddiwr sy'n colli diweddariad heddiw'n adfer. I sefydliad mawr neu gyhoeddus, enwch pwy sy'n berchen ar y cytundeb ar gyfer y digwyddiadau hyn a sut mae tanysgrifiwr yn canfod neges a ollyngwyd, oherwydd mae newid endid sy'n methu'n dawel â chyrraedd un asiantaeth yn ailgreu union y darniad y cafodd MDM ei ariannu i'w ddileu.

## Lens sector

**Cwmni newydd.** Gyda llond dwrn o beirianwyr a dim gofod anadlu i'w sbario, peidiwch â phrynu platfform MDM. Meistrolwch yr un endid sy'n llygru eich rhifau, fel arfer y cwsmer wedi'i ddyblygu ar draws hunanwasanaeth a gwerthiant, gyda gwaith paru yn y warws rydych eisoes yn ei redeg ac un person yn adolygu parau ansicr yn wythnosol. Cadwch bob uniad wedi'i gofnodi a'n wrthdroadwy fel bod rheol wael yn costio prynhawn, nid perthynas cwsmer, ac ailedrychwch ar offer trymach dim ond pan fydd y ciw adolygu â llaw yn tyfu y tu hwnt i un adolygydd.

**Busnes bach.** Nid oes gennych stiward data a chyllideb dynn, felly triniwch hyn fel penderfyniad prynu-nid-adeiladu a phwyswch ar safonau a gewch am ddim. Ffafriwch offer sydd eisoes yn dad-ddyblygu cysylltiadau ac yn siarad codau gwlad ac arian cyfred ISO yn hytrach na hyb pwrpasol na allwch ei gynnal, a dewiswch un parth, cwsmeriaid neu gynhyrchion fel arfer, lle mae dyblygiadau'n costio arian go iawn i chi. Neilltuwch yr atebolrwydd i berchennog wedi'i enwi hyd yn oed os yw'n ffracsiwn o wythnos un person, oherwydd eirfa sy'n crwydro heb i neb wylio yw'r hyn sy'n torri eich adroddiadau'n dawel.

**Menter.** Ar draws dwsin o systemau ERP a CRM a gronnwyd drwy gaffael, y gwaith yw llywodraethu portffolio: rhestrwch barthau yn ôl cost eu dyblygu, sefydlwch stiwardiaid grymusedig yn y busnes, a safonwch reolau goroesiad a fersiynu data cyfeirio fel bod grwpiau'n stopio ail-ddatrys yr un broblem baru. Cyllidebwch gost integreiddio a stiwardiaeth barhaol yn benodol, lledaenwch gofnodion aur fel digwyddiadau wedi'u fersiynu fel bod ffynonellau'n gwella dros amser, a rheolwch MDM fel rhaglen a fesurir gyda chyfraddau dyblygu a metrigau ciw adolygu yn hytrach na glanhad untro.

**Llywodraeth.** Mae rheolau caffael, cyfraith rhannu data lem, ac atebolrwydd cyhoeddus yn siapio pob dewis. Allweddwch yr endid person ar ddynodwr cenedlaethol a lywodraethir, fersiynwch ddata cyfeirio yn ôl dyddiad dilys fel bod cofnodion hanesyddol yn aros yn gywir, a gwnewch ddatrys hunaniaeth yn fwriadol geidwadol: mae parau ansicr yn mynd at stiwardiaid wedi'u hyfforddi, byth uniadau awtomataidd, oherwydd gall uniad anghywir wrthod budd-dal neu ollwng data un dinesydd i un arall. Cofnodwch bob paru ar gyfer archwilio ac apêl, mynnwch gludadwyedd data a rhesymeg baru wedi'i datgelu gan werthwyr, a chadwch y gallu cyfan o fewn y safonau rhyngweithredu y mae'r sector cyhoeddus eisoes wedi ymrwymo iddynt.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni meddalwedd sy'n tyfu'n gyflym yn gwerthu drwy hunanwasanaeth a thîm gwerthiant, ac mae'r ddwy sianel yn creu'r un cwsmer ddwywaith o dan enwau cwmni ychydig yn wahanol. Mae refeniw-fesul-cyfrif yn edrych yn anghywir ac mae'r tîm gwerthiant yn parhau i alw defnyddwyr presennol yn oer. Yn hytrach na phrynu platfform trwm, maent yn dechrau gyda chofrestrfa ysgafn: gwaith paru yn eu warws data sy'n cysylltu cofnodion yn ôl parth e-bost ac enw cwmni wedi'i normaleiddio, gydag un stiward rhan-amser yn adolygu'r parau ansicr yn wythnosol. Mae'n costio ychydig, yn trwsio'r gwall adrodd, ac yn profi'r gwerth sy'n cyfiawnhau mwy o fuddsoddiad wrth iddynt dyfu.

**Menter.** Mae gwneuthurwr byd-eang wedi tyfu drwy gaffael ac yn rhedeg dwsin o systemau ERP a CRM, pob un â'i gofnodion cyflenwr ei hun, felly mae'r un cyflenwr yn ymddangos bymtheg ffordd ac ni all y cwmni negodi fel un prynwr na gweld ei wir wariant. Mae'n sefydlu hyb MDM ar arddull cydfodolaeth ar gyfer parthau cyflenwr a chynnyrch, gan ddefnyddio paru penderfynol ar ddynodwyr treth a chofrestru ynghyd â sgorio tebygolaidd ar enwau a chyfeiriadau. Mae stiwardiaid wedi'u henwi mewn caffael yn tiwnio'r rheolau goroesiad ac yn gweithio'r ciw adolygu, a chyhoeddir cofnodion aur fel digwyddiadau newid sy'n llifo'n ôl i mewn i bob ERP fel bod data glân yn gwella'r ffynonellau. Mae gwelededd gwariant cyfunol yn datgloi telerau contract gwell, ac mae'r dreth gymodi a oedd yn treulio cyllid bob chwarter yn cwympo'n sydyn.

**Llywodraeth.** Mae llywodraeth genedlaethol eisiau i asiantaethau drin dinesydd fel un person yn hytrach na dieithryn ym mhob cownter, tra'n parchu terfynau cyfreithiol llym ar rannu data. Mae'n adeiladu hyb data meistr canolog ar gyfer yr endid person, wedi'i allweddi ar ddynodwr cenedlaethol a lywodraethir, gyda data cyfeirio wedi'i fersiynu yn ôl dyddiad dilys fel bod cofnodion hanesyddol yn aros yn gywir. Mae datrys hunaniaeth yn fwriadol geidwadol: mae parau ansicr yn mynd at stiwardiaid wedi'u hyfforddi yn hytrach nag uniadau awtomataidd, oherwydd gallai uniad anghywir wrthod budd-dal i rywun neu ddatgelu eu data, a chofnodir pob paru ar gyfer archwilio ac apêl. Y budd yw llai o gofnodion dyblyg, llai o dwyll o hunaniaethau hollt, a dinesydd nad oes rhaid iddo brofi pwy ydyw wrth bob drws, o fewn safonau rhyngweithredu pennod 3.8.

## Achos busnes: cymhellion, ROI, a TCO

Daw'r enillion ar MDM o gael gwared ar dreth y mae'r rhan fwyaf o sefydliadau'n ei thalu heb ei henwi. Mae cofnodion dyblyg a gwrthdrawiadol yn costio arian mewn ffyrdd amlwg (marchnata gwastraffedig i'r un person bum gwaith, gwallau cludo o gyfeiriadau hen, disgowntiau cyfaint a gollwyd) ac mewn ffyrdd llai amlwg (dadansoddwyr yn cymodi cyfrifon, cyfarwyddwyr yn penderfynu ar rifau sy'n anghywir yn dawel, archwilwyr yn bilio oriau i ddatod pa gofnod sy'n go iawn). Mae golwg cyflenwr cyfunol yn aml yn talu am y rhaglen gyfan drwy delerau contract gwell yn unig.

Mae gan gyfanswm cost perchnogaeth dair rhan: y platfform neu'r adeiladu, yr integreiddio i ffynonellau a defnyddwyr, a'r fwyaf dros amser, y stiwardiaeth barhaus. Mae'r gost integreiddio'n hawdd ei danamcangyfrif, oherwydd cysylltu dwsin o systemau ffynhonnell hynafol yw lle mae rhaglenni MDM yn gwaedu amserlen a chyllideb, ac mae'r gost stiwardiaeth yn hawdd ei anghofio, oherwydd ei bod yn draul weithredu barhaol, nid adeiladu untro. I wneud yr achos i arweinyddiaeth, cysylltwch MDM â rhifau y maent eisoes yn eu tracio: cywirdeb refeniw, effeithlonrwydd marchnata, arbedion caffael, cost archwilio, a risg reoleiddiol, yna dechreuwch yn gul a gadewch i fuddugoliaeth fesuradwy ar un parth poenus ariannu'r ehangu.

## Gwrth-batrymau a pheryglon

- **Cwmpas berwi'r-cefnfor:** meistroli pob parth ar unwaith, cyflenwi dim am flynyddoedd, a cholli nawdd cyn y fuddugoliaeth gyntaf.
- **Offer cyn llywodraethu:** prynu platfform MDM cyn enwi stiwardiaid a pherchnogion, fel bod gan y peiriant ddim gyrrwr.
- **Stiwardiaid rhan-amser heb awdurdod:** neilltuo stiwardiaeth ar sleid tra'n rhoi dim mandad go iawn na amser wedi'i warchod.
- **Goroesiad distaw:** uno cofnodion yn ôl diofyn offer neu drefn llwytho, heb reolau ysgrifenedig a heb ffordd o esbonio cofnod aur.
- **Uniadau na ellir eu gwrthdroi:** uno parau ansicr yn awtomatig heb ddadwneud, fel bod cyfuniad anghywir o ddau endid go iawn yn dod yn ddifrod parhaol.
- **Data cyfeirio wedi'i drosysgrifo yn ei le:** golygu rhestrau codau heb fersiynu, gan dorri pob adroddiad hanesyddol a oedd yn gywir o dan yr hen godau.
- **Cofnodion aur nad oes neb yn eu defnyddio:** adeiladu hyb pristin nad oes unrhyw system i lawr yr afon yn tanysgrifio iddo, fel nad yw'r data glân byth yn cyrraedd penderfyniadau.
- **Ailddyfeisio codau safonol:** bathu eich rhestrau gwlad neu arian cyfred eich hun pan fydd safonau ISO'n bodoli, a cholli rhyngweithredu heb reswm.

## Model aeddfedrwydd

- **Lefel 1, Cychwyn:** Nid yw data meistr a chyfeirio'n cael eu rheoli. Mae'r un endid yn bodoli sawl gwaith heb fersiwn awdurdodol, mae rhestrau codau'n gwahaniaethu, mae paru â llaw ac yn adweithiol, ac nid oes neb yn berchen ar y broblem, felly mae cyfrifon o endidau craidd yn anghytuno ac ni all neb ddweud pa un sy'n gywir.
- **Lefel 2, Datblygu:** Cydnabyddir parthau allweddol ac mae rhywun yn eu dad-ddyblygu, yn aml yn y warws ar gyfer adrodd. Mae paru penderfynol sylfaenol yn bodoli, casglwyd rhestrau cyfeirio, ac mae ychydig o bobl yn gweithredu fel stiwardiaid anffurfiol, ond mae'r arfer yn amrywio o dîm i dîm, mae'r ffynonellau'n aros yn flêr, ac mae rheolau'n byw ym mhennau pobl yn hytrach nag ar bapur.
- **Lefel 3, Safoni:** Mae MDM yn rhaglen a lywodraethir a gymhwysir yn gyson ar draws y sefydliad. Mae gan barthau meistr berchnogion wedi'u henwi a stiwardiaid grymusedig, mae rheolau paru a goroesiad wedi'u dogfennu a'u gorfodi, cynhyrchir cofnodion aur a'u lledaenu i ddefnyddwyr, a data cyfeirio wedi'i fersiynu a'i gyhoeddi gyda dyddiadau dilys fel API.
- **Lefel 4, Rheoli:** Mae'r rhaglen yn cael ei mesur a'i rheoli yn erbyn llinellau sylfaen. Olrheinir cyfraddau dyblygu, dosraniadau hyder paru, cyfraddau uniad anghywir a pharau coll, cyflawnrwydd meysydd allweddol, a maint ac oedran ciw adolygu fel metrigau; tiwnir trothwyon yn erbyn y rhifau hynny yn hytrach nag ar sail teimlad; a meintiolir gwerth MDM (cywirdeb refeniw, arbedion caffael, cost adolygu) a'i adrodd i berchnogion ar gadwyn sefydlog.
- **Lefel 5, Cyd-drefnu:** Mae cofnodion aur yn llifo fel digwyddiadau wedi'u fersiynu bron mewn amser real, yn bwydo'r haen semantig, ac yn cael eu hymddiried ynddynt ar draws y sefydliad. Gwellir paru'n barhaus yn erbyn canlyniadau wedi'u mesur, mae meistrolaeth yn ymestyn i barthau newydd fel gallu ailadroddadwy, ac mae MDM wedi'i integreiddio â chynllunio llywodraethu a risg fel bod y rhaglen yn addasu wrth i ffynonellau, safonau, a thirwedd endidau symud.

## Syniadau ar gyfer trafodaeth

1. Os yw dwy o'ch systemau'n anghytuno ynghylch faint o gwsmeriaid sydd gennych, pa un sy'n gywir, a sut y byddech yn ei brofi?
2. Pa barth data meistr fyddai'n cyflenwi'r fuddugoliaeth fesuradwy fwyaf pe baech yn ei feistroli'n gyntaf, a beth mae'r fuddugoliaeth honno'n werth?
3. Ble fyddai paru tebygolaidd yn eich helpu heddiw, ac a ydych yn gyfforddus â'r uniad anghywir achlysurol y mae'n ei awgrymu?
4. Sut rydych yn fersiynu eich data cyfeirio, a beth sy'n torri yn eich adroddiadau hanesyddol pan fydd cod yn newid ystyr?
5. Pwy yw'r stiward wedi'i enwi ar gyfer eich endid pwysicaf, ac a oes ganddynt yr awdurdod a'r amser i wneud y gwaith go iawn?
6. Pan fydd cofnod aur yn newid, sut mae eich systemau i lawr yr afon yn darganfod, a pha mor hen y gallant fod cyn iddo frifo?

## Prif negeseuon

- Didolwch eich data'n feistr, cyfeirio, a thrafodiad; buddsoddwch mewn paru a llywodraethu lle mae dyblygu'n costio fwyaf.
- Cynhyrchwch un cofnod aur fesul endid go iawn, wedi'i gydosod gan reolau goroesiad penodol, gwrthdroadwy, wedi'u cofnodi.
- Dewiswch arddull bensaernïaeth MDM (cofrestrfa, cyfuno, cydfodolaeth, neu hyb canolog) i ffitio eich awydd am reolaeth a tharfu.
- Trinwch ddata cyfeirio fel eirfa a rennir wedi'i fersiynu, ffafriwch safonau cydnabyddedig, a byth trosysgrifo rhestrau codau yn eu lle.
- Mae MDM yn llwyddo ar lywodraethu a stiwardiaeth, nid offer; lledaenwch gofnodion aur fel digwyddiadau a mesurwch y rhaglen yn ôl penderfyniadau wedi'u gwella.

## Cyfeiriadau a darllen pellach

- David Loshin, *Master Data Management*
- Alex Berson and Larry Dubov, *Master Data Management and Data Governance*
- Dan Power, *The Definitive Guide to Master Data Management*
- John Talburt, *Entity Resolution and Information Quality*
- Peter Christen, *Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection*
- Ivan P. Fellegi and Alan B. Sunter, "A Theory for Record Linkage," *Journal of the American Statistical Association*
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*
- Ralph Kimball and Margy Ross, *The Data Warehouse Toolkit*
