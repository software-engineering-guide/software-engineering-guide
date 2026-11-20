# 5.6 Ön yüz mühendisliği

## Genel bakış ve motivasyon

Ön yüz mühendisliği, yazılımın istemciye dönük katmanını inşa etme disiplinidir: tarayıcıda ya da cihazda çalışan, tasarımları, içeriği ve veriyi çalışan bir arayüze dönüştüren kod. Çerçeve ve mimari seçimlerini, işleme stratejisini, durum yönetimini, performansı ve gerçek dünyadaki tarayıcıların, cihazların ve ağ koşullarının muazzam çeşitliliği karşısında dayanıklılığı kapsar. Ön yüz, tüm yukarı akış işinin (UX, tasarım, içerik, erişilebilirlik, uluslararasılaştırma) ya kullanıcıya başarıyla ulaştığı ya da dağılıp gittiği yerdir.

Büyük takımlar için ön yüz benzersiz biçimde zordur, çünkü kurumun denetlemediği bir ortama açıktır. Kullanıcıların tarayıcıları, cihazları, bağlantıları ve ayarları çılgınca değişir ve platform (web) sürekli evrilir. Ölçekte mimari seçimler birikir. Bugün seçilen bir çerçeve yıllarca işe alımı, performansı ve sürdürülebilirliği kısıtlar ve paket boyutu ile işleme hakkındaki binlerce küçük karar, kullanıcıların gerçekte aldığı deneyime dönüşür. Birçok bağımsız takımın yavaş, tutarsız ve kırılgan bir bütün üretmesini önleyen, ortak standartlar, bileşen kitaplıkları, performans bütçeleri ve mimari kalıplardır.

