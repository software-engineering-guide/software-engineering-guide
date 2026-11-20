# 11.3 Kuyruk kuramı

## Genel bakış ve motivasyon

[Kuyruk kuramı](https://en.wikipedia.org/wiki/Queueing_theory), bekleme hatlarının matematiksel incelemesidir. Yazılım mühendisliğinde, çok büyük bir uygulama yığınının ardındaki sessiz kuramdır. Müşteri hizmetlerinin yanıt verme hızı, [kanban](https://en.wikipedia.org/wiki/Kanban_%28development%29) planlaması (akışı iyileştirmek için [yarım kalan işi](https://en.wikipedia.org/wiki/Work_in_process) sınırlayan çekmeli bir yöntem), süreçler arası ileti kuyrukları, sürekli dağıtım hatları: bunların hepsi kuyruktur ve hepsi aynı yasalara uyar. Bu yasaları anlamak, bir takımın [teslim sürelerini](https://en.wikipedia.org/wiki/Lead_time), [çıktı hızını](https://en.wikipedia.org/wiki/Throughput), kapasiteyi ve sistemleri sınırlarına yakın çalıştırmanın gerçek maliyetini üretimde şaşırmak yerine önceden akıl yürüterek ele almasına izin verir. Bu bölüm Akış bölümünde yer alır, çünkü kuyruk kuramı akışın biçimsel temelidir: işin *neden* beklediğini ve beklemeyi gerçekte neyin azalttığını açıklar.

Motivasyon şudur: kuyruklar hakkındaki sezgi güvenilir biçimde yanlıştır ve pahalı biçimlerde yanlıştır. İnsanlar %90 kullanım oranında çalışan bir sunucunun "sorundan %10 uzakta" olduğunu varsayar; oysa kullanım %100'e yaklaştıkça bekleme süreleri doğrusal olmayan biçimde patlar. Yarım kalan işi (WIP) artırmanın teslimatı hızlandırdığını varsayarlar; oysa bu teslim sürelerini uzatır. Kapasiteyi ortalamalara göre planlarlar, sonra değişkenlik onları ezer. Biraz kuyruk kuramı, bu pahalı sezgilerin yerine, müşteri kuyruklarında, görev panolarında ve CI/CD hatlarında aynı şekilde geçerli olan, en önemlisi **[Little Yasası](https://en.wikipedia.org/wiki/Little%27s_law)** olan az sayıda sağlam ilişki koyar.

Büyük takımlar, kurumlar ve kamu için kuyruk kuramı, kapasite ve akış için ortak bir dildir; aksi hâlde birbirini duymadan konuşan rolleri bağlar. Ürün yöneticileri fikirden müşteriye teslim süresini önemser. SRE'ler sunucu kullanım oranını ve gecikmeyi önemser. DevOps takımları dağıtım sıklığını önemser. Destek liderleri yanıt sürelerini önemser. Bunların hepsi kuyruk metrikleridir ve onları tek bir çerçevede (varış hızı, hizmet hızı, kullanım oranı, bekleme süresi) ifade etmek, bir kurumun kapasite planlamasına, gerçekçi SLO'lar (hizmet düzeyi hedefleri) koymasına ve yatırımı anekdotla değil matematikle gerekçelendirmesine izin verir.

## Temel ilkeler

- **Beklemesi olan her şey bir kuyruktur:** biletler, görevler, iletiler ve dağıtımlar dahil.
- **Little Yasası çapadır:** sistemdeki öğeler = varış hızı × sistemde geçen süre (κ = λτ).
- **Kullanım oranı ve bekleme süresi doğrusal değildir:** kapasitenin son %15'i en pahalı olanıdır.
- **Değişkenlik akışın düşmanıdır:** ortalamalar acıyı gizler; kuyrukları varyans yaratır.
- **Yarım kalan işi azaltmak teslim süresini azaltır:** hedef meşguliyet değil, akıştır.
- **Bütün akışı ölçün:** varışlar, hizmet, başarılar, başarısızlıklar, atlamalar ve beklemeler.
- **Bir süreç, kuyrukların kuyruğudur:** aşamaları modelleyin, sonra kısıtlayıcı olanı eniyileyin.

## Öneriler

### Temel gösterimi öğrenin ve tutarlı kullanın

Bir avuç nicelik herhangi bir kuyruğu tanımlar. Bunlar üzerinde standartlaşmak (Yunan harfleri gelenekseldir) takımlar arasındaki belirsizliği ortadan kaldırır:

- **λ (lambda), varış hızı:** yeni öğelerin ne kadar hızlı girdiği.
- **μ (mu), hizmet hızı:** öğelerin ne kadar hızlı ele alındığı. "Hizmet hızı" belirsiz biçimde kullanıldığından, çıktı hızını açıkça **toplam hız (χ)**, **başarı hızı (α)**, **başarısızlık hızı (β)** ve **atlama hızı (σ)** olarak ayırmak çoğu zaman değerlidir; burada χ = α + β + σ.
- **ρ (rho), kullanım oranı / trafik yoğunluğu = λ / μ:** en önemli tek özet. ρ < 1 kuyruğun boşaldığı, ρ ≥ 1 sınırsız büyüdüğü anlamına gelir.
- **Süreler:** teslim süresi (τ, başlangıçtan bitişe), iş süresi (φ, fiilî işleme), bekleme süresi (ω, askıda), ve adım süresi (θ, tamamlanmalar arası).
- **ε (epsilon), hata oranı:** başarısızlıklar ÷ toplam.

Başarısızlıkları ve *atlamaları* açıkça adlandırmak yazılımda önemlidir: terk edilen bir öğe (vazgeçen bir müşteri, geride bırakılan bir sepet, reddedilen bir iş bileti) hizmet edilmeden kuyruktan çıkar ve onu "hizmet edildi" saymak metriklerinizi bozar. **Çekinmeyi** (katılmamaya karar vermek), **vazgeçmeyi** (bekledikten sonra bırakmak) ve **kuyruk değiştirmeyi** (kuyruklar arasında geçmek) birinci sınıf sonuçlar olarak izleyin.

### Planlamayı Little Yasası'na çapalayın

Little Yasası, kararlı bir sistemdeki uzun vadeli ortalama öğe sayısının, ortalama varış hızı çarpı her öğenin sistemde geçirdiği ortalama süreye eşit olduğunu söyler: **κ = λ τ** (klasik olarak L = λW). Şaşırtıcı biçimde geneldir (varış dağılımı ya da hizmet sırası hakkında hiçbir varsayım gerektirmez); bu da onu akış planlamasının iş atı yapar. Yeniden düzenlendiğinde, size **teslim süresi = yarım kalan iş ÷ çıktı hızı** olduğunu söyler. Bu, kanbanın ve yalın düşüncenin matematiksel temelidir: daha kısa teslim süreleri istiyorsanız ve çıktı hızını artıramıyorsanız, WIP'i düşürmelisiniz. Ayrıca hızlı akıl sağlığı denetimleri de verir. 40 bilet açıksa ve günde 8 tanesini kapatıyorsanız, kimse ne kadar meşgul hissederse hissetsin, ortalama bilet yaklaşık 5 gün sürer. Tek şartı *kararlılıktır*: varışlar sürekli olarak ayrılışları aşmamalıdır (ρ < 1), yoksa kuyruk ve yasanın varsayımları çöker.

### Kullanım oranının doğrusal olmayışına saygı gösterin

Kuyruk kuramının en önemli operasyonel dersi, kullanım %100'e yaklaştıkça yanıt süresinin kademeli değil, keskin biçimde artmasıdır. Bob Wescott'ın *Seven insights into queueing theory* yazısı pratik sonuçları canlı biçimde yakalar:

1. Hizmet merkezi ne kadar yavaşsa, planlamanız gereken tepe kullanım oranı o kadar düşüktür.
2. Herhangi bir şeyin son %15'ini kullanmak çok zordur.
3. Kenara ne kadar yakın çalışırsanız, yanılmanın bedeli o kadar yüksektir.
4. Yanıt süresi büyümesi, kaç öğenin bekleyebileceğiyle sınırlıdır.
5. Bunlar ortalamadır, azami değerler değil: kuyruğa göre planlayın.
6. Birden çok hizmet merkezi boyunca insani inkâr etkisine dikkat edin.
7. Küçük iyileştirmeleri en iyi ışıkta gösterin.

Tasarım çıkarımı: **bilerek boşluk payı ayırın.** Gecikmeye duyarlı sistemlerde %70–80 kullanım hedeflemek israf değildir; öngörülebilir yanıt süresi satın almaktır. Bu, doğrudan kapasite planlamasını ve SLO'ları (bölüm 3.5 ve 9.1) bilgilendirir.

### Süreçleri kuyrukların kuyruğu olarak modelleyin

Gerçek iş aşamalardan akar ve çok aşamalı bir süreç, öğeleri her adımda kendileri de kuyruğa giren bir kuyruktan ibarettir. Onu böyle modelleyin: süreç varış hızı birinci aşamanın varış hızıdır; süreç başarı hızı son aşamanın başarı hızıdır; süreç hata ve atlama sayıları aşamaların toplamlarıdır. İki yaygın biçim tekrar eder:

- Öğe sayılarının her aşamada küçüldüğü **hunileri** (işe alım: erişim → görüşme → teklif; satın alma: göz atma → sepet → ödeme; teslimat: entegre et → UAT → üretim). En önemli aşamayı eniyileyin: huni tepesindeki varışları en üst düzeye çıkarın, huni ortasındaki atlamaları (sepet terki) en aza indirin ya da son aşama hatalarını (kötü üretim dağıtımları) en aza indirin.
- Bu kitabın Akış bölümünün doğrudan ele aldığı **çift elmas** keşif-ve-teslimat akışları (keşfet → tanımla → geliştir → teslim et) (bölüm 11.1).

**Kısıtlayıcı aşamayı** (darboğaz) bulmak ve rahatlatmak, akış iyileştirmesinin karşılığını verdiği yerdir; kısıt olmayanları eniyilemek yalnızca kuyruğu başka yere taşır.

### Kuyruk metriklerini takımların zaten kullandığı KPI'lara bağlayın

Kuyruk nicelikleri, bu kitabın başka yerlerindeki teslimat ve güvenilirlik metriklerine temiz biçimde eşlenir; kuramı akademik değil pratik kılan budur:

- "Kavramdan müşteriye" **teslimat teslim süresi (Dτ)**, bir teslim süresi (τ) ölçüsüdür ve bir DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) metriğidir (bölüm 11.2).
- **Dağıtım sıklığı (Dμ)** bir hizmet hızı ölçüsüdür.
- **Değişiklik başarısızlık oranı (Dε)** bir hata oranıdır.
- **Geri getirme süresi (Rτ)** bir geri getirme teslim süresidir, yani MTTR (bölüm 9.3).

