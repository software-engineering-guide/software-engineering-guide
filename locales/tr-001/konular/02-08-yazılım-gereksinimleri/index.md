# 2.8 Yazılım gereksinimleri

## Genel bakış ve motivasyon

Bir [yazılım gereksinimi](https://en.wikipedia.org/wiki/Software_requirements), bir sistemin paydaşları için kabul edilebilir olması amacıyla sağlaması, karşılaması ya da sahip olması gereken bir yetenek veya koşul beyanıdır. [Gereksinim mühendisliği](https://en.wikipedia.org/wiki/Requirements_engineering), yani bu beyanları ortaya çıkarma, çözümleme, belirtme, doğrulama ve yönetme disiplinli işi, değer zincirinin tam başında yer alır. Mimariden koda ve [kabul testine](https://en.wikipedia.org/wiki/Acceptance_testing) kadar akış aşağısındaki her şey, gereksinimleri karşılama girişimidir. Dolayısıyla gereksinimler yanlış, eksik ya da belirsiz olduğunda, yanlış şeyi doğru inşa etmeye harcanan tüm çaba saf israftır ve bu, en pahalı israftır, çünkü onu en geç keşfedersiniz. [Yazılım Mühendisliği Bilgi Birikimi](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) (SWEBOK) Yazılım Gereksinimleri bilgi alanı bunu gerçek işin büro niteliğinde bir girişi değil, gerçek bir mühendislik disiplini olarak ele alır.

Büyük takımlar için gereksinimler, birçok insanın tek tutarlı bir sistem inşa etmesini sağlayan paylaşılan anlayıştır. Tek bir geliştirici niyeti kafasında tutabilir; birçok takım boyunca yüzlerce insan tutamaz. Gereksinimler, bir yeteneğe ihtiyaç duyanlarla onu inşa edenler arasındaki sözleşme, işi takımlara bölmenin temeli ve bir şeyin ne zaman "bitti" olduğunu yargılamanın ölçüsü olur. Sorunların ve fırsatların ortaya çıktığı keşfe (bölüm 11.1); kullanıcı ihtiyaçlarını anladığınız UX temellerine (bölüm 5.1); arayüz yükümlülüklerinin sabitlendiği API'lere ve arayüz tasarımına (bölüm 2.3); işlevsel olmayan gereksinimlerin yapıyı yönlendirdiği mimariye ve kalite niteliklerine (bölüm 3.1); ve kapsamın, maliyetin ve takvimin onların etrafında planlandığı proje yönetimine (bölüm 10.6) doğrudan bağlanırlar.

Kurumsal ve kamu ortamlarında gereksinimler yasal, sözleşmesel ve güvenlik ağırlığı taşır. Düzenlemeye tabi bir sistem, her zorunlu yükümlülüğün (erişilebilirlik, gizlilik, güvenlik, kayıt saklama, mali kontrol) bir gereksinim olarak yakalandığını, gerçekleştirildiğini ve kanıtla doğrulandığını göstermelidir. Kamu tedarikleri çoğu zaman bir gereksinim belirtimi etrafında kurulur ve ödeme, denetim ve sertifikasyon her gereksinimin karşılandığına dair kanıta izlenmesine bağlıdır. Burada gereksinimler iyi uygulamadan daha fazlasıdır: hesap verebilirliğin omurgasıdır.

## Temel ilkeler

- Bir gereksinim bir ihtiyacı ya da kısıtı ifade eder, bir çözümü değil; ne ve neden olduğunu söyler, nasıl olduğunu değil.
- Her gereksinim gerekli, belirsizliksiz, doğrulanabilir, uygulanabilir ve izlenebilir olmalıdır.
- Gereksinimler paydaşlarla keşfedilir ve pazarlık edilir, yalıtılmış biçimde icat edilmez.
- İşlevsel olmayan gereksinimler ve kısıtlar mimariyi işlevsellik kadar biçimlendirir.
- Gereksinimler evrilir; değişimi dondurmak ya da görmezden gelmek yerine bilinçli yönetin.
- İhtiyaçtan gereksinime, tasarıma, teste ve kanıta izlenebilirlik hesap verebilirliğin bağ dokusudur.
- Doğru biçimsellik düzeyi alışkanlığa değil, riske, ölçeğe ve düzenleyici bağlama bağlıdır.

## Öneriler

### Gereksinimleri net tanımlayın ve kategorilere ayırın

Kategorileri bilerek adlandırın. **[İşlevsel gereksinimler](https://en.wikipedia.org/wiki/Functional_requirement)** sistemin ne yapması gerektiğini belirtir: sağladığı davranışlar, dönüşümler ve hizmetler. **[İşlevsel olmayan gereksinimler](https://en.wikipedia.org/wiki/Non-functional_requirement)** (kalite nitelikleri) bunları ne kadar iyi yapması gerektiğini belirtir: performans, kullanılabilirlik, güvenlik, kullanışlılık, erişilebilirlik, sürdürülebilirlik ve daha fazlası; bunlar mimariye (bölüm 3.1) sıkıca bağlanır. **Kısıtlar** çözüm üzerindeki pazarlık dışı sınırlardır: zorunlu teknolojiler, standartlar, bütçeler, yasal kurallar ya da mevcut sistemlere arayüzler. Ve **iş gereksinimlerini** (kuruluşun sistemi neden istediği), **kullanıcı gereksinimlerinden** (kullanıcıların neyi başarmaya ihtiyaç duyduğu) ve **sistem gereksinimlerinden** (yazılımın bu nedenle ne yapması gerektiği) ayırın. Bu düzeyleri bulandırın ve kapsam karışıklığı çok geçmeden gelir.

### Varsayımlardan değil gerçek kaynaklardan ortaya çıkarın

Ortaya çıkarma etkin keşiftir. Gereksinimleri paydaşlardan görüşmeler, çalıştaylar, gözlem, [prototipler](https://en.wikipedia.org/wiki/Software_prototyping) ve mevcut sistemlerin ve belgelerin çözümlemesi yoluyla çekin. Gözden kaçırılması kolay olanlar dahil her ilgili paydaşı bulun: operatörler, denetçiler, destek personeli ve sistemden etkilenen ama onu doğrudan hiç kullanmayan insanlar. Ortaya çıkarmayı keşif hattına (bölüm 11.1) ve UX araştırmasına (bölüm 5.1) bağlayın; böylece belirtilen istekler altta yatan ihtiyaçlara izlensin. Her gereksinimin kaynağını ve gerekçesini kaydedin, çünkü bir gereksinimin neden var olduğunu bilmek tam olarak onu sonra güvenle değiştirmenizi sağlayan şeydir.

### Çözümleyin, pazarlık edin ve önceliklendirin

Ham ortaya çıkarılan ihtiyaçlar çatışır, örtüşür ve uygulanabilir olandan fazlasına ulaşır. Çözümleme bunları uzlaştırma yoludur: gereksinimleri sınıflandırın, çatışmaları tespit edin, uygulanabilirliği ve riski tartın ve öncelikleri paydaşlarla pazarlık edin. Zaman azaldığında doğru kapsamı kesmeniz için önceliklendirmeyi açıkça, örneğin olmalı/gerekir/olabilir ayrımlarıyla ya da değer ve maliyet sıralamasıyla yapın. Ve bir model netlik kattığı yerde gereksinimleri modelleyin: süreç akışları, durum diyagramları, veri modelleri ve arayüz tanımları düzyazının gizlediği boşlukları ortaya çıkarır.

### Doğru biçimsellik düzeyinde belirtin

Gereksinimleri riske ve hedef kitleye uyan bir biçimde yazın. Yüksek güvenceli bir kamu sistemi IEEE 29148 gibi bir standarda göre yapılandırılmış resmi bir belirtimi gerektirebilir; hızlı hareket eden bir ürün takımı gereksinimleri bir iş listesinde kabul ölçütleriyle [kullanıcı hikâyeleri](https://en.wikipedia.org/wiki/User_story) olarak yakalayabilir. Her iki durumda da her gereksinim atomik, doğrulanabilir ve "hızlı", "kullanıcı dostu" ya da "vb." gibi kaygan sözcüklerden uzak olmalıdır. Kabul ölçütleri ekleyin; böylece bir gereksinimin nasıl doğrulanacağını onu yazdığınız anda tanımlarsınız. Ve gereksinimlerin e-postalara, biletlere ve slaytlara dağılmasına izin vermek yerine tek bir yetkili kaynak tutun.

### İnşa etmeden önce doğrulayın

Doğrulama, belirttiğiniz gereksinimlerin doğru olanlar olduğunu ve birbiriyle tutarlı olduğunu teyit eder. Onları paydaşlarla gözden geçirin, senaryoları gözden geçirin ve yapabildiğinizde soyut beyanları somutlaştırmak için prototipler kullanın. Doğrulama sonraki herhangi bir düzeltmeden ucuzdur: bir gereksinim incelemesinde yakalanan bir kusur, aynı kusurun üretimde yakalanmasının maliyetinin bir kesridir.

### Gereksinimleri yönetin ve izlenebilirliği sürdürün

Gereksinimler değişir. Sizin işiniz bu değişimi kontrol etmektir, ona direnmek değil. Bir değişiklik süreci kurun: önerilen her değişikliği kabul etmeden önce etkisi, maliyeti ve akış aşağısı etkisi açısından tartın. Gereksinimleri üzerinde anlaşılan noktalarda temel çizgiye alın ve sürümleyin. Her gereksinimi ileri doğru tasarıma, koda ve testlere, geri doğru geldiği ihtiyaca bağlayan **[çift yönlü izlenebilirlik](https://en.wikipedia.org/wiki/Requirements_traceability)** tutun. İzlenebilirlik, büyük takımların yaşadığı iki soruyu cevaplar: bu ihtiyaç değişirse neyi etkiler; ve teslim edilen bu özellik için hangi ihtiyaç onu haklı çıkardı? Düzenlemeye tabi bağlamlarda, uyumu yalnızca iddia etmek yerine gösterebilmeniz için izi kabul kanıtına (test sonuçları, denetim kayıtları, onaylar) kadar uzatın.

### Çevik ve plan güdümlü bağlamlara uyum sağlayın

Plan güdümlü ve düzenlemeye tabi programlarda gereksinimleri oldukça erken belirtir ve resmi değişiklik kontrolüyle temel çizgiye alırsınız. Çevik bağlamlarda gereksinimler, uygulamadan hemen önce ayrıntılandırılan ve çalışan yazılımla sürekli doğrulanan, önceliklendirilmiş, evrilen bir iş listesi olarak yaşar. Altta yatan etkinlikler ikisinde de aynıdır; yalnızca zamanlama, biçimsellik ve yapıtlar farklıdır. Büyük kuruluşlar çoğu zaman ikisini harmanlar: kararlı, yüksek güvenceli yükümlülükleri resmi olarak belirtir ve izlerken ürün davranışını yinelemeli ayrıntılandırır. Dengeyi ideolojiye değil, riske göre seçin.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | En uygun olduğu durum | Artılar | Eksiler |
|---|---|---|---|
| Resmi baştan belirtim | Yüksek güvenceli, düzenlemeye tabi, sabit kapsamlı sözleşmeler | Güçlü izlenebilirlik; net kabul temeli; denetlenebilir | Değiştirmesi yavaş; öğrenmeden önce aşırı belirtme riski |
| Çevik iş listesi | İlgili paydaşlarla evrilen ürünler | Hızlı geri bildirim; öğrenmeye uyum sağlar; inşa edilmeyen kapsamda daha az israf | Daha zayıf uzun vadeli izlenebilirlik; denetlemesi ve sözleşmelemesi daha zor |
| Melez (resmi kısıtlar + çevik davranış) | Karışık yükümlülükleri olan kurumlar | Önemli olan yerde titizlik, başka yerde esneklik | Hangi parçanın hangisi olduğuna dair muhakeme gerektirir |

Merkezi gerilim kararlılık ile öğrenme arasındadır. Gereksinimleri erken sabitlemek size sağlam bir kabul temeli ve denetlenebilirlik satın alır, ama inşa ederken öğrendiklerinize uyum sağlama yeteneğinize mal olur. Onları ertelemek uyarlanabilirlik satın alır, ama uzun vadeli izlenebilirliğe ve sözleşmesel netliğe mal olur. Gereksinim mühendisliğine daha fazla yatırım yapmak ayrıca yakın vadeli hızı daha sonra daha az yeniden işle takas eder: bir sistemin ölçeği, ömrü ve başarısızlığının sonucu arttıkça karşılığını veren bir takas. En büyük projeler ve en çok düzenlenenler sağlam biçimde yüksek yatırım tarafında durur. Düşük riskli bir dahili araç durmaz.

## Takımınızla tartışılacak sorular

1. **En yüksek riskli sistemimiz için kim paydaş sayılır ve hangilerini kabule kadar dışarıda bırakmaya devam ediyoruz?** Büyük bir programda atlanan insanlar nadiren bariz kullanıcılardır: onlar sabah 3'te işi çalıştıran operatörler, onu sertifikalandırması gereken denetçiler, başarısızlıkları karşılayan destek personeli ve hiç oturum açmayan ama verisini tuttuğunuz etkilenen kullanıcı olmayanlardır. Onları kaçırın ve gereksinimlerini en pahalı anda, kabul sırasında ya da bir düzenleyici sorduktan sonra keşfedersiniz. Toplantıya somut bir paydaş haritası getirin ve gerilim testi yapın: her zorunlu yükümlülük (erişilebilirlik, gizlilik, kayıt saklama, güvenlik) için ona sahip olan kişiyi ve onu yakalayan gereksinimi adlandırın. Bir sahip adlandıramıyorsanız bir boşluk bulmuşsunuzdur ve çözüm, ihtiyaçlarını sonra sabit bir mimariye sonradan eklemek yerine o paydaşı şimdi ortaya çıkarmaya eklemektir.

2. **Bir gereksinim değiştiğinde, değişikliği onaylamadan önce neyi etkilediğini cevaplayabiliyor muyuz?** Bu, çift yönlü izlenebilirliğinizin gerçek mi yoksa dekoratif mi olduğunun pratik testidir. Büyük ya da düzenlemeye tabi bir sistemde tek bir kural değişikliği tasarıma, koda, testlere ve kabul kanıtına yayılabilir ve onu körü körüne onaylamak, eskiden karşıladığı bir kuralı sessizce ihlal eden uyumlu görünen bir sistem yayımlamanın yoludur. Toplantıya yakın tarihli bir değişiklik talebi getirin ve onu toplantıda ileri doğru izlemeye çalışın: bir öğleden sonralık arkeoloji alıyorsa izlenebilirliğiniz işini yapmıyordur. Cevap değişiklik sürecinizi yeniden biçimlendirmelidir; böylece etki değerlendirmesi elle bir av değil, canlı bir ize karşı hızlı bir sorgu olur ve temel çizgiler ve sürümleme size karşı değişiklik yapacağınız kararlı bir nokta verir.

3. **Gereksinimlerimizin tek yetkili kaynağı nerede yaşıyor ve ne kadar gerçek onun dışına dağılmış durumda?** Gereksinim yayılması (gerçek belirtimin e-postalara, biletlere, slaytlara ve birinin hafızasına dağılması) büyük takımlarda en yaygın başarısızlıklardan biridir ve neyin üzerinde anlaşıldığını göstermeniz gereken denetlenen sistemlerde ölümcüldür. Hangi kayıt sisteminin kanonik olduğuna yüksek sesle karar verin ve başka yerde belirtilen her şeyi kaynağı ve gerekçesiyle oraya inene kadar taslak sayın. Kanıtı getirin: yakın tarihli kaç kapsam anlaşmazlığının iki kişinin farklı "son" sürümleri anmasına dayandığını sayın. Sayı sıfırdan büyükse eylem tek bir kaynakta birleşmek ve her gereksinimin gerekçesini yazmaktır, çünkü bir gereksinimin neden var olduğunu bilmek tam olarak onu sonra güvenle değiştirmenizi ya da bırakmanızı sağlayan şeydir.

4. **İşlevsel olmayan gereksinimlerimiz mimariyi yönlendirecek kadar erken mi yakalanıyor, yoksa yapı sabitlendikten sonra keşfetmeye mi devam ediyoruz?** Performans, kullanılabilirlik, güvenlik ve erişilebilirlik yükümlülükleri mimariyi çoğu özellikten daha fazla biçimlendirir ve büyük bir programda en sık çok geç, onları karşılaması gereken yapı zaten betona dökülmüşken ortaya çıkan gereksinimlerdir. Karşıt çekim gerçektir: işlevsel davranış paydaşların yüksek sesle istediği ve iyi gösterdiği şeydir, "tepe yükte saniyenin altında yanıt" ya da "WCAG erişilebilirlik uyumu" gereksinimi ise ihlal edilene kadar görünmezdir. En yüksek riskli sisteminiz için mevcut işlevsel olmayan gereksinimler listesini, her birinin zaman çizelgesinde yazıldığı noktayı ve mimarinin (bölüm 3.1) onları açık yönlendiriciler olarak mı yoksa çıkarımla mı aldığını getirin. Kurumsal ve kamu ortamlarında zorunlu kalite yükümlülüklerini (şifreleme, kayıt saklama, erişilebilirlik yasası) ekleyin ve her birinin bir varsayım değil, tasarıma verilmiş yazılı, ölçülebilir bir gereksinim olduğunu kontrol edin, çünkü bir kalite niteliğini kabulden sonra sonradan eklemek bütçelerin ve takvimlerin sessizce öldüğü yerdir.

5. **Sahip olduğumuz her sistem için hangi biçimsellik düzeyi doğru ve onu riske göre mi yoksa alışkanlığa göre mi seçiyoruz?** Tek bir büyük kuruluş genellikle bir at-kullan dahili araçtan hayati ya da güvenlikle ilgili düzenlemeye tabi bir platforma kadar yelpazede sistemler işletir ve hepsine tek bir tören uygulamak ya düşük riskli işi evrağa gömer ya da yüksek riskli işi yetersiz belirtilmiş bırakır. Gerilim, resmi baştan belirtimin denetlenebilirliği ve sağlam kabul temeli ile evrilen bir iş listesinin hızlı geri bildirimi ve azalan israfı arasındadır ve çoğu kurum için dürüst cevap bilinçli bir harmandır: kararlı, yüksek güvenceli yükümlülükleri resmileştirin ve izleyin, ürün davranışını yinelemeli ayrıntılandırın. Sistemlerinizin başarısızlık sonucuna, düzenleyici maruziyete ve değişim oranına göre sıralanmış kısa bir envanterini getirin ve her biri için gerçekte kullandığınız biçimselliği riskin gerektirdiği biçimsellikle birlikte adlandırın. Bir ihale çağrısına ve IEEE 29148 gibi bir standarda bağlı bir kamu programı için biçimsellik kısmen sözleşmeyle belirlenir; bu yüzden tartışma, denetimin bağlı olduğu izlenebilirliği bozmadan çevik ayrıntılandırmayı üstüne nerede katmanlayabileceğinizdir.

6. **En yüksek riskli sistemimizdeki her gereksinim doğrulanabilir mi ve her biri, gereksinim yazıldığı anda yazılmış kabul ölçütleri taşıyor mu?** Doğrulayamadığınız bir gereksinim gereksinim değil, bir dilektir ve "hızlı", "güvenli" ya da "kullanıcı dostu" gibi kaygan sözcükler tam olarak kimse onları başarısız kılamadığı için incelemeyi geçer. Büyük bir takım için bu iki kat önemlidir: doğrulanamaz gereksinimler kabulde kapsam anlaşmazlıkları üretir ve bir özelliğin ne zaman gerçekten bittiğini söylemeyi imkansız kılar. Karşıt değerlendirme hızdır; her gereksinime ölçülebilir bir ölçüt ve bir doğrulama yöntemi eklemek, düzyazı yazmaktan baştan daha yavaştır, ama en pahalı geç yeniden işe karşı en ucuz savunmadır. Yakın tarihli gereksinimlerden bir örnek getirin ve her birini basit bir çıtaya karşı test edin: atomik mi, ölçülebilir mi ve nasıl kontrol edileceğini adlandırıyor mu. Düzenlemeye tabi ve kamu bağlamlarında testi kanıta kadar genişletin: izlenmiş, geçen kabul kanıtı olmayan bir gereksinim, yazılım ne yapıyor görünürse görünsün teslim edilmiş sayılmaz; bu yüzden kabul ölçütleri eninde sonunda üretmeniz gereken uyum kaydının tohumudur.

## Sektör merceği

**Girişim.** Küçük bir takım ve az pistle gereksinimleri paçayı kurtarabildiğiniz kadar hafif tutun: bir belirtim belgesi değil, tek paylaşılan iş listesinde kabul ölçütlü kullanıcı hikâyeleri. Burada bile karşılığını veren disiplin, inşa etmeden önce gerçek kullanıcılarla konuşmak ve her hikâyenin kaynağını ve gerekçesini kaydetmektir; böylece yanlış özelliği inşa ederek boşa harcayacağınız hafta kurtardığınız hafta olur. Resmi izlenebilirliği atlayın, ama gerçek ihtiyacın ne olduğunu söyleyen konuşmayı asla atlamayın.

**Küçük işletme.** Muhtemelen iş analistiniz ya da gereksinim uzmanınız yoktur; bu yüzden iş müşteriye en yakın olana düşer ve satın alma ya da inşa etme sorusu baskındır. Gereksinimleri ihtiyaç duyduğunuz sonuçların kısa, önceliklendirilmiş bir listesi olarak çerçeveleyin, sonra ısmarlama bir inşayı belirtmek için değil, hazır araçları değerlendirmek için kullanın. Altta yatan ihtiyacı bir satıcının özellik listesinden ayırmakta katı olun, çünkü "X ürününe ihtiyacımız var" olarak yazılmış bir gereksinim, gerçek ihtiyacı karşılayacak daha ucuz seçenekleri sessizce dışlar.

**Kurumsal.** Ölçek gereksinimleri birçok takımın tek tutarlı sistem inşa etmesini sağlayan sözleşmeye çevirir; bu yüzden öncelik tutarlı uygulanan standart bir süreçtir: tanımlı kategoriler, ihtiyaçtan teste çift yönlü izlenebilirlik, tek yetkili kaynak ve temel çizgilerle kontrollü değişiklik. İş, kullanıcı ve sistem gereksinimlerini açıkça ayırın ve işlevsel olmayan gereksinimleri yönlendirici olarak mimariye verin; böylece kapsam ve kalite yükümlülükleri takımlar arasında dağılmaz. Kararlı, yüksek güvenceli yükümlülükler için resmi belirtimi ürün davranışının çevik ayrıntılandırılmasıyla harmanlayın ve dengeyi herhangi bir takımın tercihiyle değil, riskle yönetin.

**Kamu.** Tedarik kuralları çoğu zaman tüm sözleşmeyi, sıklıkla IEEE 29148 gibi bir standarda göre yapılandırılmış, bir gereksinim belirtimi etrafında kurar; bu yüzden kesinlik ve eksiksizlik isteğe bağlı değil, sözleşmeseldir. Her gereksinimi tasarıma, test senaryolarına ve kabul kanıtına bağlayan bir gereksinim izlenebilirlik matrisi tutun, çünkü satıcı ödemesi, denetim ve çalışma yetkisi gösterilen kapsama bağlıdır. Şeffaflık ve kamusal hesap verebilirlik çıtayı daha da yükseltir: erişilebilirlik, gizlilik ve kayıt saklama için zorunlu yükümlülüklerin her biri açık, doğrulanabilir bir gereksinim olarak görünmelidir ve izlenmiş, geçen kanıtı olmayan bir gereksinim basitçe teslim edilmemiştir.

## Örnekler

**Girişim.** Bir planlama uygulaması inşa eden dört kişilik bir girişim gereksinimleri resmi bir belirtim değil, paylaşılan bir iş listesinde kabul ölçütlü kullanıcı hikâyeleri olarak yakalar. Takvim eşitleme özelliğini yazmadan önce kurucu beş olası müşteriyle konuşarak bir öğleden sonra geçirir ve gerçek ihtiyacın varsaydıkları eşitleme değil, iki araç arasında çifte rezervasyonlardan kaçınmak olduğunu öğrenir. O tek konuşma hikâyeyi yeniden çerçeveler ve yanlış şeyi inşa etmenin bir haftasını kurtarır. Bu ölçekte bile her hikâyenin kaynağını ve gerekçesini yazarlar; böylece öncelikler kaydığında kapsamı neden var olduğunu yeniden tartışmadan bırakabilir ya da yeniden işleyebilirler.

**Kurumsal.** Çok uluslu bir banka kredi başlatma platformunu değiştirir. Gereksinim takımı iş gereksinimlerini (onay süresini azalt, kredi düzenlemelerini karşıla), kullanıcı gereksinimlerini (kredi görevlilerinin teklifleri tek görünümde karşılaştırması gerekir) ve sistem gereksinimlerini (platform üç çekirdek sistemle entegre olmalı) ayırır. İşlevsel olmayan gereksinimler (yaygın sorgular için saniyenin altında yanıt, %99,95 kullanılabilirlik, kişisel verilerin şifrelenmesi) açıkça yakalanır ve yönlendirici olarak mimariye (bölüm 3.1) verilir. Her gereksinim iş listesi üzerinden otomatik kabul testlerine izlenir. Böylece bir düzenleyici belirli bir kredi kuralının nasıl uygulandığını sorduğunda, takım yalnızca kuraldan onu doğrulayan teste giden izi takip eder.

**Kamu.** Ulusal bir kurum, bir yardım uygunluk sistemini resmi bir ihale çağrısıyla satın alır. Sözleşme, işlevsel uygunluk kurallarını, zorunlu erişilebilirlik uyumunu, gizlilik ve kayıt saklama kısıtlarını ve güvenlik kontrollerini kapsayan IEEE 29148'e göre yapılandırılmış bir gereksinim belirtimine bağlanır. Bir gereksinim izlenebilirlik matrisi her gereksinimi tasarım öğelerine, test senaryolarına ve kabul kanıtına bağlar. Satıcı ödemeleri ve çalışma yetkisi (sistemi üretimde çalıştırmak için resmi onay) gösterilen kapsama bağlıdır. İzlenmiş, geçen kabul kanıtı olmayan bir gereksinim, yazılım ne yapıyor görünürse görünsün, basitçe teslim edilmiş sayılmaz.

## İş gerekçesi: motivasyonlar, YG ve TSM

Gereksinim mühendisliğinin ekonomik argümanı kusurları geç düzeltmenin maliyetine dayanır. Sektör çalışmaları tutarlı biçimde gereksinim kusurlarının proje başarısızlığının en yaygın ve en pahalı nedenleri arasında olduğunu ve bir kusuru düzeltme maliyetinin gereksinim aşamasından üretime büyüklük sıralarıyla tırmandığını bulur. Bu yüzden gereksinimleri netleştirmeye ve doğrulamaya harcanan para gerçekte kaldıraçtır: baştaki mütevazı bir yatırım sizi yanlış şeyi inşa etmekten, test etmekten ve işletmekten kurtarır.

Gereksinimlerin toplam sahip olma maliyeti, sistemin tüm ömrü boyunca ortaya çıkarma, belirtme, araçlar ve değişiklik yönetiminin süregelen çabasını içerir; tek seferlik bir maliyet değildir. Karşısında kötü gereksinimlerin maliyeti durur: yeniden iş, kapsam anlaşmazlıkları, takvim aşımları, başarısız kabul, sözleşmesel cezalar ve düzenlemeye tabi ortamlarda para cezaları ya da yetkinin kaybı. Liderlik için gereksinim olgunluğunu risk azaltma ve öngörülebilirlik olarak çerçeveleyin. Gereksinim oynaklığını, kusur kökenini ve teslim edilen işin doğrulanmış bir ihtiyaca izlenebilir payını izleyin ve bunları proje yönetimi tahminlerine (bölüm 10.6) bağlayın. Getiri bir özellik olarak görünmez. Hiç yaşanmayan başarısızlıklar ve yeniden iş olarak görünür.

## Anti-kalıplar ve tuzaklar

- **Gereksinim kılığında çözümler:** altta yatan ihtiyaç yerine seçilmiş bir teknolojiyi ya da ekran düzenini belirtmek; daha iyi seçenekleri dışlar.
- **Belirsiz dil:** ölçülebilir bir ölçüt olmadan "hızlı", "güvenli", "sezgisel"; gereksinimi doğrulanamaz kılar.
- **[Altın kaplama](https://en.wikipedia.org/wiki/Gold_plating_(software_engineering)):** hiçbir paydaşın gerçekte ihtiyaç duymadığı gereksinimleri yakalamak; kapsamı ve maliyeti şişirir.
- **Eksik işlevsel olmayan gereksinimler:** performans, güvenlik ya da erişilebilirlik yükümlülüklerini yalnızca mimari sabitlendikten sonra keşfetmek.
- **Gereksinim yayılması:** gerçeğin e-postalara, biletlere ve slaytlara dağılması ve yetkili kaynak olmaması.
- **Dondurulmuş ya da kontrolsüz değişim:** ya tüm değişikliği reddetmek ya da etki değerlendirmesi olmadan her değişikliği kabul etmek.
- **İzlenebilirlik yok:** bir değişikliğin neyi etkilediğini ya da bir özelliğin neden var olduğunu cevaplayamamak; denetlenen sistemlerde ölümcül.
- **Analiz felci:** çalışan yazılımdan öğrenmeyi geciktiren sonsuz belirtim.
- **Göz ardı edilen paydaşlar:** kabule kadar dışarıda bırakılan operatörler, denetçiler ve etkilenen kullanıcı olmayanlar.

## Olgunluk modeli

- **Düzey 1, Başlangıç.** Gereksinimler örtük ya da sözlüdür, tutarsız ve reaktif yakalanır. Kapsam anlaşmazlıkları ve yeniden iş yaygındır; izlenebilirlik, kabul ölçütü ve tanımlı süreç yoktur.
- **Düzey 2, Geliştirme.** Bazı takımlar gereksinimleri yazar ve proje başına izler; temel önceliklendirme ve geçici değişiklik ele alma ile. Uygulamalar vardır ama takıma ve kişiye göre değişir; bu yüzden kategoriler, biçimsellik ve kalite kuruluş genelinde tutarsızdır.
- **Düzey 3, Standartlaştırma.** Standart bir gereksinim süreci belgelenir ve kuruluş genelinde uygulanır: tanımlı kategoriler, ortaya çıkarma ve doğrulama uygulamaları, yazım anında eklenen kabul ölçütleri, tek yetkili kaynak ve ihtiyaçtan teste çift yönlü izlenebilirlik; çevik ya da plan güdümlü bağlama tutarlı uyarlanır.
- **Düzey 4, Yönetme.** Süreç veriyle ölçülür ve kontrol edilir. Gereksinim oynaklığı, kusur kökeni, izlenebilirlik kapsamı ve teslim edilen işin doğrulanmış bir ihtiyaca izlenebilir payı temel çizgilere karşı izlenir; izlenebilirlik kabul kanıtına ve uyuma uzanır ve gereksinim metrikleri proje tahminini (bölüm 10.6) besler; böylece değişim ve kalite kararları görüşe değil kanıta dayanır.
- **Düzey 5, Orkestrasyon.** Gereksinim uygulaması sürekli iyileştirilir ve kuruluş genelinde bütünleşir. Biçimsellik riske ve sonuca göre uyarlamalı ayarlanır, ortaya çıkarma ve izlenebilirlik araçları keşfe, mimariye ve teslimata bağlanır ve kuruluş yinelenen gereksinim kusurlarını koda ulaşmadan önlemek için kendi ölçüm geçmişini kullanır.

## Tartışma fikirleri

- Kıdemli bir paydaş bir gereksinimi çözüm olarak belirttiğinde gerçek bir gereksinimi erken bir çözümden nasıl ayırırsınız?
- En yüksek riskli sisteminiz ile en düşük riskli sisteminiz için doğru gereksinim biçimselliği düzeyi nedir ve kim karar verir?
- Hızlı hareket eden bir çevik iş listesinde çift yönlü izlenebilirliği bürokratik yüke dönüşmeden nasıl güncel tutarsınız?
- Kuruluşunuzda hangi işlevsel olmayan gereksinimler en sık çok geç keşfediliyor ve neden?
- Düzenlemeye tabi bir programda bir gereksinimin karşılandığına dair yeterli kabul kanıtı neyi oluşturur?
- Yapay zeka destekli ortaya çıkarma ve belirtim araçları gereksinim uygulamanızı nasıl değiştirmeli ve hangi yeni riskleri getirir?

## Önemli çıkarımlar

- Gereksinimler çözümleri değil ihtiyaçları ve kısıtları belirtir; gerekli, belirsizliksiz, doğrulanabilir ve izlenebilir olmalıdır.
- İşlevsel, işlevsel olmayan ve kısıt gereksinimlerini ve iş, kullanıcı ve sistem düzeylerini ayırın.
- Gerçek paydaşlardan ortaya çıkarın, çözümleyin ve önceliklendirin, uygun biçimsellikte belirtin, inşa etmeden önce doğrulayın ve değişimi yönetin.
- İhtiyaçtan kabul kanıtına çift yönlü izlenebilirlik, özellikle düzenlemeye tabi ortamlarda hesap verebilirliğin omurgasıdır.
- Çevik ve plan güdümlü bağlamlar aynı etkinlikleri paylaşır; zamanlama, biçimsellik ve yapıtlarda farklılaşırlar; bu yüzden riske göre seçin.
- Kötü gereksinimlerin maliyeti geç ödenir ve katlanır; erken yatırım yeniden işe ve başarısız kabule karşı kaldıraçtır.

## Kaynaklar ve ileri okuma

- IEEE and ISO/IEC, *Guide to the Software Engineering Body of Knowledge (SWEBOK)*, Software Requirements knowledge area
- Karl Wiegers and Joy Beatty, *Software Requirements*
- ISO/IEC/IEEE 29148, *Systems and software engineering: Life cycle processes: Requirements engineering*
- Suzanne Robertson and James Robertson, *Mastering the Requirements Process*
- Dean Leffingwell, *Agile Software Requirements*
- Mike Cohn, *User Stories Applied*
- Ian Sommerville, *Software Engineering* (requirements engineering chapters)
