# 3.6 Eski sistem modernizasyonu

## Genel bakış ve motivasyon

[Eski sistemler](https://en.wikipedia.org/wiki/Legacy_system) dünyayı çalıştıran sistemlerdir. Toplumların dayandığı çekirdek bankacılık defterleri, vergi ve sosyal yardım motorları, hava trafik ve savunma sistemleri, sigorta poliçe yönetimi ve devlet sicilleri çoğu zaman onlarca yıllıktır. Birçoğu [COBOL](https://en.wikipedia.org/wiki/COBOL) (Common Business-Oriented Language) ya da başka eski teknolojilerle yazılmıştır ve kritik işlemlerin çoğunu hâlâ onlar yürütür. "Eski" bir hakaret değildir. Sistemin hayatta kalacak kadar değerli, başarısızlığı felaket olacak kadar kritik ve güvenle değiştirmesi zor olacak kadar yaşlı olduğu anlamına gelir. Eski sistem modernizasyonu, bu sistemlerin sunduğu temel hizmetleri aksatmadan onları iyileştirme, taşıma ya da değiştirme disiplinidir.

Bu orantısız biçimde bir kurumsal ve kamu sorunudur ve en büyük, en görünür BT başarısızlıklarının yaşandığı yerdir. Dünyadaki büyük işlemlerin çok büyük bir bölümü hâlâ [ana bilgisayar](https://en.wikipedia.org/wiki/Mainframe_computer) sistemlerine uğrar. Büyük kurumlardaki üretim kodunun önemli bir kısmı, yaşlanan ve küçülen bir uzman havuzu tarafından bakımı yapılan eski dillerdedir. En ağır yükü devletler taşır: onlarca yılda kodlanmış yasal yükümlülükler, yönetimlerden uzun yaşayan satın alma ve bütçe döngüleri ve kesintiye uğratılamayan vatandaş hizmetleri. Asıl risk bu sistemlerin eski olması değildir, çünkü birçoğu mükemmel çalışır. Risk, onları bakımda tutacak bilginin emekli oluşu, platformların giderek pahalılaşıp kısıtlanması ve "hepsini yeniden yazalım" cazibesinin alanın tarihindeki en pahalı başarısızlıkların bazılarına yol açmasıdır.

Bu bölüm gerçekten işe yarayan artımlı modernizasyon kalıplarını (boğucu incir ve soyutlamayla dal), eski sistem riskinin nasıl değerlendirilip önceliklendirileceğini, ana bilgisayar ve COBOL varlıklarının gözetimini, [veri taşıma](https://en.wikipedia.org/wiki/Data_migration) ve çift çalıştırma disiplinini ve hepsinden önce büyük yeniden yazım cazibesine nasıl direnileceğini ele alır. Temel inanç şudur: başarılı modernizasyon hemen her zaman artımlı, kanıta dayalı ve sürekli değer sunandır. Asla yıllara yayılan bir büyük patlama değildir.

## Temel ilkeler

- **Eski, yalnızca yaşlı değil, değerli ve temel demektir.** Dokunmadan önce sistemin ne yaptığına saygı gösterin; onlarca yılın zor kazanılmış iş kurallarını barındırır.
- **Artımlı, büyük patlamayı neredeyse her zaman yener.** Kararlı bir arayüzün ardında parça parça değiştirin; sürekli değer sunun ve riski küçük tutun.
- **Büyük yeniden yazım varsayılan başarısızlık biçimidir.** Tam yeniden yazımlar düzenli olarak bütçeyi aşar, vaadini yerine getiremez ve iptal edilir; bu dürtüye derin şüpheyle yaklaşın.
- **Anlamadığınız şeyi modernize edemezsiniz.** Değiştirmeden önce davranışı (belgelenmemiş kurallar dahil) [tersine mühendislikle](https://en.wikipedia.org/wiki/Reverse_engineering) çıkarın ve belgeleyin.
- **Projeler veri taşımada ölür.** Veri, herkesin beklediğinden daha eski, daha kirli ve daha dolaşıktır; onu birinci sınıf bir çaba olarak planlayın.
- **Güven kurmak için eskiyi ve yeniyi paralel çalıştırın.** Çift çalıştırma ve karşılaştırma, geçişten önce tutarsızlıkları yakalar.
- **Yaşa göre değil, risk ve değere göre önceliklendirin.** Yalnızca en eski olanı değil, en riskli ve en değerli olanı önce modernize edin.
- **Motoru değiştirirken ışıkları açık tutun.** Hizmet boyunca çalışmaya devam etmelidir; kritik vatandaş ya da mali sistemler için kabul edilebilir kesinti yoktur.

## Öneriler

### Boğucu incir kalıbıyla artımlı modernize edin

**Boğucu incir** (bir ağacın etrafında büyüyüp yavaş yavaş onun yerini alan sarmaşığın adını taşır) güvenli modernizasyonun iş atıdır. Eski sistemin önüne bir yönlendirme katmanı (bir API ağ geçidi, cephe ya da vekil) koyun. Sonra yetenek yetenek, yedeği modern bir sistemde inşa edin ve trafiğin o dilimini ona yönlendirin, gerisini eski sistemde bırakın. Zamanla yeni sistem büyür, eskisi küçülür ve sonunda emekliye ayrılabilir. Bu, sürekli değer sunar, her değişikliği küçük ve geri alınabilir tutar, riskli bir geçişten kaçınır ve herhangi bir noktada durmanıza ya da yeniden önceliklendirmenize izin verir. Büyük patlamanın tam tersidir. Eski sistem çalışmaya ve ekmeğini kazanmaya devam ederken siz onu çevresinden değiştirirsiniz.

### İç dikişler için soyutlamayla dal kullanın

Sistemin birçok parçasının bağımlı olduğu bir bileşeni değiştirmeniz gerektiğinde **soyutlamayla dal** kullanın. Mevcut gerçeklemenin üzerine bir soyutlama katmanı (bir arayüz) koyun, çağıranları soyutlamaya bağımlı olacak şekilde taşıyın, aynı soyutlamanın ardında yeni gerçeklemeyi inşa edin, geçişi yapın (çoğu zaman bir [özellik bayrağının](https://en.wikipedia.org/wiki/Feature_toggle) ardında, kademeli olarak) ve son olarak eski gerçeklemeyi kaldırın. Bu, büyük bir bileşenin uzun ömürlü bir dal olmadan geliştirmenin ana hattında artımlı biçimde değiştirilmesini sağlar ve sistemi boyunca yayımlanabilir tutar. Boğucu incirle doğal biçimde eşleşir: cephe dış dikişleri, soyutlamayla dal iç dikişleri halleder.

### Eski sistem riskini bilinçli değerlendirin ve önceliklendirin

Modernize etmeden önce varlıkların açık gözlü bir envanterini ve risk değerlendirmesini çıkarın. Her sistemi iş kritikliği, teknik risk (eskime, desteklenmeyen platformlar, güvenlik maruziyeti), değişiklik sıklığı ve en önemlisi **bilgi riski** (kaç kişinin hâlâ bakımını yapabildiği ve emekliliğe ne kadar yakın oldukları) üzerinden puanlayın. Sistemleri risk ve değer ızgarasına yerleştirin. Hem yüksek riskli hem yüksek değerli olanı modernize etmeye öncelik verin. Eski olsalar bile kararlı, az değişen, iyi anlaşılmış sistemleri olduğu gibi bırakmayı düşünün, çünkü kimsenin değiştirmesi gerekmeyen çalışan bir sistem acil durum değildir. Bu değerlendirme "her şey eski ve korkutucu" duygusunu savunulabilir, sıralanmış bir yol haritasına çevirir.

### Ana bilgisayar ve COBOL varlıklarını yalnızca değiştirmeyin, gözetin

Her ana bilgisayar ya da COBOL sistemi yakında değiştirilmeli ya da güvenle değiştirilebilir değildir. Yakın vadeli öncelik çoğu zaman **gözetimdir**: bilgi emekli olmadan önce onu yakalayın. Kodun barındırdığı iş kurallarını belgeleyin (çoğu belgesiz ve yeri doldurulamaz), mevcut davranışı sabitleyen otomatik testlere yatırım yapın ki gelecekteki değişiklik güvenli olsun, bakımcı alın ve çapraz eğitin, ve çekirdek yerinde kalsa bile çevresindeki teslim uygulamalarını (kaynak denetimi, [sürekli entegrasyon](https://en.wikipedia.org/wiki/Continuous_integration) (Sİ), otomatik test) modernize edin. Modernize ettiğiniz yerde, ilk adım olarak eski yetenekleri modern API'lerle sunmayı (kapsülleme) tercih edin. Otomatik COBOL'dan modern dile çeviriye temkinli yaklaşın, çünkü çalışan ama çoğu zaman anlaşılmaz mantığı sadakatle yeniden üreten kod üretir. En kıt kaynak hesaplama gücü değil, anlayıştır.

### Veri taşıma ve çift çalıştırmayı projenin özü sayın

Çoğu modernizasyon çabasının en zor ve en riskli kısmı **veridir**. Hacimlidir, kalitesi düşük ve tutarsızdır ve onlarca yılda birikmiş belgesiz anlamlarla doludur. Onu profilleyin ve temizleyin, eski şemaları yeniye açıkça eşleyin ve hiçbir şeyin kaybolmadığını ya da değişmediğini kanıtlayabilmeniz için tam uzlaştırmayla (sayımlar, sağlama toplamları, iş toplamları) tekrarlanabilir, otomatik bir taşıma kurun. Geçişin riskini **çift çalıştırmayla** (paralel çalıştırma) azaltın: eski ve yeni sistemleri aynı girdiler üzerinde yan yana çalıştırın ve yeni sistem eskisiyle güven eşiğinize kadar eşleşene dek çıktıları karşılaştırın. Ancak o zaman geçin ve geri dönebilme yeteneğini koruyun. Gerçekten kritik sistemlerde, hepsini bir kerede değil dilim dilim taşıyın ve geçin.

### Büyük yeniden yazım cazibesini yönetin

Dağınık eski sistemi atıp sıfırdan temiz bir yenisini kurma içgüdüsü güçlüdür ve büyük, kritik sistemler için neredeyse her zaman yanlıştır. Tam yeniden yazımlar "çirkin" koddaki değeri (uç durumlar, mevzuat kuralları, gerçek kullanıcıların bağımlı olduğu hata uyumlu davranışlar) hafife alır, öngörülenden çok daha uzun sürer, sona kadar hiç değer sunmaz ve çoğu zaman muazzam harcamadan sonra iptal edilir. Varsayılan olarak artımlı modernizasyonu seçin. Yeniden yazımları platformun gerçekten sürdürülemez olduğu ve artımlı yolların tükendiği durumlara saklayın. O zaman bile yeniden yazımı tek bir büyük patlama sürümü yerine boğucu kalıpla bağımsız teslim edilebilir parçalara bölün. Liderlik tam bir yeniden yazım için bastırdığında şu soruda ısrar edin: ilk üç ayda hangi değer yayımlanacak ve program yarıda durdurulursa ne olacak?

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
|---|---|---|
| Boğucu incir (artımlı) | Sürekli değer, düşük risk, geri alınabilir, hizmeti çalışır tutar | Daha uzun toplam süre, iki sistemi paralel çalıştırmak gerekir, entegrasyon yükü |
| Büyük patlama yeniden yazımı | Temiz sayfa, yeni kodda eski kısıtlar yok | Çok yüksek başarısızlık oranı, sona kadar değer yok, çok yüksek maliyet, iş kuralları kaybı |
| Kapsülleme (API'lerle sarmalama) | Hızlı, düşük riskli, çekirdeğe dokunmadan erişimi modernize eder | Çekirdek eski kalır; temel riski çözmez, erteler |
| Olduğu gibi bırakma (gözetim) | Proje riski yok; kısa vadede en ucuz | Bilgi ve platform riski birikmeye devam eder; sonunda zorunlu eylem |

Temel ödünleşim, dönüşüm hızı ile başarısızlık riski arasındadır ve eski sistem modernizasyonu bu takasın en dengesiz olduğu alandır. "Hızlı, temiz" büyük patlama yeniden yazımı bir seraptır ve tekrar tekrar en yavaş ve en pahalı sonucu üretir: iptal edilmiş bir program ve hâlâ modernize edilmemiş bir sistem. Artımlı yaklaşımlar daha yavaş hissettirir ve iki sistemi paralel çalıştırmayı gerektirir, ama boyunca değer sunar, riski küçük ve geri alınabilir tutar ve deneysel olarak güvenilir yoldur. Gerçek yargı kararı, kararlı bir eski sistemi biraz daha gözetmek ile artımlı değiştirmeye şimdi başlamak arasındadır. Bu kararı eski teknolojiden duyulan rahatsızlığa değil, risk gidişatına, özellikle bilgi riskine bırakın.

## Takımınızla tartışılacak sorular

1. **Eski sisteminizin önüne bir yönlendirme katmanı koyabileceğiniz bir yer var mı, yoksa yaratmak için ne gerekir?** Boğucu incir bir dikişe bağlıdır: bir yeteneği tek tek yeni bir gerçeklemeye yönlendirebileceğiniz bir API ağ geçidi, cephe ya da vekil. Birçok eski sistemde böyle bir dikiş yoktur, bu yüzden ilk modernizasyon artımı çoğu zaman sadece araya girme noktasını inşa etmektir ve bu iş kolayca hafife alınır. Mevcut entegrasyon haritasını getirin ve büyük patlama geçişi olmadan trafiğin yetenek başına nerede yakalanabileceğini sorun. Hiçbir yer yoksa, iç bir dikişte soyutlamayla dal başlangıç hamlesi olabilir. Yönlendirme katmanı olmadan artımlı bir yolunuz yoktur; kurumların genellikle başarısız olan yeniden yazıma geri itilmesinin yolu tam olarak budur.

2. **Varlıklarınızı gerçekten bir risk ve değer ızgarasında çizdiniz mi, yoksa yol haritanızı en eski hissettiren sistem mi yönlendiriyor?** Bölüm, önce yüksek riskli ve yüksek değerli olanı modernize etmenizde ve kararlı, az değişen, iyi anlaşılmış sistemleri çok eski olsalar bile bilerek rahat bırakmanızda ısrar eder. Açık bir ızgara olmadan dikkat en gürültülü şikâyete ya da en az modaya uygun teknolojiye akar; gerçek saatli bombalar (emekliliğe yakın iki bakımcısı olan kritik bir sistem) bekler. Her sistemi iş kritikliği, teknik risk, değişiklik sıklığı ve bilgi riski üzerinden puanlayın, sonra sağ üst köşeden başlayarak sıralayın. O ızgarayı ortak harita olarak toplantıya getirin. Bilgi riskine en ağır ağırlığı verin, çünkü yalnızca kötüleşen ve insanlar gittikten sonra geri satın alınamayan tek girdi odur.

3. **Geçtiğinizde tek bir kaydın bile kaybolmadığını ya da değişmediğini nasıl kanıtlayacaksınız ve bu kanıtı kim onaylayacak?** Veri taşıma bu projelerin öldüğü yerdir ve güven uzlaştırmadan gelir: eski ile yeni arasında eşleşen satır sayıları, sağlama toplamları ve iş kontrol toplamları, ayrıca aynı girdiler üzerinde çıktıları yüksek bir eşiğe kadar uyuşana dek karşılaştıran çift çalıştırma. Bir sosyal yardım ya da defter sisteminde tutarsızlık, eksik ödenen bir vatandaş ya da kaybolan bir kuruştur; bu yüzden kanıt yalnızca bir mühendisi değil, bir denetçiyi de tatmin etmelidir. Hangi toplamları uzlaştıracağınıza, hangi güven eşiğinin geçişi tetikleyeceğine ve eskiyi ve yeniyi ne kadar süre paralel çalıştıracağınıza şimdi karar verin. Boyunca geri almayı mümkün tutun ve hepsini bir kerede değil dilim dilim geçin. Çift çalıştırma sırasında bulduğunuz tutarsızlıklar genellikle korumanız gereken belgesiz eski kurallardır; bu yüzden her birini yalnızca bir kusur değil, bir keşif sayın.

4. **Hangi eski sistemlerinizi gözetiyorsunuz, hangilerini etkin biçimde değiştiriyorsunuz ve hangisinin hangisi olduğuna kim karar verdi?** Bölüm, yerinde istikrara kavuşturmaya değer sistemler (kuralları belgelemek, karakterizasyon testleri eklemek, bakımcıları çapraz eğitmek) ile artımlı değiştirmeye değer sistemler arasında bilinçli bir çizgi çeker ve ikisi çok farklı finansman ve kadro gerektirir. Büyük bir kurum için tehlike kaymadır: "şimdilik gözet" etiketli bir sistem, son bakımcı emekli olana ve seçim kriz altında sizin yerinize yapılana dek sessizce "sonsuza dek gözet" olur. Rakip hususlar bir yanda gözetim maliyeti ve platform eskimesi, öbür yanda değiştirmenin riski ve aksaması; bilgi riski dengeyi belirlemeli, çünkü yalnızca kötüleşir. Risk ve değer ızgarasını, her sistem için bakımcı sayısını ve emeklilik ufkunu ve gözet-ya-da-değiştir kararı için açık bir sahibi getirin. Kurumsal ve kamu varlıklarında her sistem için bir gözden geçirme ritmi ve hesap verebilir bir yetkili belirleyin, çünkü kimsenin yeniden ele almadığı bir sınıflandırma kimsenin vermediği bir karardır.

5. **Liderlik tam bir yeniden yazım istediğinde sabit cevabınız nedir ve artımlı bir yolun ilk üç ayda ne yayımladığını gösterebiliyor musunuz?** Büyük patlama yeniden yazımı varsayılan başarısızlık biçimidir, ama temiz sayfa satması kolay, boğucu incir satması zor olduğu için finanse edilmeye devam eder. Büyük bir takımın, tartışmanın odadaki en kıdemli kişiyle değil kanıtla kazanılması için prova edilmiş bir cevaba ihtiyacı vardır. Gerçek gerilim, bazı platformların gerçekten sürdürülemez olması ve yeniden yazımın haklı olmasıdır; bu yüzden cevap toptan bir ret olamaz: artımlı dikişlerin hâlâ var olup olmadığını eski platformu ayakta tutmanın gerçek maliyetiyle tartmalıdır. İlk artımın sunacağı değeri, benzer yeniden yazımların tarihsel başarısızlık oranını ve önerilen her yeniden yazımın bağımsız yayımlanabilir parçalara ayrıştırılmasını getirin. Çok yıllık bir programın iptalinin kamu parasını herkesin gözü önünde yaktığı kamuda, her yeniden yazımın erken değer sunmasında ve yarıda durdurulursa tam kayıp olmadan hayatta kalmasında ısrar edin.

6. **En eski kodunuza kilitlenmiş iş kurallarını, onları anlayan insanlar gitmeden önce nasıl yakalayacaksınız?** Eski bir sistemdeki değerin büyük kısmı, onlarca yıllık uç durumların, mevzuatın ve hata uyumlu düzeltmelerin biriktirdiği belgesiz davranıştır ve yazılı bir kayıtta değil, küçülen bir emekli uzman havuzunda yaşar. Büyük bir kurum için bu, insanlar gittikten sonra geri satın alınamayan tek risktir; bu yüzden daha görünür platform işinden önce finanse edilmeyi hak eder. Rakip çekim, bilgi yakalamanın (belgeleme, karakterizasyon testleri, tersine mühendislik, çapraz eğitim) hiçbir şey yayımlamayan bir yük gibi hissettirmesidir ve tam da bu yüzden ertelenir. Kritik bilgiyi kimin elinde tuttuğunun, ayrılmaya ne kadar yakın olduklarının ve bugün hangi test kapsamının mevcut davranışı sabitlediğinin bir envanterini getirin. Düzenlenmiş ve kamusal ortamlarda eski kodda kodlanmış yasal kuralları bir uyum varlığı sayın: onları sessizce kaybetmek bir teknik borç değil, bir hukuki maruziyettir.

## Sektör merceği

**Girişim.** Eski sisteminiz bir ana bilgisayar değil, kendi aceleyle yazdığınız MVP'dir: şimdi gelir taşıyan ve herkesin dokunmaktan korktuğu bir prototip. Yeniden yazmayın. En korkutucu modülü temiz bir arayüzün ardına sarın, davranışını sabitlemek için karakterizasyon testleri ekleyin ve işlevselliği artımlı olarak dışarı çıkarın ki her küçük sürüm değer sunsun ve riski küçültsün. Sıfırdan yeniden inşa için pistiniz yok, bu yüzden seçenek bırakmak zarafetten daha önemlidir.

**Küçük işletme.** Modernizasyon takımınız ve dar bir bütçeniz var; bu yüzden pratik hamle genellikle çalışan bir sistemi çalışır tutmaktır: onu anlayan tek kişinin bildiklerini yakalayın, kaynak denetimine ve birkaç otomatik teste alın ve özel bir yeniden inşa yerine bir tedarikçiye ya da paket ürüne yaslanın. Kararı satın alma ve inşa etme olarak çerçeveleyin ve yetenek bir meta olduğunda satın almayı tercih edin. Sınırlı çabanızı yalnızca en eski görünene değil, başarısızlığı işi durduracak tek sisteme harcayın.

**Kurumsal.** Sorun portföy ölçeğindedir: onlarca sistem, birçok takım ve varlık genelinde bilgi riski. Ortak bir risk ve değer değerlendirmesi yürütün, artımlı kalıplarda (boğucu incir ve soyutlamayla dal) standartlaşın ve veri taşıma ile çift çalıştırmayı herkesin güvendiği uzlaştırmayla birinci sınıf disiplinler olarak ele alın. Modernizasyonu kahramanca projelerin dağınıklığı olarak değil, risk gidişatına karşı sürekli bir portföy olarak yönetin ve gözetim ile bilgi yakalamayı açıkça bütçeleyin ki hiçbir kritik sistem emekli olan tek bir bakımcıya bağımlı kalmasın.

**Kamu.** Onlarca yılda kodlanmış yasal yükümlülükler, satın alma kuralları ve kesintiye uğratılamayan vatandaş hizmetleri büyük patlama değişimini özellikle tehlikeli kılar. Dilim dilim geçişle artımlı boğucu incir taşımayı tercih edin, uzlaştırma ve uzun paralel çalıştırmayla tek bir vatandaş kaydının kaybolmadığını ya da yanlış hesaplanmadığını kanıtlayın ve boyunca geri almayı mümkün tutun. Satın alma, opak çeviri yerine veri taşınabilirliğini ve iş kurallarının açıklanmasını talep etmelidir ve her çok yıllık program erken denetlenebilir değer sunmalı ve yarıda durdurulursa kamusal incelemeden sağ çıkmalıdır.

## Örnekler

**Girişim.** Üç yıllık bir girişimin özgün MVP'si kendi türünden bir eski sisteme dönüşmüştür: şimdi gerçek gelir işleyen ve herkesin dokunmaktan korktuğu aceleyle yazılmış bir prototip. Yeniden yazım yerine takım, en kötü modülü temiz bir arayüzün ardına sarar, mevcut davranışını sabitlemek için karakterizasyon testleri ekler ve işlevselliği birkaç ay boyunca parça parça ondan çıkarır. Her küçük sürüm değer sunar ve korkutucu kısmı küçültür; böylece girişim, karşılayamayacağı sıfırdan bir yeniden inşaya şirketi bahse sokmadan sürdürülebilir bir sistem elde eder.

**Kurumsal.** Büyük bir sigortacı poliçe yönetimini güvenilir ama değiştirmesi pahalı olan ve emekliliğe yaklaşan bir avuç mühendisin bakımını yaptığı bir ana bilgisayar COBOL sisteminde çalıştırır. Yeniden yazım yerine sigortacı ana bilgisayarı modern API'lerle sarar ve boğucu inciri uygular: yeni teklif al ve satın al ile self servis yetenekleri modern bir platformda inşa edilir ve bir cepheden yönlendirilir; çekirdek poliçe kayıtları ana bilgisayarda kalır. Paralel olarak takım iş kurallarını belgeler ve COBOL çevresine [karakterizasyon testleri](https://en.wikipedia.org/wiki/Characterization_test) ekler. Birkaç yıl içinde yetenek yetenek ana bilgisayardan çıkar, her sürüm değer sunar; kalan çekirdek krizde değil, sigortacının koşullarıyla emekliye ayrılabilir hâle gelir.

**Kamu.** Bir sosyal güvenlik kurumu milyonlarca vatandaşa ödeme yapan, kesintiye uğratılamayan ve yanlış ödeme yapılamayan onlarca yıllık bir yardım hesaplama sistemini modernize etmelidir. Benzer başarısız programları inceledikten sonra büyük patlama değişimini reddeder. Bunun yerine veriyi profiller ve temizler, kontrol toplamlarına karşı tam uzlaştırmalı otomatik taşıma kurar ve yeni yardım motorunu birçok ay boyunca eskisiyle paralel çalıştırır; ikisine de aynı talepleri verir, her hesaplamayı karşılaştırır ve her tutarsızlığı inceler (çoğu zaman korunması gereken belgesiz eski kuralları ortaya çıkarır). Yalnızca yeni sistem eskisiyle çok yüksek bir güvene kadar eşleştiğinde, boyunca geri almayı koruyarak yardım türü yardım türü geçer. Boğucu cephe, vatandaşların geçiş boyunca tek ve kesintisiz bir hizmet görmesini sağlar.

## İş gerekçesi: motivasyonlar, YG ve TSM

Eski sistem modernizasyonunun alışılmadık bir iş gerekçesi vardır, çünkü en büyük maliyet çoğu zaman *eylemsizliğin* maliyetidir ve en büyük risk modernizasyon projesinin kendisidir. Modernize etmemenin biriken maliyetleri somuttur: eskiyen platformlarda artan bakım ve lisanslama, giderek kıtlaşan ve pahalılaşan bir uzman iş gücü, yeni mevzuat ya da hizmet taleplerini hızla karşılayamama ve sistemi anlayan kimse kalmadığında yaşanacak felaket bir başarısızlığa artan maruziyet. Buna karşılık modernizasyon maliyeti yüksektir ve büyük patlama olarak yapıldığında gerçekten yüksek bir başarısızlık olasılığı taşır. Artımlı yaklaşımın YG için önemi tam da budur: tek büyük bahsi, her biri değer getiren ve durdurulabilen bir dizi küçük bahse çevirir.

Davayı liderliğe seçimi yeniden çerçeveleyerek anlatın. Soru "modernize et ya da etme" değildir. Soru şudur: "şimdi artımlı modernize et ya da artan gözetim maliyetleri öde ve sonra kriz altında zorunlu, daha riskli bir modernizasyonla yüzleş." Mevcut durumun TSM'sini (platform ve lisans maliyetleri, kıt becerilerin primi, kurtarılamaz bir kesintinin riske göre ağırlıklı maliyeti) ölçün ve hizmeti çalışır tutarken her artımla riski ve maliyeti azaltan aşamalı bir programla karşılaştırın. En önemlisi, önerilen her yeniden yazımın erken ve sık değer sunacak biçimde yapılandırılmasında ısrar edin. Üç yıl boyunca hiçbir şey sunmayan ve toplam kayıpla iptal edilebilen bir program bir yatırım değil, bir kumardır. Boğucu yaklaşım için en güçlü YG argümanı seçenek bırakmaktır: değer sürekli yayımlanır ve kurum herhangi bir noktada rotasını ayarlayabilir.

## Anti-kalıplar ve tuzaklar

- **Büyük patlama yeniden yazımı.** Sona kadar değer sunmayan ve çoğu zaman büyük maliyetle iptal edilen, çok yıllık, ya hep ya hiç değişim.
- **Anlamadan yeniden yazmak.** İş kuralları hiç belgelenmemiş kodu değiştirip gerçek kullanıcıların ve yasaların bağımlı olduğu uç durumları sessizce düşürmek.
- **Veriyi hafife almak.** Projenin en zor, en riskli kısmı olan veri taşımayı sonradan akla gelen bir iş olarak görmek.
- **Çift çalıştırmayı atlamak.** Paralel karşılaştırma olmadan yeni sisteme geçmek ve tutarsızlıkları ancak gerçek insanları etkiledikten sonra keşfetmek.
- **Çözüm olarak otomatik çeviri.** COBOL'u modern bir dile makineyle çevirip işin bittiğine inanmak ve eski mantığı kelimesi kelimesine yeniden üreten anlaşılmaz kod elde etmek.
- **Riske değil yaşa göre modernize etmek.** Yüksek riskli, çok değişen sistemler beklerken eski ama kararlı sistemlere çaba harcamak.
- **Bilgiyi kaybetmek.** Son bakımcıların iş kurallarını yakalamadan ve karakterizasyon testleri eklemeden emekli olmasına izin vermek.
- **Geri alma yok.** Yeni sistem gerçek yük ve gerçek veriyle yanlış davrandığında geri dönüşü olmadan geçmek.

## Olgunluk modeli

- **Düzey 1, Başlangıç.** Eski sistemlerden korkulur ve donmuştur; değişiklikten kaçınılır. Envanter ya da risk değerlendirmesi yoktur. Modernizasyon, hiç denenirse, hayal kırıklığının yönlendirdiği gelişigüzel bir ya hep ya hiç yeniden yazımdır. Bilgi, hiçbir şey yazılı olmadan birkaç emekli olacak kafada yaşar.
- **Düzey 2, Geliştirme.** Bazı takımların bir envanteri ve kabaca bir risk anlayışı vardır ve birkaç eski sistem erişim için API'lerle sarılmıştır. Artımlı kalıplar bilinir ama düzensiz uygulanır ve düşünce hâlâ büyük patlama yeniden yazımlarına kayar. Veri taşıma denenir ama hafife alınır ve uygulama takımdan takıma çok değişir.
- **Düzey 3, Standartlaştırma.** Sistemler, belgelenmiş, kurum genelinde bir yönteme göre risk ve değerle önceliklendirilir. Artımlı kalıplar (boğucu incir, soyutlamayla dal) zorunlu varsayılandır ve her modernizasyon standart bir oyun kitabını izler. Veri taşıma, geçişten önce çift çalıştırmalı, planlı ve uzlaştırılmış bir çabadır; bilgi yakalama ve karakterizasyon testleri isteğe bağlı değil, gerekli uygulamadır.
- **Düzey 4, Yönetme.** Modernizasyon veriyle ölçülür ve denetlenir. Varlıkların temel çizgileri vardır: sistem başına bakımcı sayısı ve emeklilik ufku, karakterizasyon testi kapsamı, taşıma uzlaştırma başarı oranları, çift çalıştırma tutarsızlık sayıları ve artım başına sunulan değer; hepsi hedeflere karşı izlenir. Gözet-ya-da-değiştir kararları ve geçiş git ya da gitme çağrıları bu kanıta dayanır ve bilgi riski eşiğini aşan bir sistem krizi beklemek yerine eylemi tetikler.
- **Düzey 5, Orkestrasyon.** Modernizasyon sürekli, iş ve risk planlamasıyla bütünleşik ve uyarlanabilirdir. Portföy, risk gidişatı (özellikle bilgi riski) değiştikçe yeniden dengelenir, artımlı değişim rutin ve dramsızdır, her artım değer sunar ve geri alınabilirdir ve kurum hızı bilinçli biçimde yönlendirir. Her taşımadan çıkan dersler ortak oyun kitabına geri beslenir; böylece tüm varlık zamanla iyileşir.

## Tartışma fikirleri

1. En kritik eski sisteminizin bakımını kaç kişi hâlâ yapabiliyor ve ayrılmaya ne kadar yakınlar?
2. Büyük patlama yeniden yazımı nerede sizi cezbediyor ve bunun yerine artımlı bir yaklaşım ilk üç ayda hangi değeri yayımlayabilir?
3. En eski sistemlerinizdeki iş kuralları ne kadar iyi belgelenmiş ve kod değiştirilirse onlara ne olur?
4. Taşımanız gereken veriyi profilleyip ne kadar kirli ve dolaşık olduğunu gerçekten biliyor musunuz?
5. Güvenle rahat bırakabileceğiniz hangi eski ama kararlı sistemlere modernizasyon enerjisi harcıyorsunuz?
6. Yeni sisteminizi eskisiyle paralel çalıştırıp geçmeden önce uyuştuklarını kanıtlayabilir misiniz?

## Önemli çıkarımlar

- Eski, değerli ve temel demektir; değiştirmeden önce sisteme saygı gösterin ve onu anlayın.
- Boğucu incir ve soyutlamayla dalla artımlı modernize edin, sürekli değer sunun ve her değişikliği küçük ve geri alınabilir tutun.
- Büyük patlama yeniden yazımını varsayılan başarısızlık biçimi sayın; onu gerçekten sürdürülemez platformlara saklayın ve o zaman bile ayrıştırın.
- Yaşa göre değil, risk ve değere göre (özellikle bilgi riskine göre) önceliklendirin; bazı eski sistemler değiştirilmekten çok gözetilmeye uygundur.
- Veri taşıma ve çift çalıştırma çabanın kalbidir; profilleyin, uzlaştırın, paralel çalıştırın ve geri almayı koruyun.
- En güçlü iş gerekçesi seçenek bırakmaktır: artımlı modernizasyon tek büyük, riskli bahsi değer getiren birçok küçük bahse çevirir.

## Kaynaklar ve ileri okuma

- Michael Feathers, *Working Effectively with Legacy Code*
- Martin Fowler, "StranglerFigApplication" and "BranchByAbstraction"
- Sam Newman, *Monolith to Microservices*
- Nicholas Carr / industry studies on mainframe and COBOL dependency (context on the scale of legacy estates)
- Robert Annett, *Working with Legacy Systems*
- Eric Evans, *Domain-Driven Design* (anti-corruption layer)
- Gregor Hohpe, *Enterprise Integration Patterns* and *The Software Architect Elevator*
- Standish Group *CHAOS Report* (evidence on large project and rewrite failure rates)
