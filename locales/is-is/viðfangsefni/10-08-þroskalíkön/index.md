# 10.8 Þroskalíkön

## Yfirlit og tilgangur

[Þroskalíkan](https://en.wikipedia.org/wiki/Maturity_model) er skipulögð leið til að meta hve hæf og samræmd venja þín er á einhverju sviði og til að lýsa leið til að bæta hana. Það skilgreinir lítinn stiga þrepa. Neðst er vinnan ad hoc og viðbragðsdrifin. Efst er hún mæld, stýrð og stöðugt fínstillt. Hvert þrep hefur sjáanleg einkenni sem þú getur borið saman við.

Þroskalíkön breyta óljósri spurningu („erum við góð í þessu?“) í endurtakanlegt svar („við erum á stigi 2 hér, stigi 4 þar og þetta er það sem stig 3 myndi krefjast“). Þessi bók notar fimm þrepa líkan í hverjum kafla og tekur þau saman í kafla 12.4. Þessi kafli fjallar um agann sjálfan: hvernig líkönin virka, hvenær þau hjálpa og hvernig þau afvegaleiða.

Ástæðan fyrir mikilvægi þeirra er einföld. Stórar skipulagsheildir geta ekki bætt það sem þær sjá ekki. Yfir tugi teyma er geta mjög mismunandi og ósýnilega. Sum teymi hafa framúrskarandi prófanir og veikt öryggi, önnur hið gagnstæða. Þroskalíkan gefur þér sameiginlegan orðaforða og sameiginlegan mælikvarða, svo bil verði samanburðarhæf, fjárfestingu megi forgangsraða og framvindu megi rekja yfir tíma frekar en aðeins fullyrða. Þekkt dæmi eru CMMI ([Capability Maturity Model Integration](https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration), fyrir ferli), DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) líkanið (afhendingarframmistaða hugbúnaðar), OWASP SAMM (Software Assurance Maturity Model) og BSIMM (Building Security In Maturity Model) fyrir hugbúnaðaröryggi, TMMi (Test Maturity Model integration, fyrir prófanir), Agile Fluency líkanið og þroskalíkön gagnastjórnunar, auk óteljandi innri stigakorta.

