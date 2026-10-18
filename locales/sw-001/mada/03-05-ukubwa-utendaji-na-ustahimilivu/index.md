# 3.5 Ukubwa, utendaji, na ustahimilivu

## Muhtasari na msukumo

[Uwezo wa kupanuka](https://en.wikipedia.org/wiki/Scalability), utendaji, na ustahimilivu ni sifa tatu tofauti, na watu mara nyingi huzichanganya. **Utendaji** ni jinsi mfumo unavyojibu haraka na kazi kiasi gani unafanya kwa kila kipimo cha rasilimali. **Uwezo wa kupanuka** ni jinsi unavyodumisha utendaji vizuri mzigo unapokua. **Ustahimilivu** ni jinsi unavyoendelea kufanya kazi, au kudhoofika kwa neema, mambo yanaposhindwa. Mfumo unaweza kuwa wa haraka lakini usiopanuka (mzuri kwa mzigo mdogo, unaanguka kwa mzigo mkubwa), unaopanuka lakini dhaifu (unashughulikia ujazo lakini unaanguka kijenzi kimoja kikishindwa), au ustahimilivu lakini polepole. Shirika kubwa linahitaji vyote vitatu, vilivyobuniwa ndani tangu mwanzo, kwa sababu kuvirudisha baada ya uzinduzi ni ghali na kunasumbua.

Kwa mifumo ya mashirika makubwa na serikali, matokeo ya kukosea haya ni ya hadharani na makali. Fikiria lango la manufaa linalopinda siku ya kwanza ya mpango mpya, mfumo wa kuwasilisha kodi unaoisha muda siku ya mwisho, au jukwaa la malipo linalozimika wakati wa kilele cha ununuzi. Hizi ni kushindwa kunakofanya vichwa vya habari, kuchochea uchunguzi, na kumomonyoa uaminifu wa umma. Mifumo hii pia inakabiliana na mzigo wenye vilele vingi, mara nyingi uliowekewa muda kisheria (tarehe za mwisho za kuwasilisha, vipindi vya kujiandikisha, siku za mshahara) na wajibu mkali wa upatikanaji na kurejesha. Lazima upange uwezo kwa vilele vinavyotabirika, udhoofike kwa neema chini ya visivyotabirika, na urejeshe ndani ya mipaka iliyofafanuliwa ya muda na upotevu wa data baada ya maafa. Huu ni uhandisi wenye kipimo cha uwajibikaji kwa umma.

Sura hii inashughulikia kupanua kwa upana dhidi ya kwa wima, kutokuwa na hali na [kugawanya](https://en.wikipedia.org/wiki/Shard_(database_architecture)) kama vichocheo vya ukubwa, [kusawazisha mzigo](https://en.wikipedia.org/wiki/Load_balancing_(computing)), [kupanua kiotomatiki](https://en.wikipedia.org/wiki/Autoscaling) na upangaji wa uwezo, uhandisi wa utendaji wenye bajeti wazi, mifumo ya ustahimilivu na [uhandisi wa machafuko](https://en.wikipedia.org/wiki/Chaos_engineering), na [urejeshaji baada ya maafa](https://en.wikipedia.org/wiki/Disaster_recovery) wa kanda nyingi ukiwekwa kwa RTO, RPO, na mwendelezo wa biashara. Ujumbe unaounganisha ni kwamba sifa hizi ni zao la usanifu wa makusudi na majaribio endelevu, si matumaini.

*Angalia pia:* sura ya 3.3 (mifumo iliyosambazwa), sura ya 9.1 (uhandisi wa kutegemewa kwa tovuti), na sura ya 9.2 (uonekanaji na ufuatiliaji).

## Kanuni kuu

- **Buni kwa kupanua kwa upana, si kwa wima.** Kupanua kwa wima kuna dari na [nukta moja ya kushindwa](https://en.wikipedia.org/wiki/Single_point_of_failure); kupanua kwa upana ndiyo njia ya kufikia ukubwa mkubwa, ustahimilivu.
- **Kutokuwa na hali ndicho kichocheo cha kupanua kwa upana.** Ombi lolote likiweza kwenda kwa tukio lolote, unaweza kuongeza na kuondoa uwezo kwa uhuru.
- **Huwezi kuboresha usichokipima.** Kazi ya utendaji huendeshwa na uchunguzi na majaribio ya mzigo dhidi ya bajeti wazi, kamwe si kwa kubahatisha.
- **Kila kitu kinashindwa; buni kwa hilo.** Dhania vijenzi vitashindwa na ujenge ili mfumo unusurike kushindwa kwao.
- **Kudhoofika kwa neema kunashinda kushindwa kwa ngumu.** Mfumo unaofanya kazi kwa sehemu na kuacha vipengele visivyo muhimu ni bora kuliko kukatika kamili.
- **Uwezo hupangwa, vilele hufyonzwa.** Tabiri mzigo unaotabirika; tumia kupanua kiotomatiki na nafasi ya ziada kwa kilichobaki.
- **Malengo ya kurejesha ni maamuzi ya biashara.** RTO na RPO huchaguliwa na biashara dhidi ya gharama, kisha kuhandisiwa kwayo.
- **Jaribu ustahimilivu kwa makusudi.** Hujui mfumo ni ustahimilivu hadi uufanye ushindwe kwa makusudi.

## Mapendekezo

### Pendelea kupanua kwa upana na ubuni huduma zisizo na hali

Kupanua kwa wima (mashine kubwa zaidi) ni rahisi na wakati mwingine ndiyo hatua sahihi ya kwanza, lakini inagonga dari ngumu, inakuwa ghali kupita kiasi kwenye ncha ya juu, na inaacha nukta moja ya kushindwa. **Kupanua kwa upana** (mashine nyingi nyuma ya kisawazishaji cha mzigo) hupanuka mbali zaidi na kuboresha upatikanaji, kwa sababu kupoteza tukio moja kunanusurika. Sharti la awali ni **kutokuwa na hali**. Usihifadhi kikao cha mteja wala hali ya ombi kwenye tukio; ipeleke kwenye hifadhi ya pamoja (hifadhidata, kache, tokeni). Huduma zisizo na hali zinaweza kuongezwa, kuondolewa, kubadilishwa, na kusawazishwa mzigo kwa uhuru, ndiyo inayowezesha kupanua kiotomatiki na usambazaji wa kuzunguka. Pale hali lazima ipangwe kwa vipande, **gawanya** kwa ufunguo unaosambaza mzigo sawasawa na kuweka data inayohusiana kwenye kipande kimoja.

### Sawazisha mzigo, panua kiotomatiki, na panga uwezo

Weka **kisawazishaji cha mzigo** mbele ya kila ngazi iliyopanuliwa kusambaza trafiki na kuelekeza kuzunguka matukio yasiyo na afya kupitia ukaguzi wa afya. Sanidi **kupanua kiotomatiki** kuongeza uwezo kiashiria cha mbele (CPU, kina cha foleni ya maombi, ucheleweshaji) kinapovuka kizingiti na kuondoa mzigo unaposhuka. Rekebisha kasi ya kupanua na vipindi vya baridi ili usichelewe nyuma ya kilele wala kuyumba. Kupanua kiotomatiki si mbadala wa **upangaji wa uwezo**. Kwa vilele vinavyotabirika, muhimu kwa biashara (tarehe za mwisho za kodi, vipindi vya kujiandikisha, matukio ya mauzo), tabiri mzigo, tayarisha au pasha moto uwezo mapema, na ujaribu mzigo kwa lengo hilo mapema. Kupanua kiotomatiki peke yake hakuwezi kuitikia mara moja badiliko la ghafla la hatua, na kuanza baridi kunaongeza ucheleweshaji hasa unapoweza kuumudu kidogo zaidi. Daima weka nafasi ya ziada. Kuendesha kwa 100% hakuacha nafasi ya kufyonza vilele au kushindwa.

### Handisi utendaji dhidi ya bajeti wazi

Weka **bajeti za utendaji** (malengo madhubuti kama ucheleweshaji wa p95 wa API chini ya ms 200, ukurasa shirikishi chini ya sekunde 2, au gharama kwa muamala chini ya kizingiti) na uzitekeleze katika majaribio na ufuatiliaji ili kurudi nyuma kufeli bomba badala ya kuwafikia watumiaji. Endesha uboreshaji kwa **upimaji**. Chunguza ili kupata kizuizi halisi, ambacho mara chache kipo unapokisia, na ujaribu mzigo kupata mahali mfumo unavunjika na jinsi unavyotenda karibu na kikomo hicho. Lenga njia muhimu na mkia (p95/p99), kwa sababu kwa ukubwa ucheleweshaji wa mkia unatawala uzoefu wa mtumiaji. Boresha kizuizi kikubwa zaidi kwanza, pima tena, na usimame ukitimiza bajeti. Kuboresha kupita kiasi msimbo ambao tayari unatosha ni juhudi iliyopotea.

### Jenga mifumo ya ustahimilivu na uthibitishe kwa uhandisi wa machafuko

Tumia mifumo ya ustahimilivu kutoka mifumo iliyosambazwa: muda wa kuisha, majaribio ya kurudia yaliyofungwa yenye kurudi nyuma, [vivunja mzunguko](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern) (vinavyoshindwa haraka utegemezi usipokuwa na afya), na vyumba vilivyotengwa (vinavyotenga makundi ya rasilimali ili kushindwa kumoja kusiweze kuchosha yaliyobaki), pamoja na **kudhoofika kwa neema** (acha au rahisisha vipengele visivyo muhimu chini ya mkazo: zima mapendekezo, hudumia maudhui yaliyohifadhiwa kwenye kache, weka kazi zisizo za dharura kwenye foleni) na **kumwaga mzigo** (kataa au punguza maombi ya ziada kulinda kiini badala ya kuporomoka kabisa). Ondoa nukta moja ya kushindwa kupitia ziada kwenye kila ngazi. Kisha **thibitisha** ustahimilivu kwa uhandisi wa machafuko. Ingiza kushindwa kwa makusudi (ua matukio, ongeza ucheleweshaji, kata utegemezi, shindwa eneo) katika majaribio yanayodhibitiwa, ukianzia kwenye majaribio na kukomaa hadi siku za mchezo za uzalishaji, kuthibitisha mfumo unatenda kama ulivyobuniwa. Ustahimilivu ambao haujawahi kujaribiwa ni dhana tu.

### Panga kanda nyingi, urejeshaji baada ya maafa, na mwendelezo wa biashara

Amua malengo ya kurejesha waziwazi: **RTO** (Recovery Time Objective, unaweza kuwa chini kwa muda gani) na **RPO** (Recovery Point Objective, unaweza kumudu kupoteza data kiasi gani). Haya ni maamuzi ya biashara yenye athari za moja kwa moja za gharama, na yanaendesha usanifu. Chaguo huanzia kwa gharama na kasi: chelezo-na-rejesha (nafuu zaidi, polepole zaidi), taa ya majaribio, tayari ya joto, na kanda nyingi hai-hai (ghali zaidi, karibu sifuri RTO/RPO). Chagua ngazi ambayo umuhimu wa kila mfumo unahalalisha. Si kila kitu kinahitaji hai-hai. Nakili data kuvuka kanda sambamba na RPO uliyochagua, otomatisha kubadilisha, na, zaidi ya yote, **jaribu kubadilisha mara kwa mara**. Urejeshaji baada ya maafa usiojaribiwa hushindwa kwa uhakika unapohitajika hatimaye. Funika yote haya katika **mpango wa mwendelezo wa biashara** unaojumuisha watu, mawasiliano, na njia mbadala za mkono, si teknolojia tu.

## Mabadilishano: faida na hasara

| Chaguo | Faida | Hasara |
|---|---|---|
| Kupanua kwa wima | Rahisi, hakuna badiliko la msimbo, juhudi ndogo ya awali | Dari ngumu, ghali juu, nukta moja ya kushindwa |
| Kupanua kwa upana | Ukubwa karibu usio na kikomo, huboresha upatikanaji | Inahitaji kutokuwa na hali, kusawazisha mzigo, uendeshaji zaidi |
| Kupanua kiotomatiki | Hulinganisha gharama na mahitaji, hushughulikia mzigo unaobadilika | Huitikia kwa kuchelewa; kuanza baridi; inaweza kuyumba ikirekebishwa vibaya |
| Kanda nyingi hai-hai | Karibu sifuri RTO/RPO, hunusurika kupoteza kanda | Gharama na ugumu wa juu zaidi, uthabiti wa data mgumu |
| DR ya chelezo-na-rejesha | Nafuu zaidi, rahisi zaidi | RTO ndefu, dirisha kubwa zaidi la kupoteza data |

Biashara kuu ni gharama dhidi ya uhakikisho. Kila ongezeko la nafasi ya ukubwa, utendaji, na uwezo wa kurejesha hugharimu fedha na ugumu, na malipo si ya mstari. Kutoka upatikanaji wa 99.9% hadi 99.99%, au kutoka RTO ya saa hadi sekunde, kunaweza kuzidisha gharama. Nidhamu ni kupima ukubwa wa kila uwekezaji kwa umuhimu halisi wa mfumo na uvumilivu wa biashara kwa kukatika na kupoteza data, badala ya kuhandisi kila kitu kwa ngazi ya juu kabisa kwa silika. Mfumo wa malipo unaomkabili raia unastahili ziada ya hai-hai; zana ya ndani ya ripoti haistahili.

## Maswali ya kujadili na timu yako

1. **Tukio lenu kubwa la mwisho lilipotokea, ni ipi kati ya tatu (utendaji, ukubwa, ustahimilivu) ilishindwa kweli, na je, mlirekebisha sahihi?** Sura inazitenganisha kwa makusudi: mfumo unaweza kuwa wa haraka lakini ukaporomoka chini ya mzigo, kupanuka lakini ukaanguka kijenzi kimoja kikifa, au kunusurika kushindwa huku ukiwa polepole. Timu mara nyingi hutambua vibaya, zikiongeza uwezo kwa tatizo la ustahimilivu au kuimarisha mfumo ambao ulikuwa tu na rasilimali chache kwa kilele. Pitia matukio mawili makali ya mwisho na utaje ni sifa ipi ilivunjika na jibu liliboresha nini kweli. Tofauti hubadilisha suluhisho: kutokuwa na hali na kugawanya kwa ukubwa, ziada na vivunja mzunguko kwa ustahimilivu, uchunguzi na bajeti kwa utendaji. Kupata kategoria sahihi ni tofauti kati ya kutumia kwa tiba na kutumia kwa dalili.

2. **Je, kurudi nyuma kwa utendaji kunafeli bomba lenu, au kunawafikia watumiaji kabla mtu yeyote hajaona?** Bajeti ya utendaji (ucheleweshaji wa p95, muda wa ukurasa kuwa shirikishi, gharama kwa muamala) inalinda watumiaji tu ikitekelezwa kiotomatiki, ili badiliko linalovunja ifeli ujenzi badala ya kusafirishwa. Katika timu kubwa yenye wachangiaji wengi, ucheleweshaji hupenya kupitia commit elfu ndogo, na bila lango mkia huoza polepole hadi uzinduzi uufichue. Leta bajeti zenu za sasa na uangalie kama zimefungwa kwenye CI na ufuatiliaji, na kama zinalenga p95 na p99 badala ya wastani, kwa sababu mkia ndio watumiaji wanaohisi kwa ukubwa. Pale hakuna bajeti, kuiweka ndiyo hatua ya kwanza. Utekelezaji ndio unaogeuza nia njema kuwa sifa inayonusurika ukuaji wa timu.

3. **Chini ya mkazo, nini kinaachwa kwanza, na je, mlibuni mpangilio huo au mtaugundua kwenye kukatika?** Kudhoofika kwa neema na kumwaga mzigo kunamaanisha mfumo unaacha kazi isiyo muhimu kulinda kiini, lakini tu ikiwa mmeamua mapema kipi ni muhimu. Kwa huduma inayomkabili raia, orodha hiyo mara nyingi ni uamuzi wa sera: kuwasilisha marejesho ya kodi lazima kunusurike hata kama dashibodi za hali na utafutaji wa kihistoria vinazimika. Hakuna aliyechagua, mfumo unaacha chochote kinachoshindwa kwanza, ambacho kinaweza kuwa hasa kile watumiaji wanachohitaji zaidi. Orodhesha vipengele vyenu kwa mpangilio wa kipaumbele na uthibitishe usanifu unaweza kuacha vile vya kipaumbele cha chini (majibu yaliyohifadhiwa kwenye kache, mapendekezo yaliyozimwa, kazi zisizo za dharura zilizowekwa kwenye foleni) bila kuchukua njia muhimu pamoja. Kisha ujaribu chini ya mzigo halisi, kwa sababu kudhoofika kusikojaribiwa ni matumaini tu.

4. **Kwa mfumo wenu muhimu zaidi, RTO na RPO ni nini, nani alichagua namba hizo kweli, na lini mara ya mwisho mlithibitisha mnaweza kuzitimiza?** Recovery Time Objective (unaweza kuwa chini kwa muda gani) na Recovery Point Objective (unaweza kumudu kupoteza data kiasi gani) ni maamuzi ya biashara yenye athari za moja kwa moja za gharama, hata hivyo katika timu kubwa mara nyingi huvumbuliwa na yeyote aliyeandika kitabu cha uendeshaji badala ya kumilikiwa na watu wanaowajibika kwa huduma. Mvuto unaoshindana ni gharama dhidi ya uhakikisho: kupunguza RTO kutoka saa hadi sekunde au RPO kutoka dakika hadi sifuri kunaweza kuzidisha bili ya miundombinu, kwa hiyo namba sahihi ni ile ambayo biashara italipia kweli, si ya kuvutia zaidi. Leta malengo yaliyoandikwa, tarehe ya jaribio la mwisho halisi la kubadilisha, na muda uliopimwa na upotevu wa data ambao jaribio hilo lilizalisha, kwa sababu lengo lisilojaribiwa ni tamanio. Katika mazingira ya mashirika makubwa na serikali namba hizi zinaweza kuwekwa na sheria, mkataba, au SLA, kwa hiyo taja nani anaziidhinisha na kama mazoezi ya mwisho yalitimiza wajibu au yalikosa kimyakimya.

5. **Kwa kilele chenu kikubwa zaidi kinachotabirika, mnaamini kupanua kiotomatiki kuitikie papo hapo, au mmetabiri mzigo, mmetayarisha mapema, na kujaribu mzigo kwa lengo hilo?** Kupanua kiotomatiki huitikia kwa kuchelewa na kuanza baridi huongeza ucheleweshaji hasa unapoweza kuumudu kidogo zaidi, kwa hiyo badiliko la hatua linalojulikana (tarehe ya mwisho ya kuwasilisha, kipindi cha kujiandikisha, tukio la mauzo) ndilo hasa kisa ambapo kupanua kwa kuitikia kunashindwa na upangaji wa uwezo wa makusudi unashinda. Mvutano ni gharama: kupasha moto uwezo kwa kilele kunamaanisha kulipia nafasi ya ziada isiyotumika mwaka mwingi, na kishawishi ni kutumaini kupanua kiotomatiki kutafunika bure. Leta namba za kilele cha mwaka jana, utabiri wa mwaka huu pamoja na ukuaji, na matokeo ya jaribio la mzigo lililoendeshwa kwa mara kadhaa ya utabiri huo badala ya trafiki ya wastani ya leo. Kwa huduma ya serikali au ya shirika kubwa inayokabili kilele kilichowekewa muda kisheria, ongeza matokeo ya kukosea, kwa kuwa lango la manufaa au mfumo wa kodi unaopinda siku ya kwanza unakuwa uchunguzi wa umma, si alasiri ya polepole tu.

6. **Mmewahi kushindwa kijenzi kwa makusudi kwenye uzalishaji, na je, ngazi ya ziada ya kila mfumo inalingana na umuhimu na gharama yake?** Ustahimilivu ambao haujawahi kujaribiwa ni dhana, na ngazi unazoweza kununua huanzia chelezo-na-rejesha ya bei nafuu kupitia tayari ya joto hadi kanda nyingi hai-hai ya ghali, kwa hiyo nidhamu ni kutumia uhakikisho mahali panapohalalishwa badala ya kupamba kila kitu au kutolinda chochote. Mazingatio yanayoshindana ni eneo la mlipuko na bajeti: majaribio ya machafuko lazima yawe na vizuizi na swichi ya kusitisha, na hai-hai kwa zana ya ndani ya ripoti ni upotevu huku chelezo pekee kwa jukwaa la malipo ni uzembe. Leta orodha ya nukta zenu moja za kushindwa, ngazi ya ziada ya kila mfumo muhimu, na ushahidi wa uingizaji wa mwisho unaodhibitiwa wa kushindwa na ulichofichua. Katika majalada ya mashirika makubwa na serikali, oanisha kila ngazi na kiwango cha umuhimu kilichoandikwa ili mkaguzi aone kwamba fedha zinafuata hatari, na hakuna anayelazimika kutetea matumizi kwa mara ya kwanza wakati wa kukatika.

## Mtazamo wa sekta

**Kampuni changa.** Huwezi kutabiri kama uzinduzi unaleta usajili hamsini au hamsini elfu, kwa hiyo nunua ukubwa badala ya kuujenga: endesha huduma zisizo na hali nyuma ya kisawazishaji cha mzigo kinachosimamiwa na uache jukwaa lipanuke kiotomatiki kwa kiwango cha maombi. Weka bajeti moja ya wastani ya utendaji na uchague hifadhi za data zinazosimamiwa ili kilele kisilazimishe usanifu upya saa nane usiku. Ruka urejeshaji wa kanda nyingi na programu za machafuko kwa sasa; weka chelezo zilizojaribiwa na utumie umakini wako adimu wa kihandisi kwenye bidhaa, si ziada ambayo trafiki yako haijaihalalisha bado.

**Biashara ndogo.** Bila mtaalamu wa kutegemewa na bajeti finyu, chaguo la kununua-dhidi-ya-kujenga linaegemea sana kununua: jukwaa linalosimamiwa au mkusanyiko wa serverless hufanya kupanua na kubadilisha kuwa kazi ya mtoaji, na kanda moja inayoendeshwa vizuri kwa kawaida inatosha. Weka ustahimilivu kama ahadi chache madhubuti unazoweza kuzitimiza, kama chelezo ya kila usiku ambayo umewahi kurejesha mara moja na dirisha la kweli la kurejesha ulilowasilisha kwa wateja. Epuka kulipia hai-hai au majaribio ya mzigo endelevu ambayo huna trafiki wala wafanyakazi wa kuyahalalisha.

**Biashara kubwa.** Tatizo ni uthabiti kuvuka timu nyingi: sawazisha bajeti za utendaji zinazotekelezwa kwenye CI, maktaba ya pamoja ya mifumo ya ustahimilivu (muda wa kuisha, vivunja mzunguko, vyumba vilivyotengwa), na ngazi ya ziada iliyoandikwa kwa kila mfumo iliyofungwa na umuhimu wake. Hifadhi kanda nyingi hai-hai kwa huduma za ngazi ya kwanza, endesha programu ya uhandisi wa machafuko yenye vizuizi na siku za mchezo za uzalishaji, na uchukulie upangaji wa uwezo kwa vilele vinavyojulikana kama nidhamu iliyopangwa badala ya wazo la baadaye. Tawala RTO na RPO kati ili kila mfumo muhimu uwe na malengo yanayomilikiwa, yaliyojaribiwa ambayo mkaguzi anaweza kuyathibitisha.

**Serikali.** Mzigo mara nyingi umewekewa muda kisheria na wajibu wa upatikanaji ni wa kisheria, kwa hiyo upangaji wa uwezo hauwezi kutegemea kupanua kiotomatiki kuitikia papo hapo: tabiri kilele cha tarehe ya mwisho, tayarisha mapema, na ujaribu mzigo mbali juu ya utabiri. Ununuzi unapaswa kubainisha RTO, RPO, na ratiba ya kubadilisha kulikofanyiwa mazoezi kama mahitaji ya kimkataba, si ahadi za muuzaji, na unapaswa kuepuka kufungwa kwa kanda moja kwa huduma muhimu. Amua mapema njia ipi ni muhimu kisheria (kuwasilisha marejesho, kudai manufaa) ili kudhoofika kuache dashibodi za hali na utafutaji kwanza, na uwe wazi kwa umma kuhusu kukatika na kurejesha badala ya kutumaini hakuna anayegundua.

## Mifano

**Kampuni changa.** Kampuni changa ndogo inayozindua kwenye Product Hunt haiwezi kutabiri kama itapata usajili hamsini au hamsini elfu, kwa hiyo inaweka huduma zake zisizo na hali nyuma ya kisawazishaji cha mzigo kinachosimamiwa na kuacha jukwaa lipanuke kiotomatiki kwa kiwango cha maombi. Inaweka bajeti moja ya wastani ya utendaji (kurasa zinajibu chini ya ms 300 kwenye asilimia ya 95) na kuchagua hifadhidata inayosimamiwa ili kilele cha trafiki kisilazimishe usanifu upya saa nane usiku. Kilele cha siku ya uzinduzi kinapofika, tovuti inapunguza kasi kidogo badala ya kuanguka, na timu inatumia siku kuzungumza na watumiaji wapya badala ya kupambana na kukatika.

**Biashara kubwa.** Kampuni ya vyombo vya habari vya utiririshaji inaendesha huduma zisizo na hali kuvuka kanda nyingi nyuma ya kusawazisha mzigo kwa dunia nzima, ikipanuka kiotomatiki kwa kiwango cha maombi kufuata wimbi la kila siku la saa za kilele cha jioni. Bajeti za utendaji zinadhibiti kila toleo kwa ucheleweshaji wa kuanza wa p99. Chini ya kushindwa kwa kanda, trafiki inahamia kiotomatiki kwa kanda zenye afya, na vipengele visivyo muhimu (sanaa ya kibinafsi, kuonyesha upya mapendekezo) vinadhoofika kwanza kulinda uchezaji. Kampuni inaendesha majaribio endelevu ya machafuko kwenye uzalishaji, ikiua matukio mara kwa mara na kuingiza ucheleweshaji, ili kushindwa halisi kusitofautishwe na mazoezi na kusisababishe kukatika kunakoonekana na wateja.

**Serikali.** Wakala wa kodi unajua mfumo wake wa kuwasilisha unakabili kilele kikubwa, kilichowekwa kisheria cha tarehe ya mwisho kila mwaka. Badala ya kutegemea kupanua kiotomatiki kuitikia papo hapo, unatabiri mzigo wa kilele kutoka miaka iliyopita, unatayarisha uwezo wiki mapema, na kujaribu mzigo hadi 150% ya utabiri. Usanifu hauna hali nyuma ya visawazishaji vya mzigo pamoja na kanda ya pili ya tayari ya joto. RTO na RPO zimewekwa na sera (si zaidi ya dakika 15 za kukatika na karibu hakuna upotevu wa data kwa marejesho yaliyowasilishwa), na kubadilisha kunafanyiwa mazoezi kila robo mwaka. Chini ya mzigo uliokithiri, vipengele visivyo muhimu (dashibodi za hali, utafutaji wa kihistoria) vinaachwa kwanza ili kuwasilisha marejesho, njia muhimu kisheria, ibaki ikipatikana.

## Kesi ya biashara: sababu, ROI, na TCO

Ukubwa, utendaji, na ustahimilivu ni visa vya kawaida ambapo gharama ya kushindwa inazidi sana gharama ya kinga. Lakini kinga inaonekana kwenye bajeti na kushindwa ni kwa uwezekano tu, ndiyo maana vinafadhiliwa kidogo kwa muda mrefu hadi maafa ya kwanza. Gharama ya kupokea ni halisi: miundombinu ya ziada, uwezo wa kanda nyingi, zana za majaribio ya mzigo na machafuko, na muda wa kihandisi wa kujenga kutokuwa na hali na mifumo ya ustahimilivu. Gharama ya *kutowekeza* ni kukatika kwa hadhi ya juu wakati wa mahitaji ya kilele: mapato yaliyopotea kwa dakika kwa biashara, wajibu wa kisheria uliokosekana na uchunguzi wa umma kwa serikali, adhabu za [makubaliano ya kiwango cha huduma](https://en.wikipedia.org/wiki/Service-level_agreement) (SLA), na uharibifu wa kudumu wa sifa.

Weka hoja kwa uongozi kwa namba ambazo biashara tayari inazielewa. Kadiria gharama ya saa moja ya kukatika wakati wa kilele (miamala iliyopotea, adhabu, urekebishaji, sifa), kisha ilinganishe na gharama ya kila mwaka ya ziada na majaribio yanayozuia hilo. Kwa mifumo muhimu kinga karibu daima ni sehemu ndogo ya tukio moja kubwa. Funga RTO na RPO na fedha wazi: mapato kiasi gani au miamala mingapi kwa saa ya kukatika, na upotevu wa data kiasi gani unavumilika kisheria au kibiashara. Wasilisha utendaji kama kiegemeo cha mapato na kuridhika, kwa kuwa mifumo ya haraka zaidi hubadilisha vizuri zaidi na kugharimu kidogo kwa kila muamala, na wasilisha ustahimilivu kama bima ambayo malipo yake ni madogo ikilinganishwa na hasara inayofunika. Hoja yenye nguvu zaidi ni kwamba sifa hizi ni za bei nafuu kubuni ndani na za maangamizi kurudisha baada ya kukatika kunakolazimisha suala.

## Mifumo mibaya na mitego

- **Vikao vya kunata na hali ndani ya tukio.** Kuhifadhi hali ya kikao kwenye seva, kuzuia kupanua kwa upana kwa uhuru na kubadilisha matukio kwa usalama.
- **Kupanua kiotomatiki kama upangaji wa uwezo.** Kudhani kupanua kiotomatiki kutafyonza kilele cha badiliko la hatua linalojulikana ambacho ni polepole mno kuitikia.
- **Kuendesha moto bila nafasi ya ziada.** Kufanya kazi kwa matumizi karibu ya 100%, bila kuacha chochote cha kufyonza vilele au kushindwa.
- **Kuboresha bila kuchunguza.** Kurekebisha msimbo usio kizuizi huku halisi kikibaki bila kuguswa.
- **Kupuuza mkia.** Kuripoti ucheleweshaji wa wastani huku watumiaji wa p99 wakiteseka; wastani huficha maumivu kwa ukubwa.
- **Urejeshaji baada ya maafa usiojaribiwa.** Mpango wa DR na chelezo ambazo hazijawahi kutumika na zitashindwa zitakapohitajika.
- **Nukta moja za kushindwa.** Kisawazishaji kimoja cha mzigo, msingi mmoja wa hifadhidata, kanda moja: kijenzi kisicho na ziada kinachoangusha kila kitu.
- **Uhandisi wa machafuko bila vizuizi.** Kuingiza kushindwa bila udhibiti wa eneo la mlipuko au swichi ya kusitisha, kusababisha kukatika hasa ulikokusudia kuzuia.

## Kielelezo cha ukomavu

- **Ngazi ya 1: Kuanzisha.** Ya papo hapo na ya kuitikia. Tukio moja au lililopanuliwa kwa wima, na hali ikishikiliwa kwenye seva. Hakuna majaribio ya mzigo, hakuna bajeti za utendaji, na hakuna urejeshaji baada ya maafa zaidi ya chelezo za mara kwa mara ambazo hakuna aliyewahi kuzirejesha. Kushindwa kwa kijenzi chochote husababisha kukatika kamili, na matatizo ya ukubwa yanagunduliwa kwenye uzalishaji.
- **Ngazi ya 2: Kuendeleza.** Mazoea ya msingi yanaonekana lakini yanatofautiana kwa timu. Baadhi ya huduma zimepanuliwa kwa upana na hazina hali nyuma ya kisawazishaji cha mzigo, na kupanua kiotomatiki kwa msingi kwenye chache. Majaribio ya mzigo hufanyika kabla ya uzinduzi mkubwa lakini si mara kwa mara, na chelezo zipo huku urejeshaji baada ya maafa ukiwa umeandikwa lakini mara chache unafanyiwa mazoezi. Kile timu moja inafanya vizuri nyingine haijaanza.
- **Ngazi ya 3: Kusawazisha.** Mazoea yameandikwa na kutekelezwa shirika zima. Uwezo unapangwa kwa vilele vinavyojulikana wenye nafasi ya ziada, bajeti za utendaji zinatekelezwa kwenye CI ili kurudi nyuma kufeli ujenzi, na mifumo ya ustahimilivu (muda wa kuisha, majaribio ya kurudia yaliyofungwa, vivunja mzunguko, vyumba vilivyotengwa) pamoja na kudhoofika kwa neema ndiyo chaguo-msingi. RTO na RPO zinafafanuliwa kwa kila mfumo, ngazi za ziada zinagawiwa kwa umuhimu, na kubadilisha kwa urejeshaji baada ya maafa kunajaribiwa kwa ratiba ya kawaida kuvuka timu.
- **Ngazi ya 4: Kusimamia.** Sifa zinapimwa na kudhibitiwa dhidi ya vipimo vya msingi. Timu zinafuatilia ucheleweshaji wa p95 na p99, bajeti za makosa, na matumizi na nafasi ya ziada dhidi ya utabiri, na kutoa tahadhari juu ya ukiukaji badala ya kuugundua kwenye uzinduzi. Nyakati za kubadilisha zilizojaribiwa zinalinganishwa na RTO na RPO lengwa, vizingiti vya kudhoofika na kumwaga mzigo vinathibitishwa kwa vipimo, na maamuzi ya kwenda au kutokwenda kwa matoleo na uwezo yanaendeshwa na data. Namba zinapoteleza kutoka kipimo cha msingi, pengo linaonekana na linamilikiwa badala ya kufichwa nyuma ya wastani.
- **Ngazi ya 5: Kuratibu.** Ukubwa, utendaji, na ustahimilivu vinaboreshwa kila wakati na kuunganishwa kuvuka shirika. Kanda nyingi hai-hai zinatumika popote umuhimu unahalalisha, uhandisi wa machafuko unaendeshwa mfululizo ikijumuisha siku za mchezo za uzalishaji, na utabiri wa uwezo unalisha moja kwa moja upangaji na ununuzi. Ustahimilivu unathibitishwa kwa kuendelea, malengo ya kurejesha yanatimizwa na kuthibitishwa mfululizo, na usanifu hubadilika mifumo ya mzigo na picha ya hatari inapohama, ukifungwa na mwendelezo wa biashara na upangaji wa hatari.

## Mawazo ya kujadili

1. Ni huduma zipi zenu bado zinashikilia hali kwenye tukio, na nini kinawazuia kuzifanya zisiwe na hali?
2. Kwa mfumo wenu muhimu zaidi, RTO na RPO ni nini, nani aliziweka, na lini mara ya mwisho mlithibitisha mnaweza kuzitimiza?
3. Je, kupanua kiotomatiki kunawalinda kweli dhidi ya kilele chenu kikubwa zaidi kinachojulikana, au mnakitegemea kufanya kitu ambacho hakiwezi?
4. Nukta yenu moja iliyobaki ya kushindwa iko wapi, na mpango wa kuiondoa ni upi?
5. Mnapima na kupanga bajeti ya ucheleweshaji wa p99, au mnajificha nyuma ya wastani?
6. Mmewahi kushindwa kijenzi kwa makusudi kwenye uzalishaji? Kama sivyo, mnajuaje ustahimilivu wenu unafanya kazi?

## Mambo muhimu ya kukumbuka

- Tofautisha utendaji, uwezo wa kupanuka, na ustahimilivu; mfumo mkubwa unahitaji vyote vitatu, vilivyobuniwa ndani tangu mwanzo.
- Kupanua kwa upana na huduma zisizo na hali ndiyo msingi wa ukubwa, upatikanaji, na usambazaji salama.
- Changanya kupanua kiotomatiki na upangaji halisi wa uwezo na nafasi ya ziada kwa vilele vinavyotabirika, muhimu kwa biashara.
- Endesha utendaji kwa uchunguzi na majaribio ya mzigo dhidi ya bajeti wazi, ukilenga njia muhimu na mkia.
- Jenga ustahimilivu kwa muda wa kuisha, vivunja mzunguko, vyumba vilivyotengwa, kudhoofika kwa neema, na ziada, kisha uuthibitishe kwa uhandisi wa machafuko.
- Weka RTO na RPO kama maamuzi ya biashara, handisi DR ilingane na umuhimu wa kila mfumo, na ujaribu kubadilisha mara kwa mara.

## Marejeo na usomaji zaidi

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Michael Nygard, *Release It!: Design and Deploy Production-Ready Software*
- Betsy Beyer et al. (Google), *Site Reliability Engineering* and *The Site Reliability Workbook*
- Casey Rosenthal and Nora Jones, *Chaos Engineering*
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud*
- John Allspaw, *The Art of Capacity Planning*
- Ilya Grigorik, *High Performance Browser Networking*
- Nassim Nicholas Taleb, *Antifragile*
