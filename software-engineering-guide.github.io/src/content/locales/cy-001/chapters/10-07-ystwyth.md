# 10.7 Agile

## Trosolwg a chymhelliant

Meddylfryd ar gyfer cyflenwi meddalwedd (a gwerth) yn ailadroddol, yn gynyddrannol, ac mewn cydweithrediad agos â'r bobl a fydd yn ei ddefnyddio yw [Agile](https://en.wikipedia.org/wiki/Agile_software_development). Wedi'i godeiddio yn y *Manifesto for Agile Software Development* yn 2001, deellir orau nid fel proses ond fel set o **werthoedd ac egwyddorion**: blaenoriaethu unigolion a rhyngweithiadau, meddalwedd sy'n gweithio, cydweithredu â chwsmeriaid, ac ymateb i newid, dros y rhagosodiadau trwm-ar-gynllun, trwm-ar-gontract, trwm-ar-ddogfennaeth a ddaeth o'u blaen. Mae fframweithiau fel [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)), [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)), a [Extreme Programming](https://en.wikipedia.org/wiki/Extreme_programming) (XP) yn *weithrediadau* o'r meddylfryd hwnnw. Maent yn fannau cychwyn defnyddiol, ond nid y meddylfryd ei hun. Mae'r bennod hon yn ategu pennod 1.4 (ffyrdd o weithio, sy'n arolygu dulliau'n eang) drwy fynd yn ddwfn ar Agile yn benodol.

Fe'i gyrrir gan yr un grym sy'n ysgogi'r piblinellau darganfod a chyflenwi (penodau 11.1–11.2): mae gofynion ar gyfer meddalwedd yn cael eu *darganfod*, nid eu gwybod yn llawn ymlaen llaw, ac mae'r byd yn newid yn gyflymach nag y gall cynllun hir ei amsugno. Mae cyflenwi mawr-a-sydyn, cynllunio-popeth-yn-gyntaf, dro ar ôl tro yn cynhyrchu systemau sy'n hwyr, dros gyllideb, ac, waethaf oll, yn anghywir, oherwydd bod yr holl ddysgu'n cyrraedd ar y diwedd, pan mae'n ddrytaf gweithredu arno. Mae bet craidd Agile yn syml: mae cylchoedd byr o adeiladu meddalwedd go iawn, gweithredol a chael adborth go iawn yn curo cylchoedd hir o ddyfalu. Wedi'i wneud yn dda, mae'n lleihau risg yn barhaus yn hytrach na'i gohirio.

I dimau mawr, mentrau, a llywodraeth, mae Agile yn bwerus ac yn aml yn cael ei ystumio. Mae mentrau'n ei fabwysiadu ar draws cannoedd o dimau ac yn aml yn ei leihau i ddefod ("rydym yn gwneud stand-ups nawr") heb newid sut y gwneir penderfyniadau na sut y mesurir gwerth. Mae llywodraeth wedi cofleidio Agile yn fwriadol, oherwydd bod cyflenwi ailadroddol, sy'n canolbwyntio ar y defnyddiwr, yn dangos yn amlwg ei fod yn lleihau risg rhaglenni cyhoeddus mawr: cododd y U.S. Digital Service a'i *Digital Services Playbook*, Government Digital Service a Service Standard y DU, a diwygiadau caffael ystwyth i gyd yn rhannol mewn ymateb i fethiannau [rhaeadr](https://en.wikipedia.org/wiki/Waterfall_model) proffil uchel. Mae'r wobr yn real. Felly hefyd y mae'r modd methiant o "agile mewn enw yn unig."

## Egwyddorion allweddol

- **Gwerthfawrogwch bedwar gwerth y Manifesto** (pobl, meddalwedd sy'n gweithio, cydweithredu, ac ymatebolrwydd) dros arteffactau proses.
- **Cyflenwch feddalwedd sy'n gweithio yn aml** mewn cynyddrannau bach; meddalwedd sy'n gweithio yw prif fesur cynnydd.
- **Croesawwch newid**, hyd yn oed yn hwyr; mae addasadwyedd yn nodwedd, nid yn fethiant.
- **Adeiladwch o gwmpas timau cymhellol, grymusedig, hunan-drefnu.**
- **Cydweithredwch yn barhaus â defnyddwyr a rhanddeiliaid.**
- **Myfyriwch a gwellwch** ar gyflymder rheolaidd.
- **Cynhaliwch gyflymder dynol** a rhagoriaeth dechnegol: mae cyflymder heb grefft yn cwympo.

## Argymhellion

### Angori ar werthoedd ac egwyddorion, nid seremonïau

Yr argymhelliad Agile pwysicaf un yw arwain gyda'r *pam*. Nid yw tîm sy'n cynnal stand-up dyddiol, adolygiad sbrint, a retrospective, ond sy'n dal i ymrwymo i gwmpas sefydlog ar ddyddiad sefydlog, yn cuddio newyddion drwg, ac na fydd byth yn newid y cynllun, yn ystwyth. Mae'n rhaeadr gyda chyfarfodydd. Defnyddiwch y deuddeg egwyddor fel rhestr wirio ar gyfer ystwythder gwirioneddol. A ydych yn cyflenwi meddalwedd sy'n gweithio'n aml? A allwch chi groesawu newid yn yr ailadroddiad nesaf? A yw'r tîm yn penderfynu *sut* i wneud y gwaith? A yw'r cwsmer wir yn rhan o'r broses? Os nad yw'r seremonïau'n cynhyrchu'r canlyniadau hynny, trwsiwch y canlyniadau, nid y seremonïau.

### Dewis fframwaith fel man cychwyn, nid crefydd

Dewiswch fframwaith sy'n addas i'r gwaith a'i addasu:

- **Scrum:** sbrintiau wedi'u hamserfocsio, backlog wedi'i flaenoriaethu, a rolau diffiniedig (perchennog cynnyrch, meistr scrum, datblygwyr). Da ar gyfer cyflenwi nodweddion gyda pherchennog cynnyrch clir; gwan pan fo gwaith yn cael ei yrru'n fawr gan ymyriadau.
- **Kanban:** llif parhaus gyda therfynau gwaith-ar-y-gweill penodol a system dynnu. Da ar gyfer cefnogaeth, gweithrediadau, a chyrraedd anrhagweladwy (ac wedi'i seilio'n uniongyrchol ar theori llif a chiwio, gweler penodau 11.2, 11.3). Mae cyfyngu WIP yn byrhau amser arwain ([Deddf Little](https://en.wikipedia.org/wiki/Little%27s_law)).
- **Extreme Programming (XP):** arferion peirianneg gan gynnwys [datblygu wedi'i yrru gan brofion](https://en.wikipedia.org/wiki/Test-driven_development), [rhaglennu mewn parau](https://en.wikipedia.org/wiki/Pair_programming), [integreiddio parhaus](https://en.wikipedia.org/wiki/Continuous_integration), ailffactora, rhyddhadau bach. Yr asgwrn cefn technegol sy'n gwneud unrhyw fframwaith yn gynaliadwy.
- **Scrumban** a chymysgeddau: cyfuniadau pragmatig y mae llawer o dimau aeddfed yn cydgyfeirio arnynt.

Sgaffaldau yw fframweithiau. Cadwch yr hyn sy'n helpu, gollyngwch yr hyn nad yw, a pheidiwch byth â gadael i "dyna mae'r fframwaith yn ei ddweud" drechu "dyna pam mae'r egwyddorion yn ei ddweud."

### Mynnu rhagoriaeth dechnegol

Mae Agile heb ddisgyblaeth beirianneg yn dirywio'n gyflym i gynhyrchu cyflym o god na ellir ei gynnal, "dark scrum," lle mae timau'n sbrintio eu hunain i mewn i bwll tar o ddiffygion a [dyled dechnegol](https://en.wikipedia.org/wiki/Technical_debt). Nid yw arferion XP yn ychwanegion dewisol. Integreiddio parhaus (pennod 8.1), profi awtomataidd (pennod 2.4), ailffactora, datblygu seiliedig ar gefn (pennod 2.6), a dyluniad glân (pennod 2.2) yw'r hyn sy'n galluogi tîm i barhau i newid meddalwedd yn rhad, sef holl gynsail ystwythder. Mae cyflymder cynaliadwy'n bwysig am yr un rheswm: ni all timau wedi'u llosgi allan gynnal ansawdd nac ymatebolrwydd.

### Graddio'n ofalus, a ffafrio dad-raddio

Mae fframweithiau graddio, fel SAFe (y Scaled Agile Framework), LeSS, Nexus, a Scrum@Scale, yn cydgysylltu llawer o dimau tuag at nodau a rennir. Gallant helpu, ond maent yn cario rhybudd (yn adleisio pennod 1.4): mae fframweithiau graddio trwm yn aml yn ailgyflwyno union yr orbenion gorchymyn-a-rheolaeth, trwm-ar-gynllun yr oedd Agile i fod i'w dileu. Cyn i chi fabwysiadu fframwaith mawr, ceisiwch *ddad-raddio*. Trefnwch o gwmpas timau annibynnol, wedi'u halinio â ffrwd gyda pherchnogaeth glir a lleiafswm o ddibyniaethau traws-dîm (pennod 1.2), fel bod angen llai o beirianwaith cydgysylltu arnoch yn y lle cyntaf. Lle mae cydgysylltu wir yn angenrheidiol, ychwanegwch y strwythur ysgafnaf sy'n gweithio, a chysylltwch ef â chanlyniadau (OKRs, amcanion a chanlyniadau allweddol, pennod 11.1), nid allbwn.

### Gwneud ystwythder yn real mewn menter a llywodraeth

Gall cyflenwi addasol a chyfyngiadau sefydliadol gyd-fodoli, ond mae angen dyluniad bwriadol:

- **Llywodraethu hybrid:** craidd cyflenwi addasol y tu mewn i blisgyn cyllido/cydymffurfiaeth rhagfynegol (pennod 10.6), fel bod ailadrodd yn bodloni yn hytrach nag yn ymladd yn erbyn goruchwyliaeth.
- **Caffael ystwyth:** contractau modiwlaidd, seiliedig ar ganlyniadau a chynyddrannau byrrach yn lle un mega-gontract cwmpas sefydlog; dyma lle mae Agile sector cyhoeddus yn llwyddo neu'n methu amlaf.
- **Cydymffurfio wrth fynd:** adeiladwch archwiliad, hygyrchedd (pennod 5.3), a diogelwch (pennod 4.1) i mewn i'r cynyddran drwy awtomeiddio a ffwythiannau ffitrwydd (gwiriadau awtomataidd sy'n gwirio priodweddau pensaernïol ac ansawdd yn barhaus; penodau 8.5, 1.6), nid giât hwyr.
- **Mynediad defnyddiwr go iawn:** yr anoddaf a'r pwysicaf. Mae angen cyswllt gwirioneddol ar dimau â dinasyddion neu gwsmeriaid, y mae rheolau caffael a diogelwch yn aml yn eu rhwystro.

### Gwella'n barhaus, ac ei olygu

Y retrospective yw injan wella Agile, ac mae'n ddiwerth os nad yw'n cynhyrchu unrhyw newid. Cynhaliwch retrospectives sy'n cynhyrchu nifer bach o gamau gweithredu pendant, wedi'u perchnogi, a'u cwblhau mewn gwirionedd cyn yr un nesaf. Mesurwch ganlyniadau (a symudodd y newid ganlyniad allweddol? gweler pennod 11.1) a llif (a yw amseroedd arwain yn crebachu? gweler penodau 11.2, 11.3). Peidiwch â mesur velocity: mae'n signal capasiti sy'n dod yn gelwydd y foment y byddwch yn ei ddefnyddio fel targed cynhyrchiant.

## Cyfaddawdau: manteision ac anfanteision

| Penderfyniad | Manteision | Anfanteision |
|---|---|---|
| **Agile (addasol)** | Adborth cyflym; yn amsugno newid; gwerth cynnar, parhaus | Anos sefydlogi cwmpas/cost ymlaen llaw; angen cwsmer ymgysylltiedig a disgyblaeth |
| **Rhaeadr (rhagfynegol)** | Cwmpas rhagweladwy; cyfeillgar i gontract/archwiliad | Adborth hwyr; risg mawr-a-sydyn; ffit gwael i ofynion ansicr |
| **Scrum** | Cyflymder, rolau, ffocws; wedi'i ddeall yn eang | Gorbenion seremoni; yn ei chael hi'n anodd gyda gwaith wedi'i yrru gan ymyriadau |
| **Kanban** | Llif, terfynau WIP, hyblyg; gwych ar gyfer gweithrediadau | Llai o strwythur; angen disgyblaeth i ddal terfynau |
| **Graddio trwm (SAFe)** | Yn cydgysylltu llawer o dimau; cyfarwydd i sefydliadau mawr | Gall ailgyflwyno gorchymyn-a-rheolaeth; trwm-ar-seremoni |
| **Dad-raddio / ymreolaeth tîm** | Llai o orbenion cydgysylltu; timau cyflymach | Angen cyplu isel a phlatfform/perchnogaeth cryf |

Y tyndra diffiniol yw **addasadwyedd yn erbyn rhagweladwyedd**, a'r camddehongliad clasurol yw bod Agile yn golygu "dim cynllun." Nid yw. Mae'n golygu cynllunio'n barhaus ac ymrwymo i *ganlyniadau a chyflymder* tra'n gadael i *gwmpas* hyblygu. Y trap arall sy'n ailddigwydd yw trin Agile fel proses *yn unig* (seremonïau) neu beirianneg *yn unig* (XP). Mae angen y ddau.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Yn eich cyd-destun menter neu lywodraeth, a yw eich contractau'n fodiwlaidd ac yn seiliedig ar ganlyniadau, neu a yw cyflenwi wedi'i gloi y tu mewn i un mega-gontract cwmpas sefydlog?** Caffael ystwyth yw lle mae ystwythder sector cyhoeddus yn llwyddo neu'n methu amlaf, oherwydd bod un contract pris-sefydlog, cwmpas-sefydlog yn gorfodi rhaeadr ni waeth beth mae'r timau cyflenwi'n galw eu cyfarfodydd. Mae contractau modiwlaidd, seiliedig ar ganlyniadau gyda chynyddrannau byrrach yn gadael i gwmpas hyblygu tuag at graidd gwerthfawr o fewn cyllid sefydlog, sef union y patrwm y tu ôl i lwyddiannau modern sector cyhoeddus a'r gwrthwenwyn i fethiannau mawr-a-sydyn y gorffennol. Dewch â thystiolaeth: edrychwch ar eich contractau cyfredol a gofynnwch a yw gwerthwr yn cael ei dalu am feddalwedd sy'n gweithio wedi'i ddangos neu am gwmpas sefydlog a lofnodwyd flynyddoedd yn ôl. Dylai'r ateb siapio sut rydych yn strwythuro'r caffael nesaf yn llawer mwy na pha fframwaith y mae eich timau'n ei fabwysiadu'n fewnol. Ni allwch fod yn addasol mewn cyflenwi tra bo'ch contract yn mynnu lansiad pell, popeth-neu-ddim.

2. **A yw archwiliad, hygyrchedd, a diogelwch wedi'u hadeiladu i mewn i bob cynyddran drwy awtomeiddio, neu wedi'u bolltio ymlaen fel giât hwyr?** Cydymffurfio-wrth-fynd yw'r hyn sy'n gadael i gyflenwi addasol gyd-fodoli â chyfyngiadau sefydliadol: adeiladwch y gwiriadau i mewn i'r cynyddran drwy awtomeiddio a ffwythiannau ffitrwydd yn hytrach na'u cadw ar gyfer sgrialu cyn-rhyddhau. Mae giât gydymffurfio hwyr yn ailgyflwyno'r risg mawr-a-sydyn y mae Agile yn bodoli i'w dileu, oherwydd bod y problemau drud yn ymddangos ar y diwedd pan fyddant anoddaf eu trwsio. Dewch â thystiolaeth: ar gyfer eich cynyddran ddiwethaf, gwiriwch a wiriwyd tystiolaeth hygyrchedd, diogelwch, ac archwiliad yn awtomataidd yn y biblinell neu a gafodd ei gohirio i adolygiad â llaw cyn lansio. Dylai'r ateb wthio'r priodweddau hyn i mewn i wiriadau awtomataidd parhaus, fel bod goruchwyliaeth yn cael ei bodloni gan y weithred o adeiladu yn hytrach na chan gam ar wahân. Dyma hefyd sy'n cadw rhaglen reoleiddiedig yn onest rhwng archwiliadau yn hytrach na dim ond yn yr wythnosau cyn un.

3. **Sut fyddech chi'n gwybod a yw eich timau'n sbrintio i mewn i ddyled dechnegol, a beth sy'n amddiffyn cyflymder cynaliadwy o dan bwysau lansio?** Mae Agile heb ddisgyblaeth beirianneg yn dirywio i dark scrum, lle mae timau'n sbrintio'n gyflym i mewn i bwll tar o ddiffygion a chod na ellir ei gynnal, ac ni all timau wedi'u llosgi allan gynnal ansawdd nac ymatebolrwydd. Arferion XP (integreiddio parhaus, profi awtomataidd, ailffactora, datblygu seiliedig ar gefn) yw'r hyn sy'n galluogi tîm i barhau i newid meddalwedd yn rhad, sef holl gynsail ystwythder, felly nid ydynt yn ychwanegion dewisol i'w masnachu i ffwrdd pan fydd dyddiad yn agosáu. Dewch â thystiolaeth: tracio a yw amseroedd arwain yn crebachu neu'n tyfu, a yw cyfraddau diffygion yn dringo, ac a yw'r tîm yn dawel yn gweithio oriau hwy i daro pob sbrint. Dylai'r ateb wneud rhagoriaeth dechnegol a chyflymder dynol yn anhrafodadwy, oherwydd bod cyflymder a brynwyd drwy aberthu crefft yn cwympo o fewn ychydig ailadroddiadau. Mesurwch lif a chanlyniadau, byth velocity fel targed, oherwydd y foment y byddwch yn gwneud signal capasiti'n nod cynhyrchiant mae'n dod yn gelwydd.

4. **Cyn i chi estyn am fframwaith graddio trwm, a ydych wedi ceisio lleihau'r dibyniaethau traws-dîm sy'n creu'r angen i gydgysylltu yn y lle cyntaf?** Mae hyn yn bwysicaf i sefydliad mawr, oherwydd mai'r reddf pan fo'n rhaid i lawer o dimau lansio gyda'i gilydd yw prynu fframwaith fel SAFe, LeSS, neu Scrum@Scale, ac mae peirianwaith graddio trwm yn aml yn smyglo'n ôl yr orbenion gorchymyn-a-rheolaeth, trwm-ar-gynllun y mae Agile yn bodoli i'w dileu. Mae'r ystyriaeth gystadleuol yn real: mae angen rhywfaint o gydgysylltu mewn gwirionedd, ac mae dad-raddio i mewn i dimau annibynnol, wedi'u halinio â ffrwd yn mynnu cyplu isel, perchnogaeth glir, a phlatfform aeddfed digon i adael i dimau hunanwasanaethu, nad oes gennych efallai eto. Dewch â thystiolaeth i'r drafodaeth: mapiwch y dibyniaethau gwirioneddol sy'n gorfodi timau i aros ar ei gilydd, a gofynnwch faint fyddai'n goroesi ailddyluniad bwriadol o ffiniau tîm a pherchnogaeth gwasanaeth. Mewn rhaglenni menter a llywodraeth, lle mae siart sefydliadol o ddwsinau o dimau'n gyffredin, y cwestiwn onest yw a ydych yn ychwanegu strwythur cydgysylltu i wneud iawn am bensaernïaeth a dyluniad tîm y gallech chi eu symleiddio yn lle hynny, fel bod angen llai o gydgysylltu o gwbl.

5. **A oes gan eich timau gyswllt gwirioneddol, wedi'i ailadrodd â'r dinasyddion neu'r cwsmeriaid y maent yn adeiladu ar eu cyfer, neu a yw adborth yn cyrraedd wedi'i hidlo drwy ddirprwyon?** Cydweithredu â chwsmeriaid yw un o bedwar gwerth y Manifesto, ac mae ailadroddiadau sy'n brin o gyswllt defnyddiwr go iawn yn optimeiddio'r peth anghywir yn dawel, sef y methiant drutaf y mae Agile i fod i'w atal. Y tyndra yw bod mynediad uniongyrchol yn anodd ei drefnu ar raddfa ac yn aml wedi'i rwystro gan yr union reolau caffael, preifatrwydd, a diogelwch y mae'n rhaid i sefydliadau mawr a chyhoeddus eu hanrhydeddu, felly'r llwybr hawdd yw amnewid dirprwy: dadansoddwr busnes, pwyllgor rhanddeiliaid, neu becyn ymchwil y chwarter diwethaf. Dewch â thystiolaeth: ar gyfer eich ychydig gynyddrannau diwethaf, cyfrifwch faint a ddilyswyd gan ddefnyddiwr go iawn yn defnyddio'r feddalwedd mewn gwirionedd, a faint a ddibynnodd ar farn rhywun am yr hyn y mae defnyddwyr ei eisiau. Ar gyfer gwasanaeth llywodraeth, ychwanegwch a wnaeth eich profi defnyddioldeb gyrraedd y bobl fwyaf effeithiedig, gan gynnwys defnyddwyr technoleg gynorthwyol a'r rhai â hyder digidol isel, oherwydd bod gwasanaeth cyhoeddus sy'n gweithio dim ond i'r mwyafrif hyderus wedi methu â'i rwymedigaeth atebolrwydd hyd yn oed os rhedodd pob seremoni yn ôl yr amserlen.

6. **A yw eich timau'n cael eu cyllido a'u llywodraethu o gwmpas canlyniadau a chyflymder, neu o gwmpas cwmpas sefydlog sy'n gorfodi rhaeadr yn dawel y tu ôl i'r seremonïau?** Dyma'r gwahaniaeth rhwng ystwythder gwirioneddol ac agile ffug, ac fe'i penderfynir uwchben y tîm, yn y modd y rhyddheir arian a'r modd yr adroddir llwyddiant, nid yn a yw stand-ups yn digwydd. Y dynfa gystadleuol yw bod swyddogaethau cyllid, portffolio, a goruchwyliaeth wedi'u hadeiladu i gymeradwyo cwmpas sefydlog yn erbyn cyllideb sefydlog flynyddoedd ymlaen llaw, ac mae gofyn iddynt gyllido canlyniad gyda chwmpas hyblyg yn teimlo fel colli rheolaeth y byddant yn ei gwrthsefyll. Dewch â thystiolaeth: olrheiniwch sut y cyllidwyd menter gyfredol a beth mae'n adrodd arno, a gwiriwch a yw timau'n cael eu mesur ar ganlyniadau a llif a gyflenwyd neu ar bwyntiau stori a chydymffurfiaeth â chwmpas a lofnodwyd amser maith yn ôl. Mewn lleoliadau menter a llywodraeth, cysylltwch hyn yn uniongyrchol â'r plisgyn cyllido a chydymffurfiaeth (pennod 10.6): os yw'r arian wedi'i ymrwymo i lansiad pell, popeth-neu-ddim, ni all y timau fod yn addasol ni waeth pa mor ffyddlon y maent yn perfformio'r defodau, ac mae'r ateb yn perthyn i'r model llywodraethu yn hytrach na'r timau cyflenwi.

## Lens sector

**Cwmni newydd.** Byddwch y gwerthoedd a hepgorwch y ddadl fframwaith. Lansiwch dafell weithredol i ddefnyddwyr go iawn bob wythnos, eisteddwch yn ddigon agos at sylfaenwyr a chwsmeriaid cynnar fel bod adborth yn cyrraedd yn ddyddiol, a chroesawwch newid cyfeiriad y foment y bydd tystiolaeth yn dweud bod y bet gyfredol yn anghywir. Eich adnodd prinnaf yw sylw peirianneg, felly amddiffynnwch ragoriaeth dechnegol (integreiddio parhaus, profion awtomataidd, datblygu seiliedig ar gefn) hyd yn oed o dan bwysau lansio, oherwydd dyna'r ddisgyblaeth sy'n eich cadw'n gallu troi'n rhad yr wythnos nesaf.

**Busnes bach.** Heb hyfforddwr agile a chyllideb dynn, triniwch Agile fel llond llaw o arferion yn hytrach na rhaglen drawsnewid rydych yn ei staffio: cylch wythnosol byr, bwrdd gweladwy gyda therfynau gwaith-ar-y-gweill, ac un gwelliant pendant bob wythnos rydych yn ei orffen mewn gwirionedd. Pwyswch ar Kanban, nad oes angen fawr o seremoni arno ac sy'n addas ar gyfer gwaith wedi'i yrru gan ymyriadau, a mabwysiadwch yr arferion wedi'u mewnosod yn yr offer rydych eisoes yn eu prynu yn hytrach na sefydlu proses drwm. Barnwch yr ymdrech yn ôl a ydych yn lansio meddalwedd ddefnyddiol i gwsmeriaid yn amlach, nid yn ôl pa mor agos rydych yn efelychu Scrum.

**Menter.** Y broblem yw cydgysylltu llawer o dimau heb ailgyflwyno gorchymyn-a-rheolaeth. Ffafriwch ddad-raddio, hynny yw, lleihau dibyniaethau traws-dîm drwy ddyluniad tîm wedi'i halinio â ffrwd a phlatfform cadarn, cyn i chi fabwysiadu fframwaith graddio trwm. Cyllidwch a llywodraethwch o gwmpas canlyniadau (OKRs) a chyflymder yn hytrach na chwmpas blynyddol sefydlog a phwyntiau stori, gwnewch arferion peirianneg arddull XP yn anhrafodadwy ar draws timau, a rheolwch gyflenwi fel portffolio gyda metrigau llif a mesurau canlyniad fel bod grwpiau'n gwella ar dystiolaeth yn hytrach na defod.

**Llywodraeth.** Mae rheolau caffael, tryloywder, ac atebolrwydd cyhoeddus yn siapio pob dewis. Strwythurwch gontractau modiwlaidd, seiliedig ar ganlyniadau gyda chynyddrannau byrrach yn lle un mega-gontract cwmpas sefydlog, gan mai caffael ystwyth yw lle mae ystwythder sector cyhoeddus yn llwyddo neu'n methu amlaf. Adeiladwch archwiliad, hygyrchedd, a diogelwch i mewn i bob cynyddran drwy awtomeiddio fel bod goruchwyliaeth yn cael ei bodloni gan y weithred o adeiladu, cyhoeddwch gynnydd a thystiolaeth o werth cyhoeddus i gyrff goruchwylio, ac ymladdwch dros fynediad gwirioneddol at ddinasyddion (gan gynnwys defnyddwyr technoleg gynorthwyol) bob ailadroddiad, oherwydd dyna'r cyfyngiad sy'n cael ei drafod i ffwrdd amlaf.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd pum person yn hepgor y ddadl seremoni ac yn byw gwerthoedd Agile yn uniongyrchol. Mae'n lansio tafell weithredol i ddefnyddwyr go iawn bob wythnos, yn eistedd yn ddigon agos at sylfaenwyr a chwsmeriaid cynnar fel bod adborth yn cyrraedd yn ddyddiol, ac yn croesawu newid cyfeiriad yr wythnos nesaf pan fydd tystiolaeth yn dweud bod y bet gyfredol yn anghywir. Mae'r tîm yn gwrthod masnachu rhagoriaeth dechnegol am gyflymder, felly mae integreiddio parhaus, profion awtomataidd, a datblygu seiliedig ar gefn yn anhrafodadwy hyd yn oed o dan bwysau lansio, ac mae pob retrospective dydd Gwener yn cynhyrchu un newid pendant y mae'r tîm yn ei orffen mewn gwirionedd cyn yr un nesaf. Nid yw byth yn tracio velocity fel targed, gan fesur yn lle hynny a symudodd gwaith a lansiwyd actifadu ac a yw amseroedd arwain yn crebachu.

**Menter.** Mae trawsnewidiad 60 tîm cwmni telathrebu i ddechrau'n "gwneud Scrum" ond nid yw'n gweld gwelliant. Mae timau'n dal i dderbyn cwmpas blynyddol sefydlog ac yn adrodd ar velocity. Mae ailosod yn ail-ganolbwyntio ar egwyddorion: mae OKRs chwarterol yn disodli mandadau nodweddion, mae timau'n cael eu had-drefnu i leihau dibyniaethau traws-dîm (dad-raddio), a gwneir arferion XP (CI, TDD, datblygu seiliedig ar gefn) yn anhrafodadwy. Mae amseroedd arwain yn disgyn, mae diffygion yn gostwng, ac, yn hollbwysig, mae'r busnes yn dechrau mesur canlyniadau yn hytrach na phwyntiau stori, gan gysylltu cyflenwi Agile â'r biblinell ddarganfod (pennod 11.1).

**Llywodraeth.** Mae tîm gwasanaeth digidol yn ailadeiladu cais budd-daliadau sy'n wynebu dinasyddion gan ddefnyddio Agile y tu mewn i blisgyn llywodraethu hybrid: cynyddrannau pythefnos yn cyflenwi meddalwedd wedi'i phrofi gan ddefnyddwyr, sy'n gweithio; hygyrchedd a diogelwch wedi'u hadeiladu i mewn i bob cynyddran; a chaffael modiwlaidd yn disodli un contract pris-sefydlog. Mae profi defnyddioldeb go iawn gyda dinasyddion (gan gynnwys defnyddwyr technoleg gynorthwyol) pob ailadroddiad yn dal problemau y byddai'r hen broses raeadr wedi'u lansio. Mae'r rhaglen yn cyflenwi gwasanaeth defnyddiadwy'n gynnar ac yn dangos gwerth cyhoeddus mesuradwy i gyrff goruchwylio. Dyma'r patrwm y tu ôl i lwyddiannau modern sector cyhoeddus, a'r gwrthwenwyn i fethiannau mawr-a-sydyn y gorffennol.

## Achos busnes: cymhellion, ROI, a TCO

Daw enillion Agile o **leihad risg a gwireddu gwerth cyflymach**. Drwy gyflenwi meddalwedd sy'n gweithio'n gynnar ac yn aml, mae timau'n troi ansicrwydd yn dystiolaeth yn barhaus, gan ddal methiannau'r-peth-anghywir a fydd-ddim-yn-gweithio tra maent yn rhad, yn hytrach nag mewn lansiad pell, drud. Mae'r ymchwil y tu ôl i gyflenwi modern (canfyddiadau DORA, [DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment), ym mhennod 11.2) yn dangos bod yr arferion y mae Agile yn eu hyrwyddo (bataliau bach, rhyddhadau aml, adborth cyflym, rhagoriaeth dechnegol) yn cydberthyn â chyflenwi gwell *a* sefydlogrwydd *a* pherfformiad sefydliadol. Mae cynyddrannau cynnar hefyd yn dechrau dychwelyd gwerth yn gynt, gan wella amseriad a maint cyfan ROI o gymharu â rhyddhad mawr-a-sydyn nad yw'n dychwelyd dim tan y diwedd.

O ran **[cyfanswm cost berchnogaeth](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**, mae Agile yn gostwng cost newid dros oes system, ar yr amod bod y ddisgyblaeth beirianneg yn real. Ei brif risg yw *agile ffug*: seremoni heb egwyddor na chrefft, sy'n ychwanegu gorbenion cyfarfod tra'n cyflenwi dim o'r budd, a gall fod yn waeth na rhaeadr onest. Felly mae'r achos busnes yn amodol. Mae'r ROI yn uchel pan fyddwch yn mabwysiadu Agile fel meddylfryd-ynghyd-â-pheirianneg, ac yn tua sero (neu'n negyddol) pan fyddwch yn ei fabwysiadu fel defod. Gwnewch yr achos i arweinyddiaeth drwy fframio Agile fel lleihad risg parhaus a mesur canlyniadau, nid fel "mynd yn gyflymach," a thrwy fynnu bod y buddsoddiad yn cynnwys arferion technegol, nid dim ond cyfarfodydd newydd.

## Gwrth-batrymau a pheryglon

- **Agile ffug / cargo-cult:** seremonïau'n cael eu perfformio tra bo penderfyniadau, cyllid, a meddylfryd yn aros yn rhaeadr.
- **Velocity fel cynhyrchiant:** troi amcangyfrif capasiti'n darged, sy'n ei lygru ([Deddf Goodhart](https://en.wikipedia.org/wiki/Goodhart%27s_law)).
- **Dark scrum:** sbrintio heb ragoriaeth dechnegol i mewn i god na ellir ei gynnal, yn llawn diffygion.
- **Retrospectives heb newid:** myfyrio nad yw'n cynhyrchu unrhyw gamau gweithredu wedi'u cwblhau.
- **Cwmpas *a* dyddiad *a* chost sefydlog:** ei alw'n agile tra bo ansawdd yn amsugno'r pwysau yn dawel.
- **Cwsmer absennol:** dim adborth defnyddiwr go iawn, felly mae ailadroddiadau'n optimeiddio'r peth anghywir.
- **Addoli fframwaith:** "dyna mae SAFe/Scrum yn ei ddweud" yn trechu'r egwyddorion a barn y tîm.
- **Graddio cyn dad-raddio:** ychwanegu fframweithiau cydgysylltu trwm yn lle lleihau dibyniaethau.

## Model aeddfedrwydd

- **Lefel 1, Cychwyn.** Cyflenwi rhaeadr neu ad hoc; rhyddhadau mawr-a-sydyn; mae gwaith yn adweithiol a thrwm-ar-gynllun, heb adborth ailadroddol a heb ymdeimlad a rennir o pam y gallai Agile helpu.
- **Lefel 2, Datblygu.** Mae ychydig o dimau'n mabwysiadu seremonïau Agile (stand-ups, sbrintiau, retrospectives), ond mae'r ymarfer yn anghyson ar draws y sefydliad: mae meddylfryd a disgyblaeth beirianneg yn llusgo ar ôl y defodau, trinnir velocity fel allbwn, ac mae cwmpas yn dal yn sefydlog ymlaen llaw.
- **Lefel 3, Safoni.** Mae gwerthoedd ac egwyddorion wir yn llywio gwaith ar draws y sefydliad, wedi'u dogfennu a'u disgwyl gan bob tîm: mae rhagoriaeth dechnegol arddull XP (CI, profi awtomataidd, ailffactora, datblygu seiliedig ar gefn) yn arfer safonol, mae timau'n hunan-drefnu, mae cwsmeriaid yn ymgysylltiedig bob ailadroddiad, ac mae retrospectives yn cynhyrchu newid pendant, wedi'i gwblhau.
- **Lefel 4, Rheoli.** Mesurir a rheolir cyflenwi yn erbyn llinellau sylfaen: mae timau'n tracio amser arwain, amlder defnyddio, cyfradd methiant newid, a chyfradd dianc diffygion (y metrigau llif a sefydlogrwydd arddull DORA), ochr yn ochr â mesurau canlyniad wedi'u clymu i ganlyniadau allweddol, ac yn cymharu pob un yn erbyn llinell sylfaen hysbys. Tracir camau gweithredu retrospective i gwblhad, monitrir signalau cyflymder cynaliadwy fel goramser a llosgi allan, ac ni ddefnyddir velocity byth fel targed cynhyrchiant. Mae penderfyniadau mynd a pheidio â mynd yn gorwedd ar y dystiolaeth hon yn hytrach na barn.
- **Lefel 5, Cydgysylltu.** Mae cyflenwi addasol wedi'i integreiddio â chynllunio busnes a risg ar draws y sefydliad: mae canlyniadau (OKRs) yn gyrru cyllid a chyflymder, mae dyluniad tîm dibyniaeth-isel (dad-raddio) yn lleihau gorbenion cydgysylltu, ac mae llywodraethu hybrid yn bodloni goruchwyliaeth heb arafu cyflenwi. Mae gwelliant parhaus yn ddiwylliannol yn hytrach na seremonïol, ac mae'r sefydliad yn rheolaidd yn ailgwmpasu, yn ailffurfio timau, ac yn ail-gydbwyso ei bortffolio wrth i dystiolaeth a'r darlun risg symud.

## Syniadau ar gyfer trafodaeth

1. Sgoriwch eich tîm yn erbyn deuddeg egwyddor Agile: ble rydych yn ystwyth mewn seremoni ond nid mewn sylwedd?
2. A yw velocity'n cael ei ddefnyddio ar eich tîm fel rhagolwg neu fel targed, a beth mae hynny wedi'i wneud i ymddygiad?
3. Pa arferion technegol XP sydd ar goll, a sut mae eu habsenoldeb yn ymddangos fel diffygion neu newid araf?
4. Cyn mabwysiadu fframwaith graddio, a allech chi leihau dibyniaethau traws-dîm yn lle hynny?
5. Yn eich cyd-destun, beth yn benodol sy'n rhwystro mynediad defnyddiwr go iawn bob ailadroddiad, a sut allech chi ei ddileu?
6. Beth oedd y newid pendant diwethaf a gynhyrchodd retrospective mewn gwirionedd?

## Prif negeseuon

- Mae Agile yn **feddylfryd o werthoedd ac egwyddorion**, nid set o seremonïau; mannau cychwyn yw fframweithiau, nid y nod.
- Cyflenwch **feddalwedd sy'n gweithio'n aml**, croesawwch newid, a grymuswch **dimau hunan-drefnu**.
- **Mae rhagoriaeth dechnegol (arferion XP) yn anhrafodadwy.** Mae ystwythder hebddi'n dod yn ddirywiad cyflym.
- **Graddiwch yn ofalus; ffafriwch ddad-raddio.** Lleihewch ddibyniaethau cyn ychwanegu fframweithiau cydgysylltu.
- Mewn menter/llywodraeth, cyfunwch **gyflenwi addasol â llywodraethu hybrid a chaffael ystwyth**, ac ymladdwch dros fynediad defnyddiwr go iawn.
- Y ROI yw **lleihad risg parhaus a gwerth cynharach**, ond dim ond pan fo Agile yn real, nid yn ddefod. Gweler penodau 1.4, 11.1, 11.2, 10.6, ac 11.3.

## References and further reading

- Kent Beck et al., *Manifesto for Agile Software Development* and its twelve principles (agilemanifesto.org, 2001).
- Ken Schwaber and Jeff Sutherland, *The Scrum Guide*.
- Kent Beck, *Extreme Programming Explained: Embrace Change*.
- David J. Anderson, *Kanban: Successful Evolutionary Change for Your Technology Business*.
- Mike Cohn, *User Stories Applied* and *Succeeding with Agile*.
- Jeff Patton, *User Story Mapping*.
- Stephen Denning, *The Age of Agile*.
- Matthew Skelton and Manuel Pais, *Team Topologies* (team design and descaling).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (evidence for agile/DevOps practices).
- U.S. Digital Service, *Digital Services Playbook*; UK Government, *Government Service Standard*.
