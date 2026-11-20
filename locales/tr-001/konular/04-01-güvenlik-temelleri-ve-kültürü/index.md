# 4.1 Güvenlik temelleri ve kültürü

## Genel bakış ve motivasyon

Güvenlik, sonradan eklediğiniz bir özellik değildir ve mühendislikten ayrı oturan uzmanlaşmış tek bir takımın işi de değildir. Büyük bir kurumda güvenlik, sistemin bütününün nasıl tasarlandığının, inşa edildiğinin, işletildiğinin ve yönetildiğinin bir niteliğidir. Yüzlerce hizmette binlerce mühendis kod sevk ettiğinde, bir olayın ne kadar zarar vereceğini en zayıf halka belirler. Yanlış yapılandırılmış tek bir depolama kovası, yamalanmamış bir bağımlılık ya da fazla yetkili bir hizmet hesabı milyonlarca kaydı açığa çıkarabilir. Bunun ölçekte yaşanmasını önleyen şey temeller ve kültürdür.

Kurumlar için bahisler mali ve itibarla ilgilidir: ihlal maliyetleri, düzenleyici cezalar, kaybedilen müşteriler ve düşen değerlemeler. Kamu için bahisler ulusal güvenliğe, kamu güvenine ve temel hizmetlerin sürekliliğine kadar uzanır. Her iki ortam da sert bir gerçeği paylaşır: güvenliği yalnızca kontroller ve kapılarla zorlayamazsınız. İşi yapan insanlar onu içselleştirmelidir. Mühendislerin tehditleri anladığı, sahiplik hissettiği ve endişe dile getirdiğinde ödüllendirildiği bir kültür, kaleci rolü oynayan aşırı yüklenmiş bir güvenlik takımına yaslanan kültürden çok daha iyi sonuç verir.

