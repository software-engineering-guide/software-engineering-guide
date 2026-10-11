# 12.3 Sniðmát

Þessi sniðmát eru afrita-og-líma tilbúnir upphafspunktar. Lyftu hvaða sniðmáti sem er í wiki, geymslu eða miðakerfi og fylltu út í hornklofa-staðgenglana. Skáletraðar athugasemdir og línuathugasemdir útskýra hvað á heima í hverjum hluta. Eyddu þeim þegar hlutinn er fylltur út. Haltu sniðmátum léttum: sniðmát sem er fljótlegra að sleppa en að klára verður ekki notað. Lagaðu fyrirsagnir og hluta að skipulagsheild þinni, en varðveittu tilgang hvers hluta.

Nokkrar venjur notaðar hér að neðan:

- Texti í `[hornklofum]` er staðgengill til að skipta út.
- Texti í _skáletri_ eða `<!-- athugasemdum -->` er leiðsögn til að eyða.
- Haltu fullbúna skjalinu eins stuttu og hægt er á meðan það svarar enn spurningum sínum.

## Arkitektúrákvörðunarskrá (ADR)

```markdown
# ADR [NNNN]: [Stuttur titill ákvörðunarinnar]

- Staða: [Fyrirhuguð | Samþykkt | Úrelt | Leyst af hólmi af ADR-XXXX]
- Dagsetning: [ÁÁÁÁ-MM-DD]
- Ákvarðanaaðilar: [nöfn eða hlutverk]
- Ráðfært við: [nöfn eða hlutverk]

## Samhengi

<!-- Hvert er vandamálið, aflið eða skorðan sem knýr þessa ákvörðun?
     Settu staðreyndir og kröfur fram hlutlaust. Taktu aðeins með það
     sem framtíðarlesari þarf til að skilja hvers vegna ákvörðun var
     nauðsynleg. -->

## Ákvörðun

<!-- Settu valið fram í einni eða tveimur skýrum setningum: „Við munum ...“ -->

## Valkostir sem voru íhugaðir

<!-- Listaðu raunhæfu kostina sem þú vóst og hvers vegna hver var eða
     var ekki valinn. Að minnsta kosti tveir valkostir ættu að birtast hér. -->

- Kostur A: [samantekt]; hafnað vegna [ástæða].
- Kostur B: [samantekt]; hafnað vegna [ástæða].
- Valinn kostur: [samantekt]; valinn vegna [ástæða].

## Afleiðingar

<!-- Heiðarlegar niðurstöður ákvörðunarinnar, bæði góðar og slæmar. -->

- Jákvætt: [ávinningur sem fékkst]
- Neikvætt: [kostnaður, áhætta eða takmarkanir sem samþykktar eru]
- Eftirfylgni: [flutningar, ný vinna eða ákvarðanir sem þetta ræsir]

## Tengt

<!-- Tenglar á fyrri ADR, RFC, miða eða skjöl sem þetta tengist. -->
```

## RFC / hönnunarskjal

```markdown
# RFC: [Titill]

- Höfundur(ar): [nöfn]
- Staða: [Drög | Í rýni | Samþykkt | Hafnað | Útfært]
- Rýnendur: [nöfn eða hlutverk]
- Stofnað: [ÁÁÁÁ-MM-DD]
- Síðast uppfært: [ÁÁÁÁ-MM-DD]
- Miði / rakning: [tengill]

## Samantekt

<!-- Ein málsgrein: hvað þetta leggur til og hvers vegna það skiptir máli.
     Lesandi ætti að átta sig á kjarnanum úr þessum hluta einum. -->

## Vandamál og hvatar

<!-- Hvaða vandamál erum við að leysa? Hver verður fyrir áhrifum? Hvað
     gerist ef við gerum ekkert? Taktu með viðeigandi bakgrunn og skorður. -->

## Markmið og ekki-markmið

- Markmið: [hvernig árangur lítur út, mælanlegt þar sem hægt er]
- Ekki-markmið: [skýrt utan umfangs, til að koma í veg fyrir umfangssig]

## Fyrirhuguð hönnun

<!-- Kjarni skjalsins. Lýstu nálguninni, arkitektúrnum, gagnalíkaninu,
     viðmótunum og lykilflæðum. Notaðu myndir þar sem þær skýra. Útskýrðu
     hvernig það virkar, ekki bara hvað það er. -->

## Valkostir sem voru íhugaðir

<!-- Aðrar nálganir og hvers vegna þær voru ekki valdar. Sýnir lesandanum
     að hönnunarrýmið var kannað. -->

## Áhrif og áhættur

- Öryggi og persónuvernd: [afleiðingar og mildun]
- Afköst og stærð: [væntanlegt álag og hegðun]
- Rekstrarhæfni: [vöktun, bilunarhættir, útgáfa, afturköllun]
- Kostnaður: [áhrif á innviði eða leyfi]
- Afturábakssamhæfi: [flutningur og úrelding]

## Prófana- og útgáfuáætlun

<!-- Hvernig breytingin verður staðfest og gefin út á öruggan hátt. -->

## Opnar spurningar

<!-- Óútkljáð mál sem þú vilt að rýnendur vegi. -->
```

