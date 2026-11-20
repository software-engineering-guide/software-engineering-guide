# 2.1 Kodlama standartları ve üslup

## Genel bakış ve motivasyon

Kodlama standartları, birçok insanın kodu sanki tek bir özenli yazar yazmış gibi yazmasını sağlayan ortak kurallardır. Adlandırmayı, biçimlendirmeyi, dosya düzenini, deyimleri, hata yönetimini ve bir takımın tercih ettiği paradigmaları kapsarlar. Küçük bir takımda bireysel zevk günü kurtarabilir. Büyük bir takımda (yüzlerce ya da binlerce mühendis, birçok yüklenici, yüksek personel devri) tutarsızlık her okumada, her incelemede ve her uyumda ödediğiniz bir vergiye dönüşür. Standartlar, sayısız küçük üslup tartışmasını, bir makinenin sizin için uyguladığı tek seferlik bir karara çevirir.

Büyük kuruluşlar için bahisler somuttur. Kod yazıldığından çok daha sık okunur. Kurumsal ve kamu ortamlarında bir kod satırı, yazarı ayrıldıktan yıllar sonra denetçiler, güvenlik inceleyicileri ve bakımcılar tarafından okunabilir. Tutarlı üslup bu okumanın zihinsel maliyetini düşürür, hata yüzeyini küçültür ve otomatik analizi [linter'lar](https://en.wikipedia.org/wiki/Lint_(software)) (olası hataları ve üslup ihlallerini otomatik işaretleyen araçlar), güvenlik tarayıcıları ve [yeniden düzenleme](https://en.wikipedia.org/wiki/Code_refactoring) araçları genelinde güvenilir kılar. Finansal hizmetler, sağlık, savunma ve kamu sistemleri gibi düzenlemenin geçerli olduğu yerlerde, standartlar ayrıca bir kod tabanının sürdürülebilir ve kontrol altında olduğuna dair kanıtın parçasını oluşturur.

Modern yaklaşım, üslubu süregelen insan yargısına bağlı bir mesele olarak değil, çözülmüş, otomatik bir kaygı olarak ele almaktır. Biçimlendiriciler ve linter'lar editörde, commit öncesi kancalarda ve her değişiklikte çalışan otomatik derleme ve test süreci olan [sürekli entegrasyonda](https://en.wikipedia.org/wiki/Continuous_integration) (CI) çalışır. Makineler üslubu uygular; böylece inceleme dikkatinizi tasarıma ve doğruluğa harcayabilirsiniz. Amaç kendi başına tekdüzelik değildir. Sürtünmenin ortadan kaldırılmasıdır: temelleri yeniden öğrenmeden hizmetler ve takımlar arasında gezinebilmelisiniz.

## Temel ilkeler

- Tutarlılık bireysel tercihi yener; her yerde uygulanan tek bir üzerinde uzlaşılmış üslup, eşitsiz uygulanan "en iyi" üsluptan daha değerlidir.
- Uygulamayı otomatikleştirin. Biçimlendiriciler ve linter'lar doğruluk kaynağıdır; boşluklar hakkındaki kod inceleme yorumları değil.
- İlk yazar için değil, okuyucu ve bakımcı için optimize edin.
- Özel ev kuralları yerine, daha geniş dil topluluğunun zaten kullandığı kuralları tercih edin.
- Standardı benimsemesi kolay kılın: kimsenin okumadığı bir PDF yerine paylaşılan yapılandırmalar, şablonlar ve araçlar sağlayın.
- Üslup kuralları az, savunulabilir ve belirsiz olmayan nitelikte olmalı; her kuralın bir uygulama mekanizması vardır, yoksa yalnızca bir öneridir.
- Adlandırma en yüksek kaldıraçlı okunabilirlik kararıdır ve açık rehberliği hak eder.

## Öneriler

### Dil başına kanonik bir üslup kılavuzu benimseyin

Kullandığınız her dil için, temel olarak geniş kabul görmüş bir üslup kılavuzu benimseyin (örneğin o dilin topluluk ya da tedarikçi kılavuzu) ve yalnızca kuruluşunuzun ihtiyaç duyduğu farkları belgeleyin. Sıfırdan bir ev üslubu icat etmeyin. Seçiminizi merkezi, bulunabilir bir yerde yayımlayın ve onu kod gibi sürümleyin.

### Biçimlendiricileri pazarlık dışı varsayılanlar yapın

Biçimlendiricisi olan her dil için görüşlü bir otomatik biçimlendirici kullanın ve depoya işlenmiş tek bir paylaşılan yapılandırma ile. Biçimlendirme asla incelemede gündeme gelmemelidir, çünkü kaydederken otomatik uygulanır ve CI'de doğrulanır. Bir dilin güçlü bir biçimlendiricisi yoksa tek bir linter yapılandırması seçin ve aynı şekilde ele alın.

### Linter'ları tavsiye değil, uygulanan kapılar olarak çalıştırın

Linter'ları üzerinde uzlaşılmış bir kural kümesiyle yapılandırın, ihlallerde derlemeyi başarısız kılın ve kural kümesini [sürüm kontrolünde](https://en.wikipedia.org/wiki/Version_control) tutun ki değişiklikler incelemeden geçsin. Otomatik düzeltilebilir kuralları (otomatik uygulayın) insan yargısı gerektiren kurallardan (işaretleyin ve engelleyin) ayırın. Yeni kuralları "uyarı" modunda başlatın, birikimi temizleyin, sonra onları "hata"ya yükseltin.

### Birden fazla katmanda uygulayın

Anlık geri bildirim için editör entegrasyonu, yerel uygulama için commit öncesi kancalar ve yetkili kapı olarak CI kontrolleri sağlayın. Bir ihlali ne kadar erken yakalarsanız o kadar ucuzdur. Yerel kancalar atlanabileceği için CI son güvence olmalıdır.

### Adlandırmaya açık kurallar verin

Dil başına büyük/küçük harf kurallarını standartlaştırın, niyeti ortaya koyan isimleri zorunlu kılın, yanıltıcı kısaltmaları yasaklayın ve boolean'lar, koleksiyonlar, birimler ve eşzamansız işlemler için kuralları tanımlayın. Alan sözcük dağarcığınızı paylaşılan bir sözlüğe yazın ki aynı kavram her yerde aynı ada sahip olsun.

### Çok dilli tutarlılığı bilinçli yönetin

Birkaç dile yayılan bir kod tabanında, sözdizimi farklı olsa bile tutarlı kavramları (hata yönetimi kalıpları, günlük yapısı, proje düzeni) hedefleyin. Merkezi bir depodan dil başına yapılandırmalar sağlayın ki yeni bir hizmet standartları şablonlar ya da iskeleler aracılığıyla otomatik miras alsın.

### Deyimleri ve paradigmaları kodlayın

Biçimlendirmenin ötesine geçin. Tercih ettiğiniz deyimleri, örneğin hataların nasıl ele alınacağını, modüllerin nasıl yapılandırılacağını ve istisnalar ile sonuç türlerinin ne zaman kullanılacağını, takımlarınızın tercih ettiği paradigmalarla birlikte yazıya dökün. Gerçek okunabilirlik ve sürdürülebilirlik burada yaşar.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
|---|---|---|
| Sıkı otomatik biçimlendirici, sıfır yapılandırma | Tüm biçimlendirme tartışmasını bitirir; anlık tutarlılık; basit uyum | Bazı beğenilmeyen seçimler pazarlık dışıdır; ilk uygulandığında büyük fark |
| Ev kurallarıyla yapılandırılabilir linter | Kuruluş ihtiyaçlarına göre uyarlanır; gerçek hata önleme kuralları kodlayabilir | Yapılandırma kayması; kural gereksiz tartışması; bakım yükü |
| Topluluk standardının toptan benimsenmesi | Yeni işe alınanlara tanıdık; güçlü araç ekosistemi; düşük bakım | Özel kuruluş kısıtlarına uymayabilir; ara sıra sakar kurallar |
| Özel dahili standart | Kuruluşa tam uyar | Yazması ve sürdürmesi pahalı; işe alınanlara yabancı; zayıf araçlar |
| Takım başına özerklik | Yüksek yerel moral; bağlama özgü | Parçalanma; acı verici takımlar arası hareketlilik; tutarsız araçlar |

Uygulanan varsayılanlar, küçük bir bireysel özerkliği büyük kolektif kazançlarla takas eder: daha az inceleme sürtünmesi, daha hızlı uyum ve güvenilir otomasyon. Ana risk, standardı gerçek kusurları önlemeden herkesi yavaşlatan yüzlerce kurala aşırı mühendislik yapmaktır. Kural kümesini küçük ve kanıta dayalı tutun ve bakımın ucuz kalması için mevcut bir standardı benimsemeye yönelin.

## Takımınızla tartışılacak sorular

1. **Hangi linter kuralları derlemeyi başarısız kılmalı ve herkesi durdurmadan bir kuralı uyarıdan hataya nasıl yükseltirsiniz?** Bu bölüm her kuralın bir uygulama mekanizmasına ihtiyacı olduğunu ve yeni kuralların uyarı modunda yer almasını, birikimlerinin temizlenmesini, sonra hataya çevrilmesini savunur. Büyük bir takımda, kirli bir kod tabanına karşı bir kuralı hataya çevirmek bir gecede yüzlerce ilgisiz değişikliği engeller. Toplantıya sağlam kanıt getirin: her aday kural için mevcut ihlal sayısı ve otomatik düzeltilebilir mi yoksa insan yargısı mı gerektirdiği. Kurumsal ve kamu ortamlarında geçti/kaldı çizgisi aynı zamanda denetim kapılarını da besler, bu yüzden belirsiz bir kural kümesi uyum hikayenizi zayıflatır. Aşamalı bir dağıtıma karar verin: yapabildiğinizi otomatik düzeltin, temizliği bütçeleyin, sonra kapı koyun.

2. **Mevcut kodunuza ilk kez bir biçimlendirici uyguladığınızda, bu yeniden biçimlendirmenin git blame'i bozmasını ve incelemeleri boğmasını nasıl önleyeceksiniz?** Ödünleşim tablosu büyük bir ilk farkı uyarır ve anti-kalıplar bölümü yeniden biçimlendirme commit'lerini mantık değişiklikleriyle karıştırmayı gösterir. Tek bir kapsamlı yeniden biçimlendirme binlerce satırı yeniden yazar ve blame'i gerçek yazar yerine yeniden biçimlendirmeye işaret ettirir; bu, yıllar sonra hata ayıklayan herkese zarar verir. Yeniden biçimlendirmeyi tek, izole, açıkça etiketlenmiş bir commit olarak yapın ve geçmiş yararlı kalsın diye onu bir blame-yoksay dosyasına kaydedin. Kimin neyi değiştirdiğini izleyen denetçiler için bu izolasyon, temiz kanıt ile gürültü arasındaki farktır. Kodlara dokunmadan önce, sonra değil, sıralama üzerinde anlaşın.

3. **Adlandırma sözlüğünüzün ve alan sözcük dağarcığınızın sahibi kim ve yeni bir terim nasıl eklenir?** Bölüm adlandırmayı en yüksek kaldıraçlı okunabilirlik kararı olarak adlandırır ve alan sözcük dağarcığını paylaşılan bir sözlüğe yazmanızı ister. Adı konmuş bir sahip olmadan aynı kavram takımlar arasında üç farklı ad kazanır ve statik analiz ve arama araçları güvenilirliğini kaybeder. Somut sinyal olarak kod tabanınızda zaten çakışan adları olan kavramlara örnekler getirin. Bir sahip ve hafif bir öneri yolu atayın ki bir terimi eklemek ya da yeniden adlandırmak her çekme isteğinde bir tartışma değil, küçük, incelenen bir değişiklik olsun. Cevap uyumu değiştirir: yeni bir işe alınan tutarsız koddan niyeti tersine mühendislikle çözmek yerine tek bir sözlük okur.

4. **Her dil için tanınmış bir topluluk ya da tedarikçi üslup kılavuzunu toptan mı benimsiyorsunuz ve ev farkları gerçekte nerede haklı?** Bu bölüm, mevcut bir standardı temel olarak almanızı ve yalnızca kuruluşunuzun ihtiyaç duyduğu farkları belgelemenizi savunur, çünkü özel bir standardı yazmak pahalıdır ve işe alınanlara yabancıdır. Karşıt çekim gerçektir: dahili bir kısıt (bir güvenlik kuralı, eski bir çerçeve, bir erişilebilirlik yetkisi) bazen topluluk varsayılanıyla gerçekten çatışır ve tuttuğunuz her fark, artık sonsuza kadar sahip olduğunuz ve sürdürdüğünüz bir kuraldır. Önerilen fark listesini toplantıya getirin; her birini onu motive eden somut kısıtla birlikte ve yalnızca zevk olan herhangi bir farkı kesmeye hazır olun. Kurumsal ve kamu ortamlarında, daha geniş dil topluluğuyla eşleşen bir temel, yüklenicilerin ve yeni tedarikçilerin zaten akıcı gelmesi anlamına da gelir; bu uyumu kısaltır ve denetçilerin aradığı sürdürülebilirlik kanıtını güçlendirir.

5. **Çok dilli bir kod tabanında hangi kurallar gerçekten evrensel ve hangileri dile yerel kalıyor ve depo başına yapılandırmaların kaymasını nasıl önlersiniz?** Bölüm, sözdizimi farklı olsa bile diller boyunca tutarlı kavramlar (hata yönetimi, günlük yapısı, proje düzeni) ve yeni hizmetlerin standartları otomatik miras alması için merkezi bir depodan sunulan dil başına yapılandırmalar ister. Gerilim, bir dilin deyimlerini diğerine zorlamanın sakar, deyimsel olmayan kod üretmesi, her takımı kendi yapılandırmasını çatallamaya bırakmanın ise "standart"ın hiçbir şey ifade etmemesiyle sonuçlanmasıdır. Somut sinyal olarak depo başına mevcut linter ve biçimlendirici yapılandırmalarınızın bir envanterini ve zaten ne kadar uzaklaştıklarını gösteren bir farkı getirin. Onlarca hizmet işleten büyük bir kuruluş için dağıtım mekanizmasına (şablonlar, iskeleler, paylaşılan bir yapılandırma paketi) karar verin ki bir kural değişikliği her depoya elle kopyalanmak yerine bir kez yayılsın.

6. **Bir kuralı devre dışı bırakmak ne zaman meşru, bastırmayı kim inceliyor ve toptan devre dışı bırakmaların standardı içten boşaltmasını nasıl önlersiniz?** Anti-kalıplar bölümü yaygın satır içi bastırmaları kuralın yanlış olduğunun ya da takımın pes ettiğinin işareti olarak gösterir, yine de katı bir istisnasız politika insanları sırf linter'ı tatmin etmek için daha kötü kod yazmaya iter. Hafif bir yol üzerinde anlaşın: bir bastırma bir gerekçe taşımalı, mümkün olan en dar kapsamda durmalı ve küresel bir yoksay dosyasına gömülmek yerine incelemede görünür olmalıdır. Kural ve depo başına mevcut bastırma sayısını getirin, çünkü yüzlerce kez bastırılmış bir kural, koddan çok kuralla ilgili bir şey söylüyordur. Düzenlemeye tabi ve kamu işlerinde açıklanmamış toptan bastırmalar denetim hikayesini doğrudan zayıflatır, çünkü hat artık birleştirilen kodun üzerinde uzlaşılan kapıları gerçekten geçtiğini gösteremez.

## Sektör merceği

**Girişim.** Hız kazanır, bu yüzden tek diliniz için topluluk biçimlendiricisi ve linter varsayılanlarını ilk günden benimseyin ve ikinci mühendis gelmeden önce bir commit öncesi kancaya ve CI'ye bağlayın. Sürdürmeye vaktiniz olmayan bir ev üslubu yazmayın: depoda gönderilen yapılandırma standardın tamamıdır. İkinci bir dil eklediğinizde, sıfırdan kural icat etmek yerine o dilin kanonik kılavuzuna uzanın.

**Küçük işletme.** Özel bir araç uzmanı ve sıkı bir bütçe olmadan tümüyle dilinizle birlikte gelen ya da yanında duran ücretsiz, görüşlü biçimlendiriciye yaslanın ve ayarlamak yerine varsayılanlarını kabul edin. Bu net bir inşa etmek yerine satın alma durumudur: özel bir kural kümesini sürdürmek sahip olmadığınız zamana mal olurken, hazır bir biçimlendirici hiçbir şeye mal olmaz ve üslup tartışmasını hemen bitirir. Yapılandırmayı depoda tutun ki gelecek yıl tutacağınız tek yüklenici onu bir konuşma olmadan miras alsın.

**Kurumsal.** Ölçekte iş birçok takım arasında yönetişimdir: dil başına paylaşılan biçimlendirici ve linter yapılandırmalarını tutan merkezi bir mühendislik standartları deposu, bu yapılandırmaları çeken şablonlardan üretilen yeni hizmetler ve uyumsuz birleştirmeleri engelleyen CI kapıları. Kural kümesini kod gibi sürümleyin ve değişiklikleri periyodik bir incelemeden geçirin ki standartlar sürüklenmek yerine bilinçli evrilsin. Getiri, mühendislerin takımlar arasında tanıdık koda geçmesi ve her depo tutarlı olduğu için güvenilir sinyal üreten otomatik araçlardır.

**Kamu.** Tedarik ve hesap verebilirlik seçimi biçimlendirir: belirli bir üslubu ve güvenlik kural kümesini çalışma yetkisi gereksinimlerinin parçası olarak zorunlu kılın ve hattın birleştirilen her değişikliğin üzerinde uzlaşılan kapıları geçtiğini gösteren bir raporu denetim kanıtı olarak üretmesini sağlayın. Bir biçimlendirici otomatik uygulandığı için birden fazla tedarikçi ve yüklenicinin kodu tutarlı görünür; bu, sözleşmeler bittikten çok sonra kamusal bakım işini korur. Standart şeffaf olsun ve herhangi bir gelecek tedarikçi onu özel kilitlenme olmadan benimseyebilsin diye özel kurallar yerine tanınmış topluluk temellerini tercih edin.

## Örnekler

**Girişim.** Dört kişilik bir girişim, tek diliyle ilgili topluluk biçimlendiricisi ve linter varsayılanlarını ilk günden benimser ve onları commit öncesi kancaya ve CI'ye bağlar; böylece kimse incelemede boşluk hakkında tartışmaz. Yapılandırma deponun içinde gönderildiği için beşinci ve altıncı işe alınanlar onu otomatik miras alır ve hiç biçimlendirme yorumu görmez. Takım daha sonra ikinci bir dil eklediğinde, sürdürmeye vakitleri olmayan bir ev üslubu icat etmek yerine o dilin standart kılavuzuna uzanır.

**Kurumsal.** Büyük bir banka onlarca takım boyunca Java, Python ve TypeScript ile hizmetler işletir. Her dil için paylaşılan biçimlendirici ve linter yapılandırmalarını tutan merkezi bir "mühendislik standartları" deposu yayımlar. Yeni hizmetler bu yapılandırmaları çeken bir şablondan üretilir, böylece her depo uyumlu başlar. CI herhangi bir ihlalde birleştirmeleri engeller ve üç ayda bir yapılan inceleme kural değişikliklerini yönetir. Her depo tanıdık göründüğü için takımlar arasında geçen mühendislerin uyum süresi gözle görülür biçimde düşer.

**Kamu.** Eski bir sistemi modernize eden bir kamu kurumu, çalışma yetkisi (ATO) gereksinimlerinin, yani sistemi üretimde çalıştırmak için gereken resmi onayın parçası olarak bir erişilebilirlik ve güvenlik linter kural kümesini zorunlu kılar. Üslup uyumu denetim kanıtının parçası olur: hat, birleştirilen tüm kodun üzerinde uzlaşılan [statik analiz](https://en.wikipedia.org/wiki/Static_program_analysis) kapılarını geçtiğini gösteren bir rapor üretir. Bir biçimlendirici otomatik uygulandığı için birden fazla tedarikçiden yükleniciler görsel olarak tutarlı kod üretir; bu, sözleşmeler bittikten sonra hükümetin uzun vadeli bakım işini kolaylaştırır.

## İş gerekçesi: motivasyonlar, YG ve TSM

Standartları benimsemenin maliyeti çoğunlukla bir kereliktir: kılavuzları seçmek, araçları bağlamak ve bir büyük ilk yeniden biçimlendirme commit'i uygulamak. Yinelenen maliyet düşüktür, çünkü uygulama otomatiktir. Standartları benimsememenin maliyeti yinelenen ve bileşiktir: her inceleme üsluba dakikalar harcar, her uyum daha yavaştır, statik analiz araçları gürültü üretir ve tutarsız kod hataları gizler. Büyük bir kuruluş genelinde bu dakikalar tam zamanlı eşdeğer kayıplara toplanır.

Getiri azalan inceleme gecikmesi, daha az üslupla ilgili inceleme yorumu, daha hızlı uyum ve otomatik araçlardan daha yüksek sinyal olarak görünür. Düzenlemeye tabi ortamlarda denetim hazırlığında ek bir getiri vardır: gösterilebilir, uygulanan kontroller uyum incelemelerinin çabasını ve riskini azaltır. Liderliğe gerekçeyi sunmak için standartları geliştirici verimliliği ve denetim duruşu üzerinde düşük maliyetli, yüksek kaldıraçlı bir kaldıraç olarak çerçeveleyin ve inceleme yorumu analizi ve uyum anketi verileriyle tutarsızlığın mevcut maliyetine bir sayı koyun.

## Anti-kalıplar ve tuzaklar

- **Kod incelemesinde tartışılan üslup:** uygulamanın otomatik olmadığının işareti; kuralı araçlara taşıyın.
- **Okunmayan standart belgesi:** uygulaması olmayan bir wiki sayfası süstür; her kuralın bir mekanizmaya ihtiyacı vardır.
- **Kural çoğalması:** kusurları önlemeden işi yavaşlatan yüzlerce titiz kural.
- **Yapılandırma kayması:** her depo, "standart" hiçbir şey ifade etmeyene kadar kendi linter yapılandırmasını çatallar.
- **Özellik işinin ortasında tüm depoyu biçimlendirmek:** yeniden biçimlendirme commit'lerini mantık değişiklikleriyle karıştırmak incelemeyi ve blame'i yok eder; büyük yeniden biçimlendirmeleri izole, açıkça etiketlenmiş commit'lerde yapın.
- **Toptan bastırmalarla linter'ı görmezden gelmek:** yaygın satır içi devre dışı bırakmalar yanlış bir kuralın ya da pes etmiş bir takımın işaretidir.
- **Sahipliksiz standartlar:** net sahibin olmaması kuralların hiç evrilmeyip çürümesi demektir.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Üslup yazar başınadır ve reaktiftir; paylaşılan yapılandırma yoktur; biçimlendirme incelemede tartışılır ve o gün en çok umursayan kişi tarafından karara bağlanır.
- **Düzey 2, Geliştirme:** Tek tek takımlar bir biçimlendirici ve linter benimser, ama yapılandırmalar ve kural kümeleri takımdan takıma ve depodan depoya değişir; böylece tutarlılık her takımın sınırında durur.
- **Düzey 3, Standartlaştırma:** Dil başına merkezi paylaşılan yapılandırmalar belgelenir ve kuruluş genelinde uygulanır; CI uyumsuz birleştirmeleri engeller; yeni depolar standartları şablonlar ya da iskeleler aracılığıyla otomatik miras alır.
- **Düzey 4, Yönetme:** Standart verilerle ölçülür ve kontrol edilir: ihlal oranları, bastırma sayıları, üslupla ilgili inceleme yorumları ve uyum süresi temel çizgilere karşı izlenir ve kural değişiklikleri görüş yerine bu kanıtla yükseltilir ya da emekliye ayrılır.
- **Düzey 5, Orkestrasyon:** Standartlar sürekli iyileştirilir ve kuruluş genelinde bütünleşir; çok dilli deyimler ve alan sözcük dağarcığı belgelenir ve uygulanır, uygulama neredeyse sürtünmesizdir ve kural kümesi diller, araçlar ve kuruluş ihtiyaçları kaydıkça uyum sağlar.

## Tartışma fikirleri

- Uygulanan bir kural ile mühendis muhakemesine güvenen belgelenmiş bir yönerge arasındaki çizgi nerede?
- Kuruluş, gerçek bir dahili kısıtla çatışan sevilen bir topluluk kuralını nasıl ele almalı?
- Standartların sahibi kim ve kural değişiklikleri aksaklık olmadan nasıl önerilir, tartışılır ve yayılır?
- Çok dilli bir kod tabanında hangi kurallar gerçekten evrensel olmalı ve hangileri dile yerel kalmalı?
- Standartları büyük bir eski kod tabanına, aksatıcı bir büyük patlama yeniden biçimlendirmesi olmadan nasıl uygularsınız?
- Yapay zeka destekli araçlar, mekanik biçimlendirmenin ötesinde deyimleri önermede ya da uygulamada hangi rolü oynamalı?

## Önemli çıkarımlar

- Üslubu otomatik, çözülmüş bir sorun olarak ele alın ki insanlar tasarımı ve doğruluğu incelesin.
- Mevcut topluluk standartlarını benimseyin ve yalnızca farkları belgeleyin.
- Editörde, commit öncesinde ve CI katmanlarında uygulayın; CI yetkili kapı olsun.
- Kural kümesini küçük, savunulabilir ve merkezi olarak yönetilen tutun.
- Okunabilirliğin gerçekten kazanıldığı yer boşluk değil, adlandırma ve deyimlerdir.

## Kaynaklar ve ileri okuma

- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Steve McConnell, *Code Complete*
- Dustin Boswell and Trevor Foucher, *The Art of Readable Code*
- Kevlin Henney (ed.), *97 Things Every Programmer Should Know*
- Google, *Google Engineering Practices* and language style guides (as reference exemplars)
