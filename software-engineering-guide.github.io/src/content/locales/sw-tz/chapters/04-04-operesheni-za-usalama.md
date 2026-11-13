# 4.4 Operesheni za usalama

## Muhtasari na msukumo

Kinga ni muhimu, lakini haitoshi kamwe. Wapinzani waliodhamiria, udhaifu mpya, na makosa ya kawaida ya binadamu yanamaanisha baadhi ya vitisho vitateleza kupita ulinzi wako. Operesheni za usalama ni nidhamu ya kuvipata haraka, kujibu vizuri, na kurudisha ulichojifunza kwenye ulinzi imara zaidi. Ndiyo tofauti kati ya tukio lililodhibitiwa ndani ya dakika na lile linaloota kwa miezi kabla mtu yeyote hajaona.

Katika shirika kubwa, operesheni za usalama lazima zifanye kazi kwa ukubwa na kasi. Maelfu ya huduma huzalisha bahari ya kumbukumbu. Mamia ya udhaifu mpya hufichuliwa kila wiki. Usambazaji haukomi kamwe. Operesheni za mkono, za kisanii haziwezi kuendana. Jibu ni kuweka usalama ndani ya bomba la utoaji ([DevSecOps](https://en.wikipedia.org/wiki/DevSecOps)), kuotomatisha ugunduzi na jibu, na kujenga misuli ya kushughulikia matukio kwa utulivu yanapotokea. Kwa serikali, operesheni za usalama pia hubeba wajibu wa kisheria: ratiba za lazima za kuripoti matukio, ufichuzi ulioratibiwa wa udhaifu, na ukali wa uchunguzi wa kidijitali unaoweza kustahimili uchunguzi wa kisheria.

Sura hii inashughulikia kuunganisha usalama kwenye bomba, kusimamia udhaifu na kupachika, kujibu matukio na kufanya uchunguzi wa kidijitali, kuendesha ugunduzi kupitia [SIEM](https://en.wikipedia.org/wiki/Security_information_and_event_management) na SOAR, na kuthibitisha ulinzi kupitia timu nyekundu na ya zambarau na [majaribio ya kupenya](https://en.wikipedia.org/wiki/Penetration_test).

## Kanuni kuu

- **Otomatisha ya kawaida.** Mashine zinashughulikia uchanganuzi, uhusiano, na jibu linalojirudia ili binadamu walenge busara.
- **Sukuma usalama kwenye bomba.** Majaribio na malango yanaishi katika [CI/CD](https://en.wikipedia.org/wiki/CI/CD) (ujumuishaji na utoaji endelevu), yakitoa maoni ya haraka mahali wahandisi tayari wanafanya kazi.
- **Dhania uvunjaji na jiandae.** Fanyia mazoezi jibu la tukio kabla hujalihitaji; tukio si wakati wa kuboresha papo hapo.
- **Pima na upunguze muda.** Muda wa wastani wa kugundua na muda wa wastani wa kujibu ndio vipimo vinavyojalisha zaidi.
- **Kujifunza bila lawama.** Kila tukio na karibu-kosa linakuwa somo linaloimarisha mfumo, si utafutaji wa mtu wa kuadhibu.
- **Thibitisha ulinzi kwa uadui.** Jaribu usalama wako jinsi washambulizi halisi wangefanya, kisha rekebisha wanachokipata.
- **Uhandisi wa ugunduzi ni bidhaa.** Chukulia ugunduzi kama msimbo: ulio kwenye udhibiti wa matoleo, unaojaribiwa, na kuboreshwa mfululizo.

## Mapendekezo

### Jenga DevSecOps ndani ya bomba

Unganisha majaribio ya kiotomatiki ya usalama moja kwa moja kwenye ujumuishaji na utoaji endelevu ili maoni yawafikie wahandisi ndani ya dakika:

- **[SAST](https://en.wikipedia.org/wiki/Static_application_security_testing)** (Static Application Security Testing) huchambua msimbo wa chanzo kwa mifumo yenye udhaifu unapowekwa.
- **[DAST](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)** (Dynamic Application Security Testing) huchunguza programu inayoendesha kwa dosari zinazoweza kutumiwa.
- **SCA** (Software Composition Analysis) huweka alama utegemezi wenye udhaifu unaojulikana.
- **Uchanganuzi wa IaC** hukagua miundombinu-kama-msimbo kwa usanidi usio salama kabla haujasambazwa.
- **Uchanganuzi wa siri** huzuia vitambulisho kuingia kwenye hazina.

Rekebisha zana hizi bila huruma kudhibiti matokeo ya uongo. Kichanganuzi kinacholia mbwa-mwitu hupuuzwa. Weka malango yanayotegemea hatari: zuia kwa matokeo makali, yenye imani ya juu, na ufuatilie mengine bila kusimamisha utoaji. Unataka ishara ya haraka, inayoaminika, si ukuta wa kelele.

### Simamia udhaifu na pachika kwa utaratibu

Mkondo thabiti wa udhaifu unadai mchakato wenye utaratibu, uliopewa vipaumbele, si hofu mpya kwa kila kichwa cha habari.

- Dumisha orodha sahihi ya mali ili ujue nini kinaweza kuathirika na udhaifu wowote.
- Weka kipaumbele urekebishaji kwa hatari halisi: changanya ukali, uwezekano wa kunyonywa (je, unanyonywa porini?), mfiduo, na umuhimu wa mali badala ya kupachika kwa alama ghafi tu.
- Fafanua na utekeleze **SLA za urekebishaji** (makubaliano ya kiwango cha huduma) kwa ngazi ya ukali, na upime ufuasi.
- Otomatisha kupachika pale unapoweza kwa usalama, hasa kwa miundombinu na utegemezi.
- Endesha programu ya **ufichuzi ulioratibiwa wa udhaifu** yenye njia wazi ya kupokea na, pale inapofaa, [zawadi kwa hitilafu](https://en.wikipedia.org/wiki/Bug_bounty_program), ili watafiti wa nje waripoti dosari kwa uwajibikaji badala ya kuzitupa hadharani.

### Jiandae na uendeshe jibu la tukio

Tukio linapotokea, mchakato uliofanyiwa mazoezi una thamani zaidi ya zana yoyote.

- Dumisha **mpango wa kujibu matukio** wenye majukumu yaliyofafanuliwa (kamanda wa tukio, kiongozi wa mawasiliano, wachunguzi), uainishaji wa ukali, na njia za kupandisha.
- Anzisha awamu wazi: **maandalizi, ugunduzi na uchambuzi, kudhibiti, kuondoa, kurejesha, na mapitio ya baada ya tukio.**
- Hifadhi ushahidi ipasavyo kwa **[uchunguzi wa kidijitali](https://en.wikipedia.org/wiki/Digital_forensics)**: nasa kumbukumbu, kumbukumbu ya mfumo, na picha za diski kwa mnyororo ulioandikwa wa utunzaji ili matokeo yashikilie kisheria na uchambuzi uwe sahihi.
- Panga **mawasiliano ya uvunjaji** mapema: nani anawaarifu wateja, wadhibiti, na umma, kwa ratiba gani, na ushiriki wa kisheria na uhusiano wa umma. Saa za udhibiti (mara nyingi saa 72 au chini) zinaanza kutiki wakati wa ugunduzi.
- Endesha **mazoezi ya mezani** mara kwa mara ili timu ijue mpango kabla ya mgogoro halisi, na ufanye mapitio ya baada ya tukio yasiyo na lawama yanayozalisha maboresho madhubuti.

### Endesha ugunduzi kwa SIEM na SOAR, na uhandisi ugunduzi

Kusanya ishara zako za usalama pamoja na utende juu yake kwa ukubwa.

- Tumia **SIEM** (Security Information and Event Management) kukusanya na kuhusisha kumbukumbu na matukio kutoka eneo zima, ukifichua mifumo ya kutia shaka.
- Tumia **SOAR** (Security Orchestration, Automation, and Response) kuotomatisha upangaji wa matokeo na vitabu vya mikakati ya jibu: kutajirisha tahadhari, kutenga wenyeji, kuzima vitambulisho, na kufungua kesi bila kusubiri binadamu kwa hatua za kawaida.
- Fanya **uhandisi wa ugunduzi**: chukulia kanuni za ugunduzi kama msimbo wenye matoleo, unaojaribiwa uliopangiliwa na mfumo kama [MITRE ATT&CK](https://en.wikipedia.org/wiki/MITRE_ATT%26CK), pima viwango vyake halisi vya ukweli na uongo, na boresha mfululizo ufikiaji wa mbinu halisi za wapinzani.
- Hakikisha uandishi kamili, usioweza kuchezewa wa kumbukumbu kuvuka programu na miundombinu; huwezi kugundua usichoandika kwenye kumbukumbu.

### Thibitisha ulinzi kwa timu nyekundu na ya zambarau na majaribio ya kupenya

Kujaribu ulinzi wako jinsi mshambulizi angefanya ndiyo njia pekee ya kujua unafanya kazi kweli.

- **Majaribio ya kupenya** hutoa tathmini iliyolengwa, ya nukta moja ya wakati ya mifumo mahususi, mara nyingi kwa uzingatiaji.
- **[Red teaming](https://en.wikipedia.org/wiki/Red_team)** huiga mpinzani halisi anayefuata malengo kuvuka mazingira yako, ikijaribu ugunduzi na jibu pamoja na kinga.
- **Purple teaming** huleta washambulizi (nyekundu) na watetezi (buluu) pamoja kwa ushirikiano ili kila shambulio la kuigwa liboreshe mara moja ugunduzi na vidhibiti, ikigeuza zoezi kuwa uwezo wa kudumu.
- Rudisha matokeo yote kwenye uhandisi wa ugunduzi, urekebishaji, na mafunzo.

## Mabadilishano: faida na hasara

| Uamuzi | Faida | Hasara |
|---|---|---|
| Malango yanayozuia ya bomba | Husimamisha masuala yanayojulikana kusafirishwa | Msuguano, matokeo ya uongo huchukiza timu |
| Uchanganuzi usiozuia | Msuguano mdogo, utoaji wa haraka | Masuala yanaweza kusafirishwa; inahitaji nidhamu kurekebisha |
| SOC ya ndani | Muktadha wa kina, udhibiti kamili | Ghali, ngumu kuajiri saa 24/7 |
| Ugunduzi/jibu linalosimamiwa | Ufikiaji wa saa 24/7, utaalamu unapohitajika | Muktadha mdogo, utegemezi wa muuzaji |
| Kupachika kwa kiotomatiki | Haraka, hufunga madirisha haraka | Hatari ya mabadiliko yanayovunja |
| Red teaming ya mara kwa mara | Uthibitisho halisi, hupata mapengo halisi | Ghali, inatumia rasilimali nyingi |
| Programu ya zawadi kwa hitilafu | Ugunduzi wa umati, ufikiaji mzuri | Mzigo wa kupanga, gharama za malipo, kelele |

Mvutano wa msingi ni kasi dhidi ya uhakikisho, na ufikiaji dhidi ya gharama. Malango yanayozuia na kupachika kwa kiotomatiki huongeza uhakikisho lakini huongeza msuguano na hatari. Mbinu zisizozuia husonga haraka lakini zinategemea kufuatilia. Ugunduzi wa saa nzima ni muhimu kwa ukubwa lakini ghali kujenga ndani, jambo linalosukuma mashirika mengi kuelekea mifumo mseto. Njia endelevu ni kuotomatisha ya kawaida yenye imani ya juu, kuhifadhi umakini wa binadamu kwa busara ya kweli, na kuendelea kurekebisha mizani kwa matokeo yaliyopimwa badala ya hofu.

## Maswali ya kujadili na timu yako

1. **SLA zenu za urekebishaji kwa ukali ni zipi, na nini kinazitekeleza kweli?** Mkondo thabiti wa udhaifu unahitaji mchakato wenye utaratibu, uliopewa vipaumbele, si hofu mpya kwa kila kichwa cha habari, na SLA kwa ngazi ya ukali ndivyo mnavyoendelea kuendana. Amua saa zenu (kwa mfano, muhimu ndani ya siku, makali ndani ya wiki) na, muhimu vilevile, jinsi mnavyopima ufuasi na nani anawajibika tarehe ya mwisho inapoteleza. Weka kipaumbele kwa hatari halisi, mkichanganya ukali na uwezekano wa kunyonywa porini, mfiduo, na umuhimu wa mali, badala ya kupachika kwa alama ghafi ya CVSS tu. Leta backlog yenu ya sasa ya matokeo wazi yaliyopangwa kwa umri na ukali, kwa sababu zile muhimu ambazo hazijapachikwa zilizo nje ya dirisha lake ndio ushahidi unaojalisha. SLA ikiwa haina utekelezaji wala mmiliki, ni tamanio, na uchanganuzi bila urekebishaji unajenga tu deni la ukaguzi na hisia ya uongo ya usalama.

2. **Tukio linapotokea saa nane usiku, nani ni kamanda wa tukio, na saa ya udhibiti inaanza kwa kasi gani?** Mchakato uliofanyiwa mazoezi una thamani zaidi ya zana yoyote, kwa hiyo mnahitaji majukumu yaliyotajwa (kamanda wa tukio, kiongozi wa mawasiliano, wachunguzi), viwango vilivyofafanuliwa vya ukali, na njia za kupandisha zilizoandikwa kabla ya mgogoro. Saa za udhibiti mara nyingi hukimbia saa 72 au chini na kuanza wakati wa ugunduzi, kwa hiyo amua mapema nani anawaarifu wateja, wadhibiti, na umma, na uthibitishe kisheria na uhusiano wa umma wapo kwenye mzunguko. Kuhifadhi ushahidi wa kidijitali kwa mnyororo ulioandikwa wa utunzaji lazima kutokee kabla mtu yeyote hajajenga upya mwenyeji ulioathirika, la sivyo mnapoteza uwezo wa kuelewa au kuthibitisha kilichotokea. Leta tarehe ya zoezi lenu la mwisho la mezani, kwa sababu likiwa la zamani au halijawahi, mpango wenu haujajaribiwa. Kwa timu za serikali, tarehe za mwisho za kisheria za kuripoti hufanya hili kuwa la lazima, kwa hiyo fanyia mazoezi njia ya arifa, si jibu la kiufundi tu.

3. **Ni vitendo vipi vya kawaida vya jibu mtakavyoiacha SOAR ichukue bila binadamu kwenye mzunguko?** Uotomatishaji ni kizidishi cha nguvu kinachoruhusu timu ndogo kufunika eneo kubwa, na kipimo kinachojalisha ni muda wa wastani wa kujibu, ambao vitabu vya mikakati vya kiotomatiki vinaweza kupunguza kutoka saa hadi dakika. Amua vitendo vipi vyenye imani ya juu (kutenga mwenyeji, kufuta kitambulisho, kufungua kesi) mnaviamini viendeshwe kiotomatiki, na vipi vinahitaji busara ya binadamu kwanza. Hatari ni matokeo ya uongo yanayochochea kitendo cha kusumbua, kwa hiyo funga uotomatishaji na ubora wa ugunduzi na urekebishe bila huruma, kwa sababu mfumo unaolia mbwa-mwitu huzimwa. Leta kiasi chenu cha sasa cha tahadhari na kiwango cha matokeo ya uongo, kwa sababu namba hizo zinawaambia vitabu vipi vya mikakati ni salama kuotomatisha leo. Kila hatua ya jibu ikisubiri binadamu, hamtaendana kwa ukubwa, na muda wa kukaa, unaoendesha gharama ya uvunjaji, utabaki juu.

4. **Matokeo gani ya bomba yanazuia toleo, yapi yanafuatiliwa tu, na nani anaweka kiwango cha matokeo ya uongo chini vya kutosha wahandisi bado wauamini lango?** Kichanganuzi kinacholia mbwa-mwitu hupuuzwa, na wahandisi wanapopoteza imani kwenye lango hushawishi liondolewe, kwa hiyo thamani ya DevSecOps inasimama juu ya ubora wa ishara badala ya ufikiaji ghafi. Mvutano ni halisi: zuia kidogo mno na msimbo wenye udhaifu unasafirishwa; zuia mno na unaongeza msuguano, kupunguza kasi ya utoaji, na kuchoma nia njema. Leta viwango vya ukweli na uongo vya kila kichanganuzi (SAST, DAST, SCA, IaC, na uchanganuzi wa siri), mara ngapi timu zinabatilisha au kukandamiza lango, na umri wa matokeo mnayoyafuatilia tu bila kurekebisha. Kwa shirika kubwa au chombo cha serikali kinachoendesha mabomba mamia, weka sera ya kuzuia-dhidi-ya-kufuatilia kati na uirekebishe kwa data, kwa sababu malango yanayotofautiana kiholela timu hadi timu huunda mapengo ya ukaguzi na hisia kwamba usalama ni wa kiholela.

5. **Mna uhakika kiasi gani kwamba ugunduzi wenu bado unafunika mbinu ambazo mshambulizi halisi angetumia, na nani anaumiliki kama msimbo uliojaribiwa, wenye matoleo?** Ugunduzi huoza kimyakimya mazingira yenu na wapinzani wenu wanavyobadilika, kwa hiyo seti ya kanuni iliyoonekana kamili mwaka jana inaweza kupoteza ufikiaji muda mrefu kabla ya tukio hatimaye kufichua pengo. Kuchukulia ugunduzi kama msimbo, ulio kwenye udhibiti wa matoleo, unaojaribiwa, na kuoanishwa na mfumo kama MITRE ATT&CK, ndiko kunakotenganisha mazoea ya kihandisi na rundo la tahadhari zilizopitwa, hata hivyo kunashindania muda adimu wa wachambuzi na upangaji wa moja kwa moja. Leta ramani yenu ya sasa ya ufikiaji wa ATT&CK, kiwango kilichopimwa cha ukweli na uongo cha ugunduzi wenu mkuu, na matokeo ya zoezi lenu la mwisho la purple-team, kwa kuwa majaribio ya ushirikiano ya nyekundu-na-buluu ndiyo njia ya haraka zaidi ya kuthibitisha ugunduzi gani unawaka kweli. Katika mazingira ya mashirika makubwa na serikali ambapo mfumo unaweza kuamriwa, funga kila ugunduzi na mmiliki aliyetajwa na mzunguko wa mapitio, kwa sababu ufikiaji ambao hakuna anayeudumisha ni ufikiaji mnaogundua mlipoteza baada ya uvunjaji tu.

6. **Mnajenga ugunduzi na jibu ndani, mnanunua ugunduzi na jibu linalosimamiwa, au kuchanganya, na mmepima gharama ya ufikiaji wa saa nzima wa kweli?** Muda wa kukaa unaendesha gharama ya uvunjaji, kwa hiyo saa zisizofunikwa (usiku, wikendi, sikukuu) ndizo hasa mvamizi asiyegunduliwa anapofanya madhara zaidi, hata hivyo kuajiri kituo cha operesheni za usalama cha saa 24/7 ndani ni ghali na ngumu kudumisha. Biashara ni muktadha na udhibiti dhidi ya gharama na kasi hadi ufikiaji: timu ya ndani inajua eneo lenu kwa kina lakini ni polepole na ghali kujenga, wakati mtoa huduma anayesimamiwa anatoa utaalamu wa papo hapo saa nzima kwa bei ya muktadha mwembamba na utegemezi wa muuzaji. Leta saa zenu za sasa za ufikiaji, muda wenu wa wastani wa kugundua na kujibu nje ya saa za kazi, kiasi chenu cha tahadhari, na usomaji wa uaminifu wa kama mnaweza kuajiri na kubakiza wachambuzi ambao kituo cha kujiendesha kinahitaji. Kwa serikali na mashirika makubwa yanayodhibitiwa, pima makazi ya data, uthibitisho wa wafanyakazi, na wajibu wa kisheria wa kuripoti ambao mtoa huduma lazima aweze kuutimiza, na uthibitishe mkataba unahifadhi ukali wa uchunguzi wa kidijitali na mnyororo wa utunzaji ambao mashauri ya kisheria yanadai.

## Mtazamo wa sekta

**Kampuni changa.** Kasi na kunusurika vinatangulia, kwa hiyo nunua usalama kama zao la pembeni la zana unazoendesha tayari badala ya kuajiri operesheni. Unganisha vichanganuzi vya bure kwenye CI kuzuia uvujaji wa siri na utegemezi wenye udhaifu unaojulikana wakati wa commit, tuma kumbukumbu kwa huduma inayosimamiwa ya gharama ndogo yenye tahadhari chache za thamani ya juu, na uandike mpango wa tukio wa ukurasa mmoja (nani wa kumpigia, jinsi ya kuzungusha vitambulisho, piga picha kabla ya kujenga upya) kabla hujaihitaji. Rasilimali yako adimu ni umakini wa kihandisi, kwa hiyo otomatisha ya kawaida na upinge kuanzisha kituo cha operesheni za usalama usichoweza kukiendesha.

**Biashara ndogo.** Bila mtaalamu maalumu wa usalama na bajeti finyu, egemea ugunduzi na jibu linalosimamiwa na vipengele vya usalama vilivyojengwa tayari kwenye majukwaa yako. Chukulia kupachika na orodha ya mali kama tabia zenye kiegemeo cha juu zaidi: jua unachoendesha, kiweke cha sasa, na utekeleze tarehe rahisi ya mwisho ya urekebishaji kwa ukali. Pendelea wauzaji wanaoshughulikia ufuatiliaji wa saa nzima, upokeaji wa ufichuzi ulioratibiwa, na kunasa uchunguzi wa kidijitali kwa ajili yako, na ufanyie mazoezi kitu kimoja ambacho huwezi kukabidhi nje, yaani kuamua nani anatangaza tukio na nani anazungumza na wateja.

**Biashara kubwa.** Changamoto ni uthabiti kuvuka timu nyingi na mabomba mamia: sera ya pamoja ya lango la kuzuia-dhidi-ya-kufuatilia, SLA za urekebishaji zinazotekelezwa shirika zima, jukwaa la SIEM na SOAR lenye ugunduzi uliopimwa, na purple teaming inayogeuza kila zoezi kuwa ufikiaji mpya. Simamia operesheni za usalama kama jalada lenye dashibodi za muda wa wastani wa kugundua na kujibu, ufuasi wa SLA, na usahihi wa ugunduzi, na uamue kwa makusudi pale kina cha ndani kinashinda ukubwa unaosimamiwa. Weka bajeti ya gharama ya usimamizi wa binadamu wa kupanga na kurekebisha waziwazi, kwa sababu uotomatishaji huhamisha juhudi badala ya kuiondoa.

**Serikali.** Kanuni za ununuzi, uwazi, na uwajibikaji wa umma huumba kila uchaguzi. Tarehe za mwisho za kisheria za kuripoti matukio na ufichuzi ulioratibiwa wa udhaifu ni wajibu badala ya chaguo, kwa hiyo fanyia mazoezi njia ya arifa kwa mamlaka ya kitaifa kwa uangalifu ule ule kama jibu la kiufundi, na uhifadhi ushahidi wa kidijitali chini ya mnyororo wa utunzaji unaostahimili uchunguzi wa kisheria. Pendelea mikataba inayoweka mantiki ya ugunduzi na data ikihamishika, udai mtoa huduma yeyote anayesimamiwa atimize mahitaji ya makazi na uthibitisho wa wafanyakazi, na utarajie tathmini za red-team na uchanganuzi endelevu kulisha mchakato wa idhini ambao umma unaweza kuuamini.

## Mifano

**Kampuni changa.** Kampuni changa isiyo na kituo cha operesheni za usalama inaunganisha vichanganuzi vya bure kwenye bomba lake la CI ili uvujaji wa siri na utegemezi wenye udhaifu unaojulikana unaswe wakati wa commit, ikizuia tu kwa matokeo yenye imani ya juu ili wahandisi wawili wasizamishwe katika kelele. Wanaandika mpango wa tukio wa ukurasa mmoja kabla ya kuuhitaji: nani wa kumpigia, jinsi ya kuzungusha vitambulisho, na kupiga picha ya mwenyeji ulioathirika kabla ya kuujenga upya ili waweze kujifunza kilichotokea. Wanatuma kumbukumbu kwa huduma inayosimamiwa ya gharama ndogo na kuweka tahadhari chache kwa matukio ambayo yangeashiria uvunjaji kweli, kwa hiyo tatizo linajitokeza ndani ya saa badala ya miezi inayochukua kulitambua kwa bahati.

**Biashara kubwa.** Kampuni ya programu-kama-huduma inaendesha SAST, SCA, IaC, na uchanganuzi wa siri kwenye kila bomba, ikizuia tu kwa matokeo makali, yenye imani ya juu na kufuatilia mengine kwenye dashibodi yenye SLA za urekebishaji. SIEM inalisha jukwaa la SOAR linalotenga wenyeji kiotomatiki na kufuta vitambulisho kwa tahadhari zenye imani ya juu, ikipunguza muda wa wastani wa kujibu kutoka saa hadi dakika. Mazoezi ya purple-team ya kila robo mwaka dhidi ya mbinu za MITRE ATT&CK yanazalisha moja kwa moja kanuni mpya za ugunduzi, yakiziba mapengo ya ufikiaji hatua kwa hatua.

**Serikali.** Wakala wa shirikisho unaendesha kituo cha operesheni za usalama (SOC) chenye kuripoti matukio kwa lazima kwa mamlaka ya mtandao ya kitaifa ndani ya tarehe za mwisho za kisheria. Unaendesha programu ya ufichuzi ulioratibiwa wa udhaifu yenye njia ya umma ya kupokea kama sera inavyohitaji, na kuhifadhi ushahidi wa kidijitali chini ya taratibu kali za mnyororo wa utunzaji zinazofaa mashauri ya kisheria. Tathmini za red-team za kila mwaka na uchanganuzi endelevu wa udhaifu vinalisha idhini inayoendelea ya wakala na SLA zake za urekebishaji zinazotegemea hatari.

## Kesi ya biashara: sababu, ROI, na TCO

Karibu kila kitu kuhusu kesi ya operesheni za usalama kinashuka hadi muda wa kukaa: kadiri mshambulizi anavyokaa bila kugunduliwa, ndivyo uvunjaji unavyogharimu zaidi. Tafiti mara kwa mara zinaonyesha matukio yaliyodhibitiwa haraka yanagharimu kidogo sana kuliko yale yanayodumu kwa miezi. Jumla ya gharama ya umiliki inajumuisha zana (SIEM, SOAR, vichanganuzi), uajiri au huduma zinazosimamiwa kwa ugunduzi na jibu, na muda wa kujenga na kufanyia mazoezi michakato ya tukio. Dhidi ya hilo kuna gharama ya kutowekeza: uvunjaji uliogunduliwa kuchelewa, unaoenea kuvuka mifumo, ukivuta faini za udhibiti, arifa za lazima, mashtaka, na madhara ya sifa, yote yakizidishwa na machafuko ya jibu lisilofanyiwa mazoezi.

ROI inatokana na ugunduzi na jibu la haraka, uotomatishaji unaoruhusu timu ndogo kufunika eneo kubwa, na maboresho ya kinga yanayorudishwa kutoka kila tukio na zoezi. DevSecOps hasa hulipa kwa kunasa masuala kwenye bomba ambapo ni nafuu, badala ya uzalishaji ambapo ni ghali na ya umma. Unapoweka kesi kwa uongozi, weka namba kwenye muda wenu wa sasa wa kugundua na kujibu, onyesha jinsi zinavyofungamana na muda wa kukaa na gharama, na weka uotomatishaji kama kizidishi cha nguvu kinachoepuka kukuza idadi ya wafanyakazi sambamba na eneo. Kwa serikali, sisitiza kwamba wajibu wa kisheria wa kuripoti na kufichua hufanya operesheni zilizokomaa kuwa za lazima.

## Mifumo mibaya na mitego

- **Uchovu wa tahadhari.** Tahadhari nyingi mno kiasi wachambuzi wanazizima na kukosa ile halisi.
- **Uchanganuzi bila urekebishaji.** Kuzalisha matokeo ambayo hakuna anayerekebisha, kuunda hisia ya uongo ya usalama na deni la ukaguzi.
- **Hakuna mpango wa tukio.** Kuboresha papo hapo wakati wa mgogoro, kupoteza dakika muhimu na kushughulikia ushahidi vibaya.
- **Kuharibu ushahidi.** Kujenga upya mwenyeji ulioathirika kabla ya kunasa uchunguzi wa kidijitali, kupoteza uwezo wa kuelewa au kuthibitisha kilichotokea.
- **Utamaduni wa lawama katika mapitio.** Kuwaadhibu wajibuji ili tukio linalofuata lifichwe au kushughulikiwa kwa kujihami.
- **Majaribio ya kupenya kwa uzingatiaji tu.** Jaribio moja la kila mwaka kutosheleza mkaguzi, na matokeo yakipuuzwa hadi mwaka ujao.
- **Malango yanayozuia yenye matokeo mengi ya uongo.** Kumomonyoa imani hadi wahandisi wanadai malango yaondolewe kabisa.
- **Ugunduzi wa weka-na-sahau.** Kanuni zinazooza mazingira na wapinzani wanapobadilika, zikipoteza ufikiaji kimyakimya.

## Kielelezo cha ukomavu

**Ngazi ya 1: Kuanzisha.** Operesheni za usalama ni za papo hapo na za kuitikia. Majaribio ya usalama ni ya mkono na nadra, na hakuna uandishi wa kumbukumbu wa kati wala SIEM. Hakuna mpango wa tukio, kwa hiyo jibu linaboreshwa papo hapo. Kupachika hufanyika tu kichwa cha habari kinapolazimisha, na ulinzi haujaribiwi kwa uadui kamwe.

**Ngazi ya 2: Kuendeleza.** Mazoea ya msingi yanaonekana lakini hayana uthabiti kuvuka timu. Baadhi ya mabomba huendesha vichanganuzi huku mengine hayaendeshi chochote, na uandishi wa kumbukumbu wa kati upo katika mifuko. Mpango wa msingi wa tukio umeandikwa lakini mara chache unafanyiwa mazoezi, kupachika kunafuata ratiba legevu, na jaribio la kupenya la kila mwaka linatosheleza uzingatiaji bila kubadilisha mengi. Ufikiaji na ukali hutegemea timu gani unauliza.

**Ngazi ya 3: Kusawazisha.** Mazoea yameandikwa na kutekelezwa shirika zima. Uchanganuzi kamili wa DevSecOps wenye malango yanayotegemea hatari unatumika kwa uthabiti, SIEM inahusisha matukio, na vitabu vya mikakati vya awali vya SOAR vinaendesha. Jibu la tukio linafanyiwa mazoezi kwa mazoezi ya mezani na mapitio yasiyo na lawama, SLA za urekebishaji kwa ukali zinatekelezwa na wamiliki waliotajwa, na ufichuzi ulioratibiwa wa udhaifu na red teaming ya mara kwa mara ni kawaida badala ya kighairi.

**Ngazi ya 4: Kusimamia.** Operesheni zinapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Muda wa wastani wa kugundua na kujibu, ufuasi wa SLA kwa ngazi ya ukali, ufikiaji wa uchanganuzi, viwango vya ukweli na uongo vya ugunduzi, na muda wa kukaa vinafuatiliwa kwenye dashibodi na kupitiwa kwa mzunguko. Ugunduzi unabeba usahihi na ukumbukaji uliopimwa unaooanishwa na MITRE ATT&CK, maamuzi ya uotomatishaji yanafungwa na data ya matokeo ya uongo badala ya matumaini, na kipimo kinachoteleza zaidi ya kipimo chake cha msingi huchochea jibu lililofafanuliwa badala ya kupita bila kutambuliwa.

**Ngazi ya 5: Kuratibu.** Operesheni za usalama zinaboreshwa mfululizo, zimeunganishwa kuvuka shirika, na zinajirekebisha. Uhandisi wa ugunduzi, purple teaming, urekebishaji, na mapitio ya tukio vinalisha mzunguko mmoja unaojirekebisha kwa mbinu mpya za wapinzani zinapojitokeza. Vitabu vya mikakati vya kiotomatiki vinashughulikia ya kawaida kuvuka eneo zima ili binadamu walenge busara, usalama unapangwa kando ya utoaji na hatari, na kila tukio na zoezi linaimarisha mfumo kwa kupimika huku vipimo vikuu vikiendelea kushuka.

## Mawazo ya kujadili

1. Matokeo ya bomba yapi yanapaswa kuzuia toleo, na yapi yafuatiliwe tu?
2. Jenga SOC ya ndani, tumia ugunduzi na jibu linalosimamiwa, au changanya, na kwa nini?
3. Mnazuiaje kanuni za ugunduzi zisioze mazingira yenu yanapobadilika?
4. Kupachika kunapaswa kuotomatishwa kwa ukali kiasi gani kwa kuzingatia hatari ya mabadiliko yanayovunja?
5. Mapitio ya baada ya tukio yasiyo na lawama kweli yanaonekanaje katika utamaduni wenu?
6. Mnapimaje kama red na purple teaming zinaboresha ulinzi wenu kweli?

## Mambo muhimu ya kukumbuka

- Kinga hushindwa hatimaye; operesheni zipo kugundua na kujibu haraka.
- Weka SAST, DAST, SCA, IaC, na uchanganuzi wa siri kwenye bomba kwa malango yanayotegemea hatari.
- Weka kipaumbele kupachika kwa uwezekano halisi wa kunyonywa na umuhimu wa mali, chini ya SLA zinazotekelezwa.
- Fanyia mazoezi jibu la tukio, hifadhi ushahidi wa kidijitali, na upange mawasiliano ya uvunjaji mapema.
- Tumia SIEM na SOAR kuhusisha na kuotomatisha; chukulia ugunduzi kama msimbo uliohandisiwa, uliojaribiwa.
- Thibitisha ulinzi kwa majaribio ya kupenya, red teaming, na purple teaming ya ushirikiano.
- Muda wa kukaa unaendesha gharama ya uvunjaji, kwa hiyo muda wa wastani wa kugundua na kujibu ndio vipimo vinavyojalisha.

## Marejeo na usomaji zaidi

- National Institute of Standards and Technology, *SP 800-61: Computer Security Incident Handling Guide*
- National Institute of Standards and Technology, *SP 800-40: Guide to Enterprise Patch Management*
- MITRE, *ATT&CK Framework*
- Anton Chuvakin and others, *Logging and Log Management* / SIEM literature
- Jim Bird, *DevOpsSec: Securing Software through Continuous Delivery*
- Richard Bejtlich, *The Practice of Network Security Monitoring*
- FIRST, *Coordinated Vulnerability Disclosure* guidance and *CVSS* specification
