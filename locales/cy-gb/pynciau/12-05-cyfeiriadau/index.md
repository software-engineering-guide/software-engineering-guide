# 12.5 Cyfeiriadau

Mae'r adran hon yn cyfuno cyfarpar cyfeirio'r llawlyfr: croesgyfeirio i gorff
gwybodaeth SWEBOK, mynegai i'r safonau a'r fframweithiau a ddyfynnir drwyddo
draw, a llyfryddiaeth ddethol o ddarllen argymelledig. Mae ffynonellau ar gyfer
pob pennod hefyd yn ymddangos yn yr adran *Cyfeiriadau a darllen pellach* ar
ddiwedd pob pennod.

---

# Croesgyfeirio SWEBOK

Mae'r llawlyfr hwn wedi'i alinio â **SWEBOK V4.0** (Software Engineering Body
of Knowledge) IEEE Computer Society. Mae'r 18 maes gwybodaeth i gyd wedi'u
cynnwys; mae'r tabl yn mapio pob un i'r penodau sy'n ymdrin ag ef, ac wedyn
mae'r llawlyfr yn mynd ymhell y tu hwnt i SWEBOK i mewn i AI, data, UX,
DevOps, cynaliadwyedd, llif, a thechnoleg budd y cyhoedd.

| Maes gwybodaeth SWEBOK V4.0 | Prif benodau |
|---|---|
| 1. Gofynion Meddalwedd | 2.8, 11.1, 5.1 |
| 2. Pensaernïaeth Meddalwedd | 3.1, 3.2, 3.3 |
| 3. Dylunio Meddalwedd | 2.2, 3.1 |
| 4. Adeiladu Meddalwedd | 2.9, 2.1 |
| 5. Profi Meddalwedd | 2.4, 8.5 |
| 6. Gweithrediadau Peirianneg Meddalwedd | 9.1, 9.2, 9.3, 8.1 |
| 7. Cynnal a Chadw Meddalwedd | 3.7, 3.6, 10.4 |
| 8. Rheoli Ffurfweddiad Meddalwedd | 2.10, 2.6, 8.2 |
| 9. Rheolaeth Peirianneg Meddalwedd | 10.1, 10.6, 10.2 |
| 10. Proses Peirianneg Meddalwedd | 1.4, 10.7, 10.8 |
| 11. Modelau a Dulliau Peirianneg Meddalwedd | 2.12, 3.1, 2.2 |
| 12. Ansawdd Meddalwedd | 2.11, 2.4, 3.1 |
| 13. Diogelwch Meddalwedd | 4.1, 4.2, 4.3, 4.4 |
| 14. Ymarfer Proffesiynol Peirianneg Meddalwedd | 10.5, 1.1, 1.3 |
| 15. Economeg Peirianneg Meddalwedd | 10.10, 10.1, 9.4 |
| 16. Sylfeini Cyfrifiadura | 2.13, 3.3, 3.4 |
| 17. Sylfeini Mathemategol | 2.13, 11.3 |
| 18. Sylfeini Peirianneg | 2.13, 3.1 |

---

# Safonau a fframweithiau

Mae'r atodiad hwn yn fynegai trefnus o'r safonau, fframweithiau, a rheoliadau
go iawn a ddyfynnir drwy'r llawlyfr. Mae'n gymorth llywio, nid yn llawlyfr
cydymffurfiaeth: ymgynghorwch bob amser â'r ffynhonnell awdurdodol ac, lle bo'n
berthnasol, â chyfreithiwr neu archwilydd cymwysedig am y testun cyfredol a'i
berthnasedd i'ch cyd-destun.

Trefnwyd y cofnodion yn ôl maes. Mae pob un yn enwi'r safon neu'r fframwaith,
y corff cyhoeddi, cwmpas un llinell, a'r penodau neu'r meysydd lle mae fwyaf
perthnasol. Lle bo enw'n cael ei fyrfoddi'n gyffredin, dangosir y byrfodd.
Rhoddir rhifau a theitlau dogfennau dim ond lle maent wedi'u sefydlu'n dda; ni
chynhwysir unrhyw URLau.

## Sut i ddefnyddio'r atodiad hwn

- **Rheoliadau** (er enghraifft, GDPR, HIPAA) sy'n rhwymol gyfreithiol o fewn
  eu hawdurdodaeth a'u sector. Maent yn gosod rhwymedigaethau, nid dim ond
  arfer da.
- **Safonau** (er enghraifft, ISO/IEC 27001, WCAG) yw manylebau ffurfiol, sy'n
  aml yn ardystiadwy. Mae rhai'n wirfoddol; mae rhai'n orfodol yn ôl cyfraith
  neu gontract.
- **Fframweithiau** (er enghraifft, NIST CSF, NIST AI RMF) yw canllawiau
  strwythuredig, gwirfoddol fel arfer, y byddwch yn eu teilwra i'ch proffil
  risg.
- Mae perthnasedd yn dibynnu ar awdurdodaeth, sector, mathau o ddata, a
  thelerau contract. Rhaid i lawer o sefydliadau fodloni sawl un o'r rhain ar
  unwaith.

## Diogelwch a phreifatrwydd

