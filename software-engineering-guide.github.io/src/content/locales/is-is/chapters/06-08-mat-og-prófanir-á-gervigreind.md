# 6.8 Mat og prófanir á gervigreind

## Yfirlit og tilgangur

Prófanir á venjulegum hugbúnaði hvíla á hughreystandi forsendu: gefið sama inntak skilar forritið sama úttaki og þú getur staðhæft nákvæmlega hvert það úttak á að vera. Gervigreind brýtur þá forsendu. Líkan getur svarað sömu spurningu á tvo vegu, báða ásættanlega. Það er hægt að gefa einkunn á kvarða frá röngu til snilldarlegs frekar en staðið eða fallið. Og oft er ekkert eitt rétt svar til að staðhæfa gegn. Þess vegna verður mat, sú grein að mæla hve vel líkan hegðar sér yfir mörg dæmigerð tilvik frekar en að athuga eitt úttak gegn einu væntu gildi, burðarás hvers traustverðs gervigreindarkerfis. Þegar teymi afhenda gervigreindareiginleika sem skammar þau er rótin næstum alltaf sú að þau höfðu enga alvöru leið til að mæla gæði fyrir útgáfu.

Fyrir stór teymi er mat það sem gerir breytingar öruggar. Þú munt skipta um líkön, endurskrifa fyrirmæli, stilla sókn og bæta við verkfærum, og sérhver þessara breytinga getur hljóðlega rýrt hegðun sem þú hélst trausta. Án endurtakanlegrar leiðar til að mæla gæði er hver breyting fjárhættuspil og hver afturför uppgötvuð af notanda. Þessi kafli er mælingarförunautur smíðakaflanna: skapandi gervigreindar og mállíkanaforrita (kafli 6.3), gervigreindarfulltrúa og sjálfstæðra kerfa (kafli 6.7) og vélnámsverkfræði og MLOps (kafli 6.2). Hann framlengir almenna prófunarstefnu þína (kafli 2.4) inn í líkindaheiminn.

Fyrirtækja- og opinbert umhverfi hækkar húfið enn frekar. Fyrirtæki sem rekur tugi gervigreindareiginleika þarf sameiginlegan matsvettvang svo hvert teymi finni ekki upp einkunnagjöf frá grunni. Opinber stofnun þarf mat sem er skjalfest og úttektarhæft, því „við prófuðum það“ verður að verða „hér eru sönnunargögnin, gagnasafnið, mælikvarðinn og samþykktin“. Mat er þar sem ábyrg og traustverð gervigreind (kafli 6.5) hættir að vera gildisyfirlýsing og verður eitthvað sem þú getur sýnt eftirlitsaðila.

## Meginreglur

- Líttu á mat sem fyrsta flokks vöru, ekki eftirþanka sem er festur á fyrir opnun.
- Mældu með dæmigerðum gögnum sem spegla raunverulega notkun, ekki leikfangadæmum sem smjaðra fyrir líkaninu.
- Sameinaðu óbeintengt mat fyrir hraða endurtekningu við beintengt mat fyrir sannleika.
- Notaðu mannlegt mat sem akkeri þitt og kvarðaðu hvern sjálfvirkan einkunnagjafa gegn því.
- Verndaðu matssöfn þín gegn mengun, annars munu tölurnar ljúga að þér.
- Tengdu mat við samfellda samþættingu sem hlið, svo gæði geti ekki hljóðlega afturför.
- Haltu áfram að mæla í framleiðslu, því gæði reka þótt kóðinn þinn geri það ekki.

## Ráðleggingar

### Taktu upp matsdrifna þróun

Áður en þú stillir fyrirmæli eða velur líkan skaltu skrifa matið. Þetta speglar prófdrifna þróun: þú skilgreinir hvað „gott“ þýðir í mælanlegum skilmálum og smíðar síðan í átt að því. Mat hér þýðir gagnasafn inntaka parað við stigunaraðferð sem skilar tölu eða einkunn fyrir hvert úttak. Byrjaðu smátt. Tuttugu vandlega valin tilvik sem endurspegla raunverulegan ásetning notenda slá þúsund tilviljanakennd. Stækkaðu safnið eftir því sem þú lærir hvar kerfið bregst og bættu hverri framleiðslubilun aftur við sem varanlegu tilviki svo sömu mistök geti ekki snúið aftur óséð.

Matsdrifin þróun breytir hegðun teymis. Þegar skilgreining á góðu er skrifuð niður og keyranleg verða rökræður um hvort breyting hjálpaði athugunarhæfar frekar en smekksatriði. Gerðu matssafnið að rýndum grip í útgáfustýringu, rétt við hlið fyrirmælanna og kóðans sem það mælir.

### Aðgreindu óbeintengt og beintengt mat og notaðu bæði