Fyrir fyrirtæki og sérstaklega hið opinbera bera þroskalíkön sérstakt vægi. Opinber verktaka hefur lengi notað CMMI-matsstig sem hæfisskilyrði seljanda og rammaverk eins og bandaríska CMMC ([Cybersecurity Maturity Model Certification](https://en.wikipedia.org/wiki/Cybersecurity_Maturity_Model_Certification)) binda netöryggisþroska beint við hæfi til varnarmálavinnu. Það gefur þroskalíkönum raunverulegar tennur. Það skapar líka meginhættu þessa kafla: þegar stig verður hlið eða markmið fínstilla menn fyrir matið frekar en undirliggjandi getu. Rétt notuð eru þroskalíkön spegill. Illa notuð eru þau leikhús.

## Meginreglur

- **Þroski er leið, ekki markmið.** Markmiðið er geta og niðurstöður, ekki stigatala.
- **Metðu til að læra, ekki til að gefa einkunn.** Heiðarlegt sjálfsmat slær flatterandi úttekt.
- **Hærra er ekki alltaf betra.** Rétta markmiðið fer eftir áhættu, samhengi og kostnaði.
- **Mældu á hvert svið, ekki ein heildareinkunn.** Geta er ójöfn. Ein tala felur það.
- **Forgangsraðaðu lægsta-þroska, hæstu-áhættu bilunum fyrst.**
- **Gættu þín á [lögmáli Goodharts](https://en.wikipedia.org/wiki/Goodhart%27s_law).** Þegar stig er orðið markmið hættir það að mæla getu.
- **Endurmetðu reglulega.** Þroski rekur þegar fólk, kerfi og ógnir breytast.

## Ráðleggingar

### Veldu rétta líkanið fyrir sviðið

Láttu líkanið passa við getuna sem þú vilt bæta og kjóstu viðurkennd, sönnunargagnabyggð líkön fram yfir uppfundin þar sem þau eru til:

- **Ferli og afhending:** CMMI (víðtækur ferlisþroski), DORA getulíkanið (afhendingarframmistaða, grundað í rannsóknum, kafli 11.2).
- **Öryggi:** OWASP SAMM og BSIMM (hugbúnaðaröryggisvenjur), CMMC (varnarmálanetöryggi).
- **Prófanir og gæði:** TMMi.
- **Lipur aðferðafræði og vinnulag:** Agile Fluency líkanið (kafli 10.7).
- **Gögn:** þroskalíkön gagnastjórnunar (DMM, DCAM).

Til innri nota er einföld fjögurra eða fimm þrepa skali beitt á hverja getu (eins og þessi bók gerir) oft framkvæmanlegri en þungt ytra rammaverk. Taktu frá formleg, úttekin líkön þar sem þau eru samningsbundið krafist.

### Metðu heiðarlega og á hverja getu

Keyrðu mat sem framleiðir sannleika, ekki þægindi. Fáðu fólkið sem vinnur vinnuna með. Safnaðu sönnunargögnum frekar en skoðunum. Gefðu hverri getu einkunn sér, svo myndin endurspegli veruleikann: sterkt hér, veikt þar. Sjálfsmat notað til að leiðbeina umbótum er meira virði en ytra mat notað til að vinna sér inn merki, því hið fyrra umbunar hreinskilni og hið síðara umbunar framsetningu. Kafli 12.4 veitir samþætt sjálfsmat yfir öll svið þessarar bókar. Notaðu það sem upphafstæki.

### Notaðu þroska til að forgangsraða, ekki til að refsa

Úttak mats er forgangsraðaður umbótaverkefnalisti, ekki einkunnaspjald til að kenna um. Sameinaðu þroska við áhættu. Stig 1 geta á lágáhættusviði getur verið í lagi. Stig 2 geta á öryggis- eða reglufylgnimikilvægu sviði er brýnt. Beindu fjárfestingu að bilunum þar sem lágur þroski mætir hárri áhættu og tengdu vinnuna við niðurstöður (kafli 11.1) svo umbætur séu mældar með árangri, ekki með því að klífa stigann sjálfs sín vegna.

### Settu markstig af ásetningi: hærra er ekki ókeypis

Hvert stig upp kostar fyrirhöfn og bætir oft við ferlaþunga. Rétta markmiðið er sjaldan „stig 5 alls staðar.“ Það er stigið þar sem aukageta réttlætir enn aukakostnaðinn fyrir áhættu þess sviðs. Regluverkuð og öryggismikilvæg geta kann sannarlega að þurfa efstu þrepin og úttekt krefst oft að minnsta kosti „skilgreinds“ stigs 3. Mörg önnur eru vel þjónað á stigi 3 og myndu aðeins safna skrifræði með því að ýta lengra. Ákveddu markmið á hverja getu og hættu að klífa þegar áhættuleiðrétt ávöxtun gerir það.

### Gættu þín á þroskaleikhúsi

Eini bilunarhátturinn sem eyðileggur gildi þroskalíkana er að fínstilla fyrir einkunnina. Gættu að mati sem gefur rausnarlega einkunn, sönnunargögnum sett saman aðeins fyrir úttektina eða „stig 5“ fullyrðingum sem framleiðsluatvik mótmæla. Haltu matinu bundnu sjáanlegri hegðun og raunverulegum niðurstöðum. Skiptu um matsmenn eða fáðu ytri raunveruleikaathugun. Líttu á grunsamlega háa sjálfseinkunn sem lykt. Um leið og stigið verður markmiðið hættir líkanið að segja þér sannleikann.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar |
|---|---|---|
| **Formleg úttekin líkön (CMMI, CMMC)** | Samanburðarhæf, samningsbundið viðurkennd, ströng | Dýr. Býður upp á leik. Getur steinrunnið ferli |
| **Létt innri stigakort** | Hröð, framkvæmanleg, lítill kostnaður | Minna samanburðarhæf út á við. Auðvelt að skekkja |
| **Sönnunargagnabyggð getulíkön (DORA)** | Tengd raunverulegum niðurstöðum. Rannsóknabyggð | Þrengra umfang. Þarf raunverulega mælikvarða |
| **Ein heildarþroskaeinkunn** | Einfalt að miðla | Felur ójafna getu. Afvegaleiðir |
| **Mat á hverja getu** | Nákvæm, framkvæmanleg forgangsröðun | Meiri fyrirhöfn. Engin ein fyrirsagnartala |

Meginspennan er **mat sem spegill á móti mati sem markmið**. Sama líkan sem hjálpar teymi að sjá sig skýrt verður gagnstætt tilgangi sínum um leið og stig er tengt umbun, hæfi eða stöðu. Því meira sem stig skiptir máli, því meiri orka flæðir í útlit þroska frekar en innihald.

## Spurningar til að ræða með teyminu

1. **Ættum við að halda hreinskilnu innra sjálfsmati aðskildu frá öllu samningsbundið úttekið stigi og hver á hvort?** Þegar CMMC- eða CMMI-stig hliðar tekjur reka úttektin og sannleikurinn í sundur, því orka flæðir í átt að því að standast frekar en að bæta. Fyrir stórt fyrirtæki eða opinberan seljanda er það bil þar sem áhætta felst: þú stenst úttektina og ert áfram útsett(ur). Haltu tvær bækur af ásetningi. Haltu formlegu úttektinni fyrir hæfi og haltu bersöglu innra stigakorti sem enginn er verðlaunaður fyrir að blása upp. Nefndu eiganda fyrir hvort og líttu á hvaða fjarlægð sem er milli þeirra sem merki til að rannsaka, ekki til að breiða yfir. Komdu með nýleg atvik, næstum-slys og hrörnun eftir úttekt á fundinn sem sönnunargögn um hvor bókin segir sannleikann.

2. **Tökum við fyrir hvert svið upp viðurkennt sönnunargagnabyggt líkan eða finnum við upp eigið stigakort og er það rétt val?** Viðurkennd líkön (DORA fyrir afhendingu, SAMM eða BSIMM fyrir öryggi, TMMi fyrir prófanir) bera rannsóknir og ytri samanburðarhæfni sem heimasmíðað rist getur ekki jafnað. Létt innri fjögurra þrepa skali er hraðari og framkvæmanlegri og oft betri kosturinn fyrir innri stýringu. Gildran er að finna upp þungt sérsmíðað rammaverk sem hefur alla seremóníu formlegs líkans og engan sönnunargagnagrunn. Ákveddu fyrir hvert svið: taktu frá formleg úttekin líkön þar sem samningur krefst þeirra, notaðu sönnunargagnabyggð líkön þar sem þau eru til og passa og haltu einfaldri skala á hverja getu fyrir allt annað. Komdu með lista yfir sviðin, merktu hvaða líkan hvert notar í dag og véfengdu hvert uppfundið stigakort.

3. **Hver keyrir mat okkar, hvernig myndum við grípa rausnarlega einkunnagjöf og hve oft endurmetum við?** Mat sem gefur sjálfu sér einkunn smjaðrar fyrir sjálfu sér og þroski rekur þegar fólk, kerfi og ógnir breytast, svo tveggja ára gömul úttekt er oft skáldskapur. Skiptu um matsmenn eða fáðu ytri raunveruleikaathugun og líttu á grunsamlega háa sjálfseinkunn sem lykt til að elta, ekki sigur til að fagna. Settu endurmatstakt tengdan því hve hratt hvert svið breytist: öryggi oftar en, segjum, skjölun. Safnaðu sönnunargögnum og fáðu fólkið sem vinnur vinnuna með frekar en að safna skoðunum stjórnenda. Ef svar þitt er að eitt teymi gefur sjálfu sér einkunn einu sinni á ári án krossathugunar ertu að mæla þægindi, ekki getu.

4. **Hvaða markþroskastig þarf hver geta í raun og hvar myndi það aðeins kaupa ferlaþunga að ýta hærra?** Hærra er ekki ókeypis: hvert stig upp kostar fyrirhöfn og bætir yfirleitt við seremóníu, svo almennt markmið um stig 5 alls staðar tæmir endanlega umbótafjárhagsáætlun í skrifræði sem sum svið munu aldrei endurgreiða. Fyrir stóra skipulagsheild er rétta markmiðið breytilegt eftir getu, því lágáhættusvið á stigi 2 getur verið fullkomlega öruggt á meðan öryggis- eða reglufylgnimikilvægt svið á sama stigi er neyðarástand. Komdu með áhættumat á hverja getu, heiðarlegt mat á hvað næsta þrep kostar í fyrirhöfn og ferli og öll úttektar- eða samningsgólf, þar sem margar úttektir krefjast að minnsta kosti skilgreinds stigs 3. Í fyrirtækja- og opinberu umhverfi þurfa sum regluverkuð geta sannarlega efstu þrepin á meðan flest eru vel þjónuð á stigi 3, svo ákveddu markmið yfirvegað, getu fyrir getu, og hættu að klífa þegar áhættuleiðrétt ávöxtun gerir það.

5. **Í síðasta skipti sem við hækkuðum þroskastig, batnaði niðurstaðan sem það átti að vernda í raun eða hreyfðist aðeins einkunnin?** Stig sem hækkar á meðan atvik, leiðtími eða gallahlutföll standa í stað er lögmál Goodharts í verki: þegar talan verður markmiðið hættir hún að mæla getu. Fyrir stórt teymi sleppur þetta auðveldlega framhjá, því vel heppnuð úttekt finnst eins og framvinda jafnvel þegar framleiðsla segir aðra sögu. Tengdu stig hverrar getu við raunverulegan niðurstöðumælikvarða áður en þú fjárfestir og komdu síðan með fyrir-og-eftir sönnunargögnin í umræðuna: atvik á ársfjórðung, bilunarhlutfall breytinga, tími til endurheimtar, hvað sem getan er til að bæta. Í fyrirtækja- og opinberum eignasöfnum þar sem úttekið stig hliðar hæfi er bilið hættulegt, því stigið getur hækkað á samsettum sönnunargögnum á meðan undirliggjandi venja hrörnar hljóðlega og fyrsta sönnun þess er brot, rof eða misheppnuð úttekt.

6. **Miðlum við einni fyrirsagnarþroskaeinkunn eða mynd á hverja getu og eru stig nokkru sinni tengd umbun, röðun eða stöðu teymis?** Ein heildartala er auðveld að kynna fyrir forystu og felur nákvæmlega ójöfnuðinn sem skiptir máli, því sterk afhending getur falið stig 1 öryggisgetu. Hitakort á hverja getu er meiri vinna en sýnir hvar lágur þroski mætir hárri áhættu. Erfiðari spurningin er hvernig einkunnirnar eru notaðar, því um leið og stig er tengt umbun eða röðun teymis deyr heiðarleg skýrslugjöf og orka flæðir í útlit þroska frekar en innihald. Komdu með hitakortið og hreinskilna frásögn af hverjum stað þar sem stig fóðrar nú frammistöðumat, fjárhagsákvörðun eða seljendastigakort. Fyrir fyrirtæki og opinbera seljendur, þar sem úttekin stig geta hliðað tekjur og hæfi, vertu skýr um hvaða einkunnir bera afleiðingar og hverjar eru aðeins til að stýra, því þroskamynd sem fólk er verðlaunað fyrir að blása upp hættir að lýsa veruleika.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Þungt úttekið líkan er aukakostnaður sem þú hefur ekki efni á á stuttri fjárhagslegri þrautseigju. Keyrðu klukkustundar sjálfsmat á einfaldri skala yfir handfylli getu, lagaðu aðeins lægsta-þroska bilið sem hindrar eitthvað áþreifanlegt (segjum öryggisspurningalista fyrsta fyrirtækjaviðskiptavinarins) og láttu hitt vera. Matið ætti að kosta síðdegi, ekki ráðgjafa, og úttak þess er ein næsta aðgerð frekar en einsleit há einkunn sem þú hvorki þarft né getur fjármagnað.

**Lítið fyrirtæki.** Án sérstaks matsmanns og með þröngt fjárhagsáætlun skaltu fá létt opinbert líkan að láni frekar en að panta sérsmíðað rammaverk: stuttan afhendingar- eða öryggisgátlista sem þú getur gefið sjálfur einkunn. Líttu á það sem árlegt samtal um hvar veikur blettur myndi kosta þig viðskiptavin, ekki sem viðvarandi áætlun. Haltu því ódýru og berorðu, því flatterandi einkunn sem þú borgaðir seljanda fyrir að framleiða er minna virði en hreinskilin sem þú gerðir sjálf(ur) á síðdegi.

**Stórfyrirtæki.** Verðmætið er sameiginlegt stigakort á hverja getu beitt samræmt yfir mörg teymi, svo bil verði samanburðarhæf og umbótafjárhagsáætlun flæði þangað sem lágur þroski mætir hárri áhættu. Gættu þín harkalega á þroskaleikhúsi þegar stig fóðra fjárhagsáætlun eða stöðu: skiptu um matsmenn eða fáðu ytri raunveruleikaathugun og stýrðu niðurstöðunum sem hitakorti sem beinir troðnu-slóðar fjárfestingu (kafli 4.2) frekar en deildatöflu sem raðar teymum og drepur heiðarlega skýrslugjöf.

**Hið opinbera.** Þroskastig er hér oft bókstaflegt hlið: CMMC fyrir varnarmálavinnu, CMMI-úttekt sem hæfisskilyrði seljanda. Uppfylltu krafið stig með raunverulegri getu og haltu hreinskilnu innra sjálfsmati aðskildu frá formlegri úttekt svo úttektargólfið verði aldrei hljóðlega loftið. Skjalfestu sönnunargögn gagnsætt fyrir matsmenn og líttu á hvaða fjarlægð sem er milli vottaðs stigs og raunverulegrar venju sem ábyrga áhættu til að loka, ekki pappírsvinnu til að skjala.

## Dæmi

**Sprotafyrirtæki.** Tíu manna SaaS-sprotafyrirtæki keyrir klukkustundar sjálfsmat gegn einfaldri fjögurra þrepa skala sem nær yfir afhendingu, prófanir, öryggi og bakvakt. Það finnur afhendingu og prófanir á stigi 3 en öryggi fast á stigi 1, sem skiptir máli því það er við það að skrifa undir fyrsta fyrirtækjaviðskiptavin sinn með öryggisspurningalista. Stofnendurnir eyða því næsta mánuði í að hækka aðeins öryggi í verjanlegt stig 2 og láta hitt vera, frekar en að elta einsleita háa einkunn sem þeir hvorki þurfa né hafa efni á enn.

**Stórfyrirtæki.** Fjármálaþjónustufyrirtæki metur 40 teymi sín með léttu stigakorti á hverja getu (afhending, prófanir, öryggi, sýnileiki, bakvakt). Hitakortið sýnir að öryggisþroski dregst mest aftur úr þar sem regluverksútsetning er hæst, svo vettvangsteymið fjármagnar troðnu-slóðar öryggisverkfæri (kafli 4.2) fyrir þau teymi fyrst. Því matið er notað til að forgangsraða fjárfestingu frekar en að raða teymum skýra stjórnendur heiðarlega frá. Endurmat ári síðar sýnir raunverulega hreyfingu og, mikilvægast, færri öryggisatvik, ekki bara hærri einkunnir.

**Hið opinbera.** Varnarmálaverktaki verður að ná krafinu CMMC-stigi til að bjóða í vinnu og kerfissamþættir heldur CMMI-úttekt sem samningshæfi. Hér er þroskastigið bókstaflegt hlið að tekjum. Vel rekna útgáfan lítur á krafið stig sem gólf fyrir raunverulega getu og heldur hreinskilnu innra sjálfsmati aðskildu frá formlegri úttekt. Illa rekna útgáfan setur saman sönnunargögn fyrir úttektina og lætur raunverulega venju hrörna daginn eftir, stenst úttektina á meðan hún er áfram útsett.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Ávöxtun þroskamats kemur af **beindri fjárfestingu**. Umbótafjárhagsáætlanir eru endanlegar. Eytt blint fjármagna þær það sem er háværast. Þroskamat sýnir þér hvar geta er veikust gegn áhættu, svo sama útgjald kaupir meiri áhættulækkun og meiri niðurstöðubætingu. Matið sjálft er ódýrt, aðeins dagar skipulagðrar, sönnunargagnabyggðrar rýni, borið saman við kostnað misráðstafaðra umbótaáætlana eða, verra, ógreinds getubils sem kemur fram sem brot, rof eða misheppnuð úttekt.

Hvað **heildareignarkostnað** varðar er agi þessi ódýr þegar þú heldur honum léttum og dýr þegar hann harðnar í úttektarskrifræði. Ríkjandi falinn kostnaður er *þroskaleikhús*: fyrirhöfn eytt í að framleiða útlit þroska skilar engu og getur falið raunverulega áhættu, sem er neikvæð ávöxtun. Til að færa rök við forystu skaltu setja fram þroska sem áhættu-og-fjárfestingarlinsu, hitakort sem breytir „bættu allt“ í „bættu þessa þrjá hluti fyrst“, og fjárhagsáætlaðu skýrt gegn freistingunni að elta stig sjálfs sín vegna. Þar sem stig er samningsbundið krafist (CMMC, CMMI) er ávöxtunin bein: það er verðið á hæfi og markmiðið er að uppfylla það með raunverulegri getu frekar en dýrri uppgerð.

## Andmynstur og gildrur

- **Stig sem markmið:** að elta tölu í stað getunnar sem hún á að tákna.
- **Þroskaleikhús:** að setja saman sönnunargögn fyrir úttekt á meðan raunveruleg venja hrörnar.
- **Ein heildareinkunn:** ein þroskaeinkunn sem felur hættulegan ójöfnuð.
- **Hærra-er-alltaf-betra:** að ýta hverri getu á stig 5 óháð áhættu eða kostnaði.
- **Meta einu sinni, aldrei aftur:** einskiptis úttekt meðhöndluð sem varanlegur sannleikur.
- **Raða teymum til að kenna um:** að nota þroska til refsingar, sem drepur heiðarlega skýrslugjöf.
- **Líkanadýrkun:** að fylgja seremóníu þungs rammaverks út fyrir gagnsemi.
- **Að hunsa niðurstöður:** að klífa stigann á meðan afhending, áreiðanleiki eða öryggi batnar ekki.

## Þroskalíkan

- **Stig 1, Upphaf.** Enginn sameiginlegur skilningur á þroska. Geta er gert ráð fyrir, ójöfn og ómæld. Allt mat er viðbragðsdrifið, ræst af atviki eða úttektarkröfu frekar en skipulagt.
- **Stig 2, Þróun.** Fá teymi keyra ad hoc mat gegn einhverri skala, en líkanið, taktur og strangleiki eru ólík eftir teymum. Niðurstöður eru notaðar ósamræmt og sönnunargögn þunn, svo að gefa einkunn fyrir útlitið er stöðug áhætta.
- **Stig 3, Stöðlun.** Eitt líkan á hverja getu og matstaktur er skjalfestur og beitt um skipulagsheildina. Mat er sönnunargagnabyggt, felur í sér fólkið sem vinnur vinnuna og nærir forgangsraðaðan umbótaverkefnalista frekar en einkunnaspjald.
- **Stig 4, Stjórnun.** Þroski er mældur og stýrður með gögnum: stig hverrar getu er rakið gegn grunnlínu, tengt niðurstöðumælikvarða (atvikum, leiðtíma, bilunarhlutfalli breytinga) og endurmetið á föstum takti, svo rek og rausnarleg einkunnagjöf birtast sem tölur frekar en skoðanir og markmið eru sett yfirveguð á hvert svið gegn áhættu og kostnaði.
- **Stig 5, Samhæfing.** Mat er samþætt um skipulagsheildina og stöðugt bætt: þroski, áhætta og niðurstöður upplýsa fjárfestingu sem ein aðlögunarhæf mynd, markmið eru endurjöfnuð þegar ógnir og samhengi breytast, matsmönnum er skipt eða þeir athugaðir að utan sem sjálfsagt mál og venjan leggur virkt niður seremóníu sem vinnur ekki lengur fyrir kostnaði sínum.

## Hugmyndir til umræðu

1. Hverja getu ykkar gerið þið ráð fyrir að sé þroskuð án sönnunargagna?
2. Hvar fellur lægsti þroski ykkar saman við hæstu áhættu ykkar og fer umbótafjárhagsáætlun ykkar þangað?
3. Er einhvert þroskastig í skipulagsheild ykkar markmið eða hlið? Hvaða hegðun hefur það framkallað?
4. Hvert er rétta markstig fyrir hverja getu og hvar myndi frekari klifur aðeins bæta við skrifræði?
5. Myndu teymi ykkar skýra heiðarlega frá þroska sínum eða refsar notkun ykkar á einkunnum hreinskilni?
6. Þegar þið „bættuð þroska“ síðast, breyttust niðurstöður í raun?

## Helstu atriði

- Þroskalíkan metur getu gegn stiga þrepa og lýsir leið til að bæta: spegill, ekki bikar.
- Veldu viðurkennd, sönnunargagnabyggð líkön á hvert svið (CMMI, DORA, SAMM/BSIMM, CMMC). Létt skala á hverja getu er oft framkvæmanlegust.
- **Metðu heiðarlega, á hverja getu**, og notaðu niðurstöður til að **forgangsraða eftir áhættu**, ekki til að raða eða kenna um.
- **Hærra er ekki alltaf betra:** settu markstig yfirveguð gegn áhættu og kostnaði.
- Gættu þín á **þroskaleikhúsi** og **lögmáli Goodharts**: stig sem verður markmið hættir að mæla getu.
- Sjá kafla 12.4 fyrir samþætt þroskasjálfsmat þessarar bókar og hvern kafla eigin þroskahluta.

## Heimildir og frekari lestur

- CMMI Institute / ISACA, *Capability Maturity Model Integration (CMMI)*.
- Watts Humphrey, *Managing the Software Process* (origins of software process maturity).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (capability, not maturity-level, thinking for delivery).
- OWASP, *Software Assurance Maturity Model (SAMM)*; BSIMM (*Building Security In Maturity Model*).
- U.S. Department of Defence, *Cybersecurity Maturity Model Certification (CMMC)*.
- TMMi Foundation, *Test Maturity Model integration*.
- James Shore and Diana Larsen, *The Agile Fluency Model*.
- Martin Fowler, "Maturity Model" (bliki), on their uses and abuses.