## Eftirmálsrýni / atvikarýni (án sakbendingar)

```markdown
# Eftirmálsrýni: [Titill atviks]

- Atvikaauðkenni: [ID]
- Dagsetning atviks: [ÁÁÁÁ-MM-DD]
- Höfundar: [nöfn]
- Staða: [Drög | Lokið]
- Alvarleiki: [SEV1 | SEV2 | SEV3]

> Þessi rýni er án sakbendingar. Við einbeitum okkur að kerfum og
> stuðlandi þáttum, ekki einstaklingum. Markmiðið er að læra og að
> koma í veg fyrir endurtekningu.

## Samantekt

<!-- Tvær eða þrjár setningar: hvað gerðist, áhrifin og úrlausnin,
     læsilegt fyrir þann sem er ekki sérfræðingur. -->

## Áhrif

- Lengd: [upphafstími til endurheimtartíma, með tímabelti]
- Notendur fyrir áhrifum: [umfang og fjöldi]
- Viðskiptaáhrif: [tekjur, SLA, orðspor eða annað]

## Tímalína

<!-- Tímastimpluð, staðreyndabyggð röð atburða. Taktu með greiningu,
     stigmögnun, lykilaðgerðir og endurheimt. -->

- [HH:MM] [atburður]
- [HH:MM] [atburður]

## Stuðlandi þættir

<!-- Keðja aðstæðna sem leiddi til atviksins. Kjóstu „stuðlandi þætti“
     fram yfir eina rótarorsök. -->

## Greining og viðbrögð

- Hvernig var það greint? [viðvörun, skýrsla viðskiptavinar o.s.frv.]
- Hvað hjálpaði viðbrögðunum?
- Hvað hægði á viðbrögðunum?

## Hvað fór vel

<!-- Viðurkenndu skilvirkar aðgerðir og varnir sem virkuðu. -->

## Aðgerðaatriði

<!-- Sértæk, í eigu og dagsett. Sinntu forvörnum, greiningu og
     mildun. Raktu þau í venjulegum verkefnalista. -->

| Aðgerð | Eigandi | Skiladagur | Gerð (koma í veg fyrir/greina/milda) | Miði |
|--------|---------|------------|--------------------------------------|------|
| [aðgerð] | [nafn] | [dagsetning] | [gerð] | [tengill] |

## Lærdómur

<!-- Hvað skipulagsheildin í heild ætti að taka með sér. -->
```

## Ógnarlíkan (STRIDE-byggt)