Óbeintengt mat keyrir fast gagnasafn gegnum kerfið þitt í stýrðu umhverfi, hratt, ódýrt og endurtakanlega, svo þú getir borið saman útgáfur áður en nokkuð fer í loftið. Beintengt mat mælir lifandi kerfið með raunverulegum notendum gegnum mælikvarða eins og verklok, stigmögnunarhlutfall, þumal upp og þumal niður endurgjöf og viðskiptaniðurstöður síðar í ferlinu. Óbeintengt segir þér hvort breyting sé líkleg til að vera örugg. Beintengt segir þér hvort hún virkaði í raun. Þú þarft hvort tveggja, því óbeintengd söfn ná aldrei fullkomlega raunveruleikanum og beintengd merki berast of seint til að vera eini varnarveggurinn þinn.

Tengdu þetta tvennt í lykkju. Þegar beintengdir mælikvarðar dýfa eða notendur merkja slæmt svar skaltu fanga það tilvik, merkja það og fella það inn í óbeintengda safnið. Leiddu tilraunir gegnum sama stýrða samanburð og þú notar fyrir allar vörubreytingar, sem er svið vörugreiningar og tilrauna (kafli 7.4). A/B-prófun sem sýnir að nýtt líkan lyftir verkárangri er meira virði en nokkur óbeintengd einkunn, samt er það óbeintengda einkunnin sem lét þig þora að keyra prófið.

### Smíðaðu dæmigerð matssöfn og varðu þau gegn mengun

Mat þitt er aðeins jafn heiðarlegt og gögnin. Smíðaðu gullsöfn, valin söfn inntaka með staðfestum vænum úttökum eða stigunarkvörðum, sem spegla raunverulega dreifingu þess sem notendur spyrja: algengu tilvikin, sjaldgæfu en mikilvægu tilvikin, andstæðingstilvikin og þau sem kerfið þitt hefur nú rangt. Lagskiptu þau svo þú getir lesið gæði eftir hluta frekar en að fela flokk sem bregst inni í sæmilegu meðaltali. Láttu sérfræðinga á sviðinu staðfesta væntu svörin, því gullsafn byggt á röngum svörum er verra en ekkert.

Verndaðu síðan þau gögn gegn mengun. Mengun prófunarsafns gerist þegar matsdæmi þín leka inn í þjálfunargögn líkans eða inn í fyrirmælin sjálf, svo líkanið virðist standa sig vel því það hefur í raun séð svörin. Þess vegna getur líkan skorað glæsilega á opinberu mælipróf og hrasað á raunverulegri umferð þinni. Haltu hluta matsgagna þinna einkaeign og sendu þau aldrei til þriðja aðila sem þú getur ekki treyst. Endurnýjaðu söfn með tímanum. Varastu lúmskari lekann þar sem forritarar fínstilla fyrirmæli í höndunum gegn matssafninu þar til einkunnin er merkingarlaus, form ofaðlögunar að prófinu frekar en raunverulegra umbóta. Taktu frá ferskt afskipt safn sem þú horfir aðeins á stöku sinnum.

### Veldu mælikvarða sem passa verkinu

