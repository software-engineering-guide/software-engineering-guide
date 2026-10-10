# 2.5 Kóðarýni og samvinna

## Yfirlit og tilgangur

[Kóðarýni](https://en.wikipedia.org/wiki/Code_review) er sú venja að láta einhvern annan en höfundinn skoða breytingu áður en hún sameinast. Hún er ein af áhrifamestu gæða- og þekkingarmiðlunaraðgerðum sem hugbúnaðarskipulagsheild á, og fyrir stór teymi er hún líka helsti búnaður samhæfingar og menningar. Rýni grípur galla, dreifir þekkingu á kóðagrunninum, framfylgir stöðlum og leiðbeinir verkfræðingum, en aðeins þegar hún er gerð vel. Illa gerð verður hún flöskuháls, uppspretta núnings eða stimpill sem gefur falska tryggingu.

Fyrir stór teymi er rýni þar sem einstaklingsvinna mætir sameiginlegu eignarhaldi. Hún er oft aðalsnertipunktur milli verkfræðinga sem annars vinna hver fyrir sig, svo viðmið hennar móta hvernig öll skipulagsheildin vinnur saman. Rýni dreifir þekkingu svo enginn hluti kerfisins sé skilinn af aðeins einum, sem dregur úr [strætóstuðulsáhættu](https://en.wikipedia.org/wiki/Bus_factor), hættunni þegar þekking situr hjá of fáum, sem hrjáir stór, langlíf kerfi. Hún býr líka til úttektarslóð um hver breytti hverju og hver samþykkti.

Í fyrirtækja- og opinberu samhengi hefur rýni oft regluvarsluvídd. [Aðskilnaður starfa](https://en.wikipedia.org/wiki/Separation_of_duties) (enginn einn stýrir heilli viðkvæmri breytingu), skyldubundin samþykki og rekjanleiki eru oft skyldaðar stýringar. Breyting sem snertir viðkvæm kerfi kann að þurfa rýni tiltekinna hlutverka og rýniskráin verður úttektarsönnun. Áskorun þín er að fullnægja þessum stýringum á meðan rýni er haldið hraðri og uppbyggilegri, í stað þess að breyta henni í helgisið.

## Meginreglur

- Rýndu til að bæta breytinguna og deila þekkingu, ekki til að sýna þig.
- Litlar breytingar fá betri rýni, svo haltu sameiningarbeiðnum (PR) markvissum og hóflegum að stærð.
- Rýnitöf er kostnaður alls teymisins. Hröð afgreiðsla heldur öllum á hreyfingu.
- Sjálfvirknivæddu vélræna hlutann (stíl, próf, öryggisskannanir) svo menn rýni hönnun og réttleika.
- Aðskildu hindrandi atriði frá ábendingum og kjörum og vertu skýr um hvað er hvað.
- Gagnrýndu kóðann, ekki manneskjuna. Endurgjafarviðmið ráða hvort rýni byggir upp traust eða tærir það.
- Höfundurinn ber ábyrgð á að gera breytinguna auðvelda til rýni.

## Ráðleggingar

### Hafðu sameiningarbeiðnir litlar og vel lýstar

Haltu hverri breytingu á einu rökrænu áhyggjuefni og nógu lítilli til að rýna vandlega. Stórar PR fá grunna rýni. Gefðu skýra lýsingu á hvað breyttist, hvers vegna og hvernig þú staðfestir það, svo rýnirinn hafi samhengi. Skiptu vélrænum endurbyggingum og hegðunarbreytingum í aðskildar PR, svo hver sé auðveld að rökræða. Góð lýsing er mikilvægasta einstaka framlag höfundar til rýnigæða.

### Settu rýnistaðla og gátlista

Tilgreindu hvað rýnar ættu að leita að: réttleika, hönnunarfit, nægjanleika prófa, öryggisáhrifum, læsileika og fylgni við staðla. Léttur gátlisti heldur rýni samræmdri og kemur í veg fyrir að mikilvægar víddir renni í gegn, án þess að breyta rýni í hakreitaverk. Skilgreindu hvað krefst rýni, hver getur samþykkt og öll hlutverkabundin samþykki sem þarf fyrir viðkvæm svæði.

### Settu og vaktaðu viðmið um rýnitöf

Komdu þér saman um markafgreiðslutíma, til dæmis að svara innan vinnudags, og gerðu rýni að fyrsta flokks hluta dagsins frekar en einhverju kreistu inn síðast. Langar rýnibiðraðir stöðva afhendingu og freista verkfræðinga til of stórra, lotaðra breytinga. Vaktaðu tíma að fyrstu rýni og tíma að sameiningu og líttu á viðvarandi töf sem ferlisvanda til að laga, ekki persónulegan brest.

### Sjálfvirknivæddu allt vélrænt

Keyrðu snið, [lint-skoðun](https://en.wikipedia.org/wiki/Lint_(software)), próf og öryggis- og ósjálfstæðisskönnun í [samfelldri samþættingu](https://en.wikipedia.org/wiki/Continuous_integration) (CI), svo rýnar eyði aldrei athygli í þau. Taktu frá mannlega rýni fyrir það sem vélar geta ekki dæmt: hvort hönnunin sé rétt, hvort aðferðin passi kerfinu, hvort prófin séu marktæk og hvort kóðinn muni enn skiljast síðar.

### Notaðu para- og hópforritun þar sem þær passa

Notaðu [paraforritun](https://en.wikipedia.org/wiki/Pair_programming), þar sem tveir verkfræðingar skrifa kóða saman við eina vinnustöð, fyrir flókna eða áhættusama vinnu, móttöku og þekkingarflutning. Hún er stöðug rýni og útrýmir oft þörfinni fyrir sérstakt rýniskref. Notaðu [hópforritun](https://en.wikipedia.org/wiki/Mob_programming), þar sem allt teymið vinnur að einu verkefni í einu, fyrir mikilvægar hönnunarákvarðanir eða til að dreifa þekkingu á flóknu svæði yfir teymið. Líttu á þetta sem viðbót við ósamtíma rýni, valið eftir samhengi, ekki staðgengla til að skylda alls staðar.

### Taktu upp sjálfvirka og gervigreindaraðstoðaða rýni varlega

Notaðu sjálfvirk rýniverkfæri og gervigreindaraðstoðarmenn til að grípa algeng vandamál, leggja til umbætur og létta rýnarbyrði, en líttu á úttak þeirra sem inntak, ekki vald. Gervigreindarrýni er góð í yfirborðsatriðum og samræmi en léleg í djúpri hönnunardómgreind og kerfissamhengi. Haltu manneskju ábyrgri fyrir hverju samþykki, sérstaklega fyrir öryggisviðkvæmar og regluvörslutengdar breytingar.

### Settu uppbyggileg endurgjafarviðmið

Settu viðmið sem halda endurgjöf sértækri, góðri og beinni að kóðanum. Hvettu rýna til að spyrja spurninga frekar en gefa skipanir, útskýra rökin að baki beiðni og hrósa góðri vinnu. Merktu hindrandi áhyggjur og valkvæðar ábendingar skýrt (til dæmis með því að forskeyta ekki-hindrandi athugasemdir). Þessi viðmið ráða hvort rýni styrkir teymið eða elur á gremju.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
|---|---|---|
| Ósamtíma PR-rýni | Sveigjanleg, skjalfest, skalar yfir tímabelti | Töf, missir blæbrigði, getur virst andstæð |
| Paraforritun | Stöðug rýni, hraður þekkingarflutningur, mikil gæði | Tveir á einu verkefni, þreytandi, erfiðara að tímasetja |
| Hópforritun | Samræming alls teymis, dreifir djúpri þekkingu | Dýrt samtals, ekki fyrir hefðbundna vinnu |
| Skyldubundnir margir rýnar | Sterk trygging, regluvörsluvænt | Hægara, dreifir ábyrgð, biðraðarþrýstingur |
| Gervigreindaraðstoðuð rýni | Hröð, þreytulaus á algengum vandamálum, dregur úr álagi | Missir kerfissamhengi, falskt sjálfstraust ef of mikið er treyst |

Kjarnaspennan er nákvæmni gegn hraða. Dýpri rýni grípur meira, en hún hægir á afhendingu og getur pirrað höfunda. Hraðari rýni heldur flæði, en hætta er á að hún verði yfirborðskennd. Leiðin í gegn er að láta rýnidýpt samsvara áhættu breytingar, svo léttvægar breytingar fái létta rýni og áhættusamar djúpa, og að sjálfvirknivæða vélræna vinnu svo mannleg fyrirhöfn einbeitist þar sem hún skiptir máli.

## Spurningar til að ræða með teyminu

1. **Hvað telst of stórt fyrir eina sameiningarbeiðni og aðskilurðu vélrænar endurbyggingar frá hegðunarbreytingum?** Þessi kafli segir skýrt að stórar PR fái grunna rýni og að höfundurinn eigi rýnanleikann, og hann biður þig að aðskilja endurbyggingar frá hegðunarbreytingum svo hvort sé auðvelt að rökræða. Í stóru teymi tryggir risa-PR stimpil, sem gefur falska tryggingu á meðan raunverulegir gallar leka í gegn. Komdu með sönnunargögnin: dreifingu PR-stærða þinna og hvernig rýnidýpt fellur eftir því sem mismunur vex. Komdu þér saman um hagnýt stærðarviðmið og venju að lenda hreinum endurbyggingum aðskildum frá rökfræðibreytingum, svo rýnir geti í raun haldið hverri breytingu í höfðinu. Sá eini agi lyftir gæðum hverrar rýni sem fylgir.

2. **Hvernig greinirðu á milli hindrandi andmæla og valkvæðrar ábendingar og er sú venja í raun notuð?** Kaflinn biður þig að aðskilja hindrandi atriði frá kjörum og vera skýran um hvað er hvað, og hann merkir að hindra á kjör sem tærandi andmynstur. Án sameiginlegrar venju les stílskoðun rýnis sem skyldubundin breyting, sem elur á gremju og hægir á afhendingu yfir allt teymið. Komdu með dæmi úr nýlegum rýnum þar sem kjör stöðvaði sameiningu sem áþreifanlegt merki. Taktu upp létt merki, til dæmis forskeyti sem merkir ekki-hindrandi athugasemdir, svo höfundar viti samstundis hvað verður að breytast á móti hvað er ábending. Það heldur rýni einbeittri að réttleika og hönnun frekar en smekk.

3. **Hver verður að samþykkja breytingar á öryggisviðkvæmum eða regluvörslutengdum kóða og hvernig er þeirri leiðsögn framfylgt?** Þessi kafli lýsir hlutverkabundnum samþykkjum, kóðaeignarreglum og aðskilnaði starfa þar sem enginn einn stýrir heilli viðkvæmri breytingu, með samþykkið skráð sem úttektarsönnun. Í fyrirtækja- og opinberu umhverfi eru þetta skyldaðar stýringar og áhættan er að þær séu annaðhvort sniðgengnar eða breytist í flöskuháls sem frystir afhendingu. Komdu með merkið: hvaða einingar eru viðkvæmar og hvort eignarreglur beina þeim breytingum nú sjálfvirkt til réttra samþykkjenda. Kóðaðu leiðsögnina í kóðaeignarstillingu og paraðu hana við sjálfvirkar athuganir og litlar breytingar, svo stýringin sé fullnægð án mannlegrar hliðvarðabiðraðar. Ákveddu þetta af ásetningi frekar en að uppgötva bilið í úttekt.

4. **Hvaða rýnitafarmarkmið hefurðu í raun samþykkt og mælirðu og framfylgir því, eða er það aðeins von?** Kaflinn lítur á rýnitöf sem kostnað alls teymisins og biður þig að vakta tíma að fyrstu rýni og tíma að sameiningu og líta á viðvarandi töf sem ferlisvanda frekar en persónulegan brest. Í stóru teymi skattleggur óeignuð rýnibiðröð alla hljóðlega: höfundar lota stærri breytingum til að forðast biðina, þær breytingar fá síðan grynnri rýni og afhendingartími drífur upp án nokkurs eins sökudólgs. Sjónarmiðið á móti er að hart töfamarkmið getur ýtt rýnum til að renna yfir, svo hraða og dýpt þarf að jafna frekar en skipta blindandi. Komdu með sönnunargögnin: núverandi dreifingu tíma að fyrstu rýni, hvernig hún er breytileg eftir teymi og breytingastærð og hvar rýni situr lengst. Í fyrirtækja- og opinberu umhverfi skaltu tengja markmiðið við flæðimælikvarða sem forystan fylgist þegar með, því skyldubundin margra-rýna stýring án töfaviðmiðs verður flöskuhálsinn sem frystir afhendingu og freistar fólks til að fara fram hjá stýringunni alfarið.

5. **Fyrir hvaða tegundir breytinga treystirðu sjálfvirkri og gervigreindaraðstoðaðri rýni og hvar verður manneskja að bera ábyrgð?** Kaflinn segir að líta á úttak gervigreindarrýni sem inntak, ekki vald: sterkt á yfirborðsatriðum og samræmi, veikt á djúpri hönnunardómgreind og kerfissamhengi, með manneskju ábyrga fyrir hverju samþykki. Án skýrra marka rekur stórt teymi í ofurtraust, þar sem grænt vélmennisathugasemd les sem staðin rýni og raunveruleg hönnunar- og öryggisáhætta rennur í gegn undir fölsku sjálfstrausti. Togið á móti er að gervigreindarrýni léttir raunverulega álag og grípur algenga galla þreytulaust, svo að banna hana sóar vogarafli. Komdu með sönnunargögnin: hvar sjálfvirkar tillögur hafa gripið raunveruleg vandamál, hvar þær hafa framleitt suð og hvaða breytingagerðir (öryggisviðkvæmar, regluvörslutengdar, arkitektúrlegar) þú myndir aldrei láta vél samþykkja eina. Fyrir fyrirtækja- og opinbert starf skaltu nefna hver ber ábyrgð á samþykki þegar gervigreindaraðstoðarmaður var í lykkjunni, því úttekt mun spyrja hver rýndi breytingu og „tólið gerði það“ er ekki svar sem eftirlitsaðili tekur gilt.

6. **Hvar ættu pörun eða hópforritun að koma í stað ósamtíma rýni og hvernig notarðu rýni til að draga úr strætóstuðulsáhættu af ásetningi?** Kaflinn rammar para- og hópforritun sem stöðuga rýni valda eftir samhengi, og nefnir rýni sem búnaðinn sem dreifir þekkingu svo enginn hluti kerfisins sé skilinn af aðeins einum. Ef þetta er skilið eftir óbeint þjappast þekking saman: sami sérfræðingurinn rýnir hverja breytingu á undirkerfi, rýni verður stimpill því enginn annar getur áskorað hann og strætóstuðulsáhætta vex einmitt þar sem kerfið er mikilvægast. Sjónarmiðið á móti er kostnaður, því hópforritun eyðir tíma alls teymisins og pörun bindur tvo verkfræðinga, svo þú getur ekki skyldað hana alls staðar. Komdu með sönnunargögnin: hvaða einingar hafa aðeins einn trúverðugan rýni, hvar móttaka stöðvast og hvar flókið svæði myndi njóta góðs af lifandi lotu yfir athugasemdaþráðum. Í stórri eða opinberri skipulagsheild skaltu líta á vísvitandi þekkingardreifingu sem áhættustýringu, því langlíft kerfi þar sem mikilvægir hlutar velta á einni manneskju er rekstrar- og samfelluskuldbinding, ekki bara mönnunaróþægindi.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með þrjá eða fjóra verkfræðinga skaltu hafa rýni létta: samþykki eins liðsfélaga á lítilli sameiningarbeiðni, vélrænar athuganir í CI og enginn skyldubundinn annar rýnir sem myndi stöðva sameiningu. Raunverulega markmiðið er minna regluvarsla en að tryggja að fleiri en einn skilji hvern hluta kerfisins, svo paraðu á áhættusömu hlutunum og líttu á það sem móttöku. Byggðu ekki þunga kóðaeignarleiðsögn sem þú munt brátt vaxa upp úr. Sameiginlegt viðmið um litlar, vel lýstar breytingar kaupir mestan ávinninginn nánast ókeypis.

**Lítið fyrirtæki.** Þú hefur varla rýniverkfærasérfræðing, svo hallaðu þér að því sem hýsingarvettvangur þinn (til dæmis stýrð Git-þjónusta) gefur þér úr kassanum frekar en að smíða sérsniðna sjálfvirkni. Kauptu lint-, próf- og öryggisskönnunarsamþættingarnar í stað þess að viðhalda þeim, svo fáu verkfræðingarnir þínir eyði af skornum skammti rýnimínútum í hönnun og réttleika. Haltu einni einfaldri reglu, hver breyting fær eitt annað augnapar, og standastu freistinguna að bæta við ferli sem þú hefur engan til að viðhalda.

**Stórfyrirtæki.** Áskorunin er samræmi milli margra teyma: sameiginlegir staðlar, kóðaeignarreglur sem beina viðkvæmum breytingum til réttra samþykkjenda og hlutverkabundin samþykki skráð sem úttektarsönnun. Sjálfvirknivæddu vélrænu athuganirnar um alla skipulagsheildina svo mannleg rýni einbeitist að hönnun og fylgstu með rýnitöf sem flæðimælikvarða svo skyldubundnar margra-rýna stýringar verði ekki hljóðlega að flöskuhálsum. Láttu rýnidýpt samsvara breytingaáhættu með skjalfestri stefnu, svo léttvægar breytingar haldist hraðar á meðan áhættusamar fá aðskilnað starfa og dýpri skoðun.

**Hið opinbera.** Breytingastýring er oft skylda: sérhver framleiðslubreyting rýnd og samþykkt af einhverjum öðrum en höfundinum, með skrána geymda sem úttektarsönnun til að fullnægja kröfum um aðskilnað starfa. Kjóstu gagnsæja, rekjanlega slóð um hver skrifaði, hver samþykkti og hvaða athuganir stóðust, og fjárfestu í sjálfvirkni og litlum, tíðum breytingum svo stýringin frysti ekki afhendingu. Þar sem rýniverkfæri eru keypt skaltu krefjast útflytjanlegra úttektarskráa og forðast innilokun, því sönnunin verður að lifa hvaða einstaka söluaðila sem er og standast opinbera skoðun.

## Dæmi

**Sprotafyrirtæki.** Fjögurra verkfræðinga sprotafyrirtæki heldur hverri sameiningarbeiðni lítilli og biður um samþykki eins liðsfélaga fyrir sameiningu, minna vegna regluvörslu en til að tryggja að enginn einn sé sá eini sem skilur hluta kerfisins. CI keyrir sniðmótarann og prófin, svo mennirnir eyða fáu rýnimínútunum sínum í hönnun og réttleika frekar en bil. Þegar teymið lendir á flóknum hluta greiðsluflæðisins para tveir þeirra sig á honum í stað þess að skiptast á ósamtíma athugasemdum, sem tvöfaldast sem móttaka fyrir nýjasta starfsmanninn.

**Stórfyrirtæki.** Stórt hugbúnaðarfyrirtæki krefst að minnsta kosti einnar samþykkjandi rýni á hverja breytingu, auk annars samþykkis fyrir breytingar á öryggisviðkvæmum einingum sem kóðaeignarreglur auðkenna. CI sér um allar stíl- og prófaathuganir, svo rýnar einbeita sér að hönnun og réttleika. Teymið rekur tíma að fyrstu rýni og lítur á hækkandi miðgildi sem merki um að endurjafna vinnuálag. Nýir verkfræðingar fá móttöku gegnum pörun, sem styttir leið þeirra að sjálfstæðum framlögum.

**Hið opinbera.** Landsbundin stofnun sem starfar undir ströngum breytingastýringarkröfum skyldar að sérhver framleiðslubreyting sé rýnd og samþykkt af einhverjum öðrum en höfundinum, með samþykkið skráð til úttektar. Til að halda stýringunni frá því að verða flöskuháls fjárfestir stofnunin í sjálfvirkum athugunum og litlum, tíðum breytingum og setur sama-dags rýnisvarsviðmið. Rýnislóðin, sem nær yfir hver skrifaði, hver samþykkti og hvaða athuganir stóðust, verður hluti af regluvörslusönnun hverrar útgáfu og fullnægir kröfum um aðskilnað starfa án þess að frysta afhendingu.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Kóðarýni borgar sig til baka í þremur gjaldmiðlum: gallar gripnir fyrir framleiðslu, þekking dreifð yfir teymið og staðlar haldnir sjálfvirkt yfir tíma. Að grípa galla í rýni er margfalt ódýrara en að grípa hann í framleiðslu, og þekkingardreifingarávinningurinn dregur úr lykilmannaáhættu sem annars getur kostað skipulagsheild dýrt þegar einhver fer. Rýni er líka menningarflutningsbúnaðurinn sem heldur vaxandi teymi samhangandi.

Kostnaður rýni er verkfræðitími og nokkur töf, hvort tveggja viðráðanlegt með góðum vinnubrögðum. Kostnaðurinn við að rýna *ekki*, eða rýna illa, felur í sér framleiðslugalla, sílóuð þekking, ósamræmdan kóða og, í eftirlitsskyldu umhverfi, misheppnaðar úttektir og regluvörslu niðurstöður. Ofþung rýni hefur líka raunverulegan kostnað: langar biðraðir, of stórar lotur, niðurdregnir verkfræðingar. Til að færa rök við forystu skaltu tengja rýnivinnubrögð við bilanahlutfall breytinga, afhendingartíma og móttökuhraða og rekja rýnitöf sem skýran flæðimælikvarða.

## Andmynstur og gildrur

- **Stimpillinn:** samþykki án raunverulegrar skoðunar sem gefur falska tryggingu og fullnægir aðeins bókstaf stýringar.
- **Risa-PR:** þúsundir lína sem aðeins er hægt að renna yfir og tryggir grunna rýni.
- **Eingöngu smámunarýni:** að einblína á léttvægi á meðan hönnun og réttleiki er misst, oft því vélrænar athuganir eru ekki sjálfvirknivæddar.
- **Rýni sem hliðvarsla:** að nota rýni til að sýna yfirráð eða hindra aðra, sem eitrar samvinnu.
- **Hæga biðröðin:** rýnir sem sitja dögum saman, stöðva afhendingu og hvetja til lotunar.
- **Ofurtraust á gervigreindarrýni:** að líta á sjálfvirkar tillögur sem valdbærar og sleppa mannlegri dómgreind á áhættusömum breytingum.
- **Að hindra á kjör:** að setja fram persónulegar stílskoðanir sem skyldubundnar breytingar án þess að greina þær frá raunverulegum göllum.

## Þroskalíkan

- **Stig 1, Upphaf:** Rýni er ad hoc og viðbragðsdrifin. Hún er oft sleppt eða gerð ósamræmt, vélræn atriði ráða athugasemdum, endurgjafarviðmið eru ósett og öll samþykkjaslóð er tilviljanakennd frekar en yfirveguð.
- **Stig 2, Þróun:** Grunnrýnivinnubrögð eru til en breytileg eftir teymum. Rýni er skyldað sums staðar og hæg eða valkvæð annars staðar, sjálfvirkni er að hluta og stærð og gæði PR sveiflast mikið án sameiginlegrar væntingar.
- **Stig 3, Stöðlun:** Staðlar eru skjalfestir og framfylgt um alla skipulagsheildina. Litlar markvissar PR, sjálfvirkt snið, lint, próf og öryggisskönnun í CI, skýrir gátlistar, skýr venja um hindrandi á móti ábendingum og kóðaeignarreglur sem beina viðkvæmum breytingum til réttra samþykkjenda.
- **Stig 4, Stjórnun:** Rýni er mæld og stýrð gegn grunnlínum. Tími að fyrstu rýni, tími að sameiningu, rýnidýpt á móti breytingaáhættu, hlutfall galla sem sleppa og bilanahlutfall breytinga eru rakin. Viðvarandi töf er meðhöndluð sem ferlisvandi og gögnin knýja hvar á að endurjafna rýnaálag og hvar stýringar hægja á afhendingu án þess að bæta við tryggingu.
- **Stig 5, Samhæfing:** Rýni er stöðugt bætt og samþætt um skipulagsheildina. Dýpt aðlagast breytingaáhættu, pörun, hópforritun og gervigreindaraðstoð eru notuð af ásetningi með manneskju ábyrga, þekkingardreifing og strætóstuðulsáhætta eru stýrð af ásetningi og rýni bætir mælanlega gæði, afhendingarflæði og móttöku.

## Hugmyndir til umræðu

- Hvert er rétt rýnitafarmarkmið fyrir teymið þitt og hvað kemur í veg fyrir að þú náir því?
- Hvernig lætur þú rýnidýpt samsvara breytingaáhættu án þess að bæta við skriffinnsku?
- Hvar skila pörun eða hópforritun betri árangri en ósamtíma rýni í þínu samhengi?
- Hve mikið ætti að treysta gervigreindaraðstoðaðri rýni og fyrir hvaða tegundir breytinga?
- Hvernig heldurðu rýnigjöf uppbyggilegri eftir því sem teymið stækkar og verður fjölbreyttara?
- Hvernig fullnægirðu regluvörslusamþykkiskröfum án þess að skapa flöskuhálsa?

## Helstu atriði

- Haltu sameiningarbeiðnum litlum og vel lýstum. Höfundurinn á rýnanleikann.
- Sjálfvirknivæddu hið vélræna svo menn rýni hönnun, réttleika og próf.
- Rektu og stýrðu rýnitöf sem flæðikostnaði alls teymisins.
- Láttu rýnidýpt samsvara breytingaáhættu og greindu hindrandi atriði frá kjörum.
- Notaðu pörun, hópforritun og gervigreindaraðstoð sem viðbót eftir samhengi og haltu manneskju ábyrgri.

## Heimildir og frekari lestur

- Karl Wiegers, *Peer Reviews in Software: A Practical Guide*
- Google, *Engineering Practices: How to Do a Code Review* (as a reference exemplar)
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Kent Beck, *Extreme Programming Explained* (on pair programming)
- Woody Zuill, writings on mob programming
- Michael Lopp, *Managing Humans* (on engineering collaboration)
