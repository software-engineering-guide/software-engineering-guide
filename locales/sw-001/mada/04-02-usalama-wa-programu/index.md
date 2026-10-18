# 4.2 Usalama wa programu

## Muhtasari na msukumo

Usalama wa programu ndipo vitisho vya dhahania vinapokutana na msimbo madhubuti. Uvunjaji mwingi unaofika kwenye vichwa vya habari hufuatiliwa hadi dosari ya safu ya programu: uingizaji, mtiririko wa uthibitishaji ulioharibika, siri iliyofichuliwa, au utegemezi ulioathiriwa. Kwa timu kubwa zinazosafirisha huduma nyingi, sehemu ngumu si kujua dosari hizi zipo. Ni kuzizuia kwa uthabiti kuvuka msimbo mkubwa ulioandikwa na maelfu ya mikono kwa miaka mingi.

Kwa mashirika makubwa, usalama wa programu ni suala la uaminifu wa wateja na wajibu wa kudhibitiwa. Dosari katika mtiririko wa kuingia au njia ya malipo inaweza kuchochea ulaghai, faini, na kufichuliwa kwa lazima kwa uvunjaji. Mifumo ya serikali inakabiliana na hatari zilezile za kiufundi ikiwa na data yenye dau kubwa zaidi: kustahiki manufaa, rekodi za kodi, data ya haki ya jinai, na miundombinu ya taifa. Katika mazingira yote mawili, programu ndio mlango wa mbele, na washambulizi wanaupima mara kwa mara na kiotomatiki.

Sura hii inashughulikia mazoea yanayoweka programu ustahimilivu: kujua na kujilinda dhidi ya madarasa ya kawaida ya udhaifu, kuthibitisha ingizo na kusimba pato, kupata uthibitishaji na uidhinishaji sawa, kusimamia siri, na kulinda mnyororo wa ugavi wa programu unaozidi kuamua uso wako halisi wa shambulio.

*Angalia pia:* sura ya 4.1 (misingi ya usalama, uundaji wa vitisho, na mzunguko salama wa uendelezaji), sura ya 10.3 (mnyororo wa ugavi wa chanzo huria na leseni), na sura ya 10.2 (SBOM, hatari, na uhakikisho).

## Kanuni kuu

