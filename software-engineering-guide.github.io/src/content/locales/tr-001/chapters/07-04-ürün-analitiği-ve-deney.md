# 7.4 Ürün analitiği ve deney

## Genel bakış ve motivasyon

Ürün analitiği, insanların bir ürünü gerçekte nasıl kullandığını davranışlarını yakalayıp çözümleyerek anlama pratiğidir: hangi özelliklere dokunuyorlar, nerede başarılı oluyorlar, nerede bırakıp gidiyorlar ve onları neyin geri getirdiği. Deney, kontrollü denemeler yürüterek neden-sonuç ilişkisini kanıtlama disiplinidir; en yaygın biçimi [A/B testleridir](https://en.wikipedia.org/wiki/A/B_testing) (iki varyantın rastgele atanmış, yüz yüze karşılaştırması). Böylece ürün değişikliklerini görüşlere ya da sezgiye göre değil, gerçek etkilerine göre yargılarsınız. İkisi birlikte ürün kararlarını "bence"den "biliyoruz"a, en azından "ölçtük"e taşır.

Büyük takımlar için bu pratikler belirleyicidir. Düzinelerce squad milyonlarca kişinin kullandığı bir ürüne değişiklik yayınladığında, yönlendirilmemiş sezgi net etkisini kimsenin ölçemediği bir değişiklik akışı üretir ve verinin çözmesi gereken tartışmaları en yüksek sesli kişi kazanır. Kurumlar gelir ve dönüşümü ölçekte korumak, zararlı değişiklikleri tam yayından önce yakalamak için deney kullanır. Kamu dijital hizmetleri de temel hizmetlerin (yardım başvuruları, vergi beyanı, ruhsat yenileme) kullanımını ve tamamlanma oranını artırmak için giderek aynı yöntemleri kullanıyor; tamamlanma oranındaki küçük bir iyileşme, vatandaş çıktılarında büyük kazanımlara ve çağrı merkezi yükünde azalmaya dönüşür.

Ürün analitiğinin değeri tümüyle enstrümantasyonun kalitesine ve çözümlemenin titizliğine bağlıdır. Özensiz olay izleme kimsenin güvenmediği veri üretir. Kötü yürütülen deneyler kendinden emin ama yanlış sonuçlar üretir. Üstelik bu veri davranışsal ve çoğu zaman kişisel olduğundan, onu gizliliğe saygılı ve onamı gözeten biçimde toplamalısınız; bu birçok yargı bölgesinde yasal bir zorunluluk, her yerde etik bir yükümlülüktür. Bu bölüm enstrümantasyonu, temel davranışsal çözümlemeleri, titiz deneyi, önemli metrikleri seçmeyi ve tüm bunları saygılı biçimde yapmayı ele alır.

## Temel ilkeler

- Belgelenmiş bir izleme planı ve tutarlı bir sınıflandırmayla bilinçli biçimde enstrümante edin.
- Nedensel sorularda görüşler yerine kontrollü deneyleri tercih edin.
- İstatistiksel titizlik pazarlık konusu değildir; yetersiz güçlü ya da gözetlenen testler yanıltır.
- Boş gösterişli sayılara değil, gerçek değere bağlı bir kuzey yıldızı metriğine demir atın.
- Yalnızca edinimi değil, [elde tutmayı](https://en.wikipedia.org/wiki/Customer_retention) ve etkileşimi de ölçün.
- Gereken en az davranışsal veriyi, açık onamla toplayın.
- Enstrümantasyonu sahipleri ve kalite kontrolleri olan bir ürün gibi ele alın.
- Olumsuz ya da düz çıkan bir deney sonucu bir başarısızlık değil, değerli bir bulgudur.

## Öneriler

### İzleme planı ve sınıflandırmayla enstrümante edin

Olay eklemeden önce bir izleme planı tasarlayın: yakalayacağınız olaylar, özellikleri, adlandırma kuralları ve her birinin yanıtladığı sorular. Verinin takımlar ve zaman boyunca çözümlenebilir kalması için tutarlı bir sınıflandırma (olaylar ve özellikler için kararlı bir adlandırma düzeni) uygulayın. İzleme planını yönetilen bir şema gibi ele alın: sürümleyin, değişiklikleri gözden geçirin ve olayları ona göre doğrulayın; böylece hatalı ya da beklenmedik olayları aylar sonra boşluk olarak keşfetmek yerine alım anında yakalarsınız. Bu disiplin olmadan ürün verisi tutarsız, yinelenmiş ve belgelenmemiş olaylardan oluşan kullanılamaz bir karmaşaya dönüşür.

### Hunileri, kohortları, elde tutmayı ve etkileşimi çözümleyin

Kullanıcıların kilit akışlarda nerede bıraktığını görmek ve iyileştirmeleri hedeflemek için hunileri kullanın. Ne zaman katıldıklarına ya da ne yaptıklarına göre tanımlanan grupları karşılaştırmak için [kohort çözümlemesini](https://en.wikipedia.org/wiki/Cohort_analysis) kullanın; bu, değişikliklerin davranışı zaman içinde gerçekten iyileştirip iyileştirmediğini ortaya koyar. Elde tutmayı ölçün (kullanıcılar geri geliyor mu), çünkü elde tutma olmadan edinim delik bir kovadır. Etkileşimi dürüstçe tanımlayın: gösterişli sayılar yerine anlamlı bir etkin kullanıcı tanımı kullanın. Temiz enstrümantasyona dayanan bu çözümlemeler size üründe gerçekte neler olduğunu söyler.

### Titiz deneyler yürütün

Nedensel sorular için kontrollü deneyler yürütün: kullanıcıları rastgele varyantlara atayın ve sonuçları karşılaştırın. Titizlik birkaç disiplin gerektirir. Başlamadan önce yeterli [istatistiksel güç](https://en.wikipedia.org/wiki/Power_%28statistics%29) için gereken örneklem büyüklüğünü ve süreyi hesaplayın. Bir sonuç anlamlı göründü diye erken durmayın: gözetleme yanlış pozitifleri şişirir. Birincil metriğinizi ve hipotezinizi önceden belirleyin; böylece birçok metrik arasında anlamlı çıkan herhangi birini avlamaktan kaçınırsınız. Rastgele atamanın sağlam olduğunu ve koruma metriklerinin (performans, gelir, şikayetler) zarar görmediğini kontrol edin. Atamayı, çözümlemeyi ve koruma metriklerini standartlaştırmak için bir deney platformu kullanın; böylece her takım istatistiği kötü biçimde yeniden icat etmek yerine sağlam testler yürütür.

### Bir kuzey yıldızı metriği seçin ve gösterişli metriklerden kaçının

Ürününüzün kullanıcılara sunduğu çekirdek değeri yakalayan ve büyüdüğünde gerçek başarıya işaret eden tek bir kuzey yıldızı metriği seçin; karşılığında değer olmadan yükselen gösterişli bir sayı olmasın. Toplam kayıtlı kullanıcı, ham sayfa görüntüleme ve birikimli indirme sayıları klasik gösterişli metriklerdir: yalnızca yukarı çıkarlar ve sağlığı nadiren yansıtırlar. Sunulan ve elde tutulan değere bağlı metrikleri tercih edin ve kuzey yıldızının çevresine takımların gerçekten etkileyebileceği küçük bir girdi metriği kümesi koyun. Bir vekili o kadar çok eniyilemekten sakının ki gerçek hedefe zarar verirsiniz.

### Gizliliğe ve onama saygı gösterin

Davranışsal veri kişisel veridir. Yalnızca tanımlı bir amaç için gerekeni toplayın, yasanın gerektirdiği şekilde onam alın ve onuru gözetin, kullanıcılara şeffaflık ve denetim verin. Yeterli olduğu yerde toplu ve takma adlandırılmış çözümlemeyi tercih edin, saklamayı en aza indirin ve her hassas veri kümesine uyguladığınız yönetişim, sınıflandırma ve erişim denetimlerini uygulayın. Gizliliğe saygı, [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) (AB'nin Genel Veri Koruma Tüzüğü) gibi rejimleri karşılamaktan fazlasını yapar: ürünün dayandığı kullanıcı güvenini sürdürür. Analitiği, izlenmeyi reddeden bir kullanıcının yine de çalışan bir ürün alacağı biçimde tasarlayın.

### Enstrümantasyonu ve deneyleri ürün olarak ele alın

Enstrümantasyona kalitesinden, kapsamından ve belgelenmesinden sorumlu bir sahip verin; bozuk ya da eksik olayları boru hatlarını izlediğiniz gibi izleyin. Paylaşılan bir platform, deney tasarımının gözden geçirilmesi ve geçmiş sonuçların bir deposuyla bir deney kültürü kurun; böylece kuruluş testleri tekrarlayıp sonuçları unutmak yerine birikimli olarak öğrenir.

## Ödünleşimler: artılar ve eksiler

| Seçim | Artılar | Eksiler | En uygun |
|---|---|---|---|
| Yoğun enstrümantasyon | Zengin davranışsal içgörü | Maliyet, gizlilik maruziyeti, gürültü | Veriye dayalı ürünler |
| Asgari enstrümantasyon | Ucuz, düşük gizlilik riski | Kör noktalar, zayıf çözümleme | Erken ya da düşük riskli ürünler |
| A/B deneyi | Nedensel kesinlik, metrikleri korur | Trafik, zaman, titizlik ister | Yüksek trafikli ürünler |
| Yayınla ve gözle | Hızlı, trafik eşiği yok | Karıştırılmış, nedensellik yok | Düşük trafikli ya da geri alınabilir değişiklikler |
| Kuzey yıldızı odağı | Uyum, net öncelikler | Aşırı basitleştirir, oyunlanma riski | Çoğu ürün takımı |
| Çok sayıda KPI | İnce ayrım | Dağınık odak, çelişen hedefler | Olgun analitik kuruluşlar |

Merkezi ödünleşim, trafiğin aracılık ettiği hız ile kesinlik arasındadır. Deneyler nedensel kesinlik verir ama istatistiksel güce ulaşmak için yeterli kullanıcı ve yeterli sabır gerektirir. Düşük trafikli özelliklerde ya da açıkça geri alınabilir değişikliklerde disiplinli yayınla ve gözle pragmatik olabilir. Enstrümantasyon içgörüyü maliyet ve gizlilik maruziyetiyle takas eder; bu yüzden istif yapmak yerine amaçlı toplayın. Kuzey yıldızı metriği ise ince ayrımı uyumla takas eder: odak için güçlüdür, oyunlanırsa tehlikelidir, bu yüzden onu koruma metrikleriyle eşleştirin.

## Takımınızla tartışılacak sorular

1. **İzleme planınızın sahibi kim ve olayları alım anında ona göre doğruluyor musunuz, böylece hatalı veri aylar sonra boşluk olarak ortaya çıkmak yerine hızlı başarısız oluyor mu?** Bölüm izleme planını yönetilen bir şema olarak ele alır: sürümlenmiş, gözden geçirilmiş ve doğrulanmış; verinin takımlar ve zaman boyunca çözümlenebilir kalması için tutarlı bir sınıflandırmayla. Bu disiplin olmadan ürün verisi tutarsız, yinelenmiş ve belgelenmemiş olaylardan oluşan kullanılamaz bir karmaşaya bozulur ve boşlukları ancak bir soruyu yanıtlamaya çalıştığınızda keşfedersiniz. Düzinelerce squad'ın ve milyonlarca kullanıcının dokunduğu bir ürün için sahipsiz bir izleme planı, her takımın olayları farklı adlandırması ve hiçbir takımlar arası çözümlemenin tutmaması demektir. Kanıt getirin: kilit bir huni seçin ve olaylarının belgelenmiş ve tutarlı adlandırılmış olup olmadığını kontrol edin. Sahiplik belirsizse atayın ve bozuk ya da eksik olayları boru hatlarını izlediğiniz gibi izleyin.

2. **Tüm takımlarınız deneyleri güç hesapları ve koruma metrikleri olan paylaşılan bir platform üzerinden mi yürütüyor, yoksa her biri istatistiği kötü biçimde yeniden mi icat ediyor?** Bölüm titizliğin pazarlık konusu olmadığı konusunda açıktır: başlamadan önce yeterli istatistiksel güç için örneklem büyüklüğünü ve süreyi hesaplayın, birincil metriği ve hipotezi önceden belirleyin, gözetleyip erken durmayın ve performans, gelir ve şikayetler gibi koruma metriklerini izleyin. Paylaşılan bir deney platformu atamayı, çözümlemeyi ve koruma metriklerini standartlaştırır; böylece her squad anlamlı görünen bir şey çıkana kadar gözetlemek yerine her takım sağlam testler yürütür. Yüksek trafikli kurumsal ürünlerde, önlenen tek bir kötü yayın (elde tutmaya sessizce zarar veren bir yeniden tasarım) tüm programın maliyetini karşılayabilir. Bir sinyal getirin: takımlar şu anda güç hesaplıyor mu, yoksa sonuç iyi göründüğünde mi duruyor? İkincisiyse çözüm ortak bir platform ve tasarım incelemesidir.

3. **Ürününüz izlenmeyi reddeden bir kullanıcı için nasıl çalışıyor ve tanımlı bir amaç için yalnızca gereken en az davranışsal veriyi mi topluyorsunuz?** Bölüm davranışsal veriyi kişisel veri olarak ele alır: yalnızca tanımlı bir amacın gerektirdiğini toplayın, yasanın gerektirdiği şekilde onam alın ve onuru gözetin, saklamayı en aza indirin ve her hassas veri kümesindeki sınıflandırma ve erişim denetimlerini uygulayın. Buna saygı göstermek ürünün dayandığı kullanıcı güvenini sürdürür ve GDPR ile benzer rejimler altında bir nezaket değil, yasal bir zorunluluktur. Karşıt baskı, daha zengin içgörü için yoğun enstrümantasyon yapma dürtüsüdür; bu maliyeti, gürültüyü ve gizlilik maruziyetini artırır. Kanıt getirin: topladıklarınızı listeleyin, her olayı yanıtladığı bir soruya bağlayın, sonra izlenmeyi reddetmenin yine de çalışan bir ürün verdiğini kontrol edin. Bazı toplamanın amacı yoksa ya da deneyimi bozuyorsa kesin ve analitiği, vazgeçen kullanıcılar için zarifçe bozulacak biçimde tasarlayın.

4. **Ürününüzün sunduğu değeri hangi tek kuzey yıldızı metriği yakalıyor ve gerçek hedef zarar görene kadar takımların vekili oyunlamasını nasıl engelliyorsunuz?** Kuzey yıldızı metriği birçok takımı tek bir başarı tanımında hizalar; ancak bölüm, fazla eniyilenen bir vekilin temsil etmesi gereken hedefe zarar verebileceği ve toplam kayıtlı kullanıcı ya da birikimli indirme gibi gösterişli sayıların sağlığı yansıtmadan yalnızca tırmandığı konusunda uyarır. Düzinelerce squad'ın her birinin kendi hedefinin peşinde olduğu büyük bir kuruluşta, belirsiz ya da oyunlanabilir bir kuzey yıldızı, toplamı gerçek bir iyileşme etmeyen yerel kazanımlar ya da daha kötüsü kimsenin fark etmediği sessiz zarar üretir. Mevcut kuzey yıldızı adayını, takımların gerçekten etkileyebileceği küçük girdi metriği kümesini ve oyunlamayı yakalayacak koruma metriklerini getirin; sonra raporlanan her metriği, kullanıcılar daha kötü durumdayken yükselip yükselemeyeceğini sorarak sınayın. Başlık metriğinin bütçeyi ve kamuya raporlamayı yönlendirebildiği kurumsal ve kamu ortamlarında, kuzey yıldızını elde tutulan değer ya da tamamlanmış çıktı tanımına bağlayın; böylece kimse hiç dönüşmeyen kayıtların ya da tıklamaların peşinden giderek onu şişiremez.

5. **Düşük trafikli özelliklerde, disiplinli bir yayınla ve gözle ile tam bir kontrollü deney arasındaki dürüst çizgi nerede ve kim karar veriyor?** Deneyler nedensel kesinlik verir ama istatistiksel güce ulaşmak için yeterli kullanıcı ve sabır gerektirir; ince trafikli bir akışa yetersiz güçlü bir test zorlamak, aradığı etkiyi saptayamayan bir sonuç için haftaları yakar. Karşıt risk, yayınla ve gözlemenin karıştırılmış olması ve nedenselliği hiçbir şekilde kanıtlamamasıdır; onu deneyle eşdeğer saymak takımların aslında mevsimselliğin ya da eşzamanlı bir değişikliğin eseri olan kazanımları sahiplenmesine izin verir. Söz konusu akışın trafik ve dönüşüm hacmini, önem verdiğiniz asgari saptanabilir etkiyi ve değişikliğin geri alınabilirliğini getirin, sonra bir kural kararlaştırın: bir trafik eşiğinin üstünde deney, altında net koruma metrikleriyle yayınla ve gözle. Geliri koruyan kurumsal ürünler ve bir gerilemenin vatandaşlara zarar verdiği kamu hizmetleri için, bir deneyden muaf tutma yetkisini kimin elinde tuttuğunu belirleyin ve geri alınabilir değişikliklerin gerçekten geri alınabilir kalmasını isteyin; böylece kötü bir yayınla ve gözle hızla geri çekilebilir.

6. **Olumsuz ve düz deney sonuçlarını paylaşılan bir depoya kaydediyor musunuz, yoksa kuruluş aynı çıkmaz sokakları yeniden mi keşfediyor?** Bölüm, düz ya da olumsuz bir sonucun başarısızlık değil değerli kanıt olduğunu açıkça söyler; yine de aranabilir bir sonuç deposu olmadan ders buharlaşır ve başka bir takım bir yıl sonra aynı kaybeden testi yeniden çalıştırır. Büyük bir kuruluşta bu birikir, çünkü birikimli öğrenme bir deney kültürünün bütün getirisidir ve yalnızca deney tasarımları ve sonuçları bir sonraki takımın bulacağı yere yazıldığında birikir. Geçen çeyrekte çalıştırılan deney sayısını, kaç sonucun belgelenmiş ve bulunabilir olduğunu ve yeni bir test tasarlamadan önce depoyu gerçekten kontrol eden olup olmadığını getirin. Kurumsal ve kamu ortamlarında kalıcı bir kayıt aynı zamanda denetime ve hesap verebilirliğe hizmet eder; bir kararın görüşe değil kanıta dayandığını gösterir ve kamuya dönük bir değişiklik sorgulandığında gözden geçirenlere savunulabilir bir iz verir.

## Sektör merceği

**Girişim.** Başka bir şey eklemeden önce etkinleştirme ve ilk oturum olaylarınız için tek sayfalık bir izleme planı yazın; böylece takım büyürken en erken veri temiz kalır. Gerçek A/B testlerini en yüksek hacimli akışınıza saklayın, başka yerlerde dikkatli yayınla ve gözle kullanın, bir tane kurmak yerine barındırılan bir analitik ve deney aracı satın alın ve etkinleştirme gibi tek bir kuzey yıldızı metriğine bağlı kalın. Yalnızca canlı bir soruyu yanıtlayan olayları toplayın; böylece hiç okumadığınız veri için depolama maliyeti ya da gizlilik riski ödemezsiniz.

**Küçük işletme.** Ayrılmış bir analistiniz ve dar bir bütçeniz yokken, zaten kullandığınız araçlara gömülü analitiğe yaslanın ve deneyi sürekli bir program değil, ara sıra yapılan yüksek değerli bir çalışma olarak ele alın. Seçim genellikle kurmak yerine satın almaktır: gömülü bir huni ve kohort görünümü, bakımını yapamayacağınız özel bir boru hattından iyidir. Yürüttüğünüz az sayıdaki testi geliri yönlendiren tek akışa odaklayın ve onamı basit ve dürüst biçimde ele alın; böylece izlenmeyi reddeden bir müşteri yine de çalışan bir ürün alır.

**Kurumsal.** Birçok takım arasında ölçekte sorun yönetişimdir: alım anında doğrulanan sürümlü bir izleme planı, atamayı, güç hesaplarını ve koruma metriklerini standartlaştıran paylaşılan bir deney platformu ve squad'ların testleri tekrarlamak yerine birikimli öğrenmesi için bir sonuç deposu. Enstrümantasyona bir boru hattı gibi izlenen adlı bir sahip verin, etkilenebilir girdilerle çevrili tek bir kuzey yıldızı metriği üzerinde anlaşın ve davranışsal veriye her hassas veri kümesiyle aynı veri sınıflandırması ve erişim denetimlerini, sonuçları etkileyen yayın kararları için denetim izleriyle birlikte uygulayın.

**Kamu.** Satın alma kuralları, şeffaflık ve kamusal hesap verebilirlik her seçimi şekillendirir. Tanımlı bir amaç için gereken en az davranışsal veriyi toplayın, onam alın ve onuru gözetin, neyi neden izlediğinizi sade bir dille yayınlayın ve reddeden kişilere çalışan bir hizmet verin. Temel hizmetlerin tamamlanmasını artırmak için form ifadesi ve yerleşimi üzerinde kontrollü deneyler yürütün, her testin denetim için belgelenmiş, savunulabilir bir kaydını tutun ve her analitik tedarikçisinden veri işlemesini açıklamasını ve taşınabilirlik tanımasını isteyin; böylece kilitlenmeden kaçınırsınız.

## Örnekler

**Girişim.** Küçük bir tüketici uygulaması, yeni bir analitik eklemeden önce kayıt ve ilk oturum olayları için kısa, belgelenmiş bir izleme planı yazdı; böylece takım büyürken veri temiz kaldı. Bir huni, yeni kullanıcıların çoğunun hesap doğrulama adımında bıraktığını gösterdi ve daha net ifadeler üzerine yapılan basit bir A/B testi ilk hafta elde tutmayı artırdı. Trafik mütevazı olduğundan takım deneyleri yalnızca en yüksek hacimli akışlarında yürüttü, daha küçük değişiklikler için dikkatli yayınla ve gözle kullandı ve kuzey yıldızı metriği olarak etkinleştirmeyi korudu.

**Kurumsal.** Bir abonelikli yayın hizmeti, yönetilen bir izleme planı enstrümante eder ve her anlamlı değişikliği önceden belirlenmiş metrikler, güç hesapları ile oynatma performansı ve müşteri kaybı üzerindeki koruma metrikleri olan bir deney platformundan geçirir. Yeniden tasarlanan bir karşılama akışı incelemelerde daha iyi görünüyordu, ancak kontrollü bir test birinci hafta elde tutmayı düşürdüğünü gösterdi; takım onu geniş yayından önce geri aldı ve bu, platformun maliyetinden çok daha değerli bir kurtarmaydı.

**Kamu.** Bir dijital hizmetler kurumu, yardım başvuru akışını gizliliğe saygılı, onamı gözeten bir izleme planıyla enstrümante eder ve form ifadesi ile yerleşimi üzerinde kontrollü deneyler yürütür. Bir huni çözümlemesi, başvuranların üçte birinin vazgeçtiği belirli bir adımı ortaya çıkardı. Daha net yönlendirme üzerine yapılan bir deney tamamlanmayı anlamlı biçimde artırdı; hem eksik başvuruları hem çağrı merkezi hacmini azalttı ve bunu yalnızca gereken en az davranışsal veriyi toplayarak yaptı.

## İş gerekçesi: motivasyonlar, YG ve TSM

Ürün analitiği ve deneyin YG'si doğrudan çıktılarda görünür: daha yüksek dönüşüm, elde tutma ve tamamlanma ve en önemlisi zararlı değişiklikleri yayınlamanın önlenen maliyeti. Deney, kendi değerini ölçen az sayıdaki pratikten biridir, çünkü her test önlediği kazancı ya da kaybı raporlar. İyi enstrümantasyon, tahmini kanıtla değiştirerek her ürün kararının getirisini çarpar ve bir kuzey yıldızı metriği birçok takımı aynı başarı tanımında hizalar.

Benimseme maliyeti analitik ve deney araçlarını, iyi enstrümante etmek için mühendislik emeğini, testleri titizlikle yürütecek analitik becerisini ve onam için gizlilik programı yükünü içerir. Bunu benimsememenin maliyetiyle tartın: etkileri bilinmeyen değişiklikler yayınlamak, tartışmaları kanıtla değil kıdemle kazanmak, ürün durgunlaşırken pohpohlayan gösterişli metriklerin peşinden gitmek ve özensiz veri toplamadan doğan düzenleyici maruziyet. Liderliğe sunulacak argüman, deneyin ürün geliştirmeyi ölçülebilir, kendini düzelten bir sürece dönüştürdüğü ve önlenen ilk kötü yayının çoğu zaman tüm programı karşıladığıdır.

## Anti-kalıplar ve tuzaklar

- İzleme planı olmadan olay eklemek; tutarsız, kullanılamaz veri üretir.
- Deneyleri gözetleyip anlamlı göründüklerinde durmak; yanlış pozitifleri şişirir.
- Birçok metriği test edip tesadüfen anlamlı çıkan her birini kutlamak.
- Aradıkları etkiyi saptayamayan yetersiz güçlü testler yürütmek.
- Gerçek değeri yansıtmadan yükselen gösterişli metrikleri eniyilemek.
- Bir vekil metriği o kadar oyunlamak ki gerçek hedef zarar görür.
- Onam ya da tanımlı bir amaç olmadan davranışsal veri istiflemek.
- Olumsuz sonuçları kaydetmeyi unutmak; böylece kuruluş başarısız testleri tekrarlar.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Enstrümantasyon seyrek ya da tutarsızdır, kararlar görüş ve kıdemle verilir, deney yürütülmez ve toplam kayıt gibi gösterişli metrikler raporlanır. Onam özensizce ele alınır.
- **Düzey 2, Geliştirme:** Bazı olaylar izlenir ama sınıflandırma takımlar arasında kayar. Zaman zaman güç hesabı olmadan ad hoc A/B testleri yürütülür, huniler ve elde tutma gayriresmi biçimde incelenir ve bir kuzey yıldızı metriği önerilmiş ama henüz yerleşmemiştir.
- **Düzey 3, Standartlaştırma:** Yönetilen bir izleme planı ve tutarlı bir sınıflandırma belgelenmiş, sürümlenmiş ve her takım genelinde alım anında doğrulanır. Huniler, kohortlar ve elde tutma düzenli olarak çözümlenir, deneyler önceden belirlenmiş metrikler, güç hesapları ve koruma metrikleriyle paylaşılan bir platformda yürütülür ve gizlilik ile onam kuruluş genelinde düzgün biçimde ele alınır.
- **Düzey 4, Yönetme:** Pratik temel çizgilere karşı ölçülür: enstrümantasyon kapsamı ve olay kalitesi hata oranları izlenir, deney hızı ve bir testle kapılanan yayınların payı raporlanır, koruma metriği ihlalleri ve gözetleme otomatik olarak yakalanır ve kuzey yıldızı metriği ile girdi metrikleri açık bırakma eşikleriyle izlenir. Veri kalitesi ve gizlilik uyumu varsayılmak yerine sabit bir ritimle denetlenir.
- **Düzey 5, Orkestrasyon:** Deney her anlamlı değişiklik için varsayılandır, enstrümantasyon bir boru hattı gibi sahiplenilir ve izlenir ve olumsuz ve düz sonuçları da içeren paylaşılan bir sonuç deposu kuruluşun birikimli öğrenmesini ve çıkmaz sokakları emekli etmesini sağlar. Analitik ürün ve risk planlamasıyla bütünleşmiştir, tasarım gereği gizliliğe saygılıdır ve metrik kümesi ürün, pazar ve düzenlemeler değiştikçe sürekli yeniden kapsamlandırılır.

## Tartışma fikirleri

- Ürününüzün gerçek kuzey yıldızı metriği nedir ve herkes üzerinde anlaşıyor mu?
- Raporladığınız metriklerden hangileri yalnızca yukarı çıkan gösterişli sayılardır?
- Takımlarınız deney çalıştırmadan önce istatistiksel gücü hesaplıyor mu, yoksa gözetleyip duruyor mu?
- Enstrümantasyonunuzun kullanıcı acısını gizleyen kör noktaları nerede?
- İhtiyaç duyduğunuz şeyi öğrenmeye devam ederken analitiği nasıl gizliliğe saygılı tutuyorsunuz?
- Düşük trafikli özelliklerde yayınla ve gözle ne zaman kabul edilebilir, tam deney ne zaman gerekir?

## Önemli çıkarımlar

- Yönetilen bir izleme planı ve tutarlı bir sınıflandırmayla bilinçli biçimde enstrümante edin.
- Yalnızca edinimi değil, hunileri, kohortları, elde tutmayı ve etkileşimi çözümleyin.
- Titiz deneyler yürütün: güç hesapları, önceden belirlenmiş metrikler, gözetleme yok.
- Gerçek değere bağlı bir kuzey yıldızı metriğine demir atın ve gösterişli metriklere karşı korunun.
- Gereken en az davranışsal veriyi açık onam ve güçlü yönetişimle toplayın.
- Enstrümantasyonu bir ürün olarak ele alın ve birikimli bir deney kültürü kurun.
- Düz ya da olumsuz bir deney sonucu bir başarısızlık değil, değerli kanıttır.

## Kaynaklar ve ileri okuma

- Ron Kohavi, Diane Tang, and Ya Xu, "Trustworthy Online Controlled Experiments."
- Alistair Croll and Benjamin Yoskovitz, "Lean Analytics."
- Eric Ries, "The Lean Startup."
- Avinash Kaushik, "Web Analytics 2.0."
- Georgi Georgiev, "Statistical Methods in Online A/B Testing."
- Regulation (EU) 2016/679, General Data Protection Regulation (GDPR).
- Douglas W. Hubbard, "How to Measure Anything."
