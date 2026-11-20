# 12.2 Kontrol listeleri

Bu kontrol listeleri pratik, kullanıma hazır hızlı başvurulardır. Herhangi bir kontrol listesini bir çekme isteği şablonuna, bir wiki sayfasına, bir bilet kaydına ya da bir inceleme toplantısı gündemine kopyalayın ve maddeleri kendi bağlamınıza uyarlayın. Her maddeyi, bir kişinin doğrulayıp evet ya da hayır diye cevaplayabileceği bir şey olarak ele alın. Kontrol listesi bir hafıza yardımcısı ve ortak bir standarttır, muhakemenin yerine geçmez; geçerli olmayan maddeleri silin, alanınızın gerektirdiği maddeleri ekleyin.

Bunları iyi kullanmak için rehberlik:

- Kontrol listelerini insanların gerçekten tamamlayabileceği kadar kısa tutun. Bir kontrol listesi düzenli olarak atlanıyorsa fazla uzun ya da fazla genel demektir.
- Bir makinenin doğrulayabileceği her maddeyi otomatikleştirin (biçimlendirme, testler, taramalar); böylece insanlar dikkatlerini muhakeme gerektiren maddelere harcar.
- Kontrol listelerinizi sürümleyin ve düzenli aralıklarla gözden geçirin. Hiç değişmeyen bir kontrol listesi büyük olasılıkla kullanılmıyordur.
- Süreciniz için önemli olduğunda engelleyici maddelerle tavsiye niteliğindeki maddeleri birbirinden ayırın.

## Kod incelemesi kontrol listesi

Başkasının değişikliğini inceleyen gözden geçiren için.

- [ ] Değişiklik, açıklamasının ve bağlantılı biletin söylediğini yapıyor.
- [ ] Kapsam tek bir mantıksal kaygıya odaklı; ilgisiz değişiklikler ayrılmış.
- [ ] Tasarım mevcut mimariye uyuyor ve kolayca kaçınılabilecek bir bağlaşım getirmiyor.
- [ ] Yalnızca mutlu yol değil, uç durumlar, hata yolları ve başarısızlık kipleri de ele alınmış.
- [ ] Testler var, anlamlı ve davranış gerilediğinde başarısız olurlar.
- [ ] Adlandırma, yapı ve yorumlar kodu gelecekteki bir okuyucu için anlaşılır kılıyor.
- [ ] Hiçbir gizli bilgi, kimlik bilgisi, belirteç ya da kişisel veri commit edilmemiş.
- [ ] Güvenlik açısından hassas girdi uygun biçimde doğrulanıyor, kodlanıyor ya da parametreleştiriliyor.
- [ ] Herkese açık arayüzler, sözleşmeler ve geriye dönük uyumluluk korunuyor ya da bilerek sürümleniyor.
- [ ] Günlükleme, ölçümler ve hata raporlama değişikliği üretimde işletmek için yeterli.
- [ ] Dokümantasyon, işletim el kitapları ve yapılandırma değişikliğe uyacak biçimde güncellenmiş.
- [ ] Geri bildirim engelleyici sorunlar ve öneriler olarak ayrılmış ve kişiyi değil kodu konu alacak biçimde yazılmış.

## Çekme isteği yazarı kontrol listesi

İnceleme istemeden önce yazar için.

