# 6.2 Makine öğrenimi mühendisliği (MLOps)

## Genel bakış ve motivasyon

Genellikle [MLOps](https://en.wikipedia.org/wiki/MLOps) denen makine öğrenimi mühendisliği, [makine öğrenimini](https://en.wikipedia.org/wiki/Machine_learning) not defterlerinden ve deneylerden çıkarıp güvenilir, gözlemlenebilir, bakımı yapılabilir üretim sistemlerine taşıma disiplinidir. Geleneksel yazılım, kodunun söylediği gibi davranır. Bir ML sistemi ise kodunun, verisinin ve öğrenilmiş model parametrelerinin birlikte söylediği gibi davranır. Bu, ML sistemlerini test etmeyi ve yeniden üretmeyi zorlaştırır ve dünya eğitildikleri verilerden uzaklaştıkça sessizce başarısız olmaya yatkın kılar. MLOps, yazılım mühendisliğinin titizliğini (sürüm denetimi, test, sürekli teslimat ve izleme) kod artı veri artı model şeklindeki bu üç parçalı gerçekliğe getirir.

Büyük takımlar için MLOps, bir gösterimde göz kamaştıran tek seferlik bir modeli, birçok takımın güvenle inşa edip dağıtabileceği ve işletebileceği bir model filosundan ayıran şeydir. Ortak platformlar ve uygulamalar olmadan her takım veri hatlarını, eğitim döngülerini ve dağıtımı yeniden icat eder ve altı ay sonra kimsenin yeniden üretemediği kırılgan sistemlerle kalırsınız. Kurumsal firmalar düzinelerce modelde ölçeklenmek, hizmet düzeyi hedeflerini karşılamak ve belirli bir tahminin nasıl üretildiğini soran denetçileri tatmin etmek için MLOps'a güvenir.

Kamuda ve düzenlemeye tabi sektörlerde MLOps çoğu zaman kılık değiştirmiş bir uyum gereksinimidir. Tekrarlanabilirlik, köken ve sürümleme, bir kurumun hukuken önemli bir soruyu yanıtlamasını sağlayan şeylerdir: bir vatandaşı etkileyen kararı tam olarak hangi model, hangi veri üzerinde eğitilmiş, hangi kodla üretti? Olgun bir MLOps uygulaması bu sorunun yıllar sonra bile yanıtlanabilir kalmasını sağlar; bu hem iyi mühendislik hem de bir hukuki güvencedir.

*Ayrıca bakınız:* bölüm 8.1 (CI/CD ve teslimat), bölüm 9.2 (gözlemlenebilirlik ve izleme) ve bölüm 6.6 (yapay zeka altyapısı ve işletimi).

## Temel ilkeler

- Veriyi, kodu ve modelleri birlikte sürümlenen yapıtlar olarak ele alın; herhangi birini değiştirmek sistem davranışını değiştirir.
- Veriden eğitilmiş modele ve dağıtıma uzanan yolu otomatikleştirin; böylece tekrarlanabilir ve denetlenebilir olur.
- Her modeli, onu üreten tam veriye, koda ve yapılandırmaya izlenebilir kılın.
- Modelleri dağıtımdan önce temsil gücü yüksek, ayrılmış veriler üzerinde değerlendirin ve sonrasında da değerlendirmeye devam edin.
- Modellerin bozulacağını varsayın; ilk günden kayma (canlı verinin ya da girdi-çıktı ilişkilerinin modelin eğitildiği şeyden yavaş yavaş sapması), veri kalitesi sorunları ve performans aşınması için izleyin.
- Zekice ama tekrarlanamayan deneyler yerine sıkıcı, tekrarlanabilir hatları tercih edin.
- Deney hızı ile üretim güvenilirliği kaygılarını ayırın ve aralarında bilinçli bir köprü kurun.

## Öneriler

### Tüm ML yaşam döngüsünü açıkça yönetin

Her aşamayı tanımlayın ve ölçümleyin: veri alımı ve doğrulama, [özellik mühendisliği](https://en.wikipedia.org/wiki/Feature_engineering), eğitim, değerlendirme, dağıtım ve izleme. Aşamalar arasındaki sınırları açık hale getirin; böylece her biri test edilebilir, yeniden denenebilir ve denetlenebilir olur. Bir modelin geçici bir not defterinde eğitilip operasyona fırlatıldığı yaygın başarısızlıktan kaçının. Bunun yerine yaşam döngüsünü, yetkili herhangi bir mühendisin temiz bir çıkıştan çalıştırabileceği orkestre edilmiş bir hatla sarın.

### Özellik depoları, deney izleme ve model kayıt defterleri kullanın

Bir **özellik deposu**, özellik tanımlarını merkezileştirir; böylece aynı dönüşümler hem eğitimde hem sunumda çalışır. Bu, eğitim-sunum sapmasını (özelliklerin eğitim için ve canlı tahminler için hesaplanma biçimleri arasındaki tutarsızlıklar) ortadan kaldırır ve takımların özellikleri yeniden hesaplamak yerine yeniden kullanmasını sağlar. **Deney izleme**, her eğitim çalıştırmasının parametrelerini, kod sürümünü, veri sürümünü ve ölçütlerini kaydeder; böylece sonuçlar karşılaştırılabilir ve tekrarlanabilir olur. Bir **model kayıt defteri**, eğitilmiş modellerin kayıt sistemidir; sürümleri, kökeni, değerlendirme sonuçlarını, onay durumunu ve dağıtım aşamasını tutar. Birlikte bunlar, davranış değiştiğinde "ne değişti?" sorusunu yanıtlamanıza ve modelleri yönetilen aşamalardan geçirerek terfi ettirmenize ya da geri almanıza imkan verir.

### Veri ve modelleri tekrarlanabilir ve kökenle birlikte sürümlü hale getirin

Yalnızca kodunuzu değil, veri kümelerinizi de sürümleyin. Bir eğitim çalıştırması değişmez bir anlık görüntüye başvursun diye içerik adreslenebilir depolama ya da veri sürümleme araçları kullanın. Kodu git işlemeleriyle, ortamları kilitli bağımlılıklar ve kapsayıcı imgeleriyle sabitleyin. Kökeni uçtan uca yakalayın: hangi ham veri hangi özellikleri besledi, hangi özellikler ve kod hangi modeli üretti ve o model nerede dağıtılmış durumda. Bir olay ya da denetim geldiğinde köken, adli bir kabusu basit bir sorguya dönüştürür. Sonuçlar buna bağlı olduğunda rastgeleliği (tohumları) ve donanımı kaydedin.

### Dağıtım kalıplarını iş yüküne göre seçin

- **Toplu** puanlama, büyük veri kümeleri üzerinde bir zamanlamaya göre çalışır; işletmesi en basittir, gecikmeye toleranslıdır, raporlar ve dönemsel kararlar için idealdir.
- **Çevrimiçi (gerçek zamanlı)** sunum, tekil isteklere sıkı gecikme bütçeleri içinde yanıt verir; düşük gecikmeli özellik erişimi ve dikkatli kapasite planlaması gerektirir.
- **Akış** puanlama, olayları geldikçe sürekli puanlar; tazeliğin kritik olduğu sahtecilik tespiti ve izlemeye uygundur.
- **Uç** modelleri; gecikme, gizlilik, bağlantı ya da veri egemenliği nedenleriyle cihazlarda ya da şirket içi donanımda çalıştırır; kamuda ve saha ortamlarında yaygındır.

Gereksinimi karşılayan en basit kalıbı seçin ve devreye almayı gölge dağıtımlar, kanaryalar ve anında geri alma ile tasarlayın.

### Kayma, bozulma ve veri kalitesi için izleyin

Üretimde girdileri ve çıktıları ölçümleyin. **Veri kaymasına** (girdi dağılımlarının değişmesi), **[kavram kaymasına](https://en.wikipedia.org/wiki/Concept_drift)** (girdiler ile hedef arasındaki ilişkinin değişmesi), **veri kalitesi** başarısızlıklarına (boş değerler, şema değişiklikleri, kırık yukarı akış kaynakları) ve elinizde olduğu yerde gecikmeli gerçek değere karşı ölçülen **performans bozulmasına** dikkat edin. Uyarı eşikleri belirleyin, çalışma kılavuzları yazın ve izlemeyi yeniden eğitim tetikleyicilerinize bağlayın. Sessiz bozulma klasik ML başarısızlık kipidir ve izleme, ona karşı tek savunmanızdır.

## Ödünleşimler: artılar ve eksiler

| Karar | Seçenek A | Seçenek B | Ödünleşim |
|---|---|---|---|
| Sunum kalıbı | Toplu | Çevrimiçi | Basitlik ve maliyet, tazelik ve gecikmeye karşı |
| Özellik hesaplama | Özellik deposu | Model başına hatlar | Tutarlılık ve yeniden kullanım, kurulum yüküne karşı |
| Platform | Yönetilen bir MLOps platformu satın almak | Açık kaynak araçları bir araya getirmek | Hız ve destek, esneklik ve bağımlılığa karşı |
| Yeniden eğitim | Zamanlanmış | Kayma ile tetiklenen | Öngörülebilirlik, duyarlılık ve karmaşıklığa karşı |
| Tekrarlanabilirlik titizliği | Tam veri sürümleme | Hafif izleme | Denetim gücü, depolama ve emeğe karşı |

Kapsayıcı ödünleşim, şimdiki yatırım ile sonraki kırılganlık arasındadır. Ağır tekrarlanabilirlik ve izleme altyapısı baştan emek ister, ama açıklanamayan başarısızlıkların, yeniden üretilemeyen modellerin ve aşınmış güvenin çok daha büyük maliyetini önler. Yönetilen platformlar takımları hızlandırır ama bağımlılık yaratabilir; açık kaynak yığınlar, entegrasyon işi karşılığında kontrol sunar. Büyük kurumlar genellikle bu karmaşıklığı yol açılmış varsayılanların arkasına saklayan ortak bir platform takımından yarar görür.

## Takımınızla tartışılacak sorular

1. **Dağıtılmış bir modelin, bir müşteri ya da vatandaş zarar görmeden önce sessizce bozulduğunu nasıl öğrenirdik ve o uyarının sahibi kim?** Sessiz çürüme klasik ML başarısızlık kipidir: kod hâlâ çalışır, model hâlâ güvenle puanlar döndürür ve dünya eğitim verisinden uzaklaştıkça kalite kayar. Birçok model çalıştıran büyük bir takımda bunun tüm filo için bir kez değil, model başına yanıtlanması gerekir, çünkü her birinin kendi kayma profili ve kendi gerçek değer gecikmesi vardır. Veri kayması, kavram kayması ve veri kalitesi kırılmaları için mevcut izleyicilerinizi, uyarı eşiklerini ve kimin yanıt vereceğini söyleyen çalışma kılavuzunu getirin. Etiketlerin haftalar geç geldiği düzenlemeye tabi ortamlarda, bu arada izleyebileceğiniz vekil sinyalleri tartışın, çünkü gecikmeli gerçek değeri beklemek, zararı keşfetmeyi beklemek demektir. Bir modelin kayma uyarısı için tek bir sahip adlandırılmamışsa, o model fiilen izlenmiyor demektir.

2. **Bir denetçi bizden on sekiz ay önceki belirli bir tahmini yeniden üretmemizi isteseydi, bunu gerçekten uçtan uca yapabilir miydik?** Tekrarlanabilirlik, iyi mühendisliğin içinde gizlenen uyum gereksinimidir: bir kurumun, birini etkileyen bir kararı tam olarak hangi modelin, hangi veri üzerinde eğitilmiş, hangi kodla ürettiğini yanıtlamasını sağlar. Gerçek bir örnek getirin ve izlemeyi deneyin: değişmez veri anlık görüntüsü, git işlemesi, kilitli bağımlılıklar ve kapsayıcı imgesi, kaydedilmiş tohumlar ve ham veriden özelliklere ve dağıtılmış modele uzanan köken. İşaret, bu zincirdeki herhangi bir halkanın eksik ya da elle yapılan olup olmadığıdır. Kamu ve düzenlemeye tabi sektörler için yasanın gerçekte gerektirdiği saklama süresine karar verin ve depolamanızın kökeni o pencerenin tamamı boyunca yanıtlanabilir tuttuğunu doğrulayın, çünkü bir boşluk rutin bir sorguyu adli bir acil duruma çevirir.

3. **Bir modeli üretime terfi ettirme ve geri alma kuralımız nedir ve bu kural kayıt defteri tarafından mı, yoksa yalnızca güvenle mi uygulanıyor?** Yönetilmeyen terfi, not defteri deneylerinin üretime sızma biçimidir ve kötü bir modelin, kimse onu temiz biçimde geri alamadığı için orada kalma biçimidir. Birçok takımda olgun ile kırılgan arasındaki fark, model kayıt defterinin terfiyi zorunlu onay ve değerlendirmeyle kapılayıp kapılamadığı ya da bir mühendisin ağırlıkları elle itip itemediğidir. Mevcut terfi yolunuzu, geri alma mekanizmanızı ve gölge dağıtımların ya da kanaryaların tam trafikten önce gerçekten çalıştığına dair kanıtı getirin. Yeniden eğitimin zamanlanmış mı yoksa kayma ile mi tetiklendiğini ve yeniden eğitilen modellerin dağıtımdan önce doğrulama kapılarından geçip geçmediğini tartışın, çünkü canlı veride doğrulamasız yeniden eğitim kaymayı ya da zehirlenmeyi büyütür. Yanıt, insanların uyması beklenen bir wiki sayfasında değil, platformda uygulanmalıdır.

4. **MLOps platformumuzu açık kaynak araçlar üzerinde mi kuruyoruz, yönetilen birini mi satın alıyoruz, yoksa ikisini mi harmanlıyoruz ve bağımlılığı kim tarttı?** Bu seçim, gelecekteki her modelin ne kadar hızlı yayına çıkacağının ve verileriniz ile hatlarınız üzerinde ne kadar kontrol tutacağınızın tavanını belirler. Yönetilen bir platform takımları üretime hızla ulaştırır ve desteği taşır, ama özellik tanımlarınızı, köken kayıtlarınızı ve model yapıtlarınızı kolayca ayrılamayacağınız tescilli bir biçime hapsedebilir; bir araya getirilmiş açık kaynak yığın, gerçek entegrasyon ve bakım emeği karşılığında sizi taşınabilir tutar. Her yol için toplam sahip olma maliyetini (lisans ya da inşa, depolama, yeniden eğitim için işlem ve onu işletecek platform kadrosu), takımınızın altyapıyı işletme kapasitesine dair dürüst bir değerlendirmeyi ve somut bir çıkış testini getirin: kayıt defterinizi, özellik deponuzu ve kökeninizi dışa aktarıp başka yerde yeniden kurabilir misiniz? Kurumsal ve kamu ortamlarında tedarik kısıtlarını ve veri egemenliği kurallarını ekleyin, çünkü eğitim verisini düzenleyicinizin yasakladığı bir bölgede ya da biçimde saklayan bir platform, ne kadar kullanışlı olursa olsun diskalifiye edilir.

5. **Özellik depomuz ve model kayıt defterimiz tek bir merkezi platform mu olmalı, yoksa takım başına birleşik (federe) mi ve eğitim-sunum sapması bugün bize neye mal oluyor?** Özellik tanımlarını merkezileştirmek, bir özelliğin eğitimde bir biçimde, sunumda başka bir biçimde hesaplandığı sapmayı ortadan kaldırır; bu sessiz ve pahalı bir doğruluk kaybı kaynağıdır, ama tek bir platform her takımı yavaşlatan bir darboğaza dönüşebilir. Federasyon, takımlara özerklik verir ama tesisatı ve iki takımın aynı özelliği tutarsız tanımlama olasılığını çoğaltır. Sapmanın sizi nerede zaten ısırdığına, kaç takımın özellikleri yeniden kullanıp kaçının yeniden inşa ettiğine ve ortak bir platform takımının sunabileceği yol açılmış varsayılanlara dair kanıt getirin. Büyük bir kurum için tek bir denetlenebilir kayıt sisteminin yönetişim yararını merkezi bir kuyruğun teslimat maliyetine karşı tartın ve düzenlemeye tabi ortamlarda, bir denetçinin herhangi bir tahmini onu üreten tam özellik koduna izlemesini sağlayan merkezi kökeni tercih edin.

6. **Her modelin dağıtım kalıbını gerçek gecikme, tazelik ve egemenlik ihtiyaçlarıyla eşleştirdik mi, yoksa her şeyi tek bir biçime mi varsayılan yaptık?** Toplu, çevrimiçi, akış ve uç, çok farklı işletme maliyeti ve karmaşıklık taşır; yanlış olanı seçmek ya bir gecelik raporun hiç ihtiyaç duymadığı gerçek zamanlı altyapıya aşırı harcama yapar ya da bir sahtecilik puanlayıcısını bağımlı olduğu tazelikten mahrum bırakır. Her iş yükü için gereksinimin gerçekte hangi kalıbı haklı çıkardığına karar verin ve modern hissettirdiği için en karmaşık seçenekte standartlaşmaya direnin. Her model için gecikme bütçesini, hacmi, bayat bir yanıtın maliyetini ve gerçek değer gecikmesini getirin. Kamu ve saha ortamlarında uç ve şirket içi dağıtımı bilinçli biçimde tartın, çünkü veri egemenliği kuralları ya da kesintili bağlantı modelleri yerel donanıma zorlayabilir ve bu seçim, oraya ittiğiniz her modeli nasıl sürümlediğinizi, izlediğinizi ve geri aldığınızı yeniden şekillendirir.

## Sektör merceği

**Girişim.** En kıt kaynağınız mühendislik dikkatidir; bu yüzden MLOps'u hafif tutun ve satın alın. Deneyleri basit bir barındırılan araçta izleyin, dağıtılan her modeli eğitim verisi anlık görüntüsüne ve git'teki kod işlemesine sabitleyin ve bir platform yerine tek bir ucuz kayma denetimi ekleyin. İkinci ya da üçüncü bir model yeniden kullanımı değerli kılana kadar özellik deposunu ve özel hatları atlayın; bakımını yapamayacağınız kırılgan bir yığın, eksik bir yetkinlikten daha hızlı batırır.

**Küçük işletme.** Büyük olasılıkla bir ML platform uzmanınız yok ve bütçeniz dar; bu yüzden MLOps'u kadro kurduğunuz bir sistem olarak değil, zaten çalıştırdığınız araçlara gömülü bir şey olarak görün. Sürümlemeyi, dağıtımı ve izlemeyi sizin yerinize halleden yönetilen bir hizmeti tercih edin ve disiplini bir veri hijyeni ve tekrarlanabilirlik sorusu olarak çerçeveleyin: belirli bir sonucu hangi modelin ve verinin ürettiğini bilin ve geri alma yeteneğini koruyun. Verilerinizi ve modellerinizi dışa aktarmanıza izin veren satıcıları tercih edin; böylece sonraki bir geçiş mümkün kalır.

**Kurumsal.** Sorun, düzinelerce model ve çok sayıda takım arasında ölçektir: gruplar hatları yeniden icat etmeyi bıraksın diye ortak bir özellik deposu, deney izleme ve yönetilen terfiye sahip bir model kayıt defteri. Yol açılmış varsayılanlar sunan bir platform takımı bütçeleyin, her model denetlenebilir ve her olay açıklanabilir olsun diye kökeni ve izlemeyi standartlaştırın ve yap ya da satın al ile bağımlılığı, alttaki araçları değiştirilebilir tutan bir arayüzün arkasında bilinçli biçimde yönetin. Doğrulama kapılarını ve geri almayı gelenekte değil, platformda uygulayın.

**Kamu.** Tekrarlanabilirlik, köken ve sürümleme kılık değiştirmiş uyum gereksinimleridir; bu yüzden onları ilk günden birinci sınıf olarak ele alın. Dağıtılan her modelin ardındaki tam veri kümesini ve kodu sürümleyin, bu kökeni yasal olarak gerekli süre boyunca saklayın ve bir vatandaşı etkileyen herhangi bir geçmiş tahmini yeniden üretebilin. Ağır sonuçlu kararları bir insanın incelemesinde tutun, veri egemenliği kurallarının gerektirdiği yerde uç ve şirket içi dağıtımı tartın ve herhangi bir satıcı platformunun verilerinizin, özelliklerinizin ve kökeninizin tam taşınabilirliğini vermesini isteyin.

## Örnekler

**Girişim.** Küçük bir analitik girişimi, ilk müşteri kaybı tahmin modelini tek bir veri bilimci ve hafif bir kurulumla yayına aldı. Deneyleri basit bir barındırılan araçta izledi, dağıtılan her modeli eğitim verisi anlık görüntüsüne ve git'teki kod işlemesine sabitledi ve yakın zamanlı girdileri eğitim dağılımıyla karşılaştıran basit bir haftalık iş ekledi. Bir veri kaynağı tarih biçimini değiştirip tahminler kaymaya başladığında, bu basit denetim bunu öfkeli bir müşteri aramasından sonra değil, günler içinde yakaladı ve takım son iyi modeli yeniden üretip geri alabildi.

**Kurumsal.** Bir perakende bankası düzinelerce kredi ve sahtecilik modeli çalıştırıyor. Takımlar arasında paylaşılan bir özellik deposunda, bir deney izleme hizmetinde ve zorunlu onay kapıları olan bir model kayıt defterinde standartlaştı. Üretimdeki her model, eğitim verisi anlık görüntüsüne ve kod işlemesine kadar izlenebiliyor. Sahtecilik modelleri akış puanlayıcılar olarak, kredi modelleri toplu olarak çalışıyor. Bir izleme katmanı girdi kaymasını gözlüyor ve bir veri kaynağı şeması değiştiğinde uyarıyor; bu, bir keresinde kırık bir yukarı akış beslemesini kararları bozmadan önce yakaladı.

**Kamu.** Bir kamu yardımları kurumu, vaka incelemelerine öncelik vermek için bir ML modeli kullanıyor. Bu kararlar vatandaşların hizmetlere erişimini etkilediğinden kurum, dağıtılan her modelin ardındaki tam veri kümesini ve kodu sürümlüyor, bu kökeni yasal olarak gerekli süre boyunca saklıyor ve istendiğinde geçmişteki herhangi bir tahmini yeniden üretebiliyor. Modeller, işaretlenen vakaları bir insanın incelediği toplu olarak dağıtılıyor ve gelen nüfus kaydığında bir kayma izleyicisi zorunlu bir yeniden değerlendirme başlatıyor; böylece model, doğrulandığı koşulların dışında sessizce uygulanmıyor.

## İş gerekçesi: motivasyonlar, YG ve TSM

MLOps, kırılgan deneyleri güvenilir varlıklara dönüştürerek kendini amorti eder. YG (yatırım getirisi); yeni modeller için daha hızlı üretime geçişten, daha az maliyetli olaydan, daha az yinelenen altyapıdan ve çok sayıda modeli küçük bir platform takımıyla işletebilme yeteneğinden gelir. Ortak bir özellik deposu ve kayıt defteri, model başına teslimat süresini dramatik biçimde kısaltabilir, çünkü takımlar aynı tesisatı yeniden inşa etmeyi bırakır.

TSM (toplam sahip olma maliyeti); platform inşası ya da lisansını, sürümlü veri ve modeller için depolamayı, yeniden eğitim için işlemi ve hepsini işletecek kadroyu kapsar. Bunu benimsememenin maliyetine karşı tartın: yeniden üretemediğiniz ya da denetleyemediğiniz modeller, müşterilere ya da vatandaşlara zarar veren sessiz başarısızlıklar ve düzenleyici bulgular. Düzenlemeye tabi ortamlarda, bir denetimde açıklanamayan bir modelin maliyeti, tüm MLOps yatırımını gölgede bırakabilir. Gerekçeyi liderliğe MLOps'u bir yük olarak değil, risk azaltma ve teslimat hızlandırma olarak çerçeveleyerek sunun: gelecekteki her modelin yolculuk edeceği yol açılmış bir yol.

## Anti-kalıplar ve tuzaklar

- **Not defterinden üretime sıçramalar.** Yönetilmeyen not defterlerinde eğitilmiş modelleri tekrarlanabilirlik olmadan dağıtmak.
- **Eğitim-sunum sapması.** Eğitimde ve sunumda farklı özellik kodu, sessiz doğruluk kaybına yol açar.
- **Veri sürümlemesi yok.** Kodu sürümleyip veriyi sürümlememek; böylece çalıştırmalar yeniden üretilemez.
- **Dağıt ve unut.** Bir modeli izleme olmadan yayına almak, bozulmayı ancak kullanıcılar şikayet edince keşfetmek.
- **Otopilotta yeniden eğitim.** Canlı veride doğrulama olmadan otomatik yeniden eğitim yapmak; kaymayı ya da zehirlenmeyi büyütür.
- **Tek seferlik altyapı.** Her takımın kendi hattını kurması; maliyeti ve kırılganlığı çoğaltır.
- **Gecikmeli etiketleri yok saymak.** Gerçek değer haftalar sonra geldiğinde doğruluğu anında ölçebileceğinizi varsaymak.

## Olgunluk modeli

1. **Düzey 1, Başlangıç.** Modeller not defterlerinde geçici olarak kuruluyor; elle dağıtım; veri ya da modellerin sürümlemesi yok; izleme yok; geçmiş bir tahmini yeniden üretmek bir tahmin oyunu.
2. **Düzey 2, Geliştirme.** Bir miktar deney izleme ve bir model kayıt defteri ortaya çıkıyor ama uygulamalar takıma göre değişiyor; dağıtım yarı otomatik; temel izleme birkaç modeli kapsıyor; veri sürümleme kısmi ve kökende boşluklar var.
3. **Düzey 3, Standartlaştırma.** Bir özellik deposu, kayıt defteri, tekrarlanabilir hatlar ve uçtan uca köken içeren ortak bir platform belgeleniyor ve kurum genelinde uygulanıyor; kayma ve veri kalitesi izlemesi modeller arasında çalışıyor; terfi ve geri alma her takımın kullandığı yönetilen bir yolu izliyor.
4. **Düzey 4, Yönetme.** Filo referans düzeylere karşı ölçülüyor: kayma oranları, veri kalitesi kırılmaları, gecikmeli gerçek değere karşı model doğruluğu, eğitim-sunum sapması, üretime geçiş süresi ve model başına işletme maliyeti ölçüt olarak izleniyor; uyarı eşikleri ve doğrulama kapıları kanıta dayalı olarak uygulanıyor ve her modelin sağlığı, adı belli bir sahiple sabit bir sıklıkla inceleniyor.
5. **Düzey 5, Orkestrasyon.** Yaşam döngüsü tamamen otomatik, denetlenebilir ve uyarlanabilir; kayma ile tetiklenen yeniden eğitim doğrulama kapılarının arkasında çalışıyor; self servis yol açılmış yollar takımların güvenle teslim etmesini sağlıyor; sürekli değerlendirme model performansını iş ölçütlerine bağlıyor ve platform teslimat, risk ve uyumla bütünleşiyor; böylece veri ve koşullar değiştikçe modeller rutin biçimde emekliye ayrılıyor, değiştiriliyor ve yeniden kapsamlandırılıyor.

## Tartışma fikirleri

- Deney özgürlüğü ile üretim tekrarlanabilirliğini nasıl dengelersiniz?
- Kullanım örnekleriniz için doğru yeniden eğitim tetikleyicisi nedir (zamanlama, kayma ya da performans aşınması)?
- Veri ve model kökenini ne kadar süre saklamanız gerekir ve bu gereksinimi ne belirler?
- Özellik depoları ve kayıt defterleri merkezi platformlar mı olmalı, yoksa takım başına birleşik mi?
- Gerçek değer etiketleri uzun gecikmelerle geldiğinde doğruluğu nasıl izlersiniz?
- Uç dağıtım, eklediği işletme karmaşıklığına ne zaman değer?

## Önemli çıkarımlar

- ML davranışı kod artı veri artı modelden gelir; üçünü birlikte sürümleyin ve yönetin.
- Özellik depoları, deney izleme ve kayıt defterleri tekrarlanabilir ML'in omurgasıdır.
- Köken, modelleri denetlenebilir ve olayları açıklanabilir kılar: düzenlemeye tabi ortamlarda vazgeçilmezdir.
- Gecikme, tazelik ve egemenlik ihtiyaçlarına uysun diye toplu, çevrimiçi, akış ya da ucu seçin.
- Modeller bozulur; kayma, veri kalitesi ve aşınma için izleme isteğe bağlı değildir.

## Kaynaklar ve ileri okuma

- Chip Huyen, *Designing Machine Learning Systems*.
- Andriy Burkov, *Machine Learning Engineering*.
- D. Sculley et al., *Hidden Technical Debt in Machine Learning Systems*.
- Mark Treveil et al., *Introducing MLOps*.
- Valliappa Lakshmanan, Sara Robinson, and Michael Munn, *Machine Learning Design Patterns*.
- Emmanuel Ameisen, *Building Machine Learning Powered Applications*.