- **Usiamini ingizo kamwe.** Chukulia data yote inayovuka mpaka wa uaminifu kama ya uadui hadi ithibitishwe.
- **Chaguo-msingi salama.** Njia salama inapaswa kuwa rahisi; tabia isiyo salama inapaswa kuhitaji juhudi ya makusudi, inayoonekana.
- **Shindwa kwa kufunga.** Ukaguzi wa usalama usipoweza kukamilika, kataa ufikiaji badala ya kuruhusu.
- **Ulinzi wa kina kwenye safu ya programu.** Changanya uthibitisho, usimbaji, vigezo, na ulinzi wa mfumo wa kazi; usitegemee kimoja.
- **Upendeleo mdogo kwa utambulisho na tokeni.** Weka vitambulisho kwa wigo mwembamba na uviishie haraka.
- **Utegemezi wako ni msimbo wako.** Unawajibika kwa usalama wa kila kitu unachosafirisha, ikijumuisha vijenzi vya mtu wa tatu na vya chanzo huria.
- **Viwango kuliko ubunifu wa papo hapo.** Tumia mifumo iliyochunguzwa kama [OWASP](https://en.wikipedia.org/wiki/OWASP) (Open Worldwide Application Security Project) ASVS badala ya kuvumbua vidhibiti vyako vya usalama.

## Mapendekezo

### Jua na ulinde dhidi ya OWASP Top 10, thibitisha kwa ASVS

OWASP Top 10 ni orodha ya msingi ya tasnia ya hatari muhimu zaidi za programu za wavuti: udhibiti wa ufikiaji ulioharibika, kushindwa kwa kriptografia, uingizaji, usanifu usio salama, usanidi mbaya wa usalama, vijenzi vyenye udhaifu, kushindwa kwa uthibitishaji, kushindwa kwa uadilifu wa data, kushindwa kwa kumbukumbu, na ghushi ya ombi la upande wa seva. Ichukulie kama maarifa yanayohitajika kwa kila mhandisi, si rejeo la uzingatiaji la kuhifadhi.

Kwa kiwango kigumu, kinachojaribika, pokea **OWASP Application Security Verification Standard (ASVS)**. ASVS hufafanua mahitaji ya usalama katika ngazi tatu za uhakikisho, ikikupa vidhibiti madhubuti, vinavyokaguliwa vya kubuni na kujaribu dhidi yake. Chagua ngazi inayolingana na hatari ya kila programu, na uthibitishe dhidi yake.

### Thibitisha ingizo na simba pato

Dosari za uingizaji hubaki miongoni mwa zenye madhara zaidi hasa kwa sababu ni rahisi sana kuziingiza. Jilinde kwa vidhibiti vya tabaka:

- **Thibitisha ingizo** dhidi ya orodha kali za kuruhusu (aina inayotarajiwa, urefu, umbo, wigo). Kataa badala ya kusafisha pale unapoweza.
- **Tumia hoja zenye vigezo** na [taarifa zilizoandaliwa](https://en.wikipedia.org/wiki/Prepared_statement) kwa ufikiaji wote wa hifadhidata; kamwe usijenge SQL kwa kuunganisha mfuatano. Tumia wajenzi salama wa hoja na ORM (object-relational mappers) kwa usahihi.
- **Simba pato** kwa muktadha. HTML, sifa za HTML, JavaScript, URL, na CSS kila moja inahitaji usimbaji tofauti. Tegemea kutoroka kiotomatiki kwa mfumo wa kazi na uelewe mipaka yake.
- **Zuia [uandishi wa hati kuvuka tovuti](https://en.wikipedia.org/wiki/Cross-site_scripting) (XSS)** kwa usimbaji wa pato pamoja na Sera imara ya Usalama wa Maudhui kama safu ya pili.
- **Zuia uingizaji wa amri na kiolezo** kwa kuepuka kuita ganda kwa data isiyoaminika na kwa kutumia violezo visivyo na mantiki au vilivyowekwa kwenye sanduku.

### Pata uthibitishaji na uidhinishaji sawa

Uthibitishaji huthibitisha mtumiaji ni nani. Uidhinishaji huamua anaweza kufanya nini. Vyote viwili hushindwa mara nyingi, kwa hiyo vipate sawa.

- Pendelea itifaki zilizothibitishwa: **[OAuth 2.0](https://en.wikipedia.org/wiki/OAuth)** kwa uidhinishaji uliokabidhiwa na **[OpenID Connect](https://en.wikipedia.org/wiki/OpenID_Connect) (OIDC)** kwa uthibitishaji. Usijenge hivi kutoka mwanzo.
- Tekeleza **[uthibitishaji wa vipengele vingi](https://en.wikipedia.org/wiki/Multi-factor_authentication) (MFA)**, hasa kwa ufikiaji wenye upendeleo na wa kiusimamizi.
- Hifadhi nenosiri tu kama hashi zenye chumvi ukitumia algoriti ya kisasa, ya polepole, inayotumia kumbukumbu nyingi (kama [Argon2](https://en.wikipedia.org/wiki/Argon2) au [bcrypt](https://en.wikipedia.org/wiki/Bcrypt)). Kamwe usihifadhi wala kuandika kwenye kumbukumbu vitambulisho vya maandishi wazi.
- Simamia **vikao** kwa uangalifu: zalisha tokeni zenye nguvu za kriptografia, weka bendera salama za kuki na HttpOnly, zungusha upendeleo unapobadilika, na ishie vikao visivyotumika.
- Tekeleza **uidhinishaji upande wa seva kwa kila ombi**, ukikagua kwamba mhusika aliyethibitishwa anamiliki au anaweza kufikia rasilimali mahususi. Uidhinishaji ulioharibika wa kiwango cha kitu (kufikia rekodi ya mtumiaji mwingine kwa kubadilisha kitambulisho) ni mojawapo ya dosari za kawaida na kali zaidi za API.
- Weka mantiki ya uidhinishaji kati pale inapowezekana ili sera iwe thabiti na inayokaguliwa.

### Simamia siri na zungusha funguo

Siri zilizoandikwa moja kwa moja kwenye msimbo wa chanzo ni chanzo cha kudumu cha uvunjaji. Jenga tabia yenye nidhamu kuzunguka usimamizi wa siri:

- Hifadhi siri kwenye msimamizi wa siri au hazina maalumu, kamwe si kwenye chanzo, faili za usanidi, au vigeu vya mazingira vilivyowekwa kwenye udhibiti wa matoleo.
- Changanua commit na hazina kwa siri zilizovuja kiotomatiki, na uzuie uunganishaji unaoziingiza.
- Zungusha funguo na vitambulisho mara kwa mara na mara moja kwa kufichuliwa kunakoshukiwa. Pendelea vitambulisho vya muda mfupi, vinavyotolewa kiotomatiki kuliko vya muda mrefu, tuli.
- Tumia upendeleo mdogo kwa kila siri: iwekee wigo kwa kile inachohitaji hasa.
- Simba siri zikihifadhiwa na zinaposafiri, na ukague ufikiaji wake.

### Linda mnyororo wa ugavi wa programu

Programu za kisasa hukusanywa hasa kutoka vijenzi vya mtu wa tatu, jambo linalofanya mnyororo wa ugavi kuwa uso mkuu wa shambulio.

- Dumisha **[Orodha ya Vifaa vya Programu](https://en.wikipedia.org/wiki/Software_bill_of_materials) (SBOM)** kwa kila programu ili ujue hasa unachosafirisha na uweze kujibu haraka udhaifu mpya unapotua.
- Changanua utegemezi mfululizo (Software Composition Analysis, au SCA) na urekebishe vijenzi vyenye udhaifu unaojulikana haraka.
- Funga na uthibitishe matoleo ya utegemezi; tumia faili za kufunga na rejista zinazoaminika.
- Pokea **SLSA** (Supply-chain Levels for Software Artifacts) kuinua uadilifu wa ujenzi, na uzalishe uthibitisho wa **asili** unaoeleza jinsi vitu vilivyojengwa.
- **Saini vitu** na uthibitishe saini kabla ya usambazaji ili uweze kuamini kinachoendesha ni kile ulichojenga.
- Linda mfumo wa ujenzi wenyewe; bomba la CI lililoathirika linaweza kuingiza msimbo hasidi kwa kila mtumiaji wa chini ya mkondo.

## Mabadilishano: faida na hasara

| Uamuzi | Faida | Hasara |
|---|---|---|
| Nunua/pokea mtoa utambulisho (OIDC) | Umejaribiwa vizuri, MFA imejengwa ndani, msimbo mdogo wa kulinda | Utegemezi wa muuzaji, juhudi ya uunganishaji, gharama |
| Jenga uthibitishaji maalumu | Udhibiti kamili, hakuna utegemezi wa nje | Rahisi sana kukosea, matengenezo ya juu |
| Uthibitisho mkali wa orodha ya kuruhusu | Huzuia madarasa mazima ya udhaifu | Unaweza kuvunja kesi halali za pembeni, kazi zaidi mapema |
| Vitambulisho vya muda mfupi | Dirisha dogo la uvunjaji, kufuta kiotomatiki | Inahitaji miundombinu imara ya utoaji |
| Masasisho ya utegemezi ya ukali | Udhaifu unaojulikana mdogo | Msukosuko, mabadiliko yanayoweza kuvunja, mzigo wa majaribio |
| SBOM + kusaini + asili | Jibu la tukio la haraka, uaminifu unaothibitishika | Uwekezaji wa zana na mchakato, mabadiliko ya kiutamaduni |

Mvutano unaojirudia ni ukali wa awali dhidi ya mfiduo unaoendelea. Kujenga uthibitishaji maalumu au kuruka usafi wa utegemezi kunahisi haraka leo na kunagharimu sana baadaye. Kupokea viwango vilivyochunguzwa na vidhibiti vya kiotomatiki vya mnyororo wa ugavi kunagharimu juhudi sasa, lakini kunageuza hatari isiyo na kikomo, isiyotabirika kuwa iliyosimamiwa, iliyofungwa. Kwa timu kubwa, kizidishi cha uotomatishaji ndicho kinachojalisha zaidi: kidhibiti kilichotumika mara moja kwenye kiolezo cha njia iliyopakwa lami kinalinda kila huduma inayokitumia.

## Maswali ya kujadili na timu yako

1. **Vidhibiti vipi vya ASVS mtaviweka kwenye mfumo wenu wa kazi wa njia iliyopakwa lami ili wahandisi wavipate bure?** Hatua yenye kiegemeo cha juu zaidi kwa timu kubwa ni kufanya njia salama kuwa chaguo-msingi, ili kidhibiti kilichoandikwa mara moja kwenye mfumo wa kazi wa pamoja kilinde kila huduma inayoupokea. Amua mahitaji yapi ya ASVS (hoja zenye vigezo, usimbaji wa pato, bendera salama za kikao, ukaguzi wa uidhinishaji wa upande wa seva) yanastahili kuwa kwenye kiolezo badala ya kumbukumbu ya kila mhandisi. Kwa majalada ya mashirika makubwa na serikali, amua pia programu zipi zinahitaji ASVS Ngazi ya 2 dhidi ya Ngazi ya 3, na ufunge hilo na unyeti wa data ambayo kila moja inagusa. Leta orodha ya huduma zenu na uweke alama zipi tayari zinarithi chaguo-msingi hizi na zipi zinatekeleza usalama upya kwa mkono, kwa sababu zile za mkono ndipo uingizaji na udhibiti wa ufikiaji ulioharibika hujificha. Chaguo-msingi salama zikiishi kwenye ukurasa wa wiki tu, zitarukwa chini ya shinikizo la utoaji, kwa hiyo ziweke kwenye msimbo.

2. **Mtapataje na kurekebisha uidhinishaji ulioharibika wa kiwango cha kitu kuvuka kila API, si mpya tu?** Kufikia rekodi ya mtumiaji mwingine kwa kubadilisha kitambulisho ni mojawapo ya dosari za kawaida na kali zaidi za API, na hujificha kwenye vituo vya zamani vinavyotangulia viwango vyenu vya sasa. Uidhinishaji wa upande wa seva kwa kila ombi na kila kitu ndiyo kanuni, lakini sehemu ngumu ni kuthibitisha unashikilia kuvuka msimbo mkubwa, wa miaka mingi ulioandikwa na mikono mingi. Amua kama mtaweka mantiki ya uidhinishaji kati, kuongeza majaribio ya kiotomatiki yanayojaribu ufikiaji wa kuvuka wapangaji, au kuendesha majaribio yaliyolengwa dhidi ya API zenu za hatari ya juu kwanza. Leta orodha ya vituo vinavyofichua vitambulisho vya vitu na uvipange kwa unyeti wa wanachorudisha. Bila ufagiaji wa makusudi, mtaendelea kusafirisha dosari hii na kuigundua tu mtafiti au mshambulizi anapoigundua.

3. **Mpango wenu wa udhaifu mkubwa unaofuata wa utegemezi ni upi: mnaweza kupata na kupachika kila huduma iliyoathirika kwa kasi gani?** Dosari muhimu inapotua kwenye maktaba maarufu, kampuni zenye SBOM sahihi hutambua huduma zilizoathirika ndani ya saa huku zingine zikitumia wiki kutafuta, na pengo hilo la kasi huamua madhara mnayopata. Amua sasa kama mnazalisha Orodha ya Vifaa vya Programu kwa kila kitu, kama uchanganuzi wa utegemezi unaendesha kwenye kila bomba, na nani anamiliki uamuzi wa kupachika kwa dharura. Kwa wanunuzi wa serikali na wanaodhibitiwa, SBOM na asili iliyosainiwa zinazidi kuwa sharti la kufanya biashara, kwa hiyo utayari huu pia unalinda mapato. Leta jibu la uaminifu la mazoezi: chagua maktaba mnayotumia kwa upana na upime inachukua muda gani kuorodhesha kila huduma inayoisafirisha. Jibu likipimwa kwa siku, wekeza kwenye orodha na kusaini kabla tukio linalofuata halijawalazimisha.

4. **Mtahamaje kutoka siri tuli za muda mrefu hadi vitambulisho vya muda mfupi vinavyotolewa kiotomatiki, na mifumo ipi inazuia hilo leo?** Siri zilizoandikwa moja kwa moja na za muda mrefu ni chanzo cha kudumu cha uvunjaji, na suluhisho, vitambulisho vya muda mfupi vinavyotolewa kwa mahitaji, linategemea miundombinu ya utoaji ambayo mifumo ya zamani mara nyingi haiwezi kuitumia. Kwa timu kubwa hatari ni upokeaji usio sawa: jukwaa la kisasa linazungusha funguo kila saa huku huduma ya urithi bado ikisafirisha nenosiri la hifadhidata tuli kwenye faili ya usanidi. Amua mizigo ipi inaweza kutumia msimamizi wa siri au mfumo wa utambulisho wa mzigo sasa, ipi inahitaji uwekezaji kwanza, na nani anamiliki kitabu cha uendeshaji cha kuzungusha ufunguo unaposhukiwa kuvuja. Leta orodha ya kila kitambulisho kinachotumika, muda wake wa maisha, eneo lake la mlipuko kikifichuliwa, na kama uchanganuzi wa commit ungekinasa kabla ya kuunganisha. Katika mazingira ya mashirika makubwa na serikali, funga hili na ukaguzi: wakaguzi wanazidi kutarajia ushahidi wa kuzungusha, ufikiaji wenye wigo, na uandishi wa kumbukumbu za ufikiaji kwa kila siri, na kitambulisho tuli ambacho huwezi kukizungusha bila kukatika ni matokeo yanayosubiri kuandikwa.

5. **Wapi bado mnaendesha uthibitishaji wa papo hapo au usio thabiti, na mpango wa kuunganisha kwenye itifaki zilizothibitishwa ni upi?** Kujenga uthibitishaji ni mojawapo ya njia rahisi za kuingiza dosari fiche, zinazotumika, hata hivyo maeneo makubwa mengi yanabeba angalau mtiririko mmoja wa kuingia wa urithi unaotangulia uamuzi wa kusawazisha juu ya OAuth 2.0 na OIDC. Shinikizo zinazoshindana ni halisi: kuhamisha mtiririko wa zamani kunahatarisha kuvunja watumiaji na uunganishaji uliopo, wakati kuuacha mahali pake kunaweka lengo lenye thamani ya juu likiwa halijalindwa vizuri. Amua kama mtaunganisha kwenye mtoa utambulisho mmoja, kutekeleza MFA kwa usawa, na kuweka tarehe ya mwisho ya kustaafisha kila mtiririko maalumu, au kukubali vighairi vilivyoandikwa vyenye vidhibiti mbadala. Leta ramani ya kila njia ya uthibitishaji kwenye meli, ipi inatekeleza MFA, ipi inahifadhi nenosiri kwa hashi ya kisasa inayotumia kumbukumbu nyingi, na ipi ni maalumu. Kwa majalada ya mashirika makubwa na serikali, ongeza pembe ya uzingatiaji: viwango kama NIST SP 800-63 huweka matarajio madhubuti kwa uhakikisho wa utambulisho, na mtiririko wa papo hapo usioweza kuyaonyesha hautanusurika ukaguzi au mapitio ya idhini ya kuendesha.

6. **Mnathibitishaje vidhibiti hivi vinashikilia kwenye uzalishaji, na mnaweza kuthibitisha kwa ushahidi badala ya madai?** Kuandika chaguo-msingi salama si sawa na kujua kila huduma bado inaliheshimu, na vidhibiti huoza kimyakimya msimbo unapobadilika, vighairi vinapojilimbikiza, na vituo vipya vinaposafirishwa. Kwa timu kubwa swali ni ufikiaji: huduma zipi zinaendesha uchambuzi tuli, uchanganuzi wa utegemezi, na majaribio ya kidinamiki au ya kupenya, na mnajuaje zile zinazoruka si programu zenye hatari ya juu zaidi? Amua uthibitisho gani ni wa lazima kwenye bomba dhidi ya wa mara kwa mara, nani anapanga matokeo, na ushahidi gani mnaohifadhi kuonyesha kidhibiti kilijaribiwa na kupita katika tarehe fulani. Leta ramani yenu ya sasa ya ufikiaji, muda wenu wa wastani wa kurekebisha kwa ukali, na orodha ya programu zisizo na jaribio la hivi karibuni. Katika muktadha unaodhibitiwa na wa serikali, ushahidi huu si wa hiari: wakaguzi, maafisa wa idhini, na wachunguzi wa uvunjaji wote huuliza uthibitisho kwamba vidhibiti vilithibitishwa, na sera isiyo na rekodi za majaribio mara chache inawaridhisha.

## Mtazamo wa sekta

**Kampuni changa.** Ukiwa na wahandisi wawili au watatu na bila mtaalamu wa usalama, kiegemeo chako ni kurithi usalama badala ya kuujenga: pokea mtoa OIDC anayesimamiwa, tegemea mfumo wa kazi ambao ORM yake huweka vigezo kwenye hoja kwa chaguo-msingi, na uweke siri kwenye msimamizi wa siri wa jukwaa lako badala ya faili za `.env` ambazo mwenzako anaweza kuziweka kwa bahati mbaya. Washa uchanganuzi wa kiotomatiki wa utegemezi unaofungua maombi ya kuvuta ya kupachika, na uchukulie hilo kama la kutosha kwa sasa. Usijenge uthibitishaji wala kriptografia maalumu, kwa sababu hoja moja iliyoingizwa au ufunguo mmoja uliovuja unaweza kumaliza kampuni kabla haijapata wateja.

**Biashara ndogo.** Huenda huna mtaalamu wa usalama wa programu na bajeti ni finyu, kwa hiyo nunua vidhibiti vilivyojengwa ndani ya zana na majukwaa unayolipia tayari badala ya kuajiri kazi maalumu. Chagua mtoa utambulisho anayehifadhiwa mwenye MFA iliyojumuishwa, hifadhidata inayosimamiwa inayokuelekeza kwenye ufikiaji wenye vigezo, na mwenyeji wa hazina anayechanganua commit kwa siri zilizovuja moja kwa moja. Elekeza umakini wako adimu kwenye misingi ya OWASP Top 10 inayosababisha uvunjaji mwingi halisi, na upendelee wauzaji wanaosafirisha chaguo-msingi salama usizoweza kuzizima kwa kawaida.

**Biashara kubwa.** Kuvuka timu nyingi changamoto ni uthabiti: weka vidhibiti vya ASVS kwenye mifumo ya kazi ya njia iliyopakwa lami ili kila huduma mpya irithi hoja zenye vigezo, usimbaji wa pato, vikao salama, na uidhinishaji wa upande wa seva bure. Endesha SBOM sahihi na uchanganuzi wa utegemezi wa meli nzima ili udhaifu mkubwa unaofuata wa maktaba uwe suala la saa, si wiki, na weka sera ya uidhinishaji kati ili ufikiaji wa kuvuka wapangaji ujaribike. Sawazisha kwenye mtoa utambulisho mmoja mwenye MFA inayotekelezwa, na simamia usalama wa programu kama jalada linalotawaliwa lenye ngazi za ASVS zilizopangwa kwa hatari na ushahidi unaokaguliwa.

**Serikali.** Kanuni za ununuzi, uwazi, na uwajibikaji wa umma huumba vidhibiti unavyopaswa kuonyesha, si kutekeleza tu. Thibitisha huduma zinazomkabili raia dhidi ya OWASP ASVS kwa ngazi inayolingana na unyeti wa data, saini kila kitu kilichosambazwa na uthibitishe asili yake kwa SLSA kutimiza maagizo ya mnyororo wa ugavi, na utoe vitambulisho vya muda mfupi kutoka hazina ya kati yenye uandishi kamili wa kumbukumbu za ufikiaji. Tarajia kuwaonyesha wakaguzi na maafisa wa idhini mnyororo ulioandikwa wa utunzaji kutoka chanzo hadi uzalishaji, na upangilie uhakikisho wa utambulisho na viwango vilivyochapishwa kama NIST SP 800-63.

## Mifano

**Kampuni changa.** Timu ya SaaS ya wahandisi watatu inaruka kujenga kuingia kwake na kupokea mtoa OIDC anayesimamiwa siku ya kwanza, ikipata MFA na kuweka upya nenosiri kwa usalama bila kuandika msimbo muhimu kwa usalama ambao haiwezi kumudu kukosea. Inategemea ORM ya mfumo wa kazi ili hoja ziwe na vigezo kwa chaguo-msingi, inaweka siri kwenye msimamizi wa siri wa jukwaa badala ya faili za `.env` ambazo mwenzako anaweza kuziweka kwa bahati mbaya, na kuwasha uchanganuzi wa kiotomatiki wa utegemezi unaofungua ombi la kuvuta maktaba inapohitaji kupachikwa. Hakuna kati ya haya linalopunguza kasi ya timu, na linamaanisha ufunguo mmoja uliovuja au hoja moja iliyoingizwa haimalizi kampuni kabla haijapata wateja.

**Biashara kubwa.** Jukwaa la rejareja linalohudumia makumi ya mamilioni ya wanunuzi linasawazisha uthibitishaji kwenye OIDC kupitia mtoa utambulisho mmoja, likitekeleza MFA kwa wafanyakazi na uthibitishaji wa hatua ya juu kwa mabadiliko ya akaunti yenye thamani kubwa. Ufikiaji wote wa hifadhidata unapita kwenye ORM iliyosanidiwa kuweka vigezo kwenye hoja, na Sera ya Usalama wa Maudhui inaunga mkono usimbaji wa pato. Baada ya udhaifu uliotangazwa sana katika maktaba maarufu ya kumbukumbu, SBOM ya kampuni inaiwezesha kutambua kila huduma iliyoathirika ndani ya saa na kuipachika kwa siku mbili, huku washindani wasio na orodha wakitumia wiki kutafuta.

**Serikali.** Wakala wa manufaa wa shirikisho unajenga huduma zinazomkabili raia zilizothibitishwa dhidi ya OWASP ASVS Ngazi ya 2, na Ngazi ya 3 kwa vijenzi vinavyoshughulikia rekodi nyeti zaidi. Siri zinaishi kwenye hazina ya kati inayotoa vitambulisho vya muda mfupi; uchanganuzi wa commit unazuia ufunguo wowote uliovuja. Kila kitu kilichosambazwa kimesainiwa na asili yake kuthibitishwa kwa SLSA, ikitimiza agizo la shirikisho la minyororo ya ugavi ya programu inayothibitishika na kuwapa wakaguzi mnyororo wazi wa utunzaji kutoka chanzo hadi uzalishaji.

## Kesi ya biashara: sababu, ROI, na TCO

Matumizi ya usalama wa programu hununua chini kategoria inayoelekea zaidi na ghali zaidi ya uvunjaji. Jumla ya gharama ya umiliki inajumuisha zana (vichanganuzi, wasimamizi wa siri, watoa utambulisho), muda wa mhandisi wa kurekebisha matokeo, na msuguano mdogo wa chaguo-msingi salama. Dhidi ya hilo, pima gharama ya kuruka: uvunjaji wa uingizaji na udhibiti wa ufikiaji ulioharibika mara kwa mara hufichua mamilioni ya rekodi, ukichochea faini za udhibiti, arifa za lazima, hasara za ulaghai, mbio za urekebishaji, na uharibifu wa sifa unaokandamiza mapato kwa miaka.

ROI ni imara zaidi vidhibiti vinapokuwa vya kiotomatiki na vinavyotumika tena. Muunganisho mmoja uliosanidiwa vizuri wa utambulisho, safu moja iliyoimarishwa ya hoja kwenye mfumo wa kazi wa pamoja, na bomba moja linalozuia utegemezi wenye udhaifu hulinda meli nzima kwa gharama ya pembeni ndogo kwa kila huduma. Vidhibiti vya mnyororo wa ugavi hasa vimetoka kuwa vya hiari hadi muhimu: utegemezi ulioathiriwa unaweza kugeuza kila mteja wako kuwa mwathirika, na wadhibiti na wanunuzi wa mashirika makubwa wanazidi kudai SBOM na asili iliyosainiwa kama sharti la kufanya biashara. Unapoweka kesi kwa uongozi, funga uwekezaji na hatari mahususi zilizotajwa na mahitaji ya ununuzi na uzingatiaji yanayozuia mapato usipoyatimiza.

## Mifumo mibaya na mitego

- **Kuvumbua kriptografia au uthibitishaji wako.** Karibu daima huzalisha dosari fiche, zinazotumika.
- **Uthibitisho wa upande wa mteja tu.** Unakwepeka kwa urahisi; seva lazima ithibitishe upya kila kitu.
- **Usafishaji wa orodha ya kuzuia.** Kujaribu kuondoa herufi "mbaya" badala ya kuruhusu nzuri tu; washambulizi hupata mapengo.
- **Siri kwenye chanzo au faili za mazingira.** Chanzo cha kawaida zaidi cha uvujaji wa vitambulisho.
- **Kupuuza uidhinishaji kwenye ufikiaji wa vitu.** Kudhani mtumiaji aliyethibitishwa anaweza kufikia kitu chochote ambacho kitambulisho chake anaweza kukisia.
- **Utegemezi wa weka-na-sahau.** Kamwe kutosasisha vijenzi vya mtu wa tatu hadi uvunjaji ulazimishe.
- **Kuchukulia Top 10 kama mstari wa kumaliza.** Ni sakafu, si kiwango kamili; tumia ASVS kwa kina.
- **Kuandika data nyeti kwenye kumbukumbu.** Nenosiri, tokeni, na PII (taarifa zinazomtambulisha mtu) kwenye kumbukumbu huwa uvunjaji unaosubiri kutokea.

## Kielelezo cha ukomavu

**Ngazi ya 1: Kuanzisha.** Usalama wa programu unategemea maarifa ya msanidi mmoja mmoja na unaitikia baada ya matukio tu. Hakuna vidhibiti vya kawaida. Siri ziko kwenye chanzo. Utegemezi mara chache husasishwa. Uthibitishaji ni wa papo hapo na maalumu, na dosari za uingizaji au udhibiti wa ufikiaji ulioharibika hupatikana kwa bahati badala ya kwa mchakato.

**Ngazi ya 2: Kuendeleza.** Mazoea ya msingi yanaonekana lakini yanatofautiana timu hadi timu. Ufahamu wa OWASP Top 10 unaenea, baadhi ya ulinzi wa kiwango cha mfumo wa kazi upo, na msimamizi wa siri yupo lakini unatumika bila usawa. Uchanganuzi wa utegemezi unaendesha mara kwa mara. Mifumo mipya inapokea mtoa utambulisho wa kawaida, huku huduma za zamani zikiweka mtiririko wao wa kuingia wa papo hapo bila kuuguswa.

**Ngazi ya 3: Kusawazisha.** Vidhibiti vimeandikwa na kutekelezwa shirika zima. Mahitaji yanayotegemea ASVS yanawekwa kwa ngazi ya hatari, hoja zenye vigezo na usimbaji wa pato ni kawaida, na mtoa utambulisho wa kati mwenye MFA anahitajika. Siri zinasimamiwa na kuchanganuliwa kiotomatiki, SBOM zinazalishwa, na uchanganuzi wa utegemezi unaendesha kwenye kila bomba.

**Ngazi ya 4: Kusimamia.** Mazoea yanapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Ufikiaji wa uchanganuzi na majaribio, muda wa wastani wa kurekebisha kwa ukali, sehemu ya huduma zinazorithi chaguo-msingi za njia iliyopakwa lami, umri wa kuzungusha vitambulisho na siri, na ulinganifu wa ASVS vyote vinafuatiliwa kwenye dashibodi. Vighairi vinaandikwa na tarehe za kuisha, kuteleza kutoka kipimo cha msingi huchochea hatua, na matoleo yanadhibitiwa kwa vizingiti vilivyofafanuliwa vya usalama badala ya maamuzi ya busara.

**Ngazi ya 5: Kuratibu.** Usalama unaboreshwa kila wakati na kuunganishwa kuvuka shirika. Chaguo-msingi salama zimejengwa ndani ya mifumo ya kazi ya njia iliyopakwa lami ili njia salama iwe ya kiotomatiki, vitambulisho vya muda mfupi vinatumika kila mahali, na uhakikisho kamili wa mnyororo wa ugavi wenye kusaini na asili (SLSA) ni kawaida. Uthibitisho ni endelevu, jibu kwa udhaifu mpya ni la haraka na linapimwa, na kila tukio linalisha violezo vya pamoja ili marekebisho moja yaimarishe meli nzima.

## Mawazo ya kujadili

1. Mantiki ya uidhinishaji inapaswa kuishi wapi ili iwe thabiti na inayodumishika kuvuka huduma nyingi?
2. Mnapaswa kusasisha utegemezi kwa ukali kiasi gani kwa kuzingatia biashara kati ya mfiduo na msukosuko?
3. Ngazi ipi ya ASVS inafaa kwa kila darasa la programu katika jalada lenu?
4. Mnaondoaje siri za muda mrefu bila kuunda miundombinu dhaifu ya utoaji?
5. Ingechukua nini kwa shirika lenu kuzalisha na kutumia SBOM na asili kwa kila kitu?
6. Mnazuiaje chaguo-msingi salama zisizimwe chini ya shinikizo la utoaji?

## Mambo muhimu ya kukumbuka

- OWASP Top 10 ni maarifa muhimu; ASVS inatoa kiwango kinachojaribika.
- Weka tabaka za uthibitisho wa ingizo, vigezo, na usimbaji wa pato kushinda uingizaji na XSS.
- Tumia itifaki zilizothibitishwa (OAuth 2.0, OIDC) na utekeleze MFA; kamwe usijenge uthibitishaji kutoka mwanzo.
- Tekeleza uidhinishaji upande wa seva kwa kila ombi na kila kitu.
- Weka siri nje ya chanzo, zisimamie kati, na uzungushe hadi vitambulisho vya muda mfupi.
- Mnyororo wa ugavi ni uso mkuu wa shambulio; tumia SBOM, SCA, kusaini, na asili (SLSA).
- Vidhibiti vya kiotomatiki, vinavyotumika tena hulinda meli nzima kwa gharama ya pembeni ndogo kwa kila huduma.

## Marejeo na usomaji zaidi

- OWASP, *Top 10 Web Application Security Risks*
- OWASP, *Application Security Verification Standard (ASVS)*
- OWASP, *Cheat Sheet Series* (Input Validation, Authentication, Authorization, Secrets Management)
- Dafydd Stuttard and Marcus Pinto, *The Web Application Hacker's Handbook*
- Aaron Parecki, *OAuth 2.0 Simplified*
- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines*
- Cloud Native Computing Foundation and OpenSSF, *SLSA framework* and *Supply-chain Security guidance*
