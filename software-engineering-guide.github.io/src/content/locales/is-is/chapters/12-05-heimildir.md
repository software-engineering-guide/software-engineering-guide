# 12.5 Heimildir

Þessi hluti tekur saman tilvísunarbúnað handbókarinnar: samsvörunartöflu við SWEBOK
þekkingargrunninn, skrá yfir staðla og rammaverk sem vísað er til um alla bókina
og sérvalda heimildaskrá með ráðlögðum lestri. Heimildir fyrir hvern kafla
birtast einnig í hlutanum *Heimildir og frekari lestur* aftast í hverjum kafla.

---

# SWEBOK samsvörunartafla

Þessi handbók er samstillt **SWEBOK V4.0** frá IEEE Computer Society (Software
Engineering Body of Knowledge). Öll 18 þekkingarsviðin eru þakin. Taflan varpar
hverju á kaflana sem fjalla um það og handbókin fer síðan langt út fyrir SWEBOK
í gervigreind, gögn, notendaupplifun, DevOps, sjálfbærni, flæði og almannahagstækni.

| SWEBOK V4.0 þekkingarsvið | Aðalkaflar |
|---|---|
| 1. Software Requirements | 2.8, 11.1, 5.1 |
| 2. Software Architecture | 3.1, 3.2, 3.3 |
| 3. Software Design | 2.2, 3.1 |
| 4. Software Construction | 2.9, 2.1 |
| 5. Software Testing | 2.4, 8.5 |
| 6. Software Engineering Operations | 9.1, 9.2, 9.3, 8.1 |
| 7. Software Maintenance | 3.7, 3.6, 10.4 |
| 8. Software Configuration Management | 2.10, 2.6, 8.2 |
| 9. Software Engineering Management | 10.1, 10.6, 10.2 |
| 10. Software Engineering Process | 1.4, 10.7, 10.8 |
| 11. Software Engineering Models and Methods | 2.12, 3.1, 2.2 |
| 12. Software Quality | 2.11, 2.4, 3.1 |
| 13. Software Security | 4.1, 4.2, 4.3, 4.4 |
| 14. Software Engineering Professional Practice | 10.5, 1.1, 1.3 |
| 15. Software Engineering Economics | 10.10, 10.1, 9.4 |
| 16. Computing Foundations | 2.13, 3.3, 3.4 |
| 17. Mathematical Foundations | 2.13, 11.3 |
| 18. Engineering Foundations | 2.13, 3.1 |

---

# Staðlar og rammaverk

Þessi viðauki er skipulögð skrá yfir raunverulega staðla, rammaverk og
reglugerðir sem vísað er til um alla handbókina. Hún er leiðsögutæki, ekki
reglufylgnihandbók: leitaðu alltaf til yfirvaldsheimildarinnar og, þar sem við á,
hæfra lögfræði- eða úttektarráðgjafa fyrir gildandi texta og hvernig hann á við
í samhengi þínu.

Færslum er skipt í flokka eftir sviðum. Hver færsla nefnir staðalinn eða rammaverkið,
útgáfuaðilann, eina línu um umfang og kaflana eða sviðin þar sem hann á mest
við. Þar sem nafn er almennt stytt er skammstöfunin sýnd. Skjalanúmer og
titlar eru aðeins gefin þar sem þau eru vel rótgróin. Engir tenglar eru með.

## Hvernig á að nota þennan viðauka

- **Reglugerðir** (til dæmis GDPR, HIPAA) eru lagalega bindandi innan lögsögu
  sinnar og geira. Þær setja skyldur, ekki bara góða venju.
- **Staðlar** (til dæmis ISO/IEC 27001, WCAG) eru formlegar, oft vottanlegar
  forskriftir. Sumir eru valkvæðir. Sumir eru skyldaðir með lögum eða samningi.
- **Rammaverk** (til dæmis NIST CSF, NIST AI RMF) eru skipulögð, yfirleitt
  valkvæð leiðsögn sem þú sníðir að áhættusniði þínu.
- Gildissvið veltur á lögsögu, geira, gagnagerðum og samningsskilmálum. Margar
  skipulagsheildir verða að uppfylla nokkra þessara samtímis.

## Öryggi og persónuvernd

