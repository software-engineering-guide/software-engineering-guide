# 5.3 Erişilebilirlik

## Genel bakış ve motivasyon

[Erişilebilirlik](https://en.wikipedia.org/wiki/Accessibility) (çoğu zaman "a11y" diye kısaltılır), engelli insanların algılayabileceği, anlayabileceği, içinde gezinebileceği ve kullanabileceği yazılım inşa etme uygulamasıdır. Buna görme engelli ya da az gören, sağır ya da işitme güçlüğü olan, motor yetersizliği olan, bilişsel ya da öğrenme farklılıkları olan insanlar ve kırık bir kol, parlak güneş ışığı ya da gürültülü bir oda gibi geçici ya da durumsal sınırlarla karşılaşanlar dahildir. Yaklaşık beş kişiden birinin bir engeli vardır ve herkes erişilebilir tasarımdan bir noktada yararlanır. Bu, dar bir kesime yönelik bir uyarlama değildir. Bir kalite tabanıdır.

Büyük takımlar için erişilebilirlik bireylerin iyi niyetine bırakılmamalı, sisteme yerleştirilmelidir. Birçok takım tek bir ürüne yazılım sevk ettiğinde, tek bir erişilemez bileşen (etiketsiz bir form alanı, yalnızca renkle gösterilen bir durum göstergesi, bir kipteki klavye tuzağı) engelli kullanıcıları bütün bir yolculuğun dışında bırakabilir. Erişilebilirliği ortak bileşenlere, tasarım belirteçlerine, test hatlarına ve bitti tanımlarına yerleştirmek, onu ölçekte güvenilir kılmanın tek yoludur. Sonradan eklemek pahalı ve hataya açıktır. Baştan tasarlamak ucuz ve kalıcıdır.

Kamu için erişilebilirlik yasal bir gereklilik ve bir yurttaşlık yükümlülüğüdür, olsa da olur bir şey değil. Kamu hizmetleri, kamunun her üyesine hizmet etmelidir ve engelli vatandaşların çoğu zaman başka sağlayıcısı yoktur: devletin web sitesi erişilemezse, yardımlarını, ruhsatlarını alamaz ya da başka bir yolla oy kullanamazlar. Dünyanın dört bir yanındaki yasalar ve standartlar erişilebilirliği kamu kurumları için, giderek özel sektör için de zorunlu kılar. Bu bölüm erişilebilirliği aynı anda üç şey olarak ele alır: yasal bir görev, etik bir görev ve sadece iyi tasarım.

*Ayrıca bakınız:* bölüm 5.2 (arayüz tasarımı ve tasarım sistemleri), bölüm 5.6 (ön yüz mühendisliği) ve bölüm 5.1 (kullanıcı deneyimi temelleri).

## Temel ilkeler

- Erişilebilirlik, güvenlik ve performans gibi bir temel kalite niteliğidir, isteğe bağlı bir özellik değil.
- POUR ilkeleri: arayüzler Algılanabilir (Perceivable), Kullanılabilir (Operable), Anlaşılabilir (Understandable) ve Sağlam (Robust) olmalıdır.
- Önce [anlamsal HTML](https://en.wikipedia.org/wiki/Semantic_HTML); [ARIA](https://en.wikipedia.org/wiki/WAI-ARIA)'yı yalnızca gerçek boşlukları doldurmak için kullanın, yerel öğelerin yerine asla.
- Fareyle kullanılabilen her şey yalnızca klavyeyle de kullanılabilmelidir.
- Bilgiyi yalnızca renkle, biçimle ya da konumla aktarmayın.
- Otomatik araçlar sorunların yalnızca bir bölümünü yakalar; elle ve [yardımcı teknoloji](https://en.wikipedia.org/wiki/Assistive_technology) testi şarttır.
- Erişilebilir tasarım herkes için daha iyi tasarımdır (["kaldırım rampası etkisi"](https://en.wikipedia.org/wiki/Curb_cut): engelliler için yapılmış özelliklerin tüm kullanıcılara yarar sağlaması).
- Engelli insanlar için değil, onlarla birlikte tasarlayın ve test edin.

## Öneriler

### WCAG'a göre tasarlayın ve inşa edin, güncel standardı hedefleyin

[Web İçeriği Erişilebilirlik Yönergeleri](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG), uluslararası referanstır. WCAG 2.1 ve 2.2, A, AA ve AAA uyum düzeylerinde test edilebilir başarı ölçütleriyle dört POUR ilkesi altında düzenlenmiştir. Taban olarak AA düzeyini hedefleyin; çoğu yasanın atıf yaptığı budur. WCAG 2.2, odak görünürlüğü, hedef boyutu ve bilişsel yükün azaltılması için ölçütler ekler. WCAG 3.0, farklı yapılandırılmış ve hâlâ geliştirilmekte olan ortaya çıkan bir halefidir. Onu izleyin ama bugün 2.2 AA'ya göre inşa edin. Yönergeleri bir tavan değil bir taban olarak görün: her ölçütü geçmek gerçekten kullanılabilir bir deneyimi garanti etmez.

### Anlamsal HTML ve doğru ARIA kullanın

Yerel HTML öğeleri (düğmeler, bağlantılar, form denetimleri, başlıklar, listeler, yer işaretleri) yerleşik erişilebilirlik anlamsallığı, klavye davranışı ve yardımcı teknoloji desteğiyle gelir. Önce onları kullanın. ARIA (Erişilebilir Zengin İnternet Uygulamaları) rollerine, durumlarına ve özelliklerine yalnızca HTML'in ifade edemediği özel öğeleri tanımlamak için başvurun ve ARIA Yazım Uygulamalarını izleyin. ARIA'nın ilk kuralı basittir: yerel bir öğe işi görecekse ARIA kullanmayın. Yanlış ARIA, hiç olmamasından kötüdür: [ekran okuyucuları](https://en.wikipedia.org/wiki/Screen_reader) aktif olarak yanıltır. Sayfaya mantıklı bir başlık yapısı, anlamlı etiketler, görseller için alternatif metin, medya için altyazılar ve dökümler ve her etiket ile denetimi arasında programatik bir bağlantı verin.

### Klavye ve yardımcı teknoloji ile kullanılabilirliği garanti edin

Her etkileşimli öğeye yalnızca klavyeyle, mantıklı bir sırayla ve açıkça görünür bir odak göstergesiyle ulaşılabilmeli ve onu kullanmak mümkün olmalıdır. Klavye tuzaklarından kaçının. İçerik değiştiğinde odağı bilinçli yönetin: bir diyalog açıldığında odağı oraya taşıyın, kapandığında geri verin ve dinamik güncellemeleri canlı bölgeler (live region) aracılığıyla duyurun. Masaüstünde ve mobilde ekran okuyucular, ekran büyütme, sesli denetim ve anahtar erişimi dahil gerçek yardımcı teknolojilerle test edin. Ve azaltılmış hareket ve artırılmış kontrast gibi kullanıcı tercihlerine saygı gösterin.

### Otomatik araçlarla, elle incelemeyle ve gerçek kullanıcılarla test edin

Otomatik erişilebilirlik tarayıcıları değerlidir ve her değişiklikte hatta çalışmalıdır. Ancak çalışmalar, gerçek sorunların yalnızca azınlığını, kabaca üçte birini yakaladıklarını tutarlı biçimde gösterir. Gerisi insan yargısı ister: klavye turları, ekran okuyucu testi, kontrast denetimleri ve içeriğin gerçekten anlaşılır olup olmadığını sormak. Hepsinden önemlisi, engelli insanları kullanılabilirlik testlerine dahil edin. Erişilebilirlik kabul ölçütlerini bitti tanımına yerleştirin, böylece sorunlar lansman öncesi bir denetimde değil, hikâye başına yakalanır.

### Erişilebilirliği kahramanlıkla değil, kurumsal olarak yürütün

Erişilebilirliği tasarım sistemine yerleştirin ki bileşenler varsayılan olarak erişilebilir sevk edilsin. Tasarımcıların, mühendislerin, içerik yazarlarının ve ürün yöneticilerinin her birinin neden sorumlu olduğunu bilmesi için eğitim sunun. Bir erişilebilirlik standardı, bir sahip ya da mükemmeliyet merkezi ve bir düzeltme süreci belirleyin. Bir erişilebilirlik beyanı yayımlayın ve kullanıcılara engelleri bildirecek bir yol verin. Ve erişilebilir biçimde satın alın: tedarikçilerden ve üçüncü taraf bileşenlerden uyum sağlamalarını ve kanıt (erişilebilirlik uyum raporu gibi) sunmalarını isteyin.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
|---|---|---|
| Erişilebilirliği baştan içine inşa etmek | En ucuz, kalıcı, herkes için daha iyi | Başlangıçta eğitim ve disiplin gerektirir |
| Sonradan uyarlamak / düzeltmek | Emeği erteler, hızlı lansmanın önünü açar | Çok daha pahalı, kırılgan, bu arada yasal risk |
| Yalnızca otomatik test | Hızlı, ucuz, CI'da gerilemeleri yakalar | Sorunların yaklaşık üçte ikisini kaçırır; yanlış güven |
| Elle + yardımcı teknoloji testi | Gerçek kullanılabilirlik engellerini yakalar | Daha yavaş, yetkin test uzmanları ve cihazlar gerektirir |
| Engelli kullanıcılarla test | Gerçek deneyim hakkında temel gerçek | Katılımcı bulma çabası ve maliyeti, saygılı yapılmalı |

Temel ödünleşim, baştan disiplin ile ertelenmiş maliyet arasındadır. İçine inşa edilmiş erişilebilirlik ucuzdur ve herkes için kaliteyi artırır; yasal baskı altında sonradan uyarlanan erişilebilirlik pahalı, eksik ve stresli olur. Uzun vadede "hız" ile gerçek bir ödünleşim yoktur: erişilemez yazılım, kullanıcılarınızın beşte biri için basitçe çalışmaz. Bu bir tasarruf değil, bir kusurdur.

## Takımınızla tartışılacak sorular

1. **Erişilebilirlik gerilemeleri, bozuk bir test gibi derlememizi (build) başarısız kılıyor mu, kılmıyorsa neden?** Otomatik tarayıcılar sorunların yalnızca üçte birini yakalar, ama yakaladıkları (eksik etiketler, kontrast hataları, etiketsiz denetimler) CI'da yakalaması ucuz, lansman öncesi bir denetimde bulması pahalı olanlardır. Bir gerilemeyi derleme başarısızlığı saymak, erişilebilirliği kahramanca bireysel emekten güvenilir bir sistem özelliğine taşıyan şeydir; birçok takım tek bir ürüne sevk ettiğinde işe yarayan tek şey de budur. Hangi denetimlerin engelleyici, hangilerinin tavsiye niteliğinde olduğuna ve bir başarısızlığı kimin geçersiz kılabileceğine karar verin. Toplantıya güncel tarayıcı sonuçlarınızı ve bitti tanımınızı getirin. Erişilebilirlik ölçütleri hikâye başına bitti tanımına yazılmamışsa, bir son tarih sıkıştığı anda öncelikleri düşecektir.

2. **Özel öğeler için kuralımız nedir ve ARIA sevk edilmeden önce kim inceler?** Yerel HTML öğeleri klavye davranışı ve yardımcı teknoloji desteğiyle bedavaya gelir ve yanlış ARIA hiç olmamasından kötüdür, çünkü ekran okuyucuları aktif olarak yanıltır. Anlamsal HTML'in varsayılan olduğu ve her özel öğenin (özel bir açılır liste, tarih seçici ya da kip) birleştirmeden önce ARIA Yazım Uygulamalarını izleyen bir klavye ve ekran okuyucu turu gerektirdiği konusunda uzlaşın. Bu, en çok birçok takımın yeniden kullandığı etkileşimli bileşenler için önemlidir, çünkü klavye tuzağı olan tek bir bozuk kip, engelli kullanıcıları bütün bir yolculuktan dışlayabilir. Özel öğelerinizin bir listesini getirin ve hangilerinin gerçek bir ekran okuyucuyla test edildiğini sorun. Test edilmemiş olanlar, paylaşılan kodda saklanan yüklerdir.

3. **Erişilebilirlik yer paylaşımları (overlay) konusundaki politikamız nedir ve bunların gerçek bir çözüm olduğuna inanan var mı?** Yer paylaşımları, bir siteyi uyumlu yapan tek satırlık bir betik olarak pazarlanır ve yasal baskı geldiğinde ve bir son tarih yaklaştığında cazip görünür. Gerçek uyumu sağlamazlar, yardımcı teknoloji kullanıcıları için deneyimi kötüleştirebilirler ve kamu açısından temeldeki yasal görevi karşılanmamış bırakırlar. Sorunun üstünü örten bir bileşen satın almak yerine anlamsal işaretlemeye, klavye desteğine ve engelli insanlarla teste yatırım yapacağınıza açıkça karar verin. Bir yer paylaşımı aboneliğinin maliyetini getirin ve erişilebilirliği bileşenlerinize ve hattınıza bir kez inşa etmenin maliyetiyle karşılaştırın. Bunu erken çerçevelemek, daha sonra para harcayıp hiçbir şeyi düzeltmeyen panik halinde bir tedarik kararını önler.

4. **Engelli insanlar tasarımımızın ve testimizin parçası mı, yoksa hâlâ kendi icat ettiğimiz hayali bir kullanıcı için mi tasarlıyoruz?** Otomatik tarayıcılar ve hatta uzman denetimleri size işaretlemenin uyumlu olup olmadığını söyler; görme engelli bir kullanıcının ödemenizi gerçekten tamamlayıp tamamlayamayacağını ya da bilişsel engeli olan bir kişinin hata iletilerinizi anlayıp anlayamayacağını söylemez. Engelli katılımcıları dahil etmek tek temel gerçek kaynağıdır ve ne inşa ettiğinizi değiştirir, ama katılımcıları nasıl adil biçimde bulacağınız, zamanları için onlara nasıl ödeme yapacağınız ve tek bir katılımcıyı her engelin sözcüsü saymaktan nasıl kaçınacağınız konusunda gerçek sorular doğurur. Güncel araştırma listenizi, katılımcı bulma ve ödeme uygulamalarınızı ve son yılda kaç çalışmanın engelli katılımcıları içerdiğinin dürüst bir sayımını getirin. Büyük bir kurum için görme, işitme, motor ve bilişsel ihtiyaçları kapsayan, adil ücretlendirilen yinelenen bir panel, bunu tek seferlik bir jestten güvenilir bir girdiye dönüştürür; kamuda hizmet ettiğiniz topluma katılım çoğu zaman isteğe bağlı bir nezaket değil, yasal ve yurttaşlık yükümlülüğünün bir parçasıdır.

5. **Üçüncü taraf bir bileşen satın aldığımızda ya da gömdüğümüzde erişilebilirlik kanıtı istiyor muyuz ve kim denetliyor?** Büyük bir ürünün içinde sevk edilenin çoğu şirket içinde yazılmaz: bir kütüphaneden gelen tarih seçici, bir iframe içindeki ödeme bileşeni, bir grafik paketi, koca bir SaaS modülü. Tek bir erişilemez gömülü bileşen, kendi kodunuz ne kadar temiz olursa olsun bütün bir yolculuğu başarısız kılabilir ve bir kez bağlandıktan sonra onu değiştirmek pahalıdır. Erişilebilirliğin bir tedarik gereksinimi olduğuna, tedarikçilerin bir erişilebilirlik uyum raporu (bir ürünün WCAG'a karşı nasıl ölçüldüğünü belirten VPAT gibi bir belge) sunması gerektiğine ve birinin iddiayı dosyalamak yerine teknik olarak doğrulaması gerektiğine karar verin. Üçüncü taraf bileşenlerinizin envanterini getirin ve hangilerinin güncel, inandırıcı uyum kanıtına sahip olduğunu sorun. Kurumsal ve kamu satın almasında, WCAG 2.2 AA uyumunu ve düzeltme hakkını sözleşmeye yazın; çünkü imzadan önce verilen bir söz, canlıya geçişten sonra keşfedilen bir engelden çok daha ucuza uygulatılır.

6. **Hedef uyum düzeyimiz nedir, sahibi kim ve standartlar değiştikçe bunu nasıl güncel tutarız?** WCAG 2.2 AA bugünün tabanıdır ve çoğu yasa ona atıf yapar, ama 2.2 birçok takımın benimsemediği ölçütler ekledi ve WCAG 3.0 farklı bir yapıyla geliyor. Adı konmuş bir sahip olmadan standart sürüklenir: farklı takımlar farklı sürümleri hedefler, kimse farkı izlemez ve uyum denetimler arasında sessizce çürür. İnşa ettiğiniz tam sürüme ve düzeye, onu yükseltme yetkisinin kimde olduğuna ve yeni ölçütlerin tasarım sistemine ve bitti tanımına nasıl ulaştığına karar verin. Güncel beyan edilmiş hedefinizi, takımların onu gerçekte nerede karşıladığının kanıtını ve atladığınız 2.2 ölçütlerini benimsemek için kısa bir yol haritasını getirin. Büyük ya da kamusal bir kurum için bir erişilebilirlik sahibi ya da mükemmeliyet merkezi, yayımlanmış bir erişilebilirlik beyanı ve bir sonraki standart sürümü için belgelenmiş bir plan, bir düzenleyiciye ya da bir mahkemeye iyi niyetle değil kanıtla yanıt vermenizi sağlayan şeylerdir.

## Sektör merceği

**Girişim.** Burada hız sizden yanadır, çünkü erişilebilirlik kod tabanı küçükken en ucuzdur. İlk sprintten itibaren CI'a otomatik bir tarayıcı ve çekme isteği (pull request) kontrol listenize bir klavye turu ekleyin ve klavye ile ekran okuyucu desteğini bedavaya almak için anlamsal HTML'e yaslanın. Yer paylaşımlarını ve ağır araçları atlayın; karşılığı, bir müşterinin tedarik takımı satış ortasında uyum raporu istediğinde, telaşlanmak yerine günler içinde yanıt verebilmenizdir.

**Küçük işletme.** Erişilebilirlik uzmanınız ve dar bir bütçeniz yoksa, erişilebilirliği inşa etmek yerine satın alın: zaten uyumlu olan ve bunu belirten bir platform, tema ya da bileşen kütüphanesi seçin ve erişilebilirlik beyanı yayımlayan tedarikçileri tercih edin. Yüksek değerli temelleri ücretsiz araçlarla, yalnızca klavyeyle denetimlerle, bir kontrast denetleyicisiyle ve her alanda net etiketlerle kendiniz karşılayın; çünkü müşterileri en sık dışlayan hataları bunlar yakalar. Yanlış ya da kullanılamaz bir otomatik akışı kaybedilmiş bir müşteri olarak görün, çünkü küçük bir işletme nadiren geri dönülecek yardımlı bir kanal sunar.

**Kurumsal.** Ölçekte iş, erişilebilirliği birçok takım arasında bir sistem özelliği yapmaktır. Tasarım sisteminde varsayılan olarak erişilebilir bileşenler sevk edin, gerilemeleri CI'da engelleyin ve bir düzeltme süreci ile tasarımcılar, mühendisler ve içerik yazarları için eğitimi olan bir sahip ya da mükemmeliyet merkezi kurun. Uyumu zaman içinde bir ölçüt olarak izleyin, WCAG uyumunu tedariğe yazın ve üçüncü taraf bileşenleri bir portföy olarak yönetin; böylece tek bir gömülü bileşen ortak bir yolculuğu sessizce başarısız kılamaz.

**Kamu.** Erişilebilirlik yasal bir zorunluluk ve yurttaşlık görevidir, çünkü engelli vatandaşların bir yardım, ruhsat ya da oy için çoğu zaman başka sağlayıcısı yoktur. Yargı alanınızın atıf yaptığı standarda göre inşa edin (örneğin Section 508, EN 301 549 ya da WCAG 2.2 AA'ya eşlenen Avrupa Erişilebilirlik Yasası), engelleri bildirme yolu olan bir erişilebilirlik beyanı yayımlayın ve hizmet ettiğiniz engelli toplumla test edin. Yer paylaşımlarını gerçek uyumun yerine geçen bir şey olarak reddedin ve tedarikçilerden sözleşmede inandırıcı kanıt ve düzeltme hakkı sunmalarını isteyin.

## Örnekler

**Girişim.** İşe alım aracı geliştiren üç kişilik bir girişim, erişilebilir kalmanın sonradan düzeltmekten ucuz olduğunu düşünerek, daha ilk sprintten itibaren derlemesine bir erişilebilirlik tarayıcısı ve çekme isteği kontrol listesine hızlı bir klavye turu ekledi. Orta ölçekli bir müşterinin tedarik takımı bir satış döngüsü sırasında erişilebilirlik uyum raporu istediğinde, girişim zaten anlamsal HTML kullanıyor, her alanı etiketliyor ve her yerde görünür odağa sahipti; telaşlanmak yerine günler içinde yanıt verdi. Bu hazırlık, bir rakibin aynı gereksinimde kaybettiği bir anlaşmayı kazandırdı.

**Kurumsal.** Büyük bir perakendeci, görme engelli müşteriler ekran okuyucuyla ödemeyi tamamlayamadığı için toplu davayla karşılaştı. Uzlaşma ve hukuk masraflarının ötesinde şirket, mahkeme gözetimindeki bir takvim altında düzeltme yapmak zorunda kaldı. Sonrasında erişilebilirliği tasarım sistemine ve CI hattına yeniden yerleştirdi, bitti tanımına ekran okuyucu testi ekledi ve takımlarını eğitti. Yeniden inşa edilen, erişilebilir ödeme herkes için dönüşümü artırdı ve destek taleplerini azalttı: ekran okuyucu kullanıcılarına yardım eden düzeltmeler (net etiketler, hata iletileri, mantıklı sıra) bütün kullanıcılara yardım etti.

**Kamu.** Bir kamu yardım kurumu, çevrimiçi başvurusu için yasal olarak WCAG 2.1 AA'yı karşılamak zorundaydı. Görme engelli ve az gören kullanıcılar, yalnızca klavye kullananlar ve bilişsel engeli olan kullanıcılarla yapılan erken testler, yalnızca renkle gösterilen bir "zorunlu alan" göstergesinin, erişilemez bir tarih seçicinin ve duyurulmayan doğrulama hatalarının insanların bitirmesini engellediğini ortaya çıkardı. Bunları anlamsal işaretleme, görünür odak, canlı bölge hata duyuruları ve [sade dil](https://en.wikipedia.org/wiki/Plain_language) yardımıyla düzeltmek, engelli vatandaşların ilk kez kendi başlarına başvuru yapmasını sağladı. Bu, yüz yüze yardıma bağımlılığı azalttı ve yasal zorunluluğu karşılarken hizmet maliyetini düşürdü.

## İş gerekçesi: motivasyonlar, YG ve TSM

İş gerekçesi pazar erişimine, yasal riske, hizmet maliyetine ve kaliteye dayanır. Engelli insanlar ve aileleri önemli bir satın alma gücünü elinde tutar; onları dışlamak bunu elden çıkarmaktır. Erişilebilir hizmetler, pahalı yardımlı kanallara (telefon ve yüz yüze yardım) olan ihtiyacı azaltır; bu, özellikle kamuda doğrudan bir operasyonel tasarruftur. Ve erişilebilirlik iyileştirmeleri (net etiketler, klavye desteği, okunabilir içerik, sağlam işaretleme) herkese yardım ettiği için, genel tamamlama ve memnuniyeti tipik olarak yükseltirler.

TSM açısından benimseme maliyeti eğitim, araçlar ve erişilebilirliği bileşenlere ve hatlara yerleştirmektir; baştan yapıldığında hepsi mütevazıdır. Benimsememenin maliyeti ciddidir ve birkaç yönden gelir: yasal sorumluluk (davalar, uzlaşmalar, mahkemece emredilen düzeltmeler, düzenleyici cezalar), son tarih baskısı altında sonradan uyarlamanın çok daha yüksek masrafı, itibar zararı ve dışlanan kullanıcılara daha pahalı kanallarla hizmet vermenin süregelen maliyeti. Sonradan uyarlama tipik olarak, baştan tasarlamanın maliyetinin birkaç katına mal olur.

Liderliğe gerekçeyi sunmak için, geçerli olduğu yerde yasal yükümlülükle başlayın (kamu için pazarlık konusu değildir, özel sektör için de giderek öyledir). Ardından dışladığınız ulaşılabilir nüfusu, bu dışlamanın yardımlı kanal maliyetini ve tüm kullanıcılar için "kaldırım rampası" kazançlarını sayısallaştırın. Erişilebilirliği hayırseverlik değil, risk yönetimi artı kalite olarak konumlandırın.

## Anti-kalıplar ve tuzaklar

- **Lansman öncesi onay kutusu olarak erişilebilirlik**: sürekli uygulama yerine sonda bir denetim; pahalı son dakika yeniden işini garantiler.
- **"Div çorbası"**: genel öğeler üzerinde tıklama işleyicileri olan, yardımcı teknolojiye görünmez, anlamsal olmayan işaretleme.
- **ARIA'nın kötü kullanımı**: bozuk işaretlemenin üzerine ARIA yapıştırmak; düz işaretlemeden daha çok yanıltır.
- **Yalnızca renkle bilgi**: yalnızca renkle gösterilen durum; renk körü kullanıcılara görünmez.
- **Görünmez odak**: estetik için odak çerçevelerini kaldırmak; klavye kullanıcılarını çaresiz bırakır.
- **Klavye tuzakları**: odağı hapseden ya da kaybeden kipler ve bileşenler.
- **Otomatik tarama rehaveti**: bir tarayıcıyı geçip ürünün erişilebilir olduğunu varsaymak.
- **Erişilebilirlik yer paylaşımları**: gerçek uyumu sağlamayan ve deneyimi kötüleştirebilen üçüncü taraf "tek satırlık çözüm" bileşenleri.
- **Engelli kullanıcıları araştırmanın dışında bırakmak**: gerçek kullanıcılarla test etmek yerine hayali bir engelli kullanıcı için tasarlamak.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Erişilebilirlik uygulaması yoktur. Sorunlar yalnızca bir kullanıcı şikâyet ettiğinde ya da bir dava geldiğinde keşfedilir ve yanıt tepkiseldir. İşaretleme anlamsal değildir ve test edilmemiştir; sorunun sahibi yoktur.

**Düzey 2, Geliştirme.** Farkındalık vardır ve bazı takımlar bunun üzerine hareket eder: burada bir derlemede otomatik tarayıcı, şurada bir klavye turu, büyük bir sürümden önce bir lansman öncesi denetim. Uygulama temel düzeydedir ve takımlar arasında tutarsızdır; erişilebilirlik hâlâ geç aşamada bir kontrol listesidir ve takvim baskısı altında sık sık önceliği düşer.

**Düzey 3, Standartlaştırma.** WCAG 2.2 AA belgelenmiş standarttır ve kurum genelinde uygulanır. Erişilebilirlik tasarım sistemine yerleştirilmiştir; böylece bileşenler varsayılan olarak erişilebilir sevk edilir, otomatik ve elle test edilir ve bitti tanımına yazılır. Takımlar eğitilmiştir, bir sahip ya da mükemmeliyet merkezi vardır ve bir düzeltme süreci tanımlanmıştır.

**Düzey 4, Yönetme.** Erişilebilirlik, başlangıç değerlerine karşı veriyle ölçülür ve denetlenir. Kurum uyum ölçütlerini zaman içinde izler (tarayıcı geçme oranları, önem derecesine göre açık engellerin sayısı, kritik yolculukların ekran okuyucu test kapsamı ve düzeltme süresi), bunları takım başına bir panoda raporlar ve gerilemeleri tavsiye niteliğinde uyarılar yerine derleme başarısızlıkları olarak ele alır. Hedefler bir başlangıç değerine göre konur ve ilerleme gözden geçirilir; böylece geri kalan bir takım, bir denetim onu bulmadan önce görünür olur.

**Düzey 5, Orkestrasyon.** Erişilebilirlik sürekli iyileştirilir ve kurum genelinde bütünleşiktir. Engelli insanlar araştırmanın ve testin yinelenen bir parçasıdır; erişilebilirlik tedariğe, tasarım belirteçlerine ve CI'a gömülüdür. Kurum standartlar değiştikçe uyum sağlar (yeni WCAG ölçütlerini benimser ve WCAG 3.0'a hazırlanır) ve tedarikçileri ile ortaklarını etkiler; böylece bütün tedarik zinciri uyumlu hale gelir.

## Tartışma fikirleri

- Son tarihler sıkıştığında erişilebilirliğin önceliğinin düşmesini nasıl önlersiniz?
- Risk profiliniz için otomatik, elle ve kullanıcı testinin doğru karışımı nedir?
- Erişilebilirlik uyumu tedarikçi sözleşmelerine ve tedariğe nasıl yazılmalı?
- WCAG uyumu ile engelli insanlar için gerçek kullanılabilirlik arasındaki boşluğu nasıl ele alırsınız?
- Takımlar bugün 2.2'ye göre inşa ederken WCAG 3.0'a nasıl hazırlanmalı?
- Engelli katılımcıları araştırma için adil ve saygılı biçimde nasıl bulur ve ücretlendirirsiniz?

## Önemli çıkarımlar

- Erişilebilirlik temel bir kalite niteliğidir ve kamu için yasal bir gerekliliktir.
- Taban olarak WCAG 2.2 AA'ya göre tasarlayın; zihinsel model olarak POUR ilkelerini kullanın.
- Önce anlamsal HTML; ARIA yalnızca gerçek boşlukları doldurmak için, doğru yapılmış olarak.
- Otomatik araçlar sorunların yaklaşık üçte birini yakalar; elle ve yardımcı teknoloji testi şarttır.
- Engelli insanlar için değil, onlarla birlikte test edin.
- Erişilebilirliği içine inşa etmek ucuz ve kalıcıdır; sonradan uyarlamak pahalı ve kırılgandır.
- Erişilebilir tasarım herkes için daha iyi tasarımdır: kaldırım rampası etkisi gerçektir.

## Kaynaklar ve ileri okuma

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
