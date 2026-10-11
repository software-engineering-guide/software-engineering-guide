# 3.17 Leit og upplýsingaleit

## Yfirlit og tilgangur

Fyrr eða síðar skrifar einhver nokkur orð í reit og býst við að kerfið þitt finni rétta hlutinn. Sá reitur er blekkjandi einfaldur. Á bak við hann situr ein elsta og ríkasta grein tölvunarfræði: [upplýsingaleit](https://en.wikipedia.org/wiki/Information_retrieval) (information retrieval), vísindin um að finna viðeigandi atriði í stóru safni út frá ónákvæmri beiðni. Leit er ekki eiginleiki sem þú festir á vöru seint. Hún er kerfisáhyggjuefni með eigið gagnalíkan, eigin bilunarhætti, eigin stigvaxtarsögu og eigin leið til að hafa rangt fyrir sér. Þegar leit er góð finnur fólk það sem það þarf og tekur varla eftir því. Þegar leit er slæm fer það, eða verra, ályktar að það sem það vildi sé ekki til.

Þessi kafli meðhöndlar leit sem fyrsta flokks arkitektúr. Hún situr við hlið gagna- og geymsluákvarðana kafla 3.4, því leitarvísitala er sérhæfð geymsla fínstillt fyrir fyrirspurnir, aðgreind frá aðalgagnageymslunni sem á sannleikann. Hún styðst við skyndiminnis- og afhendingarhugmyndir kafla 3.15, því leitarniðurstöður og tillögur eru tafarviðkvæmar og skyndiminnishæfar. Og hún skarast nú mikið við vinnu með mállíkön og skapandi gervigreind í kafla 6.3, því nútíma upplýsingaleit færir stórum mállíkönum samhengið sem þau þurfa til að svara vel.

Fyrir stór teymi er leit þar sem mikilvægi, ferskleiki og stærð rekast saman. Fyrirtækjavörulisti með tugum milljóna atriða, opinber skrárgátt sem svarar til almennings, þekkingargrunnur þjónustuborðs sem verður að draga fram eina greinina sem leysir miðann: hvert krefst þess að leit sé mæld, stillt og rekin af sömu nákvæmni og hvert annað framleiðslukerfi. Hagsmunirnir eru áþreifanlegir. Skattayfirvald þar sem leit finnur ekki rétta eyðublaðið á skilafresti, eða heilbrigðisgátt sem grefur viðeigandi leiðbeiningar undir hávaða, bregst notendum á hátt sem tærir traust á stofnuninni að baki.

## Meginreglur

- Líttu á leitarvísitöluna sem afleidda geymslu, aðgreinda frá aðalgagnageymslunni þinni.
- Mikilvægi er mælanleg gæði, ekki smekksatriði. Dæmdu það með gögnum.
- Samsvaraðu því hvernig fólk skrifar í raun: stafsett rangt, stuttaralega og tvíræða.
- Sameinaðu orðbundna og merkingarlega upplýsingaleit. Hvorug ein og sér nær yfir hverja fyrirspurn.
- Hannaðu vísitöluleiðsluna fyrir ferskleika, ekki bara fyrstu hleðslu.
- Metið utan nets með dómum og á netinu með raunverulegri hegðun, og notaðu hvort tveggja.
- Stigvaxaðu leit af ásetningi með sneiðum og afritum og fylgstu með henni eins og hverri þjónustu.

## Ráðleggingar

### Byrjaðu á umhverfu vísitölunni og greiningarleiðslunni

Vélin í hjarta klassískrar leitar er [umhverf vísitala](https://en.wikipedia.org/wiki/Inverted_index) (inverted index): varp frá hverju hugtaki á lista skjalanna sem innihalda það, spegilmynd skjals sem listar hugtök sín. Biddu um „reikningur endurgreiðsla“ og vélin sker bókunarlistann fyrir „reikningur“ við bókunarlistann fyrir „endurgreiðsla“ á millisekúndum, sama hve mörg milljón skjöl þú heldur. Þessi gagnagerð er ástæða þess að leit finnst tafarlaus, og að skilja hana útskýrir mest af því sem leit gerir og gerir ekki vel.

Vísitalan er aðeins jafn góð og textinn sem þú gefur henni, og það er verk [greinisins](https://en.wikipedia.org/wiki/Text_normalization). Greining keyrir í áföngum. Fyrst skiptir [tilkenning](https://en.wikipedia.org/wiki/Lexical_analysis) (tokenisation) textastraumi í hugtök, sem er erfiðara en að skipta á bilum þegar þú mætir greinarmerkjum, bandstrikun og málum eins og kínversku sem afmarka ekki orð. Síðan lágstafar, fjarlægir áherslumerki og fellir afbrigði saman. Síðan dregur [stofnun](https://en.wikipedia.org/wiki/Stemming) (stemming) eða nákvæmari frænka hennar lemmun „hlaupa“, „hljóp“ og „hleypur“ í átt að sameiginlegum stofni svo fyrirspurn um eitt passi við hin. Stoðorðameðhöndlun, samheitaþensla og málgreining fylla upp. Reglan sem sparar þér sársauka: greining við vísitölugerð og greining við fyrirspurn verða að vera sammála, því hugtak finnst aðeins ef báðar hliðar normaða það eins.

### Skildu mikilvægisröðun áður en þú stillir hana

Að finna samsvarandi skjöl er auðveldi helmingurinn. Að raða þeim svo það besta sitji efst er erfiði helmingurinn, og það kallast röðun. Hefðbundni vinnuhesturinn er [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf), stytting á hugtakstíðni sinnum umhverf skjalatíðni: hugtak vegur meira þegar það birtist oft í skjali (hugtakstíðni) og þegar það er sjaldgæft yfir allt safnið (umhverf skjalatíðni), svo „ljóstillífun“ vegur þyngra en „og“. Flestar nútímavélar nota [Okapi BM25](https://en.wikipedia.org/wiki/Okapi_BM25) sem sjálfgefið, endurbót sem mettar hugtakstíðni (tíunda tilvikið bætir litlu við níunda) og normar fyrir skjalalengd svo löng skjöl vinni ekki með stærðinni einni saman. Þú þarft ekki að leiða formúluna út, en þú ættir að vita að hnappur er til, að hann hefur rökrétt sjálfgefin gildi og að breyting á honum breytir því hvaða niðurstöður raðast fyrst.

Dæmdu gæði með tveimur orðum úr greininni. [Nákvæmni](https://en.wikipedia.org/wiki/Precision_and_recall) (precision) er hlutfall skilaðra niðurstaðna sem eru viðeigandi. Endurheimt (recall) er hlutfall allra viðeigandi niðurstaðna sem þú skilaðir. Þau skipta hvort gegn öðru. Slakaðu á fyrirspurninni til að ná hverri mögulegri samsvörun og nákvæmni fellur þegar hávaði læðist inn. Hertu hana fyrir hreint niðurstöðusafn og endurheimt fellur þegar góðar samsvaranir detta út. Sérhver mikilvægisákvörðun, frá villuþoli til samheitaþenslu, er veðmál um hvar á þeim ferli notendur þínir vilja vera, og svarið er ólíkt fyrir lagaskjalasafn (kjóstu endurheimt, misstu ekkert) á móti verslun (kjóstu nákvæmni, sýndu sigurvegara).

### Fjárfestu í fyrirspurnarskilningi

Notendur skrifa ekki eins og skjölin þín eru skrifuð. Þeir stafsetja rangt, stytta, leita að samheiti sem þú skráðir aldrei og troða þremur ásetningum í fjögur orð. Fyrirspurnarskilningur er lagið sem brúar það bil og það borgar fjárfestingu til baka meira en nánast nokkuð annað. Bættu við völdum og numdum samheitum svo „fartölva“ finni „lófatölva“ og „hjartaáfall“ finni „hjartavöðvadrep“. Bættu við villuþoli gegnum [breytifjarlægð](https://en.wikipedia.org/wiki/Levenshtein_distance) (edit distance), fjölda eins-stafs breytinga milli tveggja strengja, svo „kvittun“ stafsett vitlaust finni samt kvittanir. Greindu einindi og ásetning svo „flug til Parísar undir $500“ leiðist á réttar síur frekar en orðapoka.

Meðhöndlaðu erfiðustu fyrirspurnirnar af ásetningi. Leit að sjaldgæfum nákvæmum streng, eins og pöntunarnúmeri eða lagatilvitnun, vill nákvæma samsvörun og enga snjalla þenslu. Óljós náttúrulegs máls spurning vill andstæðuna. Leiddu þetta ólíkt frekar en að þvinga eina hegðun á bæði. Og hannaðu alltaf [engar-niðurstöður](https://en.wikipedia.org/wiki/Faceted_search) tilvikið: þegar fyrirspurn skilar engu skaltu slaka á henni, leggja til valkosti eða falla til baka á víðari samsvörun, því tóm síða er fljótasta leiðin til að missa notanda.

### Bættu við flötun, sjálfvirkri útfyllingu og skipulagðri síun

Leit er meira en raðaður listi. [Flötuð leit](https://en.wikipedia.org/wiki/Faceted_search) (faceted search) leyfir notendum að þrengja niðurstöður eftir skipulögðum eigindum: vörumerki, verðbili, deild, dagsetningu, skjalategund. Fletir breyta yfirþyrmandi niðurstöðusafni í leidda samræðu og tvöfaldast sem leiðsögn. Þeir byggja á að gögn þín séu hreint eigindamerkt, sem er gagnagæðafjárfesting andstreymis leitar, og þeir víxlverka við röðun, því sía breytir frambjóðendasafninu sem röðunarvélin sér.

Sjálfvirk útfylling og tillögur móta fyrirspurnina áður en hún er send. Góður tillögugjafi leggur til raunverulegar, verðmætar fyrirspurnir meðan notandinn skrifar, leiðréttir stafsetningu snemma og dregur fram vinsæla eða vaxandi ásetninga. Hann er tafarkritískur (hvert lyklaslag er beiðni) og nýtur beint skyndiminnismynstra kafla 3.15. Tillögur stýra fólki líka að fyrirspurnum sem þú meðhöndlar vel, sem hljóðlega hækkar heildarmikilvægi. Líttu á tillögugjafann sem sína eigin litlu vísitölu með eigin röðun, stillta á fyrirspurnaskrár frekar en skjalaefni.

### Sameinaðu orðbundna og vektorleit

Klassísk leit samsvarar orðum. Hún getur ekki sagt að „bíll“ og „vélknúið ökutæki“ merki hið sama nema þú segðir henni það, og hún hrasar á spurningum orðuðum á vegu sem skjölin þín nota aldrei. [Vektorleit](https://en.wikipedia.org/wiki/Nearest_neighbor_search) tekur á þessu með því að tákna texta sem [fellingu](https://en.wikipedia.org/wiki/Word_embedding) (embedding), þéttan tölulegan vektor framleiddan af vélnámslíkani þannig að svipuð merking lendi nálægt hvor annarri í vektorrýminu. Upplýsingaleit verður þá næstunágrannaleit í því rými, og því nákvæm næstu nágrannaleit er of hæg í stærð nota vélar áætlaða næstu nágranna (ANN) reiknirit sem skipta örlitlu af nákvæmni fyrir mikinn hraða. Merkingarleg leit af þessu tagi finnur rétta skjalið jafnvel þegar það deilir engum orðum með fyrirspurninni.

Hvorug nálgun vinnur alls staðar. Orðbundin leit skarar fram úr á nákvæmum hugtökum, nöfnum, kóðum og sjaldgæfum lykilorðum. Hún er gagnsæ og ódýr að útskýra. Vektorleit skarar fram úr á merkingu, umorðun og náttúrulegs máls spurningum, en hún getur misst af nákvæmu auðkenni og er erfiðari að villuleita. Sterka sjálfgefið fyrir alvarleg kerfi er [blendingsleit](https://en.wikipedia.org/wiki/Learning_to_rank): keyrðu bæði og sameinaðu niðurstöður, oft með tækni eins og gagnkvæmri röðunarsamruna (reciprocal rank fusion) sem blandar tveimur röðuðum listum án þess að stig þeirra þurfi að vera samanburðarhæf. Blendingur gefur þér nákvæmni lykilorða og endurheimt merkingar, og hann skerðist mjúklega þegar önnur hliðin er veik.

### Tengdu leit við sóknarauðgaða myndun

Hraðast vaxandi neytandi leitar er ekki manneskja sem les niðurstöðulista. Það er mállíkan. [Sóknarauðguð myndun](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (RAG) festir skapandi líkan í gögnum þínum með því að sækja viðeigandi kafla og setja þá í samhengi líkansins svo það svari úr staðreyndum þínum frekar en þjálfunarminni sínu. Myndunargæði kafla 6.3 eru beint háð sóknargæðum: gefðu líkaninu ranga kafla og það mun sjálfsöruggt setja saman rangt svar. Allt í þessum kafla (að skipta texta í kafla, raða þeim vel, sameina orðbundin og vektormerki, halda vísitölunni ferskri) er einmitt sóknarhelmingur RAG. Ef skipulagsheild þín smíðar á stórum mállíkönum er leitarkerfi þitt grunnurinn, og að bæta endurheimt á réttu köflunum hjálpar aðstoðarmanninum oft meira en að skipta um líkan.

### Smíðaðu vísitöluleiðslu fyrir ferskleika

Vísitala er afrit og afrit rekur. Vísitöluleiðslan er vélbúnaðurinn sem heldur leitarvísitölunni í takti við aðalgagnageymsluna: les upprunabreytingar, keyrir greiningu og fellingu og skrifar í vísitöluna, helst sem straum frekar en næturlotu. Þetta er gagnaverkfræðiáhyggjuefni (kafli 7.2), og sama varkárni um röð, endurtekningar og eins-áhrif úr kafla 3.3 gildir, því úr takti uppfærsla getur reist eytt skjal upp frá dauðum. Ákveddu ferskleikamarkmið þitt skýrt. Verð eða birgðatala gæti þurft að vera leitarhæf innan sekúndna. Skjalavistað stefnuskjal getur dregist aftur úr um klukkustundir. Styddu fulla endurvísitölugerð fyrir skema- og greinibreytingar og hannaðu hana til að keyra án niðurtíma, yfirleitt með því að smíða nýja vísitölu og skipta um samnefni atómískt þegar hún er tilbúin.

### Stilltu mikilvægi með mati, ekki skoðun

Mikilvægisrökræður eru ósigranlegar með fullyrðingum, svo komdu mælingum í stað skoðana. Utan nets skaltu smíða dómalista: safn dæmigerðra fyrirspurna parað við mat manna á hvaða niðurstöður eru viðeigandi, og skora röðun þína gegn honum með mælikvarða eins og [NDCG](https://en.wikipedia.org/wiki/Discounted_cumulative_gain) (normalised discounted cumulative gain), sem verðlaunar að setja mjög viðeigandi niðurstöður nálægt toppnum og afsláttar þær sem grafnar eru neðar. Mat utan nets leyfir þér að bera saman tvær röðunarstillingar áður en önnur hvor snertir notanda. Á netinu skaltu fylgjast með raunverulegri hegðun: smellihlutfalli, stöðu smellinna niðurstaðna, fyrirspurnarendurmótun, hlutfalli án niðurstaðna og umbreytingum. Keyrðu stýrðar tilraunir (kafli 7.4) svo mikilvægisbreyting sé sönnuð gegn viðmiðunarhópi frekar en afhent á hugboði. Notaðu bæði, því mælikvarðar utan nets eru hraðir en hugsjónakenndir, á meðan netmælikvarðar eru raunverulegir en hægir og hávaðasamir. Þroskaða lykkjan nemur fyrirspurnaskrár til að stækka dómalistann, svo mat batni eftir því sem þú lærir.

### Stigvaxaðu með sneiðum og afritum og fylgstu með öllu

Leit stigvaxar eftir tveimur ásum. [Sneiðing](https://en.wikipedia.org/wiki/Shard_(database_architecture)) skiptir einni vísitölu yfir vélar með því að skipta skjölum, svo fyrirspurn dreifist á hverja sneið og hlutaniðurstöðurnar sameinast. Þetta leyfir vísitölu að vaxa umfram það sem ein vél heldur og dreifir vísitölugerðarálagi. Afrit afrita hverja sneið svo lesumferð dreifist yfir eintök og missir hnúts tapar ekki gögnum. Afrit þjóna fyrirspurnarafköstum og veita seiglu. Fleiri sneiðar hækka útbreiðslukostnað á fyrirspurn, svo stærðarákvarðaðu þær eftir gögnunum þínum, ekki kringlóttri tölu. Rektu leit með sýnileika kafla 9.2: raktu fyrirspurnartafarhundraðshluta (halinn skiptir meira máli en meðaltalið), vísitölutöf, skyndiminnishitahlutföll, villuhlutföll og, sem fyrsta flokks merki, mikilvægismælikvarða eins og hlutfall án niðurstaðna og smellistöðu. Leitarkerfi sem er hratt en skilar slæmum niðurstöðum bregst hljóðlega, og aðeins mikilvægisfjarmæling mun segja þér það.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
|---|---|---|
| Orðbundin (BM25) leit | Nákvæm hugtök, kóðar, nöfn. Gagnsæ. Ódýr | Blind á samheiti og umorðun án stillingar |
| Vektorleit (merkingarleg) | Skilur merkingu og spurningar. Sterk endurheimt | Missir af nákvæmum auðkennum. Dýr í útreikningi. Erfiðari að villuleita |
| Blendingsleit | Nákvæmni lykilorða auk endurheimtar merkingar | Fleiri hreyfanlegir hlutar. Samruni þarfnast stillingar og prófana |
| Ágeng villu- og samheitaþensla | Meiri endurheimt. Fyrirgefandi gagnvart raunverulegum notendum | Nákvæmni fellur. Hávaðasamar niðurstöður ef óstýrt |
| Rauntímavísitölugerð | Ferskar niðurstöður innan sekúndna | Meiri kostnaður og flækja en lota |
| Fleiri sneiðar | Stærri vísitölur. Samsíða vísitölugerð | Meiri útbreiðsla á fyrirspurn og samhæfingarkostnaður |
| Mat utan nets (dómalistar) | Hratt, endurtakanlegt, öruggt að endurtaka | Hugsjónakennt. Passar kannski ekki við raunverulega notendahegðun |
| Mat á netinu (smellimælikvarðar, próf) | Endurspeglar raunverulega notendur og ásetning | Hægt, hávaðasamt, þarfnast umferðar og tilraunaaga |

Endurtekna spennan er nákvæmni gegn endurheimt og hún felur sig inni í hverjum hnapp. Slakaðu á samsvörun, þenstu samheiti og hallaðu þér að merkingu og þú nærð meira á kostnað hávaða. Hertu allt og þú ert hreinn en missir af hlutum. Engin altæk stilling er til, aðeins rétta stillingin fyrir tiltekið safn og áheyrendahóp, fundin með mælingu. Önnur spennan er ferskleiki gegn kostnaði: rauntímavísitölugerð og blendingssókn kaupa bæði gæði með reikniafli og flækju. Leystu bæði á sama hátt, með því að binda hverja ákvörðun við mikilvægismælikvarða og notendaniðurstöðu frekar en innsæi, svo þú sjáir hvað breyting keypti þér í raun.

## Spurningar til að ræða með teyminu

1. **Hvernig mælum við mikilvægi leitar í dag og myndum við taka eftir ef það versnaði?** Mörg teymi geta ekki svarað þessu, sem þýðir að mikilvægi þeirra er það sem sjálfgefnu gildin framleiddu og þau fljúga blind gagnvart afturförum. Komdu með núverandi merki þín: hefurðu dómalista, rekurðu hlutfall án niðurstaðna og smellistöðu, gætirðu borið saman tvær röðunarstillingar hlutlægt? Bilið milli „leit finnst í lagi“ og „hér er NDCG okkar á hundrað metnum fyrirspurnum og hér er þróun síðasta mánaðar“ er bilið milli þess að giska og að verkfræða. Aðgerðin sem fylgir er að smíða jafnvel lítinn dómalista og mæla smellihegðun, því þú getur ekki stillt það sem þú mælir ekki, og sérhver mikilvægisbreyting sem þú afhendir blint er breyting sem þú getur ekki varið.

2. **Hvar bregðast orðbundin og merkingarleg sókn okkur hvor um sig og ættum við að fara í blending?** Hrein lykilorðaleit bregst hljóðlega á umorðuðum spurningum og samheitum, á meðan hrein vektorleit bregst hljóðlega á nákvæmum auðkennum og sjaldgæfum hugtökum, og flest teymi hafa aðeins rekið aðra þeirra. Komdu með safn raunverulegra fyrirspurna sem skiluðu lélegum niðurstöðum og flokkaðu hvers vegna hver brást: var það vantandi samheiti, stafsetningarvilla, merkingarleg misræmi eða vantandi nákvæm samsvörun? Mynstrið í þessum bilunum segir þér hvort blendingsleit myndi hjálpa og hvar á að eyða fyrirhöfn fyrst. Þetta skiptir meira máli ef þú nærir mállíkan, því sóknarbilanir verða sjálfsörugg röng svör, og kostnaður slæmrar niðurstöðu hækkar skarpt þegar skapandi lag situr ofan á.

3. **Hver er ferskleikakrafa okkar og uppfyllir vísitöluleiðslan okkar hana í raun?** Ferskleiki er yfirleitt gert ráð fyrir frekar en tilgreindur, svo teymi uppgötva misræmið í atviki þegar eytt atriði heldur áfram að birtast eða verðuppfærsla dregst aftur úr um klukkustundir. Komdu með raunverulegu tölurnar: hve langur tími frá breytingu í aðalgagnageymslunni þar til sú breyting er leitarhæf, og hvernig ber það saman við það sem mismunandi hlutar vörulistans þíns þurfa í raun? Svarið mun líklega vera ólíkt eftir gagnategund, og að nefna það neyðir fram leiðsluákvarðanirnar um straum á móti lotu, röð og endurvísitölugerð. Vísitala sem er úrelt á vegu sem notendur þínir sjá tærir traust á allri vörunni, og ferskleikamarkmið sem þú hefur aldrei mælt er markmið sem þú ert líklega að missa af.

4. **Smíðum við leit á eigin vél eða kaupum við stýrða leitar- eða vektorþjónustu og hvað myndi kosta okkur að skipta um skoðun síðar?** Smíða-eða-kaupa ákvörðunin setur kostnaðarbyggingu þína og stjórnarþak í ár, og stór teymi reka gjarnan inn í eitt svar af tregðu frekar en að ákveða það af ásetningi. Komdu með raunverulegu tölurnar beggja vegna: rekstrarkostnað við að reka og stigvaxa eigin klasa og fellingarleiðslu á móti kostnaði á fyrirspurn eða áskrift stýrðrar þjónustu, og verkfræðitímann sem hvort krefst af fólki sem þú gætir sett annars staðar. Falin breytan er binding: hve mikið af röðun þinni, greiningu og vektorskema er flytjanlegt og hve lengi flutningur myndi í raun taka ef verðlagning eða geta breyttist undir þér. Í fyrirtækja- og opinberu umhverfi skaltu bæta við innkaupafyrirvara og útgönguskyldum, því þjónusta sem getur ekki afhjúpað röðunarhegðun sína eða flutt út vísitöluna þína er ósjálfstæði sem þér kann ekki að vera heimilt að samþykkja.

5. **Hve mikið erum við reiðubúin að fjárfesta í fyrirspurnarskilningi og hver rýnir fyrirspurnirnar sem bregðast?** Notendur stafsetja rangt, stytta og orða spurningar í orðum sem skjölin þín nota aldrei, svo bilið milli hrárrar fyrirspurnar og góðrar niðurstöðu er þar sem mest af skynjuðum leitargæðum býr, samt er það sjaldan skýrt verk neins. Komdu með hlutfall án niðurstaðna, efstu bregðandi og endurmótuðu fyrirspurnir þínar og heiðarlega frásögn af samheita-, villuþols- og ásetningsmeðhöndluninni sem þú hefur í dag. Togið á móti er nákvæmni gegn endurheimt: hvert samheiti og hver eining breytifjarlægðar sem þú leyfir nær fleiri raunverulegum notendum og hleypir inn meiri hávaða, svo rétta fjárfestingin er sú sem þú getur mælt frekar en sú sem hljómar rausnarleg. Fyrir stóra eða opinbera skipulagsheild er langi hali bregðandi fyrirspurna líka kort af óuppfylltri þörf, og að rýna hann á föstum takti breytir stuðningskostnaði í vegvísi, sérstaklega þar sem misst eyðublað eða bætur hafa raunverulegar afleiðingar fyrir borgara.

6. **Hver á mikilvægi sem fjármagnaða, viðvarandi ábyrgð og hvernig mun matslykkjan lifa eftir opnun?** Leit er aldrei búin: vörulistar breytast, tungumál rekur og stilling síðasta ársfjórðungs rotnar hljóðlega, svo kerfi án ábyrgs eiganda hnígur aftur í átt að því sem sjálfgefnu gildin framleiða. Komdu með skipuritsveruleikann: er mikilvægi nefnt teymi með tíma og mælikvarða, eða verk sem lendir á hverjum sem síðast snerti vísitöluna, og er dómalisti og tilraunabúnaður til staðar sem nýr einstaklingur gæti tekið upp? Spennan er að mikilvægisvinna er óglamúrleg og auðvelt að svipta fjármögnun um leið og leit virðist virka, sem er einmitt þegar rotnunin byrjar. Í fyrirtækja- og opinberu samhengi skaltu tengja eignarhald við áþreifanlegar skyldur, nákvæmni á markað, notkunaraðgengi, fjölmála þekju og rýni á fyrirspurnum án niðurstaðna, svo ábyrgðin sé úttektarhæf og gufi ekki upp þegar opnunarteymið tvístrast.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Náðu í stýrða leitar- eða vektorþjónustu og afhentu BM25-sjálfgefin gildi á degi eitt. Settu ekki upp eigin klasa áður en þú hefur fyrirspurnir til að stilla gegn. Veldu það eina leitaryfirborð sem snertir tekjur eða varðveislu, mældu smellistöðu og hlutfall án niðurstaðna frá fyrstu útgáfu og láttu raunverulegar fyrirspurnaskrár, ekki vegvísi, segja þér hvenær á að bæta við samheitum eða merkingarlagi. Sama sóknarlagið sem þú smíðar fyrir leit verður RAG-bakendinn þinn síðar, svo haltu því á bak við þunnt viðmót.

**Lítið fyrirtæki.** Þú hefur nánast örugglega engan mikilvægisverkfræðing, svo keyptu leit innbyggða í vettvanginn sem þú rekur þegar, eins og netverslunarhýsilinn, þjónustuborðið eða efnisstjórnunarkerfið, og líttu á stillingu sem létt, endurtekið verk frekar en verkefni. Eyddu takmarkaðri fyrirhöfn í gagnagæðagrunnatriðin sem leit byggir á: hrein vörueigindi fyrir fleti, skynsamlegar fyrirsagnir og stuttan samheitalista fyrir orðin sem viðskiptavinir þínir nota í raun. Fylgstu með fyrirspurnum án niðurstaðna mánaðarlega, því þær eru ódýrasta merkið um bil sem þú getur lokað án verkfræðings.

**Stórfyrirtæki.** Vandinn er mikilvægi í stærð yfir mörg teymi, vörulista og mál: sameiginleg dómalistaaðferð, mat á markað og fjármögnuð mikilvægisvirkni svo hver hópur sé ekki að endurstilla BM25 frá grunni. Staðlaðu vísitöluleiðsluna, ferskleikamarkmiðin og tilraunaagann sem hliðar röðunarbreytingar og stærðarákvarðaðu sneiðingu og afritun af ásetningi frekar en vana. Vegðu smíða-á-móti-kaupa skýrt, þar sem stýrð vektorþjónusta getur skorið rekstrarkostnað á verði einhverrar stjórnar og hugsanlegrar bindingar.

**Hið opinbera.** Finnanleiki er oft lagaleg skylda og jafnréttismál: borgari sem finnur ekki rétta eyðublaðið getur ekki nýtt rétt. Kjóstu endurheimt og túlkanlega röðun svo stofnunin geti útskýrt hvers vegna niðurstaða birtist, bættu við samheitum sem brúa einföld hugtök að opinberum titlum og líttu á notkunaraðgengi og fjölmála stuðning sem kröfur frekar en aukaatriði. Innkaup ættu að vega bindingu og krefjast þess að hver stýrð þjónusta afhjúpi röðunarhegðun sína og veiti gagnaflytjanleika, og fyrirspurnir án niðurstaðna ætti að rýna sem opinbera skrá yfir óuppfyllta þörf.

## Dæmi

**Sprotafyrirtæki.** Tíu manna hugbúnaðarfyrirtæki bætir leit við þekkingargrunn þjónustuborðs síns svo viðskiptavinir geti bjargað sér sjálfir. Þeir byrja á BM25-sjálfgefnum gildum og rekast fljótt á þakið: notendur spyrja spurninga á látlausu máli sem deila engum lykilorðum með greinunum. Þeir bæta við vektorfellingum og sameina hvort tveggja með gagnkvæmum röðunarsamruna, og afleiðing batnar á einni nóttu. Til að stilla nema þeir eigin fyrirspurnaskrár, merkja nokkur hundruð pör fyrirspurna og greina og rekja smellistöðu vikulega. Þegar þeir bæta síðar við aðstoðarmanni í vörunni verður sama sóknarlagið RAG-bakendinn, svo leitarfjárfestingin borgar sig tvisvar.

**Stórfyrirtæki.** Hnattrænn smásali rekur vöruleit yfir tugi milljóna atriða yfir tugi markaða og mála. Vísitalan er sneidd fyrir stærð og afrituð fyrir gegnumstreymi, með greinum á hverju máli sem meðhöndla tilkenningu og stofnun rétt fyrir hvern markað. Flötuð leiðsögn eftir vörumerki, verði og framboði breytir risastórum niðurstöðusöfnum í leidda skoðun og sjálfvirk útfylling stýrir kaupendum að hátt umbreytandi fyrirspurnum. Mikilvægi er fjármagnað teymi með dómalista á hvern markað og samfelldar netilraunir. Röðunarbreyting fer út aðeins eftir að hún slær viðmiðunarhópinn á umbreytingu. Rauntímavísitöluleiðsla heldur verði og birgðum leitarhæfum innan sekúndna, því uppselt atriði raðað fyrst er töpuð sala og stuðningsmiði.

**Hið opinbera.** Landsbundin stofnun birtir reglugerðir, eyðublöð og leiðbeiningar sem almenningur verður að geta fundið, oft undir lagaskyldu og á skilafrestsháannaálagi. Teymið kýs endurheimt og gagnsæi: borgarar sem leita að bótum mega ekki missa af viðeigandi eyðublaði og stofnunin verður að geta útskýrt hvers vegna niðurstaða birtist, sem ýtir þeim að túlkanlegri orðbundinni röðun aukinni, varlega, með samheitum fyrir einföldu hugtökin sem fólk notar í stað opinberra titla. Notkunaraðgengi og fjölmála stuðningur eru kröfur, ekki aukaatriði. Vísitalan endurvísitölusetur án niðurtíma á bak við samnefni þegar stefnuskjöl breytast og fyrirspurnir án niðurstaðna eru skráðar og rýndar sem merki um óuppfyllta opinbera þörf.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Leit situr beint á leiðinni að verðmæti. Í verslun flæðir mælanlegur hluti tekna gegnum leitarreitinn, og notendur sem leita umbreyta á hærra hlutfalli en þeir sem bara vafra, svo fáein stig af mikilvægisbótum þýða raunverulega peninga. Í stuðningi og innri verkfærum afstýrir betri leit miðum, styttir meðhöndlunartíma og endurheimtir klukkustundirnar sem þekkingarstarfsmenn tapa í að leita að skjölum. Í opinbera geiranum er skilvirk leit þjónustugæða- og jafnréttismál: fólk sem finnur ekki rétta eyðublaðið eða leiðbeiningarnar getur ekki nýtt rétt eða uppfyllt skyldu. Þessar niðurstöður eru magnsetjanlegar, sem er einmitt ástæða þess að leit verðskuldar fjármagnað mat frekar en besta-viðleitni sjálfgefin gildi.

Heildareignarkostnaður fer langt út fyrir leyfið eða klasann. Þú borgar fyrir reikniafl og geymslu vísitölunnar og afrita hennar, fyrir fellingagerð ef þú ferð merkingarlega, fyrir vísitöluleiðsluna sem heldur henni ferskri og, mest af öllu, fyrir viðvarandi mannlega vinnu við mikilvægisstillingu og mat. Sá síðasti kostnaður er sá sem teymi vanmeta og sá sem ræður mest árangri, því leit er aldrei búin: vörulistar breytast, tungumál rekur og stilling gærdagsins rotnar. Að kaupa stýrða leitar- eða vektorþjónustu getur lækkað rekstrarkostnað og flýtt þér, á verði einhverrar stjórnar og hugsanlegrar bindingar, klassísk smíða-eða-kaupa ákvörðun til að vega gegn stærð þinni og aðgreiningu. Sterkustu viðskiptarökin binda tiltekinn mikilvægismælikvarða við tiltekna niðurstöðu, fjármagna matslykkjuna og líta á leit sem vöru sem er mæld og bætt, ekki íhlut sem er settur upp og gleymdur.

## Andmynstur og gildrur

- **Ósamræmd greining:** greinar við vísitölugerð og fyrirspurn eru ósammála, svo hugtök samsvara hljóðlega ekki og niðurstöður hverfa án villu.
- **Mikilvægi eftir skoðun:** röðun stillt af þeim sem rökræðir harðast, án dómalista, án mælikvarða og án leiðar til að grípa afturfarir.
- **Vektor-eingöngu trú:** að skipta lykilorðaleit alveg út fyrir fellingar og bregðast síðan á nákvæmum auðkennum, kóðum og sjaldgæfum hugtökum.
- **Að hunsa engar niðurstöður:** að láta tómar niðurstöðusíður standa í stað þess að slaka á, leggja til eða falla til baka, og missa notandann.
- **Úrelt vísitala:** næturlotuleiðsla sem afgreiðir verð, birgðir eða eyðingar sem notendur sjá að eru rangar.
- **Endurvísitölusetningarniðurtími:** að endurbyggja á staðnum í stað á bak við samnefni og taka leit af netinu við hverja skemabreytingu.
- **Óstillt sjálfgefin gildi að eilífu:** að afhenda BM25 beint úr kassanum og endurskoða það aldrei þegar safnið og áheyrendahópurinn þróast.
- **Engin mikilvægisfjarmæling:** að vakta töf og villur en ekki hlutfall án niðurstaðna eða smellistöðu, svo slæmar niðurstöður bregðast hljóðlega.
- **Of ákafa þensla:** að stafla samheitum og villuþoli þar til nákvæmni hrynur og hver fyrirspurn skilar hávaða.

## Þroskalíkan

- **Stig 1, Upphaf:** Leit er sjálfgefin gagnagrunnsfyrirspurn eða óstillt vél með verksmiðjustillingar, sett upp viðbragðsdrifið þegar einhver loks biður um hana. Engin mikilvægismæling, ekkert fyrirspurnarskilningslag og ferskleiki er það sem lotuverk framleiðir. Lélegar niðurstöður eru aðeins teknar eftir þegar notendur kvarta og hver lagfæring er einskiptis.
- **Stig 2, Þróun:** Raunveruleg leitarvél er til staðar með skynsamlegri greiningu, BM25-röðun og grunnflötum og sjálfvirkri útfyllingu. Sum samheiti og villuþol eru til, teymið vaktar töf og villur og er byrjað að skrá fyrirspurnir án niðurstaðna. Vinnubrögð eru mismunandi frá teymi til teymis og vöru til vöru og mikilvægi er enn stillt eftir skoðun frekar en sönnunargögnum.
- **Stig 3, Stöðlun:** Mikilvægisvinnubrögð eru skjalfest og beitt samræmt um skipulagsheildina. Teymi mæla með sameiginlegri dómalistaaðferð og NDCG utan nets og smellimælikvörðum á netinu, keyra blendings orðbundna-auk-vektor sókn þar sem hún hjálpar, halda vísitöluleiðslunni við yfirlýst ferskleikamarkmið og endurvísitölusetja án niðurtíma á bak við samnefni. Sneiðing og afritun eru stærðarákvörðuð af ásetningi og mikilvægismælikvarðar eru vaktaðir við hlið rekstrarlegra.
- **Stig 4, Stjórnun:** Leit er mæld og stýrð gegn grunnlínum. Hvert leitaryfirborð rekur NDCG-þróun, hlutfall án niðurstaðna, smellistöðu og endurmótunarhlutfall gegn umsaminni grunnlínu, með þjónustustigsmarkmiðum á fyrirspurnartafarhundraðshluta og vísitölutöf. Röðunar- og greiningarbreytingar fara út aðeins eftir að stýrð tilraun slær viðmiðið á nefndri niðurstöðu, mikilvægisafturför kallar sjálfkrafa á viðvörun og mælaborð á markað eða hluta gera hljóða rotnun sýnilega áður en notendur finna hana. Ákvarðanir um að breyta hnappi eru teknar á gögnum, með skýrum afturköllunarviðmiðum.
- **Stig 5, Samhæfing:** Leitarbætur eru samfelld, tilraunadrifin lykkja samþætt um skipulagsheildina. Dómalistar vaxa úr numdum fyrirspurnaskrám, fyrirspurnarskilningur aðlagast raunverulegu máli og sókn er stillt sem sameiginlegur grunnur fyrir niðurstraums skapandi forrit. Allt kerfið er vaktað frá enda til enda fyrir bæði hraða og mikilvægi og leitarvinnubrögðin endurjafna sig eftir því sem vörulistar, mál og líkanalandslagið reka.

## Hugmyndir til umræðu

1. Hvaða hlutfall leita þinna skilar engum niðurstöðum eða leiðir til endurmótunar og hvað leiða þessar fyrirspurnir í ljós um óuppfyllta þörf?
2. Ef þú skiptir lykilorðaleit út fyrir hreina vektorleit á morgun, hvaða fyrirspurnir myndu brotna og hvernig myndirðu vita það áður en notendur þínir gerðu það?
3. Hver á mikilvægi í skipulagsheildinni þinni og hafa þeir dómalista og mælikvarða, eða aðeins skoðanir og sögusagnir?
4. Hve löng er töfin frá breytingu í aðalgagnageymslunni þinni þar til sú breyting er leitarhæf og er það ásættanlegt fyrir hverja gagnategund?
5. Ef mállíkan neytir leitarniðurstaðna þinna, uppfyllir sóknargæði þín hærri kröfuna sem skapandi svar gerir?
6. Hvernig myndirðu verja röðunarbreytingu fyrir tortryggnum hagsmunaaðila: með tilraunaniðurstöðu eða með sögu?

## Helstu atriði

- Líttu á leit sem fyrsta flokks kerfi: afleidd vísitala með eigið gagnalíkan, leiðslu, stigvöxt og bilunarhætti, aðgreind frá aðalgagnageymslunni þinni.
- Náðu tökum á grunnatriðunum (umhverf vísitala, samræmd greining, BM25-röðun, nákvæmni gegn endurheimt) áður en þú nærð í eitthvað flóknara.
- Fjárfestu í fyrirspurnarskilningi (samheitum, villuþoli, ásetningi og raunverulegri engar-niðurstöður áætlun) því notendur skrifa aldrei eins og skjölin þín lesa.
- Hafðu blendingssókn sem sameinar orðbundna og vektorleit sem sjálfgefið og mundu að þetta sama sóknarlag er grunnur sóknarauðgaðrar myndunar.
- Skiptu skoðun út fyrir mælingu: dómalista og NDCG utan nets, smellimælikvarða og stýrðar tilraunir á netinu og mikilvægisfjarmælingu vaktaða eins og hvert annað framleiðslumerki.

## Heimildir og frekari lestur

- Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schütze, *Introduction to Information Retrieval*
- Stephen E. Robertson and Hugo Zaragoza, *The Probabilistic Relevance Framework: BM25 and Beyond*
- Ricardo Baeza-Yates and Berthier Ribeiro-Neto, *Modern Information Retrieval: The Concepts and Technology behind Search*
- Doug Turnbull and John Berryman, *Relevant Search: With Applications for Solr and Elasticsearch*
- Trey Grainger, Doug Turnbull, and Max Irwin, *AI-Powered Search*
- Patrick Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
- Jeff Johnson, Matthijs Douze, and Hervé Jégou, "Billion-Scale Similarity Search with GPUs"
- Kalervo Järvelin and Jaana Kekäläinen, "Cumulated Gain-Based Evaluation of IR Techniques"
