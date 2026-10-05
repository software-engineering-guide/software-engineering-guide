# 6.1 Strategaeth a pharodrwydd DA

## Trosolwg a chymhelliant

Mae [deallusrwydd artiffisial](https://en.wikipedia.org/wiki/Artificial_intelligence) wedi mynd o fod yn nofelti ymchwil i fod yn allu craidd y disgwylir bellach i sefydliadau mawr ei ddefnyddio'n gyfrifol ac ar raddfa. I fentrau ac asiantaethau llywodraeth, nid yw'r cwestiwn go iawn bellach a all DA wneud rhywbeth trawiadol mewn demo. Yn hytrach, a yw buddsoddiad penodol yn datrys problem go iawn yn well na'r dewisiadau amgen, y gellir ei weithredu'n ddiogel am flynyddoedd, ac a all oroesi archwiliad, caffael, a chraffu cyhoeddus. Strategaeth DA yw'r ddisgyblaeth o benderfynu ble i gymhwyso DA, ble i'w osgoi, a pha sylfeini sydd eu hangen arnoch cyn i'r model cyntaf gyrraedd cynhyrchu.

I dimau mawr, mae graddfa ac inertia'n codi'r peryglon. Gall menter wedi'i fframio'n wael losgi cyllidebau, tynnu sylw peirianwyr talentog, ac erydu ymddiriedaeth gyda rheoleiddwyr a dinasyddion pan fydd yn methu'n gyhoeddus. Gall un a ddewiswyd yn dda awtomeiddio gwaith undonog, dod ag mewnwelediad i'r wyneb o ddata na allech ei gyrraedd erioed o'r blaen, a rhyddhau pobl fedrus ar gyfer gwaith gwerth uwch. Anaml mai'r model ei hun yw'r gwahaniaeth. Mae'n dibynnu ar pa mor dda rydych yn fframio'r broblem, pa mor barod yw eich data a'ch talent, a pha mor onest yw eich achos busnes.

Mae cyd-destunau llywodraeth a rheoleiddiedig yn ychwanegu mwy o gyfyngiadau. Rhaid i gyrff cyhoeddus gyfiawnhau gwariant, gwarantu tryloywder, osgoi gwahaniaethu anghyfreithlon, ac aros yn atebol i swyddogion etholedig a'r cyhoedd. Gall rheolau caffael wahardd clymu un-ffynhonnell, mynnu esboniadwyedd, a mynnu bod gwerthwyr yn datgelu ymddygiad model. Yma, triniwch gydymffurfiaeth, archwiliadwyedd, a dewisiadau ymadael fel gofynion dosbarth cyntaf, nid ôl-ystyriaethau.

## Egwyddorion allweddol

- Dechreuwch o broblem sy'n werth ei datrys, nid o dechnoleg sy'n chwilio am ddefnydd.
- Ffafriwch y dull symlaf sy'n bodloni'r angen; mae DA yn un dewis ymhlith llawer, ac yn aml nid yr un gorau.
- Trinwch barodrwydd data, talent, ac aeddfedrwydd platfform fel rhagofynion, nid ffrydiau gwaith cyfochrog i'w datrys yn ddiweddarach.
- Gwnewch benderfyniadau adeiladu-yn-erbyn-prynu'n benodol ac ailedrychwch arnynt wrth i'r farchnad a'ch galluoedd newid.
- Meintiolwch gyfanswm cost perchnogaeth, gan gynnwys gweithredu, monitro, ac amnewid yn y pen draw, nid dim ond y drwydded neu'r peilot.
- Cynlluniwch ar gyfer ymadael o'r diwrnod cyntaf: osgowch bensaernïaethau sy'n gwneud newid gwerthwyr neu fodelau'n ddrud iawn.
- Mewn lleoliadau rheoleiddiedig a chyhoeddus, triniwch dryloywder, cydymffurfiaeth caffael, ac atebolrwydd fel cyfyngiadau cynllunio.
- Mesurwch gost *peidio â* gweithredu ochr yn ochr â chost gweithredu.

## Argymhellion

### Fframiwch y broblem cyn dewis technoleg

Ysgrifennwch ddatganiad problem un dudalen. Enwch y penderfyniad neu'r dasg rydych eisiau ei gwella, y llinell sylfaen bresennol, y canlyniad mesuradwy rydych ei eisiau, a beth sy'n digwydd pan fydd y system yn ei chael yn anghywir. Yna gofynnwch a yw'r broblem hyd yn oed yn addas ar gyfer DA. A oes digon o ddata perthnasol? A yw'r dasg yn seiliedig ar batrwm yn hytrach na rheol? A allwch oddef atebion tebygolaidd? A all dynol wirio'r allbwn? Mae llawer o broblemau'n cael eu datrys yn well gyda meddalwedd penderfynol, dylunio proses gwell, neu ddim ond hylendid data gwell. Ysgrifennwch i lawr yn benodol ble *nad* yw DA yn ffit da: er enghraifft, penderfyniadau y mae'n rhaid iddynt fod yn berffaith esboniadwy yn ôl y gyfraith, neu lle mae cost gwall prin yn drychinebus ac yn amhosibl ei ddal.

### Defnyddiwch goeden benderfynu adeiladu-yn-erbyn-prynu-yn-erbyn-fine-tune-yn-erbyn-prompt

Symudwch o'r rhataf a'r cyflymaf i'r drutaf a'r mwyaf rheoledig:

1. **Prompio model wedi'i letya sy'n bodoli.** Os yw model at ddiben cyffredinol (megis Claude gan Anthropic, neu gynigion cymharol gan ddarparwyr eraill) yn datrys y broblem gyda phrompio a adalw gofalus, gwnewch hynny'n gyntaf. Cost isaf, ailadrodd cyflymaf, dim seilwaith hyfforddi.
2. **Ychwanegwch adalw neu offer.** Os yw'r bwlch yn wybodaeth neu weithredoedd, ychwanegwch [genhedliad wedi'i ehangu gan adalw](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (RAG), sy'n nôl dogfennau perthnasol adeg ymholiad ac yn eu cyflenwi i'r model fel cyd-destun, a defnydd offer cyn cyffwrdd pwysau model.
3. **Fine-tune neu addasu.** Os na all prompio gyflawni'r cywirdeb, y dôn, neu'r fformat sydd ei angen yn gyson, [fine-tune](https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)) fodel llai ar eich data: hynny yw, hyfforddi ymhellach fodel wedi'i raghyfforddi ar eich enghreifftiau i'w arbenigo. Mae hyn yn prynu rheolaeth am gost piblinell [MLOps](https://en.wikipedia.org/wiki/MLOps) (gweithrediadau dysgu peiriant).
4. **Prynwch gynnyrch arbenigol.** Ar gyfer parthau wedi'u diffinio'n dda (prosesu dogfennau, sgorio twyll), gall cynnyrch gwerthwr aeddfed guro unrhyw beth a adeiladwch.
5. **Adeiladwch o'r dechrau.** Cadwch hyfforddi [modelau sylfaen](https://en.wikipedia.org/wiki/Foundation_model) (modelau mawr wedi'u rhaghyfforddi ar ddata eang ac y gellir eu haddasu i lawer o dasgau) ar gyfer sefydliadau â data unigryw, talent dwfn, a rhesymau strategol. I bron pob menter ac asiantaeth, dyma'r dewis anghywir.

