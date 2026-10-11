# 8.7 Smíðakerfi og afurðastjórnun

## Yfirlit og tilgangur

Smíðin er þar sem frumkóði þinn verður að einhverju sem þú getur afhent. Sérhver leiðsla í kafla 8.1 byrjar hér: áður en þú getur prófað, skannað, sett upp eða eflt nokkuð þarf smíðakerfi að breyta tré frumskráa í áþreifanlegan grip, þýdda tvíundaskrá, pakka, gámamynd eða búnt af kyrrstæðum eignum. Ef það fyrsta skref er hægt, óstöðugt eða óendurtakanlegt erfir hvert skref á eftir skaðann. Smíði sem framleiðir ólíkt úttak á tveimur vélum grefur undan hverju prófi sem þú keyrir og hverju samþykki sem þú safnar, því það sem þú staðfestir er ekki sannanlega það sem þú afhendir.

Þessi kafli fjallar um það fyrsta skref og úttak þess: smíðakerfið sem býr til gripi og afurðastjórnunina sem geymir, útgáfumerkir, tryggir og eflir þá. Hann er viljandi þrengri en kafli 8.1, sem nær yfir alla leiðslu samfelldrar samþættingar og samfelldrar afhendingar (CI/CD). Hér er viðfangsefnið smíðin sjálf og gripirnir sem hún gefur frá sér. Hann er viðbót við kafla 2.10 um hugbúnaðarstillingastjórnun, sem stýrir hvernig þú rekur og stjórnar inntökunum, og kafla 2.18 um ósjálfstæða- og aðfangakeðjustjórnun, sem stýrir þriðja aðila kóðanum sem þú dregur inn. Smíðin er þar sem þessi inntök mætast: frumkóði þinn, ósjálfstæði og stillingar renna allt saman í eitt óbreytanlegt úttak.

Fyrir stór teymi er það sem er í húfi áþreifanlegt. Þegar hundruð verkfræðinga bíða eftir margra mínútna smíðum oft á dag dvergar samanlagður tapaður tími nær allan annan verkfræðikostnað. Þegar gripir eru breytanlegir, órakir eða endursmíðaðir fyrir hvert umhverfi taparðu getunni til að segja með vissu hvað keyrir í framleiðslu. Í fyrirtækja- og opinberu umhverfi er sú rekjanleiki ekki valkvæður. Úttektaraðilar og öryggisfulltrúar þurfa sönnunargögn um að tvíundaskráin í framleiðslu kom frá rýndum frumkóða, smíðuð af traustu kerfi, með skráðri vörsluslóð. Agaðar smíða- og afurðavenjur breyta þeim sönnunargögnum í aukaafurð venjulegrar vinnu frekar en óðagot fyrir hverja úttekt.

## Meginreglur

- Smíðin er fyrsta skref afhendingar: líttu á hraða hennar og réttleika sem framleiðsluáhyggjuefni.
- Stefndu að endurtakanlegum og, þar sem framkvæmanlegt, lokuðum smíðum: sömu inntök, sama úttak, í hvert sinn.
- Smíðaðu grip einu sinni, efldu síðan nákvæmlega þann grip yfir umhverfi.
- Gerðu gripi óbreytanlega og innihaldsvistfangsbundna og útgáfumerktu þá á marktækan hátt.
- Geymdu gripi í stýrðu safni með varðveislu, aðgangsstýringu og uppruna.
- Notaðu skyndiminni ótæpilega, en líttu á skyndiminnið sem öryggismörk, ekki bara hraðabragð.
- Fangaðu uppruna, undirskriftir og efnislista við smíði, ekki eftir á.

## Ráðleggingar

### Líttu á smíðina sem fyrsta skref afhendingar

Smíðakerfi þitt eru framleiðsluinnviðir og þú ættir að fjármagna og viðhalda því þannig. Hröð, rétt smíði grips er grunnurinn sem CI/CD (kafli 8.1) hvílir á. Þegar teymi líta á smíðina sem eftirþanka, haug af skeljaskriftum sem enginn á, borga þau fyrir það í óstöðugum leiðslum, dularfullum „virkar á minni vél“ göllum og hægri endurgjöf sem rýrir allt verkfræðiflæðið sem lýst er í 11. hluta. Gefðu smíðinni eiganda, skilgreiningu geymda í útgáfustýringu við hlið kóðans (kafli 2.14 um hirslugerð) og sama rýniaga og öll önnur mikilvæg kerfi.

### Gerðu smíðar endurtakanlegar og, þar sem þú getur, lokaðar