Çeşitli **MTTR'leri** (ortalama *yanıt*, *onarım*, *kurtarma* ve *çözme* süresi) birbirinden ayırın; çünkü olay kuyruğunun farklı bölümlerini ölçerler ve rutin olarak birbirine karıştırılırlar. SLI/SLO/SLA'ları (bölüm 9.1) kuyruk terimleriyle temellendirmek, hedefleri dürüst ve karşılaştırılabilir tutar.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| **Sistemleri yüksek kullanımda çalıştırmak** | Birim başına daha düşük donanım/maliyet | Doğrusal olmayan gecikme patlamaları; ani artışlara kırılgan |
| **Cömert boşluk payı ayırmak** | Öngörülebilir gecikme; varyansa dayanıklı | Daha yüksek kararlı durum maliyeti; "az kullanılıyor" görünür |
| **WIP'i sınırlamak (kanban)** | Daha kısa teslim süreleri; daha az bağlam değiştirme | Daha yavaş hissettirir; sınırı tutmak disiplin gerektirir |
| **Biçimsel kuyruk modelleme** | Sayısallaştırılmış kapasite kararları; daha az sürpriz | Öğrenme eğrisi; modeller dağınık gerçekliği basitleştirir |
| **Yalnızca pratik kurallar** | Hızlı, matematik yok | Tam da en pahalı olduğu yerde (kapasiteye yakın) yanlış |

