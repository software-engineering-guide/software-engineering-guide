# 4.2 Forritaöryggi

## Yfirlit og tilgangur

Forritaöryggi er þar sem óhlutbundnar ógnir mæta áþreifanlegum kóða. Flest innbrot sem rata í fréttir rekja sig til galla á forritalagi: innsprautunar, bilaðs auðkenningarflæðis, afhjúpaðs leyndarmáls eða brotinnar ósjálfstæðiseiningar. Fyrir stór teymi sem afhenda margar þjónustur er erfiði hlutinn ekki að vita að þessir gallar séu til. Hann er að koma í veg fyrir þá samræmt yfir víðfeðman kóðagrunn skrifaðan af þúsundum handa yfir mörg ár.

Fyrir fyrirtæki er forritaöryggi spurning um traust viðskiptavina og regluverksskyldu. Galli í innskráningarflæði eða greiðsluleið getur kveikt svik, sektir og skyldubundna innbrotsupplýsingu. Kerfi hins opinbera standa frammi fyrir sömu tæknilegu áhættu með gögn af meiri hagsmunum: bótahæfi, skattskrár, refsiréttargögn og þjóðarinnviði. Í báðum umhverfum eru forritin framdyrnar og árásaraðilar kanna þær stöðugt og sjálfvirkt.

Þessi kafli nær yfir vinnubrögðin sem halda forritum seigum: að þekkja og verjast algengum veikleikaflokkum, staðfesta inntak og kóða úttak, fá auðkenningu og heimild rétta, stýra leyndarmálum og tryggja hugbúnaðaraðfangakeðjuna sem í auknum mæli ræður raunverulegu árásaryfirborði þínu.

*Sjá einnig:* kafla 4.1 (öryggisgrunn, ógnarmótun og öruggan þróunarlífsferil), kafla 10.3 (opna aðfangakeðju og leyfisveitingar) og kafla 10.2 (SBOM, áhættu og tryggingu).

## Meginreglur

