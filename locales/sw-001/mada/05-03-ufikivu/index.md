# 5.3 Ufikivu

## Muhtasari na msukumo

[Ufikivu](https://en.wikipedia.org/wiki/Accessibility) (mara nyingi hufupishwa "a11y") ni mazoea ya kujenga programu ambazo watu wenye ulemavu wanaweza kuziona, kuzielewa, kuzipitia, na kuzitumia. Hilo linajumuisha watu ambao ni vipofu au wenye uoni hafifu, ambao ni viziwi au wasiosikia vizuri, wenye ulemavu wa mwendo, wenye tofauti za kiakili au za kujifunza, na wanaokabiliwa na mipaka ya muda au ya hali kama mkono uliovunjika, mwanga mkali wa jua, au chumba chenye kelele. Takriban mtu mmoja kati ya watano ana ulemavu, na kila mtu hunufaika na usanifu unaofikika wakati fulani. Hili si malazi ya kikundi kidogo. Ni kiwango cha msingi cha ubora.

Kwa timu kubwa, ufikivu lazima ujengwe ndani ya mfumo, usiachwe kwa nia njema ya mtu mmoja mmoja. Timu nyingi zinaposafirisha ndani ya bidhaa moja, kijenzi kimoja kisichofikika (nyanja ya fomu isiyo na lebo, kiashiria cha hali cha rangi tu, mtego wa kibodi kwenye dirisha ibukizi) kinaweza kuwafungia nje watumiaji walemavu kutoka safari nzima. Kujenga ufikivu ndani ya vijenzi vya pamoja, tokeni za usanifu, mabomba ya majaribio, na ufafanuzi wa kukamilika ndiyo njia pekee ya kuufanya wa kutegemewa kwa ukubwa. Kuurudisha baadaye ni ghali na unaokabiliwa na makosa. Kuubuni ndani ni nafuu na wa kudumu.

Kwa serikali, ufikivu ni sharti la kisheria na wajibu wa kiraia, si pambo. Huduma za umma lazima zimhudumie kila mwanachama wa umma, na raia walemavu mara nyingi hawana mtoa huduma mbadala: tovuti ya serikali ikiwa haifikiki, hawawezi kupata manufaa yao, leseni, au kupiga kura kwa njia nyingine. Sheria na viwango duniani kote hufanya ufikivu kuwa wa lazima kwa vyombo vya umma, na hatua kwa hatua kwa sekta binafsi pia. Sura hii inachukulia ufikivu kama mambo matatu kwa wakati mmoja: wajibu wa kisheria, wajibu wa kimaadili, na usanifu mzuri tu.

*Angalia pia:* sura ya 5.2 (usanifu wa UI na mifumo ya usanifu), sura ya 5.6 (uhandisi wa frontend), na sura ya 5.1 (misingi ya UX).

## Kanuni kuu

- Ufikivu ni sifa ya msingi ya ubora, kama usalama na utendaji, si kipengele cha hiari.
- Kanuni za POUR: violesura lazima viwe Vinavyoonekana (Perceivable), Vinavyoendeshwa (Operable), Vinavyoeleweka (Understandable), na Imara (Robust).
- [HTML ya kisemantiki](https://en.wikipedia.org/wiki/Semantic_HTML) kwanza; tumia [ARIA](https://en.wikipedia.org/wiki/WAI-ARIA) kujaza mapengo halisi tu, kamwe si mbadala wa vipengele asili.
- Kila kitu kinachoweza kutumika kwa kipanya lazima kiweze kutumika kwa kibodi peke yake.
- Usipitishe taarifa kwa rangi, umbo, au nafasi peke yake.
- Zana za kiotomatiki hunasa sehemu ndogo tu ya masuala; majaribio ya mkono na ya [teknolojia saidizi](https://en.wikipedia.org/wiki/Assistive_technology) ni muhimu.
- Usanifu unaofikika ni usanifu bora kwa kila mtu (["athari ya kingo ya barabara,"](https://en.wikipedia.org/wiki/Curb_cut) ambapo vipengele vilivyojengwa kwa walemavu vinawanufaisha watumiaji wote).
- Sanifu na ujaribu na watu walemavu, si kwa ajili yao tu.

## Mapendekezo

### Sanifu na ujenge kwa WCAG, ukilenga kiwango cha sasa

[Miongozo ya Ufikiaji wa Maudhui ya Wavuti](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) ndiyo rejeo la kimataifa. WCAG 2.1 na 2.2 zimepangwa chini ya kanuni nne za POUR, zenye vigezo vya mafanikio vinavyojaribika katika viwango vya uzingatiaji A, AA, na AAA. Lenga Kiwango cha AA kama msingi wako; ndicho sheria nyingi zinarejelea. WCAG 2.2 inaongeza vigezo vya mwonekano wa umakini, ukubwa wa shabaha, na kupunguza mzigo wa kiakili. WCAG 3.0 ni mrithi anayeibuka, aliyepangwa tofauti na bado anaendelezwa. Mtazame, lakini jenga kwa 2.2 AA leo. Chukulia miongozo kama sakafu, si dari: kupita kila kigezo hakuhakikishi uzoefu unaotumika kweli.

### Tumia HTML ya kisemantiki na ARIA sahihi

Vipengele asili vya HTML (vitufe, viungo, vidhibiti vya fomu, vichwa, orodha, alama za mandhari) vinakuja na kisemantiki cha ufikivu kilichojengwa ndani, tabia ya kibodi, na usaidizi wa teknolojia saidizi. Vitumie kwanza. Tumia majukumu, hali, na sifa za ARIA (Accessible Rich Internet Applications) kuelezea tu wijeti maalumu ambazo HTML haiwezi kuzieleza, na ufuate Mazoea ya Uandishi ya ARIA. Kanuni ya kwanza ya ARIA ni rahisi: usitumie ARIA ikiwa kipengele asili kitatosha. ARIA isiyo sahihi ni mbaya kuliko hakuna: inapotosha kikamilifu [visomaji skrini](https://en.wikipedia.org/wiki/Screen_reader). Ipe ukurasa muundo wa kimantiki wa vichwa, lebo zenye maana, maandishi mbadala kwa picha, manukuu na nakala kwa vyombo vya habari, na kiungo cha kiprogramu kati ya kila lebo na kidhibiti chake.

### Hakikisha uendeshaji wa kibodi na teknolojia saidizi

Kila kipengele shirikishi lazima kifikiwe na kuendeshwa kwa kibodi peke yake, kwa mpangilio wa kimantiki, na kiashiria cha umakini kinachoonekana wazi. Epuka mitego ya kibodi. Simamia umakini kwa makusudi maudhui yanapobadilika: hamisha umakini kwenye kidirisha kinapofunguka, urudishe kinapofungwa, na utangaze masasisho ya kidinamiki kupitia maeneo hai. Jaribu na teknolojia saidizi halisi, ikijumuisha visomaji skrini kwenye kompyuta na simu, ukuzaji wa skrini, udhibiti wa sauti, na ufikiaji wa swichi. Na uheshimu mapendeleo ya mtumiaji kama mwendo uliopunguzwa na utofautishaji ulioongezeka.

### Jaribu kwa zana za kiotomatiki, mapitio ya mkono, na watumiaji halisi

Vichanganuzi vya kiotomatiki vya ufikivu ni vya thamani, na vinapaswa kuendeshwa kwenye bomba kwa kila badiliko. Lakini tafiti mara kwa mara zinaonyesha vinanasa sehemu ndogo tu ya masuala halisi, takriban theluthi moja. Mengine yanahitaji busara ya binadamu: kupitia kwa kibodi, majaribio ya visomaji skrini, ukaguzi wa utofautishaji, na kuuliza kama maudhui yanaeleweka kweli. Muhimu zaidi ya yote, jumuisha watu wenye ulemavu katika majaribio ya utumiaji. Jenga vigezo vya kukubali vya ufikivu ndani ya ufafanuzi wa kukamilika, ili masuala yanaswe kwa kila hadithi badala ya ukaguzi wa kabla ya uzinduzi.

### Fanya ufikivu uwe wa kishirika, si wa kishujaa

Weka ufikivu ndani ya mfumo wa usanifu ili vijenzi visafirishwe vikiwa vinafikika kwa chaguo-msingi. Toa mafunzo ili wasanifu, wahandisi, waandishi wa maudhui, na wasimamizi wa bidhaa kila mmoja ajue anachowajibika. Anzisha kiwango cha ufikivu, mmiliki au kituo cha ubora, na mchakato wa kurekebisha. Chapisha taarifa ya ufikivu na uwape watumiaji njia ya kuripoti vikwazo. Na nunua kwa ufikivu: hitaji wauzaji na vijenzi vya watu wa tatu kuzingatia, na kutoa ushahidi (kama ripoti ya uzingatiaji wa ufikivu).

## Mabadilishano: faida na hasara

| Mbinu | Faida | Hasara |
|---|---|---|
| Jenga ufikivu tangu mwanzo | Nafuu zaidi, wa kudumu, bora kwa kila mtu | Inahitaji mafunzo ya awali na nidhamu |
| Rudisha / rekebisha baadaye | Huahirisha juhudi, hufungua uzinduzi wa haraka | Ghali zaidi sana, dhaifu, mfiduo wa kisheria kwa muda huo |
| Majaribio ya kiotomatiki tu | Ya haraka, nafuu, hunasa regression kwenye CI | Hukosa ~theluthi mbili ya masuala; imani ya uongo |
| Majaribio ya mkono + teknolojia saidizi | Hunasa vikwazo halisi vya utumiaji | Polepole, yanahitaji wajaribu wenye ujuzi na vifaa |
| Majaribio na watumiaji walemavu | Ukweli wa msingi juu ya uzoefu halisi | Juhudi na gharama ya uajiri, lazima ifanywe kwa heshima |

Mabadilishano ya msingi ni nidhamu ya awali dhidi ya gharama iliyoahirishwa. Ufikivu uliojengwa ndani ni wa bei nafuu na unaboresha ubora kwa kila mtu; ufikivu unaorudishwa chini ya shinikizo la kisheria ni ghali, pungufu, na wa mkazo. Kwa muda mrefu hakuna mabadilishano halisi dhidi ya "kasi": programu isiyofikika haifanyi kazi tu kwa moja ya tano ya watumiaji wako. Hiyo ni kasoro, si akiba.

## Maswali ya kujadili na timu yako

1. **Regression za ufikivu zinashindwa ujenzi wetu kama jaribio lililovunjika, na kama sivyo, kwa nini?** Vichanganuzi vya kiotomatiki hunasa takriban theluthi moja ya masuala, lakini yale vinayonasa (lebo zilizokosekana, kushindwa kwa utofautishaji, vidhibiti visivyo na lebo) ni nafuu kunasa kwenye CI na ghali kupata kwenye ukaguzi wa kabla ya uzinduzi. Kuchukulia regression kama kushindwa kwa ujenzi ndiko kunakohamisha ufikivu kutoka juhudi ya kishujaa ya mtu mmoja mmoja hadi sifa ya mfumo ya kutegemewa, ambayo ndiyo kitu pekee kinachofanya kazi timu nyingi zinaposafirisha ndani ya bidhaa moja. Amua ukaguzi upi unazuia, upi ni wa ushauri, na nani anaweza kubatilisha kushindwa. Leta matokeo yenu ya sasa ya kichanganuzi na ufafanuzi wenu wa kukamilika kwenye mkutano. Vigezo vya ufikivu visipoandikwa kwenye ufafanuzi wa kukamilika kwa kila hadithi, vitatolewa kafara tarehe ya mwisho itakapobana.

2. **Kanuni yetu ni ipi kwa wijeti maalumu, na nani anapitia ARIA kabla haijasafirishwa?** Vipengele asili vya HTML vinakuja na tabia ya kibodi na usaidizi wa teknolojia saidizi bure, na ARIA isiyo sahihi ni mbaya kuliko hakuna kwa sababu inapotosha visomaji skrini kikamilifu. Kubaliana kwamba HTML ya kisemantiki ndiyo chaguo-msingi na kwamba wijeti yoyote maalumu (menyu ya kushuka ya mtu mwenyewe, kichagua tarehe, au dirisha ibukizi) inahitaji kupitia kwa kibodi na kisomaji skrini kabla ya kuunganishwa, kufuata Mazoea ya Uandishi ya ARIA. Hili ni muhimu zaidi kwa vijenzi shirikishi ambavyo timu nyingi huvitumia tena, kwa sababu dirisha moja lililovunjika lenye mtego wa kibodi linaweza kuwafungia nje watumiaji walemavu kutoka safari nzima. Leta orodha ya wijeti zenu maalumu na uliza zipi zimejaribiwa na kisomaji skrini halisi. Zozote ambazo hazijajaribiwa ni dhima zilizojificha kwenye msimbo wa pamoja.

3. **Sera yetu ni ipi kuhusu vifuniko vya ufikivu, na je, mtu yeyote anaamini ni suluhisho halisi?** Vifuniko vinauzwa kama hati ya mstari mmoja inayofanya tovuti izingatie, na vinashawishi shinikizo la kisheria linapofika na tarehe ya mwisho inapokaribia. Havitoi uzingatiaji halisi, vinaweza kuzidisha uzoefu kwa watumiaji wa teknolojia saidizi, na kwa serikali vinaacha wajibu wa kisheria wa msingi bila kutimizwa. Amua wazi kwamba mtawekeza kwenye alama za kisemantiki, usaidizi wa kibodi, na majaribio na watu walemavu badala ya kununua wijeti inayofunika tatizo. Leta gharama ya usajili wa kifuniko na ulinganishe na kujenga ufikivu ndani ya vijenzi na bomba lenu mara moja. Kuweka hili mapema kunazuia uamuzi wa ununuzi wa hofu baadaye unaotumia fedha na kutorekebisha chochote.

4. **Watu walemavu ni sehemu ya usanifu na majaribio yetu, au bado tunasanifu kwa mtumiaji wa kufikirika tuliyemvumbua?** Vichanganuzi vya kiotomatiki na hata ukaguzi wa wataalamu hukuambia kama alama zinazingatia; havikuambii kama mtumiaji kipofu anaweza kumaliza malipo yako au mtu mwenye ulemavu wa kiakili anaweza kuelewa ujumbe wako wa makosa. Kuwashirikisha washiriki walemavu ndicho chanzo pekee cha ukweli wa msingi, na kunabadilisha mnachojenga, lakini kunaibua maswali halisi kuhusu jinsi mnavyoajiri kwa haki, jinsi mnavyowalipa watu kwa muda wao, na jinsi mnavyoepuka kumchukulia mshiriki mmoja kama msemaji wa kila ulemavu. Leta orodha yenu ya sasa ya utafiti, mazoea yenu ya uajiri na malipo, na hesabu ya uaminifu ya tafiti ngapi za mwaka uliopita zilijumuisha washiriki walemavu. Kwa shirika kubwa, jopo linalojirudia lenye fidia ya haki na ufikiaji kuvuka mahitaji ya kuona, kusikia, mwendo, na kiakili ndilo linalogeuza hili kutoka ishara ya mara moja kuwa pembejeo ya kutegemewa; katika serikali, kuwashirikisha umma mnaowahudumia mara nyingi ni sehemu ya wajibu wa kisheria na kiraia, si adabu ya hiari.

5. **Tunaponunua au kupachika kijenzi cha mtu wa tatu, tunahitaji ushahidi wa ufikivu, na nani anaukagua?** Mengi ya yale yanayosafirishwa katika bidhaa kubwa hayajaandikwa ndani: kichagua tarehe kutoka maktaba, wijeti ya malipo kwenye iframe, kifurushi cha chati, moduli nzima ya SaaS. Kijenzi kimoja kisichofikika kilichopachikwa kinaweza kushindwa safari nzima bila kujali msimbo wenu wenyewe ni safi kiasi gani, na kikishaunganishwa, kukibadilisha ni ghali. Amua kwamba ufikivu ni sharti la ununuzi, kwamba wauzaji lazima watoe ripoti ya uzingatiaji wa ufikivu (waraka kama VPAT unaosema bidhaa inalinganaje na WCAG), na kwamba mtu wa kiufundi anathibitisha dai badala ya kulipanga faili tu. Leta orodha ya vijenzi vyenu vya watu wa tatu na uliza vipi vina ushahidi wa sasa, unaoaminika wa uzingatiaji. Katika ununuzi wa mashirika makubwa na serikali, andika uzingatiaji wa WCAG 2.2 AA na haki ya kurekebisha kwenye mkataba, kwa sababu ahadi iliyotolewa kabla ya kusaini ni nafuu zaidi sana kutekeleza kuliko kizuizi kilichogunduliwa baada ya kuanza kutumika.

6. **Kiwango chetu lengwa cha uzingatiaji ni kipi, nani anakimiliki, na tunakiweka cha sasa vipi viwango vinavyosonga?** WCAG 2.2 AA ndiyo sakafu ya leo na sheria nyingi zinairejelea, lakini 2.2 iliongeza vigezo ambavyo timu nyingi hazijavipokea, na WCAG 3.0 inakuja na muundo tofauti. Bila mmiliki aliyetajwa, kiwango huteleza: timu tofauti zinalenga matoleo tofauti, hakuna anayefuatilia pengo, na uzingatiaji unaoza kimyakimya kati ya ukaguzi. Amua toleo na kiwango kamili mnachojenga kwacho, nani ana mamlaka ya kukiinua, na jinsi vigezo vipya vinavyofika kwenye mfumo wa usanifu na ufafanuzi wa kukamilika. Leta lengo lenu la sasa lililotajwa, ushahidi wa mahali timu zinalifikia kweli, na mpango mfupi wa barabara wa kupokea vigezo vya 2.2 mlivyoruka. Kwa shirika kubwa au la umma, mmiliki wa ufikivu au kituo cha ubora, taarifa ya ufikivu iliyochapishwa, na mpango ulioandikwa wa toleo linalofuata la kiwango ndivyo vinavyowaruhusu kujibu mdhibiti au mahakama kwa ushahidi badala ya nia njema.

## Mtazamo wa sekta

**Kampuni changa.** Kasi inakupendelea hapa, kwa sababu ufikivu ni nafuu zaidi msingi wa msimbo ukiwa mdogo. Ongeza kichanganuzi cha kiotomatiki kwenye CI na kupitia kwa kibodi kwenye orodha hakiki ya ombi la kuvuta tangu sprint ya kwanza, na uegemee HTML ya kisemantiki ili upate usaidizi wa kibodi na kisomaji skrini bure. Ruka vifuniko na zana nzito; faida ni kwamba timu ya ununuzi ya mteja inapouliza ripoti ya uzingatiaji katikati ya mauzo, unaweza kujibu ndani ya siku badala ya kukimbizana.

**Biashara ndogo.** Bila mtaalamu wa ufikivu na bajeti finyu, nunua ufikivu badala ya kuujenga: chagua jukwaa, mada, au maktaba ya vijenzi inayozingatia tayari na inayosema hivyo, na upendelee wauzaji wanaochapisha taarifa ya ufikivu. Shughulikia misingi ya thamani ya juu mwenyewe kwa zana za bure, ukaguzi wa kibodi-tu, kikagua utofautishaji, na lebo wazi kwenye kila nyanja, kwa sababu hivyo hunasa kushindwa kunakowatenga wateja mara nyingi zaidi. Chukulia mtiririko wa kiotomatiki usio sahihi au usiotumika kama mteja aliyepotea, kwa kuwa biashara ndogo mara chache hutoa njia ya kusaidiwa ya kurudi nayo.

**Biashara kubwa.** Kwa ukubwa kazi ni kufanya ufikivu kuwa sifa ya mfumo kuvuka timu nyingi. Safirisha vijenzi vinavyofikika kwa chaguo-msingi kwenye mfumo wa usanifu, zuia regression kwenye CI, na uanzishe mmiliki au kituo cha ubora chenye mchakato wa kurekebisha na mafunzo kwa wasanifu, wahandisi, na waandishi wa maudhui. Fuatilia uzingatiaji kwa muda kama kipimo, andika uzingatiaji wa WCAG kwenye ununuzi, na simamia vijenzi vya watu wa tatu kama jalada ili wijeti moja iliyopachikwa isishindwe kimyakimya safari ya pamoja.

**Serikali.** Ufikivu ni agizo la kisheria na wajibu wa kiraia, kwa kuwa raia walemavu mara nyingi hawana mtoa huduma mbadala wa manufaa, leseni, au kupiga kura. Jenga kwa kiwango ambacho mamlaka yako inanukuu (kwa mfano Section 508, EN 301 549, au Sheria ya Ufikivu ya Ulaya iliyooanishwa na WCAG 2.2 AA), chapisha taarifa ya ufikivu yenye njia ya kuripoti vikwazo, na ujaribu na umma mlemavu unaowahudumia. Kataa vifuniko kama mbadala wa uzingatiaji halisi, na udai wauzaji watoe ushahidi unaoaminika na haki ya kurekebisha kwenye mkataba.

## Mifano

**Kampuni changa.** Kampuni changa ya watu watatu inayojenga zana ya kuajiri iliongeza kichanganuzi cha ufikivu kwenye ujenzi wake na kupitia kwa kibodi kwa haraka kwenye orodha hakiki ya ombi la kuvuta tangu sprint ya kwanza kabisa, ikiona ni nafuu kubaki inafikika kuliko kurekebisha baadaye. Timu ya ununuzi ya mteja wa ukubwa wa kati ilipouliza ripoti ya uzingatiaji wa ufikivu wakati wa mzunguko wa mauzo, kampuni changa tayari ilitumia HTML ya kisemantiki, iliweka lebo kila nyanja, na ilikuwa na umakini unaoonekana kila mahali, kwa hiyo walijibu ndani ya siku badala ya kukimbizana. Utayari huo ulishinda mkataba ambao mshindani alipoteza kwa sharti lilelile.

**Biashara kubwa.** Muuzaji mkubwa wa rejareja alikabiliwa na kesi ya kundi kwa sababu wateja vipofu hawakuweza kukamilisha malipo kwa kisomaji skrini. Zaidi ya suluhu na ada za kisheria, kampuni ililazimika kurekebisha chini ya ratiba inayosimamiwa na mahakama. Baadaye ilijenga upya ufikivu ndani ya mfumo wake wa usanifu na bomba la CI, iliongeza majaribio ya kisomaji skrini kwenye ufafanuzi wa kukamilika, na kufunza timu zake. Malipo yaliyojengwa upya yanayofikika pia yaliboresha ubadilishaji na kupunguza mawasiliano ya msaada kwa kila mtu: marekebisho yaliyowasaidia watumiaji wa visomaji skrini (lebo wazi, ujumbe wa makosa, mpangilio wa kimantiki) yaliwasaidia watumiaji wote.

**Serikali.** Wakala wa manufaa ya umma ulihitajika kisheria kutimiza WCAG 2.1 AA kwa ombi lake la mtandaoni. Majaribio ya mapema na watumiaji vipofu na wenye uoni hafifu, watumiaji wa kibodi-tu, na watumiaji wenye ulemavu wa kiakili yalifichua kwamba kiashiria cha "nyanja inayohitajika" cha rangi tu, kichagua tarehe kisichofikika, na makosa ya uthibitishaji yasiyotangazwa yalikuwa yakiwazuia watu kumaliza. Kurekebisha haya, kupitia alama za kisemantiki, umakini unaoonekana, matangazo ya makosa ya eneo hai, na msaada wa [lugha rahisi](https://en.wikipedia.org/wiki/Plain_language), kuliwaruhusu raia walemavu kuomba wenyewe kwa mara ya kwanza. Hilo lilipunguza utegemezi wa msaada wa ana kwa ana na kupunguza gharama ya kuhudumia, huku likitimiza agizo la kisheria.

## Kesi ya biashara: sababu, ROI, na TCO

Kesi ya biashara inasimama juu ya ufikiaji wa soko, hatari ya kisheria, gharama ya kuhudumia, na ubora. Watu walemavu na familia zao wanadhibiti nguvu kubwa ya matumizi; kuwatenga kunapoteza hiyo. Huduma zinazofikika hupunguza hitaji la njia za gharama za kusaidiwa (msaada wa simu na ana kwa ana), ambayo ni akiba ya moja kwa moja ya uendeshaji, hasa kwa serikali. Na kwa sababu maboresho ya ufikivu (lebo wazi, usaidizi wa kibodi, maudhui yanayosomeka, alama imara) yanamsaidia kila mtu, kwa kawaida huongeza ukamilishaji na kuridhika kwa jumla.

Kwenye TCO, gharama ya kupokea ni mafunzo, zana, na kujenga ufikivu ndani ya vijenzi na mabomba, yote ya wastani ukifanya tangu mwanzo. Gharama ya kutopokea ni kali na inatoka pande kadhaa: dhima ya kisheria (kesi, suluhu, urekebishaji ulioamriwa na mahakama, adhabu za udhibiti), gharama kubwa zaidi sana ya kurudisha chini ya shinikizo la tarehe ya mwisho, uharibifu wa sifa, na gharama endelevu ya kuhudumia watumiaji waliotengwa kupitia njia ghali zaidi. Kurudisha kwa kawaida kunagharimu mara kadhaa ya kile kubuni ndani kungegharimu.

Kuweka kesi kwa uongozi, anza na wajibu wa kisheria pale unapotumika (haubadiliki kwa serikali na unazidi kwa sekta binafsi). Kisha pima kwa namba idadi ya watu inayoweza kufikiwa unayoitenga, gharama ya njia za kusaidiwa ya kutengwa huko, na faida za "kingo ya barabara" kwa watumiaji wote. Weka ufikivu kama usimamizi wa hatari pamoja na ubora, si hisani.

## Mifumo mibaya na mitego

- **Ufikivu kama kisanduku cha kabla ya uzinduzi**: ukaguzi mwishoni badala ya mazoea endelevu, ukihakikisha kazi ghali ya dakika ya mwisho.
- **"Div soup"**: alama zisizo za kisemantiki zenye vishughulikiaji vya kubofya kwenye vipengele vya jumla, zisizoonekana kwa teknolojia saidizi.
- **Matumizi mabaya ya ARIA**: kubandika ARIA kwenye alama zilizovunjika, ambayo inapotosha visomaji skrini zaidi ya alama za kawaida.
- **Taarifa za rangi tu**: hali inayoonyeshwa kwa rangi peke yake, isiyoonekana kwa wasioona rangi.
- **Umakini usioonekana**: kuondoa muhtasari wa umakini kwa urembo, kuwaacha watumiaji wa kibodi wakiwa wamekwama.
- **Mitego ya kibodi**: madirisha ibukizi na wijeti zinazonasa au kupoteza umakini.
- **Kuridhika na uchanganuzi wa kiotomatiki**: kupita kichanganuzi na kudhani bidhaa inafikika.
- **Vifuniko vya ufikivu**: wijeti za "suluhisho la mstari mmoja" za watu wa tatu ambazo hazitoi uzingatiaji halisi na zinaweza kuzidisha uzoefu.
- **Kuwatenga watumiaji walemavu kwenye utafiti**: kusanifu kwa mtumiaji mlemavu wa kufikirika badala ya kujaribu na halisi.

## Kielelezo cha ukomavu

**Ngazi ya 1: Kuanzisha.** Hakuna mazoea ya ufikivu. Masuala yanagunduliwa tu mtumiaji anapolalamika au kesi inapofika, na jibu ni la kuitikia. Alama si za kisemantiki na hazijaribiwi, na hakuna anayemiliki tatizo.

**Ngazi ya 2: Kuendeleza.** Ufahamu upo na baadhi ya timu zinatenda juu yake: kichanganuzi cha kiotomatiki kwenye ujenzi hapa, kupitia kwa kibodi pale, ukaguzi wa kabla ya uzinduzi kabla ya toleo kubwa. Mazoea ni ya msingi na hayana uthabiti kuvuka timu, ufikivu bado ni orodha hakiki ya hatua za marehemu, na mara nyingi unatolewa kafara chini ya shinikizo la ratiba.

**Ngazi ya 3: Kusawazisha.** WCAG 2.2 AA ni kiwango kilichoandikwa, kinachotekelezwa shirika zima. Ufikivu umejengwa ndani ya mfumo wa usanifu ili vijenzi visafirishwe vikifikika kwa chaguo-msingi, vinajaribiwa kiotomatiki na kwa mkono, na vimeandikwa kwenye ufafanuzi wa kukamilika. Timu zimefunzwa, mmiliki au kituo cha ubora kipo, na mchakato wa kurekebisha umefafanuliwa.

**Ngazi ya 4: Kusimamia.** Ufikivu unapimwa na kudhibitiwa kwa data dhidi ya vipimo vya msingi. Shirika linafuatilia vipimo vya uzingatiaji kwa muda (viwango vya kupita vya kichanganuzi, idadi ya vikwazo vilivyo wazi kwa ukali, ufikiaji wa majaribio ya kisomaji skrini wa safari muhimu, na muda wa kurekebisha), linaviripoti kwa kila timu kwenye dashibodi, na kuchukulia regression kama kushindwa kwa ujenzi badala ya maonyo ya ushauri. Malengo yamewekwa dhidi ya kipimo cha msingi na maendeleo yanapitiwa, kwa hiyo timu inayoteleza inaonekana kabla ukaguzi haujaipata.

**Ngazi ya 5: Kuratibu.** Ufikivu unaboreshwa mfululizo na kuunganishwa kuvuka shirika. Watu walemavu ni sehemu ya utafiti na majaribio mara kwa mara, na ufikivu umepachikwa kwenye ununuzi, tokeni za usanifu, na CI. Shirika linajirekebisha viwango vinaposonga (kupokea vigezo vipya vya WCAG na kujiandaa kwa WCAG 3.0), na linaathiri wauzaji na washirika ili mnyororo mzima wa ugavi uzingatie.

## Mawazo ya kujadili

- Mnazuiaje ufikivu usitolewe kafara tarehe za mwisho zinapobana?
- Mchanganyiko sahihi wa majaribio ya kiotomatiki, ya mkono, na ya watumiaji kwa wasifu wenu wa hatari ni upi?
- Uzingatiaji wa ufikivu unapaswa kuandikwa vipi kwenye mikataba ya wauzaji na ununuzi?
- Mnashughulikiaje pengo kati ya uzingatiaji wa WCAG na utumiaji halisi kwa watu walemavu?
- Timu zinapaswa kujiandaaje kwa WCAG 3.0 huku zikijenga kwa 2.2 leo?
- Mnaajiri na kulipa vipi washiriki walemavu wa utafiti kwa haki na heshima?

## Mambo muhimu ya kukumbuka

- Ufikivu ni sifa ya msingi ya ubora na, kwa serikali, sharti la kisheria.
- Sanifu kwa WCAG 2.2 AA kama sakafu; tumia kanuni za POUR kama mfano wa kiakili.
- HTML ya kisemantiki kwanza; ARIA kujaza mapengo halisi tu, ikifanywa sawa.
- Zana za kiotomatiki hunasa takriban theluthi moja ya masuala; majaribio ya mkono na ya teknolojia saidizi ni muhimu.
- Jaribu na watu walemavu, si kwa ajili yao tu.
- Kujenga ufikivu ndani ni nafuu na kwa kudumu; kurudisha ni ghali na dhaifu.
- Usanifu unaofikika ni usanifu bora kwa kila mtu: athari ya kingo ya barabara ni halisi.

## Marejeo na usomaji zaidi

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2* and supporting Understanding/Techniques documents
- W3C, *WAI-ARIA Authoring Practices Guide*
- W3C Web Accessibility Initiative (WAI), introductory and tutorial materials
- Laura Kalbag, *Accessibility for Everyone*
- Sarah Horton and Whitney Quesenbery, *A Web for Everyone*
- Regine Gilbert, *Inclusive Design for a Digital World*
- U.S. Section 508 standards and Section508.gov guidance
- European standard EN 301 549 and the European Accessibility Act
- Government accessibility guidance (e.g., UK GDS accessibility manual)
- WebAIM, research and articles including the annual accessibility analyses