### Sefydlwch ragofynion data, talent, a phlatfform

Archwiliwch eich data am argaeledd, ansawdd, labelu, llinach, a sail gyfreithiol ar gyfer defnydd. Cadarnhewch fod gennych yr hawl mewn gwirionedd i'w ddefnyddio ar gyfer DA, gan gynnwys unrhyw ddata personol neu drydydd parti. Aseswch dalent yn onest: mae angen gwyddonwyr data arnoch, a hefyd peirianwyr ML, peirianwyr data, rheolwyr cynnyrch sy'n deall systemau tebygolaidd, ac adolygwyr a all werthuso allbynnau. Cyn i chi raddio, sefydlwch linell sylfaen platfform: tracio arbrofion, cofrestrfa model (y system cofnod ar gyfer fersiynau model wedi'u hyfforddi a'u statws cymeradwyo), monitro, a chyflenwi diogel, fel nad yw pob achos defnydd newydd yn ailddyfeisio gweithrediadau.

### Trinwch gyd-destunau rheoleiddiedig a llywodraeth yn fwriadol

Dewch â thimau caffael, cyfreithiol, a risg i mewn yn gynnar. Mynnwch fod gwerthwyr yn datgelu tarddiad model, arferion data hyfforddi, canlyniadau gwerthuso, a chyfyngiadau hysbys. Ffafriwch gontractau sy'n rhoi cludadwyedd i'ch data a'ch prompiau, ac osgowch fformatau perchnogol sy'n eich maglu. Lle bo'n briodol, cyhoeddwch ddiben a mesurau diogelu systemau DA sy'n wynebu'r cyhoedd, a rhowch sianel i bobl herio penderfyniadau awtomataidd. Aliniwch â fframweithiau cydnabyddedig (gweler pennod 6.5) fel bod archwiliadau'n dod o hyd i broses ddogfennedig, amddiffynadwy.

