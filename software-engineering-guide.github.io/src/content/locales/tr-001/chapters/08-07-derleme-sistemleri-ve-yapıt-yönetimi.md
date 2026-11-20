# 8.7 Derleme sistemleri ve yapıt yönetimi

## Genel bakış ve motivasyon

Derleme, kaynak kodunuzun teslim edebileceğiniz bir şeye dönüştüğü yerdir. Bölüm 8.1'deki her işlem hattı buradan başlar: herhangi bir şeyi test etmeden, taramadan, dağıtmadan ya da terfi ettirmeden önce bir derleme sisteminin bir kaynak dosya ağacını somut bir yapıta, yani derlenmiş bir ikili dosyaya, bir pakete, bir konteyner imajına ya da statik varlıklardan oluşan bir demete dönüştürmesi gerekir. O ilk adım yavaş, kararsız ya da yeniden üretilemezse, ardındaki her adım hasarı devralır. İki makinede farklı çıktı üreten bir derleme, çalıştırdığınız her testi ve topladığınız her onayı baltalar, çünkü incelediğiniz şey, teslim ettiğiniz şey olduğu kanıtlanabilir biçimde aynı değildir.

Bu bölüm o ilk adımla ve çıktısıyla ilgilidir: yapıtları inşa eden derleme sistemi ve onları saklayan, sürümleyen, güvenceye alan ve terfi ettiren yapıt yönetimi. Bilinçli olarak, tam sürekli entegrasyon ve sürekli teslimat (CI/CD) işlem hattını kapsayan bölüm 8.1'den daha dardır. Burada konu derlemenin kendisi ve ürettiği yapıtlardır. Girdileri nasıl izleyip denetlediğinizi yöneten yazılım yapılandırma yönetimi (bölüm 2.10) ve içeri çektiğiniz üçüncü taraf kodunu yöneten bağımlılık ve tedarik zinciri yönetimi (bölüm 2.18) ile tamamlayıcıdır. Derleme, bu girdilerin buluştuğu yerdir: kaynağınız, bağımlılıklarınız ve yapılandırmanız tek bir değişmez çıktıda birleşir.

Büyük takımlar için bahisler somuttur. Yüzlerce mühendis günde birçok kez çok dakikalık derlemeleri beklediğinde, toplam kayıp zaman hemen her diğer mühendislik maliyetini gölgede bırakır. Yapıtlar değişebilir, izlenmeyen ya da ortam başına yeniden derlenen şeyler olduğunda, üretimde ne çalıştığını güvenle söyleme yeteneğinizi kaybedersiniz. Kurumsal ve kamu ortamlarında bu izlenebilirlik isteğe bağlı değildir. Denetçilerin ve güvenlik görevlilerinin, üretimdeki ikili dosyanın incelenmiş kaynaktan, güvenilir bir sistemde derlendiğine ve kayıtlı bir gözetim zincirine sahip olduğuna dair kanıta ihtiyacı vardır. Disiplinli bir derleme ve yapıt pratiği, bu kanıtı her denetimden önceki bir telaş yerine normal işin yan ürünü haline getirir.

## Temel ilkeler

- Derleme, teslimatın ilk adımıdır: hızını ve doğruluğunu üretim kaygıları olarak ele alın.
- Yeniden üretilebilir ve mümkün olduğunda kapalı (hermetic) derlemeleri hedefleyin: aynı girdiler, her seferinde aynı çıktı.
- Bir yapıtı bir kez derleyin, sonra tam o yapıtı ortamlar boyunca terfi ettirin.
- Yapıtları değişmez ve içerik adresli yapın ve anlamlı biçimde sürümleyin.
- Yapıtları saklama, erişim denetimi ve köken bilgisi olan yönetilen bir depoda saklayın.
- Agresif biçimde önbelleğe alın, ama önbelleği yalnızca bir hız hilesi değil, bir güvenlik sınırı olarak görün.
- Köken bilgisini, imzaları ve malzeme listesini işten sonra değil, derleme zamanında yakalayın.

## Öneriler

### Derlemeyi teslimatın ilk adımı olarak görün

Derleme sisteminiz üretim altyapısıdır ve onu öyle fonlayıp sürdürmelisiniz. Bir yapıtın hızlı ve doğru inşası, CI/CD'nin (bölüm 8.1) dayandığı temeldir. Takımlar derlemeyi sonradan akla gelen bir şey, kimsenin sahip olmadığı bir yığın kabuk betiği olarak ele aldığında, bunun bedelini kararsız işlem hatlarıyla, gizemli "benim makinemde çalışıyor" kusurlarıyla ve 11. Bölümde anlatılan tüm mühendislik akışını aşındıran yavaş geri bildirimle öderler. Derlemeye bir sahip, kodla birlikte sürüm kontrolünde tutulan bir tanım (depo yapısı üzerine bölüm 2.14) ve diğer her kritik sistemle aynı inceleme disiplinini verin.

### Derlemeleri yeniden üretilebilir ve, yapabildiğinizde, kapalı yapın

