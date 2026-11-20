# 10.3 Tedarik, açık kaynak ve lisanslama

## Genel bakış ve motivasyon

Hemen her modern yazılım sistemi, çoğunlukla başkasının yazdığı bileşenlerden bir araya getirilir. [Açık kaynak yazılım](https://en.wikipedia.org/wiki/Open-source_software); işletim sistemlerinin, dillerin, çatıların, veritabanlarının ve bulut altyapısının temelini oluşturur. Kuruma iki yoldan girer: bilinçli [tedarik](https://en.wikipedia.org/wiki/Procurement) yoluyla ve tek tek geliştiricilerin gelişigüzel `import` ifadeleriyle. Bu bölüm, bu tüketimi (ve uygun düştüğünde katkıyı) bilinçli yapmakla ilgilidir. Bu bir strateji, lisans uyumu, yükümlülüklerin ve copyleft riskinin anlaşılması ve bağımlı olduğunuz bileşenlerin kaçınılmaz [ömür sonu](https://en.wikipedia.org/wiki/End-of-life_(product)) için bir plan demektir.

Büyük takımlar için bahisler aynı anda hukuki, operasyonel ve stratejiktir. Hukuken, açık kaynak [lisansları](https://en.wikipedia.org/wiki/Software_license) gerçek yükümlülükleri olan, uygulanabilir sözleşmelerdir. [Copyleft](https://en.wikipedia.org/wiki/Copyleft) (türev işlerin aynı koşullarla paylaşılmasını gerektirebilen lisanslama) konusunu yanlış anlamak, en kötü durumda tescilli kaynağın açıklanmasını zorunlu kılabilir ya da dava açılmasını tetikleyebilir. Lisans ihlalleri, [durum tespiti](https://en.wikipedia.org/wiki/Due_diligence) sırasında bir devralmayı ya da halka arzı bile engelleyebilir. Operasyonel olarak, yönetilmeyen bağımlılıklar çürür: bileşenler bakımsız kalır, güvenlik açıkları biriktirir ve üretimin derinliklerinde gömülüyken ömrünü tamamlar. Stratejik olarak açık kaynak, maliyet tasarrufu sağlayan bir girdiden fazlasıdır. [Bağımlılıktan](https://en.wikipedia.org/wiki/Vendor_lock-in) kaçınmanın, yetenek çekmenin ve bel bağladığınız ekosistemleri şekillendirmenin bir yoludur; ancak bu avantajları yalnızca bilerek ilgilenirseniz elde edersiniz.

Kamunun ek bir boyutu var. Birçok yargı alanında artık açık kaynağı, açık standartları ve kurumlar arası kod paylaşımını tercih eden açık politikalar bulunuyor. Bunlar sıklıkla "kamu parası, kamu kodu" olarak ifade edilir: vergi mükellefleri tarafından fonlanan yazılımın varsayılan olarak kamuya açık olması gerektiği ilkesi. Dolayısıyla kamu sektörü mühendisleri hem lisans uyumunda hem de açık kaynağı tercih etme, yayımlama ve yeniden kullanma yönündeki etkin görevlendirmelerde yol bulmak zorundadır. Bu bölüm bunların hepsini ölçekte yönetilebilir kılmayı amaçlar.

## Temel ilkeler

- **Açık kaynak bir tedarik zinciridir, bedava bir şey değil.** Tüketilen bileşenlere herhangi bir kritik tedarikçiye gösterdiğiniz titizlikle yaklaşın.
- **Lisanslar görmezden gelinecek izinler değil, yükümlülüklerdir.** Her bağımlılık koşullar taşır; sevk etmeden önce onları bilin.
- **Copyleft bir tasarım kısıtıdır, tabu değil.** Copyleft lisansları kullanılabilir ve değerlidir; yalnızca yazılımı nasıl birleştirip dağıttığınızı anlamanızı gerektirir.
- **Bilinçli tüketin, stratejik katkıda bulunun.** Neyi içeri alacağınıza karar verin ve size hizmet ettiği yerde, çatallamak yerine yukarı akışa göndermeye yatırım yapın.
- **Her şeyin envanterini çıkarın.** Göremediğinize uyum sağlayamaz, onu güvence altına alamaz ya da güncelleyemezsiniz; bir SBOM (yazılım malzeme listesi, yazılımınızdaki bileşenlerin eksiksiz envanteri) asgari şarttır.
- **Baştan ömür sonunu planlayın.** Her bağımlılık bir gün bakımsız kalacaktır; zorlanmadan önce çıkışınızı bilin.
- **Kamuda, varsayılan olarak açık olun.** [Açık standartları](https://en.wikipedia.org/wiki/Open_standard) ve açık kaynağı tercih edin ve belirli bir neden yoksa kamu parasıyla yazılan kodu yayımlayın.

## Öneriler

### Bir açık kaynak stratejisi ve tüketim politikası belirleyin

Geliştiricilerin açık kaynağı kuruma nasıl getirebileceği konusunda net bir politika yayımlayın: hangi lisanslar önceden onaylı, hangileri inceleme gerektiriyor ve hangileri kullanım durumlarınız için yasak. Hızlı, sürtünmesi düşük bir onay yolu sağlayın. Kod kopyalamaktan daha yavaş bir politika basitçe göz ardı edilir. Bağlamları ayırt edin, çünkü aynı lisans, bir bileşen içeride hizmet olarak kullanıldığında, dağıtılan bir ürüne gömüldüğünde ya da tescilli bir uygulamaya bağlandığında farklı davranır. Kolay yolu uyumlu yol yapın: incelenmiş bileşenlerden oluşan özenle seçilmiş bir iç depo, hatta otomatik tarama ve geliştiricilerin rutin durumlar için avukat aramadan izleyebileceği net rehberlik.

### Lisans uyumunu, yükümlülükleri ve copyleft riskini yönetin

Lisans ailelerini ve yükümlülüklerini tanıyın. [Serbest lisanslar](https://en.wikipedia.org/wiki/Permissive_software_license) (MIT, BSD ve Apache 2.0 gibi) esas olarak atıf ve bildirimin korunmasını gerektirir; Apache 2.0 buna açık bir patent hakkı ekler. Zayıf copyleft (örneğin [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License) ve MPL), kapsanan dosyalardaki değişiklikleri paylaşmanızı gerektirir ama genellikle tescilli kodla birleştirmenize izin verir. Güçlü copyleft (örneğin [GPL](https://en.wikipedia.org/wiki/GNU_General_Public_License)), dağıtılan işin bütününün aynı koşullarla sunulmasını gerektirebilir. Ağ copyleft'i ([AGPL](https://en.wikipedia.org/wiki/GNU_Affero_General_Public_License)) bu yükümlülüğü yalnızca ikili dosyalar olarak dağıtılan değil, ağ üzerinden sunulan yazılıma da genişletir. En önemli yükümlülükler iki şeye bağlıdır: yazılımı dağıtıp dağıtmadığınıza ve bileşenleri ne kadar sıkı birleştirdiğinize. Uyumu otomatikleştirin: bağımlılıkları lisanslar için tarayın, gerekli atıf ve bildirim dosyalarını üretip sevk edin ve yasak bir lisansın üretime sessizce girememesi için derlemeyi politikaya göre geçitleyin.

### Bir Açık Kaynak Program Ofisi (OSPO) kurun

Açık kaynağı ölçekte tüketiyorsanız, açık kaynak stratejisinin, politikasının, uyum araçlarının, katkı yönetişiminin ve topluluk ilişkilerinin sahibi olan bir odak noktası, yani bir OSPO oluşturun. OSPO, her takımın kendi kararını vermesinin kaosunu dizginler. Tekil takımların sürdüremeyeceği uzmanlığı sağlar. Ve stratejik değeri yakalar: hangi projelere yatırım yapılacağına, yukarı akışa ne zaman katkıda bulunulacağına ve kendi açık kaynak projelerinizin nasıl iyi yayımlanacağına karar verir. Küçük bir OSPO bile (bazen bir kişi artı işlevler arası bir çalışma grubu), başıboşluğa kıyasla tutarlılığı çarpıcı biçimde artırır ve hukuki riski azaltır.

### Katkıyı ve uygun düştüğünde yayımlamayı yönetin

Ne zaman geri katkı vereceğinize bilinçli karar verin. Bağımlı olduğunuz projelere düzeltmeleri ve özellikleri yukarı akışa göndermek, bakım yükünüzü azaltır, çünkü özel yamalar taşımayı bırakırsınız. Ayrıca iyi niyet ve etki kazandırır ve sizin için kritik bileşenleri güçlendirir. Fikri mülkiyetin ve katkıcı sözleşmelerinin nasıl ele alındığı dahil, onaylı katkılar için geliştiricilere net, hızlı bir süreç verin. Kendi açık kaynak projelerinizi yayımladığınızda bunu doğru yapın: uygun bir lisans seçin, yönetişimi belgeleyin ve vekilliğe söz verin. Terk edilmiş bir proje, hiç proje olmamasından daha çok itibarınıza zarar verir.

### Hükümetin açık kaynak ve "kamu parası, kamu kodu" görevlendirmelerini karşılayın

Kamu sektörü takımları açıklığı varsayılan olarak ele almalıdır. Bağımlılıktan kaçınmak ve kurumlar ile tedarikçiler arasında çalışmak için açık standartları tercih edin. Kamu fonlarıyla geliştirilen kaynak kodunu, belirli ve belgelenmiş bir muafiyet geçerli olmadıkça (güvenliğe duyarlı bileşenler, üçüncü taraf hakları ya da gizlilik kaygıları için) açıkça yayımlayın. İnşa etmeden önce yeniden kullanın: başka bir kurumun uygun kodu zaten yayımlayıp yayımlamadığını kontrol edin. Bu beklentileri tedarike işleyin; böylece tedarikçiler, kurumun bakımını yapamayacağı ya da paylaşamayacağı tescilli kara kutular yerine, devletin uygun hakları elinde tuttuğu açık, yeniden kullanılabilir, iyi belgelenmiş kod teslim eder.

### Bağımlılıkları ve ömrünü tamamlamış yazılımı yönetin

Her bileşenin ve sürümünün, lisansının ve bakım durumunun canlı bir envanterini (SBOM) tutun. Bağımlılıkları makul ölçüde güncel tutun. Küçük, sık güncellemeler, nadir, dev sıçramalardan çok daha ucuz ve güvenlidir. Yukarı akış projelerini ömür sonu duyuruları ve güvenlik destek pencereleri için izleyin ve geçişleri, bir güvenlik açığı sizi telaşa itmeden önce, destek bitmeden planlayın. Terk edilme riski taşıyan kritik bileşenler için, bakımcıyı fonlayıp fonlamayacağınıza, bakımı kendiniz üstlenip üstlenmeyeceğinize, çatallayıp çatallamayacağınıza ya da değiştirip değiştirmeyeceğinize önceden karar verin. Hem ticari hem açık kaynak yazılımın ömür sonunu izleyin ve desteğin tükenmesini diğer her operasyonel risk gibi aynı ölçüte tabi tutun.

## Ödünleşimler: artılar ve eksiler

| Seçim | Artılar | Eksiler |
|---|---|---|
| Açık kaynağı serbestçe tüketmek | Hızlı teslimat; büyük kaldıraç; lisans ücreti yok | Artık sizin olan lisans, güvenlik ve bakım yükümlülükleri |
| Katı lisans izin listesi | Düşük hukuki risk; öngörülebilir | Takımları yavaşlatır; gerçekten yararlı bileşenleri dışlayabilir |
| Yalnızca serbest lisanslar | Asgari yükümlülük; birleştirmesi kolay | Değerli copyleft projelerinden vazgeçmek; daha az karşılıklılık |
| Uygun yerde copyleft'i kabul etmek | Güçlü ekosistemlere erişim; karşılıklılık yararları | Birleştirme ve dağıtımda özen gerektirir |
| Yukarı akışa katkı vermek | Daha az özel yama yükü; etki; iyi niyet | Süregelen emek; fikri mülkiyet ve süreç yükü |
| Bunun yerine tescilli inşa etmek | Tam denetim; dış yükümlülük yok | Yüksek maliyet; sıradan olanı yeniden icat etmek; sonsuza dek bakımı sizde |
| Kamuda varsayılan olarak yayımlamak | Şeffaflık; yeniden kullanım; bağımlılıktan kaçınma | Yayımlama emeği; güvenlik incelemesi; sürdürülen vekillik |

Merkezî gerilim, geliştirici hızı ile denetim arasındadır. Her şeyi ağır incelemenin arkasına kilitlerseniz geliştiriciler politikanın çevresinden dolanır. Bu, serbest ama görünür bir yaklaşımdan daha kötü olan, yönetilmeyen gölge bağımlılıklar yaratır. Tamamen denetimsiz bırakırsanız hukuki ve güvenlik borcunu görünmez biçimde biriktirirsiniz. Çözüm otomasyon ve özenli seçimdir: önceden incelenmiş bileşenler, hat taraması ve net varsayılanlarla uyumlu yolu en hızlı yol yapın; böylece sürtünmesiz denetim elde edersiniz. Copyleft konusunda ödünleşim "riskli ile güvenli" değil, "anlaşılmış ile anlaşılmamış"tır. Birleştirme ve dağıtım biçiminizi bildiğinizde copyleft tümüyle kullanılabilirdir.

## Takımınızla tartışılacak sorular

1. **İçeride, dağıtılan ve ağ üzerinden sunulan bağlamlarda güçlü ve ağ copyleft'i için açık kuralınız nedir?** Copyleft bir tasarım kısıtıdır, tabu değil ve yükümlülükler iki şeye bağlıdır: yazılımı dağıtıp dağıtmadığınıza ve bileşenleri ne kadar sıkı birleştirdiğinize. Bir iç araçtaki GPL, sevk ettiğiniz bir ürüne bağlanan GPL'den çok farklı davranır ve AGPL, açıklama görevlerini yalnızca ağ üzerinden sunduğunuz yazılıma kadar genişletir; bu da hizmet olarak çalıştırdığınız her şey için yap-ya-da-benimse hesabınızı değiştirir. Kuralı bağlam başına yazın, böylece bir geliştirici avukat aramadan (örneğin) serbest lisansların her yerde önceden onaylı, güçlü copyleft'in içeride tamam ama sevk edilen üründen engelli ve AGPL'nin ağa bağlı bir hizmete dokunmadan önce incelemeye ihtiyacı olduğunu bilir. Kanıt getirin: mevcut bağımlılık ağacınızı tarayın ve copyleft bileşenlerin dağıtım sınırınıza göre şu an nerede durduğunu bulun. Sonra derlemeyi bu politikaya göre geçitleyin, çünkü hiçbir tarayıcının uygulamadığı bir kural, geliştiricilerin yanlışlıkla çiğneyeceği bir kuraldır.

2. **Bir Açık Kaynak Program Ofisine ihtiyacınız var mı ve lisans politikası, tarama ve katkı kararlarının bugün sahibi kim?** Dürüst yanıt "kimse" ya da "her takım karar veriyor" ise, hukuki ve güvenlik borcunu görünmez biçimde biriktiren bir başıboşluk yürütüyorsunuz demektir. Bir OSPO, bir kişi artı işlevler arası bir çalışma grubu bile olsa, bu kaosu dizginler ve stratejik değeri yakalar: hangi yukarı akış projelerine yatırım yapılacağı, ne zaman katkı verileceği ve kendi projelerinizin nasıl iyi yayımlanacağı. Toplantıya kanıtla gelin: herhangi biri güncel onaylı lisans listesini, SBOM'u ve bir devralma durum tespiti sırasında bir copyleft sorusunu yanıtlayacak kişinin adını üretebiliyor mu? Yanıt net bir sahiplik atamalı ve önceden incelenmiş bileşenler ve hat taraması yoluyla uyumlu yolu en hızlı yol yapmalı; böylece geliştiriciler sürtünmesiz denetim elde eder. Kod kopyalamaktan daha yavaş bir politika basitçe göz ardı edilir.

3. **Hangi bağımlılıklar yarın terk edilse en çok zarar verir ve her biri için önceden kararlaştırılmış yanıtınız nedir?** Her bağımlılık eninde sonunda ömrünü tamamlar ve bu olayın pahalı sürümü, bir güvenlik açığı dikkati zorlayana kadar çekirdek bir bileşenin aylar önce desteğini yitirdiğini keşfetmektir. Terk edilme riski taşıyan kritik bileşenleriniz için bakımcıyı fonlayıp fonlamayacağınıza, bakımı kendiniz üstlenip üstlenmeyeceğinize, çatallayıp çatallamayacağınıza ya da değiştirip değiştirmeyeceğinize önceden karar verin. Kanıt getirin: SBOM'unuzdan, başarısızlığı gelir getiren ya da misyon açısından kritik bir hizmeti durduracak bileşenleri listeleyin ve her birinin bakım durumunu ve güvenlik destek penceresini not edin. Yanıt, ömür sonunu bir sürprizden, planlı bir geçişle izlenen bir operasyonel riske dönüştürmeli ve diğer her risk gibi aynı ölçüte tabi tutulmalı. Bağımlılıkları küçük, sık adımlarla güncel tutmak, nadir, dev, zorunlu sıçramadan çok daha ucuzdur.

4. **Dolaylı bağımlılık ağacınızın en altına kadar uzanan eksiksiz, güncel bir SBOM üretebilir misiniz ve ne kadar hızlı?** Yaygın kullanılan bir kütüphaneye manşetlik bir güvenlik açığı düştüğünde, liderliğin sorduğu ilk soru "açıkta mıyız ve nerede?" olur. Bunu saatler içinde yanıtlayamayan bir takım zaten geridedir, çünkü gerçek risk genellikle kimsenin bilerek seçmediği bağımlılıklarda birkaç katman aşağıda saklanır. Karşı değerlendirme maliyet ve gürültüdür: birçok hizmet boyunca tam dolaylı envanter büyük, sürekli değişen bir liste üretir ve aşırı uyarı insanlara onu görmezden gelmeyi öğretir; bu yüzden hangi derinliğin ve hangi şiddetin gerçekten eylemi tetiklediğine karar vermelisiniz. Tartışmaya kanıtla gelin: şu an bir üretim hizmeti için yeni bir SBOM üretmeyi deneyin, doğrudan ile dolaylı bileşenleri sayın ve ne kadar sürdüğünü ölçün. Bir kurum ya da kamu kuruluşu için bunu somut bir olay müdahale hedefine ve etkilenen bileşenleri açıklama yönündeki her düzenleyici göreve bağlayın, çünkü sayamayacağınız bir maruziyeti raporlama görevi, ihlal edeceğiniz bir görevdir.

5. **Kritik bir bağımlılığı bedava saymak yerine fonlamaya, katkı vermeye ya da ona vekillik etmeye ne zaman değer?** Çoğu kurum açık kaynağı bir kamu hizmeti gibi tüketir, sonra gelir getiren bir hizmetin altındaki bir bileşenin karşılıksız çalışan tek bir gönüllü olduğunu görünce şaşırır. Bir bakımcıyı fonlamaya, düzeltmeleri yukarı akışa göndermeye ya da kendi projenizi yayımlayıp ona vekillik etmeye bilinçli karar vermek, kırılgan bedava bir girdiyi dayanıklı, etkilediğiniz bir girdiye dönüştürür ve mühendislerinizin her yükseltmede özel yamalar taşımasını önler. Gerilim şudur: katkı ve vekillik gerçek, süregelen mühendislik zamanına mal olur ve fikri mülkiyet ve süreç yükü taşır; bu yüzden her şey için yapamazsınız. Kanıt getirin: SBOM'unuzdan, başarısızlığı misyon açısından kritik bir hizmeti durduracak bir avuç bileşeni işaretleyin ve her birinin bakımcı sayısını, fonlamasını ve ona karşı zaten kaç özel yama taşıdığınızı not edin. Büyük ya da kamusal bir kurum için, gürültüyle yayımladığınız ve terk edilen bir açık kaynak sürümünün itibar maliyetini tartın ve kamuda, yayımlanan kamu parası kodunun sürdürülen vekilliğini isteğe bağlı bir ekstra değil, teslimatın parçası olarak görün.

6. **Tedarikiniz gerçekten ihtiyaç duyduğunuz haklarla açık, yeniden kullanılabilir, iyi belgelenmiş kod mu teslim ediyor, yoksa bakımını yapamayacağınız ya da çıkamayacağınız tescilli kara kutular mı?** Açık kaynak uzmanlığı olmadan yazılan sözleşmeler rutin olarak bir tedarikçiye pişman olacağınız bir denetim verir: kapalı biçimler, yayımlama ya da değiştirme hakkı yok ve tedarikçi gittiğinde kurumun yamayamayacağı bağımlılıklar. Bunu erken doğru yapmak, yenileme sırasında ayrılamayacağınızı keşfetmekten çok daha ucuzdur. Karşı değerlendirmeler hız ve tedarikçi seçimidir: açık teslimat ve taşınabilirlik talep etmek alanı daraltabilir ve bir ihaleyi yavaşlatabilir ve bazı gerçekten yararlı tedarikçiler buna direnir. Kanıt getirin: yakın tarihli iki sözleşmeyi çekin ve lisans koşullarını, kaynak kodu teslimini, belgeleme standartlarını, SBOM sağlanmasını ve kurumun elinde tuttuğu hakları belirtip belirtmediklerini kontrol edin. Kurumsal tedarik için bunu bağımlılık ve toplam maliyet analizine bağlayın; kamu için bunu varsayılan olarak açık ve "kamu parası, kamu kodu" görevlendirmelerine ve bütün sistemi değil, yalnızca güvenliğe duyarlı kısımları kapatmanıza izin veren belgelenmiş muafiyet sürecine bağlayın.

## Sektör merceği

**Girişim.** Hemen her şeyi açık kaynaktan bir araya getiriyorsunuz ve avukatınız yok; bu yüzden kuralı tek sayfada tutun: MIT ve Apache 2.0 gibi serbest lisanslar önceden onaylı, güçlü copyleft iç araçlar için tamam ama sevk edilen üründen engelli ve garip her şey hızlı bir kurucu incelemesinden geçer. Hatta bir lisans ve güvenlik açığı taraması ekleyin ve ilk günden bir SBOM tutun, çünkü bunu doğru yapmanın en ucuz anı, bir alıcının durum tespitinin bağımlılık ağacınızı taramasından öncesidir. Copyleft'i korkudan yasaklamayın; anlayın ve devam edin.

**Küçük işletme.** Açık kaynak uzmanı ve dar bir bütçe olmadan kadro yerine araçlara yaslanın: derlemedeki bir tarayıcı ve kısa bir onaylı lisans listesi, bir insanın yapacağı işin çoğunu yapar. Tüketimi dürüstçe yap-ya-da-satın-al olarak çerçeveleyin, çünkü iyi bakımlı açık bir bileşeni yeniden icat etmek genellikle pahalı seçimdir, ama envanterini hiç çıkarmadığınız birine bağımlı olmak da öyle. Neyi hangi lisansla kullandığınızın basit bir kaydını tutun; böylece bir müşteri güvenlik anketi ya da bir güvenlik açığı uyarısı bir telaşa dönüşmez.

**Kurumsal.** Ölçekte sorun birçok takım arasında tutarlılıktır; bu yüzden politikanın, otomatik taramanın, atıf üretiminin ve katkı yönetişiminin sahibi olacak bir OSPO kurun ve özenle seçilmiş, önceden incelenmiş bileşenlerle uyumlu yolu en hızlı yol yapın. Copyleft kurallarını hatta bağlam başına uygulayın, hizmetler boyunca SBOM'ları sürdürün ve bağımlılık güncelliğini ve ömür sonunu izlenen operasyonel risk olarak yönetin. Açık kaynağı, kod tabanınızın çoğunluğu için tedarik zinciri yönetimi olarak görün ve devralma durum tespiti için denetime hazır kanıt tutun.

**Kamu.** Açıklık çoğu zaman isteğe bağlı değil, görevlendirilmiştir; bu yüzden varsayılan olarak açık standartları izleyin ve güvenlik, üçüncü taraf hakları ya da gizlilik için belgelenmiş bir muafiyet geçerli olmadıkça kamu parasıyla yazılan kodu yayımlayın. Kurumlar arası bir katalogu kontrol ederek inşa etmeden önce yeniden kullanın ve açık, yeniden kullanılabilir, iyi belgelenmiş teslimatları ve elde tutulan hakları tedarike işleyin; böylece tescilli kara kutular yerine bakımı yapılabilir kod alırsınız. Yayımlanan koda gerçek vekillik gösterin ve muafiyet sürecini dar ve şeffaf tutun, böylece yalnızca kapatması gerekeni kapatır.

## Örnekler

**Girişim.** Mobil uygulama geliştiren dört kişilik bir girişim, hemen her şeyi açık kaynaktan bir araya getiriyor ve kadroda avukatı yok. Copyleft'i korkudan yasaklamak yerine kurucular tek sayfalık bir politika yazıyor: MIT ve Apache 2.0 gibi serbest lisanslar önceden onaylı, GPL gibi güçlü copyleft iç araçlar için tamam ama açıklama görevlerinden kaçınmak için sevk edilen uygulamadan engelli ve olağandışı her şey hızlı bir kurucu incelemesinden geçiyor. Yasak bir lisansın bir sürüme sızamaması için hatta bir lisans ve güvenlik açığı taraması ekliyorlar, ilk günden bir SBOM tutuyorlar ve her yükseltmede özel bir yama taşımayı bırakmak için kritik bir kütüphaneye küçük bir düzeltmeyi yukarı akışa gönderiyorlar. Bunu erken doğru yapmak, bir alıcının durum tespiti eninde sonunda bağımlılık ağacını taradığında acı verici bir sürprizden de kurtarıyor.

**Kurumsal.** Dağıtılan bir ürün sevk eden bir yazılım şirketi bir OSPO yürütüyor. OSPO, onaylı lisans listesi, özenle seçilmiş bir iç bileşen deposu ve her hatta otomatik lisans ve güvenlik açığı taraması tutuyor. Bir geliştirici yeni bir bağımlılık çektiğinde hat lisansını politikaya göre kontrol ediyor, ürünle sevk edilen atıf bildirimlerini üretiyor ve inceleme gerektiren her şeyi işaretliyor. Güçlü copyleft bileşenlere iç araçlar için izin veriliyor ama açıklama yükümlülüklerinden kaçınmak için dağıtılan üründen engelleniyor. Şirket birkaç kritik bağımlılığa düzeltmeleri yukarı akışa gönderiyor. Bu, mühendislerinin her yükseltmede taşıdığı özel yama birikimini ortadan kaldırdı.

**Kamu.** Ulusal bir dijital hizmet "kamu parası, kamu kodu" politikası altında çalışıyor. Yeni hizmetler açık standartlar üzerine inşa ediliyor, varsayılan olarak herkese açık bir kod deposunda açıkça geliştiriliyor ve kurumlar arasında yeniden kullanılıyor. Tedarik şablonları, tedarikçilerin devletin yayımlama ve değiştirme haklarını elinde tuttuğu açık, iyi belgelenmiş, yeniden kullanılabilir kod teslim etmesini şart koşuyor. Yeni bir bileşene başlamadan önce takımlar kurumlar arası bir katalogda mevcut yeniden kullanılabilir kodu arıyor. Güvenliğe duyarlı modüller, bütün sistemi kapalı yapmak yerine belgelenmiş bir süreçle yayımlamadan muaf tutuluyor.

## İş gerekçesi: motivasyonlar, YG ve TSM

Açık kaynağı iyi yönetmek, onun muazzam kaldıracını yakalamakla gizli maliyetlerini ödemek arasındaki farktır. Açık kaynak, büyük bir kurumun asla inşa etmeyi karşılayamayacağı bir temelin üzerinde durmasına izin verir. Ama [toplam sahip olma maliyeti](https://en.wikipedia.org/wiki/Total_cost_of_ownership) uyumu, güvenlik yamalamayı ve eninde sonunda geçişi içerir; planlasanız da planlamasanız da gelen maliyetler. Bilinçli yönetim, öngörülemez, pahalı krizleri küçük, istikrarlı, planlı maliyetlere dönüştürür. Bu krizler arasında bir devralma durum tespiti sırasında bulunan copyleft ihlali, terk edilmiş bir bileşenden acil geçiş ya da kimsenin orada olduğunu bilmediği bir bağımlılıktaki güvenlik açığı bulunur.

Benimseme maliyeti maruziyete kıyasla mütevazıdır: bir OSPO ya da çalışma grubu, tarama araçları ve bir envanter tutma disiplini. Benimsememenin maliyeti hukuki sorumluluk, başarısız durum tespiti, yamalanmamış bağımlılıklara kadar izlenen güvenlik olayları ve sonunda acı verici toptan geçişleri zorlayan ertelenmiş yükseltmelerin biriken gideri olarak ortaya çıkar. Liderliğe gerekçe sunarken açık kaynak yönetimini, kod tabanınızın çoğunluğu için tedarik zinciri yönetimi olarak çerçeveleyin. Stratejik avantajı da not edin: önlenen bağımlılık, daha hızlı teslimat, yetenek çekme ve bel bağladığınız ekosistemler üzerinde etki. Kamuda görevlendirme boyutunu ekleyin. Açıklık çoğu zaman isteğe bağlı değil, gereklidir ve iyi yapmak hem uyumsuzluktan hem de çifte kamu harcamasından kaçınır.

## Anti-kalıplar ve tuzaklar

- **Kopyala-yapıştır lisanslama.** Geliştiricilerin lisans kontrolü olmadan bileşenleri çekmesi ve yükümlülükleri yalnızca denetimde ya da devralmada keşfetmesi.
- **Envanter yok.** Bir güvenlik açığı ya da lisans sorusu patladığında "ne kullanıyoruz ve hangi lisansla?" sorusuna yanıt verememek.
- **Copyleft paniği.** Anlamak yerine korkudan bütün copyleft'i yasaklamak ve değerli ekosistemlerden vazgeçmek.
- **Terk edilmiş açık kaynak sürümü.** Bir projeyi gürültüyle yayımlayıp sonra hiç bakımını yapmamak ve itibara zarar vermek.
- **Dolaylı bağımlılıkları göz ardı etmek.** Doğrudan bağımlılıkları incelerken gerçek riskin birkaç katman aşağıda saklanması.
- **Ömür sonu sürprizi.** Çekirdek bir bileşenin aylar önce desteğini yitirdiğini, yalnızca bir güvenlik açığı dikkati zorladığında keşfetmek.
- **Kopyalamadan yavaş politika.** Geliştiricilerin çevresinden dolanacağı kadar ağır bir uyum süreci; bu da görünmez gölge bağımlılıklar yaratır.
- **Kamu kara kutuları.** Varsayılan olarak açık ilkelerini çiğneyerek, kurumun bakımını yapamayacağı, paylaşamayacağı ya da çıkamayacağı tescilli sistemler tedarik etmek.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Geliştiriciler politika ya da envanter olmadan açık kaynağı serbestçe ekler. Lisanslar incelenmemiştir ve copyleft yükümlülükleri bilinmez. Ömür sonu kazara, genellikle bir güvenlik açığı dikkati zorladığında keşfedilir. Açık kaynak stratejisinin sahibi yoktur.

**Düzey 2, Geliştirme.** Temel bir politika ve onaylı lisans listesi vardır ve bazı takımlar onları izler. Tarama olur, ama çoğu zaman elle, geç ya da yalnızca birkaç projede. Büyük sistemler için bir envanter tutulurken dolaylı bağımlılıklar haritalanmaz. Katkı ve ömür sonu ele alınışı anlıktır ve takımlar arasında tutarsızdır.

**Düzey 3, Standartlaştırma.** Bir OSPO ya da eşdeğeri stratejinin, politikanın ve araçların sahibidir ve kurum geneline yayar. Lisans ve güvenlik açığı taraması her hatta otomatiktir, atıf ve bildirim dosyaları otomatik üretilir ve derleme, yasak bir lisansın giremeyeceği şekilde geçitlenir. SBOM'lar dolaylı ağacın en altına kadar sürdürülür, katkı belgelenmiş bir süreci izler, ömür sonu planlı geçişlerle izlenir ve kamu takımları varsayılan olarak yayımlar.

**Düzey 4, Yönetme.** Program başlangıç değerlerine karşı ölçülür ve denetlenir. Hizmetler boyunca politika tarama kapsamını, açıklanan bir bağımlılık güvenlik açığını yamalamanın ortalama süresini, güvenlik destek penceresi içindeki bileşen payını, lisans ihlali kaçış oranını, bağımlılık güncellik gecikmesini ve yukarı akışa gönderilen özel yama sayısını izlersiniz. Copyleft'in dağıtım sınırına göre yerleşimi izlenir ve hedeflere karşı ölçütler her geç ya da geçme kararını görüşe değil, ölçüte dayandırır.

**Düzey 5, Orkestrasyon.** Açık kaynak, kurum genelinde bütünleşik, sürekli iyileştirilen stratejik bir varlıktır. Uyum tümüyle otomatiktir ve uyumsuz bileşenler üretime ulaşamaz. Kritik yukarı akış projelerine bilinçli yatırım yapar, rutin olarak katkı verir ve kendi iyi yürütülen projelerinize vekillik edersiniz. Bağımlılık güncelliği ve ömür sonu, risk ve ölçütler değiştikçe uyarlanarak yönetilir ve açıklık gerçek bir rekabet ve yurttaşlık avantajına dönüşür.

## Tartışma fikirleri

- Hızlı serbest bir varsayılan ile hukuki ve güvenlik borcundan kaçınmak için gereken denetim arasındaki doğru çizgi nerede?
- Bir kurum kritik bir yukarı akış bağımlılığını bedava saymak yerine ne zaman fonlamalı ya da bakımını yapmalı?
- Kendi bileşenlerinizden hangilerinin açık kaynak olarak yayımlanmaya ve vekilliğe değer olduğuna nasıl karar verirsiniz?
- Kamu için, ilkeyi aşındırmadan bileşenleri varsayılan olarak yayımlama kuralından muaf tutmanın savunulabilir bir süreci nedir?
- Lisans ve güvenlik incelemesi dolaylı bağımlılıklarda gerçekçi olarak ne kadar derine inmelidir?
- Ağ copyleft'i (AGPL), hizmet olarak sunduğunuz yazılım için yap-ya-da-benimse hesabınızı değiştirir mi?

## Önemli çıkarımlar

- Açık kaynak çoğu kod tabanının çoğunluğudur ve bedava ve sonuçsuz sayılmamalı, bir tedarik zinciri olarak yönetilmelidir.
- Lisanslar gerçek yükümlülükler taşır; serbest, zayıf copyleft, güçlü copyleft ve ağ copyleft ailelerini ve dağıtım ile birleştirmenin görevleri nasıl tetiklediğini anlayın.
- Özenli seçim, otomatik tarama ve net varsayılanlarla uyumlu yolu en hızlı yol yapın, yoksa geliştiriciler politikanın çevresinden dolanır.
- Stratejiyi, uyumu, katkıyı ve vekilliği ölçekte sahiplenmek için bir OSPO kurun.
- Bir SBOM tutun, bağımlılıkları küçük adımlarla güncel tutun ve ömür sonunu bir krizi zorlamadan önce planlayın.
- Kamuda, varsayılan olarak açık standartları izleyin ve kamu parası kodunu yayımlayın, inşa etmeden önce yeniden kullanın.

## Kaynaklar ve ileri okuma

- Heather Meeker, *Open (Source) for Business* and *Open Source for Business*
- Van Lindberg, *Intellectual Property and Open Source*
- The Linux Foundation and TODO Group, *OSPO guides* and *Open Source Program Office resources*
- OpenChain (ISO/IEC 5230), *Open Source Licence Compliance*
- Software Package Data Exchange (SPDX, ISO/IEC 5962) specification
- CycloneDX SBOM specification
- Free Software Foundation, *GNU General Public Licence* and *GPL FAQ*
- Open Source Initiative, *The Open Source Definition* and approved licence list
- Free Software Foundation Europe, *Public Money, Public Code*
- U.S. Federal Source Code Policy and Code.gov guidance
- UK Government, *Technology Code of Practice* and open-standards principles
