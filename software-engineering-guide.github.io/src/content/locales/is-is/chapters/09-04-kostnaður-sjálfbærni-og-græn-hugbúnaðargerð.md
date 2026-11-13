# 9.4 Kostnaður, sjálfbærni og græn hugbúnaðargerð

## Yfirlit og tilgangur

Hugbúnaður keyrir á efnislegum innviðum sem eyða peningum, rafmagni, vatni og efnum. Mestalla sögu tölvunar voru þessir kostnaðarliðir vandamál einhvers annars: fjárfestingarfjárhagsáætlanir földu vélbúnaðinn og orka var ósýnileg verkfræðingum. [Skýjatölvun](https://en.wikipedia.org/wiki/Cloud_computing) breytti því. Hún gerði neyslu fínkorna, eftir þörfum og beint eignanlega, sem breytti kostnaði, og í auknum mæli kolefni, í verkfræðiáhyggjuefni. Þessi kafli fjallar um tvo samtvinnaða aga: **FinOps**, þá venju að færa fjárhagslega ábyrgð að breytilegum skýjaútgjöldum, og **[græna hugbúnaðargerð](https://en.wikipedia.org/wiki/Green_computing)**, þá venju að smíða kerfi sem vinna sama verk með minni orku og lægri kolefnislosun. Þau skarast mikið, því skilvirkur hugbúnaður er yfirleitt bæði ódýrari og hreinni.

Fyrir stór teymi eru tölurnar gríðarlegar. Skýjareikningar stórs fyrirtækis geta náð tugum eða hundruðum milljóna á ári og fáein prósentustig af sóun eru raunverulegir peningar sem gætu fjármagnað stöðugildi eða vörur. [Kolefnisfótspor](https://en.wikipedia.org/wiki/Carbon_footprint) stórra stafrænna landareigna er líka umtalsvert og skipulagsheildir standa frammi fyrir vaxandi þrýstingi frá eftirlitsaðilum, fjárfestum, viðskiptavinum og eigin starfsfólki til að mæla og minnka það. Þegar hundruð teyma taka hver sjálfstæðar ákvarðanir um tilvikastærðir, gagnavarðveislu og arkitektúr safnast litlar óhagkvæmnir í mikinn kostnað og losun. Stjórnarhættir sem gera kostnað og kolefni sýnileg og ábyrg eru nauðsynlegir til að halda hvoru tveggja í skefjum.

Mikilvægi fyrir fyrirtæki og hið opinbera er beint. Opinberar skipulagsheildir eyða skattfé og eru í auknum mæli bundnar sjálfbærnimarkmiðum og núllkolefnisskuldbindingum, svo að sýna skilvirkan, lágkolefnisrekstur er bæði fjárhags- og stefnuskylda. Fyrirtæki standa frammi fyrir fjárfestaskoðun á umhverfisárangri og samkeppnisþrýstingi á framlegð. Í báðum umhverfum hafa kostnaður og sjálfbærni færst frá eftirþönkum yfir í stjórnarmálefni. Verkfræðiákvarðanir eru þar sem þessi áhyggjuefni rætast að lokum eða misfarast.

## Meginreglur

- **Gerðu neyslu sýnilega.** Þú getur ekki fínstillt það sem þú sérð ekki. Kostnaður og kolefni verða að vera eignuð teymum og þjónustum sem valda þeim.
- **Ábyrgð liggur hjá eigendum.** Verkfræðingarnir sem útvega auðlindir ættu að sjá og eiga kostnað og kolefnisáhrif þeirra.
- **Skilvirkni þjónar kostnaði og kolefni saman.** Að vinna sama verk með færri auðlindum sparar yfirleitt peninga og losun samtímis.
- **Stilltu stærð samfellt.** Eftirspurn breytist, svo útvegun verður að vera endurskoðuð, ekki sett einu sinni og gleymd.
- **Kolefni hefur tíma og stað.** Sami útreikningur losar meira eða minna eftir því hvenær og hvar rafmagnið er framleitt.
- **Jafnvægisstilltu þríhyrninginn.** Kostnaður, afköst og áreiðanleiki skiptast á. Fínstilltu af ásetningi, ekki blindandi.
- **Hannaðu fyrir skilvirkni snemma.** Arkitektúrval ráða langtímakostnaði og kolefni langtum meira en síðbúin stilling.

## Ráðleggingar

### Komdu á FinOps-sýnileika, fínstillingu og ábyrgð

FinOps fer í þremur endurteknum áföngum. **Upplýsa**: byggðu sýnileika gegnum merkingu, skiptingu og mælaborð, svo hver kostnaður sé eignaður teymi, þjónustu og viðskiptatilgangi og sameiginlegum kostnaði sé skipt sanngjarnt. **Fínstilla**: útrýmdu sóun (aðgerðalausum og munaðarlausum auðlindum), stilltu stærð of stórra þjónusta, taktu upp skuldbindingarbundna afslætti eins og frátekningar eða sparnaðaráætlanir fyrir stöðugt grunnálag og notaðu afgangs- eða afturkallanlega afkastagetu fyrir vinnu sem má trufla. **Reka**: felldu kostnað inn í venjulega verkfræðivenju með fjárhagsáætlunum, fráviksviðvörunum, spám og reglulegum rýnum. Umfram allt skaltu setja kostnaðargögn fyrir framan verkfræðingana sem búa hann til. Gerðu skilvirkni að sameiginlegu markmiði verkfræði, fjármála og vöru, ekki fjármálaáhyggjuefni eingöngu.

### Smíðaðu kolefnismeðvitaðan og orkunýtinn hugbúnað

Að minnka kolefni hefur þrjár vogarstengur. **Orkunýtni**: skrifaðu og stilltu hugbúnað til að vinna sama verk með færri örgjörvalotum, minna minni og minni gagnaflutningum, með betri reikniritum, skyndiminni og með því að forðast óþarfa útreikninga. **Vélbúnaðarnýtni**: nýttu auðlindir til fulls með hærri nýtingu, samþjöppun og nútímalegum skilvirkum vélbúnaði, því aðgerðalaus afkastageta eyðir enn orku og felur í sér framleiðslukolefni. **Kolefnismeðvitund**: færðu sveigjanlegt vinnuálag í tíma og rúmi að því hvenær og hvar raforkukerfið er hreinna, til dæmis með því að keyra lotuverk þegar endurnýjanleg framleiðsla er mikil eða í svæðum með lágkolefnisrafmagn. Mældu með viðurkenndum aðferðum eins og Software Carbon Intensity forskriftinni. Kjóstu veitendur og svæði með sterkar endurnýjanlegar skuldbindingar og gagnsæja skýrslugjöf.

### Hannaðu sjálfbæran arkitektúr og stilltu stærð

Arkitektúr ákveður gólf kostnaðar og kolefnis. Kjóstu teygjanlega hönnun sem skalast að raunverulegri eftirspurn og skalast niður í núll þegar aðgerðalaus, svo þú borgir aldrei fyrir að halda ónotaðri afkastagetu keyrandi. [Miðlaralaus](https://en.wikipedia.org/wiki/Serverless_computing) tækni og [sjálfskölun](https://en.wikipedia.org/wiki/Autoscaling) draga úr sóun fyrir hviðukennt vinnuálag og stýrðar þjónustur geta bætt nýtingu gegnum [fjölleigu](https://en.wikipedia.org/wiki/Multitenancy). Stilltu stærð reikniafls, geymslu og gagnagrunna gegn raunverulegri notkun frekar en óttafullri ofútvegun. Settu gagnalífsferilsstefnur svo köld gögn færist á ódýrari, orkulægri þrep eða séu eydd. Að minnka gagnamagn og netflutning skerðir bæði geymslukostnað og orkuna við að flytja bita. Líttu á skilvirkni sem hönnunarkröfu, rýnda við hlið afkasta og áreiðanleika.

### Jafnvægisstilltu kostnað, afköst og áreiðanleika af ásetningi

Kostnaður, afköst og áreiðanleiki mynda þríhyrning. Þrýstu einu hart og þú skattleggur yfirleitt hin: meiri tvítekning og lægri töf kosta meira og eyða oft meiri orku. Gerðu þessar málamiðlanir skýrar og tengdu þær við viðskiptagildi. Notaðu SLO ([þjónustustigsmarkmið](https://en.wikipedia.org/wiki/Service-level_objective)) til að skilgreina hve mikinn áreiðanleika og afköst þjónustan þarf í raun, útvegaðu síðan að því markmiði frekar en að gullhúða allt jafnt. Ókritískt og innra vinnuálag getur sætt sig við ódýrari, minna tvítekna, kolefnissveigjanlegri uppsetningar. Taktu frá úrvalsútvegun fyrir það sem raunverulega verðskuldar hana.

### Stýrðu án þess að kæfa

Veittu varnarrimla, ekki hlið. Miðlæg vettvangsteymi geta boðið skilvirk sjálfgefin gildi, merkingarframfylgd, fjárhagsáætlunarviðvaranir og sjálfsafgreiðslumælaborð, á meðan dagleg ákvarðanataka er skilin eftir hjá teymunum sem eiga vinnuálagið. Settu markmið fyrir alla skipulagsheildina um kostnaðarnýtni og kolefnisminnkun, skýrðu frá framvindu gagnsætt og fagnaðu sparnaði. Forðastu þunga samþykktaskrifræði sem hægir á afhendingu. Markmiðið er að gera skilvirka valið að auðvelda sjálfgefna valinu.

## Málamiðlanir: kostir og gallar

| Ákvörðun | Kostir | Gallar |
|---|---|---|
| Skuldbindingarafslættir | Mikill sparnaður á grunnálagi | Binding, áhætta ef eftirspurn breytist |
| Afgangs-/afturkallanleg afkastageta | Ódýrasta reikniafl, notar umframafl | Truflanir, aukin flækja |
| Ágeng stærðarstilling | Lægri kostnaður og kolefni | Hætta á vanframboð í toppum |
| Kolefnismeðvituð tímasetning | Minni losun | Seinkuð verk, verkfræðifyrirhöfn |
| Fjölsvæðatvítekning | Meiri áreiðanleiki | Meiri kostnaður, orka og kolefni |

Sameinandi málamiðlunin er að hámarksáreiðanleiki og -afköst fara sjaldan saman við lágmarkskostnað og -kolefni. Tvítekin, sívirk, lágtafarskerfi eru dýr og orkufrek, svo einsleit gullhúðun sóar bæði peningum og losun á vinnuálag sem þarf það ekki. Aginn er að stilla metnað að viðskiptagildi með SLO, eyða úrvalsauðlindum aðeins þar sem þær skipta máli. Skuldbindingarafslættir og afgangsafkastageta bjóða raunverulegan sparnað, en þau koma með bindingar- og truflunaráhættu sem þú verður að stýra. Kolefnismeðvituð tímasetning sparar losun, en hún hentar aðeins vinnuálagi sem þolir töf eða flutning.

## Spurningar til að ræða með teyminu

1. **Hvaða hlutfall skýjaútgjalda ykkar er í raun merkt og eignað teymi í dag?** Upplýsa-áfangi FinOps er grunnurinn: þú getur ekki fínstillt það sem þú sérð ekki og ómerkt, óskipt útgjöld þýða að enginn á sóunina. Komdu með raunverulega þekjutöluna í umræðuna, ekki væntingu, og lista yfir stærstu ómerktu liðina. Fyrir stóra skipulagsheild þar sem hundruð teyma útvega hvert sjálfstætt þýðir lágt eignunarhlutfall að sameiginlegar óhagkvæmnir safnast ósýnilega í milljónir. Í opinberu og fyrirtækjaumhverfi er eignun líka hvernig þú ver skattfé eða hluthafafé og hvernig þú skiptir sanngjörnum hlut sameiginlegra vettvangskostnaða. Svarið setur fyrstu hreyfingu þína: ef þekja er lág koma merkingarframfylgd og skipting á undan allri stærðarstillingu, því fínstilling án sýnileika er ágiskun.

2. **Hve mikið af grunnálagi ykkar er þakið skuldbindingarafslætti og hvað gerist við þær skuldbindingar ef eftirspurn breytist?** Frátekningar og sparnaðaráætlanir skila miklum sparnaði á stöðugu grunnálagi, en þær koma með bindingu, svo að kaupa of ágengt breytir afslætti í skuld þegar vara er lögð niður eða flutt. Komdu með tölurnar: skuldbundið þekjuhlutfall ykkar, þróun grunnálags og vinnuálagið sem er líklegast til að breyta lögun á næsta ári. Aginn er að skuldbinda aðeins gólfið sem þú ert viss um að haldist, þekja breytilega lagið með eftir-þörfum eða afgangsafkastagetu og endurskoða eftir því sem eftirspurn þróast. Fyrir stórt fyrirtæki er þetta fjárstýringarlíka ákvörðun með raunverulega fjárhagslega útsetningu, svo fjármál og verkfræði ættu að eiga hana saman frekar en önnur hliðin ein. Svarið ætti að aðgreina varanlegt grunnálag frá óvissri eftirspurn og stærðarsetja skuldbindingar að því fyrrnefnda.

3. **Hve mikið af flota ykkar situr aðgerðalaust og teljið þið framleiðslukolefni vélbúnaðarins eða aðeins orkuna sem hann brennir á meðan hann keyrir?** Aðgerðalaus afkastageta eyðir enn orku og ber framleiðslukolefnið sem þegar var eytt til að smíða vélbúnaðinn, svo að einblína aðeins á keyrsluorku á meðan þú ofútvegar missir þú af raunverulegum hluta fótsporsins. Komdu með nýtingargögn: meðaltal og hámark, bilið milli útvegaðs og notaðs og hvar skala-í-núll eða samþjöppun er möguleg. Hærri nýting þjónar kostnaði og kolefni í senn, sem er meginþráður þessa kafla, svo aðgerðalaus sóun er hreinasti sigurinn sem þú átt. Fyrir skipulagsheildir undir núllkolefnisumboði er heiðarlegur kolefnismælikvarði sem inniheldur innfellda losun það sem aðgreinir raunverulegar framfarir frá grænþvotti sem býður eftirlits- og orðsporsbakslag. Svarið ætti að beina lægst nýttu vinnuálögum að samþjöppun, sjálfskölun eða skala-í-núll og setja mælingaraðferð sem hunsar ekki hljóðlega framleiðslukolefni.

4. **Sjá verkfræðingar ykkar kostnað og kolefni eigin þjónusta og bregst nokkur við því sem hann sér?** Sýnileiki borgar sig aðeins þegar hann nær til fólksins sem útvegar auðlindir og breytir hegðun þess, svo mælaborð sem fjármál rýna mánaðarlega en verkfræðingar opna aldrei er skraut, ekki ábyrgð. Togið á móti er raunverulegt: vettvangsteymi vilja miðlæga stjórn og hreina skýrslugjöf, á meðan afhendingarteymi þola illa allt sem finnst eins og eftirlit eða enn eitt hlið á afhendingu. Komdu með sönnunargögn um hver horfir í raun á kostnaðar- og kolefnisgögn, hve oft og hvort stærðarstilling eða hreinsun hafi fylgt í kjölfarið síðasta ársfjórðung. Fyrir stóra skipulagsheild þar sem hundruð teyma útvega sjálfstætt er munurinn á merki sem verkfræðingar eiga og skýrslu sem þeir hunsa munurinn á samsettum sparnaði og samsettri sóun. Í fyrirtækja- og opinberu umhverfi skaltu setja einingahagfræði (kostnað og kolefni á beiðni, á viðskiptavin eða á mál) fyrir framan eigandateymið, því samantekin tala ver fjárhagsáætlun en tala á einingu breytir hönnunarákvörðun.

5. **Hvaða vinnuálög ykkar eru sannarlega sveigjanleg í tíma eða svæði og hvað þyrfti til að tímasetja þau þar sem raforkukerfið er hreinna?** Kolefnismeðvituð tímasetning færir sveigjanlega vinnu að því hvenær og hvar rafmagn er lágkolefnis, en hún hentar aðeins verkum sem þola töf eða flutning, svo fyrsta verkið er að aðgreina sannarlega frestanlega lotuvinnu frá öllu sem snýr að notendum eða er töfarbundið. Málamiðlunin er að flutningur verka yfir svæði eða utan álagstíma bætir við verkfræðifyrirhöfn, gagnaflutningskostnaði og stundum gagnabúsetuáhættu sem getur vegið þyngra en sparaða losunin. Komdu með frambjóðendalista lotu- og greiningarverka, töfarþol þeirra, gagnabúsetuskorður og kolefnisstyrk svæðanna sem þú mátt löglega keyra þau í. Fyrir fyrirtæki er þetta hófleg fínstilling ofan á stærðarstillingu, svo raðaðu henni á eftir kostnaðargrunnatriðunum frekar en á undan. Hjá hinu opinbera kunna gagnabúsetu- og fullveldisreglur að banna að færa borgaragögn yfir landamæri hvað sem hreinleika raforkukerfisins líður, svo svæðisvalið er lagaleg spurning áður en það er kolefnisspurning.

6. **Hvaða skilvirkni- og sjálfbærnimarkmið hafið þið sett og eru þau skrifuð svo að að ná þeim geti ekki hljóðlega brotið áreiðanleika?** Markmið einbeita fyrirhöfn, en gróft kostnaðar- eða kolefnismarkmið býður rangri hegðun: teymi útvega of lítið, strípa tvítekningu eða fresta vinnu á vegu sem skipta litlum sparnaði fyrir stórt atvik. Spennan er milli metnaðarfullrar tölu ofan frá sem forysta getur skýrt frá og markmiðs neðan frá byggðs á raunverulegum SLO hverrar þjónustu, svo sætta verður þetta tvennt frekar en að leggja á. Komdu með núverandi markmið þín, grunnlínuna sem þau eru mæld gegn og áreiðanleikavarnarrimlana sem stöðva fínstillingu frá því að skera inn í það sem þjónusta þarf sannarlega. Fyrir stóra skipulagsheild verða samanlögð markmið að brotna sanngjarnt niður á teymi þar sem vinnuálög eru ólík, svo borgarasnúin greiðsluþjónusta og innra skýrsluverk ættu ekki að bera sömu skilvirknivæntingu. Í fyrirtækja- og opinberu samhengi þar sem sjálfbærnitölur birtast í opinberum upplýsingagjöfum skaltu tengja hverja skýrða tölu við úttektarhæfa mælingaraðferð, því markmið sem þú getur ekki varið undir skoðun er skuld, ekki afrek.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Kostnaður er rekstrarþol, svo einn eftirmiðdagur af merkingu og ein fjárhagsáætlunarviðvörun getur keypt þér annan mánuð áður en þú sækir fé aftur. Slepptu FinOps-ferli og kolefnisbókhaldi alveg. Fylgstu bara með reikningnum, drepðu aðgerðalausar auðlindir og veldu stýrðan vettvang sem skalast í núll svo þú borgir fyrir álag frekar en afkastagetu sem situr tilbúin. Knappasta auðlind þín er athygli verkfræðinga, svo sjálfvirknivæddu augljósu sóunina og haltu áfram.

**Lítið fyrirtæki.** Þú hefur engan FinOps-sérfræðing og þröngt fjárhagsáætlun, svo hallaðu þér að kostnaðarverkfærunum sem skýjaveitan gefur þér nú þegar frekar en að kaupa sérstakan vettvang. Settu mánaðarlega fjárhagsáætlunarviðvörun, kveiktu á stærðarstillingartillögum veitunnar og kjóstu stýrðar og miðlaralausar þjónustur sem fella rekstrarnýtni inn í verðið. Líttu á sjálfbærni sem að velja lágkolefnissvæði og skilvirkt sjálfgefið gildi, ekki skýrslugerðaráætlun sem þú þarft að manna.

**Stórfyrirtæki.** Vandinn er stjórnarhættir yfir mörg teymi: samræmd merking, sanngjörn skipting á sameiginlegum vettvangskostnaði, skuldbindingarafsláttarstefna í sameiginlegri eigu fjármála og verkfræði og kostnaður og kolefni birt sem merki sem hvert teymi sér. Staðlaðu skilvirk sjálfgefin gildi og mælingaraðferð svo hundruð sjálfstæðra útvegunarákvarðana safnist ekki í sóun og stýrðu skýjaútgjöldum og losun sem eignasafni með markmiðum, fráviksviðvörunum og gagnsærri skýrslugjöf frekar en dreifingu staðbundinna fínstillinga.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta hvert val. Þú eyðir skattfé og ert oft bundinn núllkolefnisumboði, svo þú verður að sýna bæði fjárhagslega varfærni og úttektuð framfarir í losun, sem þýðir heiðarlegan kolefnismælikvarða sem inniheldur innfelldan vélbúnað frekar en grænþvott. Gagnabúsetu- og fullveldisreglur kunna að takmarka hvaða svæði þú getur notað hvað sem hreinleika raforkukerfisins líður og skilvirkni- og losunarmælikvarða gæti þurft að birta fyrir opinbera skoðun, svo veldu mælingaraðferðir sem þú getur varið undir úttekt.

## Dæmi

**Sprotafyrirtæki.** Sprotafyrirtæki á fræstigi sér skýjareikninginn tvöfaldast á tveimur mánuðum og getur ekki sagt hvers vegna. Stofnandi eyðir eftirmiðdegi í að merkja hverja auðlind eftir eiginleika og kveikir á einfaldri fjárhagsáætlunarviðvörun. Merkin afhjúpa gleymdan prófunarklasa og of stóran gagnagrunn sem keyrir allan sólarhringinn fyrir næturverk. Að loka klasanum og færa verkið í tímasetta keyrslu utan álagstíma á minna tilviki skerðir reikninginn um þriðjung, sem kaupir teyminu annan mánuð af rekstrarþoli.

**Stórfyrirtæki.** Fjölþjóðlegur smásali með stóra, útbreidda skýjalandareign setur upp FinOps-venju. Hann framfylgir merkingu, eignar hvern kostnað vöruteymi og birtir útgjöld á mælaborðum sem verkfræðingar sjá daglega. Innan árs fjarlægir hann aðgerðalausar auðlindir, stillir stærð of stórra þjónusta og kaupir sparnaðaráætlanir fyrir stöðugt grunnálag, sem skerðir skýjaútgjöld um nálægt fjórðung. Hann tímasetur síðan næturgreiningarlotuverk í lágkolefnissvæðum og utan álagstíma, sem lækkar bæði kostnað og losun, og skýrir frá kolefnissparnaðinum í árlegri sjálfbærniupplýsingagjöf sinni.

**Hið opinbera.** Opinber stofnun sem rekur borgaraþjónustu undir landsbundnu núllkolefnisumboði verður að sýna bæði fjárhagslega varfærni með skattfé og framfarir í átt að losunarmarkmiðum. Hún stillir stærð og samþjappar vinnuálagi, setur gagnavarðveislustefnur sem færa sjaldan notaðar skrár á köld, orkulág geymsluþrep og velur skýjasvæði knúin háum hlutföllum endurnýjanlegs rafmagns. Hún mælir kolefnisstyrk helstu þjónusta sinna og birtir skilvirkni- og losunarmælikvarða fyrir opinbera ábyrgð. Skilvirk sjálfgefin gildi og sjálfsafgreiðslumælaborð leyfa tugum afhendingarteyma að taka sjálfbærar ákvarðanir án miðlægra flöskuhálsa.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtunin hér er óvenju bein. FinOps-fínstilling skerðir yfirleitt skýjaútgjöld um fimmtung til þriðjung með agaðri fyrirhöfn, sparnaður sem rennur beint í afkomuna eða til að fjármagna nýja vinnu. Kolefnisminnkun ber líka sífellt fjárhagslegt gildi, gegnum forðað kolefnisverð, hæfi til samninga með sjálfbærnikröfum og minni eftirlits- og orðsporsáhættu. Því skilvirkni lækkar kostnað og kolefni í senn borgar ein fjárfesting í sýnileika og stærðarstillingu sig á báðum víddum.

Heildareignarkostnaður verður að telja upptökukostnað: verkfæri fyrir kostnaðar- og kolefnissýnileika, FinOps- eða vettvangsstarfsfólkið til að reka venjuna og verkfræðitímann til að stilla stærð og endurhanna. Þetta er hóflegt gagnvart sparnaðinum og minnkar eftir því sem skilvirk sjálfgefin gildi festast í sessi. Kostnaður þess að taka ekki upp safnast hljóðlega upp: stjórnlausir skýjareikningar sem vaxa hraðar en reksturinn, sóun sem kemur aldrei upp á yfirborðið því enginn á hana og vaxandi eftirlits-, fjárfesta- og orðsporsútsetning varðandi sjálfbærni. Til að færa rök við forystu skaltu setja fram núverandi útgjöld og vaxtarferil þeirra, áætlaða sóun og viðmiðunarsparnað af FinOps-upptöku. Paraðu það síðan við losunarminnkunina og reglufylgnigildið. Rammaðu kostnað og sjálfbærni sem sama skilvirknifrumkvæði séð gegnum tvær linsur, svo reksturinn þurfi ekki að velja milli þess að spara peninga og að skera kolefni.

## Andmynstur og gildrur

- **Engin kostnaðareignun.** Ómerkt, óskipt útgjöld þýða að enginn á sóun og enginn getur fínstillt hana.
- **Setja-og-gleyma útvegun.** Að stilla stærð auðlinda einu sinni og endurskoða aldrei tryggir rek í offramboð.
- **FinOps aðeins hjá fjármálum.** Að líta á kostnað sem bakvinnsluáhyggjuefni frekar en verkfræðimerki bregst, því verkfræðingar taka ákvarðanirnar sem knýja útgjöld.
- **[Grænþvottur](https://en.wikipedia.org/wiki/Greenwashing).** Að fullyrða sjálfbærni án mælinga býður eftirlits- og orðsporsbakslagi.
- **Skilvirkni á kostnað áreiðanleika.** Að skera svo ágengt að þjónustur bili undir álagi skiptir litlum sparnaði fyrir stórt atvik.
- **Að hunsa innfellt kolefni.** Að einblína aðeins á keyrsluorku á meðan aðgerðalaus vélbúnaður er ofútvegaður missir af framleiðslufótsporinu.
- **Skrifræðishlið.** Þungir samþykktarferlar fyrir útgjöld hægja á afhendingu og ýta teymum til að sniðganga stjórnarhætti.

## Þroskalíkan

**Stig 1, Upphaf.** Skýjakostnaður er óvænt á mánaðarreikningnum. Engin merking, skipting eða kolefnismeðvitund er til og útvegun er rausnarleg og sjaldan endurskoðuð. Sóun er ósýnileg því enginn á hana og öll hreinsun sem gerist er viðbragð við reikningsáfalli frekar en venja.

**Stig 2, Þróun.** Grunnkostnaðarsýnileiki og merking eru til og einhver stærðarstilling og hreinsun aðgerðalausra auðlinda gerast, en þekja og nákvæmni eru mjög ólík milli teyma. Fáeinir hópar fylgjast með útgjöldum sínum og prófa lágkolefnissvæði. Aðrir gera hvorugt. Sjálfbærni er viðurkennd en ekki mæld og góðar venjur velta á frumkvæði einstaklinga frekar en sameiginlegri væntingu.

**Stig 3, Stöðlun.** FinOps-venja er skjalfest og beitt um skipulagsheildina: merkingu er framfylgt, sameiginlegum kostnaði er skipt með samþykktri aðferð og fjárhagsáætlanir, spár og fráviksviðvaranir eru staðlaðar. Skuldbindingarafslættir og stærðarstilling fylgja skilgreindri handbók og kolefni er mælt fyrir helstu þjónustur með viðurkenndri aðferð eins og Software Carbon Intensity forskriftinni, með svæða- og tímasetningarvali íhuguðu samræmt frekar en tilvik fyrir tilvik.

**Stig 4, Stjórnun.** Kostnaður og kolefni eru mæld og stýrð gegn grunnlínum. Teymi rekja einingahagfræði (kostnað og kolefni á beiðni, á viðskiptavin eða á mál), nýtingu þar með talið aðgerðalaust og áætlað innfellt kolefni, skuldbindingarþekju gegn grunnálagi og spánákvæmni, allt skýrt gegn skipulagsmarkmiðum. Frávik ræsa rannsókn, skilvirkni og SLO-fylgni eru rýnd saman svo fínstilling rýri aldrei hljóðlega áreiðanleika og ákvarðanir um fara eða ekki í útvegun eru teknar á þessum gögnum frekar en eðlisávísun.

**Stig 5, Samhæfing.** Kostnaður og kolefni eru samfelld, eigin verkfræðimerki ofin inn í daglega venju. Skilvirk sjálfgefin gildi, sjálfvirk stærðarstilling og kolefnismeðvituð tímasetning eru normið og skipulagsheildin endurjafnar landareign sína stöðugt eftir því sem eftirspurn, verð og kolefnisstyrkur raforkukerfisins breytast. Kostnaður, afköst og áreiðanleiki eru jafnvægisstillt af ásetningi gegnum SLO, sjálfbærnimælikvarðar næra opinbera og fjárfestaskýrslugerð með úttektarhæfum aðferðum og venjan aðlagast eftir því sem reksturinn, markaðurinn og regluverk þróast.

## Hugmyndir til umræðu

- Hver ætti að eiga skýjakostnað í skipulagsheild ykkar: fjármál, miðlægt FinOps-teymi eða verkfræðiteymin sem útvega auðlindir?
- Hvernig eignið þið sameiginlegan vettvangskostnað sanngjarnt yfir mörg notendateymi?
- Hvar er rétta jafnvægið milli kostnaðarsparnaðar og áreiðanleika eða afkasta sem þið gætuð fórnað til að ná honum?
- Hvernig myndu þið mæla kolefnisfótspor þjónusta ykkar og hve mikið treystið þið tiltækum gögnum?
- Hvaða vinnuálög ykkar eru nógu sveigjanleg fyrir kolefnismeðvitaða tímasetningu í tíma eða svæði?
- Hvernig setjið þið skilvirkni- og sjálfbærnimarkmið sem hvetja teymi án þess að hvetja til áhættusamrar vanframboðar?

## Helstu atriði

- Skýið gerði kostnað og kolefni að verkfræðiáhyggjuefnum. Sýnileiki og eignarhald eru grunnurinn að því að stýra hvoru tveggja.
- FinOps virkar í þremur áföngum: upplýsa (sýnileiki), fínstilla (stærðarstilla og afsláttur) og reka (fella inn í venju).
- Skilvirkur hugbúnaður sparar yfirleitt peninga og kolefni saman, svo líttu á þau sem eitt frumkvæði með tveimur linsum.
- Minnkaðu kolefni gegnum orkunýtni, hærri vélbúnaðarnýtingu og kolefnismeðvitaða tímasetningu í tíma og stað.
- Arkitektúr og stærðarstilling ráða langtímakostnaði og kolefni. Hannaðu fyrir teygjanleika og skala-í-núll.
- Jafnvægisstilltu kostnað, afköst og áreiðanleika af ásetningi með SLO og stýrðu með varnarrimlum frekar en hliðum.

## Heimildir og frekari lestur

- J.R. Storment, Mike Fuller, *Cloud FinOps: Collaborative, Real-Time Cloud Financial Management*
- FinOps Foundation, *FinOps Framework* documentation
- Green Software Foundation, *Principles of Green Software Engineering* and *Software Carbon Intensity (SCI) Specification*
- Anne Currie, Sarah Hsu, Sara Bergman, *Building Green Software*
- Adrian Cockcroft, writings on cloud efficiency and sustainability
- The Shift Project, *Lean ICT: Towards Digital Sobriety*