Láttu mælinguna samsvara lögun úttaksins. Fyrir flokkun og útdrátt, þar sem rétt merki er til, gilda klassískir mælikvarðar: [nákvæmni og endurheimt](https://en.wikipedia.org/wiki/Precision_and_recall) (af atriðunum sem þú merktir, hve mörg voru rétt, og af réttu atriðunum, hve mörg fannstu), [F-einkunnin](https://en.wikipedia.org/wiki/F-score) sem jafnvægisstillir þau og nákvæm samsvörun. Fyrir allt þar sem örugg líkindi skipta máli skaltu mæla [kvörðun](https://en.wikipedia.org/wiki/Calibration_(statistics)), hvort gefin 80 prósenta vissa sé rétt um 80 prósent tímans, því vel kvarðað líkan sem veit hvenær það er óvisst er langtum öruggara en ofsjálfsöruggt.

Mynduð úttök eru erfiðari. Tilvísunarmiðaðir mælikvarðar eins og [BLEU](https://en.wikipedia.org/wiki/BLEU) og ROUGE, upphaflega smíðaðir fyrir vélþýðingu og samantekt, bera myndaðan texta saman við tilvísunartexta með því að telja skarast orð og orðasambönd. Þeir eru ódýrir og endurtakanlegir og þeir eru veikir staðgenglar fyrir gæði: þeir verðlauna yfirborðsskörun og refsa réttu svari sem er orðað öðruvísi en tilvísunin. Notaðu þá sem gróf afturfaramerki, ekki sem skilgreiningu þína á góðu. Fyrir opin verk virkar einkunnarkvarðastigun betur: skilgreindu skýr viðmið (er það jarðtengt, fullkomið, öruggt og rétt sniðið) og skoraðu hvert. Kvarðar gera huglæg gæði læsileg og rýnanleg.

### Notaðu LLM-sem-dómara, en kvarðaðu hann gegn mönnum

Að gefa mynduðu úttaki einkunn í höndunum skalast ekki, svo teymi nota í auknum mæli sterkt [stórt mállíkan](https://en.wikipedia.org/wiki/Large_language_model) sem sjálfvirkan dómara, gefa því inntakið, úttakið og kvarða og biðja það að skora. Þessi LLM-sem-dómari aðferð er hröð og furðu öflug, og hún ber raunverulega skekkju sem þú verður að stýra. Dómarar hneigjast til að kjósa lengri svör, hygla fyrsta valkostinum sem er sýndur í pöruðum samanburði (stöðuskekkja), verðlauna eigin ritstíl og geta látið blekkjast af lipri en rangri rökfærslu. Óheft gefur skekktur dómari þér örugga, nákvæma, ranga tölu.

Kvarðaðu dómarann gegn mannlegum merkjum. Láttu fólk gefa úrtaki einkunn, athugaðu síðan hve vel líkansdómarinn er sammála því og haltu áfram að stilla dómarafyrirmælin þar til samsvörun er næg til að treysta. Dragðu úr þekktri skekkju af ásetningi: slembiraðaðu valkostum, stýrðu fyrir lengd og biddu um kvarðafest stig með ástæðum frekar en bera tölu. Líttu á dómarann sem mælitæki sem þarf reglulega endurkvörðun, ekki fast véfrétt. Þegar þú smíðar dómarann skaltu sjálfgefa hæfasta líkanið sem er tiltækt, því veikur dómari er veikur reglustokkur.

### Haltu mönnum í lykkjunni fyrir sannleikann

Mannlegt mat er áfram akkerið sem hver sjálfvirkur mælikvarði er mældur gegn, svo fjárfestu í að gera það vel. Skrifaðu skýrar leiðbeiningar fyrir merkingu, þjálfaðu merkjara þína og mældu samsvörun milli merkjara, að hve miklu leyti óháðir rýnar gefa sama tilviki sömu einkunn. Lítil samsvörun þýðir yfirleitt að kvarðinn þinn er tvíræður, ekki að rýnar þínir séu kærulausir, svo lagaðu kvarðann. Í sviðum með miklu í húfi skaltu nota hæfa sérfræðinga, ekki hópvinnufólk sem skortir samhengið til að dæma lagalegt eða læknisfræðilegt svar.

### Rauðliðaprófaðu fyrir öryggi og andstæðingsstyrk

Venjuleg matssöfn mæla hvort kerfið geri rétt á sanngjörnum inntökum. [Rauðliðaprófun](https://en.wikipedia.org/wiki/Red_team), að ráðast viljandi á eigið kerfi til að finna hvar það hegðar sér illa, mælir hvað gerist undir þrýstingi. Kannaðu fyrirmælainnspýtingu, jailbreak, óöruggt efni, persónuverndarleka og skekkt úttök. Gerðu það að endurtakanlegu safni, ekki einskiptisæfingu: breyttu hverri vel heppnaðri árás í varanlegt afturfaratilvik svo lagfærður veikleiki haldist lagfærður. Þetta starf tengist beint ábyrgri og traustverðri gervigreind (kafli 6.5) og í regluverkuðu umhverfi eru þau oft sönnunargögnin sem fullnægja öryggisrýni.

### Metdu fulltrúa eftir verkárangri frá enda til enda

Fulltrúar sem skipuleggja og framkvæma yfir mörg skref verða ekki dæmdir eitt úttak í einu. Það sem skiptir máli er hvort allt verkið tókst: bókaði fulltrúinn fundinn, leysti miðann eða kláraði vinnuflæðið rétt og örugglega. Smíðaðu verkmiðað mat í sandkassaumhverfi þar sem fulltrúinn getur starfað gegn raunhæfum en öruggum prófunargögnum og skoraðu lokaniðurstöður auk ferilsins, það er runu skrefa og verkfærakalla sem hann tók til að komast þangað. Rétt svar fengið gegnum hættulega eða sóunarsama leið er samt vandamál. Þetta er nauðsynlegt fyrir gervigreindarfulltrúa og sjálfstæð kerfi (kafli 6.7), þar sem ein röng aðgerð getur haft raunverulegar afleiðingar.

### Tengdu mat við CI og vaktaðu framleiðslu

Gerðu mat sjálfvirkt. Keyrðu óbeintengda safnið þitt í [samfelldri samþættingu](https://en.wikipedia.org/wiki/Continuous_integration) (CI) á hverja breytingu á fyrirmælum, líkani eða sókn og hliðaðu sameiningar á því rétt eins og þú hliðar á einingaprófum, venja sem á rætur í víðtækari prófunarstefnu þinni (kafli 2.4). Því einkunnir eru hávaðasamar skaltu hliða á þröskuldum og þróun frekar en að krefjast fullkominnar keyrslu, og láta smíðina falla þegar lykilmælikvarði fer niður fyrir gólf sitt eða afturför fer yfir sett svigrúm. Haltu síðan áfram að fylgjast með í framleiðslu: vaktaðu gæðamerki, úttaksdreifingar og inntaksrek svo þú grípir hæga rýrnun sem óbeintengd próf missa af, sem tengist vöktunarvinnubrögðum vélnámsverkfræði og MLOps (kafli 6.2). Líkan sem var nákvæmt við opnun getur rýrnað þegar heimurinn sem það lýsir breytist undir því.

## Málamiðlanir: kostir og gallar

| Matsaðferð | Kostir | Gallar | Best þegar |
|---|---|---|---|
| Mannlegt mat | Hæsta trúverðugleiki, fangar blæbrigði | Hægt, kostnaðarsamt, erfitt að skala | Sannleikur, mikið í húfi, kvörðun dómara |
| LLM-sem-dómari | Hraður, ódýr, skalast í stór söfn | Skekktur, þarfnast kvörðunar | Tíðar óbeintengdar keyrslur á myndað úttak |
| Tilvísunarmiðaðir mælikvarðar (BLEU, ROUGE) | Ódýrir, ákvörðunarbundnir, endurtakanlegir | Veikur staðgengill fyrir raunveruleg gæði | Gróf afturfaramerki, ekki lokadómar |
| Klassískir mælikvarðar (nákvæmni, endurheimt, F-einkunn) | Hlutlægir, vel skildir | Passa aðeins verkum með réttum merkjum | Flokkun, útdráttur, sókn |
| Opinber mælipróf | Sambærileg milli líkana, engin uppsetning | Mengun, léleg passun við verk þitt | Snemmbúin líkanaúrval, ekki útgáfuhlið |
| Beintengt mat (A/B, endurgjöf) | Endurspeglar raunverulega notendur og niðurstöður | Hægt, berst eftir útsetningu | Að staðfesta að breyting hjálpaði í raun |

Kjarnaspennan er hraði gegn trúverðugleika. Mannlegt mat er traustverðugast og minnst skalanlegt. Sjálfvirk einkunnagjöf er öfug. Lausnin er að leggja þau í lög: notaðu hraðar, ódýrar aðferðir fyrir stöðuga endurtekningu, festu þær við mannlegt mat með reglulegri kvörðun og taktu frá fulla mannlega rýni fyrir ákvarðanir með mestu í húfi og til að athuga að ódýru mælikvarðarnir fylgi enn raunveruleikanum. Önnur spenna er óbeintengd þægindi gegn beintengdum sannleika. Óbeintengd söfn leyfa þér að hreyfa þig hratt en spegla framleiðslu aldrei fullkomlega, svo líttu á sterka óbeintengda einkunn sem leyfi til að keyra vandlegt beintengt próf, ekki sönnun þess að þú sért búinn.

## Spurningar til að ræða með teyminu

1. **Hver er „nógu gott“ viðmið okkar og hver á matssafnið sem skilgreinir það?** Sérhver gervigreindareiginleiki hefur falið gæðaþröskuld og þegar hann er ósagður setur hver verkfræðingur sinn eftir tilfinningu og deilur eru útkljáðar af þeim sem er elstur í herberginu. Að skrifa viðmiðið niður sem keyranlegt matssafn með markeinkunnum á hluta breytir þeim deilum í mælanlegar spurningar. Komdu með núverandi skilgreiningu þína á árangri, gögnin á bak við hana og heiðarlega frásögn af því hver viðheldur henni í raun, því matssafn án eiganda rotnar jafn hratt og hver annar ósinnti kóði. Ákveddu hvort viðmiðið sé ólíkt eftir áhættustigi, þar sem opinbert lagasvar ætti að standast hærra viðmið en innra hugmyndaflugstæki. Svarið ætti að segja þér hvort nokkur geti nú afhent gervigreindarbreytingu án nokkurs mælingarstaðals milli hans og notenda.

2. **Hvernig vitum við að matstölur okkar eru heiðarlegar frekar en mengaðar eða ofaðlagaðar?** Einkunn er aðeins gagnleg ef hún spáir fyrir um raunveruleg gæði og margar leiðir eru til að hún hætti því: mæliprófsgögn leka inn í þjálfun, forritarar fínstilla fyrirmæli gegn prófasafninu þar til talan er merkingarlaus eða gullsafn byggt á svörum sem aldrei voru staðfest. Komdu með sönnunargögn um hvaðan matsgögn þín komu, hve mikið af þeim er haldið einkaeign og hve oft þau eru endurnýjuð. Ræddu hvort þú haldir ferskt afskipt safn sem þú horfir sjaldan á, svo þú hafir að minnsta kosti eina tölu sem enginn hefur fínstillt gegn. Ef þú getur ekki útskýrt hvers vegna einkunnir þínar myndu enn halda á gögnum sem líkanið hefur aldrei haft áhrif á ertu að mæla þína eigin endurspeglun.

3. **Hvar halda menn sér í lykkjunni og hvernig höldum við sjálfvirkum dómurum okkar kvarðaðum gegn þeim?** LLM-sem-dómari og tilvísunarmælikvarðar leyfa þér að gefa einkunn í stærð, og þeir reka frá mannlegum dómi á vegu sem eru ósýnilegir nema þú athugir. Komdu með núverandi samsvörunarhlutfall milli sjálfvirkrar einkunnagjafar og mannlegrar rýni, hve nýlega þú mældir það og hvaða skekkju (lengd, stöðu, stíl) þú hefur prófað fyrir. Ákveddu hvaða ákvarðanir krefjast mannlegs einkunnagjafa óháð kostnaði, venjulega þær sem hafa mest í húfi og þær sem eru notaðar til að endurkvarða sjálfvirka dómarann. Ræddu líka gæði merkingar, því dómari kvarðaður gegn ósamkvæmum mannlegum merkjum erfir þann ósamkvæmni. Svarið ætti að framleiða áætlun um endurkvörðun, ekki einskiptisblessun.

4. **Hvaða gervigreindarbreytingar eru hliðaðar á mati í dag og hverjar ná enn til notenda á sjálfstrausti einhvers einu?** Hlið sem keyrir á sumum breytingum en ekki öðrum gefur þér blekkingu um öryggi á meðan raunverulegar afturfarir renna í gegnum óhliðuðu leiðina: hljóðláta fyrirmælalagfæringu, sóknarstillingu, líkanaútgáfuhækkun sem enginn taldi breytingu. Fyrir stórt teymi vex hættan með fjölda fólks sem getur snert fyrirmæli, því hver óhliðuð leið er leið til að afhenda afturför sem ekkert gagnasafn sá nokkru sinni. Komdu með lista yfir breytingategundir sem nú ræsa óbeintengda safnið í samfelldri samþættingu, þær sem gera það ekki og síðustu atvikin rakin til óhliðaðrar breytingar. Ákveddu hvaða þröskuld og þróun hliðið framfylgir, því hávaðasöm einkunn krefst gólfs og afturfarasvigrúms frekar en kröfu um fullkomna keyrslu. Í fyrirtækja- og opinberu umhverfi skaltu tengja hliðið við útgáfuskrána sjálfa, svo sönnunargögnin um að breyting var mæld séu hluti úttektarslóðarinnar en ekki skjáskot sem einhver tók einu sinni.

5. **Hve miklu eyðum við í mat og er sú eyðsla í samræmi við áhættu hvers eiginleika?** Mat er ekki ókeypis: merkingarvinna, reikniafl sem sjálfvirkir dómarar brenna á hverri keyrslu og viðvarandi vinna við að halda gullsöfnum dæmigerðum kosta allt raunverulega peninga, og teymi sem nefnir aldrei þann kostnað hneigist annaðhvort til að vanfjárfesta á eiginleika með miklu í húfi eða gullhúða einnota. Togið á móti er milli trúverðugleika og fjárhagsáætlunar, því traustverðasta aðferðin, sérfræðingarýni manna, er líka sú minnst skalanlega, svo þú hefur ekki efni á henni alls staðar og verður að ákveða hvar hún vinnur sér verð. Komdu með núverandi kostnað á matskeyrslu, merkingartíma á eiginleika og heiðarlegt áhættustig fyrir hvert kerfi svo herbergið sjái hvert peningarnir fara á móti hvar hættan býr. Fyrir fyrirtæki er þetta sterkustu rökin fyrir sameiginlegum matsvettvangi sem dreifir merkingu og reikniafli yfir mörg teymi. Fyrir opinbera stofnun ætti áhættustigið að varpast beint á dýpt sönnunargagna sem eftirlitsaðili mun síðar krefjast.

6. **Þegar betra líkan kemur, hve hratt getum við sannað hvort það hjálpar og hver má gera skiptin?** Verðmæti matssafns kemur skarpast fram daginn sem sterkara líkan kemur út, því teymi sem getur keyrt gullsöfn sín og rauðliðasafn gegn nýja líkaninu á einum eftirmiðdegi getur tekið upp umbætur sem teymi sem gefur einkunn í höndunum missir af mánuðum saman. Spennan er milli hraða og varúðar: þú vilt hreyfa þig daginn sem betra líkan birtist og þú getur ekki leyft skiptum að hljóðlega rýra flokk svara sem meðaltalið þitt felur. Komdu með tímann sem það tekur nú að keyra fullan óbeintengdan samanburð gegn nýjum veitanda, hvort matssöfn þín séu flytjanleg milli líkana og hlutana þar sem afturför skipti mestu máli. Í regluverkuðu og opinberu umhverfi skaltu nefna hver hefur vald til að samþykkja líkanabreytingu og hvaða skjalfest sönnunargögn hann krefst, því óskjalfest líkanaskipti á bak við ákvörðun sem snýr að borgara er nákvæmlega sú breyting sem úttektaraðili mun biðja þig að rökstyðja.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Smíðaðu minnsta heiðarlega matið sem þú getur og láttu það vaxa með vörunni. Töflureiknir með tuttugu til fjörutíu raunverulegum tilvikum, hvert með staðfestu væntu svari, keyrður af skriftu fyrir hverja sameiningu, slær hvaða opinbert mælipróf sem er fyrir þitt svið og kostar nánast ekkert. Slepptu sameiginlega vettvanginum og LLM-sem-dómaranum þar til einkunnagjöf í höndunum særir í raun, en felldu hverja bilun sem notandi tilkynnir inn í safnið frá fyrsta degi, því það viðbragð er það sem kemur í veg fyrir sömu skömmina tvisvar.

**Lítið fyrirtæki.** Þú hefur líklega engan matssérfræðing og kaupir gervigreind innbyggða í verkfæri, svo verkefni þitt er að krefjast sönnunargagna frekar en að smíða þau. Spyrðu hvern seljanda hvernig hann mældi gæði, hvort hann prófi á gögnum sem líkjast þínum og hvernig þú myndir taka eftir afturför eftir uppfærslu sem þú valdir ekki. Haltu litlu einkasafni þinna eigin raunverulegu tilvika til að skoða verkfærið sjálfur, því rangt sjálfvirkt svar sem nær til viðskiptavinar kostar þig langtum meira en mínúturnar sem sú athugun tekur.

**Stórfyrirtæki.** Vinningurinn er sameiginlegur matsvettvangur svo tugur teyma finni ekki hvert upp einkunnagjöf: sameiginleg geymsla fyrir gullsöfn, óbeintengd söfn hliðuð í samfelldri samþættingu, skráð LLM-dómara fyrirmæli með kvörðunareinkunnum sínum og beintengdir mælikvarðar á eiginleika. Leggðu stjórnarhætti ofan á með áhættustigum sem setja nauðsynlegt viðmið og samþykktina fyrir útgáfu, svo eiginleiki með miklu í húfi standist hærra hlið en innra tæki. Vettvangurinn dreifir merkingu og reikniafli yfir teymi, sem eru sterkustu rökin fyrir að smíða einn frekar en láta hvern hóp spinna.

**Hið opinbera.** Mat verður að vera úttektarhæft, ekki bara gert, svo geymdu útgáfu gagnasafnsins, mælikvarðana, nafn rýnisins og samþykktina sem ábyrgðarsönnunargögn fyrir hverja útgáfu. Rauðliðasafn ætti að sanna að kerfið neiti að finna upp stefnu eða fullyrða lög sem eru ekki í heimildum þess og innkaup ættu að krefjast þess að seljendur upplýsi hvernig þeir mátu líkanið og veiti flytjanleika matsgagna þinna. Þegar eftirlitsaðili spyr hvernig þú veist að verkfærið er öruggt verður svarið að vera dagsett skrá, ekki fullvissun.

## Dæmi

**Sprotafyrirtæki.** Fjögurra manna fyrirtæki sem smíðar gervigreindaraðstoðarmann til samningsrýni byrjaði á töflureikni með fjörutíu raunverulegum ákvæðum, hvert merkt af innanhúslögfræðingi þeirra með áhættunni sem það ætti að merkja. Hver fyrirmælabreyting keyrði gegn því safni í skriftu fyrir sameiningu og einkunnin prentaðist í sameiningarbeiðninni. Þegar notendur merktu ákvæði sem var misst fór það beint í töfluna, svo safnið óx með vörunni. Þegar magn jókst bættu þau við LLM-sem-dómara til að gefa útskýringargæðum einkunn, en aðeins eftir að hafa athugað að hann væri sammála lögfræðingnum á úrtaki. Ódýrt, einkaeign og heiðarlegt sló hvaða opinbert mælipróf sem er fyrir þeirra svið.

**Stórfyrirtæki.** Stór banki rak tugi gervigreindareiginleika yfir stuðning, leit og innri verkfæri og hvert teymi hafði gefið einkunn öðruvísi. Þau smíðuðu sameiginlegan matsvettvang: sameiginlegan stað til að geyma gullsöfn, keyra óbeintengd söfn í CI, skrá LLM-dómara fyrirmæli með kvörðunareinkunnum og rekja beintengda mælikvarða á eiginleika. Stjórnarhættir sátu ofan á, með áhættustigum sem settu nauðsynlegt viðmið og samþykktina sem þurfti fyrir útgáfu. Nýr svikaútskýringareiginleiki gat ekki farið í loftið fyrr en matssafn hans var rýnt, rauðliðasafn hans stóðst og ábyrgur eigandi hans skrifaði undir niðurstöðurnar. Endurnotkun vettvangsins þýddi að teymi rökræddu svið sitt, ekki hvernig á að mæla.

**Hið opinbera.** Opinber heilbrigðisstofnun setti upp aðstoðarmann til að hjálpa starfsfólki að svara bótaspurningum út frá samþykktri leiðsögn. Því rangt svar gat haft áhrif á rétt einhvers varð mat að vera úttektarhæft. Hver útgáfa keyrði skjalfest matssafn sem náði yfir algengar spurningar, jaðartilvik og andstæðingsfyrirmæli og niðurstöðurnar, útgáfa gagnasafnsins, mælikvarðarnir og nafn rýnisins voru geymd sem ábyrgðarsönnunargögn. Rauðliðasafn athugaði að kerfið neitaði að finna upp stefnu eða fullyrða lög sem voru ekki í heimildum þess. Þegar eftirlitsaðili spurði hvernig stofnunin vissi að verkfærið væri öruggt var svarið dagsett skrá, ekki fullvissun.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Mat borgar sig með því að gera hverja aðra gervigreindarfjárfestingu öruggari og hraðari. Ávöxtun þess (ROI) birtist sem færri framleiðsluatvik, hraðari endurtekning því teymi geta breytt fyrirmælum og líkönum af öryggi og getan til að taka upp betri líkön daginn sem þau koma því þú getur sannað hvort þau hjálpa. Skýrasta leiðin til að verðmeta það er kostnaður fjarveru þess: ein opinber ofskynjun, skekkt úttak eða gagnaleki getur kostað langtum meira í úrbótum, glötuðu trausti og eftirlitsáhættu en ára matsinnviðir. Það er munurinn á að finna afturför í CI ókeypis og að finna hana í dagblaðinu.

Heildareignarkostnaður (TCO) er raunverulegur og vert að nefna. Þú borgar fyrir merkingarvinnu, fyrir reikniaflið sem sjálfvirkir dómarar nota og fyrir viðvarandi vinnu við að halda matssöfnum dæmigerðum eftir því sem notkun breytist. Í fyrirtækjastærð dreifir sameiginlegur vettvangur mestu af þessu yfir mörg teymi, sem eru sterkustu rökin fyrir að smíða einn frekar en láta hvern hóp spinna. Færðu rök við forystu með því að para áþreifanlega áhættu (kostnað eins slæms opinbers svars í þínu sviði) við áþreifanlega getu (hraðann til að taka upp hvert nýtt líkan örugglega) og með því að ramma mat sem eftirlitið sem leyfir skipulagsheildinni að hreyfa sig hratt án þess að hreyfa sig kæruleysislega.

## Andmynstur og gildrur

- **Tilfinningadrifin útgáfa.** Að dæma gervigreindarbreytingar með því að prófa nokkur fyrirmæli í höndunum, án gagnasafns og án endurtakanlegrar einkunnar.
- **Mæliprófaleikhús.** Að treysta sterkri opinberri mæliprófseinkunn sem sönnun þess að kerfið passi verki þínu og hunsa mengun og dreifingarmisræmi.
- **Ofaðlögun að matssafninu.** Að fínstilla fyrirmæli gegn sama fasta safni þar til talan er há og merkingarlaus, án ferskrar afskiptrar viðmiðunar.
- **Ókvarðaðir dómarar.** Að setja upp LLM-sem-dómara og treysta einkunnum hans án þess að athuga nokkurn tímann samsvörun við mannlega einkunnagjafa.
- **Mælikvarðadýrkun.** Að fínstilla BLEU eða ROUGE eins og það séu gæði og afhenda verri svör sem skarast tilviljanakennt við tilvísunartextann.
- **Einskiptis rauðliðaprófun.** Að ráðast á kerfið einu sinni fyrir opnun og breyta niðurstöðum aldrei í varanleg afturfarapróf.
- **Eingöngu óbeintengt sjálfstraust.** Að trúa að góð óbeintengd einkunn þýði að eiginleikinn virki, án beintengdrar mælingar á raunverulegum niðurstöðum.
- **Munaðarlaus matssöfn.** Gagnasöfn sem enginn á, sem taka aldrei við framleiðslubilunum og hætta hægt að endurspegla raunveruleikann.

## Þroskalíkan

- **Stig 1, Upphaf:** Gervigreindarbreytingar eru dæmdar í höndunum á nokkrum dæmum, viðbragðsdrifið, þegar einhver hefur áhyggjur. Ekkert gagnasafn, engin endurtakanleg einkunn og ekkert hlið. Afturfarir finnast af notendum og enginn getur sagt hvort kerfið er betra eða verra en í síðasta mánuði.
- **Stig 2, Þróun:** Sum teymi halda litlum gullsöfnum og keyra þau handvirkt fyrir stórar breytingar og nokkrar klassískar eða tilvísunarmiðaðar einkunnir eru til. Mannleg rýni á sér stað fyrir mikilvæga eiginleika, en einkunnagjöf er ósamræmd milli teyma, mat er ekki sjálfvirkt eða hliðað og hver hópur gerir það öðruvísi.
- **Stig 3, Stöðlun:** Óbeintengd söfn keyra í samfelldri samþættingu á hverja breytingu á fyrirmælum, líkani eða sókn og hliða sameiningar, eftir einni skjalfestri venju um skipulagsheildina. LLM-sem-dómari er kvarðaður gegn mannlegum merkjum, rauðliðaprófun er endurtakanlegt safn og gagnasöfn eru í eigu, útgáfustýrð og nærð af framleiðslubilunum, með mengun virkt varða.
- **Stig 4, Stjórnun:** Mat er mælt og stýrt með gögnum gegn grunnlínum. Samsvörunarhlutföll dómara og manns, rauðliðapróf árangurshlutföll, einkunnir á hluta, beintengdur verkárangur og rek eru rakin yfir tíma og sameiningar hliða á þröskuldum og afturfarasvigrúmi frekar en einni fullkominni keyrslu. Merkingarkostnaður og reikniafl á keyrslu eru fjárhagsáætluð á eiginleika, endurkvörðun gerist á áætlun og hver niðurstaða ber ábyrgan eiganda og samþykkt.
- **Stig 5, Samhæfing:** Sameiginlegur matsvettvangur þjónar allri skipulagsheildinni og óbeintengt og beintengt mat mynda samfellda lykkju tengda viðskiptaniðurstöðum. Ný líkön eru sönnuð gegn flytjanlegum matssöfnum daginn sem þau koma, eignasafnið aðlagast eftir því sem notkun og áhætta breytast, matssönnunargögn eru úttektarhæf fyrir eftirlitsaðila og lærdómur af bilunum eins teymis flæðir inn í gagnasöfn allra teyma.

## Hugmyndir til umræðu

1. Hvernig ákveðurðu hvenær óbeintengd einkunn er nógu sterk til að réttlæta beintengda tilraun, og hvenær ekki?
2. Hvert er rétta hlutfall mannlegs mats og sjálfvirkrar einkunnagjafar fyrir áhættusnið þitt og hve oft ættirðu að endurskoða það?
3. Þegar opinbert mælipróf og einkamatssafn þitt eru ósammála um hvaða líkan er betra, hverju treystirðu og hvers vegna?
4. Hvernig heldurðu matssafni dæmigerðu þegar hegðun notenda breytist, án þess að láta það þenjast út í eitthvað of hægt til að keyra í CI?
5. Hvað tilheyrir rauðliðasafni fyrir þitt svið og hver er hæfur til að hanna árásirnar?
6. Hvernig metur þú feril fulltrúa, ekki bara lokasvar hans, án þess að drukkna í kostnaði við að gefa hverju skrefi einkunn?

## Helstu atriði

- Gervigreindarmat er ólíkt hugbúnaðarprófunum því úttök eru óákvörðunarbundin og sjaldan er eitt rétt svar, svo þú mælir gæði yfir dæmigerð tilvik í stað þess að staðhæfa nákvæm gildi.
- Stundaðu matsdrifna þróun: skilgreindu mælanleg gæði fyrst, smíðaðu síðan í átt að þeim og felldu hverja framleiðslubilun aftur inn í safnið.
- Leggðu aðferðir í lög eftir hraða og trúverðugleika: ódýr sjálfvirk einkunnagjöf fyrir stöðuga endurtekningu, mannlegt mat sem akkeri og kvörðun til að halda þeim samstilltum.
- Varastu mengun og ofaðlögun, annars munu tölurnar smjaðra fyrir þér á meðan raunverulega kerfið bregst notendum.
- Tengdu óbeintengt mat við CI sem hlið og haltu áfram að mæla gæði og rek í framleiðslu, því líkan sem var gott við opnun getur rýrnað.

## Heimildir og frekari lestur

- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Lianmin Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*.
- Kishore Papineni et al., *BLEU: A Method for Automatic Evaluation of Machine Translation*.
- Chin-Yew Lin, *ROUGE: A Package for Automatic Evaluation of Summaries*.
- Percy Liang et al., *Holistic Evaluation of Language Models (HELM)*.
- Deep Ganguli et al., *Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviours, and Lessons Learned*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- National Institute of Standards and Technology, *AI Risk Management Framework*.
