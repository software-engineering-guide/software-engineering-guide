# 11.2 Teslimat hattı

## Genel bakış ve motivasyon

Teslimat hattı, doğrulanmış bir fikri kullanıcıların elindeki çalışan yazılıma (güvenilir, tekrarlanabilir ve ölçülebilir biçimde) dönüştüren ve ortaya çıkan sonuç verisini keşfe (bölüm 11.1) geri besleyen iş akışıdır. Bir kod işlemesinden (commit) bir üretim değişikliğine, oradan kullanıcılar ve iş üzerindeki ölçülmüş bir etkiye uzanan endüstriyel yoldur. Keşif *ne ve neden* sorusunu yanıtlarken, teslimat *nasıl güvenle sevk ederiz, ne kadar hızlı ve gerçekten işe yaradı mı* sorusunu yanıtlar.

Bu bölüm bilerek bütünleştiricidir. Mekanikler ayrıntılı olarak başka yerlerde yaşar: test stratejisi (bölüm 2.4), test ve süreç otomasyonu (bölüm 8.5), [sürekli entegrasyon](https://en.wikipedia.org/wiki/Continuous_integration) ve [sürekli teslimat](https://en.wikipedia.org/wiki/Continuous_delivery) (CI/CD) ile dağıtım stratejileri (bölüm 8.1), kod olarak altyapı (bölüm 8.2), güvenilirlik ve SLO'lar (hizmet düzeyi hedefleri, bölüm 9.1) ve deneyler (bölüm 7.4). Burada bunları tek bir uçtan uca hatta toplarız ve en önemlisi, bütün makinenin yalnızca sürüm değil değer üretip üretmediğini söyleyen **sonuç metriklerini** ekleriz.

Büyük takımlar için teslimat hattı, mühendislik etkinliğine yapılan en yüksek kaldıraçlı tek yatırımdır. On yıllık araştırma, özellikle *Accelerate* kitabında özetlenen DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) programı, hızlı, otomatik, düşük riskli teslimat hatlarına sahip takımların çıktı hızında *ve* kararlılıkta *ve* kurumsal sonuçlarda daha iyi performans gösterdiğini ortaya koyar. Hız ile güvenliğin birbirinden ödün verdiği yönündeki eski inanç deneysel olarak yanlıştır. Kurumlarda güçlü bir hat, yüzlerce mühendisin birleştirme kaosuna ve elle yapılan sürüm tiyatrosuna çökmeden entegre olmasını sağlar. Kamuda ise yüksek törenli, üç aylık, ya hep ya hiç "büyük patlama" sürümlerinin (tarihsel olarak başarısız programların başlıca nedeni) yerine, değişiklik kontrolü yükümlülüklerini otomasyona *rağmen* değil otomasyon *aracılığıyla* karşılayan küçük, geri alınabilir, denetlenebilir değişiklikler koyar.

## Temel ilkeler

- **Tekrarlanabilir her şeyi otomatikleştirin.** Elle adımlar yavaştır, hataya açıktır ve denetlenemez.
- **Küçük partiler, sık sürümler.** Küçük değişiklikleri gözden geçirmek, test etmek, sevk etmek ve geri almak daha kolaydır.
- **Kaliteyi içine inşa edin.** Hızlı, otomatik testler ve kapılar kusurları üretimden sonra değil, önce yakalar.
- **Dağıtımı sürümden ayırın.** Kodu karanlıkta sevk edin; özellikleri hazır olduklarında bayraklarla açın.
- **Her şeyi geri alınabilir kılın.** Hızlı geri alma ve aşamalı maruz bırakma, dağıtımı bir bahisten bir deneye dönüştürür.
- **Hat, doğruluk kaynağıdır.** Sürüm denetiminde ve hatta değilse, olmamıştır.
- **Yalnızca çıktıyı değil, sonucu ölçün.** Dağıtım sayısı bir çıktıdır; oynayan bir metrik bir sonuçtur.

## Öneriler

### Test paketini otomatikleştirin ve ona göre kapı koyun

Test otomasyonu, hızlı teslimatı güvenli kılan temeldir. Dengeli, çoğunlukla otomatik bir test portföyü uygulayın (bölüm 2.4): çok sayıda hızlı birim testi, daha az entegrasyon ve sözleşme testi, az sayıda uçtan uca test ve ayrıca otomatik güvenlik (SAST/DAST/SCA: statik, dinamik ve yazılım bileşimi analizi), erişilebilirlik ve performans denetimleri. Bunları hatta **kalite kapıları** olarak çalıştırın ki hiçbir değişiklik geçmeden üretime ulaşmasın. Paketi hızlı ve güvenilir tutun: yavaş ya da kararsız bir paket atlanır ve bu da amacını boşa çıkarır (bölüm 8.5). Hattın bir geliştiriciye, bir işlemeden dakikalar sonra net bir geçti/kaldı sinyali vermesini hedefleyin.

