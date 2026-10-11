# 5.2 Viðmótshönnun og hönnunarkerfi

## Yfirlit og tilgangur

[Viðmótshönnun (UI)](https://en.wikipedia.org/wiki/User_interface_design) er handverkið að móta það sem fólk sér og snertir: uppsetningu, [leturgerð](https://en.wikipedia.org/wiki/Typography), liti, bil, stýringar og ástönd. [Hönnunarkerfi](https://en.wikipedia.org/wiki/Design_system) tekur það handverk og breytir því í sameiginlega, endurnýtanlega, stýrða eign: skjalfest safn reglna, íhluta, mynstra og tákna sem hvert teymi sækir í, svo öll varan líti út og hegði sér sem ein. Viðmótshönnun ákveður hvernig einn skjár á að líta út. Hönnunarkerfi ákveður hvernig tíu þúsund skjáir yfir mörg teymi haldast samfelldir.

Fyrir stóra skipulagsheild er hönnunarkerfið áhrifamesta einstaka fjárfestingin í viðmótsgæðum og afhendingarhraða. Án þess finnur hvert teymi upp hnappa, eyðublöð, glugga og villumeðhöndlun að nýju, hvert lítillega ólíkt, hvert viðhaldið sérstaklega, hvert bilað sérstaklega. Notendur borga fyrir þetta í ruglingi og vantrausti. Reksturinn borgar fyrir það í tvíteknu átaki og ójöfnum gæðum. Hönnunarkerfi breytir einskiptis hönnunarákvörðunum í endurnýtanlegt fjármagn: leystu [aðgengi](https://en.wikipedia.org/wiki/Accessibility), [svörun](https://en.wikipedia.org/wiki/Responsive_web_design) og vörumerki einu sinni í íhlut, og hvert teymi erfir niðurstöðuna.

Fyrirtæki og hið opinbera bæta við tveimur sértækum þrýstingum. Fyrst, stærð: hundruð forrita, mörg smíðuð af söluaðilum eða fengin með samruna, þurfa öll að finnast eins og ein skipulagsheild. Í öðru lagi, langlífi og breyting: vörumerki eru endurnýjuð, stofnanir endurskipulagðar og einn vettvangur kann að þurfa að þjóna nokkrum vörumerkjum eða undirstofnunum úr einum kóðagrunni. Vel hannað hönnunarkerfi, með réttri þemun og táknun, gerir þessar umfangsmiklu breytingar viðráðanlegar í stað skelfilegra.

## Meginreglur

- Samræmi lækkar [vitrænt álag](https://en.wikipedia.org/wiki/Cognitive_load). Hnappur ætti að líta út og hegða sér eins alls staðar.
- Hönnunarákvarðanir eru eignir: fangaðu þær einu sinni sem endurnýtanlega íhluti og tákn.
- Tákn eru sannleiksuppspretta sjónrænna ákvarðana. Íhlutir neyta tákna, aldrei harðkóðaðra gilda.
- Aðgengi og svörun eru byggð inn í íhluti, ekki fest á hvern skjá.
- Hönnunarkerfi er vara með notendur (hönnuði og forritara), ekki einskiptis afurð.
- Sjónræn stigskipting stýrir athygli: leturgerð, litur og rými ættu að gera mikilvægi augljóst.
- Stjórnarhættir halda kerfi samfelldu. Framlag heldur því lifandi.

## Ráðleggingar

### Byggðu kerfið upp í lögum: tákn, íhlutir, mynstur

Hönnunartákn (design tokens) eru nefnd, vettvangsóháð gildi fyrir lit, bil, leturgerð, radíus, hæð og hreyfingu: atómísku ákvarðanirnar. Byggðu þau í þrepum: frumstæð litapalletta (hrá gildi), merkingarfræðileg tákn (`color-action-primary`, `space-inset-md`) sem bera merkingu og íhlutastigstákn þar sem þú þarft. Íhlutir neyta merkingarfræðilegu táknanna, svo ein breyting breiðist alls staðar út. Fyrir ofan íhluti sitja mynstur: sannreyndar samsetningar eins og gagnatafla, fjölþrepa eyðublað eða tómt ástand. Skjalfestu öll þrjú lögin á einum stað, með lifandi dæmum og notkunarleiðbeiningum.

### Fáðu sjónrænu grunnatriðin rétt

Settu upp leturgerðarskala með skýrri stigskiptingu og rausnarlegu línubili fyrir læsileika og haltu þig við takmarkað safn stærða og þykkta. Skilgreindu lit sem kerfi, með nægu birtuskili fyrir aðgengi (sjá aðgengiskaflann) og merkingarfræðileg hlutverk, frekar en hráa litbrigði dreifða um viðmótið. Notaðu bilskala og uppsetningarrist svo röðun og taktur haldist samfelld án giskunar á hvern skjá. Sjónræn stigskipting ætti að gera aðalaðgerðina og mikilvægustu upplýsingarnar augljósar í fljótu bragði.

### Hannaðu svörunar- og farsíma-fyrst

Hannaðu fyrir minnsta sanngjarna sýnisvæði fyrst, bættu síðan við fyrir stærri skjái. Þetta neyðir þig til að forgangsraða nauðsynlegu efni og stýringum. Notaðu flæðandi uppsetningar og afstæðar einingar svo viðmót aðlagist hvaða skjá sem er, frekar en að smella milli fárra fastra brotpunkta. Gerðu snertimarkmið nógu stór og tryggðu að víxlverkanir virki með snertingu, mús og lyklaborði. Sérstaklega hjá hinu opinbera skaltu gera ráð fyrir að umtalsverður hluti notenda þinna sé á litlum, eldri eða ódýrum tækjum.

### Gerðu hönnunar-til-þróunar afhendingu og samsvörun að fyrsta flokks áhyggjuefni

Hönnunarkerfi borgar sig aðeins þegar afhent viðmót passar við ætlaða hönnun og heldur áfram að passa. Stefndu að einni sannleiksuppsprettu: tákn flutt út úr hönnunartólinu nærir kóða beint, svo hönnuðir og verkfræðingar vísi í sömu gildi. Útvegaðu kóðað íhlutasafn sem verkfræðingar munu í raun nota, með sömu nöfnum og eigindum og hönnunaríhlutirnir. Notaðu sjónræna afturfaraprófun (sjálfvirkan samanburð birts viðmóts gegn samþykktum grunnmyndum) og hönnunarrýniathuganir til að grípa rek. Og mældu „hönnunar-kóða samsvörun“ sem skýran heilsumælikvarða: hlutfall viðmóts smíðað úr kerfisíhlutum á móti einnota kóða.

### Styddu þemun og hvítmerkingu í fyrirtækjastærð

Hannaðu fyrir mörg vörumerki frá byrjun ef nokkur möguleiki er á að þú þurfir þau. Því íhlutir neyta merkingarfræðilegra tákna er þema einfaldlega annað gildasett tákna, svo vörumerkjaendurnýjun eða nýtt undirvörumerki verður gagnabreyting, ekki kóðaendurskrift. Styddu ljós og dökk þemu, háskerpubirtuskilsham og vörumerkjun á hvern leigjanda gegnum sama búnað. Haltu vörumerkjasértækri rökfræði úr íhlutum og ýttu henni í táknasett og stillingu.

### Stýrðu kerfinu sem vöru

Gefðu hönnunarkerfinu sérstakt teymi, vegvísi, útgáfumerkingu, breytingaskrá og stuðningsrás. Tilgreindu hvernig teymi leggja til nýja íhluti og hvernig þeir eru rýndir og færðir upp. Jafnaðu miðlæga stjórn (til að varðveita samfellu og aðgengi) við framlagslíkan (svo kerfið þróist með raunverulegum þörfum í stað þess að verða flöskuháls). Miðlaðu úreldingum og flutningum skýrt og gefðu neytandi teymum nægan fyrirvara.

## Málamiðlanir: kostir og gallar

| Ákvörðun | Kostir | Gallar |
|---|---|---|
| Smíða hönnunarkerfi | Samræmi, hraði, aðgengi einu sinni, auðveldari endurnýjun vörumerkis | Kostnaður fyrirfram og viðvarandi, þarfnast sérstaks teymis |
| Taka upp tilbúið kerfi | Hröð byrjun, sannreynd mynstur | Almennt útlit, erfiðara að passa einstakt vörumerki og þarfir |
| Strangir miðlægir stjórnarhættir | Samfella, gæði, aðgengi tryggt | Getur stíflað teymi, fundist skrifræðislegt |
| Opið framlagslíkan | Þróast með raunverulegum þörfum, sameiginlegt eignarhald | Hætta á reki og ósamræmi án rýni |
| Mikil táknun og þemun | Ódýr endurnýjun vörumerkis og fjölvörumerkjastuðningur | Meiri ágripun, brattari námsferill |

Hönnunarkerfi skipta kostnaði fyrirfram og stjórnarhátta fyrir langtímasamræmi og hraða. Fyrir litla vöru með eitt teymi borgar aukakostnaðurinn sig kannski ekki. Fyrir stóra skipulagsheild með mörg teymi og langlífar vörur er spurningin ekki hvort á að hafa kerfi heldur hve mikið á að fjárfesta og hvernig á að stýra því. Algengasta eftirsjáin er vanfjárfesting í stjórnarháttum og samsvörunarverkfærum: kerfið er til á pappír, en teymi reka hljóðlega í burtu frá því.

## Spurningar til að ræða með teyminu

1. **Hvernig er táknaarkitektúr okkar þrepaskiptur og er íhlutum bannað að nota harðkóðuð gildi?** Allur ávinningur hönnunarkerfis (ódýr endurnýjun vörumerkis, fjölvörumerkjaþemun, aðgengi leyst einu sinni) byggir á að íhlutir neyti merkingarfræðilegra tákna eins og `color-action-primary` frekar en hrárra litbrigða og pixlagilda dreifðra um kóða. Ákveddu þrepin núna: frumstæða litapallettu, merkingarfræðileg tákn sem bera merkingu og íhlutastigstákn aðeins þar sem þú raunverulega þarft. Ofágripun er raunveruleg hætta, svo komdu þér saman um hve mörg lög er of mikið og hvernig forritari finnur rétta táknið fljótt. Komdu með grep á harðkóðuðum litum og bili yfir kóðagrunn þinn sem sönnunargögn um rek. Ef vörumerkjarökfræði er bökuð inn í íhluti verður endurnýjun vörumerkis kóðaendurskrift í stað stillingarbreytingar, sem er einmitt stórslysið sem táknun er til að koma í veg fyrir.

2. **Hvernig mælum við og verjum hönnunar-kóða samsvörun og hvaða verkfæri grípa rek sjálfvirkt?** Hönnunarkerfi sem er aðeins til sem hönnunarskrá er límmiðablað: verkfræðingar endurbyggja allt hvort sem er og afhent viðmót víkur hægt frá ásetningi. Komdu þér saman um skýran samsvörunarmælikvarða (hlutfall viðmóts smíðað úr kerfisíhlutum á móti einnota kóða) og tengdu sjónræna afturfaraprófun inn í CI svo birtir skjáir séu bornir saman við samþykktar grunnmyndir. Þetta skiptir máli í fyrirtækja- og opinberri stærð því hundruð forrita, mörg smíðuð af söluaðilum eða erfð með samruna, þurfa öll að finnast eins og ein skipulagsheild. Komdu með núverandi samsvörunartölu og lista yfir helstu sérsmíðuðu íhlutina sem teymi endurbyggja stöðugt. Ef enginn á mælikvarðann eða afturfarasafnið er rek þegar að vinna hljóðlega.

3. **Hvernig stýrum við framlagi, úreldingu og flutningi svo kerfið stífli hvorki teymi né sundrist?** Ströng miðlæg stjórn tryggir samfellu og aðgengi en getur breytt hönnunarkerfisteyminu í flöskuháls sem teymi fara framhjá. Opið framlag heldur kerfinu lifandi en teflir í hættu sundurleitum afbrigðum án rýni. Ákveddu framlagsleiðina: hvernig teymi leggur til nýjan íhlut, hver rýnir hann og hvernig hann er færður upp. Jafn mikilvægt skaltu koma þér saman um hvernig þú miðlar brjótandi breytingum, því úreldingar án flutningsstuðnings og fyrirvara valda því að neytandi teymi stöðvast eða kvíslast. Komdu með dæmi um íhluti sem teymi smíðuðu utan kerfisins og spyrðu hvers vegna þau lögðu ekki aftur inn. Svarið leiðir yfirleitt í ljós hvort stjórnarhættir þínir eru þjónusta eða hindrun.

4. **Hvernig tryggjum við að aðgengi sé leyst einu sinni innan íhluta og hvað stöðvar teymi frá því að afhenda óaðgengilegan einnota hlut?** Sterkustu rökin fyrir hönnunarkerfi eru að litbirtuskil, fókusástönd, lyklaborðsvirkni og skjálesarmerkingarfræði séu leyst einu sinni og erfð alls staðar, en það loforð hrynur um leið og teymi handsmíða eigin stýringar. Fyrir stóra skipulagsheild er þetta þar sem stærsta lagalega og mannorðslega áhættan situr, því eitt óaðgengilegt greiðslueyðublað eða dagsetningarvalmynd getur hindrað raunverulega notendur og kveikt kvartanir yfir hverja vöru sem afritaði það. Vegðu miðlæga framfylgd (aðgengilega íhluti auk lint-tóls eða rýnihliðs sem hafnar hráu álagi) gegn sjálfræði teyma og ákveddu hvar harða línan er. Komdu með niðurstöður aðgengisúttektar, lista yfir íhluti með samræmisstöðu þeirra og talningu sérsmíðaðra stýringa sem teymi endurbyggðu utan kerfisins. Í fyrirtækja- og opinberu umhverfi er þetta ekki kurteisi: skyldur eins og WCAG, Section 508 og EN 301 549 gera samræmi að innkaupa- og úttektarkröfu, svo íhlutasafn með skjalfestu samræmi er sjálft regluvörslueign.

5. **Hve mörgum vörumerkjum, leigjendum og þemum þarf þetta kerfi að þjóna og höfum við hannað táknalagið fyrir það núna frekar en að bæta því við síðar?** Þemun er ódýr ef þú hannaðir fyrir hana og grimm ef þú gerðir það ekki, því vörumerki eða leigjandi sem aldrei var séð fyrir þvingar vörumerkjarökfræði aftur inn í íhluti og aflýsir öllum tilgangi táknunar. Fyrir stórt teymi mótar þessi ákvörðun árum af vinnu: vettvangur sem verður að þjóna nokkrum vörumerkjum, ljósu og dökku þema, háskerpubirtuskilsham og vörumerkjun á hvern leigjanda þarfnast merkingarfræðilegs táknalags nógu hreins til að þema sé einfaldlega annað gildasett. Jafnaðu þann sveigjanleika gegn ofágripun, því táknatré sem enginn getur ratað er eigin bilun. Komdu með vegvísi vörumerkja og leigjenda sem þú getur séð fyrir, fjölda þema í notkun í dag og alla íhluti sem þegar leka vörumerkjasértækri rökfræði. Í fyrirtækja- og opinberu samhengi bæta samrunar, yfirtökur og endurskipulagning stofnana rútínulega við vörumerkjum sem þú skipulagðir ekki, svo að hanna fyrir fjölvörumerki frá byrjun er munurinn á gagnabreytingu og margra ára endurskrift.

6. **Hvernig munum við flytja eldri forrit og söluaðilasmíðuð forrit yfir á kerfið og hvernig er hönnunarkerfisteymið fjármagnað svo það lifi af næsta fjárhagslotu?** Hönnunarkerfi skilar ávöxtun sinni aðeins þegar raunverulegar vörur taka það upp, samt eru erfiðustu forritin að breyta þau gömlu og útvistuðu sem þurfa það mest, og teymið sem viðheldur kerfinu er oft það fyrsta sem er skorið þegar fjárhagur þrengist. Fyrir stóra skipulagsheild verðurðu að velja milli stórhvellsflutnings og stigvaxandi og hvernig á að fá söluaðila til að smíða á íhlutum þínum frekar en í kringum þá. Komdu með skrá yfir forrit með núverandi samsvörunareinkunn þeirra, mat á flutningsfyrirhöfn á forrit og samningsvogarstengurnar sem þú heldur yfir söluaðilum. Í fyrirtækja- og opinberu umhverfi skaltu skrifa hönnunarkerfissamræmi inn í innkaupaskilmála svo ný söluaðilavinna lendi á kerfinu sjálfgefið og fjármagnaðu viðhaldsteymið sem varanlega sameiginlega innviði, því kerfi sem missir ráðsmenn sína í endurskipulagningu rekur aftur í sundrun innan árs.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með tvo eða þrjá verkfræðinga og ekkert svigrúm skaltu ekki smíða stýrt kerfi. Eyddu degi eða tveimur í að skilgreina lítið safn merkingarfræðilegra tákna fyrir lit, bil og leturgerð, auk tylftar sameiginlegra íhluta, allt í einni skrá sem allt teymið vísar í. Hallaðu þér að tilbúnu frumstæðu bókasafni fyrir erfiðu hlutana og haltu engu harðkóðuðu svo fyrsta raunverulega endurnýjun vörumerkis sé táknabreyting frekar en endurskrift.

**Lítið fyrirtæki.** Án sérstaks hönnuðar og með þröngt fjárhagsáætlun skaltu kaupa frekar en smíða: taktu upp sannreynt íhlutasafn eða viðmótssett og þemaðu það létt að vörumerki þínu. Markmið þitt er samfelld, aðgengileg vara án þess að manna hönnunarkerfisteymi, svo kjóstu kerfi sem afhendir aðgengi og svörun í kassanum. Stattu gegn löngun til að kvíslast það, því sérsniðið afrit sem þú getur ekki viðhaldið verður skuld um leið og upphaflega verkefnið heldur áfram.

**Stórfyrirtæki.** Vandinn er samfella yfir mörg teymi og langlífar vörur, svo líttu á hönnunarkerfið sem stýrða sameiginlega innviði með sérstöku teymi, útgáfumerkingu og vegvísi. Raktu hönnunar-kóða samsvörun sem raunverulegan mælikvarða, tengdu sjónræna afturfaraprófun inn í CI og hannaðu táknalagið fyrir mörg vörumerki og þemu frá byrjun. Fjárhagsáætlaðu stjórnarhátta- og flutningskostnað skýrt og stýrðu upptöku sem eignasafni frekar en að gera ráð fyrir að teymi reki sjálf yfir á kerfið.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta hvert val. Aðgengissamræmi við staðla eins og WCAG, Section 508 og EN 301 549 er lagakrafa, ekki kjör, svo íhlutasafn með skjalfestu samræmi verður regluvörslueign. Kjóstu eða framlengdu sameiginlegt opinbert hönnunarkerfi svo borgarar mæti sömu mynstrum yfir þjónustur, skrifaðu notkun hönnunarkerfis inn í söluaðilasamninga og birtu íhluti og leiðbeiningar opinskátt svo stofnanir og birgjar þeirra geti tekið þær upp og verið haldnir við þær.

## Dæmi

**Sprotafyrirtæki.** Tveggja verkfræðinga sprotafyrirtæki endurbyggði hnappa og eyðublaðsreiti lítillega ólíkt á hverjum nýjum skjá og varan var farin að líta út eins og saumuð saman. Í stað þungs kerfis eyddu þeir tveimur dögum í að skilgreina lítið safn merkingarfræðilegra hönnunartákna fyrir lit, bil og leturgerð, auk um tylftar sameiginlegra íhluta, allt í einni skrá sem allt teymið vísaði í. Því ekkert var harðkóðað var endurnýjun vörumerkis, þegar fyrsta hönnunarmeðvitaða ráðning þeirra lagði til hreinni litapallettu, táknabreyting sem lenti yfir allt forritið á eftirmiðdegi í stað skjá-fyrir-skjá baráttu.

**Stórfyrirtæki.** Hnattrænt hugbúnaðarfyrirtæki með tugi vörateyma byggði táknað hönnunarkerfi með sameiginlegu kóðuðu íhlutasafni. Merkingarfræðileg tákn leyfðu þeim að afhenda fulla vörumerkjaendurnýjun yfir allar vörur á vikum, í stað margra ára baráttu á hvert teymi, því breytingin var nýtt táknasett frekar en þúsundir harðkóðaðra litabreytinga. Hönnunar-kóða samsvörun, rakin sem mælaborðsmælikvarði, jókst þegar teymi skiptu út sérsmíðuðum íhlutum, sem skar tvítekið viðmótsviðhald.

**Hið opinbera.** Landsstjórn bjó til sameiginlegt hönnunarkerfi fyrir opinbera þjónustu (sameiginlega íhluti, mynstur og aðgengi innbyggt) fyrirskipað yfir stofnanir. Borgari sem færist milli skattaþjónustu, heilbrigðisþjónustu og leyfisveitingaþjónustu mætir sama haus, eyðublaðsstýringum og villumynstrum, sem byggir traust og styttir námsferil. Stofnanir og söluaðilar þeirra afhenda hraðar og aðgengilegar því erfiðu vandamálin eru leyst miðlægt, og ríkið getur uppfært leiðbeiningar eða aðgengislagfæringar einu sinni og látið þær breiðast alls staðar út.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun hönnunarkerfis kemur af því að fjarlægja tvítekningu og flýta afhendingu. Í stað þess að hvert teymi hanni og smíði sömu íhlutina semja þau úr sameiginlegu safni, sem mælanlega flýtir afhendingu og losar hönnuði og verkfræðinga fyrir vörusértæka vinnu. Aðgengi og svörun, leyst einu sinni í íhlutum, spara þér úrbótakostnað á hvert verkefni. Endurnýjun vörumerkis og þemun sem áður tók ár tekur nú vikur.

Hvað heildareignarkostnað varðar er upptökukostnaðurinn sérstakt teymi, verkfæri og fyrirhöfn fyrir núverandi vörur að flytja yfir á kerfið. Kostnaðurinn við að taka ekki upp er greiddur stöðugt: tvítekin smíði og viðhald yfir teymi, ósamræmd og óaðgengileg viðmót sem skapa stuðnings- og lagaáhættu og hæg, dýr vörumerkjaendurnýjun. Því tvítekningin dreifist yfir fjárhagsáætlanir margra teyma er auðvelt að líta framhjá henni: hönnunarkerfi gerir þennan falda kostnað sýnilegan og fangar hann á einum stað.

Til að færa rök við forystu skaltu magnsetja tvítekna íhlutavinnu yfir teymi, tímaávinning í markaðssetningu af samsetningu og kostnað og lengd síðustu vörumerkjaendurnýjunar þinnar á móti því sem táknað kerfi myndi leyfa. Rammaðu kerfið sem sameiginlega innviði með mælanlegan upptökumælikvarða (samsvörunarprósentu), svo gildi þess sé hægt að rekja með tímanum frekar en bara fullyrða.

## Andmynstur og gildrur

- **Hönnunarkerfi sem límmiðablað**: kyrrstæð hönnunarskrá án kóðaðra íhluta, svo verkfræðingar endurbyggja allt hvort sem er.
- **Harðkóðuð gildi alls staðar**: litir og bil dreifð um kóða, sem gerir þemun og vörumerkjaendurnýjun ómögulega.
- **Engir stjórnarhættir**: kerfið sundrast þegar teymi bæta við sundurleitum afbrigðum. Samræmi veðrast.
- **Stjórnarhættir án framlags**: miðlæga teymið verður flöskuháls og teymi fara framhjá því.
- **Að hunsa samsvörun**: kóðaða viðmótið rekur frá hönnunarásetningi og enginn mælir bilið.
- **Ofágripun**: svo mörg tákn og lög að enginn getur fundið eða notað rétta.
- **Vörumerkjarökfræði bökuð í íhluti**: gerir fjölvörumerki og þemun að kóðaendurskrift í stað stillingarbreytingar.
- **Brjótandi breytingar án flutningsstuðnings**: neytandi teymi stöðvast eða kvíslast kerfið.

## Þroskalíkan

**Stig 1: Upphaf.** Hvert teymi smíðar eigið viðmót ad hoc og viðbragðsdrifið. Engir sameiginlegir íhlutir, ósamræmt útlit og hegðun, litir og bil harðkóðuð á hvern skjá. Sérhver vörumerkjaendurnýjun er handvirk skjá-fyrir-skjá barátta.

**Stig 2: Þróun.** Sameiginleg stílleiðbeining eða íhlutasafn er til en er að hluta, valkvætt og oft úr takti milli hönnunar og kóða. Sum teymi nota það, önnur ekki, og grunnvinnubrögð eru mjög ólík frá teymi til teymis.

**Stig 3: Stöðlun.** Táknað hönnunarkerfi með viðhaldið kóðað safn, skjölun og stjórnarhætti er skjalfest og framfylgt um alla skipulagsheildina. Íhlutir neyta merkingarfræðilegra tákna, þemun er studd og aðgengi og svörun eru byggð inn frekar en fest á hvern skjá.

**Stig 4: Stjórnun.** Kerfið er mælt og stýrt með gögnum gegn grunnlínum. Hönnunar-kóða samsvörun er rakin sem skýr mælikvarði með markmiðum á hverja vöru, sjónræn afturfaraprófun keyrir í CI til að grípa rek og aðgengissamræmi er mælt gegn stöðlum frekar en gert ráð fyrir. Upptökumælaborð sýna íhlutaþekju eftir teymi og kostnaður og lengd vörumerkjaendurnýjunar eru skráð svo umbætur séu sýnilegar með tímanum.

**Stig 5: Samhæfing.** Hönnunarkerfið er stöðugt batnandi vara samþætt um skipulagsheildina og aðlögunarhæf að breytingum. Það hefur útgáfumerkingu, vegvísi og virkt framlagslíkan, svo það þróast með raunverulegum þörfum. Vörumerkjaendurnýjun og ný þemu eru rútínutáknabreytingar, fjölvörumerkja- og fjölleigendaþemun er eðlileg og teymið leggur niður, endurmarkar og færir upp mynstur á sönnunargögnum úr notkunargögnum og nærir hönnunarverkfæri og afhendingarleiðslur úr einni sannleiksuppsprettu.

## Hugmyndir til umræðu

- Hvernig jafnarðu miðlæga stjórnarhætti gegn sjálfræði teyma án þess að sundra eða stífla?
- Hver er rétti mælikvarðinn fyrir „hönnunar-kóða samsvörun“ og hvernig heldurðu honum heiðarlegum?
- Hvenær ætti teymi að mega smíða einnota íhlut í stað þess að nota kerfið?
- Hvernig fjármagnarðu og mannar hönnunarkerfi svo það lifi af fjárhagslotur og endurskipulagningar?
- Hve mikill þemun sveigjanleiki er virði aukins ágripunarkostnaðar?
- Hvernig flytur þú eldri forrit og söluaðilasmíðuð forrit yfir á sameiginlegt kerfi?

## Helstu atriði

- Hönnunarkerfi breytir einskiptis hönnunarákvörðunum í endurnýtanlegt, stýrt fjármagn.
- Byggðu það upp í lögum (tákn, íhlutir, mynstur), þar sem íhlutir neyta merkingarfræðilegra tákna.
- Byggðu aðgengi og svörun inn í íhluti svo hvert teymi erfi þau.
- Líttu á hönnunar-kóða samsvörun sem mælanlegan heilsumælikvarða, ekki forsendu.
- Táknun gerir vörumerkjaendurnýjun og fjölvörumerkjaþemun að gagnabreytingu, ekki endurskrift.
- Stýrðu kerfinu sem vöru með vegvísi, útgáfumerkingu og framlagslíkani.
- Í fyrirtækja- og opinberri stærð er sameiginlegt kerfi áhrifamesta viðmótsfjárfestingin sem í boði er.

## Heimildir og frekari lestur

- Brad Frost, *Atomic Design*
- Alla Kholmatova, *Design Systems: A Practical Guide to Creating Design Languages*
- Josef Müller-Brockmann, *Grid Systems in Graphic Design*
- Robert Bringhurst, *The Elements of Typographic Style*
- Ellen Lupton, *Thinking with Type*
- Luke Wroblewski, *Mobile First*
- Ethan Marcotte, *Responsive Web Design*
- Nathan Curtis, writings on design tokens and design system governance
- W3C Design Tokens Community Group, format specification
- Government design systems (e.g., UK Government Design System, U.S. Web Design System) as reference implementations
