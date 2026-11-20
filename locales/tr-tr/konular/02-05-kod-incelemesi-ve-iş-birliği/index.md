# 2.5 Kod incelemesi ve iş birliği

## Genel bakış ve motivasyon

[Kod incelemesi](https://en.wikipedia.org/wiki/Code_review), bir değişiklik birleşmeden önce yazarından başka birinin onu incelemesi uygulamasıdır. Bir yazılım kuruluşunun sahip olduğu en yüksek kaldıraçlı kalite ve bilgi paylaşımı etkinliklerinden biridir ve büyük takımlar için aynı zamanda eşgüdümün ve kültürün temel mekanizmalarından biridir. İnceleme kusurları yakalar, kod tabanı bilgisini yayar, standartları uygular ve mühendislere mentorluk yapar; ama yalnızca iyi yapıldığında. Kötü yapıldığında bir darboğaza, sürtünme kaynağına ya da yanlış güvence veren bir lastik damgaya dönüşür.

Büyük takımlar için inceleme, bireysel işin ortak sahiplenmeyle buluştuğu yerdir. Aksi halde kendi başlarına çalışan mühendisler arasındaki ana temas noktası çoğu zaman odur; bu yüzden normları tüm kuruluşun nasıl iş birliği yaptığını biçimlendirir. İnceleme bilgiyi yayar, böylece sistemin hiçbir parçası yalnızca bir kişi tarafından anlaşılmaz; bu da büyük, uzun ömürlü sistemleri rahatsız eden [otobüs faktörü](https://en.wikipedia.org/wiki/Bus_factor) riskini, yani bilginin çok az kişide olması tehlikesini azaltır. Ayrıca kimin neyi değiştirdiğine ve kimin onayladığına dair bir denetim izi oluşturur.

Kurumsal ve kamu bağlamlarında inceleme çoğu zaman bir uyum boyutu taşır. [Görev ayrılığı](https://en.wikipedia.org/wiki/Separation_of_duties) (hiçbir kişi hassas bir değişikliğin tamamını denetlemez), zorunlu onaylar ve izlenebilirlik sıklıkla gerekli kontrollerdir. Hassas sistemlere dokunan bir değişiklik belirli roller tarafından incelenmeyi gerektirebilir ve inceleme kaydı denetim kanıtı olur. Sizin zorluğunuz, incelemeyi törene dönüştürmek yerine hızlı ve yapıcı tutarken bu kontrolleri karşılamaktır.

## Temel ilkeler

- Gösteriş yapmak için değil, değişikliği iyileştirmek ve bilgi paylaşmak için inceleyin.
- Küçük değişiklikler daha iyi inceleme alır; bu yüzden çekme isteklerini (PR) odaklı ve makul boyutta tutun.
- İnceleme gecikmesi takım çapında bir maliyettir. Hızlı dönüş herkesi hareket halinde tutar.
- Mekanik şeyleri (üslup, testler, güvenlik taramaları) otomatikleştirin ki insanlar tasarımı ve doğruluğu incelesin.
- Engelleyici sorunları öneriler ve tercihlerden ayırın ve hangisinin hangisi olduğunu açıkça belirtin.
- Kişiyi değil, kodu eleştirin. Geri bildirim normları, incelemenin güven mi inşa ettiğini yoksa aşındırdığını mı belirler.
- Bir değişikliği incelenmesi kolay kılmak yazarın sorumluluğudur.

## Öneriler

### Çekme isteklerini küçük ve iyi tanımlanmış yapın

Her değişikliği tek bir mantıksal kaygıya odaklı ve dikkatle incelenecek kadar küçük tutun. Büyük PR'lar yüzeysel inceleme alır. Neyin değiştiğine, nedenine ve nasıl doğruladığınıza dair net bir açıklama verin ki inceleyicinin bağlamı olsun. Mekanik yeniden düzenlemeleri ve davranış değişikliklerini ayrı PR'lara bölün; böylece her biri üzerinde akıl yürütmek kolay olsun. İyi bir açıklama, yazarın inceleme kalitesine tek en önemli katkısıdır.

### İnceleme standartları ve kontrol listeleri oluşturun

İnceleyicilerin nelere bakması gerektiğini açıkça yazın: doğruluk, tasarıma uyum, test yeterliliği, güvenlik etkileri, okunabilirlik ve standartlara uyum. Hafif bir kontrol listesi, incelemeleri tutarlı tutar ve önemli boyutların gözden kaçmasını önler; incelemeyi kutu işaretlemeye dönüştürmez. Neyin inceleme gerektirdiğini, kimin onaylayabileceğini ve hassas alanlar için gereken rol tabanlı onayları tanımlayın.

### İnceleme gecikmesi normlarını belirleyin ve izleyin

Hedef bir dönüş süresi üzerinde anlaşın, örneğin bir iş günü içinde yanıt vermek, ve incelemeyi en son sıkıştırılan bir şey değil, günün birinci sınıf bir parçası yapın. Uzun inceleme kuyrukları teslimatı durdurur ve mühendisleri aşırı büyük, toplu değişikliklere sürükler. İlk incelemeye kadar süreyi ve birleştirmeye kadar süreyi izleyin ve süregelen gecikmeyi kişisel bir kusur değil, düzeltilecek bir süreç sorunu olarak ele alın.

### Mekanik olan her şeyi otomatikleştirin

Biçimlendirmeyi, [linter](https://en.wikipedia.org/wiki/Lint_(software)) denetimini, testleri ve güvenlik ile bağımlılık taramasını [sürekli entegrasyonda](https://en.wikipedia.org/wiki/Continuous_integration) (CI) çalıştırın; böylece inceleyiciler onlara asla dikkat harcamasın. İnsan incelemesini makinelerin yargılayamadığı şeylere saklayın: tasarımın doğru olup olmadığı, yaklaşımın sisteme uyup uymadığı, testlerin anlamlı olup olmadığı ve kodun sonradan hâlâ anlam taşıyıp taşımayacağı.

### Eşli ve topluluk programlamayı uyduğu yerde kullanın

Karmaşık ya da yüksek riskli iş, uyum ve bilgi aktarımı için iki mühendisin tek bir iş istasyonunda birlikte kod yazdığı [eşli programlamayı](https://en.wikipedia.org/wiki/Pair_programming) kullanın. Sürekli incelemedir ve çoğu zaman ayrı bir inceleme adımı ihtiyacını ortadan kaldırır. Kritik tasarım kararları için ya da zorlu bir alanın bilgisini takıma yaymak için tüm takımın aynı anda tek bir görev üzerinde çalıştığı [topluluk programlamayı](https://en.wikipedia.org/wiki/Mob_programming) kullanın. Bunları eşzamansız incelemeyi her yerde zorunlu kılınacak ikameler olarak değil, bağlama göre seçilen tamamlayıcılar olarak düşünün.

### Otomatik ve yapay zeka destekli incelemeyi dikkatle benimseyin

Yaygın sorunları yakalamak, iyileştirmeler önermek ve inceleyicinin yükünü hafifletmek için otomatik inceleme araçlarını ve yapay zeka asistanlarını kullanın, ama çıktılarını otorite değil girdi olarak ele alın. Yapay zeka incelemesi yüzey sorunlarında ve tutarlılıkta iyidir, derin tasarım muhakemesinde ve sistem bağlamında zayıftır. Her onay için, özellikle güvenlik açısından hassas ve uyumla ilgili değişikliklerde, bir insanı sorumlu tutun.

### Yapıcı geri bildirim normları belirleyin

Geri bildirimi belirli, nazik ve koda odaklı tutan normlar belirleyin. İnceleyicileri emir vermek yerine soru sormaya, bir isteğin ardındaki gerekçeyi açıklamaya ve iyi işi övmeye teşvik edin. Engelleyici kaygıları ve isteğe bağlı önerileri açıkça işaretleyin (örneğin engelleyici olmayan notlara önek koyarak). Bu normlar, incelemenin takımı güçlendirip güçlendirmediğini ya da kırgınlık üretip üretmediğini belirler.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
|---|---|---|
| Eşzamansız PR incelemesi | Esnek; belgelenmiş; saat dilimleri arasında ölçeklenir | Gecikme; nüans kaybı; husumetli hissettirebilir |
| Eşli programlama | Sürekli inceleme; hızlı bilgi aktarımı; yüksek kalite | Bir görevde iki kişi; yorucu; planlaması daha zor |
| Topluluk programlama | Tüm takımın hizalanması; derin bilgiyi yayar | Toplamda pahalı; rutin iş için değil |
| Zorunlu çoklu inceleyici | Güçlü güvence; uyum dostu | Daha yavaş; sorumluluğu dağıtır; kuyruk baskısı |
| Yapay zeka destekli inceleme | Yaygın sorunlarda hızlı, yorulmaz; yükü azaltır | Sistem bağlamını kaçırır; aşırı güvenilirse yanlış güven |

Çekirdek gerilim titizlik ile hız arasındadır. Daha derin inceleme daha fazlasını yakalar, ama teslimatı yavaşlatır ve yazarları hayal kırıklığına uğratabilir. Daha hızlı inceleme akışı korur, ama yüzeysel olma riski taşır. Çıkış yolu, inceleme derinliğini değişiklik riskine uydurmaktır; önemsiz değişiklikler hafif, riskli değişiklikler derin inceleme alır ve insan çabasının önemli olan yere yoğunlaşması için mekanik işi otomatikleştirmektir.

## Takımınızla tartışılacak sorular

1. **Tek bir çekme isteği için ne fazla büyük sayılır ve mekanik yeniden düzenlemeleri davranış değişikliklerinden ayırıyor musunuz?** Bu bölüm büyük PR'ların yüzeysel inceleme aldığını ve incelenebilirliğin yazara ait olduğunu açıkça söyler ve her birinin üzerinde akıl yürütmek kolay olsun diye yeniden düzenlemeleri davranış değişikliklerinden ayırmanızı ister. Büyük bir takımda dev bir PR lastik damgayı garanti eder; bu da gerçek kusurların geçmesine izin verirken yanlış güvence verir. Kanıtı getirin: PR boyutlarınızın dağılımı ve fark büyüdükçe inceleme derinliğinin nasıl düştüğü. Pratik bir boyut normu ve saf yeniden düzenlemeleri mantık değişikliklerinden ayrı indirme alışkanlığı üzerinde anlaşın; böylece bir inceleyici her değişikliği gerçekten kafasında tutabilsin. Bu tek disiplin, ardından gelen her incelemenin kalitesini yükseltir.

2. **Engelleyici bir itirazı isteğe bağlı bir öneriden nasıl ayırıyorsunuz ve bu kural gerçekten kullanılıyor mu?** Bölüm engelleyici sorunları tercihlerden ayırmanızı ve hangisinin hangisi olduğunu açıkça belirtmenizi ister ve tercih üzerine engellemeyi aşındırıcı bir anti-kalıp olarak işaretler. Paylaşılan bir kural olmadan, bir inceleyicinin üslup görüşü zorunlu bir değişiklik gibi okunur; bu da kırgınlık üretir ve tüm takım boyunca teslimatı yavaşlatır. Somut sinyal olarak, bir tercihin bir birleştirmeyi durdurduğu son incelemelerden örnekler getirin. Yazarların neyin değişmesi gerektiğini, neyin öneri olduğunu anında bilmesi için hafif bir işaret, örneğin engelleyici olmayan notları etiketleyen bir önek, benimseyin. Bu, incelemeyi zevke değil doğruluğa ve tasarıma odaklı tutar.

3. **Güvenlik açısından hassas ya da uyumla ilgili koddaki değişiklikleri kim onaylamalı ve bu yönlendirme nasıl uygulanıyor?** Bu bölüm rol tabanlı onayları, kod sahipliği kurallarını ve hiçbir kişinin hassas bir değişikliğin tamamını denetlemediği görev ayrılığını, onayın denetim kanıtı olarak kaydedilmesiyle tarif eder. Kurumsal ve kamu ortamlarında bunlar gerekli kontrollerdir ve risk, ya atlanmaları ya da teslimatı donduran bir darboğaza dönüşmeleridir. Sinyali getirin: hangi modüller hassas ve sahiplik kuralları bu değişiklikleri şu anda doğru onaylayıcılara otomatik yönlendiriyor mu. Yönlendirmeyi kod sahipliği yapılandırmasına kodlayın ve otomatik kontroller ile küçük değişikliklerle eşleştirin; böylece kontrol, insan kapı bekçiliği kuyruğu olmadan karşılanır. Boşluğu bir denetim sırasında keşfetmek yerine bunu bilinçli kararlaştırın.

4. **Gerçekte hangi inceleme gecikmesi hedefi üzerinde anlaştınız ve onu ölçüp uyguluyor musunuz, yoksa yalnızca bir dilek mi?** Bölüm inceleme gecikmesini takım çapında bir maliyet olarak ele alır ve ilk incelemeye kadar süreyi ve birleştirmeye kadar süreyi izlemenizi, süregelen gecikmeyi kişisel bir kusur değil bir süreç sorunu olarak değerlendirmenizi ister. Büyük bir takımda sahipsiz bir inceleme kuyruğu herkesi sessizce vergilendirir: yazarlar beklemekten kaçınmak için daha büyük değişiklikleri toplar, bu değişiklikler daha yüzeysel inceleme alır ve teslimat öncül süresi tek bir suçlu olmadan yukarı kayar. Karşıt değerlendirme, sert bir gecikme hedefinin inceleyicileri göz gezdirmeye itebilmesidir; bu yüzden hız ve derinlik körü körüne takas edilmek yerine dengelenmelidir. Kanıtı getirin: ilk incelemeye kadar sürenizin mevcut dağılımı, takıma ve değişiklik boyutuna göre nasıl değiştiği ve incelemelerin en uzun nerede beklediği. Kurumsal ve kamu ortamlarında hedefi liderliğin zaten izlediği akış metriklerine bağlayın, çünkü gecikme normu olmayan zorunlu çoklu inceleyici kontrolü, teslimatı donduran ve insanları kontrolü tamamen dolanmaya özendiren darboğaz olur.

5. **Hangi tür değişiklikler için otomatik ve yapay zeka destekli incelemeye güveniyorsunuz ve nerede bir insan sorumlu kalmalı?** Bölüm yapay zeka inceleme çıktısını otorite değil girdi olarak ele almayı söyler: yüzey sorunlarında ve tutarlılıkta güçlü, derin tasarım muhakemesinde ve sistem bağlamında zayıf; her onayda sorumlu bir insan. Açık bir sınır olmadan büyük bir takım aşırı güvene kayar; yeşil bir bot yorumu geçilmiş bir inceleme gibi okunur ve gerçek tasarım ve güvenlik riskleri yanlış güven altında geçer. Karşıt çekim, yapay zeka incelemesinin yükü gerçekten hafifletmesi ve yaygın kusurları yorulmadan yakalamasıdır; bu yüzden onu yasaklamak kaldıracı boşa harcar. Kanıtı getirin: otomatik önerilerin gerçek sorunları nerede yakaladığı, nerede gürültü ürettiği ve hangi değişiklik türlerini (güvenlik açısından hassas, uyumla ilgili, mimari) bir makinenin tek başına onaylamasına asla izin vermeyeceğiniz. Kurumsal ve kamu işi için, döngüde bir yapay zeka asistanı varken bir onayın sorumluluğunu kimin taşıdığını adlandırın, çünkü bir denetim bir değişikliği kimin incelediğini soracaktır ve "araç yaptı" bir düzenleyicinin kabul ettiği bir cevap değildir.

6. **Eşli ya da topluluk programlama nerede eşzamansız incelemenin yerini almalı ve otobüs faktörü riskini azaltmak için incelemeyi bilinçli nasıl kullanıyorsunuz?** Bölüm eşli ve topluluk programlamayı bağlama göre seçilen sürekli inceleme olarak çerçeveler ve incelemeyi, sistemin hiçbir parçasının yalnızca bir kişi tarafından anlaşılmamasını sağlayan bilgi yayma mekanizması olarak adlandırır. Örtük bırakıldığında bilgi yoğunlaşır: aynı uzman bir alt sistemdeki her değişikliği inceler, kimse ona meydan okuyamadığı için inceleme lastik damgaya döner ve otobüs faktörü riski tam da sistemin en kritik olduğu yerde büyür. Karşıt değerlendirme maliyettir, çünkü topluluk programlama tüm takımın zamanını harcar ve eşli programlama iki mühendisi bağlar; bu yüzden her yerde zorunlu kılamazsınız. Kanıtı getirin: hangi modüllerin yalnızca bir güvenilir inceleyicisi var, uyumun nerede tıkandığı ve zorlu bir alanın yorum dizileri yerine canlı bir oturumdan nerede yararlanacağı. Büyük ya da kamusal bir kuruluşta bilinçli bilgi yayılımını risk yönetimi olarak ele alın, çünkü kritik parçaları tek bir kişiye bağlı uzun ömürlü bir sistem yalnızca bir kadro rahatsızlığı değil, operasyonel ve süreklilik yükümlülüğüdür.

## Sektör merceği

**Girişim.** Üç dört mühendisle incelemeyi hafif tutun: küçük bir çekme isteğinde bir takım arkadaşının onayı, CI'de mekanik kontroller ve bir birleştirmeyi durduracak zorunlu ikinci inceleyici yok. Asıl hedef uyumdan çok sistemin her parçasını birden fazla kişinin anlamasını sağlamaktır; bu yüzden riskli parçalarda eşli çalışın ve bunu uyum olarak ele alın. Yakında aşacağınız ağır kod sahipliği yönlendirmesi kurmayın; küçük, iyi tanımlanmış değişikliklerin paylaşılan normu faydanın çoğunu neredeyse sıfır maliyetle sağlar.

**Küçük işletme.** Muhtemelen inceleme araçları uzmanınız yoktur; bu yüzden özel otomasyon kurmak yerine barındırma platformunuzun (örneğin yönetilen bir Git hizmeti) kutudan çıktığı gibi verdiğine yaslanın. Linter, test ve güvenlik taraması entegrasyonlarını sürdürmek yerine satın alın; böylece az sayıdaki mühendisiniz kıt inceleme dakikalarını tasarıma ve doğruluğa harcasın. Tek basit bir kural tutun: her değişiklik başka bir çift göz görür; ve sürdürecek kimsenizin olmadığı süreç eklemeye direnin.

**Kurumsal.** Zorluk birçok takım boyunca tutarlılıktır: paylaşılan standartlar, hassas değişiklikleri doğru onaylayıcılara yönlendiren kod sahipliği kuralları ve denetim kanıtı olarak kaydedilen rol tabanlı onaylar. İnsan incelemesi tasarıma yoğunlaşsın diye mekanik kontrolleri kuruluş genelinde otomatikleştirin ve zorunlu çoklu inceleyici kontrollerinin sessizce darboğaza dönüşmemesi için inceleme gecikmesini bir akış metriği olarak izleyin. İnceleme derinliğini belgelenmiş bir politikayla değişiklik riskine uydurun; böylece önemsiz değişiklikler hızlı kalırken yüksek riskli olanlar görev ayrılığı ve daha derin inceleme alır.

**Kamu.** Değişiklik kontrolü çoğu zaman zorunludur: her üretim değişikliği, yazarından başka biri tarafından incelenir ve onaylanır; kayıt, görev ayrılığı gereksinimlerini karşılamak için denetim kanıtı olarak tutulur. Kimin yazdığının, kimin onayladığının ve hangi kontrollerin geçtiğinin şeffaf, izlenebilir bir izini tercih edin ve kontrolün teslimatı dondurmaması için otomasyona ve küçük, sık değişikliklere yatırım yapın. İnceleme araçları tedarik edildiğinde, dışa aktarılabilir denetim günlükleri talep edin ve kilitlenmeden kaçının; çünkü kanıt tek bir satıcıdan uzun yaşamalı ve kamusal incelemeye dayanmalıdır.

## Örnekler

**Girişim.** Dört mühendislik bir girişim her çekme isteğini küçük tutar ve birleştirmeden önce bir takım arkadaşının onayını ister; bunu uyumdan çok, hiçbir tek kişinin sistemin bir parçasını anlayan tek kişi olmamasını sağlamak için yapar. CI biçimlendiriciyi ve testleri çalıştırır; böylece insanlar az sayıdaki inceleme dakikasını boşluk yerine tasarıma ve doğruluğa harcar. Takım ödeme akışının zorlu bir parçasına geldiğinde, ikisi eşzamansız yorum alışverişi yerine birlikte eşli çalışır; bu, en yeni işe alınan için uyum işlevi de görür.

**Kurumsal.** Büyük bir yazılım şirketi her değişiklikte en az bir onaylayan inceleme ve kod sahipliği kurallarıyla belirlenen güvenlik açısından hassas modüllerdeki değişiklikler için ikinci bir onay ister. CI tüm üslup ve test kontrollerini halleder; böylece inceleyiciler tasarıma ve doğruluğa odaklanır. Takım ilk incelemeye kadar süreyi izler ve yükselen bir medyanı iş yükünü yeniden dengelemek için sinyal olarak ele alır. Yeni mühendisler eşli çalışmayla uyum sağlar; bu, bağımsız katkıya giden yollarını kısaltır.

**Kamu.** Sıkı değişiklik kontrolü gereksinimleri altında çalışan ulusal bir kurum, her üretim değişikliğinin yazarından başka biri tarafından incelenip onaylanmasını ve onayın denetim için kaydedilmesini zorunlu kılar. Bu kontrolün darboğaza dönüşmesini önlemek için kurum otomatik kontrollere ve küçük, sık değişikliklere yatırım yapar ve aynı gün inceleme yanıtı normu belirler. Kimin yazdığını, kimin onayladığını ve hangi kontrollerin geçtiğini kapsayan inceleme izi, her sürüm için uyum kanıtının parçası olur; teslimatı dondurmadan görev ayrılığı gereksinimlerini karşılar.

## İş gerekçesi: motivasyonlar, YG ve TSM

Kod incelemesi size üç para biriminde geri öder: üretimden önce yakalanan kusurlar, takıma yayılan bilgi ve zaman içinde otomatik olarak korunan standartlar. İncelemede bir kusuru yakalamak üretimde yakalamaktan çok daha ucuzdur ve bilgi paylaşımı faydası, biri ayrıldığında bir kuruluşa aksi halde pahalıya mal olabilecek kilit kişi riskini azaltır. İnceleme ayrıca büyüyen bir takımı tutarlı tutan kültürel aktarım mekanizmasıdır.

İncelemenin maliyeti mühendis zamanı ve biraz gecikmedir; ikisi de iyi uygulamalarla yönetilebilir. İncelememenin ya da kötü incelemenin maliyeti üretim kusurlarını, silolanmış bilgiyi, tutarsız kodu ve düzenlemeye tabi ortamlarda başarısız denetimleri ve uyum bulgularını içerir. Aşırı ağır incelemenin de kendi gerçek maliyeti vardır: uzun kuyruklar, aşırı büyük toplu işler, moralsiz mühendisler. Gerekçeyi liderliğe sunmak için inceleme uygulamalarını değişim başarısızlık oranına, teslimat öncül süresine ve uyum hızına bağlayın ve inceleme gecikmesini açık bir akış metriği olarak izleyin.

## Anti-kalıplar ve tuzaklar

- **Lastik damga:** gerçek bir inceleme olmadan onaylar; yanlış güvence verir ve bir kontrolün yalnızca lafzını karşılar.
- **Dev PR:** yalnızca göz gezdirilebilen binlerce satır; yüzeysel incelemeyi garanti eder.
- **Yalnızca ayrıntıcı inceleme:** tasarımı ve doğruluğu kaçırırken önemsiz şeylere odaklanmak; çoğu zaman mekanik kontroller otomatik olmadığı için.
- **Kapı bekçiliği olarak inceleme:** üstünlük iddia etmek ya da başkalarını engellemek için incelemeyi kullanmak; iş birliğini zehirler.
- **Yavaş kuyruk:** günlerce bekleyen incelemeler; teslimatı durdurur ve toplu işlemeyi teşvik eder.
- **Yapay zeka incelemesine aşırı güvenmek:** otomatik önerileri otoriter görmek ve riskli değişikliklerde insan yargısını bırakmak.
- **Tercih üzerine engellemek:** kişisel üslup görüşlerini gerçek kusurlardan ayırmadan zorunlu değişiklikler olarak sunmak.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** İnceleme gelişigüzel ve reaktiftir. Çoğu zaman atlanır ya da tutarsız yapılır, yorumlara mekanik sorunlar hâkimdir, geri bildirim normları belirlenmemiştir ve herhangi bir onay izi bilinçli değil tesadüfidir.
- **Düzey 2, Geliştirme:** Temel inceleme uygulamaları vardır ama takımdan takıma değişir. İnceleme bazı yerlerde zorunlu, bazılarında yavaş ya da isteğe bağlıdır, otomasyon kısmidir ve çekme isteği boyutu ve kalitesi paylaşılan bir beklenti olmadan geniş ölçüde salınır.
- **Düzey 3, Standartlaştırma:** Standartlar belgelenmiş ve kuruluş genelinde uygulanır. Küçük odaklı PR'lar, CI'de otomatik biçimlendirme, linter denetimi, testler ve güvenlik taraması, net kontrol listeleri, açık bir engelleyici ve öneri ayrımı kuralı ve hassas değişiklikleri doğru onaylayıcılara yönlendiren kod sahipliği kuralları.
- **Düzey 4, Yönetme:** İnceleme temel çizgilere karşı ölçülür ve kontrol edilir. İlk incelemeye kadar süre, birleştirmeye kadar süre, değişiklik riskine karşı inceleme derinliği, kusur kaçış oranı ve değişim başarısızlık oranı izlenir; süregelen gecikme bir süreç sorunu olarak ele alınır ve veri, inceleyici yükünün nerede yeniden dengeleneceğini ve hangi kontrollerin güvence katmadan teslimatı yavaşlattığını yönlendirir.
- **Düzey 5, Orkestrasyon:** İnceleme sürekli iyileştirilir ve kuruluş genelinde bütünleşir. Derinlik değişiklik riskine uyum sağlar, eşli çalışma, topluluk programlama ve yapay zeka desteği sorumlu bir insanla bilinçli kullanılır, bilgi yayılımı ve otobüs faktörü riski kasıtlı yönetilir ve inceleme kaliteyi, teslimat akışını ve uyumu ölçülebilir biçimde iyileştirir.

## Tartışma fikirleri

- Takımınız için doğru inceleme gecikmesi hedefi nedir ve ona ulaşmanızı ne engelliyor?
- Bürokrasi eklemeden inceleme derinliğini değişiklik riskine nasıl uydurursunuz?
- Sizin bağlamınızda eşli çalışma ya da topluluk programlama eşzamansız incelemeyi nerede geride bırakır?
- Yapay zeka destekli inceleme ne kadar güvenilmeli ve hangi tür değişiklikler için?
- Takım büyüyüp çeşitlendikçe inceleme geri bildirimini yapıcı nasıl tutarsınız?
- Darboğaz yaratmadan uyum onay gereksinimlerini nasıl karşılarsınız?

## Önemli çıkarımlar

- Çekme isteklerini küçük ve iyi tanımlanmış tutun; incelenebilirlik yazara aittir.
- Mekanik olanı otomatikleştirin ki insanlar tasarımı, doğruluğu ve testleri incelesin.
- İnceleme gecikmesini takım çapında bir akış maliyeti olarak izleyin ve yönetin.
- İnceleme derinliğini değişiklik riskine uydurun ve engelleyici sorunları tercihlerden ayırın.
- Eşli çalışmayı, topluluk programlamayı ve yapay zeka desteğini bağlama uyan tamamlayıcılar olarak kullanın; bir insanı sorumlu tutun.

## Kaynaklar ve ileri okuma

- Karl Wiegers, *Peer Reviews in Software: A Practical Guide*
- Google, *Engineering Practices: How to Do a Code Review* (as a reference exemplar)
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Kent Beck, *Extreme Programming Explained* (on pair programming)
- Woody Zuill, writings on mob programming
- Michael Lopp, *Managing Humans* (on engineering collaboration)
