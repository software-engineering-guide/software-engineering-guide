# 6.3 Üretken yapay zeka ve LLM uygulamaları

## Genel bakış ve motivasyon

[Üretken yapay zeka](https://en.wikipedia.org/wiki/Generative_artificial_intelligence) ve özellikle [büyük dil modelleri](https://en.wikipedia.org/wiki/Large_language_model) (LLM'ler), doğal dil yönergelerinden akıcı metin, kod, özet ve yapılandırılmış veri üretebilir. Bu, onları asistanlar, arama, belge işleme ve otomasyon için güçlü yapı taşları haline getirir. Ama bu güçlü yanlar kendine özgü bir risk profiliyle gelir. LLM'ler olasılıksaldır. Kendinden emin yanlışlar ([halüsinasyonlar](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))) üretebilirler. Onlara nasıl istem verdiğinize duyarlıdırlar. Ve [istem enjeksiyonu](https://en.wikipedia.org/wiki/Prompt_injection) (modelin davranışını ele geçirmek için girdilere gizlice sokulan kötü niyetli yönergeler) gibi yeni saldırı yüzeyleri açarlar. Bu yüzden güvenilir LLM uygulamaları kurmak modelden çok, onun etrafındaki mühendislikle ilgilidir: bağlamı nasıl sağladığınız, yanıtları güvenilir bilgiye nasıl dayandırdığınız, çıktıları nasıl kısıtladığınız ve kaliteyi nasıl değerlendirdiğiniz.

Büyük takımlar için LLM uygulamaları, hem geleneksel yazılımdan hem klasik makine öğreniminden farklı yeni kalıplar gerektirir. Çoğu zaman bir eğitim adımı yoktur. Bunun yerine davranış; istemler, getirilen bağlam, araç tanımları ve koruma bariyerleri (modelin girdilerini ve çıktılarını kısıtlayan çalışma zamanı denetimleri) ile şekillenir. Bu, mühendislik çabasını bağlam yönetimine, erişim kalitesine, orkestrasyona ve değerlendirmeye kaydırır. LLM'leri ölçekte benimseyen kurumsal firmalar ortak kalıplara ihtiyaç duyar; böylece her takım aynı başarısızlık kiplerini zor yoldan yeniden keşfetmez.

Kamu ve düzenlemeye tabi kurumlar ek talepler ile karşı karşıyadır. Bir politika atfı uyduran ya da hassas veri sızdıran bir LLM yalnızca bir hata değildir; hukuki ya da güvenlik olayı olabilir. Bu ortamlar yetkili kaynaklara dayandırmayı, sıkı çıktı doğrulamasını, ağır sonuçlu çıktılar için insan gözetimini ve sisteme ne sorulduğuna ve ne ürettiğine dair net kayıtları gerektirir. Bu bölümdeki teknikler (erişimle artırılmış üretim, koruma bariyerleri ve titiz değerlendirme), LLM'leri yüksek riskli bağlamlarda dağıtılabilecek kadar güvenli kılan şeylerdir. Anthropic'in Claude modelleri, yetkin birçok sağlayıcı arasında önde gelen seçeneklerden biridir; buradaki uygulamalar hangi modeli seçtiğinizden bağımsız olarak geçerlidir.

## Temel ilkeler

- Modeli, ezberlediği şeye güvenmek yerine güvenilir bilgiye dayandırın.
- İstemleri ve bağlamı, harcanıp atılan dizeler değil, mühendislenmiş, sürümlenen yapıtlar olarak ele alın.
- Modelin yanlış olabileceğini ya da manipüle edilebileceğini varsayın; çıktıları doğrulayın ve eylemleri kısıtlayın.
- Hatayı ve saldırı yüzeyini azaltmak için modele yalnızca ihtiyaç duyduğu bağlamı ve araçları verin, fazlasını değil.
- Çevrimdışı test kümeleri, çevrimiçi ölçütler ve insan yargısıyla sürekli değerlendirin.
- Ağır sonuçlu çıktılar için insanı döngüde tutun.
- Modeli, güvenilen bir sistemin içinde güvenilmeyen bir bileşen olarak tasarlayın.

## Öneriler

### İstemleri mühendisleyin ve bağlamı bilinçli yönetin

İstemleri kod gibi ele alın: sürüm denetiminde saklayın, değişiklikleri inceleyin ve bir örnek paketine karşı test edin. Her istemi açıkça yapılandırın: rol ve görev, kısıtlar, biçim gereksinimleri ve işe yaradığı yerlerde örnekler. Bağlam penceresini (modelin aynı anda göz önünde bulundurabileceği sabit metin aralığı) kıt bir kaynak olarak ele alın. En ilgili bilgiyi dahil edin, düşünceli biçimde sıralayın ve gürültüyü ayıklayın, çünkü alakasız ya da aşırı bağlam kaliteyi düşürür ve maliyeti artırır. Çok turlu uygulamalarda konuşma durumunu açıkça yönetin; önemli olanı korurken sınırlar içinde kalmak için geçmişi özetleyin ya da kısaltın. Model değiştiği anda bozulan ayrıntılı numaralar yerine net yönergeleri ve az örnekli örnekleri (isteme eklenen bir avuç çalışılmış gösterim) tercih edin.

### Yanıtları erişimle artırılmış üretimle (RAG) temellendirin

Bilgi yoğun görevlerde güvenilir bir külliyattan ilgili belgeleri getirin ve modele bağlam olarak sunun; ona yalnızca o malzemeden yanıt vermesini ve kaynaklarını belirtmesini söyleyin. RAG, bilgiyi yeniden eğitim olmadan güncel tutar, yanıtları onaylı içerikle sınırlar ve atıf ile doğrulamayı mümkün kılar. Erişim kalitesine yatırım yapın: belgeleri mantıklı biçimde parçalayın, alanınıza uygun [gömmeler](https://en.wikipedia.org/wiki/Word_embedding) (benzer anlamları birbirine yakın yerleştiren sayısal vektör temsilleri) seçin ve getirilen pasajların yanıtı gerçekten içerip içermediğini denetleyin, çünkü yanlış pasaja dayanan akıcı bir yanıt, hiç yanıt olmamasından daha kötüdür. Ve ilgili hiçbir şey çıkmadığında, sistem içerik uydurmak yerine bunu söylesin.

### Ajanları ve araç kullanımını ölçülü kurun

LLM'ler araçları (arama, veritabanları, hesap makineleri, iç API'ler) çağırabilir ve birden çok adımda planlayıp eyleme geçen ajanlar halinde bir araya getirilebilir. Bu gerçek yetenek ekler, ama riski de çoğaltır: her araç, yanlış ya da manipüle edilmiş bir modelin zarar vermesinin bir yolu daha demektir. Araçları kesin şemalarla tanımlayın, her argümanı doğrulayın, en az ayrıcalık uygulayın ve iletişim göndermek ya da para taşımak gibi ağır sonuçlu eylemler için onay ya da insan onayı isteyin. Ajan döngülerini sınırlı, gözlemlenebilir ve kesilebilir tutun. Sınırsız özerkliğe uzanmadan önce sıkı kapsamlı, tek amaçlı araçlarla başlayın.

### Koruma bariyerleri ekleyin ve çıktıları doğrulayın

Modeli savunma katmanlarıyla sarın. Girişte, özellikle güvenilmeyen içerik (web sayfaları, kullanıcı belgeleri) bağlama girdiğinde, istem enjeksiyonunu süzün ve tespit edin. Çıkışta, yapıyı bir şemaya karşı doğrulayın, iddiaları kaynaklarla karşılaştırın, güvensiz ya da uyumsuz içeriği süzün ve doğrulama başarısız olduğunda reddedin ya da yeniden deneyin. Yapılandırılmış çıktılarda, modelin biçimlendirmesine güvenmek yerine ayrıştırın ve doğrulayın. Ham model çıktısının doğrulama olmadan geri döndürülemez eylemleri tetiklemesine asla izin vermeyin. Halüsinasyon azaltmayı, modelin kendi başına yönettiği bir şey olarak değil, temellendirme, atıf, doğrulama ve insan incelemesiyle elde ettiğiniz bir sistem özelliği olarak ele alın.

### Çevrimdışı, çevrimiçi ve insanlarla değerlendirin

Bilinen iyi ya da dereceli puanlanmış çıktılara sahip temsili girdilerden oluşan bir değerlendirme paketi kurun ve her istem ya da model değişikliğinde çalıştırın (çevrimdışı değerlendirme). Üretimde gerçek davranışı görev başarısı, yükseltme oranı ve kullanıcı geri bildirimi gibi ölçütlerle ölçün (çevrimiçi değerlendirme). Öznel kalite için insan incelemecileri ve, dikkatle, model tabanlı puanlamayı kullanın. Değerlendirme, istemleri ve modelleri güvenle değiştirmenize izin veren güvenlik ağıdır. Onsuz kör uçuş yaparsınız.

## Ödünleşimler: artılar ve eksiler

| Seçim | Artılar | Eksiler | En uygun olduğu durum |
|---|---|---|---|
| Saf istem yazımı | Basit, hızlı, değiştirmesi ucuz | Sınırlı temellendirme, halüsinasyon görebilir | Geniş görevler, düşük risk |
| RAG | Güncel, temellendirilmiş, atıf yapılabilir | Erişimi doğru yapmak zordur | Bilgi ağırlıklı, olgusal görevler |
| Araçlı ajanlar | Güçlü, eyleme geçebilir | Daha büyük saldırı yüzeyi, kontrolü daha zor | Koruma bariyerleriyle iyi kapsamlanmış otomasyon |
| Daha büyük, daha güçlü model | Daha iyi kalite ve akıl yürütme | Daha yüksek maliyet ve gecikme | Karmaşık ya da yüksek riskli görevler |
| Daha küçük, daha ucuz model | Hızlı ve ucuz | Zor görevlerde daha zayıf | Yüksek hacim, basit görevler |

Temel gerilim, yetenek ile kontrol ve maliyet arasındadır. Daha fazla özerklik ve daha büyük modeller daha çok değer sunar, ama daha fazla koruma bariyeri, daha fazla değerlendirme ve daha fazla para talep eder. RAG ile temellendirme, erişim mühendisliği pahasına güvenilirliği artırır. Doğru denge risk düzeyine bağlıdır: yüksek riskli uygulamalar, daha pahalıya mal olsa bile temellendirmeye, doğrulamaya ve insan gözetimine yaslanır.

## Takımınızla tartışılacak sorular

1. **Bir LLM özelliği halkın karşısına çıkmadan önce hangi doğruluk ve temellendirme çıtasını aşmalı ve onayı kim veriyor?** Yanlış kaynağı atfeden ya da bir politika uyduran akıcı bir yanıt, hiç yanıt olmamasından daha kötüdür ve kamuda uydurma bir atıf bir hata değil, hukuki bir olaydır. Büyük bir takım için açık bir çıta, her grubun kendi özel eşiğini sezgiyle belirlemesini önler. "Yeterince temellendirilmiş" tanımınızı getirin: her iddianın getirilmiş, doğrulanmış bir kaynağa izlenmesi gerekip gerekmediğini, erişim boş döndüğünde sistemin reddetmesi gerekip gerekmediğini ve düşmanca değerlendirme kümenizin gerçekte neyi kapsadığını. İzlenecek işaret, herhangi birinin şu anda gerileme çalıştırması olmadan bir istem değişikliğini doğrudan kullanıcılara gönderip gönderemediğidir. Riskler hukuki ya da güvenlikle ilgiliyse, yanıt en yüksek riskli çıktıları yayımdan önce gerçek yetkisi olan bir insan incelemecinin önünden geçirmelidir.

2. **LLM özelliklerimizden hangileri gizlice ajan ve her araca en az ayrıcalık ve geri döndürülemez eylemlerde bir insan kapısı verildi mi?** Modelin araç çağırmasına ya da birden çok adımda eyleme geçmesine izin veren her özellik ajan bölgesine geçmiştir ve her araç, yanlış ya da manipüle edilmiş bir modelin zarar vermesinin bir yolu daha demektir. LLM'leri iç API'lere bağlayan kurumsal firmalar için bu soru, "basit asistan" etiketinin sakladığı riski ortaya çıkarır. Modelin çağırabileceği her aracın envanterini, argüman doğrulamasını, ayrıcalık kapsamını ve hangi eylemlerin (iletişim göndermek, para taşımak, kayıtları değiştirmek) onay gerektirdiğini getirin. Ajan döngülerinin sınırlı, gözlemlenebilir ve kesilebilir olup olmadığını tartışın. Yanıt, şu anda onsuz ulaşılabilir olan ağır sonuçlu ya da geri döndürülemez bir eylemin olduğu her yerde kapsamları daraltmalı ve insan onay kapıları eklemelidir.

3. **Yanlış pasaja dayanan kendinden emin bir yanıt iyi göründüğüne göre, erişim kalitemizin düştüğünü bir gün içinde nasıl anlarız?** RAG, yanıtları ancak erişim gerçekten yanıtı içeren pasajı ortaya çıkardığında güvenilir kılar ve erişim; belgeler değiştikçe, parçalar bayatladıkça ya da gömmeler alanınızdan kaydıkça sessizce çürür. Model kötü bağlam üzerinde hâlâ akıcı yazdığı için kullanıcılar, güven zaten kaybolana kadar şikayet etmeyebilir. Mevcut erişim gecikmesi ve geri çağırma ölçülerinizi, getirilen pasajların yanıtı gerçekten içerip içermediğini nasıl denetlediğinizi ve dizin tazeliğinin belge değişikliklerine nasıl ayak uydurduğunu getirin. Yüksek riskli ya da kamusal dağıtımlar için, kötü bir yanıtı kötü pasajına izleyebilmek adına getirilen kaynakların denetim için günlüğe kaydedilmesini tartışın. Hiç erişim değerlendirmeniz yoksa, inançla temellendiriyorsunuz demektir.

4. **İstemleri, bağlamı ve değerlendirme kümelerini sürümlenen, incelenen yapıtlar olarak mı görüyoruz, yoksa not defterlerine ve sohbet günlüklerine dağılmış dizeler olarak mı?** İstemler takımlar arasında sürümsüz ve yinelenmiş biçimde yayıldığında, bir yerdeki düzeltme diğerlerine asla ulaşmaz ve geçen çeyrekte sisteme ne yapması söylendiğini kimse yeniden üretemez. Büyük bir takım için ortak bir istem kayıt defteri ve her değişiklikte çalışan bir gerileme paketi, iki takım ötedeki bir özelliği sessizce bozmadan bir modeli değiştirmenizi ya da bir yönergeyi düzenlemenizi sağlayan şeylerdir. Karşı çekim hızdır: mühendisler bir istemi yapıştırıp yayına aldıklarında en hızlı yinelerler; bu yüzden hızlı deneyler ile kullanıcılara dokunan her şey arasındaki çizginin nerede durduğunu kararlaştırın. İstemlerinizin bugün gerçekte nerede yaşadığını, bir değerlendirme kümesinin değişiklikleri kapılayıp kapılamadığını ve erişim külliyatını isteme paralel olarak nasıl sürümlediğinizi getirin. Kurumsal ve kamu ortamlarında denetim gereksinimini ekleyin: aylar sonra belirli bir çıktıyı tam olarak hangi istemin ve hangi kaynakların ürettiğini göstermeniz gerekebilir ve yeniden kurgulayamadığınız bir istem, savunamayacağınız bir kayıttır.

5. **Hacim büyüdükçe kaliteyi sessizce düşürmeden çıkarım maliyetini nasıl kontrol edeceğiz ve model seçimi kararı kimde?** LLM özellikleri için TSM, çağrı başına çıkarım maliyetinin baskın olduğu bir kalemdir ve bir pilotta önemsiz görünen maliyetler üretim ölçeğinde hızla birikir; bu da takımları sessizce daha zayıf bir modele geçip kimsenin kalite düşüşünü fark etmemesini ummaya ayartır. Büyük bir kurumda, her takımın model ve maliyet sınırlarını sezgiyle seçmesi hem sürpriz faturalar hem tutarsız kalite üretir. Gerçek ödünleşim, yetenek ile maliyet ve gecikme arasındadır: daha büyük bir model zor görevlerde daha iyi akıl yürütür, daha küçük olan basit görevlerde daha ucuz ve hızlıdır; önbellekleme, yönlendirme ve erişim kapsamı da sayıyı oynatır. Çözülen görev başına maliyeti, değerlendirme kümenizde model katmanına göre kaliteyi ve istem ya da bağlam şişkinliğinin token harcamasını nerede şişirdiğini getirin. Kurumsal ve kamu bütçelemesinde model seçimini ve harcama tavanını kimin onayladığını adlandırın, çünkü kimsenin sahip olmadığı bir maliyet kalemi, trafik üç katına çıktığında kimsenin kontrol etmediği bir kalemdir.

6. **Modele hangi hassas veri ulaşabilir, bu veri nereye gidiyor ve sınırlar içinde kaldığını kanıtlayabilir miyiz?** Her istem, getirilen belge ve araç sonucu, modele ve barındırılan bir sağlayıcıyla birlikte çevrenizin dışına kişisel ya da gizli veri taşıyabilir ve buradaki bir sızıntı, bir kusur kaydı değil, hukuki ya da güvenlik olayıdır. İç sistemlere LLM bağlayan büyük bir takım için risk tesisatta saklanır: belirli bir kullanıcının asla görmemesi gereken kayıtları içeren bir erişim külliyatı ya da ham girdileri yakalayan günlükler. Gerilim, yetenek ile maruz kalma arasındadır, çünkü gizleme ve sıkı kapsamlama, kurmaya çalıştığınız özelliği körleştirebilir. Bağlama nelerin girdiğine dair bir veri akışı haritasını, sağlayıcının saklama ve eğitim şartlarını ve hassas alanları nasıl gizlediğinizi, kapsamladığınızı ve günlüğe kaydettiğinizi getirin. Düzenlemeye tabi ve kamusal ortamlarda bunu veri ikamet kurallarına, kayıt saklama görevlerine ve bir satıcının verilerinizi nasıl kullanabileceğine dair sözleşmesel sınırlara bağlayın, çünkü kanıtlayamadığınız gözetim, sahip olmadığınız gözetimdir.

## Sektör merceği

**Girişim.** Çekirdek değerinize dokunan dar bir LLM özelliğini, kendi içeriğiniz üzerinde erişimle barındırılan bir model üzerine kurulu olarak yayına alın ve sağlayıcıları değiştirebilmek için istemleri ince bir arayüzün arkasında git'te tutun. Her değişiklikten önce gerçek sorulardan oluşan küçük bir değerlendirme dosyası çalıştırın, istem enjeksiyonunu körleştirmek için yapıştırılan kullanıcı metnini süzün ve aylık harcamayı sıkı biçimde sınırlayın. Ajanlara ve kendi sunucunuzda barındırmaya direnin: gözetleyemeyeceğiniz sınırsız bir araç çağırma döngüsü bir gösterim değil, bir yüktür.

**Küçük işletme.** Büyük olasılıkla bir ML uzmanınız yok; bu yüzden bir inşa için kadro kurmak yerine zaten kullandığınız araçlara gömülü LLM özelliklerini satın alın. Riski sade bir soru olarak çerçeveleyin: kendinden emin yanlış bir yanıt size nerede bir müşteriye mal olur ve çıktı dışarı çıkmadan önce kim denetliyor. Kaynaklarını gösteren, insanı döngüde tutmanıza izin veren ve yapay zekayı yanlış davrandığında kapatmayı kolaylaştıran satıcıları tercih edin.

**Kurumsal.** Sorun, birçok takım arasındaki ölçektir: RAG, koruma bariyerleri ve araç şemaları için ortak kalıplar yayımlayın; ayrıca her grup aynı başarısızlık kiplerini yeniden keşfetmeyi bıraksın diye ortak bir değerlendirme koşum takımı ve istem kayıt defteri sağlayın. Çıkarım maliyetini ve insan incelemesini açıkça bütçelendirin, modeller değiştirilebilir kalsın diye arayüz katmanını standartlaştırın ve ajanları en az ayrıcalık, sınırlı döngüler ve denetim günlüğüyle merkezi olarak yönetin. LLM özelliklerini bir pilot dağınıklığı olarak değil, ölçütleri ve sonlandırma ölçütleri olan bir portföy olarak yönetin.

**Kamu.** Şeffaflık, tedarik kuralları ve hesap verebilirlik her seçimi şekillendirir. Atıflarla onaylı kaynaklara sıkıca dayandırın, erişim boş döndüğünde reddedin ve modelin atıf yapamayacağı hukuku ifade etmesini yasaklayın. Ağır sonuçlu çıktıları hesap verebilir bir yetkilinin incelemesinde tutun, denetim için girdileri ve getirilen kaynakları günlüğe kaydedin, her sürümden önce düşmanca bir değerlendirme kümesi çalıştırın ve sözleşmede model sınırlamalarının ve veri işleme şartlarının açıklanmasını talep edin.

## Örnekler

**Girişim.** Üç kişilik bir geliştirici araçları girişimi, kullanıcılar temel sorular için e-posta atmayı bıraksın diye kendi belgeleri üzerine bir sohbet yardımcısı ekledi. Her yanıt belirli bir belge sayfasına atıf yapsın diye RAG kullandı, erişim boş döndüğünde modele "Emin değilim, kime sorabileceğiniz şu" demesini söyledi ve istemlerini git'te tuttu. Her değişiklikten önce gerilemeleri yakalamak için istemleri gerçek kullanıcı sorularından oluşan küçük bir dosyaya karşı çalıştırdı ve istem enjeksiyonunu körleştirmek için kullanıcının yapıştırdığı metni süzdü. Yardımcı yaygın soruları ele aldı ve gerisini sessizce kurucuların ortak gelen kutusuna aktardı.

**Kurumsal.** Bir yazılım şirketi, ürün belgeleri üzerine bir iç destek asistanı kurdu. Yanıtlar belirli belge sayfalarına atıf yapsın diye [RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) kullandı, erişim başarısız olduğunda modele "bilmiyorum" demesini söyledi ve atıf yapılan her kaynağın gerçekten var olduğunu doğruladı. İstemler sürüm denetimindeydi ve her değişiklikte gerçek destek sorularından oluşan bir pakete karşı test ediliyordu. Asistan rutin bildirimleri saptırdı ve düşük güvenli her şeyi insan temsilcilere yükseltti; çevrimiçi ölçütler çözüm ve düzeltme oranlarını izledi.

**Kamu.** Bir kamu kurumu, personelin vatandaş sorularına yanıt taslağı hazırlamasına yardım etmek için bir LLM asistanı dağıttı. Temellendirme sıkıydı: model yanıtları yalnızca atıflarla onaylı rehberlikten oluşturabiliyordu ve getirilen kaynaklarda bulunmayan politikayı ifade etmesi yasaktı. Hesap verebilir bir yetkili, dışarı çıkmadan önce her taslağı inceledi. Girdi süzme, vatandaşların gönderdiği belgelerden gelen istem enjeksiyonuna karşı koruyordu, çıktılar denetim için günlüğe kaydediliyordu ve her sürümden önce düşmanca ve uç durum sorgularından oluşan bir değerlendirme kümesi çalıştırılarak sistemin hukuk meselelerinde spekülasyondan kaçındığı doğrulanıyordu.

## İş gerekçesi: motivasyonlar, YG ve TSM

LLM uygulamaları, dil ağırlıklı işi otomatikleştirerek YG (yatırım getirisi) sağlar: soruları yanıtlamak, belgeleri özetlemek, içerik taslağı hazırlamak ve yapılandırılmamış metinden yapı çıkarmak. Değer; saptırılan bildirimler, daha hızlı taslak hazırlama, daha az elle inceleme ve yeni self servis yetkinlikleri olarak ortaya çıkar. Çoğu zaman bir eğitim adımı olmadığından ilk değere ulaşma süresi kısadır ve bu büyük bir çekim noktasıdır.

TSM (toplam sahip olma maliyeti) ise sürekli çıkarım maliyeti, erişim altyapısı, değerlendirme hatları, koruma bariyeri sistemleri ve insan incelemesi tarafından domine edilir. Çağrı başına maliyetler ölçekte hızla birikir ve izlenmeyen bir uygulama güvensiz ya da pahalı davranışa kayabilir. Benimsememenin maliyeti, hizmet kalitesinde ve personel verimliliğinde geri kalmaktır. Dikkatsizce benimsemenin maliyeti, kamuya açık bir halüsinasyon olayı ya da bir veri sızıntısıdır. Gerekçeyi liderliğe somut bir verimlilik hedefini somut bir güvenlik ve değerlendirme planıyla eşleştirerek ve değeri kalıcı tutan koruma bariyerleri ile insan gözetimini bütçeleyerek sunun.

## Anti-kalıplar ve tuzaklar

- **Akıcı çıktıya güvenmek.** Kendinden emin, iyi yazılmış metni doğru metinle karıştırmak.
- **Erişim değerlendirmesi olmayan RAG.** Erişimin işlediğini varsaymak ve doğru pasajları ortaya çıkarıp çıkarmadığını hiç denetlememek.
- **İstem enjeksiyonu körlüğü.** Güvenilmeyen içeriği savunma olmadan istemlere beslemek.
- **Sınırsız ajanlar.** Ajanların sınırsız ya da insan onayı olmadan ağır sonuçlu eylemler yapmasına izin vermek.
- **Değerlendirme koşum takımı yok.** İstemleri ve modelleri gerileme testi olmadan, sezgiyle değiştirmek.
- **İstem dağınıklığı.** İstemlerin takımlar arasında dağınık, sürümsüz ve yinelenmiş olması.
- **Aşırı otomasyon.** İnsanları, hukuki ya da güvenlik ağırlığı taşıyan kararlardan çıkarmak.

## Olgunluk modeli

1. **Düzey 1, Başlangıç.** İzole projelerde geçici istem yazımı; temellendirme, koruma bariyeri ya da değerlendirme yok; istemler birinin yapıştırdığı yerde yaşıyor ve halüsinasyonlar üretimde keşfediliyor.
2. **Düzey 2, Geliştirme.** Bazı takımlar RAG ve istem sürümleme, temel çıktı doğrulaması ve küçük bir elle değerlendirme kümesi ekliyor, ama uygulamalar takımdan takıma değişiyor ve ortak beklentiye değil, bireysel savunuculara dayanıyor.
3. **Düzey 3, Standartlaştırma.** RAG, koruma bariyerleri, araç şemaları ve istem sürümleme için belgelenmiş kalıplar kurum genelinde uygulanıyor; her istem ya da model değişikliğinde otomatik çevrimdışı değerlendirme çalışıyor; yüksek riskli akışlar çevrimiçi ölçütler ve insan incelemesi taşıyor.
4. **Düzey 4, Yönetme.** Portföy referans düzeylere karşı ölçülüyor: erişim geri çağırması, halüsinasyon ve ret oranları, enjeksiyon savunma kapsamı, çağrı başına maliyet ve gecikme, yükseltme ve düzeltme oranları panolarda izleniyor; sürüm kapıları ve sonlandırma ölçütleri görüşe değil kanıta dayalı olarak devreye giriyor ve bir ölçütü yanlış yöne oynatan her değişikliği bir gerileme çalıştırması engelliyor.
5. **Düzey 5, Orkestrasyon.** Sürekli çevrimdışı ve çevrimiçi değerlendirme iş sonuçlarına bağlı; enjeksiyon savunmaları, ajanlar ve temellendirme yönetiliyor ve gözlemlenebilir; kurum LLM özelliklerini rutin biçimde emekliye ayırıyor, yeniden ayarlıyor ve yeniden kapsamlandırıyor ve kalite, maliyet ve risk değiştikçe modelleri değiştiriyor.

## Tartışma fikirleri

- Hangi çıktıların kullanımdan önce insan incelemesi gerektirdiğine nasıl karar verirsiniz?
- Bir yanıt kullanıcılara gösterilmeden önce "yeterince temellendirilmiş" standardınız nedir?
- Güvenilmeyen içeriğin bağlama girmesi gerektiğinde istem enjeksiyonuna karşı nasıl savunma yaparsınız?
- Bir ajan, daha basit tek çağrılı bir tasarıma kıyasla eklediği riske ne zaman değer?
- Model tabanlı puanlamaya aşırı güvenmeden öznel kaliteyi ölçekte nasıl değerlendirirsiniz?
- İstemleri birçok takım arasında nasıl bakımı yapılabilir ve tutarlı tutarsınız?

## Önemli çıkarımlar

- Güvenilirlik, modelin etrafındaki mühendislikten gelir: bağlam, temellendirme, koruma bariyerleri ve değerlendirme.
- RAG yanıtları güvenilir kaynaklara dayandırır ve atıf ile doğrulamayı mümkün kılar.
- Modeli güvenilmeyen bir bileşen olarak ele alın; çıktıları doğrulayın ve araç kullanımını kısıtlayın.
- Ajanlara en az ayrıcalık, sınırlı döngüler ve ağır sonuçlu eylemler için insan onayı verin.
- Çevrimdışı, çevrimiçi ve insanlarla sürekli değerlendirin; değişikliği güvenli kılan budur.

## Kaynaklar ve ileri okuma

- Patrick Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*.
- Jason Wei et al., *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Anthropic, *Building Effective Agents* (engineering guidance).
- Louis-François Bouchard and Louie Peters, *Building LLMs for Production*.