### Cyfrifwch gyfanswm cost perchnogaeth a gwarchodwch yn erbyn clymu

Modelwch gost y cylch bywyd cyflawn: casgliad neu drwyddedu, piblinellau data, adolygiad dynol, monitro, ail-hyfforddi, ymateb i ddigwyddiadau, a datgomisiynu. Cymharwch ef â chost y statws quo a'r dewisiadau amgen. Lleihau clymu drwy roi'r model y tu ôl i ryngwyneb mewnol, cadw prompiau a setiau data gwerthuso'n gludadwy, a phrofi ail ddarparwr o bryd i'w gilydd.

## Cyfaddawdau: manteision ac anfanteision

| Dull | Manteision | Anfanteision | Gorau pan |
|---|---|---|---|
| Prompio model wedi'i letya | Cyflym, rhad, dim seilwaith, hawdd newid | Llai o reolaeth, cost fesul galwad, cwestiynau rhannu data | Prototeipiau, tasgau eang, gofynion ansicr |
| Ehangu drwy adalw | Yn seilio atebion yn eich data, y gellir ei ddiweddaru | Mae ansawdd adalw'n anodd, yn ychwanegu seilwaith | Tasgau trwm o ran gwybodaeth |
| Fine-tune model llai | Rheolaeth, cost is fesul galwad ar raddfa, dewis ar-safle | Angen MLOps, data, a chynnal | Tasgau sefydlog, cyfaint uchel, arbenigol |
| Prynu cynnyrch | Profedig, wedi'i gefnogi, cyflym i werth | Cost trwydded, clymu, ffit cyfyngedig | Problemau nwydd wedi'u diffinio'n dda |
| Adeiladu model sylfaen | Rheolaeth a gwahaniaethu mwyaf | Cost enfawr, talent prin, risg uchel | Bron byth, y tu allan i labordai blaengar |

