# 5.7 Smáforritaþróun

## Yfirlit og tilgangur

[Smáforritaþróun](https://en.wikipedia.org/wiki/Mobile_app_development) er sú grein að smíða hugbúnað fyrir síma og spjaldtölvur. Fyrir marga er sími nú aðal- eða eina tölvan sem þeir eiga. Það gerir smáforritið að framdyrum þjónustu þinnar og oft yfirborðinu þar sem notendur dæma alla skipulagsheildina þína.

Farsímar eru sérstakt verkfræðiumhverfi, ekki lítil útgáfa af vefnum eða borðtölvunni. Tækið keyrir í vasa, á rafhlöðu, yfir tengingar sem koma og fara. Skjáir eru litlir. Stýrikerfið stýrir því sem forritið þitt má gera. Tveir ráðandi vettvangar eru til ([iOS](https://en.wikipedia.org/wiki/IOS) frá Apple og [Android](https://en.wikipedia.org/wiki/Android_%28operating_system%29) frá Google), hvor með eigin tungumál, hönnunarreglur og búð. Þú getur ekki einfaldlega afhent uppfærslu þegar þér hentar, því búð rýnir hana fyrst og notendur velja hvenær þeir setja hana upp. Þessi kafli byggir á framendaverkfræði (kafli 5.6), grunni notendaupplifunar (kafli 5.1) og aðgengi (kafli 5.3) og styðst við forritaöryggi (kafli 4.2) og CI/CD og afhendingu (kafli 8.1).

Mikilvægi fyrir fyrirtæki og hið opinbera er mikið. Fyrirtæki afhenda viðskiptavinaforrit og innri forrit fyrir eigið vinnuafl, oft stýrð gegnum [farsímatækjastjórnun](https://en.wikipedia.org/wiki/Mobile_device_management) (MDM: miðlægan hugbúnað sem stillir og tryggir fyrirtækjatæki). Ríkisstjórnir smíða borgarasnúin forrit fyrir bætur, heilsu, auðkenni og greiðslur og verða að þjóna öllum, þar á meðal fólki á gömlum tækjum og hægum tengingum, undir aðgengislögum. Í báðum umhverfum eru farsímar alvarleg, langlíf skuldbinding, svo meðhöndlaðu þá af sömu nákvæmni og þú gefur hverju öðru framleiðslukerfi.

## Meginreglur

- Hannaðu fyrir tækið: lítinn skjá, rafhlöðu og net sem kemur og fer.
- Gerðu ráð fyrir slitróttri tengingu. Vinndu ótengt fyrst og samstilltu þegar þú getur.
- Virtu hönnunar- og víxlverkunarvenjur hvers vettvangs.
- Þú stýrir ekki útgáfutíma. Búðin og notandinn gera það.
- Sundrun er eðlileg. Styddu raunverulegt svið tækja og stýrikerfisútgáfa.
- Geymdu gögn örugglega á tækinu, því tæki týnast og er stolið.
- Aðgengi er krafa, ekki lokafægi.
- Veldu smíðanálgun þína fyrir allan líftíma forritsins, ekki bara opnunardaginn.

## Ráðleggingar

### Veldu smíðanálgunina af ásetningi

Þrjár víðar nálganir eru til og hver passar ólíkum þörfum.

[Innlend þróun](https://en.wikipedia.org/wiki/Mobile_app_development) þýðir að skrifa sérstaklega fyrir hvern vettvang með eigin verkfærum: Swift fyrir iOS, Kotlin fyrir Android. Þú færð bestu afköst, fyllsta aðgang að tækjaeiginleikum og trúverðugasta vettvangsyfirbragð, á kostnað þess að smíða og viðhalda tveimur kóðagrunnum.

[Þverpallarammar](https://en.wikipedia.org/wiki/Cross-platform_software) leyfa einum kóðagrunni að beinast að báðum vettvöngum. [React Native](https://en.wikipedia.org/wiki/React_Native) notar JavaScript og birtir raunverulega innlenda íhluti. [Flutter](https://en.wikipedia.org/wiki/Flutter_%28software%29) notar Dart-málið og teiknar eigin viðmótshluta. Þetta dregur úr tvítekinni fyrirhöfn og getur flýtt afhendingu, en bætir við háð á heilsu rammans og getur dregist aftur úr nýjustu vettvangseiginleikum.

[Framsækið vefforrit](https://en.wikipedia.org/wiki/Progressive_web_app) (PWA: vefsíða sem hægt er að setja upp og sem getur virkað ótengt) þarf enga búð og uppfærist samstundis, en hefur takmarkaðan aðgang að sumum tækjaeiginleikum og veikari viðveru á heimaskjánum.

Veldu út frá nauðsynlegum tækjaeiginleikum, afkastasniði, viðhaldssjóndeildarhring, færninni sem þú getur ráðið og útbreiðslunni sem þú þarft. Afkastamikið neytendaforrit getur réttlætt innlent. Efnis- og eyðublaðaforrit með lítið teymi gæti passað vel við þverpalla eða PWA.

### Fylgdu hönnunarleiðbeiningum vettvangs

Hver vettvangur hefur útgefnar, ítarlegar venjur. Apple veitir [Human Interface Guidelines](https://en.wikipedia.org/wiki/Human_interface_guidelines) og Google veitir [Material Design](https://en.wikipedia.org/wiki/Material_Design). Þær ná yfir leiðsögn, bendingar, leturgerð, bil og kerfishegðun. Að fylgja þeim gerir forritið kunnuglegt, sem lækkar fyrirhöfnina sem notendur eyða í að læra það. Að berjast gegn þeim lætur forrit finnast framandi og klaufalegt. Þverpalla kóðagrunnur þarf samt að virða venjur hvers vettvangs þar sem þær eru ólíkar, frekar en að þvinga yfirbragð eins vettvangs á hinn.

### Hannaðu fyrir farsímaskorður

Byggðu ótengt fyrst: láttu kjarnaverk virka án tengingar, geymdu breytingar staðbundið og samstilltu þegar netið snýr aftur. Meðhöndlaðu árekstra yfirvegað þegar sömu gögn breytast á tveimur stöðum. Vertu sparsamur með rafhlöðu og gögn: lotaðu netköll, forðastu stöðuga staðsetningar- eða bakgrunnsvinnu, þjappaðu hleðslum og virtu gagnasparnaðarstillingar notandans. Skipuleggðu fyrir sundrun, hið víða svið skjástærða, tækjaafls og stýrikerfisútgáfa. Veldu stuðningssvið út frá raunverulegum notkunargögnum og prófaðu á hóflegum vélbúnaði, ekki bara flaggskipum. Hannaðu fyrir litla skjái með skýrri stigskiptingu, stórum snertimarkmiðum og efni sem aðlagast mismunandi stærðum og stefnum.

### Skipuleggðu dreifingu, útgáfumerkingu og uppfærslur

Útgáfa fer gegnum [Apple App Store](https://en.wikipedia.org/wiki/App_Store_%28Apple%29) og [Google Play](https://en.wikipedia.org/wiki/Google_Play), hvort með rýniferli og stefnur sem geta seinkað eða hafnað útgáfu. Byggðu rýnitíma inn í tímaáætlun þína og lestu stefnurnar snemma. Því notendur velja hvenær þeir uppfæra muntu alltaf hafa margar útgáfur á vettvangi í einu. Haltu forritinu afturábaksamhæfðu við eldri biðlara og útgáfumerktu API þín (kafli 2.3) svo gamalt forrit haldi áfram að virka. Útvegaðu leið til að krefjast uppfærslu þegar þú verður, til dæmis þvingaða uppfærslubeiðni þegar útgáfa er óörugg eða óstudd, og notaðu hana sparlega. Fyrirtæki geta líka dreift innri forritum gegnum MDM eða einkarásir frekar en opinberu búðirnar.

### Notaðu ýtitilkynningar og djúptengla af aðgát

[Ýtitilkynningar](https://en.wikipedia.org/wiki/Push_technology) leyfa þér að ná til notenda þegar forritið er lokað. Notaðu þær fyrir raunverulegt gildi, virtu samþykki notandans og vettvangsheimildir og forðastu hávaða, því fólk afvirkjar tilkynningar frá forritum sem ganga of langt. [Djúptenglar](https://en.wikipedia.org/wiki/Deep_linking) senda notanda beint á tiltekinn skjá frá tengli eða tilkynningu. Stilltu þá svo tengill opni rétta staðinn í forritinu og falli mjúklega aftur á vefinn þegar forritið er ekki uppsett.

### Tryggðu forritið og gögn þess

Líttu á tækið sem ótraust og mögulega týnt. Geymdu viðkvæm gögn í öruggri geymslu vettvangsins ([iOS Keychain](https://en.wikipedia.org/wiki/Keychain_%28software%29) eða Android Keystore), aldrei í skýrum skrám. Bjóddu [lífkennaauðkenningu](https://en.wikipedia.org/wiki/Biometrics) (fingrafar eða andlit) til að opna viðkvæmar aðgerðir, studda af aðgangskóða. Íhugaðu [skírteinafestingu](https://en.wikipedia.org/wiki/Public_key_pinning) (að athuga að þjónninn leggi fram væntanlegt skírteini) fyrir tengingar með miklum hagsmunum og skipuleggðu snúning þeirra skírteina. Lágmarkaðu það sem þú geymir á tækinu, verðu leyndarmál og fylgdu víðtækari leiðsögn í forritaöryggi (kafli 4.2).

### Byggðu raunverulega prófunar- og afhendingarleiðslu

Prófaðu á raunverulegum tækjum, ekki bara [hermum](https://en.wikipedia.org/wiki/Emulator), því vélbúnaður, skynjarar og afköst eru ólík. Notaðu tækjastofu eða skýjatækjabú til að dekka dæmigert svið gerða og stýrikerfisútgáfa. Sjálfvirknivæddu smíðar, prófanir, undirritun og búðarinnsendingu gegnum [samfellda samþættingu og afhendingu](https://en.wikipedia.org/wiki/CI/CD) (kafli 8.1), þar á meðal beta-dreifingu til prófenda fyrir opinbera útgáfu. Að stýra undirritunarlyklum og búðarauðkennisgögnum örugglega er hluti þessarar leiðslu.

### Gerðu aðgengi að kröfu

Styddu aðgengiseiginleika hvers vettvangs: skjálesara ([VoiceOver](https://en.wikipedia.org/wiki/VoiceOver) á iOS, [TalkBack](https://en.wikipedia.org/wiki/Google_TalkBack) á Android), kvika textastærð, nægilegt litbirtuskil og stór snertimarkmið. Merktu stýringar svo hjálpartækni geti lýst þeim. Prófaðu með raunverulegum hjálpartækjum, ekki bara sjálfvirkum athugunum. Sérstaklega fyrir hið opinbera er aðgengi lagaskylda og smáatriðin búa í aðgengi (kafli 5.3).

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
|---|---|---|
| Innlent (Swift, Kotlin) | Bestu afköst, fullur tækjaaðgangur, sannur vettvangsbragur | Tveir kóðagrunnar, hærri kostnaður, fleira starfsfólk |
| React Native | Einn JavaScript-kóðagrunnur, raunverulegir innlendir íhlutir, hröð endurtekning | Rammaháð, brúarflækja, eiginleikatöf |
| Flutter | Einn kóðagrunnur, samfellt viðmót, sterk afköst | Dart-færni sjaldgæfari, stærra forrit, eigið íhlutalíkan |
| Framsækið vefforrit | Engin búð, samstundis uppfærslur, einn vefkóðagrunnur | Takmarkaðir tækjaeiginleikar, veikari viðvera, vettvangstakmörk |
| Þvingaðar uppfærslur | Fjarlægir óöruggar gamlar útgáfur fljótt | Pirrar notendur ef ofnotað. Getur hindrað aðgang |
| Skírteinafesting | Sterk vernd gegn hlerun | Brotnar ef skírteini snúast án forritsuppfærslna |

Endurtekna málamiðlunin er útbreiðsla og afhendingarhraði gegn dýpt og trúverðugleika. Innlent gefur ríkustu, trúverðugustu upplifunina en kostar mest að smíða og viðhalda. Þverpalla- og PWA-nálganir spara fyrirhöfn og víkka útbreiðslu, með einhverjum kostnaði í vettvangsbrag eða tækjaaðgangi. Fyrir lítið teymi sem afhendir eyðublöð og efni er að deila kóðagrunni oft skynsamlegt. Fyrir kröfuhart neytendaforrit getur innlend dýpt verið verðsins virði. Ákveddu með allan líftíma forritsins í sjónmáli, ekki bara opnunina.

## Spurningar til að ræða með teyminu

1. **Hve lengi styðjum við gamla biðlara á vettvangi og er API okkar útgáfumerkt til að halda þeim virkum?** Því notendur velja hvenær þeir uppfæra hefurðu alltaf margar útgáfur af forritinu uppsettar í einu, og bakendabreyting sem gerir ráð fyrir að allir séu núgildandi mun brjóta langa halann af eldri biðlurum. Ákveddu afturábaksamhæfisglugga þinn, útgáfumerktu API svo gamalt forrit haldi áfram að virka og haltu sjaldan notaðri þvingaðri uppfærsluleið fyrir útgáfur sem eru raunverulega óöruggar. Þetta skiptir máli fyrir bæði borgaraforrit hins opinbera og vinnuaflsforrit fyrirtækja, þar sem fólk á gömlum tækjum getur ekki eða vill ekki uppfæra á þínum tímaáætlun. Komdu með núverandi útgáfudreifingargögn og spyrðu hvað brotnar fyrir elsta biðlarann sem enn er í raunverulegri notkun. Ef þú veist ekki þá dreifingu skaltu mæla hana áður en þú afhendir næstu brjótandi breytingu.

2. **Hver er viðmið okkar til að senda ýtitilkynningu og hver ákveður hvað er þess virði að trufla notanda?** Ýtitilkynningar ná til fólks þegar forritið er lokað, sem gerir þær öflugar og auðvelt að misnota, og notendur afvirkja tilkynningar (eða eyða forritinu) frá vörum sem ganga of langt. Komdu þér saman um hvað telst raunverulegt gildi, hvernig notendur stýra tíðni og rás og hvernig þú heiðrar vettvangssamþykki frekar en að nöldra um heimild. Án sameiginlegs viðmiðs mun hvert teymi með mælikvarða að ná grípa í ýtingu, og öll rásin hnígur í hávaða. Komdu með tilkynningarnar sem þú sendir síðasta mánuð og spyrðu hverjum notandinn hefði þakkað þér fyrir. Ef flestar voru kynningartilkynningar skaltu herða stefnuna áður en afþökkunarhlutfallið gerir það fyrir þig.

3. **Er afhendingarleiðsla okkar fyrir smáforrit raunveruleg, með undirritun, tækjabúi og beta-dreifingu, eða er útgáfa stressandi handvirkt óðagot?** Farsímar bæta við hættum sem vefurinn hefur ekki: búðarrýni getur seinkað eða hafnað útgáfu, undirritunarlykla og búðarauðkennisgögn þarf að meðhöndla örugglega og vélbúnaður og skynjarar eru nógu ólík til að hermar feli raunveruleg vandamál. Að sjálfvirknivæða smíðar, prófanir, undirritun og búðarinnsendingu gegnum CI/CD, með beta-dreifingu til prófenda og skýjatækjabúi sem dekkar gerðirnar sem notendur þínir bera í raun, er það sem breytir útgáfum úr hetjudáðum í rútínu. Ákveddu hver á leiðsluna og undirritunarlyklana og hvernig búðarrýnitími er byggður inn í hverja útgáfuáætlun. Komdu með söguna af síðustu útgáfu þinni og teldu handvirku skrefin. Hvert þeirra er staður þar sem stressandi útgáfa getur farið úrskeiðis undir fresti.

4. **Höfum við valið innlent, þverpalla eða framsækið vefforrit fyrir allan líftíma þessarar vöru, eða aðeins fyrir opnunardaginn?** Smíðanálgunin er stærsta einstaka vogarstöngin á kostnað og getu smáforrits árum saman, og val gert til að afhenda hratt getur fangað þig: innlent kaupir ríkasta tækjaaðgang og vettvangsbrag á verði tveggja kóðagrunna og tveggja færnisetta, á meðan þverpalla og PWA deila kóða en bæta við rammaháð eða missa aðgang að sumum tækjaeiginleikum. Fyrir stórt teymi knýr þessi ákvörðun ráðningar, viðhaldsfjárhagsáætlun og hve hratt þú getur tekið upp hverja árlega stýrikerfisútgáfu, svo hún verðskuldar skýran eiganda frekar en sjálfgefið sett af þeim sem skrifaði fyrstu frumgerðina. Komdu með nauðsynlega tækjaeiginleika, afkastasnið, viðhaldssjóndeildarhring og færnina sem þú getur í raun ráðið, og vertu heiðarlegur um hvaða vettvangseiginleika þú myndir fórna undir hverjum valkosti. Í fyrirtækja- og opinberu umhverfi skaltu vega hvort forritið sé langlíf skuldbinding sem verður að lifa af starfsmannaveltu og áratug vettvangsbreytinga, og skrá ákvörðunina og rökstuðning hennar svo framtíðarteymi þurfi ekki að giska hvers vegna kóðagrunnurinn lítur út eins og hann gerir.

5. **Hvaða tækja- og stýrikerfisútgáfustuðningssvið þurfa raunverulegir notendur okkar og erum við að prófa á vélbúnaðinum sem þeir bera í raun frekar en símunum á skrifborðum okkar?** Sundrun er eðlilegt ástand farsíma: notendur spanna breitt svið skjástærða, tækjaafls og stýrikerfisútgáfa, og forrit stillt á flaggskip teymisins mun afhendast hægt eða bilað á hóflega vélbúnaðinum sem stór hluti áheyrendahóps þíns á. Að setja stuðningssvið er málamiðlun milli útbreiðslu og fyrirhafnar, því hver eldri gerð og stýrikerfisútgáfa sem þú lofar að styðja víkkar prófunarfylkið og viðhaldsbyrðina, svo sviðið verður að koma af raunverulegum notkunargögnum frekar en forsendu. Komdu með tækja- og stýrikerfisútgáfudreifingu þína, gerðirnar sem skýjatækjabú eða stofa dekkar nú og afköstin sem þú hefur mælt á lágbúnaði, ekki bara hermum. Fyrir borgaraforrit hins opinbera er þetta nánast óumsemjanlegt, því þú verður að þjóna öllum þar á meðal fólki á gömlum tækjum og hægum tengingum undir aðgengisskyldum, og fyrir fyrirtækjaflota ættirðu að prófa nákvæmlega hrjúfu handtækin sem starfsfólk ber frekar en almennt úrtak.

6. **Hvaða viðkvæm gögn búa á tækinu og er hvert varið gegn síma sem er týndur, stolinn eða í annarra höndum?** Farsími ferðast í vasa og týnist eða er stolið, svo hvert gagn eða leyndarmál geymt í skýrri skrá er einum týndum síma frá afhjúpun, og sprengjusvæðið vex með hverjum notanda. Sjónarmiðin toga hvert gegn öðru: skyndiminnisgeymsla gagna á tækinu er það sem gerir ótengt fyrst virkt og forritið hratt, samt er hvert geymt atriði skuld sem verður að sitja í öruggri geymslu vettvangsins (iOS Keychain eða Android Keystore), vera lágmörkuð og helst vörð með lífkennum eða aðgangskóða. Komdu með skrá yfir nákvæmlega hvað forritið geymir staðbundið, hvar hvert atriði er geymt, hvað opnar það og hvort tengingar með miklum hagsmunum nota skírteinafestingu með vinnanlegri snúningsáætlun. Í fyrirtækjaumhverfi skaltu tengja þetta við farsímatækjastjórnunarstefnu og fjareyðingu og í opinberu umhverfi skaltu líta á persónugögn á tækinu sem persónuverndar- og lagalega útsetningu sem verður að réttlæta, skjalfesta og verja undir úttekt.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með örlítið teymi og lítið svigrúm hefurðu sjaldan efni á tveimur innlendum kóðagrunnum eða tveimur færnisettum, svo þverpalla rammi eða jafnvel PWA sem nær báðum búðum úr einum kóðagrunni vinnur yfirleitt. Afhentu ótengt fyrst fyrir eina kjarnaverkið sem skiptir máli, haltu hvaða tákni sem er í öruggri geymslu frekar en skýrri skrá og byggðu búðarrýnitíma inn í hverja útgáfu svo höfnun sprengi ekki opnunardag. Slepptu þvinguðum uppfærslum, skírteinafestingu og tækjabúi þar til raunveruleg notkun réttlætir þau.

**Lítið fyrirtæki.** Án sérstaks farsímasérfræðings og með þröngt fjárhagsáætlun skaltu hallast fast að kaupum yfir smíði: forritasmið án kóða, hvítmerkt forrit frá sölustaða- eða bókunarsöluaðila þínum eða vel gert PWA af núverandi vef þínum slær oft sérsmíðað forrit sem þú getur ekki viðhaldið. Ef þú pantar forrit skaltu eiga undirritunarlyklana og búðarreikningana sjálfur svo verktaki geti ekki haldið viðveru þinni í gíslingu, og krefjast aðgengis og öruggrar geymslu á tækinu í samningnum. Haltu umfanginu við eitt eða tvö verk sem viðskiptavinir vinna í raun á síma.

**Stórfyrirtæki.** Í stærð er forritið langlíf skuldbinding yfir mörg teymi, svo staðlaðu smíðanálgunina, öruggu geymslumynstrið, CI/CD-leiðsluna og API-útgáfumerkingarstefnuna frekar en að láta hverja vöru finna þau upp aftur. Innri vinnuaflsforrit flæða yfirleitt gegnum farsímatækjastjórnun fyrir uppsetningu, stillingu, fjareyðingu og stefnu, á meðan viðskiptavinaforrit þurfa tækjabú sem dekkar raunverulega notkun og úttekið aðgengi og öryggi. Stýrðu undirritunarlyklum, búðarauðkennisgögnum og útgáfutíma miðlægt svo brjótandi bakendabreyting skilji aldrei langa halann af eldri biðlurum eftir strandaðan.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta hvert val. Þú verður að þjóna öllum, þar á meðal fólki á gömlum tækjum og hægum tengingum, svo aðgengi er lagaskylda staðfest með raunverulegum hjálpartækjum og breitt tækjastuðningssvið er nánast óumsemjanlegt. Kjóstu nálganir og samninga sem forðast söluaðilabindingu, halda gögnum flytjanlegum og leyfa almenningi að skoða hvað forritið gerir við gögn þeirra, og líttu á persónugögn á tækinu sem útsetningu sem þú verður að réttlæta og skjalfesta undir úttekt.

## Dæmi

**Sprotafyrirtæki.** Þriggja manna sprotafyrirtæki sem smíðar venjurakningarforrit þurfti að ná bæði til iOS og Android en hafði ekki efni á tveimur innlendum kóðagrunnum eða tveimur færnisettum. Þau völdu þverpalla ramma svo eitt lítið teymi gæti afhent í báðar búðir og hönnuðu ótengt fyrst frá byrjun svo notandi gæti skráð venju í neðanjarðarlest án merkis og samstillt síðar. Þau héldu innskráningartákninu í öruggri geymslu vettvangsins frekar en skýrri skrá, byggðu búðarrýnitíma inn í hverja útgáfuáætlun og prófuðu á nokkrum ódýrum eldri símum við hlið eigin, sem greip sljóa afkastagetu sem þau hefðu annars afhent.

**Stórfyrirtæki.** Flutningafyrirtæki smíðaði innra forrit fyrir ökumenn sína og vöruhúsastarfsfólk. Því vöruhús og afhendingarleiðir hafa blettótt merki valdi teymið ótengt fyrst hönnun: skannanir og stöðuuppfærslur vistast staðbundið og samstillast þegar tenging snýr aftur. Þau notuðu þverpalla ramma til að þjóna einum kóðagrunni á báða vettvanga með litlu teymi. Forritinu er dreift gegnum farsímatækjastjórnun frekar en opinberu búðirnar, svo upplýsingatækni stýrir uppsetningu, stillingu og öryggisstefnu á fyrirtækjatækjum. Viðkvæm auðkennisgögn búa í öruggri geymslu vettvangsins og lífkenni opna forritið. Skýjatækjabú prófar dæmigert svið hrjúfu handtækjanna sem starfsfólk ber í raun.

**Hið opinbera.** Landsbundin stofnun afhenti borgarasnúið forrit fyrir auðkenni og bætur. Aðgengi var hörð krafa frá fyrsta degi: fullur skjálesarastuðningur, kvik textastærð og sterkt birtuskil, prófað með raunverulegum hjálpartækjum til að mæta lögum. Því borgarar nota gríðarlegt svið tækja studdi teymið breitt band eldri gerða og hægra tenginga og hélt kjarnaverkum virkum ótengdum. Viðkvæm gögn haldast í öruggri tækjageymslu, lífkenni vernda aðgang og tengingar með miklum hagsmunum nota skírteinafestingu með skipulögðu snúningsferli. API-útgáfumerking heldur eldri uppsettum forritum virkum og sjaldan notuð þvinguð uppfærsluleið er til fyrir öryggislagfæringar. Búðarrýnitímalínur eru byggðar inn í hverja útgáfuáætlun.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Farsímar eru þar sem margir notendur mæta þjónustu þinni, svo forritið hefur áhrif á upptöku, ánægju og klárun verka sem skipta skipulagsheild þína máli. Hratt, áreiðanlegt, vel hannað forrit eykur notkun og dregur úr stuðningsálagi. Fyrir fyrirtæki getur innra farsímaforrit gert farsímavinnuafl mælanlega afkastameira og skorið pappírsvinnu. Fyrir ríkisstjórnir víkkar nothæft borgaraforrit aðgang og dregur úr eftirspurn eftir símaverum og persónulegri þjónustu.

Hvað heildareignarkostnað (TCO) varðar er val á nálgun stærsta vogarstöngin. Innlent þýðir að borga fyrir tvo kóðagrunna og tvö færnisett yfir allan líftíma forritsins. Þverpalla skiptir einhverju af því fyrir ósjálfstæði sem þú verður að halda núgildandi. Umfram kóða skaltu fjárhagsáætla búðargjöld og rýnilotur, tækjaprófunarstofu eða skýjabú, viðvarandi stýrikerfisútgáfustuðning þar sem vettvangar gefa út árlega og öryggisvinnuna sem farsímar krefjast. Kostnaður vanfjárfestingar birtist í hrunum á óstuddum tækjum, öryggisatvikum af óvörðum gögnum á tækinu, hafnaðar eða seinkaðar útgáfur og notendur sem yfirgefa hægt eða klaufalegt forrit.

Til að færa rök við forystu skaltu tengja forritið við áþreifanlegar niðurstöður: verkklárun, varðveislu, vinnuaflsframleiðni eða minnkaðan stuðningskostnað. Verðleggðu alla nálgunarákvörðunina yfir líftíma forritsins, ekki bara fyrstu útgáfu, og nefndu áhætturnar (öryggi, aðgengislög, búðarhöfnun) sem alvarleg farsímavinnubrögð draga úr.

## Andmynstur og gildrur

- **Að meðhöndla farsíma sem smækkaða vefsíðu**: að hunsa snertingu, bendingar og vettvangsvenjur.
- **Að gera ráð fyrir fullkomnu neti**: engin ótengd meðhöndlun, svo forritið brotnar um leið og merki fellur.
- **Að prófa aðeins á nýjasta flaggskipinu**: felur léleg afköst á tækjunum sem raunverulegir notendur bera.
- **Að geyma leyndarmál í skýrum skrám**: viðkvæm gögn afhjúpuð þegar tæki týnist eða er stolið.
- **Tilkynningaofgnótt**: of margar ýtingar, svo notendur þagga niður eða eyða forritinu.
- **Að hunsa búðarrýnitíma**: útgáfuáætlanir sem gera ráð fyrir tafarlausri útgáfu og skrika síðan.
- **Engin þvinguð uppfærsluleið**: óöruggar gamlar útgáfur lifa áfram án leiðar til að leggja þær niður.
- **Rafhlöðu- og gagnatæming**: stöðug bakgrunnsvinna og málglað net sem notendur taka eftir.
- **Aðgengi sem eftirþanki**: útilokar notendur og, hjá hinu opinbera, brýtur lög.
- **Einn kóðagrunnur þvingaður til að líta eins út alls staðar**: forrit sem finnst framandi á báðum vettvöngum.

## Þroskalíkan

**Stig 1: Upphaf.** Farsímar eru ad hoc og viðbragðsdrifnir. Forritið er smíðað eins og vefsíða, prófað á eigin símum teymisins og brotnar oft ótengt. Lítil hugsun fer í örugga geymslu, aðgengi eða búðarrýnitímalínur. Útgáfur eru stressandi handvirkt óðagot og enginn á smíðanálgunina eða undirritunarlyklana.

**Stig 2: Þróun.** Grunnvinnubrögð birtast, en ósamræmd milli teyma og vara. Smíðanálgun er valin fyrir tiltekið forrit, það fylgir vettvangsgrunnatriðum og er prófað á nokkrum raunverulegum tækjum og einhver ótengd meðhöndlun og örugg geymsla er til. Smíðar eru að hluta sjálfvirkar og einhver á búðarinnsendingar, samt kann forrit annars teymis að gera allt þetta ólíkt eða alls ekki.

**Stig 3: Stöðlun.** Góð vinnubrögð eru skjalfest og framfylgd um alla skipulagsheildina. Ótengt-fyrst er sjálfgefið, skjalfest tækjastuðningssvið er prófað á tækjastofu eða skýjabúi og vettvangshönnunarleiðbeiningum og aðgengi er fylgt og staðfest með raunverulegum hjálpartækjum. Örugg geymsla, lífkenni og API-útgáfumerking eru staðall, CI/CD sjálfvirknivæðir smíðar, prófanir, undirritun og beta-dreifingu og búðarrýnitími er skipulagður inn í hverja útgáfu.

**Stig 4: Stjórnun.** Farsímagæði eru mæld og stýrð gegn grunnlínum. Hrun, kaldræsingar- og skjábirtingarafköst, rafhlöðu- og gagnanotkun og verkklárunarhlutföll eru fangað samfellt frá raunverulegum tækjum og rakin gegn markmiðum, með sundurliðun eftir gerð og stýrikerfisútgáfu svo afturför á lágbúnaði sé gripin, ekki afhent. Aðgengi og öryggi eru úttekin frekar en gert ráð fyrir, tilkynningaafþökkunar- og uppfærsluupptökuhlutföll eru vöktuð og stuðningssvið og smíðanálgun eru rýnd á þeim sönnunargögnum. Ákvarðanir um að drepa eða laga útgáfu hvíla á mælikvörðum, ekki á hvernig forritið fannst á síma leiðtogans.

**Stig 5: Samhæfing.** Farsímar eru stöðugt bættir og samþættir um skipulagsheildina, og þeir aðlagast þegar tækjalandslagið breytist. Skírteinasnúningur, þvingaðar uppfærsluleiðir og afturköllun eru rútína, stuðningssvið og smíðanálgun eru endurmörkuð á sönnunargögnum þar sem vettvangar gefa út árlega og allt svið notenda og tækja er meðhöndlað sem fyrsta flokks. Farsímaskipulagning er samtengd öryggi, aðgengi, API og afhendingarvinnubrögðum, svo stýrikerfisbreyting, nýtt tækjaþrep eða stefnubreyting sé tekin upp sem rútínuvinna frekar en neyðartilvik.

## Hugmyndir til umræðu

- Hvernig ákveðurðu milli innlends, þverpalla og framsækins vefforrits fyrir tiltekna vöru?
- Hvaða tækja- og stýrikerfisútgáfustuðningssvið passar við raunveruleg notendagögn þín og hvernig heldurðu því núgildandi?
- Hvar er ótengt fyrst nauðsynlegt í forritinu þínu og hvernig muntu meðhöndla samstillingarárekstra?
- Hvenær er þvinguð uppfærsla réttlætanleg og hvernig forðastu að hindra notendur ósanngjarnt?
- Hvernig muntu prófa á raunverulegum tækjum í stærð sem endurspeglar notendur þína?
- Hvaða viðkvæm gögn búa á tækinu og hvernig er hvert vernd?
- Hvernig virðirðu venjur hvers vettvangs úr sameiginlegum kóðagrunni?

## Helstu atriði

- Veldu smíðanálgunina (innlent, þverpalla eða PWA) fyrir allan líftíma forritsins.
- Fylgdu vettvangshönnunarleiðbeiningum svo forritið finnist kunnuglegt og lækki fyrirhöfn notenda.
- Hannaðu fyrir farsímaskorður: ótengt fyrst, sparsöm rafhlaða og gögn, sundrun, litla skjái.
- Þú stýrir ekki útgáfutíma. Skipuleggðu fyrir búðarrýni, útgáfumerkingu og þvingaðar uppfærslur.
- Notaðu ýtitilkynningar og djúptengla af hófsemi og samþykki.
- Tryggðu gögn á tækinu með öruggri geymslu, lífkennum og, þar sem réttlætanlegt, skírteinafestingu.
- Prófaðu á raunverulegum tækjum og sjálfvirknivæddu farsímaleiðsluna gegnum CI/CD.
- Gerðu aðgengi að kröfu, sem fyrir hið opinbera er lögbundið.

## Heimildir og frekari lestur

- Apple, *Human Interface Guidelines*
- Google, *Material Design* guidelines
- Apple, *App Store Review Guidelines*
- Google, *Google Play developer policies and Android developer documentation*
- OWASP, *Mobile Application Security Verification Standard (MASVS)* and *Mobile Security Testing Guide*
- React Native project documentation
- Flutter project documentation
- Google, *web.dev* guidance on progressive web apps
- U.S. Section 508 and WCAG (Web Content Accessibility Guidelines) references for mobile accessibility
- NIST, *Guidelines on mobile device security and management*