Yinelenen ödünleşim **verimlilik ile öngörülebilirlik** arasındadır: kullanımı yükseltmek, bir anda işe yaramayana kadar para tasarruf ettirir; o noktada gecikme, başarısızlık ve yangın söndürme maliyetleri tasarrufu bastırır. Kuyruk kuramının katkısı, o uçurumun *nerede* olduğunu söylemesidir; böylece ödünleşim bir kaza değil bir seçim olur.

## Takımınızla tartışılacak sorular

1. **Gecikmeye duyarlı her sistem için açık kullanım oranı hedefiniz nedir ve kim onayladı?** Boşluk payı, öngörülebilir gecikmenin bilinçli bir satın alımıdır; bu yüzden gelen yükün rastgele ne olduğunun bir kazası değil, belirtilmiş bir ilke olmalıdır. Yanıt süresi doğrusal olmayan biçimde arttığı için, %85'te çalışmak zaten yüksek kuyruk gecikmesi anlamına gelebilir; yine de finans boşluk payını israf olarak görür ve kullanımı yukarı iter. Sayıları getirin: mevcut kullanım, ölçülmüş gecikme eğrisi ve son gecikme olayınızın maliyeti, ardından her hizmet için uçurumun nerede durduğunu gösterin. Mevsimsel tepeleri olan (beyan sezonu, kayıt pencereleri) kurumsal ve kamu sistemlerinde, hedefi ortalamaya değil tepeye göre uçurumun uzağına koyun. Kullanım hedefinin sahibi yoksa, gecikme olayları "birdenbire" ortaya çıkmaya devam edecektir.

