# 3.9 Kerfisverkfræði

## Yfirlit og tilgangur

[Kerfisverkfræði](https://en.wikipedia.org/wiki/Systems_engineering) er sú grein að verkfræða heilt flókið kerfi frá enda til enda, svo allir hlutar þess vinni saman að því að mæta raunverulegri þörf. Hlutarnir eru miklu meira en hugbúnaður. Nútímakerfi sameinar yfirleitt hugbúnað, vélbúnað, fólk, gögn og ferla, og það verður að starfa í óreiðukenndum raunheimi. Kerfisverkfræði heldur öllu þessu samstilltu yfir allt líf kerfisins.

Þetta er ólíkt hugbúnaðararkitektúr. Hugbúnaðararkitektúr (kafli 3.1) ákveður hvernig hugbúnaðaríhlutir eru byggðir upp og hvernig þeir tala saman. Kerfisverkfræði situr einu stigi ofar. Hún spyr hvað kerfið í heild verður að gera, hvernig hugbúnaður, vélbúnaður og mannlegir rekstraraðilar skipta verkinu og hvernig þú sannar að fullbúinn hluturinn virki. Faglegt heimili hennar er [INCOSE](https://en.wikipedia.org/wiki/International_Council_on_Systems_Engineering), alþjóðaráð kerfisverkfræði (International Council on Systems Engineering), og akkerisstaðall hennar er [ISO/IEC/IEEE 15288](https://en.wikipedia.org/wiki/ISO/IEC_15288), sem skilgreinir ferlin fyrir líf kerfis.

Þetta skiptir máli fyrir stórar áætlanir fyrirtækja og hins opinbera því kerfi þeirra eru stór, langlíf og öryggis- eða verkefniskritísk. Varnarvettvangur, flugumferðarkerfi eða gervihnattaþyrping blandar sérsmíðuðum vélbúnaði, hlutum frá þriðja aðila, innbyggðum og skýjahugbúnaði og mannlegum rekstraraðilum, og ekkert eitt teymi getur haldið öllu í höfðinu. Þú smíðar líka oft [kerfi kerfa](https://en.wikipedia.org/wiki/System_of_systems): mörg sjálfstæð kerfi, hvert gagnlegt eitt og sér, sem verða að vinna saman til að skila stærri getu.

Þessi kafli tengist hugbúnaðarkröfum (kafli 2.8), grunnatriðum arkitektúrs (kafli 3.1), líkönum og aðferðum hugbúnaðar (kafli 2.12), samvirkni og opnum stöðlum (kafli 3.8) og verkefnastjórnun (kafli 10.6).

## Meginreglur

- **Verkfræddu heildina, ekki hlutana.** Kerfi heppnast eða mistekst sem heild, svo að fínstilla eitt undirkerfi í einangrun getur gert heildina verri.
- **Fylgdu lífsferlinum.** Kerfi hefur líf frá fyrstu hugmynd til lokaniðurlagningar. Skipuleggðu allt það, ekki bara smíðina.
- **Raktu sérhverja kröfu.** Sérhver þörf ætti að varpast á kröfu, hönnunarþátt og próf. Ef þú getur ekki rakið hana geturðu ekki sannað hana.
- **Stýrðu viðmótum af ásetningi.** Flestar bilanir gerast á mörkum milli hluta, svo viðmót verðskulda skýrt eignarhald og stýringu.
- **Sannprófaðu og staðfestu sitt í hvoru lagi.** Að smíða hlutinn rétt (sannprófun) og að smíða rétta hlutinn (staðfesting) eru ólíkar spurningar, og þú þarft bæði svörin.
- **Búðu þig undir sprottna hegðun.** Að sameina hluta skapar hegðun sem enginn einn hluti sýnir. Sumt af henni er tilgangurinn, og sumt er andstyggileg óvænt uppákoma.
- **Samverkfræddu vélbúnað og hugbúnað.** Þegar hvort tveggja er sérsmíðað takmarka ákvarðanir í öðru hitt, svo skipuleggðu þau saman.

## Ráðleggingar

### Stýrðu fullum lífsferli kerfisins

Líttu á kerfið sem hafi heilt líf og skipuleggðu hvert skeið. Algengur lífsferill gengur svona: **hugmynd** (skilja þörfina og kanna valkosti), **kröfur** (segja nákvæmlega hvað kerfið verður að gera), **hönnun** (ákveða arkitektúrinn og hlutana), **samþætting** (leiða hlutana saman), **sannprófun og staðfesting** (sanna að það virki og sé rétta kerfið), **rekstur** (reka og viðhalda því) og **niðurlagning** (leggja það niður örugglega, þar á meðal gögn og förgun). ISO/IEC/IEEE 15288 gefur þér ferlarammann fyrir þetta. Skeiðin þurfa ekki að vera stíf fossaaðferð. Þú getur endurtekið, gert frumgerðir og afhent áfanga. Atriðið er að þú takist meðvitað á við hvert skeið, þar á meðal dýru síðari skeiðin sem fyrstu áætlanir hunsa oft.

### Fangaðu þarfir hagsmunaaðila og úthlutaðu kröfum með rekjanleika

Byrjaðu á fólkinu sem lætur sig kerfið varða: notendum, rekstraraðilum, eigendum, eftirlitsaðilum og almenningi. Safnaðu **þörfum** þeirra á látlausu máli og breyttu þeim síðan í verkfræddar **kröfur** sem eru sértækar og prófanlegar (sjá kafla 2.8). Næst kemur **kröfuúthlutun**: að úthluta hverri kröfu á kerfisstigi á tiltekið undirkerfi, svo þú vitir hvaða hluti ber ábyrgð á að uppfylla hana. Haltu **[rekjanleika](https://en.wikipedia.org/wiki/Requirements_traceability)**fylki, lifandi skrá sem tengir hverja þörf við kröfu hennar, við hönnunarþáttinn sem fullnægir henni og við prófið sem sannprófar hana. Hún leyfir þér að sanna hvenær sem er að sérhver þörf sé þakin og sérhver hluti sé til af ástæðu.

### Stýrðu viðmótum skýrt

Viðmót eru þar sem hlutar mætast og þar sem kerfi bila oftast. Viðmót getur verið líkamlegur tengill, netsamskiptaregla, gagnasnið eða mannlegt verklag. Fyrir hvert þeirra skaltu skrifa **viðmótsstýringarskjal** (Interface Control Document, ICD): samþykkta forskrift á nákvæmlega hvernig tveir hlutar tengjast og skiptast á upplýsingum. Gefðu hverju viðmóti skýran eiganda á hvorri hlið. Að treysta á sameiginlegar, útgefnar forskriftir frekar en einnota tengla gerir samþættingu miklu auðveldari, sem eru samvirknirökin í kafla 3.8. Frystu viðmót snemma þar sem þú getur, því síðbúin breyting gárast í hvern hluta sem snertir það.

### Samþættu og síðan sannprófaðu og staðfestu

**Kerfissamþætting** sameinar undirkerfi í virka heild, yfirleitt í áföngum frekar en öll í einu, svo þú finnir vandamál meðan þau eru enn lítil. Eftir samþættingu kemur **[sannprófun og staðfesting](https://en.wikipedia.org/wiki/Verification_and_validation)** (V&V), tvær aðgreindar athuganir. **Sannprófun** spyr: smíðuðum við kerfið rétt, það er, uppfyllir það tilgreindar kröfur sínar? Þú sannprófar með skoðun, greiningu, sýnikennslu og prófi. **Staðfesting** spyr: smíðuðum við rétta kerfið, það er, mætir það raunverulegum þörfum hagsmunaaðila í raunverulegri notkun? Kerfi getur staðist sannprófun (það uppfyllir forskriftina) en fallið á staðfestingu (forskriftin var röng). Skipuleggðu hvort tveggja snemma og skrifaðu kröfur og viðmót svo hægt sé að sannprófa þau yfirleitt.

### Taktu upp líkanamiðaða kerfisverkfræði

Hefðbundin kerfisverkfræði framleiddi fjöll skjala sem rak úr takti. **[Líkanamiðuð kerfisverkfræði](https://en.wikipedia.org/wiki/Model-based_systems_engineering)** (MBSE) kemur í stað þess hauga með einu, sameiginlegu, formlegu líkani af kerfinu, sem sýnir og skýrslur eru búnar til úr. Algengasta líkanamálið er **[SysML](https://en.wikipedia.org/wiki/Systems_Modeling_Language)** (Systems Modelling Language), myndrænt mál til að lýsa kröfum, uppbyggingu, hegðun og skorðum kerfis. Því allt býr í einu tengdu líkani uppfærir breyting alls staðar og rekjanleiki verður fyrirspurn frekar en handvirkur eltingaleikur. MBSE tengist líkanahugmyndum kafla 2.12. Taktu hana upp smám saman, byrjaðu á áhættumestu hlutunum þar sem sameiginlegt líkan borgar sig hraðast.

### Beittu kerfishugsun á sprottna hegðun

Æfðu [kerfishugsun](https://en.wikipedia.org/wiki/Systems_thinking): rökræddu um heildina og tengslin milli hluta, ekki bara hlutana einn í einu. Svona sér þú fyrir **[sprottna hegðun](https://en.wikipedia.org/wiki/Emergence)**: eiginleika sem birtast aðeins þegar hlutar sameinast og enginn einn hluti sýnir. Góð sprottin hegðun er oft tilgangur kerfisins (drónasveimur þekur svæði sem enginn einn dróni gæti). Slæm sprottin hegðun er óvænta bilunin (tvö örugg undirkerfi víxlverka og skapa hættulegt ástand). Þú getur ekki prófað sprottna hegðun út úr kerfi sem þú mótaðir aldrei, svo notaðu hermun og skipulagða hættugreiningu til að finna hana fyrir rekstur.

### Samverkfræddu vélbúnað og hugbúnað

Þegar kerfi inniheldur sérsmíðaðan vélbúnað skaltu verkfræða vélbúnað og hugbúnað saman, vinnubrögð sem kallast **[samhönnun vélbúnaðar og hugbúnaðar](https://en.wikipedia.org/wiki/Hardware/software_co-design)**. Ákvarðanir binda hvor aðra: vélbúnaðurinn setur tíma-, minnis- og aflmörk sem hugbúnaðurinn verður að lifa innan, og þarfir hugbúnaðarins móta hvað vélbúnaðurinn verður að veita. Langir afhendingartímar vélbúnaðar knýja líka áætlunina. Ákveddu snemma hvaða aðgerðir búa í vélbúnaði og hvaða í hugbúnaði, og endurskoðaðu þá skiptingu eftir því sem skorður koma í ljós.

## Málamiðlanir: kostir og gallar

| Nálgun | Kostir | Gallar / kostnaður |
|---|---|---|
| Full kerfisverkfræðinákvæmni | Færri síðbúnar óvæntar uppákomur, sterkur rekjanleiki, öruggara og úttektarhæft | Hár upphafskostnaður, hægari byrjun, þungt ferli |
| Létt / eingöngu hugbúnaðarnálgun | Hröð, ódýr, sveigjanleg fyrir lítið umfang | Brotnar á stórum fjölfaglegum kerfum, missir af viðmótum og sprottinni hegðun |
| Líkanamiðuð (MBSE) | Einn sannleiksgrunnur, auðveldur rekjanleiki, samræmd sýn | Verkfæra- og þjálfunarkostnaður, menningarbreyting, námsferill |
| Skjalamiðuð kerfisverkfræði | Kunnugleg, lágur verkfærakostnaður, auðvelt að deila | Skjöl reka úr takti, rekjanleiki handvirkur og villuhættulegur |

Meginmálamiðlunin er nákvæmni gegn hraða. Full kerfisverkfræði hleður fyrirhöfn fram í hugmynd, kröfur og viðmótsvinnu. Sú fyrirhöfn borgar sig margfalt á stórum, langlífum, öryggiskritískum kerfum, þar sem galli sem finnst í rekstri getur kostað þúsundfalt meira en sami galli sem finnst í kröfum. Á lítilli, skammlífri, eingöngu hugbúnaðarvöru er sú nákvæmni ofgert. Láttu þyngd ferlisins samsvara stærð, líftíma og áhættu kerfisins. Bilunarhátturinn er að beita einnota verkefnavenjum á kerfi sem mun keyra í þrjátíu ár og bera raunverulega áhættu.

## Spurningar til að ræða með teyminu

1. **Hvar hafið þið smíðað nákvæmlega það sem forskriftin krafðist og samt afhent rangt kerfi, og hvað hefði gripið það?** Sannprófun (smíðuðum við það rétt) og staðfesting (smíðuðum við rétta hlutinn) svara ólíkum spurningum, og kerfi getur staðist hvert sannprófunarpróf en fallið á staðfestingu því forskriftin sjálf var röng. Á stórum áætlunum falla þessi tvö saman í „prófun“, svo enginn staðfestir gegn raunverulegri þörf rekstraraðila fyrr en seint, þegar lagfæring kostar þúsundfalt meira en kröfubreyting. Komdu með fyrra dæmi þar sem afhent kerfi uppfyllti kröfur sínar en missti af raunverulegri þörf, og spyrðu hvaða staðfestingarstarfsemi (hermun með raunverulegum rekstraraðilum, snemmbúin frumgerð á vettvangi) hefði leitt það í ljós fyrr. Skipuleggðu báðar athuganir frá byrjun og skrifaðu kröfur og viðmót svo hægt sé að sannprófa þau yfirleitt. Greinarmunurinn ræður hvar þú eyðir takmarkaðri rýnifyrirhöfn.

2. **Hvernig leitið þið að slæmri sprottinni hegðun áður en kerfið er í rekstri, ekki eftir?** Að sameina örugg undirkerfi getur skapað hættuleg ástönd sem enginn einn hluti sýnir, og þú getur ekki prófað sprottna hegðun út úr kerfi sem þú mótaðir aldrei. Fyrir öryggis- eða verkefniskritíska áætlun er óvænta víxlverkunin sú sem skaðar einhvern eða bregst verkefninu, svo hún þarf að finnast fyrir lifandi rekstur. Komdu með nálgun þína við að móta heildina (hermun, skipulögð hættugreining, SysML-líkan sem fangar víxlverkanir) og spyrðu hvaða þvert-undirkerfishegðun þú hefur í raun kannað á móti gert ráð fyrir að sé ekki til. Góð sprottin hegðun er oft tilgangur kerfisins og vert að hanna í átt að henni. Slæm sprottin hegðun er bilunin sem þú verður að verkfræða gegn. Ef eina samþættingaraðferð þín er að tengja hlutana saman og sjá hvað gerist ertu að skipuleggja að uppgötva sprottna hegðun í framleiðslu.

3. **Hvenær þarf að frysta langan afhendingartíma vélbúnaðarákvarðanir og hvernig knýr sá frestur hugbúnaðaráætlun ykkar?** Þegar kerfi inniheldur sérsmíðaðan vélbúnað verður að samverkfræða hvort tveggja: flögan setur tíma-, minnis- og aflþök sem hugbúnaðurinn lifir innan, og afhendingartímar vélbúnaðar ráða oft allri áætluninni. Teymi sem líta á hugbúnað sem aðskiljanlegan fínstilla staðbundið og rekast síðan á vélbúnaðarskorður við samþættingu og tapa mánuðum. Komdu með afhendingartíma vélbúnaðar og dagsetninguna sem skipting aðgerða milli vélbúnaðar og hugbúnaðar verður að vera ákveðin og endurskoðaðu þá skiptingu eftir því sem skorður koma í ljós frekar en að frysta hana blint. Því fyrr sem þú ákveður hvaða aðgerðir búa í kísil og hverjar í hugbúnaði, því færri dýrar afturvendingar mætirðu. Viðmótin þar á milli verðskulda viðmótsstýringarskjal og eiganda á hvorri hlið, því síðbúin breyting þar gárast í allt sem snertir þau.

4. **Getið þið rakið eina þörf hagsmunaaðila alla leið að kröfunni, hönnunarþættinum og prófinu sem sannar hana, og hver heldur þeim tengslum lifandi?** Rekjanleiki er það sem leyfir þér að sýna hvenær sem er að sérhver þörf sé þakin og sérhver hluti sé til af ástæðu, samt rotnar fylkið á stórri áætlun um leið og enginn á það. Togið á móti er raunverulegt: verkfræðingar upplifa rekjanleika sem skrifræðiskostnað og fylki sem haldið er við í höndunum rekur úr takti hraðar en hönnunin breytist. Komdu með einn raunverulegan þráð úr núverandi áætlun og reyndu að ganga hann frá enda til enda í herberginu, frá nefndri þörf hagsmunaaðila, til úthlutaðrar kröfu, til undirkerfisins og hönnunarþáttarins sem fullnægir henni, til sannprófunarprófsins, og taktu eftir hvar keðjan brotnar. Ákveddu hver á fylkið og hvort það ætti að búa í líkani þar sem rekjanleiki er fyrirspurn frekar en handvirkur eltingaleikur. Fyrir áætlanir fyrirtækja og hins opinbera er fylkið líka úttektargagnið sem eftirlitsaðilar og innkaupayfirvöld krefjast, svo brotin keðja gerir meira en að hægja á verkfræði. Hún getur stöðvað vottun eða greiðslu.

5. **Er líkanamiðuð nálgun þess virði verkfæra- og menningarkostnaðarins fyrir ykkur, eða yrði hún dýr hilluvara?** Skjalamiðuð kerfisverkfræði er kunnugleg og ódýr í verkfærum, en skjöl hennar reka úr takti og rekjanleiki hennar er handvirkur og villuhættulegur. MBSE kemur í stað haugsins með einu tengdu líkani, á verði verkfæra, þjálfunar og raunverulegrar menningarbreytingar. Hvor öfgin er dýr: slepptu MBSE á stórri fjölfaglegri áætlun og þú borgar í samþættingaróvæntum, taktu hana upp án agans til að halda líkaninu núgildandi og hún rotnar í hilluvöru verri en ekkert líkan. Komdu með heiðarlegt mat á verkfæraþroska þínum, hver í teyminu getur í raun samið og viðhaldið SysML-líkani og hvaða eitt áhættumikið undirkerfi gæti tilraunakeyrt nálgunina þar sem sameiginlegt líkan borgar sig hraðast. Ákveddu smám saman frekar en að fyrirskipa það fyrir alla skipulagsheildina í einu. Fyrir stóra áætlun fyrirtækis eða hins opinbera með marga birgja skaltu vega hvort sameiginlegt líkan sé eina raunhæfa leiðin til að halda kröfum, viðmótum og prófum samræmdum yfir verktaka sem annars skiptast á úreltum skjölum.

6. **Fjármagnar lífsferilsáætlun ykkar rekstur og niðurlagningu í alvöru, eða stoppar hún hljóðlega við opnun?** Skeiðin sem ráða heildarkostnaði langlífs kerfis, að reka það í áratugi og leggja það niður örugglega, eru þau sem fyrstu áætlanir hunsa rútínulega, því þrýstingur er alltaf að afhenda. Sjónarmiðið á móti er að peningar og athygli eru knöppust einmitt þegar þessi síðari skeið finnast fjarlægust, svo rekstri, viðhaldi, gagnaflutningi og förgun er frestað þar til það verður dýrt, áhættusamt óðagot. Komdu með núverandi lífsferilsáætlun og athugaðu hvort hún nefnir eigendur, fjárhagsáætlanir og útgönguviðmið fyrir rekstur og niðurlagningu, eða hvort hún lítur á opnun sem marklínu. Spyrðu hvað verður um gögnin og vélbúnaðinn við lok líftíma og hver borgar fyrir árin af viðhaldi þar á milli. Fyrir kerfi fyrirtækja og hins opinbera sem verða að ganga í tuttugu eða þrjátíu ár og síðan hætta undir opinberri athugun getur óskipulögð niðurlagning brotið regluverks-, umhverfis- eða skjalavörsluskyldur, svo niðurlagning á heima í áætluninni og fjárhagsáætluninni frá fyrstu hugmyndarýni.

## Sjónarhorn eftir geirum

**Sprotafyrirtæki.** Örlítið teymi getur ekki rekið formlega kerfisverkfræðiáætlun og ætti ekki að reyna það, en það getur samt litið á fastbúnað, forrit og ský sem eitt kerfi frekar en þrjú aðskilin verkefni. Skrifaðu eitt stutt viðmótsskjal sem festir hvernig hlutarnir tala saman, haltu einfaldri töflu sem tengir hverja viðskiptavinaþörf við hlutann sem fullnægir henni og slepptu þungu ferli. Knappasta auðlind þín er verkfræðiathygli, svo eyddu rekjanleikafyrirhöfn aðeins þar sem röng forsenda á mörkum myndi hljóðlega brjóta vöruna á vettvangi.

**Lítið fyrirtæki.** Án sérstaks kerfisverkfræðings og með þröngt fjárhagsáætlun skaltu hallast að útgefnum stöðlum og keyptum undirkerfum frekar en sérsmíðaðri samþættingu sem þú þarft að hanna og sannprófa sjálfur. Kjóstu söluaðila sem afhjúpa skýrar viðmótsforskriftir svo hlutarnir passi saman án sérsmíðaðs tengils sem þú verður að eiga að eilífu. Rammaðu kaupa-eða-smíða valið um hvaða viðmótum þú getur raunhæft stýrt og sannprófað yfir líftíma vörunnar og keyptu restina.

**Stórfyrirtæki.** Í stórum stíl er vandinn samræmi yfir mörg teymi og birgja: sameiginlegt lífsferilsferli í samræmi við ISO/IEC/IEEE 15288, viðmótsstýringarskjal og nefndur eigandi fyrir hver birgjamörk og rekjanleiki frá enda til enda svo ein íhlutabreyting kveiki ekki áætlunarvítt óðagot. Fjárfestu í MBSE þar sem sameiginlegt líkan heldur kröfum, viðmótum og prófum samstilltum yfir verktaka. Stýrðu ferlinu svo sannprófun og staðfesting haldist aðgreind og sérhver krafa sé úthlutuð á ábyrgan hluta.

**Hið opinbera.** Innkaupareglur, gagnsæi og opinber ábyrgð móta hvert val. Tilgreindu kerfisverkfræðiferli, rekjanleika og V&V-sönnunargögn í samningnum, krefstu þess að birgjar afhendi viðmótsstýringarskjöl og lífsferilsgögn sem þú getur úttekið og taktu frá öryggis- og verkefnastaðfestingu fyrir óháða rýni með raunverulegum rekstraraðilum áður en nokkur lifandi yfirfærsla á sér stað. Skipuleggðu og fjármagnaðu rekstur og niðurlagningu skýrt, því opinber áætlun svarar fyrir allan lífsferilinn, þar á meðal örugga niðurlagningu og skjalavörslu.

## Dæmi

**Sprotafyrirtæki.** Fjögurra manna vélbúnaðarsprotafyrirtæki sem smíðar tengdan skynjara hefur ekki efni á formlegri kerfisverkfræðiáætlun, en lítur samt á vöruna sem eitt kerfi fastbúnaðar, farsímaforrits og skýjabakenda frekar en þrjú aðskilin verkefni. Þeir skrifa eitt stutt viðmótsskjal sem festir hvernig tækið, forritið og þjónninn tala saman (skeytasnið, einingar, villukóða) og halda einfaldri töflu sem tengir hverja viðskiptavinaþörf við hlutann sem fullnægir henni. Þegar ódýrari skynjaraflaga þvingar fram fastbúnaðarbreytingu sýnir sameiginlega viðmótið strax hverju forritið og bakendinn verða að breyta, svo íhlutaskipti brjóta ekki hljóðlega vöruna á vettvangi.

**Stórfyrirtæki.** Alþjóðlegur bílaframleiðandi smíðar nýjan rafbílavettvang: kerfi hugbúnaðar (rafhlöðustjórnun, ökumannsaðstoð, afþreying), vélbúnaðar (mótora, skynjara, flaga) og mannlegra þátta, auk margra birgja sem hver afhendir undirkerfi. Fyrirtækið rekur kerfisverkfræðiáætlun. Þarfir hagsmunaaðila fæða úthlutaðar kröfur, sérhvert birgjaviðmót hefur viðmótsstýringarskjal og SysML-líkan tengir kröfur við hönnun við próf. Þegar rafhlöðufrumubirgir breytir íhlut sýnir rekjanleikalíkanið nákvæmlega hvaða kröfur, viðmót og próf verða fyrir áhrifum, svo breytingin er afmörkuð í stað þess að kveikja áætlunarvítt óðagot.

**Hið opinbera.** Landsbundið flugleiðsöguyfirvald nútímavæðir flugumferðarstjórnunarkerfi sitt, öryggiskritískt kerfi kerfa sem spannar ratsjár, vinnustöðvar flugumferðarstjóra, fjarskipti og hugbúnað, rekið allan sólarhringinn. Áætlunin fylgir ISO/IEC/IEEE 15288 yfir allan lífsferilinn. Sannprófun sannar að hvert undirkerfi uppfylli forskrift sína, og staðfesting gegnum hermun með raunverulegum flugumferðarstjórum sannar að samþætta kerfið styðji örugga starfsemi áður en nokkur lifandi umferð reiðir sig á það. Ströng V&V leyfir yfirvaldinu að færa yfir í áföngum, með varaleið í hverju skrefi, því hér er óprófuð sprottin bilun almannaöryggisatburður.

## Viðskiptarök: hvatar, ávöxtun fjárfestingar og heildarkostnaður

Hvatinn er að gallar verða veldisvaxandi dýrari eftir því sem síðar þeir finnast. Kröfuvilla sem gripin er á kröfuskeiðinu kostar nánast ekkert að laga. Sama villa gripin í rekstri getur kostað þúsundfalt meira, og á öryggiskritísku kerfi getur hún kostað líf, innkallanir eða misheppnað verkefni. Kerfisverkfræði færir gallauppgötvun yfir á ódýru snemmskeiðin.

Fyrir **ávöxtun fjárfestingar** (ROI, verðmæti fengið miðað við kostnað) er ávinningurinn forðuð endurvinna, færri samþættingarbilanir og áætlanir sem standast tíma og fjárhag í stað þess að fara fram úr. Iðnaðarrannsóknir á stórum áætlunum finna ítrekað að sterk kerfisverkfræðifyrirhöfn fylgir minni framúrkeyrslum. Fyrir **heildareignarkostnað** (TCO, allur lífstímakostnaður við að smíða, reka og leggja niður kerfi) gerir kerfisverkfræði grein fyrir rekstrar- og niðurlagningarskeiðunum sem ráða langtímakostnaði en ad hoc verkefni hunsa. Að hanna fyrir viðhaldshæfni, viðmót og förgun frá byrjun lækkar kostnað áratuganna sem kerfið eyðir í notkun. Sjá verkefnastjórnun (kafli 10.6).

## Andmynstur og gildrur

- **Stór fyrirframhönnun án endurtekningar.** Að líta á lífsferilinn sem stífa einstefnu fossaaðferð, svo þú lærir að kröfurnar voru rangar aðeins eftir að hafa smíðað allt.
- **Kröfur án rekjanleika.** Haugur krafna sem enginn tengir við hönnun eða próf, svo þú getur hvorki sannað þekju né réttlætt neinn hluta.
- **Að hunsa viðmót.** Að gera ráð fyrir að undirkerfi passi bara saman og tapa síðan mánuðum við samþættingu í mörkamisræmi sem enginn átti.
- **Sannprófun án staðfestingar.** Að sanna að kerfið uppfylli forskrift sína án þess að athuga nokkurn tíma hvort forskriftin passaði við raunverulegar þarfir og afhenda svo rangt kerfi.
- **Að líta á hugbúnað sem aðskilinn.** Hugbúnaðarteymi fínstilla staðbundið og hunsa vélbúnaðarskorður, tímasetningu og mannlega rekstraraðila.
- **MBSE sem hilluvara.** Að smíða líkan einu sinni og láta það rotna úr takti svo það verður verra en ekkert líkan.
- **Að sleppa niðurlagningarskipulagi.** Engin áætlun um niðurlagningu, gagnaflutning eða förgun, svo lok líftíma verður dýrt, áhættusamt óðagot.

## Þroskalíkan

**Stig 1: Upphaf.** Kerfisverkfræði er ad hoc og viðbragðsdrifin. Kröfur búa í dreifðum skjölum, viðmót uppgötvast við samþættingu og sannprófun er hvaða prófun sem tekst að framkvæma. Stórar áætlanir fara reglulega fram úr og koma teyminu á óvart seint.

**Stig 2: Þróun.** Grunnvinnubrögð eru til á helstu áætlunum. Kröfur eru fangaðar og grunnlínumerktar, lykilviðmót hafa stýringarskjöl og sannprófunaráætlun er til. Vinnubrögð eru ósamræmd milli teyma og byggja á einstaklingum frekar en sameiginlegri aðferð.

**Stig 3: Stöðlun.** Kerfisverkfræði er skjalfestur agi um alla skipulagsheildina í samræmi við ISO/IEC/IEEE 15288 og framfylgt yfir teymi. Allur lífsferillinn er skipulagður, rekjanleika er viðhaldið frá enda til enda, viðmótum er formlega stýrt og sannprófun og staðfesting eru aðgreind og skipulögð. MBSE er notuð á flóknum áætlunum.

**Stig 4: Stjórnun.** Kerfisverkfræði er mæld og stýrð með gögnum. Skipulagsheildin rekur mælikvarða gegn grunnlínum: kröfusveiflu og rekjanleikaþekju, viðmótsgalla sem finnast við samþættingu, árangurshlutföll sannprófunar og staðfestingar og gallaleka eftir lífsferilsskeiði (hve margir gallar sleppa frá hverju skeiði til að finnast síðar á hærri kostnaði). Rýnir stýra áætlunum eftir þessum tölum og þröskuldar kalla fram úrbætur frekar en slökkvistarf eftir á.

**Stig 5: Samhæfing.** Kerfisverkfræði er stöðugt bætt og samþætt um skipulagsheildina. Lifandi MBSE-líkan er eini sannleiksgrunnurinn, rekjanleiki er sjálfvirkur, hermun spáir fyrir um sprottna hegðun fyrir smíði og mælikvarðar fyrri áætlana næra þá næstu. Vélbúnaður og hugbúnaður eru samverkfræddir sem sjálfsagður hlutur og ferlið aðlagast eftir því sem áætlanir, birgjar og áhættur breytast.

## Hugmyndir til umræðu

- Hvar er línan milli kerfisverkfræði og hugbúnaðararkitektúrs í skipulagsheildinni þinni og hver á rýmið þar á milli?
- Geturðu á stærstu áætlun þinni rakið eina þörf hagsmunaaðila alla leið að prófinu sem sannprófar hana? Ef ekki, hvað þyrfti til?
- Hverjar af nýlegum bilunum þínum urðu á viðmóti og hver átti það?
- Myndi MBSE borga sig fyrir þig, eða yrði hún dýr hilluvara miðað við menningu þína og verkfæri?
- Fjallar lífsferilsáætlun þín í alvöru um rekstur og niðurlagningu, eða stoppar hún hljóðlega við opnun?

## Helstu atriði

- Kerfisverkfræði verkfræðir heilt kerfi (hugbúnað, vélbúnað, fólk og ferla) frá enda til enda og er aðgreind frá hugbúnaðararkitektúr.
- Skipuleggðu allan lífsferilinn, frá hugmynd gegnum kröfur, hönnun, samþættingu, V&V, rekstur og niðurlagningu.
- Raktu hverja þörf að kröfu, hönnunarþætti og prófi og úthlutaðu hverri kröfu á ábyrgan hluta.
- Stýrðu viðmótum skýrt með skýru eignarhaldi og stýringarskjölum, því mörk eru þar sem kerfi bila.
- Sannprófun (smíðuðum það rétt) og staðfesting (smíðuðum rétta hlutinn) eru ólíkar athuganir og þú þarft báðar.
- Notaðu MBSE og SysML fyrir einn tengdan sannleiksgrunn og notaðu kerfishugsun til að sjá fyrir sprottna hegðun.
- Láttu þyngd ferlisins samsvara stærð, líftíma og áhættu kerfisins.

## Heimildir og frekari lestur

- INCOSE, *INCOSE Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities*
- ISO/IEC/IEEE 15288, *Systems and Software Engineering: System Life Cycle Processes*
- ISO/IEC/IEEE 29148, *Systems and Software Engineering: Requirements Engineering*
- Sanford Friedenthal, Alan Moore, and Rick Steiner, *A Practical Guide to SysML: The Systems Modelling Language*
- NASA, *NASA Systems Engineering Handbook* (NASA/SP-2016-6105)
- Andrew P. Sage and William B. Rouse, *Handbook of Systems Engineering and Management*
- Dennis M. Buede and William D. Miller, *The Engineering Design of Systems: Models and Methods*
- Donella H. Meadows, *Thinking in Systems: A Primer*
- Eberhardt Rechtin and Mark W. Maier, *The Art of Systems Architecting*
- U.S. Department of Defence, *Defence Acquisition Guidebook* (systems engineering guidance)
