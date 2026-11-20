# 8.6 Sürüm yönetimi ve aşamalı teslimat

## Genel bakış ve motivasyon

Modern sürüm yönetiminin en yararlı fikri aynı zamanda en basitidir: kod teslim etmek ile bir özelliği açığa çıkarmak iki ayrı olaydır ve birini diğeri olmadan yapabilmelisiniz. Bölüm 8.1 (CI/CD ve teslimat) değişikliğinizin bir kez derlenmesini, test edilmesini ve değişmez bir yapıt olarak terfi ettirilmesini sağlar. Bu bölüm sonrasında olanlarla ilgilidir: dağıtılmış o kodu gerçek kullanıcılar için canlı bir deneyime nasıl, kademeli, güvenli ve geri dönüşü hızlı biçimde dönüştürürsünüz. **Dağıtım**, kodu sunuculara kurmak demektir. **Sürüm**, kullanıcıların bir yeteneğe erişmesine izin vermek demektir. İkisini ayırdığınızda dağıtım rutin ve sıkıcı hale gelir, sürüm ise kontrollü, geri alınabilir bir karara dönüşür.

Büyük takımlar için bu ayrım, teslim etmenin duygusal sıcaklığını değiştirir. Onlarca hizmet ve yüzlerce mühendis her gün üretimi değiştirirken, "dağıtım sürüme eşittir" modeli, kullanıcıya dönük her değişikliği riskli ve hepsi bir anda gerçekleşen bir olay yapar. Ayrıştırma, bitmemiş işi bir anahtarın arkasında birleştirmenize, bir özelliği trafiğin yüzde birine açmanıza, sayıları izlemenize ve derlemeye dokunmadan genişletmenize ya da geri çekilmenize izin verir. **Aşamalı teslimat** bunun şemsiye terimidir: otomatik denetimler devam edip etmeyeceğine karar verirken bir değişikliği genişleyen bir kitleye sürmek.

Kurumsal ve kamu ortamları koordinasyon ve kanıt ekler. Bir ödeme platformu, bir şema üzerinde anlaşması gereken birçok hizmet boyunca sürüm çıkarır. Bir kamu kurumu işletme yetkisi ve resmi değişiklik kontrolü altında çalışır ve denetçiler tam olarak kimin neye ve ne zaman maruz kaldığına dair kanıt ister. İyi yapıldığında aşamalı teslimat hem hızlı hareket etme isteğini hem de kontrolü kanıtlama yükümlülüğünü karşılar, çünkü etki alanını sınırlayan aynı mekanizma, sürümün denetlenebilir bir kaydını da üretir.

## Temel ilkeler

- **Dağıtım sürüm değildir.** Kodu karanlıkta teslim edin, sonra bilinçli olarak açın.
- **Önce küçük etki alanı.** Bir değişikliği herkese açmadan önce birkaç kişiye açın.
- **Her sürümün bir geri vitesi vardır.** Saniyeler içinde geri alamıyorsanız sürümü tasarlamayı bitirmemişsiniz demektir.
- **Terfiyi sinyaller yönetsin.** Bir kademeli açılımın ilerleyip ilerlemeyeceğine takvimler ya da iyimserlik değil, sağlık ölçütleri ve hata bütçeleri karar verir.
- **Bir bayrak, kaldırılana kadar bir yüktür.** Her anahtar, sürdürmeniz ve sonunda silmeniz gereken koddur.
- **Veritabanı değişikliğini iki yönde de ayakta tutun.** Açılımlar ve geri almalar aynı şemaya karşı güvenli olmalıdır.
- **Onaylar kaydetmeli, engellememeli.** Denetim kanıtı işlem hattının yan ürünüdür, haftalık bir toplantı değil.

## Öneriler

### Dağıtımı sürümden özellik bayraklarıyla ayırın

