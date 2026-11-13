# 2.16 Afkastaverkfræði

## Yfirlit og tilgangur

Afkastaverkfræði er handverkið að gera kóða nógu hraðan, af ásetningi, með mælingu í stað innsæis. Þessi kafli starfar á stigi kóða og íhluta: aðgerða, lykkja, gagnagerða, fyrirspurna, minnisúthlutana og þess hvernig ein þjónusta ver tíma sínum. Hann er systurkafli kafla 3.5, sem fjallar um afköst á kerfisstigi (að skala út, álagsdreifingu, afkastagetu og seiglu). Þegar kerfi er hægt spyr kafli 3.5 hve margar vélar þú þarft. Þessi kafli spyr hvers vegna ein vél er að vinna svona mikið í fyrsta lagi. Þú þarft venjulega hvort tveggja, og kóðastigssýnin er þar sem undrandi mikill kostnaður og töf felast í raun.

Fyrir stór teymi skiptir þessi agi máli því afköst rýrna hljóðlega. Engin ein breyting gerir þjónustu hæga, en þúsund smáar gera það, hver með því að bæta við gagnagrunnskalli eða ótakmarkaðri lykkju. Án sameiginlegrar aðferðar til að mæla, fjárhagsáætla og hliða afköst uppgötvarðu rotnunina aðeins þegar viðskiptavinur kvartar eða útgáfa bráðnar. Aðferð breytir afköstum úr hetjulegu slökkvistarfi í venjulegan eiginleika sem þú verndar.