Y prif gyfaddawd yw rheolaeth yn erbyn cost a chyflymder. Mae prompio'n rhoi'r cyflymder a'r hyblygrwydd mwyaf i chi ond y lleiaf o reolaeth; mae adeiladu'n rhoi'r rheolaeth fwyaf ond yn mynnu adnoddau na ddylai fawr o sefydliadau eu gwario. Dylai'r rhan fwyaf o dimau mawr fyw yn y canol: promptio ac adalw'n gyntaf, fine-tune yn ddetholus, a phrynu ar gyfer anghenion nwydd. Mae clymu'n cyfnewid cyfleustra tymor byr am risg tymor hir, ac mae hynny'n bwysig yn enwedig mewn llywodraeth, lle mae rhwymedigaethau ymadael aml-flwyddyn yn gyffredin.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Ble mae pob un o'n tri phrif achos defnydd ymgeisiol yn eistedd ar yr ysgol prompio-yna-adalw-yna-fine-tune-yna-prynu-yna-adeiladu, a pha dystiolaeth a fyddai'n ei symud gris?** Mae hyn yn bwysig oherwydd bod y rhan fwyaf o wariant DA gwastraffedig yn dod o ddechrau gris yn rhy uchel: hyfforddi model pan fyddai prompio gofalus wedi gweithio. I dîm mawr, mae cytuno ar yr ysgol fel diofyn a rennir yn stopio pob grŵp rhag ailddyfeisio piblinell ddrud. Dewch â'r datganiad problem un dudalen ar gyfer pob ymgeisydd, y llinell sylfaen bresennol, a darlleniad gonest ar a yw'r bwlch yn wybodaeth (adalw), yn gysondeb (fine-tuning), neu'n nwydd wedi'i ddatrys (prynu). Mewn lleoliadau menter a llywodraeth, ychwanegwch gost caffael ac archwilio pob gris, gan fod model fine-tuned yn llusgo baich MLOps nad oes gan alwad wedi'i letya. Dylai'r ateb adael i chi ladd neu israddio o leiaf un prosiect wedi'i orgwmpasu yn yr ystafell.

2. **Beth yw ein cynllun ymadael pendant ar gyfer y gwerthwr neu'r model rydym yn dibynnu arno fwyaf, ac a ydym wedi ei brofi mewn gwirionedd?** Mae clymu'n rhad i'w dderbyn ac yn ddrud i'w ddatod, ac mewn llywodraeth efallai y byddwch yn cario rhwymedigaethau ymadael aml-flwyddyn na allwch eu bodloni os na wnaethoch chi erioed eu hymarfer. Dewch â'r rhestr o nodweddion perchnogol rydych yn dibynnu arnynt, a yw prompiau a setiau data gwerthuso'n gludadwy, a sut mae'r model yn eistedd y tu ôl i ryngwyneb mewnol (neu ddim). Yr arwydd i'w wylio yw a yw unrhyw un erioed wedi rhedeg eich cyfres werthuso yn erbyn ail ddarparwr; os na, gobaith yw eich cynllun ymadael, nid cynllun. Os yr ateb gonest yw y byddai newid yn cymryd misoedd ac ailysgrifennu cod craidd, triniwch hynny fel diffyg dylunio i'w drwsio nawr, nid pont i'w chroesi'n ddiweddarach.

3. **Beth mae cerdyn sgorio parodrwydd gonest yn ei ddweud am ein hawliau data, a pha achosion defnydd y mae'n eu gwahardd heddiw?** Sgipio parodrwydd data yw'r methiant sy'n suddo peilotiaid yn dawel: mae'r model yn gweithio, ond ni chawsoch chi erioed y sail gyfreithiol i ddefnyddio'r data, neu mae'n ddi-label a heb linach. I sefydliad mawr, mae data personol a thrydydd parti'n codi terfynau cydsyniad a chytundebol sy'n amrywio yn ôl awdurdodaeth ac yn ôl set ddata. Dewch ag archwiliad o argaeledd, ansawdd, labelu, llinach, a sail gyfreithiol ar gyfer pob ymgeisydd, a byddwch yn barod i farcio rhai achosion defnydd fel wedi'u rhwystro nes bod sylfeini data'n bodoli. Mewn lleoliadau rheoleiddiedig a chyhoeddus, nid oedi yw sail gyfreithiol na ellir ei defnyddio, mae'n stop caled, a dylai ariannu'r gwaith parodrwydd fod yn linell benodol yn y cynllun yn hytrach nag ôl-ystyriaeth.

