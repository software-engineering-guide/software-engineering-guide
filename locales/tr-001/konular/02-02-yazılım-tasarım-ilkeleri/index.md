# 2.2 Yazılım tasarım ilkeleri

## Genel bakış ve motivasyon

Yazılım tasarım ilkeleri, kodu zaman içinde anlayabileceğiniz, değiştirebileceğiniz ve genişletebileceğiniz biçimde düzenlemek için buluşsal yöntemlerdir. Adı konmuş kısaltmaları ([SOLID](https://en.wikipedia.org/wiki/SOLID), beş [nesne yönelimli](https://en.wikipedia.org/wiki/Object-oriented_programming) tasarım ilkesi için; [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), kendini tekrar etme; [KISS](https://en.wikipedia.org/wiki/KISS_principle), basit tut; [YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it), buna ihtiyacın olmayacak), yapısal kavramları ([bağlaşım](https://en.wikipedia.org/wiki/Coupling_(computer_programming)), [bütünlük](https://en.wikipedia.org/wiki/Cohesion_(computer_science)), [ilgilerin ayrılması](https://en.wikipedia.org/wiki/Separation_of_concerns)), katalogdaki [tasarım kalıplarını](https://en.wikipedia.org/wiki/Software_design_pattern), [Alan Odaklı Tasarım](https://en.wikipedia.org/wiki/Domain-driven_design) (yazılımı iş alanının dilinde modelleme) gibi daha üst düzey modelleme yaklaşımlarını ve nesne yönelimli, [işlevsel](https://en.wikipedia.org/wiki/Functional_programming) ve [veri odaklı](https://en.wikipedia.org/wiki/Data-oriented_design) üsluplar arasındaki seçimi içerirler. Bunların hiçbiri yasa değildir. Sıkıştırılmış deneyimdir ve onları muhakemeyle uygulamanız gerekir.

Büyük takımlar için paylaşılan ilkelerin değeri eşgüdümdür. Yüzlerce mühendis aynı sistem üzerinde çalıştığında, tasarım tartışmaları için ortak bir sözcük dağarcığına ve bağımsız yazılan modüllerin birbirine oturması için ortak bir varsayılanlar kümesine ihtiyaç duyarlar. İyi tasarım, birçok insanın sürekli çarpışmadan bir sistemi paralel değiştirmesini sağlayan şeydir. Ayrıca bir sistemi on yıl sonra da değiştirilebilir tutan şeydir; kurumsal ve kamu sistemlerinin normal ömrü, özgün yazarların görev süresinin çok ötesinde.

Kritik beceri ilkeleri ezberlemek değildir. Her birinin sizi ne zaman yanılttığını bilmektir. Her ilkenin bir başarısızlık biçimi vardır: DRY yanlış soyutlama üretebilir, SOLID gereksiz dolaylılık üretebilir, YAGNI gerçekten ihtiyaç duyduğunuz genişletilebilirliği aç bırakabilir. Bu bölüm ilkeleri uygulanabilirlik alanı olan araçlar olarak ele alır ve kısaltmaların hizmet etmeye çalıştığı daha derin özellikler olarak bağlaşım ve bütünlüğü vurgular.

## Temel ilkeler

- Önce bağlaşımı ve bütünlüğü yönetin; adı konmuş ilkelerin çoğu bu iki özelliği iyileştirmenin dolaylı yollarıdır.
- Değişim için optimize edin: iyi tasarım, gerçekten yapmanız gereken değişikliklerin maliyetini en aza indirir.
- Şimdi çalışan en basit tasarımı tercih edin, ama değişimin olası olduğu yerde sınırları koruyun.
- Tekrar, yanlış soyutlamadan ucuzdur; kalıp netleşene kadar bekleyin.
- Bağımlılıkları açık kılın ve onları kararlı şeylere doğru yöneltin.
- Alanı alanın dilinde modelleyin; yazılım sınırlarını iş sınırlarıyla hizalayın.
- Paradigmaları ideolojiye değil soruna uyacak şekilde seçin; çoğu büyük sistem pragmatik olarak karışıktır.

## Öneriler

### SOLID'i bir kontrol listesi değil, bir mercek olarak kullanın

Modülleri bütünlüklü tutmak için tek sorumluluğu, bir sınırın gerçekten var olduğu yerde bağımlılıkları soyutlamalara yöneltmek için bağımlılık tersine çevirmeyi ve uzantı noktalarının gerçek olduğu yerde açık-kapalıyı uygulayın. Yalnızca bir gerçekleştirim varken ve ikincisi görünürde yokken kısaltmayı tatmin etmek için arayüzler, fabrikalar ve katmanlar üretmeyin. Dolaylılığın bir maliyeti vardır ve onu her okumada ödersiniz.

### DRY'ı metne değil, bilgiye uygulayın

DRY, tek bir yetkili *bilgi* parçasını tekrar etmemekle ilgilidir. Yalnızca benzer görünen satırları ortadan kaldırmakla ilgili değildir. Benzer görünen ama farklı nedenlerle değişen iki kod parçası ayrı kalmalıdır. İlgisiz şeyleri bağlayan erken bir paylaşılan soyutlama yerine biraz tekrarı tercih edin. Gerçek kalıp iki ya da üç kez ortaya çıktığında soyutlamayı çıkarın.

### KISS ve YAGNI'nin spekülasyona direnmesine izin verin

Hayal ettiğiniz değil, sahip olduğunuz gereksinimler için inşa edin. Yapılandırılabilir çerçeveler, eklenti sistemleri ve kimsenin istemediği uzantı noktaları gibi spekülatif genelliği önleyin. Karşı denge, bazı esnekliğin gerçekten erken inşa edilmesinin daha ucuz olmasıdır; kararlı bir arayüz ya da temiz bir dikiş gibi. YAGNI spekülatif *gerçekleştirime* karşı çıkar, düşünceli sınırlara değil.

### Düşük bağlaşım ve yüksek bütünlük için açıkça tasarlayın

Her modülü tek, iyi tanımlanmış bir şey yaptırın (bütünlük) ve dar arayüzler aracılığıyla mümkün olduğunca az başka modüle bağımlı olun (düşük bağlaşım). Bir tasarımı incelediğinizde, hangi değişikliklerin modül sınırları boyunca dalgalandığını sorun. O dalgalar bağlaşımın gerçek ölçüsüdür. İlgilerin ayrılması, katmanlara ve kesişen ilgilere uygulanan aynı fikirdir.

### Tasarım kalıplarını sözcük dağarcığı olarak kullanın, anti-kalıpları uyarı olarak uygulayın

Kalıplar yinelenen çözümler için yararlı paylaşılan adlardır. Sorun gerçekten eşleştiğinde birine uzanın. Sofistike görünmek için kalıp dayatmayın, çünkü kalıpla dolu kod çoğu zaman aşırı mühendisliğin işaretidir. Yaygın [anti-kalıpları](https://en.wikipedia.org/wiki/Anti-pattern) (tanrı nesneleri, uygunsuz yerlerde anemik modeller, büyük çamur topları, dağıtık tek parçalar) tanı etiketleri olarak öğrenin.

### Alan karmaşık olduğunda Alan Odaklı Tasarımı benimseyin

Zengin iş kuralları olan sistemler için DDD'nin taktik ve stratejik araçlarını kullanın: alan uzmanlarıyla paylaşılan yaygın bir dil, sistemi bağımsız modellenen parçalara ayıran sınırlı bağlamlar ve bu parçaların nasıl ilişkili olduğunu tarif eden bağlam haritaları. Sınırlı bağlamlar özellikle kurumsal ölçekte değerlidir, çünkü takım sahipliğini model sınırlarıyla hizalar. DDD basit [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) (oluştur, oku, güncelle, sil) sistemleri için fazladır.

### Paradigmaları uyuma göre seçin

Durumlu davranışı kapsüllemek ve alanları modellemek için nesne yönelimini kullanın. Dönüşümler, eşzamanlılık ve [değişmezlik](https://en.wikipedia.org/wiki/Immutable_object) yoluyla öngörülebilirlik için işlevsel üslubu kullanın. Performansın ve önbellek davranışının baskın olduğu yerde veri odaklı tasarımı kullanın. Büyük sistemler üçünü de karıştırır. Seçimi bileşen başına yapın ve üsluplar arasındaki sınırları temiz tutun.

## Ödünleşimler: artılar ve eksiler

| İlke / yaklaşım | İyi uygulandığında | Başarısızlık biçimi |
|---|---|---|
| SOLID | Değişimin gerçekleştiği yerlerde net dikişler; sınanabilir birimler | Arayüz ve katman çoğalması; getirisiz dolaylılık |
| DRY | Gerçek bilgi için tek doğruluk kaynağı | İlgisiz kodu bağlayan yanlış soyutlama |
| KISS / YAGNI | Yalın, anlaşılabilir sistemler | Az tasarlanmış dikişler; gereken esnekliğin maliyetli sonradan eklenmesi |
| Tasarım kalıpları | Paylaşılan sözcük dağarcığı; kanıtlanmış yapılar | Kalıp kargo kültü; kazara karmaşıklık |
| Alan Odaklı Tasarım | Hizalı modeller ve takımlar; evcilleştirilmiş karmaşıklık | Basit alanlarda ağır tören; yanlış yerleştirilmiş bağlam sınırları |
| İşlevsel / değişmez | Öngörülebilirlik; daha güvenli eşzamanlılık | Doğası gereği durumlu sorunlara sakar uyum; performans sürprizleri |

Yinelenen gerilim az tasarım ile aşırı tasarım arasındadır. Az tasarlanmış sistemler bağlaşım biriktirir ve katılaşır. Aşırı tasarlanmış sistemler birinin anlaması ve sürdürmesi gereken soyutlamada boğulur. Cevap sabit bir nokta değildir. Bir disiplindir: fikrinizi değiştirmenize izin veren dikişleri koruyarak, yeterli bilgiye sahip olana kadar kararları erteleyin.

## Takımınızla tartışılacak sorular

1. **Paylaşılan bir soyutlamayı çıkarmak için somut eşiğiniz nedir ve DRY'ın yanlış olanı üretmesini nasıl önlersiniz?** Bu bölüm tekrarın yanlış soyutlamadan ucuz olduğu konusunda açıktır ve çıkarmadan önce kalıbın iki ya da üç kez görünmesini beklemenizi söyler. Büyük bir takımda tehlike, birinin benzer görünen iki parçayı takım sınırları arasında paylaşılan bir modüle ayırması ve ardından her gelecek değişikliğin bir çağıranı diğerine dalgalandırmasıdır. Getirilecek sinyal, tekrarlanan parçaların aynı nedenle mi değiştiği yoksa yalnızca şimdilik benzer mi göründüğüdür. Üçün kuralı üzerinde anlaşın ve çağıranları bağlamadan önce aday bir soyutlamanın gerçekten birlikte değiştiğini isteyin. Bu tek anlaşma, birçok takım ona bağımlı olduğunda çözülmesi pahalı bir bağlaşım sınıfını önler.

2. **Bağlaşımı ve bütünlüğü sezgiye bırakmak yerine tasarım incelemesinde nasıl görünür kılarsınız?** Temel ilkeler bağlaşımı ve bütünlüğü her kısaltmanın üstüne koyar ve bağlaşımı modül sınırları boyunca dalgalanan değişiklikler olarak tanımlar. Sezgi, her biri sistemin yalnızca kendi köşesini gören yüzlerce mühendis boyunca ölçeklenmez. Bir makinenin üretebileceği kanıtı getirin: bağımlılık grafikleri ve hangi modüllerin aynı commit'lerde birlikte düzenlenmeye devam ettiğini gösteren birlikte değişim verileri. Bir değişikliğin hangi modül sınırlarını geçmeye zorladığını soran açık bir inceleme sorusu ekleyin. İki modül her zaman birlikte değiştiğinde, bu ya onları birleştirmeniz ya da aralarındaki sınırı düzeltmeniz için işarettir.

3. **Sistemlerinizde Alan Odaklı Tasarımı haklı çıkaracak kadar zengin bir alan ile onun fazla olduğu düz bir CRUD uygulaması arasındaki çizgi nerede?** Bölüm DDD'nin sınırlı bağlamlarını tam olarak takım sahipliğini model sınırlarıyla hizaladıkları için önerir ve DDD'nin basit oluştur-oku-güncelle-sil sistemleri için fazla olduğunu ve gerçek modelleme olmadan törene dönüştüğünü uyarır. Bunu her iki yönde yanlış yapmanın maliyeti yüksektir: ince bir alanda ağır DDD basit bir uygulamayı törene gömer, birçok takım arasında yayılan bir paylaşılan model ise sürekli takımlar arası eşgüdüm zorlar. Gerçekten karar veren sinyalleri getirin: iş kurallarının yoğunluğu ve kaç takımın parçaları bağımsız sahiplenmesi gerektiği. Stratejik makineyi karmaşık çekirdeğe ayırın ve basit kenarların basit kalmasına izin verin. Bu sizi hem DDD tiyatrosundan hem büyük çamur topundan uzak tutar.

4. **Bir soyutlama, arayüz ya da tasarım kalıbı eklediği dolaylılığa ne zaman değer ve bir tasarımı aşırı mühendislik diye adlandırma yetkisi kimde?** Bu bölüm dolaylılığın her okumada ödediğiniz bir maliyeti olduğu ve SOLID'i tatmin etmek ya da sofistike görünmek için arayüzler, fabrikalar ve katmanlar üretmenin bir başarısızlık biçimi olduğu konusunda açıktır. Büyük bir takımda baskı ters yöne işler: inceleyiciler ekstra soyutlamayı disiplinli göründüğü için geçirir ve kimse daha az yapıyı savunan kişi olmak istemez. Karşıt değerlendirme gerçektir, çünkü bazı dikişler yerini gerçekten hak eder ve onları sonra kaldırmak pahalıdır. Tartışmaya somut kanıt getirin: bir arayüzün bugün gerçekte kaç gerçekleştirimi var, uzantı noktası hiç ne sıklıkla esnedi ve bir okuyucunun tek bir kod yolunu izlemek için kaç dosya açması gerekiyor. Görünürde ikincisi olmayan tek bir gerçekleştirimin satır içine alınmak için varsayılan neden olduğu konusunda anlaşın ve bir tasarımı hakaret gibi okunmadan aşırı mühendislik olarak etiketleyebilecek kişiyi adlandırın. Yazarlarından bir on yıl uzun yaşayan kurumsal ve kamu sistemlerinde, gereksiz dolaylılık her gelecek bakımcının ödediği bir vergidir; bu yüzden "bu soyutlama bize ne satın alıyor" sorusunu kişisel bir meydan okuma değil, kalıcı bir inceleme sorusu olarak ele alın.

5. **Her bileşenin hangi paradigmayı, nesne yönelimli, işlevsel ya da veri odaklı, kullandığına nasıl karar verirsiniz ve aralarındaki sınırları nasıl temiz tutarsınız?** Bölüm, büyük sistemlerin pragmatik olarak karışık olduğunu ve bileşen başına uyuma göre seçmeniz gerektiğini savunur; durumlu alanlar için nesne yönelimini, dönüşümler ve eşzamanlılık için işlevsel üslubu ve performansın ve önbellek davranışının baskın olduğu yerde veri odaklı tasarımı kullanarak. Yönetilmezse paradigma seçimi, modülü ilk kimin yazdığı meselesi olur ve değişken durum saf olması gereken dönüşümlere sızar ya da işlevsel bir saflık doğası gereği durumlu bir sorunla savaşır. Getirmeye değer kanıt, gerçek acınızın nerede olduğudur: hangi bileşenler gizli durum nedeniyle test edilmesi zor, hangi sıcak yollar önbelleğe bağlı ve mevcut üslubun sakar geçici çözümlere zorladığı yer. Her katman için varsayılan paradigmaya bilinçli karar verin ve üsluplar arasındaki dikişlerin nereye düştüğünü yazın ki işlevsel bir çekirdek ve zorunlu bir kenar birbirine sızmasın. Bir hesaplamanın belirli bir dönem için denetlenebilir ve yeniden üretilebilir olması gereken düzenlemeye tabi ya da kamu sisteminde, değişmez, işlevsel bir çekirdek çoğu zaman bir zevk değil bir uyum gereksinimidir ve bu kısıt sınırı izlemek yerine yönlendirmelidir.

6. **Bu ilkelerin dogmaya sertleşmesini nasıl önlersiniz ve bir tasarım kararının ardındaki gerekçeyi gelecekteki bir takımın yeniden ele alabilmesi için nereye kaydedersiniz?** Bu bölümdeki her ilkenin bir uygulanabilirlik alanı ve bir başarısızlık biçimi vardır ve tüm çerçeveleme onları uygulanacak yasalar değil muhakemeyle kullanılacak araçlar olarak ele alır. Büyük bir takımda bir ilke sessizce bir kurala dönüşür: DRY her tekrarı yasaklar, SOLID sınıf başına bir arayüz zorunlu kılar ve pragmatik istisnalar sonuç yerine kısaltmayı alıntılayan insanlar tarafından incelemede engellenir. Gerilim, bir miktar tutarlılığın yüzlerce mühendisin eşgüdümüne gerçekten yardım etmesidir; bu yüzden her ilkeyi basitçe isteğe bağlı ilan edemezsiniz. Bir ilkeye harfiyen uymanın daha kötü bir tasarım ürettiği örnekleri ve varsa, belirli bir sınırın ya da soyutlamanın neden var olduğunu açıklayan karar kayıtlarını getirin. İlkelerin bir mühendisin kayıtlı bir gerekçeyle sapabileceği varsayılanlar olduğu konusunda anlaşın ve sonuçlu tasarım seçimlerini kısa bir mimari karar kaydında yakalayın ki sonraki takım yalnızca kodu değil gerekçeyi de miras alsın. Özgün yazarların çoktan gittiği ve denetimlerin sistemin neden böyle biçimlendiğini sorduğu kurumsal ve kamu sistemlerinde, o yazılı iz, gelecekteki takımların güvenle değiştirebileceği bir tasarım ile dokunmaktan korktukları bir tasarım arasındaki farktır.

## Sektör merceği

**Girişim.** Yayımlanan en basit tasarımı tercih edin ve gerçek bir ikinci kullanım durumu bir dikişi zorlayana kadar tek iyi düzenlenmiş modül tutun. En kıt kaynağınız mühendislik dikkatidir; bu yüzden erken arayüzler, katmanlar ve spekülatif çerçeveler saf maliyettir. Herhangi bir paylaşılan soyutlamayı çıkarmadan önce üçün kuralını izleyin ve YAGNI'nin henüz kimsenin istemediği uzantı noktalarını öldürmesine izin verin.

**Küçük işletme.** Kadroda mimar olmadan ve sıkı bir bütçeyle, kendi kalıplarınızı icat etmek yerine satın aldığınız çerçevelere ve kütüphanelere zaten işlenmiş tasarıma yaslanın. Özel tasarım çabasını gerçekten sizin işiniz olan birkaç kurala ayırın ve geri kalan her şeyi geleneksel tutun ki bir yüklenici ya da yeni bir işe alınan onu okuyabilsin. Anladığınız biraz tekrar, yalnızca yazarının sürdürebileceği zekice bir soyutlamadan iyidir.

**Kurumsal.** Paylaşılan ilkelerin getirisi birçok takım arasında eşgüdümdür: tasarım incelemesi için ortak bir sözcük dağarcığı ve gruplar bağımsız evrilsin diye model sınırlarını takım sahipliğiyle hizalayan sınırlı bağlamlar. Bağlaşımı ve bütünlüğü bağımlılık ve birlikte değişim verileriyle açıkça yönetin ve sonuçlu tasarım kararlarını kaydedin ki sistemler yazarları ayrıldıktan çok sonra bile değiştirilebilir kalsın. Hem takımları bağlayan yanlış soyutlamaya hem her okuyucuyu vergilendiren aşırı mühendisliğe karşı eşit derecede korunun.

**Kamu.** Denetlenebilirlik ve yeniden üretilebilirlik çoğu zaman tasarımı belirler. Değişmez, işlevsel bir çekirdek, belirli bir dönem için geçmiş bir hesaplamayı tam olarak yeniden üretmenizi sağlar; gizli değişken durumlu karmaşık bir nesne grafiği bunu garanti edemez. Bağlam sınırlarında paylaşılan tablolar yerine açık yayımlanmış sözleşmeleri tercih edin ve tasarımı ve karar kayıtlarını denetçiler ve sistemi bir on yıl sonra miras alacak takım için okunabilir tutun.

## Örnekler

**Girişim.** İlk ürününü inşa eden üç mühendislik girişimi, her özelliği arayüz ve fabrika katmanlarına bölme dürtüsüne direnir; gerçek bir ikinci kullanım durumu ortaya çıkana kadar tek iyi düzenlenmiş modül tutar. Aynı mantık kayıt ve faturalama akışlarında üçüncü kez göründüğünde, spekülatif bir çerçeve yerine tek küçük paylaşılan bir işlevi çıkarırlar. Bu, kod tabanını herhangi birinin kafasında tutabileceği kadar küçük tutar ve çizdikleri birkaç dikiş ürünün en çok değişmesi muhtemel olduğu yere düşer.

**Kurumsal.** Büyük bir sigorta platformu poliçe, hasar ve faturalamayı, her biri kendi veri modeli ve hizmet sınırı olan özel bir takıma ait ayrı sınırlı bağlamlar olarak modeller. Bağlamların buluştuğu yerde, bir hasar bir poliçeye başvurduğunda, paylaşılan veritabanı tabloları yerine açık yayımlanmış sözleşmelerle konuşurlar. Bu, üç takımın bağımsız evrilmesine izin verir ve yaygın dil, sigortacılar ve aktüerlerle konuşmaları kesin tutar. Daha önceki bir sürüm tek bir yayılan modeli paylaşmıştı ve her değişiklik takımlar arası eşgüdüm gerektiriyordu.

**Kamu.** Ulusal bir vergi işleme sistemi hesaplama motoru için bilinçli olarak veri odaklı, işlevsel bir çekirdeği tercih eder. Vergi kuralları, değişmez girdi kayıtları üzerinde saf dönüşümler olarak ifade edilir; bu, onları belirli bir vergi yılı için denetlenebilir, sınanabilir ve yeniden üretilebilir kılar. Zorunlu, durumlu parçalar (iş akışı, bildirimler) kenarlarda tutulur. Denetçiler belirli bir kural sürümüne işaret edebilir ve herhangi bir geçmiş hesaplamayı tam olarak yeniden üretebilir; bu, gizli değişken durumlu karmaşık bir nesne grafiğinin garanti edemeyeceği yasal bir gereksinimdir.

## İş gerekçesi: motivasyonlar, YG ve TSM

Tasarım kalitesi, bir sistemin *değiştirilebilirliğine* yapılan bir yatırımdır ve değiştirilebilirlik toplam sahip olma maliyetine hâkimdir. Bir sistemin maliyetinin çoğu ilk yayından sonra, değişiklik ve genişletmede ortaya çıkar. İyi tasarlanmış sistemler değişim maliyetini zaman içinde kabaca sabit tutar. Kötü tasarlanmış olanlarda her değişikliğin maliyeti, sistem fiilen değiştirilemez hale gelip yeniden yazılması gerekene kadar, hepsinin en pahalı sonucu, tırmanır.

Benimseme maliyeti çoğunlukla beceri ve inceleme disiplinidir: ilkeleri öğretmek ve baştan tasarım zamanı harcamak. Benimsememenin maliyeti [teknik borcun](https://en.wikipedia.org/wiki/Technical_debt) yavaş birikimi, düşen teslimat hızı, artan kusur oranları ve sonunda maliyetli yeniden yazmalardır. Liderliğe gerekçeyi sunmak için tasarım disiplinini teslimat öngörülebilirliğine ve yeniden yazma programlarından kaçınmaya bağlayın ve zaman içinde değişim başarısızlık oranı ve karşılaştırılabilir özellikleri gerçekleştirme süresi gibi öncü göstergeleri izleyin. Tersi başarısızlığa da dikkat edin: belirsiz gelecekler için tasarıma aşırı yatırım yapmak da değeri yok eder. Bu yüzden argüman *uygun* tasarım içindir; gelecekteki değişimin ne kadar olası ve maliyetli olduğuna göre ayarlanmış.

## Anti-kalıplar ve tuzaklar

- **Spekülatif genellik:** hiç gelmeyen hayali gereksinimler için genişletilebilirlik inşa etmek.
- **Yanlış soyutlama:** DRY'ı tatmin etmek için ilgisiz kodu zorla bir araya getirmek; tekrardan daha kötü bir bağlaşım yaratmak.
- **Kalıp kargo kültü:** tasarım kalıplarını kendi iyiliği için uygulamak; fayda olmadan dolaylılık eklemek.
- **Anemik ya da tanrı nesneleri:** davranışı olmayan modeller ya da her şeyi yapan nesneler; ikisi de yanlış yerleştirilmiş sorumlulukları işaret eder.
- **Dağıtık tek parça:** fiziksel olarak bölünmüş ama hâlâ sıkı bağlı hizmetler; iki yaklaşımın maliyetlerini birleştirir.
- **Büyük çamur topu:** fark edilebilir yapı yok; her değişiklik her şeyi riske atar.
- **DDD tiyatrosu:** ona değer veren alan modellemesi olmadan sözcük dağarcığını ve klasör yapısını benimsemek.

## Olgunluk modeli

- **Düzey 1, Başlangıç:** Tasarım gelişigüzel ve reaktiftir; bağlaşım denetimsiz birikir; ilkeler bilinmez ya da slogan olarak anılır ve soyutlamalar bireysel alışkanlıkla belirir ya da kaybolur.
- **Düzey 2, Geliştirme:** Takımlar ilkeleri bilir ve uygular, ama tutarsız ve çoğu zaman dogmatik; bazı gruplar bağlaşımı ve bütünlüğü bilinçli yönetirken diğerleri yönetmez ve kuruluş genelinde paylaşılan bir sözcük dağarcığı yoktur.
- **Düzey 3, Standartlaştırma:** Paylaşılan bir tasarım sözcük dağarcığı, soyutlamaları çıkarmak için üçün kuralı, bağlaşım ve bütünlük analizi ve takımlara hizalı sınırlı bağlamlar belgelenmiş ve kuruluş genelinde beklenir; bireysel zevke bırakılmak yerine tasarım incelemesinde tutarlı uygulanır.
- **Düzey 4, Yönetme:** Tasarım sağlığı temel çizgilere karşı ölçülür: bağlaşım ve birlikte değişim verileri, değişim başarısızlık oranı ve karşılaştırılabilir özellikleri gerçekleştirme süresi zaman içinde izlenir; böylece soyutlamalar ve sınırlar kanıta dayanarak eklenir, korunur ya da kaldırılır ve aşırı mühendislik ile yanlış soyutlama görüş yerine veriyle yakalanır.
- **Düzey 5, Orkestrasyon:** Tasarım disiplini kuruluş genelinde teslimat ve risk planlamasıyla bütünleşir; ilkeler nüansla ve bilinen başarısızlık biçimleriyle uygulanır; paradigma ve sınır seçimleri bilinçlidir ve sürekli yeniden ele alınır ve kuruluş alan ve kanıt kaydıkça soyutlamaları rutin olarak yeniden düzenler, yeniden kapsamlar ve emekliye ayırır.

## Tartışma fikirleri

- Gelecekteki gereksinime sahip olmadan önce gerekli bir dikişi spekülatif genellikten nasıl ayırırsınız?
- DRY takımınızı en son ne zaman yanlış soyutlamaya götürdü ve bunu nasıl fark ettiniz?
- Sınırlı bağlam sınırları nereye düşmeli ve organizasyon şemasını ne kadar yakından yansıtmalı?
- Sizin bağlamınızda koddan önce ne kadar tasarım olmalı ve kararları nasıl kaydedersiniz?
- Sisteminizin hangi parçaları daha işlevsel ya da veri odaklı bir üslubtan yararlanırdı?
- Tasarım ilkelerinin pragmatik istisnalara direnen dogmaya sertleşmesini nasıl önlersiniz?

## Önemli çıkarımlar

- Önemli olan özellikler bağlaşım ve bütünlüktür; kısaltmalar o amaçlara giden araçlardır.
- Her ilkenin bir başarısızlık biçimi vardır; her birinin ne zaman yanılttığını bilin.
- Erken ya da yanlış bir soyutlama yerine biraz tekrarı tercih edin.
- Karmaşık alanları takım sahipliğiyle hizalamak için DDD ve sınırlı bağlamları kullanın.
- Paradigmaları uyuma göre seçin; büyük sistemler pragmatik olarak karışıktır.
- Gerçekten ihtiyaç duyacağınız değişimler için tasarlayın; hem az hem aşırı tasarımdan kaçının.

## Kaynaklar ve ileri okuma

- Robert C. Martin, *Clean Architecture* and *Agile Software Development, Principles, Patterns, and Practices*
- Eric Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software*
- Vaughn Vernon, *Implementing Domain-Driven Design*
- Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*
- Martin Fowler, *Refactoring: Improving the Design of Existing Code* and *Patterns of Enterprise Application Architecture*
- David L. Parnas, *On the Criteria to Be Used in Decomposing Systems into Modules*
- Sandi Metz, *Practical Object-Oriented Design*
