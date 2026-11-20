# 3.5 Ölçeklenebilirlik, performans ve dayanıklılık

## Genel bakış ve motivasyon

[Ölçeklenebilirlik](https://en.wikipedia.org/wiki/Scalability), performans ve dayanıklılık üç ayrı niteliktir ve insanlar çoğu zaman bunları birbirine karıştırır. **Performans**, sistemin ne kadar hızlı yanıt verdiği ve kaynak birimi başına ne kadar iş yaptığıdır. **Ölçeklenebilirlik**, yük büyürken performansı ne kadar iyi koruduğudur. **Dayanıklılık**, bir şeyler başarısız olduğunda çalışmaya ne kadar iyi devam ettiği ya da zarifçe bozulduğudur. Bir sistem hızlı ama ölçeklenemez olabilir (düşük yükte harika, yüksek yükte çöker), ölçeklenebilir ama kırılgan olabilir (hacmi kaldırır ama bir bileşen başarısız olunca devrilir) ya da dayanıklı ama yavaş olabilir. Büyük bir kuruluşun üçüne de ihtiyacı vardır ve üçü de en baştan tasarlanmalıdır, çünkü herhangi birini yayına çıktıktan sonra eklemek pahalı ve yıkıcıdır.

Kurumsal ve kamu sistemleri için bunları yanlış yapmanın sonuçları kamuya açık ve ağırdır. Yeni bir düzenlemenin ilk gününde çöken bir yardım portalını, son tarihte zaman aşımına uğrayan bir vergi beyan sistemini ya da yoğun alışveriş sırasında devre dışı kalan bir ödeme platformunu düşünün. Bunlar manşetlere çıkan, soruşturmaları tetikleyen ve kamu güvenini aşındıran başarısızlıklardır. Bu sistemler ayrıca çok tepeli, çoğu zaman yasal olarak zamanlanmış yükle (beyan son tarihleri, kayıt pencereleri, maaş günleri) ve sıkı erişilebilirlik ve toparlanma yükümlülükleriyle karşılaşır. Öngörülebilir dalgalanmalar için kapasite planlamanız, öngörülemeyenlerde zarifçe bozulmanız ve bir felaketten sonra tanımlı süre ve veri kaybı sınırları içinde toparlanmanız gerekir. Bu, kamuya hesap verebilirlik boyutu olan bir mühendisliktir.

Bu bölüm yatay ve dikey ölçeklemeyi, ölçeği mümkün kılan unsurlar olarak durumsuzluğu ve [parçalamayı](https://en.wikipedia.org/wiki/Shard_(database_architecture)), [yük dengelemeyi](https://en.wikipedia.org/wiki/Load_balancing_(computing)), [otomatik ölçeklemeyi](https://en.wikipedia.org/wiki/Autoscaling) ve kapasite planlamayı, açık bütçelerle performans mühendisliğini, dayanıklılık kalıplarını ve [kaos mühendisliğini](https://en.wikipedia.org/wiki/Chaos_engineering) ve RTO, RPO ve iş sürekliliği çerçevesinde çok bölgeli [felaket kurtarmayı](https://en.wikipedia.org/wiki/Disaster_recovery) kapsar. Birleştirici mesaj şudur: bu nitelikler umudun değil, bilinçli tasarımın ve sürekli sınamanın ürünüdür.

*Ayrıca bakın:* bölüm 3.3 (dağıtık sistemler), bölüm 9.1 (site güvenilirliği mühendisliği) ve bölüm 9.2 (gözlemlenebilirlik ve izleme).

## Temel ilkeler

- **Dikey değil, yatay ölçek için tasarlayın.** Dikey ölçeklemenin bir tavanı ve bir [tekil hata noktası](https://en.wikipedia.org/wiki/Single_point_of_failure) vardır; büyük, dayanıklı ölçeğe yatay ölçeklemeyle ulaşılır.
- **Durumsuzluk, yatay ölçeğin sağlayıcısıdır.** Her istek herhangi bir örneğe gidebiliyorsa kapasiteyi özgürce ekleyip çıkarabilirsiniz.
- **Ölçmediğinizi iyileştiremezsiniz.** Performans çalışması, tahminle değil, açık bütçelere karşı profil çıkarma ve yük testiyle yürütülür.
- **Her şey başarısız olur; bunun için tasarlayın.** Bileşenlerin başarısız olacağını varsayın ve sistemi, onların başarısızlığından sağ çıkacak şekilde kurun.
- **Zarif bozulma, sert başarısızlıktan iyidir.** Gerekli olmayan özellikleri bırakan kısmen çalışan bir sistem, tam bir kesintiden iyidir.
- **Kapasite planlanır, dalgalanmalar emilir.** Öngörülebilir yükü tahmin edin; geri kalanı için otomatik ölçeklemeyi ve boşluk payını kullanın.
- **Toparlanma hedefleri iş kararlarıdır.** RTO ve RPO iş tarafından maliyete karşı seçilir, sonra onlara göre mühendislik yapılır.
- **Dayanıklılığı bilinçli sınayın.** Sistemi bilerek başarısız kılana kadar dayanıklı olduğunu bilemezsiniz.

## Öneriler

### Yatay ölçeklemeyi tercih edin ve durumsuz hizmetler tasarlayın

Dikey ölçekleme (daha büyük makineler) basittir ve bazen doğru ilk adımdır, ama sert bir tavana çarpar, üst uçta orantısız pahalılaşır ve tekil bir hata noktası bırakır. **Yatay ölçekleme** (bir yük dengeleyicinin arkasında daha çok makine) çok daha öteye ölçeklenir ve erişilebilirliği iyileştirir, çünkü bir örneği kaybetmek atlatılabilir. Ön koşul **durumsuzluktur**. Örnek üzerinde hiçbir istemci oturumu ya da istek durumu tutmayın; bunu paylaşılan bir depoya (veritabanı, önbellek, belirteç) itin. Durumsuz hizmetler özgürce eklenebilir, çıkarılabilir, değiştirilebilir ve yük dengelenebilir; bu da hem otomatik ölçeklemeyi hem aşamalı dağıtımı mümkün kılan şeydir. Durumun bölünmesi gereken yerde, yükü eşit dağıtan ve ilişkili veriyi aynı parçada tutan bir anahtarla **parçalayın**.

### Yük dengeleyin, otomatik ölçekleyin ve kapasite planlayın

Trafiği dağıtmak ve sağlık kontrolleriyle sağlıksız örneklerin etrafından dolaşmak için ölçeklenen her katmanın önüne bir **yük dengeleyici** koyun. **Otomatik ölçeklemeyi**, öncü bir gösterge (CPU, istek kuyruğu derinliği, gecikme) bir eşiği aştığında kapasite ekleyecek ve yük düştüğünde kaldıracak şekilde yapılandırın. Ölçekleme hızını ve soğuma sürelerini, ne bir sıçramanın gerisinde kalacak ne de çırpınacak şekilde ayarlayın. Otomatik ölçekleme, **kapasite planlamanın** yerini tutmaz. Öngörülebilir, iş açısından kritik dalgalanmalar (vergi son tarihleri, kayıt dönemleri, satış etkinlikleri) için yükü tahmin edin, kapasiteyi önceden hazırlayın ya da ısıtın ve o hedefe karşı önceden yük testi yapın. Otomatik ölçekleme bir adım değişikliğe anında tepki veremez ve soğuk başlangıçlar, en az kaldıramayacağınız anda gecikme ekler. Her zaman boşluk payı bırakın. Yüzde 100'de çalışmak sıçramaları ya da başarısızlıkları emecek yer bırakmaz.

### Performansı açık bütçelere göre mühendislikle yönetin

**Performans bütçeleri** belirleyin (p95 API gecikmesi 200 ms altında, sayfanın 2 saniyede etkileşimli olması ya da işlem başına maliyetin bir eşiğin altında olması gibi somut hedefler) ve bunları test ve izlemede zorlayın; böylece gerilemeler kullanıcılara ulaşmak yerine boru hattını başarısız kılar. Optimizasyonu **ölçümle** yönlendirin. Gerçek darboğazı bulmak için profil çıkarın (bu nadiren tahmin ettiğiniz yerdedir) ve sistemin nerede kırıldığını ve o sınırın yakınında nasıl davrandığını bulmak için yük testi yapın. Kritik yola ve kuyruğa (p95/p99) odaklanın, çünkü ölçekte kuyruk gecikmeleri kullanıcı deneyimine hükmeder. Önce en büyük darboğazı optimize edin, yeniden ölçün ve bütçeyi tutturduğunuzda durun. Zaten yeterli olan kodu aşırı optimize etmek boşa harcanmış çabadır.

### Dayanıklılık kalıplarını yerleştirin ve kaos mühendisliğiyle doğrulayın

Dağıtık sistemlerdeki dayanıklılık kalıplarını uygulayın: zaman aşımları, geri çekilmeli sınırlı yeniden denemeler, [devre kesiciler](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern) (bağımlılık sağlıksız olduğunda hızlı başarısız olur) ve bölmeler (bir başarısızlığın geri kalanı tüketememesi için kaynak havuzlarını yalıtır); ayrıca **zarif bozulma** (stres altında gerekli olmayan özellikleri bırakın ya da basitleştirin: önerileri kapatın, önbellekteki içeriği sunun, acil olmayan işi kuyruğa alın) ve **yük atma** (tamamen çökmek yerine çekirdeği korumak için fazla istekleri reddedin ya da kısın). Her katmanda artıklıkla tekil hata noktalarını ortadan kaldırın. Sonra dayanıklılığı kaos mühendisliğiyle **doğrulayın**. Sistemin tasarlandığı gibi davrandığını kanıtlamak için denetimli deneylerde kasıtlı olarak başarısızlıklar enjekte edin (örnekleri öldürün, gecikme ekleyin, bir bağımlılığı kesin, bir bölgeyi çökertin); testte başlayıp üretimdeki oyun günlerine olgunlaşın. Hiç sınanmamış dayanıklılık yalnızca bir hipotezdir.

### Çok bölgeyi, felaket kurtarmayı ve iş sürekliliğini planlayın

Toparlanma hedeflerine açıkça karar verin: **RTO** (Recovery Time Objective, Kurtarma Süresi Hedefi: ne kadar süre kapalı kalabileceğiniz) ve **RPO** (Recovery Point Objective, Kurtarma Noktası Hedefi: ne kadar veri kaybını göze alabileceğiniz). Bunlar doğrudan maliyet sonuçları olan iş kararlarıdır ve mimariyi yönlendirirler. Seçenekler maliyet ve hız açısından değişir: yedekten geri yükleme (en ucuz, en yavaş), pilot ışık, ılık yedek ve etkin-etkin çok bölge (en pahalı, sıfıra yakın RTO/RPO). Her sistemin kritikliğinin haklı çıkardığı katmanı seçin. Her şeyin etkin-etkine ihtiyacı yoktur. Veriyi seçilen RPO ile uyumlu olarak bölgeler arasında çoğaltın, yük devretmeyi otomatikleştirin ve her şeyden önce **yük devretmeyi düzenli sınayın**. Sınanmamış felaket kurtarma, nihayet gerektiği anda güvenilir biçimde başarısız olur. Tüm bunları yalnızca teknolojiyi değil, insanları, iletişimi ve elle yedek planları da kapsayan bir **iş sürekliliği planıyla** sarın.

## Ödünleşimler: artılar ve eksiler

| Seçim | Artılar | Eksiler |
|---|---|---|
| Dikey ölçekleme | Basit, kod değişikliği yok, düşük ilk çaba | Sert tavan, üstte pahalı, tekil hata noktası |
| Yatay ölçekleme | Neredeyse sınırsız ölçek, erişilebilirliği iyileştirir | Durumsuzluk, yük dengeleme ve daha çok operasyon gerektirir |
| Otomatik ölçekleme | Maliyeti talebe uydurur, değişken yükü karşılar | Gecikmeyle tepki verir; soğuk başlangıçlar; yanlış ayarlanırsa çırpınabilir |
| Etkin-etkin çok bölge | Sıfıra yakın RTO/RPO, bölge kaybından sağ çıkar | En yüksek maliyet ve karmaşıklık, zor veri tutarlılığı |
| Yedekten geri yüklemeli felaket kurtarma | En ucuz, en basit | Uzun RTO, daha geniş veri kaybı penceresi |

Merkezi ödünleşim maliyet ile güvence arasındadır. Ölçeklenebilirlik payı, performans ve toparlanma yeteneğindeki her artış para ve karmaşıklığa mal olur ve getiriler doğrusal değildir. Yüzde 99,9 erişilebilirlikten yüzde 99,99'a ya da bir saatlik RTO'dan saniyelere geçmek maliyeti katlayabilir. Disiplin, her yatırımı sistemin gerçek kritikliğine ve işin kesinti ile veri kaybına tahammülüne göre boyutlandırmaktır; her şeyi refleksle en yüksek katmana göre mühendislikle yönetmek değil. Vatandaşa dönük bir ödeme sistemi etkin-etkin artıklığı hak eder; iç bir raporlama aracı hak etmez.

## Takımınızla tartışılacak sorular

1. **Son ciddi olayınız yaşandığında üçünden (performans, ölçeklenebilirlik, dayanıklılık) hangisi gerçekten başarısız oldu ve doğru olanı mı düzelttiniz?** Bölüm bunları bilerek ayırır: bir sistem hızlı ama yük altında çökebilir, ölçeklenebilir ama bir bileşen ölünce devrilebilir ya da başarısızlıklardan sağ çıkarken yavaş olabilir. Takımlar çoğu zaman yanlış teşhis koyar; bir dayanıklılık sorununa kapasite ekler ya da bir dalgalanma için yetersiz kaynaklanmış bir sistemi sağlamlaştırır. Son iki ciddi olayı gözden geçirin ve hangi niteliğin bozulduğunu ve yanıtın gerçekte neyi iyileştirdiğini söyleyin. Ayrım çözümü değiştirir: ölçek için durumsuzluk ve parçalama, dayanıklılık için artıklık ve devre kesiciler, performans için profil çıkarma ve bütçeler. Kategoriyi doğru bulmak, tedaviye harcamakla bir belirtiye harcamak arasındaki farktır.

2. **Performans gerilemeleri boru hattınızı başarısız kılıyor mu, yoksa kimse fark etmeden kullanıcılara mı ulaşıyor?** Bir performans bütçesi (p95 gecikmesi, sayfanın etkileşimli olma süresi, işlem başına maliyet) yalnızca otomatik olarak zorlanırsa kullanıcıları korur; böylece onu aşan bir değişiklik yayına çıkmak yerine derlemeyi başarısız kılar. Çok katılımcılı büyük bir takımda gecikme binlerce küçük commit yoluyla sızar ve bir kapı olmadan kuyruk, bir lansman onu açığa çıkarana kadar yavaş yavaş çürür. Mevcut bütçelerinizi getirin ve bunların CI'a ve izlemeye bağlı olup olmadığını, ve ortalamalar yerine p95 ve p99'u hedefleyip hedeflemediğini kontrol edin, çünkü ölçekte kullanıcıların hissettiği kuyruktur. Bütçe olmayan yerde bir tane belirlemek ilk hamledir. Zorlama, iyi bir niyeti takım büyümesinden sağ çıkan bir özelliğe çevirir.

3. **Stres altında önce ne bırakılıyor ve bu sırayı siz mi tasarladınız, yoksa kesintide mi keşfedeceksiniz?** Zarif bozulma ve yük atma, sistemin çekirdeği korumak için gerekli olmayan işten vazgeçmesi demektir, ama yalnızca neyin gerekli olduğuna önceden karar verdiyseniz. Vatandaşa dönük bir hizmet için bu sıralama çoğu zaman bir politika kararıdır: durum panoları ve geçmiş sorgulamalar karanlığa gömülse bile bir vergi beyanını göndermek ayakta kalmalıdır. Kimse seçmemişse sistem ilk neyin başarısız olduğunu bırakır; bu da kullanıcıların en çok ihtiyaç duyduğu şey olabilir. Özelliklerinizi öncelik sırasına dizin ve mimarinin düşük öncelikli olanları (önbellekteki yanıtlar, kapatılan öneriler, kuyruğa alınan acil olmayan iş) kritik yolu da beraberinde götürmeden bırakabildiğini doğrulayın. Sonra gerçek yük altında sınayın, çünkü sınanmamış bozulma yalnızca bir umuttur.

4. **En kritik sisteminiz için RTO ve RPO nedir, bu sayıları gerçekte kim seçti ve bunları karşılayabildiğinizi en son ne zaman kanıtladınız?** Kurtarma Süresi Hedefi (ne kadar süre kapalı kalabileceğiniz) ve Kurtarma Noktası Hedefi (ne kadar veri kaybını göze alabileceğiniz) doğrudan maliyet sonuçları olan iş kararlarıdır; ama büyük bir takımda çoğu zaman hizmetten sorumlu kişilerin sahiplenmesi yerine çalıştırma kılavuzunu yazan kişi tarafından uydurulur. Karşıt çekim maliyet ile güvence arasındadır: RTO'yu bir saatten saniyelere ya da RPO'yu dakikalardan sıfıra indirmek altyapı faturasını katlayabilir; bu yüzden doğru sayı, en etkileyici olan değil, işin gerçekten ödeyeceği olandır. Belgelenmiş hedefleri, son gerçek yük devretme testinin tarihini ve o testin ürettiği ölçülen süreyi ve veri kaybını getirin, çünkü sınanmamış bir hedef bir dilektir. Kurumsal ve kamu ortamlarında bu sayılar yasa, sözleşme ya da SLA ile belirlenmiş olabilir; bu yüzden bunları kimin onayladığını ve son provanın yükümlülüğü karşılayıp karşılamadığını ya da sessizce kaçırıp kaçırmadığını söyleyin.

5. **En büyük öngörülebilir dalgalanmanız için otomatik ölçeklemenin o an tepki vermesine mi güveniyorsunuz, yoksa yükü tahmin edip, önceden hazırlayıp o hedefe karşı yük testi mi yaptınız?** Otomatik ölçekleme gecikmeyle tepki verir ve soğuk başlangıçlar tam en az kaldıramayacağınız anda gecikme ekler; bu yüzden bilinen bir adım değişikliği (bir beyan son tarihi, bir kayıt penceresi, bir satış etkinliği) tam da tepkisel ölçeklemenin başarısız olduğu ve bilinçli kapasite planlamanın kazandığı durumdur. Gerilim maliyettir: bir tepe için kapasiteyi önceden ısıtmak, yılın çoğunda boşta duran boşluk payı için ödeme yapmak demektir ve cazibe, otomatik ölçeklemenin bunu bedavaya karşılayacağını ummaktır. Geçen yılın tepe sayılarını, bu yılın büyümeli tahminini ve bugünün ortalama trafiğine değil, o tahminin bir katına kadar yürütülen yük testinin sonuçlarını getirin. Yasal olarak zamanlanmış bir dalgalanmayla karşılaşan bir devlet ya da kurumsal hizmet için bunu yanlış yapmanın sonucunu ekleyin; ilk gün çöken bir yardım portalı ya da vergi sistemi yalnızca yavaş bir öğleden sonra değil, bir kamu soruşturması olur.

6. **Üretimde hiç bilerek bir bileşeni çökerttiniz mi ve her sistemin artıklık katmanı kritikliğine ve maliyetine gerçekten uyuyor mu?** Hiç sınanmamış dayanıklılık bir hipotezdir ve satın alabileceğiniz katmanlar ucuz yedekten geri yüklemeden ılık yedeğe ve pahalı etkin-etkin çok bölgeye uzanır; bu yüzden disiplin, güvenceyi haklı olduğu yere harcamaktır; her şeyi yaldızlamak ya da hiçbir şeyi korumamak değil. Rekabet eden hususlar etki alanı ve bütçedir: kaos deneylerinin korkulukları ve bir iptal anahtarı olmalıdır; iç bir raporlama aracı için etkin-etkin israftır, bir ödeme platformu için yalnızca yedek ise ihmaldir. Tekil hata noktalarınızın envanterini, her kritik sistemin artıklık katmanını ve son denetimli hata enjeksiyonunun kanıtını ve neyi ortaya çıkardığını getirin. Kurumsal ve kamu portföylerinde her katmanı belgelenmiş bir kritiklik derecesine eşleyin; böylece bir denetçi paranın riski izlediğini görebilir ve harcamayı ilk kez kesinti sırasında savunmak zorunda kalan olmaz.

## Sektör merceği

**Girişim.** Bir lansmanın elli kayıt mı yoksa elli bin kayıt mı getireceğini tahmin edemezsiniz; bu yüzden ölçeği kurmak yerine satın alın: yönetilen bir yük dengeleyicinin arkasında durumsuz hizmetler çalıştırın ve platformun istek oranına göre otomatik ölçeklemesine izin verin. Tek bir mütevazı performans bütçesi belirleyin ve yönetilen veri depoları seçin; böylece bir sıçrama sabah ikide yeniden mimariyi zorlamaz. Çok bölgeli felaket kurtarmayı ve kaos programlarını şimdilik atlayın; sınanmış yedekleri tutun ve kıt mühendislik dikkatinizi, trafiğinizin henüz haklı çıkarmadığı artıklığa değil, ürüne harcayın.

**Küçük işletme.** Güvenilirlik uzmanı olmadan ve dar bir bütçeyle, satın alma ile kurma arasındaki seçim büyük ölçüde satın almaya eğilir: yönetilen bir platform ya da sunucusuz yığın, ölçeklemeyi ve yük devretmeyi sağlayıcının işi yapar ve iyi işletilen tek bir bölge genellikle yeterlidir. Dayanıklılığı, tutabileceğiniz az sayıda somut söz olarak çerçeveleyin; örneğin gerçekten bir kez geri yüklediğiniz bir gece yedeği ve müşterilere ilettiğiniz gerçekçi bir toparlanma penceresi gibi. Haklı çıkaracak trafiğiniz ya da kadronuz olmayan etkin-etkin ya da sürekli yük testi için ödeme yapmaktan kaçının.

**Kurumsal.** Sorun birçok takım arasındaki tutarlılıktır: CI'da zorlanan performans bütçelerini, paylaşılan bir dayanıklılık kalıpları kütüphanesini (zaman aşımları, devre kesiciler, bölmeler) ve her sistem için kritikliğine bağlı belgelenmiş bir artıklık katmanını standartlaştırın. Etkin-etkin çok bölgeyi birinci kademe hizmetlere ayırın, korkuluklu bir kaos mühendisliği programı ve üretimde oyun günleri yürütün ve bilinen dalgalanmalar için kapasite planlamayı sonradan düşünülen bir şey değil, takvimli bir disiplin olarak ele alın. RTO ve RPO'yu merkezi olarak yönetin; böylece her kritik sistemin bir denetçinin doğrulayabileceği, sahipli ve sınanmış hedefleri olur.

**Kamu.** Yük çoğu zaman yasal olarak zamanlanmıştır ve erişilebilirlik yükümlülükleri yasaldır; bu yüzden kapasite planlama, otomatik ölçeklemenin o an tepki vermesine dayanamaz: son tarih dalgalanmasını tahmin edin, önceden hazırlayın ve tahminin çok üzerinde yük testi yapın. Tedarik, RTO'yu, RPO'yu ve prova edilmiş yük devretmelerin bir takvimini satıcı vaatleri değil, sözleşmesel gereksinimler olarak belirtmeli ve kritik hizmetler için tek bölgeye kilitlenmekten kaçınmalıdır. Hangi yolun yasal olarak gerekli olduğuna (bir beyanı göndermek, bir yardım talep etmek) önceden karar verin; böylece bozulma önce durum panolarını ve sorgulamaları bırakır ve kimsenin fark etmeyeceğini ummak yerine kesintiler ve toparlanma konusunda halka karşı şeffaf olun.

## Örnekler

**Girişim.** Product Hunt'ta yayına giren küçük bir girişim elli kayıt mı yoksa elli bin kayıt mı alacağını tahmin edemez; bu yüzden hizmetlerini yönetilen bir yük dengeleyicinin arkasında durumsuz tutar ve platformun istek oranına göre otomatik ölçeklemesine izin verir. Tek bir mütevazı performans bütçesi belirler (sayfalar 95. yüzdelikte 300 ms altında yanıt verir) ve yönetilen bir veritabanı seçer; böylece bir trafik sıçraması sabah ikide yeniden mimariyi zorlamaz. Lansman günü dalgalanması geldiğinde site devrilmek yerine biraz yavaşlar ve takım günü bir kesintiyle savaşmak yerine yeni kullanıcılarla konuşarak geçirir.

**Kurumsal.** Bir yayın medyası şirketi, küresel yük dengelemenin arkasında birden fazla bölgede durumsuz hizmetler çalıştırır ve günlük en çok izlenme saati dalgasını izlemek için istek oranına göre otomatik ölçekler. Performans bütçeleri her sürümü p99 başlatma gecikmesinde denetler. Bir bölge başarısızlığında trafik otomatik olarak sağlıklı bölgelere kayar ve gerekli olmayan özellikler (kişiselleştirilmiş görseller, öneri yenilemesi) oynatmayı korumak için önce bozulur. Şirket üretimde sürekli kaos deneyleri yürütür, düzenli olarak örnekleri sonlandırır ve gecikme enjekte eder; böylece gerçek başarısızlıklar tatbikatlardan ayırt edilemez ve müşterinin göreceği bir kesintiye yol açmaz.

**Kamu.** Bir vergi dairesi, beyan sisteminin her yıl devasa, yasal olarak sabit bir son tarih dalgalanmasıyla karşılaştığını bilir. O an tepki vermesi için otomatik ölçeklemeye güvenmek yerine, tepe yükü önceki yıllardan tahmin eder, kapasiteyi haftalar önceden hazırlar ve tahminin yüzde 150'sine kadar yük testi yapar. Mimari, yük dengeleyicilerin arkasında durumsuzdur ve ılık yedekli ikinci bir bölgesi vardır. RTO ve RPO politikayla belirlenmiştir (gönderilen beyanlar için en fazla 15 dakika kesinti ve sıfıra yakın veri kaybı) ve yük devretme üç ayda bir prova edilir. Aşırı yük altında gerekli olmayan özellikler (durum panoları, geçmiş sorgulamalar) önce bırakılır; böylece yasal olarak gerekli yol olan beyan gönderimi erişilebilir kalır.

## İş gerekçesi: motivasyonlar, YG ve TSM

Ölçeklenebilirlik, performans ve dayanıklılık, başarısızlığın maliyetinin önlemin maliyetini kat kat aştığı klasik durumlardır. Ama önlem bütçede görünür ve başarısızlık yalnızca potansiyeldir; bu yüzden ilk felakete kadar kronik olarak yeterince fonlanmazlar. Benimseme maliyeti gerçektir: yedekli altyapı, çok bölgeli kapasite, yük testi ve kaos araçları ve durumsuzluğu ve dayanıklılık kalıplarını kurmak için mühendislik zamanı. Yatırım yapmamanın maliyeti, talebin tepesinde yüksek profilli bir kesintidir: ticarette dakika dakika kaybedilen gelir, devlet için kaçırılan yasal yükümlülükler ve kamu soruşturması, [hizmet düzeyi sözleşmesi](https://en.wikipedia.org/wiki/Service-level_agreement) (SLA) cezaları ve kalıcı itibar hasarı.

Vakayı yönetime iş dünyasının zaten anladığı sayılarla çerçeveleyin. Tepe sırasında bir saatlik kesintinin maliyetini (kaybedilen işlemler, cezalar, onarım, itibar) tahmin edin, sonra bunu onu önleyen artıklığın ve testin yıllık maliyetiyle karşılaştırın. Kritik sistemler için önlem hemen her zaman tek bir büyük olayın küçük bir kesridir. RTO ve RPO'yu açık paraya bağlayın: kesintinin saati başına ne kadar gelir ya da kaç işlem ve ne kadar veri kaybı yasal ya da ticari olarak tolere edilebilir. Performansı bir gelir ve memnuniyet kaldıracı olarak sunun, çünkü daha hızlı sistemler daha iyi dönüştürür ve işlem başına daha az maliyetlidir; dayanıklılığı ise primi kapsanan zarara göre küçük olan bir sigorta olarak sunun. En güçlü argüman, bu niteliklerin tasarıma katmanın ucuz ve sorunu zorlayan kesintiden sonra geriye dönük eklemenin yıkıcı olduğudur.

## Anti-kalıplar ve tuzaklar

- **Yapışkan oturumlar ve örnek içi durum.** Oturum durumunu sunucuda saklamak; serbest yatay ölçeklemeyi ve güvenli örnek değişimini engeller.
- **Kapasite planlama olarak otomatik ölçekleme.** Otomatik ölçeklemenin, tepki vermek için fazla yavaş olduğu bilinen bir adım değişikliği dalgalanmasını emeceğini varsaymak.
- **Boşluk payı olmadan sıcak çalışmak.** Neredeyse yüzde 100 kullanımda çalışıp sıçramaları ya da başarısızlıkları emecek hiçbir şey bırakmamak.
- **Profil çıkarmadan optimize etmek.** Darboğaz olmayan kodu ayarlarken gerçek olanın dokunulmadan kalması.
- **Kuyruğu görmezden gelmek.** p99 kullanıcıları acı çekerken ortalama gecikmeyi raporlamak; ortalamalar ölçekteki acıyı gizler.
- **Sınanmamış felaket kurtarma.** Hiç uygulanmamış ve gerektiğinde başarısız olacak bir felaket kurtarma planı ve yedekler.
- **Tekil hata noktaları.** Tek yük dengeleyici, tek veritabanı birincili, tek bölge: her şeyi çökerten yedeksiz bir bileşen.
- **Korkuluksuz kaos mühendisliği.** Etki alanı denetimi ya da iptal anahtarı olmadan başarısızlık enjekte etmek ve önlemek istediğiniz kesintiyi yaratmak.

## Olgunluk modeli

- **Düzey 1, Başlangıç.** Plansız ve tepkisel. Tek örnekli ya da dikey ölçeklenmiş, durumu sunucuda tutulan. Yük testi yok, performans bütçesi yok ve kimsenin geri yüklemediği ara sıra alınan yedeklerin ötesinde felaket kurtarma yok. Herhangi bir bileşen başarısızlığı tam bir kesintiye yol açar ve ölçek sorunları üretimde keşfedilir.
- **Düzey 2, Geliştirme.** Temel uygulamalar ortaya çıkar ama takımdan takıma değişir. Bazı hizmetler bir yük dengeleyicinin arkasında yatay ölçeklenmiş ve durumsuzdur; birkaçında temel otomatik ölçekleme vardır. Yük testi büyük lansmanlardan önce yapılır ama rutin değildir; yedekler vardır, felaket kurtarma ise belgelenmiş ama nadiren uygulanmıştır. Bir takımın iyi yaptığına bir başkası henüz başlamamıştır.
- **Düzey 3, Standartlaştırma.** Uygulamalar belgelenmiş ve kuruluş çapında uygulanır. Kapasite bilinen dalgalanmalar için boşluk payıyla planlanır, performans bütçeleri CI'da zorlanır; böylece gerilemeler derlemeyi başarısız kılar ve dayanıklılık kalıpları (zaman aşımları, sınırlı yeniden denemeler, devre kesiciler, bölmeler) ve zarif bozulma varsayılandır. RTO ve RPO sistem başına tanımlıdır, artıklık katmanları kritikliğe göre atanır ve felaket kurtarma yük devretmesi takımlar arasında düzenli bir takvimle sınanır.
- **Düzey 4, Yönetme.** Nitelikler taban çizgilerine karşı ölçülür ve denetlenir. Takımlar p95 ve p99 gecikmesini, hata bütçelerini ve tahmine karşı kullanımı ve boşluk payını izler ve ihlalleri lansmanda keşfetmek yerine alarmla yakalar. Sınanmış yük devretme süreleri hedef RTO ve RPO ile karşılaştırılır, bozulma ve yük atma eşikleri metriklerle doğrulanır ve sürümler ile kapasite hakkındaki başla ya da başlama kararları veriyle yönlendirilir. Sayılar taban çizgisinden saptığında boşluk, ortalamaların ardına gizlenmek yerine görünür ve sahiplidir.
- **Düzey 5, Orkestrasyon.** Ölçeklenebilirlik, performans ve dayanıklılık sürekli iyileştirilir ve kuruluş boyunca bütünleşir. Etkin-etkin çok bölge kritikliğin haklı çıkardığı her yerde kullanılır, kaos mühendisliği üretimdeki oyun günleri dahil sürekli çalışır ve kapasite tahmini doğrudan planlamayı ve tedariği besler. Dayanıklılık sürekli doğrulanır, toparlanma hedefleri tutarlı biçimde karşılanır ve kanıtlanır; mimari yük kalıpları ve risk tablosu değiştikçe uyum sağlar ve iş sürekliliği ile risk planlamasına bağlıdır.

## Tartışma fikirleri

1. Hizmetlerinizden hangileri hâlâ durumu örnekte tutuyor ve onları durumsuz yapmanızı ne engelliyor?
2. En kritik sisteminiz için RTO ve RPO nedir, bunları kim belirledi ve karşılayabildiğinizi en son ne zaman kanıtladınız?
3. Otomatik ölçekleme sizi gerçekten bilinen en büyük dalgalanmanıza karşı koruyor mu, yoksa yapamayacağı bir şeyi yapmasına mı güveniyorsunuz?
4. Kalan tekil hata noktanız nerede ve onu kaldırma planı nedir?
5. p99 gecikmesini ölçüp bütçeliyor musunuz, yoksa ortalamaların ardına mı saklanıyorsunuz?
6. Üretimde hiç bilerek bir bileşeni çökerttiniz mi? Çökertmediyseniz dayanıklılığınızın işe yaradığını nasıl biliyorsunuz?

## Önemli çıkarımlar

- Performansı, ölçeklenebilirliği ve dayanıklılığı ayırt edin; büyük bir sistemin üçüne de ihtiyacı vardır ve üçü de en baştan tasarlanmalıdır.
- Yatay ölçekleme ve durumsuz hizmetler; ölçeğin, erişilebilirliğin ve güvenli dağıtımın temelidir.
- Otomatik ölçeklemeyi, öngörülebilir ve iş açısından kritik dalgalanmalar için gerçek kapasite planlama ve boşluk payıyla birleştirin.
- Performansı, kritik yola ve kuyruğa odaklanarak, açık bütçelere karşı profil çıkarma ve yük testiyle yönlendirin.
- Dayanıklılığı zaman aşımları, devre kesiciler, bölmeler, zarif bozulma ve artıklıkla kurun, sonra kaos mühendisliğiyle doğrulayın.
- RTO ve RPO'yu iş kararları olarak belirleyin, felaket kurtarmayı her sistemin kritikliğine uyacak şekilde mühendislikle yönetin ve yük devretmeyi düzenli sınayın.

## Kaynaklar ve ileri okuma

- Martin Kleppmann, *Designing Data-Intensive Applications*
- Michael Nygard, *Release It!: Design and Deploy Production-Ready Software*
- Betsy Beyer et al. (Google), *Site Reliability Engineering* and *The Site Reliability Workbook*
- Casey Rosenthal and Nora Jones, *Chaos Engineering*
- Brendan Gregg, *Systems Performance: Enterprise and the Cloud*
- John Allspaw, *The Art of Capacity Planning*
- Ilya Grigorik, *High Performance Browser Networking*
- Nassim Nicholas Taleb, *Antifragile*