4. **Sut y byddwn yn gwybod bod achos defnydd DA byw'n gweithio go iawn, a pha dystiolaeth a fyddai'n ein gwneud i'w ladd?** Mae'r rhan fwyaf o bortffolios DA yn cronni zombis: peilotiaid a gyflenwyd, a wnaeth argraff ar rywun, ac sydd bellach yn rhedeg am byth heb i unrhyw un wirio a ydynt yn dal i ennill eu cost. Cytunwch y llinell sylfaen a'r metrig llwyddiant cyn lansio, yna gosodwch drothwy lladd penodol, fel bod y penderfyniad i stopio'n cael ei wneud ymlaen llaw yn hytrach na'i amddiffyn yn y funud. Dewch â'r metrig presennol, cost goruchwyliaeth ddynol fesul canlyniad, a'r crwydro rydych wedi'i weld ers lansio. I bortffolios menter a llywodraeth, enwch pwy sy'n adolygu pob system ar gadwyn sefydlog a phwy sy'n dal awdurdod i'w ymddeol; mae achos defnydd nad oes neb yn atebol am ei adolygu'n un na fydd neb byth yn ei ddiffodd.

5. **Ble mae dynol yn aros yn y ddolen, faint mae'r oruchwyliaeth honno'n ei gostio, ac a ydym wedi ei chyllidebu mewn gwirionedd?** Yr achosion defnydd DA sy'n edrych rataf yw'r rhai sy'n tybio'n dawel awtomeiddio llawn, yna'n gollwng cost drwy'r adolygiad, cywiriad, ac uwchgyfeirio y mae realiti'n ei orfodi'n ôl i mewn. Penderfynwch yn fwriadol pa benderfyniadau y mae'n rhaid i berson eu cadarnhau, pa rai y caiff y model eu cymryd ar ei ben ei hun, a pha rai na chaiff byth eu cymryd, yna prisiwch yr amser dynol y mae hynny'n ei olygu. Dewch â chyfaint yr achosion hyder isel, cost ateb anghywir, a'r llwybr uwchgyfeirio presennol. Mewn lleoliadau rheoleiddiedig a chyhoeddus, cysylltwch bob penderfyniad awtomataidd â swyddog atebol a llwybr apêl, oherwydd goruchwyliaeth na allwch ei disgrifio yw goruchwyliaeth nad oes gennych.

6. **A oes gennym y dalent a'r platfform i redeg yr hyn rydym yn ei gynnig, neu a ydym yn tybio'n dawel gapasiti nad oes gennym?** Mae cynlluniau DA uchelgeisiol yn methu llai ar y model nag ar y sylfeini di-lachar: neb i gynnal y biblinell, neb a all werthuso allbynnau, dim platfform i'w ddefnyddio arno. Parwch bob achos defnydd ymgeisiol â'r sgiliau a'r seilwaith sydd ei angen mewn gwirionedd, a byddwch yn onest lle mae'r bwlch yn benodiad, yn bartner, neu'n rheswm i beidio ag adeiladu. Dewch â rhestr o bwy all fod yn berchen ar bob system mewn cynhyrchu, ar ba blatfform y bydd yn rhedeg, a pha alluoedd y byddai'n rhaid i chi eu prynu. I sefydliad mawr neu gyhoeddus, ychwanegwch amseroedd arwain caffael a recriwtio, gan fod cynllun sy'n dibynnu ar dalent na allwch ei recriwtio o fewn y ffenestr berthnasol yn gynllun i dan-gyflenwi.

## Lens sector