```markdown
# Ógnarlíkan: [Heiti kerfis eða eiginleika]

- Höfundur(ar): [nöfn]
- Dagsetning: [ÁÁÁÁ-MM-DD]
- Rýnendur: [öryggistengiliður, eigendur]
- Umfang: [hvað er og er ekki þakið]

## Kerfisyfirlit

<!-- Stutt lýsing á kerfinu, tilgangi þess og notendum. -->

## Eignir

<!-- Hvað er þess virði að vernda: gögn, skilríki, virkni, orðspor.
     Skráðu viðkvæmni hverrar. -->

## Traustmörk og gagnaflæði

<!-- Lýstu eða teiknaðu íhluti, gagnageymslur, ytri aðila og mörkin
     þar sem traust breytist. -->

## Ógnir (STRIDE)

<!-- Íhugaðu STRIDE-flokkana fyrir hvern þátt. Skráðu hverja trúverðuga
     ógn, áhættu hennar og mildunina eða samþykktu áhættuna. -->

| Ógn | STRIDE-flokkur | Þáttur fyrir áhrifum | Áhætta (L/M/H) | Mildun | Staða |
|-----|----------------|----------------------|----------------|--------|-------|
| [ógn] | Gervi (Spoofing) | [þáttur] | [áhætta] | [stýring] | [opin/milduð/samþykkt] |
| [ógn] | Átroðningur (Tampering) | [þáttur] | [áhætta] | [stýring] | [staða] |
| [ógn] | Afneitun (Repudiation) | [þáttur] | [áhætta] | [stýring] | [staða] |
| [ógn] | Upplýsingaleki (Information disclosure) | [þáttur] | [áhætta] | [stýring] | [staða] |
| [ógn] | Þjónustuneitun (Denial of service) | [þáttur] | [áhætta] | [stýring] | [staða] |
| [ógn] | Réttindahækkun (Elevation of privilege) | [þáttur] | [áhætta] | [stýring] | [staða] |

## Forsendur og ósjálfstæði

<!-- Öryggisforsendur sem reiðst er á og ytri stýringar sem treyst er. -->

## Opin mál og eftirfylgni

<!-- Ógnir sem þarfnast frekari vinnu, raktar sem miðar. -->
```

## Keyrsluhandbók

```markdown
# Keyrsluhandbók: [Heiti verks eða sviðsmyndar]

- Þjónusta: [heiti þjónustu]
- Eigandi: [teymi]
- Síðast rýnt: [ÁÁÁÁ-MM-DD]
- Tengdar viðvaranir: [viðvörunarnöfn]

## Tilgangur

<!-- Hvenær á að nota þessa keyrsluhandbók og hverju hún áorkar. -->

## Forsendur

<!-- Aðgangur, verkfæri og heimildir sem þarf áður en byrjað er. -->

## Greining / einkenni

<!-- Það sem rekstraraðilinn sér: viðvaranir, villuundirskriftir,
     mælaborð. -->

## Orsakagreining

<!-- Skref fyrir skref athuganir til að staðfesta vandamálið og þrengja
     orsökina. Taktu með nákvæmar skipanir, fyrirspurnir eða mælaborðstengla. -->

1. [skref og væntanleg niðurstaða]
2. [skref og væntanleg niðurstaða]

## Úrlausn

<!-- Áþreifanleg, röðuð skref til að laga eða milda. Taktu fram öll skref
     sem eru áhættusöm eða óafturkræf og hvernig á að staðfesta árangur. -->

1. [skref]
2. [staðfestu endurheimt]

## Afturköllun

<!-- Hvernig á að afturkalla aðgerðirnar ef úrlausnin gerir hluti verri. -->

## Stigmögnun

<!-- Hverjum á að ná í og hvenær á að stigmagna. Varabakvakt, eigandi
     teymi og seljendatengiliðir. -->

## Tilvísanir

<!-- Mælaborð, tengdar keyrsluhandbækur, arkitektúrskjöl. -->
```

## Þjónustu-README / færsla í þjónustuskrá

```markdown
# [Heiti þjónustu]

- Eigandi teymi: [teymi]
- Bakvakt: [tengill á vaktaskipulag]
- Þrep / mikilvægi: [Þrep 1 | 2 | 3]
- Geymsla: [tengill]
- Staða: [Virk | Úrelt]

## Hvað hún gerir

<!-- Ein málsgrein um ábyrgð þjónustunnar og notendur hennar. -->

## Arkitektúr

<!-- Lykilíhlutir, ósjálfstæði (uppstreymis og niðurstreymis) og tengill
     á hönnunarskjal eða mynd. -->

## Viðmót

- API / endapunktar: [tengill á forskrift]
- Atburðir birtir / notaðir: [efni]
- Gagnageymslur: [gagnagrunnar, skyndiminni, fötur]

## Keyrslutími og útsetning

- Umhverfi: [dev, staging, prod]
- Hvernig á að útsetja: [tengill á leiðslu og ferli]
- Stilling og eiginleikarofar: [hvar og hvernig]

## Sýnileiki

- Mælaborð: [tenglar]
- Viðvaranir: [tenglar]
- Skrár: [hvar á að finna þær]
- SLO: [tengill]

## Rekstur

- Keyrsluhandbækur: [tenglar]
- Algeng verk: [skölun, endurræsing, bakfylling]
- Þekkt vandamál og takmarkanir: [athugasemdir]

## Að byrja (fyrir nýja framlagsaðila)

<!-- Hvernig á að smíða, prófa og keyra staðbundið. -->

## Tengiliðir

- Slack / spjallrás: [tengill]
- Stigmögnun: [leið]
```