| Safon / fframwaith | Corff cyhoeddi | Cwmpas (un llinell) | Prif benodau / meysydd |
| --- | --- | --- | --- |
| ISO/IEC 27001 | ISO / IEC | Gofynion ar gyfer System Rheoli Diogelwch Gwybodaeth (ISMS). | 4.1–4.6 Diogelwch a chydymffurfiaeth |
| ISO/IEC 27002 | ISO / IEC | Canllawiau a set reolaethau i gefnogi ISO/IEC 27001. | 4.1–4.4 Diogelwch |
| ISO/IEC 27017 / 27018 | ISO / IEC | Rheolaethau diogelwch penodol i'r cwmwl (27017) a diogelu data personol adnabyddadwy yn y cwmwl (27018). | 4.3 Seilwaith a diogelwch cwmwl; 4.5 Preifatrwydd |
| NIST Cybersecurity Framework (CSF) | National Institute of Standards and Technology | Fframwaith gwirfoddol wedi'i drefnu o amgylch Llywodraethu, Adnabod, Diogelu, Canfod, Ymateb, Adfer. | 4.1, 4.4 Sylfeini a gweithrediadau diogelwch |
| NIST SP 800-53 | National Institute of Standards and Technology | Catalog o reolaethau diogelwch a phreifatrwydd ar gyfer systemau gwybodaeth. | 4.3, 4.6 Diogelwch cwmwl a chydymffurfiaeth |
| NIST SP 800-63 | National Institute of Standards and Technology | Canllawiau sicrwydd hunaniaeth ddigidol a dilysu. | 4.2, 4.3 Diogelwch cymhwysiad a seilwaith |
| OWASP Top Ten | Open Worldwide Application Security Project | Y risgiau diogelwch cymhwysiad gwe mwyaf critigol, wedi'u diweddaru'n gyfnodol. | 4.2 Diogelwch cymhwysiadau |
| OWASP ASVS | Open Worldwide Application Security Project | Gofynion a phrofion gradd ar gyfer gwirio diogelwch cymhwysiadau. | 2.4, 4.2 Profi a diogelwch cymhwysiadau |
| OWASP SAMM | Open Worldwide Application Security Project | Model aeddfedrwydd ar gyfer adeiladu ac asesu rhaglen diogelwch meddalwedd. | 4.1 Sylfeini a diwylliant diogelwch |
| STRIDE | Originated at Microsoft | Tacsonomeg modelu bygythiadau ar gyfer dosbarthu bygythiadau. | 4.2 Diogelwch cymhwysiadau |
| MITRE ATT&CK | MITRE | Cronfa wybodaeth o dactegau a thechnegau gwrthwynebwyr ar gyfer canfod ac amddiffyn. | 4.4 Gweithrediadau diogelwch |
| SLSA | Open Source Security Foundation (OpenSSF) | Fframwaith graddol ar gyfer cyfanrwydd a tharddiad cadwyn gyflenwi meddalwedd. | 4.2, 8.1, 10.3 Cadwyn gyflenwi a chyflenwi |
| SBOM (SPDX / CycloneDX) | Linux Foundation (SPDX); OWASP (CycloneDX) | Fformatau safonol ar gyfer biliau deunyddiau meddalwedd. | 4.2, 10.3 Diogelwch cymhwysiadau a thrwyddedu |
| PCI DSS | PCI Security Standards Council | Gofynion diogelwch ar gyfer trin data cardiau talu. | 4.2, 4.5, 4.6 Diogelwch, preifatrwydd, cydymffurfiaeth |

## Cydymffurfiaeth a llywodraeth

### Yr Unol Daleithiau

| Rheoliad / fframwaith | Corff cyhoeddi | Cwmpas (un llinell) | Prif benodau / meysydd |
| --- | --- | --- | --- |
| HIPAA | US Dept. of Health and Human Services | Mesurau diogelu ar gyfer gwybodaeth iechyd warchodedig (PHI). | 4.5, 4.6 Preifatrwydd a chydymffurfiaeth |
| SOX (Sarbanes-Oxley Act) | US Congress / SEC | Gofynion adrodd ariannol a rheolaeth fewnol ar gyfer cwmnïau cyhoeddus. | 4.6, 10.2 Cydymffurfiaeth ac archwilio |
| FISMA | US Congress | Gofynion rhaglen diogelwch gwybodaeth ar gyfer asiantaethau ffederal. | 4.3, 4.6 Diogelwch cwmwl a chydymffurfiaeth |
| FedRAMP | US General Services Administration / FedRAMP PMO | Awdurdodiad diogelwch safonol ar gyfer gwasanaethau cwmwl a ddefnyddir gan asiantaethau ffederal. | 4.3, 4.6 Diogelwch cwmwl a chydymffurfiaeth |
| NIST SP 800-171 | National Institute of Standards and Technology | Diogelu gwybodaeth reoledig, ddigyfrinach (CUI) mewn systemau anffederal. | 4.6 Cydymffurfiaeth (cadwyn gyflenwi amddiffyn) |
| CMMC | US Department of Defense | Ardystio aeddfedrwydd seiberddiogelwch contractwyr amddiffyn. | 4.6 Cydymffurfiaeth (amddiffyn) |
| FIPS 140-3 | National Institute of Standards and Technology | Gofynion diogelwch ar gyfer modiwlau cryptograffig. | 4.3 Seilwaith a diogelwch cwmwl |
| CCPA / CPRA | State of California | Hawliau preifatrwydd defnyddwyr a rhwymedigaethau busnes yng Nghaliffornia. | 4.5 Preifatrwydd a diogelu data |

### Yr Undeb Ewropeaidd a'r Deyrnas Unedig

| Rheoliad / safon | Corff cyhoeddi | Cwmpas (un llinell) | Prif benodau / meysydd |
| --- | --- | --- | --- |
| GDPR | European Union | Rheoliad cynhwysfawr ar brosesu data personol. | 4.5, 4.6 Preifatrwydd a chydymffurfiaeth |
| UK GDPR / Data Protection Act 2018 | United Kingdom | Cyfundrefn diogelu data ôl-Brexit y DU. | 4.5, 4.6 Preifatrwydd a chydymffurfiaeth |
| eIDAS | European Union | Fframwaith ar gyfer adnabyddiaeth electronig a gwasanaethau ymddiriedaeth. | 4.2, 4.3 Diogelwch |
| NIS2 Directive | European Union | Rhwymedigaethau seiberddiogelwch ar gyfer endidau hanfodol a phwysig. | 4.4, 4.6 Gweithrediadau diogelwch a chydymffurfiaeth |
| DORA (Digital Operational Resilience Act) | European Union | Gofynion gwydnwch gweithredol ar gyfer y sector ariannol. | 9.1, 10.2 Dibynadwyedd ac archwilio |
| EU AI Act | European Union | Rheoleiddio AI yn seiliedig ar risg (gweler llywodraethu AI isod). | 6.1, 6.5 Strategaeth AI ac AI cyfrifol |