| Staðall / rammaverk | Útgefandi | Umfang (ein lína) | Aðalkaflar / svið |
| --- | --- | --- | --- |
| ISO/IEC 27001 | ISO / IEC | Kröfur fyrir upplýsingaöryggisstjórnunarkerfi (ISMS). | 4.1–4.6 Öryggi og reglufylgni |
| ISO/IEC 27002 | ISO / IEC | Leiðsögn og stýringasafn sem styður ISO/IEC 27001. | 4.1–4.4 Öryggi |
| ISO/IEC 27017 / 27018 | ISO / IEC | Skýjasértækar öryggisstýringar (27017) og vernd persónugreinanlegra upplýsinga í skýinu (27018). | 4.3 Innviða- og skýjaöryggi. 4.5 Persónuvernd |
| NIST Cybersecurity Framework (CSF) | National Institute of Standards and Technology | Valkvætt rammaverk skipulagt í kringum Govern, Identify, Protect, Detect, Respond, Recover. | 4.1, 4.4 Öryggisgrunnur og rekstur |
| NIST SP 800-53 | National Institute of Standards and Technology | Skrá yfir öryggis- og persónuverndarstýringar fyrir upplýsingakerfi. | 4.3, 4.6 Skýjaöryggi og reglufylgni |
| NIST SP 800-63 | National Institute of Standards and Technology | Leiðbeiningar um stafræn auðkenni og tryggingu auðkenningar. | 4.2, 4.3 Forrita- og innviðaöryggi |
| OWASP Top Ten | Open Worldwide Application Security Project | Mikilvægustu öryggisáhættur vefforrita, uppfærðar reglulega. | 4.2 Forritaöryggi |
| OWASP ASVS | Open Worldwide Application Security Project | Flokkaðar kröfur og prófanir til að staðfesta forritaöryggi. | 2.4, 4.2 Prófanir og forritaöryggi |
| OWASP SAMM | Open Worldwide Application Security Project | Þroskalíkan til að smíða og meta hugbúnaðaröryggisáætlun. | 4.1 Öryggisgrunnur og menning |
| STRIDE | Upprunnið hjá Microsoft | Ógnarlíkanaflokkun til að flokka ógnir. | 4.2 Forritaöryggi |
| MITRE ATT&CK | MITRE | Þekkingargrunnur um taktík og tækni andstæðinga fyrir greiningu og vörn. | 4.4 Öryggisrekstur |
| SLSA | Open Source Security Foundation (OpenSSF) | Stigskipt rammaverk fyrir heilleika og uppruna hugbúnaðaraðfangakeðju. | 4.2, 8.1, 10.3 Aðfangakeðja og afhending |
| SBOM (SPDX / CycloneDX) | Linux Foundation (SPDX). OWASP (CycloneDX) | Staðalsnið fyrir hugbúnaðarefnisskrár. | 4.2, 10.3 Forritaöryggi og leyfi |
| PCI DSS | PCI Security Standards Council | Öryggiskröfur fyrir meðhöndlun greiðslukortagagna. | 4.2, 4.5, 4.6 Öryggi, persónuvernd, reglufylgni |

## Reglufylgni og hið opinbera

### Bandaríkin

| Reglugerð / rammaverk | Útgefandi | Umfang (ein lína) | Aðalkaflar / svið |
| --- | --- | --- | --- |
| HIPAA | US Dept. of Health and Human Services | Verndarráðstafanir fyrir verndaðar heilbrigðisupplýsingar (PHI). | 4.5, 4.6 Persónuvernd og reglufylgni |
| SOX (Sarbanes-Oxley Act) | US Congress / SEC | Kröfur um fjárhagsskýrslugjöf og innri stýringar fyrir opinber fyrirtæki. | 4.6, 10.2 Reglufylgni og úttekt |
| FISMA | US Congress | Kröfur um upplýsingaöryggisáætlanir fyrir alríkisstofnanir. | 4.3, 4.6 Skýjaöryggi og reglufylgni |
| FedRAMP | US General Services Administration / FedRAMP PMO | Staðlað öryggisheimildarveiting fyrir skýjaþjónustur notaðar af alríkisstofnunum. | 4.3, 4.6 Skýjaöryggi og reglufylgni |
| NIST SP 800-171 | National Institute of Standards and Technology | Vernd stýrðra óleynilegra upplýsinga (CUI) í kerfum utan alríkis. | 4.6 Reglufylgni (aðfangakeðja varnarmála) |
| CMMC | US Department of Defence | Vottun netöryggisþroska varnarmálaverktaka. | 4.6 Reglufylgni (varnarmál) |
| FIPS 140-3 | National Institute of Standards and Technology | Öryggiskröfur fyrir dulritunareiningar. | 4.3 Innviða- og skýjaöryggi |
| CCPA / CPRA | State of California | Persónuverndarréttindi neytenda og skyldur fyrirtækja í Kaliforníu. | 4.5 Persónuvernd og gagnavernd |

### Evrópusambandið og Bretland

| Reglugerð / staðall | Útgefandi | Umfang (ein lína) | Aðalkaflar / svið |
| --- | --- | --- | --- |
| GDPR | European Union | Víðtæk reglugerð um vinnslu persónuupplýsinga. | 4.5, 4.6 Persónuvernd og reglufylgni |
| UK GDPR / Data Protection Act 2018 | United Kingdom | Gagnaverndarkerfi Bretlands eftir Brexit. | 4.5, 4.6 Persónuvernd og reglufylgni |
| eIDAS | European Union | Rammi fyrir rafræn auðkenni og traustþjónustur. | 4.2, 4.3 Öryggi |
| NIS2 Directive | European Union | Netöryggisskyldur fyrir nauðsynlega og mikilvæga aðila. | 4.4, 4.6 Öryggisrekstur og reglufylgni |
| DORA (Digital Operational Resilience Act) | European Union | Kröfur um rekstrarseiglu fyrir fjármálageirann. | 9.1, 10.2 Áreiðanleiki og úttekt |
| EU AI Act | European Union | Áhættubyggð reglugerð gervigreindarkerfa (sjá gervigreindarstjórnarhætti hér að neðan). | 6.1, 6.5 Gervigreindarstefna og ábyrg gervigreind |

## Aðgengi

