# 3.9 Sistem mühendisliği

## Genel bakış ve motivasyon

[Sistem mühendisliği](https://en.wikipedia.org/wiki/Systems_engineering), karmaşık bir sistemin tamamını uçtan uca mühendislik konusu yapma disiplinidir; böylece tüm parçalar gerçek bir ihtiyacı karşılamak için birlikte çalışır. Parçalar yazılımdan çok daha fazlasını içerir. Modern bir sistem genellikle yazılımı, donanımı, insanları, veriyi ve süreçleri birleştirir ve dağınık bir gerçek dünyada çalışmak zorundadır. Sistem mühendisliği bunların hepsini sistemin tüm ömrü boyunca uyumlu tutar.

Bu, yazılım mimarisinden farklıdır. Yazılım mimarisi (bölüm 3.1) yazılım bileşenlerinin nasıl yapılandırılacağına ve birbirleriyle nasıl konuşacağına karar verir. Sistem mühendisliği bir üst düzeyde durur. Sistemin bir bütün olarak ne yapması gerektiğini, yazılım, donanım ve insan operatörlerin işi nasıl paylaşacağını ve bitmiş ürünün çalıştığını nasıl kanıtlayacağınızı sorar. Mesleki yuvası, Uluslararası Sistem Mühendisliği Konseyi olan [INCOSE](https://en.wikipedia.org/wiki/International_Council_on_Systems_Engineering)'tir ve dayanak standardı, bir sistemin yaşam süreci için süreçleri tanımlayan [ISO/IEC/IEEE 15288](https://en.wikipedia.org/wiki/ISO/IEC_15288)'dir.

Bu, büyük kurumsal ve kamu programları için önemlidir, çünkü sistemleri büyük, uzun ömürlü ve güvenlik açısından ya da görev açısından kritiktir. Bir savunma platformu, bir hava trafik sistemi ya da bir uydu takımyıldızı; özel donanımı, üçüncü taraf parçaları, gömülü ve bulut yazılımını ve insan operatörleri harmanlar ve hiçbir tek takım bütünü kafasında tutamaz. Ayrıca çoğu zaman bir [sistemler sistemi](https://en.wikipedia.org/wiki/System_of_systems) kurarsınız: her biri kendi başına yararlı olan ve daha büyük bir yetenek sunmak için iş birliği yapması gereken birçok bağımsız sistem.

Bu bölüm yazılım gereksinimleri (bölüm 2.8), mimari temelleri (bölüm 3.1), yazılım modelleri ve yöntemleri (bölüm 2.12), birlikte çalışabilirlik ve açık standartlar (bölüm 3.8) ve proje yönetimi (bölüm 10.6) ile bağlantılıdır.

## Temel ilkeler

- **Parçaları değil, bütünü mühendisliğe konu edin.** Bir sistem bir bütün olarak başarılı ya da başarısız olur; bu yüzden bir alt sistemi tek başına eniyilemek bütünü kötüleştirebilir.
- **Yaşam döngüsünü izleyin.** Bir sistemin ilk kavramdan son emekliliğe kadar bir hayatı vardır. Yalnızca inşayı değil, hepsini planlayın.
- **Her gereksinimi izleyin.** Her ihtiyaç bir gereksinime, bir tasarım öğesine ve bir teste eşlenmelidir. İzleyemiyorsanız kanıtlayamazsınız.
- **Arayüzleri bilinçli yönetin.** Çoğu başarısızlık parçalar arasındaki sınırlarda olur; bu yüzden arayüzler açık sahiplenmeyi ve denetimi hak eder.
- **Doğrulamayı ve geçerlemeyi ayrı yapın.** Şeyi doğru inşa etmek (doğrulama) ve doğru şeyi inşa etmek (geçerleme) farklı sorulardır ve ikisinin de cevabına ihtiyacınız var.
- **Ortaya çıkan davranışı bekleyin.** Parçaları birleştirmek hiçbir tek parçanın göstermediği davranışlar yaratır. Bir kısmı amaçtır, bir kısmı kötü bir sürprizdir.
- **Donanımı ve yazılımı birlikte mühendisliğe konu edin.** İkisi de özel olduğunda, birindeki kararlar diğerini kısıtlar; bu yüzden onları birlikte planlayın.

## Öneriler

### Sistemin tüm yaşam döngüsünü yönetin

Sistemi bütün bir hayatı olan bir varlık olarak ele alın ve her aşamayı planlayın. Yaygın bir yaşam döngüsü şöyle işler: **kavram** (ihtiyacı anlama ve seçenekleri keşfetme), **gereksinimler** (sistemin ne yapması gerektiğini kesin biçimde belirtme), **tasarım** (mimariye ve parçalara karar verme), **entegrasyon** (parçaları bir araya getirme), **doğrulama ve geçerleme** (çalıştığını ve doğru sistem olduğunu kanıtlama), **işletim** (çalıştırma ve bakım) ve **emeklilik** (veri ve bertaraf dahil, güvenle hizmetten çıkarma). ISO/IEC/IEEE 15288 size bunun için bir süreç çerçevesi verir. Aşamaların katı bir şelale olması gerekmez; yineleyebilir, prototip çıkarabilir ve artımlar teslim edebilirsiniz. Önemli olan, erken planların çoğu zaman yok saydığı pahalı sonraki aşamalar dahil her aşamayı bilinçli biçimde ele almanızdır.

### Paydaş ihtiyaçlarını yakalayın ve gereksinimleri izlenebilirlikle tahsis edin

Sistemi önemseyen insanlardan başlayın: kullanıcılar, operatörler, sahipler, düzenleyiciler ve kamu. Onların **ihtiyaçlarını** sade bir dille toplayın, sonra bu ihtiyaçları belirli ve sınanabilir mühendislik **gereksinimlerine** dönüştürün (bkz. bölüm 2.8). Sırada **gereksinim tahsisi** gelir: her sistem düzeyi gereksinimi belirli bir alt sisteme atamak; böylece onu karşılamaktan hangi parçanın sorumlu olduğunu bilirsiniz. Bir **[izlenebilirlik](https://en.wikipedia.org/wiki/Requirements_traceability) matrisi** tutun: her ihtiyacı gereksinimine, onu karşılayan tasarım öğesine ve onu doğrulayan teste bağlayan yaşayan bir kayıt. Bu, her an her ihtiyacın karşılandığını ve her parçanın bir nedenle var olduğunu kanıtlamanızı sağlar.

### Arayüzleri açıkça yönetin

Arayüzler parçaların buluştuğu ve sistemlerin en sık bozulduğu yerlerdir. Bir arayüz fiziksel bir konektör, bir ağ protokolü, bir veri biçimi ya da bir insan prosedürü olabilir. Her biri için bir **Arayüz Kontrol Belgesi** (ICD) yazın: iki parçanın tam olarak nasıl bağlandığına ve bilgi alışverişi yaptığına dair üzerinde anlaşılmış bir belirtim. Her arayüze her iki tarafta net bir sahip verin. Tek seferlik konektörler yerine paylaşılan, yayımlanmış belirtimlere dayanmak entegrasyonu çok daha kolaylaştırır; bölüm 3.8'deki birlikte çalışabilirlik argümanı budur. Mümkün olduğunda arayüzleri erken dondurun, çünkü geç bir değişiklik ona dokunan her parçaya yayılır.

### Entegre edin, sonra doğrulayın ve geçerleyin

**Sistem entegrasyonu** alt sistemleri çalışan bütüne birleştirir; genellikle hepsi bir anda değil aşamalar halinde yapılır ki sorunları hâlâ küçükken bulasınız. Entegrasyondan sonra **[doğrulama ve geçerleme](https://en.wikipedia.org/wiki/Verification_and_validation)** (D&G) gelir, iki ayrı kontrol. **Doğrulama** şunu sorar: sistemi doğru mu inşa ettik, yani belirtilmiş gereksinimlerini karşılıyor mu? Doğrulamayı inceleme, analiz, gösterim ve test yoluyla yaparsınız. **Geçerleme** şunu sorar: doğru sistemi mi inşa ettik, yani gerçek kullanımda paydaşların gerçek ihtiyaçlarını karşılıyor mu? Bir sistem doğrulamayı geçip (belirtime uyuyor) geçerlemede başarısız olabilir (belirtim yanlıştı). İkisini de erken planlayın ve gereksinimleri ile arayüzleri en baştan doğrulanabilecek biçimde yazın.

### Model tabanlı sistem mühendisliğini benimseyin

Geleneksel sistem mühendisliği birbirinden kopan dağ gibi belgeler üretirdi. **[Model tabanlı sistem mühendisliği](https://en.wikipedia.org/wiki/Model-based_systems_engineering)** (MBSE) bu yığını, görünümlerin ve raporların üretildiği tek, paylaşılan, biçimsel bir sistem modeliyle değiştirir. Yaygın modelleme dili, bir sistemin gereksinimlerini, yapısını, davranışını ve kısıtlarını betimlemek için grafiksel bir dil olan **[SysML](https://en.wikipedia.org/wiki/Systems_Modeling_Language)**'dir (Sistem Modelleme Dili). Her şey tek bir bağlantılı modelde yaşadığı için bir değişiklik her yerde güncellenir ve izlenebilirlik elle kovalamak yerine bir sorguya dönüşür. MBSE, bölüm 2.12'deki modelleme fikirleriyle bağlantılıdır. Onu kademeli benimseyin; ortak bir modelin en hızlı karşılığını verdiği en yüksek riskli parçalardan başlayın.

### Ortaya çıkan davranışa sistem düşüncesi uygulayın

[Sistem düşüncesini](https://en.wikipedia.org/wiki/Systems_thinking) uygulayın: yalnızca parçaları teker teker değil, bütünü ve parçalar arasındaki ilişkileri düşünün. **[Ortaya çıkan davranışı](https://en.wikipedia.org/wiki/Emergence)** böyle öngörürsünüz: yalnızca parçalar birleştiğinde beliren ve hiçbir tek parçanın göstermediği özellikler. İyi ortaya çıkış çoğu zaman sistemin amacıdır (bir dron sürüsü hiçbir tek dronun kaplayamayacağı bir alanı kaplar). Kötü ortaya çıkış sürpriz başarısızlıktır (iki güvenli alt sistem etkileşerek tehlikeli bir durum yaratır). Hiç modellemediğiniz bir sistemden ortaya çıkışı test ederek çıkaramazsınız; bu yüzden onu işletimden önce bulmak için simülasyon ve yapılandırılmış tehlike analizi kullanın.

### Donanımı ve yazılımı birlikte mühendisliğe konu edin

Bir sistem özel donanım içerdiğinde, donanımı ve yazılımı birlikte mühendisliğe konu edin; buna **[donanım/yazılım birlikte tasarımı](https://en.wikipedia.org/wiki/Hardware/software_co-design)** denir. Kararlar birbirini bağlar: donanım, yazılımın içinde yaşamak zorunda olduğu zamanlama, bellek ve güç sınırlarını koyar ve yazılımın ihtiyaçları donanımın sağlaması gerekenleri şekillendirir. Uzun donanım temin süreleri de takvimi belirler. Hangi işlevlerin donanımda, hangilerinin yazılımda yaşayacağına erken karar verin ve kısıtlar ortaya çıktıkça bu ayrımı yeniden gözden geçirin.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler / maliyet |
|---|---|---|
| Tam sistem mühendisliği titizliği | Daha az geç sürpriz, güçlü izlenebilirlik, daha güvenli ve denetlenebilir | Yüksek başlangıç maliyeti, yavaş başlangıç, ağır süreç |
| Hafif / yalnızca yazılım yaklaşımı | Küçük kapsam için hızlı, ucuz, esnek | Büyük çok disiplinli sistemlerde çöker, arayüzleri ve ortaya çıkışı kaçırır |
| Model tabanlı (MBSE) | Tek doğruluk kaynağı, kolay izlenebilirlik, tutarlı görünümler | Araç ve eğitim maliyeti, kültür değişimi, öğrenme eğrisi |
| Belge tabanlı sistem mühendisliği | Tanıdık, düşük araç maliyeti, paylaşması kolay | Belgeler birbirinden kopar, izlenebilirlik elle yapılır ve hataya açıktır |

Merkezdeki ödünleşim titizlik ile hız arasındadır. Tam sistem mühendisliği çabayı kavrama, gereksinimlere ve arayüz çalışmasına öne çeker. Bu çaba, büyük, uzun ömürlü, güvenlik açısından kritik sistemlerde kendini kat kat öder; çünkü işletimde bulunan bir kusurun maliyeti, aynı kusurun gereksinimlerde bulunmasından binlerce kat fazla olabilir. Küçük, kısa ömürlü, yalnızca yazılımdan oluşan bir üründe bu titizlik gereğinden fazladır. Sürecinizin ağırlığını sistemin boyutuna, ömrüne ve riskine uydurun. Başarısızlık biçimi, atılacak proje alışkanlıklarını otuz yıl çalışacak ve gerçek dünya riski taşıyacak bir sisteme uygulamaktır.

## Takımınızla tartışılacak sorular

1. **Belirtimin istediği şeyi tam olarak inşa edip yine de yanlış sistemi nerede teslim ettiniz ve neyi yakalamış olurdu?** Doğrulama (doğru inşa ettik mi) ve geçerleme (doğru şeyi inşa ettik mi) farklı sorulara cevap verir ve bir sistem, belirtimin kendisi yanlış olduğu için her doğrulama testini geçip geçerlemede başarısız olabilir. Büyük programlarda ikisi "test"te birleştirilir; böylece kimse gerçek operatör ihtiyacına karşı geç bir zamana kadar geçerleme yapmaz, o zaman da bir düzeltme bir gereksinim değişikliğinden binlerce kat pahalıdır. Teslim edilen sistemin gereksinimlerini karşıladığı hâlde asıl ihtiyacı kaçırdığı geçmiş bir örnek getirin ve hangi geçerleme etkinliğinin (gerçek operatörlerle bir simülasyon, sahada erken bir prototip) bunu daha erken ortaya çıkarabileceğini sorun. İki kontrolü de en baştan planlayın ve gereksinimleri ile arayüzleri hiç değilse doğrulanabilecek biçimde yazın. Bu ayrım, kıt inceleme çabanızı nereye harcayacağınıza karar verir.

2. **Kötü ortaya çıkan davranışı sistem işletimdeyken değil, öncesinde nasıl avlıyorsunuz?** Güvenli alt sistemleri birleştirmek, hiçbir tek parçanın göstermediği tehlikeli durumlar yaratabilir ve hiç modellemediğiniz bir sistemden ortaya çıkışı test ederek çıkaramazsınız. Güvenlik açısından ya da görev açısından kritik bir programda, sürpriz etkileşim birini yaralayan ya da görevi başarısızlığa uğratan etkileşimdir; bu yüzden canlı işletimden önce bulunmalıdır. Bütünü modelleme yaklaşımınızı (simülasyon, yapılandırılmış tehlike analizi, etkileşimleri yakalayan bir SysML modeli) getirin ve hangi alt sistemler arası davranışları gerçekten keşfettiğinizi, hangilerini yok varsaydığınızı sorun. İyi ortaya çıkış çoğu zaman sistemin amacıdır ve ona doğru tasarım yapmaya değer; kötü ortaya çıkış, karşısında mühendislik yapmanız gereken başarısızlıktır. Tek entegrasyon stratejiniz parçaları birbirine bağlayıp ne olacağını görmekse, ortaya çıkışı üretimde keşfetmeyi planlıyorsunuz demektir.

3. **Uzun temin süreli donanım kararları ne zaman dondurulmalı ve bu son tarih yazılım takviminizi nasıl belirliyor?** Bir sistem özel donanım içerdiğinde ikisi birlikte mühendisliğe konu edilmelidir: çip, yazılımın içinde yaşadığı zamanlama, bellek ve güç tavanlarını koyar ve donanım temin süreleri çoğu zaman tüm takvime hükmeder. Yazılımı ayrılabilir sayan takımlar yerel olarak eniyiler, sonra entegrasyonda donanım kısıtlarına çarpar ve aylar kaybeder. Donanım temin sürelerini ve donanım/yazılım işlev ayrımının kararlaştırılması gereken tarihi getirin ve bu ayrımı körlemesine dondurmak yerine kısıtlar ortaya çıktıkça yeniden gözden geçirin. Hangi işlevlerin silikonda, hangilerinin yazılımda yaşayacağına ne kadar erken karar verirseniz, o kadar az pahalı geri dönüşle karşılaşırsınız. İkisi arasındaki arayüzler bir Arayüz Kontrol Belgesini ve her tarafta bir sahibi hak eder, çünkü orada geç bir değişiklik ona dokunan her şeye yayılır.

4. **Tek bir paydaş ihtiyacını gereksinime, tasarım öğesine ve onu kanıtlayan teste kadar izleyebiliyor musunuz ve bu bağı kim canlı tutuyor?** İzlenebilirlik, her an her ihtiyacın karşılandığını ve her parçanın bir nedenle var olduğunu göstermenizi sağlayan şeydir; yine de büyük bir programda matris, kimse sahiplenmediği anda çürür. Rakip çekim gerçektir: mühendisler izlenebilirliği bürokratik yük olarak yaşar ve elle tutulan bir matris tasarımın değişmesinden daha hızlı eskir. Mevcut bir programdan gerçek bir bağ getirin ve onu odada uçtan uca yürümeyi deneyin: adı konmuş bir paydaş ihtiyacından, tahsis edilmiş gereksinime, onu karşılayan alt sisteme ve tasarım öğesine, doğrulama testine; zincirin nerede koptuğunu not edin. Matrisin sahibine ve izlenebilirliğin elle kovalamak yerine bir sorgu olduğu bir modelde yaşayıp yaşamaması gerektiğine karar verin. Kurumsal ve kamu programlarında matris aynı zamanda düzenleyicilerin ve tedarik makamlarının talep ettiği denetim kanıtıdır; bu yüzden kopuk bir zincir yalnızca mühendisliği yavaşlatmaz, sertifikasyonu ya da ödemeyi durdurabilir.

5. **Model tabanlı bir yaklaşım sizin için araç ve kültür maliyetine değer mi, yoksa pahalı bir rafta duran yazılıma mı dönüşür?** Belge tabanlı sistem mühendisliği tanıdıktır ve araçlandırması ucuzdur, ama belgeleri birbirinden kopar ve izlenebilirliği elle yapılır, hataya açıktır; MBSE yığını tek bir bağlantılı modelle değiştirir, bedeli araç, eğitim ve gerçek bir kültür değişimidir. Her iki uç da pahalıdır: büyük çok disiplinli bir programda MBSE'yi atlarsanız entegrasyon sürprizleriyle ödersiniz, modeli güncel tutacak disiplin olmadan benimserseniz, hiç model olmamasından beter bir raf yazılımına çürür. Araç olgunluğunuza dair dürüst bir okuma, takımda bir SysML modelini kimin gerçekten yazıp bakımını yapabileceği ve hangi tek yüksek riskli alt sistemin yaklaşımı, ortak modelin en hızlı karşılığını verdiği yerde pilot edebileceği konusunda dürüst bir değerlendirme getirin. Tüm kuruluşa bir anda zorunlu kılmak yerine kademeli karar verin. Çok tedarikçili büyük bir kurumsal ya da kamu programında, ortak bir modelin, aksi hâlde eskimiş belgeler takas eden yüklenicilerde gereksinimleri, arayüzleri ve testleri tutarlı tutmanın tek gerçekçi yolu olup olmadığını tartın.

6. **Yaşam döngüsü planınız işletimi ve emekliliği ciddi biçimde finanse ediyor mu, yoksa sessizce fırlatmada mı duruyor?** Uzun ömürlü bir sistemin toplam maliyetine hükmeden aşamalar, yani onu onlarca yıl çalıştırmak ve güvenle hizmetten çıkarmak, erken planların düzenli olarak yok saydığı aşamalardır, çünkü baskı her zaman teslim etmektir. Rakip düşünce şudur: para ve dikkat, bu sonraki aşamalar en uzak göründüğü anda en kıttır; bu yüzden işletim, bakım, veri taşıma ve bertaraf, pahalı ve riskli bir telaşa dönüşene kadar ertelenir. Mevcut yaşam döngüsü planını getirin ve işletim ile emeklilik için sahipleri, bütçeleri ve çıkış ölçütlerini adlandırıp adlandırmadığına ya da fırlatmayı bitiş çizgisi sayıp saymadığına bakın. Ömrün sonunda veriye ve donanıma ne olacağını ve aradaki yılların bakımını kimin ödeyeceğini sorun. Yirmi ya da otuz yıl çalışması ve sonra kamu denetimi altında emekli olması gereken kurumsal ve kamu sistemlerinde, plansız bir hizmetten çıkarma düzenleyici, çevresel ya da kayıt saklama yükümlülüklerini ihlal edebilir; bu yüzden emeklilik, ilk kavram incelemesinden itibaren plana ve bütçeye aittir.

## Sektör merceği

**Girişim.** Minik bir takım resmî bir sistem mühendisliği programı yürütemez ve denememelidir, ama yine de bellenimi, uygulamayı ve bulutu üç ayrı proje olarak değil, tek bir sistem olarak ele alabilir. Parçaların nasıl konuştuğunu sabitleyen tek bir kısa arayüz belgesi yazın, her müşteri ihtiyacını onu karşılayan parçaya bağlayan basit bir tablo tutun ve ağır süreci atlayın. En kıt kaynağınız mühendislik dikkatidir; bu yüzden izlenebilirlik çabasını yalnızca bir sınırdaki yanlış bir varsayımın ürünü sahada sessizce bozacağı yerlere harcayın.

**Küçük işletme.** Özel bir sistem mühendisi ve dar bir bütçe olmadığında, tasarlamanız ve doğrulamanız gereken özel entegrasyon yerine yayımlanmış standartlara ve satın alınmış alt sistemlere yaslanın. Sonsuza dek sahip olmanız gereken özel bir konektör olmadan parçaların uyması için net arayüz belirtimleri sunan tedarikçileri tercih edin. Yap-ya-da-satın-al seçimini, ürünün ömrü boyunca hangi arayüzleri gerçekçi biçimde denetleyip doğrulayabileceğiniz çerçevesine oturtun ve gerisini satın alın.

**Kurumsal.** Ölçekte sorun, birçok takım ve tedarikçi arasında tutarlılıktır: ISO/IEC/IEEE 15288'e hizalanmış ortak bir yaşam döngüsü süreci, her tedarikçi sınırı için bir Arayüz Kontrol Belgesi ve adı konmuş bir sahip ve tek bir bileşen değişikliğinin program çapında bir telaşı tetiklememesi için uçtan uca izlenebilirlik. Ortak bir modelin gereksinimleri, arayüzleri ve testleri yükleniciler arasında uyumlu tuttuğu yerlerde MBSE'ye yatırım yapın. Doğrulama ve geçerleme ayrı kalsın ve her gereksinim sorumlu bir parçaya tahsis edilsin diye süreci yönetin.

**Kamu.** İhale kuralları, şeffaflık ve kamusal hesap verebilirlik her seçimi şekillendirir. Sistem mühendisliği sürecini, izlenebilirliği ve D&G kanıtını sözleşmede belirtin, tedarikçilerden denetleyebileceğiniz arayüz kontrol belgeleri ve yaşam döngüsü ürünleri teslim etmelerini isteyin ve herhangi bir canlı geçişten önce güvenlik ve görev geçerlemesini gerçek operatörlerle bağımsız incelemeye ayırın. İşletimi ve emekliliği açıkça planlayın ve finanse edin, çünkü kamu programı güvenli hizmetten çıkarma ve kayıt saklama dahil tüm yaşam döngüsünden sorumludur.

## Örnekler

**Girişim.** Bağlantılı bir sensör geliştiren dört kişilik bir donanım girişimi resmî bir sistem mühendisliği programını karşılayamaz, ama yine de ürünü üç ayrı proje olarak değil, bellenimden, bir mobil uygulamadan ve bir bulut arka uçtan oluşan tek bir sistem olarak ele alır. Cihazın, uygulamanın ve sunucunun nasıl konuştuğunu sabitleyen (mesaj biçimleri, birimler, hata kodları) tek bir kısa arayüz belgesi yazarlar ve her müşteri ihtiyacını onu karşılayan parçaya bağlayan basit bir tablo tutarlar. Daha ucuz bir sensör çipi bir bellenim değişikliğini zorunlu kıldığında, bu ortak arayüz uygulamanın ve arka ucun neyi ayarlaması gerektiğini hemen gösterir; böylece bir bileşen değişimi ürünü sahada sessizce bozmaz.

**Kurumsal.** Küresel bir otomotiv üreticisi yeni bir elektrikli araç platformu kurar: yazılımdan (batarya yönetimi, sürücü yardımı, bilgi-eğlence), donanımdan (motorlar, sensörler, çipler) ve insan faktörlerinden oluşan bir sistem, artı her biri alt sistemler teslim eden birçok tedarikçi. Şirket bir sistem mühendisliği programı yürütür. Paydaş ihtiyaçları tahsis edilmiş gereksinimleri besler, her tedarikçi arayüzünün bir Arayüz Kontrol Belgesi vardır ve bir SysML modeli gereksinimleri tasarıma, tasarımı testlere bağlar. Bir batarya hücresi tedarikçisi bir bileşeni değiştirdiğinde, izlenebilirlik modeli hangi gereksinimlerin, arayüzlerin ve testlerin etkilendiğini tam olarak gösterir; böylece değişiklik program çapında bir telaşı tetiklemek yerine sınırlı kalır.

**Kamu.** Ulusal bir hava seyrüsefer otoritesi, radarları, kontrolör iş istasyonlarını, iletişimi ve yazılımı kapsayan, günün yirmi dört saati işletilen, güvenlik açısından kritik bir sistemler sistemi olan hava trafik yönetim sistemini modernize eder. Program tüm yaşam döngüsü boyunca ISO/IEC/IEEE 15288'i izler. Doğrulama her alt sistemin belirtimini karşıladığını kanıtlar ve gerçek kontrolörlerle simülasyon yoluyla geçerleme, hiçbir canlı trafik ona bağımlı olmadan önce bütünleşik sistemin güvenli işletimi desteklediğini kanıtlar. Titiz D&G, otoritenin her adımda geri dönüş seçeneğiyle aşamalı geçiş yapmasını sağlar, çünkü burada test edilmemiş bir ortaya çıkan başarısızlık bir kamu güvenliği olayıdır.

## İş gerekçesi: motivasyonlar, YG ve TSM

Motivasyon, kusurların ne kadar geç bulunursa o kadar üstel biçimde pahalılaşmasıdır. Gereksinimler aşamasında yakalanan bir gereksinim hatasının düzeltilmesi neredeyse hiçbir şeye mal olmaz. Aynı hata işletimde yakalanırsa binlerce kat fazlasına mal olabilir ve güvenlik açısından kritik bir sistemde canlara, geri çağırmalara ya da başarısız bir göreve mal olabilir. Sistem mühendisliği kusur keşfini ucuz erken aşamalara kaydırır.

**Yatırım getirisi** (YG, kazanılan değerin harcanan maliyete oranı) açısından karşılık, önlenen yeniden işleme, daha az entegrasyon başarısızlığı ve aşım yerine takvime ve bütçeye uyan programlardır. Büyük programlara dair sektör çalışmaları, güçlü sistem mühendisliği çabasının daha küçük aşımlarla ilişkili olduğunu tekrar tekrar bulur. **Toplam sahip olma maliyeti** (TSM, bir sistemi inşa etmenin, çalıştırmanın ve emekli etmenin tüm ömür boyu maliyeti) açısından, sistem mühendisliği uzun vadeli maliyete hükmeden ama plansız projelerin yok saydığı işletim ve emeklilik aşamalarını hesaba katar. Bakım kolaylığı, arayüzler ve bertaraf için en baştan tasarım yapmak, sistemin hizmette geçirdiği on yılların maliyetini düşürür. Bkz. proje yönetimi (bölüm 10.6).

## Anti-kalıplar ve tuzaklar

- **Yinelemesiz büyük peşin tasarım.** Yaşam döngüsünü katı, tek yönlü bir şelale olarak ele almak; böylece gereksinimlerin yanlış olduğunu ancak her şeyi inşa ettikten sonra öğrenirsiniz.
- **İzlenebilirliksiz gereksinimler.** Kimsenin tasarıma ya da testlere bağlamadığı bir gereksinim yığını; böylece kapsamı kanıtlayamaz ve hiçbir parçayı gerekçelendiremezsiniz.
- **Arayüzleri yok saymak.** Alt sistemlerin kendiliğinden uyacağını varsaymak, sonra kimsenin sahiplenmediği sınır uyumsuzlukları yüzünden entegrasyonda aylar kaybetmek.
- **Geçerlemesiz doğrulama.** Sistemin belirtimini karşıladığını kanıtlayıp belirtimin gerçek ihtiyaçlarla eşleşip eşleşmediğini hiç kontrol etmemek, sonra yanlış sistemi teslim etmek.
- **Yazılımı ayrı saymak.** Yazılım takımlarının donanım kısıtlarını, zamanlamayı ve insan operatörleri yok sayarak yerel olarak eniyilemesi.
- **Raf yazılımı olarak MBSE.** Bir modeli bir kez kurup uyumdan çürümesine izin vermek; böylece hiç modelden daha kötü olur.
- **Emeklilik planlamasını atlamak.** Hizmetten çıkarma, veri taşıma ya da bertaraf için plan olmaması; böylece ömrün sonu pahalı ve riskli bir telaşa dönüşür.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Sistem mühendisliği geçici ve tepkiseldir. Gereksinimler dağınık belgelerde yaşar, arayüzler entegrasyonda keşfedilir ve doğrulama, yapılabilen her ne test varsa odur. Büyük programlar düzenli olarak aşar ve takımı geç bir zamanda şaşırtır.

**Düzey 2, Geliştirme.** Büyük programlarda temel uygulamalar vardır. Gereksinimler yakalanır ve temel çizgiye alınır, önemli arayüzlerin kontrol belgeleri vardır ve bir doğrulama planı bulunur. Uygulama takımlar arasında tutarsızdır ve ortak bir yönteme değil bireylere bağlıdır.

**Düzey 3, Standartlaştırma.** Sistem mühendisliği, ISO/IEC/IEEE 15288'e hizalanmış ve takımlar boyunca uygulanan, belgelenmiş, kuruluş çapında bir disiplindir. Tüm yaşam döngüsü planlanır, izlenebilirlik uçtan uca sürdürülür, arayüzler biçimsel olarak denetlenir ve doğrulama ile geçerleme ayrı ve planlıdır. MBSE karmaşık programlarda kullanılır.

**Düzey 4, Yönetme.** Sistem mühendisliği veriyle ölçülür ve denetlenir. Kuruluş, temel çizgilere karşı metrikleri izler: gereksinim değişkenliği ve izlenebilirlik kapsamı, entegrasyonda bulunan arayüz kusurları, doğrulama ve geçerleme başarı oranları ve yaşam döngüsü aşamasına göre kusur sızıntısı (her aşamadan kaç kusurun kaçıp sonradan daha yüksek maliyetle yakalandığı). İncelemeler programları bu sayılara göre yönlendirir ve eşikler, olay sonrası yangın söndürme yerine düzeltici eylemi tetikler.

**Düzey 5, Orkestrasyon.** Sistem mühendisliği sürekli iyileştirilir ve kuruluş genelinde bütünleşiktir. Yaşayan bir MBSE modeli tek doğruluk kaynağıdır, izlenebilirlik otomatiktir, simülasyon ortaya çıkan davranışı inşadan önce öngörür ve geçmiş programların metrikleri bir sonrakini besler. Donanım ve yazılım olağan olarak birlikte mühendisliğe konu edilir ve süreç, programlar, tedarikçiler ve riskler değiştikçe uyum sağlar.

## Tartışma fikirleri

- Kuruluşunuzda sistem mühendisliği ile yazılım mimarisi arasındaki çizgi nerede ve ikisi arasındaki boşluğa kim sahip?
- En büyük programınızda tek bir paydaş ihtiyacını onu doğrulayan teste kadar izleyebiliyor musunuz? İzleyemiyorsanız, bunun için ne gerekir?
- Son başarısızlıklarınızdan hangisi bir arayüzde yaşandı ve ona kim sahipti?
- MBSE sizin için karşılığını verir mi, yoksa kültürünüz ve araçlarınız göz önüne alındığında pahalı bir raf yazılımına mı dönüşür?
- Yaşam döngüsü planınız işletimi ve emekliliği ciddi biçimde ele alıyor mu, yoksa sessizce fırlatmada mı duruyor?

## Önemli çıkarımlar

- Sistem mühendisliği tüm sistemi (yazılım, donanım, insanlar ve süreçler) uçtan uca mühendisliğe konu eder ve yazılım mimarisinden ayrıdır.
- Kavramdan gereksinimlere, tasarıma, entegrasyona, D&G'ye, işletime ve emekliliğe kadar tüm yaşam döngüsünü planlayın.
- Her ihtiyacı bir gereksinime, bir tasarım öğesine ve bir teste kadar izleyin ve her gereksinimi sorumlu bir parçaya tahsis edin.
- Arayüzleri net sahiplik ve kontrol belgeleriyle açıkça yönetin, çünkü sınırlar sistemlerin bozulduğu yerlerdir.
- Doğrulama (doğru inşa ettik) ve geçerleme (doğru şeyi inşa ettik) farklı kontrollerdir ve ikisine de ihtiyacınız var.
- Tek bağlantılı bir doğruluk kaynağı için MBSE ve SysML kullanın ve ortaya çıkan davranışı öngörmek için sistem düşüncesinden yararlanın.
- Sürecinizin ağırlığını sistemin boyutuna, ömrüne ve riskine uydurun.

## Kaynaklar ve ileri okuma

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