- [ ] Çekme isteği, tek oturumda dikkatle incelenebilecek kadar küçük ve odaklı.
- [ ] Açıklama neyin değiştiğini, nedenini ve nasıl doğrulandığını belirtiyor.
- [ ] Bağlantılı bilet, sorun kaydı ya da tasarım belgesi gözden geçirenlere gerekli bağlamı veriyor.
- [ ] Tüm otomatik denetimler yerelde ya da CI'da geçiyor (derleme, lint, biçimlendirme, testler, taramalar).
- [ ] Yeni ve değişen davranış testlerle kapsanıyor.
- [ ] Mekanik yeniden düzenlemeler davranış değişikliklerinden ayrılmış.
- [ ] Kendi kendine inceleme tamam: kendi diff'inizi satır satır okudunuz.
- [ ] Hata ayıklama kodu, yorum satırına alınmış bloklar, gizli bilgiler ya da başıboş dosyalar kalmamış.
- [ ] Veritabanı geçişleri, özellik bayrakları ve yapılandırma değişiklikleri belgelenmiş ve geri alınabilir.
- [ ] Geriye dönük uyumsuz değişiklikler bir geçiş yoluyla birlikte açıkça belirtilmiş.
- [ ] İncelemeye yardımcı olacak yerlerde ekran görüntüleri, kayıtlar ya da örnek çıktılar eklenmiş.
- [ ] Doğru gözden geçirenler ve gereken rol tabanlı onaylayıcılar istenmiş.

## Bitti tanımı

Bir iş öğesinin tamamlanmış sayılmadan önce karşılaması gereken ortak standart.

- [ ] Biletteki kabul ölçütlerinin hepsi karşılanmış ve gösterilebilir.
- [ ] Kod meslektaş incelemesinden geçmiş ve gereken gözden geçirenler tarafından onaylanmış.
- [ ] Otomatik testler yazılmış, geçiyor ve değişiklikle birlikte birleştirilmiş.
- [ ] Kod ana hatta birleştirilmiş ve boru hattından sorunsuz dağıtılıyor.
- [ ] Üzerinde anlaşılan önem eşiğindeki bilinen kusurların hiçbiri açık kalmamış.
- [ ] Dokümantasyon, yardım metinleri ve işletim el kitapları güncellenmiş.
- [ ] Gözlemlenebilirlik yerinde: ilgili günlükler, ölçümler ve uyarılar var.
- [ ] Güvenlik ve gizlilik etkileri değerlendirilmiş ve ele alınmış.
- [ ] Kullanıcıya dönük yerlerde değişiklik için erişilebilirlik gereksinimleri karşılanmış.
- [ ] Özellik bayrakları yapılandırılmış ve kullanıma açma planı üzerinde anlaşılmış.
- [ ] Ürün sahibi ya da paydaş sonucu kabul etmiş.
- [ ] Her takip işi örtük bırakılmayıp izlenen biletler olarak kaydedilmiş.

## Üretime çıkış / canlıya alma hazırlığı

Önemli bir değişikliği ya da yeni bir hizmeti üretime göndermeden önce.

- [ ] Kullanıma açma planı, aşamalı ya da kanarya adımları ve başarı ölçütleriyle birlikte belgelenmiş.
- [ ] Geri alma planı belgelenmiş, denenmiş ve hızla uygulanabilir.
- [ ] Kapasite ve yük testleri sistemin beklenen ve en yüksek talebi karşıladığını gösteriyor.
- [ ] İzleme, panolar ve uyarılar canlı ve lansmandan önce doğrulanmış.
- [ ] Nöbet kapsamı planlanmış ve müdahale edenler sistemi tanıyor.
- [ ] En olası başarısızlık ve işletim senaryoları için işletim el kitapları var.
- [ ] Bağımlılıklar, entegrasyonlar ve üçüncü taraflar hazır olarak doğrulanmış ve hız sınırları anlaşılmış.
- [ ] Güvenlik incelemesi ve gereken onaylar tamamlanmış.
- [ ] Varsa veri geçişi uçtan uca test edilmiş ve doğrulanmış bir geri çekilme yolu var.
- [ ] Özellik bayrakları değişikliğin yeniden dağıtım gerektirmeden devre dışı bırakılmasına izin veriyor.
- [ ] Gereken yerlerde hukuki, gizlilik ve uyumluluk onayları alınmış.
- [ ] İletişim planı paydaşları, desteği ve müşterileri kapsıyor.
- [ ] Gitme/gitmeme kararı, adı belli sahipler tarafından açık ölçütlere göre veriliyor.