2. **Sistemlerinizin neresinde bir kuyruk sınırsız ve bunalınca yükü atacak karşı basınç yok?** Sınırsız bir kuyruk zarifçe başarısız olmaz; çökmeye doğru bozulur, çünkü varışların sürekli olarak ayrılışları aşması (rho >= 1) kuyruğun sınırsız büyümesi demektir. İleti kuyruklarınızın, iş parçacığı havuzlarınızın ve istek tamponlarınızın envanterini çıkarın ve her birinde varış hızı hizmet hızını aştığında ne olduğunu sorun: yükü mü atıyor, karşı basınç mı uyguluyor, yoksa çöküyor mu? Bu, bir aşağı akış sistemi doygunluğa ulaştığında hizmetler arasında zincirleme etki yapabilen kurumsal ölçekte keskin biçimde önemlidir. Bir kuyruğun biriktiği bir yük testi sonucunu ya da geçmiş bir olayı getirin ve sistemin fazla işi reddedip reddetmediğine ya da hepsini tutmaya çalışıp çalışmadığına bakın. Çözüm, Little Yasası'ndan türetilen zaman aşımları ve açık karşı basınçla sınırlı kuyruklardır; böylece aşırı yük devirmek yerine atar.

3. **Fikirden üretime akışınızı kuyrukların kuyruğu olarak modelliyor musunuz ve iyileştirmeleriniz gerçek kısıta mı yönelik?** Çok aşamalı bir süreç, öğeleri her aşamada kuyruğa giren bir kuyruktur ve kısıtlayıcı aşamadan başkasını eniyilemek kuyruğu yalnızca taşır. Teslimat huninizi haritalayın (entegre et'ten UAT'ye, üretime; ya da keşfet'ten tanımla'ya, geliştir'e, teslim et'e) ve işin gerçekte nerede yığıldığını bulmak için her aşamada varış, hizmet, bekleme ve atlama hızlarını ölçün. Takımlar rutin olarak darboğazı değil en iyi anladıkları aşamayı eniyiler; bu da emek harcar ve hiçbir şeyi oynatmaz. Hislerinizi değil, aşama başına bekleme süresi verisini getirin; çünkü darboğaz çoğu zaman bir çalışma durumu değil bir bekleme durumudur (gözden geçirme, onay, ortam kullanılabilirliği). Kısıtı öğrendiğinizde oraya yönelin ve kısıt olmayanları rahat bırakın.