## Hygyrchedd

| Safon | Corff cyhoeddi | Cwmpas (un llinell) | Prif benodau / meysydd |
| --- | --- | --- | --- |
| WCAG (2.1 / 2.2) | World Wide Web Consortium (W3C) | Canllawiau ar gyfer cynnwys gwe hygyrch, gyda lefelau cydymffurfio A/AA/AAA. | 5.3 Hygyrchedd; 5.1–5.6 UX a blaen-ben |
| WAI-ARIA | World Wide Web Consortium (W3C) | Rolau, cyflyrau, a phriodweddau ar gyfer cymwysiadau rhyngrwyd cyfoethog hygyrch. | 5.3, 5.6 Hygyrchedd a blaen-ben |
| Section 508 | US Access Board / US federal law | Gofynion hygyrchedd ar gyfer TGCh ffederal UDA, wedi'u halinio â WCAG. | 5.3 Hygyrchedd (llywodraeth UDA) |
| EN 301 549 | ETSI / CEN / CENELEC | Gofynion hygyrchedd Ewropeaidd ar gyfer caffael TGCh, wedi'u halinio â WCAG. | 5.3 Hygyrchedd (sector cyhoeddus yr UE) |
| ADA (Americans with Disabilities Act) | US Congress | Cyfraith hawliau sifil sy'n gwahardd gwahaniaethu ar sail anabledd, wedi'i chymhwyso i wasanaethau digidol. | 5.3 Hygyrchedd |
| ISO/IEC 40500 | ISO / IEC | Mabwysiadu WCAG 2.0 yn rhyngwladol fel safon ffurfiol. | 5.3 Hygyrchedd |

## Llywodraethu AI

| Fframwaith / rheoliad | Corff cyhoeddi | Cwmpas (un llinell) | Prif benodau / meysydd |
| --- | --- | --- | --- |
| NIST AI Risk Management Framework (AI RMF) | National Institute of Standards and Technology | Fframwaith gwirfoddol i lywodraethu, mapio, mesur, a rheoli risg AI. | 6.1, 6.5 Strategaeth AI ac AI cyfrifol |
| ISO/IEC 42001 | ISO / IEC | Gofynion ar gyfer System Rheoli AI (AIMS). | 6.1, 6.5 Llywodraethu AI |
| ISO/IEC 23894 | ISO / IEC | Canllawiau ar reoli risg penodol i AI. | 6.5 AI cyfrifol a dibynadwy |
| EU AI Act | European Union | Rhwymedigaethau cyfreithiol graddedig yn ôl risg ar gyfer darparwyr a defnyddwyr systemau AI. | 6.1, 6.3, 6.5 Cymwysiadau a llywodraethu AI |
| OECD AI Principles | Organisation for Economic Co-operation and Development | Egwyddorion yn seiliedig ar werthoedd ar gyfer AI dibynadwy, dylanwadol ar bolisi. | 6.5, 10.5 AI cyfrifol a moeseg |

## Ansawdd a phroses

| Safon / fframwaith | Corff cyhoeddi | Cwmpas (un llinell) | Prif benodau / meysydd |
| --- | --- | --- | --- |
| ISO/IEC 25010 | ISO / IEC | Model ansawdd cynnyrch meddalwedd (addasrwydd swyddogaethol, dibynadwyedd, diogelwch, ac ati). | 2.2, 2.4 Dylunio a phrofi |
| ISO/IEC/IEEE 12207 | ISO / IEC / IEEE | Prosesau cylch bywyd meddalwedd. | 1.4, 10.1 Ffyrdd o weithio a rheoli rhaglenni |
| ISO 9001 | ISO | Gofynion ar gyfer System Rheoli Ansawdd gyffredinol. | 10.2 Risg, archwilio, a sicrwydd |
| CMMI | ISACA / CMMI Institute | Model aeddfedrwydd ar gyfer gallu a gwelliant proses. | 10.1, 10.2 Rheoli rhaglenni a sicrwydd |
| DORA metrics | DevOps Research and Assessment (Google Cloud) | Pedwar metrig perfformiad cyflenwi allweddol ar gyfer timau meddalwedd. | 8.1, 8.4, 9.1 Cyflenwi, platfform, dibynadwyedd |
| SPACE framework | Microsoft / GitHub researchers | Model amlddimensiwn ar gyfer mesur cynhyrchedd datblygwyr. | 1.3, 8.4 Twf a phrofiad datblygwyr |
| ITIL | AXELOS / PeopleCert | Fframwaith arferion rheoli gwasanaethau TG. | 9.1, 9.3 Dibynadwyedd a rheoli digwyddiadau |

## Pensaernïaeth

| Safon / fframwaith | Corff cyhoeddi | Cwmpas (un llinell) | Prif benodau / meysydd |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010 | ISO / IEC / IEEE | Safon ar gyfer disgrifio pensaernïaeth a golygfeydd. | 2.7, 3.1 Dogfennaeth a sylfeini pensaernïaeth |
| TOGAF | The Open Group | Fframwaith a dull datblygu pensaernïaeth fenter. | 3.1, 10.1 Pensaernïaeth a rheoli portffolio |
| C4 model | Community (Simon Brown) | Dull pedwar lefel ar gyfer delweddu pensaernïaeth meddalwedd. | 2.7, 3.1 Dogfennaeth a phensaernïaeth |
| arc42 | Community (Starke / Hruschka) | Templed ar gyfer strwythuro dogfennaeth pensaernïaeth. | 2.7, 3.1 Dogfennaeth a phensaernïaeth |
| ADRs | Community practice | Cofnodion ysgafn o benderfyniadau pensaernïaeth arwyddocaol. | 1.5, 2.7, 3.1 Gwneud penderfyniadau a dogfennaeth |

