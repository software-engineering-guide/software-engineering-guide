# 2.8 Hugbúnaðarkröfur

## Yfirlit og tilgangur

[Hugbúnaðarkrafa](https://en.wikipedia.org/wiki/Software_requirements) er yfirlýsing um getu eða skilyrði sem kerfi verður að veita, fullnægja eða búa yfir til að vera ásættanlegt fyrir hagsmunaaðila sína. [Kröfuverkfræði](https://en.wikipedia.org/wiki/Requirements_engineering), agaða vinnan við að draga fram, greina, tilgreina, staðfesta og stýra þessum yfirlýsingum, situr fremst í virðiskeðjunni. Allt neðar, frá arkitektúr til kóða til [samþykkisprófana](https://en.wikipedia.org/wiki/Acceptance_testing), er tilraun til að fullnægja kröfum. Þegar kröfur eru rangar, ófullkomnar eða tvíræðar er því öll fyrirhöfnin sem fer í að smíða rangan hlut rétt hrein sóun, og dýrasta sóun sem til er, því þú uppgötvar hana síðast. Þekkingarsvið [Software Engineering Body of Knowledge](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) (SWEBOK) um hugbúnaðarkröfur lítur á þetta sem raunverulega verkfræðigrein, ekki skrifstofulegan formála að raunverulegu verki.

Fyrir stór teymi eru kröfur sameiginlegi skilningurinn sem lætur marga smíða eitt samhangandi kerfi. Einn hönnuður getur haldið ásetningnum í höfðinu. Hundruð manna yfir mörg teymi geta það ekki. Kröfur verða samningurinn milli þeirra sem þurfa getu og þeirra sem smíða hana, grundvöllur til að skipta vinnu milli teyma og mælistikan til að dæma hvenær eitthvað er „búið“. Þær tengjast beint uppgötvun (kafli 11.1), þar sem vandamál og tækifæri birtast, grunni notendaupplifunar (kafli 5.1), þar sem þú skilur þarfir notenda, API og viðmótshönnun (kafli 2.3), þar sem viðmótsskyldur eru festar, arkitektúr og gæðaeiginleikum (kafli 3.1), þar sem ófallbundnar kröfur móta uppbyggingu, og verkefnastjórnun (kafli 10.6), þar sem umfang, kostnaður og tímaáætlun er skipulögð í kringum þær.

Í fyrirtækja- og opinberu umhverfi bera kröfur laga-, samnings- og öryggisvægi. Eftirlitsskylt kerfi þarf að sýna að sérhver skyldubundin skylda (aðgengi, persónuvernd, öryggi, skjalavarðveisla, fjárhagsstýring) sé fönguð sem krafa, útfærð og staðfest með sönnunargögnum. Opinber innkaup eru oft byggð í kringum kröfulýsingu, og greiðsla, úttekt og vottun velta öll á því að rekja hverja kröfu til sönnunargagna um að henni hafi verið fullnægt. Hér eru kröfur meira en góð venja: þær eru burðarás ábyrgðar.

## Meginreglur

- Krafa tjáir þörf eða skorðu, ekki lausn. Hún segir hvað og hvers vegna, ekki hvernig.
- Sérhver krafa verður að vera nauðsynleg, ótvíræð, sannprófanleg, framkvæmanleg og rekjanleg.
- Kröfur eru dregnar fram og samið um þær við hagsmunaaðila, ekki fundnar upp í einangrun.
- Ófallbundnar kröfur og skorður móta arkitektúr jafn mikið og virkni.
- Kröfur þróast. Stýrðu breytingum af ásetningi frekar en að frysta þær eða hunsa.
- Rekjanleiki, frá þörf til kröfu til hönnunar til prófs til sönnunar, er bindivefur ábyrgðar.
- Rétt formfesta veltur á áhættu, stærð og regluverkssamhengi, ekki vana.

## Ráðleggingar

### Skilgreindu kröfur skýrt og flokkaðu þær

Nefndu flokkana af ásetningi. **[Fallbundnar kröfur](https://en.wikipedia.org/wiki/Functional_requirement)** segja hvað kerfið verður að gera: hegðunina, umbreytingarnar og þjónusturnar sem það veitir. **[Ófallbundnar kröfur](https://en.wikipedia.org/wiki/Non-functional_requirement)** (gæðaeiginleikar) segja hve vel það verður að gera þær: afköst, tiltækileiki, öryggi, nothæfi, aðgengi, viðhaldanleiki og fleira. Þær binda sig þétt við arkitektúr (kafli 3.1). **Skorður** eru óumsemjanlegu mörkin á lausnina: skyldaðar tæknir, staðlar, fjárhagsáætlanir, lagareglur eða viðmót við núverandi kerfi. Og aðskildu **viðskiptakröfur** (hvers vegna skipulagsheildin vill kerfið) frá **notendakröfum** (hvað notendur þurfa að ná fram) frá **kerfiskröfum** (hvað hugbúnaðurinn verður því að gera). Blandaðu þessum stigum saman og umfangsrugl fylgir fljótt.

### Dragðu fram úr raunverulegum uppsprettum, ekki forsendum

Útdráttur er virk uppgötvun. Dragðu kröfur frá hagsmunaaðilum gegnum viðtöl, vinnustofur, athugun, [frumgerðir](https://en.wikipedia.org/wiki/Software_prototyping) og greiningu á núverandi kerfum og skjölum. Finndu hvern viðeigandi hagsmunaaðila, líka þá sem auðvelt er að yfirsjást: rekstraraðila, endurskoðendur, stuðningsfólk og fólk sem kerfið snertir en notar aldrei beint. Tengdu útdráttinn við uppgötvunarleiðsluna (kafli 11.1) og notendaupplifunarrannsóknir (kafli 5.1), svo yfirlýstar óskir rekjist aftur til undirliggjandi þarfa. Skráðu uppsprettu og rök hverrar kröfu, því að vita hvers vegna krafa er til er einmitt það sem leyfir þér að breyta henni örugglega síðar.

### Greindu, semdu og forgangsraðaðu

Hrár útdreginn þarfir stangast á, skarast og leggjast saman í meira en er framkvæmanlegt. Greining er hvernig þú sættir þær: flokkar kröfur, kemur auga á árekstra, vegur framkvæmanleika og áhættu og semur um forgangsröðun við hagsmunaaðila. Forgangsraðaðu fyrir opnum tjöldum, til dæmis með verður/ætti/gæti-greiningu eða virði-á-móti-kostnaði röðun, svo þegar tími þrýtur skerðu rétt umfang. Og mótaðu kröfurnar hvar sem líkan bætir við skýrleika: ferlaflæði, ástandsrit, gagnalíkön og viðmótsskilgreiningar draga fram göt sem prósi felur.

### Tilgreindu á réttu formfestustigi

Skrifaðu kröfur niður á formi sem passar áhættunni og áhorfendunum. Opinbert kerfi með mikilli tryggingu getur réttlætt formlega tilgreiningu skipulagða samkvæmt staðli eins og IEEE 29148. Hraðfara vöruteymi getur fangað kröfur sem [notendasögur](https://en.wikipedia.org/wiki/User_story) með samþykkisviðmiðum í verkefnalista. Hvort sem er ætti hver krafa að vera frumeindaleg, sannprófanleg og laus við sleipt orðalag eins og „hratt“, „notendavænt“ eða „o.s.frv.“. Festu samþykkisviðmið við, svo þú skilgreinir hvernig á að sannprófa kröfu á sama augnabliki og þú skrifar hana. Og haltu einni valdbærri uppsprettu í stað þess að láta kröfur dreifast yfir tölvupósta, miða og glærur.

### Staðfestu áður en þú smíðar

Staðfesting sannreynir að kröfurnar sem þú hefur tilgreint séu hinar réttu og hangi saman. Rýndu þær með hagsmunaaðilum, farðu í gegnum sviðsmyndir og, þar sem þú getur, notaðu frumgerðir til að gera óhlutbundnar yfirlýsingar áþreifanlegar. Staðfesting er ódýrari en nokkur síðari leiðrétting: galli gripinn í kröfurýni kostar brot af sama galla gripnum í framleiðslu.

### Stýrðu kröfum og haltu rekjanleika

Kröfur breytast. Verk þitt er að stýra þeirri breytingu, ekki standa gegn henni. Settu upp breytingaferli: vegðu hverja fyrirhugaða breytingu fyrir áhrif, kostnað og áhrif neðar áður en þú samþykkir hana. Settu grunnlínu á kröfur á samþykktum punktum og útgáfustýrðu þær. Haltu **[tvístefnu rekjanleika](https://en.wikipedia.org/wiki/Requirements_traceability)** sem tengir hverja kröfu fram á við til hönnunar, kóða og prófa, og aftur á við til þarfarinnar sem hún kom frá. Rekjanleiki svarar spurningunum tveimur sem stór teymi lifa eftir: ef þessi þörf breytist, hvað hefur það áhrif á, og fyrir þennan afhenta eiginleika, hvaða þörf réttlætti hann? Í eftirlitsskyldu samhengi skaltu framlengja slóðina alla leið til samþykkissönnunar (prófaniðurstaðna, úttektarskráa, undirskrifta) svo þú getir sýnt fram á regluvörslu en ekki bara fullyrt hana.

### Lagaðu að lipru og áætlanadrifnu samhengi

Í áætlanadrifnum og eftirlitsskyldum áætlunum tilgreinirðu og setur grunnlínu á kröfur nokkuð snemma, með formlegri breytingastýringu. Í lipru samhengi lifa kröfur sem forgangsraðaður, þróandi verkefnalisti, útfærður rétt fyrir innleiðingu og staðfestur stöðugt gegnum virkan hugbúnað. Undirliggjandi athafnir eru þær sömu í báðum. Aðeins tímasetning, formfesta og afurðir eru ólík. Stórar skipulagsheildir blanda oft þessu tvennu: þær tilgreina og rekja stöðugar, háa-tryggingar skyldur formlega, á meðan þær útfæra vöruhegðun endurtekið. Veldu jafnvægið eftir áhættu, ekki hugmyndafræði.

## Málamiðlanir: kostir og gallar

| Nálgun | Best fyrir | Kostir | Gallar |
|---|---|---|---|
| Formleg tilgreining fyrirfram | Há-tryggingar, eftirlitsskyld, föst-umfangs samningar | Sterkur rekjanleiki, skýr samþykkisgrundvöllur, úttektarhæf | Hæg að breyta, hætta á ofurtilgreiningu áður en lært er |
| Lipur verkefnalisti | Þróandi vörur með þátttakandi hagsmunaaðilum | Hröð endurgjöf, aðlagast námi, minni sóun á ósmíðuðu umfangi | Veikari langdrægur rekjanleiki, erfiðara að úttekta og semja um |
| Blendingur (formlegar skorður + lipur hegðun) | Fyrirtæki með blandaðar skyldur | Nákvæmni þar sem það skiptir máli, sveigjanleiki annars staðar | Krefst dómgreindar um hvaða hlutar eru hverjir |

Meginspennan er milli stöðugleika og náms. Að festa kröfur snemma kaupir þér fastan samþykkisgrundvöll og úttektarhæfi, en kostar þig getuna til að aðlagast því sem þú lærir meðan þú smíðar. Að fresta þeim kaupir aðlögunarhæfni, en kostar þig langdrægan rekjanleika og samningsskýrleika. Að fjárfesta meira í kröfuverkfræði skiptir líka skammtímahraða fyrir minni endurvinnslu síðar: skipti sem borgar sig eftir því sem stærð, endingu og afleiðingar bilunar kerfis aukast. Stærstu verkefnin og þau mest eftirlitsskyldu sitja fast á hári fjárfestingarhliðinni. Lítið áhættulítið innra verkfæri gerir það ekki.

## Spurningar til að ræða með teyminu

1. **Hver telst hagsmunaaðili fyrir áhættumesta kerfi okkar og hverja skiljum við stöðugt út þar til samþykki?** Í stórri áætlun eru fólkið sem er sleppt sjaldan augljósir notendur: það eru rekstraraðilarnir sem reka hlutinn klukkan þrjú að nóttu, endurskoðendurnir sem þurfa að votta hann, stuðningsfólkið sem tekur á móti bilunum og þeir sem kerfið snertir en notar ekki, sem skrá sig aldrei inn en gögn þeirra þú heldur. Saknaðu þeirra og þú uppgötvar kröfur þeirra á dýrasta augnablikinu, við samþykki eða eftir að eftirlitsaðili spyr. Komdu með áþreifanlegt hagsmunaaðilakort á fundinn og álagsprófaðu það: fyrir hverja skyldubundna skyldu (aðgengi, persónuvernd, skjalavarðveislu, öryggi) nefndu manneskjuna sem á hana og kröfuna sem fangar hana. Ef þú getur ekki nefnt eiganda hefurðu fundið bil, og lagfæringin er að bæta þeim hagsmunaaðila við útdrátt núna frekar en að eftirbæta þörfum þeirra í fastan arkitektúr síðar.

2. **Þegar krafa breytist, getum við svarað hverju hún hefur áhrif á áður en við samþykkjum breytinguna?** Þetta er hagnýta prófið á hvort tvístefnu rekjanleiki þinn er raunverulegur eða skrautlegur. Í stóru eða eftirlitsskyldu kerfi getur ein reglubreyting gárað inn í hönnun, kóða, próf og samþykkissönnun, og að samþykkja hana blindandi er hvernig þú afhendir kerfi sem lítur reglufylgið út en brýtur hljóðlega reglu sem það fullnægði áður. Komdu með nýlega breytingarbeiðni og reyndu að rekja hana fram á við á fundinum: ef það tekur eftirmiðdag af fornleifafræði er rekjanleiki þinn ekki að vinna sitt verk. Svarið ætti að endurmóta breytingaferlið þitt, svo áhrifamat sé hröð fyrirspurn gegn lifandi slóð frekar en handvirk leit, og svo grunnlínur og útgáfustýring gefi þér stöðugan punkt til að breyta gegn.

3. **Hvar býr eina valdbæra uppspretta krafna okkar og hve mikill sannleikur er dreifður utan hennar?** Kröfusundrun (raunverulega tilgreiningin sem lifir yfir tölvupósta, miða, glærur og minni einhvers) er ein algengasta bilun í stórum teymum og hún er banvæn í úttektarhæfum kerfum þar sem þú verður að sýna hvað var samþykkt. Ákveddu, upphátt, hvaða skráningarkerfi er valdbært og líttu á allt sem sagt er annars staðar sem drög þar til það lendir þar með uppsprettu og rökum fest við. Komdu með sönnunargögn: teldu hve margar nýlegar umfangsdeilur enduðu í því að tveir vitnuðu í ólíkar „lokaútgáfur“. Ef talan er hærri en núll er aðgerðin að sameina í eina uppsprettu og skrifa niður rökin fyrir hverja kröfu, því að vita hvers vegna krafa er til er einmitt það sem leyfir þér að breyta henni eða sleppa örugglega síðar.

4. **Eru ófallbundnar kröfur okkar fangaðar nógu snemma til að knýja arkitektúr, eða höldum við áfram að uppgötva þær eftir að uppbyggingin er föst?** Afkasta-, tiltækileika-, öryggis- og aðgengisskyldur móta arkitektúr meira en flestir eiginleikar, og í stórri áætlun eru þær kröfurnar sem oftast koma upp of seint, þegar uppbyggingin sem þyrfti að fullnægja þeim er þegar steypt í steinsteypu. Togið á móti er raunverulegt: fallbundin hegðun er það sem hagsmunaaðilar biðja um upphátt og sýnist vel í kynningu, á meðan „undir-sekúndu svar undir hámarksálagi“ eða „WCAG aðgengisfylgni“ krafa er ósýnileg þar til hún er brotin. Komdu með núverandi lista yfir ófallbundnar kröfur fyrir áhættumesta kerfið þitt, punktinn á tímalínunni þar sem hver var skrifuð og hvort arkitektúr (kafli 3.1) fékk þær sem skýra knýjendur eða dró þær ályktun. Í fyrirtækja- og opinberu umhverfi skaltu bæta við skyldubundnum gæðaskyldum (dulkóðun, skjalavarðveislu, aðgengislögum) og athuga að hver og ein sé skrifleg, mælanleg krafa afhent hönnun frekar en forsenda, því að eftirbæta gæðaeiginleika eftir samþykki er þar sem fjárhagsáætlanir og tímaáætlanir deyja hljóðlega.

5. **Hvaða formfesta er rétt fyrir hvert kerfi sem við eigum og veljum við hana eftir áhættu eða vana?** Ein stór skipulagsheild rekur venjulega úrval kerfa, frá einnota innra verkfæri til lífs- eða öryggiseftirlitsskylds vettvangs, og að beita einni helgisiði á þau öll annaðhvort grefur áhættulitla vinnu í pappírsvinnu eða skilur áhættumikla vinnu vantilgreinda. Spennan er milli úttektarhæfis og fasts samþykkisgrundvallar formlegrar tilgreiningar fyrirfram og hraðrar endurgjafar og minni sóunar þróandi verkefnalista, og heiðarlega svarið fyrir flest fyrirtæki er yfirveguð blanda: formgerðu og rektu stöðugar, há-tryggingar skyldur á meðan þú útfærir vöruhegðun endurtekið. Komdu með stutta skrá yfir kerfin þín raðaða eftir afleiðingum bilunar, regluáhættu og breytingahraða, og nefndu fyrir hvert formfestuna sem þú notar í raun á móti formfestunni sem áhættan réttlætir. Fyrir opinbera áætlun fest við útboð og staðal eins og IEEE 29148 er formfestan að hluta fyrirmæli samningsins, svo umræðan snýst um hvar þú getur lagt lipra útfærslu ofan á án þess að brjóta rekjanleikann sem úttektin veltur á.

6. **Er hægt að sannprófa hverja kröfu í áhættumesta kerfinu okkar og ber hver samþykkisviðmið skrifuð á augnablikinu sem krafan var skrifuð?** Krafa sem þú getur ekki sannprófað er ekki krafa, hún er ósk, og sleipt orðalag eins og „hratt“, „öruggt“ eða „notendavænt“ kemst í gegnum rýni einmitt því enginn getur fellt það. Fyrir stórt teymi skiptir þetta tvöfalt máli: ósannprófanlegar kröfur framleiða umfangsdeilur við samþykki og gera ómögulegt að segja hvenær eiginleiki er raunverulega búinn. Sjónarmiðið á móti er hraði, því að festa mælanlegt viðmið og sannprófunaraðferð við hverja kröfu er hægara fyrirfram en prósi, en það er ódýrasta vörnin gegn dýrustu seinu endurvinnslunni. Komdu með úrtak nýlegra krafna og prófaðu hverja gegn einföldu viðmiði: er hún frumeindaleg, er hún mælanleg og nefnir hún hvernig hún verður athuguð. Í eftirlitsskyldu og opinberu samhengi skaltu framlengja prófið til sönnunargagna: krafa án rekjanlegrar, staðinnar samþykkissönnunar telst ekki afhent sama hvað hugbúnaðurinn virðist gera, svo samþykkisviðmið eru fræ regluvörsluskrárinnar sem þú munt að lokum þurfa að framleiða.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með pínulítið teymi og lítið fjármagn skaltu halda kröfum eins léttum og þú kemst upp með: notendasögur með samþykkisviðmiðum í einum sameiginlegum verkefnalista, ekki tilgreiningarskjal. Agi sem borgar sig jafnvel hér er að tala við raunverulega notendur áður en þú smíðar og skrá uppsprettu og rök hverrar sögu, svo vikan sem þú hefðir sóað í að smíða rangan eiginleika sé vikan sem þú sparar. Slepptu formlegum rekjanleika, en slepptu aldrei samtalinu sem segir þér hver raunverulega þörfin er.

**Lítið fyrirtæki.** Þú hefur líklega engan viðskiptagreinanda eða kröfusérfræðing, svo verkið fellur á þann sem er næst viðskiptavininum, og kaupa-gegn-smíða spurningin ræður. Rammaðu kröfur sem stuttan, forgangsraðaðan lista yfir niðurstöðurnar sem þú þarft, notaðu hann síðan til að meta tilbúin verkfæri frekar en að tilgreina sérsmíði. Vertu strangur í að aðskilja undirliggjandi þörf frá eiginleikalista söluaðila, því krafa skrifuð sem „við þurfum vöru X“ útilokar hljóðlega ódýrari valkosti sem hefðu uppfyllt raunverulegu þörfina.

**Stórfyrirtæki.** Stærð gerir kröfur að samningnum sem lætur mörg teymi smíða eitt samhangandi kerfi, svo forgangur er stöðluð ferli beitt samræmt: skilgreindir flokkar, tvístefnu rekjanleiki frá þörf til prófs, ein valdbær uppspretta og stýrð breyting með grunnlínum. Aðskildu viðskipta-, notenda- og kerfiskröfur skýrt og afhentu ófallbundnar kröfur arkitektúr sem knýjendur, svo umfang og gæðaskyldur dreifist ekki yfir teymi. Blandaðu formlegri tilgreiningu fyrir stöðugar, há-tryggingar skyldur við lipra útfærslu vöruhegðunar og stýrðu jafnvæginu eftir áhættu en ekki kjör neins eins teymis.

**Hið opinbera.** Innkaupareglur byggja oft allan samninginn í kringum kröfulýsingu, oft skipulagða samkvæmt staðli eins og IEEE 29148, svo nákvæmni og fullkomnun er samningsbundin, ekki valkvæð. Haltu kröfurekjanleikafylki sem tengir hverja kröfu við hönnun, prófatilvik og samþykkissönnun, því greiðsla til söluaðila, úttekt og authority to operate velta öll á sýndri þekju. Gagnsæi og almenn ábyrgð hækka kröfuna enn frekar: skyldubundnar skyldur um aðgengi, persónuvernd og skjalavarðveislu verða hver að birtast sem skýr, sannprófanleg krafa, og krafa án rekjanlegrar, staðinnar sönnunar er einfaldlega ekki afhent.

## Dæmi

**Sprotafyrirtæki.** Fjögurra manna sprotafyrirtæki sem smíðar tímaáætlunarforrit fangar kröfur sem notendasögur með samþykkisviðmiðum í sameiginlegum verkefnalista, ekki formlega tilgreiningu. Áður en það skrifar dagatalssamstillingareiginleikann ver stofnandinn eftirmiðdegi í að tala við fimm væntanlega viðskiptavini og lærir að raunverulega þörfin er að forðast tvíbókanir yfir tvö verkfæri, ekki samstillingin sem þeir höfðu gert ráð fyrir. Það eina samtal endurrammar söguna og sparar viku af því að smíða rangan hlut. Jafnvel í þessari stærð skrá þeir uppsprettu og rök hverrar sögu, svo þegar forgangsröðun breytist geta þeir sleppt eða endurunnið umfang án þess að rökræða aftur hvers vegna það var til.

**Stórfyrirtæki.** Fjölþjóðlegur banki skiptir út lánaveitingarvettvangi sínum. Kröfuteymið aðskilur viðskiptakröfur (stytta samþykkistíma, uppfylla útlánareglur), notendakröfur (lánafulltrúar þurfa að bera saman tilboð í einni sýn) og kerfiskröfur (vettvangurinn verður að samþættast þremur kjarnakerfum). Ófallbundnar kröfur (undir-sekúndu svar fyrir algengar fyrirspurnir, 99,95% tiltækileiki, dulkóðun persónugagna) eru fangaðar skýrt og afhentar arkitektúr (kafli 3.1) sem knýjendur. Sérhver krafa er rakin gegnum verkefnalistann til sjálfvirkra samþykkisprófa. Þegar eftirlitsaðili spyr hvernig tiltekinni útlánareglu er framfylgt fylgir teymið einfaldlega slóðinni frá reglunni til prófsins sem sannreynir hana.

**Hið opinbera.** Landsbundin stofnun kaupir bótahæfiskerfi gegnum formlegt útboð. Samningurinn er festur við kröfulýsingu skipulagða samkvæmt IEEE 29148, sem nær yfir fallbundnar hæfisreglur, skyldubundna aðgengisfylgni, persónuverndar- og skjalavarðveisluskorður og öryggisstýringar. Kröfurekjanleikafylki tengir hverja kröfu við hönnunarþætti, prófatilvik og samþykkissönnun. Greiðslur til söluaðila og authority to operate (formlega samþykkið til að reka kerfið í framleiðslu) velta báðar á sýndri þekju. Krafa án rekjanlegrar, staðinnar samþykkissönnunar telst einfaldlega ekki afhent, sama hvað hugbúnaðurinn virðist gera.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Hagfræðirökin fyrir kröfuverkfræði hvíla á kostnaði við að laga galla seint. Iðnaðarrannsóknir finna stöðugt að kröfugallar eru meðal algengustu og dýrustu orsaka verkefnabilunar, og að kostnaður við að laga galla klífur um stærðargráður frá kröfufasanum til framleiðslu. Svo peningar sem varið er í að skýra og staðfesta kröfur eru í raun vogarafl: hófleg fjárfesting snemma sparar þér að smíða, prófa og reka rangan hlut.

Heildareignarkostnaður krafna felur í sér viðvarandi fyrirhöfn útdráttar, tilgreiningar, verkfæra og breytingastjórnunar yfir allan líftíma kerfisins. Hann er ekki einskiptis kostnaður. Gegn honum stendur kostnaður lélegra krafna: endurvinnsla, umfangsdeilur, tímaáætlunarfrávik, misheppnað samþykki, samningsbundin viðurlög og, í eftirlitsskyldu umhverfi, sektir eða tap á heimild. Fyrir forystu skaltu ramma kröfuþroska sem áhættulækkun og fyrirsjáanleika. Rektu kröfusveiflu, gallaupptök og hlutfall afhentrar vinnu sem rekja má til staðfestrar þarfar og tengdu þetta við spár verkefnastjórnunar (kafli 10.6). Ávöxtunin birtist ekki sem eiginleiki. Hún birtist sem bilanirnar og endurvinnslan sem aldrei gerðust.

## Andmynstur og gildrur

- **Lausnir í dulargervi krafna:** að tilgreina valda tækni eða skjáuppsetningu í stað undirliggjandi þarfar og útiloka betri valkosti.
- **Tvírætt orðalag:** „hratt“, „öruggt“, „innsæistengt“ án mælanlegs viðmiðs, sem gerir kröfuna ósannprófanlega.
- **[Gullhúðun](https://en.wikipedia.org/wiki/Gold_plating_(software_engineering)):** að fanga kröfur sem enginn hagsmunaaðili þarf í raun og blása upp umfang og kostnað.
- **Vantandi ófallbundnar kröfur:** að uppgötva afkasta-, öryggis- eða aðgengisskyldur aðeins eftir að arkitektúr er fastur.
- **Kröfusundrun:** sannleikurinn dreifður yfir tölvupósta, miða og glærur án valdbærrar uppsprettu.
- **Frosin eða óstýrð breyting:** annaðhvort að neita allri breytingu eða samþykkja hverja án áhrifamats.
- **Enginn rekjanleiki:** vanhæfni til að svara hverju breyting hefur áhrif á eða hvers vegna eiginleiki er til, banvænt í úttektarhæfum kerfum.
- **Greiningarlömun:** endalaus tilgreining sem seinkar námi af virkum hugbúnaði.
- **Hunsaðir hagsmunaaðilar:** rekstraraðilar, endurskoðendur og þeir sem kerfið snertir skildir út þar til samþykki.

## Þroskalíkan

- **Stig 1, Upphaf.** Kröfur eru óbeinar eða munnlegar, fangaðar ósamræmt og viðbragðsdrifið. Umfangsdeilur og endurvinnsla eru algeng. Enginn rekjanleiki, engin samþykkisviðmið og ekkert skilgreint ferli.
- **Stig 2, Þróun.** Sum teymi skrifa kröfur niður og rekja þær á verkefni, með grunnforgangsröðun og ad hoc breytingameðhöndlun. Vinnubrögð eru til en ólík eftir teymi og manneskju, svo flokkar, formfesta og gæði eru ósamræmd yfir skipulagsheildina.
- **Stig 3, Stöðlun.** Staðlað kröfuferli er skjalfest og framfylgt um alla skipulagsheildina: skilgreindir flokkar, útdráttar- og staðfestingarvenjur, samþykkisviðmið fest við á höfundartíma, ein valdbær uppspretta og tvístefnu rekjanleiki frá þörf til prófs, lagað samræmt að lipru eða áætlanadrifnu samhengi.
- **Stig 4, Stjórnun.** Ferlið er mælt og stýrt með gögnum. Kröfusveifla, gallaupptök, rekjanleikaþekja og hlutfall afhentrar vinnu sem rekja má til staðfestrar þarfar eru rakin gegn grunnlínum, rekjanleiki nær til samþykkissönnunar og regluvörslu og kröfumælikvarðar næra verkefnaspár (kafli 10.6), svo breytinga- og gæðaákvarðanir byggi á sönnunargögnum frekar en skoðunum.
- **Stig 5, Samhæfing.** Kröfuvinnubrögð eru stöðugt bætt og samþætt um skipulagsheildina. Formfesta er stillt aðlögunarhæft eftir áhættu og niðurstöðu, útdráttar- og rekjanleikaverkfæri tengjast uppgötvun, arkitektúr og afhendingu og skipulagsheildin notar eigin mælisögu til að koma í veg fyrir endurtekna kröfugalla áður en þeir ná kóða.

## Hugmyndir til umræðu

- Hvernig greinirðu raunverulega kröfu frá ótímabærri lausn þegar eldri hagsmunaaðili setur hana fram sem lausn?
- Hvaða kröfuformfesta er rétt fyrir áhættumesta kerfið þitt á móti áhættuminnsta og hver ákveður?
- Hvernig heldurðu tvístefnu rekjanleika núverandi í hraðfara lipra verkefnalista án þess að hann verði skrifræðisleg yfirbygging?
- Hvaða ófallbundnu kröfur eru oftast uppgötvaðar of seint í skipulagsheildinni þinni og hvers vegna?
- Í eftirlitsskyldri áætlun, hvað telst nægileg samþykkissönnun þess að krafa hafi verið uppfyllt?
- Hvernig ættu gervigreindaraðstoðuð útdráttar- og tilgreiningarverkfæri að breyta kröfuvinnubrögðum þínum og hvaða nýju áhættu kynna þau?

## Helstu atriði

- Kröfur segja þarfir og skorður, ekki lausnir. Þær verða að vera nauðsynlegar, ótvíræðar, sannprófanlegar og rekjanlegar.
- Aðskildu fallbundnar, ófallbundnar og skorðukröfur og viðskipta-, notenda- og kerfisstig.
- Dragðu fram úr raunverulegum hagsmunaaðilum, greindu og forgangsraðaðu, tilgreindu á hæfilegri formfestu, staðfestu áður en þú smíðar og stýrðu breytingum.
- Tvístefnu rekjanleiki frá þörf til samþykkissönnunar er burðarás ábyrgðar, sérstaklega í eftirlitsskyldu samhengi.
- Lipurt og áætlanadrifið samhengi deila sömu athöfnum. Þau eru ólík í tímasetningu, formfestu og afurðum, svo veldu eftir áhættu.
- Kostnaður lélegra krafna er greiddur seint og margfaldaður. Fjárfesting snemma er vogarafl gegn endurvinnslu og misheppnuðu samþykki.

## Heimildir og frekari lestur

- IEEE and ISO/IEC, *Guide to the Software Engineering Body of Knowledge (SWEBOK)*, Software Requirements knowledge area
- Karl Wiegers and Joy Beatty, *Software Requirements*
- ISO/IEC/IEEE 29148, *Systems and software engineering: Life cycle processes: Requirements engineering*
- Suzanne Robertson and James Robertson, *Mastering the Requirements Process*
- Dean Leffingwell, *Agile Software Requirements*
- Mike Cohn, *User Stories Applied*
- Ian Sommerville, *Software Engineering* (requirements engineering chapters)
