# 5.3 Aðgengi

## Yfirlit og tilgangur

[Aðgengi](https://en.wikipedia.org/wiki/Accessibility) (oft stytt í „a11y“) er sú venja að smíða hugbúnað sem fólk með fötlun getur skynjað, skilið, ratað um og notað. Það nær yfir fólk sem er blint eða með skerta sjón, sem er heyrnarlaust eða heyrnarskert, sem hefur hreyfihömlun, sem hefur vitræna eða námslega sérstöðu og sem stendur frammi fyrir tímabundnum eða aðstæðubundnum takmörkunum eins og handleggsbroti, skæru sólarljósi eða háværu herbergi. Um það bil einn af hverjum fimm hefur fötlun, og allir njóta góðs af aðgengilegri hönnun einhvern tíma. Þetta er ekki sérhæfð aðlögun fyrir fáa. Það er grunnlína gæða.

Fyrir stór teymi verður aðgengi að vera byggt inn í kerfið, ekki látið eftir góðum ásetningi einstaklinga. Þegar mörg teymi afhenda inn í eina vöru getur einn óaðgengilegur íhlutur (ómerktur eyðublaðsreitur, stöðuvísir sem treystir á lit einn, lyklaborðsgildra í glugga) læst fatlaða notendur úti úr heilli ferð. Að byggja aðgengi inn í sameiginlega íhluti, hönnunartákn, prófunarleiðslur og skilgreiningar á „búið“ er eina leiðin til að gera það áreiðanlegt í stærð. Að bæta því við eftir á er dýrt og villuhætt. Að hanna það inn er ódýrt og varanlegt.

Fyrir hið opinbera er aðgengi lagaskylda og borgaraleg skylda, ekki æskilegur eiginleiki. Opinber þjónusta verður að þjóna sérhverjum meðlim almennings, og fatlaðir borgarar hafa oft engan annan veitanda: ef vefur ríkisins er óaðgengilegur geta þeir ekki fengið bætur sínar, leyfi eða kosið með öðrum hætti. Lög og staðlar um allan heim gera aðgengi skylt fyrir opinbera aðila og sífellt oftar einkageirann líka. Þessi kafli meðhöndlar aðgengi sem þrennt í einu: lagaskyldu, siðferðilega skyldu og einfaldlega góða hönnun.

*Sjá einnig:* kafla 5.2 (viðmótshönnun og hönnunarkerfi), kafla 5.6 (framendaverkfræði) og kafla 5.1 (grunn notendaupplifunar).

## Meginreglur

- Aðgengi er grunngæðaeiginleiki, eins og öryggi og afköst, ekki valkvæður eiginleiki.
- POUR-reglurnar: viðmót verða að vera skynjanleg (Perceivable), nothæf (Operable), skiljanleg (Understandable) og traust (Robust).
- [Merkingarfræðilegt HTML](https://en.wikipedia.org/wiki/Semantic_HTML) fyrst. Notaðu [ARIA](https://en.wikipedia.org/wiki/WAI-ARIA) aðeins til að fylla raunveruleg göt, aldrei í stað innlendra þátta.
- Allt sem er nothæft með mús verður að vera nothæft með lyklaborði einu.
- Miðlaðu ekki upplýsingum með lit, lögun eða staðsetningu einum.
- Sjálfvirk verkfæri grípa aðeins brot vandamála. Handvirk prófun og prófun með [hjálpartækni](https://en.wikipedia.org/wiki/Assistive_technology) er nauðsynleg.
- Aðgengileg hönnun er betri hönnun fyrir alla („[kantsteinaáhrifin](https://en.wikipedia.org/wiki/Curb_cut)“, þar sem eiginleikar smíðaðir fyrir fatlað fólk gagnast öllum notendum).
- Hannaðu og prófaðu með fötluðu fólki, ekki bara fyrir það.

## Ráðleggingar

### Hannaðu og smíðaðu samkvæmt WCAG, með núverandi staðal að markmiði

[Web Content Accessibility Guidelines](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) eru alþjóðlega viðmiðið. WCAG 2.1 og 2.2 eru skipulögð undir POUR-reglunum fjórum, með prófanlegum árangursviðmiðum á samræmisstigum A, AA og AAA. Stefndu að stigi AA sem grunnlínu, það er það sem flest lög vísa til. WCAG 2.2 bætir við viðmiðum um fókussýnileika, markmiðsstærð og minnkun vitræns álags. WCAG 3.0 er væntanlegur arftaki, uppbyggður á annan hátt og enn í þróun. Fylgstu með honum, en smíðaðu samkvæmt 2.2 AA í dag. Líttu á leiðbeiningarnar sem gólf, ekki þak: að standast hvert viðmið tryggir ekki raunverulega nothæfa upplifun.

### Notaðu merkingarfræðilegt HTML og rétt ARIA

Innlendir HTML-þættir (hnappar, tenglar, eyðublaðsstýringar, fyrirsagnir, listar, kennileiti) koma með innbyggðri aðgengismerkingarfræði, lyklaborðshegðun og stuðningi hjálpartækni. Notaðu þá fyrst. Náðu í ARIA (Accessible Rich Internet Applications) hlutverk, ástönd og eiginleika aðeins til að lýsa sérsmíðuðum viðmótshlutum sem HTML getur ekki tjáð, og fylgdu ARIA Authoring Practices. Fyrsta regla ARIA er einföld: notaðu ekki ARIA ef innlendur þáttur dugar. Röng ARIA er verri en engin: hún leiðir [skjálesara](https://en.wikipedia.org/wiki/Screen_reader) virkt afvega. Gefðu síðunni rökrétta fyrirsagnabyggingu, merkingarbær merki, varatexta fyrir myndir, texta og afrit fyrir miðla og forritunarlega tengingu milli hvers merkis og stýringar þess.

### Tryggðu lyklaborðs- og hjálpartækninothæfi

Sérhver gagnvirkur þáttur verður að vera aðgengilegur og nothæfur með lyklaborði einu, í rökréttri röð, með skýrt sýnilegum fókusvísi. Forðastu lyklaborðsgildrur. Stýrðu fókus af ásetningi þegar efni breytist: færðu fókus í glugga þegar hann opnast, skilaðu honum þegar glugginn lokast og tilkynntu kvikar uppfærslur gegnum lifandi svæði. Prófaðu með raunverulegum hjálpartækjum, þar á meðal skjálesurum á tölvum og farsímum, skjástækkun, raddstýringu og rofaaðgangi. Og virtu notendastillingar eins og minnkaða hreyfingu og aukið birtuskil.

### Prófaðu með sjálfvirkum verkfærum, handvirkri rýni og raunverulegum notendum

Sjálfvirkir aðgengisskannar eru verðmætir og þeir ættu að keyra í leiðslunni á hverri breytingu. En rannsóknir sýna stöðugt að þeir grípa aðeins minnihluta raunverulegra vandamála, um það bil þriðjung. Restin þarfnast mannlegrar dómgreindar: lyklaborðsyfirferða, skjálesaraprófunar, birtuskilsathugana og spurningar um hvort efnið sé í raun skiljanlegt. Mikilvægast af öllu, fáðu fólk með fötlun inn í nothæfisprófanir. Byggðu aðgengissamþykktarviðmið inn í skilgreininguna á „búið“, svo vandamál séu gripin á sögu frekar en í úttekt fyrir opnun.

### Gerðu aðgengi skipulagslegt, ekki hetjulegt

Bakaðu aðgengi inn í hönnunarkerfið svo íhlutir afhendist aðgengilegir sjálfgefið. Bjóddu þjálfun svo hönnuðir, verkfræðingar, efnishöfundar og vörustjórar viti hver fyrir sig hvað þeir bera ábyrgð á. Settu aðgengisstaðal, eiganda eða fyrirmyndarmiðstöð og úrbótaferli. Birtu aðgengisyfirlýsingu og gefðu notendum leið til að tilkynna hindranir. Og keyptu aðgengilega: krefstu þess að söluaðilar og þriðja aðila íhlutir uppfylli kröfur og leggi fram sönnunargögn (eins og aðgengissamræmisskýrslu).

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
|---|---|---|
| Byggja aðgengi inn frá byrjun | Ódýrast, varanlegt, betra fyrir alla | Krefst þjálfunar og aga fyrirfram |
| Bæta við / úrbæta síðar | Frestar fyrirhöfn, opnar fljótlega útgáfu | Langtum dýrara, brothætt, lagaleg útsetning á meðan |
| Eingöngu sjálfvirkar prófanir | Hraðar, ódýrar, grípa afturfarir í CI | Missir af um tveimur þriðju vandamála. Falskt öryggi |
| Handvirk + hjálpartækniprófun | Grípur raunverulegar nothæfishindranir | Hægari, þarfnast hæfra prófenda og tækja |
| Prófun með fötluðum notendum | Sannleikur um raunverulega upplifun | Ráðningarfyrirhöfn og kostnaður, verður að gera af virðingu |

Meginmálamiðlunin er agi fyrirfram gegn frestuðum kostnaði. Aðgengi byggt inn er ódýrt og bætir gæði fyrir alla. Aðgengi bætt við undir lagaþrýstingi er dýrt, ófullkomið og streituvaldandi. Til lengri tíma er engin raunveruleg málamiðlun gegn „hraða“: óaðgengilegur hugbúnaður virkar einfaldlega ekki fyrir fimmtung notenda þinna. Það er galli, ekki sparnaður.

## Spurningar til að ræða með teyminu

1. **Fella aðgengisafturfarir smíðina okkar eins og brotið próf gerir, og ef ekki, hvers vegna ekki?** Sjálfvirkir skannar grípa aðeins um þriðjung vandamála, en þau sem þeir grípa (vantandi merki, birtuskilsbilanir, ómerktar stýringar) eru ódýr að grípa í CI og dýr að finna í úttekt fyrir opnun. Að líta á afturför sem smíðabilun er það sem flytur aðgengi frá hetjulegu einstaklingsátaki yfir í áreiðanlegan kerfiseiginleika, sem er það eina sem virkar þegar mörg teymi afhenda inn í eina vöru. Ákveddu hvaða athuganir eru hindrandi, hverjar ráðgefandi og hver getur yfirskrifað bilun. Komdu með núverandi skannaniðurstöður þínar og skilgreiningu á „búið“ á fundinn. Ef aðgengisviðmið eru ekki skrifuð í skilgreininguna á „búið“ á sögu verður þeim forgangsraðað niður um leið og frestur þrengist.

2. **Hver er regla okkar fyrir sérsmíðaða viðmótshluti og hver rýnir ARIA áður en hún fer út?** Innlendir HTML-þættir koma með lyklaborðshegðun og stuðningi hjálpartækni ókeypis, og röng ARIA er verri en engin því hún leiðir skjálesara virkt afvega. Komdu þér saman um að merkingarfræðilegt HTML sé sjálfgefið og að hver sérsmíðaður viðmótshlutur (sérsmíðaður fellilisti, dagsetningarvalmynd eða gluggi) krefjist lyklaborðs- og skjálesaraferðar fyrir sameiningu, samkvæmt ARIA Authoring Practices. Þetta skiptir mestu fyrir gagnvirku íhlutina sem mörg teymi endurnýta, því einn bilaður gluggi með lyklaborðsgildru getur læst fatlaða notendur úti úr heilli ferð. Komdu með lista yfir sérsmíðuðu viðmótshlutina þína og spyrðu hverjir hafa verið prófaðir með raunverulegum skjálesara. Allir sem ekki hafa verið það eru skuldir faldar í sameiginlegum kóða.

3. **Hver er stefna okkar um aðgengisyfirlög og trúir nokkur að þau séu raunveruleg lagfæring?** Yfirlög eru markaðssett sem eins línu skrifta sem gerir vef samræmdan, og þau eru freistandi þegar lagaþrýstingur kemur og frestur vofir. Þau skila ekki raunverulegu samræmi, þau geta versnað upplifun notenda hjálpartækni og fyrir hið opinbera skilja þau undirliggjandi lagaskylduna eftir ófullnægða. Ákveddu skýrt að þú munir fjárfesta í merkingarfræðilegu álagi, lyklaborðsstuðningi og prófun með fötluðu fólki frekar en kaupa viðmótshlut sem breiðir yfir vandann. Komdu með kostnað yfirlagsáskriftar og berðu saman við að byggja aðgengi inn í íhluti og leiðslu einu sinni. Að ramma þetta snemma kemur í veg fyrir örvæntingarfulla innkaupaákvörðun síðar sem eyðir peningum og lagar ekkert.

4. **Er fatlað fólk hluti hönnunar okkar og prófana, eða erum við enn að hanna fyrir ímyndaðan notanda sem við fundum upp?** Sjálfvirkir skannar og jafnvel sérfræðingaúttektir segja þér hvort álag samræmist. Þeir segja þér ekki hvort blindur notandi getur í raun klárað greiðsluna þína eða manneskja með vitræna fötlun skilur villuboðin þín. Að fá fatlaða þátttakendur inn er eina uppspretta sannleikans og það breytir því sem þú smíðar, en það vekur raunverulegar spurningar um hvernig þú ræður sanngjarnt, hvernig þú bætir fólki tíma þess og hvernig þú forðast að líta á einn þátttakanda sem talsmann fyrir hverja fötlun. Komdu með núverandi rannsóknarskrá þína, ráðningar- og greiðsluvenjur og heiðarlega talningu á því hve margar rannsóknir síðasta árs fólu í sér fatlaða þátttakendur. Fyrir stóra skipulagsheild er endurtekinn hópur með sanngjarna þóknun og þekju yfir sjón-, heyrnar-, hreyfi- og vitrænar þarfir það sem breytir þessu úr einskiptis látbragði í áreiðanlegt inntak. Hjá hinu opinbera er að fá almenning sem þú þjónar með oft hluti lagalegrar og borgaralegrar skyldu, ekki valkvæð kurteisi.

5. **Þegar við kaupum eða fellum inn þriðja aðila íhlut, krefjumst við sönnunar á aðgengi og hver athugar hana?** Mikið af því sem fer út í stórri vöru er ekki skrifað innanhúss: dagsetningarvalmynd úr bókasafni, greiðsluviðmótshlutur í iframe, línuritapakki, heil SaaS-eining. Einn óaðgengilegur innfelldur íhlutur getur fellt heila ferð sama hve hreinn eigin kóði þinn er, og þegar hann er tengdur inn er dýrt að skipta honum út. Ákveddu að aðgengi sé innkaupakrafa, að söluaðilar verði að leggja fram aðgengissamræmisskýrslu (skjal eins og VPAT sem segir hvernig vara mælist gegn WCAG) og að einhver tæknilegur staðfesti fullyrðinguna frekar en að skrá hana. Komdu með skrá yfir þriðja aðila íhluti þína og spyrðu hverjir hafa núgildandi, trúverðug samræmissönnunargögn. Í fyrirtækja- og opinberum innkaupum skaltu skrifa WCAG 2.2 AA samræmi og rétt til úrbóta inn í samninginn, því loforð gefið fyrir undirritun er langtum ódýrara að framfylgja en hindrun uppgötvuð eftir opnun.

6. **Hvert er markmiðssamræmisstig okkar, hver á það og hvernig höldum við því núgildandi þegar staðlar hreyfast?** WCAG 2.2 AA er gólf dagsins í dag og flest lög vísa til þess, en 2.2 bætti við viðmiðum sem mörg teymi hafa ekki tekið upp og WCAG 3.0 er á leiðinni með annarri byggingu. Án nefnds eiganda rekur staðallinn: ólík teymi miða á ólíkar útgáfur, enginn rekur bilið og samræmi rotnar hljóðlega milli úttekta. Ákveddu nákvæma útgáfu og stig sem þú smíðar samkvæmt, hver hefur vald til að hækka það og hvernig ný viðmið ná hönnunarkerfinu og skilgreiningunni á „búið“. Komdu með núverandi yfirlýst markmið þitt, sönnunargögn um hvar teymi uppfylla það í raun og stuttan vegvísi til að taka upp 2.2 viðmiðin sem þú hefur sleppt. Fyrir stóra eða opinbera skipulagsheild eru aðgengiseigandi eða fyrirmyndarmiðstöð, útgefin aðgengisyfirlýsing og skjalfest áætlun fyrir næstu staðalútgáfu það sem leyfir þér að svara eftirlitsaðila eða dómstól með sönnunargögnum frekar en góðum ásetningi.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hraði er þér hliðhollur hér, því aðgengi er ódýrast þegar kóðagrunnurinn er lítill. Bættu aðgengisskanna við CI og lyklaborðsferð við gátlista sameiningarbeiðna frá fyrsta spretti og hallaðu þér að merkingarfræðilegu HTML svo þú fáir lyklaborðs- og skjálesarastuðning ókeypis. Slepptu yfirlögum og þungum verkfærum. Ávinningurinn er að þegar innkaupateymi viðskiptavinar biður um samræmisskýrslu mitt í sölu geturðu svarað á dögum í stað þess að flýta þér.

**Lítið fyrirtæki.** Án aðgengissérfræðings og með þröngt fjárhagsáætlun skaltu kaupa aðgengi frekar en smíða það: veldu vettvang, þema eða íhlutasafn sem þegar samræmist og segir það og kjóstu söluaðila sem birta aðgengisyfirlýsingu. Dekkaðu verðmiklu grunnatriðin sjálfur með ókeypis verkfærum, lyklaborðsathugunum, birtuskilsathugara og skýrum merkjum á hverjum reit, því þau grípa bilanirnar sem oftast útiloka viðskiptavini. Líttu á rangt eða ónothæft sjálfvirkt flæði sem týndan viðskiptavin, því lítið fyrirtæki býður sjaldan aðstoðarrás til að falla aftur á.

**Stórfyrirtæki.** Í stærð er verkið að gera aðgengi að kerfiseiginleika yfir mörg teymi. Afhentu aðgengilega íhluti sjálfgefið í hönnunarkerfinu, hlið afturfarir í CI og settu upp eiganda eða fyrirmyndarmiðstöð með úrbótaferli og þjálfun fyrir hönnuði, verkfræðinga og efnishöfunda. Raktu samræmi með tímanum sem mælikvarða, skrifaðu WCAG-samræmi inn í innkaup og stýrðu þriðja aðila íhlutum sem eignasafni svo einn innfelldur viðmótshlutur geti ekki hljóðlega fellt sameiginlega ferð.

**Hið opinbera.** Aðgengi er lagaskylda og borgaraleg skylda, því fatlaðir borgarar hafa oft engan annan veitanda fyrir bætur, leyfi eða atkvæði. Smíðaðu samkvæmt staðlinum sem lögsagnarumdæmi þitt vísar til (til dæmis Section 508, EN 301 549 eða evrópsku aðgengislögin varpað á WCAG 2.2 AA), birtu aðgengisyfirlýsingu með leið til að tilkynna hindranir og prófaðu með fatlaða almenningnum sem þú þjónar. Hafnaðu yfirlögum sem staðgengli raunverulegs samræmis og krefstu þess að söluaðilar leggi fram trúverðug sönnunargögn og rétt til úrbóta í samningi.

## Dæmi

**Sprotafyrirtæki.** Þriggja manna sprotafyrirtæki sem smíðar ráðningartæki bætti aðgengisskanna við smíði sína og fljótri lyklaborðsferð við gátlista sameiningarbeiðna frá allra fyrsta spretti, með þeim rökum að það væri ódýrara að vera aðgengilegur en að laga það síðar. Þegar innkaupateymi meðalstórs viðskiptavinar bað um aðgengissamræmisskýrslu í söluferli notaði sprotafyrirtækið þegar merkingarfræðilegt HTML, merkti hvern reit og hafði sýnilegan fókus alls staðar, svo það svaraði á dögum í stað þess að flýta sér. Sú reiðubúð vann samning sem keppinautur tapaði á sömu kröfunni.

**Stórfyrirtæki.** Stór smásali stóð frammi fyrir hópmálsókn því blindir viðskiptavinir gátu ekki klárað greiðslu með skjálesara. Umfram sáttargreiðsluna og lögfræðikostnað þurfti fyrirtækið að úrbæta undir tímalínu dómstóls. Á eftir endurbyggði það aðgengi inn í hönnunarkerfi sitt og CI-leiðslu, bætti skjálesaraprófun við skilgreininguna á „búið“ og þjálfaði teymi sín. Endurbyggða, aðgengilega greiðslan bætti líka umbreytingu og fækkaði stuðningssamskiptum fyrir alla: lagfæringarnar sem hjálpuðu skjálesarnotendum (skýr merki, villuboð, rökrétt röð) hjálpuðu öllum notendum.

**Hið opinbera.** Opinber bótastofnun var lagalega skylduð til að uppfylla WCAG 2.1 AA fyrir netumsókn sína. Snemmbúin prófun með blindum og sjónskertum notendum, lyklaborðsnotendum og notendum með vitræna fötlun leiddi í ljós að lit-einn „skyldureitur“ vísir, óaðgengileg dagsetningarvalmynd og ótilkynntar staðfestingarvillur hindruðu fólk í að klára. Að laga þetta, með merkingarfræðilegu álagi, sýnilegum fókus, lifandi-svæðis villutilkynningum og [látlausri málhjálp](https://en.wikipedia.org/wiki/Plain_language), leyfði fötluðum borgurum að sækja um sjálfir í fyrsta sinn. Það minnkaði háð á hjálp í eigin persónu og lækkaði afgreiðslukostnað, á sama tíma og lagaskyldunni var mætt.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Viðskiptarökin hvíla á markaðsútbreiðslu, lagaáhættu, afgreiðslukostnaði og gæðum. Fatlað fólk og fjölskyldur þess ráða umtalsverðu kaupmætti. Að útiloka það fórnar honum. Aðgengileg þjónusta dregur úr þörf fyrir dýrar aðstoðarrásir (síma- og persónulega hjálp), sem er bein rekstrarsparnaður, sérstaklega hjá hinu opinbera. Og því aðgengisbætur (skýr merki, lyklaborðsstuðningur, læsilegt efni, traust álag) hjálpa öllum hækka þær yfirleitt heildarklárun og ánægju.

Hvað heildareignarkostnað varðar er upptökukostnaðurinn þjálfun, verkfæri og að byggja aðgengi inn í íhluti og leiðslur, allt hóflegt þegar þú gerir það frá byrjun. Kostnaðurinn við að taka ekki upp er alvarlegur og kemur úr nokkrum áttum: lagaleg ábyrgð (málsóknir, sáttir, dómstólafyrirskipuð úrbót, eftirlitsrefsingar), langtum hærri kostnaður við að bæta við undir frestþrýstingi, mannorðsskaði og viðvarandi kostnaður við að þjóna útilokuðum notendum gegnum dýrari rásir. Að bæta við eftir á kostar yfirleitt mörgum sinnum það sem að hanna inn hefði gert.

Til að færa rök við forystu skaltu byrja á lagaskyldunni þar sem hún á við (hún er óumsemjanleg fyrir hið opinbera og sífellt oftar fyrir einkageirann). Magnsettu síðan þýðið sem þú útilokar, aðstoðarrásarkostnað þeirrar útilokunar og „kantsteinaávinning“ fyrir alla notendur. Staðsettu aðgengi sem áhættustjórnun auk gæða, ekki góðgerðarstarf.

## Andmynstur og gildrur

- **Aðgengi sem hak fyrir opnun**: úttekt í lokin í stað samfelldra vinnubragða, sem tryggir dýra endurvinnu á síðustu stundu.
- **„Div-súpa“**: ómerkingarfræðilegt álag með smellimeðhöndlurum á almennum þáttum, ósýnilegt hjálpartækni.
- **ARIA-misnotkun**: að festa ARIA á bilað álag, sem leiðir skjálesara meira afvega en einfalt álag myndi gera.
- **Upplýsingar eingöngu í lit**: staða sýnd með lit einum, ósýnileg litblindum notendum.
- **Ósýnilegur fókus**: að fjarlægja fókusútlínur fyrir útlit, sem strandar lyklaborðsnotendur.
- **Lyklaborðsgildrur**: gluggar og viðmótshlutar sem fanga eða týna fókus.
- **Falskt öryggi eftir sjálfvirka skönnun**: að standast skanna og gera ráð fyrir að varan sé aðgengileg.
- **Aðgengisyfirlög**: þriðja aðila „eins-línu lagfæringar“ viðmótshlutir sem skila ekki raunverulegu samræmi og geta versnað upplifun.
- **Að útiloka fatlaða notendur úr rannsóknum**: að hanna fyrir ímyndaðan fatlaðan notanda í stað þess að prófa með raunverulegum.

## Þroskalíkan

**Stig 1: Upphaf.** Engin aðgengisvinnubrögð. Vandamál uppgötvast aðeins þegar notandi kvartar eða málsókn berst og viðbrögð eru viðbragðsdrifin. Álag er ómerkingarfræðilegt og óprófað og enginn á vandann.

**Stig 2: Þróun.** Vitund er til og sum teymi bregðast við henni: sjálfvirkur skanni í smíði hér, lyklaborðsferð þar, úttekt fyrir opnun fyrir stóra útgáfu. Vinnubrögð eru grunn og ósamræmd milli teyma, aðgengi er enn gátlisti á síðustu stigum og því er oft forgangsraðað niður undir tímaáætlunarþrýstingi.

**Stig 3: Stöðlun.** WCAG 2.2 AA er skjalfesti staðallinn, framfylgt um alla skipulagsheildina. Aðgengi er byggt inn í hönnunarkerfið svo íhlutir afhendist aðgengilegir sjálfgefið, prófaðir sjálfvirkt og handvirkt og skrifaðir inn í skilgreininguna á „búið“. Teymi eru þjálfuð, eigandi eða fyrirmyndarmiðstöð er til og úrbótaferli er skilgreint.

**Stig 4: Stjórnun.** Aðgengi er mælt og stýrt með gögnum gegn grunnlínum. Skipulagsheildin rekur samræmismælikvarða með tímanum (skannaárangurshlutföll, fjölda opinna hindrana eftir alvarleika, skjálesaraprófunarþekju mikilvægra ferða og tíma til úrbóta), skýrir frá þeim á hvert teymi á mælaborði og meðhöndlar afturfarir sem smíðabilanir frekar en ráðgefandi viðvaranir. Markmið eru sett gegn grunnlínu og framvinda rýnd, svo teymi sem rennur sé sýnilegt áður en úttekt finnur það.

**Stig 5: Samhæfing.** Aðgengi er stöðugt bætt og samþætt um skipulagsheildina. Fatlað fólk er hluti rannsókna og prófana reglulega og aðgengi er fellt inn í innkaup, hönnunartákn og CI. Skipulagsheildin aðlagast þegar staðlar hreyfast (tekur upp ný WCAG-viðmið og undirbýr sig fyrir WCAG 3.0) og hún hefur áhrif á söluaðila og samstarfsaðila svo öll aðfangakeðjan samræmist.

## Hugmyndir til umræðu

- Hvernig heldurðu aðgengi frá því að vera forgangsraðað niður þegar frestir þrengjast?
- Hver er rétta blandan af sjálfvirkri, handvirkri og notendaprófun fyrir áhættusnið þitt?
- Hvernig ætti að skrifa aðgengissamræmi inn í söluaðilasamninga og innkaup?
- Hvernig tekstu á við bilið milli WCAG-samræmis og raunverulegrar nothæfni fyrir fatlað fólk?
- Hvernig ættu teymi að undirbúa sig fyrir WCAG 3.0 meðan þau smíða samkvæmt 2.2 í dag?
- Hvernig ræðurðu fatlaða rannsóknarþátttakendur og bætir þeim tíma þeirra sanngjarnt og af virðingu?

## Helstu atriði

- Aðgengi er grunngæðaeiginleiki og, fyrir hið opinbera, lagakrafa.
- Hannaðu samkvæmt WCAG 2.2 AA sem gólfi. Notaðu POUR-reglurnar sem hugarlíkan.
- Merkingarfræðilegt HTML fyrst. ARIA aðeins til að fylla raunveruleg göt, gert rétt.
- Sjálfvirk verkfæri grípa um þriðjung vandamála. Handvirk prófun og hjálpartækniprófun er nauðsynleg.
- Prófaðu með fötluðu fólki, ekki bara fyrir það.
- Að byggja aðgengi inn er ódýrt og varanlegt. Að bæta við eftir á er dýrt og brothætt.
- Aðgengileg hönnun er betri hönnun fyrir alla: kantsteinaáhrifin eru raunveruleg.

## Heimildir og frekari lestur

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2* and supporting Understanding/Techniques documents
- W3C, *WAI-ARIA Authoring Practices Guide*
- W3C Web Accessibility Initiative (WAI), introductory and tutorial materials
- Laura Kalbag, *Accessibility for Everyone*
- Sarah Horton and Whitney Quesenbery, *A Web for Everyone*
- Regine Gilbert, *Inclusive Design for a Digital World*
- U.S. Section 508 standards and Section508.gov guidance
- European standard EN 301 549 and the European Accessibility Act
- Government accessibility guidance (e.g., UK GDS accessibility manual)
- WebAIM, research and articles including the annual accessibility analyses
