# 1.1 Yazılım mühendisliği değerleri

## Genel bakış ve motivasyon

[Yazılım mühendisliği](https://en.wikipedia.org/wiki/Software_engineering) değerleri, insanların yazılımı birlikte nasıl inşa ettiğini biçimlendiren ortak inançlar, normlar ve gündelik davranışlardır. Duvardaki afişler ya da çalışan el kitabındaki sözcükler değildir. Gece 3'te bir olay birini uyandırdığında, genç bir mühendis kıdemli bir mühendisle aynı fikirde olmadığında ya da bir teslim tarihi kaliteyle çarpıştığında gerçekte olan şeydir. Değerler, her teknik kararın altındaki görünmez sistemdir.

Küçük bir ekipte değerler kendiliğinden yayılır: insanlar yan yana oturur, normları özümser ve kendilerini düzeltir. Daha büyük bir ekipte bu yayılma işlemez. Artık değerleri açık hale getirmeniz, yazıya dökmeniz, liderlerin bunları örnek göstermesini sağlamanız ve sistemlerinizle pekiştirmeniz gerekir. Bunu atlarsanız kültür, her iş birliğine sessizce vergi koyan onlarca uyumsuz mikro kültüre parçalanır.

Daha büyük bir ekip için bahis yapısaldır. Zayıf değerler; işten ayrılma, yavaş kararlar, biriktirilen bilgi ve kök nedenleri hiçbir zaman tam olarak giderilmeyen tekrarlayan olaylar olarak ortaya çıkar. Güçlü değerler ise hızlı, güvenli, güvenilir değişiklikler olarak görünür: mühendisler sorunları erken ortaya koyar, başarısızlıktan öğrenir ve sorumluluk alır. Bu iki durum arasındaki fark çoğu zaman herhangi bir teknoloji tercihinden daha büyüktür.

Kurumsal ve kamu kuruluşları bunu keskin biçimde hisseder, çünkü ölçekte, denetim altında ve uzun zaman çizelgelerinde çalışırlar. Bugün inşa edilen sistemler on yıl ya da daha uzun çalışabilir ve asıl yazarlarla hiç tanışmamış insanlar tarafından yürütülür. Bu ortamlarda kültür, niyeti zaman ve personel devri boyunca taşıyan şeydir.

Düzenlemeye tabi kurumsal kuruluşlar bir baskıyla daha karşılaşır: güvenin yerine süreci koyma eğilimi. Hesap verebilirlik yüksek ve hatalar görünür olduğunda refleks; kontrolleri, onayları ve suçlamayı artırmaktır. Anlaşılabilir ama ters teper. En güvenilir, güvenli ve uyumlu kuruluşlar çoğunlukla en cezalandırıcı olanlar değil, en güçlü öğrenme kültürüne sahip olanlardır. Değerler ve uyum müttefiktir, zıt değildir.

## Temel ilkeler

- [Psikolojik güvenlik](https://en.wikipedia.org/wiki/Psychological_safety) temeldir; o olmadan diğer her uygulama bozulur.
- Başarısızlık veridir. Suçlamasız öğrenme olayları kalıcı iyileşmeye dönüştürür.
- Sahiplik yalnızca çıktılar için değil, sonuçlar için hesap verebilirlik demektir: "onu siz inşa edersiniz, siz çalıştırırsınız."
- Yazmak düşünmektir. Kararları yazıya döken bir kültür muhakemesini ölçekler.
- Sürdürülebilir tempo kahramanlıktan üstündür; [tükenmişlik](https://en.wikipedia.org/wiki/Occupational_burnout) kişisel değil, sistemsel bir başarısızlıktır.
- [Çeşitlilik, hakkaniyet ve kapsayıcılık](https://en.wikipedia.org/wiki/Diversity,_equity,_and_inclusion) karar kalitesini artıran mühendislik güçleridir.
- Değerler yukarıdan aşağıya örnek gösterilir ve aşağıdan yukarıya pekiştirilir; liderlerin eylemleri sözlerinden ağır basar.

## Öneriler

### Psikolojik güvenliği bilerek inşa edin

Psikolojik güvenlik, aşağılanma ya da cezalandırılma korkusu olmadan konuşabileceğinize, soru sorabileceğinize, hatalarınızı kabul edebileceğinize ve kararlara itiraz edebileceğinize dair ortak inançtır. Büyük ölçekli çalışmalarda takım etkinliğinin tek ve en güçlü öngörücüsüdür. Onu bilerek inşa edin. Liderlerin kendi hatalarını yüksek sesle sahiplenmesini sağlayın ("işte yaptığım bir hata ve ondan ne öğrendim"). Kötü haberi cezalandırmak yerine merakla karşılayın. Toplantılarda karşıt görüşü açıkça davet edin. İlk kimin konuşacağını döndürün ki kıdemli sesler tartışmayı çapalamasın. Ve "bilmiyorum" ile "yardıma ihtiyacım var" demeyi olağan hale getirin.

### Suçlamasız öğrenmeyi uygulayın

Bir şey bozulduğunda, başarısızlığı tetikleyen kişiye değil, başarısızlığa izin veren koşullara bakın. Suçlamasız [olay sonrası incelemeleri](https://en.wikipedia.org/wiki/Postmortem_documentation) benimseyin: ne olduğunun, zaman çizelgesinin, katkıda bulunan etkenlerin ve sahipleri ve tarihleri olan somut eylem maddelerinin yazılı kaydı. Herkesin o anda bildiklerine göre makul davrandığı varsayımından yola çıkın. "Kim batırdı?" yerine "Bunu yanlış yapmayı ne kolaylaştırdı?" diye sorun. Ve eylem maddelerini tamamlanana kadar izleyin. Takip maddelerini asla kapatmayan bir olay sonrası inceleme kültürü yalnızca tiyatrodur.

### Net sahiplik modelleri oluşturun

"Onu siz inşa edersiniz, siz çalıştırırsınız" ilkesi, bir hizmeti yazan takımı nöbet dahil onu işletmekten sorumlu kılar. Bu, tasarım kararları ile operasyonel acı arasındaki geri bildirim döngüsünü sıkılaştırır ve kaliteyi artırır. Bunu, her sistem için kimin sahibi olduğunu, ona nasıl ulaşılacağını, bağımlılıklarını ve çalışma kılavuzlarını kaydeden bir hizmet kataloğuyla eşleştirin. Sahipliği açık ve örtüşmeyen tutun. Belirsiz sahiplik, sistemlerin çürümesinin ve olayların uzamasının yoludur. Bir takım bir sistemi gerçekten tek başına işletemiyorsa, hesap verebilirliği dağıtmak yerine ona platform desteği verin.

### Yazı kültürü geliştirin

Yazmak düşüncenizi keskinleştirir ve zaman dilimlerini ve yılları aşan eserler yaratır. Önemli değişiklikler için tasarım belgelerini ve karar kayıtlarını olağan hale getirin: problemi, değerlendirilen seçenekleri, önerilen yaklaşımı ve ödünleşimleri belirten, inşa etmeden önce yorum için dolaştırılan kısa bir belge. Bu, anlaşmazlığı henüz ucuzken erken ortaya çıkarır ve ne kararlaştırdığınızın nedenine dair kalıcı bir kayıt bırakır. Şablonları hafif, beklentileri kararın ağırlığıyla orantılı tutun. Ve iyi yazıyı herkesin önünde ödüllendirin.

### Sürdürülebilir temponun korunması

Birkaç kişinin sürdürülemez çabayla kuruluşu defalarca kurtardığı kahraman kültürü, bir erdem değil, zayıflık belirtisidir. İnsanları tüketir, bilgiyi tehlikeli biçimde yoğunlaştırır ve düzeltmeniz gereken asıl sorunları gizler. Bu yüzden nöbet yükünü ölçün ve yönetin. Bir kişi sürekli çağrılıyorsa, bunu mühendislikle ortadan kaldırılacak bir kusur olarak ele alın. İzni olağan kılın, odaklanma süresini koruyun ve çıktıyı bir hafta yerine bir çeyrek üzerinden değerlendirin.

### DEI'ı bir mühendislik gücü olarak ele alın

Çeşitli takımlar daha iyi kararlar verir. Daha fazla bakış açısını tartarlar ve [grup düşüncesine](https://en.wikipedia.org/wiki/Groupthink) ve kör noktalara daha az kapılırlar; bu, erişilebilirlik, güvenlik ve geniş kitlelere hizmet etme açısından çok önemlidir. Kapsayıcılığı gündelik mühendisliğinize işleyin: erişilebilir belgeler, kodda ve arayüzlerde kapsayıcı dil, daha sessiz seslerin katkı yapmasına izin veren toplantı uygulamaları ve hem gösterişli işin hem de tutkal işinin adil paylaşımı.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
| --- | --- | --- |
| Suçlamasız olay sonrası incelemeler | Gerçek kök nedenleri ortaya çıkarır; güven inşa eder; sistemik düzeltmeleri yönlendirir | Dışarıdakilere "hesap verebilirlik yok" gibi gelebilir; eylemleri kapatmak disiplin gerektirir |
| "Onu siz inşa edersiniz, siz çalıştırırsınız" | Sıkı kalite geri bildirim döngüsü; net sahiplik | Nöbet yükü; tükenmişliği önlemek için güçlü platform desteği gerekir |
| Belge öncelikli / RFC kültürü | Kalıcı kararlar; personel devrinde ölçeklenir; eşzamansızlığa uygun | Önemsiz değişiklikler için daha yavaş; aşırı uygulanırsa bürokrasi riski |
| Sürdürülebilir tempo | Elde tutma, güvenilirlik, uzun vadeli hız | Yoğun dönemde daha yavaş hissettirir; liderliğin çizgiyi tutmasını gerektirir |

Merkezi gerilim kısa vadeli hız ile uzun vadeli sağlık arasındadır. Kahramanlık ve suçlama bir an görünen kontrol satın alır, ardından moral ve güvenilirlikte yavaş bir çöküş gelir. Suçlamasız öğrenme, sahiplik ve sürdürülebilir tempo herhangi bir haftada daha yavaş hissettirir, ancak çeyrekler ve yıllar boyunca çok daha yüksek bir hıza bileşir. Liderler, uzun vadeli kapasiteyi korumak için kısa vadeli rahatsızlığı üstlenmeye istekli olmalıdır.

## Takımınızla tartışılacak sorular

1. **"Suçlamasız" ifadesinin denetçilere, yöneticilere ve kamuoyuna "hesap verebilirlik yok" gibi okunmasını nasıl önlersiniz?** Düzenlemeye tabi bir kurumsal kuruluşta ya da gözetim altındaki bir kamu kurumunda, kimseyi suçlu göstermeyen bir olay sonrası inceleme, mühendislik dışındakilere bir örtbas gibi görünebilir. Karşıt değerlendirmeler gerçektir: yalnızca suçlamasızlığın ürettiği dürüstlüğe ihtiyacınız var ve karar vericilerin başarısızlıkların ele alındığına güvenmesine de ihtiyacınız var. Tartışmaya somut kanıt getirin, örneğin olay tekrarlama oranınız ve olay sonrası eylem maddelerinin tamamlanma oranı; çünkü takip maddelerini güvenilir biçimde kapatan bir sistem, günah keçisi olmasa da gözle görülür biçimde hesap verebilirdir. Suçlama kültürünün birleştirdiği iki soruyu ayırın: bunu yanlış yapmayı ne kolaylaştırdı ve biri gerçek ihmalle ya da kötü niyetle mi davrandı. Cevabınız hesap verebilirliğin koşulları düzeltmekte ve eylemleri kapatmakta yattığıysa, dışarıdakiler aradıkları hesap verebilirliği görebilsin diye bu mekanizmayı yayımlayın.

2. **Hangi takımlar gerçekçi biçimde işletemeyecekleri nöbet sistemlerini taşıyor ve bu açığı kim ödüyor?** "Onu siz inşa edersiniz, siz çalıştırırsınız" geri bildirim döngüsünü sıkılaştırır ve bir takımın inşa ettiğini işletecek platform desteğine sahip olduğunu varsayar. Kurumsal ve kamu ölçeğinde bazı takımlar, hiçbir küçük takımın gerçekten tek başına sahiplenemeyeceği eski sistemleri, tedarikçi kara kutularını ya da kesişen altyapıyı miras alır. Ödünleşim, hesap verebilirliği dağıtmak (kötü) ile bir takımı cevaplayamayacağı bir çağrı cihazıyla başarısızlığa hazırlamak (o da kötü) arasındadır. Çağrı verilerini getirin: bir kişi ya da takım sürekli çağrılıyorsa, bunu bir onur rozeti değil, mühendislikle ortadan kaldırılacak bir kusur olarak ele alın. Cevap size, platform takımlarına, kademeli yayınlara ve güncel çalışma kılavuzlarına nerede yatırım yapacağınızı söylemeli; böylece sahiplik net kalırken operasyonel yük insancıl kalır.

3. **Gerçekte teşvik ettiğiniz davranışlar yayımladığınız değerlerle örtüşüyor mu?** Liderler afişlerin kınadığını ödüllendirdiği anda değerler sinizme dönüşür ve ölçekte bu açık, işten ayrılmalar ve sessiz bilgi biriktirme onu ortaya çıkarana kadar görünmez kalır. Son terfi döngünüze dikkatle bakın: yangın söndürmeyi ve kahramanlığı mı yoksa yangın önlemeyi ve büyük bir takımı sağlıklı tutan tutkal işini mi ödüllendirdi? Kurumsal ve kamu kuruluşları riski bileştirir, çünkü katı kademe sistemleri ve uzun görev süreleri, uyumsuz bir teşviğin kimse düzeltmeden yıllarca sürmesine izin verir. Gerçek kanıt getirin: kim terfi etti, kim herkesin önünde övüldü ve bu insanlar gerçekte ne yaptı. Kahramanlık ödül alıyorsa, kuruluşunuza sonra çözmeyi kutladığı krizleri üretmeyi öğretiyorsunuz demektir ve çözüm duvar süsünü değil, teşvikleri değiştirmektir.

4. **Psikolojik güvenliğin belirli bir takımda yüksek mi düşük mü olduğunu, organizasyon şemasından varsaymak yerine gerçekte nasıl bilirsiniz?** Güvenlik, diğer her uygulamanın dayandığı temeldir ve aynı zamanda kendinizi kandırmanın en kolay olduğu şeydir, çünkü en az güvenliğe sahip takımlar size söyleme olasılığı en düşük olanlardır. Ölçekte bin kişi üzerindeki ortalama, önemli olan varyansı gizler: bir yönetici, başka türlü sağlıklı bir kuruluşun içinde sessizce korku temelli bir takım yürütebilir. Karşıt değerlendirmeler açıklık ile rahatlık arasındadır; çünkü gerçek sorunları ortaya çıkaran anket soruları, insanların dürüstçe cevaplamaya en isteksiz olduğu sorulardır ve sinyali toplamak başlı başına güvensiz hissettirebilir. Hislere değil somut kanıta dayanın: doğrulanmış bir güvenlik aracından takım düzeyinde sonuçlar, insanların hatalarını yazılı olarak kabul etme oranı, olay olmadan önce ortaya çıkan ramak kala raporları ve çıkış görüşmesi temaları. Kurumsal ya da kamu kuruluşu için, verinin takım düzeyinde kalmasında ve düşük puan alan bir takımı cezalandırmak için asla kullanılmamasında ısrar edin; çünkü bir güvenlik puanı sopaya dönüştüğü anda güvenliği ölçmeyi bırakır ve ölçüm korkusunu ölçmeye başlar.

5. **Gerçek nöbet ve kahramanlık yükünüz nedir ve yangınları önleyenleri mi yoksa onlarla savaşanları mı ödüllendiriyorsunuz?** Sürdürülebilir tempo, iyi niyetlerin teslimat baskısı altında sessizce çöktüğü yerdir ve büyük bir kuruluş, fark etmeden önce yıllarca birkaç yorgun insanın görünmez fazla mesaisiyle çalışabilir. Gerilim dürüsttür: kahramanlık o anda gerçekten sizi kurtarır ve ona bağımlılık bilgiyi yoğunlaştırır, sistemik kusurları gizler ve en bağlı mühendislerinizi tüketir. Tartışmaya operasyonel veriyi getirin: kişi başına haftalık çağrılar, mesai dışı dağıtımlar, nöbet yükünün takım içindeki dağılımı ve ayrıca ay be ay aynı birkaç isme ne kadarının düştüğü. Son terfi döngünüzün kimi ödüllendirdiğine de bakın. Katı kademe merdivenleri ve uzun görev süreleri olan kurumsal ve kamu kuruluşlarında, yangın söndürmeyi ödüllendiren bir kültür on yıl boyunca sorgulanmadan sürebilir; bu yüzden cevap size çağrı cihazını nerede mühendislikle aşağı çekeceğinizi ve yangın önlemeyi nasıl gözle görülür biçimde terfi ettirilebilir bir eylem haline getireceğinizi söylemelidir.

6. **Son iki yılın önemli kararlarından hangilerinin gerekçesine dair yazılı bir kayıt yok ve yazarlar gittiğinde bu neye mal olacak?** Yazı kültürü, niyeti personel devri boyunca taşıyan şeydir ve yokluğu, birinin artık kimsenin anlamadığı bir sistemi değiştirmesi gerektiği ana kadar görünmezdir. Karşıt çekim hızdır: bir tasarım belgesi ya da karar kaydı yazmak o anda sürtünme gibi hissettirir ve aşırı uygulanırsa önemsiz değişiklikleri yavaşlatan bürokrasiye dönüşür. Kalibre etmek için kanıt getirin: önemli değişikliklerden tasarım belgesi ya da karar kaydı olanların payı, insanların mevcut bir mimarinin gerekçesini gerçekte ne sıklıkla bulup alıntılayabildiği ve yeni bir mühendisin belgelenmemiş bir hizmette üretken olması ne kadar sürüyor. Sistemleri onları inşa edenlerin hepsinden daha uzun yaşayan ve denetim ya da bilgi edinme incelemesiyle karşılaşabilen kurumsal ve kamu kuruluşları için yazılı kayıt hem kurumsal bellek hem de gereken özenin kanıtıdır; bu yüzden cevap çizgiyi kararın ağırlığının yazmayı haklı kıldığı yere çekmeli, daha aşağıya çekmemelidir.

## Sektör merceği

**Girişim.** Değerler hâlâ kendiliğinden yayılır, bu yüzden ağır süreç ithal etmeyin, ama en önemli bir iki davranışı adlandırın; genellikle hatalar konusunda suçlamasız dürüstlük ve kötü haberi erken ortaya koyma eğilimi. Kurucular kendi hatalarını yüksek sesle sahiplenerek tonu belirler, çünkü minik bir takımda Slack'teki tek bir sert tepki herkese sorunları aylarca saklamayı öğretebilir. Kıt pistiniz güvenliği atlamak için değil, korumak için bir nedendir: hataları saklayan bir takım beş dakikalık bir retrodan çok daha pahalıdır.

**Küçük işletme.** Özel bir mühendislik kültürü uzmanı ve sıkı bir bütçe olmadan, satın almanız ya da personel ayırmanız gereken araçlar yerine hafif ritüellere yaslanın. Paylaşılan bir olay kanalı, tek sayfalık bir karar günlüğü ve "bunu yanlış yapmayı ne kolaylaştırdı?" alışkanlığı hiçbir şeye mal olmaz ve değerin çoğunu taşır. Uygulamalar için de yap ya da satın al çizgisini bilinçli çizin: bakımını yapamayacağınız özel bir sistem kurmak yerine hazır bir olay sonrası inceleme şablonu ve basit bir nöbet çizelgesi benimseyin.

**Kurumsal.** Ölçekte iş, tekdüzelik olmadan tutarlılıktır: suçlamasız öğrenme, net ve örtüşmeyen sahiplik ve yazı kültürü; arkasında araçlar, beklentiler ve bir hizmet kataloğu olan kuruluş geneli normlar olur. Yönetişim ve denetim sizi kontrollere iter, bu yüzden güçlü bir öğrenme kültürünün en güvenilir ve uyumlu seçenek olduğunu savunun ve bunu olay tekrarı ve eylem kapatma metrikleriyle gösterin. Takımlar arasındaki varyansa dikkat edin, çünkü ortalamalar sessizce yetenek ve bilgi sızdıran korku temelli cepleri gizler.

**Kamu.** Tedarik kuralları, şeffaflık yükümlülükleri ve kamusal hesap verebilirlik, değerlerin özellikle suçlama etrafında nasıl ifade edileceğini biçimlendirir. Kimseyi suçlu göstermeyen bir olay sonrası inceleme dış gözetime örtbas gibi okunabilir; bu yüzden mekanizmayı yayımlayın, hesap verebilirliğin koşulları düzeltmekte ve eylemleri kapatmakta yattığını gösterin ve vatandaşların ve denetçilerin görmesine izin verin. Sistemler yönetimlerden uzun yaşadığı ve personel devri yıllarla ölçüldüğü için, yazılı karar kayıtlarını hem kurumsal bellek hem de bilgi edinme incelemesi altında gereken özenin kanıtı olarak ele alın.

## Örnekler

**Girişim.** Altı kişilik bir girişim güven ve koridor sohbetiyle çalışır, bu yüzden kimse takımın değerlerini yazıya dökmez. Bir kurucu mühendis kötü bir geçiş yayımladığında ve CTO Slack'te ona çıkıştığında oda sessizleşir ve sonraki iki hata ortaya çıkarılmak yerine sessizce saklanır. Takım tek bir hafif alışkanlık benimseyerek toparlanır: her olaydan sonra beş dakikalık, şablon gerektirmeyen, suçlamasız bir "bunu yanlış yapmayı ne kolaylaştırdı?" sohbeti. Bu küçük ritüel, daha büyük bir kuruluşun ihtiyaç duyacağı süreç yükü olmadan kendiliğinden yayılan kültürü sağlıklı tutar.

**Kurumsal.** Büyük bir finansal hizmetler firması, rutin bir yapılandırma değişikliği hizmetler arasında zincirleme yayıldığında büyük bir kesinti yaşadı. Suçlama kültüründe değişikliği yayımlayan mühendis azarlanırdı ve iş burada biterdi. Bunun yerine suçlamasız bir olay sonrası inceleme, dağıtım araçlarının tehlikeli değişikliği güvenli olandan ayırt edilemez gösterdiğini, kademeli bir yayın olmadığını ve çalışma kılavuzunun güncel olmadığını ortaya koydu. Firma kademeli yayınlara ve yapılandırma doğrulamasına yatırım yaptı ve benzer değişiklikler artık güvenle başarısız oluyor. Kişiye değil sisteme bakmayı seçmek kalıcı bir mühendislik iyileştirmesi üretti.

**Kamu.** Bir kamu dijital hizmet kurumu, katı bir belge öncelikli [RFC](https://en.wikipedia.org/wiki/Request_for_Comments) (yorum talebi) süreciyle birlikte "onu siz inşa edersiniz, siz çalıştırırsınız" ilkesini benimsedi. Sistemleri siyasi yönetim değişikliklerinden ve yıllarla ölçülen personel devrinden sağ çıkmak zorunda olduğu için, her önemli karar bağlamı ve ödünleşimleri açıklayan bir tasarım belgesine kaydedilir. Yeni mühendisler ve gelen yükleniciler, on yıllık bir mimarinin ardındaki gerekçeyi tersine mühendislikle çözmek yerine okuyabilir. Bu yazılı [kurumsal bellek](https://en.wikipedia.org/wiki/Institutional_memory), kurumun yüksek personel devrine ve katı hesap verebilirlik gereksinimlerine rağmen kamu hizmetlerini güvenilir tutmasını sağlayan şeydir.

## İş gerekçesi: motivasyonlar, YG ve TSM

Kültürün getirisi gerçektir ama dolaylıdır ve bu yüzden kronik olarak az finanse edilir. Bir sistemin ömrü boyunca baskın maliyet onu inşa etmek değildir. Bakım, olay müdahalesi, yeniden iş ve yetenekli insanları kaybetme ve yeniden işe alma maliyetidir. Güçlü bir öğrenme kültürü bunların her birini iyileştirir. Suçlamasız olay sonrası incelemeler tekrar eden olayları azaltır. Net sahiplik ortalama kurtarma süresini azaltır. Yazı kültürü [işe alıştırma](https://en.wikipedia.org/wiki/Onboarding) maliyetini ve öncesindeki gerekçeden habersiz verilen kararların maliyetini düşürür.

Yalnızca işten ayrılmayı ele alın. Orta düzey bir mühendisi değiştirmek, işe alım, uyum süresi ve kapıdan çıkıp giden kurumsal bilgiyi sayınca tipik olarak yıllık maaşlarının yarısı ile iki katı arasında bir yere mal olur. Daha sağlıklı bir kültür, bin kişilik bir kuruluşta pişman olunan ayrılmaları birkaç yüzde puan bile azaltırsa, tasarruflar olay sonrası inceleme yapmanın ve belge yazmanın mütevazı maliyetini gölgede bırakır. Benimseme maliyeti çoğunlukla liderlik dikkati ve biraz süreç yüküdür. Benimsememenin maliyeti sürekli ve görünmez biçimde ödenir: daha yavaş teslimat, tekrar eden olaylar ve sessiz yetenek kaybı.

Liderliğe gerekçeyi sunmak için kültürü yöneticilerin zaten izlediği metriklere bağlayın: teslimat bekleme süresi, değişiklik başarısızlık oranı, ortalama kurtarma süresi, olay tekrarı ve pişman olunan ayrılmalar. Psikolojik güvenliği yumuşak bir fayda olarak değil, diğer her mühendislik yatırımının karşılığını vermesini sağlayan mekanizma olarak çerçeveleyin; çünkü güvensiz takımlar, bu yatırımların düzeltmek için tasarlandığı sorunları tam da gizler.

## Anti-kalıplar ve tuzaklar

- Suçla ve utandır olay incelemeleri: sorunları yeraltına iter ve insanlar bildirmeyi bırakır.
- Kahraman tapınması: yangın önleme yerine yangın söndürmeyi ödüllendirmek yangınları sürdürür.
- Liderlerin ihlal ettiği "değerler": davranışla çelişen beyan edilmiş değerler sinizm yaratır.
- Destek olmadan sahiplik: takımların gerçekçi biçimde işletemeyeceği sistemler için nöbet atamak.
- Güven ikamesi olarak süreç: gerçek güvenlik inşa etmek yerine onayları yığmak.
- Belge tiyatrosu: kimsenin okumadığı ya da kararları hiç etkilemeyen belgeler yazmak.
- Onay kutusu olarak kapsayıcılık: çeşitlilik için işe almak ama aynı sesleri kararlardan dışlamak.

## Olgunluk modeli

- Düzey 1, Başlangıç: Değerler tesadüfi ve kişiliğe bağlıdır. Olaylar suçlama demektir, bilgi birkaç kafada yaşar ve işler kahramanlıkla yapılır. Kimse takımın neye inandığını ya da baskı altında nasıl davrandığını yazıya dökmemiştir.
- Düzey 2, Geliştirme: Birkaç takım suçlamasız olay sonrası incelemelere başlar, ara sıra tasarım belgesi yazar ve sahiplikten söz eder, ancak uygulamalar tutarsız, eşitsiz uygulanmış ve henüz liderlik tarafından pekiştirilmemiştir. Sağlıklı bir takıma düşüp düşmemeniz çoğunlukla şanstır.
- Düzey 3, Standartlaştırma: Suçlamasız öğrenme, net ve örtüşmeyen sahiplik ve yazı kültürü; şablonlar, bir hizmet kataloğu ve tanımlanmış nöbet beklentileriyle kuruluş geneli belgelenmiş normlardır. Liderler değerleri örnek gösterir ve iyi bir yöneticinin oturduğu yerde değil, her yerde aynı davranışlar beklenir.
- Düzey 4, Yönetme: Kültür temel çizgilere karşı ölçülür ve verilerle kontrol edilir. Takım düzeyinde psikolojik güvenlik puanlarını, olay tekrarını, olay sonrası eylem maddesi kapatma oranını, nöbet yükü dağılımını, ortalama kurtarma süresini ve pişman olunan ayrılmaları izlersiniz ve bir takım saptığında sayılara göre hareket edersiniz. Yangın söndürme teşviklerini kanıtla ortadan kaldırın ve artık görebildiğiniz için yangın önlemeyi ödüllendirin.
- Düzey 5, Orkestrasyon: Kültür sürekli iyileştirilir ve tüm kuruluşun nasıl planladığı, işe aldığı ve terfi ettirdiğiyle bütünleşir. Güvenlik yüksektir, öğrenme hızlıdır ve uygulamalar kanıt ve bağlam değiştikçe uyum sağlar. Kuruluş nöbet yükünü yeniden dengeler, karar kayıtlarını tazeler ve normlarını bir krizin konuyu zorlamasını beklemek yerine bilinçli biçimde geliştirir.

## Tartışma fikirleri

- Kuruluşumuzda insanlar nerede "bilmiyorum" ya da "katılmıyorum" demekte kendilerini güvende hissetmiyor ve neden?
- Olay incelemelerimiz sistemi değiştiriyor mu, yoksa yalnızca kusuru atayıp devam mı ediyor?
- Mühendislikle ortadan kaldırmamız gereken kahramanlıkları mı ödüllendiriyoruz?
- Son iki yılın hangi önemli kararlarının gerekçesine dair yazılı bir kayıt yok?
- Tutkal işi ve nöbet yükü takım içinde ne kadar eşit dağılmış?
- Beyan ettiğimiz değerler, burada insanları gerçekten terfi ettiren şeyle örtüşüyor mu?

## Önemli çıkarımlar

- Değerler, her teknik kararın ardındaki görünmez işletim sistemidir; ölçekte değerler açık olmalıdır.
- Psikolojik güvenlik temeldir; o olmadan diğer uygulamalar çürür.
- Suçlamasız öğrenme başarısızlığı kalıcı sistemik iyileştirmeye dönüştürür.
- Net sahiplik ("onu siz inşa edersiniz, siz çalıştırırsınız") kalite geri bildirim döngüsünü sıkılaştırır.
- Yazı kültürü muhakemeyi zaman dilimleri ve personel devri boyunca ölçekler.
- Sürdürülebilir tempo ve kapsayıcılık birer maliyet değil, uzun vadeli hız çarpanlarıdır.

## Kaynaklar ve ileri okuma

- Amy C. Edmondson, "The Fearless Organisation" ve "Teaming"
- Google re:Work / Project Aristotle research on team effectiveness
- Sidney Dekker, "The Field Guide to Understanding 'Human Error'"
- John Allspaw, "Blameless PostMortems and a Just Culture" (Etsy Code as Craft)
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate: The Science of Lean Software and DevOps"
- Gene Kim et al., "The Phoenix Project" and "The DevOps Handbook"
- Camille Fournier, "The Manager's Path"
- Will Larson, "An Elegant Puzzle: Systems of Engineering Management"
- Tom DeMarco and Timothy Lister, "Peopleware: Productive Projects and Teams"