## Cwmwl a DevOps

| Safon / fframwaith | Corff cyhoeddi | Cwmpas (un llinell) | Prif benodau / meysydd |
| --- | --- | --- | --- |
| CIS Benchmarks | Center for Internet Security | Meincnodau ffurfweddu diogel yn seiliedig ar gonsensws ar gyfer systemau a chwmwl. | 4.3, 8.2 Diogelwch seilwaith ac IaC |
| CNCF landscape and projects | Cloud Native Computing Foundation | Ecosystem a safonau ar gyfer cyfrifiadura brodorol i'r cwmwl (e.e. Kubernetes). | 8.3 Cynwysyddion a brodorol i'r cwmwl |
| OCI (Open Container Initiative) | Open Container Initiative (Linux Foundation) | Safonau agored ar gyfer fformatau delweddau a rhedeg cynwysyddion. | 8.3 Cynwysyddion a brodorol i'r cwmwl |
| OpenTelemetry | Cloud Native Computing Foundation | Safon niwtral o ran gwerthwr ar gyfer telemetreg (olrheiniadau, metrigau, logiau). | 9.2 Arsylwadwyedd a monitro |
| Open Policy Agent (OPA) | Cloud Native Computing Foundation | Peiriant polisi at ddibenion cyffredinol ar gyfer polisi fel cod. | 4.6, 8.2, 8.3 Cydymffurfiaeth, IaC, trefniannu |
| SRE practices | Google (widely adopted) | Dull yn seiliedig ar SLI/SLO/cyllideb gwallau ar gyfer gweithredu gwasanaethau dibynadwy. | 9.1 Peirianneg dibynadwyedd safleoedd |
| FinOps Framework | FinOps Foundation | Arferion ar gyfer rheolaeth ariannol cwmwl ac atebolrwydd cost. | 9.4 Cost, cynaliadwyedd, meddalwedd gwyrdd |

## Data

| Safon / fframwaith | Corff cyhoeddi | Cwmpas (un llinell) | Prif benodau / meysydd |
| --- | --- | --- | --- |
| DAMA-DMBOK | DAMA International | Corff gwybodaeth sy'n trefnu disgyblaethau rheoli data. | 7.1 Strategaeth a llywodraethu data |
| ISO/IEC 38505 | ISO / IEC | Llywodraethu data fel ased sefydliadol. | 7.1 Llywodraethu data |
| ISO 8000 | ISO | Safonau ansawdd data a data meistr. | 7.1, 7.2 Llywodraethu a pheirianneg data |
| Data mesh | Community (Zhamak Dehghani) | Dull datganoledig, wedi'i seilio ar barth, o drin data fel cynnyrch. | 7.1, 7.2 Strategaeth a pheirianneg data |
| DCAM | EDM Council | Model asesu gallu rheoli data. | 7.1 Strategaeth a llywodraethu data |

## Nodiadau ar gwmpas a newid

Mae safonau a rheoliadau'n esblygu. Mae rhifau fersiwn (er enghraifft, WCAG 2.1
o gymharu â 2.2, neu flynyddoedd adolygu ISO) a chatalogau rheolaethau'n
newid dros amser, ac mae cyfreithiau newydd (fel rheoliadau AI a gwydnwch
penodol i sector) yn parhau i ymddangos. Trinwch yr atodiad hwn fel map
cychwynnol: cadarnhewch y fersiwn gyfredol, yr awdurdodaeth, a'r perthnasedd
cyn dibynnu ar unrhyw gofnod ar gyfer penderfyniad cydymffurfiaeth neu
gaffael. Lle mae penodau'r llawlyfr a'r atodiad hwn yn gwahaniaethu o ran
manylion, y ddogfen ffynhonnell awdurdodol sydd bob amser yn llywodraethu.


---

# Darllen argymelledig

Mae'r atodiad hwn yn rhestr ddarllen ddethol, ag anodiadau, sy'n rhychwantu
pob maes yn y llawlyfr. Mae'n ffafrio gweithiau sydd wedi llunio arfer ar
raddfa fawr: clasuron cydnabyddedig, cyfeirlyfrau trylwyr, a'r safonau a'r
adroddiadau y mesurir timau mawr, menter, a llywodraeth yn eu herbyn.

Mae pob cofnod yn rhoi'r teitl a'r awdur(on), a'i ddilyn gan un frawddeg am
pam mae'n bwysig. Trefnwyd y rhestr o dan ddeg rhan y llyfr. Darllenwch yn
ddethol: dewiswch y ddau neu dri gwaith agosaf at eich poen presennol, nid y
silff gyfan. Lle mae gwaith yn rhychwantu meysydd, fe'i gosodir lle mae fwyaf
defnyddiol; mae llawer yn perthyn i sawl rhan.

Nodyn ar safonau: mae cyrff fel NIST, OWASP, W3C/WCAG, ISO, a rhaglen DORA yn
cyhoeddi dogfennau byw sy'n cael eu hadolygu'n gyfnodol. Dyfynnwch a
darllenwch y fersiwn gyfredol; mae'r anodiadau isod yn disgrifio eu diben
parhaus.

## Sylfeini: Diwylliant, Pobl, a Phroses

