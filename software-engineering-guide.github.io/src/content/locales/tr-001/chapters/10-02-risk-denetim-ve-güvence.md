# 10.2 Risk, denetim ve güvence

## Genel bakış ve motivasyon

Risk, denetim ve güvence; neyin ters gidebileceğini, hem yazılımınız hem de onu inşa edip çalıştıran kurum açısından anlama pratiğidir. Bu konuda ne yapacağınıza karar verirsiniz. Sonra sahip olduğunuzu iddia ettiğiniz kontrollerin gerçekten çalıştığını kanıtlarsınız. Bunu yöneticilere, düzenleyicilere, denetçilere ve kamuya kanıtlarsınız. Küçük bir takımda [risk yönetimi](https://en.wikipedia.org/wiki/Risk_management) çoğunlukla örtüktür. Birkaç kişi bütün resmi kafasında taşır. Büyük bir kurumda ya da kamu kurumunda riski açık ve sistematik hale getirmeniz gerekir. Hiçbir kişi bütün yüzeyi göremez. Başarısızlığın sonuçları büyüktür ve çoğu zaman düzenlemeye tabidir. Güven varsayılmaz, gösterilmelidir.

Bu, büyük kurumlar için üç nedenle daha önemlidir. Birincisi, ölçek maruziyeti çarpar. Daha fazla sistem, tedarikçi, veri, insan ve bağlantı, daha fazla başarısızlık yolu ve başarısızlık geldiğinde daha büyük bir etki alanı demektir. İkincisi, büyük kurumlar dış taraflara (düzenleyicilere, denetçilere, yönetim kurullarına, mahkemelere ve vatandaşlara) hesap verir ve bunlar güvence değil kanıt ister. Üçüncüsü, yoğunlaşma sessizce sızar. Paylaşılan platformlar, ortak tedarikçiler ve yeniden kullanılan bileşenler, hiçbir tekil takımın fark etmediği ama bütün kurumu bir anda çökertebilecek [tek hata noktaları](https://en.wikipedia.org/wiki/Single_point_of_failure) yaratır.

Bu bölüm, kurumsal risk yönetimi disiplinini teslimatı bürokrasiye boğmadan yazılıma getirmeyi amaçlar. İyi yapıldığında risk ve güvence, mühendisliğe konan bir vergi değildir. Büyük bir kurumun ölçekte işletme hakkını kazanma biçimidir. "Bize güvenin" sözünü "işte kanıt" sözüne dönüştürürler.

## Temel ilkeler

- **Risk yönetilir, ortadan kaldırılmaz.** İş, riski kabul edilen bir düzeye kadar belirlemek, değerlendirmek, ele almak ve izlemektir; sıfıra indirilebileceğini varsaymak değil.
- **Riske yaratıldığı yerde sahip çıkın.** Bir sistemi inşa eden ve çalıştıran takım onun riskinin sahibidir; merkezî işlevler standart koyar ve denetler, hesap verebilirliği üstlenmez.
- **Beyan yerine kanıt.** Gösteremediğiniz bir kontrol, sahip olmadığınız bir kontroldür.
- **Anlık yerine sürekli.** Yıllık [denetimler](https://en.wikipedia.org/wiki/Audit) kaymayı çok geç yakalar; kontroller mümkün olduğunda sürekli ve otomatik olarak izlenmelidir.
- **Üçüncü taraflar riskinizi devralır.** Tedarikçilerinizin zayıflıkları sizin zayıflıklarınız olur; tedarik zinciri riski sizin riskinizdir.
- **Yoğunlaşma birinci sınıf bir risktir.** Birleştirme yoluyla verimlilik, adlandırılması ve yönetilmesi gereken tek hata noktalarını sessizce yaratır.
- **Orantılılık.** Kontrolün derinliğini sonuca göre ayarlayın; her sistemi azami kritiklikte ele almak emeği boşa harcar ve kaçınmayı doğurur.

## Öneriler

### Kurumsal risk yönetimini yazılıma uygulayın

Riskleri karşılaştırabilmek ve toplayabilmek için kurum genelinde ortak bir risk çerçevesi ve sözcük dağarcığı benimseyin. Her önemli sistem için bir [risk kaydı](https://en.wikipedia.org/wiki/Risk_register) tutun ve tekil kayıtları bir portföy görünümüne toplayın. Her risk için olasılığı, etkiyi, sahibi, mevcut kontrolleri ve ele alma kararını (kabul, azaltma, devretme ya da kaçınma) kaydedin. Görevleri ayırmak için ["üç savunma hattı"](https://en.wikipedia.org/wiki/Three_lines_of_defence) modelini kullanın: takımlar kendi risklerinin sahibidir ve onları yönetir (birinci hat), risk ve uyum işlevleri politika koyar ve sorgular (ikinci hat) ve iç denetim bağımsız biçimde güvence verir (üçüncü hat). Her takım tahmin yürütmesin diye, kurumun ne kadar risk taşımaya razı olduğunu bilmeleri için en üstte açık bir [risk iştahı](https://en.wikipedia.org/wiki/Risk_appetite) belirleyin.

### Üçüncü taraf ve tedarik zinciri riskine güvence verin

Tedarikçilerinizin ve, aynı derecede önemli olarak, dolaylı açık kaynak bileşenleri de dahil yazılım bağımlılıklarınızın envanterini çıkarın. Her tedarikçiyi taşıdığı erişim ve kritikliğe orantılı olarak değerlendirin. İyi kanıt zaten varken anketleri yeniden icat etmek yerine tanınmış onaylara (bir sağlayıcının güvenlik kontrolleri üzerine bağımsız denetim raporu olan SOC 2 ya da [ISO 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001) raporları gibi) yaslanın. Bir güvenlik açığı patladığı anda "etkilendik mi?" sorusuna yanıt verebilmeniz için tükettiğiniz bileşenler için bir yazılım malzeme listesi (SBOM) isteyin. Tedarik zinciri bütünlüğünü hattınıza yerleştirin: kaynağı doğrulayın, yapıtları sabitleyin ve imzalayın ve derlemenize nelerin girdiğini denetleyin. Güvenlik, ihlal bildirimi, denetim hakları ve çıkış şartlarını sözleşmelere yazın. Tedarikçileri yalnızca işe alımda değil, düzenli bir tempoda yeniden değerlendirin.

### Denetim izleri, kanıt ve sürekli kontrol izleme kurun

Sistemleri, çalışmanın yan ürünü olarak kanıt üretecek şekilde tasarlayın. Önemli eylemlerin değiştirilemez, zaman damgalı, kurcalanmaya karşı kanıt bırakan denetim günlüklerini tutun: kim neyi neye, ne zaman ve hangi yetkiyle yaptı. Bu günlükleri, tam da kaydettikleri kişilerce değiştirilmekten koruyun. Otomatik ve sürekli izlenen kontrolleri tercih edin: uyumsuz değişiklikleri engelleyen kod olarak politika, gerekli incelemeleri zorlayan hat geçitleri ve kontrol durumunu gerçek zamanlı gösteren panolar. Sürekli kontrol izleme, denetimi kanıtı yeniden kurmak için yapılan dönemsel bir telaştan, istikrarlı bir güvence akışına dönüştürür. Kaymayı bir sonraki yıllık incelemede değil, saatler içinde yakalar.

### İş sürekliliğini ve felaket kurtarmayı yönetin

Sistemler başarısız olursa kurumunuzun neyi, ne kadar hızlı sürdürmesi gerektiğini bilin. Mühendislik kolaylığına göre değil, iş ihtiyacına göre hizmet başına kurtarma süresi ve kurtarma noktası hedeflerini (RTO/RPO) belirlemek için bir iş etki analizi yürütün. Ardından [iş sürekliliği](https://en.wikipedia.org/wiki/Business_continuity_planning) ve [felaket kurtarma](https://en.wikipedia.org/wiki/Disaster_recovery) (FK) planlarını sürdürün ve (kurumların atladığı kısım bu) onları gerçekten sınayın. Tam yedek geçişi ve yedekten geri yükleme tatbikatlarını içeren düzenli alıştırmalar yapın. Sınanmamış yedekler ve sınanmamış yedek geçişi yetenek değil, varsayımdır. Bunu kurumsal düzeyde yönetin; böylece sistemler arası bağımlılıkları gerçek felaket sırasında değil, öncesinde anlarsınız.

### Yoğunlaşma riskini ve tek hata noktalarını yönetin

Birçok hizmetin tek bir şeye bağlı olduğu yerleri bilerek arayın: tek bir bulut bölgesi, tek bir kimlik doğrulama sağlayıcısı, tek bir kilit tedarikçi, tek bir veritabanı, tek bir kişi. Bu yoğunlaşmaları portföy düzeyinde haritalayın, çünkü tekil takımlar onları göremez. En kritik olanlar için yedeklilik, çok bölgeli ya da çok tedarikçili stratejiler ve zarif bozulma yoluyla yoğunlaşmayı azaltın; eklenen maliyeti ve karmaşıklığı dürüstçe tartın. Verimlilik için yoğunlaşmayı kabul ettiğinizde bunu bilinçli, belgelenmiş, sahibi olan ve yedek planı sınanmış bir karar yapın. Çökene kadar kimsenin fark etmediği bir kaza olmasına izin vermeyin.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
|---|---|---|
| Ağır resmî kontroller | Güçlü güvence; denetime ve düzenleyiciye hazır | Teslimatı yavaşlatır; kutucuk işaretleme uyumunu ve kaçınmayı davet eder |
| Hafif risk temelli kontroller | Hızlı; emek gerçek maruziyete odaklanır | Olgun muhakeme gerektirir; risk kötü değerlendirilirse boşluklar |
| Anlık denetim | Tanıdık; net geçti/kaldı anı | Kaymayı geç yakalar; yalnızca denetim gününe hazırlanma teşviki |
| Sürekli kontrol izleme | Erken kayma tespiti; daha az denetim telaşı | Peşin otomasyon yatırımı; araç ve enstrümantasyon maliyeti |
| Birleştirme / tek tedarikçi | Düşük maliyet; daha basit; hacim kaldıracı | Yoğunlaşma riski; tek hata noktası; bağımlılık |
| Yedeklilik / çok tedarikçi | Dayanıklılık; tek hata noktası yok | Daha yüksek maliyet ve karmaşıklık; bakımı ve güvenliği daha fazla |

Yinelenen ödünleşim, güvence ile hız arasındadır. Çözüm, orantılılık artı otomasyondur. Her yere uygulanan ağır kontroller herkesi yavaşlatır ve daha kötüsü, takımlara uyumu oyuna getirilecek bir tiyatro gibi görmeyi öğretir. Yalnızca hafif kontroller her takımda bulunmayan muhakemeye bağlıdır. Çıkış yolu: kontrol derinliğini sonuca göre ayarlamak ve kontrolleri teslimat hattına otomatikleştirmek; böylece güvence sonradan eklenmek yerine inşa etme eyleminden gelir. Yoğunlaşma ödünleşiminin (verimlilik ile dayanıklılık) evrensel bir yanıtı yoktur. Her kritik bağımlılık için bilinçli karar verin; kabul edilen riski belgeleyin ve yedek planı sınayın.

## Takımınızla tartışılacak sorular

1. **Kontrol derinliği sonuca uysun diye sistemleri kritikliğe göre nasıl sınıflandıracaksınız?** Orantılılık, güvence ile hız arasındaki gerilimin çözümüdür: her sistemi azami kritiklikte ele alırsanız emeği boşa harcar ve takımlara uyumu oyuna getirmeyi öğretirsiniz; hiçbir şeyi kritik saymazsanız savunmasız yakalanırsınız. Her sistemi en üstte belirlenmiş bir risk iştahına bağlayan açık bir kademelendirmeye ihtiyacınız var; böylece düşük riskli bir iç araç ile vatandaşa dönük bir yardım sistemi aynı kontrolleri taşımaz. Tartışmaya kanıtla gelin: sistemlerinizi, her birinin taşıdığı veriyi ve etki alanını ve şu an uygulanan kontrolleri listeleyin, sonra iki yönde de uyumsuzlukları arayın. Yanıt, neyi hatta otomatikleştirdiğinizi ve neyi insan muhakemesine bıraktığınızı değiştirmeli ve takımlara tahmin yürütmek yerine günlük ödünleşimler için net bir temel vermelidir. Üzerinde anlaşılmış kademeler olmadan orantılılık sadece bir sözcüktür.

2. **Kritik bir bağımlılık bir güvenlik açığı açıkladığında "etkilendik mi?" sorusuna dakikalar içinde yanıt verebilir misiniz?** Yaygın kullanılan bir bileşen bozulduğunda hızlı yanıt veren kurumların elinde, dolaylı açık kaynak bağımlılıkları da dahil, bir bileşenin kullanıldığı her yeri haritalayan bir SBOM envanteri zaten vardır. Dürüst yanıtınız günlerse ya da "bakmamız gerekir" ise, bu açık, kontrol altına alınmış bir yanıt ile telaş arasındaki farktır. Kanıtla gelin: bağımlı olduğunuz gerçek bir kütüphane seçin ve onu sevk eden her hizmeti listelemenin ne kadar sürdüğünü ölçün. Yanıt, hatta SBOM üretmeye, yapıtları sabitleyip imzalamaya ve kaynağı doğrulamaya yapılacak yatırımı yönlendirmeli; böylece maruziyet bir soruşturma değil, bir sorgu olur. Bu tedarik zinciri riskidir ve tedarikçilerinizin zayıflıkları zaten sizin zayıflıklarınızdır.

3. **Hangi hizmetler tam yedek geçişi ve yedekten geri yükleme tatbikatı alıyor, ne sıklıkla ve geçtiklerini kim onaylıyor?** Sınanmamış yedekler ve sınanmamış yedek geçişi yetenek değil, varsayımdır ve kurumlar bunu bir felaketten önce değil, gerçek bir felaket sırasında keşfeder. Hizmet başına kurtarma süresi ve kurtarma noktası hedeflerini iş ihtiyacından belirlemek için bir iş etki analizi yürütün, sonra tatbikat sıklığını bu kademelere bağlayın. Kanıt getirin: en kritik hizmetiniz için son tam geri yükleme ne zaman uçtan uca gerçekten uygulandı ve belirtilen RTO'yu karşıladı mı? Yanıt, sonuçları liderliğe raporlanan rutin, sistemler arası FK alıştırmaları takvimi üretmeli; çünkü kurumsal düzeydeki yönetişim, tek bir takımın göremeyeceği sistemler arası bağımlılıkları açığa çıkarandır. Verimlilik için tek bölgeli ya da tek tedarikçili yoğunlaşmayı kabul ettiğinizde bunu bilinçli, belgelenmiş, sahibi olan ve yedek planı sınanmış bir karar yapın.

4. **Hangi kontrolleriniz çalışmanın yan ürünü olarak otomatik kanıt üretiyor ve hangileri hâlâ denetim zamanı birinin kanıt derlemesine bağlı?** Gösteremediğiniz bir kontrol, sahip olmadığınız bir kontroldür ve denetimlerden sakin çıkan kurumlar, hatlarının kimse toplamayı hatırlamadan önemli eylemlerin değiştirilemez, zaman damgalı kayıtlarını yaydığı kurumlardır. Karşı çekim gerçektir: kontrolleri kod olarak politikaya ve sürekli izlemeye otomatikleştirmek peşin mühendislik emeğine mal olur, oysa anlık kanıt toplama, yıllık telaş gelip kayma aylardır birikene kadar daha ucuz hissettirir. Tartışmaya kanıtla gelin: en önemli birkaç kontrolünüz için kanıtın şu an kurcalamaya karşı kanıt bırakan bir depoda olup olmadığını, günlüklerin kaydettiği kişilerin onları değiştirip değiştiremeyeceğini ve bir çeyreğin faaliyetini yeniden kurmanın kaç saat süreceğini sorun. Yanıt, yatırımı elle onaylamak yerine sürekli kontrol izlemeye ve hat geçitlerine yöneltmeli. Kurumsal ve kamu ortamlarında en güçlü konum, denetçilere canlı kontrol panolarına okuma erişimi vermektir; böylece denetim dönemsel bir yeniden kurmadan, istikrarlı bir kanıt akışının sürekli örneklenmesine dönüşür.

5. **Üç savunma hattı gerçekten ayrılmış görevler olarak mı işliyor, yoksa sahiplik bulanıklaşıp bir sistemi inşa edenler aynı zamanda ona güvence mi veriyor?** Modelin bütün amacı bağımsızlıktır: takımlar birinci hatta risklerinin sahibi olur ve onları yönetir, risk ve uyum ikinci hatta politika koyar ve sorgular, iç denetim üçüncü hatta bağımsız güvence verir ve bu roller birbirine karıştığında güvence kendi kendini notlayan ödeve dönüşür. Gerilim şudur: risk sahipliğini teslimat takımlarına vermek, merkezî bir işlevin onu üstlenmesinden daha yavaş ve çekişmeli hissedebilir, ama merkezî üstlenme sessizce hesap verebilirliği riskin gerçekte yaratıldığı yerden kaldırır. Kanıt getirin: yakın zamanda alınmış önemli bir risk kararını haritalayın ve kimin sahip olduğunu, kimin sorguladığını ve kimin bağımsız biçimde güvence verdiğini adlandırın, sonra tek bir grubun bu rollerden ikisini oynayıp oynamadığını kontrol edin. Tartışma ayrıca en üstte açıkça bir risk iştahı belirlenip belirlenmediğini de ortaya çıkarmalı, çünkü bu olmadan her takım ne kadar risk taşıyacağını tahmin eder. Düzenlemeye tabi bir kurum ya da kamu kurumu için, kalan riski resmen kabul eden, sistemi inşa eden takımdan ayrı hesap verebilir bir yetkili, çoğu zaman bir nezaket değil, katı bir gerekliliktir.

6. **Birçok hizmetiniz sessizce nerede tek bir şeye bağlı ve portföy düzeyinde bu yoğunlaşmanın sahibi kim?** Tek bir bulut bölgesine, tek bir kimlik doğrulama sağlayıcısına, tek bir kilit tedarikçiye, tek bir veritabanına ya da tek bir kişiye birleştirmek gerçek verimlilik ve hacim kaldıracı sağlar ve aynı güvenilirlikte, hiçbir tekil takımın göremediği tek hata noktaları üretir; çünkü her takım yalnızca kendi dilimini görür. Dürüst ödünleşim verimlilik ile dayanıklılıktır ve evrensel bir yanıtı yoktur: yedeklilik ve çok bölgeli ya da çok tedarikçili stratejiler, dayanıklılığı para, karmaşıklık ve güvenliği sağlanacak daha fazla yüzey karşılığında satın alır. Kanıt getirin: paylaşılan bağımlılıkların portföy düzeyinde bir haritasını çıkarmayı deneyin ve tek bir kesintinin birçok hizmete yayıldığı darboğazları arayın, sonra bu yoğunlaşmalardan hangisinin gerçekten sahibi olan biri olup olmadığını kontrol edin. Yanıt, kazara oluşan yoğunlaşmayı en kritik bağımlılıklar için bilinçli, belgelenmiş, acil durum planı sınanmış kararlara dönüştürmeli. Kurumsal ve kamu portföylerinde, vatandaşa dönük tek bölgeli bir hizmeti açığa çıkaran bölgesel bir kesinti, düzenleyicilerin ve kamuoyunun sonradan inceleyeceği tam olarak o başarısızlıktır; bu yüzden felaket sırasında değil, öncesinde haritalayın.

## Sektör merceği

**Girişim.** Bir avuç insan ve risk departmanına yetecek pist olmadığında, güvenceyi ayrı bir işlev değil, inşanın yan ürünü yapın. Her girdi için bir sahibi ve bir ele alma kararı olan tek ve kısa bir risk kaydı tutun, sıfırdan kontrol yazmak yerine bulut sağlayıcınızın SOC 2 raporuna yaslanın ve hatta SBOM üretin; böylece bir bağımlılık hatası düştüğü gün "açıkta mıyız?" bir sorgu olur. Göze çarpan tek yoğunlaşmanızı yüksek sesle adlandırın, genellikle dağıtım yapabilen tek kişidir ve bilgi tek bir kafaya hapsolmasın diye yanına birini eşleştirin.

**Küçük işletme.** Özel bir risk ya da denetim uzmanınız ve dar bir bütçeniz var; bu yüzden güvenceyi inşa etmek yerine satın alın: aksi halde üretmeniz gereken kanıtı zaten taşıyan SOC 2 ya da ISO 27001 onaylarına sahip tedarikçileri tercih edin. Sınırlı emeğinizi sonucun en yüksek olduğu yere harcayın; tek bir risk kaydı ve aylık yedekten geri yükleme tatbikatı, kimsenin sürdürmediği ayrıntılı bir çerçeveden iyidir. Sözleşmeleri bir kontrol olarak görün; tedarikçi anlaşmalarına ihlal bildirimi ve çıkış şartlarını yazın, böylece onların riskini körlemesine daha az devralırsınız.

**Kurumsal.** Belirleyici sorun, birçok takım üzerindeki ölçektir: üç hat modelini yürütün, yönetim kurulu düzeyinde bir portföy görünümüne toplanan hizmet başına risk kayıtları tutun ve takımlar tahmin yürütmeyi bıraksın diye en üstte açık bir risk iştahı belirleyin. Anahtar kontrolleri hatta uygulanan kod olarak politika biçiminde kodlayın, denetçilere yıllık denetimlere hazırlanmak yerine canlı kontrol panolarına okuma erişimi verin ve yoğunlaşma riskini portföy düzeyinde haritalayın, çünkü hiçbir tekil takım paylaşılan darboğazları göremez. Orantılılık bir slogan değil gerçek olsun diye kontrol derinliğini açık kritiklik kademeleriyle sonuca uydurun.

**Kamu.** Tedarik kuralları, şeffaflık ve kamusal hesap verebilirlik her tercihi şekillendirir. Hesap verebilir bir yetkilinin kalan riski kabul ettiği resmî bir yetkilendirme süreci izleyin, yetkilendirme tek seferlik bir sertifika değil sürekli bir durum olsun diye sürekli izleme sürdürün ve tedarikçi sözleşmelerine denetim hakları ve veri taşınabilirliği şartlarını yazın. Vatandaşa dönük tek bölgeli bir hizmeti açığa çıkaran bölgesel bir kesinti kamusal bir mesele haline geldiğinden, en kritik hizmetler için çok bölgeli yedek geçişini ve sınanmış geri yüklemeleri zorunlu kılın ve felaket kurtarma alıştırması sonuçlarını sabit bir tempoda liderliğe raporlayın.

## Örnekler

**Girişim.** Hasta verisi işleyen altı kişilik bir sağlık teknolojisi girişimi bir risk departmanını karşılayamaz; bu yüzden güvenceyi inşanın yan ürünü yapar. Paylaşılan bir belgede, her girdi için bir sahibi ve bir ele alma kararı olan tek ve kısa bir risk kaydı tutar ve onu cuma ayakta toplantısında gözden geçirir. Kendi kontrollerini sıfırdan yazmak yerine bulut sağlayıcısının SOC 2 raporuna yaslanır, bir bağımlılık hatası düştüğü gün "açıkta mıyız?" sorusuna yanıt verebilmek için hatta SBOM üretir ve her ay yedekten geri yükleme tatbikatı yapar, çünkü sınanmamış bir yedek yalnızca bir umuttur. Göze çarpan tek yoğunlaşma riskini de yüksek sesle adlandırır: dağıtım yapabilen tek kurucu ve bilgi tek bir kafaya hapsolmasın diye yanına ikinci bir mühendis eşleştirir.

**Kurumsal.** Sürekli düzenleyici incelemesi altında çalışan bir ödeme şirketi, üç hat modelini yürütür. Yönetim kurulu düzeyinde bir panoya toplanan hizmet başına risk kayıtları tutar. Anahtar kontrollerini dağıtım hattında uygulanan kod olarak politika biçiminde kodlar. Değişiklik onayları, erişim verme ve yapılandırma değişiklikleri, kurcalanmaya karşı kanıt bırakan bir depoya değiştirilemez denetim olayları yayar. Şirket yıllık denetimlere hazırlanmak yerine denetçilere canlı kontrol panolarına okuma erişimi verir ve denetimi sürekli kanıtın örneklenmesine dönüştürür. Yaygın kullanılan bir açık kaynak kütüphane kritik bir hata açıkladığında şirketin SBOM envanteri "nerede açıktayız?" sorusunu dakikalar içinde yanıtlar.

**Kamu.** Ulusal bir devlet kurumu, herhangi bir sistemin çalışmasına izin vermeden önce resmî bir yetkilendirme süreci izler. Belgelenmiş kontroller, bağımsız bir değerlendirme ve kalan riski kabul eden hesap verebilir bir yetkili gerektirir. Sürekli izleme sürdürür; böylece yetkilendirme tek seferlik bir sertifika değil, süregelen bir durumdur. Bir bölgesel bulut kesintisi bir keresinde vatandaşa dönük bir yardım sisteminde tek bölgeli bir bağımlılığı açığa çıkardı. Karşılık olarak kurum portföyü boyunca [yoğunlaşma riskini](https://en.wikipedia.org/wiki/Concentration_risk) haritaladı, en kritik hizmetleri için çok bölgeli yedek geçişini ve sınanmış geri yüklemeleri zorunlu kıldı ve şimdi sonuçları liderliğe raporlanan dönemsel felaket kurtarma alıştırmaları yürütüyor.

## İş gerekçesi: motivasyonlar, YG ve TSM

Risk ve güvencenin getirisi, önlenen felaket kayıpları tarafından belirlenir: büyük bir ihlal, bir düzenleyici ceza, kritik bir hizmetin uzun süreli kesintisi ya da bir tedarik zinciri ihlali. Bu olaylar tek tek nadirdir ama tek tek devasadır. Önlenen tek bir olay, bütün güvence programının çok yıllı maliyetini aşabilir. Kayıp önlemenin ötesinde, olgun güvence uyumun süregelen maliyetini düşürür, çünkü kanıt telaşla toplanmak yerine otomatik olarak üretilir. Düzenlemeye tabi işi kazanmayı ve müşteri durum tespitinden geçmeyi kolaylaştırır. Ve olay müdahalesini hızlandırır, çünkü maruziyetinizi zaten bilirsiniz.

Benimseme maliyeti, risk ve denetim kadrosunu, izleme ve kanıt için araçları ve kontrolleri hatlara otomatikleştirme mühendisliği emeğini içerir. Benimsememenin maliyeti, önlemediğiniz felaketlerin beklenen değeri artı elle denetim hazırlığının yavaş vergisi ve her kamusal başarısızlıktan sonra biriken itibar zararıdır. Liderliğe gerekçe sunarken az sayıda makul en kötü durumu ve olasılıklarını nicelendirin. Sürekli kontrol izlemeyi, büyük, öngörülemez, ara sıra gelen bir kaybı küçük, istikrarlı, öngörülebilir bir maliyetle takas etmek olarak çerçeveleyin. Toplam sahip olma maliyetini vurgulayın: bir kez otomatikleştirilen bir kontrol, bundan sonra her yıl denetim maliyetini aşağı çeker.

## Anti-kalıplar ve tuzaklar

- **Kutucuk işaretleme uyumu.** Gerçek kontrol çalışmazken bir denetçiyi tatmin eden belgeler üretmek.
- **Denetim günü tiyatrosu.** Yalnızca yıllık denetimden önceki haftalarda uyumlu olan ve yılın geri kalanında kayan sistemler.
- **Mezarlık olarak risk kaydı.** Bir kez doldurulan ve bir daha ele alınmayan, gerçek kararlardan kopuk bir kayıt.
- **Sınanmamış FK.** Hiç uygulanmamış ve bu yüzden gerektiğinde çalışmayan yedek ve yedek geçişi planları.
- **Logoya göre tedarikçi güveni.** Tanınmış bir tedarikçinin kanıt olmadan güvenli olduğunu varsaymak ve dolaylı bağımlılıkları büsbütün göz ardı etmek.
- **Görünmez yoğunlaşma.** Verimlilik için tek bir bölgeye, tedarikçiye ya da kişiye birleştirip ortaya çıkan tek hata noktasının kimse tarafından sahiplenilmemesi.
- **Teslimat engeli olarak güvence.** Orantılılığı olmayan ağır merkezî kontroller; takımlar bunların çevresinden dolanır ve hiç güvencesi olmayan gölge sistemler yaratır.
- **Aktörün düzenleyebildiği günlükler.** Denetlenen kişilerin değiştirebildiği ve hiçbir şeyi kanıtlamayan denetim izleri.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Risk, olaylardan sonra tepkisel biçimde ele alınır. Paylaşılan bir çerçeve ya da kayıt yoktur. Kontroller belgelenmemiş ve doğrulanmamıştır; denetimler acı veren, elle yapılan telaşlardır. Yoğunlaşma ve tedarikçi riski incelenmemiştir ve tek hata noktaları ancak çöktüklerinde ortaya çıkar.

**Düzey 2, Geliştirme.** Temel uygulamalar ortaya çıkar ama takımdan takıma değişir. Büyük sistemler için bazı risk kayıtları vardır ve denetimler geçilsin diye bir kontrol çerçevesi benimsenmiştir, ama hazırlık elle ve anlıktır. Kilit tedarikçiler işe alımda değerlendirilir, sonrasında değil. Yedekler vardır ama nadiren sınanır ve tek hata noktalarının yalnızca bir kısmı bilinir.

**Düzey 3, Standartlaştırma.** Üç hat modeli ve ortak bir çerçeve belgelenmiş ve kurum genelinde uygulanmıştır; bu da maruziyeti karşılaştırmanıza ve toplamanıza izin veren tek bir risk sözcük dağarcığı sağlar. Birçok kontrol hatlara otomatikleştirilmiştir ve sürekli izleme anahtar kontrolleri kapsar. SBOM'lar dahil tedarikçi ve bağımlılık envanterleri sürdürülür, FK bir takvime göre sınanır ve yoğunlaşma riski tekil takımlara bırakılmak yerine portföy düzeyinde haritalanır.

**Düzey 4, Yönetme.** Güvence yalnızca belgelenmekle kalmaz, başlangıç değerlerine karşı ölçülür ve denetlenir. Kontrol kapsamı, kayma tespit süresi, belirtilen RTO ve RPO'ya karşı FK tatbikatı geçme oranları, bir açıklamadan sonra "etkilendik mi?" sorusuna yanıt vermenin ortalama süresi ve kalan riskin belirtilen risk iştahına karşı durumu birer ölçüt olarak izlenir ve liderliğe raporlanır. Başlangıç değerinden sapmalar eylemi tetikler, sonlandırma ölçütleri ve iyileştirme son tarihleri kanıta göre uygulanır ve her önemli geç ya da geçme kararı beyana göre değil, rakamlara göre verilir.

**Düzey 5, Orkestrasyon.** Güvence sürekli iyileştirilir ve kurum genelinde bütünleşiktir. Denetçiler canlı kanıtı örnekler, risk iştahı risk profili değiştikçe uyum sağlayan orantılı kontrolleri yönlendirir ve tedarik zinciri bütünlüğü hatta doğrulanır. FK alıştırmaları rutin ve sistemler arasıdır, yoğunlaşma kararları bilinçli, sahibi olan ve acil durum planı sınanmıştır ve risk ile güvence portföy ve stratejik planlamaya örülmüştür; böylece kurum maruziyeti değiştikçe kontrolleri yeniden dengeler.

## Tartışma fikirleri

- Takımların günlük ödünleşimler için gerçekten kullanabileceği anlamlı bir risk iştahını nasıl belirlersiniz?
- Hatta otomatikleştirilen kontroller ile insan muhakemesi gerektiren kontroller arasındaki doğru sınır nedir?
- Verimlilik için yoğunlaşma riskini kabul etmek ne zaman doğru karardır ve bu kararı zaman içinde nasıl dürüst tutarsınız?
- Küçük bir dolaylı bağımlılık ile derin erişimi olan kritik bir tedarikçi için ne kadar tedarik zinciri güvencesi orantılıdır?
- Sürekli kontrol izleme, bağımsız denetimin yerini hiç tam olarak alabilir mi, yoksa bağımsızlık insan bir dış kişi mi gerektirir?
- Risk ve güvence işlevlerinin takımların çevresinden dolandığı bir teslimat darboğazına dönüşmesini nasıl önlersiniz?

## Önemli çıkarımlar

- Risk kabul edilen bir düzeye yönetilir, yaratıldığı yerde sahiplenilir ve beyanla değil kanıtla kanıtlanır.
- Kayma erken yakalansın ve kanıt işletimin yan ürünü olarak üretilsin diye anlık denetimler yerine sürekli, otomatik kontrol izlemeyi tercih edin.
- Üçüncü taraf ve tedarik zinciri riski (dolaylı açık kaynak bağımlılıkları dahil) sizin riskinizdir; envanterini çıkarın, SBOM isteyin ve kaynağı doğrulayın.
- İş sürekliliği ve FK ancak sınanırsa yetenektir; sınanmamış yedekler ve yedek geçişi varsayımdır.
- Yoğunlaşma riski ve tek hata noktaları, tekil takımlara görünmeyen portföy düzeyi meselelerdir; onları haritalayın ve birleştirmeyi bilinçli, acil durum planı sınanmış bir karar yapın.
- İş gerekçesine önlenen felaket hâkimdir; büyük öngörülemez ara sıra gelen bir kaybı küçük istikrarlı öngörülebilir bir maliyetle takas edin.

## Kaynaklar ve ileri okuma

- ISO 31000, *Risk Management: Guidelines*
- ISO/IEC 27001 and 27005, *Information Security Management* and *Information Security Risk Management*
- NIST, *Risk Management Framework (SP 800-37)* and *Security and Privacy Controls (SP 800-53)*
- NIST, *Secure Software Development Framework (SP 800-218)* and *Cybersecurity Framework*
- Committee of Sponsoring Organisations of the Treadway Commission (COSO), *Enterprise Risk Management: Integrating with Strategy and Performance*
- AICPA, *SOC 2 Trust Services Criteria*
- The Open Group, *FAIR (Factor Analysis of Information Risk)*
- Betsy Beyer et al., *Site Reliability Engineering* (Google)
- Institute of Internal Auditors, *The Three Lines Model*
