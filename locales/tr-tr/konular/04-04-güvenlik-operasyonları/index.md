# 4.4 Güvenlik operasyonları

## Genel bakış ve motivasyon

Önleme gereklidir, ama asla yeterli değildir. Kararlı saldırganlar, yeni zafiyetler ve sıradan insan hataları, bazı tehditlerin savunmalarınızı aşacağı anlamına gelir. Güvenlik operasyonları, onları hızla bulma, iyi yanıt verme ve öğrendiklerinizi daha güçlü savunmalara geri besleme disiplinidir. Dakikalar içinde sınırlandırılan bir olayla, kimse fark etmeden aylarca çürüyen bir olay arasındaki farktır.

Büyük bir kurumda güvenlik operasyonlarının ölçekle ve hızla çalışması gerekir. Binlerce hizmet okyanuslar kadar günlük üretir. Her hafta yüzlerce yeni zafiyet duyurulur. Dağıtım hiç durmaz. El işçiliğine dayanan operasyonlar buna yetişemez. Çözüm, güvenliği teslimat hattına gömmek ([DevSecOps](https://en.wikipedia.org/wiki/DevSecOps)), tespiti ve yanıtı otomatikleştirmek ve olaylar başınıza geldiğinde sakin kalabilecek kası geliştirmektir. Kamu için güvenlik operasyonları ayrıca yasal yükümlülükler taşır: zorunlu olay bildirim süreleri, koordineli zafiyet açıklaması ve hukuki incelemeye dayanabilecek adli titizlik.

Bu bölüm güvenliği hatta entegre etmeyi, zafiyetleri ve yamaları yönetmeyi, olaylara yanıt vermeyi ve adli inceleme yapmayı, tespiti [SIEM](https://en.wikipedia.org/wiki/Security_information_and_event_management) ve SOAR ile yürütmeyi ve savunmaları kırmızı ve mor takım çalışmaları ile [sızma testi](https://en.wikipedia.org/wiki/Penetration_test) ile doğrulamayı kapsar.

## Temel ilkeler

- **Rutini otomatikleştirin.** Makineler tarama, ilişkilendirme ve tekrarlayan yanıtı üstlenir; insanlar muhakemeye odaklanır.
- **Güvenliği hatta kaydırın.** Testler ve kapılar, mühendislerin zaten çalıştığı yerde hızlı geri bildirim veren [CI/CD](https://en.wikipedia.org/wiki/CI/CD) (sürekli entegrasyon ve sürekli teslimat) içinde yaşar.
- **İhlali varsayın ve hazırlanın.** Olay müdahalesini ihtiyaç duymadan önce prova edin; olay anı doğaçlama zamanı değildir.
- **Süreyi ölçün ve azaltın.** Ortalama tespit süresi ve ortalama yanıt süresi en önemli metriklerdir.
- **Suçlamasız öğrenme.** Her olay ve ramak kala durum, cezalandıracak birini aramak yerine sistemi sağlamlaştıran bir derse dönüşür.
- **Savunmaları saldırgan gözüyle doğrulayın.** Güvenliğinizi gerçek saldırganların yapacağı gibi test edin, sonra bulduklarını düzeltin.
- **Tespit mühendisliği bir üründür.** Tespitlere kod gibi davranın: sürüm kontrollü, test edilmiş ve sürekli iyileştirilen.

## Öneriler

### DevSecOps'u hatta yerleştirin

Otomatik güvenlik testlerini doğrudan sürekli entegrasyona ve teslimata katın; geri bildirim mühendislere dakikalar içinde ulaşsın:

- **[SAST](https://en.wikipedia.org/wiki/Static_application_security_testing)** (Statik Uygulama Güvenliği Testi), kaynak kodu commit edilirken zafiyetli kalıplar için analiz eder.
- **[DAST](https://en.wikipedia.org/wiki/Dynamic_application_security_testing)** (Dinamik Uygulama Güvenliği Testi), çalışan uygulamayı sömürülebilir kusurlar için yoklar.
- **SCA** (Yazılım Bileşeni Analizi), bilinen zafiyetli bağımlılıkları işaretler.
- **IaC taraması**, kod olarak altyapıdaki güvensiz yapılandırmaları dağıtılmadan önce kontrol eder.
- **Gizli bilgi taraması**, kimlik bilgilerinin depoya girmesini engeller.

Yanlış pozitifleri kontrol altında tutmak için bu araçları acımasızca ayarlayın. Boşuna alarm veren bir tarayıcı görmezden gelinir. Riske dayalı kapılar koyun: yüksek önem derecesindeki ve yüksek güvenilirlikteki bulgularda engelleyin, gerisini teslimatı durdurmadan izleyin. İstediğiniz hızlı ve güvenilir bir sinyaldir, gürültü duvarı değil.

### Zafiyetleri yönetin ve yamaları sistematik uygulayın

Sürekli akan zafiyetler, her manşette yeni bir panik değil, sistematik ve önceliklendirilmiş bir süreç gerektirir.

- Herhangi bir zafiyetten nelerin etkilenebileceğini bilmek için doğru bir varlık envanteri tutun.
- Düzeltmeyi gerçek riske göre önceliklendirin: yalnızca ham puana göre yama yapmak yerine önem derecesini, sömürülebilirliği (gerçek dünyada sömürülüyor mu?), maruziyeti ve varlığın kritikliğini birleştirin.
- Önem derecesi kademesine göre **düzeltme SLA'ları** (hizmet düzeyi anlaşmaları) tanımlayın, uygulayın ve uyumu ölçün.
- Güvenle yapabildiğiniz yerde, özellikle altyapı ve bağımlılıklarda yamalamayı otomatikleştirin.
- Net bir bildirim kanalı olan bir **koordineli zafiyet açıklaması** programı ve uygun olduğunda bir [hata ödül programı](https://en.wikipedia.org/wiki/Bug_bounty_program) yürütün; dışarıdaki araştırmacılar kusurları herkese açık biçimde ifşa etmek yerine sorumlu biçimde bildirebilsin.

### Olay müdahalesine hazırlanın ve yürütün

Bir olay başınıza geldiğinde, prova edilmiş bir süreç herhangi bir araçtan daha değerlidir.

- Tanımlı rolleri (olay komutanı, iletişim sorumlusu, araştırmacılar), önem sınıflandırmalarını ve eskalasyon yollarını içeren bir **olay müdahale planı** tutun.
- Net aşamalar belirleyin: **hazırlık, tespit ve analiz, sınırlandırma, ortadan kaldırma, kurtarma ve olay sonrası inceleme.**
- Kanıtı **[adli bilişim](https://en.wikipedia.org/wiki/Digital_forensics)** için doğru biçimde koruyun: bulgular hukuken geçerli ve analiz sağlam olsun diye günlükleri, bellek ve disk görüntülerini belgelenmiş bir gözetim zinciriyle yakalayın.
- **İhlal iletişimini** önceden planlayın: müşterilere, düzenleyicilere ve kamuoyuna kim, hangi zaman çizelgesiyle, hukuk ve halkla ilişkiler katılımıyla bildirir. Düzenleyici saatler (çoğu zaman 72 saat ya da daha az) keşif anında işlemeye başlar.
- Takım gerçek bir krizden önce planı bilsin diye düzenli **masa başı tatbikatlar** yapın ve somut iyileştirmeler üreten suçlamasız olay sonrası incelemeler yürütün.

### Tespiti SIEM ve SOAR ile işletin, tespitleri mühendisliğe tabi tutun

Güvenlik sinyallerinizi bir araya getirin ve ölçekle harekete geçin.

- Tüm yapıdaki günlükleri ve olayları toplamak, ilişkilendirmek ve şüpheli kalıpları yüzeye çıkarmak için bir **SIEM** (Güvenlik Bilgisi ve Olay Yönetimi) kullanın.
- Triyaj ve yanıt oyun kitaplarını otomatikleştirmek için **SOAR** (Güvenlik Orkestrasyonu, Otomasyonu ve Yanıtı) kullanın: uyarıları zenginleştirmek, sunucuları izole etmek, kimlik bilgilerini devre dışı bırakmak ve rutin adımlar için bir insanı beklemeden vaka açmak.
- **Tespit mühendisliği** uygulayın: tespit kurallarını [MITRE ATT&CK](https://en.wikipedia.org/wiki/MITRE_ATT%26CK) gibi bir çerçeveyle hizalanmış, sürümlenmiş ve test edilmiş kod olarak ele alın, gerçek ve yanlış pozitif oranlarını ölçün ve gerçek saldırgan tekniklerinin kapsamını sürekli iyileştirin.
- Uygulamalar ve altyapı genelinde kapsamlı, kurcalamaya dayanıklı günlük tutmayı sağlayın; günlüğe almadığınızı tespit edemezsiniz.

### Savunmaları kırmızı ve mor takım çalışmaları ve sızma testleriyle doğrulayın

Savunmalarınızı bir saldırgan gibi test etmek, gerçekten çalıştıklarını bilmenin tek yoludur.

- **Sızma testi**, belirli sistemlerin odaklı ve belirli bir andaki değerlendirmesini sağlar; çoğu zaman uyum için yapılır.
- **[Kırmızı takım çalışması](https://en.wikipedia.org/wiki/Red_team)**, ortamınızda hedeflerin peşindeki gerçekçi bir saldırganı simüle eder ve önlemenin yanı sıra tespiti ve yanıtı da sınar.
- **Mor takım çalışması**, saldırganları (kırmızı) ve savunucuları (mavi) iş birliği içinde bir araya getirir; böylece her simüle saldırı tespitleri ve kontrolleri hemen iyileştirir ve bir tatbikat kalıcı yeteneğe dönüşür.
- Tüm bulguları tespit mühendisliğine, düzeltmeye ve eğitime geri besleyin.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| Engelleyen hat kapıları | Bilinen sorunların canlıya çıkmasını durdurur | Sürtünme, yanlış pozitifler takımları sinirlendirir |
| Engellemeyen tarama | Düşük sürtünme, hızlı teslimat | Sorunlar canlıya çıkabilir; düzeltmek disiplin gerektirir |
| Kurum içi SOC | Derin bağlam, tam kontrol | Pahalı, 7/24 kadro zor |
| Yönetilen tespit/yanıt | 7/24 kapsam, uzmanlık elinizin altında | Daha az bağlam, tedarikçi bağımlılığı |
| Otomatik yamalama | Hızlı, pencereleri çabuk kapatır | Bozucu değişiklik riski |
| Sık kırmızı takım çalışması | Gerçekçi doğrulama, gerçek boşlukları bulur | Maliyetli, kaynak yoğun |
| Hata ödül programı | Kitlesel keşif, iyi kapsam | Triyaj yükü, ödül maliyeti, gürültü |

Temel gerilim hız ile güvence, kapsam ile maliyet arasındadır. Engelleyen kapılar ve otomatik yamalama güvenceyi en üst düzeye çıkarır ama sürtünme ve risk ekler. Engellemeyen yaklaşımlar daha hızlı ilerler ama takibe bağlıdır. Günün her saati tespit, ölçekte şarttır ama kurum içinde kurması pahalıdır; bu da birçok kurumu hibrit modellere iter. Sürdürülebilir yol, yüksek güvenilirlikli rutini otomatikleştirir, insan dikkatini gerçek muhakemeye saklar ve dengeyi korku yerine ölçülmüş sonuçlarla ayarlamayı sürdürür.

## Takımınızla tartışılacak sorular

1. **Önem derecesine göre düzeltme SLA'larınız nedir ve bunları gerçekte ne uygulatır?** Sürekli akan zafiyetler, her manşette yeni bir panik değil, sistematik ve önceliklendirilmiş bir süreç gerektirir; önem kademesine göre SLA'lar tempoyu böyle korursunuz. Saatlerinizi belirleyin (örneğin kritik için günler, yüksek için haftalar) ve en az onun kadar önemlisi, uyumu nasıl ölçeceğinizi ve bir süre kaçtığında kimin sorumlu olduğunu karar verin. Yalnızca ham CVSS puanına göre yama yapmak yerine, önceliği gerçek riske göre belirleyin: önem derecesini, gerçek dünyadaki sömürülebilirliği, maruziyeti ve varlık kritikliğini birleştirin. Açık bulgularınızın mevcut birikimini yaşa ve önem derecesine göre sıralı getirin, çünkü pencerelerini aşmış yamalanmamış kritik bulgular önemli olan kanıttır. SLA'nın bir uygulayıcısı ve sahibi yoksa bir dilekten ibarettir ve düzeltmesiz tarama yalnızca denetim borcu ve sahte bir güvenlik hissi biriktirir.

2. **Gece 2'de bir olay başınıza geldiğinde olay komutanı kim ve düzenleyici saat ne kadar hızlı başlar?** Prova edilmiş bir süreç herhangi bir araçtan daha değerlidir; bu yüzden kriz öncesinde yazılı adlandırılmış roller (olay komutanı, iletişim sorumlusu, araştırmacılar), tanımlı önem düzeyleri ve eskalasyon yolları gerekir. Düzenleyici saatler çoğu zaman 72 saat ya da daha az sürer ve keşifte başlar; bu yüzden müşterilere, düzenleyicilere ve kamuoyuna kimin bildireceğini önceden belirleyin ve hukuk ile halkla ilişkilerin işin içinde olduğunu doğrulayın. Belgelenmiş bir gözetim zinciriyle adli kanıtı korumak, ele geçirilmiş bir sunucu yeniden kurulmadan önce yapılmalıdır; aksi halde olanı anlama ya da kanıtlama yeteneğini kaybedersiniz. Son masa başı tatbikatınızın tarihini getirin; çok eskiyse ya da hiç yapılmadıysa planınız denenmemiştir. Kamu takımları için yasal bildirim süreleri bunu zorunlu kılar; bu yüzden yalnızca teknik yanıtı değil, bildirim yolunu da prova edin.

3. **Hangi rutin yanıt eylemlerini SOAR'un insan müdahalesi olmadan yapmasına izin vereceksiniz?** Otomasyon, yalın bir takımın geniş bir yapıyı kapsamasını sağlayan bir kuvvet çarpanıdır ve önemli metrik, otomatik oyun kitaplarının saatlerden dakikalara indirebildiği ortalama yanıt süresidir. Hangi yüksek güvenilirlikli eylemlere (bir sunucuyu izole etmek, bir kimlik bilgisini iptal etmek, bir vaka açmak) kendiliğinden çalışacak kadar güvendiğinizi ve hangilerinin önce insan muhakemesi gerektirdiğini belirleyin. Risk, bir yanlış pozitifin yıkıcı bir eylemi tetiklemesidir; bu yüzden otomasyonu tespit kalitesine bağlayın ve acımasızca ayarlayın, çünkü boşuna alarm veren bir sistem kapatılır. Mevcut uyarı hacminizi ve yanlış pozitif oranınızı getirin; bu sayılar bugün hangi oyun kitaplarını otomatikleştirmenin güvenli olduğunu söyler. Her yanıt adımı bir insanı bekliyorsa ölçekte yetişemezsiniz ve ihlal maliyetini belirleyen bekleme süresi yüksek kalır.

4. **Hangi hat bulguları sürümü engeller, hangileri yalnızca izlenir ve yanlış pozitif oranını mühendislerin hâlâ kapıya güvenecek kadar düşük tutmaktan kim sorumlu?** Boşuna alarm veren bir tarayıcı görmezden gelinir ve mühendisler bir kapıya olan güvenlerini kaybettiklerinde onu kaldırmak için kulis yaparlar; bu yüzden DevSecOps'un değeri ham kapsamda değil sinyal kalitesindedir. Gerilim gerçektir: çok az şeyi engellerseniz zafiyetli kod canlıya çıkar; çok fazlasını engellerseniz sürtünme ekler, teslimatı yavaşlatır ve iyi niyeti tüketirsiniz. Her tarayıcının (SAST, DAST, SCA, IaC ve gizli bilgi taraması) gerçek ve yanlış pozitif oranlarını, takımların bir kapıyı ne sıklıkla geçersiz kıldığını ya da bastırdığını ve yalnızca izleyip düzeltmediğiniz bulguların yaşını getirin. Yüzlerce hat işleten bir kurumsal ya da kamu kurumunda engelle-ya-da-izle politikasını merkezi olarak belirleyin ve veriyle ayarlayın; çünkü takımdan takıma keyfi biçimde farklılaşan kapılar hem denetim boşlukları hem de güvenliğin kaprisli olduğu hissini yaratır.

5. **Tespitlerinizin gerçek bir saldırganın kullanacağı teknikleri hâlâ kapsadığından ne kadar eminsiniz ve bunlara test edilmiş, sürümlenmiş kod olarak kim sahip?** Ortamınız ve saldırganlarınız evrildikçe tespitler sessizce çürür; bu yüzden geçen yıl kapsamlı görünen bir kural kümesi, bir olay boşluğu nihayet ortaya çıkarmadan çok önce kapsamını kaybedebilir. Tespitlere kod gibi davranmak (sürüm kontrollü, test edilmiş ve MITRE ATT&CK gibi bir çerçeveyle eşlenmiş), bir mühendislik pratiğini bayat uyarı yığınından ayıran şeydir; yine de canlı triyajla aynı kıt analist zamanı için rekabet eder. Mevcut ATT&CK kapsam haritanızı, en önemli tespitlerinizin ölçülmüş gerçek ve yanlış pozitif oranını ve son mor takım tatbikatınızın sonuçlarını getirin; çünkü iş birliğine dayalı kırmızı-mavi test, hangi tespitlerin gerçekten tetiklendiğini kanıtlamanın en hızlı yoludur. Bir çerçevenin zorunlu olabileceği kurumsal ve kamu ortamlarında her tespiti adlandırılmış bir sahibe ve bir gözden geçirme ritmine bağlayın, çünkü kimsenin bakmadığı kapsamı kaybettiğinizi ancak ihlalden sonra keşfedersiniz.

6. **Tespit ve yanıtı kurum içinde mi kuruyorsunuz, yönetilen tespit ve yanıt mı satın alıyorsunuz, yoksa ikisini mi harmanlıyorsunuz ve gerçek günün her saati kapsamın maliyetini hesapladınız mı?** Bekleme süresi ihlal maliyetini belirler; bu yüzden kapsanmayan saatler (geceler, hafta sonları, tatiller) tespit edilmemiş bir sızıntının en çok zarar verdiği zamandır, ama kurum içinde 7/24 bir güvenlik operasyon merkezi kadrolamak pahalıdır ve sürdürülmesi zordur. Ödünleşim, bağlam ve kontrol ile maliyet ve kapsama ulaşma hızı arasındadır: kurum içi takım yapınızı derinlemesine tanır ama kurması yavaş ve pahalıdır; yönetilen sağlayıcı günün her saati anında uzmanlık verir ama bağlam daha incedir ve tedarikçi bağımlılığı doğar. Mevcut kapsam saatlerinizi, mesai dışı ortalama tespit ve yanıt sürenizi, uyarı hacminizi ve kendi işlettiğiniz bir merkezin gerektirdiği analistleri işe alıp elde tutabileceğinize dair dürüst bir değerlendirmeyi getirin. Kamu ve düzenlemeye tabi kurumlar için sağlayıcının karşılaması gereken veri yerleşimini, personel güvenlik izni gereksinimlerini ve yasal bildirim yükümlülüklerini tartın ve sözleşmenin hukuki süreçlerin talep ettiği adli titizliği ve gözetim zincirini koruduğunu doğrulayın.

## Sektör merceği

**Girişim.** Önce hız ve hayatta kalma gelir; bu yüzden operasyon kadrolamak yerine güvenliği zaten çalıştırdığınız araçların yan ürünü olarak edinin. Ücretsiz tarayıcıları CI'ye bağlayarak commit anında gizli bilgi sızıntılarını ve bilinen zafiyetli bağımlılıkları engelleyin, günlükleri az sayıda yüksek değerli uyarısı olan düşük maliyetli yönetilen bir hizmete iletin ve ihtiyaç duymadan önce tek sayfalık bir olay planı yazın (kimi aramalı, kimlik bilgileri nasıl döndürülür, yeniden kurmadan önce anlık görüntü alın). En kıt kaynağınız mühendislik dikkatidir; bu yüzden rutini otomatikleştirin ve ayakta tutamayacağınız bir güvenlik operasyon merkezi kurmaya direnin.

**Küçük işletme.** Özel bir güvenlik uzmanı ve sıkı bir bütçeniz yoksa yönetilen tespit ve yanıta ve platformlarınıza zaten yerleşik güvenlik özelliklerine yaslanın. Yamalamayı ve varlık envanterini en yüksek kaldıraçlı alışkanlıklar sayın: ne çalıştırdığınızı bilin, güncel tutun ve önem derecesine göre basit bir düzeltme süresi uygulayın. Günün her saati izlemeyi, koordineli açıklama bildirimini ve adli yakalamayı sizin için üstlenen tedarikçileri tercih edin ve dışarıya veremeyeceğiniz tek şeyi prova edin: olayı kimin ilan ettiği ve müşterilerle kimin konuştuğu.

**Kurumsal.** Zorluk birçok takım ve yüzlerce hat arasında tutarlılıktır: paylaşılan bir engelle-ya-da-izle kapı politikası, kurum genelinde uygulanan düzeltme SLA'ları, ölçülmüş tespitleri olan bir SIEM ve SOAR platformu ve her tatbikatı yeni kapsama çeviren mor takım çalışması. Güvenlik operasyonlarını ortalama tespit ve yanıt süreleri, SLA uyumu ve tespit hassasiyeti panoları olan bir portföy olarak yönetin ve kurum içi derinliğin yönetilen ölçeği nerede yendiğine bilinçli karar verin. Triyaj ve ayarlamanın insan gözetimi maliyetini açıkça bütçeleyin, çünkü otomasyon emeği ortadan kaldırmaz, yer değiştirir.

**Kamu.** Tedarik kuralları, şeffaflık ve kamusal hesap verebilirlik her seçimi şekillendirir. Yasal olay bildirim süreleri ve koordineli zafiyet açıklaması seçenek değil yükümlülüktür; bu yüzden ulusal makama bildirim yolunu teknik yanıt kadar özenle prova edin ve adli kanıtı hukuki incelemeye dayanabilecek bir gözetim zinciri altında koruyun. Tespit mantığını ve veriyi taşınabilir tutan sözleşmeleri tercih edin, her yönetilen sağlayıcının yerleşim ve güvenlik izni gereksinimlerini karşılamasını talep edin ve kırmızı takım değerlendirmelerinin ve sürekli taramanın, kamunun güvenebileceği bir yetkilendirme sürecini beslemesini bekleyin.

## Örnekler

**Girişim.** Güvenlik operasyon merkezi olmayan bir girişim, ücretsiz tarayıcıları CI hattına bağlar; gizli bilgi sızıntıları ve bilinen zafiyetli bağımlılıklar commit anında yakalanır, iki mühendis gürültüde boğulmasın diye yalnızca yüksek güvenilirlikli bulgularda engellenir. İhtiyaç duymadan önce tek sayfalık bir olay planı yazarlar: kimi aramalı, kimlik bilgileri nasıl döndürülür ve ne olduğunu öğrenebilmek için ele geçirilmiş bir sunucuyu yeniden kurmadan önce anlık görüntüsünü almak. Günlükleri düşük maliyetli yönetilen bir hizmete iletir ve gerçekten bir ihlale işaret edecek olaylara birkaç uyarı koyarlar; böylece bir sorun tesadüfen fark edilmenin alacağı aylar yerine saatler içinde ortaya çıkar.

**Kurumsal.** Bir hizmet olarak yazılım şirketi her hatta SAST, SCA, IaC ve gizli bilgi taraması çalıştırır, yalnızca yüksek önem derecesindeki ve yüksek güvenilirlikteki bulgularda engeller, gerisini düzeltme SLA'larıyla bir panoda izler. Bir SIEM, yüksek güvenilirlikli uyarılarda sunucuları otomatik izole eden ve kimlik bilgilerini iptal eden bir SOAR platformunu besler ve ortalama yanıt süresini saatlerden dakikalara indirir. MITRE ATT&CK teknikleri üzerinde üç ayda bir yapılan mor takım tatbikatları doğrudan yeni tespit kuralları üretir ve kapsam boşluklarını istikrarla kapatır.

**Kamu.** Bir federal kurum, yasal sürelerde bir ulusal siber makama zorunlu olay bildirimi yapan bir güvenlik operasyon merkezi (SOC) işletir. Politikanın gerektirdiği biçimde herkese açık bir bildirim kanalıyla koordineli zafiyet açıklaması programı yürütür ve adli kanıtı hukuki süreçlere uygun sıkı gözetim zinciri prosedürleri altında korur. Yıllık kırmızı takım değerlendirmeleri ve sürekli zafiyet taraması, kurumun süregiden yetkilendirmesini ve riske dayalı düzeltme SLA'larını besler.

## İş gerekçesi: motivasyonlar, YG ve TSM

Güvenlik operasyonlarının gerekçesinin neredeyse tamamı bekleme süresine dayanır: bir saldırgan ne kadar uzun süre fark edilmezse ihlal o kadar pahalıya mal olur. Çalışmalar tutarlı biçimde hızla sınırlandırılan olayların aylarca süren olaylardan dramatik biçimde daha ucuz olduğunu gösterir. Toplam sahip olma maliyeti (TSM) araçları (SIEM, SOAR, tarayıcılar), tespit ve yanıt için kadroyu ya da yönetilen hizmetleri ve olay süreçlerini kurma ve prova etme zamanını içerir. Karşısında yatırım yapmamanın maliyeti durur: geç keşfedilen, sistemlere yayılan, düzenleyici cezalar, zorunlu bildirimler, davalar ve itibar kaybı getiren bir ihlal; hepsi prova edilmemiş bir yanıtın kaosuyla daha da kötüleşir.

Yatırım getirisi (YG), daha hızlı tespit ve yanıttan, yalın bir takımın geniş bir yapıyı kapsamasını sağlayan otomasyondan ve her olaydan ve tatbikattan geri beslenen önleme iyileştirmelerinden gelir. Özellikle DevSecOps, sorunları pahalı ve herkese açık oldukları üretimde değil, ucuz oldukları hatta yakalayarak karşılığını verir. Liderliğe gerekçeyi sunarken mevcut ortalama tespit ve yanıt sürelerinize sayı koyun, bunların bekleme süresine ve maliyete nasıl bağlandığını gösterin ve otomasyonu, yapıyla orantılı olarak kadro büyütmeyi önleyen bir kuvvet çarpanı olarak çerçeveleyin. Kamu için yasal bildirim ve açıklama yükümlülüklerinin olgun operasyonları zorunlu kıldığını vurgulayın.

## Anti-kalıplar ve tuzaklar

- **Uyarı yorgunluğu.** O kadar çok uyarı ki analistler dikkati bırakır ve gerçek olanı kaçırır.
- **Düzeltmesiz tarama.** Kimsenin düzeltmediği bulgular üretmek; sahte bir güvenlik hissi ve denetim borcu yaratır.
- **Olay planı yok.** Kriz sırasında doğaçlama yapmak, kritik dakikaları boşa harcamak ve kanıtı kötü yönetmek.
- **Kanıtı yok etmek.** Ele geçirilmiş bir sunucuyu adli kanıtı yakalamadan yeniden kurmak; olanı anlama ya da kanıtlama yeteneğini kaybetmek.
- **İncelemelerde suçlama kültürü.** Müdahale edenleri cezalandırarak bir sonraki olayın gizlenmesine ya da savunmacı biçimde ele alınmasına yol açmak.
- **Yalnızca uyum için sızma testi.** Bir denetçiyi tatmin etmek için yapılan tek bir yıllık test; bulgular gelecek yıla kadar görmezden gelinir.
- **Yüksek yanlış pozitifli engelleyen kapılar.** Güveni, mühendislerin kapıların tamamen kaldırılmasını talep etmesine kadar aşındırmak.
- **Kur ve unut tespitler.** Ortam ve saldırganlar evrildikçe çürüyen ve sessizce kapsamını kaybeden kurallar.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Güvenlik operasyonları gelişigüzel ve tepkiseldir. Güvenlik testleri elle yapılır ve seyrektir; merkezi günlük tutma ya da SIEM yoktur. Olay planı yoktur, bu yüzden yanıt anın içinde doğaçlanır. Yamalama yalnızca bir manşet zorladığında yapılır ve savunmalar hiçbir zaman saldırgan gözüyle test edilmez.

**Düzey 2, Geliştirme.** Temel pratikler ortaya çıkar ama takımlar arasında tutarsızdır. Bazı hatlar tarayıcı çalıştırırken bazıları hiçbirini çalıştırmaz ve merkezi günlük tutma yer yer vardır. Temel bir olay planı belgelenmiştir ama nadiren prova edilir, yamalama gevşek zaman çizelgelerini izler ve yıllık bir sızma testi pek bir şey değiştirmeden uyumu sağlar. Kapsam ve titizlik hangi takıma sorduğunuza bağlıdır.

**Düzey 3, Standartlaştırma.** Pratikler belgelenmiş ve kurum genelinde uygulanır. Riske dayalı kapılarla tam DevSecOps taraması tutarlı biçimde uygulanır, bir SIEM olayları ilişkilendirir ve ilk SOAR oyun kitapları çalışır. Olay müdahalesi masa başı tatbikatlar ve suçlamasız incelemelerle prova edilir, önem derecesine göre düzeltme SLA'ları adlandırılmış sahiplerle uygulanır ve koordineli zafiyet açıklaması ile düzenli kırmızı takım çalışması istisna değil norm olur.

**Düzey 4, Yönetme.** Operasyonlar taban çizgilerine karşı ölçülür ve kontrol edilir. Ortalama tespit ve yanıt süresi, önem kademesine göre SLA uyumu, tarama kapsamı, tespitlerin gerçek ve yanlış pozitif oranları ve bekleme süresi panolarda izlenir ve belirli bir ritimle gözden geçirilir. Tespitler MITRE ATT&CK ile eşlenmiş ölçülmüş hassasiyet ve duyarlılık taşır, otomasyon kararları umuda değil yanlış pozitif verisine dayandırılır ve taban çizgisini aşan bir metrik fark edilmeden geçmek yerine tanımlı bir yanıtı tetikler.

**Düzey 5, Orkestrasyon.** Güvenlik operasyonları sürekli iyileştirilir, kurum genelinde entegredir ve uyum sağlar. Tespit mühendisliği, mor takım çalışması, düzeltme ve olay incelemesi, yeni saldırgan teknikleri ortaya çıktıkça onlara uyum sağlayan tek bir döngüyü besler. Otomatik oyun kitapları tüm yapıda rutini üstlenir; insanlar muhakemeye odaklanır, güvenlik teslimat ve riskle birlikte planlanır ve her olay ve tatbikat çekirdek metrikler düşmeye devam ederken sistemi ölçülebilir biçimde sağlamlaştırır.

## Tartışma fikirleri

1. Hangi hat bulguları sürümü engellemeli, hangileri yalnızca izlenmeli?
2. Kurum içi SOC mu kurmalı, yönetilen tespit ve yanıt mı kullanmalı, yoksa ikisini mi harmanlamalı ve neden?
3. Ortamınız evrildikçe tespit kurallarının çürümesini nasıl önlersiniz?
4. Bozucu değişiklik riski göz önüne alındığında yamalama ne kadar agresif otomatikleştirilmeli?
5. Sizin kültürünüzde gerçekten suçlamasız bir olay sonrası inceleme nasıl görünür?
6. Kırmızı ve mor takım çalışmalarının savunmalarınızı gerçekten iyileştirip iyileştirmediğini nasıl ölçersiniz?

## Önemli çıkarımlar

- Önleme eninde sonunda başarısız olur; operasyonlar hızla tespit etmek ve yanıt vermek için vardır.
- SAST, DAST, SCA, IaC ve gizli bilgi taramasını riske dayalı kapılarla hatta yerleştirin.
- Yamalamayı gerçek sömürülebilirliğe ve varlık kritikliğine göre, uygulanan SLA'lar altında önceliklendirin.
- Olay müdahalesini prova edin, adli kanıtı koruyun ve ihlal iletişimini önceden planlayın.
- İlişkilendirmek ve otomatikleştirmek için SIEM ve SOAR kullanın; tespitlere mühendislikle üretilmiş, test edilmiş kod olarak davranın.
- Savunmaları sızma testleri, kırmızı takım çalışması ve iş birliğine dayalı mor takım çalışmasıyla doğrulayın.
- Bekleme süresi ihlal maliyetini belirler; bu yüzden ortalama tespit ve yanıt süresi önemli metriklerdir.

## Kaynaklar ve ileri okuma

- National Institute of Standards and Technology, *SP 800-61: Computer Security Incident Handling Guide*
- National Institute of Standards and Technology, *SP 800-40: Guide to Enterprise Patch Management*
- MITRE, *ATT&CK Framework*
- Anton Chuvakin and others, *Logging and Log Management* / SIEM literature
- Jim Bird, *DevOpsSec: Securing Software through Continuous Delivery*
- Richard Bejtlich, *The Practice of Network Security Monitoring*
- FIRST, *Coordinated Vulnerability Disclosure* guidance and *CVSS* specification