| Staðall | Útgefandi | Umfang (ein lína) | Aðalkaflar / svið |
| --- | --- | --- | --- |
| WCAG (2.1 / 2.2) | World Wide Web Consortium (W3C) | Leiðbeiningar um aðgengilegt vefefni, með A/AA/AAA samræmisstigum. | 5.3 Aðgengi. 5.1–5.6 UX og framendi |
| WAI-ARIA | World Wide Web Consortium (W3C) | Hlutverk, ástönd og eiginleikar fyrir aðgengileg rík internetforrit. | 5.3, 5.6 Aðgengi og framendi |
| Section 508 | US Access Board / US federal law | Aðgengiskröfur fyrir bandaríska alríkis-upplýsingatækni, samstilltar WCAG. | 5.3 Aðgengi (bandarísk stjórnvöld) |
| EN 301 549 | ETSI / CEN / CENELEC | Evrópskar aðgengiskröfur fyrir upplýsingatækniinnkaup, samstilltar WCAG. | 5.3 Aðgengi (opinber geiri ESB) |
| ADA (Americans with Disabilities Act) | US Congress | Mannréttindalög sem banna mismunun vegna fötlunar, beitt á stafrænar þjónustur. | 5.3 Aðgengi |
| ISO/IEC 40500 | ISO / IEC | Alþjóðleg upptaka WCAG 2.0 sem formlegs staðals. | 5.3 Aðgengi |

## Gervigreindarstjórnarhættir

| Rammaverk / reglugerð | Útgefandi | Umfang (ein lína) | Aðalkaflar / svið |
| --- | --- | --- | --- |
| NIST AI Risk Management Framework (AI RMF) | National Institute of Standards and Technology | Valkvætt rammaverk til að stýra, kortleggja, mæla og stjórna gervigreindaráhættu. | 6.1, 6.5 Gervigreindarstefna og ábyrg gervigreind |
| ISO/IEC 42001 | ISO / IEC | Kröfur fyrir gervigreindarstjórnunarkerfi (AIMS). | 6.1, 6.5 Gervigreindarstjórnarhættir |
| ISO/IEC 23894 | ISO / IEC | Leiðsögn um gervigreindarsértæka áhættustjórnun. | 6.5 Ábyrg og áreiðanleg gervigreind |
| EU AI Act | European Union | Áhættuflokkaðar lagaskyldur fyrir veitendur og útsetjendur gervigreindarkerfa. | 6.1, 6.3, 6.5 Gervigreindarforrit og stjórnarhættir |
| OECD AI Principles | Organisation for Economic Co-operation and Development | Gildamiðaðar meginreglur um áreiðanlega gervigreind, áhrifamiklar á stefnumótun. | 6.5, 10.5 Ábyrg gervigreind og siðfræði |

## Gæði og ferli

| Staðall / rammaverk | Útgefandi | Umfang (ein lína) | Aðalkaflar / svið |
| --- | --- | --- | --- |
| ISO/IEC 25010 | ISO / IEC | Gæðalíkan hugbúnaðarvöru (virknihæfi, áreiðanleiki, öryggi o.s.frv.). | 2.2, 2.4 Hönnun og prófanir |
| ISO/IEC/IEEE 12207 | ISO / IEC / IEEE | Lífsferlisferli hugbúnaðar. | 1.4, 10.1 Vinnulag og áætlanastjórnun |
| ISO 9001 | ISO | Kröfur fyrir almennt gæðastjórnunarkerfi. | 10.2 Áhætta, úttekt og trygging |
| CMMI | ISACA / CMMI Institute | Þroskalíkan fyrir ferlagetu og umbætur. | 10.1, 10.2 Áætlanastjórnun og trygging |
| DORA metrics | DevOps Research and Assessment (Google Cloud) | Fjórir lykilafhendingarframmistöðumælikvarðar fyrir hugbúnaðarteymi. | 8.1, 8.4, 9.1 Afhending, vettvangur, áreiðanleiki |
| SPACE framework | Microsoft / GitHub researchers | Fjölvíddar líkan til að mæla framleiðni forritara. | 1.3, 8.4 Vöxtur og upplifun forritara |
| ITIL | AXELOS / PeopleCert | Rammaverk upplýsingatækniþjónustustjórnunarvenja. | 9.1, 9.3 Áreiðanleiki og atvikastjórnun |

## Arkitektúr

| Staðall / rammaverk | Útgefandi | Umfang (ein lína) | Aðalkaflar / svið |
| --- | --- | --- | --- |
| ISO/IEC/IEEE 42010 | ISO / IEC / IEEE | Staðall fyrir arkitektúrlýsingu og sjónarhorn. | 2.7, 3.1 Skjölun og undirstöðuatriði arkitektúrs |
| TOGAF | The Open Group | Fyrirtækjaarkitektúrrammaverk og þróunaraðferð. | 3.1, 10.1 Arkitektúr og eignasafnsstjórnun |
| C4 model | Samfélag (Simon Brown) | Fjögurra stiga nálgun til að sjóngera hugbúnaðararkitektúr. | 2.7, 3.1 Skjölun og arkitektúr |
| arc42 | Samfélag (Starke / Hruschka) | Sniðmát til að byggja upp arkitektúrskjölun. | 2.7, 3.1 Skjölun og arkitektúr |
| ADRs | Samfélagsvenja | Léttar skrár yfir mikilvægar arkitektúrákvarðanir. | 1.5, 2.7, 3.1 Ákvarðanataka og skjölun |

