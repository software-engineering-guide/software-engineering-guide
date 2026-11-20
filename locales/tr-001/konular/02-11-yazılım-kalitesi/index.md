# 2.11 Yazılım kalitesi

## Genel bakış ve motivasyon

[Yazılım kalitesi](https://en.wikipedia.org/wiki/Software_quality), bir sistemin belirtilen ihtiyaçları ve makul beklentileri ne kadar iyi karşıladığıdır. Bu, çalışıp çalışmadığından fazlası demektir: sistemin güvenilir, güvenli, sürdürülebilir, kullanılabilir, performanslı ve zaman içinde amacına uygun olup olmadığı demektir. Kalite testten daha geniştir. Test (bölüm 2.4) kusurları ortaya çıkaran bir etkinliktir. Kalite, doğru şeyi iyi inşa etmenin ve bunu kanıtla yaptığınızı bilmenin bütün disiplinidir. Bir sistem her testi geçip yine de sürdürülemez, erişilemez ya da kullanıcıların gerçekte ihtiyaç duyduğuna kötü uyuyorsa düşük kaliteli olabilir.

Büyük bir takımda kalite tek bir kişinin kafasında ya da tek bir takımın alışkanlıklarında yaşayamaz. Yüzlerce mühendis, birden çok ürün ve uzun ömürlü sistemler, paylaşılan bir kalite tanımına, onu güvence altına alan açık süreçlere ve daha iyiye mi yoksa daha kötüye mi gittiğini söyleyen ölçümlere ihtiyaç duyar. Bu olmadan "kalite" bir son tarihe karşı her tartışmayı kaybeden belirsiz bir özleme dönüşür ve değişim yavaş ve riskli olana kadar kusurlar birikir.

Kurumsal ve kamu ortamlarında bahisler yükselir. Düzenlemeye tabi, güvenlik açısından kritik ve vatandaşa dönük sistemler kaliteyi yalnızca iddia etmek değil, göstermek zorundadır: belgelenmiş süreçler, izlenebilir kanıt ve bağımsız doğrulama çoğu zaman zorunludur. Kötü kalite doğrudan mali, yasal ve itibar maliyeti taşır ve bazı alanlarda insanları tehlikeye atar. Modellerden, süreçlerden, ölçümden ve kültürden inşa edilen bilinçli bir kalite disiplini, kaliteyi bir kazadan yönetilen bir sonuca çevirir.

## Temel ilkeler

- Kalite amaca uygunluk artı gereksinimlere uyumdur; ikisini de açıkça tanımlayın.
- Kalite içine kurulur, testle sokulmaz; doğrulama kusurları bulur, ama önleme onlardan kaçınır.
- [Kalite güvencesini](https://en.wikipedia.org/wiki/Quality_assurance) (süreçlerimiz sağlam mı?) [kalite kontrolünden](https://en.wikipedia.org/wiki/Quality_control) (bu ürün iyi mi?) ayırın.
- Doğrulama "doğru inşa ettik mi?" diye sorar; geçerleme "doğru şeyi inşa ettik mi?" diye sorar.
- Kaliteyi küçük bir anlamlı metrik kümesiyle ölçün; metrikleri hedef değil sinyal olarak ele alın.
- Bir kusurun maliyeti ne kadar geç bulunursa o kadar artar; bu yüzden kalite etkinliklerini öne çekin.
- Kalite bütün kuruluşun ve kültürünün bir özelliğidir, sonda bir kapı değil.

## Öneriler

### ISO/IEC 25010 gibi paylaşılan bir kalite modeli benimseyin

Tanınmış bir ürün kalitesi modeli benimseyerek kuruluşunuza kalite için ortak bir sözcük dağarcığı verin. [ISO/IEC 25010](https://en.wikipedia.org/wiki/ISO/IEC_25010) işlevsel uygunluk, performans verimliliği, uyumluluk, kullanılabilirlik, güvenilirlik, güvenlik, sürdürülebilirlik ve taşınabilirlik gibi özellikleri tanımlar. Kaliteyi somutlaştırmak için kullanın: her sistem için hangi özelliklerin en çok önemli olduğuna ve her biri için "yeterince iyi"nin ne demek olduğuna karar verin. Bu ürün kalitesi özellikleri, mimariyi yönlendiren aynı **kalite nitelikleridir** (bölüm 3.1). Kalite ve mimari tek bir kaygının iki görünümüdür; bu yüzden onların iki rakip liste yerine tek öncelik listesini paylaşmasına izin verin.

### Kalite güvencesini kalite kontrolünden ayırın

Kalite güvencesini (KG) ve kalite kontrolünü (KK) ayrı ama tamamlayıcı etkinlikler olarak ele alın. KG süreç odaklı ve önleyicidir: işin yapılış biçimini standartlar, incelemeler, bitti tanımları ve eğitimle iyileştirir; böylece kusurlar ilk etapta ortaya çıkmaya daha az eğilimli olur. KK ürün odaklı ve algılayıcıdır: girmiş kusurları yakalamak için test, [kod incelemesi](https://en.wikipedia.org/wiki/Code_review) ve denetimler gibi gerçek iş ürünlerini inceler. Olgun bir kuruluş ikisine de yatırım yapar ama KG'ye yönelir, çünkü kusurları önlemek onları bulup düzeltmekten ucuzdur.

### Açık yazılım kalite yönetimi süreçleri yürütün

Kaliteyi sessiz bir umut değil, yönetilen bir süreç yapın. Önemli iş için hedef kalite özelliklerini, güvence ve kontrol etkinliklerini, kabul ölçütlerini ve kimin sorumlu olduğunu belirten bir kalite planı yazın. Onu zaten sahip olduğunuz uygulamalara örün: hem kontrol hem bilgi paylaşma yolu olarak kod incelemesi (bölüm 2.5), otomatik güvenlik ağı olarak test stratejisi (bölüm 2.4) ve sürekli denetim olarak [statik analiz](https://en.wikipedia.org/wiki/Static_program_analysis). Yalnızca olaylara tepki vermek yerine kalite verisini düzenli gözden geçirin ve eğilimlere göre harekete geçin.

### Doğrulama ve geçerlemeyi ayrı disiplinler olarak uygulayın

Doğrulama, iş ürünlerinin belirtimlerini karşıladığını, yani her aşamaya doğru girdilerin doğru çıktılar ürettiğini, incelemeler, statik analiz ve gereksinimlere karşı test yoluyla teyit eder. Geçerleme, bitmiş sistemin gerçekten kullanıcı ihtiyaçlarını ve amaçlanan kullanımı karşıladığını kullanıcı testi, kabul testi, pilotlar ve saha geri bildirimi yoluyla teyit eder. İkisine de ihtiyacınız var. Bir sistem kusurlu bir belirtime karşı doğru olabilir (doğrulanmış ama geçerli değil) ya da gerçek bir ihtiyacı karşılarken yine de kusur içerebilir (geçerli ama doğrulanmamış). Düzenlemeye tabi ortamlarda geliştiricilerden ayrı bir tarafça yapılan bağımsız [doğrulama ve geçerleme](https://en.wikipedia.org/wiki/Verification_and_validation) (BD&G) gerekebilir.

### Kaliteyi anlamlı metriklerle ölçün

Kalite sonuçlarını ve itici güçlerini yansıtan küçük bir metrik kümesi seçin ve onları zaman içinde izleyin. Yararlı ölçüler arasında kusur yoğunluğu, kusur kaçış oranı (üretimde bulunan kusurlara karşı sürümden önce bulunanlar), algılama ve onarım için ortalama süre, değişim başarısızlık oranı, karmaşıklık ve tekrar gibi kod sağlığı sinyalleri ve kullanıcı bildirimli sorunlar ve erişilebilirlik uyumu gibi geçerleme sinyalleri bulunur. Boş gösteriş ve oyunlaştırılabilir metriklerden uzak durun: hedef haline gelen bir metrik gerçekliği ölçmeyi bırakır. Sayıları incelemelerden ve kullanıcı geri bildiriminden gelen nitel sinyallerle eşleştirin.

### Kusurları sistematik karakterize edin ve yönetin

Kusurları yalnızca söndürülecek yangınlar değil, veri olarak ele alın. Onları ciddiyete, türe ve kök nedene göre sınıflandırın. Keşiften çözüme kadar izleyin. Tekrarı önlemek için kalıpları arayın. Tek seferlik hataları sistemik zayıflıklardan ayırmak için [kök neden analizi](https://en.wikipedia.org/wiki/Root_cause_analysis) ve kusur kategorilendirme gibi teknikleri kullanın. Öğrendiklerinizi güncellenmiş standartlar, eklenen testler ve iyileştirilmiş incelemeler yoluyla KG'ye geri besleyin; böylece aynı kusur sınıfı geri gelmez. Nedeni anlaşılmadan düzeltilen bir kusur, geri davet ettiğiniz bir kusurdur.

### Kalite maliyetini bilinçli yönetin

Kalite ekonomisini klasik kategorilerle anlayın: önleme maliyetleri (eğitim, standartlar, iyi tasarım, araçlar), değerlendirme maliyetleri (incelemeler, test, denetimler) ve başarısızlık maliyetleri (sürümden önce iç yeniden iş, artı kullanıcıların bulduğu, çok daha pahalıya mal olan dış başarısızlıklar). Yatırımınızı önlemeye ve erken değerlendirmeye kaydırın, çünkü orada harcanan her dolar sonradan birçok dolarlık başarısızlık maliyetinden kaçınır. Bu maliyetleri görünür kılın; böylece "kaliteye vaktimiz yok" olduğu şey olarak görülür: başarısızlığa daha çok harcamayı seçmek.

### Bir kalite kültürü kurun

Kaliteyi herkesin sorumluluğu yapın; sonda inceleyen bir akış aşağısı KG departmanına devredilmek yerine yazılımı inşa eden takımlara ait olsun. Liderler kalite sonuçlarını ödüllendirmeli, kusurları ve ucuz atlatmaları bildirmeyi güvenli kılmalı ve kalite verisini sopa değil öğrenme aracı olarak ele almalıdır. Kusurlara suçlamasız bir yaklaşım sorunları erken açığa çıkarır. Suçlayıcı bir yaklaşım onları pahalı olana kadar gizler.

## Ödünleşimler: artılar ve eksiler

| Uygulama / seçim | Artılar | Eksiler |
|---|---|---|
| Resmi kalite modeli (ISO 25010) | Paylaşılan sözcük dağarcığı; açık öncelikler | Dogmatik uygulanırsa yük |
| Ağır kalite güvencesi (önleme) | Daha az kusur; daha düşük toplam maliyet | Baştan yatırım; karşılığını göstermesi daha yavaş |
| Ağır kalite kontrolü (denetim) | Sızan kusurları yakalar | Pahalı; kusurları geç bulur |
| Bağımsız BD&G | Yüksek güvence; nesnel | Maliyetli; daha yavaş; husumetli hissettirebilir |
| Zengin kalite metrikleri | Görünürlük; erken uyarı | Oyunlaştırma riski; ölçüm yükü |
| Özel KG takımı | Odak ve uzmanlık | Sorumluluğu geliştiricilerden devralabilir |
| Takımlara ait kalite | Sahiplik; hızlı geri bildirim | Her yerde disiplin ve beceri gerektirir |

Merkezi ödünleşim, zamanlamayla biçimlenen yatırım ile güvence arasındadır. Önleme, sonradan daha büyük başarısızlık maliyetlerinden kaçınmak için şimdi para harcar. Bu yüzden ekonomik olarak doğru kalite düzeyi azami değildir; daha fazla güvencenin marjinal maliyetinin kaçındığı başarısızlık maliyetine eşit olduğu noktadır. O nokta güvenlik açısından kritik sistemlerde yüksek, düşük riskli dahili araçlarda daha düşük durur. Diğer yinelenen gerilim sahipliktir. Merkezi KG grupları uzmanlık kurar ama geliştiricilerin sorumluluğu devretmesine izin verebilir. Takımlara ait kalite sahiplik kurar ama her yerde beceri ve disiplin talep eder.

## Takımınızla tartışılacak sorular

1. **Aynı sınıftan bir kusur iki kez ortaya çıktığında kök neden analizi mi yapıyoruz, yoksa sadece yeniden mi düzeltiyoruz?** Nedeni anlaşılmadan düzeltilen bir kusur geri davet ettiğiniz bir kusurdur ve büyük bir takımda aynı kök neden, kimse noktaları birleştirmeden önce birçok hizmet boyunca ortaya çıkabilir. Kusurları veri olarak ele almak (ciddiyete, türe ve nedene göre sınıflandırılmış, sonra kalıplar için taranmış) giderek daha güvenilir hale gelen takımı, aynı hatayı yeniden düzeltmekle meşgul kalandan ayıran şeydir. Toplantıya kusur izleyicinizi getirin ve yinelenen imzalara bakın: yakın tarihli kaç olay, sistemik olarak hiç ele almadığınız bir neden paylaşıyor? Cevap önlemeyi beslemelidir; böylece yinelenen bir neden güncellenmiş bir standardı, yeni bir paylaşılan yardımcıyı, eklenen bir testi ya da daha iyi bir inceleme kontrol listesini yönlendirir, çünkü bir yerdeki bir düzeltmenin tüm sınıfın geri dönmesini durdurması böyle olur.

2. **Takımımızda bir kusuru ya da ucuz atlatmayı bildirmek güvenli mi ve bir tane dile getiren kişiye ne oluyor?** Kalite kültürün bir özelliğidir ve suçlamasız bir yaklaşım sorunları erken açığa çıkarırken suçlayıcı olan onları pahalı olana kadar gizler; bu, düzenlemeye tabi ya da vatandaşa dönük bir sistemde kamusal bir başarısızlık ya da bir ceza demek olabilir. Bu en çok ölçekte önemlidir; çünkü bir riske en yakın mühendis çoğu zaman kıdemsizdir ve sessiz kalma teşviki güçlüdür. Dürüst sinyalleri getirin: ucuz atlatmalar günlüğe alınıp tartışılıyor mu, yoksa kayboluyor mu? Ölü sonrası değerlendirmeler nedenleri mi, kişileri mi adlandırıyor? Eylem, kalite verisini sopa değil öğrenme aracı yapmak, sorunları ortaya çıkaranları ödüllendirmek ve suçlamasız ölü sonrası değerlendirmeler yürütmektir, çünkü takımınızın bildirmekten korktuğu şeyi önleyemezsiniz.

3. **Geçerleme bir sürümü gerçekten durdurabilir mi ve bir son tarih yaklaşırken bu yetki kimde?** Doğrulama (doğru inşa ettik mi?) ve geçerleme (doğru şeyi inşa ettik mi?) ayrı disiplinlerdir ve geçerlemenin dişi ancak başarısız bir erişilebilirlik kontrolü, başarısız bir kabul testi ya da ağır bir kullanıcı araştırması gerçekten yayımlamayı engelleyebiliyorsa vardır. Kurumsal ve kamu ortamlarında bu çoğu zaman zorunludur, bazen geliştiricilerden ayrı bir tarafın bağımsız doğrulama ve geçerlemesiyle ve "yine de yayımladık" bir gözetim organının kabul ettiği bir cevap değildir. Son birkaç sürümünüzü getirin: herhangi bir kalite sinyali hiç gerçekten birini durdurdu mu, yoksa kapı her zaman tarihe mi boyun eğiyor? Geçerleme hiç bir sürümü engellemediyse süstür ve çözüm kabul ölçütlerini baştan kalite planına yazmak, ilerle ya da dur kararının sahibini adlandırmak ve o karara teslimat baskısından bağımsız gerçek yetki vermektir.

4. **Kötü kalitenin maliyetini gerçekten biliyor muyuz ve harcamayı başarısızlıktan önlemeye bilinçli kaydırıyor muyuz?** Kötü kalite maliyeti (KKM), iç yeniden işe, üretim olaylarına, acil düzeltmelere, destek yüküne, kaybedilen kullanıcılara ve cezalara giden paradır ve neredeyse her zaman incelemeler ve teste yapılan görünür harcamadan büyüktür. Büyük bir takımda başarısızlık maliyetleri olay kanallarına, destek kuyruklarına ve kimsenin yeniden iş olarak günlüğe almadığı yeniden işe dağılır; bu yüzden biri onları toplayana kadar görünmez kalırlar. Gerilim, önlemenin şimdi, bir bütçe döngüsünde para harcaması, sonra ve başkasının bütçesine düşecek başarısızlık maliyetlerinden kaçınmak için olmasıdır; bu da takası sonsuza dek ertelemeyi kolaylaştırır. Gerçek rakamları getirin: olay sayısı ve maliyeti, yeniden iş saatleri, kaçan kusur oranı ve harcamanın önleme, değerlendirme ve başarısızlık arasındaki mevcut dağılımı, sonra karışımın daha erken kayması gerekip gerekmediğine karar verin. Yaşam boyu maliyetin çoğunun ilk sürümden sonra düştüğü kurumsal ve kamu sistemleri için KKM'yi bütçeyi elinde tutanların önüne koyun, çünkü bir gözetim organının görebileceği bir sayıyı takas etmek, belirsiz bir "kalite" çağrısını takas etmekten çok daha zordur.

5. **Kalite metriklerimizden hangileri sessizce hedefe dönüştü ve şimdi hangi davranışı yönlendiriyor?** Hedef haline gelen bir metrik gerçekliği ölçmeyi bırakır: bir kapsam yüzdesinin peşinden koşun ve kusur yakalayan değil sayıyı oynatan testler elde edersiniz. Ölçekte bu tehlikelidir, çünkü onlarca takım arasında paylaşılan bir başlık panosu hepsi için teşvikleri belirler ve oyunlaştırılabilir bir metrik oyunlaştırmayı aynı anda her yere yayar. Karşıt değerlendirme, hâlâ ölçüme ihtiyacınız olmasıdır; bu yüzden cevap nadiren "metriği bırak"tır, "onu bir karşı sinyalle eşleştir ve incelemelerden ve kullanıcılardan gelen nitel kanıtla birlikte oku"dur. Mevcut metrik kümenizi getirin ve her biri için baskı altındaki birinin kaliteyi iyileştirmeden onu oynatmak için ne yapabileceğini ve bunun olduğunu görüp görmediğinizi sorun. Düzenlemeye tabi ve vatandaşa dönük ortamlarda, altta yatan geçerleme (erişilebilirlik, gerçek kullanıcı sonuçları) hiç gerçekten uygulanmamışken yeşil görünen uyum metriklerine özellikle dikkat edin, çünkü bir denetçi eninde sonunda sayının ardındaki gerçekliği test edecektir.

6. **Kaliteye burada kim sahip: kodu yazan takımlar mı, sonda ayrı bir grup mu ve gerçekte hangisini kaynaklandırıyoruz?** Sahiplik akış aşağısındaki her şeyi biçimlendirir, çünkü akış aşağısı bir KG silosu geliştiricilerin yazdıkları kodun sorumluluğunu devretmesine izin verirken, takımlara ait kalite her takımda beceri ve disiplin talep etme bedeliyle sahiplik kurar. Büyük bir takımda bu ya-ya-da değildir: sürdürülebilir kalıp genellikle kaliteye kod incelemesi ve otomatik testlerle sahip olan takımlar, desteği de standartları sürdüren, kalite güvencesini süreç iyileştirmesi olarak yürüten ve kaliteyi sonda denetlemek yerine koçluk yapan küçük bir merkezi gruptan alırlar. Kalite işinin şu anda nerede gerçekleştiğinin, bir kusur kaçtığında kimin sorumlu olduğunun ve bütçe ve kadronun gerçekte nerede durduğunun, söylemin kalitenin yaşadığını söylediği yere karşı dürüst bir haritasını getirin. Kurumsal ve kamu kuruluşları için bağımsız doğrulama ve geçerleme gereksinimini ekleyin: bazı güvence rejimleri ayrı bir taraf zorunlu kılar; bu yüzden hangi kontrollerin teslimat takımlarına ait olduğuna ve hangilerinin denetimi karşılamak için bağımsız kalması gerektiğine bilinçli karar verin.

## Sektör merceği

**Girişim.** Hız töreni yener; bu yüzden ürününüzü gerçekten koruyan iki üç kalite özelliğini, genellikle güvenilirlik ve sürdürülebilirliği adlandırın ve cilanın beklemesine izin verin. Kadrolayamayacağınız ayrı bir KG grubu kurmak yerine kaliteyi tüm takım genelinde kod incelemesi ve mütevazı bir otomatik test takımıyla sahiplenin. Aynı sınıftan bir hata iki kez göründüğünde kök nedene yirmi dakika harcayın ve bir paylaşılan yardımcı ile bir test ekleyin; böylece hızlı hareket ederken önleme ucuz ve değişim başarısızlık oranınız düşük kalır.

**Küçük işletme.** Özel bir kalite uzmanı ve sıkı bir bütçe olmadan, çalıştırmanız gereken bir süreç yerine satın aldığınız araçlara ve platformlara yerleşik kaliteye yaslanın. Yazılım seçtiğinizde satıcının kalite kanıtını satın almanın parçası olarak ele alın: güvenlik duruşu, erişilebilirlik, destek duyarlılığı ve sürümlerinin ne sıklıkla bozulduğu. Sürdürecek kimsenizin olmadığı ayrıntılı bir metrik programı yerine ucuz, dürüst birkaç sinyali (üretim olayları, müşteri bildirimli sorunlar, düzeltme süresi) izleyin.

**Kurumsal.** İş birçok takım boyunca tutarlılıktır: ISO/IEC 25010 gibi paylaşılan bir kalite modeli benimseyin, kalite güvencesini (süreç) kalite kontrolünden (ürün) ayırın ve harcamayı önlemeye kaydıran kalite maliyeti incelemeleri yürütün. Kaliteyi teslimat takımlarına ait tutun; standartları ve kusur kaçış oranı, değişim başarısızlık oranı ve kod sağlığı eğilimleri panolarını sürdüren küçük bir merkezi grupla destekleyin. Sözcük dağarcığını ve kapıları standartlaştırın ki gruplar kalite uygulamasını yeniden icat etmeyi bıraksın, takımlara o çıtaları kendi yollarıyla karşılamaları için yer bırakın.

**Kamu.** Tedarik, şeffaflık ve kamusal hesap verebilirlik çerçeveyi belirler; bu yüzden kalite gereksinimlerini sözleşmelere yazın ve iddia yerine belgelenmiş, izlenebilir kalite kanıtı isteyin. Geliştiricilerden ayrı bir tarafça bağımsız doğrulama ve geçerleme, zorunlu erişilebilirlik uyumu ve denetim izinin parçası olarak tutulan ciddiyet ve kök nedenli kusur kayıtları bekleyin. Kötü kalite maliyeti rakamlarını (yeniden iş, itirazlar, hizmet başarısızlıkları) gözetim organlarına raporlayın ve geçerlemeye, kendisine bağımlı vatandaşları başarısız kılacak bir sürümü engellemek için gerçek yetki verin.

## Örnekler

**Girişim.** Beş kişilik bir girişim, erken ürünü için önemli olan kalite özelliklerinin güvenilirlik ve sürdürülebilirlik olduğuna karar verir ve piksel mükemmel cilanın beklemesine izin verir. Kaliteye tüm takım sahiptir: kod incelemesi ve mütevazı bir otomatik test takımı kontrollerdir ve kusurları devredecek ayrı bir KG grubu yoktur. Aynı sınıftan bir hata iki kez göründüğünde hızlı bir kök neden bakışına yirmi dakika harcarlar ve bir paylaşılan yardımcı ile bir test eklerler; böylece her seferinde elle yeniden düzeltilmek yerine tekrarlamayı durdurur. O küçük önleme alışkanlığı, hâlâ hızlı hareket ederlerken değişim başarısızlık oranlarını düşük tutar.

**Kurumsal.** Büyük bir finansal hizmetler firması ISO/IEC 25010'u kalite sözcük dağarcığı olarak benimser ve her ürün için güvenilirlik, güvenlik ve sürdürülebilirlik için hedef düzeyleri kaydeder. Takımlar kaliteye sahiptir: kod incelemesi ve otomatik testler hattaki kontrollerdir; küçük bir merkezi grup ise standartları sürdürerek ve koçluk yaparak KG yürütür. Bir kalite panosu kusur kaçış oranını, değişim başarısızlık oranını ve kod sağlığı eğilimlerini izler. Kusurlar sınıflandırılır ve kök nedenlendirilir ve yinelenen nedenler paylaşılan kütüphanelerin ve kontrol listelerinin güncellenmesini yönlendirir. Liderlik kalite maliyeti verisini üç ayda bir gözden geçirir ve harcamayı önlemeye kaydırmıştır; bu hem üretim olaylarını hem onları düzeltme maliyetini düşürmüştür.

**Kamu.** Vatandaşa dönük bir yardım platformu sunan ulusal bir kurum, belgelenmiş kalite kanıtı gerektiren bir güvence rejimi altında çalışır. Her sürüm için bir kalite planıyla resmi bir kalite yönetimi süreci yürütür, ayrıca geliştiricilerden ayrı bir takımın bağımsız doğrulama ve geçerlemesini. Doğrulama her iş ürününü politikaya izlenen gereksinimlere karşı kontrol eder. Geçerleme, erişilebilirlik uyum testini ve gerçek vatandaşlarla kullanıcı araştırmasını içerir ve ikisi de bir sürümü engelleyebilir. Kusurlar denetim izinin parçası olarak ciddiyet ve kök nedenle izlenir ve kötü kalite maliyeti rakamları (yeniden iş, itirazlar ve hizmet başarısızlıkları) önlemeye sürekli yatırımı haklı çıkarmak için gözetim organlarına gider.

## İş gerekçesi: motivasyonlar, YG ve TSM

Kalitenin getirisi daha düşük toplam sahip olma maliyeti ve istikrarlı teslimat hızıdır. Kalitenin maliyetinin iki yüzü vardır. İyi harcama, önleme ve değerlendirme, görünür ve kontrol edilebilirdir: tasarım, standartlar, incelemeler, test ve araçlar. Kötü kalite maliyeti (KKM) daha büyüktür ama çoğu zaman gizlidir: iç yeniden iş, üretim olayları, acil düzeltmeler, müşteri desteği, kaybedilen kullanıcılar, düzenleyici cezalar ve itibar hasarı. Crosby'nin "Quality Is Free" eserine kadar uzanan çalışmalar, kötü kalitenin toplam maliyetinin onu önlemenin maliyetini gölgede bıraktığını ve kusurların ne kadar geç yakalarsanız o kadar daha pahalı hale geldiğini tutarlı biçimde bulmuştur: tasarımda bulunan bir sorun, aynı sorunun üretimde bulunmasının bir kesrine mal olur.

Liderlik için argüman "kaliteye daha çok harca" değildir. "Genel olarak daha az harcamak için daha erken harca"dır. KKM'yi kendi verilerinizden (olay sayısı ve maliyeti, yeniden iş saatleri, kaçan kusur oranı) nicelleştirin ve önleme ve erken değerlendirmenin onu nasıl düşürdüğünü gösterin. Kaliteyi iş sonuçlarına bağlayın: güvenilirlik müşterileri elde tutar, sürdürülebilirlik gelecekteki değişimi ucuz tutar ve güvenlik ile erişilebilirlik sizi hukuki belalardan uzak tutar. Maliyetin çoğunun ilk sürümden sonra düştüğü uzun ömürlü kurumsal ve kamu sistemlerinde, kalitenin sürdürülebilirlik ve güvenilirlik boyutları yaşam boyu maliyete hâkimdir. Bu, erken kalite yatırımını verebileceğiniz en yüksek kaldıraçlı kararlardan biri yapar.

## Anti-kalıplar ve tuzaklar

- **Son kapı olarak kalite:** kaliteyi içine kurmak yerine sonda denetlemek; kusurlar en pahalı oldukları anda bulunur.
- **Testi kaliteyle karıştırmak:** geçen testlerin yüksek kalite anlamına geldiğini varsaymak; sürdürülebilirliği, kullanılabilirliği ve amaca uygunluğu görmezden gelmek.
- **Ayrı silo olarak KG:** "kaliteye sahip olan" ve geliştiricilerin yazdıkları kodun sorumluluğunu devretmesine izin veren akış aşağısı bir takım.
- **Metrik tiyatrosu:** kapsam yüzdelerini ya da kusur sayılarını hedef olarak kovalamak; oyunlaştırmayı davet eder ve gerçek kaliteyi gizler.
- **Geçerlemesiz doğrulama:** belirtimi doğru inşa edip belirtimin gerçek ihtiyaçları karşıladığını hiç kontrol etmemek.
- **Kök neden analizi yok:** kusurları sistemik nedeni ele almadan tek tek düzeltmek; bu yüzden aynı sınıf tekrarlar.
- **Kötü kalite maliyetini görmezden gelmek:** başarısızlık maliyetleri gizli ve ölçülmemiş olduğu için kaliteyi saf maliyet olarak görmek.

## Olgunluk modeli

**Düzey 1 (Başlangıç).** Kalite tanımsız ve gelişigüzeldir. Bireysel titizliğe biner, çoğunlukla sonda elle testle kontrol edilir ve kusurlar ortaya çıktıkça reaktif ele alınır. Paylaşılan model, metrik ve güvence ile kontrol arasında çizgi yoktur.

**Düzey 2 (Geliştirme).** Temel uygulamalar ortaya çıkar: kod incelemesi, otomatik testler ve bir kusur izleyici. Bazı kalite verisi toplanır ama düzensiz ve her takım kendi yoluyla yapar. Kalite hâlâ çoğunlukla test olarak görülür, önleme asgaridir, doğrulama gerçekleşir ve geçerleme gayriresmidir.

**Düzey 3 (Standartlaştırma).** Kuruluş paylaşılan bir kalite modeli (ISO/IEC 25010 gibi) benimser, KG'yi KK'dan ayırır ve takımlar arasında belgelenmiş ve tutarlı uygulanan kalite planları ve kabul ölçütleriyle kalite yönetimi süreçleri yürütür. Doğrulama ve geçerleme ayrı ve bilinçlidir ve kusurlar üzerinde anlaşılmış bir şemaya göre sınıflandırılır ve kök nedenlendirilir.

**Düzey 4 (Yönetme).** Kalite temel çizgilere karşı ölçülür ve kontrol edilir. Küçük bir anlamlı metrik kümesi zaman içinde izlenir (kusur yoğunluğu, kusur kaçış oranı, algılama ve onarım için ortalama süre, değişim başarısızlık oranı ve karmaşıklık ve tekrar gibi kod sağlığı sinyalleri) ve kalite maliyeti önleme, değerlendirme ve başarısızlık boyunca nicelleştirilir. Kabul ve kalite kapıları görüşe değil kanıta dayanarak uygulanır, eğilimler sabit bir tempoyla gözden geçirilir ve geçerleme bir sürümü gerçekten engelleyebilir.

**Düzey 5 (Orkestrasyon).** Kalite, iş ve risk planlamasıyla bütünleşmiş, sürekli iyileştirilen, kültürel olarak sahiplenilen bir disiplindir. Vurgu önlemedir, kalite maliyeti verisi yatırımın nereye gideceğini yönlendirir ve kök neden bulguları tekrarı sistematik önler. Takımlar kaliteye uçtan uca sahiptir, metrikler sürekli iyileştirmeyi besler ve kuruluş ürünler, riskler ve düzenleme kaydıkça kalite uygulamasını uyarlar. Bu, bölüm 10.8'deki olgunluk modellerinin üst düzeyleriyle örtüşür.

## Tartışma fikirleri

- Sistemleriniz için hangi ISO/IEC 25010 kalite özellikleri en çok önemli ve her biri için "yeterince iyi" nedir?
- Kuruluşunuz önleme-değerlendirme-başarısızlık harcama karışımında nerede duruyor ve kaymalı mı?
- Pratikte doğrulamayı geçerlemeden ayırıyor musunuz, yoksa ikisini de "test"te mi topluyorsunuz?
- Kalite yazılımı inşa eden takımlara mı ait, yoksa ayrı bir gruba mı devredilmiş ve onu taşısanız ne değişirdi?
- Gerçek kötü kalite maliyetiniz nedir ve iş gerekçesini kurmak için onu yeterince iyi ölçebilir misiniz?
- Kalite metriklerinizden hangileri gerçek sinyal ve hangileri oyunlaştırılabilir hedeflere dönüştü?

## Önemli çıkarımlar

- Kalite testten daha geniştir: güvenilirlik, güvenlik ve sürdürülebilirlik gibi özellikler boyunca amaca uygunluk artı uyumdur.
- Kalite niteliklerini açık yapmak ve mimariyle (bölüm 3.1) hizalamak için paylaşılan bir kalite modeli (ISO/IEC 25010) kullanın.
- Kalite güvencesini (önle, süreç) kalite kontrolünden (algıla, ürün) ayırın ve önlemeye yönelin.
- Doğrulamayı (doğru inşa ettik) ve geçerlemeyi (doğru şeyi inşa ettik) ayrı disiplinler olarak uygulayın.
- Kaliteyi birkaç anlamlı metrikle ölçün ve tekrarı önlemek için kusurları ciddiyet ve kök nedenle karakterize edin.
- Kalite maliyetini yönetin: önleme ve erken değerlendirme, özellikle uzun ömürlü sistemlerde başarısızlıktan çok daha ucuzdur.
- Takımların kaliteye sahip olduğu, kod incelemesi (bölüm 2.5) ve test stratejisiyle (bölüm 2.4) desteklenen suçlamasız bir kalite kültürü kurun.

## Kaynaklar ve ileri okuma

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, Software Quality knowledge area.
- ISO/IEC 25010, *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): System and software quality models*.
- ISO/IEC 25000 series (SQuaRE), *Software product quality requirements and evaluation*.
- Philip B. Crosby, *Quality Is Free: The Art of Making Quality Certain*.
- W. Edwards Deming, *Out of the Crisis*.
- Capers Jones and Olivier Bonsignour, *The Economics of Software Quality*.
- Gerald Weinberg, *Quality Software Management*.
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (quality assurance and V&V process context).
