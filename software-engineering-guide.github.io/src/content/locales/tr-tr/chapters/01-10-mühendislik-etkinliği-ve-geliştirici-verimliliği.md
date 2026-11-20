# 1.10 Mühendislik etkinliği ve geliştirici verimliliği

## Genel bakış ve motivasyon

Büyük bir yazılım kuruluşunun her lideri er ya da geç aynı sorunun bir sürümünü sorar: yazılım inşa etmekte daha iyi oluyor muyuz ve bunu nasıl bilirdik? Bu bölüm buna dürüstçe cevap vermekle ilgilidir. **Mühendislik etkinliği**, kuruluşunuzun mühendislik çabasını değerli, güvenilir yazılıma ne kadar iyi dönüştürdüğüdür. **Geliştirici verimliliği** bunun bireysel ve takım tarafıdır: bir geliştiricinin ne kadar yararlı çıktı üretebildiği ve çalışma ortamının onların zamanı ve dikkatinin ne kadarını elinden almak yerine geri verdiği.

Sorun, birinin bunu tek bir sayıya indirgemeye çalıştığı anda başlar. Kod satırlarını sayın, insanlar daha çok kod yazar. Hikaye puanlarını sayın, tahminler şişer. Commit'leri, çekme isteklerini ya da masa başı saatleri sayın, ilerlemeyi değil hareketi ödüllendirirsiniz. Bir bilgi çalışanı için verimlilik bir parça sayısı değildir. On bin satır ölü kodu silen ya da bir takım arkadaşının üretim kesintisinden kaçınması için bir gününü eşli çalışmaya harcayan bir geliştirici, hiçbir saf metriğin yakalamadığı mükemmel bir iş yapmıştır. "Ne kadar verimliyiz?" sorusunun dürüst cevabı çok boyutludur ve geliştiricinin işi deneyimlemesini yumuşak değil gerçek bir sinyal olarak ele alır.

Bu, ölçeklendikçe daha çok, daha az değil, önemli hale gelir. Onlarca takımı olan bir kurumsal kuruluşta küçük miktarlarda sürtünme (yavaş bir derleme, kararsız bir test seti, bir ortam için iki günlük bekleme) yüzlerce mühendis boyunca muazzam kayıp kapasiteye dönüşür. Çıktıda piyasa fiyatı olmayan kamuda risk "çıktı tiyatrosu"dur: kamu değeri ölçülmezken üretilen belgeleri ya da kapatılan biletleri ölçmek. Bu bölümün amacı, mühendislik kuruluşunun etkinliğini ve geliştiricilerinin gündelik deneyimini oyunlaştırma, gözetim ya da insanları birbirine karşı sıralama olmadan ölçmenize ve iyileştirmenize yardımcı olmaktır.

## Temel ilkeler

- **Verimlilik çok boyutludur.** Hiçbir tek sayı onu yakalamaz. *Ölçü* olarak sunulan herhangi bir metrik yanlıştır.
- **Sürtünmeyi kaldırmak için ölçün, insanları sıralamak için değil.** Ölçümün konusu sistemdir, birey değil.
- **Üçgenleyin.** Geliştiricilerin işin nasıl hissettirdiğine dair söylediklerini sistemlerin gerçekte kaydettikleriyle birleştirin.
- **Geliştiricinin deneyimi veridir.** Geri bildirim döngüleri, bilişsel yük ve akış ölçülebilir ve iyileştirmeye değerdir.
- **Her metriğin oyunlaştırılacağını varsayın.** Goodhart yasasına karşı birden fazla boyut ve dürüst niyetle tasarlayın.
- **Çıktılara dikkatle bağlayın.** Etkinlik iş değerine bağlanmalı, ama bozan bir hedefe dönüşmemelidir.

## Öneriler

### Tek metrik tuzağını reddedin