[Endurtakanleg smíði](https://en.wikipedia.org/wiki/Reproducible_builds) framleiðir bita-fyrir-bita eins úttak úr sama frumkóða, svo hver sem er geti endursmíðað sjálfstætt og staðfest að gripur passi við frumkóða sinn. Þetta er eiginleikinn sem leyfir þér að treysta að tvíundaskrá hafi ekki verið átt við milli innritunar og útsetningar. Að komast þangað þýðir að útrýma uppsprettum ófyrirsjáanleika: innfelldum tímastimplum, algildum skráarslóðum, slembiröð í smíðaröð og netsóknum sem niðurstöður reka með tímanum.

Lokuð smíði fer lengra með því að lýsa yfir öllum inntökum fyrirfram og keyra í einangruðu umhverfi sem nær ekki til netsins eða umhverfisástands hýslans. Ekkert fer inn í smíðina nema það sem þú lýstir yfir: festar verkfærakeðjuútgáfur, fest ósjálfstæði, skýrar frumskrár. Lokun er það sem gerir endurtakanleika áreiðanlegan frekar en heppilegan. Full lokun hefur raunverulegan kostnað í verkfærum og aga, svo líttu á hana sem stefnu frekar en tvíundagildi. Jafnvel að hluta framfarir, að festa þýðandaútgáfuna þína, að hafa ósjálfstæði innanborðs eða læsa þeim, að fjarlægja tímastimpla, kaupa þér mest af traustinu fyrir brot af fyrirhöfninni.

### Leystu ósjálfstæði ákvörðunarbundið með læsiskrám

Sérhver smíði dregur inn þriðja aðila kóða og hvernig þú leysir hann ræður hvort smíðin er ákvörðunarbundin. [Læsiskrá](https://en.wikipedia.org/wiki/Lock_file) skráir nákvæma leysta útgáfu og dulritunarkjötkássu hvers beins og afleidds ósjálfstæðis, svo smíði eftir mánuði leysist í nákvæmlega sama gráf. Innritaðu læsiskrána, líttu á breytingar á henni sem rýnanlega atburði og staðfestu kjötkássur við hverja sókn svo breyttur andstreymispakki geti ekki læðst inn óséður. Þetta er smíðatímaandlit aðfangakeðjuagans í kafla 2.18. Án læsiskrár segir „hún smíðaðist í gær“ þér ekkert um hvað hún mun smíða í dag, því fljótandi útgáfusvið getur hljóðlega dregið nýja útgáfu eða árásaraðili getur gefið út illkvittna.

### Notaðu stigvaxandi smíðar og skyndiminni, staðbundið og fjarlægt

Enginn ætti að endursmíða það sem hefur ekki breyst. Stigvaxandi smíðar rekja hvaða inntök fæða hvaða úttök og endursmíða aðeins hlutana sem breyting hefur áhrif á. Smíðaskyndiminni geymir úttök fyrri vinnu lyklað á kjötkássu inntaka þeirra, svo óbreytt skotmark er sótt í stað þess að vera endurreiknað. Staðbundið skyndiminni flýtir lykkju eins forritara. Fjarlægt eða dreift smíðaskyndiminni deilir niðurstöðum yfir allt teymið og CI-flotann, svo sá fyrsti sem smíðar tiltekið inntak borgar kostnaðinn og allir aðrir fá skyndiminnisgrip. Á stórri einstofnshirslu er þetta munurinn á tíu mínútna smíði og tíu sekúndna.

Ávinningurinn er endurgjafarhraði forritara, sem er ein áhrifamesta fjárfesting sem þú getur gert. Hröð, rétt endurgjöf heldur verkfræðingum í flæði og styttir lykkjuna milli þess að skrifa kóða og að vita hvort hann virkar. Gættu réttleika skyndiminnisins vandlega samt: skyndiminnislykill sem sleppir raunverulegu inntaki (umhverfisbreytu, verkfæraútgáfu) framleiðir úrelt niðurstöður sem eru gríðarlega erfiðar að aflúsa. Skyndiminnið er aðeins jafn traust og fullkomleiki kjötkássunar inntaka þess.

### Veldu smíðaverkfæri sem passa stærð þinni

Smíðaverkfæri sitja á litrófi. Í létta endanum líkana [Make](https://en.wikipedia.org/wiki/Make_(software)) og málabundin verkfæri einfalt ósjálfstæðagráf og nægja fyrir eina þjónustu eða litla hirslu. Í miðjunni bæta vistkerfisverkfæri eins og Gradle og Maven fyrir Java-heiminn, eða staðlaðar verkfærakeðjur fyrir Go, Rust og JavaScript, við ósjálfstæðaleysingu og venjum. Í þunga endanum líkana gröfbundin kerfi eins og [Bazel](https://en.wikipedia.org/wiki/Bazel_(software)) og svipuð einstofnssmíðaverkfæri alla smíðina sem fínkorna, lokað [stefnt órásargraf](https://en.wikipedia.org/wiki/Directed_acyclic_graph) skotmarka, sem gerir nákvæma stigvaxandi smíði, fjarlægt skyndiminni og fjarlæga keyrslu mögulega yfir stóran kóðagrunn.

Þyngri verkfæri borga sig þegar þú átt mörg samtengd verkefni, stóra einstofnshirslu (kafli 2.14) eða smíðatíma sem hamla teymum þínum. Þau kosta raunverulega fjárfestingu: brattari lærdómsferil, flutningsfyrirhöfn og sérstakt teymi til að viðhalda smíðaskilgreiningum. Taktu ekki upp Bazel-flokks verkfæri því það er í tísku. Taktu það upp þegar smíðagráfið þitt er nógu stórt til að fínkorna skyndiminni og samhliða vinnsla endurheimti meiri verkfræðitíma en verkfærið kostar í rekstri. Fyrir flest lítil og meðalstór kerfi er gott vistkerfisverkfæri með fjarlægu skyndiminni kjörstaðurinn.

### Geymdu gripi í stýrðu safni

Þegar þú hefur smíðað grip þarf hann heimili. [Afurðasafn](https://en.wikipedia.org/wiki/Software_repository) (einnig kallað skrásetning) geymir pakka, gámamyndir og tvíundaskrár þínar með útgáfumerkingu, aðgangsstýringu og lýsigögnum. Það er mótvægi frumkóðasafns þíns: frumkóði inn, gripir út, hvort tveggja stýrt. Gott safn gefur þér einn traustan stað til að birta og sækja innri gripi, miðlar og geymir ytri í skyndiminni svo þú sért ekki að ná til opinbera internetsins við hverja smíði og skráir hver birti hvað og hvenær. Gámamyndir hafa eigin skrásetningarvenjur og aðrar pakkategundir hafa sínar, en aginn er sá sami: ekkert keyrir í framleiðslu sem kom ekki úr stýrðri, aðgangsstýrðri geymslu.

### Útgáfumerktu gripi og gerðu þá óbreytanlega og innihaldsvistfangsbundna

Gefðu hverjum grip marktæka útgáfu. [Merkingarfræðileg útgáfumerking](https://en.wikipedia.org/wiki/Software_versioning) (major.minor.patch) miðlar eðli breytingar til notenda: aðalhækkun gefur til kynna brjótandi breytingu, undirhækkun bætir við samhæfum eiginleikum, bótarhækkun lagar galla. Samhliða mannlæsilegu útgáfunni skaltu auðkenna hvern grip með dulritunarkjötkássu innihalds hans, svo hann sé innihaldsvistfangsbundinn. Innihaldsvistfang, oft kallað kjötkássa, er fingrafar sem breytist ef eitt bæti breytist, sem leyfir þér að vísa í nákvæman grip ótvírætt og greina hvers kyns átroðning.

Gerðu birta gripi óbreytanlega: þegar útgáfa er birt breytist hún aldrei. Að birta aftur önnur bæti undir sömu útgáfu er aðfangakeðjuhætta og aflúsunarmartröð, því tveir menn geta haldið „útgáfu 1.4.2“ og haft ólíkan hugbúnað. Breytanleg merki eins og „latest“ eru þægileg mönnum en verða alltaf að leysast, fyrir allt sem skiptir máli, í tiltekna óbreytanlega kjötkássu sem þú skráir. Settu upp eftir kjötkássu, ekki fljótandi merki, svo það sem þú prófaðir sé sannanlega það sem þú keyrir.

### Smíðaðu einu sinni, efldu alls staðar

Smíðaðu grip einu sinni, færðu síðan sama grip gegnum umhverfi þín: þróun, millisvið, framleiðslu. Þessi „smíðaðu einu sinni, efldu alls staðar“ regla er mikilvægasta einstaka afurðastjórnunarvenjan. Ef þú endursmíðar fyrir hvert umhverfi hefurðu hent tryggingunni þinni um að prófaði gripurinn sé sá útsetti, því hver endursmíði getur dregið ólíkt ósjálfstæði eða keyrt á örlítið ólíkri vél. Efling er lýsigagnaaðgerð: þú merkir þegar smíðaða, þegar prófaða kjötkássu sem samþykkta fyrir næsta umhverfi og þú stillir hana fyrir það umhverfi gegnum utanvið stillingar (kafli 2.10) frekar en með endursmíði. Þetta heldur tvíundaskránni fastri og stillingunni breytilegri, sem er nákvæmlega aðgreiningin sem þú vilt fyrir bæði áreiðanleika og úttektarhæfni.

### Fangaðu uppruna, undirritaðu gripi og búðu til SBOM

Við smíði skaltu skrá hvaðan gripurinn kom og sanna að ekki hafi verið átt við hann. Uppruni er undirrituð yfirlýsing um hvernig gripur var smíðaður: hvaða frumkóðainnritun, hvaða smiður, hvaða inntök. Að undirrita grip leyfir notendum að staðfesta áreiðanleika og heilleika áður en þeir keyra hann og að staðfesta undirskriftir við útsetningu lokar lykkjunni. [Hugbúnaðarefnisskrá](https://en.wikipedia.org/wiki/Software_supply_chain) (SBOM), fullkomin skrá yfir íhluti og ósjálfstæði innan grips, leyfir þér að svara „erum við fyrir áhrifum?“ innan mínútna þegar nýr veikleiki er upplýstur, frekar en að eyða dögum í að grafa gegnum smíðaskrár.

Rammar eins og SLSA (Supply-chain Levels for Software Artifacts) gefa þér stigskipt líkan fyrir smíðatímaheilleika: hærri stig krefjast lokaðra, einangraðra smíða og óbrenglanlegs uppruna. Búðu til allt þetta í smíðinni, þar sem upplýsingarnar eru áreiðanlegar og ódýrar að safna, ekki endurbyggðar eftir á þegar það er dýrt og óáreiðanlegt. Þessi vinna þjónar beint öruggum hugbúnaðarþróunarlífsferli kafla 4.9 og aðfangakeðjuáhyggjum kafla 2.18.

### Tryggðu skyndiminnið og stýrðu varðveislu og kostnaði

Sameiginlegt smíðaskyndiminni eru sameiginleg traustmörk. Ef árásaraðili getur skrifað eitraða færslu keyrir hver notandi sem sækir hana í hættu kóða og hraðaforskotið verður árásarflötur. Verndaðu skyndiminnið með auðkenningu, afmarkaðu skrifaðgang þröngt (oft aðeins traust CI, aldrei fartölvur forritara) og gakktu úr skugga um að skyndiminnislyklar kjötkássi hvert raunverulegt inntak svo eitruð eða úrelt færsla geti ekki dulbúist sem lögmæt. Líttu á skyndiminniseitrun sem raunverulegt ógnarlíkan, sérstaklega fyrir fjarlæg skyndiminni deild yfir teymi.

Gripir safna líka kostnaði. Gámamyndir og smíðaúttök eru stór og ótakmarkað skrásetningarsafn vex þar til geymslureikningar og hæg uppflettingar neyða málið. Skilgreindu varðveislustefnur: geymdu hvern framleiðsluefldan grip og allt sem keyrandi kerfi vísar í, fyrndu gamlar þróunar- og sameiningarbeiðnasmíðar sjálfvirkt og skráðu hvað þú eyddir. Markmiðið er geymsla sem heldur því sem þú þarft fyrir endurtakanleika og úttekt á meðan hún losar sig við hávaðann, á kostnaði sem þú velur meðvitað frekar en einum sem kemur þér á óvart.

## Málamiðlanir: kostir og gallar

| Ákvörðun | Kostir | Gallar |
|---|---|---|
| Þungt gröfbundið smíðaverkfæri (Bazel-flokks) | Fínkorna stigvaxandi smíði, fjarlægt skyndiminni og keyrsla, skalast að risastórum einstofnshirslum | Brattur lærdómsferill, flutningskostnaður, þarfnast sérstaks smíðateymis |
| Létt smíðaverkfæri (Make, málabundin) | Einfalt, lítil yfirbygging, fljótlegt að taka upp | Léleg stigvaxandi smíði og skyndiminni í stærð, veik lokun |
| Fjarlægt/dreift smíðaskyndiminni | Deildar niðurstöður, dramatískur hraðaaukning yfir flotann | Skyndiminniseitrunarflötur, réttleiki veltur á fullkominni inntakakjötkássun |
| Fullkomlega lokaðar smíðar | Áreiðanlegur endurtakanleiki, sterkur uppruni | Raunverulegur verkfæra- og agakostnaður, erfiðari staðbundin vinnuflæði |
| Smíða einu sinni, efla alls staðar | Prófaði gripurinn er sá afhenti, hrein úttektarslóð | Krefst utanvið stillinga og agaðrar eflingar |
| Óbreytanlegir, innihaldsvistfangsbundnir gripir | Skemmdavarin, ótvíræðar tilvísanir | Minna þægilegt en fljótandi merki, meiri geymsla að stýra |
| Löng gripavarðveisla | Full endurtakanleiki og úttektarsaga | Geymslukostnaður, hægari uppflettingar án hreinsunarstefnu |

Endurtekna spennan er milli hraða og trausts. Skyndiminni, sameiginlegir smíðaflotar og fljótandi merki gera allt smíðar hraðari og þægilegri og hvert þeirra, notað af kæruleysi, veikir getu þína til að segja nákvæmlega hvað þú smíðaðir og sanna að ekki hafi verið átt við það. Leystu það með því að gera traustu leiðina að hröðu leiðinni. Fullkomin inntakakjötkássa gerir skyndiminnið bæði hratt og rétt. Að setja upp eftir kjötkássu er jafn fljótlegt og eftir merki og langtum öruggara. Að búa til SBOM í smíðinni kostar sekúndur og sparar daga. Þú þarft sjaldan að velja hraða fram yfir heilleika ef þú verkfræðir heilleikann inn í hröðu leiðina frá upphafi.

## Spurningar til að ræða með teyminu

1. **Getum við endursmíðað framleiðslugrip síðasta ársfjórðungs í dag og fengið sömu bæti, og ef ekki, hvað vantar?** Þetta er hvassasta prófið á smíðaaga ykkar, því endurtakanleiki veltur á föstum verkfærakeðjum, læstum ósjálfstæðum og útrýmdum ófyrirsjáanleika sem vinna öll saman. Veldu tiltekinn grip sem var afhentur fyrir nokkrum mánuðum og reyndu í raun að endursmíða hann úr skráðu frumkóðainnrituninni. Það sem þú lærir af tilrauninni er verðmætara en nokkurt stefnuskjal: kannski flaut ósjálfstæðissvið, kannski var þýðandaútgáfan aldrei fest, kannski er tímastimpill bakaður inn. Götin sem þú finnur eru endurtakanleikabakslag þitt og að loka þeim er það sem leyfir þér að treysta að það sem þú úttektir sé það sem þú keyrir, sem skiptir gríðarlegu máli í regluverkuðu og opinberu umhverfi þar sem sú vörsluslóð er lagakrafa.

2. **Smíðum við hvern grip einu sinni og eflum hann, eða endursmíðum við fyrir hvert umhverfi, og hvernig myndum við sanna hvort?** Mörg teymi trúa að þau efli einn grip en uppgötva, þegar þau líta náið, að millisvið og framleiðsla ræsa hvort sína nýju smíði með lúmskt ólíkum inntökum. Raktu eina raunverulega útgáfu frá innritun til framleiðslu og staðfestu hvort nákvæmlega sama kjötkássan fór gegnum hvert umhverfi eða hvort ný bæti urðu til á leiðinni. Ef þú finnur endursmíði hefurðu fundið stað þar sem prófunartryggingar þínar eru veikari en þú hélst, því prófaði gripurinn og útsetti gripurinn eru ekki sannanlega eins. Lagfæringin, að færa stillingar út svo tvíundaskráin haldist föst á meðan stillingar breytast, borgar sig bæði í áreiðanleika og langtum hreinni úttektarsögu.

3. **Ef mikilvægur veikleiki væri tilkynntur í algengu bókasafni á morgun, hve hratt gætum við talið upp hvern grip sem inniheldur það?** Þessi spurning prófar hvort smíðatímauppruna- og SBOM-venja ykkar er raunveruleg eða metnaðarfull. Þegar víðnotaður íhlutur reynist nýtanlegur eru skipulagsheildirnar sem jafna sig á klukkustundum þær sem búa til efnisskrá við smíði og geyma hana með hverjum grip. Þær sem jafna sig á vikum eru að grafa gegnum smíðaskrár og taka viðtöl við verkfræðinga. Gakktu gegnum sviðsmyndina áþreifanlega með bókasafni sem þú reiðir þig í raun á og tímasettu hve langan tíma svarið tæki í dag. Bilið milli þess tíma og „mínútna“ er bein mæling á aðfangakeðjuútsetningu þinni og það tengist beint öruggu þróunarlífsferilsvinnunni í kafla 4.9.

4. **Hve miklum verkfræðitíma kosta smíðar okkar á dag og hver eru viðskiptarökin fyrir að gera þær hraðari?** Smíðatöf er skattur sem sérhver verkfræðingur borgar á hverja breytingu og í stærð stórs teymis er auðvelt að vanmeta samanlagða upphæðina því engin ein bið finnst dýr. Að samþykkja að mæla hana breytir óljósri kvörtun í tölu sem þú getur vegið gegn kostnaði fjarlægs skyndiminnis, betri stigvaxandi smíði eða þyngri smíðaverkfæra. Komdu með miðgildi og versta tilfelli staðbundinna og CI-smíðatíma, fjölda smíða á dag og heiðarlegt mat á því hve oft hæg smíði ýtir einhverjum úr flæði í samhengisskipti. Sjónarmiðið á móti er að hraðari smíðar eru ekki ókeypis: fjarlægt skyndiminni og dreifð keyrsla bæta við innviðum til að reka og tryggja og þyngri verkfæri bæta við viðhaldsteymi. Fyrir fyrirtæki eða opinbera skipulagsheild skaltu telja afkasta- og móralskostnað hægrar endurgjafar yfir mörg teymi, sem dvergar yfirleitt innviðareikninginn og er nákvæmlega rammunin sem forysta fjármagnar nú þegar.

5. **Hver getur skrifað í sameiginlega smíðaskyndiminnið okkar og hvað kemur í veg fyrir að eitruð færsla nái framleiðslu?** Sameiginlegt skyndiminni skiptir hraðasigri fyrir ný traustmörk og sami búnaður sem leyfir niðurstöðu eins verkfræðings að þjóna öllum flotanum leyfir einni spilltri eða illkvittinni færslu að stefna öllum í hættu sem sækja hana. Fyrir stórt teymi er sprengisvæðið öll skipulagsheildin, svo þetta á skilið yfirvegaða ákvörðun frekar en hvað sem sjálfgefin gildi verkfæris eru. Komdu með lista yfir hver og hvað hefur skrifaðgang að hverju skyndiminni, hvort skrif eru afmörkuð við traust CI frekar en fartölvur forritara og hvort skyndiminnislyklar ykkar kjötkássa hvert raunverulegt inntak svo úrelt eða eitruð færsla geti ekki dulbúist sem lögmæt. Spennan er að þéttustu stýringarnar hægja á þægilegu leiðinni þar sem forritarar ýta skyndiminnisfærslum úr eigin vélum. Í fyrirtækja- og opinberu umhverfi skaltu líta á skyndiminniseitrun sem skýra ógn í aðfangakeðjulíkani þínu og krefjast sömu aðgangsstýringa, skráningar og rýni og þú beitir á hvert annað framleiðslukerfi sem getur sprautað kóða inn í útgáfu.

6. **Á hvaða punkti réttlætir smíðagráf okkar þyngri verkfæri og hvernig munum við vita að við höfum farið yfir hann?** Valið milli léttra vistkerfisverkfæris og gröfbundins kerfis eins og Bazel er ein af dýrari og erfiðari-að-afturkalla ákvörðunum á þessu sviði, því að flytja stóran kóðagrunn í fínkorna smíðaskilgreiningar kostar mánuði og sérstakt teymi. Að ákveða þröskuldinn fyrirfram heldur þér frá því að taka upp flækju sem þú þarft ekki því hún er í tísku, eða að loða við létt verkfæri langt eftir að smíðatímar þínir hamla hverju teymi. Komdu með stærð og samtengingu smíðagráfsins þíns, núverandi smíða- og skyndiminnisárangursmælikvarða og raunhæft mat á flutnings- og viðvarandi viðhaldskostnaði gegn verkfræðitímanum sem verkfærið myndi endurheimta. Togið á móti er að þung verkfæri skila nákvæmri stigvaxandi smíði og fjarlægri keyrslu sem ekkert annað jafnast á við í stærð, en aðeins ef gráfið ykkar er sannarlega nógu stórt til að endurgreiða það. Fyrir stórt fyrirtæki eða stofnun skaltu líka vega hvort lokun og upprunaábyrgðir verkfærisins hjálpi til við að fullnægja úttektar- og aðfangakeðjukröfum, sem getur breytt útreikningnum umfram hráan hraða.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með örlítið teymi og ekkert svigrúm fyrir smíðainnviði skaltu halda því léttu: notaðu málabundin smíðaverkfæri, taktu upp læsiskrár frá fyrsta degi og settu upp gámamyndir eftir kjötkássu frekar en „latest“ merkinu, þar sem þessar venjur kosta nánast ekkert og spara þér heilan flokk „virkar á minni vél“ sársauka síðar. Stattu gegn þungum gröfbundnum smíðaverkfærum. Knappasta auðlind þín er athygli verkfræðinga. Fjarlægt smíðaskyndiminni er eina uppfærslan sem vert er að seilast í þegar smíðar fara að skríða yfir nokkrar mínútur.

**Lítið fyrirtæki.** Án sérstaks smíðaverkfræðings skaltu halla þér að stýrðum þjónustum frekar en að reka eigin afurðainnviði: hýst skrásetning og innbyggt skyndiminni CI-veitunnar gefa þér útgáfumerkingu, varðveislu og aðgangsstýringu án vettvangsteymis. Rammaðu valið sem kaup yfir smíði, settu sjálfvirka fyrningarstefnu svo geymslukostnaður haldist fyrirsjáanlegur og gakktu úr skugga um að grunnatriðin séu til staðar, læst ósjálfstæði og óbreytanlegar, kjötkássufestar útsetningar, því þau vernda þig jafnvel þegar enginn fylgist með leiðslunni í fullu starfi.

**Stórfyrirtæki.** Yfir mörg teymi er vandinn samræmi: sameiginlegur, eigin smíðavettvangur, sameiginlegt afurðasafn og framfylgdir staðlar fyrir læsiskrár, undirritun, SBOM og smíða-einu-sinni-efla svo enginn hópur finni upp óáreiðanlega leiðslu aftur. Fjárfestu í fjarlægu skyndiminni og, þar sem smíðagráfið réttlætir það, gröfbundnum verkfærum og líttu á skyndiminnið sem stýrð traustmörk með afmörkuðum skrifaðgangi og úttektarskráningu. Stýrðu gripum sem stýrðri landareign með varðveislustefnum og uppruna svo hver framleiðsluíhlutur rekist til rýnds frumkóða eftir þörfum.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð gera smíðatímaheilleika að reglufylgnikröfu, ekki fínheitum. Samræmdu leiðsluna við stigskiptan ramma eins og SLSA, keyrðu smíðar í einangruðu, netskorðuðu umhverfi úr föstum verkfærakeðjum og miðlaðu þriðja aðila ósjálfstæðum gegnum innra safn sem skannar og samþykkir þau fyrir notkun. Geymdu undirritaðar SBOM og uppruna óbreytanlega í árin sem skjalavörslulög krefjast, settu aðeins upp undirritaða, kjötkássuauðkennda gripi og vertu tilbúinn að votta fyrir úttektaraðilum og almenningi að hugbúnaðurinn í framleiðslu sé nákvæmlega það sem var rýnt og samþykkt.

## Dæmi

**Sprotafyrirtæki.** Fimmtán manna sprotafyrirtæki sem rekur litla einstofnshirslu byrjar á málabundnum smíðaverkfærum og hraðri endurgjöf, sem er rétta valið í þeirra stærð. Eftir því sem þau vaxa skríða smíðatímar yfir fimm mínútur og verkfræðingar fara að skipta um samhengi á meðan þeir bíða. Frekar en að stökkva í þungt gröfbundið smíðaverkfæri bæta þau við fjarlægu smíðaskyndiminni deilt milli véla forritara og CI, sem skerðir flestar smíðar í sekúndur því óbreytt skotmörk eru sótt, ekki endursmíðuð. Þau taka upp læsiskrár fyrir hvert mál, setja upp gámamyndir eftir kjötkássu í stað „latest“ merkisins og kveikja á sjálfvirkri fyrningu fyrir myndasmíðar sameiningarbeiðna svo skrásetningarreikningurinn haldist flatur. Öll fyrirhöfnin tekur nokkrar vikur og kaupir til baka klukkustundir af verkfræðitíma á hverjum degi.

**Stórfyrirtæki.** Alþjóðlegt fjármálaþjónustufyrirtæki rekur stóra einstofnshirslu yfir hundruð verkfræðinga og tekur upp gröfbundið smíðakerfi með fjarlægu skyndiminni og fjarlægri keyrslu, því í þeirra stærð endurheimtir fínkorna stigvaxandi smíði langtum meiri verkfræðitíma en smíðateymið kostar. Sérhver gripur er smíðaður lokað í einangruðu umhverfi, undirritaður og birtur í stýrðri skrásetningu með SBOM og undirrituðum uppruna áföstum. Útsetningar gerast eftir innihaldskjötkássu og stefnuvél neitar að keyra hverja mynd þar sem undirskrift staðfestist ekki. Gripir eru efldir, aldrei endursmíðaðir, frá millisviði til framleiðslu, svo tvíundaskráin sem stóðst prófun er sannanlega sú sem þjónar viðskiptavinum. Þegar úttektaraðilar biðja um að rekja framleiðsluíhlut til rýnds frumkóða er vörsluslóðin fyrirspurn, ekki rannsókn.

**Hið opinbera.** Landsbundið skattyfirvald sem nútímavæðir kerfi sín lítur á aðfangakeðjuheilleika við smíði sem reglufylgnikröfu og samræmir leiðslu sína stigskiptum ramma eins og SLSA. Smíðar keyra í einangruðu, netskorðuðu umhverfi úr föstum verkfærakeðjum og læstum ósjálfstæðum, svo úttakið er endurtakanlegt og sjálfstætt sannreynanlegt. Sérhver gripur ber undirritaða SBOM og uppruna, geymda óbreytanlega árum saman til að uppfylla skjalavörslulög. Þriðja aðila ósjálfstæði eru miðluð gegnum innra safn sem skannar og samþykkir þau áður en nokkur smíði getur notað þau, sem heldur óskoðuðum kóða alveg utan netsins. Því stofnunin setur aðeins upp undirritaða, eflda gripi auðkennda með kjötkássu getur hún vottað fyrir eftirlitsaðilum og almenningi að hugbúnaðurinn sem vinnur úr framtölum borgara sé nákvæmlega það sem var rýnt og samþykkt.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun smíða- og afurðaaga birtist fyrst sem endurheimtur verkfræðitími. Hægar smíðar skattleggja hvern verkfræðing á hverja breytingu og kostnaðurinn safnast yfir stóra skipulagsheild: að raka mínútur af smíði sem keyrir þúsundir sinnum á dag endurheimtir mannár árlega og, erfiðara að magnsetja en jafn raunverulegt, heldur verkfræðingum í flæði í stað samhengisskipta. Fjarlægt skyndiminni og góð stigvaxandi smíði borga sig oft á vikum. Endurtakanlegir gripir, smíðaðir einu sinni og efldir fækka heilum flokki „það virkaði í millisviði“ atvika, sem lækkar bilunarhlutfall breytinga og meðaltíma til endurheimtar, afhendingarmælikvarðana sem leiðtogar fylgjast þegar með.

Stærri, minna sýnilega ávöxtunin er áhættuminnkun. Undirritaðir gripir, SBOM og uppruni breyta aðfangakeðjuatviki úr marga vikna neyðarástandi í afmarkað viðbragð á klukkustundum og þeir breyta úttektum úr neyðaræfingu í fyrirspurn. Í regluverkuðu og opinberu samhengi er sá rekjanleiki forsenda þess að starfa yfirleitt, svo fjárfestingin er ekki valkvæð heldur skipulagsleg. Heildareignarkostnaður rennur hinn veginn þegar þú vanrækir þetta: breytanlegir gripir og óendurtakanlegar smíðar safnast í landareign sem enginn getur gert fulla grein fyrir, geymsla vex ótakmarkað án varðveislustefnu og sérhver úttekt og sérhvert atvik kostar meira en það ætti að gera. Til að færa rök við forystu skaltu tengja smíðahraða við verkfræðiafköst og tengja afurðaheilleika við úttektarkostnað og brotaútsetningu, hvort tveggja sem þeir fjármagna nú þegar.

## Andmynstur og gildrur

- **Endursmíði fyrir hvert umhverfi:** að framleiða fersk bæti fyrir millisvið og framleiðslu og henda tryggingunni um að prófaði gripurinn sé sá útsetti.
- **Útsetning eftir fljótandi merki:** að keyra „latest“ eða breytanlegt merki í stað óbreytanlegrar kjötkássu, svo það sem keyrir er ófyrirsjáanlegt og órekjanlegt.
- **Engin læsiskrá:** fljótandi útgáfusvið sem láta smíð hljóðlega draga ólík eða illkvittin ósjálfstæði með tímanum.
- **Ófullkomnir skyndiminnislyklar:** að sleppa raunverulegu inntaki úr skyndiminnislyklinum, sem framleiðir úrelt niðurstöður sem sóa dögum í aflúsun.
- **Óvarið sameiginlegt skyndiminni:** að leyfa ótraustum rithöfundum að eitra fjarlægt skyndiminni svo notendur sæki og keyri spillt úttök.
- **Óákvörðunarbundnar smíðar:** innfelldir tímastimplar, algildar slóðir og óföst verkfæri sem láta úttak vera breytilegt og gera staðfestingu ómögulega.
- **Að taka upp þung verkfæri of snemma:** að taka á sig Bazel-flokks flækju áður en smíðagráfið er nógu stórt til að réttlæta hana.
- **SBOM og uppruni sem eftirþanki:** að endurbyggja aðfangakeðjulýsigögn eftir smíðina, þegar það er dýrt og óáreiðanlegt, í stað þess að búa þau til í smíðinni.
- **Ótakmörkuð varðveisla:** að fyrna aldrei gamla gripi þar til geymslukostnaður og hægar uppflettingar neyða skelfda hreinsun.

## Þroskalíkan

- **Stig 1, Upphaf:** Smíðar eru ad hoc skriftur sem enginn á, oft keyrðar úr vélum forritara. Úttak er óákvörðunarbundið, ósjálfstæði fljóta án læsiskráa, gripir eru endursmíðaðir fyrir hvert umhverfi og settir upp eftir breytanlegu merki og ekkert sameiginlegt skyndiminni, engin undirritun og enginn efnislisti er til.
- **Stig 2, Þróun:** Sum teymi hafa fært smíðar í CI úr innritaðri skilgreiningu og tekið upp læsiskrár, en vinnubrögð eru ósamræmd um skipulagsheildina. Gripir kunna að lenda í stýrðu safni með grunnútgáfumerkingu og staðbundið eða einfalt fjarlægt skyndiminni flýtir algengum smíðum, samt gerast enn endursmíðar fyrir hvert umhverfi og uppruni er brotakenndur.
- **Stig 3, Stöðlun:** Endurtakanlegar, að mestu lokaðar smíðar eru skjalfestar og framfylgdar um skipulagsheildina, með föstum verkfærakeðjum og sameiginlegu fjarlægu skyndiminni þar sem lyklar kjötkássa öll raunveruleg inntök. Gripir eru óbreytanlegir, innihaldsvistfangsbundnir, merktir merkingarfræðilega, smíðaðir einu sinni og efldir alls staðar, undirritaðir og afhentir með SBOM. Skyndiminnisaðgangur er stýrður og varðveislustefnum er beitt samræmt yfir teymi.
- **Stig 4, Stjórnun:** Smíðalandareignin er mæld og stýrð gegn grunnlínum. Smíðatímar, skyndiminnisárangurshlutföll, endurgjafartími forritara og geymslukostnaður eru rakin með skýrum markmiðum, afturfarir kalla fram aðgerð og undirskrifta- og upprunastaðfesting er framfylgd við útsetningu svo misheppnuð athugun blokki útgáfu. Aðfangakeðjuheilleiki við smíði er metinn gegn stigskiptum ramma eins og SLSA og tölurnar ráða hvar þú fjárfestir næst.
- **Stig 5, Samhæfing:** Smíða-, skyndiminnis-, afurða- og aðfangakeðjuvenjur eru stöðugt bættar og samþættar um skipulagsheildina. Verkfæri, varðveisla og öryggisstaða aðlagast eftir því sem þú lærir af atvikum og úttektum, fjarlæg keyrsla og skyndiminni eru stillt eftir því sem kóðagrunnurinn þróast og smíðatímaheilleiki er ofinn inn í víðtækari öruggan hugbúnaðarþróunarlífsferil frekar en festur á eftir á.

## Hugmyndir til umræðu

1. Hver er núverandi miðgildi og versta tilfelli staðbundins smíðatíma ykkar og hvað myndi fjarlægt skyndiminni gera fyrir hvort?
2. Hverjir gripa ykkar eru settir upp eftir breytanlegu merki í dag og hvað þyrfti til að setja upp hvern eftir kjötkássu?
3. Hvar réttlætir smíðagráf ykkar þyngri verkfæri og hvar myndu þau verkfæri kosta meira en þau spara?
4. Hver getur skrifað í sameiginlega smíðaskyndiminnið ykkar og hvað kemur í veg fyrir að eitruð færsla nái framleiðslu?
5. Getið þið framleitt undirritaða SBOM fyrir það síðasta sem þið afhentuð og ef ekki, hvert er minnsta skrefið í átt að því?
6. Hver er varðveislustefna ykkar fyrir smíðagripi og hvað kostar geymslan ykkur í dag á móti því sem hún ætti að kosta?

## Helstu atriði

- Smíðin er fyrsta skref afhendingar: fjármagnaðu hraða hennar og réttleika sem framleiðsluáhyggjuefni, því allt niðurstreymis erfir galla hennar.
- Gerðu smíðar endurtakanlegar og, þar sem framkvæmanlegt, lokaðar, með föstum verkfærakeðjum og læsiskrám, svo gripurinn sem þú úttektir sé sannanlega sá sem þú afhendir.
- Notaðu skyndiminni og smíðaðu stigvaxandi, staðbundið og fjarlægt, en kjötkássaðu hvert raunverulegt inntak og tryggðu skyndiminnið, því sameiginlegt skyndiminni eru sameiginleg traustmörk.
- Smíðaðu hvern grip einu sinni, gerðu hann óbreytanlegan og innihaldsvistfangsbundinn, útgáfumerktu hann marktækt og efldu nákvæmlega þann grip yfir umhverfi.
- Búðu til uppruna, undirskriftir og SBOM við smíði og geymdu gripi með varðveislu og aðgangsstýringu, sem breytir aðfangakeðjuheilleika og úttektarviðbúnaði í aukaafurð venjulegrar vinnu.

## Heimildir og frekari lestur

- Jez Humble and David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Titus Winters, Tom Manshreck, and Hyrum Wright (eds.), *Software Engineering at Google: Lessons Learned from Programming Over Time*
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering: How Google Runs Production Systems*
- Peter Smith, *Software Build Systems: Principles and Experience*
- The Open Source Security Foundation, *SLSA: Supply-chain Levels for Software Artifacts* (specification)
- National Institute of Standards and Technology, *Secure Software Development Framework (SSDF), SP 800-218*
- Tom Preston-Werner, *Semantic Versioning Specification (SemVer)*
