# 9.2 Uonekanaji na telemetry

## Muhtasari na msukumo

[Telemetry](https://en.wikipedia.org/wiki/Telemetry) ni data ambayo mfumo hutoa kuhusu tabia yake wenyewe: vipimo, kumbukumbu, nyayo, na matukio yanayokusanywa kutoka programu inayoendesha. Ufuatiliaji hujibu maswali ambayo tayari ulijua kuuliza kutoka telemetry hiyo. Diski imejaa? Kiwango cha makosa kiko juu ya kizingiti? Huduma iko hewani? [Uonekanaji](https://en.wikipedia.org/wiki/Observability_(software)) ni mpana zaidi. Ni uwezo wa kuuliza maswali mapya kuhusu hali ya ndani ya mfumo kutoka nje, bila kusafirisha msimbo mpya, ili uweze kuelewa tabia ambayo hukuitarajia kamwe. Mifumo inapokua kuwa usanifu uliosambazwa, wa [huduma ndogo](https://en.wikipedia.org/wiki/Microservices), na [unaoendeshwa na matukio](https://en.wikipedia.org/wiki/Event-driven_architecture), kushindwa kunakoumiza zaidi ni kule ambako hakuna aliyetarajia, na uonekanaji ndio unaokuwezesha kukutatua. Ufuatiliaji unakuambia kwamba kuna kitu kibaya. Uonekanaji unakusaidia kugundua kwa nini.

Kwa timu kubwa, tofauti hii ni ya kuamua. Ungeweza kuelewa monolith kwa kusoma kumbukumbu kwenye mashine moja. Jukwaa la kisasa linavuka mamia ya huduma, timu nyingi, kanda kadhaa, na utegemezi wa watu wengine, ambapo ombi moja la mtumiaji linaweza kugusa makumi ya vijenzi. Hakuna mtu mmoja anayeshikilia mfumo mzima kichwani. Telemetry ya pamoja, yenye ubora wa juu inakuwa tishu ya kuunganisha inayomruhusu mhandisi yeyote kufuata ombi kuvuka mipaka, kuoanisha dalili kuvuka huduma, na kufikiri kuhusu mfumo ambao hakuna anayeumiliki kikamilifu. Bila hiyo, matukio yanachelewa, lawama zinarushwa kati ya timu, na chanzo cha tatizo kinabaki kimefichwa.

Mifumo ya mashirika makubwa na serikali huinua dau kwa uzingatiaji, uwezo wa kukaguliwa, na uwajibikaji wa umma. Wadhibiti wanaweza kuhitaji ushahidi wa nani alifikia nini na lini. Timu za usalama zinahitaji telemetry kugundua uvamizi. Huduma zinazowakabili raia lazima zionyeshe zinatimiza ahadi zao za utendaji zilizochapishwa. Uonekanaji mzuri unahudumia yote haya kwa wakati mmoja: ni zana ya kihandisi, kidhibiti cha usalama, na utaratibu wa uwajibikaji kwa pamoja. Kusawazisha kwenye upimaji wazi kunaepuka kufungwa kwa mawakala wa umiliki wa muuzaji mmoja, jambo la umuhimu mkubwa mifumo inapohitaji kudumu miongo na kunusurika mizunguko ya ununuzi.

*Tazama pia:* sura ya 9.1 (uhandisi wa kutegemewa wa tovuti na SLO), sura ya 9.3 (usimamizi wa matukio), na sura ya 3.3 (mifumo iliyosambazwa).

## Kanuni kuu

- **Pima kwa maswali yasiyojulikana.** Buni telemetry ili uweze kuchunguza kushindwa kwa riwaya, zaidi ya kule ulikotabiri.
- **Nguzo tatu, hadithi moja.** Vipimo, kumbukumbu, na nyayo ni mitazamo inayokamilishana; thamani yake huzidishwa zikiunganishwa, si zikitengwa.
- **Panga kila kitu.** Telemetry iliyopangwa, inayosomeka na mashine ni bora kuliko maandishi huru ambayo binadamu pekee wanaweza kuyasoma.
- **Unganisha kwa vitambulisho vya pamoja.** Vitambulisho vya nyayo na maombi vinavyosambazwa kila mahali vinakuruhusu kushona tukio moja kuvuka huduma.
- **Tahadharisha kwa dalili, si sababu.** Waite binadamu kwa matatizo yanayoonekana kwa mtumiaji; acha dashibodi na uchunguzi ufichue sababu ya msingi.
- **Kila mwito lazima utekelezeke.** Tahadhari isiyohitaji hatua ya binadamu ni kelele inayomomonyoa uaminifu na kusababisha uchovu.
- **Kardinalitii ya juu ni kipengele.** Uwezo wa kugawanya kwa mtumiaji, ombi, kanda, na toleo ndio unaofanya utatuzi kwenye uzalishaji uwezekane.
- **Miliki upimaji wako.** Sawazisha kwenye telemetry wazi, isiyoegemea muuzaji ili udhibiti data yako na uweze kubadilisha backend.

## Mapendekezo

### Jenga juu ya nguzo tatu na zaidi

**Vipimo** ni mfululizo wa wakati wa kinumeri, nafuu kuhifadhi na bora kwa dashibodi, mienendo, na vizingiti vya tahadhari. **Kumbukumbu** ni rekodi tofauti zenye muhuri wa wakati za matukio, tajiri kwa maelezo na muhimu kwa uchunguzi wa kiuchunguzi. **[Nyayo](https://en.wikipedia.org/wiki/Tracing_(software))** hufuata ombi moja linaposafiri kupitia huduma, zikionyesha ucheleweshaji na utegemezi kuvuka grafu ya miito iliyosambazwa. Zaidi ya hizi, fikiria **matukio** (mabadiliko ya hali yenye maana kama usambazaji), **wasifu** (mahali msimbo unapotumia CPU na kumbukumbu), na **[ufuatiliaji wa watumiaji halisi](https://en.wikipedia.org/wiki/Real_user_monitoring)** wa uzoefu halisi wa mteja. Hakuna nguzo moja ya kutosha peke yake. Lengo ni kuhama kwa urahisi kati yake wakati wa uchunguzi.

### Sawazisha kwenye OpenTelemetry na kumbukumbu zilizopangwa

Pokea [OpenTelemetry](https://en.wikipedia.org/wiki/OpenTelemetry) kama kiwango kisichoegemea muuzaji cha kuzalisha na kukusanya vipimo, kumbukumbu, na nyayo. Inatenganisha upimaji na backend ya uchambuzi, ili uweze kubadilisha wauzaji bila kupima upya mamia ya huduma. Sifa hiyo ni muhimu kwa mifumo ya muda mrefu ya mashirika makubwa na serikali. Toa kumbukumbu kama rekodi zilizopangwa (kwa mfano JSON) zenye majina ya sehemu thabiti kwa muhuri wa wakati, ukali, huduma, na vitambulisho. Sambaza kitambulisho cha ufuatiliaji au uhusiano kutoka ukingoni kupitia kila mwito wa chini ya mkondo, na ukijumuishe kwenye kila mstari wa kumbukumbu na mfano wa kipimo, ili nguzo tatu ziungane kiotomatiki.

### Buni tahadhari kwa utekelezekaji na kelele ndogo

Falsafa yako ya tahadhari huamua kama simu ya dharura ni endelevu. Tahadharisha hasa kwa dalili ambazo watumiaji wanahisi, zilizoonyeshwa kama kasi za kuteketeza za SLO ([lengo la kiwango cha huduma](https://en.wikipedia.org/wiki/Service-level_objective)). Pigia simu unapoteketeza bajeti yako ya makosa (upungufu unaoruhusiwa kutoka lengo hilo) haraka vya kutosha kuivunja, ukitumia tahadhari za kasi ya kuteketeza za madirisha mengi kusawazisha ugunduzi wa haraka dhidi ya kengele za uongo. Hifadhi kupiga simu kwa matatizo yanayohitaji hatua ya haraka ya binadamu, na elekeza kila kitu kingine kwenye tiketi au dashibodi. Futa tahadhari zinazowaka bila kuhitaji hatua bila huruma, kwa sababu uchovu wa tahadhari ni sababu kuu ya matukio halisi kukosekana na simu ya dharura kuchosha. Kila tahadhari iunganishwe na kitabu cha mwongozo.

### Unda kielelezo cha afya kwa dashibodi na ufuatiliaji wa SLO

Jenga dashibodi kuzunguka kielelezo wazi cha afya, si ukuta wa kila kipimo ulicho nacho. Mfumo mzuri wa kuanzia ni "ishara nne za dhahabu": ucheleweshaji, trafiki, makosa, na ujazo. Unda dashibodi za kiwango cha huduma zinazoonyesha hali ya SLO na bajeti ya makosa iliyobaki kwa mtazamo mmoja, pamoja na dashibodi za kiwango cha juu zinazoiga afya ya mfumo mzima na ya safari za watumiaji. Zipange kwa makusudi, kwa sababu dashibodi zinazoonyesha kila kitu haziwasilishi chochote. Ziweke karibu na tahadhari na vitabu vya mwongozo, ili waitikiaji wasonge haraka kutoka ishara hadi muktadha hadi hatua.

### Wezesha utatuzi kwenye uzalishaji kwa kardinalitii ya juu

Matatizo magumu zaidi ya uzalishaji hupiga kipande finyu: mteja mmoja, kanda moja, toleo moja la API, aina moja ya kifaa. Kuyachunguza unahitaji telemetry ya **kardinalitii ya juu** (wingi wa thamani tofauti), yaani uwezo wa kupanga na kuchuja kwa sehemu zenye thamani nyingi tofauti kama kitambulisho cha mtumiaji au ombi. Matukio mapana, yenye sifa nyingi yanayobeba vipimo vingi kwa kila rekodi yanakuruhusu kuuliza maswali yoyote baada ya tukio. Weka kardinalitii ya kutosha na uaminifu wa sampuli kutenga yaliyotoka nje ya kawaida, na pendelea nyayo zilizounganishwa na mifano ili kuruka kwenye kipimo kukupeleke moja kwa moja kwenye maombi ya polepole yanayowakilisha.

### Simamia gharama, uhifadhi, na sampuli

Kiasi cha telemetry hukua na mfumo na kinaweza kugeuka gharama kubwa. Weka sera za uhifadhi kwa daraja la data: weka data ya ubora wa juu kwa muda mfupi na jumla kwa muda mrefu zaidi. Tumia sampuli za busara kwa nyayo, zilizoelekezwa kuhifadhi makosa na maombi ya polepole, ili ushikilie mkia wa kuvutia bila kulipia kila mafanikio ya kawaida. Pitia matumizi yako ya telemetry mara kwa mara, kwa sababu gharama zisizosimamiwa za uonekanaji zinaweza kushindana na miundombinu inayoonekana.

## Mabadilishano: faida na hasara

| Uamuzi | Faida | Hasara |
|---|---|---|
| Matukio ya kardinalitii ya juu | Utatuzi wenye nguvu, uliza chochote | Gharama ya juu ya hifadhi na hoja |
| Sampuli kali | Gharama ndogo, kelele ndogo | Inaweza kukosa matukio adimu |
| Tahadhari za msingi wa dalili | Miito michache, inayotekelezeka | Inahitaji SLO nzuri ili ifanye kazi vizuri |
| Kiwango cha OpenTelemetry | Hakiegemei muuzaji, kinahamishika | Juhudi ya uhamishaji, zana zinazokomaa |
| Uhifadhi mrefu wa kumbukumbu | Uchunguzi bora na ukaguzi | Gharama ya hifadhi, mfiduo wa faragha |

Maamuzi ya uonekanaji hushuka kwenye mvutano kati ya uaminifu na gharama. Kunasa kila kitu kwa ubora kamili kunakupa mtazamo kamilifu wa nyuma, lakini kwa ukubwa ni ghali kupita kiasi. Ukikata kwa ukali unaokoa fedha, lakini unaweza kutupa rekodi moja ambayo ingeeleza kukatika. Sampuli na madaraja ya uhifadhi ndio jinsi timu zilizokomaa zinavyotembea mstari huu, zikihifadhi makosa na yaliyotoka nje ya kawaida huku zikipunguza data ya kawaida. Mabadilishano ya tahadhari ni kati ya unyeti na kelele: tahadhari nyingi mno husababisha uchovu na matukio kukosekana, chache mno huacha matatizo yakioza. Tahadhari za msingi wa dalili zinazoendeshwa na SLO hutatua mengi ya haya, lakini tu ikiwa mna SLO zenye maana.

## Maswali ya kujadili na timu yako

1. **Mpango wenu wa kuhamisha huduma za urithi hadi OpenTelemetry ni upi, na mnaepukaje kulipia mikusanyiko miwili ya upimaji wakati wa mpito?** Upimaji usioegemea muuzaji ni sifa inayokuruhusu kubadilisha backend bila kupima upya mamia ya huduma, na ni muhimu zaidi kwa mifumo ya muda mrefu ya mashirika makubwa na serikali inayodumu kuliko mkataba wowote wa muuzaji. Uhamishaji ndipo nia njema zinapokwama: maeneo yaliyopimwa nusu huacha mapengo hasa ombi linapovuka kutoka huduma mpya hadi ya zamani, likivunja ufuatiliaji wa mwanzo hadi mwisho. Leta orodha kwenye mjadala: huduma zipi zinatoa data ya wakala wa umiliki, zipi zinatoa OpenTelemetry, na wapi muktadha wa ufuatiliaji unapotea mpakani. Amua mfuatano unaofuata njia halisi za maombi badala ya chati za shirika, na weka bajeti kwa dirisha mnapoendesha vikusanyaji viwili. Jibu linaamua kama mnamiliki telemetry yenu kweli au mnabaki mmefungwa kwa mawakala wa muuzaji mmoja.

2. **Lini mlikagua mwisho kila tahadhari kwa utekelezekaji, na miito mingapi mwezi uliopita ilikuwa haihitaji hatua ya binadamu?** Uchovu wa tahadhari ni sababu kuu ya matukio halisi kukosekana na simu ya dharura kuchosha, kwa hiyo mwito usiohitaji hatua si kelele isiyo na madhara, unamomonyoa kikamilifu mwitikio mnaoutegemea. Leta ushahidi: vuta miito ya mwezi uliopita, weka alama kila mmoja kama uliotendewa kazi au uliopuuzwa, na uhesabu ni mingapi ilihusishwa na kitabu cha mwongozo. Kwa timu kubwa inayovuka huduma nyingi, tahadhari zenye kelele kutoka timu moja hupunguza hisia za simu ya dharura ya pamoja kwa kila mtu. Weka kiwango kwamba kila mwito unaunganishwa na kitabu cha mwongozo na unafungwa kwa kasi ya kuteketeza ya SLO, kisha futa mengine bila huruma. Matokeo ya ukaguzi huu yanapaswa kupunguza moja kwa moja kiasi chenu cha miito na kuwaambia huduma zipi hazina SLO yenye maana nyuma ya tahadhari zake.

3. **Mkakati wenu wa sampuli za nyayo ni upi, na mna uhakika kiasi gani kwamba unahifadhi makosa na mkia wa polepole?** Kiasi cha telemetry hukua na mfumo na gharama za uonekanaji zisizosimamiwa zinaweza kushindana na miundombinu inayoonekana, kwa hiyo mtafanya sampuli, na swali ni kama mnafanya sampuli kwa busara. Kuondoa kardinalitii au kufanya sampuli bila mwelekeo huondoa hasa rekodi zinazohitajika kutatua matatizo finyu yanayompiga mteja mmoja, kanda moja, au toleo moja la API. Leta madaraja yenu ya sasa ya uhifadhi na kanuni za sampuli: mnaelekeza kuhifadhi makosa na maombi ya polepole, mkitumia nyayo zilizounganishwa na mifano ili kuruka kwenye kipimo kuelekeze kwenye ombi la polepole linalowakilisha? Kwa mifumo iliyokaguliwa na inayofungwa na faragha, patanisha uhifadhi na kanuni za kupunguza data ili msihodhi data ya kibinafsi ili kutatua. Jibu linaweka mahali mnapotumia bajeti ya telemetry na kama kukatika kwenu kugumu kijacho kunaelezeka au ni fumbo.

4. **SLO zenu zipi ni ahadi halisi za safari ya mtumiaji, na zipi ni vipimo mbadala ambavyo hakuna nje ya timu mmiliki anayeviamini?** Tahadhari za msingi wa dalili hufanya kazi tu dalili zinapolingana na vitu ambavyo watumiaji wanahisi kweli, kwa hiyo tahadhari iliyofungwa kwenye kizingiti cha CPU au lengo la upatikanaji lililobuniwa huwapigia watu simu kwa matatizo ambayo huenda hayajalishi huku ikibaki kimya kwa yale yanayojali. Kwa shirika kubwa, SLO pia ni mkataba unaoziruhusu timu huru kushiriki zamu moja ya simu ya dharura bila kujadili ukali upya katika kila tukio. Leta orodha ya sasa ya SLO, safari ya mtumiaji ambayo kila lengo linakusudiwa kulinda, na ukiukaji wa robo iliyopita pamoja na kama wateja walilalamika kweli. Katika mazingira ya mashirika makubwa na serikali, funga SLO zinazoonekana zaidi kwa ahadi za utendaji zilizochapishwa ambazo huduma inashikiliwa nazo, ili ishara ileile ya kasi ya kuteketeza inayomwita mhandisi iwe pia ushahidi mnaouonyesha kwa mdhibiti au chombo cha usimamizi. Mjadala unapaswa kustaafisha vipimo mbadala na kuwaachia orodha fupi ya malengo ambayo mtu asiye mhandisi angeyatambua kama ahadi kwa watumiaji.

5. **Nani anamiliki utawala wa data ya telemetry, na mnaweza kuthibitisha kwamba data ya kibinafsi imefichwa kabla ya kutua kwenye backend yenu ya uonekanaji?** Matukio ya kardinalitii ya juu na uhifadhi mrefu wa kumbukumbu ndio vipengele vinavyofanya utatuzi uwezekane, na ndivyo vinavyogeuza hifadhi ya uonekanaji kuwa nakala isiyosimamiwa ya data ya kibinafsi ya watumiaji wenu. Mvuto unaoshindana ni halisi: wahandisi wanataka sifa tajiri zaidi na uhifadhi mrefu zaidi, huku faragha na sheria vikitaka kupunguza data na maisha mafupi. Leta ramani ya mtiririko wa data inayoonyesha sehemu zipi hubeba data ya kibinafsi au nyeti, wapi kuficha au kutoa tokeni kunatokea kwenye bomba, na madaraja yenu ya uhifadhi ni yapi kwa kila daraja la data. Kwa mifumo inayodhibitiwa na ya umma, taja mmiliki anayewajibika, patanisha uhifadhi na msingi halali wa kisheria na kanuni za kupunguza data mnazofanya kazi chini yake, na uwe tayari kumwonyesha mkaguzi kwamba ufikiaji wa telemetry yenyewe unaandikwa na kudhibitiwa. Jibu linaamua kama jukwaa lenu la uonekanaji ni mali au uvunjaji wa kudumu unaosubiri kugunduliwa.

6. **Tukio linapovuka huduma za timu kadhaa, telemetry yenu inamruhusu mwitikiaji mmoja kufuata ombi mwanzo hadi mwisho, au njia inavunjika kila mpaka wa umiliki?** Ahadi nzima ya telemetry iliyounganishwa, yenye vitambulisho vinavyosambazwa ni kwamba mhandisi mmoja anaweza kufikiri kuhusu mfumo ambao hakuna anayeumiliki kikamilifu, na ahadi hiyo inaporomoka hasa mpakani ambapo muktadha wa ufuatiliaji unapotea au timu mbili zinatumia vitambulisho na zana zisizooana. Pima mvuto kuelekea uhuru wa timu katika kuchagua zana za uonekanaji dhidi ya gharama ya pamoja ya eneo lililogawanyika ambapo kila makabidhiano ni mwisho usio na njia wakati wa kukatika. Leta ratiba ya tukio la hivi karibuni la timu mbalimbali na uweke alama mahali mwitikiaji alipopoteza uzi, pamoja na orodha ya huduma zipi zinasambaza kitambulisho cha uhusiano cha pamoja na zipi hazifanyi. Kwa biashara kubwa au jukwaa la serikali lililokusanywa kutoka wauzaji wengi na mifumo ya muda mrefu, amua kiasi cha kuamuru kati, kiwango cha pamoja cha muktadha wa ufuatiliaji na mpango wa pamoja wa vitambulisho, dhidi ya kile mnachowaachia timu, kwa sababu vijenzi mnavyonunua upya kwa miongo bado vinapaswa kufanya kazi pamoja kwenye ombi lilelile. Jibu linawaambia kama tukio lenu lijalo la timu nyingi litakuwa uchunguzi ulioratibiwa au duru ya kunyoosheana vidole.

## Mtazamo wa sekta

**Kampuni changa.** Ukiwa na huduma chache na bila mikono ya ziada, pima kwa OpenTelemetry tangu siku ya kwanza na usafirishe kumbukumbu za JSON zilizopangwa zinazobeba kitambulisho kimoja cha ombi mwanzo hadi mwisho. Uwekezaji huo mdogo hugeuza "programu ni polepole" kuwa nyayo unazoweza kuzisoma, na unakuweka huru kuhama kutoka daraja la bure hadi backend ya kulipia baadaye bila kupima upya. Ruka dashibodi za kina na mitambo ya SLO hadi uwe na watumiaji ambao uzoefu wao unaweza kuupima kweli.

**Biashara ndogo.** Huna mtaalamu wa uonekanaji na bajeti ni finyu, kwa hiyo egemea backend inayosimamiwa ambapo upimaji, hifadhi, na dashibodi vinakuja pamoja badala ya kukusanya mrundikano wako. Uamuzi wa kununua-dhidi-ya-kujenga unapendelea kununua karibu kila mara hapa; umakini wako adimu unatumika vizuri zaidi kwa tahadhari mbili au tatu za ishara za dhahabu zinazokuambia huduma imeanguka kuliko kuendesha bomba la telemetry. Weka kikomo kigumu cha uhifadhi ili gharama ya telemetry isizidi kimyakimya miundombinu inayoitazama.

**Biashara kubwa.** Kazi ni utawala kuvuka timu nyingi: kiwango cha pamoja cha OpenTelemetry, mpango wa pamoja wa vitambulisho vya uhusiano, na dashibodi zilizopangwa za SLO ili mwitikiaji mmoja afuate ombi kuvuka makumi ya huduma. Simamia telemetry kama kituo cha gharama chenye madaraja ya uhifadhi na sera ya sampuli, sawazisha tahadhari kwenye kasi za kuteketeza za SLO ili kuweka simu ya dharura ya pamoja endelevu, na futa tahadhari zenye kelele kati ili uchovu wa timu moja usipunguze hisia za kila mtu. Chukulia safu ya upimaji kama miundombinu isiyoegemea muuzaji inayodumu kuliko mkataba wowote wa backend.

**Serikali.** Kanuni za ununuzi, uwazi, na uwajibikaji wa umma huumba muundo. Sawazisha kwenye upimaji wazi ili mfumo unaotarajiwa kuendesha miongo upitie ununuzi upya na wauzaji tofauti bila kushikiliwa mateka na mawakala wa umiliki, na dai uwezo huo wa kuhamishika kwenye mkataba. Tumia kumbukumbu za ukaguzi zilizopangwa kuonyesha nani alifikia rekodi ipi na lini, ficha au toa tokeni data ya kibinafsi kabla haijafika kwenye hifadhi ya telemetry, na patanisha uhifadhi na sheria ya kupunguza data. Chapisha dashibodi za SLO kwa huduma zinazowakabili raia ili ishara zilezile wanazotazama wahandisi wenu ziwe ushahidi unaoonekana wa ahadi mnazoshikiliwa nazo.

## Mifano

**Kampuni changa.** Kampuni changa ya watu wanne inasafirisha backend ya simu na inaendelea kupata malalamiko hafifu ya "programu ni polepole" ambayo haiwezi kuyazalisha. Timu inaongeza OpenTelemetry kwenye huduma zake chache na kubadilisha kwenda kumbukumbu za JSON zilizopangwa zenye kitambulisho cha ombi kinachobebwa kutoka programu kupitia kila hatua. Ripoti inayofuata ya polepole inatatuliwa ndani ya dakika: nyayo moja inaonyesha faharasa ya hifadhidata iliyokosekana kwenye jedwali la oda chini ya hoja maalumu. Kwa sababu walichagua upimaji wazi mapema, baadaye wanahama kutoka daraja la bure hadi backend ya kulipia bila kupima upya chochote.

**Biashara kubwa.** Jukwaa kubwa la biashara mtandaoni linapima kila huduma kwa OpenTelemetry, likisambaza kitambulisho cha ufuatiliaji kutoka kivinjari cha mteja kupitia malipo, ghala, na usafirishaji. Mauzo yanaposhuka, mhandisi wa simu ya dharura anaanza kutoka tahadhari ya kasi ya kuteketeza ya SLO, anafungua ishara za dhahabu za dashibodi ya malipo, anaona ucheleweshaji ulioongezeka katika kanda moja, na kufuata nyayo ya mfano hadi mwito wa polepole wa hifadhidata katika huduma moja. Sifa za kardinalitii ya juu zinaonyesha tatizo limefungwa kwenye aina moja ya bidhaa, jambo linaloongoza marekebisho yaliyolengwa ndani ya dakika badala ya masaa.

**Serikali.** Huduma ya taifa ya afya inaendesha jukwaa la rekodi za wagonjwa chini ya kanuni kali za ukaguzi na faragha. Kumbukumbu zilizopangwa zinanasa nani alifikia rekodi ipi na lini, zikilisha ufuatiliaji wa usalama na ripoti za uzingatiaji, huku sehemu zinazotambulisha mtu zikifichwa au kutolewa tokeni kwenye telemetry. Dashibodi za SLO za umma zinaonyesha upatikanaji na ucheleweshaji wa kuweka miadi kwa raia. Kwa kusawazisha kwenye upimaji wazi, wakala unaepuka kufungwa kwa umiliki kuvuka mfumo unaotarajiwa kuendesha miongo na kununuliwa upya na wauzaji tofauti katika maisha yake.

## Kesi ya biashara: sababu, ROI, na TCO

Faida kuu ya uonekanaji ni kushuka kwa kasi kwa muda wa kugundua na kutatua matukio. Kwa huduma ambayo kukatika ni ghali, kupunguza muda wa wastani wa kutatua kutoka masaa hadi dakika hulipia zana mara nyingi katika tukio moja kubwa. Uonekanaji pia huokoa muda wa kihandisi ambao ungetumika kukisia, kuzalisha hitilafu, na kubishana timu ipi ina kosa, na unafupisha mzunguko wa maoni unaoziwezesha timu kusafirisha kwa kujiamini. Thamani ya usalama na uzingatiaji ni halisi pia: telemetry ileile inasaidia kugundua uvamizi na ushahidi wa ukaguzi.

Jumla ya gharama ya umiliki inajumuisha juhudi ya upimaji, gharama za hifadhi na hoja za telemetry, na nidhamu ya kutenga ishara kutoka kelele. Gharama hizi zinaonekana na zinajirudia, jambo linalowavutia uongozi kuwekeza kidogo mno. Gharama ya kutopokea ni kubwa zaidi lakini ngumu kuona: kukatika kwa muda mrefu, matatizo ya utendaji yasiyotambuliwa, matukio ya usalama yanayogunduliwa kwa kuchelewa au kamwe, na wahandisi wanaochoka kwa tahadhari ambazo hawawezi kufanya chochote kuzihusu. Toa hoja kwa data halisi ya matukio. Onyesha muda wa kutatua na athari ya biashara ya kukatika kwa hivi karibuni, na ukadirie upungufu ambao telemetry bora ingeleta. Kuweka uonekanaji kama bima inayoharakisha pia utoaji, badala ya kituo cha gharama tupu, kunashinda hoja.

## Mifumo mibaya na mitego

- **Tahadharisha kwa kila kitu.** Kupiga simu kwa kila mkengeuko kunawafundisha waitikiaji kupuuza tahadhari, kwa hiyo matukio halisi yanapenya.
- **Miito ya msingi wa sababu.** Kutahadharisha kwa sababu za ndani badala ya dalili za mtumiaji kunajaza simu ya dharura kelele na kukosa kushindwa kwa riwaya.
- **Kumbukumbu zisizopangwa.** Kumbukumbu za maandishi huru ambazo haziwezi kuulizwa wala kuunganishwa zinalazimisha kutafuta kwa mkono polepole wakati wa matukio.
- **Nguzo tatu zilizotengwa.** Vipimo, kumbukumbu, na nyayo kwenye zana zisizounganishwa bila vitambulisho vya pamoja vinazuia kufuata tukio mwanzo hadi mwisho.
- **Kuenea kwa dashibodi.** Mamia ya dashibodi zisizopangwa yanamaanisha hakuna anayejua ipi inaonyesha kama mfumo una afya.
- **Kuporomoka kwa kardinalitii.** Kuondoa sehemu za kardinalitii ya juu kuokoa gharama kunaondoa hasa data inayohitajika kutatua matatizo finyu.
- **Kufungwa na muuzaji.** Mawakala wa umiliki kila mahali hufanya kubadilisha backend kuwa ghali kupita kiasi na kushikilia data yako mateka.

## Kielelezo cha ukomavu

**Ngazi ya 1, Kuanzisha.** Uonekanaji ni wa papo hapo na wa kuitikia. Ukaguzi wa msingi wa muda wa kufanya kazi na kumbukumbu zisizopangwa zinaishi kwenye mashine mmoja mmoja, utatuzi unamaanisha kuingia kwenye seva kutafuta, na hakuna telemetry ya pamoja. Tahadhari zina kelele, za msingi wa sababu, na mara nyingi hupuuzwa, kwa hiyo matukio halisi yanajitokeza kupitia malalamiko ya watumiaji badala ya ishara.

**Ngazi ya 2, Kuendeleza.** Mazoea ya msingi yanaonekana lakini yanatofautiana kwa timu. Baadhi ya huduma husukuma vipimo na kumbukumbu mahali pa kati, dashibodi chache na tahadhari za kizingiti zipo, lakini kumbukumbu zimepangwa nusu tu na nyayo hazipo au ni za sehemu. Uhusiano kuvuka huduma ni wa mkono, na kama mhandisi anaweza kufuata ombi mwanzo hadi mwisho kunategemea timu zipi zinahusika.

**Ngazi ya 3, Kusawazisha.** Upimaji umeandikwa na kutekelezwa kote shirikani. OpenTelemetry kuvuka huduma na kitambulisho cha ufuatiliaji au uhusiano kinachosambazwa, kumbukumbu zilizopangwa zenye majina thabiti ya sehemu, ufuatiliaji uliosambazwa, dashibodi zilizopangwa za ishara za dhahabu, na tahadhari za dalili za msingi wa SLO ndicho kiwango ambacho kila timu inafuata. Kila mwito unaunganishwa na kitabu cha mwongozo na unafungwa kwa SLO, na simu ya dharura ni endelevu badala ya chanzo cha uchovu.

**Ngazi ya 4, Kusimamia.** Eneo la uonekanaji lenyewe linapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Mnafuatilia ufunikaji wa upimaji na kiwango cha usambazaji wa muktadha wa ufuatiliaji kuvuka huduma, sehemu ya miito iliyotendewa kazi dhidi ya iliyopuuzwa, muda wa wastani wa kugundua na kutatua, mafanikio ya SLO na kuteketeza bajeti ya makosa, na gharama ya telemetry kwa kila huduma dhidi ya bajeti. Mapengo na kelele za tahadhari zinashushwa kwa data kuelekea malengo wazi, uaminifu wa sampuli unathibitishwa ili rekodi za makosa na mkia wa polepole zinusurike, na maamuzi ya kwenda au kutokwenda kuhusu ufunikaji na uhifadhi yanafanywa kwa ushahidi badala ya maoni.

**Ngazi ya 5, Kuratibu.** Uonekanaji unaboreshwa mfululizo na kuunganishwa kuvuka shirika. Telemetry ya kardinalitii ya juu, tajiri kwa matukio inawezesha uchunguzi wa papo hapo wa kipande chochote, tahadhari zinaendeshwa na kasi ya kuteketeza ya SLO kwa kelele ndogo, na sampuli na uhifadhi vinajirekebisha kwa gharama na hatari zinazobadilika. Telemetry inalisha upangaji wa uwezo, ugunduzi wa usalama, na maamuzi ya bidhaa kama jambo la kawaida, na jukwaa linarekebisha upya ishara, bajeti, na ufunikaji wake mfumo, picha ya tishio, na wajibu wa udhibiti unavyohama.

## Mawazo ya kujadili

- Usawa sahihi uko wapi kati ya uaminifu wa telemetry na gharama kwa huduma zenu muhimu zaidi?
- Mnaamuaje nini kinastahili mwito dhidi ya tiketi dhidi ya kipengele cha dashibodi tu?
- Mkakati wenu wa kusambaza vitambulisho vya uhusiano kuvuka timu zisizoshiriki msingi wa msimbo wala mzunguko wa matoleo ni upi?
- Mnahifadhije nguvu ya utatuzi ya kardinalitii ya juu huku mkitimiza mahitaji ya faragha na kupunguza data?
- Zana za uonekanaji ziamriwe kati au zichaguliwe kwa timu, na matokeo ni yapi kwa njia yoyote?
- Mngewaonyeshaje wakaguzi kwamba telemetry yenu ni kamili na inaonyesha uchezewaji?

## Mambo muhimu ya kukumbuka

- Ufuatiliaji hugundua matatizo yanayojulikana; uonekanaji unakuruhusu kuchunguza yasiyojulikana bila kusafirisha msimbo mpya.
- Vipimo, kumbukumbu, na nyayo vina thamani zaidi vikiunganishwa kupitia vitambulisho vya pamoja, si vikitengwa.
- Sawazisha kwenye OpenTelemetry na kumbukumbu zilizopangwa ili kubaki bila kuegemea muuzaji na kuhamishika kuvuka maisha marefu ya mfumo.
- Tahadharisha kwa dalili zinazoonekana kwa mtumiaji kupitia kasi za kuteketeza za SLO, fanya kila mwito utekelezeke, na futa kelele bila kuchoka.
- Panga dashibodi kuzunguka kielelezo wazi cha afya kama ishara za dhahabu badala ya kuonyesha kila kipimo.
- Telemetry ya kardinalitii ya juu, tajiri kwa matukio ndiyo inayofanya utatuzi wa matatizo finyu ya uzalishaji uwezekane.

## Marejeo na usomaji zaidi

- Charity Majors, Liz Fong-Jones, George Miranda, *Observability Engineering: Achieving Production Excellence*
- Cindy Sridharan, *Distributed Systems Observability*
- Betsy Beyer et al., *Site Reliability Engineering* (chapters on monitoring and alerting)
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud*
- OpenTelemetry project, specification and documentation (Cloud Native Computing Foundation)
- Google, *The Four Golden Signals* (Site Reliability Engineering, monitoring chapter)
