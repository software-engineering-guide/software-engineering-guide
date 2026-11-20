# 7.9 Ana veri ve referans veri yönetimi

## Genel bakış ve motivasyon

Beş sisteme kurumun kaç müşterisi olduğunu sorun, beş farklı sayı alırsınız. Biri e-posta adreslerini sayar, biri sözleşmeleri, biri oturum açmaları sayar ve ikisi "Acme Corp" ile "ACME Corporation"ın aynı şirket olup olmadığı konusunda anlaşamaz. [Ana veri yönetimi](https://en.wikipedia.org/wiki/Master_data_management) (MDM), işinizin paylaştığı çekirdek varlıkları (müşteri, ürün, tedarikçi, çalışan, konum) her sistemin güvenebileceği tek bir yetkili sürümde uzlaştırma disiplinidir.

Verinizi üç türe ayırarak başlayın, çünkü her biri farklı muamele ister. Ana veri, işinizin isimlerini tanımlar: birçok sürecin atıfta bulunduğu kişiler, yerler ve şeyler. Referans veri, bu süreçlerin kullandığı denetimli sözlüktür: para birimi kodları, ülke kodları, ölçü birimi listeleri, ürün kategorileri. İşlem verisi ise fiilleri kaydeder: verilen bir sipariş, yapılan bir ödeme, gönderilen bir sevkiyat. Ana ve referans veri işlemlerden daha düşük hacimlidir ama her yerde atıfta bulunulur; bu yüzden içlerindeki bir hata aşağı akıştaki her şeyi kirletir.

Bunu yanlış yapmanın maliyeti somuttur. Aynı müşteri dört biraz farklı kayıt olarak bulunduğunda dört katalog postalarsınız, saklanmaya değer tek bir ilişkiyi göremezsiniz ve müşteri başına gelir rakamınız sessizce yanlıştır. Birçok kaynaktan bir araya getirilmiş bir varlığın tek güvenilir sürümü olan [altın kayıt](https://en.wikipedia.org/wiki/Single_source_of_truth), bu çelişen kopyaların yerini alır; böylece her entegrasyon aynı eşleştirme sorununu yeniden çözmeyi bırakır.

On yıllarca büyüme ve satın almalarla birikmiş sistemleri uzlaştıran kurumsal yapılar için MDM, tutarlı bir müşteri görünümü ile kalıcı bir uzlaştırma vergisi arasındaki farktır. Kamu için bahisler yükselir: üç kurumda üç farklı kişi olarak görünen bir vatandaş bir yardımdan mahrum bırakılabilir, iki kez vergilendirilebilir ya da daireler arasında kaybolabilir. Bu bölüm; sahipliği ve politikayı belirleyen veri stratejisi ve yönetişimi (bölüm 7.1), varlıkların ne anlama geldiğini tanımlayan veri modelleme ve anlamsal katman (bölüm 7.7) ve kayıtları zaman içinde temiz tutan veri kalitesi ve gözlemlenebilirliği (bölüm 7.8) tamamlar.

## Temel ilkeler

- Verinizi ana, referans ve işlem verisi olarak ayırın; her biri farklı ele alınır.
- Gerçek dünyadaki her varlık için bir altın kayıt, kazara keşfedilmeyip bilinçli olarak oluşturulmuş.
- Bir MDM mimari stilini modaya göre değil, kontrol ve gecikme ihtiyaçlarınıza uygun seçin.
- Eşleştirme ve hayatta kalma (survivorship) iş kurallarıdır; bunları yazın ve sorumluların (steward) ayarlamasına izin verin.
- Referans veri paylaşılan sözlüktür; onu bir API gibi sürümleyin ve yayımlayın.
- Yönetişim ve sorumluluk MDM'nin motorudur; yazılım yalnızca araçtır.
- Altın kayıtları olay olarak yayın ki aşağı akış sistemleri eskimesin, senkron kalsın.
- MDM'yi yüklenen kayıtlarla değil, iyileşen kararlar ve kaldırılan yinelemelerle ölçün.

## Öneriler

### Önce ana, referans ve işlem verisini sınıflandırın

Sıralamadığınız şeyi yönetemezsiniz; bu yüzden veri alanlarınızı sınıflandırarak başlayın. Ana veri için yararlı bir sınama, yanlış bir değerin yayılıp yayılmadığıdır: tek bir kötü adres faturalamaya, sevkiyata ve yasal tebligatlara dalga dalga yayılıyorsa ana veriye bakıyorsunuz demektir. Bu, yatırımınızı yönlendirir: sipariş kalemleri için değil, müşteri varlığı için bir eşleştirme motoru kurarsınız. Alanları açıkça adlandırın, yinelenmenin yol açtığı acıya göre sıralayın ve en çok acıtan bir ya da ikisiyle başlayın; genellikle müşteri ve ürün, çünkü doğrudan gelire dokunurlar.

### Bir MDM mimari stilini bilinçli seçin

Dört yaygın mimari stil vardır ve doğrusu, ne kadar yetkiyi merkezileştirebildiğinize ve değişikliklerin ne kadar hızlı yayılması gerektiğine bağlıdır. Kayıt defteri (registry) stili veriyi kaynak sistemlerde bırakır ve yalnızca eşleşmiş tanımlayıcılardan oluşan bir dizin kurar; böylece hiçbir veriyi taşımadan "bu beş kayıt aynı müşteridir" diyebilir. Ucuz ve düşük risklidir, ama salt okunurdur, dolayısıyla kaynakları düzeltemez. Birleştirme (consolidation) stili kopyaları merkezi bir merkeze çeker ve raporlama için altın kayıtlara birleştirir, ama düzeltmeleri geri itmez; kaynaklar dağınık kalır. Bir arada var olma (coexistence) stili daha da ileri gider: temizlenmiş değerleri kaynak sistemlere geri eşitler, böylece kaynaklar bağımsız çalışmaya devam ederken zamanla iyileşir. Merkezi ya da işlemsel merkez stili, MDM merkezini kayıt sisteminin kendisi yapar: varlıklar doğrudan orada oluşturulur ve düzenlenir, diğer tüm sistemler ondan tüketir. Bu en güçlü tutarlılığı ve kontrolü verir ve işin nerede yapıldığını değiştirdiği için benimsemesi en zor olanıdır. Birçok kurum, değer kanıtlayan bir kayıt defterinden başlayıp güven arttıkça bir arada var olmaya doğru ilerler ve farklı alanlarda birden fazla stili birlikte çalıştırır.

### Eşleştirme, birleştirme ve hayatta kalma kurallarını açıkça belirleyin

MDM'nin kalbi, iki kaydın aynı gerçek dünya şeyini ne zaman tanımladığına karar vermektir. Bu, [kayıt eşleştirmedir](https://en.wikipedia.org/wiki/Record_linkage) ve gerçek veri yazım hataları, kısaltmalar ve eksik alanlarla dolu olduğundan nadiren tam bir anahtar eşleşmesi kadar basittir. Deterministik eşleştirme, seçilen alanlarda kesin kurallar kullanır (aynı vergi numarası ya da aynı e-posta artı posta kodu). Olasılıksal eşleştirme, [yaklaşık dize eşleştirme](https://en.wikipedia.org/wiki/Approximate_string_matching) ve ağırlıklarla birçok alan boyunca benzerliği puanlar; böylece "Bob Smith, 12 Main St" ile "Robert Smith, 12 Main Street" bir eşiğin üzerinde büyük olasılıkla eşleşme sayılabilir. Hangi kayıtların aynı varlığa atıfta bulunduğuna karar vermeye kimlik çözümleme denir ve müşteri görünümlerinden sahtecilik tespitine kadar her şeyi besler.

Kayıtlar eşleştikten sonra hangi değerlerin altın kayda geçeceğine karar vermelisiniz. Bu hayatta kalma kuralları iş mantığıdır; bu yüzden onları açık yapın: telefon numarası için en yeni değeri, adres için en eksiksiz değeri, yasal ad için en güvenilir kaynağı tercih edin. Eşleşmelerin otomatik birleştirildiği bir eşik bandı, otomatik reddedildiği daha düşük bir bant ve bir insanın karar verdiği orta bir bant belirleyin; sorumluluğun (stewardship) yaşadığı yer burasıdır. Her birleştirmeyi geri alınabilir ve günlüklü tutun, çünkü iki gerçek müşteriyi kaynaştıran yanlış bir birleştirme, kaçırılan bir birleştirmeden daha kötüdür.

### Referans veriyi sürümlü paylaşılan sözlük olarak ele alın

Referans veri, sistemlerinizin konuştuğu paylaşılan sözlüktür ve kayan bir sözlük sessiz uyumsuzluğa yol açar: bir sistem ISO ülke kodu "GB" kullanırken diğeri "UK" kullandığında birleştirmeler başarısız olur ve sayımlar ayrışır. Her referans listesini tek bir yönetilen yerde tutun, her tüketici için yayımlayın ve en önemlisi sürümleyin. Kodlar zaman içinde eklenir, kullanımdan kalkar, bölünür ve birleştirilir; listeyi yerinde üzerine yazarsanız eski kodlar altında doğru olan geçmiş raporları bozarsınız.

Bir referans veri kümesine sözleşmesi olan bir API gibi davranın. Onu yürürlük tarihleriyle yayımlayın ki bir tüketici "bu tarihte geçerli bölge kodları nelerdi" diye sorabilsin, kullanımdan kalkan kodları silmek yerine saklayın ve bir kodun anlamı değiştiğinde eşlemeyi kaydedin. Var olduklarında tanınmış dış standartları tercih edin; ISO ülke ve para birimi kodları gibi, çünkü standartlar size birlikte çalışabilirliği bedavaya verir ve bölüm 3.8'deki açık standartlar disipliniyle bağlanır.

### Yalnızca düz kayıtları değil, hiyerarşileri ve ilişkileri de modelleyin

Ana veri bağımsız satırlardan oluşan bir yığın değil, bir ilişkiler ağıdır. Bir müşteri bir haneye ve bir kurumsal ana şirkete aittir. Bir ürün bir kategoriye ve bir markaya toplanır. Bu hiyerarşiler gerçek iş anlamı taşır: satışları kurumsal ana şirkete göre topladığınızda manzara, tek tek hesaba göre toplamaya kıyasla tamamen değişir. Bu ilişkileri açıkça modelleyin ki tüketiciler onlarda tutarlı biçimde gezinsin; her takım kendi toplama yöntemini icat etmesin.

Bir varlığın aynı anda birkaç hiyerarşiye ihtiyaç duyduğu duruma dikkat edin. Bir ürün finans için bir biçimde, ürün yönetimi (merchandising) için başka bir biçimde toplanabilir ve ikisi de meşrudur; bu yüzden tek bir gerçek ağaç dayatmak yerine birden fazla adlandırılmış hiyerarşiyi destekleyin. Alanlar arası ilişkiler de önemlidir, hangi tedarikçinin hangi ürünü sağladığı gibi.

### Altın kayıtları anlamsal katmana ve veri kalitesine bağlayın

MDM'nin ürettiği altın kayıtlar, bölüm 7.7'nin anlamsal katmanının ölçütleri tanımlarken atıfta bulunduğu güvenilir varlıklardır: "aktif müşteriler" ancak "müşteri" belirsiz olmadığında bir şey ifade eder. Altın kayıtlarınızı anlamsal katmana besleyin ki her ölçüt aynı tekilleştirilmiş, çözümlenmiş varlıkları saysın.

MDM ve veri kalitesi (bölüm 7.8) aynı madalyonun iki yüzüdür: kalite denetimleri MDM'nin sonra çözdüğü yinelemeleri, boşlukları ve biçim ihlallerini bulur; MDM'nin eşleştirmesi ise denetimlerin kaçırdığı kalite sorunlarını yüzeye çıkarır. Ana verinize özel olarak sürekli kalite izlemesi çalıştırın: yineleme oranları, eşleşme güven dağılımları, anahtar alanların bütünlüğü (eksiksizliği) ve inceleme kuyruğunun boyutu; böylece kayma tüketiciler görmeden önce yüzeye çıkar.

### Altın kayıtları olaylarla yayın

Hiçbir aşağı akış sisteminin görmediği bir altın kayıt kimseye yardım etmez. En güçlü kalıp olay güdümlü yayılmadır: bir varlık oluşturulduğunda, birleştirildiğinde ya da düzeltildiğinde MDM merkezi bir değişiklik olayı yayımlar ve abone sistemler yerel kopyalarını günceller. Bu, [olay güdümlü mimariye](https://en.wikipedia.org/wiki/Event-driven_architecture) ve bölüm 7.2'nin akış kalıplarına dayanır; herkesi bir gün eskimiş bırakan kırılgan gece toplu eşitlemeleri olmadan onlarca sistemi tutarlı tutar.

Olayları yararlı olacak kadar bağlamla yayımlayın: varlık tanımlayıcısı, neyin değiştiği, yeni hayatta kalan değerler ve tüketicilerin güncellemeleri sıralayıp kaçırdıklarını fark edebilmesi için bir sürüm. Tüketicileri eş güçlü yapın ki bir olayı yeniden oynatmak zarar vermesin ve abone olamayan sistemler için bir API sunun. Veri mimarisi ve depolama (bölüm 3.4) ilkesi burada da geçerlidir: altın kaydın akması için tasarlayın, çünkü kimsenin tüketmediği altın kayıt, pahalı bir elektronik tablodan ibarettir.

### Araçlardan önce sorumluluk ve yönetişimi atayın

MDM bir teknoloji projesi olarak başarısız olur, bir yönetişim projesi olarak başarılı olur. Kritik rol, belirli bir alanın kalitesinden ve kurallarından sorumlu olan, belirsiz eşleşmeleri çözen, hayatta kalma kurallarını ayarlayan ve iki departman "tedarikçi"nin ne demek olduğu konusunda anlaşamadığında hakemlik eden [veri sorumlusudur](https://en.wikipedia.org/wiki/Data_steward) (data steward). Sorumlular genellikle mühendis değil, derin alan bilgisine sahip iş insanlarıdır ve gerçek yetkiye ve ayrılmış zamana ihtiyaç duyarlar; çünkü yetkisiz yarı zamanlı sorumluluk, MDM'nin durdurmak için var olduğu kaymayı tam olarak üretir.

Sorumluları bölüm 7.1'deki yönetişim yapılarıyla çevreleyin: her alandan sorumlu bir veri sahibi, alanlar arası anlaşmazlıkları çözecek bir konsey ve ana kayıtları kimin oluşturup birleştirebileceğine dair net politikalar. Kararları belgeleyin, çünkü bir müşteriyi eşleştirme kuralları, personel değişimini atlatması gereken kurumsal bilgidir. Araçlar yönetişime hizmet eder; sorumlularınızı adlandırmadan bir MDM platformu satın almak, sürücüsüz bir motor satın almaktır.

## Ödünleşimler: artılar ve eksiler

| MDM stili | Artılar | Eksiler |
|---|---|---|
| Kayıt defteri (yalnızca dizin) | Ucuz, düşük risk, kaynaklara dokunulmaz | Salt okunur; kaynak veriyi düzeltemez |
| Birleştirme (merkezi kopyalar) | Analitik için hızla temiz kayıtlar | Kaynaklar dağınık kalır; geri yazma yok |
| Bir arada var olma (kaynaklara geri eşitleme) | Kaynaklar iyileşir; dengeli kontrol | Daha fazla entegrasyon; yönetilecek eşitleme çakışmaları |
| Merkezi / işlemsel merkez | En güçlü tutarlılık ve kontrol | En yüksek maliyet; işin yapıldığı yeri değiştirir |
| Deterministik eşleştirme | Öngörülebilir, açıklanabilir, denetlenebilir | Yazım hatalarını, varyantları ve dağınık veriyi kaçırır |
| Olasılıksal eşleştirme | Gerçek dünya çeşitliliğini yakalar | Ayar gerektirir; dikkatsizce yapılırsa yanlış birleştirmeler |

MDM'deki temel gerilim kontrol ile aksama arasındadır. Size en temiz ve en tutarlı veriyi veren stiller (bir arada var olma ve merkezi merkezler), tam da kaynak sistemlerin ve sahiplerinin çalışma biçimine en çok müdahale edenlerdir ve MDM programlarının tıkandığı yer bu müdahaledir. Pratik yol, düşük riskli bir stille güven kazanmak ve yalnızca iş gerekçesinin net olduğu yerde daha güçlü kontrole doğru ilerlemektir. Eşleştirme ödünleşimi paralel işler: deterministik kurallar denetlenebilirdir ama kırılgandır; olasılıksal puanlama güçlüdür ama sorumluluk ve ara sıra yanlış birleştirmeye hoşgörü gerektirir. Olgun programların çoğu ikisini harmanlar.

## Takımınızla tartışılacak sorular

1. **Hangi ana veri alanları bize gerçekten acı çektiriyor ve bunları hepsiyle birden uğraşmak yerine maliyete göre sıraladık mı?** Birçok MDM programı kendi hırsının altında çöker: kurumdaki her varlığı bir anda ana veri yapmaya çalışır ve iki yıl boyunca hiçbir şey teslim etmez. Verimli hamle, yinelenme ve çelişkinin size gerçek para ya da güven kaybettirdiği bir ya da iki alanı (genellikle müşteri ya da ürün) bulmak ve bu maliyeti sayıya dökmektir: boşa giden postalar, uzlaştırma saatleri, yanlış gelir rakamları, denetim bulguları. Aynı varlığın sistemleriniz boyunca birden çok biçimde göründüğüne dair somut örnekler getirin ve nereden başlayacağınızı bu sıralamanın söylemesine izin verin; çünkü dar ve ölçülebilir bir kazanım, genişlemek için gereken itibarı kurar.

2. **Her ana veri alanının sahibi kim ve sorumlularımızın işi gerçekten yapacak yetkisi ve zamanı var mı?** Yetkilendirilmiş sorumluluk olmadan MDM aracı, sürücüsüz bir arabadır ve en yaygın başarısızlık biçimi, bir slaytta bir sorumlu adlandırıp ona gerçek bir yetki ve ayrılmış saat vermemektir. Belirsiz eşleşmeleri çözen ve "müşteri sayılan nedir" anlaşmazlıklarını yatıştıran insanların alan uzmanlığına, karar yetkisine ve korunan zamana ihtiyacı vardır. Organizasyon şemanızı getirin ve en önemli alanınız için iki kaydın aynı kişi olup olmadığına tam olarak kimin karar verdiğini ve satış ile finans anlaşamadığında kimin hakemlik ettiğini sorun. O kişiyi adlandıramıyor ve ayrılmış zamanını gösteremiyorsanız, programı batıracak boşluğu bulmuşsunuz demektir.

3. **İki kaydı bir altın kayıtta birleştirdiğimizde kararı açıklayabilir ve geri alabilir miyiz, hayatta kalan değerler nereden geliyor?** Hayatta kalma kuralları çoğu takımın hiç yazmadığı iş mantığıdır; bu da birleştirmelerin yükleme sırası ya da araç varsayılanları kazasıyla gerçekleştiği, iki gerçek müşteriyi kaynaştıran yanlış bir birleştirmenin geri alınmasının acı verici olduğu anlamına gelir. Gerçek bir birleştirilmiş kayıt getirin ve her hayatta kalan alanı kaynağına ve kuralına kadar izleyin: neden bu adres, neden bu ad, neden bu telefon numarası. Her birleştirmenin günlüklendiğini ve geri alınabildiğini, belirsiz eşleşmelerden oluşan orta bandın otomatik birleştirilmek yerine bir insana gittiğini doğrulayın. Belirli bir altın kaydı açıklayamıyorsanız, sorumlularınız onu bir denetçiye ya da haksızlığa uğramış bir müşteriye karşı savunamaz.

4. **Her ana veri yapmayı planladığımız alan için hangi MDM mimari stili uygun ve bu seçimi kaynak sistem sahiplerine yüklediği aksamaya karşı savunabilir miyiz?** Seçtiğiniz stil, veriyi ne kadar temizleyebileceğinizi ve kaynakların sahibi takımlara ne kadar müdahale edeceğinizi belirler; kontrol ve aksama gerçeğine göre değil, moda ya da satıcı sunumuna göre seçmek programların yarı yolda tıkanmasının yoludur. Bir kayıt defteri değeri ucuza kanıtlar ama bir kaynağı asla düzeltmez; merkezi bir merkez en güçlü tutarlılığı verir ama kayıtların oluşturulduğu yeri taşır; bu, teknik kılığına girmiş örgütsel bir değişikliktir. Her aday alan için kaynak sahipleri üzerinde gerçekte ne kadar yetkiniz olduğuna, aşağı akış kopyalarının ne kadar taze olması gerektiğine ve bir geri yazmanın mevcut iş akışlarında neyi bozacağına dair dürüst bir okuma getirin. Kurumsal ve kamu ortamlarında kayıt sistemini taşımanın geçiş ve değişim yönetimi maliyetini ekleyin; çünkü günlük işleri taşınan takımlar, kendilerine danışılmayan bir merkeze direnir ve tıkanmış bir bir arada var olma kurulumu, yayına çıkan mütevazı bir kayıt defterinden daha pahalıdır.

5. **Eşleştirme eşiklerini nasıl ayarlıyoruz ve her alanda hangi yanlış birleştirme ve kaçırılan eşleşme oranıyla yaşayabileceğimiz konusunda anlaştık mı?** Her olasılıksal eşleştirme motoru, yanlış birleştirmeleri (iki gerçek varlığı kaynaştırmak) kaçırılan eşleşmelerle (tek bir varlığı bölünmüş bırakmak) takas eder ve denge, araçta birinin bıraktığı bir varsayılan değil, bir iş kararıdır. Otomatik birleştirme ve otomatik reddetme bantlarını çok geniş ayarlarsanız altın kayıtları sessizce bozarsınız; çok dar ayarlarsanız insan inceleme kuyruğu sorumluların temizleyebileceğinden hızlı büyür. Mevcut güven dağılımını, inceleme kuyruğunun boyutunu ve yaşını ve her iki türden örnek hataları getirin ki oda her yönün gerçek maliyetini görsün. Bir kamu kimlik alanında kaçırılan eşleşmeye ve insan incelemesine ağır biçimde yönelin; çünkü yanlış bir birleştirme bir yardımı engelleyebilir ya da bir vatandaşın verisini bir başkasına ifşa edebilir ve bu hatanın itiraz ve denetim maliyeti, bir sorumlunun gelecek hafta çözeceği bir yinelemenin maliyetini cüceleştirir.

6. **Aşağı akış sistemleri bir altın kaydın değiştiğini nasıl öğreniyor ve bir karar yanlış gitmeden önce her biri ne kadar eski olabilir?** Hiçbir sistemin tüketmediği, mükemmel çözümlenmiş bir altın kayıt pahalı bir elektronik tablodur ve yayılma mekanizması (değişiklik olayları, bir abonelik API'si ya da gece toplu işi) her bağımlı kararın ne kadar güncel olduğunu sessizce belirler. Olay güdümlü yayılma onlarca tüketiciyi neredeyse gerçek zamanlı tutar ama eş güçlü tüketiciler ve sürümlü olaylar ister; gece eşitlemesi daha basittir ama herkesi bir gün eskimiş bırakır; bu bir pazarlama listesi için sorun olmayabilir ama bir sahtecilik denetimi için tehlikelidir. Tüketen sistemlerin listesini, her birinin gerçekte ihtiyaç duyduğu tazeliği ve bir güncellemeyi kaçıran bir tüketicinin bugün nasıl toparlandığını getirin. Büyük ya da kamusal bir kurumda bu olayların sözleşmesinin kimde olduğunu ve bir abonenin düşen bir mesajı nasıl fark ettiğini adlandırın; çünkü bir kuruma sessizce ulaşamayan bir varlık değişikliği, MDM'nin ortadan kaldırmak için fonlandığı parçalanmayı yeniden yaratır.

## Sektör merceği

**Girişim.** Bir avuç mühendisle ve boşa harcayacak zaman olmadan bir MDM platformu satın almayın. Rakamlarınızı bozan tek varlığı ana veri yapın; genellikle self servis ile satış arasında yinelenen müşteri, zaten çalıştırdığınız ambarda bir eşleştirme işiyle ve belirsiz eşleşmeleri haftalık gözden geçiren tek bir kişiyle. Her birleştirmeyi günlüklü ve geri alınabilir tutun ki kötü bir kural bir müşteri ilişkisine değil, bir öğleden sonraya mal olsun; daha ağır araçlara yalnızca elle inceleme kuyruğu tek bir incelemecinin kapasitesini aştığında yeniden bakın.

**Küçük işletme.** Veri sorumlunuz yok ve bütçeniz dar; bu yüzden bunu inşa etme değil satın alma kararı olarak ele alın ve bedavaya aldığınız standartlara yaslanın. Bakımını yapamayacağınız özel bir merkez yerine kişileri zaten tekilleştiren ve ISO ülke ve para birimi kodlarını konuşan araçları tercih edin ve yinelemelerin size gerçek para kaybettirdiği tek alanı seçin; genellikle müşteriler ya da ürünler. Sorumluluğu, bir kişinin haftasının küçük bir kısmı bile olsa adı belli bir sahibe atayın; çünkü kimsenin izlemediği yerde kayan sözlük, raporlarınızı sessizce bozan şeydir.

**Kurumsal.** Satın almalarla birikmiş bir düzine ERP ve CRM sistemi boyunca iş, portföy yönetişimidir: alanları yinelenmelerinin maliyetine göre sıralayın, iş tarafında yetkilendirilmiş sorumlular kurun ve hayatta kalma kurallarını ile referans veri sürümlemeyi standartlaştırın ki gruplar aynı eşleştirme sorununu yeniden çözmeyi bıraksın. Entegrasyon ve kalıcı sorumluluk maliyetini açıkça bütçeleyin, altın kayıtları sürümlü olaylar olarak yayın ki kaynaklar zamanla iyileşsin ve MDM'yi tek seferlik bir temizlik olarak değil, yineleme oranları ve inceleme kuyruğu ölçütleriyle ölçülen bir program olarak yönetin.

**Kamu.** Tedarik kuralları, katı veri paylaşımı yasası ve kamusal hesap verebilirlik her seçimi şekillendirir. Kişi varlığını yönetilen bir ulusal tanımlayıcıya bağlayın, referans veriyi yürürlük tarihine göre sürümleyin ki geçmiş kayıtlar doğru kalsın ve kimlik çözümlemeyi bilerek muhafazakâr yapın: belirsiz eşleşmeler eğitimli sorumlulara gider, asla otomatik birleştirmelere değil; çünkü yanlış bir birleştirme bir yardımı engelleyebilir ya da bir vatandaşın verisini başkasına sızdırabilir. Her eşleşmeyi denetim ve itiraz için günlükleyin, satıcılardan veri taşınabilirliği ve açıklanmış eşleştirme mantığı talep edin ve tüm yeteneği kamu sektörünün zaten taahhüt ettiği birlikte çalışabilirlik standartlarının içinde tutun.

## Örnekler

**Girişim.** Hızla büyüyen bir yazılım şirketi hem self servis kayıt hem de bir satış takımıyla satış yapar ve iki kanal aynı müşteriyi biraz farklı şirket adlarıyla iki kez oluşturur. Hesap başına gelir yanlış görünür ve satış takımı mevcut kullanıcıları soğuk aramaya devam eder. Ağır bir platform almak yerine hafif bir kayıt defteriyle başlarlar: veri ambarlarında kayıtları e-posta alan adı ve normalleştirilmiş şirket adıyla bağlayan bir eşleştirme işi ve belirsiz eşleşmeleri haftalık gözden geçiren yarı zamanlı tek bir sorumlu. Maliyeti düşüktür, raporlama hatasını düzeltir ve büyüdükçe daha fazla yatırımı haklı çıkaran değeri kanıtlar.

**Kurumsal.** Küresel bir üretici satın almalarla büyümüştür ve her biri kendi tedarikçi kayıtlarına sahip bir düzine ERP ve CRM sistemi çalıştırır; böylece aynı tedarikçi on beş biçimde görünür ve şirket tek bir alıcı olarak pazarlık edemez ya da gerçek harcamasını göremez. Tedarikçi ve ürün alanları için bir arada var olma stilinde bir MDM merkezi kurar; vergi ve sicil tanımlayıcılarında deterministik eşleştirme ve adlar ile adreslerde olasılıksal puanlama kullanır. Satın almadaki adı belli sorumlular hayatta kalma kurallarını ayarlar ve inceleme kuyruğunu işler; altın kayıtlar değişiklik olayları olarak yayımlanır ve temizlenmiş veri kaynakları iyileştirsin diye her ERP'ye geri akar. Birleştirilmiş harcama görünürlüğü daha iyi sözleşme koşullarının kilidini açar ve finansı her çeyrek tüketen uzlaştırma vergisi keskin biçimde düşer.

**Kamu.** Ulusal bir hükümet, veri paylaşımına dair katı yasal sınırlara saygı gösterirken kurumların bir vatandaşı her gişede bir yabancı olarak değil, tek bir kişi olarak görmesini ister. Kişi varlığı için, yönetilen bir ulusal tanımlayıcıya bağlı merkezi bir ana veri merkezi kurar; referans veri yürürlük tarihine göre sürümlenir ki geçmiş kayıtlar doğru kalsın. Kimlik çözümleme bilerek muhafazakârdır: belirsiz eşleşmeler otomatik birleştirmelere değil eğitimli sorumlulara gider, çünkü yanlış bir birleştirme birinin yardımını engelleyebilir ya da verisini ifşa edebilir ve her eşleşme denetim ve itiraz için günlüklenir. Getirisi daha az yinelenen kayıt, bölünmüş kimliklerden kaynaklanan daha az sahtecilik ve her kapıda kim olduğunu kanıtlamak zorunda olmayan bir vatandaştır; bunların hepsi bölüm 3.8'in birlikte çalışabilirlik standartları içinde gerçekleşir.

## İş gerekçesi: motivasyonlar, YG ve TSM

MDM'nin getirisi, çoğu kurumun adını koymadan ödediği bir verginin kaldırılmasından gelir. Yinelenen ve çelişen kayıtlar bariz biçimlerde para kaybettirir (aynı kişiye beş kez boşa pazarlama, eski adreslerden kaynaklanan sevkiyat hataları, kaçırılan hacim indirimleri) ve daha az bariz biçimlerde de (sayıları uzlaştıran analistler, sessizce yanlış olan rakamlara göre karar veren yöneticiler, hangi kaydın gerçek olduğunu çözmek için saat faturalayan denetçiler). Birleştirilmiş bir tedarikçi görünümü, çoğu zaman yalnızca daha iyi sözleşme koşullarıyla tüm programın maliyetini çıkarır.

Toplam sahip olma maliyetinin (TSM) üç parçası vardır: platform ya da inşa, kaynaklara ve tüketicilere entegrasyon ve zaman içinde en büyüğü olan süregelen sorumluluk. Entegrasyon maliyetini küçümsemek kolaydır, çünkü bir düzine eskimiş kaynak sistemi bağlamak MDM programlarının takvim ve bütçe kaybettiği yerdir; sorumluluk maliyetini unutmak da kolaydır, çünkü bu tek seferlik bir inşa değil, kalıcı bir işletme giderdir. Liderliğe gerekçeyi sunmak için MDM'yi zaten izledikleri sayılara bağlayın: gelir doğruluğu, pazarlama verimliliği, tedarik tasarrufları, denetim maliyeti ve düzenleyici risk; ardından dar başlayın ve yüksek acılı tek bir alandaki ölçülmüş bir kazanımın genişlemeyi fonlamasına izin verin.

## Anti-kalıplar ve tuzaklar

- **Okyanusu kaynatma kapsamı:** her alanı bir anda ana veri yapmaya çalışmak, yıllarca hiçbir şey teslim etmemek ve ilk kazanımdan önce sponsorluğu kaybetmek.
- **Yönetişimden önce araç:** sorumluları ve sahipleri adlandırmadan bir MDM platformu satın almak; böylece motorun sürücüsü olmaz.
- **Yetkisiz yarı zamanlı sorumlular:** sorumluluğu bir slaytta atayıp gerçek bir yetki ya da korunan zaman vermemek.
- **Sessiz hayatta kalma:** kayıtları araç varsayılanıyla ya da yükleme sırasıyla, yazılı kural olmadan ve bir altın kaydı açıklama imkanı olmadan birleştirmek.
- **Geri alınamaz birleştirmeler:** belirsiz eşleşmeleri geri alma imkanı olmadan otomatik birleştirmek; böylece iki gerçek varlığın yanlış kaynaşması kalıcı zarara dönüşür.
- **Yerinde üzerine yazılan referans veri:** kod listelerini sürümlemeden düzenlemek ve eski kodlar altında doğru olan her geçmiş raporu bozmak.
- **Kimsenin tüketmediği altın kayıtlar:** hiçbir aşağı akış sisteminin abone olmadığı kusursuz bir merkez kurmak; böylece temiz veri kararlara hiç ulaşmaz.
- **Standart kodları yeniden icat etmek:** ISO standartları varken kendi ülke ya da para birimi listelerinizi üretmek ve sebepsiz yere birlikte çalışabilirliği kaybetmek.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Ana ve referans veri yönetilmiyor. Aynı varlık yetkili bir sürümü olmadan birçok kez bulunur, kod listeleri ayrışır, eşleştirme elle ve tepkiseldir ve sorunun sahibi yoktur; böylece çekirdek varlıkların sayıları uyuşmaz ve hangisinin doğru olduğunu kimse söyleyemez.
- **Düzey 2, Geliştirme:** Temel alanlar tanınır ve biri onları tekilleştirir; çoğu zaman raporlama için ambarda. Temel deterministik eşleştirme vardır, referans listeleri toplanır ve birkaç kişi gayriresmî sorumlu olarak hareket eder, ama uygulama takımdan takıma değişir, kaynaklar dağınık kalır ve kurallar kağıtta değil, insanların kafasında yaşar.
- **Düzey 3, Standartlaştırma:** MDM, kurum genelinde tutarlı biçimde uygulanan yönetilen bir programdır. Ana alanların adı belli sahipleri ve yetkilendirilmiş sorumluları vardır, eşleştirme ve hayatta kalma kuralları belgelenip uygulanır, altın kayıtlar üretilip tüketicilere yayılır ve referans veri bir API gibi yürürlük tarihleriyle sürümlenip yayımlanır.
- **Düzey 4, Yönetme:** Program temel çizgilere karşı ölçülür ve denetlenir. Yineleme oranları, eşleşme güven dağılımları, yanlış birleştirme ve kaçırılan eşleşme oranları, anahtar alan bütünlüğü (eksiksizliği) ve inceleme kuyruğunun boyutu ile yaşı ölçüt olarak izlenir; eşikler sezgiyle değil bu sayılara göre ayarlanır ve MDM değeri (gelir doğruluğu, tedarik tasarrufları, inceleme maliyeti) sayıya dökülüp sabit bir ritimle sahiplere raporlanır.
- **Düzey 5, Orkestrasyon:** Altın kayıtlar neredeyse gerçek zamanlı sürümlü olaylar olarak akar, anlamsal katmanı besler ve kurum genelinde güvenilir kabul edilir. Eşleştirme ölçülen sonuçlara karşı sürekli iyileştirilir, ana veri yapma yeni alanlara tekrarlanabilir bir yetenek olarak genişler ve MDM, kaynaklar, standartlar ve varlık manzarası değiştikçe program uyum sağlasın diye yönetişim ve risk planlamasıyla bütünleşir.

## Tartışma fikirleri

1. İki sisteminiz kaç müşteriniz olduğu konusunda anlaşamıyorsa hangisi doğru ve bunu nasıl kanıtlarsınız?
2. Hangi ana veri alanı önce ana veri yapıldığında en büyük ölçülebilir kazancı getirir ve bu kazanımın değeri nedir?
3. Olasılıksal eşleştirme bugün size nerede yardımcı olurdu ve ima ettiği ara sıra yanlış birleştirmeyle rahat mısınız?
4. Referans verinizi nasıl sürümlüyorsunuz ve bir kodun anlamı değiştiğinde geçmiş raporlarınızda ne bozuluyor?
5. En önemli varlığınızın adı belli sorumlusu kim ve işi gerçekten yapacak yetkisi ve zamanı var mı?
6. Bir altın kayıt değiştiğinde aşağı akış sistemleriniz bunu nasıl öğreniyor ve canınız yanmadan önce ne kadar eski kalabilirler?

## Önemli çıkarımlar

- Verinizi ana, referans ve işlem verisi olarak ayırın; eşleştirme ve yönetişime yinelenmenin en çok maliyet getirdiği yerde yatırım yapın.
- Gerçek dünyadaki her varlık için, açık, geri alınabilir ve günlüklü hayatta kalma kurallarıyla oluşturulmuş tek bir altın kayıt üretin.
- Kontrol ve aksama iştahınıza uygun bir MDM mimari stili seçin (kayıt defteri, birleştirme, bir arada var olma ya da merkezi merkez).
- Referans veriyi sürümlü paylaşılan sözlük olarak ele alın, tanınmış standartları tercih edin ve kod listelerini asla yerinde üzerine yazmayın.
- MDM araçla değil, yönetişim ve sorumlulukla başarılı olur; altın kayıtları olay olarak yayın ve programı iyileşen kararlarla ölçün.

## Kaynaklar ve ileri okuma

- David Loshin, *Master Data Management*
- Alex Berson and Larry Dubov, *Master Data Management and Data Governance*
- Dan Power, *The Definitive Guide to Master Data Management*
- John Talburt, *Entity Resolution and Information Quality*
- Peter Christen, *Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection*
- Ivan P. Fellegi and Alan B. Sunter, "A Theory for Record Linkage," *Journal of the American Statistical Association*
- DAMA International, *DAMA-DMBOK: Data Management Body of Knowledge*
- Ralph Kimball and Margy Ross, *The Data Warehouse Toolkit*
