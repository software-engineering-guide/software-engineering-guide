# 3.15 Skyndiminni og efnisdreifing

## Yfirlit og tilgangur

[Skyndiminni](https://en.wikipedia.org/wiki/Cache_(computing)) (cache) er afrit af gögnum geymt einhvers staðar hraðar eða nær en frumritið, svo þú getir svarað beiðni án þess að vinna alla dýru vinnuna aftur. Nánast hvert kerfi sem finnst hratt er hratt vegna skyndiminnis. Gagnagrunnsfyrirspurnin sem tæki 40 millisekúndur skilar á innan við einni þegar niðurstaða hennar situr þegar í minni. Myndin sem færi yfir haf er afgreidd af vél í sömu borg. Skyndiminni er aflmesta afkastatæknin sem þú hefur, og líka sú sem líklegust er til að færa þér lúmskan, óþolandi galla.

Þessi kafli fer djúpt í skyndiminnisstefnu. Kafli 3.4 (gagnaarkitektúr og geymsla) kynnir skyndiminni og efnisdreifinet sem eitt geymsluáhyggjuefni meðal margra og kafli 3.13 (netkerfi og tengingar) fjallar um netslóðina sem þau ferðast á. Hér færðu ákvarðanirnar: hvar á að setja skyndiminni, hvernig á að lykla það, hvenær á að ógilda það, hvernig á að verja það undir álagi og hvernig á að rökræða um úreldinguna sem þú skiptir fyrir hraða. Skyndiminni snertir afkastaverkfræði (kafli 2.16), stigvöxt og seiglu (kafli 3.5), hlutabilunarveruleika dreifðra kerfa (kafli 3.3) og, því eitrað skyndiminni getur afgreitt árás til þúsunda notenda, forritaöryggi (kafli 4.2).

Hvatinn kemur niður á þremur vogarstöngum. Skyndiminni sker töf, svo notendur bíða minna. Það sker álag, svo upptök þín afgreiða meiri umferð á sama vélbúnaði. Og það sker kostnað, því beiðni sem er svarað á jaðrinum snertir aldrei gagnagrunninn þinn, reikniaflið eða útleiðarreikninginn. Fyrir stór teymi er sameiginleg skyndiminnisstefna munurinn á vettvangi sem stigvaxar fyrirsjáanlega og vettvangi þar sem hver þjónusta finnur upp ógildingu að nýju og fær hana ranga. Í kerfum fyrirtækja og hins opinbera, þar sem umferð rýkur upp á skilafrestum og opnunardögum, er vel hannað skyndiminni oft það sem stendur milli virkrar gáttar og opinberrar bilunar.

## Meginreglur

- Notaðu skyndiminni til að skera töf, álag og kostnað, og vittu hvert þeirra þú ert að kaupa.
- Settu skyndiminni á rétt lag stigveldisins, næst þar sem það hjálpar mest.
- Líttu á ógildingu sem erfiða hlutann. Hannaðu lykla og líftíma áður en þú geymir í skyndiminni.
- Verðu skyndiminnið undir álagi með samruna, skjálfta og stormvörnum.
- Veldu skrifmynstur af ásetningi: samræmi og hraði toga hvort gegn öðru.
- Mældu hitahlutfall, úreldingu og upptakaálag. Ómælt skyndiminni er skuld.
- Líttu á skyndiminnisgeymt efni sem árásaryfirborð. Eitrað skyndiminni afgreiðir alla.

## Ráðleggingar

### Skildu skyndiminnisstigveldið

Skyndiminni er ekki eitt í einum stað. Það er stigveldi afrita, hvert nær notandanum en það síðasta, og þú hannar yfir allt. Næst notandanum er biðlaraskyndiminnið: HTTP-skyndiminni vafrans, staðbundin geymsla farsímaforrits, skyndiminni í minni ferlis. Næst er [efnisdreifinetið](https://en.wikipedia.org/wiki/Content_delivery_network) (CDN), floti þjóna dreifður um heiminn sem halda afritum af efni þínu á netjaðrinum, nálægt notendum. Á bak við það situr öfugi milliþjónninn eða gáttarskyndiminnið, sameiginlegt skyndiminni fyrir framan þjóna þína. Síðan forritaskyndiminnið: hraður lykil-gildis geymsla eins og gagnanet í minni sem heldur útreiknuðum niðurstöðum, setum og birtum brotum. Að lokum eigið fyrirspurnar- og biðminnisskyndiminni gagnagrunnsins, sem heldur heitum síðum í minni svo diskurinn sé snertur sjaldnar.

Hvert lag þjónar sérstöku verki: biðlaraskyndiminnið útrýmir beiðninni alveg, CDN gleypir hnattræna lesumferð, öfugi milliþjónninn ver upptökin fyrir endurtekinni eins vinnu, forritaskyndiminnið sparar endurútreikning og gagnagrunnsskyndiminnið heldur geymslunni viðbragðsgóðri. Beiðni sem missir af hverju lagi og nær gagnagrunninum er hægasta, dýrasta leiðin sem þú átt, svo tilgangur stigveldisins er að svara eins langt upp og út og þú getur örugglega. Hannaðu það sem kerfi, því skyndiminnisgeymt brot á forritalaginu og úrelt CDN-afrit fyrir ofan það geta verið ósammála á vegu sem rugla notendur.

### Líttu á ógildingu sem erfiða vandamálið

Til er gamall brandari um að tvö erfiðustu vandamál tölvunarfræði séu að nefna hluti, [skyndiminnisógilding](https://en.wikipedia.org/wiki/Cache_invalidation) og skekkjur um einn. Brandarinn endist því ógilding er í raun erfið: skyndiminni er afrit, og um leið og frumritið breytist er hvert afrit hugsanleg lygi. Þú hefur þrjár víðar aðferðir. Tímabundin fyrning með lífstíma (TTL), tímalengdinni sem færsla helst gild áður en hún telst úrelt, er einföldust: þú sættir þig við afmarkaða úreldingu og lætur færslur eldast út. Skýr ógilding hreinsar eða uppfærir færslur þegar undirliggjandi gögn breytast, sem er nákvæmt en krefst þess að þú vitir hvern stað þar sem afrit býr. Atburðadrifin ógilding gerir skyndiminni áskrifendur að breytingaatburðum svo þau endurnýi sig sjálf, sem stigvaxar betur yfir mörg skyndiminni en bætir við skilaboðaháð.

Flest raunveruleg kerfi blanda þessu: stutt TTL fyrir gögn sem breytast oft og þola sekúndur af úreldingu, lengri TTL auk skýrrar hreinsunar fyrir gögn sem breytast sjaldan en verða að vera rétt þegar þau gera það, og útgáfumerkta skyndiminnislykla fyrir efni sem er óbreytanlegt eftir útgáfu. Útgáfulykilbragðið er vert að tileinka sér: í stað þess að ógilda breytirðu lyklinum. Stílblað afgreitt sem `app.v187.css` þarf aldrei að hreinsa, því ný útgáfa er nýr lykill og gamli hættir einfaldlega að vera beðinn um. Hvenær sem þú getur breytt ógildingarvanda í nafngiftarvanda skaltu gera það.

### Hannaðu skyndiminnislykla og TTL af ásetningi

Skyndiminni er aðeins jafn gott og lykill þess. [Skyndiminnislykillinn](https://en.wikipedia.org/wiki/Cache_(computing)) er auðkennið sem gildi er geymt undir og flett upp, og að fá hann rangan veldur tveimur andstæðum bilunum. Of grófur, og þú afgreiðir gögn eins notanda til annars: sérsniðin síða geymd í skyndiminni undir vefslóð sem hunsar notandaauðkenni er gagnaleki. Of fínn, og hitahlutfall þitt hrynur því engar tvær beiðnir deila lykli. Ákveddu af ásetningi hvað á heima í lyklinum: auðkenni tilfangsins auk þess sem lögmætt breytir svarinu (tungumál, gjaldmiðill, tækjaflokkur) og ekkert sem gerir það ekki. Normaðu lykla svo léttvægur munur eins og röð fyrirspurnarbreyta sundri ekki skyndiminninu.

TTL verðskulda sömu hugsun. TTL er loforð um hámarksúreldingu sem þú munt afgreiða, svo stilltu það út frá raunverulegu umburðarlyndi gagnanna, ekki kringlóttri tölu sem einhver giskaði á: hlutabréfaskjár þolir sekúndur, vörulisti mínútur, útgefin reglugerð klukkustundir eða útgáfumerktur lykill og engin fyrning yfirleitt. Bættu við lítilli slembidreifingu, kallaðri skjálfti, svo hópur færslna skrifaður saman renni ekki allur út á sama augnabliki og æði á upptökin. Skrifaðu þessi val niður, því TTL án rökstuðnings er tala sem næsti verkfræðingur mun óttast að breyta.

### Verðu gegn stormum og sameinaðu beiðnir

Þegar vinsæl skyndiminnisfærsla rennur út missa allar beiðnir sem vildu hana af henni í einu og æða saman á upptökin. Þetta er [skyndiminnisstormurinn](https://en.wikipedia.org/wiki/Cache_stampede), einnig kallaður hjarðhlaup, og hann getur fellt einmitt gagnagrunninn sem skyndiminnið átti að verja. Smíðaðu varnirnar einu sinni og endurnýttu þær alls staðar. Beiðnasamruni (single-flight) lætur aðeins fyrstu beiðni um vantandi lykil endurreikna gildið meðan hinar bíða eftir niðurstöðu hennar, svo þúsund samtímis missir valda einu upptakakalli. Líkindabundinn snemmbúinn endurútreikningur endurnýjar heita færslu af handahófi lítillega áður en hún rennur út, svo ein bakgrunnsbeiðni endurnýi hana áður en hópurinn sér misst. Stale-while-revalidate stefna afgreiðir örlítið úrelt afritið strax og endurnýjar það ósamstillt, svo notendur bíða aldrei eftir missi.

Þessi mynstur skipta mestu máli einmitt þegar þú þarft skyndiminnið mest, undir háannaálagi, svo staðfestu þau í raunhæfum stærðum: vörn sem virkar með tíu notendum getur samt brugðist við tíu þúsund. Parið þau við seigluminstrin úr kafla 3.5, sérstaklega tímamörk og rofa, svo þegar upptökin eru raunverulega hæg verji skyndiminnislagið þau í stað þess að hrúga ofan á. Markmiðið er skyndiminni sem hegðar sér best undir þrýstingi, ekki eitt sem magnar topp í rekstrarrof.

### Veldu skrifmynstur af ásetningi

Hvernig þú meðhöndlar skrif ræður hve ferskt skyndiminnið þitt helst og hve miklu þú teflir í hættu við bilun. Fjögur algeng mynstur eru til. Í [cache-aside](https://en.wikipedia.org/wiki/Cache_(computing)) (löt hleðsla) athugar forritið skyndiminnið, og við missi les það upptökin, fyllir skyndiminnið og skilar gildinu. Skrif fara á upptökin og ógilda færsluna. Það er sjálfgefið af góðri ástæðu: einfalt, og skyndiminnið heldur aðeins því sem beðið er um. Í write-through fer hvert skrif í skyndiminni og upptök saman, svo skyndiminnið er alltaf núgildandi, á kostnað skriftafar og að geyma gögn sem gætu aldrei verið lesin. Í write-back (write-behind) fara skrif fyrst í skyndiminnið og skolast til upptakanna ósamstillt, sem gerir skrif hröð en teflir í hættu tapi ef skyndiminnið deyr fyrir skolun. Í write-around fara skrif beint á upptökin og sleppa skyndiminninu, sem forðast hræringu frá skrifþungum gögnum sem sjaldan eru lesin, á kostnað tryggðs fyrsta lestrarmissis.

Veldu fyrir hvert vinnuálag, ekki einu sinni fyrir allt kerfið. Lesþungur vörulisti hentar cache-aside eða write-through. Skrifþung skrá eða mælikvarðastraumur hentar write-around, svo skyndiminnið sé ekki hrært af gögnum sem enginn les aftur. Write-back hentar skrifum með miklu gegnumstreymi þar sem lítil, skilin hætta á tapi er ásættanleg og ending er séð um annars staðar. Tilgreindu mynstrið fyrir hvert skyndiminni skýrt, því lesandi sem gerir ráð fyrir cache-aside þegar kóðinn gerir write-back mun misdæma bæði ferskleika og bilunarhegðun.

### Láttu brottrekstrarstefnu samsvara aðgangsmynstri þínu

Skyndiminni hefur fasta stærð, svo þegar það fyllist verður eitthvað að fara. Brottrekstrarstefnan ræður hvað. [Síðast notað fyrir lengst](https://en.wikipedia.org/wiki/Cache_replacement_policies) (LRU) rekur út færsluna sem hefur verið ósnert lengst, veðjar á að nýleg notkun spái fyrir um framtíðarnotkun, og er skynsamleg sjálfgefin stefna. Sjaldnast notað (LFU) rekur út færsluna með fæstar heimsóknir, sem hentar stöðugum heitum mengjum þar sem fáir hlutir eru eilíflega vinsælir en getur loðað við færslur sem voru eitt sinn heitar og aðlagast aldrei. Afbrigði eins og hluta-LRU og aðlögunarstefnur blanda nýleika og tíðni. Fyrstur-inn-fyrstur-út og einföld tímabundin fyrning eru ódýrari en bitlausari.

Láttu stefnuna samsvara því hvernig gögn þín eru sótt: LFU eða tíðnimeðvituð stefna fyrir lítið heitt mengi sem sjaldan breytist, LRU þar sem vinsældir hreyfast með tímanum eins og með fréttir eða vinsælt efni. Hvað sem þú velur skaltu stærðarákvarða skyndiminnið svo heita mengið komist fyrir, því skyndiminni of lítið til að halda vinnumenginu slær, rekur færslur út rétt áður en þeirra er aftur þörf. Fylgstu með brottrekstrarhlutfalli sem fyrsta flokks mælikvarða, þar sem skyndileg hækkun þýðir yfirleitt að skyndiminnið er of lítið eða lyklasprenging sundri því.

### Notaðu HTTP-skyndiminnismerkingu rétt

Vefurinn hefur þroskað, staðlað skyndiminnislíkan innbyggt í [HTTP](https://en.wikipedia.org/wiki/HTTP), og að nota það vel gefur þér biðlara- og CDN-skyndiminni ókeypis. `Cache-Control` hausinn er stýriflöturinn: `max-age` setur ferskleikalífstímann, `public` og `private` segja hvort sameiginleg skyndiminni megi geyma svarið, `no-store` bannar skyndiminnisgeymslu og `stale-while-revalidate` leyfir að afgreiða úrelt afrit meðan það er endurnýjað. Staðfesting leyfir skyndiminni að athuga ferskleika ódýrt án þess að sækja meginmálið aftur. [ETag](https://en.wikipedia.org/wiki/HTTP_ETag) (entity tag) er ógegnsætt útgáfuauðkenni sem þjónninn festir við svar. Biðlarinn sendir það til baka í `If-None-Match` haus og þjónninn svarar `304 Not Modified` án meginmáls ef ekkert breyttist. `Last-Modified` með `If-Modified-Since` gerir það sama með tímastimplum.

Hagnýti agi er að vera skýr. Settu `Cache-Control` á hvert svar frekar en að láta skyndiminni giska með ágiskunum. Merktu einkasvör á hvern notanda `private` eða `no-store` svo sameiginlegur milliþjónn geymi þau aldrei, algeng og hættuleg mistök. Notaðu útgáfumerktar vefslóðir með löngu max-age og `immutable` tilskipuninni fyrir kyrrstæðar eignir, og staðfestingu með ETag fyrir efni sem breytist ófyrirsjáanlega. Að fá þessa hausa rétta breytir öllu biðlara- og CDN-laginu í rétt, staðlabyggt skyndiminni sem þú þurftir ekki að smíða.

### Ýttu vinnu út á jaðarinn með CDN og jaðartölvun

CDN byrjaði sem leið til að geyma kyrrstæðar skrár nálægt notendum og gerir það enn frábærlega: myndir, skriftur, myndband og niðurhal afgreitt frá jaðarstað millisekúndum í burtu í stað fjarlægra upptaka. Nútíma CDN fara lengra. Þau geyma kvikt og sérsniðið efni með fínkornuðum lyklum, ljúka TLS á jaðrinum, gleypa umferðartoppa og dreifðar álagsárásir og keyra í auknum mæli kóðann þinn. [Jaðartölvun](https://en.wikipedia.org/wiki/Edge_computing) (edge computing) keyrir rökfræði á jaðarstöðunum sjálfum, svo þú getir sérsniðið svar, athugað heimild eða sett saman síðubrot án umferðarlotu til miðlægs svæðis.

Hallaðu þér að þessu fyrir lestrana sem ráða mestum hluta flestra kerfa. Settu kyrrstæðar eignir á bak við CDN með langlífum, útgáfumerktum vefslóðum, geymdu API-svör á jaðrinum þar sem ferskleiki leyfir (lyklað varlega svo sérsníðing leki ekki) og notaðu jaðartölvun fyrir tafarviðkvæma, létta rökfræði nálægt notendum. Skiptin eru ná á móti stjórn: jaðarinn er hraður og nálægur en fjarri gögnum þínum og erfiðari að villuleita, svo haltu öllu sem krefst sterks samræmis eða ferskrar valdbærar stöðu á upptökunum og láttu jaðarinn meðhöndla hina gríðarlegu, skyndiminnishæfu lesumferð.

### Líttu á skyndiminnið sem árásaryfirborð

Skyndiminni afgreiðir sama geymda svarið til margra notenda, sem gerir það að skotmarki. [Skyndiminniseitrun](https://en.wikipedia.org/wiki/Cache_poisoning) (cache poisoning) er árás þar sem beiðni er smíðuð svo skyndiminnið geymi skaðlegt eða árásaraðilastýrt svar og afgreiði það síðan til allra sem á eftir koma. Hún nýtir yfirleitt ólyklað inntak: haus sem forritið speglar inn í svarið en skyndiminnið hunsar þegar það býr til lykilinn. Skyld vefskyndiminnisblekking (web cache deception) blekkir skyndiminni til að geyma einkasvar fórnarlambs undir opinberri vefslóð. Hvort tveggja eru bilanir í lyklun og í að treysta inntaki, fjallað ítarlegar um í kafla 4.2.

Verðu af ásetningi. Hafðu í skyndiminnislyklinum sérhvert inntak sem getur breytt svarinu og neitaðu að spegla ólykla hausa inn í skyndiminnisgeymd meginmál. Láttu sameiginlegt skyndiminni aldrei geyma auðkennd svör á hvern notanda undir sameiginlegum lykli. Normaðu og staðfestu beiðnaslóðir og breytur áður en þú geymir. Stilltu `Vary` rétt svo skyndiminni skipti svörum eftir hausunum sem skipta raunverulega máli, eins og efniskóðun eða tungumál. Því ein eitruð færsla skaðar hvern niðurstraumsnotanda skaltu líta á skyndiminnisstillingu sem öryggisviðkvæman kóða og rýna hana sem slíka.

### Gerðu skyndiminnishegðun sýnilega

Þú getur ekki stýrt skyndiminni sem þú getur ekki séð. Aðalmælikvarðinn er hitahlutfallið: hlutfall beiðna afgreiddra úr skyndiminni frekar en upptökum. Hitahlutfall sem hljóðlega fellur úr 95 í 70 prósent getur margfaldað upptakaálag nokkrum sinnum og fer á undan rekstrarrofi, og þú munt aðeins grípa það snemma ef þú fylgist með því. Mældu hvert lag sérstaklega, þar sem heilbrigt CDN-hitahlutfall getur falið hrynjandi forritaskyndiminnishitahlutfall undir. Þetta er skyndiminnissértæka hlið sýnileikavinnubragðanna í kafla 9.2.

Raktu meira en heimsóknir: brottrekstrarhlutfall og minnisþrýsting til að grípa of lítið, töf á hverju lagi til að staðfesta að skyndiminnið sé í raun hraðara, upptökubeiðnahlutfall til að sjá hve mikið álag skyndiminnið gleypir og úreldingu (hve gamlar afgreiddar færslur eru) til að staðfesta að þú standir við ferskleikaloforð þín. Gefðu viðvörun á hlutföllin sem spá vandræðum, sérstaklega fallandi hitahlutfall eða hækkandi brottrekstrarhlutfall, svo þú fáir fregnir af skertu skyndiminni af mælaborði frekar en frá notendum. Sýnilegt skyndiminni er eign sem þú getur stillt. Ósýnilegt er falið ósjálfstæði sem bíður þess að koma þér á óvart.

## Málamiðlanir: kostir og gallar

Skyndiminni kaupir hraða og stigvöxt með gjaldmiðli ferskleika og flækju. Hvert skyndiminni er veðmál um að úrelt-en-hratt slái ferskt-en-hægt fyrir þessi tilteknu gögn, og listin er að leggja það veðmál meðvitað frekar en sjálfgefið. Taflan hér að neðan dregur saman helstu valin.

| Val | Kostir | Gallar |
|---|---|---|
| Cache-aside | Einfalt. Geymir aðeins það sem er lesið | Fyrsti lestur missir alltaf. Hætta á stuttri úreldingu eftir skrif |
| Write-through | Skyndiminni alltaf núgildandi við skrif | Hægari skrif. Geymir gögn sem gætu aldrei verið lesin |
| Write-back | Mjög hröð skrif. Gleypir hrinur | Gagnatapshætta ef skyndiminni bilar fyrir skolun |
| Write-around | Forðast hræringu skyndiminnis með skrifþungum gögnum | Tryggður missir við fyrsta lestur |
| Stutt TTL | Afmörkuð, lítil úrelding | Lægra hitahlutfall. Meira upptakaálag |
| Langt TTL / útgáfumerktir lyklar | Hátt hitahlutfall. Lágt upptakaálag | Úrelding nema ógilt. Krefst agaðra lykla |
| CDN og jaðar | Hnattræn lág töf. Gleypir toppa | Fjarri gögnum. Erfiðara að villuleita og ógilda |
| LRU-brottrekstur | Aðlagast breytilegum vinsældum | Getur rekið út stöðugt heitt mengi undir skönnunarþungu álagi |
| LFU-brottrekstur | Verndar stöðugt heitt mengi | Hægt að aðlagast. Loðir við áður heitar færslur |

Endurtekna spennan er samræmi gegn afköstum. Skyndiminni með langt TTL og hátt hitahlutfall er hratt og ódýrt og getur afgreitt úrelt gögn. Skyndiminni með stutt TTL og ágenga ógildingu er ferskt og rétt og vinnur upptökin harðar. Ekkert algilt rétt svar er til, aðeins rétt svar fyrir hvert gagnastykki, sett af raunverulegu umburðarlyndi þess gagnvart úreldingu. Önnur spennan er einfaldleiki gegn ná: forritaskyndiminni er nálægt gögnum þínum og auðvelt að rökræða um, á meðan jaðarinn er fjarri, hraður og erfiðari að ógilda. Leystu hvort tveggja með því að flokka gögn þín eftir ferskleikaþörf og lesmagni og staðsetja og stilla síðan hvern flokk af ásetningi.

## Spurningar til að ræða með teyminu

1. **Hvert er raunverulegt úreldingarumburðarlyndi hverrar tegundar gagna sem við geymum í skyndiminni og höfum við sett TTL og ógildingu út frá því umburðarlyndi frekar en af vana?** Flest teymi geyma í skyndiminni með TTL sem einhver valdi einu sinni og endurskoðaði aldrei, svo sum gögn eru afgreidd úreltari en reksturinn getur sætt sig við á meðan önnur renna svo ágengt út að skyndiminnið hjálpar varla. Komdu með tíu efstu skyndiminnisgeymdu tilföng þín og spyrðu, fyrir hvert, fólkið sem á þau gögn hve úrelt þau mega örugglega vera: sekúndur, mínútur, klukkustundir eða aldrei eftir útgáfu. Þú munt yfirleitt komast að því að svörin eru mjög ólík og að núverandi TTL þín passa ekki við þau. Útkoman sem þú vilt er stutt ferskleikaflokkun, hver flokkur varpaður á aðferð (stutt TTL, langt TTL auk hreinsunar eða útgáfumerktir óbreytanlegir lyklar), svo skyndiminnisákvarðanir fylgi af merkingu gagna í stað ágiskunar.

2. **Ef vinsælasta skyndiminnisfærsla okkar rynni út núna undir háannaumferð, hvað yrði um upptökin?** Þessi spurning afhjúpar hvort þú hefur raunverulega stormvörn eða aðeins von. Mörg kerfi ganga vel þar til heitur lykill rennur út á umferðartoppi og hver beiðni ræðst á gagnagrunninn í einu, sem breytir skyndiminninu úr skildi í gikk. Farðu áþreifanlega í gegnum slóðina fyrir annasamasta endapunkt þinn: er beiðnasamruni svo aðeins ein missir nái upptökunum, er skjálfti svo færslur renni ekki út í takt, er stale-while-revalidate stefna svo notendur bíði aldrei eftir áfyllingu? Komdu með álagsprófunarsönnunargögn, ekki innsæi, því stormvörn sem heldur við tíu notendur getur samt hrunið við tíu þúsund. Ef þú getur ekki svarað af öryggi fannstu næstu seigluinnvestingu þína.

3. **Erum við viss um að ekkert sameiginlegt skyndiminni geymi nokkurn tíma einkagögn eins notanda undir lykli sem annar notandi getur náð?** Þetta er skyndiminnismistökin sem verða öryggisatvik og fyrirsögn. Þau gerast þegar sérsniðið eða auðkennt svar er geymt undir lykli sem sleppir notandaauðkenni, eða þegar `Cache-Control` haus ætlaður til að halda svari einkamáli vantar, svo sameiginlegur milliþjónn eða CDN geymir það og afgreiðir næstu manneskju. Úttektaðu hvaða svör eru skyndiminnishæf á sameiginlegum lögum, staðfestu að hvert svar á hvern notanda sé merkt `private` eða `no-store` og staðfestu að hver skyndiminnislykill innihaldi hvert inntak sem breytir svarinu. Líttu á þetta sem öryggisrýni, því sprengjusvæðið er hver niðurstraumsnotandi, og tengdu það við vinnubrögðin í kafla 4.2.

4. **Hvaða skrifmynstur notar hvert skyndiminni okkar í raun og valdi því einhver af ásetningi?** Cache-aside, write-through, write-back og write-around gefa andstæð loforð um ferskleika og um hvað þú missir þegar skyndiminnið bilar, samt er mynstrið í flestum kóðagrunnum hvað sem fyrsti höfundur afritaði. Fyrir stórt teymi skiptir þetta máli því ein þjónusta sem gerir ráð fyrir cache-aside ferskleika á meðan önnur keyrir hljóðlega write-back getur framleitt gögn sem líta spillt út en eru bara úrelt, og bakvaktarverkfræðingurinn eyðir klukkustundum í að elta draug. Komdu með skrá yfir hvert skyndiminni: skrifmynstrið, ferskleikann sem það tryggir og hvað verður um óskolað skrif ef ferlið deyr. Þar sem eitthvert skyndiminni notar write-back skaltu koma með endingarsöguna sem styður það. Í fyrirtækja- og opinberum kerfum sem meðhöndla fjárhags- eða skráagögn er write-back skyndiminni án stuðningsábyrgðar úttektarniðurstaða sem bíður þess að gerast, svo umræðan ætti að enda með mynstur hvers skyndiminnis nefnt, rökstutt og skrifað niður.

5. **Þegar við setjum upp eða breytum gögnum, ógildir hvert viðeigandi skyndiminnislag rétt, eða treystum við á að einhver muni að hreinsa?** Ógilding er erfiði hlutinn og bilunarhátturinn er hljóður: leiðrétt gildi sem helst rangt í klukkustundir því eitt lag stigveldisins, CDN, öfugur milliþjónn eða forritaskyndiminni, fékk aldrei skilaboðin. Stór skipulagsheild margfaldar þessa áhættu, því ein rökræn breyting getur þurft að breiðast yfir mörg skyndiminni á mörgum svæðum í eigu ólíkra teyma. Komdu með áþreifanlega rekjun á einni nýlegri gagnabreytingu og fylgdu henni gegnum hvert skyndiminnislag og spyrðu við hvert: hvað kveikti á ógildingu hér og hve langan tíma tók það? Kjóstu hönnun sem breytir ógildingu í nafngift (útgáfumerktir lyklar) eða í atburði (breyting birtir hreinsun) fram yfir handvirkar keyrsluhandbækur. Í opinberum kerfum þar sem röng útgefin tala, skattprósenta eða bótafjárhæð, getur borið lagalegt vægi er ógildingarbil ekki óþægindi heldur regluvörsluútsetning, svo útkoman ætti að vera kortlögð ógildingarleið fyrir hvern flokk skyndiminnisgeymdra gagna.

6. **Lítum við á skyndiminni sem sameiginlega vettvangsinnviði, eða finnur hvert teymi upp lykla, ógildingu og stormvörn upp á eigin spýtur?** Skyndiminni gert vel er lítið safn erfiðra vandamála leyst einu sinni: normaðir lyklar, atburðadrifin ógilding, beiðnasamruni, réttar HTTP-merkingar og sýnileiki á hvert lag. Þegar hvert teymi spinnur þetta borgar stór skipulagsheild fyrir sömu mistökin ítrekað, og eitrunargalli eða einkagagnaleki lagaður í einni þjónustu helst hljóðlega í tíu öðrum. Komdu með heiðarlegt kort af því hver á skyndiminnisvenjur í dag og hve mikill tvítekinn skyndiminniskóði er til yfir þjónustur. Sjónarmiðið á móti er sjálfræði: teymi standa gegn skyldubundnu sameiginlegu bókasafni, svo vegðu troðna slóð sem er auðveld í upptöku gegn hörðum staðli sem er framfylgt. Fyrir vettvangshóp fyrirtækis eða hins opinbera er sameiginleg, vel prófuð skyndiminnisgeta líka ódýrasta leiðin til að láta öryggis- og úttektarkröfur gilda einsleitt, svo umræðan ætti að ákveða hvað verður sameiginlegir innviðir og hver fjármagnar það.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Skyndiminni er ódýrasta leið þín til að lifa af umferðartopp sem þú hefur ekki enn efni á að stigvaxa fyrir, svo eyddu þeim litla tíma sem þú hefur í fáar áhrifamiklar staðsetningar: CDN með útgáfumerktum vefslóðum fyrir kyrrstæðar eignir, og eitt cache-aside lag með stuttum TTL og skjálfta fyrir framan heitustu fyrirspurn þína. Hallaðu þér að stýrðum CDN- og skyndiminnisþjónustum frekar en að reka þín eigin og bættu við beiðnasamruna snemma, því opnunardagsstormur gegn litlum gagnagrunni er bilunin sem líklegust er til að enda góðan dag illa. Slepptu íburðarmiklum ógildingaráætlunum þar til þú hefur gögn sem segja þér að þær skipti máli.

**Lítið fyrirtæki.** Án skyndiminnissérfræðings og með þröngt fjárhagsáætlun skaltu kjósa að kaupa skyndiminni sem þú færð ókeypis innan verkfæra sem þú rekur þegar: CDN búnt með hýsingu þinni, HTTP `Cache-Control` hausa á svörum veframmans þíns og innbyggt fyrirspurnarskyndiminni gagnagrunnsins. Kaupa-eða-smíða valið hallast hér nánast alltaf að kaupum, þar sem rangt lyklað skyndiminni sem lekur gögnum eins viðskiptavinar til annars kostar miklu meira en stýrða þjónustan sem þú forðaðist. Fáðu tvo ódýru sigrana rétta, réttar HTTP-merkingar og að geyma aldrei auðkenndar síður á sameiginlegum lögum, og láttu framandi mynstur vera.

**Stórfyrirtæki.** Í stórum stíl yfir mörg teymi færist áhættan frá nokkru einu skyndiminni til ósamræmis milli þeirra: sundurleit lyklakerfi, ójöfn ógilding og einkagagnalekar sem birtast í einni þjónustu en ekki annarri. Útvegaðu skyndiminni sem sameiginlega vettvangsinnviði með troðnum sjálfgefnum slóðum fyrir lykla, ógildingu, stormvörn og sýnileika á hvert lag, svo hitahlutfall, brottrekstur og úrelding séu sýnileg á einum stað og stýrð einsleitt. Gerðu skyndiminnisstillingu rýnanlega sem öryggisviðkvæman kóða og líttu á ógildingu yfir svæði sem fyrsta flokks hönnunarvanda frekar en keyrsluhandbók hvers teymis.

**Hið opinbera.** Innkaupa- og gagnsæisskorður móta hvað þú getur geymt og hvernig þú sannar að það sé öruggt. Geymdu opinbert efni ágengt, leiðbeiningar, eyðublöð og gjaldskrártöflur á bak við CDN með löngum TTL, svo skilafrestsbylgja sé gleypt langt frá upptökunum, og skjalfestu þá stillingu fyrir úttekt. Auðkenndar síður sem sýna eigin skrár borgara mega aldrei snerta sameiginlegt skyndiminni og sú regla ætti að vera sannreynanleg, ekki bara fullyrt. Þar sem CDN eða skyndiminnisþjónusta er keypt af söluaðila skaltu krefjast þess að samningurinn afhjúpi stýringarnar sem þú þarft (lyklun, hreinsun og skráningu) og forðast bindingu sem fangaði opinber gögn á bak við séreignarleg skyndiminnissnið.

## Dæmi

**Sprotafyrirtæki.** Lítið neytendaforrit keyrir vörulista sinn gegnum cache-aside lag studt af geymslu í minni, með 60 sekúndna TTL og skjálfta svo færslur renni ekki út saman. Kyrrstæðar eignir fara á CDN með útgáfumerktum skráarnöfnum og eins árs max-age, svo uppsetning sem breytir stílblaði afgreiðir nýja vefslóð og þarf aldrei hreinsun. Þegar opnun í vinsælu hlaðvarpi sendir umferðartopp þýðir single-flight samruni að þúsundir samtímis heimasíðumissa valda einum gagnagrunnslestri, ekki þúsundum. Stofnendurnir eyða nánast engu í skyndiminni en ráða við topp sem hefði brætt litla gagnagrunninn þeirra, því þeir settu fáein vel valin skyndiminni af ásetningi.

**Stórfyrirtæki.** Hnattrænn smásali afgreiðir milljónir kaupenda gegnum lagskipt skyndiminni: CDN fyrir myndir og skyndiminnishæf API-svör, sameiginlegt öfugs-milliþjóns skyndiminni á hverju svæði og forritaskyndiminni fyrir útreiknað verð og birgðabrot. Skyndiminnislyklar eru normaðir og innihalda gjaldmiðil, tungumál og tækjaflokk, svo sérsníðing leki aldrei og hitahlutföll haldist há. Vörugögn nota stutt TTL með atburðadrifinni ógildingu, svo verðbreyting birtir á skilaboðabus sem hreinsar viðkomandi lykla yfir svæði á sekúndum. Hvert lag skýrir hitahlutfall, brottrekstrarhlutfall og úreldingu til sýnileikavettvangsins úr kafla 9.2, og viðvörun á fallandi hitahlutfall greip einu sinni of lítið skyndiminni áður en það varð afgreiðslurekstrarrof.

**Hið opinbera.** Landsbundið skattayfirvald rekur skilagátt sem er hljóð mestan hluta ársins og yfirbuguð nálægt skilafresti. Teymið geymir í skyndiminni ágengt þar sem það er öruggt og aldrei þar sem það er ekki. Opinbert efni (leiðbeiningarsíður, eyðublöð, gjaldskrártöflur) er afgreitt frá CDN með löngum TTL og útgáfumerktum vefslóðum, sem gleypir lesbylgju skiladagsins langt frá upptökunum. Auðkenndar síður sem sýna framtal borgara eru merktar `no-store` og snerta aldrei sameiginlegt skyndiminni, svo enginn skattgreiðandi fær nokkru sinni gögn annars. Skyndiminnisstilling er rýnd sem öryggisviðkvæmur kóði gegn vinnubrögðum kafla 4.2 og stormvörn er álagsprófuð á skilafrestsstærð mánuðum fyrirfram, svo gáttin sem áður bognaði á annasamasta degi ársins heldur nú.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun skyndiminnis er óvenju bein og auðveld að magnsetja. Skyndiminni sem hækkar hitahlutfall úr 80 í 95 prósent sker upptakaumferð um þrjá fjórðu, sem getur þýtt að fresta gagnagrunnsuppfærslu, reka færri forritaþjóna eða lifa umferðartopp sem annars hefði krafist neyðarstigvaxtar. Töfarbætur umbreytast í tekjur í verslun og í ánægju- og klárunarhlutföll í opinberri þjónustu, þar sem rannsóknir hafa lengi tengt hraðari síður við hærri umbreytingu og minni brottfall. Útleiðar- og reikniaflskostnaður lækkar því beiðni afgreidd frá jaðrinum borgar aldrei fyrir upptakabandvídd eða vinnslu. Fyrir lesþung kerfi, sem flest kerfi eru, er skyndiminni oft ódýrustu afköstin sem þú getur keypt.

Vegðu heildareignarkostnað heiðarlega. Beinn kostnaður er hóflegur: CDN- og skyndiminnisinnviðir eru ódýrir miðað við upptakagetuna sem þeir spara. Raunverulegi kostnaðurinn er verkfræðiagi, því skyndiminni sem er rangt er verra en ekkert skyndiminni. Úreldingargallar, ógildingarmistök og skyndiminniseitrunarveikleikar bera allir raunverulegan kostnað og þeir vaxa þegar skyndiminni er spunnið eftir teymum í stað þess að vera afhent sem sameiginleg, vel prófuð geta. Sterkustu viðskiptarökin fjármagna lítið magn sameiginlegra skyndiminnisinnviða og venja (staðlaðir lyklar, ógilding, stormvörn og sýnileiki) svo hvert teymi fái ávinninginn án þess að endurtaka mistökin. Rammað fyrir forystu tengist skyndiminni mælikvörðum sem hún fylgist þegar með: innviðakostnaði, síðutöf, umbreytingar- og klárunarhlutföllum og atvikatíðni á háannaatburðum.

## Andmynstur og gildrur

- **Skyndiminni án ógildingar:** að setja langt TTL án leiðar til að hreinsa, svo leiðrétt gildi helst rangt í klukkustundir.
- **Lyklar of grófir:** að geyma sérsniðin svör undir sameiginlegum lykli og leka gögnum eins notanda til annars.
- **Lyklar of fínir:** að hafa breytileg inntök í lyklinum svo engar tvær beiðnir passa nokkurn tíma og hitahlutfallið hrynur.
- **Engin stormvörn:** heitur lykill rennur út undir álagi og hver beiðni æðir á upptökin í einu.
- **Samstillt fyrning:** hópur færslna skrifaður saman rennur allur út á sama augnabliki án skjálfta og veldur reglubundnu hjarðhlaupi.
- **Einkagögn geymd á sameiginlegum lögum:** `Cache-Control: private` eða `no-store` vantar, svo milliþjónn eða CDN geymir auðkennd svör.
- **Að hunsa ólykluð inntök:** að spegla haus inn í svarmeginmál en sleppa honum úr lyklinum, sem opnar dyrnar að skyndiminniseitrun.
- **Of lítið skyndiminni:** skyndiminni of lítið til að halda vinnumenginu slær og rekur út færslur rétt áður en þeirra er þörf.
- **Ómælt skyndiminni:** engin hita- eða brottrekstrarmælikvarði, svo skertu skyndiminni er ósýnilegt þar til það verður rekstrarrof.
- **Write-back án endingar:** hröð skrif sem hverfa þegar skyndiminnið deyr fyrir skolun, án stuðningsábyrgðar.

## Þroskalíkan

- **Stig 1, Upphaf:** Skyndiminni er ad hoc og á hvern hönnuð, bætt við viðbragðsdrifið þegar eitthvað finnst hægt. TTL eru giskuð, lyklar ósamræmdir, ógilding handvirk eða fjarverandi og úrelt gögn og dularfullir gallar eru algeng. Enginn rekur hitahlutfall og umferðartoppur sem skyndiminni hefði átt að gleypa veldur þess í stað rekstrarrofi.
- **Stig 2, Þróun:** Teymi geyma í skyndiminni á augljósum stöðum og nota CDN fyrir kyrrstæðar eignir. Grunn TTL og cache-aside birtast, en venjur eru mismunandi frá þjónustu til þjónustu, ógilding er ósamræmd, stormvörn vantar, reglur um einka- á móti sameiginlegu skyndiminni eru óformlegar og sýnileiki er takmarkaður við stöku stikkprufur.
- **Stig 3, Stöðlun:** Skyndiminnisstefna er skjalfest og framfylgt um alla skipulagsheildina. Skyndiminnislyklar eru normaðir, TTL fylgja sameiginlegri ferskleikaflokkun, ógilding er atburðadrifin þar sem hún skiptir máli, stormvörn og réttar HTTP-merkingar eru staðlaðar, einkagögn eru aldrei geymd á sameiginlegum lögum og hvert lag skýrir hita- og brottrekstrarhlutfall í sameiginlega sýnileikaleiðslu.
- **Stig 4, Stjórnun:** Skyndiminni er mælt og stýrt gegn grunnlínum. Hvert lag hefur markhitahlutfall, úreldingarfjárhagsáætlanir og brottrekstrarþröskulda, og mælaborð gefa viðvörun þegar hitahlutfall fellur eða brottrekstrarhlutfall hækkar yfir grunnlínu. Stormvarnir eru álagsprófaðar á háannastærð, upptakaálagsminnkun er magnsett fyrir hvert skyndiminni, TTL og brottrekstrarstefnur eru stilltar út frá mældum aðgangsmynstrum og skyndiminnisstilling er rýnd sem öryggisviðkvæmur kóði fyrir útgáfu.
- **Stig 5, Samhæfing:** Skyndiminni er stöðugt bætt og samþætt um skipulagsheildina. Staðsetning, lyklar og TTL aðlagast breytilegri umferð, jaðartölvun er notuð þar sem hún vinnur sér inn sæti sitt, getuáætlun og kostnaðarlíkön draga úr skyndiminnismælikvörðum og lærdómur af atvikum eins teymis nærir sameiginlegar venjur. Skipulagsheildin lítur á skyndiminni sem hannaða, mælda, aðlögunarhæfa getu frekar en safn staðbundinna reddinga.

## Hugmyndir til umræðu

1. Hvaða eina skyndiminni í kerfinu þínu, ef það yrði kalt núna, myndi stofna upptökunum mest í hættu, og hvað ver það?
2. Fyrir hvert lag skyndiminnisstigveldis þíns, geturðu nefnt núverandi hitahlutfall þess eftir minni og ef ekki, hvað segir það þér?
3. Hvar hefurðu breytt ógildingarvanda í nafngiftarvanda með útgáfumerktum lyklum og hvar gætirðu enn gert það?
4. Hver af skrifleiðum þínum notar cache-aside, write-through, write-back eða write-around og var hvert valið af ásetningi?
5. Ef árásaraðili stýrði einum beiðnahaus, gæti hann eitrað eitthvert skyndiminnisgeymt svar sem notendur þínir deila?
6. Hvernig myndirðu vita, innan mínútna, að hitahlutfall þitt hefði hljóðlega fallið um tuttugu stig?

## Helstu atriði

- Skyndiminni sker töf, álag og kostnað, og skyndiminnisstigveldið (biðlari, CDN og jaðar, öfugur milliþjónn, forrit, gagnagrunnur) leyfir þér að svara eins langt upp og út og þú getur örugglega.
- Ógilding er erfiði hlutinn. Hannaðu skyndiminnislykla og TTL af ásetningi og breyttu ógildingarvanda í nafngiftarvanda með útgáfumerktum lyklum hvar sem þú getur.
- Verðu skyndiminnið undir álagi með beiðnasamruna, skjálfta og stale-while-revalidate, því skyndiminni er mest þörf einmitt þegar stormur gæti brotið það.
- Veldu skrifmynstur og brottrekstrarstefnur fyrir hvert vinnuálag og notaðu HTTP-skyndiminnismerkingu (`Cache-Control`, ETag, staðfestingu) skýrt frekar en að láta skyndiminni giska.
- Líttu á skyndiminnisgeymt efni sem árásaryfirborð og mældu hitahlutfall, brottrekstur og úreldingu, því ósýnilegt eða rangt lyklað skyndiminni er falin skuld, ekki eign.

## Heimildir og frekari lestur

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Andrew S. Tanenbaum and Herbert Bos, *Modern Operating Systems*
- John L. Hennessy and David A. Patterson, *Computer Architecture: A Quantitative Approach*
- Roy T. Fielding and Julian Reschke, "Hypertext Transfer Protocol (HTTP/1.1): Caching," RFC 7234, IETF
- Mark Nottingham, "Caching Tutorial for Web Authors and Webmasters"
- James Kettle, "Practical Web Cache Poisoning," PortSwigger Research
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering: How Google Runs Production Systems*
- Michael T. Nygard, *Release It! Design and Deploy Production-Ready Software*
