# 2.10 Yazılım yapılandırma yönetimi

## Genel bakış ve motivasyon

[Yazılım yapılandırma yönetimi](https://en.wikipedia.org/wiki/Software_configuration_management) (YYY), bir yazılım sisteminin bileşenlerini tanımlama, nasıl değiştiklerini kontrol etme, her değişikliğin durumunu kaydetme ve inşa ettiğiniz ve teslim ettiğiniz şeyin amaçladığınızla eşleştiğini doğrulama disiplinidir. Basit görünen ama ölçekte zorlaşan bir soruyu cevaplar: bu sürümde tam olarak ne var, oraya nasıl geldi ve kim onayladı? [SWEBOK](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) YYY'yi temel bir bilgi alanı olarak ele alır ve bunun net bir nedeni vardır: diğer her mühendislik etkinliği karşısında çalışacağı kararlı, bilinen bir yapılandırmaya ihtiyaç duyar.

Büyük bir takımda YYY, binlerce hareketli parçayı tutarlı tutan bağ dokusudur. Kaynak kod, kütüphaneler, kapsayıcı imajları, altyapı tanımları, yapılandırma verisi, belgeleme ve test yapıtları kendi saatlerinde değişir ve teslim edilen bir sistem, hepsinin belirli sürümlerinin belirli bir bileşimidir. Bilinçli yapılandırma yönetimi olmadan o bileşim bilinmez ve yeniden üretilemez. Geçmiş bir sürümü yeniden oluşturamaz, bir kusuru onu yaratan değişikliğe izleyemez ya da üretimde neyin çalıştığını güvenle söyleyemezsiniz.

Kurumsal ve kamu ortamları bahsi yükseltir. Düzenlemeye tabi ve kamu sektörü programları değişikliklerin yetkilendirildiğini, incelendiğini ve kaydedildiğini; teslim edilen bir derlemenin onaylı gereksinimlere ve kaynağa izlendiğini; ve sisteme hiçbir şeyin kontrolsüz girmediğini göstermelidir. Burada YYY, bir mühendislik sistemi olduğu kadar bir kanıt sistemidir. [Sürüm kontrolü](https://en.wikipedia.org/wiki/Version_control) (bölüm 2.6) kaynak geçmişini yönetir; YYY ise tüm yapılandırmayı ve onun değiştiği kontrollü süreci yönetir. [Kod olarak altyapıyla](https://en.wikipedia.org/wiki/Infrastructure_as_code) (bölüm 8.2), teslimat hatlarıyla (bölüm 8.1) ve denetim ve güvenceyle (bölüm 10.2) yakından bağlantılıdır.

## Temel ilkeler

- Sistem davranışını belirleyen her şey, yalnızca kaynak kod değil, kontrol altındaki bir [yapılandırma öğesidir](https://en.wikipedia.org/wiki/Configuration_item).
- Bir [temel çizgi](https://en.wikipedia.org/wiki/Baseline_(configuration_management)) bilinen, üzerinde anlaşılmış bir referans noktasıdır; değişiklikler temel çizgilere karşı rastgele değil bilinçli yapılır.
- Değişim önlenmez, kontrol edilir ve kaydedilir; amaç yetkilendirilmiş, izlenebilir değişimdir.
- Durum muhasebesi, bir yapılandırmada ne olduğunu ve değişim geçmişinin ne olduğunu her zaman cevaplayabileceğiniz anlamına gelir.
- Denetimler, inşa edilen ve teslim edilen sistemin kayıtlı yapılandırmayla ve onaylı gereksinimlerle eşleştiğini doğrular.
- Yeniden üretilebilirlik pazarlık dışıdır: yayımlanan herhangi bir sürüm kontrollü girdilerden yeniden inşa edilebilmelidir.
- Tanımlamayı, kaydetmeyi ve doğrulamayı otomatikleştirin; elle defter tutma ölçeklenmez ve denetimden sağ çıkmaz.

## Öneriler

### YYY sürecini tanımlayın ve sahiplik atayın

Neyin yapılandırma kontrolü altında olduğunu, öğelerin nasıl tanımlandığını, değişikliklerin nasıl önerilip onaylandığını ve durumun nasıl kaydedilip denetlendiğini söyleyen bir YYY planı yazın. Net sahiplik atayın, örneğin bir yapılandırma yöneticisi ya da sorumlu bir takım; böylece YYY herkesin ve dolayısıyla kimsenin işi olmaz. Süreci riske göre ölçeklendirin: küçük bir dahili araç hafif dokunuşlu kontrol ister, güvenlik açısından kritik ya da düzenlemeye tabi bir sistem resmi kurullar ve kayıtlar. Planı, denetçilerin ve ortakların izleyebilmesi için IEEE 828 gibi tanınmış bir standarda dayandırın.

### Yapılandırma öğelerini tanımlayın ve temel çizgiler oluşturun

Sistemin nasıl davrandığını belirleyen yapılandırma öğelerini listeleyin: kaynak, bağımlılıklar, derleme betikleri, kapsayıcı imajları, altyapı tanımları, yapılandırma verisi, şemalar ve kilit belgeler. Her birine kararlı bir tanımlayıcı ve bir sürümleme şeması verin. Temel çizgileri anlamlı noktalarda (yayımlanmış bir sürüm, onaylı bir gereksinim kümesi, sertifikalı bir derleme) belirleyin; böylece değişim yapacağınız ve geri döneceğiniz üzerinde anlaşılmış bir referansınız olur. Bir temel çizgi değişmezdir: ilan ettiğinizde onu düzenlemezsiniz. Yalnızca değişiklik süreciyle oluşturulan yeni bir temel çizgiyle onun yerini alırsınız.

### Değişimi tanımlı bir süreç ve uygun kurullarla kontrol edin

Kontrollü öğelere yapılan değişiklikleri tanımlı bir yoldan geçirin: öneri, etki değerlendirmesi, onay, uygulama ve doğrulama. Daha yüksek riskli öğeler için bir değişikliği yetkilendirmeden önce maliyeti, riski ve takvimi tartan bir [değişiklik kontrol kurulu](https://en.wikipedia.org/wiki/Change_control_board) (DKK) kullanın. Kurulu doğru boyutlandırın: rutin kod değişiklikleri için hafif otomatik bir kapı ve temel çizgilere, arayüzlere ya da düzenlenen davranışa dokunan değişiklikler için resmi, işlevler arası bir DKK. Her kararı ve ardındaki gerekçeyi kaydedin ve önemli yapılandırma kararlarını gerekçenin hayatta kalması için karar kayıtlarına (bölüm 1.6) bağlayın.

### Yapılandırma durum muhasebesini sürdürün

Her yapılandırma öğesinin doğru, sorgulanabilir bir kaydını tutun: güncel sürümü, ait olduğu temel çizgi ve ona uygulanan değişiklik talepleri. Bu durum muhasebesi, herhangi bir anda bir sürümün neyi içerdiğini ve oraya nasıl geldiğini cevaplamanızı sağlayan şeydir. Kaydı gerçeklikten sapan paralel bir elektronik tablo tutmak yerine kayıt araçlarınızdan (sürüm kontrolü, hat, yapıt kayıt defteri) otomatik üretin. Bu kayıt, gereksinimden değişikliğe, derlemeye ve dağıtıma izlenebilirliğin omurgasıdır.

### Yapılandırma denetimleri yürütün

İki şeyi düzenli bir takvimle doğrulayın. İşlevsel bir yapılandırma denetimi, yapılandırmanın gereksinimlerinin belirttiği gibi çalıştığını teyit eder. Fiziksel bir yapılandırma denetimi, teslim edilen yapıtların kayıtlı yapılandırmayla eşleştiğini teyit eder: derlemenin kayıtlı kaynaktan ve bağımlılıklardan geldiğini ve hesaba katılmamış hiçbir şey içermediğini. Bunun mümkün olduğunca çoğunu otomatikleştirin: [yeniden üretilebilir derlemeler](https://en.wikipedia.org/wiki/Reproducible_builds), yapıt sağlama toplamları, yazılım malzeme listeleri (SBOM) ve kaynak doğrulamaları denetimi elle incelemeden sürekli bir kontrole çevirir.

### Sürümleri ve teslimatı kontrollü olaylar olarak yönetin

Bir sürümü, tekrarlanabilir bir süreçle teslim edilen belirli, tanımlanmış bir temel çizgi olarak ele alın. Sürümlerinizi açıkça sürümleyin, tam olarak nelerin dahil olduğunu tarif eden bir manifesto ya da malzeme listesi üretin ve sürümden kaynak revizyonuna ve dağıtılmış yapıta eşlemeyi kaydedin. Akış aşağısındaki herkesin bütünlüklerini doğrulayabilmesi için yayımlanan yapıtları imzalayın ve sağlama toplamı alın. Ortamlar arası terfinin kendisi kontrollü, kaydedilmiş ve geri alınabilir olsun diye sürüm yönetimini teslimat hattına (bölüm 8.1) bağlayın.

### YYY araçlarını seçin ve entegre edin

Yalnızca disipline güvenmek yerine tanımlamayı, kontrolü, muhasebeyi ve denetimi otomatikleştiren araçlara yaslanın: kaynak için sürüm kontrolü, ikililer için yapıt ve imaj kayıt defterleri, derlemeler için değişmez bir hat, ortamlar için kod olarak altyapı ve kaynak için bağımlılık ve SBOM araçları. Tek bir değişikliğin commit'ten dağıtılmış sürüme izlenebilir biçimde akması için bunları bağlayın. Aradığınız, yapılandırma kaydının ayrı bir büro angaryası değil, işi yapmanın yan ürünü olduğu bir araç zinciridir.

## Ödünleşimler: artılar ve eksiler

| Seçim | Artılar | Eksiler |
|---|---|---|
| Resmi değişiklik kontrol kurulları | Güçlü yetkilendirme ve denetim izi; değişimden önce tartılan risk | Daha yavaş verim; rutin değişikliklere uygulanırsa yük |
| Hafif otomatik kapılar | Hızlı akış; düşük yük; çok sayıda değişikliğe ölçeklenir | Yüksek riskli temel çizgiler için daha zayıf; daha az müzakere |
| Katı değişmez temel çizgiler | Yeniden üretilebilir, denetlenebilir referans noktaları | Disiplin ve araç gerektirir; aşırı kullanılırsa sürtünme |
| Otomatik durum muhasebesi | Doğru, her zaman güncel kayıt; denetime hazır | Baştan araç ve entegrasyon yatırımı |
| Elle yapılandırma kayıtları | Başlaması basit; araç gerekmez | Gerçeklikten sapar; ölçekte ve denetim altında başarısız olur |

Merkezi ödünleşim kontrol ile akış arasındadır. Ağır değişiklik kontrolü güçlü güvence verir ama teslimatı yavaşlatır. Hafif kontrol hızlı akar ama izlenebilirliği zayıflatır. Cevap küresel olarak birini seçmek değildir; kontrolü riske göre katmanlamaktır: rutin değişiklikleri hızlı kapılardan otomatikleştirin ve resmi kurulları ve değişmez temel çizgileri yetkilendirme ve denetlenebilirliğin gerçekten önemli olduğu öğelere saklayın. İkinci ödünleşim, baştaki araç yatırımı ile süregelen büro maliyeti ve denetim riski arasındadır. Otomatik muhasebe kurmak daha pahalıdır ve yaşamak çok daha ucuzdur.

## Takımınızla tartışılacak sorular

1. **Yapılandırma öğesi listemize tam olarak ne ait ve yeni bir şey ortaya çıktığında karar kimin?** YYY yalnızca kontrollü öğelerin listesi davranışı gerçekten belirleyen şeylerin kümesiyle eşleşirse işler ve büyük bir sistemde o küme çoğu takımın düşündüğünden daha büyüktür: kaynak, bağımlılıklar, derleme betikleri, kapsayıcı imajları, altyapı tanımları, şemalar, özellik bayrakları ve yazılımın ne yaptığını sessizce değiştiren yapılandırma verisi. Kimse listeye sahip değilse bayatlar ve sizi üretimde düşüren öğe, kimsenin kontrol etmeyi düşünmediği tek şey çıkar. Mevcut envanterinizi toplantıya getirin ve içinde eksik olan davranış belirleyici öğeleri arayın. Sorumlu bir sahip (bir yapılandırma yöneticisi ya da adı konmuş bir takım) atayın; böylece yeni bir öğe eklemek kaza değil bilinçli bir karar olsun, çünkü herkesin işi olan YYY kimsenin işi değildir.

2. **Dağıtılmış bir yapıtın düşündüğümüz kaynaktan ve hattan geldiğini kanıtlayabilir miyiz ve bu kanıt kurcalamadan sağ çıkar mı?** Yeniden üretilebilirlik ve izlenebilirlik YYY'nin tüm amacıdır ve sorunun keskin hali, çalışan ikiliyi belirli bir commit'e ve derleme çalıştırmasına iddia değil kanıtla bağlayıp bağlayamayacağınızdır. Düzenlemeye tabi ya da yüksek değerli bir sistemde bu aynı zamanda tedarik zinciri savunmanızdır: imzalı kaynak doğrulamaları, yapıt sağlama toplamları ve bir yazılım malzeme listesi "oldukça eminiz"i bir denetçinin ya da olay müdahalecisinin doğrulayabileceği bir şeye çevirir. Son sürümünüzü getirin ve dağıtılmış yapıttan onaylı değişikliğe geriye doğru yürümeyi deneyin. Herhangi bir halka kayıtlı, doğrulanabilir bir bağ değil de elle yapılmış bir iddiaysa, bir saldırganın ya da dürüst bir hatanın fark edilmeden bir şey sokabileceği yer orasıdır ve onu kapatmak, kaydın teslimatın yan ürünü olması için imzalamayı ve kaynak doğrulamayı hatta bağlamak demektir.

3. **Bugün herhangi biri bir sürümü yerinde düzenleyebiliyor mu ve bu, ona güvenme yeteneğimize ne yapar?** Bir temel çizgi yalnızca değişmezse yararlıdır: "sürüm" sonradan düzenlenebildiği anda onu artık yeniden üretemez ya da referans olarak güvenemezsiniz ve her akış aşağısı denetim arkeolojiye dönüşür. Klasik başarısızlık, doğrudan üretimde düzenlenen yapılandırma ya da sessizce taşınan bir etikettir; zararsız hissettiren ve bir sürümü sonradan yeniden kurmayı imkansız kılan tam da kısayol budur. Toplantıya dürüst cevabı getirin: dağıtılmış bir temel çizgiyi değişiklik sürecinden geçmeden değiştirme erişimi kimde ve bu oldu mu? Çözüm, temel çizgileri gerçekten değişmez yapmak ve her değişikliği öneri, etki değerlendirmesi, onay ve doğrulamadan geçirmektir; titizliği katmanlayarak rutin değişiklikler hızlı otomatik kapılardan akarken temel çizgi ve düzenlenen değişiklikler bir kurula gider.

4. **Yapılandırma durum muhasebemiz kayıt araçlarımızdan otomatik mi üretiliyor yoksa elle mi tutuluyor ve gerçekte dağıtılandan ne kadar saptı?** Durum muhasebesi, herhangi bir anda bir sürümün neyi içerdiğini ve oraya nasıl geldiğini cevaplamanızı sağlayan kayıttır ve büyük bir sistemde o kayıt yalnızca paralel bir elektronik tabloya yazılmak yerine işten dökülürse güvenilirdir. Karşıt çekim, elle tutulan bir defterin başlamak için ucuz ve esnek hissettirmesidir; otomatikleştirmek ise sürüm kontrolünü, hattı ve yapıt kayıt defterini, kaydın teslimatın yan ürünü olması için entegre etmek demektir. Bugün güvendiğiniz defteri getirin, rastgele üç yakın tarihli sürüm seçin ve kayıtlı sürümlerin, temel çizgilerin ve uygulanan değişiklik taleplerinin araçların gönderildiğini söylediğiyle eşleşip eşleşmediğini kontrol edin. Bir kurumsal ya da kamu programı için gerçeklikten ayrışan bir durum kaydı bir düzen sorunu değil, gerçekleşmeyi bekleyen bir denetim bulgusudur, çünkü tek bir boşluğu yakalayan bir denetçi tüm anlatıya güvenmeyi bırakır ve sizden onu elle yeniden kurmanızı ister.

5. **Değişiklik kontrolümüz riske göre katmanlanmış mı, yoksa dokunduğu şeyden bağımsız olarak her değişikliği aynı tören düzeyi mi yönetiyor?** Kontrol ve akış birbirine karşı çeker: resmi bir değişiklik kontrol kurulu bir değişikliği yetkilendirmeden önce maliyeti, riski ve takvimi tartar, ama bu töreni rutin bir kod ince ayarına uygulamak yalnızca gecikme ekler; paylaşılan bir temel çizgiyi ya da düzenlenen bir ödeme akışını hızlı otomatik bir kapıdan geçirmek ise müzakereyi tam da ihtiyaç duyduğunuz yerden kaldırır. Başarısızlık biçimleri simetriktir: insanların dolanmayı öğrendiği tekdüze ağırlık ya da yüksek riskli bir değişikliğin incelenmeden geçmesine izin veren tekdüze gevşeklik. Geçen çeyreğin değişikliklerinden her birinin neye dokunduğuna göre sıralanmış bir örnek getirin ve aldığı titizliğin gerçekten riskiyle eşleşip eşleşmediğini kontrol edin. Düzenlemeye tabi ya da kamu ortamında hangi öğe sınıflarının işlevler arası bir kurula ulaşması gerektiğini ve hangilerinin otomatik kapılardan akabileceğini adlandırın ve bu katmanlamayı açıkça kaydedin, çünkü "muhakeme kullanıyoruz" bir denetçinin ya da gözetim organının doğrulayabileceği bir kontrol değildir.

6. **İşlevsel ve fiziksel bir yapılandırma denetimini en son ne zaman yürüttük ve kanıtın ne kadarı yeniden kurulum değil canlı kayıt olurdu?** İşlevsel bir yapılandırma denetimi sistemin gereksinimlerin belirttiği gibi çalıştığını, fiziksel bir yapılandırma denetimi ise teslim edilen yapıtların kayıtlı yapılandırmayla eşleştiğini ve hesaba katılmamış hiçbir şey içermediğini teyit eder; onları atlayın ve temel çizgilerinizin ve durum muhasebenizin dürüst olduğuna hiç kontrol etmeden güveniyorsunuz demektir. Gerilim maliyettir: elle denetimler yavaş ve acı vericidir, takımların onları ertelemesinin nedeni tam olarak budur ve çıkış yolu, doğrulamanın sürekli olması için kontrolleri yeniden üretilebilir derlemeler, yapıt sağlama toplamları, yazılım malzeme listeleri ve kaynak doğrulamalarıyla otomatikleştirmektir. En son sürümünüzü getirin ve anında gereksinimden değişikliğe, derlemeye ve dağıtıma izi ve yapıttan kaynağa kanıtı üretmeyi deneyin. Kurumsal ve kamu programları için bu kanıt izi sertifikasyon ve gözetimin talep ettiği şeydir; bu yüzden dürüst soru, yarınki denetimin zaten elinizde olan kayıtlardan mı yoksa karşılayamayacağınız bir arkeoloji alıştırmasından mı cevaplanacağıdır.

## Sektör merceği

**Girişim.** YYY'yi hafif ama gerçek tutun. Kaynağı, altyapı tanımlarını ve yapılandırma verisini sürüm kontrolüne koyun ve her sürümü elle bir araya getirilmiş yapıt yerine tek bir hattın ürettiği etiketli bir derleme yapın. Boyutunuzda fazla olan değişiklik kontrol kurullarını ve resmi temel çizgileri atlayın, ama kimsenin yapılandırmayı doğrudan üretimde düzenlemesine asla izin vermeyin, çünkü bir müşteri gelecek salı bir hata bulduğunda bir sürümü yeniden üretilemez kılan tek kısayol budur.

**Küçük işletme.** Yapılandırma yöneticisi ve sıkı bir bütçe olmadan, size YYY'yi neredeyse bedavaya veren araçlara yaslanın: barındırılan bir sürüm kontrolü platformu, yerleşik hattı ve bir yapıt kayıt defteri; böylece yapılandırma kaydı kadrolamanız gereken bir iş değil, bir yan ürün olur. Bu yeteneği özel bir süreç inşa etmek yerine zaten ödediğiniz araçlara gömülü satın alın. Kıt dikkatinizi en önemli iki alışkanlığa harcayın: yeniden üretilebilir etiketli sürümler ve davranış değiştiren yapılandırmayı elle üretim düzenlemelerinden uzak tutmak.

**Kurumsal.** Sorun birçok takım boyunca tutarlılıktır: paylaşılan bir YYY planı, ortak bir yapılandırma öğesi sınıflandırması, katmanlı değişiklik kontrolü ve sürüm kontrolünden, yapıt kayıt defterinden ve hattan otomatik üretilen durum muhasebesi. Resmi değişiklik kontrol kurullarını ve değişmez temel çizgileri paylaşılan platform ve düzenlenen akışlar için saklayın, rutin değişikliklerin otomatik kapılardan akmasına izin verin ve imzalı kaynak doğrulamasını ve SBOM'ları standartlaştırın; böylece herhangi bir takımın sürümü izlenebilir ve herhangi bir denetçi bir yeniden kurulum görevlendirmek yerine canlı bir kaydı sorgulayabilir.

**Kamu.** Tedarik kuralları, şeffaflık ve kamusal hesap verebilirlik süreci biçimlendirir. IEEE 828 gibi tanınmış bir standarda hizalı resmi bir YYY planını izleyin, yapılandırma öğelerini sözleşmesel dönüm noktalarında temel çizgiye alın ve kontrollü bir temel çizgiye yapılan her değişikliği etkiyi, kararı ve gerekçeyi kaydeden bir kuruldan geçirin. Teslim edilen yapıtların kontrollü girdilerden yeniden üretilebilir, sağlama toplamlı ve onaylı gereksinimden teslim edilen derlemeye uçtan uca izlenebilir olmasını isteyin; çünkü o belgelenmiş kanıt izi tam olarak sertifikasyonun, denetimin ve kamusal gözetimin talep ettiği şeydir.

## Örnekler

**Girişim.** Altı kişilik bir girişim YYY'sini hafif ama gerçek tutar: kaynak, altyapı tanımları ve yapılandırma verisi sürüm kontrolünde yaşar ve her sürüm elle bir araya getirilmek yerine aynı hattın ürettiği etiketli, sürümlü bir derlemedir. Bir müşteri geçen salı ortaya çıkan bir hata bildirdiğinde, tahmin etmek yerine dakikalar içinde dağıtılmış yapıtı tam commit'e izlerler. Boyutlarında fazla olan değişiklik kontrol kurullarını ve resmi temel çizgileri atlarlar, ama kimsenin yapılandırmayı doğrudan üretimde düzenlemesine izin vermezler, çünkü bir sürümü sonradan yeniden üretilemez kılan o tek kısayoldur.

**Kurumsal.** Büyük bir finansal hizmetler şirketi tüm dağıtılabilir yapıtları, altyapı tanımlarını ve yapılandırma verisini yapılandırma kontrolü altına alır. Her sürüm, üretilmiş bir yazılım malzeme listesiyle değişmez, sürümlü bir temel çizgidir ve her dağıtılmış yapıt onu belirli bir kaynak revizyonuna ve hat çalıştırmasına bağlayan imzalı bir kaynak doğrulaması taşır. Rutin uygulama değişiklikleri otomatik hat kapılarından akarken, paylaşılan platform temel çizgilerine ya da düzenlenen ödeme akışlarına yapılan değişiklikler bir değişiklik kontrol kuruluna gider. Durum muhasebesi sürüm kontrolünden, yapıt kayıt defterinden ve hattan otomatik üretilir; böylece denetçiler yeniden kurulum istemek yerine canlı bir kaydı sorgular.

**Kamu.** Bir savunma programı IEEE 828'e hizalı resmi bir YYY planını izler. Yapılandırma öğeleri listelenir ve sözleşmesel dönüm noktalarında temel çizgiye alınır ve bir değişiklik kontrol kurulu kontrollü bir temel çizgiye yapılan her değişikliği yetkilendirir; etkiyi, kararı ve gerekçeyi kaydeder. İşlevsel yapılandırma denetimleri teslim edilen sistemin belirtilen gereksinimleri karşıladığını, fiziksel yapılandırma denetimleri ise teslim edilen yapıtların kayıtlı yapılandırmayla tam olarak eşleştiğini teyit eder. Sürümler kontrollü girdilerden yeniden üretilebilir, sağlama toplamlı ve onaylı gereksinimden değişiklik talebine ve teslim edilen derlemeye uçtan uca izlenebilirdir; bu tam olarak sertifikasyonun ve gözetimin talep ettiği kanıt izidir.

## İş gerekçesi: motivasyonlar, YG ve TSM

YYY, bir sistemin ömrü boyunca riski ve maliyeti kontrol etmek için vardır. Getiri yeniden üretilebilirlik ve izlenebilirlikten gelir: herhangi bir sürümü yeniden oluşturabilir, kusurları onlara yol açan değişikliklere izleyebilir ve denetim sorularını arkeoloji yerine kayıtlardan cevaplayabilirsiniz. Bu, olay teşhis süresini kısaltır, denetimlerin maliyetini ve uzunluğunu azaltır ve kimsenin neyin çalıştığını ya da nasıl yeniden inşa edileceğini söyleyemediği pahalı başarısızlık sınıfını önler.

Toplam sahip olma maliyeti otomasyondan yanadır. Elle yapılandırma kayıtları başlamak için ucuzdur ve sürdürmek için giderek pahalıdır ve tam da en çok ihtiyaç duyduğunuzda, bir olay ya da denetim sırasında, gerçeklikten saptıkları için başarısız olurlar. Otomatik tanımlama, muhasebe ve denetim baştan daha pahalıdır, ama yapılandırma kaydını teslimat hattının neredeyse bedava bir yan ürününe çevirir. Gerekçeyi liderliğe sunmak için YYY'yi sürümleri yeniden üretilebilir ve değişiklikleri denetlenebilir kılan kontrol olarak çerçeveleyin ve onu yeniden üretilemez sürümlerin, uzayan denetimlerin ve kontrolsüz değişimin uyum riskinin maliyetine karşı tartın.

## Anti-kalıplar ve tuzaklar

- **Kabile bilgisiyle yapılandırma:** bir sürümün gerçek içeriği hiçbir kayıtta değil, yalnızca bir mühendisin kafasında yaşar.
- **Değişken temel çizgiler:** "sürüm" yerinde düzenlenir; bu yüzden artık yeniden üretilemez ya da referans olarak güvenilemez.
- **Kontrolsüz yapılandırma verisi:** kod sürüm kontrolündedir ama davranışını değiştiren yapılandırma üretimde geçici olarak düzenlenir.
- **Değişiklik kontrolü tiyatrosu:** her şeyi lastik damgalayan, gerçek bir inceleme eklemeden gecikme ekleyen bir kurul.
- **Elle durum muhasebesi:** gerçekte dağıtılandan sessizce ayrışan bir sürüm elektronik tablosu.
- **Yeniden üretilemez derlemeler:** kontrollü girdilerden yeniden inşa edilemeyen sürümler; bu yüzden denetimler ve yeniden inşalar tahmine dönüşür.
- **İzlenemeyen sürümler:** dağıtılmış yapıttan kaynak revizyonuna, değişiklik talebine ve onaya eşleme yok.

## Olgunluk modeli

- **Düzey 1 (Başlangıç):** YYY gelişigüzel ve reaktiftir. Yalnızca kaynak kontrol altındadır; sürümler elle bir araya getirilir; temel çizgi yoktur, dağıtılanın güvenilir bir kaydı yoktur ve geçmiş bir derlemeyi yeniden üretmenin yolu yoktur.
- **Düzey 2 (Geliştirme):** Temel uygulamalar vardır ama takımdan takıma değişir. Bazı sistemler yapılandırma öğelerini ve bir değişiklik sürecini tanımlar ve sürümlerini sürümler, temel çizgiler orada burada vardır, ama kayıtlar kısmen elle tutulur ve kontrolün titizliği kuruluş genelinde tutarsızdır.
- **Düzey 3 (Standartlaştırma):** Uygulamalar belgelenir ve kuruluş genelinde uygulanır. Ortak bir yapılandırma öğesi sınıflandırması, değişmez temel çizgiler, katmanlı değişiklik kontrolü ve durum muhasebesi oluşturulmuş ve büyük ölçüde otomatiktir; sürümler yeniden üretilebilir ve izlenebilirdir ve denetimler hafızayla değil araçlarla desteklenir.
- **Düzey 4 (Yönetme):** YYY veriyle ölçülür ve kontrol edilir. Yeniden üretilebilirlik oranı, gereksinimden dağıtılmış yapıta izlenebilirlik kapsamı, her kontrol katmanından değişiklik öncül süresi, yapılandırma kayması olayları ve denetim bulguları temel çizgilere ve hedeflere karşı izlenir. Sapmalar düzeltmeyi tetikler ve her ilerle ya da dur kararı iddiaya değil bu kanıta dayanır.
- **Düzey 5 (Orkestrasyon):** YYY sürekli iyileştirilir ve kuruluş genelinde bütünleşir. Yeniden üretilebilir derlemeler, SBOM'lar, kaynak doğrulamaları ve canlı durum muhasebesiyle tam otomatik ve sürekli doğrulanan süreç teslimata, güvenliğe ve denetime örülür ve risk ve teslimat sonuçları kaydıkça uyum sağlar; kontrolleri kanıta dayanarak emekliye ayırır ve yeniden kapsamlar.

## Tartışma fikirleri

- Son sürümünüzü bugün kontrollü girdilerden tam olarak yeniden üretebilir misiniz ve ne kadar sürerdi?
- Hangi yapılandırma öğeleri davranışı belirliyor ama gerçekte kontrol altında değil, özellikle yapılandırma verisi ve altyapı?
- Değişiklik kontrolünüz riske göre mi katmanlanmış, yoksa her yerde tekdüze yük mü ya da tekdüze gevşeklik mi ekliyor?
- Yapılandırma kaydınız nerede yaşıyor ve gerçekte dağıtılandan ne kadar saptı?
- Yarın bir denetimde hangi kanıtı üretebilirdiniz ve ne kadarı kayıt değil yeniden kurulum olurdu?
- Yeniden üretilebilir derlemeler, SBOM'lar ve kaynak doğrulamaları denetimlerinizin otomatik doğrulayabileceği şeyi nasıl değiştirir?

## Önemli çıkarımlar

- YYY tüm yapılandırmayı (kod, bağımlılıklar, altyapı ve yapılandırma verisi) kontrol eder, yalnızca kaynağı değil.
- Temel çizgiler değişmez referans noktalarıdır; değişim onlara karşı yetkilendirilir ve kaydedilir, önlenmez.
- Durum muhasebesi herhangi bir anda bir sürümün neyi içerdiğini ve oraya nasıl geldiğini cevaplamanızı sağlamalıdır.
- Denetimler inşa edilen ve teslim edilenin kayıtlı yapılandırmayla ve onaylı gereksinimlerle eşleştiğini doğrular.
- Kontrolü riske göre katmanlayın ve tanımlamayı, muhasebeyi ve denetimi otomatikleştirin; böylece kayıt teslimatın yan ürünü olur.

## Kaynaklar ve ileri okuma

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Configuration Management knowledge area
- IEEE Std 828, *Standard for Configuration Management in Systems and Software Engineering*
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (configuration management process)
- Jez Humble and David Farley, *Continuous Delivery*
- Bob Aiello and Leslie Sachs, *Configuration Management Best Practices: Practical Methods that Work in the Real World*
- NIST guidance on software supply chain security, software bills of materials (SBOM), and artifact provenance
- CNCF and open standards for build provenance and attestation (as reference frameworks)
