# 2.7 Skjölun

## Yfirlit og tilgangur

[Skjölun](https://en.wikipedia.org/wiki/Software_documentation) er skrifleg þekking sem lætur fólk nota, reka og breyta hugbúnaði án þess að þurfa að púsla skilningnum saman úr kóðanum einum. Hún kemur í mörgum tegundum: hvernig á að byrja, hvernig á að ljúka verkefni, hvernig kerfi er uppbyggt, hvernig á að bregðast við atviki, hvað [API](https://en.wikipedia.org/wiki/API) tekur við og skilar. Hver þjónar öðrum lesanda með aðra þörf. Góð skjölun er ekki valkvæð. Hún er munurinn á þekkingu sem skalar yfir stóra skipulagsheild og þekkingu sem lifir í höfðum fárra manna.

Fyrir stór teymi er skjölun besta vörn þín gegn lykilmannaáhættu (hættunni þegar mikilvæg þekking situr hjá aðeins einum eða fáum) og hraðasta leið þín til að taka á móti nýliðum. Þegar hundruð verkfræðinga reiða sig á kerfi sem þeir smíðuðu ekki, og fólk kemur, flytur og fer allan tímann, getur skipulagsheildin aðeins starfað ef þekking er skrifuð niður og auðveld að finna. Óskjalfest kerfi verða brothætt: aðeins höfundar þeirra geta breytt þeim örugglega, og þegar þeir fara missir skipulagsheildin getuna til að viðhalda eigin hugbúnaði. Það er ein algengasta og dýrasta bilun í stórum stíl.

Fyrirtækja- og opinbert samhengi hækkar hagsmunina enn frekar. Kerfi lifa lengi, svo skjölun þín þarf að þjóna umsjónarmönnum árum, jafnvel áratugum, eftir að upphaflega teymið er farið. Regluverks- og úttektarkerfi skylda oft tiltekin skjöl sem sönnun stýringar: arkitektúrskrár, [keyrsluhandbækur](https://en.wikipedia.org/wiki/Runbook) (skref-fyrir-skref rekstrar- og atvikaviðbragðsferla) og ákvörðunarannála. Opinber kerfi sem eru afhent milli söluaðila treysta alfarið á skjölun til að bera þekkingu yfir samningsmörk. Og samt er skjölun alræmd fyrir að rotna, svo raunverulega áskorunin er að halda henni nákvæmri eftir því sem hugbúnaðurinn breytist.

## Meginreglur

- Skrifaðu fyrir tiltekinn lesanda með tiltekna þörf. Ólíkar skjalagerðir þjóna ólíkum tilgangi.
- Haltu skjölun nálægt kóðanum og líttu á hana sem kóða (skjöl-sem-kóði).
- Nákvæmni slær fullkomnun. Lítið magn af áreiðanlegri skjölun slær mikið magn sem er rangt.
- Myndaðu það sem hægt er að mynda. Viðhaldtu ekki í höndunum því sem verkfæri getur framleitt úr uppsprettu sannleikans.
- Berstu virkt gegn skjalarotnun. Úrelt skjöl eru verri en engin því þau villa um fyrir.
- Gerðu skjölun finnanlega. Þekking sem ekki finnst er í reynd fjarverandi.
- Skráðu ákvarðanir og rök þeirra, ekki bara núverandi ástand.

## Ráðleggingar

### Taktu upp skjöl-sem-kóða

Geymdu skjölun í [útgáfustýringu](https://en.wikipedia.org/wiki/Version_control) rétt við hlið kóðans sem hún lýsir, skrifaðu hana í látlausu textamerkjamáli og rýndu hana gegnum sama sameiningarbeiðnaferli. Það heldur henni útgáfustýrðri, rýnanlegri og nálægt kóðanum, svo þú getir uppfært hvort tveggja saman. Birtu hana gegnum sjálfvirka leiðslu svo nýjasta útgáfan sé alltaf tiltæk. Að líta á skjöl sem kóða færir sama aga og heldur kóða áreiðanlegum: rýni, sögu og sjálfvirkni.

### Skipulegðu efni með Diátaxis-rammanum

Skipulegðu skjölun í fjórar aðskildar gerðir, því að blanda þeim þjónar engum lesanda vel: kennsluleiðbeiningar (námsmiðaðar, fyrir nýliða), hvernig-á-að leiðbeiningar (verkefnamiðaðar, fyrir tiltekið markmið), tilvísun (upplýsingamiðuð, nákvæm og tæmandi) og útskýring (skilningsmiðuð, hvers vegna og samhengið). Haltu þessu aðskildu og allt verður auðveldara að skrifa, rata um og viðhalda, því hver síða hefur eitt skýrt hlutverk og einn skýran markhóp.

### Viðhaldtu nauðsynlegum rekstrarskjölum

Gefðu hverju hugbúnaðarsafni skýra [README](https://en.wikipedia.org/wiki/README) sem útidyr þess: hvað það er, hvernig á að smíða og keyra það og hvert á að fara næst. Skrifaðu keyrsluhandbækur fyrir rekstrarverkefni og atvikaviðbrögð, svo hver sem er á bakvakt geti brugðist við, ekki bara sérfræðingarnir. Haltu arkitektúrskjölun sem útskýrir uppbyggingu kerfisins og lykilíhluti. Og útvegaðu móttökuskjölun sem kemur nýjum verkfræðingi fljótt til starfa. Þetta eru skjölin sem þú saknar mest þegar þau eru ekki til.

### Myndaðu API-skjöl og breytingaskrár úr uppsprettu sannleikans

Myndaðu API-tilvísunarskjölun þína úr véllæsilega samningnum eða kóðaskýringum, svo hún geti ekki rekið frá raunverulega viðmótinu. Haltu [breytingaskrá](https://en.wikipedia.org/wiki/Changelog), helst myndaðri úr skipulögðum commit eða útgáfuathugasemdum, svo neytendur sjái hvað breyttist milli útgáfa. Að sjálfvirknivæða þetta tekur rotnunargjörnustu handviðhaldnu skjölunina af þér og heldur henni áreiðanlegri.

### Skráðu arkitektúrákvarðanir

Fangaðu mikilvægar arkitektúr- og hönnunarákvarðanir sem létt, dagsett skrár sem segja samhengið, ákvörðunina og afleiðingar hennar. Þessar ákvörðunarskrár varðveita rökin sem annars töpuðust, svo framtíðarumsjónarmenn sjái hvers vegna kerfið er eins og það er í stað þess að efast um það eða endurtaka gömul mistök. Þær borga sig sérstaklega yfir langan líftíma fyrirtækja- og opinberra kerfa.

### Berstu gegn skjalarotnun af ásetningi

Líttu á úrelta skjölun sem galla. Uppfærðu skjölin sem hluta af sömu breytingu og breytir hegðun og gerðu það að rýniviðmiði. Úthlutaðu eignarhaldi svo hvert mikilvægt skjal hafi einhvern ábyrgan. Rýndu verðmæta skjölun fyrir nákvæmni öðru hverju, snyrtu það sem er úrelt og fjarlægðu eða merktu skýrt allt sem þú treystir ekki lengur. Skjölunin sem rotnar minnst er lifandi skjölun: mynduð eða prófuð gegn kerfinu sjálfu.

### Fjárfestu í þekkingarstjórnun og finnanleika

Gerðu skjölun finnanlega með góðri leit, skýrri leiðsögn og þekktu heimili, svo fólk geti fundið það sem það þarf án þess að þurfa að spyrja einhvern. Láttu hana ekki sundrast yfir of mörg ótengd wiki og verkfæri. Og fangaðu [þögla þekkingu](https://en.wikipedia.org/wiki/Tacit_knowledge), óformlega skilninginn sem lifir í spjallþráðum og höfðum fólks, í varanlegt, finnanlegt form áður en hún rennur burt.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
|---|---|---|
| Skjöl-sem-kóði | Útgáfustýrð, rýnanleg, nálægt kóða, lítil rotnun | Krefst verkfræðiaga, minna vinalegt höfundum sem eru ekki tæknilegir |
| Wiki / þekkingargrunnur | Auðvelt að breyta, aðgengilegt öllum | Rekur frá kóða, sundrast, rotnar hljóðlega |
| Mynduð skjöl (API, breytingaskrá) | Alltaf nákvæm, lítið viðhald | Takmörkuð við það sem uppsprettan tjáir, þarf verkfæri |
| Handskrifuð útskýring | Rík samhengi og rök sem vélar geta ekki framleitt | Vinnufrek, hætt við að úreldast |
| Diátaxis-uppbygging | Skýr tilgangur á hverja síðu, auðveldara að rata og viðhalda | Uppbyggingarfyrirhöfn fyrirfram, krefst höfundaaga |

Meginmálamiðlunin er fyrirhöfn gegn nákvæmni og endingu. Ódýrasta skjölunin að skrifa, fljótleg wiki-síða, er líka sú sem er hættust við rotnun og sundrun. Endingarbesta skjölunin, mynduð úr uppsprettunni eða rýnd sem kóði, kostar meiri aga fyrirfram en helst áreiðanleg. Góð þumalfingursregla: myndaðu það sem þú getur, haltu restinni nálægt kóðanum og rýndri eins og kóða og taktu frá vinnufreka handskrifaða útskýringu fyrir rökin sem aðeins menn geta veitt.

## Spurningar til að ræða með teyminu

1. **Eru skjöl þín aðskilin eftir lesendaþörf, eða blandast kennsla, tilvísun og útskýring saman á einni síðu?** Þessi kafli mælir með Diátaxis-skiptingunni í kennsluleiðbeiningar, hvernig-á-að leiðbeiningar, tilvísun og útskýringu, og telur blöndun gerða upp sem andmynstur sem þjónar engum lesanda vel. Í stórum stíl þurfa nýliði sem lærir kerfið og bakvaktarverkfræðingur sem leitar að nákvæmri staðreynd ólíkar síður, og ein blönduð síða hægir á báðum. Komdu með merkið: veldu mest heimsóttu skjöl þín og athugaðu hvort hvert hafi eitt skýrt hlutverk og einn skýran markhóp. Endurskipuleggðu verstu tilvikin í aðskildar gerðir, svo hver síða sé auðveldari að skrifa, rata um og halda uppfærðri. Sú uppbygging er það sem gerir skjölun viðhaldanlega eftir því sem skipulagsheildin vex.

2. **Fangarðu mikilvægar arkitektúrákvarðanir með rökum þeirra, eða aðeins núverandi ástand?** Kaflinn mælir með léttum, dagsettum ákvörðunarskrám sem segja samhengi, ákvörðun og afleiðingar, og tekur fram að þær borgi sig mest yfir langan líftíma fyrirtækja- og opinberra kerfa. Án þeirra getur umsjónarmaður árum síðar ekki séð hvers vegna kerfið er eins og það er, svo hann efast um traust val eða endurtekur gömul mistök. Komdu með nýlega erfiða ákvörðun þar sem rökin lifa nú aðeins í spjallþræði eða minni einhvers sem áþreifanlegt merki. Taktu upp stutt ákvörðunarskrársnið og gerðu að skrifa eina hluta af hverri mikilvægri hönnunarbreytingu. Rökin eru einmitt þekkingin sem aðeins menn geta veitt og rotnar hraðast þegar hún er óskrifuð.

3. **Getur hvaða bakvaktarverkfræðingur sem er brugðist við atviki úr keyrsluhandbókunum þínum einum, án þess að kalla út manneskjuna sem smíðaði kerfið?** Þessi kafli nefnir keyrsluhandbækur sem nauðsynlegt rekstrarskjal svo hver sem er á bakvakt geti brugðist við, ekki bara sérfræðingarnir, og lýsir opinberu teymi sem gat aðeins erft kerfi því keyrsluhandbækur báru þekkinguna yfir samningsmörk. Lykilmannaáhætta er bilunin sem þetta ver gegn: þegar eini sérfræðingurinn er óaðgengilegur eða farinn breytir óskjalfest endurheimtarferli venjulegu atviki í rekstrarrof. Komdu með sönnunargögnin: taktu nýlegt atvik og athugaðu hvort keyrsluhandbókin ein hefði leyst það. Skrifaðu og prófaðu keyrsluhandbækur fyrir ferlana sem fólk óttast og líttu á keyrsluhandbók sem getur ekki staðið ein sem galla. Það er munurinn á endurheimt klukkan 2 að nóttu og stigmögnun klukkan 2 að nóttu.

4. **Hver af API-tilvísunum þínum og breytingaskrám eru myndaðar úr uppsprettu sannleikans og hverjar eru enn handviðhaldnar og reka hljóðlega?** Þessi kafli segir þér að mynda tilvísunarskjölun úr véllæsilega samningnum eða kóðaskýringum svo hún geti ekki vikið frá raunverulega viðmótinu, og telur handviðhald mynduanlegs efnis upp sem andmynstur. Fyrir stórt teymi er handskrifað API-skjal sem dregst aftur úr raunverulega viðmótinu verra en ekkert: hver neytandi sem treystir því skrifar bilaða samþættingu, og bilunin kemur fram langt frá úreltu síðunni sem olli henni. Komdu með áþreifanlega merkið: taktu úrtak af handfylli mest notuðu viðmóta þinna og berðu birta tilvísun saman við raunverulega samninginn til að sjá hve langt hver hefur rekið. Þar sem þú finnur rek skaltu tengja tilvísunina við smíðina svo hún myndist upp á nýtt við hverja breytingu og leggja niður handhaldna afritið. Í fyrirtækja- og opinberu umhverfi, þar sem viðmót eru notuð yfir teymi, söluaðila og samningsmörk sem þú sérð aldrei, er valdbær mynduð tilvísun oft það eina sem heldur samþættarum frá því að smíða gegn skáldskap.

5. **Hver á hvert verðmætt skjal og hvernig myndirðu taka eftir því í dag ef eitt hefði úrelst?** Kaflinn lítur á úrelta skjölun sem galla og varar við að óeignuð skjöl rotni því að uppfæra þau er verk enginn, á meðan úrelt skjöl sett fram sem núverandi eyðileggja traust á allri skjölun þinni. Í stórum stíl er hættan ekki ein röng síða heldur hæg rýrnun sjálfstrausts: þegar lesendur hafa brennt sig á úreltum leiðbeiningum hætta þeir að treysta öllu safninu og fara aftur að trufla fólk. Komdu með eignarhaldskort yfir mikilvægustu skjöl þín og heiðarlegt svar við því hvernig rotnun greinist, með rýnitakti, myndun, prófum gegn kerfinu eða hreinni heppni. Úthlutaðu nefndum eiganda á hvert skjal sem skiptir máli og kjóstu lifandi skjölun sem er mynduð eða prófuð svo úrelding birtist vélrænt en ekki gegnum vandræðalegan lesanda. Fyrir fyrirtækja- og opinber kerfi sem lifa upphafleg teymi sín er óeignuð skjölun skuldbinding sem endurskoðandi eða erfandi söluaðili mun að lokum rukka þig fyrir.

6. **Hve finnanleg er skjölun þín og hve mikil mikilvæg þekking lifir enn aðeins í spjallþráðum og höfðum fólks?** Þessi kafli segir að þekking sem ekki finnst sé í reynd fjarverandi, varar við að sundra skjölum yfir of mörg ótengd wiki og verkfæri og hvetur þig til að fanga þögla þekkingu í varanlegt, finnanlegt form áður en hún rennur burt. Í stórri skipulagsheild er sama staðreyndin oft enduruppgötvuð, endurspurð og endursvöruð hundrað sinnum því enginn finnur hvar hún var þegar skrifuð, og hver brottför tekur óbætanlegt samhengi út um dyrnar. Komdu með sönnunargögnin: teldu hve mörg aðskilin skjalaheimili þú heldur, reyndu að finna þrjár mikilvægar staðreyndir með leit einni og taktu eftir hvar raunveruleg svör reyndust lifa í minni einhvers eða grafin skilaboð. Sameinaðu í átt að þekktu heimili með raunverulegri leit og skýrri leiðsögn, og gerðu að fanga þögla þekkingu venjulegan hluta vinnunnar en ekki hetjulega björgun. Í opinberu og mikið útvistuðu samhengi, þar sem kerfi flytjast milli söluaðila og teyma með samningi, er finnanleg skrifleg þekking það eina sem lifir yfirfærsluna.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með handfylli verkfræðinga og ekkert svigrúm skaltu skjalfesta aðeins það sem rekstrarrof klukkan 2 að nóttu eða nýr starfsmaður myndi í raun þurfa: raunverulegt README fyrir hverja þjónustu, eina prófaða keyrsluhandbók fyrir uppsetningar-og-endurheimtarferlið sem allir óttast og fáeinar dagsettar athugasemdir um ákvarðanirnar sem þú myndir annars gleyma. Myndaðu API-skjöl úr samningnum svo þú viðhaldir þeim aldrei í höndunum. Stattu gegn freistingunni að smíða skjölunarvettvang. Útgáfustýrð mappa af merkjamáli við hlið kóðans er nóg þar til þú finnur raunverulegan sársauka.

**Lítið fyrirtæki.** Án tæknilegs rithöfundar og með þröngt fjárhagsáætlun skaltu hallast að skjölun sem verkfærin þín mynda nú þegar og að léttu skjöl-sem-kóða frekar en mannaðri áætlun. Rammaðu valið sem kaupa á móti smíða: kjóstu vettvanga sem framleiða eigin núverandi tilvísun og leitanlegan þekkingargrunn fram yfir wiki sem þú verður að sinna í höndunum. Eyddu af skornum skammti fyrirhöfn í skjölin tvö eða þrjú þar sem fjarvera þeirra myndi stöðva reksturinn og láttu ranga eða vantandi síðu vera kveikjuna að því að laga eignarhald.

**Stórfyrirtæki.** Yfir mörg teymi er vandinn samræmi og finnanleiki: sameiginleg skjöl-sem-kóða leiðsla, sameiginleg uppbygging eins og Diátaxis, mynduð API-tilvísun og breytingaskrár og ákvörðunarskrár beitt eins alls staðar svo þekking sundrist ekki yfir tugi wiki. Úthlutaðu eignarhaldi fyrir hvert verðmætt skjal og mældu nákvæmni, ekki bara tilvist. Líttu á arkitektúrskrár, keyrsluhandbækur og ákvörðunarannála sem úttektarsönnun og staðlaðu hvernig þau eru framleidd svo stýringarrýni finni skjalfesta, rökstudda slóð en ekki hlaup.

**Hið opinbera.** Innkaupareglur og almenn ábyrgð gera skjölun að afurð, ekki kurteisi. Skrifaðu arkitektúrskjölun, keyrsluhandbækur og ákvörðunarskrár inn í samninga sem skyldubundin afurð, rýnd fyrir nákvæmni svo þekking lifi söluaðilaskipti og kerfi sé hægt að reka af hverjum sem erfir það. Krefstu þess að hver heimilaður rekstraraðili geti brugðist við atviki úr keyrsluhandbókinni einni og haltu ákvörðunarannálum sem gagnsærri opinberri skrá um hvers vegna val voru gerð. Þunn skjölun hér er ekki einkaóþægindi. Hún verður kostnaðarsöm öfug verkfræði fjármögnuð af skattgreiðendum.

## Dæmi

**Sprotafyrirtæki.** Fimm manna sprotafyrirtæki skrifar raunverulegt README fyrir hverja þjónustu og stutta keyrsluhandbók fyrir eina uppsetningar-og-endurheimtarferlið sem allir óttast, svo rekstrarrof klukkan 2 að nóttu velti ekki á því að vekja eina stofnandann sem þekkir kerfið. Þeir mynda API-skjöl úr samningnum í stað þess að skrifa þau í höndunum og skrifa nokkrar dagsettar athugasemdir sem útskýra hvers vegna þeir völdu gagnagrunninn sinn og auðkenningaraðferð. Það helst létt, en það þýðir að sjöundi og áttundi starfsmaðurinn fá móttöku úr skjölum en ekki með því að trufla alla.

**Stórfyrirtæki.** Stórt hugbúnaðarfyrirtæki geymir alla skjölun sína í sömu hugbúnaðarsöfnum og kóðann sinn, skrifaða í merkjamáli og rýnda í sameiningarbeiðnum rétt við hlið breytinganna sem þau lýsa. API-tilvísanir eru myndaðar úr þjónustusamningum, svo þær reka aldrei. Breytingaskrár eru myndaðar úr skipulögðum commit og arkitektúrákvörðunarskrár varðveita rökin að baki stórum valum. Birt skjalavefsvæði smíðast sjálfvirkt við hverja sameiningu. Nýir verkfræðingar verða fljótt afkastamiklir því móttökuleiðbeiningar og keyrsluhandbækur eru núverandi og finnanlegar, og bakvaktarverkfræðingar styðjast við keyrsluhandbækur í stað þess að kalla út upphaflegu höfundana.

**Hið opinbera.** Landsbundin stofnun erfir kerfi frá brottfarandi verktaka og treystir alfarið á skjölun til að bera þekkingu yfir samningsmörkin. Því fyrri söluaðilinn hélt arkitektúrskjölun, keyrsluhandbókum og ákvörðunarskrám sem skyldubundnum afurðum getur nýja teymið rekið og breytt kerfinu án upphaflegu höfundanna. Þar sem skjölun var þunn stendur stofnunin frammi fyrir kostnaðarsamri öfugri verkfræði. Sú reynsla knýr nýja stefnu: skjölun er samningsbundin afurð, rýnd fyrir nákvæmni frekar en meðhöndluð sem eftiráhugsun, og keyrsluhandbækur verða að leyfa hverjum heimiluðum rekstraraðila að bregðast við atvikum.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Skjölun borgar sig til baka í styttri móttökutíma, minni lykilmannaáhættu, hraðari atvikaviðbrögðum og lægri breytingakostnaði yfir líftíma kerfis. Nýir verkfræðingar sem ná framleiðni á dögum frekar en vikum, bakvaktarstarfsfólk sem leysir atvik úr keyrsluhandbók í stað þess að stigmagna, umsjónarmenn sem breyta kerfi af öryggi árum eftir að það var smíðað: þetta eru stór, endurtekin sparnaður sem safnast upp yfir stóra skipulagsheild og langan kerfislíftíma.

Hvað kostar skjölun? Höfundar- og viðhaldsfyrirhöfn. Hvað kostar að skjalfesta *ekki*? Þú borgar stöðugt: í hægri móttöku, endurteknum spurningum, lykilmannaflöskuhálsum, hægari atvikaendurheimt og, í öfgum, kerfum sem enginn getur breytt örugglega, sem neyðir fram dýr endurskrif eða öfuga verkfræði. Í söluaðilaskiptum og úttektaraðstæðum getur vantandi skjölun borið beinan samnings- og regluvörslukostnað. Til að færa rök við forystu skaltu setja tölur á móttökutíma, atvikaviðbragðstíma og hve mikið af mikilvægri þekkingu situr í einstökum höfðum. Rammaðu síðan skjöl-sem-kóða og myndun sem leiðir til að fá varanlega skjölun án samsvarandi viðhaldsbyrði. Og leggðu áherslu á að ónákvæm skjölun er skuldbinding, svo fjárfestingin verður að fela í sér að halda henni núverandi.

## Andmynstur og gildrur

- **Úrelt skjölun sett fram sem núverandi:** villir lesendur og eyðileggur traust á allri skjölun.
- **Skrifað-einu-sinni wiki:** síður búnar til og aldrei uppfærðar, reka hljóðlega frá raunveruleikanum.
- **Skjölunarsundrun:** þekking dreifð yfir mörg verkfæri og wiki svo ekkert finnst.
- **Blöndun skjalagerða:** kennsla, tilvísun og útskýring í einni hrúgu á einni síðu, sem þjónar engum lesanda vel.
- **Handviðhald mynduanlegs efnis:** handskrifuð API-skjöl sem óhjákvæmilega víkja frá raunverulega viðmótinu.
- **Ættbálkaþekking:** mikilvægur skilningur geymdur aðeins í höfðum fólks og spjallsögu, glatast þegar það fer.
- **Skjölun sem eftiráhugsun:** skrifuð í lokin, ef nokkurn tíma, frekar en samhliða breytingunni.
- **Ekkert eignarhald:** skjöl án ábyrgs eiganda rotna því að uppfæra þau er verk enginn.

## Þroskalíkan

- **Stig 1, Upphaf.** Skjölun er rýr, dreifð og úrelt, og þekking lifir í höfðum fólks. Það sem er til var skrifað einu sinni og aldrei snert aftur, svo rekstrarrof eða brottför þýðir öfug verkfræði kerfisins.
- **Stig 2, Þróun.** Lykilskjöl eru til, svo sem README og nokkrar keyrsluhandbækur, en þeim er viðhaldið ósamræmt og erfitt er að finna þau. Sum teymi skjalfesta vel og önnur varla, og engin sameiginleg væntig er um hvað hugbúnaðarsafn ætti að bera eða hvar það ætti að búa.
- **Stig 3, Stöðlun.** Skjöl-sem-kóða er normið um alla skipulagsheildina: sameiginleg uppbygging eins og Diátaxis, mynduð API-tilvísun og breytingaskrár, ákvörðunarskrár og væntig í rýni um að skjöl breytist með kóðanum sem þau lýsa. Sérhvert verðmætt skjal hefur nefndan eiganda og eitt þekkt heimili með raunverulegri leit.
- **Stig 4, Stjórnun.** Skjölun er mæld, ekki bara til staðar. Þú rekur þekju nauðsynlegra skjala, skjalabreytingatíðni gegn kóðabreytingatíðni, móttökutíma, atvikalausn úr keyrsluhandbókum einum og ferskleika gegn skilgreindum úreldingarþröskuldi, og rýnir þá mælikvarða gegn grunnlínum. Rotnun er gripin vélrænt með myndun, prófum gegn kerfinu og tengla- og nákvæmnisathugunum, og úreltar síður eru merktar eða snyrtar á grundvelli gagna frekar en tilviljunar.
- **Stig 5, Samhæfing.** Skjölun er stöðugt bætt og samþætt um skipulagsheildina: lifandi, að mestu mynduð eða prófuð gegn kerfinu, eignuð, finnanleg og aðlögunarhæf. Mælikvarðar næra aftur hvar þú fjárfestir, þögul þekking er fönguð sem venjulegur hluti vinnunnar og safnið er virkt endurjafnað og snyrt eftir því sem kerfi, teymi og lesendur breytast.

## Hugmyndir til umræðu

- Hvaða skjölun, ef hún hyrfi á morgun, myndi skaða skipulagsheildina þína mest og er hún til og helst núverandi?
- Hvernig gerirðu uppfærslu skjölunar að eðlilegum hluta þess að breyta kóða frekar en aðskildu verki?
- Hvar geturðu skipt út handskrifaðri skjölun fyrir myndaða skjölun tengda uppsprettu sannleikans?
- Hvernig mælirðu hvort skjölun þín sé nákvæm og notuð, ekki bara til staðar?
- Hvernig ættu gervigreindaraðstoðarmenn að breyta því hvernig þú skrifar, viðheldur og leitar í skjölun og hvar gætu þeir kynnt sennilegt-en-rangt efni?
- Hvernig fangarðu þögla þekkingu áður en fólkið sem ber hana fer?

## Helstu atriði

- Líttu á skjölun sem kóða: útgáfustýrða, rýnda, nálægt uppsprettunni og birta sjálfvirkt.
- Skipulegðu efni eftir lesendaþörf með kennsluleiðbeiningum, hvernig-á-að leiðbeiningum, tilvísun og útskýringu.
- Viðhaldtu verðmætum nauðsynjum: README, keyrsluhandbókum, arkitektúrskjölum, móttöku og ákvörðunarskrám.
- Myndaðu API-skjöl og breytingaskrár svo þau geti ekki vikið frá uppsprettu sannleikans.
- Berstu gegn rotnun með eignarhaldi, rýniviðmiðum og snyrtingu. Ónákvæm skjölun er verri en engin.

## Heimildir og frekari lestur

- Daniele Procida, *Diátaxis* documentation framework
- Andrew Etter, *Modern Technical Writing*
- Anne Gentle, *Docs Like Code*
- Google, *Developer Documentation Style Guide* and Season of Docs guidance (as reference exemplars)
- Michael Nygard, *Documenting Architecture Decisions* (architecture decision records)
- Andrew Hunt and David Thomas, *The Pragmatic Programmer* (on knowledge and documentation)
- *Keep a Changelog* (as a reference convention)
