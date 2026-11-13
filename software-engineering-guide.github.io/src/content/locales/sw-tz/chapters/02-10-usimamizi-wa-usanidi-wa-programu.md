# 2.10 Usimamizi wa usanidi wa programu

## Muhtasari na msukumo

[Usimamizi wa usanidi wa programu](https://en.wikipedia.org/wiki/Software_configuration_management) (SCM) ni nidhamu ya kutambua vipengele vya mfumo wa programu, kudhibiti jinsi vinavyobadilika, kurekodi hali ya kila badiliko, na kuthibitisha kwamba kile ulichokijenga na kutoa kinalingana na ulichokusudia. Hujibu swali linalosikika rahisi lakini linakuwa gumu kwa ukubwa: hasa nini kiko katika toleo hili, kilifikaje huko, na nani aliidhinisha? [SWEBOK](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) inachukulia SCM kama eneo la msingi la maarifa kwa sababu iliyo wazi: kila shughuli nyingine ya kihandisi inahitaji usanidi thabiti, unaojulikana wa kufanya kazi dhidi yake.

Katika timu kubwa, SCM ni tishu ya kuunganisha inayoweka maelfu ya sehemu zinazosonga zikiwa thabiti. Msimbo wa chanzo, maktaba, picha za kontena, fasili za miundombinu, data ya usanidi, nyaraka, na vitu vya majaribio vyote hubadilika kwa saa zake zenyewe, na mfumo uliotolewa ni mchanganyiko mmoja mahususi wa matoleo mahususi ya vyote. Bila usimamizi wa usanidi wa makusudi, mchanganyiko huo haujulikani na hauwezi kuzalishwa upya. Huwezi kuunda upya toleo la zamani, kufuatilia kasoro hadi badiliko lililoisababisha, wala kusema kwa kujiamini kinachoendesha kwenye uzalishaji.

Mazingira ya mashirika makubwa na ya serikali huinua dau. Programu zinazodhibitiwa na za sekta ya umma lazima zionyeshe kwamba mabadiliko yaliidhinishwa, yalipitiwa, na kurekodiwa; kwamba ujenzi uliotolewa unafuatiliwa hadi mahitaji na chanzo vilivyoidhinishwa; na kwamba hakuna kilichoingia kwenye mfumo bila udhibiti. Hapa SCM ni mfumo wa ushahidi kama ulivyo wa kihandisi. [Udhibiti wa matoleo](https://en.wikipedia.org/wiki/Version_control) (sura ya 2.6) husimamia historia ya chanzo; SCM hutawala usanidi mzima na mchakato unaodhibitiwa unaobadilika kwao. Umefungamana kwa karibu na [miundombinu kama msimbo](https://en.wikipedia.org/wiki/Infrastructure_as_code) (sura ya 8.2), mabomba ya utoaji (sura ya 8.1), na ukaguzi na uhakikisho (sura ya 10.2).

## Kanuni kuu

- Kila kitu kinachoamua tabia ya mfumo ni [kipengee cha usanidi](https://en.wikipedia.org/wiki/Configuration_item) kilicho chini ya udhibiti, si msimbo wa chanzo tu.
- [Kipimo cha msingi](https://en.wikipedia.org/wiki/Baseline_(configuration_management)) ni nukta ya marejeo inayojulikana, iliyokubaliwa; mabadiliko hufanywa dhidi ya vipimo vya msingi kwa makusudi, si kwa ghafla.
- Mabadiliko hudhibitiwa na kurekodiwa, hayazuiwi; lengo ni badiliko lililoidhinishwa, linalofuatilika.
- Uhasibu wa hali unamaanisha unaweza kujibu daima nini kiko katika usanidi na historia yake ya mabadiliko ni ipi.
- Ukaguzi huthibitisha kwamba mfumo uliojengwa na kutolewa unalingana na usanidi uliorekodiwa na mahitaji yaliyoidhinishwa.
- Uwezo wa kuzalishwa upya hauwezi kujadiliwa: toleo lolote lililotolewa lazima liweze kujengwa upya kutoka ingizo zinazodhibitiwa.
- Otomatisha utambuzi, kurekodi, na uthibitisho; uhasibu wa mkono haupanuki na haunusurike ukaguzi.

## Mapendekezo

### Fafanua mchakato wa SCM na ukabidhi umiliki

Andika mpango wa SCM unaosema nini kiko chini ya udhibiti wa usanidi, jinsi vipengee vinavyotambuliwa, jinsi mabadiliko yanavyopendekezwa na kuidhinishwa, na jinsi hali inavyorekodiwa na kukaguliwa. Kabidhi umiliki wazi, kama msimamizi wa usanidi au timu inayowajibika, ili SCM isiwe kazi ya kila mtu na kwa hiyo ya hakuna. Panua mchakato kwa hatari: zana ndogo ya ndani inahitaji udhibiti mwepesi, wakati mfumo muhimu kwa usalama au unaodhibitiwa unahitaji bodi na rekodi rasmi. Funga mpango kwenye kiwango kinachotambuliwa kama IEEE 828 ili wakaguzi na washirika waweze kuufuata.

### Tambua vipengee vya usanidi na uweke vipimo vya msingi

Orodhesha vipengee vya usanidi vinavyoamua jinsi mfumo unavyotenda: chanzo, utegemezi, hati za ujenzi, picha za kontena, fasili za miundombinu, data ya usanidi, miundo, na nyaraka muhimu. Mpe kila kimoja kitambulisho thabiti na mpango wa matoleo. Weka vipimo vya msingi katika nukta za maana (toleo lililotolewa, seti ya mahitaji iliyoidhinishwa, ujenzi uliothibitishwa) ili uwe na marejeo yaliyokubaliwa ya kubadilisha dhidi yake na kurudi. Kipimo cha msingi hakibadiliki: ukishakitangaza, hukihariri. Unakibatilisha tu kwa kipimo kipya cha msingi kilichoundwa kupitia mchakato wa mabadiliko.

### Dhibiti mabadiliko kupitia mchakato uliofafanuliwa na bodi zinazofaa

Elekeza mabadiliko ya vipengee vinavyodhibitiwa kupitia njia iliyofafanuliwa: pendekezo, tathmini ya athari, idhini, utekelezaji, na uthibitisho. Kwa vipengee vya hatari kubwa, tumia [bodi ya udhibiti wa mabadiliko](https://en.wikipedia.org/wiki/Change_control_board) (CCB) inayopima gharama, hatari, na ratiba kabla ya kuidhinisha badiliko. Rekebisha ukubwa wa bodi: lango jepesi la kiotomatiki kwa mabadiliko ya kawaida ya msimbo, na CCB rasmi ya kuvuka kazi kwa mabadiliko yanayogusa vipimo vya msingi, violesura, au tabia inayodhibitiwa. Rekodi kila uamuzi na hoja nyuma yake, na uunganishe maamuzi muhimu ya usanidi na rekodi za maamuzi (sura ya 1.6) ili hoja ibaki.

### Dumisha uhasibu wa hali ya usanidi

Weka rekodi sahihi, inayoweza kuulizwa ya kila kipengee cha usanidi: toleo lake la sasa, kipimo cha msingi kinachokibeba, na maombi ya mabadiliko yaliyotumika kwake. Uhasibu huu wa hali ndio unaokuruhusu kujibu, wakati wowote, toleo lina nini na lilifikaje huko. Zalisha rekodi kiotomatiki kutoka zana zako za rekodi (udhibiti wa matoleo, bomba, hazina ya vitu vilivyotengenezwa) badala ya kudumisha lahajedwali sambamba inayoteleza kutoka uhalisia. Rekodi hii ndiyo uti wa mgongo wa ufuatiliaji kutoka hitaji hadi badiliko hadi ujenzi hadi usambazaji.

### Fanya ukaguzi wa usanidi

Thibitisha mambo mawili kwa ratiba ya kawaida. Ukaguzi wa usanidi wa kiutendaji unathibitisha kwamba usanidi unatenda jinsi mahitaji yake yanavyobainisha. Ukaguzi wa usanidi wa kimwili unathibitisha kwamba vitu vilivyotolewa vinalingana na usanidi uliorekodiwa: kwamba ujenzi ulitoka kwenye chanzo na utegemezi vilivyorekodiwa na hauna kisichohesabiwa. Otomatisha sehemu kubwa kadiri uwezavyo: [ujenzi unaoweza kuzalishwa upya](https://en.wikipedia.org/wiki/Reproducible_builds), jumla za ukaguzi za vitu, orodha za vifaa vya programu (SBOM), na uthibitisho wa asili hugeuza ukaguzi kutoka ukaguzi wa mkono hadi ukaguzi endelevu.

### Simamia matoleo na utoaji kama matukio yanayodhibitiwa

Chukulia toleo kama kipimo mahususi, kilichotambuliwa cha msingi kinachotolewa kupitia mchakato unaorudiwa. Weka matoleo yako katika matoleo waziwazi, zalisha orodha au muswada wa vifaa unaoeleza hasa kilichomo, na rekodi uhusiano kutoka toleo hadi marekebisho ya chanzo hadi kitu kilichosambazwa. Saini na weka jumla za ukaguzi kwenye vitu vilivyotolewa ili yeyote chini ya mkondo athibitishe uadilifu wake. Funga usimamizi wa matoleo na bomba la utoaji (sura ya 8.1) ili kupandisha kupitia mazingira kuwe kwenyewe kudhibitiwa, kurekodiwa, na kunakoweza kutenguliwa.

### Chagua na uunganishe zana za SCM

Tegemea zana zinazootomatisha utambuzi, udhibiti, uhasibu, na ukaguzi badala ya kutegemea nidhamu peke yake: udhibiti wa matoleo kwa chanzo, hazina za vitu na picha kwa binary, bomba lisilobadilika kwa ujenzi, miundombinu kama msimbo kwa mazingira, na zana za utegemezi na SBOM kwa asili. Ziunganishe ili badiliko moja litiririke kwa kufuatilika kutoka commit hadi toleo lililosambazwa. Unachokitafuta ni mnyororo wa zana ambapo rekodi ya usanidi ni zao la pembeni la kufanya kazi, si kazi ya kikarani tofauti.

## Mabadilishano: faida na hasara

| Chaguo | Faida | Hasara |
|---|---|---|
| Bodi rasmi za udhibiti wa mabadiliko | Idhini imara na njia ya ukaguzi; hatari inapimwa kabla ya badiliko | Uwezo wa kupitisha wa polepole; mzigo ukitumika kwa mabadiliko ya kawaida |
| Malango mepesi ya kiotomatiki | Mtiririko wa haraka; mzigo mdogo; yanapanuka kwa mabadiliko mengi | Dhaifu kwa vipimo vya msingi vya hatari kubwa; mazingatio kidogo |
| Vipimo vya msingi visivyobadilika kwa ukali | Nukta za marejeo zinazoweza kuzalishwa, kukaguliwa | Zinahitaji nidhamu na zana; msuguano zikitumika kupita kiasi |
| Uhasibu wa hali wa kiotomatiki | Rekodi sahihi, ya sasa daima; tayari kwa ukaguzi | Uwekezaji wa awali wa zana na uunganishaji |
| Rekodi za usanidi za mkono | Rahisi kuanza; hakuna zana zinazohitajika | Zinateleza kutoka uhalisia; zinashindwa kwa ukubwa na chini ya ukaguzi |

Mabadilishano ya msingi ni udhibiti dhidi ya mtiririko. Udhibiti mzito wa mabadiliko hutoa uhakikisho imara lakini hupunguza kasi ya utoaji. Udhibiti mwepesi hutiririka haraka lakini hudhoofisha ufuatiliaji. Jibu si kuchagua moja kwa jumla; ni kupanga udhibiti kwa hatari: otomatisha mabadiliko ya kawaida kupitia malango ya haraka, na uhifadhi bodi rasmi na vipimo vya msingi visivyobadilika kwa vipengee ambapo idhini na uwezo wa kukaguliwa vinajalisha kweli. Mabadilishano ya pili ni uwekezaji wa awali wa zana dhidi ya gharama endelevu ya kikarani na hatari ya ukaguzi. Uhasibu wa kiotomatiki unagharimu zaidi kuweka na kidogo zaidi sana kuishi nao.

## Maswali ya kujadili na timu yako

1. **Hasa nini kinastahili kuwa kwenye orodha yetu ya vipengee vya usanidi, na nani anamiliki uamuzi kitu kipya kinapoonekana?** SCM hufanya kazi tu ikiwa orodha ya vipengee vinavyodhibitiwa inalingana na seti ya vitu vinavyoamua tabia kweli, na katika mfumo mkubwa seti hiyo ni kubwa kuliko timu nyingi zinavyofikiria: chanzo, utegemezi, hati za ujenzi, picha za kontena, fasili za miundombinu, miundo, bendera za vipengele, na data ya usanidi inayobadilisha kimyakimya kile programu inachofanya. Hakuna anayemiliki orodha ikiteleza, na kipengee kilichowaangusha kwenye uzalishaji kinageuka kuwa kile ambacho hakuna aliyefikiria kukidhibiti. Leta orodha yenu ya sasa kwenye mkutano na uwinde vipengee vinavyoamua tabia ambavyo havimo. Kabidhi mmiliki anayewajibika (msimamizi wa usanidi au timu iliyotajwa) ili kuongeza kipengee kipya kiwe uamuzi wa makusudi, si ajali, kwa sababu SCM ambayo ni kazi ya kila mtu ni kazi ya hakuna.

2. **Tunaweza kuthibitisha kitu kilichosambazwa kilitoka kwenye chanzo na bomba tunalodhani, na je, uthibitisho huo ungenusurika kuchezewa?** Uwezo wa kuzalishwa upya na ufuatiliaji ndiyo hoja nzima ya SCM, na toleo kali la swali ni kama unaweza kuunganisha binary inayoendesha na commit mahususi na ujenzi uliotekelezwa kwa ushahidi, si dai. Katika mfumo unaodhibitiwa au wenye thamani ya juu hii pia ni ulinzi wako wa mnyororo wa ugavi: uthibitisho wa asili uliosainiwa, jumla za ukaguzi za vitu, na orodha ya vifaa vya programu hugeuza "tuna uhakika kiasi" kuwa kitu ambacho mkaguzi au mshughulikiaji wa matukio anaweza kukithibitisha. Leta toleo lenu la mwisho na ujaribu kulifuata nyuma kutoka kitu kilichosambazwa hadi badiliko lililoidhinishwa. Hatua yoyote ikiwa dai la mkono badala ya kiungo kilichorekodiwa, kinachothibitishika, hapo ndipo mshambulizi au kosa la uaminifu linaweza kuteleza kitu bila kuonekana, na kulifunga kunamaanisha kuunganisha kusaini na asili kwenye bomba ili rekodi iwe zao la pembeni la utoaji.

3. **Je, yeyote anaweza kuhariri toleo mahali pake leo, na hilo lingefanya nini kwa uwezo wetu wa kuliamini?** Kipimo cha msingi kina manufaa tu ikiwa hakibadiliki: mara "toleo" linapoweza kuhaririwa baada ya tukio, huwezi tena kulizalisha upya wala kulitegemea kama marejeo, na kila ukaguzi unaofuata unakuwa uchimbaji wa kiakiolojia. Kushindwa kwa kawaida ni usanidi uliohaririwa moja kwa moja kwenye uzalishaji au lebo iliyohamishwa kimyakimya, ambayo ndiyo njia ya mkato inayohisi isiyo na madhara na inayofanya toleo lisiwezekane kujengwa upya baadaye. Leta jibu la uaminifu kwenye mkutano: nani ana ufikiaji wa kubadilisha kipimo cha msingi kilichosambazwa bila kupitia mchakato wa mabadiliko, na je, imewahi kutokea? Suluhisho ni kufanya vipimo vya msingi visivyobadilika kweli na kuelekeza kila badiliko kupitia pendekezo, tathmini ya athari, idhini, na uthibitisho, ukipanga ukali ili mabadiliko ya kawaida yatiririke kupitia malango ya haraka ya kiotomatiki huku mabadiliko ya kipimo cha msingi na yaliyodhibitiwa yakienda kwa bodi.

4. **Je, uhasibu wetu wa hali ya usanidi unazalishwa kiotomatiki kutoka zana zetu za rekodi, au unadumishwa kwa mkono, na umeteleza kiasi gani kutoka kinachosambazwa kweli?** Uhasibu wa hali ni rekodi inayokuruhusu kujibu, wakati wowote, toleo lina nini na lilifikaje huko, na katika mfumo mkubwa rekodi hiyo inaaminika tu ikiwa inatokana na kazi badala ya kuchapwa kwenye lahajedwali sambamba. Mvuto unaoshindana ni kwamba rejista iliyodumishwa kwa mkono huhisi nafuu kuanza na inayonyumbulika, wakati kuiotomatisha kunamaanisha kuunganisha udhibiti wa matoleo, bomba, na hazina ya vitu ili rekodi iwe zao la pembeni la utoaji. Leta rejista mnayoitegemea leo, chagua matoleo matatu ya hivi karibuni kwa nasibu, na uangalie kama matoleo yaliyorekodiwa, vipimo vya msingi, na maombi ya mabadiliko yaliyotumika yanalingana na yale zana zinasema yalisafirishwa. Kwa programu ya shirika kubwa au serikali, rekodi ya hali inayotofautiana na uhalisia si tatizo la usafi, ni matokeo ya ukaguzi yanayosubiri, kwa sababu mkaguzi anayenasa pengo moja anaacha kuamini maelezo yote na kukuomba uyajenge upya kwa mkono.

5. **Je, udhibiti wetu wa mabadiliko umepangwa kwa hatari, au kiwango kilekile cha taratibu kinatawala kila badiliko bila kujali linagusa nini?** Udhibiti na mtiririko vinavutana: bodi rasmi ya udhibiti wa mabadiliko hupima gharama, hatari, na ratiba kabla ya kuidhinisha badiliko, lakini kutumia taratibu hizo kwa marekebisho ya kawaida ya msimbo kunaongeza kuchelewa tu, huku kusukuma kipimo cha msingi cha pamoja au mtiririko wa malipo unaodhibitiwa kupitia lango la haraka la kiotomatiki kunaondoa mazingatio hasa pale unapoyahitaji. Njia za kushindwa ni sawia: uzito wa sare ambao watu hujifunza kuuzunguka, au ulegevu wa sare unaoruhusu badiliko la hatari kubwa kuteleza bila kuchunguzwa. Leta sampuli ya mabadiliko ya robo iliyopita yaliyopangwa kwa kila moja liligusa nini, na uangalie kama ukali uliopokea ulilingana na hatari yake. Katika mazingira yanayodhibitiwa au ya sekta ya umma, taja madarasa gani ya vipengee lazima yafike kwa bodi ya kuvuka kazi na yapi yanaweza kutiririka kupitia malango ya kiotomatiki, na urekodi mpangilio huo waziwazi, kwa sababu "tunatumia busara" si udhibiti ambao mkaguzi au chombo cha usimamizi kinaweza kuthibitisha.

6. **Lini mara ya mwisho tuliendesha ukaguzi wa usanidi wa kiutendaji na wa kimwili, na ushahidi kiasi gani ungekuwa rekodi hai badala ya ujenzi upya?** Ukaguzi wa usanidi wa kiutendaji unathibitisha mfumo unatenda jinsi mahitaji yake yanavyobainisha, na ukaguzi wa usanidi wa kimwili unathibitisha vitu vilivyotolewa vinalingana na usanidi uliorekodiwa na havina kisichohesabiwa; viruke na unaamini kwamba vipimo vyako vya msingi na uhasibu wa hali ni vya uaminifu bila kuvikagua kamwe. Mvutano ni gharama: ukaguzi wa mkono ni wa polepole na wenye maumivu, ndiyo hasa kwa nini timu huuahirisha, na njia ya kutoka ni kuotomatisha ukaguzi kwa ujenzi unaoweza kuzalishwa upya, jumla za ukaguzi za vitu, orodha za vifaa vya programu, na uthibitisho wa asili ili uthibitisho uwe endelevu. Leta toleo lenu la hivi karibuni na ujaribu kuzalisha, papo hapo, ufuatiliaji wa hitaji-hadi-badiliko-hadi-ujenzi-hadi-usambazaji na uthibitisho wa kitu-hadi-chanzo. Kwa programu za mashirika makubwa na serikali, njia hii ya ushahidi ndiyo uthibitisho na usimamizi unadai, kwa hiyo swali la uaminifu ni kama ukaguzi wa kesho ungejibiwa kutoka rekodi mnazoshikilia tayari au zoezi la kiakiolojia msiloweza kulimudu.

## Mtazamo wa sekta

**Kampuni changa.** Weka SCM nyepesi lakini halisi. Weka chanzo, fasili za miundombinu, na data ya usanidi kwenye udhibiti wa matoleo, na ufanye kila toleo kuwa ujenzi wenye lebo unaozalishwa na bomba moja badala ya kitu kilichokusanywa kwa mkono. Ruka bodi za udhibiti wa mabadiliko na vipimo rasmi vya msingi, ambavyo ni vya kupindukia kwa ukubwa wako, lakini kamwe usimruhusu yeyote ahariri usanidi moja kwa moja kwenye uzalishaji, kwa sababu njia hiyo moja ya mkato ndiyo inayofanya toleo lisiwezekane kuzalishwa upya mteja anapokutana na hitilafu Jumanne ijayo.

**Biashara ndogo.** Bila msimamizi wa usanidi na bajeti finyu, tegemea zana zinazokupa SCM karibu bure: jukwaa la udhibiti wa matoleo linalohifadhiwa, bomba lake lililojengwa ndani, na hazina ya vitu, ili rekodi ya usanidi iwe zao la pembeni badala ya kazi unayopaswa kuiajiria. Nunua uwezo huu ukiwa umejengwa ndani ya zana unazolipia tayari badala ya kujenga mchakato maalumu. Tumia umakini wako adimu kwa tabia mbili zinazojalisha zaidi, matoleo yenye lebo yanayoweza kuzalishwa upya na kuweka usanidi unaobadilisha tabia nje ya marekebisho ya mkono ya uzalishaji.

**Biashara kubwa.** Tatizo ni uthabiti kuvuka timu nyingi: mpango wa pamoja wa SCM, uainishaji wa pamoja wa vipengee vya usanidi, udhibiti wa mabadiliko uliopangwa kwa ngazi, na uhasibu wa hali unaozalishwa kiotomatiki kutoka udhibiti wa matoleo, hazina ya vitu, na bomba. Hifadhi bodi rasmi za udhibiti wa mabadiliko na vipimo vya msingi visivyobadilika kwa majukwaa ya pamoja na mtiririko unaodhibitiwa, acha mabadiliko ya kawaida yatiririke kupitia malango ya kiotomatiki, na usawazishe asili iliyosainiwa na SBOM ili toleo la timu yoyote lifuatiliwe na mkaguzi yeyote auulize rekodi hai badala ya kuagiza ujenzi upya.

**Serikali.** Kanuni za ununuzi, uwazi, na uwajibikaji wa umma huunda mchakato. Fuata mpango rasmi wa SCM uliopangiliwa na kiwango kinachotambuliwa kama IEEE 828, weka vipengee vya usanidi kama vipimo vya msingi katika hatua za kimkataba, na uelekeze kila badiliko la kipimo cha msingi kinachodhibitiwa kupitia bodi inayorekodi athari, uamuzi, na hoja. Hitaji vitu vilivyotolewa viweze kuzalishwa upya kutoka ingizo zinazodhibitiwa, viwe na jumla za ukaguzi, na vifuatilike mwanzo hadi mwisho kutoka hitaji lililoidhinishwa hadi ujenzi uliotolewa, kwa sababu njia hiyo iliyoandikwa ya ushahidi ndiyo uthibitisho, ukaguzi, na usimamizi wa umma vinadai.

## Mifano

**Kampuni changa.** Kampuni changa ya watu sita inaweka SCM yake nyepesi lakini halisi: chanzo, fasili za miundombinu, na data ya usanidi vyote vinaishi kwenye udhibiti wa matoleo, na kila toleo ni ujenzi wenye lebo, wenye toleo unaozalishwa na bomba lilelile badala ya kukusanywa kwa mkono. Mteja anaporipoti hitilafu iliyotokea Jumanne iliyopita, wanafuatilia kitu kilichosambazwa hadi commit hasa ndani ya dakika badala ya kubahatisha. Wanaruka bodi za udhibiti wa mabadiliko na vipimo rasmi vya msingi, ambavyo vingekuwa vya kupindukia kwa ukubwa wao, lakini wanakataa kumruhusu yeyote ahariri usanidi moja kwa moja kwenye uzalishaji, kwa sababu njia hiyo moja ya mkato ndiyo inayofanya toleo lisiwezekane kuzalishwa upya baadaye.

**Biashara kubwa.** Kampuni kubwa ya huduma za kifedha inaweka vitu vyote vinavyoweza kusambazwa, fasili za miundombinu, na data ya usanidi chini ya udhibiti wa usanidi. Kila toleo ni kipimo cha msingi kisichobadilika, chenye toleo chenye orodha ya vifaa vya programu iliyozalishwa, na kila kitu kilichosambazwa kinabeba uthibitisho wa asili uliosainiwa unaokiunganisha na marekebisho mahususi ya chanzo na ujenzi wa bomba. Mabadiliko ya kawaida ya programu yanatiririka kupitia malango ya bomba ya kiotomatiki, huku mabadiliko ya vipimo vya msingi vya jukwaa la pamoja au mtiririko wa malipo unaodhibitiwa yakienda kwa bodi ya udhibiti wa mabadiliko. Uhasibu wa hali unazalishwa kiotomatiki kutoka udhibiti wa matoleo, hazina ya vitu, na bomba, kwa hiyo wakaguzi wanauliza rekodi hai badala ya kuomba ujenzi upya.

**Serikali.** Programu ya ulinzi inafuata mpango rasmi wa SCM uliopangiliwa na IEEE 828. Vipengee vya usanidi vinaorodheshwa na kuwekwa kama vipimo vya msingi katika hatua za kimkataba, na bodi ya udhibiti wa mabadiliko inaidhinisha kila badiliko la kipimo cha msingi kinachodhibitiwa, ikirekodi athari, uamuzi, na hoja. Ukaguzi wa usanidi wa kiutendaji unathibitisha mfumo uliotolewa unatimiza mahitaji yaliyobainishwa, na ukaguzi wa usanidi wa kimwili unathibitisha vitu vilivyotolewa vinalingana hasa na usanidi uliorekodiwa. Matoleo yanaweza kuzalishwa upya kutoka ingizo zinazodhibitiwa, yana jumla za ukaguzi, na yanafuatilika mwanzo hadi mwisho, kutoka hitaji lililoidhinishwa kupitia ombi la badiliko hadi ujenzi uliotolewa, ambayo ndiyo hasa njia ya ushahidi ambayo uthibitisho na usimamizi vinadai.

## Kesi ya biashara: sababu, ROI, na TCO

SCM ipo kudhibiti hatari na gharama kwa maisha ya mfumo. Mapato yanatokana na uwezo wa kuzalishwa upya na ufuatiliaji: unaweza kuunda upya toleo lolote, kufuatilia kasoro hadi mabadiliko yaliyozisababisha, na kujibu maswali ya ukaguzi kutoka rekodi badala ya uchimbaji wa kiakiolojia. Hilo hupunguza muda wa kutambua matukio, hupunguza gharama na urefu wa ukaguzi, na huzuia darasa ghali la kushindwa ambapo hakuna anayeweza kusema kinachoendesha au jinsi ya kukijenga upya.

Jumla ya gharama ya umiliki inapendelea uendeshaji wa kiotomatiki. Rekodi za usanidi za mkono ni nafuu kuanza na ghali kudumisha kwa kuendelea, na zinashindwa hasa unapozihitaji zaidi, wakati wa tukio au ukaguzi, kwa sababu zimeteleza kutoka uhalisia. Utambuzi, uhasibu, na ukaguzi wa kiotomatiki unagharimu zaidi mapema lakini unageuza rekodi ya usanidi kuwa zao la pembeni la karibu bure la bomba la utoaji. Kujenga hoja kwa uongozi, weka SCM kama udhibiti unaofanya matoleo yaweze kuzalishwa upya na mabadiliko yaweze kukaguliwa, na uupime dhidi ya gharama ya matoleo yasiyoweza kuzalishwa upya, ukaguzi mrefu, na hatari ya uzingatiaji ya badiliko lisilodhibitiwa.

## Mifumo mibaya na mitego

- **Usanidi kwa maarifa ya kikabila:** maudhui halisi ya toleo yanaishi kichwani mwa mhandisi tu, si katika rekodi yoyote.
- **Vipimo vya msingi vinavyobadilika:** "toleo" linahaririwa mahali pake, kwa hiyo haliwezi tena kuzalishwa upya wala kuaminiwa kama marejeo.
- **Data ya usanidi isiyodhibitiwa:** msimbo uko katika udhibiti wa matoleo lakini usanidi unaobadilisha tabia yake unahaririwa ghafla kwenye uzalishaji.
- **Maigizo ya udhibiti wa mabadiliko:** bodi inayothibitisha kila kitu kwa muhuri wa mpira, ikiongeza kuchelewa bila uchunguzi halisi.
- **Uhasibu wa hali wa mkono:** lahajedwali ya matoleo inayotofautiana kimyakimya na kinachosambazwa kweli.
- **Ujenzi usioweza kuzalishwa upya:** matoleo yasiyoweza kujengwa upya kutoka ingizo zinazodhibitiwa, kwa hiyo ukaguzi na kujenga upya ni kubahatisha.
- **Matoleo yasiyofuatilika:** hakuna uhusiano kutoka kitu kilichosambazwa hadi marekebisho ya chanzo, ombi la badiliko, na idhini.

## Kielelezo cha ukomavu

- **Ngazi ya 1 (Kuanzisha):** SCM ni ya papo hapo na ya kuitikia. Chanzo tu kinadhibitiwa; matoleo yanakusanywa kwa mkono; hakuna vipimo vya msingi, hakuna rekodi ya kuaminika ya kinachosambazwa, na hakuna njia ya kuzalisha upya ujenzi wa zamani.
- **Ngazi ya 2 (Kuendeleza):** Mazoea ya msingi yapo lakini yanatofautiana timu hadi timu. Baadhi ya mifumo hufafanua vipengee vya usanidi na mchakato wa mabadiliko na kuweka matoleo katika matoleo, vipimo vya msingi vipo hapa na pale, lakini rekodi ni za mkono kwa sehemu na ukali wa udhibiti hauna uthabiti kuvuka shirika.
- **Ngazi ya 3 (Kusawazisha):** Mazoea yameandikwa na kutekelezwa shirika zima. Uainishaji wa pamoja wa vipengee vya usanidi, vipimo vya msingi visivyobadilika, udhibiti wa mabadiliko wa ngazi, na uhasibu wa hali vimeanzishwa na kwa kiasi kikubwa vya kiotomatiki; matoleo yanazalishwa upya na yanafuatilika, na ukaguzi unasaidiwa na zana badala ya kumbukumbu.
- **Ngazi ya 4 (Kusimamia):** SCM inapimwa na kudhibitiwa kwa data. Kiwango cha kuzalishwa upya, ufikiaji wa ufuatiliaji kutoka hitaji hadi kitu kilichosambazwa, muda wa kuongoza wa mabadiliko kupitia kila ngazi ya udhibiti, matukio ya kuteleza kwa usanidi, na matokeo ya ukaguzi vinafuatiliwa dhidi ya vipimo vya msingi na malengo. Mikengeuko huchochea urekebishaji, na kila uamuzi wa kwenda au kutokwenda unasimama kwenye ushahidi huu badala ya dai.
- **Ngazi ya 5 (Kuratibu):** SCM inaboreshwa kila wakati na kuunganishwa kuvuka shirika. Ikiwa ya kiotomatiki kikamilifu na inayothibitishwa mfululizo kwa ujenzi unaoweza kuzalishwa upya, SBOM, uthibitisho wa asili, na uhasibu wa hali hai, mchakato umefumwa katika utoaji, usalama, na ukaguzi, na hubadilika hatari na matokeo ya utoaji yanapohama, ukistaafisha na kupanga upya wigo wa udhibiti kwa ushahidi.

## Mawazo ya kujadili

- Je, unaweza kuzalisha upya toleo lenu la mwisho hasa kutoka ingizo zinazodhibitiwa leo, na ingechukua muda gani?
- Ni vipengee vipi vya usanidi vinavyoamua tabia lakini haviko chini ya udhibiti kweli, hasa data ya usanidi na miundombinu?
- Je, udhibiti wenu wa mabadiliko umepangwa kwa hatari, au unaongeza mzigo wa sare au ulegevu wa sare kila mahali?
- Rekodi yenu ya usanidi inaishi wapi, na imeteleza kiasi gani kutoka kinachosambazwa kweli?
- Ushahidi gani ungeweza kuzalisha kwenye ukaguzi kesho, na kiasi gani kingekuwa ujenzi upya badala ya rekodi?
- Ujenzi unaoweza kuzalishwa upya, SBOM, na uthibitisho wa asili vinabadilishaje kile ambacho ukaguzi wenu unaweza kuthibitisha kiotomatiki?

## Mambo muhimu ya kukumbuka

- SCM hudhibiti usanidi mzima (msimbo, utegemezi, miundombinu, na data ya usanidi), si chanzo tu.
- Vipimo vya msingi ni nukta za marejeo zisizobadilika; badiliko linaidhinishwa na kurekodiwa dhidi yake, haliwezi kuzuiwa.
- Uhasibu wa hali lazima ukuruhusu kujibu, wakati wowote, toleo lina nini na lilifikaje huko.
- Ukaguzi huthibitisha kinachojengwa na kutolewa kinalingana na usanidi uliorekodiwa na mahitaji yaliyoidhinishwa.
- Panga udhibiti kwa hatari na uotomatishe utambuzi, uhasibu, na ukaguzi ili rekodi iwe zao la pembeni la utoaji.

## Marejeo na usomaji zaidi

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Configuration Management knowledge area
- IEEE Std 828, *Standard for Configuration Management in Systems and Software Engineering*
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (configuration management process)
- Jez Humble and David Farley, *Continuous Delivery*
- Bob Aiello and Leslie Sachs, *Configuration Management Best Practices: Practical Methods that Work in the Real World*
- NIST guidance on software supply chain security, software bills of materials (SBOM), and artifact provenance
- CNCF and open standards for build provenance and attestation (as reference frameworks)
