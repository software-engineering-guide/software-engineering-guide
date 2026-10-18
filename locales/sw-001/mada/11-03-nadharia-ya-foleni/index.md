# 11.3 Nadharia ya foleni

## Muhtasari na msukumo

[Nadharia ya foleni](https://en.wikipedia.org/wiki/Queueing_theory) ni utafiti wa kihisabati wa mistari ya kusubiri. Katika uhandisi wa programu, ni nadharia ya kimya nyuma ya mazoea mengi mno. Kuitikia kwa huduma kwa wateja, upangaji wa [kanban](https://en.wikipedia.org/wiki/Kanban_%28development%29) (mbinu ya kuvuta inayoweka kikomo cha [kazi inayoendelea](https://en.wikipedia.org/wiki/Work_in_process) kuboresha mtiririko), foleni za ujumbe kati ya michakato, mabomba ya usambazaji endelevu: yote ni foleni, na yote hutii sheria zilezile. Kuelewa sheria hizo kunaruhusu timu kufikiri kuhusu [nyakati za kuongoza](https://en.wikipedia.org/wiki/Lead_time), [upitishaji](https://en.wikipedia.org/wiki/Throughput), uwezo, na gharama halisi ya kuendesha mifumo karibu na mipaka yake, badala ya kushangazwa nayo kwenye uzalishaji. Sura hii iko katika sehemu ya Mtiririko kwa sababu nadharia ya foleni ndiyo msingi rasmi wa mtiririko: inaeleza *kwa nini* kazi inasubiri, na nini kinapunguza kusubiri kweli.

Hii ndiyo motisha: silika kuhusu foleni daima si sahihi, na si sahihi kwa njia ghali. Watu hudhania seva inayoendesha kwa matumizi ya asilimia 90 iko "asilimia 10 mbali na matatizo," wakati kwa kweli nyakati za kusubiri hulipuka bila mstari matumizi yanapokaribia asilimia 100. Hudhania kuongeza kazi inayoendelea (WIP) kunaharakisha utoaji, wakati kunarefusha nyakati za kuongoza. Hupanga uwezo kuzunguka wastani, kisha huharibiwa na kutofautiana. Nadharia kidogo ya foleni hubadilisha silika hizi ghali kwa uhusiano mchache imara, muhimu zaidi **[Sheria ya Little](https://en.wikipedia.org/wiki/Little%27s_law)**, unaoshikilia kuvuka foleni za wateja, mbao za kazi, na mabomba ya CI/CD vilevile.

Kwa timu kubwa, biashara kubwa, na serikali, nadharia ya foleni ni lugha ya pamoja ya uwezo na mtiririko, inayounganisha majukumu ambayo vinginevyo huzungumza bila kusikilizana. Mameneja wa bidhaa wanajali muda wa kuongoza kutoka wazo hadi mteja. SRE wanajali matumizi ya seva na ucheleweshaji. Timu za DevOps zinajali mzunguko wa usambazaji. Viongozi wa msaada wanajali nyakati za kuitikia. Hivi vyote ni vipimo vya foleni, na kuvionyesha kwenye mfumo mmoja (kasi ya kufika, kasi ya huduma, matumizi, muda wa kusubiri) kunaruhusu shirika kupanga uwezo, kuweka SLO (malengo ya kiwango cha huduma) za kweli, na kuhalalisha uwekezaji kwa hisabati badala ya hadithi.

## Kanuni kuu

- **Kila chenye kusubiri ni foleni:** tiketi, kazi, ujumbe, na usambazaji vikijumuishwa.
- **Sheria ya Little ndiyo nanga:** vipengee kwenye mfumo = kasi ya kufika × muda kwenye mfumo (κ = λτ).
- **Matumizi na muda wa kusubiri havina mstari:** asilimia 15 ya mwisho ya uwezo ndiyo ghali zaidi.
- **Kutofautiana ni adui wa mtiririko:** wastani huficha maumivu; tofauti huunda foleni.
- **Kupunguza kazi inayoendelea hupunguza muda wa kuongoza:** mtiririko, si kuwa na shughuli, ndio lengo.
- **Pima mtiririko mzima:** kufika, huduma, mafanikio, kushindwa, kuruka, na kusubiri.
- **Mchakato ni foleni ya foleni:** unda kielelezo cha hatua, kisha boresha inayobana.

## Mapendekezo

### Jifunze nukuu ya msingi na uitumie kwa uthabiti

Idadi ndogo ya kiasi inaelezea foleni yoyote. Kusawazisha juu yake (herufi za Kigiriki ni za kawaida) huondoa utata kuvuka timu:

- **λ (lambda), kasi ya kufika:** vipengee vipya vinaingia kwa kasi gani.
- **μ (mu), kasi ya huduma:** vipengee vinashughulikiwa kwa kasi gani. Kwa kuwa "kasi ya huduma" hutumika kwa utata, mara nyingi inafaa kugawanya upitishaji waziwazi kuwa **kasi jumla (χ)**, **kasi ya mafanikio (α)**, **kasi ya kushindwa (β)**, na **kasi ya kuruka (σ)**, ambapo χ = α + β + σ.
- **ρ (rho), matumizi / ukali wa trafiki = λ / μ:** muhtasari muhimu zaidi. ρ < 1 inamaanisha foleni inamwagika; ρ ≥ 1 inamaanisha inakua bila mipaka.
- **Nyakati:** muda wa kuongoza (τ, kuanza hadi kumaliza), muda wa kazi (φ, usindikaji halisi), muda wa kusubiri (ω, kinachosubiri), na muda wa hatua (θ, kati ya ukamilishaji).
- **ε (epsilon), uwiano wa makosa:** kushindwa ÷ jumla.

Kutaja kushindwa na *kuruka* waziwazi ni muhimu katika programu: kipengee kinachoachwa (mteja anayekata tamaa, kikapu kilichoachwa, tiketi ya kazi iliyokataliwa) huondoka kwenye foleni bila kuhudumiwa, na kujifanya kilikuwa "kimehudumiwa" kunaharibu vipimo vyako. Fuatilia **kutokujiunga** (kuamua kutojiunga), **kujiondoa** (kukata tamaa baada ya kusubiri), na **kuruka foleni** (kubadilisha foleni) kama matokeo ya daraja la kwanza.

### Egemeza upangaji kwenye Sheria ya Little

Sheria ya Little inasema kwamba wastani wa muda mrefu wa idadi ya vipengee kwenye mfumo thabiti ni sawa na wastani wa kasi ya kufika mara wastani wa muda ambao kila kipengee kinatumia kwenye mfumo: **κ = λ τ** (kwa kawaida L = λW). Ni ya jumla kwa kustaajabisha (haihitaji dhana yoyote kuhusu usambazaji wa kufika wala mpangilio wa huduma), jambo linaloifanya kuwa zana kuu ya upangaji wa mtiririko. Ikipangwa upya, inakuambia kwamba **muda wa kuongoza = kazi inayoendelea ÷ upitishaji**. Hiyo ndiyo msingi wa kihisabati wa kanban na lean: ukitaka nyakati fupi za kuongoza na huwezi kuongeza upitishaji, lazima upunguze WIP. Pia inatoa ukaguzi wa haraka wa busara. Ikiwa tiketi 40 ziko wazi na unafunga 8 kwa siku, tiketi ya wastani inachukua takriban siku 5, bila kujali kila mtu anahisi ana shughuli kiasi gani. Sharti lake moja ni *uthabiti*: kufika lazima kusizidi kuondoka kwa kudumu (ρ < 1), la sivyo foleni, na dhana za sheria, zinavunjika.

### Heshimu kutokuwa na mstari kwa matumizi

Somo muhimu zaidi la kiuendeshaji la nadharia ya foleni ni kwamba muda wa kuitikia hupanda kwa kasi, si taratibu, matumizi yanapokaribia asilimia 100. *Seven insights into queueing theory* ya Bob Wescott inanasa matokeo ya kivitendo kwa uhai:

1. Kadiri kituo cha huduma kilivyo polepole, ndivyo matumizi ya kilele unayopaswa kupanga yanavyokuwa ya chini.
2. Ni vigumu sana kutumia asilimia 15 ya mwisho ya chochote.
3. Kadiri unavyokimbia karibu na ukingo, ndivyo bei ya kukosea inavyokuwa juu.
4. Ukuaji wa muda wa kuitikia umefungwa na vipengee vingapi vinaweza kusubiri.
5. Hivi ni wastani, si upeo: panga kwa mkia.
6. Jihadhari na athari ya kukataa ya binadamu kuvuka vituo vingi vya huduma.
7. Onyesha maboresho madogo katika mwanga wake bora.

Maana ya usanifu: **tayarisha nafasi ya ziada kwa makusudi.** Kulenga matumizi ya asilimia 70–80 kwa mifumo inayojali ucheleweshaji si upotevu; ni kununua muda wa kuitikia unaotabirika. Hili linaarifu moja kwa moja upangaji wa uwezo na SLO (sura za 3.5 na 9.1).

### Unda kielelezo cha michakato kama foleni ya foleni

Kazi halisi hutiririka kupitia hatua, na mchakato wa hatua nyingi ni foleni tu ambayo vipengee vyake vyenyewe vimewekwa kwenye foleni kila hatua. Uunde kielelezo hivyo: kasi ya kufika ya mchakato ni kasi ya kufika ya hatua ya 1; kasi ya mafanikio ya mchakato ni kasi ya mafanikio ya hatua ya mwisho; hesabu za makosa na za kuruka za mchakato ni jumla kuvuka hatua. Maumbo mawili ya kawaida yanarudiwa:

- **Mifereji**, ambapo hesabu za vipengee hupungua kila hatua (kuajiri: kufikia → mahojiano → ofa; ununuzi: kuvinjari → kikapu → kulipa; utoaji: kuunganisha → UAT → uzalishaji). Boresha hatua inayojali zaidi: ongeza kufika kwa juu ya mfereji, punguza kuruka kwa katikati ya mfereji (kuachwa kwa kikapu), au punguza makosa ya hatua ya mwisho (matoleo mabaya ya uzalishaji).
- Mtiririko wa **almasi mbili** wa ugunduzi-na-utoaji (gundua → fafanua → tengeneza → toa), ambao sehemu ya Mtiririko ya kitabu hiki inaushughulikia moja kwa moja (sura ya 11.1).

Kutafuta na kupunguza **hatua inayobana** (kizuizi) ndipo uboreshaji wa mtiririko unapolipa; kuboresha zisizobana huhamisha foleni tu.

### Unganisha vipimo vya foleni na KPI ambazo timu tayari zinatumia

Kiasi cha foleni hulingana wazi na vipimo vya utoaji na vya kutegemewa kwingineko katika kitabu hiki, ndiyo inayofanya nadharia iwe ya vitendo badala ya ya kitaaluma:

- **Muda wa kuongoza wa utoaji (Dτ)**, "dhana hadi mteja," ni kipimo cha muda wa kuongoza (τ) na kipimo cha DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) (sura ya 11.2).
- **Mzunguko wa usambazaji (Dμ)** ni kipimo cha kasi ya huduma.
- **Kiwango cha kushindwa kwa mabadiliko (Dε)** ni uwiano wa makosa.
- **Muda wa kurejesha (Rτ)** ni muda wa kuongoza wa kurejesha, yaani MTTR (sura ya 9.3).

Tofautisha **MTTR** kadhaa (muda wa wastani wa *kuitikia*, *kurekebisha*, *kupona*, na *kutatua*) kwa sababu zinapima sehemu tofauti za foleni ya tukio na mara kwa mara zinachanganywa. Kuweka SLI/SLO/SLA (sura ya 9.1) kwenye maneno ya foleni kunaweka malengo ya uaminifu na yanayolinganishwa.

## Mabadilishano: faida na hasara

| Uamuzi | Faida | Hasara |
|---|---|---|
| **Endesha mifumo kwa matumizi ya juu** | Gharama ndogo ya vifaa/kitengo | Milipuko ya ucheleweshaji isiyo na mstari; dhaifu kwa miruko |
| **Tayarisha nafasi ya ukarimu** | Ucheleweshaji unaotabirika; ustahimilivu kwa tofauti | Gharama ya juu ya hali thabiti; inaonekana "haitumiki" |
| **Weka kikomo cha WIP (kanban)** | Nyakati fupi za kuongoza; ubadilishaji mdogo wa muktadha | Inahisi polepole; inahitaji nidhamu kushikilia kikomo |
| **Uundaji rasmi wa vielelezo vya foleni** | Maamuzi ya uwezo yaliyopimwa kwa namba; mshangao mdogo | Mkondo wa kujifunza; vielelezo vinarahisisha uhalisia wa fujo |
| **Kanuni za kidole gumba tu** | Haraka, hakuna hisabati | Si sahihi hasa pale ghali zaidi (karibu na uwezo) |

Mabadilishano yanayojirudia ni **ufanisi dhidi ya kutabirika**: kusukuma matumizi juu kunaokoa fedha hadi ghafla hakuokoi, hapo ucheleweshaji, kushindwa, na gharama za kuzima moto zinazidi akiba. Mchango wa nadharia ya foleni ni kukuambia *wapi* mwamba huo uko ili mabadilishano yawe chaguo, si ajali.

## Maswali ya kujadili na timu yako

1. **Lengo lenu wazi la matumizi kwa kila mfumo unaojali ucheleweshaji ni lipi, na nani aliliidhinisha?** Nafasi ya ziada ni ununuzi wa makusudi wa ucheleweshaji unaotabirika, kwa hiyo inapaswa kuwa sera iliyotajwa, si ajali ya mzigo wowote uliofika. Kwa kuwa muda wa kuitikia hupanda bila mstari, kuendesha kwa asilimia 85 tayari kunaweza kumaanisha ucheleweshaji wa mkia ulioinuka, hata hivyo fedha huona nafasi ya ziada kama upotevu na kusukuma matumizi juu. Leta namba: matumizi ya sasa, mkunjo wa ucheleweshaji uliopimwa, na gharama ya tukio lenu la mwisho la ucheleweshaji, kisha onyesha mwamba uko wapi kwa kila huduma. Kwa mifumo ya biashara kubwa na serikali yenye vilele vya msimu (msimu wa kuwasilisha, madirisha ya usajili), weka lengo kutoka kwenye mwamba kwa kilele, si wastani. Kama hakuna anayemiliki lengo la matumizi, matukio ya ucheleweshaji yataendelea kuonekana "kutoka popote."

2. **Wapi katika mifumo yenu foleni haina mipaka, bila shinikizo-nyuma la kumwaga mzigo inapozidiwa?** Foleni isiyo na mipaka haishindwi kwa neema; inashuka kuwa kuporomoka, kwa sababu kufika kunazidi kuondoka kwa kudumu (rho >= 1) kunamaanisha foleni inakua bila kikomo. Orodhesha foleni zenu za ujumbe, madimbwi ya nyuzi, na akiba za maombi, na uulize kinachotokea kwa kila moja kasi ya kufika inapozidi kasi ya huduma: inamwaga mzigo, inatumia shinikizo-nyuma, au inaanguka? Hili ni muhimu sana kwa ukubwa wa biashara kubwa, ambapo huduma moja ya chini ya mkondo iliyojaa inaweza kuenea kuvuka huduma. Leta matokeo ya jaribio la mzigo au tukio la zamani ambapo foleni ilijaa, na uangalie kama mfumo ulikataa kazi ya ziada au ulijaribu kushikilia yote. Suluhisho ni foleni zenye mipaka zenye shinikizo-nyuma wazi na muda wa kuisha unaotokana na Sheria ya Little, ili kuzidiwa kumwage badala ya kuangusha.

3. **Mnaunda kielelezo cha mtiririko wenu wa wazo-hadi-uzalishaji kama foleni ya foleni, na je, maboresho yenu yanalenga kizuizi halisi?** Mchakato wa hatua nyingi ni foleni ambayo vipengee vyake vimewekwa kwenye foleni kila hatua, na kuboresha chochote kingine kuliko hatua inayobana huhamisha foleni tu. Chora ramani ya mfereji wenu wa utoaji (kuunganisha hadi UAT hadi uzalishaji, au gundua hadi fafanua hadi tengeneza hadi toa) na upime kasi za kufika, huduma, kusubiri, na kuruka kila hatua kupata mahali kazi inapojilimbikiza kweli. Timu mara kwa mara huboresha hatua zinazoielewa zaidi badala ya kizuizi, jambo linalotumia juhudi na haliwezi kusogeza chochote. Leta data ya muda wa kusubiri kwa kila hatua, si hisia, kwa sababu kizuizi mara nyingi ni hali ya kusubiri (mapitio, idhini, upatikanaji wa mazingira) badala ya hali ya kazi. Mara mnapojua kizuizi, lenga huko na muache zisizobana.

4. **Mnatumia Sheria ya Little kuweka vikomo vya WIP, au mnaongeza uwezo kutibu nyakati za kuongoza ambazo nidhamu zaidi tu ingerekebisha?** Sheria ya Little inasema muda wa kuongoza ni sawa na kazi inayoendelea ikigawanywa kwa upitishaji, kwa hiyo ikiwa huwezi kuongeza upitishaji, kiguzo pekee kilichobaki cha nyakati fupi za kuongoza ni kupunguza WIP, kinachogharimu kujizuia tu. Mvuto unaoshindana ni halisi: kuweka kikomo cha kazi inayoendelea kunahisi polepole na bila kazi, na mameneja walio chini ya shinikizo wangependelea kuajiri au kununua vifaa kuliko kuziambia timu kuanza kidogo na kumaliza zaidi. Leta namba ngumu, vipengee vilivyo wazi sasa na kiwango cha ukamilishaji kwa kila hatua, na uhesabu muda wa wastani wa kuongoza unaodokezwa, kisha ulinganishe na watu wanavyoamini; pengo kwa kawaida ni kubwa na la aibu. Katika biashara kubwa au wakala, ombi la kuajiri au la ununuzi lililohalalishwa kama suluhisho la muda wa kuongoza linapaswa kujaribiwa dhidi ya hesabu hii kwanza, kwa sababu ongezeko la wafanyakazi linaloinua WIP linaweza kurefusha nyakati za kuongoza ambazo lilikusudiwa kufupisha.

5. **Mnapanga uwezo kuzunguka wastani, au mmepima tofauti inayounda foleni zenu kweli?** Foleni hutokana na tofauti, si wastani, kwa hiyo mifumo miwili yenye mzigo wa wastani ulio sawa inaweza kufanya tofauti kabisa ikiwa moja ina kufika kwa miruko au muda wa huduma wenye mkia mrefu. Mvutano ni kwamba wastani ni rahisi kukusanya na wa kutuliza kuripoti, wakati tofauti na mkia ni ngumu kupima na hazikaribishwi kwenye sasisho la hali. Leta usambazaji, si wastani: miruko ya kufika, nyakati za huduma na kusubiri za asilimia ya 95 na ya 99, na ukubwa wa makundi yanayokusanya kazi kuwa miruko. Kwa mifumo ya biashara kubwa na serikali yenye mawimbi yanayotabirika (msimu wa kuwasilisha, uendeshaji wa mishahara, madirisha ya usajili, mizigo ya mwisho wa robo), panga akiba na lengo la matumizi kutoka tofauti ya kipindi cha kilele, kwa sababu usanifu uliopimwa kwa wastani wa mwaka utashindwa hasa umma unapotazama.

6. **Foleni zenu zipi zinahesabu kimya kuachwa na kukataliwa kana kwamba kazi ilihudumiwa, na mahitaji gani yasiyotimizwa hilo linaficha?** Kipengee kinachokataa kujiunga, kujiondoa, au kukataliwa huondoka kwenye foleni bila kushughulikiwa, na kukirekodi kama "kimehudumiwa" kunaharibu upitishaji wenu, uwiano wa makosa, na mpango wa uwezo kwa wakati mmoja. Mazingatio yanayoshindana ni kwamba "simu zilizojibiwa" au "tiketi zilizofungwa" zinaonekana bora kwenye dashibodi kuliko "wapigaji waliokata tamaa," kwa hiyo namba ya uaminifu ndiyo ambayo hakuna anayejitolea kuifichua. Leta kasi ya kuruka (σ), hesabu za kutokujiunga na kujiondoa, na tofauti kati ya mzigo uliotolewa na uliohudumiwa, ili mahitaji halisi yaonekane. Hili ni kali sana katika utoaji wa huduma za serikali, ambapo raia wanaoacha foleni ya simu au maombi ya mafao ni wajibu usiotimizwa badala ya kesi zilizotatuliwa, na kuwaripoti kama waliohudumiwa kunapotosha utendaji na kudharau uwezo ambao umma unadaiwa.

## Mtazamo wa sekta

**Kampuni changa.** Huna muda wa uundaji rasmi wa vielelezo vya foleni na huuhitaji. Fikia ushindi wa bei nafuu mbili kwanza: tumia Sheria ya Little kwenye mrundikano wako kuona muda halisi wa kuongoza ambao WIP yako inadokeza, na tazama ubao wako wa kanban kwa hatua ambapo kazi inajilimbikiza kabla ya kuajiri dhidi ya kizuizi ambacho huenda hakipo. Weka matumizi mbali na mwamba kwenye njia yoyote inayojali ucheleweshaji kwa kuacha nafasi ya ziada badala ya kuirekebisha, kwa sababu kukatika wakati wa mruko wa ukuaji kunagharimu zaidi sana kuliko uwezo kidogo usiotumika.

**Biashara ndogo.** Bila mtaalamu wa foleni kwenye wafanyakazi, nunua vipimo badala ya kujenga vielelezo. Chagua dawati la msaada, wakala wa ujumbe, au jukwaa la upangishaji ambalo tayari linaripoti kasi ya kufika, muda wa kusubiri, na kuachwa, na usome namba hizo badala ya kuzitoa. Weka uamuzi kama kutazama dalili mbili: kusubiri kunakopanda bila mstari unapozidi kuwa na shughuli, na wateja wanaokata tamaa kabla ya kuhudumiwa, kwa kuwa mteja aliyepotea ni gharama ya foleni inayoumiza zaidi biashara ndogo.

**Biashara kubwa.** Kazi ni kufanya fikra ya foleni kuwa nidhamu ya pamoja kuvuka timu nyingi: nukuu moja iliyokubaliwa (λ, μ, ρ, muda wa kuongoza), sera thabiti za WIP na nafasi ya ziada ya matumizi, na viwango vya shinikizo-nyuma ili huduma moja ya chini ya mkondo iliyojaa isienee kuvuka huduma. Weka SLO na uwezo kutoka uchambuzi wa foleni badala ya makisio, na usimamie foleni zako kama jalada lenye vipimo vya msingi na mapitio ili hakuna timu moja inayoendesha kwa joto kwa kujitenga. Pachika uchambuzi kwenye utawala wa uwezo na ukaguzi, ili lengo la nafasi ya ziada liwe uamuzi ulioandikwa ambao mtu anaumiliki.

**Serikali.** Ununuzi, uwazi, na uwajibikaji wa umma huumba kila uchaguzi wa uwezo. Pima vituo vya mawasiliano na mifumo inayowakabili raia kutoka tofauti ya kipindi cha kilele (msimu wa kuwasilisha, madirisha ya usajili), si wastani wa mwaka, na uajiri ili kuweka matumizi mbali na mwamba mahitaji yanapopanda. Fuatilia kutokujiunga na kujiondoa kama mahitaji ya umma yasiyotimizwa badala ya kuyaficha ndani ya "simu zilizojibiwa," na uhalalishe matumizi ya uwezo kwa makadirio ya muda wa kusubiri ya Sheria ya Little, yanayowapa wakaguzi na viongozi waliochaguliwa kesi inayoweza kutetewa, iliyoungwa na hisabati badala ya hadithi.

## Mifano

**Kampuni changa.** Timu ya SaaS ya watu watano iliyozama kwenye mrundikano wa msaada inadhania inahitaji kuajiri wakala mwingine. Kabla ya kutumia fedha, wanatumia Sheria ya Little: tiketi 60 zilizo wazi na 12 zinazofungwa kwa siku maana yake tiketi ya wastani inasubiri takriban siku 5, jambo linalolingana na barua pepe zenye hasira. Wakitazama ubao wao wa kanban, wanaona tiketi zinajilimbikiza zikisubiri uhandisi, si msaada, kwa hiyo wanaweka kikomo cha kazi inayoendelea na kuelekeza ripoti za hitilafu moja kwa moja kwenye mbio badala ya kuziacha zisubiri kwenye foleni. Muda wa kuongoza unashuka hadi chini ya siku mbili bila kuajiri mtu mpya, na wanatumia bajeti iliyoachwa kwenye kizuizi halisi.

**Biashara kubwa.** Jukwaa la malipo linalopima huduma yake ya uidhinishaji linapima λ ≈ maombi 850/sekunde na μ kwa nodi ≈ 200/sekunde. Kwa upofu hiyo ni takriban nodi 5 (ρ = 0.85), lakini kwa kujua kwamba ρ = 0.85 tayari inamaanisha ucheleweshaji wa mkia ulioinuka kwa kasi, timu inatayarisha hadi ρ ≈ 0.65 na kutumia Sheria ya Little kutabiri idadi ya maombi yanayoendelea na kuweka kina cha foleni na muda wa kuisha. Matukio ya msimu wa kilele yaliyokuwa yanaonekana "kutoka popote" yanatoweka, kwa sababu timu haikuwa tena inafanya kazi kwenye sehemu mwinuko ya mkunjo.

**Serikali.** Kituo cha mawasiliano cha mamlaka ya kodi kinaunda kielelezo cha msaada wa msimu wa kuwasilisha kama foleni: miruko ya kufika (λ), uwezo wa mawakala (μ), na, muhimu, **kasi ya kuruka (σ)** ya raia wanaoacha baada ya kusubiri kwa muda mrefu. Kwa kufuatilia kutokujiunga na kujiondoa badala ya "simu zilizojibiwa" tu, uongozi unaona mahitaji halisi yasiyotimizwa, unaajiri ili kuweka matumizi mbali na mwamba wakati wa vilele, na kuhalalisha uwezo wa ziada kwa makadirio ya muda wa kusubiri ya Sheria ya Little, kesi inayoweza kutetewa, iliyoungwa na hisabati kwa matumizi ya umma badala ya ya hadithi.

## Kesi ya biashara: sababu, ROI, na TCO

Nadharia ya foleni inalipa kwa kuzuia makosa mawili ghali: **kutayarisha kupita kiasi** (kulipia uwezo usiotumika usioutaka) na, kwa uharibifu mkubwa zaidi, **kutayarisha pungufu karibu na mwamba** (ambapo ongezeko dogo la mzigo husababisha ucheleweshaji mkubwa, SLA zilizovunjwa, wateja walioacha, na matumizi ya dharura). Kwa sababu gharama ya kuendesha karibu na asilimia 100 ya matumizi haina mstari, akiba ya "ongeza mzigo kidogo tu" ni ndogo na hasara ni ya maafa, hasa ulinganifu usio sawa ambao hisabati kidogo hugeuza kuwa uamuzi wa makusudi. Faida inapimwa kwa kukatika kulikoepukwa, SLA zilizotimizwa, wateja waliobaki ambao vinginevyo wangekataa kujiunga, na zamu tulivu zaidi za simu ya dharura.

Kwenye **jumla ya gharama ya umiliki**, mfumo ni wa bei nafuu kupokea (ni maarifa, si zana) na unaboresha karibu kila uamuzi wa uwezo, ucheleweshaji, na mtiririko ambao shirika kubwa hufanya kuvuka maisha ya mfumo. Sheria ya Little na vikomo vya WIP hupunguza nyakati za kuongoza bila kununua chochote (ushindi wa mchakato tupu), huku nidhamu ya matumizi ikibadilisha gharama ndogo, inayotabirika ya hali thabiti kwa kuondoa kushindwa ghali, kusikotabirika. Kutoa hoja kwa uongozi, tafsiri tukio la hivi karibuni la ucheleweshaji kuwa mkunjo wa matumizi na uonyeshe lengo la nafasi ya ziada lingelizuia, na utumie Sheria ya Little kuunganisha kupunguza WIP moja kwa moja na utoaji wa haraka.

## Mifumo mibaya na mitego

- **Kupanga uwezo kuzunguka wastani:** kupuuza tofauti, ambayo ndiyo inayounda foleni kweli.
- **Kuendesha kwa joto:** kulenga matumizi ya asilimia 90+ kwenye mifumo inayojali ucheleweshaji na kushtushwa na ucheleweshaji wa mkia.
- **Kuhesabu kuruka kama huduma:** kuchukulia wateja walioacha au tiketi zilizokataliwa kama zilizohudumiwa, kuharibu vipimo.
- **Kurundika WIP:** kuchanganya kuwa na shughuli na upitishaji na kurefusha nyakati za kuongoza.
- **Kuboresha kisichobana:** kuboresha hatua zisizobana na kuhamisha foleni kwingine.
- **Kuchanganya MTTR:** kuripoti "kupona" huku ukipima "kurekebisha," au kinyume chake.
- **Foleni zisizo na mipaka:** hakuna shinikizo-nyuma, kwa hiyo mfumo uliozidiwa unashuka kuwa kuporomoka badala ya kumwaga mzigo.
- **Wastani kama upeo:** kubuni kwa wastani na kupigiwa simu na mkia.

## Kielelezo cha ukomavu

- **Ngazi ya 1, Kuanzisha:** Foleni (tiketi, kazi, ujumbe, usambazaji) hazisimamiwi na ni za kuitikia; uwezo unakisiwa; matumizi yanaendesha popote mzigo unapotua; matatizo ya ucheleweshaji yanaishtua timu na kuzimwa moto baada ya tukio.
- **Ngazi ya 2, Kuendeleza:** Timu chache zinakusanya vipimo vya msingi (upitishaji, wastani wa kusubiri) lakini zinavisoma kama wastani na kuvitumia bila uthabiti; baadhi ya vikundi vinaweka kikomo cha WIP au kuacha nafasi ya ziada huku vingine vikiendesha kwa joto; hakuna nukuu ya pamoja, kwa hiyo mazoea hayasafiri kuvuka timu.
- **Ngazi ya 3, Kusawazisha:** Nukuu ya pamoja (λ, μ, ρ, muda wa kuongoza) imeandikwa na kutekelezwa shirika zima; vikomo vya WIP na malengo ya nafasi ya ziada ya matumizi yamewekwa kwa makusudi kwa kila mfumo unaojali ucheleweshaji; MTTR kadhaa zinatofautishwa; foleni zenye mipaka zenye shinikizo-nyuma ni chaguo-msingi kuvuka huduma.
- **Ngazi ya 4, Kusimamia:** Foleni zinapimwa na kudhibitiwa dhidi ya vipimo vya msingi: kasi ya kufika, kasi ya huduma, matumizi, ucheleweshaji wa mkia (p95/p99), na muda wa kuongoza vinafuatiliwa kwa malengo yaliyofafanuliwa na SLO; kina cha foleni, muda wa kuisha, na nafasi ya ziada vinatokana na Sheria ya Little badala ya kukisiwa; kutokujiunga, kujiondoa, na kasi ya kuruka vinahesabiwa ili mzigo uliotolewa utofautishwe na uliohudumiwa; maamuzi ya uwezo yanapitiwa kwa ushahidi huu, si hisia.
- **Ngazi ya 5, Kuratibu:** Mtiririko unaundwa kielelezo mfululizo kama foleni ya foleni; vizuizi vinatambuliwa na kupunguzwa kama mazoea endelevu; uwezo, SLO, na shinikizo-nyuma vinajirekebisha kwa mahitaji na tofauti zinazohama; vipimo vya foleni vinafungwa moja kwa moja na DORA na KPI za biashara, na shirika linasawazisha upya uwezo kuvuka mtiririko mzima mzigo na picha ya hatari zinapobadilika.

## Mawazo ya kujadili

1. Mifumo yenu inayojali ucheleweshaji inaendesha kwa matumizi gani kweli, na mwamba wake uko wapi?
2. Tumia Sheria ya Little kwenye mrundikano wenu wa sasa: WIP ÷ upitishaji wenu unadokeza muda gani wa kuongoza, na je, unalingana na uhalisia?
3. Foleni zenu zipi zinahesabu kimya "kuruka" (kuachwa, kukataliwa) kana kwamba zilihudumiwa?
4. Wapi kupunguza WIP kungefupisha muda wa kuongoza kwa bei nafuu zaidi kuliko kuongeza uwezo?
5. Hatua ipi katika mtiririko wenu wa wazo-hadi-uzalishaji ndio kizuizi halisi, na je, maboresho yenu yanalenga huko?
6. Dashibodi zenu zinaonyesha wastani ambapo mkia ndio unaokuumiza kweli?

## Mambo muhimu ya kukumbuka

- Foleni za wateja, mbao za kanban, foleni za ujumbe, na mabomba ya usambazaji yote ni foleni zinazotawaliwa na sheria zilezile.
- **Sheria ya Little (κ = λτ)** inaegemeza upangaji wa mtiririko: muda wa kuongoza = WIP ÷ upitishaji.
- Matumizi na muda wa kusubiri ni **visivyo na mstari**: tayarisha nafasi ya ziada; asilimia 15 ya mwisho ndiyo ghali zaidi.
- Fuatilia picha kamili: kufika, huduma, mafanikio, **kushindwa na kuruka**, na kusubiri; usiruhusu kuachwa kufichwa.
- Unda kielelezo cha michakato kama **foleni ya foleni** na urekebishe **kizuizi**, si kazi ya kujishughulisha.
- Vipimo vya foleni vinalingana moja kwa moja na vipimo vya **DORA/mtiririko** na **SLI/SLO** (sura za 11.1, 11.2, 9.1), vikiupa shirika zima lugha moja ya uwezo na mtiririko.

## Marejeo na usomaji zaidi

- Bob Wescott, *Seven Insights into Queueing Theory* (and *The Every Computer Performance Book*).
- John D. C. Little, "A Proof for the Queuing Formula L = λW" (1961): Little's Law.
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate*: flow-based DORA metrics that align with queue KPIs.
- Donald Reinertsen, *The Principles of Product Development Flow*: queues, batch size, and WIP economics.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability*: Little's Law applied to kanban.
- Joel Parker Henderson, *Queueing Theory*: notation, KPIs, and queue-of-queues (github.com/joelparkerhenderson/queueing-theory).
- Dan Slimmon, "The most important thing to understand about queues" (2016).
- Wikipedia: "Queueing theory," "M/M/1 queue," "Little's law," "Markov chain."
