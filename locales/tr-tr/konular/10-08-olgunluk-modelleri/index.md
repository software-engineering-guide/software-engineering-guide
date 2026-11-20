# 10.8 Olgunluk modelleri

## Genel bakış ve motivasyon

[Olgunluk modeli](https://en.wikipedia.org/wiki/Maturity_model), uygulamanızın bir alanda ne kadar yetkin ve tutarlı olduğunu değerlendirmenin ve onu iyileştirmek için bir yol tanımlamanın yapılandırılmış bir yoludur. Küçük bir düzey merdiveni tanımlar. En altta iş gelişigüzel ve tepkiseldir. En üstte ölçülür, yönetilir ve sürekli en iyilenir. Her basamağın karşısında kontrol edebileceğiniz gözlemlenebilir özellikler vardır.

Olgunluk modelleri belirsiz bir soruyu ("bunda iyi miyiz?") tekrarlanabilir bir cevaba çevirir ("burada düzey 2'deyiz, şurada düzey 4'teyiz ve düzey 3 şunu gerektirirdi"). Bu kitap her bölümde beş düzeyli bir model kullanır ve bunları bölüm 12.4'te birleştirir. Bu bölüm disiplinin kendisiyle ilgilidir: modellerin nasıl çalıştığı, ne zaman yardımcı olduğu ve nasıl yanılttığı.

Önemli olmalarının nedeni basittir. Büyük kurumlar göremedikleri şeyi iyileştiremez. Düzinelerce takım boyunca yetkinlik muazzam ve görünmez biçimde değişir. Bazı takımların mükemmel testleri ve zayıf güvenliği vardır; bazılarında tersi. Bir olgunluk modeli size ortak bir sözcük dağarcığı ve ortak bir ölçüt verir; böylece boşluklar karşılaştırılabilir olur, yatırım önceliklendirilebilir ve ilerleme yalnızca ileri sürülmek yerine zaman içinde izlenebilir. İyi bilinen örnekler arasında CMMI ([Capability Maturity Model Integration](https://en.wikipedia.org/wiki/Capability_Maturity_Model_Integration), süreç için), DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) modeli (yazılım teslimat performansı), yazılım güvenliği için OWASP SAMM (Software Assurance Maturity Model) ve BSIMM (Building Security In Maturity Model), TMMi (Test Maturity Model integration, test için), Agile Fluency modeli ve veri yönetimi olgunluk modelleri ile sayısız iç puan kartı vardır.

Kurumsal ve özellikle kamu için olgunluk modelleri özel bir ağırlık taşır. Devlet sözleşmeciliği uzun süredir CMMI değerlendirme düzeylerini bir tedarikçi yeterliliği olarak kullanmıştır ve ABD CMMC ([Cybersecurity Maturity Model Certification](https://en.wikipedia.org/wiki/Cybersecurity_Maturity_Model_Certification)) gibi çerçeveler siber güvenlik olgunluğunu savunma işine uygunluğa doğrudan bağlar. Bu olgunluk modellerine gerçek diş verir. Aynı zamanda bu bölümün merkezî riskini de yaratır: bir düzey kapı ya da hedef olduğunda insanlar altta yatan yetkinlik yerine değerlendirme için optimize eder. İyi kullanıldığında olgunluk modelleri bir aynadır. Kötü kullanıldığında tiyatrodur.

## Temel ilkeler

- **Olgunluk bir araçtır, amaç değil.** Hedef bir düzey numarası değil, yetkinlik ve sonuçlardır.
- **Puanlamak için değil, öğrenmek için değerlendirin.** Dürüst özdeğerlendirme, pohpohlayıcı bir değerlendirmeden iyidir.
- **Yüksek her zaman daha iyi değildir.** Doğru hedef riske, bağlama ve maliyete bağlıdır.
- **Tek bir küresel not değil, alan başına ölçün.** Yetkinlik eşitsizdir; tek bir sayı bunu gizler.
- **En düşük olgunluklu, en yüksek riskli boşlukları önce önceliklendirin.**
- **[Goodhart Yasası](https://en.wikipedia.org/wiki/Goodhart%27s_law)'na dikkat edin.** Bir düzey hedef olduğunda yetkinliği ölçmeyi bırakır.
- **Düzenli aralıklarla yeniden değerlendirin.** İnsanlar, sistemler ve tehditler değiştikçe olgunluk kayar.

## Öneriler

### Alan için doğru modeli seçin

Modeli iyileştirmek istediğiniz yetkinliğe uydurun ve var oldukları yerde icat edilmişlere göre yerleşik, kanıta dayalı modelleri tercih edin:

- **Süreç ve teslimat:** CMMI (geniş süreç olgunluğu), DORA yetkinlik modeli (araştırmaya dayalı teslimat performansı, bölüm 11.2).
- **Güvenlik:** OWASP SAMM ve BSIMM (yazılım güvenliği uygulamaları), CMMC (savunma siber güvenliği).
- **Test ve kalite:** TMMi.
- **Çeviklik ve çalışma biçimleri:** Agile Fluency modeli (bölüm 10.7).
- **Veri:** veri yönetimi olgunluk modelleri (DMM, DCAM).

İç kullanım için yetkinlik başına uygulanan basit bir dört ya da beş düzeyli ölçek (bu kitabın yaptığı gibi) çoğu zaman ağır bir dış çerçeveden daha uygulanabilirdir. Resmî, değerlendirilmiş modelleri sözleşmesel olarak gerektikleri yerlere saklayın.

### Dürüstçe ve yetkinlik başına değerlendirin

Rahatlık değil, gerçek üreten değerlendirmeler yürütün. İşi yapan insanları dahil edin. Görüş değil, kanıt toplayın. Her yetkinliği ayrı puanlayın; böylece tablo gerçekliği yansıtır: burada güçlü, şurada zayıf. İyileştirmeyi yönlendirmek için kullanılan bir özdeğerlendirme, bir rozet kazanmak için kullanılan dış bir değerlendirmeden daha değerlidir; çünkü birincisi açık sözlülüğü, ikincisi sunumu ödüllendirir. Bölüm 12.4, bu kitaptaki her alan boyunca birleşik bir özdeğerlendirme sağlar; bunu başlangıç aracı olarak kullanın.

### Olgunluğu cezalandırmak için değil, önceliklendirmek için kullanın

Bir değerlendirmenin çıktısı suçlama için bir karne değil, önceliklendirilmiş bir iyileştirme iş listesidir. Olgunluğu riskle birleştirin. Düşük riskli bir alandaki düzey 1 yetkinlik sorun olmayabilir. Güvenlik ya da uyum açısından kritik bir alandaki düzey 2 yetkinlik acildir. Yatırımı düşük olgunluğun yüksek riskle buluştuğu boşluklara yönlendirin ve işi sonuçlara (bölüm 11.1) bağlayın; böylece iyileştirme, merdivene kendi uğruna tırmanılarak değil, sonuçlarla ölçülür.

### Hedef düzeyleri bilinçli belirleyin: yüksek bedava değildir

Her düzey yukarı çıkış çaba maliyeti taşır ve çoğu zaman süreç ağırlığı ekler. Doğru hedef nadiren "her yerde düzey 5"tir. Ek yetkinliğin o alanın riski için ek maliyeti hâlâ haklı çıkardığı düzeydir. Düzenlemeye tabi ve güvenlik açısından kritik yetkinlikler gerçekten üst basamaklara ihtiyaç duyabilir ve denetim çoğu zaman en az "tanımlı" bir düzey 3 gerektirir. Diğer birçoğu düzey 3'te iyi hizmet alır ve daha fazla zorlamakla yalnızca bürokrasi biriktirir. Hedefleri yetkinlik başına belirleyin ve riske göre ayarlanmış getiri durduğunda tırmanmayı bırakın.

### Olgunluk tiyatrosuna karşı korunun

Olgunluk modellerinin değerini yok eden tek başarısızlık biçimi puan için optimize etmektir. Cömert not veren değerlendirmelere, yalnızca değerlendirme için derlenen kanıta ya da üretim olaylarının çürüttüğü "düzey 5" iddialarına dikkat edin. Değerlendirmeyi gözlemlenebilir davranışa ve gerçek sonuçlara bağlı tutun. Değerlendiricilerinizi döndürün ya da dışarıdan akıl sağlığı kontrolüne tabi tutun. Şüpheli biçimde yüksek bir özpuanı bir koku olarak ele alın. Düzey hedef olduğu an model size gerçeği söylemeyi bırakır.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
|---|---|---|
| **Resmî değerlendirilmiş modeller (CMMI, CMMC)** | Karşılaştırılabilir, sözleşmesel olarak tanınır, titiz | Maliyetli; oyunlamaya davetiye çıkarır; süreci katılaştırabilir |
| **Hafif iç puan kartları** | Hızlı, uygulanabilir, düşük ek yük | Dışarıyla daha az karşılaştırılabilir; önyargılanması kolay |
| **Kanıta dayalı yetkinlik modelleri (DORA)** | Gerçek sonuçlara bağlı; araştırma destekli | Daha dar kapsam; gerçek metrikler gerekir |
| **Tek genel olgunluk notu** | İletmesi basit | Eşitsiz yetkinliği gizler; yanıltır |
| **Yetkinlik başına değerlendirme** | Doğru, uygulanabilir önceliklendirme | Daha fazla çaba; tek başlık sayısı yok |

Merkezî gerilim **ayna olarak değerlendirme ile hedef olarak değerlendirme** arasındadır. Bir takımın kendini net görmesine yardım eden aynı model, bir düzey ödüle, uygunluğa ya da statüye bağlandığı anda ters etki yapar. Bir düzey ne kadar önemliyse, enerji o kadar çok özün değil, olgunluğun görünümüne akar.

## Takımınızla tartışılacak sorular

1. **Sözleşmesel olarak değerlendirilmiş herhangi bir düzeyden ayrı, açık sözlü bir iç özdeğerlendirme tutmalı mıyız ve her birinin sahibi kim?** Bir CMMC ya da CMMI düzeyi geliri kapıdan geçirdiğinde değerlendirme ve gerçek birbirinden uzaklaşır, çünkü enerji iyileşmeye değil, geçmeye akar. Büyük bir kurum ya da bir devlet tedarikçisi için bu boşluk riskin saklandığı yerdir: denetimi geçersiniz ve açıkta kalırsınız. Bilinçli olarak iki defter tutun. Resmî değerlendirmeyi uygunluk için saklayın ve kimsenin şişirmekle ödüllendirilmediği, açık sözlü bir iç puan kartı tutun. Her biri için bir sahip adlandırın ve aralarındaki herhangi bir mesafeyi üstünü örtmek için değil, araştırmak için bir sinyal sayın. Hangi defterin gerçeği söylediğine kanıt olarak son olayları, ramak kalanları ve değerlendirme sonrası çürümeyi toplantıya getirin.

2. **Her alan için yerleşik, kanıta dayalı bir model mi benimsiyoruz yoksa kendi puan kartımızı mı icat ediyoruz ve bu doğru karar mı?** Yerleşik modeller (teslimat için DORA, güvenlik için SAMM ya da BSIMM, test için TMMi) evde yapılmış bir ızgaranın eşleşemeyeceği araştırma ve dış karşılaştırılabilirlik taşır. Hafif bir iç dört düzeyli ölçek daha hızlı ve daha uygulanabilirdir ve iç yönlendirme için çoğu zaman daha iyi seçimdir. Tuzak, resmî bir modelin tüm töreni olup kanıt tabanının hiçbiri olmayan ağır bir özel çerçeve icat etmektir. Alan başına karar verin: resmî değerlendirilmiş modelleri bir sözleşmenin gerektirdiği yerlere saklayın, var oldukları ve uydukları yerde kanıta dayalı modelleri kullanın ve geri kalan her şey için basit bir yetkinlik başına ölçek tutun. Alanların listesini getirin, her birinin bugün hangi modeli kullandığını işaretleyin ve icat edilmiş her puan kartına meydan okuyun.

3. **Değerlendirmelerimizi kim yürütüyor, cömert notlandırmayı nasıl yakalarız ve ne sıklıkla yeniden değerlendiririz?** Kendini notlandıran bir değerlendirme kendini pohpohlar ve olgunluk insanlar, sistemler ve tehditler değiştikçe kayar; bu yüzden iki yıllık bir değerlendirme çoğu zaman kurgudur. Değerlendiricileri döndürün ya da dışarıdan bir akıl sağlığı kontrolü getirin ve şüpheli biçimde yüksek bir özpuanı kutlanacak bir zafer değil, kovalanacak bir koku olarak ele alın. Yeniden değerlendirme ritmini her alanın ne kadar hızlı değiştiğine bağlayın: güvenlik, örneğin belgelemeden daha sık. Yöneticilerden görüş toplamak yerine kanıt toplayın ve işi yapan insanları dahil edin. Cevabınız bir takımın yılda bir kez, çapraz kontrol olmadan kendini puanlaması ise yetkinliği değil, rahatlığı ölçüyorsunuz.

4. **Her yetkinlik gerçekte hangi hedef olgunluk düzeyine ihtiyaç duyuyor ve daha yükseğe zorlamak nerede yalnızca süreç ağırlığı satın alır?** Yüksek bedava değildir: her düzey yukarı çıkış çaba maliyeti taşır ve genellikle tören ekler; bu yüzden her yerde düzey 5 gibi toptan bir hedef, bazı alanların hiç geri ödemeyeceği bürokrasiye sınırlı bir iyileştirme bütçesini boşaltır. Büyük bir kurum için doğru hedef yetkinliğe göre değişir; çünkü düşük riskli bir alanda düzey 2 mükemmel güvenli olabilirken, güvenlik ya da uyum açısından kritik bir alanda aynı düzey bir acil durumdur. Yetkinlik başına bir risk derecelendirmesi, bir sonraki basamağın çaba ve süreçte neye mal olacağına dair dürüst bir tahmin ve herhangi bir denetim ya da sözleşme tabanı getirin; çünkü birçok denetim en az tanımlı bir düzey 3 gerektirir. Kurumsal ve kamu ortamlarında bazı düzenlemeye tabi yetkinlikler gerçekten üst basamaklara ihtiyaç duyar, çoğu ise düzey 3'te iyi hizmet alır; bu yüzden hedefleri bilinçli, yetkinlik yetkinlik belirleyin ve riske göre ayarlanmış getiri durduğunda tırmanmayı bırakın.

5. **Bir olgunluk düzeyini son yükselttiğimizde, korumak istediği sonuç gerçekten iyileşti mi yoksa yalnızca puan mı hareket etti?** Olaylar, teslim süresi ya da kusur oranları düz kalırken tırmanan bir düzey iş başındaki Goodhart Yasası'dır: sayı hedef olduğunda yetkinliği ölçmeyi bırakır. Büyük bir takım için bu kolayca gözden kaçar; çünkü başarılı bir değerlendirme, üretim farklı bir hikâye anlatsa bile ilerleme gibi hissettirir. Yatırım yapmadan önce her yetkinliğin düzeyini gerçek bir sonuç metriğine bağlayın, sonra öncesi ve sonrası kanıtını tartışmaya getirin: üç ayda bir olaylar, değişiklik başarısızlık oranı, kurtarma süresi, yetkinliğin neyi iyileştirmek için var olduğuna bağlı olarak. Değerlendirilmiş bir düzeyin uygunluğu kapıdan geçirdiği kurumsal ve kamu portföylerinde boşluk tehlikelidir; çünkü düzey derlenen kanıtla yükselirken altta yatan uygulama sessizce çürüyebilir ve bunun ilk kanıtı bir ihlal, kesinti ya da başarısız denetimdir.

6. **Tek bir başlık olgunluk notu mu yoksa yetkinlik başına bir tablo mu iletiyoruz ve düzeyler hiç ödüle, sıralamaya ya da takım statüsüne bağlanıyor mu?** Tek bir genel sayıyı liderliğe sunmak kolaydır ve tam da önemli olan eşitsizliği gizler; çünkü güçlü teslimat düzey 1'lik bir güvenlik yetkinliğini maskeleyebilir; yetkinlik başına bir ısı haritası daha fazla iş ister, ama düşük olgunluğun yüksek riskle nerede buluştuğunu gösterir. Daha zor soru puanların nasıl kullanıldığıdır; çünkü bir düzey bir takımın ödülüne ya da sıralamasına bağlandığı an dürüst raporlama ölür ve enerji özün değil, olgunluğun görünümüne akar. Isı haritasını ve bir düzeyin şu anda bir performans değerlendirmesini, bir bütçe kararını ya da bir tedarikçi puan kartını beslediği her yerin açık sözlü bir dökümünü getirin. Değerlendirilmiş düzeylerin geliri ve uygunluğu kapıdan geçirebildiği kurumlar ve devlet tedarikçileri için hangi notların sonuç taşıdığı ve hangilerinin yalnızca yönlendirmek için var olduğu konusunda açık olun; çünkü insanların şişirmekle ödüllendirildiği bir olgunluk tablosu gerçeği betimlemeyi bırakır.

## Sektör merceği

**Girişim.** Kısa bir pistte ağır, değerlendirilmiş bir model karşılayamayacağınız ek yüktür. Birkaç yetkinlik boyunca basit bir ölçekte bir saatlik özdeğerlendirme yapın, yalnızca somut bir şeyi engelleyen en düşük olgunluklu boşluğu düzeltin (örneğin ilk kurumsal müşterinizin güvenlik anketi) ve gerisine dokunmayın. Değerlendirme bir danışmana değil, bir öğleden sonraya mal olmalı ve çıktısı ihtiyaç duymadığınız ve finanse edemeyeceğiniz tekdüze yüksek bir puan değil, tek bir sonraki eylem olmalıdır.

**Küçük işletme.** Özel bir değerlendiriciniz ve dar bir bütçeniz yok; bu yüzden özel bir çerçeve görevlendirmek yerine hafif bir kamusal model ödünç alın: kendiniz puanlayabileceğiniz kısa bir teslimat ya da güvenlik kontrol listesi. Bunu sürekli bir program olarak değil, zayıf bir noktanın size bir müşteriye mal olacağı yere dair yıllık bir sohbet olarak ele alın. Ucuz ve açık sözlü tutun; çünkü bir tedarikçiye ürettirmek için ödediğiniz pohpohlayıcı bir puan, bir öğleden sonra kendiniz yaptığınız açık sözlü bir puandan daha az değerlidir.

**Kurumsal.** Değer, birçok takım boyunca tutarlı biçimde uygulanan ortak bir yetkinlik başına puan kartıdır; böylece boşluklar karşılaştırılabilir olur ve iyileştirme bütçesi düşük olgunluğun yüksek riskle buluştuğu yere akar. Düzeyler bütçeyi ya da statüyü beslemeye başladığında olgunluk tiyatrosuna karşı sıkı korunun: değerlendiricileri döndürün ya da dışarıdan akıl sağlığı kontrolüne tabi tutun ve sonuçları takımları sıralayıp dürüst raporlamayı öldüren bir lig tablosu değil, asfaltlanmış yol yatırımını (bölüm 4.2) yönlendiren bir ısı haritası olarak yönetin.

**Kamu.** Bir olgunluk düzeyi burada çoğu zaman gerçek bir kapıdır: savunma işi için CMMC, bir tedarikçi yeterliliği olarak CMMI değerlendirmesi. Gereken düzeyi gerçek yetkinlikle karşılayın ve denetim tabanının sessizce tavana dönüşmemesi için açık sözlü bir iç özdeğerlendirmeyi resmî değerlendirmeden ayrı tutun. Kanıtı değerlendiricilere şeffaf biçimde belgeleyin ve sertifikalı düzey ile gerçek uygulama arasındaki mesafeyi dosyalanacak evrak değil, kapatılacak hesap verebilir bir risk olarak ele alın.

## Örnekler

**Girişim.** On kişilik bir SaaS girişimi, teslimat, test, güvenlik ve nöbeti kapsayan basit bir dört düzeyli ölçeğe karşı bir saatlik özdeğerlendirme yürütür. Teslimat ve testi düzey 3'te, ama güvenliği düzey 1'de takılı bulur; bu önemlidir, çünkü ilk kurumsal müşterisini bir güvenlik anketiyle imzalamak üzeredir. Bu yüzden kurucular önümüzdeki ayı yalnızca güvenliği savunulabilir bir düzey 2'ye çıkarmaya harcar ve ihtiyaç duymadıkları ve henüz karşılayamayacakları tekdüze yüksek bir puanın peşinden koşmak yerine gerisine dokunmaz.

**Kurumsal.** Bir finansal hizmetler firması 40 takımını hafif bir yetkinlik başına puan kartıyla (teslimat, test, güvenlik, gözlemlenebilirlik, nöbet) değerlendirir. Isı haritası, güvenlik olgunluğunun en çok düzenleyici maruziyetin en yüksek olduğu yerde geride kaldığını ortaya çıkarır; bu yüzden platform takımı önce o takımlar için asfaltlanmış yol güvenlik araçlarını (bölüm 4.2) finanse eder. Değerlendirme takımları sıralamak yerine yatırımı önceliklendirmek için kullanıldığından yöneticiler dürüstçe raporlar. Bir yıl sonraki yeniden değerlendirme gerçek hareket gösterir ve en önemlisi yalnızca daha yüksek puanları değil, daha az güvenlik olayını da.

**Kamu.** Bir savunma yüklenicisi iş için teklif vermek üzere gereken bir CMMC düzeyine ulaşmalıdır ve bir sistem entegratörü sözleşme yeterliliği olarak bir CMMI değerlendirmesi tutar. Burada olgunluk düzeyi gelire giden gerçek bir kapıdır. İyi yürütülen sürüm gereken düzeyi gerçek yetkinlik için bir taban sayar ve açık sözlü bir iç özdeğerlendirmeyi resmî değerlendirmeden ayrı tutar. Kötü yürütülen sürüm değerlendirme için kanıt derler ve gerçek uygulamanın ertesi gün çürümesine izin verir; denetimi geçer ama açıkta kalır.

## İş gerekçesi: motivasyonlar, YG ve TSM

Olgunluk değerlendirmesinin getirisi **yönlendirilmiş yatırımdan** gelir. İyileştirme bütçeleri sınırlıdır. Körü körüne harcandığında en gürültülü olanı finanse eder. Bir olgunluk değerlendirmesi yetkinliğin riske karşı en zayıf olduğu yeri gösterir; böylece aynı harcama daha fazla risk azaltması ve daha fazla sonuç iyileşmesi satın alır. Değerlendirmenin kendisi ucuzdur, yalnızca birkaç günlük yapılandırılmış, kanıta dayalı inceleme; yanlış tahsis edilmiş iyileştirme programlarının ya da daha kötüsü bir ihlal, kesinti ya da başarısız denetim olarak yüzeye çıkan tespit edilmemiş bir yetkinlik boşluğunun maliyetine karşı.

**Toplam sahip olma maliyetinde** disiplin hafif tuttuğunuzda düşük maliyetlidir ve değerlendirme bürokrasisine katılaştığında yüksek maliyetlidir. Başlıca gizli maliyet *olgunluk tiyatrosudur*: olgunluğun görünümünü üretmeye harcanan çaba hiçbir şey getirmez ve gerçek riski maskeleyebilir; bu negatif YG'dir. Liderliğe gerekçeyi sunmak için olgunluğu bir risk ve yatırım merceği olarak, "her şeyi iyileştir"i "önce şu üç şeyi iyileştir"e çeviren bir ısı haritası olarak sunun ve düzeyleri kendi uğruna kovalama dürtüsüne karşı açıkça bütçeleyin. Bir düzeyin sözleşmesel olarak gerektiği yerde (CMMC, CMMI) YG doğrudandır: uygunluğun bedelidir ve amaç onu maliyetli bir numara ile değil, gerçek yetkinlikle karşılamaktır.

## Anti-kalıplar ve tuzaklar

- **Hedef olarak düzey:** temsil etmesi gereken yetkinlik yerine bir sayının peşinden koşmak.
- **Olgunluk tiyatrosu:** gerçek uygulama çürürken bir değerlendirme için kanıt derlemek.
- **Tek küresel not:** tehlikeli eşitsizliği gizleyen tek bir olgunluk puanı.
- **Yüksek her zaman daha iyi:** risk ya da maliyetten bağımsız olarak her yetkinliği düzey 5'e zorlamak.
- **Bir kez değerlendir, bir daha asla:** tek seferlik bir değerlendirmeyi kalıcı gerçek saymak.
- **Suçlamak için takımları sıralamak:** olgunluğu cezalandırma için kullanmak, dürüst raporlamayı öldürür.
- **Model tapınması:** ağır bir çerçevenin törenini yararlılığın ötesine kadar izlemek.
- **Sonuçları görmezden gelmek:** teslimat, güvenilirlik ya da güvenlik iyileşmezken merdivene tırmanmak.

## Olgunluk modeli

- **Düzey 1, Başlangıç.** Olgunluğa dair paylaşılan bir kavram yok; yetkinlik varsayılır, eşitsizdir ve ölçülmez; herhangi bir değerlendirme planlı değil, bir olay ya da denetim talebiyle tetiklenen tepkiseldir.
- **Düzey 2, Geliştirme.** Birkaç takım bir ölçeğe karşı gelişigüzel değerlendirmeler yürütür, ama model, ritim ve titizlik takımdan takıma değişir; sonuçlar tutarsız kullanılır ve kanıt zayıftır, bu yüzden görünüm için puanlama daima mevcut bir risktir.
- **Düzey 3, Standartlaştırma.** Tek bir yetkinlik başına model ve değerlendirme ritmi belgelenmiş ve kurum genelinde uygulanır; değerlendirmeler kanıta dayalıdır, işi yapan insanları dahil eder ve bir karne yerine önceliklendirilmiş bir iyileştirme iş listesini besler.
- **Düzey 4, Yönetme.** Olgunluk veriyle ölçülür ve denetlenir: her yetkinliğin düzeyi bir temel çizgiye karşı izlenir, bir sonuç metriğine (olaylar, teslim süresi, değişiklik başarısızlık oranı) bağlanır ve belirlenmiş bir ritimle yeniden değerlendirilir; böylece kayma ve cömert notlandırma görüş değil, sayı olarak görünür ve hedefler riske ve maliyete karşı alan başına bilinçli belirlenir.
- **Düzey 5, Orkestrasyon.** Değerlendirme kurum genelinde bütünleşiktir ve sürekli iyileştirilir: olgunluk, risk ve sonuçlar yatırımı tek uyarlanabilir bir tablo olarak bilgilendirir, hedefler tehditler ve bağlam değiştikçe yeniden dengelenir, değerlendiriciler olağan olarak döndürülür ya da dışarıdan kontrol edilir ve uygulama artık maliyetini hak etmeyen töreni aktif olarak emekliye ayırır.

## Tartışma fikirleri

1. Yetkinliklerinizin hangilerini kanıt olmadan olgun varsayıyorsunuz?
2. En düşük olgunluğunuz en yüksek riskinizle nerede çakışıyor ve iyileştirme bütçeniz oraya mı gidiyor?
3. Kurumunuzda herhangi bir olgunluk düzeyi bir hedef ya da kapı mı? Bu hangi davranışı üretti?
4. Her yetkinlik için doğru hedef düzey nedir ve daha fazla tırmanmak nerede yalnızca bürokrasi ekler?
5. Takımlarınız olgunluklarını dürüstçe raporlar mıydı, yoksa puanları kullanma biçiminiz açık sözlülüğü cezalandırıyor mu?
6. En son "olgunluğu iyileştirdiğinizde" sonuçlar gerçekten değişti mi?

## Önemli çıkarımlar

- Bir olgunluk modeli yetkinliği bir düzey merdivenine karşı değerlendirir ve iyileşmek için bir yol tanımlar: bir ayna, bir kupa değil.
- Alan başına yerleşik, kanıta dayalı modelleri seçin (CMMI, DORA, SAMM/BSIMM, CMMC); hafif bir yetkinlik başına ölçek çoğu zaman en uygulanabilir olanıdır.
- **Dürüstçe, yetkinlik başına değerlendirin** ve sonuçları sıralamak ya da suçlamak için değil, **riske göre önceliklendirmek** için kullanın.
- **Yüksek her zaman daha iyi değildir:** hedef düzeyleri riske ve maliyete karşı bilinçli belirleyin.
- **Olgunluk tiyatrosuna** ve **Goodhart Yasası**'na dikkat edin: hedef olan bir düzey yetkinliği ölçmeyi bırakır.
- Bu kitabın birleşik olgunluk özdeğerlendirmesi ve her bölümün kendi olgunluk bölümü için bkz. bölüm 12.4.

## Kaynaklar ve ileri okuma

- CMMI Institute / ISACA, *Capability Maturity Model Integration (CMMI)*.
- Watts Humphrey, *Managing the Software Process* (origins of software process maturity).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (capability, not maturity-level, thinking for delivery).
- OWASP, *Software Assurance Maturity Model (SAMM)*; BSIMM (*Building Security In Maturity Model*).
- U.S. Department of Defence, *Cybersecurity Maturity Model Certification (CMMC)*.
- TMMi Foundation, *Test Maturity Model integration*.
- James Shore and Diana Larsen, *The Agile Fluency Model*.
- Martin Fowler, "Maturity Model" (bliki), on their uses and abuses.
