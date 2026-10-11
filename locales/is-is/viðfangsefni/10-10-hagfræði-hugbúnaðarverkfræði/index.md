# 10.10 Hagfræði hugbúnaðarverkfræði

## Yfirlit og tilgangur

Hagfræði hugbúnaðarverkfræði er sá agi að taka verkfræðiákvarðanir út frá verðmæti og kostnaði, undir óvissu, yfir tíma. Hún er rökhugsunin sem svarar spurningunum sem forystan spyr í raun. Er þetta þess virði að smíða? Hver þessara þriggja kosta gefur bestu ávöxtun? Hvað mun það kosta okkur að eiga þetta kerfi næsta áratug, ekki bara að senda það þennan ársfjórðung? Ættum við að greiða niður þessa [tæknilegu skuld](https://en.wikipedia.org/wiki/Technical_debt) núna, eða fresta henni og greiða vextina? Sérhver vegvísir, innkaup, vettvangsfjárfesting og nútímavæðingaráætlun er, undir niðri, hagfræðileg röksemd. Þessi kafli nefnir agann sem gerir þær röksemdir skýrar, samanburðarhæfar og verjanlegar.

Fyrir eitt teymi getur hagfræðileg rökhugsun verið óformleg, því kostnaður rangs vals er lítill og leiðréttist fljótt. Fyrir fyrirtæki eða opinbera stofnun eru húfin stór, peningarnir annarra og ákvarðanirnar rýndar af fjármálum, úttektaraðilum og almenningi. Áætlunarverkefni sem lítur ódýrt út því einhver taldi aðeins smíðakostnað og hunsaði ár af rekstri, leyfum, stuðningi og endanlegri útskiptingu mun sprengja fjárhagsáætlun sína með ömurlegum áreiðanleika. Tillaga sem lofar ávöxtun en lýsir aldrei forsendum sínum verður ekki véfengd, borin saman eða dregin til ábyrgðar. Hagfræði hugbúnaðarverkfræði gefur þér sameiginlegt, megindlegt tungumál, svo knappt fjármagn flæði til vinnunnar sem skapar mest verðmæti.

Þessi kafli er greiningarhryggjarstykkið í [ávöxtunar fjárfestingar](https://en.wikipedia.org/wiki/Return_on_investment) (ROI) og [heildareignarkostnaðar](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TCO) rökhugsuninni sem notuð er um alla þessa handbók. Eignasafns- og áætlanastjórnun (kafli 10.1) ákveður *hvað* á að fjármagna. Þessi kafli veitir hagfræðilegu aðferðina við *hvernig* á að ákveða. Hann tengist innkaupum (kafli 10.3), þar sem þessir útreikningar réttlæta smíða-eða-kaupa og samningaval, kostnaði, FinOps (fjármálarekstri, það er yfirveguðum stjórnun skýja- og rekstrarútgjalda) og grænum hugbúnaði (kafli 9.4), sem breytir rekstrarkostnaðarhagfræði í rekstrarvenju, uppgötvunarleiðslunni og niðurstöðum (kafli 11.1), þar sem verðmætatilgátur eru mótaðar og prófaðar, tæknilegri skuld í ákvörðunartöku og stjórnarháttum (kafli 1.5) og hugbúnaðarviðhaldi (kafli 3.7), þar sem langi hali eignarkostnaðar lendir í raun.

## Meginreglur

- **Verðmæti og kostnaður eru bæði áætlanir.** Líttu á hverja tölu sem bil með forsendum, ekki staðreynd. Heiðarleg óvissa slær falska nákvæmni.
- **Peningar hafa tímavirði.** Króna í dag er meira virði en króna næsta ár. Núvirtu framtíðarsjóðstreymi áður en þú berð kosti saman.
- **Ákveddu út frá heildareignarkostnaði, ekki kaupverði.** Smíðin er útborgun. Rekstur, stuðningur og viðhald eru húsnæðislánið.
- **Aðeins framtíðarkostnaður og -ávinningur skiptir máli fyrir ákvörðun.** [Sokkinn kostnaður](https://en.wikipedia.org/wiki/Sunk_cost) er farinn. Hunsaðu hann þegar þú velur hvað á að gera næst.
- **Sérhvert val hefur [fórnarkostnað](https://en.wikipedia.org/wiki/Opportunity_cost).** Viðeigandi samanburður er alltaf besta önnur notkun sömu peninga, fólks og tíma.
- **Seinkun hefur verð.** [Kostnaður seinkunar](https://en.wikipedia.org/wiki/Cost_of_delay), verðmætið sem glatast á meðan ákvörðun eða afhending bíður, er oft stærsta og mest hunsaða talan í líkaninu.
- **Gerðu viðskiptarökin hrekjanleg.** Settu forsendurnar svo skýrt fram að veruleikinn geti síðar sannað þær réttar eða rangar.

## Ráðleggingar

### Grundaðu ákvarðanir á undirstöðuatriðum hagfræði

Byggðu sameiginlegan orðaforða áður en þú byggir töflureikna. Aðgreindu *verðmæti* (ávinninginn sem hagsmunaaðili hlýtur) frá *kostnaði* (því sem er neytt til að framleiða hann) og settu hvort tveggja fram sem *sjóðstreymi*, peninga sem hreyfast inn eða út á tilteknum tímum. Því greiðsla næsta árs er minna virði en ein í dag skaltu beita *[tímavirði peninga](https://en.wikipedia.org/wiki/Time_value_of_money)*: núvirtu framtíðarsjóðstreymi með afvöxtunarstuðli sem endurspeglar [fjármagnskostnað](https://en.wikipedia.org/wiki/Cost_of_capital) þinn eða opinberan stuðul. *Tillaga* er þá skipulagður samanburður á sjóðstreymisstraumum keppandi kosta yfir skilgreindan sjóndeildarhring. Krefstu þess að hver mikilvæg tillaga lýsi sjóndeildarhring sínum, afvöxtunarstuðli og forsendum á einni blaðsíðu, svo rýnendur rökræði innihald frekar en að afhjúpa stærðfræðina.

### Ákveddu skýrt undir óvissu og áhættu

Hugbúnaðarákvarðanir eru teknar með ófullkomnum upplýsingum. Að þykjast annað eru mistökin. Líkanaðu óvissu í stað þess að fela hana. Notaðu þriggja punkta áætlanir (bjartsýn, líkleg, svartsýn) í stað stakra talna og reiknaðu *[væntigildi](https://en.wikipedia.org/wiki/Expected_value)* með því að vega niðurstöður eftir líkum þeirra. Fyrir afdrifaríkt val skaltu keyra [næmnigreiningu](https://en.wikipedia.org/wiki/Sensitivity_analysis): breyttu tveimur eða þremur mikilvægustu inntökunum og sjáðu hvort tillagan snýst við. Aðgreindu *áhættu* (megindlegar líkur) frá djúpri *óvissu* (óþekktar líkur) og kjóstu kosti sem varðveita sveigjanleika þegar óvissa er mikil. Áfangaskipt skuldbinding sem leyfir þér að stoppa, snúa við eða tvöfalda eftir nám er oft meira virði en ódýrara allt-eða-ekkert veðmál.

### Láttu ákvörðunaraðferðina passa við rekstrar- og opinbert samhengi

Skipulagsheildir í hagnaðarskyni fínstilla yfirleitt fjárhagslega ávöxtun með [núvirtu hreinu virði](https://en.wikipedia.org/wiki/Net_present_value), ROI og endurgreiðslutíma gegn fjármagnskostnaði. Sjálfseignar- og opinberir aðilar fínstilla verkefnaverðmæti, þjónustuniðurstöður, jafnræði og ráðsmennsku almannafjár og geta ekki dregið hvern ávinning niður í tekjur. Notaðu sama greiningartækjasafnið í báðum aðstæðum, en veldu markfallið heiðarlega. Hjá hinu opinbera eru [kostnaðar- og ábatagreining](https://en.wikipedia.org/wiki/Cost%E2%80%93benefit_analysis) og hagkvæmnigreining, opinberir afvöxtunarstuðlar og heildarlíftímakostnaðarmat oft skylduð. Metdu til fjár það sem má meta til fjár og notaðu fyrir hitt skýr, skjalfest ófjárhagsleg viðmið frekar en að smygla þeim inn sem leiðréttingarstuðlum. Í báðum heimum er agaginn sá sami: gerðu markmiðið og málamiðlanirnar sýnileg.

### Áætlaðu kostnað með fleiri en einni aðferð

Engin ein áætlunaraðferð er áreiðanleg ein, svo krossprófadu. Sameinaðu *samlíkingu* (berðu saman við svipaða fyrri vinnu), *sérfræðimat* (skipulagt inntak frá reyndum verkfræðingum, t.d. wideband Delphi eða planning poker), *sundurliðun* (brjóttu vinnuna niður og rúllaðu áætlunum upp, neðan frá) og *stikalíkön* (formúludrifin, svo sem [COCOMO II](https://en.wikipedia.org/wiki/COCOMO), kvörðuð á gögnin þín). Þar sem þú hefur reynslubundin afköst skaltu kjósa söguleg flæðigögn fram yfir ágiskaða stærðarsetningu. Settu áætlanir alltaf fram sem bil með vissu, endurmetðu þegar þú lærir og aðgreindu áætlun á *fyrirhöfn* frá skuldbindingu um *dagsetningu*. Að rugla þessu tvennu saman er hvernig áætlanir verða að brotnum loforðum.

### Reiknaðu TCO, ROI, NPV og endurgreiðslutíma samræmt

Taktu upp lítið, staðlað verkfærasafn og beittu því jafnt, svo kostir séu samanburðarhæfir yfir eignasafnið. *Heildareignarkostnaður* leggur saman allan kostnað yfir allan líftímann: smíði, útsetningu, leyfi, rekstur, stuðning, öryggi og niðurlagningu. *ROI* setur hreinan ávinning fram sem hlutfall af kostnaði. *Núvirt hreint virði (NPV)* núvirðir hvert framtíðarsjóðstreymi til dagsins í dag og leggur saman. Jákvætt NPV þýðir að kosturinn skapar verðmæti við afvöxtunarstuðul þinn. *[Endurgreiðslutími](https://en.wikipedia.org/wiki/Payback_period)* er tíminn til að endurheimta upphaflega útlagða fjárhæð. Hann er einfaldur og innsæisríkur en blindur á allt eftir jafnvægispunkt og á tímavirði peninga, svo notaðu hann aðeins samhliða NPV. Staðlaðu sjóndeildarhring og afvöxtunarstuðul yfir samanborna kosti, annars er samanburðurinn merkingarlaus.

### Verðleggðu tæknilega skuld og kostnað seinkunar

Gerðu tvo venjulega ósýnilega kostnaðarliði skýra. *Tæknileg skuld* hegðar sér eins og fjárhagsleg skuld: flýtileiðir fá hraða að láni núna og rukka vexti síðar, sem hægari afhendingu, fleiri galla og hærri rekstrarkostnað. Metdu vextina, hve mikið skuldin skattleggur hverja framtíðarútgáfu, svo valið að stofna til hennar eða greiða hana verði hagfræðileg ákvörðun frekar en siðferðileg (sjá kafla 1.5 og 3.7). *Kostnaður seinkunar* er verðmætið sem glatast fyrir hverja tímaeiningu sem verðmætur hlutur er seinn. Að magngreina hann breytir óljósum „við ættum að flýta okkur“ eðlisávísunum í raunverulega forgangsröðun, beinast með Weighted-Shortest-Job-First röðun. Teymi sem verðleggja seinkun hætta að fínstilla fyrir nýtingu og byrja að fínstilla fyrir verðmæti.

### Metdu óáþreifanlegt og byggðu viðskiptarökin

Margir stærstu ávinningar standast ekki hreina dollaratölu: minni áhætta, bætt öryggisstaða, framleiðni forritara, vörumerkjatraust, verkefnaniðurstöður, valkvæðni. Að þykjast þá núll skekkir hverja ákvörðun í átt að hinu áþreifanlega. Metdu þá samt. Metdu til fjár með staðgenglum þar sem trúverðugt er (kostnaður brots sem forðað er, klukkustundir sparaðar sinnum hlaðið taxta). Þar sem þú getur það ekki skaltu gefa þeim skýra einkunn gegn nefndum viðmiðum og bera þá samhliða fjárhagslíkaninu. Settu allt saman í *viðskiptarök*: vandamálið, kosti sem íhugaðir voru (þar á meðal að gera ekkert), kostnað og ávinning yfir sjóndeildarhringinn, helstu forsendur og áhættur, tilmælin og mælikvarðana sem þú munt síðar nota til að dæma hvort það virkaði. Haltu því lifandi og endurskoðaðu það gegn raunútkomu svo skipulagsheildin læri að áætla betur.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
|---|---|---|
| Ítarleg megindleg líkanagerð (NPV, TCO) | Ströng, samanburðarhæf, úttektarhæf. Neyðir forsendur fram í dagsljósið | Tímafrek. Fölsk nákvæmni ef inntök eru veik. Getur útilokað hið ómælda |
| Léttar þumalputtareglur (endurgreiðslutími, kostnaður seinkunar) | Hraðar, innsæisríkar, auðvelt að miðla | Hunsa tímavirði eða langan hala kostnaðar. Hráar fyrir stórar skuldbindingar |
| Stakar tölur sem áætlanir | Einfaldar, afgerandi, auðvelt að skipuleggja kringum | Fela óvissu. Verða falsk loforð. Refsa heiðarleika |
| Bil og væntigildi | Heiðarleg um áhættu. Styðja áfangaskiptar ákvarðanir | Erfiðara að miðla. Getur virst undanskotsfullt fyrir hagsmunaaðila sem vilja eina tölu |
| Að meta óáþreifanlegt til fjár með staðgenglum | Heldur stórum ávinningi í líkaninu. Leyfir málamiðlanir | Staðgenglar eru umdeilanlegir. Hætta á að framleiða þægilegar tölur |
| Full heildarlíftíma-TCO greining | Kemur í veg fyrir smíða-ódýrt-reka-dýrt óvænt | Krefst rekstrarkostnaðargagna sem mörg teymi skortir snemma |

Endurtekna spennan er milli strangleika og hraða. Þung fjárhagsleg líkanagerð bætir stórar, óafturkræfar, dýrar ákvarðanir, en hún er sóun, jafnvel skaðleg, á litlum, afturkræfum, þar sem hún þvær bara fyrirfram ákveðið svar í yfirvaldi töflureiknisins. Þroskaðar skipulagsheildir laga greininguna að húfunum: einnar blaðsíðu röksemd um kostnað seinkunar fyrir hefðbundinn eiginleika, fullt NPV-og-TCO viðskiptamál fyrir fjölára vettvang eða innkaup. Önnur spennan er milli nákvæmni og heiðarleika. Ein örugg tala er auðveldari að bregðast við en oft röng. Bil er sannsögult en erfiðara að skuldbinda sig til. Lausnin er að ákveða með bilum og væntigildi, skuldbinda sig síðan til áfangaskiptra hluta, svo þú haldir möguleikanum á að leiðrétta stefnu þegar sönnunargögn berast.

## Spurningar til að ræða með teyminu

1. **Aðgreinum við fyrirhafnaráætlun frá dagsetningarskuldbindingu og krossprófaum við áætlanir í stað þess að treysta einni tölu?** Ein örugg tala er auðveld að skipuleggja kringum og oft röng og um leið og bilmiðuð fyrirhafnaráætlun harðnar í fasta dagsetningu er heiðarleiki refsað og áætlunin verður brotið loforð. Krossprófadu: sameinaðu samlíkingu, sérfræðimat, sundurliðun og söguleg afköst og kjóstu raunveruleg flæðigögn fram yfir ágiskaða stærðarsetningu. Settu áætlanir fram sem bil með vissu og endurmetðu þegar þú lærir. Fyrir stórt áætlunarverkefni undir fjármála- og úttektareftirliti er þetta munurinn á verjanlegri spá og tölu sem enginn getur véfengt. Komdu með nýlega áætlun sem rann til og spyrðu hvort hún var fyrirhafnaráætlun sem var stýrt að dagatali.

2. **Verðleggjum við kostnað seinkunar og notum hann til að raða vinnu, eða fínstillum við enn fyrir nýtingu?** Kostnaður seinkunar, verðmætið sem glatast fyrir hverja tímaeiningu sem verðmætur hlutur er seinn, er oft stærsta og mest hunsaða talan í líkaninu. Teymi sem verðleggja hann aldrei fínstilla fyrir að halda öllum uppteknum, sem hljóðlega sveltir verðmætustu vinnuna. Magngreindu hann og raðaðu með Weighted-Shortest-Job-First svo vinnan sem tapar mestu verðmæti á að bíða fari fyrst. Þetta endurraðar vegvísum og endurrammar „við ættum að flýta okkur“ sem raunverulega forgangsröðun. Komdu með tvö eða þrjú verkefni í gangi og metdu hvað hvert kostar á viku seinkunar. Ef þú getur það ekki er það bilið til að loka.

3. **Ákveða viðskiptarök okkar út frá heildarlíftíma-TCO gegn grunnlínu um að gera ekkert og er strangleikinn lagaður að húfunum?** Smíði er útborgun. Rekstur, leyfi, stuðningur og endanleg útskipting eru húsnæðislánið og áætlunarverkefni sem telur aðeins smíðakostnað mun sprengja fjárhagsáætlun sína með ömurlegum áreiðanleika. Sérhver alvarleg tillaga ætti að bera saman kosti (þar á meðal að gera ekkert) yfir staðlaðan sjóndeildarhring við sameiginlegan afvöxtunarstuðul og lýsa forsendum sínum á einni blaðsíðu svo rýnendur rökræði innihald frekar en reikning. Lagaðu fyrirhöfnina að: einnar blaðsíðu röksemd um kostnað seinkunar fyrir hefðbundinn eiginleika, fullt NPV-og-TCO mál fyrir fjölára vettvang eða innkaup. Þung líkanagerð á lítilli, afturkræfri ákvörðun þvær bara fyrirfram ákveðið svar í yfirvaldi töflureiknisins. Komdu með nýlega ákvörðun og spyrðu hvort rekstrarkostnaður, ekki verðmiðinn, réði henni.

4. **Hvaða afvöxtunarstuðul notum við til að bera saman kosti yfir tíma og höfum við prófað hvort tillagan lifir af öðrum stuðli?** Tímavirði peninga þýðir að króna á ári fimm er ekki króna í dag, samt sleppa margar tillögur afvöxtun alveg eða grafa stuðul sem enginn samþykkti. Staðlaðu einn stuðul og einn sjóndeildarhring yfir samanborna kosti, annars er samanburðurinn reikningur klæddur sem innsýn. Samkeppnissjónarmiðið er að stuðullinn sjálfur er umdeilanlegur: of lágur og þú gerir hátt undir höfði langtíma megaverkefnum, of hár og þú sveltir fjárfestingar sem borga sig hægt. Komdu með stuðulinn sem þú notaðir, hvaðan hann kom (fjármagnskostnaður þinn eða opinber birtur stuðull) og næmnigreiningu sem sýnir við hvaða stuðul tillagan snýst við. Fyrir fyrirtækjafjármál og sérstaklega hið opinbera er stuðullinn oft skyldaður, til dæmis opinber matsstuðull, og óskjalfestur eða ósamkvæmur stuðull er nákvæmlega það sem úttektaraðili mun véfengja fyrst.

5. **Þegar verkefni stendur sig illa, ákveðum við út frá væntu framtíðarvirði og hunsum það sem við höfum þegar eytt og höfum við byggt fjármögnun þannig að við getum í raun stoppað?** Sokkinn kostnaður er farinn, en hann beitir öflugu togi: teymi verja misheppnað átak með fénu sem þegar var hellt í það frekar en verðmætinu sem er enn framundan. Samkeppnisþrýstingurinn er raunverulegur, því að stoppa lítur út eins og að viðurkenna sóun og ber pólitískan kostnað, svo agann verður að byggja inn í hvernig þú fjármagnar frekar en að skilja eftir því hvernig nokkrum líður í augnablikinu. Kjóstu áfangaskiptar skuldbindingar sem eru sjálfstætt verðmætar og leyfa þér að stoppa, snúa við eða tvöfalda eftir hvern áfanga, í stað einnar óafturkræfrar veðmáls. Komdu með átak í gangi sem er á eftir, eftirstandandi kostnað til að klára borinn saman við vænt eftirstandandi ávinning og punktinn þar sem næsta fjármögnunarhlið fellur. Í fyrirtækja- eða opinberu eignasafni skaltu nefna hver hefur vald til að stöðva áætlun og hvort fjármögnunarbyggingin gefi þeim raunverulegan ákvörðunarpunkt, því skuldbinding án hliðs er skuldbinding sem enginn getur stöðvað.

6. **Erum við heiðarleg um markfall okkar og metum við óáþreifanlegt skýrt frekar en að líta á það sem núll?** Sumir stærstu ávinningarnir, minni áhætta, öryggisstaða, framleiðni forritara, verkefnaniðurstöður og valkvæðni, standast ekki hreina dollaratölu og að þykjast þá núll skekkir hverja ákvörðun í átt að hinu áþreifanlega og skammtíma. Mótáhættan er öfug mistök: að framleiða þægilega tölu og klæða ágiskun í falska nákvæmni. Ákveddu yfirvegað hvaða ávinning þú metur til fjár með trúverðugum staðgenglum (brot sem forðað er, klukkustundir sparaðar sinnum hlaðið taxta) og hvern þú gefur einkunn gegn nefndum ófjárhagslegum viðmiðum borin samhliða líkaninu. Komdu með nýlega ákvörðun þar sem óáþreifanlegt skipti máli og spyrðu hvort það var verðlagt, gefin einkunn eða hljóðlega sleppt. Fyrir opinberan aðila er þetta enn skarpara: verkefnaverðmæti, jafnræði og ráðsmennska almannafjár verða ekki öll dregin niður í tekjur, svo veldu markfallið opinskátt og skjalfestu ófjárhagslegu viðmiðin frekar en að smygla þeim inn sem leiðréttingarstuðlum.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Með fáa mánuði af fjárhagslegri þrautseigju er ríkjandi hagfræðilega talan kostnaður seinkunar: hver vika sem fáir verkfræðingar þínir eyða frá kjarnavörunni eru tekjur og nám frestað. Haltu greiningunni á einni blaðsíðu og kjóstu að kaupa hversdagsgetu frekar en að smíða hana, svo knöpp verkfræðiathygli haldist á aðgreinandanum. Slepptu flóknum NPV-líkönum. Gróf heildarlíftímasamanburður og hörð útgjaldamörk nægja til að grípa smíða-ódýrt-reka-dýrt gildruna áður en hún bítur.

**Lítið fyrirtæki.** Þú hefur engan fjármálagreinanda, svo haltu aðferðinni einfaldri og heiðarlegri: berðu saman fullan kostnað við að eiga hvern kost, áskrift auk vinnustundanna sem hún eyðir, gegn því að gera ekkert. Smíða-á-móti-kaupa kallið hallar nánast alltaf að kaupum, því kerfi sem þú getur ekki viðhaldið verður óáætlaður rekstrarkostnaður sem vex hljóðlega. Dæmdu fjárfestingar á stuttum, innsæisríkum endurgreiðslutíma frekar en afvöxtuðum líkönum og gættu að verðlagningu á notanda sem lítur ódýr út þar til þú skalar.

**Stórfyrirtæki.** Áskorunin er samanburðarhæfni yfir mörg teymi og langt eignasafn: staðlaðu einn afvöxtunarstuðul, einn sjóndeildarhring og eitt verkfærasafn (NPV, TCO, kostnað seinkunar) svo keppandi tillögur megi raða á sama grunni. Verðleggðu vexti tæknilegrar skuldar og kostnað seinkunar skýrt, því í stærð dverga þeir upphaflegan smíðakostnað. Gerðu viðskiptarök að lifandi skjölum endurskoðuðum gegn raunútkomu, svo áætlunarnákvæmni batni og fjármál og úttekt sjái hvers vegna fjármagn flæddi þangað sem það gerði.

**Hið opinbera.** Kostnaðar- og ábatagreining, opinber afvöxtunarstuðull og heildarlíftímakostnaðarmat eru oft skylduð og markmiðið er opinbert verðmæti frekar en tekjur, svo metdu til fjár það sem þú getur trúverðuglega og gefðu hinu einkunn gegn skýrum, birtum viðmiðum. Lýstu hverri forsendu opinskátt gegn grunnlínu um að gera ekkert, því úttektaraðilar og almenningur munu prófa þær. Byggðu fjármögnun í sjálfstætt verðmæta áfanga svo ávinningur hvers áfanga sé nýttur og mældur áður en sá næsti er skuldbundinn og svo hægt sé að stöðva áætlun án þess að stranda sokkið almannafé.

## Dæmi

**Sprotafyrirtæki.** Sex manna sprotafyrirtæki með níu mánaða fjárhagslega þrautseigju ræðir hvort smíða eigi eigið greiðslukerfi eða borga fyrir hýst. Á einni blaðsíðu bera stofnendurnir saman kostina tvo yfir átján mánaða sjóndeildarhring: smíðin lítur ódýrari út á pappír en kostar þrjá verkfræðingamánuði fyrirfram og kostnaður seinkunar (tekjur frestaðar á meðan þessir verkfræðingar senda ekki kjarnavöruna) dvergar áskriftargjaldið. Þeir kaupa hýsta greiðslukerfið, verja knappan verkfræðitíma sinn fyrir aðgreinandann og endurskoða ákvörðunina aðeins ef verðlagning eða umfang breytir reikningnum.

**Stórfyrirtæki.** Smásali vegur að flytja netverslunarstaflann sinn á nýjan vettvang á móti því að halda áfram að plástra þann sem fyrir er. Verkfræði- og fjármálateymið byggir fimm ára líkan við afvöxtunarstuðul fyrirtækisins, ber saman þrjá kosti (gera ekkert, stigvaxandi endurbætur á kóða og fullan nýjan vettvang) á TCO yfir smíði, skýjarekstrarkostnað, leyfi og stuðning. Þeir magngreina vexti tæknilegrar skuldar óbreytts ástands (hækkandi atvikahlutfall og hægari útgáfutakt) og kostnað seinkunar eiginleika sem gamli staflinn getur ekki stutt. Nýi vettvangurinn sýnir hærri upphafskostnað en jákvætt NPV á ári þrjú og lægri rekstrarkostnað eftir það. Næmnigreining staðfestir að tillagan heldur nema skýjaverð hækki mikið. Þeir fjármagna hana í áföngum tengdum áfangamarkmiðum frekar en sem eina óafturkræfa skuldbindingu.

**Hið opinbera.** Stofnun sem nútímavæðir bótakerfi er skylduð til að leggja fram kostnaðar- og ábatagreiningu með opinberum afvöxtunarstuðli og heildarlíftímakostnaðarmati. Því helstu ávinningar eru verkefnaniðurstöður (hraðari, nákvæmari, jafnari þjónusta) metur teymið til fjár það sem það getur trúverðuglega (minna álag á símaver, færri rangar greiðslur, forðuð svik) og gefur hinu einkunn gegn skýrum opinberum verðmætaviðmiðum frekar en að finna upp dollaratölur. Viðskiptarökin kynna grunnlínu um að gera ekkert, lýsa forsendum sínum opinskátt fyrir úttekt og byggja fjármögnun í sjálfstætt verðmæta áfanga, svo ávinningur hvers áfanga sé nýttur og mældur áður en sá næsti er skuldbundinn.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun þess að iðka hagfræði hugbúnaðarverkfræði er betri fjármagnsúthlutun: peningar, fólk og tími flæða til vinnunnar sem skapar mest verðmæti. Verkunarhátturinn er þríþættur. Í fyrsta lagi forðuð sóun: tillögur sem falla á heiðarlegu NPV- eða TCO-prófi eru hafnaðar áður en þær eyða árum af útgjöldum. Í öðru lagi betri röðun: að verðleggja kostnað seinkunar færir verðmætustu vinnuna fram, sem samsetur ávöxtun yfir eignasafnið. Í þriðja lagi færri dýr óvænt atvik: heildarlíftímakostnaðarmat kemur í veg fyrir klassísku bilunina að fjármagna ódýra smíði og verða fyrir fyrirsát af dýrum rekstri.

Kostnaður venjunnar er hóflegur: greinandatími til að byggja líkön, agi til að lýsa forsendum og menningarvinnan við að fá leiðtoga til að ákveða út frá núvirtum, heildarlíftímatölum frekar en yfirskriftarverði. Kostnaðurinn við að iðka hana *ekki* er stærri en dreifður. Þú ofmetur kerfisbundið hið áþreifanlega og skammtíma, vanmetur skuld og seinkun og uppgötvar rekstrarkostnað aðeins eftir að hann er óumflýjanlegur. Rammaðu agann fyrir forystu sem gæðaeftirlitið á hverri annarri fjárfestingarákvörðun. Hann bætir ekki við nýjum útgjaldalið svo mikið sem gerir hvern núverandi útgjaldalið ábyrgan. Ein forðuð lágverðmæta áætlun, eða ein nákvæm TCO-spá sem kemur í veg fyrir rekstrarkostnaðarsprengingu, borgar fyrir alla venjuna margfalt.

## Andmynstur og gildrur

- **Kaupverð sem heildarkostnaður.** Að ákveða út frá smíða- eða leyfisgjaldi á meðan ár af rekstri, stuðningi og endanlegri útskiptingu eru hunsuð.
- **Sokkinn-kostnaðar skuldbinding.** Að halda áfram misheppnuðu átaki vegna fjár sem þegar var eytt frekar en væntra framtíðarvirðis.
- **Nákvæmnisleikhús.** Töflureiknar með tíu aukastöfum byggðir á giskuðum inntökum, sem lána falskt vald fyrirfram ákveðinni niðurstöðu.
- **Að hunsa tímavirði peninga.** Að bera saman skammtíma og fjarlæg sjóðstreymi eins og króna á ári fimm jafngildi krónu í dag.
- **Óáþreifanlegt sem núll.** Að útiloka áhættu, öryggi, framleiðni og verkefnaverðmæti því þau eru erfið að verðleggja, sem skekkir hverja ákvörðun í átt að því mælanlega.
- **Áætlun sem loforð.** Að meðhöndla bilmiðaða fyrirhafnaráætlun sem fasta dagsetningarskuldbindingu og stýra síðan að dagatalinu.
- **Óverðlögð tæknileg skuld.** Að taka flýtileiðir án þess að gera grein fyrir vöxtunum, þar til samsetti skatturinn á afhendingu verður kreppa.
- **Blinda á kostnað seinkunar.** Að fínstilla fyrir nýtingu teymis og einingarkostnað á meðan langtum stærra verðmæti sem tapast vegna seinkunar er hunsað.

## Þroskalíkan

**Stig 1 (Upphaf).** Ákvarðanir eru réttlættar með yfirskriftarverði og magatilfinningu, viðbragðsdrifið og tilvik fyrir tilvik. Engin afvöxtun, ekkert TCO, engar lýstar forsendur. Áætlanir eru stakar tölur meðhöndlaðar sem loforð. Tæknileg skuld og kostnaður seinkunar eru ósýnileg í öllum líkönum.

**Stig 2 (Þróun).** Stærri fjárfestingar bera gróf viðskiptarök með nokkrum kostnaðar- og ávinningsliðum og nokkur rekstrarkostnaður er íhugaður. Einfaldur endurgreiðslutími eða ROI birtist, en tímavirði peninga og heildarlíftímakostnaðarmat er beitt ójafnt og er ólíkt eftir teymum. Áætlanir bera stundum bil, þótt venjan sé ósamræmd.

**Stig 3 (Stöðlun).** Staðlað hagfræðiverkfærasafn (NPV, TCO, ROI, kostnaður seinkunar) með sameiginlegum afvöxtunarstuðli og sjóndeildarhring er skjalfest og beitt samræmt yfir eignasafnið. Óvissa er líkönuð með bilum og væntigildi. Tæknileg skuld er metin og forgangsraðað. Viðskiptarök bera saman grunnlínu um að gera ekkert, lýsa forsendum sínum og eru úttektarhæf.

**Stig 4 (Stjórnun).** Spár eru mældar gegn raunútkomu og stýrðar með gögnum. Áætlunarnákvæmni, raungerð ROI, rekstrarkostnaður á móti spá og niðurstöður kostnaðar seinkunar eru raktar gegn grunnlínum og marktækt frávik ræsir rýni. Viðskiptarök bera skilgreinda árangursmælikvarða og stöðvunarskilyrði framfylgd á sönnunargögnum frekar en tilfinningum og afvöxtunarstuðuls- og næmniforsendur eru staðfestar gegn sögulegum niðurstöðum, svo tölurnar séu stýrðar frekar en aðeins framleiddar.

**Stig 5 (Samhæfing).** Hagfræðileg rökhugsun er samfelld, kvörðuð og samþætt við eignasafns-, innkaupa- og áhættuáætlanagerð. Viðskiptarök eru lifandi skjöl endurskoðuð þegar sönnunargögn berast og áætlunarnákvæmni batnar með tímanum því niðurstöður nærast aftur inn. Kostnaður seinkunar knýr röðun, óáþreifanlegt er metið skýrt og áfangaskipt fjármögnun varðveitir valkvæðni, svo skipulagsheildin endurjafnar fjármagn aðlögunarhæft í átt að vinnunni sem skapar mest verðmæti þegar aðstæður breytast.

## Hugmyndir til umræðu

- Hve mikill fjárhagslegur strangleiki er þess virði að beita á afturkræfa, ódýra ákvörðun áður en greiningin kostar meira en ákvörðunin?
- Hvaða afvöxtunarstuðul ætti skipulagsheild ykkar að nota og hve mikið breytist tillagan þegar þið breytið honum?
- Hvenær er að meta óáþreifanlegt til fjár raunveruleg innsýn og hvenær er það að framleiða þægilega tölu?
- Hvernig verðleggið þið vexti tæknilegrar skuldar nógu sannfærandi til að forystan fjármagni niðurgreiðslu hennar?
- Í opinberu samhengi, hvernig vegið þið jafnræði og verkefnaniðurstöður sem standast ekki peningalegt mat á móti kostum með hreinni fjárhagslegri ávöxtun?
- Ættu viðskiptarök að vera endurskoðuð gegn raunútkomu og hver er ábyrgur þegar raungert verðmæti víkur frá spánni?

## Helstu atriði

- Hagfræði hugbúnaðarverkfræði gerir málamiðlanir verðmætis og kostnaðar skýrar, samanburðarhæfar og verjanlegar: hún er greiningarhryggjarstykkið í ROI- og TCO-rökhugsuninni sem notuð er um alla þessa handbók.
- Ákveddu út frá heildareignarkostnaði yfir allan líftímann, ekki kaupverði, og núvirtu framtíðarsjóðstreymi svo tímavirði peninga sé virt.
- Líttu á áætlanir sem bil undir óvissu, krossprófadu kostnað með mörgum aðferðum og láttu aldrei fyrirhafnaráætlun harðna í fast dagsetningarloforð.
- Verðleggðu venjulega ósýnilegu kostnaðarliðina, tæknilega skuld sem vexti og kostnað seinkunar sem glatað verðmæti, því þeir eru oft stærstu tölurnar í líkaninu.
- Metdu óáþreifanlegt skýrt frekar en að líta á það sem núll og veldu rekstrar- eða opinbert markfall heiðarlega.
- Byggðu lifandi viðskiptarök sem lýsa forsendum og kostum þar á meðal að gera ekkert, lagaðu strangleikann að húfunum og endurskoðaðu spár gegn raunútkomu svo skipulagsheildin læri að áætla betur.

## Heimildir og frekari lestur

- Barry W. Boehm, *Software Engineering Economics*
- Barry W. Boehm et al., *Software Cost Estimation with COCOMO II*
- IEEE Computer Society, *SWEBOK Guide* (Software Engineering Economics knowledge area)
- Donald G. Reinertsen, *The Principles of Product Development Flow* (cost of delay, WSJF)
- Steve McConnell, *Software Estimation: Demystifying the Black Art*
- Douglas W. Hubbard, *How to Measure Anything: Finding the Value of Intangibles in Business*
- Ward Cunningham, "The WyCash Portfolio Management System" (the technical-debt metaphor)
- Philippe Kruchten, Robert Nord, and Ipek Ozkaya, *Managing Technical Debt*
- Mark Schwartz, *The Art of Business Value* and *A Seat at the Table*
- U.S. Office of Management and Budget, Circular A-94 (guidelines and discount rates for benefit-cost analysis)
- HM Treasury, *The Green Book: Central Government Guidance on Appraisal and Evaluation*
