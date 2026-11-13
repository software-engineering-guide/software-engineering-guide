# 4.3 Usalama wa miundombinu na wingu

## Muhtasari na msukumo

Programu zinaendesha juu ya miundombinu, na siku hizi miundombinu hiyo kwa kiasi kikubwa ni ya wingu, inayoelezwa na programu, na inayobadilika daima. Mhandisi mmoja sasa anaweza kutayarisha hifadhidata, kufungua njia ya mtandao, au kutoa ruhusa kwa amri moja, kwa ukubwa na kasi ambayo udhibiti wa jadi wa mabadiliko haukuwahi kuitarajia. Nguvu hiyo ndiyo hasa sababu usanidi mbaya, si unyonyaji wa kigeni, ndio chanzo kikuu cha uvunjaji wa wingu. Ndoo ya uhifadhi iliyo wazi kwa umma kwa bahati mbaya au jukumu la ufikiaji lenye upana kupita kiasi linaweza kufichua data ya shirika zima ndani ya sekunde.

Kwa mashirika makubwa, miundombinu ya wingu inavuka watoa huduma wengi, maelfu ya akaunti, na mchanganyiko wa huduma zinazosimamiwa, kontena, na kazi za serverless. Uso wa shambulio si mzunguko tuli. Ni mkusanyiko hai, unaoenea wa rasilimali na utambulisho. Kwa serikali, ugumu uleule hukutana na mifumo mikali ya idhini, maagizo ya makazi ya data, na mipaka ya uainishaji inayoumba kila uchaguzi wa usanifu. Katika yote mawili, safu ya utambulisho imekuwa mzunguko mpya: nani anaweza kufanya nini, kwa rasilimali ipi, chini ya masharti gani.