**Cwmni newydd.** Mae cyflymder a goroesiad yn dominyddu. Dewiswch un achos defnydd cul sy'n cyffwrdd eich gwerth craidd, ei gyflenwi ar fodel wedi'i letya y tu ôl i ryngwyneb tenau, a chapio gwariant yn galed. Osgowch adeiladu seilwaith neu hyfforddi modelau: eich adnodd prinnaf yw sylw peirianneg, ac mae piblinell fine-tuned na allwch ei chynnal yn atebolrwydd, nid ffos amddiffynnol. Cadwch newid yn rhad fel y gallwch ddilyn marchnad sy'n symud yn gyflym.

**Busnes bach.** Yn ôl pob tebyg, nid oes gennych wyddonwyr data a chyllideb dynn, felly triniwch DA fel rhywbeth rydych yn ei brynu wedi'i blannu mewn offer rydych eisoes yn eu defnyddio, nid rhaglen rydych yn ei staffio. Fframiwch barodrwydd fel cwestiwn hylendid data a phreifatrwydd yn hytrach na phrosiect dysgu peiriant: gwybyddwch pa ddata cwsmer sydd gennych, beth y cewch ei wneud ag ef, a ble y byddai ateb awtomataidd anghywir yn costio cwsmer i chi. Ffafriwch werthwyr sy'n gwneud y DA'n ddewisol, yn dryloyw, ac yn hawdd ei ddiffodd.

**Menter.** Y broblem yw llywodraethu portffolio ar draws llawer o dimau: ysgol adeiladu-yn-erbyn-prynu a rennir, asesiadau parodrwydd cyson, a dadansoddiad clymu a chyfanswm cost fel bod grwpiau'n stopio ailddyfeisio piblinellau drud. Cyllidebwch y baich MLOps a goruchwyliaeth ddynol yn benodol, safonwch yr haen ryngwyneb fel bod darparwyr yn aros yn gyfnewidiol, a rheolwch achosion defnydd DA fel portffolio gyda metrigau clir a meini prawf lladd yn hytrach na gwasgariad o beilotiaid.

**Llywodraeth.** Mae tryloywder, rheolau caffael, ac atebolrwydd yn siapio pob dewis. Ffafriwch systemau sy'n dyfynnu ffynonellau swyddogol yn hytrach na chynhyrchu polisi, cadwch ddynol yn atebol am benderfyniadau canlyniadol, a mynnwch gludadwyedd data a datgeliad o gyfyngiadau model mewn contractau. Cyhoeddwch ddisgrifiad mewn iaith blaen a llwybr apêl, anrhydeddwch unrhyw rwymedigaethau ymadael aml-flwyddyn a lofnodwch, a chadwch DA allan o benderfyniadau asesu terfynol y mae'n rhaid iddynt orffwys gyda swyddog atebol.

## Enghreifftiau

**Cwmni newydd.** Roedd cwmni newydd amserlennu pum person eisiau ychwanegu nodwedd "trefna gyfarfod i mi" iaith naturiol heb dynnu ei ddau beiriannydd oddi ar y cynnyrch craidd. Dewisodd y broblem leiaf a oedd yn bwysig, dosrannu cais yn amser arfaethedig, a'i gyflenwi gyda model wedi'i letya y tu ôl i API mewnol tenau fel y gallai newid darparwyr yn ddiweddarach. Gosododd y tîm gap gwariant misol caled, tracio a oedd defnyddwyr yn derbyn yr amseroedd a awgrymwyd, a chytuno i ailedrych ar fodel fine-tuned dim ond os oedd cyfaint erioed yn cyfiawnhau'r gwaith ychwanegol.