- **Accelerate: The Science of Lean Software and DevOps**. Nicole Forsgren, Jez Humble, Gene Kim. Y sylfaen ymchwil sy'n dangos bod perfformiad cyflenwi'n rhagfynegi perfformiad sefydliadol, ac yn diffinio'r metrigau (a elwir bellach yn DORA) i'w mesur.
- **The Phoenix Project**. Gene Kim, Kevin Behr, George Spafford. Nofel fusnes sy'n gwneud llif, gwaith ar y gweill, a "Thair Ffordd" DevOps yn reddfol i arweinwyr ac amheuwyr fel ei gilydd.
- **Team Topologies: Organizing Business and Technology Teams for Fast Flow**. Matthew Skelton and Manuel Pais. Geirfa ymarferol (timau wedi'u halinio â ffrwd, platfform, galluogi, ac is-system gymhleth) ar gyfer dylunio sefydliadau sy'n cynhyrchu meddalwedd dda.
- **An Elegant Puzzle: Systems of Engineering Management**. Will Larson. Fframweithiau wedi'u profi yn y maes ar gyfer maint timau, rheoli twf sefydliadol, a gwneud penderfyniadau cylchol arweinyddiaeth beirianneg.
- **Staff Engineer: Leadership Beyond the Management Track**. Will Larson. Yn diffinio'r archdeipiau staff-plws a'r llwybr arweinyddiaeth dechnegol i'r rhai sydd am gael effaith heb ddod yn rheolwyr.
- **The Manager's Path**. Camille Fournier. Canllaw fesul cam o arweinydd technegol i weithredwr sy'n angori ysgolion gyrfa a'r trawsnewid i reolaeth.
- **The Staff Engineer's Path**. Tanya Reilly. Cydymaith i lenyddiaeth staff-plws sy'n canolbwyntio ar waith bob dydd arweinyddiaeth dechnegol, dylanwad, a llywio heb awdurdod.
- **Peopleware: Productive Projects and Teams**. Tom DeMarco and Timothy Lister. Y ddadl barhaus mai problemau canolog meddalwedd yw rhai cymdeithasegol, nid technegol.
- **The Mythical Man-Month**. Frederick P. Brooks Jr. Tarddiad Cyfraith Brooks a'r gwahaniaeth rhwng cymhlethdod hanfodol a chymhlethdod damweiniol sy'n dal i lywodraethu staffio ac amserlennu.
- **The Fearless Organization: Creating Psychological Safety in the Workplace**. Amy C. Edmondson. Y sylfaen ymchwil ar gyfer diwylliant di-fai a'r diogelwch sy'n gwneud dysgu o fethiant yn bosibl.
- **Thinking, Fast and Slow**. Daniel Kahneman. Yr adroddiad diffiniol o duedd wybyddol, hanfodol ar gyfer cyfweliadau strwythuredig, calibradu, a gwneud penderfyniadau gonest.

## Crefft Rhaglennu ac Ansawdd Cod

- **The Pragmatic Programmer: Your Journey to Mastery**. Andrew Hunt and David Thomas. Y catalog sylfaenol o arferion proffesiynol (DRY, uniongyrchedd, bwledi olrhain) sy'n diffinio ystyr crefftwaith.
- **Refactoring: Improving the Design of Existing Code**. Martin Fowler. Y catalog canonaidd o drawsffurfiadau sy'n cadw ymddygiad a disgyblaeth gwella cod parhaus, wedi'i gefnogi gan brofion.
- **Clean Code: A Handbook of Agile Software Craftsmanship**. Robert C. Martin. Safon a ddefnyddir yn eang (ac a drafodir) ar gyfer enwi, ffwythiannau, a darllenadwyedd sy'n llunio disgwyliadau adolygu llawer o dimau.
- **Code Complete**. Steve McConnell. Llawlyfr cynhwysfawr, wedi'i seilio ar dystiolaeth, o arferion adeiladu sy'n parhau'n llinell sylfaen drylwyr ar gyfer ansawdd rhaglennu.
- **Test-Driven Development: By Example**. Kent Beck. Y cyflwyniad gwreiddiol, ymarferol i'r cylch coch-gwyrdd-ailffactora a chynllunio profi'n gyntaf.
- **Working Effectively with Legacy Code**. Michael Feathers. Y pecyn cymorth diffiniol ar gyfer ychwanegu profion at god heb rai a'i newid yn ddiogel, ac yn anhepgor ar gyfer systemau hirhoedlog.
- **Growing Object-Oriented Software, Guided by Tests**. Steve Freeman and Nat Pryce. Arddangosiad wedi'i weithio o TDD tu allan i mewn, ffugio (mocking), ac esblygu cynllun trwy brofion.
- **A Philosophy of Software Design**. John Ousterhout. Triniaeth finiog, farnol o gymhlethdod, modiwlau dwfn, a chuddio gwybodaeth sy'n herio rhai o uniongrededd "clean code" mewn modd cynhyrchiol.

## Pensaernïaeth a Systemau

- **Designing Data-Intensive Applications**. Martin Kleppmann. Y cyfeirlyfr modern gorau un ar gyfaddawdau storio, dyblygu, rhaniad, cysondeb, a phrosesu ffrydiau ar raddfa fawr.
- **Fundamentals of Software Architecture: An Engineering Approach**. Mark Richards and Neal Ford. Arolwg eang, cyfredol o arddulliau pensaernïol, nodweddion, a rôl a gwneud penderfyniadau'r pensaer.
- **Software Architecture: The Hard Parts**. Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani. Triniaeth wedi'i seilio ar benderfyniadau o gyfaddawdau pensaernïaeth ddosranedig, gronigrwydd gwasanaethau, a pherchnogaeth data.
- **Building Evolutionary Architectures**. Neal Ford, Rebecca Parsons, Patrick Kua. Yn cyflwyno ffwythiannau ffitrwydd a phensaernïaeth wedi'i chynllunio i newid yn ddiogel dros amser.
- **Domain-Driven Design: Tackling Complexity in the Heart of Software**. Eric Evans. Tarddiad cyd-destunau ffiniedig, iaith hollbresennol, a chyfuniadau (aggregates): geirfa cynllunio gwasanaethau modern.
- **Building Microservices: Designing Fine-Grained Systems**. Sam Newman. Y cyfeirlyfr ar gyfer dadelfennu, ffiniau gwasanaethau, defnyddio, ac oblygiadau sefydliadol microwasanaethau.
- **Monolith to Microservices**. Sam Newman. Catalog patrymau ar gyfer dadelfennu cynyddrannol, fel strangler fig a branch by abstraction, heb ailysgrifennu mawr, peryglus, ar unwaith.
- **Patterns of Enterprise Application Architecture**. Martin Fowler. Y cyfeirlyfr patrymau enwedig (repository, unit of work, a mwy) a roddodd iaith gyffredin i systemau menter.
- **Enterprise Integration Patterns**. Gregor Hohpe and Bobby Woolf. Y catalog diffiniol o batrymau negeseua sy'n sail i bensaernïaeth wedi'i llywio gan ddigwyddiadau ac anghydamserol.
- **Release It! Design and Deploy Production-Ready Software**. Michael T. Nygard. Ffynhonnell y torrwr cylched (circuit breaker), y bylchfur (bulkhead), a phatrymau sefydlogrwydd eraill ar gyfer systemau sy'n goroesi cynhyrchu go iawn.
- **Design Patterns: Elements of Reusable Object-Oriented Software**. Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides ("Gang of Four"). Y catalog hanesyddol allweddol o batrymau gwrthrych-gyfeiriedig a geirfa cynllunio gyffredin.

## Diogelwch, Preifatrwydd, ac Ymddiriedaeth

- **Threat Modeling: Designing for Security**. Adam Shostack. Y canllaw ymarferol, cynhwysfawr i STRIDE a modelu bygythiadau strwythuredig fel arfer beirianneg rheolaidd.
- **Security Engineering: A Guide to Building Dependable Distributed Systems**. Ross Anderson. Y cyfeirlyfr gwyddoniadurol ar sut mae systemau go iawn yn methu a sut i adeiladu rhai sy'n gwrthsefyll ymosodiad.
- **The Tangled Web: A Guide to Securing Modern Web Applications**. Michal Zalewski. Taith drylwyr trwy fodel diogelwch porwyr a'r ffyrdd cynnil y mae platfformau gwe'n bradychu tybiaethau naïf.
- **Cryptography Engineering**. Niels Ferguson, Bruce Schneier, Tadayoshi Kohno. Canllaw ymarferwr i ddefnyddio cryptograffeg yn gywir ac osgoi'r camgymeriadau cyffredin, peryglus.
- **Building Secure and Reliable Systems**. Heather Adkins et al. (Google). Cyfuniad Google o ddiogelwch a dibynadwyedd fel priodweddau cydblethedig wedi'u cynllunio i mewn o'r cychwyn.
- **Zero Trust Networks**. Evan Gilman and Doug Barth. Triniaeth glir o egwyddorion a mecanwaith pensaernïaeth rhwydwaith byth-ymddiried, gwirio-bob-amser.
- **OWASP Top 10**. OWASP Foundation. Y llinell sylfaen consensws o'r risgiau diogelwch cymhwysiadau gwe mwyaf critigol, y cyfeirir ati gan bolisi ac archwiliad ledled y byd.
- **OWASP Application Security Verification Standard (ASVS)**. OWASP Foundation. Rhestr wirio raddedig, brofadwy o ofynion diogelwch sy'n addas ar gyfer contractau a meini prawf derbyn.
- **NIST SP 800-53: Security and Privacy Controls for Information Systems and Organizations**. NIST. Y catalog rheolaethau wrth wraidd diogelwch ffederal UDA a sylfaen awdurdodi FedRAMP a FISMA.
- **NIST Cybersecurity Framework (CSF)**. NIST. Y strwythur adnabod-diogelu-canfod-ymateb-adfer a fabwysiadwyd yn eang ar gyfer trefnu rhaglen diogelwch.
- **NIST SP 800-207: Zero Trust Architecture**. NIST. Y diffiniad cyfeirio a'r pensaernïaethau cyfeirio sy'n angori'r rhan fwyaf o raglenni ymddiried-sero menter a llywodraeth.

## UX, UI, a Chynllunio Cynnyrch

- **The Design of Everyday Things**. Don Norman. Y testun sylfaenol ar gynigiadau (affordances), arwyddyddion, adborth, a chynllunio dynol-ganolog sy'n berthnasol ymhell y tu hwnt i wrthrychau ffisegol.
- **Don't Make Me Think, Revisited**. Steve Krug. Y ddadl gryno, barhaus dros ddefnyddioldeb hunan-amlwg a gwerth profi defnyddioldeb rhad, aml.
- **About Face: The Essentials of Interaction Design**. Alan Cooper, Robert Reimann, David Cronin. Y cyfeirlyfr cynhwysfawr ar gynllunio rhyngweithio, personas, a chynllunio wedi'i gyfeirio at nod.
- **Design Systems: A Practical Guide**. Alla Kholmatova. Adroddiad wedi'i seilio ar dystiolaeth o adeiladu systemau cydrannau cyson, ailddefnyddiadwy a'r iaith gyffredin y tu ôl iddynt.
- **Refactoring UI**. Adam Wathan and Steve Schoger. Canllaw ymarferol, wedi'i lywio gan enghreifftiau, i loywder gweledol ar gyfer peirianwyr sy'n cynllunio rhyngwynebau heb hyfforddiant ffurfiol.
- **Letting Go of the Words: Writing Web Content that Works**. Ginny Redish. Y canllaw diffiniol i gynllunio cynnwys mewn iaith blaen, wedi'i ganolbwyntio ar dasgau.
- **Inclusive Design Patterns / Accessibility for Everyone**. Heydon Pickering; Laura Kalbag. Cydymeithion ymarferol ar gyfer adeiladu rhyngwynebau sy'n gweithio ar gyfer yr ystod lawn o alluoedd dynol.
- **A Web for Everyone: Designing Accessible User Experiences**. Sarah Horton and Whitney Quesenbery. Pont wedi'i llywio gan egwyddorion rhwng safonau hygyrchedd a phrofiad defnyddiwr da.
- **Web Content Accessibility Guidelines (WCAG) 2.2**. W3C. Y safon y cyfeirir ati'n rhyngwladol (canfyddadwy, gweithredadwy, dealladwy, gadarn) y tu ôl i'r rhan fwyaf o gyfraith hygyrchedd.
- **U.S. Web Design System (USWDS)**. U.S. government. Enghraifft weithredol o system gynllunio hygyrch, wedi'i seilio ar safonau, wedi'i hadeiladu ar gyfer gwasanaethau cyhoeddus ar raddfa fawr.

## Deallusrwydd Artiffisial a Dysgu Peiriant

- **Designing Machine Learning Systems**. Chip Huyen. Y canllaw ymarferol blaenllaw i adeiladu systemau ML cynhyrchu o'r dechrau i'r diwedd: data, nodweddion, defnyddio, a monitro.
- **Reliable Machine Learning: Applying SRE Principles to ML in Production**. Cathy Chen et al. Yn ymestyn disgyblaeth SRE (SLOs, monitro, ymateb i ddigwyddiadau) i systemau dysgu peiriant.
- **Deep Learning**. Ian Goodfellow, Yoshua Bengio, Aaron Courville. Y cyfeirlyfr academaidd safonol ar gyfer y ddamcaniaeth a'r dulliau sy'n sail i rwydweithiau niwral modern.
- **AI Engineering: Building Applications with Foundation Models**. Chip Huyen. Canllaw cyfredol i gynllunio, gwerthuso, a gweithredu cymwysiadau wedi'u hadeiladu ar fodelau sylfaen mawr.
- **Weapons of Math Destruction**. Cathy O'Neil. Achos byw dros atebolrwydd algorithmig a niweidiau byd go iawn modelau heb eu harchwilio, hanfodol ar gyfer AI sector cyhoeddus.
- **Interpretable Machine Learning**. Christoph Molnar. Cyfeirlyfr cynhwysfawr, ar gael am ddim, ar ddulliau esboniadwyedd ar gyfer modelau a'u rhagfynegiadau.
- **NIST AI Risk Management Framework (AI RMF 1.0)**. NIST. Y fframwaith cyfeirio ar gyfer llywodraethu, mapio, mesur, a rheoli risg AI, y cyfeirir ato fwyfwy mewn polisi a chaffael.

## Data, Dadansoddeg, a Mewnwelediad

- **The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling**. Ralph Kimball and Margy Ross. Y cyfeirlyfr canonaidd ar sgemâu seren a modelu dimensiynol ar gyfer dadansoddeg.
- **Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing**. Ron Kohavi, Diane Tang, Ya Xu. Y canllaw awdurdodol i redeg arbrofion sy'n rhoi canlyniadau dibynadwy, gweithredadwy ar raddfa fawr.
- **Fundamentals of Data Engineering**. Joe Reis and Matt Housley. Map niwtral o ran gwerthwr o gylch bywyd data modern a'r arferion peirianneg y tu ôl iddo.
- **Data Mesh: Delivering Data-Driven Value at Scale**. Zhamak Dehghani. Y testun sefydlu ar gyfer y dull wedi'i seilio ar barth, cynnyrch-ganolog o drefnu data ar raddfa fawr.
- **Storytelling with Data**. Cole Nussbaumer Knaflic. Canllaw ymarferol i weledoli data gonest, clir a chyfathrebu mewnwelediad i wneuthurwyr penderfyniadau.
- **The Visual Display of Quantitative Information**. Edward R. Tufte. Y gwaith sylfaenol ar gywirdeb graffigol, inc-data, a moeseg dangos data'n onest.
- **DAMA-DMBOK: Data Management Body of Knowledge**. DAMA International. Y fframwaith cyfeirio cynhwysfawr ar gyfer llywodraethu data, stiwardiaeth, ansawdd, a chatalogio.
- **The Book of Why**. Judea Pearl and Dana Mackenzie. Cyflwyniad darllenadwy i gasgliad achosol, hanfodol ar gyfer symud o gydberthynas i benderfyniadau amddiffynadwy.

## Awtomeiddio, DevOps, a Pheirianneg Platfform

- **The DevOps Handbook**. Gene Kim, Jez Humble, Patrick Debois, John Willis. Y llyfr chwarae cynhwysfawr sy'n trosi'r "Tair Ffordd" yn arferion diriaethol ar gyfer llif, adborth, a dysgu parhaus.
- **Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation**. Jez Humble and David Farley. Y testun sylfaenol ar biblinellau defnyddio, awtomeiddio, a rhyddhau meddalwedd yn ddiogel ac yn aml.
- **Infrastructure as Code: Managing Servers in the Cloud**. Kief Morris. Y cyfeirlyfr ar drin seilwaith fel meddalwedd: modiwlau, profi, anghyfnewidioldeb, a llithriad.
- **Team Topologies**. Matthew Skelton and Manuel Pais. (Gweler Sylfeini.) Hefyd yn hanfodol yma ar gyfer llunio timau platfform a'r profiad datblygwr y maent yn ei ddarparu.
- **Kubernetes Patterns**. Bilgin Ibryam and Roland Huß. Catalog o batrymau ailddefnyddiadwy ar gyfer cynllunio cymwysiadau brodorol i'r cwmwl ar Kubernetes.
- **Software Engineering at Google**. Titus Winters, Tom Manshreck, Hyrum Wright. Sut mae arferion peirianneg fel profi, adolygu, offer, a rheoli dibyniaethau'n graddio i ddegau o filoedd o beirianwyr dros ddegawdau.
- **The Twelve-Factor App**. Adam Wiggins (Heroku). Y maniffesto cryno, dylanwadol ar gyfer adeiladu gwasanaethau cludadwy, graddadwy, brodorol i'r cwmwl.
- **DORA State of DevOps Report**. DORA / Google Cloud (annual). Y rhaglen ymchwil barhaus y tu ôl i'r pedwar metrig cyflenwi allweddol a'r galluoedd sy'n gyrru perfformiad.

## Gweithrediadau, Dibynadwyedd, ac Arsylwadwyedd

- **Site Reliability Engineering: How Google Runs Production Systems**. Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.). Y testun sylfaenol sy'n diffinio SLIs, SLOs, cyllidebau gwallau, a disgyblaeth peirianneg dibynadwyedd.
- **The Site Reliability Workbook**. Betsy Beyer et al. (eds.). Y cydymaith ymarferol gydag enghreifftiau ymarferol, SLOs wedi'u gweithio, a chanllawiau gweithredu.
- **Observability Engineering**. Charity Majors, Liz Fong-Jones, George Miranda. Y diffiniad modern o arsylwadwyedd, data cardinolrwydd uchel, a datnamu anhysbys-anhysbysion mewn cynhyrchu.
- **Implementing Service Level Objectives**. Alex Hidalgo. Canllaw trylwyr, ymarferol i gynllunio, mesur, a defnyddio SLOs a chyllidebau gwallau'n dda.
- **Release It!**. Michael T. Nygard. (Gweler Pensaernïaeth.) Hefyd yn sylfaenol yma ar gyfer patrymau sefydlogrwydd cynhyrchu a gweithredu systemau gwydn.
- **The Art of Capacity Planning**. Arun Kejariwal and John Allspaw. Dull wedi'i lywio gan ddata i ragweld galw a chynllunio capasiti ar gyfer systemau sy'n tyfu.
- **Chaos Engineering: System Resiliency in Practice**. Casey Rosenthal and Nora Jones. Y driniaeth ddiffiniol o chwistrellu methiant yn fwriadol i adeiladu hyder yng ngwydnwch system.
- **Google SRE Book, Chapter on Postmortems**. Google. Y model a efelychir yn eang ar gyfer post-mortemau di-fai a dysgu o ddigwyddiadau.