- **Treystu aldrei inntaki.** Líttu á öll gögn sem fara yfir traustmörk sem fjandsamleg þar til þau eru staðfest.
- **Örugg sjálfgefin gildi.** Örugga leiðin ætti að vera auðvelda leiðin. Óörugg hegðun ætti að krefjast yfirvegaðrar, sýnilegrar fyrirhafnar.
- **Bila lokað.** Þegar öryggisathugun getur ekki lokið skaltu neita aðgangi frekar en að leyfa hann.
- **Vörn í dýpt á forritalagi.** Sameinaðu staðfestingu, kóðun, stikuð fyrirspurnir og rammavernd. Reiddu þig ekki á eitt.
- **Lágmarksréttindi fyrir auðkenni og tákn.** Afmarkaðu auðkennisgögn þröngt og láttu þau renna fljótt út.
- **Ósjálfstæði þín eru kóði þinn.** Þú berð ábyrgð á öryggi alls sem þú afhendir, þar á meðal íhluta þriðja aðila og opins hugbúnaðar.
- **Staðlar fram yfir spuna.** Notaðu sannreynda ramma eins og [OWASP](https://en.wikipedia.org/wiki/OWASP) (Open Worldwide Application Security Project) ASVS frekar en að finna upp eigin öryggisstýringar.

## Ráðleggingar

### Þekktu og verðu OWASP Top 10, sannreyndu með ASVS

OWASP Top 10 er grunnlisti iðnaðarins yfir mikilvægustu vefforritaáhættur: bilaða aðgangsstýringu, dulritunarbilanir, innsprautun, óörugga hönnun, öryggisrangstillingu, berskjölduð íhluti, auðkenningarbilanir, gagnaheilleikabilanir, skráningarbilanir og beiðnafölsun frá þjóni (server-side request forgery). Líttu á hann sem skylduþekkingu fyrir hvern verkfræðing, ekki bara regluvörsluviðmið til að skjalfesta.

Fyrir strangan, prófanlegan staðal skaltu taka upp **OWASP Application Security Verification Standard (ASVS)**. ASVS skilgreinir öryggiskröfur á þremur tryggingarstigum, sem gefur þér áþreifanlegar, úttektarhæfar stýringar til að hanna og prófa gegn. Veldu stigið sem hentar áhættu hvers forrits og sannreyndu gegn því.

### Staðfestu inntak og kóðaðu úttak

Innsprautunargallar eru áfram meðal þeirra skaðlegustu einmitt því þeir eru svo auðvelt að innleiða. Verðu með lagskiptum stýringum:

- **Staðfestu inntak** gegn ströngum leyfilistum (væntanleg tegund, lengd, snið, svið). Hafnaðu frekar en að hreinsa þar sem þú getur.
- **Notaðu stikaðar fyrirspurnir** og [undirbúnar yfirlýsingar](https://en.wikipedia.org/wiki/Prepared_statement) fyrir allan gagnagrunnsaðgang. Smíðaðu aldrei SQL með strengjasamtengingu. Notaðu örugga fyrirspurnasmiði og ORM (object-relational mapper) rétt.
- **Kóðaðu úttak** eftir samhengi. HTML, HTML-eigindi, JavaScript, vefslóðir og CSS krefjast hvert ólíkrar kóðunar. Treystu á sjálfvirka umbreytingu rammans og skildu takmörk hennar.
- **Komdu í veg fyrir [skriftuinnsprautun milli vefsvæða](https://en.wikipedia.org/wiki/Cross-site_scripting) (XSS)** með úttakskóðun auk sterkrar Content Security Policy sem annars lags.
- **Komdu í veg fyrir skipana- og sniðmátsinnsprautun** með því að forðast að kalla á skel með ótraustum gögnum og með því að nota rökfræðilaus eða sandkassað sniðmát.

### Fáðu auðkenningu og heimild rétta

Auðkenning sannar hver notandi er. Heimild ræður hvað hann má gera. Hvort tveggja bilar oft, svo fáðu þau rétt.

- Kjóstu rótgróin samskiptaregla: **[OAuth 2.0](https://en.wikipedia.org/wiki/OAuth)** fyrir framseldar heimildir og **[OpenID Connect](https://en.wikipedia.org/wiki/OpenID_Connect) (OIDC)** fyrir auðkenningu. Smíðaðu þau ekki frá grunni.
- Framfylgdu **[fjölþátta auðkenningu](https://en.wikipedia.org/wiki/Multi-factor_authentication) (MFA)**, sérstaklega fyrir forréttinda- og stjórnunaraðgang.
- Geymdu lykilorð aðeins sem söltuð kjötkássa með nútímalegu, hægu, minnisþungu reikniriti (eins og [Argon2](https://en.wikipedia.org/wiki/Argon2) eða [bcrypt](https://en.wikipedia.org/wiki/Bcrypt)). Geymdu eða skráðu aldrei lykilorð í skýrum texta.
- Stýrðu **setum** vandlega: búðu til dulritunarlega sterk tákn, settu secure og HttpOnly kökufána, snúðu við réttindabreytingu og láttu aðgerðalausar setur renna út.
- Framfylgdu **heimild á þjóninum fyrir hverja beiðni** og athugaðu að auðkennda gerandanum tilheyri eða hafi aðgang að tilteknu tilfangi. Biluð heimild á hlutstigi (að nálgast skrá annars notanda með því að breyta auðkenni) er einn algengasti og alvarlegasti API-gallinn.
- Miðlægðu heimildarrökfræði þar sem hagkvæmt er svo stefna sé samræmd og úttektarhæf.

### Stýrðu leyndarmálum og snúðu lyklum

Harðkóðuð leyndarmál í frumkóða eru eilíf orsök innbrota. Byggðu agaðan vana í kringum leyndarmálastjórnun:

- Geymdu leyndarmál í sérstökum leyndarmálastjóra eða hvelfingu, aldrei í frumkóða, stillingarskrám eða umhverfisbreytum sem innritaðar eru í útgáfustýringu.
- Skannaðu innritanir og hugbúnaðarsöfn sjálfvirkt fyrir lekin leyndarmál og hindraðu sameiningar sem kynna þau.
- Snúðu lyklum og auðkennisgögnum reglulega og tafarlaust við hvern grun um afhjúpun. Kjóstu skammlíf, sjálfvirkt útgefin auðkennisgögn fram yfir langlíf, kyrrstæð.
- Beittu lágmarksréttindum á hvert leyndarmál: afmarkaðu það við nákvæmlega það sem það þarf.
- Dulkóðaðu leyndarmál í hvíld og á ferð og úttektaðu aðgang að þeim.

### Tryggðu hugbúnaðaraðfangakeðjuna

Nútímaforrit eru að mestu sett saman úr íhlutum þriðja aðila, sem gerir aðfangakeðjuna að aðalárásaryfirborði.

- Haltu **hugbúnaðarefnisskrá ([SBOM](https://en.wikipedia.org/wiki/Software_bill_of_materials))** fyrir hvert forrit svo þú vitir nákvæmlega hvað þú afhendir og getir brugðist hratt við þegar nýr veikleiki lendir.
- Skannaðu ósjálfstæði samfellt (Software Composition Analysis, eða SCA) og úrbættu þekkta berskjölduð íhluti fljótt.
- Festu og staðfestu ósjálfstæðisútgáfur. Notaðu lásskrár og traust skráningarsöfn.
- Taktu upp **SLSA** (Supply-chain Levels for Software Artifacts) til að auka smíðaheilleika og búðu til **herkomu**vottanir sem lýsa hvernig gripir voru smíðaðir.
- **Undirritaðu gripi** og staðfestu undirskriftir fyrir uppsetningu svo þú getir treyst að það sem keyrir sé það sem þú smíðaðir.
- Tryggðu smíðakerfið sjálft. Brotin CI-leiðsla getur sprautað illgjörnum kóða í hvern niðurstraumsneytanda.

## Málamiðlanir: kostir og gallar

| Ákvörðun | Kostir | Gallar |
|---|---|---|
| Kaupa/taka upp auðkennaveitu (OIDC) | Sannreynd, MFA innbyggt, minni kóði til að tryggja | Söluaðilaháð, samþættingarfyrirhöfn, kostnaður |
| Smíða sérsmíðaða auðkenningu | Full stjórn, ekkert ytra ósjálfstæði | Afar auðvelt að fá rangt, hátt viðhald |
| Ströng leyfilistastaðfesting | Hindrar heila veikleikaflokka | Getur brotið lögmæt jaðartilvik, meiri fyrirhöfn fyrirfram |
| Skammlíf auðkennisgögn | Lítill brotagluggi, sjálfvirk afturköllun | Krefst öflugra útgáfuinnviða |
| Ágengar ósjálfstæðisuppfærslur | Færri þekktir veikleikar | Hræring, hugsanlegar brjótandi breytingar, prófunarbyrði |
| SBOM + undirritun + herkoma | Hröð atvikaviðbrögð, sannanlegt traust | Verkfæra- og ferlafjárfesting, menningarbreyting |

Endurtekna málamiðlunin er fyrirhöfn fyrirfram gegn viðvarandi útsetningu. Að smíða sérsmíðaða auðkenningu eða sleppa ósjálfstæðishreinlæti finnst hraðara í dag og kostar þig gríðarlega síðar. Að taka upp sannreynda staðla og sjálfvirkar aðfangakeðjustýringar kostar fyrirhöfn núna, en breytir ótakmarkaðri, ófyrirsjáanlegri áhættu í stýrða, afmarkaða. Fyrir stór teymi skiptir sjálfvirknimargfaldarinn mestu máli: stýring sem er beitt einu sinni í sniðmáti á troðinni slóð ver hverja þjónustu sem notar það.

## Spurningar til að ræða með teyminu

1. **Hvaða ASVS-stýringar munuð þið baka inn í rammann á troðinni slóð ykkar svo verkfræðingar fái þær ókeypis?** Áhrifamesta hreyfing stórs teymis er að gera örugga leiðina að sjálfgefinni, svo stýring skrifuð einu sinni í sameiginlegum ramma verji hverja þjónustu sem tekur hann upp. Ákveddu hvaða ASVS-kröfur (stikaðar fyrirspurnir, úttakskóðun, öruggir setufánar, heimildarathuganir á þjóninum) eiga heima í sniðmátinu frekar en í minni hvers verkfræðings. Fyrir fyrirtækja- og opinber eignasöfn skaltu líka ákveða hvaða forrit þurfa ASVS stig 2 á móti stigi 3 og tengja það við viðkvæmni gagnanna sem hvert snertir. Komdu með lista yfir þjónustur þínar og merktu hverjar erfa þegar þessi sjálfgefnu gildi og hverjar endurútfæra öryggi í höndunum, því handsmíðuðu eru þar sem innsprautun og biluð aðgangsstýring fela sig. Ef örugg sjálfgefin gildi búa aðeins á wiki-síðu verða þau sleppt undir afhendingarþrýstingi, svo settu þau í kóða.

2. **Hvernig munuð þið finna og laga bilaða heimild á hlutstigi yfir hvert API, ekki bara þau nýju?** Að nálgast skrá annars notanda með því að breyta auðkenni er einn algengasti og alvarlegasti API-gallinn, og hann felur sig í eldri endapunktum sem eru eldri en núverandi staðlar þínir. Heimild á þjóninum á hverri beiðni og hverjum hlut er reglan, en erfiði hlutinn er að sannreyna að hún haldi yfir víðfeðman, ára gamlan kóðagrunn skrifaðan af mörgum höndum. Ákveddu hvort þú miðlægir heimildarrökfræði, bætir við sjálfvirkum prófum sem reyna þvert-leigjenda aðgang eða keyrir markvissa prófun gegn áhættumestu API-unum fyrst. Komdu með skrá yfir endapunkta sem afhjúpa hlutaauðkenni og raðaðu þeim eftir viðkvæmni þess sem þeir skila. Án yfirvegaðrar yfirferðar munt þú halda áfram að afhenda þennan galla og uppgötva hann aðeins þegar rannsakandi eða árásaraðili gerir það.

3. **Hver er áætlun ykkar fyrir næsta útbreidda ósjálfstæðisveikleika: hve fljótt getið þið fundið og plástrað hverja áhrifaða þjónustu?** Þegar mikilvægur galli lendir í vinsælu bókasafni finna fyrirtækin með nákvæma SBOM áhrifaðar þjónustur á klukkustundum á meðan önnur eyða vikum í leit, og sá hraðamunur ræður hve miklum skaða þú tekur. Ákveddu núna hvort þú framleiðir hugbúnaðarefnisskrá fyrir hvern grip, hvort ósjálfstæðisskönnun keyrir í hverri leiðslu og hver á neyðarplástursákvörðunina. Fyrir eftirlitsskylda og opinbera kaupendur eru SBOM og undirrituð herkoma sífellt oftar skilyrði fyrir viðskiptum, svo þessi reiðubúð ver líka tekjur. Komdu með heiðarlegt svar við æfingu: veldu bókasafn sem þú notar víða og tímasettu hve lengi það tekur að telja upp hverja þjónustu sem afhendir það. Ef svarið er mælt í dögum skaltu fjárfesta í skrá og undirritun áður en næsta atvik neyðir þig til þess.

4. **Hvernig munuð þið færa ykkur frá langlífum kyrrstæðum leyndarmálum yfir í skammlíf, sjálfvirkt útgefin auðkennisgögn og hvaða kerfi hindra það í dag?** Harðkóðuð og langlíf leyndarmál eru eilíf innbrotsorsök, og lagfæringin, skammlíf auðkennisgögn útgefin eftir þörfum, byggir á útgáfuinnviðum sem eldri kerfi geta oft ekki notað. Fyrir stórt teymi er hættan ójöfn upptaka: nútímavettvangur snýr lyklum á klukkustundar fresti á meðan eldri þjónusta afhendir enn kyrrstætt gagnagrunnslykilorð í stillingarskrá. Ákveddu hvaða vinnuálög geta neytt leyndarmálastjóra eða vinnuálagsauðkennakerfis núna, hverjar þurfa fjárfestingu fyrst og hver á snúningskeyrsluhandbókina um leið og lykill er grunaður um leka. Komdu með skrá yfir hvert auðkennisgagn í notkun, líftíma þess, sprengjusvæði ef afhjúpað og hvort innritunarskönnun myndi grípa það fyrir sameiningu. Í fyrirtækja- og opinberu umhverfi skaltu tengja þetta við úttekt: endurskoðendur ætlast í auknum mæli til sönnunargagna um snúning, afmarkaðan aðgang og aðgangsskráningu fyrir hvert leyndarmál, og kyrrstætt auðkennisgagn sem þú getur ekki snúið án niðurtíma er niðurstaða sem bíður þess að vera skrifuð upp.

5. **Hvar rekið þið enn heimasmíðaða eða ósamræmda auðkenningu og hver er áætlunin um að sameina á sannreynd samskiptareglur?** Að smíða auðkenningu er ein auðveldasta leiðin til að innleiða lúmska, nýtanlega galla, samt bera flest stór bú að minnsta kosti eitt eldra innskráningarflæði sem er eldra en ákvörðunin um að staðla á OAuth 2.0 og OIDC. Þrýstingurinn sem togast á er raunverulegur: að flytja gamalt flæði teflir núverandi notendum og samþættingum í hættu, á meðan að skilja það eftir heldur verðmiklu skotmarki illa vörðu. Ákveddu hvort þú sameinar á eina auðkennaveitu, framfylgir MFA einsleitt og setur frest til að leggja niður hvert sérsmíðað flæði, eða samþykkir skjalfestar undantekningar með bótastýringum. Komdu með kort af hverri auðkenningarleið í flotanum, hverjar framfylgja MFA, hverjar geyma lykilorð með nútímalegu minnisþungu kjötkássa og hverjar eru sérsmíðaðar. Fyrir fyrirtækja- og opinber eignasöfn skaltu bæta við regluvarslusjónarhorni: staðlar eins og NIST SP 800-63 setja áþreifanlegar væntingar um auðkennistryggingu, og heimasmíðað flæði sem getur ekki sýnt þær mun ekki lifa af úttekt eða rýni um heimild til að starfa.

6. **Hvernig sannreynið þið að þessar stýringar haldi í framleiðslu og getið þið sannað það með sönnunargögnum frekar en fullyrðingu?** Að skrifa öruggt sjálfgefið gildi er ekki það sama og að vita að hver þjónusta virði það enn, og stýringar rotna hljóðlega eftir því sem kóði breytist, undantekningar hrúgast upp og nýir endapunktar fara út. Fyrir stórt teymi er spurningin þekja: hvaða þjónustur keyra kyrrstæða greiningu, ósjálfstæðisskönnun og kvika prófun eða innbrotspróf, og hvernig veistu að þær sem sleppa þeim eru ekki áhættumestu forrit þín? Ákveddu hvaða sannprófun er skylda í leiðslunni á móti reglubundin, hver flokkar niðurstöðurnar og hvaða sönnunargögn þú geymir til að sýna að stýring var prófuð og stóðst á tiltekinni dagsetningu. Komdu með núverandi þekjukort þitt, meðaltíma til úrbóta eftir alvarleika og lista yfir forrit án nýlegs prófs. Í eftirlitsskyldu og opinberu samhengi eru þessi sönnunargögn ekki valkvæð: endurskoðendur, heimildarembættismenn og innbrotsrannsakendur biðja allir um sönnun þess að stýringar hafi verið sannreyndar, og stefna án prófunarskráa fullnægir þeim sjaldan.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með tvo eða þrjá verkfræðinga og engan öryggissérfræðing er vogarafl þitt að erfa öryggi frekar en að smíða það: taktu upp stýrða OIDC-auðkennaveitu, hallaðu þér að ramma þar sem ORM stikar fyrirspurnir sjálfgefið og geymdu leyndarmál í leyndarmálastjóra vettvangsins frekar en `.env` skrám sem liðsfélagi gæti innritað fyrir slysni. Kveiktu á sjálfvirkri ósjálfstæðisskönnun sem opnar plástursbeiðnir og líttu á það sem nóg í bili. Smíðaðu ekki eigin auðkenningu eða dulritun, því ein innsprautuð fyrirspurn eða einn lekinn lykill getur bundið enda á fyrirtækið áður en það hefur viðskiptavini.

**Lítið fyrirtæki.** Þú hefur líklega engan forritaöryggissérfræðing og þröngt fjárhagsáætlun, svo keyptu stýringar innbyggðar í verkfærin og vettvangana sem þú borgar þegar fyrir frekar en að manna sérstaka starfsemi. Veldu hýsta auðkennaveitu með MFA innifalið, stýrðan gagnagrunn sem ýtir þér að stikuðum aðgangi og hugbúnaðarsafnshýsil sem skannar innritanir fyrir lekin leyndarmál úr kassanum. Einbeittu knappri athygli þinni að OWASP Top 10 grunnatriðunum sem valda flestum raunverulegum innbrotum og kjóstu söluaðila sem afhenda örugg sjálfgefin gildi sem þú getur ekki óvarlega slökkt á.

**Stórfyrirtæki.** Yfir mörg teymi er áskorunin samræmi: bakaðu ASVS-stýringar inn í ramma á troðnum slóðum svo hver ný þjónusta erfi stikaðar fyrirspurnir, úttakskóðun, örugg setur og heimild á þjóninum ókeypis. Haltu nákvæmum SBOM og flotavíðri ósjálfstæðisskönnun svo næsti útbreiddi bókasafnsveikleiki sé spurning um klukkustundir, ekki vikur, og miðlægðu heimildarstefnu svo þvert-leigjenda aðgangur verði prófanlegur. Staðlaðu á eina auðkennaveitu með framfylgdu MFA og stýrðu forritaöryggi sem stýrðu eignasafni með áhættuþrepuðum ASVS-stigum og úttektuðum sönnunargögnum.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta stýringarnar sem þú verður að sýna fram á, ekki bara útfæra. Sannreyndu borgarasnúnar þjónustur gegn OWASP ASVS á stigi sem samsvarar viðkvæmni gagna, undirritaðu hvern uppsettan grip og vottaðu herkomu hans samkvæmt SLSA til að fullnægja aðfangakeðjuskyldum og gefðu út skammlíf auðkennisgögn úr miðlægri hvelfingu með fullri aðgangsskráningu. Búðu þig undir að sýna endurskoðendum og heimildarembættismönnum skjalfesta vörsluslóð frá frumkóða til framleiðslu og samstilltu auðkennistryggingu við útgefna staðla eins og NIST SP 800-63.

## Dæmi

**Sprotafyrirtæki.** Þriggja verkfræðinga SaaS-teymi sleppir því að smíða eigin innskráningu og tekur upp stýrða OIDC-veitu á degi eitt, sem færir MFA og örugga endurstillingu lykilorða án þess að skrifa öryggiskritískan kóða sem það hefur ekki efni á að fá rangan. Það treystir á ORM rammans svo fyrirspurnir eru stikaðar sjálfgefið, geymir leyndarmál í leyndarmálastjóra vettvangsins frekar en í `.env` skrám sem liðsfélagi gæti innritað fyrir slysni og kveikir á sjálfvirkri ósjálfstæðisskönnun sem opnar plástursbeiðni þegar bókasafn þarf plástrun. Ekkert af þessu hægir á teyminu og það þýðir að einn lekinn lykill eða ein innsprautuð fyrirspurn bindur ekki enda á fyrirtækið áður en það hefur viðskiptavini.

**Stórfyrirtæki.** Smásöluvettvangur sem þjónar tugum milljóna kaupenda staðlar auðkenningu á OIDC gegnum eina auðkennaveitu, framfylgir MFA fyrir starfsfólk og stigmagnaðri auðkenningu fyrir verðmiklar reikningsbreytingar. Allur gagnagrunnsaðgangur fer gegnum ORM stillt til að stika fyrirspurnir og Content Security Policy styður úttakskóðun. Eftir víðfrægan veikleika í vinsælu skráningarbókasafni leyfir SBOM fyrirtækisins því að finna hverja áhrifaða þjónustu á klukkustundum og plástra þær á tveimur dögum, á meðan keppinautar án skráa eyddu vikum í leit.

**Hið opinbera.** Sambandsbótastofnun smíðar borgarasnúnar þjónustur sannreyndar gegn OWASP ASVS stigi 2, með stigi 3 fyrir íhlutina sem meðhöndla viðkvæmustu skrárnar. Leyndarmál búa í miðlægri hvelfingu sem gefur út skammlíf auðkennisgögn. Innritunarskönnun hindrar hvern lekinn lykil. Hver uppsettur gripur er undirritaður og herkoma hans vottuð samkvæmt SLSA, sem fullnægir sambandsskyldu um sannanlegar hugbúnaðaraðfangakeðjur og gefur endurskoðendum skýra vörsluslóð frá frumkóða til framleiðslu.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Útgjöld til forritaöryggis kaupa niður líklegasta og dýrasta innbrotsflokkinn. Heildareignarkostnaðurinn felur í sér verkfæri (skanna, leyndarmálastjóra, auðkennaveitur), verkfræðitíma til að úrbæta niðurstöður og vægan núning öruggra sjálfgefinna gilda. Á móti því skaltu vega kostnaðinn við að sleppa því: innsprautunar- og bilaðrar-aðgangsstýringar innbrot afhjúpa rútínulega milljónir skráa, sem kveikir eftirlitssektir, skyldubundnar tilkynningar, svikatap, úrbótalotur og mannorðsskaða sem bælir tekjur árum saman.

Ávöxtunin er sterkust þegar stýringar eru sjálfvirkar og endurnýttar. Ein vel stillt auðkennissamþætting, eitt hert fyrirspurnarlag í sameiginlegum ramma og ein leiðsla sem hindrar berskjölduð ósjálfstæði verja allan flotann á jaðarkostnaði á þjónustu. Aðfangakeðjustýringar sérstaklega hafa farið úr valkvæðum í nauðsynlegar: brotin ósjálfstæðiseining getur gert hvern viðskiptavin þinn að fórnarlambi, og eftirlitsaðilar og fyrirtækjakaupendur krefjast æ oftar SBOM og undirritaðrar herkomu sem skilyrði fyrir viðskiptum. Þegar þú færir rök við forystu skaltu tengja fjárfestinguna við tilteknar, nefndar áhættur og við innkaupa- og regluvörslukröfur sem hindra tekjur ef þú uppfyllir þær ekki.

## Andmynstur og gildrur

- **Að rúlla eigin dulritun eða auðkenningu.** Framleiðir nánast alltaf lúmska, nýtanlega galla.
- **Eingöngu staðfesting á biðlara.** Léttvægt að sniðganga. Þjónninn verður að endurstaðfesta allt.
- **Svartlistahreinsun.** Að reyna að fjarlægja „vonda“ stafi í stað þess að leyfilista góða. Árásaraðilar finna götin.
- **Leyndarmál í frumkóða eða umhverfisskrám.** Algengasta einstaka orsök auðkennisgagnaleka.
- **Að hunsa heimild á hlutaaðgangi.** Að gera ráð fyrir að auðkenndur notandi megi nálgast hvaða hlut sem hann getur giskað á auðkenni.
- **Setja-og-gleyma ósjálfstæði.** Að uppfæra aldrei íhluti þriðja aðila þar til innbrot neyðir það.
- **Að líta á Top 10 sem marklínuna.** Það er gólf, ekki tæmandi staðall. Notaðu ASVS fyrir dýpt.
- **Að skrá viðkvæm gögn.** Lykilorð, tákn og PII (persónugreinanlegar upplýsingar) í skrám verða innbrot sem bíður þess að gerast.

## Þroskalíkan

**Stig 1: Upphaf.** Forritaöryggi byggir á þekkingu einstakra hönnuða og bregst aðeins við eftir atvik. Engar staðlaðar stýringar. Leyndarmál sitja í frumkóða. Ósjálfstæði eru sjaldan uppfærð. Auðkenning er sérsmíðuð og ad hoc og innsprautunar- eða bilaðrar-aðgangsstýringar gallar finnast fyrir tilviljun frekar en með ferli.

**Stig 2: Þróun.** Grunnvinnubrögð birtast en eru mismunandi milli teyma. OWASP Top 10 vitund breiðist út, sumar rammastigsvarnir eru til staðar og leyndarmálastjóri er til en notaður ójafnt. Ósjálfstæðisskönnun keyrir stundum. Ný kerfi taka upp staðlaða auðkennaveitu, á meðan eldri þjónustur halda heimasmíðuðum innskráningarflæðum sínum óbreyttum.

**Stig 3: Stöðlun.** Stýringar eru skjalfestar og framfylgt um alla skipulagsheildina. ASVS-byggðar kröfur eru settar fyrir hvert áhættuþrep, stikaðar fyrirspurnir og úttakskóðun eru normið og miðlæg auðkennaveita með MFA er skylda. Leyndarmálum er stýrt og þau skönnuð sjálfvirkt, SBOM eru framleiddar og ósjálfstæðisskönnun keyrir í hverri leiðslu.

**Stig 4: Stjórnun.** Vinnubrögðin eru mæld og stýrð gegn grunnlínum. Skönnunar- og prófaþekja, meðaltími til úrbóta eftir alvarleika, hlutfall þjónusta sem erfa sjálfgefin gildi troðinnar slóðar, aldur snúnings auðkennisgagna og leyndarmála og ASVS-samræmi eru öll rakin á mælaborðum. Undantekningar eru skráðar með fyrningardagsetningum, rek frá grunnlínu kallar fram aðgerð og útgáfur eru hliðaðar á skilgreindum öryggisþröskuldum frekar en dómgreindarákvörðunum.

**Stig 5: Samhæfing.** Öryggi er stöðugt bætt og samþætt um skipulagsheildina. Örugg sjálfgefin gildi eru byggð inn í ramma á troðnum slóðum svo örugga leiðin er sjálfvirk, skammlíf auðkennisgögn eru notuð alls staðar og full aðfangakeðjutrygging með undirritun og herkomu (SLSA) er staðall. Sannprófun er samfelld, viðbrögð við nýjum veikleikum eru hröð og mæld og hvert atvik nærir aftur í sameiginleg sniðmát svo ein lagfæring herðir allan flotann.

## Hugmyndir til umræðu

1. Hvar ætti heimildarrökfræði að búa til að vera bæði samræmd og viðhaldanleg yfir margar þjónustur?
2. Hve ágengt ættirðu að uppfæra ósjálfstæði miðað við málamiðlunina milli útsetningar og hræringar?
3. Hvert ASVS-stig er viðeigandi fyrir hvern flokk forrita í eignasafninu þínu?
4. Hvernig útrýmirðu langlífum leyndarmálum án þess að skapa brothætta útgáfuinnviði?
5. Hvað þyrfti til að skipulagsheildin þín framleiði og neyti SBOM og herkomu fyrir hvern grip?
6. Hvernig heldurðu öruggum sjálfgefnum gildum frá því að vera afvirkjuð undir afhendingarþrýstingi?

## Helstu atriði

- OWASP Top 10 er nauðsynleg þekking. ASVS veitir prófanlega staðalinn.
- Lagskiptu inntaksstaðfestingu, stikun og úttakskóðun til að sigra innsprautun og XSS.
- Notaðu sannreyndar samskiptareglur (OAuth 2.0, OIDC) og framfylgdu MFA. Smíðaðu aldrei auðkenningu frá grunni.
- Framfylgdu heimild á þjóninum fyrir hverja beiðni og hvern hlut.
- Haltu leyndarmálum úr frumkóða, stýrðu þeim miðlægt og snúðu yfir í skammlíf auðkennisgögn.
- Aðfangakeðjan er aðalárásaryfirborð. Notaðu SBOM, SCA, undirritun og herkomu (SLSA).
- Sjálfvirkar, endurnýtanlegar stýringar verja allan flotann á jaðarkostnaði á þjónustu.

## Heimildir og frekari lestur

- OWASP, *Top 10 Web Application Security Risks*
- OWASP, *Application Security Verification Standard (ASVS)*
- OWASP, *Cheat Sheet Series* (Input Validation, Authentication, Authorisation, Secrets Management)
- Dafydd Stuttard and Marcus Pinto, *The Web Application Hacker's Handbook*
- Aaron Parecki, *OAuth 2.0 Simplified*
- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines*
- Cloud Native Computing Foundation and OpenSSF, *SLSA framework* and *Supply-chain Security guidance*