**Menter.** Roedd yswiriwr rhyngwladol eisiau cyflymu didoli hawliadau. Yn lle hyfforddi model pwrpasol, fframiodd y broblem yn gul (llwybro a chrynhoi hawliadau sy'n dod i mewn), prototeipio gyda model wedi'i letya ynghyd ag adalw dros ei ddogfennau polisi, a mesur yn erbyn amser trin dynol a chywirdeb. Dim ond ar ôl profi gwerth y gwnaeth fine-tune fodel llai ar gyfer y math hawliad cyfaint uchaf i dorri cost fesul galwad. Cadwodd y model y tu ôl i API mewnol fel y gallai gyfnewid darparwyr, a modelodd TCO tair blynedd a oedd yn cynnwys adolygiad dynol o achosion hyder isel.

**Llywodraeth.** Ystyriodd awdurdod treth cenedlaethol gynorthwyydd DA i helpu staff ateb ymholiadau dinasyddion. Am fod yr atebion hynny'n cyffwrdd rhwymedigaethau cyfreithiol, mynnodd yr asiantaeth dryloywder: ni allai'r system ond dod ag arweiniad swyddogol i'r wyneb gyda dyfyniadau, byth dyfeisio polisi, ac adolygodd dynol bob awgrym awtomataidd cyn iddo fynd allan. Mynnodd caffael fod y gwerthwr yn datgelu cyfyngiadau model ac yn rhoi cludadwyedd data, a chyhoeddodd yr asiantaeth ddisgrifiad mewn iaith blaen o'r system a llwybr apêl. Cadwodd DA allan o benderfyniadau asesu terfynol yn llwyr, gan gadw'r rheiny ar gyfer swyddogion atebol.

## Achos busnes: cymhellion, ROI, a TCO

Mae strategaeth DA yn bodoli i'ch helpu i osgoi dau fethiant drych-ddelwedd: gorfuddsoddi mewn DA nad yw byth yn talu ar ei ganfed, a thanfuddsoddi tra bod cystadleuwyr neu asiantaethau cymar yn tynnu ar y blaen. Daw ROI o lafur a arbedwyd, amser cylch wedi'i leihau, cyfraddau gwall is, a galluoedd newydd wedi'u galluogi. Mesurwch y rhain yn erbyn llinell sylfaen wirioneddol, a disgowntiwch am gost wirioneddol goruchwyliaeth ddynol, sy'n anaml yn diflannu.

Rhaid i TCO gynnwys yr eitemau llinell di-lachar: piblinellau data, monitro, ail-hyfforddi wrth i'r byd grwydro, adolygiad diogelwch, a datgomisiynu yn y pen draw. Gall peilot sy'n edrych yn rhad droi'n ddrud unwaith y bydd yn rhedeg ar raddfa am flynyddoedd. Cyflwynwch gost *peidio â* mabwysiadu hefyd: gwasanaeth arafach, cost â llaw uwch, a chrwydro strategol. Gwnewch yr achos i arweinyddiaeth gyda golwg portffolio: ychydig o fetiau hyder uchel, metrigau llwyddiant clir, meini prawf lladd ar gyfer methiannau, ac asesiad parodrwydd sy'n dangos bod sylfeini data a thalent yn bodoli. Gofynnwch i arweinwyr ariannu parodrwydd yn benodol; ei sgipio, a byddwch yn gwarantu ailwaith drud.

## Gwrth-batrymau a pheryglon

- **Ateb yn chwilio am broblem.** Prynu DA am fod cymheiriaid wedi gwneud hynny, yna hela am achos defnydd.
- **Sgipio parodrwydd data.** Lansio modelau ar ddata nad yw ar gael, wedi'i labelu, neu'n gyfreithiol ddiddefnydd.
- **Penderfyniadau wedi'u gyrru gan demo.** Ymrwymo ar sail demo caboledig heb werthusiad ansawdd cynhyrchu.
- **Anwybyddu'r ddolen ddynol.** Tybio awtomeiddio llawn a than-gyllidebu adolygiad, sef lle mae'r rhan fwyaf o gost yn cuddio.
- **Clymu distaw.** Adeiladu'n ddwfn ar nodweddion perchnogol un gwerthwr heb gynllun ymadael.
- **Tanamcangyfrif gweithrediadau.** Trin defnyddio fel y llinell derfyn yn hytrach na dechrau rhwymedigaeth cynnal a chadw.
- **Cydymffurfiaeth fel ôl-ystyriaeth.** Ôl-osod tryloywder ac archwiliadwyedd ar ôl dylunio, am gynifer o weithiau'r gost.

## Model aeddfedrwydd

1. **Cychwyn.** Arbrofion ad hoc, dim strategaeth a rennir, penderfyniadau wedi'u gyrru gan hype a brwdfrydedd unigol.
2. **Datblygu.** Mae fframio problemau'n bodoli ar gyfer rhai prosiectau; mae llinell sylfaen platfform gyntaf yn ymddangos; trafodir adeiladu-yn-erbyn-prynu ond yn anghyson.
3. **Safoni.** Portffolio o achosion defnydd DA gyda metrigau clir, coeden benderfynu ddogfennedig, asesiadau parodrwydd, a dadansoddiad clymu a TCO, wedi'u cymhwyso'n gyson ar draws timau.
4. **Rheoli.** Mesurir y portffolio: trecir parodrwydd, ROI, TCO, a chost goruchwyliaeth ddynol yn erbyn llinellau sylfaen; gorfodir meini prawf lladd ar dystiolaeth; mae effaith cyflenwi ac ansawdd yn gyrru pob penderfyniad mynd neu beidio â mynd.
5. **Cyd-drefnu.** Mae strategaeth DA wedi'i hintegreiddio â chynllunio busnes a risg; cynhelir parodrwydd yn barhaus; mae'r sefydliad yn rheolaidd yn ymddeol, yn amnewid, ac yn ailgwmpasu systemau DA ar sail tystiolaeth, gan ailgydbwyso'r portffolio wrth i'r farchnad a'r darlun risg symud.

## Syniadau ar gyfer trafodaeth

- Sut rydych yn penderfynu pryd mae problem yn wirioneddol anaddas ar gyfer DA, a phwy sydd ag awdurdod i ddweud na?
- Pa drothwy parodrwydd ddylai giatio prosiect o beilot i gynhyrchu?
- Faint o glymu sy'n dderbyniol yn gyfnewid am amser cyflymach i werth?
- Mewn llywodraeth, sut ddylai rhwymedigaethau tryloywder siapio'r dewis adeiladu-yn-erbyn-prynu?
- Sut rydych yn cadw amcangyfrifon TCO'n onest pan fo gan werthwyr a brwdfrydigion gymhellion i'w tanddatgan?
- Pwy sy'n berchen ar y portffolio DA, a sut mae penderfyniadau lladd yn cael eu gwneud?

## Prif negeseuon

- Mae strategaeth yn dechrau gyda phroblem go iawn a llinell sylfaen onest, nid gyda thechnoleg.
- Ffafriwch y dewis symlaf: prompio, yna adalw, yna fine-tune, yna prynu, ac anaml adeiladu o'r dechrau.
- Mae parodrwydd data, talent, a phlatfform yn rhagofynion; mae eu hariannu'n rhan o'r cynllun.
- Mae cyd-destunau rheoleiddiedig a llywodraeth yn mynnu tryloywder, cydymffurfiaeth caffael, a dewisiadau ymadael drwy ddylunio.
- Modelwch TCO llawn a chost anweithredu, a gwarchodwch yn erbyn clymu gwerthwr o'r penderfyniad pensaernïaeth cyntaf.

## Cyfeiriadau a darllen pellach

- Ajay Agrawal, Joshua Gans, and Avi Goldfarb, *Prediction Machines: The Simple Economics of Artificial Intelligence*.
- Eric Siegel, *The AI Playbook: Mastering the Rare Art of Machine Learning Deployment*.
- Andriy Burkov, *The Hundred-Page Machine Learning Book*.
- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- Organisation for Economic Co-operation and Development, *OECD AI Principles*.
- Thomas H. Davenport, *The AI Advantage: How to Put the Artificial Intelligence Revolution to Work*.
