# 10.4 Büyük ve uzun ömürlü sistemleri sürdürmek

## Genel bakış ve motivasyon

Yazılım mühendisliği üzerine yazılanların çoğu yeni şeyler inşa etmekle ilgilidir. Ama dünyanın önemli yazılımlarının çoğu eski, büyük ve hâlâ çalışmaktadır: vergi sistemleri, yardım ödemeleri, hava trafik kontrolü, çekirdek bankacılık, endüstriyel kontrol ve gündelik hayatın altyapısı. Bu sistemler rutin olarak on, yirmi, hatta otuz yıl çalışır. Bu, onları inşa edenlerin görev süresinden çok daha uzundur ve çoğu zaman onları üreten şirketlerden ve dillerden de uzundur. Bu tür sistemleri sürdürmek, onları on yıllar boyunca ve personel kuşakları boyunca güvenilir, güvenli, anlaşılır ve değişime açık tutmak demektir. Alanın en zor ve en az gösterişli disiplinlerinden biridir ve büyük kurumların ve devletlerin en ağır yükü taşıdığı yerdir.

Bu neden büyük kurumlar için daha önemli? Yükümlülüğün sürekliliği yüzünden. Bir girişim yazılımını yeniden yazabilir ya da terk edebilir. Ulusal bir hükümet, yeniden düzenleme yaparken emekli maaşı ödemeyi bırakamaz. Kurumların ve ajansların sahip olduğu sistemlerin başarısızlığının sonuçları geçim kaynakları, güvenlik ya da kamu güveni ile ölçülür. Ve bunların birçoğuna aynı anda sahiptirler; onları da on yıllar boyunca gelip giden insanlar çalıştırır. Merkezî tehditler egzotik değildir. Sistemi anlayan insanların yavaş erozyonu ([otobüs faktörü](https://en.wikipedia.org/wiki/Bus_factor), bir sistem hakkındaki bilgi kaybolmadan önce kaç kişinin ayrılması gerektiğinin azlığı), belgelenmemiş bilginin birkaç kafada birikmesi, teknoloji yığınının [ömür sonuna](https://en.wikipedia.org/wiki/End-of-life_(product)) doğru çürümesi ve bir sistem dokunulamayacak kadar kritik ve güvenle değiştirilemeyecek kadar kötü anlaşıldığında çöken felçtir.

Bu bölüm vekillikle ilgilidir: bir sistemin yazarlarından zarafetle uzun yaşamasına yardım eden bilinçli, gösterişsiz iş. Sahiplik sürekliliğini ve otobüs faktörü azaltmayı, planlı [kullanımdan kaldırmayı](https://en.wikipedia.org/wiki/Deprecation) ve ömrünü doldurma, bilgi aktarımını, on yıllar süren sistemlerin kendine özgü zorluklarını ve yenilik yapmak ile vatandaşların ve müşterilerin bel bağladığı istikrarı korumak arasındaki sürekli denge işini kapsar.

## Temel ilkeler

- **Her kritik sistemin her zaman bir sahibi olmalı.** Sahiplik sürekli bir atamadır, kimin yazdığının anısı değil.
- **Tek bir kafada yaşayan bilgi bir varlık değil, risktir.** Anlayışı kişi ayrılmadan önce kurumsallaştırın.
- **Sıkıcı olmak bir özelliktir.** Uzun ömürlü kritik sistemlerde istikrar ve öngörülebilirlik çoğu zaman yeniliğin önüne geçer.
- **Sonu baştan planlayın.** Her sistem emekliye ayrılacak ya da değiştirilecek; o gün için tasarlayın ve belgeleyin.
- **Güvende kalmanın yolu değişimdir.** Dokunulamayacak kadar korkutucu bir sistem zaten başarısız oluyordur; değişme yeteneği bir hayatta kalma özelliğidir.
- **Süreklilik bireylerden uzun yaşar.** Takımları, belgelendirmeyi ve süreçleri, hiçbir tekil ayrılış kriz olmayacak şekilde tasarlayın.
- **Güven asıl üründür.** Vatandaşa ve müşteriye dönük sistemlerde, zaman içinde sürdürülen güvenilirlik ve adalet misyondur.

## Öneriler

### Vekilliği ve sahiplik sürekliliğini kurun

Önemli olan her sistem için açık, güncel sahiplik atayın. Sahipliği bireysel değil takım düzeyinde tutun; böylece sahiplik ayrılışlardan sağ çıkar. Her sistem için kimin sahip olduğunu, ne yaptığını, neye bağlı olduğunu ve ne kadar kritik olduğunu kaydeden bir [hizmet kataloğu](https://en.wikipedia.org/wiki/Service_catalog) tutun. Sahipliği düzenli olarak gözden geçirin ve hiçbir sistemin sahipsiz kalmasına izin vermeyin. Sahipsiz bir kritik sistem, olmayı bekleyen bir acil durumdur. Takımlar yeniden düzenlendiğinde sahipliği varsayımla değil, bir devir teslimle, bilinçli biçimde aktarın. En kritik uzun ömürlü sistemler için sahipliğin yalnızca işletimi değil, sistemi anlama ve değiştirme yeteneğini de içerdiğinden emin olun; böylece vekillik salt çocuk bakıcılığına dönüşmez.

### Otobüs faktörünü ve kilit kişi riskini azaltın

Bilginin yoğunlaşmasını etkin biçimde ölçün ve azaltın. Bir sistemi yalnızca bir kişi dağıtabiliyor, hata ayıklayabiliyor ya da değiştirebiliyorsa, bu herhangi bir donanım kadar gerçek bir [tek hata noktasıdır](https://en.wikipedia.org/wiki/Single_point_of_failure). Bunu eşli çalışma ve rotasyon, zorunlu kod incelemesi, paylaşılan nöbet ve hiçbir kritik görevin tam olarak tek yetkin kişisi olmayacağı yönünde bilinçli bir kuralla azaltın. Her temel işlevi en az iki (tercihen üç) kişinin yapabilmesi için çapraz eğitim verin. Kilit bir kişinin ayrılışını, sürekli hazırlandığınız öngörülebilir bir olay olarak görün, soğurduğunuz bir şok olarak değil. Belgeleme yardımcı olur. Ama gerçek uygulama yoluyla bir takıma yayılmış çalışma bilgisi, kimsenin uygulamadığı belgelerden çok daha dayanıklıdır.

### Bilgi aktarımını kurumsallaştırın

Aksi halde insanlarla birlikte gidecek bilgiyi yakalayın. Önce yeniden kurması zor olan bilgiye odaklanın: kararların neden verildiği, hangi alternatiflerin neden reddedildiği, keskin kenarların ve sistemin geri kalanının sessizce dayandığı kritik kısa yolların nerede olduğu ve sistemin stres altında nasıl davrandığı. Yalnızca seçimleri değil, seçimlerin arkasındaki gerekçeyi korumak için mimari karar kayıtlarını kullanın. [Çalışma kılavuzlarını](https://en.wikipedia.org/wiki/Runbook) ve operasyonel belgeleri sisteme yakın tutun ve doğru kalsınlar diye onları düzenli olarak uygulayın. Yeni vekilleri gerçek yetkinliğe ulaştıran işe alıştırma yolları kurun. Ayrılışları, gerçek devir teslim zamanıyla bilgi aktarımı olayları olarak ele alın. [Örtük bilginin](https://en.wikipedia.org/wiki/Tacit_knowledge), yani bir sisteme dair hissin, esas olarak ona sahip biriyle yan yana yaparak aktarıldığını unutmayın; bu yüzden mümkün olduğunda ayrılan ve gelen vekilleri çakıştırın.

### Kullanımdan kaldırmayı, sonlandırmayı ve ömür sonunu yönetin

Sonları bilinçli planlayın. Bir sistemi emekliye ayırmaya ya da değiştirmeye karar verdiğinizde sonlandırmayı kendi başına bir proje olarak ele alın: her tüketiciyi ve bağımlılığı belirleyin, bir geçiş yolu ve gerçekçi bir takvim sağlayın, net ve tekrar tekrar iletişim kurun ve tüketicileri geçiş boyunca destekleyin. Eskisini kapatmanın zor işini kimse yapmayacağı için eski ve yeni sistemi sonsuza dek paralel çalıştırma tuzağından kaçının. Devreden çıkarmayı tamamlamak için açık hesap verebilirlik atayın. Özellikle yasal saklama kuralları geçerli olduğunda, bir sistem çalışmayı bıraktıktan çok sonra bile veriyi, kayıtları ve emekli sistem hakkında soruları yanıtlama yeteneğini koruyun. Kötü yapılmış bir sonlandırma, bakımı yapılmayan ama hâlâ güvenilen zombi sistemler bırakır: tüm olasılıkların en kötüsü.

### Sistemleri on yıllar boyunca sürdürün

Yirmi ya da otuz yıl çalışması gereken sistemler için her şeyden uzun yaşamayı planlayın: özgün takımdan, tedarikçilerden, dil ekosisteminden ve donanımdan. Gelecekteki bakımcılara bir şans vermek için tescilli kara kutular yerine [açık standartları](https://en.wikipedia.org/wiki/Open_standard) ve belgelenmiş arayüzleri tercih edin. Parçalar, denenmeyecek kadar riskli, ya hep ya hiç bir [yeniden yazımla](https://en.wikipedia.org/wiki/Rewrite_(programming)) değil, tek tek değiştirilebilsin diye modülerleştirin. Sistemi sürekli bakımda tutun. Küçük adımlarla güncel tutulan bir sistem sürdürülebilir kalır. "Çalışıyor" diye dondurulan bir sistem, yığını destekten düştükçe sessizce bakımsız hale gelir. Onu işletecek becerileri de koruyun: gerçekten eski teknoloji için, son uzmanın hiç emekli olmayacağını ummak yerine, ardıllarınızı bilinçli olarak eğitin.

### Yenilik ile istikrar ve güven arasında denge kurun

Mülkünüzün, yeniliğin değer yarattığı kısımlarını, istikrarın değer olduğu kısımlardan ayırt edin. Vatandaşların ve müşterilerin her gün bel bağladığı çekirdek sistemler genellikle heyecan verici yeniden yazımlardan çok güvenilirliği, geriye dönük uyumluluğu ve dikkatli değişimi ödüllendirir. Yeniliğe kenarlarda (yeni kanallar, yeni özellikler, yeni arayüzler) yatırım yaparken dayanıklı çekirdeği kararlı ve iyi anlaşılmış tutun. Çekirdeği değiştirin, evet, ama kahramanca sıçramalarla değil, küçük, geri alınabilir, iyi sınanmış artışlarla. Hedef hem güvenilir hem de evrilebilen bir sistemdir: [çürüyecek](https://en.wikipedia.org/wiki/Software_rot) kadar dondurulmuş, güvenilmez olacak kadar çalkalanmış asla.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
|---|---|---|
| Eski sistemi tutmak ve bakımını yapmak | Kurumsal bilgiyi korur; düşük aksama; kanıtlanmış güvenilirlik | Yaşlanan yığın; kıt beceriler; bakımsız kalırsa artan risk |
| Toptan yeniden yazım | Taze yığın; birikmiş pisliği atar | Çok yüksek başarısızlık oranı; zor kazanılmış uç durum bilgisini kaybeder |
| Artımlı modernizasyon | Sürekli risk azaltma; çalışmaya devam eder | Yavaş; sürdürülen fonlama ve disiplin gerektirir |
| Belgeleme ağırlıklı aktarım | Açık, aranabilir kayıt | Bakımsız kalırsa çürür; örtük bilgiyi kaçırır |
| İnsan temelli aktarım (eşli çalışma/rotasyon) | Dayanıklı çalışma bilgisi; dirençli takımlar | Mevcut verimliliğe mal olur; bilinçli planlama gerektirir |
| Kritik çekirdeği dondurmak | Kısa vadede azami istikrar | Yığın bakımsızlığa yaşlanır; dokunulamayacak kadar korkutucu hale gelir |

Belirleyici ödünleşim istikrar ile evrim arasındadır ve saf çözümlerin ikisi de başarısız olur. Kritik bir sistemi korumak için dondurursanız, eninde sonunda bakımsız ve güvensiz hale gelmesini garantilersiniz. Modernleştirmek için toptan yeniden yazarsanız, toptan değiştirmelerin kötü şöhretli yüksek başarısızlık oranını davet eder ve kimsenin orada olduğunu hatırlamadığı on yıllarca kodlanmış uç durum bilgisini çöpe atarsınız. Dayanıklı yol sürekli, artımlı değişimdir: sistemi küçük adımlarla canlı ve hareketli tutun; böylece asla destekten düşmez ve asla korkutucu bir sıçramaya ihtiyaç duymaz. Bilgi aktarımı da benzer bir ödünleşimdir: belgelerin kolaylığı ile yaşanmış deneyimin dayanıklılığı arasında. Yanıt ikisidir: omurga olarak yaşanmış, takımın elinde tuttuğu bilgi ve başvuru olarak belgeler.

## Takımınızla tartışılacak sorular

1. **Kritik sistemlerinizden hangilerinin şu anda güncel, adı konmuş bir takım sahibi yok?** Sahiplik sürekli bir atamadır, kodu kimin yazdığının anısı değil ve sahipsiz bir kritik sistem, yalnızca bozulduğunda fark edilen, olmayı bekleyen bir acil durumdur. Hizmet kataloğunuzu dolaşın (ya da bir tane kurun) ve her sistemin kimin sahip olduğunu, neye bağlı olduğunu ve ne kadar kritik olduğunu kaydettiğini kontrol edin. Kanıt getirin: üç önemli sistem seçin ve hesap verebilir takımı ve sahipliğin en son ne zaman gözden geçirildiğini adlandırmayı deneyin. Bir sistem sahipsizse ya da bir yeniden düzenleme onu sessizce düşürdüyse sahipliği varsayımla değil, gerçek bir devir teslimle bilinçli biçimde atayın. Sahipliğin sistemi anlama ve değiştirme yeteneğini de içerdiğinden emin olun; böylece vekillik salt çocuk bakıcılığına dönüşmez.

2. **Bir sistemi değiştirdiğinizde eskisini gerçekten kapatmaktan kim sorumlu?** Ebedi paralel çalıştırma yaygın ve maliyetli bir başarısızlıktır: kapatmanın sahibi olmadığı için eski ve yeni sistemler süresiz yan yana çalışır; iki sistemin bakımını yaparsınız ve ikisinin de güvenliğini elde edemezsiniz. Her sonlandırmayı, devreden çıkarmayı tamamlamak için adı konmuş hesap verebilirlik, haritalanmış bir tüketici listesi, bir geçiş yolu ve gerçekçi bir takvimle yönetilen bir proje olarak ele alın. Kanıt getirin: mülkünüzde bugün bakım çeken kaç "geçici" paralel çalıştırma ya da yarı emekli sistem var? Sistem çalışmayı bıraktıktan çok sonra bile yasal saklama kurallarını karşılamak için veriyi ve kayıtları koruyun, ama saklamanın hiç bitirmemek için bir bahane olmasına izin vermeyin. Kötü yapılmış bir sonlandırma, bakımı yapılmayan ama hâlâ güvenilen zombi sistemler bırakır; tüm olasılıkların en kötüsü.

3. **Uzun ömürlü sistemleriniz için hangi becerileri iş gücü piyasası sağlamayı bırakacak ve ardıl planınız nedir?** Yirmi ya da otuz yıl çalışan sistemler dil ekosistemlerinden, tedarikçilerinden ve eski yığını anlayan insanların kariyerlerinden uzun yaşar ve piyasa size güvenilir biçimde yedek vermez. Otobüs faktörünü bilinçli azaltın; böylece hiçbir kritik işlevin tam olarak tek yetkin kişisi olmaz ve her temel görevi en az iki, tercihen üç kişi yapabilsin diye çapraz eğitim verin. Kanıt getirin: yaşlanan her kritik sistem için, onu güvenle kaç kişinin değiştirebildiğini ve en bilgili olanların emekliliğe ne kadar yakın olduğunu sayın. Yanıt ardılların bilinçli eğitimini ve ayrılan ile gelen vekiller arasında gerçek bir çakışmayı yönlendirmeli, çünkü örtük bilgi (bir sisteme dair his) esas olarak ona sahip biriyle yan yana yaparak aktarılır. Belgeler başvurudur; yaşanmış, takımın elinde tuttuğu bilgi omurgadır.

4. **En kritik uzun ömürlü sisteminizi en son ne zaman değiştirdiniz ve hâlâ kimse bunu göze alabiliyor mu?** Bir yıldır kimsenin dokunmadığı bir sistem kararlı değil, "dokunulamayacak kadar korkutucu" tuzağına doğru sürükleniyordur; orada her değişiklikten korkulur ve bu yüzden yığın sessizce destekten düşer. Büyük bir kurum için bu önemlidir, çünkü felç birikir: dondurma ne kadar uzun sürerse bilgi o kadar solar ve eninde sonunda kaçınılmaz olan değişim o kadar riskli olur. Kanıt getirin: her kritik sistem için son bilinçli değişikliğin tarihini, bugün herkesin deneyeceği en küçük değişikliğin boyutunu ve rutin bir bağımlılık ya da güvenlik yamasının bu hafta kahramanlık gerektirmeden sevk edilip edilemeyeceğini. Karşı değerlendirme gerçektir, çünkü değişim de risk getirir; bu yüzden hedef çalkantı değil, küçük, geri alınabilir, iyi sınanmış adımların istikrarlı bir temposudur. Dondurulmuş bir çekirdeğin bir vatandaş hizmetinin altında on yıl durabildiği kurumsal ve kamu mülklerinde, "asla değiştirmiyoruz" sözünü bir güvence değil, bir kırmızı bayrak olarak görün ve değiştirme seçeneğini canlı tutan sürekli bakımı fonlayın.

5. **Mülkünüzün ne kadarı ömür sonunda ya da yakınında bir teknolojide çalışıyor ve o saati kim izliyor?** Yaşlanan çalışma zamanları, desteklenmeyen veritabanları ve bakımı bırakılmış çatılar, bir güvenlik yamasının gelmeyi bıraktığı gün ani bir krize dönüşen yavaş başarısızlık biçimidir. Büyük bir takım için tehlike, ufkun kimsenin sorumluluğunda olmamasıdır: tekil takımlar bozulanı yamalar ama hangi yığınların ne zaman tedarikçi desteğini yitireceğine dair portföy görünümünü kimse tutmaz. Kanıt getirin: her kritik sistemin çekirdek teknolojilerinin, yayımlanmış ömür sonu ya da destek sonu tarihlerinin ve çalıştırdığınız ile hâlâ desteklenen arasındaki mevcut boşluğun envanteri. Gerilim, sürekli yükseltmenin maliyeti ile ertelemenin riski arasındadır ve erteleme genellikle felaket biçimde kaybedene kadar kazanır. Tedarik ve akreditasyon döngülerinin bir yıl ya da daha uzun sürebildiği kurumsal ve kamu ortamlarında, uzak görünen bir ömür sonu tarihi çoğu zaman zaten hazırlık süreniz içindedir; bu yüzden ardıllık ve yükseltme işi saat dolmadan çok önce başlamalıdır.

6. **Mülkünüzün neresinde istikrar değer, yenilik ise yük ve bu sınırı nasıl dürüst tutuyorsunuz?** Her sistem aynı muameleyi ödüllendirmez: vatandaşların ve müşterilerin her gün bel bağladığı çekirdek sistemler genellikle güvenilirliği ve dikkatli değişimi ödüllendirirken kenarlar deneyi ödüllendirir ve ikisini karıştırmak para harcar ya da kesintileri davet eder. Büyük bir kurum için risk, hırs ve kariyer teşviklerinin heyecan verici yeniden yazımları tam da sıkıcı kalması gereken dayanıklı çekirdeğe itmesidir. Kanıt getirin: güvenilirliğin misyon olduğu ve yeniliğin değer yarattığı yerleri işaretleyen bir mülk haritası, artı o çizgiyi iki yönde de aşan yakın tarihli değişiklikler ve bunların maliyeti. Karşı değerlendirme, istikrarlı bir çekirdeğin bile evrilmesi gerektiğidir; bu yüzden "kararlı" bir dondurma bahanesi olamaz. Kurumsal ve kamu bağlamlarında, bu sınırı açık kritiklik kademelerine ve kamunun başarısızlığını göze alamayacağı bir sistemin riskli yeniden yazımını veto edebilecek adı konmuş bir yetkiye bağlayın; böylece muhakeme bu çeyrekte en yüksek sesi çıkaranla kaymaz.

## Sektör merceği

**Girişim.** Bir avuç mühendis ve az bir pistle sürdürme riskiniz, faturalama ya da kimlik doğrulama gibi kaybetmeyi göze alamayacağınız sistemleri yazan bir ya da iki kişide yoğunlaşır. Sürece neredeyse hiçbir şey harcamayın, ama ucuz, yüksek değerli şeyleri şimdi yapın: her kritik sistemden ikinci bir kişiyi eşli çalışmayla geçirin, şaşırtıcı kısımlar için tek sayfalık bir mimari karar kaydı yazın ve gerçekten kullandığınız bir çalışma kılavuzu tutun. Bir şeyi yalnızca eski diye yeniden yazma dürtüsüne direnin, çünkü sizin boyutunuzda çekirdek bir sistemin başarısız yeniden yazımı şirketi bitirebilir.

**Küçük işletme.** Özel bir bakım takımınız ve dar bir bütçeniz yok; bu yüzden kendiniz sürdürmeniz gerekecek bir şeyi inşa etmek yerine satın almayı ve barındırmayı tercih edin. Ayrılmanıza izin veren tedarikçileri ve açık standartları tercih edin ve hangi dış sistemin hangi kritik işlevi çalıştırdığının ve bozulduğunda kimi arayacağınızın sade bir kaydını tutun. Özel koda sahipseniz, tek bir ayrılış ya da süresi dolmuş bir destek sözleşmesi sizi mahsur bırakmasın diye onu en az iki kişinin (ya da güvenilir bir yüklenici artı bir çalışanın) anladığından emin olun.

**Kurumsal.** Zorluğunuz portföy ölçeğidir: birçok uzun ömürlü sistem, birçok takım ve on yıllar boyunca rotasyonla değişen personel. Takım düzeyinde sahipliği bir hizmet kataloğunda standartlaştırın, otobüs faktörünü mülk genelinde ölçün ve toptan yeniden yazımlara bahis yapmak yerine sürekli artımlı modernizasyonu fonlayın. Hiçbir kritik yığın sessizce destekten düşmesin diye ömür sonu ufuklarını merkezî olarak yönetin ve her sonlandırmayı devreden çıkarmayı tamamlamak için adı konmuş hesap verebilirlikle denetlenen bir proje olarak yürütün.

**Kamu.** Yükümlülüğün sürekliliği mutlaktır: yeniden düzenleme yaparken yardım ödemeyi ya da hava trafik kontrolünü bırakamazsınız ve başarısızlıklar kamusal ve ağır sonuçludur. Tedarik kuralları sizi açık standartlara, veri taşınabilirliğine ve belgelenmiş arayüzlere iter; böylece gelecekteki bakımcıların ve gelecekteki tedarikçilerin bir şansı olur. İş gücü piyasasının artık sağlamadığı eski teknolojiler için bilinçli ardıllık eğitimini fonlayın, yasal saklamayı karşılamak için emekli sistemlerin kayıtlarını koruyun ve vatandaş hizmetlerinin sürdürülen güvenilirliğini bir genel gider değil, hesap verebilir misyon olarak görün.

## Örnekler

**Girişim.** Beş kişilik bir girişimin zaten kaybetmeyi göze alamayacağı bir sistemi var: kurucularından birinin ilk ayda yazdığı ve şimdi her müşteri tahsilatını çalıştıran faturalama hizmeti. Onu yalnızca o kurucu anlıyor; bu yüzden takım otobüs faktörünü bir iltifat değil, gerçek bir risk olarak görüyor. İkinci bir mühendisi tam bir faturalama döngüsü boyunca eşli çalışmayla geçiriyor, tuhaf yeniden deneme mantığının neden var olduğunu açıklayan kısa bir mimari karar kaydı yazıyor ve bir olay sırasında gerçekten uyguladıkları bir çalışma kılavuzunu kodun yanında tutuyor. Onu yalnızca eski ve gösterişsiz diye yeniden yazmaya direniyor, bunun yerine küçük geri alınabilir adımlarla iyileştiriyorlar; böylece şirketi ayakta tutan hizmet birden fazla kafa tarafından anlaşılıyor.

**Kurumsal.** Büyük bir sigortacı, on yıllar önce yazılmış ve hâlâ işinin merkezinde olan bir poliçe yönetim sistemi çalıştırıyor. Riskli bir toptan yeniden yazım denemek yerine sistemi iyi tanımlanmış arayüzlerin arkasında modülerleştirdi ve şimdi her seferinde bir bileşeni değiştiriyor; her değişiklik küçük ve geri alınabilir. Her kritik işlevi yapabilen en az üç kişi var. Nöbet paylaşılıyor. Mimari karar kayıtları sistemin neden öyle çalıştığını yakalıyor. Özenle hazırlanmış bir iç kurs, yeni mühendisleri [eski](https://en.wikipedia.org/wiki/Legacy_system) yığında yetkinliğe getiriyor ve ayrılan uzmanlar ardıllarıyla çakışıyor; böylece örtük bilgi yaparak aktarılıyor.

**Kamu.** Ulusal bir sosyal güvenlik kurumu, otuz yıldan fazla çalışan ve duramayacak yardım ödeme sistemleri işletiyor. Açık takım sahipliğini bir hizmet kataloğuna kaydediyor. Sistemleri dondurmak yerine sürekli bakımı fonluyor. Ardılları eski teknolojilerde bilinçli olarak eğitiyor, çünkü iş gücü piyasası onları sağlamayacak. Eskimiş bir alt sistemi emekliye ayırdığında sonlandırmayı yönetilen bir proje olarak yürütüyor: her tüketiciyi haritalıyor, geçiş desteği sağlıyor, yasal saklama kurallarını karşılamak için kayıtları koruyor ve devreden çıkarmanın gerçekten tamamlanması için hesap verebilirlik atıyor; böylece hiçbir zombi sistem oyalanmıyor.

## İş gerekçesi: motivasyonlar, YG ve TSM

Uzun ömürlü sistemleri sürdürmenin getirisi, [toplam sahip olma maliyetlerine](https://en.wikipedia.org/wiki/Total_cost_of_ownership) hâkim olan iki felaket başarısızlık biçiminden kaçınmaktan gelir. Birincisi ani krizdir: kilit bir kişi ayrılır, desteklenmeyen bir bileşen ihlal edilir ya da sahipsiz bir sistem onu anlayan kimse olmadan başarısız olur. İkincisi başarısız mega projedir: bütçeyi aşan, eksik teslim eden ya da çöken aceleye getirilmiş toptan yeniden yazım. İkisi de olağanüstü pahalıdır ve ikisi de büyük ölçüde istikrarlı vekillikle önlenebilir. Önlenen tek bir yeniden yazım başarısızlığının ya da kritik bir vatandaş hizmetinin önlenen tek bir uzun kesintisinin maliyeti, genellikle yıllarca süren sürdürülen bakım yatırımını aşar.

Benimseme maliyeti süregelen ve gösterişsizdir: yeni özellik üretmeyen bakımı fonlamak, kısa vadeli çıktıyı azaltan çapraz eğitim ve belgeleme zamanı için ödeme yapmak ve asla manşetlere çıkmayan artımlı modernizasyona yatırım yapmak. Benimsememenin maliyeti ertelenmiş ve daha büyüktür: yığın yaşlandıkça artan risk, şişen kilit kişi maruziyeti ve eninde sonunda acil durum koşullarında zorunlu, yüksek riskli, yüksek maliyetli bir değiştirme. Liderliğe gerekçe sunarken bakımı "maliyet merkezi"nden "kurumun kaybetmeyi göze alamayacağı sistemler için risk yönetimi"ne yeniden çerçeveleyin. Toplam sahip olma maliyetini yalnızca inşayı değil, (sürdürme ve eninde sonunda devreden çıkarma dahil) bütün çok on yıllık ömür boyunca sunun. Ve şunu vurgulayın: vatandaşa ve müşteriye dönük sistemlerde sürdürülen güvenilirlik bir genel gider değildir. Gerçek ürün olan güvendir.

## Anti-kalıplar ve tuzaklar

- **Kahraman bakımcı.** Sistemi anlayan, yerine konamaz tek kişi; ayrılışı varoluşsal bir olaydır.
- **Dondur ve unut.** Kritik bir sistemi "bitti" ilan etmek, bakımı durdurmak ve yığınının bakımsızlığa yaşlanmasını izlemek.
- **Mahkûm yeniden yazım.** Kodlanmış bilgiyi çöpe atan ve genellikle bütçeyi aşan ya da başarısız olan toptan bir değiştirmeye kurumu bahis yapmak.
- **Sahipsiz sistemler.** Güncel sahibi olmayan, yalnızca bozulduğunda fark edilen kritik yazılım.
- **Belgeleme tiyatrosu.** Eskimiş, uygulanmamış ve kimsenin güvenmediği ciltlerce belge.
- **Ebedi paralel çalıştırma.** Kapatmaktan kimse sorumlu olmadığı için eski ve yeni sistemlerin süresiz yan yana çalışması.
- **Örtük bilgi kaybı.** Uzmanların çakışma olmadan ayrılmasına izin vermek; böylece sisteme dair his buharlaşır.
- **Dokunulamayacak kadar korkutucu.** Her değişiklikten korkulacak kadar kötü anlaşılan bir sistem; bu da çürümesini garantiler.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Sürdürme anlık ve tepkiseldir. Sistemler bireysel kahramanlara bağlıdır, sahiplik atanmak yerine hatırlanır ve bilgi belgelenmemiş biçimde birkaç kafada yaşar. Eski sistemler bozulana kadar dondurulur, yaşlanan yığınlar fark edilmeden ömür sonuna doğru sürüklenir ve emeklilikler duyurulur ama asla tamamlanmaz.

**Düzey 2, Geliştirme.** Temel uygulamalar ortaya çıkar ama takımdan takıma değişir. Sahiplik en bariz büyük sistemler için yazıya dökülmüştür, bazı çalışma kılavuzları ve belgeler vardır ve birkaç kritik işlevin ikinci bir yetkin kişisi vardır. Bakım fonlanır ama tepkiseldir, çapraz eğitim biri hatırladığında olur ve bunların hiçbirini kurum genelinde yapmanın ortak bir yolu yoktur.

**Düzey 3, Standartlaştırma.** Vekillik uygulamaları belgelenmiş ve kurum genelinde uygulanmıştır. Takım düzeyinde sahiplik bir hizmet kataloğunda kayıtlıdır ve yeniden düzenlemelerden sağ çıkar. Rotasyon ve çapraz eğitimle otobüs faktörü azaltma kalıcı bir kuraldır, mimari karar kayıtları ve uygulanan çalışma kılavuzları beklenir, modernizasyon politika gereği artımlıdır ve her sonlandırma, devreden çıkarmayı tamamlamak için adı konmuş hesap verebilirlikle yönetilen bir proje olarak yürütülür.

**Düzey 4, Yönetme.** Sürdürme, başlangıç değerlerine karşı veriyle ölçülür ve denetlenir. Kritik sistem başına otobüs faktörünü, her birini güvenle değiştirebilecek kişi sayısını, her çekirdek teknolojinin yaşını ömür sonu tarihine göre, mülkün sürekli ile ertelenmiş bakım altındaki payını ve takılıp kalmış paralel çalıştırma ve yarım kalmış devreden çıkarma sayısını izlersiniz. Bu ölçütlerin eylemi tetikleyen eşikleri vardır: otobüs faktörü tabanının altına düşen ya da destek sonu ufkunu aşan bir sistem fonlanmış iyileştirme alır ve vekillik sağlığı teslimatla birlikte liderliğe raporlanır.

**Düzey 5, Orkestrasyon.** Vekillik sürekli iyileştirilir ve kurum genelinde bütünleşiktir. Hiçbir kritik sistem tek bir insani hata noktası değildir, çakışma yoluyla örtük bilgi dahil bilgi aktarımı rutindir ve sistemler küçük geri alınabilir adımlarla evrilir; böylece hiçbiri destekten düşmez. Sahiplik, ömür sonu izleme, ardıllık ve sonlandırma planlaması portföy ve risk planlamasına örülmüştür, mülk teknolojiler ve yükümlülükler değiştikçe yeniden dengelenir ve çok on yıllık sistemler, onlara bel bağlayan insanların güveni korunarak sürdürülür.

## Tartışma fikirleri

- Otobüs faktörünü anlamlı biçimde nasıl ölçersiniz ve farklı kritiklik düzeyleri için doğru hedef nedir?
- Artımlı modernizasyon ne zaman gerçekten uygulanamaz olur ve yeniden yazım daha küçük risk haline gelir?
- Vekilliğin bir çıkmaz sokak değil, saygın bir kariyer yolu olması için bakım işini nasıl fonlayıp ödüllendirirsiniz?
- Son uzman emekli olmak üzereyken ve çakışma mümkün değilken örtük bilgiyi korumanın doğru yolu nedir?
- Emekli bir sistem hakkında soruları yanıtlama yeteneğini ne kadar süre korumalısınız ve bunun bedelini kim öder?
- Mülkünüzün neresinde istikrar değer, yenilik ise yük ve bu yargıyı zaman içinde nasıl dürüst tutarsınız?

## Önemli çıkarımlar

- En önemli yazılımların çoğu eski ve uzun ömürlüdür; onları on yıllar ve personel kuşakları boyunca sürdürmek birinci sınıf bir disiplindir.
- Her kritik sistemin güncel, takım düzeyinde sahipliğe ihtiyacı var; sahipsiz kritik sistemler örtük acil durumlardır.
- Otobüs faktörünü bilinçli azaltın (hiçbir kritik görevin tam olarak tek yetkin kişisi olmamalı) ve örtük bilgiyi yalnızca belgelerle değil, çakışma yoluyla aktarın.
- Uzun ömürlü sistemleri sürekli ve artımlı olarak bakımda tutun; onları dondurmak ve toptan yeniden yazımlara bahis yapmak iki başarısızlık biçimidir.
- Sonları, yükümlülükleri karşılamak için veri ve kayıtları koruyarak, hesap verebilir tamamlanmayla yönetilen projeler olarak planlayın.
- Vatandaşa ve müşteriye dönük sistemlerde sürdürülen güvenilirlik ve adalet misyondur ve bakım, kaybetmeyi göze alamayacağınız şeyler için risk yönetimidir.

## Kaynaklar ve ileri okuma

- Michael Feathers, *Working Effectively with Legacy Code*
- Titus Winters, Tom Manshreck, and Hyrum Wright, *Software Engineering at Google*
- Frederick P. Brooks Jr., *The Mythical Man-Month*
- Nat Pryce and Steve Freeman, *Growing Object-Oriented Software, Guided by Tests*
- Sam Newman, *Monolith to Microservices*
- Martin Fowler, *Refactoring* and writings on the Strangler Fig pattern
- Betsy Beyer et al., *Site Reliability Engineering* and *The Site Reliability Workbook* (Google)
- Diomidis Spinellis, *Code Reading: The Open Source Perspective*
- U.S. Government Accountability Office, reports on federal legacy IT modernisation