Bu bölüm, bu kılavuzdaki diğer her güvenlik bölümünün altında yatan zihinsel modelleri ve kültürel uygulamaları ortaya koyar. Güvenliği herkesin işi yapmayı, [tehdit modellemeyi](https://en.wikipedia.org/wiki/Threat_model), güvenli geliştirme yaşam döngüsünü, [derinlemesine savunma](https://en.wikipedia.org/wiki/Defense_in_depth_(computing)) ve [sıfır güven](https://en.wikipedia.org/wiki/Zero_trust_security_model) gibi temel mimari ilkeleri ve güvenlik işini korku ya da moda yerine gerçek riske göre nasıl önceliklendireceğinizi kapsar.

*Ayrıca bakın:* bölüm 4.2 (uygulama güvenliği), bölüm 4.3 (altyapı ve bulut güvenliği), bölüm 4.4 (güvenlik operasyonları) ve bölüm 4.6 (uyum ve yönetişim) bu temellerin üzerine kurulur.

## Temel ilkeler

- **Güvenlik herkesin işidir.** Her mühendis, ürün yöneticisi ve operatör, inşa ettiği şeyin güvenliğine sahip çıkar. Güvenlik takımı destekler, danışmanlık verir ve denetler; işi tek başına yapmaz ve yapamaz.
- **İhlal olduğunu varsayın.** Saldırganlar zaten içerideymiş gibi tasarlayın. Ele geçirilmiş bir bileşenin erişebileceği şeyleri en aza indirin.
- **Derinlemesine savunma.** Hiçbir tek kontrol yeterli değildir. Birinin başarısızlığı hepsinin başarısızlığı anlamına gelmesin diye bağımsız kontrolleri katmanlayın.
- **[En az ayrıcalık](https://en.wikipedia.org/wiki/Principle_of_least_privilege).** Gereken en düşük erişimi, gereken en kısa süre için verin ve artık gerekmediğinde otomatik olarak geri alın.
- **Sola kaydırın.** Sorunları, düzeltmesi en ucuz olduğu için olabildiğince erken bulun ve giderin.
- **Risk temelli önceliklendirme.** Çabayı, olasılık ile etkinin birleşiminin en yüksek olduğu yere harcayın; bunu bu hafta haberlere çıkan şeye göre değil, CIA üçlüsüne (gizlilik, bütünlük ve erişilebilirlik) göre yapın.
- **Suçlamasız öğrenme.** Güvenlik olaylarını ve ramak kalaları ceza için değil, öğrenme fırsatı olarak ele alın.

## Öneriler

### Bir güvenlik şampiyonları programı kurun

Her mühendislik takımına belirlenmiş bir güvenlik şampiyonu yerleştirin. Şampiyonlar tam zamanlı güvenlik uzmanı değildir. Ek eğitim almış ve merkezi güvenlik takımına doğrudan hattı olan mühendislerdir. Tasarımları gözden geçirirler, bulguları önceliklendirirler, takım arkadaşlarının sorularını yanıtlarlar ve güvenlik bağlamını planlamaya taşırlar. Bu, her takım için bir uzman işe almadan güvenlik uzmanlığını kurumun geneline yayar ve güven de inşa eder, çünkü tavsiye kod tabanını gerçekten bilen bir meslektaştan gelir.

Şampiyonlara gerçek destek verin: öğrendiklerini paylaşacakları düzenli bir forum, eğitim ve konferanslar için bütçe, performans değerlendirmelerinde takdir ve teslimat taahhütlerinden ayrılmış zaman. Yalnızca kâğıt üzerinde var olan bir şampiyonlar programı hiçbir şey üretmez.

### Tehdit modellemeyi rutin hale getirin

Tehdit modelleme, inşa etmeden önce "ne ters gidebilir?" diye sorma disiplinli alışkanlığıdır. Yeni hizmetler, büyük özellikler ve güven sınırlarındaki her değişiklik için yapın. Gerçekten sık yapılabilecek kadar hafif tutun.

- **[STRIDE](https://en.wikipedia.org/wiki/STRIDE_model)**, güvenlik özelliklerine eşlenmiş pratik bir kontrol listesidir: Spoofing (kimlik sahteciliği, kimlik doğrulama), Tampering (kurcalama, bütünlük), Repudiation (inkâr, inkâr edilemezlik), Information disclosure (bilgi sızması, gizlilik), Denial of service (hizmet reddi, erişilebilirlik) ve Elevation of privilege (ayrıcalık yükseltme, yetkilendirme). Her veri akışını gezin ve her kategorinin nasıl uygulandığını sorun.
- **PASTA** (Process for Attack Simulation and Threat Analysis), teknik tehditleri iş etkisine bağlayan, daha ağır, risk merkezli, yedi aşamalı bir yöntemdir; yüksek değerli sistemler için kullanın.
- **[Saldırı ağaçları](https://en.wikipedia.org/wiki/Attack_tree)**, bir hedefi ("müşteri verisini çalmak") saldırganın atacağı dallanan adımlara ayırır; yolları bulmanıza ve budamanıza yardımcı olur.

Tehdit modellerini kodun yanında yaşayan belgeler olarak tutun ve mimari her değiştiğinde yeniden ele alın.

### Güvenli bir yazılım geliştirme yaşam döngüsü kurun

Güvenliği son bir kapı olarak görmek yerine her aşamaya örün:

- **Gereksinimler:** güvenlik ve gizlilik gereksinimlerini işlevsel olanlarla birlikte yakalayın.
- **Tasarım:** tehdit modelleyin ve güven sınırlarını gözden geçirin.
- **Gerçekleştirme:** güvenli kodlama standartlarını, kod incelemesini ve commit öncesi sır taramasını zorunlu kılın.
- **Test:** hatta [SAST](https://en.wikipedia.org/wiki/Static_application_security_testing) (statik uygulama güvenliği testi), [DAST](https://en.wikipedia.org/wiki/Dynamic_application_security_testing) (dinamik uygulama güvenliği testi) ve bağımlılık taramasını çalıştırın (bkz. bölüm 4.4).
- **Yayın:** kaynağı doğrulayın, yapıtları imzalayın ve yapılandırmayı denetleyin.
- **İşletim:** izleyin, yamalayın ve yanıt verin.

Sola kaydırmanın amacı, bütün işi öne yığıp mühendisleri bunaltmak değildir. Amaç, erken düzeltilmesi çok daha ucuz olan kusur türlerini yakalamaktır.

### Sıfır güven mimarisi ilkelerini benimseyin

Geleneksel çevre güvenliği, ağın içindeki her şeyin güvenilir olduğunu varsayar. Bu varsayım, saldırgan bir dayanak noktası elde ettiği anda çöker. Sıfır güven, örtük ağ güveninin yerine açık ve sürekli doğrulamayı koyar: ağda nereden gelirse gelsin her isteği kimliğe, cihaz duruşuna ve bağlama göre doğrulayın ve yetkilendirin. Güçlü kimliği, en az ayrıcalıklı yetkilendirmeyi, mikro bölümlemeyi ve her yerde [şifrelemeyi](https://en.wikipedia.org/wiki/Encryption) birleştirin. Sıfır güven bir üründen çok bir yolculuktur; bu yüzden ona adım adım yaklaşın.

### CIA üçlüsünü kullanarak riske göre önceliklendirin

Her varlığı ve kontrolü **Gizlilik**, **Bütünlük** ve **Erişilebilirlik** çevresinde çerçeveleyin. Bütün veri aynı korumaya ihtiyaç duymaz: herkese açık bir pazarlama sayfası ile sağlık kayıtları veritabanının gizlilik ihtiyaçları çok farklıdır. Varlıklarınızı sınıflandırın, ele geçirilme olasılığını ve etkisini tahmin edin ve kıt güvenlik çabasını en yüksek riskli birleşimlere yöneltin. Başkalarının sonradan gözden geçirip savunabilmesi için risk kararlarınızı yazın.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
|---|---|---|
| Merkezi güvenlik takımı tüm güvenliğe sahip olur | Derin uzmanlık, tutarlı standartlar | Darboğaz, mühendisler ilgisini kaybeder, ölçeklenmez |
| Dağıtık güvenlik (şampiyonlar) | Ölçeklenir, sahiplik kurar, daha hızlı geri bildirim | Yatırım gerektirir, beceri düzeyi eşitsizdir, eşgüdüm ister |
| Her şey için ağır, peşin tehdit modelleme | Kapsamlı, tasarım kusurlarını yakalar | Teslimatı yavaşlatır, kutu işaretlemeye dönüşebilir |
| Hafif, riske hedeflenmiş tehdit modelleme | Hızlı, önemli olana odaklı | "Düşük riskli" sistemlerdeki tehditleri kaçırabilir |
| Yayınları engelleyen katı kapılar | Uyumu zorunlu kılar | Sürtünme, geçici çözümleri teşvik eder |

Merkezî gerilim, hız ile güvence arasındadır. Kapılara ve merkezi denetime fazla yaslanırsanız mühendislerin dolanıp geçtiği bir sürtünme yaratır, gölge BT'yi ve küskünlüğü beslersiniz. Destek vermeden özerkliğe fazla yaslanırsanız tutarsız, denetlenmemiş bir güvenlik elde edersiniz. Sürdürülebilir cevap, destekleyici korkuluklarla güçlü bir kültürdür: yapabildiğiniz yerde otomatik, yargı gerektiren yerde insan eliyle ve her zaman yalnızca dayatılmak yerine açıklanarak.

## Takımınızla tartışılacak sorular

1. **Sistemlerinizden hangileri ağır tehdit modellemeyi hak ediyor ve katmanı kim belirliyor?** Büyük bir envanterde her hizmete yedi aşamalı bir PASTA analizi uygulayamazsınız; bu yüzden 30 dakikalık bir STRIDE geçişinin ne zaman yeterli olduğuna, yüksek değerli bir sistemin ne zaman derin, iş etkisi güdümlü modellemeyi hak ettiğine dair açık bir kurala ihtiyacınız var. Kararı CIA sınıflandırmanıza dayandırın: düzenlemeye tabi kayıtları, ödeme akışlarını ya da kimlik doğrulama mantığını tutan sistemler en üsttedir, herkese açık bir pazarlama sayfası değildir. Kurumsal ve kamu işlerinde bir denetçi, belirli bir sistemin neden öyle modellendiğini savunmanızı isteyecektir; bu yüzden katmanlama ölçütlerini yazın ve onları uygulayan sahibi adlandırın. Toplantıya mevcut varlık sınıflandırmanızı ve tehdit modeli olmayan hizmetlerin bir listesini getirin, çünkü ikisi arasındaki boşluk gerçek riskinizdir. Çıtada anlaşamazsanız her şeyi hafifçe ya da hiçbir şeyi derinlemesine modellemeye varsayılan olarak düşersiniz; ikisi de sizi yarı yolda bırakır.

2. **Bir güvenlik şampiyonu ile bir teslimat son tarihi çarpıştığında, yayını gerçekte kim durdurabilir?** Bir şampiyonlar programı, şampiyon yalnızca ek eğitim ve iyi niyetle değil gerçek yetkiyle donatıldıysa sonuçları değiştirir. Bir şampiyonun sevkiyatı engelleyip engelleyemeyeceğine, merkezi AppSec takımına yükseltip yükseltmeyeceğine ve hangi önem düzeyindeki bir bulgunun teslimatı durdurmayı, hangisinin yalnızca takip edilmeyi haklı kıldığına önceden karar verin. Bu en çok baskı altında önemlidir; örneğin bir ürün yöneticisi lansmandan bir hafta önce bir tasarım kusurundan feragat etmek istediğinde, ki ele alınmamış kusurların düzeltmesi tam da o zaman en pahalıdır. Bir güvenlik kaygısının bir son tarihle karşılaştığı yakın tarihli bir örneği getirin ve kimin nasıl karar verdiğini izleyin, çünkü o hikâye gerçek yükseltme yolunuzu ortaya koyar. Dürüst cevap teslimatın her zaman kazandığıysa şampiyonlarınız süstür; daha fazlasını eklemeden önce teşviki düzeltmelisiniz.

3. **"İhlal olduğunu varsayın" bir sonraki tasarım incelemenizde somut olarak neyi değiştiriyor?** İlkeye başıyla onaylamak kolay, işlevsel hale getirmek zordur; bu yüzden onu somut taahhütlere bağlayın: hangi güven sınırlarını sıkılaştıracağınızı, nerede mikro bölümleme ekleyeceğinizi ve ele geçirilmiş tek bir hizmet hesabının erişebileceği şeyleri nasıl küçülteceğinizi. Büyük bir takım için getirisi patlama yarıçapının küçülmesidir; böylece tek bir hizmete giren saldırgan arkasındaki veri deposuna sıçrayamaz. Kurumsal ve kamu ortamlarında bu, en az ayrıcalık ve kısa ömürlü kimlik bilgisi kararlarınızı da şekillendirir; bunları baştan tasarlamak ucuz, sonradan eklemek acı vericidir. Gerçek bir hizmet diyagramı getirin ve saldırgan web katmanını ele geçirdikten sonra ne yaptığını sorun, ardından bu çeyrekte iki sınırlandırma değişikliğine söz verin. İhlallerin olduğuna dair belirsiz bir mutabakat, bir izni, bir ağ kuralını ya da bir kimlik bilgisi ömrünü değiştirmedikçe değersizdir.

4. **Güvenlik kültürünüzün gerçekten iyileştiğini nasıl anlayacaksınız ve yönetim kuruluna hangi metriği savunurdunuz?** Eğitim tamamlama oranları ve bilet sayıları toplaması kolay ve neredeyse işe yaramazdır, çünkü risk azaltımını değil etkinliği ölçerler ve büyük bir kurum bunların içinde boğulur. Gerçekten bütçeyle destekleyeceğiniz sonuç metrikleri seçin: yüksek önem düzeyli bulguları gidermenin medyan süresi, güncel bir tehdit modeli taşıyan hizmetlerin payı, üretimden önce yakalanan olayların oranı ve güven arttıkça düşmesi değil yükselmesi gereken, kendiliğinden bildirilen ramak kala oranı. Rakip bir husus da her iyi metriğin oyuna getirilebilmesidir; bu yüzden her birini bir karşı metrikle eşleştirin ve anlık görüntü yerine eğilimi inceleyin. Mevcut panonuzu getirin ve güvenlik gerçekten kötüleşse hangi sayıların değişeceğini sorun; değişmeyecek olanlar süstür. Kurumsal ve kamu ortamlarında bir düzenleyici ya da denetim komitesi kontrollerin işe yaradığına dair kanıt isteyecektir; bu yüzden yalnızca yeşil görünen değil, inceleme altında savunabileceğiniz metrikleri seçin.

5. **Bir mühendis bir sonraki sefer bir hata bildirdiğinde gerçekte ne olacak; süreciniz uygulamada mı suçlamasız, yoksa yalnızca slaytta mı?** Suçlamasız öğrenme en sık dile getirilen ve en az yaşanan ilkedir, çünkü ilk ciddi olay liderliğin buna gerçekten inanıp inanmadığını sınar. Bir sorunu düzeltmenin hesap verebilirliğini, ona yol açmanın cezasından nasıl ayıracağınıza ve olay sonrası incelemeyi, adı geçen kişilerle değil bozuk sistemlerle ilgili kalacak biçimde kimin yürüteceğine önceden karar verin. Gerilim gerçektir: paydaşlar birinin sorumlu tutulmasını ister, ama bildireni cezalandırmak bir sonraki hatanın bir ihlale dönüşene kadar gizli kalmasını garanti eder. Son iki olay incelemenizi getirin ve bir kişiyi mi yoksa bir kontrolü mü suçladıklarına, alarmı veren mühendise teşekkür edilip edilmediğine ya da sessizce kenara çekilip çekilmediğine bakın. Kamu ve düzenlemeye tabi kurumlarda zorunlu ihlal bildirimi kuralları bahsi daha da yükseltir, çünkü hataları gizleyen bir kültür, yasal yaptırım taşıyan bildirim son tarihlerini de kaçıracaktır.

6. **Sola kaydırma araçlarınızın sürtünmesine kim sahip; onları satın mı alıyorsunuz, kendiniz mi kuruyorsunuz, yoksa içlerinde mi boğuluyorsunuz?** Otomatik statik ve dinamik analiz, bağımlılık taraması ve sır taraması güvenli bir geliştirme yaşam döngüsünün belkemiğidir; ama mühendisleri yanlış pozitiflerle boğan bir hat onlara güvenlik çıktısını görmezden gelmeyi öğretir ve bu, hiç tarama yapmamaktan daha kötüdür. Araçları kimin ayarlayacağına, bulguları kimin önceliklendireceğine ve entegre bir platform mu satın alacağınıza yoksa sonra kendiniz bakmak zorunda kalacağınız açık kaynak tarayıcıları mı bir araya getireceğinize karar verin. Rakip hususlar kapsam ile gürültü ve denetim ile maliyettir: sürekli yalan yere alarm veren ucuz bir tarayıcı, bir şampiyonlar programının yıllarca kurduğu güveni yakar. Mevcut yanlış pozitif oranınızı, mühendislerin engelleyici bir kontrolü beklediği ortalama süreyi ve bir kapıyı sessizce devre dışı bırakan takımların listesini getirin. Büyük kurumlarda ve kamuda tedarik ve araç dağınıklığı boyutunu da ekleyin; çünkü on takımın her birinin kendi tarayıcısını alması, hiçbir denetçinin uzlaştıramayacağı tutarsız bir kapsam üretir.

## Sektör merceği

**Girişim.** Güvenlik takımınız yok ve pistiniz kısa; bu yüzden kültür karşılayabileceğiniz tek kontroldür. Kimlik doğrulamaya ya da ödemelere dokunan her özellikten önce 30 dakikalık bir tehdit modelleme beyaz tahtasını alışkanlık yapın, en az ayrıcalığı ve MFA'yı her yerde açın çünkü hiçbir maliyeti yoktur ve herkesin bir kaygıyı işaretleyebileceği suçlamasız bir kanal tutun. Ağır süreç ve araçlardan kaçının; kurucu mühendisler onu sürdüremez ve şimdi kurduğunuz disiplin, kurumsal alıcıların size sonradan güvenmesini sağlayan şeydir.

**Küçük işletme.** Özel bir güvenlik uzmanınız ve dar bir bütçeniz var; bu yüzden kendi hattınızı kurmak yerine zaten satın aldığınız araçlardaki güvenli varsayılanlara yaslanın. MFA'yı, yamalamayı ve en az ayrıcalığı sizin yerinize uygulayan yönetilen platformları tercih edin ve güvenliği bir veri hijyeni sorusu olarak ele alın: hangi hassas verileri tuttuğunuzu ve ona kimin erişebildiğini bilin. Kur ya da satın al arasında seçmeniz gerekirse satın alın, çünkü güncel tuttuğunuz yönetilen bir kontrol, çürümeye bıraktığınız özel yapım bir kontrolden iyidir.

**Kurumsal.** Yüzlerce hizmet ve binlerce mühendis ölçeğinde zorluk, birçok takım arasında tutarlılık ve yönetişimdir. Bir güvenlik şampiyonları programı yürütün, tehdit modelleme katmanlarını CIA sınıflandırmasına bağlı olarak standartlaştırın ve her takımın iyi varsayılanları miras alması için asfalt yol şablonları ve otomatik hat kontrolleri sağlayın. Düzeltme ve kapsam metriklerini taban çizgilerine göre izleyin ve her sistemin neden öyle modellendiğini ve öyle kontrol edildiğini gösteren bir denetim izi tutun.

**Kamu.** Tedarik kuralları, şeffaflık yükümlülükleri ve kamusal hesap verebilirlik her seçimi şekillendirir. Sıfır güven ilkeleri ve kısa ömürlü kimlik bilgileri çoğu zaman yürütme politikasıyla zorunlu kılınır ve sertleştirme bütçesinin nereye gittiğine dair belgelenmiş, riske dayalı bir gerekçeyi bir denetçiye gösterebilmelisiniz. Önce en hassas vatandaş kayıtlarını tutan sistemlere öncelik verin, kamunun bilme hakkı olduğu yerde güvenceleri yayımlayın ve satıcılardan, opak kara kutuları kabul etmek yerine sınırlamalarını açıklamalarını isteyin.

## Örnekler

**Girişim.** On kişilik bir girişimin güvenlik takımı da bunun için bütçesi de yok; bu yüzden iki kurucu mühendis, kimlik doğrulamaya ya da ödemelere dokunan her özellikten önce tehdit modellemeyi 30 dakikalık bir beyaz tahta alışkanlığı yapar: neyin ters gidebileceğini ve bunu kimin isteyeceğini sorarlar. Hiçbir maliyeti olmayan birkaç temel alışkanlık benimserler: her bulut rolünde en az ayrıcalık, her hesapta MFA ve herkesin suçlanma korkusu olmadan bir kaygıyı dile getirebileceği suçlamasız bir kanal. Daha sonra bir tur yatırım aldıklarında ve kurumsal alıcılar güvenliği nasıl yönettiklerini sorduğunda, o erken kültür bir tane uydurmak için telaşlanmak yerine dürüstçe cevap vermelerini sağlar.

**Kurumsal.** 6.000 mühendisli küresel bir banka, her ekip için eğitimli bir şampiyonla bir güvenlik şampiyonları programı yürütür. Şampiyonlar aylık bir loncaya katılır, üç ayda bir eğitimi tamamlar ve her yeni hizmet için STRIDE kullanarak tehdit modellemeye öncülük eder. Merkezi AppSec takımı asfalt yol şablonlarını ve otomatik hat kontrollerini sürdürür. İki yıl içinde, yüksek önem düzeyli bulguları gidermenin medyan süresi 45 günden 9 güne düştü ve tasarım aşamasındaki tehdit modelleme, bir ödeme API'sindeki bir yetkilendirme kusurunu üretime ulaşmadan yakalayarak büyük olasılıkla bildirilmesi gereken bir olayı önledi.

**Kamu.** Eski sistemlerini modernleştiren ulusal bir vergi idaresi, yürütme politikasıyla zorunlu kılınan sıfır güven ilkelerini benimser. Her dahili hizmet çağrısı kısa ömürlü kimlik bilgileriyle doğrulanır ve istek başına yetkilendirilir; ağ bölümleri artık güven sağlamaz. İdare, vatandaşa dönük her hizmeti "mükellef kayıtlarını sızdırmak" ve "bir beyannameyi değiştirmek" köklü saldırı ağaçlarına karşı tehdit modeller. CIA etki düzeyleriyle uyumlu, riske dayalı önceliklendirme, sertleştirme bütçesini önce en hassas kayıtları tutan sistemlere odaklar.

## İş gerekçesi: motivasyonlar, YG ve TSM

Bir güvenlik kültürü inşa etmenin maliyeti gerçektir: şampiyon zamanı, eğitim, araçlar ve tehdit modelleme ile incelemeleri yapmanın mütevazı yükü. Ama bu maliyet, yapmamanın maliyetinin yanında küçüktür. Ortalama büyük bir veri ihlali, soruşturma, bildirim, giderme, düzenleyici cezalar, hukuki risk ve kaybedilen işler hesaba katıldığında milyonları bulur. Kamu ihlalleri, hiçbir faturanın tam olarak yakalayamadığı görev kesintisi ve kamu güveninin aşınmasını da ekler.

Güvenlik yatırımının getirisi üç yerden gelir: **önlenen olaylar** (hiç yaşanmayan ihlal), **azalan düzeltme maliyeti** (tasarım zamanında düzeltilen kusurlar, üretimde düzeltilenlerin çok küçük bir kısmına mal olur) ve **daha hızlı teslimat** (asfalt yollar ve otomatik kontroller, takımların elle incelemeyi beklemek yerine güvenle sevk etmesini sağlar). Liderliğe gerekçeyi sunarken güvenliği soyut bir iyilik olarak değil, fiyat etiketli bir risk yönetimi olarak çerçeveleyin. En önemli risklerin beklenen kaybını (olasılık çarpı etki), onları azaltmanın maliyetini ve geriye kalan riski gösterin. Yöneticiler ölçebildikleri risk azaltımını finanse eder.

## Anti-kalıplar ve tuzaklar

- **Güvenlik tiyatrosu.** Etkileyici görünen ama gerçek bir riski azaltmayan, bir şeyi korumak için değil bir denetimi tatmin etmek için benimsenen kontroller.
- **Sonda bir kapı olarak güvenlik takımı.** Tasarım kusurlarını lansmandan bir hafta önce, düzeltmesi en pahalı ve feragat edilmesi en olası olduğu zaman keşfetmek.
- **Suçlama kültürü.** Bir hatayı bildiren mühendisi cezalandırmak, bir sonraki hatanın gizli kalmasını garanti eder.
- **Onay kutusu tehdit modelleme.** Kimsenin okumadığı bir şablonu doldurmak ve gerçek mimariden kopuk belgeler üretmek.
- **Herkese uyan tek beden kontroller.** Herkese açık bir web sitesine ve bir ödeme sistemine aynı ağır süreci uygulamak, çabayı boşa harcar ve küskünlük doğurur.
- **Korku güdümlü önceliklendirme.** Varlıklarınızı gerçekten tehdit eden şey yerine, haberlerde gündemde olan açığın peşinden koşmak.
- **Yalnızca adı olan şampiyonlar.** Şampiyonları zaman, eğitim ya da yetki vermeden atamak.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Güvenlik tepkisel ve merkezidir. İncelemeler varsa geç yapılır ve tehdit modelleme yoktur. Olaylar geçici düzeltmeleri tetikler. Mühendisler güvenliği başkasının sorunu olarak görür ve paylaşılan bir standart yoktur.

**Düzey 2, Geliştirme.** Bir güvenlik takımı vardır ve standartlar tanımlar, ancak uygulama takımlar arasında tutarsızdır. Büyük projelerde bir miktar tehdit modelleme yapılır, diğerlerinde hiç yapılmaz. Temel eğitim mevcuttur. Güvenlik hâlâ bir kapı olarak algılanır ve sola kaydırma gerçek değil, arzu edilen bir şeydir.

**Düzey 3, Standartlaştırma.** Güvenlik şampiyonları her takıma yerleşmiştir. Tehdit modelleme yeni hizmetler için rutindir, CIA sınıflandırmasına göre katmanlanır ve güvenli geliştirme yaşam döngüsü kurum genelinde belgelenmiş ve zorunlu kılınmıştır. Riske dayalı önceliklendirme işi yönlendirir, güvenli kodlama standartları ve hat kontrolleri varsayılan asfalt yoldur ve suçlamasız olay sonrası incelemeler norm haline gelmiştir.

**Düzey 4, Yönetme.** Güvenlik sonuçları ölçülür ve taban çizgilerine göre kontrol edilir. Kurum, yüksek önem düzeyli bulguları gidermenin medyan süresini, tehdit modeli kapsamını, üretimden önce yakalanan olayların payını ve ramak kala bildirim oranlarını takım bazında izler. Şampiyonların bir yayını durdurma yetkisi tanımlanmıştır ve gerçekten kullanılır. Risk kararları olasılık çarpı etki olarak nicelleştirilir, kaydedilir ve sabit bir ritimde gözden geçirilir; böylece kontrol boşlukları sürpriz olarak değil veri olarak ortaya çıkar.

**Düzey 5, Orkestrasyon.** Güvenlik gerçekten herkesin işidir ve teslimat, risk ve iş planlamasıyla bütünleşiktir. Tehdit modelleme ve güvenli tasarım alışkanlık haline gelmiştir ve hafiftir, sıfır güven ilkeleri büyük ölçüde gerçekleşmiştir. Metrikler sürekli iyileştirmeyi yönlendirir, kurum takımlar arasında ramak kalalardan öğrenir ve kontroller tehdit tablosu ile mimari değiştikçe otomatik olarak uyum sağlar.

## Tartışma fikirleri

1. Eğitim tamamlamalarını saymanın ötesinde, bir güvenlik kültürünün gerçekten iyileşip iyileşmediğini nasıl ölçersiniz?
2. Güvenlik şampiyonlarının ele aldığı şeyle merkezi takımın sahip olduğu şey arasındaki doğru sınır nerededir?
3. Tehdit modellemeyi bürokratik bir onay kutusuna dönüştürmeden nasıl değerli tutarsınız?
4. Eski envanteriniz için tam bir sıfır güven mimarisi gerçekçi mi ve değilse pragmatik alt küme nedir?
5. Güvenlik işi, aynı mühendisler için yarışan özellik teslimatına karşı nasıl önceliklendirilmelidir?
6. Hangi teşvikler mühendis davranışını güvenlik sahipliğine doğru gerçekten değiştirir?

## Önemli çıkarımlar

- Güvenlik, büyük kurumların kültürel bir özelliğidir; tek bir takıma devredilen bir görev değildir.
- Güvenlik şampiyonları uzmanlığı ve sahipliği mühendislik genelinde ölçeklendirir.
- Tehdit modelleme (STRIDE, PASTA, saldırı ağaçları) tasarım kusurlarını erken ve ucuza ortaya çıkarır.
- Güvenli bir SDLC ve sola kaydırma zihniyeti, kusurları en az maliyetli oldukları anda yakalar.
- Derinlemesine savunma, en az ayrıcalık ve sıfır güven temel mimari ilkelerdir.
- CIA üçlüsü ve riske dayalı önceliklendirme, kıt çabayı en çok önem taşıdığı yere yöneltir.
- Güvenlik kültürü inşa etmenin maliyeti, önlediği ihlallerin maliyetinden çok daha küçüktür.

## Kaynaklar ve ileri okuma

- Adam Shostack, *Threat Modelling: Designing for Security*
- Ross Anderson, *Security Engineering: A Guide to Building Dependable Distributed Systems*
- Michael Howard and Steve Lipner, *The Security Development Lifecycle*
- Betsy Beyer et al. (Google), *Building Secure and Reliable Systems*
- National Institute of Standards and Technology, *SP 800-207: Zero Trust Architecture*
- National Institute of Standards and Technology, *Secure Software Development Framework (SSDF), SP 800-218*
- OWASP, *Threat Modelling* and *Security Champions* guidance
