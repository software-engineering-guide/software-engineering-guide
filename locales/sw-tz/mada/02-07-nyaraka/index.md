# 2.7 Nyaraka

## Muhtasari na msukumo

[Nyaraka](https://en.wikipedia.org/wiki/Software_documentation) ni maarifa yaliyoandikwa yanayowaruhusu watu kutumia, kuendesha, na kubadilisha programu bila kulazimika kukusanya uelewa kutoka kwa msimbo pekee. Zinakuja katika aina nyingi: jinsi ya kuanza, jinsi ya kukamilisha kazi, jinsi mfumo ulivyopangwa, jinsi ya kujibu tukio, [API](https://en.wikipedia.org/wiki/API) inakubali na kurudisha nini. Kila moja inamhudumia msomaji tofauti mwenye hitaji tofauti. Nyaraka nzuri si za hiari. Ndio tofauti kati ya maarifa yanayopanuka kuvuka shirika kubwa na maarifa yanayoishi vichwani mwa watu wachache tu.

Kwa timu kubwa, nyaraka ndizo ulinzi wako bora dhidi ya hatari ya mtu-muhimu (hatari wakati maarifa muhimu yanakaa kwa mtu mmoja au wachache tu) na njia yako ya haraka zaidi ya kutambulisha wageni. Mamia ya wahandisi wanapotegemea mifumo ambayo hawakuijenga, na watu wakijiunga, kuhama, na kuondoka daima, shirika linaweza kufanya kazi tu ikiwa maarifa yameandikwa na ni rahisi kupatikana. Mifumo isiyoandikwa huwa dhaifu: waandishi wake tu wanaweza kuibadilisha kwa usalama, na waandishi hao wanapoondoka, shirika hupoteza uwezo wa kudumisha programu yake mwenyewe. Hiyo ni mojawapo ya kushindwa kwa kawaida na ghali zaidi kwa ukubwa.

Mazingira ya mashirika makubwa na ya serikali huinua dau zaidi. Mifumo huishi muda mrefu, kwa hiyo nyaraka zako lazima ziwahudumie wadumishaji miaka, hata miongo, baada ya timu ya awali kuondoka. Mifumo ya udhibiti na ukaguzi mara nyingi huamuru nyaraka mahususi kama ushahidi wa udhibiti: rekodi za usanifu, [miongozo ya uendeshaji](https://en.wikipedia.org/wiki/Runbook) (taratibu za hatua kwa hatua za kiuendeshaji na za kukabiliana na matukio), na kumbukumbu za maamuzi. Mifumo ya sekta ya umma inayokabidhiwa kati ya wasambazaji hutegemea nyaraka kabisa kubeba maarifa kuvuka mipaka ya mikataba. Hata hivyo nyaraka zinajulikana kuoza kwa urahisi, kwa hiyo changamoto halisi ni kuziweka sahihi programu inapobadilika.

## Kanuni kuu

- Andika kwa msomaji mahususi mwenye hitaji mahususi; aina tofauti za nyaraka hutumikia madhumuni tofauti.
- Weka nyaraka karibu na msimbo na uzichukulie kama msimbo (nyaraka-kama-msimbo).
- Usahihi unashinda ukamilifu; kiasi kidogo cha nyaraka za kuaminika kinashinda kiasi kikubwa kisicho sahihi.
- Zalisha kinachoweza kuzalishwa; usidumishe kwa mkono kile ambacho zana inaweza kuzalisha kutoka chanzo cha ukweli.
- Pigana na kuoza kwa nyaraka kikamilifu; nyaraka zilizochakaa ni mbaya kuliko kutokuwa nazo kwa sababu zinapotosha.
- Fanya nyaraka zipatikane; maarifa yasiyopatikana kwa vitendo hayapo.
- Rekodi maamuzi na sababu zake, si hali ya sasa tu.

## Mapendekezo

### Pokea nyaraka-kama-msimbo

Weka nyaraka katika [udhibiti wa matoleo](https://en.wikipedia.org/wiki/Version_control) kando ya msimbo unaoueleza, ziandike kwa lugha ya alama ya maandishi wazi, na uzipitie kupitia mchakato uleule wa maombi ya kuvuta. Hilo huzifanya zikae katika matoleo, zipitiwe, na ziwe karibu na msimbo, ili uweze kusasisha vyote pamoja. Zichapishe kupitia bomba la kiotomatiki ili toleo la hivi karibuni lipatikane daima. Kuchukulia nyaraka kama msimbo kunaleta nidhamu ileile inayoweka msimbo kuaminika: mapitio, historia, na uendeshaji wa kiotomatiki.

### Panga maudhui kwa mfumo wa Diátaxis

Panga nyaraka katika aina nne tofauti, kwa sababu kuzichanganya hakumhudumii msomaji yeyote vyema: mafunzo (yanayoelekezwa kwa kujifunza, kwa wageni), miongozo ya jinsi ya (inayoelekezwa kwa kazi, kwa lengo mahususi), marejeo (yanayoelekezwa kwa taarifa, sahihi na kamili), na maelezo (yanayoelekezwa kwa uelewa, kwa nini na muktadha). Ziweke tofauti na kila kitu kinakuwa rahisi kuandika, kuabiri, na kudumisha, kwa sababu kila ukurasa una kazi moja wazi na hadhira moja wazi.

### Dumisha nyaraka muhimu za kiuendeshaji

Mpe kila hazina [README](https://en.wikipedia.org/wiki/README) wazi kama mlango wake wa mbele: ni nini, jinsi ya kuijenga na kuiendesha, na pa kwenda baadaye. Andika miongozo ya uendeshaji kwa kazi za kiuendeshaji na kukabiliana na matukio, ili yeyote aliye zamu aweze kutenda, si wataalamu tu. Weka nyaraka za usanifu zinazoeleza muundo wa mfumo na vipengele muhimu. Na toa nyaraka za utambulisho zinazomfanya mhandisi mpya awe na tija haraka. Hizi ndizo nyaraka unazozikosa zaidi zisipokuwepo.

### Zalisha nyaraka za API na kumbukumbu za mabadiliko kutoka chanzo cha ukweli

Zalisha nyaraka zako za marejeo ya API kutoka mkataba unaosomeka na mashine au maelezo ya msimbo, ili zisiweze kutofautiana na kiolesura halisi. Weka [kumbukumbu ya mabadiliko](https://en.wikipedia.org/wiki/Changelog), kwa hakika iliyozalishwa kutoka commit zenye muundo au maelezo ya toleo, ili watumiaji waone kilichobadilika kati ya matoleo. Kuotomatisha haya huondoa nyaraka zinazodumishwa kwa mkono zinazooza kwa urahisi zaidi mabegani mwako na kuziweka za kuaminika.

### Rekodi maamuzi ya usanifu

Nasa maamuzi muhimu ya usanifu na ubunifu kama rekodi nyepesi, zenye tarehe zinazotaja muktadha, uamuzi, na matokeo yake. Rekodi hizi za maamuzi huhifadhi sababu ambayo ingepotea vinginevyo, ili wadumishaji wa baadaye waone kwa nini mfumo uko jinsi ulivyo badala ya kuuhoji au kurudia makosa ya zamani. Hulipa hasa kwa maisha marefu ya mifumo ya mashirika makubwa na ya serikali.

### Pigana na kuoza kwa nyaraka kwa makusudi

Chukulia nyaraka zilizochakaa kama kasoro. Sasisha nyaraka katika badiliko lilelile linalobadilisha tabia, na ufanye hilo kuwa matarajio ya mapitio. Kabidhi umiliki ili kila waraka muhimu uwe na mtu anayewajibika. Pitia nyaraka zenye thamani ya juu kwa usahihi mara kwa mara, ondoa kisichotumika, na ondoa au uweke alama wazi chochote usichokiamini tena. Nyaraka zinazooza kidogo zaidi ni nyaraka hai: zilizozalishwa au kujaribiwa dhidi ya mfumo wenyewe.

### Wekeza katika usimamizi wa maarifa na uwezo wa kupatikana

Fanya nyaraka zipatikane kupitia utafutaji mzuri, uabiri wazi, na nyumba inayojulikana, ili watu wapate wanachohitaji bila kumuuliza mtu. Usiruhusu zigawanyike kuvuka wiki na zana nyingi zisizounganishwa. Na nasa [maarifa fiche](https://en.wikipedia.org/wiki/Tacit_knowledge), uelewa usio rasmi unaoishi kwenye nyuzi za gumzo na vichwani mwa watu, katika umbo la kudumu, linalopatikana kabla hayajatoweka.

## Mabadilishano: faida na hasara

| Mbinu | Faida | Hasara |
|---|---|---|
| Nyaraka-kama-msimbo | Zina matoleo, zinapitiwa, karibu na msimbo; kuoza kwa chini | Zinahitaji nidhamu ya mhandisi; si rafiki sana kwa waandishi wasio wa kiufundi |
| Wiki / msingi wa maarifa | Rahisi kuhariri; zinafikika kwa kila mtu | Zinatofautiana na msimbo; zinagawanyika; zinaoza kimya |
| Nyaraka zilizozalishwa (API, kumbukumbu za mabadiliko) | Daima sahihi; matengenezo ya chini | Zimewekewa kikomo na kile chanzo kinachoeleza; zinahitaji zana |
| Maelezo yaliyoandikwa kwa mkono | Muktadha tajiri na sababu ambazo mashine haziwezi kuzalisha | Zinahitaji kazi nyingi; zinaelekea kuchakaa |
| Muundo wa Diátaxis | Madhumuni wazi kwa kila ukurasa; rahisi kuabiri na kudumisha | Juhudi za awali za kupanga; inahitaji nidhamu ya mwandishi |

Mabadilishano ya msingi ni juhudi dhidi ya usahihi na uimara. Nyaraka za bei nafuu zaidi kuandika, ukurasa wa haraka wa wiki, pia ndizo zinazoelekea zaidi kuoza na kugawanyika. Nyaraka za kudumu zaidi, zilizozalishwa kutoka chanzo au kupitiwa kama msimbo, zinagharimu nidhamu zaidi mapema lakini zinabaki za kuaminika. Kanuni nzuri ya kidole gumba: zalisha unachoweza, weka kilichobaki karibu na msimbo na kupitiwa kama msimbo, na uhifadhi maelezo yenye kazi nyingi yaliyoandikwa kwa mkono kwa sababu ambayo binadamu pekee wanaweza kutoa.

## Maswali ya kujadili na timu yako

1. **Je, nyaraka zenu zimetenganishwa kwa hitaji la msomaji, au mafunzo, marejeo, na maelezo yanachanganyika kwenye ukurasa mmoja?** Sura hii inapendekeza mgawanyo wa Diátaxis katika mafunzo, miongozo ya jinsi ya, marejeo, na maelezo, na inaorodhesha kuchanganya aina kama mfumo mbaya usiomhudumia msomaji yeyote vyema. Kwa ukubwa, mgeni anayejifunza mfumo na mhandisi aliye zamu anayewinda ukweli sahihi wanahitaji kurasa tofauti, na ukurasa mmoja uliochanganyika hupunguza kasi ya wote wawili. Leta ishara: chagua nyaraka zenu zinazotembelewa zaidi na uangalie kama kila moja ina kazi moja wazi na hadhira moja wazi. Rekebisha wakosaji wabaya zaidi kuwa aina tofauti, ili kila ukurasa uwe rahisi kuandika, kuabiri, na kuweka wa sasa. Muundo huo ndio unaofanya nyaraka zidumishike shirika linapokua.

2. **Je, mnanasa maamuzi muhimu ya usanifu pamoja na sababu zake, au hali ya sasa tu?** Sura inapendekeza rekodi nyepesi, zenye tarehe za maamuzi zinazotaja muktadha, uamuzi, na matokeo, na inabainisha kwamba zinalipa zaidi kwa maisha marefu ya mifumo ya mashirika makubwa na ya serikali. Bila hizo, mdumishaji miaka baadaye hawezi kuona kwa nini mfumo uko jinsi ulivyo, kwa hiyo anahoji chaguo sahihi au kurudia makosa ya zamani. Leta uamuzi mgumu wa hivi karibuni ambao hoja yake sasa inaishi kwenye uzi wa gumzo au kumbukumbu ya mtu kama ishara madhubuti. Pokea muundo mfupi wa rekodi ya uamuzi na ufanye kuandika moja kuwa sehemu ya badiliko lolote muhimu la usanifu. Sababu ndiyo hasa maarifa ambayo binadamu pekee wanaweza kutoa na ambayo huoza haraka zaidi yasipoandikwa.

3. **Je, mhandisi yeyote aliye zamu anaweza kujibu tukio kutoka miongozo yenu ya uendeshaji peke yake, bila kumwita mtu aliyejenga mfumo?** Sura hii inataja miongozo ya uendeshaji kama waraka muhimu wa kiuendeshaji ili yeyote aliye zamu aweze kutenda, si wataalamu tu, na inaeleza timu ya serikali iliyoweza kurithi mfumo kwa sababu miongozo ya uendeshaji ilibeba maarifa kuvuka mpaka wa mkataba. Hatari ya mtu-muhimu ndiyo kushindwa ambako hili linalinda dhidi yake: mtaalamu pekee asipopatikana au kuondoka, utaratibu wa kurejesha usioandikwa hugeuza tukio la kawaida kuwa kukatika. Leta ushahidi: chukua tukio la hivi karibuni na uangalie kama mwongozo wa uendeshaji peke yake ungelitatua. Andika na ujaribu miongozo kwa taratibu ambazo watu wanaziogopa, na uchukulie mwongozo usioweza kusimama peke yake kama kasoro. Hiyo ndiyo tofauti kati ya kupona saa nane usiku na kupandisha ngazi saa nane usiku.

4. **Ni marejeo na kumbukumbu zipi za API zenu zinazozalishwa kutoka chanzo cha ukweli, na zipi bado zinadumishwa kwa mkono na kuteleza kimyakimya?** Sura hii inakuambia uzalishe nyaraka za marejeo kutoka mkataba unaosomeka na mashine au maelezo ya msimbo ili zisitofautiane na kiolesura halisi, na inaorodhesha kudumisha kwa mkono maudhui yanayoweza kuzalishwa kama mfumo mbaya. Kwa timu kubwa, waraka wa API ulioandikwa kwa mkono unaochelewa nyuma ya kiolesura halisi ni mbaya kuliko kutokuwa nao: kila mtumiaji anayeuamini anaandika uunganishaji uliovunjika, na kushindwa kunaibuka mbali na ukurasa uliochakaa uliosababisha. Leta ishara madhubuti: chukua sampuli ya violesura vyenu vinavyotumika zaidi na ulinganishe rejeo lililochapishwa na mkataba halisi kuona kila moja limeteleza umbali gani. Pale unapopata kuteleza, unganisha rejeo na ujenzi ili lizalishwe upya kwa kila badiliko, na ustaafishe nakala iliyodumishwa kwa mkono. Katika mazingira ya mashirika makubwa na ya serikali, ambapo violesura vinatumiwa kuvuka timu, wasambazaji, na mipaka ya mikataba usiyoiona, rejeo lenye mamlaka lililozalishwa mara nyingi ndilo kitu pekee kinachowazuia waunganishaji wasijenge dhidi ya uongo.

5. **Nani anamiliki kila waraka wenye thamani ya juu, na ungejuaje leo kama mmoja umechakaa?** Sura inachukulia nyaraka zilizochakaa kama kasoro na inaonya kwamba nyaraka zisizo na mmiliki huoza kwa sababu kuzisasisha ni kazi ya hakuna, huku nyaraka zilizochakaa zinazowasilishwa kama za sasa zikiharibu uaminifu kwa nyaraka zako zote. Kwa ukubwa hatari si ukurasa mmoja mbaya bali kumomonyoka polepole kwa imani: wasomaji wanapoungua na maagizo yaliyopitwa na wakati, wanaacha kuamini mkusanyiko mzima na kurudi kukatiza watu. Leta ramani ya umiliki ya nyaraka zenu muhimu zaidi na jibu la uaminifu kwa jinsi kuoza kunavyogunduliwa, iwe kwa ratiba ya mapitio, uzalishaji, majaribio dhidi ya mfumo, au bahati tupu. Kabidhi mmiliki aliyetajwa kwa kila waraka unaojalisha, na upendelee nyaraka hai zilizozalishwa au kujaribiwa ili kuchakaa kuonekane kimitambo badala ya kupitia msomaji aliyeaibika. Kwa mifumo ya mashirika makubwa na ya serikali inayodumu kuliko timu zake za awali, nyaraka zisizo na mmiliki ni dhima ambayo mkaguzi au msambazaji mrithi hatimaye atakutoza.

6. **Nyaraka zenu zinapatikana kwa kiasi gani, na maarifa muhimu kiasi gani bado yanaishi kwenye nyuzi za gumzo na vichwani mwa watu tu?** Sura hii inasema maarifa yasiyopatikana kwa vitendo hayapo, inaonya dhidi ya kugawanya nyaraka kuvuka wiki na zana nyingi zisizounganishwa, na inakuhimiza unase maarifa fiche katika umbo la kudumu, linalopatikana kabla hayajatoweka. Katika shirika kubwa ukweli ule ule mara nyingi hugunduliwa upya, kuulizwa upya, na kujibiwa upya mara mia kwa sababu hakuna anayeweza kupata mahali ulipokwisha kuandikwa, na kila kuondoka huchukua muktadha usiobadilishika nje ya mlango. Leta ushahidi: hesabu nyumba ngapi tofauti za nyaraka mnazodumisha, jaribu kupata ukweli muhimu matatu kwa utafutaji peke yake, na uone majibu halisi yalikuwa wapi, kwenye kumbukumbu ya mtu au ujumbe uliozikwa. Unganisha kuelekea nyumba inayojulikana yenye utafutaji halisi na uabiri wazi, na ufanye kunasa maarifa fiche kuwe sehemu ya kawaida ya kazi badala ya uokoaji wa kishujaa. Katika mazingira ya sekta ya umma na yaliyo na mikataba mingi, ambapo mifumo hupita kati ya wasambazaji na timu kwa mkataba, maarifa yaliyoandikwa yanayopatikana ndiyo kitu pekee kinachookoka makabidhiano.

## Mtazamo wa sekta

**Kampuni changa.** Ukiwa na wahandisi wachache na bila muda wa ziada, andika tu kile ambacho kukatika kwa saa nane usiku au mwajiriwa mpya angehitaji kweli: README halisi kwa kila huduma, mwongozo mmoja uliojaribiwa wa utaratibu wa kutoa-na-kurejesha ambao kila mtu anauogopa, na maelezo machache yenye tarehe kuhusu maamuzi ambayo vinginevyo ungeyasahau. Zalisha nyaraka za API kutoka mkataba ili usizidumishe kwa mkono kamwe. Pinga kujenga jukwaa la nyaraka; folda yenye matoleo ya alama kando ya msimbo inatosha hadi uhisi maumivu halisi.

**Biashara ndogo.** Bila mwandishi wa kiufundi na bajeti finyu, tegemea nyaraka ambazo zana zako zinazalisha tayari na nyaraka-kama-msimbo nyepesi badala ya programu yenye wafanyakazi. Weka uchaguzi kama kununua dhidi ya kujenga: pendelea majukwaa yanayozalisha rejeo lao la sasa na msingi wa maarifa unaotafutika kuliko wiki unayopaswa kuitunza kwa mkono. Tumia juhudi zako adimu kwa nyaraka mbili au tatu ambazo kutokuwepo kwake kungesimamisha biashara, na uache ukurasa usio sahihi au uliokosekana uwe kichocheo cha kurekebisha umiliki.

**Biashara kubwa.** Kuvuka timu nyingi tatizo ni uthabiti na uwezo wa kupatikana: bomba la pamoja la nyaraka-kama-msimbo, muundo wa pamoja kama Diátaxis, marejeo ya API na kumbukumbu za mabadiliko zilizozalishwa, na rekodi za maamuzi zinazotumika kwa namna ileile kila mahali ili maarifa yasigawanyike kuvuka makumi ya wiki. Kabidhi umiliki kwa kila waraka wenye thamani ya juu na upime usahihi, si uwepo tu. Chukulia rekodi za usanifu, miongozo ya uendeshaji, na kumbukumbu za maamuzi kama ushahidi wa ukaguzi, na usawazishe jinsi zinavyozalishwa ili mapitio ya udhibiti yakute njia iliyoandikwa, inayoweza kutetewa badala ya mhangaiko.

**Serikali.** Kanuni za ununuzi na uwajibikaji wa umma hufanya nyaraka kuwa kitu cha kutoa, si fadhila. Andika nyaraka za usanifu, miongozo ya uendeshaji, na rekodi za maamuzi ndani ya mikataba kama vitu vilivyoamriwa, vilivyopitiwa kwa usahihi ili maarifa yaokoke mpito wa msambazaji na mfumo uweze kuendeshwa na yeyote anayeurithi. Hitaji kwamba mwendeshaji yeyote aliyeidhinishwa aweze kujibu tukio kutoka kwa mwongozo wa uendeshaji peke yake, na uweke kumbukumbu za maamuzi kama rekodi ya umma ya uwazi ya kwa nini chaguo zilifanywa. Nyaraka nyembamba hapa si usumbufu wa faragha; zinakuwa gharama ya kuchambua mfumo upya inayofadhiliwa na mlipakodi.

## Mifano

**Kampuni changa.** Kampuni changa ya watu watano inaandika README halisi kwa kila huduma na mwongozo mfupi wa uendeshaji kwa utaratibu mmoja wa kutoa-na-kurejesha ambao kila mtu anauogopa, kwa hiyo kukatika kwa saa nane usiku hakutegemei kumwamsha mwanzilishi mmoja anayejua mfumo. Wanazalisha nyaraka za API kutoka mkataba badala ya kuziandika kwa mkono, na kuandika maelezo machache yenye tarehe yanayoeleza kwa nini walichagua hifadhidata yao na mbinu yao ya uthibitishaji. Inabaki nyepesi, lakini inamaanisha waajiriwa wa sita na wa saba wanatambulishwa kutoka nyaraka badala ya kumkatiza kila mtu.

**Biashara kubwa.** Kampuni kubwa ya programu inaweka nyaraka zake zote katika hazina zilezile kama msimbo wake, zimeandikwa kwa alama na kupitiwa katika maombi ya kuvuta kando ya mabadiliko zinayoyaeleza. Marejeo ya API yanazalishwa kutoka mikataba ya huduma, kwa hiyo hayateleza kamwe. Kumbukumbu za mabadiliko zinazalishwa kutoka commit zenye muundo, na rekodi za maamuzi ya usanifu zinahifadhi hoja nyuma ya chaguo kuu. Tovuti iliyochapishwa ya nyaraka inajengwa kiotomatiki kwa kila uunganishaji. Wahandisi wapya wanapata tija haraka kwa sababu miongozo ya utambulisho na ya uendeshaji ni ya sasa na inapatikana, na wahandisi walio zamu wanategemea miongozo ya uendeshaji badala ya kuwaita waandishi wa awali.

**Serikali.** Wakala wa kitaifa unarithi mfumo kutoka kwa mkandarasi anayeondoka, ukitegemea nyaraka kabisa kubeba maarifa kuvuka mpaka wa mkataba. Kwa sababu muuzaji wa awali alidumisha nyaraka za usanifu, miongozo ya uendeshaji, na rekodi za maamuzi kama vitu vilivyoamriwa, timu mpya inaweza kuendesha na kubadilisha mfumo bila waandishi wa awali. Pale nyaraka zilikuwa nyembamba, wakala unakabiliwa na gharama kubwa ya kuchambua mfumo upya. Uzoefu huo unaendesha sera mpya: nyaraka ni kitu cha kimkataba cha kutoa, kinachopitiwa kwa usahihi badala ya kuchukuliwa kama wazo la baadaye, na miongozo ya uendeshaji lazima imruhusu mwendeshaji yeyote aliyeidhinishwa kujibu matukio.

## Kesi ya biashara: sababu, ROI, na TCO

Nyaraka hulipa kwa muda mfupi wa utambulisho, hatari ndogo ya mtu-muhimu, kukabiliana na matukio kwa kasi, na gharama ndogo ya mabadiliko kwa maisha ya mfumo. Wahandisi wapya wanaofikia tija ndani ya siku badala ya wiki, wafanyakazi walio zamu wanaotatua matukio kutoka mwongozo wa uendeshaji badala ya kupandisha, wadumishaji wanaobadilisha mfumo kwa kujiamini miaka baada ya kujengwa: hizi ni akiba kubwa, zinazojirudia zinazojumlika kuvuka shirika kubwa na maisha marefu ya mfumo.

Nyaraka zinagharimu nini? Juhudi za kuandika na kudumisha. *Kutoandika* kunagharimu nini? Unalipa daima: katika utambulisho wa polepole, maswali yanayorudiwa, vikwazo vya mtu-muhimu, urejeshaji polepole wa matukio, na, kwa kiwango kikubwa, mifumo ambayo hakuna anayeweza kuibadilisha kwa usalama, ikilazimisha kuandika upya kwa gharama au kuchambua mfumo upya. Katika hali za mpito wa msambazaji na ukaguzi, nyaraka zinazokosekana zinaweza kubeba gharama za moja kwa moja za kimkataba na za uzingatiaji. Kujenga hoja kwa uongozi, weka nambari kwenye muda wa utambulisho, muda wa kukabiliana na matukio, na kiasi cha maarifa muhimu kinachokaa vichwani mwa watu binafsi. Kisha weka nyaraka-kama-msimbo na uzalishaji kama njia za kupata nyaraka za kudumu bila mzigo sawia wa matengenezo. Na sisitiza kwamba nyaraka zisizo sahihi ni dhima, kwa hiyo uwekezaji lazima ujumuishe kuziweka za sasa.

## Mifumo mibaya na mitego

- **Nyaraka zilizochakaa zinazowasilishwa kama za sasa:** hupotosha wasomaji na kuharibu uaminifu kwa nyaraka zote.
- **Wiki ya kuandikwa-mara-moja:** kurasa zinazoundwa na kamwe kusasishwa, zikiteleza kimyakimya kutoka uhalisia.
- **Mgawanyiko wa nyaraka:** maarifa yaliyotawanyika kuvuka zana na wiki nyingi hivi hakuna kinachoweza kupatikana.
- **Kuchanganya aina za nyaraka:** mafunzo, marejeo, na maelezo yaliyochanganyika kwenye ukurasa mmoja, bila kumhudumia msomaji yeyote vyema.
- **Kudumisha kwa mkono maudhui yanayoweza kuzalishwa:** nyaraka za API zilizoandikwa kwa mkono zinazotofautiana bila kuepukika na kiolesura halisi.
- **Maarifa ya kikabila:** uelewa muhimu unaokaa vichwani mwa watu na historia ya gumzo tu, unaopotea wanapoondoka.
- **Nyaraka kama wazo la baadaye:** zilizoandikwa mwishoni, kama zipo, badala ya kando ya badiliko.
- **Hakuna umiliki:** nyaraka zisizo na mmiliki anayewajibika huoza kwa sababu kuzisasisha ni kazi ya hakuna.

## Kielelezo cha ukomavu

- **Ngazi ya 1, Kuanzisha.** Nyaraka ni chache, zimetawanyika, na zimechakaa, na maarifa yanaishi vichwani mwa watu. Kilichopo kiliandikwa mara moja na kamwe hakikuguswa tena, kwa hiyo kukatika au kuondoka kunamaanisha kuchambua mfumo upya.
- **Ngazi ya 2, Kuendeleza.** Nyaraka muhimu zipo, kama README na miongozo michache ya uendeshaji, lakini zinadumishwa bila uthabiti na ni ngumu kupata. Baadhi ya timu huandika vizuri na nyingine kidogo sana, na hakuna matarajio ya pamoja kuhusu hazina inapaswa kubeba nini au iishi wapi.
- **Ngazi ya 3, Kusawazisha.** Nyaraka-kama-msimbo ni kawaida kuvuka shirika: muundo wa pamoja kama Diátaxis, marejeo ya API na kumbukumbu za mabadiliko zilizozalishwa, rekodi za maamuzi, na matarajio katika mapitio kwamba nyaraka zibadilike na msimbo unaoeleza. Kila waraka wenye thamani ya juu una mmiliki aliyetajwa, na kuna nyumba moja inayojulikana yenye utafutaji halisi.
- **Ngazi ya 4, Kusimamia.** Nyaraka zinapimwa, si kuwepo tu. Unafuatilia ufikiaji wa nyaraka muhimu, kiwango cha badiliko la nyaraka dhidi ya cha msimbo, muda wa utambulisho, utatuzi wa matukio kutoka miongozo ya uendeshaji peke yake, na ujana dhidi ya kizingiti kilichofafanuliwa cha kuchakaa, na unapitia vipimo hivyo dhidi ya vipimo vya msingi. Kuoza kunanaswa kimitambo kupitia uzalishaji, majaribio dhidi ya mfumo, na ukaguzi wa viungo na usahihi, na kurasa zilizochakaa zinawekewa bendera au kupunguzwa kwa ushahidi badala ya bahati.
- **Ngazi ya 5, Kuratibu.** Nyaraka zinaboreshwa kila wakati na kuunganishwa kuvuka shirika: hai, kwa kiasi kikubwa zilizozalishwa au kujaribiwa dhidi ya mfumo, zenye wamiliki, zinazopatikana, na zinazobadilika. Vipimo vinalisha mahali unapowekeza, maarifa fiche yananaswa kama sehemu ya kawaida ya kazi, na mkusanyiko unasawazishwa upya na kupunguzwa kikamilifu mifumo, timu, na wasomaji wanapobadilika.

## Mawazo ya kujadili

- Nyaraka zipi, zikitoweka kesho, zingeumiza shirika lenu zaidi, na je, zipo kwa sasa na zinabaki za sasa?
- Mnafanyaje kusasisha nyaraka kuwe sehemu ya asili ya kubadilisha msimbo badala ya kazi tofauti?
- Mnaweza kubadilisha nyaraka zilizoandikwa kwa mkono na zilizozalishwa zilizofungwa na chanzo cha ukweli wapi?
- Mnapimaje kama nyaraka zenu ni sahihi na zinatumika, si zipo tu?
- Wasaidizi wa AI wanapaswa kubadilishaje jinsi mnavyoandika, kudumisha, na kutafuta nyaraka, na wanaweza kuleta wapi maudhui yanayoonekana sahihi lakini si sahihi?
- Mnanasaje maarifa fiche kabla watu wanaoyashikilia hawajaondoka?

## Mambo muhimu ya kukumbuka

- Chukulia nyaraka kama msimbo: zenye matoleo, zinazopitiwa, karibu na chanzo, na zinazochapishwa kiotomatiki.
- Panga maudhui kwa hitaji la msomaji kwa mafunzo, miongozo ya jinsi ya, marejeo, na maelezo.
- Dumisha nyaraka muhimu zenye thamani ya juu: README, miongozo ya uendeshaji, nyaraka za usanifu, utambulisho, na rekodi za maamuzi.
- Zalisha nyaraka za API na kumbukumbu za mabadiliko ili zisiweze kuteleza kutoka chanzo cha ukweli.
- Pigana na kuoza kwa umiliki, matarajio ya mapitio, na kupunguza; nyaraka zisizo sahihi ni mbaya kuliko kutokuwa nazo.

## Marejeo na usomaji zaidi

- Daniele Procida, *Diátaxis* documentation framework
- Andrew Etter, *Modern Technical Writing*
- Anne Gentle, *Docs Like Code*
- Google, *Developer Documentation Style Guide* and Season of Docs guidance (as reference exemplars)
- Michael Nygard, *Documenting Architecture Decisions* (architecture decision records)
- Andrew Hunt and David Thomas, *The Pragmatic Programmer* (on knowledge and documentation)
- *Keep a Changelog* (as a reference convention)
