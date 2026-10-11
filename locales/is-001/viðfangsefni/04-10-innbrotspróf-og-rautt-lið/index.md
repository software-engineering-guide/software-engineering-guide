# 4.10 Innbrotspróf og rautt lið

## Yfirlit og tilgangur

Þú getur byggt hverja stýringu sem ógnarlíkan þitt kallar á og samt ekki vitað hvort þær virka. Skjölun segir að eldveggurinn loki þeirri gátt, kóðarýni segir að inntak sé staðfest, stefnan segir að lágmarksréttindum sé framfylgt. Sóknaröryggi (offensive security) er hvernig þú kemst að því hvort eitthvað af því sé satt þegar ákveðinn árásaraðili þrýstir á það. Þessi kafli fjallar um að ráðast vísvitandi á eigin kerfi, með heimild, til að finna veikleikana áður en raunverulegur andstæðingur gerir það.

Fagið liggur eftir sviði. Í léttari endanum situr [veikleikaskönnun](https://en.wikipedia.org/wiki/Vulnerability_scanner): sjálfvirk verkfæri sem kanna þekkta galla og rangstillingar. Í miðjunni situr [innbrotspróf](https://en.wikipedia.org/wiki/Penetration_test): hæfur maður sem tengir saman veikleika til að sanna nýtanleika gegn skilgreindu skotmarki. Í fjarlægari endanum situr [rautt lið](https://en.wikipedia.org/wiki/Red_team): markmiðsdrifin herferð sem líkir eftir raunverulegum andstæðingi yfir fólk, ferla og tækni, og prófar getu þína til að greina og bregðast við, ekki bara getu þína til að koma í veg fyrir. Hvert svarar annarri spurningu, og að rugla þeim er algengasta leiðin sem skipulagsheildir sóa peningum og hugga sig með falskri tryggingu.

Þessi kafli situr vísvitandi aðskilinn frá nágrönnum sínum. Kafli 4.4 fjallar um öryggisrekstur: varnar- og vöktunarhliðina sem fylgist með ógnum og bregst við þeim. Þessi kafli er sóknarhliðin sem prófar hvort sú vörn virki í raun. Kafli 4.9 fjallar um öruggan hugbúnaðarlífsferil, þar sem öryggi er byggt inn í hvernig kóði er hannaður og afhentur. Sóknarprófun sannreynir afurð þess lífsferils að utan. Hún byggir líka á grunni og menningu kafla 4.1 og forritaöryggisvinnubrögðum kafla 4.2.

Fyrir stór fyrirtæki er sóknarprófun bæði áhættuminnkunartæki og regluverksskylda. Greiðsluvinnsluaðilar, bankar og heilbrigðisveitendur standa frammi fyrir skýrum kröfum um að prófa. Fyrir hið opinbera ná hagsmunirnir til þjóðaröryggis og almenningstrausts: andstæðingar hér eru vel búin þjóðríki og kerfin sem þau miða á reka kosningar, bætur og mikilvæga innviði. Í báðum umhverfum kemur gildið ekki af skýrslunni heldur af því sem þú lagar og hve miklu hraðar þú lærir að greina næsta innbrot.

## Meginreglur

- Láttu verkefnið samsvara spurningunni: skönnun, innbrotspróf og rautt lið svara ólíku.
- Fáðu skriflega heimild og skýrar þátttökureglur áður en nokkur snertir kerfi.
- Niðurstöður eru einskis virði þar til þær eru úrbættar og endurprófaðar. Raktu þær eins og hverja aðra vinnu.
- Rautt lið er til að gera bláa liðið betra, ekki til að vinna.
- Líktu eftir raunverulegum andstæðingum og aðferðum þeirra, ekki almennum gátlistum.
- Mældu greiningu og viðbrögð, ekki bara fjölda veikleika sem finnast.
- Varastu leikhús: verkefni afmarkað til að standast lítur áhrifamikið út og sannar ekkert.

## Ráðleggingar

### Skildu sóknaröryggissviðið

Byrjaðu á að nefna hvað þú ert að kaupa. Veikleikaskönnun er víð, sjálfvirk og ódýr. Keyrðu hana samfellt gegn búi þínu til að grípa þekkt [Common Vulnerabilities and Exposures](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) (CVE) og rangstillingar. Hún framleiðir magn og rangar jákvæðar og getur ekki sagt þér hvort galli er raunverulega nýtanlegur í samhengi. Innbrotspróf setur hæfan prófanda gegn skilgreindu skotmarki í fastan glugga, sem tengir saman veikleika til að sýna raunveruleg áhrif: þessi skannaniðurstaða, ásamt þessari veiku heimild, skilar lénsstjórnanda. Það svarar „má brjóta þennan tiltekna hlut, og hve illa“.

Rautt lið svarar stærri spurningu: „ef ákveðinn andstæðingur beindi sjónum að okkur, myndum við taka eftir og gætum við stöðvað hann“. Það er markmiðsmiðað (sækja þetta gagnasafn, ná þessu kerfi), nær yfir allt árásaryfirborðið þar á meðal fólk og líkamlegan aðgang og er yfirleitt rekið án þess að vara varnarmenn við. [Fjólublátt lið](https://en.wikipedia.org/wiki/Red_team#Purple_team) rífur múrinn: rauða og bláa liðið vinna saman í sama herbergi, árásaraðilinn keyrir aðferð og varnarmaðurinn horfir á hvort verkfæri hans grípi hana og stillir greiningar í rauntíma. Fjólublátt lið skilar oft meiri varnarbótum á hverja krónu en leynilegt rautt lið, því hver aðgerð verður kennslustund.

### Veldu svart-, grátt- eða hvítkassapróf af ásetningi

Hve miklu þú segir prófandanum mótar það sem þú lærir. Svartkassapróf gefur honum ekkert nema skotmark og líkir eftir utanaðkomandi árásaraðila án innanhússþekkingar. Það er raunsætt en hægt, og prófendur kunna að eyða öllu fjárhagsáætluninni í könnun sem raunverulegur andstæðingur myndi taka mánuði í. Hvíttkassapróf réttir frumkóða, arkitektúrteikningar og auðkennisgögn, sem leyfir prófandanum að fara djúpt og dekka meira í tímanum sem er í boði. Grátt er mitt á milli: nokkur þekking, nokkur auðkennisgögn, sem líkir eftir árásaraðila sem hefur gert heimavinnuna eða illgjörnum innanbúðarmanni.

Fyrir flest forritapróf gefur grákassa- eða hvítkassapróf betri ávöxtun, því þú borgar fyrir dýpt greiningar, ekki fyrir að prófandinn enduruppgötvi netskipan þína. Taktu svartkassapróf frá fyrir þegar raunsæi könnunarskeiðsins er sjálft það sem þú vilt prófa, eins og að mæla hve mikið utanaðkomandi getur lært af opinberu fótspori þínu. Vertu skýr um hvað þú pantar, því svartkassaskýrsla sem finnur lítið getur þýtt að þú sért öruggur eða að prófandinn hafi runnið út á tíma við jaðarinn.

### Afmarkaðu vandlega og skrifaðu þátttökureglur

Umfang er þar sem verkefni heppnast eða mistakast. [Þátttökureglna](https://en.wikipedia.org/wiki/Rules_of_engagement) skjal skilgreinir hvað er innan marka og hvað ekki, hvaða aðferðir eru leyfðar, prófunargluggann, kerfin og netin sem eru dekkuð, gagnameðhöndlunarkröfur og neyðartengiliði á báðum hliðum. Það nefnir framleiðslukerfin sem eru bönnuð eða krefjast aðgæslu, setur reglu um að stöðva ef prófandinn finnur eitthvað virkt hættulegt og skilgreinir hvað gerist ef hann rekst á raunverulega árásaraðilavirkni eða raunverulega viðkvæm gögn.

Skrifaðu niður stigmögnunarleiðir og „leyfisbréf“: heimild sem prófandinn getur framvísað ef öryggisstarfsfólk eða lögregla ávarpar hann mitt í verkefni. Samþykktu fyrirfram hvernig niðurstöður eru geymdar og sendar, því innbrotsprófsskýrsla er kort af því hvernig á að brjótast inn hjá þér og verður að vera vernduð í samræmi við það. Þröngt umfang framleiðir djúpar niðurstöður á litlu yfirborði. Vítt umfang framleiðir grunna þekju á stóru. Veldu af ásetningi og láttu umfang aldrei hljóðlega vaxa mitt í verkefni án endurheimildar.

### Líttu á heimild sem línuna milli prófunar og glæps

Einstaka athöfnin sem aðgreinir innbrotsprófanda frá glæpamanni er heimild. Að nálgast kerfi sem þér er ekki heimilt að nálgast er glæpur samkvæmt lögum eins og [Computer Fraud and Abuse Act](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act) í Bandaríkjunum og jafngildum annars staðar, og góður ásetningur er engin vörn. Heimild verður að koma skriflega frá einhverjum með raunverulegt vald til að veita hana, ná nákvæmlega yfir kerfin og aðferðirnar í umfangi og vera undirrituð áður en vinna hefst.

Kerfi þriðju aðila flækja þetta. Skýjaveitan þín, hugbúnaður-sem-þjónusta söluaðilar þínir og hvaða sameiginlegu innviðir sem er kunna að hafa eigin prófunarstefnur, og þú getur ekki heimilað árás á eignir sem þú átt ekki. Athugaðu reglur veitenda, biddu um leyfi þar sem krafist er og haltu prófunum innan eigin leigu. Félagsverkfræði sem beinist að starfsfólki vekur siðferðilegar og lagalegar spurningar um samþykki og sálrænan skaða sem þú verður að hugsa í gegnum fyrirfram. Þegar í vafa skaltu fá lögfræðiráðgjafa að. Kostnaður samtals er léttvægur miðað við kostnað óheimils aðgangsatviks.

### Vegðu innanhússteymi gegn þriðja aðila prófendum

Innanhúss rautt lið þekkir umhverfi þitt, byggir tengsl við varnarmenn og getur prófað samfellt frekar en í árlegum hrinum. Sú þekking er líka takmörkun: þau deila blindum blettum þínum og skipulagsforsendum, og sjálfstæði þeirra má véfengja þegar þau skýra til sömu forystu og kerfin sem þau prófa. Þriðja aðila fyrirtæki koma með fersk augu, sérhæfða færni og sjálfstæðið sem endurskoðendur og eftirlitsaðilar krefjast oft, en þau fara hægt af stað, kosta meira á verkefni og fara þegar skýrslan er afhent.

Flestar þroskaðar áætlanir nota hvort tveggja. Innanhússteymi sjá um samfellda andstæðingslíkingu, greiningarstillingu og djúpu umhverfisþekkinguna sem gerir fjólublátt lið árangursríkt. Utanaðkomandi fyrirtæki veita reglubundna óháða sannprófun, uppfylla sjálfstæðiskröfur staðla eins og PCI DSS og kanna svæðin sem þitt eigið fólk hefur hætt að sjá. Hvort sem þú notar, krefstu þess að prófendur séu hæfir: vottanir eins og OSCP (Offensive Security Certified Professional) og sýnd reynsla skipta meira máli en fægð söluglæra.

### Reku villuverðlaun og samræmda upplýsingagjöf

[Villuverðlauna](https://en.wikipedia.org/wiki/Bug_bounty_program)áætlun býður utanaðkomandi rannsakendum að finna og tilkynna veikleika í skiptum fyrir viðurkenningu og greiðslu. Hún gefur þér samfellda, hópfjármagnaða prófun yfir svið færni sem þú gætir aldrei ráðið alla í einu, og þú borgar aðeins fyrir raunverulegar niðurstöður. Hún kemur ekki í stað skipulegra innbrotsprófa, því rannsakendur elta það sem borgar sig og kunna að hunsa heila flokka, en hún er öflug viðbót sem dregur fram hugvitssamar árásir.

Áður en þú rekur greidd verðlaun þarftu [samræmda veikleikaupplýsinga](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure)stefnu: útgefna, auðfundna leið fyrir hvern sem er til að tilkynna öryggisvandamál örugglega, skuldbindingu um að elta ekki rannsakendur í góðri trú með lögsókn, skilgreinda viðbragðstímalínur og innra ferli til að flokka og laga það sem berst. security.txt skrá og skýrt tilkynningarvistfang eru lágmarkið. Ríkisstofnanir fyrirskipa sífellt oftar veikleikaupplýsingastefnur fyrir opinber kerfi, og að hafa enga rás stöðvar ekki rannsakendur frá því að finna galla. Hún stöðvar þá aðeins frá því að segja þér það örugglega.

### Notaðu gert-ráð-fyrir-broti og andstæðingslíkingu

Jaðarpróf eingöngu gerir ráð fyrir að árásaraðilinn byrji utan, en raunveruleg innbrot byrja oft með vefveiddu auðkennisgagni eða brotinni fartölvu sem er þegar inni. [Gert-ráð-fyrir-broti](https://en.wikipedia.org/wiki/Breach_and_attack_simulation) æfing byrjar prófandann með fótfestu, svo sem aðgang sem venjulegur starfsmaður, og spyr hve langt hann kemst þaðan. Þetta prófar innri skiptingu, greiningu og sprengjusvæðisstýringar beint, frekar en að veðja öllu á jaðar sem verður að lokum farið yfir. Það er yfirleitt betri nýting á tíma rauðs liðs en að horfa á þau mala gegn hertum jaðri.

Festu herferðina í raunverulegri hegðun andstæðinga með [MITRE ATT&CK](https://en.wikipedia.org/wiki/MITRE_ATT%26CK), opinberum þekkingargrunni um aðferðirnar og tæknina sem árásaraðilar nota í raun, skipulögðum frá upphaflegum aðgangi til útflutnings. Andstæðingslíking velur ógnaraðila sem vitað er að miðar á geira þinn, endurskapar skjalfestar aðferðir hans og prófar hvort þú greinir og stöðvar hvert skref. Þetta er langtum gagnlegra en almenn árás, því það varpar vörnum þínum gegn tilteknu andstæðingunum sem þú stendur frammi fyrir og framleiðir niðurstöður sem ógnargreind þín getur forgangsraðað.

### Færðu niðurstöður til bláa liðsins og greiningarverkfræði

Tilgangur sóknar er betri vörn. Sérhver aðgerð rauðs liðs er tækifæri til að spyrja: gáfu verkfæri okkar merki, sá einhver það og brást hann rétt við. Keyrðu verkefni þannig að hver aðferð varpist á greiningu sem þú hefur, þarft að byggja eða þarft að stilla. Þetta er greiningarverkfræði: að breyta hegðun árásaraðila í áreiðanlegar viðvaranir, og þar safnast verðmæti rauðs liðs. Niðurstaða eins og „við vorum ekki greind við hliðarhreyfingu“ ætti að verða ný greiningarregla, prófuð með því að keyra aðferðina aftur.

Borðæfingar framlengja þetta til ákvarðanatöku. Safnaðu fólkinu sem myndi bregðast við raunverulegu atviki og gakktu í gegnum raunhæfa sviðsmynd á pappír: hver lýsir yfir atviki, hver talar við lögfræði, hver ákveður að taka kerfi af netinu. Borðæfingar eru ódýrar, afhjúpa bil í hlutverkum og samskiptum sem tæknipróf missa af og undirbúa mannfólkið sem skiptir mestu þegar atvikastjórnun kafla 9.3 fer í gang. Paraðu tæknilegt rautt lið við reglulegar borðæfingar svo bæði verkfæri þín og fólk séu æfð.

### Raktu úrbætur og endurprófaðu

Veikleikaskýrsla sem enginn bregst við er skuld, því þú rekur nú vitandi galla sem endurskoðandi getur vitnað í. Færðu hverja niðurstöðu inn í venjulegt verkrakningarkerfi þitt með eiganda, alvarleika og skiladegi bundnum áhættu. Mikilvægar niðurstöður fá neyðarmeðferð. Lægri fara í bakskrá með heiðarlegum forgangi. Mælikvarðinn sem skiptir máli er tími til úrbóta, ekki tími til skýrslu.

Endurprófun lokar lykkjunni. Eftir að lagfæring fer út staðfestir prófandinn (eða sjálfvirk athugun) að veikleikinn sé raunverulega horfinn og að lagfæringin hafi ekki opnað nýtt gat. Án endurprófunar er „úrbætt“ von, ekki staðreynd, og margar niðurstöður endurtaka sig því lagfæring var ófullkomin eða afturför kom þeim aftur. Staðlar eins og PCI DSS krefjast þessarar lykkju skýrt. Byggðu endurprófun inn í verkefnasamninginn svo hún sé ekki gleymdur eftirþanki.

## Málamiðlanir: kostir og gallar

| Nálgun | Best fyrir | Kostir | Gallar |
|---|---|---|---|
| Veikleikaskönnun | Samfellda þekju þekktra galla | Ódýr, víð, sjálfvirk, tíð | Hávaðasöm. Getur ekki sannað nýtanleika |
| Innbrotspróf | Að sanna áhrif á skilgreint skotmark | Djúpt mannlegt innsæi. Raunverulegar nýtingarkeðjur | Augnabliksmat. Þröngt afmarkað. Kostnaðarsamt |
| Rautt lið | Að prófa greiningu og viðbrögð | Raunsætt. Æfir fólk og ferla | Dýrt. Hægt. Krefst þroskaðs blás liðs |
| Fjólublátt lið | Að bæta greiningar hratt | Mikill lærdómur á krónu. Samvinnuþýtt | Minna raunsætt. Krefst beggja teyma tiltækra |
| Villuverðlaun | Viðvarandi hópfjármagnaða uppgötvun | Borgað á niðurstöðu. Fjölbreytt færni | Ójöfn þekja. Flokkunarbyrði. Krefst ferlis |

Kjarnaspennan er raunsæi gegn námshraða. Leynilegt rautt lið er raunsæjasta próf sem þú getur keyrt, en lærdómur þess berst hægt og aðeins eftir fulla herferð, og óþroskað blátt lið lærir lítið af að vera hljóðlega sigrað. Fjólublátt lið fórnar undrun til að hámarka hve hratt varnarmenn bæta sig. Önnur spenna er breidd gegn dýpt: skönnun dekkar allt grunnt, á meðan innbrotspróf dekkar sneið djúpt. Þroskaðar áætlanir lagskipta þetta frekar en að velja eitt og keyra samfellda skönnun undir reglubundnu djúpu prófi og stöku fullu rauðliðaherferðum. Röng hreyfing er að kaupa eitt árlegt innbrotspróf, skjalfesta skýrsluna og kalla vandann leystan.

## Spurningar til að ræða með teyminu

1. **Þegar við pöntum sóknarprófun, erum við skýr um hvaða spurningu við erum í raun að spyrja og passar verkefnið við hana?** Margar skipulagsheildir kaupa „innbrotspróf“ og fá veikleikaskönnun með mannskrifuðum samantekt, trúa síðan að þær hafi prófað varnir sínar þegar þær hafa aðeins athugað þekkta galla. Aðrar panta rautt lið þegar greiningargeta þeirra er svo óþroskuð að æfingin sannar aðeins það sem allir vissu. Komdu með síðustu þrjú verkefnaumfang þín og skýrslurnar sem af þeim hlutust og spyrðu hvort hvert svaraði spurningunni sem þú þurftir svar við: þekju þekktra veikleika, nýtanleika tiltekins skotmarks eða getu til að greina og bregðast við innbroti. Svarið ætti að móta yfirvegaða blöndu skönnunar, innbrotsprófa og rauðs eða fjólublás liðs samræmda þroska þínum.

2. **Hvað verður um niðurstöðu eftir að skýrslan lendir og hvernig myndum við sanna að hún var löguð?** Gildi sóknaröryggis liggur alfarið í úrbótum, samt mæla margar áætlanir árangur með stærð skýrslunnar frekar en minnkun áhættunnar. Raktu raunverulega niðurstöðu frá síðasta verkefni þínu: hver átti hana, hvernig var henni forgangsraðað gegn eiginleikavinnu, hvenær var hún lagfærð og staðfesti einhver að lagfæringin virkaði í raun. Ef þú getur ekki framleitt þá slóð býr prófun þín til þekkingu sem þú bregst ekki við, sem er verra en að vita ekki, því nú ertu vitandi útsettur. Afurð þessarar umræðu ætti að vera rakið úrbótavinnuflæði með eigendum, áhættubyggðum frestum og skylduendurprófun innbyggðri í hvern samning.

3. **Er rauða liðið okkar að gera bláa liðið betra, eða bara að halda stigum?** Rautt lið sem fagnar ógreindum sigrum og hamstrar aðferðir sínar er skemmtilegt og gagnslaust. Sambandið ætti að vera samvinnuþýtt undir andstæða yfirborðinu: sérhver aðferð sem fer ógreind ætti að verða ný greiningarregla, sérhver árangursrík leið ætti að upplýsa skiptingu og liðin tvö ættu að ræða saman eftirá. Spyrðu varnarmenn þína hvað þeir lærðu af síðasta rauðliðaverkefni og hvort einhver áþreifanleg greining eða stýring breyttist fyrir vikið. Ef heiðarlega svarið er ekkert ertu að borga fyrir leikhús og ættir að færa þig í átt að fjólubláu liði og andstæðingslíkingu skýrt bundinni greiningarverkfræði.

4. **Fyrir næsta verkefni okkar, höfum við skriflega heimild fyrir hverja eign í umfangi, þar á meðal þær sem við eigum ekki?** Heimild er línan milli innbrotsprófs og tölvuglæpaatviks, og í stórri skipulagsheild sitja kerfin sem prófandi mun snerta sjaldan innan eins eignarhaldsmarka: þau spanna skýjaleigur, hugbúnaður-sem-þjónusta vettvanga, stýrð net og sameiginlega innviði sem samstarfsaðili eða söluaðili stýrir. Þrýstingurinn sem togast á er hraði, því að elta undirritað leyfi og prófunarstefnur veitenda er hægt og freistandi að sleppa þegar frestur vofir. Komdu með drög að þátttökureglum, eignaskrána með eiganda nefndan gegn hverju kerfi, viðeigandi prófunarstefnur skýja- og söluaðila og undirritaða heimildarbréfið sem prófandinn getur framvísað ef ávarpaður mitt í verkefni. Fyrir fyrirtækja- og opinbert starf er útsetningin brýn: óheimil könnun gegn sameiginlegum vettvangi getur brotið samninga, kallað fram regluverksskýrslugjöf eða, fyrir opinbera stofnun, orðið fyrirsögn um ríkið sem ræðst á kerfi sem það hafði ekki rétt á að snerta, svo lögfræðiráðgjafi ætti að samþykkja áður en nokkur byrjar.

5. **Erum við að fjárfesta í innanhúss rauðu liði, utanaðkomandi fyrirtækjum eða báðu og passar sú skipting við það sem við þurfum í raun?** Þetta er smíða-eða-kaupa ákvörðun með raunverulega peninga og margra ára afleiðingar: innanhússteymi kostar laun og verkfæri og skilar samfelldri andstæðingslíkingu og djúpri umhverfisþekkingu, á meðan utanaðkomandi fyrirtæki kosta meira á verkefni en koma með fersk augu, sérhæfða færni og sjálfstæðið sem endurskoðendur og eftirlitsaðilar krefjast. Spennan er að hvort um sig dekkar blindan blett hins, svo að líta á þau sem staðgengla frekar en viðbætur skilur yfirleitt eftir bil. Komdu með núverandi útgjöld þín á hvort, vottanir og sýnda afrekaskrá þeirra sem vinna verkið, takt verkefna og sjálfstæðiskröfurnar sem staðlar þínir leggja á. Í eftirlitsskyldu fyrirtæki geta PCI DSS og sambærileg kerfi knúið utanaðkomandi óháða prófun hversu gott sem innanhússteymi þitt er. Hjá hinu opinbera gera innkaupareglur og þörfin til að sýna armslengdarmat fyrir heimild til að starfa viðurkenndan þriðja aðila oft skyldu, ekki valkost.

6. **Höfum við örugga rás fyrir utanaðkomandi rannsakendur til að tilkynna veikleika og erum við tilbúin að meðhöndla það sem berst?** Stór opinber skipulagsheild er þegar könnuð af rannsakendum hvort sem hún býður þeim eða ekki, og eina spurningin er hvort þeir geta sagt henni það örugglega eða neyðast til að birta eða selja það sem þeir finna. Sjónarmiðið á móti er reiðubúð: að opna samræmda upplýsingagjafarstefnu eða greidd villuverðlaun býr til innkomnar skýrslur og flokkunarbyrði, og áætlun sem borgar fyrir niðurstöður sem hún lagar aldrei er verri en engin. Komdu með núverandi security.txt skrá þína og tilkynningarvistfang ef eitthvert, innleiðingar- og flokkunarferli þitt, viðbragðstímalínurnar sem þú getur heiðarlega skuldbundið þig til og bakskrárgetuna til að úrbæta það sem berst. Fyrir ríkisstofnanir er veikleikaupplýsingastefna á opinberum kerfum sífellt oftar tilskipun frekar en kurteisi, og fyrir fyrirtæki eru vel rekin verðlaun bæði uppspretta hugvitssamra niðurstaðna og sönnun á þroska við áreiðanleikakönnun viðskiptavina, svo ákvörðunin snýst minna um hvort þú hafir rás en hvort þú sért mannaður til að heiðra hana.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Þú hefur ekki efni á innanhúss rauðu liði, svo lagskiptu ódýra þekju í staðinn. Tengdu veikleikaskönnun inn í uppsetningarleiðslu þína til að grípa þekkt ósjálfstæðisgalla á hverri smíði, birtu security.txt skrá og einfalda samræmda upplýsingagjafarstefnu svo rannsakendur nái til þín og pantaðu eitt grákassa innbrotspróf frá virtu fyrirtæki áður en fyrsti fyrirtækjasamningur þinn fer í gegn og raktu hverja niðurstöðu til staðfestrar lagfæringar. Hraði skiptir meira máli en víð áætlun: veldu eitt prófið sem opnar sölu eða lokar stærstu áhættu þinni og slepptu restinni þar til þú vex.

**Lítið fyrirtæki.** Án öryggissérfræðings á launaskrá og með þröngt fjárhagsáætlun skaltu kaupa frekar en smíða. Notaðu stýrða skönnunarþjónustu og ráðu utanaðkomandi innbrotsprófsfyrirtæki á hóflegum takti í stað þess að setja upp nokkra innanhússgetu og tryggðu að samningur þinn feli í sér endurpróf svo „lagað“ sé sannað, ekki gert ráð fyrir. Verðmætasta, ódýrasta hreyfing þín er útgefin leið fyrir hvern sem er til að tilkynna galla ásamt aganum til að plástra hratt, því mest raunverulegt brot á fyrirtæki af þinni stærð kemur gegnum þekkta, óplástraða veikleika.

**Stórfyrirtæki.** Í stærð er áskorunin stjórnarhættir yfir mörg teymi. Reku samfellda skönnun undir reglubundnum óháðum utanaðkomandi innbrotsprófum sem fullnægja stöðlum eins og PCI DSS, haltu innanhúss rauðu liði fyrir samfellda andstæðingslíkingu og fjólublátt lið og stýrðu úrbótum sem rökuðu eignasafni með eigendum, áhættubyggðum frestum og skylduendurprófun. Færðu hverja ógreinda aðferð inn í greiningarverkfræði og framleiddu úttektargögnin, þekju, tímalínur og lokunarhlutföll, sem regluvarsla og stjórn þín búast við.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta alla áætlunina. Haltu veikleikaupplýsingastefnu á opinberum kerfum eins og tilskipanir krefjast í auknum mæli, notaðu viðurkennda óháða matsaðila fyrir innbrotsprófin sem hliða heimild kerfis til að starfa og mótaðu andstæðingslíkingu eftir tilteknu þjóðríkjaaðilunum sem leyniþjónustusamstarfsaðilar þínir merkja. Meðhöndlaðu heimild, umfang og gagnameðhöndlun með aukinni nákvæmni því kerfin reka kosningar, bætur og mikilvæga innviði, og gerðu endurpróf að forsendu þess að halda hvaða kerfi sem er lifandi.

## Dæmi

**Sprotafyrirtæki.** Tuttugu manna fjártæknisprotafyrirtæki hefur ekki efni á innanhúss rauðu liði, svo það lagskiptir því sem það getur. Sjálfvirk veikleikaskönnun keyrir á hverri uppsetningu gegnum leiðsluna og grípur þekkt ósjálfstæðisgalla snemma. Það birtir security.txt skrá og einfalda samræmda upplýsingagjafarstefnu og opnar síðan hófleg villuverðlaun á opinberum vettvangi þegar varan stöðugast og borgar raunverulegum rannsakendum fyrir raunverulega galla. Áður en það skrifar undir fyrsta fyrirtækjaviðskiptavin pantar það grákassa innbrotspróf á forritinu frá virtu fyrirtæki, rekur hverja niðurstöðu til lokunar í venjulegu málakerfi sínu og borgar fyrir endurpróf til að staðfesta lagfæringarnar. Þessi lagskipta nálgun gefur trúverðuga öryggisþekju á kostnaði sem sprotafyrirtækið getur staðið undir, og innbrotsprófsskýrslan verður sönnunargagn sem það getur deilt við áreiðanleikakönnun viðskiptavina.

**Stórfyrirtæki.** Fjölþjóðleg smásala sem vinnur kortagreiðslur verður að uppfylla PCI DSS, sem krefst bæði innri og ytri innbrotsprófa að minnsta kosti árlega og eftir verulegar breytingar, auk skiptingarprófa til að sanna að korthafaumhverfið sé einangrað. Hún rekur samfellda skönnun yfir þúsundir eigna, pantar óháð utanaðkomandi innbrotspróf til að fullnægja staðlinum og heldur innanhúss rauðu liði sem keyrir gert-ráð-fyrir-broti æfingar festar í MITRE ATT&CK gegn ógnaraðilum sem vitað er að miða á smásölu. Rauða liðið vinnur náið með öryggisrekstrarvirkni kafla 4.4: sérhver ógreind aðferð verður að greiningarverkfræðimiða og ársfjórðungslegar fjólublá-liðs lotur stilla viðvaranir. Úrbætur eru raktar með áhættubyggðum frestum og öll áætlunin framleiðir úttektargögnin sem regluvarsla kafla 4.6 krefst.

**Hið opinbera.** Landsbundin stofnun sem rekur borgarabótakerfi stendur frammi fyrir þjóðríkjaandstæðingum og opinberu umboði til að vernda viðkvæm persónugögn. Hún heldur veikleikaupplýsingastefnu á öllum opinberum kerfum, eins og ríkistilskipanir krefjast í auknum mæli, sem gefur rannsakendum örugga rás til að tilkynna galla. Óháðir þriðja aðila matsaðilar framkvæma innbrotspróf sem hluta heimildarferlisins áður en nokkurt kerfi fer lifandi og samfelld vöktun felur í sér viðvarandi skönnun. Stofnunin rekur andstæðingslíkingu mótaða eftir tilteknu ógnarhópunum sem leyniþjónustusamstarfsaðilar hennar merkja og reglulegar borðæfingar æfa atvikaviðbrögðin og lagasamhæfinguna sem raunverulegt innbrot myndi krefjast. Niðurstöður nærir formlega úrbótaáætlun með fyrirskipuðum tímalínum og endurpróf er forsenda þess að halda heimild kerfis til að starfa.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun sóknaröryggis er innbrotið sem þú varðst ekki fyrir. Alvarlegt gagnainnbrot kostar milljónir í beinum viðbrögðum, eftirlitssektum, lagalegri ábyrgð, viðskiptavinabrottfalli og mannorðsskaða, og dýrasti einstaki þátturinn er hve lengi innbrot fer ógreint. Rautt og fjólublátt lið ráðast beint á þá tölu með því að minnka bilið milli brots og greiningar. Innbrotspróf sem finnur nýtanlega leið að viðskiptavinagagnagrunni þínum, lagfærð áður en árásaraðili finnur hana, borgar alla áætlunina margfalt í einu forðuðu atviki.

Harðir hvatar eru líka til. PCI DSS fyrirskipar innbrotspróf fyrir alla sem meðhöndla kortagögn. Rammar og opinber heimildakerfi krefjast óháðs mats fyrir og meðan á rekstri stendur. Fyrirtækjaviðskiptavinir krefjast nýlegra innbrotsprófsskýrslna sem skilyrði samninga. Í þessum tilvikum er prófunin ekki valkvæð og spurningin er aðeins hvort þú dregur raunverulegt öryggisgildi úr peningum sem þú verður að eyða hvort sem er.

Heildareignarkostnaðurinn felur í sér meira en verkefnagjaldið. Fjárhagsáætlaðu verkfæri og starfsfólk innanhússteymis ef þú byggir eitt, flokkunarbyrði villuverðlauna og umfram allt úrbótavinnuna sem niðurstöður framleiða, sem er þar sem raunverulegu útgjöldin lenda. Áætlun sem pantar próf en vanfjármagnar lagfæringar er það versta af báðu: hún borgar fyrir slæmu fréttirnar og borgar svo aftur þegar hunsaða niðurstaðan er nýtt. Til að færa rök við forystu skaltu tengja prófun við mælikvarða sem hún fylgist með: meðaltíma til greiningar, meðaltíma til úrbóta, úttektarniðurstöður lokaðar og áhættuminnkun á mikilvægustu eignum þínum.

## Andmynstur og gildrur

- **Skanna-og-endurnefna:** að selja veikleikaskönnun sem innbrotspróf, afhenda úttak verkfæris án mannlegrar staðfestingar eða nýtingarkeðja.
- **Skýrsla og gleyma:** að líta á afurðina sem markmiðið, skjalfesta niðurstöðurnar og rekja aldrei úrbætur eða endurpróf.
- **Afmarka til að standast:** að þrengja verkefnið svo kerfin sem líklegust eru til að falla séu þægilega utan marka og framleiða hreina skýrslu sem þýðir ekkert.
- **Rautt lið sem stigatafla:** andstæð teymi sem hamstrar aðferðir og fagnar sigrum í stað þess að gera varnarmenn betri.
- **Að prófa óþroskað blátt lið leynilega:** að keyra leynilegt rautt lið áður en þú hefur nokkra greiningargetu, svo æfingin sannar aðeins það sem þú vissir þegar.
- **Engin heimild eða óljóst umfang:** að byrja vinnu án skriflegs leyfis, eða láta umfang læðast inn í kerfi sem þú átt ekki og bjóða lagalegt stórslys heim.
- **Jaðarþráhyggja:** að prófa aðeins ytri jaðarinn og hunsa gert-ráð-fyrir-broti veruleikann að árásaraðilar byrja inni.
- **Að hunsa upplýsingagjafarrásina:** að hafa enga örugga leið fyrir utanaðkomandi rannsakendur til að tilkynna galla, svo þeir birta opinberlega eða selja í staðinn.
- **Leikhúsmælikvarðar:** að telja veikleika fundna frekar en áhættu minnkaða, greiningu bætta og tíma til úrbóta styttan.

## Þroskalíkan

- **Stig 1, Upphaf:** Prófun er stöku og viðbragðsdrifin, oft eitt árlegt innbrotspróf gert til að haka í reit, eða kveikt aðeins eftir atvik. Skýrslur eru skjalfestar með lítilli eftirfylgni, úrbætur eru órakin, engin upplýsingagjafarrás er til og greining raunverulegs innbrots er óprófuð og líklega fjarverandi.
- **Stig 2, Þróun:** Veikleikaskönnun og innbrotspróf eru til en ósamræmd milli teyma, þar sem sumir hópar skanna samfellt og aðrir alls ekki. Niðurstöður eru fangaðar einhvers staðar, þó eigendur og frestir séu blettótt, endurpróf er ad hoc og samræmd upplýsingagjafarrás kann að vera til fyrir sum kerfi en ekki allt búið.
- **Stig 3, Stöðlun:** Sóknarprófun er skjalfest áætlun framfylgd um alla skipulagsheildina, ekki atburður. Skönnun keyrir samfellt undir tímasettum innbrotsprófum pöntuðum á skilgreindum takti og eftir meiriháttar breytingar, þátttökureglur og heimild eru staðlað vinnubrögð, hver niðurstaða er rakin til lokunar með eiganda og áhættubyggðum fresti, endurpróf er skylda og samræmd upplýsingagjafarstefna dekkar öll opinber kerfi.
- **Stig 4, Stjórnun:** Áætlunin er mæld og stýrð gegn grunnlínum. Þú rekur meðaltíma til greiningar og meðaltíma til úrbóta, hlutfall rauðliðaaðferða sem framleiddu merki, greiningarþekju gegn MITRE ATT&CK aðferðunum sem skipta máli fyrir geira þinn, endurtekningarhlutföll niðurstaðna og upplýsingagjafarviðbragðstíma og heldur hverjum mælikvarða gegn markmiði og bregst við þegar hann rekur. Gert-ráð-fyrir-broti æfingar og andstæðingslíking eru rútína, rautt lið starfar samfellt, niðurstöður nærir greiningarverkfræði og fara/ekki-fara ákvarðanir hvíla á sönnunargögnum frekar en skoðun.
- **Stig 5, Samhæfing:** Rautt og fjólublátt lið eru samþætt um skipulagsheildina og aðlögunarhæf. Sérhver aðferð varpast á prófaða greiningu, andstæðingslíking fylgir tilteknu ógnaraðilunum sem miða á geira þinn núna eftir því sem leyniþjónusta breytist og áætlunin fínpússar stöðugt umfang, aðferðir og mælikvarða eftir því sem hún lærir. Sóknarprófun, öryggisrekstur, greiningarverkfræði og atvikaviðbrögð starfa sem ein lykkja sem minnkar mælanlega bilið milli brots og greiningar með tímanum.

## Hugmyndir til umræðu

1. Ef raunverulegur árásaraðili næði fótfestu sem venjulegur starfsmaður í dag, hve langt gæti hann náð áður en nokkur tæki eftir og hvernig veistu það?
2. Hver af síðustu verkefnum þínum voru raunverulega raunsæ og hver voru afmörkuð svo líklegu bilanirnar væru þægilega utan marka?
3. Hve margar niðurstöður úr síðasta prófi þínu eru enn opnar og hvað segir það um hvort prófun eða úrbætur séu raunverulegi flöskuhálsinn?
4. Hafa utanaðkomandi rannsakendur örugga, augljósa leið til að tilkynna þér veikleika og hvað gerist þegar skýrsla berst?
5. Hvenær æfðu atvikasvarar þínir síðast innbrot á pappír og afhjúpaði borðæfingin bil sem tæknipróf þín misstu af?
6. Ertu að mæla veikleika fundna, eða ertu að mæla greiningu bætta og áhættu minnkaða?

## Helstu atriði

- Sóknaröryggi er svið: skönnun finnur þekkta galla, innbrotspróf sannar nýtanleika og rautt lið prófar greiningu og viðbrögð. Láttu verkefnið samsvara spurningunni.
- Skrifleg heimild og skýrar þátttökureglur eru línan milli öryggisprófunar og glæps. Slepptu þeim aldrei, sérstaklega á kerfum sem þú átt ekki að fullu.
- Gildið er í úrbótum og endurprófun, ekki skýrslunni. Raktu hverja niðurstöðu með eiganda, áhættubyggðum fresti og staðfestri lagfæringu.
- Rautt lið er til að gera bláa liðið betra. Færðu niðurstöður inn í greiningarverkfræði, kjóstu fjólublátt lið og gert-ráð-fyrir-broti æfingar og festu herferðir í raunverulegum aðferðum andstæðinga gegnum MITRE ATT&CK.
- Mældu greiningu og viðbrögð, ekki bara veikleikafjölda, og varastu verkefni afmörkuð til að standast, sem framleiða huggun án öryggis.

## Heimildir og frekari lestur

- Georgia Weidman, *Penetration Testing: A Hands-On Introduction to Hacking*
- Peter Kim, *The Hacker Playbook 3: Practical Guide to Penetration Testing*
- Jim O'Gorman, Devon Kearns, and Mati Aharoni, *Metasploit: The Penetration Tester's Guide*
- Joe Vest and James Tubberville, *Red Team Development and Operations: A Practical Guide*
- MITRE, *MITRE ATT&CK* framework and knowledge base
- Payment Card Industry Security Standards Council, *PCI DSS Requirements and Testing Procedures* and *Penetration Testing Guidance*
- National Institute of Standards and Technology, *NIST SP 800-115: Technical Guide to Information Security Testing and Assessment*
- Dafydd Stuttard and Marcus Pinto, *The Web Application Hacker's Handbook*