Fyrir fyrirtæki eru afköst peningar: hraðari kóði þýðir færri vélar, lægri skýjareikninga og getu til að standast [þjónustustigssamning](https://en.wikipedia.org/wiki/Service-level_agreement) (SLA) um töf án ofúthlutunar. Fyrir hið opinbera eru afköst aðgengi: síða sem hleðst á gömlum síma yfir veika farsímatengingu er munurinn á því að borgari ljúki bótakröfu og gefist upp. Opinber kerfi þurfa líka endurgeranleg viðmiðunarsönnunargögn, því innkaupa- og eftirlitsstofnanir munu biðja þig að sanna tölurnar, ekki bara fullyrða þær.

## Meginreglur

- **Mældu áður en þú fínstillir.** Flöskuhálsinn er næstum aldrei þar sem þú giskar. Greindu, bregstu síðan við.
- **Forðastu ótímabæra fínstillingu.** Viðvörun Donalds Knuth gildir: að fínstilla kóða sem skiptir ekki máli kostar skýrleika og kaupir ekkert.
- **Skilgreindu „nógu hratt“ sem tölu.** Afkastafjárhagsáætlun með markmiði og hundraðshluta breytir skoðun í staðist eða fallið.
- **Meðaltöl ljúga, hundraðshlutar segja sannleikann.** Halinn (p99) er það sem notendur finna, ekki meðaltalið.
- **Reikniritasigrar slá örfínstillingu.** Betri flækjuflokkur slær hvaða fastastuðulssnilld sem er.
- **Töf og afköst eru ólík markmið.** Að bæta annað getur versnað hitt. Vittu hvað þú ert að kaupa.
- **Viðmiðaðu af heiðarleika eða alls ekki.** Upphitun, dreifni og dæmigert vinnuálag aðskilja raunverulegar tölur frá skáldskap.
- **Hliðaðu afköst í CI, fylgstu með þeim í framleiðslu.** Afturfarir gripnar fyrir sameiningu eru ódýrar. Gripnar af notendum, dýrar.

## Ráðleggingar

### Mældu fyrst og greindu áður en þú snertir línu

Elsta reglan á þessu sviði er sú sem er mest hunsuð: finndu flöskuhálsinn áður en þú fínstillir. Náðu í [greini](https://en.wikipedia.org/wiki/Profiling_(computer_programming)), verkfæri sem tekur sýni eða mælir keyrandi forrit til að sýna hvar það eyðir tíma og minni. Greindu örgjörva (hvaða aðgerðir brenna lotum), minni og úthlutun (hvað er úthlutað og hve oft, þar sem úthlutunarvelta knýr sorphirðuhlé) og I/O (tími sem fer í bið eftir diski, neti eða gagnagrunni). [Logagraf](https://en.wikipedia.org/wiki/Flame_graph), staflað sjónræn framsetning þar sem hver kassi er aðgerð og breidd hans er tími, gerir ráðandi kostnaðinn augljósan í fljótu bragði: leitaðu að breiðustu kössunum, ekki dýpstu stöflunum. Fínstilltu stærsta kostnaðinn fyrst, mældu aftur og stoppaðu þegar þú nærð fjárhagsáætluninni. Þetta tengist sýnileikavenjum kafla 9.2, því framleiðslugreining slær hverja ágiskun gerða á fartölvu.

Gættu þín líka gegn andstæðu mistökunum. Heil lína Knuths er að ótímabær fínstilling sé rót mikils ills, og hann átti við smáu óhagkvæmnina sem freista þín til að fórna læsilegum kóða fyrir ímyndaðan hraða. Skrifaðu skýru útgáfuna fyrst, mældu og fínstilltu aðeins kóðann sem greinirinn ákærir.

### Skilgreindu hvað „nógu hratt“ þýðir með afkastafjárhagsáætlunum

Hraði er ekki dyggð í óhlutbundnu: hann er markmið sem þú nærð eða missir af. Settu **afkastafjárhagsáætlun**: áþreifanleg mörk eins og „p99 afgreiðslutöf undir 300 ms“ eða „þessi endapunktur úthlutar undir 1 MB á beiðni“. Tengdu hana við eitthvað sem notendur eða viðskiptin finna og settu hana fram sem **hundraðshluta**, ekki meðaltal, því meðaltalið felur hæga halann þar sem raunverulegir notendur búa. Ef 1% beiðna taka 5 sekúndur getur meðaltal þitt litið vel út á meðan marktækur hluti viðskiptavina þjáist. Fjárhagsáætlanir gefa teymi sameiginlega, óumdeilanlega skilgreiningu á „búið“ og línu sem afturför fer sýnilega yfir.

### Náðu í reikniritaskilvirkni áður en þú örfínstillir

Stærstu, ódýrustu sigrarnir koma frá [reikniritaskilvirkni](https://en.wikipedia.org/wiki/Algorithmic_efficiency), hvernig vinnan vex þegar inntakið vex, lýst með [Big O-ritháttum](https://en.wikipedia.org/wiki/Big_O_notation) (leið til að flokka vaxtarhraða, svo O(n log n) röðun skalar mun betur en O(n í öðru veldi)). Hreiðruð lykkja sem er ósýnileg við tíu atriði verður stórslys við tíu þúsund. Áður en þú handstillir heita aðgerð skaltu spyrja hvort hún geri í grundvallaratriðum of mikla vinnu: óviljandi N+1 fyrirspurn, línuleg skönnun sem ætti að vera hakkatöfluuppflétting eða endurtekin vinna sem mætti muna. Þetta tengist reikniritaundirstöðunum í kafla 2.13. Engin fastastuðulsstilling bjargar röngum flækjuflokki.

### Greindu töf frá afköstum og virtu halann

**Töf** er hve lengi ein aðgerð tekur. **Afköst** (throughput) eru hve margar aðgerðir ljúka á tímaeiningu. Þetta eru ekki sama markmiðið og að fínstilla annað getur skaðað hitt. Lotun bætir afköst en bætir töf við fyrsta atriðið í lotunni. Að bæta við samhliða vinnuþrælum eykur afköst en getur versnað halatöf með samkeppni. Ákveddu hvort notendur þínir þurfa í raun. Og fylgstu alltaf með halanum: p95 og p99 töf, hægustu 5% og 1% beiðna, því í stórum stíl gerir notandi margar beiðnir og lendir oft í halanum. Skýrðu frá hundraðshlutum, vektu á þeim og fjárhagsáætlaðu fyrir þá.

### Þekktu mörk hliðrunar

Þegar þú hliðrar skaltu muna [lögmál Amdahls](https://en.wikipedia.org/wiki/Amdahl%27s_law): hröðunin af því að bæta við örgjörvum er takmörkuð af broti vinnunnar sem verður að keyra í röð. Ef 10% verks eru í eðli sínu raðbundin kemur enginn fjöldi kjarna þér fram yfir 10x hröðun. Samtími (að skipuleggja vinnu svo verkefni geti þokast sjálfstætt) og hliðrun (að keyra þau í raun á sama tíma) bæta við raunverulegri flækju, frá kappakstursástandi til samhæfingaryfirbyggingar. Mældu raðbundna brotið áður en þú gerir ráð fyrir að fleiri þræðir bjargi þér og vertu heiðarlegur um að einfaldasta rétta útgáfan er oft nógu hröð.

### Notaðu skyndiminni og gagnastaðsetningu og virtu kostnað þeirra

[Skyndiminni](https://en.wikipedia.org/wiki/Cache_(computing)), hröð geymsla nýlegra eða dýrt reiknaðra niðurstaðna, er öflugasta afkastaverkfærið sem þú átt og það hættulegasta. Skot Phils Karlton um að erfiðu vandamálin tvö í tölvunarfræði séu ógilding skyndiminnis og nafngiftir er viðvörun: úrelt skyndiminni þjónar röngum svörum og ógildingarrökfræði er þar sem lúmskir gallar fæðast. Geymdu í skyndiminni af ásetningi, settu fyrningartíma og þekktu réttleikasöguna þína áður en þú fínstillir hittihlutfallið. Á lægsta stigi nýtir [staðsetning tilvísana](https://en.wikipedia.org/wiki/Locality_of_reference), að halda gögnum sem eru notuð saman nálægt hvert öðru í minni, skyndiminnisstigveldi örgjörvans og getur gert kóða nokkrum sinnum hraðari án reikniritabreytinga, með því að breyta skyndiminnismissum í hitti. Samfelld fylki slá bendilseltingar gerðir af þessari ástæðu. Þetta sker gagnaskipulagsval í kafla 3.4.

### Viðmiðaðu af heiðarleika og vantreystu örviðmiðum

Viðmið sem lýgur er verra en ekkert, því það gefur falskt sjálfstraust. Hitaðu upp áður en þú mælir, svo þú tímasetjir stöðugt ástand frekar en einskiptis ræsingu og tímabundna þýðingu (just-in-time). Keyrðu margar endurtekningar og skýrðu frá dreifni, ekki einni heppinni tölu. Notaðu dæmigert vinnuálag með raunhæfum gagnastærðum og dreifingum, því örviðmið á leikfangainntaki mælir oft getu þýðandans til að eyða prófinu þínu frekar en raunverulegan hraða kóðans. Gættu þín á klassísku gildrunum: gildi sem fínstillirinn sannar ónotað og fjarlægir, lykkja sem keyrslutíminn hífir eða skyndiminni sem er heitt í viðmiðinu og kalt í framleiðslu. Þegar þú ert í vafa skaltu mæla alla leiðina, ekki einangruðu aðgerðina.

### Hliðaðu afköst í CI og fylgstu með þeim í framleiðslu

Gerðu afköst að eiginleika sem leiðslan verndar. Bættu afkastaprófum við stefnu kafla 2.4, með afturfarahliðum sem láta smíðina mistakast þegar lykilviðmið eða fjárhagsáætlun versnar umfram þröskuld. Þetta grípur hæga skriðið fyrir sameiningu. Lokaðu síðan lykkjunni í framleiðslu með fjarmælingum kafla 9.2: rektu raunverulega töfarhundraðshluta, úthlutunartíðni og hægar fyrirspurnir gegn fjárhagsáætlunum þínum, því framleiðsluumferð finnur tilvikin sem viðmið þín ímynduðu sér aldrei.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
|---|---|---|
| Fínstilla núna, byggt á innsæi | Finnst afkastamikið, stöku heppinn sigur | Stillir venjulega rangan kóða, bætir við flækju fyrir engan ávinning |
| Mæla fyrst, fínstilla síðan | Beinist að raunverulegum flöskuhálsi, gagnabyggt | Krefst verkfæra og aga, hægara að byrja |
| Skyndiminni | Mikill töf- og afkastaávinningur | Ógildingargallar, úrelt gögn, minniskostnaður |
| Meiri hliðrun | Meiri afköst á hliðrunarhæfri vinnu | Amdahl-loft, samkeppni, samtímagallar |
| Örfínstilling | Kreistir fastastuðla | Lítið loft, skaðar læsileika, oft suð |
| Reikniritabót | Sigrar skala með inntaksstærð | Krefst greiningar, stundum stærri endurskrif |
| CI-afkastahlið | Stöðvar afturfarir snemma og ódýrt | Óáreiðanleg viðmið tæra traust, þarf stöðugt umhverfi |

Meginspennan er fyrirhöfn gegn ávinningi og lausnin er mæling. Afkastavinna hefur skarpt minnkandi ávöxtun: fyrsta greinastýrða lagfæringin gæti helmingað töf, sú tíunda gæti rakað af prósentu á meðan hún tvöfaldar kóðaflækju. Þú leysir þetta með því að neita að fínstilla án tölu í hendi og fjárhagsáætlunar til að ná. Mældu til að finna lagfæringuna sem er þess virði að gera og stoppaðu um leið og þú hreinsar fjárhagsáætlunina frekar en að elta hraða í sjálfum sér.

## Spurningar til að ræða með teyminu

1. **Hefurðu skriflega afkastafjárhagsáætlun fyrir mikilvægar leiðir þínar og er hún sett fram sem hundraðshluti?** Mörg teymi hafa óljósa tilfinningu fyrir að hlutir ættu að vera „hraðir“ en enga tölu sem nokkur gæti fallið gegn, sem þýðir að afköst eru verk enginn þar til þau brotna. Fjárhagsáætlun eins og „p99 undir 300 ms“ gerir markmiðið áþreifanlegt, gefur rýnum eitthvað til að framfylgja og breytir afturför í sýnilegan atburð frekar en hæga skrið. Þetta skiptir mestu í stórum teymum, þar sem töf læðist inn gegnum margar hendur og enginn einn höfundur sér samanlagðan kostnað. Komdu með núverandi tafargögn þín og spurðu hvort þú skýrir frá meðaltölum, sem smjaðra fyrir þér, eða hundraðshlutum, sem segja sannleikann. Ef þú getur ekki sagt hvað „nógu hratt“ þýðir sem tölu er það fyrsta sem þarf að laga.

2. **Þegar þú fínstilltir eitthvað síðast, sagði greinir þér hvar þú ættir að leita, eða giskaðirðu?** Flöskuhálsinn er alræmt einhvers staðar annars staðar en reyndir verkfræðingar búast við, og tími sem fer í að stilla rangan kóða er tapaður tvisvar, einu sinni í vinnunni og einu sinni í viðbættri flækju. Menning sem greinir fyrst eyðir fyrirhöfn þar sem hún borgar sig og lætur skýran kóða í friði. Biddu teymið að rifja upp síðustu þrjár afkastalagfæringar og hvort hver byrjaði á mælingu eða grun. Íhugaðu hvort þú getir greint í framleiðslu, eða raunhæfu sviðsetningarumhverfi, því greining á fartölvu getur villt illa. Svarið afhjúpar hvort afkastavinna þín er verkfræði eða þjóðtrú.

3. **Hvað stöðvar afkastaafturför frá því að ná framleiðslu í dag?** Í vaxandi teymi er heiðarlega svarið oft „kvörtun viðskiptavinar“, sem þýðir að notendur eru afturfaraprófið þitt. CI-hlið sem lætur smíðina mistakast þegar viðmið eða fjárhagsáætlun versnar grípur vandamálið meðan það er ódýrt að laga og höfundurinn man enn breytinguna. Ræddu hvort viðmið þín séu nógu stöðug til að hliða á, því óáreiðanlegt afkastapróf sem æpir úlfur verður hunsað eða afvirkjað. Talaðu líka um hvað þú fylgist með í framleiðslu, því sumar afturfarir birtast aðeins undir raunverulegri umferð og gögnum. Markmiðið er að gera afköst að eiginleika sem kerfið ver sjálfvirkt, ekki einn sem þú enduruppgötvar í atviki.

4. **Fínstillirðu fyrir töf eða afköst á hverri mikilvægri leið og hefur nokkur skrifað það val niður?** Þetta eru ólík markmið sem toga í gagnstæðar áttir: lotun og samhliða vinnuþrælar lyfta afköstum en geta bætt töf við einstakar beiðnir, svo teymi sem fínstillir af innsæi kaupir oft rangan ás og lætur notendur bíða til að spara vélartíma sem enginn skorti. Í stóru teymi margfaldast hættan, því einn hópur stillir sameiginlega þjónustu fyrir magnafköst á meðan annar reiðir sig á hana fyrir gagnvirka töf, og hvorugur þekkir markmið hins. Komdu með raunverulegt notkunarmynstur hverrar leiðar (gagnvirk beiðni á móti bakgrunnslotu), núverandi hundraðshlutatöf og viðvarandi afköst sem þú þarft, ákveddu síðan ásinn skýrt frekar en að leyfa sjálfgefnu að birtast. Fyrir fyrirtækja- eða opinbert kerfi undir SLA skaltu nefna hvaða mælikvarða samningurinn er skrifaður gegn, því að fínstilla ómælda ásinn getur brotið samning á meðan mælaborð þín líta heilbrigð út.

5. **Hvernig veistu að viðmið þín mæla raunverulega vinnu frekar en fínstillirinn að eyða prófinu þínu?** Viðmið sem lýgur er verra en ekkert, því það réttir teyminu falskt sjálfstraust og afturför er síðan afhent samt. Teymi skýra reglulega frá einni heppinni tölu úr köldu keyrslu á leikfangainntaki, sem mælir ræsingu, tímabundna þýðingu og getu þýðandans til að fjarlægja ónotaðan kóða frekar en hegðunina sem notendur lenda í í raun. Komdu með dæmi um viðmið og yfirheyrðu það: hitar það upp, keyrir margar endurtekningar, skýrir frá dreifni, notar dæmigerðar gagnastærðir og dreifingar og sigrar dauðakóðaeyðingu á niðurstöðu sinni. Togið á móti er að heiðarleg viðmið eru hægari að skrifa og keyra en fljótleg örviðmið, svo komdu þér saman um hvar ódýrar nálganir eru ásættanlegar og hvar þú krefst nákvæmni. Í opinberu eða eftirlitsskyldu umhverfi þar sem innkaupa- og eftirlitsstofnanir munu biðja þig að endurskapa tölurnar skaltu fanga tækið, vinnuálagið og umhverfið ásamt niðurstöðunni svo hægt sé að sannreyna fullyrðinguna frekar en bara fullyrða hana.

6. **Þegar afkastavinna keppir við eiginleika um sömu verkfræðingana, hvernig ákveðurðu og hver hefur fjárhagsáætlunarvaldið?** Afköst hafa skarpt minnkandi ávöxtun, svo fyrsta greinastýrða lagfæringin gæti helmingað töf á meðan sú tíunda rakar af prósentu fyrir tvöfalda kóðaflækju, og án reglu vinnur háværasta röddin eða næsti frestur. Sjónarmiðin sem togast á eru raunveruleg: ólöguð afkastaskuld safnast hljóðlega og verður dýrari að eftirbæta, en samt sveltir að elta hraða framhjá fjárhagsáætluninni vegvísinn og bætir við flækju sem hægir á framtíðarvinnu. Komdu með núverandi fjárhagsáætlunarstöðu fyrir hverja mikilvæga leið, áætlaðan kostnað óbreytts ástands í vélum eða týndri umbreytingu og jaðarávinning næstu fínstillingar, svo málamiðlunin sé gerð á sönnunargögnum en ekki þrýstingi. Fyrir stórt fyrirtæki eða opinbera áætlun skaltu nefna hver á afkastafjárhagsáætlunina og hver getur heimilað verkfræðitíma gegn henni, því markmið sem enginn er ábyrgur fyrir að verja er markmið sem hljóðlega rýrnar.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Afhendingarhraði slær ferli, svo standa gegn endurskrifum og stóra afkasta­ramma. Eyddu einum eftirmiðdegi með greini á leiðinni sem notendur kvarta í raun yfir, lagaðu stærsta kostnaðinn (oft N+1 fyrirspurn eða óviljandi línulega skönnun) og bættu einni léttri hundraðshlutafjárhagsáætlun við CI svo sigurinn geti ekki hljóðlega afturförast. Taktu frá djúpa fínstillingu fyrir augnablikið þegar raunveruleg tala, ekki grunur, segir að kóðinn sé of hægur.

**Lítið fyrirtæki.** Án afkastasérfræðings og með þröngt fjárhagsáætlun skaltu hallast að verkfærunum sem þú borgar nú þegar fyrir: greininum í keyrsluumhverfi þínu, töfarhundraðshlutunum í hýsingarmælaborðinu og innbyggða fyrirspurnagreinanda gagnagrunnsins. Settu eina eða tvær einfaldar fjárhagsáætlanir tengdar einhverju sem viðskiptavinir finna, eins og síðuhleðslu- eða afgreiðslutíma, og líttu á brot sem merki um að kaupa hraðara þrep eða laga verstu fyrirspurnina frekar en að ræsa stillingarverkefni sem þú getur ekki mannað.

**Stórfyrirtæki.** Í flotastærð eru afköst beinn kostnaður, svo stýrðu þeim sem sameiginlegum aga: staðlað greiningarverkfæri, hundraðshlutafjárhagsáætlanir tengdar viðskiptamælikvörðum og CI-afturfarahlið beitt samræmt svo hæga skrið neins eins teymis blási ekki upp allan skýjareikninginn. Rektu töf, úthlutun og afköst gegn grunnlínum yfir þjónustur og haltu endurgeranlegum viðmiðunarsönnunargögnum, því 30% örgjörvaminnkun á stórum flota er endurtekinn sparnaður sem vert er að úttekta og verja gegn SLA-viðurlögum.

**Hið opinbera.** Afköst eru aðgengisábyrgð: síða sem hleðst á gömlum síma yfir veika tengingu ákvarðar hvort borgari ljúki bótakröfu. Settu skýrar fjárhagsáætlanir gegn raunhæfum lágendatækjum og þrengdum netum og birtu endurgeranlegar viðmiðunarniðurstöður sem fanga tækið, netið og vinnuálagið, svo innkaupa- og eftirlitsstofnanir geti sannreynt tölurnar frekar en tekið þær á trú. Kjóstu gagnsæja, úttektarhæfa mælingu fram yfir fullyrðingar söluaðila og haltu birgjum við sömu endurgeranlegu sönnunargögnin.

## Dæmi

**Sprotafyrirtæki.** Lítið SaaS-teymi tekur eftir að mælaborð þeirra er sljótt og freistast til að endurskrifa það í hraðari ramma. Í staðinn verja þeir eftirmiðdegi með greini og logagrafi, sem sýnir að 70% beiðnitímans er einn endapunktur sem gefur út eina gagnagrunnsfyrirspurn á hverja röð, klassíska N+1 mynstrið. Þeir skipta því út fyrir eina lotuðu fyrirspurn, töf fellur úr 1,2 sekúndum í 90 millisekúndur og þeir bæta p99 fjárhagsáætlun upp á 200 ms við létt CI-viðmið svo lagfæringin geti ekki hljóðlega afturförast. Engin endurskrif, einn eftirmiðdagur, tífaldur sigur.

**Stórfyrirtæki.** Verslunarvettvangur rekur þúsundir tilvika og skýjareikningur hans er ráðinn af einni meðmælaþjónustu. Greiningarátak finnur mikla úthlutunarveltu sem veldur tíðum sorphirðuhléum, auk skyndiminnis með lélegt hittihlutfall. Að stilla gagnagerðir fyrir staðsetningu og laga skyndiminnislyklana sker örgjörva á hverja beiðni um 40%, sem leyfir teyminu að keyra sömu umferð á 40% færri vélum. Sparnaðurinn borgar verkfræðifyrirhöfnina á vikum og p99 töfar-SLA sem var stundum brotinn heldur nú þægilega, sem forðast samningsviðurlög.

**Hið opinbera.** Landsbundið skattayfirvald verður að þjóna borgurum á gömlum tækjum og hægum sveitatengingum. Teymið setur skýra fjárhagsáætlun: framtalssíðan verður að vera gagnvirk á innan við 3 sekúndum á lágendasíma yfir þrengdan 3G-prófíl. Þeir greina síðuna, skera vinnuna sem hindrar gagnvirkni og birta endurgeranlegar viðmiðunarniðurstöður, fanga tækið, netið og vinnuálagið, svo eftirlitsstofnanir og aðgengisendurskoðendur geti sannreynt fullyrðinguna frekar en tekið hana á trú. Afköst hér eru ekki kostnaðarstýritæki heldur aðgengisábyrgð sem heldur þjónustunni nothæfri fyrir alla.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun afkastaverkfræði birtist í þremur bókum. Sú fyrsta er innviðakostnaður: hraðari kóði vinnur sama verk á færri vélum, og fyrir stóran flota er 30% örgjörvaminnkun beinn, endurtekinn sparnaður sem dvergar einskiptis verkfræðifyrirhöfn. Önnur er tekjur og ánægja: töf fylgir umbreytingu, brottfalli og trausti notenda, svo að raka af halanum er vaxtartæki, ekki bara hreinlætisverk. Þriðja er forðuð áhætta: SLA-brot ber viðurlög, og útgáfa sem bráðnar undir álagi ber orðsporsskaða og slökkvistarfskostnað.

Heildareignarkostnaðurinn er hóflegur og fyrirfram hlaðinn. Þú fjárfestir í greiningarverkfærum, stöðugu viðmiðunarumhverfi og CI-hliðum, auk agans til að skrifa fjárhagsáætlanir og lesa greiningar. Stærri, falinn kostnaðurinn er valkosturinn: afkastaskuld safnast hljóðlega, og að eftirbæta hraða í hægt kerfi eftir útgáfu er miklu dýrara en að vernda hann stöðugt. Færðu rök við forystu í hennar eigin einingum. Þýddu töf í umbreytingu eða lokahlutfall borgara, þýddu örgjörva í mánaðarlegan skýjakostnað og þýddu afturfarahlið í forðuð atvik. Sterkustu rökin eru að afköst eru ódýr að vernda commit fyrir commit og rústandi að endurheimta eftir að þau hafa rotnað.

## Andmynstur og gildrur

- **Fínstilling án greiningar.** Að stilla kóða sem er ekki flöskuhálsinn á meðan raunverulegi kostnaðurinn er snertur ekki.
- **Ótímabær fínstilling.** Að fórna skýrleika fyrir ímyndaðan hraða sem greinirinn hefði aldrei merkt.
- **Að skýra frá meðaltölum.** Að fela sársaukafullan hala á bak við þægilegt meðaltal. Notendur finna p99, ekki meðaltalið.
- **Örviðmiðaleikhús.** Tölur úr leikfangavinnuálagi sem fínstillirinn eyddi til hálfs, án upphitunar eða dreifni.
- **Skyndiminni án ógildingarsögu.** Að elta hittihlutfall á meðan úrelt eða röng gögn eru þjónuð.
- **Að gera ráð fyrir að fleiri þræðir hjálpi.** Að hunsa lögmál Amdahls og raðbundna brotið og drukkna síðan í samkeppni.
- **Ekkert afturfarahlið.** Að láta notendur vera afkastaprófið því ekkert í CI ver fjárhagsáætlunina.
- **Að fínstilla ranga ásinn.** Að kaupa afköst með lotun þegar notendur þurftu litla töf, eða öfugt.

## Þroskalíkan

- **Stig 1, Upphaf:** Afköst eru aðeins tekin fyrir þegar eitthvað brotnar. Engar fjárhagsáætlanir, engin greiningarvenja, engin viðmið. Fínstilling er ágiskun knúin af innsæi og meðaltöl eru eini mælikvarðinn sem nokkur skýrir frá.
- **Stig 2, Þróun:** Sum teymi greina við atvik og halda nokkrum viðmiðum, en vinnubrögðin eru ósamkvæm og veltast á áhuga einstaklinga. Fjárhagsáætlanir eru til óformlega fyrir eina eða tvær mikilvægar leiðir og hundraðshlutar birtast á sumum mælaborðum, en ekkert hliðar afturför fyrir afhendingu og hvert teymi finnur upp sína eigin nálgun.
- **Stig 3, Stöðlun:** Mikilvægar leiðir bera skriflegar hundraðshlutafjárhagsáætlanir og greining er skjalfest, væntanlegt fyrsta skref áður en nokkur fínstillir. CI inniheldur afkastapróf með afturfarahliðum, heiðarlegar viðmiðunarreglur (upphitun, dreifni, dæmigerð gögn) eru skrifaðar niður og framfylgt um alla skipulagsheildina og hvert teymi fylgir sömu aðferð frekar en sinni eigin.
- **Stig 4, Stjórnun:** Skipulagsheildin mælir afköst sem stýrðan eiginleika. Töfarhundraðshlutar, afköst, úthlutunartíðni og hægfara fyrirspurnatalningar eru raktar gegn skýrum grunnlínum í framleiðslu og CI, afturfarir eru magngreindar gegn þröskuldum frekar en rökræddar og fjárhagsáætlanir eru tengdar viðskiptamælikvörðum eins og umbreytingu eða skýjakostnaði svo brot kalli fram gagnabyggða ákvörðun. Viðmiðunarsönnunargögn eru endurgeranleg og fönguð með tæki, vinnuálagi og umhverfi til úttektar.
- **Stig 5, Samhæfing:** Afköst eru stöðugt bætt og samþætt um skipulagsheildina. Fjárhagsáætlanir, greining, heiðarleg viðmið og logagrafsgreining eru venjuleg færni, afturfarahlið eru stöðug og treyst og framleiðslu- og CI-gögn loka lykkjunni sjálfvirkt. Skipulagsheildin aðlagar fjárhagsáætlanir eftir því sem umferð, vélbúnaður og viðskiptaforgangsröðun breytast, endurjafnar fyrirhöfn í átt að leiðunum þar sem ávinningur er mestur og ver afköst sem varanlegan eiginleika frekar en tímabundið átak.

## Hugmyndir til umræðu

1. Hverjar af mikilvægum leiðum þínum hafa skriflega, hundraðshlutabyggða fjárhagsáætlun í dag og hverjar eru varðar aðeins af von?
2. Hvenær kom greinir þér síðast á óvart og hvað kenndi það þér um hvar þú gerir ráð fyrir að tíminn fari?
3. Hita viðmið þín upp, skýra frá dreifni og nota dæmigerð gögn, eða eru þau að mæla fínstillirinn?
4. Hvar ertu að eyða vélum til að breiða yfir kóða sem greiningarátak gæti gert ódýrari?
5. Fyrir mest hliðraða vinnuálagið þitt, hvert er raðbundna brotið og takmarkar lögmál Amdahls hröðunina sem þú eltir?
6. Ef liðsfélagi sameinaði breytingu sem tvöfaldaði p99 töf, hve langt þar til einhver tæki eftir og hvernig myndi hann komast að því?

## Helstu atriði

- Mældu áður en þú fínstillir. Flöskuhálsinn er sjaldan þar sem þú giskar og ótímabær fínstilling kostar skýrleika fyrir engan ávinning.
- Skilgreindu „nógu hratt“ sem hundraðshlutafjárhagsáætlun, því meðaltöl fela halann þar sem raunverulegir notendur búa.
- Kjóstu reikniritasigra (betri Big O-flokk) fram yfir örstillingu og vittu hvort þú þarft töf eða afköst.
- Virtu mörk hliðrunar (lögmál Amdahls) og hættur skyndiminnis (ógilding og úrelding).
- Viðmiðaðu af heiðarleika með upphitun, dreifni og dæmigerðu vinnuálagi og vantreystu örviðmiðum.
- Hliðaðu afköst í CI (kafli 2.4) og fylgstu með þeim í framleiðslu (kafli 9.2). Bættu kerfisstigssýnina í kafla 3.5.
- Afköst eru kostnaður fyrir fyrirtæki, aðgengi fyrir hið opinbera, og ódýr að vernda stöðugt en dýr að eftirbæta.

## Heimildir og frekari lestur

- Brendan Gregg, *Systems Performance: Enterprise and the Cloud* (profiling, flame graphs, and method).
- Brendan Gregg, *BPF Performance Tools* (practical observability and profiling on Linux).
- Donald E. Knuth, "Structured Programming with go to Statements" (*ACM Computing Surveys*, 1974): the source of the premature-optimisation maxim.
- Donald E. Knuth, *The Art of Computer Programming* (algorithmic analysis and complexity).
- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein, *Introduction to Algorithms* (Big O and algorithmic efficiency).
- Gene M. Amdahl, "Validity of the Single Processor Approach to Achieving Large-Scale Computing Capabilities" (1967): the origin of Amdahl's law.
- Ulrich Drepper, "What Every Programmer Should Know About Memory" (the memory hierarchy and data locality).
- Martin Kleppmann, *Designing Data-Intensive Applications* (latency, throughput, and tail behaviour in systems).
- Aleksey Shipilev, "JMH and the pitfalls of microbenchmarking" (honest benchmarking practice on managed runtimes).
- Ilya Grigorik, *High Performance Browser Networking* (client-side and network performance for low-bandwidth users).