## Güvenlik incelemesi / tehdit modeli kontrol listesi

Bir değişikliğin ya da sistemin güvenlik duruşunu değerlendirmek için.

- [ ] Güven sınırları ve veri akışları belirlenmiş ve belgelenmiş.
- [ ] Kimlik doğrulama, gerektiren her giriş noktasında zorunlu kılınıyor.
- [ ] Yetkilendirme denetimleri her eylem ve kaynak için en az ayrıcalık ilkesini uyguluyor.
- [ ] Tüm dış girdi doğrulanıyor ve çıktı hedefine göre kodlanıyor.
- [ ] Gizli bilgiler yönetilen bir kasada saklanıyor, asla kodda ya da yapılandırmada değil, ve döndürülebiliyor.
- [ ] Veri, sınıflandırmanın gerektirdiği şekilde aktarım sırasında ve beklemede şifreli.
- [ ] Bağımlılıklar bilinen açıklar için taranıyor ve güncel tutuluyor.
- [ ] Güvenilmeyen girdi için enjeksiyon, serileştirmeyi geri alma ve SSRF riskleri azaltılmış.
- [ ] Güvenlikle ilgili olaylar hassas veriyi kaydetmeden günlüğe alınıyor.
- [ ] Hız sınırlama, kotalar ve kötüye kullanım korumaları açık uç noktaları koruyor.
- [ ] Hata iletileri yığın izlerini, iç ayrıntıları ya da hassas bilgiyi sızdırmıyor.
- [ ] STRIDE ya da benzeri yöntemle belirlenen tehditler, azaltma önlemleri ya da kabul edilen riskle birlikte kaydedilmiş.
- [ ] Güvenlik testi (SAST, DAST ya da sızma testi) planlanmış ya da tamamlanmış.

## Gizlilik ve veri koruma (DPIA tarzı) kontrol listesi

Kişisel ya da hassas veri içeren işleme için.

- [ ] Toplanan kişisel veri envantere alınmış, sınıflandırılmış ve gerekenle sınırlanmış.
- [ ] Her işleme amacı için hukuki dayanak ya da yetki belgelenmiş.
- [ ] Amaçla sınırlılık uygulanıyor: veri yalnızca belirtilen amaçlar için kullanılıyor.
- [ ] Saklama süreleri tanımlanmış ve silme ya da anonimleştirme otomatikleştirilmiş.
- [ ] Veri sahibi hakları (erişim, düzeltme, silme, taşınabilirlik) yerine getirilebiliyor.
- [ ] Dayanılan rıza varsa serbestçe verilmiş, belirli ve geri alınabilir.
- [ ] Üçüncü taraflar ve işleyiciler yeterli veri koruma şartlarıyla bağlı.
- [ ] Sınır ötesi aktarımların uygun bir hukuki aktarım mekanizması var.
- [ ] Kişisel veriye erişim kısıtlanmış, günlüğe alınıyor ve gözden geçiriliyor.
- [ ] Bireylere yönelik gizlilik riskleri değerlendirilmiş ve azaltılmış ya da üst makama iletilmiş.
- [ ] Veri ihlali tespit ve bildirim süreçleri tanımlanmış.
- [ ] Tasarımda ve varsayılan olarak gizlilik tercihleri özellik için belgelenmiş.
- [ ] Gereken yerlerde veri koruma görevlisi ya da gizlilik gözden geçireni onay vermiş.

## Erişilebilirlik (WCAG) kontrol listesi

WCAG ilkeleriyle uyumlu, kullanıcıya dönük arayüzler için.