İlk disiplin, tek bir sayıyı verimlilik olarak adlandırmayı reddetmektir. Kod satırları, commit sayıları, hikaye puanı [hızı](https://en.wikipedia.org/wiki/Velocity_(software_development)) ve kaydedilen saatlerin hepsi ölümcül bir kusuru paylaşır: değeri değil faaliyeti ölçerler ve faaliyeti şişirmek çocuk oyuncağıdır. Bu, [Goodhart yasasının](https://en.wikipedia.org/wiki/Goodhart%27s_law) iş başında olmasıdır; bir ölçü bir hedefe dönüştüğünde iyi bir ölçü olmaktan çıkar ilkesi. Hız, bir takımın kendi tahmin yardımcısı olarak icat edildi; bir yönetici bir takımın puanlarını diğerininkine karşılaştırdığı anda takımlar tahminlerini sessizce yeniden ölçekler ve sayı anlamsız hale gelir. Biri tek bir verimlilik KPI'ı talep ettiğinde, bunu yerine getirmeniz değil yeniden şekillendirmeniz gereken bir talep olarak ele alın. Bunun yerine küçük dengeli bir küme sunun ve tek bir sayının neden onları yanıltacağını açıklayın.

### Ne ölçeceğinizi yapılandırmak için SPACE'i kullanın

**SPACE çerçevesi** birlikte tutmaya değer beş boyut verir: **S**atisfaction ve well-being (memnuniyet ve iyi oluş), **P**erformance (performans), **A**ctivity (faaliyet), **C**ommunication ve collaboration (iletişim ve iş birliği) ve **E**fficiency ve flow (verimlilik ve akış). SPACE'in amacı, en az birkaç boyut seçmeniz, asla yalnızca bir tane ve asla hepsini aynı kategoriden seçmemenizdir. Faaliyet metrikleri (commit'ler, dağıtımlar) toplaması kolay olduğu için baştan çıkarıcıdır, ama tek başlarına çarpıtırlar. Onları bir memnuniyet sinyali ve bir performans sinyaliyle eşleştirin ki diğerleri ortaya çıkarmadan hiçbir tek boyut oyunlaştırılamasın. Memnuniyet çökerken ve değişiklik başarısızlık oranı tırmanırken daha çok dağıtım yapan bir takım daha verimli değildir ve dengeli bir küme bunu size hemen gösterir.

### Geliştirici deneyimini geri bildirim döngüleri, bilişsel yük ve akış olarak ele alın

