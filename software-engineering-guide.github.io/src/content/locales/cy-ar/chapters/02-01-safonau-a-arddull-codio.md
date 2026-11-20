# 2.1 Safonau a steil codio

## Trosolwg a chymhelliant

Confensiynau a rennir yw safonau codio sy'n galluogi llawer o bobl i ysgrifennu cod fel pe bai un awdur gofalus wedi'i ysgrifennu. Maent yn ymdrin ag enwi, fformatio, cynllun ffeiliau, idiomau, trin gwallau, a'r paradeimau mae tîm yn eu ffafrio. Ar dîm bach, gall chwaeth unigolyn gario'r dydd. Ar dîm mawr (cannoedd neu filoedd o beirianwyr, llawer o gontractwyr, trosiant uchel), mae anghysondeb yn dod yn dreth rydych chi'n ei thalu ar bob darlleniad, pob adolygiad, a phob sefydlu. Mae safonau'n troi dadleuon steilistig bach di-ri yn benderfyniad un-tro y mae peiriant wedyn yn ei orfodi ar eich rhan.

I sefydliadau mawr mae'r risgiau'n goncrid. Mae cod yn cael ei ddarllen yn llawer amlach nag y mae'n cael ei ysgrifennu. Mewn lleoliadau menter a llywodraeth, gall llinell o god gael ei darllen gan archwilwyr, adolygwyr diogelwch, a chynhalwyr flynyddoedd ar ôl i'w hawdur adael. Mae steil cyson yn gostwng cost feddyliol y darllen hwnnw, yn crebachu'r arwynebedd ar gyfer gwallau, ac yn gwneud dadansoddiad awtomataidd yn ddibynadwy ar draws [dolenwyr](https://en.wikipedia.org/wiki/Lint_(software)) (teclynnau sy'n fflagio gwallau a thoriadau steil tebygol yn awtomatig), sganwyr diogelwch, a theclynnau [ailffactora](https://en.wikipedia.org/wiki/Code_refactoring). Lle mae rheoleiddio'n berthnasol, fel mewn gwasanaethau ariannol, gofal iechyd, amddiffyn, a systemau sector cyhoeddus, mae safonau hefyd yn ffurfio rhan o'r dystiolaeth bod cronfa god yn gynaliadwy ac yn cael ei rheoli.

Y dull modern yw trin steil fel pryder wedi'i ddatrys, wedi'i awtomeiddio yn hytrach na mater o farn ddynol barhaus. Mae fformatwyr a dolenwyr yn rhedeg yn y golygydd, mewn bachau cyn-ymrwymo, ac mewn [integreiddio parhaus](https://en.wikipedia.org/wiki/Continuous_integration) (CI), y broses adeiladu-a-phrofi awtomataidd sy'n rhedeg ar bob newid. Mae peiriannau'n gorfodi'r steil, felly gallwch chi wario'ch sylw adolygu ar ddylunio a chywirdeb. Nid unffurfiaeth er ei mwyn ei hun yw'r nod. Dileu ffrithiant ydyw: dylech allu symud rhwng gwasanaethau a thimau heb ailddysgu'r pethau sylfaenol.

## Egwyddorion allweddol

- Mae cysondeb yn drech na hoffter unigol; mae un steil y cytunwyd arno, wedi'i chymhwyso ym mhobman, yn werth mwy na'r steil "orau" wedi'i chymhwyso'n anghyson.
- Awtomeiddiwch orfodaeth. Fformatwyr a dolenwyr yw'r ffynhonnell wirionedd, nid sylwadau adolygu cod am fylchau.
- Optimeiddiwch ar gyfer y darllenydd a'r cynhaliwr, nid yr awdur gwreiddiol.
- Ffafriwch gonfensiynau y mae cymuned ehangach yr iaith eisoes yn eu defnyddio dros reolau tŷ pwrpasol.
- Gwnewch y safon yn hawdd i'w mabwysiadu: darparwch ffurfweddiadau, templedi, ac offer a rennir yn hytrach na PDF nad oes neb yn ei ddarllen.
- Dylai rheolau steil fod yn ychydig, yn amddiffynadwy, ac yn ddiamwys; mae gan bob rheol fecanwaith gorfodi neu nid yw ond yn awgrym.
- Enwi yw'r penderfyniad darllenadwyedd sydd â'r trosoledd uchaf ac mae'n haeddu canllawiau penodol.

## Argymhellion

### Mabwysiadwch ganllaw steil canonaidd fesul iaith

Ar gyfer pob iaith rydych chi'n ei defnyddio, mabwysiadwch ganllaw steil eang ei chydnabyddiaeth fel y llinell sylfaen (er enghraifft, canllaw'r gymuned neu'r gwerthwr ar gyfer yr iaith honno) a dogfennwch dim ond y gwahaniaethau y mae eich sefydliad eu hangen. Peidiwch â dyfeisio steil tŷ o'r dechrau. Cyhoeddwch eich dewis mewn lle canolog, hygyrch, a fersiynwch ef fel cod.

### Gwnewch fformatwyr yn ragosodiadau anymdrafodadwy

Defnyddiwch fformatiwr awtomatig barn-benodol ar gyfer pob iaith sydd ag un, gydag un ffurfweddiad a rennir wedi'i wirio i mewn i'r ystorfa. Ni ddylai fformatio byth godi mewn adolygiad, oherwydd ei fod yn cael ei gymhwyso'n awtomatig wrth gadw ac yn cael ei wirio yn CI. Lle nad oes gan iaith fformatiwr cryf, dewiswch un ffurfweddiad dolenwr a'i drin yr un fath.

### Rhedwch ddolenwyr fel gatiau gorfodedig, nid cyngor

Ffurfweddwch ddolenwyr gyda set reolau y cytunwyd arni, methwch yr adeiladwaith ar doriadau, a chadwch y set reolau mewn [rheolaeth fersiynau](https://en.wikipedia.org/wiki/Version_control) fel bod newidiadau'n mynd drwy adolygiad. Gwahanwch reolau y gellir eu trwsio'n awtomatig (cymhwyswch nhw'n awtomatig) oddi wrth reolau sydd angen barn ddynol (fflagiwch a rhwystrwch). Cyflwynwch reolau newydd ym modd "rhybuddio", clirio'r ôl-groniad, yna eu dyrchafu i "wall".

### Gorfodwch ar sawl haen

Darparwch integreiddiad golygydd ar gyfer adborth ar unwaith, bachau cyn-ymrwymo ar gyfer gorfodaeth leol, a gwiriadau CI fel y gât awdurdodol. Y cynharaf y byddwch chi'n dal toriad, yr rhataf ydyw. Rhaid i CI fod y cadarnle terfynol, oherwydd gellir osgoi bachau lleol.

### Rhowch reolau enwi penodol

Safonwch gonfensiynau achos fesul iaith, mynnwch enwau sy'n datgelu bwriad, gwaharddwch fyrfoddau camarweiniol, a diffiniwch gonfensiynau ar gyfer Boole-au, casgliadau, unedau, a gweithrediadau anghydamserol. Ysgrifennwch eich geirfa parth mewn geirfa a rennir fel bod gan yr un cysyniad yr un enw ym mhobman.

### Rheolwch gysondeb amlieithog yn fwriadol

Mewn cronfa god sy'n rhychwantu sawl iaith, anelwch at gysyniadau cyson (patrymau trin gwallau, strwythur cofnodi, cynllun prosiect) hyd yn oed lle mae'r gystrawen yn wahanol. Darparwch ffurfweddiadau fesul iaith o ystorfa ganolog fel bod gwasanaeth newydd yn etifeddu'r safonau'n awtomatig drwy dempledi neu sgaffaldiau.

### Codeiddiwch idiomau a paradeimau

Ewch y tu hwnt i fformatio. Ysgrifennwch eich idiomau a ffefrir, megis sut i drin gwallau, sut i strwythuro modiwlau, a phryd i ddefnyddio eithriadau yn hytrach na mathau canlyniad, ynghyd â'r paradeimau y mae'ch timau'n eu ffafrio. Dyma lle mae darllenadwyedd a chynaliadwyedd gwirioneddol yn byw.

## Cyfaddawdau: manteision ac anfanteision

| Dull | Manteision | Anfanteision |
|---|---|---|
| Fformatiwr awtomatig llym, dim ffurfweddiad | Yn dod â phob dadl fformatio i ben; cysondeb ar unwaith; sefydlu dibwys | Nid oes modd trafod rhai dewisiadau amhoblogaidd; gwahaniaeth cychwynnol mawr pan gaiff ei gymhwyso gyntaf |
| Dolenwr ffurfweddadwy gyda rheolau tŷ | Wedi'i deilwra i anghenion y sefydliad; gall amgodio rheolau atal-gwallau gwirioneddol | Llithriad ffurfweddiad; ffraeo bach-bwysig am reolau; baich cynnal |
| Safon gymunedol wedi'i mabwysiadu'n gyfan gwbl | Cyfarwydd i benodiadau newydd; ecosystem offer cryf; cynnal isel | Efallai na fydd yn ffitio cyfyngiadau sefydliadol niche; rheolau lletchwith achlysurol |
| Safon fewnol bwrpasol | Yn ffitio'r sefydliad yn union | Drud i'w hysgrifennu a'i chynnal; anghyfarwydd i benodiadau newydd; offer gwan |
| Ymreolaeth fesul tîm | Morâl lleol uchel; penodol i gyd-destun | Chwalfa; symudedd traws-dîm poenus; offer anghyson |

Mae rhagosodiadau gorfodedig yn cyfnewid ychydig o ymreolaeth unigol am enillion cyfunol mawr: llai o ffrithiant adolygu, sefydlu cyflymach, ac awtomatiaeth ddibynadwy. Y prif risg yw gor-beirianyddu'r safon yn gannoedd o reolau sy'n arafu pawb heb atal diffygion gwirioneddol. Cadwch y set reolau'n fach ac yn seiliedig ar dystiolaeth, a phwyswch tuag at fabwysiadu safon sy'n bodoli eisoes fel bod cynnal yn parhau'n rhad.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Pa reolau dolenwr ddylai fethu'r adeiladwaith, a sut ydych chi'n dyrchafu rheol o rybudd i wall heb atal pawb?** Mae'r bennod hon yn dadlau bod gan bob rheol angen mecanwaith gorfodi, ac y dylai rheolau newydd lanio mewn modd rhybuddio, cael eu hôl-groniad wedi'i glirio, yna troi i wall. Ar dîm mawr, mae troi rheol i wall yn erbyn cronfa god fudr yn rhwystro cannoedd o newidiadau anghysylltiedig dros nos. Dewch â thystiolaeth galed i'r cyfarfod: y cyfrif toriad presennol ar gyfer pob rheol ymgeisiol, ac a yw'n hunan-drwsiadwy neu angen barn ddynol. Mewn lleoliadau menter a llywodraeth mae'r llinell llwyddo/methu hefyd yn bwydo gatiau archwilio, felly mae set reolau amwys yn gwanhau eich stori cydymffurfiaeth. Penderfynwch gyflwyniad graddol: hunan-drwsiwch yr hyn y gallwch, cyllidebwch y glanhau, yna gatiwch.

2. **Pan fyddwch chi'n cymhwyso fformatiwr am y tro cyntaf i'ch cod etifeddol, sut ydych chi'n atal yr ail-fformatio hwnnw rhag chwalu blame git a boddi adolygiadau?** Mae'r tabl cyfaddawdau'n rhybuddio am wahaniaeth cychwynnol mawr, ac mae'r adran gwrth-batrymau'n nodi cymysgu ymrwymiadau ail-fformatio â newidiadau rhesymeg. Mae un ail-fformatio ysgubol yn ailysgrifennu miloedd o linellau ac yn gwneud i blame bwyntio at yr ail-fformatio yn hytrach na'r awdur gwirioneddol, sy'n niweidio unrhyw un sy'n dadfygio flynyddoedd yn ddiweddarach. Gwnewch yr ail-fformatio fel un ymrwymiad ynysig, wedi'i labelu'n glir, a'i gofrestru mewn ffeil anwybyddu-blame fel bod hanes yn parhau'n ddefnyddiol. I archwilwyr sy'n olrhain pwy newidiodd beth, mae'r ynysu hwnnw'n wahaniaeth rhwng tystiolaeth lân a sŵn. Cytunwch ar y drefn cyn i chi gyffwrdd â'r cod, nid ar ôl hynny.

3. **Pwy sy'n berchen ar eich geirfa enwi a'ch geirfa parth, a sut mae term newydd yn cael ei ychwanegu?** Mae'r bennod yn galw enwi'n benderfyniad darllenadwyedd sydd â'r trosoledd uchaf ac yn gofyn i chi ysgrifennu'r eirfa parth mewn geirfa a rennir. Heb berchennog wedi'i enwi, mae'r un cysyniad yn codi tri enw gwahanol ar draws timau, ac mae offer dadansoddi-statig a chwilio'n colli dibynadwyedd. Dewch â enghreifftiau o gysyniadau sydd eisoes ag enwau gwrthdrawiadol yn eich cronfa god fel y signal concrid. Neilltuwch un perchennog a llwybr cynnig ysgafn, fel bod ychwanegu neu ailenwi term yn newid bach, wedi'i adolygu yn hytrach na dadl ym mhob cais tynnu. Mae'r ateb yn newid sefydlu: mae penodiad newydd yn darllen un eirfa yn hytrach na pheiriannu bwriad yn ôl o god anghyson.

4. **Ar gyfer pob iaith, ydych chi'n mabwysiadu canllaw steil cymunedol neu werthwr cydnabyddedig yn gyfan gwbl, a lle mae gwahaniaethau tŷ wir yn cael eu cyfiawnhau?** Mae'r bennod hon yn dadlau y dylech chi gymryd safon sy'n bodoli eisoes fel y llinell sylfaen a dogfennu dim ond y gwahaniaethau y mae eich sefydliad eu hangen, oherwydd bod safon bwrpasol yn ddrud i'w hysgrifennu ac yn anghyfarwydd i benodiadau newydd. Mae'r tyniad cystadleuol yn wirioneddol: weithiau mae cyfyngiad mewnol (rheol ddiogelwch, fframwaith etifeddol, mandad hygyrchedd) yn gwrthdaro'n wirioneddol â'r rhagosodiad cymunedol, ac mae pob gwahaniaeth rydych chi'n ei gadw'n rheol rydych chi nawr yn berchen arni ac yn ei chynnal am byth. Dewch â'r rhestr gwahaniaethau arfaethedig i'r cyfarfod, pob un gyda'r cyfyngiad concrid sy'n ei gymell, a byddwch yn barod i dorri unrhyw wahaniaeth sydd ond yn chwaeth. Mewn lleoliadau menter a llywodraeth, mae llinell sylfaen sy'n cyfateb i gymuned ehangach yr iaith hefyd yn golygu bod contractwyr a gwerthwyr newydd yn cyrraedd yn rhugl yn barod, sy'n byrhau sefydlu ac yn cryfhau'r dystiolaeth cynaliadwyedd y mae archwilwyr yn chwilio amdani.

5. **Mewn cronfa god amlieithog, pa gonfensiynau sy'n wirioneddol gyffredinol a pha rai sy'n aros yn iaith-leol, a sut ydych chi'n atal ffurfweddiadau fesul-ystorfa rhag llithro?** Mae'r bennod yn gofyn am gysyniadau cyson (trin gwallau, strwythur cofnodi, cynllun prosiect) ar draws ieithoedd hyd yn oed lle mae'r gystrawen yn wahanol, ac am ffurfweddiadau fesul iaith wedi'u gweini o ystorfa ganolog fel bod gwasanaethau newydd yn etifeddu safonau'n awtomatig. Y tyndra yw bod gorfodi idiomau un iaith ar un arall yn cynhyrchu cod lletchwith, an-idiomatig, tra bo gadael i bob tîm fforcio ei ffurfweddiad ei hun yn dod i ben gyda "'r safon" yn golygu dim byd. Dewch â rhestr eiddo o'ch ffurfweddiadau dolenwr a fformatiwr fesul-ystorfa presennol a gwahaniaeth sy'n dangos pa mor bell y maen nhw eisoes wedi llithro ar wahân, fel y signal concrid. I sefydliad mawr sy'n rhedeg dwsinau o wasanaethau, penderfynwch y mecanwaith dosbarthu (templedi, sgaffaldiau, pecyn ffurfweddiad a rennir) fel bod newid rheol yn lledaenu unwaith yn hytrach na chael ei gopïo â llaw i mewn i bob ystorfa.

6. **Pryd mae analluogi rheol yn ddilys, pwy sy'n adolygu'r atal, a sut ydych chi'n atal atal-cwbl rhag gwacáu'r safon?** Mae'r adran gwrth-batrymau'n fflagio ataliadau mewnlin eang fel arwydd bod rheol yn anghywir neu fod tîm wedi rhoi'r gorau iddi, eto mae polisi dim-eithriadau anhyblyg yn gwthio pobl i ysgrifennu cod gwaeth dim ond i fodloni'r dolenwr. Cytunwch ar lwybr ysgafn: rhaid i ataliad gario rheswm, eistedd yn y cwmpas culaf posibl, a bod yn weladwy mewn adolygiad yn hytrach na chael ei gladdu mewn ffeil anwybyddu byd-eang. Dewch â'r cyfrif presennol o ataliadau fesul rheol a fesul ystorfa, oherwydd mae rheol wedi'i hatal gannoedd o weithiau'n dweud rhywbeth wrthych am y rheol, nid y cod. Mewn gwaith rheoleiddiedig a sector cyhoeddus, mae ataliadau-cwbl heb esboniad yn gwanhau'r stori archwilio'n uniongyrchol, gan na all y biblinell bellach ddangos bod cod wedi'i uno wir wedi pasio'r gatiau y cytunwyd arnynt.

## Lens sector

**Cwmni newydd.** Mae cyflymder yn ennill, felly mabwysiadwch ragosodiadau'r fformatiwr a'r dolenwr cymunedol ar gyfer eich un iaith ar y diwrnod cyntaf a'u gwifro i mewn i fach cyn-ymrwymo a CI cyn i'r ail beiriannydd gyrraedd. Peidiwch ag ysgrifennu steil tŷ nad oes gennych amser i'w gynnal: y ffurfweddiad a gludir yn yr ystorfa yw'r safon gyfan. Pan fyddwch chi'n ychwanegu ail iaith, estynnwch am ganllaw canonaidd yr iaith honno yn hytrach na dyfeisio confensiynau o'r dechrau.

**Busnes bach.** Heb arbenigwr offer penodedig a chyllideb dynn, dibynnwch yn gyfan gwbl ar y fformatiwr rhad ac am ddim, barn-benodol sy'n dod gyda'ch iaith neu ochr yn ochr â hi, a derbyniwch ei ragosodiadau yn hytrach na'u tiwnio. Mae hwn yn achos prynu-dros-adeiladu clir: mae cynnal set reolau bwrpasol yn costio amser nad oes gennych, tra bo fformatiwr oddi ar y silff yn costio dim ac yn dod â dadl steil i ben ar unwaith. Cadwch y ffurfweddiad yn yr ystorfa fel bod y contractwr unigol y byddwch yn ei gyflogi flwyddyn nesaf yn ei etifeddu heb sgwrs.

**Menter.** Ar raddfa'r swydd yw llywodraethu ar draws llawer o dimau: ystorfa safonau-peirianneg ganolog sy'n dal y ffurfweddiadau fformatiwr a dolenwr a rennir fesul iaith, gwasanaethau newydd wedi'u cynhyrchu o dempledi sy'n tynnu'r ffurfweddiadau hynny, a gatiau CI sy'n rhwystro uniadau anghydnaws. Fersiynwch y set reolau fel cod a llwybrwch newidiadau drwy adolygiad cyfnodol fel bod safonau'n esblygu'n fwriadol yn hytrach na llithro. Yr enillion yw peirianwyr yn symud rhwng timau i mewn i god cyfarwydd, ac offer awtomataidd sy'n cynhyrchu signal dibynadwy oherwydd bod pob ystorfa'n gyson.

**Llywodraeth.** Mae caffael ac atebolrwydd yn siapio'r dewis: mandadwch set reolau steil a diogelwch penodol fel rhan o ofynion awdurdod-i-weithredu, a chael y biblinell i gynhyrchu adroddiad sy'n dangos bod pob newid a unwyd wedi pasio'r gatiau y cytunwyd arnynt fel tystiolaeth archwilio. Oherwydd bod fformatiwr yn cael ei gymhwyso'n awtomatig, mae cod gan sawl gwerthwr a chontractwr yn edrych yn gyson, sy'n amddiffyn y swydd cynnal cyhoeddus ymhell ar ôl i'r contractau ddod i ben. Ffafriwch linellau sylfaen cymunedol cydnabyddedig dros reolau pwrpasol fel bod y safon yn dryloyw a gall unrhyw gyflenwr yn y dyfodol ei mabwysiadu heb glymu perchnogol.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd pedwar person yn mabwysiadu rhagosodiadau'r fformatiwr a'r dolenwr cymunedol ar gyfer ei un iaith ar y diwrnod cyntaf, gan eu gwifro i mewn i fach cyn-ymrwymo a CI fel nad oes neb yn dadlau am fylchau mewn adolygiad. Oherwydd bod y ffurfweddiad yn cael ei gludo o fewn yr ystorfa, mae'r pumed a'r chweched penodiad yn ei etifeddu'n awtomatig ac byth yn gweld sylw fformatio. Pan fydd y tîm yn ddiweddarach yn ychwanegu ail iaith, maen nhw'n estyn am ganllaw safonol yr iaith honno yn hytrach na dyfeisio steil tŷ nad oes ganddynt amser i'w gynnal.

**Menter.** Mae banc mawr yn rhedeg gwasanaethau yn Java, Python, a TypeScript ar draws dwsinau o dimau. Mae'n cyhoeddi ystorfa "safonau peirianneg" ganolog sy'n dal y ffurfweddiadau fformatiwr a dolenwr a rennir ar gyfer pob iaith. Mae gwasanaethau newydd yn cael eu cynhyrchu o dempled sy'n tynnu'r ffurfweddiadau hynny, felly mae pob ystorfa'n dechrau'n gydnaws. Mae CI'n rhwystro uniadau ar unrhyw doriad, ac mae adolygiad chwarterol yn llywodraethu newidiadau rheol. Mae amser sefydlu ar gyfer peirianwyr sy'n symud rhwng timau'n gostwng yn amlwg, oherwydd bod pob ystorfa'n edrych yn gyfarwydd.

**Llywodraeth.** Mae asiantaeth sector cyhoeddus sy'n moderneiddio system etifeddol yn mandadu set reolau dolennu hygyrchedd a diogelwch fel rhan o'i ofynion awdurdod-i-weithredu (ATO), y gymeradwyaeth ffurfiol sydd ei hangen i redeg y system mewn cynhyrchiad. Mae cydymffurfiaeth steil yn dod yn rhan o'r dystiolaeth archwilio: mae'r biblinell yn cynhyrchu adroddiad sy'n dangos bod pob cod a unwyd wedi pasio'r gatiau [dadansoddiad-statig](https://en.wikipedia.org/wiki/Static_program_analysis) y cytunwyd arnynt. Oherwydd bod fformatiwr yn cael ei gymhwyso'n awtomatig, mae contractwyr o sawl gwerthwr yn cynhyrchu cod cyson yn weledol, sy'n gwneud swydd cynnal hirdymor y llywodraeth yn haws ar ôl i'r contractau ddod i ben.

## Achos busnes: cymhellion, ROI, a TCO

Mae cost mabwysiadu safonau'n bennaf yn un-tro: dewis canllawiau, gwifro offer, a chymhwyso un ymrwymiad ail-fformatio cychwynnol mawr. Mae'r gost gyson yn isel, oherwydd bod gorfodaeth wedi'i hawtomeiddio. Mae cost *peidio* â mabwysiadu safonau'n gyson ac yn cyfansymu: mae pob adolygiad yn treulio munudau ar steil, mae pob sefydlu'n arafach, mae offer dadansoddiad-statig yn cynhyrchu sŵn, ac mae cod anghyson yn cuddio gwallau. Ar draws sefydliad mawr, mae'r munudau hynny'n adio i golledion cyfwerth-amser-llawn.

Mae'r enillion yn ymddangos fel llai o oediant adolygu, llai o sylwadau adolygu cysylltiedig â steil, sefydlu cyflymach, a signal uwch o offer awtomataidd. Mewn amgylcheddau rheoleiddiedig mae enillion pellach mewn parodrwydd archwilio: mae rheolaethau y gellir eu dangos, wedi'u gorfodi, yn lleihau ymdrech a risg adolygiadau cydymffurfiaeth. I wneud yr achos i arweinyddiaeth, fframiwch safonau fel lifer cost-isel, trosoledd-uchel ar gynhyrchedd datblygwyr a safiad archwilio, a rhowch rif ar gost bresennol anghysondeb gan ddefnyddio dadansoddiad sylwadau-adolygu a data arolwg sefydlu.

## Gwrth-batrymau a pheryglon

- **Steil yn cael ei ddadlau mewn adolygiad cod:** yr arwydd nad yw gorfodaeth wedi'i hawtomeiddio; symudwch y rheol i mewn i offer.
- **Y ddogfen safonau ddi-ddarllen:** mae tudalen wici heb orfodaeth yn addurniad; mae angen mecanwaith ar bob rheol.
- **Ymledu rheolau:** cannoedd o reolau pedantig sy'n arafu gwaith heb atal diffygion.
- **Llithriad ffurfweddiad:** mae pob ystorfa'n fforcio ei ffurfweddiad dolenwr ei hun nes bod "'r safon" yn golygu dim byd.
- **Fformatio'r ystorfa gyfan yng nghanol gwaith nodwedd:** mae cymysgu ymrwymiadau ail-fformatio â newidiadau rhesymeg yn dinistrio adolygu a blame; gwnewch ail-fformatio mawr mewn ymrwymiadau ynysig, wedi'u labelu'n glir.
- **Anwybyddu'r dolenwr gydag ataliadau-cwbl:** mae analluogi eang mewnlin yn arwydd o reol anghywir neu dîm sydd wedi rhoi'r gorau iddi.
- **Safonau heb berchnogaeth:** nid oes perchennog clir yn golygu na fydd rheolau byth yn esblygu ac yn pydru.

## Model aeddfedrwydd

- **Lefel 1, Cychwyn:** Mae steil fesul-awdur ac adweithiol; dim ffurfweddiadau a rennir; mae fformatio'n cael ei ddadlau mewn adolygiad ac yn cael ei setlo gan bwy bynnag sy'n poeni fwyaf y diwrnod hwnnw.
- **Lefel 2, Datblygu:** Mae timau unigol yn mabwysiadu fformatiwr a dolenwr, ond mae ffurfweddiadau a setiau rheolau'n amrywio o dîm i dîm ac o ystorfa i ystorfa, felly mae cysondeb yn stopio wrth ffiniau pob tîm.
- **Lefel 3, Safoni:** Mae ffurfweddiadau canolog a rennir fesul iaith wedi'u dogfennu a'u gorfodi ar draws y sefydliad; mae CI'n rhwystro uniadau anghydnaws; mae ystorfeydd newydd yn etifeddu'r safonau'n awtomatig drwy dempledi neu sgaffaldiau.
- **Lefel 4, Rheoli:** Mae'r safon yn cael ei mesur a'i rheoli gyda data: mae cyfraddau toriad, cyfrifon ataliad, sylwadau adolygu cysylltiedig â steil, ac amser sefydlu'n cael eu holrhain yn erbyn llinellau sylfaen, ac mae newidiadau rheol yn cael eu dyrchafu neu eu diddymu ar sail y dystiolaeth honno yn hytrach na barn.
- **Lefel 5, Cerddorfa:** Mae safonau'n cael eu gwella'n barhaus ac wedi'u hintegreiddio ar draws y sefydliad; mae idiomau amlieithog a geirfa parth wedi'u dogfennu a'u gorfodi, mae gorfodaeth bron yn ddi-ffrithiant, ac mae'r set reolau'n addasu wrth i ieithoedd, offer, ac anghenion sefydliadol newid.

## Syniadau ar gyfer trafodaeth

- Ble mae'r llinell rhwng rheol orfodedig a chanllaw dogfennedig sy'n ymddiried ym marn peiriannydd?
- Sut ddylai'r sefydliad drin rheol gymunedol annwyl sy'n gwrthdaro â chyfyngiad mewnol gwirioneddol?
- Pwy sy'n berchen ar y safonau, a sut mae newidiadau rheol yn cael eu cynnig, eu dadlau, a'u cyflwyno heb darfu?
- Mewn cronfa god amlieithog, pa gonfensiynau ddylai fod yn wirioneddol gyffredinol a pha rai ddylai aros yn iaith-leol?
- Sut ydych chi'n ôl-ffitio safonau ar gronfa god etifeddol fawr heb ail-fformatio mawr-tanchwa tarfus?
- Pa rôl ddylai offer â chymorth AI ei chwarae wrth awgrymu neu orfodi idiomau y tu hwnt i fformatio mecanyddol?

## Casgliadau allweddol

- Triniwch steil fel problem wedi'i hawtomeiddio, wedi'i datrys fel bod pobl yn adolygu dylunio a chywirdeb.
- Mabwysiadwch safonau cymunedol sy'n bodoli eisoes a dogfennwch dim ond y gwahaniaethau.
- Gorfodwch ar haenau golygydd, cyn-ymrwymo, a CI, gyda CI fel y gât awdurdodol.
- Cadwch y set reolau'n fach, yn amddiffynadwy, ac wedi'i llywodraethu'n ganolog.
- Enwi ac idiomau, nid bylchau, yw lle mae darllenadwyedd wir yn cael ei ennill.

## Cyfeiriadau a darllen pellach

- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt a David Thomas, *The Pragmatic Programmer*
- Steve McConnell, *Code Complete*
- Dustin Boswell a Trevor Foucher, *The Art of Readable Code*
- Kevlin Henney (gol.), *97 Things Every Programmer Should Know*
- Google, *Google Engineering Practices* a chanllawiau steil iaith (fel esiamplau cyfeirio)