- [ ] Tüm içeriğe yalnızca bir klavye kullanılarak ulaşılabiliyor ve içerik işletilebiliyor.
- [ ] Odak sırası mantıklı ve görünür bir odak göstergesi var.
- [ ] Metin renk karşıtlığı hedef oranı karşılıyor (gövde metni için genellikle 4,5:1).
- [ ] Görsellerin ve metin dışı içeriğin anlamlı alternatif metni var.
- [ ] Form alanlarının ilişkili etiketleri ve açık hata iletileri var.
- [ ] Başlıklar, yer işaretleri ve yapı anlamsal olarak işaretlenmiş.
- [ ] Etkileşimli bileşenler yardımcı teknolojiye doğru ad, rol ve durumu sunuyor.
- [ ] İçerik %200 yakınlaştırmada ve küçük ekranlarda yeniden akıyor ve kullanılabilir kalıyor.
- [ ] Zaman sınırları ayarlanabiliyor ve hareketli ya da kendiliğinden oynayan içerik duraklatılabiliyor.
- [ ] Renk bilgiyi iletmenin tek yolu değil.
- [ ] Medyanın altyazıları ve gereken yerlerde dökümleri ya da sesli betimlemesi var.
- [ ] Arayüz bir ekran okuyucuyla ve otomatik erişilebilirlik araçlarıyla test edilmiş.

## API tasarım incelemesi kontrol listesi

Bir API'yi yayımlamadan ya da değiştirmeden önce.

- [ ] Kaynak ve işlem adlandırması tutarlı ve öngörülebilir.
- [ ] Sözleşme makine tarafından okunabilir bir şemada belirtilmiş (örneğin OpenAPI).
- [ ] Sürümleme stratejisi tanımlanmış ve geriye dönük uyumluluk korunuyor ya da yönetiliyor.
- [ ] Sayfalama, süzme ve sıralama tutarlı kurallara uyuyor.
- [ ] Hata yanıtları tutarlı yapı, kod ve eyleme dönük iletiler kullanıyor.
- [ ] Kimlik doğrulama ve yetkilendirme her işlem için belirtilmiş.
- [ ] Girdi doğrulaması ve boyut sınırları tanımlanmış ve uygulanıyor.
- [ ] Yeniden denemelerin beklendiği işlemler için eş güçlülük tanımlanmış.
- [ ] Hız sınırları, kotalar ve kısıtlama davranışı belgelenmiş.
- [ ] Zaman aşımları, yeniden denemeler ve başarısızlık anlambilimi istemciler için açık.
- [ ] Yanıtlarda hassas veri ifşası en aza indirilmiş ve gerekçelendirilmiş.
- [ ] Dokümantasyon her işlem ve hata durumu için örnek içeriyor.
- [ ] Kullanımdan kaldırma politikası ve sonlandırma takvimleri tanımlanmış.

## Mimari karar (ADR) incelemesi kontrol listesi

Önerilen bir karar kaydını incelemek için.

- [ ] Bağlam ve çözülen sorun açıkça belirtilmiş.
- [ ] Karar, tek bir seçim olarak belirsizliğe yer bırakmadan ifade edilmiş.
- [ ] En az iki gerçekçi alternatif ele alınmış ve karşılaştırılmış.
- [ ] Hem olumlu hem olumsuz sonuçlar belgelenmiş.
- [ ] İşlevsel olmayan etkiler (başarım, güvenlik, maliyet, işletilebilirlik) ele alınmış.
- [ ] Karar mevcut ilkelerle ve önceki ADR'lerle uyumlu ya da onların yerini açıkça alıyor.
- [ ] Etkilenen takımlara ve paydaşlara danışılmış.
- [ ] Geri alınabilirlik ve değişim maliyeti değerlendirilmiş.
- [ ] Varsayımlar ve kısıtlar açık hale getirilmiş.
- [ ] Durum (önerildi, kabul edildi, yerini aldı) belirlenmiş ve tarihlendirilmiş.
- [ ] Karar bulunabilir durumda ve ilgili sistemlerden bağlantılı.
- [ ] Her takip eylemi ya da geçiş izlenen iş olarak kaydedilmiş.

## Olay müdahalesi kontrol listesi

Etkin bir üretim olayı sırasında.

