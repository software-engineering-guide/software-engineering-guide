# 2.3 API'ler ve arayüz tasarımı

## Genel bakış ve motivasyon

Bir [API](https://en.wikipedia.org/wiki/API) (uygulama programlama arayüzü), bir yazılım parçasının diğerine yetenek sunduğu sözleşmedir. Takımların, sistemlerin ve kuruluşların buluştuğu yerdir ve yanlış yapılması en kalıcı ve en pahalı olan şeydir. Bir iç işlev imzasını özgürce yeniden düzenleyebilirsiniz. Yayımlanmış bir API farklıdır: hiç tanışmayabileceğiniz tüketicilere verilmiş bir sözdür ve onu bozmak onları bozar. Kuruluşlar [tek parçaları](https://en.wikipedia.org/wiki/Monolithic_application) hizmetlere böldükçe ve yetenekleri ortaklara ve kamuya açtıkça, API ana ürün yüzeyi ve ana entegrasyon riski haline gelir.

Büyük takımlar için API'ler, insanların bağımsız çalışmasını sağlayan şeydir. İyi tasarlanmış bir arayüz, her tüketiciyle eşgüdüm sağlamadan iç yapınızı değiştirmenize izin verir; bir hizmet sınırının bütün amacı budur. Kötü tasarlanmış bir arayüz ise iç ayrıntıyı sızdırır, eşzamanlı dağıtıma zorlar ve bir hizmetler kümesini dağıtık tek parçaya dönüştürür: birbirinden ayrılmış ama birlikte inşa edilip dağıtılmaları gerekecek kadar bağlı hizmetler. API tasarımınız takımlarınızın ne kadar bağımsız hareket edebileceğini doğrudan belirler.

Kurumsal ve kamu ortamlarında API'ler ayrıca uyum, güvenlik ve uzun ömür yükümlülükleri taşır. Bir kamu API'sinin [açık standartları](https://en.wikipedia.org/wiki/Open_standard) izlemesi, yıllarca kararlı kalması ve eşgüdüm sağlayamayacağınız dış geliştiricilere hizmet etmesi gerekebilir. Kurumsal API'ler, sözleşmeli hizmet düzeyleriyle ortak entegrasyonlarının temelini oluşturur. Bunların hepsi sürümleme disiplini, [geriye dönük uyumluluk](https://en.wikipedia.org/wiki/Backward_compatibility), yönetişim ve geliştirici deneyimi çıtasını yükseltir.

## Temel ilkeler

- Önce sözleşmeyi tasarlayın. Arayüz, gerçekleştirimin yan ürünü değil, bilinçli bir ürün kararıdır.
- Kendi rahatınız için değil, tüketicinin deneyimi için optimize edin.
- Geriye dönük uyumluluğu bir söz olarak ele alın. Bozucu değişiklikler yeni bir sürüm ve bir geçiş yolu gerektirir.
- Kolay olanı doğru yapın: makul varsayılanlar, öngörülebilir hatalar, tutarlı kurallar.
- Başarısızlık için tasarlayın. [Eş güçlülük](https://en.wikipedia.org/wiki/Idempotence) (tekrarlanan bir istek tek bir istekle aynı etkiye sahiptir), yeniden denemeler, sayfalama ve [hız sınırlama](https://en.wikipedia.org/wiki/Rate_limiting) sonradan düşünceler değil, birinci sınıf kaygılardır.
- Protokol üslubunu moda için değil, etkileşime uyacak şekilde seçin.
- API'leri sahipleri, yaşam döngüleri ve belgeleriyle ürünler olarak yönetin.

## Öneriler

### API öncelikli ve sözleşme güdümlü çalışın

Gerçekleştirimi yazmadan önce API sözleşmesini, kaynaklarını, işlemlerini, şemalarını ve hata anlamlarını tanımlayın ve inceleyin. Makine tarafından okunabilir bir belirtim kullanın; böylece sözleşme belgeleri, istemci ve sunucu taslaklarını, taklit sunucuları ve doğrulamayı üretebilir. Artık tüketiciler siz inşa ederken taklide karşı entegre olmaya başlayabilir ve sözleşme, her iki tarafın test ettiği tek doğruluk kaynağı haline gelir.

### Etkileşim üslubunu bilinçli seçin

[REST](https://en.wikipedia.org/wiki/REST) (temsili durum aktarımı), [GraphQL](https://en.wikipedia.org/wiki/GraphQL), [gRPC](https://en.wikipedia.org/wiki/GRPC) ve [olay güdümlü mesajlaşma](https://en.wikipedia.org/wiki/Event-driven_architecture) arasından kişisel tercihe değil, etkileşime göre seçin. Kaynak odaklı, geniş biçimde birlikte çalışabilir, önbelleğe alınabilir arayüzler için REST kullanın. Çeşitli istemcilerin zengin bir grafik üzerinde esnek, toplanmış okumalara ihtiyaç duyduğu yerde GraphQL kullanın. İç hizmetler arasında yüksek performanslı, güçlü tipli çağrılar için gRPC kullanın. Eşzamansız, ayrık iş akışları ve durum değişikliklerini yaymak için olay güdümlü mesajlaşma kullanın. Birçok büyük sistem aynı anda birkaç üslup kullanır; her biri uyduğu yerde.

### Sürümleme ve kullanımdan kaldırmayı disiplinle yapın

Açık bir sürümleme stratejisi ve yayımlanmış bir kullanımdan kaldırma politikası benimseyin: değişiklikleri nasıl sınıflandırdığınız, eski sürümleri ne kadar desteklediğiniz ve tüketicileri nasıl bilgilendirdiğiniz. Geriye dönük uyumlu değişiklikler (isteğe bağlı alanlar eklemek, yeni uç noktalar) ile bozucu değişiklikler (alanları kaldırmak ya da yeniden adlandırmak, türleri ya da anlamları değiştirmek) arasında net bir çizgi çizin. Mevcut bir alanın anlamını asla değiştirmeyin. Tüketicilere geçiş için örtüşme pencereleri verin ve zaman çizelgelerini önceden iyi iletin.

### Hata anlamlarını tutarlı ve makine tarafından okunabilir yapın

Yapılandırılmış, öngörülebilir hatalar döndürün: kararlı makine tarafından okunabilir kodlar, insan tarafından okunabilir mesajlar ve hassas iç ayrıntıları sızdırmadan harekete geçmeye yetecek bağlam. Her uç noktada aynı durum anlamlarını kullanın ki istemciler hataları tekdüze ele alabilsin. Bir tüketicinin karşılaşabileceği her hatayı belgeleyin.

### Eş güçlülüğü, sayfalamayı ve hız sınırlamayı içine kurun

Eş güçlülük anahtarlarını destekleyerek yazma işlemlerini yeniden deneme için güvenli yapın; böylece zaman aşımından sonra yeniden deneyen bir istemci iki kez ücret kesmez ya da iki kez oluşturmaz. Her liste uç noktasını ilk günden sayfalayın ve büyük ya da değişen veri kümeleri için imleç tabanlı sayfalamayı tercih edin. Hız sınırlarını uygulayın ve belgeleyin ve istemcilerin zarifçe geri çekilebilmesi için güncel sınır durumunu istemcilere döndürün.

### API'leri yönetin ve geliştirici deneyimine yatırım yapın

Her API'yi bir sahibi, bir yaşam döngüsü ve bir katalog girişiyle ürün olarak ele alın. Arayüzlerin takımlar arasında tutarlı kalması için bir tasarım incelemesi ya da API standartları kurulu kurun. Geliştirici deneyimine yatırım yapın: doğru referans belgeleri, hızlı başlangıçlar, örnekler, bir kum havuzu ve bir değişiklik günlüğü. Büyük bir ekosistemde API'leri keşfedilebilir kılan bir portal ya da katalog şarttır.

## Ödünleşimler: artılar ve eksiler

| Üslup | En uygun olduğu durum | Artılar | Eksiler |
|---|---|---|---|
| REST / HTTP | Herkese açık, kaynak odaklı API'ler | Yaygın, önbelleğe alınabilir, basit, birlikte çalışabilir | Aşırı/yetersiz getirme; çok sayıda gidiş dönüş; belirtilmedikçe gevşek sözleşmeler |
| GraphQL | Çeşitli istemciler için esnek okumalar | İstemcinin belirttiği sorgular; tek uç nokta; güçlü şema | Önbellek ve hız sınırlama karmaşıklığı; sorgu maliyeti riskleri; sunucu karmaşıklığı |
| gRPC | Dahili yüksek performanslı çağrılar | Hızlı, kompakt, güçlü tipli, akış | Zayıf tarayıcı desteği; daha az insan tarafından okunabilir; daha ağır araçlar |
| Olay güdümlü | Eşzamansız, ayrık iş akışları | Gevşek bağlaşım; ölçeklenebilir; dayanıklı | Akıl yürütmesi daha zor; nihai tutarlılık; operasyonel karmaşıklık |

Sürümleme stratejileri kararlılığı bakımla takas eder. Birçok eski sürümü desteklemek tüketicileri korur ama sürdürmeniz ve test etmeniz gereken kodu çoğaltır. Geriye dönük uyumluluk kendi özgürlüğünüzü tüketici kararlılığıyla takas eder; yaygın kullanılan bir API için genellikle doğru takastır. Büyük resim: kötü bir API kararının maliyetini arayüzün bütün ömrü boyunca her tüketici öder. Bu yüzden sınırda hemen her yerden daha fazla tasarım çabası harcamak değerlidir.

## Takımınızla tartışılacak sorular

1. **Bir değişikliği geriye dönük uyumlu mu yoksa bozucu mu diye nasıl sınıflandırıyorsunuz ve sessiz bir bozulmayı yayımlanmadan önce hangi otomatik kontrol yakalıyor?** Bu bölüm sert bir çizgi çizer: isteğe bağlı alanlar ve yeni uç noktalar eklemek güvenlidir, alanları kaldırmak ya da yeniden adlandırmak, türleri değiştirmek ya da bir alanın anlamını değiştirmek tüketicileri bozar. Büyük bir takımda değişikliği yapan kişi çoğu zaman her tüketiciyi göremez, bu yüzden "küçük" bir ince ayar, hiç konuşmadığınız ortakları sessizce bozabilir. Toplantıya somut sinyal getirin: yayımlanmış belirtime karşı CI'de otomatik sözleşme uyumluluğu kontrolleri çalıştırıyor musunuz yoksa birinin kuralı hatırlamasına mı güveniyorsunuz. Bozucu bir değişikliğin her ortak boyunca koordineli bir geçişe zorladığı ve satıcı ve yönetim değişikliklerine yayılabildiği kurumsal ve kamu ortamlarında, maliyet tüketici sayısıyla ölçeklenir. Sınıflandırma kurallarına karar verin ve bir uyumluluk kapısı bağlayın; böylece uyumsuz bir değişiklik bir entegrasyon yerine derlemeyi başarısız kılar.

2. **Hangi güvenilirlik ilkelleri, eş güçlülük anahtarları, sayfalama ve hız sınırlama, ilk günden her yeni uç noktada zorunludur?** Bölüm bunların birinci sınıf kaygılar olduğunu ısrarla belirtir, çünkü yayında bir ücret uç noktasına eş güçlülük anahtarı eklemek ya da zaten gönderilen bir listeye sayfalama eklemek başlı başına bozucu bir değişikliktir. Büyük bir ekosistem bunu büyütür: testte çalışan bir uç nokta gerçek veri hacminde çöker ve eş güçlü olmayan bir yazma tek bir ağ aksamasını çift ücrete çevirir. Hangi mevcut uç noktaların bunlardan yoksun olduğuna ve bir yeniden deneme fırtınasının ne yapacağına dair kanıt getirin. Varsayılanları yeni uç noktalar için pazarlık dışı yapın: her listede imleç sayfalama, her yazmada eş güçlülük anahtarları, güncel durumlarını döndüren belgelenmiş hız sınırları. Bu, gelecekteki zorunlu bir geçişi tek seferlik bir tasarım alışkanlığına dönüştürür.

3. **Sözleşmeyi gerçekleştirimi yazmadan önce gerçekten tasarlayıp inceliyor musunuz, yoksa arayüz koddan mı sızıyor?** API öncelikli öneri, baştan incelenen, belgeleri, taslakları ve taklitleri üreten ve tüketicilerin siz inşa ederken bir taklide karşı entegre olmasına izin veren makine tarafından okunabilir bir belirtim ister. Sözleşme gerçekleştirimin ardından geldiğinde arayüz iç veritabanı yapısını açığa çıkarır ve gerçekleştirim her değiştiğinde kayar; bu, bu bölümdeki en büyük anti-kalıptır. İncelenecek sinyal: bir tüketici bugün taklitinize karşı entegre olmaya başlayabilir mi, yoksa çalışan bir arka yüzü mü beklemeli. Arayüzün ürün yüzeyi ve yanlış yapılması en pahalı şey olduğu herkese açık ve ortak API'ler için sözleşmeye bir gün harcamak haftalarca destek gidip gelmesini önler. Sözleşme incelemesini gerçekleştirim başlamadan önce zorunlu bir adım yapın.

4. **İki takım aynı yeteneği açığa çıkarmak istediğinde hangi etkileşim üslubu kazanır ve dördüncü bir protokole hayır deme yetkisi kimde?** Bu bölüm REST, GraphQL, gRPC ya da olay güdümlü mesajlaşmayı etkileşim uyumuna göre seçmenizi söyler, ama ölçekte gerçek risk her takımın kendi favorisini seçmesi ve tüketicilerin her uç noktada farklı bir kuralla karşılaşmasıdır. Büyük bir kuruluş bu parçalanmanın bedelini istemci kütüphaneleri, ağ geçitleri, izleme ve artık bir yerine dört deyim öğrenen her entegratörün bilişsel yükü olarak öder. Zaten üretimde olan protokollerin envanterini, her birinin hizmet etmek için seçildiği etkileşimi ve birden fazlasına yayılan tüketicileri getirin. Karşıt değerlendirme gerçektir: paylaşılan bir varsayılan çoğalmayı azaltır, ancak katı bir zorunluluk gRPC şeklindeki sorunları REST şeklindeki bir deliğe zorlar. İstisna sürecine sahip olan standart organını ya da mimari incelemeyi adlandırın, çünkü kurumsal ve kamu alanlarında üslup çoğalması entegrasyon üzerinde kalıcı bir vergi haline gelir ve ortaklar her birine bağımlı olduğunda geri alması zor bir sorundur.

5. **Yayımlanmış kullanımdan kaldırma politikamız nedir ve ilan ettiğimiz destek penceresine gerçekten uyduğumuzu kanıtlayabilir miyiz?** Bölüm sürümlemeyi ve kullanımdan kaldırmayı bir disiplin olarak ele alır: eski sürümlerin ne kadar yaşadığına, tüketicilerin nasıl bilgilendirildiğine ve geçiş için ne kadar örtüşme aldıklarına dair yazılı bir politika. Uygulayamayacağınız bir söz hiç olmamasından kötüdür, çünkü büyük bir ekosistem hiç konuşmadığınız ve üretimde bozulana kadar emekli bir sürümü çağırmaya devam edecek tüketiciler içerir. Tartışmaya kanıt getirin: bugün kaç canlı sürüm taşıyorsunuz, her birindeki gerçek kullanım, hangi tüketicilerin hâlâ kullanımdan kaldırılmış bir uç noktayı çağırdığını görüp göremediğiniz ve son kapatmanın ne kadar önceden duyurulduğu. Karşıt baskı bakım maliyeti ile tüketici kararlılığıdır ve ikisi de gerçektir. Sözleşmeli hizmet düzeyleri altındaki kurumsal ortaklar ve yönetimler ve satıcı değişiklikleri boyunca ayakta kalması gereken kamu API'leri için destek penceresi onu veren takımdan uzun yaşayabilecek bir taahhüttür; bu yüzden kimin sahip olduğuna ve bir kapatmanın gerçekleşmeden önce nasıl güvenli kanıtlandığına karar verin.

6. **Geliştirici deneyimimizin iyi olduğunu nasıl biliyoruz, yoksa API bizim için çalıştığı için mi varsayıyoruz?** Bu bölüm her API'yi, benimsenmesinin doğru referans belgelerine, hızlı başlangıçlara, örneklere, bir kum havuzuna, bir değişiklik günlüğüne ve keşfedilebilir bir kataloğa bağlı olduğu bir ürün olarak çerçeveler. Takımlar rutin olarak "API işliyor"u "API kullanılabilir" ile karıştırır ve boşluk destek biletleri, başarısız entegrasyonlar ve sessizce vazgeçen tüketiciler olarak ortaya çıkar. Görüş yerine ölçülebilir sinyaller getirin: yeni bir entegratör için ilk başarılı çağrıya kadar geçen süre, uç nokta başına destek bileti hacmi, yayımlanmış belgelerin canlı sözleşmeye göre ne kadar eskidiği ve yeni gelenin ekibinize e-posta atmadan portaldan kendi kendine hizmet alıp alamayacağı. Gerilim, belgeleme ve portalların özellik yayımlamayla yarışan gerçek çaba gerektirmesidir; yine de büyük bir ekosistemde zayıf geliştirici deneyimi entegrasyon maliyetini aynı anda yüzlerce tüketiciye iter. Açık bir API'nin eşgüdüm sağlayamayacağınız dış geliştiricilere hizmet ettiği ve şeffaflığın çoğu zaman zorunlu olduğu kamuda, kullanılabilir, iyi belgelenmiş, keşfedilebilir bir arayüz bir olsa iyi olurun değil, kamusal hesap verebilirlik yükümlülüğünün parçasıdır.

## Sektör merceği

**Girişim.** İki üç mühendis ve tören için zaman olmadan sözleşmeyi hafif ama gerçek tutun: ilk tasarım ortağı müşterilerinizin siz inşa ederken entegre olabileceği tek bir makine tarafından okunabilir belirtim. Henüz bir API ağ geçidi, bir katalog ya da bir yönetişim kurulu kurmayın, ama sonradan eklemesi acı verici iki alışkanlığı kilitleyin: yazmalarda eş güçlülük anahtarları ve listelerde imleç sayfalama; çünkü onları yayındaki bir uç noktaya sonradan eklemek karşılayamayacağınız bozucu bir değişikliktir. Tek bir etkileşim üslubunu, neredeyse her zaman REST'i tercih edin; böylece ilk yılınıza protokol çoğalması taşımazsınız.

**Küçük işletme.** Özel bir API uzmanı ve sıkı bir bütçe olmadan, bir genelcinin derin protokol uzmanlığı olmadan arayüzü sürdürebilmesi için bir belirtimden belgeler, taklitler ve istemci taslakları üreten araçlara yaslanın. Satın alma ve inşa etmeyi sıkı tartın: hazır bir ağ geçidi ya da bir API yönetim platformu, aksi halde elle yapacağınız hız sınırlama, anahtarlar ve bir geliştirici portalı verir. Yüzeyi küçük ve kuralları tutarlı tutun, çünkü her fazladan uç nokta ve her tek seferlik hata biçimi ince bir takımın sonsuza kadar desteklemesi gereken bir şeydir.

**Kurumsal.** Birçok özerk takım boyunca merkezi sorun, darboğaz olmadan tutarlılıktır: paylaşılan bir üslup kılavuzu, bir API standartları incelemesi, arayüzleri keşfedilebilir kılan bir katalog ve sessiz bir bozulmanın bir entegrasyon yerine derlemeyi başarısız kılması için CI'de otomatik geriye dönük uyumluluk kontrolleri. Her API'yi adı konmuş bir sahibi, bir yaşam döngüsü ve yayımlanmış bir kullanımdan kaldırma politikasıyla ürün olarak yönetin ve portföy sağlıklı kalsın diye benimsemeyi, destek yükünü ve bozucu değişiklik sıklığını ölçün. Etkileşim üslublarını ve sürümleme kurallarını kuruluş genelinde standartlaştırın, çünkü bu ölçekte parçalanma pahalı varsayılandır.

**Kamu.** Tedarik kuralları, açık standart zorunlulukları ve kamusal hesap verebilirlik her seçimi biçimlendirir. Sözleşmeyi açıkça yayımlayın, zorunlu açık standartları izleyin ve eşgüdüm sağlayamayacağınız dış geliştiricilerin kendi kendilerine hizmet alabilmesi için bir kum havuzu ve referans belgeleri sağlayın. Uzun vadeli geriye dönük uyumluluğu bir politika gereksinimi olarak ele alın, çünkü entegrasyonlar yönetimler ve satıcı değişiklikleri boyunca ayakta kalmalıdır ve bozucu değişiklikleri nadir, ağır yönetilen ve çok önceden duyurulan yapın. API'yi ve belgelerini kamusal ve denetim incelemesine dayanacak kadar şeffaf tutun ve gelecekteki bir yönetimi tuzağa düşürecek özel biçimlerden kaçının.

## Örnekler

**Girişim.** İlk herkese açık API'sini yayımlayan bir tohum aşaması girişimi, sözleşmeyi koddan önce makine tarafından okunabilir bir belirtim olarak yazar; böylece iki tasarım ortağı müşterisi arka yüz hâlâ inşa edilirken bir taklide karşı entegre olabilir. Yalnızca bir avuç tüketiciyle bile, ücret uç noktasına eş güçlülük anahtarları ve her listeye imleç sayfalama ekler, çünkü ortaklar API'ye bağımlı olduktan sonra onları sonradan eklemek karşılayamayacağı bozucu bir değişiklik anlamına gelirdi. Baştaki sözleşme bir güne mal olur ve haftalarca destek gidip gelmesinden tasarruf sağlar.

**Kurumsal.** Büyük bir ödeme şirketi binlerce satıcıya herkese açık bir REST API sunar. Her yazma uç noktası bir eş güçlülük anahtarı kabul eder, böylece bir ağ yeniden denemesi asla çift ücret oluşturmaz. Her liste uç noktası imleç sayfalama kullanır. Hatalar herkese açık bir referansta belgelenmiş kararlı kodlar taşır. Resmi bir kullanımdan kaldırma politikası, herhangi bir sürüm için önceden bildirim ve geçiş kılavuzlarıyla uzun bir destek penceresi garanti eder. Bu disiplin rekabetçi bir avantajdır: entegratörler API'nin altlarında bozulmayacağına güvenir.

**Kamu.** Ulusal bir dijital hizmet, zorunlu açık standartları ve API öncelikli bir tasarım sürecini izleyerek vatandaş verileri için açık bir API yayımlar. Sözleşme yapıdan önce belirtilir ve incelenir, merkezi bir kamu API kataloğunda yayımlanır ve bir kum havuzuyla sunulur; böylece bireysel olarak eşgüdüm sağlanamayan üçüncü taraf geliştiriciler kendi başlarına entegre olabilir. Uzun vadeli geriye dönük uyumluluk bir politika gereksinimidir, çünkü entegrasyonlar yönetimler ve satıcı değişiklikleri boyunca ayakta kalmalıdır. Bu yüzden bozucu değişiklikler nadir ve ağır yönetilir.

## İş gerekçesi: motivasyonlar, YG ve TSM

İyi API tasarımı, sistemleri bağlamanın ve ortakları uyumlandırmanın çoğu zaman en büyük maliyeti olan entegrasyon maliyetini düşürür. Net, kararlı, iyi belgelenmiş bir API ile tüketiciler tek bir destek bileti olmadan günler içinde entegre olur. Kötü olanı sonsuz destek yükü, başarısız entegrasyonlar ve itibar hasarı üretir. API'nin kendisi ürün olduğunda geliştirici deneyimi benimsemeyi ve geliri doğrudan yönlendirir.

En büyük gizli maliyet bozucu değişikliklerdir. Her bozucu değişiklik, dahili takımlar ve dış ortaklar dahil tüm tüketicileri koordineli bir geçişe zorlar ve toplam maliyet tüketici sayısıyla ve onların birlikte hareket etmesinin ne kadar zor olduğuyla ölçeklenir. Sözleşme öncelikli tasarıma, geriye dönük uyumluluğa ve sürümleme disiplinine baştan yatırım yapmak bu pahalı, kuruluş çapında geçiş olaylarından kaçınır. Liderlikle konuşurken API kalitesini takım özerkliği, ortak ekosistem büyümesi ve maliyetli zorunlu geçişlerden kaçınmanın kaldıraç noktası olarak çerçeveleyin. Kanıtınız olarak entegrasyon süresini, destek bileti hacmini ve bozucu değişiklik sıklığını izleyin.

## Anti-kalıplar ve tuzaklar

- **Önce gerçekleştirim API'leri:** arayüz iç veritabanı yapısını sızdırır ve gerçekleştirim her değiştiğinde değişir.
- **Sessiz bozucu değişiklikler:** bir alanı yeniden amaçlamak ya da doğrulamayı sürüm artışı olmadan sıkılaştırmak tüketicileri öngörülemez biçimde bozar.
- **Gevezeler arayüzler:** tek bir mantıksal işlem için çok sayıda gidiş dönüş gerektiren, performansa ve kullanılabilirliğe zarar veren tasarımlar.
- **Tutarsız kurallar:** her uç nokta kendi adlandırmasını, hata biçimini ve sayfalamasını icat eder; böylece istemciler genelleyemez.
- **Sayfalama ya da hız sınırlama yok:** testte çalışıp gerçek veri hacminde ya da yükte çöken uç noktalar.
- **Eş güçlü olmayan yazmalar:** yeniden denemeler kopyalara yol açar; tek bir ağ aksaması veriyi bozar.
- **Sürüm çoğalması:** kullanımdan kaldırma olmadan çok fazla canlı sürüm; bakımı yönetilemez olana kadar çoğaltır.
- **Sonradan düşünce olarak belgeler:** tüm entegrasyon maliyetini tüketicilere iten belgesiz ya da eskimiş referanslar.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** API'ler gerçekleştirimden bir yan ürün olarak ortaya çıkar; paylaşılan kural yoktur; arayüz iç veritabanı yapısını sızdırır; bozucu değişiklikler yaygındır, duyurulmaz ve bir tüketicinin entegrasyonu başarısız olduğunda keşfedilir.
- **Düzey 2, Geliştirme:** Bazı takımlar temel REST kurallarını izler, gayriresmi sürümler ve belgeleri elle yazar, ama uygulama takımlar arasında tutarsızdır; eş güçlülük, sayfalama ve hız sınırlama bazı uç noktalarda görünür, diğerlerinde görünmez; tüketiciler her API'nin tuhaflıklarını vaka vaka öğrenmeye devam eder.
- **Düzey 3, Standartlaştırma:** Makine tarafından okunabilir belirtimlerle sözleşme öncelikli tasarım belgelenir ve kuruluş genelinde uygulanır; yayımlanmış bir kullanımdan kaldırma politikası, tutarlı hata anlamları ve zorunlu eş güçlülük, imleç sayfalama ve hız sınırlama her yeni uç nokta için geçerlidir; paylaşılan bir üslup kılavuzu ve bir API standartları incelemesi arayüzleri takımlar arasında tutarlı tutar.
- **Düzey 4, Yönetme:** API portföyü temel çizgilere karşı ölçülür ve kontrol edilir: otomatik geriye dönük uyumluluk kontrolleri CI'de her değişikliği kapıya koyar ve ilk başarılı çağrıya kadar süreyi, uç nokta başına destek bileti hacmini, bozucu değişiklik sıklığını, canlı sürüm sayısını ve uç nokta başına kullanımı izlersiniz; böylece kullanımdan kaldırma ve tasarım kararları görüşe değil kanıta dayanır. Her API, adı konmuş sahibi olan bir katalogda yönetilen bir üründür ve bir hizmet hedeflerinden saptığında metrikler eylemi tetikler.
- **Düzey 5, Orkestrasyon:** API stratejisi sürekli iyileştirilir ve kuruluş genelinde bütünleşir; katalog, ağ geçidi, sürümleme kuralları ve uyumluluk kapıları tek bir sistem olarak çalışır; kuruluş ölçülen benimsemeye ve maliyete dayanarak arayüzleri rutin olarak emekliye ayırır, birleştirir ve yeniden kapsamlar; etkileşim üslubu ve sürümleme standartları ekosistem, ortaklar ve teknoloji kaydıkça uyum sağlar ve bozucu değişiklikler nadir ve iyi yönetilir.

## Tartışma fikirleri

- Dahili bir API'nin dışarıya yayımlanacak kadar kararlı olduğuna ne zaman karar verirsiniz?
- Sizin bağlamınızda kullanımdan kaldırılmış sürümler için doğru destek penceresi nedir ve bedelini kim öder?
- GraphQL ya da gRPC dahili olarak REST'in yerini nerede almalı ve değerden çok karmaşıklık nerede ekler?
- Birçok özerk takım boyunca darboğaz olmadan API tutarlılığını nasıl uygularsınız?
- Yapay zekanın tüketebileceği API'ler ve ajan araç arayüzleri tasarım kurallarınızı nasıl değiştirmeli?
- Hangi otomatik kontroller geriye dönük uyumsuz değişiklikleri yayımlanmadan önce yakalayabilir?

## Önemli çıkarımlar

- Önce sözleşmeyi tasarlayın; API bir üründür ve uzun ömürlü bir sözdür.
- Geriye dönük uyumluluk tüketicileri korur; bozucu değişiklikler yeni sürümler ve geçiş yolları gerektirir.
- REST, GraphQL, gRPC ya da olayları modaya değil etkileşim uyumuna göre seçin.
- Eş güçlülüğü, sayfalamayı, hız sınırlamayı ve tutarlı hataları ilk günden içine kurun.
- API'leri sahipleri, katalogları ve güçlü geliştirici deneyimiyle ürünler olarak yönetin.

## Kaynaklar ve ileri okuma

- Roy Fielding, *Architectural Styles and the Design of Network-based Software Architectures* (dissertation)
- Arnaud Lauret, *The Design of Web APIs*
- Mike Amundsen, *RESTful Web APIs* and *Design and Build Great Web APIs*
- Sam Newman, *Building Microservices*
- OpenAPI Specification; JSON Schema (as reference standards)
- Martin Kleppmann, *Designing Data-Intensive Applications*