## Ský og DevOps

| Staðall / rammaverk | Útgefandi | Umfang (ein lína) | Aðalkaflar / svið |
| --- | --- | --- | --- |
| CIS Benchmarks | Centre for Internet Security | Samstöðubyggðar öruggar stillingargrunnlínur fyrir kerfi og ský. | 4.3, 8.2 Innviðaöryggi og IaC |
| CNCF landscape and projects | Cloud Native Computing Foundation | Vistkerfi og staðlar fyrir skýjabyggða tölvun (t.d. Kubernetes). | 8.3 Gámar og skýjabyggð |
| OCI (Open Container Initiative) | Open Container Initiative (Linux Foundation) | Opnir staðlar fyrir gámamyndir og keyrslusnið. | 8.3 Gámar og skýjabyggð |
| OpenTelemetry | Cloud Native Computing Foundation | Seljandahlutlaus staðall fyrir fjarmælingar (rakningar, mælikvarða, skrár). | 9.2 Sýnileiki og vöktun |
| Open Policy Agent (OPA) | Cloud Native Computing Foundation | Almenn stefnuvél fyrir stefnu-sem-kóða. | 4.6, 8.2, 8.3 Reglufylgni, IaC, stýring |
| SRE practices | Google (víða tekið upp) | SLI/SLO/villufjárhagsáætlunarbyggð nálgun til að reka áreiðanlegar þjónustur. | 9.1 Áreiðanleikaverkfræði |
| FinOps Framework | FinOps Foundation | Venjur fyrir fjármálastjórnun skýs og kostnaðarábyrgð. | 9.4 Kostnaður, sjálfbærni, grænn hugbúnaður |

## Gögn

| Staðall / rammaverk | Útgefandi | Umfang (ein lína) | Aðalkaflar / svið |
| --- | --- | --- | --- |
| DAMA-DMBOK | DAMA International | Þekkingargrunnur sem skipuleggur gagnastjórnunargreinar. | 7.1 Gagnastefna og stjórnarhættir |
| ISO/IEC 38505 | ISO / IEC | Stjórnarhættir gagna sem skipulagsheildareignar. | 7.1 Gagnastjórnarhættir |
| ISO 8000 | ISO | Gagnagæða- og stofngagnastaðlar. | 7.1, 7.2 Gagnastjórnarhættir og verkfræði |
| Data mesh | Samfélag (Zhamak Dehghani) | Valddreifð, lénsmiðuð nálgun að gögnum sem vöru. | 7.1, 7.2 Gagnastefna og verkfræði |
| DCAM | EDM Council | Getumatslíkan gagnastjórnunar. | 7.1 Gagnastefna og stjórnarhættir |

## Athugasemdir um umfang og breytingar

Staðlar og reglugerðir þróast. Útgáfunúmer (til dæmis WCAG 2.1 á móti 2.2, eða
ISO endurskoðunarár) og stýringaskrár breytast með tímanum og ný lög (eins og
geirasértækar gervigreindar- og seigluregluverk) halda áfram að koma fram.
Líttu á þennan viðauka sem upphafskort: staðfestu núverandi útgáfu, lögsögu og
gildissvið áður en þú reiðir þig á nokkra færslu fyrir reglufylgni- eða
innkaupaákvörðun. Þar sem kaflar handbókarinnar og þessi viðauki eru ólíkir í
smáatriðum ræður yfirvaldsheimildarskjalið alltaf.


---

# Ráðlagður lestur

Þessi viðauki er sérvalinn, athugasemdalegur lestrarlisti yfir öll svið
handbókarinnar. Hann kýs verk sem hafa mótað venjur í stærð: viðurkennd
sígild verk, ströng tilvísunarrit og staðla og skýrslur sem stór fyrirtæki,
teymi og ríkisstjórnir eru mæld gegn.

Hver færsla gefur titil og höfund(a), fylgt af einni setningu um hvers vegna hún
skiptir máli. Listinn er skipulagður undir tíu hlutum bókarinnar. Lestu
valkvætt: veldu tvö eða þrjú verk næst núverandi sársauka þínum, ekki alla
hilluna. Þar sem verk spannar svið er það sett þar sem það nýtist mest. Mörg
tilheyra nokkrum hlutum.

Athugasemd um staðla: stofnanir eins og NIST, OWASP, W3C/WCAG, ISO og DORA-
áætlunin gefa út lifandi skjöl sem eru endurskoðuð reglulega. Vísaðu í og lestu
núverandi útgáfu. Athugasemdirnar hér að neðan lýsa varanlegum tilgangi þeirra.

## Undirstöður: menning, fólk og ferli