4. **WIP sınırlarını belirlemek için Little Yasası'nı kullanıyor musunuz, yoksa yalnızca daha fazla disiplinin düzelteceği teslim sürelerini kapasite ekleyerek mi tedavi ediyorsunuz?** Little Yasası, teslim süresinin yarım kalan işin çıktı hızına bölümüne eşit olduğunu söyler; yani çıktı hızını artıramıyorsanız, daha kısa teslim süreleri için kalan tek kaldıraç, kendini tutmaktan başka bir şeye mal olmayan WIP'i düşürmektir. Karşıt çekim gerçektir: yarım kalan işi sınırlamak daha yavaş ve boş hissettirir ve baskı altındaki yöneticiler takımlara daha az başlayıp daha çok bitirmelerini söylemektense işe almayı ya da donanım satın almayı tercih eder. Sert sayıları getirin, aşama başına açık öğeler ve tamamlanma hızı, ve ima edilen ortalama teslim süresini hesaplayıp insanların inandığıyla karşılaştırın; açık genellikle büyük ve utandırıcıdır. Büyük bir kurumda ya da kurumda, teslim süresi düzeltmesi olarak gerekçelendirilen bir işe alım ya da tedarik talebi önce bu aritmetikle sınanmalıdır; çünkü WIP'i artıran bir kadro artışı, kısaltmak için tasarlandığı teslim sürelerini tam da uzatabilir.

5. **Kapasiteyi ortalamalara göre mi planlıyorsunuz, yoksa kuyruklarınızı gerçekten yaratan değişkenliği sayısallaştırdınız mı?** Kuyruklar ortalamadan değil varyanstan oluşur; bu yüzden aynı ortalama yüke sahip iki sistem, biri ani artışlı varışlara ya da uzun kuyruklu hizmet sürelerine sahipse tamamen farklı davranabilir. Gerilim şudur: ortalamaları toplamak kolaydır ve raporlaması rahatlatıcıdır; varyansı ve kuyruğu ölçmek daha zordur ve bir durum güncellemesinde istenmez. Ortalamayı değil dağılımı getirin: varış ani artışlılığı, 95. ve 99. yüzdelik hizmet ve bekleme süreleri ve işi ani artışlara yoğunlaştıran parti boyutları. Öngörülebilir dalgaları olan (beyan sezonu, maaş bordrosu çalıştırmaları, kayıt pencereleri, çeyrek sonu yükleri) kurumsal ve kamu sistemlerinde, tamponu ve kullanım hedefini tepe dönemi varyansına göre planlayın; çünkü yıllık ortalamaya göre boyutlandırılmış bir tasarım tam da halkın izlediği anda başarısız olur.

6. **Hangi kuyruklarınız terk edilmeleri ve reddedilmeleri iş hizmet edilmiş gibi sessizce sayıyor ve bu hangi karşılanmamış talebi gizliyor?** Çekinen, vazgeçen ya da reddedilen bir öğe ele alınmadan kuyruktan çıkar ve onu "hizmet edildi" olarak kaydetmek çıktı hızınızı, hata oranınızı ve kapasite planınızı aynı anda bozar. Rakip husus, "yanıtlanan çağrılar" ya da "kapatılan biletler"in bir panoda "vazgeçen arayanlar"dan daha iyi görünmesidir; bu yüzden dürüst sayı, kimsenin gönüllü olarak ortaya koymadığı sayıdır. Gerçek talep görünür olsun diye atlama hızını (σ), çekinme ve vazgeçme sayılarını ve sunulan yük ile hizmet edilen yük arasındaki farkı getirin. Bu, telefon kuyruğunu ya da bir yardım başvurusunu terk eden vatandaşların çözülmüş vakalar değil karşılanmamış yükümlülükler olduğu kamu hizmeti sunumunda keskin biçimde önemlidir; onları ele alınmış olarak raporlamak hem performansı yanlış gösterir hem de halka borçlu olunan kapasiteyi olduğundan az gösterir.

## Sektör merceği

**Girişim.** Biçimsel kuyruk modellemeye vaktiniz yok ve ihtiyacınız da yok. Önce en ucuz iki kazanıma uzanın: WIP'inizin ima ettiği gerçek teslim süresini görmek için Little Yasası'nı birikmiş işinize uygulayın ve var olmayabilecek bir darboğaza karşı işe almadan önce, işin yığıldığı aşamayı görmek için kanban panonuzu izleyin. Gecikmeye duyarlı her yolda kullanımı ayarlamak yerine boşluk payı bırakarak uçurumdan uzak tutun; çünkü bir büyüme sıçraması sırasındaki kesinti, biraz boş kapasiteden çok daha pahalıdır.

