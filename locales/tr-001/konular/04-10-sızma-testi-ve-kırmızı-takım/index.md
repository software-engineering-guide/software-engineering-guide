# 4.10 Sızma testi ve kırmızı takım

## Genel bakış ve motivasyon

Tehdit modelinizin gerektirdiği her denetimi kurabilir ve yine de çalışıp çalışmadıklarını bilemeyebilirsiniz. Belgeler güvenlik duvarının o bağlantı noktasını engellediğini söyler, kod gözden geçirme girdinin doğrulandığını söyler, politika asgari ayrıcalığın uygulandığını söyler. Saldırgan güvenlik, kararlı bir saldırgan üzerine bastırdığında bunların hiçbirinin doğru olup olmadığını öğrenme yoludur. Bu bölüm, gerçek bir düşman bulmadan önce zayıflıkları bulmak için kendi sistemlerinize, yetkilendirme altında, kasıtlı olarak saldırmakla ilgilidir.

Disiplin bir yelpaze boyunca uzanır. Hafif uçta [güvenlik açığı taraması](https://en.wikipedia.org/wiki/Vulnerability_scanner) durur: bilinen kusurları ve yanlış yapılandırmaları yoklayan otomatik araçlar. Ortada [sızma testi](https://en.wikipedia.org/wiki/Penetration_test) durur: tanımlı bir hedefe karşı istismar edilebilirliği kanıtlamak için zayıflıkları zincirleyen yetenekli bir insan. En uçta [kırmızı takım](https://en.wikipedia.org/wiki/Red_team) çalışması durur: insanlar, süreçler ve teknoloji boyunca gerçek bir düşmanı taklit eden ve yalnızca önleme yeteneğinizi değil, algılama ve yanıt verme yeteneğinizi de sınayan hedef güdümlü bir kampanya. Her biri farklı bir soruyu yanıtlar ve bunları karıştırmak, kurumların para harcayıp yalancı güvenceyle kendilerini avutmasının en yaygın yoludur.

Bu bölüm komşularından bilerek ayrı durur. Bölüm 4.4 güvenlik operasyonlarını ele alır: tehditleri izleyen ve onlara yanıt veren savunma ve izleme tarafı. Bu bölüm, o savunmanın gerçekten işleyip işlemediğini sınayan saldırgan karşılıktır. Bölüm 4.9, güvenliğin kodun nasıl tasarlandığına ve yayımlandığına yerleştirildiği güvenli yazılım geliştirme yaşam döngüsünü ele alır; saldırgan test, o yaşam döngüsünün ürününü dışarıdan doğrular. Ayrıca bölüm 4.1'in temellerine ve kültürüne ve bölüm 4.2'nin uygulama güvenliği pratiklerine dayanır.

Büyük kurumlar için saldırgan test hem bir risk azaltma aracı hem de bir düzenleyici yükümlülüktür. Ödeme işleyicileri, bankalar ve sağlık hizmeti sağlayıcıları test etmek için açık gereksinimlerle karşı karşıyadır. Kamuda bahisler ulusal güvenliğe ve kamu güvenine uzanır: buradaki düşmanlar kaynakları bol ulus devletlerdir ve hedefledikleri sistemler seçimleri, yardımları ve kritik altyapıyı işletir. Her iki ortamda da değer, rapordan değil, neyi düzelttiğinizden ve bir sonraki saldırıyı algılamayı ne kadar hızlı öğrendiğinizden gelir.

## Temel ilkeler

- Çalışmayı soruyla eşleştirin: tarama, sızma testi ve kırmızı takım çalışması farklı şeyleri yanıtlar.
- Kimse bir sisteme dokunmadan önce yazılı yetkilendirme ve net angajman kuralları alın.
- Bulgular, düzeltilip yeniden sınanana kadar değersizdir; onları diğer işler gibi izleyin.
- Bir kırmızı takım, kazanmak için değil, mavi takımı daha iyi yapmak için vardır.
- Genel denetim listelerini değil, gerçek düşmanları ve tekniklerini taklit edin.
- Yalnızca bulunan açık sayısını değil, algılamayı ve yanıt vermeyi ölçün.
- Tiyatroya dikkat edin: geçmek için kapsamı belirlenmiş bir çalışma etkileyici görünür ve hiçbir şeyi kanıtlamaz.

## Öneriler

### Saldırgan güvenlik yelpazesini anlayın

Neyi satın aldığınızı adlandırarak başlayın. Güvenlik açığı taraması geniş, otomatik ve ucuzdur; bilinen [Common Vulnerabilities and Exposures](https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) (CVE) kayıtlarını ve yanlış yapılandırmaları yakalamak için yapınıza karşı sürekli çalıştırın. Hacim ve yanlış pozitif üretir ve bir kusurun bağlam içinde gerçekten istismar edilebilir olup olmadığını söyleyemez. Sızma testi, yetenekli bir test uzmanını sabit bir pencere boyunca tanımlı bir hedefe karşı koyar ve gerçek etkiyi göstermek için zayıflıkları zincirler: şu tarayıcı bulgusu, şu zayıf izinle birleşince alan yöneticisi verir. "Bu belirli şey kırılabilir mi ve ne kadar kötü" sorusunu yanıtlar.

Kırmızı takım çalışması daha büyük bir soruyu yanıtlar: "kararlı bir düşman bizi hedef alsa fark eder miydik ve onu durdurabilir miydik." Hedef odaklıdır (şu veri kümesini dışarı sızdır, şu kontrol sistemine ulaş), insanlar ve fiziksel erişim dahil tüm saldırı yüzeyini kapsar ve genellikle savunmacılar uyarılmadan yürütülür. [Mor takım çalışması](https://en.wikipedia.org/wiki/Red_team#Purple_team) duvarı yıkar: kırmızı ve mavi aynı odada birlikte çalışır, saldırgan bir teknik çalıştırır ve savunmacı araçlarının onu yakalayıp yakalamadığını izler, algılamaları gerçek zamanlı ayarlar. Mor takım çalışması, gizli bir kırmızı takımdan çoğu zaman dolar başına daha fazla savunma iyileşmesi sağlar, çünkü her eylem bir öğretme anına dönüşür.

### Kara, gri ya da beyaz kutuyu bilinçli seçin

Test uzmanına ne kadar şey söylediğiniz, ne öğreneceğinizi şekillendirir. Kara kutu testi onlara bir hedeften başka hiçbir şey vermez ve içeriden hiçbir bilgisi olmayan dış bir saldırganı simüle eder; gerçekçidir ama yavaştır ve test uzmanları gerçek bir düşmanın aylarını alacak keşfe tüm bütçeyi harcayabilir. Beyaz kutu testi kaynak kodu, mimari diyagramları ve kimlik bilgilerini teslim eder; test uzmanının derine inmesine ve eldeki sürede daha fazla alanı kapsamasına izin verir. Gri kutu ikisinin arasındadır: biraz bilgi, biraz kimlik bilgisi; ödevini yapmış bir saldırganı ya da kötü niyetli bir içerdekini taklit eder.

Uygulama testlerinin çoğunda gri ya da beyaz kutu daha iyi getiri verir, çünkü test uzmanının alt ağ düzeninizi yeniden keşfetmesi için değil, analizin derinliği için ödeme yaparsınız. Kara kutuyu, keşif aşamasının gerçekçiliğinin kendisinin sınamak istediğiniz şey olduğu durumlar için ayırın; örneğin bir yabancının herkese açık ayak izinizden ne kadar şey öğrenebildiğini ölçmek gibi. Hangisini görevlendirdiğiniz konusunda açık olun, çünkü az şey bulan bir kara kutu raporu ya güvende olduğunuz ya da test uzmanının çevrede zamanının bittiği anlamına gelebilir.

### Kapsamı dikkatle belirleyin ve angajman kurallarını yazın

Kapsam, çalışmaların başarıya ya da başarısızlığa uğradığı yerdir. Bir [angajman kuralları](https://en.wikipedia.org/wiki/Rules_of_engagement) belgesi, neyin sınırlar içinde olduğunu ve neyin olmadığını, hangi tekniklerin izinli olduğunu, test penceresini, kapsanan sistemleri ve ağları, veri işleme gereksinimlerini ve her iki taraftaki acil durum iletişim kişilerini tanımlar. Sınırların dışında olan ya da dikkat gerektiren üretim sistemlerini adlandırır, test uzmanı etkin biçimde tehlikeli bir şey bulursa durma kuralını belirler ve gerçek saldırgan etkinliğine ya da gerçekten hassas verilere rastlarlarsa ne olacağını tanımlar.

Yükseltme yollarını ve bir "hapisten çıkış" mektubunu yazın: çalışma ortasında güvenlik personeli ya da kolluk onlara itiraz ederse test uzmanının ibraz edebileceği yetkilendirme. Bulguların nasıl saklanıp iletileceğine önceden karar verin, çünkü bir sızma testi raporu sizi nasıl ihlal edeceklerinin haritasıdır ve buna göre korunmalıdır. Dar kapsam küçük bir yüzeyde derin bulgular üretir; geniş kapsam büyük bir yüzeyde sığ kapsam üretir. Bilerek seçin ve kapsamın çalışma ortasında yeniden yetkilendirme olmadan sessizce genişlemesine asla izin vermeyin.

### Yetkilendirmeyi test ile suç arasındaki çizgi sayın

Bir sızma test uzmanını bir suçludan ayıran tek eylem yetkilendirmedir. Erişim yetkiniz olmayan sistemlere erişmek, ABD'de [Computer Fraud and Abuse Act](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act) gibi yasalar ve başka yerlerdeki karşılıkları kapsamında bir suçtur ve iyi niyet bir savunma değildir. Yetkilendirme, onu verme yetkisine gerçekten sahip birinden yazılı gelmeli, kapsamdaki sistemleri ve teknikleri tam olarak kapsamalı ve iş başlamadan önce imzalanmış olmalıdır.

Üçüncü taraf sistemler bunu karmaşıklaştırır. Bulut sağlayıcınızın, hizmet olarak yazılım satıcılarınızın ve paylaşılan her altyapının kendi test politikaları olabilir ve sahibi olmadığınız varlıklara yönelik bir saldırıyı yetkilendiremezsiniz. Sağlayıcı kurallarını kontrol edin, gereken yerde izin isteyin ve testi kendi kiracılığınızın içinde tutun. Çalışanları hedefleyen sosyal mühendislik, rıza ve psikolojik zarar konusunda önceden düşünmeniz gereken etik ve yasal sorular doğurur. Şüphede, hukuk müşavirini dahil edin; bir konuşmanın maliyeti, yetkisiz erişim olayının maliyeti yanında önemsizdir.

### İç takımları üçüncü taraf test uzmanlarıyla tartın

İç bir kırmızı takım ortamınızı bilir, savunmacılarla ilişkiler kurar ve yıllık patlamalar yerine sürekli test edebilir. Bu aşinalık aynı zamanda bir sınırlamadır: sizin kör noktalarınızı ve kurumsal varsayımlarınızı paylaşırlar ve test ettikleri sistemlerle aynı liderliğe rapor verdiklerinde bağımsızlıkları sorgulanabilir. Üçüncü taraf firmalar taze gözler, uzmanlaşmış beceriler ve denetçilerin ve düzenleyicilerin çoğu zaman talep ettiği bağımsızlığı getirir; ama yavaş ısınır, çalışma başına daha pahalıya mal olur ve rapor teslim edildiğinde ayrılır.

Olgun programların çoğu ikisini de kullanır. İç takımlar sürekli düşman taklidini, algılama ayarını ve mor takım çalışmasını verimli kılan derin ortam bilgisini üstlenir. Dış firmalar dönemsel bağımsız doğrulama sağlar, PCI DSS gibi standartların bağımsızlık gereksinimlerini karşılar ve kendi insanlarınızın görmeyi bıraktığı alanları yoklar. Hangisini kullanırsanız kullanın, test uzmanlarının nitelikli olmasında ısrar edin: OSCP (Offensive Security Certified Professional) gibi sertifikalar ve kanıtlanmış deneyim, parlak bir satış sunumundan daha önemlidir.

### Hata ödül programları ve koordineli ifşa yürütün

Bir [hata ödül](https://en.wikipedia.org/wiki/Bug_bounty_program) programı, dış araştırmacıları takdir ve ödeme karşılığında açıkları bulmaya ve bildirmeye davet eder. Size asla bir anda işe alamayacağınız bir beceri yelpazesi boyunca sürekli, kalabalık kaynaklı test sağlar ve yalnızca gerçek bulgular için ödersiniz. Yapılandırılmış sızma testinin yerine geçmez, çünkü araştırmacılar ödeme getireni kovalar ve bütün kategorileri görmezden gelebilir; ama yaratıcı saldırıları ortaya çıkaran güçlü bir tamamlayıcıdır.

Ücretli bir ödül programı yürütmeden önce bir [koordineli açık ifşası](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure) politikasına ihtiyacınız var: herkesin bir güvenlik sorununu güvenle bildirmesi için yayımlanmış, bulması kolay bir yol, iyi niyetli araştırmacıları yasal olarak kovuşturmama taahhüdü, tanımlı yanıt süreleri ve gelenleri sınıflandırıp düzeltmek için bir iç süreç. Bir security.txt dosyası ve net bir bildirim adresi asgaridir. Kamu kurumları, herkese açık sistemler için açık ifşa politikalarını giderek daha çok zorunlu kılar ve hiçbir kanalınızın olmaması araştırmacıların hataları bulmasını durdurmaz; yalnızca size güvenle söylemelerini engeller.

### İhlal varsayımı ve düşman taklidini kullanın

Yalnızca çevre testi, saldırganın dışarıda başladığını varsayar; ama gerçek ihlaller çoğu zaman oltalanmış bir kimlik bilgisiyle ya da zaten içerideki ele geçirilmiş bir dizüstü bilgisayarla başlar. Bir [ihlal varsayımı](https://en.wikipedia.org/wiki/Breach_and_attack_simulation) çalışması, test uzmanını sıradan bir çalışan olarak erişim gibi bir dayanak noktasıyla başlatır ve oradan ne kadar ileri gidebileceğini sorar. Bu, eninde sonunda aşılacak bir çevreye her şeyi bahse yatırmak yerine, iç bölümlemenizi, algılamanızı ve patlama yarıçapı denetimlerinizi doğrudan sınar. Bir kırmızı takımın zamanını, sertleştirilmiş bir kenara karşı debelenmelerini izlemekten genellikle daha iyi kullanır.

Kampanyayı gerçek düşman davranışına, saldırganların gerçekte kullandığı taktiklerin ve tekniklerin ilk erişimden sızdırmaya kadar düzenlenmiş herkese açık bir bilgi tabanı olan [MITRE ATT&CK](https://en.wikipedia.org/wiki/MITRE_ATT%26CK) ile oturtun. Düşman taklidi, sektörünüzü hedeflediği bilinen bir tehdit aktörü seçer, belgelenmiş tekniklerini yeniden üretir ve her adımı algılayıp durdurup durdurmadığınızı sınar. Bu, genel bir saldırıdan çok daha yararlıdır, çünkü savunmalarınızı karşılaştığınız belirli düşmanlara karşı haritalar ve tehdit istihbaratınızın önceliklendirebileceği bulgular üretir.

### Bulguları mavi takıma ve algılama mühendisliğine besleyin

Saldırının amacı daha iyi savunmadır. Her kırmızı takım eylemi şunu sormak için bir fırsattır: araçlarımız bir sinyal üretti mi, biri gördü mü ve doğru yanıt verdi mi. Çalışmaları, her tekniğin sahip olduğunuz, kurmanız gereken ya da ayarlamanız gereken bir algılamaya eşleneceği biçimde yürütün. Bu algılama mühendisliğidir: saldırgan davranışını güvenilir uyarılara dönüştürmek ve kırmızı takım değerinin birikerek büyüdüğü yer burasıdır. "Yanal hareket sırasında algılanmadık" bulgusu yeni bir algılama kuralı olmalı ve tekniğin yeniden çalıştırılmasıyla sınanmalıdır.

Masa başı tatbikatlar bunu karar vermeye genişletir. Gerçek bir olaya yanıt verecek kişileri toplayın ve gerçekçi bir senaryoyu kâğıt üzerinde adım adım gözden geçirin: olayı kim ilan eder, hukukla kim konuşur, bir sistemi çevrimdışı almaya kim karar verir. Masa başı tatbikatlar ucuzdur, teknik testlerin kaçırdığı rol ve iletişim boşluklarını açığa çıkarır ve bölüm 9.3'ün olay yönetimi devreye girdiğinde en çok önem taşıyan insanları hazırlar. Hem araçlarınızın hem de insanlarınızın çalıştırılması için teknik kırmızı takım çalışmasını düzenli masa başı tatbikatlarla eşleştirin.

### Düzeltmeyi izleyin ve yeniden sınayın

Kimsenin harekete geçmediği bir açık raporu bir yükümlülüktür, çünkü artık bir denetçinin anabileceği bir kusuru bile bile çalıştırıyorsunuz. Her bulguyu bir sahip, bir önem derecesi ve riske bağlı bir bitiş tarihiyle olağan iş izleme sisteminize besleyin. Kritik bulgular acil işlem görür; daha düşük olanlar dürüst bir önceliklendirmeyle iş listesine katılır. Önemli metrik, rapor verme süresi değil, düzeltme süresidir.

Yeniden test döngüyü kapatır. Bir düzeltme yayımlandıktan sonra test uzmanı (ya da otomatik bir denetim) açığın gerçekten gittiğini ve düzeltmenin yeni bir delik açmadığını doğrular. Yeniden test olmadan "düzeltildi" bir olgu değil, bir umuttur ve birçok bulgu, düzeltme eksik kaldığı ya da bir gerileme onları yeniden getirdiği için tekrarlar. PCI DSS gibi standartlar bu döngüyü açıkça gerektirir. Yeniden testi, unutulmuş bir sonradan akla gelen olmasın diye, çalışma sözleşmesine yerleştirin.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | En uygun olduğu durum | Artılar | Eksiler |
|---|---|---|---|
| Güvenlik açığı taraması | Bilinen kusurların sürekli kapsamı | Ucuz, geniş, otomatik, sık | Gürültülü; istismar edilebilirliği kanıtlayamaz |
| Sızma testi | Tanımlı bir hedefte etkiyi kanıtlamak | Derin, insan kavrayışı; gerçek istismar zincirleri | Belli bir anın görüntüsü; dar kapsamlı; maliyetli |
| Kırmızı takım | Algılamayı ve yanıt vermeyi sınamak | Gerçekçi; insanları ve süreci çalıştırır | Pahalı; yavaş; olgun bir mavi takım gerektirir |
| Mor takım | Algılamaları hızla iyileştirmek | Dolar başına yüksek öğrenme; iş birlikçi | Daha az gerçekçi; her iki takımın da müsait olmasını gerektirir |
| Hata ödül programı | Süregelen kalabalık kaynaklı keşif | Bulgu başına ödeme; çeşitli beceriler | Düzensiz kapsam; sınıflandırma yükü; süreç gerektirir |

Temel gerilim, gerçekçilik ile öğrenme hızı arasındadır. Gizli bir kırmızı takım yürütebileceğiniz en gerçekçi testtir, ama dersleri yavaş gelir ve yalnızca tam bir kampanyadan sonra; olgunlaşmamış bir mavi takım sessizce yenilmekten az şey öğrenir. Mor takım çalışması, savunmacıların ne kadar hızlı iyileştiğini en üst düzeye çıkarmak için sürprizden vazgeçer. İkinci bir gerilim genişlik ile derinlik arasındadır: tarama her şeyi sığ kapsar, sızma testi ise bir dilimi derin kapsar. Olgun programlar bunlardan birini seçmek yerine katmanlar: dönemsel derin testlerin altında sürekli tarama ve ara sıra tam kapsamlı kırmızı takım kampanyaları. Yanlış hamle, yılda tek bir sızma testi satın alıp raporu dosyalamak ve sorunu çözülmüş saymaktır.

## Takımınızla tartışılacak sorular

1. **Saldırgan test görevlendirdiğimizde gerçekte hangi soruyu sorduğumuz konusunda net miyiz ve çalışma ona uyuyor mu?** Birçok kurum bir "sızma testi" satın alır ve insan yazımı bir özetle bir güvenlik açığı taraması alır; sonra yalnızca bilinen kusurları denetlemişken savunmalarını test ettiklerine inanırlar. Diğerleri, algılama yetenekleri o kadar olgunlaşmamışken bir kırmızı takım görevlendirir ki tatbikat yalnızca herkesin zaten bildiğini kanıtlar. Son üç çalışmanızın kapsamlarını ve sonuçtaki raporları getirin ve her birinin ihtiyaç duyduğunuz soruyu yanıtlayıp yanıtlamadığını sorun: bilinen açıkların kapsamı, belirli bir hedefin istismar edilebilirliği ya da bir saldırıyı algılama ve ona yanıt verme yeteneği. Cevap, olgunluğunuza uyan, tarama, sızma testi ve kırmızı ya da mor takım çalışmasından oluşan bilinçli bir karışımı şekillendirmelidir.

2. **Rapor ulaştıktan sonra bir bulguya ne oluyor ve düzeltildiğini nasıl kanıtlardık?** Saldırgan güvenliğin değeri tamamen düzeltmededir; yine de birçok program başarıyı riskin küçülmesiyle değil, raporun büyüklüğüyle ölçer. Son çalışmanızdaki gerçek bir bulguyu izleyin: kimin sahip olduğu, özellik işine karşı nasıl önceliklendirildiği, ne zaman düzeltildiği ve düzeltmenin gerçekten işe yaradığını birinin doğrulayıp doğrulamadığı. Bu izi sunamıyorsanız, testiniz göre davranmadığınız bilgi üretiyor demektir; bu bilmemekten daha kötüdür, çünkü artık bile bile açıktasınız. Bu tartışmanın çıktısı, sahipleri, riske dayalı son tarihleri ve her sözleşmeye yerleştirilmiş zorunlu yeniden testi olan izlenen bir düzeltme iş akışı olmalıdır.

3. **Kırmızı takımımız mavi takımımızı daha iyi mi yapıyor, yoksa yalnızca skor mu tutuyor?** Algılanmayan zaferleri kutlayan ve tekniklerini istifleyen bir kırmızı takım eğlendiricidir ve işe yaramazdır. İlişki, düşmanca yüzeyin altında iş birlikçi olmalıdır: algılanmayan her teknik yeni bir algılama kuralı olmalı, başarılı her yol bölümlemeyi bilgilendirmeli ve iki takım birlikte değerlendirme yapmalıdır. Savunmacılarınıza son kırmızı takım çalışmasından ne öğrendiklerini ve bunun sonucunda somut bir algılamanın ya da denetimin değişip değişmediğini sorun. Dürüst cevap hiçbir şeyse tiyatro için ödüyorsunuz demektir ve algılama mühendisliğine açıkça bağlı mor takım çalışmasına ve düşman taklidine yönelmelisiniz.

4. **Bir sonraki çalışmadan önce, sahibi olmadıklarımız dahil kapsamdaki her varlık için yazılı yetkilendirmemiz var mı?** Yetkilendirme, bir sızma testi ile bir bilgisayar suçu olayı arasındaki çizgidir ve büyük bir kurumda bir test uzmanının dokunacağı sistemler nadiren tek bir sahiplik sınırının içinde yer alır: bulut kiracılıklarına, hizmet olarak yazılım platformlarına, yönetilen ağlara ve bir ortağın ya da satıcının denetlediği paylaşılan altyapıya yayılırlar. Rakip baskı hızdır, çünkü imzalı izin ve sağlayıcı test politikalarının peşinden koşmak yavaştır ve bir son tarih yaklaştığında atlamak cazip gelir. Taslak angajman kurallarını, her sistemin karşısında bir sahibin adlandırıldığı varlık envanterini, ilgili bulut ve satıcı test politikalarını ve çalışma ortasında itiraz edilirse test uzmanının ibraz edebileceği imzalı yetkilendirme mektubunu getirin. Kurumsal ve kamu işlerinde maruziyet keskindir: paylaşılan bir platforma yetkisiz bir yoklama sözleşmeleri ihlal edebilir, düzenleyici raporlamayı tetikleyebilir ya da bir kamu kurumu için hükümetin dokunma hakkı olmayan sistemlere saldırdığına dair bir manşete dönüşebilir; bu yüzden kimse başlamadan önce hukuk müşaviri onay vermelidir.

5. **İç bir kırmızı takıma mı, dış firmalara mı, yoksa ikisine birden mi yatırım yapıyoruz ve bu bölüşüm gerçekte ihtiyacımız olana uyuyor mu?** Bu, gerçek para ve çok yıllık sonuçları olan bir yap ya da satın al kararıdır: iç takım maaşlara ve araçlara mal olur ve sürekli düşman taklidi ile derin ortam bilgisi sunar; dış firmalar çalışma başına daha pahalıdır ama taze gözler, uzmanlaşmış beceriler ve denetçilerin ve düzenleyicilerin talep ettiği bağımsızlığı getirir. Gerilim, her birinin diğerinin kör noktasını kapsamasıdır; bu yüzden onları tamamlayıcı değil de ikame saymak genellikle bir boşluk bırakır. Her birine şu anki harcamanızı, işi yapan kişilerin sertifikalarını ve kanıtlanmış geçmişini, çalışmaların sıklığını ve standartlarınızın getirdiği bağımsızlık gereksinimlerini getirin. Düzenlemeye tabi bir kurumda, PCI DSS ve benzeri rejimler iç takımınız ne kadar iyi olursa olsun dış bağımsız testi zorunlu kılabilir; kamuda, tedarik kuralları ve işletim yetkisinden önce eli kolu bağlı olmayan bir değerlendirme gösterme gereği, akredite bir üçüncü tarafı çoğu zaman isteğe bağlı değil zorunlu kılar.

6. **Dış araştırmacıların açıkları bildirmesi için güvenli bir kanalımız var mı ve gelenleri ele almaya hazır mıyız?** Büyük, kamuya açık bir kurum, davet etsin etmesin zaten araştırmacılar tarafından yoklanmaktadır ve tek soru, onların size güvenle söyleyip söyleyemeyeceği ya da bulduklarını yayımlamaya ya da satmaya zorlanıp zorlanmayacağıdır. Rakip düşünce hazırlıktır: koordineli ifşa politikası ya da ücretli hata ödül programı açmak gelen raporlar ve bir sınıflandırma yükü üretir ve hiç düzeltmediği bulgular için ödeme yapan bir program hiç olmamasından daha kötüdür. Varsa mevcut security.txt dosyanızı ve bildirim adresinizi, alım ve sınıflandırma sürecinizi, dürüstçe taahhüt edebileceğiniz yanıt sürelerini ve gelenleri düzeltmek için iş listesi kapasitenizi getirin. Kamu kurumları için herkese açık sistemlerde açık ifşa politikası giderek bir nezaket değil, bir yönergedir; kurumlar için iyi yürütülen bir ödül programı hem yaratıcı bulguların kaynağı hem de müşteri durum tespiti sırasında olgunluk kanıtıdır; bu yüzden karar, bir kanalınız olup olmayacağından çok, ona saygı gösterecek kadar kadrolu olup olmadığınızdır.

## Sektör merceği

**Girişim.** İç bir kırmızı takımı karşılayamazsınız; bu yüzden bunun yerine ucuz kapsam katmanlayın. Her derlemede bilinen bağımlılık kusurlarını yakalamak için güvenlik açığı taramasını dağıtım boru hattınıza bağlayın, araştırmacıların size ulaşabilmesi için bir security.txt dosyası ve basit bir koordineli ifşa politikası yayımlayın ve ilk kurumsal anlaşmanızdan önce saygın bir firmadan tek bir gri kutu sızma testi görevlendirin; her bulguyu onaylanmış bir düzeltmeye kadar izleyin. Hız, geniş bir programdan daha önemlidir: bir satışın önünü açan ya da en büyük riskinizi kapatan tek testi seçin ve büyüyene kadar gerisini atlayın.

**Küçük işletme.** Kadroda bir güvenlik uzmanı ve sıkı bir bütçe olmadan, kurmak yerine satın alın. Herhangi bir iç yetenek kurmak yerine yönetilen bir tarama hizmeti kullanın ve ılımlı bir sıklıkla dış bir sızma testi firması tutun; sözleşmenize bir yeniden test dahil olsun ki "düzeltildi" varsayılmak yerine kanıtlansın. En yüksek değerli, en düşük maliyetli hamleniz, herkesin bir kusuru bildirmesi için yayımlanmış bir yol ve hızla yama yapma disiplinidir; çünkü sizin boyutunuzdaki bir işletmenin gerçek dünyadaki ele geçirilmelerinin çoğu bilinen, yamalanmamış zayıflıklardan gelir.

**Kurumsal.** Ölçekte zorluk, birçok takım boyunca yönetişimdir. Dönemsel bağımsız dış sızma testlerinin altında sürekli tarama çalıştırın; bunlar PCI DSS gibi standartları karşılasın. Sürekli düşman taklidi ve mor takım çalışması için bir iç kırmızı takım bulundurun ve düzeltmeyi sahipleri, riske dayalı son tarihleri ve zorunlu yeniden testi olan izlenen bir portföy olarak yönetin. Algılanmayan her tekniği algılama mühendisliğine besleyin ve uyumun ve yönetim kurulunuzun beklediği denetim kanıtını, kapsamı, zaman çizelgelerini ve kapanış oranlarını üretin.

**Kamu.** Tedarik kuralları, şeffaflık ve kamuya hesap verebilirlik tüm programı şekillendirir. Yönergelerin giderek daha çok gerektirdiği gibi herkese açık sistemlerde bir açık ifşa politikası sürdürün, bir sistemin işletim yetkisini kapılayan sızma testi için akredite bağımsız değerlendiriciler kullanın ve düşman taklidini istihbarat ortaklarınızın işaret ettiği belirli ulus devlet aktörleri üzerine modelleyin. Yetkilendirmeyi, kapsamı ve veri işlemeyi ekstra titizlikle ele alın, çünkü sistemler seçimleri, yardımları ve kritik altyapıyı işletir; ve herhangi bir sistemi canlı tutmanın ön koşulu olarak yeniden testi zorunlu kılın.

## Örnekler

**Girişim.** Yirmi kişilik bir fintech girişimi iç bir kırmızı takımı karşılayamaz; bu yüzden elinden geleni katmanlar. Otomatik güvenlik açığı taraması boru hattı üzerinden her dağıtımda çalışır ve bilinen bağımlılık kusurlarını erken yakalar. Bir security.txt dosyası ve basit bir koordineli ifşa politikası yayımlar, ürün oturduktan sonra herkese açık bir platformda mütevazı bir hata ödül programı açar ve gerçek hatalar için gerçek araştırmacılara öder. İlk kurumsal müşterisini imzalamadan önce, saygın bir firmadan uygulamanın gri kutu sızma testini görevlendirir, her bulguyu olağan sorun izleyicisinde kapanışa kadar izler ve düzeltmeleri doğrulamak için bir yeniden test öder. Bu katmanlı yaklaşım, girişimin sürdürebileceği bir maliyetle inandırıcı bir güvenlik kapsamı verir ve sızma testi raporu müşteri durum tespiti sırasında paylaşabileceği kanıta dönüşür.

**Kurumsal.** Kart ödemelerini işleyen çok uluslu bir perakendeci, PCI DSS'i karşılamalıdır; bu standart, en az yılda bir ve önemli değişikliklerden sonra hem iç hem dış sızma testi ve kart sahibi ortamının yalıtıldığını kanıtlamak için bölümleme testi gerektirir. Binlerce varlık boyunca sürekli tarama çalıştırır, standardı karşılamak için bağımsız dış sızma testleri görevlendirir ve perakendeyi hedeflediği bilinen tehdit aktörlerine karşı MITRE ATT&CK'e dayanan ihlal varsayımı tatbikatları yürüten bir iç kırmızı takım bulundurur. Kırmızı takım, bölüm 4.4'ün güvenlik operasyonları işleviyle yakından çalışır: algılanmayan her teknik bir algılama mühendisliği kaydına dönüşür ve üç ayda bir yapılan mor takım oturumları uyarıları ayarlar. Düzeltme riske dayalı son tarihlerle izlenir ve tüm program, bölüm 4.6 uyumunun gerektirdiği denetim kanıtını üretir.

**Kamu.** Vatandaş yardım sistemlerini işleten ulusal bir kurum, ulus devlet düşmanlarıyla ve hassas kişisel verileri koruma yönündeki kamusal bir göreve karşı karşıyadır. Hükümet yönergelerinin giderek daha çok gerektirdiği gibi, tüm herkese açık sistemlerinde bir açık ifşa politikası sürdürür ve araştırmacılara kusurları bildirmeleri için güvenli bir kanal verir. Bağımsız üçüncü taraf değerlendiriciler, herhangi bir sistem canlıya çıkmadan önce yetkilendirme sürecinin parçası olarak sızma testleri yürütür ve sürekli izleme süregelen taramayı içerir. Kurum, istihbarat ortaklarının işaret ettiği belirli tehdit gruplarına göre modellenmiş düşman taklidi yürütür ve düzenli masa başı tatbikatlar, gerçek bir ihlalin gerektireceği olay yanıtını ve hukuki eşgüdümü prova eder. Bulgular zorunlu zaman çizelgeleri olan resmî bir düzeltme programına beslenir ve yeniden test, bir sistemin işletim yetkisini korumanın ön koşuludur.

## İş gerekçesi: motivasyonlar, YG ve TSM

Saldırgan güvenliğin getirisi, yaşamadığınız ihlaldir. Ciddi bir veri ihlali doğrudan yanıt, düzenleyici cezalar, hukuki sorumluluk, müşteri kaybı ve itibar zararı olarak milyonlara mal olur ve tek en pahalı etken, bir saldırının ne kadar süre algılanmadan kaldığıdır. Kırmızı ve mor takım çalışması, ele geçirilme ile algılama arasındaki boşluğu daraltarak bu sayıya doğrudan saldırır. Müşteri veritabanınıza istismar edilebilir bir yol bulan ve bir saldırgan bulmadan önce düzeltilen bir sızma testi, tek bir önlenmiş olayda tüm programın bedelini kat kat öder.

Sert itici güçler de var. PCI DSS, kart verisi işleyen herkes için sızma testini zorunlu kılar. Çerçeveler ve kamu yetkilendirme rejimleri, işletimden önce ve işletim sırasında bağımsız değerlendirme gerektirir. Kurumsal müşteriler, sözleşmelerin koşulu olarak yakın tarihli sızma testi raporları talep eder. Bu durumlarda test isteğe bağlı değildir ve soru yalnızca, zaten harcamanız gereken paradan gerçek güvenlik değeri çıkarıp çıkarmadığınızdır.

Toplam sahip olma maliyeti (TSM) çalışma ücretinden fazlasını içerir. Bir iç takım kurarsanız araçlar ve kadro için, bir hata ödül programının sınıflandırma yükü için ve her şeyden önce bulguların doğurduğu, gerçek harcamanın düştüğü düzeltme işi için bütçe ayırın. Testleri görevlendirip düzeltmeyi yetersiz fonlayan bir program iki dünyanın da en kötüsüdür: kötü haber için öder ve görmezden gelinen bulgu istismar edildiğinde yeniden öder. Gerekçeyi liderliğe sunmak için testi takip ettikleri metriklere bağlayın: ortalama algılama süresi, ortalama düzeltme süresi, kapatılan denetim bulguları ve en kritik varlıklarınızdaki risk azalması. Yatırım getirisi (YG) buradan okunur.

## Anti-kalıplar ve tuzaklar

- **Tara ve yeniden adlandır:** bir güvenlik açığı taramasını sızma testi diye satmak, insan doğrulaması ya da istismar zincirleme olmadan bir aracın çıktısını teslim etmek.
- **Raporla ve unut:** teslim edilebiliri hedef saymak, bulguları dosyalamak ve düzeltmeyi ya da yeniden testi asla izlememek.
- **Geçmek için kapsam:** çalışmayı, başarısız olması en olası sistemlerin elverişli biçimde sınırların dışında kalacağı biçimde daraltmak; hiçbir şey ifade etmeyen temiz bir rapor üretmek.
- **Skor tablosu olarak kırmızı takım:** savunmacıları daha iyi yapmak yerine teknikleri istifleyen ve zaferleri kutlayan düşmanca bir takım.
- **Olgunlaşmamış bir mavi takımı gizlice test etmek:** hiçbir algılama yeteneğiniz yokken gizli bir kırmızı takım yürütmek; tatbikat yalnızca zaten bildiğinizi kanıtlar.
- **Yetkilendirme yok ya da muğlak kapsam:** yazılı izin olmadan işe başlamak ya da kapsamın sahibi olmadığınız sistemlere kaymasına izin vermek; hukuki felaketi davet eder.
- **Çevre takıntısı:** yalnızca dış kenarı test edip saldırganların içeride başladığı ihlal varsayımı gerçeğini görmezden gelmek.
- **İfşa kanalını görmezden gelmek:** dış araştırmacıların hataları bildirmesi için güvenli bir yol olmaması; bu yüzden herkese açık yayımlarlar ya da satarlar.
- **Tiyatro metrikleri:** azalan riski, iyileşen algılamayı ve kısalan düzeltme süresini değil, bulunan açıkları saymak.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Test ara sıra ve tepkiseldir; çoğu zaman bir kutuyu işaretlemek için yapılan tek bir yıllık sızma testi ya da yalnızca bir olaydan sonra tetiklenen bir test. Raporlar az takiple dosyalanır, düzeltme izlenmez, ifşa kanalı yoktur ve gerçek bir saldırının algılanması sınanmamıştır ve büyük olasılıkla yoktur.
- **Düzey 2, Geliştirme:** Güvenlik açığı taraması ve sızma testi vardır ama takımlar arasında tutarsızdır; bazı gruplar sürekli tarar, bazıları hiç taramaz. Bulgular bir yerde kaydedilir, ancak sahipler ve son tarihler düzensizdir, yeniden test gelişigüzeldir ve bazı sistemler için koordineli bir ifşa kanalı olabilir ama tüm yapı için olmaz.
- **Düzey 3, Standartlaştırma:** Saldırgan test, bir olay değil, kurum genelinde uygulanan belgelenmiş bir programdır. Tarama, tanımlı bir sıklıkla ve büyük değişikliklerden sonra görevlendirilen zamanlanmış sızma testlerinin altında sürekli çalışır, angajman kuralları ve yetkilendirme standart uygulamadır, her bulgu bir sahip ve riske dayalı bir son tarihle kapanışa kadar izlenir, yeniden test zorunludur ve bir koordineli ifşa politikası tüm herkese açık sistemleri kapsar.
- **Düzey 4, Yönetme:** Program temel çizgilere göre ölçülür ve denetlenir. Ortalama algılama süresini ve ortalama düzeltme süresini, sinyal üreten kırmızı takım tekniklerinin yüzdesini, sektörünüzle ilgili MITRE ATT&CK teknikleri karşısında algılama kapsamını, bulgu tekrarlama oranlarını ve ifşa yanıt sürelerini izlersiniz ve her metriği bir hedefe karşı tutup sürüklendiğinde harekete geçersiniz. İhlal varsayımı tatbikatları ve düşman taklidi rutindir, bir kırmızı takım sürekli çalışır, bulgular algılama mühendisliğini besler ve gidiş ya da gitmeme kararları görüşe değil kanıta dayanır.
- **Düzey 5, Orkestrasyon:** Kırmızı ve mor takım çalışması kurum genelinde bütünleşiktir ve uyum sağlar. Her teknik sınanmış bir algılamaya eşlenir, düşman taklidi istihbarat değiştikçe sektörünüzü şu anda hedefleyen belirli tehdit aktörlerini izler ve program, öğrendikçe kapsamını, tekniklerini ve metriklerini sürekli rafine eder. Saldırgan test, güvenlik operasyonları, algılama mühendisliği ve olay yanıtı, ele geçirilme ile algılama arasındaki boşluğu zaman içinde ölçülebilir biçimde daraltan tek bir döngü olarak çalışır.

## Tartışma fikirleri

1. Gerçek bir saldırgan bugün sıradan bir çalışan olarak bir dayanak noktası edinse, kimse fark etmeden ne kadar ileri gidebilirdi ve bunu nasıl bilirsiniz?
2. Son çalışmalarınızdan hangileri gerçekten gerçekçiydi ve hangileri olası başarısızlıkların elverişli biçimde sınırların dışında kalacağı biçimde kapsamlandı?
3. Önceki testinizden kaç bulgu hâlâ açık ve bu, gerçek darboğazınızın test mi yoksa düzeltme mi olduğu hakkında ne söylüyor?
4. Dış araştırmacıların size bir açığı bildirmesi için güvenli, belirgin bir yol var mı ve bir rapor geldiğinde ne oluyor?
5. Olay müdahale ekibiniz bir ihlali en son ne zaman kâğıt üzerinde prova etti ve masa başı tatbikat, teknik testlerinizin kaçırdığı boşlukları açığa çıkardı mı?
6. Bulunan açıkları mı ölçüyorsunuz, yoksa iyileşen algılamayı ve azalan riski mi?

## Önemli çıkarımlar

- Saldırgan güvenlik bir yelpazedir: tarama bilinen kusurları bulur, sızma testi istismar edilebilirliği kanıtlar ve kırmızı takım çalışması algılamayı ve yanıt vermeyi sınar. Çalışmayı soruyla eşleştirin.
- Yazılı yetkilendirme ve net angajman kuralları, güvenlik testi ile suç arasındaki çizgidir; özellikle tamamen sahibi olmadığınız sistemlerde bunları asla atlamayın.
- Değer raporda değil, düzeltmede ve yeniden testtedir. Her bulguyu bir sahip, riske dayalı bir son tarih ve onaylanmış bir düzeltmeyle izleyin.
- Bir kırmızı takım, mavi takımı daha iyi yapmak için vardır. Bulguları algılama mühendisliğine besleyin, mor takım çalışmasını ve ihlal varsayımı tatbikatlarını tercih edin ve kampanyaları MITRE ATT&CK üzerinden gerçek düşman tekniklerine oturtun.
- Yalnızca açık sayılarını değil, algılamayı ve yanıt vermeyi ölçün ve geçmek için kapsamı belirlenmiş, güvenlik olmadan rahatlık üreten çalışmalardan sakının.

## Kaynaklar ve ileri okuma

- Georgia Weidman, *Penetration Testing: A Hands-On Introduction to Hacking*
- Peter Kim, *The Hacker Playbook 3: Practical Guide to Penetration Testing*
- Jim O'Gorman, Devon Kearns, and Mati Aharoni, *Metasploit: The Penetration Tester's Guide*
- Joe Vest and James Tubberville, *Red Team Development and Operations: A Practical Guide*
- MITRE, *MITRE ATT&CK* framework and knowledge base
- Payment Card Industry Security Standards Council, *PCI DSS Requirements and Testing Procedures* and *Penetration Testing Guidance*
- National Institute of Standards and Technology, *NIST SP 800-115: Technical Guide to Information Security Testing and Assessment*
- Dafydd Stuttard and Marcus Pinto, *The Web Application Hacker's Handbook*