- **Accelerate: The Science of Lean Software and DevOps**. Nicole Forsgren, Jez Humble, Gene Kim. Rannsóknagrunnurinn sem sýnir að afhendingarframmistaða spáir fyrir um frammistöðu skipulagsheildar og skilgreinir mælikvarðana (nú kallaða DORA) til að mæla hana.
- **The Phoenix Project**. Gene Kim, Kevin Behr, George Spafford. Viðskiptaskáldsaga sem gerir flæði, vinnu í gangi og „Þrjár leiðir“ DevOps auðskiljanleg fyrir leiðtoga og efasemdarmenn.
- **Team Topologies: Organising Business and Technology Teams for Fast Flow**. Matthew Skelton and Manuel Pais. Hagnýtur orðaforði (straumstillt, vettvangs-, aðstoðar- og flókin-undirkerfis teymi) til að hanna skipulagsheildir sem framleiða góðan hugbúnað.
- **An Elegant Puzzle: Systems of Engineering Management**. Will Larson. Reyndar rammar til að stærðarsetja teymi, stýra vexti skipulagsheildar og taka endurteknar ákvarðanir verkfræðiforystu.
- **Staff Engineer: Leadership Beyond the Management Track**. Will Larson. Skilgreinir staff-plús frumgerðirnar og tæknilegu forystuleiðina fyrir þá sem vilja áhrif án þess að verða stjórnendur.
- **The Manager's Path**. Camille Fournier. Stig fyrir stig leiðarvísir frá tæknistjóra til framkvæmdastjóra sem festir starfsferilsstiga og umskiptin í stjórnun.
- **The Staff Engineer's Path**. Tanya Reilly. Förunautur staff-plús bókmenntanna sem einbeitir sér að daglegri vinnu tæknilegrar forystu, áhrifa og stýringar án valds.
- **Peopleware: Productive Projects and Teams**. Tom DeMarco and Timothy Lister. Varanleg röksemd fyrir að meginvandamál hugbúnaðar séu félagsfræðileg, ekki tæknileg.
- **The Mythical Man-Month**. Frederick P. Brooks Jr. Upptök lögmáls Brooks og greinarmunarins á nauðsynlegri og tilviljanakenndri flækju sem enn stýrir mönnun og tímasetningu.
- **The Fearless Organisation: Creating Psychological Safety in the Workplace**. Amy C. Edmondson. Rannsóknagrunnurinn fyrir menningu án sakbendingar og öryggið sem gerir nám af mistökum mögulegt.
- **Thinking, Fast and Slow**. Daniel Kahneman. Endanleg frásögn af hugrænni hlutdrægni, nauðsynleg fyrir skipulögð viðtöl, kvörðun og heiðarlega ákvarðanatöku.

## Forritunarhandverk og kóðagæði

- **The Pragmatic Programmer: Your Journey to Mastery**. Andrew Hunt and David Thomas. Grundvallarskrá faglegra venja (DRY, hornréttleiki, ljósspor) sem skilgreinir hvað handverk þýðir.
- **Refactoring: Improving the Design of Existing Code**. Martin Fowler. Viðurkennda skráin yfir hegðunarvarðveitandi umbreytingar og aga samfelldra, prófastuddra kóðabóta.
- **Clean Code: A Handbook of Agile Software Craftsmanship**. Robert C. Martin. Víða notaður (og umdeildur) staðall fyrir nafngift, föll og læsileika sem mótar væntingar margra teyma um rýni.
- **Code Complete**. Steve McConnell. Víðtæk, sönnunargagnavísandi handbók um smíðavenjur sem er enn ítarleg grunnlína fyrir forritunargæði.
- **Test-Driven Development: By Example**. Kent Beck. Upprunalega, hagnýta kynningin á rauður-grænn-endurbæta hringnum og prófa-fyrst hönnun.
- **Working Effectively with Legacy Code**. Michael Feathers. Endanlega verkfærasafnið til að bæta prófunum við og breyta á öruggan hátt kóða sem hefur engar, ómissandi fyrir langlíf kerfi.
- **Growing Object-Oriented Software, Guided by Tests**. Steve Freeman and Nat Pryce. Unnin sýnikennsla á utan-inn TDD, hermun og að þróa hönnun gegnum prófanir.
- **A Philosophy of Software Design**. John Ousterhout. Hvöss, ákveðin umfjöllun um flækju, djúpar einingar og upplýsingafelun sem véfengir á gagnlegan hátt hluta „clean code“ réttrúnaðarins.

## Arkitektúr og kerfi

