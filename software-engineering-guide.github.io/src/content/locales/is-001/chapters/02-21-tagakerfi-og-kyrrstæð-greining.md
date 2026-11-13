# 2.21 Tagakerfi og kyrrstæð greining

## Yfirlit og tilgangur

Flestir gallar eru gripnir seint, í keyrslu, af prófi eða notanda eða atviki. Heill flokkur þeirra þarf aldrei að ná svo langt. [Tagakerfi](https://en.wikipedia.org/wiki/Type_system) og gott [kyrrstætt forritagreiningar](https://en.wikipedia.org/wiki/Static_program_analysis)verkfæri lesa kóðann þinn áður en hann keyrir og sanna að ákveðin mistök geti ekki gerst: strengur notaður þar sem tölu er krafist, núll afvísað, breyta lesin áður en hún er skrifuð, tilvik skilið eftir ómeðhöndlað. Þessi kafli fjallar um að ýta réttleika til vinstri, nær augnablikinu þegar þú skrifar línuna, þar sem lagfæring kostar sekúndur í stað blaðsíðu í atvikarýni.

Kyrrstæð greining er hver sú aðferð sem skoðar frumkóða eða þýddan kóða án þess að keyra hann. Tagaathugun er útbreiddasta formið, en fjölskyldan inniheldur líka lint-tól (verkfæri sem merkja stílbundin og réttleikamynstur), gagnaflæðisgreina og, í fjarlægari endanum, formlega sannprófun. Sameiginlega loforðið er flokkur ábyrgða sem þú færð ókeypis á hverri smíði, að eilífu, án prófs til að skrifa og án rýnis til að muna. Það loforð er ástæða þess að þessi agi situr við hlið kóðunarstaðla (kafli 2.1), hönnunarreglna hugbúnaðar (kafli 2.2) og prófunarstefnu (kafli 2.4): hann er enn ein sjálfvirk leið til að gera stóran kóðagrunn öruggan til að breyta.

Fyrir stór teymi safnast gildið upp. Þegar hundruð verkfræðinga snerta sameiginlegt kerfi er tagaundirskrift samningur sem þýðandi framfylgir á hverjum þeirra, og athugari í leiðslunni er rýnir sem þreytist aldrei og hyglir engum. Í fyrirtækjaumhverfi lækkar þetta kostnað móttöku og samþættingar, því tögin skjalfesta ásetning og greinendurnir grípa mistökin sem nýliðar gera. Í opinberum og öðrum hávirðiskerfum, þar sem rangt svar getur neitað bótum eða afhjúpað gögn, eru vélrænt athugaðar ábyrgðir sönnun: þær sýna endurskoðanda að heilir flokkar galla eru ómögulegir með smíði, ekki bara óprófaðir. Þetta tengist beint hugbúnaðargæðum (kafli 2.11) og forritaöryggi (kafli 4.2).

## Meginreglur

- Ýttu réttleika til vinstri: gríptu galla við höfundartíma, ekki í framleiðslu.
- Kjóstu ábyrgðir sem vélin athugar fram yfir venjur sem menn verða að muna.
- Kóðaðu ásetning í tög svo ólögleg ástönd geti alls ekki verið framsett.
- Taktu upp tög smám saman í kviku kóða. Þú þarft ekki allt eða ekkert.
- Líttu á viðvaranir sem villur og skrúfaðu grunnlínuna svo hún geti aðeins batnað.
- Keyrðu sömu greina í ritlinum og í leiðslunni, með eins reglum.
- Stýrðu röngum jákvæðum niðurstöðum með agaðri, rökstuddri, rýnanlegri niðurfellingu.

## Ráðleggingar

### Veldu kyrrstæða eða kvika tagun með opin augu

Í kyrrstætt tögðu tungumáli eru tög athuguð áður en forritið keyrir. Í [kviku tögðu](https://en.wikipedia.org/wiki/Dynamic_programming_language) eru þau athuguð meðan það keyrir, ef yfirleitt. Hvorugt er altækt rétt, og heiðarlega römmunin er skipti á ábyrgðum fyrir sveigjanleika. Kyrrstæð tagun kaupir vélrænt athugaða samninga, endurbyggingu sem þú getur treyst og verkfæri (sjálfvirk útfylling, örugg endurnefning, stökk-að-skilgreiningu) sem vita hvað hlutir eru. Kvik tagun kaupir hraða frumgerðasmíði, hnitmiðaðan kóða og lágan helgisið sem hentar skriftum og könnunarvinnu. Því stærra, langlífara og hærri hagsmunir kerfisins, því meira borgar kyrrstæða hliðin sig, því kostnaður heildarkóðagrunns endurbyggingar og kostnaður keyrslutagavillu vaxa báðir með stærð.

Vertu nákvæmur um annan, hornréttan ás: sterk á móti veik tagun. Sterk tagað tungumál neitar að þvinga hljóðlega ósamrýmanleg tög (að leggja tölu við streng gefur villu). Veikt tagað breytir hljóðlega og framleiðir óvæntar uppákomur eins og `"3" + 4` sem gefur eitthvað sem þú ætlaðir ekki. Þú getur haft kyrrstæða og veika, eða kvika og sterka. Þegar þú metur tungumál skaltu spyrja bæði spurninganna sérstaklega, því „sterk“ er oft það sem fólk vill í raun þegar það segir „tagað“.

### Hallaðu þér að tagaályktun til að halda tögum ódýrum

Algeng andmæli gegn kyrrstæðri tagun er hávaðinn af því að skrifa tag á hverja línu. [Tagaályktun](https://en.wikipedia.org/wiki/Type_inference) fjarlægir mest af þeim kostnaði: þýðandinn leiðir tög af samhengi, svo þú skýrir mörkin (aðgerðaundirskriftir, opinber viðmót) og lætur innra ástandið vera ályktað. Nútímatungumál álykta ágengt og gefa þér öryggi kyrrstæðrar athugunar með miklu af hnitmiðun kviks kóða. Taktu upp húsareglu sem skýrir hlutana sem lesandi reiðir sig á sem samning, útfluttar aðgerðir og opinberar gerðir, og skilur staðbundnar breytur eftir ályktun. Þetta heldur undirskriftum heiðarlegum og sjálfskjalfestandi en hlífir innra ástandinu við ringulreið, og tengist læsileikamarkmiðum kafla 2.1.

### Gerðu ólögleg ástönd óframsetjanleg

Öflugasta hugmyndin í hagnýtri tagahönnun er að móta tög þín svo rangt ástand sé ekki hægt að skrifa niður. Ef pöntun er annaðhvort „drög“ án greiðslu eða „lögð inn“ með greiðslu skaltu ekki móta hana sem eina byggingu með núllgildum reitum þar sem drög gætu óvart borið greiðslu og innlögð pöntun gæti borið enga. Mótaðu hana sem [summugerð](https://en.wikipedia.org/wiki/Tagged_union) (einnig kölluð merkt sambandsgerð, mismunandi sambandsgerð eða afbrigði): gildi sem er nákvæmlega ein af föstu safni forma, hvert ber eigin gögn. Nú eru ógildu samsetningarnar ekki til, og kóði sem meðhöndlar gildið verður að gera grein fyrir hverju tilviki eða þýðandinn kvartar. Þetta breytir keyrslu-„ætti aldrei að gerast“ í þýðingartíma-„getur ekki gerst“, sem er allur tilgangurinn.

Sama eðlisávísun knýr nokkur hversdagsverkfæri. Notaðu talningagerð í stað töfrastrengs fyrir fast safn ástanda. Vefðu staðfest gildi í sérstaka gerð (`EmailAddress` frekar en bera strenginn) svo „óstaðfest inntak“ og „staðfest netfang“ séu ólík tög sem þýðandinn heldur aðskildum. Þetta er tagakerfistjáning mörkastaðfestingaragans úr villumeðhöndlun (kafli 2.20): staðfestu einu sinni á jaðrinum, breyttu í gerð sem kóðar ábyrgðina og láttu innri kóða treysta henni.

### Taktu núllgildi og sniðmát alvarlega

[Núllbendillinn](https://en.wikipedia.org/wiki/Null_pointer), sem uppfinningamaður hans kallaði „milljarða dollara mistök“ sín, er algengasta leiðin sem kyrrstætt tagakerfi laug áður fyrr: gildi tagað sem strengur gat verið núll í leyni, og þú komst að því með hruni. Nútímatagakerfi laga þetta með því að gera núllgildi skýrt. Gildi er annaðhvort `String` sem er aldrei núll eða `Option`/`Maybe`/núllgild gerð sem þú verður að taka upp fyrir notkun, og þýðandinn neyðir þig til að meðhöndla tóma tilvikið. Ef tungumál þitt býður ekki-núllgildar gerðir eða valkvæða gerð skaltu nota þær alls staðar og líta á bert núllgilt sem lykt. Þetta fjarlægir heila ætt framleiðsluhruna.

[Sniðmát](https://en.wikipedia.org/wiki/Generic_programming) (generics), einnig kölluð stikuð margmyndun, leyfa þér að skrifa kóða sem virkar yfir margar gerðir án þess að yfirgefa tagaöryggi: `List<T>` er listi af einhverri tiltekinni gerð `T`, athugaður við þýðingu, frekar en listi af ótögðum hlutum sem þú steypir og biður fyrir. Náðu í sniðmát til að smíða endurnýtanleg ílát, aðgerðir og ágripanir sem haldast sterkt tagaðar. Parið summugerðir, ekki-núllgildar gerðir og sniðmát er það sem lætur nútímatagakerfi tjá raunverulegar lénsreglur frekar en bara merkja frumstæður.

### Taktu upp tög smám saman í núverandi kviku kóða

Þú þarft ekki að endurskrifa kvikan kóðagrunn til að fá ávinning tagunar. [Stigvaxandi tagun](https://en.wikipedia.org/wiki/Gradual_typing) leyfir tögðum og ótögðum kóða að sambúa, svo þú bætir við tögum smám saman þar sem þau borga sig mest. Mörg vistkerfi styðja þetta nú beint: tagavísbendingar í Python athugaðar af sérstökum tagaathugara, tagað yfirmengi sem þýðist í kvikt tungumál eða tagaskýringar lagðar yfir núverandi keyrsluumhverfi. Byrjaðu á mörkum og mikilvægustu einingum (peningakóðanum, öryggiskóðanum, gagnalíkaninu), kveiktu á athugaranum í frjálslegum ham og hertu hann með tímanum. Bættu við reglu um að nýr kóði verði að vera tagaður meðan gamli kóðinn nær í. Innan fárra ársfjórðunga getur stór ótagaður kóðagrunnur náð því marki að flestar breytingar eru tagaathugaðar, og mikilvægustu hlutarnir eru þaktir fyrst.

### Keyrðu lint-tól, tagaathugara og dýpri greina saman

Tagaathugun er eitt lag. Bættu við hinum. [Lint](https://en.wikipedia.org/wiki/Lint_(software))-tól grípur grunsamleg mynstur sem tagaathugari hunsar: úthlutun sem er alltaf sönn, ónotaða breytu, gegnumfall í switch, tilfang sem aldrei er lokað. Dýpri greinar rökræða um hegðun forritsins. [Gagnaflæðisgreining](https://en.wikipedia.org/wiki/Data-flow_analysis) rekur hvernig gildi ferðast gegnum kóðann til að svara spurningum eins og „er þessi breyta nokkurn tíma notuð áður en henni er úthlutað“ eða „getur þessi skráarhöndlun lekið á villuleið“. Mörg þessara verkfæra byggja á [ágripunartúlkun](https://en.wikipedia.org/wiki/Abstract_interpretation), aðferð sem keyrir forritið í ágripun yfir mengi mögulegra gilda (til dæmis „jákvætt“, „núll“ eða „neikvætt“ í stað nákvæmra talna) til að sanna eiginleika yfir allar keyrslur í einu, án þess að keyra nokkra eina.

Sumir greinar sitja við hlið öryggisverkfæra. Kyrrstæð forritaöryggisprófun (SAST) skannar frumkóða fyrir veikleikamynstur eins og innsprautun, óörugga afraðgreiningu eða litað gögn sem ná hættulegri viðtöku, og deilir gagnaflæðisvélbúnaðinum sem lýst er hér. Líttu á hana sem hluta þessarar fjölskyldu og samhæfðu hana forritaöryggi (kafli 4.2). Hagnýta ráðleggingin er lagskipt safn: hraður lint-tól fyrir stíl og augljósa galla, tagaathugari fyrir samninga og einn eða fleiri dýpri greinar fyrir eiginleikana sem skipta máli á þínu sviði. Stilltu þá úr útgáfustýrðum skrám svo reglurnar séu þær sömu fyrir alla.

### Líttu á viðvaranir sem villur og skrúfaðu grunnlínuna

Viðvörun sem lætur ekki smíðina mistakast er viðvörun sem verður hunsuð. Þegar skrá fyllist af hundruðum umborinna viðvarana les enginn hana og sú sem skiptir máli felur sig í hávaðanum. Taktu upp viðvaranir-sem-villur stefnu svo ný viðvörun brjóti smíðina og sé löguð á augnabliki þegar það er ódýrast. Á eldri kóðagrunni með þúsundir núverandi viðvarana geturðu ekki snúið þeim rofa á einni nóttu, svo notaðu skrúfu: skráðu núverandi talningu sem grunnlínu, hindraðu hverja breytingu sem eykur hana og knúðu hana niður með tímanum. Grunnlínan getur aðeins fallið. Þetta leyfir þér að kveikja á ströngri reglu í dag án mikillar hreinsunar fyrirfram, á meðan þú tryggir að ástandið versni aldrei og batni jafnt og þétt.

### Tengdu greiningu inn í ritla og CI, með hraðri endurgjöf

Kyrrstæð greining borgar sig mest þegar endurgjöf er tafarlaus. Keyrðu sömu athuganir í ritlinum, gegnum [Language Server Protocol](https://en.wikipedia.org/wiki/Language_Server_Protocol) eða jafngildi, svo hönnuður sjái villuna þegar hann skrifar, áður en hann vistar jafnvel. Keyrðu síðan eins reglusafn í samfelldri samþættingu (CI) svo ekkert sameinist án þess að standast, sem tengist leiðslu kafla 8.1. Þetta tvennt verður að vera sammála: ef ritillinn er mildur og CI strangt, eða öfugt, missir fólk traust á hvoru tveggja. Haltu greiningunni nógu hraðri til að keyra á hverri breytingu, geymdu niðurstöður í skyndiminni og greindu aðeins það sem breyttist þar sem þú getur, svo athugarinn sé hjálp en ekki skattur. Þegar ritill og leiðsla framfylgja sömu reglum á sama hátt hættir staðallinn að vera skjal sem fólk gleymir og verður eiginleiki umhverfisins.

### Taktu frá formlega sannprófun fyrir kóðann sem verðskuldar hana

Í fjarlægari enda sviðsins liggur [formleg sannprófun](https://en.wikipedia.org/wiki/Formal_verification): að sanna stærðfræðilega að forrit uppfylli nákvæma tilgreiningu, ekki bara að það standist próf. Aðferðir spanna líkanaprófun (tæmandi könnun ástanda kerfis) til setningasönnunar og háðra tagagerða (tög nógu tjáningarrík til að kóða fullar tilgreiningar). Þetta er dýpsta ábyrgðin sem í boði er og dýrust að framleiða, svo hún vinnur sér aðeins inn pláss þar sem galli er skelfilegur eða þar sem vottun krefst þess: dulritunarbókasöfn, flugstýringarkóði, hypervisor, mikilvæg samskiptaregla. Fyrir flestan hugbúnað er rétta fjárfestingin sterk tög auk góðra greina, sem fanga mestan ávinninginn á broti af kostnaði. Vittu að formlegar aðferðir (kynntar í kafla 2.12) eru til og hvar línan liggur, svo þú náir í þær af ásetningi á sjaldgæfa íhlutinn sem þarf þær.

### Haltu niðurfellingu heiðarlegri

Enginn greinir er fullkominn, og agi sem aðskilur treyst verkfæri frá hunsuðu er hvernig þú meðhöndlar mistök þess. Sérhvert alvarlegt verkfæri leyfir þér að fella niður niðurstöðu. Krefstu þess að hver niðurfelling sé þröng (ein lína eða ein niðurstaða, aldrei heil skrá eða regla), beri ástæðu í athugasemd og sé sýnileg í rýni eins og hver annar kóði. Altæk slökkvun efst í skrá er hvernig þekja rotnar hljóðlega. Úttektaðu niðurfellingar reglulega og líttu á vaxandi haug af þeim sem merki um að regla sé rangt kvörðuð eða að kóðinn hafi raunverulegt vandamál sem einhver felur. Heiðarleg niðurfelling heldur verkfærinu trúverðugu. Þögul, yfirgripsmikil niðurfelling breytir því í leikhús.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
|---|---|---|
| Kyrrstæð tagun | Vélrænt athugaðir samningar, öruggar endurbyggingar, rík verkfæri | Meiri helgisiður fyrirfram, hægari snemma frumgerðasmíði |
| Kvik tagun | Hröð að skrifa, sveigjanleg, lítill helgisiður | Tagavillur birtast í keyrslu, endurbyggingar áhættusamar |
| Tagaályktun | Öryggi með hnitmiðun, minni skýringahávaði | Ályktuð tög geta hulið ásetning ef ofnotað |
| Stigvaxandi tagun | Stigvaxandi upptaka, þekja mikilvægan kóða fyrst | Ótagaðir jaðrar leka enn, hlutaábyrgðir |
| Lint-tól og gagnaflæðisgreining | Grípa galla sem tög missa af, ódýrt að keyra | Rangar jákvæðar, hávaði ef óstillt |
| Viðvaranir-sem-villur með skrúfu | Nýjum vandamálum hindrað, grunnlína batnar aðeins | Getur fundist hindrandi, þarf niðurfellingarstefnu |
| Formleg sannprófun | Sterkasta ábyrgð, sannar eiginleika fyrir öll inntök | Dýr, sérhæfð, sjaldan réttlætt |

Endurtekna spennan er ábyrgðir gegn núningi. Hvert skref í átt að strangari tagun og dýpri greiningu kaupir þér flokk galla sem verður ómögulegur, og hvert skref bætir við helgisið, verkfæratíma og stöku röngu jákvæðu sem kostar hönnuð mínútur. Leystu það eftir hagsmunum og líftíma. Einnota skrifta eða tilraun vill létta, hraða, kvika endann. Greiðsluhöfuðbók, heimildaathugun eða kerfi sem ríkið mun reka í fimmtán ár vill sterk tög, lagskipta greina, viðvaranir-sem-villur og, fyrir hættulegasta kjarnann, kannski formlega sönnun. Láttu nákvæmni samsvara kostnaði þess að hafa rangt og láttu ályktun og stigvaxandi upptöku halda núningnum viðráðanlegum.

## Spurningar til að ræða með teyminu

1. **Hvar í kóðagrunninum okkar hefði tagakerfi komið í veg fyrir síðustu framleiðsluatvik okkar og vitum við það?** Flest teymi rökræða um tagun í óhlutbundnu þegar sönnunargögnin sitja í eigin atvikasögu. Dragðu síðustu tíu eða tuttugu framleiðslugalla og flokkaðu þá: hve margir voru núll þar sem gildi var vænst, röng lögun send yfir mörk, ómeðhöndlað tilvik, strengjagert gildi sem rak? Þetta eru einmitt gallarnir sem tagaathugari og lint-tól grípa ókeypis. Ef stór hluti atvika þinna er í þeirri körfu hefurðu áþreifanleg, dollaramæld rök fyrir sterkari tagun í einingunum þar sem þau gerðust. Ef nánast engin eru það lifa gallarnir þínir annars staðar (rökfræði, samtími, kröfur) og þyngri tagun er kannski ekki verðmætasta hreyfing þín. Hvort sem er skiptirðu skoðun út fyrir gögn.

2. **Ef við tækjum upp stigvaxandi tagun, hvar myndum við byrja og hvað myndi „nógu gott“ þýða?** Að kveikja á athugara yfir stóran kvikan kóðagrunn er áætlun, ekki rofi, og röðunin ræður hvort það tekst eða stöðvast. Ræddu hvaða einingar bera mesta áhættu (peningar, auðkenning, kjarnagagnalíkan) og verðskulda því tög fyrst, á móti hverjar eru stöðugar og nógu áhættulitlar til að skilja ótaggaðar í bili. Komdu þér saman um reglu fyrir nýjan kóða (tagaður frá fyrsta degi) svo ótagaða yfirborðið hætti að vaxa meðan þú höggvum í afganginn. Skilgreindu markmið: kannski sérhver opinber aðgerðaundirskrift tögð, sérhver mörk staðfest í gerð, athugarinn keyrandi í ströngum ham á mikilvægu pökkunum. Án skilgreindrar marklínu verður stigvaxandi tagun eilíf og hálfþakin, sem er það versta af báðu.

3. **Hver er stefna okkar þegar kyrrstæður greinir hefur rangt fyrir sér og heldur hún verkfærinu traustu?** Sérhver greinir framleiðir rangar jákvæðar, og hvernig þú meðhöndlar þær ræður hvort verkfærið helst gagnlegt eða er afvirkjað í gremju. Farðu í gegnum áþreifanleg tilvik: þegar niðurstaða er ósvikin röng jákvæð, er niðurfellingin þröng, með ástæðu í athugasemd og sýnileg í rýni, eða afvirkjar einhver alla regluna fyrir allt hugbúnaðarsafnið? Líttu á núverandi niðurfellingar þínar: hve margar eru til, bera þær rökstuðning og hvenær úttektaði einhver þær síðast? Haugur óútskýrðra, víðra niðurfellinga þýðir að þekja þín er hljóðlega holur. Markmiðið er sameiginlegur, framfylgdur agi sem heldur greininum trúverðugum, svo niðurstöður hans séu treystar og brugðist við þeim frekar en að vera viðbragðsdrifið þaggað niður.

4. **Hvaða tungumál og greina staðlaðum við og hvernig höldum við einu reglusafni þegar stakkurinn okkar sundrast yfir teymi?** Þegar hundruð verkfræðinga vinna á nokkrum tungumálum eyðileggur hvert teymi sem rekur til eigin athugara, eigin lint-reglna og eigin strangleikastillingar hljóðlega ábyrgðina, því samningur sem er framfylgdur í einu hugbúnaðarsafni er bara ábending í því næsta. Togið á móti er raunverulegt: miðlæg stöðlun gefur þér færanlega verkfræðinga og einsleit úttektargögn, en samt getur reglusafn lagt á frá miðjunni stangast á við málvenjur tungumáls eða hægt á teymi sem hafði góðar ástæður fyrir eigin stillingu. Komdu með skrá yfir tungumálin í framleiðslu, greina og útgáfur sem hvert teymi rekur og mismun á reglusöfnum þeirra svo rekið sé sýnilegt en ekki gert ráð fyrir. Í fyrirtækja- eða opinberu umhverfi skaltu tengja svarið við innkaup og úttekt: ein útgáfustýrð stilling sem hvert hugbúnaðarsafn erfir er það sem leyfir endurskoðanda að staðfesta að sömu athuganir hafi keyrt alls staðar, og það stöðvar birgi frá því að afhenda kóða undir veikari reglum en eigið starfsfólk þitt verður að uppfylla.

5. **Hve hröð er greining okkar og á hvaða punkti byrjar fólk að fara fram hjá henni?** Athugari er aðeins ábyrgð ef hann keyrir á hverri breytingu, og um leið og hann gerir breyta-smíða-lykkjuna sársaukafulla læra verkfræðingar að sleppa honum, afvirkja hann staðbundið eða sameina með hann rauðan og lofa að laga seinna. Spennan er dýpt gegn hraða: dýpri gagnaflæðis- eða öryggisgreining finnur galla sem hraður lint-tól missir af, en ef full röðin tekur tuttugu mínútur hætta menn að bíða eftir henni, og athugun sem enginn bíður eftir verndar ekkert. Komdu með raunverulegu tölurnar í umræðuna: ritlaendurgjafartöf, CI-veggklukkutíma greiningarstigs, skyndiminnishittihlutföll, hve oft smíðar eru sameinaðar með athuganir sleppt eða yfirskrifaðar og hve mikið af keyrslunni er stigvaxandi á móti full. Fyrir stóra eða opinbera skipulagsheild skaltu bæta við útreikningsreikningnum og afkastakostnaðinum, því í flotastærð er hægt skyldubundið greiningarstig bæði fjárhagslína og biðröð sem seinkar hverri útgáfu, og heiðarlega lausnin er venjulega stigvaxandi greining og skyndiminni frekar en að slaka hljóðlega á reglunum.

6. **Hvaða vélrænt athuguðu sönnunargögn getum við í raun framleitt fyrir endurskoðanda og hverjar mikilvægu fastayrðingar okkar ná þau yfir?** Í eftirlitsskyldum og hávirðiskerfum er tilgangur tagunar og kyrrstæðrar greiningar sýnileg sönnun þess að heilir flokkar galla séu ómögulegir með smíði, umfram daglegu gallana sem hún kemur í veg fyrir, og sú fullyrðing er einskis virði ef þú getur ekki sýnt hvaða fastayrðingar eru framfylgdar og hvar. Málamiðlunin er umfang gegn kostnaði: að sanna meira (ekki-núllgildi alls staðar, summugerðir fyrir hvert löglegt ástand, formleg sannprófun á kjarnaútreikningnum) kaupir sterkari sönnunargögn, en hvert skref upp á við í nákvæmni kostar skýringafyrirhöfn, sérfræðitíma og smíðaflækju sem þú þarft kannski ekki á áhættulitlum kóða. Komdu með kort af öryggiskritískum einingum þínum að ábyrgðunum sem hver ber nú, lista yfir opnar niðurfellingar með rökstuðningi þeirra og öll bil þar sem mikilvæg regla er framfylgd með venju frekar en þýðandanum. Fyrir opinbera eða eftirlitsskylda skipulagsheild skaltu ramma þetta sem vottunarsönnunargögn: endurskoðandi ætti að geta rakið nauðsynlegan eiginleika til vélrænt athugaðrar gerðar eða sönnunar og séð niðurfellingarskrána sem skjalfestir hverja undantekningu, svo regluvarsla hvíli á afurðum sem verkfærakeðjan býr til en ekki handvirkri rýni eftir á.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Hraði vinnur, svo náðu í ódýrasta öryggið sem hægir ekki á þér: sterktagað tungumál eða tagaathugari í frjálslegum ham, auk hraðs lint-tóls í ritlinum, og tagaðu peninga- og auðkenningarkóðann fyrst. Slepptu formlegri sannprófun og djúpum gagnaflæðisgreinum alveg, þeir kosta tíma sem þú hefur ekki. Ávinningurinn sem þú vilt snemma er endurbygging sem þú getur treyst við tíu þúsund línur, svo kveiktu á athugaranum áður en kóðagrunnurinn er of stór til að temja.

**Lítið fyrirtæki.** Án kyrrstæðrar greiningarsérfræðings á launaskrá skaltu kjósa tungumál og verkfærakeðju þar sem góð sjálfgefin gildi eru innbyggð frekar en safn sem þú verður að stilla og hafa umsjón með. Keyptu greininguna innbyggða í IDE-ið þitt og hýsta CI frekar en að setja upp eigin vettvang og haltu reglusafninu nálægt samfélagsstaðlinum svo verktaki eða nýr starfsmaður þekki það. Líttu á viðvaranir-sem-villur og lítinn tagaðan kjarna sem áhrifamestu hreyfingar sem takmarkað fjárhagsáætlun þín getur gert.

**Stórfyrirtæki.** Verkið er stjórnarhættir yfir mörg teymi: ein útgáfustýrð stilling sem hvert hugbúnaðarsafn erfir, eins reglur í ritlinum og leiðslunni og skrúfuð grunnlína svo þekja neins teymis geti ekki hljóðlega fallið. Staðlaðu greinana, raktu tagaþekju og niðurfellingatalningar sem eignasafnsmælikvarða og úttektaðu niðurfellingar á föstum takti svo vélrænt athugaðar ábyrgðir haldist nógu einsleitar til að endurskoðandi geti reitt sig á þær. Fjárhagsáætlaðu vettvangsteymið sem á sameiginlegu stillinguna, því samræmi yfir þúsundir verkfræðinga viðheldur sér ekki sjálft.

**Hið opinbera.** Innkaup, gagnsæi og langir líftímar ráða. Krefstu þess í samningum að birgjar uppfylli sömu greiningarreglur og eigið starfsfólk þitt og afhendi stillinguna og niðurfellingarskrárnar sem afurðir, svo ábyrgðin lifi söluaðilaskipti. Kjóstu vélrænt athuguð sönnunargögn fram yfir handvirka tryggingu fyrir hæfis- og greiðslurökfræði, taktu frá formlega sannprófun fyrir útreikninga þar sem bilun myndi ólöglega neita bótum og haltu hverri niðurfellingu skjalfestri til úttektar yfir áratuginn eða meira sem kerfið mun keyra.

## Dæmi

**Sprotafyrirtæki.** Sex manna sprotafyrirtæki smíðar vöru sína í kviku tungumáli fyrir hraða, sem þjónar þeim vel þar til endurbygging við tíu þúsund línur byrjar að valda keyrslutagavillum sem þeir finna aðeins í framleiðslu. Þeir taka upp stigvaxandi tagun: þeir kveikja á tagaathugara í frjálslegum ham, bæta tagavísbendingum fyrst við kjarnalénslíkanið og greiðslukóðann og setja reglu um að allar nýjar einingar séu fulltagaðar. Þeir tengja athugarann og lint-tól inn í ritilinn og CI með eins stillingu og líta á nýjar viðvaranir sem villur á meðan þeir skrúfa núverandi niður. Innan tveggja ársfjórðunga hverfa hrunin vegna ósamræmdra forma, endurbygging hættir að vera ógnvekjandi og sjálfvirk útfylling nýs starfsmanns veit í raun hvað hver aðgerð skilar. Fjárfestingin kostaði nokkrar verkfræðivikur og fjarlægði endurtekna uppsprettu viðskiptavinasýnilegra galla.

**Stórfyrirtæki.** Alþjóðlegur banki staðlar kyrrstæða greiningu yfir þúsundir verkfræðinga. Sérhvert hugbúnaðarsafn erfir sameiginlega stillingu: tagaathugari í ströngum ham, lint-tól, gagnaflæðisgreinir og SAST-skanni fyrir öryggismynstur, allt keyrandi í ritlinum og framfylgt í leiðslunni svo ekkert sameinist án þess að standast. Lénsgerðir gera ólögleg ástönd óframsetjanleg í kóðanum sem færir peninga: bókuð færsla og bið færsla eru ólíkar gerðir, gjaldmiðlar eru tagaðir svo þú getur ekki lagt dollara við evrur og staðfest inntök eru aðskildar gerðir frá hráum. Viðvaranir eru villur og grunnlína hvers teymis getur aðeins fallið. Niðurfellingar krefjast rökstuðnings og eru úttektaðar ársfjórðungslega. Því ábyrgðirnar eru vélrænt athugaðar og einsleitar geta endurskoðendur séð að heilir flokkar galla eru ómögulegir með smíði, og verkfræðingar færast af öryggi yfir ókunnar þjónustur.

**Hið opinbera.** Landsbundið skattayfirvald nútímavæðir bótaútreikningskerfi sem verður að vera rétt og útskýranlegt árum saman. Kjarnahæfisrökfræðin er skrifuð í sterktögðu tungumáli þar sem lénslíkanið kóðar reglurnar: staða umsækjanda er summugerð sem nær yfir öll lögleg tilvik, fjárhæðir eru sérstök gerð sem ekki er hægt að rugla við talningar og ekkert gildi sem gæti vantað er skilið eftir sem bert núllgilt. Kyrrstæð greining keyrir í CI sem hlið og öryggiskritískasta útreikningseiningin er að auki athuguð með formlegum aðferðum til að sanna að lykilfastayrðingar haldi fyrir öll inntök, sem fullnægir vottunarkröfum. Sérhver niðurfelling er skjalfest til úttektar. Þegar upphaflegir höfundar halda áfram erfa arftakar þeirra kóða þar sem þýðandinn framfylgir samningunum, svo þeir geti breytt honum örugglega áratug síðar.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun tagunar og kyrrstæðrar greiningar er tilfærsla á því hvar þú borgar fyrir galla. Galli gripinn af tagaathugara í ritlinum kostar sekúndur. Sami galli gripinn í framleiðslu kostar atvik, rannsókn, hugsanlega skaða viðskiptavina og eftirlitsniðurstöðu. Rannsóknir á gallahagfræði sýna stöðugt kostnað hækka um stærðargráðu á hverju stigi sem galli lifir af, frá höfundartíma til rýni til prófs til framleiðslu. Kyrrstæð greining færir heilan flokk galla á ódýrasta stigið, á hverri smíði, án vinnu á hvern galla. Það er fastur, að mestu einskiptis uppsetningarkostnaður sem kaupir ótakmarkaðan straum forðaðra galla, sem er nálægt besta vogarafli í verkfræði.

Kostnaðurinn er raunverulegur en hóflegur og fyrirfram hlaðinn. Þú velur og stillir verkfærin, þú borgar nokkurn helgisið í skýringum (mildaðan af ályktun), þú eyðir verkfræðitíma í að taka upp stigvaxandi tagun í eldri kóða og þú samþykkir stöku rangar jákvæðar. Settu það gegn heildareignarkostnaði valkostsins: sérhver tagalöguð galli sem nær framleiðslu, sérhver áhættusöm endurbygging forðuð því ekkert tryggir réttleika, sérhver hæg móttaka því kóðinn skjalfestir ekki eigin samninga og, í eftirlitsskyldu umhverfi, sérhver úttekt sem verður að fullnægja með handvirkri rýni en ekki vélrænt athuguðum sönnunargögnum. Til að færa rök við forystu skaltu tengja það við mælikvarða sem hún fylgist þegar með: bilanahlutfall breytinga, hlutfall galla sem sleppa, meðaltíma til endurheimtar og hlutfall atvika rakin til forðanlegra tega- og núllvillna. Línuritið sem sannfærir fólk er eigin atvikasaga þín flokkuð eftir því hvort athugari hefði gripið þau.

## Andmynstur og gildrur

- **Neyðarútgangurinn sem vani:** að steypa í `any`, `dynamic` eða ótagað jafngildi til að þagga niður athugarann, sem þurrkar út ábyrgðina einmitt þar sem þú þurftir hana mest.
- **Strengjagert allt:** að senda bera strengi og ótögð kort yfir mörk í stað þess að móta ástönd sem raunveruleg tög, svo þýðandinn getur ekki hjálpað.
- **Núllgilt sjálfgefið:** að skilja gildi eftir núllgild þegar tungumálið býður ekki-núllgildar og valkvæðar gerðir, sem varðveitir milljarða dollara mistökin.
- **Viðvaranir sem aldrei bila:** þúsundir umborinna viðvarana þar sem sú sem skiptir máli er ósýnileg, því ekkert brýtur nokkurn tíma smíðina.
- **Ritill og CI ósammála:** mildur staðbundið og strangur í leiðslunni, eða öfugt, svo hönnuðir vantreysta báðu og sameiningar koma fólki á óvart.
- **Altæk niðurfelling:** að afvirkja alla reglu eða skrá í stað einnar rökstuddrar niðurstöðu og hola hljóðlega út þekju.
- **Greiningarleikhús:** að keyra verkfæri þar sem enginn les eða bregst við niðurstöðum, svo skýrslurnar safnast og virðið er núll.
- **Allt-eða-ekkert tagun:** að neita að byrja því þú getur ekki tagað allt í einu og afsala þér stóru ávinningunum af því að tagað mikilvæga kóðann fyrst.
- **Sannprófun alls staðar:** að ná í formlegar aðferðir á venjulegum kóða og eyða af skornum skammti sérfræðifyrirhöfn þar sem sterk tög hefðu nægt.

## Þroskalíkan

- **Stig 1, Upphaf:** Tagun og greining eru ad hoc og á hvern hönnuð. Kvikur kóði hefur engan athugara, eða kyrrstætt tungumál keyrir með viðvaranir hunsaðar. Tagalöguð gallar (núll, röng form, ómeðhöndluð tilvik) ná reglulega framleiðslu og endurbygging er óttast því ekkert sannreynir réttleika.
- **Stig 2, Þróun:** Lint-tól og, þar sem viðeigandi, tagaathugari keyra á sumum verkefnum, en reglur eru ólíkar milli teyma, viðvaranir brjóta ekki smíðina og neyðarútgangar og víðar niðurfellingar eru algengar. Nokkur ávinningur næst, en þekja er ósamræmd og traust á verkfærunum er blettótt.
- **Stig 3, Stöðlun:** Sameiginleg, útgáfustýrð stilling framfylgir tagaathugun og lint í ritlinum og CI með eins reglum um alla skipulagsheildina. Viðvaranir eru villur með skrúfaða grunnlínu, núllgildi og summugerðir eru notaðar til að gera ólögleg ástönd óframsetjanleg á mörkum og sérhver niðurfelling krefst skjalfestrar, rýnanlegrar ástæðu.
- **Stig 4, Stjórnun:** Greining er mæld og stýrð gegn grunnlínum. Tagaþekja á mikilvægum einingum, viðvörunartalningar, röngu-jákvæðu hlutföll, niðurfellingatalningar og hlutfall framleiðsluatvika sem athugari hefði gripið eru allt rakin gegn skýrum markmiðum. Mælikvarðarnir hliða breytingu: þekja á peninga- og auðkenningarkóðanum má ekki falla, hækkandi rangt-jákvætt hlutfall kallar fram endurkvörðun reglna og mælaborð sýna hvort ábyrgðirnar halda í raun en ekki bara eru stilltar.
- **Stig 5, Samhæfing:** Greining er stöðugt bætt og samþætt um skipulagsheildina. Stigvaxandi tagun hefur náð mikilvægum einingum, gagnaflæðis- og öryggisgreinar keyra reglulega, reglur aðlagast eftir því sem tungumál og ógnir þróast og formleg sannprófun er beitt af ásetningi á fáa íhluti sem bilun væri skelfileg í. Verkfærin, mælikvarðarnir og reglusafnið næra aftur í hönnun, ráðningar og innkaup, svo öll skipulagsheildin verður jafnt og þétt öruggari til að breyta.

## Hugmyndir til umræðu

1. Hverjir af nýlegum framleiðslugöllum þínum hefði tagaathugari eða lint-tól gripið og hvaða hlutfall af heildinni tákna þeir?
2. Hvar í lénslíkani þínu gæti summugerð eða staðfest umbúðagerð breytt keyrslu-„ætti aldrei að gerast“ í þýðingartíma-„getur ekki gerst“?
3. Ef þú breyttir viðvörunum í villur á morgun, hve margar myndu brjóta smíðina og hvaða grunnlína og skrúfa myndi leyfa þér að taka upp stefnuna án hreinsunarkrossferðar?
4. Keyra ritillinn þinn og leiðslan nákvæmlega sömu reglur og hvernig myndi hönnuður komast að því ef þær hefðu rekið í sundur?
5. Hve margar niðurfellingar búa í kóðagrunninum þínum núna, hve margar bera rökstuðning og hvenær voru þær síðast úttektaðar?
6. Er einhver íhlutur í kerfinu þínu þar sem bilun er nógu skelfileg til að réttlæta formlega sannprófun og hvernig myndirðu vita það?

## Helstu atriði

- Kyrrstæð tagun og greining ýta heilum flokki galla á ódýrasta augnablikið til að laga þá: þegar þú skrifar kóðann, á hverri smíði, án vinnu á hvern galla.
- Kjóstu ábyrgðir sem vélin athugar fram yfir venjur sem menn verða að muna og kóðaðu ásetning í tög svo ólögleg ástönd geti alls ekki verið framsett.
- Þú þarft ekki allt eða ekkert: stigvaxandi tagun leyfir þér að þekja mikilvæga kóðann (peninga, auðkenningu, gagnalíkan) fyrst meðan restin nær í.
- Líttu á viðvaranir sem villur með skrúfaða grunnlínu, keyrðu eins reglur í ritlinum og CI og haltu niðurfellingu þröngri, rökstuddri og úttektaðri.
- Láttu nákvæmni samsvara hagsmunum: sterk tög auk lagskiptra greina fyrir flest kerfi og formleg sannprófun tekin frá fyrir sjaldgæfa íhlutinn sem bilun í er skelfileg.

## Heimildir og frekari lestur

- Benjamin C. Pierce, *Types and Programming Languages*
- Simon Peyton Jones (ed.), *The Implementation of Functional Programming Languages*
- Flemming Nielson, Hanne Riis Nielson, and Chris Hankin, *Principles of Program Analysis*
- Patrick Cousot and Radhia Cousot, "Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints"
- Scott Wlaschin, *Domain Modelling Made Functional*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Michael Barr and the MISRA Consortium, *MISRA C: Guidelines for the Use of the C Language in Critical Systems*
- Al Bessey et al., "A Few Billion Lines of Code Later: Using Static Analysis to Find Bugs in the Real World," Communications of the ACM
