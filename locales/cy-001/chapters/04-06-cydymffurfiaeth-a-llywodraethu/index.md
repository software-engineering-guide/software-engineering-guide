# 4.6 Cydymffurfiaeth a llywodraethu

## Trosolwg a chymhelliant

Cydymffurfiaeth yw'r ddisgyblaeth o brofi bod eich sefydliad yn bodloni ei rwymedigaethau cyfreithiol, contractiol, a moesegol, i archwilwyr, rheoleiddwyr, cwsmeriaid, a dinasyddion. Llywodraethu yw strwythur y polisïau, rolau, a rheolaethau sy'n gwneud cydymffurfiaeth yn briodwedd ailadroddadwy o'r sefydliad yn hytrach na brwydr flynyddol arwrol. I fentrau mawr, ac yn enwedig i lywodraeth, nid gorbenion dewisol yw cydymffurfiaeth. Yn aml, dyma'r drwydded i weithredu. Heb y tystysgrifau a'r awdurdodiadau cywir, ni allwch werthu i ddiwydiannau rheoleiddiedig, ni allwch ennill contractau llywodraeth, ac ni allwch brosesu rhai mathau o ddata yn gyfreithlon.

Mae'r dirwedd gydymffurfiaeth yn eang ac yn haenog. Mae mentrau'n llywio cyfreithiau diogelu data (GDPR, CCPA), rheolau sector (HIPAA ar gyfer iechyd, PCI-DSS ar gyfer cardiau talu, SOX ar gyfer adrodd ariannol), a thystysgrifau gwirfoddol-ond-disgwyliedig (ISO 27001, SOC 2). Mae llywodraeth a'i chontractwyr yn wynebu bydysawd ychwanegol: awdurdodiadau FedRAMP a FISMA, catalogau rheolaeth NIST 800-53 a 800-171, CMMC ar gyfer cadwyn gyflenwi amddiffyn, dosbarthiadau lefel effaith, mandadau hygyrchedd (Section 508, ADA, WCAG, EN 301 549), a rhwymedigaethau cofnodion gan gynnwys FOIA. Nid yw rheoli hyn i gyd â llaw yn graddio. Yr ateb modern yw cydymffurfiaeth barhaus, lle mae rheolaethau'n cael eu hawtomeiddio a thystiolaeth yn cael ei chynhyrchu fel sgil-gynnyrch o weithrediadau arferol.

Mae'r bennod hon yn ymdrin â'r prif fframweithiau, y cyfundrefnau penodol i lywodraeth sy'n cario pwysau trwm, hygyrchedd fel mandad cyfreithiol, a'r symudiad o archwiliadau cyfnodol i gydymffurfiaeth barhaus, wedi'i gyrru gan dystiolaeth, a llywodraethu cadarn.

## Egwyddorion allweddol

- **Sgil-gynnyrch peirianneg dda yw cydymffurfiaeth.** Mae systemau sy'n cael eu rhedeg yn dda gyda rheolaethau cryf yn cynhyrchu tystiolaeth yn naturiol; nid yw cydymffurfiaeth-fel-theatr yn gwneud hynny.
- **Mapiwch reolaethau unwaith, bodlonwch lawer o fframweithiau.** Yn aml mae un rheolaeth yn mynd i'r afael â gofynion ar draws sawl safon; rheolwch set reolaeth unedig.
- **Parhaus dros gyfnodol.** Awtomeiddiwch gasglu tystiolaeth fel bod cydymffurfiaeth bob amser ymlaen, nid brwydr cyn archwiliad.
- **Mae llywodraethu'n diffinio atebolrwydd.** Mae perchnogaeth glir o bolisïau, rheolaethau, a risgiau'n gwneud cydymffurfiaeth yn gynaliadwy.
- **Gofyniad yw hygyrchedd, nid rhinwedd ddewisol.** I lywodraeth, ac yn gynyddol i fentrau, mae'n orfodol yn gyfreithiol.
- **Rhwymedigaethau yw cofnodion.** Mae cadw, dosbarthu, a datgelu cofnodion yn cario grym cyfreithiol, yn enwedig mewn llywodraeth.
- **Cynlluniwch ar gyfer yr archwiliwr.** Mae systemau sy'n cynhyrchu tystiolaeth glir, na ellir ei newid, yn rhatach i'w harchwilio ac yn haws ymddiried ynddynt.

## Argymhellion

### Gwybod pa fframweithiau sy'n berthnasol a mapio rheolaethau unwaith

Dechreuwch drwy nodi pa gyfundrefnau sy'n rhwymo eich sefydliad, yna adeiladwch fframwaith rheolaeth unedig sy'n mapio pob rheolaeth i bob gofyniad y mae'n ei fodloni.