## SLO / villufjárhagsáætlunarstefna

```markdown
# SLO- og villufjárhagsáætlunarstefna: [Heiti þjónustu eða ferðar]

- Eigandi: [teymi]
- Gildistökudagur: [ÁÁÁÁ-MM-DD]
- Rýnitaktur: [t.d. ársfjórðungslega]

## Þjónustustigsvísar (SLI)

<!-- Skilgreindu hvern SLI nákvæmlega: mældu stærðina, hvernig hún er
     mæld og hvaðan (helst frá sjónarhorni notandans). -->

| SLI | Skilgreining | Gagnauppspretta |
|-----|--------------|-----------------|
| Aðgengi | [t.d. árangursríkar beiðnir / heildarbeiðnir] | [uppspretta] |
| Töf | [t.d. hlutfall beiðna undir X ms] | [uppspretta] |

## Markmið (SLO)

| SLI | Markmið | Mælingagluggi |
|-----|---------|---------------|
| Aðgengi | [t.d. 99,9%] | [t.d. rúllandi 28 dagar] |
| Töf | [t.d. 95% undir 300 ms] | [rúllandi 28 dagar] |

## Villufjárhagsáætlun

<!-- Leyfður óáreiðanleiki: 100% mínus markmiðið, yfir gluggann. Settu
     fjárhagsáætlunina fram í áþreifanlegum skilmálum (t.d. mínútur/mánuð). -->

- Fjárhagsáætlun: [leidd heimild]

## Stefna þegar fjárhagsáætlunin er uppurin

<!-- Samþykktu afleiðingarnar. Gerðu þær áþreifanlegar og framfylgjanlegar. -->

- [t.d. Frystu óbráða eiginleikaútgáfur þar til fjárhagsáætlunin jafnar sig.]
- [t.d. Forgangsraðaðu áreiðanleikavinnu í næstu áætlanalotu.]
- [t.d. Stigmagnaðu til verkfræðiforystu ef brotið er tvo glugga í röð.]

## Stefna þegar fjárhagsáætlunin er heilbrigð

<!-- Hvaða aukaáhættu teymið má taka, t.d. hraðari útgáfur. -->

## Viðvaranir

<!-- Brunahraðaviðvaranir og þröskuldar tengdir þessu SLO. -->
```

## Færsla í áhættuskrá

```markdown
## Áhætta: [Stuttur titill áhættu]

- Áhættuauðkenni: [ID]
- Dagsetning vakin: [ÁÁÁÁ-MM-DD]
- Eigandi: [nafn eða hlutverk ábyrgt fyrir að stýra þessari áhættu]
- Flokkur: [öryggi | rekstur | reglufylgni | fjármál | afhending | seljandi]
- Staða: [Opin | Í mildun | Samþykkt | Lokað]

### Lýsing

<!-- Settu áhættuna fram sem: orsök -> atburður -> afleiðing. Hvað gæti
     gerst og hvers vegna það skiptir máli. -->

### Mat

- Líkur: [Lágar | Meðal | Háar]
- Áhrif: [Lág | Meðal | Há]
- Heildareinkunn: [leidd af líkum x áhrifum]

### Núverandi stýringar

<!-- Það sem dregur nú þegar úr þessari áhættu í dag. -->

### Mildunaráætlun

<!-- Fyrirhugaðar aðgerðir til að draga úr líkum eða áhrifum, með
     eigendum og dagsetningum. Ef áhættan er samþykkt skaltu skrá hver
     samþykkti hana og hvers vegna. -->

| Aðgerð | Eigandi | Skiladagur | Staða |
|--------|---------|------------|-------|
| [aðgerð] | [nafn] | [dagsetning] | [staða] |

### Rýni

- Næsta rýnidagsetning: [ÁÁÁÁ-MM-DD]
- Ákvörðun / athugasemdir: [öll samþykktaráritun eða breyting]
```

