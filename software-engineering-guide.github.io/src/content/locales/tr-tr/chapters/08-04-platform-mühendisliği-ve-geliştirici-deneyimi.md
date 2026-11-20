# 8.4 Platform mühendisliği ve geliştirici deneyimi

## Genel bakış ve motivasyon

[Platform mühendisliği](https://en.wikipedia.org/wiki/Platform_engineering), diğer mühendislerin yazılımlarını geliştirmek, teslim etmek ve işletmek için kullandığı bir iç ürünü, yani bir iç geliştirici platformunu (IDP) inşa etme ve işletme disiplinidir. Her takımın kendi işlem hatlarını, altyapısını ve araçlarını sıfırdan bir araya getirmesi yerine, özel bir platform takımı iyi desteklenen "altın yollar" boyunca özenle seçilmiş, self servis yetenekler sunar. Altın yollar, makul varsayılanların içine gömüldüğü, görüşlü ve desteklenen güzergâhlardır. [Geliştirici deneyimi](https://en.wikipedia.org/wiki/Developer_experience) (DevEx) ise yakından ilişkili bir kaygıdır: kurumda mühendis olmanın nasıl hissettirdiği, bir geliştiricinin fikirden çalışan yazılıma ne kadar kolay ve hızlı ulaşabildiği ve yolda ne kadar sürtünme bulunduğu.

Büyük takımlar için bu önemlidir, çünkü [bilişsel yük](https://en.wikipedia.org/wiki/Cognitive_load) ve sürtünme zarif biçimde ölçeklenmez. Çok sayıda takımınız olduğunda, her mühendisin aynı anda yönetmesi gereken araç, sistem ve karar sayısı büyümeye devam eder. Çok geçmeden zamanlarının büyük bir bölümü değer üretmek yerine altyapı tesisatına ve koordinasyona gider. Platform olmayınca her takım aynı sorunları, yani sağlama, dağıtım, gözlemlenebilirlik ve uyumu, tutarsız biçimde ve tekrar tekrar çözer. İyi bir platform bu ortak karmaşıklığı üstlenir. Takımlar böylece kendi alanlarına odaklanabilir ve yine de kurumun güvenlik, güvenilirlik ve maliyet standartlarını devralır.

Kurumsal ve kamu açısından önemi yüksektir, çünkü bu kurumlar ölçeği sıkı yönetişimle birleştirir. Platform; uyum, güvenlik ve denetim gereksinimlerini bir kez, takımların varsayılan olarak izlediği döşenmiş yollar olarak kodlamak için doğal yerdir. Bu, her takımın politikayı kendi başına doğru yorumlayıp uygulamasını beklemekten çok daha iyidir. Yönetişimi bir sürtünme kaynağından standart iş akışının görünmez bir özelliğine dönüştürür; büyük ve düzenlemeye tabi kurumların kontrolü kaybetmeden hızlı hareket etmesi için tam olarak gereken budur.

## Temel ilkeler

- Platformu bir ürün olarak ele alın: kullanıcıları, bir yol haritası ve benimsenmeyi zorlamak yerine kazanma görevi olsun.
- Altın yollar sağlayın: doğru yolu kolay yol yapan, görüşlü ve iyi desteklenen güzergâhlar.
- Yetenekleri self servis yapın ki takımlar biletlerde ve insan devirlerinde beklemesin.
- Kapı dikmek yerine yol döşeyin; meşru işi engellemeden yönlendiren korkuluklar kurun.
- Uygulama geliştiricilerin bilişsel yükünü durmaksızın azaltın.
- Geliştirici deneyimini ve üretkenliği dengeli, çok boyutlu sinyallerle ölçün.
- Altın yolları isteğe bağlı ama takımların kendiliğinden seçeceği kadar iyi tutun.

## Öneriler

### Platformu bir ürün olarak inşa edin

En önemli tek değişim, platformu yukarıdan dayatılan zorunlu bir standart olarak değil, iç müşterilere hizmet eden bir ürün olarak görmektir. Pratikte bu; geliştirici ihtiyaçlarını araştırma ve geri bildirimle anlamak, bir yol haritası sürdürmek, benimsenmeyi ve memnuniyeti ölçmek ve deneyimin hesabını vermek demektir. Takımların kullanmaya zorlandığı ama onları yavaşlatan bir platforma içerlenir ve etrafından dolanılır. Takımları gerçekten hızlandıran bir platform ise itibarıyla yayılır. Kaliteyle kazanılan benimseme, platform başarısının en doğru ölçüsüdür.

### Altın yollar ve döşenmiş yollar sağlayın

Yaygın yolculuklar için altın yollar tanımlayın: yeni bir hizmet oluşturmak, dağıtmak, bir veritabanı eklemek, gözlemlenebilirliği bağlamak, uyum gereksinimlerini karşılamak. Altın yol, makul varsayılanların içine gömüldüğü, desteklenen, görüşlü ve uçtan uca bir güzergâhtır. Bu yollar boyunca korkuluklar yerleştirin; yani güvenlik taramasını, politika denetimlerini ve en iyi uygulamaları, böylece yolu izleyen bir takım otomatik olarak uyumlu ve güvenli olur. Amaç basittir: bir şeyi yapmanın en kolay yolu aynı zamanda doğru, güvenli ve uyumlu yolu da olmalıdır. Yolları isteğe bağlı tutun ki gerçekten sıradışı ihtiyaçları olan takımlar ayrılabilsin. Ama yolları, çoğu takımın hiç ayrılmak istemeyeceği kadar çekici yapın.

### Gerçek self servis altyapı sunun

Altyapıyı ve yetenekleri self servis arayüzlerle sunarak bilet-ve-bekle devirlerini ortadan kaldırın: bir portal, bir komut satırı aracı, bir API ya da şablonlu depolar. Bir geliştirici, talep açıp başka bir takımı günlerce beklemeden, dakikalar içinde uyumlu bir ortam sağlayabilmeli, bir şablondan yeni bir hizmet ayağa kaldırabilmeli ya da bir veritabanı isteyebilmelidir. Self servis, platformu bir darboğazdan bir hızlandırıcıya çeviren şeydir. Ve yalnızca altta yatan korkuluklar self servisi güvenli kıldığı için işler.

### Geliştirici portalları, hizmet kataloğları ve puan kartları sunun

Geliştirici portalı size tek bir bakış penceresi verir: tüm hizmetlerin sahipleri, belgeleri, bağımlılıkları ve sağlık durumuyla bir kataloğu. Hizmet katalogları sahipliği ve mimariyi keşfedilebilir kılar. Hiç kimsenin tüm sistemi kafasında tutamadığı ölçekte bu paha biçilmezdir. Puan kartları her hizmeti test kapsamı, güvenlik duruşu, nöbet hazırlığı ve belgeleme gibi standartlara göre ölçer ve takımlara nerede durduklarına ve neyi iyileştireceklerine dair net, nesnel bir resim verir. Bu araçlar birlikte mühendislerin bilgi aramaya harcadığı zamanı keser ve hesap verebilirliği netleştirir.

### Geliştirici deneyimini dengeli çerçevelerle ölçün

Tek sayılı üretkenlik ölçütlerine direnin. Kolayca oyuna getirilir ve yanıltıcıdır. Geliştirici deneyiminin gerçek dokusunu yakalamak için SPACE gibi çok boyutlu çerçeveler kullanın (memnuniyet ve esenlik, performans, etkinlik, iletişim ve iş birliği, verimlilik ve akış). Anketlerden gelen algısal verileri araçlardan gelen sistem verileriyle birleştirin. Teslim ölçütlerini, örneğin teslim süresini ve dağıtım sıklığını, geliştirici duyguyla birlikte izleyin. Amaç sürtünmeyi anlamak ve kaldırmaktır, bireyleri sıralamak değil. Gözetim gibi hissettiren ölçüm, platformun dayandığı güveni aşındırır.

### Bilişsel yükü birinci sınıf bir hedef yapın

Bilişsel yük, yani bir geliştiricinin işini yapmak için harcaması gereken toplam zihinsel çaba, platformların azaltmak için var olduğu gizli vergidir. Bir uygulama geliştiricinin ustalaşması gereken araç, kavram ve bağlam değiştirme sayısını en aza indirin. Makul varsayılanlar sağlayın ki takımlar daha az düşük değerli karar versin. Sahipliği, her takım sistemin sınırlı ve kavranabilir bir dilimine sahip olacak biçimde yapılandırın. Herhangi bir platform özelliğini değerlendirirken tek bir soru sorun: bunu kullanacak takımların yükünü azaltıyor mu, artırıyor mu?

## Ödünleşimler: artılar ve eksiler

| Seçim | Artılar | Eksiler | En uygun durum |
|---|---|---|---|
| Ürün olarak platform (isteğe bağlı) | Benimsenmeyi kazanır; işe yarar kalır | Tam kapsamaya ulaşması daha yavaş | Çoğu kurum |
| Zorunlu platform | Hızlı standartlaşma | Hoşnutsuzluk; dolambaçlı çözümler | Yalnızca güçlü yönetişim ihtiyaçları |
| Portal/platform satın almak | Değere daha hızlı ulaşır | Daha az özelleştirilmiş; lisans maliyeti | Hazır bir başlangıç isteyen takımlar |
| Kurum içinde inşa etmek | Tam ihtiyaca uyar | Yüksek inşa ve bakım maliyeti | Büyük, kendine özgü kurumlar |
| Yalnızca katı altın yollar | En yüksek tutarlılık | Meşru uç durumları engeller | Çok tekdüze iş yükleri |
| Kaçış kapılı esnek yollar | Tutarlılığı ve özerkliği dengeler | Yönetilecek bir miktar sapma | Çeşitli takım ihtiyaçları |

Temel gerilim, standartlaşma ile özerklik arasındadır. Standartlaşma çok az olursa her takım tekerleği tutarsız biçimde yeniden icat eder. Çok fazla olursa ihtiyaçları gerçekten farklı olan takımları boğarsınız. Ürün olarak platform felsefesi bunu, standartlaşmayı zorunlu değil çekici kılarak çözer. İkinci gerçek ödünleşim, inşa etmek ile satın almak arasındadır. Kurum içi bir platform inşa etmek tam ihtiyacınıza uyar ama kayda değer süregelen maliyet taşır. Mevcut araçları benimsemek, bir miktar özelleştirme pahasına değere ulaşmayı hızlandırır.

## Takımınızla tartışılacak sorular

1. **Platformun, öğrenilecek bir araç daha eklemek yerine bilişsel yükü gerçekten azalttığını nasıl anlayacaksınız?** Bilişsel yük, bir mühendisin işi yapmak için harcadığı toplam zihinsel çabadır ve kavram ile bağlam değişikliği ekleyen bir platform etkileyici görünürken bile durumu kötüleştirebilir. Her özellik için tek bir sınama benimseyin: bunu kullanan takımların yükünü azaltıyor mu, artırıyor mu? Ölçekte bu belirleyicidir, çünkü platform yüzlerce mühendisin önünde durur ve kafa karıştırıcı bir soyutlama hepsini her gün vergilendirir. Kanıt getirin: bir geliştiricinin bir değişikliği teslim etmek için kaç araca ve portala dokunduğu, yeni bir çalışan için ilk dağıtıma kadar geçen süre ve insanların nerede takıldığına dair nitel geri bildirim. Platform araç zincirini küçültmek yerine büyütüyorsa, döşenmiş bir yol değil bir vergi inşa etmişsiniz demektir.

2. **Puan kartlarınız hangi standartları uygulatıyor ve kötü puan alan bir hizmete gerçekte ne oluyor?** Puan kartları her hizmeti test kapsamı, güvenlik duruşu, nöbet hazırlığı ve belgeleme gibi beklentilere göre ölçer ve kırmızı bir puanın sonucu yoksa değerleri çöker. Puan kartlarının yalnızca danışma niteliğinde mi olduğuna, incelemeye mi girdiğine yoksa belirli yetenekleri mi kapıladığına karar verin ve standartların sahibini belirleyin. Düzenlemeye tabi kurumlarda puan kartları, gözetim organlarına uyum duruşunda sürekli görünürlük sağlayıp elle raporlamanın yerini alabilir, bu yüzden koyduğunuz çıta önemlidir. Taslak standartlarınızı ve bunlara göre puanlanmış gerçek hizmetlerden bir örneklemi getirin ve takımların meşru olarak nerede itiraz edeceğini tartışın. Kimsenin harekete geçmediği bir puan kartı bir panodur; net beklentilere bağlı bir puan kartı davranışı değiştirir.

3. **Platformu bir yol haritası, kullanıcı araştırması ve benimseme ölçütleriyle gerçek bir ürün olarak mı yürütüyorsunuz, yoksa bir buyruk olarak mı?** Bu bölümün temel iddiası, standartlaşmanın zorlanmak yerine çekici olması gerektiği ve bunun ancak iç mühendisleri kazanmanız gereken müşteriler olarak görürseniz geçerli olduğudur. Platformun ürün yöneticiliğini kimin üstleneceğine, geliştirici ihtiyaçlarını nasıl toplayacağınıza ve hangi benimseme ve memnuniyet sayılarının başarıyı tanımladığına karar verin. Büyük kurumlarda buyruk cezbedicidir, çünkü hızlı standartlaştırır, ama araçlar insanları yavaşlattığında dolambaçlı çözümler ve hoşnutsuzluk doğurur. Bugünkü gönüllü benimseme oranlarını, memnuniyet sinyallerini ve takımların bugün bildirdiği başlıca sürtünme noktalarını getirin. Takımlar buyruk kalktığı anda platformu bırakacaksa, bir ürün değil bir politika inşa etmişsiniz demektir.

4. **Bir takım altın yolun kenarına ulaştığında kaçış kapısı nedir ve yolu genişletip genişletmeyeceğine ya da çizgiyi koruyup korumayacağına kim karar verir?** Altın yol, makul varsayılanlara sahip, desteklenen ve görüşlü bir güzergâhtır; değeri çoğu takımın üzerinde kalmasından gelir, ama çıkışı olmayan bir yol gerçekten sıradışı işi platformun tümüyle dışına iten bir kapıya dönüşür. Bir takımın sapmayı nasıl talep edeceği, kimin inceleyeceği ve tek seferlik bir istisnayı yolun kendisinin değişmesi gerektiğine dair bir sinyalden nasıl ayıracağınız konusunda önceden anlaşın. Büyük bir kurum için bu, çeşitliliği sindiren bir platform ile bir takım engellendiğini hissettiği anda gölge araçlara dağılan bir platform arasındaki farktır. Yoldan ayrılan takımların güncel sayısını, verdikleri nedenleri ve bir istisnanın onaylanmasının ne kadar sürdüğünü getirin. Kurumsal ve kamu ortamlarında her kaçış kapısını aştığı uyum denetimlerine bağlayın; böylece döşenmiş yoldan sapma, güvenlik ya da akreditasyon temelinden sessizce sapmaya dönüşmez.

5. **Platformu kurum içinde mi inşa ediyorsunuz yoksa satın mı alıyorsunuz ve her iki yolun süregelen maliyetini dürüstçe fiyatladınız mı?** Platformun kendisi bir yaşam döngüsü olan bir üründür ve inşa etme ya da satın alma seçimi maliyet yapınızı yıllarca belirler: kurum içi bir portal tam ihtiyacınıza uyar ama onu sürdürecek fonlanmış bir takım ister, satın alınan bir platform ise lisans ve asla mükemmel olmayan bir uyum pahasına daha hızlı değere ulaşır. Hangi yeteneklerin inşa etmeye değecek kadar ayırt edici, hangilerinin satın almanız gereken sıradan olduğuna karar verin ve satıcılar olgunlaştıkça bu çizgiyi yeniden gözden geçirin. Büyük bir takım için bahis kaldıraçtır: yanlış bir inşa kararı kıt kıdemli mühendisleri bir ürünün halledeceği tesisata gömerken, yanlış bir satın alma kararı yüzlerce geliştiriciyi başkasının yol haritasına kilitler. Her seçenek için bakım, yükseltmeler ve çıkış maliyeti dahil gerçekçi bir toplam maliyet tahmini getirin. Kurumsal ve kamu tedarikinde akreditasyon ve veri taşınabilirliği şartlarını ekleyin ve üzerine inşa ettiğiniz hizmet kataloğunu ve puan kartlarını terk etmeden ayrılmanıza izin veren sözleşmeleri tercih edin.

6. **Platform takımı hizmet verdiği geliştiricilere göre nasıl fonlanıyor ve boyutlandırılıyor, bütçeler daraldığında ona ne oluyor?** Platform kaldıraçla kendini kanıtlar, çünkü küçük bir takım çok daha büyük bir uygulama geliştirici kitlesinin üretkenliğini katlar; ama aynı çerçeve, finans kesinti ararken ve fayda tek bir ürün hattına atfedilemeyip yayıldığında onu kolay bir hedef de yapar. Fonlama modeline, platform mühendislerinin destekledikleri geliştiricilere oranına ve bu yatırımı inanç yerine kanıtla nasıl savunacağınıza karar verin. Büyük bir kurum için yetersiz fonlanan platform, hiç olmamasından kötüdür: takımlar ona bağımlı olur, o çürür ve sürtünme bir bağımlılıkla birlikte geri döner. Platformun kadro sayısını, benimseme ve memnuniyet eğilimini ve kurum genelinde geri kazanılan geliştirici saatlerinin bir tahminini getirin. Kamu ve düzenlemeye tabi kurumlarda platformu uyumun bir kez kodlandığı yer olarak çerçeveleyin; böylece onu kesmek para kazandırmaz, denetim ve güvenlik işini artık elle yapmak zorunda kalan her takıma yeniden dağıtır.

## Sektör merceği

**Girişim.** Birkaç mühendisiniz varsa ve harcayacak pistiniz yoksa platform takımı kurmayın; yeni bir hizmetin klonlayıp bir saat içinde çalıştırabileceği tek bir altın yol şablon deposu inşa edin. Onu CI, bir konteyner derlemesi, lint ve bir sağlık denetimiyle önceden bağlayın ve kimse zorunlu kıldığı için değil, açıkça zaman kazandırdığı için yayılmasına izin verin. Alabileceğiniz her sıradan yeteneği satın alın, araç zincirini küçük tutun ve korunacak şeyin kapsama değil bilişsel yük olduğunu unutmayın.

**Küçük işletme.** Özel bir platform uzmanınız ve dar bir bütçeniz var; bu yüzden bir iç geliştirici platformunu kendiniz inşa etmek yerine yönetilen bir platforma ya da görüşlü bir bulut hizmetine yaslanın. Kararı satın alma-ya-karşı-inşa olarak çerçeveleyin ve varsayılanı satın almak yapın: satın alınmış bir portal ve şablonları, onları sürdürecek bir takım olmadan genelci mühendislerinize altın yollar verir. Self servis ve ayrılması kolay araçlar seçin ki bir satıcı değişikliği işlettiğiniz o birkaç hizmeti çaresiz bırakmasın.

**Kurumsal.** Ölçek ve çok sayıda takım, portföy tutarlılığını ödül yapar: fonlanmış bir platform takımı, korkuluklu altın yollar, self servis sağlama, bir hizmet kataloğu ve yüzlerce hizmette sahipliği ve kaliteyi görünür kılan puan kartları. Platformu, dolambaçlı çözümler doğuran bir buyruk olarak değil, gönüllü benimsemeyi kazanan bir ürün olarak yürütün ve güvenliği ve uyumu bir kez döşenmiş yollar olarak kodlayın ki yönetişim varsayılan olarak yolculuğa katılsın. Geliştirici deneyimini dengeli çerçevelerle ölçün ve platformun fonlamasını geri kazanılan geliştirici saatleriyle savunun.

**Kamu.** Tedarik kuralları, şeffaflık ve kamusal hesap verebilirlik platformu şekillendirir. Zorunlu güvenlik denetimlerini ve akreditasyon gereksinimlerini altın yollar boyunca korkuluk olarak kodlayın; böylece self servis portal üzerinden sağlama yapan bir takım, denetim temelini zaten karşılayan bir ortamı devralır ve aylarca süren elle akreditasyon büyük ölçüde otomatik bir adıma dönüşür. Gözetim organlarına uyum duruşunda sürekli ve denetlenebilir görünürlük vermek için puan kartlarını kullanın ve tedarikte veri taşınabilirliği ile açık arayüzler talep edin ki inşa ettiğiniz katalog ve döşenmiş yollar tek bir tedarikçiye kilitli kalmasın.

## Örnekler

**Girişim.** On iki kişilik bir girişimin platform takımı yoktur; bu yüzden kıdemli bir mühendis birkaç Cuma günü, CI, bir Dockerfile, lint ve bir sağlık denetimiyle önceden bağlanmış tek bir "yeni hizmet" şablon deposu inşa etmeye harcar. Herhangi bir mühendis onu klonlayıp bir saat içinde hazırlık ortamında çalışan bir hizmete sahip olabilir; eski bir projeden yapılandırma kopyalayıp boşlukları tahmin etmesine gerek kalmaz. Şablon altın yoldur ve herkese açıkça zaman kazandırdığı için tüm takım, kimseye söylenmeden onu benimser.

**Kurumsal.** Büyük bir sigorta şirketi, bir iç geliştirici portalı sunan bir platform takımı kurar. Portal her hizmeti sahibi, belgeleri ve sağlık puan kartıyla kataloglar. Yeni hizmetler, CI/CD, güvenlik taraması, gözlemlenebilirlik ve uyum denetimleriyle önceden bağlanmış altın yol şablonlarından oluşturulur. Veritabanları ve ortamlar portal üzerinden self servis sağlanır. Yeni bir mühendisin ise başlama süresi haftalardan günlere düşer ve her hizmet aynı döşenmiş yolu izlediği için denetim kanıtı otomatik olarak üretilir. Platform benimsemesi gönüllüdür ve onu kullanan takımlar gözle görülür biçimde daha hızlı teslim ettiği için yayılır.

**Kamu.** Düzinelerce dijital hizmet işleten bir federal kurum ortak bir platform kurar. Zorunlu güvenlik denetimlerini ve akreditasyon gereksinimlerini altın yolları boyunca korkuluk olarak kodlar. Altyapıyı self servis portal üzerinden sağlayan bir takım, denetim temelini zaten karşılayan bir ortamı devralır. Bu, aylar süren elle akreditasyon çalışmasını büyük ölçüde otomatik hale getirir. Puan kartları her hizmetin uyum duruşunu izler; gözetim organlarına elle raporlama olmadan sürekli görünürlük verir ve kıt uzman personeli tekrarlayan incelemeden kurtarır.

## İş gerekçesi: motivasyonlar, YG ve TSM

Platform mühendisliğinin YG'si, geri kazanılan geliştirici zamanından ve kazanılan tutarlılıktan gelir. Mühendisler altyapıyla boğuşmaya ve bilgi aramaya daha az zaman harcadığında, pahalı zamanlarının daha büyük bölümü ürün değeri sunmaya gider. Daha hızlı başlama, daha az tekrarlanan çözüm ve otomatik uyum; hepsi ölçülebilir kapasiteye ve azalan riske dönüşür. Platform birçok takıma hizmet verdiği için ona yapılan her iyileştirme tüm kurum boyunca kaldıraçlanır.

TSM açısından benimseme maliyeti gerçek ve süregelen bir yatırımdır: fonlanmış bir platform takımı, araçlar (inşa edilmiş ya da satın alınmış) ve platformu sürekli iyileştirmeyle bir ürün olarak yürütme disiplini. Benimsememenin maliyeti yaygın ama büyüktür: her takımın aynı altyapı vergisini tekrar tekrar ödemesi, tutarsız güvenlik ve uyum, yavaş başlama ve angarya yüzünden tükenen kıdemli mühendisler. Liderlik için gerekçe en iyi kaldıraç terimleriyle kurulur. Mütevazı, iyi yönetilen bir platform takımı çok daha büyük bir uygulama geliştirici kitlesinin üretkenliğini katlar ve yönetişimi, her takımın onu doğru yapmasına güvenmek yerine bir kez kodlar.

## Anti-kalıplar ve tuzaklar

- **Sunulmayıp dayatılan platform.** Geliştiricilerin sevmediği bir platformu zorunlu kılmak dolambaçlı çözümler ve hoşnutsuzluk doğurur.
- **Fildişi kule platform takımı.** Gerçek geliştirici ihtiyaçlarını anlamadan inşa etmek, kimsenin istemediği araçlar üretir.
- **Döşenmiş yollar yerine kapılar.** Meşru işi engelleyen korkuluklar takımları platformu tümüyle atlamaya iter.
- **Tek üretkenlik ölçütü.** Üretkenliği oyuna getirilebilir tek bir sayıya indirmek davranışı bozar ve güveni aşındırır.
- **Gözetim olarak ölçüm.** Bireyleri sıralamak için kullanılan DevEx ölçütleri, platformun ihtiyaç duyduğu psikolojik güvenliği yok eder.
- **Kaçış kapısı olmayan altın yol.** Gerçek uç durumlar için esneyemeyen katı yollar engele dönüşür.
- **Yetersiz fonlanan platform.** Platformu bir yan proje olarak görmek onu aç bırakır ve kötü bir deneyimi garantiler.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Platform yoktur. Her takım kendi araçlarını ve altyapısını tepkisel biçimde bir araya getirir; yoğun bilet odaklı devirler, tekrarlanan çözümler ve yüksek bilişsel yük vardır. Her takım sağlamayı, dağıtımı ve uyumu kendi başına, tutarsız biçimde çözer.

**Düzey 2, Geliştirme.** Çoğu zaman hevesli bir mühendisin inşa ettiği bazı ortak araçlar, şablonlar ve başlangıç depoları ortaya çıkar, ama parçalıdır ve kısmen elle yürür. Birkaç takım bir altın yolu benimserken diğerleri görmezden gelir, self servis sınırlıdır ve geliştirici deneyimi ölçülmez; bu yüzden platformun değeri anekdota dayanır.

**Düzey 3, Standartlaştırma.** Bir platform takımı, kurum genelinde uygulanan belgelenmiş altın yollar, self servis sağlama, hizmet kataloglu bir geliştirici portalı ve puan kartları yürütür. Güvenlik, politika ve uyum korkulukları döşenmiş yollara gömülüdür; böylece standart iş akışı uyumlu olandır ve aynı gelenekler gruplara göre değişmek yerine takımlar arasında geçerlidir.

**Düzey 4, Yönetme.** Platform veriyle, başlangıç değerlerine karşı ölçülür ve kontrol edilir. Benimseme, memnuniyet, ilk dağıtıma kadar geçen süre, teslim süresi ve dağıtım sıklığı, SPACE gibi dengeli çerçeveler ve birleşik anket ve sistem sinyalleriyle izlenir; puan kartı sonuçları incelemeye girer ve bilişsel yük, başlama süresi ve geri kazanılan geliştirici saatleri hedeflere karşı izlenir. Bir yeteneğe yatırım yapma ya da onu emekliye ayırma kararları savunuculuğa değil kanıta dayanır.

**Düzey 5, Orkestrasyon.** Platform, yüksek gönüllü benimsemeye sahip olgun bir üründür; geliştirici geri bildirimi ve ölçütlerle sürekli iyileştirilir ve kurum genelinde güvenlik, uyum ve teslim planlamasıyla bütünleşiktir. Altın yollar ihtiyaçlar değiştikçe uyum sağlar, yönetişim standart iş akışının görünmez bir özelliğidir ve platform takımı, teknoloji ve kurum geliştikçe yetenekleri rutin olarak emekliye ayırır, değiştirir ve kapsamlarını yeniden belirler.

## Tartışma fikirleri

- Bir platformu zorunlu kılmadan nasıl benimsetirsiniz ve bir buyruk, eğer varsa, ne zaman haklı çıkar?
- Hangi altın yollar takımlarınıza ilk olarak en çok değeri sağlar?
- Geliştirici deneyimini gözetim gibi hissettirmeden nasıl ölçersiniz?
- Sıradışı takımlar platformdan tümüyle çıkmaya zorlanmasın diye kaçış kapıları nerede bulunmalı?
- Bir platform takımı için, hizmet verdiği geliştiricilere göre doğru boyut ve fonlama modeli nedir?
- Geliştirici portalınız ve araçlarınız için neyi kurum içinde inşa edeceğinize, neyi satın alacağınıza nasıl karar verirsiniz?

## Önemli çıkarımlar

- Platformu, takımları gerçekten hızlandırarak benimsenmeyi kazanan bir ürün olarak yürütün.
- Doğru, güvenli ve uyumlu yolu kolay yol yapan altın yollar ve döşenmiş yollar sağlayın.
- Takımlar biletlerde ve devirlerde beklemeyi bırakacak şekilde gerçek self servis sunun.
- Sahipliği, mimariyi ve kaliteyi görünür kılmak için portalları, katalogları ve puan kartlarını kullanın.
- Geliştirici deneyimini SPACE gibi dengeli çerçevelerle ölçün, asla oyuna getirilebilir tek bir sayıyla değil.
- Bilişsel yükü azaltmayı platformun merkezi amacı sayın.

## Kaynaklar ve ileri okuma

- Matthew Skelton and Manuel Pais, *Team Topologies*.
- Nicole Forsgren, Margaret-Anne Storey, Chandra Maddila, et al., "The SPACE of Developer Productivity" (paper).
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate*.
- Gregor Hohpe, *The Software Architect Elevator*.
- Camille Fournier, *The Manager's Path*.
- Cloud Native Computing Foundation, platform engineering white paper.