- **Designing Data-Intensive Applications**. Martin Kleppmann. Besta einstaka nútímatilvísunin um málamiðlanir geymslu, afritunar, skiptingar, samræmis og straumvinnslu í stærð.
- **Fundamentals of Software Architecture: An Engineering Approach**. Mark Richards and Neal Ford. Víðtæk, núverandi könnun á arkitektúrstílum, eiginleikum og hlutverki og ákvarðanatöku arkitektsins.
- **Software Architecture: The Hard Parts**. Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani. Ákvörðunarmiðuð umfjöllun um málamiðlanir dreifðs arkitektúrs, þjónustukornastærð og gagnaeignarhald.
- **Building Evolutionary Architectures**. Neal Ford, Rebecca Parsons, Patrick Kua. Kynnir hæfnisföll og arkitektúr sem er hannaður til að breytast á öruggan hátt með tímanum.
- **Domain-Driven Design: Tackling Complexity in the Heart of Software**. Eric Evans. Upptök afmarkaðra samhengja, alltumlykjandi tungumáls og samstæðna: orðaforði nútíma þjónustuhönnunar.
- **Building Microservices: Designing Fine-Grained Systems**. Sam Newman. Tilvísunin fyrir sundurliðun, þjónustumörk, útsetningu og skipulagsafleiðingar örþjónusta.
- **Monolith to Microservices**. Sam Newman. Mynstraskrá fyrir stigvaxandi sundurliðun, svo sem köfnunarfíkju og grein-með-útdrætti, án áhættusams allt-í-einu endurskrifs.
- **Patterns of Enterprise Application Architecture**. Martin Fowler. Nefnda-mynsturstilvísunin (geymsla, vinnueining og fleira) sem gaf fyrirtækjakerfum sameiginlegt tungumál.
- **Enterprise Integration Patterns**. Gregor Hohpe and Bobby Woolf. Endanlega skráin yfir skilaboðamynstur sem undirstrika atburðadrifinn og ósamstilltan arkitektúr.
- **Release It! Design and Deploy Production-Ready Software**. Michael T. Nygard. Uppspretta rofans, skilrúmsins og annarra stöðugleikamynstra fyrir kerfi sem lifa af raunverulega framleiðslu.
- **Design Patterns: Elements of Reusable Object-Oriented Software**. Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides ("Gang of Four"). Sögulega afgerandi skráin yfir hlutbundin mynstur og sameiginlegur hönnunarorðaforði.

## Öryggi, persónuvernd og traust

- **Threat Modelling: Designing for Security**. Adam Shostack. Hagnýti, ítarlegi leiðarvísirinn um STRIDE og skipulagða ógnarlíkanagerð sem hefðbundna verkfræðivenju.
- **Security Engineering: A Guide to Building Dependable Distributed Systems**. Ross Anderson. Alfræðitilvísunin um hvernig raunveruleg kerfi bila og hvernig á að smíða þau sem standast árás.
- **The Tangled Web: A Guide to Securing Modern Web Applications**. Michal Zalewski. Ströng ferð um öryggislíkan vafrans og lúmsku leiðirnar sem vefvettvangar svíkja barnalegar forsendur.
- **Cryptography Engineering**. Niels Ferguson, Bruce Schneier, Tadayoshi Kohno. Leiðarvísir iðkenda um að nota dulritun rétt og forðast algeng, hættuleg mistök.
- **Building Secure and Reliable Systems**. Heather Adkins et al. (Google). Samsetning Google á öryggi og áreiðanleika sem samtvinnuðum eiginleikum hönnuðum inn frá upphafi.
- **Zero Trust Networks**. Evan Gilman and Doug Barth. Skýr umfjöllun um meginreglur og vélvirki treystu-aldrei-staðfestu-alltaf netarkitektúrs.
- **OWASP Top 10**. OWASP Foundation. Samstöðugrunnlínan yfir mikilvægustu öryggisáhættur vefforrita, vísað til í stefnu og úttekt um allan heim.
- **OWASP Application Security Verification Standard (ASVS)**. OWASP Foundation. Þrepaskiptur, prófanlegur gátlisti öryggiskrafna hentugur fyrir samninga og samþykktarviðmið.
- **NIST SP 800-53: Security and Privacy Controls for Information Systems and Organisations**. NIST. Stýringaskráin í hjarta bandarísks alríkisöryggis og grunnur FedRAMP- og FISMA-heimildarveitingar.
- **NIST Cybersecurity Framework (CSF)**. NIST. Víða tekna greina-verja-uppgötva-bregðast-endurheimta byggingin til að skipuleggja öryggisáætlun.
- **NIST SP 800-207: Zero Trust Architecture**. NIST. Viðmiðunarskilgreiningin og viðmiðunararkitektúrar sem festa flestar fyrirtækja- og opinberar zero-trust áætlanir.

## UX, UI og vöruhönnun

- **The Design of Everyday Things**. Don Norman. Undirstöðutextinn um notkunarvísbendingar, merki, endurgjöf og manneskjumiðaða hönnun sem á við langt umfram líkamlega hluti.
- **Don't Make Me Think, Revisited**. Steve Krug. Hnitmiðuð, varanleg röksemd fyrir sjálfsögðum nothæfi og gildi ódýrra, tíðra nothæfisprófana.
- **About Face: The Essentials of Interaction Design**. Alan Cooper, Robert Reimann, David Cronin. Ítarlega tilvísunin um gagnvirkni hönnun, persónur og markmiðadrifna hönnun.
- **Design Systems: A Practical Guide**. Alla Kholmatova. Jarðbundin frásögn af að smíða samræmd, endurnýtanleg íhlutakerfi og sameiginlega tungumálið á bak við þau.
- **Refactoring UI**. Adam Wathan and Steve Schoger. Hagnýtur, dæmadrifinn leiðarvísir að sjónrænni fágun fyrir verkfræðinga sem hanna viðmót án formlegrar þjálfunar.
- **Letting Go of the Words: Writing Web Content that Works**. Ginny Redish. Endanlegur leiðarvísir um einfalt mál, verkmiðaða efnishönnun.
- **Inclusive Design Patterns / Accessibility for Everyone**. Heydon Pickering. Laura Kalbag. Hagnýtir förunautar til að smíða viðmót sem virka fyrir allt svið mannlegrar getu.
- **A Web for Everyone: Designing Accessible User Experiences**. Sarah Horton and Whitney Quesenbery. Meginregludrifin brú milli aðgengisstaðla og góðrar notendaupplifunar.
- **Web Content Accessibility Guidelines (WCAG) 2.2**. W3C. Alþjóðlega vísaði staðallinn (skynjanlegt, nothæft, skiljanlegt, sterkt) á bak við flest aðgengislög.
- **U.S. Web Design System (USWDS)**. U.S. government. Virkt dæmi um aðgengilegt, staðlabyggt hönnunarkerfi smíðað fyrir opinbera þjónustu í stærð.

