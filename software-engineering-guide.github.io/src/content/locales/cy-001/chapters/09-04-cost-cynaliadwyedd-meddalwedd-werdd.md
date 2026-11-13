# 9.4 Cost, cynaliadwyedd, a meddalwedd gwyrdd

## Trosolwg a chymhelliant

Mae meddalwedd yn rhedeg ar seilwaith ffisegol sy'n defnyddio arian, trydan, dŵr, a deunyddiau. Am y rhan fwyaf o hanes cyfrifiadura, problem rhywun arall oedd y costau hyn: roedd cyllidebau cyfalaf yn cuddio'r caledwedd, ac roedd ynni'n anweladwy i beirianwyr. Newidiodd [cyfrifiadura cwmwl](https://en.wikipedia.org/wiki/Cloud_computing) hynny. Gwnaeth ddefnydd yn ronynnog, ar-alw, ac yn uniongyrchol briodoladwy, a drodd gost, a fwyfwy carbon, yn bryderon peirianyddol. Mae'r bennod hon yn ymdrin â dwy ddisgyblaeth gydgysylltiedig: **FinOps**, yr arfer o ddod ag atebolrwydd ariannol i wariant cwmwl amrywiol, a **[meddalwedd gwyrdd](https://en.wikipedia.org/wiki/Green_computing)**, yr arfer o adeiladu systemau sy'n gwneud yr un gwaith gyda llai o ynni ac allyriadau carbon is. Maent yn gorgyffwrdd yn helaeth, gan fod meddalwedd effeithlon fel arfer yn rhatach ac yn lanach fel ei gilydd.

I dimau mawr, mae'r ffigurau'n enfawr. Gall biliau cwmwl ar gyfer menter fawr gyrraedd degau neu gannoedd o filiynau y flwyddyn, ac mae ychydig bwyntiau o wastraff yn cynrychioli arian go iawn a allai ariannu nifer staff neu gynhyrchion. Mae [ôl troed carbon](https://en.wikipedia.org/wiki/Carbon_footprint) ystadau digidol mawr hefyd yn sylweddol, ac mae sefydliadau'n wynebu pwysau cynyddol gan reoleiddwyr, buddsoddwyr, cwsmeriaid, a'u gweithwyr eu hunain i'w fesur a'i leihau. Pan fo cannoedd o dimau'n gwneud penderfyniadau annibynnol yr un am feintiau enghraifft, cadw data, a phensaernïaeth, mae aneffeithlonrwyddau bach yn cyfansymio'n gostau ac allyriadau mawr. Mae llywodraethu sy'n gwneud cost a charbon yn weladwy ac yn atebol yn hanfodol i gadw'r ddau dan reolaeth.

Mae perthnasedd menter a llywodraeth yn uniongyrchol. Mae sefydliadau'r sector cyhoeddus yn gwario arian trethdalwyr ac yn gynyddol wedi'u rhwymo gan orchmynion cynaliadwyedd ac ymrwymiadau sero-net, felly mae dangos gweithrediad effeithlon, carbon isel yn rhwymedigaeth ariannol a pholisi fel ei gilydd. Mae mentrau'n wynebu craffu buddsoddwyr ar berfformiad amgylcheddol a phwysau cystadleuol ar farjinau. Yn y ddau leoliad, mae cost a chynaliadwyedd wedi symud o ôl-ystyriaethau i bryderon lefel-bwrdd. Y dewisiadau peirianyddol yw lle mae'r pryderon hynny'n cael eu gwireddu neu eu colli yn y pen draw.

## Egwyddorion allweddol

- **Gwnewch ddefnydd yn weladwy.** Ni allwch optimeiddio'r hyn na allwch ei weld; rhaid priodoli cost a charbon i'r timau a'r gwasanaethau sy'n eu hachosi.
- **Mae atebolrwydd yn eistedd gyda pherchnogion.** Dylai'r peirianwyr sy'n darparu adnoddau weld a pherchen ar eu heffaith gost a charbon.
- **Mae effeithlonrwydd yn gwasanaethu cost a charbon gyda'i gilydd.** Mae gwneud yr un gwaith â llai o adnoddau fel arfer yn arbed arian ac allyriadau ar yr un pryd.
- **Ail-feintiwch yn barhaus.** Mae galw'n newid, felly rhaid ailedrych ar ddarpariaeth, nid ei gosod unwaith a'i anghofio.
- **Mae gan garbon amser a lle.** Mae'r un cyfrifiad yn allyrru mwy neu lai yn dibynnu ar pryd a ble y cynhyrchir y trydan.
- **Cydbwyswch y triawd.** Mae cost, perfformiad, a dibynadwyedd yn cyfaddawdu â'i gilydd; optimeiddiwch yn fwriadol, nid yn ddall.
- **Dyluniwch ar gyfer effeithlonrwydd yn gynnar.** Mae dewisiadau pensaernïol yn dominyddu cost a charbon hirdymor yn llawer mwy na thiwnio cyfnod-hwyr.

## Argymhellion

### Sefydlu gweladwyedd, optimeiddio, ac atebolrwydd FinOps

Mae FinOps yn mynd rhagddo mewn tri chyfnod ailadroddus. **Hysbysu**: adeiladwch weladwyedd trwy dagio, dyraniad, a dangosfyrddau, fel bod pob cost yn cael ei phriodoli i dîm, gwasanaeth, a phwrpas busnes, a bod costau a rennir yn cael eu rhannu'n deg. **Optimeiddio**: dilëwch wastraff (adnoddau segur ac amddifad), ail-feintiwch wasanaethau a ddarparwyd yn ormodol, mabwysiadwch ostyngiadau seiliedig-ar-ymrwymiad megis cadwedigaethau neu gynlluniau arbed ar gyfer llwyth-sylfaen sefydlog, a defnyddiwch gapasiti smotyn neu ragflaenadwy ar gyfer gwaith y gellir ei ymyrryd. **Gweithredu**: mewnblannwch gost i mewn i arfer peirianyddol arferol gyda chyllidebau, rhybuddion anghysondeb, rhagolygon, ac adolygiadau rheolaidd. Yn anad dim, rhowch ddata cost o flaen y peirianwyr sy'n ei greu. Gwnewch effeithlonrwydd yn nod a rennir gan beirianneg, cyllid, a chynnyrch, nid pryder cyllid-yn-unig.

### Adeiladu meddalwedd ymwybodol-o-garbon ac effeithlon-o-ran-ynni

Mae gan leihau carbon dri lifer. **Effeithlonrwydd ynni**: ysgrifennwch a ffurfweddwch feddalwedd i wneud yr un gwaith â llai o gylchoedd CPU, llai o gof, a llai o symudiad data, trwy algorithmau gwell, storfa dros dro, ac osgoi cyfrifiad diangen. **Effeithlonrwydd caledwedd**: defnyddiwch adnoddau'n llawn trwy ddefnydd uwch, cyfuno, a chaledwedd modern effeithlon, gan fod capasiti segur yn dal i dynnu pŵer ac yn ymgorffori carbon gweithgynhyrchu. **Ymwybyddiaeth garbon**: symudwch lwythi gwaith hyblyg mewn amser a lle i pryd a ble mae'r grid yn lanach, er enghraifft rhedeg swyddi batsh pan fo cynhyrchu adnewyddadwy'n uchel, neu mewn rhanbarthau â thrydan carbon-isel. Mesurwch gan ddefnyddio dulliau cydnabyddedig megis y fanyleb Software Carbon Intensity. Ffafriwch ddarparwyr a rhanbarthau ag ymrwymiadau adnewyddadwy cryf ac adrodd tryloyw.

### Dylunio pensaernïaethau cynaliadwy ac ail-feintio

Mae pensaernïaeth yn pennu'r llawr ar gyfer cost a charbon. Ffafriwch ddyluniadau elastig sy'n graddio i alw gwirioneddol ac yn graddio i sero pan fo'n segur, fel na thelwch byth am gadw capasiti heb ei ddefnyddio'n rhedeg. Mae [di-weinydd](https://en.wikipedia.org/wiki/Serverless_computing) a [graddio-awtomatig](https://en.wikipedia.org/wiki/Autoscaling) yn lleihau gwastraff ar gyfer llwythi gwaith pigog, a gall gwasanaethau a reolir wella defnydd trwy [amldenantiaeth](https://en.wikipedia.org/wiki/Multitenancy). Ail-feintiwch gyfrifiadura, storio, a chronfeydd data yn erbyn defnydd gwirioneddol yn hytrach na darparu gormodol ofnus. Gosodwch bolisïau cylch bywyd data fel bod data oer yn symud i haenau rhatach, ynni-is neu'n cael ei ddileu. Mae lleihau cyfaint data a throsglwyddiad rhwydwaith yn torri cost storio ac ynni symud bitiau fel ei gilydd. Triniwch effeithlonrwydd fel gofyniad dylunio, wedi'i adolygu ochr yn ochr â pherfformiad a dibynadwyedd.

### Cydbwyso cost, perfformiad, a dibynadwyedd yn fwriadol

Mae cost, perfformiad, a dibynadwyedd yn ffurfio triawd. Gwthiwch un yn galed, ac fel arfer byddwch yn trethu'r lleill: mae mwy o ddiswyddiant ac oedi is yn costio mwy, ac yn aml yn defnyddio mwy o ynni. Gwnewch y cyfaddawdau hyn yn amlwg a'u cydio wrth werth busnes. Defnyddiwch SLOau ([amcanion lefel gwasanaeth](https://en.wikipedia.org/wiki/Service-level_objective)) i ddiffinio faint o ddibynadwyedd a pherfformiad y mae'r gwasanaeth mewn gwirionedd ei angen, yna darparwch ar gyfer y targed hwnnw yn hytrach na gor-orffennu popeth yn unffurf. Gall llwythi gwaith heb fod yn feirniadol a mewnol dderbyn ffurfweddiadau rhatach, llai diswyddiant, mwy carbon-hyblyg. Cadwch ddarpariaeth premiwm ar gyfer yr hyn sy'n wirioneddol ei haeddu.

### Llywodraethu heb fygu

Darparwch giatiau gwarchod, nid giatiau. Gall timau llwyfan canolog gynnig rhagosodiadau effeithlon, gorfodaeth tagio, rhybuddion cyllideb, a dangosfyrddau hunanwasanaeth, tra'n gadael penderfyniadau dydd-i-ddydd gyda'r timau sy'n berchen ar y llwythi gwaith. Gosodwch dargedau ar draws y sefydliad ar gyfer effeithlonrwydd cost a lleihau carbon, adroddwch gynnydd yn dryloyw, a dathlwch arbedion. Osgowch fiwrocratiaeth cymeradwyo trwm sy'n arafu cyflenwi. Y nod yw gwneud y dewis effeithlon yn rhagosodiad hawdd.

## Cyfaddawdau: manteision ac anfanteision

| Penderfyniad | Manteision | Anfanteision |
|---|---|---|
| Gostyngiadau ymrwymiad | Arbedion mawr ar lwyth-sylfaen | Clymu i mewn, risg os yw galw'n symud |
| Capasiti smotyn/rhagflaenadwy | Cyfrifiadura rhataf, defnyddio grid sbâr | Torrion, cymhlethdod ychwanegol |
| Ail-feintio ymosodol | Cost a charbon is | Risg o dan-ddarpariaeth dan bigau |
| Amserlennu ymwybodol-o-garbon | Allyriadau is | Swyddi wedi'u gohirio, ymdrech beirianyddol |
| Diswyddiant aml-ranbarth | Dibynadwyedd uwch | Mwy o gost, ynni, a charbon |

Y cyfaddawd unedig yw bod dibynadwyedd a pherfformiad mwyaf yn anaml yn cyd-daro â chost a charbon lleiaf. Mae systemau diswyddiant, bob amser-ymlaen, oedi-isel yn ddrud ac yn newynog am ynni, felly mae gor-orffennu unffurf yn gwastraffu arian ac allyriadau fel ei gilydd ar lwythi gwaith nad oes eu hangen arnynt. Y ddisgyblaeth yw ail-feintio uchelgais i werth busnes gan ddefnyddio SLOau, gan wario adnoddau premiwm dim ond lle maent yn bwysig. Mae gostyngiadau ymrwymiad a chapasiti smotyn yn cynnig arbedion go iawn, ond maent yn cyflwyno risg clymu-i-mewn a thorri y mae'n rhaid i chi ei reoli. Mae amserlennu ymwybodol-o-garbon yn arbed allyriadau, ond dim ond yn addas i lwythi gwaith sy'n goddef oedi neu adleoli.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Pa gyfran o'ch gwariant cwmwl sydd mewn gwirionedd wedi'i dagio a'i briodoli i dîm heddiw?** Cyfnod hysbysu FinOps yw'r sylfaen: ni allwch optimeiddio'r hyn na allwch ei weld, ac mae gwariant heb ei dagio, heb ei ddyrannu, yn golygu nad oes neb yn berchen ar y gwastraff. Dewch â'r ffigur cwmpasiad go iawn i'r drafodaeth, nid dyhead, a rhestr yr eitemau llinell heb eu tagio mwyaf. I sefydliad mawr lle mae cannoedd o dimau'n darparu'n annibynnol yr un, mae cyfradd priodoliad isel yn golygu bod aneffeithlonrwyddau a rennir yn cyfansymio'n anweledig i mewn i filiynau. Mewn lleoliadau llywodraeth a menter, priodoliad hefyd yw sut yr ydych yn amddiffyn gwariant trethdalwr neu gyfranddaliwr a sut yr ydych yn dyrannu costau cyfran-deg platfformau a rennir. Mae'r ateb yn gosod eich symudiad cyntaf: os yw cwmpasiad yn isel, mae gorfodaeth tagio a dyraniad yn dod cyn unrhyw ail-feintio, gan fod optimeiddio heb weladwyedd yn ddyfalu.

2. **Faint o'ch llwyth-sylfaen sy'n cael ei orchuddio gan ostyngiadau ymrwymiad, a beth sy'n digwydd i'r ymrwymiadau hynny os yw galw'n symud?** Mae cadwedigaethau a chynlluniau arbed yn cyflenwi arbedion mawr ar lwyth-sylfaen sefydlog, ond maent yn cyflwyno clymu-i-mewn, felly mae prynu'n rhy ymosodol yn troi gostyngiad yn atebolrwydd pan fo cynnyrch yn dod i ben neu'n mudo. Dewch â'r ffigurau: eich canran cwmpasiad ymrwymedig, tuedd eich llwyth-sylfaen, a'r llwythi gwaith sydd fwyaf tebygol o newid siâp yn y flwyddyn nesaf. Y ddisgyblaeth yw ymrwymo dim ond y llawr yr ydych yn hyderus sy'n parhau, gorchuddio'r haen amrywiol ag ar-alw neu smotyn, ac ailedrych wrth i alw esblygu. I fenter fawr mae hwn yn benderfyniad arddull-trysorlys ag agoredrwydd ariannol go iawn, felly dylai cyllid a pheirianneg berchen arno gyda'i gilydd yn hytrach nag ochr unigol. Dylai'r ateb wahanu eich llwyth-sylfaen parhaol oddi wrth eich galw ansicr a meintioli ymrwymiadau i'r cyntaf.

3. **Faint o'ch fflyd sy'n eistedd yn segur, ac a ydych yn cyfrif carbon gweithgynhyrchu ymgorfforedig neu ddim ond yr ynni y mae'n ei losgi tra'n rhedeg?** Mae capasiti segur yn dal i dynnu pŵer ac yn cario'r carbon gweithgynhyrchu a wariwyd eisoes i adeiladu'r caledwedd, felly mae canolbwyntio dim ond ar ynni gweithredol tra'n darparu gormodol yn colli rhan wirioneddol o'r ôl troed. Dewch â data defnydd: cyfartaledd a brig, y bwlch rhwng darparedig a defnyddiedig, a lle mae graddio-i-sero neu gyfuno'n bosibl. Mae defnydd uwch yn gwasanaethu cost a charbon ar unwaith, sef llinyn drwodd y bennod hon, felly gwastraff segur yw'r ennill glanaf sydd gennych. I sefydliadau dan orchymyn sero-net, mesur carbon gonest sy'n cynnwys allyriadau ymgorfforedig yw'r hyn sy'n gwahanu cynnydd go iawn oddi wrth wyrdd-olchi sy'n gwahodd ymateb rheoleiddiol ac enw da. Dylai'r ateb dargedu eich llwythi gwaith defnydd-isaf ar gyfer cyfuno, graddio-awtomatig, neu raddio-i-sero, a gosod dull mesur nad yw'n distaw anwybyddu carbon gweithgynhyrchu.

4. **A yw eich peirianwyr yn gweld cost a charbon eu gwasanaethau eu hunain, ac a yw unrhyw un yn gweithredu ar yr hyn a welant?** Nid yw gweladwyedd yn talu ar ei ganfed ond pan gyrhaedda'r bobl sy'n darparu adnoddau ac yn newid eu hymddygiad, felly mae dangosfwrdd y mae cyllid yn ei adolygu'n fisol ond na fydd peirianwyr byth yn ei agor yn addurn, nid yn atebolrwydd. Mae'r dynfa gystadleuol yn real: mae timau llwyfan eisiau rheolaeth ganolog ac adrodd glân, tra bo timau cyflenwi'n digio unrhyw beth sy'n teimlo fel gwyliadwriaeth neu giât arall ar gyflenwi. Dewch â thystiolaeth o bwy sy'n edrych mewn gwirionedd ar ddata cost a charbon, pa mor aml, ac a yw unrhyw ail-feintio neu lanhau wedi dilyn ohono yn y chwarter diwethaf. I sefydliad mawr lle mae cannoedd o dimau'n darparu'n annibynnol, y gwahaniaeth rhwng signal y mae peirianwyr yn berchen arno ac adroddiad y maent yn ei anwybyddu yw'r gwahaniaeth rhwng arbedion cyfansymiol a gwastraff cyfansymiol. Mewn lleoliadau menter a llywodraeth, rhowch economeg uned (cost a charbon fesul cais, fesul cwsmer, neu fesul achos) o flaen y tîm perchnogol, gan fod ffigur cyfanredol yn amddiffyn cyllideb ond mae ffigur fesul-uned yn newid penderfyniad dylunio.

5. **Pa rai o'ch llwythi gwaith sy'n wirioneddol hyblyg mewn amser neu ranbarth, a beth fyddai ei angen i'w hamserlennu lle mae'r grid yn lanach?** Mae amserlennu ymwybodol-o-garbon yn symud gwaith hyblyg i pryd a ble mae trydan yn garbon-isel, ond dim ond yn addas i swyddi sy'n goddef oedi neu adleoli, felly'r gwaith cyntaf yw gwahanu gwaith batsh gwir-ohiradwy oddi wrth unrhyw beth wynebu-defnyddiwr neu oedi-glwm. Y cyfaddawd yw bod symud swyddi ar draws rhanbarthau neu ffenestri oddi-frig yn ychwanegu ymdrech beirianyddol, cost trosglwyddo data, ac weithiau risg preswyliad-data a all bwyso'n drymach na'r allyriadau a arbedwyd. Dewch â rhestr ymgeisiol o swyddi batsh a dadansoddeg, eu goddefiant oedi, eu cyfyngiadau preswyliad-data, a dwyster carbon y rhanbarthau y gallwch eu rhedeg ynddynt yn gyfreithlon. I fentrau mae hwn yn optimeiddiad cymedrol ar ben ail-feintio, felly dilyniannwch ef ar ôl y sylfeini cost yn hytrach na chynt. Mewn llywodraeth, gall rheolau preswyliad-data a sofraniaeth wahardd symud data dinasyddion ar draws ffiniau ni waeth pa mor lân yw'r grid, felly mae'r dewis rhanbarth yn gwestiwn cyfreithiol cyn ei fod yn un carbon.

6. **Pa dargedau effeithlonrwydd a chynaliadwyedd yr ydych wedi'u gosod, ac a ydynt wedi'u hysgrifennu fel na all eu taro dorri dibynadwyedd yn ddistaw?** Mae targedau'n canolbwyntio ymdrech, ond mae nod cost neu garbon bras yn gwahodd yr ymddygiad anghywir: mae timau'n tan-ddarparu, yn stripio diswyddiant, neu'n gohirio gwaith mewn ffyrdd sy'n cyfnewid arbediad bach am ddigwyddiad mawr. Y tyndra yw rhwng ffigur uchelgeisiol o'r brig i lawr y gall arweinyddiaeth ei adrodd a tharged o'r gwaelod i fyny wedi'i seilio ar SLOau gwirioneddol pob gwasanaeth, felly rhaid cysoni'r ddau yn hytrach na'u gorfodi. Dewch â'ch targedau presennol, y llinell sylfaen y'u mesurir yn eu herbyn, a'r giatiau gwarchod dibynadwyedd sy'n atal optimeiddio rhag erydu'n ddistaw yr hyn y mae gwasanaeth wir ei angen. I sefydliad mawr, rhaid i dargedau cyfanredol ddadelfennu'n deg i dimau y mae eu llwythi gwaith yn wahanol, felly ni ddylai gwasanaeth taliad wynebu-cwsmer a swydd adrodd fewnol gario'r un disgwyliad effeithlonrwydd. Mewn cyd-destunau menter a llywodraeth lle mae ffigurau cynaliadwyedd yn ymddangos mewn datgeliadau cyhoeddus, cydiwch bob ffigur a adroddir wrth ddull mesur archwiliadwy, gan fod targed na allwch ei amddiffyn dan graffu'n atebolrwydd, nid yn gyflawniad.

## Lens sector

**Cwmni newydd.** Cost yw redfa, felly gall un prynhawn o dagio ac un rhybudd cyllideb brynu mis arall i chi cyn i chi godi arian eto. Hepgorwch broses FinOps a chyfrifyddu carbon yn gyfan gwbl; gwyliwch y bil, lladdwch adnoddau segur, a dewiswch lwyfan a reolir sy'n graddio i sero fel eich bod yn talu am lwyth yn hytrach na chapasiti'n eistedd yn barod. Eich adnodd prinnaf yw sylw peirianyddol, felly awtomeiddiwch y gwastraff amlwg a symudwch ymlaen.

**Busnes bach.** Nid oes gennych arbenigwr FinOps a chyllideb dynn, felly pwyswch ar yr offer cost y mae eich darparwr cwmwl eisoes yn eu rhoi i chi yn hytrach na phrynu llwyfan pwrpasol. Gosodwch rybudd cyllideb misol, trowch ymlaen argymhellion ail-feintio'r darparwr, a ffafriwch wasanaethau a reolir a di-weinydd sy'n plygu effeithlonrwydd gweithredol i mewn i'r pris. Triniwch gynaliadwyedd fel dewis rhanbarth carbon-isel a rhagosodiad effeithlon, nid fel rhaglen adrodd y mae'n rhaid i chi ei staffio.

**Menter.** Y broblem yw llywodraethu ar draws llawer o dimau: tagio cyson, dyraniad teg o gostau platfform a rennir, strategaeth gostyngiad-ymrwymiad y mae cyllid a pheirianneg yn berchen arni ar y cyd, a chost a charbon yn dod i'r amlwg fel signalau y mae pob tîm yn eu gweld. Safonwch ragosodiadau effeithlon a dull mesur fel nad yw cannoedd o benderfyniadau darpariaeth annibynnol yn cyfansymio'n wastraff, a rheolwch wariant cwmwl ac allyriadau fel portffolio â thargedau, rhybuddion anghysondeb, ac adrodd tryloyw yn hytrach na gwasgariad o optimeiddiadau lleol.

**Llywodraeth.** Mae rheolau caffael, tryloywder, ac atebolrwydd cyhoeddus yn siapio pob dewis. Rydych yn gwario arian trethdalwyr ac yn aml wedi'ch rhwymo gan orchymyn sero-net, felly rhaid i chi ddangos darbodusrwydd ariannol a chynnydd allyriadau wedi'i archwilio fel ei gilydd, sy'n golygu mesur carbon gonest sy'n cynnwys caledwedd ymgorfforedig yn hytrach na gwyrdd-olchi. Gall rheolau preswyliad-data a sofraniaeth gyfyngu pa ranbarthau y gallwch eu defnyddio ni waeth pa mor lân yw'r grid, ac efallai y bydd angen cyhoeddi metrigau effeithlonrwydd ac allyriadau ar gyfer craffu cyhoeddus, felly dewiswch ddulliau mesur y gallwch eu hamddiffyn dan archwiliad.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd cyfnod-hedyn yn gwylio ei fil cwmwl yn dyblu mewn deufis ac ni all ddweud pam. Mae sylfaenydd yn treulio prynhawn yn tagio pob adnodd yn ôl nodwedd ac yn troi ymlaen rybudd cyllideb syml. Mae'r tagiau'n datgelu clwstwr llwyfannu anghofiedig a chronfa ddata rhy fawr yn rhedeg rownd y cloc ar gyfer swydd nosol. Mae cau'r clwstwr a symud y swydd i redeg amserlenedig oddi-frig ar enghraifft lai yn torri'r bil o draean, sy'n prynu i'r tîm fis arall o redfa.

**Menter.** Mae manwerthwr rhyngwladol ag ystâd cwmwl fawr, wasgaredig yn sefydlu arfer FinOps. Mae'n gorfodi tagio, yn dyrannu pob cost i dîm cynnyrch, ac yn dod â gwariant i'r amlwg mewn dangosfyrddau y mae peirianwyr yn eu gweld yn ddyddiol. O fewn blwyddyn mae'n dileu adnoddau segur, yn ail-feintio gwasanaethau a ddarparwyd yn ormodol, ac yn prynu cynlluniau arbed ar gyfer llwyth-sylfaen sefydlog, gan dorri gwariant cwmwl o oddeutu chwarter. Yna mae'n amserlennu swyddi batsh dadansoddeg nosol i redeg mewn rhanbarthau carbon-is ac oriau oddi-frig, gan leihau cost ac allyriadau fel ei gilydd, ac yn adrodd yr arbedion carbon yn ei ddatgeliad cynaliadwyedd blynyddol.

**Llywodraeth.** Rhaid i asiantaeth lywodraeth sy'n gweithredu gwasanaethau dinasyddion dan orchymyn sero-net cenedlaethol ddangos darbodusrwydd ariannol ag arian trethdalwyr a chynnydd tuag at dargedau allyriadau fel ei gilydd. Mae'n ail-feintio ac yn cyfuno llwythi gwaith, yn gosod polisïau cadw-data sy'n symud cofnodion a gyrchir yn anfynych i storfa oer, ynni-isel, ac yn dewis rhanbarthau cwmwl a bwerir gan gyfrannau uchel o drydan adnewyddadwy. Mae'n mesur dwyster carbon ei brif wasanaethau ac yn cyhoeddi metrigau effeithlonrwydd ac allyriadau ar gyfer atebolrwydd cyhoeddus. Mae rhagosodiadau effeithlon a dangosfyrddau hunanwasanaeth yn gadael i ddwsinau o dimau cyflenwi wneud dewisiadau cynaliadwy heb dagfeydd canolog.

## Achos busnes: cymhellion, ROI, a TCO

Mae'r elw yma'n anarferol o uniongyrchol. Mae optimeiddio FinOps yn gyffredin yn lleihau gwariant cwmwl o bumed i draean gydag ymdrech ddisgybledig, arbediad sy'n llifo'n syth i'r gwaelodlin, neu i ariannu gwaith newydd. Mae lleihau carbon fwyfwy'n cario gwerth ariannol hefyd, trwy brisio carbon a osgowyd, cymhwysedd ar gyfer contractau â gofynion cynaliadwyedd, a risg reoleiddiol ac enw da wedi'i leihau. Gan fod effeithlonrwydd yn gostwng cost a charbon ar unwaith, mae un buddsoddiad mewn gweladwyedd ac ail-feintio'n talu ar ei ganfed ar y ddau ddimensiwn.

Rhaid i gyfanswm cost perchnogaeth gyfrif cost mabwysiadu: offer ar gyfer gweladwyedd cost a charbon, y staff FinOps neu lwyfan i redeg yr arfer, a'r amser peirianyddol i ail-feintio ac ail-bensaernïo. Mae'r rhain yn gymedrol o'u cymharu â'r arbedion, ac maent yn crebachu wrth i ragosodiadau effeithlon ddod yn fewnblanedig. Mae cost peidio â mabwysiadu'n cyfansymio'n ddistaw: biliau cwmwl direol sy'n tyfu'n gyflymach na'r busnes, gwastraff nad yw byth yn dod i'r amlwg gan nad oes neb yn berchen arno, ac agoredrwydd rheoleiddiol, buddsoddwr, ac enw da cynyddol ar gynaliadwyedd. I wneud yr achos i arweinyddiaeth, cyflwynwch wariant presennol a'i lwybr twf, y gwastraff amcangyfrifedig, ac arbedion meincnod o fabwysiadu FinOps. Yna parwch ef â gwerth lleihau allyriadau a chydymffurfiaeth. Fframiwch gost a chynaliadwyedd fel yr un fenter effeithlonrwydd wedi'i weld trwy ddau lens, fel nad oes rhaid i'r busnes ddewis rhwng arbed arian a thorri carbon.

## Gwrth-batrymau a pheryglon

- **Dim priodoliad cost.** Mae gwariant heb ei dagio, heb ei ddyrannu, yn golygu nad oes neb yn berchen ar wastraff ac na all neb ei optimeiddio.
- **Darparu gosod-ac-anghofio.** Mae meintioli adnoddau unwaith a byth ailedrych arnynt yn gwarantu drifft i mewn i ordarpariaeth.
- **FinOps cyllid-yn-unig.** Mae trin cost fel pryder cefn-swyddfa yn hytrach na signal peirianyddol yn methu, gan mai peirianwyr sy'n gwneud y penderfyniadau sy'n gyrru gwariant.
- **[Gwyrdd-olchi](https://en.wikipedia.org/wiki/Greenwashing).** Mae hawlio cynaliadwyedd heb fesur yn gwahodd ymateb rheoleiddiol ac enw da.
- **Effeithlonrwydd ar draul dibynadwyedd.** Mae torri mor ymosodol fel bod gwasanaethau'n methu dan lwyth yn cyfnewid arbediad bach am ddigwyddiad mawr.
- **Anwybyddu carbon ymgorfforedig.** Mae canolbwyntio dim ond ar ynni gweithredol tra'n darparu gormodol o galedwedd segur yn colli'r ôl troed gweithgynhyrchu.
- **Giatiau biwrocrataidd.** Mae prosesau cymeradwyo trwm ar gyfer gwariant yn arafu cyflenwi ac yn gwthio timau i weithio o amgylch llywodraethu.

## Model aeddfedrwydd

**Lefel 1, Cychwyn.** Mae costau cwmwl yn syndod ar y bil misol. Nid oes tagio, dyraniad, na ymwybyddiaeth garbon, ac mae darpariaeth yn hael ac yn anaml wedi'i hailedrych. Mae gwastraff yn anweladwy gan nad oes neb yn berchen arno, ac mae unrhyw lanhau sy'n digwydd yn ymateb i sioc bil yn hytrach nag yn arfer.

**Lefel 2, Datblygu.** Mae gweladwyedd cost sylfaenol a thagio'n bodoli, a digwydd rhywfaint o ail-feintio a glanhau adnoddau segur, ond mae cwmpasiad a thrylwyredd yn amrywio'n eang rhwng timau. Mae ychydig grwpiau'n gwylio eu gwariant ac yn ceisio rhanbarthau carbon-isel; nid yw eraill yn gwneud yr un o'r naill na'r llall. Cydnabyddir cynaliadwyedd ond ni chaiff ei fesur, ac mae arferion da'n dibynnu ar fenter unigol yn hytrach nag unrhyw ddisgwyliad a rennir.

**Lefel 3, Safoni.** Mae arfer FinOps wedi'i dogfennu a'i gymhwyso ar draws y sefydliad: gorfodir tagio, dyrennir costau a rennir yn ôl dull cytunedig, ac mae cyllidebau, rhagolygon, a rhybuddion anghysondeb yn safonol. Mae gostyngiadau ymrwymiad ac ail-feintio'n dilyn llyfr chwarae diffiniedig, a mesurir carbon ar gyfer gwasanaethau mawr gan ddefnyddio dull cydnabyddedig megis y fanyleb Software Carbon Intensity, gyda dewisiadau rhanbarth ac amserlennu'n cael eu hystyried yn gyson yn hytrach nag achos wrth achos.

**Lefel 4, Rheoli.** Mesurir a rheolir cost a charbon yn erbyn llinellau sylfaen. Mae timau'n olrhain economeg uned (cost a charbon fesul cais, fesul cwsmer, neu fesul achos), defnydd gan gynnwys amcangyfrifon segur a charbon-ymgorfforedig, cwmpasiad ymrwymiad yn erbyn llwyth-sylfaen, a chywirdeb rhagolwg, y cyfan wedi'u hadrodd yn erbyn targedau sefydliadol. Mae anghysonderau'n sbarduno ymchwiliad, adolygir effeithlonrwydd a chydymffurfiad SLO gyda'i gilydd fel nad yw optimeiddio byth yn erydu dibynadwyedd yn ddistaw, a gwneir penderfyniadau bwrw ymlaen neu beidio ar ddarpariaeth ar y data hwn yn hytrach na greddf.

**Lefel 5, Cyfundrefnu.** Mae cost a charbon yn signalau peirianyddol parhaus, wedi'u perchnogi, wedi'u gwifro i mewn i arfer dyddiol. Mae rhagosodiadau effeithlon, ail-feintio awtomataidd, ac amserlennu ymwybodol-o-garbon yn norm, ac mae'r sefydliad yn ailgydbwyso ei ystâd yn barhaus wrth i alw, prisiau, a dwyster grid newid. Cyfaddawdir cost, perfformiad, a dibynadwyedd yn fwriadol trwy SLOau, mae metrigau cynaliadwyedd yn bwydo adrodd cyhoeddus a buddsoddwr â dulliau archwiliadwy, ac mae'r arfer yn addasu wrth i'r busnes, y farchnad, a rheoliad esblygu.

## Syniadau ar gyfer trafodaeth

- Pwy ddylai fod yn berchen ar gost cwmwl yn eich sefydliad: cyllid, tîm FinOps canolog, neu'r timau peirianyddol sy'n darparu adnoddau?
- Sut yr ydych yn priodoli costau platfform a rennir yn deg ar draws llawer o dimau defnyddio?
- Ble mae'r cydbwysedd cywir rhwng arbedion cost a'r dibynadwyedd neu berfformiad y gallech ei aberthu i'w cael?
- Sut y byddech yn mesur ôl troed carbon eich gwasanaethau, a faint yr ydych yn ymddiried yn y data sydd ar gael?
- Pa rai o'ch llwythi gwaith sy'n ddigon hyblyg ar gyfer amserlennu ymwybodol-o-garbon mewn amser neu ranbarth?
- Sut yr ydych yn gosod targedau effeithlonrwydd a chynaliadwyedd sy'n cymell timau heb annog tan-ddarpariaeth beryglus?

## Casgliadau allweddol

- Trodd cwmwl gost a charbon yn bryderon peirianyddol; gweladwyedd a pherchnogaeth yw sylfaen rheoli'r ddau.
- Mae FinOps yn gweithio mewn tri chyfnod: hysbysu (gweladwyedd), optimeiddio (ail-feintio a gostyngiad), a gweithredu (mewnblannu mewn arfer).
- Mae meddalwedd effeithlon fel arfer yn arbed arian a charbon gyda'i gilydd, felly triniwch hwy fel un fenter â dau lens.
- Lleihewch garbon trwy effeithlonrwydd ynni, defnydd caledwedd uwch, ac amserlennu ymwybodol-o-garbon mewn amser a lle.
- Mae pensaernïaeth ac ail-feintio'n dominyddu cost a charbon hirdymor; dyluniwch ar gyfer elastigedd a graddio-i-sero.
- Cydbwyswch gost, perfformiad, a dibynadwyedd yn fwriadol gan ddefnyddio SLOau, a llywodraethwch â giatiau gwarchod yn hytrach na giatiau.

## Cyfeiriadau a darllen pellach

- J.R. Storment, Mike Fuller, *Cloud FinOps: Collaborative, Real-Time Cloud Financial Management*
- FinOps Foundation, *FinOps Framework* documentation
- Green Software Foundation, *Principles of Green Software Engineering* and *Software Carbon Intensity (SCI) Specification*
- Anne Currie, Sarah Hsu, Sara Bergman, *Building Green Software*
- Adrian Cockcroft, writings on cloud efficiency and sustainability
- The Shift Project, *Lean ICT: Towards Digital Sobriety*
