# 9.4 Maliyet, sürdürülebilirlik ve yeşil yazılım

## Genel bakış ve motivasyon

Yazılım; para, elektrik, su ve malzeme tüketen fiziksel bir altyapı üzerinde çalışır. Bilişim tarihinin büyük bölümünde bu maliyetler bir başkasının sorunuydu: sermaye bütçeleri donanımı gizliyordu ve enerji mühendisler için görünmezdi. [Bulut bilişim](https://en.wikipedia.org/wiki/Cloud_computing) bunu değiştirdi. Tüketimi ayrıntılı, talebe bağlı ve doğrudan atfedilebilir hale getirdi; bu da maliyeti ve giderek karbonu birer mühendislik meselesine dönüştürdü. Bu bölüm iç içe geçmiş iki disiplini ele alır: değişken bulut harcamalarına mali hesap verebilirlik getirme pratiği olan **FinOps** ve aynı işi daha az enerjiyle, daha düşük karbon emisyonuyla yapan sistemler kurma pratiği olan **[yeşil yazılım](https://en.wikipedia.org/wiki/Green_computing)**. İkisi büyük ölçüde örtüşür, çünkü verimli yazılım çoğu zaman hem daha ucuz hem daha temizdir.

Büyük takımlar için rakamlar çok büyüktür. Büyük bir kurumun bulut faturası yılda onlarca ya da yüzlerce milyona ulaşabilir ve birkaç puanlık israf, kadro ya da ürün finanse edebilecek gerçek paradır. Büyük dijital varlıkların [karbon ayak izi](https://en.wikipedia.org/wiki/Carbon_footprint) de kayda değerdir ve kuruluşlar bunu ölçmek ve azaltmak için düzenleyicilerden, yatırımcılardan, müşterilerden ve kendi çalışanlarından artan bir baskı görür. Yüzlerce takım örnek boyutları, veri saklama süreleri ve mimari hakkında bağımsız kararlar aldığında küçük verimsizlikler birikerek büyük maliyetlere ve emisyonlara dönüşür. Maliyeti ve karbonu görünür ve hesap verilebilir kılan bir yönetişim, ikisini de kontrol altında tutmak için şarttır.

Kurumsal ve kamu açısından önemi doğrudandır. Kamu kuruluşları vergi mükelleflerinin parasını harcar ve giderek sürdürülebilirlik yükümlülükleri ile net sıfır taahhütleriyle bağlıdır; bu yüzden verimli, düşük karbonlu işletim göstermek hem mali hem politika yükümlülüğüdür. Şirketler çevresel performansları üzerinde yatırımcı denetimiyle ve marjlar üzerinde rekabet baskısıyla karşılaşır. Her iki ortamda da maliyet ve sürdürülebilirlik sonradan akla gelen konulardan yönetim kurulu düzeyindeki kaygılara dönüşmüştür. Bu kaygılar nihayetinde mühendislik tercihlerinde gerçekleşir ya da kaçırılır.

## Temel ilkeler

- **Tüketimi görünür kılın.** Göremediğinizi iyileştiremezsiniz; maliyet ve karbon, onlara yol açan takımlara ve hizmetlere atfedilmelidir.
- **Hesap verebilirlik sahiplerdedir.** Kaynakları sağlayan mühendisler kendi maliyet ve karbon etkilerini görmeli ve sahiplenmelidir.
- **Verimlilik maliyete ve karbona birlikte hizmet eder.** Aynı işi daha az kaynakla yapmak çoğu zaman aynı anda hem para hem emisyon tasarrufu sağlar.
- **Sürekli doğru boyutlandırın.** Talep değişir, bu yüzden kaynak sağlama bir kez yapılıp unutulmamalı, yeniden gözden geçirilmelidir.
- **Karbonun zamanı ve yeri vardır.** Aynı hesaplama, elektriğin ne zaman ve nerede üretildiğine bağlı olarak daha fazla ya da daha az emisyon üretir.
- **Üçlüyü dengeleyin.** Maliyet, performans ve güvenilirlik birbiriyle ödünleşir; körü körüne değil, bilinçli iyileştirin.
- **Verimliliği erken tasarlayın.** Mimari tercihler, geç aşama ince ayarlardan çok daha fazla uzun vadeli maliyeti ve karbonu belirler.

## Öneriler

### FinOps görünürlüğü, iyileştirmesi ve hesap verebilirliği kurun

FinOps üç yinelemeli aşamada ilerler. **Bilgilendir**: etiketleme, tahsis ve panolarla görünürlük kurun; böylece her maliyet bir takıma, hizmete ve iş amacına atfedilir ve ortak maliyetler adil biçimde paylaştırılır. **İyileştir**: israfı (boşta kalan ve sahipsiz kaynakları) ortadan kaldırın, gereğinden büyük hizmetleri doğru boyutlandırın, sabit taban yük için rezervasyonlar ya da tasarruf planları gibi taahhüt temelli indirimleri benimseyin ve kesintiye uğrayabilen işler için spot ya da önceden vazgeçilebilir kapasite kullanın. **İşlet**: bütçeler, anomali uyarıları, tahminler ve düzenli incelemelerle maliyeti olağan mühendislik pratiğine yerleştirin. Hepsinden önemlisi, maliyet verisini onu yaratan mühendislerin önüne koyun. Verimliliği yalnızca finansın değil, mühendisliğin, finansın ve ürünün ortak hedefi yapın.

### Karbon farkındalıklı ve enerji verimli yazılım geliştirin

Karbonu azaltmanın üç kaldıracı vardır. **Enerji verimliliği**: yazılımı daha iyi algoritmalar, önbellekleme ve gereksiz hesaplamadan kaçınma yoluyla aynı işi daha az CPU döngüsü, daha az bellek ve daha az veri hareketiyle yapacak biçimde yazın ve yapılandırın. **Donanım verimliliği**: daha yüksek kullanım, birleştirme ve modern verimli donanım yoluyla kaynakları tam kullanın; çünkü boşta kapasite de güç çeker ve üretim karbonunu bünyesinde taşır. **Karbon farkındalığı**: esnek iş yüklerini zamanda ve mekânda şebekenin daha temiz olduğu zamana ve yere kaydırın; örneğin toplu işleri yenilenebilir üretimin yüksek olduğu saatlerde ya da düşük karbonlu elektriğin bulunduğu bölgelerde çalıştırın. Yazılım Karbon Yoğunluğu (Software Carbon Intensity) belirtimi gibi tanınmış yaklaşımlarla ölçün. Güçlü yenilenebilir taahhütleri ve şeffaf raporlaması olan sağlayıcıları ve bölgeleri tercih edin.

### Sürdürülebilir mimariler tasarlayın ve doğru boyutlandırın

Mimari, maliyet ve karbon için tabanı belirler. Gerçek talebe göre ölçeklenen ve boştayken sıfıra ölçeklenen esnek tasarımları tercih edin; böylece kullanılmayan kapasiteyi ayakta tutmak için hiç ödeme yapmazsınız. [Sunucusuz](https://en.wikipedia.org/wiki/Serverless_computing) mimari ve [otomatik ölçekleme](https://en.wikipedia.org/wiki/Autoscaling) dalgalı iş yüklerinde israfı azaltır ve yönetilen hizmetler [çok kiracılılık](https://en.wikipedia.org/wiki/Multitenancy) sayesinde kullanımı iyileştirebilir. Hesaplamayı, depolamayı ve veritabanlarını korkuyla gereğinden fazla ayırmak yerine gerçek kullanıma göre boyutlandırın. Soğuk verinin daha ucuz, daha az enerji tüketen katmanlara taşınması ya da silinmesi için veri yaşam döngüsü ilkeleri belirleyin. Veri hacmini ve ağ aktarımını azaltmak hem depolama maliyetini hem bitleri taşımanın enerjisini düşürür. Verimliliği, performans ve güvenilirlikle birlikte incelenen bir tasarım gereksinimi olarak ele alın.

### Maliyet, performans ve güvenilirliği bilinçli dengeleyin

Maliyet, performans ve güvenilirlik bir üçlü oluşturur. Birini zorladığınızda genellikle diğerlerini vergilendirirsiniz: daha fazla artıklık ve daha düşük gecikme daha pahalıdır ve çoğu zaman daha fazla enerji tüketir. Bu ödünleşimleri açık hale getirin ve iş değerine bağlayın. Hizmetin gerçekte ne kadar güvenilirliğe ve performansa ihtiyaç duyduğunu tanımlamak için SLO'ları ([hizmet düzeyi hedefleri](https://en.wikipedia.org/wiki/Service-level_objective)) kullanın, sonra her şeyi tekdüze biçimde fazla donatmak yerine o hedefe göre kaynak ayırın. Kritik olmayan ve iç iş yükleri daha ucuz, daha az artıklı, karbon açısından daha esnek yapılandırmaları kabul edebilir. Üst düzey kaynak ayırmayı gerçekten hak edene saklayın.

### Boğmadan yönetin

Kapı değil, korkuluk sağlayın. Merkezi platform takımları verimli varsayılanlar, etiket zorlaması, bütçe uyarıları ve self servis panolar sunabilir; günlük kararları ise iş yüklerinin sahibi takımlara bırakabilir. Maliyet verimliliği ve karbon azaltımı için kurum genelinde hedefler belirleyin, ilerlemeyi şeffaf biçimde raporlayın ve tasarrufları kutlayın. Teslimatı yavaşlatan ağır onay bürokrasisinden kaçının. Amaç, verimli seçimi kolay varsayılan yapmaktır.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| Taahhüt indirimleri | Taban yükte büyük tasarruf | Kilitlenme, talep değişirse risk |
| Spot/önceden vazgeçilebilir kapasite | En ucuz hesaplama, boşta kalan şebeke kapasitesini kullanır | Kesintiler, artan karmaşıklık |
| Agresif doğru boyutlandırma | Daha düşük maliyet ve karbon | Ani yükselmelerde yetersiz kaynak riski |
| Karbon farkındalıklı zamanlama | Daha düşük emisyon | Geciken işler, mühendislik eforu |
| Çok bölgeli artıklık | Daha yüksek güvenilirlik | Daha fazla maliyet, enerji ve karbon |

Bütün bunları birleştiren ödünleşim şudur: azami güvenilirlik ve performans nadiren asgari maliyet ve karbonla örtüşür. Artıklı, her zaman açık, düşük gecikmeli sistemler pahalıdır ve çok enerji tüketir; bu yüzden tekdüze fazla donatma, buna ihtiyaç duymayan iş yüklerinde hem parayı hem emisyonu boşa harcar. Disiplin, hırsı SLO'lar yoluyla iş değerine göre ayarlamak ve üst düzey kaynakları yalnızca önemli olan yerde harcamaktır. Taahhüt indirimleri ve spot kapasite gerçek tasarruf sunar, ancak yönetmeniz gereken kilitlenme ve kesinti riski getirir. Karbon farkındalıklı zamanlama emisyon tasarrufu sağlar, ama yalnızca gecikmeye ya da başka yere taşınmaya tahammül eden iş yüklerine uyar.

## Takımınızla tartışılacak sorular

1. **Bulut harcamanızın ne kadarı bugün gerçekten etiketlenmiş ve bir takıma atfedilmiş durumda?** FinOps'un bilgilendirme aşaması temeldir: göremediğinizi iyileştiremezsiniz ve etiketsiz, tahsis edilmemiş harcama, israfın kimsenin sorumluluğunda olmadığı anlamına gelir. Tartışmaya bir istek değil, gerçek kapsam rakamını ve etiketsiz en büyük kalemlerin listesini getirin. Yüzlerce takımın bağımsız kaynak sağladığı büyük bir kurumda düşük atfetme oranı, ortak verimsizliklerin görünmez biçimde milyonlara birikmesi demektir. Kamu ve kurumsal ortamlarda atfetme, vergi mükellefi ya da hissedar harcamasını savunmanın ve ortak platformların maliyetlerini adil paylaştırmanın da yoludur. Cevap ilk hamlenizi belirler: kapsam düşükse, doğru boyutlandırmadan önce etiket zorlaması ve tahsis gelir, çünkü görünürlüksüz iyileştirme tahmin yürütmektir.

2. **Taban yükünüzün ne kadarı taahhüt indirimleriyle karşılanıyor ve talep değişirse bu taahhütlere ne olur?** Rezervasyonlar ve tasarruf planları sabit taban yükte büyük tasarruf sağlar, ancak kilitlenme getirir; bu yüzden çok agresif satın almak, bir ürün sonlandığında ya da taşındığında indirimi bir yükümlülüğe çevirir. Rakamları getirin: taahhüt edilmiş kapsam yüzdenizi, taban yük eğilimini ve önümüzdeki yıl şekil değiştirmesi en olası iş yüklerini. Disiplin, yalnızca kalıcı olacağından emin olduğunuz tabanı taahhüt etmek, değişken katmanı talep üzerine ya da spot kapasiteyle karşılamak ve talep geliştikçe yeniden gözden geçirmektir. Büyük bir kurum için bu, gerçek mali maruziyeti olan hazine tarzı bir karardır; bu yüzden finans ve mühendislik bunu taraflardan biri tek başına değil, birlikte sahiplenmelidir. Cevap, kalıcı taban yükünüzü belirsiz talebinizden ayırmalı ve taahhütleri öncekine göre boyutlandırmalıdır.

3. **Filonuzun ne kadarı boşta duruyor ve yalnızca çalışırken yaktığı enerjiyi mi sayıyorsunuz, yoksa bünyesindeki üretim karbonunu da mı?** Boşta kapasite de güç çeker ve donanımı üretmek için zaten harcanmış üretim karbonunu taşır; bu yüzden gereğinden fazla kaynak ayırırken yalnızca çalışma enerjisine odaklanmak ayak izinin gerçek bir bölümünü kaçırır. Kullanım verisini getirin: ortalama ve tepe, ayrılan ile kullanılan arasındaki fark ve sıfıra ölçeklemenin ya da birleştirmenin mümkün olduğu yerler. Daha yüksek kullanım maliyete ve karbona aynı anda hizmet eder, bu bölümün ana çizgisi budur; dolayısıyla boşta israf elinizdeki en temiz kazanımdır. Net sıfır yükümlülüğü altındaki kuruluşlar için, bünyesindeki emisyonları da içeren dürüst bir karbon ölçümü, gerçek ilerleme ile düzenleyici ve itibar tepkisini davet eden yeşil badanayı birbirinden ayırır. Cevap, en düşük kullanımlı iş yüklerinizi birleştirme, otomatik ölçekleme ya da sıfıra ölçekleme için hedeflemeli ve üretim karbonunu sessizce görmezden gelmeyen bir ölçüm yaklaşımı belirlemelidir.

4. **Mühendisleriniz kendi hizmetlerinin maliyetini ve karbonunu görüyor mu ve gördüklerine göre harekete geçen var mı?** Görünürlük ancak kaynakları sağlayan insanlara ulaşıp davranışlarını değiştirdiğinde karşılığını verir; bu yüzden finansın ayda bir incelediği ama mühendislerin hiç açmadığı bir pano hesap verebilirlik değil, süstür. Rekabet eden çekim gerçektir: platform takımları merkezi kontrol ve temiz raporlama ister, teslimat takımları ise gözetim ya da teslimatta bir kapı gibi hissettiren her şeye içerler. Maliyet ve karbon verisine gerçekte kimin baktığına, ne sıklıkla baktığına ve son çeyrekte bundan bir doğru boyutlandırma ya da temizlik doğup doğmadığına dair kanıt getirin. Yüzlerce takımın bağımsız kaynak sağladığı büyük bir kurumda, mühendislerin sahiplendiği bir sinyal ile görmezden geldikleri bir rapor arasındaki fark, birikerek büyüyen tasarruf ile birikerek büyüyen israf arasındaki farktır. Kurumsal ve kamu ortamlarında birim ekonomisini (istek, müşteri ya da dosya başına maliyet ve karbon) sahibi takımın önüne koyun; çünkü toplam rakam bir bütçeyi savunur, ama birim başına rakam bir tasarım kararını değiştirir.

5. **İş yüklerinizden hangileri zaman ya da bölge açısından gerçekten esnek ve onları şebekenin daha temiz olduğu yerde zamanlamak için neler gerekir?** Karbon farkındalıklı zamanlama, esnek işi elektriğin düşük karbonlu olduğu zamana ve yere kaydırır, ama yalnızca gecikmeye ya da başka yere taşınmaya tahammül eden işlere uyar; bu yüzden ilk iş, gerçekten ertelenebilir toplu işleri kullanıcıya dönük ya da gecikmeye bağlı her şeyden ayırmaktır. Ödünleşim şudur: işleri bölgeler ya da yoğun olmayan zaman pencereleri arasında taşımak mühendislik eforu, veri aktarım maliyeti ve bazen tasarruf edilen emisyonu aşabilecek veri ikameti riski getirir. Aday toplu ve analitik işlerin listesini, gecikme toleranslarını, veri ikameti kısıtlarını ve yasal olarak çalıştırabileceğiniz bölgelerin karbon yoğunluğunu getirin. Kurumlar için bu, doğru boyutlandırmanın üstüne küçük bir iyileştirmedir; bu yüzden onu maliyet temellerinden önce değil, sonra sıralayın. Kamuda veri ikameti ve egemenlik kuralları, şebekenin ne kadar temiz olduğuna bakılmaksızın vatandaş verisinin sınır ötesine taşınmasını yasaklayabilir; bu yüzden bölge seçimi karbondan önce hukuki bir sorudur.

6. **Hangi verimlilik ve sürdürülebilirlik hedeflerini belirlediniz ve bunlar, hedefe ulaşmanın güvenilirliği sessizce bozamayacağı biçimde mi yazılmış?** Hedefler çabayı odaklar, ama kaba bir maliyet ya da karbon hedefi yanlış davranışı çağırır: takımlar yetersiz kaynak ayırır, artıklığı söker ya da işi ertelerken küçük bir tasarrufu büyük bir olayla takas eder. Gerilim, liderliğin raporlayabileceği iddialı yukarıdan aşağı bir rakam ile her hizmetin gerçek SLO'larına dayanan aşağıdan yukarı bir hedef arasındadır; bu yüzden ikisi dayatılmak yerine uzlaştırılmalıdır. Mevcut hedeflerinizi, ölçüldükleri taban çizgisini ve iyileştirmenin bir hizmetin gerçekten ihtiyaç duyduğu şeye dokunmasını engelleyen güvenilirlik korkuluklarını getirin. Büyük bir kurumda toplam hedefler, iş yükleri farklı olan takımlara adil biçimde ayrışmalıdır; bu yüzden müşteriye dönük bir ödeme hizmeti ile iç bir raporlama işi aynı verimlilik beklentisini taşımamalıdır. Sürdürülebilirlik rakamlarının kamuya açık bildirimlerde göründüğü kurumsal ve kamu bağlamlarında, raporlanan her rakamı denetlenebilir bir ölçüm yöntemine bağlayın; çünkü inceleme altında savunamayacağınız bir hedef başarı değil, yükümlülüktür.

## Sektör merceği

**Girişim.** Maliyet, pistinizdir; bu yüzden bir öğleden sonra etiketleme ve tek bir bütçe uyarısı yeniden fon toplamadan önce size bir ay daha kazandırabilir. FinOps sürecini ve karbon muhasebesini tümüyle atlayın; yalnızca faturaya bakın, boştaki kaynakları öldürün ve hazır bekleyen kapasite için değil yük için ödeme yapmanızı sağlayan, sıfıra ölçeklenen yönetilen bir platform seçin. En kıt kaynağınız mühendislik dikkatidir; bu yüzden bariz israfı otomatikleştirin ve devam edin.

**Küçük işletme.** Ne bir FinOps uzmanınız ne de rahat bir bütçeniz var; bu yüzden özel bir platform satın almak yerine bulut sağlayıcınızın zaten verdiği maliyet araçlarına yaslanın. Aylık bir bütçe uyarısı kurun, sağlayıcının doğru boyutlandırma önerilerini açın ve operasyonel verimliliği fiyata katan yönetilen ve sunucusuz hizmetleri tercih edin. Sürdürülebilirliği, kadrolamanız gereken bir raporlama programı olarak değil, düşük karbonlu bir bölge ile verimli bir varsayılan seçmek olarak ele alın.

**Kurumsal.** Sorun, birçok takım arasında yönetişimdir: tutarlı etiketleme, ortak platform maliyetlerinin adil tahsisi, finans ve mühendisliğin birlikte sahiplendiği taahhüt indirimi stratejisi ve her takımın gördüğü sinyaller olarak sunulan maliyet ve karbon. Yüzlerce bağımsız kaynak sağlama kararının israfa birikmemesi için verimli varsayılanları ve bir ölçüm yöntemini standartlaştırın; bulut harcamasını ve emisyonları, yerel iyileştirmelerin dağınıklığı yerine hedefler, anomali uyarıları ve şeffaf raporlamayla bir portföy olarak yönetin.

**Kamu.** Tedarik kuralları, şeffaflık ve kamusal hesap verebilirlik her seçimi şekillendirir. Vergi mükelleflerinin parasını harcıyorsunuz ve çoğu zaman net sıfır yükümlülüğüyle bağlısınız; bu yüzden hem mali ihtiyatı hem denetlenmiş emisyon ilerlemesini göstermelisiniz, bu da yeşil badana yerine bünyesindeki donanımı da içeren dürüst bir karbon ölçümü demektir. Veri ikameti ve egemenlik kuralları, şebekenin ne kadar temiz olduğuna bakılmaksızın hangi bölgeleri kullanabileceğinizi kısıtlayabilir; verimlilik ve emisyon metriklerinin kamu denetimi için yayımlanması gerekebilir, bu yüzden denetim altında savunabileceğiniz ölçüm yöntemlerini seçin.

## Örnekler

**Girişim.** Tohum aşamasındaki bir girişim bulut faturasının iki ayda ikiye katlandığını görür ama nedenini söyleyemez. Bir kurucu bir öğleden sonrasını her kaynağı özelliğe göre etiketlemeye harcar ve basit bir bütçe uyarısı açar. Etiketler unutulmuş bir staging kümesini ve gece çalışan bir iş için günün 24 saati ayakta duran gereğinden büyük bir veritabanını ortaya çıkarır. Kümeyi kapatmak ve işi daha küçük bir örnekte, yoğun olmayan saatlerde zamanlanmış bir çalıştırmaya taşımak faturayı üçte bir oranında düşürür; bu da takıma bir ay daha pist kazandırır.

**Kurumsal.** Geniş, çok dağılmış bir bulut varlığına sahip çok uluslu bir perakendeci bir FinOps pratiği kurar. Etiketlemeyi zorunlu kılar, her maliyeti bir ürün takımına tahsis eder ve harcamayı mühendislerin her gün gördüğü panolarda gösterir. Bir yıl içinde boşta kaynakları kaldırır, gereğinden büyük hizmetleri doğru boyutlandırır ve sabit taban yük için tasarruf planları satın alarak bulut harcamasını kabaca dörtte bir oranında düşürür. Ardından gece çalışan analitik toplu işlerini daha düşük karbonlu bölgelerde ve yoğun olmayan saatlerde çalışacak biçimde zamanlar, hem maliyeti hem emisyonu azaltır ve karbon tasarruflarını yıllık sürdürülebilirlik bildiriminde raporlar.

**Kamu.** Ulusal bir net sıfır yükümlülüğü altında vatandaş hizmetleri işleten bir devlet kurumu, hem vergi mükelleflerinin parasında mali ihtiyatı hem emisyon hedeflerine doğru ilerlemeyi göstermek zorundadır. İş yüklerini doğru boyutlandırır ve birleştirir, nadiren erişilen kayıtları soğuk, düşük enerjili depolamaya taşıyan veri saklama ilkeleri belirler ve yüksek oranda yenilenebilir elektrikle çalışan bulut bölgeleri seçer. Başlıca hizmetlerinin karbon yoğunluğunu ölçer ve kamusal hesap verebilirlik için verimlilik ve emisyon metriklerini yayımlar. Verimli varsayılanlar ve self servis panolar, onlarca teslimat takımının merkezi darboğazlar olmadan sürdürülebilir seçimler yapmasını sağlar.

## İş gerekçesi: motivasyonlar, YG ve TSM

Buradaki getiri alışılmadık ölçüde doğrudandır. FinOps iyileştirmesi, disiplinli çabayla bulut harcamasını yaygın olarak beşte bir ile üçte bir arasında azaltır; bu, doğrudan kâra ya da yeni işlerin finansmanına akan bir tasarruftur. Karbon azaltımı da giderek finansal değer taşır: kaçınılan karbon fiyatlaması, sürdürülebilirlik gereksinimi olan sözleşmelere uygunluk ve azalan düzenleyici ve itibar riski yoluyla. Verimlilik maliyeti ve karbonu aynı anda düşürdüğü için, görünürlük ve doğru boyutlandırmaya yapılan tek bir yatırım her iki boyutta da geri öder.

Toplam sahip olma maliyeti benimseme maliyetini de saymalıdır: maliyet ve karbon görünürlüğü için araçlar, pratiği yürütecek FinOps ya da platform kadrosu ve doğru boyutlandırma ile yeniden mimarilendirme için mühendislik zamanı. Bunlar tasarruflara kıyasla mütevazıdır ve verimli varsayılanlar yerleştikçe küçülür. Benimsememenin maliyeti sessizce birikir: işten daha hızlı büyüyen kontrolsüz bulut faturaları, kimse sahiplenmediği için asla yüzeye çıkmayan israf ve sürdürülebilirlik üzerinde artan düzenleyici, yatırımcı ve itibar maruziyeti. Liderliğe gerekçeyi sunmak için mevcut harcamayı ve büyüme eğrisini, tahmini israfı ve FinOps benimsemesinden elde edilen kıyaslama tasarruflarını gösterin. Sonra bunu emisyon azaltımı ve uyum değeriyle eşleştirin. Maliyeti ve sürdürülebilirliği, iki mercekten bakılan aynı verimlilik girişimi olarak çerçeveleyin; böylece işletmenin para tasarrufu ile karbon azaltımı arasında seçim yapması gerekmez.

## Anti-kalıplar ve tuzaklar

- **Maliyet atfı yok.** Etiketsiz, tahsis edilmemiş harcama, israfın sahibi olmadığı ve kimsenin onu iyileştiremeyeceği anlamına gelir.
- **Ayarla ve unut kaynak sağlama.** Kaynakları bir kez boyutlandırıp bir daha gözden geçirmemek, gereğinden fazla kaynak ayırmaya doğru kaymayı garanti eder.
- **Yalnızca finansın FinOps'u.** Maliyeti mühendislik sinyali yerine arka ofis meselesi olarak ele almak başarısız olur, çünkü harcamayı yönlendiren kararları mühendisler verir.
- **[Yeşil badana](https://en.wikipedia.org/wiki/Greenwashing).** Ölçüm olmadan sürdürülebilirlik iddia etmek düzenleyici ve itibar tepkisini davet eder.
- **Güvenilirlik pahasına verimlilik.** O kadar agresif kesmek ki hizmetler yük altında çöker, küçük bir tasarrufu büyük bir olayla takas eder.
- **Bünyedeki karbonu görmezden gelmek.** Boştaki donanımı gereğinden fazla ayırırken yalnızca çalışma enerjisine odaklanmak üretim ayak izini kaçırır.
- **Bürokratik kapılar.** Harcama için ağır onay süreçleri teslimatı yavaşlatır ve takımları yönetişimi atlatmaya iter.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Bulut maliyetleri aylık faturada bir sürprizdir. Etiketleme, tahsis ya da karbon farkındalığı yoktur; kaynak sağlama cömerttir ve nadiren yeniden gözden geçirilir. İsrafı kimse sahiplenmediği için görünmezdir ve yapılan her temizlik bir pratik değil, fatura şokuna verilen bir tepkidir.

**Düzey 2, Geliştirme.** Temel maliyet görünürlüğü ve etiketleme vardır; bir miktar doğru boyutlandırma ve boşta kaynak temizliği yapılır, ancak kapsam ve titizlik takımlar arasında büyük farklılık gösterir. Birkaç grup harcamasını izler ve düşük karbonlu bölgeleri dener; diğerleri ikisini de yapmaz. Sürdürülebilirlik kabul edilir ama ölçülmez ve iyi alışkanlıklar ortak bir beklentiye değil, bireysel girişime bağlıdır.

**Düzey 3, Standartlaştırma.** Bir FinOps pratiği belgelenmiş ve kurum genelinde uygulanmıştır: etiketleme zorunludur, ortak maliyetler üzerinde anlaşılmış bir yöntemle tahsis edilir ve bütçeler, tahminler ve anomali uyarıları standarttır. Taahhüt indirimleri ve doğru boyutlandırma tanımlı bir oyun kitabını izler; karbon, başlıca hizmetler için Yazılım Karbon Yoğunluğu belirtimi gibi tanınmış bir yöntemle ölçülür ve bölge ile zamanlama seçimleri vaka vaka değil tutarlı biçimde düşünülür.

**Düzey 4, Yönetme.** Maliyet ve karbon taban çizgilerine karşı ölçülür ve kontrol edilir. Takımlar birim ekonomisini (istek, müşteri ya da dosya başına maliyet ve karbon), boşta ve bünyedeki karbon tahminlerini içeren kullanımı, taban yüke karşı taahhüt kapsamını ve tahmin doğruluğunu izler; hepsi kurumsal hedeflere karşı raporlanır. Anomaliler soruşturmayı tetikler, verimlilik ve SLO'ya uyum birlikte incelenir; böylece iyileştirme güvenilirliği sessizce aşındırmaz ve kaynak sağlamaya dair uygula ya da uygulama kararları sezgiye değil bu veriye dayanır.

**Düzey 5, Orkestrasyon.** Maliyet ve karbon, günlük pratiğe bağlanmış sürekli, sahiplenilmiş mühendislik sinyalleridir. Verimli varsayılanlar, otomatik doğru boyutlandırma ve karbon farkındalıklı zamanlama olağandır; kurum talep, fiyatlar ve şebeke yoğunluğu değiştikçe varlığını sürekli yeniden dengeler. Maliyet, performans ve güvenilirlik SLO'lar aracılığıyla bilinçli olarak ödünleştirilir, sürdürülebilirlik metrikleri denetlenebilir yöntemlerle kamu ve yatırımcı raporlamasını besler ve pratik; iş, pazar ve düzenleme geliştikçe uyum sağlar.

## Tartışma fikirleri

- Kurumunuzda bulut maliyetinin sahibi kim olmalı: finans, merkezi bir FinOps takımı ya da kaynakları sağlayan mühendislik takımları?
- Ortak platform maliyetlerini onları tüketen birçok takım arasında nasıl adil paylaştırırsınız?
- Maliyet tasarrufları ile bunları elde etmek için feda edebileceğiniz güvenilirlik ya da performans arasındaki doğru denge nerede?
- Hizmetlerinizin karbon ayak izini nasıl ölçerdiniz ve eldeki verilere ne kadar güvenirsiniz?
- İş yüklerinizden hangileri zaman ya da bölge açısından karbon farkındalıklı zamanlama için yeterince esnek?
- Takımları riskli yetersiz kaynak ayırmaya teşvik etmeden motive eden verimlilik ve sürdürülebilirlik hedeflerini nasıl belirlersiniz?

## Önemli çıkarımlar

- Bulut, maliyeti ve karbonu mühendislik meselesi yaptı; görünürlük ve sahiplik, ikisini de kontrol etmenin temelidir.
- FinOps üç aşamada işler: bilgilendir (görünürlük), iyileştir (doğru boyutlandır ve indirim al) ve işlet (pratiğe yerleştir).
- Verimli yazılım çoğu zaman parayı ve karbonu birlikte tasarruf ettirir; bu yüzden ikisini iki mercekli tek bir girişim olarak ele alın.
- Karbonu enerji verimliliği, daha yüksek donanım kullanımı ve zamanda ve mekânda karbon farkındalıklı zamanlama yoluyla azaltın.
- Mimari ve doğru boyutlandırma uzun vadeli maliyeti ve karbonu belirler; esneklik ve sıfıra ölçekleme için tasarlayın.
- Maliyet, performans ve güvenilirliği SLO'larla bilinçli dengeleyin ve kapılarla değil korkuluklarla yönetin.

## Kaynaklar ve ileri okuma

- J.R. Storment, Mike Fuller, *Cloud FinOps: Collaborative, Real-Time Cloud Financial Management*
- FinOps Foundation, *FinOps Framework* documentation
- Green Software Foundation, *Principles of Green Software Engineering* and *Software Carbon Intensity (SCI) Specification*
- Anne Currie, Sarah Hsu, Sara Bergman, *Building Green Software*
- Adrian Cockcroft, writings on cloud efficiency and sustainability
- The Shift Project, *Lean ICT: Towards Digital Sobriety*
