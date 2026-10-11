# 3.1 Grunnatriði arkitektúrs

## Yfirlit og tilgangur

[Hugbúnaðararkitektúr](https://en.wikipedia.org/wiki/Software_architecture) er safn mikilvægra hönnunarákvarðana sem er dýrt að breyta: uppbygging helstu íhluta, tengsl þeirra á milli og eiginleikarnir sem kerfið í heild verður að sýna. Hugsaðu um hann sem sameiginlega hugmyndamynd sem lætur marga smíða eina samfellda vöru. Í litlu teymi getur arkitektúr lifað í fáum höfðum og þróast jafnóðum. Í stórri skipulagsheild (hundruð verkfræðinga, tugir teyma, margar vörur, ára vegvísir) verður arkitektúr það sem heldur öllum samhæfðum. Þegar hann er skýr hreyfast teymi sjálfstætt án árekstra. Þegar hann er óljós verður hvert þverteymisósjálfstæði að samningaviðræðum og hvert atvik að fornleifauppgreftri.

Fyrir fyrirtæki og hið opinbera skipta grunnatriðin enn meira máli, því kerfin eru langlíf, mjög eftirlitsskyld og sameiginleg milli deilda. Skattkerfi, bótavettvangur, landsskrá heilsufarsupplýsinga eða höfuðbók í kjarna banka mun lifa lengur en starfsferill þeirra sem smíðuðu það. Ákvarðanirnar sem þú tekur í dag um tengingu, gagnaeignarhald og [gæðaeiginleika](https://en.wikipedia.org/wiki/List_of_system_quality_attributes) þrengja hvað er mögulegt í áratug eða lengur. Eftirlitsaðilar og endurskoðendur ætlast sífellt meira til skjalfests, rökstudds arkitektúrs: sönnunargagna um að áreiðanleiki, öryggi, persónuvernd og aðgengi hafi verið hönnuð inn en ekki fest á eftir. Að ná grunnatriðunum rétt er ekki fræðilegt. Það er munurinn á vettvangi sem aðlagast nýjum kröfum og vettvangi sem þarf að endurbyggja frá grunni.

Þessi kafli fjallar um varanlegu grunnatriðin sem lifa af tækniæði: gæðaeiginleika („-leikana“), arkitektúrlega marktækar kröfur, hæfnisföll og þróunararkitektúr, létta skjölun með [C4](https://en.wikipedia.org/wiki/C4_model) og arc42 og skipulagða málamiðlanagreiningu. Þetta eru verkfærin sem láta stórt teymi rökræða um arkitektúr af ásetningi frekar en fyrir slysni.

## Meginreglur

- **Arkitektúr snýst um málamiðlanir, ekki rétt svör.** Sérhver mikilvæg ákvörðun skiptir einum gæðum fyrir önnur. Verkefnið er að gera þessi skipti af ásetningi og gagnsætt.
- **Gæðaeiginleikar eru kröfur.** Afköst, aðgengi, öryggi og viðhaldshæfni verður að tilgreina af sömu nákvæmni og eiginleika, annars verður þeim fórnað undir tímapressu.
- **Ekki er sérhver krafa arkitektúrlega marktæk.** Beindu takmarkaðri hönnunarathygli að kröfunum sem móta uppbyggingu, eru erfiðar að breyta eða bera mikla áhættu.
- **Arkitektúr verður að geta þróast.** Stór fyrirframhönnun mistekst því þekking er minnst í upphafi. Hannaðu stigvaxandi og verndaðu lykileiginleika með sjálfvirkum athugunum.
- **Skjalfestu ákvarðanir, ekki bara teikningar.** Rökin að baki vali (og valkostirnir sem var hafnað) eru verðmætari en mynd af niðurstöðunni.
- **Gerðu arkitektúrinn læsilegan þeim sem sköpuðu hann ekki.** Nýliðar, endurskoðendur og framtíðarviðhaldsaðilar verða að geta endurbyggt ásetninginn.
- **Frestaðu ákvörðunum sem þú getur, taktu þær sem þú verður.** Haltu valkostum opnum þar sem breyting er ódýr. Skuldbindu þig snemma aðeins þar sem seint val er dýrt.

## Ráðleggingar

### Tilgreindu gæðaeiginleika sem mælanleg sviðsmynd

Óljós markmið eins og „kerfið ætti að vera hratt“ eða „mjög aðgengilegt“ er hvorki hægt að prófa né framfylgja. Skrifaðu í staðinn hvern gæðaeiginleika sem áþreifanlega sviðsmynd með áreiti, samhengi og mælanlegu svari: „Þegar samtímis notendur á álagstíma ná 50.000 ljúka 95% leitarbeiðna innan 300 ms.“ Náðu yfir eiginleikana sem skipta máli á þínu sviði: aðgengi, afköst, stigvöxt, öryggi, viðhaldshæfni, sýnileika, notkunaraðgengi, flytjanleika og kostnaðarhagkvæmni. Raðaðu þeim upphátt, því þú getur ekki hámarkað þá alla í einu. Kerfi stillt fyrir hámarkssamræmi verður ekki líka hámarksaðgengilegt.

### Auðkenndu arkitektúrlega marktækar kröfur (ASR)

Taktu frá tíma til að aðgreina ASR frá venjulegum kröfum. Krafa er arkitektúrlega marktæk ef hún snertir marga íhluti, er dýr í uppfyllingu, leggur á strangt skilyrði eða er tæknilega áhættusöm. Reglugerðarkröfur (gagnabúseta, varðveisla, úttektarhæfni), háálagsatburðarásir, samþætting við eldri kerfi og harðar öryggismörk eru venjulega ASR. Haltu stuttum, lifandi lista yfir þær og raktu helstu hönnunarákvarðanir aftur til hans, svo rýnar sjái hvers vegna arkitektúrinn lítur út eins og hann gerir.

### Taktu upp þróunararkitektúr og hæfnisföll

Líttu á arkitektúr sem eitthvað sem breytist skref fyrir skref í stýrðar áttir, ekki sem fasta teikningu. **Hæfnisfall** (fitness function) er sjálfvirkt, hlutlægt próf á að tiltekinn arkitektúreiginleiki haldi: smíðatímaathugun á að engin eining flytji inn úr bönnuðu lagi, afkastapróf sem fellir leiðsluna ef p99 töf versnar, öryggisskönnun sem hindrar þekkt berskjölduð ósjálfstæði, próf sem staðfestir að engin þjónusta haldi beina tengingu við gagnagrunn annarrar þjónustu. Hæfnisföll breyta arkitektúrásetningi í handrið sem er framfylgt samfellt: eina leiðin til að halda þeim ásetningi lifandi yfir stórt, breytilegt teymi.

### Skjalfestu með C4 og arc42

Notaðu **C4-líkanið** til að lýsa uppbyggingu á fjórum aðdráttarstigum (kerfissamhengi, ílát, íhlutir og kóði) svo hver áheyrendahópur lesi stigið sem hentar honum og engin ein teikning þurfi að segja allt. Notaðu **arc42** sem sniðmát fyrir frásögnina í kring: markmið, skorður, samhengi, lausnarstefnu, byggingarkubba, keyrslusviðsmyndir, uppsetningu, þverlæg atriði, ákvarðanir og áhættur. Skráðu einstakar ákvarðanir sem stuttar **[arkitektúrákvörðunarskrár (ADR)](https://en.wikipedia.org/wiki/Architectural_decision)**: samhengi, ákvörðun, staða og afleiðingar, ein skrá á ákvörðun, útgáfustýrð ásamt kóðanum. Ef þú tekur upp aðeins einn skjölunarvenju skaltu gera hann að ADR: þær borga sig meira en nokkuð annað fyrir stór teymi.

### Keyrðu skipulagða málamiðlanagreiningu og láttu áhættu stýra hönnun

Fyrir kerfi með háa hagsmuni skaltu nota aðferð eins og **[málamiðlanagreiningaraðferð arkitektúrs (ATAM)](https://en.wikipedia.org/wiki/Architecture_tradeoff_analysis_method)** til að vega tilvonandi arkitektúra gegn forgangsröðuðum gæðaeiginleikasviðsmyndum. Hún dregur fram næmispunkta (þar sem ákvörðun hefur sterk áhrif á einn eiginleika) og málamiðlunarpunkta (þar sem hún hefur áhrif á nokkra). Fyrir léttari nálgun skaltu taka upp **áhættudrifna hönnun**: eyddu hönnunarfyrirhöfn í hlutfalli við áhættu. Áhættulitlir, vel skildir hlutar þurfa lítinn helgisið. Nýstárlegar, áhrifamiklar eða óafturkræfar ákvarðanir verðskulda frumgerðir, tilraunir og formlega rýni.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
|---|---|---|
| Þung fyrirframarkitektúr | Skýr samhæfing, færri seinar óvæntar uppákomur í áætlunum með föstu umfangi | Ákvarðanir teknar þegar þekking er minnst, hæg, brothætt gagnvart breytingum |
| Sprottin / þróunararkitektúr | Aðlagast námi, minni sóun, styður hraða afhendingu | Hætta á reki án hæfnisfalla, krefst sterks verkfræðiaga |
| Formlegt ATAM-mat | Nákvæm, úttektarhæf, dregur fram falda árekstra | Tíma- og sérfræðifrek, óþarfi fyrir litlar breytingar |
| Léttar ADR + C4 | Ódýrt, læsilegt, stigvaxandi, skalast á mörg teymi | Aðeins jafn gott og agi til að halda þeim réttum |

Meginspennan er vissa gegn aðlögunarhæfni. Áætlanir hins opinbera með föstu verði og öryggiskritísk kerfi hallast að meiri fyrirframnákvæmni og formlegu mati, því kostnaður seinnar breytingar eða bilunar er gríðarlegur. Hraðfara vöruskipulagsheildir hallast að þróunaraðferðum vörðum með sjálfvirkni. Flestar stórar skipulagsheildir þurfa hvort tveggja: þyngri stjórnarhætti á óafturkræfum, áhrifamiklum ákvörðunum og þverlægum atriðum, og léttari, sprottna hönnun alls staðar annars staðar. Báðir öfgar mistakast á sinn hátt: ofhönnun sóar árum og skilar engu, á meðan vanhönnun framleiðir flækju sem getur hvorki skalast né verið úttekin.

## Spurningar til að ræða með teyminu

1. **Þegar tveir gæðaeiginleikar þínir rekast á undir álagi, hvor vinnur og hefurðu skrifað þá forgangsröð niður?** Sérhver arkitektúr neyðir fram skipti: hámarkssamræmi grefur undan aðgengi, þétt öryggi bætir við töf, ágeng skyndiminni berst gegn úttektarhæfni. Í stóru teymi er hættan sú að ólík teymi geri hljóðlega ráð fyrir ólíkum forgangi, svo eitt hámarkar afköst á meðan annað gætir strangs samræmis, og árekstur birtist aðeins í atviki. Í fyrirtækja- og opinberu umhverfi mun eftirlitsaðili spyrja hvaða eiginleika þú verndaðir og hvers vegna, svo röðunin verður að vera skýr og rökstudd en ekki þjóðsaga. Komdu með gæðaeiginleikasviðsmyndir þínar og raðaðu þeim upphátt hverri gegn annarri, par fyrir par, þar til röðin er ótvíræð. Kóðaðu síðan sigurvegarann sem hæfnisfall svo forgangurinn haldi undir tímapressu í stað þess að veðrast.

2. **Hverjar af nýlegum ákvörðunum þínum voru einstefnuhurðir og fengu þær meiri rýni en tvístefnuhurðirnar?** Áhættudrifin hönnun segir að eyða hönnunarfyrirhöfn í hlutfalli við hve erfitt er að snúa ákvörðun við, samt rýna flest teymi hverja breytingu með nokkurn veginn sama helgisið. Það sóar athygli á ódýr, afturkræf val á meðan óafturkræf (gagnalíkan bakað inn í lagaleg skrá, opinber API-samningur, kjarnagagnageymsla) læðast í gegn með of litla áskorun. Dragðu mikilvægar ákvarðanir síðasta ársfjórðungs og flokkaðu þær eftir afturkræfni, spurðu síðan hvort óafturkræfu hafi fengið frumgerðir, tilraunir eða formlega rýni. Í langlífum fyrirtækja- og opinberum kerfum safnast kostnaður rangrar einstefnuhurðar upp í áratug, svo aukin nákvæmni borgar sig margfalt. Láttu vægi ferlisins samsvara afturkræfni ákvörðunarinnar, ekki stærð breytingarinnar.

3. **Fyrir næstu áhættusömu, erfiðu-að-snúa-við ákvörðun þína, hver þarf að vera í herberginu og gegn hvaða sviðsmyndum muntu stiga valkostina?** Skipulögð málamiðlanarýni í ATAM-stíl vinnur sér inn kostnað sinn þegar ákvörðun er óafturkræf og snertir nokkra gæðaeiginleika í einu, og kraftur hennar kemur frá viðstöddum: afhendingu, öryggi, rekstri og stefnu- eða viðskiptaeigendum sem finna afleiðingarnar. Slepptu einni þessara radda og þú uppgötvar átökin eftir smíði, eins og skyndiminnisval getur hljóðlega brotið úttektarhæfniskröfu. Komdu með forgangsröðuðu gæðaeiginleikasviðsmyndirnar sem stigunarviðmið og leitaðu næmispunkta þar sem einn valkostur sveiflar einum eiginleika harkalega og málamiðlunarpunkta þar sem hann hreyfir nokkra. Útkoman sem þú vilt er stutt ADR sem skráir valkostina sem þú hafnaðir og hvers vegna, svo rökin lifi þá sem tóku ákvörðunina. Ef engin væntanleg ákvörðun virðist réttlæta þetta er það sjálft vert að athuga, því stór áætlun án óafturkræfra ákvarðana á sjóndeildarhringnum horfir venjulega ekki nógu langt fram.

4. **Ef nýliði eða utanaðkomandi endurskoðandi hefði aðeins skrifaðan arkitektúr þinn, gæti hann endurbyggt hvers vegna kerfið er í laginu sem það er og hvenær prófaðirðu það síðast?** Arkitektúr sem býr í fáum höfðum eldri sérfræðinga er einn bilunarpunktur: þegar þeir halda áfram fer röksemdafærslan að baki hverri erfiðri ákvörðun með þeim og næsta teymi lærir hana aftur gegnum atvik. Fyrir stóra skipulagsheild er læsileiki arkitektúrsins (C4-teikningar sem passa við raunveruleikann, arc42-frásögn, ADR sem skrá hafnaða valkosti) það sem lætur tugi teyma rökræða um sama kerfi án fundar. Komdu með nýlega ADR og núverandi teikningu, réttu einhverjum sem smíðaði ekki íhlutinn og horfðu hve langt hann kemst áður en hann þarf að spyrja manneskju. Í fyrirtækja- og opinberu umhverfi mun endurskoðandi gera nákvæmlega þessa æfingu, og skjölun sem lýsir kerfi síðasta árs er verri en engin því hún leiðir einmitt fólkið afvega sem verður að votta. Líttu á ferskleika skriflegu skrárinnar sem mælanlegan eiginleika og settu hæfnisfall eða rýnitakt að baki því að halda henni sannri.

5. **Hverjir af arkitektúreiginleikum þínum eru varðir af sjálfvirku hæfnisfalli í dag og hverjir reiða sig enn á að allir muni regluna?** Ásetningur sem lifir aðeins á wiki-síðu eða í minni rýnis veðrast þegar tímamörk koma, því lagskiptingarreglan, mörkin um engan sameiginlegan gagnagrunn og tafarfjárhagsáætlunin eru einmitt það sem teymi skera þegar þau eru undir þrýstingi. Í stórum, ört breytilegum kóðagrunni er eini ásetningurinn sem lifir sá sem smíði framfylgir, svo bilið milli eiginleikanna sem þú fullyrðir og þeirra sem þú athugar í raun er raunveruleg arkitektúráhætta þín. Skráðu mikilvægu eiginleika þína, merktu hvern sem framfylgdan, handvirkt rýndan eða óvarinn og komdu með síðustu þrjú skiptin sem rýni greip rek sem hæfnisfall hefði getað gripið fyrr. Í eftirlitsskyldum og opinberum kerfum skiptir þetta tvöfalt, því eftirlitsaðili spyr ekki hvort þú ætlaðir gagnabúsetu eða úttektarhæfni heldur hvernig þú sannar að hún hélt samfellt, og græn leiðsla er mun sterkara svar en stefnuskjal. Forgangsraðaðu að sjálfvirknivæða eiginleikana sem bilun í er bæði líkleg og dýr og sættu þig við að sumir verði handvirkir.

6. **Þegar þú ákveður hvort krafa sé arkitektúrlega marktæk, hver tekur þá ákvörðun og hvernig heldurðu ASR-listanum frá því að verða annaðhvort allt eða ekkert?** Gildi þess að nefna arkitektúrlega marktækar kröfur kemur frá sértækni: líttu á hverja kröfu sem marktæka og hönnun stöðvast, líttu á enga sem marktæka og byggingarlegu, áhættusömu, erfiðu-að-breyta kröfurnar læðast í gegn óvarðar. Í stóru teymi er freistingin að láta hvert teymi ákveða staðbundið, sem framleiðir ósamræmd viðmið og þverteymisóvæntar uppákomur þegar „minniháttar“ val eins hóps takmarkar uppbyggingu annars. Komdu með núverandi ASR-lista þinn, viðmiðin sem þú notaðir (snertir marga íhluti, dýr í uppfyllingu, strangt skilyrði, tæknilega áhættusöm) og nokkrar jaðarkröfur til að prófa mörkin upphátt. Fyrir fyrirtæki og hið opinbera eru reglugerðarkröfur eins og gagnabúseta, varðveisla og úttektarhæfni nánast alltaf marktækar og óumsemjanlegar, svo nefndu hver á listann, hvernig hann er rýndur og hvernig ákvörðun um að bæta við ASR eða fella eina niður er skráð, því ASR sem enginn stýrir er krafa sem enginn mun verja undir athugun.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Haltu helgisiðnum nálægt núlli og skránni nálægt fullkominni. Slepptu formlegum ATAM-vinnustofum og þungum sniðmátum, en skrifaðu samt tylft stuttra ADR fyrir valin sem væri sársaukafullt að afturkalla (gagnageymslu, einlitt kerfi á móti þjónustum, auðkenningarveitu) og festu tvær eða þrjár gæðaeiginleikasviðsmyndir sem fyrstu viðskiptavinir þínir finna í raun. Verkfræðiathygli er af skornum skammti, svo verndaðu aðeins eiginleikana sem bilun í myndi sökkva þér, eins og einangrun leigjenda, og láttu allt annað vera sprottið og ódýrt að breyta.

**Lítið fyrirtæki.** Án sérstaks arkitekts og með þröngt fjárhagsáætlun skaltu hallast að grunnatriðunum sem kosta nánast ekkert: nefndu handfylli gæðaeiginleika sem áþreifanlegar tölur, skrifaðu ADR fyrir allt sem þú ættir erfitt með að afturkalla og láttu valinn vettvang eða söluaðila bera þungu byggingarákvarðanirnar. Kjóstu að kaupa vel studdan stakk frekar en að smíða sérsmíðaða innviði og líttu á skjalfestan arkitektúr söluaðilans sem skorðu sem þú erfir frekar en eina sem þú þarft að semja frá grunni.

**Stórfyrirtæki.** Áskorunin er samfella yfir mörg teymi og ára vegvísi, svo fjárfestu í sameiginlegum búnaði: arkitektúrfélagi, sameiginlegu safni gæðaeiginleikasviðsmynda, ADR geymdar við hlið kóðans og hæfnisföllum í CI sem framfylgja mörkum sem enginn einn rýnir gæti gætt í stórum stíl. Notaðu skipulagða málamiðlanagreiningu fyrir óafturkræfar, þverlægar ákvarðanir, haltu C4-teikningum sem sameiginlegu korti í hönnunarrýni og stýrðu ASR-listanum miðlægt svo hópar hætti að taka staðbundið skynsamleg val sem rekast á á heimsvísu.

**Hið opinbera.** Langlíf, eftirlitsskyld kerfi gera skjalfestan, rökstuddan arkitektúr að innkaupa- og ábyrgðarkröfu, ekki sparisiðum. Líttu á gagnabúsetu, varðveislu, úttektarhæfni og notkunaraðgengi sem arkitektúrlega marktækar kröfur skrifaðar í arc42-lýsingu sem endurskoðendur geta lesið beint, og keyrðu léttar málamiðlanavinnustofur sem fela í sér stefnu- og öryggisfulltrúa svo árekstrar (eins og skyndiminni gegn úttektarhæfni) birtist á pappír fyrir kóða. Haltu röksemdaslóðinni nógu fullkominni til að ábyrgur embættismaður geti sýnt tilhlýðilega kostgæfni og kjóstu arkitektúra með skýrum útgönguleiðum fram yfir þá sem læsa opinberan aðila við einn söluaðila í áratug.

## Dæmi

**Sprotafyrirtæki.** Sex manna SaaS-teymi á frumstigi heldur arkitektúr sínum í sameiginlegu skjali frekar en formlegu ferli, en skrifar samt niður ákvarðanirnar sem væri sársaukafullt að afturkalla. Þau skrá um tylft ADR (hvers vegna Postgres fram yfir skjalageymslu, hvers vegna einingaskipt einlitt kerfi fram yfir þjónustur, hvers vegna þau völdu auðkenningarveituna sína) og festa tvær gæðaeiginleikasviðsmyndir sem skipta fyrstu viðskiptavini raunverulega máli: „nýskráning lýkur á innan við tveimur sekúndum“ og „enginn viðskiptavinur getur nokkurn tíma lesið gögn annars leigjanda“. Þegar þau ráða sjöunda og áttunda verkfræðinginn láta þessar athugasemdir nýliðana afhenda á fyrstu vikunni í stað þess að trufla alla til að spyrja hvers vegna hlutir eru eins og þeir eru.

**Stórfyrirtæki.** Fjölþjóðlegur banki sameinar tólf svæðisbundin greiðslukerfi og setur því upp lítið arkitektúrfélag. Félagið skilgreinir átta gæðaeiginleikasviðsmyndir (þar á meðal „vinna 10.000 færslur á sekúndu án nokkurrar týndrar færslu“ og „endurheimta svæði innan 15 mínútna“), safnar um fjörutíu ADR og framfylgir hæfnisföllum í CI ([samfelld samþætting](https://en.wikipedia.org/wiki/Continuous_integration)): engin þjónusta má skrifa í gagnagrunn annars léns, öll kall milli þjónusta verða að vera rakin og hvert ósjálfstæði með alvarlegan [CVE](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) (Common Vulnerabilities and Exposures) fellir smíðina. C4-samhengis- og ílátsteikningarnar verða sameiginlega kortið í hverri hönnunarrýni og þverteymisdeilur um samþættingu minnka verulega.

**Hið opinbera.** Landsbundin stofnun nútímavæðir bótavettvang, og lög krefjast þess að hún tryggi gagnabúsetu, sjö ára úttektarhæfni og samræmi við notkunaraðgengi. Arkitektar hennar líta á þetta sem ASR og skrifa í arc42-lýsingu sem endurskoðendur rýna beint. Þeir keyra létta ATAM-vinnustofu með afhendingarteymum, öryggi og stefnufulltrúum til að bera saman tvo tilvonandi arkitektúra og uppgötva að skyndiminnisstefna æskilegri hönnunar rekst á úttektarhæfniskröfuna. Að grípa þá málamiðlun á pappír, fyrir eina línu af kóða, sparar mánuði af endurvinnu og gefur ábyrga ráðherranum skjalfest sönnunargögn um tilhlýðilega kostgæfni.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun grunnatriða arkitektúrs er aðallega forðaður kostnaður, sem gerir hana auðvelda að fjársvelta og dýra að sleppa. Kostnaðurinn við upptöku er hóflegur: tími nokkurra reyndra arkitekta, fáeinar vinnustofur, skjölunarsniðmát og nokkur CI-fjárfesting í hæfnisföllum, venjulega lítið eins stafs hlutfall af fjárhagsáætlun áætlunar. Kostnaðurinn við að taka þau *ekki* upp kemur síðar og á álagi: endurvinna þegar ótilgreindur gæðaeiginleiki bilar í framleiðslu, neyðarendurvettvangsvæðing þegar óskjalfest tenging hindrar lögboðna breytingu, langdregin atvik því enginn skilur kerfið og fallnar úttektir sem stöðva afhendingu eða kalla fram sektir.

Fyrir forystu skaltu ramma rökin um valkvæði og áhættu. Góð grunnatriði arkitektúrs lækka kostnað framtíðarbreytinga (bein vogarstöng á afhendingarhraða og heildareignarkostnað yfir áratugalangan kerfislíftíma), draga úr því hve oft og hve lengi alvarleg atvik standa og framleiða skjölunarslóðina sem eftirlitsaðilar og endurskoðendur krefjast nú. ADR-venjan ein borgar sig fyrsta skiptið sem ný forysta spyr „hvers vegna smíðuðum við þetta svona?“ og fær svar á mínútum í stað réttarrannsóknar. Settu tölur á það þar sem þú getur: vegðu kostnað einnar stórrar endurhönnunar sem forðað var, eða einnar fallinnar úttektar sem forðað var, gegn litla áframhaldandi kostnaði vinnubragðanna.

## Andmynstur og gildrur

- **Fílabeinsturnsarkitektúr.** Arkitektar sem framleiða teikningar en snerta aldrei kóða eða tala við afhendingarteymi. Hönnun þeirra er hunsuð eða ósmíðanleg.
- **Gæðaeiginleikar sem lýsingarorð.** „Stigvaxandi, öruggt, áreiðanlegt“ án talna, án sviðsmynda og þar með engin leið til að sannreyna eða semja um málamiðlun.
- **Stór fyrirframhönnun.** Að skuldbinda hvert smáatriði áður en fyrsta lína kóða er skrifuð og læsa ákvarðanir þegar skilningur er veikastur.
- **Skjölun sem lýgur.** Teikningar sem lýsa kerfi síðasta árs. Verra en engar því þær leiða afvega.
- **Ferilskrárdrifin hönnun.** Að velja tækni til að byggja starfsferla frekar en til að uppfylla ASR.
- **Gullhúðun.** Að verkfræða fyrir stigvöxt, sveigjanleika eða almennleika sem kröfurnar báðu aldrei um, sem bætir við kostnaði og flækju til frambúðar.
- **Engin arkitektúrhandrið.** Að treysta á góðan ásetning frekar en hæfnisföll til að varðveita uppbyggingu yfir stórt teymi.

## Þroskalíkan

- **Stig 1: Upphaf.** Arkitektúr er óbeinn og lifir í höfðum einstaklinga. Engir skjalfestir gæðaeiginleikar, engar ADR, engar sameiginlegar teikningar. Uppbygging uppgötvast í atvikum og hvert þverteymisósjálfstæði er samið upp á nýtt frá grunni.
- **Stig 2: Þróun.** Sum teymi skrifa niður ákvarðanirnar sem væri sárt að afturkalla og skissa lykilteikningar, en venjan er ósamræmd: eitt teymi heldur ADR á meðan annað heldur engar, gæðaeiginleikar eru nefndir sem lýsingarorð frekar en mælanlegar sviðsmyndir og skjölun rekur úr takti milli verkefna.
- **Stig 3: Stöðlun.** Gæðaeiginleikasviðsmyndir og arkitektúrlega marktækar kröfur eru tilgreindar og forgangsraðaðar samkvæmt skjalfestum staðli fyrir alla skipulagsheildina. ADR eru rútína og geymdar við hlið kóðans, C4- og arc42-skjölun er viðhaldið samkvæmt sameiginlegu sniðmáti og skipulagðar málamiðlanarýni eru kröfur fyrir mikilvægar ákvarðanir í hverju teymi.
- **Stig 4: Stjórnun.** Arkitektúrinn er mældur gegn grunnlínum en ekki fullyrtur. Hæfnisföll í CI skila skýrslu um eiginleika eins og p99 töf, lagskiptingarbrot, órakin kall og berskjölduð ósjálfstæði. ADR-þekja og ferskleiki skjölunar eru rakin sem mælikvarðar. Málamiðlanarýni stiga valkosti gegn forgangsröðuðu sviðsmyndunum og rek gegn umsömdum grunnlínum kallar fram skilgreind viðbrögð í stað óvæntrar uppákomu. Endurskoðendur geta reitt sig á mæld sönnunargögn en ekki frásögn eina.
- **Stig 5: Samhæfing.** Arkitektúr þróast stöðugt og aðlögunarhæft yfir alla skipulagsheildina. Hæfnisfalla- og atvikagögn næra aftur hvaða eiginleikar skipta máli og hvert hönnunarfyrirhöfn fer. ASR-listar, gæðaeiginleikaforgangur og handrið eru endurmörkuð þegar kröfur og áhætta breytast og venjan er samþætt afhendingu, öryggi og áhættuáætlun svo vettvangurinn aðlagist nýjum kröfum í stað þess að vera endurbyggður frá grunni.

## Hugmyndir til umræðu

1. Hverjir þrír gæðaeiginleikar eru raunverulega óumsemjanlegir fyrir mikilvægasta kerfið þitt og geturðu sett hvern fram sem mælanlega sviðsmynd í dag?
2. Hvernig ákveðurðu hvenær ákvörðun er „arkitektúrlega marktæk“ nóg til að réttlæta ADR frekar en að bara gera hana?
3. Hvar myndu hæfnisföll grípa rek sem núverandi kóðarýni þín missir af?
4. Ofhannar skipulagsheildin þín eða vanhannar og hvaða sönnunargögn segja þér hvort?
5. Hver ber ábyrgð á arkitektúr í teymi-teyma uppbyggingu og hvernig forðastu bæði fílabeinsturna og algjört stjórnleysi?
6. Hvernig myndi utanaðkomandi endurskoðandi endurbyggja ásetning arkitektúrs þíns út frá því sem er skrifað niður í dag?

## Helstu atriði

- Arkitektúr er safn ákvarðana sem er dýrt að snúa við. Taktu þessar málamiðlanir af ásetningi og skráðu þær.
- Tilgreindu gæðaeiginleika sem mælanlegar sviðsmyndir og auðkenndu arkitektúrlega marktæku kröfurnar sem móta uppbyggingu.
- Hannaðu stigvaxandi og verndaðu lykilarkitektúreiginleika með sjálfvirkum hæfnisföllum.
- Skjalfestu létt en sannleikanum samkvæmt með C4-teikningum, arc42-frásögn og ADR á hverja ákvörðun geymdar við hlið kóðans.
- Láttu nákvæmni samsvara áhættu: þunga greiningu fyrir óafturkræfar, áhrifamiklar ákvarðanir og létt ferli alls staðar annars staðar.
- Viðskiptarökin eru forðuð endurvinna, styttri atvik, hraðari framtíðarbreytingar og úttektarreiðubúin sönnunargögn.

## Heimildir og frekari lestur

- Len Bass, Paul Clements, and Rick Kazman, *Software Architecture in Practice*
- Neal Ford, Rebecca Parsons, and Patrick Kua, *Building Evolutionary Architectures*
- Simon Brown, *Software Architecture for Developers* (and the C4 model)
- Mark Richards and Neal Ford, *Fundamentals of Software Architecture*
- George Fairbanks, *Just Enough Software Architecture: A Risk-Driven Approach*
- Michael Nygard, "Documenting Architecture Decisions" (the ADR pattern)
- Gernot Starke and Peter Hruschka, *arc42* documentation template
- Paul Clements et al., *Evaluating Software Architectures: Methods and Case Studies* (ATAM)
- ISO/IEC 25010, *Systems and software quality models*