## Gervigreind og vélnám

- **Designing Machine Learning Systems**. Chip Huyen. Leiðandi hagnýti leiðarvísirinn að smíða framleiðsluvélnámskerfi frá enda til enda: gögn, eiginleikar, útsetning og vöktun.
- **Reliable Machine Learning: Applying SRE Principles to ML in Production**. Cathy Chen et al. Víkkar SRE-aga (SLO, vöktun, atvikaviðbrögð) yfir vélnámskerfi.
- **Deep Learning**. Ian Goodfellow, Yoshua Bengio, Aaron Courville. Fræðilega staðaltilvísunin fyrir kenninguna og aðferðirnar á bak við nútíma tauganet.
- **AI Engineering: Building Applications with Foundation Models**. Chip Huyen. Núverandi leiðarvísir til að hanna, meta og reka forrit smíðuð á stórum grunnlíkönum.
- **Weapons of Maths Destruction**. Cathy O'Neil. Lifandi rök fyrir reikniritaábyrgð og raunverulegum skaða órannsakaðra líkana, nauðsynleg fyrir gervigreind hins opinbera.
- **Interpretable Machine Learning**. Christoph Molnar. Ítarleg, frjálst aðgengileg tilvísun um skýringaraðferðir fyrir líkön og spár þeirra.
- **NIST AI Risk Management Framework (AI RMF 1.0)**. NIST. Viðmiðunarrammaverkið til að stýra, kortleggja, mæla og stjórna gervigreindaráhættu, í auknum mæli vísað til í stefnu og innkaupum.

## Gögn, greining og innsýn

- **The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modelling**. Ralph Kimball and Margy Ross. Viðurkennda tilvísunin um stjörnuskema og víddarlíkanagerð fyrir greiningar.
- **Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing**. Ron Kohavi, Diane Tang, Ya Xu. Yfirvalds leiðarvísirinn að keyra tilraunir sem skila áreiðanlegum, framkvæmanlegum niðurstöðum í stærð.
- **Fundamentals of Data Engineering**. Joe Reis and Matt Housley. Seljandahlutlaust kort af nútíma gagnalífsferlinum og verkfræðivenjunum á bak við hann.
- **Data Mesh: Delivering Data-Driven Value at Scale**. Zhamak Dehghani. Stofnunartextinn um lénsmiðaða, vörumiðaða nálgun að skipulagi gagna í stærð.
- **Storytelling with Data**. Cole Nussbaumer Knaflic. Hagnýtur leiðarvísir að heiðarlegri, skýrri gagnasýn og að miðla innsýn til ákvörðunaraðila.
- **The Visual Display of Quantitative Information**. Edward R. Tufte. Undirstöðuverkið um myndrænan heilleika, gagnableksnýtingu og siðfræði þess að sýna gögn heiðarlega.
- **DAMA-DMBOK: Data Management Body of Knowledge**. DAMA International. Ítarlega tilvísunarrammaverkið um gagnastjórnarhætti, ráðsmennsku, gæði og skráningu.
- **The Book of Why**. Judea Pearl and Dana Mackenzie. Læsileg kynning á orsakaályktun, lífsnauðsynleg til að færa sig frá fylgni að verjanlegum ákvörðunum.

## Sjálfvirkni, DevOps og vettvangsverkfræði

- **The DevOps Handbook**. Gene Kim, Jez Humble, Patrick Debois, John Willis. Ítarlega leikbókin sem þýðir „Þrjár leiðir“ í áþreifanlegar venjur fyrir flæði, endurgjöf og stöðugt nám.
- **Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation**. Jez Humble and David Farley. Undirstöðutextinn um útsetningarleiðslur, sjálfvirkni og að gefa út hugbúnað á öruggan og tíðan hátt.
- **Infrastructure as Code: Managing Servers in the Cloud**. Kief Morris. Tilvísunin um að líta á innviði sem hugbúnað: einingar, prófanir, óbreytanleika og rek.
- **Team Topologies**. Matthew Skelton and Manuel Pais. (Sjá Undirstöður.) Einnig nauðsynlegt hér til að móta vettvangsteymi og upplifunina sem þau veita forriturum.
- **Kubernetes Patterns**. Bilgin Ibryam and Roland Huß. Skrá yfir endurnýtanleg mynstur til að hanna skýjabyggð forrit á Kubernetes.
- **Software Engineering at Google**. Titus Winters, Tom Manshreck, Hyrum Wright. Hvernig verkfræðivenjur eins og prófanir, rýni, verkfæri og ósjálfstæðisstjórnun skalast í tugþúsundir verkfræðinga yfir áratugi.
- **The Twelve-Factor App**. Adam Wiggins (Heroku). Hnitmiðaða, áhrifamikla stefnuyfirlýsingin um að smíða flytjanlegar, skalanlegar, skýjabyggðar þjónustur.
- **DORA State of DevOps Report**. DORA / Google Cloud (árleg). Viðvarandi rannsóknaráætlunin á bak við fjóra lykilafhendingarmælikvarðana og getuna sem knýr frammistöðu.

