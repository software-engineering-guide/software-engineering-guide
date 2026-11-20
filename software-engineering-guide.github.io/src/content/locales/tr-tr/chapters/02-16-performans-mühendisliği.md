# 2.16 Performans mühendisliği

## Genel bakış ve motivasyon

Performans mühendisliği, kodu içgüdü yerine ölçümle, bilinçli biçimde yeterince hızlı yapma zanaatıdır. Bu bölüm kod ve bileşen düzeyinde çalışır: işlevler, döngüler, veri yapıları, sorgular, bellek ayırmaları ve tek bir hizmetin zamanını nasıl harcadığı. Performansı sistem düzeyinde (dışa ölçekleme, yük dengeleme, kapasite ve dayanıklılık) ele alan bölüm 3.5'in tamamlayıcısıdır. Bir sistem yavaş olduğunda bölüm 3.5 kaç makineye ihtiyacınız olduğunu sorar; bu bölüm ise tek bir makinenin ilk etapta neden bu kadar çok iş yaptığını sorar. Genellikle ikisine de ihtiyaç duyarsınız ve kod düzeyindeki görünüm, maliyetin ve gecikmenin şaşırtıcı bir kısmının gerçekten saklandığı yerdir.

Büyük takımlar için bu disiplin önemlidir, çünkü performans sessizce çürür. Hiçbir tek commit bir hizmeti yavaşlatmaz, ama her biri bir veritabanı çağrısı ya da sınırsız bir döngü ekleyen bin küçük commit yavaşlatır. Performansı ölçmek, bütçelemek ve kapıya koymak için paylaşılan bir yöntem olmadan, çürümeyi ancak bir müşteri şikâyet ettiğinde ya da bir lansman eridiğinde keşfedersiniz. Bir yöntem performansı kahramanca bir yangın söndürmeden, koruduğunuz rutin bir özelliğe çevirir.

