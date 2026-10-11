# 6.5 Ábyrg og traustverð gervigreind

## Yfirlit og tilgangur

Ábyrg og traustverð gervigreind er sú venja að smíða og reka gervigreindarkerfi sem eru sanngjörn, gagnsæ, ábyrg, örugg og virða persónuvernd. Hún þýðir líka að geta sýnt fram á allt þetta fyrir þeim sem verða fyrir áhrifum og fyrir eftirlitsaðilum. Þegar gervigreind tekur ákvarðanir sem móta líf fólks (ráðningar, útlán, réttur til bóta) er spurningin ekki lengur bara „virkar þetta?“ heldur „er þetta rétt og getum við rökstutt það?“ Kerfi sem er nákvæmt að meðaltali getur samt verið ósanngjarnt gagnvart undirhópi, óútskýranlegt fyrir manneskjunni sem það snertir eða óöruggt þegar því er misbeitt. Þú vinnur þér inn traust með því að taka á þessum víddum af ásetningi, ekki með því að vona að þær sjái um sig sjálfar.

Fyrir stór teymi getur ábyrg gervigreind ekki verið starf eins manns eða hakreitur í lokin. Fléttaðu hana inn í hvernig þú hannar, metur, setur upp og stýrir kerfum, með skýru eignarhaldi og stigmögnun. Í stærð hafa litlar skekkjur og göt í eftirliti áhrif á marga. Ein áberandi bilun getur skaðað orðspor þitt og boðið regluverki heim. Stjórnarháttarammar eru til einmitt því góður ásetningur nær ekki í stærð.

Opinberar og regluverkaðar skipulagsheildir standa frammi fyrir bindandi skyldum. Ný lög, eins og [gervigreindarreglugerð ESB](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act), setja kröfur stigskiptar eftir áhættu. Staðlar eins og áhættustýringarrammi NIST fyrir gervigreind og ISO/IEC 42001 gefa þér uppbyggðar leiðir til að mæta þeim. Opinberir aðilar verða að forðast ólögmæta mismunun, veita leiðir til að andmæla sjálfvirkum ákvörðunum og vera gagnsæir um hvernig gervigreind er notuð við beitingu opinbers valds. Ábyrg gervigreind í þessu umhverfi er bæði siðferðisleg skylda og lagaleg nauðsyn.

*Sjá einnig:* kafla 6.1 (stefna og viðbúnaður í gervigreind), kafla 10.5 (siðferði, ábyrgð og almannahagur) og kafla 4.5 (persónuvernd og gagnavernd).

## Meginreglur

- Sanngirni er hönnunarmarkmið sem á að mæla og stýra, ekki gera ráð fyrir.
- Fólk sem verður fyrir áhrifum gervigreindarákvarðana á skilið útskýringu og leið til að andmæla þeim.
- Ábyrgð hvílir á mönnum og skipulagsheildinni, aldrei á líkaninu.
- Persónuvernd og öryggi verða að vera hönnuð inn, þar með talin vernd gegn misnotkun og misbeitingu.
- Stjórnarhættir ættu að fylgja viðurkenndum römmum svo þeir séu verjanlegir og úttektarhæfir.
- Mannlegt eftirlit verður að vera marktækt, með raunverulegu valdi til að hnekkja og stöðva.
- Hugleiddu víðtækari kostnað gervigreindar, þar með talin umhverfisáhrif hennar.

## Ráðleggingar

### Greindu og dragðu úr skekkju og ósanngirni

