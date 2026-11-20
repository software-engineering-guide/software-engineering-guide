# 3.2 Mimari üsluplar ve kalıplar

## Genel bakış ve motivasyon

Mimari üslup, bir sistemi düzenlemek için geniş, yeniden kullanılabilir bir biçimdir: nasıl ayrıştırıldığı, parçaların nasıl iletişim kurduğu ve sınırların nereye düştüğü. Birini seçmek, büyük bir kurumun verdiği en çok sonuç doğuran (ve en çok yanlış anlaşılan) kararlardan biridir. Seçim çoğu zaman takımın, alanın ve işletme gerçekliğinin gerçek kısıtlarını değil, modayı izler ("herkes [mikro hizmet](https://en.wikipedia.org/wiki/Microservices) yapıyor"). Sonunda iki karmaşadan birine düşersiniz: kurumun işletemediği dağıtık bir sistem ya da kimsenin güvenle değiştiremediği dolaşık bir [monolit](https://en.wikipedia.org/wiki/Monolithic_application). Hiçbiri üslubun suçu değildir. İkisi de üslubun duruma uydurulmamasından kaynaklanır.

Büyük geliştirici takımları için üsluplar, her şeyden önce [Conway Yasası](https://en.wikipedia.org/wiki/Conway%27s_law) yüzünden önemlidir: bir sistemin yapısı, onu inşa eden kurumun iletişim yapısını yansıtma eğilimindedir. Yani bir mimari üslup aynı zamanda bir örgüt tasarımı kararıdır. Bir sistemi hizmetlere bölmek, gerçekte takımları, sahipliği ve nöbet sorumluluğunu bölme kararıdır. Yüzlerce mühendisi olan kurumlar bağımsız dağıtıma sahip ince taneli hizmetleri karşılayabilir (ve çoğu zaman ihtiyaç duyar), çünkü birçok takım birbirini engellemeden bu bağımsızlık sayesinde sevkiyat yapar. Aynı kalıbı tek bir küçük takıma zorlarsanız, takım örgütsel yararın hiçbirini görmeden tüm işletme vergisini miras alır.

Kamu ve kurumsal ortamlar daha fazla kısıt ekler: uzun sistem ömürleri, sıkı değişiklik denetimi, satın alma döngüleri, yerleşik kayıt sistemleriyle entegrasyon ve denetlenebilirlik. Bunlar, sınırları açık ve bağımlılıkları incelemesi kolay tutan üslupları öne çıkarır. Bu bölüm başlıca üslupları gözden geçirir: monolitten mikro hizmetlere, [CQRS](https://en.wikipedia.org/wiki/Command_Query_Responsibility_Segregation) ve olay kaynağıyla [olay güdümlü mimarilere](https://en.wikipedia.org/wiki/Event-driven_architecture), [hizmet ağı](https://en.wikipedia.org/wiki/Service_mesh) ve ağ geçidi kalıplarına, [sunucusuza](https://en.wikipedia.org/wiki/Serverless_computing) ve [altıgen](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)) ve temiz mimarinin iç disiplinlerine. Daha da önemlisi, her birinin ne zaman uygun olduğunu ayırt etmenize yardım eder.

*Ayrıca bakın:* bölüm 2.2 (yazılım tasarım ilkeleri, [Alan Odaklı Tasarım](https://en.wikipedia.org/wiki/Domain-driven_design) dahil), bölüm 3.1 (mimari temelleri) ve bölüm 3.3 (dağıtık sistemler).

## Temel ilkeler

- **Üslup modayı değil, kuvvetleri izler.** Takım büyüklüğüne, alan karmaşıklığına, yüke ve işletme olgunluğuna göre seçin; bir teknoloji popüler diye asla.
- **Gerçek düşman, dağıtılabilir birimlerin sayısı değil, bağlaşımdır.** İyi modüllere ayrılmış bir monolit, dağıtık bir büyük çamur yumağından üstündür.
- **Dağıtım, bağımsızlık için ödediğiniz bir bedeldir.** Yalnızca bağımsız dağıtımın, ölçeklemenin ya da arıza yalıtımının değeri, ağ çağrılarının, kısmi başarısızlığın ve hizmetler arası veri tutarlılığının maliyetini aştığında bölün.
- **Sınırlar iş alanını izlemelidir.** Hizmetleri ve modülleri teknik katmanlarla değil, sınırlı bağlamlarla (her biri kendi açık sınırı olan kendi içinde bütün bir alan modeli) hizalayın.
- **Dışı ne olursa olsun içi iyi tasarlayın.** Altıgen/temiz katmanlama, her üslupta iş mantığını çerçevelerden ve altyapıdan bağımsız tutar.
- **Conway Yasası kaçınılmazdır, o halde ondan yararlanın.** Takım sınırlarını ve mimariyi birlikte tasarlayın.
- **İhtiyaç duyduğunuzu düşündüğünüzden daha basit başlayın.** İyi bir modüler monolitten hizmetler çıkarabilirsiniz; erken kurulmuş bir mikro hizmet karmaşasını geri dağıtmaktan çok daha zordur.

## Öneriler

### Varsayılan olarak modüler monolite başlayın; kanıtla bölün

Çoğu sisteme güçlü iç modül sınırlarıyla tek bir dağıtılabilir birim olarak başlayın: net arayüzler, başka bir modülün verisine uzanmama ve uygulanan bağımlılık kuralları. Basit işlemler, kolay yeniden düzenleme ve dağıtılıp gözlemlenecek tek bir şey elde edersiniz. Bir modülü yalnızca somut bir nedeniniz olduğunda kendi hizmetine ayırın: kendi başına ölçeklenmesi gereken bir parça, kendi temposunda dağıtım yapması gereken bir takım, yalıtmanız gereken bir arıza alanı ya da geri kalanından farklı bir teknoloji gereksinimi. Böldüğünüzde sınırlı bağlam çizgileri boyunca bölün; böylece her hizmet kendi verisinin sahibi olur ve kararlı bir sözleşme sunar.

### Mikro hizmetlerin ne zaman hak ettiğini bilin

Mikro hizmetler size bağımsız dağıtılabilirlik, bağımsız ölçekleme, arıza yalıtımı ve teknolojileri karıştırma özgürlüğü verir. Karşılığında olgun CI/CD (sürekli entegrasyon ve sürekli teslimat), otomatik altyapı, dağıtık izleme, hizmet keşfi ve bir nöbet kültürü talep ederler. Kendinize dürüstçe sorun: kurumunuz düzinelerce bağımsız dağıtılan hizmeti üretimde güvenilir biçimde çalıştırabilir mi? Platform ve işletme olgunluğu yoksa, mikro hizmetler yararlarını sunmadan yalnızca arıza biçimlerinizi çoğaltır. Birçok kurum, bir sürü küçük hizmet yerine büyük alanlara hizalanmış bir avuç iri taneli hizmetle en iyisini yapar.

### Ayrıştırma ve eşzamansızlığın karşılığını verdiği yerde olay güdümlü mimariyi kullanın

Olay güdümlü mimari, üreticilerin kimin tükettiğini bilmeden olgular yaymasına izin verir. Bu size gevşek bağlaşım, yük sıçramaları için bir tampon ve yeni tüketici eklemenin kolay bir yolunu sağlar. İş akışlarının doğal olarak eşzamansız ve tepkisel olduğu yerde kullanın. **CQRS** (Komut Sorgu Sorumluluk Ayrımı), yazma modelini bir ya da daha fazla okuma modelinden ayırır; okuma ve yazma yükleri ya da biçimleri keskin biçimde farklı olduğunda yardımcı olur. **Olay kaynağı**, durumu mevcut durum olarak değil, yalnızca eklemeli bir olay günlüğü olarak saklar; bu size kusursuz bir denetim izi ve zamanda yolculuk sağlar. "Bu değere nasıl ulaştık?" sorusunun yasal bir soru olduğu finans ve kamu için güçlüdür, ancak olayları sürümlemede, izdüşümleri yeniden kurmada ve nihai tutarlılık üzerine akıl yürütmede gerçek bir karmaşıklık ekler. Bunlara varsayılan olarak değil, bilerek başvurun.

### Çok sayıda hizmeti yönetmek için ağ geçidi, BFF ve ağ kalıplarını uygulayın

Bir **API ağ geçidi**, dış istemcilere tek bir giriş noktası sunar; kimlik doğrulamayı, hız sınırlamayı, yönlendirmeyi ve [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Transport Layer Security) sonlandırmayı yönetir. Bir **Ön Yüz için Arka Yüz (BFF)**, her istemci türüne (web, mobil, iş ortağı API'si) kendine göre uyarlanmış bir toplama katmanı verir; böylece şişkin, herkese uyan tek tip bir API'den kaçınırsınız. Bir **hizmet ağı**, kesen ilgi alanlarını (karşılıklı TLS, yeniden denemeler, zaman aşımları, trafik kaydırma ve telemetri) bir yan araç altyapı katmanına taşır; böylece uygulama takımlarının bunları yeniden gerçeklemesi gerekmez. Ağı yalnızca hizmet sayısı bu ilgi alanlarını hizmet başına yönetmeyi baş edilemez kıldığında ekleyin. Birkaç hizmet için bir ağ, değerinden fazla işletme yüküdür.

### Sunucusuzu dürüstçe tartın

Hizmet olarak işlev ve yönetilen sunucusuz platformlar, sunucu yönetimini üzerinizden alır, sıfıra ölçeklenir ve kullanıma göre faturalanır; bu, sıçramalı, olay güdümlü ya da düşük taban yüklü iş yükleri ve küçük takımlar için harikadır. Ödünleşimler gerçektir: soğuk başlatma gecikmesi, yürütme süresi ve kaynak sınırları, daha zor yerel test, olası satıcı bağımlılığı ve sürekli yüksek hacimde ayrılmış altyapıyı aşabilen maliyet. Sunucusuzu, ekonomisi ve işletme basitliği açıkça kazandığı yerde kullanın. Kararlı, yüksek verimli çekirdek sistemleri heveslenerek içine zorlamayın.

### Her hizmetin içinde iş mantığını temiz tutun

Dış üslup ne olursa olsun, içi **altıgen (portlar ve bağdaştırıcılar)** ya da **temiz mimariyle** temiz tutun: merkezde yalnızca soyutlamalara bağlı iş kuralları; kenarlarda değiştirilebilir bağdaştırıcılar olarak çerçeveler, veritabanları ve mesajlaşma. Bu, değerli alan mantığınızı altyapı olmadan sınanabilir ve teknoloji değişimleri boyunca taşınabilir tutar: birkaç çerçeve nesline dayanacak uzun ömürlü kamu ve kurumsal sistemler için belirleyici bir üstünlük.

## Ödünleşimler: artılar ve eksiler

| Üslup | En uygun olduğu durum | Artılar | Eksiler |
|---|---|---|---|
| Modüler monolit | Çoğu sistem, özellikle erken dönemde | Basit işletim, kolay işlemler ve yeniden düzenleme | Tek dağıtım birimi; tek parça olarak ölçeklenir; aşınma riski |
| Mikro hizmetler | Çok sayıda takım, yüksek ölçek, olgun platform | Bağımsız dağıtım/ölçekleme, arıza yalıtımı | Dağıtık karmaşıklık, veri tutarlılığı, yüksek işletme maliyeti |
| Olay güdümlü / CQRS / olay kaynağı | Eşzamansız iş akışları, denetim ihtiyaçları, ayrışan okuma/yazma | Gevşek bağlaşım, denetlenebilirlik, ölçeklenebilir okumalar | Nihai tutarlılık, olay sürümleme, daha zor hata ayıklama |
| Sunucusuz | Sıçramalı ya da düşük taban yüklü, olay güdümlü iş | Sunucu yönetimi yok, sıfıra ölçekleme, kullanım başına ödeme | Soğuk başlatmalar, sınırlar, bağımlılık, yüksek sürekli yükte maliyet |

Yinelenen tema şudur: esnekliği ve bağımsızlığı işletme ve bilişsel karmaşıklıkla satın alırsınız. Dağıtık ve olay güdümlü üsluplar, tek bir çağrı yığınının ve tek bir işlemin basitliğinden vazgeçerek bağımsız ölçekleme, dağıtım ve başarısız olma yeteneğini alır. Bu takas ölçekte ve olgun bir platformla karşılığını verir. Olgun platform yoksa yıkıcıdır. İç disiplinler (altıgen/temiz) neredeyse her zaman değerlidir, çünkü az maliyetlidir ve üslupları sonradan değiştirme seçeneğinizi açık tutar.

## Takımınızla tartışılacak sorular

1. **Bir sonraki hizmeti bölmeden önce, ona sahip olan takımı da bölecek misiniz ve bunu yapma yetkisi kimde?** Conway Yasası, bir hizmet sınırının gerçekte bir takım sınırı olduğu anlamına gelir; bu yüzden organizasyon şemasının desteklemediği bir bölme, dağıtık bir monolit üretir: iki dağıtılabilir birim, tek sürüm treni, ortak nöbet. Büyük bir kurumda takımları yeniden şekillendirme yetkisi genellikle mühendisliğin üzerinde, raporlama hatlarında, finansta ve İK'dadır; mimari ve örgüt tasarımının birlikte kararlaştırılması gerekmesinin nedeni budur. Tartışmaya kanıt getirin: önerilen hizmetin onu uçtan uca sahiplenebilecek, kendi nöbetini karşılayabilecek ve kendi temposunda dağıtım yapabilecek bir takımı var mı? Cevap hayırsa, ya takımı finanse edin ya da yeteneği monolitte bir modül olarak tutun. Sahipliği bölmeden kodu bölmek, dağıtımın tüm maliyetlerini alır ve bağımsızlığın hiçbirini getirmez.

2. **Hizmetlerinizin her birini bugün bağımsız dağıtabiliyor musunuz, yoksa gizlice eş adımla mı sevk ediliyorlar?** Dağıtık monolit bu bölümdeki en kötü sonuçtur: ağ çağrıları, kısmi başarısızlık ve hizmetler arası veri tutarlılığı için ödersiniz, ama yine de birini diğerleri olmadan yayımlayamazsınız. Ele veren işaretler ortak bir veritabanı, eşgüdümlü yükseltmeleri zorlayan ortak bir kütüphane ve tüm yapıyı birlikte çalıştırması gereken entegrasyon testleridir. Büyük bir takım için bu, verimi sessizce sınırlar, çünkü diyagram bağımsızlık gösterse de her takım tek bir sürümün arkasında sıraya girer. Yakın tarihli bir değişikliği alın ve onu güvenli kılmak için kaç hizmetin birlikte dağıtılması gerektiğini sayın; tek bir yeteneğe dokunan bir değişiklik için bu sayı birden büyükse sınırlarınız yanlıştır. Çözüm genellikle daha fazla hizmet eklemek değil, her hizmete kendi verisini ve kararlı, sürümlü bir sözleşme vermektir.

3. **Mevcut hizmet bölmelerinizden hangileri karşılığını vermeyi bıraktı ve onları yeniden birleştirir miydiniz?** Bölümün en gelişmiş alışkanlığı, üslup kararlarını geri döndürülebilir saymaktır: bir etken ortaya çıktığında ayırın, etken ortadan kalktığında yeniden birleştirin. Çoğu kurum yalnızca böler, böylece nano hizmetler ve gevezelik eden varlık hizmetleri, orkestrasyon ve ağ yükü her hizmetin yaptığı işi gölgede bırakana kadar birikir. Her zaman birlikte dağıtılan, bir iş yeteneği yerine bir veritabanı tablosu yüzünden var olan ya da ağ sıçramaları artık bir isteğin gecikmesine hâkim olan hizmetleri arayın. Kadro ve bütçelerin mercek altında olduğu kurumsal ve kamu ortamlarında, iki ince hizmeti tek bir iri taneli hizmete geri katlamak bir başarısızlık itirafı değil, meşru ve maliyet kısan bir hamledir. Yeniden birleştirmeyi ayırma kadar açıkça masaya koyun ve ikisine de aynı kanıtla karar verin.

4. **Platformunuz ve nöbet olgunluğunuz önerdiğiniz üslubu gerçekten destekliyor mu ve bağlanmadan önce belirli boşlukları sayabiliyor musunuz?** Mikro hizmetler, ağlar ve olay güdümlü omurgalar yararlarını yalnızca olgun CI/CD, dağıtık izleme, hizmet keşfi ve kısmi başarısızlık üzerine akıl yürütebilen bir nöbet kültürü üzerinde sunar. Büyük bir kurum hedef üslubu bir mimari forumunda kararlaştırıp eksik platformu daha sonra, düzinelerce hizmet zaten üretimdeyken ve her olayın teşhisi saatler sürerken keşfetme eğilimindedir. Bağımsız dağıtım ve ölçeklemenin çekiciliğini, sabaha karşı 3'te onu kimin çalıştırdığı sorusunun ağır başlılığıyla tartın: takımları paralel sevkiyat yapmaya özgürleştiren bölme, her takımın anlaması gereken arıza biçimlerini de çoğaltır. Tartışmaya dürüst bir envanter getirin: mevcut dağıtım sıklığı, ortalama kurtarma süresi, hizmet sınırları boyunca izlemeniz olup olmadığı ve tek bir takımın gerçekçi olarak kaç hizmeti işletebileceği. Kurumsal ve kamu ortamlarında, eksik olduğunuz platform yetenekleri için satın alma ve işe alım sürelerini ekleyin, çünkü finanse etmediğiniz bir ağı ve bir platform takımını varsayan bir üslup, desteklenemeyen bir yapıyı işletme planıdır.

5. **Alanın hangi bölümleri için tam bir olay kaynaklı denetim izi bir kolaylık değil, yasal zorunluluktur ve karar yetkisi kimde?** Olay kaynağı ve CQRS size kusursuz, yeniden kurulabilir bir geçmiş ve kendi başlarına ölçeklenen okuma modelleri satın alır; ancak sistemin ömrü boyunca olay sürümleme, izdüşüm yeniden kurmaları ve nihai tutarlılık üzerine akıl yürütme maliyeti taşırlar. Denetim izine hiç ihtiyaç duymamış bir alana uygulandığında bu karmaşıklık salt vergidir; "bu değere nasıl ulaştık?" sorusunun yasal bir soru olduğu bir alandan esirgendiğinde yokluğu bir uyum başarısızlığıdır. Rekabet eden hususlar bir yanda denetlenebilirlik ve sorgu ölçeklenebilirliği, diğer yanda hata ayıklama zorluğu ve geliştirici bilişsel yüküdür; bu yüzden karar, kalıba en hevesli olanın değil, hem düzenleyici yükümlülüğü hem işletme yükünü anlayanların elindedir. Belirli yasal ya da sözleşmesel saklama ve yeniden kurma gereksinimlerini, beklenen olay hacmini ve sürümleme ve izdüşüm işinin dürüst bir tahminini getirin. Bir kararı yıllar sonra yeniden kurmanın yasal bir görev olabildiği finans, vergi ve kamuda, belirli bir sınırlı bağlamın değişmez bir olay günlüğü gerektirip gerektirmediğini onaylayan hesap verebilir sahibi adlandırın.

6. **Sonradan çıkarmanın ucuz kalması için modüler monolitin aşınmasını nasıl önleyeceksiniz ve sınırları ne uygulatacak?** Modüler monolitle başlamanın tüm gerekçesi, temiz iç sınırların sonraki hizmet çıkarmayı karşılanabilir kılacağı vaadine dayanır; oysa bu sınırlar, bir son tarih bir modülü başkasının verisine uzanmaya ikna ettiği anda sessizce çürür. Çok sayıda katkıcısı olan büyük bir takım için iyi niyet ve kod incelemesi tek başına çizgiyi tutmaz; uygulatan bir mekanizma olmadan monolit, üslubun kaçınmak için tasarlandığı büyük çamur yumağına sessizce dönüşür. Uygulanan bağımlılık kurallarının ve modül arayüzlerinin sürtünmesini, yıllar sonra hiçbir sınırın gerçek olmadığını ve her çıkarmanın paylaşılan durumu çözmek anlamına geldiğini keşfetmenin maliyetiyle tartın. Kanıt getirin: modül sınırları derleme araçlarıyla, statik analizle ya da paket yapısıyla mı uygulanıyor, yoksa son altı birleştirmenin görmezden geldiği salt belgelenmiş gelenekler mi? Sıkı değişiklik denetimine ve birkaç çerçeve nesline dayanması gereken uzun ömürlü kurumsal ve kamu sistemlerinde, sınır uygulamasını denetlenebilir bir kontrol olarak ele alın; böylece sonradan dağıtma seçeneği, hâlâ elinizde olduğunu varsaydığınız değil, gerçekten korumuş olduğunuz bir seçenek olur.

## Sektör merceği

**Girişim.** Tek bir modüler monolite varsayılan olarak başlayın ve mikro hizmetlerin çekimine direnin, çünkü en kıt kaynağınız mühendislik dikkatidir ve bir hizmet sürüsü, ürün-pazar uyumundan önce karşılayamayacağınız işletme vergisidir. Sonradan çıkarabilmek için temiz modül sınırlarını koruyun ve sıfıra ölçekleme ile kullanım başına ödemenin sıçramalı, düşük taban yükünüze uyduğu yerde sunucusuza başvurun. Yalnızca somut bir etken ortaya çıktığında, örneğin ani yükle gelen bir bildirim göndericisi gibi, tam olarak bir şeyi ayırın ve daha erken asla.

**Küçük işletme.** Platform takımı ve dar bütçe olmadan, yönetilen bir platform üzerinde bir monoliti ya da bir avuç iri hizmeti tercih edin ve ağları, izlemeyi ve hizmet keşfini kendiniz kurmak yerine barındırılan altyapı satın alın. Sunucusuzu ve yönetilen veritabanlarını hiç sunucu işletmemenin bir yolu olarak tartın ve işletme yükünü taşıyacak kimsenizin olmadığı dağıtık bir tasarımdan sakının. Doğru mimari, bir iki kişinin gerçekten dağıtıp gözlemleyebileceği ve kurtarabileceği mimaridir.

**Kurumsal.** Gerçek sorun çok sayıda takım ve Conway Yasasıdır: iri taneli hizmetleri sınırlı bağlamlarla ve takım sahipliğiyle hizalayın ve dağıtımı güvenli kılan platforma (CI/CD, izleme, ağ ve hizmet keşfi) bilinçli yatırım yapın. Ağ geçidi, BFF ve iç temiz mimari kalıplarını standartlaştırın; böylece gruplar onları yeniden icat etmeyi bırakır ve ayırmayı ve yeniden birleştirmeyi yerel tercih olarak değil, kanıta dayalı portföy kararları olarak yönetin. Her bölmenin işletme maliyetini açıkça bütçeleyin, çünkü sizin ölçeğinizde dağıtık monolit başarısızlığı pahalıdır ve çözülmesi yavaştır.

**Kamu.** Uzun sistem ömürleri, sıkı değişiklik denetimi, satın alma döngüleri ve denetlenebilirlik seçimi şekillendirir: açık, incelenebilir sınırları ve satıcıları ve çerçeve nesillerini aşan kalıcı sözleşmeleri olan üslupları tercih edin. Olay kaynağı, vatandaşa dönük bir kararı yeniden kurmanın yasal görev olduğu yerde karmaşıklığını hak eder; bu yüzden onu çekirdek defterler için bilinçli kullanın ve her bütçeyle değişen kuralları yalıtmak için her hizmetin içinde temiz mimariyi koruyun. Tescilli sunucusuz ya da satıcı platformlarından taşınabilirliği ve çıkışı sonradan akla gelenler değil, satın alma gereksinimleri olarak ele alın.

## Örnekler

**Girişim.** Bir zamanlama ürünü geliştiren dört kişilik bir girişim, bir rakip onlar hakkında blog yazdığı için mikro hizmetlerle başlama baskısı hissediyor, ama direniyor. Tek bir dağıtılabilir birimde ayrı modüller olarak net iç sınırları olan (zamanlama, faturalama, bildirimler) tek bir modüler monolit sevk ediyorlar; böylece bir mühendis her şeyi yerelde çalıştırabiliyor ve bir sürüm tek bir itme oluyor. Ürün ilgi görmeye başladığında, ani yük altında e-postaya ve SMS'e yayılan yalnızca bildirim göndericisi kendi hizmetine çıkarılıyor. Hâlâ ürün-pazar uyumunu ararken, bir düzine hizmetin işletme vergisinin hiçbirini miras almıyorlar.

**Kurumsal.** Büyük bir e-ticaret şirketi modüler bir monolit olarak başlıyor. Trafik büyüdükçe ve takımlar çoğaldıkça, en yüksek yüklü, en bağımsız evrilen alanları (katalog, sepet, ödeme ve arama) her biri kendi verisinin sahibi ayrı hizmetlere çıkarıyor. Ödeme, envanter, karşılama ve analitiğin bir olay omurgası üzerinden tükettiği olaylar yayıyor; böylece yeni tüketiciler (sahtecilik tespiti, sadakat) ödemeye dokunmadan bağlanabiliyor. Bir API ağ geçidi kimlik doğrulamayı ve hız sınırlamayı yönetiyor ve bir BFF mobil için yükleri uyarlıyor. Kalan düşük trafikli alanlar monolitte kalıyor; bu da gereksiz parçalanmayı önlüyor.

**Kamu.** Bir vergi idaresi, çekirdek defter için olay kaynağı üzerine bir tarhiyat platformu kuruyor, çünkü bir mükellefin yükümlülüğündeki her değişiklik yıllarca yeniden kurulabilir ve yasal olarak denetlenebilir olmalı. Komutlar (beyanname ver, ödeme uygula, düzeltme çıkar) değişmez olaylar üretiyor ve okuma modelleri memurlar ve vatandaşlar için güncel bakiyeleri izdüşürüyor. CQRS, kamuya dönük sorgu tarafının yazma tarafını riske atmadan yoğun beyan sezonu için kendi başına ölçeklenmesini sağlıyor. İçeride her hizmet temiz mimariyi izliyor; böylece her bütçeyle değişen tarhiyat kuralları kalıcılık ve mesajlaşma teknolojisinden yalıtılmış kalıyor.

## İş gerekçesi: motivasyonlar, YG ve TSM

Bir üslup seçiminde söz konusu olan para çok büyüktür, çünkü karar geri döndürülmesi pahalı bir karardır. Mikro hizmetleri çok erken benimserseniz, platform inşası, yinelenen altyapı, dağıtık hata ayıklama ve daha ağır bir işletme yükü yoluyla toplam sahip olma maliyetini şişirirsiniz: sistemin ömrü boyunca sizinle kalan maliyetler. Gerçekten aşırı yüklenmiş bir monoliti bölmeyi reddederseniz teslimat verimini sınırlarsınız: takımlar paylaşılan bir sürümün arkasında sıraya girer ve her değişiklik tüm sistemi riske atar. YG konuşması gerçekte işletme harcamasını örgütsel ihtiyaçla eşleştirmekle ilgilidir.

Yönetime gerekçeyi teknoloji cinsinden değil, verim ve risk cinsinden sunun. Bağımsız dağıtılabilirlik, paralel sevkiyat yapan daha fazla takım ve daha kısa teslim süreleri demektir: ölçülebilir iş hızı. Arıza yalıtımı, daha az toplam kesinti ve daha küçük bir patlama yarıçapı demektir: ölçülebilir erişilebilirlik ve itibar koruması. Ancak her üslubun talep ettiği platform yatırımı konusunda da aynı ölçüde dürüst olun: bir ağ, izleme ve CI/CD olgunluğu isteğe bağlı ekstralar değil, ön koşullardır ve maliyetleri TSM'ye aittir. Birçok kurum için en ucuz yol, şimdilik iyi modüllere ayrılmış bir monolittir; temiz iç sınırlar sonraki çıkarmayı ucuz kılar. Bu size, ihtiyaç duymadan önce bedelini ödemeden dağıtma seçeneğini satın alır.

## Anti-kalıplar ve tuzaklar

- **Dağıtık monolit.** Birlikte dağıtılması gereken ve bir veritabanını paylaşan hizmetler: dağıtımın tüm maliyeti, bağımsızlığın hiçbiri.
- **Nano hizmetler.** Orkestrasyon ve ağ yükünün yaptıkları işi gölgede bıraktığı kadar ince taneli hizmetler.
- **Platformsuz mikro hizmetler.** CI/CD, izleme ve nöbet olgunluğunuz olmadan bölmek; arıza biçimleri çoğalır.
- **Varlık hizmetleri.** İş yeteneğine göre değil, veritabanı tablosuna göre bölmek ("Kullanıcı hizmeti", "Sipariş hizmeti"); her işlem için gevezelik eden hizmetler arası çağrıları zorlar.
- **Her yerde olay kaynağı.** Denetim izine ihtiyaç duymayan alanlara uygulamak; hiçbir yarar olmadan karmaşıklık vergisini ödemek.
- **Monolit olarak ağ geçidi.** İş mantığını API ağ geçidine koymak; merkezi bir tıkanma noktasını yeniden yaratmak.
- **Çerçeveye bağlı çekirdek.** Web ya da ORM (nesne-ilişkisel eşleme) çerçevesiyle iç içe geçmiş iş mantığı; hem testi hem teknoloji değişimini acılı kılar.

## Olgunluk modeli

- **Düzey 1, Başlangıç.** Üslup modayla ya da tesadüfen seçilir. Tek bir dolaşık monolitiniz ya da kazara bir dağıtık karmaşanız vardır, sınırlar alanı değil teknik katmanları ya da tarihi izler ve bölmeler bir şey bozulduğunda tepkisel olarak olur.
- **Düzey 2, Geliştirme.** Bazı takımlar monolitin içinde bilinçli modül sınırları çizer ya da birkaç iri hizmet kurar ve bazı kesen ilgi alanları tutarlı yönetilir. Uygulama eşitsizdir: bir grup hizmetleri sınırlı bağlamlarla hizalarken diğeri hâlâ veritabanı tablosuna göre böler ve çıkarma geçici kalır.
- **Düzey 3, Standartlaştırma.** Belgelenmiş bir yaklaşım kurum genelinde uygulanır: hizmetler sınırlı bağlamlarla hizalanır ve kendi verilerinin sahibidir, ağ geçidi ve BFF kalıpları uygun yerlerde kullanılır, iç temiz ya da altıgen katmanlama standarttır ve her bölme belirtilmiş bir etken gerektirir. Modül sınırları yalnızca gelenekle değil, araçlarla uygulanır.
- **Düzey 4, Yönetme.** Üslup kararları temel çizgilere göre ölçülür ve denetlenir. Hizmet başına dağıtım sıklığını ve teslim süresini, ortalama kurtarma süresini, tipik bir değişiklik için kaç hizmetin birlikte dağıtılması gerektiğini ve ağ sıçraması gecikmesini izlersiniz ve her bölmenin maliyetini satın alması amaçlanan bağımsızlıkla karşılaştırırsınız. Bir sınırın ayakta kalıp kalmadığını tercih değil kanıt belirler ve dağıtık monolite doğru sapma bir kesintiyle değil, metriklerle yakalanır.
- **Düzey 5, Orkestrasyon.** Mimari örgüt tasarımıyla bütünleşiktir ve sürekli uyarlanır. Olgun bir platform (CI/CD, izleme ve gerektiğinde ağ) hem dağıtımı hem yeniden birleştirmeyi ucuz kılar, takımlar bir etken ortaya çıktığında rutin olarak çıkarır ve ortadan kalktığında hizmetleri geri katlar ve üslup seçimleri takım topolojisi, yük ve risk tablosu tüm yapı boyunca değiştikçe yeniden dengelenir.

## Tartışma fikirleri

1. Sisteminizin neresinde bir monolit gerçekten bir güçtür ve neresinde gerçek bir darboğazdır?
2. Bir sonraki hizmetinizi çıkarmayı hangi somut etken haklı kılar ve onu inşa etmeden önce adlandırabilir misiniz?
3. Kurumunuz mikro hizmetlerin talep ettiği işletme olgunluğuna sahip mi? Eksik olan ne?
4. Alanınızın hangi bölümleri için tam bir olay kaynaklı denetim izi yasal ya da iş zorunluluğu, hangileri için olsa güzel olur?
5. Mevcut hizmet sınırlarınız takım sınırlarınızı ne kadar iyi yansıtıyor ve bu hizalama yardımcı mı oluyor, zarar mı veriyor?
6. Gelecek yıl web çerçevenizi ya da veritabanınızı değiştirmeniz gerekse, iş mantığınızın ne kadarını yeniden yazmanız gerekirdi?

## Önemli çıkarımlar

- Mimari üslubu moda değil, gerçek kuvvetlerden (takım büyüklüğü, alan, yük, işletme olgunluğu) seçin.
- Modüler monolit çoğu sistem için doğru varsayılandır; hizmetleri yalnızca somut bir etkenle ve sınırlı bağlam çizgileri boyunca çıkarın.
- Mikro hizmetler, işletme ve bilişsel karmaşıklığı bağımsız dağıtım, ölçekleme ve arıza yalıtımıyla takas eder; olgun bir platform gerektirirler.
- Olay güdümlü mimari, CQRS ve olay kaynağı, nihai tutarlılık ve sürümleme karmaşıklığı pahasına ayrıştırma ve denetlenebilirlik sunar; bilinçli benimseyin.
- Ağ geçitleri, BFF'ler ve ağlar çok hizmetli yapıları evcilleştirir ama ağırlık ekler; ölçek gerektirdiğinde tanıtın, daha önce değil.
- Değerli iş mantığını sınanabilir ve teknoloji değişimi boyunca kalıcı tutmak için her hizmetin içinde altıgen/temiz mimariyi uygulayın.

## Kaynaklar ve ileri okuma

- Sam Newman, *Building Microservices* and *Monolith to Microservices*
- Chris Richardson, *Microservices Patterns*
- Eric Evans, *Domain-Driven Design*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Robert C. Martin, *Clean Architecture*
- Alistair Cockburn, "Hexagonal Architecture (Ports and Adapters)"
- Gregor Hohpe and Bobby Woolf, *Enterprise Integration Patterns*
- Martin Fowler, *Patterns of Enterprise Application Architecture* (and articles on CQRS and Event Sourcing)
- Matthew Skelton and Manuel Pais, *Team Topologies*