- **GDPR / CCPA:** hawliau diogelu data a phreifatrwydd o dan [Reoliad Diogelu Data Cyffredinol](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) yr UE a [Deddf Preifatrwydd Defnyddwyr Califfornia](https://en.wikipedia.org/wiki/California_Consumer_Privacy_Act) (gweler pennod 4.5).
- **HIPAA:** y [Ddeddf Cludadwyedd ac Atebolrwydd Yswiriant Iechyd](https://en.wikipedia.org/wiki/Health_Insurance_Portability_and_Accountability_Act), sy'n mynnu mesurau diogelu ar gyfer gwybodaeth iechyd warchodedig yn sector gofal iechyd yr UD.
- **PCI-DSS:** y [Safon Diogelwch Data Diwydiant Cardiau Talu](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard), sy'n mynnu rheolaethau diogelwch ar gyfer trin data cardiau talu; mae lleihau cwmpas (tocynneiddio) yn gostwng cost yn sylweddol.
- **SOX:** y [Ddeddf Sarbanes-Oxley](https://en.wikipedia.org/wiki/Sarbanes%E2%80%93Oxley_Act), sy'n mynnu rheolaethau dros adrodd ariannol, gan bwysleisio rheoli newid, rheoli mynediad, a llwybrau archwilio.
- **[ISO 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001):** system rheoli diogelwch gwybodaeth (ISMS) gyda rheolaethau y gellir eu tystysgrifu, wedi'u seilio ar risg.
- **SOC 2:** ardystiad Rheolaethau System a Sefydliad o reolaethau ynghylch diogelwch, argaeledd, cyfrinachedd, integredd prosesu, a phreifatrwydd, y mae prynwyr mentrau'n ei ddisgwyl yn eang.
- **[Fframwaith Seiberddiogelwch NIST](https://en.wikipedia.org/wiki/NIST_Cybersecurity_Framework) (CSF):** fframwaith hyblyg, gwirfoddol gan y Sefydliad Cenedlaethol Safonau a Thechnoleg (NIST) sy'n trefnu diogelwch yn Adnabod, Amddiffyn, Canfod, Ymateb, Adfer (a Llywodraethu).

Cynhaliwch un llyfrgell reolaeth sengl wedi'i chroesfapio i'r fframweithiau hyn fel bod gweithredu rheolaeth (dyweder, adolygiad mynediad) yn cynhyrchu tystiolaeth ar gyfer SOC 2, ISO 27001, ac eraill ar unwaith. Y groesfapio hon yw'r symudiad unigol â'r dylanwad uchaf mewn cydymffurfiaeth mentrau.

### Bodloni cyfundrefnau penodol i lywodraeth yn drylwyr

Mae gwaith llywodraeth yn gosod gofynion penodol, na ellir eu trafod.

- **[FISMA](https://en.wikipedia.org/wiki/Federal_Information_Security_Management_Act_of_2002)** (y Ddeddf Rheoli Diogelwch Gwybodaeth Ffederal) yn llywodraethu diogelwch gwybodaeth ffederal; mae **[NIST SP 800-53](https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53)** yn darparu'r catalog rheolaeth ar gyfer systemau ffederal, wedi'i ddewis yn ôl categoreiddiad system (effaith isel/cymedrol/uchel).
- **[FedRAMP](https://en.wikipedia.org/wiki/FedRAMP)** (y Rhaglen Reoli Risg ac Awdurdodi Ffederal) yn safoni awdurdodiad gwasanaethau cwmwl ar gyfer defnydd ffederal, gyda llinellau sylfaen wedi'u clymu i lefelau effaith ac Awdurdodiad i Weithredu (ATO) fel y nod.
- Mae **NIST SP 800-171** yn diogelu Gwybodaeth Ddiddosbarth Reoledig (CUI) mewn systemau anffederal, gan rwymo contractwyr.
- Mae **CMMC** (Ardystiad Model Aeddfedrwydd Seiberddiogelwch) yn gwirio bod contractwyr sylfaen-ddiwydiannol amddiffyn yn gweithredu'r rheolaethau gofynnol, ar lefelau haenog.
- Mae **Lefelau Effaith (IL)** yn dosbarthu sensitifrwydd data (er enghraifft haenau IL2 i IL6 Adran Amddiffyn (DoD)) ac yn pennu'r amgylchedd a'r rheolaethau sy'n ofynnol.

Ymdriniwch â'r rhain gyda Chynllun Diogelwch System (SSP) wedi'i ddogfennu, Cynllun Gweithredu a Cherrig Milltir (POA&M) ar gyfer bylchau, a monitro parhaus i gynnal awdurdodiad yn hytrach na thrin yr ATO fel digwyddiad unwaith yn unig.

### Trin hygyrchedd fel mandad cyfreithiol

Mae hygyrchedd yn ddyletswydd foesegol ac, mewn llawer o awdurdodaethau, yn gyfraith.

- Mae **[Section 508](https://en.wikipedia.org/wiki/Section_508_Amendment_to_the_Rehabilitation_Act_of_1973)** yn mynnu bod systemau ffederal yr UD (a'u contractwyr yn aml) yn hygyrch; mae rhwymedigaethau **[ADA](https://en.wikipedia.org/wiki/Americans_with_Disabilities_Act_of_1990)** (Deddf Americanwyr ag Anableddau) yn cyrraedd gwasanaethau digidol masnachol yn gynyddol; **EN 301 549** yw'r safon Ewropeaidd ar gyfer caffael sector cyhoeddus.
- Y **[Canllawiau Hygyrchedd Cynnwys Gwe](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG)**, fel arfer ar lefel AA, yw'r meincnod technegol y cyfeirir ato gan y mandadau hyn.
- Adeiladwch hygyrchedd i mewn i ddylunio a phrofi, nid fel cam adfer: marcio semantig, llywio bysellfwrdd, cyferbyniad digonol, cefnogaeth darllenydd sgrin, a chapsiynau.
- Profwch gyda theclynnau awtomataidd a chyda defnyddwyr technoleg gynorthwyol go iawn, a dogfennwch gydymffurfiaeth (er enghraifft drwy adroddiad cydymffurfiaeth hygyrchedd, a elwir hefyd yn Voluntary Product Accessibility Template, neu VPAT).

### Adeiladu parodrwydd archwilio a chydymffurfiaeth barhaus

Symudwch o frwydr gyfnodol i osgo bob amser yn barod.

- **Awtomeiddiwch gasglu tystiolaeth:** tynnwch dystiolaeth rheolaeth (adolygiadau mynediad, canlyniadau sganio, cymeradwyaethau newid, copïau wrth gefn) yn awtomatig ac yn barhaus yn hytrach na'i chydosod â llaw cyn pob archwiliad.
- Defnyddiwch gydymffurfiaeth-fel-cod a pheiriannau polisi i orfodi a gwirio rheolaethau adeg defnyddio, gan gynhyrchu tystiolaeth fel sgil-effaith.
- Cynhaliwch ddangosfwrdd rheolaeth byw sy'n dangos statws a bylchau, fel bod y sefydliad yn barod i'w archwilio ar unrhyw adeg.
- Rheolwch eithriadau a derbyniadau risg yn benodol, gyda pherchnogion a dyddiadau dod i ben, yn hytrach na gadael i fylchau lingeru'n dawel.

### Llywodraethu rheoli cofnodion a datgeliad

Mae cofnodion yn cario rhwymedigaethau cyfreithiol penodol, yn enwedig mewn llywodraeth.

- Sefydlwch bolisi **rheoli cofnodion**: beth sy'n gyfystyr â chofnod, am ba mor hir y cedwir pob dosbarth, a sut y'i dosberthir, wedi'i alinio â threfnau statudol.
- Sicrhewch fod cofnodion yn ddilys, yn gyflawn, ac yn amlwg os ymyrrir â nhw, gyda llwybrau archwilio.
- I lywodraeth, paratowch ar gyfer **[FOIA](https://en.wikipedia.org/wiki/Freedom_of_Information_Act_(United_States))** (y Ddeddf Rhyddid Gwybodaeth, a chyfreithiau tryloywder cyfatebol): y gallu i leoli, adolygu, golygu allan, a rhyddhau cofnodion o fewn amserlenni cyfreithiol.
- Cysonwch rwymedigaethau cadw cofnodion â hawliau dileu preifatrwydd, a all wrthdaro; dogfennwch sut mae'r sefydliad yn datrys y tyndra.

## Cyfaddawdau: manteision ac anfanteision

| Penderfyniad | Manteision | Anfanteision |
|---|---|---|
| Mynd ar drywydd llawer o dystysgrifau | Yn agor marchnadoedd, yn adeiladu ymddiriedaeth | Costus, baich archwilio parhaus |
| Fframwaith rheolaeth unedig | Effeithlon, mapio unwaith yn bodloni llawer | Ymdrech ymlaen llaw i adeiladu'r groesfapio |
| Awtomeiddio cydymffurfiaeth barhaus | Bob amser yn barod i'w archwilio, cost is fesul archwiliad | Buddsoddiad offer, ymdrech beirianneg |
| Archwiliadau pwynt-mewn-amser yn unig | Cost uniongyrchol is | Brwydr, llithriant rhwng archwiliadau, risg uwch |
| Tîm cydymffurfiaeth mewnol | Cyd-destun dwfn, rheolaeth | Drud, anodd staffio pob arbenigedd |
| Llwyfan GRC / ymgynghorwyr | Arbenigedd, offer, cyflymder | Cost, dibyniaeth ar werthwr |
| Mynd ar drywydd FedRAMP/ATO | Mynediad i'r farchnad ffederal | Hir, drud, dogfennaeth drwm |

Y cyfaddawd trosfwaol yw cost ac ymdrech yn erbyn mynediad marchnad a lleihau risg. Mae tystysgrifau ac awdurdodiadau'n ddrud ac yn araf, ond i lawer o sefydliadau dyma'r tocyn mynediad i farchnadoedd cyfan: dim FedRAMP, dim busnes cwmwl ffederal; dim SOC 2, dim bargeinion mentrau. Mae'r llwybr effeithlon yn buddsoddi unwaith mewn fframwaith rheolaeth unedig, awtomataidd, fel bod cost ymylol pob tystysgrif ychwanegol yn aros yn isel. Mae cydymffurfiaeth barhaus yn costio mwy ymlaen llaw na brwydr archwilio funud olaf, ond mae'n rhatach o lawer ac yn llai peryglus dros amser. Mae'n trosi cydymffurfiaeth o argyfwng sy'n ailddigwydd yn briodwedd cyflwr sefydlog.

## Cwestiynau i'w trafod gyda'ch tîm

1. **Pa reolaethau yn eich llyfrgell sy'n mapio i'r rhan fwyaf o fframweithiau, ac a ydych yn eu tystiolaethu'n awtomatig?** Y symudiad unigol â'r dylanwad uchaf mewn cydymffurfiaeth mentrau yw set reolaeth unedig wedi'i chroesfapio fel bod gweithredu un rheolaeth (dyweder, adolygiadau mynediad) yn cynhyrchu tystiolaeth ar gyfer SOC 2, ISO 27001, HIPAA, a mwy ar unwaith. Penderfynwch pa reolaethau sy'n cario'r pwysau amlfframwaith hwn a blaenoriaethwch awtomeiddio eu tystiolaeth, oherwydd mae'r rheiny'n talu ar eu canfed ar draws pob archwiliad. Mae tystiolaeth barhaus, awtomataidd yn troi pob archwiliad o ymarfer tân drud yn wiriad arferol yn erbyn stôr byw, ac mae'n torri cost ymylol ychwanegu'r dystysgrif nesaf. Dewch â'ch rhestr rheolaeth bresennol a nodwch pa rai sy'n dal i ddibynnu ar sgrinluniau â llaw a gasglwyd cyn pob archwiliad, oherwydd dyna eich risg llithriant a brwydro. Os ydych yn rheoli pob fframwaith yn ei seilo ei hun, rydych yn dyblygu ymdrech y byddai un groesfapio sengl yn ei dileu.

2. **Os mai ATO FedRAMP neu awdurdodiad tebyg yw eich nod, a allwch ei gynnal, nid dim ond ei gyflawni?** Awdurdodiadau llywodraeth yw'r porth i'r contract, ac mae trin yr ATO fel un-a-wedi-gorffen yn fethiant clasurol, oherwydd monitro parhaus sy'n cadw'r porth ar agor. Penderfynwch a oes gennych y ddisgyblaeth i gynnal Cynllun Diogelwch System byw, gweithio Cynllun Gweithredu a Cherrig Milltir ar gyfer bylchau, a dewis rheolaethau NIST SP 800-53 yn ôl categoreiddiad effaith eich system. Mae'r cyfundrefnau hyn yn drylwyr ac ni ellir eu trafod, ac mae'r baich dogfennu a monitro'n sylweddol ac yn barhaus, nid yn wthiad diwrnod lansio. Dewch â'r bibell sydd angen yr awdurdodiad a'i phwyso yn erbyn cost go iawn ei gynnal, fel bod y buddsoddiad yn benderfyniad busnes bwriadol. Os yw Gwybodaeth Ddiddosbarth Reoledig o fewn cwmpas, cadarnhewch eich bod hefyd yn bodloni NIST SP 800-171 a'r lefel CMMC berthnasol, oherwydd gall colli'r naill neu'r llall eich datgymhwyso.

3. **A yw cydymffurfiaeth hygyrchedd yn eich diffiniad o 'wedi'i orffen', neu'n gam adfer sy'n aros i fethu archwiliad?** Mandad cyfreithiol yw hygyrchedd, nid rhinwedd ddewisol: mae Section 508 yn rhwymo systemau ffederal yr UD a'u contractwyr yn aml, mae rhwymedigaethau ADA yn cyrraedd gwasanaethau digidol masnachol yn gynyddol, ac mae EN 301 549 yn llywodraethu caffael sector cyhoeddus Ewropeaidd. Adeiladwch WCAG AA i mewn i ddylunio a phrofi (marcio semantig, llywio bysellfwrdd, cyferbyniad digonol, cefnogaeth darllenydd sgrin, capsiynau) yn hytrach na'i osod arno'n hwyr, sy'n cynhyrchu canlyniadau gwael, anghydymffurfiol a risg gyfreithiol. Penderfynwch a fyddwch yn profi gyda theclynnau awtomataidd ynghyd â defnyddwyr technoleg gynorthwyol go iawn, ac a ydych yn dogfennu cydymffurfiaeth mewn VPAT ar gyfer prynwyr sy'n ei fynnu. Dewch â rhyngwyneb sy'n cael ei lansio a rhedwch gam bysellfwrdd-yn-unig a darllenydd sgrin yn y cyfarfod, oherwydd y bylchau a ganfyddwch yw'r canfyddiadau archwilio y byddech chi fel arall yn eu cael yn ddiweddarach. Ar gyfer gwaith llywodraeth mae'r gydymffurfiaeth hon yn rhagofyniad caffael, felly triniwch hi fel porth, nid tasg glanhau.

4. **Pwy sy'n berchen ar bob rheolaeth a phob derbyniad risg, ac a oes gan eich eithriadau berchnogion a dyddiadau dod i ben?** Llywodraethu yw'r hyn sy'n troi cydymffurfiaeth o frwydr flynyddol yn briodwedd barhaol, ac mae'n methu'n dawel pan fydd gan reolaeth ddogfennaeth ond dim perchennog atebol, neu pan fydd derbyniad risg a roddwyd yn "dros dro" yn parhau am flynyddoedd. Penderfynwch pwy sy'n arwyddo pob rheolaeth, pwy sy'n adolygu eithriadau, a sut mae bylchau'n cael perchennog a therfyn amser yn hytrach na lingeru'n dawel mewn taenlen. Y dynfa gystadleuol yw cyflymder yn erbyn atebolrwydd: mae enwi perchnogion a gorfodi terfyn amser yn arafu pobl, ond mae rheolaethau heb berchennog yn llithro a daw eithriadau diderfyn yn ganfyddiad sy'n suddo'r archwiliad. Dewch â'ch cofrestr eithriadau bresennol a gwiriwch faint o gofnodion sydd â pherchennog wedi'i enwi a dyddiad dod i ben byw, oherwydd y bylchau gwag yw eich risg gronnol. I fenter fawr mae hyn yn ehangder rheolaeth ar draws llawer o dimau, ac i lywodraeth mae'r swyddog atebol a'r derbyniad risg wedi'i ddogfennu eu hunain yn arteffactau archwilio y bydd adolygydd yn eu mynnu.

5. **Pan fydd rhwymedigaethau cadw cofnodion yn gwrthdaro â hawliau dileu preifatrwydd, sut ydych chi'n datrys y gwrthdaro, ac a yw'r datrysiad hwnnw wedi'i ysgrifennu i lawr?** Mae'r dyletswyddau hyn yn gwrthdaro mewn gwirionedd: gall statud fynnu eich bod yn cadw cofnod am flynyddoedd tra bod goddrych data'n arfer hawl i gael ei anghofio, a gall peiriannydd sy'n byrfyfyrio dileu dorri'r drefn gadw mor rhwydd ag y gall daliad rhy eang dorri cyfraith breifatrwydd. Penderfynwch y rheolau blaenoriaeth ymlaen llaw, dosbarth wrth ddosbarth o gofnod, a dogfennwch sut mae daliad cyfreithiol, golygu allan, neu eithriad sail-gyfreithlon yn drech na chais dileu. Y tyndra i'w bwyso yw tryloywder a hawliau unigol yn erbyn cadw statudol a'r gallu i ateb cais FOIA neu ddarganfod o fewn amserlen gyfreithiol. Dewch â'ch trefn gadw ac un cais dileu go iawn, a cherddwch y llwybr penderfynu gwirioneddol yn y cyfarfod. I lywodraeth mae'r risgiau uchaf, oherwydd bod terfynau amser ymateb FOIA, cyfraith dosbarthu cofnodion, a hawliau preifatrwydd i gyd yn cario grym cyfreithiol ar unwaith, ac mae'n rhaid i'r cysoniad fod yn amddiffynadwy i fwy nag un rheoleiddiwr.

6. **A ydych yn adeiladu gallu cydymffurfiaeth yn fewnol neu'n ei brynu, ac a yw'r dewis hwnnw'n cyfateb i'r tystysgrifau sydd mewn gwirionedd yn porthi eich refeniw?** Sylfaen ddiramant cydymffurfiaeth barhaus yw staff ac offer, ac mae cynlluniau'n methu llai ar y fframwaith na phan nad oes neb i redeg y llwyfan GRC, tystiolaethu'r rheolaethau, neu ddehongli cyfundrefn newydd. Penderfynwch yn fwriadol pa rannau rydych yn eu staffio'n fewnol, pa rai rydych yn eu prynu fel llwyfan llywodraethu, risg, a chydymffurfiaeth, a lle rydych yn dod ag ymgynghorwyr i mewn ar gyfer awdurdodiad penodol, yna paru hynny â'r tystysgrifau sy'n dad-flocio pibell go iawn. Y cyfaddawd yw cyd-destun a rheolaeth fewnol ddwfn yn erbyn y gost a'r arbenigwyr prin y mae swyddogaeth gydymffurfiaeth lawn yn eu mynnu, o'i gymharu â dibyniaeth ar werthwr a ffioedd sy'n ailddigwydd os ydych yn prynu. Dewch â'r rhestr tystysgrifau sy'n gysylltiedig â bargeinion agored, gwir gost brwydr archwilio â llaw, a'ch bylchau staffio presennol. I fenter mae hyn yn economeg portffolio ar draws llawer o archwiliadau, ac i lywodraeth mae'r amseroedd arwain hir o awdurdodiad a chliriad yn golygu bod gallu na allwch ei staffio o fewn y ffenestr berthnasol yn gontract na allwch ei ennill.

## Trwy lens sector

**Cwmni newydd.** Ewch ar drywydd dim ond y dystysgrif sy'n dad-flocio'r fargen o'ch blaen, fel arfer SOC 2, ac estynnwch amdani gyda theclyn awtomeiddio cydymffurfiaeth yn hytrach na chyflogaeth. Ysgrifennwch i lawr y dyrnaid o reolaethau y gallwch eu cynnal mewn gwirionedd, cysylltwch gasglu tystiolaeth â'ch cwmwl a'ch cod o'r diwrnod cyntaf, a hepgorwch y fframweithiau nad oes unrhyw gwsmer yn gofyn amdanynt eto. Mae adroddiad Math I a enillwyd o arferion go iawn yn curo ffeil o bolisïau uchelgeisiol na fyddwch byth yn eu dilyn.

**Busnes bach.** Heb arbenigwr cydymffurfiaeth bwrpasol a chyllideb dynn, dibynnwch ar lwyfan llywodraethu, risg, a chydymffurfiaeth neu ymgynghorydd rhannol yn lle sefydlu swyddogaeth. Ffafriwch dystysgrifau y mae eich prynwyr yn eu mynnu mewn gwirionedd dros wal o logos, a thriniwch gadw cofnodion a hygyrchedd fel rhestrau gwirio diriaethol yn hytrach na rhaglen. Prynwch y groesfapio a'r awtomeiddio tystiolaeth yn hytrach na'u hadeiladu, oherwydd bod eich amser peirianneg prin yn well ei dreulio ar y cynnyrch.

**Menter.** Y gwaith yw llywodraethu portffolio ar draws llawer o dimau: un llyfrgell reolaeth unedig wedi'i chroesfapio i SOC 2, ISO 27001, HIPAA, a PCI-DSS, gyda thystiolaeth yn cael ei chasglu'n awtomatig i mewn i stôr a rennir. Enwch berchnogion ar gyfer pob rheolaeth a derbyniad risg, gorfodwch derfyn amser ar eithriadau, a rheolwch dystysgrifau fel portffolio fel bod ychwanegu'r nesaf yn gost isel. Cyllidebwch yr offer GRC a chalendr yr archwiliad yn benodol, a chadwch gydymffurfiaeth yn briodwedd cyflwr sefydlog yn hytrach nag ymarfer tân blynyddol.

**Llywodraeth.** Mae rheolau caffael, tryloywder, ac atebolrwydd cyhoeddus yn llunio pob dewis. Triniwch awdurdodiad FedRAMP neu FISMA fel rhwymedigaeth barhaus gyda Chynllun Diogelwch System byw a monitro parhaus, nid gwthiad diwrnod lansio, a chadwch gydymffurfiaeth WCAG AA a Section 508 fel pyrth caffael. Bodlonwch derfynau amser dosbarthu cofnodion a FOIA ar amserlenni statudol, cysonwch nhw yn erbyn hawliau dileu preifatrwydd yn ysgrifenedig, a chadwch swyddog atebol wedi'i enwi ar gyfer pob rheolaeth ganlyniadol.

## Enghreifftiau

**Cwmni newydd.** Mae cwmni newydd SaaS cam-hadu'n canfod bod ei fargen fenter gyntaf wedi'i rhwystro ar adroddiad SOC 2 nad oes ganddo, felly mae'n dechrau'n fach: mae'n troi ymlaen declyn awtomeiddio cydymffurfiaeth sy'n gwylio ei gwmwl a'i god, ac mae'n ysgrifennu i lawr y dyrnaid o reolaethau y gall eu cynnal mewn gwirionedd yn hytrach na pholisïau uchelgeisiol y bydd yn eu hanwybyddu. Drwy gasglu tystiolaeth yn awtomatig o'r dechrau, gan gynnwys adolygiadau mynediad, copïau wrth gefn, a chymeradwyaethau newid, mae'n cyrraedd adroddiad Math I mewn wythnosau yn lle chwarter panig o sgrinluniau. Mae trin y rheolaethau hynny fel arferion go iawn yn hytrach na theatr archwilio'n golygu bod y dystysgrif yn adlewyrchu sut mae'r tîm yn gweithio mewn gwirionedd ac yn dad-flocio'r refeniw roeddent yn ei hela.

**Menter.** Mae gwerthwr meddalwedd cwmwl yn adeiladu un fframwaith rheolaeth sengl wedi'i groesfapio i SOC 2, ISO 27001, HIPAA, a PCI-DSS. Caiff tystiolaeth (adolygiadau mynediad, sganiau gwendid, cymeradwyaethau newid, gwiriad copi wrth gefn) ei chasglu'n awtomatig i mewn i lwyfan GRC (llywodraethu, risg, a chydymffurfiaeth), fel bod pob archwiliad blynyddol yn tynnu o stôr tystiolaeth byw yn hytrach na mis gwyllt o sgrinluniau. Am fod rheolaethau'n mapio ar draws fframweithiau, ychydig o waith cynyddrannol oedd angen ychwanegu ISO 27001 ar ôl SOC 2, a gall y cwmni roi ardystiad cyfredol i brynwyr mentrau ar alw, gan fyrhau cylchoedd gwerthu.

**Llywodraeth.** Mae contractwr sy'n mynd ar drywydd defnydd cwmwl ffederal yn categoreiddio ei system fel FISMA cymedrol, yn dewis y rheolaethau NIST SP 800-53 cyfatebol, ac yn gweithio tuag at awdurdodiad FedRAMP gyda Chynllun Diogelwch System a POA&M sy'n olrhain bylchau sy'n weddill. Wrth drin Gwybodaeth Ddiddosbarth Reoledig, mae hefyd yn bodloni NIST SP 800-171 a'r lefel CMMC berthnasol ar gyfer ei waith amddiffyn. Mae pob rhyngwyneb sy'n wynebu dinasyddion yn cydymffurfio â WCAG AA i fodloni Section 508, wedi'i ddogfennu mewn VPAT. Mae cofnodion yn dilyn trefnau cadw statudol ac yn chwiliadwy i fodloni terfynau amser ymateb FOIA, gyda monitro parhaus yn cynnal yr awdurdodiad dros amser.

## Achos busnes: cymhellion, ROI, a TCO

Mae cydymffurfiaeth yn anghyffredin ymhlith buddsoddiadau diogelwch oherwydd bod ei ROI yn aml yn refeniw uniongyrchol, nid colled a osgowyd yn unig. Heb y tystysgrifau a'r awdurdodiadau cywir, mae marchnadoedd cyfan yn syml ar gau. Mae SOC 2'n dad-flocio bargeinion mentrau; mae FedRAMP yn dad-flocio rhai ffederal; mae HIPAA a PCI-DSS yn dad-flocio gofal iechyd a thaliadau. Mae cyfanswm cost perchnogaeth yn cynnwys ffioedd archwilio, offer GRC, staff neu ymgynghorwyr cydymffurfiaeth, ac amser peirianneg i weithredu a thystiolaethu rheolaethau, ynghyd â chost sylweddol iawn mynd ar drywydd awdurdodiadau llywodraeth. Ond cost peidio â bod yn gydymffurfiol yw colli'r busnes yn gyfan gwbl, ynghyd â'r dirwyon, sancsiynau, a therfyniadau contract sy'n dilyn troseddau, a all gyrraedd canran sylweddol o refeniw.

Y trosol effeithlonrwydd yw'r fframwaith rheolaeth unedig gyda thystiolaeth barhaus, awtomataidd. Mae'n torri cost ymylol pob tystysgrif ychwanegol, ac mae'n troi archwiliadau o ymarferion tân drud yn wiriadau arferol yn erbyn stôr tystiolaeth byw. Wrth wneud yr achos i arweinyddiaeth, fframiwch gydymffurfiaeth fel galluogi refeniw a lleihau risg gyda'i gilydd. Meintiolwch y bibell sydd angen pob tystysgrif, cost archwiliad wedi methu neu awdurdodiad a gollwyd, a'r cynilion o awtomeiddio o'i gymharu â brwydro â llaw parhaus. I gontractwyr llywodraeth, pwysleisiwch mai'r awdurdodiad yw'r porth i'r contract, ac mai monitro parhaus sy'n cadw'r porth ar agor.

## Gwrth-batrymau a pheryglon

- **Brwydrau wedi'u gyrru gan archwiliad.** Gwneud dim nes bod archwiliad yn agosáu, yna cydosod tystiolaeth mewn panig a gadael i reolaethau lithro rhwng archwiliadau.
- **Cydymffurfiaeth pwynt-mewn-amser.** Pasio'r archwiliad, yna gadael y rheolaethau tan y flwyddyn nesaf.
- **Seilos fframwaith.** Rheoli pob tystysgrif ar wahân, gan ddyblygu ymdrech yn hytrach na mapio rheolaethau unwaith.
- **Theatr cydymffurfiaeth.** Dogfennau a sgrinluniau sy'n bodloni archwiliwr ond nad ydynt yn adlewyrchu unrhyw reolaeth go iawn.
- **Hygyrchedd fel ôl-feddwl.** Gosod hygyrchedd arno'n hwyr, gan gynhyrchu canlyniadau gwael, anghydymffurfiol a risg gyfreithiol.
- **Anwybyddu rhwymedigaethau cofnodion.** Methu dyletswyddau cadw a FOIA nes bod cais cyfreithiol yn datgelu'r bwlch.
- **Trin ATO fel un-a-wedi-gorffen.** Cael eich awdurdodi, yna esgeuluso'r monitro parhaus sy'n cadw'r awdurdodiad yn ddilys.
- **Cymysgu cydymffurfiaeth â diogelwch.** Nid yw pasio archwiliad yr un peth â bod yn ddiogel; llawr yw cydymffurfiaeth, nid nenfwd.

## Model aeddfedrwydd

**Lefel 1: Cychwyn.** Mae cydymffurfiaeth yn adweithiol ac yn ad hoc. Nid oes fframwaith rheolaeth yn bodoli. Caiff tystiolaeth ei chydosod â llaw o dan bwysau dyddiad cau, fframwaith wrth fframwaith. Caiff rhwymedigaethau hygyrchedd a chofnodion eu hanwybyddu i raddau helaeth. Mae canfyddiadau a phethau a aeth bron o'i le yn aml, ac mae pob archwiliad yn frwydr newydd.

**Lefel 2: Datblygu.** Caiff prif fframweithiau eu nodi a chaiff rhai rheolaethau a pholisïau eu dogfennu, ond mae'r arfer yn anghyson ar draws timau: mae un grŵp yn cynnal adolygiadau mynediad tra nad yw un arall yn gwneud hynny. Mae archwiliadau'n pasio, ond dim ond gydag ymdrech â llaw drwm. Ystyrir hygyrchedd yn hwyr, ac mae cadw cofnodion sylfaenol yn bodoli mewn pocedi heb drefn unedig.

**Lefel 3: Safoni.** Caiff un llyfrgell reolaeth sengl ei dogfennu ac mae'n croesfapio'r prif safonau, fel bod gweithredu un rheolaeth yn tystiolaethu sawl un ar unwaith, a chaiff ei gorfodi ar draws y sefydliad yn hytrach na thîm wrth dîm. Caiff hygyrchedd ei adeiladu i mewn i ddylunio a phrofi a chaiff cydymffurfiaeth ei dogfennu mewn VPAT. Caiff rheoli cofnodion, ac, i lywodraeth, barodrwydd FOIA, eu sefydlu, a chaiff awdurdodiadau eu mynd ar eu trywydd gyda Chynllun Diogelwch System a POA&M.

**Lefel 4: Rheoli.** Caiff y rhaglen gydymffurfiaeth ei mesur yn erbyn llinellau sylfaen a thargedau, nid dim ond ei dogfennu. Mae'r sefydliad yn olrhain cwmpas rheolaeth, ffresni tystiolaeth, amser i gasglu tystiolaeth, canfyddiadau archwilio agored a'u hoedran, cyfrif eithriadau a chydymffurfiaeth â therfynau amser, amser cyfartalog i unioni bwlch, a chyfraddau cydymffurfiaeth hygyrchedd, yna'n eu hadolygu yn erbyn llinellau sylfaen cyfnod blaenorol. Mae gan dderbyniadau risg berchnogion, dyddiadau dod i ben, a metrigau; caiff llithriant ei ganfod o'r dangosfwrdd yn hytrach na'i ddarganfod adeg archwilio; ac mae penderfyniadau mynd/peidio â mynd ar dystysgrif newydd yn dibynnu ar barodrwydd wedi'i fesur.

**Lefel 5: Cydgysylltu.** Cydymffurfiaeth barhaus yw'r cyflwr sefydlog, gyda thystiolaeth awtomataidd, bob amser ymlaen a chanllawiau cydymffurfiaeth-fel-cod sy'n gorfodi ac yn gwirio rheolaethau adeg defnyddio. Mae ychwanegu tystysgrif newydd yn gost isel oherwydd bod y fframwaith unedig eisoes yn ymdrin â'r rhan fwyaf ohoni. Mae monitro parhaus yn cynnal awdurdodiadau heb dor-barhad, mae cydymffurfiaeth wedi'i hintegreiddio â chynllunio busnes a risg, ac mae'r sefydliad yn addasu rheolaethau'n rhagweithiol wrth i reoliadau a bygythiadau newid, gan aros yn barod i'w archwilio ar unrhyw adeg.

## Syniadau ar gyfer trafodaeth

1. Pa dystysgrifau sydd mewn gwirionedd yn dad-flocio refeniw i'ch sefydliad, ac ym mha flaenoriaeth?
2. Sut ydych chi'n adeiladu croesfapio rheolaeth unedig heb iddo ddod yn faich biwrocrataidd ei hun?
3. Beth fyddai ei angen i wneud eich sefydliad yn barod i'w archwilio ar unrhyw adeg yn hytrach nag adeg archwilio?
4. Sut ydych chi'n cysoni rhwymedigaethau cadw cofnodion â hawliau dileu preifatrwydd pan fyddant yn gwrthdaro?
5. Sut ydych chi'n cadw cydymffurfiaeth rhag dirywio'n theatr sy'n bodloni archwilwyr ond nad yw'n adlewyrchu unrhyw reolaeth go iawn?
6. Ar gyfer gwaith llywodraeth, sut ydych chi'n cynnal monitro parhaus fel na fydd awdurdodiadau byth yn dod i ben?

## Prif negeseuon

- Cydymffurfiaeth yn aml yw'r drwydded i weithredu: hebddi, mae marchnadoedd cyfan ar gau.
- Adeiladwch un fframwaith rheolaeth unedig wedi'i groesfapio i lawer o safonau, a mapiwch reolaethau unwaith.
- Mae cyfundrefnau llywodraeth (FISMA, FedRAMP, NIST 800-53/171, CMMC, lefelau effaith) yn drylwyr ac ni ellir eu trafod.
- Mandad cyfreithiol yw hygyrchedd (Section 508, ADA, WCAG, EN 301 549), nid rhinwedd ddewisol.
- Symudwch o frwydrau archwilio cyfnodol i gydymffurfiaeth barhaus gyda thystiolaeth awtomataidd.
- Mae rheoli cofnodion a FOIA'n cario rhwymedigaethau cyfreithiol go iawn, yn enwedig mewn llywodraeth.
- Llawr yw pasio archwiliad, nid prawf o ddiogelwch; mae cydymffurfiaeth a diogelwch yn gysylltiedig ond yn wahanol.

## Cyfeiriadau a darllen pellach

- National Institute of Standards and Technology, *SP 800-53: Security and Privacy Controls*
- National Institute of Standards and Technology, *SP 800-171: Protecting Controlled Unclassified Information*
- National Institute of Standards and Technology, *Cybersecurity Framework (CSF)*
- ISO/IEC 27001, *Information Security Management Systems*
- AICPA, *SOC 2 Trust Services Criteria*
- PCI Security Standards Council, *Payment Card Industry Data Security Standard*
- US General Services Administration, *FedRAMP* documentation; *Section 508* standards
- W3C, *Web Content Accessibility Guidelines (WCAG)*; ETSI *EN 301 549*
