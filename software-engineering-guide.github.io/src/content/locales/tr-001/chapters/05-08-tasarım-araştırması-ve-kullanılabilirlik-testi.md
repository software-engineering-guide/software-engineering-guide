# 5.8 Tasarım araştırması ve kullanılabilirlik testi

## Genel bakış ve motivasyon

[Kullanıcı araştırması](https://en.wikipedia.org/wiki/User_research), için ürün geliştirdiğiniz insanları tanıma disiplinidir: hedefleri, bağlamları, görevleri ve onları tökezleten engeller. Temel değeri risk azaltmaktır. Yazılımdaki en pahalı hata bir kusur ya da kaçırılmış bir son tarih değildir; yanlış şeyi iyi inşa etmek, sonra lansmandan sonra kimsenin buna ihtiyaç duymadığını ya da kimsenin kullanamadığını keşfetmektir. Araştırma, yanlış çıkacak bir yöne mühendislik emeği dökmeden önce bu riski ucuza düşürür. Bölüm 5.1 UX temellerini atar; bu bölüm o temelleri dürüst tutan iki motora derinlemesine iner: ne inşa edeceğinizi söyleyen üretken (generative) araştırma ve inşa ettiğinizin gerçekten işe yarayıp yaramadığını söyleyen değerlendirici (evaluative) araştırma.

Büyük takımlarda bahisler katlanır. Birçok ekip tek bir ürüne teslimat yaptığında, her biri her sprintte kullanıcılar hakkında bahis oynar ve ortak bir araştırma alışkanlığı olmadan bu bahisler, özgüven kılığına girmiş görüşlerden ibarettir. Küçük ama sürekli bir kanıt akışı herkese üzerinden tartışabileceği aynı gerçekliği verir; böylece tartışmalar en kıdemli ya da en yüksek sesli kişiyle değil, "gidip birkaç kullanıcıyı izleyelim" ile biter. Araştırma ayrıca yolculuk eder: iyi yürütülmüş tek bir çalışma, iyi kaydedilip paylaşılırsa bir düzine takımın varsayımını aynı anda düzeltebilir.

Kurumsal ve kamu alanı çıtayı bir kez daha yükseltir. Kurumsal yazılımın çoğu zaman bırakıp gidemeyen mecbur kullanıcıları vardır; bu yüzden kullanılamaz araçların bedeli, bir panoda görebileceğiniz kullanıcı kaybıyla değil, hatalar, eğitim ve kaybedilen saatlerle ödenir. Kamu hizmetleri bütün topluma ulaşır: kriz içindeki insanlara, eski telefonlara, düşük dijital özgüvene sahip kişilere ya da başka seçeneği olmayanlara. Birçok ulusal dijital hizmet standardı tam da bu nedenle kullanıcı araştırmasını zorunlu kılar, çünkü kimsenin dolduramadığı bir form insanları hak ettikleri yardımlardan eder. Burada araştırma bir incelik değildir. Kamuya verilen bir sözü tutmanın yoludur.

## Temel ilkeler

- Araştırma yanlış şeyi inşa etme riskini azaltır; inşa etmeden önce en ucuzdur, sonra değil.
- Üretken araştırma doğru sorunu bulur; değerlendirici araştırma çözümü sınar. İkisine de ihtiyacınız var.
- İnsanların yalnızca ne söylediğini değil, ne yaptığını izleyin; beyan edilen tercih ile gerçek davranış ayrışır.
- Nitel yöntemler nedenini açıklar; nicel yöntemler kaç kişi olduğunu ölçer. Eşleştirin.
- Küçük ve sürekli, nadir ve ağır olandan iyidir. Her hafta birkaç kullanıcı, yılda bir büyük çalışmadan daha çok öğretir.
- Bulgularınız katılımcılarınız kadar temsilidir; bu yüzden engelli ve ulaşılması zor kullanıcılar dahil, bilinçli işe alım yapın.
- Tek bir takımın slayt dosyasında yaşayan içgörü kaybolur. Araştırmayı tüm kurum yeniden kullanabilsin diye kaydedin.
- Yanlılık yönlendirici sorularla ve ümitli sentezle sızar; ona karşı bilerek tasarım yapın.

## Öneriler

### Üretken araştırmayı değerlendirici araştırmadan ayırın

Hangi soruyu sorduğunuzu açıkça belirleyin, çünkü yöntemler farklıdır. Üretken (ya da keşif) araştırması açık uçludur ve henüz bir çözümünüz yokken sorun uzayını keşfeder: İnsanlar gerçekte neyi başarmaya çalışıyor? Mevcut deneyim nerede acıtıyor? Neyi dolanıyorlar? Değerlendirici araştırma belirli bir tasarımı bir görev üzerinde sınar: İnsanlar bunu tamamlayabiliyor mu ve nerede tökezliyorlar? İkisini karıştırmak ikisini de boşa harcar. Sorunu hâlâ anlamıyorken sıkı bir senaryoya bağlı [kullanılabilirlik testi](https://en.wikipedia.org/wiki/Usability_testing) oturumu yürütmek, yanlış soruya cilalı cevaplar verir; bir ödeme akışını doğrulamanız gerekirken yapılandırılmamış bir sohbet sizi tahminle baş başa bırakır. Önce araştırma sorusunu adlandırın, sonra yöntemi seçin ve üretken bulguları yol haritasının gerçekten şekillendiği ürün keşfine (bölüm 10.14) besleyin.

### Yöntemi soruya uydurun

Her işe yarayan bir yöntem yoktur, yalnızca uyumlar vardır. Kullanıcı görüşmeleri motivasyonları, zihinsel modelleri ve geçmişi ortaya çıkarır ve keşif için iş atınızdır. İnsanların kendi ortamlarında gerçek iş yaparken gözlemlendiği [bağlamsal sorgulama](https://en.wikipedia.org/wiki/Contextual_inquiry), kimsenin toplantı odasında anmadığı dolanma yollarını ve kesintileri açığa çıkarır. Anketler geniş bir nüfus boyunca tutumları ve sıklıkları ölçer ama arkasındaki nedenleri açıklayamaz ve özensiz soru tasarımını acımasızca cezalandırır. [Kart sıralama](https://en.wikipedia.org/wiki/Card_sorting) ve ağaç testi bilgi mimarisini kullanıcıların zihinsel modellerinden türetir ve doğrular: kart sıralama insanlardan kavramları gruplamalarını ve etiketlemelerini ister, ağaç testi ise önerilen bir yapıda bir şeyleri bulup bulamayacaklarını denetler. Günlük çalışmaları, işe alıştırma ya da alışkanlık oluşumu gibi günler ya da haftalar boyunca ilerleyen ve hiçbir tek oturumun göremeyeceği davranışı yakalar. Basit bir sezgisel kural: insanları anlamak için görüşme ve bağlamsal sorgulamayı, bilgiyi yapılandırmak için kart sıralama ve ağaç testini, zaman ve ölçek boyunca görmek için anket ve günlük çalışmalarını, bir tasarımı denetlemek için kullanılabilirlik testini kullanın.

### Kullanılabilirlik testlerini erken, sık ve küçük yapın

Kullanılabilirlik testi tek başına en yüksek kaldıraçlı değerlendirici yöntemdir ve kod var olmadan çok önce kâğıt eskizlerle başlayabilirsiniz. İyi bilinen sezgisel kural, tur başına yaklaşık beş kullanıcının ciddi, bariz kullanılabilirlik sorunlarının çoğunluğunu ortaya çıkardığıdır; bu yüzden sonda on beş kişilik tek büyük bir çalışma yerine, tasarım evrildikçe beşer kişilik üç tur yapmak daha iyidir. Yine de sezgisel kuralın sınırlarını bilin. Beş kullanıcı yalnızca büyük sorunları keşfeden tek bir türdeş grup için yeterlidir; başarı oranlarını ölçmez, ayrı kullanıcı kesimlerini kapsamaz (anlamlı biçimde farklı her grubun kendi birkaç kişisi gerekir) ve nadir ama ağır sorunları yakalamaz. Akıl yürütmeyi derinleştirmek, anında uyum sağlamak ve karmaşık ya da hassas görevleri ele almak istediğinizde yönetilen (moderated) testi; hız, hacim, coğrafi erişim ve basit akışlar için daha düşük maliyet istediğinizde yönetilmeyen (unmoderated) testi seçin. Olgun takımların çoğu ikisini de yapar: anlamak için yönetilen, ölçekte doğrulamak için yönetilmeyen.

### Tanığı yönlendirmeyen görevler ve sorular yazın

Çalışmanız protokolünüz kadar güvenilirdir ve onu bozmanın en hızlı yolu, umduğunuz cevabı sezdirmektir. Katılımcılara talimat değil, gerçekçi hedefler verin: "Profili Düzenle düğmesine tıklayın ve adresinizi değiştirin" yerine "yeni taşındınız ve adresinizi güncellemeniz gerekiyor" deyin. Gelecekteki niyetler yerine geçmiş davranışı sorun, çünkü "bunu kullanır mıydınız?" güvenilir biçimde kibar yalanlar, "bunu en son ne zaman yaptığınızı anlatın" ise gerçekler üretir. Kendi sonucunu varsayan sorulardan kaçının ve insanın zaten inandığını destekleyen kanıtı fark etme ve hatırlama eğilimi olan [doğrulama yanlılığına](https://en.wikipedia.org/wiki/Confirmation_bias) karşı uyanık olun. Tasarımı yazan araştırmacı katılımcıları sessizce başarıya doğru yönlendirmemeli ve izleyen takım, ne anlama geldiğini tartışmadan önce olanı kaydetmelidir. Görevlerin tasarımını ve iletişimini ürünün tasarımından ayırdığınızda (bölüm 5.4) daha temiz sinyal alırsınız.

### Gerçekten kullanıcılarınızı temsil eden katılımcılar bulun

Bulgular, işe alımınızın yanlılığını miras alır. Yalnızca kendinden emin, bağlantılı, teknolojiyle rahat gönüllülerle test ederseniz, neredeyse yardıma ihtiyaç duymayan insanlar için harika çalışan ama en çok ihtiyacı olanları yarı yolda bırakan bir şey çıkarırsınız. Kesimlerinizi tanımlayın, sonra onlara karşı bilinçli işe alım yapın: yardımcı teknolojiye dayanan engelli kullanıcılar (bölüm 5.3) ve kriz içindeki insanlar, düşük dijital özgüvene sahip kişiler, yaşlı kullanıcılar, yavaş bağlantıdaki ya da eski cihazlardaki kişiler gibi ulaşılması zor gruplar dahil. Bu katılımcılara ulaşmak daha çok çaba, çoğu zaman toplum kuruluşlarıyla ortaklık, uygun teşvikler ve esnek lojistik gerektirir; ama bunu atlamak kullanıcıları ortadan kaldırmaz, yalnızca keşfi çok daha pahalı ve çok daha zararlı olduğu üretime taşır. Teşvikleri oyuna getiren profesyonel test edicilere değil, kesimin gerçek üyelerine ulaşmak için dikkatle eleyin.

### Bulguları yalnızca raporlara değil, kararlara sentezleyin

Ham gözlemler içgörü değildir. Sentezin işi, bir yığın oturum notunu takımın harekete geçebileceği az sayıda karara dönüştürmektir. Yakınlık haritalama, bireysel gözlemleri temalar altında kümelemek ([yakınlık diyagramının](https://en.wikipedia.org/wiki/Affinity_diagram) arkasındaki uygulama), oturumlar arasında kalıpları görünür kılmanın standart hamlesidir. Görüşme ağırlıklı çalışmalarda hafif bir [tematik analiz](https://en.wikipedia.org/wiki/Thematic_analysis), hangi temaların gerçekten verilerle desteklendiği konusunda sizi dürüst tutar. Kalıcı kalıpları bölüm 5.1'deki paylaşılan modellere, kanıta dayalı personalara ve yolculuk haritalarına yükseltin; böylece içgörü buharlaşmak yerine birikir. İyi sentezin sınavı basittir: bir karar değişti mi? Güzel bir slayt dosyası üreten ve hiçbir yol haritası maddesini değiştirmeyen bir çalışma tiyatrodur. Her çalışmayı, her biri için önerilen bir eylemle birlikte kısa, sıralı bir bulgu listesiyle bitirin.

### Nitel araştırmayı analitik ve deneylerle üçgenleyin

Nitel araştırma ve nicel veri aynı sorunun farklı yarılarını cevaplar ve her biri diğerinin kör noktasını kapatır. Araştırma kullanıcıların neden öyle davrandığını açıklar ama yalnızca odadaki bir avuç insanı görür; analitik ve deney (bölüm 7.4) bütün nüfusu görür ama motivasyonu açıklayamaz ve hiç kullanıcı olmamış insanların sorunlarını yakalayamaz. Bunları bir döngü olarak kullanın: analitik bir terk noktası gösterir, araştırma onu açıklar, bir yeniden tasarım onu ele alır ve bir deney düzeltmenin sayıyı oynatıp oynatmadığını ölçer. Nitel ve nicel sinyaller uyuşmadığında çelişkiyi sıkıntı değil ipucu sayın, çünkü genellikle biri, farkında olmadığınız bir şeyi ölçüyordur. Hiçbir kaynak diğerinin patronu değildir; karar ikisini birlikte okumaktan çıkar.

### Araştırma ölçeklensin diye araştırma operasyonlarını kurun

Birkaç takımdan fazlası araştırma yapmaya başladığı anda darboğaz yöntem olmaktan çıkar ve lojistiğe dönüşür: işe alım, planlama, rıza, teşvikler, not depolama ve birisi yeniden yürütmeden önce geçen çeyreğin çalışmasını bulmak. Araştırma operasyonları (ResearchOps), bu mekanizmayı güvenilir kılma pratiğidir. Bulguların etiketlendiği, keşfedilebilir olduğu ve takımlar arasında yeniden kullanılabildiği aranabilir bir içgörü deposuna; rıza, gizlilik ve insanlarla ne sıklıkta iletişime geçildiğine saygı gösteren bir katılımcı yönetim sistemine; çalışmaların telaş değil istikrarlı bir alışkanlık olması için düzenli bir araştırma ritmine yatırım yapın. Araştırmayı demokratikleştirmek, yani araştırmacı olmayanların bazı çalışmaları yürütmesine izin vermek yapmaya değerdir ama yalnızca güvencelerle: şablonlar, eğitim ve gözden geçirme; böylece öğrenme hacmini kötü protokollerin ve yanlı sonuçların hacmini artırmadan ölçeklersiniz.

## Ödünleşimler: artılar ve eksiler

| Yöntem | En uygun olduğu yer | Artılar | Eksiler |
| --- | --- | --- | --- |
| Kullanıcı görüşmeleri | Keşif, motivasyonlar | Derin neden, esnek, başlamak ucuz | Küçük N, görüşmeci yanlılığına açık |
| Bağlamsal sorgulama | Gerçek dünya davranışı | Dolanma yollarını ve bağlamı açığa çıkarır | Zaman alıcı, planlaması zor |
| Anketler | Ölçekte tutumlar | Büyük N, ölçülebilir | Nedenini açıklayamaz, kötü yazması kolay |
| Kart sıralama ve ağaç testi | Bilgi mimarisi | Yapıyı zihinsel modellere dayandırır | Dar kapsam, dikkatli analiz gerektirir |
| Günlük çalışmaları | Zaman içindeki davranış | Boylamsal kalıpları yakalar | Yüksek bırakma, katılımcı emeği |
| Yönetilen kullanılabilirlik testi | Bir tasarımı anlamak | Derinleştirici, uyarlanabilir, zengin | Daha yavaş, daha maliyetli, planlama yoğun |
| Yönetilmeyen kullanılabilirlik testi | Ölçekte doğrulamak | Hızlı, ucuz, coğrafi olarak geniş | Takip yok, karmaşık görevlerde yüzeysel |

Temel gerilim derinlik ile ölçek arasındadır ve çözüm seçmek değil sıralamaktır. Anlamak ve hipotez üretmek için derin, nitel, küçük N'li yöntemleri, sonra bunları ölçmek ve doğrulamak için geniş, nicel yöntemleri kullanın. İkinci gerilim hız ile titizlik arasındadır: sürekli hafif araştırma takımı her hafta öğrenir tutar, ama onu değerli kılan aynı hız, işe alım ve protokolde köşe kesmeyi kolaylaştırır. Bunu titizliği geri döndürülebilirliğe uydurarak çözün. Geri almanın pahalı olduğu kararlara (çekirdek akışlar, bilgi mimarisi, platform bahisleri) gerçek yöntemsel özen harcayın ve bir sonraki sprintte değiştirebileceğiniz ayrıntılarda hızlı ve esnek davranın.

## Takımınızla tartışılacak sorular

1. **Bir ürün bahsi oynadığımızda, fikrimizi değiştirecek en küçük araştırma parçası nedir ve taahhüt etmeden önce onu yürütmeye razı mıyız?** Takımlar ilkesel olarak araştırmayı sever ve son tarih baskısı altında atlar; bu yüzden gerçek soru, kanıtın yol haritası üzerinde herhangi bir yetkisi olup olmadığıdır. Neyin çürüten kanıt sayılacağına önceden karar verin, çünkü sonuç ne olursa olsun görmezden geleceğiniz bir çalışma herkesin zamanını boşa harcar ve bir tür tiyatrodur. Bu en çok geri almanın pahalı olduğu kararlar için önemlidir; bir haftalık keşif, yanlış şeyi inşa etmenin aylarının yanında önemsizdir. Güncel bir kararı getirin ve rotanızı değiştirecek bulguyu yüksek sesle söyleyin. Hiçbir bulgu onu değiştiremiyorsa araştırma yapmıyorsunuz, güvence topluyorsunuz; dürüstçe taahhüt etmeli ya da kararı yeniden açmalısınız.

2. **Test ettiğimiz insanlar gerçekten ürünü kullananlara, özellikle en çok zorlananlara benziyor mu?** Kendinden emin, bağlantılı, müsait gönüllüleri işe almak rahattır ve bu rahatlık ürününüzün gerçekte ne kadar kullanılabilir olduğuna dair pohpohlayıcı ve yanlış bir okuma üretir. Yazılımın iyi çalışmasına en çok ihtiyaç duyan kullanıcıların, yani engelli kullanıcıların, kriz içindeki insanların, düşük dijital özgüvene sahip kişilerin işe alınması genellikle en zordur; bu yüzden onlar için mücadele etmezseniz örneklemden sessizce düşerler. Son üç çalışmanızın katılımcı demografisini çekin ve gerçek kullanıcı tabanınızın ya da kamu hizmeti yükümlülüklerinizin yanına koyun. Kolay ulaşılan kullanıcılara doğru çarpıksa güveniniz yersizdir; bir sonraki bulgu turuna güvenmeden önce işe alım hattını düzeltin, toplum kuruluşlarıyla ortaklık kurun ve teşvikleri ayarlayın.

3. **Araştırma bulgularımız nerede yaşıyor ve başka bir takım altı ay sonra onları bulup yeniden kullanabilir mi?** Büyük bir kurumda aynı soru tekrar tekrar araştırılır, çünkü kimse ilk takımın zaten ödediği cevabı bulamamıştır; bu, özen kılığına girmiş saf israftır. İçgörü deposunun sahibinin kim olduğuna, çalışmaların nasıl etiketlenip özetleneceğine ve bir bulguyu kaydetmenin insanların gerçekten yapacağı kadar hızlı olması için asgari uygulanabilir yazının ne olduğuna karar verin. Bulgular yeniden kullanılıp paylaşıldıkça rıza ve katılımcı gizliliğine ne olacağını düşünün, çünkü özensiz yeniden kullanım bir uyum ve güven sorunudur. Yakın tarihli bir kararı getirin ve arkasındaki kanıtı izlemeye çalışın. Çalışmayı birkaç dakikadan kısa sürede bulamıyorsanız, araştırmanız üretebildiğinizden hızlı buharlaşıyor demektir.

4. **"Yaklaşık beş kullanıcı" kuralına başvurduğumuzda, bu ürün gerçekte kaç ayrı kesime hizmet veriyor ve her birinden gerçek bir örneklemi test ediyor muyuz?** Beş kullanıcı sezgisel kuralı, bir ürünün anlamlı biçimde farklı birkaç kullanıcı grubu olduğunda tuzağa dönüşür, çünkü tek gruptan beş katılımcı diğerleri hakkında hiçbir şey söylemez; yine de sayı, sanki bir tur herkes için meseleyi çözmüş gibi alıntılanır. Ortak bir ürüne teslimat yapan büyük bir takım için kesimler hızla çoğalır: farklı roller, bölgeler, cihazlar, erişilebilirlik ihtiyaçları ve uzmanlık düzeyleri; anlamlı biçimde farklı her grubun kendi birkaç kişisi gerekir. Rakip baskı maliyet ve takvimdir, çünkü her turda her kesimi test etmek pahalıdır; bu yüzden hangi kesimlerin en çok risk taşıdığına karar verin, onları her turda kapsayın ve gerisini dönüşümlü yapın. Gerçek kesim haritanızı ve son turlardan kesim başına katılımcı sayılarını getirin ve hangi grupları hiç izlemediğiniz konusunda dürüst olun. Mecbur kullanıcıların ve kamu hizmeti yükümlülüklerinin ihmal edilen kesimin basitçe terk edip gidemeyeceği anlamına geldiği kurumsal ve kamu ortamlarında, test edilmemiş bir kesim sessizce başarısız olduğunuz bir nüfustur ve bu boşluk planda ortalamada kaybolmuş bir istatistik değil, açık bir kapsam olarak yer almalıdır.

5. **Burada bir çalışmayı kim yürütebilir ve eğitimsiz bir meraklının ölçekte kendinden emin saçmalık üretmesini ne engelliyor?** Araştırmayı demokratikleştirmek daha çok takımın daha hızlı öğrenmesini sağlar, ama şablonlar, eğitim ve gözden geçirme olmadan yanlı protokolleri, yönlendirici soruları ve ümitli sentezi de ölçekler; böylece öğrenme hacmi ve kötü sonuç hacmi birlikte yükselir. Gerilim üretim hızı ile güven arasındadır: her şeyi birkaç araştırmacıdan geçirirseniz darboğaz olurlar, kapıları güvencesiz açarsanız kurumu kimsenin harekete geçmemesi gereken bulgularla boğarsınız. Hangi çalışma türlerinin devredilmesinin güvenli olduğuna (hızlı bir yönetilmeyen görev testi gibi), hangilerinin eğitimli bir el gerektirdiğine (hassas konular, savunmasız katılımcılar ya da bilgi mimarisi bahisleri gibi) karar verin ve şablonları, gözden geçirme adımını ve son kendi kendine hizmet çalışmalarının kaçının incelemeden sağ çıkacağını görmek için dürüst bir denetimi getirin. Büyük bir işletme ya da kamu kurumu için satın alma ve gizlilik boyutunu ekleyin: paylaşılan araştırma araçları çoğu zaman satın alınır ve herkesin rıza takibi olmadan katılımcılarla iletişime geçmesine izin veren bir kendi kendine hizmet platformu bir uyum olayı olmaya adaydır; bu yüzden güvenceler yöntem kalitesi kadar yasal veri işleme ile de ilgilidir.

6. **Analitiğimiz ve görüşmelerimiz aynı özellik hakkında zıt hikâyeler anlattığında, bu takım hangisine inanacağına nasıl karar veriyor?** Nitel ve nicel sinyaller tek sorunun farklı yarılarını cevaplar ve aralarındaki çelişkiyi kıdemle çözülecek bir sıkıntı saymak elinizdeki en yararlı ipucunu çöpe atar, çünkü genellikle bir kaynak farkında olmadığınız bir şeyi ölçüyordur. Büyük bir kurum için risk kabileciliktir: yalnızca panolara güvenen bir veri takımı ve yalnızca oturumlara güvenen bir araştırma takımı, birlikte okumak yerine her biri diğerini küçümser. Gerçek, yakın tarihli bir anlaşmazlığı getirin; analitikten gelen terk noktasını araştırmadan gelen nedenlerin yanına koyun ve analitiğin nerede olduğunu gösterdiği, araştırmanın nedenini açıkladığı ve bir deneyin düzeltmenin sayıyı oynatıp oynatmadığını ölçtüğü döngüyü yürüyün. Tek bir metriğin finansmanı ya da kamusal bir taahhüdü sürükleyebildiği kurumsal ve kamu bağlamlarında, ikisi uyuşmadığında kimin hakemlik yapacağını ve hangi kanıtın tartışmayı kapatacağını önceden adlandırın; böylece karar, odadaki en yüksek sesli savunucuya sahip işleve değil, üçgenlenmiş bir okumaya dayansın.

## Sektör merceği

**Girişim.** Bir avuç insanla ve boşa harcayacak pist olmadan, araştırmayı bir aşama değil, satın alabileceğiniz en ucuz sigorta sayın. Bir kurucu fazla kod yazmadan önce kâğıt prototipler üzerinde beş yönetilen oturum yürütsün, görevleri talimat değil hedef olarak çerçevelesin ve izlediğiniz şey fikri hâlâ eskizlerken öldürsün ya da yönlendirsin. Depoyu ve paneli atlayın; asıl amaç yanlış şeyi inşa etmekten kaçınacak kadar hızlı öğrenmektir.

**Küçük işletme.** Muhtemelen özel bir araştırmacınız ve dar bir bütçeniz var; bu yüzden kadrolu bir araştırma işlevi yerine düşük maliyetli, yönetilmeyen test araçlarına ve hafif görüşmelere yaslanın. Kullanılabilirlik testi yazılımı satın alırken işe alımı ve rızayı sizin için hallenen araçları tercih edin, çünkü bu mekanizmayı kendiniz kurmak sizin ölçeğinizde nadiren değer. Bir müşteriyi kazandıran ya da kaybettiren birkaç akışı test edin ve tanığı yönlendirmeyen görevler yazmakta disiplinli olun, çünkü kötü bir protokol elinizdeki küçük bütçeyi boşa harcar.

**Kurumsal.** Paylaşılan ürünlere birçok ekip teslimat yaparken kısıt yönetişimdir: aranabilir bir içgörü deposu, rıza takibi olan yönetilen bir katılımcı paneli ve çalışmaların telaş değil alışkanlık olması için bir araştırma ritmi. Araştırmayı şablon, eğitim ve gözden geçirme güvenceleri içinde demokratikleştirin ki hacim kötü protokolleri ölçeklemeden büyüsün ve iki ekibin aynı soruyu cevaplamak için iki kez ödememesi adına bulguların etiketli ve denetlenebilir olduğundan emin olun. Katılımcı verisini düzenlenmiş sayın: saklama, rıza ve iletişim sıklığı politika gerektirir.

**Kamu.** Birçok ulusal dijital hizmet standardı kullanıcı araştırmasını zorunlu ve değerlendirmeye tabi kılar; bu yüzden onu bir hizmetin kanıtla geçmesi gereken bir kapı sayın. Satın alma kuralları araçlarınızı ve işe alım tedarikçilerinizi şekillendirir, şeffaflık kiminle test ettiğinizi ve ne bulduğunuzu belgelemek demektir ve kamusal hesap verebilirlik, en zor ulaşılan kullanıcıları, yardımlı dijital ve engelli katılımcılar dahil, işe almak demektir; çünkü onları dışarıda bırakan bir hizmet insanları haklarından eder. Bir değerlendiricinin, denetçinin ya da kamunun araştırmanın gerçek olduğunu görebilmesi için rıza ve yöntem kayıtlarını net tutun.

## Örnekler

**Girişim.** Serbest çalışanlar için gider yazılımı geliştiren altı kişilik bir girişim, öldürücü özelliğin otomatik fiş taraması olduğuna ikna olmuş ve kaba bir sürümünü inşa etmişti. Daha fazla yatırım yapmadan önce iki kurucu, görevleri talimat değil hedef olarak çerçeveleyerek ("az önce gider olarak girdiğiniz kahveyi kaydedin") kâğıt prototiplerle gerçek serbest çalışanlarla beş yönetilen kullanılabilirlik oturumu yürüttü. Beşten dördü taramayı tamamen görmezden gelip tutarları elle yazdı, çünkü gerçek kaygıları veri girişi hızı değil, bir giderin vergi denetiminden sağ çıkıp çıkmayacağıydı. Takım ürünü denetime hazır kategorizasyon ve net bir kâğıt izi etrafında yeniden yönlendirdi, yineledikçe iki küçük tur daha yürüttü ve tıkanan bir ücretsiz denemeyi ödeme yapan abonelere çevirdi; hepsi bir haftalık eskiz ve konuşmanın maliyetine.

**Kurumsal.** Küresel bir lojistik şirketi, siteler boyunca depo yazılımını standartlaştırıyordu ve düzinelerce ürün ekibini dürüst tutmak için kalıcı bir araştırma operasyonları işlevi kurdu. Etiketli bir içgörü deposu, periyodik oturumlar için rıza vermiş depo çalışanlarından oluşan yönetilen bir panel ve iki haftalık bir araştırma ritmi inşa ettiler. İki ekip birbirinden bağımsız olarak aynı tarama iş akışını yeniden tasarlamayı önerdiğinde, depoda yapılan bir arama, önceki çeyreğe ait bir bağlamsal sorgulamayı ortaya çıkardı: tarama hatalarının çoğunu ekran düzeni değil, eldivenler ve soğuk depo koşulları sürüklüyordu. Yeniden kullanılan bu tek bulgu her iki ekibi de daha büyük dokunma hedeflerine ve eldivene uygun etkileşimlere yönlendirdi, tekrarlanan keşfi önledi ve yayına alındığında hatalı taramaları ölçülebilir biçimde azalttı.

**Kamu.** Randevu alma hizmetini yeniden tasarlayan ulusal bir sağlık servisi, kullanıcı araştırmasını isteğe bağlı değil, dijital hizmet standardı gereği zorunlu saydı. Demografik olarak geniş bir örneklemle yönetilen kullanılabilirlik testinin yanında takım, normalde bir akrabaya ya da kütüphane görevlisine güvenen insanlarla yardımlı dijital oturumlar yürüttü ve ekran okuyucu ile anahtar erişimi kullanan engelli katılımcıları (bölüm 5.3) hayır kurumlarıyla ortaklıklar yoluyla işe aldı. Test, bölüm başlıklarındaki klinik jargonun yaşlı ve daha düşük özgüvenli kullanıcıların gerçek bir engele ulaşmadan önce vazgeçmesine yol açtığını ortaya çıkardı. İçeriği hastaların sade dildeki hedefleri etrafında yeniden yapılandırmak, sonra kazancı ölçekte yönetilmeyen bir çalışma ve canlı bir analitik karşılaştırmasıyla (bölüm 7.4) doğrulamak, başarılı kendi kendine hizmet randevularını artırdı ve çağrı merkezi yükünü azalttı; hem hizmet maliyetini hem de erişimde hakkaniyeti iyileştirdi.

## İş gerekçesi: motivasyonlar, YG ve TSM

Araştırmanın getirisi üç kaldıraçtan gelir. Birincisi, önlenen israf: yanlış bir yönü bir çeyrek mühendislikten sonra değil, bir haftalık keşif sırasında yakalamak, en büyük ve en az sayılan tasarruftur; tam da boşa giden inşa hiç gerçekleşmediği ve bu yüzden bir raporda hiç görünmediği için. İkincisi, daha yüksek başarı: daha çok kullanıcının değerli görevleri tamamlaması; bu, tüketici ürünlerinde dönüşüm, kullanıcıların mecbur olduğu kurumsal ortamlarda verimlilik ve daha az hata olarak görünür. Üçüncüsü, daha düşük hizmet maliyeti: kullanılabilir hizmetler daha az destek talebi, daha az eğitim ve düzeltilecek daha az sonraki hata üretir.

Toplam sahip olma maliyeti, araştırma yapmanın maliyetini onu atlamanın maliyetine karşı tartmalıdır. Yapmanın maliyetleri görünür ve mütevazıdır: araştırmacılar, işe alım ve teşvikler, araçlar, bir depo ve takvimde zaman. Atlamanın maliyetleri daha büyüktür ama başka bütçelere dağılmıştır: terk edilen işlemler, destek talepleri, eğitim günleri, pahalı geç yeniden tasarımlar, başarısız lansmanlar ve kamu sektöründe vatandaşların dışlanması ile bunu izleyen yasal ve itibar riski. Bu maliyetler ürün kaleminde değil destek, eğitim ve operasyonlarda saklandığı için liderlik bunları rutin olarak hafife alır; bir lansman başarısız olana kadar araştırmanın isteğe bağlı görünmesinin nedeni tam olarak budur.

Gerekçeyi kurmak için araştırmayı yöneticilerin zaten izlediği sayılara bağlayın: tamamlama ve dönüşüm oranları, işlem başına maliyet, destek hacmi, eğitim süresi ve hata ile yeniden iş oranları. Gerçek bir akışta küçük, ölçülmüş bir önce-sonra çalışması yürütün, hareketi gösterin ve portföye yayın. Araştırmayı, bir kullanılabilirlik raporunu hiç okumayabilecek ama ters gidebilecek bir bahsi anlayan finans ve yönetişim paydaşlarıyla yankılanan bir dil olan, geri döndürülemez kararlarda risk azaltma olarak çerçeveleyin.

## Anti-kalıplar ve tuzaklar

- **Araştırma tiyatrosu**: zaten verilmiş bir kararı haklı çıkarmak için yürütülen çalışmalar; uygunsuz olduklarında bulgular sessizce görmezden gelinir.
- **Tanığı yönlendirmek**: istenen cevabı sezdiren görevler ve sorular; hiçbir anlamı olmayan pohpohlayıcı veri üretir.
- **Doğrulama yanlılıklı sentez**: yalnızca plana uyan gözlemleri duymak ve gerisini atmak.
- **Beş kullanıcı yanılgısı**: "yaklaşık beş kullanıcı"yı evrensel bir yasa saymak; onun tek bir kesim varsaydığını ve başarı oranlarını değil yalnızca ciddi sorunları bulduğunu görmezden gelmek.
- **Kolaya kaçan işe alım**: kim ulaşılması kolaysa onu test etmek; böylece engelli ve ulaşılması zor kullanıcılar örneklemden kaybolur.
- **Beyan edilen tercihe güvenmek**: insanların gerçekte ne yaptığını izlemek yerine "evet, bunu kullanırdım" cümlesine inanmak.
- **İçgörü mezarlıkları**: tek bir takımın slaytlarında gömülü bulgular; böylece aynı soru tekrar tekrar araştırılır.
- **Güvencesiz demokratikleştirme**: herkesin şablon ya da gözden geçirme olmadan çalışma yürütmesine izin vermek; yanlı protokolleri ve sallantılı sonuçları ölçeklemek.
- **Nitel ve nicel kabileciliği**: favori bir veri kaynağı seçip diğerini üçgenlemek yerine küçümsemek.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Araştırma gelişigüzeldir ya da yoktur ve kararlar görüşe ve kıdeme dayanır. Kullanılabilirlik testi, yapılırsa, lansmandan önce elde kim varsa onunla yapılan reaktif bir tek seferliktir ve bulgular nadiren bir şeyi değiştirir.
- **Düzey 2, Geliştirme:** Bazı takımlar kullanılabilirlik testleri ve ara sıra görüşmeler yürütür, ama işe alım kolaya kaçar, protokoller gayriresmidir ve içgörüler dağınık slayt dosyalarında yaşar. Uygulama squad'dan squad'a çok değişir ve araştırma, takvim baskısı altında kesilen bir aşamadır.
- **Düzey 3, Standartlaştırma:** Üretken ve değerlendirici araştırma belgelenmiş ve takımlar arasında sürekli yürütülür; ortak bir süreçle önceliklendirmeyi besler. İşe alım engelli ve ulaşılması zor kullanıcılar dahil gerçek kesimleri hedefler, aranabilir bir içgörü deposu vardır, sentez sıralı kararlar üretir ve araştırma operasyonları ritmi, şablonları ve katılımcıları kurum genelinde yönetir.
- **Düzey 4, Yönetme:** Araştırma programı temel çizgilere karşı ölçülür. Takımlar kullanıcı kesimlerinin kapsamını, görev başarısı ve tamamlama oranlarını, içgörüden yayına alınan değişikliğe kadar geçen süreyi ve destek hacmi, eğitim süresi ile hata ve yeniden iş oranları üzerindeki sonraki etkiyi izler ve bir metrik kaydığında harekete geçiren eşikler belirler. Depo yeniden kullanımı ve çalışma kalitesi izlenir; böylece liderler araştırmanın ürettiği getiriyi varsaymak yerine görebilir.
- **Düzey 5, Orkestrasyon:** Araştırma, analitik ve deneylerle üçgenlenmiş sürekli bir döngüdür; içgörüden yayına alınan değişikliğe ve ölçülen etkiye kapanır ve kurum genelinde ürün stratejisi ve risk planlamasıyla bütünleşiktir. Demokratikleştirilmiş araştırma güvenceler içinde güvenle yürür, bulgular ürün ve kullanıcıları değiştikçe birikir ve uyum sağlar ve araştırma yalnızca ekranları değil, stratejiyi de gözle görülür biçimde şekillendirir.

## Tartışma fikirleri

1. Bir inşaya taahhüt etmeden önce ne kadar keşif "yeterli"dir ve yeterince öğrenildiğini söyleme yetkisi kimdedir?
2. Analitik ve görüşmeler aynı özellik hakkında zıt hikâyeler anlattığında, takım hangisine göre harekete geçeceğine nasıl karar vermelidir?
3. Araştırmayı sorumlu biçimde demokratikleştirmek ile eğitimsiz coşkunun ölçekte yanlı çalışmalar üretmesine izin vermek arasındaki çizgi nerededir?
4. Değeri, bu yüzden hiç yapmadığınız ve asla gösteremeyeceğiniz bir hata olan bir çalışmanın getirisini nasıl ölçersiniz?
5. Krizdeki ya da savunmasız koşullardaki insanlarla, yüklerine yük eklemeden araştırma yapmanın etik yolu nedir?
6. Kamu hizmeti standartlarındaki gibi zorunlu kullanıcı araştırması, bir lansmanı engelleyebilen bir kapı olmalı mı ve bunu kim uygular?

## Önemli çıkarımlar

- Araştırma yanlış şeyi inşa etme riskini azaltmak için vardır ve inşa etmeden önce en ucuzdur.
- Üretken araştırmayı (doğru sorunu bul) değerlendirici araştırmadan (çözümü sına) ayırın; yöntemi sorudan seçin.
- "Yaklaşık beş kullanıcı", tur başına tek bir kesimdeki ciddi sorunların çoğunu bulur, ama başarıyı ölçmez ve ayrı grupları kapsamaz.
- Görevleri gerçekçi hedefler olarak yazın, geçmiş davranışı sorun ve yönlendirici sorulara ve doğrulama yanlılığına karşı tasarım yapın.
- Engelli ve ulaşılması zor insanlar dahil, kullanıcılarınızı gerçekten temsil eden katılımcıları işe alın; yoksa bulgularınız sessizce yanlıştır.
- Slaytlara değil, sıralı kararlara sentezleyin; sınav, bir kararın gerçekten değişip değişmediğidir.
- Nitel araştırmayı analitik ve deneylerle üçgenleyin ve öğrenme birikebilsin diye bulguları paylaşılan bir depoda tutun.

## Kaynaklar ve ileri okuma

- Erika Hall, *Just Enough Research*
- Steve Krug, *Rocket Surgery Made Easy*
- Jakob Nielsen, *Usability Engineering*
- Mike Kuniavsky, *Observing the User Experience*
- Steve Portigal, *Interviewing Users*
- Tomer Sharon, *Validating Product Ideas: Through Lean User Research*
- Hugh Beyer and Karen Holtzblatt, *Contextual Design*
- Donna Spencer, *Card Sorting: Designing Usable Categories*
- Kathy Baxter, Catherine Courage, and Kelly Caine, *Understanding Your Users*
- Kate Towsey, *Research That Scales: The Research Operations Handbook*
- Nielsen Norman Group, articles on usability testing, sample size, and research methods
- UK Government Digital Service, *Service Manual*: user research guidance
