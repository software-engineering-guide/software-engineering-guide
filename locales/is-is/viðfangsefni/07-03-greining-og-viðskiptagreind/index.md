# 7.3 Greining og viðskiptagreind

## Yfirlit og tilgangur

Greining og viðskiptagreind breyta stýrðum, verkfræðilegum gögnum í skilning og aðgerðir. [Viðskiptagreind](https://en.wikipedia.org/wiki/Business_intelligence) (BI) þýðir hefðbundið skýrslugerðina, mælaborðin og sjálfsafgreiðsluverkfærin sem láta fólk sjá hvað er að gerast í rekstrinum. Greining er víðtækari venja að spyrja og svara spurningum með gögnum, frá einföldum lýsingum á fortíðinni til líkana sem mæla með því sem gera skal næst. Saman eru þau hvernig skipulagsheild sér sjálfa sig.

Fyrir stór teymi er þetta lag þar sem gögn vinna annaðhvort fyrir sér eða verða uppspretta ruglings. Þegar þúsundir starfsmanna geta smíðað eigin skýrslur er hættan ekki of litlar upplýsingar heldur of margar andstæðar upplýsingar: þrjú mælaborð sem sýna þrjár ólíkar tekjutölur, hver verjanleg, engin áreiðanleg. Fyrirtæki lifa og deyja á tölunum í stjórnarkynningum og eftirlitsskýrslum. Opinberar stofnanir skila skýrslum til löggjafarþinga, eftirlitsaðila og almennings. Í báðum er mælikvarði sem merkir ólíkt fyrir ólíkt fólk skuld. Graf sem villir um, jafnvel af sakleysi, getur knúið dýrar rangar ákvarðanir eða rýrt traust almennings.

Lykilhugmyndin til að temja þetta í stærð er [merkingarlagið](https://en.wikipedia.org/wiki/Semantic_layer): stýrð, miðlæg skilgreining á mælikvörðum og víddum sem hvert verkfæri og hver skýrsla sækir í, svo „virkur viðskiptavinur“ eða „mánaðartekjur“ séu reiknaðar á einn samþykktan hátt alls staðar. Í kringum þá hugmynd sitja agarnir heiðarleg sjónræn framsetning, yfirveguð mælaborðshönnun og stjórn á sundurleysinu sem sjálfsafgreiðsla framleiðir óhjákvæmilega. Þessi kafli sýnir þér hvernig þú gefur fólki breiðan aðgang að gögnum án þess að gefa upp eina útgáfu sannleikans.

## Meginreglur

- Ein stýrð skilgreining ætti að vera á hverjum mikilvægum mælikvarða, notuð alls staðar.
- Láttu greiningartegundina samsvara spurningunni: lýsa, greina, spá eða mæla fyrir um.
- Sjálfsafgreiðsla er öflug en verður að vera stýrð til að koma í veg fyrir mælikvarðaofvöxt.
- Graf verða að vera heiðarleg. Markmiðið er skilningur, ekki sannfæring með bjögun.
- Mælaborð ættu að knýja ákvarðanir, ekki bara sýna gögn.
- Vottaðu traust efni svo notendur viti á hvað þeir geta treyst.
- Snyrtu og leggðu niður. Fleiri mælaborð er ekki meiri innsýn.
- Felldu greiningu inn þar sem ákvarðanir eru teknar, ekki bara í aðskilda viðskiptagreindargátt.

## Ráðleggingar

### Skildu fjórar tegundir greiningar

Lýsandi greining greinir frá því sem gerðist. Greinandi greining útskýrir hvers vegna það gerðist. [Spágreining](https://en.wikipedia.org/wiki/Predictive_analytics) spáir fyrir um það sem líklegt er að gerist. [Fyrirmælagreining](https://en.wikipedia.org/wiki/Prescriptive_analytics) mælir með því sem gera skal í því. Flestar skipulagsheildir offjárfesta í lýsandi mælaborðum og vanfjárfesta í greiningu og aðgerðum. Ýttu vinnu þinni upp þennan stiga af ásetningi. Paraðu hvern mikilvægan mælikvarða við getuna til að bora í orsakir og tengdu spár við áþreifanlegar ákvarðanir og inngrip. Þannig breytir greining hegðun frekar en bara að lýsa henni.

### Byggðu merkingarlag og stýrðu mælikvörðum

Skilgreindu mælikvarða og víddir einu sinni, í miðlægu merkingarlagi, og láttu hvert viðskiptagreindartól, minnisbók og innfellda skýrslu reikna út frá þeim skilgreiningum. Þetta drepur klassíska vandamálið um ólíkar tölur. Það gerir líka mælikvarðarökfræði útgáfustýrða, prófanlega og rýnanlega. Stýrðu mælikvörðum eins og API: hver vottaður mælikvarði hefur eiganda, skýra skilgreiningu og breytingaskrá. Haltu vottuðum mælikvörðum aðskildum frá tilraunakenndum, svo notendur viti hvað er áreiðanlegt.

### Gerðu sjálfsafgreiðslu mögulega innan varnarrimla

Gefðu greinendum og viðskiptanotendum sjálfsafgreiðsluaðgang til að kanna gögn. Miðlæg viðskiptagreindarteymi geta ekki svarað hverri spurningu og flöskuhálsar ýta fólki bara að töflureiknum. En útvegaðu varnarrimla: valin vottuð gagnasöfn, merkingarlagið fyrir samræmda mælikvarða, sniðmát og þjálfun. Markmiðið er einfalt: láttu auðvelda leiðina nota stýrðar skilgreiningar. Merktu þrep efnis (vottað, stutt af teymi og persónulegt) svo frelsi til að kanna villi ekki fyrir um opinberan sannleika.

### Hannaðu mælaborð fyrir ákvarðanir

Byrjaðu hvert mælaborð á ákvörðuninni sem það styður og áheyrendunum sem taka hana. Leiddu með fáum mælikvörðum sem skipta máli. Útvegaðu samhengi (markmið, þróun, samanburð) svo tölurnar séu túlkanlegar og gerðu borun niður mögulega fyrir greiningu. Stattu gegn freistingunni að troða hverju fáanlegu grafi á eina síðu. Mælaborð sem svarar „erum við á áætlun og ef ekki, hvar á ég að leita?“ er margfalt meira virði en eitt sem sýnir fimmtíu mælikvarða sem enginn bregst við.

### Stundaðu heiðarlega gagnasýn

Veldu grafgerðir sem passa gögnunum: línur fyrir þróun yfir tíma, súlur fyrir samanburð yfir flokka. Forðastu kökurit fyrir allt umfram nokkrar sneiðar. Byrjaðu ása súlurita á núlli, haltu kvörðum samræmdum og forðastu tvöfalda ása sem framleiða falska fylgni. Notaðu lit af ásetningi og aðgengilega, ekki til skrauts. Merktu skýrt og sýndu óvissu þar sem hún skiptir máli. Prófið er einfalt: myndi upplýstur áhorfandi komast að sömu niðurstöðu og gögnin styðja, eða hefur hönnunin ýtt honum í átt að annarri?

### Snyrtu efni og berstu gegn ofvexti

Sjálfsafgreiðsla án snyrtingar framleiðir þúsundir úreltra, tvítekinna og yfirgefinna mælaborða. Komdu á lífsferilsstjórnun: raktu notkun, geymdu ónotað efni í skjalasafni, fjarlægðu tvítök og endurvottaðu það sem eftir er reglulega. Gerðu vottuðu skrána auðfinnanlega, svo fólk endurnýti traust efni frekar en að endurbyggja það. Minna safn traustra, vel viðhaldinna mælaborða slær víðfeðman kirkjugarð.

### Felldu inn greiningu og rekstrarskýrslugerð

Ekki öll greining tilheyrir aðskilinni gátt. Felldu viðeigandi mælikvarða og skýrslur beint inn í rekstrarforritin þar sem fólk vinnur nú þegar, svo sem viðskiptavinakerfið ([CRM](https://en.wikipedia.org/wiki/Customer_relationship_management)), málastjórnunarkerfið eða miðakerfið, svo innsýn berist á ákvörðunarstaðinn. Fyrir rekstrarskýrslugerð með ströngum töfar- eða sniðkröfum (reikninga, yfirlit, eftirlitsskýrslur) skaltu nota sérsmíðaða skýrslugerð. Teygðu ekki gagnvirk mælaborð til að vinna verk sem þau passa illa.

## Málamiðlanir: kostir og gallar

| Val | Kostir | Gallar | Best passun |
|---|---|---|---|
| Miðlægt viðskiptagreindarteymi | Samræmt, stýrt, gæðastýrt | Flöskuháls, hægt að bregðast við | Regluverkuð skýrslugerð |
| Sjálfsafgreiðsluviðskiptagreind | Hröð, skalanleg, valdeflir notendur | Ofvöxtur, ósamræmdir mælikvarðar | Breið könnun |
| Merkingarlag | Einn sannleikur, endurnýtanlegt, stýrt | Líkana- og viðhaldsvinna fyrirfram | Hvaða skipulagsheild sem er umfram smæð |
| Innfelld greining | Innsýn á ákvörðunarstað | Verkfræðikostnaður, erfiðara að stýra | Rekstrarvinnuflæði |
| Auðug mælaborð | Heildstæð sýn | Yfirþyrmandi, lítið hlutfall aðgerða | Sjaldan tilvalin |
| Einbeitt mælaborð | Knýja ákvarðanir | Krefst ritstjórnaragga | Flest notkunartilvik |

Kjarnaspennan er aðgangur gegn samræmi. Að læsa viðskiptagreind inni í miðlægu teymi tryggir samræmdar tölur, en það sveltir skipulagsheildina af tímanlegum svörum og ýtir undir skuggatöflureikna. Full sjálfsafgreiðsla valdeflir alla, en margfaldar andstæða mælikvarða og úrelt efni. Þú þarft ekki að velja hlið. Sameinaðu breiðan sjálfsafgreiðsluaðgang við stýrt merkingarlag og vottun, svo fólk sé frjálst að kanna á meðan mikilvægu tölurnar haldast einar og traustverðar.

## Spurningar til að ræða með teyminu

1. **Hafið þið fjárfest í merkingarlagi og stýrið þið hverjum vottuðum mælikvarða eins og API með eiganda, skilgreiningu og breytingaskrá?** Meginhugmynd kaflans er ein stýrð skilgreining á hverjum mælikvarða sem hvert verkfæri, minnisbók og innfelld skýrsla reiknar út frá, sem drepur klassíska vandamálið um þrjú mælaborð sem sýna þrjár tekjutölur. Fyrir fyrirtæki þar sem stjórnarkynningar og eftirlitsskýrslur hvíla á einni tölu, og fyrir stofnanir þar sem opinberar útgáfur verða að passa við innri tölur, er ólíkur mælikvarði bein skuld. Málamiðlunin er raunveruleg: merkingarlagið krefst líkanavinnu fyrirfram og viðvarandi viðhalds. Komdu með sönnunargögn: teldu hve margar skilgreiningar á mikilvægasta mælikvarðanum ykkar eru til í dag og hvað sátt kostar nú í klukkustundum greinenda. Ef talan er hærri en einn borgar merkingarlagið sig sjálft og að stýra mælikvörðum með eigendum og breytingaskrám heldur því einu með tímanum.

2. **Hvar liggur línan milli sjálfsafgreiðslufrelsis og mælikvarðaofvaxtar og hvaða varnarrimlar halda auðveldu leiðinni stýrðri?** Kaflinn heldur því fram að þú eigir ekki að velja milli læstrar miðlægrar viðskiptagreindar og óheftrar sjálfsafgreiðslu: miðlæg teymi verða flöskuhálsar sem ýta fólki að töflureiknum, á meðan full sjálfsafgreiðsla margfaldar andstæða mælikvarða og úrelt mælaborð. Lausnin er breiður aðgangur ofan á vottuð gagnasöfn, merkingarlagið, sniðmát og skýr efnisþrep (vottað, stutt af teymi, persónulegt) svo könnun villi ekki fyrir um opinberan sannleika. Komdu með áþreifanleg merki: hve mörg mælaborð eru til, hve mörg eru í raun notuð og hvort notendur geti greint traust efni frá tilraunum. Ef fólk getur það ekki ættu vottun og lífsferilsstjórnun (að rekja notkun, geyma ónotað í skjalasafni, endurvotta rest) að verða viðvarandi venja, því minna traust safn slær víðfeðman kirkjugarð.

3. **Eru graf ykkar nógu heiðarleg til að lifa af skoðun og hver athugar að hönnunin styðji niðurstöðuna sem gögnin réttlæta í raun?** Kaflinn setur skýrt próf: myndi upplýstur áhorfandi komast að sömu niðurstöðu og gögnin styðja, eða hefur hönnunin ýtt honum annað? Styttir ásar, tvöfaldir ásar sem framleiða falska fylgni og þrívíð kökurit eru nefndar gildrur. Fyrir opinberar útgáfur til borgara og regluverkaðar skýrslur rýrir sakleysislega villandi graf traust almennings eða býður niðurstöðu, svo heiðarleiki hér er stjórnarhættamál, ekki bara smekkur. Komdu með dæmi þar sem graf í skipulagsheild ykkar villti áheyrendur sína og ákveddu hvort þið þurfið sjónræna staðla (súluása frá núlli, samræmda kvarða, sýnda óvissu) framfylgda á útgefnu efni. Svarið ætti að setja rýniviðmið fyrir allt sem yfirgefur húsið.

4. **Hver af mælaborðum ykkar breyta í raun ákvörðun og hvert er viðmið ykkar til að leggja niður eitt sem gerir það ekki?** Kaflinn krefst þess að mælaborð byrji á ákvörðuninni sem það styður, samt safna flestar stórar skipulagsheildir hégómamælaborðum sem eru horfð á og aldrei brugðist við, ruglað saman við gagnadrifna menningu. Þetta skiptir máli í stærð því hvert mælaborð ber falinn kostnað: það þarf að viðhalda, mælikvarðar þess haldast samræmdir við merkingarlagið og tilvist þess þynnir athygli frá skýrslunum sem knýja aðgerðir. Togið á móti er að fólki finnst öruggara með meira sýnileika og ekkert teymi vill að mælaborð þess sé sett í skjalasafn. Komdu með notkunarmælingar (hver opnar hvert mælaborð, hve oft og hvort nokkur niðurstreymisaðgerð fylgir) og hreinskilinn lista yfir ákvarðanirnar sem helstu mælaborðin þín eiga að upplýsa. Fyrir fyrirtæki nærir þetta eignasafnssnyrtingu og leyfiskostnaðarstýringu. Fyrir opinbera stofnun svarar það líka eftirlitsspurningum um hvort skýrslugerðarútgjöld framleiði mælanlegt rekstrarverðmæti frekar en skjái sem enginn les.

5. **Eruð þið offjárfest í að lýsa fortíðinni þegar verðmætið er í greiningu, spám og fyrirmælum og hvað myndi færa einn lykilmælikvarða upp þann stiga?** Kaflinn setur fram fjórar greiningartegundir (lýsandi, greinandi, spá, fyrirmæli) og varar við því að flestar skipulagsheildir hlaði upp lýsandi mælaborðum á meðan þær vanfjárfesta í greiningunni og aðgerðunum sem breyta niðurstöðum. Fyrir stórt teymi þýðir að sitja fast í lýsingu að greinendur eyða tíma sínum í að endurskýra frá því sem allir vita nú þegar, á meðan erfiðari spurningunni um hvers vegna það gerðist og hvað á að gera næst er ósvarað. Spennan er að greinandi og spávinna krefst dýpri gagnaverkfræði, líkanastjórnunar og greinendafærni, svo auðveldara er að fjármagna enn eitt mælaborð. Komdu með núverandi skiptingu greiningarvinnu ykkar á milli fjögurra tegunda og einn mælikvarða þar sem borun í orsakir eða spá myndi sannanlega breyta ákvörðun. Í fyrirtæki tengir þetta greiningu við framlegð og áhættu. Í opinberri stofnun verður spá- og fyrirmælavinna (til dæmis að spá eftirspurn eftir þjónustu) líka að bera skýranleika- og sanngirnisvarnir áður en hún upplýsir ákvarðanir um borgara.

6. **Hvar þarf innsýn að berast inni í verkfærunum sem fólk vinnur nú þegar í og hvar ættuð þið að nota sérsmíðaða rekstrarskýrslugerð í stað mælaborðs?** Kaflinn aðgreinir gagnvirka viðskiptagreind frá innfelldri greiningu og frá sérsmíðaðri rekstrarskýrslugerð eins og reikningum, yfirlitum og eftirlitsskýrslum, og varar við að teygja mælaborð til að vinna verk sem það passar illa. Þetta skiptir stór teymi máli því framlínustarfsfólk yfirgefur sjaldan viðskiptavinakerfi sitt eða málastjórnunarkerfi til að leita í aðskildri viðskiptagreindargátt, svo innsýn sem býr aðeins í gátt fer ónotuð á ákvörðunarstundinni. Sjónarmiðin á móti eru verkfræðikostnaður og stjórnun: að fella mælikvarða inn í rekstrarforrit er erfiðara að smíða og erfiðara að halda samræmdu við vottaðar skilgreiningar, á meðan pixelnákvæm skýrslugerð krefst strangrar töfar og sniðs sem mælaborðstólið getur ekki tryggt. Komdu með kort af því hvar ákvarðanir eru í raun teknar og hverjar þeirra krefjast nú þess að einhver skipti um verkfæri til að finna töluna. Fyrir fyrirtæki mótar þetta hvar verkfræðivinnu er fjárfest. Fyrir opinbera stofnun hafa lögbundnar skýrslur og yfirlit til borgara oft lagaleg snið- og varðveislureglur sem gera sérsmíðaða skýrslugerð skyldu frekar en valkost.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Skilgreindu fáu kjarnamælikvarðana þína einu sinni, jafnvel í léttu verkfæri, svo stjórnarkynningin og vörumælaborðið séu aldrei ósammála. Slepptu þungum merkingarlagsvettvangi: ein sameiginleg uppspretta skilgreininga og einn stuttur listi traustra mælaborða dugar á meðan teymið er örlítið. Hraði skiptir meira máli en fágun hér, svo kjóstu hýst viðskiptagreindartól sem þú getur beint að vöruhúsinu þínu í dag fram yfir allt sem þú þyrftir að smíða.

**Lítið fyrirtæki.** Án sérstaks viðskiptagreindarsérfræðings skaltu halla þér að greiningu sem er þegar innbyggð í verkfærin sem þú átt, svo sem viðskiptavinakerfið eða bókhaldshugbúnaðinn, frekar en að setja upp aðskilinn vettvang. Rammaðu valið sem kaup gegn smíði og láttu kaup vinna sjálfgefið. Áhættan þín er töflureiknamenning þar sem hver er með ólíka „tekju“-tölu, svo komdu þér saman um fáu skilgreiningarnar sem skipta máli og skrifaðu þær niður. Kjóstu verkfæri sem gera vottaðar skýrslur auðveldar að deila og erfiðar að kvíslast af slysni.

**Stórfyrirtæki.** Kjarnavandinn er samræmi yfir mörg teymi: fjárfestu í stýrðu merkingarlagi, vottaðu traust efni og stýrðu mælaborðaofvexti sem viðvarandi lífsferli með eigendum, notkunarrakningu og endurvottun. Líttu á hvern vottaðan mælikvarða eins og API með skilgreiningu, eiganda og breytingaskrá og aðgreindu vottað efni frá tilraunakenndu svo sjálfsafgreiðsla villi ekki fyrir um opinberan sannleika. Fjárhagsáætlaðu líkana- og snyrtivinnuna skýrt, því í stærð er valkosturinn greinendur sem sætta ólíkar tölur endalaust.

**Hið opinbera.** Útgefnar tölur verða að passa við innri tölur og lifa af opinbera og löggjafarskoðun, svo stýrt merkingarlag og framfylgdir sjónrænir staðlar (ásar frá núlli, heiðarlegir kvarðar, sýnd óvissa) eru ábyrgðarkröfur, ekki fínheit. Innkaupareglur kunna að takmarka hvaða viðskiptagreindartól þú getur keypt og krefjast gagnaflytjanleika, svo forðastu bindingu við séreignarmælikvarðarökfræði eins seljanda. Haltu vottuðum opinberum útgáfum aðskildum frá tilraunagreiningu og gefðu borgurum graf sem eru nógu heiðarleg til að upplýstur áhorfandi komist að niðurstöðunni sem gögnin réttlæta í raun.

## Dæmi

**Sprotafyrirtæki.** Hjá markaðstorgi á frumstigi héldu stofnendurnir tveir hvor sinn töflureikni yfir „mánaðartekjur“ og tölurnar pössuðu aldrei alveg þegar þeir undirbjuggu stjórnarkynninguna. Þeir skilgreindu mælikvarðann einu sinni í litlu merkingarlagi, beindu einu viðskiptagreindartóli að því og merktu einn stuttan lista mælaborða sem þau traustu sem allir ættu að nota. Skýrslugerð breyttist úr sáttargjörð á sunnudagskvöldi í tengil sem þeir gátu opnað af sjálfstrausti.

**Stórfyrirtæki.** Fjarskiptafyrirtæki þjáðist af því að fjármál, markaðssetning og rekstur skýrðu hvert frá ólíkum fjölda „virkra áskrifenda“. Það kynnti merkingarlag sem skilgreinir hvern kjarnamælikvarða einu sinni, flutti mælaborð til að reikna út frá því og vottaði valið safn traustra skýrslna á meðan þúsundir úreltra voru settar í skjalasafn. Stjórnarskýrslugerð hætti að vera sáttaræfing og sjálfsafgreiðsluupptaka jókst því fólk treysti tölunum.

**Hið opinbera.** Lýðheilsudeild smíðaði vottuð mælaborð sem sækja í stýrt merkingarlag, svo tilfellatölur og hlutföll eru reiknuð eins yfir innri ákvarðanatöku og opinberar útgáfur. Sjónrænir staðlar halda grafum sem birt eru borgurum heiðarlegum (ásar frá núlli, skýr óvissubönd), sem ver traust almennings. Innfelldar skýrslur sýna staðbundna mælikvarða inni í málastjórnunarverkfærunum sem framlínustarfsfólk notar nú þegar.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun vel rekinnar greiningar og viðskiptagreindar kemur af hraðari, betri ákvörðunum og af því að skera sóun. Þegar fólk treystir einu mengi talna hætta fundir að vera rifrildi um hvers töflureiknir sé réttur og verða umræður um hvað eigi að gera. Sjálfsafgreiðsla dregur úr biðröðinni hjá miðlægum teymum og merkingarlag kemur í veg fyrir endurtekinn kostnað við að sætta ólíka mælikvarða. Heiðarleg, ákvörðunarmiðuð mælaborð hækka hlutfallið sem innsýn verður að aðgerð.

Upptökukostnaðurinn felur í sér viðskiptagreindarvettvangsleyfi, að smíða og viðhalda merkingarlaginu, snyrtivinnu og þjálfun. Vegðu hann gegn kostnaði þess að taka ekki upp: greinendur og stjórnendur sóa klukkustundum í að sætta andstæðar tölur, ákvarðanir teknar á villandi grafum, uppsafnað óviðhaldið mælaborð og, í opinberu umhverfi, rýrt traust þegar útgefnar tölur stangast á. Til stjórnenda eru rökin einföld. Stýrt merkingarlag auk snyrtrar sjálfsafgreiðslu er munurinn á gögnum sem eign sem allir treysta og viðvarandi uppsprettu ruglings og endurvinnu.

## Andmynstur og gildrur

- Hvert teymi reiknar lykilmælikvarða á sinn hátt, sem framleiðir andstæðar tölur.
- Mælaborð smíðuð til að sýna allt frekar en að styðja ákvörðun.
- Villandi graf (styttir ásar, tvöfaldir ásar, þrívíð kökurit) sem bjaga niðurstöður.
- Að líta á sjálfsafgreiðslu sem staðgengil stjórnunar frekar en viðbót við hana.
- Þúsundir úreltra, tvítekinna mælaborða án lífsferilsstjórnunar.
- Hégómamælaborð sem enginn bregst við, ruglað saman við gagnadrifna menningu.
- Að teygja gagnvirka viðskiptagreind til að framleiða pixelnákvæm eftirlitsskjöl.
- Engin vottun, svo notendur geta ekki greint traust efni frá tilraunum.

## Þroskalíkan

1. **Upphaf.** Skýrslur eru smíðaðar ad hoc í töflureiknum, mælikvarðar skilgreindir ósamræmt og graf oft villandi. Ekkert merkingarlag, engin vottun og engin snyrting, svo ólíkar tölur eru normið.
2. **Þróun.** Viðskiptagreindartól er til staðar með nokkrum sameiginlegum mælaborðum, en mælikvarðaskilgreiningar eru enn ólíkar milli teyma. Sjálfsafgreiðsla er óstýrð og ofvöxtur byrjar. Fáeinir hópar kunna að líkana mælikvarða vandlega, en venjan er ósamræmd og ekkert er framfylgt um skipulagsheildina.
3. **Stöðlun.** Merkingarlag skilgreinir kjarnamælikvarða einu sinni, skjalfest og framfylgt yfir hvert verkfæri og hverja skýrslu. Vottað efni er aðgreint frá tilraunakenndu, sjálfsafgreiðsla starfar innan varnarrimla, sjónrænir staðlar eru birtir og lífsferilsstjórnun efnis er viðvarandi venja frekar en stöku hreinsun.
4. **Stjórnun.** Greiningarlandareignin er mæld gegn grunnlínum. Mælaborðanotkun er rakin og ónotað efni magnsett og lagt niður á takti. Fjöldi ólíkra skilgreininga á lykilmælikvörðum er vaktaður í átt að einni. Samræmi við grafarýni, sjálfsafgreiðsluupptaka og tími til svars eru rakin og sáttarkostnaður og leiðtími mælikvarðabreytinga mæld, svo rek frá vottuðum skilgreiningum sé gripið og leiðrétt á sönnunargögnum.
5. **Samhæfing.** Mælikvörðum er stýrt eins og API með eigendum og breytingaskrám, greining spannar lýsandi til fyrirmæla og tengist áþreifanlegum aðgerðum og skýrslur eru felldar inn á ákvörðunarstöðum. Skipulagsheildin treystir einni útgáfu sannleikans alls staðar, heftir ofvöxt virkt og endurmarkar og endurvottar greiningu sína stöðugt þegar reksturinn og spurningar hans breytast.

## Hugmyndir til umræðu

- Hve margar ólíkar skilgreiningar á mikilvægasta mælikvarða ykkar eru til í dag?
- Hver af mælaborðum ykkar breyta í raun ákvörðun og hver eru bara horft á?
- Hvar hefur graf í skipulagsheild ykkar villt áheyrendur sína, af sakleysi eða ekki?
- Eruð þið offjárfest í að lýsa fortíðinni samanborið við að greina og bregðast við?
- Hvað myndi vottunarþrep fyrir efni gera fyrir traust og endurnotkun í skipulagsheild ykkar?
- Hvernig jafnvægið þið þörf borgara eða eftirlitsaðila fyrir heiðarleg graf við togið í átt að sannfærandi?

## Helstu atriði

- Skilgreindu hvern mikilvægan mælikvarða einu sinni í stýrðu merkingarlagi notuðu alls staðar.
- Ýttu greiningu upp stigann frá lýsandi til greinandi, spár og fyrirmæla.
- Gerðu sjálfsafgreiðslu mögulega innan varnarrimla. Vottaðu traust efni.
- Hannaðu mælaborð í kringum ákvarðanir, ekki í kringum fáanleg gögn.
- Gerðu hvert graf heiðarlegt. Markmiðið er skilningur, ekki sannfæring.
- Snyrtu miskunnarlaust og leggðu niður úrelt efni til að berjast gegn ofvexti.
- Felldu greiningu inn á ákvörðunarstað og notaðu sérsmíðaða rekstrarskýrslugerð.

## Heimildir og frekari lestur

- Edward Tufte, "The Visual Display of Quantitative Information."
- Stephen Few, "Show Me the Numbers" and "Information Dashboard Design."
- Cole Nussbaumer Knaflic, "Storytelling with Data."
- Alberto Cairo, "How Charts Lie."
- Ralph Kimball and Margy Ross, "The Data Warehouse Toolkit."
- Darrell Huff, "How to Lie with Statistics."
- Benn Stancil and others, writings on the semantic layer and metrics stores.