- [ ] Olayı ilan edin ve tek bir olay komutanı atayın.
- [ ] Önemi, kapsamı ve müşteri etkisini değerlendirip iletin.
- [ ] Özel bir iletişim kanalı ve olay kaydı açın.
- [ ] Açık roller atayın: komutan, iletişim sorumlusu ve operasyon sorumlusu.
- [ ] Kök neden analizinden önce hafifletmeye ve hizmeti geri getirmeye öncelik verin.
- [ ] Paydaşlara belirli bir ritimle düzenli durum güncellemeleri gönderin.
- [ ] Olayların, eylemlerin ve kararların zaman çizelgesini onlar gerçekleştikçe kaydedin.
- [ ] Gerektiğinde ek müdahale edenlere ya da tedarikçilere yükseltin.
- [ ] Veri ya da mevzuat söz konusuysa hukuk, güvenlik ve uyumluluk ekiplerini bilgilendirin.
- [ ] Düzeltmeyi doğrulayın ve sistemin tamamen toparlandığını teyit edin.
- [ ] Olayı resmen kapatın ve çözümü duyurun.
- [ ] İnsanlar dağılmadan önce suçlamasız olay sonrası incelemeyi planlayın.

## Olay sonrası inceleme kontrol listesi

Bir olaydan sonraki geriye dönük inceleme için.

- [ ] İnceleme suçlamasız ve sistemlere ile katkıda bulunan etkenlere odaklı.
- [ ] Olayın olgusal, zaman damgalı bir zaman çizelgesi belgelenmiş.
- [ ] Müşteri ve iş etkisi ölçülmüş (süre, kapsam, maliyet).
- [ ] Tespit çözümlenmiş: sorunun nasıl ve ne zaman fark edildiği.
- [ ] Müdahale çözümlenmiş: neyin yardımcı olduğu ve neyin toparlanmayı yavaşlattığı.
- [ ] Yalnızca tek bir kök neden değil, katkıda bulunan nedenler belirlenmiş.
- [ ] Neyin ters gittiğinin yanı sıra neyin iyi gittiği de kaydedilmiş.
- [ ] Eylem maddeleri belirli, sahiplere atanmış ve son tarihleri var.
- [ ] Eylem maddeleri önlemeyi, tespiti ve hafifletmeyi ele alıyor.
- [ ] Takip maddeleri normal iş listesinde tamamlanana kadar izleniyor.
- [ ] Olay sonrası inceleme, başkalarının ondan öğrenebilmesi için geniş çapta paylaşılmış.
- [ ] Olaylar arasındaki sistemik örüntüler düzenli aralıklarla gözden geçiriliyor.

## Nöbet hazırlığı kontrol listesi

Birisi bir nöbet vardiyasına başlamadan önce.

- [ ] Müdahale eden, ihtiyaç duyduğu tüm sistemlere, panolara ve araçlara erişebiliyor.
- [ ] Uyarılar müdahale edene güvenilir biçimde ulaşıyor ve test edilmiş.
- [ ] Yükseltme yolları ve ikincil nöbetçi kişileri biliniyor ve güncel.
- [ ] En yaygın ve en ciddi uyarılar için işletim el kitapları var.
- [ ] Müdahale eden bu sistemler için oryantasyonu ya da gölge çalışmayı tamamlamış.
- [ ] Son değişiklikler, süren olaylar ve bilinen sorunlar devir teslim edilmiş.
- [ ] Gürültüyü ve yanlış çağrıları en aza indirmek için uyarı eşikleri ayarlanmış.
- [ ] Müdahale eden bir olayın nasıl ilan edileceğini ve komutana nasıl ulaşılacağını biliyor.
- [ ] Müdahale edenin çalışma ortamından üretime erişim mümkün.
- [ ] İletişim kanalları ve paydaş irtibat bilgileri belgelenmiş.
- [ ] Nöbet çizelgesi yayımlanmış ve kapsamda boşluk yok.
- [ ] Nöbet için ücretlendirme, beklentiler ve iş yükü sınırları açık.

## SLO tanımlama kontrol listesi