## Menter, Llywodraeth, a Budd y Cyhoedd

- **Working in Public: The Making and Maintenance of Open Source Software**. Nadia Eghbal. Yr astudiaeth hanfodol o sut mae cod agored yn cael ei gynnal mewn gwirionedd, a baich cynhalwyr y tu ôl i'r dibyniaethau y mae mentrau'n dibynnu arnynt.
- **Recoding America: Why Government Is Failing in the Digital Age and How We Can Do Better**. Jennifer Pahlka. Adroddiad clir o pam mae technoleg sector cyhoeddus yn methu a sut y gall diwygio wedi'i ganolbwyntio ar gyflenwi ei drwsio.
- **Digital Transformation at Scale: Why the Strategy Is Delivery**. Andrew Greenway et al. Gwersi o Wasanaeth Digidol Llywodraeth y DU ar drawsnewid gwasanaethau cyhoeddus trwy gyflenwi, nid cynllunio.
- **Project to Product**. Mik Kersten. Y Fframwaith Llif ar gyfer symud mentrau mawr o gyllid seiliedig ar brosiectau i ffrydiau gwerth cynnyrch parhaol.
- **Escaping the Build Trap**. Melissa Perri. Sut mae sefydliadau'n camgymryd allbwn am ganlyniad, a sut mae rheolaeth cynnyrch yn ei drwsio, gyda pherthnasedd uniongyrchol i lywodraethu portffolio a rhaglenni.
- **U.S. Digital Services Playbook**. U.S. Digital Service. Set gryno o chwaraeon ar gyfer cyflenwi gwasanaethau digidol llywodraeth effeithiol, defnyddiwr-ganolog.
- **GOV.UK Service Manual and Service Standard**. UK Government Digital Service. Safon weithredol, gyhoeddedig ar gyfer adeiladu gwasanaethau cyhoeddus da, a efelychir yn eang gan lywodraethau eraill.
- **NIST SP 800-37: Risk Management Framework**. NIST. Y fframwaith proses y tu ôl i awdurdodi i weithredu (ATO) a monitro parhaus mewn systemau ffederal UDA.
- **The FinOps Foundation Framework**. FinOps Foundation. Y model cyfeirio ar gyfer gwelededd cost cwmwl, optimeiddio, ac atebolrwydd ar draws cyllid a pheirianneg.

