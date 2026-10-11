# 9.2 Sýnileiki og fjarmælingar

## Yfirlit og tilgangur

[Fjarmælingar](https://en.wikipedia.org/wiki/Telemetry) eru gögnin sem kerfi gefur frá sér um eigin hegðun: mælikvarðarnir, skrárnar, rakningarnar og atburðirnir sem safnað er úr keyrandi hugbúnaði. Vöktun svarar spurningum sem þú vissir þegar að þú ættir að spyrja úr þeim fjarmælingum. Er diskurinn fullur? Er villuhlutfallið yfir þröskuldi? Er þjónustan uppi? [Sýnileiki](https://en.wikipedia.org/wiki/Observability_(software)) er víðtækari. Hann er geta til að spyrja nýrra spurninga um innra ástand kerfis utan frá, án þess að afhenda nýjan kóða, svo þú getir skilið hegðun sem þú sást aldrei fyrir. Þegar kerfi vaxa í dreifðan, [örþjónustu](https://en.wikipedia.org/wiki/Microservices)- og [atburðadrifinn arkitektúr](https://en.wikipedia.org/wiki/Event-driven_architecture) eru bilanirnar sem meiða mest þær sem enginn sá fyrir og sýnileiki er það sem leyfir þér að aflúsa þær. Vöktun segir þér að eitthvað er rangt. Sýnileiki hjálpar þér að finna út hvers vegna.

Fyrir stór teymi er þessi greinarmunur afgerandi. Þú gast skilið risaforrit með því að lesa skrár á einni vél. Nútímavettvangur spannar hundruð þjónusta, mörg teymi, mörg svæði og ósjálfstæði þriðja aðila, þar sem ein notendabeiðni getur snert tugi íhluta. Enginn einn maður heldur öllu kerfinu í höfðinu. Sameiginlegar, vandaðar fjarmælingar verða bandvefurinn sem leyfir hverjum verkfræðingi að fylgja beiðni yfir mörk, raða einkennum upp yfir þjónustur og rökræða um kerfi sem enginn á til fulls. Án þeirra dragast atvik á langinn, sök flýgur milli teyma og rótarorsakir haldast faldar.

Fyrirtækja- og opinber kerfi hækka húfið með reglufylgni, úttektarhæfni og opinberri ábyrgð. Eftirlitsaðilar kunna að krefjast sönnunargagna um hver fékk aðgang að hverju og hvenær. Öryggisteymi þurfa fjarmælingar til að greina innbrot. Borgarasnúnar þjónustur verða að sýna að þær mæti útgefnum afkastaskuldbindingum sínum. Góður sýnileiki þjónar öllu þessu í senn: hann er verkfræðitól, öryggisstýring og ábyrgðarbúnaður í einu. Að staðla á opin mælitæki forðast bindingu við séreignarumboðsmenn eins seljanda, sem skiptir gríðarlegu máli þegar kerfi verða að endast áratugi og lifa af innkaupahringi.

*Sjá einnig:* kafla 9.1 (áreiðanleikaverkfræði og SLO), kafla 9.3 (atvikastjórnun) og kafla 3.3 (dreifð kerfi).

## Meginreglur

- **Mældu fyrir óþekktar spurningar.** Hannaðu fjarmælingar svo þú getir rannsakað nýjar bilanir, umfram þær sem þú spáðir.
- **Þrjár stoðir, ein saga.** Mælikvarðar, skrár og rakningar eru viðbótarsýnir. Gildi þeirra margfaldast þegar þær eru tengdar, ekki í síló.
- **Byggðu allt upp.** Uppbyggðar, vélþáttanlegar fjarmælingar slá frjálsan texta sem aðeins menn geta lesið.
- **Tengdu með sameiginlegum auðkennum.** Rakningar- og beiðniauðkenni dreifð alls staðar leyfa þér að sauma einn atburð saman yfir þjónustur.
- **Varaðu við einkennum, ekki orsökum.** Kallaðu menn út fyrir notendasýnileg vandamál. Láttu mælaborð og rannsókn draga fram undirliggjandi orsök.
- **Sérhvert útkall verður að vera framkvæmanlegt.** Viðvörun sem krefst engra mannlegra aðgerða er hávaði sem rýrir traust og veldur þreytu.
- **Há fjölbreytni gilda er eiginleiki.** Getan til að sneiða eftir notanda, beiðni, svæði og útgáfu er það sem gerir aflúsun í framleiðslu mögulega.
- **Eigðu mælitæki þín.** Staðlaðu á opnar, söluaðilahlutlausar fjarmælingar svo þú stýrir gögnum þínum og getir skipt um bakenda.

## Ráðleggingar

### Byggðu á stoðunum þremur og lengra

**Mælikvarðar** eru tölulegar tímaraðir, ódýrir í geymslu og tilvaldir fyrir mælaborð, þróun og viðvörunarþröskulda. **Skrár** eru stakar, tímastimplaðar færslur atburða, ríkar af smáatriðum og nauðsynlegar fyrir réttarrannsókn. **[Rakningar](https://en.wikipedia.org/wiki/Tracing_(software))** fylgja einni beiðni þegar hún færist gegnum þjónustur og sýna töf og ósjálfstæði yfir dreifða kallagrafið. Umfram þetta skaltu íhuga **atburði** (marktækar ástandsbreytingar eins og útsetningar), **greiningar** (hvar kóði eyðir örgjörva og minni) og **[rauntímanotendavöktun](https://en.wikipedia.org/wiki/Real_user_monitoring)** á raunverulegri upplifun biðlara. Engin ein stoð nægir ein. Markmiðið er að færa sig mjúklega milli þeirra í rannsókn.

### Staðlaðu á OpenTelemetry og uppbyggða skráningu

Taktu upp [OpenTelemetry](https://en.wikipedia.org/wiki/OpenTelemetry) sem söluaðilahlutlausan staðal til að búa til og safna mælikvörðum, skrám og rakningum. Það aðgreinir mælingar frá greiningarbakendanum, svo þú getir skipt um söluaðila án þess að endurmæla hundruð þjónusta. Sá eiginleiki er mikilvægur fyrir langlíf fyrirtækja- og opinber kerfi. Gefðu skrár út sem uppbyggðar færslur (til dæmis JSON) með samræmdum reitaheitum fyrir tímastimpil, alvarleika, þjónustu og auðkenni. Dreifðu rakningar- eða fylgniauðkenni frá jaðrinum gegnum hvert niðurstreymiskall og hafðu það í hverri skráarlínu og mælikvarðaáminningu, svo stoðirnar þrjár tengist sjálfvirkt.

### Hannaðu viðvaranir fyrir framkvæmanleika og lítinn hávaða

Viðvörunarheimspeki þín ákveður hvort bakvakt er sjálfbær. Varaðu aðallega við einkennum sem notendur finna, sett fram sem SLO ([þjónustustigsmarkmið](https://en.wikipedia.org/wiki/Service-level_objective)) brunahraða. Kallaðu út þegar þú brennir gegnum villufjárhagsáætlun þína (leyfða skerðingu frá því markmiði) nógu hratt til að brjóta hana, með fjölglugga brunahraðaviðvörunum til að jafnvægisstilla hraða greiningu gegn fölskum viðvörunum. Taktu frá útköll fyrir vandamál sem þurfa tafarlausa mannlega aðgerð og beindu öllu öðru í miða eða mælaborð. Fjarlægðu viðvaranir sem kvikna án þess að krefjast aðgerðar, miskunnarlaust, því viðvörunarþreyta er leiðandi orsök missta raunverulegra atvika og bakvaktarkulnunar. Sérhver viðvörun ætti að tengjast keyrsluhandbók.

### Líkanaðu heilsu með mælaborðum og SLO-vöktun

Byggðu mælaborð í kringum skýrt heilsulíkan, ekki vegg af hverjum mælikvarða sem þú átt. Góður upphafsrammi er „fjögur gullnu merkin“: töf, umferð, villur og mettun. Búðu til þjónustustigsmælaborð sem sýna SLO-stöðu og eftirstandandi villufjárhagsáætlun í fljótu bragði, auk hærra stigs mælaborða sem líkana heildarkerfis- og notendaferðaheilsu. Snyrtu þau vandlega, því mælaborð sem sýna allt miðla engu. Haltu þeim nálægt viðvörunum og keyrsluhandbókum, svo viðbragðsaðilar færist fljótt frá merki til samhengis til aðgerðar.

### Gerðu aflúsun í framleiðslu mögulega með fjölbreytni gilda

Erfiðustu framleiðsluvandamálin lenda á þröngri sneið: einum viðskiptavini, einu svæði, einni API-útgáfu, einni tækjategund. Til að rannsaka þau þarftu fjarmælingar með **háa fjölbreytni gilda**, getuna til að flokka og sía eftir reitum með mörgum ólíkum gildum eins og notandaauðkenni eða beiðniauðkenni. Breiðir, ríkulega eigindaðir atburðir sem bera margar víddir á færslu leyfa þér að spyrja handahófskenndra spurninga eftir á. Haltu nægri fjölbreytni og úrtaksnákvæmni til að einangra frávik og kjóstu rakningar tengdar áminningum, svo toppur á mælikvarða leiði þig beint að dæmigerðum hægum beiðnum.

### Stýrðu kostnaði, varðveislu og úrtaki

Fjarmælingamagn vex með kerfinu og getur orðið stór útgjaldaliður. Settu varðveislustefnur eftir gagnaflokki: geymdu hánákvæm gögn stutt og samantektir lengur. Beittu skynsamlegu úrtaki á rakningar, hneigðu að því að halda villum og hægum beiðnum, svo þú haldir áhugaverða halanum án þess að borga fyrir hvern venjulegan árangur. Rýndu fjarmælingaútgjöld reglulega, því óstýrður sýnileikakostnaður getur keppt við innviðina sem hann fylgist með.

## Málamiðlanir: kostir og gallar

| Ákvörðun | Kostir | Gallar |
|---|---|---|
| Atburðir með háa fjölbreytni gilda | Öflug aflúsun, spyrðu hvað sem er | Hærri geymslu- og fyrirspurnakostnaður |
| Ágengt úrtak | Lægri kostnaður, minni hávaði | Getur misst sjaldgæfa atburði |
| Einkennabundnar viðvaranir | Færri, framkvæmanleg útköll | Þarf góð SLO til að virka vel |
| OpenTelemetry staðall | Söluaðilahlutlaust, flytjanlegt | Flutningsfyrirhöfn, þroskandi verkfæri |
| Löng skráavarðveisla | Betri réttarrannsókn og úttekt | Geymslukostnaður, persónuverndarútsetning |

Sýnileikaákvarðanir snúast um spennu milli nákvæmni og kostnaðar. Að fanga allt í fullri upplausn gefur fullkomið eftirá-sjónarhorn, en í stærð er það óheyrilega dýrt. Skerðu ágengt og þú sparar peninga, en þú gætir hent einu færslunni sem hefði útskýrt rof. Úrtak og varðveisluþrep eru hvernig þroskuð teymi ganga þessa línu, halda villum og frávikum á meðan þau þynna venjuleg gögn. Viðvörunarmálamiðlunin er milli næmis og hávaða: of margar viðvaranir valda þreytu og missum atvikum, of fáar láta vandamál grassera. Einkennabundnar, SLO-drifnar viðvaranir leysa mikið af þessu, en aðeins ef þú hefur marktæk SLO á sínum stað.

## Spurningar til að ræða með teyminu

1. **Hver er áætlun ykkar um að færa arfleifðarþjónustur yfir á OpenTelemetry og hvernig forðist þið að borga fyrir tvo mælingastafla á flutningstímanum?** Söluaðilahlutlaus mæling er eiginleikinn sem leyfir þér að skipta um bakenda án þess að endurmæla hundruð þjónusta og hún skiptir mestu fyrir langlífu fyrirtækja- og opinberu kerfin sem lifa lengur en nokkur einn söluaðilasamningur. Flutningurinn er þar sem góður ásetningur stöðvast: hálfmæld landareign skilur eftir göt nákvæmlega þar sem beiðni fer frá nýrri þjónustu til gamallar, sem brýtur rakninguna frá enda til enda. Komdu með skrá í umræðuna: hvaða þjónustur gefa út séreignarumboðsgögn, hverjar OpenTelemetry og hvar rakningarsamhengi týnist við mörkin. Ákveddu röðun sem fylgir raunverulegum beiðnaslóðum frekar en skipuritum og fjárhagsáætlaðu gluggann þar sem þú rekur báða safnara. Svarið ræður því hvort þú átt í raun fjarmælingar þínar eða situr fastur við umboðsmenn eins seljanda.

2. **Hvenær úttektuðuð þið síðast hverja viðvörun fyrir framkvæmanleika og hve mörg útköll síðasta mánaðar kröfðust engrar mannlegrar aðgerðar?** Viðvörunarþreyta er leiðandi orsök missta raunverulegra atvika og bakvaktarkulnunar, svo útkall sem þarf enga aðgerð er ekki skaðlaus hávaði, það rýrir virkt viðbragðið sem þú treystir á. Komdu með kvittanir: dragðu útköll síðasta mánaðar, merktu hvert sem brugðist við eða hunsað og teldu hve mörg tengdust keyrsluhandbók. Fyrir stórt teymi sem spannar margar þjónustur gerir hávaðasamar viðvaranir eins teymis sameiginlega bakvakt ónæma. Settu staðal um að sérhvert útkall tengist keyrsluhandbók og SLO brunahraða, eyddu síðan restinni miskunnarlaust. Niðurstaða þessarar úttektar ætti beint að skera útkallamagn ykkar og segja ykkur hvaða þjónustur hafa engin marktæk SLO á bak við viðvaranir sínar.

3. **Hver er rakningarúrtaksstefna ykkar og hve viss eruð þið um að hún haldi villunum og hæga halanum?** Fjarmælingamagn vex með kerfinu og óstýrður sýnileikakostnaður getur keppt við innviðina sem hann fylgist með, svo þið munuð taka úrtak og spurningin er hvort þið takið úrtak skynsamlega. Að strípa fjölbreytni eða taka úrtak blindandi fjarlægir einmitt færslurnar sem þarf til að aflúsa þröngu vandamálin sem lenda á einum viðskiptavini, einu svæði eða einni API-útgáfu. Komdu með núverandi varðveisluþrep og úrtaksreglur: hneigist þið að því að halda villum og hægum beiðnum, nota rakningar tengdar áminningum svo mælikvarðatoppur leiði að dæmigerðri hægri beiðni? Fyrir úttektuð og persónuverndarbundin kerfi skaltu sætta varðveislu við gagnalágmörkunarreglur svo þú hamstrir ekki persónugögn til að aflúsa. Svarið setur hvar þú eyðir fjarmælingafjárhagsáætlun og hvort næsta erfiða rof ykkar er útskýranlegt eða ráðgáta.

4. **Hver af SLO ykkar eru raunverulegar notendaferðaskuldbindingar og hver eru staðgenglamælikvarðar sem enginn utan eigandateymisins trúir?** Einkennabundnar viðvaranir virka aðeins þegar einkennin varpast á hluti sem notendur finna í raun, svo viðvörun tengd örgjörvaþröskuldi eða tilbúnu aðgengismarkmiði kallar fólk út fyrir vandamál sem skipta kannski ekki máli á meðan hún þegir um þau sem gera það. Fyrir stóra skipulagsheild eru SLO líka samningurinn sem leyfir sjálfstæðum teymum að deila bakvaktarlotu án þess að endurdeila alvarleika í hverju atviki. Komdu með núverandi SLO-skrá, notendaferðina sem hvert markmið á að vernda og brot síðasta ársfjórðungs með því hvort viðskiptavinir kvörtuðu í raun. Í fyrirtækja- og opinberu umhverfi skaltu tengja sýnilegustu SLO við útgefnar afkastaskuldbindingar sem þjónustan er látin standa við, svo sama brunahraðamerkið sem kallar verkfræðing út sé líka sönnunargagnið sem þú sýnir eftirlitsaðila eða úttektaraðila. Umræðan ætti að leggja niður staðgenglamælikvarðana og skilja eftir stuttan lista markmiða sem ekki-verkfræðingur þekkir sem loforð til notenda.

5. **Hver á gagnastjórnarhætti fjarmælinga og getið þið sannað að persónugögn séu strikuð út áður en þau lenda í sýnileikabakendanum?** Atburðir með háa fjölbreytni gilda og löng skráavarðveisla eru nákvæmlega eiginleikarnir sem gera aflúsun mögulega og nákvæmlega þeir sem breyta sýnileikageymslu í óstýrt afrit af persónugögnum notenda þinna. Togið á móti er raunverulegt: verkfræðingar vilja ríkari eigindi og lengri varðveislu, á meðan persónuvernd og lögfræði vilja gagnalágmörkun og stutta líftíma. Komdu með gagnaflæðikort sem sýnir hvaða reitir bera persónuleg eða viðkvæm gögn, hvar útstrikun eða táknun gerist í leiðslunni og hverjar varðveisluþrep þín eru á gagnaflokk. Fyrir regluverkuð og opinber kerfi skaltu nefna ábyrga eigandann, varpa varðveislu á lagagrundvöllinn og gagnalágmörkunarreglurnar sem þú starfar undir og vera tilbúinn að sýna úttektaraðila að aðgangur að fjarmælingunum sjálfum sé skráður og stýrður. Svarið ákveður hvort sýnileikavettvangur ykkar er eign eða varanlegt brot sem bíður þess að uppgötvast.

6. **Þegar atvik spannar þjónustur nokkurra teyma, leyfa fjarmælingar ykkar einum viðbragðsaðila að fylgja beiðninni frá enda til enda, eða brotnar slóðin við hver eignarhaldsmörk?** Allt loforðið um tengdar, auðkennisdreifðar fjarmælingar er að einn verkfræðingur geti rökrætt um kerfi sem enginn á til fulls og það loforð hrynur nákvæmlega við mörkin þar sem rakningarsamhengi er fellt niður eða þar sem tvö teymi nota ósamrýmanleg auðkenni og verkfæri. Vegðu togið í átt að sjálfræði teyma í vali sýnileikaverkfæra gegn sameiginlegum kostnaði sundraðrar landareignar þar sem hver afhending er blindgata í rofi. Komdu með nýlega þverteymisatvikatímalínu og merktu hvar viðbragðsaðilinn missti þráðinn, auk skrár yfir hvaða þjónustur dreifa sameiginlegu fylgniauðkenni og hverjar ekki. Fyrir stórt fyrirtæki eða opinberan vettvang settan saman úr mörgum söluaðilum og langlífum kerfum skaltu ákveða hve mikið þú skyldar miðlægt, sameiginlegan rakningarsamhengisstaðal og sameiginlegt auðkennakerfi, á móti því sem þú skilur eftir teymum, því íhlutirnir sem þú endurinnkaupir áratugum saman verða enn að vera samvirkir á sömu beiðni. Svarið segir þér hvort næsta fjölteymisatvik ykkar er samræmd rannsókn eða hringur af fingrabendingum.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með örfáar þjónustur og engar lausar hendur skaltu mæla með OpenTelemetry frá fyrsta degi og afhenda uppbyggðar JSON-skrár sem bera eitt beiðniauðkenni frá enda til enda. Sú litla fjárfesting breytir „forritið er hægt“ í rakningu sem þú getur lesið og heldur þér frjálsum að færa þig úr ókeypis þrepi yfir í greiddan bakenda síðar án þess að endurmæla. Slepptu íburðarmiklum mælaborðum og SLO-vélbúnaði þar til þú átt notendur sem upplifun þú getur í raun mælt.

**Lítið fyrirtæki.** Þú hefur engan sýnileikasérfræðing og þröngt fjárhagsáætlun, svo hallaðu þér að stýrðum bakenda þar sem mælingar, geymsla og mælaborð koma saman frekar en að setja saman eigin stafla. Kaup-gegn-smíða valið hallar að kaupum nánast alltaf hér. Knöpp athygli þín er betur varið í tvær eða þrjár gullnu-merkja viðvaranirnar sem segja þér að þjónustan er niðri en í að reka fjarmælingaleiðslu. Settu harða varðveislutakmörkun svo fjarmælingakostnaður geti ekki hljóðlega farið fram úr innviðunum sem hann fylgist með.

**Stórfyrirtæki.** Verkið er stjórnarhættir yfir mörg teymi: sameiginlegur OpenTelemetry-staðall, sameiginlegt fylgniauðkennakerfi og valin SLO-mælaborð svo einn viðbragðsaðili geti fylgt beiðni yfir tugi þjónusta. Stýrðu fjarmælingum sem kostnaðarstöð með varðveisluþrepum og úrtaksstefnu, staðlaðu viðvaranir á SLO-brunahraða til að halda sameiginlegri bakvakt sjálfbærri og klipptu hávaðasamar viðvaranir miðlægt svo þreyta eins teymis ónæmi ekki alla. Líttu á mælingalagið sem söluaðilahlutlausa innviði sem lifa lengur en nokkur einn bakendasamningur.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta hönnunina. Staðlaðu á opin mælitæki svo kerfi sem búist er við að keyri áratugi lifi af endurinnkaup ólíkra söluaðila án þess að vera gísl séreignarumboðsmanna og krefstu þess flytjanleika í samningnum. Notaðu uppbyggðar úttektarskrár til að sýna hver fékk aðgang að hvaða skrá og hvenær, striku út eða táknaðu persónugögn áður en þau ná fjarmælingageymslunni og sættu varðveislu við gagnalágmörkunarlög. Birtu SLO-mælaborð fyrir borgarasnúnar þjónustur svo sömu merki og verkfræðingar ykkar fylgjast með séu sýnileg sönnunargögn um skuldbindingarnar sem þið eruð látin standa við.

## Dæmi

**Sprotafyrirtæki.** Fjögurra manna sprotafyrirtæki afhendir farsímabakenda og fær sífellt óljósar kvartanir um „forritið er hægt“ sem það getur ekki endurskapað. Teymið bætir OpenTelemetry við örfáu þjónusturnar og skiptir yfir í uppbyggðar JSON-skrár með beiðniauðkenni borið frá forritinu gegnum hvern áfanga. Næsta hæga tilkynning leysist á mínútum: ein rakning sýnir vantandi gagnagrunnsvísitölu á pöntunartöflunni undir tiltekinni fyrirspurn. Því þau völdu opin mælitæki snemma flytja þau síðar úr ókeypis þrepi yfir í greiddan bakenda án þess að endurmæla neitt.

**Stórfyrirtæki.** Stór netverslunarvettvangur mælir hverja þjónustu með OpenTelemetry og dreifir rakningarauðkenni frá vafra viðskiptavinarins gegnum greiðslu, greiðsluvinnslu, birgðir og sendingu. Þegar umbreyting fellur byrjar bakvaktarverkfræðingur á SLO-brunahraðaviðvörun, opnar gullnu merkin á greiðslumælaborðinu, tekur eftir hækkaðri töf á einu svæði og fylgir áminningarrakningu að hægu gagnagrunnskalli í einni þjónustu. Eigindi með háa fjölbreytni gilda sýna að vandamálið er bundið við einn vöruflokk, sem leiðir til markvissrar lagfæringar á mínútum frekar en klukkustundum.

**Hið opinbera.** Landsbundin heilbrigðisþjónusta rekur sjúkraskrárvettvang undir ströngum úttektar- og persónuverndarreglum. Uppbyggðar skrár fanga hver fékk aðgang að hvaða skrá og hvenær og næra bæði öryggisvöktun og reglufylgniskýrslugerð, á meðan persónugreinanlegir reitir eru strikaðir út eða táknaðir í fjarmælingum. Opinber SLO-mælaborð sýna aðgengi og töf fyrir borgarasnúna tímabókun. Með því að staðla á opin mælitæki forðast stofnunin séreignarbindingu yfir kerfi sem búist er við að keyri áratugi og verði endurinnkaupað af ólíkum söluaðilum á líftíma sínum.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Helsta ávöxtun sýnileika er stórfelld lækkun á tímanum sem tekur að greina og leysa atvik. Fyrir þjónustu þar sem niðurtími er dýr borgar það að skera meðaltíma til úrlausnar úr klukkustundum í mínútur verkfærin margfalt í einu stóru atviki. Sýnileiki sparar líka verkfræðitímann sem þú myndir annars eyða í að giska, endurskapa galla og rífast um hvaða teymi er sekt og hann styttir endurgjafarlykkjuna sem leyfir teymum að afhenda af öryggi. Öryggis- og reglufylgniverðmætið er einnig raunverulegt: sömu fjarmælingar styðja innbrotsgreiningu og úttektarsönnunargögn.

Heildareignarkostnaður felur í sér mælingafyrirhöfn, fjarmælingageymslu- og fyrirspurnakostnað og agann til að velja merki úr hávaða. Þessir kostnaðarliðir eru sýnilegir og endurteknir, sem freistar forystu til að vanfjárfesta. Kostnaður þess að taka ekki upp er stærri en erfiðari að sjá: langvarandi rof, ógreind afkastavandamál, öryggisatvik fundin seint eða aldrei og verkfræðingar sem brenna út á viðvörunum sem þeir geta ekkert gert við. Færðu rök með áþreifanlegum atvikagögnum. Sýndu úrlausnartímann og viðskiptaáhrif nýlegra rofa og áætlaðu minnkunina sem betri fjarmælingar myndu skila. Að ramma sýnileika sem tryggingu sem líka flýtir fyrir afhendingu, frekar en hreinan kostnaðarlið, vinnur rökin.

## Andmynstur og gildrur

- **Allt kallar út.** Að kalla út fyrir hvert frávik kennir viðbragðsaðilum að hunsa viðvaranir, svo raunveruleg atvik sleppa í gegn.
- **Orsakabundin útköll.** Að kalla út vegna innri orsaka frekar en notendaeinkenni flæðir bakvakt af hávaða og missir nýjar bilanir.
- **Óuppbyggðar skrár.** Frjálsar textaskrár sem ekki er hægt að spyrjast fyrir um eða tengja neyða hæga, handvirka grep-leit í atvikum.
- **Þrjár stoðir í síló.** Mælikvarðar, skrár og rakningar í ótengdum verkfærum án sameiginlegra auðkenna hindra að atburði sé fylgt frá enda til enda.
- **Mælaborðaofvöxtur.** Hundruð ósnyrtra mælaborða þýða að enginn veit hvert sýnir hvort kerfið er heilbrigt.
- **Fjölbreytnihrun.** Að strípa reiti með háa fjölbreytni gilda til að spara kostnað fjarlægir einmitt gögnin sem þarf til að aflúsa þröng vandamál.
- **Söluaðilabinding.** Séreignarumboðsmenn alls staðar gera það óheyrilega dýrt að skipta um bakenda og halda gögnum þínum í gíslingu.

## Þroskalíkan

**Stig 1, Upphaf.** Sýnileiki er ad hoc og viðbragðsdrifinn. Grunnuppitímaathuganir og óuppbyggðar skrár búa á einstökum vélum, aflúsun þýðir að skrá sig inn á þjóna til að grep-a og engar sameiginlegar fjarmælingar eru til. Viðvaranir eru hávaðasamar, orsakabundnar og oft hunsaðar, svo raunveruleg atvik koma upp gegnum kvartanir notenda frekar en merki.

**Stig 2, Þróun.** Grunnvinnubrögð birtast en eru ólík eftir teymum. Sumar þjónustur senda mælikvarða og skrár á miðlægan stað, nokkur mælaborð og þröskuldaviðvaranir eru til, en skrár eru aðeins hálfuppbyggðar og rakningar vantar eða eru að hluta. Fylgni yfir þjónustur er handvirk og hvort verkfræðingur getur fylgt beiðni frá enda til enda veltur á því hvaða teymi eiga í hlut.

**Stig 3, Stöðlun.** Mælingar eru skjalfestar og framfylgdar um skipulagsheildina. OpenTelemetry yfir þjónustur með dreifðu rakningar- eða fylgniauðkenni, uppbyggð skráning með samræmdum reitaheitum, dreifðar rakningar, valin gullnu-merkja mælaborð og SLO-byggðar einkennaviðvaranir eru staðallinn sem hvert teymi fylgir. Sérhvert útkall tengist keyrsluhandbók og SLO og bakvakt er sjálfbær frekar en uppspretta kulnunar.

**Stig 4, Stjórnun.** Sýnileikalandareignin sjálf er mæld og stýrð gegn grunnlínum. Þú rekur mælingaþekju og útbreiðsluhlutfall rakningarsamhengis yfir þjónustur, hlutfall útkalla sem brugðist var við á móti hunsuð, meðaltíma til greiningar og úrlausnar, SLO-árangur og villufjárhagsáætlunarbruna og fjarmælingakostnað á þjónustu gegn fjárhagsáætlun. Göt og viðvörunarhávaði eru keyrð niður með gögnum í átt að skýrum markmiðum, úrtaksnákvæmni er staðfest svo villu- og hæga-halafærslur lifi og ákvarðanir um fara eða ekki á þekju og varðveislu eru teknar á sönnunargögnum frekar en skoðun.

**Stig 5, Samhæfing.** Sýnileiki er stöðugt bættur og samþættur um skipulagsheildina. Fjarmælingar ríkar af atburðum með háa fjölbreytni gilda leyfa ad hoc rannsókn á hverri sneið, viðvaranir eru SLO-brunahraðadrifnar með lágmarkshávaða og úrtak og varðveisla aðlagast breytilegum kostnaði og áhættu. Fjarmælingar nærir afkastagetuáætlun, öryggisgreiningu og vöruákvarðanir að rútínu og vettvangurinn endurstillir eigin merki, fjárhagsáætlanir og þekju eftir því sem kerfið, ógnamyndin og regluverksskyldur breytast.

## Hugmyndir til umræðu

- Hvar er rétta jafnvægið milli fjarmælinganákvæmni og kostnaðar fyrir mikilvægustu þjónustur ykkar?
- Hvernig ákveðið þið hvað verðskuldar útkall á móti miða á móti aðeins mælaborðsfærslu?
- Hver er stefna ykkar til að dreifa fylgniauðkennum yfir teymi sem deila hvorki kóðagrunni né útgáfuhring?
- Hvernig varðveitið þið aflúsunarkraft hárrar fjölbreytni gilda á meðan þið mætið persónuverndar- og gagnalágmörkunarkröfum?
- Ætti sýnileikaverkfæri að vera miðlægt skylduð eða valin á teymi og hverjar eru afleiðingarnar hvort sem er?
- Hvernig myndið þið sýna úttektaraðilum fram á að fjarmælingar ykkar séu fullkomnar og skemmdavarðar?

## Helstu atriði

- Vöktun greinir þekkt vandamál. Sýnileiki leyfir þér að rannsaka óþekkt án þess að afhenda nýjan kóða.
- Mælikvarðar, skrár og rakningar eru verðmætastar þegar þær eru tengdar gegnum sameiginleg auðkenni, ekki í síló.
- Staðlaðu á OpenTelemetry og uppbyggða skráningu til að vera söluaðilahlutlaus og flytjanlegur yfir langa líftíma kerfa.
- Varaðu við notendasýnilegum einkennum gegnum SLO-brunahraða, gerðu sérhvert útkall framkvæmanlegt og klipptu hávaða miskunnarlaust.
- Hannaðu mælaborð í kringum skýrt heilsulíkan eins og gullnu merkin frekar en að sýna hvern mælikvarða.
- Fjarmælingar ríkar af atburðum með háa fjölbreytni gilda eru það sem gerir aflúsun þröngra framleiðsluvandamála mögulega.

## Heimildir og frekari lestur

- Charity Majors, Liz Fong-Jones, George Miranda, *Observability Engineering: Achieving Production Excellence*
- Cindy Sridharan, *Distributed Systems Observability*
- Betsy Beyer et al., *Site Reliability Engineering* (chapters on monitoring and alerting)
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud*
- OpenTelemetry project, specification and documentation (Cloud Native Computing Foundation)
- Google, *The Four Golden Signals* (Site Reliability Engineering, monitoring chapter)