## Einblöðungur verkefnis / vörukynning

```markdown
# [Heiti verkefnis eða vöru]: einblöðungur

- Styrktaraðili: [nafn]
- Leiðtogi: [nafn]
- Dagsetning: [ÁÁÁÁ-MM-DD]
- Staða: [Hugmynd | Samþykkt | Í vinnslu | Sent]

## Vandamál

<!-- Ein málsgrein: viðskiptavina- eða viðskiptavandamálið og sönnunargögn
     um að það sé raunverulegt og þess virði að leysa. -->

## Markhópur

<!-- Hver hefur þetta vandamál og hver hagnast á að leysa það. -->

## Fyrirhuguð lausn

<!-- Stutt lýsing á því sem við munum smíða eða breyta. Haltu henni á
     stigi ásetnings, ekki útfærsluatriða. -->

## Af hverju núna

<!-- Ástæðan til að gera þetta núna frekar en seinna. -->

## Árangursmælikvarðar

<!-- Hvernig við munum vita að það virkaði. Kjóstu mælanlegar niðurstöður. -->

- [mælikvarði og markmið]

## Umfang

- Innan umfangs: [það sem við munum gera]
- Utan umfangs: [það sem við munum ekki gera]

## Áhættur og opnar spurningar

<!-- Helstu óvissur og ósjálfstæði. -->

## Gróf áætlun og áfangar

<!-- Háleitir áfangar og áætluð tímasetning. -->

## Kostnaður og auðlindir

<!-- Fólk, tími og fjárhagsáætlun sem þarf. -->
```

## Bakvaktarafhendingarglósur

```markdown
# Bakvaktarafhending: [ÁÁÁÁ-MM-DD]

- Fráfarandi: [nafn]
- Komandi: [nafn]
- Þjónusta/þjónustur: [nöfn]

## Heildarstaða

<!-- Ein lína: rólegt, hávaðasamt eða yfirstandandi vandamál. -->

## Opin atvik

<!-- Öll virk eða nýlega leyst atvik sem næsti viðbragðsaðili verður að
     vita um, með tenglum. -->

- [atvik, staða og hvað er eftir]

## Yfirstandandi eða fyrirhugaðar breytingar

<!-- Útsetningar, flutningar, viðhaldsgluggar eða tilraunir í gangi sem
     gætu valdið viðvörunum. -->

## Háværar eða flöktandi viðvaranir

<!-- Viðvaranir sem kviknuðu og raunveruleg merking þeirra, svo næsta
     manneskja sé ekki afvegaleidd. Skráðu allar tímabundnar þaggaðar
     viðvaranir og fyrningu þeirra. -->

## Fylgstu með

<!-- Mælikvarðar eða kerfi sem stefna í áhyggjuvekjandi átt. -->

## Eftirfylgni í bið

<!-- Verk afhent næstu vakt, með tenglum á miða. -->

## Athugasemdir

<!-- Allt annað gagnlegt: aðgangsfrávik, seljandavandamál, samhengi. -->
```

## Breytingabeiðni (fyrir regluverkaða breytingastýringu)

