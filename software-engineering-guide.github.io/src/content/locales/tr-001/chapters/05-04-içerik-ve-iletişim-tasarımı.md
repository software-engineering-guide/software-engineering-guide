# 5.4 İçerik ve iletişim tasarımı

## Genel bakış ve motivasyon

İçerik ve iletişim tasarımı, bir ürünün insanların harekete geçmesine yardım etmek için kullandığı sözcükleri, iletileri ve bilgiyi şekillendirme işidir. [İçerik stratejisini](https://en.wikipedia.org/wiki/Content_strategy) (hangi içeriğin kim için ve neden var olması gerektiği), UX yazarlığını ve mikro metni (bir arayüzün içindeki etiketler, düğmeler, ipuçları ve hata iletileri) ve kullanıcılara e-posta, bildirim ve diğer kanallar üzerinden ulaşan iletişimi kapsar. Sözcükler arayüzdür. Çoğu yazılımda ürün deneyimi, görsellerden çok içeriğin kendisidir.

Büyük takımlar için içerik bir eşgüdüm ve güven sorunudur. Birçok takım birbirinden bağımsız yazdığında terminoloji birbirinden uzaklaşır, ton ekrandan ekrana samimiden bürokratiğe savrulur ve aynı kavram üç farklı ad edinir. Kullanıcılar ipucunu kaybeder, güvenlerini de kaybeder. Ortak bir içerik stratejisi bunu çözer. Bir ses ve ton rehberi, denetimli bir söz varlığı ve hatalar ile boş durumlar için yeniden kullanılabilir kalıplar, sözcükler için tasarım sisteminin pikseller için yaptığını yapar: bağımsız takımların tutarlı ve güvenilir bir bütün üretmesini sağlar.

Kurumsal ve kamu ortamlarında açık içerik çoğu zaman bir üslup meselesi değil, yasal ve etik bir zorunluluktur. [Sade dil](https://en.wikipedia.org/wiki/Plain_language) yasaları, kamu iletişiminin harekete geçmesi gereken kişilerce anlaşılabilir olmasını şart koşar. Bir yardım formunda, bir tıbbi talimatta ya da bir güvenlik uyarısında kötü kurulmuş içerik gerçek zarara yol açabilir: kaçırılmış bir son tarih, yanlış bir doz, bir dolandırıcılık mağduru. Manipülatif ["karanlık kalıpların"](https://en.wikipedia.org/wiki/Dark_pattern) (insanları kendi çıkarlarına aykırı seçimlere kandıran ya da zorlayan arayüz tasarımları) çağında, bir ürünün seçenekleri nasıl sunduğu bir güven ve güvenlik meselesidir, giderek de bir mevzuat meselesi.

## Temel ilkeler

- Sözcükler arayüzdür; içerik, sonradan eklenen bir dolgu değil, deneyimin çekirdek parçasıdır.
- Okurun hedefi ve bağlamı için, sade dille, ihtiyaç duyduğu anda yazın.
- Zekâ yerine açıklık; şaşkın bir kullanıcı esprili bir hata iletisinden keyif almaz.
- Terminoloji ve ton tutarlılığı bilişsel yükü azaltır ve güven kurar.
- İyi varsayılanlar ve yardımcı boş durumlar insanları başarıya yönlendirir.
- Tasarımda dürüstlük: kullanıcıları asla seçimlere kandırmayın, zorlamayın ya da utandırmayın.
- İçerik yapılandırılmış ve yeniden kullanılabilir olmalı; koda gömülü ve çoğaltılmış olmamalı.
- İletişimi çok kanallı yolculuğun bütünü için tasarlayın ve dikkate saygı gösterin.

## Öneriler

### Bir içerik stratejisi ve ses oluşturun

İçeriğin kimin için olduğuna, onlara hangi işlerde yardım ettiğine ve nasıl duyulması gerektiğine karar vererek başlayın. Somut örnekli bir ses ve ton rehberi ve aynı şeyin her zaman aynı adla anılması için bir terminoloji sözlüğü ([denetimli söz varlığı](https://en.wikipedia.org/wiki/Controlled_vocabulary)) yazın. Tonun bağlamı izlemesine izin verin: hatada güven verici, güvenlik uyarısında sakin, başarıda kutlayıcı. Ses sabit kalır; ton esner. İçeriği, sahipleri, incelemesi ve yaşam döngüsü olan yönetilen bir varlık olarak ele alın; son dakikada bir alana yazılmış metin olarak değil.

### İnsanların harekete geçmesine yardım eden mikro metin yazın

Düğmeleri yaptıkları eylemle etiketleyin ("Başvuruyu gönder", "Tamam" değil). Hatalar ortaya çıkmadan önlemek için ipuçları ve yardımcı metinler yazın. Önemli sözcükleri öne alın; böylece ekrana göz gezdiren insanlar da asıl noktayı yakalar. İkinci kişiyi ve etken çatıyı kullanın. Cümleleri kısa ve belirli tutun. Her mikro metin parçası, ne olacağına ve sonra ne yapılacağına dair belirsizliği azaltmalıdır.

### Sade dili standart yapın ve yasal gereklilikleri karşılayın

Yazarların değil, tüm kitlenizin uyduğu bir [okuma düzeyinde](https://en.wikipedia.org/wiki/Readability) yazın. Yaygın sözcükleri, kısa cümleleri ve somut talimatları tercih edin; jargonu ve kısaltmaları ilk kullanımda açın ya da kullanmayın. Kamu sektöründe sade dil çoğu zaman yasayla ve politikayla zorunludur: geçerli sade dil standartlarını izleyin ve anlaşılırlığı gerçek kullanıcılarla, okuryazarlığı daha düşük olanlar ve ana dili farklı olanlar dahil, sınayın. Sade dil "basitleştirmek" değildir. Uzman okurlar da açık ve verimli metni tercih eder.

### Hata iletilerini, boş durumları ve varsayılanları bilinçli tasarlayın

Bir hata iletisi neyin ters gittiğini, nedenini ve nasıl düzeltileceğini sade dille, suçlamadan ve kullanıcının üzerinde harekete geçemeyeceği kodlar olmadan söylemelidir. Kullanıcının girdisini koruyun ve iletiyi sorunun tam olduğu yere koyun. Boş durumlar bir tanıtım fırsatıdır: boş bir uçurum göstermek yerine buraya neyin ait olduğunu ve nasıl ekleneceğini açıklayın. Çoğu kullanıcı hiçbir şeyi değiştirmeden başarılı olsun diye yardımcı, güvenli varsayılanlar seçin ve varsayılanı yalnızca işletmenin değil, kullanıcının çıkarına hizmet eden seçenek yapın.

### Güven ve güvenlik için tasarlayın; karanlık kalıplardan kaçının

Seçenekleri dürüstçe ve simetrik sunun: abonelikten çıkmak abone olmak kadar kolay, reddetmek kabul etmek kadar belirgin olmalıdır. Utandırarak onaylatma ("Hayır, teşekkürler, para biriktirmeyi sevmiyorum"), önceden işaretlenmiş rıza, gizli maliyetler, sahte aciliyet ve girmesi kolay çıkması zor "hamamböceği tuzağı" akışlarını kullanmayın. Etiğin ötesinde, bu kalıpların çoğu artık tüketici koruma ve gizlilik yasalarına göre yasadışıdır. Güvenlik, gizlilik ve para hakkındaki iletişimde özellikle özen gösterin, çünkü manipülasyon en çok zararı orada verir ve dolandırıcılar meşru iletileri orada taklit eder.

### Çok kanallı iletişimi tutarlı tasarlayın

E-posta, anlık bildirim, SMS ve uygulama içi iletiler tek bir yolculuğun parçalarıdır. Kullanıcılar kanallar arasında istenmeyen ileti yağmuruna tutulmasın ya da çelişkiyle karşılaşmasın diye bunları eşgüdümlü yönetin. Dikkate saygı gösterin: yalnızca zamanında ve yararlı olduğunda bildirin, kullanıcıların sıklığı ve kanalı denetlemesine izin verin ve her iletiyi erişilebilir ve sade yapın. İşlemsel iletişimin (makbuzlar, uyarılar, son tarihler) güvenilir, açık ve [kimlik avıyla](https://en.wikipedia.org/wiki/Phishing) karıştırılması zor olduğundan emin olun: tutarlı gönderen kimliği ve biçim, kullanıcıların gerçek iletilere güvenmesine yardım eder.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| Merkezi içerik stratejisi | Tutarlılık, güven, yeniden kullanım | Ek yük; darboğaza dönüşürse takımları yavaşlatabilir |
| Her yerde sade dil | Anlaşılırlık, kapsayıcılık, yasal uyum | Yeniden yazma emeği; uzmanlar jargonu kaybetmeye direnebilir |
| Eğlenceli, markalı ses | Kişilik, akılda kalıcılık | Hatalarda, yüksek riskli durumlarda ya da çeşitli kitlelerde ters tepebilir |
| Güçlü varsayılanlar | Çoğu kullanıcı zahmetsizce başarılı olur | Yönlendirme riski; kullanıcının çıkarına ayarlanmalı |
| Zengin çok kanallı iletişim | Zamanında, ilgi çekici | Kolayca gürültüye dönüşür; gizlilik ve rıza yükü |

Temel gerilim, marka kişiliği ile açıklık arasında ve etkileşim ile dikkate saygı arasındadır. Bağlam çözer. Riskin düşük olduğu yerde ses sıcaklık katsın; riskin yüksek olduğu yerde (hatalar, para, güvenlik, hukuk) sade ve sakin açıklığa öncelik verin. Varsayılanlarda ve iletişimde etik çizgi basittir: tasarım kullanıcının gerçek çıkarına mı hizmet ediyor, yoksa dikkatsizliğini mi sömürüyor?

## Takımınızla tartışılacak sorular

1. **Hata iletileri, boş durumlar ve varsayılanlar tasarım sistemimizde ortak kalıplar mı, yoksa her ekranda yeniden mi icat ediliyor?** Bunlar tüm deneyimin en yüksek kaldıraçlı anlarıdır: iyi bir hata neyin ters gittiğini, nedenini ve nasıl düzeltileceğini suçlamadan ve işe yaramaz bir kod olmadan söyler; iyi bir boş durum bir boşluk göstermek yerine insanlara oraya neyin ait olduğunu öğretir. Her takım bunları sıfırdan yazdığında bir yerde "Error 500", başka bir yerde yardımcı bir ileti görürsünüz ve kullanıcılar güvenini kaybeder. Bu kalıpların, bileşenlerin yanında, üzerinde anlaşılmış yapılar ve örnek metinlerle tasarım sisteminde yaşayıp yaşamayacağına karar verin. Ürününüzden üç gerçek hata iletisi ve üç boş durum getirin ve yüksek sesle okuyun. Herhangi biri kullanıcıyı suçluyorsa ya da kurtuluş yolu sunmuyorsa ilk iş kalemini bulmuşsunuz demektir.

2. **İçeriğimiz yapılandırılmış ve yeniden kullanılabilir mi, yoksa ekranlara gömülü ve çoğaltılmış mı?** Doğrudan bir bileşene yazılmış metin tutarlı biçimde güncellenemez, incelenemez ve kod değişikliği olmadan yerelleştirilemez; bu da gelecekteki her pazarı ve her ifade düzeltmesini sessizce engeller. Bu, ölçek büyüdüğünde keskinleşir: sözlük ve tek bir kaynak olmadığı için aynı kavram üç ad edinir. İçeriğin nasıl saklanacağına, denetimli söz varlığının sahibinin kim olacağına ve bir ifade değişikliğinin her ekran için ayrı dağıtım yapmadan nasıl yayılacağına karar verin. Ürününüzün tutarsız yazdığı ya da adlandırdığı bir terim örneği getirin ve kaç yeri düzenlemeniz gerekeceğini izleyin. Cevap "elle bul ve değiştir" ise içeriğiniz kodda sıkışmış demektir.

3. **İçerik tasarımcıları iş akışına ne zaman giriyor ve manipülatif bir akışı engelleme yetkisi kimde?** İçerik sonradan akla gelen bir şeyse (yayına kadar lorem ipsum, sonra kutuya sığan ne varsa) deneyimin büyük kısmını taşıyan sözcükler en az düşünceyi alır ve kimse dürüstlüğün sahibi olmadığı için büyüme baskısı altında karanlık kalıplar sızar. İçeriğin en baştan bir tasarım girdisi olduğunda, iş akışında bir ses ve ton rehberi ve inceleme bulunduğunda anlaşın ve utandırarak onaylatma ya da önceden işaretlenmiş rıza içeren bir akışı yayına çıkmadan durdurabilecek kişiyi adlandırın. Tüketici koruma ve gizlilik yasaları bu kalıpları giderek yasakladığı için bu artık etik olduğu kadar yasal bir sorudur. Yakın zamanda yayına çıkmış bir akış getirin ve reddetmenin kabul etmek kadar kolay ve belirgin olup olmadığını sorun. Değilse, düzeltmekten bugün kimin sorumlu olacağına karar verin.

4. **Aslında hangi okuma düzeyine göre yazıyoruz ve en yüksek riskli içeriğimizi gerçek kullanıcıların anladığını nasıl biliyoruz?** Sade dili iddia etmek kolay, kanıtlamak zordur: yazarlar kendi kavrayış düzeylerinde yazar ve açıklığa en çok ihtiyaç duyan okurlar, yani okuryazarlığı daha düşük olanlar ve ana dili farklı olanlar, odada en az temsil edilenlerdir. Büyük bir kurum için riskler katlanır, çünkü kafa karıştırıcı tek bir yardım mektubu ya da güvenlik uyarısı, kimse ulaşıp ulaşmadığını ölçmeden milyonlarca alıcıya kopyalanır. Tüm kitleniz için bir hedef okuma düzeyi belirleyin, jargonu ilk kullanımda açın ya da yasaklayın ve yalnızca bir okunabilirlik puanına güvenmek yerine gerçek insanlarla anlaşılırlık testi yapmayı taahhüt edin. En çok trafik alan üç iletişiminizi ve yazım takımı dışındaki birinin bunlar üzerinde doğru harekete geçebildiğinin kanıtını getirin. Kurumsal ve kamu ortamlarında geçerli sade dil yasasını ya da politikasını ekleyin ve bugün hangi belgelerin denetimden geçemeyeceği konusunda dürüst olun.

5. **E-posta, anlık bildirim, SMS ve uygulama içi kanallarda kullanıcılara nasıl, ne zaman ve ne sıklıkta ileti göndereceğimizi kim yönetiyor; böylece yolculuğun bütünü tutarlı kalıyor?** Her takım kendi kanalına sahip olduğunda kullanıcılar istenmeyen iletilere boğulur, çelişkiyle karşılaşır ve sonunda gerçekten önemli olan işlemsel iletiler dahil her şeyi görmezden gelmeye ya da abonelikten çıkmaya alışır. Yolculuğu eşgüdümlü yönetmek, sıklık sınırlarında anlaşmak, kullanıcılara kanal ve rıza üzerinde gerçek denetim vermek ve gerçek iletilerin onları taklit eden kimlik avıyla karıştırılmaması için tutarlı bir gönderen kimliği sürdürmek demektir. Tek bir kullanıcının yoğun bir haftada alabileceği her iletinin kaydını getirin ve yinelenenleri, çelişenleri ve dolandırıcılık sanılabilecek olanları sayın. Karşıt çekim, etkileşim baskısıdır: büyüme takımları her zaman bir temas noktası daha ister, dikkate saygının ise anlık bir ölçütü yoktur. Kurumsal ve kamu bağlamlarında, istenmeyen iletişimi yasal riske dönüştüren rıza ve gizlilik yükümlülüklerini ekleyin ve kanalı kötüye kullanan bir kampanyaya kimin veto edebileceğini adlandırın.

6. **İçeriğimizin işe yarayıp yaramadığını nasıl ölçüyoruz ve marka sesi nerede tamamen sade açıklığa yerini bırakıyor?** Hiç ölçülmeyen içerik zevke göre sürüklenir ve ifadeyi kullanıcı değil, en yüksek sesli paydaş belirler. İçeriği gerçek sinyallere bağlayın: destek talebi kategorileri, tamamlama ve dönüşüm hunileri, hata ve itiraz oranları, abonelikten çıkma ve şikâyet oranları; böylece bir yeniden yazım tercihle değil sonuçla değerlendirilir. Aynı zamanda sesin nerede yol vermesi gerektiği konusunda anlaşın: esprili bir hata, şakacı bir para iletisi ya da eğlenceli bir güvenlik uyarısı, riskin en yüksek olduğu anda güveni aşındırır. Yüksek trafikli bir akış, etkilediği ölçüt ve kişiliğin yardımcı olduğu yer ile sakin açıklığın zorunlu olduğu yer arasında önerilen bir çizgi getirin. Büyük ya da kamusal bir kurum için o çizginin sahibini ve kanıtlanmış bir iyileştirmenin takımlar arasında nasıl yayılacağını adlandırın; bir ekranı kazanıp gerisini kaybetmek yerine.

## Sektör merceği

**Girişim.** Yazar yokken ve iki mühendisle, içeriği işe alım değil kurucu görevi olarak ele alın. Bir günü en yüksek kaldıraçlı sözcüklere ayırın: düğmeleri eylemleriyle adlandırın, boş panoyu ilk çalıştırma eğitimine dönüştürün ve hataların neyin düzeltileceğini söylemesini sağlayın. Büyürken ton sade kalsın diye tek sayfalık bir ses rehberi yazın; tutarsızlık gerçekten acıtana kadar sözlüğü ve içerik platformunu atlayın.

**Küçük işletme.** İçerik tasarımcısı ve dar bir bütçeyle, zaten kullandığınız araçlara yerleşik sade dil ve mikro metin geleneklerine yaslanın ve işlemsel e-postaları sıfırdan hazırlamak yerine şablon satın alın. Müşteri kaybettiren birkaç ekrana öncelik verin: bir boş durum, bir ödeme hatası, bir iptal akışı. Reddetmeyi kabul etmek kadar kolay tutun ki karanlık kalıp yasalarından uzak kalın. Müşteriye dönük her şeyi yayından önce ücretsiz bir okunabilirlik denetleyicisinden geçirin.

**Kurumsal.** Sorun birçok takım arasındaki tutarlılıktır: ortak bir ses ve ton rehberi, bir kavramın tek adı olması için denetimli bir söz varlığı ve tasarım sisteminde bileşenlerin yanında yaşayan hata, boş durum ve varsayılan kalıpları. İçeriği sürüm denetiminde, koda gömülü değil yapılandırılmış ve yerelleştirilebilir olarak saklayın, ona sahipler ve inceleme verin ve kullanıcılar istenmeyen iletiye boğulmasın ya da çelişkiyle karşılaşmasın diye çok kanallı iletişimi eşgüdümleyin. Hiçbir takımın büyüme baskısı altında utandırarak onaylatma ya da önceden işaretlenmiş rıza yayına almaması için dürüstlüğü merkezden yönetin.

**Kamu.** Sade dil çoğu zaman bir tercih değil yasal bir görevdir; bu yüzden geçerli standartları izleyin ve anlaşılırlığı gerçek alıcılarla, okuryazarlığı daha düşük olanlar ve ana dili farklı olanlar dahil, sınayın. Her bildirimi eylem ve son tarihle açın, jargonu ayıklayın ve her iletişimin göndericisini açıkça belirtmesini sağlayın ki insanlar onu dolandırıcılıkla karıştırmasın. Seçenekleri dürüst ve simetrik tutun, kendinizi bağladığınız içerik standartlarını yayımlayın ve insanlara anlamadıkları bir kararı sorgulamaları için sade bir yol verin.

## Örnekler

**Girişim.** Yazarı olmayan küçük bir girişim, deneme kullanıcılarının çoğunun kaydolup boş bir pano gördüğünü ve bir daha dönmediğini fark etti. Bir kurucu bir günü mikro metni yeniden yazmaya ayırdı: boş durum artık neyin ekleneceğini açıklıyor ve tek tıkla örnek bir proje sunuyordu, düğmeler "Tamam" yerine eylemlerini adlandırıyordu ve hata iletileri neyin ters gittiğini ve nasıl düzeltileceğini söylüyordu. Etkinleşme ertesi hafta belirgin biçimde yükseldi ve aynı kurucu, tüm takım büyürken tonu sade ve tutarlı tutsun diye tek sayfalık bir ses rehberi yazdı.

**Kurumsal.** Bir SaaS şirketi, ilk katılım akışını, hata iletilerini ve boş durumlarını açık, eylem odaklı mikro metin ve belgelenmiş bir ses rehberi etrafında yeniden yazdı. "Nasıl yapılır..." sorularına gelen destek talepleri azaldı, boş durumlar artık kullanıcılara ne yapacaklarını öğrettiği için etkinleşme iyileşti ve denemeden ücretliye dönüşüm yükseldi. Şirket ayrıca güveni zedeleyen ve eleştiri çeken, utandırarak onaylatan bir iptal akışını kaldırdı ve yerine açık, simetrik bir iptal yolu koydu; bu da beklenmedik biçimde itibarı ve geri kazanımları iyileştirdi.

**Kamu.** Bir kurum, alıcıların düzenli olarak yanlış okuduğu, bu yüzden randevuların kaçırılmasına ve yardımların haksız yere kesilmesine yol açan bir yardım uygunluk mektubunu yeniden yazdı. Sade dil standartlarını uygulayan takım, mektubu gereken eylem ve son tarihle açtı, hukuki jargonu çıkardı ve anlaşılırlığı ana dili farklı olanlar dahil gerçek alıcılarla sınadı. Anlaşılırlık keskin biçimde arttı ve kaçırılan son tarih oranları düştü; bu da itirazları ve dosya işlerini azalttı. Mektup artık kendini ve göndericisini açıkça tanıttığı için alıcıların onu dolandırıcılıkla karıştırma olasılığı da azaldı.

## İş gerekçesi: motivasyonlar, YG ve TSM

İçerik kalitesi ölçülebilir sonuçlar doğurur: daha yüksek görev tamamlama ve dönüşüm, daha düşük destek hacmi, daha az hata ve itiraz, daha fazla güven ve elde tutma. Açık mikro metin ve yardımcı varsayılanlar, takılıp destek arayan ya da vazgeçen insan sayısını azaltır. Sade dilli iletişim aşağı akıştaki maliyeti düşürür: daha az kafası karışmış çağrı, düzeltilecek daha az hata, kamu bağlamlarında daha az itiraz. Güvenilir, manipülatif olmayan tasarım, karanlık kalıp mevzuatı sıkılaştıkça itibarı korur ve yasal riski azaltır.

TSM açısından benimseme maliyeti mütevazıdır: içerik tasarımcıları ya da eğitimli yazarlar, bir ses rehberi ve sözlük ve iş akışında inceleme. Benimsememenin maliyeti dağınık ve büyüktür: destek ve çağrı merkezi yükü, terk edilen işlemler, hata düzeltme, itirazlar, manipülatif kalıplar ya da uyumsuz iletişim için yasal cezalar ve aşınan güven. Bu maliyetler ürün bütçesine değil destek ve operasyonlara düştüğü için liderlik onları olduğundan az tartma eğilimindedir.

Gerekçeyi kurmak için içerik çalışmasını destek talebi kategorilerine, tamamlama ve dönüşüm hunilerine, hata ve itiraz oranlarına ve abonelikten çıkma ya da şikâyet oranlarına bağlayın. Yüksek trafikli bir akışın ya da yüksek hacimli bir iletişimin küçük bir yeniden yazımı genellikle açık, atfedilebilir bir iyileşme sağlar ve uygulamayı ölçeklemeyi haklı çıkaran da budur.

## Anti-kalıplar ve tuzaklar

- **Sonradan akla gelen içerik**: yayına kadar lorem ipsum, sonra kutuya sığan ne varsa.
- **Jargon ve iç dil**: kullanıcının değil, kurumun bakış açısından yazmak.
- **Suçlayan, işe yaramaz hatalar**: kurtuluş yolu olmayan "Error 500" ya da "Geçersiz girdi".
- **Boş durumlar**: rehberliğin olması gereken yerde bir boşluk.
- **Karanlık kalıplar**: utandırarak onaylatma, önceden işaretlenmiş rıza, gizli maliyetler, hamamböceği tuzakları, sahte aciliyet.
- **Tutarsız terminoloji**: ürün boyunca tek kavram için üç ad.
- **Bildirim yağmuru**: kullanıcıları görmezden gelmeye ya da abonelikten çıkmaya alıştıran aşırı iletişim.
- **Sınanmamış okunabilirlik**: içeriğin açık olduğunu gerçek kullanıcılarla sınamadan varsaymak.
- **Koda gömülü, çoğaltılmış metin**: tutarlı biçimde güncellenemez ya da yerelleştirilemez.

## Olgunluk modeli

**Düzey 1, Başlangıç.** İçerik pratiği yok. Sözcükleri ekranı yapan kişi, o anda kutunun ihtiyacına göre, geçici olarak yazıyor. Terminoloji ve ton tutarsız, hatalar kullanıcıyı suçluyor ya da üzerinde harekete geçilemeyen kodlar gösteriyor ve boş durumlar bomboş bir uçurum.

**Düzey 2, Geliştirme.** Bir üslup rehberi ya da bazı ses notları olabilir ve birkaç takım sade dil alışkanlıkları edinmiştir. İçerik hâlâ geç aşamada, takım başına yapılan bir faaliyettir; yeniden kullanım ve sınama azdır, bu yüzden kalite ve tutarlılık bir ekipten ötekine çok değişir.

**Düzey 3, Standartlaştırma.** Bir içerik stratejisi, ses ve ton rehberi ve denetimli söz varlığı belgelenmiş ve takımlar arasında kullanılıyor. Sade dil standarttır ve gerekli olduğunda uyumludur; hatalar, boş durumlar ve varsayılanlar ortak kalıpları izler; içerik ekran başına koda gömülmek yerine yapılandırılmış, incelenmiş ve yeniden kullanılabilirdir.

**Düzey 4, Yönetme.** İçerik sonuçlara karşı veriyle ölçülür. Okunabilirlik ve anlaşılırlık testi sonuçları, destek talebi kategorileri, tamamlama ve dönüşüm hunileri, hata ve itiraz oranları ile abonelikten çıkma ve şikâyet oranları taban değerlere karşı izlenir ve her içerik değişikliği bu sayıları oynatıp oynatmadığına göre değerlendirilir. Karanlık kalıplar belgelenmiş bir politikaya karşı denetlenir ve çok kanallı ileti sıklığı üzerinde anlaşılmış sınırlara karşı izlenir.

**Düzey 5, Orkestrasyon.** İçerik sürekli iyileştirilir ve kurum genelinde bütünleşiktir. Kalıplar tasarım sisteminde yaşar, varsayılan olarak yerelleştirilmiş ve erişilebilirdir; denetimli söz varlığı her yerde kavram başına tek ad tutar; çok kanallı iletişim eşgüdümlü ve kullanıcı denetimlidir; ve pratik mevzuat, kitle ve kanallar değiştikçe uyum sağlar, içeriği görüşe değil kanıta dayanarak emekliye ayırır ve yeniden yazar.

## Tartışma fikirleri

- Marka sesi nerede tamamen sade açıklığa yerini bırakmalı ve çizgiyi kim çiziyor?
- Büyüme takımları ölçütler konusunda baskı altındayken karanlık kalıp yasağı politikasını nasıl uygularsınız?
- Birçok takım arasında terminolojiyi onları darboğaza sokmadan nasıl tutarlı tutarsınız?
- Tüm halkın kullandığı bir hizmet için doğru okuma düzeyi nedir?
- Bildirim sıklığı ve kanal denetimi kurum genelinde nasıl yönetilmeli?
- Gerçek iletileri, onları taklit eden kimlik avından nasıl ayırt edilebilir yaparsınız?

## Önemli çıkarımlar

- İçerik çekirdek arayüzdür; sözcükleri görsellerle aynı titizlikle tasarlayın.
- Sade dil herkes için anlaşılırlığı artırır ve çoğu zaman yasal olarak zorunludur.
- Hatalar, boş durumlar ve varsayılanlar yüksek kaldıraçlı anlardır: yardımcı olacak biçimde tasarlayın.
- Karanlık kalıplardan kaçının: seçenekleri dürüst ve simetrik sunun; bunlar giderek yasadışı hâle geliyor.
- Tutarlı terminoloji ve ton güven kurar ve bilişsel yükü azaltır.
- Çok kanallı iletişimi eşgüdümleyin; kullanıcının dikkatine ve denetimine saygı gösterin.
- İçerik kalitesi doğrudan destek hacminde, tamamlamada, hatalarda ve güvende görünür.

## Kaynaklar ve ileri okuma

- Ginny Redish, *Letting Go of the Words*
- Torrey Podmajersky, *Strategic Writing for UX*
- Sarah Richards, *Content Design*
- Kristina Halvorson and Melissa Rach, *Content Strategy for the Web*
- Nicole Fenton and Kate Kiefer Lee, *Nicely Said*
- Erika Hall, *Conversational Design*
- Harry Brignull, *Deceptive Patterns* (dark patterns research)
- U.S. Federal Plain Language Guidelines and PlainLanguage.gov
- UK Government Digital Service, content design and style guidance
- Nielsen Norman Group, articles on error messages, microcopy, and readability