## Sut i ddefnyddio'r rhestr hon

- **Dechreuwch gyda'ch poen.** Os yw defnyddio'n araf ac yn frawychus, darllenwch *Accelerate*, *Continuous Delivery*, ac adroddiadau *DORA* cyn unrhyw beth arall.
- **Darllenwch ar gyfer y degawd, nid y sbrint.** Ffafriwch y gweithiau sy'n esbonio egwyddorion parhaus dros y rhai sydd wedi'u clymu i fersiwn teclyn penodol.
- **Cadarnhewch rifyn cyfredol safonau.** Mae NIST, OWASP, WCAG, ISO, a DORA yn adolygu eu cyhoeddiadau; gweithiwch bob amser o'r rhyddhad diweddaraf a nodwch y fersiwn yn eich polisïau eich hun.
- **Adeiladwch silff gyffredin.** Mae tîm sydd wedi darllen dau neu dri o'r llyfrau hyn yn gyffredin yn dadlau llai ac yn penderfynu'n gyflymach, oherwydd ei fod yn rhannu geirfa a set o bwyntiau cyfeirio.
- **Gweler hefyd bennod 12.5** am y mynegai llawn o safonau a fframweithiau cyfeirio, a **phennod 12.6** am sut i drefnu dilyniant mabwysiadu'r arferion y mae'r gweithiau hyn yn eu disgrifio.
