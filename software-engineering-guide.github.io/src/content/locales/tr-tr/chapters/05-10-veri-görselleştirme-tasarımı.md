# 5.10 Veri görselleştirme tasarımı

## Genel bakış ve motivasyon

Bir grafik, mürekkepten yapılmış bir argümandır. Veriyi çizdiğinizde, okurun önce neyi fark edeceğini, neyi karşılaştıracağını ve geçip gitmeden önceki iki saniyede hangi sonuca varacağını seçersiniz. İyi yaparsanız zor bir soru kendi kendine cevaplanır: eğilim bellidir, aykırı değer göze çarpar, iki grubun farklı olduğu açıktır. Kötü yaparsanız aynı veri yanıltır, şaşırtır ya da basitçe sıkar ve bilgilendirmesi gereken karar hislerle verilir. [Veri görselleştirme](https://en.wikipedia.org/wiki/Data_and_information_visualization), sayıları insanların ne anlama geldiklerini görmelerini sağlayan resimlere dönüştürme tasarım zanaatıdır.

Bu bölüm o zanaatla ilgilidir: doğru grafiği seçmek, veriyi dürüstçe kodlamak, rengi ve yerleşimi gözün olması gereken yere inmesi için kullanmak ve her şeyi erişilebilir tutmak. Bölüm 5'in içinde yer alır, çünkü bir grafik bir arayüzdür ve bölümün geri kalanından her şeyi miras alır. Bölüm 5.1'in [kullanıcı deneyimi](https://en.wikipedia.org/wiki/User_experience) (UX) temelleri üzerine kurulur, bölüm 5.2'nin tasarım sistemlerinden belirteçler ve bileşenler ödünç alır, bölüm 5.3'ün erişilebilirlik görevlerini karşılamalıdır ve bölüm 5.4'teki içerik tasarımının sade, amaçlı sesiyle konuşur. Bilerek tesisat işinin dışında kalır. Analitik ve iş zekâsının (bölüm 7.3) veri hatları, ambarları ve raporlama araçları farklı bir konudur; bölüm 7.5'in daha geniş karar bilimi ve veri kültürü de öyle. Burada verinin nereden geldiğinden bağımsız olarak resmi nasıl iyi yapacağınızı öğrenirsiniz.

Büyük takımlar için bahisler eşgüdüm ve güvendir. Her squad kendi grafiklerini biçimlendirdiğinde şirket, her biri farklı eksenler, renkler ve yuvarlamalarla "zaman içinde gelir"in elli lehçesine sahip olur ve yöneticiler hepsine güvenmemeyi öğrenir. Kurumsal ortamlarda yanıltıcı bir pano gerçek bütçeyi yanlış yöne sürer. Kamuda, kamusal bir grafik vatandaşlarla iletişim eylemidir ve bölüm 10.16'daki paydaş iletişiminin bir parçasıdır: bir halk sağlığı grafiğindeki kesik bir eksen milyonları paniğe sürükleyebilir ya da yanlış biçimde rahatlatabilir ve erişilebilirlik bir tercih değil, yasal bir görevdir. İyi görselleştirme tasarımı, verinin inanılma hakkını kazanma yoludur.

## Temel ilkeler

- Okurun sorusundan başlayın, sonra onu cevaplayan grafiği seçin.
- Görsel kodlamayı veri türüne uydurun: kesin karşılaştırma için konum, kategoriler için ton.
- Veri taşıyan mürekkep payını en üst düzeye çıkarın; hiçbir şey taşımayan süsü silin.
- Gözün önce noktaya inmesi için ön-dikkatsel nitelikleri bilinçli kullanın.
- Paletleri veri rolüne göre seçin (ardışık, ıraksak, kategorik) ve renk körlüğüne karşı güvenli tutun.
- Asla yalnızca renge güvenmeyin; metin, yapı ve bir tablo yedeği sağlayın.
- Ölçek konusunda doğruyu söyleyin: kesik eksen, yanıltıcı alan ve gereksiz çift eksen olmasın.
- İçgörüyü işaretleyin; okuru onu aratmayın.

## Öneriler

### Sorudan başlayın, sonra grafiği seçin

Her iyi grafik bir veri kümesiyle değil, bir soruyla başlar. Bir grafik türüne uzanmadan önce okurun sorusunu tek bir cümleyle adlandırın, sonra onu bir görevle eşleştirin. Karşılaştırma ("hangisi daha büyük?"), uzunlukların ortak bir tabanda durduğu ve gözün onları zahmetsizce sıraladığı bir [çubuk grafik](https://en.wikipedia.org/wiki/Bar_chart) ister. Zaman içindeki eğilim ("hangi yöne gidiyor?"), bağlı bir çizgi sürekli değişim olarak okunduğu için bir [çizgi grafik](https://en.wikipedia.org/wiki/Line_chart) ister. Dağılım ("nasıl yayılıyor?"), şekli, merkezi ve aykırı değerleri gösteren bir histogram ya da kutu grafiği ister. Parça-bütün ("her parçanın payı nedir?") çoğunlukla bir pastadan çok yığılmış bir çubukla daha iyi sunulur, çünkü insanlar uzunlukları açılardan çok daha doğru karşılaştırır; [pasta grafiğini](https://en.wikipedia.org/wiki/Pie_chart) bölünmenin bütün hikâye olduğu iki ya da üç dilim için saklayın. İlişki ("bu ikisi birlikte mi hareket ediyor?"), korelasyonu ve kümeleri bir bakışta gösteren tek grafik olan bir [saçılım grafiği](https://en.wikipedia.org/wiki/Scatter_plot) ister.

Disiplin, grafiği sorunun seçmesine izin vermektir, asla tersini değil. Etkileyici göründüğü için seçilen bir grafik türü (3B patlatılmış bir pasta, bir radar grafiği, ortasında sayı olan bir halka) okurun değil tasarımcının yararına verilmiş bir karardır. Bir tablo soruyu daha hızlı cevaplayacaksa (dört satır için kesin rakamlara ihtiyaç duyan okurun hiç grafiğe ihtiyacı yoktur), tabloyu kullanın. Grafik yalnızca bir resim, ızgaradaki rakamların gizleyeceği bir örüntüyü ortaya çıkardığında haklıdır.

### Görsel kodlamayı veriye uydurun

Bir grafik, veriyi görsel özelliklere eşleyerek çalışır ve bu özellikler eşit değildir. On yıllarca algı araştırması onları sıralar. Ortak bir ölçek üzerindeki konum insanların sahip olduğu en doğru kanaldır; bu yüzden paylaşılan bir eksendeki çubuklar ve noktalar karşılaştırmada her şeyi geçer. Sonra uzunluk gelir, sonra açı ve eğim, sonra alan, sonra renk yoğunluğu ve son olarak ton; ton niceliği yargılamak için neredeyse işe yaramazdır ama kategorileri etiketlemek için mükemmeldir. En kesin kanalınızı en önemli niceliğinize harcayın.

Kanalı veri türüne de uydurun. Nicel veri (sayılar, tutarlar, süreler) konuma, uzunluğa ya da ardışık bir renk rampasına aittir. Sıralı veri (küçük, orta, büyük) sıralı boyutu ya da açıktan koyuya bir rampayı kullanabilir. Kategorik veri (bölge, ürün hattı, parti) tona ya da şekle aittir; bir kategorinin diğerinden "daha fazla" olduğunu ima eden bir boyuta asla. Klasik hata, bir kategoriyi gökkuşağı olarak kodlamaktır; böylece okurun gözü verinin sahip olmadığı bir sıra icat eder. Niceliği gözün nicelik okuduğu yerde, kimliği gözün kimlik okuduğu yerde kodlayın.

### Grafiksel mükemmelliğin peşinde olun: veri-mürekkebini en üst düzeye çıkarın

Edward Tufte görselleştirmeye en net tasarım etiğini verdi ve içselleştirmeye değer. Temel ölçüsü [veri-mürekkep oranıdır](https://en.wikipedia.org/wiki/Data-ink_ratio): sayfadaki bütün mürekkebin (ya da piksellerin) hangi kesri gerçekten veriyi kodluyor? Gerisi (ağır ızgara çizgileri, kutulu kenarlıklar, gölgeler, arka plan dolguları, gereksiz göstergeler, süs amaçlı 3B) okurun dikkatine bir vergidir. Tufte bu süse grafik çöpü (chartjunk) der ve talimat kesindir: silin. Izgara çizgilerini fısıldayana kadar açın, grafik kenarlığını bırakın, okuru göstergeye gönderme yerine veriyi doğrudan etiketleyin ve verinin neredeyse tek başına durmasına izin verin. Bir grafik, eklenecek bir şey kalmadığında değil, anlam kaybetmeden çıkarılacak bir şey kalmadığında bitmiştir.

Takımlar için özellikle anılmaya değer bir Tufte fikri vardır: küçük katlar (small multiples). Sekiz seriyi tek bir karmakarışık çizgi grafiğine sıkıştırmak yerine, her seri için bir tane olmak üzere aynı eksenler ve ölçekle bir ızgarada sekiz küçük grafik çizin. Göz ızgarayı tarar ve yadırganan olanı anında fark eder, çünkü her panel doğrudan karşılaştırılabilirdir. Küçük katlar "okunamayacak kadar çok çizgi"yi "göz gezdirebileceğiniz bir sayfaya" çevirir ve tek bir aşırı yüklü çizime daha çok renk ve daha çok gösterge girdisi yığmaktan çok daha iyi ölçeklenir.

### Ön-dikkatsel nitelikleri ve görsel hiyerarşiyi kullanın

Bazı görsel farklar, bilinçli dikkatten önce, saniyenin bir kesrinde, okurun onları "aramasına" gerek kalmadan kaydedilir. Bu ön-dikkatsel nitelikler (gri noktalar arasında tek bir kırmızı nokta, bir uzun çubuk, uzayda ayrı duran bir öğe) gözü yönlendirmek için sahip olduğunuz en güçlü araçtır. Bunları bilerek kullanın. Grafiğin amacı bir bölgenin geride kaldığıysa, o bölgeyi renklendirin ve gerisini grileştirin; okur başlığı okumadan mesajı görür. Her şey parlak ve kalınsa hiçbir şey öyle değildir, çünkü kontrast görelidir ve vurguyla dolu bir sayfa gürültüyle dolu bir sayfadır.

Bu, veriye uygulanan görsel hiyerarşidir: okurun önce fark etmesi gereken tek şeye karar verin ve en güçlü sinyalinizi oraya harcayın. Başlık ve işaretleme çıkarımı sözcüklerle söyler. Renk ve ağırlık kanıtı gösterir. Destekleyen her şey (eksenler, ızgara çizgileri, ikincil seriler) ön planın konuşabilmesi için griye çekilir. Hiyerarşisi olmayan bir grafik, okurdan neyin önemli olduğunu bulma gibi tasarımcının işini yapmasını ister.

### Rengi role göre seçin ve renk körlüğüne karşı güvenli yapın

Renk en sık kötüye kullanılan kanaldır; bu yüzden onu üç aileli bir sistem olarak ele alın. Ardışık bir palet tek bir tonda açıktan koyuya akar ve düşükten yükseğe giden niceliği kodlar (nüfus yoğunluğu, gelir). Iraksak bir palet, nötr bir orta noktada buluşan iki tona sahiptir ve bir merkezden sapmayı kodlar (sıcaklık anomalisi, sıfır etrafında kâr ve zarar, nötr etrafında anket mutabakatı). Kategorik bir palet, sırası olmayan grupları etiketlemek için ayrı tonlardan oluşan bir kümedir; yaklaşık yedi renkle sınırlı tutun, çünkü ötesinde okur onları ayırt edemez. Yanlış aileyi seçmek (bir nicelik için kategorik gökkuşağı, sırasız kategoriler için ardışık rampa) okurun algısıyla savaşır.

Sonra erişilebilir yapın, çünkü erkeklerin yaklaşık on ikide biri bir tür [renk körlüğüne](https://en.wikipedia.org/wiki/Color_blindness) sahiptir. Kırmızı ve yeşil klasik tuzaktır: kırmızı-kötü, yeşil-iyi bir grafik en yaygın eksikliğe karşı görünmezdir. Renk körlüğüne güvenli paletler seçin (maviden turuncuya ıraksak şemalar ve ColorBrewer gibi araçlardan iyi sınanmış kategorik kümeler güvenli başlangıç noktalarıdır) ve yayına almadan önce yaygın eksiklikleri simüle ederek doğrulayın. Kontrastı da denetleyin; böylece metin ve işaretler bölüm 5.3'teki erişilebilirlik standartlarının gerektirdiği oranları karşılar. Renk, onsuz da ayakta kalan bir mesajı pekiştirmelidir.

### Yalnızca renge güvenmeyin; alternatifler sağlayın

Veri görselleştirmede erişilebilirlik palet seçiminin ötesine geçer. [Web İçeriği Erişilebilirlik Yönergeleri'nin](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) temel kuralı, bilginin iletilmesinin tek yolunun asla renk olmaması gerektiğidir. Bu yüzden rengi ikinci bir ipucuyla eşleştirin: doğrudan etiketler, saçılımda ayrı şekiller ya da işaretçiler, çizgi grafiğinde farklı çizgi stilleri (düz, kesikli) ya da önemli çubukta bir metin etiketi. Tonlarınızı ayırt edemeyen bir okur, yedekli kodlamadan hâlâ mesajın tamamını almalıdır.

Gerçek bir metin alternatifi ve bir yedek sağlayın. Bir grafik görüntüsü, "satış grafiği" değil, çıkarımı belirten bir alternatif metne ve eğilimi adlandıran daha uzun bir açıklamaya ya da altyazıya ihtiyaç duyar. Mümkün olan her yerde, altta yatan veriyi erişilebilir bir tablo olarak sunun; böylece hem ekran okuyucu kullanıcısı hem de elektronik tablo meraklısı bir analist sayılara doğrudan ulaşır. Bu, bölüm 5.2'nin "bir bileşende bir kez çöz" disiplinini yansıtır: uygun rollerle, etkileşimli öğeler için klavye odağıyla ve yerleşik bir tablo görünümüyle erişilebilir grafik bileşenleri inşa edin; böylece her takım bunu pano başına yeniden icat etmek yerine miras alır.

### Keşfettiğinizi, açıkladığınızı ya da izlediğinizi bilin

Grafikler üç farklı işe hizmet eder ve onları karıştırmak kötü iş üretir. Keşif amaçlı görselleştirme sizin, yani verinin içinde neyin ilginç olduğunu arayan analistin içindir; hızlı, yoğun ve çirkin olabilir, çünkü izleyici yineleyecek tek bir uzmandır. Açıklayıcı görselleştirme bir izleyici içindir, zaten anladığınız belirli bir bulguyu iletir; bilinçlidir, işaretlenmiştir ve tek bir mesaja indirgenmiştir ve bölüm 10.16'nın hikâye anlatımına aittir. Bir pano üçüncü bir şeydir: bilinen metrikleri zaman içinde izlemek için kalıcı, bir bakışta okunur bir ekran; tek seferlik bir argümandan çok "şu anda bir şey yanlış mı?" için eniyilenmiştir.

Tasarımı işe uydurun. Bir başlığı ve tek bir vurgulu serisi olan açıklayıcı bir grafik, okurun bir bakışta birçok metriğe ve gözünün yerleşimi öğrenmesi için tutarlı yerleşime ihtiyaç duyduğu bir izleme panosu için yanlıştır. Anlatı işaretlemesiyle tıkıştırılmış bir pano her sabah kontrol etmek için yorucudur. Ve ham çizimlerle dolu bir keşif not defteri, bir açıklamaymış gibi bir yöneticiye asla verilmemelidir. Önce işe karar verin; tasarım onu izler.

### Asla yanıltmayın: dürüst ölçekler, dürüst alanlar

Güveni yok etmenin en hızlı yolu, doğru görünürken yalan söyleyen bir grafiktir. En yaygın yalan, kesik eksendir: bir çubuk grafiğinin y eksenini 0 yerine 90'dan başlatmak, çubuk uzunluğu artık değerle eşleşmediği için yüzde 2'lik bir farkı bir uçuruma çevirir. Çubuklar her zaman sıfırdan başlamalıdır; büyüklüğü değil değişimi kodlayan çizgi grafikleri, net etiketlerseniz sıfır olmayan bir taban kullanabilir. İkinci tuzak çift eksendir: tek bir grafikte iki y ölçeği, ölçekleri kaydırarak istediğiniz her korelasyonu üretmenize izin verir ve okurlar nadiren fark eder. Bunun yerine iki hizalı grafiği ya da endekslenmiş bir görünümü tercih edin. Üçüncüsü yanıltıcı alandır: bir değeri temsil etmek için bir simgeyi ya da baloncuğu hem genişlik hem yükseklikle ölçeklediğinizde, alan karesi kadar büyür ve farkı çılgınca abartır; kenar uzunluğuna değil alana göre ölçekleyin.

Bunları üslup tercihleri değil, bütünlük kuralları sayın. Bir grafik, okurdan güvenmesini istediğiniz bir iddiadır ve bu çarpıtmaların her biri, küçük bir şeyi büyük ya da ilgisiz bir şeyi bağlantılı göstermek için algının nasıl çalıştığını sömürür. Aşağıdaki kamu ve kurumsal örnekler, izleyici kamu ya da yönetim kurulu olduğunda bu ihanetin ne kadar pahalıya mal olduğunu gösterir.

### İçgörüyü işaretleyin ve etkileşimi ölçülü ekleyin

Okura noktayı buldurtan bir grafik yarım kalmıştır. İşaretleyin: konuyu ("Zaman içinde kayıtlar") değil bulguyu ("Kayıtlar Mart lansmanından sonra ikiye katlandı") söyleyen bir başlık, anahtar olay için bir belirtme çizgisi, hedef ya da ortalama için bir referans çizgisi. İşaretleme, bölüm 5.4'teki tasarımın resimle buluştuğu yerdir; sözcükler argümanı taşır ve işaretler kanıtı sağlar.

Etkileşim yeri ancak gerçek bir takip sorusunu cevapladığında hak eder. Kesin değerler için araç ipuçları, bir kesime filtreleme ve ayrıntıya inme, okurun statik grafiğin tutamayacağı bir sonraki sorusu olduğunda yardımcı olur. Ama etkileşim bir maliyettir: bilgiyi bir fare üstüne gelmenin arkasına gizler, dokunmatik ekranda ve klavye kullanıcıları için başarısız olur ve performansı sürünmeye çevirebilir. Web'de bölüm 5.6'daki çizim bütçesini izleyin: on binlerce nokta, on binlerce tekil belge öğesi değil, canvas ya da toplulaştırılmış bir görünüm ister. Varsayılan, statik görünümün çekirdek hikâyenin tamamını anlatmasını sağlayın ve etkileşimin altındaki derinliği ortaya çıkarmasına izin verin.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| Görselleştirmeyi kendi ürününüzde inşa etmek | Tasarım, erişilebilirlik ve etkileşim üzerinde tam kontrol | Mühendislik zamanına mal olur; performans ve bakım sizin |
| Bir BI aracının grafiklerini kullanmak | Hızlı, ucuz, ambara bağlı | Genel görünüm; sınırlı erişilebilirlik ve işaretleme kontrolü |
| Etkileşimli grafikler | Takip sorularını cevaplar; yerinde keşif | Daha yavaş, erişilebilir yapması daha zor, baskıda ve dokunmatikte başarısız |
| Statik grafikler | Hızlı, erişilebilir, baskıya hazır, belirsizliksiz | Okurun bir sonraki sorusunu cevaplayamaz |
| Pano | Birçok bilinen metriğin bir bakışta izlenmesi | Tek seferlik bir argüman için zayıf; metrik yayılmasını özendirir |
| Açıklayıcı grafik | Tek bir mesajı güçle iletir | İzleme ya da açık uçlu keşif için yanlış |
| Zengin renk ve efektler | Göz alıcı; cilalı hissettirir | Grafik çöpü; veri-mürekkep oranına ve erişilebilirliğe zarar verir |

Yinelenen gerilim, anlatım gücü ile dürüstlük ve netlik arasındadır. Bir grafiği zenginleştiren her özellik (ikinci bir eksen, bir renk geçişi, bir 3B perspektif, bir animasyon) aynı zamanda yanıltmanın ya da noktayı gömmenin bir yolunu ekler. Bunu varsayılan olarak azı seçerek çözün: soruyu cevaplayan en basit grafik, en az renkle, doğruyu söyleyen ölçekle. Anlatım gücünü yalnızca belirli bir okur sorusu gerektirdiğinde ekleyin ve erişilebilirlik ve performans maliyetini bilerek ödeyin. Diğer kalıcı ödünleşim inşa etmek ya da satın almaktır. Bir BI aracı bir grafiği dakikalar içinde ekrana getirir ve iç izleme için doğru seçimdir; müşteriye dönük bir ürüne gömülü bir görselleştirme genellikle yalnızca amaca özel bir bileşenin verdiği tasarım, erişilebilirlik ve performans kontrolüne ihtiyaç duyar.

## Takımınızla tartışılacak sorular

1. **Grafiklerimiz tek bir görsel dili mi paylaşıyor, yoksa her takım kendi dilini mi icat ediyor?** Her squad kendi renklerini, eksen kurallarını, yuvarlamasını ve grafik türlerini seçtiğinde kurum, güveni sessizce aşındıran lehçeler biriktirir: farklı ölçekler ve farklı yeşillerle "aktif kullanıcıları" gösteren iki pano, yöneticilere verinin güvenilemeyeceğini öğretir. Aynı metriğin üç takımdan üç grafiğini getirin ve yan yana koyun. Bulacağınız boşluklar (burada kesik bir eksen, orada bir kategori gökkuşağı, birinde binlerle diğerinde milyonlarla gelir), bölüm 5.2'deki tasarım sistemi gibi yönetilen, üzerinde uzlaşılmış paletlere, varsayılan eksen kurallarına ve yerleşik erişilebilirliğe sahip paylaşılan bir grafik bileşen kütüphanesinin gerekçesidir. Amaç, şirketteki herhangi bir grafiğin görür görmez doğru okunmasıdır, çünkü dilbilgisi paylaşılmıştır.

2. **En önemli grafiklerimiz renk körü bir okuru ve bir ekran okuyucuyu atlatır mı?** Veri görselleştirmede erişilebilirliği atlamak kolaydır, çünkü grafikler onları yapanlara hâlâ iyi görünür ve tuzak tam olarak budur. Liderliğinizin en sık gördüğü üç grafiği alın ve bir renk körlüğü simülatöründen geçirin, sonra ekran kapalıyken yalnızca alternatif metni ve varsa tablo yedeğini kullanarak anlamaya çalışın. Kırmızı-yeşil bir durum grafiği düzleşiyorsa, alternatif metin "grafik"ten başka bir şey söylemiyorsa ya da altta yatan sayılara fare olmadan ulaşmanın yolu yoksa, şu anda dışarıda bıraktığınız bir okur grubu bulmuşsunuz demektir; kamu çalışmasında bu, bölüm 5.3'teki standartlar uyarınca yasal bir riskir. Düzeltmenin kimin sorumluluğunda olduğuna ve düzeltmenin bir kez çözülmesi için paylaşılan bir bileşende yer alıp almayacağına karar verin.

3. **Bir kararı süren her grafik için, cevapladığı soruyu gösterebilir ve yanıltmadığını doğrulayabilir miyiz?** Birçok grafik, canlı bir soruyu cevapladığı için değil, birisi bir zamanlar yaptığı için vardır ve en çok izlenenlerin bazıları kimse fark etmeden ölçeği çarpıtır. Ana panolarınızdaki grafikleri tek tek gözden geçirin ve her biri için bilgilendirdiği kararı adlandırın ve bütünlüğünü denetleyin: sıfırdan çubuklar, gereksiz çift eksen yok, dürüstçe ölçeklenmiş alanlar, bir konuyu değil bir bulguyu söyleyen bir başlık. Hiçbir güncel soruyu cevaplamayan grafikler silinmeye aday, yanıltanlar acil onarıma adaydır; çünkü bir farkı sessizce abartan bir grafik hiç grafik olmamasından kötüdür. Bu doğrudan bölüm 7.5'in karar kültürüne bağlanır: grafiklerine güvenen bir takım daha hızlı, daha sağlam temelli çağrılar yapar.

4. **Bir takım grafiğe ihtiyaç duyduğunda önce BI aracının yerleşik grafiklerine mi yoksa yönetilen bir bileşen kütüphanesine mi uzanıyoruz ve hangisine kimin karar verdiği?** BI aracına doğru çekim gerçektir: hızlı, ucuz ve zaten ambara bağlıdır; bu yüzden izleme panolarının çoğu oraya aittir. Ama genel varsayılanları lehçelerin ve grafik çöpünün sızdığı yerdir ve erişilebilirlik ile işaretleme kontrolleri genellikle zayıftır; bu, itibarınızı taşıyan müşteriye dönük ve kamusal grafikler için en çok önem taşır. Büyük bir kurum için tehlike, varsayılanın hiç karara bağlanmamasıdır; böylece her takım en kolay olana kayar ve varlık parçalanır. Bugün grafiklerin gerçekte nerede inşa edildiğinin bir envanterini, BI aracına karşı amaca özel bir bileşenden birkaç yan yana örneği ve her birindeki erişilebilirlik boşluklarını getirin. Kurumsal ve kamu ortamlarında satın alma gerçeğini ekleyin: çoğu zaman yıllarca tek bir BI platformuna kilitlenirsiniz; bu yüzden sözleşmeden sonra değil önce, hangi grafikleri dürüst ve erişilebilir biçimde çizebildiğini ve hangilerinin yönetilen bir bileşen gerektirdiğini tam olarak bilin.

5. **Bir grafiği dış ya da yönetici kitlesine kimin yayımlamasına izin var ve önce hangi gözden geçirmeden geçiyor?** Kendi kendine hizmet analitiği gerçek bir iyiliktir, ama yanıltıcı bir grafiğin ikinci bir çift göz olmadan yönetim kuruluna ya da kamuya ulaşabileceği anlamına gelir; kamusal bir grafikteki kesik bir eksen ya da etiketsiz bir sıçramayı geri almak, önlemekten çok daha zordur. Gerilim hız ve özerklik ile bütünlük ve güven arasındadır: çok sıkı kapı koyarsanız insanlar sizi dolanır, çok az koyarsanız bir piyasayı ya da bir seçmen kitlesini paniğe sürükleyen grafiği yayına verirsiniz. En görünür grafikleriniz için mevcut yayımlama yolunu, incelemesiz dış kitleye ulaşan örnekleri ve yöntem ile belirsizliğin grafiğin üzerinde işaretlenip işaretlenmediğine dair kanıtı getirin. Kamu sektöründe ve düzenlenmiş işlerde bu keskindir: resmî bir istatistik vatandaşlarla iletişimdir ve bölüm 10.16'daki paydaş güveninin bir parçasıdır; bu yüzden kimin onayladığını, hangi bütünlük ve erişilebilirlik kontrol listesini uyguladığını ve bir grafik yanılttığında hesap verebilirliğin nerede durduğunu adlandırın.

6. **Etkileşimi nerelere ekledik ve varsayılan statik görünüm fare olmadan hâlâ hikâyenin tamamını anlatıyor mu?** Etkileşim baştan çıkarıcı ve pahalıdır: değerleri bir fare üstüne gelmenin arkasına gizler, dokunmatikte ve klavye kullanıcıları için bozulur ve bölüm 5.6'nın uyardığı gibi büyük veri kümelerinde çizim bütçesini sürünmeye çevirebilir. Rakip düşünce, gerçek bir takip sorusunun (kesin bir değer, bir ayrıntıya inme, filtrelenmiş bir kesim) bazen maliyete değmesidir; bu yüzden amaç yasak değil ölçülülüktür. Yayına aldığınız etkileşimli grafiklerin listesini, her birini fare olmadan ve telefonda denemenin sonuçlarını ve veri on binlerce noktaya büyüdüğünde performans sayılarını getirin. Kurumsal ve kamu kitleleri için erişilebilirlik boyutu, bölüm 5.3'teki standartlar uyarınca yasal bir görevdir ve grafikler kiosklarda, çıktılarda ve yardımcı teknolojide okunur; bu yüzden statik, işaretlenmiş varsayılan çekirdek mesajı taşımalı ve etkileşim yalnızca altına derinlik ekleyebilmelidir.

## Sektör merceği

**Girişim.** Hız kazanır; bu yüzden kadrolayamayacağınız bir görselleştirme bileşen varlığı inşa etmek yerine BI aracınızın içindeki grafiklere ya da hafif bir grafik kütüphanesine yaslanın. Sonradan karşılığını veren tek ucuz karar, ilk günden tek bir renk körlüğüne güvenli palet ve sıfırdan başlayan çubuk alışkanlığı seçmektir; böylece on müşteriniz olmadan aynı metriğin bir düzine lehçesini biriktirmezsiniz. Erişilebilir yapmaya vaktiniz olmayacak etkileşimli bir grafik yerine bulgusunu söyleyen statik, işaretlenmiş bir grafiği tercih edin.

**Küçük işletme.** Veri uzmanınız ve dar bir bütçeniz yoksa, görselleştirmeyi zaten ödediğiniz araçlardan alacağınız bir şey olarak ele alın: elektronik tablo, analitik SaaS, CRM'nizdeki pano. Önemli olan bir avuç bütünlük kuralını öğrenin (çubuklar sıfırdan başlar, bir nicelik için gökkuşağı yok, dokuz dilimli pasta yok) ve özel bir palet yaptırmak yerine hazır, renk körlüğüne güvenli bir palet uygulayın. Grafiği satın alın, inşa etmeyin ve dikkatinizi onu doğru okumaya saklayın.

**Kurumsal.** Sorun birçok takım boyunca tutarlılıktır; bu yüzden görselleştirmeyi bir tasarım sistemi gibi yönetin: üzerinde uzlaşılmış ardışık, ıraksak ve kategorik paletlere, dürüst eksen varsayılanlarına, standart sayı biçimlendirmesine ve yerleşik erişilebilirliğe sahip paylaşılan bir grafik bileşen kütüphanesi. Bunu bölüm 8.1'in teslimat hattında görsel gerileme ve bütünlük kontrolleriyle zorunlu kılın; böylece bir ekseni kesen ya da kontrastta başarısız olan bir grafik yayına çıkmadan engellenir. Getirisi, herhangi bir takımın grafiğinin görür görmez doğru okunması ve liderliğin bir sayının hangi sürümüne inanacağını sormayı bırakmasıdır.

**Kamu.** Her kamusal grafik bir iletişim eylemidir ve kamusal hesap verebilirliğe tabidir; bu yüzden dürüst ölçekler ve WCAG erişilebilirliği tercih değil, görevdir. Sıfırdan çubukları, alana göre kodlanan alanı, renk körlüğüne güvenli paletleri, bulguyu söyleyen sade dilli başlıkları ve her grafiğin yanında indirilebilir erişilebilir bir tabloyu zorunlu kılın. Tartışmalı bir rakamın yanıltıcı bir manşete indirgenememesi için yöntemi ve belirsizliği grafiğin üzerinde işaretleyin ve satın aldığınız herhangi bir BI aracının bu standartları karşılayabildiğinden emin olun, çünkü yükümlülük satıcıdan bağımsız olarak sizindir.

## Örnekler

**Girişim.** On kişilik bir analitik girişimi, müşteriye dönük bir kullanım panosu yayına alır. İlk sürüm bir BI aracının varsayılan temasını kullanır: kategori renklerinin gökkuşağı, her yerde ızgara çizgileri ve kimsenin okuyamadığı dokuz dilimli bir pasta. Kullanıcılar sayıların güvenilmez hissettirdiğinden şikâyet eder. Takım onu küçük bir renk körlüğüne güvenli paletle gömülü bileşenler olarak yeniden inşa eder, pastayı sıralanmış bir çubuk grafikle değiştirir, ızgara çizgilerini açar ve gösterge ortadan kalksın diye doğrudan etiketler ekler. Bulguyu söyleyen başlıklar koyar ve her grafiğe alternatif metin ve bir tablo anahtarı ekler. Panoyla etkileşim artar, çünkü müşteriler sonunda onu bir bakışta okuyabilir ve daha temiz tasarım tanıtımlarda bir satış noktası olur.

**Kurumsal.** Çok uluslu bir bankanın düzinelerce takım tarafından inşa edilmiş yüzlerce iç panosu vardır; her birinin kendi renkleri ve eksen alışkanlıkları vardır ve yöneticiler onlara rutin olarak güvenmez, çünkü aynı metrik her sunumda farklı görünür. Şirket BI platformunun üzerine yönetilen bir grafik kütüphanesi getirir: üzerinde uzlaşılmış ardışık, ıraksak ve kategorik paletler; çubuk eksenlerinin sıfırdan başlaması gerektiğine dair katı bir kural; standart sayı biçimlendirmesi ve her bileşene gömülü erişilebilirlik. Bölüm 8.1'in teslimat hattındaki bir görsel gerileme kontrolü, standartları ihlal eden grafikleri engeller. Bir yıl içinde herhangi bir takımın grafiği görür görmez doğru okunur ve liderlik "bu sayının hangi sürümüne inanmalıyım?" diye sormayı bırakır.

**Kamu.** Ulusal bir istatistik kurumu ekonomi, sağlık ve nüfus üzerine kamusal veri yayımlar ve grafikleri, altta yatan rakamları doğrulayamayan gazeteciler, politika yapıcılar ve vatandaşlar tarafından okunur. Kurum her grafiği kamuyla iletişim ve bölüm 10.16'daki paydaş güveninin bir parçası olarak ele alır. Dürüst ölçekleri (sıfırdan çubuklar, yanıltıcı çift eksen yok, alana göre kodlanan alan), bölgesel karşılaştırmalar için renk körlüğüne güvenli ıraksak paletleri, bulguyu söyleyen sade dilli başlıkları ve WCAG'yi karşılamak için her grafiğin yanında indirilebilir erişilebilir bir tabloyu zorunlu kılar. Tartışmalı bir rakam yayımlandığında işaretleme yöntemi ve belirsizliği grafiğin üzerinde açıklar; böylece kesik bir eksen ya da etiketsiz bir sıçrama, kamu güvenini aşındıran yanıltıcı bir manşete asla dönüşemez.

## İş gerekçesi: motivasyonlar, YG ve TSM

İyi görselleştirme tasarımının getirisi daha hızlı, daha iyi kararlar ve daha az pahalı hatadır. Bir sorunu bir bakışta ortaya çıkaran bir pano sinyalden eyleme giden süreyi kısaltır ve doğruyu söyleyen bir grafik, kesik bir eksenin ürettiği bir yanılsamanın peşinden bütçenin koşmasını önler. Bu kazançları bir faturaya koymak zordur ama gerçektir: hangi grafiğe inanılacağını tartışarak geçen her liderlik toplantısı, yanlış okunmuş bir eğilim üzerine kurulan her strateji ve ürününüzün analitiği okunamaz olduğu için ayrılan her müşteri, net tasarımın ortadan kaldırdığı bir maliyettir. Grafiklerin gerçek parayı sürdüğü yerlerde, banka örneğinde olduğu gibi, güvenilen sayıların değeri onları iyi inşa etmenin maliyetini fersah fersah aşar.

Benimseme maliyeti çoğunlukla tek seferlik ve paylaşılandır. Üzerinde uzlaşılmış paletleri, eksen ve biçimlendirme kurallarını ve erişilebilirlik varsayılanlarını tanımlar, sonra bunları bir grafik bileşen kütüphanesine kodlarsınız; böylece takımlar pano başına yeniden karar vermek yerine onları miras alır. Süregiden sahip olma maliyeti gerçektir ama mütevazıdır: kütüphaneyi bakımda tutmak, standartlar evrildikçe erişilebilir tutmak ve tek seferlik özel grafiklerin yayılmasına direnmek. İhmalin maliyeti sessizce birikir: tutarsız, yanıltıcı, erişilebilir olmayan grafikler tüm verinize olan güveni aşındırır, düzenlenmiş ve kamu ortamlarında yasal risk doğurur ve insanları ham elektronik tablolara geri iter; bu da bölüm 7.3'ün analitik yığınına yapılan yatırımın tamamını boşa harcar. Liderliğe gerekçeyi sunmak için görselleştirme kalitesini zaten izledikleri sonuçlara bağlayın: karar hızı, raporlamaya güven ve kamu sektöründe erişilebilirlik uyumu.

## Anti-kalıplar ve tuzaklar

- **Kesik çubuk ekseni:** çubukları sıfırın üstünden başlatıp küçük bir farkı uçurum gibi göstermek; en yaygın tek grafik yalanı.
- **Gereksiz çift eksen:** tek bir grafikte iki y ölçeği; yazarın göstermek istediği her korelasyonu üretmek için kayar.
- **Yanıltıcı alan:** bir simgeyi ya da baloncuğu kenar uzunluğuyla ölçeklemek; böylece alanı ve algılanan değer karesi kadar büyür.
- **Nicelik için gökkuşağı:** sıralı bir niceliği sırasız kategorik tonlarla kodlamak; göz büyüklüğü okuyamaz.
- **Çok dilimli pasta:** üçten fazla dilim; okurları yargılayamayacakları açıları karşılaştırmaya zorlar; sıralanmış bir çubuk kullanın.
- **Grafik çöpü:** veri-mürekkep oranını düşüren ve sinyali gömen ağır ızgara çizgileri, kenarlıklar, 3B ve gölgeler.
- **Tek ipucu olarak renk:** etiketsiz ve şekilsiz kırmızı-yeşil durum; renk körü okurlara ve ekran okuyuculara görünmez.
- **Gösterge avı:** doğrudan çizgi ya da çubuk üzerindeki bir etiketin yeteceği yerde uzak bir göstergeye gönderme.
- **Her şeye vurgu:** her seri kalın ve parlak; böylece kontrast çöker ve hiçbir şey öne çıkmaz.
- **Tablonun kazandığı yerde grafik:** okurun kesin okuması gereken dört sayı için bir resim.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Grafikler elde hangi araç varsa onunla gelişigüzel yapılır. Renkler, eksenler ve biçimler yazara göre değişir, kesik eksenler ve gökkuşağı kategoriler yaygındır, erişilebilirlik düşünülmemiştir ve okurlar sonuçlara güvenmez.
- **Düzey 2, Geliştirme:** Bazı takımlar temel uygulamaları benimser, ama kurum genelinde tutarsızdır. Çubuklar yer yer sıfırdan başlar, bariz grafik çöpü incelemede cesaretlendirilmez ve birkaç takımda bir kurum paleti vardır; yine de koridorun ilerisindeki bir başka takım hâlâ dokuz dilimli bir pasta ve kırmızı-yeşil bir durum grafiği yayına alır.
- **Düzey 3, Standartlaştırma:** Paylaşılan bir grafik bileşen kütüphanesi, üzerinde uzlaşılmış ardışık, ıraksak ve kategorik paletleri, dürüst eksen kurallarını, standart biçimlendirmeyi ve erişilebilirliği (renk körlüğüne güvenli, alternatif metin, tablo yedeği) kodlar. Standartlar belgelenmiş ve kurum genelinde zorunlu tutulur; açıklayıcı, keşif amaçlı ve pano kullanımları tasarımla ayrıştırılır.
- **Düzey 4, Yönetme:** Görselleştirme kalitesi temel çizgilere karşı ölçülür ve kontrol edilir. Erişilebilirlik ve grafik bütünlüğü kontrolleri teslimat hattında çalışır ve geçme oranlarını raporlar; sıfırdan çubukları, kontrast uyumlu rengi ve tablo yedeğini olan grafiklerin payı bir metrik olarak izlenir; kavrayış gerçek okurlarla bir temel çizgiye karşı sınanır ve her anahtar metriğin ayrışan lehçelerinin sayısı, bire doğru eğilirken izlenir. Standartları ihlal eden grafikler yayından önce yakalanır ve kütüphanenin nerede çalışmaya ihtiyaç duyduğunu görüş değil sayılar sürer.
- **Düzey 5, Orkestrasyon:** Görselleştirme sürekli iyileştirilir ve kurum genelinde bütünleşiktir. Standartlar erişilebilirlik gereksinimleri ve okur ihtiyaçları değiştikçe uyum sağlar, paletler, bileşenler ve kurallar ölçülmüş kanıttan rafine edilir, işaretleme ve anlatı norm olur ve pratik analitik ve karar kültürüne dokunmuştur; böylece herhangi bir takımın grafiği görür görmez doğru okunur ve kurum öğrendikçe görsel dil evrilir.

## Tartışma fikirleri

1. Ana panonuzdaki hangi grafik, ekseni sıfırdan başlasaydı farklı görünürdü ve bu hikâyeyi değiştirir mi?
2. En önemli grafiğinizi seçin: mesajı gri tonlamada ayakta kalıyor mu, kalmıyorsa hangi yedekli ipucu düzeltirdi?
3. Statik, işaretlenmiş bir grafiğin hikâyenin tamamını daha hızlı anlatacağı yerde etkileşimli bir grafiği nerede kullanıyorsunuz?
4. Grafik başlıklarınız bulguları mı yoksa konuları mı söylüyor ve bir manşet sayısı sessizce tersine dönse kim fark ederdi?
5. Hangi grafikleriniz hiçbir güncel kararı cevaplamıyor ve kimse eksikliğini hissetmeden silmek için ne gerekir?
6. Bir takım görselleştirmeyi ne zaman üründe inşa etmeli, ne zaman BI aracını kullanmalı ve seçmek için yazılı bir kuralınız var mı?

## Önemli çıkarımlar

- Okurun sorusundan başlayın, sonra grafiği seçin: karşılaştırma için çubuklar, eğilim için çizgiler, ilişki için saçılım, dağılım için histogram, parça-bütün için pastalar yerine sıralanmış çubuklar.
- Kodlamayı veriye uydurun: konumu ve uzunluğu en önemli niceliğinize harcayın ve tonu kategoriler için kullanın, büyüklük için asla.
- Grafiksel mükemmelliğin peşinde olun: veri-mürekkep oranını en üst düzeye çıkarın, grafik çöpünü silin, küçük katları kullanın ve gözü ön-dikkatsel kontrast ve net hiyerarşiyle yönlendirin.
- Rengi bir sistem olarak ele alın (ardışık, ıraksak, kategorik), renk körlüğüne güvenli tutun ve asla yalnızca renge güvenmeyin; etiketler, alternatif metin ve bir tablo yedeği sağlayın.
- Ölçek konusunda doğruyu söyleyin (sıfırdan çubuklar, dürüst alanlar, gereksiz çift eksen yok), içgörüyü işaretleyin ve etkileşimi yalnızca gerçek bir takip sorusu gerektirdiğinde ekleyin.

## Kaynaklar ve ileri okuma

- Edward R. Tufte, *The Visual Display of Quantitative Information*
- Edward R. Tufte, *Envisioning Information*
- Stephen Few, *Show Me the Numbers: Designing Tables and Graphs to Enlighten*
- Stephen Few, *Information Dashboard Design: Displaying Data for At-a-Glance Monitoring*
- Cole Nussbaumer Knaflic, *Storytelling with Data: A Data Visualisation Guide for Business Professionals*
- Alberto Cairo, *The Truthful Art: Data, Charts, and Maps for Communication*
- Alberto Cairo, *How Charts Lie: Getting Smarter about Visual Information*
- William S. Cleveland, *The Elements of Graphing Data*
- Jacques Bertin, *Semiology of Graphics: Diagrams, Networks, Maps*
- Tamara Munzner, *Visualisation Analysis and Design*
- Cynthia A. Brewer, ColorBrewer: Colour Advice for Cartography (colorbrewer2.org)
- World Wide Web Consortium (W3C), *Web Content Accessibility Guidelines (WCAG) 2.2*
