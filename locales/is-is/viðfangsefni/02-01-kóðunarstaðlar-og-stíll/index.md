# 2.1 Kóðunarstaðlar og stíll

## Yfirlit og tilgangur

Kóðunarstaðlar eru sameiginlegu venjurnar sem láta marga skrifa kóða eins og einn vandvirkur höfundur hefði skrifað hann. Þeir ná yfir nafngiftir, snið, skráaskipan, málvenjur, villumeðhöndlun og hugmyndafræðin sem teymi kýs. Í litlu teymi getur einstaklingssmekkur ráðið. Í stóru teymi (hundruð eða þúsundir verkfræðinga, margir verktakar, mikil velta) verður ósamræmi skattur sem þú borgar við hvern lestur, hverja rýni og hverja móttöku. Staðlar breyta ótal litlum stíldeilum í einskiptis ákvörðun sem vél framfylgir síðan fyrir þig.

Fyrir stórar skipulagsheildir eru hagsmunirnir áþreifanlegir. Kóði er lesinn miklu oftar en hann er skrifaður. Í fyrirtækja- og opinberu umhverfi getur kóðalína verið lesin af endurskoðendum, öryggisrýnum og umsjónarmönnum árum eftir að höfundur hennar er farinn. Samræmdur stíll lækkar andlegan kostnað þess lesturs, minnkar yfirborð fyrir galla og gerir sjálfvirka greiningu áreiðanlega yfir [lint-tól](https://en.wikipedia.org/wiki/Lint_(software)) (verkfæri sem merkja sjálfvirkt líklega galla og stílbrot), öryggisskanna og [endurbyggingar](https://en.wikipedia.org/wiki/Code_refactoring)verkfæri. Þar sem regluverk á við, eins og í fjármálaþjónustu, heilbrigðisþjónustu, varnarmálum og opinberum kerfum, eru staðlar líka hluti af sönnun þess að kóðagrunnur sé viðhaldanlegur og stýrður.

Nútímaleg nálgun er að líta á stíl sem leyst, sjálfvirkt málefni frekar en viðvarandi mannlegt dómgreindarmál. Sniðmótarar og lint-tól keyra í ritlinum, í pre-commit hooks og í [samfelldri samþættingu](https://en.wikipedia.org/wiki/Continuous_integration) (CI), sjálfvirka smíða- og prófunarferlinu sem keyrir á hverja breytingu. Vélar framfylgja stílnum, svo þú getur eytt rýniathygli þinni í hönnun og réttleika. Markmiðið er ekki einsleitni í sjálfri sér. Það er að fjarlægja núning: þú ættir að geta flutt þig milli þjónusta og teyma án þess að læra grunnatriðin upp á nýtt.

## Meginreglur

- Samræmi slær einstaklingsval. Einn samþykktur stíll, beitt alls staðar, er meira virði en „besti“ stíllinn beitt ójafnt.
- Sjálfvirknivæddu framfylgd. Sniðmótarar og lint-tól eru uppspretta sannleikans, ekki kóðarýniathugasemdir um bil.
- Fínstilltu fyrir lesandann og umsjónarmanninn, ekki upphaflega höfundinn.
- Kjóstu venjur sem víðara tungumálasamfélag notar þegar frekar en sérsniðnar húsreglur.
- Gerðu staðalinn auðveldan í upptöku: veittu sameiginlegar stillingar, sniðmát og verkfæri frekar en PDF sem enginn les.
- Stílreglur ættu að vera fáar, rökstuddar og ótvíræðar. Sérhver regla hefur framfylgdarbúnað eða hún er aðeins ábending.
- Nafngiftir eru áhrifamesta læsileikaákvörðunin og verðskulda skýra leiðsögn.

## Ráðleggingar

### Taktu upp viðurkenndan stílleiðarvísi fyrir hvert tungumál

Fyrir hvert tungumál sem þú notar skaltu taka upp víða viðurkenndan stílleiðarvísi sem grunnlínu (til dæmis samfélags- eða söluaðilaleiðarvísi þess tungumáls) og skjalfesta aðeins frávikin sem skipulagsheildin þín þarf. Finndu ekki upp húsastíl frá grunni. Birtu val þitt á miðlægum, finnanlegum stað og útgáfustýrðu það eins og kóða.

### Gerðu sniðmótara að óumsemjanlegum sjálfgefnum gildum

Notaðu ákveðinn sjálfvirkan sniðmótara fyrir sérhvert tungumál sem hefur einn, með einni sameiginlegri stillingu innritaðri í hugbúnaðarsafnið. Snið ætti aldrei að koma upp í rýni, því það er beitt sjálfvirkt við vistun og staðfest í CI. Þar sem tungumál skortir sterkan sniðmótara skaltu velja eina lint-stillingu og meðhöndla hana á sama hátt.

### Keyrðu lint-tól sem framfylgd hlið, ekki ráð

Stilltu lint-tól með samþykktu regluþetti, láttu smíðina mistakast við brot og haltu regluþettinu í [útgáfustýringu](https://en.wikipedia.org/wiki/Version_control) svo breytingar fari í gegnum rýni. Aðskildu sjálfvirkt lagfæranlegar reglur (beittu þeim sjálfvirkt) frá reglum sem þurfa mannlega dómgreind (merktu og hindraðu). Kynntu nýjar reglur í „viðvörunar“ ham, hreinsaðu uppsafnaða skuld og hækkaðu þær síðan í „villu“.

### Framfylgdu á mörgum lögum

Veittu ritlasamþættingu fyrir tafarlausa endurgjöf, pre-commit hooks fyrir staðbundna framfylgd og CI-athuganir sem lokahliðið. Því fyrr sem þú grípur brot, því ódýrara er það. CI þarf að vera síðasta bakstoðin, því hægt er að sniðganga staðbundna hooks.

### Gefðu nafngiftum skýrar reglur

Staðlaðu hástafa- og lágstafavenjur fyrir hvert tungumál, krefstu merkingarbærra nafna, bannaðu villandi skammstafanir og skilgreindu venjur fyrir bóleanbreytur, safnaðgerðir, einingar og ósamtíma aðgerðir. Skrifaðu lénsorðaforða þinn niður í sameiginlega orðasafnið svo sama hugtak hafi sama nafn alls staðar.

### Stýrðu fjöltyngdu samræmi af ásetningi

Í kóðagrunni sem spannar nokkur tungumál skaltu stefna að samræmdum hugtökum (villumeðhöndlunarmynstur, skráningaruppbygging, verkefnaskipan) jafnvel þar sem setningafræði er ólík. Veittu stillingar fyrir hvert tungumál úr miðlægu hugbúnaðarsafni svo ný þjónusta erfi staðlana sjálfkrafa gegnum sniðmát eða grindarsmíði.

### Skráðu málvenjur og hugmyndafræði

Farðu út fyrir snið. Skrifaðu niður uppáhalds málvenjurnar þínar, svo sem hvernig á að meðhöndla villur, hvernig á að skipuleggja einingar og hvenær á að nota undantekningar á móti niðurstöðugerðum, ásamt hugmyndafræðinni sem teymin þín kjósa. Hér býr raunverulegur læsileiki og viðhaldanleiki.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
|---|---|---|
| Strangur sjálfvirkur sniðmótari, engin stilling | Bindur enda á allar sniðdeilur, tafarlaust samræmi, léttvæg móttaka | Sum illa líkað val eru óumsemjanleg, stór upphafsmunur þegar fyrst er beitt |
| Stillanlegt lint-tól með húsreglum | Sniðið að þörfum skipulagsheildar, getur kóðað raunverulegar gallaforvarnarreglur | Stillingarrek, reglu-bikeshedding, viðhaldsbyrði |
| Samfélagsstaðall tekinn upp í heild | Kunnuglegur nýjum starfsmönnum, sterkt verkfæravistkerfi, lítið viðhald | Passar kannski ekki sértækum skorðum skipulagsheildar, stöku óþægilegar reglur |
| Sérsmíðaður innri staðall | Passar skipulagsheildinni nákvæmlega | Dýrt að skrifa og viðhalda, ókunnugt nýjum starfsmönnum, veik verkfæri |
| Sjálfstæði hvers teymis | Mikill staðbundinn móral, samhengisbundið | Sundrun, sársaukafull hreyfanleiki milli teyma, ósamræmd verkfæri |

Framfylgd sjálfgefin gildi skipta litlu einstaklingssjálfstæði fyrir mikinn sameiginlegan ávinning: minni rýninúning, hraðari móttöku og áreiðanlega sjálfvirkni. Meginhættan er að ofhanna staðalinn í hundruð reglna sem hægja á öllum án þess að koma í veg fyrir raunverulega galla. Haltu regluþettinu litlu og gagnabyggðu og hallaðu þér að því að taka upp núverandi staðal svo viðhald haldist ódýrt.

## Spurningar til að ræða með teyminu

1. **Hvaða lint-reglur ættu að láta smíðina mistakast og hvernig hækkarðu reglu úr viðvörun í villu án þess að stöðva alla?** Þessi kafli heldur því fram að sérhver regla þurfi framfylgdarbúnað og að nýjar reglur ættu að lenda í viðvörunarham, fá uppsafnaða skuld hreinsaða og síðan breytast í villu. Í stóru teymi blokkar það að breyta reglu í villu gegn óhreinum kóðagrunni hundruð ótengdra breytinga á einni nóttu. Komdu með harðar sannanir á fundinn: núverandi brotafjölda fyrir hverja frambjóðandareglu og hvort hún sé sjálfvirkt lagfæranleg eða þurfi mannlega dómgreind. Í fyrirtækja- og opinberu umhverfi nærir standast/falla-línan líka úttektarhlið, svo óljóst regluþett veikir regluvörslusöguna þína. Ákveddu stigskipta útrúllun: lagaðu sjálfvirkt það sem þú getur, fjárhagsáætlaðu hreinsunina og hliðaðu síðan.

2. **Þegar þú beitir sniðmótara fyrst á eldri kóða, hvernig kemurðu í veg fyrir að sú endursníðing eyðileggi git blame og drekki rýnum?** Málamiðlunartaflan varar við stórum upphafsmun og andmynstrakaflinn bendir á að blanda endursniðs-commit við rökfræðibreytingar. Ein yfirgripsmikil endursníðing endurskrifar þúsundir lína og lætur blame benda á endursniðið í stað raunverulegs höfundar, sem skaðar hvern þann sem vinnur við villuleit árum síðar. Gerðu endursníðið sem eitt einangrað, skýrt merkt commit og skráðu það í blame-ignore skrá svo sagan haldist gagnleg. Fyrir endurskoðendur sem rekja hver breytti hverju er sú einangrun munurinn á hreinni sönnun og suði. Komdu þér saman um röðunina áður en þú snertir kóðann, ekki eftir.

3. **Hver á nafngiftaorðasafnið þitt og lénsorðaforðann og hvernig bætist nýtt hugtak við?** Kaflinn kallar nafngiftir áhrifamestu læsileikaákvörðunina og biður þig að skrifa lénsorðaforðann í sameiginlegt orðasafn. Án nefnds eiganda fær sama hugtakið þrjú ólík nöfn yfir teymi og kyrrstæð greining og leitarverkfæri missa áreiðanleika. Komdu með dæmi um hugtök sem hafa þegar misvísandi nöfn í kóðagrunninum þínum sem áþreifanlegt merki. Úthlutaðu einum eiganda og léttri tillöguleið, svo að bæta við eða endurnefna hugtak sé lítil, rýnd breyting frekar en rifrildi í hverri sameiningarbeiðni. Svarið breytir móttökunni: nýr starfsmaður les eitt orðasafn í stað þess að rekja ásetning afturábak úr ósamræmdum kóða.

4. **Tekurðu fyrir hvert tungumál upp viðurkenndan samfélags- eða söluaðilastílleiðarvísi í heild, og hvar eru húsfrávik raunverulega réttlætanleg?** Þessi kafli heldur því fram að þú ættir að taka núverandi staðal sem grunnlínu og skjalfesta aðeins frávikin sem skipulagsheildin þín þarf, því sérsmíðaður staðall er dýr að skrifa og ókunnugur nýjum starfsmönnum. Togið á móti er raunverulegt: innri skorða (öryggisregla, eldri rammi, aðgengiskrafa) stangast stundum raunverulega á við samfélagssjálfgefið, og hvert frávik sem þú heldur er regla sem þú átt nú og viðheldur að eilífu. Komdu með fyrirhugaðan frávikalista á fundinn, hvert með áþreifanlegri skorðu sem rökstyður það, og vertu tilbúinn að skera hvert frávik sem er aðeins smekkur. Í fyrirtækja- og opinberu umhverfi þýðir grunnlína sem passar við víðara tungumálasamfélag einnig að verktakar og nýir söluaðilar koma þegar reiprennandi, sem styttir móttöku og styrkir viðhaldanleikasönnunina sem endurskoðendur leita að.

5. **Í fjöltyngdum kóðagrunni, hvaða venjur eru sannarlega altækar og hverjar haldast tungumálabundnar, og hvernig kemurðu í veg fyrir að stillingar hvers safns reki?** Kaflinn biður um samræmd hugtök (villumeðhöndlun, skráningaruppbyggingu, verkefnaskipan) yfir tungumál jafnvel þar sem setningafræði er ólík, og um stillingar fyrir hvert tungumál þjónaðar úr miðlægu hugbúnaðarsafni svo ný þjónusta erfi staðla sjálfkrafa. Spennan er sú að þvinga málvenjur eins tungumáls upp á annað framleiðir óþægilegan, óidiómatískan kóða, á meðan að leyfa hverju teymi að greina sína eigin stillingu endar með því að „staðallinn“ þýðir ekkert. Komdu með skrá yfir núverandi lint- og sniðmótarastillingar hvers safns og mismun sem sýnir hve langt þær hafa þegar rekið í sundur sem áþreifanlegt merki. Fyrir stóra skipulagsheild sem rekur tugi þjónusta skaltu ákveða dreifingarbúnaðinn (sniðmát, grindarsmíði, sameiginlegan stillingapakka) svo regluviðbót breiðist út einu sinni frekar en að vera handafrituð í hvert hugbúnaðarsafn.

6. **Hvenær er að slökkva á reglu lögmætt, hver rýnir niðurfellinguna og hvernig kemurðu í veg fyrir að altækar slökkvanir holi staðalinn að innan?** Andmynstrakaflinn merkir útbreiddar innlínu-niðurfellingar sem merki um að regla sé röng eða teymi hafi gefist upp, en samt þrýstir stíf engar-undantekningar stefna fólki til að skrifa verri kóða bara til að fullnægja lint-tólinu. Komdu þér saman um létta leið: niðurfelling verður að bera ástæðu, sitja á þrengsta mögulega umfangi og vera sýnileg í rýni en ekki grafin í altæka hunsunarskrá. Komdu með núverandi fjölda niðurfellinga á hverja reglu og hvert safn, því regla sem er felld niður hundruð sinnum er að segja þér eitthvað um regluna, ekki kóðann. Í eftirlitsskyldri og opinberri vinnu veikja óútskýrðar altækar niðurfellingar úttektarsöguna beint, því leiðslan getur ekki lengur sýnt að sameinaður kóði hafi raunverulega staðist samþykkt hlið.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hraði vinnur, svo taktu upp samfélagssniðmótarann og lint-sjálfgefin gildi fyrir eina tungumálið þitt fyrsta daginn og tengdu þau við pre-commit hook og CI áður en annar verkfræðingurinn kemur. Skrifaðu ekki húsastíl sem þú hefur engan tíma til að viðhalda: stillingin sem fylgir í safninu er allur staðallinn. Þegar þú bætir við öðru tungumáli skaltu ná í viðurkenndan leiðarvísi þess tungumáls frekar en að finna upp venjur frá grunni.

**Lítið fyrirtæki.** Án sérstaks verkfærasérfræðings og með þröngt fjárhagsáætlun skaltu hallast alfarið að ókeypis, ákveðna sniðmótaranum sem fylgir eða er við hlið tungumálsins og samþykkja sjálfgefin gildi hans frekar en að fínstilla þau. Þetta er skýrt kaupa-fram-yfir-smíða tilvik: að viðhalda sérsniðnu regluþetti kostar tíma sem þú hefur ekki, á meðan tilbúinn sniðmótari kostar ekkert og bindur enda á stíldeilur strax. Haltu stillingunni í hugbúnaðarsafninu svo eini verktakinn sem þú ræður næsta ár erfi hana án samtals.

**Stórfyrirtæki.** Í stórum stíl er verkefnið stjórnarhættir yfir mörg teymi: miðlægt verkfræðistaðlahugbúnaðarsafn sem heldur sameiginlegu sniðmótara- og lint-stillingunum fyrir hvert tungumál, ný þjónusta mynduð úr sniðmátum sem sækja þær stillingar og CI-hlið sem hindra ósamræmdar sameiningar. Útgáfustýrðu regluþettið eins og kóða og beindu breytingum í gegnum reglubundna rýni svo staðlar þróist af ásetningi frekar en að reka. Ávinningurinn er verkfræðingar sem flytja milli teyma í kunnuglegan kóða og sjálfvirk verkfæri sem framleiða áreiðanlegt merki því hvert safn er samræmt.

**Hið opinbera.** Innkaup og ábyrgð móta valið: skyldaðu tiltekinn stíl og öryggisregluþett sem hluta af authority-to-operate kröfum og láttu leiðsluna gefa út skýrslu sem sýnir að hver sameinuð breyting stóðst samþykkt hlið sem úttektarsönnun. Því sniðmótari er beitt sjálfvirkt lítur kóði frá mörgum söluaðilum og verktökum samræmdur út, sem ver opinbera viðhaldsverkið löngu eftir að samningum lýkur. Kjóstu viðurkenndar samfélagsgrunnlínur fram yfir sérsniðnar reglur svo staðallinn sé gagnsær og hver framtíðarbirgir geti tekið hann upp án séreignarinnilokunar.

## Dæmi

**Sprotafyrirtæki.** Fjögurra manna sprotafyrirtæki tekur upp samfélagssniðmótarann og lint-sjálfgefin gildi fyrir eina tungumálið sitt fyrsta daginn, tengir þau við pre-commit hook og CI svo enginn deili um bil í rýni. Því stillingin fylgir inni í safninu erfa fimmti og sjötti starfsmaðurinn hana sjálfkrafa og sjá aldrei sniðathugasemd. Þegar teymið bætir síðar við öðru tungumáli ná þeir í staðlaðan leiðarvísi þess tungumáls frekar en að finna upp húsastíl sem þeir hafa engan tíma til að viðhalda.

**Stórfyrirtæki.** Stór banki rekur þjónustur í Java, Python og TypeScript yfir tugi teyma. Hann birtir miðlægt „verkfræðistaðla“-hugbúnaðarsafn sem heldur sameiginlegu sniðmótara- og lint-stillingunum fyrir hvert tungumál. Ný þjónusta er mynduð úr sniðmáti sem sækir þær stillingar, svo hvert safn byrjar samræmt. CI hindrar sameiningar við öll brot og ársfjórðungsleg rýni stýrir reglubreytingum. Móttökutími verkfræðinga sem flytja milli teyma styttist merkjanlega, því hvert safn lítur kunnuglega út.

**Hið opinbera.** Opinber stofnun sem nútímavæðir eldra kerfi skyldar aðgengis- og öryggis-lint-regluþett sem hluta af authority-to-operate (ATO) kröfum sínum, formlegu samþykki sem þarf til að reka kerfið í framleiðslu. Stílsamræmi verður hluti af úttektarsönnun: leiðslan framleiðir skýrslu sem sýnir að allur sameinaður kóði stóðst samþykkt [kyrrstæðrar greiningar](https://en.wikipedia.org/wiki/Static_program_analysis)hlið. Því sniðmótari er beitt sjálfvirkt framleiða verktakar frá mörgum söluaðilum sjónrænt samræmdan kóða, sem gerir langtímaviðhaldsverk ríkisins auðveldara eftir að samningum lýkur.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Kostnaður við að taka upp staðla er aðallega einskiptis: að velja leiðarvísa, tengja verkfæri og beita einu stóru upphafsendursniðs-commit. Endurtekni kostnaðurinn er lágur, því framfylgd er sjálfvirk. Kostnaðurinn við að taka *ekki* upp staðla er endurtekinn og safnast upp: hver rýni eyðir mínútum í stíl, hver móttaka er hægari, kyrrstæð greiningarverkfæri framleiða suð og ósamræmdur kóði felur galla. Yfir stóra skipulagsheild leggjast þessar mínútur saman í fullt-starf-jafngildistap.

Ávöxtunin birtist sem minni rýnitöf, færri stílbundnar rýniathugasemdir, hraðari móttaka og hærra merki frá sjálfvirkum verkfærum. Í eftirlitsskyldu umhverfi er frekari ávöxtun í úttektarviðbúnaði: sýnanleg, framfylgd stýring dregur úr fyrirhöfn og áhættu regluvörslurýni. Til að færa rök við forystu skaltu setja staðla fram sem ódýrt, áhrifamikið stýritæki á framleiðni þróunaraðila og úttektarstöðu og setja tölu á núverandi kostnað ósamræmis með greiningu rýniathugasemda og móttökukönnunargögnum.

## Andmynstur og gildrur

- **Stíll rökræddur í kóðarýni:** merki um að framfylgd er ekki sjálfvirk. Færðu regluna í verkfæri.
- **Ólesna staðlaskjalið:** wiki-síða án framfylgdar er skraut. Sérhver regla þarf búnað.
- **Reglusprengja:** hundruð smásmugulegra reglna sem hægja á vinnu án þess að koma í veg fyrir galla.
- **Stillingarrek:** hvert safn greinir sína eigin lint-stillingu þar til „staðallinn“ þýðir ekkert.
- **Að sníða allt safnið í miðri eiginleikavinnu:** að blanda endursniðs-commit við rökfræðibreytingar eyðileggur rýni og blame. Gerðu stórar endursníðingar í einangruðum, skýrt merktum commit.
- **Að hunsa lint-tólið með altækum niðurfellingum:** útbreiddar innlínu-slökkvanir gefa til kynna ranga reglu eða teymi sem hefur gefist upp.
- **Staðlar án eignarhalds:** enginn skýr eigandi þýðir að reglur þróast aldrei og rotna.

## Þroskalíkan

- **Stig 1, Upphaf:** Stíll er á hvern höfund og viðbragðsdrifinn. Engar sameiginlegar stillingar. Snið er rökrætt í rýni og útkljáð af þeim sem lætur sig mestu varða þann daginn.
- **Stig 2, Þróun:** Einstök teymi taka upp sniðmótara og lint-tól, en stillingar og regluþett eru ólík milli teyma og safna, svo samræmi stoppar við mörk hvers teymis.
- **Stig 3, Stöðlun:** Miðlægar sameiginlegar stillingar fyrir hvert tungumál eru skjalfestar og framfylgt um alla skipulagsheildina. CI hindrar ósamræmdar sameiningar. Ný hugbúnaðarsöfn erfa staðlana sjálfkrafa gegnum sniðmát eða grindarsmíði.
- **Stig 4, Stjórnun:** Staðallinn er mældur og stýrður með gögnum: brotahlutföll, niðurfellingatalningar, stílbundnar rýniathugasemdir og móttökutími eru rakin gegn grunnlínum, og reglubreytingar eru hækkaðar eða lagðar niður á þeim gögnum frekar en skoðun.
- **Stig 5, Samhæfing:** Staðlar eru stöðugt bættir og samþættir um skipulagsheildina. Fjöltyngdar málvenjur og lénsorðaforði eru skjalfest og framfylgt, framfylgd er nær núningslaus og regluþettið aðlagast eftir því sem tungumál, verkfæri og þarfir skipulagsheildar breytast.

## Hugmyndir til umræðu

- Hvar er línan milli framfylgdrar reglu og skjalfestrar leiðbeiningar sem treystir dómgreind verkfræðinga?
- Hvernig ætti skipulagsheildin að meðhöndla ástsæla samfélagsreglu sem stangast á við raunverulega innri skorðu?
- Hver á staðlana og hvernig eru reglubreytingar lagðar til, ræddar og útfærðar án truflunar?
- Í fjöltyngdum kóðagrunni, hvaða venjur ættu að vera sannarlega altækar og hverjar ættu að haldast tungumálabundnar?
- Hvernig bætirðu stöðlum við stóran eldri kóðagrunn án truflandi stórhvells-endursniðs?
- Hvaða hlutverk ætti gervigreindaraðstoð að hafa í að leggja til eða framfylgja málvenjum umfram vélrænt snið?

## Helstu atriði

- Líttu á stíl sem sjálfvirkt, leyst vandamál svo menn rýni hönnun og réttleika.
- Taktu upp núverandi samfélagsstaðla og skjalfestu aðeins frávikin.
- Framfylgdu á ritils-, pre-commit- og CI-lögum, með CI sem lokahliðið.
- Haltu regluþettinu litlu, rökstuddu og miðlægt stýrðu.
- Nafngiftir og málvenjur, ekki bil, er þar sem læsileiki vinnst í raun.

## Heimildir og frekari lestur

- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Steve McConnell, *Code Complete*
- Dustin Boswell and Trevor Foucher, *The Art of Readable Code*
- Kevlin Henney (ed.), *97 Things Every Programmer Should Know*
- Google, *Google Engineering Practices* and language style guides (as reference exemplars)
