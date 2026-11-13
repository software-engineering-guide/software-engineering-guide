# 6.7 Gervigreindarfulltrúar og sjálfstæð kerfi

## Yfirlit og tilgangur

**Gervigreindarfulltrúi** er [stórt mállíkan](https://en.wikipedia.org/wiki/Large_language_model) (LLM) vafið í lykkju: það fær markmið, getur kallað á verkfæri, heldur einhverju minni um það sem það hefur gert og ákveður sjálft næsta skref þar til markmiðinu er náð eða það gefst upp. Sú lykkja er allur munurinn á fulltrúa og einföldum fyrirmæla-svar köllum úr kafla 6.3. Eitt kall svarar spurningu. Fulltrúi les tölvupóstinn sinn, leitar í gagnagrunni, stofnar miða, athugar niðurstöðuna og reynir aftur. Líkanið er ekki lengur bara að framleiða texta. Það er að velja aðgerðir í kerfum þínum.

Sú breyting breytir verkfræðivandamálinu. Þegar líkan skrifar bara orð er slæmt úttak slæm setning. Þegar líkan stýrir verkfærum getur slæmt úttak sent ranga skilaboð, eytt skrá eða fært fé. [Greindur fulltrúi](https://en.wikipedia.org/wiki/Intelligent_agent) er því best skilinn sem ótraustur skipuleggjandi innan trausts kerfis, og mest af vinnu þinni fer í að afmarka hvað sá skipuleggjandi má gera. Þessi kafli byggir beint á mállíkanagrunni kafla 6.3, trausts- og ábyrgðaráhyggjum kafla 6.5 og vettvangsvinnubrögðum kafla 6.6.

Fyrir stór teymi er það sem er í húfi jafnt skipulagslegt og tæknilegt. Fyrirtæki vilja fulltrúa tengda við raunveruleg innri kerfi (miðakerfi, fjármál, viðskiptavinaskrár), sem þýðir að fulltrúar erfa raunverulegar aðgangsstýringar og raunverulegar breytingastjórnunarskyldur. Hið opinbera bætir við opinberri ábyrgð: sjálfráð aðgerð sem hefur áhrif á borgara verður að vera skýranleg, undir eftirliti og úttektarhæf eftir á. Mynstrið er öflugt. Sett upp án aga er það fljótleg leið til að sjálfvirknivæða mistök.

## Meginreglur

- Fulltrúi er líkan auk lykkju, verkfæra, minnis og markmiðs. Áhættan býr í lykkjunni, ekki prósanum.
- Afmarkaðu sjálfræði við verkið. Gefðu minnsta frelsi sem klárar verkið.
- Kjóstu fast vinnuflæði þegar skrefin eru þekkt. Seilstu í opið sjálfræði aðeins þegar þau eru það ekki.
- Líttu á hvert verkfæri sem árásarflöt og veittu því minnstu réttindi sem það getur unnið með.
- Settu mann í lykkjuna fyrir afleiddar eða óafturkræfar aðgerðir og gerðu afturköllun ódýra.
- Metdu á verkárangri, ekki á því hvernig afritið les.
- Raktu hverja keyrslu. Aðgerð sem þú getur ekki endurbyggt er aðgerð sem þú getur ekki stýrt.
- Einfaldasta hönnun sem virkar er yfirleitt sú rétta. Oft er það alls ekki fulltrúi.

## Ráðleggingar

### Byrjaðu á vinnuflæði, bættu við sjálfræði aðeins þar sem þú verður

Algengustu mistökin eru að seilast í sjálfráðan fulltrúa þegar föst leiðsla myndi duga. Ef þú þekkir skrefin nú þegar (draga út reiti, staðfesta þá, fletta upp skrá, semja svar), skrifaðu það sem samstillt vinnuflæði með líkanið að fylla tiltekin hólf. Sjálfræði vinnur sér sæti þegar leiðin verður í raun ekki ákveðin fyrirfram, til dæmis opin rannsókn eða flokkun yfir mörg möguleg verkfæri. Afmarkaðu sjálfræðið við verkið: settu þak á fjölda skrefa, takmarkaðu verkfærasettið við það sem þetta markmið þarf og settu skýrt stöðvunarskilyrði. Góð regla er að gefa líkaninu nákvæmlega jafn mikið frelsi og vandinn krefst og ekki gráðu meira.

### Gerðu verkfærabeitingu að kjarnagetu og gerðu hana örugga

Verkfærabeiting (einnig kölluð fallkall) er það sem breytir líkani í fulltrúa. Skilgreindu hvert verkfæri með nákvæmu skema, staðfestu hvert viðfang sem líkanið gefur og beittu [lágmarksréttindareglunni](https://en.wikipedia.org/wiki/Principle_of_least_privilege): skýrslufulltrúi sem aðeins les fær lesaðgangsréttindi, aldrei skrifaðgang sem hann gæti misnotað. Keyrðu verkfæri í [sandkassa](https://en.wikipedia.org/wiki/Sandbox_(computer_security)) svo slæmt kall nái ekki út fyrir sprengisvæði sitt. Kjóstu mörg þröng verkfæri með einn tilgang fram yfir fá breið, því þröngt verkfæri er auðveldara að rökræða um, veita heimildir og úttekta. Þetta er sama aðhaldið og kafli 6.3 hvetur til fyrir verkfærabeitingu mállíkana, gert að miðju.

### Notaðu skýr rökhugsunar- og skipulagsmynstur

Fulltrúar vinna betur þegar hugsun þeirra er uppbyggð. Í rökhugsa-og-framkvæma mynstri (gert vinsælt af ReAct-rannsókninni) skiptir líkanið á milli þess að rökhugsa um aðstæður og grípa til aðgerðar, og athugar síðan niðurstöðuna áður en það rökhugsar aftur. Fyrir erfiðari markmið skaltu láta líkanið skipuleggja fyrst (brjóta niður í undirverk) og framkvæma síðan, svo þú getir skoðað og jafnvel samþykkt áætlunina áður en nokkurt verkfæri keyrir. Haltu þessum lykkjum vaktanlegum og stöðvanlegum. Áætlun sem þú getur lesið er áætlun sem þú getur stöðvað.

### Hafðu menn í lykkjunni fyrir afleiddar aðgerðir

Ákveddu, fyrir hvert verkfæri og hverja aðgerð, hvort líkanið megi starfa eitt eða verði að spyrja fyrst. Afturkræfar aðgerðir með lítið í húfi (leit, uppköst) mega keyra án eftirlits. Afleiddar eða óafturkræfar (að senda ytri samskipti, færa fé, breyta framleiðslugögnum, ákveða mál borgara) þurfa [mann-í-lykkjunni](https://en.wikipedia.org/wiki/Human-in-the-loop) hlið með raunverulegu valdi til að segja nei. Hannaðu fyrir afturkræfni hvar sem þú getur: kjóstu að sviðsetja breytingu frekar en að festa hana og gerðu afturköllun að fyrsta flokks eiginleika svo röng aðgerð kosti mínútur, ekki atvik.

### Líttu á öryggislíkanið sem fjandsamlegt

Fulltrúar víkka árásarflötinn sem lýst er í kafla 4.2. Aðalógnin er [fyrirmælainnspýting](https://en.wikipedia.org/wiki/Prompt_injection): illkvittin fyrirmæli falin í vefsíðu, skjali eða tölvupósti sem fulltrúinn les og hlýðir. Náskyld er [blekkta umboðsmannsvandamálið](https://en.wikipedia.org/wiki/Confused_deputy_problem), þar sem árásaraðili platar réttindamikinn fulltrúa til að misnota eigin lögmætan aðgang, til dæmis með því að leka gögnum gegnum verkfæri sem fulltrúanum er leyft að kalla á. Gerðu ráð fyrir að allt efni sem fulltrúinn tekur inn kunni að vera fjandsamlegt. Aðgreindu traust fyrirmæli frá ótraustum gögnum, takmarkaðu verkfæri svo rænd fulltrúa nái ekki til viðkvæmra kerfa og láttu aldrei hrátt líkanaúttak ræsa óafturkræfa aðgerð án staðfestingar.

### Metdu á verkárangri og afturfaraprófaðu óákvörðunarbundna hegðun

Dæmdu fulltrúa eftir því hvort þeir klára verkið, ekki eftir því hvort afritið hljómar gáfulega. Smíðaðu matssafn dæmigerðra markmiða með athugunarhæfum árangursviðmiðum (fékk miðinn rétta forgangsröð, passaði endurgreiðslan við stefnu) og keyrðu það á hverja breytingu á fyrirmælum, líkani eða verkfærum. Því fulltrúar eru óákvörðunarbundnir sannar ein keyrsla lítið: keyrðu hvert tilvik oft og raktu árangurshlutfall, ekki staðið eða fallið. Þetta framlengir óbeintengda og beintengda matsagann úr köflum 6.3 og 6.2 (vélnámsverkfræði og MLOps) til kerfa þar sem úttakið er runa aðgerða.

### Mældu keyrslur fyrir vöktun, kostnað og bilanameðhöndlun

Þú getur ekki stýrt því sem þú sérð ekki. Raktu hverja fulltrúakeyrslu frá enda til enda (kafli 6.6): markmiðið, hvert rökhugsunarskref, hvert verkfærakall með viðföngum og niðurstöðu, tókenin sem fóru og lokaniðurstöðuna. Þessi rakning er í senn aflúsari þinn, úttektarslóð og kostnaðarmælir. Settu hörð fjárhagsáætlunarmörk á skref, tíma og útgjöld, því fulltrúi sem lykkjast getur brennt töf og peningum hratt. Meðhöndlaðu bilun skýrt: endurreyndu tímabundnar verkfæraskekkjur með veldisundanhaldi, en greindu lykkjur þar sem líkanið endurtekur bilandi aðgerð og bilaðu öruggt frekar en að streða.

## Málamiðlanir: kostir og gallar

| Val | Kostir | Gallar | Best þegar |
|---|---|---|---|
| Fast vinnuflæði (líkanið fyllir hólf) | Fyrirsjáanlegt, ódýrt, auðvelt að prófa og úttekta | Stíft. Brotnar á ófyrirséðum leiðum | Skrefin eru þekkt fyrirfram |
| Sjálfráður einn fulltrúi | Sveigjanlegur. Ræður við opin markmið | Erfiðari í stjórn, mati og afmörkun | Leiðin verður ekki ákveðin fyrirfram |
| Fjölfulltrúasamstilling | Samhliða vinnsla. Sérhæfð hlutverk | Samræmingarkostnaður, magnandi villur, hærri útgjöld | Verk brotnar í raun niður í óháða hluta |
| Aðgerð án eftirlits | Hröð, lítill núningur | Mistök keyra án athugunar | Aðgerðir eru afturkræfar og lítið í húfi |
| Mann-í-lykkjunni hlið | Öryggi, ábyrgð, afturkræfni | Hægara. Krefst rýnigetu | Aðgerðir eru afleiddar eða óafturkræfar |

Kjarnaspennan er sjálfræði gegn stjórn. Meira sjálfræði ræður við fleiri aðstæður en krefst fleiri varnarrimla, meira mats og meiri peninga, og það bilar á vegu sem erfiðara er að sjá fyrir. Fjölfulltrúahönnun freistar teyma með glæsileika, samt bætir hver aukafulltrúi við samræmingarkostnaði og enn einum stað þar sem lítil villa getur magnast í ranga niðurstöðu. Leystu spennuna með því að byrja á minnsta sjálfræði sem leysir vandann og bæta við frelsi aðeins þegar áþreifanlegt verk neyðir þig til þess, alltaf parað við samsvarandi varnarrim.

## Spurningar til að ræða með teyminu

1. **Þarf þessi eiginleiki í raun fulltrúa, eða væri fast vinnuflæði öruggara og ódýrara?** Sjálfræði er tælandi, en flest verk hafa þekkjanleg skref sem samstillt leiðsla meðhöndlar með langtum minni áhættu. Fyrir stórt teymi þýðir sjálfgefið val á fulltrúum að hver hópur tekur á sig mats-, rakningar- og öryggisbyrðar sem einfaldari hönnun myndi forðast. Komdu með tiltekið verk og spyrðu hvort skref þess verði ákveðin fyrirfram. Ef svo er, er fulltrúi líklega ofhönnun. Taktu frá opið sjálfræði fyrir markmið þar sem leiðin er í raun ólík eftir tilviki. Svarið ætti að ýta flestum eiginleikum í átt að vinnuflæði og skilja eftir lítið, yfirvegað mengi sem sannir fulltrúar.

2. **Fyrir hvert verkfæri sem fulltrúi okkar getur kallað á, hvað er það versta sem rændur fulltrúi gæti gert með því og hvað stöðvar það?** Fyrirmælainnspýting og blekkta umboðsmannsárásir snúa eigin lögmætum aðgangi fulltrúans gegn þér, svo rétta linsan er fjandsamleg (kafli 4.2). Skráðu hvert verkfæri, réttindaumfang þess og hvort illkvittin fyrirmæli smyglað gegnum innlesið efni gætu náð til þess. Fyrir fyrirtæki sem tengja fulltrúa við innri kerfi er þetta þar sem lágmarksréttindi, sandkassar og mannleg hlið á óafturkræfum aðgerðum verða raunveruleg. Komdu með lista verkfæra og auðkennisgögnin sem hvert heldur á. Ef einhver afleidd aðgerð er aðgengileg án staðfestingar eða mannlegrar athugunar er það fyrsta sem á að laga.

3. **Hvernig myndum við vita að árangurshlutfall fulltrúa féll, þar sem hver keyrsla lítur trúverðug út?** Fulltrúar eru óákvörðunarbundnir, svo afrit sem les vel getur samt hafa tekið ranga aðgerð og ein græn keyrsla sannar ekkert. Spyrðu hvort þú eigir matssafn markmiða með athugunarhæfum niðurstöðum, keyrt oft á hvert tilvik til að framleiða árangurshlutfall frekar en eitt staðið. Fyrir útsetningar með miklu í húfi eða opinberar skaltu ræða hvernig keyrslurakningar leyfa þér að endurbyggja nákvæmlega hvað gerðist þegar eitthvað fer úrskeiðis (kaflar 6.5 og 6.6). Ef eina merkið þitt eru notendakvartanir ertu þegar of seinn. Svarið ætti að fjármagna matsramma fyrir stærð, ekki eftir atvik.

4. **Hverjar af aðgerðum þessa fulltrúa eru í raun óafturkræfar, hver hefur vald til að samþykkja þær og höfum við rýnigetuna til að manna það hlið?** Freistingin er að láta líkanið starfa án eftirlits alls staðar, en mannlegt hlið er aðeins raunverulegt ef nefndur maður með vald til að segja nei er til taks þegar fulltrúinn spyr. Fyrir stórt teymi verður samþykktarröð sem enginn á hljóðlega að stimpli og öryggið sem þú hannaðir gufar upp undir magni. Komdu með fullan lista aðgerða sem fulltrúinn getur tekið, merktu hverja afturkræfa eða óafturkræfa og metdu daglegt magn lágtraustsmála sem lenda á rýni. Vegðu núning og mönnunarkostnað hliðs gegn sprengisvæði ósýnilegra mistaka og kjóstu að endurhanna óafturkræfa aðgerð í sviðsetta, afturkræfa fram yfir að bæta við öðrum rýni. Í fyrirtækja- og opinberu umhverfi skaltu tengja hverja afleidda aðgerð við ábyrgan embættismann og breytingastjórnunarskrá, því sjálfráð aðgerð sem hefur áhrif á borgara eða viðskiptavin og enginn maður samþykkti er nákvæmlega bilunin sem úttekt finnur.

5. **Seilumst við í fjölfulltrúahönnun því verkið brotnar í raun niður, eða því hún lítur glæsilega út?** Að skipta vinnu milli sérhæfðra fulltrúa er tælandi, samt bætir hver aukafulltrúi við samræmingarkostnaði og enn einum stað þar sem lítil villa magnast í ranga niðurstöðu. Fyrir stóra skipulagsheild er kostnaðurinn ekki bara útgjöld og töf: fjölfulltrúakerfi er langtum erfiðara að rekja, meta og rökræða um þegar það bilar, svo stjórnarhættabyrðin margfaldast með hverju hlutverki sem þú bætir við. Komdu með verkið og sýndu áþreifanlega hvaða hlutar keyra óháð og samhliða, berðu síðan saman mælt árangurshlutfall og kostnað fjölfulltrúaútgáfu við einn fulltrúa á sama matssafni. Ef einn fulltrúi vinnur eða jafnast er glæsilega hönnunin ofhönnun. Fyrir regluverkaðar eða opinberar útsetningar skaltu muna að hver fulltrúi í keðjunni er enn einn íhlutur sem eftirlitsaðili verður að geta skoðað, svo bætt uppbygging sem þú getur ekki rökstutt er bætt skuld.

6. **Hver eru hörðu fjárhagsáætlunarmörkin á skref, tíma og útgjöld fulltrúa og hvernig yrði lykkjandi fulltrúi gripinn áður en hann eykur kostnað eða töf?** Fulltrúi sem endurtekur bilandi aðgerð getur brennt peningum og tíma án viðvörunar, svo ótakmarkað sjálfræði er fjárhagsleg áhætta jafnt og öryggisleg. Fyrir stórt teymi sem rekur marga fulltrúa getur ein illa hagandi lykkja hækkað skýjareikning eða klárað hraðatakmörk sem sveltir hvert annað vinnuálag, sem gerir mörk á keyrslu að sameiginlegu rekstraráhyggjuefni en ekki vandamáli eins teymis. Komdu með núverandi skrefa-, tíma- og tókenafjárhagsáætlanir fyrir hvern fulltrúa, viðvörunina sem kviknar þegar keyrsla fer yfir þær og lykkjugreininguna sem bilar öruggt frekar en að streða. Vegðu þröng mörk, sem kunna að skera af lögmætt erfitt verk, gegn rúmum sem láta kostnað hlaupa burt. Í fyrirtækja- og opinberu umhverfi þar sem útgjöld verða að vera spáð og rökstudd er fulltrúi með ótakmarkaðan kostnað línuliður sem þú getur ekki varið í fjárhagsrýni eða úttekt.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Afhentu einn þröngan fulltrúa sem snertir kjarnagildi þitt, á hýstu líkani, með minnsta verkfærasettið sem klárar verkið og hart þak á skref og útgjöld. Stattu gegn fjölfulltrúasýnikennslunni: knöppu verkfræðiathygli þinni er betur varið í að afmarka sjálfræði eins fulltrúa og rekja keyrslur hans en að samræma hlutverk sem þú getur ekki viðhaldið. Hafðu hverja afleidda aðgerð á bak við eitt „semja, aldrei senda“ hlið svo mistök kosti einn smell að afturkalla, ekki atvik.

**Lítið fyrirtæki.** Þú hefur engan til að reka matsramma eða sandkassa, svo kjóstu fulltrúa innbyggða í verkfæri sem þú treystir og kveiktu aðeins á sjálfræðinu sem þú getur haft eftirlit með með augunum. Líttu á hvern fulltrúa sem getur sent, greitt eða eytt fyrir þína hönd sem eitthvað til að halda frá þar til maður staðfestir hverja aðgerð, því röng sjálfvirk skilaboð til viðskiptavinar kosta þig sambandið. Kjóstu seljendur sem sýna þér hvað fulltrúinn gerði og leyfa þér að slökkva á sjálfvirkninni.

**Stórfyrirtæki.** Vandinn er að stýra fulltrúum yfir mörg teymi: sameiginleg mynstur til að afmarka sjálfræði, verkfæraauðkenni með lágmarksréttindum, sandkassa, mann-í-lykkjunni hlið og rakningu frá enda til enda svo enginn hópur finni upp varnarrimlana aftur. Tengdu fulltrúa við innri kerfi undir sömu aðgangsstýringum og maður hefði, hliðaðu óafturkræfar aðgerðir á bak við nefnda samþykkjendur og breytingastjórnun og stýrðu eignasafninu með árangurshlutfallsmælikvörðum, fjárhagsáætlunum á keyrslu og andstæðingaprófunum á innspýtingu. Staðlaðu rakningar- og matslagið svo hegðun hvers fulltrúa megi endurbyggja og úttekta.

**Hið opinbera.** Innkaup, gagnsæi og opinber ábyrgð afmarka hvert val. Haltu fulltrúum við að afla staðreynda og semja uppkast og taktu frá hverja ákvörðun sem hefur áhrif á borgara fyrir ábyrgan mann, því ábyrgð á opinberri ákvörðun verður ekki framseld til líkans. Skráðu hverja keyrslu svo eftirlitsaðili sjái hvaða heimildir voru hafðar til hliðsjónar og hvað var gert, krefstu þess að seljendur upplýsi um verkfæri og takmarkanir fulltrúans og sannaðu með andstæðingamatssafni að fulltrúinn neiti að aðhafast umfram afmarkað umboð sitt.

## Dæmi

**Sprotafyrirtæki.** Fimm manna greiningarsprotafyrirtæki smíðar stuðningsflokkunarfulltrúa. Hann les innkomandi miða, leitar í skjölunum og annaðhvort semur svar eða beinir miðanum til manns, og það er allt verkfærasettið. Auðkennisgögnin eru lesaðgangur auk einnar „stofna uppkast“ aðgerðar sem sendir aldrei án þess að maður smelli á senda. Hver keyrsla er rakin svo stofnendurnir sjái hvers vegna miða var beint þangað sem hann fór og næturmatssafn fimmtíu raunverulegra miða keyrir fulltrúann fimm sinnum á hvern til að rekja leiðarnákvæmnihlutfall. Þegar snjöll fjölfulltrúasýnikennsla keppinautar freistar þeirra halda þeir sig við einn fulltrúa því verk þeirra brotnar ekki niður.

**Stórfyrirtæki.** Banki smíðar fulltrúa til að hjálpa starfsfólki rekstrar að jafna misheppnaðar greiðslur. Hann tengist innri kerfum undir sömu aðgangsstýringum og mannlegur afgreiðslumaður hefur, veittum gegnum þjónustuauðkenni með lágmarksréttindum afmörkuð við jöfnun eingöngu. Fulltrúinn má rannsaka frjálst (lesa höfuðbækur, leita í færslusögu) en sérhver aðgerð sem færir fé eða breytir skrá er sviðsett og krefst nefnds mannlegs samþykkjanda, sem uppfyllir breytingastjórnun. Innlesin skjöl eru meðhöndluð sem ótraustum til að sljóvga fyrirmælainnspýtingu, verkfæri keyra í sandkassa og hver keyrsla er rakin frá enda til enda fyrir úttekt. Óbeintengt matssafn hliðar hverja líkana- eða fyrirmælabreytingu og fjárhagsáætlanir á keyrslu setja þak á skref og útgjöld svo lykkjandi fulltrúi geti ekki aukið kostnað eða töf.

**Hið opinbera.** Bótastofnun prófar fulltrúa til að hjálpa málafulltrúum að safna staðreyndum fyrir kröfu: að sækja skrár, athuga hæfisreglur og semja samantekt. Stofnunin dregur harða línu: fulltrúinn safnar og semur uppköst, en mannlegur málafulltrúi tekur og á hverja ákvörðun sem hefur áhrif á borgara, því ábyrgð á opinberum ákvörðunum verður ekki framseld til líkans (kafli 6.5). Hver keyrsla er fullskráð og sýnir hvaða heimildir voru hafðar til hliðsjónar og hvað var samið, svo eftirlitsaðili geti úttektað hvert mál. Sjálfræði er viljandi afmarkað við lesa-og-semja, verkfæri hafa lágmarksréttindi og keyra í sandkassa og andstæðingamatssafn staðfestir að fulltrúinn neiti að aðhafast umfram að safna staðreyndum.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Fulltrúar skila ávöxtun með því að sjálfvirknivæða fjölþrepavinnu sem áður þurfti mann til að smella milli kerfa: flokkun, jöfnun, rannsóknir og hversdagsrekstur. Gildið birtist sem vinna kláruð án manns í hverju skrefi, hraðari hringrásartími og starfsfólk leyst undan til verka sem krefjast dómgreindar. Því fulltrúar byggja á núverandi mállíkönum og verkfærum er tími til vinnandi frumgerðar stuttur, sem er nákvæmlega ástæða þess að teymi ofsmíða.

Heildareignarkostnaður er þar sem fulltrúar eru ólíkir einföldum mállíkanseiginleikum. Ofan á ályktunarkostnað borgarðu fyrir verkfærasamþættingar, sandkassa- og heimildalagnir, matsrammann, rakningar- og vöktunarstaflann (kafli 6.6) og mannlegu rýnana sem manna samþykktarhliðin. Lykkjandi eða illa afmarkaður fulltrúi bætir við breytilegum kostnaði sem getur rokið upp án viðvörunar, svo fjárhagsáætlunarmörk á skref og útgjöld eru hluti hönnunarinnar, ekki eftirþanki. Kostnaður þess að taka ekki upp er hægari rekstur og handvirk leiðindavinna sem keppinautar þínir sjálfvirknivæða. Kostnaður þess að taka upp af kæruleysi er sjálfráð aðgerð sem sendir röng skilaboð, lekur gögnum eða tekur ábyrgðarlausa ákvörðun. Færðu rök við forystu með því að para eitt áþreifanlegt sjálfvirknimarkmið við áþreifanlega áætlun um varnarrimla, mat og mannlegt eftirlit og með því að vera heiðarlegur um að varnarrimlarnir eru megnið af kostnaðinum.

## Andmynstur og gildrur

- **Fulltrúi þegar vinnuflæði myndi duga.** Að taka á sig alla áhættu sjálfræðis fyrir verk þar sem skrefin voru þekkjanleg.
- **Of breið verkfæri og auðkennisgögn.** Eitt „gerðu hvað sem er“ verkfæri í stað þröngra verkfæra með lágmarksréttindi.
- **Blinda á fyrirmælainnspýtingu.** Að mata fulltrúa á ótraustu efni sem hefur raunveruleg réttindi.
- **Ekkert mannlegt hlið á óafturkræfum aðgerðum.** Að láta líkanið senda, greiða eða eyða án athugunar.
- **Fjölfulltrúaleikhús.** Að skipta einföldu verki milli fulltrúa og borga samræmingarkostnað fyrir engan ávinning.
- **Tilfinningabyggt mat.** Að dæma eftir því hvernig afritið les í stað verkárangurshlutfalls.
- **Ótakmarkaðar lykkjur.** Ekkert þak á skref, tíma eða útgjöld, svo fastur fulltrúi brennir peningum og töf.
- **Órakin keyrsla.** Engin skrá yfir hvað fulltrúinn gerði, sem skilur þig eftir án getu til að aflúsa, úttekta eða gera grein fyrir.

## Þroskalíkan

- **Stig 1, Upphaf:** Fulltrúar eru frumgerðir ad hoc með breiðan verkfæraaðgang og engin mörk. Árangur er dæmdur eftir sýnikennslu, viðbragðsdrifið, eftir að eitthvað brotnar. Ekkert matssafn, engin rakning og ekkert mannlegt hlið á afleiddum aðgerðum.
- **Stig 2, Þróun:** Sumir fulltrúar hafa afmarkaðar lykkjur og verkfæri með lágmarksréttindi og grunnrakning er til, en vinnubrögð eru ólík eftir teymum. Handvirkt matssafn grípur gróf afturför í fáum verkefnum á meðan önnur hafa ekkert. Mannlegt samþykki ver augljósustu óafturkræfu aðgerðirnar, en þekja er ójöfn og óskjalfest.
- **Stig 3, Stöðlun:** Sameiginleg mynstur stýra sjálfræði, verkfæraheimildum, sandkössum og mann-í-lykkjunni hliðum, skjalfest og framfylgd yfir öll teymi. Sérhver afleidd aðgerð er hliðuð eða staðfest, fulltrúar eru raktir frá enda til enda og sjálfvirkt matssafn með árangurshlutfallseinkunn keyrir á hverja breytingu. Fyrirmælainnspýting er meðhöndluð sem viðvarandi ógn með skilgreind viðbrögð.
- **Stig 4, Stjórnun:** Fulltrúaeignasafnið er mælt og stýrt gegn grunnlínum. Árangurshlutfall á verk, árangur innspýtingarvarna, kostnaður og skrefafjöldi á keyrslu, tafir á mannlegu samþykki og lykkju- eða bilunaratvik eru rakin sem mælikvarðar. Afturköllunar- og drápsþröskuldum er framfylgt á þeim sönnunargögnum frekar en kvörtunum. Fjárhagsáætlanir á keyrslu fyrir skref, tíma og útgjöld eru vaktaðar og afturför í hvaða mælikvarða sem er kallar fram aðgerð fyrir stærð, ekki eftir atvik.
- **Stig 5, Samhæfing:** Sjálfræði er parað við verkáhættu með stefnu og stillt samfellt eftir því sem niðurstöður berast. Samfellt óbeintengt og beintengt mat tengir hegðun fulltrúa við viðskiptaniðurstöður og skipulagsheildin leggur reglulega niður, endurmarkar eða endurheimilar fulltrúa þegar áhættumyndin breytist. Rakning, kostnaðarfjárhagsáætlanir og úttektarslóðir eru samræmdar yfir eignasafnið. Innspýtingar- og blekkta umboðsmannsvarnir eru prófaðar andstæðingslega og ábyrgð á sjálfráðum aðgerðum er skýr og úttektarhæf.

## Hugmyndir til umræðu

1. Hverjir af núverandi mállíkanseiginleikum þínum eru hljóðlega orðnir fulltrúar og hefur sjálfræði hvers verið afmarkað af ásetningi?
2. Fyrir hvert fulltrúaverkfæri, hver er ódýrasta leiðin sem árásaraðili gæti misnotað það gegnum innspýtt efni og hvað stöðvar það?
3. Hvar hefurðu valið fjölfulltrúahönnun og geturðu sýnt að samræmingarkostnaðurinn borgaði sig gegn einum fulltrúa?
4. Hvaða fulltrúaaðgerðir eru í raun óafturkræfar og gætirðu endurhannað hverja þeirra til að vera afturkræfa eða sviðsetta?
5. Ef fulltrúi tæki skaðlega aðgerð á morgun, gætirðu endurbyggt nákvæmlega hvað hann gerði og hver bar ábyrgð?

## Helstu atriði

- Fulltrúi er mállíkan í lykkju með verkfærum, minni og markmiði. Áhættan býr í lykkjunni og verkfærunum, ekki textanum.
- Kjóstu fast vinnuflæði þegar skrefin eru þekkt. Taktu frá sjálfræði fyrir raunverulega opin markmið og afmarkaðu það þröngt.
- Verkfærabeiting er kjarnageta. Gefðu hverju verkfæri lágmarksréttindi, staðfest skema og sandkassa.
- Hliðaðu afleiddar og óafturkræfar aðgerðir á bak við mann með raunverulegt vald og hannaðu fyrir ódýra afturköllun.
- Líttu á umhverfið sem fjandsamlegt: varastu fyrirmælainnspýtingu og blekkta umboðsmannsmisnotkun (kafli 4.2).
- Metdu á verkárangurshlutfalli yfir margar keyrslur og raktu hverja keyrslu fyrir aflúsun, kostnaðarstýringu og úttekt (kaflar 6.5 og 6.6).
- Oft er rétta svarið að smíða alls ekki fulltrúa.

## Heimildir og frekari lestur

- Shunyu Yao et al., *ReAct: Synergising Reasoning and Acting in Language Models*.
- Timo Schick et al., *Toolformer: Language Models Can Teach Themselves to Use Tools*.
- Anthropic, *Building Effective Agents* (engineering guidance on workflows versus agents).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications* (including prompt injection and excessive agency).
- Simon Willison, writing on prompt injection and the "lethal trifecta" for AI agents.
- Norman Hardy, *The Confused Deputy* (the classic statement of the confused-deputy problem).
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach* (intelligent agents and rational action).