**Geliştirici deneyimi (DevEx)**, burada mühendislik işi yapmanın nasıl hissettirdiğidir ve göründüğünden daha somuttur. Ölçüp iyileştirebileceğiniz üç şeye dayanır. **Geri bildirim döngüleri**, bir geliştiricinin bir şeyin işe yarayıp yaramadığını öğrenmek için ne kadar beklediğidir: yerel derleme süresi, test seti süresi, kod inceleme geri dönüşü, dağıtım süresi. Yavaş döngüler bağlam değiştirmeyi ve boşta beklemeyi zorlar. **[Bilişsel yük](https://en.wikipedia.org/wiki/Cognitive_load)**, bir görevin talep ettiği toplam zihinsel çaba, bir geliştiricinin basit bir değişiklik yapmak için çok fazla aracı, belgelenmemiş sistemi ve karmaşık bağımlılığı idare etmesi gerektiğinde artar. **[Akış](https://en.wikipedia.org/wiki/Flow_(psychology))**, parçalanmış takvimlerin ve sürekli kesintilerin yok ettiği odaklı, üretken dalma halidir. Bir geri bildirim döngüsünü kısalttığınızda, bir geliştiricinin kafasında tutması gereken bir kavramı kaldırdığınızda ya da bir odaklanma zamanı bloğunu koruduğunuzda, hiçbir faaliyet sayısının kaydetmeyeceği bir biçimde verimliliği iyileştirmiş olursunuz. Bu, platform mühendisliğinin asfalt yollar ve self servis yoluyla hizmet ettiği aynı DevEx kaygısıdır (bölüm 8.4).

### Algıları sistem metrikleriyle üçgenleyin

Hiçbir tek veri kaynağı tek başına güvenilir değildir, bu yüzden iki türü birleştirin. **Algısal veri**, bir **geliştirici deneyimi anketi** aracılığıyla geliştiricilerin kendilerinden gelir: yayımlamaktan ne kadar emin hissettiklerini, zamanı nerede kaybettiklerini ve neyin sinirlerini bozduğunu soran düzenli, çoğunlukla anonim bir anket. **Sistem verisi** araçlarınızdan gelir: hat zamanlamaları, inceleme gecikmesi, olay sıklığı. Her biri diğerini düzeltir. Anketler araçların kaçırdığı acıyı yakalar; örneğin moral bozucu bir nöbet rotasyonu ya da korkulan bir eski hizmet. Sistem metrikleri insanların normalleştirdiği ve bildirmeyi bıraktığı sorunları yakalar. Bir anket derlemelerin acı verici olduğunu söylediğinde ve hat verileriniz on beş dakikalık ortanca bir derlemeyi doğruladığında, öncelikli, savunulabilir bir yatırımınız olur. Anketi istikrarlı bir ritimle yürütün, kısa tutun ve her zaman anket sayesinde neyin değiştiğini göstererek döngüyü kapatın.

### DORA'yı bir liderlik tablosu değil, bir teslimat sinyali olarak kullanın

Dört **[DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment) (DORA)** metriği (dağıtım sıklığı, değişiklikler için bekleme süresi, değişiklik başarısızlık oranı ve hizmeti geri getirme süresi), hızı istikrarla eşleştiren ve hiçbirinin diğeri için feda edilmediği, teslimat yeteneğiniz hakkında güçlü, araştırma destekli bir okumadır. Bölüm 11.5 bunların derinliğine sahip çıkar ve bölüm 11.2 ölçtükleri teslimat hattını kapsar; onları orada kullanın. Burada rehberlik, onları nasıl tutacağınızla ilgilidir. DORA'yı, takımları ya da bireyleri sıralamak için bir puan tablosu olarak değil, teslimat sisteminizin iyileşip iyileşmediğini gösteren takım düzeyinde bir sağlık sinyali olarak ele alın. DORA sayıları birinin performans değerlendirmesinde göründüğü anda takımlar sıklığı şişirmek için dağıtımları bölmeye ve başarısızlık oranlarını korumak için olayları gizlemeye başlar ve sinyal ölür.

### Sistemi ölçün, bireyi asla gözetlemeyin

Bu, aşmamanız gereken çizgidir. Metrikleri takım ve kuruluş düzeyinde toplayın ve onları sürtünmeyi bulup kaldırmak için kullanın. Geliştiricileri commit'lere, saatlere ya da "verimlilik puanlarına" göre sıralayan panolar kurmayın ve bireysel telemetrinin ücreti ya da terfiyi beslemesine izin vermeyin. Gözetim, etkili mühendisliğin bağımlı olduğu psikolojik güvenliği ve güveni yok eder ve insanlara işi değil metriği optimize etmeyi öğretir. Bireysel gelişim ve değerlendirme, kariyer basamaklarının ve yönetici görüşmelerinin ayrı, insani mekanizmalarına aittir (bölüm 1.3). Etkinlik ölçümü "takımlarımızı ne yavaşlatıyor?" diye sorar. Asla "en yavaş mühendisimiz kim?" diye sormaz.

### Angaryaya ve sürtünmeye doğrudan saldırın

Zamanın nereden sızdığını görebildiğinizde onu geri harcayın. Etkinliği sınırlayan şeyin çoğu, büyümeyle ölçeklenen ve kalıcı değer sunmayan manuel, tekrarlayan, otomatikleştirilebilir iş olan **angaryadır** (bölüm 9.1). Yavaş incelemeler de sürtünmedir, bu yüzden kod incelemesini (bölüm 2.5) daha küçük değişiklikler ve net beklentilerle düzene sokmak temel bir geri bildirim döngüsünü kısaltır. Asfalt yollar ve self servis platformlar (bölüm 8.4) tüm bekleme ve bilişsel yük kategorilerini bir seferde kaldırır. Ayrıca [teknik borca](https://en.wikipedia.org/wiki/Technical_debt) karşı bütçe ayırın; geçmiş kestirmelerin her gelecek değişikliği vergilendiren birikmiş maliyeti; çünkü kimsenin güvenle değiştiremeyeceği bir kod tabanı en derin verimlilik çukurudur.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
| --- | --- | --- |
| Tek verimlilik metriği (LOC, hız, commit'ler) | Ucuz, kolay, liderler için tek bir sayı | Hemen oyunlaştırılır; değeri değil faaliyeti ölçer; güveni aşındırır |
| SPACE tarzı dengeli küme | Oyunlaştırmaya direnir; gerçeği yansıtır | Toplaması daha çok iş; tek bir rakamda özetlemesi daha zor |
| DevEx anketi (algısal) | Araçların kaçırdığı hissedilen acıyı yakalar | Öznel; dürüst kalmak için güven ve takip gerekir |
| Sistem metrikleri (DORA, hat zamanlamaları) | Nesnel, sürekli, toplamda sahtesi zor | Moral ve bağlama kör; bireylere uygulanırsa tehlikeli |
| İkisini üçgenlemek | Her kaynak diğerini düzeltir; sağlam | Araçlara ve anket disiplinine yatırım gerektirir |

Temel gerilim titizlik ile dürüstlük arasındadır. Tek bir sayıyı raporlamak kolaydır ve bozmak kolaydır; zengin, çok boyutlu bir tablo dürüsttür ama meşgul bir yöneticiye iletmesi daha zordur. Bunu küçük dengeli bir küme seçerek (birkaç SPACE boyutu artı bir anket artı teslimat okuması olarak DORA), anlık görüntüler yerine eğilimleri raporlayarak ve sayıların insanları puanlamak için değil sistemi iyileştirmek için var olduğunu açıkça belirterek çözün. Liderlik "tek bir grafik" istediğinde, onlara birkaç tamamlayıcı sinyalin bir eğilimini verin ve onları sahte bir bileşik haline çökertme dürtüsünü reddedin.

## Takımınızla tartışılacak sorular

1. **Bir lider yarın tek bir verimlilik sayısı talep etse, ona ne verirdiniz?** Bu soru kuruluşunuzun tuzağı anlayıp anlamadığını ortaya çıkarır. Dürüst cevap, hiçbir tek sayının güvenli olmadığıdır ve göreviniz talebi oyunlaştırmaya direnen küçük dengeli bir kümeye yeniden şekillendirmektir. Zaten raporladığınız metrikleri getirin ve her biri için "zeki, alaycı bir takım bunu daha iyi iş yapmadan nasıl şişirirdi?" diye sorun. Cevap kolaysa, metrik bir hedef haline geldiği anda tehlikelidir. Bunun yerine ne sunacağınızı ve liderliğe tek bir sayının onları yanlış şeyi optimize etmeye nasıl yanıltacağını nasıl açıklayacağınızı tartışın. O konuşmanın kalitesi, ölçümün size yardım edip etmeyeceğini ya da sizi bozup bozmayacağını öngörür.

2. **En yavaş geri bildirim döngünüz nedir ve size her gün neye mal oluyor?** Geri bildirim döngüleri verimliliğin sessizce sızdığı yerlerdir: on beş dakikalık bir derleme, iki günlük bir inceleme beklemesi, her yeşil kontrole güveni aşındıran kararsız bir test seti. Bir geliştirici deneyimi anketinden ve hat araçlarınızdan gerçek sayılar getirin ve algılanan acı ile ölçülen gecikmenin örtüşüp örtüşmediğine bakın. Günlük maliyeti, beklemeyi ona çarpan geliştirici sayısı ve ne sıklıkla çarptıkları ile çarparak tahmin edin; yatırım gerekçesi genellikle kendini kurar. Önce hangi döngüyü kısaltacağınıza ve düzeltmenin kime ait olduğuna karar verin. En yavaş döngüsünü adlandıramayan bir takım, en çok önemli olan şeyi ölçmeye henüz başlamamıştır.

3. **Ölçümünüz nerede gözetim gibi hissettirme riski taşıyor ve bunu nasıl önleyeceksiniz?** Sistemi ölçmek ile insanları izlemek arasındaki fark güven ile korku arasındaki farktır ve fark edilmeden aşılması kolaydır. Her panoyu ve raporu gözden geçirin ve herhangi birinin bir bireyi sıralayıp sıralayamayacağını ya da bir performans değerlendirmesini besleyip beslemeyeceğini sorun. Neyin toplanmış, neyin anonim ve neyin sınır dışı kaldığına açıkça karar verin, sonra bunu ölçülen takımlara açıkça söyleyin. Gözetim ve denetim baskısının güçlü olduğu kurumsal ve kamu ortamlarında bireylere inme dürtüsü sürekli olduğundan, korkuluk bir umut değil, belirtilmiş bir ilke olmalıdır. Geliştiriciler sayıların kendilerine karşı kullanıldığına inanırlarsa sayıları optimize ederler ve gerçek kaybolur.

4. **Geliştiricilere işin nasıl hissettirdiğini en son sorduğumuzda bunun sonucunda ne değişti ve onlar bunu hiç öğrendi mi?** Görünür bir eylem üretmeyen bir anket, geliştiricilere dürüstçe cevap vermeyi bırakmayı öğretir; bu yüzden ikinci sessiz anket birincisinden daha az ve daha soluk yanıt çeker ve güvendiğiniz araç, ölçeklediğiniz anda çürür. Büyük bir kuruluş için israf bileşir: yüzlerce kişi sürtünmeyi bildirmek için zaman harcar, bir rapor dolaşır ve hiçbir şey yayımlanmaz. Son anketin ilk üç bulgusunu, her birinin tetiklediği somut işi ve sonucu onu dile getiren insanlara nasıl ilettiğinizi getirin. En yüksek sesli şikayetle hareket etmek ile en yaygın olanla hareket etmek arasındaki karşıt çekimi tartın, çünkü bunlar çoğu zaman farklı sorunlardır. Anket yorgunluğu ve istişare aşırı yükünün zaten yüksek olduğu kurumsal ve kamu ortamlarında döngüyü kapatmayı bir yönetişim taahhüdü olarak ele alın: yanıtın kime ait olduğunu adlandırın, neyin değiştiğini yayımlayın ve cevaplanmamış bir anketin hiç olmamasından kötü olduğunu kabul edin.

5. **Dürüstlüğü cezalandıran bir liderlik tablosu kurmadan takımları nasıl karşılaştırırız?** Büyük kuruluşların liderleri doğal olarak hangi takımların gelişip hangilerinin sıkıştığını bilmek ister; ancak takımları ham hıza, dağıtım sıklığına ya da DORA sayılarına göre sıralamak, ağır düzenleme altındaki bir ödeme takımı ile sıfırdan bir prototip takımının farklı dünyalarda yaşadığını görmezden gelir. Karşıt değerlendirme gerçektir: sorunlu takımları fark etmeniz ve işe yarayanı yaymanız gerekir, ama karşılaştırma bir skor tablosuna dönüştüğü anda takımlar tahminleri yeniden ölçekler, olayları gizler ve konumlarını korumak için dağıtımları böler. Kuruluşunuzda takım bağlamlarının nasıl farklılaştığına dair belirli örnekler getirin, ayrıca her takımı komşularına değil zaman içinde kendi gidişatına karşılaştırma önerisiyle. Gözetim ve denetim baskısının takımlar arası sıralamaya güçlü biçimde ittiği kurumsal ve kamu ortamlarında, neyin karşılaştırılabileceği, neyin yalnızca takım başına bir eğilim olarak okunacağı ve haksız bir karşılaştırmayı reddetmeye kimin yetkili olduğu üzerinde önceden anlaşın.

6. **Bir teslimat metriğini bozan bir hedefe çevirmeden etkinliği gerçek çıktılara nasıl bağlarız?** Değere hiç bağlanmayan etkinlik liderliğe göbek bakmak gibi görünür, ama bekleme süresi ya da dağıtım sıklığı gibi bir teslimat sinyali bir performans değerlendirmesinde hedef olduğu anda takımlar sayıyı optimize eder ve vekillik etmesi amaçlanan çıktıyı terk eder. Büyük bir kuruluş için gerilim şiddetlidir, çünkü yöneticiler mühendislik çabasından iş sonuçlarına temiz bir çizgi ister, oysa dürüst çizgi dağınık ve gecikmelidir. Mevcut çıktı ölçülerinizi, onlara bağlayacağınız teslimat sinyallerini ve her birinin hedef haline gelirse nasıl oyunlaştırılabileceğine dair açık bir hesabı getirin. Liderliğin yeniden anlatabileceği basit bir hikaye ile bozulmaya direnen doğru bir tablo arasındaki çekimi tartın. Geliri anlamaya çapa olmayan bir kamu ya da piyasa dışı dahili platformda, çıktıları ham faaliyet yerine hizmet güvenilirliği, düzeltmelerde döngü süresi ve kamu yararı olarak tanımlamaya ve bu seçimi daha kolay sayılan eserleri tercih edebilecek gözetim organlarına karşı savunmaya hazır olun.

## Sektör merceği

**Girişim.** Bir avuç mühendis ve az pistle panoları tümüyle atlayın ve en hızlı hareket eden iki şeyi ölçün: on sorulu bir geliştirici deneyimi anketi ve temel hat zamanlamaları. En büyük verimlilik riskiniz yavaş ya da kararsız bir test seti ve sürekli bağlam değiştirmedir; bu yüzden en kötü geri bildirim döngüsünü bulun, kısaltın ve devam edin. Yürütecek kimsenizin olmadığı bir ölçüm programı kurmayın, çünkü günün nereden sızdığı hakkında tek bir dürüst konuşma, sonra sürdürmek zorunda kalacağınız herhangi bir araçtan daha iyidir.

**Küçük işletme.** Ölçüm uzmanı olmadan ve sıkı bir bütçeyle, mevcut araçlarınızın zaten kaydettiğine yaslanın: zaten ödediğiniz sistemlerden derleme süreleri, inceleme gecikmesi ve olay sayıları. Bir tane inşa etmek yerine hafif bir anket aracı satın alın ve harcayamayacağınız güveni size mal edecek bireysel verimlilik panosu için tedarikçi teklifine direnin. Tüm çabayı, kimsenin gününü boşa harcamayı karşılayamayacak küçük bir takım için sürtünmeyi kaldırma olarak çerçeveleyin.

**Kurumsal.** Onlarca takım arasında ödül, ölçekte geri kazanılan kapasitedir ve tehlike, sessizce insanları sıralamaya kayan merkezi bir panodur. Dengeli bir programı standartlaştırın (üç ayda bir DevEx anketi, birkaç SPACE boyutu ve takım başına bir teslimat eğilimi olarak okunan DORA) ve onu bireysel telemetrinin asla toplanmayacağı şekilde yönetin. Her takımı kendi gidişatına karşılaştırın, platform yatırımını (bölüm 8.4) verinin ortaya çıkardığı sürtünmeye karşı haklı çıkarın ve bir liderlik tablosu olacak herhangi bir metriği reddetme yetkisini tek bir sorumlu sahibe verin.

**Kamu.** Çıktıda piyasa fiyatı olmadan ve güçlü gözetim baskısıyla çıktı tiyatrosuna (belgeleri ve kapatılan biletleri saymaya) çekim sürekli ve denetim altında adı konmuş bireyleri gözetlemeye çekim daha da güçlüdür. Bunun yerine çıktıları ve teslimat yeteneğini ölçün: bir hizmetin bir düzeltmeyi ne kadar hızlı yayımladığı, ne kadar güvenilir olduğu ve personel ile yüklenicilerin işi anonim bir anket aracılığıyla nasıl deneyimlediği. Memurları ve yüklenicileri aynı sistem düzeyi temelde ölçün, ölçümün ne için olduğunu yayımlayın ve bir yasama organına, takım başına bir teslimat eğiliminin herhangi bir bireysel puandan kamu değerinin daha dürüst bir okuması olduğunu savunmaya hazır olun.

## Örnekler

**Girişim.** Yirmi kişilik bir girişim herkes meşgulken yayımlamanın yavaşladığını fark eder. Bir verimlilik panosu kurmak yerine mühendislik lideri on sorulu bir DevEx anketi yürütür ve temel hat zamanlamalarını çeker. Anket ve veri aynı fikirdedir: test seti yirmi iki dakika sürer ve rastgele başarısız olur; bu yüzden insanlar değişiklikleri toplu hale getirir ve beklerken bağlam değiştirir. Takım iki hafta kararsız testleri düzeltmeye ve seti paralelleştirmeye harcar ve onu dört dakikaya indirir. Dağıtım sıklığı kendiliğinden yükselir, memnuniyet bir sonraki ankette sıçrar ve bunun gerçekleşmesi için kimse hiç sıralanmadı ya da puanlanmadı.

**Kurumsal.** Kırk mühendislik takımı olan bir banka dahili platformuna sürekli yatırımı haklı çıkarmak ister. Platform grubu dengeli bir ölçüm programı benimser: tüm takımlar genelinde üç ayda bir DevEx anketi, SPACE tarzı sinyaller ve takım düzeyinde bir teslimat sağlığı eğilimi olarak okunan DORA metrikleri (bölüm 11.5). Önemlisi, takımları birbirlerine değil, zaman içinde kendi gidişatlarına karşılaştırarak adil biçimde kıyaslarlar, çünkü takım bağlamları çılgınca farklıdır. Veri, asfalt yollardaki (bölüm 8.4) takımların yeni mühendisleri haftalar yerine günler içinde uyumlandırdığını ve çok daha düşük bilişsel yük bildirdiğini gösterir. Yüzlerce geliştirici boyunca geri kazanılan kapasite olarak çerçevelenen bu kanıt, platformu bir yıl daha finanse eder. Bireysel telemetri bilerek asla toplanmaz.

**Kamu.** Federal bir dijital hizmetler kurumu, çıktıda piyasa fiyatı olmayan bir ortamda mühendislik harcamasının değer sunduğunu bir yasama organına göstermek zorundadır. Çıktı tiyatrosunu (belgeleri ya da kapatılan biletleri saymayı) reddeder ve bunun yerine çıktıları ve teslimat yeteneğini ölçer: hizmetlerin bir düzeltmeyi ne kadar hızlı yayımlayabildiği, ne kadar güvenilir oldukları ve iş gücü ile yüklenicilerinin işi anonim bir anket aracılığıyla nasıl deneyimlediği. DORA tarzı teslimat sinyalleri, modernizasyonun gerçekten verimi ve istikrarı iyileştirip iyileştirmediğini gösterir; ham faaliyet yerine kamusal çıktılara geri bağlanır (bölüm 11.5). Ölçüm asla bireyleri sıralamadığı ve yüklenici ile memur personeli aynı sistem düzeyi temelde ölçüldüğü için kurum, bu tür çabaları batıran gözetim ve moral sorunlarından kaçınır ve gözetim organlarına değer üzerine dürüst bir okuma verir.

## İş gerekçesi: motivasyonlar, YG ve TSM

Etkinliği ölçmenin ve iyileştirmenin getirisi geri kazanılan kapasitedir ve ölçekte sayılar büyüktür. Küçük sürtünmeler büyük bir kuruluşta çarpılır: yüz mühendisin günde birkaç kez çarptığı on dakikalık bir derleme, yılda beklemekle geçen binlerce mühendis saatidir. O döngüyü kısaltın ve kimseyi işe almadan anlamlı kapasite eklemiş olursunuz. Buradaki baskın YG, platform mühendisliğindekiyle aynıdır (bölüm 8.4): pahalı mühendislik zamanının beklemeden ve angaryadan değerli işe yönlendirilmesi.

Toplam sahip olma maliyeti mütevazı ama gerçektir. Anket araçları ve onu yürütme disiplini için, hatları araçlandırmak için ve eğilimleri okuyup harekete geçmek için yönetim dikkati için ödersiniz. YG için daha büyük risk ölçümü kötü yapmaktır. Tek bir oyunlaştırılmış metrik ya da bir gözetim programı negatif getiriler üretebilir: gerçek çıktılar durağan kalırken bir sayıyı optimize etmek için aylarca çaba, artı her gelecek değişikliği daha zor yapan güven aşınması. Hiç ölçmemenin maliyeti dağınık ve muazzamdır: sürtünme ve angarya görünmez biçimde birikir, kıdemli mühendisler kaçınılabilir israfta tükenir ve liderlik yatırımların yardımcı olup olmadığını söyleyemez. Gerekçeyi liderliğe kaldıraç ve dürüstlük olarak sunun: büyük bir iş gücünün zamanı nerede kaybettiğini bulan ve ilk bulguyla hareket ettiğiniz anda kendini kat kat ödeyen küçük, güvenilir, dengeli bir ölçüm programı.

## Anti-kalıplar ve tuzaklar

- **Tek verimlilik metriği.** Herhangi bir tek sayı (LOC, hız, commit'ler, saatler) hedef olduğu gün oyunlaştırılır.
- **Bireyleri sıralamak.** Liderlik tabloları ve bireysel "verimlilik puanları" güveni yok eder ve insanlara metriği optimize etmeyi öğretir.
- **Gözetim olarak ölçüm.** Değerlendirmeleri besleyen ayrıntılı bireysel telemetri, etkili işin ihtiyaç duyduğu psikolojik güvenliği aşındırır.
- **Takipsiz anketler.** Geliştiricilere işin nasıl hissettirdiğini sorup hiçbir şeyi değiştirmemek, onlara dürüstçe cevap vermeyi bırakmayı öğretir.
- **Takımların ham sayılarını karşılaştırmak.** Takım bağlamları farklıdır; takımlar arası hız ya da DORA karşılaştırmaları dürüstlüğü cezalandırır ve oyunlaştırmayı ödüllendirir.
- **Çıktı tiyatrosu.** Gerçek çıktılar ölçülmezken üretilen eserleri (belgeler, biletler, yayımlanan özellikler) saymak; piyasa fiyatının olmadığı yerde yaygın.
- **Performans değerlendirmesinde DORA.** Teslimat metrikleri insanları puanladığı anda takımlar olayları gizler ve dağıtımları böler ve sinyal ölür.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Verimlilik sezgiyle ya da kod satırları, hız ya da saatler gibi tek oyunlaştırılabilir bir metrikle yargılanır. Ölçüm gelişigüzel ve reaktiftir, sürtünme görünmezdir, şikayetler anekdotsaldır ve kimse kuruluşun iyileşip iyileşmediğini söyleyemez.
- **Düzey 2, Geliştirme:** Bazı takımlar temel uygulamalar benimser: birkaç metrik, çoğu zaman faaliyet sayıları ve ara sıra geliştirici deneyimi anketi. Uygulamalar takımdan takıma tutarsızdır, veri toplanır ama nadiren harekete geçilir, ham takımlar arası karşılaştırmalar sızar ve bireyleri sıralamadan koruyan paylaşılan bir ilke yoktur.
- **Düzey 3, Standartlaştırma:** Dengeli bir ölçüm programı belgelenir ve kuruluş genelinde uygulanır; SPACE tarzı boyutlar, düzenli bir DevEx anketi ve bir teslimat sinyali olarak DORA kullanır (bölüm 11.5). Metrikler politika gereği takımlara toplanır, bireyler asla sıralanmaz ve bulgular geri bildirim döngülerini kısaltmak ve angaryayı azaltmak için somut işi yönlendirir (bölüm 9.1).
- **Düzey 4, Yönetme:** Program temel çizgilere karşı ölçülür ve kontrol edilir. Geri bildirim döngüsü süreleri, anket puanları ve DORA eğilimleri üzerinde anlaşılmış hedefler taşır ve zaman içinde izlenir; her takım komşularına değil kendi gidişatına karşılaştırılır; platform ve angarayı azaltma yatırımları geri kazanılan kapasiteye dair öncesi-sonrası verilerle haklı çıkarılır ve herhangi bir sinyaldeki gerileme fark edilmeden geçmek yerine bir incelemeyi tetikler.
- **Düzey 5, Orkestrasyon:** Ölçüm güvenilir, rutin ve uyarlanabilirdir. Algısal ve sistem verisi üçgenlenir, eğilimler sürekli iyileştirmeyi besler, sürtünme ve bilişsel yük aktif olarak aranıp kaldırılır, ölçüm kümesinin kendisi kuruluş değiştikçe gözden geçirilir ve etkinlik, hiçbir metriğin bozan bir hedef haline gelmesine izin verilmeden iş ve kamu çıktılarıyla bütünleşir.

## Tartışma fikirleri

1. Mevcut metriklerinizden hangileri zeki bir takım tarafından daha iyi iş yapmadan şişirilebilir ve onları neyle değiştirirdiniz?
2. Tüm kuruluşta tam olarak bir geri bildirim döngüsünü kısaltabilseydiniz, hangisi en çok geri kazanılan kapasiteyi döndürürdü?
3. Bağlamları farklıyken birçok takımı dürüstlüğü cezalandıran bir liderlik tablosu yaratmadan adil biçimde nasıl kıyaslarsınız?
4. Sistemi ölçmek ile bireyi gözetlemek arasındaki çizgi nerede ve kuruluşunuzda bunu uygulamaya kim yetkili?
5. Kamu ya da dahili bir platform gibi çıktıda piyasa fiyatı olmayan bir ortamda, faaliyet yerine gerçek değeri nasıl ölçersiniz?
6. Bu çeyreğin anketinin bir şeyi değiştirdiğini kanıtlamak için bir geliştiriciye ne gösterirdiniz?

## Önemli çıkarımlar

- Mühendisler için verimlilik çok boyutludur. Herhangi bir tek sayıyı (kod satırları, hız, commit'ler, saatler) *ölçü* olarak reddedin, çünkü Goodhart yasası onun oyunlaştırılacağını garanti eder.
- Hiçbir boyutun tek başına oyunlaştırılamaması için birkaç boyutu bir arada tutmak üzere **SPACE çerçevesini** (memnuniyet ve iyi oluş, performans, faaliyet, iletişim ve iş birliği, verimlilik ve akış) kullanın.
- **Geliştirici deneyimi** geri bildirim döngülerine, bilişsel yüke ve akışa iner. Döngüleri kısaltmak ve yükü kaldırmak, faaliyet sayılarının asla göstermediği gerçek verimliliktir.
- Bir DevEx anketinden gelen algısal veriyi araçlarınızdan gelen sistem verisiyle **üçgenleyin**; her biri diğerini düzeltir.
- **DORA** metriklerini bir liderlik tablosu değil, takım düzeyinde bir teslimat sinyali olarak ele alın; derinlikleri bölüm 11.5'te, hat ise bölüm 11.2'dedir.
- **Sistemi** ölçün, bireyi asla. Takımlara toplayın, değerlendirmeyi bölüm 1.3'ün ayrı insani kanallarında tutun ve ölçümün gözetime dönüşmesine asla izin vermeyin.
- Geri kazanılan zamanı angaryayı kesmeye (bölüm 9.1), kod incelemesini hızlandırmaya (bölüm 2.5) ve yolları asfaltlamaya (bölüm 8.4) harcayın. Etkinliği, hiçbir metriğin bozan bir hedef haline gelmesine izin vermeden iş çıktılarına bağlayın.

## Kaynaklar ve ileri okuma

- Nicole Forsgren, Margaret-Anne Storey, Chandra Maddila, Thomas Zimmermann, Brian Houck, and Jenna Butler, "The SPACE of Developer Productivity" (*ACM Queue*, 2021): the multidimensional framework.
- Abi Noda, Margaret-Anne Storey, Nicole Forsgren, and Michaela Greiler, "DevEx: What Actually Drives Productivity" (*ACM Queue*, 2023): feedback loops, cognitive load, and flow.
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps* (the DORA metrics and their research basis).
- DORA, *Accelerate State of DevOps Report* (annual): the ongoing research programme behind the four metrics.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy, eds., *Site Reliability Engineering* (toil and its elimination).
- Matthew Skelton and Manuel Pais, *Team Topologies* (cognitive load as a first-class design concern).
- Mihaly Csikszentmihalyi, *Flow: The Psychology of Optimal Experience* (the origin of flow state).
- Tom DeMarco and Timothy Lister, *Peopleware: Productive Projects and Teams* (focus, interruption, and the human side of productivity).
- Goodhart, C. A. E., "Problems of Monetary Management: The UK Experience" (1975): the origin of Goodhart's law; see also Marilyn Strathern's widely quoted formulation.
- U.S. Government Accountability Office (GAO) guidance on performance measurement: measuring value in non-market public-sector settings.