Kurumsal ve kamu açısından ilgisi çok keskindir. Kurumlar, çerçevenin uzun ömürlülüğünün ve sürdürülebilirliğinin yeniliğe tercih edildiği ve birçok takımın birlikte çalışması gereken uzun ömürlü uygulamalar sürdürür. Hükümetler, eski cihazlardaki, yavaş ya da kotalı bağlantılardaki ve yardımcı teknolojilerdeki insanlar dahil tüm kamuya hizmet verir. Bu da performansı, [aşamalı geliştirmeyi](https://en.wikipedia.org/wiki/Progressive_enhancement) ve dayanıklılığı isteğe bağlı bir cila değil, herkes için çalışan bir hizmet ile en az avantajlıyı dışlayan bir hizmet arasındaki fark yapar. Yalnızca en yeni telefonda ve hızlı bağlantıda çalışan bir kamu hizmeti, görevinde başarısız olur.

## Temel ilkeler

- Ön yüz denetlemediğiniz bir ortamda çalışır; değişkenlik ve başarısızlık için tasarlayın.
- Uzun ömürlü sistemler için sıkıcı, dayanıklı teknolojiyi seçin; sürdürülebilirlik ve işe alım için en iyileyin.
- Performans bir özelliktir ve birçok kullanıcı için erişimin ön koşuludur.
- Aşamalı geliştirme: önce çalışan bir çekirdek deneyim sunun, sonra geliştirmeleri katmanlayın.
- Daha az kod gönderin; en hızlı ve en güvenilir kod, göndermediğiniz koddur.
- İşleme stratejisini modaya değil, içerik türüne ve kullanıcı ihtiyacına uydurun.
- Dayanıklılık: işler ters gittiğinde arayüz bozulmak yerine zarifçe işlev kaybetmelidir.
- Standartlar ve platform özellikleri çerçevelerden uzun yaşar; platforma yaslanın.

## Öneriler

### Çerçeveleri heyecana değil, uzun ömürlülüğe ve uyuma göre seçin

Ön yüz teknolojisini, gündemde olana göre değil, soruna, takıma, bakım ufkuna ve işe alım piyasasına göre seçin. Uzun ömürlü kurumsal ve kamu sistemleri için olgun, iyi desteklenen, geniş yetenek havuzu, kararlı sürüm uygulamaları ve net yükseltme yolları olan teknolojileri tercih edin. Çerçeve kargaşasının toplam maliyetini tartın: yeniden yazımlar pahalı ve risklidir. Yatırımınız çerçeve değişimlerinden sağ çıksın diye [web standartlarına](https://en.wikipedia.org/wiki/Web_standards) yaslanan yaklaşımları tercih edin ve uygulama tek bir kitaplığın yaşam döngüsüne rehin düşmesin diye çerçeveye özgü kodu sınırlar ardında yalıtın.

### İşleme stratejisini ihtiyaca uydurun

Başlıca işleme stratejilerinin her biri farklı içeriğe uyar. Sunucu tarafı işleme (SSR) hızlı ilk boyama ve iyi SEO ([arama motoru optimizasyonu](https://en.wikipedia.org/wiki/Search_engine_optimization)) üretir ve istemci JavaScript'i olmadan çalışır; içerik ağırlıklı ve kamuya dönük sayfalara uygundur. [Statik site üretimi](https://en.wikipedia.org/wiki/Static_site_generator) (SSG) azami hız ve önbelleklenebilirlik için derleme anında önceden işler; seyrek değişen içerik için idealdir. İstemci tarafı işleme (CSR), kimlik doğrulamanın ardındaki son derece etkileşimli, uygulama benzeri deneyimlere uyar. Akış ve aşamalı hidrasyon, kullanıcılar içeriği daha erken görüp kullansın diye sayfayı artımlı olarak gönderir ve etkinleştirir. Birçok büyük sistem, tek bir küresel seçim yapmak yerine bunları rota başına harmanlar. Durumu bilinçli yönetin: sunucu durumunu, URL durumunu ve yerel arayüz durumunu ayrı tutun ve her şeyi tek bir ağır genel depoda toplamaktan kaçının.

### Performansı bütçelenmiş, ölçülen bir disiplin olarak ele alın

Performans bütçeleri (paket boyutu, istek sayısı ve temel ölçütler üzerinde açık sınırlar) benimseyin ve gerilemeler derlemeyi başarısız kılsın diye bunları CI'da zorlayın. Core Web Vitals'ı (yükleme, etkileşim ve görsel kararlılık) yalnızca hızlı makinelerdeki laboratuvar testleriyle değil, gerçek cihazlardan ve ağlardan gerçek kullanıcı izlemeyle takip edin. JavaScript'i agresifçe azaltın: kullanıcılar yalnızca belirli bir görünümün ihtiyaç duyduğunu indirsin diye kodu bölün ve [tembel yükleyin](https://en.wikipedia.org/wiki/Lazy_loading), kritik olmayan işi erteleyin ve ağır kitaplıklar yerine platform yeteneklerini tercih edin. Görselleri ve yazı tiplerini en iyileyin, etkili önbellekleyin ve temsilî düşük uç cihazlarda ve yavaş bağlantılarda ölçün.

### Aşamalı geliştirme ve dayanıklılıkla inşa edin

Anlamsal HTML ve en az ya da hiç JavaScript ile çalışan bir tabandan başlayın, sonra yetenekli istemciler için geliştirin. Bu, betikler yüklenemediğinde, bir cihaz eski olduğunda ya da bir ağ güvenilmez olduğunda, uç durum değil yaygın bir gerçeklik, çekirdek görevin mümkün kalmasını sağlar. Hataları zarifçe ele alın: boş ekranlar ya da sonsuz dönen göstergeler yerine yükleme, boş, hata ve çevrimdışı koşulları için yararlı durumlar gösterin. İnsanların bel bağladığı hizmetlerde, uygulama aralıklı bağlantıda da kullanılabilir kalsın ve bağlantı döndüğünde senkronlasın diye çevrimdışı öncelikli teknikleri düşünün.

### Tarayıcılar, cihazlar ve yardımcı teknolojiler arası uyumluluğu sağlayın

Kullanıcılarınızın gerçekte sahip olduğu tarayıcılar, cihazlar ve yardımcı teknolojiler üzerinde, takımın kendi makineleri yerine gerçek analitiğe dayanarak test edin. En yeni platform özelliklerinin her yerde mevcut olduğunu varsaymak yerine aşamalı geliştirme ve özellik algılama kullanın. Tek bir kod tabanı telefonlardan masaüstlerine hizmet etsin diye [duyarlı](https://en.wikipedia.org/wiki/Responsive_web_design) inşa edin (tasarım sistemi bölümüne bakın). Erişilebilirliği ve uluslararasılaştırmayı sonraki geçişler olarak değil, en baştan ön yüz mimarisine bütünleştirin.

### Ön yüzü ortak altyapı olarak yönetin

Takımlar tutarlı ve üretken olsun diye ortak bileşen kitaplıkları, lint, biçimlendirme ve derleme araçları sağlayın. Mimari yönergeler (uygulamaların nasıl yapılandırılacağı, durumun nasıl yönetileceği ve paketlerin nasıl bölüneceği) ve CI'da zorlanan performans bütçeleri belirleyin. Çok büyük ön yüzler için takımların bağımsız dağıtım yapmasına izin veren modüler ya da mikro ön yüz mimarilerini düşünün, ancak eklenen karmaşıklığı ve performans maliyetini dikkatle tartın; bunlar bedava değildir.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| Popüler, olgun çerçeve | Geniş yetenek havuzu, kararlı, destekli | Miras yükü taşıyabilir; en yeni özellikleri benimsemede daha yavaş |
| En yeni çerçeve | Modern özellikler, performans kazanımları | Kargaşa riski, küçük yetenek havuzu, belirsiz uzun ömür |
| SSR / SSG | Hızlı ilk boyama, SEO, JS olmadan çalışır | Sunucu ya da derleme karmaşıklığı, önbellekleme zorlukları |
| CSR (SPA) | Zengin etkileşim, uygulama hissi | Yavaş ilk yükleme, JS'e bağımlı, SEO ve dayanıklılık maliyeti |
| Ağır istemci JavaScript'i | Zengin özellikler | Düşük uç cihazlarda zayıf performans, kırılgan |
| Aşamalı geliştirme | Dayanıklı, kapsayıcı, her yerde çalışır | Çalışan bir taban tanımlamak için daha çok tasarım emeği |
| Mikro ön yüzler | Bağımsız takım dağıtımları, ölçek | Karmaşıklık, çoğaltılmış bağımlılıklar, performans yükü |

Yinelenen ödünleşim, zenginlik ve geliştirici kolaylığı ile erişim, performans ve dayanıklılık arasındadır. Ağır istemci tarafı yaklaşımlar hızlı makinelerde inşa etmesi ve gösterilmesi keyiflidir, ancak zayıf cihazlardaki ve ağlardaki kullanıcıları dışlar. Kurumsal ve özellikle kamu kitleleri için dengeyi performansa, aşamalı geliştirmeye ve dayanıklılığa doğru yatırın, çünkü kullanıcıları dışlamanın maliyeti yüksektir ve çoğu zaman pazarlık konusu değildir.

## Takımınızla tartışılacak sorular

1. **Uygulama tek bir kitaplığın yaşam döngüsüne rehin düşmesin diye çerçeveye özgü kodu nasıl yalıtıyoruz?** Uzun ömürlü kurumsal ve kamu sistemleri için çerçeve kargaşası, kaçınılabilir en büyük harcamadır: yeniden yazım pahalı ve risklidir ve bugünün gözde kitaplığı yıllarca işe alımı ve bakımı kısıtlar. Web standartlarına yaslanmak ve çerçeveye özgü kodu net sınırların ardına koymak, iş mantığınızın ve içeriğinizin bir sonraki çerçeve değişiminden sağ çıkması demektir. Bu dikişlerin nerede olduğuna ve yeni bir mühendisin platform kodunu çerçeve kodundan ayırt edip edemeyeceğine karar verin. Son çerçeve geçişinizin neye mal olduğunun ya da yaklaşan geçişin neye mal olacağının bir tahminini getirin. Çekirdek mantığınız tek bir kitaplığın API'lerine kaynaklanmışsa, çerçeve seçimini savunmadan önce o bağlaşımı fiyatlandırın.

2. **İşleme stratejisini rota başına mı eşleştiriyoruz, yoksa tüm ürüne tek bir strateji mi dayatıyoruz?** Sunucu tarafı işleme, kamuya açık içerik için hızlı ilk boyama sağlar ve istemci JavaScript'i olmadan çalışır; statik üretim seyrek değişen sayfalar için hızı azamiye çıkarır ve istemci işleme, oturum açmanın ardındaki etkileşimli, uygulama benzeri yüzeylere uyar. Birini küresel olarak dayatmak ya kamuya açık sayfaları ağır JavaScript ile yavaşlatır ya da basit bir içerik sayfasını gereğinden fazla mühendislikle donatır. Bu, kamu için bir erişim sorusudur: büyük bir paket yüklendikten sonra çalışan bir hizmet, eski cihazlardaki ve yavaş bağlantılardaki kullanıcıları dışlar. Temel rotalarınızı getirin ve her birini bugün gerçekte kullandığı stratejiyle etiketleyin. Kamuya dönük bir sayfa içeriğini göstermek için JavaScript'e ihtiyaç duyuyorsa, bunun bilinçli bir tercih mi yoksa kaza mı olduğuna karar verin.

3. **Durum yönetimimiz ne kadar disiplinli ve her şeyi tek bir ağır genel depoda mı topluyoruz?** Sunucu durumunu, URL durumunu ve yerel arayüz durumunu ayrı tutmak, büyük ön yüzleri yavaş ve kırılgan yapan bağlaşımı ve yeniden işleme fırtınalarını önler; yine de cazip varsayılan her şeyi tek bir genel depoya yığmaktır. Bu, tek bir ortak depoya dokunan çok sayıda takımın gizli bağımlılıklar ve öngörülemez performans yarattığı ölçekte birikir. Her tür durumun nereye ait olduğu ve genel depoya neyin ait olmadığı konusunda anlaşın. Gerektiğinden çok yeniden işlenen bir bileşen getirin ve nedenini izleyin. Cevap şişkin bir merkezî depoysa, bağlaşım katılaşmadan sınırlara karar verin.

4. **Performans bütçelerimiz neler, CI'da derlemeyi başarısız kılıyorlar mı ve kullanıcılarımızın gerçekte sahip olduğu cihazlarda mı ölçülüyorlar?** Kimsenin uygulamadığı bir bütçe bir temennidir ve yalnızca takımın hızlı dizüstü bilgisayarlarında ölçülen bir bütçe, var olmayan bir kullanıcıyı tarif eder. Büyük bir kurum için bütçeler, düzinelerce takım ortak bir yüzeye özellik eklerken paket boyutunu ve Core Web Vitals'ı denetimde tutan tek mekanizmadır, çünkü hiçbir tek inceleyici her gerilemeyi gözle yakalayamaz. Karşıt baskı teslimat hızıdır: birkaç kilobayt yüzünden sert bir derleme başarısızlığı, önlediği terk edilmeyi fiyatlandırana kadar engelleyici hissettirir. Mevcut bütçelerinizi, düşük uç cihazlardan ve yavaş bağlantılardan gerçek kullanıcı izleme verilerini ve bir gerilemenin sızdığı sürümlerin listesini getirin. Eski telefonlardaki ve kotalı verideki insanlar dahil tüm kamuya hizmet etme görevinin olduğu kamuda, bütçeyi medyana değil kullanıcılarınızın en yavaş onda birine bağlayın ve CI kapısını pazarlıksız yapın.

5. **Hizmetlerimizin hangileri istemci JavaScript'i olmadan çalışmaya devam etmeli ve bu yolu gerçekten test ettik mi?** Aşamalı geliştirmeyi iddia etmek kolay, sessizce bozmak da kolaydır, çünkü geliştirilmiş yol geliştiricilerin her gün kullandığı yoldur, taban ise sınanmadan çürür. Bunu bilinçli kararlaştırmak ölçekte önemlidir, çünkü tek bir platforma gönderen birçok takım, ortak bir standart aksini söylemedikçe betiklerin her zaman yükleneceğini varsayar ve tek bir sert bağımlılık, paketi yüklenemeyen herkes için çekirdek görevi bozabilir. Ödünleşim gerçektir: JavaScript'siz çalışan bir taban tasarım emeği gerektirir ve etkileşimi nasıl inşa ettiğinizi kısıtlar. Kritik kullanıcı yolculuklarınızı, her birini betikler devre dışı ya da başarısız hâlde yükleyen bir testi ve betiklerin sahada gerçekte ne sıklıkla yüklenemediğine dair kanıtı getirin. Bir kamu hizmetinde, tek bir betik zaman aşımına uğradığında çöken bir yardım ya da vergi formu, aşağı çekilmiş bir deneyim değil, yasal bir yükümlülüğü tamamlayamayan bir yurttaştır; bu yüzden tabanı bir incelik değil, bir uyum gerekliliği olarak ele alın.

6. **Mikro ön yüzler karmaşıklıklarının bedelini ne zaman gerçekten öder ve bir takım onlara uzanmadan önce kim karar verir?** Bağımsız takım dağıtımları çekicidir, ancak mikro ön yüzler dağıtık sistem karmaşıklığı, çoğaltılmış bağımlılıklar ve kullanıcıların daha yavaş yüklemelerle ödediği bir performans vergisi taşır. Ortak bir karar noktası olmadan, hırslı takımlar bunları ölçek maliyeti haklı çıkarmadan çok önce örgütsel kolaylık için benimser ve ürünün tamamı yükü devralır. Karşıt değerlendirme özerkliktir: tek bir ortak kod tabanında yayın yapan takımlar birbirini engelleyebilir ve gerçek ölçekte bu bağlaşım kendi başına pahalı bir sorundur. Yüzeye dokunan takım sayısını, bugün gerçekte yaşadığınız dağıtım çekişmesini ve bir bölünmenin getireceği yük çoğaltmasının ölçülmüş bir tahminini getirin. Mimari kararların birçok takımı yıllarca bağladığı ve denetimden ve devir teslimden sağ çıkması gereken kurumsal ve kamu platformlarında, her takımın tek başına karar vermesine izin vermek yerine açık, belgelenmiş bir eşik ve geçişi onaylayan bir sahip isteyin.

## Sektör merceği

**Girişim.** Her kayıt önemliyken hız ve erişim birlikte önemlidir, bu yüzden kamuya açık sayfalar için ağır tek sayfa uygulamasına direnin. Pazarlama ve kayıt akışınızı, ilk müşterilerinizin kullandığı orta sınıf telefonlarda ve dalgalı veride hızlı yüklensin diye sunucuda işleyin ve istemci tarafı etkileşimi oturum açmanın ardındaki uygulamaya saklayın. Dikkatsiz bir bağımlılığın sayfayı sessizce şişirememesi için CI'da tek bir basit paket boyutu bütçesi koyun ve işe aldıkça küçük kod tabanı sürdürülebilir kalsın diye web standartlarına yaslanın.

**Küçük işletme.** Özel bir ön yüz uzmanı olmadan ve dar bir bütçeyle, özel yapım herhangi bir şey yerine iyi desteklenen ana akım bir çerçeveyi ya da barındırılan bir site oluşturucuyu tercih edin; böylece geniş bir yetenek havuzundan işe alır ve bakımı kadrolamak yerine satın alırsınız. Seçimi dayanıklılık olarak çerçeveleyin: en ucuz seçenek, iki yıl içinde yeniden yazmaya zorlanmayacağınız seçenektir. Hızlı, mobil dostu sayfalar ve kutudan çıktığı gibi erişilebilir işaretleme konusunda ısrar edin; yavaş ya da bozuk bir ödeme, kaybetmeyi göze alamayacağınız müşterilere mal olur.

**Kurumsal.** Sorun birçok takım arasında tutarlılıktır: ortak bir bileşen kitaplığı, üzerinde anlaşılmış mimari kalıplar, lint ve derleme araçları ve hiçbir takımın bütünü sessizce geriletememesi için CI'da zorlanan performans bütçeleri. Çerçeveleri yenilik yerine uzun ömür ve işe alım için seçin, bir sonraki geçişten sağ çıkmak için çerçeveye özgü kodu sınırlar ardında yalıtın ve işleme stratejisini yüzey başına eşleştirin. Ön yüzü gerçek kullanıcı izleme, yönetişim ve her mimari seçimin neden yapıldığının denetlenebilir kaydıyla ortak altyapı olarak yönetin.

**Kamu.** Eski cihazlardaki, yavaş ya da kotalı bağlantılardaki ve yardımcı teknolojilerdeki insanlar dahil tüm kamuya hizmet veriyorsunuz; bu yüzden aşamalı geliştirme ve performans birer cila değil yükümlülüktür. Yurttaşa dönük hizmetler için JavaScript'siz çalışan bir tabanı katı kural yapın, sayfaları medyana değil en yavaş kullanıcılara göre bütçeleyin ve bir betik başarısız olduğunda çekirdek görevi tamamlanabilir tutun. Satın alma ve şeffaflık geçerlidir: tek satıcıya kilitlenmeyi önleyen dayanıklı, standartlara yaslanan teknolojiyi tercih edin, sözleşmelerde erişilebilirlik ve performans gerekliliklerini belgeleyin ve hizmetin yalnızca gösteri cihazı için değil, en az avantajlı kullanıcı için çalıştığını gösterebilir olun.

## Örnekler

**Girişim.** Tohum aşamasındaki bir girişim pazarlama sitesini ve kayıt akışını ağır bir tek sayfa uygulaması olarak kurmaya meyletti, ancak hedef müşterileri çoğunlukla dalgalı mobil verideki orta sınıf telefonlarda alışveriş yapanlardı. İki kurucu bunun yerine kamuya açık sayfaları sunucuda işledi; böylece hızlı yüklendi ve herhangi bir JavaScript çalışmadan önce işe yaradı ve istemci tarafı etkileşimi oturum açmanın ardındaki uygulamaya sakladı. Dikkatsiz bir bağımlılığın sayfayı sessizce şişirememesi için CI'da basit bir paket boyutu bütçesi koydular. Yalın, hızlı ilk yükleme kayıtları ölçülebilir biçimde iyileştirdi ve web standartlarına yaslanmak, işe aldıkça küçük kod tabanlarını bakımı kolay tuttu.

**Kurumsal.** Bir finansal hizmetler firması, olgun bir çerçeve, ortak bir bileşen kitaplığı ve CI'da zorlanan performans bütçeleri üzerinde standartlaşarak geniş bir iç ve müşteri uygulamaları kümesini modernleştirdi. İşleme stratejisi yüzey başına seçildi: kamuya açık pazarlama ve içerik için sunucuda işlenen, önbelleklenebilir sayfalar ve etkileşimli panolar için oturum açmanın ardında istemcide işlenen bir uygulama. Paket bütçeleri ve gerçek kullanıcı izleme, gerilemeleri yayından önce yakaladı; firmanın birçok takımı genelinde yükleme sürelerini hızlı tuttu ve daha önce maliyetli yeniden yazımları zorunlu kılan çerçeve kargaşası riskini azalttı.

**Kamu.** Ulusal bir dijital hizmet takımı, yurttaşa dönük hizmetleri aşamalı geliştirmeyi katı bir kural yaparak kurdu: her hizmet önce anlamsal HTML ve sunucu işlemeyle çalışır ve JavaScript yalnızca geliştirir. Bu, hizmetin eski telefonlarda, yavaş kırsal bağlantılarda ve yardımcı teknolojilerde, bir hükümetin dışlayamayacağı nüfuslarda, işlemesini garanti eder. Performans bütçeleri sayfaları düşük uç cihazlarda hafif ve hızlı tutar ve zarif işlev kaybı, başarısız bir betiğin birinin yardım başvurusunu tamamlamasını asla engellememesi demektir. Sonuç, hızlı, dayanıklı, erişilebilir ve tüm kamunun kullanabildiği bir hizmettir.

## İş gerekçesi: motivasyonlar, YG ve TSM

Ön yüz mühendisliği seçimleri geliri, erişimi ve maliyeti belirler. Performans doğrudan dönüşüme, etkileşime ve görev tamamlamaya bağlıdır. Daha hızlı deneyimler ölçülebilir biçimde daha yavaşlarını geçer ve zayıf cihazlardaki kullanıcılar için performans, hizmeti kullanmakla bırakmak arasındaki çizgidir. Aşamalı geliştirme ve çok cihazlı destek ulaşılabilir kitleyi genişletir; bu kamu için bir görev, kurumsal için pazar payıdır. Sağlam çerçeve ve mimari seçimleri, ön yüz mühendisliğindeki kaçınılabilir en büyük harcama olan yeniden yazımların sıklığını ve maliyetini azaltır.

TSM açısından benimseme maliyetleri, performans bütçelerinin ve testin disiplini, aşamalı geliştirmenin emeği ve ortak araçlara ve bileşen kitaplıklarına yapılan yatırımdır. Benimsememenin maliyeti, kullanıcı ve gelir kaybettiren yavaş deneyimlerle, düşük uç ve yardımcı teknoloji kullanıcılarının dışlanmasıyla (kamuda yasal riskle), sahada kırılan kırılgan uygulamalarla ve trendlerin peşinden koşmanın yol açtığı pahalı çerçeve kargaşası ve yeniden yazımlarla ödenir. Ön yüz sorunları tek bir kalem olarak değil dağınık terk edilme ve destek yükü olarak yüzeye çıkar; bu yüzden yetersiz yatırım yapmak kolaydır.

Liderliğe gerekçeyi kurmak için Core Web Vitals'ı ve yükleme sürelerini dönüşüm ve tamamlama hunilerine bağlayın, ağır istemci tarafı yaklaşımların dışladığı kullanıcıları nicelendirin ve geçmiş ya da yaklaşan yeniden yazımların maliyetini dayanıklı, standartlara yaslanan bir mimarinin kararlılığına karşı fiyatlandırın. Performans bütçelerini ve aşamalı geliştirmeyi risk azaltma ve erişim genişletme olarak çerçeveleyin.

## Anti-kalıplar ve tuzaklar

- **Çerçeve kovalamak**: kullanıcıya faydası olmadan kargaşa doğuran, en yeni kitaplıkla yeniden yazmak.
- **Yalnızca JavaScript deneyimleri**: büyük bir paket yüklenip çalışana kadar hiçbir şey işlemez, birçok kullanıcıyı dışlar.
- **Yalnızca hızlı cihazlarda test**: takımın amiral gemisi dizüstü bilgisayarları gerçek kullanıcı deneyimini gizler.
- **Paket boyutunu görmezden gelmek**: sayfalar her yerde yavaşlayana kadar sınırsız bağımlılık büyümesi.
- **Performans bütçesi olmaması**: gerilemeler sürümden sürüme sessizce birikir.
- **Boş ekran başarısızlıkları**: yükleme, boş, hata ya da çevrimdışı durumu yok; başarısız bir istek sayfayı bozar.
- **Aşırı merkezileşmiş genel durum**: her şey tek bir depoda, bağlaşım ve yeniden işleme fırtınaları yaratır.
- **Erken mikro ön yüzler**: haklı çıkaracak ölçek olmadan dağıtık sistem karmaşıklığı ve çoğaltılmış yükler.
- **Erişilebilirliği ve i18n'i mimaride ihmal etmek**: yüksek maliyetle sonradan eklemek.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Takım başına, ortak standart olmadan geçici ön yüz. Ağır istemci tarafı kodu, performans bütçesi yok, yalnızca takımın kendi cihazlarında test edilmiş. Çerçeve seçimleri tercihle ya da heyecanla yapılır ve başarısız bir betik kullanıcıları boş bir ekrana bakakalmış bırakabilir.

**Düzey 2, Geliştirme.** Bazı takımlar ortak araçları ve bir bileşen kitaplığını benimser, ancak uygulama kurum genelinde tutarsızdır. Performans bütçelenmek ya da zorlanmak yerine ara sıra ölçülür. İşleme stratejisi içerik türünden bağımsız olarak çoğu zaman tekdüzedir ve çok cihazlı test sınırlı ve elle yapılır.

**Düzey 3, Standartlaştırma.** Çerçeve ve mimari uzun ömür için bilinçli seçilir; seçimler kurum genelinde belgelenir ve zorlanır. İşleme stratejisi yüzey başına eşleştirilir, aşamalı geliştirme ve zarif işlev kaybı standarttır ve ortak bileşen kitaplıkları, lint ve derleme araçları her takım için geçerlidir. Tarayıcılar arası uyumluluk, erişilebilirlik ve uluslararasılaştırma sonradan eklenmek yerine yerleşiktir.

**Düzey 4, Yönetme.** Ön yüz veriyle ölçülür ve denetlenir. Performans bütçeleri gerilemeler derlemeyi başarısız kılsın diye CI'da zorlanır ve Core Web Vitals, açık taban değerlere karşı gerçek düşük uç cihazlardan ve yavaş bağlantılardan gerçek kullanıcı izlemeyle takip edilir. Paket boyutu, hata ve çevrimdışı durum kapsamı ve en yavaş bağlantılarda hizmet verilen kullanıcı payı raporlanır ve gözden geçirilir; böylece kararlar görüşe değil kanıta dayanır.

**Düzey 5, Orkestrasyon.** Performans, dayanıklılık ve erişim sürekli iyileştirilir ve tüm kurumda iş sonuçlarına bağlanır. Ön yüz dayanıklılık için web standartlarına yaslanır, geçişler ucuz olsun diye çerçeve bağımlılıklarını yalıtır ve cihazlar, platform ve gerçek kullanıcı verileri değiştikçe mimariyi uyarlanabilir biçimde evirir. Tüm kamu ve tüm cihazlar birinci sınıftır ve ön yüz pratiği ayrı bir mesele olarak ele alınmak yerine tasarım, erişilebilirlik ve ürün planlamasıyla bütünleşiktir.

## Tartışma fikirleri

- Bir çerçeve geçişinin maliyetine ve riskine değip değmediğine nasıl karar verirsiniz?
- Hangi Core Web Vitals ve paket bütçeleri derlemeyi başarısız kılan sert eşikler olmalı?
- Aşamalı geliştirme nerede şarttır ve istemci tarafı uygulama nerede kabul edilebilir?
- Birçok özerk takım arasında ön yüz mimarisini nasıl tutarlı tutarsınız?
- Mikro ön yüzler karmaşıklıklarının bedelini ne zaman gerçekten öder?
- Gerçek cihaz ve yavaş ağ testi hatta nasıl yerleştirilmeli?

## Önemli çıkarımlar

- Ön yüz denetlemediğiniz bir ortamda çalışır: değişkenlik ve başarısızlık için tasarlayın.
- Uzun ömürlü sistemler için dayanıklı, iyi desteklenen teknolojiyi seçin; web standartlarına yaslanın.
- İşleme stratejisini (SSR, SSG, CSR, akış) içeriğe ve ihtiyaca uydurun; çoğu zaman rota başına harmanlanır.
- Performansı, gerçek kullanıcı verileriyle CI'da zorlanan, bütçelenmiş ve ölçülen bir disiplin olarak ele alın.
- Çekirdek deneyim her yerde çalışsın diye aşamalı geliştirmeyle inşa edin.
- Daha az JavaScript gönderin; kodu bölün, tembel yükleyin ve platform yeteneklerini tercih edin.
- Özellikle kamu için performans ve dayanıklılık, hakkaniyetli erişimin ön koşullarıdır.

## Kaynaklar ve ileri okuma

- Jeremy Keith, *Resilient Web Design*
- Aaron Gustafson, *Adaptive Web Design* (progressive enhancement)
- Steve Souders, *High Performance Web Sites*
- Ilya Grigorik, *High Performance Browser Networking*
- Addy Osmani, writings on performance, code-splitting, and the cost of JavaScript
- Google, *Web Vitals* and web.dev performance guidance
- MDN Web Docs, web platform and progressive enhancement references
- Alex Russell, essays on the cost of JavaScript and device diversity
- UK Government Digital Service, progressive enhancement and frontend guidance
- WHATWG HTML Living Standard and W3C web platform specifications
