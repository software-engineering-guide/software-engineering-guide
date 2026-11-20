# 2.6 Sürüm kontrolü ve kaynak yönetimi

## Genel bakış ve motivasyon

[Sürüm kontrolünü](https://en.wikipedia.org/wiki/Version_control) kod tabanınızın kayıt sistemi olarak düşünün. Her değişikliği, kimin, ne zaman ve neden yaptığını yakalar ve birçok insanın birbirinin işini ezmeden aynı yazılım üzerinde çalışmasını sağlar. Büyük bir kuruluş için bir yedekten çok daha fazlasıdır. İş birliğinin, [sürekli entegrasyonun](https://en.wikipedia.org/wiki/Continuous_integration) (CI), denetimin ve sürüm yönetiminin üzerine oturduğu temeldir. Dallanma, depo yapısı ve commit disiplini hakkında verdiğiniz kararlar, takımınızın ne kadar hızlı ve ne kadar güvenle hareket edebileceğini biçimlendirir.

Büyük takımlar için kaynak yönetimi gerçekte ölçekte bir eşgüdüm sorunudur. Yüzlerce mühendis paylaşılan koda değişiklik gönderdiğinde, birleştirmeleri küçük tutan, ana hattı yayımlanabilir tutan ve geçmişi okunabilir tutan bir stratejiye ihtiyaç duyarlar. Sürekli entegre eden bir takım akıcı ilerler. Dalların haftalarca ayrışmasına izin veren bir takım bir entegrasyon krizinden diğerine sendeler. Depo yapınız, tek büyük depo ya da çok sayıda, takımların kodu nasıl paylaştığını ve eşgüdümü nasıl sağladığını da biçimlendirir.

Kurumsal ve kamu ortamları birkaç talep daha ekler: izlenebilirlik, erişim kontrolü ve saklama. Bir değişikliğin denetim için onaylı bir iş kalemine bağlanması gerekebilir. Sırlar asla geçmişe girmemelidir. Depo erişimi güvenlik sınırlarına saygı göstermelidir. Burada sürüm kontrolü uygulamalarınız kuruluşun kontrol çerçevesinin parçası olur ve sızdırılmış bir sır ya da denetlenemeyen bir geçmiş gibi bir hata ciddi sonuçlar doğurabilir.

## Temel ilkeler

- Küçük değişiklikleri sık entegre edin; uzun ayrışma birleştirme acısının kökenidir.
- Ana hattı her zaman yayımlanabilir tutun.
- Geçmiş belgedir; commit'leri nedenini anlaması gereken gelecekteki okuyucu için yazın.
- Asla sır commit'lemeyin; geçmişe ulaşan her sırrı ele geçirilmiş sayın.
- Hijyenin uygulanmasını yalnızca disipline güvenmek yerine otomatikleştirin (kancalar, CI kontrolleri).
- Depo yapısını (tek ya da çok depo) modaya göre değil, takımların kodu gerçekte nasıl paylaştığına ve eşgüdümü nasıl sağladığına göre seçin.
- İzlenebilirlik için değişiklikleri gerekçelerine (iş kalemleri, biletler ya da kararlar) bağlayın.

## Öneriler

### Kısa ömürlü dallarla gövde tabanlı geliştirmeyi tercih edin

[Gövde tabanlı geliştirmeye](https://en.wikipedia.org/wiki/Trunk-based_development) yönelin: haftalarla değil saat ya da günlerle ölçülen kısa ömürlü özellik dalları kullanarak paylaşılan bir ana hatta sık entegre edin. Kısa dallar birleştirmeleri küçük ve entegrasyonu sürekli tutar ve bu alışkanlık yüksek teslimat performansıyla güçlü biçimde ilişkilidir. İş henüz bitmediğinde onu uzun ömürlü bir dalda park etmeyin. Bitmemiş işi gizleyen çalışma zamanı anahtarları olan [özellik bayraklarını](https://en.wikipedia.org/wiki/Feature_toggle) kullanın; böylece onu güvenle birleştirebilirsiniz. Uzun ömürlü sürüm dallarını gerçek çok sürümlü destek için saklayın ve taşıdıkları bakım maliyetini bilerek girin.

### Sürüm temponuza uyan bir dallanma modeli seçin

[Dallanma modelinizi](https://en.wikipedia.org/wiki/Branching_(version_control)) gerçekte nasıl yayımladığınıza uydurun. Sürekli dağıtım yapıyorsanız, asgari dallanmalı gövde tabanlı geliştirme size iyi hizmet eder. Müşterilere sürümlü sürümler gönderiyorsanız ya da aynı anda birkaç canlı sürümü destekliyorsanız, sürüm dallarına ve geri taşımaya ihtiyaç duyabilirsiniz. Sürüm modeliniz gerçekten gerektirmedikçe birçok uzun ömürlü dalı olan ağır modellerden uzak durun, çünkü birleştirme ve bakım yükünü çoğaltırlar.

### Tek depo ile çok depo arasında bilinçli karar verin

Takımlar kodu yoğun paylaştığında, atomik projeler arası değişiklikler gerektiğinde ve birleşik araçlar ve görünürlük istendiğinde birçok projeyi tutan tek bir depo olan [tek depoya](https://en.wikipedia.org/wiki/Monorepo) başvurun. Karşılığında ölçeklenmiş derleme araçlarına ve erişim kontrollerine ihtiyacı kabul edersiniz. Takımlar ve hizmetler gerçekten bağımsız olduğunda, yalıtılmış erişim ve sürüm döngüleri istendiğinde ve atomik depolar arası değişikliklere ihtiyaç olmadığında, proje ya da hizmet başına ayrı depolara, yani çok depoya, başvurun. Karşılığında depolara yayılan değişiklikleri eşgüdümleme maliyetini kabul edersiniz. İkisi de ölçekte çalışır. Sürekli sürtünme yaratan, bağlaşım kalıbınız için yanlış seçimdir.

### Commit hijyenini ve geleneksel commit'leri uygulayın

Bir değişikliğin yalnızca ne olduğunu değil, neden yapıldığını açıklayan commit mesajları isteyin. Mesajlar yapılandırılmış ve makine tarafından ayrıştırılabilir olsun diye geleneksel commit'ler gibi bir kural benimseyin; bu, değişiklik günlüklerini ve sürümlemeyi otomatikleştirmenizi sağlar. Geçmiş ikiye bölünebilir ve geri alması kolay kalsın diye commit'leri atomik, her biri tek bir mantıksal değişiklik, tutun. Hafızaya yaslanmak yerine kancaların ve CI kontrollerinin mesaj biçimini ve temel hijyeni uygulamasına izin verin.

### Büyük ikili dosyaları ve üretilmiş kodu olağan geçmişin dışında tutun

Büyük ikili varlıkları doğrudan ana geçmişe commit'lemeyin, çünkü her klonu sonsuza dek şişirirler. Bunun yerine büyük dosya depolama mekanizması ya da bir yapıt deposu kullanın. Kural olarak üretilmiş kodu da commit'lemekten kaçının; onu derlemede üretin. Üretilmiş bir yapıtı gerçekten commit'lemeniz gerektiğinde, onu yalıtın ve incelemeleri ve farkları kirletmemesi için açıkça işaretleyin.

### Sırların depoya asla girmesini önleyin

Kimlik bilgileri daha inmeden engellensin diye otomatik sır taramasını commit öncesi kancalarınıza ve CI'ye koyun. Mühendislere düzgün bir sır yönetim sistemi verin; böylece bir kimlik bilgisini koda gömme ihtiyacı hiç doğmasın. Ve geçmişe ulaşan her sırrı ele geçirilmiş sayın: hemen döndürün. Bir sır itilip klonlandıktan sonra onu geçmişten kaldırmak zor ve güvenilmezdir.

### Erişim kontrolü ve izlenebilirlik kurun

Depo erişimini güvenlik sınırlarına ve [en az ayrıcalığa](https://en.wikipedia.org/wiki/Principle_of_least_privilege) saygı gösterecek biçimde kurun. Her değişikliğin gerekçesine izlenebilmesi için commit'leri ya da çekme isteklerini iş kalemlerine bağlayın; bu hem günlük mühendislik bağlamına hem denetime yardımcı olur. Hiçbir şey üzerinde anlaştığınız kapıları geçmeden birleşmesin diye kilit dallarınızı gerekli kontroller ve incelemelerle koruyun.

## Ödünleşimler: artılar ve eksiler

| Seçim | Artılar | Eksiler |
|---|---|---|
| Gövde tabanlı geliştirme | Sürekli entegrasyon; küçük birleştirmeler; yüksek akış | Özellik bayrakları ve disiplin gerektirir; daha az yalıtım |
| Uzun ömürlü özellik dalları | Süren işin güçlü yalıtımı | Acı verici birleştirmeler; gecikmiş entegrasyon; sapma |
| Tek depo | Atomik projeler arası değişiklikler; paylaşılan araçlar; görünürlük | Ölçeklenmiş derleme araçları gerektirir; varsayılan olarak kaba erişim kontrolü |
| Çok depo | Bağımsız sürümler; yalıtılmış erişim; depo başına basit araçlar | Depolar arası değişiklikler zor; sürüm eşgüdümü yükü |
| Geleneksel commit'ler | Otomatik değişiklik günlükleri ve sürümleme; tutarlı geçmiş | Baştan kural; uygulama gerekir |

Buradaki büyük ödünleşim entegrasyon sıklığı ile yalıtım arasındadır. Uzun ömürlü dallar daha güvenli hissettirir, çünkü işiniz kendi başına bir yanda durur; ama pahalı birleştirmelere ve sonradan entegrasyon sürprizlerine yol açan tam da bu yalıtımdır. Gövde tabanlı geliştirme bu yalıtım hissinden sürekli, ucuz entegrasyon karşılığında vazgeçer ve sizden özellik bayrakları ve disiplin getirmenizi ister. Tek depo ve çok depo kararı, projeler arası kolaylığı takım bağımsızlığıyla takas eder. Kodunuzun gerçekte ne kadar sıkı bağlı olduğuna uyanı seçin.

## Takımınızla tartışılacak sorular

1. **Korumalı ana hattınıza hiçbir şey birleşmeden önce hangi kontroller geçmeli ve o ana hat gerçekten her zaman yayımlanabilir mi?** Bu bölüm yayımlanabilir bir ana hattı temel ilke olarak ele alır ve kırık ya da incelenmemiş kodun herkesin bağımlı olduğu dala ulaştığı korumasız bir ana hattı anti-kalıp olarak adlandırır. Büyük bir takımda kırmızı bir ana hat herkesi aynı anda engeller; bu yüzden istediğiniz kapı kişisel değil, paylaşılan bir güvenlik özelliğidir. Kanıtı getirin: dal korumanızın bugün gerçekte neyi uyguladığı ve ana hattın şu anda ne sıklıkla bozuk olduğu. Gerekli kümeye, geçen testlere, güvenlik taramalarına ve incelemeye karar verin ve ana hattı umutla değil politikayla yayımlanabilir yapın. O kapı, birçok insanın korkmadan sürekli entegre etmesini sağlayan şeydir.

2. **Geleneksel commit'leri benimsemek, otomatikleştirdiği şeyler düşünüldüğünde takımınız için kural yüküne değer mi?** Bölüm yapılandırılmış, makine tarafından ayrıştırılabilir commit mesajlarını tam olarak değişiklik günlüklerini ve sürümlemeyi otomatikleştirmenizi sağladıkları için önerir ve geçmiş ikiye bölünebilir ve geri alınabilir kalsın diye atomik commit'ler ister. Ödünleşim gerçektir: baştan bir kural öder ve uygulamaya ihtiyaç duyarsınız; karşılığında üretilmiş sürüm notları ve güvenilir geçmiş alırsınız. Bugün elle yaptığınız şeylerin sinyalini getirin; örneğin değişiklik günlüklerini elle yazmak ya da bir gerilemeyi hangi commit'in getirdiğini aramak. Sık yayımlıyor ya da birden fazla sürüm sürdürüyorsanız otomasyon genellikle kendini öder; nadiren sürüm çıkarıyorsanız daha hafif bir kural yeterli olabilir. Biçimi kancaların ve CI'nin uygulamasına bırakın ki hafızaya yaslanmasın.

3. **Depo yapınızın talep ettiği operasyonel maliyeti, ister tek depo araçları ister depolar arası eşgüdüm olsun, kabul ettiniz mi?** Bu bölüm hem tek deponun hem çok deponun ölçekte çalıştığını ve sürekli sürtünme yaratanın bağlaşım kalıbınız için yanlış seçim olduğunu söyler. Bir tek depo ölçeklenmiş derleme araçlarına ve daha ince taneli erişim kontrolüne ihtiyaç duyar; çok depolar ise depolara yayılan her değişikliği sürüm kayması riskiyle bir eşgüdüm projesine çevirir. Somut sinyali getirin: değişikliklerinizin ne sıklıkla proje sınırlarını geçtiği ve derleme ve erişim araçlarınızın sahip olduğunuz yapıyı taşıyıp taşıyamadığı. Projeler arası atomik değişiklikler yaygınsa tek depo araçlarına yatırım yapın; takımlar ve hizmetler gerçekten bağımsızsa depolar arası eşgüdüm maliyetini bilinçli kabul edin. Amaç yapıyı kodunuzun gerçekte ne kadar sıkı bağlı olduğuna uydurmak ve sonra o yapının gerektirdiği araçları finanse etmektir.

4. **Yoğun bir depoya şu anda canlı bir kimlik bilgisi commit'lense, onu ne kadar çabuk algılarsınız ve döndürme umut değil gerçekten otomatik mi?** Bu bölüm geçmişe ulaşan her sırrı ele geçirilmiş sayar ve sonradan kaldırmanın zor ve güvenilmez olduğunu uyarır; bu yüzden önleme ve hızlı döndürme tek gerçek savunmadır. Büyük bir takım için maruziyet bileşiktir: paylaşılan bir depoya itilen bir sır dakikalar içinde onlarca makineye klonlanır ve CI önbelleklerine yansıtılır; bu yüzden yavaş bir insan tepkisi bir ihlali garanti eder. Karşıt değerlendirme sürtünmedir: agresif commit öncesi tarama ve zorunlu döndürme insanları yavaşlatır ve yanlış pozitifler üretir; bu yüzden kontrolleri kapatmak yerine ayarlamalısınız. Kanıtı getirin: sır taramasının hem commit öncesi kancalarda hem CI'de çalışıp çalışmadığı, bilinen bir sızıntıyı algılama ve döndürme ortalama süreniz ve mühendislerin kimlik bilgisini koda gömme cazibesini ortadan kaldıran bir sır yönetim sistemine sahip olup olmadığı. Kurumsal ve kamu ortamlarında bunu olay sürecinize ve saklama kurallarınıza bağlayın, çünkü denetlenebilir bir geçmişteki sızdırılmış bir kimlik bilgisi hem güvenlik hem uyum olayıdır ve düzenleyici kimin bildiğini ve ne kadar hızlı hareket ettiğini soracaktır.

5. **Dallarınız gerçekten kısa ömürlü mü ve değilse, bitmemiş iş neden bir özellik bayrağının ardında gizlenmek yerine bir dalda park ediliyor?** Bölüm, uzun ayrışma birleştirme acısının kökeni olduğu için gövde tabanlı geliştirmeye güçlü biçimde yönelir ve özellik bayraklarını, tamamlanmamış işi haftalarca yalıtmak yerine güvenle birleştirmenize izin veren mekanizma olarak sunar. Büyük bir takımda bu bir kişisel tercih değil, bir eşgüdüm özelliğidir: haftalarca yaşayan her dal, birinin sonunda uzlaştırması gereken gerçekliğin özel bir çatalı olur ve o uzlaştırmanın maliyeti kadro sayısıyla büyür. Karşıt değerlendirme, özellik bayraklarının kendi maliyetini taşımasıdır; çalışma zamanı karmaşıklığı, kombinasyonları test etmek ve emekliye ayrılması gereken bayatlamış bayraklar dahil. Veriyi getirin: dal ömürlerinizin gerçek dağılımı, entegrasyonun ne sıklıkla çatışma ya da sürpriz ürettiği ve şu anda kaç uzun ömürlü dal olduğu ve neden. Büyük ya da düzenlemeye tabi bir kuruluş için sürüm resmini ekleyin; çünkü gerçek çok sürümlü destek, disiplinli geri taşımayla uzun ömürlü sürüm dallarını haklı çıkarabilir ve bu, günlük özellik işini ana hattın dışına park etmekten farklı bir karardır.

6. **Geçmişinizdeki her değişiklik doğru güvenlik sınırları içinde yazarına ve gerekçesine izlenebilir mi ve bu bir denetime dayanır mı?** Bu bölüm erişim kontrolünü, en az ayrıcalığı ve değişiklikleri iş kalemlerine bağlamayı isteğe bağlı cila değil, kuruluşun kontrol çerçevesinin parçası olarak ele alır. Büyük bir takım için izlenebilirlik, opak bir commit akışını bir olay ya da uyum incelemesi sırasında akıl yürütebileceğiniz bir şeye çeviren şeydir ve erişim sınırları tek bir ele geçirilmiş hesabın asla dokunmaması gereken koda ulaşmasını engelleyen şeydir. Karşıt değerlendirme geliştirici hızıdır: zorunlu iş kalemi bağlantıları, ince taneli izinler ve gerekli incelemeler, küçük ve hızlı hareket eden bir takımın makul biçimde atlayabileceği tören ekler. Kanıtı getirin: korumalı dalların iddia ettiğiniz kontrolleri ve incelemeleri gerçekten isteyip istemediği, commit'lerin onaylı iş kalemlerine gerçekten atıfta bulunup bulunmadığı ve erişimin bugün gerçek güvenlik sınırlarınıza nasıl eşlendiği. Kurumsal ve kamu bağlamlarında bunu sınıflandırma, saklama ve denetim yükümlülüklerine bağlayın, çünkü denetlenemeyen bir geçmiş ya da aşırı geniş bir erişim izni, bir programı durdurabilen ya da bir akreditasyonu başarısız kılabilen bir bulgu olur.

## Sektör merceği

**Girişim.** Hız ve hayatta kalma kazanır. Tek bir depo kullanın, gövde tabanlı çalışın, kısa ömürlü dalları günde birkaç kez birleştirin ve bitmemiş işi uzun dallar yerine basit özellik bayraklarının ardında gizleyin. Sır taramasını ilk commit'ten açın, çünkü herkese açık bir depodaki sızdırılmış bir anahtar, onu sınırlayacak güvenlik takımı olmayan bir şirketi batırabilir. Ayrıntılı dallanma modellerini ve ağır süreci atlayın; korumalı bir ana dal ve anlamlı commit mesajları hızlı hareket etmek için yeterli disiplindir.

**Küçük işletme.** Özel bir platform ya da DevOps uzmanı ve sıkı bir bütçe olmadan, yönetilen varsayılanları inşa etmek yerine satın alın. Barındırılan bir Git sağlayıcısı size dal korumasını, gerekli incelemeleri ve sır taramasını kutudan çıktığı gibi verir; bu yüzden sürdüremeyeceğiniz bir sunucuyu kendiniz barındırmak yerine onlara yaslanın. Kararı veri hijyeni olarak çerçeveleyin: hangi depoların hassas yapılandırma tuttuğunu bilin, kimlik bilgilerini sağlayıcının sır yöneticisinde tutun ve platformun gerçekten ihtiyaç duyduğunuz birkaç kuralı uygulamasına izin verin.

**Kurumsal.** Zor sorun birçok takım boyunca tutarlılıktır. Dal korumasını, commit kurallarını ve sır taramasını kuruluş çapında politika olarak standartlaştırın ki gruplar onları yeniden icat etmeyi bıraksın ve tek depo ile çok depo seçimini bağlaşım kalıbına göre bilinçli yapın; talep ettiği ölçeklenmiş derleme araçlarını ya da depolar arası eşgüdümü finanse edin. Değişiklikleri kod sahipliği kurallarıyla doğru inceleyicilere yönlendirin, izlenebilirlik için commit'leri iş kalemlerine bağlayın ve sürüm kontrolü hijyenini bireysel alışkanlık meselesi olarak değil, sahipleri ve metrikleri olan yönetilen bir kontrol olarak ele alın.

**Kamu.** Tedarik kuralları, şeffaflık ve kamusal hesap verebilirlik tüm kurulumu biçimlendirir. Her commit'in onaylı bir iş kalemine atıfta bulunmasını isteyin, erişimi sınıflandırma sınırı başına denetleyin ve sır taramasını ve anında döndürmeyi belgelenmiş bir olay süreci altında zorunlu kılın. Sitelerin hepsinin aynı anda yükseltemediği yerlerde, uzun ömürlü sürüm dalları ve disiplinli geri taşıma ile birden fazla dağıtılmış sürümü destekleyin ve geçmişi denetlenebilir ve saklanmış tutun; böylece akreditasyon, bilgi edinme ve gözetim talepleri telaşsız cevaplanabilsin.

## Örnekler

**Girişim.** Üç kişilik bir girişim hem alışkanlıktan hem zorunluluktan gövde tabanlı çalışır; kısa ömürlü dalları günde birkaç kez main'e birleştirir ve yarım kalmış özellikleri basit bayrakların ardında gizler. Sır taramasını ilk commit'ten CI'de açarlar, çünkü herkese açık bir depodaki sızdırılmış bir API anahtarı, sonuçlarını sınırlayacak güvenlik takımı olmayan bir şirketi batırabilir. Tek bir depo, korumalı bir main dalı ve anlamlı commit mesajları, kendi geçmişlerine takılmadan hızlı hareket etmeleri için yeterli disiplini verir.

**Kurumsal.** Büyük bir teknoloji şirketi yüzlerce hizmet ve paylaşılan kütüphaneden oluşan bir tek depo işletir. Ölçeklenmiş derleme araçları ve kod sahipliği kuralları her değişikliği doğru inceleyicilere yönlendirir. Tek bir commit, paylaşılan bir kütüphaneyi ve her tüketiciyi aynı anda atomik olarak güncelleyebilir; bu, dağıtık depoları rahatsız eden sürüm kayması sorunlarını atlatır. Özellik bayraklı gövde tabanlı geliştirme ana hattı yayımlanabilir tutar ve sır taraması tüm depoda kimlik bilgilerini commit anında engeller.

**Kamu.** Ulusal bir savunma yüklenicisi sıkı izlenebilirliği sürdürür. Her commit onaylı bir iş kalemine atıfta bulunmalıdır. Dal koruması geçen güvenlik taramaları ve bağımsız inceleme ister ve erişim sınıflandırma sınırı başına sıkı denetlenir. Sır taraması zorunludur ve açığa çıkan her kimlik bilgisi bir olay süreci altında anında döndürmeyi tetikler. Uzun ömürlü sürüm dalları, hepsi aynı anda yükseltemeyen sitelerde birden fazla dağıtılmış sürümü destekler ve güvenlik düzeltmeleri disiplinli biçimde geri taşınır.

## İş gerekçesi: motivasyonlar, YG ve TSM

Sağlam kaynak yönetimini benimsemek neredeyse bedavadır ve onsuz kalmak pahalıdır. Gövde tabanlı geliştirme ve sürekli entegrasyon, yüksek yazılım teslimat performansıyla en güçlü biçimde ilişkilendirilen uygulamalar arasındadır; bu da daha iyi kurumsal sonuçlarla ilişkilidir. Temiz, izlenebilir geçmiş olayları teşhis etme ve denetimleri karşılama süresini keser ve disiplinli dallanma sizi entegrasyon krizlerinin ve birleştirme maratonlarının yinelenen, bütçelenmemiş maliyetinden kurtarır.

En büyük dengesiz risk sürüm kontrolündeki sırlardır. Tek bir sızdırılmış kimlik bilgisi, maliyeti herhangi bir araç yatırımını gölgede bırakan bir ihlale yol açabilir ve geçmiş bu tür sızıntıların kalıcı olmasını sağlar. Onları önlemek ucuzdur; sonrasını temizlemek değildir. Kötü yapı seçimleri kronik sürtünme olarak ortaya çıkar: her depolar arası değişiklik bir eşgüdüm projesine ya da her tek depo derlemesi bir darboğaza dönüşür. Gerekçeyi liderliğe sunmak için dallanma stratejinizi teslimat metriklerine ve olay teşhis süresine bağlayın ve sır taramasını ve erişim kontrolünü yüksek maliyetli ihlal ve denetim riskine karşı düşük maliyetli kontroller olarak çerçeveleyin.

## Anti-kalıplar ve tuzaklar

- **Uzun ömürlü ayrışan dallar:** acı verici, riskli entegrasyon olaylarına birleşen haftalarca yalıtılmış iş.
- **Geçmişteki sırlar:** klonlarda sonsuza dek kalan ve açığa çıktığında döndürmeyi gerektiren koda gömülü kimlik bilgileri.
- **Büyük ikili dosyaları ana geçmişe commit'lemek:** her klonu kalıcı olarak şişirmek ve tüm işlemleri yavaşlatmak.
- **Anlamsız commit mesajları:** geçmişin belge olarak değerini yok eden "fix", "wip", "changes".
- **Üretilmiş kodu elle yazılmış gibi commit'lemek:** gürültülü farklar, birleştirme çatışmaları ve doğruluk kaynağı konusunda kafa karışıklığı.
- **Bağlaşım için yanlış depo yapısı:** sıkı bağlı kod için çok depo ya da ölçeklenmiş araçlar olmadan tek depo.
- **Korumasız ana hat:** gerekli kontrol yok; bu yüzden kırık ya da incelenmemiş kod herkesin bağımlı olduğu dala ulaşır.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Gelişigüzel ve reaktif. Dallanma doğaçlamadır, dallar haftalarca yaşar, commit mesajları "fix" ya da "wip" der, sır taraması yoktur ve entegrasyon bir birleştirme krizinden diğerine sendeler.
- **Düzey 2, Geliştirme:** Temel uygulamalar ortaya çıkar ama takıma göre değişir. Bir dallanma modeli ve mesaj kuralları bazı yerlerde vardır, ama dallar hâlâ çok uzun yaşar, uygulama kısmidir, sır taraması yamalıdır ve depo yapısı seçilmek yerine miras alınmıştır.
- **Düzey 3, Standartlaştırma:** Uygulamalar belgelenir ve kuruluş genelinde uygulanır: kısa dallarla gövde tabanlı geliştirme, korumalı ve her zaman yayımlanabilir bir ana hat, uygulanan commit kuralları, hem kancalarda hem CI'de sır taraması, en az ayrıcalıklı erişim ve bilinçli bir tek depo ya da çok depo seçimi.
- **Düzey 4, Yönetme:** Kaynak uygulamaları veriyle ölçülür ve kontrol edilir. Dal ömrünü, entegrasyon sıklığını, ana hat bozulma oranını, sızdırılmış bir sırrı algılama ve döndürme ortalama süresini ve değişiklikten iş kalemine izlenebilirliği üzerinde anlaşılan temel çizgilere karşı izlersiniz ve bir sonraki olayı beklemek yerine sayılar saptığında harekete geçersiniz.
- **Düzey 5, Orkestrasyon:** Uygulamalar sürekli iyileştirilir ve kuruluş genelinde bütünleşir. Dallanma, depo yapısı ve araçlar takımlar ve kod bağlaşımı değiştikçe uyum sağlar, otomasyon hijyeni uçtan uca uygular ve sürüm kontrolü verisi kuruluş genelinde teslimat, güvenlik ve risk kararlarını besler.

## Tartışma fikirleri

- Takımınızın dal ömrü gerçekten kısa mı ve değilse sürekli entegrasyonu ne engelliyor?
- Tek depo ya da çok depo seçiminiz kodunuzun gerçekte ne kadar bağlı olduğuyla uyuşuyor mu?
- Bugün büyük ikili dosyaları ve üretilmiş yapıtları nasıl ele alıyorsunuz ve size neye mal oluyor?
- Şu anda canlı bir kimlik bilgisi commit'lense ne olurdu ve onu ne kadar hızlı algılar ve döndürürdünüz?
- Sizin bağlamınızda ne kadar commit mesajı ve izlenebilirlik disiplini uygulamaya değer?
- Özellik bayrakları dallanma stratejinizi nasıl değiştirir ve hangi yeni riskleri getirir?

## Önemli çıkarımlar

- Kısa ömürlü dallarla sık entegre edin; uzun ayrışma, kaçınmak istediği acıya yol açar.
- Ana hattı yayımlanabilir tutun ve gerekli kontrollerle koruyun.
- Sırların geçmişe girmesine asla izin vermeyin; otomatik tarayın ve girerlerse hemen döndürün.
- Tek depo ya da çok depoyu gerçek bağlaşım ve eşgüdüm ihtiyaçlarınıza göre seçin.
- Commit geçmişini belge olarak ele alın; anlamlı, geleneksel, atomik commit'lerle.

## Kaynaklar ve ileri okuma

- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Jez Humble and David Farley, *Continuous Delivery*
- Scott Chacon and Ben Straub, *Pro Git*
- Paul Hammant and others, writings on trunk-based development
- Conventional Commits specification (as a reference standard)
- Martin Fowler, articles on branching patterns and continuous integration
