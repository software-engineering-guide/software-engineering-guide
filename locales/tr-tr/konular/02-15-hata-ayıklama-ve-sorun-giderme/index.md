# 2.15 Hata ayıklama ve sorun giderme

## Genel bakış ve motivasyon

Hata ayıklama, bir sistemin yapmaması gereken bir şeyi neden yaptığını bulmanın disiplinli işidir; sorun giderme ise aynı becerinin zaman baskısı altında çalışan bir üretim sistemine çevrilmesidir. İkisi de [bilimsel yöntemin](https://en.wikipedia.org/wiki/Scientific_method) kusurlara uygulanmasıdır: şaşırtıcı bir davranışı gözlemler, nedeni hakkında bir hipotez kurar, onu doğrulayacak ya da çürütecek bir deney tasarlar ve neyi değiştireceğinizi sezginizin değil kanıtın söylemesine izin verirsiniz. Bu şekilde yapıldığında hata ayıklama öğrenilebilir, öğretilebilir bir mühendislik becerisidir. Folklor olarak yapıldığında batıl inanca dönüşür: rastgele satırları değiştirmek, sunucuları yeniden başlatmak ve ummak.

Büyük bir takım için fark pahalıdır. Tek bir zor kusur birkaç hizmetteki mühendisleri içine çekebilir, nöbet saatlerini tüketebilir ve bir sürümü durdurabilir. Her kişi sezgiyle hata ayıkladığında bu çaba bileşik olmaz, çünkü kimse başkasının ne denediğini yeniden üretemez ya da açıklayamaz. Takım bir yöntemi paylaştığında (önce yeniden üret, aramayla yalıt, hatayı başarısız bir testte yakala, sonra düzelt) aynı çaba tekrarlanabilir bir sürece ve büyüyen bir gerileme takımına dönüşür. Hata ayıklama, test stratejisine (bölüm 2.4), yazılım kalitesine (bölüm 2.11) ve kodu en baştan teşhis edilebilir kılan inşa alışkanlıklarına (bölüm 2.9) sıkıca bağlanır.

Kurumsal ve kamu ortamlarında bahisler yükselir. Kurumsal kusurlar hizmet ve takım sınırlarını geçer; bu yüzden belirtiyi gören kişi nadiren nedene sahip olan kişidir. Kamu sistemleri çoğu mühendisin hiç karşılaşmadığı kısıtlar ekler: üretime bir hata ayıklayıcı bağlayamayacağınız hava boşluklu ya da kısıtlı ortamlar, yapıtlardan teşhis edilmesi gereken yeniden üretilebilir derlemeler ve neyi neden değiştirdiğinizi kaydetmesi gereken denetim izleri. Üçünde de amaç aynıdır: tahmini kanıtla değiştirmek.

## Temel ilkeler

- **Kuramlaştırmadan önce yeniden üretin.** İstek üzerine tetikleyemediğiniz bir hata bir kusur değil, bir söylentidir.
- **Hata ayıklama hipotez testidir.** Neye inandığınızı belirtin, sonra sizi yanlış çıkarabilecek en ucuz deneyi tasarlayın.
- **Önce hatayı ve yığın izini okuyun.** Sistem genellikle bir satırı değiştirmeden önce nerede bozulduğunu söyler.
- **Sorun uzayında arayın, taramayın.** Yukarıdan aşağı okumak yerine her adımda şüpheli bölgeyi yarılayın.
- **Asgariye indirin.** Yalnızca temel tetikleyici kalana kadar durumu sadeleştirin.
- **Her seferinde tek değişiklik.** Saçma atışı düzenlemeler, hangi değişikliğin önemli olduğunu söyleyecek kanıtı yok eder.
- **Düzeltmeden önce hatayı başarısız bir testte yakalayın.** Düzeltme yalnızca o test yeşile döndüğünde ve yeşil kaldığında kanıtlanır.
- **En yakın belirtiyi değil, kök nedeni bulun.** Belirtiyi gizleyen bir yama kusurun geri dönmesine izin verir.

## Öneriler

### Hiçbir şeyi değiştirmeden önce kusuru güvenilir biçimde yeniden üretin

İlk işiniz güvenilir bir yeniden üretimdir: hatayı istek üzerine tetikleyen bir dizi adım ya da otomatik bir durum. Onsuz gerçek bir düzeltmeyi bir tesadüften ayıramazsınız, çünkü belirti hiç kontrol etmediğiniz nedenlerle gelip gidebilir. Girdileri, ortamı, sürümleri ve zamanlamayı sabitleyin. Hata aralıklıysa, yeniden üretim güvenilir olana kadar onu ortaya çıkaran gizli değişkeni (belirli bir veri kaydı, bir saat sınırı, eşzamanlı bir istek) arayın. Güvenilir bir yeniden üretim hata ayıklamadaki tek en değerli yapıttır, çünkü ondan sonraki her şey ölçülebilir hale gelir.

### Koda dokunmadan önce hatayı, günlükleri ve yığın izini okuyun

Tek bir kuram kurmadan önce sistemin size zaten söylediğini okuyun. [Yığın izi](https://en.wikipedia.org/wiki/Stack_trace) (başarısızlık anındaki çağrı zincirinin kaydı) genellikle başarısız olan dosyayı, satırı ve diziyi adlandırır. İstisna mesajı, çevresindeki günlük satırları ve kapsamdaki değerler siz hiçbir şeyi değiştirmeden aramayı daraltır. Mühendisler, izin ilk satırda dışladığı nedenler hakkında kuramlaştırarak saatler harcar. Hata çıktısını ilk tanık olarak ele alın, dikkatle ve tamamen okuyun ve ancak sonra neyi araştıracağınıza karar verin.

### Sorun uzayının ikili aramasıyla yalıtın

Kodu yukarıdan aşağı taramayın. Arayın. [İkili aramayı](https://en.wikipedia.org/wiki/Binary_search_algorithm) kullanın: durumun hâlâ iyi olduğu bir nokta ve zaten kötü olduğu bir nokta bulun, sonra orta noktayı kontrol edin ve her seferinde şüpheli bölgeyi yarılayarak tekrarlayın. Bu bin satırlık bir aramayı on soruya çevirir. Gerileme bir dizi commit boyunca ortaya çıktığında, aynı fikri geçmişe ikiye bölmeyle uygulayın: `git bisect` commit aralığını yürür ve kusuru getiren tam değişikliği adlandırana kadar her revizyonu iyi ya da kötü olarak işaretlersiniz. İyi ya da kötü testini otomatikleştirin ve ikiye bölme kendi kendine çalışır.

### Asgari yeniden üretilebilir örneğe indirin

Hatayı tetikleyebildiğinizde onu küçültün. [Asgari yeniden üretilebilir örnek](https://en.wikipedia.org/wiki/Minimal_reproducible_example), hâlâ başarısız olan en küçük girdi ve kod yoludur: daha fazla kaldırmanın hatayı ortadan kaldırdığı noktaya kadar veriyi, özellikleri ve adımları çıkarın. İndirgeme angarya değildir; ortadan kaldırdığınız her öğe dışladığınız bir nedendir; bu yüzden asgari durum çoğu zaman doğrudan kusura işaret eder. Girdi büyük ya da yapılandırılmışsa, asgari başarısız alt kümeyi bulmak için başarısız bir girdinin parçalarını sistematik olarak kaldıran bir algoritma olan [delta hata ayıklamayla](https://en.wikipedia.org/wiki/Delta_debugging) küçültmeyi otomatikleştirin. Küçük, kendi içinde bütün bir yeniden üretim aynı zamanda başka bir takıma verebileceğiniz en iyi hata raporudur.

### Günlüklerle donatın, sonra etkileşimli bir hata ayıklayıcı kullanın

Aracı hataya uydurun. Günlük tutma ve hedefli donatım, davranışı zaman içinde, süreçler arasında ya da duraklatamayacağınız bir ortamda görmeniz gerektiğinde en iyisidir. Kesme noktaları koymanıza, satır satır adımlamanıza ve canlı durumu incelemenize izin veren etkileşimli bir hata ayıklayıcı, kodu yerelde çalıştırabildiğinizde ve tek bir çalıştırmayı yakından izlemeniz gerektiğinde en iyisidir. Donatımı dağınık print ifadeleri olarak değil, bir hipoteze bağlı bilinçli bir deney olarak ekleyin ve hata çözüldüğünde onu kaldırın ya da kalıcı yapılandırılmış günlüğe terfi ettirin. Üretimde, gözlemlenebilirlik güdümlü hata ayıklamaya yaslanın: yüksek kardinaliteli olaylar ve dağıtık izleme (bölüm 9.2) tek bir isteği birçok hizmet boyunca izlemenizi sağlar; bu, hata ayıklayıcı bağlayamayacağınız dağıtık bir sistemde hata ayıklamanın çoğu zaman tek yoludur.

### Düzeltmeden önce hatayı yakalayan başarısız bir test yazın

Düzeltmeyi yazmadan önce hata yüzünden başarısız olan bir test yazın. Bu üç şeyi aynı anda yapar: nedeni gerçekten anladığınızı kanıtlar, "düzeltildi"nin tam olarak ne demek olduğunu tanımlar ve kalıcı bir koruma olur. Sonra düzeltmeyi yapın ve testin yeşile döndüğünü izleyin. O test artık takımınıza bir [gerileme testi](https://en.wikipedia.org/wiki/Regression_testing) koruması olarak katılır; böylece aynı kusur fark edilmeden dönemez. Bu uygulama hata ayıklamayı doğrudan test stratejinize (bölüm 2.4) bağlar: çözdüğünüz her zor hata takımı bulduğundan daha güçlü bırakır ve kararsız bir test aynı muameleyi görür (yeniden deneme ek açıklaması yerine belirlenimsizliği yeniden üretin, sonra karşı koruma koyun).

### Kök nedeni bulun ve analizi suçlamasız tutun

Belirtiyi düzeltmek hatayı düzeltmek değildir. Başarısızlığı gerçek kaynağına kadar izleyin; maskelemek yerine kaldırabileceğiniz bir nedene ulaşana kadar her katmanda neden diye sorun. Üretime ulaşan kusurlar için olay yönetiminin (bölüm 9.3) parçası olarak suçlamasız bir kök neden analizi yürütün: kusurun yayımlanıp sağ kalmasına izin veren sistem ve süreç koşullarına odaklanın, satırı yazan bireye asla. Suçlama bilgiyi yer altına iter ve hata ayıklama bilgiyle çalışır. Çıktı hem bir düzeltme hem de o kusur sınıfının bir dahaki sefere daha erken nasıl yakalanacağına dair bir değişikliktir.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
|---|---|---|
| Günlük tutma ve donatım | Üretimde ve dağıtık sistemlerde çalışır; davranışı zaman içinde yakalar | Gürültü, maliyet ve günlük yayılması; zamanlama hatalarını bozabilir |
| Etkileşimli hata ayıklayıcı | Kesin, canlı durum incelemesi; yerel hatalar için hızlı | Kısıtlı ya da hava boşluklu üretimde işe yaramaz; eşzamanlılık hatalarını gizleyebilir |
| Önce yeniden üretme disiplini | Tahmini ölçüme çevirir; başarısız bir testi mümkün kılar | Baştan yavaş; bazı hataları tetiklemek gerçekten zordur |
| İkili arama ve ikiye bölme | Tanımadığınız kodda bile hızlı yalıtım | Güvenilir bir iyi ya da kötü testi gerektirir; hatalar etkileştiğinde zor |
| Delta hata ayıklama indirgemesi | Devasa girdileri tetikleyiciye otomatik küçültür | Kurulum maliyeti; başarısızlığın belirlenimci olduğunu varsayar |
| Belirtiyi şimdi düzeltmek | Baskı altında hizmeti hızla geri getirir | Kök nedenin dönmesine izin verir; borç biriktirir |

Merkezi gerilim hız ile kesinlik arasındadır. Bir üretim olayı sırasında hizmeti geri getirmek için önce kanamayı durdurmanız (bir geri alma ya da belirti yaması) gerekebilir ve bu meşrudur. Hata orada durmaktır. Gerilimi iki işi ayırarak çözün: kullanıcıları korumak için hızlı hafifletin, sonra kusuru kapalı saymadan önce yeniden üretin, kök nedeni bulun ve gerileme korumasını ekleyin. Takipsiz bir belirti düzeltmesi, yeniden karşılaşmayı kabul ettiğiniz bir hatadır.

## Takımınızla tartışılacak sorular

1. **Biri zor bir hatayla karşılaştığında ilk yaptığı şey nedir ve bu yeniden üretmek mi yoksa tahmin etmek mi?** Dürüst cevap, takımınızın paylaşılan bir yöntemi mi yoksa özel folklorla dolu bir odası mı olduğunu ortaya çıkarır. İnsanlardan son zor kusurlarını yüksek sesle anlatmalarını isteyin: önce güvenilir bir yeniden üretim mi elde ettiler, yoksa kodu değiştirmeye ve bir şeyleri yeniden başlatmaya mı başladılar? Önce yeniden üreten bir takım bir hatayı insanlar arasında devredebilir, çünkü yeniden üretim yolculuk eder; tahmin eden takım edemez, çünkü her deneme tekrarlanamazdır. Takım büyüdükçe bu daha çok önem kazanır, çünkü bir belirtiyi gören kişi giderek onu düzeltebilecek kişi olmaz. Varsayılan tahminse, önce yeniden üretmeyi bir norm olarak kararlaştırın ve temiz bir yeniden üretimi bir hata biletine giriş bedeli yapın.

2. **Düzelttiğimiz hatalar geri geliyor mu ve gelseler bilir miydik?** Geri dönen bir kusur, kök nedeni hiç kaldırılmamış ve düzeltmesi bir testle hiç korunmamış bir kusurdur. Son çeyreğin olaylarını ve yeniden açılan biletlerini çekin ve kaçının daha önceki hataların tekrarı ya da yakın akrabası olduğunu sayın. Her tekrar, takımın bir belirtiyi yamaladığının, başarısız testi atladığının ya da kök neden analizini çok erken bıraktığının kanıtıdır. Çözüm bir kuraldır: eski davranışta başarısız olan ve yenisinde geçen bir test takıma katılana kadar hiçbir hata kapatılmaz. Yakın tarihli yinelenen bir hata getirin ve onu hangi korumanın yakalayacağını sorun, çünkü eksik olan o korumadır.

3. **Onlara dokunmamıza izin verilme biçimi göz önüne alındığında üretim sistemlerimizde hiç hata ayıklayabilir miyiz?** Kurumsal ve özellikle kamu ortamlarında genellikle bir hata ayıklayıcı bağlayamaz, gerçek veriyle yeniden üretemez ve bir denetim izi olmadan çalışan bir sistemi değiştiremezsiniz. Tek hata ayıklama tekniğiniz yerel etkileşimli bir hata ayıklayıcıysa, tam olarak en zor hataların yaşadığı yerde kördürsünüz. Bir üretim başarısızlığının gerçekte arkasında ne kanıt bıraktığını sorun: yapılandırılmış günlükler, dağıtık izler (bölüm 9.2), çekirdek dökümleri ya da yeniden üretilebilir derleme yapıtları. Gelecekteki bir olayın teşhis edilebilir olması için neyi varsayılan olarak yakalamanız gerektiğine şimdi karar verin, çünkü zaten gerçekleşmiş bir başarısızlığa donatım ekleyemezsiniz. Düzenlemeye tabi ortamlarda aynı izin denetim yükümlülüklerinizi de karşıladığını doğrulayın.

4. **Bir üretim olayı kanamayı hızla durdurmamızı gerektirdiğinde, kök nedenin sonradan yine de bulunduğundan nasıl emin oluyoruz?** Bir olay sırasında geri alma ya da belirti yaması kullanıcıları korumak için doğru ilk harekettir, ama tehlike, bilet hizmet döner dönmez kapanır ve altta yatan kusurun hiç teşhis edilmemesidir. Büyük bir takım için borcun görünmez biçimde biriktiği yer burasıdır, çünkü aynı başarısızlık sınıfı aylar sonra farklı bir hizmette ve farklı bir nöbetçi mühendisle yeniden ortaya çıkar. Son birkaç birinci ciddiyet olayınızı getirin ve her birini kontrol edin: hafifletmeyi bir yeniden üretim, bir kök neden analizi ve bir gerileme koruması izledi mi, yoksa hikâye "hizmet geri geldi"de mi bitti? Hafifletilmiş bir olayın kök neden anlaşılana ve korunana kadar açık kalması konusunda açık bir kural üzerinde anlaşın ve o takibin sahibini adlandırın. Kurumsal ve kamu ortamlarında bunu olay yönetimi sürecinize (bölüm 9.3) bağlayın; böylece olay sonrası inceleme, bir sonraki yangın başladığında kayan bir nezaket yerine zorunlu, denetlenebilir bir adım olur.

5. **Bir başarısızlığın ne kadarını sonradan yeniden kurabiliriz ve varsayılan olarak neyi yakalayacağımıza kim karar verdi?** Zaten gerçekleşmiş bir başarısızlığa donatım ekleyemezsiniz; bu yüzden herhangi bir olayın teşhis edilebilirliği, yayımlamayı seçtiğiniz günlükler, izler, metrikler ve dökümlerle önceden sabitlenir. Rakip değerlendirme maliyet ve gürültüdür: yüksek kardinaliteli olaylar ve tam izleme bedava değildir ve fazla günlük tutma sinyali gömer, depolamayı şişirir ve düzenlenen bağlamlarda veri saklama maruziyetinizi artırır. Gerçek yakın tarihli bir olay getirin ve arkasında ne kanıt bıraktığını sorun, sonra geriye doğru yakalamış olmayı dilediğinize ve onu tutmanın neye mal olacağına çalışın. Hangi sinyallerin varsayılan olarak açık, hangilerinin örneklenmiş ya da isteğe bağlı olduğuna bilinçli karar verin ve bu kararı bir kaza değil politika olması için kaydedin. Kurumsal ya da kamu sistemi için o gözlemlenebilirlik bütçesinden kimin sorumlu olduğunu ve yakalanan izin denetim, gizlilik ve veri ikameti yükümlülüklerini de karşılayıp karşılamadığını ekleyin.

6. **Hata ayıklamayı öğretilen, ölçülebilir bir beceri olarak mı ele alıyoruz, yoksa yeni mühendisler onu sızma yoluyla mı özümsüyor?** Hata ayıklama öğrenilebilir, yine de çoğu takım onu açıkça hiç öğretmez; bu yüzden kıdemsizler kendilerine en yakın olan folkloru miras alır ve önce yeniden üretme yöntemi eşitsiz yayılır ya da hiç yayılmaz. Gerilim, bilinçli öğretimin (zor hatalar üzerinde eşli çalışma, olay sonrası bulguları yazmak, metrikleri izlemek) başka yerlerde her zaman gerekli hissedilen kıdemli zamanına mal olmasıdır. Tartışmaya iki sayı getirin: tekrarlanan kusur oranınızı ve teşhis etme sürenizi, çünkü onları ölçemiyorsanız yönteminizin iyileşip iyileşmediğini ya da çürüyüp çürümediğini söyleyemezsiniz. Uyumun gerçek bir hata ayıklama alıştırması içerip içermediğini ve kök neden bulgularının gerçekten daha erken algılamayı besleyip beslemediğini düşünün. Büyük ya da kamusal bir kuruluşta belgelenmiş, ölçülen bir hata ayıklama uygulaması aynı zamanda denetçilerin, düzenleyicilerin ve gözetim organlarının giderek görmeyi beklediği mühendislik titizliğinin kanıtı olur.

## Sektör merceği

**Girişim.** Bir avuç mühendis ve hiç boşluk olmadan, amacınız ağır süreç kurmak değil, hataları yeniden üretmesi ucuz ve unutması imkansız kılmaktır. `git bisect`'e, hızlı bir yerel yeniden üretime ve düzeltilen hata başına bir başarısız teste yaslanın, çünkü bu alışkanlık dakikalara mal olur ve yayımlamaya çalışırken aynı kusur için yeniden ödeme yapmanızı durdurur. Resmi ölü sonrası değerlendirmeleri atlayın, ama gerileme testini asla atlamayın: her zaman karşılayabileceğiniz kadar küçük ve her zaman tutmaya değer kadar değerli tek yapıttır.

**Küçük işletme.** Muhtemelen özel bir güvenilirlik ya da gözlemlenebilirlik uzmanınız ve sıkı bir araç bütçeniz vardır; bu yüzden yığınınızın zaten verdiğini tercih edin: okunabilir yığın izleri, yapılandırılmış günlükler ve satın aldığınız çerçevelere ve barındırılan hizmetlere yerleşik izleme. Yeni bir platformu değerlendirdiğinizde başarısızlıkları ne kadar teşhis edilebilir kıldığını tartın, çünkü neyin ters gittiğini gizleyen ucuz bir araç, lisansın tasarruf ettiğinden çok daha fazlasına tahmin zamanı olarak mal olur. Önce yeniden üret ve her seferinde tek değişiklik, kimsenin ayıracak saati olmadığında en hızlı karşılığını veren bedava disiplinlerdir.

**Kurumsal.** Zor hatalarınız hizmet ve takım sınırlarını geçer; bu yüzden belirtiyi gören kişi nadiren nedene sahiptir ve paylaşılan bir yöntem herhangi bir bireyin becerisinden daha önemlidir. Önce yeniden üretmeyi, ikili arama yalıtımını, düzeltmeden önce başarısız bir testi ve suçlamasız ölü sonrası değerlendirmeleri takımlar boyunca standartlaştırın ve tek bir isteğin hizmetler boyunca izlenebilmesi için dağıtık izlemeye (bölüm 9.2) yatırım yapın. Hata ayıklamayı ölçülen bir yetenek olarak yönetin: tekrarlanan kusur oranını ve teşhis etme süresini izleyin ve aynı başarısızlık sınıfının hizmet haritanızı turlamaması için kök neden bulgularını daha erken algılamaya geri besleyin.

**Kamu.** Tedarik kuralları, kısıtlı ortamlar ve kamusal hesap verebilirlik, hiç nasıl hata ayıklayabileceğinizi biçimlendirir. Çoğu zaman üretime bir hata ayıklayıcı bağlayamaz ya da vatandaş verisini bir dizüstü bilgisayara kopyalayamazsınız; bu yüzden izin verilenden teşhis için tasarlayın: yeniden üretilebilir derlemeler, yalıtılmış bir korunaklı alanda sentetik kayıtlar ve varsayılan olarak yakalanan yapılandırılmış günlükler ve izler. Her teşhis adımını ve her değişikliği denetim izine kaydedin ve satıcıların başarısızlıkları tedarikçinin sözüne bağımlı olmak yerine bağımsız araştırmanıza yetecek kadar telemetri ve derleme yeniden üretilebilirliği sunmasını isteyin.

## Örnekler

**Girişim.** Dört mühendislik bir takım, ödemenin kullanıcıların bir kesri için başarısız olduğunu görmeye devam eder ama testte hiç olmaz. Tahmin etmek yerine bir mühendis, başarısız isteğin tam yükünü yeniden oynatarak güvenilir bir yeniden üretim yakalar, sonra görmezden geldikleri yığın izini okur; o iz bir tarih ayrıştırma çağrısına işaret eder. Haftanın commit'leri boyunca hızlı bir `git bisect`, bir tarih kütüphanesini değiştiren değişikliği adlandırır. Suçlu zaman damgasıyla başarısız bir test yazarlar, ayrıştırıcıyı düzeltirler, testin yeşile döndüğünü izlerler ve onu takımda tutarlar. Tüm araştırma bir öğleden sonrayı alır çünkü kuramlaştırmadan önce yeniden ürettiler ve hata hiç dönmez.

**Kurumsal.** Bir ödeme platformu hiçbir tek takımın açıklayamadığı aralıklı zaman aşımları görür, çünkü belirti ödemede görünür ama neden üç hizmet ötede yaşar. Nöbetçi mühendisler başarısız tek bir isteği hizmet sınırları boyunca izlemek için dağıtık izlemeyi (bölüm 9.2) kullanır ve eşzamanlı yük altında ara sıra kilitlenen bir akış aşağısı çağrı bulur; sonucun iş parçacıkları arasındaki şanssız zamanlamaya bağlı olduğu klasik bir [yarış koşulu](https://en.wikipedia.org/wiki/Race_condition). Bunu bir yük testiyle yeniden üretir, başarısız bir entegrasyon testinde yakalar, kilitlemeyi düzeltir ve bir sonraki oluşumun günler değil dakikalar içinde yakalanması için bir izleme aralığı ve bir uyarı ekleyen suçlamasız bir ölü sonrası değerlendirme (bölüm 9.3) yürütür.

**Kamu.** Bir yardım kurumu vaka sistemini, mühendislerin üretime bir hata ayıklayıcı bağlayamadığı ve vatandaş verisini dizüstü bilgisayarlarına kopyalayamadığı hava boşluklu bir ortamda çalıştırır. Mutabakatta bir hesaplama kusuru ortaya çıkar. Takım ortamın izin verdiğinden hata ayıklar: yapılandırılmış günlükler, yalıtılmış bir test korunaklı alanında kurabilecekleri yeniden üretilebilir bir derleme ve başarısız vakayı yeniden yaratan sentetik kayıtlar. Her teşhis adımı denetim izine kaydedilir, düzeltme kanıt olarak başarısız ve sonra geçen bir testle gönderilir ve kök neden analizi yeni bir sürüm öncesi kontrolü besler. Yeniden üretim sentetik veri kullandığı için hiçbir vatandaş kaydı sınırdan çıkmadı.

## İş gerekçesi: motivasyonlar, YG ve TSM

Disiplinli hata ayıklamanın getirisi, tahmin ederek harcanmayan mühendis saatleri ve tekrarlamayan kusurlarla ölçülür. Teşhis edilmemiş aralıklı bir hata kıdemli zamanın günlerini ve tekrarlanan nöbet yükseltmelerini tüketebilir; önce yeniden üretme yöntemi bunu sınırlı, devredilebilir bir göreve çevirir ve başarısız test alışkanlığı aynı kusurun gelecek çeyrek yine size fatura etmesini durdurur. Büyük bir kuruluş boyunca aynı hata için asla yeniden ödememenin bileşik etkisi önemlidir ve liderliğin zaten izlediği değişim başarısızlık oranını ve ortalama kurtarma süresini doğrudan iyileştirir.

Toplam sahip olma maliyeti çoğunlukla eğitim ve araçlardır ve mütevazıdır. Paylaşılan kurallara (önce yeniden üret, her seferinde tek değişiklik, düzeltmeden önce başarısız bir test), araç zincirinde zaten yaygın olan hata ayıklayıcılara ve izlemeye ve bölüm 9.2'de anlatılan gözlemlenebilirlik yatırımına ihtiyacınız vardır. Daha büyük, gizli maliyet alternatiftir: mühendislerin saçma atışı değişiklikler uyguladığı, belirtilerin yamalanıp geri döndüğü ve nöbet yükünün sınırsız büyüdüğü bir batıl inanç kültürü. Yalnızca nöbet angaryasını azaltmak çoğu zaman yatırımı haklı çıkarır ve liderliğe gerekçe, alışkanlıklarda ve donatımda tek seferlik bir maliyete karşı daha az tekrarlanan olay ve daha hızlı kurtarma olarak en basit biçimde ifade edilir.

## Anti-kalıplar ve tuzaklar

- **Saçma atışı hata ayıklama:** birçok şeyi aynı anda değiştirmek; bu yüzden bir düzeltme bile nedene dair hiçbir şey öğretmez.
- **Yeniden üretmeden düzeltmek:** istek üzerine hiç tetikleyemediğiniz bir hatada zafer ilan etmek.
- **Hata çıktısını görmezden gelmek:** yığın izinin zaten dışladığı nedenler hakkında kuramlaştırmak.
- **Belirti yamalama:** kök neden dönmek üzere hayatta kalırken belirtiyi susturmak.
- **Print ifadesi yayılması:** kodda bırakılmış dağınık hata ayıklama çıktısı; hipoteze bağlı bir deney yerine gürültü ekler.
- **Gerileme testini atlamak:** hatayı düzeltip hiç koruma bırakmamak; bu yüzden sessizce geri gelebilir.
- **Kararsız testleri yeniden denemek:** altta yatan yarış koşulunu ya da [heisenbug'ı](https://en.wikipedia.org/wiki/Heisenbug), yani onu gözlemlemeye çalıştığınız anda değişen ya da kaybolan bir hatayı, hata ayıklamak yerine belirlenimsizliği yeniden denemelerle gizlemek.
- **Suçlamaya dayalı ölü sonrası değerlendirmeler:** yazarı cezalandırmak; hata ayıklamanın bağımlı olduğu bilgiyi yer altına iter.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Hata ayıklama bireysel folklor ve tepkidir. Mühendisler tahmin eder, saçma atışı değişiklikler uygular ve bir şeyleri yeniden başlatır. Hatalar belirtide düzeltilir, yeniden üretimler nadirdir ve aynı kusurlar tekrarlar. Üretim güçlükle teşhis edilebilir ve hiçbir deneme tekrarlanabilir olmadığı için kimse bir hatayı başkasına devredemez.
- **Düzey 2, Geliştirme:** Bazı mühendisler güvenilir biçimde yeniden üretir, yığın izlerini okur ve hata ayıklayıcılar kullanır, ama uygulama tutarsızdır ve kişiden kişiye ve takımdan takıma değişir. Günlük tutma vardır ama gürültülü ve yapılandırılmamıştır. Düzeltmeler bazen başarısız bir testle gönderilir, çoğu zaman gönderilmez ve kök neden analizi yalnızca biri ısrar ettiğinde gerçekleşir.
- **Düzey 3, Standartlaştırma:** Önce yeniden üret, ikili arama yalıtımı, her seferinde tek değişiklik ve düzeltmeden önce başarısız bir test, kuruluş genelinde uygulanan belgelenmiş takım normlarıdır. İkiye bölme ve delta hata ayıklama indirgemesi yaygın uygulamadır. Üretimde yapılandırılmış günlük ve izleme (bölüm 9.2) vardır ve suçlamasız ölü sonrası değerlendirmeler (bölüm 9.3) her kaçan kusur için standart yanıttır.
- **Düzey 4, Yönetme:** Hata ayıklama uygulaması temel çizgilere karşı ölçülür ve kontrol edilir. Tekrarlanan kusur oranı, teşhis etme süresi, yeniden açılan bilet sayısı ve bir gerileme testiyle gönderilen düzeltmelerin payı takım başına izlenir ve belirli bir tempoyla gözden geçirilir. Yeniden üretim ve kök neden tamamlanması iyi niyet değil kapı olarak ele alınır ve temel çizgiye karşı eğilimler araçlara, eğitime ve gözlemlenebilirliğe nereye yatırım yapacağınızı yönlendirir.
- **Düzey 5, Orkestrasyon:** Hata ayıklama, kalite (bölüm 2.11) ve olay yönetimiyle (bölüm 9.3) bütünleşen öğretilen bir beceridir ve tüm döngü sürekli uyum sağlar. Gözlemlenebilirlik, çoğu üretim hatası bir hata ayıklayıcı olmadan teşhis edilebilsin diye tasarlanır, çözülen her hata gerileme takımını güçlendirir ve kök neden bulguları kusur sınıfları yeniden teşhis edilmek yerine önlensin diye daha erken algılamayı besler. Kuruluş sistemleri ve başarısızlık biçimleri evrildikçe çabayı yeniden dengeler ve tekrarlanan kusur oranı düşmeye devam eder.

## Tartışma fikirleri

1. Yakın tarihli hatalarınızın kaçı biri kodu değiştirmeden önce güvenilir biçimde yeniden üretildi ve o kesir yönteminiz hakkında ne söylüyor?
2. Bir gerileme göründüğünde takımınız ikiye bölmeye mi uzanır, yoksa biri fark edene kadar kodu elle mi okur?
3. Üretim sisteminiz bugün ne kadar teşhis edilebilir ve zaten gerçekleşmiş bir başarısızlık hakkında neyi yakalamış olmak için ne verirdiniz?
4. Düzeltmeleriniz tutarlı biçimde başarısız ve sonra geçen bir testle gönderiliyor mu ve değilse, o disiplin nerede kırılıyor?
5. Kararsız testleri nasıl ele alıyorsunuz: belirlenimsizliği hata ayıklıyor musunuz, yoksa yeniden denemelerle üstünü mü örtüyorsunuz?
6. Hata ayıklama yeni mühendislere bilinçli öğretiliyor mu, yoksa folklor sızma yoluyla özümsemeleri için mi bırakılıyorlar?

## Önemli çıkarımlar

- Hata ayıklama hipotez testidir: güvenilir yeniden üretin, hatayı ve yığın izini okuyun, sonra taramak yerine ikili arama ve ikiye bölmeyle yalıtın.
- Başarısızlığı asgari yeniden üretilebilir örneğe indirin, büyük girdiler için delta hata ayıklama kullanın, çünkü kaldırılan her öğe dışlanmış bir nedendir.
- Aracı hataya uydurun: üretim ve dağıtık sistemler için donatım ve izleme (bölüm 9.2), yerel araştırma için etkileşimli hata ayıklayıcılar.
- Düzeltmeden önce hatayı yakalayan başarısız bir test yazın; böylece düzeltme kanıtlanır ve kusur kalıcı olarak korunur (bölüm 2.4).
- Kök nedeni bulup kaldırın, suçlamasız ölü sonrası değerlendirmeler (bölüm 9.3) yürütün ve hata ayıklamayı folklor değil öğrenilebilir bir beceri olarak ele alın.
- Her seferinde tek şey değiştirin; saçma atışı değişiklikler ve belirti yamaları kanıtı yok eder ve hatayı geri davet eder.

## Kaynaklar ve ileri okuma

- David J. Agans, *Debugging: The 9 Indispensable Rules for Finding Even the Most Elusive Software and Hardware Problems*
- Andreas Zeller, *Why Programs Fail: A Guide to Systematic Debugging*
- Andreas Zeller and Ralf Hildebrandt, "Simplifying and Isolating Failure-Inducing Input" (the delta debugging algorithm)
- Brian W. Kernighan and Rob Pike, *The Practice of Programming* (chapter on debugging)
- Andrew Hunt and David Thomas, *The Pragmatic Programmer* (the chapters on debugging and assertions)
- Steve McConnell, *Code Complete: A Practical Handbook of Software Construction* (the debugging chapter)
- John Regehr, "Reducers Are Fuzzers" and related writing on test-case reduction
- Charity Majors, Liz Fong-Jones, and George Miranda, *Observability Engineering* (debugging production with high-cardinality telemetry and tracing)
- Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy, eds., *Site Reliability Engineering* (blameless postmortems and production debugging)
