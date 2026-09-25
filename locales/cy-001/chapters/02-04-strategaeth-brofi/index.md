# 2.4 Strategaeth brofi

## Trosolwg a chymhelliant

Mae strategaeth [brofi](https://en.wikipedia.org/wiki/Software_testing) yn set fwriadol o ddewisiadau ynghylch beth i'w brofi, ar ba lefel, pa mor awtomatig, ac i ba hyder, fel y gall eich tîm newid cod yn gyflym heb ei dorri. Profion yw'r hyn sy'n galluogi sefydliad mawr i ddefnyddio'n aml ac yn ddiogel. Maent yn amgodio ymddygiad disgwyliedig, yn dal atchweliadau, ac yn rhoi'r hyder i beirianwyr [ailffactora](https://en.wikipedia.org/wiki/Code_refactoring). Heb strategaeth gydlynol, mae profi'n tueddu i fynd un o ddwy ffordd wael: absennol (datblygu wedi'i yrru gan ofn, araf ei symud) neu wedi chwyddo (miloedd o brofion araf, ansefydlog nad oes neb yn ymddiried ynddynt).

I dîm mawr, mae'r strategaeth yn bwysicach nag unrhyw brawf unigol. Mae cannoedd o beirianwyr sy'n gweithio mewn cod-sail a rennir angen rhwyd ddiogelwch gyflym, ddibynadwy. Heb un, mae pob newid yn beryglus ac mae pob rhyddhad yn troi'n arteithiad â llaw. Mae profion hefyd yn gweithredu fel dogfennaeth weithredadwy o ymddygiad a fwriadwyd, sy'n amhrisiadwy unwaith y bydd yr awduron gwreiddiol wedi symud ymlaen. Y strategaeth sy'n penderfynu a yw eich cyfres brofion yn ased sy'n cyflymu cyflenwi neu'n rwymedigaeth sy'n ei lusgo i lawr.

Mewn cyd-destunau menter a llywodraethol, mae gan brofi bwysau ychwanegol. Gall rheoliadau fynnu cwmpas a thystiolaeth brofi ddogfennedig. Mae systemau diogelwch-hanfodol a rhai sy'n wynebu dinasyddion yn mynnu sicrwydd uchel. Gall profi hygyrchedd a diogelwch fod yn ofynnol yn gyfreithiol. Felly rhaid i'r strategaeth gydbwyso cyflymder, hyder, cost, a chydymffurfiaeth, a rhaid iddi drin cwmpas fel signal, nid targed i'w gamblo.

## Egwyddorion allweddol

- Profwch i ennill yr hyder i newid, nid i daro rhif.
- Ffafriwch brofion cyflym, dibynadwy, ynysig. Mae profion araf neu ansefydlog yn erydu'r ymddiriedaeth sy'n gwneud cyfres yn ddefnyddiol.
- Gwthiwch brofion i'r lefel isaf sy'n rhoi hyder gwirioneddol, a chadwch brofion araf, eang ar gyfer risg integreiddio wirioneddol.
- Mae prawf ansefydlog yn brawf wedi torri. Triniwch ansefydlogrwydd fel diffyg dosbarth cyntaf.
- Mae cwmpas yn signal, nid yn nod. Nid yw cwmpas uchel o god dibwys yn profi fawr ddim.
- Profwch ymddygiad a chontractau, nid manylion gweithredu, fel bod eich profion yn goroesi ailffactora.
- Gwnewch brofi answyddogaethol (hygyrchedd, perfformiad, diogelwch) yn rhan o'r strategaeth, nid yn ôl-ystyriaeth.

## Argymhellion

### Defnyddio pyramid profi fel diofyn, a gwybod ei feirniadaethau

Diofynnwch at lawer o [brofion uned](https://en.wikipedia.org/wiki/Unit_testing) cyflym, llai o [brofion integreiddio](https://en.wikipedia.org/wiki/Integration_testing), a nifer fach o brofion pen-i-ben, gan fod cost a breuoldeb yn codi wrth i gwmpas dyfu. Gwybyddwch y beirniadaethau hefyd: dylai'r siâp ddilyn eich pensaernïaeth, nid dogma. Efallai y bydd angen haen integreiddio fwy ar system trwm ar wasanaethau (y "trophi profi"), a'r nod gwirioneddol yw hyder fesul uned o gost a chyflymder, nid silwét penodol. Beth bynnag a wnewch, osgowch y pyramid gwrthdroëdig o brofion pen-i-ben araf yn bennaf.

### Mabwysiadu TDD, BDD, a datblygiad wedi'i yrru gan fanyleb lle maent yn helpu

Defnyddiwch [ddatblygiad wedi'i yrru gan brofion](https://en.wikipedia.org/wiki/Test-driven_development) (TDD) i yrru dyluniad a gwarantu profadwyedd, yn enwedig ar gyfer rhesymeg gymhleth. Mae'n ddisgyblaeth dylunio yn ogystal â disgyblaeth brofi. Defnyddiwch [ddatblygiad wedi'i yrru gan ymddygiad](https://en.wikipedia.org/wiki/Behavior-driven_development) (BDD) i fynegi profion mewn iaith parth rydych yn ei rhannu â rhanddeiliaid, sy'n werthfawr ar gyfer meini prawf derbyn mewn amgylcheddau rheoledig neu drwm ar ofynion. Mae datblygiad wedi'i yrru gan fanyleb yn mynd un cam ymhellach: mae'n trin manyleb weithredadwy (yr ymddygiad y cytunwyd arno, wedi'i fynegi fel enghreifftiau) fel yr un ffynhonnell wirionedd sy'n llywio'r gweithrediad ac yn ei ddilysu fel ei gilydd. Mae hyn yn disgleirio lle mae'n rhaid i ofynion fod yn olrheiniadwy i dystiolaeth dderbyn, fel mewn rhaglenni llywodraethol a rheoledig. Yn gysylltiedig â'r tri yw **[profi symud-i'r-chwith](https://en.wikipedia.org/wiki/Shift-left_testing)**: symud dilysu mor gynnar â phosibl yn y cylchred oes, ysgrifennu profion ochr yn ochr â neu cyn y cod a'u rhedeg yn barhaus, fel eich bod yn dal diffygion pan ydynt rhataf i'w trwsio, yn hytrach nag mewn camau profi diweddar neu mewn cynhyrchiad. Nid yw'r un o'r rhain yn orfodol ym mhobman. Cymhwyswch nhw lle maent yn ychwanegu eglurder.

### Cyflogi technegau uwch ar gyfer cod gwerth-uchel

Defnyddiwch brofi seiliedig-ar-briodwedd i wirio anfarwynion ar draws llawer o fewnbynnau a gynhyrchwyd, gan ddal achosion ymyl y mae profion seiliedig-ar-enghraifft yn eu colli. Defnyddiwch [brofi ffwslyd](https://en.wikipedia.org/wiki/Fuzzing) ar barswyr a ffiniau mewnbwn heb ymddiriedaeth i ddod o hyd i chwalfeydd a diffygion diogelwch. Defnyddiwch [brofi treiglo](https://en.wikipedia.org/wiki/Mutation_testing) i fesur a yw eich profion yn canfod namau a chwistrellwyd go iawn, signal ansawdd llawer gwell na chwmpas amrwd. Defnyddiwch brofi ciplun yn ddoeth ar gyfer allbwn cyfresol, a gwyliwch am fagl cymeradwyo cipluniau'n ddall eto.

### Rheoli data prawf a defnyddio data synthetig

Gwnewch brofion yn benderfynadwy â data prawf wedi'i reoli, ynysig, ac osgowch ffitiadau newidiadwy a rennir sy'n cyplu profion at ei gilydd. Cynhyrchwch [ddata synthetig](https://en.wikipedia.org/wiki/Synthetic_data) sy'n adlewyrchu nodweddion cynhyrchiad heb ddatgelu gwybodaeth bersonol go iawn, sy'n hanfodol lle mae rheolau preifatrwydd yn gwahardd defnyddio data cynhyrchiad mewn amgylcheddau prawf. Darparwch ffatrïoedd neu adeiladwyr fel y gall pob prawf lunio'n union y data sydd ei angen arno.

### Trin profion ansefydlog fel diffygion

Canfyddwch ansefydlogrwydd yn awtomatig, symudwch brofion ansefydlog allan o'r llwybr rhwystrol, a'u trwsio neu eu dileu erbyn dyddiad cau. Mae cyfres sy'n methu ar hap yn hyfforddi peirianwyr i anwybyddu methiannau, sy'n dinistrio ei gwerth cyfan. Traciwch gyfraddau ansefydlogrwydd a gwnewch ddibynadwyedd yn fetrig ansawdd penodol ar gyfer y gyfres brofion ei hun.

### Defnyddio cwmpas fel signal, ac ychwanegu profi answyddogaethol

Mesurwch gwmpas i ganfod meysydd heb eu profi, ond peidiwch â'i droi'n darged caled sy'n gwahodd gamblo â phrofion di-honiad. Ategwch ef â phrofi treiglo am ddyfnder. Adeiladwch brofi hygyrchedd (gwiriadau awtomataidd ynghyd ag archwiliadau â llaw), profi perfformiad (llinellau sylfaen llwyth ac oedi â chanfod atchweliad), a phrofi diogelwch (sganio dibyniaethau, [dadansoddiad statig](https://en.wikipedia.org/wiki/Static_program_analysis), a phrofi dynamig) i mewn i'r biblinell.

## Cyfaddawdau: manteision ac anfanteision

| Math prawf / arfer | Manteision | Anfanteision |
|---|---|---|
| Profion uned | Cyflym, manwl gywir, rhad, sefydlog | Yn colli bygiau integreiddio a lefel-system |
| Profion integreiddio | Yn dal diffygion rhyngwyneb a gweirio | Arafach; mwy o osod; mwy brau |
| Profion pen-i-ben | Yr hyder uchaf mewn ymddygiad go iawn | Araf, ansefydlog, drud i'w cynnal |
| TDD | Dyluniad gwell, profadwyedd gwarantedig | Cromlin ddysgu; yn teimlo'n araf i ddechrau |
| Profi seiliedig-ar-briodwedd | Yn dod o hyd i achosion ymyl, yn amgodio anfarwynion | Angen meddwl mewn priodweddau; anos ei ysgrifennu |
| Profi treiglo | Mesur gwir o effeithiolrwydd prawf | Drud yn gyfrifiannol; araf i'w redeg |
| Targed cwmpas uchel | Yn dod â chod heb ei brofi i'r wyneb | Gellir ei gamblo; gall annog profion gwerth isel |

Y cyfaddawd canolog yw hyder yn erbyn cyflymder a chost. Mae profion ehangach yn rhoi mwy o hyder ond yn rhedeg yn arafach ac yn torri'n amlach. Mae profion culach yn gyflym ac yn sefydlog ond yn colli diffygion lefel-system. Mae'r cymysgedd cywir yn uchafswmu hyder fesul eiliad o adborth a fesul awr o gynnal a chadw. Ac mae gorbrofi'n fodd methiant gwirioneddol: gall cyfres wedi chwyddo o brofion diangen, araf, brau gostio mwy na'r bygiau y mae'n eu hatal.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Pa brofion answyddogaethol, hygyrchedd, perfformiad, a diogelwch, ddylai rwystro rhyddhad, a pha rai ddylai ond adrodd?** Mae'r bennod hon yn dadlau bod profi answyddogaethol yn perthyn yn y strategaeth yn hytrach nag fel ôl-ystyriaeth, ac yn nodi y gall hygyrchedd fod yn ofynnol yn gyfreithiol a gall profi diogelwch fod yn rhan o dystiolaeth awdurdod-i-weithredu. I system fawr neu un sy'n wynebu dinasyddion, mae porth rhwystrol yn arafu cyflenwi, ond mae diffyg hygyrchedd neu ddiogelwch a ganfyddir mewn cynhyrchiad yn cario cost unioni, enw da, a chyfreithiol sy'n gorbwyso'r prawf. Dewch â'r signalau sy'n ei benderfynu: eich datguddiad rheoleiddiol, a yw'r system yn wynebu dinasyddion, a pha mor aml y mae'r diffygion hyn yn dianc i gynhyrchiad ar hyn o bryd. Gwnewch y gwiriadau sy'n ofynnol yn gyfreithiol yn rhwystrol a gadewch i wiriadau risg-is adrodd gyda thueddiad, fel bod y porth yn adlewyrchu risg go iawn yn hytrach na dogma. Mae'r ateb yn gosod yn uniongyrchol beth all a na all uno.

2. **A ydych chi'n gosod canran cwmpas caled fel porth, ac os felly, beth sy'n atal peirianwyr rhag ei gamblo â phrofion di-honiad?** Mae'r bennod yn gadarn bod cwmpas yn signal, nid yn nod, bod cwmpas uchel o god dibwys yn profi fawr ddim, a bod targed caled yn gwahodd gamblo. Mae un rhif a osodir ar draws sefydliad mawr yn cynhyrchu profion yn gyson sy'n gweithredu cod heb honni dim, sy'n codi'r metrig ac yn gostwng hyder go iawn. Dewch â signal gwell i'r drafodaeth: sgôr profi treiglo ar eich modylau gwerth-uchaf, sy'n mesur a yw profion yn wirioneddol yn canfod namau a chwistrellwyd. Defnyddiwch gwmpas i ganfod meysydd heb eu profi a phrofi treiglo am ddyfnder, a gwrthwynebwch droi'r naill na'r llall yn darged y mae arweinyddiaeth yn ei olrhain ar wahân. Penderfynwch ble mae'r rhif wir yn helpu a ble mae ond yn gwahodd theatr.

3. **Beth yw eich polisi pan fydd y gyfres brofion yn tyfu'n rhy araf i beirianwyr aros amdani?** Y cyfaddawd canolog yn y bennod hon yw hyder yn erbyn cyflymder a chost, ac mae'n enwi gorbrofi fel modd methiant gwirioneddol lle mae cyfres chwyddedig, ddiangen, araf yn costio mwy na'r bygiau y mae'n eu hatal. Ar dîm mawr, mae amser rhedeg cyfres yn dreth a rennir a delir ar bob newid, ac mae cyfres y mae pobl yn dysgu ei hosgoi'n colli ei holl werth. Dewch â'r dystiolaeth: amser wal-glo CI, y profion arafaf, a faint o gwmpas pen-i-ben diangen sy'n dyblygu profion uned rhatach. Gwthiwch brofion i'r lefel isaf sy'n rhoi hyder gwirioneddol, cyflinellu, a dileu profion araf diangen erbyn dyddiad cau. Optimeiddio hyder fesul eiliad o adborth, nid cyfrif prawf amrwd, yw'r nod.

4. **Pan fydd prawf yn dod yn ansefydlog, pwy sy'n berchen arno, pa mor gyflym y mae'n rhaid ei drwsio neu ei ddileu, a beth sy'n gorfodi'r dyddiad cau hwnnw?** Mae'r bennod hon yn trin prawf ansefydlog fel prawf wedi torri, diffyg dosbarth cyntaf, gan fod cyfres sy'n methu ar hap yn hyfforddi tîm mawr i anwybyddu adeiladau coch ac yn dinistrio'n dawel y rhwyd ddiogelwch y mae pawb yn dibynnu arni. Mae'r pwysau cystadleuol yn wirioneddol: mae cwarantinio prawf ansefydlog yn dad-rwystro cyflenwi heddiw ond mae'n peryglu cuddio bwg ysbeidiol gwirioneddol, tra bo rhwystro arno'n stopio cannoedd o beirianwyr dros fethiant a allai fod yn sŵn pur. Dewch â'r dystiolaeth sy'n ei setlo: eich cyfradd ansefydlogrwydd gyfredol, pa mor hir y mae profion yn eistedd wedi'u cwarantinio cyn i unrhyw un eu cyffwrdd, a faint o brofion wedi'u cwarantinio a droeodd allan i guddio diffyg gwirioneddol. Neilltuwch berchennog i bob prawf a gwarantiniwyd, gosodwch ddyddiad cau caled i drwsio neu ddileu, a thraciwch ddibynadwyedd fel metrig penodol ar gyfer y gyfres ei hun. Mewn lleoliadau menter a llywodraethol lle mae adeiladu gwyrdd yn rhan o dystiolaeth rhyddhau, mae pentwr cwarantin heb ei reoli hefyd yn rwymedigaeth archwilio, gan eich bod yn cyflenwi ar signal rydych wedi cytuno'n breifat i beidio ag ymddiried ynddo.

5. **A gaiff eich caniatáu i ddefnyddio data cynhyrchiad mewn amgylcheddau prawf, ac os na, sut y byddwch chi'n cynhyrchu data synthetig ffyddlon ddigon i ddal diffygion gwirioneddol?** Mae'r bennod yn uniongyrchol bod rheolau preifatrwydd yn aml yn gwahardd data personol go iawn mewn profi, a bod yn rhaid i ddata synthetig adlewyrchu nodweddion cynhyrchiad neu mae eich profion yn rhoi hyder ffug. I sefydliad mawr mae'r tyndra rhwng ffyddlondeb a chydymffurfiaeth: mae data cynhyrchiad yn dal yr achosion ymyl anniben y mae data synthetig yn eu colli, ond mae pob copi ohono'n lluosi eich datguddiad a'ch rhwymedigaethau. Dewch â'r manylion: pa setiau data sy'n cario data personol neu reoledig, beth mae eich rheolau preifatrwydd a phreswyliad data'n eu mynnu go iawn, a pha mor dda mae eich ffitiadau cyfredol yn atgynhyrchu'r dosraniadau a'r achosion ymyl a welwyd mewn cynhyrchiad. Safonwch ffatrïoedd neu adeiladwyr fel bod pob prawf yn llunio'n union y data sydd ei angen arno, a buddsoddwch mewn cynhyrchu synthetig sy'n cyfateb i ddosraniadau demograffig a chyfaint go iawn. Mewn rhaglenni llywodraethol a rheoledig, nid llwybr byr yw defnyddio data dinasyddion mewn amgylchedd prawf, mae'n doriad adroddadwy, felly rhaid setlo'r strategaeth ddata cyn i'r amgylchedd cyntaf gael ei sefydlu.

6. **Ble y dylid disgwyl TDD, BDD, neu ddatblygiad wedi'i yrru gan fanyleb yn hytrach na bod yn ddewisol, a phwy sy'n penderfynu?** Mae'r bennod hon yn cyflwyno'r rhain fel disgyblaethau i'w cymhwyso lle maent yn ychwanegu eglurder, nid mandadau ar gyfer pob llinell o god, ac eto mae tîm mawr yn elwa o ddiofyn a rennir fel nad yw arfer yn dryllio fesul tîm. Y cyfaddawd yw rhwng buddion dylunio ac olrheiniadwyedd (manylebau gweithredadwy y gall arbenigwyr polisi eu hadolygu, profion sy'n goroesi ailffactora) a'r gromlin ddysgu wirioneddol a'r arafwch ymlaen llaw sy'n gwneud i fandad cyffredinol wrthgynhyrchu. Dewch â thystiolaeth i'w gwmpasu: pa fodylau sy'n cario rhesymeg gymhleth neu gyfraddau methiant-newid uchel, lle mae'n rhaid i feini prawf derbyn fod yn olrheiniadwy i ofynion, a sut mae timau sydd eisoes yn ymarfer y rhain yn adrodd ar gyflymder a chyfraddau diffyg. Cadwch y disgwyliad ar gyfer rhesymeg gymhleth a meysydd trwm ar ofynion, a gadewch i god symlach ddewis drosto'i hun. Mewn rhaglenni rheoledig a llywodraethol lle mae'n rhaid i feddalwedd fod yn olrheiniadwy i'r gyfraith y mae'n ei gweithredu, mae datblygiad wedi'i yrru gan fanyleb â thystiolaeth dderbyn weithredadwy yn llai o ddewis ac yn fwy o lwybr at eich awdurdod-i-weithredu, felly enwch yn benodol lle mae'n ofynnol.

## Lens sector

**Cwmni newydd.** Ni all tîm bach staffio QA, felly gwnewch i'r gyfres ennill ei chadw: profion uned cyflym ar bob ymrwymiad ynghyd â chwpl o brofion pen-i-ben dros yr un llwybr sy'n talu'r biliau, a dim byd na fyddwch yn ei gynnal. Hepgorwch dargedau cwmpas a phrofwch y rhesymeg rydych fwyaf ofn ei thorri, fel y gallwch gyflenwi sawl gwaith y dydd heb basiad atchweliad â llaw. Trwsiwch brawf ansefydlog yr un diwrnod, gan fod cyfres y mae'r tîm yn dysgu ei hanwybyddu'n waeth na dim cyfres o gwbl ar y cam hwn.

**Busnes bach.** Heb beiriannydd prawf pwrpasol a chyllideb dynn, pwyswch ar y profi sydd wedi'i adeiladu i mewn i'r fframweithiau a'r offer rydych eisoes yn eu rhedeg yn hytrach na harnais pwrpasol na allwch ei gynnal. Blaenoriaethwch y llond llaw o wiriadau sy'n diogelu refeniw ac ymddiriedaeth cwsmeriaid, a defnyddiwch CI wedi'i gynnal fel nad ydych yn cynnal seilwaith adeiladu eich hun. Ffafriwch brynu sganio hygyrchedd a diogelwch fel gwasanaeth dros ei adeiladu, gan y gall un diffyg a fethwyd gostio mwy na blwyddyn o'r teclyn.

**Menter.** Ar draws llawer o dimau, problem y strategaeth yw cysondeb: diofyn pyramid a rennir, cwarantin prawf-ansefydlog awtomatig, a phyrth answyddogaethol sy'n golygu'r un peth ym mhobman, fel bod adeiladu gwyrdd yn ddibynadwy ni waeth pwy a'i cynhyrchodd. Cyllidebwch amser rhedeg cyfres fel treth a rennir a chyflinellwch yn ymosodol, gan fod amser wal-glo CI yn cael ei dalu ar bob newid gan bob peiriannydd. Rheolwch sgorau cwmpas a threiglo fel signalau portffolio â pherchnogaeth glir, nid rhifau y mae arweinyddiaeth yn eu holrhain ar wahân.

**Llywodraeth.** Mae caffael a goruchwyliaeth yn gwneud profi'n dystiolaeth, nid hylendid peirianneg yn unig. Mynegwch reolau cymhwysedd a pholisi fel manylebau gweithredadwy a adolygir gan arbenigwyr parth, fel y gallwch olrhain y feddalwedd i'r gyfraith y mae'n ei gweithredu, a gwnewch brofi hygyrchedd a diogelwch yn rhwystrol gan eu bod yn ofynnol yn gyfreithiol ac yn rhan o dystiolaeth awdurdod-i-weithredu. Defnyddiwch ddata synthetig a gynhyrchwyd i gyfateb i ddosraniadau go iawn, gan fod data dinasyddion mewn amgylchedd prawf yn doriad adroddadwy, a chadwch yr arteffactau prawf yn archwiliadwy fel y gall adolygydd allanol gadarnhau'n union beth a ddilyswyd.

## Enghreifftiau

**Cwmni newydd.** Ni all cwmni newydd pum person fforddio tîm QA, felly mae'n pwyso ar gyfres brofion uned gyflym sy'n rhedeg ar bob ymrwymiad ynghyd â chwpl o brofion pen-i-ben sy'n cwmpasu'r llwybr cofrestru-i-dalu sy'n talu'r biliau. Mae'r sylfaenwyr yn hepgor cwmpas cynhwysfawr ac yn lle hynny'n profi'r rhesymeg y maent fwyaf ofn ei thorri, sy'n eu galluogi i gyflenwi sawl gwaith y dydd heb basiad atchweliad â llaw. Pan fydd prawf ansefydlog yn dechrau methu ar hap, maent yn ei drwsio'r un diwrnod, gan fod cyfres y mae'r tîm yn dysgu ei hanwybyddu'n waeth na dim cyfres ar y cam lle mae ymddiriedaeth yn bopeth.

**Menter.** Mae platfform e-fasnach mawr yn cynnal miloedd o brofion uned cyflym sy'n rhedeg ar bob ymrwymiad mewn munudau, set ffocysedig o brofion integreiddio o amgylch ffiniau taliad ac eiddo, a chyfres fach o brofion pen-i-ben ar gyfer y teithiau talu hanfodol. Caiff profion pen-i-ben ansefydlog eu cwarantinio'n awtomatig a'u neilltuo i'w trwsio. Gan fod peirianwyr yn ymddiried yn y gyfres, maent yn defnyddio sawl gwaith y dydd, yn hyderus bod adeiladu coch yn golygu problem go iawn.

**Llywodraeth.** Mae system fudd-daliadau genedlaethol sy'n gweithredu o dan oruchwyliaeth reoleiddiol yn defnyddio BDD i fynegi rheolau cymhwysedd fel manylebau gweithredadwy a adolygir gan arbenigwyr polisi, sy'n rhoi tystiolaeth olrheiniadwy bod y feddalwedd yn gweithredu'r gyfraith. Mae'n defnyddio data synthetig a gynhyrchwyd i gyfateb i ddosraniadau demograffig go iawn, gan fod rheolau preifatrwydd yn gwahardd data dinasyddion mewn amgylcheddau prawf. Mae profi hygyrchedd yn orfodol ac yn rhwystro rhyddhad, gan fod yn rhaid i'r gwasanaeth fod yn ddefnyddiadwy gan bob dinesydd. Ac mae profi diogelwch yn rhan o dystiolaeth awdurdod-i-weithredu (ATO), y cymeradwyaeth ffurfiol i redeg y system mewn cynhyrchiad.

## Achos busnes: cymhellion, ROI, a TCO

Yr elw ar brofi yw'r gallu i newid meddalwedd yn gyflym ac yn ddiogel, sef sylfaen cyflymder cyflenwi cynaliadwy. Mae cyfres awtomataidd ddibynadwy'n disodli [profi atchweliad](https://en.wikipedia.org/wiki/Regression_testing) â llaw, araf, drud ac yn dal diffygion pan ydynt rataf i'w trwsio, cyn rhyddhau yn hytrach na mewn cynhyrchiad. Mewn system reoledig neu sy'n wynebu dinasyddion, mae cost diffyg cynhyrchiad (unioni, enw da, a datguddiad cyfreithiol posibl) yn gorbwyso cost y profion a fyddai wedi'i ddal.

Mae cost mabwysiadu'n wirioneddol: rydych yn ysgrifennu ac yn cynnal profion, ac yn adeiladu seilwaith [integreiddio parhaus](https://en.wikipedia.org/wiki/Continuous_integration) (CI). Ond mae cost peidio â phrofi'n uwch ac mae'n cyfansymio: datblygu wedi'i yrru gan ofn sy'n arafu i gropian, atchweliadau aml, a phrosesau rhyddhau â llaw na allant raddio. Mae cost i orbrofi hefyd, felly'r ddadl yw dros strategaeth wedi'i dylunio'n dda, nid yr uchafswm o brofion. I wneud yr achos i arweinyddiaeth, cysylltwch y gyfres ag amlder defnyddio, cyfradd methiant-newid, ac amser cymedrig i adfer, a meintiolwch yr ymdrech brofi â llaw y mae'n ei disodli a'r digwyddiadau cynhyrchiad y mae'n eu hatal.

## Gwrth-batrymau a pheryglon

- **Profi côn-hufen-iâ:** profion pen-i-ben araf yn bennaf dros sylfaen uned denau; araf, ansefydlog, drud.
- **Cwmpas fel targed:** hela canran â phrofion di-honiad neu ddibwys nad ydynt yn profi dim.
- **Profi manylion gweithredu:** profion wedi'u cyplu i fewnolion sy'n torri ar bob ailffactora, gan atal newid.
- **Ansefydlogrwydd a oddefir:** methiannau ar hap sy'n hyfforddi'r tîm i anwybyddu adeiladau coch.
- **Data prawf newidiadwy a rennir:** profion sy'n ymyrryd â'i gilydd ac yn methu'n annisgwyladwy.
- **Defnyddio data cynhyrchiad mewn profi:** toriad preifatrwydd a chydymffurfiaeth yn aros i ddigwydd.
- **Profi answyddogaethol wedi'i hepgor:** hygyrchedd, perfformiad, a diogelwch a ddarganfyddir mewn cynhyrchiad yn unig.
- **Y gyfres heb ymddiriedaeth:** mor annibynadwy fel bod peirianwyr yn rheolaidd yn ei hailredeg neu'n ei hosgoi, gan wadu ei diben.

## Model aeddfedrwydd

- **Lefel 1, Cychwyn:** Mae profi â llaw ac yn adweithiol; mae cwmpas awtomataidd yn isafswm; mae atchweliadau'n aml ac yn cael eu dal yn hwyr, yn aml gan ddefnyddwyr yn hytrach na'r gyfres.
- **Lefel 2, Datblygu:** Mae profion uned awtomataidd a rhai profion integreiddio'n bodoli, ond mae'r gyfres yn araf neu'n ansefydlog, mae ymddiriedaeth yn isel, ac mae arfer yn amrywio'n fawr o un tîm i'r llall.
- **Lefel 3, Safoni:** Mae cyfres gytbwys, gyflym, ddibynadwy'n rhwystro pob newid; caiff diofyn pyramid dogfennedig, polisi prawf-ansefydlog, a phrofi answyddogaethol (hygyrchedd, perfformiad, diogelwch) eu gorfodi'n gyson ar draws timau.
- **Lefel 4, Rheoli:** Caiff iechyd y gyfres ei fesur a'i reoli yn erbyn llinellau sylfaen; caiff cyfradd ansefydlogrwydd, amser wal-glo CI, sgôr treiglo ar fodylau gwerth-uchel, a chyfradd diffygion a ddihangodd eu tracio a'u hadolygu; mae cwmpas yn un signal ymhlith sawl un, ac mae pyrth yn sbarduno ar dystiolaeth yn hytrach na barn.
- **Lefel 5, Cerdorfa:** Mae technegau uwch (seiliedig-ar-briodwedd, treiglo, ffwslyd) yn targedu cod gwerth-uchel; mae profi wedi'i integreiddio â metrigau cyflenwi fel amlder defnyddio, cyfradd methiant-newid, ac amser cymedrig i adfer; mae'r sefydliad yn ailffurfio'r gyfres yn barhaus i'w bensaernïaeth a'i risg, gan ymddeol profion diangen a buddsoddi lle mae tystiolaeth yn dangos bod diffygion yn dal i ddianc.

## Syniadau ar gyfer trafod

- Pa siâp y mae eich dosraniad prawf yn ei gymryd go iawn, ac a yw'n cyfateb i'ch pensaernïaeth a'ch risg?
- Sut rydych chi'n penderfynu pryd mae darn o god yn haeddu profi seiliedig-ar-briodwedd neu dreiglo yn erbyn profion enghreifftiol?
- Beth yw eich polisi ar gyfer profion ansefydlog, ac a gaiff ei orfodi go iawn?
- Sut rydych chi'n cynhyrchu data synthetig realistig heb ollwng gwybodaeth sensitif?
- Ble mae cwmpas wir yn eich helpu, a ble mae wedi cael ei gamblo?
- Sut y dylid adolygu profion a gynhyrchwyd gan AI fel eu bod yn ychwanegu hyder yn hytrach na sŵn?

## Prif negeseuon

- Profwch i ennill hyder i newid; optimeiddiwch hyder fesul uned o gyflymder a chost.
- Defnyddiwch y pyramid fel diofyn ond siapiwch brofi i'ch pensaernïaeth.
- Triniwch brofion ansefydlog fel diffygion a chwmpas fel signal, nid targed.
- Cymhwyswch dechnegau uwch lle mae'r gwerth yn cyfiawnhau'r gost.
- Cynhwyswch brofi hygyrchedd, perfformiad, a diogelwch yn y strategaeth, a defnyddiwch ddata synthetig i ddiogelu preifatrwydd.

## Cyfeiriadau a darllen pellach

- Kent Beck, *Test-Driven Development: By Example*
- Lisa Crispin a Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*
- Michael Feathers, *Working Effectively with Legacy Code*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Martin Fowler, erthyglau ar y Pyramid Profi a phatrymau cysylltiedig â phrofi