## Rekstur, áreiðanleiki og sýnileiki

- **Site Reliability Engineering: How Google Runs Production Systems**. Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.). Undirstöðutextinn sem skilgreinir SLI, SLO, villufjárhagsáætlanir og agann að verkfræða áreiðanleika.
- **The Site Reliability Workbook**. Betsy Beyer et al. (eds.). Hagnýti förunauturinn með dæmum, unnum SLO og útfærsluleiðsögn.
- **Observability Engineering**. Charity Majors, Liz Fong-Jones, George Miranda. Nútímaskilgreiningin á sýnileika, háfjölda gögnum og að aflúsa óþekktum-óþekktu í framleiðslu.
- **Implementing Service Level Objectives**. Alex Hidalgo. Ítarlegur, hagnýtur leiðarvísir að hanna, mæla og nota SLO og villufjárhagsáætlanir vel.
- **Release It!**. Michael T. Nygard. (Sjá Arkitektúr.) Einnig grundvallaratriði hér fyrir framleiðslustöðugleikamynstur og að reka seigluð kerfi.
- **The Art of Capacity Planning**. Arun Kejariwal and John Allspaw. Gagnadrifin nálgun að spá fyrir um eftirspurn og skipuleggja afkastagetu fyrir vaxandi kerfi.
- **Chaos Engineering: System Resiliency in Practice**. Casey Rosenthal and Nora Jones. Endanlega umfjöllunin um að sprauta viljandi bilun til að byggja traust á kerfisseiglu.
- **Google SRE Book, Chapter on Postmortems**. Google. Víða hermt líkan fyrir eftirmálsrýni án sakbendingar og nám af atvikum.

## Fyrirtæki, hið opinbera og almannahagur

- **Working in Public: The Making and Maintenance of Open Source Software**. Nadia Eghbal. Nauðsynleg rannsókn á hvernig opinn hugbúnaður er í raun viðhaldinn og viðhaldsaðilabyrðin á bak við ósjálfstæðin sem fyrirtæki reiða sig á.
- **Recoding America: Why Government Is Failing in the Digital Age and How We Can Do Better**. Jennifer Pahlka. Hreinskilin frásögn af hvers vegna tækni hins opinbera bregst og hvernig afhendingarmiðaðar umbætur geta lagað það.
- **Digital Transformation at Scale: Why the Strategy Is Delivery**. Andrew Greenway et al. Lærdómur frá UK Government Digital Service um að umbreyta opinberri þjónustu með því að afhenda, ekki skipuleggja.
- **Project to Product**. Mik Kersten. Flow Framework til að færa stór fyrirtæki frá verkefnamiðaðri fjármögnun yfir í varanlega vöruverðmætastrauma.
- **Escaping the Build Trap**. Melissa Perri. Hvernig skipulagsheildir rugla afurð saman við niðurstöðu og hvernig vörustjórnun lagar það, með beina þýðingu fyrir stjórnarhætti safna og áætlana.
- **U.S. Digital Services Playbook**. U.S. Digital Service. Hnitmiðað safn leikja til að afhenda skilvirka, notendamiðaða stafræna þjónustu hins opinbera.
- **GOV.UK Service Manual and Service Standard**. UK Government Digital Service. Virkur, birtur staðall til að smíða góða opinbera þjónustu, víða hermdur af öðrum ríkisstjórnum.
- **NIST SP 800-37: Risk Management Framework**. NIST. Ferlarammaverkið á bak við heimild til reksturs (ATO) og samfellda vöktun í bandarískum alríkiskerfum.
- **The FinOps Foundation Framework**. FinOps Foundation. Viðmiðunarlíkanið fyrir skýjakostnaðarsýnileika, fínstillingu og ábyrgð yfir fjármál og verkfræði.

## Hvernig á að nota þennan lista

- **Byrjaðu á sársauka þínum.** Ef útsetningar eru hægar og ógnvekjandi skaltu lesa *Accelerate*, *Continuous Delivery* og *DORA* skýrslurnar fyrst.
- **Lestu fyrir áratuginn, ekki sprettinn.** Kjóstu verkin sem útskýra varanlegar meginreglur fram yfir þau sem eru bundin við tiltekna verkfæraútgáfu.
- **Staðfestu núverandi útgáfu staðla.** NIST, OWASP, WCAG, ISO og DORA endurskoða útgáfur sínar. Vinndu alltaf frá nýjustu útgáfu og skráðu útgáfuna í eigin stefnum.
- **Byggðu sameiginlega hillu.** Teymi sem hefur lesið tvær eða þrjár þessara bóka saman rökræðir minna og ákveður hraðar, því það deilir orðaforða og safni viðmiðunarpunkta.
- **Sjá einnig kafla 12.5** fyrir fulla skrá yfir viðmiðunarstaðla og rammaverk, og **kafla 12.6** um hvernig á að raða upptöku venjanna sem þessi verk lýsa.