**Küçük işletme.** Kadroda kuyruk uzmanı olmadan, modelleri kurmak yerine metrikleri satın alın. Varış hızını, bekleme süresini ve terk edilmeyi zaten raporlayan bir yardım masası, ileti aracısı ya da barındırma platformu seçin ve bu sayıları türetmek yerine okuyun. Kararı iki belirtiyi izlemek olarak çerçeveleyin: meşgul oldukça doğrusal olmayan biçimde tırmanan beklemeler ve hizmet edilmeden vazgeçen müşteriler; çünkü kaybedilmiş bir müşteri, küçük bir işletmeyi en çok acıtan kuyruk maliyetidir.

**Kurumsal.** İş, kuyruk düşüncesini birçok takım arasında paylaşılan bir disiplin yapmaktır: üzerinde anlaşılmış tek bir gösterim (λ, μ, ρ, teslim süresi), tutarlı WIP ve kullanım-boşluk payı ilkeleri ve doygun bir aşağı akış sisteminin hizmetler arasında zincirleme etki yapmaması için karşı basınç standartları. SLO'ları ve kapasiteyi tahminle değil kuyruk analiziyle belirleyin ve kuyruklarınızı temel çizgiler ve gözden geçirmelerle bir portföy olarak yönetin; böylece hiçbir takım tek başına sıcak çalışmaz. Analizi kapasite yönetişimine ve denetime işleyin; böylece boşluk payı hedefi, birinin sahip olduğu belgelenmiş bir karar olur.

**Kamu.** Tedarik, şeffaflık ve kamusal hesap verebilirlik her kapasite seçimini şekillendirir. İletişim merkezlerini ve vatandaşa dönük sistemleri yıllık ortalamaya değil tepe dönemi varyansına (beyan sezonu, kayıt pencereleri) göre boyutlandırın ve talep sıçradığında kullanımı uçurumdan uzak tutacak şekilde kadrolayın. Çekinmeyi ve vazgeçmeyi "yanıtlanan çağrılar" içinde gizlemek yerine karşılanmamış kamusal talep olarak izleyin ve kapasite harcamasını, denetçilere ve seçilmiş yetkililere anekdot yerine savunulabilir, matematikle desteklenmiş bir dava veren Little Yasası bekleme süresi tahminleriyle gerekçelendirin.

## Örnekler

**Girişim.** Destek birikmiş işi altında boğulan beş kişilik bir SaaS takımı, bir temsilci daha işe almaları gerektiğini varsayar. Parayı harcamadan önce Little Yasası'nı uygularlar: 60 açık bilet ve günde 12 kapanan, ortalama bir biletin yaklaşık 5 gün beklediği anlamına gelir; bu da öfkeli e-postalarla örtüşür. Kanban panolarını izlerken biletlerin destekte değil mühendislikte beklediğini fark ederler; bu yüzden yarım kalan işi sınırlar ve hata raporlarını kuyruğa girmelerine izin vermek yerine doğrudan sprinte yönlendirirler. Teslim süresi yeni işe alım olmadan iki günün altına düşer ve serbest kalan bütçeyi gerçek darboğaza harcarlar.

**Kurumsal.** Yetkilendirme hizmetini boyutlandıran bir ödeme platformu λ ≈ 850 istek/saniye ve düğüm başına μ ≈ 200/saniye ölçer. Saf bir hesapla bu ~5 düğümdür (ρ = 0,85), ama ρ = 0,85'in zaten keskin biçimde yükselmiş kuyruk gecikmesi anlamına geldiğini bilen takım ρ ≈ 0,65'e göre kaynak ayırır ve uçuştaki istek sayılarını tahmin etmek ve kuyruk derinliklerini ve zaman aşımlarını belirlemek için Little Yasası'nı kullanır. Eskiden "birdenbire" ortaya çıkan yoğun sezon olayları kaybolur; çünkü takım artık eğrinin dik kısmında çalışmamaktadır.