Bir hizmet düzeyi hedefi tanımlarken.

- [ ] SLO'nun koruduğu kullanıcı yolculuğu ya da yetenek açıkça belirlenmiş.
- [ ] Hizmet düzeyi göstergeleri (SLI'lar) açık, ölçülebilir nicelikler olarak tanımlanmış.
- [ ] SLI'lar mümkün olduğunda kullanıcının bakış açısından ölçülüyor.
- [ ] Hedef, %100 değil, kullanıcıların gerçekten ihtiyaç duyduğu düzeyde belirlenmiş.
- [ ] Ölçüm penceresi (örneğin yuvarlanan 28 gün) belirtilmiş.
- [ ] Hedeften türetilen hata bütçesi hesaplanmış ve anlaşılmış.
- [ ] Bir politika, hata bütçesi tükendiğinde ne olacağını tanımlıyor.
- [ ] SLI'lar için veri kaynakları güvenilir ve ölçümleme yapılmış.
- [ ] Uyarılar yalnızca eşik ihlallerine değil, yanma hızına bağlı.
- [ ] Sahipler ve paydaşlar SLO'nun gerçekçi ve anlamlı olduğunda anlaşmış.
- [ ] SLO belgelenmiş ve bir panoda görünür.
- [ ] Hizmet geliştikçe SLO'ları gözden geçirmek ve düzeltmek için bir takvim var.

## CI/CD boru hattı kontrol listesi

Sürekli entegrasyon ve teslimat boru hattı için.

- [ ] Her commit otomatik bir derleme ve test çalıştırmasını tetikliyor.
- [ ] Boru hattı hızlı başarısız oluyor ve sonuçları yazarlara açıkça bildiriyor.
- [ ] Lint, biçimlendirme ve statik analiz otomatik çalışıyor.
- [ ] Birim, entegrasyon ve ilgili uçtan uca testler boru hattında çalışıyor.
- [ ] Güvenlik ve bağımlılık taraması her derlemede çalışıyor.
- [ ] Derleme çıktıları sürümlenmiş, değişmez ve bir kayıt defterinde saklanıyor.
- [ ] Gizli bilgiler güvenli biçimde enjekte ediliyor ve günlüklerde asla yazdırılmıyor.
- [ ] Dağıtımlar otomatik ve ortamlar arasında tekrarlanabilir.
- [ ] Dağıtım stratejisi (kanarya, mavi-yeşil, kademeli) tanımlanmış ve kullanılıyor.
- [ ] Geri alma otomatik ya da belgelenmiş tek bir eylem.
- [ ] Boru hattı izinleri en az ayrıcalık ilkesine uyuyor ve denetlenebilir.
- [ ] Boru hattı yapılandırması sürüm kontrolünde kod olarak saklanıyor.
- [ ] Gereken yerlerde derleme kaynağı kaydı ve yazılım malzeme listesi üretiliyor.

## Kod olarak altyapı inceleme kontrol listesi

Kod olarak tanımlanmış altyapıyı incelemek için.

- [ ] Değişiklikler tamamen kodla ifade ediliyor ve boru hattı üzerinden uygulanıyor.
- [ ] Uygulamadan önce bir plan ya da deneme çalıştırması çıktısı inceleniyor.
- [ ] Durum, eşzamanlı değişiklikleri önlemek için kilitlemeyle güvenli biçimde saklanıyor.
- [ ] Kaynaklar adlandırma, etiketleme ve sahiplik kurallarına uyuyor.
- [ ] En az ayrıcalıklı IAM rolleri ve politikaları kullanılıyor; kaçınılabilecek yerlerde joker karakter yok.
- [ ] Ağ ifşası en aza indirilmiş; istenmeyen herkese açık erişim yok.
- [ ] Gizli ve hassas değerlere sabit kodlanmak yerine bir kasadan başvuruluyor.
- [ ] Depolama, veritabanları ve aktarım için şifreleme etkin.
- [ ] Değişiklikler eş güçlü ve yeniden uygulanması güvenli.
- [ ] Etki alanı anlaşılmış; yıkıcı değişiklikler açıkça belirtilmiş.
- [ ] Değişikliğin maliyet etkisi göz önüne alınmış.
- [ ] Modüller yeniden kullanılabilir, sürümlenmiş ve test edilmiş.
- [ ] Bant dışı değişiklikleri yakalamak için sapma tespiti yerinde.

## Yapay zeka/ML model yayın kontrol listesi

Bir makine öğrenmesi modelini üretime yayımlamadan önce.

- [ ] Modelin amaçlanan kullanımı, kapsamı ve sınırlılıkları belgelenmiş.
- [ ] Eğitim ve değerlendirme verisinin kaynağı, lisansı ve rızası doğrulanmış.
- [ ] Veri ve model sürümlenmiş ve yeniden üretilebilir.
- [ ] Başarım, temsil edici ve ayrı tutulmuş test verisi üzerinde değerlendirilmiş.
- [ ] Adalet ve yanlılık ilgili alt gruplar genelinde değerlendirilmiş.
- [ ] Model, mevcut modele ya da bir temel çizgiye karşı değerlendirilmiş.
- [ ] Başarısızlık kipleri, uç durumlar ve dağılım dışı davranış anlaşılmış.
- [ ] Güvenlik, kötüye kullanım ve zararlı çıktı riskleri değerlendirilmiş ve azaltılmış.
- [ ] Sapma, veri kalitesi ve başarım düşüşü için izleme yerinde.
- [ ] Önceki bir modele ya da kural tabanlı bir yola geri alma ya da yedek yol var.
- [ ] Sonuçları ağır kararlar için insan gözetimi ya da itiraz yolu sağlanmış.
- [ ] Gizlilik incelemesi eğitim verisini ve çıkarım girdilerini ve çıktılarını kapsıyor.
- [ ] Paydaşlar için bir model kartı ya da eşdeğer dokümantasyon yayımlanmış.

## Veri boru hattı kalitesi kontrol listesi

Analitiği ya da ürünleri besleyen bir veri boru hattı için.

- [ ] Kaynak veri şemaları doğrulanıyor ve şema değişiklikleri tespit ediliyor.
- [ ] Veri alımı geç gelen, yinelenen ve sırasız kayıtları doğru ele alıyor.
- [ ] Veri kalitesi denetimleri (bütünlük, benzersizlik, aralıklar) otomatik çalışıyor.
- [ ] Başarısız kayıtlar sessizce atılmak yerine karantinaya alınıyor ve görünür kılınıyor.
- [ ] Dönüşümler temsil edici ve uç durum girdileriyle test ediliyor.
- [ ] Boru hattı eş güçlü ve başarısızlıktan sonra yeniden çalıştırması güvenli.
- [ ] Çıktıların tazeliği ve gecikmesi beklentilere karşı izleniyor.
- [ ] Tüketiciler verinin nereden geldiğini bilsin diye soy ağacı belgelenmiş.
- [ ] Kişisel ve hassas veri uygun biçimde sınıflandırılmış, maskelenmiş ya da kısıtlanmış.
- [ ] Geriye dönük doldurma ve yeniden işleme destekleniyor ve belgelenmiş.
- [ ] Uyarılar sahiplere başarısızlıkları ve kalite ihlallerini bildiriyor.
- [ ] Saklanan veri üzerinde saklama ve silme politikaları uygulanıyor.
- [ ] Aşağı akış tüketicileri ve SLA'lar belgelenmiş.

## Açık kaynak alımı ve lisans incelemesi kontrol listesi

Bir açık kaynak bileşenini benimsemeden önce.

- [ ] Bileşenin lisansı belirlenmiş ve onaylı listede.
- [ ] Lisans yükümlülükleri (atıf, copyleft, bildirimler) anlaşılmış ve yerine getiriliyor.
- [ ] Lisansın dağıtım modelinizle uyumluluğu doğrulanmış.
- [ ] Proje etkin biçimde bakım görüyor ve sağlıklı bir topluluğu var.
- [ ] Bilinen açıklar denetlenmiş ve sürüm güncel.
- [ ] Bağımlılık ve geçişli bağımlılıkları envantere alınmış.
- [ ] Güvenlik duruşu ve geçmiş olay tarihçesi gözden geçirilmiş.
- [ ] Bileşen, önemli bir tekrar olmadan gerçek bir ihtiyacı karşılıyor.
- [ ] Bileşenin çıkış maliyeti ve yerine başkasının konabilirliği düşünülmüş.
- [ ] Bileşen yazılım malzeme listesine kaydedilmiş.
- [ ] Adı belli bir sahip güncellemeleri ve güvenlik duyurularını izlemekten sorumlu.
- [ ] Değiştirilmişse katkıyı geri verme ve dahili çatal politikalarına uyuluyor.

## Tedarikçi / üçüncü taraf riski kontrol listesi

Harici bir tedarikçiyi ya da hizmeti devreye almadan önce.

- [ ] İş ihtiyacı ve tedarikçinin erişeceği veri açıkça tanımlanmış.
- [ ] Tedarikçinin güvenlik duruşu değerlendirilmiş (sertifikalar, denetimler, anket).
- [ ] Veri işleme şartları, sahiplik ve çıkışta silme sözleşmede açık.
- [ ] Tedarikçinin alt işleyicileri ve veri konumları açıklanmış ve kabul edilebilir.
- [ ] İlgili mevzuata uyum doğrulanmış.
- [ ] Çalışma süresi, destek ve SLA taahhütleri belgelenmiş.
- [ ] İhlal bildirim yükümlülükleri ve süreleri sözleşmede yer alıyor.
- [ ] Erişim en az ayrıcalıkla sınırlanmış ve geri alınabilir.
- [ ] İş sürekliliği ve tedarikçi başarısızlığının etkisi değerlendirilmiş.
- [ ] Kilitlenmeyi önlemek için bir çıkış ve veri geçişi planı var.
- [ ] Maliyetler, yenileme şartları ve fiyat değişikliği maddeleri anlaşılmış.
- [ ] Tedarikçi, bir gözden geçirme tarihiyle risk kaydına eklenmiş.

## Kamu uyumluluğu (ATO / FedRAMP tarzı) hazırlık kontrol listesi

Çalışmak için resmi yetkilendirme gerektiren sistemler için.

- [ ] Sistem sınırı ve veri akışları tanımlanmış ve çizilmiş.
- [ ] Veri etki düzeyine ve hassasiyete göre kategorilere ayrılmış.
- [ ] Geçerli kontrol temel çizgisi seçilmiş ve uyarlanmış.
- [ ] Bir sistem güvenlik planı her kontrolün nasıl uygulandığını belgeliyor.
- [ ] Kontroller uygulanmış, kanıtlanmış ve plana eşlenmiş.
- [ ] Sürekli izleme ve açık taraması işler durumda.
- [ ] Bir eylem ve kilometre taşı planı açık bulguları giderilene kadar izliyor.
- [ ] Erişim denetimi, denetim günlüğü ve kimlik yönetimi gereksinimleri karşılıyor.
- [ ] Şifreleme onaylı algoritmaları ve doğrulanmış modülleri kullanıyor.
- [ ] Bir olay müdahale planı belgelenmiş ve denenmiş.
- [ ] Bir acil durum ve felaket kurtarma planı belgelenmiş ve denenmiş.
- [ ] Kontrollerin bağımsız bir değerlendirmesi ya da denetimi tamamlanmış.
- [ ] Yetkilendirici makam, yetkilendirmeyi vermek için gereken risk değerlendirmesine sahip.
- [ ] Yeniden yetkilendirme tetikleyicileri ve süregelen yetkilendirme ritmi tanımlanmış.