Sura hii inashughulikia jinsi ya kulinda msingi huo: [usimamizi wa utambulisho na ufikiaji](https://en.wikipedia.org/wiki/Identity_management) (IAM), [kugawanya mtandao](https://en.wikipedia.org/wiki/Network_segmentation), [usimbaji fiche](https://en.wikipedia.org/wiki/Encryption) na [usimamizi wa funguo](https://en.wikipedia.org/wiki/Key_management), usalama wa kontena na mizigo ya [serverless](https://en.wikipedia.org/wiki/Serverless_computing), na usimamizi endelevu wa msimamo unaozuia eneo la wingu linalosonga haraka lisiteleze kuelekea hatari.

## Kanuni kuu

- **Utambulisho ndio mzunguko.** Maamuzi ya ufikiaji yanategemea utambulisho imara na uidhinishaji wa kina, si mahali pa mtandao.
- **Upendeleo mdogo, daima.** Kila utambulisho, wa binadamu au mashine, unapata ruhusa za kiwango cha chini kinachohitajika, na si zaidi.
- **Gawanya kudhibiti.** Gawanya mitandao na mizigo ili kuathiriwa katika eneo moja kusiweze kuenea kwa uhuru.
- **Simba kila mahali.** Linda data wakati wa kusafiri na ikihifadhiwa kwa chaguo-msingi, kwa funguo zinazosimamiwa vizuri.
- **Isiyobadilika na ya kutangaza.** Fafanua miundombinu kama msimbo (IaC), sambaza kwa kutobadilika, na uchukulie kuteleza kama kasoro.
- **Uthibitisho endelevu.** Msimamo si ukaguzi wa mara moja; changanua na tekeleza mfululizo.
- **Usanidi salama kwa chaguo-msingi.** Hali ya chaguo-msingi ya rasilimali yoyote inapaswa kuwa imefungwa, si wazi.

## Mapendekezo

### Buni usimamizi wa utambulisho na ufikiaji kwa makusudi

IAM ndiyo sehemu muhimu zaidi ya usalama wa wingu, na ile inayosimamiwa vibaya mara nyingi zaidi.

- Tumia **[udhibiti wa ufikiaji unaotegemea jukumu](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC)** kutoa ruhusa kwa kazi, na **[udhibiti wa ufikiaji unaotegemea sifa](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC)** pale maamuzi ya kina zaidi, yanayofahamu muktadha yanahitajika (kulingana na lebo, mazingira, uainishaji wa data, au muda).
- Ondoa vitambulisho tuli vya muda mrefu kwa kupendelea tokeni za muda mfupi zinazotolewa kiotomatiki na muungano wa utambulisho wa mzigo wa kazi.
- Tekeleza [MFA](https://en.wikipedia.org/wiki/Multi-factor_authentication) (uthibitishaji wa vipengele vingi) kwa ufikiaji wote wa binadamu na uhitaji uthibitishaji imara kwa vitendo vyenye upendeleo.
- Tumia upendeleo mdogo kwa ukali: anza kutoka sifuri na uongeze ruhusa kwa makusudi. Pitia na ukate ruhusa zisizotumika mara kwa mara; ufikiaji huelekea kujilimbikiza.
- Tenganisha majukumu ili hakuna utambulisho mmoja unaoweza kufanya na kuidhinisha mabadiliko nyeti.
- Tumia akaunti au miradi maalumu kuunda mipaka migumu kati ya mazingira (uzalishaji, majaribio, uendelezaji) na kati ya vitengo vya biashara.

### Gawanya mitandao na mizigo kwa kina

Mitandao tambarare huwaruhusu washambulizi kuzurura kando mara wanapokuwa ndani. Gawanya na udhibiti.

- Gawanya kwenye kiwango cha mtandao kuwa ngazi na kanda, ukiruhusu trafiki ambayo kila ngazi inahitaji kihalali tu.
- Tumia **kugawanya kwa kina** ili mizigo ya mtu mmoja mmoja iwasiliane tu na wenzao mahususi inaowahitaji, kunakotekelezwa na sera inayofahamu utambulisho badala ya kanuni pana za subnet.
- Kataa kwa chaguo-msingi trafiki ya mashariki-magharibi; hitaji kanuni wazi za kuruhusu.
- Weka hifadhi za data nyeti kwenye subnet za faragha bila mfiduo wa moja kwa moja wa mtandao, zinazofikiwa kupitia njia zinazodhibitiwa tu.
- Tumia muunganisho wa faragha kwa huduma zinazosimamiwa badala ya kuelekeza kupitia mtandao wa umma pale inapowezekana.

### Simba data na simamia funguo ipasavyo

Usimbaji fiche ni imara tu kama usimamizi wa funguo nyuma yake.

- Simba **wakati wa kusafiri** kwa [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Transport Layer Security) ya sasa kila mahali, ikijumuisha trafiki ya ndani ya huduma-hadi-huduma.
- Simba **ikihifadhiwa** kwa chaguo-msingi kwa hifadhi zote, hifadhidata, na nakala rudufu.
- Simamia funguo kwa **Huduma ya Usimamizi wa Funguo (KMS)**, na utumie **[Moduli ya Usalama wa Vifaa](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM)** kwa funguo za uhakikisho wa juu zaidi na kwa mahitaji ya udhibiti.
- Zungusha funguo kwa ratiba na uunge mkono kuzungusha kwa haraka kwa kuathiriwa kunakoshukiwa.
- Dhibiti na kagua nani anaweza kutumia na kusimamia funguo tofauti na nani anaweza kufikia data, ili utunzaji wa funguo utekeleze kutenganisha majukumu.
- Fikiria funguo zinazosimamiwa na mteja pale udhibiti au uaminifu wa kimkataba unahitaji shirika kushikilia funguo badala ya mtoa huduma.

### Linda kontena, Kubernetes, na serverless

Kila mfano wa kokotoo unaleta hatari zake.

- **Kontena:** jenga kutoka picha za msingi ndogo, zinazoaminika; changanua picha kwa udhaifu kabla ya usambazaji; endesha kama si-mzizi; fanya mifumo ya faili ya kusoma tu pale inapowezekana; na kamwe usiweke siri ndani ya picha.
- **[Kubernetes](https://en.wikipedia.org/wiki/Kubernetes):** washa RBAC na weka wigo mwembamba kwa akaunti za huduma; tumia sera za mtandao kwa kugawanya kwa kina; tumia vidhibiti vya kuingia na injini za sera kutekeleza viwango; zuia kontena zenye upendeleo; tenga mizigo nyeti; na weka ndege ya udhibiti na nodi zikiwa zimepachikwa.
- **Serverless:** tumia upendeleo mdogo kwa jukumu la utekelezaji la kila kazi (chanzo cha kawaida cha ruhusa nyingi kupita kiasi); thibitisha ingizo zote za matukio; simamia siri kupitia hifadhi ya siri ya jukwaa; na ufuatilie mifumo isiyo ya kawaida ya miito.

Mfano wowote, weka wakati wa kuendesha umepachikwa na picha mbichi. Kontena ni salama tu kama programu iliyo ndani yake.

### Simamia msimamo wa usalama wa wingu mfululizo

Wingu hubadilika haraka mno kwa ukaguzi wa mkono wa mara kwa mara kuendana.

- Pokea zana za **Cloud Security Posture Management (CSPM)** kugundua mfululizo usanidi mbaya, mfiduo wa umma, na ukiukaji wa sera kuvuka akaunti.
- Fafanua sera ya usalama kama msimbo na uitekeleze wakati wa usambazaji ili usanidi mbaya uzuiwe kabla haujatua.
- Pendelea kinga (vizuizi vinavyosimamisha usanidi mbaya) kuliko ugunduzi (tahadhari baada ya tukio), na uchanganye vyote viwili.
- Dumisha orodha sahihi ya rasilimali na utambulisho; huwezi kulinda usichoweza kukiona.
- Fuatilia na urekebishe kuteleza kati ya miundombinu-kama-msimbo iliyotangazwa na hali halisi inayoendesha.

## Mabadilishano: faida na hasara

| Uamuzi | Faida | Hasara |
|---|---|---|
| RBAC | Rahisi, inaeleweka, rahisi kukagua | Mbaya, mlipuko wa majukumu kwa ukubwa |
| ABAC | Ya kina, inafahamu muktadha, inapanuka kwa lebo | Ngumu kubuni na kufikiria |
| Funguo zinazosimamiwa na mtoa huduma (KMS) | Rahisi, iliyounganishwa, mzigo mdogo wa uendeshaji | Mtoa huduma anashikilia utunzaji; udhibiti mdogo |
| Funguo zinazosimamiwa na mteja/HSM | Udhibiti kamili, hutimiza maagizo makali | Mzigo wa uendeshaji, hatari ya kupoteza funguo |
| Vizuizi vya kinga | Husimamisha usanidi mbaya kabla haujatokea | Vinaweza kuzuia kazi halali, vinahitaji kurekebishwa |
| CSPM ya kugundua tu | Inayonyumbulika, haizuii | Madhara yanaweza kutokea kabla ya kugunduliwa |
| Kugawanya kwa kina | Udhibiti imara wa kusonga kando | Ugumu wa uendeshaji, mtawanyiko wa sera |

Mabadilishano makuu ni udhibiti dhidi ya mzigo wa uendeshaji. Vidhibiti vikali zaidi (funguo zinazosimamiwa na mteja, kugawanya kwa kina kwa ukali, ABAC) hupunguza hatari, lakini vinadai utaalamu na matengenezo ambayo timu ndogo hupata shida kuyadumisha. Kiwango sahihi kinategemea unyeti wa data ni upi na udhibiti gani unatumika. Mbinu ya kiutendaji huweka chaguo-msingi salama imara kwa kila mtu, kisha huhifadhi ukali wa ziada kwa mifumo yenye hatari kubwa zaidi, na hupendelea vizuizi vya kiotomatiki vinavyofanya chaguo salama kuwa chaguo-msingi badala ya nidhamu ya mkono.

## Maswali ya kujadili na timu yako

1. **Mtachora wapi mipaka migumu ya akaunti au mradi, na nini kinakaa ndani ya kila moja?** Akaunti na miradi maalumu huunda udhibiti imara zaidi ambao wingu hutoa, ili kuathiriwa kwa uendelezaji kusifikie uzalishaji na kitengo kimoja cha biashara kisiguse data ya kingine. Amua mpango wenu wa mipaka kabla eneo lenu halijakua kuwa maelfu ya akaunti, kwa sababu kurudisha kutenga kwenye muundo tambarare ni polepole na hatari. Kwa kazi ya mashirika makubwa na serikali, mipaka hii pia inaoana wazi na kutenganisha mazingira, uainishaji wa data, na mipaka ya eneo la mlipuko ambayo wakaguzi wanatarajia kuona. Leta mchoro wa sasa wa mizigo ipi inashiriki akaunti leo na uweke alama mahali jukumu moja lenye upana kupita kiasi linavuka uzalishaji na zisizo za uzalishaji. Data nyeti ikikaa kwenye akaunti moja na mizigo ya majaribio, hiyo ndiyo mpaka wa kurekebisha kwanza.

2. **Kiwango chenu ni kipi cha nani anaweza kusimamia funguo dhidi ya nani anaweza kufikia data iliyosimbwa?** Usimbaji fiche ni imara tu kama usimamizi wa funguo, na kutenganisha utunzaji wa funguo na ufikiaji wa data kunageuza KMS yenu kuwa nukta ya kutekeleza kutenganisha majukumu. Amua nani anaweza kuunda, kuzungusha, na kutumia funguo, na uhakikishe seti hiyo haiingiliani na watu wanaoweza kusoma data ambayo funguo hizo zinalinda. Kwa mifumo inayodhibitiwa na ya serikali, hili mara nyingi huendesha uchaguzi kati ya funguo zinazosimamiwa na mtoa huduma na funguo zinazosimamiwa na mteja au HSM, ambazo hubeba udhibiti zaidi na hatari zaidi ya uendeshaji ya kupoteza funguo. Leta sera zenu za sasa za funguo na uangalie kama utambulisho wowote mmoja unaweza kusimamia ufunguo na kusoma data iliyo nyuma yake, kwa sababu hilo ni pengo la kawaida la kimya. Utunzaji na ufikiaji visipogawanywa, usimbaji fiche wa kuhifadhiwa unakulinda kidogo kuliko dashibodi inavyodokeza.

3. **Mtafanyaje chaguo-msingi salama zisiepukike kwenye eneo lenu la kutua badala ya kupendekezwa tu?** Usanidi mbaya, si unyonyaji wa kigeni, ndio chanzo kikuu cha uvunjaji wa wingu, na suluhisho ni vizuizi vya kinga vinavyozuia hifadhidata ya umma au ndoo isiyosimbwa kabla haijatua, si tahadhari baada ya tukio. Amua sera zipi mtazitekeleza wakati wa usambazaji (hakuna uhifadhi wa umma, usimbaji fiche umewashwa kwa chaguo-msingi, lebo za lazima) na zipi mtazigundua na kuripoti tu. Kwa timu kubwa, kuweka haya kwenye maeneo ya kutua na violezo vya miundombinu-kama-msimbo kunamaanisha kila akaunti mpya inarithi ulinzi bila juhudi ya kila timu, ikigeuza usalama kutoka kodi inayojirudia kuwa uwekezaji wa mara moja. Leta matokeo yenu ya mwezi uliopita ya usanidi mbaya na uliza ni yapi kizuizi cha kinga kingeyazuia moja kwa moja. Usimamizi wenu wa msimamo ukiwa wa kugundua tu, madhara yanaweza kutokea kabla mtu yeyote hajaona tahadhari, kwa hiyo hamisha ukaguzi wenye athari kubwa zaidi kwenye kinga.

4. **Mnaondoaje vitambulisho tuli vya muda mrefu bila kuvunja uotomatishaji unaovitegemea kimyakimya?** Funguo za ufikiaji zilizopachikwa ambazo hazioi kamwe ni miongoni mwa visababishi vya kawaida zaidi vya uvunjaji wa wingu, kwa sababu ufunguo mmoja uliovuja kwenye hati, kumbukumbu, au hazina humpa mshambulizi ufikiaji wa kudumu. Mvuto unaoshindana ni wa uendeshaji: kazi za CI za urithi, kazi za cron, na uunganishaji wa mtu wa tatu mara nyingi hudhani ufunguo tuli upo, na kuzibadilisha kwenda tokeni za muda mfupi au muungano wa utambulisho wa mzigo wa kazi huchukua muda wa kihandisi ambao hakuna aliyeupangia. Kwa timu kubwa, njia ya uhamishaji ya pamoja (toa tokeni kiotomatiki, weka kiwango cha kuisha, na utoe tahadhari kwa ufunguo wowote mpya wa muda mrefu) huzuia kila kikundi kuvumbua jibu lake dhaifu. Leta orodha ya kila kitambulisho tuli kinachotumika, umri wake, eneo lake la mlipuko, na kama mfumo inaoulisha unaweza kukubali utambulisho ulioungana leo. Katika mazingira ya mashirika makubwa na serikali, funga tarehe ya mwisho na mizunguko ya ukaguzi na idhini, kwa sababu kitambulisho kinachodumu kuliko mtu aliyekiunda ndicho hasa matokeo yanayokwamisha idhini endelevu.

5. **Rasilimali inapowekwa vibaya au ufunguo kuathiriwa, mnaweza kugundua, kudhibiti, na kurekebisha kwa kasi gani, na je, mmepima?** Ndoo ya umma au jukumu lenye upana kupita kiasi ni hatari tu kadiri dirisha linavyobaki wazi, kwa hiyo muda wa wastani wa kugundua na kurekebisha ndio namba inayofunga mfiduo wenu kweli. Mvutano ni kati ya vizuizi vya kinga vinavyosimamisha kosa wakati wa usambazaji na usimamizi wa msimamo wa kugundua unaonasa kinachoteleza, na mnahitaji takwimu za uaminifu kwa yote mawili badala ya dhana ya kufariji kwamba vizuizi vinafunika kila kitu. Leta matokeo yenu ya robo iliyopita ya usanidi mbaya na kuteleza yenye mihuri ya muda, muda wa wastani kutoka kuingizwa hadi kurekebishwa, na rekodi ya mazoezi ya kuzungusha ufunguo ulioathirika. Kwa maeneo ya mashirika makubwa na serikali yanayovuka maelfu ya akaunti, kubaliana nani anamiliki kurekebisha matokeo ambayo hakuna timu inayoonekana kuyamiliki, kwa sababu tahadhari isiyo na mjibu anayewajibika ni tahadhari inayozeeka kuwa tukio.

6. **Mtaweka vipi msimamo wa usalama thabiti kuvuka mawingu, akaunti, na timu nyingi bila kupunguza kasi ya kila mtu?** Maeneo ya wingu-nyingi na akaunti nyingi hugawanyika haraka: kila mtoa huduma ana mfano wake wa IAM, chaguo-msingi zake, na zana zake za msimamo, kwa hiyo sera inayotekelezwa mahali pamoja hupungua kimyakimya kwingine. Biashara ni kati ya udhibiti wa kati unaohakikisha uthabiti na uhuru wa mahali unaoruhusu timu kusonga haraka, na kuegemea mno upande wowote ama kunakwamisha utoaji au kuacha viwango viteleze. Leta ramani yenu ya sasa ya ufikiaji: akaunti zipi zinarithi vizuizi vya eneo la kutua, zipi hazisimamiwi, na wapi kidhibiti kilekile kinaonyeshwa kwa njia tatu tofauti kuvuka watoa huduma. Kwa shirika kubwa au la umma, ongeza pembe ya ukaguzi, kwa sababu wakaguzi wanatarajia kiwango kimoja kinachoweza kutetewa kinachotumika kila mahali, na kidhibiti kilichopo kwenye wingu lenu kuu lakini si la pili ni pengo ambalo mshambulizi aliyedhamiria au mpimaji atalipata kwanza.

## Mtazamo wa sekta

**Kampuni changa.** Kasi na kunusurika vinashinda, kwa hiyo egemea kabisa chaguo-msingi salama zinazosafirishwa bure: usimbaji fiche wa kuhifadhiwa umewashwa, ndoo za uhifadhi za faragha isipokuwa binadamu azifungue, MFA kwenye akaunti ya mzizi, na utambulisho wa mzigo wa kazi uliojengwa ndani wa mtoa huduma badala ya funguo za ufikiaji zilizobandikwa. Usianzishe jukwaa la CSPM wala kugawanya kwa kina kwa mkono usioweza kudumisha; kizuizi kimoja kinachozuia hifadhidata iliyofunguliwa kwa mtandao hununua ulinzi mwingi kwa alasiri ya kazi. Weka kila kitu kwenye miundombinu-kama-msimbo tangu mwanzo ili kuimarisha kupanuke nawe badala ya kuwa uandishi upya wa baadaye.

**Biashara ndogo.** Bila mhandisi maalumu wa usalama na bajeti finyu, pendelea huduma zinazosimamiwa ambazo chaguo-msingi zake tayari zimeimarishwa na ambazo usimamizi wa funguo unashughulikiwa kwa ajili yako, badala ya kujenga nidhamu yako ya KMS. Chukulia usalama wa wingu kama swali la usafi wa usanidi: jua ndoo na hifadhidata zipi zipo, ziweke za faragha, hitaji MFA, na uwashe ukaguzi wa msimamo wa asili wa mtoa huduma usiogharimu ziada. Unaponunua zana, pendelea zile zinazoweka alama mfiduo wa umma na uhifadhi usiosimbwa moja kwa moja, kwa sababu makosa hayo mawili husababisha uvunjaji mwingi unaoepukika.

**Biashara kubwa.** Tatizo halisi ni uthabiti kuvuka maelfu ya akaunti na timu nyingi, kwa hiyo kazi ni kazi ya jukwaa: maeneo ya kutua yanayotayarisha kila akaunti ikiwa imeimarishwa, vizuizi vinavyotekelezwa kama sera-kama-msimbo, na CSPM inayochanganua mfululizo kuteleza. Sawazisha mfano wa IAM, kanuni za utunzaji wa funguo, na msingi wa kugawanya ili vikundi viache kuvumbua matoleo dhaifu zaidi, na upime msimamo kuvuka eneo badala ya kuamini neno la kila timu. Weka bajeti ya uhandisi endelevu wa kuweka sera za sasa watoa huduma wanapoongeza huduma na eneo linapokua.

**Serikali.** Kanuni za ununuzi, maagizo ya makazi ya data, na mifumo ya idhini huumba kila uchaguzi, kwa hiyo vidhibiti vya usalama hufanya kazi mara mbili kama ushahidi wa ukaguzi. Pendelea usimamizi wa funguo uliothibitishwa na FIPS wenye utunzaji uliotengwa na ufikiaji wa data, kanda zilizotengwa zinazoweka data ndani ya mipaka ya taifa, na picha za kontena zilizosainiwa, zilizochanganuliwa zenye udhibiti mkali wa kuingia. Chapisha vizuizi unavyoweza, lisha usimamizi endelevu wa msimamo moja kwa moja kwenye idhini inayoendelea, na uhitaji wauzaji wafichue chaguo-msingi za usanidi na waunge mkono vidhibiti vya kugawanya na utunzaji wa funguo ambavyo mipaka yako ya uainishaji inadai.

## Mifano

**Kampuni changa.** Kampuni changa ndogo inaendesha kila kitu kwenye akaunti moja ya wingu na haiwezi kuajiri timu ya jukwaa, kwa hiyo inategemea chaguo-msingi zinazosafirishwa salama: usimbaji fiche wa kuhifadhiwa umewashwa kwa chaguo-msingi, ndoo za uhifadhi za faragha isipokuwa binadamu azifungue waziwazi, na MFA inayohitajika kwenye akaunti ya mzizi. Badala ya funguo za ufikiaji za muda mrefu zilizobandikwa kwenye CI, inatumia utambulisho wa mzigo wa kazi uliojengwa ndani wa mtoa huduma ili bomba lipate vitambulisho vya muda mfupi kiotomatiki. Kizuizi kimoja cha bure kinachoweka alama hifadhidata yoyote iliyofunguliwa kwa mtandao kinawaokoa na kosa la kawaida zaidi na ghali zaidi la wingu, kwa gharama ya alasiri moja ya usanidi.

**Biashara kubwa.** Kampuni ya vyombo vya habari inayoendesha maelfu ya akaunti kuvuka watoa huduma wawili wa wingu inatekeleza muundo wa eneo la kutua: kila akaunti inatayarishwa kutoka kiolezo chenye usimbaji fiche wa kuhifadhiwa umewashwa kwa chaguo-msingi, hakuna ufikiaji wa umma kwenye uhifadhi, lebo za lazima, na msingi wa sera za vizuizi. CSPM inachanganua mfululizo kuteleza, na muungano wa utambulisho wa mzigo wa kazi umeondoa funguo za muda mrefu kwa mifumo ya CI. Msanidi anapojaribu kwa bahati mbaya kufungua hifadhidata kwa mtandao, sera ya kinga inazuia badiliko na kufungua tiketi kiotomatiki.

**Serikali.** Wakala unaohusiana na ulinzi unaendesha katika kanda ya wingu iliyotengwa yenye makazi ya data yanayotekelezwa kwa sera ili hakuna data inayoondoka mipaka ya taifa. Funguo nyeti zaidi zinaishi kwenye HSM zilizothibitishwa na FIPS (Federal Information Processing Standards), na utunzaji wa funguo ukitenganishwa na ufikiaji wa data kutekeleza kutenganisha majukumu. Makundi ya Kubernetes yanatumia sera kali za mtandao na vidhibiti vya kuingia; kila picha ya kontena inachanganuliwa na kusainiwa kabla ya kuruhusiwa kuendesha. Usimamizi endelevu wa msimamo unalisha moja kwa moja ushahidi wa idhini inayoendelea ya wakala.

## Kesi ya biashara: sababu, ROI, na TCO

Usalama wa miundombinu ya wingu ndipo uwekezaji mdogo huzuia hasara za maafa, za kiwango cha kichwa cha habari. Jumla ya gharama ya umiliki inajumuisha zana za CSPM, huduma za usimamizi wa funguo, muda wa kihandisi wa kubuni IAM ya upendeleo mdogo na kugawanya, na juhudi endelevu ya kuweka sera za sasa. Gharama hizi ni halisi lakini za wastani. Gharama ya kuruka ni rasilimali moja iliyowekwa vibaya inayofichua hifadhidata nzima ya wateja, pamoja na faini za udhibiti, gharama za arifa, na uharibifu wa kudumu wa chapa unaofuata. Uvunjaji wa usanidi mbaya wa wingu ni miongoni mwa matukio ya kawaida zaidi na yanayoweza kuzuilika zaidi katika tasnia.

Uotomatishaji na utumiaji tena huzidisha ROI. Weka chaguo-msingi salama kwenye maeneo ya kutua na violezo vya miundombinu-kama-msimbo, na kila akaunti na mzigo mpya unarithi ulinzi bila juhudi ya kila timu, ukigeuza usalama kutoka kodi ya mkono inayojirudia kuwa uwekezaji wa jukwaa wa mara moja. Kwa serikali na mashirika makubwa yanayodhibitiwa, usimamizi imara wa msimamo pia unapunguza gharama ya ukaguzi na idhini endelevu kwa kuzalisha ushahidi kiotomatiki. Unapoweka kesi kwa uongozi, sisitiza kwamba safu ya utambulisho na usanidi sasa ndiyo njia kuu ya uvunjaji, kwamba usanidi mbaya unazuilika, na kwamba vizuizi vinapunguza hatari na msuguano wa mapitio ya mkono.

## Mifumo mibaya na mitego

- **Ruhusa za wildcard.** Kutoa ufikiaji mpana wa `*` "ili mambo yafanye kazi" na kamwe kutoubana.
- **Funguo tuli za muda mrefu.** Funguo za ufikiaji zilizopachikwa kwenye hati na CI ambazo hazioi kamwe na hatimaye kuvuja.
- **Mitandao tambarare.** Hakuna kugawanya, kwa hiyo mwenyeji mmoja aliyeathirika anafikia kila kitu.
- **Wazi kwa bahati mbaya.** Uhifadhi na hifadhidata zilizofichuliwa kwa mtandao kupitia mipangilio ya chaguo-msingi au ya uzembe.
- **Usimbaji fiche bila nidhamu ya funguo.** Kuwasha usimbaji fiche lakini kuacha ufikiaji wa funguo wazi au kutozungusha kamwe.
- **Siri zilizooka ndani ya picha.** Vitambulisho vilivyopachikwa kwenye picha za kontena vinavyoenea kila mahali picha inapoendesha.
- **Majukumu ya serverless yenye ruhusa nyingi kupita kiasi.** Kazi zilizopewa zaidi sana ya zinavyohitaji kwa sababu kuweka wigo kuliruka.
- **Msimamo wa ukaguzi tu.** Kugundua usanidi mbaya baada ya tukio badala ya kuuzuia wakati wa usambazaji.
- **Kupuuza kuteleza.** Kuacha mazingira yanayoendesha yatofautiane na miundombinu-kama-msimbo hadi hakuna anayejua hali halisi.

## Kielelezo cha ukomavu

**Ngazi ya 1: Kuanzisha.** Utayarishaji wa mkono unaoendeshwa na yeyote anayehitaji rasilimali. Ruhusa pana za wildcard na funguo tuli za muda mrefu. Mitandao tambarare bila kugawanya. Usimbaji fiche unatumika bila uthabiti, kama kabisa. Hakuna usimamizi wa msimamo; usanidi mbaya hujitokeza tu baada ya tukio kulazimisha swali.

**Ngazi ya 2: Kuendeleza.** Baadhi ya majukumu ya IAM na MFA yanaonekana, na usimbaji fiche wa kuhifadhiwa umewashwa kwa hifadhi kuu, lakini mazoea hutofautiana timu hadi timu. Ngazi za msingi za mtandao zipo bila kukataa kwa chaguo-msingi. Mapitio ya usanidi hufanyika mara kwa mara na kwa mkono. Miundombinu inafafanuliwa kama msimbo kwa sehemu, kwa hiyo kuimarisha kunategemea kikundi kipi kilitayarisha akaunti.

**Ngazi ya 3: Kusawazisha.** RBAC na ABAC ya upendeleo mdogo yenye vitambulisho vya muda mfupi imeandikwa na kutekelezwa shirika zima. Kugawanya kunatumia kukataa kwa chaguo-msingi mashariki-magharibi. Usimbaji fiche wakati wa kusafiri na kuhifadhiwa umewashwa kwa chaguo-msingi, funguo zikiwa kwenye KMS kwa ratiba ya kuzungusha na utunzaji ukitenganishwa na ufikiaji wa data. Kuimarisha kontena na Kubernetes ni kiwango, na CSPM inaendesha dhidi ya sera zilizofafanuliwa zinazotumika kwa uthabiti kuvuka kila akaunti.

**Ngazi ya 4: Kusimamia.** Msimamo unapimwa, haudhaniwi. Unafuatilia vipimo vilivyotajwa dhidi ya vipimo vya msingi na malengo: sehemu ya utambulisho ndani ya kipimo chao cha msingi cha upendeleo mdogo, muda wa wastani wa kugundua na kurekebisha usanidi mbaya na kuteleza, ufikiaji wa vizuizi na CSPM kuvuka akaunti, ulinganifu wa kuzungusha funguo, na idadi ya vitambulisho vya muda mrefu vinavyobaki. Matokeo yanapangwa kwa eneo la mlipuko, urekebishaji una mmiliki na lengo la kiwango cha huduma, na data ya mwelekeo wa namba hizi huendesha mahali juhudi inayofuata ya kuimarisha inakoenda.

**Ngazi ya 5: Kuratibu.** Chaguo-msingi salama zimeokwa ndani ya maeneo ya kutua na miundombinu-kama-msimbo ili kila rasilimali izaliwe ikiwa imeimarishwa, na vidhibiti hujirekebisha eneo na picha ya tishio vinapohama. Kugawanya kwa kina kunatumia sera inayofahamu utambulisho; funguo zinazosimamiwa na mteja na HSM hulinda mifumo ya uhakikisho wa juu zaidi kwa kutenganisha utunzaji. Vizuizi vya kinga huzuia usanidi mbaya wakati wa usambazaji, kuteleza kunagunduliwa na kurekebishwa kiotomatiki, na ushahidi wa msimamo unalisha idhini endelevu kiotomatiki. Usalama umeunganishwa na utoaji na upangaji wa hatari, na shirika hustaafisha na kupanga upya wigo wa vidhibiti mara kwa mara watoa huduma, huduma, na kanuni zinapobadilika.

## Mawazo ya kujadili

1. ABAC inastahili ugumu wake wapi dhidi ya kubaki na RBAC katika mazingira yenu?
2. Mnaondoaje vitambulisho vya muda mrefu bila kuvunja uotomatishaji wa urithi?
3. Mgawanyo sahihi kati ya vizuizi vya kinga na usimamizi wa msimamo wa kugundua ni upi?
4. Mifumo ipi inahalalisha funguo zinazosimamiwa na mteja au HSM kwa kuzingatia gharama yao ya uendeshaji?
5. Mnazuiaje ruhusa za upendeleo mdogo zisijilimbikize kimyakimya kurudi kwenye upendeleo kupita kiasi?
6. Ugumu wa wingu-nyingi unapaswa kubadilishaje mbinu yenu ya msimamo na sera thabiti?

## Mambo muhimu ya kukumbuka

- Utambulisho ni mzunguko mpya; wekeza katika IAM ya upendeleo mdogo yenye vitambulisho vya muda mfupi.
- Gawanya mitandao na ugawanye mizigo kwa kina kudhibiti kuathiriwa.
- Simba wakati wa kusafiri na ikihifadhiwa kwa chaguo-msingi, na usimamie funguo kwa KMS/HSM na kutenganisha utunzaji.
- Imarisha kontena, Kubernetes, na serverless; weka wakati wa kuendesha na picha zikiwa zimepachikwa.
- Pendelea vizuizi vya kinga kuliko ugunduzi wa baada ya tukio, na usimamie msimamo mfululizo.
- Oka chaguo-msingi salama kwenye maeneo ya kutua na miundombinu-kama-msimbo ili ulinzi upanuke kiotomatiki.
- Usanidi mbaya, si unyonyaji wa kigeni, ndio chanzo kikuu cha uvunjaji wa wingu, na unazuilika.

## Marejeo na usomaji zaidi

- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- Center for Internet Security, *CIS Benchmarks* (cloud providers, Kubernetes, Docker)
- Cloud Security Alliance, *Cloud Controls Matrix* and *Security Guidance for Cloud Computing*
- NIST, *SP 800-190: Application Container Security Guide*
- Liz Rice, *Container Security*
- Marco Lancini and others, *Cloud security posture and detection* engineering literature
- Provider Well-Architected security pillars (as vendor-neutral architectural guidance)
