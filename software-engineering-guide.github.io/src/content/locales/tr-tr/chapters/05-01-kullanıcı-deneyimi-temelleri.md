# 5.1 Kullanıcı deneyimi temelleri

## Genel bakış ve motivasyon

[Kullanıcı deneyimi](https://en.wikipedia.org/wiki/User_experience) (UX), insanları (hedeflerini, bağlamlarını, kısıtlarını) anlamak ve ardından yazılımı, en az sürtünmeyle başarılı olmalarına yardım edecek biçimde şekillendirmektir. En sona uygulanan bir süs değildir. İlk kod satırından önce başlayan ve sürümden çok sonrasına kadar süren bir çalışma biçimidir. Bu bölüm, büyük bir kurumun ürün kararlarını tahminlerle değil kanıtla almasını sağlayan araştırma, modelleme ve [tasarım düşüncesi](https://en.wikipedia.org/wiki/Design_thinking) uygulamalarını ele alır.

Büyük takımlar için UX, bir zanaat olduğu kadar bir eşgüdüm sorunudur. Onlarca ekip tek bir ortak ürüne yazılım sevk ettiğinde, uyuşmayan zihinsel modeller, tekrarlanan akışlar ve çelişen terminoloji yığılarak hiçbir tek takımın sahiplenmediği karmaşık bir bütün oluşturur. Ortak kişilikler (persona), üzerinde uzlaşılmış yolculuk haritaları ve belgelenmiş bir [bilgi mimarisinden](https://en.wikipedia.org/wiki/Information_architecture) oluşan ortak bir UX temeli, her takıma kullanıcının aynı haritasını verir; böylece ayrı kararları tutarlı bir deneyimde toplanır. Bu temel olmadan her takım yerel olarak iyileştirme yapar ve ürün bir bütün olarak anlamsızlaşır.

Kurumsal ve kamu alanı bahisleri yükseltir. Kurumsal yazılımın çoğu zaman vazgeçemeyen kullanıcıları vardır, bu yüzden kötü UX'in bedeli insanların ayrılmasıyla değil, eğitim, destek talepleri, hatalar ve kaybedilen verimlilikle ödenir. Kamu hizmetleri çoğu zaman kriz içindeki, eski cihazlı, dijital özgüveni düşük ya da başka sağlayıcısı olmayan insanlar dahil bütün topluma ulaşır. Burada UX kalitesi bir hakkaniyet ve toplumsal güven meselesidir: kötü tasarlanmış bir yardım başvurusu, birinin gıdasız ya da barınaksız kalmasına yol açabilir; hak sahibi olmadığı için değil, formu tamamlayamadığı için.

## Temel ilkeler

- Hızlı bağlantıda, tam dikkatle çalışan idealleştirilmiş bir kullanıcı için değil, gerçek koşullarda gerçek işler yapan gerçek insanlar için tasarlayın.
- Araştırma riski azaltır. Yanlış bir varsayımı keşfetmenin en ucuz zamanı, onun üzerine bir şey inşa etmeden öncesidir.
- Kullanıcılar ne yapacaklarını güvenilir biçimde söyleyemez; yalnızca beyan ettikleri tercihi değil, davranışı gözlemleyin.
- Sevk etmek istediğiniz özelliğe değil, kullanıcının halletmeye çalıştığı işe odaklanın.
- Tutarlılık bir özelliktir: ürün boyunca tutarlı bir zihinsel model bilişsel yükü azaltır.
- [Erişilebilirlik](https://en.wikipedia.org/wiki/Accessibility) ve kapsayıcılık, sonradan yapılan bir uyum taraması değil, baştan iyi UX'in parçasıdır.
- Nitel ve nicel yöntemler farklı soruları yanıtlar; ikisini de kullanın.
- Küçük ve sık araştırma, seyrek ve ağır çalışmalardan iyidir.

## Öneriler

### Sürekli, karma yöntemli araştırma kurun

Ara sıra yapılan büyük çalışmalar yerine hafif ama sürekli bir araştırma uygulaması hedefleyin. Görüşmeler güdüleri ve zihinsel modelleri ortaya çıkarır. [Kullanılabilirlik testi](https://en.wikipedia.org/wiki/Usability_testing), tasarımların nerede bozulduğunu gösterir; tur başına beş ila sekiz katılımcı, ciddi sorunların çoğunu yüzeye çıkarır. Anketler tutumları ölçekte ölçer ama "neden"i açıklayamaz. Analitik ve ölçümleme, bütün nüfusta insanların gerçekte ne yaptığını gösterir. Bir nitel yöntemi (neden) bir nicel yöntemle (kaç kişi) eşleştirin, böylece bulgular hem açıklanır hem de boyutlandırılır. Ve bir araştırma deposu tutun; böylece içgörüler tek bir ekibin slaytlarında kaybolmak yerine takımlar arasında aranabilir ve yeniden kullanılabilir kalır.

### Kullanıcıları kişilikler, yolculuk haritaları ve yapılacak işlerle modelleyin

Demografik karikatürler değil, hedefleri, bağlamları ve kısıtları yakalayan, kanıta dayalı az sayıda kişilik oluşturun. İhtiyaçları yapılacak işler (jobs-to-be-done) olarak çerçeveleyin: bir özellik değil, kullanıcının ulaşmaya çalıştığı asıl sonuç ("işimi kaybettiğimde, kirayı ödemeye devam edebilmek için hangi desteklere hak kazandığımı hızla anlamak istiyorum"). Bu, odağı özelliklerden sonuçlara taşır. Yolculuk haritaları, deneyimin tamamını kanallar boyunca ve zaman içinde çizer; hiçbir tek ekranın göstermediği boşlukları ve devir noktalarını ortaya çıkarır. Arka sahnesi yoğun hizmetlerde (çağrı merkezleri, vaka yöneticileri, sipariş karşılama), ön sahne deneyimini arkadaki sistemlere ve çalışanlara bağlamak için [hizmet planları](https://en.wikipedia.org/wiki/Service_blueprint) kullanın.

### Bilgi mimarisini bilinçli tasarlayın

Bilgi mimarisi (BM), içeriğin, özelliklerin ve gezinmenin nasıl yapılandırıldığı ve etiketlendiğidir. Bu yapıyı organizasyon şemanızdan değil, kullanıcıların zihinsel modellerinden türetmek için [kart sıralama](https://en.wikipedia.org/wiki/Card_sorting) ve ağaç testi kullanın. Büyük kurumlarda sık görülen bir hata, iç departman sınırlarını üst düzey gezinme olarak sunmaktır. Aynı kavramın her yerde aynı adı taşıması için denetimli bir sözlük oluşturun. [Etkileşim tasarımı](https://en.wikipedia.org/wiki/Interaction_design) ise an be an davranışı tanımlar: durumlar, geri bildirim, hatadan kurtarma ve adımlar arasındaki akış.

### Tasarım düşüncesini pratik biçimde uygulayın

Çift elmas modeli (doğru sorunu tanımlamak için önce açıp sonra daraltmak, ardından doğru çözümü tasarlamak için yine açıp daraltmak) kullanışlı bir çerçevedir. Yine de onu katı, kapılı bir süreç olarak değil, bir zihniyet olarak ele alın. Pratikte sıkı döngüler işletin: bir hipotez kurun, çizin, bir avuç kullanıcıyla test edin ve günler içinde öğrenin. Daha ağır keşfi gerçekten yeni ya da yüksek riskli sorunlara saklayın. Ve atölyelerin yapışkan not ürettiği ama hiçbir değişikliğin sevk edilmediği "yenilik tiyatrosuna" dikkat edin.

### UX'i teslimata entegre edin

Tasarımcıları ve araştırmacıları, özellikleri duvarın üzerinden atan ayrı bir "UX departmanı" yerine teslimat takımlarının içine yerleştirin. Araştırma bulgularını önceliklendirmenin kalıcı bir girdisi yapın. Kullanılabilirlik ölçütleri ve erişilebilirlik denetimleri gibi UX kalite kapılarını bitti tanımına koyun. Ve sonuç ölçütlerini (görev başarısı, görev süresi, hata oranı, memnuniyet) teslimat ölçütlerinizin hemen yanında izleyin.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
|---|---|---|
| Sürekli keşif araştırması | Sorunları erken yakalar, ortak anlayış kurar | Süregelen maliyet, katılımcı bulma hattı ve yetkin kadro gerektirir |
| Ağır ön araştırma | Büyük yatırımdan önce derin içgörü | Yavaştır, ancak sevk ederek öğrenilebilen şeyleri geciktirebilir |
| Yalnızca analitiğe dayalı kararlar | Ölçeklenir, nesneldir, ölçümlendikten sonra ucuzdur | Ne olduğunu açıklar ama nedenini değil; kullanıcı olmayanlara ve uç durumlara kördür |
| Kişilikler ve yolculuk haritaları | Birçok takımı kullanıcının tek bir modeli etrafında hizalar | Eskir, veriyle tazelenmezse kurguya dönüşebilir |
| Gömülü tasarımcılar | Hızlı geri bildirim, ortak sahiplik | Zanaatı birçok takımda tutarlı tutmak daha zordur |

Her kurum araştırma yatırımını teslimat hızıyla dengeler. Hata, bunu ya bu ya şu olarak görmektir. Verimli duruş orantılı olandır: geri alması pahalı kararlara (çekirdek BM, birincil akışlar, platform seçimleri) daha fazla keşif, sonradan kolayca değiştirebileceğiniz ayrıntılara daha az keşif harcayın. Araştırmanın maliyeti, yanlış şeyi iyi inşa etmenin maliyeti yanında neredeyse her zaman küçüktür.

## Takımınızla tartışılacak sorular

1. **Ortak bilgi mimarisinin ve denetimli sözlüğün sahibi kim ve bir takım bunlardan sapmak istediğinde ne olur?** Ölçekte en sık görülen hata, her ekibin kendi organizasyon şeması yapısını ve aynı kavram için kendi adlarını sunmasına izin vermektir; ürün, tek bir şey için üç sözcüğe ve kullanıcı görevlerini değil departmanları yansıtan bir gezinmeye sahip olur. BM'nin ve sözlüğün merkezi olarak mı sahiplenileceğine, iç siyaset yerine kart sıralama ve ağaç testinden mi türetileceğine ve bir takımın değişikliği nasıl talep edeceğine şimdi karar verin. Bu, kurumsal ve kamu alanında daha önemlidir, çünkü vazgeçemeyen kullanıcılar bırakıp gidemez; tutarsızlığın bedeli kayıp müşteriyle değil, eğitim, destek talepleri ve hatalarla ödenir. Kanıt olarak yinelenen terimlerin ve çelişen akışların güncel listesini getirin. Bir sahip adlandıramıyorsanız, ilk eylem maddeniz budur.

2. **Araştırma katılımcıları için katılımcı bulma hattımız nedir ve yardımlı dijital, düşük özgüvenli ve dijital olmayan kullanıcılara ulaşıyor mu?** Sürekli keşif, her hafta gerçek kullanıcıların karşısına çıkabilirseniz işler ve bulunması en zor insanlar çoğu zaman hizmete en çok ihtiyaç duyanlardır: kriz içindeki, eski cihazlı ya da normalde yardıma güvenen insanlar. Yalnızca özgüvenli, bağlantılı gönüllüleri test etmek size gurur okşayan ama yanlış bir resim verir; erişim hakkaniyetinin bütün mesele olduğu kamu hizmetlerinde özellikle. Katılımcı bulmayı kimin yürüteceğine, hangi teşvikleri sunacağınıza ve hassas bir insanın yüküne yük eklemeden yardımlı dijital oturumları nasıl gözlemleyeceğinize karar verin. Son üç çalışmanızın katılımcı demografisini getirin ve gerçek kullanıcı tabanınızla karşılaştırın. Ulaşması kolay kullanıcılara kayıyorsa, bulgulara güvenmeden önce hattı düzeltin.

3. **Bitti tanımımıza hangi UX kalite kapıları girmeli ve bunların tiyatroya dönüşmesini nasıl önleriz?** Tasarımcıları ve araştırmacıları gömmek, ancak araştırma önceliklendirmenin kalıcı bir girdisiyse ve kullanılabilirlik ile erişilebilirlik denetimleri bir hikâyenin sevk edilmesini gerçekten engelliyorsa karşılığını verir; herkesin başını salladığı ve görmezden geldiği bir slayt destesi olmamalıdır. Teslimat ölçütlerinizin yanında izleyeceğiniz somut sonuç ölçütlerini seçin: görev başarısı, görev süresi, hata oranı ve memnuniyet. Risk, önceden verilmiş kararları haklı çıkarmak için yürütülen araştırmadır; bu yüzden bir lansmanı bir UX kapısında kimin veto edebileceğine ve hangi kanıtın bir yöneticinin görüşünü geçersiz kılacağına karar verin. Yakın tarihli bir özelliği getirin ve araştırmasının kararı değiştirip değiştirmediğini ya da yalnızca süsleyip süslemediğini sorun. Bulgular bir yol haritasını hiç oynatmıyorsa, kapılarınız kozmetiktir.

4. **Kişiliklerimizin, yolculuk haritalarımızın ve BM'mizin, onları üreten araştırma bir yıllık olunca kurguya dönüşmesini nasıl önleriz?** Ortak modeller, onlarca takımın tek bir tutarlı deneyime doğru tasarım yapmasını sağlayan şeydir, ama ancak hâlâ gerçek kullanıcıları tanımladıkları sürece işe yararlar; bir kişilik, kanıt özeti olmaktan çıkıp tartışma kazanmak için anılan bir nesneye dönüştüğü anda aktif zarar verir. Her modelin yenilenmesinden kimin sorumlu olduğuna, hangi sıklıkla ve hangi veriye karşı (yeni görüşmeler, analitik, destek temaları) yapılacağına karar verin ve eskiyen modellerin belli olması için görünür bir "son doğrulama" tarihi üzerinde uzlaşın. Rakip husus maliyettir: her şeyi sürekli yenilemek israftır, bu yüzden yenileme sıklığını kullanıcı tabanının ya da yolculuğun o bölümünün gerçekte ne kadar hızlı değiştiğine bağlayın. Güncel en önemli kişiliklerinizin kökenini getirin ve her birinin gerçek bir kullanıcıya karşı en son ne zaman kontrol edildiğini sorun. Vazgeçemeyen ya da kamusal bir kullanıcı tabanının yavaş ama sonuçları ağır biçimde değiştiği kurumsal ve kamu alanında (yaşlanan nüfus, yeni bir yardım, bir cihaz geçişi), sessizce eskiyen bir model, yılların yatırımını artık var olmayan kullanıcılara yöneltebilir.

5. **Erişilebilirlik sürecimizin neresinde yer alıyor ve bir sürümün bir şikâyetten sonra değil, sevk edilmeden önce bunu karşıladığını kanıtlayabilir miyiz?** Erişilebilirliği geç bir uyum taramasına bırakmak hem en yaygın hata hem de en pahalı olanıdır, çünkü anlamsal yapıyı, odak sırasını ve kontrastı inşa edilmiş bir arayüze sonradan eklemek, onları baştan tasarlamaktan çok daha pahalıdır. Hangi standardı kendinize şart koşacağınıza (örneğin WCAG, Web İçeriği Erişilebilirlik Yönergeleri), uyumun bitti tanımında engelleyici bir kapı olup olmayacağına ve erişilemez bir özellik üretime ulaştığında kimin sorumlu olduğuna karar verin. Gerilim, hız ile kapsayıcılık arasındadır ve teslim baskısı altındaki takımlar zorunlu kılınmayan denetimleri sessizce bırakır. Son denetiminizi, arkasındaki otomatik ve elle kapsamı ve sürümden önce değil sonra bulunan erişilebilirlik sorunlarının sayısını getirin. Özellikle kamu için bu nezaket meselesi değildir: çoğu zaman yasal bir görev ve hakkaniyet meselesidir, çünkü engelli ya da yardımlı dijital kullanıcıları dışlayan bir kamu hizmeti, ikincil bir amacında değil, temel amacında başarısız olmuştur.

6. **Analitiğimiz ve nitel araştırmamız çeliştiğinde hangisine inanacağımıza nasıl karar veririz ve hakemliği kim yapar?** Büyük kurumlar hem binlerce kullanıcının ne yaptığını gösteren panolar hem de bir avuç kişinin neden öyle davrandığını açıklayan görüşmeler biriktirir ve ikisi sık sık zıt yönleri gösterir: tamamlama oranı yüksek ama insanları sessizce aşağılayan bir akış ya da oturumlarda övülen ama ölçekte kimsenin dokunmadığı bir özellik. Nasıl çapraz doğrulama yapacağınıza, her yöntemin hangi soruyu yanıtlamak için güvenildiğine (büyüklük ve erişim için analitik, neden ve anlam için araştırma) ve ikisi çatıştığında kararı verme yetkisinin kimde olduğuna önceden karar verin. Risk, önceden seçilmiş planı okşayan kaynağı seçmektir. Yakın tarihli somut bir uyuşmazlığı getirin ve gerçekte nasıl çözüldüğünü gözden geçirin. Kurumsal ve kamusal ortamlarda bahisler daha da keskindir, çünkü analitik en önemli insanları sistematik olarak eksik sayar: kullanıcı olmayanlar, vazgeçenler ve yardımcı teknoloji kullananlar nadiren hunide görünür, bu yüzden yalnızca sayılara güvenmek dışlananları görünmez kılabilir.

## Sektör merceği

**Girişim.** Araştırmacınız ve bir depoya ayıracak vaktiniz yok; bu yüzden araştırmayı bir kurucu alışkanlığı yapın: bir sonraki şeyi inşa etmeden önce bir öğleden sonra beş gerçek kullanıcının yanında oturun. Resmi kişilikleri ve yolculuk haritalarını atlayın; çözdüğünüz tek iş hakkında, her hafta insanları izleyerek tazelenen ortak bir anlayış, kimsenin bakımını yapmadığı belgelerden iyidir. Avantajınız, bütün takımın bir içgörüyü ortaya çıktığı gün özümseyebilmesidir; bu hızı koruyun ve törenlere direnin.

**Küçük işletme.** UX uzmanınız ve dar bir bütçeniz yoksa, kendi kurallarınızı icat etmek yerine kullanıcılarınızın zaten bildiği geleneklere yaslanın ve akışları sıfırdan tasarlamak yerine makul varsayılanları olan araçlar satın alın. Ucuz ve yüksek değerli araştırmayı kendiniz yapın: bir görüntülü görüşme üzerinden bir avuç kullanılabilirlik oturumu ve destek taleplerinizi okumak, ciddi sorunların çoğunu ortaya çıkarır. Erişilebilirlik temellerini (kontrast, etiketler, klavye erişimi), kadro ayırdığınız bir proje olarak değil, iyi bir bileşen kütüphanesinden aldığınız asgari koşullar olarak görün.

**Kurumsal.** Temel sorun birçok takım arasında tutarlılıktır, bu yüzden ortak temellere yatırım yapın: sahipli kişilikler, bakımı yapılan yolculuk haritaları, denetimli bir sözlük ve ekiplerin etrafından dolaşmak yerine doğru tasarım yaptığı belgelenmiş bir bilgi mimarisi. Tasarımcıları ve araştırmacıları teslimat takımlarına gömün, ama ürünün tutarsız lehçelere bölünmemesi için zanaatı merkezi olarak yönetin. Bir araştırma deposunu ve bitti tanımındaki kalite kapılarını finanse edin ve UX sonuç ölçütlerini bir portföy olarak izleyin; böylece hiçbir tek takımın yerel iyileştirmesi bütünü bozmaz.

**Kamu.** Erişilebilirlik ve erişim hakkaniyeti tercih değil görevdir; bu yüzden sürümleri yayımlanmış bir standarda bağlayın ve yardımlı dijital, düşük özgüvenli ve dijital olmayan kullanıcılar dahil toplumun tüm yelpazesiyle araştırma yapın. Tedarik ve şeffaflık teslimatı şekillendirir: tasarım ilkelerinizi ve araştırma yöntemlerinizi yayımlayın, hizmetleri iç departmanlar yerine vatandaşların yaşam olayları etrafında yapılandırın ve denetim için test kanıtlarını saklayın. Kullanıcıların çoğu zaman başka sağlayıcısı olmadığı için, tamamlayamadıkları bir akış hizmeti reddetmek demektir; bu yüzden ulaşılması en zor kullanıcının tamamlamasını gerçek başarı ölçüsü olarak görün.

## Örnekler

**Girişim.** Küçük klinikler için bir randevu aracı geliştiren dört kişilik bir girişim, resepsiyonistlerin neye ihtiyaç duyduğu konusunda güçlü fikirlere sahipti ama kanıtı yoktu. Daha fazla özellik yazmadan önce kurucular, her biri bir öğleden sonra boyunca beş resepsiyonistin yanında oturup onların çalışmasını izledi. Gerçek acının rezervasyon hızı değil, kafa karıştırıcı bir takvim görünümünün yol açtığı çifte rezervasyonlar olduğunu öğrendiler; bu, önceki satış görüşmelerinde kimsenin söylemeyi aklına getirmediği bir şeydi. Ürünü o tek iş etrafında yeniden çerçevelemek ve düzeltmeleri bir hafta boyunca aynı beş kişiyle çizip test etmek, duraksayan bir denemeyi ilk ödeme yapan müşterilere dönüştürdü.

**Kurumsal.** Çok uluslu bir banka, yedi bölgesel iç kredi tahsis aracını tek bir platformda birleştirdi. Takım, özellik kümelerini birleştirmek yerine bölgelerdeki risk değerlendirmecileriyle yolculuk haritalaması ve hizmet planlaması yaptı. Herkesin varsaydığı "bölgesel farkların" çoğunun gerçek süreç farkları değil, tutarsız terminoloji ve ekran sırası olduğunu buldular. Birleşik bir BM ve ortak bir sözlük, değerlendirmecilerin eğitim süresini önemli ölçüde kısalttı ve işlem hatalarını azalttı, çünkü çalışanlar artık tek bir zihinsel modeli paylaşıyordu.

**Kamu.** Çevrimiçi beyan hizmetini yeniden tasarlayan bir ulusal vergi idaresi, yaş, cihaz ve dijital özgüven düzeyleri farklı mükelleflerle moderatörlü kullanılabilirlik testleri yaptı; ayrıca normalde yardıma güvenen insanların yardımlı dijital gözlemini yürüttü. Testler, jargonla dolu bölüm başlıklarının insanların vazgeçmesine ya da beyannameyi yanlış doldurmasına yol açtığını ortaya çıkardı. İçeriği mükelleflerin yapılacak işleri etrafında yeniden çerçevelemek ve BM'yi iç vergi kodları yerine yaşam olayları etrafında yeniden yapılandırmak, başarılı özhizmet tamamlamalarını artırdı ve çağrı merkezi hacmini azalttı; bu da erişim hakkaniyetini iyileştirirken hizmet maliyetini doğrudan düşürdü.

## İş gerekçesi: motivasyonlar, YG ve TSM

UX'in getirisi üç kaldıraçtan gelir: daha fazla başarı (daha fazla kullanıcı değerli görevleri tamamlar), daha düşük hizmet maliyeti (daha az destek talebi, daha az eğitim, daha az hata) ve daha az yeniden iş (yanlış yönleri inşa edilmeden yakalamak). Kullanıcıların vazgeçemediği kurumsal ortamlarda getiri, dönüşüm olarak değil, verimlilik ve daha az hata olarak görünür; binlerce çalışan boyunca işlem başına kazanılan birkaç saniye, yıllık büyük tasarruflara dönüşür.

Toplam sahip olma maliyeti (TSM), benimsemenin maliyetini benimsememenin maliyetiyle tartmak zorundadır. Benimseme maliyetleri kolay görülür: araştırmacılar ve tasarımcılar, katılımcı bulma ve teşvikler, araçlar ve takvimdeki zaman. Benimsememenin maliyeti daha büyük ama fark etmesi daha zordur: terk edilen işlemler, destek ve eğitim yükü, pahalı geç yeniden tasarımlar, başarısız lansmanlar ve kamu hizmetleri insanları dışladığında itibar ya da yasal risk. Bu maliyetler ürün hattına değil destek, eğitim ve operasyon bütçelerine yayıldığı için, liderlik onları çoğu zaman hafife alır.

Liderliğe gerekçeyi sunmak için UX'i yöneticilerin zaten izlediği ölçütlere bağlayın: tamamlama ve dönüşüm oranları, işlem başına maliyet, destek talebi hacmi, eğitim günleri ile hata ve yeniden iş oranları. Ölçülebilir bir öncesi-sonrası gösteren küçük, ölçümlenmiş bir pilot yürütün, ardından portföye genelleyin. Araştırmayı geri alınamaz kararlardaki risk azaltımı olarak çerçevelemek, finans ve yönetişim paydaşlarında karşılık bulma eğilimindedir.

## Anti-kalıplar ve tuzaklar

- **HiPPO güdümlü tasarım**: kanıt yerine en yüksek ücretli kişinin görüşüyle verilen kararlar.
- **Araştırma tiyatrosu**: önceden verilmiş kararları haklı çıkarmak için yürütülen, bulguları görmezden gelinen çalışmalar.
- **Kurgu olarak kişilikler**: gerçek kullanıcılara karşı hiç doğrulanmamış, tartışma kazanmak için kullanılan uydurma profiller.
- **BM olarak organizasyon şeması**: kullanıcı görevlerini değil, iç departmanları yansıtan gezinme.
- **Büyük patlama araştırması**: hiçbir şeyi değiştiremeyecek kadar geç gelen seyrek, pahalı çalışmalar.
- **Yalnızca mutlu yolu test etmek**: hata durumlarını, uç durumları ve stres altındaki kullanıcıları görmezden gelmek.
- **Son kat boya olarak tasarım**: UX'i yalnızca bitmiş bir yapıyı "güzel göstermek" için devreye sokmak.
- **Yardımlı ve dijital olmayan kullanıcıları yok saymak**: yalnızca özgüvenli, bağlantılı kullanıcılar için tasarlamak.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Özel bir UX uygulaması yoktur. Kararlar görüş ve en yüksek ücretli kişinin sezgisiyle alınır. Araştırma, olacaksa, plansız ve tepkiseldir; kötü giden bir lansmanla tetiklenir. Akışlar ve terminoloji takımlar arasında tutarsızdır ve genel deneyimin sahibi yoktur.

**Düzey 2, Geliştirme.** Bazı takımların tasarımcıları vardır ve ara sıra kullanılabilirlik testleri yapar; birkaç kişilik ya da yolculuk haritası mevcuttur, ama uygulama ekipler arasında çok değişir ve bakımı yapılmaz. UX sürekli bir disiplin olarak değil bir aşama olarak ele alınır ve takvim baskısı altında sık sık atlanır. İyi iş ceplerde olur ama ürün genelinde toplanmaz.

**Düzey 3, Standartlaştırma.** Sürekli karma yöntemli araştırma önceliklendirmeyi besler; ortak kişilikler, yolculuk haritaları ve denetimli sözlüklü bir BM belgelenmiş ve takımlar arasında kullanılır. Kullanılabilirlik ölçütleri ve erişilebilirlik denetimleri dahil UX kalite kapıları bitti tanımında yer alır ve kurum genelinde uygulanır. Aranabilir bir araştırma deposu, içgörüleri tek bir ekibin slaytlarında hapsolmak yerine yeniden kullanılabilir tutar.

**Düzey 4, Yönetme.** Uygulama yalnızca yerine getirilmekle kalmaz, başlangıç değerlerine karşı ölçülür. Görev başarısını, görev süresini, hata oranını, memnuniyeti ve erişilebilirlik uyumunu üzerinde uzlaşılmış ölçütler olarak izler, hedefler koyar ve sürümler boyunca izlersiniz. Araştırma katılımcı örneklemleri, bulguların temsili olması için gerçek kullanıcı tabanıyla karşılaştırılır, kalite kapıları görüş yerine geçme oranlarını raporlar ve araştırmanın maliyeti, destek taleplerinde, eğitimde ve yeniden işte ölçülen azalmalarla tartılır. Sevk etme ya da bekletme kararları, bu başlangıç değerlerine karşı kanıta dayanır.

**Düzey 5, Orkestrasyon.** Araştırma sürekli, sonuca bağlı ve kurum genelinde ürün, iş ve risk planlamasıyla bütünleşiktir. Takımlar kontrollü deneyler yürütür, içgörüden sevk edilen değişikliğe ve ölçülen etkiye kadar döngüyü kapatır ve nüfus ile yolculukları değiştikçe kullanıcı modellerini emekliye ayırır ya da yeniden kapsamlar. UX temeli sürekli uyum sağlar: kişilikler, yolculuklar, BM ve standartlar kanıta göre tazelenir ve kurum, geri alınabilirlik ile risk değiştikçe keşif yatırımını nereye yapacağını yeniden dengeler.

## Tartışma fikirleri

- Bir yöne bağlanmadan önce ne kadar keşif "yeterlidir" ve kim karar verir?
- Kişilikleri ve yolculuk haritalarını eskimiş eserlere dönüşmelerine izin vermek yerine nasıl canlı tutarsınız?
- Nicel analitik ve nitel araştırma çeliştiğinde hangisine ve neden güvenirsiniz?
- Büyük bir kurum, merkezi bir UX standardını her takımın özerkliğiyle nasıl dengelemelidir?
- Kriz içindeki insanların kullandığı hizmetleri, yüklerine yük eklemeden araştırmanın doğru yolu nedir?
- Bu yüzden hiç yapmadığınız bir hatayı önleyen araştırmanın YG'sini nasıl ölçersiniz?

## Önemli çıkarımlar

- UX, en sonda bir süs değil, baştan itibaren bir çalışma biçimidir.
- Nitel yöntemleri (neden) nicel yöntemlerle (kaç kişi) birleştirin.
- Kullanıcıları kanıta dayalı kişilikler, yolculuk haritaları, yapılacak işler ve hizmet planlarıyla modelleyin.
- Bilgiyi organizasyon şemasına değil, kullanıcıların zihinsel modellerine göre yapılandırın.
- Tasarım düşüncesini katı bir süreç değil, sıkı öğrenme döngüleri olan pratik bir zihniyet olarak ele alın.
- Araştırmanın maliyeti, yanlış şeyi inşa etmenin maliyeti yanında küçüktür.
- Kurumsal ve kamu alanında UX kalitesi doğrudan verimliliğe, hizmet maliyetine ve erişim hakkaniyetine dönüşür.

## Kaynaklar ve ileri okuma

- Don Norman, *The Design of Everyday Things*
- Steve Krug, *Don't Make Me Think*
- Erika Hall, *Just Enough Research*
- Kim Goodwin, *Designing for the Digital Age*
- Louis Rosenfeld, Peter Morville, and Jorge Arango, *Information Architecture: For the Web and Beyond*
- Clayton Christensen et al., *Competing Against Luck* (jobs-to-be-done)
- Alan Cooper, *The Inmates Are Running the Asylum*
- Jakob Nielsen, *Usability Engineering*
- UK Government Digital Service, *Service Manual* and *Design Principles*
- U.S. General Services Administration, *18F Methods* and the *U.S. Web Design System* research guidance
- Nielsen Norman Group, research method articles and reports