```markdown
# Breytingabeiðni: [Titill breytingar]

- Breytingaauðkenni: [ID]
- Beiðandi: [nafn]
- Dagsetning send: [ÁÁÁÁ-MM-DD]
- Gerð: [Staðlað | Venjuleg | Neyðar]
- Forgangur: [Lágur | Meðal | Hár]
- Staða: [Send | Samþykkt | Hafnað | Útfært | Lokað]

## Lýsing á breytingu

<!-- Hvað er að breytast og hvers vegna. Vísaðu í miðann eða kröfuna. -->

## Kerfi og íhlutir fyrir áhrifum

<!-- Þjónustur, gögn, umhverfi og notendur fyrir áhrifum. -->

## Rökstuðningur og viðskiptaáhrif

<!-- Ástæðan fyrir breytingunni og áhrifin af að gera hana ekki. -->

## Áhættumat

- Áhættustig: [Lágt | Meðal | Hátt]
- Möguleg áhrif ef breytingin bregst: [lýsing]
- Áhrif á öryggi, persónuvernd eða reglufylgni: [lýsing]

## Útfærsluáætlun

<!-- Röðuð skref, ábyrgir aðilar og tímasetning. -->

## Prófana- og staðfestingaráætlun

<!-- Hvernig árangur verður staðfestur fyrir og eftir breytinguna. -->

## Afturfarar- / afturköllunaráætlun

<!-- Hvernig á að snúa breytingunni við ef hún bregst og endurheimtartími. -->

## Tímaáætlun

- Fyrirhugaður gluggi: [byrjun og lok, með tímabelti]
- Væntanlegur niðurtími: [lengd eða enginn]

## Samþykktir

| Hlutverk | Nafn | Ákvörðun | Dagsetning |
|----------|------|----------|------------|
| Breytingaeigandi | [nafn] | [samþykkja/hafna] | [dagsetning] |
| Tæknilegur rýnir | [nafn] | [samþykkja/hafna] | [dagsetning] |
| Breytingaráðgjafarnefnd | [nafn] | [samþykkja/hafna] | [dagsetning] |

## Rýni eftir útfærslu

<!-- Niðurstaða, vandamál sem komu upp og hvort afturför var nauðsynleg. -->
```

## Persónuverndarmat (DPIA) yfirlit

```markdown
# Persónuverndarmat: [Heiti vinnslustarfsemi]

- Matsaðili: [nafn]
- Dagsetning: [ÁÁÁÁ-MM-DD]
- Rýnendur: [persónuverndarfulltrúi / persónuverndartengiliður]
- Staða: [Drög | Rýnt | Samþykkt]

## 1. Lýsing á vinnslunni

<!-- Hvaða persónuupplýsingar eru unnar, hvernig, af hverjum og í hvaða
     tilgangi. Taktu með gagnaflæði frá söfnun til eyðingar. -->

- Skráðir einstaklingar: [um hvern gögnin eru]
- Gagnaflokkar: [gerðir persónuupplýsinga, athugaðu sérstaka flokka]
- Tilgangur: [hvers vegna gögnin eru unnin]
- Viðtakendur og vinnsluaðilar: [hver fær eða meðhöndlar gögnin]
- Varðveislutími: [hve lengi gögn eru geymd og eyðingaraðferð]
- Alþjóðlegir flutningar: [áfangastaðir og flutningsleið]

## 2. Nauðsyn og meðalhóf

<!-- Er vinnslan nauðsynleg fyrir tilganginn? Er hún minnst íþyngjandi
     valkosturinn? Hver er lagagrundvöllurinn eða heimildin? -->

- Lagagrundvöllur / heimild: [grundvöllur fyrir hvern tilgang]
- Gagnalágmörkun: [hvers vegna hver reitur er nauðsynlegur]
- Nákvæmni og rökstuðningur varðveislu: [athugasemdir]
- Hvernig réttindi skráðra einstaklinga eru studd: [aðgangur, eyðing o.s.frv.]

## 3. Samráð

<!-- Hagsmunaaðilar, og þar sem við á skráðir einstaklingar, sem ráðfært var við. -->

## 4. Áhætta fyrir einstaklinga

<!-- Auðkenndu persónuverndaráhættur og metdu hverja. -->

| Áhætta fyrir einstaklinga | Líkur | Alvarleiki | Heild |
|---------------------------|-------|------------|-------|
| [t.d. óheimill aðgangur að viðkvæmum gögnum] | [L/M/H] | [L/M/H] | [einkunn] |

## 5. Ráðstafanir til að draga úr áhættu

<!-- Fyrir hverja áhættu, mildunina og eftirstandandi áhættu eftir hana. -->

| Áhætta | Ráðstöfun | Eftirstandandi áhætta | Samþykkt af |
|--------|-----------|-----------------------|-------------|
| [áhætta] | [stýring] | [L/M/H] | [nafn] |

## 6. Niðurstaða og undirskrift

- Eftirstandandi áhætta ásættanleg: [Já | Nei]
- Ráðstafanir samþykktar af: [nafn, hlutverk]
- Samráð við eftirlitsyfirvald krafist: [Já | Nei]
- Rýnidagsetning: [ÁÁÁÁ-MM-DD]
```
