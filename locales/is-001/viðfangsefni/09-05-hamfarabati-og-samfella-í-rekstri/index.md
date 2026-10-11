# 9.5 Hamfarabati og samfella í rekstri

## Yfirlit og tilgangur

Fyrr eða síðar mun eitthvað sem þú áætlaðir ekki fella kerfi: rof á öllu skýjasvæði, klaufalegt `DROP TABLE`, flóð í gagnaveri, kúgunarhugbúnaðarsprenging eða birgir sem hverfur yfir nótt. Spurningin er aldrei hvort truflun berst, heldur hve hratt þú jafnar þig og hve miklu þú tapar á leiðinni. Þessi kafli fjallar um að vera tilbúinn fyrir slæma daginn áður en hann kemur.

Tveir agar svara þeim viðbúnaði og þeir eru ekki hið sama. [Samfelluáætlanagerð í rekstri](https://en.wikipedia.org/wiki/Business_continuity_planning) (BCP) heldur allri skipulagsheildinni starfandi gegnum truflun: fólki, skrifstofum, samskiptum, launagreiðslum og mikilvægu viðskiptaferlunum sem viðskiptavinir reiða sig á. [Hamfarabati](https://en.wikipedia.org/wiki/Disaster_recovery) (DR) er þrengra, tæknilega verkið að endurheimta upplýsingatæknikerfi og gögn eftir að þau bila. Samfella er markmiðið. Endurheimt er eitt af tækjunum. Þú getur endurheimt hvern þjón og samt brugðist viðskiptavinum ef enginn vissi hver mátti lýsa yfir hamförum eða hvernig á að ná til þeirra. Þessi kafli lítur á DR sem verkfræðivenju og BCP sem viðskiptarammann sem hún þjónar.

Fyrir stór teymi skalast það sem er í húfi með þér. Fyrirtæki ber eftirlitsskyldur um endurheimt, fjölsvæðafótspor og samþjöppunaráhættu hjá örfáum birgjum. Hið opinbera ber lagaskyldu til að viðhalda nauðsynlegum störfum fyrir borgara, lögfest sem rekstrarsamfella. Bæði starfa undir skoðun þar sem óprófuð áætlun er skuld sem þú uppgötvar á versta mögulega augnabliki. Endurheimt er þar sem áreiðanleiki (kafli 9.1) og atvikaviðbrögð (kafli 9.3) mæta erfiðari spurningunni um að lifa af bilanirnar sem þú getur ekki hannað í burtu.

## Meginreglur

- **Samfella er víðtækari en endurheimt.** Að endurheimta þjóna er ekki hið sama og að halda rekstrinum gangandi.
- **Tvær tölur knýja allt.** Endurheimtartímamarkmið (RTO) og endurheimtargagnamarkmið (RPO), sett út frá viðskiptaáhrifum, stærðarsetja hverja ákvörðun.
- **Óprófað afrit er ekki afrit.** Endurheimt sem þú hefur aldrei framkvæmt er von, ekki geta.
- **Gerðu ráð fyrir að afritið sé skotmark.** Kúgunarhugbúnaður leitar fyrst að afritum þínum, svo haltu eintökum óbreytanlegum og ótengdum.
- **Endurbyggðu úr kóða, ekki úr minni.** Ef þú getur ekki endurskapað innviði úr frumkóða geturðu ekki endurheimt þá áreiðanlega.
- **Kortleggðu hverju þú treystir á.** Þú endurheimtir aðeins jafn hratt og hægasta andstreymisósjálfstæði þitt.
- **Mældu endurheimt eins og hvert annað kerfi.** Raunverulegt RTO og RPO úr raunverulegum æfingum, ekki tölurnar sem þú skrifaðir á glæru.

## Ráðleggingar

### Settu RTO og RPO út frá áhrifagreiningu á rekstur

Sérhver endurheimtarákvörðun stígur af tveimur tölum, svo fáðu þær réttar fyrst. **Endurheimtartímamarkmiðið (RTO)** er hve lengi kerfi má vera niðri áður en skaðinn er óásættanlegur. **Endurheimtargagnamarkmiðið (RPO)** er hve miklum gögnum þú hefur efni á að tapa, mælt sem aldur síðasta góða eintaks sem þú getur endurheimt í. Greiðsluhöfuðbók gæti krafist RTO upp á mínútur og RPO nærri núlli. Innra greiningarmælaborð gæti þolað dag af hvoru. Þú getur ekki sett þetta í verkfræði. Leiddu þær út úr [áhrifagreiningu á rekstur](https://en.wikipedia.org/wiki/Business_impact_analysis) (BIA) sem raðar viðskiptaferlum eftir kostnaði truflunar þeirra og rekur hvert aftur til kerfanna og gagnanna sem það þarf. Þrengri markmið kosta meira, svo BIA er það sem kemur í veg fyrir að þú gullhúðir léttvæga þjónustu og vanverndir mikilvæga.

### Gerðu afrit rétt: 3-2-1 regluna, óbreytanleika og prófanir

Afrit eru gólfið undir hverri endurheimtarstefnu og flestar skipulagsheildir gera þau verr en þær halda. Fylgdu [afritunar](https://en.wikipedia.org/wiki/Backup)aganum sem kallast **3-2-1 reglan**: haltu að minnsta kosti þremur eintökum gagna þinna, á tveimur ólíkum miðlum eða kerfum, með eitt eintak á öðrum stað. Nútímaógnir bæta við tveimur kröfum til viðbótar. Haltu að minnsta kosti einu eintaki **óbreytanlegu** (skrifa-einu-sinni, óeyðanlegu yfir varðveislugluggann) og helst **ótengdu eða loftgöpuðu**, því kúgunarhugbúnaður dulkóðar eða eyðir nú viljandi afritum sem hann nær til áður en hann tilkynnir sig. Umfram allt skaltu prófa endurheimtir á áætlun. Óprófað afrit er ekki afrit, það er óprófuð forsenda, og bilanirnar sem þú finnur í æfingu (spilltar skjalasöfn, týndir dulkóðunarlyklar, afrit af röngu drifi) eru nákvæmlega þær sem hefðu bundið enda á þig í raunverulegum atburði.

### Veldu DR-stefnu eftir litrófi kostnaðar gegn hraða

DR-stefnur skipta peningum fyrir endurheimtarhraða og þú ættir að velja á kerfi út frá RTO þess og RPO frekar en að kaupa eitt þrep fyrir allt. Fjögur mynstur festa litrófið. **Afrit og endurheimt** er ódýrast og hægast: þú endurbyggir úr afritum þegar hamfarir skella á, með RTO upp á klukkustundir til daga. **Vökuljós** heldur lágmarkskjarna (gagnagrunnum í afritun, kjarnastillingum á sínum stað) volgum en niðurskölluðum, tilbúnum að víkka. **Volg biðstaða** rekur minna, alltaf-kveikt eintak af öllum staflanum sem þú skalar upp við yfirfærslu, sem skerðir RTO í mínútur. **Fjölstaða virk-virk** rekur fulla afkastagetu á tveimur eða fleiri stöðum sem þjóna lifandi umferð, sem gefur nánast núll RTO á hæsta kostnaði og flækju. Láttu þrepið samsvara tölunni sem reksturinn skrifaði undir og borgaðu ekki virk-virk verð fyrir kerfi sem þolir vökuljós.

### Afritaðu gögn með samkvæmnimálamiðlunina í huga

Endurheimtarhraði veltur á því hve núgildandi biðstöðugögn þín eru og hér erfirðu erfiðu vandamál [dreifðra kerfa](https://en.wikipedia.org/wiki/Distributed_computing) (kafli 3.3). **Samstillt afritun** staðfestir hverja skrift á öðrum stað áður en hún kvittar, sem gefur RPO nærri núlli á kostnað aukinnar skriftartafar og harðra fjarlægðarmarka. **Ósamstillt afritun** kvittar staðbundið og sendir breytingar eftir á, svo hún er hröð og landfræðilega sveigjanleg en skilur eftir afritunartafarglugga sem þú tapar við yfirfærslu. Ekkert val er ókeypis: sterkari samkvæmni kostar töf, veikari samkvæmni kostar gögn. Ákveddu á gagnageymslu út frá RPO hennar og þekktu dæmigerða afritunartöf þína, því sú töf er raunverulegt RPO þitt á slæmum degi, ekki talan í hönnunarskjalinu.

### Endurbyggðu úr kóða með innviðum sem kóða

Þú getur ekki áreiðanlega endurheimt umhverfi sem þú útvegaðir í höndunum, því enginn man hvern smell. Skilgreindu umhverfi þín sem [innviði sem kóða](https://en.wikipedia.org/wiki/Infrastructure_as_code) (kafli 8.2) svo heilan stafla megi endurskapa úr útgáfustýrðum frumkóða í þekktu góðu ástandi. Þetta breytir endurheimt úr fornleifafræðiverkefni í endurtakanlega leiðslukeyrslu, heldur biðstöðusvæði þínu heiðarlegu (það rekur minna þegar bæði eru smíðuð úr sama kóða) og gefur þér hreina leið til að setja upp endurheimtarinnviði í nýjum reikningi eða svæði eftir að hafa orðið fyrir broti. Geymdu kóðann, leyndarmálatilvísanir og keyrsluhandbækur einhvers staðar sem lifir af tap frumumhverfisins.

### Kortleggðu ósjálfstæði áður en þú þarft þau

Kerfi bila í vefjum, ekki í einangrun, og endurheimt stöðvast á ósjálfstæðinu sem þú gleymdir. Kortleggðu hverju hvert mikilvægt kerfi þarf til að virka: andstreymisþjónustum, DNS, auðkenningu og auðkenni, skírteinisyfirvöldum, skilaboðaröðum og API-um þriðja aðila og SaaS-veitum. Taktu eftir endurheimtarröðinni, því að koma forriti upp á undan gagnagrunni þess eða auðkennisveitu framleiðir bara annað rof. Gefðu ytri birgjum sérstakan gaum, þar sem endurheimt þín er takmörkuð af þeirra og þú gætir ekki haft neinn sýnileika í hana. Þessi kortlagning tengist beint seiglu og mjúkri skerðingu (kafli 3.5): því færri hörð ósjálfstæði sem kerfi hefur, því hraðar kemur það aftur.

### Prófaðu endurheimt sem venju, ekki atburð

DR-áætlun sem þú hefur ekki æft er skáldskapur. Byggðu stiga prófa. **Borðæfing** leiðir teymið gegnum sviðsmynd á pappír til að finna göt í hlutverkum, ákvörðunum og samskiptum. **Leikdagur** sprautar raunverulegri stýrðri bilun í lifandi-líkt umhverfi. **Full yfirfærsluæfing** skiptir í raun yfir á endurheimtarstaðinn og keyrir á honum. Keyrðu þetta á takti, snúðu sviðsmyndum (þar með talið tap lykilmanns eða birgis) og mældu útkomuna: fangaðu **raunverulegt RTO og RPO** sem þú náðir og berðu saman við markmið. Bilið milli mældrar og lofaðrar endurheimtar er heiðarlegasti áreiðanleikamælikvarðinn sem þú átt og að loka því er allur tilgangur æfingarinnar.

### Skipuleggðu netendurheimt sem sína eigin sviðsmynd

Kúgunarhugbúnaður og eyðileggjandi netárásir brjóta forsendur venjulegs DR, svo meðhöndlaðu þær sérstaklega. Í náttúruhamförum eru gögn þín heil annars staðar. Í [kúgunarhugbúnaðar](https://en.wikipedia.org/wiki/Ransomware)atburði eru gögn þín og oft afrit þín vopnið og endurheimtarumhverfi þitt kann sjálft að vera í hættu. Skipuleggðu **hreinherbergisendurheimt**: einangrað, traust umhverfi þar sem þú endurheimtir úr óbreytanlegum eintökum, skannar eftir innbrotinu og endurbyggir auðkenni og auðkennisgögn áður en nokkuð er tengt aftur. Vittu hvert afrit er síðasti þekkti hreini punkturinn þinn og búðu við að það að finna hann tekur réttarrannsóknartíma sem venjulegt RTO þitt fjárhagsáætlaði aldrei. Þetta er þar sem óbreytanleg, ótengd eintök vinna sér inn kostnað sinn og það tengist þétt atvikastjórnun (kafli 9.3) og reglufylgni- og stjórnarháttaskyldum um brotameðhöndlun (kafli 4.6).

## Málamiðlanir: kostir og gallar

| DR-stefna | Kostir | Gallar |
|---|---|---|
| Afrit og endurheimt | Ódýrast, einfalt, lágur viðvarandi kostnaður | Hægt RTO (klukkustundir til dagar). Stærra RPO |
| Vökuljós | Lágur kostnaður. Kjarnagögn volg og tilbúin | Handvirk uppskölun. Endurheimt tekur enn raunverulegan tíma |
| Volg biðstaða | Hratt RTO (mínútur). Fullur stafli sannaður | Viðvarandi kostnaður keyrandi öðru umhverfi |
| Fjölstaða virk-virk | Nánast núll RTO. Engin eins-staðar bilun | Hæsti kostnaður og flækja. Samkvæmni er erfið |
| Samstillt afritun | RPO nærri núlli | Skriftartöf. Fjarlægðartakmörkuð. Þéttari tenging |
| Ósamstillt afritun | Hröð, sveigjanleg, landfræðilega frjáls | Gagnatapsgluggi jafn afritunartöf |

Kjarnaspennan er að endurheimtarhraði og gagnaferskleiki kosta báðir peninga og flækju og hvorugt er ókeypis á nokkru þrepi. Leystu það á kerfi frekar en á skipulagsheild: láttu áhrifagreininguna úthluta hverju mikilvægu kerfi RTO og RPO, keyptu síðan nákvæmlega stefnuna sem mætir því. Að eyða virk-virk peningum á skýrslutól sveltir höfuðbókina sem þurfti þá og öfugt er vanræksla. Aginn er að láta útgjöld samsvara tölunni sem reksturinn á og endurskoða þá samsvörun eftir því sem mikilvægi kerfa breytist.

## Spurningar til að ræða með teyminu

1. **Hver eru RTO og RPO fyrir hvert mikilvægt kerfi ykkar og hver í rekstrinum skrifaði undir þau?** Ef verkfræði fann þessar tölur upp ein eru þær ágiskanir og ágiskanir eru fjármagnaðar annaðhvort of rausnarlega eða alls ekki. Endurheimtartíma- og endurheimtargagnamarkmiðin ættu að falla út úr áhrifagreiningu á rekstur sem raðar ferlum eftir kostnaði truflunar þeirra, svo höfuðbókin fái mínútur og innra wiki fái dag. Komdu með núverandi þrepaskiptingu og spyrðu hvort sá sem ber ábyrgð á hverju viðskiptaferli myndi í raun sætta sig við gagnatapið og niðurtímann sem þú hefur hannað fyrir. Í stórri skipulagsheild er þetta samtal það sem kemur í veg fyrir dýru mistökin að vernda allt jafnt, sem verndar ekkert vel. Ef enginn utan verkfræði getur nefnt tölurnar hefurðu ekki enn markmið, þú hefur vonir.

2. **Hvenær framkvæmduð þið síðast raunverulega endurheimt og mælduð þið raunverulegt RTO og RPO sem þið náðuð?** Afrit sem þú hefur aldrei endurheimt er óprófuð forsenda og bilunarhættirnir sem drepa þig (spilltar skjalasöfn, týndir dulkóðunarlyklar, skyndimynd af röngu drifi, ósjálfstæði sem kemur ekki upp) koma aðeins fram þegar þú reynir. Komdu með dagsetningu og niðurstöðu síðustu fullu yfirfærsluæfingar ykkar, ekki síðustu borðæfingar, og bilið milli endurheimtarinnar sem þið náðuð og endurheimtarinnar sem þið lofuðuð. Fyrir stórt teymi sannar ein vel heppnuð endurheimt eins kerfis ekki hin, svo spyrðu hve hátt hlutfall mikilvægra kerfa hefur verið endurheimt frá enda til enda síðasta árið. Mælda bilið er heiðarlegasta áreiðanleikatalan ykkar og ef þið getið ekki nefnt hana er áætlun ykkar skáldskapur þar til sannað er annað.

3. **Ef kúgunarhugbúnaður dulkóðaði framleiðsluna ykkar og næði til afrita ykkar í nótt, hvert er síðasta þekkta hreina eintakið og hvar myndið þið endurbyggja?** Venjulegt hamfarabati gerir ráð fyrir að gögn ykkar séu örugg annars staðar og eyðileggjandi netárás brýtur nákvæmlega þá forsendu með því að gera gögn ykkar og afrit að vopninu. Spyrðu hvort að minnsta kosti eitt afritseintak sé óbreytanlegt og ótengt, hvernig þið mynduð auðkenna síðasta hreina endurheimtarpunktinn og hvaðan traust hreinherbergisumhverfi kæmi þegar framleiðslan sjálf er í hættu. Þessi sviðsmynd þarf réttarrannsóknartíma sem venjulegt RTO ykkar fjárhagsáætlaði aldrei, svo komdu með heiðarlegt mat á því hve lengi það tekur í raun að finna hreinan punkt. Fyrir fyrirtækja- og opinber teymi er þetta líka reglufylgniatburður (kafli 4.6) með brotatilkynningarklukkur í gangi samhliða. Ef svarið er „við myndum endurheimta nýjasta afritið“ hafið þið alls ekki skipulagt þetta.

4. **Hvert kerfa ykkar borgar fyrir endurheimtarþrep sem áhrifagreining þess á rekstur réttlætir ekki og hvert er hættulega vanverndað?** Endurheimtarhraði og gagnaferskleiki kosta báðir peninga á hverju þrepi, svo almenn stefna annaðhvort sóar virk-virk fjárhagsáætlun á skýrslutól eða sveltir höfuðbókina sem raunverulega þurfti hana. Togið á móti er raunverulegt: eitt staðalþrep er langtum einfaldara fyrir mörg teymi að reka, á meðan þrepaskipting á kerfi parar útgjöld við gildi en krefst viðvarandi umönnunar eftir því sem mikilvægi kerfis færist. Komdu með núverandi DR-stefnu fyrir hvert mikilvægt kerfi, RTO og RPO sem hún miðar að, mánaðarkostnað biðstöðu hennar og afritunar og dagsetninguna þegar þrepaskiptingin var síðast endurskoðuð gegn ferskri áhrifagreiningu. Í fyrirtækja- eða opinberu umhverfi margfaldast ósamsvarandi þrep yfir svæði og úttekt mun biðja þig að réttlæta bæði peningana sem þú eyðir og útsetninguna sem þú sættir þig við, svo óútskýrður virk-virk reikningur og óvarin mikilvæg þjónusta eru jafn erfið að verja.

5. **Þekkið þið í raun endurheimtarröð mikilvægra kerfa ykkar og hversu langt endurheimt ykkar veltur á birgjum sem þið getið ekki prófað?** Kerfi bila í vefjum, ekki í einangrun, og endurheimt stöðvast á ósjálfstæðinu sem enginn kortlagði: komdu forriti upp á undan gagnagrunni þess, auðkennisveitu eða DNS og þú framleiðir einfaldlega annað rof. Að kortleggja ósjálfstæði er leiðinlegt og kortið úreldist, en valkosturinn er að uppgötva endurheimtarröðina í beinni við yfirfærslu og samþjöppunaráhætta hjá örfáum SaaS-veitum er ósýnileg þar til þær bila saman og takmarka endurheimt ykkar við þeirra. Komdu með núverandi ósjálfstæðakort, skjalfesta endurheimtarröð og lista yfir ytri birgja með yfirlýstum endurheimtarskuldbindingum þeirra og hvort þið hafið nokkru sinni staðfest einhverja. Fyrir stóra eða opinbera skipulagsheild eru samfella birgja og samþjöppunaráhætta í auknum mæli innkaupa- og eftirlitsáhyggjuefni, svo þær endurheimtarskyldur eiga heima í samningnum á formi sem þið getið úttektað frekar en í markaðsefni seljanda.

6. **Ef þið endurheimtuð hvern þjón í nótt, myndi reksturinn í raun halda áfram og hver hefur heimild til að lýsa yfir hamförum?** Hamfarabati endurheimtir upplýsingatækni, en rekstrarsamfella heldur skipulagsheildinni starfandi: fólki, samskiptum, launagreiðslum og ákvörðunum sem velta á því að einhver hafi vald til að taka þær. Þú getur endurheimt hvert kerfi og samt brugðist viðskiptavinum ef enginn vissi hver gæti lýst yfir hamförum eða hvernig á að ná til starfsfólks þegar venjulegar rásir eru líka niðri. Verkfræði á endurheimt, en samfella spannar aðstöðu, mannauð, samskipti og arftakaröð forystu og þessi samskeyti milli deilda eru nákvæmlega þar sem áætlun rotnar hljóðlega. Komdu með yfirlýsingarvaldið og stigmögnunarkeðjuna, varasamskiptaáætlunina, nefnda arftaka og varaaðstöðu og dagsetninguna þegar viðskiptahliðin (ekki bara upplýsingatækni) æfði áætlunina síðast. Hið opinbera ber lagalega rekstrarsamfelluskyldu með nefndum arftökum og nauðsynlegum störfum og fyrirtæki standa frammi fyrir eftirlitsskyldum um samfellu, svo bæði eru dæmd eftir því hvort reksturinn lifir slæma daginn af, ekki bara þjónarnir.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með örlítið teymi og lítið svigrúm hefurðu ekki efni á heitu öðru svæði, svo vertu yfirvegaður um ódýru hlutana sem samt bjarga þér. Settu eitt heiðarlegt endurheimtarþrep, fylgdu 3-2-1 reglunni með sjálfvirkum skyndimyndum og að minnsta kosti einu óbreytanlegu eintaki sem eigin stjórnendur þínir geta ekki eytt og hafðu allt umhverfið sem innviði sem kóða svo þú getir endurbyggt úr frumkóða. Slepptu íburðarmikilli áætlun og keyrðu í staðinn eina raunverulega endurheimt í tilraunaumhverfi ársfjórðungslega, því ein tímasett æfing kennir þér meira en mappa sem enginn les.

**Lítið fyrirtæki.** Án sérstaks samfellusérfræðings og með þröngt fjárhagsáætlun skaltu líta á endurheimt sem eitthvað sem þú kaupir frekar en smíðar. Hallaðu þér að stýrðu afriti, skyndimyndum og þversvæðaafritun skýjaveitunnar frekar en að setja upp sérsmíðaða DR-innviði og veldu söluaðila þar sem afrit eru óbreytanleg og þú getur sjálfur keyrt endurheimtarferlið. Rammaðu allt verkefnið í kringum tvær spurningar sem þú getur svarað án sérfræðings: hve miklum gögnum getum við tapað og hve lengi getum við verið niðri, og sannaðu að ein endurheimt virki áður en þú treystir henni.

**Stórfyrirtæki.** Í stærð er vandinn eignasafnsstjórnarhættir yfir mörg teymi: áhrifagreining á rekstur sem úthlutar hverri þjónustu RTO og RPO, endurheimtarstefnur þrepaskiptar frá afriti-og-endurheimt upp í virk-virk og miðlæg sýn á andstreymis- og birgjaósjálfstæði þar með talda samþjöppunaráhættu. Fjárhagsáætlaðu biðstöðu-, afritunar- og óbreytanlegu eintakakostnað skýrt, keyrðu yfirfærslur vottaðar af eftirlitsaðila á takti og mældu raunverulega endurheimt gegn markmiði sem rakinn áreiðanleikamælikvarða. Haltu netendurheimt sem eigin áætlun með óbreytanlegum hvelfingareintökum og hreinherbergiskeyrsluhandbók, prófuð óháð náttúruhamfaraæfingunum.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta hvert val og samfella er oft lagaleg skylda frekar en val. Byggðu rekstrarsamfelluáætlun sem auðkennir nauðsynleg störf, raðar endurheimt þeirra og nefnir arftaka og varaaðstöðu svo ákvarðanir stöðvist aldrei vegna skorts á heimilaðri manneskju og samræmdu hana viðurkenndri leiðsögn eins og NIST SP 800-34 til stuðnings FISMA-skyldum. Haltu loftgöpuðum afritseintökum, skilgreindu innviði sem kóða til endurbyggingar á varasvæði og keyrðu árlega fulla æfingu auk borðæfinga fyrir kúgunarhugbúnað þar sem mældar niðurstöður eru skýrðar eftirlitsaðilum sem sönnunargögn um að nauðsynleg þjónusta lifi af.

## Dæmi

**Sprotafyrirtæki.** Tólf manna SaaS-fyrirtæki hefur ekki efni á heitu öðru svæði, svo það er yfirvegað um ódýru hlutana. Það setur eitt heiðarlegt þrep: RTO upp á fjórar klukkustundir, RPO upp á fimmtán mínútur fyrir viðskiptavinagagnagrunninn. Það fylgir 3-2-1 reglunni með sjálfvirkum skyndimyndum, einu eintaki afrituðu á annað skýjasvæði og einu óbreytanlegu eintaki með læstum varðveisluglugga sem eigin stjórnendur þess geta ekki eytt. Allt umhverfið er innviðir sem kóði (kafli 8.2), svo það getur sett upp ferskan stafla úr frumkóða. Einu sinni á ársfjórðungi keyrir það raunverulega endurheimt í tilraunaumhverfi á föstudagseftirmiðdegi, tímasetur hana og skilar stuttri athugasemd. Fyrsta æfingin tók níu klukkustundir og fann vantandi flutningsskref. Lagfæringin er ástæða þess að sú næsta tók þrjár.

**Stórfyrirtæki.** Fjölþjóðlegur banki starfar undir eftirlitskröfum um endurheimt sem skylda prófaða samfellu fyrir mikilvæga þjónustu. Hann rekur volga biðstöðu á öðru svæði fyrir kjarnabankakerfi sitt, með samstilltri afritun innan stórborgarpars fyrir nánast núll RPO og ósamstilltri afritun á fjarlægt svæði til að lifa af svæðishamfarir. Áhrifagreining á rekstur úthlutar hverri þjónustu RTO og RPO og miðlægt teymi kortleggur andstreymisósjálfstæði þar með talda tvo SaaS-veitendur merkta sem samþjöppunaráhættu. Tvisvar á ári framkvæmir hann fulla yfirfærslu vottaða af eftirlitsaðila, mælir raunverulegt gegn markmiði og færir götin inn í næstu lotu. Sérstök netendurheimtaráætlun heldur óbreytanlegum hvelfingareintökum og hreinherbergiskeyrsluhandbók, prófuð óháð náttúruhamfaraæfingunum.

**Hið opinbera.** Landsbundin stofnun sem afhendir bætur rekur rekstrarsamfelluáætlun (COOP) byggða til að viðhalda nauðsynlegum störfum sínum í hvaða truflun sem er. Samkvæmt [rekstrarsamfellu](https://en.wikipedia.org/wiki/Continuity_of_Operations) venju og NIST SP 800-34 viðbragðsáætlunarleiðsögninni sem styður FISMA-skyldur hennar auðkennir hún nauðsynleg störf, raðar endurheimt þeirra og nefnir arftaka og varaaðstöðu svo ákvarðanir stöðvist aldrei vegna skorts á heimilaðri manneskju. Borgarasnúin kerfi bera skjalfest RTO og RPO, afrit fylgja 3-2-1 reglunni með loftgöpuðum eintökum og innviðir eru skilgreindir sem kóði til endurbyggingar á varasvæði. Árleg full æfing, auk borðæfinga fyrir kúgunarhugbúnaðarsviðsmynd, prófar áætlunina gegn mældri endurheimt og niðurstöðurnar eru skýrðar eftirlitsaðilum sem sönnunargögn um að nauðsynleg þjónusta lifi slæma daginn af.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun DR og samfellu er forðuð stórslys, sem er sannarlega erfitt að verðmeta þar til þú þarft þess og sársaukafullt áþreifanlegt þegar þú gerir það. Rammaðu það sem áhættustýringu: væntur kostnaður truflunar er líkindi hennar sinnum áhrif og áhrif fyrir stóra skipulagsheild spanna frá glötuðum tekjum á klukkustund af niðurtíma gegnum eftirlitsviðurlög, brotatilkynningarkostnað og orðsporsskaðann sem lifir lengur en rofið. Einn óendurheimtanlegur kúgunarhugbúnaðaratburður hefur bundið enda á fyrirtæki og, í opinbera geiranum, tekið nauðsynlega borgaraþjónustu úr sambandi vikum saman. Gegn því er kostnaður prófaðrar endurheimtargetu hóflegur og þekkjanlegur.

Heildareignarkostnaður (TCO) er raunverulegur og viðvarandi: biðstöðuinnviðir, afritunarbandbreidd, afritageymsla (margfölduð af óbreytanlegum og ótengdum eintökum) og verkfræðitími til að smíða sjálfvirkni og keyra æfingar. Þetta er nákvæmlega ástæða þess að þú þrepaskiptir eftir RTO og RPO í stað þess að kaupa virk-virk alls staðar, svo útgjöld fylgi gildi hvers kerfis frekar en almennri stefnu. Til að færa rök við forystu skaltu þýða áætlunina á þeirra mál: hér er niðurtíminn og gagnatapið sem við getum lifað af í dag, hér er bilið að markmiðum okkar, hér er hvað það kostar að loka því og hér er útsetningin ef við gerum það ekki. Sannfærandi gripurinn er mæld æfing, því endurheimt sem þú hefur sýnt fram á er tala sem forysta getur treyst og óprófuð áætlun er skuld dulbúin sem eign.

## Andmynstur og gildrur

- **Óprófuð afrit.** Endurheimt sem þú hefur aldrei framkvæmt er von. Æfingin er þar sem þú finnur spillinguna, týnda lykilinn og ranga drifið.
- **Afrit aðgengileg úr framleiðslu.** Ef kúgunarhugbúnaður getur dulkóðað eða eytt afritum þínum hefurðu eitt eintak, ekki þrjú. Haltu einu óbreytanlegu og ótengdu.
- **Eitt RTO og RPO fyrir allt.** Almenn þrep ofvernda hið léttvæga og vanvernda hið mikilvæga. Þrepaskiptu út frá áhrifagreiningu á rekstur.
- **Að rugla DR við BCP.** Að endurheimta hvern þjón á meðan enginn veit hver lýsir yfir hamförum eða hvernig á að ná til starfsfólks er endurheimt kerfi og misheppnaður rekstur.
- **Handsmíðuð endurheimtarumhverfi.** Innviðir sem þú getur ekki endurbyggt úr kóða reka og rek uppgötvast mitt í yfirfærslu.
- **Hunsuð ósjálfstæði.** Að endurheimta forrit á undan gagnagrunni þess, auðkennisveitu eða DNS framleiðir bara annað rof.
- **Áætlunarrotnun.** Mappa skrifuð einu sinni og aldrei æfð lýsir kerfi sem er ekki lengur til.
- **Blindir blettir birgja.** Endurheimt þín er takmörkuð af endurheimt mikilvægu birgja þinna og samþjöppunaráhætta er ósýnileg þar til þeir bila saman.

## Þroskalíkan

- **Stig 1, Upphaf:** Endurheimt er ad hoc og viðbragðsdrifin. Afrit kunna að keyra en endurheimtir eru óprófaðar. Engin samþykkt RTO eða RPO, engin áhrifagreining á rekstur og endurheimt er spunnin í atvikinu. Alvarlegt gagnatap eða kúgunarhugbúnaðaratburður yrði líklega óendurheimtanlegur.
- **Stig 2, Þróun:** Grunnvinnubrögð eru til en ósamræmd yfir teymi. Sum mikilvæg kerfi hafa afrit sem fylgja 3-2-1 reglunni og skjalfest RTO og RPO fyrir mikilvægustu þjónusturnar og grunn-DR-áætlun er til með endurheimtir prófaðar stöku sinnum. Þekja er að hluta, ósjálfstæði eru ekki kortlögð, æfingar eru ad hoc og agi eins teymis felur ekki í sér agann hjá því næsta.
- **Stig 3, Stöðlun:** Endurheimtarvenjur eru skjalfestar og framfylgdar um skipulagsheildina. Áhrifagreining á rekstur knýr þrepaskipt RTO og RPO yfir kerfi, endurheimtarstefnur eru paraðar við þau þrep, umhverfi eru innviðir sem kóði, ósjálfstæði og endurheimtarröð eru kortlögð og tímasettar æfingar (borðæfing, leikdagur og yfirfærsla) keyra á skilgreindum takti. Netendurheimtaráætlun með óbreytanlegum, ótengdum eintökum er skjalfest og beitt samræmt frekar en látin einstökum teymum eftir.
- **Stig 4, Stjórnun:** Endurheimt er mæld og stýrð gegn grunnlínum. Hver æfing fangar raunverulegt RTO og RPO sem náðist og rekur bilið að markmiði og mælikvarðar eins og endurheimtarárangurshlutfall, hlutfall mikilvægra kerfa endurheimt frá enda til enda á síðasta ári, afritaþekja og óbreytanleiki og vöktuð afritunartöf sem raunverulegt RPO eru skýrðir á mælaborðum. Frávik ræsa aðgerð, þrepaskipting er leidd út aftur úr gögnum um hvernig kerfi eru í raun notuð og ákvarðanir um fara eða ekki hvíla á sönnunargögnum frekar en tölunum sem skrifaðar eru á glæru.
- **Stig 5, Samhæfing:** Endurheimt er stöðugt bætt, samþætt um skipulagsheildina og aðlögunarhæf. Yfirfærsla og hreinherbergisendurheimtir netárása eru æfðar sem rútína, birgja- og samþjöppunaráhætta er virkt stýrt og samfella er samþætt áreiðanleika (kafli 9.1) og atvikaviðbrögðum (kafli 9.3) svo skipulagsheildin endurheimti fyrirsjáanlega eftir bilunum sem hún hefur aldrei séð og endurmarki endurheimtarstöðu sína eftir því sem kerfalandslagið og ógnamyndin breytast.

## Hugmyndir til umræðu

1. Hvert mikilvægra kerfa ykkar hefur aldrei verið endurheimt frá enda til enda og hvað þyrfti til að sanna að hægt sé?
2. Ef þið misstuð aðalskýjasvæði ykkar í heilan dag, hvaða viðskiptaferli stöðvast og í hvaða röð mynduð þið koma kerfum aftur?
3. Hve mikið af endurheimt ykkar veltur á birgjum sem þið getið ekki séð eða prófað endurheimt hjá?
4. Hvar borgið þið fyrir endurheimtarþrep sem áhrifagreining á rekstur réttlætir ekki og hvar vanverndið þið?
5. Ef afrit ykkar væru aðgengileg og dulkóðuð í nótt, hver er raunverulegur síðasti þekkti hreini endurheimtarpunktur ykkar?
6. Hvert er heiðarlegt bil milli lofaðs RTO og RPO og þeirra sem síðasta æfing ykkar náði í raun?

## Helstu atriði

- **Samfella er markmiðið. Endurheimt er tæki.** Samfelluáætlanagerð í rekstri heldur skipulagsheildinni starfandi. Hamfarabati endurheimtir upplýsingatæknikerfin sem hún treystir á.
- **RTO og RPO knýja allt** og bæði koma frá áhrifagreiningu á rekstur, ekki verkfræðiágiskun. Þrepaskiptu kerfi frekar en að vernda öll jafnt.
- **Óprófað afrit er ekki afrit.** Fylgdu 3-2-1 reglunni, haltu að minnsta kosti einu óbreytanlegu og ótengdu eintaki gegn kúgunarhugbúnaði og prófaðu endurheimtir á áætlun.
- **Láttu DR-stefnuna samsvara tölunni:** afrit-og-endurheimt, vökuljós, volg biðstaða eða virk-virk, valið eftir RTO og RPO hvers kerfis.
- **Afritun skiptir samkvæmni fyrir ferskleika** (kafli 3.3). Raunverulegt RPO þitt er afritunartöf þín, ekki hönnunarskjalið.
- **Endurbyggðu úr kóða** með innviðum sem kóða (kafli 8.2) og kortleggðu ósjálfstæði áður en þú þarft þau.
- **Prófaðu með borðæfingum, leikdögum og fullum yfirfærsluæfingum** og mældu raunverulegt RTO og RPO á móti markmiðum RTO og RPO.
- **Skipuleggðu netendurheimt sérstaklega** með hreinherbergisendurheimt og tengdu alla venjuna við áreiðanleika (kafli 9.1), atvikaviðbrögð (kafli 9.3) og reglufylgni (kafli 4.6).

## Heimildir og frekari lestur

- ISO 22301, *Security and resilience: Business continuity management systems: Requirements* (the international standard for BCP).
- National Institute of Standards and Technology, *SP 800-34 Rev. 1: Contingency Planning Guide for Federal Information Systems* (RTO, RPO, and recovery strategies for government systems).
- National Institute of Standards and Technology, *SP 800-61 Rev. 2: Computer Security Incident Handling Guide* (incident and cyber-recovery handling).
- U.S. Federal Emergency Management Agency, *Continuity Guidance Circular* and federal COOP guidance (essential functions and continuity of operations).
- Federal Financial Institutions Examination Council (FFIEC), *Business Continuity Management* booklet (regulatory recovery expectations for financial institutions).
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy, eds., *Site Reliability Engineering: How Google Runs Production Systems* (reliability and disaster testing).
- Kelly Shortridge and Aaron Rinehart, *Security Chaos Engineering* (deliberately exercising failure and recovery).
- Cybersecurity and Infrastructure Security Agency (CISA), *#StopRansomware Guide* (ransomware prevention and recovery practice).
