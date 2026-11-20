# 9.1 Site güvenilirliği mühendisliği

## Genel bakış ve motivasyon

[Site güvenilirliği mühendisliği](https://en.wikipedia.org/wiki/Site_reliability_engineering) (SRE), yazılım mühendisliği uygulamalarını üretim sistemlerini işletmeye uygular. Operasyonu, geliştirmeden ayrı tutulan, elle yürütülen, bilet güdümlü bir iş olarak görmek yerine SRE, güvenilirliği kodla, ölçümle ve net hizmet hedefleriyle çözdüğünüz bir mühendislik sorunu olarak ele alır. Google tarafından yaygınlaştırılan ama artık geniş çapta benimsenen temel fikir basittir: sistemleri çalışır tutan insanlar zamanlarının çoğunu, aynı arızalarla tekrar tekrar elle boğuşmak yerine otomasyon kurmaya ve sistemleri iyileştirmeye harcamalıdır.

Büyük takımlar için bu önemlidir, çünkü ölçek güvenilirliğin hem değerini hem de yanlış yapmanın maliyetini artırır. Tek bir hizmet milyonlarca kullanıcıyı ya da binlerce dahili tüketiciyi desteklediğinde, bir saatlik kesinti kaybedilen gelir, kaçan işlemler ve aşınan güven demektir. Bir avuç sunucuda sorunsuz çalışan elle operasyonlar, yüzlerce hizmet ve [sürekli dağıtım](https://en.wikipedia.org/wiki/Continuous_deployment) altında çöker. SRE size güvenilirlik için ortak bir dil, özellik sevk etmek ile işleri istikrarlı tutmak arasındaki ödünleşimi açık hale getirmenin bir yolunu ve bu çizgiyi birçok takım boyunca tutarlı biçimde korumanın bir yolunu verir.

Kurumsal ve kamu bağlamları daha fazla ağırlık ekler. Bankacılık, sağlık ve kamu hizmetleri gibi düzenlenen sektörler çoğu zaman yasal ya da sözleşmesel erişilebilirlik taahhütleri, denetim gereklilikleri ve vatandaşları ya da güvenliği etkileyen kesintilere karşı çok az hoşgörü taşır. Devletin dijital hizmetleri güvenilirlik hedeflerini ve performans verilerini giderek daha fazla herkese açık yayımlıyor. SRE, "yeterince güvenilir"in ne demek olduğunu tanımlamanın, onu dürüstçe ölçmenin ve mühendislik önceliklerini yönetime ve gözetim kurumlarına görüşle değil veriyle savunmanın titiz, kanıta dayalı bir yolunu verir.

*Ayrıca bakınız:* bölüm 9.2 (gözlemlenebilirlik ve izleme), bölüm 9.3 (olay yönetimi) ve bölüm 3.5 (ölçeklenebilirlik, performans ve dayanıklılık).

## Temel ilkeler

- **Güvenilirlik en önemli özelliktir.** Çalışmayan bir sistem, kaç özelliği olursa olsun değersizdir; ama kusursuz güvenilirliğe ne ulaşılabilir ne de maliyetine değer.
- **Güvenilirliği ölçülebilir hedeflerle tanımlayın.** Hizmet düzeyi göstergeleri (SLI), hedefleri (SLO) ve sözleşmeleri (SLA), belirsiz beklentileri herkesin üzerinde anlaşabileceği sayılara çevirir.
- **Yüzde 100 yanlış hedeftir.** Kullanıcılar çok güvenilir bir sistemle kusursuz güvenilir bir sistem arasındaki farkı ayırt edemez; bu yüzden "yeterince güvenilir"i hedefleyin ve kalan bütçeyi hıza harcayın.
- **Hata bütçeleri teşvikleri hizalar.** SLO ile yüzde 100 arasındaki boşluk, geliştiricilerin ve operatörlerin paylaştığı bir risk bütçesidir ve tartışmaların yerine aritmetiği koyar.
- **Angarya düşmandır.** Tekrarlayan, elle yapılan, otomatikleştirilebilir operasyonel iş ölçülmeli, sınırlanmalı ve sistematik olarak ortadan kaldırılmalıdır.
- **Bilinçle otomatikleştirin.** Otomasyon, küçük bir takımın büyük bir sistemi işletmesinin yoludur; ona yatırım yapmak birinci sınıf bir mühendislik faaliyetidir.
- **Suçlamasız öğrenme.** Arızalar, bireyleri cezalandırma fırsatı değil, sistemleri ve süreçleri iyileştirme fırsatı olarak görülür.

## Öneriler

### SLI, SLO ve SLA'ları bilinçli biçimde tanımlayın

Kullanıcının bakış açısından başlayın. **[Hizmet düzeyi göstergesi](https://en.wikipedia.org/wiki/Service-level_indicator)**, bir hizmetin davranışının nicel bir ölçüsüdür; örneğin 300 milisaniyenin altında sunulan isteklerin oranı ya da başarılı yanıtların payı. Kullanıcı memnuniyetini gerçekten yansıtan az sayıda SLI seçin: erişilebilirlik, gecikme, doğruluk ve tazelik yaygın olanlardır. **[Hizmet düzeyi hedefi](https://en.wikipedia.org/wiki/Service-level_objective)**, bir SLI için hedef değer ya da aralıktır; örneğin "istekler arasında yüzde 99,9 başarı, 28 günlük kayan pencerede." **[Hizmet düzeyi sözleşmesi](https://en.wikipedia.org/wiki/Service-level_agreement)**, söz verilen bir düzeye bağlı sonuçları (iadeler, cezalar) olan bir sözleşmedir. SLO'larınızı SLA'larınızdan daha sıkı tutun; böylece bir taahhüdü ihlal etmeden önce uyarı alırsınız. SLO'larınızı yayımlayın, üç ayda bir gözden geçirin ve öğrendikçe sıkılaşan ya da gevşeyen yaşayan belgeler olarak görün.

### Hata bütçelerini benimseyin ve uygulayın

Hata bütçesi `%100 eksi SLO`dur. SLO'nuz yüzde 99,9 ise bütçeniz pencere başına yüzde 0,1 güvenilmezliktir, yani ayda kabaca 43 dakika. Bunu planlı riske harcayın: iddialı sürümler, deneyler ve kontrollü arıza testleri. Bütçe sağlıklıyken takımlar hızlı sevk edebilir. Bütçe tükendiğinde politika önceliği otomatik olarak güvenilirlik işine kaydırmalı ve sistem toparlanana kadar riskli değişiklikleri durdurmalıdır. Hata bütçesinin gücü, önceden üzerinde anlaşmanızdır; bu yüzden kesinti anındaki duyguyu ve politikayı ayıklar.

### Angaryayı ölçün ve azaltın

Angarya; elle yapılan, tekrarlayan, otomatikleştirilebilir, taktik ve sistemle birlikte büyüyen operasyonel işlerdir. SRE zamanının angaryaya giden yüzdesini izleyin ve bir tavan koyun (genellikle yüzde 50 civarı); böylece mühendislik zamanının en az yarısı kalıcı iyileştirmelere gider. Angarya azaltma projelerinden oluşan bir iş listesi tutun, sıklık çarpı maliyete göre önceliklendirin ve tekrarlayan bir görevi öldürmeyi yeni bir özellik sevk etmek kadar kutlayın. Bir **otomasyon yetkisi** bunu açık hale getirir: belirli bir sayıdan fazla elle yaptığınız her prosedür otomasyon ya da self servis araç adayı olur.

### Kapasiteyi planlayın ve talebi öngörün

Beklenen yükünüzü tarihsel eğilimlerden, planlı lansmanlardan ve iş projeksiyonlarından modelleyin. Organik büyüme öngörülerini pazarlama kampanyaları, vergi son tarihleri ya da devlette çok önemli olan yardım kayıt dönemleri gibi tek seferlik olaylarla birleştirin. Zirvenin üzerinde pay bırakın, varsayımlarınızı denetlemek için yük testi yapın, mümkün olan yerde ölçeklemeyi otomatikleştirin ve büyük taahhütler için insan gözden geçirmeli bir [kapasite planı](https://en.wikipedia.org/wiki/Capacity_planning) tutun. Bir yetersizlik sizi hazırlıksız yakalamasın diye tedarik bekleme sürelerini izleyin.

### Güvenilirliği gerçek maliyeti olan bir özellik olarak görün

Erişilebilirlikte fazladan her "dokuz", yedeklilikte, testte ve operasyonel inceliklerde genellikle bir öncekinden çok daha pahalıya gelir. Dokuzların maliyetini açık hale getirin; böylece ürün sahipleri hedefi gözleri açık seçer. Zarif bozulma için tasarlayın; böylece kısmi arızalar toplam kesinti yerine azaltılmış hizmet verir. Yedeklilik ve yük devretmeye, her bileşene eşit değil, SLO ile orantılı yatırım yapın.

### Bir SRE örgütlenme modeli seçin

Tek bir doğru yapı yoktur. **Merkezi** bir SRE takımı size tutarlılık, derin uzmanlık ve ortak araçlar sağlar, ama darboğaz ya da başkalarının sorunlarının çöplüğü haline gelebilir. **Gömülü** model, SRE'leri yakın iş birliği için ürün takımlarının içine yerleştirir, ama tutarsızlık ve yalıtılma riski taşır. Birçok büyük kurum bir melez kullanır: merkezi bir platform ve standartlar takımı artı gömülü güvenilirlik mühendisleri; bir hizmetin ne zaman SRE desteğine hak kazandığını ve önce hangi üretim hazırlığı çıtasını geçmesi gerektiğini tanımlayan net bir devreye alma modeliyle birlikte.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| Sıkı SLO'lar (daha çok dokuz) | Daha yüksek kullanıcı güveni, sözleşmeleri karşılar | Artan maliyet, daha yavaş özellik teslimi |
| Gevşek SLO'lar (daha az dokuz) | Daha hızlı sevk, daha düşük maliyet | Kullanıcı kaybı ve SLA cezası riski |
| Merkezi SRE | Tutarlılık, ortak uzmanlık | Darboğazlar, üründen uzaklık |
| Gömülü SRE | Yakın iş birliği, bağlam | Tutarsızlık, kadrolaması zor |
| Yoğun otomasyon yatırımı | Ölçeklenir, angaryayı azaltır | Başlangıç maliyeti, otomasyonun kendisi de başarısız olabilir |

Güvenilirlik mühendisliği, özünde sınırlı kaynakları akıllıca harcamakla ilgilidir. Kullanıcıların fark bile edemeyeceği fazladan bir dokuzun peşinde koşmak, özellikleri finanse edebilecek ya da fiyatları düşürebilecek parayı israf eder. Öbür yöne gidip arızaları gerçek zarara yol açan bir sisteme yetersiz yatırım yapmak ise ihmaldir. Hata bütçesi çerçevesi tam da bu ödünleşimi örtük ve çekişmeli olmaktan çıkarıp görünür ve pazarlığa açık kılmak için vardır. Örgütlenme modeli ödünleşimi de aynı ölçüde gerçektir: doğru yanıt şirket büyüklüğüne, mühendislik olgunluğuna ve hizmetlerinizin ne kadar tekdüze olduğuna bağlıdır.

## Takımınızla tartışılacak sorular

1. **Kullanıcılarınızın gerçekte hissettiği şeyi tam olarak hangi SLI yansıtıyor ve bunun bir gösteriş metriği olmadığını gösterebilir misiniz?** Yanlış göstergeyi seçerseniz kullanıcılar acı çekerken her pano yeşil görünür; bu bölümün uyardığı gösteriş-SLI tuzağı budur. Tartışmaya gerçek veri getirin: aynı kullanıcı yolculuğunu (oturum açmadan panoya, ödemeden onaya) sunucu CPU'su ya da bir arka uç sağlık denetimi yerine gerçek bir istek yolundan ölçün. Büyük bir takımda tek bir kötü SLI yayılır: düzinelerce hizmet onu devralır, uyarılar yanlış şey için tetiklenir ve hata bütçesi anlamını yitirir. Bir SLA'nın iade ya da vatandaş etkisi taşıdığı kurumsal ve kamu ortamlarında SLI'nız, denetçilere savunduğunuz kanıttır; bu yüzden kullanıcıya görünen başarıya doğrudan izlenebilmelidir. Sayıdan bir kullanıcının deneyimine çizgi çekemiyorsanız sayıyı değiştirin.

2. **Bir hizmet, SRE takımınızın onu nöbete almasından önce neyi kanıtlamalı ve hayır diyecek olan kim?** Üretim hazırlığı çıtası olmadan merkezi bir SRE takımı her kararsız hizmetin çöplüğü olur ve başkalarının teknik borcunda boğulur. Giriş ölçütlerini yazın: sahibi olan bir SLO, çalışan işletim kılavuzları, eyleme dönüştürülebilir uyarılar, kapasite payı ve gösterilmiş bir dağıt ve geri al yolu. Büyük bir kurumda bu devreye alma modeli, güvenilirlik takımının herkesi yavaşlatan bir darboğaz olmasını önleyen şeydir. Düzenlenen ortamlarda hazırlık incelemesi, gözetim kurumlarına gösterebileceğiniz bir kontrol işlevi de görür. Devreye almayı reddetme yetkisinin kimde olduğuna karar verin, çünkü kimsenin uygulamadığı çıta çıta değildir ve yanıt, SRE'nin ölçeklenip ölçeklenmeyeceğini ya da devralınan acı altında çöküp çökmeyeceğini değiştirir.

3. **Tek ve en büyük öngörülebilir zirveniz için ne kadar önceden kaynak ayırıyorsunuz ve tedarik bekleme sürenizi biliyor musunuz?** Bulut esnekliğinin anlık ve sonsuz olduğunu varsaymak, tam da en önemli zirvelerde yetersizliğe davetiye çıkarır; bu zirveler (vergi son tarihleri, kayıt pencereleri, indirim etkinlikleri) başarısızlığın en görünür ve en pahalı olduğu anlardır. Sayıları getirin: tarihsel zirve yükü, öngörülen büyüme, yük testi yaptığınız çarpan ve büyük ayrılmış kapasiteyi ya da uzmanlaşmış örnekleri edinmenin gerçek bekleme süresi. Devletin mevsimsel hizmetlerinde zirve normal yükün birkaç katı olabilir ve siyasi olarak kaçırılamaz; bu yüzden haftalar öncesinden kaynak ayırmak, otomatik ölçeklemenin yetişmesini ummaktan iyidir. Yanıt somut bir takvim belirlemelidir: ne zaman yük testi yaparsınız, ne zaman kapasiteyi kilitlersiniz ve "git" kararı kimin?

4. **Hata bütçeniz tükendiğinde gerçekte ne olur ve bunu uygulatma yetkisi kimde?** Tükendiğinde hiç harekete geçilmeyen bir hata bütçesi süsten ibarettir ve kesinti anı, politikayı sıfırdan pazarlamak için en kötü andır. Karşıt çekim gerçektir: taahhüt edilmiş bir lansman, bir gelir son tarihi ya da bir kamuya duyuru, riskli değişikliklerin dondurulmasına sert biçimde karşı basar. Yanma hızı verisini, önceden kararlaştırılmış politika metnini ve bütçenin son birkaç ihlalinin kaydını getirin; böylece dondurmanın gerçekten tutup tutmadığını görebilirsiniz. Büyük bir takımda bütçe ancak her grup aynı uygulamayı devralırsa teşvikleri hizalar; bu yüzden bir istisnayı kimin onaylayacağına ve o istisnanın nasıl kaydedileceğine önceden karar verin. Bir SLA'nın ceza ya da vatandaş etkisi taşıdığı kurumsal ve kamu ortamlarında istisna izi bir denetim kanıtına dönüşür; bu yüzden bütçe zaten tükendiğinde doğaçlama yapmak yerine hesap verecek sahibi şimdiden adlandırın.

5. **SRE takımınızın haftasının ne kadarı angarya ve bu ölçülmüş bir sayı mı, yoksa bir his mi?** Kimsenin saymadığı angarya sessizce genişler, ta ki takım bütün zamanını yangın söndürmeye harcayıp kalıcı iyileştirmeye hiç ayırmayana kadar; SRE'nin kurtulmak için var olduğu tuzak tam budur. Gerilim şudur: angaryayı ölçmek de iştir ve son tarih baskısı altındaki mühendisler saatlerinin nereye gittiğini kaydetmeye direnir. Dürüst bir örnek getirin: ortak bir angarya tanımına (elle yapılan, tekrarlayan, otomatikleştirilebilir, taktik ve sistemle birlikte ölçeklenen) karşı bir iki haftalık izlenen zaman, ayrıca sıklık çarpı maliyete göre sıralanmış otomasyon projeleri listesi. Büyük bir kurumda yüzde 50 tavanı ancak takım takım raporlanır ve savunulursa bir anlam taşır; bu yüzden sayıyı kimin gözden geçireceği ve bir takım tavanı aştığında ne olacağı üzerinde anlaşın. Düzenlenen ve kamu bağlamlarında angaryayı sınırlamak, elle operasyonların dışarıda bıraktığı kontrol ve denetim işi için kıt uzmanları serbest bırakır; bu yüzden angarya rakamını yönetimin görmesi gereken bir kapasite sinyali olarak ele alın.

6. **Hangi SRE örgütlenme modelini işletiyorsunuz ve onun artık uymadığını hangi kanıt söyler?** Merkezi bir takım tutarlılık ve ortak araçlar sağlar ama darboğaz olabilir; gömülü model bağlam sağlar ama tutarsızlığa kayar; çoğu büyük kurumun yerleştiği melez, net bir devreye alma modeline ihtiyaç duyar, yoksa her ikisinin zayıflıklarını da devralır. Gerginliği ortaya çıkaran sinyalleri getirin: hizmetlerin SRE desteği için ne kadar beklediği, güvenilirlik uygulamasının takımlar arasında ne kadar değiştiği ve gömülü mühendislerin profesyonel bir topluluktan kopuk hissedip hissetmediği. Doğru yanıt şirket büyüklüğüne, mühendislik olgunluğuna ve hizmetlerinizin ne kadar tekdüze olduğuna bağlıdır; bu yüzden ilk seçimi kalıcı saymak yerine bunlar değiştikçe yeniden gözden geçirin. Çok sayıda takımı ve sıkı tekdüzelik gereksinimleri olan bir kurumsal ya da kamu kuruluşunda, merkezi bir standartlar ve platform grubu artı gömülü güvenilirlik mühendisleri genellikle tutarlılığı yerel bağlamla dengeler; ancak bu yalnızca devreye alma modeli ve üretim hazırlığı çıtası yazılıysa ve birileri onlara sahipse işe yarar.

## Sektör merceği

**Girişim.** Bir avuç mühendisiniz varsa ve özel bir güvenilirlik takımına kaynağınız yoksa, en önemli kullanıcı yolculuğunda tek bir SLO seçin ve nöbeti bütün takımla paylaşın. Gözlemlenebilirlik altyapısı kurmak yerine bulut sağlayıcınızın yönetilen hizmetlerine ve yerleşik izlemesine yaslanın ve düzeltmelerin kalıcı olması için ortak bir belgede kısa olay sonrası incelemeler yazın. Burada hız süreçten daha önemlidir: gerçekten uyguladığınız gevşek bir SLO, kimsenin izlemediği ayrıntılı bir SLO'dan iyidir.

**Küçük işletme.** Güvenilirliği yürütecek bir uzmanınız yoksa onu platformunuz üzerinden satın aldığınız bir disiplin olarak görün: özel bir yığın yerine barındırılan çalışma süresi izleme, yönetilen veritabanları ve durum sayfası araçları. Faturaları ödeyen işlemlere bağlı bir ya da iki SLO belirleyin ve hangi arızaların size bir müşteriye mal olacağına dürüstçe karar verin. Dayanıklılığı, inşa etmekten ucuz olduğu yerde satın alın ve operasyonel yükü, mevcut mühendislerinizin özellik işiyle birlikte taşıyabileceği kadar hafif tutun.

**Kurumsal.** Zorluk, birçok takım boyunca tutarlılıktır: ortak bir SLO sözlüğü, ortak bir hata bütçesi politikası ve SRE'nin bir hizmeti nöbete almasından önce her hizmetin geçtiği bir üretim hazırlığı çıtası. Merkezi bir platform ve standartlar grubu artı gömülü güvenilirlik mühendisleri, darboğaz olmadan uygulamayı tekdüze tutar; yönetişim de hata bütçelerinin her yerde aynı biçimde raporlanıp uygulanmasını ister. Gözlemlenebilirlik altyapısına ve otomasyon yatırımına açıkça bütçe ayırın ve güvenilirliği, yönetimin görebileceği metriklerle bir portföy olarak yönetin.

**Kamu.** Kamu hizmetleri çoğu zaman yayımlanmış erişilebilirlik hedefleri, yasal taahhütler ve denetim yükümlülükleri taşır; bu yüzden SLO ve hata bütçesi kararları, gözetim kurumlarına savunduğunuz kayıtlara dönüşür. Satın alma kuralları hangi izleme ve barındırmayı kullanabileceğinizi kısıtlayabilir ve şeffaflık beklentileri güvenilirlik verisini herkese açık bir durum panosunda yayımlamaya iter. Vergi son tarihleri ve yardım kayıt pencereleri gibi aşırı mevsimsel zirvelere haftalar önceden hazırlanın ve suçlamasız bir olay sonrası inceleme kültürünü sürdürün; böylece kamuya açık arızalar bireysel suçlama yerine sistem iyileştirmesini besler.

## Örnekler

**Girişim.** On kişilik bir girişim tek bir web uygulaması işletiyor ve nöbeti üç mühendis arasında paylaşıyor. Karşılayamayacağı bir güvenilirlik takımı kurmak yerine tek bir anlamlı SLO seçiyor: oturum açmadan panoya akışta gerçek kullanıcı isteklerinden ölçülen yüzde 99,5 başarı. Kararsız bir üçüncü taraf API'si bu bütçeyi yemeye başladığında takım, bir sonraki özelliği sevk etmek yerine bir Cuma gününü yeniden deneme ve önbellek eklemeye harcıyor, ardından düzeltme kalıcı olsun diye ortak bir belgede iki paragraflık bir olay sonrası inceleme yazıyor.

**Kurumsal.** Küresel bir ödeme şirketi, işlem API'si için yüzde 99,99 erişilebilirlik SLO'su belirliyor; bu, ayda kabaca dört dakikalık bir hata bütçesi demek. Merkezi bir SRE platform takımı ortak [gözlemlenebilirliğin](https://en.wikipedia.org/wiki/Observability_(software)), olay araçlarının ve hata bütçesi politikasının sahibi; gömülü güvenilirlik mühendisleri ise her ürün grubunun içinde çalışıyor. Yeni bir sahtekarlık tespiti özelliği aylık bütçenin yarısını bir haftada yaktığında, önceden kararlaştırılmış politika güvenilirlik işi payı geri getirene kadar kritik olmayan sürümleri donduruyor. Yöneticiler bunu tartışmadan kabul ediyor, çünkü politikayı önceden onaylamışlardı.

**Kamu.** Ulusal bir vergi idaresi, yıllık son tarih çevresinde aşırı mevsimsel zirveleri olan bir çevrimiçi beyan hizmeti işletiyor. SRE takımı talebi önceki yılların verisi ile nüfus ve politika değişikliklerinden öngörüyor, normal zirvenin birkaç katına yük testi yapıyor ve kapasiteyi haftalar önceden ayırıyor. Erişilebilirlik ve sayfa gecikmesine ilişkin kamuya dönük SLO'lar bir durum panosunda yayımlanıyor. Suçlamasız bir [olay sonrası inceleme](https://en.wikipedia.org/wiki/Postmortem_documentation) kültürü (arızaları bireysel suç atamak yerine sistemleri iyileştirmek için gözden geçirmek) ve bir otomasyon yetkisi, beyan sezonuna bir zamanlar egemen olan elle müdahaleleri istikrarla azaltıyor; böylece personel, sistemi her son tarihte emzirmek yerine iyileştirmeye zaman ayırabiliyor.

## İş gerekçesi: motivasyonlar, YG ve TSM

SRE'nin getirisi üç kaynaktan gelir: önlenen kesinti, azalan operasyonel emek ve daha hızlı güvenli teslimat. Büyük bir hizmet için kesinti, kaybedilen gelir, cezalar ve onarım olarak saatte binlerden milyonlara varan bir maliyete yol açabilir; bu yüzden mütevazı güvenilirlik kazanımları bile bir takımın masrafını hızla çıkarır. Angarya azaltma, tekrarlayan elle maliyeti tek seferlik bir otomasyon yatırımına çevirir; böylece toplam sahip olma maliyeti ölçekle birlikte tırmanmak yerine ölçek büyüdükçe düşer. Hata bütçeleri, güvenilirlik sağlıklıyken işin daha hızlı sevk etmesine izin verir ve aşırı temkinli operasyonların masada bırakacağı özellik değerini yakalar.

Benimseme maliyeti gerçektir. SRE; yetenekli mühendislere, gözlemlenebilirlik altyapısına ve özellik son tarihleriyle yarışan bir kültürel değişime ihtiyaç duyar. Ama benimsememenin maliyeti ölçekte daha yüksektir: sınırsız operasyonel kadro, öngörülemez kesintiler, personelin tükenmesi ve ayrılması, ve niceliği zor ama yaşaması kolay itibar hasarı. Yönetime gerekçeyi sunmak için SRE'yi ölçülebilir getirileri olan bir risk yönetimi olarak çerçeveleyin. Olayların ve elle operasyonların mevcut maliyetini, iş taahhütlerine bağlı SLO hedeflerini ve ikisinde de öngörülen azalmayı sunun. Argümanı, yönetime güvenilirlik ile hız ödünleşimi üzerinde bir kaldıraç veren bir yönetişim aracı olarak hata bütçesi üzerine oturtun.

## Anti-kalıplar ve tuzaklar

- **Yeniden adlandırılmış operasyon olarak SRE.** Mühendislik zamanı, otomasyon yetkisi ve geri itme yetkisi olmadan bir operasyon takımını yeniden adlandırmak hiçbir şeyi değiştirmez.
- **Yüzde 100'ü hedeflemek.** Kusursuz güvenilirliğin peşinde koşmak, kullanıcıların fark edemeyeceği kazançlar için parayı israf eder ve teslimatı engeller.
- **Gösteriş SLI'ları.** Kullanıcıya görünen başarı yerine sunucu CPU'sunu ölçmek, kullanıcılar acı çekerken iyi görünen sayılar verir.
- **Dişsiz hata bütçeleri.** Tükendiğinde hiç uygulanmayan bir bütçe süsten ibarettir.
- **Ölçümsüz angarya.** Angaryayı izlemezseniz, hiçbir iyileştirme işi yapılamayana kadar takımı sessizce tüketir.
- **Çöplük olarak SRE.** Hazırlık çıtası olmadan her kararsız hizmeti devralan merkezi takımlar, başkalarının teknik borcunda boğulur.
- **Kapasite bekleme sürelerini yok saymak.** Bulut esnekliğinin anlık ve sonsuz olduğunu varsaymak, tam da en önemli zirvelerde yetersizliğe davetiye çıkarır.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Operasyonlar elle yürütülür ve reaktiftir. Resmi SLO yoktur, güvenilirlik bir görüş meselesidir ve yangın söndürme egemenken aynı olaylar tekrarlar. Otomasyon varsa tesadüfidir ve güvenilirliği bir mühendislik meselesi olarak kimse sahiplenmez.

**Düzey 2, Geliştirme.** Bazı hizmetlerin temel SLI ve SLO'ları ile ilkel izleme ve uyarıları vardır, ama uygulama takımlar arasında çok değişir. Angarya kabul edilir ama ölçülmez, otomasyon plansızdır ve olay sonrası incelemeler tutarsız yapılır. Güvenilirlik, kurum gerektirdiği için değil, bireylerin zorladığı köşelerde iyileşir.

**Düzey 3, Standartlaştırma.** SLI'lar, SLO'lar ve bir hata bütçesi politikası belgelenmiş ve takımlar boyunca tutarlı biçimde uygulanır. Angarya tanımlanmış ve izlenir, kapasite planlaması rutindir, üretim hazırlığı incelemeli bir SRE devreye alma modeli vardır ve otomasyon bir yan proje değil, finanse edilen bir iş akışıdır. Güvenilirlik uygulaması yazılıdır ve kuruluş genelinde uygulanır.

**Düzey 4, Yönetme.** Güvenilirlik programı, temel çizgilere karşı veriyle ölçülür ve kontrol edilir. Hata bütçesi yanma hızı, angarya yüzdesi, SLO tutturma, ortalama kurtarma süresi ve tedarik bekleme süreleri metrik olarak izlenir, sabit bir ritimle gözden geçirilir ve takımları hedeflerine bağlı tutmak için kullanılır. Bütçe ihlalleri kararlaştırılan dondurmayı tetikler, kapasite talep modellerine karşı öngörülür ve her git ya da gitme kararı görüşe değil kanıta dayanır.

**Düzey 5, Orkestrasyon.** Güvenilirlik mühendisliği kurum genelinde bütünleşmiş ve sürekli iyileştirilmiştir. Hata bütçesi politikası otomatiktir ve her yerde saygı görür, operasyonların çoğu self servistir, kapasite proaktif olarak ayrılır ve güvenilirlik verisi hız ile istikrar arasındaki uyarlanabilir ödünleşimleri yönlendirir. Kurum, iş ve risk tablosu değiştikçe SLO'ları rutin olarak yeniden kapsamlar, angaryayı emekliye ayırır ve güvenilirlik yatırımını yeniden dengeler.

## Tartışma fikirleri

- Bir kurum, onları sabitleyecek tarihsel güvenilirlik verisi yokken ilk SLO'larını nasıl belirlemeli?
- Hata bütçesi tükendiğinde ama büyük bir lansman taahhüt edilmişken, dondurmayı geçersiz kılma yetkisi kimde ve bu karar nasıl kaydedilir?
- Kurumunuz için merkezi, gömülü ya da melez SRE modellerinden hangisi doğru ve neyin değişiklik tetiklemesi gerekir?
- Fazladan bir dokuz erişilebilirliğin değerini, aynı yatırımın finanse edebileceği özelliklere karşı nasıl ölçersiniz?
- Sizin bağlamınızda angarya sayılan nedir ve değerli elle yargı ile ortadan kaldırılabilir tekrar arasındaki çizgi nerede?
- Güvenilirlik hedefleri, vatandaşa dönük devlet hizmetleri ile dahili kurumsal araçlar arasında nasıl farklılaşmalı?

## Önemli çıkarımlar

- SRE, yazılım mühendisliğini operasyonlara uygular ve güvenilirliği ölçülebilir, finanse edilebilir bir özellik olarak ele alır.
- SLI, SLO ve SLA'lar güvenilirliği görüşten üzerinde anlaşılmış sayılara çevirir; SLO'ları SLA'lardan daha sıkı tutun.
- Hata bütçesi, güvenilirlik ile hız ödünleşimini açık ve önceden pazarlanmış hale getirerek geliştiricileri ve operatörleri hizalar.
- Angaryayı ölçün ve sınırlayın, otomasyonu birinci sınıf mühendislik olarak görün; böylece operasyonlar doğrusaldan yavaş ölçeklenir.
- Kapasiteyi talep öngörülerinden planlayın ve özellikle mevsimsel zirveler için tedarik bekleme sürelerine saygı gösterin.
- Bir SRE örgütlenme modelini bilinçle seçin ve net bir devreye alma ve üretim hazırlığı çıtası tanımlayın.

## Kaynaklar ve ileri okuma

- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy, *Site Reliability Engineering: How Google Runs Production Systems*
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne, *The Site Reliability Workbook: Practical Ways to Implement SRE*
- David N. Blank-Edelman (editor), *Seeking SRE: Conversations About Running Production Systems at Scale*
- Thomas A. Limoncelli, Strata R. Chalup, Christina J. Hogan, *The Practice of Cloud System Administration*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