[Yeniden üretilebilir bir derleme](https://en.wikipedia.org/wiki/Reproducible_builds), aynı kaynaktan bit bit özdeş çıktı üretir; böylece herkes bağımsız olarak yeniden derleyip bir yapıtın kaynağıyla eşleştiğini doğrulayabilir. Bu, bir ikili dosyanın commit ile dağıtım arasında kurcalanmadığına güvenmenizi sağlayan özelliktir. Oraya varmak, belirsizlik kaynaklarını ortadan kaldırmak demektir: gömülü zaman damgaları, mutlak dosya yolları, derleme sırası rastgeleliği ve sonuçları zamanla kayan ağ çekmeleri.

Kapalı bir derleme, her girdiyi baştan bildirerek ve ağa ya da ana makinenin çevresel durumuna ulaşamayan yalıtılmış bir ortamda çalışarak daha da ileri gider. Bildirdiğiniz şey dışında derlemeye hiçbir şey girmez: sabitlenmiş araç zinciri sürümleri, sabitlenmiş bağımlılıklar, açık kaynak dosyaları. Kapalılık, yeniden üretilebilirliği şansa değil güvenilir kılan şeydir. Tam kapalılığın araçlarda ve disiplinde gerçek bir maliyeti vardır, bu yüzden onu ikili bir durum değil bir yön olarak görün. Kısmi ilerleme bile, derleyici sürümünüzü sabitlemek, bağımlılıkları satıcılamak ya da kilitlemek, zaman damgalarını ayıklamak, çabanın küçük bir kısmıyla güvenin çoğunu satın alır.

### Bağımlılıkları kilit dosyalarıyla belirlenimci çözün

Her derleme üçüncü taraf kodu içeri çeker ve bunu nasıl çözdüğünüz derlemenizin belirlenimci olup olmadığını belirler. Bir [kilit dosyası](https://en.wikipedia.org/wiki/Lock_file), her doğrudan ve dolaylı bağımlılığın tam çözümlenmiş sürümünü ve kriptografik özetini kaydeder; böylece aylar sonraki bir derleme tam olarak aynı grafa çözülür. Kilit dosyasını commit edin, ondaki değişiklikleri incelenebilir olaylar olarak görün ve her çekmede özetleri doğrulayın ki değişmiş bir üst akış paketi fark edilmeden içeri sızamasın. Bu, bölüm 2.18'deki tedarik zinciri disiplininin derleme zamanı yüzüdür. Kilit dosyası olmadan "dün derlendi" size bugün neyin derleneceğine dair hiçbir şey söylemez, çünkü kayan bir sürüm aralığı sessizce yeni bir sürüm çekebilir ya da bir saldırgan kötü amaçlı bir tane yayımlayabilir.

### Artımlı derlemeleri ve önbelleğe almayı, yerelde ve uzaktan kullanın

Kimse değişmeyeni yeniden derlememelidir. Artımlı derlemeler hangi girdilerin hangi çıktıları beslediğini izler ve yalnızca bir değişiklikten etkilenen parçaları yeniden derler. Bir derleme önbelleği, önceki işin çıktılarını girdilerinin özetiyle anahtarlayarak saklar; böylece değişmemiş bir hedef yeniden hesaplanmak yerine getirilir. Yerel bir önbellek bir geliştiricinin döngüsünü hızlandırır; uzak ya da dağıtık bir derleme önbelleği sonuçları tüm takım ve CI filosu arasında paylaşır; böylece belirli bir girdiyi ilk derleyen maliyeti öder ve diğer herkes önbellek isabeti alır. Büyük bir tek depoda bu, on dakikalık bir derleme ile on saniyelik bir derleme arasındaki farktır.

Getiri, yapabileceğiniz en yüksek kaldıraçlı yatırımlardan biri olan geliştirici geri bildirim hızıdır. Hızlı, doğru geri bildirim mühendisleri akışta tutar ve kod yazmak ile çalışıp çalışmadığını bilmek arasındaki döngüyü kısaltır. Yine de önbelleğin doğruluğunu dikkatle koruyun: gerçek bir girdiyi (bir ortam değişkeni, bir araç sürümü) dışarıda bırakan bir önbellek anahtarı, hata ayıklaması çıldırtıcı olan bayat sonuçlar üretir. Önbellek, girdi özetlemesinin eksiksizliği kadar güvenilirdir.

### Ölçeğinize uyan derleme araçlarını seçin

Derleme araçları bir yelpaze üzerinde durur. Hafif uçta, [Make](https://en.wikipedia.org/wiki/Make_(software)) ve dile özgü araçlar basit bir bağımlılık grafını modeller ve tek bir hizmet ya da küçük bir depo için yeterlidir. Ortada, Java dünyası için Gradle ve Maven gibi ekosistem araçları ya da Go, Rust ve JavaScript için standart araç zincirleri bağımlılık çözümlemesi ve gelenekler ekler. Ağır uçta, [Bazel](https://en.wikipedia.org/wiki/Bazel_(software)) ve benzeri tek depo derleme araçları gibi graf tabanlı sistemler tüm derlemeyi hedeflerin ince taneli, kapalı bir [yönlü döngüsüz grafı](https://en.wikipedia.org/wiki/Directed_acyclic_graph) olarak modeller; bu, büyük bir kod tabanında hassas artımlılığı, uzak önbelleğe almayı ve uzak yürütmeyi mümkün kılar.

Ağır araçlar, birçok birbirine bağımlı projeniz, büyük bir tek depo (bölüm 2.14) ya da takımlarınızı boğan derleme süreleriniz olduğunda karşılığını verir. Gerçek bir yatırıma mal olur: daha dik bir öğrenme eğrisi, geçiş çabası ve derleme tanımlarını sürdürecek özel bir takım. Bazel sınıfı araçları moda olduğu için benimsemeyin. Derleme grafınız, ince taneli önbellekleme ve paralellik işletme maliyetinden daha fazla mühendislik zamanı geri kazandıracak kadar büyük olduğunda benimseyin. Çoğu küçük ve orta boy sistem için, uzak önbellekli iyi bir ekosistem aracı tatlı noktadır.

### Yapıtları yönetilen bir depoda saklayın

Bir yapıtı derledikten sonra bir eve ihtiyacı vardır. Bir [yapıt deposu](https://en.wikipedia.org/wiki/Software_repository) (kayıt defteri de denir) paketlerinizi, konteyner imajlarınızı ve ikili dosyalarınızı sürümleme, erişim denetimi ve üst veriyle saklar. Kaynak deponuzun karşılığıdır: kaynak girer, yapıtlar çıkar, ikisi de yönetilir. İyi bir depo, iç yapıtları yayımlamak ve almak için tek bir güvenilir yer verir, dış olanları vekiller ve önbelleğe alır; böylece her derlemede genel internete uzanmazsınız ve kimin neyi ne zaman yayımladığını kaydeder. Konteyner imajlarının kendi kayıt defteri gelenekleri vardır ve diğer paket tiplerinin kendileri vardır, ama disiplin aynıdır: yönetilen, erişim denetimli bir depodan gelmeyen hiçbir şey üretimde çalışmaz.

### Yapıtları sürümleyin ve değişmez ve içerik adresli yapın

Her yapıta anlamlı bir sürüm verin. [Anlamsal sürümleme](https://en.wikipedia.org/wiki/Software_versioning) (major.minor.patch), bir değişikliğin doğasını tüketicilere iletir: major artışı uyumsuz bir değişikliği, minor uyumlu özellik eklemeyi, patch hata düzeltmeyi işaret eder. İnsan tarafından okunabilir sürümün yanında, her yapıtı içeriğinin kriptografik özetiyle tanımlayın; böylece içerik adresli olur. Çoğu zaman digest denen içerik adresi, tek bir bayt değişirse değişen bir parmak izidir ve kesin bir yapıta belirsizlik olmadan başvurmanıza ve her türlü kurcalamayı algılamanıza izin verir.

Yayımlanmış yapıtları değişmez yapın: bir sürüm yayımlandığında asla değişmez. Aynı sürüm altında farklı baytları yeniden yayımlamak bir tedarik zinciri tehlikesi ve hata ayıklama kâbusudur, çünkü iki kişi "sürüm 1.4.2"ye sahip olup farklı yazılımlara sahip olabilir. "latest" gibi değişebilir etiketler insanlar için kolaydır ama önemli olan her şey için her zaman kaydettiğiniz belirli bir değişmez digest'e çözülmelidir. Kayan etiketle değil digest ile dağıtın; böylece test ettiğiniz şeyin çalıştırdığınız şey olduğu kanıtlanabilir olur.

### Bir kez derle, her yere terfi ettir

Bir yapıtı bir kez derleyin, sonra aynı yapıtı ortamlarınız boyunca taşıyın: geliştirme, hazırlık, üretim. Bu "bir kez derle, her yere terfi ettir" kuralı en önemli yapıt yönetimi pratiğidir. Ortam başına yeniden derlerseniz, test edilen yapıtın dağıtılan yapıt olduğu garantisini çöpe atmış olursunuz, çünkü her yeniden derleme farklı bir bağımlılık çekebilir ya da biraz farklı bir makinede çalışabilir. Terfi bir üst veri işlemidir: önceden derlenmiş, önceden test edilmiş bir digest'i bir sonraki ortam için onaylanmış olarak işaretlersiniz ve onu yeniden derleyerek değil, dışsallaştırılmış yapılandırma (bölüm 2.10) ile o ortam için yapılandırırsınız. Bu, ikili dosyayı sabit ve yapılandırmayı değişken tutar; hem güvenilirlik hem denetlenebilirlik için istediğiniz ayrım tam olarak budur.

### Köken bilgisini yakalayın, yapıtları imzalayın ve bir SBOM üretin

Derleme zamanında yapıtın nereden geldiğini kaydedin ve değiştirilmediğini kanıtlayın. Köken bilgisi, bir yapıtın nasıl derlendiğine dair imzalı bir ifadedir: hangi kaynak commit'i, hangi derleyici, hangi girdiler. Bir yapıtı imzalamak, tüketicilerin çalıştırmadan önce özgünlüğü ve bütünlüğü doğrulamasına izin verir ve dağıtım sırasında imzaları doğrulamak döngüyü kapatır. Bir [yazılım malzeme listesi](https://en.wikipedia.org/wiki/Software_supply_chain) (SBOM), yani bir yapıtın içindeki bileşenlerin ve bağımlılıkların eksiksiz bir envanteri, yeni bir güvenlik açığı açıklandığında "etkileniyor muyuz?" sorusunu, derleme günlüklerinde günlerce kazı yapmak yerine dakikalar içinde yanıtlamanızı sağlar.

SLSA (Supply-chain Levels for Software Artifacts) gibi çerçeveler size derleme zamanı bütünlüğü için kademeli bir model verir: daha yüksek düzeyler kapalı, yalıtılmış derlemeler ve taklit edilemez köken bilgisi gerektirir. Bunların hepsini, bilginin yetkili ve toplaması ucuz olduğu derlemede üretin; pahalı ve güvenilmez olduğu sonradan yeniden oluşturmaya bırakmayın. Bu iş doğrudan bölüm 4.9'un güvenli yazılım geliştirme yaşam döngüsüne ve bölüm 2.18'in tedarik zinciri kaygılarına hizmet eder.

### Önbelleği güvenceye alın, saklamayı ve maliyeti yönetin

Paylaşılan bir derleme önbelleği, paylaşılan bir güven sınırıdır. Bir saldırgan zehirlenmiş bir girdi yazabilirse, onu çeken her tüketici ele geçirilmiş kodu çalıştırır ve hız avantajı bir saldırı yüzeyine dönüşür. Önbelleği kimlik doğrulamayla koruyun, yazma erişimini dar kapsamlandırın (çoğu zaman yalnızca güvenilir CI, asla geliştirici dizüstü bilgisayarları değil) ve önbellek anahtarlarının her gerçek girdiyi özetlediğinden emin olun; böylece zehirlenmiş ya da bayat bir girdi meşru biri gibi davranamaz. Önbellek zehirlenmesini, özellikle takımlar arasında paylaşılan uzak önbellekler için gerçek bir tehdit modeli olarak görün.

Yapıtlar da maliyet biriktirir. Konteyner imajları ve derleme çıktıları büyüktür ve sınırsız bir kayıt defteri, depolama faturaları ve yavaş aramalar konuyu zorlayana kadar büyür. Saklama politikaları tanımlayın: üretime terfi etmiş her yapıtı ve çalışan bir sistemin başvurduğu her şeyi tutun, eski geliştirme ve çekme isteği derlemelerini otomatik süresi dolsun ve neyi sildiğinizi kaydedin. Amaç, yeniden üretilebilirlik ve denetim için ihtiyacınız olanı koruyup gürültüyü döken, sizi şaşırtan değil bilinçli seçtiğiniz bir maliyetle bir depodur.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| Ağır graf derleme aracı (Bazel sınıfı) | İnce taneli artımlılık, uzak önbellek ve yürütme, devasa tek depolara ölçeklenir | Dik öğrenme eğrisi, geçiş maliyeti, özel bir derleme takımı gerektirir |
| Hafif derleme aracı (Make, yerel) | Basit, düşük yük, benimsemesi hızlı | Ölçekte zayıf artımlılık ve önbellekleme, zayıf kapalılık |
| Uzak/dağıtık derleme önbelleği | Paylaşılan sonuçlar, filo genelinde dramatik hızlanmalar | Önbellek zehirleme yüzeyi, doğruluk eksiksiz girdi özetlemesine bağlı |
| Tam kapalı derlemeler | Güvenilir yeniden üretilebilirlik, güçlü köken bilgisi | Gerçek araç ve disiplin maliyeti, daha zor yerel iş akışları |
| Bir kez derle, her yere terfi ettir | Test edilen yapıt teslim edilen yapıta eşit, temiz denetim izi | Dışsallaştırılmış yapılandırma ve disiplinli terfi gerektirir |
| Değişmez, içerik adresli yapıtlar | Kurcalamaya karşı belirgin, belirsizlik olmayan başvurular | Kayan etiketlerden daha az kullanışlı, yönetilecek daha çok depolama |
| Uzun yapıt saklama | Tam yeniden üretilebilirlik ve denetim geçmişi | Depolama maliyeti, temizlik politikası olmadan yavaş aramalar |

Yinelenen gerilim, hız ile güven arasındadır. Önbellekleme, paylaşılan derleme çiftlikleri ve kayan etiketlerin hepsi derlemeleri daha hızlı ve kolay yapar ve her biri, özensizce kullanıldığında, tam olarak ne derlediğinizi söyleme ve kurcalanmadığını kanıtlama yeteneğinizi zayıflatır. Bunu, güvenilir yolu hızlı yol yaparak çözün. Eksiksiz bir girdi özeti önbelleği hem hızlı hem doğru yapar. Digest ile dağıtmak etiketle dağıtmak kadar hızlıdır ve çok daha güvenlidir. Derlemede bir SBOM üretmek saniyelere mal olur ve günler kazandırır. Bütünlüğü baştan hızlı yola mühendislikle yerleştirirseniz, nadiren hız ile bütünlük arasında seçim yapmak zorunda kalırsınız.

## Takımınızla tartışılacak sorular

1. **Geçen çeyreğin üretim yapıtını bugün yeniden derleyip aynı baytları alabilir miyiz ve alamıyorsak eksik olan ne?** Bu, derleme disiplininizin en keskin sınavıdır, çünkü yeniden üretilebilirlik sabitlenmiş araç zincirlerinin, kilitlenmiş bağımlılıkların ve ortadan kaldırılmış belirsizliğin birlikte çalışmasına bağlıdır. Birkaç ay önce teslim edilmiş belirli bir yapıtı seçin ve onu kayıtlı kaynak commit'inden gerçekten yeniden derlemeyi deneyin. Girişimden öğrendikleriniz herhangi bir politika belgesinden daha değerlidir: belki bir bağımlılık aralığı kaymıştır, belki derleyici sürümü hiç sabitlenmemiştir, belki bir zaman damgası içine gömülüdür. Bulduğunuz boşluklar yeniden üretilebilirlik birikiminizdir ve onları kapatmak, denetlediğiniz şeyin çalıştırdığınız şey olduğuna güvenmenizi sağlar; bu gözetim zincirinin yasal bir gereklilik olduğu düzenlemeye tabi ve kamu ortamlarında son derece önemlidir.

2. **Her yapıtı bir kez derleyip terfi mi ettiriyoruz, yoksa ortam başına yeniden mi derliyoruz ve hangisi olduğunu nasıl kanıtlardık?** Birçok takım tek bir yapıtı terfi ettirdiğine inanır, ama yakından baktığında hazırlık ve üretimin her birinin biraz farklı girdilerle yeni bir derlemeyi tetiklediğini keşfeder. Gerçek bir sürümü commit'ten üretime izleyin ve her ortamdan aynı digest'in mi geçtiğini yoksa yol boyunca yeni baytların mı üretildiğini doğrulayın. Yeniden derlemeler bulursanız, test garantilerinizin sandığınızdan daha zayıf olduğu bir yer bulmuşsunuz demektir, çünkü test edilen yapıt ile dağıtılan yapıt kanıtlanabilir biçimde özdeş değildir. Düzeltme, yani yapılandırmayı dışsallaştırarak ikili dosyayı sabit tutup ayarları değiştirmek, hem güvenilirlikte hem çok daha temiz bir denetim hikâyesinde karşılığını verir.

3. **Yarın yaygın bir kütüphanede kritik bir güvenlik açığı duyurulsaydı, onu içeren her yapıtı ne kadar hızlı listeleyebilirdik?** Bu soru, derleme zamanı köken bilginizin ve SBOM pratiğinizin gerçek mi yoksa hayalî mi olduğunu sınar. Yaygın kullanılan bir bileşenin istismar edilebilir olduğu ortaya çıktığında, saatler içinde toparlanan kurumlar derleme zamanında bir malzeme listesi üretip her yapıtla birlikte saklayanlardır; haftalar içinde toparlananlar derleme günlüklerini grep'leyip mühendislerle görüşenlerdir. Senaryoyu gerçekten bağımlı olduğunuz bir kütüphaneyle somut olarak yürütün ve cevabın bugün ne kadar süreceğini ölçün. O süre ile "dakikalar" arasındaki boşluk tedarik zinciri maruziyetinizin doğrudan ölçüsüdür ve doğrudan bölüm 4.9'daki güvenli geliştirme yaşam döngüsü çalışmasına bağlanır.

4. **Derlemelerimiz her gün ne kadar mühendislik zamanına mal oluyor ve onları hızlandırmanın iş gerekçesi nedir?** Derleme gecikmesi, her mühendisin her değişiklikte ödediği bir vergidir ve büyük bir takım ölçeğinde toplamı hafife almak kolaydır, çünkü hiçbir tekil bekleme pahalı hissettirmez. Ölçmeye karar vermek, belirsiz bir şikâyeti uzak önbellek, daha iyi artımlılık ya da daha ağır derleme araçlarının maliyetine karşı tartabileceğiniz bir sayıya dönüştürür. Yerel ve CI derleme sürelerinizin ortancasını ve en kötü durumunu, günlük derleme sayısını ve yavaş bir derlemenin birini ne sıklıkla akıştan bağlam değiştirmeye ittiğine dair dürüst bir tahmini getirin. Karşıt husus, daha hızlı derlemelerin bedava olmadığıdır: uzak önbellek ve dağıtık yürütme çalıştırılacak ve güvenceye alınacak altyapı ekler ve ağır araçlar bir bakım takımı ekler. Kurumsal ya da kamu kurumu için, yavaş geri bildirimin birçok takım boyunca verim ve moral maliyetini sayın; bu genellikle altyapı faturasını gölgede bırakır ve liderliğin zaten fonladığı çerçevenin tam kendisidir.

5. **Paylaşılan derleme önbelleğimize kim yazabiliyor ve zehirlenmiş bir girdinin üretime ulaşmasını ne engelliyor?** Paylaşılan bir önbellek, bir hız kazancını yeni bir güven sınırıyla takas eder ve bir mühendisin sonucunun tüm filoya hizmet etmesini sağlayan aynı mekanizma, tek bir bozulmuş ya da kötü amaçlı girdinin onu çeken herkesi tehlikeye atmasına izin verir. Büyük bir takım için etki alanı tüm kurumdur, bu yüzden bu, bir aracın varsayılanlarının neyse o olması değil, bilinçli bir karar hak eder. Her önbelleğe kimin ve neyin yazma erişimine sahip olduğunun listesini, yazmaların geliştirici dizüstü bilgisayarları yerine güvenilir CI ile sınırlı olup olmadığını ve önbellek anahtarlarınızın her gerçek girdiyi özetleyip özetlemediğini getirin; böylece bayat ya da zehirlenmiş bir girdi meşru biri gibi davranamasın. Gerilim, en sıkı denetimlerin geliştiricilerin önbellek girdilerini kendi makinelerinden ittiği kolay yolu yavaşlatmasıdır. Kurumsal ve kamu ortamlarında önbellek zehirlenmesini tedarik zinciri modelinizde açık bir tehdit olarak görün ve bir sürüme kod enjekte edebilen diğer her üretim sistemine uyguladığınız aynı erişim denetimlerini, günlüklemeyi ve incelemeyi isteyin.

6. **Derleme grafımız hangi noktada daha ağır araçları haklı çıkarıyor ve eşiği aştığımızı nasıl bileceğiz?** Hafif bir ekosistem aracı ile Bazel gibi graf tabanlı bir sistem arasındaki seçim, bu alandaki daha pahalı ve geri alınması zor kararlardan biridir, çünkü büyük bir kod tabanını ince taneli derleme tanımlarına geçirmek aylara ve özel bir takıma mal olur. Eşiği önceden kararlaştırmak, ya moda olduğu için ihtiyacınız olmayan karmaşıklığı benimsemenizi ya da derleme süreleri her takımı boğduktan çok sonra bile hafif bir araca tutunmanızı önler. Derleme grafınızın boyutunu ve birbirine bağımlılığını, güncel derleme ve önbellek isabet ölçütlerini ve aracın geri kazandıracağı mühendislik zamanına karşı geçişin ve süregelen bakımın gerçekçi bir maliyet tahminini getirin. Karşıt çekim, ağır araçların hiçbir şeyin ölçekte eşleşemeyeceği hassas artımlılık ve uzak yürütme sağlamasıdır, ama yalnızca grafınız bunun karşılığını verecek kadar gerçekten büyükse. Büyük bir kurum ya da kamu kurumu için, aracın kapalılık ve köken bilgisi garantilerinin denetim ve tedarik zinciri gereksinimlerini karşılamaya yardım edip etmediğini de tartın; bu hesabı ham hızın ötesine kaydırabilir.

## Sektör merceği

**Girişim.** Küçücük bir takım ve derleme altyapısı için pist olmadan, hafif tutun: dile özgü derleme araçları kullanın, ilk günden kilit dosyalarını benimseyin ve konteyner imajlarını "latest" etiketi yerine digest ile dağıtın; çünkü bu alışkanlıklar neredeyse hiçbir şeye mal olmaz ve sizi sonradan bir sınıf "benim makinemde çalışıyor" acısından kurtarır. Ağır graf derleme araçlarına direnin; en kıt kaynağınız mühendislik dikkatidir. Uzak derleme önbelleği, derlemeler birkaç dakikayı aşmaya başladığında uzanmaya değer tek yükseltmedir.

**Küçük işletme.** Özel bir derleme mühendisi olmadan, kendi yapıt altyapınızı işletmek yerine yönetilen hizmetlere yaslanın: barındırılan bir kayıt defteri ve CI sağlayıcınızın yerleşik önbelleği, bir platform takımı olmadan size sürümleme, saklama ve erişim denetimi verir. Seçimi inşa etmek yerine satın almak olarak çerçeveleyin, depolama maliyetleri öngörülebilir kalsın diye otomatik bir süre dolumu politikası belirleyin ve temellerin yerinde olduğundan emin olun: kilitlenmiş bağımlılıklar ve değişmez, digest sabitlenmiş dağıtımlar; çünkü bunlar, işlem hattını tam zamanlı kimse izlemediğinde bile sizi korur.

**Kurumsal.** Birçok takım boyunca sorun tutarlılıktır: ortak, sahipli bir derleme platformu, ortak bir yapıt deposu ve hiçbir grubun güvenilmez bir işlem hattını yeniden icat etmemesi için kilit dosyaları, imzalama, SBOM'lar ve bir-kez-derle-terfi-ettir için uygulatılan standartlar. Bir uzak önbelleğe ve derleme grafı haklı çıkardığında graf tabanlı araçlara yatırım yapın ve önbelleği kapsamlı yazma erişimi ve denetim günlüklemesiyle yönetilen bir güven sınırı olarak görün. Yapıtları saklama politikaları ve köken bilgisiyle denetlenen bir varlık alanı olarak yönetin; böylece herhangi bir üretim bileşeni istendiğinde incelenmiş kaynağa kadar izlenebilir.

**Kamu.** Tedarik kuralları, şeffaflık ve kamusal hesap verebilirlik derleme zamanı bütünlüğünü bir incelik değil, bir uyum gereksinimi yapar. İşlem hattını SLSA gibi kademeli bir çerçeveyle hizalayın, derlemeleri sabitlenmiş araç zincirlerinden yalıtılmış, ağ kısıtlı ortamlarda çalıştırın ve üçüncü taraf bağımlılıkları, kullanılmadan önce onları tarayan ve onaylayan bir iç depo üzerinden vekilleyin. İmzalı SBOM'ları ve köken bilgisini kayıt saklama yasasının gerektirdiği yıllar boyunca değişmez biçimde saklayın, yalnızca imzalı, digest ile tanımlanmış yapıtları dağıtın ve denetçilere ve halka üretimdeki yazılımın tam olarak incelenen ve onaylanan şey olduğunu doğrulamaya hazır olun.

## Örnekler

**Girişim.** Küçük bir tek depo çalıştıran on beş kişilik bir girişim, bu ölçekte doğru tercih olan dile özgü derleme araçları ve hızlı geri bildirimle başlar. Büyüdükçe derleme süreleri beş dakikayı aşar ve mühendisler beklerken bağlam değiştirmeye başlar. Ağır bir graf derleme aracına atlamak yerine, geliştirici makineleri ve CI arasında paylaşılan bir uzak derleme önbelleği eklerler; bu, değişmemiş hedefler yeniden derlenmek yerine getirildiği için çoğu derlemeyi saniyelere indirir. Her dil için kilit dosyalarını benimserler, konteyner imajlarını "latest" etiketi yerine digest ile dağıtırlar ve kayıt defteri faturaları sabit kalsın diye çekme isteği imaj derlemeleri için otomatik süre dolumunu açarlar. Tüm çaba birkaç hafta sürer ve her gün saatlerce mühendislik zamanı geri kazandırır.

**Kurumsal.** Küresel bir finansal hizmetler şirketi yüzlerce mühendis boyunca büyük bir tek depo işletir ve uzak önbellekleme ve uzak yürütmeli graf tabanlı bir derleme sistemi benimser; çünkü ölçeklerinde ince taneli artımlılık, derleme takımının maliyetinden çok daha fazla mühendislik zamanı geri kazandırır. Her yapıt yalıtılmış bir ortamda kapalı derlenir, imzalanır ve ekli bir SBOM ve imzalı köken bilgisiyle yönetilen bir kayıt defterine yayımlanır. Dağıtımlar içerik digest'iyle gerçekleşir ve bir politika motoru imzası doğrulanmayan hiçbir imajı çalıştırmayı reddeder. Yapıtlar hazırlıktan üretime terfi ettirilir, asla yeniden derlenmez; böylece testi geçen ikili dosyanın müşterilere hizmet eden olduğu kanıtlanabilir. Denetçiler bir üretim bileşenini incelenmiş kaynağa kadar izlemeyi istediklerinde, gözetim zinciri bir soruşturma değil bir sorgudur.

**Kamu.** Sistemlerini modernleştiren bir ulusal vergi kurumu, derleme zamanı tedarik zinciri bütünlüğünü bir uyum gereksinimi olarak görür ve işlem hattını SLSA gibi kademeli bir çerçeveyle hizalar. Derlemeler, sabitlenmiş araç zincirlerinden ve kilitlenmiş bağımlılıklarla yalıtılmış, ağ kısıtlı ortamlarda çalışır; böylece çıktı yeniden üretilebilir ve bağımsız olarak doğrulanabilir. Her yapıt, kayıt saklama yasasını karşılamak için yıllarca değişmez biçimde saklanan imzalı bir SBOM ve köken bilgisi taşır. Üçüncü taraf bağımlılıklar, hiçbir derleme onları kullanamadan önce tarayan ve onaylayan bir iç depo üzerinden vekillenir; incelenmemiş kodu ağdan tümüyle uzak tutar. Kurum yalnızca imzalı, terfi ettirilmiş, digest ile tanımlanmış yapıtları dağıttığı için, düzenleyicilere ve halka vatandaşların beyannamelerini işleyen yazılımın tam olarak incelenen ve onaylanan şey olduğunu doğrulayabilir.

## İş gerekçesi: motivasyonlar, YG ve TSM

Derleme ve yapıt disiplininin getirisi ilk olarak geri kazanılan mühendislik zamanı olarak görünür. Yavaş derlemeler her mühendisi her değişiklikte vergilendirir ve maliyet büyük bir kurum boyunca birikir: günde binlerce kez çalışan bir derlemeden dakikalar kırpmak yılda kişi-yıllar geri kazandırır ve ölçmesi daha zor ama aynı derecede gerçek olarak, mühendisleri bağlam değiştirmek yerine akışta tutar. Uzak önbellek ve iyi artımlılık çoğu zaman haftalar içinde kendini öder. Yeniden üretilebilir, bir kez terfi edilen yapıtlar bütün bir "hazırlıkta çalışıyordu" olayları sınıfını azaltır; liderlerin zaten izlediği teslimat ölçütleri olan değişiklik başarısızlık oranını ve ortalama kurtarma süresini düşürür.

Daha büyük, daha az görünür getiri risk azaltmadır. İmzalı yapıtlar, SBOM'lar ve köken bilgisi, bir tedarik zinciri olayını çok haftalık bir acil durumdan kapsamlı, saatler süren bir müdahaleye çevirir ve denetimleri bir yangın tatbikatından bir sorguya dönüştürür. Düzenlemeye tabi ve kamu bağlamlarında bu izlenebilirlik, hiç faaliyet göstermenin bir ön koşuludur; yani yatırım isteğe bağlı değil yapısaldır. Bunu ihmal ettiğinizde toplam sahip olma maliyeti ters yönde işler: değişebilir yapıtlar ve yeniden üretilemeyen derlemeler kimsenin tam olarak hesaplayamadığı bir varlık alanına dönüşür, saklama politikası olmadan depolama sınırsız büyür ve her denetim ve her olay olması gerekenden daha pahalıya mal olur. Liderliğe gerekçeyi sunmak için, derleme hızını mühendislik verimine ve yapıt bütünlüğünü, ikisini de zaten fonladıkları denetim maliyetine ve ihlal maruziyetine bağlayın.

## Anti-kalıplar ve tuzaklar

- **Ortam başına yeniden derleme:** hazırlık ve üretim için yeni baytlar üretmek, test edilen yapıtın dağıtılan yapıt olduğu garantisini çöpe atmak.
- **Kayan etiketle dağıtmak:** değişmez bir digest yerine "latest" ya da değişebilir bir etiket çalıştırmak; böylece çalışan şey öngörülemez ve izlenemez olur.
- **Kilit dosyası yok:** bir derlemenin zamanla farklı ya da kötü amaçlı bağımlılıkları sessizce çekmesine izin veren kayan sürüm aralıkları.
- **Eksik önbellek anahtarları:** önbellek anahtarında gerçek bir girdiyi atlamak; günlerce hata ayıklamayı boşa harcayan bayat sonuçlar üretmek.
- **Güvenceye alınmamış paylaşılan önbellek:** güvenilmeyen yazarların uzak bir önbelleği zehirlemesine izin vermek; böylece tüketiciler ele geçirilmiş çıktıları çekip çalıştırır.
- **Belirlenimci olmayan derlemeler:** çıktının değişmesine yol açan ve doğrulamayı boşa çıkaran gömülü zaman damgaları, mutlak yollar ve sabitlenmemiş araçlar.
- **Ağır araçları erken benimsemek:** derleme grafı bunu haklı çıkaracak kadar büyük olmadan Bazel sınıfı karmaşıklığı üstlenmek.
- **SBOM ve köken bilgisi sonradan akla gelen olarak:** tedarik zinciri üst verisini, derlemede üretmek yerine, pahalı ve güvenilmez olduğu sırada derlemeden sonra yeniden oluşturmak.
- **Sınırsız saklama:** depolama maliyeti ve yavaş aramalar paniklemiş bir temizliği zorlayana kadar eski yapıtların süresini hiç doldurmamak.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Derlemeler, kimsenin sahip olmadığı, çoğu zaman geliştirici makinelerinden çalıştırılan gelişigüzel betiklerdir. Çıktı belirlenimci değildir, bağımlılıklar kilit dosyası olmadan kayar, yapıtlar ortam başına yeniden derlenir ve değişebilir etiketle dağıtılır; paylaşılan önbellek, imzalama ve malzeme listesi yoktur.
- **Düzey 2, Geliştirme:** Bazı takımlar derlemeleri commit edilmiş bir tanımdan CI'ya taşımış ve kilit dosyalarını benimsemiştir, ama pratik kurum genelinde tutarsızdır. Yapıtlar temel sürümlemeyle yönetilen bir depoya düşebilir ve yerel ya da basit bir uzak önbellek yaygın derlemeleri hızlandırır, ancak ortam başına yeniden derlemeler hâlâ olur ve köken bilgisi yamalıdır.
- **Düzey 3, Standartlaştırma:** Yeniden üretilebilir, büyük ölçüde kapalı derlemeler belgelenmiş ve kurum genelinde uygulatılmıştır; sabitlenmiş araç zincirleri ve anahtarları tüm gerçek girdileri özetleyen paylaşılan bir uzak önbellek vardır. Yapıtlar değişmez, içerik adresli, anlamsal sürümlü, bir kez derlenip her yere terfi ettirilir, imzalıdır ve bir SBOM ile gönderilir. Önbellek erişimi denetlenir ve saklama politikaları takımlar arasında tutarlı uygulanır.
- **Düzey 4, Yönetme:** Derleme varlık alanı taban çizgilerine karşı ölçülür ve kontrol edilir. Derleme süreleri, önbellek isabet oranları, geliştirici geri bildirim süresi ve depolama maliyeti açık hedeflerle izlenir, gerilemeler eylemi tetikler ve imza ve köken bilgisi doğrulaması dağıtım zamanında uygulatılır; böylece başarısız bir denetim sürümü engeller. Derleme zamanı tedarik zinciri bütünlüğü SLSA gibi kademeli bir çerçeveye göre değerlendirilir ve sayılar bir sonraki yatırımınızı nereye yapacağınızı yönlendirir.
- **Düzey 5, Orkestrasyon:** Derleme, önbellek, yapıt ve tedarik zinciri pratiği sürekli iyileştirilir ve kurum genelinde bütünleşiktir. Araçlar, saklama ve güvenlik duruşu olaylardan ve denetimlerden öğrendikçe uyum sağlar, uzak yürütme ve önbellekleme kod tabanı geliştikçe ayarlanır ve derleme zamanı bütünlüğü sonradan eklenmek yerine daha geniş güvenli geliştirme yaşam döngüsüne örülür.

## Tartışma fikirleri

1. Güncel yerel derleme sürenizin ortancası ve en kötü durumu nedir ve uzak bir önbellek her ikisine ne yapardı?
2. Bugün yapıtlarınızdan hangileri değişebilir etiketle dağıtılıyor ve her birini digest ile dağıtmak için ne gerekir?
3. Derleme grafınız daha ağır araçları nerede haklı çıkarıyor ve o araçlar nerede kazandırdığından fazlasına mal olur?
4. Paylaşılan derleme önbelleğinize kim yazabiliyor ve zehirlenmiş bir girdinin üretime ulaşmasını ne engelliyor?
5. Son teslim ettiğiniz şey için imzalı bir SBOM üretebilir misiniz ve üretemiyorsanız buna doğru en küçük adım nedir?
6. Derleme yapıtları için saklama politikanız nedir ve depolama bugün size neye mal oluyor ve neye mal olması gerekir?

## Önemli çıkarımlar

- Derleme teslimatın ilk adımıdır: hızını ve doğruluğunu üretim kaygıları olarak fonlayın, çünkü akış aşağısındaki her şey kusurlarını devralır.
- Derlemeleri yeniden üretilebilir ve mümkün olduğunda kapalı yapın; sabitlenmiş araç zincirleri ve kilit dosyalarıyla, böylece denetlediğiniz yapıt teslim ettiğiniz yapıt olduğu kanıtlanabilir olur.
- Yerelde ve uzaktan önbelleğe alın ve artımlı derleyin, ama her gerçek girdiyi özetleyin ve önbelleği güvenceye alın, çünkü paylaşılan bir önbellek paylaşılan bir güven sınırıdır.
- Her yapıtı bir kez derleyin, değişmez ve içerik adresli yapın, anlamlı biçimde sürümleyin ve tam o yapıtı ortamlar boyunca terfi ettirin.
- Köken bilgisini, imzaları ve bir SBOM'u derleme zamanında üretin ve yapıtları saklama ve erişim denetimiyle depolayın; böylece tedarik zinciri bütünlüğü ve denetim hazırlığı normal işin yan ürünü olur.

## Kaynaklar ve ileri okuma

- Jez Humble and David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Titus Winters, Tom Manshreck, and Hyrum Wright (eds.), *Software Engineering at Google: Lessons Learned from Programming Over Time*
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering: How Google Runs Production Systems*
- Peter Smith, *Software Build Systems: Principles and Experience*
- The Open Source Security Foundation, *SLSA: Supply-chain Levels for Software Artifacts* (specification)
- National Institute of Standards and Technology, *Secure Software Development Framework (SSDF), SP 800-218*
- Tom Preston-Werner, *Semantic Versioning Specification (SemVer)*