Kurumlar için performans paradır: daha hızlı kod daha az makine, daha düşük bulut faturaları ve gecikme konusunda fazla kaynak ayırmadan bir [hizmet düzeyi anlaşmasını](https://en.wikipedia.org/wiki/Service-level_agreement) (HDA) karşılama yeteneği demektir. Kamu için performans erişimdir: zayıf bir mobil bağlantı üzerinde eski bir telefonda yüklenen bir sayfa, bir vatandaşın yardım başvurusunu tamamlamasıyla vazgeçmesi arasındaki farktır. Kamu sistemleri ayrıca yeniden üretilebilir kıyaslama kanıtına ihtiyaç duyar, çünkü tedarik ve gözetim organları sayıları yalnızca iddia etmenizi değil, kanıtlamanızı isteyecektir.

## Temel ilkeler

- **Optimize etmeden önce ölçün.** Darboğaz hemen hemen hiçbir zaman tahmin ettiğiniz yerde değildir. Profil çıkarın, sonra harekete geçin.
- **Erken optimizasyondan kaçının.** Donald Knuth'un uyarısı geçerlidir: önemli olmayan kodu optimize etmek netliğe mal olur ve hiçbir şey kazandırmaz.
- **"Yeterince hızlı"yı bir sayı olarak tanımlayın.** Bir hedef ve bir yüzdelik içeren performans bütçesi görüşü geçti ya da kaldıya çevirir.
- **Ortalamalar yalan söyler; yüzdelikler gerçeği söyler.** Kullanıcıların hissettiği ortalama değil, kuyruktur (p99).
- **Algoritmik kazançlar mikro ayarı yener.** Daha iyi bir karmaşıklık sınıfı, her miktarda sabit çarpan zekasını geride bırakır.
- **Gecikme ve verim farklı hedeflerdir.** Birini iyileştirmek diğerini kötüleştirebilir; hangisini satın aldığınızı bilin.
- **Dürüstçe kıyaslayın ya da hiç kıyaslamayın.** Isınma, varyans ve temsili bir iş yükü gerçek sayıları kurgudan ayırır.
- **Performansı CI'de kapıya koyun, üretimde izleyin.** Birleştirmeden önce yakalanan gerilemeler ucuzdur; kullanıcılar tarafından yakalananlar pahalıdır.

## Öneriler

### Önce ölçün ve tek satıra dokunmadan önce profil çıkarın

Bu alandaki en eski kural en çok göz ardı edilendir: optimize etmeden önce darboğazı bulun. Çalışan bir programı zamanını ve belleğini nerede harcadığını göstermek için örnekleyen ya da donatan bir araç olan [profil çıkarıcıya](https://en.wikipedia.org/wiki/Profiling_(computer_programming)) uzanın. CPU'yu (hangi işlevler döngü yakıyor), belleği ve ayırmayı (neyin ne sıklıkla ayrıldığı; çünkü ayırma çalkantısı çöp toplama duraklamalarını yönlendirir) ve G/Ç'yi (disk, ağ ya da veritabanında beklemede geçen süre) profilleyin. Her kutunun bir işlev ve genişliğinin harcanan zaman olduğu yığılmış bir görselleştirme olan [alev grafiği](https://en.wikipedia.org/wiki/Flame_graph) baskın maliyeti bir bakışta belirgin kılar: en derin yığınları değil, en geniş kutuları arayın. En büyük maliyeti ilk optimize edin, yeniden ölçün ve bütçeye ulaştığınızda durun. Bu, bölüm 9.2'nin gözlemlenebilirlik uygulamalarına bağlanır, çünkü üretim profili bir dizüstü bilgisayardan yapılan her tahmini yener.

Ters hataya da karşı koruyun. Knuth'un tam cümlesi erken optimizasyonun birçok kötülüğün kökü olduğudur ve bunu okunabilir kodu hayali hız için feda etmeye sizi iten küçük verimsizlikler için kastetmişti. Önce net sürümü yazın, ölçün ve yalnızca profil çıkarıcının suçladığı kodu optimize edin.

### Performans bütçeleriyle "yeterince hızlı"nın ne demek olduğunu tanımlayın

Hız soyut bir erdem değildir; ya karşıladığınız ya da kaçırdığınız bir hedeftir. Bir **performans bütçesi** belirleyin: "p99 ödeme gecikmesi 300 ms'nin altında" ya da "bu uç nokta istek başına 1 MB'ın altında ayırır" gibi somut bir sınır. Onu kullanıcıların ya da işin hissettiği bir şeye bağlayın ve bir ortalama olarak değil, bir **yüzdelik** olarak ifade edin, çünkü ortalama gerçek kullanıcıların yaşadığı yavaş kuyruğu gizler. İsteklerin %1'i 5 saniye sürüyorsa, ortalamanız iyi görünürken müşterilerin anlamlı bir dilimi acı çeker. Bütçeler takıma paylaşılan, tartışılmaz bir bitti tanımı ve bir gerilemenin gözle görülür biçimde geçtiği bir çizgi verir.

### Mikro optimizasyondan önce algoritmik verimliliğe uzanın

En büyük, en ucuz kazançlar, girdi büyüdükçe işin nasıl büyüdüğü olan [algoritmik verimlilikten](https://en.wikipedia.org/wiki/Algorithmic_efficiency) gelir; [Büyük O gösterimiyle](https://en.wikipedia.org/wiki/Big_O_notation) (büyüme oranını sınıflandırmanın bir yolu, böylece O(n log n) bir sıralama O(n kare) bir sıralamadan çok daha iyi ölçeklenir) tarif edilir. On öğede görünmez olan iç içe bir döngü on bin öğede felakete dönüşür. Sıcak bir işlevi elle ayarlamadan önce, temelde çok fazla iş yapıp yapmadığını sorun: kazara bir N+1 sorgusu, karma araması olması gereken bir doğrusal tarama ya da notlanabilecek tekrarlanan iş. Bu, bölüm 2.13'teki algoritmik temellere bağlanır. Hiçbir miktar sabit çarpan ayarı yanlış karmaşıklık sınıfını kurtarmaz.

### Gecikmeyi verimden ayırın ve kuyruğa saygı gösterin

**Gecikme** tek bir işlemin ne kadar sürdüğüdür; **verim** birim zamanda kaç işlemin tamamlandığıdır. Aynı hedef değildirler ve birini optimize etmek diğerine zarar verebilir. Toplu işleme verimi iyileştirir ama toplu işteki ilk öğeye gecikme ekler; paralel işçiler eklemek verimi yükseltir ama çekişme yoluyla kuyruk gecikmesini kötüleştirebilir. Kullanıcılarınızın gerçekte hangisine ihtiyaç duyduğuna karar verin. Ve her zaman kuyruğu izleyin: p95 ve p99 gecikmesi, isteklerin en yavaş %5'i ve %1'i, çünkü ölçekte bir kullanıcı birçok istek yapar ve kuyruğa sık çarpar. Yüzdelikleri raporlayın, onlar üzerine uyarı kurun ve onlar için bütçe ayırın.

### Paralelliğin sınırlarını bilin

Paralelleştirdiğinizde [Amdahl yasasını](https://en.wikipedia.org/wiki/Amdahl%27s_law) hatırlayın: işlemci eklemenin hız artışı, işin seri çalışması gereken kesriyle sınırlıdır. Bir işin %10'u doğası gereği ardışıksa, hiçbir çekirdek sayısı sizi 10 kat hız artışının ötesine götürmez. Eşzamanlılık (görevlerin bağımsız ilerleyebilmesi için işi yapılandırma) ve paralellik (onları gerçekten aynı anda yürütme), yarış koşullarından eşgüdüm yüküne kadar gerçek karmaşıklık ekler. Daha fazla iş parçacığının sizi kurtaracağını varsaymadan önce seri kesri ölçün ve en basit doğru sürümün çoğu zaman yeterince hızlı olduğu konusunda dürüst olun.

### Önbelleği ve veri yerelliğini kullanın ve maliyetlerine saygı gösterin

Yakın zamanda ya da pahalıya hesaplanmış sonuçların hızlı bir deposu olan bir [önbellek](https://en.wikipedia.org/wiki/Cache_(computing)), sahip olduğunuz en güçlü performans aracı ve en tehlikeli olandır. Phil Karlton'ın bilgisayar biliminde iki zor şeyin önbellek geçersiz kılma ve isim koymak olduğu şakası bir uyarıdır: bayat bir önbellek yanlış cevaplar sunar ve geçersiz kılma mantığı ince hataların türediği yerdir. Önbelleği bilinçli kullanın, son kullanma süreleri belirleyin ve isabet oranını optimize etmeden önce doğruluk hikâyenizi bilin. En düşük düzeyde, birlikte kullanılan veriyi bellekte birbirine yakın tutan [referans yerelliği](https://en.wikipedia.org/wiki/Locality_of_reference), CPU önbellek hiyerarşisinden yararlanır ve önbellek ıskalarını isabetlere çevirerek kodu algoritmik değişiklik olmadan birkaç kat hızlı yapabilir. Bitişik diziler bu nedenle işaretçi kovalayan yapıları yener. Bu, bölüm 3.4'teki veri düzeni seçimleriyle kesişir.

### Dürüstçe kıyaslayın ve mikro kıyaslamalara güvenmeyin

Yalan söyleyen bir kıyaslama hiç olmamasından kötüdür, çünkü yanlış güven verir. Ölçmeden önce ısının; böylece tek seferlik başlangıcı ve tam zamanında derlemeyi değil, kararlı durum davranışını zamanlarsınız. Çok sayıda yineleme çalıştırın ve tek bir şanslı sayı değil, varyansı raporlayın. Gerçekçi veri boyutları ve dağılımlarıyla temsili bir iş yükü kullanın; çünkü bir oyuncak girdi üzerindeki mikro kıyaslama çoğu zaman kodun gerçek hızını değil, derleyicinin testinizi silme yeteneğini ölçer. Klasik tuzaklara dikkat edin: optimize edicinin kullanılmadığını kanıtlayıp kaldırdığı bir değer, çalışma zamanının yukarı taşıdığı bir döngü ya da kıyaslamada sıcak ve üretimde soğuk olan bir önbellek. Şüphe duyduğunuzda yalıtılmış işlevi değil, tüm yolu ölçün.

### Performansı CI'de kapıya koyun ve üretimde gözlemleyin

Performansı hattın koruduğu bir özellik yapın. Bölüm 2.4'ün stratejisine performans testleri ekleyin; kilit bir kıyaslama ya da bütçe bir eşiğin ötesinde kötüleştiğinde derlemeyi başarısız kılan gerileme kapılarıyla. Bu, yavaş sürünmeyi birleşmeden önce yakalar. Sonra döngüyü üretimde bölüm 9.2'nin telemetrisiyle kapatın: gerçek gecikme yüzdeliklerini, ayırma oranlarını ve yavaş sorguları bütçelerinize karşı izleyin, çünkü üretim trafiği kıyaslamalarınızın hiç hayal etmediği durumları bulur.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
|---|---|---|
| Sezgiye dayalı şimdi optimize etmek | Verimli hissettirir; ara sıra şanslı kazanç | Genellikle yanlış kodu ayarlar; kazanç olmadan karmaşıklık ekler |
| Önce ölç, sonra optimize et | Gerçek darboğazı hedefler; kanıta dayalı | Araç ve disiplin gerektirir; başlaması daha yavaş |
| Önbellekleme | Büyük gecikme ve verim kazançları | Geçersiz kılma hataları; bayat veri; bellek maliyeti |
| Daha fazla paralellik | Paralel işte daha yüksek verim | Amdahl tavanı; çekişme; eşzamanlılık hataları |
| Mikro optimizasyon | Sabit çarpanları sıkıştırır | Küçük tavan; okunabilirliğe zarar verir; çoğu zaman gürültü |
| Algoritmik iyileştirme | Kazançlar girdi boyutuyla ölçeklenir | Analiz gerektirir; bazen daha büyük bir yeniden yazma |
| CI performans kapıları | Gerilemeleri erken ve ucuza durdurur | Kararsız kıyaslamalar güveni aşındırır; kararlı bir ortam gerektirir |

Merkezi gerilim çaba ile getiri arasındadır ve çözüm ölçümdür. Performans işi keskin biçimde azalan getiriye sahiptir: profil güdümlü ilk düzeltme gecikmeyi yarıya indirebilir, onuncusu kod karmaşıklığını ikiye katlarken bir yüzde kırpabilir. Elinizde bir sayı ve ulaşılacak bir bütçe olmadan optimize etmeyi reddederek çözersiniz. Yapmaya değer düzeltmeyi bulmak için ölçün ve hızın kendi iyiliği için peşine düşmek yerine bütçeyi geçtiğiniz anda durun.

## Takımınızla tartışılacak sorular

1. **Kritik yollarınız için yazılı bir performans bütçeniz var mı ve bir yüzdelik olarak mı ifade ediliyor?** Birçok takımın şeylerin "hızlı" olması gerektiğine dair belirsiz bir hissi vardır ama kimsenin kendisine karşı başarısız olabileceği bir sayı yoktur; bu da performansın bozulana kadar kimsenin işi olmadığı anlamına gelir. "p99 300 ms'nin altında" gibi bir bütçe hedefi somut kılar, inceleyicilere uygulayacak bir şey verir ve bir gerilemeyi yavaş bir kayma yerine görünür bir olaya çevirir. Gecikmenin birçok elden süzüldüğü ve hiçbir tek yazarın toplam maliyeti görmediği büyük takımlarda en çok önem taşır. Mevcut gecikme verilerinizi getirin ve size iltifat eden ortalamaları mı yoksa gerçeği söyleyen yüzdelikleri mi raporladığınızı sorun. "Yeterince hızlı"nın ne demek olduğunu bir sayı olarak söyleyemiyorsanız, düzeltilecek ilk şey odur.

2. **Bir şeyi en son optimize ettiğinizde bir profil çıkarıcı mı nereye bakacağınızı söyledi, yoksa tahmin mi ettiniz?** Darboğaz meşhur biçimde deneyimli mühendislerin beklediğinden başka bir yerdedir ve yanlış kodu ayarlamaya harcanan zaman iki kez kaybedilmiş zamandır, bir kez işte ve bir kez eklenen karmaşıklıkta. Önce profil çıkaran bir kültür çabasını karşılığını verdiği yere harcar ve net koda dokunmaz. Takımınızdan son üç performans düzeltmesini ve her birinin bir ölçümle mi yoksa bir sezgiyle mi başladığını hatırlamasını isteyin. Üretimde ya da gerçekçi bir hazırlık ortamında profil çıkarıp çıkaramayacağınızı düşünün, çünkü bir dizüstü bilgisayar profili ağır biçimde yanıltabilir. Cevap performans işinizin mühendislik mi yoksa folklor mu olduğunu ortaya çıkarır.

3. **Bugün bir performans gerilemesinin üretime ulaşmasını ne durduruyor?** Büyüyen bir takımda dürüst cevap çoğu zaman "bir müşteri şikâyeti"dir; bu da kullanıcıların gerileme testiniz olduğu anlamına gelir. Bir kıyaslama ya da bütçe kötüleştiğinde derlemeyi başarısız kılan bir CI kapısı, sorunu düzeltmesi ucuzken ve yazar değişikliği hâlâ hatırlıyorken yakalar. Kıyaslamalarınızın kapıya koyacak kadar kararlı olup olmadığını tartışın, çünkü kurt var diye bağıran kararsız bir performans testi görmezden gelinecek ya da devre dışı bırakılacaktır. Üretimde neyi izlediğinizden de bahsedin, çünkü bazı gerilemeler yalnızca gerçek trafik ve verilerle ortaya çıkar. Amaç, performansı olayda yeniden keşfettiğiniz bir şey değil, sistemin otomatik savunduğu bir özellik yapmaktır.

4. **Her kritik yol için gecikme mi yoksa verim için mi optimize ediyorsunuz ve bu seçimi birisi yazdı mı?** Bunlar ters yönlere çeken farklı hedeflerdir: toplu işleme ve paralel işçiler verimi yükseltir ama tek tek isteklere gecikme ekleyebilir; bu yüzden sezgiyle optimize eden bir takım çoğu zaman yanlış ekseni satın alır ve kimsenin kıtlık çekmediği makine zamanını kurtarmak için kullanıcıları bekletir. Büyük bir takımda tehlike katlanır, çünkü bir grup paylaşılan bir hizmeti toplu verim için ayarlarken diğeri etkileşimli gecikme için ona bağımlıdır ve hiçbiri diğerinin hedefini bilmez. Her yolun gerçek kullanım kalıbını (etkileşimli istek ya da arka plan toplu işi), mevcut yüzdelik gecikmeyi ve ihtiyaç duyduğunuz sürekli verimi getirin, sonra bir varsayılanın ortaya çıkmasına izin vermek yerine ekseni açıkça belirleyin. Bir HDA altındaki kurumsal ya da kamu sistemi için anlaşmanın hangi metriğe karşı yazıldığını adlandırın, çünkü ölçülmeyen ekseni optimize etmek panolarınız sağlıklı görünürken bir sözleşmeyi ihlal edebilir.

5. **Kıyaslamalarınızın optimize edicinin testinizi silmesini değil, gerçek işi ölçtüğünü nasıl biliyorsunuz?** Yalan söyleyen bir kıyaslama hiç olmamasından kötüdür, çünkü takıma yanlış güven verir ve sonra yine de bir gerileme yayımlanır. Takımlar rutin olarak bir oyuncak girdi üzerindeki soğuk bir çalıştırmadan tek bir şanslı sayı raporlar; bu, kullanıcıların gerçekte karşılaştığı davranışı değil, başlangıcı, tam zamanında derlemeyi ve derleyicinin kullanılmayan kodu kaldırma yeteneğini ölçer. Örnek bir kıyaslama getirin ve sorgulayın: ısınıyor mu, çok sayıda yineleme çalıştırıyor mu, varyansı raporluyor mu, temsili veri boyutları ve dağılımları kullanıyor mu ve sonucundaki ölü kod ortadan kaldırmayı engelliyor mu. Rakip çekim, dürüst kıyaslamaların hızlı mikro kıyaslamalardan yazması ve çalıştırması daha yavaş olmasıdır; bu yüzden ucuz yaklaşıklıkların nerede kabul edilebilir olduğuna ve nerede titizlik talep ettiğinize karar verin. Tedarik ve gözetim organlarının sayıları yeniden üretmenizi isteyeceği kamusal ya da düzenlenen bir ortamda, iddianın yalnızca öne sürülmek yerine doğrulanabilmesi için cihazı, iş yükünü ve ortamı sonucun yanında yakalayın.

6. **Performans işi aynı mühendisler için özelliklerle yarıştığında nasıl karar veriyorsunuz ve bütçe yetkisi kimde?** Performans keskin biçimde azalan getiriye sahiptir; bu yüzden profil güdümlü ilk düzeltme gecikmeyi yarıya indirirken onuncusu kod karmaşıklığını iki katına çıkararak bir yüzde kırpabilir ve bir kural olmadan en yüksek ses ya da en yakın son tarih kazanır. Rakip değerlendirmeler gerçektir: düzeltilmemiş performans borcu sessizce bileşir ve sonradan eklemesi daha pahalı hale gelir; yine de hızın bütçenin ötesinde kovalanması yol haritasını aç bırakır ve gelecekteki işi yavaşlatan karmaşıklık ekler. Her kritik yol için mevcut bütçe durumunu, mevcut durumun makine ya da kaybedilen dönüşüm olarak tahmini maliyetini ve bir sonraki optimizasyonun marjinal getirisini getirin; böylece ödünleşim baskıyla değil kanıtla yapılır. Büyük bir kurumsal ya da kamu programı için performans bütçesine kimin sahip olduğunu ve mühendislik zamanını ona karşı harcamayı kimin yetkilendirebileceğini adlandırın, çünkü kimsenin savunmakla yükümlü olmadığı bir hedef sessizce aşınan bir hedeftir.

## Sektör merceği

**Girişim.** Teslimat hızı süreci yener; bu yüzden yeniden yazmalara ve büyük performans çerçevelerine direnin. Kullanıcıların gerçekten şikâyet ettiği yolda bir profil çıkarıcıyla bir öğleden sonra geçirin, en büyük maliyeti (çoğu zaman bir N+1 sorgusu ya da kazara bir doğrusal tarama) düzeltin ve kazancın sessizce gerilememesi için CI'ye tek bir hafif yüzdelik bütçesi ekleyin. Derin optimizasyonu, bir sezgi değil gerçek bir sayı kodun çok yavaş olduğunu söylediği ana saklayın.

**Küçük işletme.** Performans uzmanı ve sıkı bir bütçe olmadan, zaten ödediğiniz araçlara yaslanın: çalışma zamanınızdaki profil çıkarıcı, barındırma panonuzdaki gecikme yüzdelikleri ve veritabanınızdaki yerleşik sorgu çözümleyici. Müşterilerin hissettiği bir şeye, sayfa yükleme ya da ödeme süresi gibi, bağlı bir iki sade bütçe belirleyin ve bir ihlali, kadrolayamayacağınız bir ayar projesi başlatmak yerine daha hızlı bir katman satın almak ya da en kötü sorguyu düzeltmek için bir sinyal olarak ele alın.

**Kurumsal.** Filo ölçeğinde performans doğrudan maliyettir; bu yüzden onu paylaşılan bir disiplin olarak yönetin: standart profil çıkarma araçları, iş metriklerine bağlı yüzdelik bütçeleri ve hiçbir tek takımın yavaş sürünmesinin tüm bulut faturasını şişirmemesi için tutarlı uygulanan CI gerileme kapıları. Gecikmeyi, ayırmayı ve verimi hizmetler boyunca temel çizgilere karşı izleyin ve yeniden üretilebilir kıyaslama kanıtını tutun, çünkü büyük bir filoda %30 CPU azalması denetlemeye ve HDA cezalarına karşı savunmaya değer yinelenen bir tasarruftur.

**Kamu.** Performans bir erişim garantisidir: zayıf bir bağlantı üzerinde eski bir telefonda yüklenen bir sayfa, bir vatandaşın yardım başvurusunu tamamlayıp tamamlamayacağını belirler. Gerçekçi düşük uç cihazlara ve kısılmış ağlara karşı açık bütçeler belirleyin ve tedarik ve gözetim organlarının sayıları güvenle kabul etmek yerine doğrulayabilmesi için cihazı, ağı ve iş yükünü yakalayan yeniden üretilebilir kıyaslama sonuçları yayımlayın. Satıcı iddiaları yerine şeffaf, denetlenebilir ölçümü tercih edin ve tedarikçileri aynı yeniden üretilebilir kanıtla yükümlü tutun.

## Örnekler

**Girişim.** Küçük bir SaaS takımı panolarının yavaş hissettirdiğini fark eder ve onu daha hızlı bir çerçevede yeniden yazmaya heveslenir. Bunun yerine bir profil çıkarıcı ve alev grafiğiyle bir öğleden sonra geçirirler; bu, istek süresinin %70'inin satır başına bir veritabanı sorgusu veren tek bir uç nokta, klasik N+1 kalıbı olduğunu gösterir. Onu tek bir toplu sorguyla değiştirirler, gecikme 1,2 saniyeden 90 milisaniyeye düşer ve düzeltmenin sessizce gerilememesi için hafif bir CI kıyaslamasına 200 ms'lik bir p99 bütçesi eklerler. Yeniden yazma yok, bir öğleden sonra, on kat kazanç.

**Kurumsal.** Bir perakende platformu binlerce örnek çalıştırır ve bulut faturasına tek bir öneri hizmeti hâkimdir. Bir profil çıkarma kampanyası, sık çöp toplama duraklamalarına neden olan ağır ayırma çalkantısını ve zayıf isabet oranına sahip bir önbelleği bulur. Veri yapılarını yerellik için ayarlamak ve önbellek anahtarlarını düzeltmek istek başına CPU'yu %40 düşürür; bu da takımın aynı trafiği %40 daha az makinede çalıştırmasını sağlar. Tasarruf mühendislik çabasını haftalar içinde öder ve ara sıra ihlal edilen bir p99 gecikme HDA'sı artık rahatça tutar; bu da sözleşmesel cezalardan kaçınır.

**Kamu.** Ulusal bir vergi idaresi vatandaşlara eski cihazlarda ve yavaş kırsal bağlantılarda hizmet vermelidir. Takım açık bir bütçe belirler: beyan sayfası, kısılmış 3G profili üzerinde düşük uç bir telefonda 3 saniyenin altında etkileşimli hale gelmelidir. Sayfayı profiller, etkileşimi engelleyen işi keserler ve gözetim organlarının ve erişilebilirlik denetçilerinin iddiayı güvenle kabul etmek yerine doğrulayabilmesi için cihazı, ağı ve iş yükünü yakalayan yeniden üretilebilir kıyaslama sonuçları yayımlarlar. Burada performans bir maliyet kaldıracı değil, hizmeti herkes için kullanılabilir tutan bir erişim garantisidir.

## İş gerekçesi: motivasyonlar, YG ve TSM

Performans mühendisliğinin getirisi üç defterde görünür. Birincisi altyapı maliyetidir: daha hızlı kod aynı işi daha az makinede yapar ve büyük bir filo için %30 CPU azalması, tek seferlik mühendislik çabasını gölgede bırakan doğrudan, yinelenen bir tasarruftur. İkincisi gelir ve memnuniyettir: gecikme dönüşümle, terk etmeyle ve kullanıcı güveniyle ilişkilidir; bu yüzden kuyruğu kırpmak yalnızca bir hijyen görevi değil, bir büyüme kaldıracıdır. Üçüncüsü kaçınılan risktir: bir HDA ihlali ceza taşır ve yük altında eriyen bir lansman itibar hasarı ve yangın söndürme maliyeti taşır.

Toplam sahip olma maliyeti mütevazıdır ve önden yüklüdür. Profil çıkarma araçlarına, kararlı bir kıyaslama ortamına ve CI kapılarına, ayrıca bütçeler yazma ve profilleri okuma disiplinine yatırım yaparsınız. Daha büyük, gizli maliyet alternatiftir: performans borcu sessizce bileşir ve yayından sonra yavaş bir sisteme hız eklemek, onu sürekli korumaktan çok daha pahalıdır. Gerekçeyi liderliğe kendi birimleriyle sunun. Gecikmeyi dönüşüme ya da vatandaş tamamlama oranlarına, CPU'yu aylık bulut harcamasına ve bir gerileme kapısını kaçınılan olaylara çevirin. En güçlü argüman, performansın commit commit korumanın ucuz, çürüdükten sonra kurtarmanın ise yıkıcı olduğudur.

## Anti-kalıplar ve tuzaklar

- **Profil çıkarmadan optimize etmek.** Gerçek maliyet dokunulmadan kalırken darboğaz olmayan kodu ayarlamak.
- **Erken optimizasyon.** Profil çıkarıcının asla işaretlemeyeceği hayali hız için netliği feda etmek.
- **Ortalama raporlamak.** Acı verici bir kuyruğu rahat bir ortalamanın ardına gizlemek; kullanıcılar ortalamayı değil p99'u hisseder.
- **Mikro kıyaslama tiyatrosu.** Optimize edicinin yarı sildiği, ısınma ya da varyans raporlanmayan bir oyuncak iş yükünden sayılar.
- **Geçersiz kılma hikâyesi olmayan önbellek.** Bayat ya da yanlış veri sunarken isabet oranını kovalamak.
- **Daha fazla iş parçacığının yardım edeceğini varsaymak.** Amdahl yasasını ve seri kesri görmezden gelmek, sonra çekişmede boğulmak.
- **Gerileme kapısı yok.** Bütçeyi hiçbir şey CI'de korumadığı için kullanıcıların performans testi olmasına izin vermek.
- **Yanlış ekseni optimize etmek.** Kullanıcılar düşük gecikmeye ihtiyaç duyarken toplu işlemeyle verim satın almak ya da tersi.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Performans yalnızca bir şey bozulduğunda ele alınır. Bütçe, profil çıkarma alışkanlığı, kıyaslama yoktur. Optimizasyon sezgiyle yönlendirilen tahmindir ve ortalamalar kimsenin raporladığı tek metriktir.
- **Düzey 2, Geliştirme:** Bazı takımlar olaylar sırasında profil çıkarır ve birkaç kıyaslama tutar, ama uygulama tutarsızdır ve bireysel hevese bağlıdır. Bütçeler bir iki kritik yol için gayriresmi vardır ve yüzdelikler bazı panolarda görünür, ama hiçbir şey bir gerilemeyi yayımlanmadan önce kapıya koymaz ve her takım kendi yaklaşımını yeniden icat eder.
- **Düzey 3, Standartlaştırma:** Kritik yollar yazılı yüzdelik bütçeleri taşır ve profil çıkarma, kimse optimize etmeden önce belgelenmiş, beklenen ilk adımdır. CI gerileme kapılı performans testleri içerir, dürüst kıyaslama kuralları (ısınma, varyans, temsili veri) yazılıdır ve kuruluş genelinde uygulanır ve her takım kendi yöntemi yerine aynısını izler.
- **Düzey 4, Yönetme:** Kuruluş performansı kontrollü bir özellik olarak ölçer. Gecikme yüzdelikleri, verim, ayırma oranları ve yavaş sorgu sayıları üretimde ve CI'de açık temel çizgilere karşı izlenir, gerilemeler tartışılmak yerine eşiklere karşı nicelleştirilir ve bütçeler dönüşüm ya da bulut harcaması gibi iş metriklerine bağlanır; böylece bir ihlal veriyle desteklenmiş bir kararı tetikler. Kıyaslama kanıtı yeniden üretilebilir ve denetim için cihazı, iş yükü ve ortamıyla yakalanmıştır.
- **Düzey 5, Orkestrasyon:** Performans sürekli iyileştirilir ve kuruluş genelinde bütünleşir. Bütçeler, profil çıkarma, dürüst kıyaslama ve alev grafiği analizi rutin becerilerdir, gerileme kapıları kararlı ve güvenilirdir ve üretim ve CI verisi döngüyü otomatik kapatır. Kuruluş trafik, donanım ve iş öncelikleri kaydıkça bütçeleri uyarlar, çabayı getirinin en yüksek olduğu yollara yeniden dengeler ve performansı periyodik bir kampanya değil kalıcı bir özellik olarak savunur.

## Tartışma fikirleri

1. Kritik yollarınızdan hangisinin bugün yazılı, yüzdelik tabanlı bir bütçesi var ve hangileri yalnızca umutla korunuyor?
2. Bir profil çıkarıcı sizi en son ne zaman şaşırttı ve bu size zamanın nerede harcandığı varsayımınız hakkında ne öğretti?
3. Kıyaslamalarınız ısınıyor, varyansı raporluyor ve temsili veri kullanıyor mu, yoksa optimize ediciyi mi ölçüyor?
4. Bir profil çıkarma kampanyasının daha ucuz yapabileceği kodu örtmek için makineleri nerede harcıyorsunuz?
5. En çok paralelleştirilmiş iş yükünüz için seri kesir nedir ve Amdahl yasası kovaladığınız hız artışını sınırlıyor mu?
6. Bir takım arkadaşı p99 gecikmesini ikiye katlayan bir değişiklik birleştirseydi, kimse fark edene kadar ne kadar geçerdi ve nasıl öğrenirlerdi?

## Önemli çıkarımlar

- Optimize etmeden önce ölçün; darboğaz nadiren tahmin ettiğiniz yerdedir ve erken optimizasyon kazanç olmadan netliğe mal olur.
- "Yeterince hızlı"yı bir yüzdelik bütçesi olarak tanımlayın, çünkü ortalamalar gerçek kullanıcıların yaşadığı kuyruğu gizler.
- Mikro ayar yerine algoritmik kazançları (daha iyi bir Büyük O sınıfı) tercih edin ve gecikmeye mi yoksa verime mi ihtiyacınız olduğunu bilin.
- Paralelliğin sınırlarına (Amdahl yasası) ve önbelleğin tehlikelerine (geçersiz kılma ve bayatlık) saygı gösterin.
- Isınma, varyans ve temsili iş yükleriyle dürüstçe kıyaslayın ve mikro kıyaslamalara güvenmeyin.
- Performansı CI'de kapıya koyun (bölüm 2.4) ve üretimde gözlemleyin (bölüm 9.2); bölüm 3.5'teki sistem düzeyi görünümü tamamlayın.
- Performans kurumlar için maliyet, kamu için erişimdir ve sürekli korumak ucuz ama sonradan eklemek pahalıdır.

## Kaynaklar ve ileri okuma

- Brendan Gregg, *Systems Performance: Enterprise and the Cloud* (profiling, flame graphs, and method).
- Brendan Gregg, *BPF Performance Tools* (practical observability and profiling on Linux).
- Donald E. Knuth, "Structured Programming with go to Statements" (*ACM Computing Surveys*, 1974): the source of the premature-optimisation maxim.
- Donald E. Knuth, *The Art of Computer Programming* (algorithmic analysis and complexity).
- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein, *Introduction to Algorithms* (Big O and algorithmic efficiency).
- Gene M. Amdahl, "Validity of the Single Processor Approach to Achieving Large-Scale Computing Capabilities" (1967): the origin of Amdahl's law.
- Ulrich Drepper, "What Every Programmer Should Know About Memory" (the memory hierarchy and data locality).
- Martin Kleppmann, *Designing Data-Intensive Applications* (latency, throughput, and tail behaviour in systems).
- Aleksey Shipilev, "JMH and the pitfalls of microbenchmarking" (honest benchmarking practice on managed runtimes).
- Ilya Grigorik, *High Performance Browser Networking* (client-side and network performance for low-bandwidth users).
