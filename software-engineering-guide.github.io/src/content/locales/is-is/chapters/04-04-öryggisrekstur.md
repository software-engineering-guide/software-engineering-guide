# 4.4 Öryggisrekstur

## Yfirlit og tilgangur

Forvörn er nauðsynleg en aldrei nóg. Ákveðnir andstæðingar, nýir veikleikar og einföld mannleg mistök þýða að sumar ógnir munu sleppa framhjá vörnum þínum. Öryggisrekstur er sú grein að finna þær hratt, bregðast vel við og færa það sem þú lærir aftur í sterkari varnir. Hann er munurinn á atviki sem er afmarkað á mínútum og atviki sem grefur um sig mánuðum saman áður en nokkur tekur eftir.

Í stórri skipulagsheild verður öryggisrekstur að virka í stærð og á hraða. Þúsundir þjónusta framleiða höf af skrám. Hundruð nýrra veikleika eru birt í hverri viku. Uppsetning stoppar aldrei. Handvirkur, handverkskenndur rekstur heldur einfaldlega ekki í við. Svarið er að fella öryggi inn í afhendingarleiðsluna ([DevSecOps](https://en.wikipedia.org/wiki/DevSecOps)), sjálfvirknivæða greiningu og viðbrögð og byggja upp vöðvann til að meðhöndla atvik rólega þegar þau skella á. Fyrir hið opinbera ber öryggisrekstur líka lögbundnar skyldur: fyrirskipaða tímafresti til atvikaskýrslna, samræmda veikleikaupplýsingu og réttarrannsóknarnákvæmni sem stenst lagalega athugun.

Þessi kafli nær yfir að samþætta öryggi í leiðsluna, stýra veikleikum og plástrun, bregðast við atvikum og framkvæma réttarrannsóknir, keyra greiningu gegnum [SIEM](https://en.wikipedia.org/wiki/Security_information_and_event_management) og SOAR og staðfesta varnir gegnum rauða og fjólubláa liðið og [innbrotspróf](https://en.wikipedia.org/wiki/Penetration_test).

## Meginreglur

- **Sjálfvirknivæddu rútínuna.** Vélar meðhöndla skönnun, fylgni og endurtekin viðbrögð svo menn einbeiti sér að dómgreind.
- **Færðu öryggi inn í leiðsluna.** Prófanir og hlið búa í [CI/CD](https://en.wikipedia.org/wiki/CI/CD) (samfelldri samþættingu og samfelldri afhendingu), sem gefur hraða endurgjöf þar sem verkfræðingar vinna nú þegar.
- **Gerðu ráð fyrir broti og undirbúðu.** Æfðu atvikaviðbrögð áður en þú þarfnast þeirra. Atvikið er ekki tíminn til að spinna.
- **Mældu og styttu tíma.** Meðaltími til greiningar og meðaltími til viðbragða eru mikilvægustu mælikvarðarnir.
- **Nám án sakbendingar.** Hvert atvik og næstum-slys verður lærdómur sem herðir kerfið, ekki leit að einhverjum til að refsa.
- **Staðfestu varnir andstæðingslega.** Prófaðu öryggi þitt eins og raunverulegir árásaraðilar myndu gera og lagaðu það sem þeir finna.
- **Greiningarverkfræði er vara.** Líttu á greiningar sem kóða: útgáfustýrðar, prófaðar og stöðugt bættar.

## Ráðleggingar

### Byggðu DevSecOps inn í leiðsluna

Samþættu sjálfvirka öryggisprófun beint í samfellda samþættingu og afhendingu svo endurgjöf nái verkfræðingum innan mínútna:

- **[SAST](https://en.wikipedia.org/wiki/Static_application_security_testing)** (Static Application Security Testing) greinir frumkóða fyrir veikleikamynstur um leið og hann er innritaður.
- **[DAST](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)** (Dynamic Application Security Testing) kannar keyrandi forritið fyrir nýtanlega galla.
- **SCA** (Software Composition Analysis) merkir þekkt berskjölduð ósjálfstæði.
- **IaC-skönnun** athugar innviði-sem-kóða fyrir óöruggar stillingar áður en þær eru settar upp.
- **Leyndarmálaskönnun** hindrar auðkennisgögn í að komast inn í hugbúnaðarsafnið.

Stilltu þessi verkfæri miskunnarlaust til að stýra röngum jákvæðum. Skanni sem hrópar „úlfur“ er hunsaður. Settu áhættubyggð hlið: hindraðu á alvarlegum niðurstöðum með mikilli vissu og raktu restina án þess að stöðva afhendingu. Þú vilt hratt, treyst merki, ekki vegg af hávaða.

### Stýrðu veikleikum og plástraðu kerfisbundið

Stöðugur straumur veikleika kallar á kerfisbundið, forgangsraðað ferli, ekki ferskt hræðslukast við hverja fyrirsögn.

- Haltu nákvæmri eignaskrá svo þú vitir hvað gæti orðið fyrir áhrifum af tilteknum veikleika.
- Forgangsraðaðu úrbótum eftir raunverulegri áhættu: sameinaðu alvarleika, nýtanleika (er verið að nýta það í umhverfinu?), útsetningu og mikilvægi eignar frekar en að plástra eftir hráum stigafjölda einum.
- Skilgreindu og framfylgdu **úrbótaþjónustusamningum** (SLA) eftir alvarleikaþrepi og mældu fylgni.
- Sjálfvirknivæddu plástrun þar sem þú getur gert það örugglega, sérstaklega fyrir innviði og ósjálfstæði.
- Rektu **samræmda veikleikaupplýsingu** með skýrri innsendingarrás og, þar sem við á, [villuverðlaun](https://en.wikipedia.org/wiki/Bug_bounty_program), svo utanaðkomandi rannsakendur geti tilkynnt galla á ábyrgan hátt í stað þess að varpa þeim opinberlega.

### Undirbúðu og framkvæmdu atvikaviðbrögð

Þegar atvik skellur á er æft ferli meira virði en hvaða verkfæri sem er.

- Haltu **atvikaviðbragðsáætlun** með skilgreindum hlutverkum (atvikastjóra, samskiptastjóra, rannsakendum), alvarleikaflokkum og stigmögnunarleiðum.
- Settu skýr skeið: **undirbúning, greiningu og rannsókn, afmörkun, upprætingu, endurheimt og atvikarýni.**
- Varðveittu sönnunargögn rétt fyrir **[réttarrannsóknir](https://en.wikipedia.org/wiki/Digital_forensics)**: fangaðu skrár, minni og diskmyndir með skjalfestri vörsluslóð svo niðurstöður haldi lagalega og greining sé traust.
- Skipuleggðu **innbrotssamskipti** fyrirfram: hver tilkynnir viðskiptavinum, eftirlitsaðilum og almenningi, á hvaða tímalínu, með þátttöku lögfræði og almannatengsla. Regluverksklukkur (oft 72 klukkustundir eða minna) byrja að tifa við uppgötvun.
- Haltu **borðæfingar** reglulega svo teymið þekki áætlunina fyrir raunverulega kreppu og framkvæmdu atvikarýnir án sakbendingar sem skila áþreifanlegum umbótum.

### Reku greiningu með SIEM og SOAR og verkfræddu greiningar

Safnaðu öryggismerkjum þínum saman og bregstu við þeim í stærð.

- Notaðu **SIEM** (Security Information and Event Management) til að safna saman og tengja skrár og atburði yfir búið og draga fram grunsamleg mynstur.
- Notaðu **SOAR** (Security Orchestration, Automation, and Response) til að sjálfvirknivæða flokkunar- og viðbragðsleikbækur: að auðga viðvaranir, einangra gestgjafa, afvirkja auðkennisgögn og opna mál án þess að bíða eftir manneskju fyrir rútínuskref.
- Æfðu **greiningarverkfræði**: líttu á greiningarreglur sem útgáfustýrðan, prófaðan kóða samstilltan ramma eins og [MITRE ATT&CK](https://en.wikipedia.org/wiki/MITRE_ATT%26CK), mældu réttu og röngu jákvæðu hlutföll þeirra og bættu samfellt þekju á raunverulegum aðferðum andstæðinga.
- Tryggðu alhliða, fikthelda skráningu yfir forrit og innviði. Þú getur ekki greint það sem þú skráir ekki.

### Staðfestu varnir með rauðu og fjólubláu liði og innbrotsprófum

Að prófa varnir þínar eins og árásaraðili myndi gera er eina leiðin til að vita að þær virki í raun.

- **Innbrotspróf** veita markvisst, augnabliksmat á tilteknum kerfum, oft vegna regluvörslu.
- **[Rautt lið](https://en.wikipedia.org/wiki/Red_team)** hermir raunhæfan andstæðing sem eltir markmið yfir umhverfi þitt og prófar greiningu og viðbrögð jafnt og forvörn.
- **Fjólublátt lið** leiðir árásaraðila (rauða) og varnarmenn (bláa) saman í samvinnu svo hver hermd árás bæti strax greiningar og stýringar og breyti æfingu í varanlega getu.
- Færðu allar niðurstöður aftur í greiningarverkfræði, úrbætur og þjálfun.

## Málamiðlanir: kostir og gallar

| Ákvörðun | Kostir | Gallar |
|---|---|---|
| Hindrandi leiðsluhlið | Stöðvar þekkt vandamál frá því að afhendast | Núningur, rangt jákvætt pirrar teymi |
| Óhindrandi skönnun | Lítill núningur, hröð afhending | Vandamál geta farið út. Krefst aga til að laga |
| Eigin SOC | Djúpt samhengi, full stjórn | Dýrt, erfitt að manna allan sólarhringinn |
| Stýrð greining/viðbrögð | Sólarhringsþekja, sérfræðiþekking við hönd | Minna samhengi, söluaðilaháð |
| Sjálfvirk plástrun | Hröð, lokar gluggum fljótt | Hætta á brjótandi breytingum |
| Tíð rauðliðaæfing | Raunhæf sannprófun, finnur raunveruleg bil | Kostnaðarsöm, tilfangafrek |
| Villuverðlaunaáætlun | Hópfjármögnuð uppgötvun, góð þekja | Flokkunarbyrði, greiðslukostnaður, hávaði |

Kjarnaspennan er hraði gegn tryggingu, og þekja gegn kostnaði. Hindrandi hlið og sjálfvirk plástrun hámarka tryggingu en bæta við núningi og áhættu. Óhindrandi nálganir hreyfast hraðar en eru háðar eftirfylgni. Sólarhringsgreining er nauðsynleg í stærð en dýr að byggja innanhúss, sem ýtir mörgum skipulagsheildum að blendingslíkönum. Sjálfbæra leiðin sjálfvirknivæðir hárrar-vissu rútínuna, tekur frá mannlega athygli fyrir raunverulega dómgreind og heldur áfram að stilla jafnvægið með mældum útkomum frekar en ótta.

## Spurningar til að ræða með teyminu

1. **Hverjir eru úrbótaþjónustusamningar ykkar eftir alvarleika og hvað framfylgir þeim í raun?** Stöðugur straumur veikleika þarfnast kerfisbundins, forgangsraðaðs ferlis, ekki ferskts hræðslukasts við hverja fyrirsögn, og SLA eftir alvarleikaþrepi eru hvernig þú heldur í við. Ákveddu klukkur þínar (til dæmis mikilvægt á dögum, hátt á vikum) og, jafn mikilvægt, hvernig þú mælir fylgni og hver ber ábyrgð þegar frestur rennur. Forgangsraðaðu eftir raunverulegri áhættu, sameinaðu alvarleika með nýtanleika í umhverfinu, útsetningu og mikilvægi eignar, frekar en að plástra eftir hráu CVSS-stigi einu. Komdu með núverandi bakskrá opinna niðurstaðna raðaða eftir aldri og alvarleika, því óplástruð mikilvæg sem sitja framhjá glugga sínum eru sönnunargögnin sem skipta máli. Ef SLA hefur enga framfylgd og engan eiganda er það ósk, og skönnun án úrbóta byggir bara upp úttektarskuld og falska öryggistilfinningu.

2. **Þegar atvik skellur á klukkan 2 að nóttu, hver er atvikastjórinn og hve hratt byrjar regluverksklukkan?** Æft ferli er meira virði en nokkurt verkfæri, svo þú þarft nefnd hlutverk (atvikastjóra, samskiptastjóra, rannsakendur), skilgreind alvarleikastig og stigmögnunarleiðir skrifaðar niður fyrir kreppuna. Regluverksklukkur ganga oft 72 klukkustundir eða minna og byrja við uppgötvun, svo ákveddu fyrirfram hver tilkynnir viðskiptavinum, eftirlitsaðilum og almenningi og staðfestu að lögfræði og almannatengsl séu með. Að varðveita réttarsönnunargögn með skjalfestri vörsluslóð verður að gerast áður en nokkur endurbyggir brotinn gestgjafa, annars taparðu getunni til að skilja eða sanna hvað átti sér stað. Komdu með dagsetningu síðustu borðæfingar þinnar, því ef hún var fyrir löngu eða aldrei er áætlun þín óprófuð. Fyrir opinber teymi gera lögbundnir skýrslufrestir þetta óumflýjanlegt, svo æfðu tilkynningarleiðina, ekki bara tæknileg viðbrögð.

3. **Hvaða rútínuviðbragðsaðgerðir munuð þið leyfa SOAR að taka án manneskju í lykkjunni?** Sjálfvirkni er kraftmargföldun sem leyfir grönnu teymi að þekja stórt bú, og mælikvarðinn sem skiptir máli er meðaltími til viðbragða, sem sjálfvirkar leikbækur geta skorið úr klukkustundum í mínútur. Ákveddu hvaða aðgerðum hárrar vissu (að einangra gestgjafa, afturkalla auðkennisgagn, opna mál) þú treystir til að keyra sjálfvirkt og hverjar þurfa mannlega dómgreind fyrst. Hættan er að rangt jákvætt kveiki truflandi aðgerð, svo tengdu sjálfvirkni við greiningargæði og stilltu miskunnarlaust, því kerfi sem hrópar „úlfur“ er slökkt á. Komdu með núverandi viðvörunarmagn og rangt-jákvætt hlutfall, því þær tölur segja þér hvaða leikbækur eru öruggar að sjálfvirknivæða í dag. Ef hvert viðbragðsskref bíður eftir manneskju muntu ekki halda í við í stærð, og dvalartími, sem knýr innbrotskostnað, mun haldast hár.

4. **Hvaða leiðsluniðurstöður hindra útgáfu, hverjar eru aðeins raktar og hver heldur rangt-jákvætt hlutfalli nógu lágu til að verkfræðingar treysti enn hliðinu?** Skanni sem hrópar „úlfur“ er hunsaður, og um leið og verkfræðingar missa trú á hliði þrýsta þeir á að fjarlægja það, svo gildi DevSecOps hvílir á merkjagæðum frekar en hráþekju. Spennan er raunveruleg: hindraðu á of litlu og berskjölduð kóði fer út. Hindraðu á of miklu og þú bætir við núningi, hægir á afhendingu og brennir velvild. Komdu með réttu og röngu jákvæðu hlutföll hvers skanna (SAST, DAST, SCA, IaC og leyndarmálaskönnun), hve oft teymi sniðganga eða bæla hlið og aldur niðurstaðnanna sem þú aðeins rekur án þess að laga. Fyrir fyrirtæki eða opinberan aðila sem rekur hundruð leiðslna skaltu setja hindra-á-móti-rekja stefnuna miðlægt og stilla hana með gögnum, því hlið sem eru handahófskennt ólík milli teyma skapa bæði úttektarbil og þá tilfinningu að öryggi sé duttlungafullt.

5. **Hve viss eruð þið um að greiningar ykkar dekki enn aðferðirnar sem raunverulegur árásaraðili myndi nota og hver á þær sem prófaðan, útgáfustýrðan kóða?** Greiningar rýrna hljóðlega eftir því sem umhverfi þitt og andstæðingar þróast, svo regluröð sem leit tæmandi út í fyrra getur misst þekju löngu áður en atvik leiðir bilið loks í ljós. Að líta á greiningar sem kóða, útgáfustýrðan, prófaðan og varpaðan á ramma eins og MITRE ATT&CK, er það sem aðgreinir verkfræðivenju frá hrúgu úreltra viðvarana, samt keppir það um sama knappa greinendatíma og lifandi flokkun. Komdu með núverandi ATT&CK-þekjukort, mælda réttu og röngu jákvæðu hlutföll helstu greininga þinna og niðurstöður síðustu fjólubláu liðsæfingar þinnar, þar sem samvinnuprófun rauðra og blárra er fljótlegasta leiðin til að sanna hvaða greiningar kvikna í raun. Í fyrirtækja- og opinberu umhverfi þar sem rammi kann að vera fyrirskipaður skaltu tengja hverja greiningu við nefndan eiganda og rýnitakt, því þekja sem enginn viðheldur er þekja sem þú uppgötvar að þú misstir aðeins eftir innbrotið.

6. **Smíðið þið greiningu og viðbrögð innanhúss, kaupið stýrða greiningu og viðbrögð eða blandið þið tvennu, og hafið þið verðlagt hvað raunveruleg sólarhringsþekja kostar?** Dvalartími knýr innbrotskostnað, svo óþaktar stundir (nætur, helgar, frídagar) eru einmitt þegar ógreindur boðflenna gerir mestan skaða, samt er að manna sólarhrings öryggisrekstrarmiðstöð innanhúss dýrt og erfitt að viðhalda. Skiptin eru samhengi og stjórn gegn kostnaði og hraða í þekju: teymi innanhúss þekkir búið djúpt en er hægt og dýrt að byggja, á meðan stýrður veitandi gefur tafarlausa sérfræðiþekkingu allan sólarhringinn á verði þynnra samhengis og söluaðilaháðar. Komdu með núverandi þekjutíma þína, meðaltíma til greiningar og viðbragða utan vinnutíma, viðvörunarmagn og heiðarlegt mat á því hvort þú getir ráðið og haldið greinendunum sem sjálfrekin miðstöð þarfnast. Fyrir hið opinbera og eftirlitsskyld fyrirtæki skaltu vega gagnabúsetu, starfsmannaöryggisvottun og lögbundnar skýrsluskyldur sem veitandinn verður að geta uppfyllt og staðfesta að samningurinn varðveiti réttarrannsóknarnákvæmni og vörsluslóð sem málsmeðferð krefst.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hraði og lífsafkoma koma fyrst, svo keyptu öryggi sem aukaafurð verkfæra sem þú rekur þegar frekar en að manna rekstur. Tengdu ókeypis skanna inn í CI til að hindra leyndarmálaleka og þekkt berskjölduð ósjálfstæði við innritun, áframsendu skrár í ódýra stýrða þjónustu með handfylli verðmikilla viðvarana og skrifaðu eins blaðsíðu atvikaáætlun (hverjum á að hringja í, hvernig á að snúa auðkennisgögnum, taka skyndimynd áður en þú endurbyggir) áður en þú þarft hana. Knappasta auðlind þín er verkfræðiathygli, svo sjálfvirknivæddu rútínuna og stattu gegn því að setja upp öryggisrekstrarmiðstöð sem þú getur ekki haldið gangandi.

**Lítið fyrirtæki.** Án sérstaks öryggissérfræðings og með þröngt fjárhagsáætlun skaltu hallast að stýrðri greiningu og viðbrögðum og öryggiseiginleikum sem eru þegar innbyggðir í vettvangana þína. Líttu á plástrun og eignaskrá sem áhrifamestu venjurnar: vittu hvað þú rekur, haltu því núgildandi og framfylgdu einföldum úrbótafresti eftir alvarleika. Kjóstu söluaðila sem sjá um sólarhringsvöktun, innsendingu samræmdrar upplýsingagjafar og réttargagnaöflun fyrir þig, og æfðu það eina sem þú getur ekki útvistað, sem er að ákveða hver lýsir yfir atviki og hver talar við viðskiptavini.

**Stórfyrirtæki.** Áskorunin er samræmi yfir mörg teymi og hundruð leiðslna: sameiginleg hindra-á-móti-rekja hliðastefna, úrbótaþjónustusamningar framfylgdir um alla skipulagsheildina, SIEM- og SOAR-vettvangur með mældum greiningum og fjólublátt lið sem breytir hverri æfingu í nýja þekju. Stýrðu öryggisrekstri sem eignasafni með mælaborðum fyrir meðaltíma til greiningar og viðbragða, SLA-fylgni og greiningarnákvæmni, og ákveddu af ásetningi hvar dýpt innanhúss slær stýrða stærð. Fjárhagsáætlaðu mannlegan eftirlitskostnað flokkunar og stillingar skýrt, því sjálfvirkni færir fyrirhöfn frekar en að fjarlægja hana.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta hvert val. Lögbundnir atvikaskýrslufrestir og samræmd veikleikaupplýsing eru skyldur frekar en valkostir, svo æfðu tilkynningarleiðina til landsyfirvalds af jafn mikilli nákvæmni og tæknileg viðbrögð, og varðveittu réttarsönnunargögn undir vörsluslóð sem stenst lagalega athugun. Kjóstu samninga sem halda greiningarrökfræði og gögnum flytjanlegum, krefstu þess að hver stýrður veitandi uppfylli búsetu- og öryggisvottunarkröfur og vænstu þess að rauðliðaæfingar og samfelld skönnun nærir heimildarferli sem almenningur getur treyst.

## Dæmi

**Sprotafyrirtæki.** Sprotafyrirtæki án öryggisrekstrarmiðstöðvar tengir ókeypis skanna inn í CI-leiðslu sína svo leyndarmálaleka og þekkt berskjölduð ósjálfstæði sé gripið við innritun, hindrar aðeins á niðurstöðum með mikilli vissu svo verkfræðingarnir tveir drukkni ekki í hávaða. Þeir skrifa eins blaðsíðu atvikaáætlun áður en þeir þurfa hana: hverjum á að hringja í, hvernig á að snúa auðkennisgögnum og að taka skyndimynd af brotnum gestgjafa áður en hann er endurbyggður svo þeir geti lært hvað gerðist. Þeir áframsenda skrár í ódýra stýrða þjónustu og setja fáar viðvaranir á atburðina sem í raun myndu gefa til kynna innbrot, svo vandamál birtist á klukkustundum frekar en mánuðunum sem það tekur að taka eftir af tilviljun.

**Stórfyrirtæki.** Hugbúnaður-sem-þjónusta fyrirtæki rekur SAST, SCA, IaC og leyndarmálaskönnun í hverri leiðslu, hindrar aðeins á alvarlegum niðurstöðum með mikilli vissu og rekur restina á mælaborði með úrbótaþjónustusamningum. SIEM nærir SOAR-vettvang sem einangrar gestgjafa sjálfvirkt og afturkallar auðkennisgögn á viðvörunum með mikilli vissu og sker meðaltíma til viðbragða úr klukkustundum í mínútur. Ársfjórðungslegar fjólubláar liðsæfingar gegn MITRE ATT&CK aðferðum búa beint til nýjar greiningarreglur og loka þekjubilum jafnt og þétt.

**Hið opinbera.** Sambandsstofnun rekur öryggisrekstrarmiðstöð (SOC) með fyrirskipaðri atvikaskýrslugjöf til landsnetöryggisyfirvalds innan lögbundinna fresta. Hún rekur samræmda veikleikaupplýsingaáætlun með opinberri innsendingarrás eins og stefna krefst og varðveitir réttarsönnunargögn undir ströngum vörsluslóðarferlum hæfum fyrir málsmeðferð. Árleg rauðliðaæfingar og samfelld veikleikaskönnun næra áframhaldandi heimild stofnunarinnar og áhættubyggða úrbótaþjónustusamninga hennar.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Næstum allt í rökunum fyrir öryggisrekstri kemur niður á dvalartíma: því lengur sem árásaraðili fer ógreindur, því meira kostar innbrotið. Rannsóknir sýna stöðugt að atvik sem eru afmörkuð fljótt kosta stórlega minna en þau sem dragast mánuðum saman. Heildareignarkostnaðurinn felur í sér verkfæri (SIEM, SOAR, skanna), mönnun eða stýrðar þjónustur fyrir greiningu og viðbrögð og tímann til að byggja og æfa atvikaferli. Á móti stendur kostnaðurinn við að fjárfesta ekki: innbrot uppgötvað seint, dreifist yfir kerfi, dregur að sér eftirlitssektir, skyldubundnar tilkynningar, málaferli og mannorðsskaða, allt gert verra af ringulreið óæfðra viðbragða.

Ávöxtunin kemur af hraðari greiningu og viðbrögðum, sjálfvirkni sem leyfir grönnu teymi að þekja stórt bú og forvarnarbótum færðum aftur úr hverju atviki og æfingu. DevSecOps borgar sig sérstaklega með því að grípa vandamál í leiðslunni þar sem þau eru ódýr, frekar en í framleiðslu þar sem þau eru dýr og opinber. Þegar þú færir rök við forystu skaltu setja tölur á núverandi meðaltíma til greiningar og viðbragða, sýna hvernig þeir tengjast dvalartíma og kostnaði og ramma sjálfvirkni sem kraftmargföldun sem forðast að stækka starfsmannafjölda í takt við búið. Fyrir hið opinbera skaltu leggja áherslu á að lögbundnar skýrslu- og upplýsingaskyldur gera þroskaðan rekstur óumflýjanlegan.

## Andmynstur og gildrur

- **Viðvörunarþreyta.** Svo margar viðvaranir að greinendur loka á og missa af þeirri raunverulegu.
- **Skönnun án úrbóta.** Að búa til niðurstöður sem enginn lagar, sem skapar falska öryggistilfinningu og úttektarskuld.
- **Engin atvikaáætlun.** Að spinna í kreppu, sóa mikilvægum mínútum og mismeðhöndla sönnunargögn.
- **Að eyða sönnunargögnum.** Að endurbyggja brotinn gestgjafa áður en réttargagnaöflun er tekið og missa getuna til að skilja eða sanna hvað gerðist.
- **Sakbendingarmenning í rýni.** Að refsa viðbragðsaðilum svo næsta atvik sé falið eða meðhöndlað í vörn.
- **Regluvörslu-eingöngu innbrotspróf.** Eitt árlegt próf til að fullnægja endurskoðanda, með niðurstöðum hunsuðum til næsta árs.
- **Hindrandi hlið með miklum röngum jákvæðum.** Að tæra traust þar til verkfræðingar krefjast þess að hliðin séu fjarlægð alveg.
- **Setja-og-gleyma greiningar.** Reglur sem rotna eftir því sem umhverfi og andstæðingar þróast og missa hljóðlega þekju.

## Þroskalíkan

**Stig 1: Upphaf.** Öryggisrekstur er ad hoc og viðbragðsdrifinn. Öryggisprófun er handvirk og sjaldgæf og engin miðlæg skráning eða SIEM er til. Engin atvikaáætlun er til, svo viðbrögð eru spunnin á staðnum. Plástrun gerist aðeins þegar fyrirsögn neyðir hana og varnir eru aldrei andstæðingslega prófaðar.

**Stig 2: Þróun.** Grunnvinnubrögð birtast en eru ósamræmd milli teyma. Sumar leiðslur keyra skanna á meðan aðrar keyra enga, og miðlæg skráning er til á blettum. Grunnatvikaáætlun er skjalfest en sjaldan æfð, plástrun fylgir lausum tímalínum og árlegt innbrotspróf fullnægir regluvörslu án þess að breyta miklu. Þekja og nákvæmni fer eftir því hvaða teymi þú spyrð.

**Stig 3: Stöðlun.** Vinnubrögð eru skjalfest og framfylgt um alla skipulagsheildina. Full DevSecOps-skönnun með áhættubyggðum hliðum er beitt samræmt, SIEM tengir atburði og fyrstu SOAR-leikbækur keyra. Atvikaviðbrögð eru æfð með borðæfingum og rýnum án sakbendingar, úrbótaþjónustusamningar eftir alvarleika eru framfylgdir með nefndum eigendum og samræmd veikleikaupplýsing og regluleg rauðliðaæfingar eru normið frekar en undantekningin.

**Stig 4: Stjórnun.** Rekstur er mældur og stýrður gegn grunnlínum. Meðaltími til greiningar og viðbragða, SLA-fylgni eftir alvarleikaþrepi, skönnunarþekja, réttu og röngu jákvæðu hlutföll greininga og dvalartími eru rakin á mælaborðum og rýnd á takti. Greiningar bera mælda nákvæmni og endurheimt varpaða á MITRE ATT&CK, sjálfvirkniákvarðanir eru hliðaðar á rangt-jákvæðum gögnum frekar en von, og mælikvarði sem rekur fram hjá grunnlínu sinni kallar fram skilgreind viðbrögð í stað þess að fara óséður.

**Stig 5: Samhæfing.** Öryggisrekstur er stöðugt bættur, samþættur um skipulagsheildina og aðlögunarhæfur. Greiningarverkfræði, fjólublátt lið, úrbætur og atvikarýni nærir eina lykkju sem aðlagast nýjum aðferðum andstæðinga þegar þær koma fram. Sjálfvirkar leikbækur meðhöndla rútínuna yfir allt búið svo menn einbeiti sér að dómgreind, öryggi er skipulagt við hlið afhendingar og áhættu og hvert atvik og æfing herðir kerfið mælanlega meðan kjarnamælikvarðarnir halda áfram að stefna niður.

## Hugmyndir til umræðu

1. Hvaða leiðsluniðurstöður ættu að hindra útgáfu og hverjar ættu aðeins að vera raktar?
2. Smíða eigin SOC, nota stýrða greiningu og viðbrögð eða blanda báðu, og hvers vegna?
3. Hvernig heldurðu greiningarreglum frá því að rotna eftir því sem umhverfi þitt þróast?
4. Hve ágengt ætti að sjálfvirknivæða plástrun miðað við hættuna á brjótandi breytingum?
5. Hvernig lítur raunverulega atvikarýni án sakbendingar út í menningu þinni?
6. Hvernig mælirðu hvort rautt og fjólublátt lið séu í raun að bæta varnir þínar?

## Helstu atriði

- Forvörn bregst að lokum. Rekstur er til að greina og bregðast hratt við.
- Felldu SAST, DAST, SCA, IaC og leyndarmálaskönnun inn í leiðsluna með áhættubyggðum hliðum.
- Forgangsraðaðu plástrun eftir raunverulegum nýtanleika og mikilvægi eigna, undir framfylgdum SLA.
- Æfðu atvikaviðbrögð, varðveittu réttarsönnunargögn og skipuleggðu innbrotssamskipti fyrirfram.
- Notaðu SIEM og SOAR til að tengja og sjálfvirknivæða. Líttu á greiningar sem verkfræddan, prófaðan kóða.
- Staðfestu varnir með innbrotsprófum, rauðu liði og samvinnu um fjólublátt lið.
- Dvalartími knýr innbrotskostnað, svo meðaltími til greiningar og viðbragða eru mikilvægu mælikvarðarnir.

## Heimildir og frekari lestur

- National Institute of Standards and Technology, *SP 800-61: Computer Security Incident Handling Guide*
- National Institute of Standards and Technology, *SP 800-40: Guide to Enterprise Patch Management*
- MITRE, *ATT&CK Framework*
- Anton Chuvakin and others, *Logging and Log Management* / SIEM literature
- Jim Bird, *DevOpsSec: Securing Software through Continuous Delivery*
- Richard Bejtlich, *The Practice of Network Security Monitoring*
- FIRST, *Coordinated Vulnerability Disclosure* guidance and *CVSS* specification
