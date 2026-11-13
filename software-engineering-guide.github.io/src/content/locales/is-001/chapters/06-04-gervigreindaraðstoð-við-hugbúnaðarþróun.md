# 6.4 Gervigreindaraðstoð við hugbúnaðarþróun

## Yfirlit og tilgangur

Gervigreindaraðstoðarmenn í kóðun geta nú búið til kóða, lokið föllum, skrifað próf, útskýrt framandi kerfi og hjálpað þér að [endurbyggja](https://en.wikipedia.org/wiki/Code_refactoring) kóða. Notaðir vel flýta þeir fyrir hversdagsvinnu. Þeir lækka þröskuldinn að framandi málum og römmum. Þeir taka leiðindin úr stöðluðum endurteknum kóða.

Notaðir illa valda þeir raunverulegum skaða. Þeir geta flætt yfir kóðagrunn með kóða sem lítur trúverðuglega út en er lúmskt rangur. Þeir geta valdið öryggisgötum, skapað leyfisáhættu og rýrt færni verkfræðinganna sem treysta á þá. Gervigreindaraðstoð við þróun er í senn raunverulegt framleiðniverkfæri og raunveruleg áhætta. Munurinn felst nær alfarið í verkfræðiaganum í kringum hana.

Fyrir stór teymi er áskorunin samræmi og öryggi í stærð. Þegar hundruð forritara nota gervigreindaraðstoðarmenn leggjast litlar venjur einstaklinga saman í skipulagslegar niðurstöður. Ef allir samþykkja tillögur gagnrýnislaust hækkar rýnibyrði og gallahlutfall. Ef þú veitir skýr viðmið, góð sjálfgefin gildi og sterka sannprófun auka sömu verkfæri afköst án þess að lækka gæði. Framleiðnisagan er líka blæbrigðaríkari en fullyrðingar seljenda gefa til kynna. Raunverulegur ávinningur er mjög mismunandi eftir verkum og barnaleg mæling, eins og að telja samþykktar tillögur, mun blekkja þig.

Fyrirtækja- og opinbert umhverfi bætir við strangari skorðum. Kóða sem snertir regluverkuð kerfi, meðhöndlar viðkvæm gögn eða rekur mikilvæga innviði er ekki hægt að treysta bara af því að gervigreind framleiddi hann. Leyfisuppruni skiptir máli þegar mynduð kóði getur endurómað þjálfunargögn undir takmarkandi leyfum. Sumar skipulagsheildir verða að geyma frumkóða á eigin vélbúnaði og mega alls ekki senda hann til ytri þjónusta. Að setja skýr, framfylgjanleg viðmið um gervigreindaraðstoð er nú hluti af ábyrgri verkfræðiforystu. Meðal tiltækra aðstoðarmanna eru verkfæri byggð á Claude-líkönum Anthropic einn leiðandi kostur ásamt öðrum. Vinnubrögðin hér á eftir gilda hvern sem þú tekur upp.

*Sjá einnig:* kafla 2.5 (kóðarýni og samvinna), kafla 2.4 (prófunarstefna) og kafla 6.5 (ábyrg og traustverð gervigreind).

## Meginreglur

- Verkfræðingurinn, ekki aðstoðarmaðurinn, ber ábyrgð á hverri línu sem er innrituð.
- Gervigreindarmyndaður kóði er uppkast sem á að rýna og sannreyna, aldrei fullbúin vara sem hægt er að treysta.
- Sannprófunarfyrirhöfn ætti að skalast með áhættu kóðans, ekki með því hve öruggt úttakið lítur út.
- Mældu framleiðni með niðurstöðum sem skipta máli (afhent gildi, gæði, hringrásartími), ekki tillögufjölda.
- Varastu öryggis- og leyfisáhættu sem mynduð kóði getur komið með.
- Varðveittu og efldu mannlega verkfræðifærni. Láttu aðstoðarmenn ekki grafa undan hana.
- Vertu gagnsær um hvar og hvernig gervigreindaraðstoð er notuð.

## Ráðleggingar

### Notaðu gervigreindarparforritun sem uppkasts- og könnunartæki

Beindu aðstoðarmönnum að verkum þar sem þeir skara fram úr og mistök eru ódýr að grípa: stöðluðum endurteknum kóða, prófastoðum, sniðbreytingum, að útskýra framandi kóða og að kanna aðferðir. Líttu á úttak þeirra sem fyrsta uppkast. Vertu áfram í bílstjórasætinu. Lestu, skildu og breyttu hverri tillögu frekar en að samþykkja á sjálfstýringu. Á framandi sviðum skaltu nota aðstoðarmanninn til að læra, en athuga fullyrðingar hans gegn áreiðanlegum skjölum. Aðstoðarmenn geta fundið upp API og farið rangt með hegðun af fullkomnu öryggi.

### Rýndu, prófaðu og sannreyndu gervigreindarmyndaðan kóða sem ótraust inntak

Veittu gervigreindarmynduðum kóða sömu skoðun og þú myndir veita kóða frá nýjum liðsmanni, eða meiri. Mannlegur rýnir ætti að skilja hann nógu vel til að útskýra og viðhalda honum. „Gervigreindin skrifaði hann“ er aldrei ásættanlegt svar við „hvers vegna virkar þetta?“ Krefstu prófa og varastu gervigreindarmynduð próf sem staðhæfa aðeins núverandi hegðun frekar en ætlaða hegðun. Keyrðu [stöðuga greiningu](https://en.wikipedia.org/wiki/Static_program_analysis), öryggisskönnun og ósjálfstæðisathuganir. Fyrir áhættusaman kóða (auðkenningu, [dulritun](https://en.wikipedia.org/wiki/Cryptography), fjármálarökfræði, öryggiskerfi) skaltu líta á gervigreindarúttak sem upphafspunkt sem krefst sérfræðisannprófunar manna, aldrei sem áreiðanlegt.

### Mældu framleiðni heiðarlega og settu raunhæfar væntingar

Slepptu hégómamælikvörðum eins og samþykktarhlutfalli eða fjölda mynduðra lína. Horfðu í staðinn á afhendingar- og gæðamerki yfir tíma: hringrásartíma, bilunarhlutfall breytinga, hlutfall galla sem sleppa í gegn og skilvirkni samkvæmt mati forritara. Ávinningur er raunverulegur en ójafn: mikill fyrir sum verk, hverfandi eða neikvæður fyrir önnur. Tími sem sparast við að skrifa kóða getur tapast aftur við að rýna og aflúsa hann. Settu væntingar við forystu í samræmi við það, svo fjárfesting hvíli á sönnunargögnum frekar en tískubylgjum, og svo teymi séu aldrei þrýst til að samþykkja óöruggar tillögur bara til að ná mælikvarða.

### Stýrðu öryggis- og leyfisáhættu

Skannaðu mynduðan kóða eftir veikleikum og óöruggum mynstrum. Aðstoðarmenn geta endurskapað óöruggt orðbragð úr þjálfunargögnum sínum. Límdu aldrei leyndarmál, auðkennisgögn eða viðkvæm gögn inn í fyrirmæli sem send eru til ytri þjónusta. Kjóstu verkfæri sem mæta gagnameðhöndlunarkröfum þínum, þar með talda útsetningu á eigin vélbúnaði eða í einkaumhverfi þar sem frumkóði má ekki yfirgefa umhverfið. Taktu á leyfismálum líka. Myndaður kóði getur líkst leyfisskyldum þjálfunargögnum, svo notaðu verkfæri og stefnur sem draga úr þeirri áhættu, haltu uppruna til haga þar sem þú getur og beindu öllu vafasömu gegnum lögfræðirýni. Raktu uppruna ósjálfstæða sem aðstoðarmaðurinn leggur til, því hann gæti mælt með yfirgefnum eða illgjörnum pakka.

### Settu teymisviðmið, upplýsingagjöf og viðhald færni

Birtu skýra leiðsögn um hvenær og hvernig má nota gervigreindaraðstoð, hvaða gögnum má aldrei deila og hvaða sannprófun hvert áhættustig krefst. Hvettu til gagnsæis um gervigreindaraðstoðuð framlög þar sem það skiptir máli fyrir rýni og ábyrgð. Haltu mannlegri færni beittri af ásetningi. Tryggðu að verkfræðingar, einkum yngri, læri enn grunnatriðin frekar en að útvista skilningi sínum. Snúðu fólki gegnum verk sem byggja djúpa sérþekkingu og líttu á of mikla ósjálfstæði sem raunverulega langtímaáhættu fyrir getu teymisins.

## Málamiðlanir: kostir og gallar

| Vídd | Ávinningur gervigreindaraðstoðar | Áhætta gervigreindaraðstoðar |
|---|---|---|
| Hraði | Hraðari staðlaður endurtekinn kóði og uppkast | Tími tapast í að rýna rangan kóða |
| Innleiðing | Auðveldari inngangur að nýjum málum/römmum | Grunnur skilningur, uppfundin API |
| Gæði | Fleiri próf, hraðari endurbygging | Trúverðugur en lúmskt rangur kóði |
| Öryggi | Getur lagt til lagfæringar og skönnun | Getur valdið veikleikum |
| Færni | Losar tíma fyrir verðmætari vinnu | Rýrir grunnatriðin ef ofnotað |
| Leyfi | Hraðari endurnýting algengra mynstra | Uppruna- og leyfisáhætta |

Meginmálamiðlunin er hraði gegn sannprófun. Gervigreind færir fyrirhöfn frá ritun til rýni. Nettó ávinningur ræðst af því hvort rýni- og sannprófunarvenjur þínar eru nógu sterkar til að grípa það sem aðstoðarmaðurinn fer rangt með. Veik rýni leiðir til gæðahnignunar. Sterk rýni og skýr viðmið ná ávinningnum.

## Spurningar til að ræða með teyminu

1. **Hvaða hlutar kóðagrunns okkar eru alfarið bannaðir gervigreindaraðstoð og hvernig framfylgjum við því marki?** Samræmt traust er gildra: að beita sömu léttu skoðun á auðkenningu, dulritun, fjármálarökfræði og öryggiskerfi og á staðlaðan endurtekinn kóða er hvernig lúmskar, öruggar villur ná til mikilvægra slóða. Fyrir stórt teymi breytir skýr listi yfir útilokaðar einingar eða einingar sem aðeins fara í sérfræðirýni einstaklingsdómgreind í skipulagslegt öryggi. Komdu með áhættukort þitt af kóðagrunninum, núverandi stefnu þína (ef hún er til) og hvernig þú myndir í raun koma í veg fyrir að mynduð kóði lendi í takmarkaðri einingu: leiðsluathuganir, eignarhaldsreglur eða rýnihlið. Í varnar-, regluverkuðu og öryggismikilvægu umhverfi ættu sumar einingar að útiloka gervigreindaraðstoð með öllu. Svarið ætti að skala sannprófunarfyrirhöfn með áhættu kóðans, aldrei með því hve öruggt úttakið lítur út.

2. **Hverjar eru raunverulegar þróanir okkar í bilunarhlutfalli breytinga og göllum sem sleppa í gegn frá því við tókum upp aðstoðarmenn og erum við að mæla þær eða giska?** Framleiðnifullyrðingar seljenda og talning samþykktarhlutfalls eru hégómamælikvarðar sem blekkja, því tími sem sparast við að skrifa kóða getur tapast aftur við að rýna og aflúsa hann. Til að forysta fjárfesti á sönnunargögnum frekar en tískubylgjum þarftu afhendingar- og gæðamerki yfir tíma: hringrásartíma, bilunarhlutfall breytinga, hlutfall galla sem sleppa í gegn og skilvirkni samkvæmt mati forritara. Komdu með þær raunverulegu tölur sem þú átt og vertu heiðarlegur þar sem þú átt engar. Áhættan til að fylgjast með er teymi þrýst til að samþykkja óöruggar tillögur bara til að ná mælikvarða. Svarið ætti að koma niðurstöðumælikvörðum í stað tillögufjölda og setja væntingar um að ávinningur sé raunverulegur en ójafn, mikill fyrir sum verk og neikvæður fyrir önnur.

3. **Ef mynduð kóði endurómar þjálfunargögn með takmarkandi leyfi eða dregur inn áhættusamt ósjálfstæði, hver grípur það og hvenær?** Myndaður kóði getur líkst leyfisskyldu efni eða mælt með yfirgefnum eða illgjörnum pökkum, og sú áhætta lendir í vörunni þinni hvort sem einhver tók eftir henni eða ekki. Fyrir fyrirtæki og hið opinbera bera leyfisuppruni og aðfangakeðjuáhætta lagalegt vægi sem „gervigreindin skrifaði þetta“ yppt öxlum stenst ekki. Komdu með núverandi leyndarmálaskönnun, leyfisathuganir og upprunarakningu ósjálfstæða og finndu hvar í leiðslunni hver keyrir. Ræddu hvað beinir vafasömum kóða til lögfræðirýni og hver á þá ákvörðun. Ef leyndarmál geta verið límd inn í ytri verkfæri eða óskoðaðir pakkar geta sameinast án andmæla skaltu loka þeim götum áður en þú stigvaxar notkun aðstoðarmanna í teyminu.

4. **Hvernig höldum við verkfræðingum, einkum yngri, að læra grunnatriðin frekar en að útvista skilningi sínum til aðstoðarmannsins?** Færnirýrnun er hæg áhætta sem birtist aldrei í hraða þessa ársfjórðungs, en birtist árum síðar sem teymi sem getur ekki aflúsað, hannað eða rýnt án fyrirmæla. Fyrir stóra skipulagsheild er togið á móti raunverulegt: aðstoðarmenn leyfa yngri verkfræðingum að afhenda hraðar í dag og þrýstingurinn að ná afhendingarmarkmiðum berst gegn hægari vinnunni að byggja djúpa sérþekkingu. Komdu með sönnunargögn um hvernig fólkið þitt vex í raun: hvaða brot yngri verkfræðinga getur útskýrt kóðann sem það sameinaði, hve mikla ósaðstoðaða vandamálalausn innleiðing þín krefst enn og hvort rýni grípur grunnan skilning eða stimplar bara virkt úttak. Snúðu fólki af ásetningi gegnum verk sem byggja leikni og líttu á of mikla ósjálfstæði sem getuáhættu, ekki persónulegan veikleika. Í opinberum og langlífum mikilvægum kerfum gæti vinnuaflið þurft að smíða og sannreyna kerfi í áratugi án verkfæra seljenda, svo þjálfunarleið sem tryggir beinan grunn er samfellukrafa, ekki nauðsyn.

5. **Hvaða aðstoðarmenn megum við í raun nota miðað við hvar frumkóði og gögn okkar verða að vera og hvernig komum við í veg fyrir að leyndarmál nái nokkru sinni í fyrirmæli?** Gagnameðhöndlunarskorður ákveða verkfærið áður en framleiðni gerir það: aðstoðarmaður sem streymir frumkóða þínum til ytri þjónustu getur verið útilokaður alfarið, hvað sem getu hans líður. Fyrir stórt teymi er spennan milli þæginda besta hýsta verkfærisins og kröfunnar um að séreignarkóði, auðkennisgögn og viðkvæm gögn yfirgefi aldrei mörk þín. Komdu með gagnaflokkunarkort þitt, útsetningarkostina sem hver frambjóðandi býður (hýst, einka, á eigin vélbúnaði) og áþreifanlegu varnirnar sem halda leyndarmálum frá fyrirmælum: skönnun fyrir innritun, fyrirmælasíun og þjálfun verkfræðinga. Ákveddu hvaða verkfæri eru leyfð fyrir hvaða flokka kóða og gerðu mörkin framfylgjanleg frekar en ráðgefandi. Í regluverkuðu, varnar- og leynilegu umhverfi gæti útsetning á eigin vélbúnaði eða í loftgapi verið eini löglegi kosturinn, og að senda frumkóða til nokkurrar ytri þjónustu verður að vera bannað og tæknilega lokað, ekki bara latt.

6. **Hvernig breytum við dreifðum einstaklingsvenjum í samræmd viðmið um alla skipulagsheildina og hver á stefnuna þegar verkfæri þróast?** Þegar hundruð forritara spinna hver sína nálgun leggjast litlar venjur saman í skipulagslegar niðurstöður, og ósamkvæm sannprófun er þar sem gallar og áhætta slæðast í gegn. Sjónarmiðið á móti er sjálfræði: teymi hata þungar miðlægar skipanir, samt framleiðir frjálst-fyrir-alla ójöfn gæði og enga sameiginlega vernd. Komdu með núverandi leiðsögn þína (ef einhver er), sönnunargögn um hve samræmt henni er fylgt og tillögu um góð sjálfgefin gildi bökuð inn í leiðsluna svo örugga leiðin sé auðvelda leiðin. Nefndu eiganda sem heldur stefnunni núgildandi þegar aðstoðarmenn breytast á nokkurra mánaða fresti og upplýsingagjafarviðmið svo rýnar viti hvenær gervigreindaraðstoð mótaði framlag. Fyrir fyrirtæki eða opinberan aðila skaltu tengja viðmiðin við úttekt og ábyrgð: skjalfestur, framfylgdur staðall sem úttektaraðili getur skoðað slær þjóðsagnavenju sem er ólík eftir teymum og hverfur þegar lykilmaður fer.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með fáeina verkfræðinga og ekkert svigrúm til að sóa skaltu halla þér að hýstum aðstoðarmönnum fyrir staðlaðan endurtekinn kóða, próf og framandi ramma og láta þá flýta fyrir hversdagsvinnu. Haltu einni óumsemjanlegri reglu: maður sem skilur breytinguna rýnir hverja sameiningu, því lúmsk röng lína í fimm manna kóðagrunni á sér hvergi felustað og engan annan til að grípa hana. Bættu við leyndarmálaskanna og leyfisathugun snemma. Þau eru ódýr og koma í veg fyrir dýr mistök sem þú hefur ekki efni á að hreinsa upp síðar.

**Lítið fyrirtæki.** Þú hefur líklega engan öryggissérfræðing og þröngt fjárhagsáætlun, svo kjóstu aðstoðarmenn innbyggða í verkfæri sem þú treystir nú þegar fram yfir sérsniðna uppsetningu sem þú þarft að viðhalda. Rammaðu áhættuna á einföldu máli: límdu aldrei viðskiptavinagögn eða auðkennisgögn inn í ytri fyrirmæli og líttu á mynduðan kóða sem snertir reikningagerð eða auðkenningu sem uppkast til að sannreyna, ekki fullbúið svar. Veldu seljendur sem þú getur lesið gagnameðhöndlunarskilmála hjá og sem þú getur slökkt á gervigreindareiginleikum hjá ef þeir haga sér illa.

**Stórfyrirtæki.** Vandinn er samræmi og öryggi yfir mörg teymi: sameiginleg viðmið eftir áhættustigi, skyldubundin rýni og skönnun í leiðslunni og heiðarlegir afhendingar- og gæðamælikvarðar frekar en samþykktartölur. Staðlaðu verkfæravalið og útsetningarlíkanið svo séreignarkóði haldist innan marka þinna, fjárhagsáætlaðu rýni- og leiðréttingarkostnaðinn sem aðstoðarmenn færa á rýna og útilokaðu eða hliðaðu áhættumiklar einingar skýrt. Stýrðu gervigreindaraðstoð sem stjórnaðri getu með eiganda, ekki dreifingu einstaklingsvenja.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta hvert val. Kjóstu útsetningu á eigin vélbúnaði eða í einkaumhverfi þar sem frumkóði og viðkvæm gögn mega ekki yfirgefa umhverfið, bannaðu að senda kóða til ytri þjónusta og krefstu upplýsingagjafar um gervigreindaraðstoðuð framlög svo ákvarðanir haldist úttektarhæfar. Skyldaðu öryggis- og leyfisskönnun á öllum mynduðum kóða, útilokaðu gervigreindaraðstoð úr öryggismikilvægum og leynilegum einingum og haltu þjálfunarleið sem tryggir að opinbert vinnuafl geti smíðað og sannreynt kerfi án verkfæra seljenda yfir langan líftíma kerfanna sem það á.

## Dæmi

**Sprotafyrirtæki.** Sex verkfræðinga SaaS-sprotafyrirtæki tók upp gervigreindaraðstoðarmenn í kóðun til að hreyfa sig hraðar í hversdagsvinnu. Það hallaði sér að þeim fyrir staðlaðan endurtekinn kóða, próf og kóða fyrir framandi ramma, en hélt fastri reglu um að maður sem skildi breytinguna yrði að rýna hverja sameiningarbeiðni, og það bætti leyndarmálaskanna og leyfisathugun við leiðsluna. Fyrir reikningagerðar- og auðkenningarkóðann litu verkfræðingar á gervigreindarúttak sem gróft uppkast til að sannreyna línu fyrir línu frekar en að treysta. Þeir fylgdust með hringrásartíma og göllum sem sluppu í gegn frekar en að telja samþykktar tillögur og héldu ávinningnum án þess að gæði rynnu til.

**Stórfyrirtæki.** Stórt netverslunarfyrirtæki kynnti gervigreindaraðstoðarmenn í kóðun með varnarrimlum. Það bannaði leyndarmál í fyrirmælum. Það krafðist mannlegrar rýni, þar sem rýnir var ætlast til að skilja kóðann. Það bætti öryggisskönnun við leiðsluna og valdi einkaútsetningu svo séreignarkóði yfirgæfi aldrei umhverfi þess. Það mældi áhrif með hringrásartíma og bilunarhlutfalli breytinga frekar en samþykktartölum. Það fann traustan ávinning í stöðluðum endurteknum kóða og prófum, en krafðist sérfræðirýni fyrir greiðslukóða, þar sem það leit á gervigreindarúttak sem ótraust.

**Hið opinbera.** Varnarhugbúnaðarstofnun leyfði gervigreindaraðstoð aðeins gegnum verkfæri á eigin vélbúnaði sem hélt leynilegum og viðkvæmum kóða innan marka hennar. Hún bannaði að senda frumkóða til nokkurrar ytri þjónustu. Hún krafðist upplýsingagjafar um gervigreindaraðstoðuð framlög í kóðarýni og skyldaði öryggis- og leyfisskönnun á öllum mynduðum kóða. Hún útilokaði gervigreindaraðstoð alfarið úr tilteknum öryggismikilvægum einingum. Yngri verkfræðingar fylgdu þjálfunarleið sem tryggði að þeir lærðu grunnatriðin beint, svo vinnuaflið missti ekki hæfnina til að smíða og sannreyna kerfi án aðstoðar.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Hvatinn er hraðari afhending og minni leiðindavinna, svo knöpp verkfræðihæfileikar þínir geti einbeitt sér að hönnun, dómgreind og erfiðum vandamálum. Ávöxtun birtist sem styttri hringrásartími fyrir hentug verk og bætt upplifun forritara, en aðeins þar sem sannprófun heldur gæðum háum. Barnalegar ávöxtunarfullyrðingar byggðar á tillögufjölda blekkja og þú ættir að hafna þeim.

Heildareignarkostnaður felur í sér verkfæraleyfi, örugga útsetningu eða útsetningu á eigin vélbúnaði, öryggis- og leyfisskönnun og oft vanmetinn kostnað við að rýna og leiðrétta gervigreindarúttak. Kostnaður þess að taka *ekki* upp er samkeppnislegur: jafningjar gætu afhent hraðar og laðað að hæfileikafólk sem býst við nútímaverkfærum. Kostnaður þess að taka upp af kæruleysi er gæðarýrnun, öryggisatvik og lagaleg áhætta. Færðu rök við forystu með tilraunaverkefni sem mælir raunverulegar afhendingar- og gæðaniðurstöður, parað við áþreifanlega áætlun um viðmið, sannprófun og gagnavernd.

## Andmynstur og gildrur

- **Samþykki á sjálfstýringu.** Að innrita tillögur án þess að lesa þær eða skilja.
- **Hégómamælikvarðar.** Að dæma árangur eftir samþykktarhlutfalli eða mynduðum línum.
- **Leyndarmál í fyrirmælum.** Að líma auðkennisgögn eða viðkvæm gögn inn í ytri verkfæri.
- **Að treysta gervigreindarprófum.** Að samþykkja mynduð próf sem læsa núverandi hegðun, ekki ætlaða hegðun.
- **Að hunsa uppruna.** Að líta framhjá leyfis- og ósjálfstæðaáhættu í mynduðum kóða.
- **Færnirýrnun.** Að leyfa yngri verkfræðingum að útvista skilningi og læra aldrei grunnatriðin.
- **Samræmt traust.** Að beita sömu lágu skoðun á öryggismikilvægan kóða og á staðlaðan endurtekinn kóða.

## Þroskalíkan

1. **Upphaf.** Einstaklingar nota aðstoðarmenn ad hoc og viðbragðsdrifið. Engin stefna, engin mæling. Leyndarmál og hugverk eru í hættu og mynduð kóði sameinast með hvaða skoðun sem hver og einn beitir.
2. **Þróun.** Grunnnotkunarleiðsögn og gagnareglur eru til og einhver öryggisskönnun keyrir, en vinnubrögð eru ósamræmd milli teyma: dýpt sannprófunar er mismunandi eftir fólki, framleiðnifullyrðingar eru sögusagnir og áhættusamur kóði er ekki áreiðanlega hliðaður.
3. **Stöðlun.** Viðmið eftir áhættustigi eru skjalfest og framfylgd um skipulagsheildina: skyldubundin mannleg rýni, öryggis- og leyfisskönnun í leiðslunni, örugg útsetning eða útsetning á eigin vélbúnaði þar sem þarf, upplýsingagjafarvenjur og skýr listi yfir útilokaðar einingar eða einingar sem aðeins fara í sérfræðirýni.
4. **Stjórnun.** Venjan er mæld og stýrð gegn grunnlínum: hringrásartími, bilunarhlutfall breytinga og hlutfall galla sem sleppa í gegn eru rakin fyrir og eftir upptöku, kostnaður við rýni og leiðréttingu er magnsettur, leyndarmálaleka- og leyfisáhættuatvik eru talin og ákvarðanir um fara eða ekki fara á verkfærum og útvíkkun hvíla á þeim sönnunargögnum frekar en fullyrðingum seljenda.
5. **Samhæfing.** Gervigreindaraðstoð er stöðugt bætt og samþætt um skipulagsheildina: sannprófun er byggð inn í leiðsluna sem sjálfgefna leið, færniþróun er af ásetningi og rakin, stefna aðlagast þegar verkfæri breytast á nokkurra mánaða fresti og skipulagsheildin endurmetur, skiptir út og endurmarkar aðstoðarmenn reglulega eftir því sem sönnunargögn og áhættumynd breytast.

## Hugmyndir til umræðu

- Hvernig ættu sannprófunarkröfur að vera ólíkar milli staðlaðs endurtekins kóða og öryggismikilvægs kóða?
- Hvaða framleiðnimælikvarðar endurspegla í raun gildi gervigreindaraðstoðar í þínu samhengi?
- Hvenær, ef nokkurn tímann, ætti að upplýsa um gervigreindaraðstoðuð framlög?
- Hvernig kemurðu í veg fyrir færnirýrnun, einkum hjá yngri verkfræðingum?
- Hvaða gagnameðhöndlunarskorður ráða því hvaða verkfæri þú getur notað?
- Hvernig stýrirðu leyfis- og upprunaáhættu af mynduðum kóða?

## Helstu atriði

- Verkfræðingurinn ber áfram ábyrgð. Gervigreindarúttak er ótraust uppkast sem á að sannreyna.
- Skalaðu sannprófun með áhættu og treystu aldrei öryggismikilvægum gervigreindarkóða án sérfræðirýni.
- Mældu raunverulegar afhendingar- og gæðaniðurstöður, ekki tillögufjölda.
- Varastu öryggis-, gagnaleka- og leyfisáhættu með stefnu og verkfærum.
- Settu skýr viðmið og varðveittu mannlega verkfræðifærni af ásetningi.

## Heimildir og frekari lestur

- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Andrew Ng, *Machine Learning Yearning* (on realistic expectations and measurement).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Peter Naur, *Programming as Theory Building* (on understanding versus code artifacts).
- Titus Winters, Tom Manshreck, and Hyrum Wright, *Software Engineering at Google*.
- GitClear and related industry studies on AI-assisted code quality trends.