[Özellik anahtarı](https://en.wikipedia.org/wiki/Feature_toggle) ya da özellik bayrağı, yeniden dağıtım yapmadan bir kod yolunun etkin olup olmadığına karar veren bir çalışma zamanı anahtarıdır. Bayrakları tiplenmiş bir sözcük dağarcığı olarak ele alın, çünkü ömürleri farklıdır. Bir **sürüm bayrağı** devam eden işi gizler ve günlerden haftalara kadar yaşar. Bir **operasyonel bayrak** (öldürme anahtarı) yük altında bir alt sistemi devre dışı bırakmanıza izin verir ve süresiz yaşayabilir. Bir **deney bayrağı** kontrollü bir test için trafiği böler ve deneyin süresi kadar yaşar. Bir **izin bayrağı** bir yeteneği plana ya da role göre kapılar ve fiilen kalıcıdır. Her bayrağa bir sahip, bir tip, bir varsayılan ve beklenen bir kaldırma tarihi verin. Varsayılan güvenli olan olmalıdır; böylece bir bayrak hizmeti kesintisi, sınanmamış yollara açık değil, bilinen iyi davranışa kapalı başarısız olur.

### Hizmet katmanı başına bir aşamalı teslimat kalıbı seçin

Bölüm 8.1'in dağıtım stratejileri için savunduğu gibi, açılım mekanizmasını etki alanına uydurun. Bir [kanarya sürümü](https://en.wikipedia.org/wiki/Feature_toggle#Canary_release) trafiğin küçük bir dilimini yeni sürüme yönlendirir ve yalnızca sağlık korunursa genişler. Bir [mavi-yeşil dağıtım](https://en.wikipedia.org/wiki/Blue-green_deployment) iki üretim ortamı tutar ve anında geçiş ve anında geri alma için trafiği aralarında kaydırır. **Yuvarlanan dağıtım** örnekleri gruplar halinde değiştirir. **Halka tabanlı dağıtım** adlandırılmış kitleler boyunca genişler: önce iç kullanıcılar, sonra bir beta kohortu, sonra küçük bir bölge, sonra herkes. Halkalar büyük kurumlar için en yararlı çerçevedir, çünkü her adımda kimin maruz kaldığını adlandırır; bu da hem bir denetçinin hem bir olay müdahalecisinin tam olarak bilmek istediği şeydir. Konteyner platformları ve orkestrasyon (bölüm 8.3) bu kalıpları çalıştırmayı ucuz kılan trafik şekillendirme ilkellerini sağlar.

### Açılımları sağlık denetimlerine ve otomatik geri almaya bağlayın

Nesnel sağlık ölçütlerini olay sırasında değil, sürümden önce tanımlayın. Otomatik analiz, kanaryayı taban çizgisiyle hata oranı, gecikme ve doygunluk üzerinden karşılaştırır ve bir insanın fark etmesini beklemeden ya terfi ettirir ya da geri alır. Terfiyi, site güvenilirlik mühendisliğinden (bölüm 9.1) gelen [hizmet düzeyi hedefinize](https://en.wikipedia.org/wiki/Service-level_objective) ve hata bütçenize bağlayın: bütçe sağlıklıyken özgürce sürüm çıkarırsınız, bütçe tükendiğinde işlem hattı hizmet dengelenene kadar ilerlemeyi reddeder. Otomatik geri alma en çok önemlidir, çünkü küçük bir gerilemeyi büyük bir kesintiye çeviren tereddüdü ortadan kaldırır. Hızlı geri alma aynı zamanda en ucuz olay denetiminizdir: saniyeler süren bir geri alma, olay süreciniz (bölüm 9.3) tam olarak devreye girmeden önce etki alanını küçültür. Bu yolla iyileştirdiğiniz değişiklik başarısızlık oranı ve kurtarma süresi, teslimat işlem hattınızın izlediği akış ve kararlılık sinyalleriyle aynıdır (bölüm 11.2).

### Riski azaltmak için karanlık lansmanları ve gölge trafiği kullanın

Bazı değişiklikler, gerçek kullanıcılarla ilk kez tam maruziyette karşılaşmak için fazla önemlidir. **Karanlık lansman**, bir özelliği kapalı olarak teslim eder, sonra kimse görmeden önce onu dahili olarak ya da üretimin bir kısmına karşı çalıştırır. **Gölge trafik** canlı istekleri yeni kod yoluna kopyalar ve yanıtları atar; böylece sıfır kullanıcı etkisiyle gerçek yükü ve doğruluğu ölçersiniz. Bu teknikler, hiçbir hazırlık ortamının sadakatle yeniden üretemediği gerçek trafik altında bir yeniden yazımı ya da yeni bir bağımlılığı doğrulamanıza izin verir. Onları kanaryalar için kullandığınız aynı sağlık analiziyle eşleştirin.

### Kontrollü deneyleri aynı bayrak sistemi üzerinden yürütün

Deney bayrağı, sürüm mühendisliğinin ürün öğrenmesiyle buluştuğu yerdir. Bir [A/B testi](https://en.wikipedia.org/wiki/A/B_testing) bölmesi, karşılaştırılabilir kohortlara varyantlar sunar ve seçilmiş bir sonucu ölçer; bu, bölüm 7.4'ün ürün analitiği pratiğini besler. Güvenlik açılımları ve deneyler için tek bir bayrak ve hedefleme sistemini yeniden kullanın; böylece kimin hangi kovada olduğu konusunda anlaşamayan iki paralel anahtar yığını yerine tek bir denetim izine ve tek bir öldürme anahtarına sahip olursunuz.

### Veritabanını genişlet ve daralt ile geriye uyumlu tutun

Açılımlar ve geri almalar ancak şema hem eski hem yeni kodu aynı anda tolere ederse güvenli kalır; bu, her kademeli açılım sırasında kaçınılmazdır. **Genişlet ve daralt** (paralel değişiklik) kalıbını kullanın: önce geriye uyumlu bir geçişte yeni sütunlar ya da tablolar ekleyerek *genişletin*, sonra hem eski hem yeni biçime yazan kodu dağıtın, sonra geri doldurun, sonra okumaları taşıyın ve ancak çok daha sonra, çalışan hiçbir kod eski biçime bağlı kalmadığında eski biçimi kaldırarak *daraltın*. Yıkıcı bir geçişi, onu gerektiren dağıtımla asla birleştirmeyin. Bu disiplin, veritabanı çoktan ilerlemişken kodu geri almanıza olanak tanıyan şeydir ve doğrudan, karma sürüm penceresini kapsaması gereken test stratejinize (bölüm 2.4) bağlanır.

### Değişiklik yönetimini engellemek yerine kaydeden hale getirin

Değişiklik sınıflarını önceden onaylayarak denetimi akışla uzlaştırın. İşlem hattından otomatik akan, kimin onayladığını, hangi testlerin çalıştığını, hangi yapıtın dağıtıldığını ve her halkada hangi kitlelerin maruz kaldığını kaydeden standart, düşük riskli değişiklik tipleri tanımlayın. İnsan değişiklik danışma incelemesini gerçekten yüksek riskli değişikliklere saklayın. Her rutin dağıtımı inceleyen geleneksel bir [değişiklik kontrolü](https://en.wikipedia.org/wiki/Change_control) kurulu darboğaza dönüşür ve takımları amacının tersine, daha büyük, daha riskli gruplara iter. Kamuda, açılım araçları kontrol çerçevesinin gerektirdiği kanıtı ürettiğinde işletme yetkisi ve resmi değişiklik kontrolü aşamalı teslimatla bir arada var olabilir; böylece halka tabanlı kayıt denetim yapıtı olur.

## Ödünleşimler: artılar ve eksiler

| Kalıp | Artılar | Eksiler | En uygun durum |
|---|---|---|---|
| Kanarya | Veri güdümlü, küçük etki alanı | İyi ölçütler ve trafik hacmi gerektirir | Büyük kullanıcıya dönük hizmetler |
| Mavi-yeşil | Anında geçiş ve geri alma | Geçiş sırasında ortam maliyetini ikiye katlar | Hızlı geri dönüş gereken kritik hizmetler |
| Yuvarlanan | Ucuz, basit, ek ortam yok | Yavaş geri alma, karışık sürümler canlı | Durumsuz iç hizmetler |
| Halka tabanlı | Adlandırılmış kitleler, net denetim izi | Daha yavaş tam açılım; daha fazla koordinasyon | Düzenlemeye tabi ve çok hizmetli varlık alanları |
| Özellik bayrakları | Dağıtımı sürümden ayırır; anında öldürme anahtarı | Bayrak borcu; test matrisi büyür | Tamamlanmamış işi güvenle teslim eden takımlar |
| Sürüm trenleri | Öngörülebilir ritim, kolay koordinasyon | Birçok değişikliği bağlar; trenin gelmesini bekler | Bir sürümü paylaşan çok sayıda takım |
| İsteğe bağlı sürüm | Küçük gruplar, hızlı geri bildirim | Takımlar arası koordinasyon daha zor | Yüksek güvenli sürekli teslimat takımları |

Temel gerilim, koordinasyon ile bağımsızlık arasındadır. **Sürüm trenleri**, birçok takımın değişikliklerini sabit bir takvime toplar; bunu akıl yürütmek kolaydır ama bitmiş bir değişikliği beklemeye zorlar ve ilgisiz işleri tek bir olaya bağlar. **İsteğe bağlı sürüm**, her takımın hazır olduğunda teslim etmesine izin verir; bu daha hızlıdır ama hizmetlerin bağımsız dağıtılabilir ve geriye uyumlu kalmasını gerektirir. Çözüm genellikle yapıt ve şema düzeyinde ayrıştırmaktır, böylece takımlar isteğe bağlı sürüm çıkarabilir; sonra bir hizmetler arası özelliğin gerçekten açıldığı *kullanıcıya görünen* anı koordine etmek için bayrakları ve halkaları kullanırsınız. Böylece teknik sürüm ve ürün lansmanı ayrı kararlar olur ve hiçbiri diğerini engellemez.

## Takımınızla tartışılacak sorular

1. **Bir sürüm sabaha karşı 2'de ters gittiğinde geri almak kaç saniye sürüyor ve tetiği kim ya da ne çekiyor?** Dürüst cevap, dağıtımı sürümden gerçekten ayırıp ayırmadığınızı ya da yalnızca bağlaşık bir sürecin üstüne bayrak ekleyip eklemediğinizi ortaya çıkarır. Yeniden derleme, geri alınacak bir veritabanı geçişi ya da karar verecek çağrılmış bir insan gerektiren bir geri alma, geri alma değil, ikinci bir olaydır. En önemli üç hizmetiniz için gerçek mekanizmayı getirin: maruziyeti tersine çeviren bayrak ya da trafik kaydırma, onu otomatik tetikleyen sağlık sinyali ve geri almayı güvenli kılan şema garantisi. Büyük bir varlık alanı için bu, gerçek etki alanınızı belirler, çünkü hızlı otomatik geri alma bir gerilemenin kesintiye dönüşmesini önleyen şeydir. Cevap saniyelerle değil toplantılarla ölçülüyorsa, düzeltilecek ilk şey budur.

2. **Bayrakları emekliye ayırma politikanız nedir ve şu anda ne kadar bayrak borcu taşıyorsunuz?** Her özellik bayrağı, akıl yürütmeniz ve test etmeniz gereken durum sayısını katlayan koddaki bir çatallanmadır ve amacından uzun yaşayan bir bayrak saf bir yüktür. Kuralı şimdi belirleyin: her sürüm bayrağı bir sahip ve bir son kullanma tarihi alır, eskimiş bayraklar bir panoda görünür ve onları kaldırmak "bir gün temizleriz" değil planlı iştir. Canlı bayrakların sayısını, yaşlarını ve kaçının amaçlanan kaldırma tarihini geçtiğini getirin. Büyük bir kod tabanında denetimsiz bayraklar kimsenin silmeye cesaret edemediği kalıcı koşullu karmaşıklığa dönüşür ve güvenlik mekanizması hata kaynağına çevrilir. Takımın o sayıya hoşgörüsü aslında operasyonel hijyeni ne kadar ciddiye aldığına dair bir ifadedir.

3. **Değişiklik onay süreciniz sürümleri daha güvenli mi yapıyor, yoksa yalnızca daha yavaş mı?** Birçok kurum her dağıtımı inceleyen bir değişiklik danışma kurulu işletir ve rahatsız edici soru, bu kurulun hiç kötü bir değişikliği gerçekten durdurup durdurmadığı, yoksa yalnızca gecikme ekleyip eklemediğidir. Veri getirin: ortanca onay gecikmesi, kurulca incelenen ve önceden onaylanan değişiklikler için değişiklik başarısızlık oranı ve incelemenin küçük değişiklikleri ne sıklıkla daha büyük, daha riskli gruplara topladığı. Amaç, insan incelemesini gerçekten yüksek riskli değişikliklere saklamak, standart değişikliklerin ise otomatik kanıt yakalamayla işlem hattından akmasına izin vermektir. Düzenlemeye tabi ve kamu bağlamları için, açılım araçlarının kontrol çerçevesinin ihtiyaç duyduğu denetim kaydını ürettiğini doğrulayın; böylece kontrol, teslimatın önündeki bir kapı değil teslimatın yan ürünü olur. İnceleme başarısızlıkları azaltmadan gecikme ekliyorsa, uyum kostümü giymiş bir tiyatrodur.

4. **Bir makinenin hangi nesnel sağlık sinyalleriyle harekete geçmesine izin vermeye hazırsınız ve her üst düzey hizmetin gerçekten kapılama yapabilecek kadar iyi ölçütleri var mı?** Otomatik kanarya analizi ve hata bütçesi kapılama, yalnızca hata oranı, gecikme ve doygunluk, döngüde insan olmadan bir terfiye ya da geri almaya güvenilecek kadar temiz ölçülüyorsa işler ve birçok takım bir olay sırasında sinyallerinin karar vermek için fazla gürültülü ya da fazla seyrek olduğunu keşfeder. Büyük bir varlık alanı için bu, sürüm hacminizin ne kadarının manuel bakıcılık olmadan güvenle akabileceğini belirler; bu, ölçeklenen bir platform ile her açılımı izleyen bir insana ihtiyaç duyan bir platform arasındaki farktır. En kritik üç hizmetinizin gerçek panolarını getirin: kapıladığınız ölçütler, bir kanaryayı istatistiksel olarak anlamlı kılan trafik hacmi ve otomatik analizinizin yanlış pozitif oranı. Düzenlemeye tabi ve kamu ortamlarında aynı sinyaller denetlenebilir kaydı besler; dolayısıyla zayıf gözlemlenebilirlik hem bir güvenilirlik hem bir uyum boşluğudur ve ölçüt kalitesini fonlamak, varsayılan bir yetenek değil planda adı konmuş bir kalem olmalıdır.

5. **Şema değişiklikleriniz gerçekten bir geri almadan sağ çıkıyor mu ve teslim etmeden önce karma sürüm penceresinin güvenli olduğunu nasıl kanıtlıyorsunuz?** Aşamalı teslimat hızlı bir geri vites vaat eder, ama bir özelliğe bağlı yıkıcı bir geçiş bu vaadi sessizce geçersiz kılar, çünkü kodu geri almak onu çoktan ilerlemiş bir veritabanına bakar halde bırakır. Birçok hizmetin bir şemayı paylaştığı büyük bir kurum için risk birikir: bir takımın daraltma adımı başka bir takımın geri almasını mahsur bırakabilir; bu yüzden genişlet-ve-daralt disiplini yerel bir alışkanlık değil ortak bir standart olmalıdır. Geçiş el kitabınızı ve izlendiğine dair kanıtı getirin: genişletmeyi daraltmadan nasıl ayırdığınız, çift yazma ve geri doldurmanın yük altında test edilip edilmediği ve test paketinizin eski kodu yeni şemaya, yeni kodu eski şemaya karşı nasıl sınadığı. Uzun ömürlü veri taşıyan ve resmi değişiklik kontrolü olan kurumsal ve kamu varlık alanları için, geri döndürülemez bir geçiş yalnızca bir kesinti riski değil, planlı bir bakım penceresinin kurtaramayacağı bir veri bütünlüğü ve denetim açığıdır.

6. **Farklı hızlarda teslim eden takımlara yayılan hizmetler arası bir özellik söz konusu olduğunda, açıldığı anın sahibi kim ve dağıtımlarını bağlamadan nasıl koordine ediyorsunuz?** Dağıtımı sürümden ayırmanın bütün amacı, her takımın yapıtını bağımsız teslim edebilmesi ve tek bir bayrağın kullanıcıya görünen lansmanı kontrol etmesidir; ama bu ancak biri lansman kararının ve hizmet sınırları boyunca bayrak hedeflemesinin sahibiyse geçerlidir. Büyük bir takım için başarısızlık biçimi, kimsenin seçmediği fiili bir sürüm trenidir: tek bir yavaş hizmet diğer her takımı bekletir ya da koordine edilmemiş bir bayrak çevirme yarım bağlanmış bir özelliği açığa çıkarır. Bir sonraki çok hizmetli lansmanınızın bağımlılık haritasını, lansman bayrağının sahibini ve her hizmetin kendi saatinde dağıtım yapmasına izin veren geriye uyumluluk garantilerini getirin. Resmi lansman onayları olan kurumsal ve kamu programlarında, hizmetler arası açılışı kimin imzaladığını ve hangi kanıtı gördüğünü adlandırın; böylece koordineli lansman, en son kimin birleştirdiğinin bir kazası değil, bilinçli, kaydedilmiş bir karar olur.

## Sektör merceği

**Girişim.** Dağıtımı sürümden ayırmak üç mühendisle bile yapmaya değer, ama ucuz tutun. Yeni işi varsayılanı kapalı olan bir sürüm bayrağına sarın, gövdeye teslim edin ve özellikleri müşterilerden önce kendiniz için açın; böylece bitmemiş bir değişiklik asla bir dağıtımı engellemez. Kadrolayamayacağınız ağır kanarya analizi platformlarını atlayın: barındırılan bir bayrak hizmeti ve sert bir öldürme anahtarı güvenliğin çoğunu satın alır ve haftalık bayrak temizliği törenine sahip tek bir kişi borcun hızınızı yutmasını önler.

**Küçük işletme.** Sürüm mühendisi olmadan ve dar bir bütçeyle, bir açılım sistemi inşa etmek yerine mevcut platformunuzun zaten sunduğu aşamalı teslimata yaslanın. Yönetilen barındırma, bir özellik bayrağı SaaS'ı ya da çerçevenizin yerleşik aşamalı açılımı genellikle ihtiyaç duyduğunuz küçük etki alanını kapsar. Geri vitesi doğru yapmanız gereken şey olarak görün: saniyeler içinde kapatabileceğiniz bir değişiklik, ayarlamaya vaktiniz olmayan gelişmiş otomatik analizden çok daha önemlidir.

**Kurumsal.** Sorun, birçok takım ve hizmet arasında tutarlılıktır: sahipleri, tipleri ve son kullanma tarihi olan ortak bir bayrak sözcük dağarcığı, standart halka tabanlı açılım ve her yerde aynı biçimde uygulanan hata bütçesi kapılama; böylece gruplar rakip anahtar yığınları icat etmeyi bırakır. Bayrak borcunu varlık alanı genelinde bir ölçüt olarak yönetin, genişlet-ve-daralt geçişlerini standartlaştırın ki bir takımın şema değişikliği başka bir takımın geri almasını asla mahsur bırakmasın ve denetlenebilir açılım kaydını her hizmetin aynı biçimde yaydığı bir yan ürün yapın. Standart değişiklikleri önceden onaylayın ve insan incelemesini gerçekten yüksek riskli olanlara saklayın; böylece kontrol, kritik yolda bir kurul olmadan ölçeklenir.

**Kamu.** Tedarik kuralları, şeffaflık ve kamusal hesap verebilirlik her sürümü şekillendirir. Açılım araçlarını denetim kanıtının kaynağı yapın; böylece her halka genişlemesi onaylayan yetkiliyi, çalışan testleri, yapıt özetini ve maruz kalan tam nüfusu kaydeder ve bir işletme yetkisi aşamalı teslimatla savaşmak yerine onunla bir arada var olur. Adlandırılmış kitlelerini bir denetçinin ve bir olay müdahalecisinin ikisinin de okuyabildiği mavi-yeşil ya da halka tabanlı kalıpları tercih edin, önemli değişiklikleri hiçbir vatandaş etkilenmeden önce canlı vakalara karşı gölge trafikle doğrulayın ve denetlenebilir kaydı, kontrol çerçevesinin planlı bir toptan geçiş penceresi yerine kabul ettiği yapıt olarak tutun.

## Örnekler

**Girişim.** On kişilik bir SaaS şirketi günde birçok kez gövdeye teslim eder ve her yeni yeteneği varsayılanı kapalı olan bir sürüm bayrağına sarar. Riskli bir yeni faturalama entegrasyonu karanlıkta başlar: bir hafta boyunca ona karşı gölge trafik çalıştırırlar; müşteri etkisi olmadan gerçek istek biçimlerini nasıl işlediğini izlerler, sonra halka halka, kendi hesaplarından ve bir avuç dost beta müşterisinden başlayarak açarlar. Hata oranları yüzde beşlik halkada sıçradığında otomatik bir denetim bayrağı saniyeler içinde kapatır ve Pazartesi günü sakin sakin hata ayıklarlar. Bir mühendis, anahtarlar asla birikmesin diye haftalık bir bayrak temizliği törenine sahiptir.

**Kurumsal.** Küresel bir ödeme şirketi, altı hizmeti ve ortak bir şemayı kapsayan bir değişikliği koordine eder. Her takım yapıtını genişlet ve daralt kullanarak bağımsız ve geriye uyumlu biçimde dağıtır; böylece yeni sütunlar var olur ve özelliği herhangi bir kullanıcı görmeden çok önce çift yazılır. Kullanıcıya görünen lansman, hata bütçesi sağlığına bağlı halkalardan açılan tek bir deney bayrağıdır: önce iç, sonra küçük bir ülke, sonra genişleyen bir yüzde; her adımda otomatik kanarya analizi terfi ettirir ya da geri alır. Bir bayrak yönetişim hizmeti varlık alanı boyunca sahipleri, tipleri ve son kullanma tarihini uygulatır ve önceden onaylı standart değişiklikler bir kurul olmadan akar; yalnızca şema daraltma adımı insan incelemesi alır. Her halka geçişi günlüğe alınır, dolayısıyla denetim izi kendini yazar.

**Kamu.** Ulusal bir yardım kurumu işletme yetkisi ve resmi değişiklik kontrolü altında çalışır. Aşamalı teslimatı bir uyum riski olarak görmek yerine, açılım araçlarını denetim kanıtının kaynağı yapar: her halka genişlemesi onaylayan yetkiliyi, çalışan testleri, yapıt özetini ve maruz kalan tam nüfusu kaydeder. Yeni bir uygunluk hesaplaması karanlıkta başlar ve canlı vakalara karşı gölge trafikle doğrulanır, sonra anında geri alma için mavi-yeşil geçişle bir bayrağın arkasında bölge bölge açılır. Standart değişiklikler önceden sınıflandırılır; böylece rutin iş bir kurulun arkasında sıra beklemez, yüksek riskli politika değişiklikleri ise yine resmi inceleme alır. Denetlenebilir açılım kaydı, kontrol çerçevesini eski üç aylık toptan sürümün hiç yapamadığı kadar tam karşılar.

## İş gerekçesi: motivasyonlar, YG ve TSM

Aşamalı teslimatın getirisine, önlenen olaylar ve küçülen önem dereceleri hâkimdir. Kullanıcıların yüzde birine ulaşan ve otomatik geri dönen bir değişiklik yuvarlama hatasına mal olur; aynı kusur tam maruziyette saatlerce kesinti, acil müdahale ve itibar zararı demek olabilir. Dağıtımı sürümden ayırmak ayrıca sürümün kendisini planlı, yüksek stresli bir olaydan rutin bir olaya dönüştürür; bu da takım büyüklüğüyle doğrusal olmayan biçimde artan koordinasyon vergisini düşürür. Lansman kararını dağıtımdan ayırmak ürün ve mühendisliğin kendi saatlerinde ilerlemesine izin verir; böylece bir pazarlama tarihi asla riskli bir kod dondurmaya zorlamaz.

Toplam sahip olma maliyeti gerçektir ama bu getiri yanında mütevazıdır. Bir bayrak platformuna, kanarya analizi araçlarına, kapılama yapabilecek kadar iyi sağlık ölçütlerine ve geriye uyumlu şema değişiklikleri disiplinine yatırım yaparsınız. Süregelen maliyet bayrak hijyeni ve bayrakların yarattığı daha büyük test matrisidir; yönetilmeyen bir bayrak varlık alanının bu pratiğin pahalıya dönüşmesinin ana yolu olmasının nedeni budur. Benimsememenin maliyeti etki alanında ödenir: her sürüm ya hep ya hiçtir, geri almalar yavaştır ve tek bir kötü dağıtım herkesi bir anda çökertebilir. Düzenlemeye tabi kurumlar için uyum temettüsü belirleyicidir, çünkü maruziyeti sınırlayan aynı mekanizma, aksi halde elle derlenecek olan denetlenebilir kanıtı da üretir.

## Anti-kalıplar ve tuzaklar

- **Dağıtım sürüme eşit.** İkisini bağlamak, kullanıcıya dönük her değişikliği geri vitesi olmayan riskli, hepsi bir anda gerçekleşen bir olay yapar.
- **Bayrak borcu.** Amacından uzun yaşayan anahtarlar, kimsenin silmeye cesaret edemediği kalıcı koşullu karmaşıklığa dönüşür.
- **Açık başarısız olan bayraklar.** Yeni, sınanmamış yola varsayılan olan bir bayrak hizmeti kesintisi küçük bir aksamayı kesintiye çevirir.
- **Şema geri almasına ihtiyaç duyan geri alma.** Özelliğiyle birlikte teslim edilen yıkıcı bir geçiş, kodu güvenle geri döndürememenize yol açar.
- **Hislerle elle terfi.** Bir açılımı tanımlı sağlık ölçütlerine ve hata bütçelerine göre değil "iyi görünüyor" diye ilerletmek.
- **Geri alma planı olmayan açılım.** Bir özelliğin nasıl açılacağını tasarlayıp nasıl kapatılacağını tasarlamamak.
- **Değişiklik kurulunun lastik damgası.** Hiçbir şeyi reddetmeyen bir inceleme güvenlik katmadan gecikme ekler ve takımları büyük gruplara iter.
- **Ayrı sistemlerde deney ve güvenlik bayrakları.** Kimin hangi kovada olduğu konusunda anlaşamayan iki anahtar yığını, denetim yüzeyini ikiye katlar.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Dağıtım ve sürüm aynı olaydır. Değişiklikler bir anda çıkar, geri alma eski bir derlemeyi elle yeniden dağıtmak demektir ve şema geçişleri yıkıcıdır ve özelliklere bağlıdır. Her kademeli maruziyet gelişigüzel, tepkisel ve belgelenmemiştir.
- **Düzey 2, Geliştirme:** Özellik bayrakları bazı takımlar için vardır ve bitmemiş işi gizler, ama sahip, tip ve son kullanma tarihinden yoksundur ve borç birikmektedir. Kanarya ya da mavi-yeşil birkaç kritik hizmet için kullanılır, takım takım tutarsız uygulanır. Geri alma betiklenmiştir ama insan tarafından tetiklenir ve şema değişiklikleri yalnızca bazen geriye uyumludur.
- **Düzey 3, Standartlaştırma:** Dağıtım ve sürüm kurum genelinde varsayılan olarak ayrıdır. Bayraklar tiplenmiş, sahipli ve süreli, güvenli varsayılanlarla, belgelenmiş ve uygulatılan bir standardı izler. Halka tabanlı açılım ve otomatik kanarya analiziyle aşamalı teslimat norm, genişlet-ve-daralt geçişleri zorunludur ve standart değişiklikler otomatik kanıt yakalamayla işlem hattından akar.
- **Düzey 4, Yönetme:** Sürüm süreci veriyle ölçülür ve kontrol edilir. Değişiklik başarısızlık oranı, ortalama geri yükleme süresi, geri alma gecikmesi, bayrak yaşı ve sayısı ve kanarya yanlış pozitif oranı taban çizgilerine ve hata bütçelerine karşı izlenir; açılımlar bu SHH'lere (bölüm 9.1) bağlı kapılanır, böylece terfi ve geri alma tanımlı sağlık sinyallerine göre otomatik hareket eder. Bayrak borcu varlık alanı genelinde bir ölçüt olarak raporlanır ve bir takvime göre emekliye ayrılır; açılım standardından sapmalar bir ölüm sonrası incelemede değil bir panoda görünür.
- **Düzey 5, Orkestrasyon:** Aşamalı teslimat sürekli iyileştirilir ve kurum genelinde bütünleşiktir. Karanlık lansmanlar ve gölge trafik büyük değişikliklerin riskini rutin olarak azaltır, deneyler ve güvenlik açılımları tek bir bayrak sistemini ve denetim izini paylaşır ve sürüm politikası hata bütçesi durumuna gerçek zamanlı uyum sağlar. Denetlenebilir açılım kaydı değişiklik kontrolünü (bölüm 9.3) bir yan ürün olarak karşılar ve kurum halkalarını, kapılarını ve eşiklerini varlık alanı ve risk tablosu değiştikçe kanıttan ayarlar.

## Tartışma fikirleri

1. En kritik hizmetiniz için, otomatik sağlık kapılı bir geri alma ile bir insan kararı arasındaki doğru sınır nerededir ve makinenin tek başına harekete geçmesine izin verecek kadar hangi sinyale güvenirdiniz?
2. Deney bayrakları ve sürüm bayrakları tek bir platformu ve tek bir öldürme anahtarını paylaşmalı mı, yoksa onları birleştirmek ortadan kaldırdığından fazla risk mi yaratır?
3. Bir özellik farklı hızlarda teslim eden birkaç takıma yayıldığında sürüm treni ile isteğe bağlı sürüm arasında nasıl karar verirsiniz?
4. Kod tabanınızda bir sürüm bayrağının dürüst yarı ömrü nedir ve kaldırmayı oluşturmak kadar rutin yapacak olan nedir?
5. Hata bütçesi durumu kimin sürüm çıkarmasına izin verildiğini nasıl değiştirmeli ve bütçe tükendiğinde sürümleri dondurma kararı kime ait olmalı?
6. Düzenlemeye tabi bağlamınızda, kontrol çerçevesinin planlı bir sürüm penceresi yerine aşamalı teslimatı kabul etmesi için bir açılımın hangi özel kanıtı yayması gerekir?

## Önemli çıkarımlar

- **Dağıtımı sürümden ayırın.** Kod teslim etmek ve bir özelliği açığa çıkarmak farklı kararlardır ve onları ayıran şey bayraklardır.
- **Aşamalı açın.** Kanarya, mavi-yeşil, yuvarlanan ve halka tabanlı kalıplar etki alanını sınırlar; riske göre hizmet katmanı başına seçin.
- **Sağlığa ve hata bütçelerine bağlayın.** Otomatik terfiyi ve geri almayı takvimler ya da iyimserlik değil, tanımlı sinyaller ve SHH'ler (bölüm 9.1) yönetsin.
- **Önce geri vitesi tasarlayın.** Hızlı, güvenli geri alma, olay süreciniz (bölüm 9.3) tam devreye girmeden önce etki alanını küçültür.
- **Her bayrağı tipleyin, sahiplendirin ve süreli yapın.** Sürüm, operasyon, deney ve izin bayraklarının ömürleri farklıdır; yönetilmeyen bayraklar borca dönüşür.
- **Şema değişikliklerini geriye uyumlu yapın.** Hem açılımın hem geri almanın karma sürüm penceresi boyunca güvenli kalması için genişlet ve daralt kullanın (bölüm 2.4).
- **Onaylar kaydetsin, engellemesin.** Standart değişiklikleri önceden onaylayın ve insan incelemesini yüksek riske saklayın; böylece açılım kaydı denetim kanıtı olur.

## Kaynaklar ve ileri okuma

- Jez Humble and David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*.
- Nicole Forsgren, Jez Humble, and Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Gene Kim, Jez Humble, Patrick Debois, and John Willis, *The DevOps Handbook*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (eds.), *Site Reliability Engineering*.
- Pete Hodgson, "Feature Toggles (Feature Flags)" (essay on martinfowler.com).
- Danilo Sato, "Canary Release" and Martin Fowler, "BlueGreenDeployment" (essays on martinfowler.com).
- Sam Newman, *Building Microservices: Designing Fine-Grained Systems* (expand-and-contract and independent deployability).
- Pramod Sadalage and Scott Ambler, *Refactoring Databases: Evolutionary Database Design* (parallel-change schema migrations).
- Ron Kohavi, Diane Tang, and Ya Xu, *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*.
- James Governor, "Progressive Delivery" (RedMonk, the coining of the term).