Skilgreindu hvað sanngirni þýðir í þínu samhengi. Til eru margar, stundum andstæðar, stærðfræðilegar skilgreiningar og sú rétta ræðst af ákvörðuninni og lögunum. Prófaðu líkön fyrir ólíkri frammistöðu yfir verndaða og berskjaldaða hópa með dæmigerðum gögnum. Gerðu þetta fyrir útsetningu og haltu því áfram eftir hana, því [skekkja](https://en.wikipedia.org/wiki/Algorithmic_bias) getur komið upp þegar þýði færast. Dragðu úr með betri gögnum, endurvigtun, skorðum eða með því að breyta því hvernig kerfið er notað, og skjalfestu málamiðlanirnar sem þú samþykktir. Að fjarlægja verndað einkenni fjarlægir ekki skekkju, því staðgenglar eru eftir. Líttu á sanngirni sem viðvarandi mælinga- og stýringaragaga, ekki einskiptis hreinsun.

### Veittu skýranleika, túlkanleika og gagnsæi

Láttu útskýringarstigið passa við það sem er í húfi og áheyrendur. Fyrir afleiddar ákvarðanir skaltu gefa fólki sem verður fyrir áhrifum skýra ástæðu á einföldu máli sem það getur skilið og brugðist við. Fyrir innri stjórnarhætti skaltu halda nægum tæknilegum [túlkanleika](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence) til að aflúsa og verja kerfið. Kjóstu eðlislega túlkanleg líkön þar sem mikið er í húfi og túlkanleiki er framkvæmanlegur. Þar sem flókin líkön eru nauðsynleg skaltu nota útskýringartækni en vera heiðarlegur um takmörk hennar. Vertu gagnsær um hvenær gervigreind er yfirleitt notuð, sérstaklega í samskiptum við almenning.

### Stýrðu með viðurkenndum römmum

Taktu upp uppbyggða stjórnarhætti frekar en að finna upp þína eigin. **Áhættustýringarrammi NIST fyrir gervigreind** skipuleggur vinnu í kringum að stýra, kortleggja, mæla og stjórna gervigreindaráhættu. **Gervigreindarreglugerð ESB** flokkar kerfi eftir áhættu og setur skyldur í samræmi við það, með ströngum kröfum fyrir áhættumikla notkun. **ISO/IEC 42001** skilgreinir stjórnkerfi gervigreindar sem hægt er að úttekta og votta. Kortleggðu kerfi þín við þessa ramma. Haltu skjölun eins og líkana- og gagnaspjöldum (staðlaðar samantektir á tilgangi, frammistöðu og takmörkunum líkans eða gagnasafns). Framkvæmdu áhættumat fyrir útsetningu og haltu skrá yfir gervigreindarkerfi með áhættustigi þeirra og eigendum. Góðir stjórnarhættir úthluta skýrum hlutverkum, ákvörðunarrétti og stigmögnunarleiðum.

### Tryggðu mannlegt eftirlit, ábyrgð og áfrýjun

Haltu manni með marktæka stjórn á afleiddum ákvörðunum, með raunverulegt vald og upplýsingarnar sem þarf til að hnekkja kerfinu, ekki stimpil. Úthlutaðu skýrri ábyrgð: nefndu eiganda sem svarar fyrir hegðun hvers kerfis. Gefðu fólki sem verður fyrir áhrifum sjálfvirkra ákvarðana rétt til útskýringar og vinnanlegt ferli til að áfrýja til manns sem getur breytt niðurstöðunni. Skráðu ákvarðanir og forsendur þeirra, svo þú getir meðhöndlað áfrýjanir og úttektir sanngjarnt og skjótt.

### Verndaðu persónuvernd, öryggi og gegn misnotkun

Lágmarkaðu persónugögnin sem þú safnar og notar, komdu á lagagrundvelli og beittu persónuverndartækni sem hæfir viðkvæmninni. [Rauðliðaprófaðu](https://en.wikipedia.org/wiki/Red_team) kerfi fyrir og eftir útsetningu til að finna leiðir sem hægt er að blekkja þau, brjótast úr skorðum þeirra eða misnota þau til skaða, og lagaðu það sem þú finnur. Smíðaðu varnir gegn því að búa til skaðlegt efni, leka viðkvæmum gögnum eða gera misnotkun mögulega. Skipuleggðu fyrir atvik: vöktun, viðbrögð og upplýsingagjöf. Hugleiddu [tvínotkun](https://en.wikipedia.org/wiki/Dual-use_technology) (sama geta þjónar bæði gagnlegum og skaðlegum tilgangi) og misnotkun síðar í ferlinu, ekki bara ætlaða notkun.

### Taktu tillit til umhverfiskostnaðar

Þjálfun og þjónusta stórra líkana eyðir umtalsverðri orku og vatni. Mældu og skýrðu frá fótspori stærstu gervigreindarvinnuálaga. Kjóstu skilvirk líkön og vélbúnað þar sem þau mæta þörfinni. Stilltu stærð líkana að verkinu frekar en að sjálfgefa það stærsta og taktu umhverfiskostnað með í arkitektúr- og innkaupaákvarðanir.

## Málamiðlanir: kostir og gallar

| Spenna | Önnur hliðin | Hin hliðin |
|---|---|---|
| Nákvæmni gegn sanngirni | Hæsta meðalnákvæmni | Jafnar niðurstöður yfir hópa |
| Frammistaða gegn túlkanleika | Flókin, öflug líkön | Skýranleg, verjanleg líkön |
| Sjálfvirkni gegn eftirliti | Skilvirkni og stærð | Mannleg stjórn og ábyrgð |
| Gagnagildi gegn persónuvernd | Ríkari líkön úr fleiri gögnum | Gagnalágmörkun og vernd |
| Geta gegn öryggi | Breið, opin virkni | Afmörkuð, varin hegðun |
| Hraði gegn stjórnarháttum | Hröð útsetning | Ítarleg rýni og skjölun |

Sjaldan er til ókeypis hádegisverður. Að bæta sanngirni getur kostað einhverja nákvæmni. Túlkanleiki getur kostað einhverja frammistöðu. Stjórnarhættir kosta tíma. Ábyrga leiðin er að taka þessar málamiðlanir meðvitað, skjalfesta þær og velja í þágu þeirra sem verða fyrir áhrifum og verjanleika þegar mikið er í húfi. Að ramma stjórnarhætti sem bremsu á nýsköpun er fölsk tvískipting. Óstýrð gervigreindaráhætta er sjálf ógn við viðvarandi nýsköpun.

## Spurningar til að ræða með teyminu

1. **Hvaða af útsettum gervigreindarkerfum okkar myndi gervigreindarreglugerð ESB flokka sem áhættumikil og uppfyllum við þær skyldur í dag?** Áhættuskipt lög eru nú bindandi, ekki tilgátuleg, og kerfi sem ákveður ráðningu, útlán eða rétt til bóta getur borið strangar kröfur sem þú gætir þegar verið að brjóta. Fyrir stóra skipulagsheild neyðir þessi spurning fram heiðarlega skrá frekar en þægilega forsendu um að stjórnarháttum sé „sinnt“. Komdu með lista yfir gervigreindarkerfi þín með áhættustigum og eigendum, kortlagðan gegn gervigreindarreglugerð ESB, áhættustýringarramma NIST fyrir gervigreind og ISO/IEC 42001 þar sem við á. Merkið til að fylgjast með er sérhvert afleitt kerfi án áhættuflokkunar, án áhrifamats og án líkana- eða gagnaspjalds. Fyrir opinbera aðila sem beita opinberu valdi er það ekki bakslagsatriði að vanrækja skyldur, það er lagaleg útsetning, og svarið ætti að ræsa mat og skjölun sem þau kerfi krefjast.

2. **Þegar eitt líkana okkar hafnar einhverjum, getur sú manneskja fengið ástæðu á einföldu máli og náð til manns sem getur í raun snúið niðurstöðunni við?** Réttur til útskýringar og vinnanleg áfrýjun er það sem aðgreinir ábyrga gervigreind frá svörtum kassa sem skaðar fólk án úrræða. Sanngirni mæld að meðaltali getur samt brugðist einstaklingi og túlkanleiki valinn eftir útsetningu er yfirleitt leikhús. Komdu með tiltekna útsetta ákvörðun og raktu hana: ástæðuna sem manneskjan fær, áfrýjunarrásina og hvort maðurinn hinum megin hafi raunverulegt vald og skráða forsendu til að hnekkja. Í opinberu og regluverkuðu umhverfi er áfrýjunarleið oft lagaskylda, ekki kurteisi. Ef ástæðan er óskiljanleg eða áfrýjunin leiðir til stimpils er það bilið sem á að laga fyrir næstu útgáfu.

3. **Hver er sá eini nefndi maður sem ber ábyrgð þegar líkan veldur skaða og hefur hann raunverulegt vald til að stöðva það?** Ábyrgð hvílir á mönnum og skipulagsheildinni, aldrei á líkaninu, en sú regla er innantóm þar til nafn er fest við hvert kerfi og sá aðili getur í raun kippt úr sambandi. Fyrir stórt teymi þýðir dreift eignarhald að þegar sanngirnisbilun eða jailbreak kemur í ljós gera allir ráð fyrir að einhver annar fylgist með. Komdu með eignarhaldskort þitt, stigmögnunarleiðir þínar og sönnunargögn um að eftirlit sé marktækt: fær nefndi eigandinn upplýsingarnar og valdið til að hnekkja eða stöðva kerfið, eða aðeins til að kinka kolli? Ræddu hvernig þú rauðliðaprófar fyrir misnotkun og misbeitingu sem þú hefur ekki enn ímyndað þér, því að prófa aðeins ætlaða notkun missir af bilunum sem rata í fréttir. Svarið ætti ekki að skilja eftir neitt afleitt kerfi án ábyrgs eiganda sem getur stöðvað það.

4. **Fyrir hvert afleitt líkan, hvaða sanngirnisskilgreiningu völdum við, hver skrifaði undir hana og haldast undirhópamælikvarðar okkar í raun í framleiðslu?** Sanngirni hefur nokkrar stærðfræðilegar skilgreiningar sem stangast á, svo líkan sem uppfyllir jafnt hlutfall falskra jákvæðra getur brotið jafnar niðurstöður, og að velja skilgreiningu er gildisdómur sem ætti ekki að vera látinn þeim sem skrifaði þjálfunarlykkjuna. Fyrir stórt teymi felur óskoðað sjálfgefið valið inni í kóða og lætur hvern hóp síðar meir erfa ákvörðun sem enginn ræddi. Komdu með sanngirnismælikvarðann sem þú fínstilltir, verndaða og berskjaldaða hópana sem þú prófaðir yfir, dæmigerðu gögnin sem þú notaðir og rekið sem þú hefur séð frá opnun, því að fjarlægja verndað einkenni skilur eftir staðgengla sem halda skekkju á lífi. Í fyrirtækja- og opinberu umhverfi skaltu nefna aðilann sem hefur vald til að samþykkja sanngirnismálamiðlun og skrá hana, því eftirlitsaðili eða umboðsmaður mun spyrja hver ákvað að þessi skilgreining á sanngirni væri sú rétta fyrir fólk sem var synjað um lán, bætur eða starf. Ef engir undirhópamælikvarðar eru vaktaðir eftir útsetningu skaltu líta á líkanið sem ómælt frekar en sanngjarnt.

5. **Hve lítið af persónugögnum getur hvert kerfi keyrt á og höfum við rauðliðaprófað það fyrir misnotkun og tvínotkun sem við viljum helst ekki hugsa um?** Persónuvernd og öryggi verða að vera hönnuð inn og ódýrasta leiðin til að draga úr bæði brotahættu og misnotkunarfleti er að safna og geyma minna af gögnum í upphafi, samt safna teymi reglulega inntökum „ef þau hjálpa síðar“. Fyrir stóra skipulagsheild er sérhver aukareitur lagagrundvallarspurning, varðveisluskylda og stærri vinningur fyrir árásaraðila eða jailbreak. Komdu með gagnaskrána og lagagrundvöllinn fyrir hvert kerfi, niðurstöður rauðliðaprófana fyrir blekkingu, leka og skaðlega myndun og heiðarlegan lista yfir tvínotkunargetur þar sem sami eiginleiki sem hjálpar lögmætum notanda hjálpar líka einhverjum í vondri trú. Í regluverkuðu og opinberu samhengi skaltu tengja þetta við atvikaáætlun þína: vöktun, viðbrögð og upplýsingagjöf, því opinber aðili sem lekur viðkvæmum gögnum eða afhendir kerfi sem hægt er að brjótast úr skorðum stendur frammi fyrir lögbundnum skyldum, ekki bara vandræðagangi. Ef rauðliðaprófun reyndi aðeins ætluðu leiðina hefurðu prófað sýnikennsluna, ekki kerfið.

6. **Mælum við og eigum við umhverfisfótspor stærstu gervigreindarvinnuálaga okkar, eða er „notaðu stærsta líkanið“ óverðlagt sjálfgefið?** Þjálfun og þjónusta stórra líkana eyðir raunverulegri orku og vatni, og að sjálfgefa stærsta líkanið fyrir verk sem minna líkan myndi ráða við breytir verkfræðilegri styttingu í endurtekinn kostnað sem skipulagsheildin sér aldrei á mælaborði. Fyrir stórt teymi sem rekur mörg vinnuálög safnast litlar óhagkvæmni á kall í fótspor sem verður innkaupa- og skýrsluskuld þegar væntingar um upplýsingagjöf herðast. Komdu með mælt fótspor þyngstu vinnuálaga þinna, samanburð líkanastærða gegn nákvæmninni sem verkið þarf í raun og vélbúnaðar- og þjónustuvalin sem þú gætir stillt að stærð. Í fyrirtækja- og opinberu umhverfi skaltu tengja þetta við sjálfbærniskuldbindingar og innkaupaviðmið, því opinberir aðilar þurfa í auknum mæli að skýra frá umhverfisáhrifum og rökstyðja útgjöld, og ómælt fótspor er tala sem þú verður einn daginn beðinn að framleiða og getur það ekki. Ákveddu hvort umhverfiskostnaður sé formlegt inntak í líkanaval, eða viðurkenndu að hann er það ekki í dag.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Þú getur ekki mannað stjórnarháttaráð, svo gerðu léttu útgáfuna sem samt telur. Veldu túlkanleg líkön þar sem ákvörðunin er afleidd, skrifaðu eins síðu líkanaspjald, prófaðu fyrir ólíkum niðurstöðum yfir hópana sem þú getur mælt og skráðu ákvarðanir svo þú getir endurskoðað sanngirni þegar þú vex. Gefðu hverri óhagstæðri ákvörðun ástæðu á einföldu máli og leið til manns. Að sleppa þessu er ekki hraði, það er skuld sem þú hefur ekki efni á ef ein ósanngjörn ákvörðun nær til fjölmiðla eða eftirlitsaðila.

**Lítið fyrirtæki.** Án sérstaks sérfræðings skaltu líta á ábyrga gervigreind sem kaupspurningu: kjóstu seljendur sem skjalfesta sanngirnisprófanir, birta líkana- og gagnaspjöld og leyfa þér að upplýsa viðskiptavini þegar gervigreind er í notkun. Vittu hvaða persónugögnum verkfæri þín safna og hvort þú hafir lagagrundvöll til að nota þau. Þar sem rangt sjálfvirkt svar gæti skaðað viðskiptavin skaltu halda manni í lykkjunni frekar en að treysta verkfæri sem þú getur ekki skoðað eða útskýrt.

**Stórfyrirtæki.** Verkefnið er stjórnarhættir í stærð yfir mörg teymi: kortleggðu hvert kerfi við áhættustýringaramma NIST fyrir gervigreind, gervigreindarreglugerð ESB og ISO/IEC 42001, haltu skrá með áhættustigum og nefndum eigendum og krefstu sanngirnis-, öryggis- og persónuverndarprófana fyrir og eftir opnun. Staðlaðu líkana- og gagnaspjöld, rauðliðaprófanir og áfrýjunarferli svo hópar hætti að finna þau upp aftur. Fjárhagsáætlaðu stjórnarhátta-, eftirlits- og túlkanleikakostnað skýrt og líttu á óstýrða gervigreindaráhættu sem ógn við starfsleyfið.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta hvert val. Birtu gagnsæistilkynningu á einföldu máli, framkvæmdu áhrifamat fyrir útsetningu og haltu marktækri mannlegri ákvarðanatöku fyrir allar aðgerðir sem snerta borgara, með vinnanlegri áfrýjunarleið. Krefstu þess að seljendur upplýsi um takmarkanir líkana og veiti gagnaflytjanleika, forðastu ólögmæta mismunun, nefndu ábyrgan embættismann fyrir hvert kerfi og skýrðu frá umhverfisfótspori stærstu vinnuálaga.

## Dæmi

**Sprotafyrirtæki.** Lítið útlánasprotafyrirtæki sem smíðaði snemma lánshæfiseinkunnareiginleika gat ekki mannað stjórnarháttaráð, svo það gerði léttu útgáfuna sem samt skipti máli. Tveir stofnendur skrifuðu saman undir líkanið, prófuðu það fyrir ólíkum niðurstöðum yfir hópana sem þeir gátu mælt og skrifuðu stutt eins síðu líkanaspjald um gögn þess, takmarkanir og þekktar áhættur. Þeir völdu einfaldara, túlkanlegra líkan svo þeir gætu gefið hverjum synjuðum umsækjanda ástæðu á einföldu máli og leið til mannlegrar rýni, og þeir skráðu ákvarðanir svo þeir gætu endurskoðað sanngirni þegar þeir yxu.

**Stórfyrirtæki.** Banki sem setti upp lánshæfislíkan stofnaði gervigreindarstjórnarráð, kortlagði líkanið í áhættumikinn flokk og krafðist sanngirnisprófana yfir lýðfræðilega hópa fyrir og eftir opnun. Hann skjalfesti líkanið í líkanaspjaldi. Hann gaf synjuðum umsækjendum ástæðu á einföldu máli og áfrýjun til mannlegs áhættumatsmanns og rauðliðaprófaði kerfið fyrir blekkingu. Hann valdi aðeins ónákvæmara en túlkanlegra líkan, því hann þurfti að útskýra og verja hverja ákvörðun fyrir eftirlitsaðilum.

**Hið opinbera.** Opinber stofnun sem notar gervigreind til að úthluta eftirlitsfjármunum samræmdi áætlun sína við áhættustýringaramma NIST fyrir gervigreind og viðeigandi ákvæði gildandi gervigreindarlaga. Hún birti gagnsæistilkynningu sem lýsti því hvernig kerfið virkaði og öryggisráðstöfunum þess. Hún framkvæmdi áhrifamat fyrir útsetningu, hélt marktækri mannlegri ákvarðanatöku fyrir allar aðgerðir sem snertu borgara og veitti áfrýjunarferli. Sanngirni var vöktuð samfellt, umhverfiskostnaður vinnuálagsins var skýrður og ábyrgur embættismaður var nefndur sem svaraði fyrir kerfið.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ábyrg gervigreind ver verðmæti jafn mikið og hún skapar það. Ávöxtunin er að mestu forðaður kostnaður: færri mismununarkröfur, eftirlitssektir og orðsporshamfarir, mýkri úttektir og meira traust notenda og almennings, sem knýr upptöku. Traustverð kerfi eru líka sterkari, því agi sem framleiðir sanngirni og öryggi framleiðir líka betri verkfræði.

Heildareignarkostnaður felur í sér stjórnarháttastarfsfólk, sanngirnis- og öryggisprófanir, skjölun, rauðliðaprófanir, eftirlitsferli og frammistöðuna sem stundum er skipt fyrir túlkanleika eða sanngirni. Vegðu það gegn kostnaði þess að fjárfesta ekki: lagalega ábyrgð, þvingaðar lokanir, glatað traust almennings og margfalt hærri kostnað við að bæta stjórnarháttum við eftir bilun. Í regluverkuðu umhverfi er fjárfesting í ábyrgri gervigreind í auknum mæli óumsemjanleg. Færðu rök við forystu með því að ramma hana sem áhættustýringu og starfsleyfi: forsendu þess að setja gervigreind upp í stærð yfirleitt.

## Andmynstur og gildrur

- **Sanngirni með útilokun.** Að gera ráð fyrir að líkan sé sanngjarnt því það hunsar vernduð einkenni.
- **Útskýringarleikhús.** Að framleiða útskýringar sem endurspegla ekki í raun hvernig ákvarðanir eru teknar.
- **Stimpileftirlit.** Nafnbundin mannleg rýni án raunverulegs valds eða upplýsinga til að hnekkja.
- **Stjórnarhættir sem eftirþanki.** Að festa skjölun og rýni á eftir hönnun og útsetningu.
- **Engin áfrýjunarleið.** Að skilja fólk sem verður fyrir áhrifum eftir án leiðar til að andmæla sjálfvirkri ákvörðun.
- **Að hunsa misnotkun.** Að prófa aðeins ætlaða notkun og missa af jailbreak og misbeitingu.
- **Fótsporsblinda.** Að sjálfgefa stærsta líkanið án tillits til umhverfiskostnaðar.

## Þroskalíkan

1. **Upphaf.** Engar sanngirnisprófanir, útskýringar eða stjórnarhættir. Ábyrgð er óskilgreind. Skekkja, misnotkun og persónuverndarmál koma fram aðeins eftir skaða og engin skrá er til yfir gervigreindarkerfi eða áhættur þeirra.
2. **Þróun.** Einhverjar skekkjuprófanir, líkanaspjöld og rauðliðaprófanir eiga sér stað á einstökum kerfum, en vinnubrögð eru ósamræmd milli teyma. Eftirlit er handahófskennt. Rammar eins og áhættustýringarrammi NIST fyrir gervigreind og gervigreindarreglugerð ESB eru þekktir en aðeins að hluta teknir upp.
3. **Stöðlun.** Stjórnarhættir eru skjalfestir og framfylgdir um skipulagsheildina: kerfi eru kortlögð við viðurkennda ramma og ISO/IEC 42001, hvert hefur áhættustig og nefndan eiganda, og sanngirnis-, öryggis- og persónuverndarprófanir, líkana- og gagnaspjöld, áfrýjunarleiðir og rauðliðaprófanir fyrir áhættumikil kerfi eru skyldubundnar frekar en valkvæðar.
4. **Stjórnun.** Áætlunin er mæld og stýrð með gögnum: undirhópasanngirnismælikvarðar, öryggis- og jailbreak-niðurstöður, áfrýjunarmagn og afturköllunarhlutföll, hnekkingarhlutföll eftirlits og fótspor vinnuálags eru rakin gegn grunnlínum og þröskuldum. Rek og ólíkar niðurstöður kalla fram skilgreinda aðgerð og ákvarðanir um fara eða ekki fara hvíla á sönnunargögnum frekar en fullvissu.
5. **Samhæfing.** Ábyrg gervigreind er stöðugt bætt og samþætt um skipulagsheildina: vöktun á sanngirni, öryggi og misnotkun keyrir í framleiðslu, stjórnarhættir eru innbyggðir í afhendingu, umhverfiskostnaður er formlegt inntak í líkanaval og skipulagsheildin aðlagar varnir sínar þegar lög, áhætta og geta breytast, með ábyrgð í höndum allra frekar en eins teymis.

## Hugmyndir til umræðu

- Hvaða sanngirnisskilgreining á við um tiltekna ákvörðun og hver ákveður?
- Hve mikla nákvæmni eða frammistöðu er ásættanlegt að skipta fyrir sanngirni eða túlkanleika?
- Hvað gerir mannlegt eftirlit marktækt frekar en stimpil?
- Hvernig ætti að hanna áfrýjanir gegn sjálfvirkum ákvörðunum til að vera sanngjarnar og tímanlegar?
- Hvernig rauðliðaprófarðu fyrir misnotkun sem þú hefur ekki enn ímyndað þér?
- Ætti umhverfiskostnaður að hafa áhrif á líkanaval og hvernig myndir þú vega hann?

## Helstu atriði

- Traustverð gervigreind er sanngjörn, útskýranleg, ábyrg, örugg og virðir persónuvernd, í hönnun.
- Sanngirni og öryggi eru samfelldir mælinga- og stýringaragar, ekki einskiptis athuganir.
- Samræmdu stjórnarhætti við áhættustýringaramma NIST fyrir gervigreind, gervigreindarreglugerð ESB og ISO/IEC 42001 til að vera verjanlegur og úttektarhæfur.
- Haltu marktæku mannlegu eftirliti, skýrri ábyrgð og raunverulegum áfrýjunarrétti.
- Hannaðu fyrir persónuvernd og gegn misnotkun og taktu tillit til umhverfiskostnaðar.

## Heimildir og frekari lestur

- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- European Union, *Artificial Intelligence Act (Regulation on Artificial Intelligence)*.
- ISO/IEC 42001, *Information technology, Artificial intelligence, Management system*.
- Solon Barocas, Moritz Hardt, and Arvind Narayanan, *Fairness and Machine Learning: Limitations and Opportunities*.
- Christoph Molnar, *Interpretable Machine Learning*.
- Cathy O'Neil, *Weapons of Maths Destruction*.
- Emma Strubell, Ananya Ganesh, and Andrew McCallum, *Energy and Policy Considerations for Deep Learning in NLP*.
