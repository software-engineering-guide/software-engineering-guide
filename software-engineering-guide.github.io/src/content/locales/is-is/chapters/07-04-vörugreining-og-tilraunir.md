# 7.4 Vörugreining og tilraunir

## Yfirlit og tilgangur

Vörugreining er sú venja að skilja hvernig fólk notar vöru í raun með því að fanga og greina hegðun þess: hvaða eiginleika það snertir, hvar það nær árangri, hvar það hættir og hvað fær það til að koma aftur. Tilraunir eru sá agi að staðfesta orsök og afleiðingu með stýrðum prófunum, oftast [A/B-prófum](https://en.wikipedia.org/wiki/A/B_testing) (slembuðum samanburði tveggja afbrigða), svo þú dæmir vörubreytingar eftir raunverulegum áhrifum þeirra en ekki skoðun eða innsæi. Saman færa þau vöruákvarðanir frá „við teljum“ til „við vitum“, eða að minnsta kosti til „við mældum“.

Fyrir stór teymi eru þessi vinnubrögð úrslitaatriði. Þegar tugir teyma afhenda breytingar á vöru sem milljónir nota framleiðir óleiðbeint innsæi straum breytinga sem enginn getur mælt nettóáhrifin af, og háværasta röddin vinnur deilur sem gögn ættu að útkljá. Fyrirtæki nota tilraunir til að vernda tekjur og umbreytingu í stærð og grípa skaðlegar breytingar fyrir fulla útsetningu. Opinber stafræn þjónusta notar í auknum mæli sömu aðferðir til að bæta upptöku og klárun mikilvægrar þjónustu (bótaumsókna, skattaframtala, endurnýjunar leyfa), þar sem lítil bæting í klárunarhlutfalli verður að miklum ávinningi fyrir borgara og minna álagi á símaver.

Verðmæti vörugreiningar ræðst algerlega af gæðum mælinga og nákvæmni greiningar. Kæruleysisleg atburðarakning framleiðir gögn sem enginn treystir. Illa reknar tilraunir framleiða öruggar en rangar niðurstöður. Og af því þessi gögn eru hegðunarbundin og oft persónuleg verður þú að safna þeim á persónuverndarvirðandi, samþykkismeðvitaðan hátt, lagakrafa í mörgum lögsagnarumdæmum og siðferðileg skylda alls staðar. Þessi kafli fjallar um mælingar, kjarnahegðunargreiningar, ítarlega tilraunagerð, val á mælikvörðum sem skipta máli og að gera allt þetta af virðingu.

## Meginreglur

- Mældu af ásetningi með skjalfestri rakningaráætlun og samræmdri flokkun.
- Kjóstu stýrðar tilraunir fram yfir skoðun fyrir orsakaspurningar.
- Tölfræðileg nákvæmni er óumsemjanleg. Vanmáttugar eða prófanir með gægjum blekkja.
- Festu þig við norðurstjörnumælikvarða tengdan raunverulegu verðmæti, ekki hégómatölur.
- Mældu [varðveislu](https://en.wikipedia.org/wiki/Customer_retention) og þátttöku, ekki bara öflun.
- Safnaðu lágmarkshegðunargögnum sem þarf, með skýru samþykki.
- Líttu á mælingar sem vöru með eigendum og gæðaathugunum.
- Neikvæð eða flöt tilraunaniðurstaða er verðmæt uppgötvun, ekki bilun.

## Ráðleggingar

### Mældu með rakningaráætlun og flokkun

Áður en þú bætir við atburðum skaltu hanna rakningaráætlun: atburðina sem þú munt fanga, eiginleika þeirra, nafngiftavenjur og spurningarnar sem hver svarar. Framfylgdu samræmdri flokkun (stöðugu nafngiftakerfi fyrir atburði og eiginleika) svo gögn haldist greinanleg yfir teymi og tíma. Líttu á rakningaráætlunina sem stýrt skema: útgáfustýrðu hana, rýndu breytingar og staðfestu atburði gegn henni, svo þú grípir röng eða óvænt atburði við inntöku frekar en að uppgötva þá sem göt mánuðum síðar. Án þessa aga verða vörugögn ónothæfan graut ósamkvæmra, tvítekinna og óskjalfestra atburða.

### Greindu trektir, hópa, varðveislu og þátttöku

Notaðu trektir til að sjá hvar notendur hætta í lykilflæðum og til að beina umbótum. Notaðu [hópgreiningu](https://en.wikipedia.org/wiki/Cohort_analysis) til að bera saman hópa skilgreinda eftir því hvenær þeir komu eða hvað þeir gerðu, sem afhjúpar hvort breytingar bæta hegðun í raun yfir tíma. Mældu varðveislu (koma notendur aftur) því öflun án varðveislu er lekur fata. Lýstu þátttöku heiðarlega, með marktækum skilgreiningum á virkum notanda frekar en talningum sem smjaðra. Þessar greiningar, byggðar á hreinum mælingum, segja þér hvað er raunverulega að gerast í vörunni.

### Keyrðu ítarlegar tilraunir

Fyrir orsakaspurningar skaltu keyra stýrðar tilraunir: úthluta notendum af handahófi á afbrigði og bera saman niðurstöður. Nákvæmni krefst nokkurra aga. Reiknaðu úrtaksstærðina og lengdina sem þarf fyrir fullnægjandi [tölfræðilegt afl](https://en.wikipedia.org/wiki/Power_%28statistics%29) áður en þú byrjar. Hættu ekki snemma bara af því niðurstaða lítur marktæk út: gægjur blása upp falskar jákvæðar niðurstöður. Skilgreindu aðalmælikvarða og tilgátu fyrirfram, svo þú forðist að veiða hvaða marktæku niðurstöðu sem er yfir marga mælikvarða. Athugaðu að slembiröðun sé traust og að varnarmælikvarðar (afköst, tekjur, kvartanir) skaðist ekki. Notaðu tilraunavettvang til að staðla úthlutun, greiningu og varnarmælikvarða, svo hvert teymi keyri traust próf frekar en að finna upp tölfræði illa aftur.

### Veldu norðurstjörnumælikvarða og forðastu hégómamælikvarða

Veldu einn norðurstjörnumælikvarða sem fangar kjarnaverðmætið sem varan skilar notendum og sem gefur til kynna raunverulegan árangur þegar hann vex, ekki hégómatölu sem hækkar án samsvarandi verðmætis. Heildarfjöldi skráðra notenda, hrá síðuflettingar og uppsafnaðar niðurhalanir eru klassískir hégómamælikvarðar: þeir fara bara upp og endurspegla sjaldan heilsu. Kjóstu mælikvarða tengda afhentu og varðveittu verðmæti og umkringdu norðurstjörnuna með litlu mengi inntaksmælikvarða sem teymi geta í raun haft áhrif á. Varastu að fínstilla staðgengil svo hart að þú skaðir raunverulega markmiðið.

### Virtu persónuvernd og samþykki

Hegðunargögn eru persónugögn. Safnaðu aðeins því sem þú þarft í skilgreindum tilgangi, aflaðu og virtu samþykki eins og lög krefjast og veittu notendum gagnsæi og stjórn. Kjóstu samantekna og dulnefnda greiningu þar sem hún dugar, lágmarkaðu varðveislu og beittu sömu stjórnun, flokkun og aðgangsstýringum og á hvert viðkvæmt gagnasafn. Að virða persónuvernd gerir meira en að fullnægja reglum eins og [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) (almennu persónuverndarreglugerð ESB): það viðheldur trausti notenda sem varan byggir á. Hannaðu greiningu svo notandi sem afþakkar rakningu fái enn vinnandi vöru.

### Líttu á mælingar og tilraunir sem vörur

Gefðu mælingum eiganda sem ber ábyrgð á gæðum þeirra, þekju og skjölun og vaktaðu bilaða eða vantandi atburði eins og þú vaktar leiðslur. Byggðu upp tilraunamenningu með sameiginlegum vettvangi, rýni á tilraunahönnun og safni fyrri niðurstaðna svo skipulagsheildin læri smám saman frekar en að endurtaka próf og gleyma niðurstöðum.

## Málamiðlanir: kostir og gallar

| Val | Kostir | Gallar | Best passun |
|---|---|---|---|
| Þung mæling | Rík hegðunarinnsýn | Kostnaður, persónuverndarútsetning, hávaði | Gagnadrifnar vörur |
| Lágmarksmæling | Ódýr, lítil persónuverndaráhætta | Blindir blettir, veik greining | Snemmbúnar eða áhættulitlar vörur |
| A/B-tilraunir | Orsakavissa, ver mælikvarða | Krefst umferðar, tíma, nákvæmni | Vörur með mikla umferð |
| Afhenda og fylgjast með | Hratt, enginn umferðarþröskuldur | Ruglað, engin orsök | Lítil umferð eða afturkræfar breytingar |
| Norðurstjörnufókus | Samstilling, skýr forgangur | Of einföldun, hætta á kerfisbrellum | Flest vöruteymi |
| Margir KPI | Blæbrigði | Dreifður fókus, andstæð markmið | Þroskaðar greiningarskipulagsheildir |

Kjarnamálamiðlunin er hraði gegn vissu, miðluð af umferð. Tilraunir gefa orsakavissu, en þær krefjast nógu margra notenda og nógu mikillar þolinmæði til að ná tölfræðilegu afli. Fyrir eiginleika með litla umferð eða greinilega afturkræfar breytingar getur agað afhenda-og-fylgjast-með verið raunsætt. Mæling skiptir innsýn fyrir kostnað og persónuverndarútsetningu, svo safnaðu af tilgangi frekar en að hamstra. Og norðurstjörnumælikvarði skiptir blæbrigðum fyrir samstillingu: öflugur fyrir fókus, hættulegur ef spilað er á hann, svo paraðu hann við varnarmælikvarða.

## Spurningar til að ræða með teyminu

1. **Hver á rakningaráætlun ykkar og staðfestið þið atburði gegn henni við inntöku svo röng gögn bili snemma í stað þess að birtast sem göt mánuðum síðar?** Kaflinn lítur á rakningaráætlunina sem stýrt skema: útgáfustýrt, rýnt og staðfest, með samræmdri flokkun svo gögn haldist greinanleg yfir teymi og tíma. Án þess aga hnigna vörugögn í ónothæfan graut ósamkvæmra, tvítekinna og óskjalfestra atburða og þið uppgötvið götin aðeins þegar þið reynið að svara spurningu. Fyrir vöru sem tugir teyma og milljónir notenda snerta þýðir rakningaráætlun án eiganda að hvert teymi nefnir atburði öðruvísi og engin þverteymisgreining heldur. Komdu með sönnunargögn: veldu lykiltrekt og athugaðu hvort atburðir hennar séu skjalfestir og samræmt nefndir. Ef eignarhald er óljóst skaltu úthluta því og vakta bilaða eða vantandi atburði eins og þú vaktar leiðslur.

2. **Keyra öll teymi ykkar tilraunir gegnum sameiginlegan vettvang með aflútreikningum og varnarmælikvörðum, eða finnur hvert upp tölfræði illa aftur?** Kaflinn er hreinskilinn að nákvæmni er óumsemjanleg: reiknaðu úrtaksstærð og lengd fyrir fullnægjandi tölfræðilegt afl fyrir upphaf, skilgreindu aðalmælikvarða og tilgátu fyrirfram, gægstu ekki og hættu ekki snemma og fylgstu með varnarmælikvörðum eins og afköstum, tekjum og kvörtunum. Sameiginlegur tilraunavettvangur staðlar úthlutun, greiningu og varnir svo hvert teymi keyri traust próf frekar en að hvert teymi gægist þar til eitthvað lítur marktækt út. Fyrir fyrirtækjavörur með mikla umferð getur ein afstýrð slæm útgáfa (endurhönnun sem hljóðlega skaðaði varðveislu) borgað fyrir alla áætlunina. Komdu með merki: reikna teymi afl nú, eða hætta þau þegar niðurstaða lítur vel út? Ef það er hið síðarnefnda er sameiginlegur vettvangur og hönnunarrýni lagfæringin.

3. **Hvernig virkar varan enn fyrir notanda sem afþakkar rakningu og eruð þið að safna aðeins lágmarkshegðunargögnum fyrir skilgreindan tilgang?** Kaflinn lítur á hegðunargögn sem persónugögn: safnaðu aðeins því sem skilgreindur tilgangur þarf, aflaðu og virtu samþykki eins og lög krefjast, lágmarkaðu varðveislu og beittu sömu flokkun og aðgangsstýringum og á hvert viðkvæmt gagnasafn. Að virða þetta viðheldur trausti notenda sem varan byggir á og undir GDPR og svipuðum reglum er það lagakrafa, ekki kurteisi. Þrýstingurinn á móti er löngunin til að mæla þungt fyrir ríkari innsýn, sem hækkar kostnað, hávaða og persónuverndarútsetningu. Komdu með sönnunargögn: skráðu hvað þið safnið og tengdu hvern atburð við spurningu sem hann svarar, athugaðu síðan að afþökkun rakningar skili enn vinnandi vöru. Ef einhver söfnun hefur engan tilgang eða brýtur upplifunina skaltu skera hana burt og hanna greiningu til að skerðast mjúklega fyrir notendur sem afþakka.

4. **Hvaða einn norðurstjörnumælikvarði fangar verðmætið sem varan skilar og hvernig stöðvið þið teymi frá því að spila á staðgenglinn þar til raunverulega markmiðið líður?** Norðurstjörnumælikvarði samstillir mörg teymi um eina skilgreiningu á árangri, samt varar kaflinn við því að staðgengill fínstilltur of hart geti skaðað markmiðið sem hann átti að tákna, og að hégómatölur eins og heildarfjöldi skráðra notenda eða uppsafnaðar niðurhalanir klifra aðeins án þess að endurspegla heilsu. Fyrir stóra skipulagsheild þar sem tugir teyma elta hvert eigin markmið framleiðir óljós eða spilanleg norðurstjarna staðbundna sigra sem leggjast saman í engar raunverulegar umbætur, eða verra, hljóðlátan skaða sem enginn tekur eftir. Komdu með núverandi norðurstjörnuframbjóðanda, litla mengið inntaksmælikvarða sem teymi geta í raun haft áhrif á og varnirnar sem myndu grípa kerfisbrellur, prófaðu síðan hvern skýrðan mælikvarða með því að spyrja hvort hann gæti hækkað á meðan notendur hafa það verra. Í fyrirtækja- og opinberu umhverfi þar sem fyrirsagnarmælikvarði getur knúið fjárveitingu og opinbera skýrslugerð skaltu tengja norðurstjörnuna við skilgreiningu á varðveittu verðmæti eða kláruðum niðurstöðum svo enginn geti blásið hana upp með því að elta skráningar eða smelli sem aldrei umbreytast.

5. **Fyrir eiginleika með litla umferð, hvar liggur heiðarleg lína milli agaðs afhenda-og-fylgjast-með og fullrar stýrðrar tilraunar og hver ákveður?** Tilraunir gefa orsakavissu, en þær þurfa nógu marga notendur og nógu mikla þolinmæði til að ná tölfræðilegu afli, og að þvinga vanmáttuga prófun á flæði með litla umferð brennir vikum til að framleiða niðurstöðu sem getur ekki greint áhrifin sem hún leitar. Áhættan á móti er að afhenda-og-fylgjast-með er ruglað og sannar ekkert um orsök, svo að meðhöndla það sem jafngilt tilraun leyfir teymum að fullyrða sigra sem voru í raun árstíðabundnir eða tilviljun með samtímabreytingu. Komdu með umferðar- og umbreytingarmagn flæðisins sem um ræðir, minnsta greinanlega áhrif sem þú hefur áhuga á og afturkræfni breytingarinnar, og samþykktu síðan reglu: tilraun yfir umferðarþröskuldi, afhenda-og-fylgjast-með með skýrum vörnum fyrir neðan hann. Fyrir fyrirtækjavörur sem vernda tekjur og opinbera þjónustu þar sem afturför skaðar borgara skaltu nefna hver hefur vald til að víkja frá tilraun og krefjast þess að afturkræfar breytingar haldist raunverulega afturkræfar svo slæmt afhenda-og-fylgjast-með megi draga hratt til baka.

6. **Skráið þið neikvæðar og flatar tilraunaniðurstöður í sameiginlegt safn, eða uppgötvar skipulagsheildin sömu blindgöturnar aftur og aftur?** Kaflinn er skýr um að flöt eða neikvæð niðurstaða er verðmæt sönnun, ekki bilun, samt gufar lærdómurinn upp án leitarhæfs niðurstöðusafns og annað teymi endurkeyrir sama tapandi prófið ári síðar. Fyrir stóra skipulagsheild margfaldast þetta, því uppsafnaður lærdómur er öll ávöxtun tilraunamenningar og hann safnast aðeins ef tilraunahönnun og niðurstöður eru skrifaðar niður þar sem næsta teymi finnur þær. Komdu með fjölda tilrauna sem keyrðar voru síðasta ársfjórðung, hve margar niðurstöður eru skjalfestar og finnanlegar og hvort nokkur athugar safnið í raun áður en nýtt próf er hannað. Í fyrirtækja- og opinberu umhverfi þjónar varanleg skrá líka úttekt og ábyrgð og sýnir að ákvörðun hvíldi á sönnunargögnum frekar en skoðun og gefur rýnum verjanlega slóð þegar breyting sem snýr að almenningi er dregin í efa.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Skrifaðu eins síðu rakningaráætlun fyrir virkjunar- og fyrstu-lotu atburði þína áður en þú bætir við einhverju öðru, svo elstu gögnin haldist hrein þegar teymið vex. Taktu frá raunveruleg A/B-próf fyrir flæðið með mesta magnið og notaðu vandað afhenda-og-fylgjast-með annars staðar, keyptu hýst greiningar- og tilraunatól frekar en að smíða eitt og haltu þig við einn norðurstjörnumælikvarða eins og virkjun. Safnaðu aðeins atburðunum sem svara lifandi spurningu, svo þú borgir ekki geymslukostnað eða persónuverndaráhættu fyrir gögn sem þú lest aldrei.

**Lítið fyrirtæki.** Án sérstaks greinanda og með þröngt fjárhagsáætlun skaltu halla þér að greiningu sem er innbyggð í verkfæri sem þú rekur nú þegar og líta á tilraunir sem stöku verðmæta æfingu frekar en viðvarandi áætlun. Valið er yfirleitt að kaupa fram yfir að smíða: innfelld trektar- og hópasýn slær sérsmíðaða leiðslu sem þú getur ekki viðhaldið. Beindu fáu prófunum sem þú keyrir að flæðinu sem knýr tekjur og meðhöndlaðu samþykki einfaldlega og heiðarlega svo viðskiptavinur sem afþakkar rakningu fái enn vinnandi vöru.

**Stórfyrirtæki.** Í stærð yfir mörg teymi er stjórnun vandinn: útgáfustýrð rakningaráætlun staðfest við inntöku, sameiginlegur tilraunavettvangur sem staðlar úthlutun, aflútreikninga og varnir og niðurstöðusafn svo teymi læri smám saman í stað þess að endurtaka próf. Gefðu mælingum nefndan eiganda vaktaðan eins og leiðsla, komdu þér saman um einn norðurstjörnumælikvarða umkringdan inntökum sem hægt er að hafa áhrif á og beittu sömu gagnaflokkun og aðgangsstýringum á hegðunargögn og á hvert viðkvæmt gagnasafn, með úttektarslóðum fyrir afleiddar útgáfuákvarðanir.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta hvert val. Safnaðu lágmarkshegðunargögnum fyrir skilgreindan tilgang, aflaðu og virtu samþykki og birtu á einföldu máli hvað þú rekur og hvers vegna, og gefðu fólki vinnandi þjónustu ef það afþakkar. Keyrðu stýrðar tilraunir á orðalag og uppsetningu eyðublaða til að lyfta klárun mikilvægrar þjónustu, haltu skjalfestri, verjanlegri skrá yfir hverja prófun fyrir úttekt og krefstu þess að sérhver greiningarseljandi upplýsi um gagnameðhöndlun og veiti flytjanleika svo þú forðist bindingu.

## Dæmi

**Sprotafyrirtæki.** Lítið neytendaforrit skrifaði stutta, skjalfesta rakningaráætlun fyrir skráningar- og fyrstu-lotu atburði sína áður en það bætti við nýrri greiningu, svo gögnin héldust hrein þegar teymið óx. Trekt sýndi að flestir nýir notendur hættu við staðfestingarskrefið og einfalt A/B-próf á skýrara orðalagi lyfti varðveislu fyrstu viku. Með hóflega umferð keyrði teymið tilraunir aðeins á flæðin með mesta magnið og notaði vandað afhenda-og-fylgjast-með fyrir minni breytingar, á meðan virkjun var áfram norðurstjörnumælikvarðinn.

**Stórfyrirtæki.** Áskriftarstreymisþjónusta mælir með stýrðri rakningaráætlun og keyrir allar marktækar breytingar gegnum tilraunavettvang með fyrirfram skilgreindum mælikvörðum, aflútreikningum og vörnum á spilunarafköstum og brottfalli. Endurhönnuð innleiðsluflæði leit betur út í rýni, en stýrt próf sýndi að það minnkaði varðveislu fyrstu viku, svo teymið afturkallaði það fyrir víðtæka útsetningu, björgun sem var miklu meira virði en kostnaður vettvangsins.

**Hið opinbera.** Stofnun stafrænnar þjónustu mælir bótaumsóknarflæði sitt með persónuverndarvirðandi, samþykkismeðvitaðri rakningaráætlun og keyrir stýrðar tilraunir á orðalag og uppsetningu eyðublaða. Trektargreining afhjúpaði tiltekið skref þar sem þriðjungur umsækjenda gafst upp. Tilraun á skýrari leiðsögn jók klárun marktækt, sem dró úr bæði ófullkomnum umsóknum og magni í símaverum á meðan aðeins lágmarkshegðunargögnum var safnað.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun vörugreiningar og tilrauna birtist beint í niðurstöðum: hærri umbreytingu, varðveislu og klárun, og, mikilvægt, forðuðum kostnaði af því að afhenda skaðlegar breytingar. Tilraunir eru ein af fáum venjum sem magnsetja eigið verðmæti, því hvert próf skýrir frá lyftingunni eða tapinu sem það kom í veg fyrir. Góðar mælingar margfalda ávöxtun hverrar vöruákvörðunar með því að skipta ágiskun út fyrir sönnunargögn og norðurstjörnumælikvarði samstillir mörg teymi um sömu skilgreiningu á árangri.

Upptökukostnaðurinn felur í sér greiningar- og tilraunaverkfæri, verkfræðivinnu við að mæla vel, greiningarfærnina til að keyra próf af nákvæmni og persónuverndaráætlunarkostnað fyrir samþykki. Vegðu hann gegn kostnaði þess að taka ekki upp: að afhenda breytingar með óþekktum áhrifum, vinna deilur með starfsaldri frekar en sönnunargögnum, elta hégómamælikvarða sem smjaðra á meðan varan staðnar og eftirlitsútsetning af kæruleysislegri gagnasöfnun. Til stjórnenda er boðskapurinn að tilraunir breyti vöruþróun í mælanlegt, sjálfleiðréttandi ferli og að fyrsta afstýrða slæma útgáfan borgi oft fyrir alla áætlunina.

## Andmynstur og gildrur

- Að bæta við atburðum án rakningaráætlunar, sem framleiðir ósamkvæm, ónothæf gögn.
- Að gægjast á tilraunir og hætta þegar þær líta marktækar út, sem blæs upp falskar jákvæðar niðurstöður.
- Að prófa marga mælikvarða og fagna hverjum sem kemur marktækur af tilviljun.
- Að keyra vanmáttug próf sem geta ekki greint áhrifin sem þau leita.
- Að fínstilla hégómamælikvarða sem hækka án þess að endurspegla raunverulegt verðmæti.
- Að spila á staðgengilsmælikvarða svo hart að raunverulega markmiðið líður.
- Að hamstra hegðunargögn án samþykkis eða skilgreinds tilgangs.
- Að gleyma að skrá neikvæðar niðurstöður, svo skipulagsheildin endurtekur misheppnuð próf.

## Þroskalíkan

1. **Upphaf.** Mælingar eru strjálar eða ósamræmdar, ákvarðanir teknar eftir skoðun og starfsaldri, engar tilraunir keyra og hégómamælikvarðar eins og heildarskráningar eru skýrðir. Samþykki er meðhöndlað kæruleysislega.
2. **Þróun.** Sumir atburðir eru raktir, en flokkunin rekur milli teyma. Stöku ad hoc A/B-próf keyra án aflútreikninga, trektir og varðveisla eru skoðuð óformlega og norðurstjörnumælikvarði er lagður til en ekki enn innbyggður.
3. **Stöðlun.** Stýrð rakningaráætlun og samræmd flokkun eru skjalfestar, útgáfustýrðar og staðfestar við inntöku yfir hvert teymi. Trektir, hópar og varðveisla eru greind reglulega, tilraunir keyra á sameiginlegum vettvangi með fyrirfram skilgreindum mælikvörðum, aflútreikningum og vörnum og persónuvernd og samþykki eru meðhöndluð rétt um skipulagsheildina.
4. **Stjórnun.** Venjan er mæld gegn grunnlínum: mælingaþekja og villuhlutföll atburðagæða eru rakin, tilraunahraði og hlutfall útgáfa hliðuð af prófi er skýrt, brot á vörnum og gægjur eru gripin sjálfvirkt og norðurstjörnumælikvarðinn og inntaksmælikvarðar hans eru vaktaðir með skýrum drápsþröskuldum. Gagnagæði og persónuverndarfylgni eru úttektuð á föstum takti frekar en gert ráð fyrir.
5. **Samhæfing.** Tilraunir eru sjálfgefið fyrir hverja marktæka breytingu, mælingar eru í eigu og vaktaðar eins og leiðsla og sameiginlegt niðurstöðusafn sem inniheldur neikvæðar og flatar niðurstöður lætur skipulagsheildina læra smám saman og leggja niður blindgötur. Greining er samþætt vöru- og áhættuskipulagningu, persónuverndarvirðandi í hönnun og mælikvarðamengið er stöðugt endurmarkað þegar varan, markaðurinn og regluverk breytast.

## Hugmyndir til umræðu

- Hver er sanni norðurstjörnumælikvarði vöru ykkar og eru allir sammála um hann?
- Hverjir af skýrðum mælikvörðum ykkar eru hégómatölur sem fara bara upp?
- Reikna teymi ykkar tölfræðilegt afl áður en tilraunir eru keyrðar, eða gægjast þau og hætta?
- Hvar hafa mælingar ykkar blinda bletti sem fela sársauka notenda?
- Hvernig haldið þið greiningu persónuverndarvirðandi á meðan þið lærið samt það sem þið þurfið?
- Fyrir eiginleika með litla umferð, hvenær er afhenda-og-fylgjast-með ásættanlegt gegn fullri tilraun?

## Helstu atriði

- Mældu af ásetningi með stýrðri rakningaráætlun og samræmdri flokkun.
- Greindu trektir, hópa, varðveislu og þátttöku, ekki bara öflun.
- Keyrðu ítarlegar tilraunir: aflútreikninga, fyrirfram skilgreinda mælikvarða, engar gægjur.
- Festu þig við norðurstjörnumælikvarða tengdan raunverulegu verðmæti og varastu hégómamælikvarða.
- Safnaðu lágmarkshegðunargögnum með skýru samþykki og sterkri stjórnun.
- Líttu á mælingar sem vöru og byggðu upp tilraunamenningu sem safnar lærdómi.
- Flöt eða neikvæð tilraunaniðurstaða er verðmæt sönnun, ekki bilun.

## Heimildir og frekari lestur

- Ron Kohavi, Diane Tang, and Ya Xu, "Trustworthy Online Controlled Experiments."
- Alistair Croll and Benjamin Yoskovitz, "Lean Analytics."
- Eric Ries, "The Lean Startup."
- Avinash Kaushik, "Web Analytics 2.0."
- Georgi Georgiev, "Statistical Methods in Online A/B Testing."
- Regulation (EU) 2016/679, General Data Protection Regulation (GDPR).
- Douglas W. Hubbard, "How to Measure Anything."