### Sürekli entegrasyon ve sürekli teslimat uygulayın

**Sürekli entegrasyon (CI):** her geliştirici küçük değişiklikleri ana hatta sık sık (ideal olarak günlük) birleştirir ve her birleştirme otomatik bir derleme ve test çalıştırması tetikler. Bu, dalları kısa ömürlü ve entegrasyonu sürekli tutan ana dal tabanlı geliştirmeyle (bölüm 2.6) en iyi desteklenir. **Sürekli teslimat (CD):** hattı geçen her değişiklik *her zaman yayınlanabilir durumdadır* ve istek üzerine dağıtılabilir. **Sürekli dağıtım** bir adım daha ileri gider: geçen her değişiklik otomatik olarak üretime dağıtılır. Otomasyon düzeyini risk profilinize uygun seçin; düzenlenen ortamlar kontrollü bir yükseltme adımıyla sürekli teslimatta durabilir (bölüm 8.1), ama o kapıya kadar her şeyi yine de otomatikleştirmelidir.

### Aşamalı stratejilerle güvenle dağıtın

**Dağıtımı** (kodun üretimde çalışması) **sürümden** (kullanıcıların değişikliği deneyimlemesi) ayırın ve değişiklikleri kademeli olarak sunun:

- **[Özellik bayrakları](https://en.wikipedia.org/wiki/Feature_toggle)**, kodu karanlıkta dağıtmanıza ve istek üzerine kesimlere sürmenize, bayrağı çevirerek anında geri almanıza izin verir.
- **Kanarya sürümleri**, trafiğin küçük bir yüzdesini yeni sürüme yönlendirir ve genişletmeden önce sağlık metriklerini izler.
- **Mavi-yeşil dağıtımlar**, iki ortam tutar ve trafiği atomik olarak değiştirir, anında geri alma sağlar.
- **Yuvarlanan dağıtımlar**, örnekleri kademeli olarak değiştirir.
- **Aşamalı teslimat**, bayrakları, kanaryaları ve otomatik analizi birleştirerek canlı sinyallere göre yükseltir ya da geri alır.

Her stratejiyi, SLO ihlalleriyle ya da hata bütçesi tüketimiyle (hataların izin verilen güvenilmezlik bütçesini tüketme hızı; bölüm 9.1) tetiklenen otomatik geri almayla eşleştirin. Mekanikler için bölüm 8.1'e bakın.

### Sonuç metriklerini ölçün: hattı ve etkiyi ölçün

Hızlı sevk eden ama yanlış şeyi sevk eden bir teslimat hattı hızlı israftır. Üç düzeyde ölçün:

1. **Teslimat akışı, dört DORA metriği:**
   - *Dağıtım sıklığı:* üretime ne sıklıkta sürüm çıkardığınız.
   - Değişiklikler için *[teslim süresi](https://en.wikipedia.org/wiki/Lead_time):* işlemeden üretime.
   - *Değişiklik başarısızlık oranı:* bozulmaya yol açan sürümlerin yüzdesi.
   - *Başarısız dağıtımdan kurtarma süresi:* hizmeti ne kadar hızlı geri getirdiğiniz (eskiden MTTR, ortalama kurtarma süresi).
   Elit performans gösterenler istek üzerine dağıtır; teslim süreleri bir saatin altındadır, başarısızlık oranları düşüktür ve kurtarma dakikalar içinde olur. İşin nerede beklediğini görmek için değer akışı düşüncesinden **akış metriklerini** (çevrim süresi, [yarım kalan iş](https://en.wikipedia.org/wiki/Work_in_process), akış verimliliği) ekleyin.

2. **Güvenilirlik ve kalite, SLI'lar ve SLO'lar** (hizmet düzeyi göstergeleri ve hedefleri; bölüm 9.1): hizmet, her değişiklikten sonra güvenilirlik hedeflerini ve kalite niteliği taahhütlerini (bölüm 11.1) karşılıyor mu?

3. **İş ve kullanıcı sonuçları** (bölüm 7.3–7.4): değişiklik, keşfin tanımladığı anahtar sonuçları ve KPI'ları oynattı mı? Sürümün deneyle buluştuğu yer burasıdır: bir bayrağın arkasında sevk edin, bir kontrole karşı ölçün ve yalnızca kazananı tutun.

### Döngüyü keşfe geri kapatın

Teslimat hattının son eylemi dağıtım değil, **kanıttır**. Sonuç metrikleri (aktivasyon yükseldi mi, ödeme süresi kısaldı mı, destek talepleri azaldı mı) bir sonraki bahis turunun temeli olarak keşif hattına (bölüm 11.1) geri akar. Keşif ve teslimat bu geri bildirim döngüsüyle birleştiğinde kurum bir öğrenen sisteme dönüşür: varsayımlar sevk edilir, ölçülür ve ya ölçeklenir ya da geri alınır, sürekli olarak.

### Teslimatı denetlenebilir ve yönetilen kılın

Kurumsal ve kamu ortamlarında hattın kendisini bir uyum kontrolü olarak ele alın. Her değişiklik sürüm denetiminden ve otomatik bir hattan geçtiği için "bedavaya" değiştirilemez bir denetim izi elde edersiniz: kim neyi değiştirdi, hangi testler ve onaylar kapı koydu ve ne zaman dağıtıldı. Görev ayrılığını, zorunlu gözden geçirmeleri ve ilke denetimlerini **kod olarak ilke** (yönetişim kurallarının makinece uygulanabilir, sürüm denetimli bir biçimde ifade edilmesi; bölüm 8.2) olarak kodlayın; böylece değişiklik kontrolü otomatik olarak uygulanır ve sürekli kanıtlanır (bölüm 4.6 ve 10.2), bir denetimden önce elle yeniden kurulmaz.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| **Sürekli dağıtım (otomatik üretime)** | En hızlı geri bildirim; en küçük partiler; en az elle angarya | Olgun test, izleme, geri alma gerektirir; düzenlenen kapılarda zordur |
| **Elle yükseltmeli sürekli teslimat** | İnsan/uyum kontrol noktası; denetim dostu | Daha yavaş; kapıda değişiklikleri biriktirme riski |
| **Özellik bayrakları** | Dağıtım/sürüm ayrımı; anında geri alma; hedefleme | Budanmazsa bayrak borcu ve birleşimsel karmaşıklık |
| **Kanarya / aşamalı teslimat** | Etki alanını sınırlar; veriye dayalı yükseltme | Güçlü gözlemlenebilirlik ve trafik yönetimi gerektirir |
| **Mavi-yeşil** | Anında geçiş ve geri alma | Ortam maliyetini ikiye katlar; durumlu/veri geçişleri zordur |
| **Ağır elle sürüm süreci** | Kontrollü hissettirir; denetçilere tanıdık | Pratikte yavaş, hataya açık, yeniden üretilemez, kötü denetlenir |

Tarihsel ödünleşim inancı, yani *hızlanırsan daha çok bozarsın*, emekliye ayrılması gereken asıl inançtır. Kanıtlar, hızı artıran uygulamaların (otomasyon, küçük partiler, hızlı testler, geri alınabilirlik) kararlılığı artıran *aynı* uygulamalar olduğunu gösterir. Gerçek ödünleşimler hız ile güvenlik arasında değil, **yatırım ve kontrol ayrıntı düzeyi** üzerindedir.

## Takımınızla tartışılacak sorular

1. **Gerçek risk profiliniz nedir ve sürekli dağıtıma geçmek yerine sürekli teslimatta durmayı haklı çıkarıyor mu?** Otomasyon düzeyini seçmek gerçek bir karardır, varsayılan değil. Sürekli dağıtım en hızlı geri bildirimi ve en küçük partileri verir, ama olgun testler, güçlü gözlemlenebilirlik ve anında geri alma gerektirir; bu yüzden düzenlenen bir bağlam makul biçimde kontrollü bir yükseltme kapısında durabilir. Kanıt getirin: değişiklik başarısızlık oranınız, kurtarma süreniz ve test paketinizin güvenilirliği, çünkü bunlar otomatik üretimin bugün güvenli olup olmadığını söyler. Kurumsal ve kamu için, kapıya kadar her şeyi otomatikleştirin ve kapının kendisini kod olarak ilke yapın; böylece insan adımı elle angarya eklemeden kontrol ekler. Hattın kötü bir değişikliği yakalayacağına henüz güvenemiyorsanız, anahtarı çevirmeden önce kapılara ve gözlemlenebilirliğe yatırım yapın.

2. **Hattınız, hiç kimse elle yeniden kurmadan bir düzenleyicinin isteyeceği denetim kanıtını üretebiliyor mu?** Hattın kendisini bir uyum kontrolü olarak ele alın. Her değişiklik, otomatik olarak üretilmiş, kimin neyi değiştirdiğine, hangi testlerin ve onayların kapı koyduğuna ve ne zaman dağıtıldığına dair değiştirilemez bir iz taşımalıdır. Kurumsal ve kamuda görev ayrılığını ve zorunlu gözden geçirmeleri kod olarak ilke biçiminde kodlayın; böylece değişiklik kontrolü bir denetimden önce panik içinde derlenmek yerine sürekli uygulanır ve kanıtlanır. Getireceğiniz sinyal: yakın tarihli bir üretim değişikliği seçin ve onun tam onay-ve-test izini beş dakikada üretmeyi deneyin. Yapamıyorsanız, elle denetim hazırlığı için ödeme yapıyor ve otomasyonun kaldıracağı riski taşıyorsunuz.

3. **Bir sürüm üretimde bozulmaya başladığında geri almayı ne tetikler ve bu otomatik mi?** Geri alınabilirlik, hızı pervasız değil makul kılan şeydir; bu yüzden geri alma tetikleyicisi açık bir tasarımı hak eder. Bir SLO ihlalinin ya da hata bütçesi tüketiminin otomatik olarak geri alıp almayacağına, yoksa kullanıcılar zarar görürken bir insanın fark edip karar vermesi ve harekete geçmesi gerekip gerekmediğine karar verin. Son birkaç olayınızı getirin ve "metrik bozulmaya başladı" ile "değişiklik geri alındı" arasındaki açığı ölçün; bu açık gerçek etki alanınızdır. Günde birçok kez sevk eden büyük takımlar için elle geri alma ölçeklenmez; bayraklar ve kanarya analizi canlı sinyallere göre yükseltmenize ya da geri almanıza izin verir. Yanıtınız "birine çağrı gider ve çözer" ise, her dağıtımı geri alınamaz bir bahis olarak ele alıyorsunuz.

4. **Bir özellik sevk ettiğinizde, oynatması gereken metriği gerçekten oynatıp oynatmadığını ölçüyor musunuz, yoksa dağıtımı sayıp geçiyor musunuz?** Hızlı sevk eden ama etkiyi hiç denetlemeyen bir hat hızlı israftır ve çıktı ile sonuç arasındaki açık, teslimat yatırımının çoğunun sessizce sızdığı yerdir. Büyük bir kurumda haftada yüzlerce sürüm, dağıtım sıklığını skor tablosu saymayı cazip kılar, ama sıklık hareketi ölçer, değeri değil; karşıt çekim, sonuç ölçümünün enstrümantasyona, bir kontrol grubuna ve kaybeden bir özelliği kapalı bırakma disiplinine mal olmasıdır. Son birkaç sevk edilmiş özelliği ve her biri için keşfin tanımladığı hedef metriği, ölçülmüş önce-sonrayı ve oynamadığında ne yaptığınızı getirin. Kurumsal ve kamu portföylerinde, sonuçları sabit bir ritimle kimin gözden geçirdiğini ve sevk edilip hiç karşılığını vermeyen bir özelliği emekliye ayırma yetkisinin kimde olduğunu adlandırın; çünkü ölçmekten kimsenin sorumlu olmadığı bir değişikliği kimse hiçbir zaman kapatmaz. Dürüst sınama, kanıt kaybettiğini söylediği *için* geri aldığınız bir özelliği gösterip gösteremeyeceğinizdir.

5. **Hattınızın bir geliştiriciye geçti/kaldı sinyali vermesi ne kadar sürüyor ve geliştiriciler testlere, etraflarından dolaşmayacak kadar güveniyor mu?** Geri bildirim hızı ve paketteki güven, kalite kapılarının atlanmak yerine gerçekten kapı koymasını sağlayan şeylerdir ve ikisi de kod tabanı büyüdükçe sessizce aşınır. Büyük bir takım için kırk dakika süren ya da on çalıştırmada birinde kararsızlık gösteren bir paket, yüzlerce mühendisi kırmızıda birleştirmeye, denetimleri kapatmaya ya da yeşil olana kadar yeniden çalıştırmaya alıştırır; bu da hızlı gitmeyi ilk başta haklı çıkaran güvenliği sessizce kaldırır. Rakip hususlar test kapsamı ve gerçekçiliği ile geri bildirim hızı ve kararlılığıdır; birini fazla zorlamak diğerini zayıflatır. Mevcut hat süresini, kararsız yeniden çalıştırma oranını ve kapıların atlandığına ya da engelleyici olmayan olarak işaretlendiğine dair her kanıtı getirin. Bu kapıların uyumu karşılayan SAST, DAST ve ilke denetimlerini de taşıdığı kurumsal ve kamu bağlamlarında, atlanmış bir kapı hem bir kalite riski hem de bir denetim açığıdır; bu yüzden kapının gerçekten zorunlu mu yoksa yalnızca tavsiye niteliğinde mi olduğunu ölçün. Geliştiriciler yeşil bir derlemeye neden güvendiklerini ifade edemiyorsa, kapı süstür.

6. **Teslimat yolunun takımlar arasında tutarlı kalmasının ve özellik bayrağı borcunun budanmasının sahibi kim, yoksa her takım kendi hattını yeniden mi icat ediyor?** Bir kurum büyüdükçe teslimat ya ortak bir döşenmiş yolda birleşir ya da uyumsuz kapıları, dengesiz denetim izleri ve amacını aşan bayrakları olan düzinelerce özel hatta parçalanır. Gerilim gerçektir: merkezi bir döşenmiş yol tutarlılık, yönetişim ve ölçek ekonomisi verir, ama bir takımın gerçek kısıtlarını görmezden gelen bir zorunluluk gölge hatlar ve kırgınlık doğurur; bu yüzden döşenmiş yol, takımların gönüllü olarak katılacağı kadar iyi olmalıdır. Bugün kaç ayrı hattın bulunduğunun, bayrak oluşturma ve kaldırmanın nasıl yönetildiğinin ve en iyi ile en kötü takımlarınız arasında teslim süresi ve denetim kalitesinin ne kadar değiştiğinin bir envanterini getirin. Kurumsal ve kamu ortamlarında uyum açısını ekleyin: tutarsız hatlar, görev ayrılığı ve değişiklik kontrolü kanıtının her takımda farklı biçimde (ya da hiç) kanıtlandığı anlamına gelir; kod olarak ilkeli tek bir denetlenmiş döşenmiş yol bunu takım başına bir kumardan kurumsal bir güvenceye çevirir. Eski bayrakları kaldırmanın sahibi yoksa, birleşimsel borç sonunda sistemi sınanamaz kılacaktır.

## Sektör merceği

**Girişim.** Hız hayatta kalmaktır, bu yüzden hattınızı inşa etmek yerine satın alın: ana dal tabanlı geliştirmeyi barındırılan bir CI çalıştırıcısına bağlayın, her birleştirmeye hızlı birim testleri ve bir güvenlik taramasıyla kapı koyun ve barındırılan bir özellik bayrağı hizmetinin arkasında doğrudan üretime dağıtın. Platform takımını ve özel araçları atlayın; en kıt kaynağınız mühendislik dikkatidir ve tek bir genelcinin sürdürebildiği bir hat, kimsenin düzeltmeye vakit bulamadığı ayrıntılı bir hattan iyidir. Akışınızı erken öğrenmek ve yatırımcılara bir şeyleri bozmadan her gün sevk ettiğinizi gösterebilmek için dört DORA metriğini ilk günden basit bir panoda izleyin.

**Küçük işletme.** Özel bir sürüm mühendisi ve dar bir bütçeyle, teslimatı kadro ayırdığınız bir sistem değil, yönetilen hizmetlerden bir araya getirdiğiniz bir şey olarak ele alın: yönetilen CI/CD, barındırılan bir bayrak aracı ve sizin yerinize dağıtımı ve geri almayı yürüten bir bulut platformu. Bakımını karşılayamayacağınız özel hat altyapısı kurmaya direnin ve yolu, nöbetçi kişinin baskı altında anlayabileceği kadar basit tutun. Aşamalı teslimatı ve tek tıkla geri almayı kutudan çıktığı gibi sunan araçları tercih edin; çünkü korkutucu bir Cuma dağıtımını rutin bir dağıtıma çeviren yetenekler bunlardır.

**Kurumsal.** Temel sorun birçok takım arasında tutarlılıktır: takımların yeniden icat etmek yerine katıldığı, otomatik test, güvenlik ve kod olarak ilke kapıları olan desteklenen bir döşenmiş yol hattı. DORA ve SLO metrikleri kurum genelinde karşılaştırılabilir olsun diye arayüzü standartlaştırın, döşenmiş yolu sürdüren platform yeteneğini açıkça bütçeleyin ve özellik bayraklarını ve teslim süresi gerilemelerini takım başına efsane olarak değil, yönetilen varlıklar olarak yönetin. Her değişiklik aynı sürümlü, kapılı yoldan aktığında yönetişim ve denetim otomatik olarak birlikte gelir.

**Kamu.** Tedarik kuralları, şeffaflık ve kamusal hesap verebilirlik hattı şekillendirir; bu yüzden görev ayrılığını ve zorunlu onayları kod olarak ilke biçiminde uygulayan otomatik bir yükseltme kapısında duran sürekli teslimatı tercih edin. Hattın kendisini uyum kontrolü yapın: her değişiklik, elle yeniden kurmadan değişiklik kontrolü ve işletme yetkisi yükümlülüklerini karşılayan değiştirilemez bir denetim izi taşır. Yüksek törenli "büyük patlama" sürümlerini küçük, geri alınabilir, ayrıştırılmış değişikliklerle değiştirin; böylece kamuya dönük bir akışı tek bir bölgede deneyebilir, hata ve tamamlama oranlarını ölçebilir ve bozulursa dakikalar içinde geri alabilirsiniz.

## Örnekler

**Girişim.** B2B analitik aracı sevk eden üç mühendislik takımı, cuma öğleden sonraları elle dağıtım yaparak başlar; bu, haftada bir korkutucu sürüm ve bir hafta sonu endişe demektir. Bir öğleden sonra ana dal tabanlı geliştirmeyi bir GitHub Actions hattıyla kurarlar: hızlı birim testleri, bir linter ve bir güvenlik taraması her birleştirmeye kapı koyar ve geçen bir derleme LaunchDarkly bayraklarının arkasında doğrudan üretime dağıtılır. Dağıtım sıklığı haftalıktan günde birkaç kereye fırlar ve her yeni özellik karanlıkta sevk edilip önce dost bir müşteri için açıldığından, bozuk bir CSV dışa aktarımı Pazartesi olayına dönüşmek yerine dakikalar içinde yakalanıp kapatılır. Yatırımcılara takımın bir şeyleri bozmadan her gün sevk ettiğini gösterebilmek için dört DORA metriğini basit bir panoda izlerler.

**Kurumsal.** Küresel bir sigortacı 40 takımı ortak bir döşenmiş yol hattında birleştirir (takımların katıldığı, desteklenen, önceden entegre varsayılan bir araç zinciri; bölüm 8.4): ana dal tabanlı geliştirme, otomatik test ve güvenlik kapıları ve SLO ihlalinde otomatik geri almalı kanarya dağıtımı. Dağıtım sıklığı aylıktan günde birçok kereye çıkar; teslim süresi altı haftadan bir günün altına düşer; partiler küçük ve kapılar otomatik olduğu için değişiklik başarısızlık oranı düşer. En önemlisi, ürün özellikleri artık bayrakların arkasında sevk edilir ve kontrollere karşı ölçülür; böylece sigortacı her sürümü teklif tamamlama oranı üzerindeki etkisine bağlayabilir ve teslimat hattını doğrudan bölüm 11.1'in keşif tarafındaki anahtar sonuçlarına bağlar.

**Kamu.** Bir kamu kurumu, üç aylık "büyük patlama" sürümlerini (her biri elle adımlarla dolu bir hafta sonu ve sık sık kesinti kaynağı) görev ayrılığını ve zorunlu onayları kod olarak ilke biçiminde uygulayan otomatik bir yükseltme kapısında duran sürekli teslimat hattıyla değiştirir. Her değişiklik, kurumun değişiklik kontrolü ve ATO (işletme yetkisi) yükümlülüklerini karşılayan değiştirilemez bir denetim izi taşır (bölüm 4.6). Sürümler küçük, sık ve geri alınabilir hâle gelir; kurtarma süresi günlerden dakikalara düşer; ve dağıtım, bayraklar aracılığıyla sürümden ayrıldığı için kurum, ulusal kullanıma sunmadan önce yeni bir yardım akışını bir bölgede deneyebilir ve taahhüt etmeden önce tamamlama ve hata oranlarını ölçebilir.

## İş gerekçesi: motivasyonlar, YG ve TSM

Teslimat hattı yatırımının getirisi yazılımda en iyi kanıtlanmış olanlar arasındadır. Daha kısa teslim süresi ve daha yüksek dağıtım sıklığı, fikirlerin kullanıcılara daha erken ulaştığı (ve değer getirmeye ya da düzeltilmeye daha erken başladığı) anlamına gelir. Daha düşük değişiklik başarısızlık oranı ve daha hızlı kurtarma daha az kesinti, daha az yangın söndürme ve daha az itibar ve düzenleme hasarı demektir. DORA araştırması bu yetenekleri yalnızca mühendislik rahatlığıyla değil, üstün ticari ve kurumsal performansla ilişkilendirir. Bileşik etki önemlidir: her gün sevk edip öğrenen bir takım, ayda bir sevk edenden 20–30 kat daha sık yineleme yapar ve bu öğrenme hızı bir ürünün ömrü boyunca belirleyicidir.

**[Toplam sahip olma maliyeti](https://en.wikipedia.org/wiki/Total_cost_of_ownership)** (TSM) açısından otomasyon maliyeti sürekli elle angaryadan, tek seferlik artı bakım niteliğinde bir hat yatırımına kaydırır. Elle bir sürüm her seferinde kıdemli mühendis saatleri tüketir, kötü ölçeklenir ve zayıf denetim kanıtı üretir. Otomatik bir hat bu maliyeti paylaştırır, sonra hacim büyüdükçe *azaltır*, hepsi sürekli olarak daha güçlü kanıt üretirken. Geri alınabilirlik başarısızlığın maliyetini de düşürür: herhangi bir değişiklik saniyeler içinde geri alınabildiğinde, kötü bir dağıtımın beklenen maliyeti çöker; hızlı hareket etmeyi pervasız değil makul kılan budur.

Liderliğe gerekçeyi sunmak için mevcut temel çizgiyi dört DORA metriğiyle ve sürüm başına harcanan elle saatlerle ölçün, ardından kaldırılan angaryayı ve önlenen kesintiyi sayısallaştırın. Benimseme maliyeti gerçektir, yani hat mühendisliği, test yatırımı ve bir platform/döşenmiş yol yeteneği (bölüm 8.4), ama yatırım *yapmamanın* maliyeti yavaş geri bildirimde, sürüm günü riskinde, mühendis tükenmişliğinde ve denetim acısında sürekli ödenir. Belirleyici argüman keşif bağıdır: hızlı, ölçülen bir teslimat hattı, keşif hattının doğrulanmış bahislerini üretimde gerçekten sınanabilir kılan şeydir.

## Anti-kalıplar ve tuzaklar

- **Sonucu değil çıktıyı ölçmek:** hedef metrikler yerinde sayarken dağıtım sayılarını kutlamak.
- **Yavaş ya da kararsız test paketleri:** geliştiricilerin görmezden gelmeyi ya da atlamayı öğrendiği kapılar.
- **Büyük patlama, seyrek sürümler:** riskli, hata ayıklaması zor ve geri alınması zor büyük partiler.
- **Birbirine karıştırılmış dağıtım ve sürüm:** özellik bayrağı yok, bu yüzden her dağıtım geri alınamaz, kullanıcıya dönük bir bahis.
- **Elle sürüm tiyatrosu:** yavaş, tutarsız ve kötü denetlenen elle yürütülen kontrol listeleri.
- **Otomatik hat, gözlemlenebilirlik yok:** gerilemeleri tespit etme ya da teşhis etme becerisi olmadan hızlı sevk etmek.
- **Özellik bayrağı borcu:** hiç kaldırılmayan, sınanamaz birleşimsel karmaşıklığa birikmiş bayraklar.
- **DORA metriklerini oyunlaştırmak:** akışı iyileştirmek yerine sıklığı şişirmek için dağıtımları bölmek.
- **Geri bildirim döngüsü yok:** sonuçlar hiç ölçülmez, bu yüzden teslimat bir sonraki keşif döngüsünü hiç bilgilendirmez.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Elle, seyrek, yüksek törenli sürümler; test çoğunlukla elle ve elle yürütülür; başarı "sevk edildi" olarak ölçülür; geri almalar acı vericidir ve doğaçlamadır; teslimatın nasıl çalışması gerektiğine dair ortak bir fikir yoktur.
- **Düzey 2, Geliştirme:** Bazı takımlar otomatik derlemeler ve birkaç testle CI kurar; sürümler planlıdır; temel izleme vardır; uygulamalar takımdan takıma değişir ve DORA metrikleri henüz izlenmez, bu yüzden teslimat cepler halinde daha iyidir ama kurum genelinde tutarsızdır.
- **Düzey 3, Standartlaştırma:** Belgelenmiş bir döşenmiş yol hattı kurum genelinde uygulanır: otomatik test ve güvenlik kapılı sürekli teslimat, geri almalı aşamalı dağıtım ve kod olarak ilke biçiminde uygulanan görev ayrılığı. Hat değiştirilemez bir denetim izi sağlar ve her takım özel bir yol yerine aynı sürümlü yolu izler.
- **Düzey 4, Yönetme:** Hat, temel çizgilere karşı ölçülür ve kontrol edilir. Dört DORA metriği (dağıtım sıklığı, teslim süresi, değişiklik başarısızlık oranı, kurtarma süresi), SLO başarımı, hata bütçesi tüketimi ve çevrim süresi ile yarım kalan iş gibi akış metrikleri hedeflere karşı izlenir; kapılar ve geri almalar yargıya değil ölçülmüş eşiklere göre tetiklenir. Bayrak borcu, kararsız test oranları ve teslim süresi gerilemeleri izlenir ve her geç ya da geçme kararı kanıta dayanır.
- **Düzey 5, Orkestrasyon:** Teslimat sürekli iyileştirilir ve keşif ile risk planlamasıyla bütünleşir. Sürekli dağıtım uygun olan yerde aşamalı teslimat ve otomatik geri almayla çalışır; özellikler, sonuç metrikleri bir sonraki bahis turuna geri dönen ölçülmüş deneyler olarak sevk edilir; elit DORA performansı döşenmiş yol aracılığıyla takımlar arasında sürdürülür; ve kurum, yük, risk ve ürün karması değiştikçe kapıları, eşikleri ve kapasiteyi uyarlamalı olarak yeniden ayarlar.

## Tartışma fikirleri

1. Mevcut dört DORA metriğiniz nedir ve işlemeden üretime akışınızdaki en büyük darboğaz nerede?
2. Bugün dağıtımı sürümden ayırabiliyor musunuz? Ayıramıyorsanız, özellik bayrakları riskinizi nasıl değiştirirdi?
3. Test paketiniz ne kadar sürüyor ve geliştiriciler onu atlamayacak kadar ona güveniyor mu?
4. Son özelliğinizi sevk ettiğinizde, oynatması gereken metriği oynatıp oynatmadığını ölçtünüz mü?
5. Düzenlenen bir bağlamda, değişiklik kontrol süreciniz teslimatı yavaşlatıyor *mu*, yoksa hat aracılığıyla otomatik olarak mı uygulanıyor?
6. Kod tabanınızdaki hangi özellik bayrakları aylar önce kaldırılmış olmalıydı?

## Önemli çıkarımlar

- Teslimat hattı doğrulanmış fikirleri çalışan, ölçülen yazılıma dönüştürür ve sonuçları keşfe geri besler (bölüm 11.1).
- Bütün yolu otomatikleştirin: hızlı **test kapıları**, **CI/CD** ve **kod olarak altyapı**, doğruluk kaynağı olarak hatla.
- **Dağıtımı sürümden ayırın** ve otomatik geri almalı aşamalı stratejiler (bayraklar, kanarya, mavi-yeşil) kullanın.
- Üç düzeyde ölçün: **DORA/akış** metrikleri, **güvenilirlik/SLO'lar** ve **iş/kullanıcı sonuçları**.
- Hız ve kararlılık **tamamlayıcıdır**, ödünleşim değil: biri için işe yarayan uygulamalar diğerini de sağlar.
- Hat aynı zamanda bir **uyum kontrolüdür**: otomasyon değiştirilemez, sürekli bir denetim izi verir.
- YG hızlı, iyi kanıtlanmış (DORA) ve bileşiktir; yatırım yapmamanın ana maliyeti sürekli ödenir.

## Kaynaklar ve ileri okuma

- *Accelerate: The Science of Lean Software and DevOps*, by Nicole Forsgren, Jez Humble, Gene Kim (the DORA metrics and evidence).
- *Continuous Delivery*, by Jez Humble and David Farley (the foundational text).
- *The DevOps Handbook*, by Kim, Humble, Debois, Willis.
- *The Phoenix Project*, by Gene Kim, Kevin Behr, George Spafford (narrative on flow).
- *Site Reliability Engineering*, by Beyer, Jones, Petoff, Murphy, eds. (SLIs/SLOs, error budgets).
- *Team Topologies*, by Matthew Skelton and Manuel Pais (paved roads and delivery-team design).
- *Feature Flags / progressive delivery*, writings by Pete Hodgson and the LaunchDarkly/Split communities.
- Google DORA, *Accelerate State of DevOps* reports (annual).
- Kim, Gene, *The Unicorn Project* (developer-experience view of flow).
- Reinertsen, Donald, *The Principles of Product Development Flow* (batch size, queues, flow economics).
