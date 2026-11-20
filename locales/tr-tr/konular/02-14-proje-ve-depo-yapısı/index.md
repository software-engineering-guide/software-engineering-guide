# 2.14 Proje ve depo yapısı

## Genel bakış ve motivasyon

Proje ve depo yapısı, bir kod tabanının fiziksel düzenidir: herhangi bir şeyin nerede yaşadığına karar veren klasörler, dosyalar ve adlandırma kuralları. Bir *depo* (çoğu zaman "repo" diye kısaltılır), bir projenin dosyalarını ve geçmişini tutan [sürüm kontrollü](https://en.wikipedia.org/wiki/Version_control) kapsayıcıdır. Bir *proje*, birkaç ilgili bileşeni gruplandırdığında bazen *çözüm* denir, inşa ettiğiniz yazılımın mantıksal birimidir. Yapı, o yazılımı bulmak, anlamak ve değiştirmek için kullandığınız haritadır.

Küçük bir takımda bir kişi tüm düzeni kafasında tutabilir. Yüzlerce ya da binlerce mühendisin, takımlar arası sık geçişlerin ve gelip giden yüklenicilerin olduğu büyük bir takımda, farklı düzenlenen her depo yeni bir bilişsel vergi ödetir. Tanımadığınız bir depoyu açtığınızda, kaynağın, testlerin, belgelerin ve dağıtım yapılandırmasının nerede yaşadığını bir kılavuz okumadan tahmin edebilmelisiniz. Her depo bu sorulara aynı şekilde cevap verdiğinde hareketlilik ucuz ve uyum hızlıdır. Her depo bir kar tanesi olduğunda her bağlam değişimi küçük bir araştırma projesine dönüşür.

Kurumsal ve kamu ortamlarında tutarlı yapı aynı zamanda bir kontrol ve güvence kaygısıdır. Denetçiler, güvenlik inceleyicileri ve çoğu zaman özgün yazarlar gittikten yıllar sonra çalışan uzun vadeli bakımcılar, belirtim belgelerini, lisans dosyalarını, güvenlik politikalarını ve derleme tanımlarını güvenilir biçimde bulmalıdır. Öngörülebilir bir düzen ayrıca otomatik araçların (tarayıcılar, bağımlılık çözümleyiciler, uyum kontrolleri) bir sistemler portföyü boyunca aynı şekilde çalışmasına izin verir. Bu yüzden bu bölüm yapıyı bir kez karar verip her yerde uyguladığınız bir kural olarak ele alır. Kodlama standartları ve üslupla (bölüm 2.1), sürüm kontrolü ve kaynak yönetimiyle (bölüm 2.6) ve belgelemeyle (bölüm 2.7) yakından ilişkilidir.

## Temel ilkeler

- *[En az sürpriz ilkesini](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)* izleyin: düzen deneyimli bir mühendisin beklediğine uymalı, böylece hiçbir şey ezberlenmek zorunda kalmaz.
- Depolar arası tutarlılık yerel zekayı yener; her yerde yeterince tekdüze bir yapı, tek bir yerdeki mükemmel yapıdan daha değerlidir.
- [README](https://en.wikipedia.org/wiki/README) ön kapıdır; bir yeni gelen yalnızca ondan kendini yönlendirebilmelidir.
- Yapıyı adlandırma yoluyla kendini tarif eden yapın; böylece klasörler ve dosyalar amaçlarını duyursun.
- Yapıyı irade ve inceleme yorumlarıyla değil, iskele ve şablonlarla uygulayın.
- İlgileri fiziksel olarak ayırın: kaynak, testler, belgeler, derleme ve dağıtım ayrı, öngörülebilir yerlere aittir.
- Bağımlılıkları kararlı çekirdeklerden değişken kenarlara doğru tek yönde akacak biçimde düzenleyin.

## Öneriler

### Tutarlı bir üst düzey düzen benimseyin

Her deponun uygun olduğu yerde kullandığı standart bir üst düzey klasör kümesi tanımlayın ve her birinin ne için olduğunu belgeleyin. Yaygın, satıcıdan bağımsız bir kural şunları içerir: üretim kodu için bir kaynak klasörü (çoğu zaman `src`); otomatik testler için bir test klasörü (çoğu zaman `test` ya da `tests`); belgeleme için bir `docs` klasörü; derleme tanımları ve çıktıları için bir `build` klasörü; dağıtım ve *[kod olarak altyapı](https://en.wikipedia.org/wiki/Infrastructure_as_code)* (sunucuların, ağların ve hizmetlerin makine tarafından okunabilir tanımları, bölüm 8.2'de ele alınır) için bir `deploy` klasörü; otomasyon ve geliştirici araçları için bir `scripts` klasörü; çalıştırılabilir örnekler için bir `examples` klasörü; ve gereksinimler ile tasarım belirtimleri için bir `spec` ya da `specification` klasörü. Her depo her klasöre ihtiyaç duymaz, ama bir ilgi var olduğunda beklenen yerde, beklenen adla yaşamalıdır.

### README'yi giriş noktası yapın

Depo kökünde tek, kanonik başlangıç noktası olarak bir README dosyası isteyin. Projenin ne olduğunu, nasıl derlenip çalıştırılacağını, testlerin nasıl çalıştırılacağını, daha derin belgelemenin nerede bulunacağını, kimin sahip olduğunu ve nasıl katkı verileceğini belirtmelidir. README tüm belgeleme kümesi değildir; geri kalanına (bölüm 2.7) işaret eden dizindir. Eksik ya da bayat bir README'yi kusur olarak ele alın, çünkü her yeni mühendisin, denetçinin ya da entegratörün ilk okuyacağı şeydir.

### Düzenleyici ve yapılandırma dosyalarını standartlaştırın

Her katılımcının tutarlı davranışı otomatik elde etmesi için paylaşılan düzenleyici ve araç yapılandırmasını depoya işleyin. Bir `.editorconfig` dosyası (boşluk, girinti ve satır sonu kurallarını tanımlayan basit, düzenleyiciden bağımsız bir dosya), temel biçimlendirmeyi farklı düzenleyiciler ve işletim sistemleri arasında tekdüze tutar. Sürüm kontrol sistemi için bir yoksayma dosyası ekleyin (böylece derleme çıktıları ve yerel yapıtlar asla commit'lenmez), bölüm 2.1'de anlatılan paylaşılan biçimlendirici ve linter yapılandırmalarıyla birlikte. Bu dosyalar deponun kurallarını yalnızca belgelenmiş değil, etkin yapar.

### Adlandırma ve klasör kurallarını tanımlayın

Klasör ve dosya adlandırma kuralları üzerinde (büyük/küçük harf, ayırıcılar, tekil ya da çoğul ve testleri işaretleyenler gibi gerekli son ekler) anlaşın ve tekdüze uygulayın. Adlar niyeti ortaya koymalı ve kuruluşun başka yerlerde kullandığı alan sözcük dağarcığıyla eşleşmelidir. Amaç basittir: bir yol anlam iletmeli, böylece bir klasör ya da dosya adını okumak içinde ne olduğunu açmadan söylemelidir.

### Katmanları ve bağımlılıkları bilinçli düzenleyin

Kod tabanını, mimari katmanları klasör düzeninde görünecek ve bağımlılıklar tek, makul bir yönde akacak biçimde yapılandırın. Üst düzey politika alt düzey ayrıntıya bağımlı olmamalıdır. Paylaşılan, kararlı kod, birçok modülün döngü yaratmadan ulaşabileceği yerde durmalıdır. Katmanlamayı fiziksel yaptığınızda, dizin ağacına yansıtılmış, mühendisler ona uyma eğiliminde olur ve ihlaller incelemede ve otomatik bağımlılık kontrollerinde daha kolay fark edilir.

### Yapıyı iskele ve şablonlarla uygulayın

Yeni depoların zaten doğru başlaması için başlangıç projesinin otomatik üretimi olan *[iskele](https://en.wikipedia.org/wiki/Scaffold_%28programming%29)* sağlayın. Bir *şablon* ya da *cookiecutter* (birkaç soruya verilen cevaplardan hazır bir depo üreten parametreli bir proje iskeleti), standart düzeni, README'yi, yapılandırma dosyalarını ve [CI](https://en.wikipedia.org/wiki/Continuous_integration) kurulumunu tek yerde kodlar. Mühendisler yeni hizmetleri paylaşılan bir şablondan oluşturduğunda tutarlılık bir özlem yerine varsayılan olur ve şablondaki iyileştirmeler gelecek projelere akar.

### Birçok depo boyunca yapıyı ölçekte tutarlı tutun

Düzenin kendisini yönetilen bir standart olarak ele alın: başka herhangi bir mühendislik standardı gibi merkezi sürdürülen (bölüm 1.7) ve kod gibi sürümlenen (bölüm 2.6). Onu yayımlayın, onu uygulayan şablonları sağlayın ve sapmalara yalnızca belgelenmiş bir istisna süreciyle izin verin; böylece "standart" anlamını korur. Portföy ölçeğinde yapının değerinin neredeyse tamamı depolar arası tekdüzelikten gelir; bu yüzden sürüklenme, yönetilecek ana risktir.

### Yapının tek depo ile çok depo seçimini bilgilendirmesine izin verin

Yapıyı bölüm 2.6'da ele alınan depo sınırı kararıyla ilişkilendirin. Bir *[tek depo](https://en.wikipedia.org/wiki/Monorepo)* (birçok projeyi tutan bir depo), tek ağacın gezilebilir kalması için projeleri ve paylaşılan kodlarını ayırmak üzere net bir iç kurala ihtiyaç duyar. Bir *çok depo* yaklaşımı (proje ya da hizmet başına bir tane, çok sayıda küçük depo), her depo tek başına dursa bile tanıdık hissetmesi için güçlü depolar arası tutarlılığa ihtiyaç duyar. İkisinde de belgelenmiş, şablonlanmış bir yapı gezinmeyi öngörülebilir tutan şeydir. Sınır seçimi kuralı nerede uyguladığınızı değiştirir, bir kurala ihtiyaç duyup duymadığınızı değil.

## Ödünleşimler: artılar ve eksiler

| Seçim | Artılar | Eksiler |
|---|---|---|
| Katı kuruluş genelinde standart düzen | Anında aşinalık; taşınabilir mühendisler; tekdüze araçlar | Alışılmadık projelere ara sıra zayıf uyum; yönetişim gerekir |
| Takım başına düzen özgürlüğü | Yerel optimizasyon; yüksek özerklik | Parçalanma; maliyetli bağlam değişimi; tutarsız araçlar |
| İskele ve şablonlar | Varsayılan olarak doğru depolar; değişiklikler yayılır | Şablon bakımı; üretilen depolardan sapma riski |
| Derin, katmanlı klasör hiyerarşisi | Açık yapı; net sınırlar | Gezinme yükü; uzun yollar; aşırı mühendislik riski |
| Düz, sığ düzen | Taraması kolay; düşük tören | Zayıf ayrım; proje büyüdükçe çöker |

Baskın ödünleşim tekdüzelik ile özerklik arasındadır. Tek standart düzen, kod tabanları arasında geçen birçok mühendis için sürtünmeyi kaldırır; bedeli, ihtiyaçları kalıba düzgünce uymayan ara sıra bir projedir. Büyük bir kuruluşta aşinalıktan toplu kazanç hemen her zaman o yerel kayıptan ağır basar. Bu yüzden önerilen duruş, ya katı tekdüzelik ya da yönetilmeyen özgürlük yerine, güçlü bir varsayılan standart artı belgelenmiş bir istisna yoludur (bölüm 1.7). İkincil ödünleşim derinlik ile sadelik arasındadır: gerçek ilgileri ayırmaya yetecek yapı, ama gezinmenin boş klasörler arasında bir yürüyüşe dönüşmeyeceği kadar az.

## Takımınızla tartışılacak sorular

1. **Bir mühendis bizim tanımadığı bir depoya geçtiğinde testleri, dağıtım yapılandırmasını ve sahibi bulmaları ne kadar sürer?** Bu, yapının ortadan kaldırmak için var olduğu gezinme vergisidir ve portföy ölçeğinde yılda binlerce kez ciddi kayıp mühendislik zamanına toplanan küçük artışlarla ödenir. En az sürpriz ilkesinin amacı, deneyimli bir mühendisin kaynağın, testlerin, belgelerin ve dağıtımın nerede yaşadığını bir kılavuz okumadan tahmin edebilmesidir; bu yüzden dürüst test, o tahminin depolarınız boyunca başarılı olup olmadığıdır. Toplantıya gerçek bir sayı getirin: tanımadığınız iki üç dahili depoda kendinizi yönlendirme sürenizi ölçün ya da yeni katılanların ilk değişikliği yapmasının ne kadar sürdüğüne dair uyum verisi çekin. Cevap tanıma dakikaları yerine araştırma günleriyle ölçülüyorsa kar tanesi depoların maliyetini nicelleştirdiniz ve bu, her deponun paylaştığı standart düzene tek seferlik yatırımı haklı çıkarır.

2. **Mimari katmanlarımız klasör ağacında görünüyor mu, yoksa bağımlılık döngüleri düz bir düzenin içinde mi saklanıyor?** Yapı bulunabilirlikten fazlasıdır: katmanlamayı fiziksel yaptığınızda mühendisler ona uyar ve inceleyiciler ile otomatik bağımlılık kontrolleri ihlalleri fark edebilir; düz bir yığın ise uygunsuz bağlaşımın ve döngülerin, değişim tehlikeli olana kadar fark edilmeden sızmasına izin verir. Büyük, uzun ömürlü bir sistemde bu, üst düzey politikanın alt düzey ayrıntıya sessizce bağımlı olmasını önleyen şeydir ve tam olarak önlemesi ucuz, geri almak pahalı olan erozyon türüdür. Bağımlılık çizgenizi getirin ya da hızlı bir kontrol çalıştırın: döngüler var mı ve kararlı bir şey değişken bir şeye bağımlı mı? Cevap sizi katmanları dizinlerde yansıtmaya ve otomatik bağımlılık yönü kontrolleri eklemeye itmelidir; böylece sınırlar ağaçta görünür ve birinin zihinsel modelinde yaşamak yerine hatta uygulanır.

3. **Yeni depolarımız bir şablondan doğru mu başlıyor, yoksa bir viki sayfasına ve iyi niyete mi güveniyoruz?** İskeleyle uygulanan yapı varsayılandır; bir belgede tarif edilen yapı sürüklenir, çünkü gerçeklik bir sayfanın nasıl görünmeleri gerektiğini söylediğine değil, depoları neyin ürettiğine uyar. Büyük ya da düzenlemeye tabi bir kuruluş için bu aynı zamanda bir güvence kaygısıdır: her depo paylaşılan bir şablondan üretildiğinde güvenlik tarayıcıları, bağımlılık çözümleyiciler ve denetçiler lisansı, güvenlik politikasını, belirtimi ve derleme tanımını satıcılar ve yıllar boyunca her seferinde aynı yerde bulur. Kanıtı getirin: yakın tarihli depolarınızın kaçı standart şablondan iskelelendi ve kaçı elle bir araya getirildi ve şablonlu olanlar o zamandan beri ne kadar saptı? Eylem, şablonu bir depoya başlamanın tek kolay yolu yapmak, onu belgelenmiş bir istisna yoluyla sürümlü bir standart olarak yönetmek ve sürüklenmeyi otomatik algılamaktır, çünkü yapının değerinin neredeyse tamamı tekdüzelikte yaşar.

4. **Standardımızın bir tek depoyu mu yoksa birçok ayrı depoyu mu kapsadığına karar verdik mi ve aynı kural o sınırın iki tarafında da gerçekten geçerli mi?** Depo sınırı seçimi kuralı nerede uyguladığınızı değiştirir, bir kurala ihtiyaç duyup duymadığınızı değil ve yanlış yapmak ya kimsenin gezemediği tek devasa bir ağaç ya da her biri yabancı hissettiren bir depo yayılması demektir. Bir tek depo, tek ağacın gezilebilir kalması için projeleri ve paylaşılan kodlarını ayırmak üzere net bir iç kurala ihtiyaç duyarken, çok depo yaklaşımı her bağımsız deponun hâlâ tanıdık hissetmesi için güçlü depolar arası tutarlılığa ihtiyaç duyar. Mevcut envanteri getirin: kaç deponuz var, paylaşılan kod herhangi bir tek depo içinde nasıl ayrılmış ve bir mühendisin büyük ağaç içindeki bir projeyi bağımsız bir depodaki kadar hızlı bulup bulamayacağının zamanlı bir testi. Büyük bir kurum ya da farklı satıcıların ayrı depolar teslim ettiği bir kamu programı için kuralın hangi parçalarının evrensel ve hangilerinin sınıra özgü olduğuna bilinçli karar verin, çünkü denetçiler ve platform araçları kod bir ağaç ya da elli ağaç olarak geldiğinde de aynı şekilde çalışmalıdır.

5. **Yapı standardımıza kim sahip ve bir proje gerçekten ona uymadığında aslında ne oluyor?** Portföy ölçeğinde yapının değerinin neredeyse tamamı tekdüzelikten gelir; bu yüzden gerçek riskler çürüyen sahipsiz bir standart ve her takımın sessizce kendi düzenini icat edeceği kadar belirsiz bir istisna yoludur. Gerilim, hiçbir alışılmadık projeye uymayan katı tekdüzelik ile her şeyi parçalayan yönetilmeyen özgürlük arasındadır ve sağlıklı cevap, adı konmuş bir sahibin yönettiği ve kod gibi sürümlenen güçlü bir varsayılan artı belgelenmiş, denetlenebilir bir istisna sürecidir. Kanıtı getirin: tek bir sorumlu sahip, değişiklik günlüğü olan sürümlü bir standart belgesi, verilen istisnaların ve nedenlerinin bir günlüğü ve doğada bulabileceğiniz belgelenmemiş sapmaların sayısı var mı. Kurumsal ve kamu ortamlarında kimsenin kaydetmediği bir istisna bir kontrol boşluğudur; bu yüzden her sapmayı yazılı bir gerekçeye ve bir gözden geçirme tarihine bağlayın ve düzeni zorunlu kılan tedarik sözleşmelerinin sapmaları kimin onaylayabileceğini de adlandırdığından emin olun.

6. **README'miz ve depoya işlenmiş yapılandırma dosyalarımız kurallarımızı etkin mi yapıyor, yoksa dekoratif mi?** README ön kapıdır ve depoya işlenmiş `.editorconfig`, yoksayma dosyası ve linter yapılandırması kuralları kendi kendine uygulayan şeylerdir; yine de bunlar bayatlayan ilk, bir denetçi ya da yeni katılan projeyi derleyemeyene kadar kimsenin fark etmediği son şeylerdir. Gerilim, güncel kalan yalın bir README ile sürüklenen kapsamlı bir README arasında ve insanlara kodu doğru biçimlendirmeleri için güvenmekle paylaşılan yapılandırmanın bunu otomatik uygulamasına izin vermek arasındadır. Bir örnek getirin: beş depo çekin ve kaç README'nin gerçekten projenin ne olduğunu, nasıl derlenip test edilip çalıştırılacağını ve kimin sahip olduğunu belirttiğini ve kaçının bireysel alışkanlıklara güvenmek yerine paylaşılan yapılandırma dosyalarını taşıdığını kontrol edin. Entegratörlerin, güvenlik inceleyicilerinin ve uzun vadeli bakımcıların başka her şeyden önce README'yi okuduğu büyük ya da düzenlemeye tabi bir kuruluşta, eksik ya da bayat bir ön kapıyı sahibi olan bir kusur olarak ele alın ve uyumun iyi niyete bağlı olmaması için yapılandırma dosyalarının varlığını otomatik kontrol edin.

## Sektör merceği

**Girişim.** Hız kazanır; bu yüzden ilk depo için tek basit, yeterince düz bir düzen üzerinde anlaşın (src, test, docs, scripts, doldurulmuş bir README, bir `.editorconfig` ve yoksayma dosyaları) ve onu aynı öğleden sonra hafif bir şablon olarak kaydedin. İkinci hizmeti ondan üretin; böylece her iki depo da tanıdık hissettirir ve yeni bir yüklenici bir kar tanesini tersine mühendislikle çözmek yerine saatler içinde uyum sağlar. Henüz ihtiyacınız olmayan derin hiyerarşilere ve ağır yönetişime direnin; buradaki tüm getiri, iki kurucu ve bir yüklenicinin tek haritayı paylaşmasıdır.

**Küçük işletme.** Platform uzmanı ve sıkı bir bütçe olmadan, bir tane icat etmek yerine dilinizin ya da çerçevenizin zaten varsaydığı geleneksel düzeni benimseyin; böylece hazır araçlar ve her yeni işe alınan onun üzerinde önceden eğitilmiş gelir. Kendi iskelenizi inşa etmek yerine iskele (bir çerçeve üreteci ya da bir cookiecutter şablonu) satın alın ve kıt çabanızı doldurulmuş bir README'yi güncel tutmaya harcayın. O README, düzeni bilen tek kişi başka yere geçtiği gün için sahip olduğunuz en ucuz sigortadır.

**Kurumsal.** Birçok takım ve yüzlerce depo boyunca hedef tekdüzeliktir: sürümlü bir yapı standardı yayımlayın, her yeni hizmeti paylaşılan şablonlardan üretin, sürüklenmeyi otomatik algılayın ve sapmalara yalnızca belgelenmiş bir istisna süreciyle izin verin. Her depo aynı göründüğü için yeni bir takıma atanan mühendis saatler içinde verimli olur ve portföy genelinde güvenlik ve bağımlılık tarayıcıları lisansı, güvenlik politikasını ve derleme tanımını her seferinde aynı yerde bulur. Şablon bakımını ve sürüklenme algılamayı açıkça bütçeleyin, çünkü o bakım standardı ölçekte anlamlı tutan şeydir.

**Kamu.** Tedarik, şeffaflık ve uzun vadeli hesap verebilirlik düzeni biçimlendirir; bu yüzden her satıcıyı bağlayan teslimat standartlarında ortak bir yapıyı zorunlu kılın. Kodu onaylı gereksinimlere bağlayan bir `specification` klasörünü, kökte bir lisans ve güvenlik politikası dosyasını ve kod olarak altyapı tanımlarını tutan bir `deploy` klasörünü isteyin; böylece denetçiler uyum yapıtlarını her sistemde aynı şekilde bulur. Farklı satıcılardan yükleniciler tek haritayı izlediği için, bir sözleşme bittikten sonraki bakım çok daha az maliyetlidir ve kamu gereksinimden çalışan koda savunulabilir, incelenebilir bir iz kazanır.

## Örnekler

**Girişim.** Üç kişilik bir girişim ilk deposu için basit bir standart düzen üzerinde anlaşır (src, test, docs, scripts, doldurulmuş bir README, bir .editorconfig ve yoksayma dosyaları) ve onu hafif bir şablon olarak kaydeder. Bir ay sonra ikinci hizmetlerini açtıklarında onu o şablondan üretirler; böylece her iki depo da zaten tanıdık hisseder ve yeni yüklenici bir öğleden sonra uyum sağlar. Henüz ihtiyaç duymadıkları derin klasör hiyerarşilerine direnir ve ağacı bir bakışta taranabilecek kadar düz tutarlar. Maliyet bir öğleden sonralık kurulumdu ve aksi halde her gelecek depoyu küçük bir araştırma projesine çevirecek kar tanesi yayılmasından onları kurtarır.

**Kurumsal.** Çok uluslu bir perakendeci birkaç dil boyunca yüzlerce hizmet işletir. Platform takımı sürümlü bir depo yapısı standardı ve onu uygulayan bir proje şablonları kümesi yayımlar. Her yeni hizmet bir şablondan üretilir; bu yüzden standart `src`, `test`, `docs`, `deploy` ve `scripts` klasörleri, doldurulmuş bir README, bir `.editorconfig`, yoksayma dosyaları ve çalışan bir CI hattıyla gelir. Her depo aynı göründüğü için yeni bir takıma atanan mühendis saatler içinde verimli olur ve kuruluş genelinde güvenlik ve bağımlılık tarayıcıları her zaman dosyaları beklediği yerde buldukları için tekdüze çalışır.

**Kamu.** Eski sistemleri modernleştiren ulusal bir kurum, tüm satıcılar için teslimat standartlarının parçası olarak ortak bir depo düzenini zorunlu kılar. Her depo, kodu onaylı gereksinimlere bağlayan bir `specification` klasörü, belgelenmiş bir README, kökte bir lisans ve güvenlik politikası dosyası ve kod olarak altyapı tanımlarını tutan bir `deploy` klasörü (bölüm 8.2) içermelidir. Farklı satıcılardan yükleniciler aynı yapıyı izlediği için kurumun denetçileri uyum yapıtlarını her sistemde aynı şekilde bulabilir ve gelen bakımcılar haritayı zaten bildiği için sözleşme bittikten sonraki uzun vadeli bakım çok daha az maliyetlidir.

## İş gerekçesi: motivasyonlar, YG ve TSM

Bir yapı standardını benimsemenin maliyeti çoğunlukla tek seferliktir: düzen üzerinde anlaşmak, şablonları inşa etmek ve kuralı belgelemek. Yinelenen maliyet düşüktür, şablonları sürdürmekte ve istisnaları yönetmekte yoğunlaşır. Standardın *olmamasının* maliyeti yinelenen ve bileşiktir: tanımadığı bir depoyu açan her mühendis bir gezinme vergisi öder, her uyum daha yavaş ilerler ve hiçbir şey beklediğiniz yerde olmadığı için otomatik araçların depo başına yapılandırılması gerekir. Büyük bir kuruluş boyunca bu küçük sürtünmeler ciddi mühendislik zamanı kayıplarına çarpılır.

Getiri daha hızlı uyum, takımlar arasında daha ucuz hareketlilik, portföy genelinde araçlardan daha yüksek sinyal ve düzenlemeye tabi ortamlarda, yapıtlar her zaman bulunabilir olduğu için daha düşük denetim ve uzun vadeli bakım maliyeti olarak görünür. *Toplam sahip olma maliyeti* (TSM, bir sistemi inşa etmenin, çalıştırmanın ve sürdürmenin tüm ömür boyu maliyeti), öngörülebilir yapıdan yararlanan bakımcıların genellikle onu yaratan yazarlar olmadığı uzun ömürlü sistemlerde en çok düşer. Gerekçeyi liderliğe sunmak için yapıyı geliştirici verimliliğini ve denetim hazırlığını iyileştiren düşük maliyetli, yüksek kaldıraçlı bir standart olarak çerçeveleyin ve tutarsızlığın bugünkü maliyetine uyum süresi verisini ve tanımadığınız depolarda bir şey aramaya harcanan çabayı kullanarak bir sayı koyun.

## Anti-kalıplar ve tuzaklar

- **Kar tanesi depo:** her depo farklı düzenlenmiş; bu yüzden her biri sıfırdan yeniden öğrenilmelidir.
- **Eksik ya da bayat README:** ön kapı yok; yeni gelenleri projenin nasıl derlenip çalıştırılacağını tersine mühendislikle çözmeye zorlar.
- **Şablonla değil belgeyle yapı:** bir viki sayfası standart düzeni tarif eder ama hiçbir şey onu üretmez ya da uygulamaz; bu yüzden gerçeklik ondan uzaklaşır.
- **Şablon sürüklenmesi:** bir şablondan üretilen depolar zamanla ayrışır ve şablondaki iyileştirmeler onlara asla ulaşmaz.
- **Aşırı mühendislikli hiyerarşi:** gezinmeye yardım etmeden tören ekleyen, neredeyse boş klasörlerin derin iç içe geçmeleri.
- **Karışık ilgiler:** kaynak, testler, derleme çıktıları ve sırlar net ayrım olmadan birbirine karışmış.
- **Commit'lenmiş derleme çıktıları ve yerel yapıtlar:** yoksayma kuralları hiç kurulmadığı için işlenmiş üretilmiş dosyalar; geçmişi ve farkları kirletir.
- **Düz yapının gizlediği katman ihlalleri:** fiziksel sınır yok; bu yüzden bağımlılık döngüleri ve uygunsuz bağlaşım fark edilmeden sızar.

## Olgunluk modeli

- **Düzey 1 (Başlangıç):** Her depo yazarları tarafından o anın ihtiyacına tepki vererek gelişigüzel düzenlenir; düzenler geniş ölçüde değişir; README'ler eksik ya da güvenilmezdir; yeni gelenlere her depo elle gezdirilmelidir.
- **Düzey 2 (Geliştirme):** Temel kurallar gayriresmi olarak vardır ve birçok depo birbirine benzer; bazı takımlar kendi başlangıç düzenini tutar; ama yetkili bir standart, paylaşılan iskele yoktur ve yapı takımdan takıma gözle görülür sürüklenir.
- **Düzey 3 (Standartlaştırma):** Belgelenmiş, sürümlü bir yapı standardı kuruluş genelinde uygulanır; yeni depolar standart bir düzen, README, yapılandırma dosyaları ve CI taşıyan paylaşılan şablonlardan üretilir; sapmalar sessizce olmak yerine belgelenmiş bir istisna sürecinden geçer.
- **Düzey 4 (Yönetme):** Standarda uyum veriyle ölçülür ve kontrol edilir: otomatik kontroller depoların hangi kesrinin düzenle eşleştiğini, şablonlu depoların ne kadar saptığını, README eksiksizliğini ve bağımlılık yönü ihlallerini raporlar; hepsi temel çizgilere karşı izlenir; uyum ve gezinme süreleri ölçülür; istisnalar günlüğe alınıp gözden geçirilir ve şablon değişiklikleri görüşe değil kanıta dayanarak onaylanır.
- **Düzey 5 (Orkestrasyon):** Yapı sürekli iyileştirilir ve uyum sağlar: şablon iyileştirmeleri mevcut depolara otomatik yayılır, yapı yönetişimi güvenlik, uyum ve platform araçlarıyla bütünleşir ve standart diller, mimariler ve portföy kaydıkça bilinçli evrilir; kuruluş etrafında değişirken tekdüzeliği yüksek tutar.

## Tartışma fikirleri

- Kuruluşunuzda hangi üst düzey klasörler gerçekten evrensel olmalı ve hangileri isteğe bağlı?
- Bir şablondan üretilen depoların zamanla ondan sapmasını nasıl önlersiniz?
- Yararlı, katmanlı bir hiyerarşi ile aşırı mühendislikli klasör töreni arasındaki çizgi nerede?
- Yapı standardınız, varsa, bir tek depo ile çok depo yaklaşımı arasında nasıl farklılaşmalı?
- Gerçek ihtiyaçları standart düzene uymayan bir proje için doğru istisna süreci nedir?
- Yapınızın ne kadarı otomatik kontrol edilebilir ve neler hâlâ insan incelemesine dayanıyor?
- Yapı standardına ve şablonlarına kim sahip ve değişiklikler nasıl önerilip yayılıyor?

## Önemli çıkarımlar

- Her depoyu, herhangi bir mühendisin herhangi bir kod tabanında beklentiyle gezinebileceği biçimde, en az sürpriz ilkesini izleyerek düzenleyin.
- Tutarlı bir üst düzey düzen (kaynak, test, docs, build, deploy, scripts, examples, specification) benimseyin ve README'yi giriş noktası yapın.
- Kuralların yalnızca yazılmış değil etkin olması için düzenleyici ve araç yapılandırmasını (`.editorconfig` gibi) depoya işleyin.
- Yeni depoların varsayılan olarak doğru olması için yapıyı iskele ve şablonlarla uygulayın.
- Ölçekte değer tekdüzeliktedir: standardı yönetin, sürüklenmeyi kontrol edin ve sapmalara yalnızca belgelenmiş istisnayla izin verin.

## Kaynaklar ve ileri okuma

- Robert C. Martin, *Clean Architecture: A Craftsman's Guide to Software Structure and Design*
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction*
- Andrew Hunt and David Thomas, *The Pragmatic Programmer*
- Titus Winters, Tom Manshreck, and Hyrum Wright (eds.), *Software Engineering at Google*
- Scott Chacon and Ben Straub, *Pro Git*
- EditorConfig project documentation (as a reference standard for editor configuration)