**Kamu.** Bir vergi idaresinin iletişim merkezi, beyan sezonu desteğini bir kuyruk olarak modeller: varış sıçramaları (λ), temsilci kapasitesi (μ) ve en önemlisi uzun bekleyişlerden sonra vazgeçen vatandaşların **atlama hızı (σ)**. Yalnızca "yanıtlanan çağrılar" yerine çekinmeyi ve vazgeçmeyi izleyerek liderlik gerçek karşılanmamış talebi görür, tepelerde kullanımı uçurumdan uzak tutacak şekilde kadrolar ve ek kapasiteyi bekleme süresine dair Little Yasası tahminleriyle gerekçelendirir; bu, kamu harcaması için anekdotal olmayan, savunulabilir, matematikle desteklenmiş bir dava oluşturur.

## İş gerekçesi: motivasyonlar, YG ve TSM

Kuyruk kuramı iki pahalı hatayı önleyerek karşılığını verir: **aşırı kaynak ayırmak** (ihtiyacınız olmayan boş kapasite için ödemek) ve çok daha zararlısı, **uçurumun yakınında yetersiz kaynak ayırmak** (küçük yük artışlarının büyük gecikmeye, ihlal edilen SLA'lara, terk eden müşterilere ve acil harcamaya yol açtığı yer). %100 kullanıma yakın çalışmanın maliyeti doğrusal olmadığından, "biraz daha yük ekle"den elde edilen tasarruf küçük, olumsuz tarafı ise yıkıcıdır; biraz matematiğin bilinçli bir karara çevirdiği asimetri tam olarak budur. Getiri, önlenen kesintilerle, karşılanan SLA'larla, aksi hâlde çekinecek elde tutulan müşterilerle ve daha sakin nöbet dönüşümleriyle ölçülür.

**Toplam sahip olma maliyeti** açısından çerçeve benimsemesi ucuzdur (araç değil bilgidir) ve büyük bir kurumun bir sistemin ömrü boyunca verdiği hemen her kapasite, gecikme ve akış kararını iyileştirir. Little Yasası ve WIP sınırları bir şey satın almadan teslim sürelerini azaltır (saf bir süreç kazancı); kullanım disiplini ise mütevazı, öngörülebilir bir kararlı durum maliyetini pahalı, öngörülemez başarısızlıkların ortadan kalkmasıyla takas eder. Liderliğe gerekçeyi sunmak için yakın tarihli bir gecikme olayını kullanım eğrisine çevirin ve bir boşluk payı hedefinin onu nasıl önleyeceğini gösterin; WIP azaltımını doğrudan daha hızlı teslimata bağlamak için Little Yasası'nı kullanın.

## Anti-kalıplar ve tuzaklar

- **Kapasiteyi ortalamalara göre planlamak:** kuyrukları gerçekten yaratan varyansı görmezden gelmek.
- **Sıcak çalışmak:** gecikmeye duyarlı sistemlerde %90+ kullanımı hedeflemek ve kuyruk gecikmesine şaşırmak.
- **Atlamaları hizmet saymak:** terk eden müşterileri ya da reddedilen biletleri ele alınmış saymak ve metrikleri bozmak.
- **WIP yığmak:** meşguliyeti çıktı hızıyla karıştırmak ve teslim sürelerini uzatmak.
- **Darboğaz olmayanı eniyilemek:** kısıt olmayan aşamaları iyileştirmek ve kuyruğu başka yere taşımak.
- **MTTR'leri karıştırmak:** "onarım" ölçerken "kurtarma" raporlamak ya da tersi.
- **Sınırsız kuyruklar:** karşı basınç yok, bu yüzden aşırı yüklenmiş bir sistem yükü atmak yerine çökmeye doğru bozulur.
- **Ortalamaları azami değer saymak:** ortalamaya göre tasarlamak ve kuyruk yüzünden çağrılmak.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Kuyruklar (biletler, görevler, iletiler, dağıtımlar) yönetilmez ve tepkiseldir; kapasite tahmin edilir; kullanım yük nereye düşerse orada çalışır; gecikme sorunları takımı şaşırtır ve sonradan yangın söndürülerek ele alınır.
- **Düzey 2, Geliştirme:** Birkaç takım temel metrikleri (çıktı hızı, ortalama bekleme) toplar ama bunları ortalama olarak okur ve tutarsız uygular; bazı gruplar WIP'i sınırlar ya da boşluk payı bırakırken diğerleri sıcak çalışır; ortak gösterim yoktur, bu yüzden uygulamalar takımlar arasında taşınmaz.
- **Düzey 3, Standartlaştırma:** Ortak bir gösterim (λ, μ, ρ, teslim süresi) belgelenir ve kurum genelinde uygulanır; WIP sınırları ve kullanım-boşluk payı hedefleri her gecikmeye duyarlı sistem için bilerek belirlenir; çeşitli MTTR'ler ayırt edilir; karşı basınçlı sınırlı kuyruklar hizmetler genelinde varsayılandır.
- **Düzey 4, Yönetme:** Kuyruklar temel çizgilere karşı ölçülür ve kontrol edilir: varış hızı, hizmet hızı, kullanım oranı, kuyruk gecikmesi (p95/p99) ve teslim süresi tanımlı hedefler ve SLO'lar doğrultusunda izlenir; kuyruk derinlikleri, zaman aşımları ve boşluk payı tahmin edilmek yerine Little Yasası'ndan türetilir; çekinme, vazgeçme ve atlama hızı sayılır, böylece sunulan yük hizmet edilen yükten ayırt edilir; kapasite kararları his değil bu kanıta göre gözden geçirilir.
- **Düzey 5, Orkestrasyon:** Akış sürekli olarak kuyrukların kuyruğu olarak modellenir; darboğazlar süregelen bir uygulama olarak belirlenir ve rahatlatılır; kapasite, SLO'lar ve karşı basınç değişen talebe ve varyansa uyum sağlar; kuyruk metrikleri doğrudan DORA ve iş KPI'larına bağlanır ve kurum, yük ve risk tablosu değiştikçe kapasiteyi bütün akış boyunca yeniden dengeler.

## Tartışma fikirleri

1. Gecikmeye duyarlı sistemleriniz gerçekte hangi kullanım oranında çalışıyor ve uçurumları nerede?
2. Little Yasası'nı mevcut birikmiş işinize uygulayın: WIP ÷ çıktı hızınız hangi teslim süresini ima ediyor ve bu gerçekle örtüşüyor mu?
3. Hangi kuyruklarınız "atlamaları" (terkleri, reddedilenleri) sanki hizmet edilmiş gibi sessizce sayıyor?
4. WIP'i düşürmek, nerede kapasite eklemekten daha ucuza teslim süresini kısaltırdı?
5. Fikirden üretime akışınızdaki hangi aşama gerçek darboğaz ve iyileştirmeleriniz oraya mı yönelik?
6. Panolarınız, sizi asıl acıtan şey kuyruk olduğunda ortalamaları mı gösteriyor?

## Önemli çıkarımlar

- Müşteri kuyrukları, kanban panoları, ileti kuyrukları ve dağıtım hatları aynı yasalarla yönetilen kuyruklardır.
- **Little Yasası (κ = λτ)** akış planlamasını çapalar: teslim süresi = WIP ÷ çıktı hızı.
- Kullanım oranı ve bekleme süresi **doğrusal değildir**: boşluk payı ayırın; son %15 en pahalı olanıdır.
- Bütün resmi izleyin: varışlar, hizmet, başarılar, **başarısızlıklar ve atlamalar** ve beklemeler; terkin gizlenmesine izin vermeyin.
- Süreçleri **kuyrukların kuyruğu** olarak modelleyin ve meşguliyeti değil **darboğazı** düzeltin.
- Kuyruk metrikleri doğrudan **DORA/akış** ve **SLI/SLO** ölçülerine eşlenir (bölüm 11.1, 11.2, 9.1) ve bütün kuruma kapasite ve akış için tek bir dil verir.

## Kaynaklar ve ileri okuma

- Bob Wescott, *Seven Insights into Queueing Theory* (and *The Every Computer Performance Book*).
- John D. C. Little, "A Proof for the Queuing Formula L = λW" (1961): Little's Law.
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate*: flow-based DORA metrics that align with queue KPIs.
- Donald Reinertsen, *The Principles of Product Development Flow*: queues, batch size, and WIP economics.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability*: Little's Law applied to kanban.
- Joel Parker Henderson, *Queueing Theory*: notation, KPIs, and queue-of-queues (github.com/joelparkerhenderson/queueing-theory).
- Dan Slimmon, "The most important thing to understand about queues" (2016).
- Wikipedia: "Queueing theory," "M/M/1 queue," "Little's law," "Markov chain."
