# 1.6 Ákvörðunarskrár

## Yfirlit og tilgangur

**Ákvörðunarskrá** er skjal sem fangar mikilvæga ákvörðun ásamt samhengi hennar og afleiðingum. Þekktasta formið er **[arkitektúrákvörðunarskráin](https://en.wikipedia.org/wiki/Architectural_decision) (ADR)**, stutt athugasemd, óbreytanleg að vali, sem skráir eitt arkitektúrlega mikilvægt val, hvers vegna það var gert og hvað af því leiðir. Heildarsafn skráa verkefnis er **ákvörðunarannáll þess (ADL)**, og agi þess að halda þeim er hluti af **arkitektúrþekkingarstjórnun (AKM)**. Þessi kafli byggir á ákvarðanatöku- og stjórnarháttavinnubrögðum kafla 1.5 og beinist að því hvernig þú skrifar, geymir og viðheldur ákvörðunarskrám í stórum stíl.

Tilgangurinn er einfaldur og sársaukafullt að læra á erfiða mátann. Á hverju langlífu kerfi er dýrasta spurningin „hvers vegna í ósköpunum var þetta smíðað svona?“, sem fólk spyr mánuðum eða árum síðar og var ekki í herberginu. Kóðinn sýnir *hvað* kerfið gerir. Prófanir sýna að það *virkar*. En hvorugt fangar *hvers vegna* þú valdir þessa leið fram yfir kostina sem þú skoðaðir og hafnaðir. Án ákvörðunarskráa gufa þessi rök upp með starfsmannaveltu. Teymi deila aftur um útkljáð mál, afturkalla góðar ákvarðanir af slæmum ástæðum eða halda slæmum ákvörðunum af ótta. Ákvörðunarskrá er ódýrt bréf til framtíðarinnar sem varðveitir rökin.

Fyrir stór teymi er þetta samhæfingartæki jafnt sem minnishjálp. Fyrirtæki reka tugi teyma sem taka skarandi ákvarðanir. Sameiginlegur ákvörðunarannáll breytir hörðu áunnum rökum eins teymis í endurnýtanlega eign og kemur í veg fyrir ólíkar, ósamrýmanlegar ákvarðanir. Hjá hinu opinbera og í eftirlitsskyldu umhverfi eru ákvörðunarskrár nærri skyldubundnar. Endurskoðendur, eftirlitsstofnanir og arftakaverktakar þurfa allir rekjanleg rök sem tengja arkitektúrlega mikilvægar kröfur við valin sem gerð voru gegn þeim. Vel haldinn ákvörðunarannáll er oft munurinn á kerfi sem þú getur tryggt og endurskoðað og kerfi sem þú getur ekki.

## Meginreglur

- **Skráðu *hvers vegna*, ekki bara *hvað*.** Samhengi og hafnaðir kostir eru tilgangurinn.
- **Ein ákvörðun í hverri skrá.** Hafðu hverja skrá sértæka og sjálfstæða.
- **Lítið og létt slær yfirgripsmikið og ónotað.** Einnar blaðsíðu skrá sem er til slær skýrslu sem aldrei er skrifuð.
- **Tímamerktu allt.** Kostnaður, skorður og söluaðilar breytast. Dagsettu hverja fullyrðingu.
- **Kjóstu lifandi annál, í raunsæi.** Óbreytanleiki er hugsjónin. Í reynd skaltu breyta með dagsettum athugasemdum.
- **Orð fram yfir skammstafanir.** „Ákvarðanir“ býður fleiri framlög en „ADR“.
- **Gerðu ákvarðanir finnanlegar og, þar sem hægt er, prófanlegar.** Dragðu fram réttu skrána á réttu augnabliki. Tryggðu hana með hæfnisföllum.

## Ráðleggingar

### Fangaðu nauðsynlega uppbyggingu

Góð ákvörðunarskrá hefur fáa nauðsynlega hluta. Lagaðu þekkt sniðmát frekar en að finna upp nýtt:

- **Titill:** stutt boðháttarsetning í nútíð („Notum [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) fyrir höfuðbókina“).
- **Staða:** tillaga, samþykkt, leyst af hólmi, úrelt.
- **Samhengi:** aðstæðurnar, kraftarnir, viðskiptaforgangsröðun og skorðurnar sem gera þessa ákvörðun nauðsynlega. Taktu með arkitektúrlega mikilvægu kröfuna sem hún tekur á.
- **Ákvörðun:** valið sem var gert, sagt skýrt.
- **Afleiðingar:** hvað verður auðveldara og hvað erfiðara, framhaldsákvarðanir sem hún kallar fram og áhætta sem er samþykkt.

Vinsæl sniðmát eru sniðmát Michael Nygard (einfalt og víða tekið upp), sniðmát Tyree og Akerman (ítarlegra, með vegnum valkostum), MADR (Markdown Any Decision Records, sterkt á valkosti og kosti þeirra og galla) og Y-yfirlýsingar (eins setningar skipulagt form). Staðlaðu á eitt fyrir hverja skipulagsheild svo skrár séu sambærilegar. Sjá kafla 12.3 fyrir sniðmát til að afrita.

### Skrifaðu skrár sem eru sértækar, dagsettar og nánast óbreytanlegar

Hafðu hverja skrá um nákvæmlega eina ákvörðun. Tímamerktu einstakar fullyrðingar, sérstaklega allt sem rekur: verðlagningu, stærðartölur, getu söluaðila, leyfisskilmála. Í kenningu ætti skrá að vera óbreytanleg. Þegar ákvörðun breytist skrifarðu *nýja* skrá sem leysir þá gömlu af hólmi og varðveitir söguna. Í reynd finna mörg teymi að **lifandi skjal**-nálgun virkar betur: bættu nýjum upplýsingum inn í núverandi skrá með dagsetningu og athugasemd um að þær hafi borist eftir ákvörðunina. Hvort tveggja er lögmætt. Óbreytanlegi stíllinn er sterkari fyrir úttektarslóðir. Lifandi stíllinn er betri fyrir daglega teymisþekkingu. Veldu af ásetningi og vertu samkvæmur.

### Geymdu skrár þar sem vinnan er

Settu ákvörðunarskrár í [útgáfustýringu](https://en.wikipedia.org/wiki/Version_control) ásamt kóðanum: `decisions/` (eða `adr/`) möppu af [Markdown](https://en.wikipedia.org/wiki/Markdown)-skrám, eina fyrir hverja ákvörðun, nefndar með lágstöfum, bandstrikaskiptri boðháttarsetningu (`choose-database.md`, `format-timestamps.md`). Þetta gefur þér sögu, rýni og mismunargreiningu ókeypis og heldur rökunum við hlið þess sem þau útskýra. Ef teymið þitt kýs [wiki](https://en.wikipedia.org/wiki/Wiki), Google Docs eða Jira-líkan verkefnaskráa skaltu nota það í staðinn. Verkfærið skiptir mun minna máli en venjan. Létt skipanalínuverkfæri (eins og `adr-tools`) getur smíðað grind og skráð skrár.

### Nefndu þær „ákvarðanir“ og víkkaðu út fyrir arkitektúr

Hagnýt innsýn frá mörgum teymum: heitið skiptir máli. Sumir hönnuðir og stjórnendur fussa við orðinu „arkitektúr“ og „skrá“ getur virst eins og pappírsvinna eftir á. Að endurnefna möppuna einfaldlega „decisions“ snýr oft rofa. Teymi byrja að skrá val á söluaðilum, skipulagsákvarðanir, tímasetningarákvarðanir, gagna- og regluvarsluákvarðanir, allt með sama sniðmáti. Fólk lærir hraðar af orðum en skammstöfunum og leggur meira af mörkum þegar rammað er inn sem „hjálpaðu framtíðarliðsfélögum þínum að hugsa“ frekar en „fylltu út skyldueyðublaðið“.

### Skilgreindu lífsferil og stjórnarhætti

Til að ákvörðunarskrár skali skaltu koma þér saman um ferlið í kring (hér mætast stjórnarhættir kafla 1.5 og framkvæmdin):

- **Hver getur stofnað eina og hvað réttlætir það:** venjulega hver upplýstur þátttakandi. Stofnaðu skrá þegar framtíðarhönnuðir þurfa *hvers vegna*, og slepptu henni fyrir áhættulítil, sjálfstæð eða þegar skjalfest val.
- **Lífsferill:** einfalt flæði eins og *Upphaf → Rannsókn → Mat → Innleiðing → Viðhald → Lok*, með samþykkisviðmiðum til að færa sig milli stiga (vandi lýstur, kostir skoðaðir, málamiðlanir skjalfestar, hagsmunaaðilar hafðir með).
- **Hlutverk:** tillögumaður, rannsakandi, rýnir, samþykkjandi og ábyrgur umsjónarmaður sem rýnir skrána reglulega (að minnsta kosti árlega) og knýr loks fram lok hennar.
- **Stjórnarhættir:** hvernig samstaða, ágreiningur, stigmögnun og neitunarvald virka, og allar regluvarsluskorður. Hallaðu þér að meginreglum eins og *tilhneigingu til aðgerða* og *[ósammála-og-skuldbinda-sig](https://en.wikipedia.org/wiki/Disagree_and_commit)*, og taktu frá þyngra ferli fyrir óafturkræfar ákvarðanir með mikið sprengisvæði („einátta dyr“).

### Gerðu ákvarðanir prófanlegar og finnanlegar

Ákvörðunarskrá *skjalfestir* ákvörðun. **Hæfnisfall** *tryggir* hana: sjálfvirk athugun, keyrð í [samfelldri samþættingu](https://en.wikipedia.org/wiki/Continuous_integration) (CI), sem staðfestir að ákvörðunin standi enn („allar ástandsbreytingar verða að senda atburði“, „engin eining má flytja inn yfir þessi mörk“, með verkfærum eins og ArchUnit). Þetta breytir stjórnarháttum úr reglulegri handvirkri rýni í samfellda, skalanlega framfylgd, sem er sérstaklega verðmætt fyrir regluvörslu- og úttektarmarkmið (kaflar 3.1, 4.6, 8.5). Dragðu síðan *réttu* skrána fram á *réttu* augnabliki. Verkfæri sem tengja viðeigandi ákvarðanir við sameiningarbeiðni þegar hönnuður snertir kóðann sem þær stýra slá því að vona að fólk lesi skjalamöppu.

## Málamiðlanir: kostir og gallar

| Val | Kostir | Gallar |
|---|---|---|
| **Léttar ADR (Nygard/MADR)** | Fljótlegar að skrifa, eru í raun skrifaðar, lítill helgisiðakostnaður | Minni nákvæmni fyrir mikilvægar, umdeildar ákvarðanir |
| **Þung sniðmát (Tyree-Akerman)** | Vegnir kostir, sterkt fyrir stór, dýr val | Hægara, getur fælt frá reglubundinni skráningu |
| **Óbreytanlegt + leyst af hólmi** | Hrein úttektarslóð, saga varðveitt | Fleiri skrár, lesendur þurfa að rekja keðjur |
| **Lifandi skjal (dagsettar breytingar)** | Ein núverandi sannleiksuppspretta, auðvelt að viðhalda | Veikari úttektarsaga, hætta á hljóðlátum breytingum |
| **Markdown í hugbúnaðarsafni** | Útgáfustýrt, rýnanlegt, við hlið kóða | Minna vinalegt þeim sem eru ekki hönnuðir |
| **Wiki / skjalaverkfæri** | Aðgengilegt öllum hlutverkum | Veikari saga og rýni, rekur frá kóða |

Kjarnaspennan er **nákvæmni gegn upptöku**. Nákvæmasta kerfið sem enginn notar skráir ekkert. Léttasta kerfið sem allir nota safnar virði. Hafðu létt sem sjálfgefið og taktu frá þyngra ferli fyrir fáar ákvarðanir sem eru dýrar og erfitt að afturkalla.

## Spurningar til að ræða með teyminu

1. **Hvernig kemst rétta ákvörðunarskráin til hönnuðar á því augnabliki sem hann snertir kóðann sem hún stýrir, frekar en að liggja í möppu sem enginn opnar?** Skrifstýrður annáll skráir rök sem breyta aldrei hegðun, sem er algengasta leiðin sem ákvörðunarskrár bregðast: þær eru til og enginn les þær þegar það skiptir máli. Sjónarmiðið á móti er fyrirhöfn, því að draga skrár fram sjálfvirkt (festa þær við sameiningarbeiðni þegar einhver breytir stýrða kóðanum) krefst verkfærafjárfestingar sem wiki eða skjalamappa krefst ekki. Komdu með gögn í umræðuna: þegar einhver afturkallaði eða deildi nýlega aftur um útkljáða spurningu, var viðeigandi skrá finnanleg á því augnabliki, eða grafin? Fyrir stóra skipulagsheild sem rekur tugi teyma er finnanleiki það sem breytir hörðu áunnum rökum eins teymis í endurnýtanlega eign í stað einkaskjalasafns. Ákveddu hvort þú geymir skrár í útgáfustýringu við hlið kóðans og tengir þær inn í sameiningarbeiðnaflæðið, svo skráin birtist þar sem vinnan gerist.

2. **Hver er ábyrgur umsjónarmaður hverrar skrár, og hvað kemur í veg fyrir að annállinn hnigni í sjálfsörugga rangupplýsingu?** Hættulegur bilunarháttur ákvörðunarannáls er ekki tóm mappa, heldur mappa full af skrám þar sem kostnaður, geta söluaðila og skorður úreltust hljóðlega fyrir árum. Sérhver skrá þarf ábyrgan eiganda sem rýnir hana reglulega (að minnsta kosti árlega) og knýr fram að hún sé leyst af hólmi eða lögð niður, annars rotnar annállinn í þjóðsögur sem fólk vitnar í sértækt og treystir lítið. Komdu með gögn: hve margar skrár eru án dagsetningar, hve margar lýsa söluaðila eða verði sem hefur síðan breyst og hvenær hver var síðast rýnd. Hjá hinu opinbera og í eftirlitsskyldu umhverfi er þetta skarpara, því óbreytanleg, afleyst keðja er einmitt það sem endurskoðendur og arftakaverktakar reiða sig á fyrir rekjanleg rök. Ákveddu lífsferilinn skýrt, tímamerktu einstakar fullyrðingar sem reka og úthlutaðu umsjónarmönnum, svo annállinn haldist lifandi eign en ekki kirkjugarður.

3. **Ættir þú að staðla á eitt sniðmát yfir öll teymi, og hversu mikla nákvæmni þurfa mikilvægustu ákvarðanir þínar í raun?** Samanburðarhæfni er raunverulegur ávinningur: þegar öll teymi nota sömu lögun (Nygard, MADR eða svipað) getur nýtt teymi fundið þrjár fyrri skrár og tileinkað sér rökin á eftirmiðdegi í stað mánaðar umræðna. Kjarnaspennan er nákvæmni gegn upptöku, því þyngsta sniðmátið sem enginn notar skráir ekkert, á meðan léttasta sem allir nota safnar virði. Komdu með gögn: eru skrár í raun skrifaðar, og sérstaklega, hafa einhverjar stórar, umdeildar, dýrar ákvarðanir verið vangreindar því létta formið sleppti því að vega kosti? Fyrir fyrirtæki sem samhæfa skarandi val milli teyma kemur sameiginlegt sniðmát ásamt leitanlegri skrá í veg fyrir ólíkar, ósamrýmanlegar ákvarðanir. Hafðu létt sem sjálfgefið fyrir algenga tilvikið og komdu þér fyrirfram saman um hvaða einátta dyra-ákvarðanir verðskulda þyngra form með vegnum kostum.

4. **Hvað réttlætir í raun að stofna ákvörðunarskrá, og hver hefur vald til að segja að val þurfi enga?** Settu mörkin of hátt og rökin að baki afdrifaríkum valum gufa upp. Settu þau of lágt og annállinn fyllist af smáatriðum sem grafa skrárnar sem fólk raunverulega þarf. Fyrir stóra skipulagsheild þýðir óskýr þröskuldur að hvert teymi spinnur sinn eigin, svo þekja verður ójöfn og enginn getur treyst að skrá sem vantar bendi á ómikilvæga ákvörðun. Komdu með gögn í umræðuna: handfylli nýlegra ákvarðana sem voru skráðar en þurftu þess ekki, og sársaukafullar sem voru óskráðar og kostuðu þig síðar enduruppgötvun. Komdu þér saman um einfalt próf, svo sem að skrá hvenær sem framtíðarhönnuður mun þurfa *hvers vegna* og sleppa áhættulitlum, sjálfstæðum eða þegar skjalfestum valum. Í eftirlitsskyldu og opinberu samhengi breytist reikningurinn, því úttektarkrafa kann að krefjast skrár fyrir hverja arkitektúrlega mikilvæga kröfu hvort sem teymið telur hana þess virði að skrifa, svo nefndu hvaða ákvarðanir eru óumsemjanlegar fyrirfram.

5. **Eru skrárnar þínar ósvikin rök sem fönguð voru á ákvörðunarstundu, eða pappírsvinna skrifuð eftir á til að uppfylla skyldu?** Skrá sem er búin til eftir á til að loka miða hneigist til að þvo valinn kost og sleppa hljóðlega kostunum sem voru í raun vegnir, sem er einmitt upplýsingarnar sem framtíðarlesandi þarf mest. Þrýstingurinn á móti er raunverulegur: að skrifa *hvers vegna* fyrir eða meðan á ákvörðun stendur finnst hægara en að afhenda, og að viðurkenna hafnaðar leiðir skriflega krefst sálfræðilegs öryggis sem sum teymi skortir. Komdu með úrtak nýlegra skráa að borðinu og spurðu heiðarlega hvort samhengið og hafnaðir kostir lesist sem raunveruleg yfirvegun eða eftirá-smíðaður rökstuðningur. Fyrir stórt teymi eru tómar skrár verri en engar, því þær kenna fólki að annállinn sé ekki treystandi. Í úttektum fyrirtækja og hins opinbera er þessi greinarmunur skarpur: eftirlitsaðilar og arftakaverktakar reiða sig á rök sem endurspegla það sem í raun var skoðað, og skrá sem lesist sem leikhús grefur undan tryggingunni sem annállinn er til að veita.

6. **Hverjar mikilvægustu ákvarðana þinna geturðu tryggt með sjálfvirku hæfnisfalli, frekar en að treysta að reglubundin handvirk rýni grípi brot?** Ákvörðunarskrá skjalfestir val, en aðeins sjálfvirk athugun keyrð í samfelldri samþættingu heldur því vali frá því að veðrast hljóðlega þegar tugir hönnuða snerta kóðann árum saman. Málamiðlunin er fjárfesting, því að skrifa og viðhalda hæfnisföllum (með verkfærum eins og ArchUnit) kostar verkfræðitíma, og margar ákvarðanir, sérstaklega ferla- eða söluaðilaval, eru alls ekki vélrænt prófanlegar. Komdu með gögn: hvaða markaákvarðanir (einingaósjálfstæði, atburðasendingar, gagnaaðgangsreglur) hafa verið hljóðlega brotnar og aðeins gripnar seint í rýni eða í framleiðslu. Fyrir fyrirtæki sem rekur mörg teymi breyta hæfnisföll stjórnarháttum úr miðlægum flöskuhálsi í samfellda framfylgd sem skalar án þess að hægja á öllum. Í eftirlitsskyldu og opinberu samhengi er sjálfvirk, sífellt virk athugun mun sterkari úttektargögn en undirskrift á rýni, því hún sannar að ákvörðunin stendur enn í dag en ekki að einhver samþykkti hana einu sinni.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Haltu þig við venjuna og ekkert annað: `decisions/` mappa í aðalhugbúnaðarsafninu og tveggja hluta athugasemd (samhengi og val) hvenær sem þú tekur ákvörðun sem framtíðarsjálf þitt mun efast um. Slepptu lífsferli, hlutverkum og samþykkjendum alveg, því ferli sem þú getur ekki haldið uppi er ferli sem þú munt yfirgefa. Eina skráin sem sparar fyrsta starfsmanni þínum að spyrja hvers vegna kerfið er smíðað svona borgar þegar fyrir alla venjuna.

**Lítið fyrirtæki.** Án sérstaks arkitekts og með lítinn tíma skaltu setja skrár þar sem teymið vinnur nú þegar, hvort sem það er wiki, sameiginlegt skjal eða hugbúnaðarsafnið, frekar en að kaupa sérverkfæri. Venjan skiptir miklu meira máli en verkfærin, svo lækkaðu þröskuldinn: nefndu möppuna `decisions` fremur en `adr` og fangaðu söluaðila- og smíða-eða-kaupa-val í sömu andrá og tæknileg. Þegar þú reiðir þig á utanaðkomandi verktaka er stutt, dagsett skrá um hvers vegna þú valdir söluaðila eða vettvang ódýr trygging gegn því að vera læstur inn í val sem enginn getur síðar útskýrt.

**Stórfyrirtæki.** Vinnan er samhæfing milli margra teyma: staðlaðu á eitt sniðmát, birtu leitanlega skrá yfir teymi og styddu lykilmarkaákvarðanir með hæfnisföllum svo brot mistakist í smíð í stað þess að bíða rýni. Úthlutaðu ábyrgum umsjónarmanni á hverja skrá með rýnitakti, svo annállinn haldist lifandi eign í stað þess að hnigna í þjóðsögur. Vel gert verður rökstuðningur eins teymis um erfitt val að eign sem næsta teymi tileinkar sér á eftirmiðdegi í stað þess að deila aftur um.

**Hið opinbera.** Innkaupareglur, gagnsæi og almenn ábyrgð gera ákvörðunarskrár nærri skyldubundnar. Krefstu óbreytanlegrar, afleystrar skrár fyrir sérhverja arkitektúrlega mikilvæga kröfu, hverja tengda ákvörðuninni við umboðið eða regluvörslumaðgerð sem hún fullnægir, svo eftirlitsaðilar finni rekjanleg rök en ekki endurgerð. Því opinber kerfi spanna margra ára, margra söluaðila líftíma er vel haldinn annáll oft það sem leyfir arftakaverktaka að skilja hvers vegna kerfið er mótað eins og það er og halda vinnunni áfram án þess að deila aftur um útkljáð mál.

## Dæmi

**Sprotafyrirtæki.** Fimm manna sprotafyrirtæki bætir einfaldri `decisions/` möppu við aðalhugbúnaðarsafnið sitt, með tveggja hluta athugasemd (samhengi og val) hvenær sem einhver tekur ákvörðun sem framtíðarsjálf þeirra munu efast um. Þar er enginn lífsferill, engin hlutverk og engir samþykkjendur: bara venjan að skrifa *hvers vegna* við hlið kóðans. Þegar fyrsti starfsmaðurinn hefst handa sex mánuðum síðar les hún alla möppuna á klukkustund og hættir að spyrja „hvers vegna er þetta smíðað svona?“. Létti annállinn kostar mínútur á færslu og sparar þeim enduruppgötvunarskattinn sem bítur löngu áður en teymi stækkar.

**Stórfyrirtæki.** Verslunarkeðja með 30 verkfræðiteymi staðlar á MADR-sniðnar skrár í hverju hugbúnaðarsafni, auk leitanlegrar miðlægrar skrár. Þegar nýtt teymi stendur frammi fyrir „[einsafn](https://en.wikipedia.org/wiki/Monorepo) á móti fjölsafni“ finna þau þrjár fyrri skrár með samhengi og afleiðingum og tileinka sér rökin á eftirmiðdegi í stað mánaðar umræðna. Lykilmarkaákvarðanir (þjónustueignarhald, gagnaaðgangsreglur) eru studdar af ArchUnit-hæfnisföllum, svo brot mistakast í smíð í stað þess að vera gripin í rýni. Það eru stjórnarhættir sem skala án miðlægs flöskuhálss.

**Hið opinbera.** Stofnun sem nútímavæðir bótakerfi krefst ADR fyrir sérhverja arkitektúrlega mikilvæga kröfu, hverja tengda ákvörðuninni við umboðið eða regluvörslumaðgerð sem hún fullnægir (aðgengi, gagnabúseta, úttektarhæfi). Skrár eru óbreytanlegar og afleystar, sem framleiðir rekjanlegan annál sem fullnægir eftirlitsrýni. Mikilvægast er að það leyfir arftakaverktaka að skilja *hvers vegna* kerfið er mótað eins og það er, sem varðveitir samfellu yfir margra ára, margra söluaðila líftíma sem er dæmigerður fyrir opinber verkefni (kaflar 4.6, 10.4).

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ákvörðunarskrá kostar mínútur að skrifa og nokkrar í viðbót að rýna. Ávöxtunin er forðaður *endurákvörðunar*kostnaður og forðaður *rangafturköllunar*kostnaður, hvort tveggja stórt og endurtekið á langlífum kerfum. Í hvert sinn sem teymi deilir aftur um útkljáða spurningu, eða afturkallar traust val því enginn mundi skorðuna að baki, borgar það í tíma eldri verkfræðinga og oft í atviki. Ákvörðunarannáll breytir þeim endurtekna skatti í einskiptis skrif.

Hvað varðar **heildareignarkostnað** eru ákvörðunarskrár meðal áhrifamestu skjala sem þú getur haldið, því þær beinast að þeirri einu eign sem er viðkvæmust fyrir starfsmannaveltu: rökunum. Móttaka er hraðari (nýir starfsmenn lesa *hvers vegna*, ekki bara kóðann). Nútímavæðing er öruggari (kafli 3.6: þú getur greint nauðsynlegar ákvarðanir frá tilviljanakenndum). Úttektir eru ódýrari (sönnunin er þegar til). Kostnaðurinn við að halda þær *ekki* er ósýnilegur á hverju mælaborði og safnast hljóðlega upp við hverja brottför. Til að færa rök fyrir þessu við forystu skaltu benda á nýlega dýra enduruppgötvun, eða afturkallaða ákvörðun sem olli atviki, og taka fram að lagfæringin kostar næstum ekkert að koma á.

## Andmynstur og gildrur

- **Að skrá *hvað* án *hvers vegna*:** að sleppa samhengi og hafnaðum kostum, sem er allur tilgangurinn.
- **Pappírsvinna eftir á:** skrár skrifaðar til að fullnægja skyldu, ekki til að hugsa. Þær lesast tómar og enginn treystir þeim.
- **Risaskjöl með mörgum ákvörðunum:** ein risablaðsíða sem enginn getur rata um eða leyst hreint af hólmi.
- **Ódagsettar fullyrðingar:** kostnaður og skorður sem voru einu sinni sannar, settar fram sem tímalausar.
- **Hljóðlátar breytingar:** að breyta sögu ákvörðunar án dagsettrar athugasemdar og eyðileggja úttektarslóðina.
- **Skrifstýrðir annálar:** skrár búnar til og aldrei dregnar fram þegar þær eiga við, svo þær hafa ekki áhrif á hegðun.
- **Skammstafanahliðvarsla:** að heimta „ADR“ og „arkitektúr“ og letja þannig framlög.
- **Enginn lífsferill:** skrár sem aldrei eru rýndar, leystar af hólmi eða lagðar niður og hnigna í rangupplýsingu.

## Þroskalíkan

- **Stig 1 (Upphaf):** Ákvarðanir lifa í höfðum fólks, spjallþráðum og commit-skilaboðum. Fangað er viðbragðsdrifið og ad hoc, og rök tapast reglulega með starfsmannaveltu.
- **Stig 2 (Þróun):** Sum teymi halda skrár, í ýmsum sniðum og sniðmátum, hvenær sem einhver man eftir því. Vinnubrögðin eru ósamkvæm milli teyma, án sameiginlegs annáls, nafngiftar eða ferlis.
- **Stig 3 (Stöðlun):** Eitt sniðmát, geymsla í hugbúnaðarsafni og skilgreindur lífsferill og stjórnarhættir (viðmið um að stofna/sleppa, hlutverk, rýnitaktur) eru skjalfest og beitt samræmt um alla skipulagsheildina. Skrár eru rýndar og leystar af hólmi frekar en breytt hljóðlega.
- **Stig 4 (Stjórnun):** Ákvörðunarannállinn er mældur gegn grunnlínum: þekja (hlutfall arkitektúrlega mikilvægra ákvarðana sem bera skrá), ferskleiki (hlutfall skráa rýndra innan taktsins, auk fjölda ódagsettra eða úreltra fullyrðinga) og finnanleiki (hve oft viðeigandi skrá náði í raun til hönnuðarins sem breytti stýrða kóðanum). Ábyrgir umsjónarmenn bregðast við þessum mælikvörðum, leysa úreltar skrár af hólmi og loka þekjubilum á grundvelli gagna frekar en sagna.
- **Stig 5 (Samhæfing):** Leitanlegur ákvörðunarannáll milli teyma er samþættur daglegri vinnu: viðeigandi skrár birtast sjálfvirkt á breytingunum sem þær stýra, lykilákvarðanir eru tryggðar með hæfnisföllum í samfelldri samþættingu og annállinn nærir móttöku, nútímavæðingu og úttekt sem lifandi eign. Skipulagsheildin bætir sjálf vinnubrögðin stöðugt, leggur niður, leysir af hólmi og endurafmarkar skrár eftir því sem kerfið og skorður þess breytast, og jafnar á ný hvar hún fjárfestir í nákvæmni eftir því sem ákvörðunareignasafnið stækkar.

## Hugmyndir til umræðu

1. Hver var síðasta ákvörðun sem teymið þitt afturkallaði eða deildi aftur um því enginn mundi upprunalegu rökin?
2. Myndi það að endurnefna `adr/` möppuna `decisions/` breyta því hver leggur til og hvað er skráð?
3. Hverjar af mikilvægum ákvörðunum þínum gætu verið tryggðar með sjálfvirku hæfnisfalli í dag?
4. Óbreytanlegt-og-leyst-af-hólmi eða lifandi skjal: hvort hentar úttektarskyldum þínum og menningu, og hvers vegna?
5. Hvernig myndi nýr starfsmaður (eða arftakaverktaki) í dag uppgötva *hvers vegna* kerfið þitt er mótað eins og það er?
6. Hvað réttlætir að stofna ákvörðunarskrá hjá teyminu þínu, og hvað réttlætir að stofna hana *ekki*?

## Helstu atriði

- Ákvörðunarskrá fangar eina mikilvæga ákvörðun með **samhengi og afleiðingum**: *hvers vegna*, ekki bara *hvað*.
- Hafðu skrár **sértækar, tímamerktar og léttar**. Staðlaðu á eitt sniðmát (Nygard, MADR eða svipað).
- Geymdu þær **í útgáfustýringu við hlið kóðans**. Íhugaðu að nefna þær „ákvarðanir“ til að víkka út framlög.
- Skilgreindu **lífsferil og stjórnarhætti** (viðmið um að stofna/sleppa, hlutverk, rýnitaktur). Taktu frá þungt ferli fyrir einátta dyra-ákvarðanir.
- Gerðu ákvarðanir **finnanlegar** á því augnabliki sem breytt er og, þar sem hægt er, **prófanlegar** með hæfnisföllum.
- Ávöxtunin er forðaður enduruppgötvunar- og rangafturköllunarkostnaður. TCO-rökin eru sterkust þar sem starfsmannavelta, nútímavæðing og úttekt skipta mestu. Sjá kafla 1.5 (ákvarðanataka og stjórnarhættir) og kafla 3.1 (grunnatriði arkitektúrs).

## Heimildir og frekari lestur

- Michael Nygard, "Documenting Architecture Decisions" (2011): the foundational lightweight ADR.
- MADR: Markdown Any Decision Records project (adr.github.io/madr).
- Jeff Tyree and Art Akerman, "Architecture Decisions: Demystifying Architecture" (*IEEE Software*, 2005).
- Olaf Zimmermann, "Y-Statements" and "Architectural Decision Making" (ozimmer.ch).
- Joel Parker Henderson, *Architecture Decision Record (ADR)*: templates, examples, and teamwork guidance (github.com/joelparkerhenderson/architecture-decision-record).
- ThoughtWorks Technology Radar: "Lightweight Architecture Decision Records."
- Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage, *Building Evolutionary Architectures* (fitness functions).
- AWS Prescriptive Guidance, "ADR process"; Red Hat, "Why you should use ADRs."
- Wikipedia, "Architectural decision" and "Architecturally significant requirements."
