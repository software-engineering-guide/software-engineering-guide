# 4.7 Auðkenna- og aðgangsstýring

## Yfirlit og tilgangur

Sérhver beiðni sem nær kerfum þínum ber óbeina fullyrðingu: *mér er heimilt að gera þetta*. Auðkenna- og aðgangsstýring (IAM) er sú grein að ákveða hvort sú fullyrðing sé sönn. Hún svarar tveimur aðskildum spurningum sem fólk blandar stöðugt saman. [Auðkenning](https://en.wikipedia.org/wiki/Authentication) sannar hver þú ert. [Heimild](https://en.wikipedia.org/wiki/Authorization) ræður hvað þú mátt gera þegar þú hefur sannað það. Haltu þessum tveimur hugmyndum aðgreindum í huga þér og helmingur ruglingsins í þessu fagi hverfur.

Fyrir stór teymi hefur auðkenni hljóðlega orðið mikilvægasta stýringin sem þú átt. Kafli 4.3 leggur áherslu á að auðkenni sé nýi jaðarinn og kafli 4.1 byggir núlltraust ofan á það: þegar þú hættir að treysta netinu er það eina sem eftir er til að treysta staðfest auðkenni og skýr stefna. Sú breyting þýðir að veikt lykilorðsendurstillingarflæði eða gleymdur þjónustureikningur er ekki lengur lítill galli. Það eru framdyrnar. Flest raunveruleg innbrot eru ekki sniðugar árásir á minnisöryggisgalla. Þau eru stolin auðkennisgögn, of víðar heimildir og reikningar sem hefði átt að loka mánuðum fyrr.

Hagsmunirnir hækka í fyrirtækja- og opinberu umhverfi. Hnattrænt fyrirtæki stýrir í einu tugum skarast skráa, þúsundum nýliða og brottfarenda á mánuði og samstarfsaðilum sem þurfa afmarkaðan aðgang að sneið af kerfum þínum. Opinber stofnun leggur ofan á snjallkortaauðkennisgögn, fyrirskipuð auðkennistryggingarstig og endurskoðendur sem munu spyrja, skriflega, nákvæmlega hver gat snert tiltekna skrá á tilteknum degi. Þessi kafli hefur skoðun á því hvernig á að byggja auðkennalag sem svarar þeim spurningum vel án þess að stöðva fólkið þitt.

## Meginreglur

- **Auðkenning og heimild eru ólík vandamál.** Að sanna auðkenni og veita heimild þarfnast aðskilinnar hönnunar og aðskilinnar rýni.
- **Eitt auðkenni, mörg kerfi.** Sameinaðu í eina sannleiksuppsprettu fyrir hvern auðkennahóp. Skráasprenging er öryggisgalli.
- **Lágmarksréttindi sjálfgefið.** Byrjaðu á núllaðgangi og bættu við af ásetningi, fyrir menn og vélar jafnt.
- **Sérhvert auðkennisgagn er tímabundið.** Kjóstu skammlíf, sjálfvirkt útgefin auðkennisgögn fram yfir langlíf leyndarmál.
- **Afvirkjun skiptir jafn miklu máli og útvegun.** Aðgangur sem lifir lengur en þörfin er hrein áhætta.
- **Vefveiðaþolið slær mannskiljanlegt.** Færðu auðkenningu í átt að aðgangslyklum og vélbúnaðarstuddum þáttum.
- **Vélar eru líka auðkenni.** Vinnuálög, leiðslur og þjónustur þurfa stýrt auðkenni, ekki sameiginlega kyrrstæða lykla.
- **Aðgangur er lífsferill, ekki atburður.** Veittu, rýndu og afturkallaðu á áætlun og sannaðu að þú gerðir það.

## Ráðleggingar

### Aðgreindu auðkenningu frá heimild og miðlægðu hvort tveggja

Auðkenndu gegnum eina auðkennaveitu (IdP), kerfi sem staðfestir auðkenni og gefur út tákn sem önnur kerfi treysta. Láttu síðan hvert forrit taka eigin heimildarákvarðanir út frá auðkenninu og eigindunum sem táknið ber. Þessi skipting leyfir þér að styrkja auðkenningu einu sinni, fyrir alla, á meðan fínkorna heimildarrökfræði helst nálægt gögnunum sem hún ver. Taktu upp [einfalda innskráningu](https://en.wikipedia.org/wiki/Single_sign-on) (SSO), þar sem ein auðkenning veitir aðgang að mörgum forritum, svo fólkið þitt hafi eina sterka innskráningu í stað fjörutíu veikra. Samband (federation) framlengir sama traust yfir skipulagsmörk og leyfir auðkennum samstarfsaðila að nálgast kerfi þín án þess að þú stýrir lykilorðum þeirra.

### Notaðu nútímasamskiptareglurnar fyrir það sem hver er í raun ætluð

Þrír staðlar vinna mestu vinnuna og hver hefur sitt hlutverk. **OpenID Connect (OIDC)** er auðkennislag byggt á [OAuth](https://en.wikipedia.org/wiki/OAuth) 2.0. Notaðu það til að svara *hver er þessi notandi* fyrir vef- og farsímainnskráningu. **OAuth 2.0** er heimildarrammi fyrir framseldan aðgang. Notaðu hann til að leyfa forriti að kalla á API fyrir hönd notanda án þess að sjá nokkurn tíma lykilorð hans (kafli 2.3). **Security Assertion Markup Language (SAML)** er eldri XML-byggður sambandsstaðall. Hann er enn vinnuhesturinn fyrir fyrirtækja-SSO inn í rótgróin viðskiptaforrit. Algeng mistök eru að ná í OAuth til að auðkenna beint. OAuth veitir aðgang að tilföngum, OIDC situr ofan á honum til að staðfesta auðkenni. Veldu OIDC fyrir nýja notendasnúna innskráningu, haltu SAML þar sem fyrirtækjaskráin krefst þess og finndu ekki upp eigið tákngerðarsnið.

### Gerðu auðkenningu vefveiðaþolna

Lykilorð ein og sér eru óverjandi í stærð. Krefstu fjölþátta auðkenningar (MFA), sem sameinar eitthvað sem þú veist, eitthvað sem þú hefur og eitthvað sem þú ert, fyrir hvern mannlegan reikning án undantekningar. Ýttu síðan framhjá veiku þáttunum: einnota kóðar yfir SMS er hægt að veiða og SIM-skipta. Sterki áfangastaðurinn eru [aðgangslyklar](https://en.wikipedia.org/wiki/Passkey) og undirliggjandi WebAuthn staðallinn (vafra-API fyrir auðkenningu með opinberum lyklum), sem binda innskráningu við vélbúnaðarhaldinn einkalykil og við uppruna raunverulegu síðunnar, svo fölsuð síða geti ekki safnað neinu sem er þess virði að stela. Aðgangslyklar eru líka lykilorðslausir, sem notendur þínir munu þakka þér fyrir. Líttu á reikningsendurheimt og lykilorðsendurstillingu sem hluta auðkenningaryfirborðsins, því árásaraðili sem getur ekki sigrað MFA þitt mun einfaldlega ráðast á endurstillingarflæðið í staðinn.

### Stýrðu líftíma nýliða-flutnings-brottfarar og afvirkjaðu hratt

Auðkenni er lífsferill. **Nýliði** þarf réttan aðgang á degi eitt. **Flutningsmaður** sem skiptir um hlutverk þarf nýjan aðgang og, afgerandi, þarf gamli aðgangurinn að vera fjarlægður, annars safnar hann hægt lyklunum að allri byggingunni. **Brottfarandi** verður að missa allan aðgang tafarlaust, helst innan mínútna frá lokadegi sínum, yfir hvert kerfi. Knúðu þetta frá valdbærri uppsprettu, yfirleitt mannauðskerfinu, svo stöðubreyting þar útvegi og afvirki niðurstraums sjálfvirkt. Sjálfvirknivæddu það. Handvirkir brottfaralistar missa alltaf af einhverju og reikningurinn sem þeir missa af er sá sem birtist í atvikaskýrslunni.

### Veldu heimildarlíkan og tjáðu það sem stefnu-sem-kóða

Veittu heimildir með [hlutverkabyggðri aðgangsstýringu](https://en.wikipedia.org/wiki/Role-based_access_control) (RBAC), þar sem þú úthlutar heimildum á starfsvirknihlutverk og úthlutar fólki á hlutverk, því hún er einföld að rökræða um og auðveld að úttekta. Náðu í [eigindabyggða aðgangsstýringu](https://en.wikipedia.org/wiki/Attribute-based_access_control) (ABAC) þar sem þú þarft samhengismeðvitaðar ákvarðanir byggðar á eigindum eins og deild, gagnaflokkun, staðsetningu eða tíma dags. Flestar þroskaðar skipulagsheildir reka blending: RBAC fyrir grófu veitingarnar, ABAC fyrir fínu skilyrðin. Hvort sem þú velur skaltu tjá heimild sem **stefnu-sem-kóða**: reglur skrifaðar á útgáfustýrðu, prófanlegu, rýnanlegu formi frekar en smellt inn í stjórnborð. Stefna-sem-kóði gerir aðgangsákvarðanir úttektarhæfar, mismunanlegar og samræmdar yfir umhverfi, og hún leyfir þér að prófa heimildarbreytingu áður en hún fer út.

### Framfylgdu lágmarksréttindum með aðgangi á réttum tíma og PAM

Beittu [lágmarksréttindareglunni](https://en.wikipedia.org/wiki/Principle_of_least_privilege): hvert auðkenni fær lágmarksaðgang sem það þarf og ekkert umfram. Fast réttindi eru óvinurinn, því heimild veitt varanlega er heimild í boði fyrir hvern árásaraðila sem lendir á þeim reikningi hvenær sem er. Kjóstu **aðgang á réttum tíma (JIT)**, þar sem einstaklingur biður um hækkuð réttindi fyrir afmarkaðan glugga, fær þau eftir samþykki og missir þau sjálfvirkt þegar glugginn lokast. Fyrir hættulegustu reikninga þína skaltu taka upp **forréttindaaðgangsstýringu (PAM)**: kerfi sem geymir stjórnunarauðkennisgögn í hvelfingu, miðlar og skráir forréttindasetur og gefur út hækkun eftir þörfum. Markmiðið er enginn fastur stjórnunaraðgangur, svo jafnvel alveg brotin fartölva gefi ekkert varanlegt.

### Gefðu vélum og vinnuálagi raunverulegt auðkenni

Menn eru aðeins hálf auðkenni þín. Þjónustur, leiðslur, gámar og föll auðkenna sig öll gagnvart einhverju, og of oft gera þau það með langlífu leyndarmáli límdu inn í stillingarskrá. Skiptu kyrrstæðum lyklum út fyrir stýrt **vinnuálagsauðkenni**: skammlíf auðkennisgögn gefin út sjálfvirkt til vinnuálags út frá hvar það keyrir og hvað það er. Notaðu gagnkvæmt TLS (mTLS), þar sem báðar hliðar tengingar leggja fram skírteini, fyrir þjónustu-í-þjónustu auðkenningu. Haltu öllum eftirstandandi leyndarmálum í sérstökum leyndarmálastjóra með snúningi, aldrei í frumkóða eða myndum (kafli 4.2). Skammlíf, sjálfvirkt snúin vinnuálagsauðkennisgögn fjarlægja algengustu einstöku orsök skýjaauðkennisgagnaleka.

### Gerðu auðkenni að stjórnlaginu og rýndu aðgang samfellt

Í núlltraustarkitektúr (kafli 4.1) er auðkenni þar sem stefna er ákveðin og framfylgd, svo fjárfestu þar í samræmi. Lokaðu síðan lykkjunni með **aðgangsrýni**, einnig kallaðri endurvottun: á áætlun staðfestir eigandi hvers kerfis að hver manneskja og vél með aðgang þurfi hann enn, og afturkallar það sem þau geta ekki réttlætt. Færðu hvern auðkenningar- og heimildaratburð inn í úttektarslóð sem svarar *hver nálgaðist hvað, hvenær og undir hvaða stefnu* (kafli 4.6). Aðgangsrýni er hvernig þú berst gegn réttindasöfnun, hægu uppsöfnun heimilda þar sem engin ein veiting leit óeðlileg út en sem saman gera reikning alltof öflugan.

## Málamiðlanir: kostir og gallar

| Ákvörðun | Kostir | Gallar |
|---|---|---|
| Miðlæg IdP með SSO | Ein sterk innskráning, samræmd stefna, auðveld úttekt | Einn bilunarpunktur. Rekstrarrof læsir alla úti |
| RBAC | Einfalt, úttektarhæft, kunnuglegt | Hlutverkasprenging. Gróft fyrir samhengisviðkvæmar þarfir |
| ABAC | Fínkorna, samhengismeðvitað, stigvaxar með eigindum | Erfiðara að hanna, prófa og rökræða um |
| Aðgangslyklar / WebAuthn | Vefveiðaþolið, lykilorðslaust, sterkt | Endurheimt og tækjamissir þarfnast vandlegrar hönnunar |
| Aðgangur á réttum tíma | Nánast enginn fastur réttur | Núningur. Krefst hraðra, áreiðanlegra samþykktarleiða |
| Samband við samstarfsaðila | Engin ytri lykilorðastjórnun. Afmarkað traust | Traust er háð hreinlæti samstarfsaðilans sjálfs |
| Langlífir þjónustulyklar | Léttvægt auðvelt að setja upp | Leka-hættir. Helsta orsök auðkennisgagnainnbrota |

Meginspennan er öryggi gegn núningi. Sérhver stýring sem minnkar árásaryfirborðið (MFA á allt, JIT hækkun, stuttur líftími auðkennisgagna) bætir líka skrefi við dag einhvers, og fólk fer framhjá stýringum sem særa of mikið. Leystu það með því að gera örugga leið að auðveldu leiðinni: SSO svo sterk auðkenning sé einn smellur, aðgangslyklar svo ekkert lykilorð sé til að slá inn og sjálfvirk útvegun svo réttur aðgangur einfaldlega birtist. Eyddu núningsfjárhagsáætlun þinni þar sem sprengjusvæðið er stærst, á forréttinda- og framleiðsluaðgangi, og haltu daglegum aðgangi nánast núningslausum.

## Spurningar til að ræða með teyminu

1. **Hve fljótt getið þið í raun afturkallað allan aðgang manneskju sem fer í dag og hvernig vitið þið að það virkaði?** Afvirkjunarhraði er bein mæling á auðkennaþroska þínum, því brottfarandi þar sem aðgangur dvelur er óvaktaður reikningur með raunverulegar heimildir. Í stórri skipulagsheild með tugi ótengdra kerfa er heiðarlega svarið oft „við erum ekki viss“, og bilið eru yfirleitt forritin sem voru aldrei tengd við miðlægu auðkennaveituna. Komdu með raunverulega nýlega brottför og raktu hvert kerfi sem viðkomandi gat snert og athugaðu tímastimpla fyrir hvenær hver aðgangur endaði í raun. Ákveddu markmið, eins og fulla afturköllun innan einnar klukkustundar frá mannauðsstöðubreytingu, og mældu það svo þú getir sannað það frekar en að vona. Ef eitthvert kerfi reiðir sig á að einhver muni handvirkt skref er það reikningurinn sem framtíðarinnbrot mun nota.

2. **Hvar hafið þið enn fastan forréttindaaðgang og langlíf kyrrstæð auðkennisgögn og hvað þyrfti til að útrýma þeim?** Föst stjórnunarréttindi og varanlegir þjónustulyklar eru tvær eignirnar sem árásaraðilar vilja mest, því þær eru varanlegar og öflugar. Skráðu hvern mann með alltaf-kveiktan framleiðslu- eða stjórnunaraðgang og hverja þjónustu sem auðkennir sig með kyrrstæðum lykli og spyrðu heiðarlega hverjar gætu færst yfir í JIT-hækkun eða skammlíft vinnuálagsauðkenni. Sjónarmiðið á móti er rekstrarótti: teymi halda föstum aðgangi því neyðaraugnablik finnast öruggari með hann, svo þú verður að gera neyðarhækkun hraða og áreiðanlega áður en þú tekur föstu réttindin burt. Komdu með listann í umræðuna og raðaðu atriðum eftir sprengjusvæði, með framleiðslu- og stjórnunaraðgang fyrst í forgangi. Lokamarkið er enginn fastur stjórnunaraðgangur og enginn kyrrstæður lykill sem lifir lengur en ein uppsetning.

3. **Hafið þið eitt valdbært auðkenni á hvern mann og hvert vinnuálag, eða nokkur, og hvað kostar sprengingin ykkur?** Skráasprenging, þar sem sami maður er til sem fimm reikningar yfir fimm kerfi með rekandi eigindum, er þar sem afvirkjunarbil og munaðarlaus aðgangur fæðast. Að sameina í eina sannleiksuppsprettu fyrir hvern auðkennahóp er ein af fjárfestingunum með mesta vogarafl sem stórt teymi getur gert, því sérhver niðurstraumsstýring byggir á að vita að tvær skrár séu sama manneskja. Komdu með skrá yfir auðkennageymslur þínar og greindu hverjar eru valdbærar á móti hverjar eru þægileg afrit sem enginn stýrir. Málamiðlunin er að sameining er stór, óglæsilegur flutningur sem keppir við eiginleikavinnu um athygli. Ákveddu hvort viðvarandi kostnaður sprengingarinnar, í úttektarsársauka og innbrotsáhættu, réttlæti að fjármagna þann flutning núna frekar en eftir næsta atvik.

4. **Eru sterkustu auðkenningarþættir ykkar raunverulega vefveiðaþolnir og hvað hindrar ykkur í að leggja lykilorð niður fyrir fullt og allt?** Þátturinn sem árásaraðili getur ekki veitt er sá sem bindur enda á auðkennisgagnaþjófnað sem ráðandi innbrotsleið, og aðgangslyklar bundnir við WebAuthn eru eini víðtækt útsetjanlegi kosturinn sem stenst þá kröfu. Í stórri skipulagsheild er heiðarlega myndin yfirleitt blönduð: aðgangslyklar fyrir suma, einnota kóðar yfir SMS fyrir aðra og langur hali eldri forrita sem enn taka við lykilorði einu og sér. Sjónarmiðið á móti er raunverulegt, því aðgangslyklar færa erfiða vandamálið yfir á endurheimt og tækjamissi, og klaufalegt endurheimtarflæði verður nýja mjúka skotmarkið sem árásaraðili snýr sér einfaldlega að. Komdu með þekjutölurnar eftir þáttagerð, lista yfir forrit sem enn falla til baka á lykilorð og hannaða reikningsendurheimtarleið sem þú myndir treysta gegn ákveðinni félagsverkfræðitilraun. Í fyrirtækja- og opinberu umhverfi skaltu tengja markmiðið við fyrirskipað tryggingarstig, því hátryggingarkerfi sem leyfir enn vefveiðanlegan þátt hefur regluvörslubil jafnt og öryggisbil.

5. **Hvernig ákveðið þið hvaða aðgang hvert auðkenni fær og getið þið mismunað, prófað og sannað þá ákvörðun áður en hún fer út?** Bilið milli „einhver smellti heimildum inn í stjórnborð“ og „rýnd, útgáfustýrð stefna“ er munurinn á aðgangslíkani sem þú getur úttektað og einu sem þú getur aðeins beðist afsökunar á. Fyrir stórt teymi er þrýstingurinn að láta hvert forrit rækta eigin sérsmíðaðar reglur, sem framleiðir hljóðlega hlutverkasprengingu á RBAC-hliðinni og óprófanleg skilyrði á ABAC-hliðinni, þar til enginn getur sagt hvað tiltekin veiting leyfir í raun. Sjónarmiðið á móti er afhendingarhraði, því að tjá heimild sem stefnu-sem-kóða bætir við rýniskrefi sem stjórnborðssmellur gerir ekki, og teymi undir fresti gremjast núninginn þar til fyrsta fallna úttekt eða of víð veiting færir rökin fyrir þeim. Komdu með raunverulega heimildarbreytingu og raktu hvernig hún yrði lögð til, prófuð, rýnd og afturkölluð, auk fjölda hlutverka sem þú hefur og hve mörg enginn getur útskýrt. Í fyrirtækja- og opinberu umhverfi mun endurskoðandi biðja þig að sýna nákvæmlega hver gat nálgast skrá og undir hvaða reglu á tilteknum degi, og aðeins mismunanleg, prófanleg stefna svarar því án óðagots.

6. **Hvenær afturkallaði aðgangsrýni síðast eitthvað raunverulegt og hver ber ábyrgð þegar réttindasöfnun er látin óhindruð?** Aðgangsrýni er stýringin sem berst gegn hægri uppsöfnun heimilda þar sem engin ein veiting leit óeðlileg út, og rýni sem aldrei afturkallar neitt er rýnileikhús sem framleiðir pappírsvinnu í stað öryggis. Í stórri skipulagsheild er bilunarhátturinn gúmmístimpillinn: kerfiseigendur endurvotta hundruð færslna í einni lotu, samþykkja allar því að meta hverja í raun er leiðinlegt og hvatinn til að halda aðgangi flæðandi er sterkari en hvatinn til að skera hann. Sjónarmiðið á móti er að merkingarbærar rýnir kosta eigendatíma og brjóta stundum vinnuflæði einhvers þegar aðgangur sem hann reiddi sig hljóðlega á hverfur, svo þú verður að gera rýnina markvissa og áhættudrifna frekar en ógreindan lista. Komdu með afturköllunarhlutfall síðustu lotu, meðalfjölda réttinda á mann og sönnunargögn um hver á endurvottun hvers kerfis. Í fyrirtækja- og opinberu umhverfi skaltu nefna ábyrga embættismanninn fyrir hverja rýni og takt sem hann er haldinn við, því réttindasöfnun sem enginn ber ábyrgð á að grípa er einmitt ástandið sem endurskoðendur og árásaraðilar nýta báðir.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Keyptu auðkenni, smíðaðu það ekki. Ein hýst auðkennaveita með SSO, aðgangslyklum skyldubundnum og eins-smells brottfararafvirkjun gefur handfylli verkfræðinga fyrirtækjastaðals stöðu fyrir gjald á sæti. Hallaðu þér að innbyggðu vinnuálagsauðkenni veitandans svo ekki sé einn einasti langlífur skýjalykill í leiðslunni þinni og notaðu OIDC og OAuth 2.0 úr hillunni frekar en að finna upp táknameðhöndlun sem þú hefur ekki efni á að viðhalda.

**Lítið fyrirtæki.** Án auðkennasérfræðings á launaskrá skaltu kjósa SSO og MFA sem þegar fylgja verkfærunum sem þú borgar fyrir, og kveikja á þeim frekar en að leita að sérstökum vettvangi. Líttu á nýliða-flutnings-brottfarar vandann sem stuttan skriflegan gátlista bundinn þeim sem á ráðningar, og kjóstu aðgangslykla því þeir fjarlægja lykilorðsendurstillingarþjónustuborðsbyrðina sem þú hefur engan aflögu til að sinna. Forðastu sameiginlegar innskráningar, því þær eru ódýr vani sem gerir síðar eignun og afturköllun ómögulega.

**Stórfyrirtæki.** Verkið er sameining og stjórnarhættir yfir margar skrár og teymi: ein valdbær auðkennaveita knúin frá mannauðskerfinu, sjálfvirk nýliða-flutnings-brottfarar flæði, RBAC fyrir starfsvirkni með ABAC fyrir samhengi og forréttindaaðgangsstýring með setuskráningu. Tjáðu heimild sem stefnu-sem-kóða svo breytingar séu mismunanlegar og prófanlegar, keyrðu tímasettar aðgangsrýnir sem í raun afturkalla og staðlaðu viðmótið svo forrit tengist miðlægu auðkenni í stað þess að rækta hvert sína innskráningu.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð knýja hönnunina. Bindu auðkenningu við vélbúnaðarauðkennisgögn eins og PIV- eða CAC-snjallkort, settu auðkennistryggingarstig samkvæmt NIST SP 800-63 svo áhættumeiri kerfi krefjist hærri tryggingarþátta og haltu óbreytanlegum úttektarskrám sem svara nákvæmlega hver nálgaðist hvað og hvenær. Birtu látlausa meðhöndlun borgarasnúins auðkennis, haltu viðskiptavina- og starfsmannaauðkennastökkum aðskildum og tryggðu að hver forréttindaaðgerð á viðkvæmu kerfi sé miðluð og skráð fyrir endurskoðendurna sem munu spyrja.

## Dæmi

**Sprotafyrirtæki.** Tuttugu manna sprotafyrirtæki getur ekki mannað auðkennateymi, svo það kaupir eitt. Hver starfsmaður skráir sig inn gegnum eina hýsta auðkennaveitu með SSO inn í tölvupóst, kóðahýsingu, skýjastjórnborð og innra forritið, og aðgangslyklar eru skyldubundnir svo engin lykilorð séu til að veiða. Brottför er einn smellur: að afvirkja manneskjuna í auðkennaveitunni sker aðgang alls staðar í einu. Fyrir eigin vöru nota þau OIDC fyrir notendainnskráningu og OAuth 2.0 til að leyfa samþættingum að kalla á API þeirra með afmörkuðum táknum. Þjónustu-í-ský auðkenning notar innbyggt vinnuálagsauðkenni veitandans, svo ekki er einn einasti langlífur skýjalykill neins staðar í leiðslu þeirra. Þetta kostar hóflegt gjald á sæti og kaupir auðkennastöðu sterkari en mörg fyrirtæki reka.

**Stórfyrirtæki.** Fjölþjóðlegur banki hefur eytt áratug í að safna fjórum skrám og hundruðum forrita, sum sambandstengd með SAML, sum með eigin staðbundnum innskráningum. Hann fjármagnar sameiningaráætlun: ein valdbær auðkennaveita, knúin frá mannauðskerfinu, með sjálfvirkum nýliða-flutnings-brottfarar flæðum sem útvega við ráðningu og afturkalla innan mínútna frá uppsögn. RBAC dekkar venjuleg starfsvirkni á meðan ABAC framfylgir gagnabúsetu- og öryggisvottunarreglum fyrir aðgang yfir landamæri. Stjórnendur hafa engan fastan framleiðsluaðgang. Þeir biðja um aðgang á réttum tíma gegnum forréttindaaðgangsstýringarkerfi sem skráir hverja setu. Ársfjórðungslegar aðgangsrýnir neyða kerfiseigendur til að endurvotta eða afturkalla og hver ákvörðun er tjáð sem stefna-sem-kóði svo endurskoðendur geti mismunað nákvæmlega hvað breyttist og hvenær.

**Hið opinbera.** Sambandsstofnun gefur út personal identity verification (PIV) snjallkort, og her-jafngildið common access card (CAC), til starfsfólks síns, svo auðkenning er bundin við vélbúnaðarauðkennisgögn frekar en lykilorð. Auðkennaáætlun hennar fylgir sambands-auðkenna-, auðkennisgagna- og aðgangsstjórnunarnálguninni (FICAM) og setur auðkennistryggingarstig samkvæmt leiðbeiningum National Institute of Standards and Technology, NIST SP 800-63, svo áhættumeiri kerfi krefjast hærri tryggingar auðkennisgagna. Borgarasnúnar þjónustur nota sérstakan viðskiptavinaauðkennastakk á lægra tryggingarstigi með sterku MFA. Aðgangsrýnir og óbreytanlegar úttektarskrár nærir beint sönnunargögn stofnunarinnar um samfellda heimild (kafli 4.6) og hver forréttindaaðgerð á leynilegu kerfi er miðluð og skráð.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun auðkennafjárfestingar kemur frá því að færa ráðandi innbrotsleið þína úr hættusvæðinu. Stolin auðkennisgögn og ofheimilaðir reikningar knýja stóran hluta raunverulegra atvika og hvert ber þungan hala: atvikaviðbrögð, eftirlitssektir, innbrotstilkynningar og varanlegan mannorðsskaða. Vefveiðaþolið MFA eitt og sér útrýmir algengustu innbrotsleiðinni og sjálfvirk afvirkjun lokar munaðarlausa reikningsbilinu sem breytir venjulegri brottför í útsetningu. Þetta eru meðal ódýrustu áhættuminnkana í boði á hvern krónu.

Heildareignarkostnaðurinn er raunverulegur en afmarkaður. Hann felur í sér leyfisgjöld auðkennaveitu, forréttindaaðgangsstýringar- og leyndarmálavettvang, verkfræðina til að tengja hvert forrit við miðlægt auðkenni og viðvarandi fyrirhöfn aðgangsrýna. Stærri kostnaðurinn er skipulagslegur: að sameina skrár og bæta SSO við eldri forrit er hæg, óglæsileg vinna sem keppir við eiginleika. Vegðu það gegn valkostinum. Sundrað auðkenni eyðir sömu peningum að eilífu í formi handvirkra brottfara, úttektaróðagots og lykilorðsendurstillinga á þjónustuborði, auk endanlegs kostnaðar innbrotsins sem sundrunin gerir líklegt. Þegar þú færir rök við forystu skaltu ramma auðkenni sem stjórnlag núlltrausts: sameining og sjálfvirkni eru einskiptis fjárfesting sem lækkar bæði innbrotsáhættu og endurtekinn kostnað úttekta, brottfara og aðgangsstuðnings.

## Andmynstur og gildrur

- **Munaðarlausir reikningar.** Aðgangur sem lifir lengur en manneskjan eða tilgangurinn, sérstaklega óvaktaðir þjónustureikningar og gleymdir verktakar.
- **Fast stjórnunarvald alls staðar.** Alltaf-kveiktur forréttindaaðgangur í stað JIT-hækkunar, sem gefur hverjum brotnum stjórnandareikningi varanlegt vald.
- **Langlífir kyrrstæðir lyklar.** Þjónustuauðkennisgögn límd inn í stillingu eða CI sem aldrei renna út og leka að lokum.
- **Skráasprenging.** Sama manneskja sem margir óstýrðir reikningar, svo engin breyting breiðist nokkurn tíma fullkomlega út.
- **Sameiginlegir reikningar.** Auðkennisgögn notuð af nokkrum, sem eyðileggur eignun og gerir afturköllun ómögulega.
- **SMS sem sterki þátturinn.** Að líta á vefveiðanlega, SIM-skiptanlega einnota kóða sem nægilegt MFA.
- **Hlutverkasprenging.** Svo mörg þröng RBAC-hlutverk að líkanið verður óúttektarhæft og enginn veit hvað hlutverk veitir.
- **Afvirkjun sem handvirkur gátlisti.** Mannleg brottfararskref sem óhjákvæmilega missa af einum reikningnum sem skiptir máli.
- **OAuth notað til auðkenningar.** Að líta á aðgangstákn sem sönnun auðkennis í stað þess að nota OIDC.
- **Rýnileikhús.** Aðgangsendurvottanir gúmmístimplaðar án þess að nokkur meti í raun þörf.

## Þroskalíkan

- **Stig 1, Upphaf:** Hvert forrit hefur sína eigin innskráningu. Lykilorð án samræmds MFA. Útvegun og brottför eru handvirk, viðbragðsdrifin og hæg. Munaðarlausir reikningar safnast. Þjónustuauðkennisgögn eru langlífir kyrrstæðir lyklar. Engar aðgangsrýnir. Heimildir veittar og aldrei endurskoðaðar.
- **Stig 2, Þróun:** SSO nær yfir helstu forrit gegnum miðlæga auðkennaveitu, en þekja er ójöfn milli teyma. MFA er krafist fyrir mestan mannlegan aðgang. Grunn-RBAC er til. Nýliða-flutnings-brottfarar er að hluta sjálfvirkt frá mannauðskerfinu. Sumir forréttindareikningar eru í hvelfingu. Aðgangsrýnir gerast stundum og ósamræmt.
- **Stig 3, Stöðlun:** Sameinuð auðkennaveita er valdbær fyrir starfsfólk, með sjálfvirkri útvegun og skjótri afvirkjun framfylgd um alla skipulagsheildina. Vefveiðaþolið MFA er staðall og skjalfest. RBAC auk ABAC er tjáð sem stefna-sem-kóði. Forréttindaaðgangsstýring með setuskráningu er til staðar. Vinnuálagsauðkenni kemur í stað flestra kyrrstæðra lykla. Tímasettar aðgangsrýnir eru framfylgdar og úttektaðar gegn skriflegri stefnu sem hvert teymi fylgir.
- **Stig 4, Stjórnun:** Auðkennaáætlunin er mæld gegn grunnlínum og stýrð með gögnum. Þú rekur afvirkjunartíma frá mannauðsstöðubreytingu til fullrar afturköllunar, MFA- og aðgangslyklaþekju eftir hópi, fjölda reikninga með föstum forréttindaaðgangi, fjölda langlífra kyrrstæðra lykla enn í notkun, munaðarlausra reikninga og afturköllunarhlutföll aðgangsrýna. Mælikvarðar bera markmið, eins og fulla afturköllun innan einnar klukkustundar og engar nýjar fastar stjórnunarveitingar, og brot á þröskuldi kallar fram rannsókn frekar en axlayppting. Heimildarbreytingar eru prófaðar í leiðslunni og hver fara/ekki-fara ákvörðun um aðgangsveitingu er knúin af sönnunargögnum, ekki vana.
- **Stig 5, Samhæfing:** Auðkenni er stöðugt bætt stjórnlag fyrir núlltraust, samþætt öryggi, áhættu og nýliða-flutnings-brottfarar áætlanagerð um alla skipulagsheildina. Aðgangslyklar eru sjálfgefnir og lykilorð eru lögð niður. Enginn fastur réttur næst með JIT-hækkun, og öll vinnuálög nota skammlíf, sjálfvirkt snúin auðkennisgögn og mTLS. Heimild er algjörlega stefna-sem-kóði. Aðgangsrýnir eru samfelldar og áhættudrifnar, afvirkjun er nánast tafarlaus og hver ákvörðun framleiðir úttektargögn sjálfvirkt. Líkanið aðlagast eftir því sem áhættumerki breytast, herðir eða slakar á aðgangi kvikt frekar en á fastri tíðni.

## Hugmyndir til umræðu

1. Hvað þyrfti til að ná engum föstum stjórnunaraðgangi og hvaða neyðarleið myndi gera það öruggt?
2. Hvar er ABAC virði flækju sinnar í umhverfi þínu á móti því að halda sig við einfalt RBAC?
3. Hve ágengt ættirðu að leggja lykilorð niður í þágu aðgangslykla og hvaða endurheimtarflæði kemur í stað þeirra?
4. Hvaða forrit eru enn utan miðlægu auðkennaveitunnar og hvað heldur þeim þar?
5. Hvernig gefurðu samstarfsaðilum og viðskiptavinum afmarkaðan aðgang án þess að erfa öryggishreinlæti þeirra?
6. Hvaða einstaki mælikvarði fangar best afvirkjunarhraða þinn og ertu að mæla hann í dag?

## Helstu atriði

- Auðkenning sannar hver þú ert. Heimild ræður hvað þú mátt gera. Hannaðu og rýndu þau sitt í hvoru lagi.
- Sameinaðu í eina valdbæra auðkennaveitu með SSO. Skráasprenging er öryggisgalli, ekki þægindi.
- Sjálfvirknivæddu nýliða-flutnings-brottfarar lífsferilinn og gerðu afvirkjun hraða og sannanlega.
- Notaðu OIDC fyrir notendainnskráningu, OAuth 2.0 fyrir framseldan API-aðgang og SAML þar sem fyrirtækjaskráin þarf. Notaðu ekki OAuth sem auðkenningu.
- Færðu auðkenningu í átt að vefveiðaþolnum aðgangslyklum og WebAuthn. Krefstu MFA alls staðar og líttu á veika þætti sem bráðabirgðalausn.
- Framfylgdu lágmarksréttindum með aðgangi á réttum tíma og forréttindaaðgangsstýringu. Stefndu að engum föstum stjórnunarréttindum.
- Gefðu vélum raunverulegt auðkenni með skammlífum vinnuálagsauðkennisgögnum og mTLS. Útrýmdu langlífum kyrrstæðum lyklum.
- Gerðu auðkenni að stjórnlagi núlltrausts (kafli 4.1) og lokaðu lykkjunni með samfelldum aðgangsrýnum og úttektarsönnunargögnum (kafli 4.6).

## Heimildir og frekari lestur

- National Institute of Standards and Technology, *SP 800-63: Digital Identity Guidelines* (identity assurance, authentication, and federation levels)
- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- National Institute of Standards and Technology, *SP 800-162: Guide to Attribute Based Access Control (ABAC) Definition and Considerations*
- National Institute of Standards and Technology, *SP 800-53: Security and Privacy Controls*, Access Control (AC) and Identification and Authentication (IA) families
- The OAuth 2.0 Authorisation Framework, IETF RFC 6749, and the OAuth 2.0 Security Best Current Practice
- OpenID Connect Core 1.0 specification, OpenID Foundation
- Security Assertion Markup Language (SAML) 2.0 specification, OASIS
- Web Authentication (WebAuthn) Level 2, W3C Recommendation, and FIDO2 / FIDO Alliance passkey specifications
- Federal Identity, Credential, and Access Management (FICAM) architecture and playbooks, U.S. General Services Administration
- FIPS 201, *Personal Identity Verification (PIV) of Federal Employees and Contractors*
- Open Policy Agent (OPA) documentation, Cloud Native Computing Foundation (policy-as-code for authorisation)
