# 7.2 Veri mühendisliği

## Genel bakış ve motivasyon

[Veri mühendisliği](https://en.wikipedia.org/wiki/Data_engineering), veriyi üretildiği yerden değer yarattığı yere taşıyan hatları ve platformları kurma ve işletme disiplinidir. Kaynak sistemlerden alımı, verinin temiz ve modellenmiş biçimlere dönüştürülmesini, uygun maliyetli biçimlerde depolanmasını, bütün akışın orkestrasyonunu ve hepsini güvenilir tutan güvenilirlik uygulamalarını kapsar. Veri stratejisi hangi verinin var olması gerektiğine ve kimin sahip olduğuna karar veriyorsa, veri mühendisliği onun akmasını sağlayan tesisat ve makinedir.

Büyük takımlar için bu disiplin temeldir. Analitik, [iş zekası](https://en.wikipedia.org/wiki/Business_intelligence), ürün deneyleri, [makine öğrenmesi](https://en.wikipedia.org/wiki/Machine_learning) ve düzenleyici raporlama, hepsi veri hatlarının aşağı akışında yer alır. Bu hatlar kırılgan, yavaş ya da opak olduğunda bağımlı her işlev zarar görür. Panolar bayat sayılar gösterir. Modeller bozuk özniteliklerle eğitilir. Denetçiler bir rakamın nasıl üretildiğini yeniden kuramaz. Kurumsal ve kamu ölçeğinde hatlar, birçok kaynak sistemden milyarlarca kaydı işler ve tek bir sessiz arıza, yanlış veriyi kararlara, ödemelere ya da kamuya açık istatistiklere taşıyabilir.

Alan, özel yazılmış betiklerden ve yekpare [ETL (çıkar, dönüştür, yükle)](https://en.wikipedia.org/wiki/Extract,_transform,_load) araçlarından, alım, dönüştürme, orkestrasyon ve depolama için modüler, büyük ölçüde SQL güdümlü bileşenlerin açık biçimlerle birbirine bağlandığı modern veri yığınına doğru büyüdü. Bu modülerlik hem bir armağan hem de bir tuzaktır. En iyi sınıf araçları bir araya getirmenize izin verir, ama mühendislik disiplini olmadan belgelenmemiş, test edilmemiş işlerin bir yığınını üretir. Bu bölüm, hatları eş güçlü, test edilebilir, gözlemlenebilir ve ölçekte karşılanabilir maliyetli tutan uygulamaları ele alır.

## Temel ilkeler

- Hatlar yazılımdır ve sürüm denetimini, testi, gözden geçirmeyi ve CI/CD'yi hak eder.
- Güvenle yeniden çalıştırılabilen, eş güçlü ve yeniden üretilebilir dönüşümleri tercih edin.
- Veri akışlarını gözlemlenebilir kılın: tazelik, hacim, şema ve kalite izlenir.
- Ham tabloları dökmek yerine veriyi tüketicileri için bilinçli olarak modelleyin.
- Toplu ya da akış işlemeyi yenilikle değil, gerçek gecikme ihtiyaçlarına göre seçin.
- Depolama biçimini, bölümlemeyi ve işlem maliyetini birinci sınıf kaygılar olarak en iyileyin.
- Alımı, dönüştürmeyi ve sunumu ayırın; böylece her biri bağımsız evrilebilsin.
- Yüksek sesle ve erken başarısız olun; kırık bir hat, sessizce yanlış veriden daha güvenlidir.

## Öneriler

### ETL ya da ELT'yi bilinçli seçin

ETL, veriyi hedefe yüklemeden önce dönüştürür. [ELT (çıkar, yükle, dönüştür)](https://en.wikipedia.org/wiki/Extract,_load,_transform) önce ham veriyi yükler ve güçlü bir ambar ya da gölev içinde dönüştürür. Modern bulut platformları ELT'yi varsayılan hale getirdi, çünkü depolama ucuz ve işlem esnektir; ham veriyi saklamak ise mantık değiştiğinde ya da hatalar çıktığında yeniden işlemenize izin verir. Analitik iş yükleri için ELT'yi tercih edin: ham, değişmez veriyi indirin, sonra üzerine katmanlı dönüşümler kurun. Yüklemeden önce dönüştürmeyi, gizlilik, maliyet ya da sözleşme kısıtlarının veri inmeden önce temizlemeyi ya da süzmeyi gerektirdiği durumlara saklayın.

### Toplu ve akış hatlarını gecikme ihtiyaçlarına göre tasarlayın

Çoğu analitik ihtiyaç, akıl yürütmesi, test edilmesi ve geriye dönük doldurulması daha basit olan zamanlanmış toplu hatlarla iyi karşılanır. Akışa yalnızca iş gerçekten düşük gecikmeli veriye ihtiyaç duyduğunda başvurun: dolandırıcılık tespiti, operasyonel uyarı, gerçek zamanlı kişiselleştirme. Akış, sıralama, tam bir kez (exactly-once) semantiği, geç gelen veri ve durum yönetimi konusunda gerçek bir karmaşıklık ekler. İkisine de ihtiyaç duyduğunuzda, birbirinden ayrışan iki kod tabanı sürdürmek yerine toplu ve akış mantığını birleştiren mimarileri düşünün. Gecikme gereksinimleriniz konusunda dürüst olun. "Gerçek zamanlı" çoğu zaman maliyetinizi ikiye katlayan, sorgulanmamış bir dilektir.

### Orkestrasyonu açık bağımlılıklarla yapın

Hatları, açık bağımlılıkları, yeniden denemeleri ve zamanlamasıyla görevlerin [yönlü döngüsüz çizgelerini (DAG)](https://en.wikipedia.org/wiki/Directed_acyclic_graph) olarak ifade etmek için bir orkestratör kullanın. Bu size neyin çalıştığını, neyin başarısız olduğunu ve neyin engellendiğini görünür kılar, ayrıca belirlenimci biçimde geriye dönük doldurma ve yeniden çalıştırma imkânı verir. Bağımlılıkları yalnızca saate değil, verinin hazır olmasına dayandırın; böylece aşağı akıştaki işler bir tahmine göre ateşlenmek yerine yukarı akıştaki veriyi bekler. Orkestrasyon mantığını sürüm denetiminde tutun ve DAG değişikliklerine kod değişikliği gibi davranın.

### Veriyi tüketim için modelleyin

Ham tablolar analistler için nadiren uygundur. Yönetilen, yeniden kullanılabilir, self servis analitiğe ihtiyaç duyduğunuz yerde, olguları ve uyumlu boyutları [yıldız şemalarında](https://en.wikipedia.org/wiki/Star_schema) düzenleyen [boyutsal modellemeyi](https://en.wikipedia.org/wiki/Dimensional_modeling) uygulayın. Geniş, denormalize tablolar ("tek büyük tablo") belirli sorgu kalıpları için daha iyi performans verebilir ve bazı tüketiciler için daha basittir; bunun bedeli tekrar ve esneklik kaybıdır. Dönüşümlerinizi katmanlandırın: ham bir hazırlık katmanı, temizlenmiş ve uyumlanmış bir çekirdek katman ve tüketiciye dönük marts. Bu ayrım mantığı tek bir yerde düzeltmenizi sağlar ve tüketicilerin kararlı arayüzlere bağımlı olmasına izin verir.

### Hatları eş güçlü ve test edilebilir yapın

Dönüşümleri, yeniden çalıştırıldıklarında veriyi çoğaltmak ya da bozmak yerine aynı sonucu üretecek biçimde tasarlayın; örneğin iş tanımlayıcılarına dayalı belirlenimci upsert'ler ve bölüm üzerine yazma kalıplarıyla. Birden çok düzeyde test yazın: dönüştürme mantığı için birim testleri, şema testleri ve benzersizlik, boş olmayan anahtarlar, referans bütünlüğü ve kabul edilen değer aralıkları gibi beklentileri doğrulayan veri testleri. Bunları CI'da çalıştırın; böylece kötü bir değişiklik üretim verisine ulaşmadan yakalanır.

### Gözlemlenebilirliği ve güvenilirliği ölçümleyin

Veri sağlığının dört çekirdek sinyalini izleyin: tazelik (güncel mi), hacim (satır sayısı beklenen aralıkta mı), şema (yapı beklenmedik biçimde değişti mi) ve dağılım (değerler anormal biçimde kaydı mı). İhlallerde uyarı verin ve bunları sahibi takıma yönlendirin. Veri olayları için, tıpkı hizmetlerde olduğu gibi çalışma kılavuzları, nöbet rotasyonları ve suçlamasız olay sonrası incelemeleri tutun. Kökeni izleyin; bir şey bozulduğunda aşağı akıştaki etkiyi hemen görebilirsiniz.

### Depolamayı ve maliyeti en iyileyin

Parquet gibi sütunlu açık biçimleri ya da şema evrimini, zamanda geriye gitmeyi ve verimli güncellemeleri destekleyen açık tablo biçimlerini kullanın. Veriyi en çok süzdüğünüz sütunlara göre, tipik olarak tarihe göre bölümleyin ve birleştirme (compaction) yoluyla çok sayıda küçük dosyanın çoğalmasından kaçının. Sıcak ve soğuk veriyi kademeli depolama ve yaşam döngüsü politikalarıyla ayırın. Hat başına ve sorgu başına işlem harcamasını izleyin. Kontrolden çıkan maliyetler genellikle tam taramalardan, eksik bölümlerden ve sınırsız yeniden işlemeden gelir. Maliyeti, aylık faturada bir sürpriz değil, sahipleri olan bir metrik olarak ele alın.

## Ödünleşimler: artılar ve eksiler

| Seçim | Artılar | Eksiler | En uygun olduğu yer |
|---|---|---|---|
| ELT (yerinde dönüştürme) | Ham veriyi korur, ucuz depolama, yeniden işlenebilir | Büyük depolama ayak izi, yönetişim gerekir | Bulut analitiği |
| ETL (yüklemeden önce dönüştürme) | Maliyeti denetler, hassas veriyi erken süzer | Ham veri kaybolur, yeniden işlemek zorlaşır | Düzenlenen ya da kısıtlı yüklemeler |
| Toplu | Basit, test edilebilir, kolay geriye dönük doldurma | Daha yüksek gecikme | Çoğu analitik |
| Akış | Düşük gecikme, gerçek zamanlı tepki | Karmaşık, pahalı, test etmesi zor | Dolandırıcılık, operasyonel uyarı |
| Yıldız şeması | Yönetilen, yeniden kullanılabilir, self servise elverişli | Baştan modelleme çabası | Ortak iş zekası |
| Geniş tablo | Bilinen sorgularda hızlı, basit | Tekrar, daha az esnek | Dar, yüksek performanslı kullanım |

Baskın ödünleşim, sadelik ile gecikme ve esneklik arasındadır. Toplu işleme ve ELT ile katmanlı yıldız şemaları, size çoğu ihtiyacı uygun maliyetle karşılayan test edilebilir, geriye dönük doldurulabilir, iyi anlaşılmış bir sistem verir. Akış, gerçek zamanlı ve yüksek düzeyde denormalize tasarımlar hız ve belirli performans satın alır, ama operasyonel karmaşıklık ve test zorluğunda ağır bir bedelle. Karmaşıklığı yalnızca somut bir iş gereksiniminin bedelini ödediği yerde benimseyin ve basit yolu varsayılanınız olarak tutun.

## Takımınızla tartışılacak sorular

1. **ELT'yi ETL'ye tercih etmeyi bilinçli olarak seçtiniz mi ve mantık değiştiğinde ya da hatalar ortaya çıktığında yeniden işleyebilmek için ham, değişmez veriyi saklıyor musunuz?** Bölümün varsayılanı ELT'dir: ham veriyi ucuza indirin, sonra katmanlı dönüşümler kurun; çünkü ham veriyi saklamak, bir kural değiştiğinde ya da haftalar sonra bir hata çıktığında her şeyi yeniden çalıştırmanızı sağlar. Ham veriyi silmek bu seçeneği ortadan kaldırır ve yaygın, acı verici bir tuzaktır. ETL lehine rakip gerekçe, gizlilik, maliyet ya da sözleşme şartlarının veri inmeden önce süzmeyi ya da maskelemeyi gerektirdiği düzenlenen ya da kısıtlı yüklemelerde gerçektir. Kanıt getirin: geçmişi ne sıklıkla yeniden işlemeniz gerekti ve yapamadığınızda bunun bedeli ne oldu? Herhangi bir rakamı kaynağa kadar izlemesi gereken bir kamu ya da kurumsal hat için değişmez ham kayıtlar aynı zamanda bir denetlenebilirlik gereksinimidir; bu yüzden cevap hem depolama politikanızı hem de yasal savunulabilirliğinizi şekillendirir.

2. **Dört veri sağlığı sinyalinden hangisini gerçekten izliyorsunuz ve biri bozulduğunda kim çağrılıyor?** Bölüm, izlemeye değer dört sinyali adlandırır: tazelik, hacim, şema ve dağılım. Birçok takım hiçbirini izlemez ve arızaları, bayat bir panoya bakan bir yöneticiden öğrenir; bu, olabilecek en kötü dedektördür. Kurumsal ve kamu ölçeğinde tek bir sessiz arıza yanlış veriyi ödemelere, raporlara ya da kamuya açık istatistiklere itebilir; dolayısıyla geç tespitin maliyeti yalnızca yeniden işle değil, güven ve parayla ölçülür. Gerçek ortalama tespit sürenizi ve olayları şu anda ilk kimin bulduğunu getirin. Cevap "bir tüketici" ise, sahibi takıma yönlendirilen uyarılara, ayrıca çalışma kılavuzlarına ve suçlamasız olay sonrası incelemelere ihtiyacınız var; veri olaylarına tıpkı hizmet kesintileri gibi davranın.

3. **Analistleriniz modellenmiş, test edilmiş marts mı tüketiyor, yoksa ham tabloları üzerlerine döküp buna self servis mi diyorsunuz?** Bölüm açıktır: ham tablolar analistler için nadiren uygundur ve dönüşümleri ham bir hazırlık katmanına, uyumlanmış bir çekirdeğe ve tüketiciye dönük marts'a katmanlandırmak, mantığı bir kez düzeltmenizi ve tüketicilere kararlı arayüzler vermenizi sağlar. Rakip çekim hızdır, çünkü yıldız şemalarıyla ya da bilinçli geniş tablolarla modelleme baştan çaba gerektirir ve onu atlamak cazip gelir. Ama ham veriyi dökmek, modelleme maliyetini her analistin üzerine tekrar tekrar yükler ve ayrışan sayılar ile boşa giden saatler üretir. Bir işaret getirin: analist zamanının ne kadarı ham veriyi yeniden şekillendirmeye gidiyor ve kaç takım aynı birleştirmeleri yeniden kurmuş? Sayı yüksekse, tüketicilerin yeniden icat etmek yerine test edilmiş, yeniden kullanılabilir arayüzlere bağımlı olması için uyumlanmış bir çekirdek katmana yatırım yapın.

4. **"Gerçek zamanlı" maliyetini nerede gerçekten hak ediyor ve nerede operasyonel yükünüzü sessizce ikiye katlayan, sorgulanmamış bir dilek?** Bölümün varsayılanı, akıl yürütmesi, test edilmesi ve geriye dönük doldurulması daha basit olan zamanlanmış toplu işlemedir; akış, dolandırıcılık tespiti ya da operasyonel uyarı gibi işin gerçekten düşük gecikmeye ihtiyaç duyduğu durumlara ayrılır. Rakip çekim, prestij ve "canlı" veri için belirsiz paydaş taleplerdir; bunlar planlama toplantısında ucuz görünür ve üretimde pahalıya dönüşür, çünkü akış, sıralamayı, tam bir kez semantiğini, geç gelen veriyi ve durum yönetimini, ayrıca toplu mantıkla uyumlu tutulması gereken ikinci bir kod tabanını beraberinde getirir. Tartışmaya kanıt getirin: işlettiğiniz ya da önerdiğiniz her akış hattı için, beslediği kararı ve o kararın gerçekte tolere ettiği gecikmeyi sıfatlarla değil dakika ya da saatlerle adlandırın. Büyük bir kurumsal ya da kamu platformu için her gerçek zamanlı yolun nöbet ve test maliyetini ekleyin; çünkü kimsenin test edemediği ya da günün her saati kadrolayamadığı bir akış hattı, özellik kılığına girmiş bir güvenilirlik yükümlülüğüdür ve dürüst cevap çoğu zaman bir "gerçek zamanlı" gereksinimi aynı kararı karşılayan saatlik bir topluya geri indirir.

5. **Hatlarınızdan hangileri bugün güvenle yeniden çalıştırılamaz ve her dönüşümü eş güçlü yapmak için ne gerekir?** Bölüm, eş güçlü, yeniden üretilebilir dönüşümlerde ısrar eder: iş tanımlayıcılarına dayalı belirlenimci upsert'ler ve bölüm üzerine yazma kalıpları; böylece yeniden çalıştırma veriyi çoğaltmak ya da bozmak yerine aynı sonucu üretir. Rakip baskı teslimat hızıdır, çünkü saf eklemeli bir iş, yeniden çalıştırılabilir olacak biçimde tasarlanmış olandan daha hızlı sevk edilir ve bu kestirmenin maliyeti, bir arıza sabaha karşı saat ikide kısmi bir yeniden çalıştırmayı zorlayana ve biri geliri iki kez sayana kadar gizli kalır. Somut bir envanter getirin: bir arıza noktasından yeniden çalıştırılırsa veriyi bozacak işleri listeleyin ve en kötüsünün etki alanını tahmin edin. Tek bir sessiz arızanın yanlış veriyi ödemelere, raporlara ya da kamuya açık istatistiklere itebildiği kurumsal ve kamu ölçeğinde, eş güçlü olmayan işleme yalnızca rahatsız edici değildir; bir kural değişikliğinden sonra bir dönemi yeniden işlemenize ve yine de her rakamı kaynağa kadar izlemenize izin veren denetlenebilirliği zayıflatır. Bu yüzden yeniden çalıştırmaları güvenli kılacak işi finanse etmek, yalnızca bir düzen değil, bir denetim sorusudur.

6. **Her hattın çalıştırma maliyetini, bu sayının sahibini ve bulut faturanızın ne kadarının tam taramalardan ve eksik bölümlerden geldiğini biliyor musunuz?** Bölüm, depolama biçimini, bölümlemeyi ve işlem harcamasını sahipleri olan birinci sınıf kaygılar olarak ele alır ve kontrolden çıkan maliyetlerin genellikle tam taramalara, eksik bölümlere ve sınırsız yeniden işlemeye dayandığı konusunda uyarır. Rakip düşünce, maliyet işinin özellik sevk etmekten daha az acil hissettirmesidir; bu yüzden aylık fatura bir sürpriz olana ve finans, mühendisliğin yanıtlayamadığı sorular sormaya başlayana kadar ertelenir. Kanıt getirin: hat başına ve sorgu başına harcama, bölümlenmemiş taramalardan gelen maliyet payı ve birleştirilmesi gereken küçük dosya sayısı. Birçok kaynak sistemden milyarlarca kaydı işleyen büyük bir kurum için sahipsiz bir bulut faturası, hiçbir takım kendini sorumlu hissetmeden büyür; kamu ortamlarında ise kamu harcaması kalem kalem gerekçelendirilmelidir. Dolayısıyla işlem maliyetini izlenen bir metrikle adı belli bir sahibe atfetmek opak bir gideri yönetilen bir gidere dönüştürür ve çoğu zaman bir sonraki platform yatırımını finanse edecek kadar büyük tasarruflar ortaya çıkarır.

## Sektör merceği

**Girişim.** Hız, mimariyi yener. Alımı yönetilen bir bağlayıcıya bağlayın, sürüm denetimli bir avuç dönüşüm kurun ve bunları, gece sessizce bozulan elle yazılmış cron işleri yerine kendi kendine yeniden deneyen ve geriye dönük dolduran hafif bir orkestratörde çalıştırın. Her modeli ilk işlemeden itibaren eş güçlü tutun ve boş anahtarlar ile satır sayıları için birkaç ucuz test ekleyin; böylece kötü bir kaynak değişikliği, kurucunun pazartesi panosunda görünmek yerine CI'da başarısız olur. Akış ya da özel bir platform kurmayın: en kıt kaynağınız mühendislik dikkatidir.

**Küçük işletme.** Özel bir veri mühendisiniz yoksa, bir yığını bir araya getirmek yerine bütünleşik bir yığın satın almayı tercih edin. Yönetilen bir ELT hizmeti ile bir bulut ambarı, bunları sürdürecek bir platform takımı olmadan size bağlayıcıları, zamanlamayı ve depolamayı verir. Seçimi bir hat projesi değil, veri hijyeni olarak çerçeveleyin: raporlarınızı hangi kaynak sistemlerin beslediğini bilin, yanlış bir sayı izlenip yeniden işlenebilsin diye ham veriyi saklayın ve tam tablo taraması aylık bütçeyi patlatmasın diye maliyeti öngörülebilir araçlar seçin.

**Kurumsal.** Sorun, birçok takım ve birçok kaynak sistemden gelen milyarlarca kayıt arasında tutarlılıktır. ELT kalıbını, katmanlı hazırlık, çekirdek ve mart modelini ve dört veri sağlığı sinyalini standartlaştırın; böylece gruplar kırılgan hatları yeniden icat etmeyi bırakır. Her model için veri testlerini ve CI'ı zorunlu kılın, işlem maliyetini sahibi takımlara atfedin ve veri olaylarını hizmetlerde kullandığınız aynı nöbet, çalışma kılavuzu ve suçlamasız olay sonrası inceleme disiplininden geçirin; böylece sessiz bir arıza bir panoya fark edilmeden ulaşmaz.

**Kamu.** Satın alma kuralları, şeffaflık ve kamuya karşı hesap verebilirlik hattı şekillendirir. Denetlenebilirlik için değişmez ham kayıtları indirin, bunları katmanlı, test edilmiş aşamalarda dönüştürün ve bir denetçinin yayımlanmış herhangi bir rakamı kaynak belgelerine kadar izleyebilmesi için, çoğu zaman yasal bir gereklilik olarak, tam kökeni tutun. Eş güçlü işleme, bir kural değiştiğinde bir beyanname ya da raporlama dönemini güvenle yeniden işlemenize izin verir; açık biçimleri ve taşınabilir dönüştürme kodunu tercih etmek de çok yıllı bir sözleşme boyunca tek bir tedarikçiye kilitlenmenizi önler.

## Örnekler

**Girişim.** On kişilik bir analitik girişimi, gece sessizce bozulan ve bir mühendis elle yeniden çalıştırdığında bazen satırları iki kez sayan bir cron işleri yumağına dönüşmüştü. Takım alım için yönetilen bir bağlayıcıya, sürüm denetimli modeller için bir dönüştürme çerçevesine ve kendi kendine yeniden deneyen ve geriye dönük dolduran hafif bir orkestratöre geçti. Her modeli eş güçlü yaptılar ve boş anahtarlar ile satır sayıları için bir avuç test eklediler; böylece kötü bir kaynak değişikliği artık kurucunun pazartesi panosunda görünmek yerine CI'da başarısız oluyor.

**Kurumsal.** Küresel bir perakendeci, elle yazılmış yüzlerce çıkarma betiğini bir ELT yığınıyla değiştirdi. Yönetilen bağlayıcılar ham kaynak verisini indiriyor, bir dönüştürme çerçevesi bir gölevde test edilmiş, sürüm denetimli modeller kuruyor ve bir orkestratör bağımlılıkları yeniden denemeler ve geriye dönük doldurmalarla yönetiyor. Veri testleri, kaynak sistemlerden gelen şema kaymasını panolara ulaşmadan yakalıyor. Bölümlenmiş sütunlu depolama sorgu maliyetlerini önemli ölçüde düşürdü, tazeliği ise günlükten saatliğe çıkardı.

**Kamu.** Bir vergi idaresi, beyannameleri ve üçüncü taraf verilerini, denetlenebilirlik için değişmez ham kayıtları indiren, ardından bunları katmanlı, test edilmiş aşamalarda dönüştüren yönetilen bir hat üzerinden alır. Eş güçlü işleme, bir kural değiştiğinde bir beyanname dönemini güvenle yeniden işlemelerine izin verir. Tam köken izleme, denetçilerin hesaplanmış herhangi bir rakamı kaynak belgelere kadar izlemesine olanak tanır; bu, kamuya karşı hesap verebilirlik için yasal bir gerekliliktir.

## İş gerekçesi: motivasyonlar, YG ve TSM

Disiplinli veri mühendisliğinin YG'si (yatırım getirisi) güvenilirlikten, hızdan ve maliyet denetiminden gelir. Güvenilir hatlar, kararların ve raporların güvenilir veriye dayanması demektir; böylece yanlış sayıların pahalı yeniden işini ve itibar zararını önlersiniz. Modüler, test edilmiş hatlar takımların yeni veri ürünlerini daha hızlı sevk etmesini sağlar ve aşağı akıştaki her analitik ve makine öğrenmesi yatırımının değerini katlar. Depolamayı ve işlemi en iyilemek bulut faturasını doğrudan düşürür; bölümleme ve sorgu kalıpları düzeltildiğinde çoğu zaman büyük farklarla.

Benimseme maliyeti platform araçlarını, test edilmiş modüler hatlar kurmak için mühendislik zamanını ve veriyi yazılım gibi ele alma disiplinini içerir. Bunu benimsememenin maliyetiyle tartın: yalnızca yazarının anladığı kırılgan özel işler, yöneticiler tarafından keşfedilen sessiz veri bozulması, tam tablo taramalarından şişen bulut harcaması ve veri beklerken tıkanan analistler. Liderliğe, veri mühendisliğini analitiği, iş zekasını ve yapay zekayı güvenilir ve karşılanabilir kılan temel olarak anlatın. Burada eksik yatırım yaparsanız, üstündeki her veri girişiminin getirisine tavan koymuş olursunuz.

## Anti-kalıplar ve tuzaklar

- Sürüm denetimi, testi ya da gözden geçirmesi olmayan tek seferlik betikler olarak kurulmuş hatlar.
- Bir arızadan sonra yeniden çalıştırıldığında veriyi çoğaltan ya da bozan eş güçlü olmayan işler.
- Toplu işleme gecikme gereksinimini karşılayacakken, prestij için akışı benimsemek.
- Analistlere ham tabloları dökmek ve buna self servis demek.
- Gözlemlenebilirlik yok; arızalar aşağı akıştaki tüketiciler tarafından keşfediliyor.
- Bulut faturası patlayana kadar bölümlemeyi ve dosya boyutlandırmayı görmezden gelmek.
- Alımı, dönüştürmeyi ve sunumu birbirine bağlayıp hiçbir şeyin güvenle değişememesi.
- Ham veriyi silmek ve mantık değiştiğinde yeniden işlemeyi imkânsız kılmak.

## Olgunluk modeli

1. Düzey 1, Başlangıç: Testsiz ve izlemesiz, tesadüfi betikler ve elle çalıştırmalar. Arızaları aşağı akıştaki tüketiciler keşfeder, işler güvenle yeniden çalıştırılamaz ve bulut maliyetleri yönetilmez ve atfedilmez.
2. Düzey 2, Geliştirme: Bazı takımlar bir orkestratör benimsemiş ve temel dönüşümleri sürüm denetimine almış, ama uygulama kurum genelinde tutarsız. Ara sıra testler var, eş güçlülük düzensiz ve kırık hatlar hâlâ tepkisel yangın söndürme anlamına geliyor.
3. Düzey 3, Standartlaştırma: Test edilmiş ve sürüm denetimli, katmanlı hazırlık, çekirdek ve mart modeliyle ELT, takımlar arasında uygulanan belgelenmiş standarttır. Yeniden denemeler ve geriye dönük doldurmalarla orkestre edilmiş bağımlılıklar, CI'da çalışan veri testleri ve yıldız şeması modelleme ile bölümleme için ortak kurallar, her gruba bırakılmak yerine kurum genelinde uygulanır.
4. Düzey 4, Yönetme: Platform ölçülür ve denetlenir. Tazelik, hacim, şema ve dağılım, sahibi takımlara yönlendirilen uyarılarla izlenir; hat SLA'ları, ortalama tespit süresi, veri kalitesi başarı oranları ve hat başına ve sorgu başına işlem maliyeti taban çizgilerine karşı takip edilir. Geri alma ve durdurma eşikleri kanıta dayanarak uygulanır ve maliyet ile güvenilirliğin hedeflerden sorumlu, adı belli sahipleri vardır.
5. Düzey 5, Orkestrasyon: Hatlar tümüyle CI/CD, veri sözleşmeleri ve tüketicilerden önce kaymayı yakalayan otomatik anormallik tespitiyle yazılım olarak ele alınır. Toplu ve akış mantığı, gecikmenin gerçekten karşılığını verdiği yerde birleştirilir, platform sürekli iyileştirilir ve self servistir; kapasite, depolama kademeleri ve maliyet iş yükleri değiştikçe uyarlanarak yeniden dengelenir, böylece yeni veri ürünleri kararlı bir temel üzerinde hızla sevk edilir.

## Tartışma fikirleri

- Yığınınızın neresinde "gerçek zamanlı" maliyetini gerçekten hak ediyor ve neresinde dilekten ibaret?
- Hangi hatlar bugün güvenle yeniden çalıştırılamaz ve bunu düzeltmek için ne gerekir?
- Bulut veri faturanızın ne kadarı tam taramalardan ve eksik bölümlerden geliyor?
- Analistleriniz modellenmiş marts mı yoksa ham tabloları mı tüketiyor ve bu onlara neye mal oluyor?
- Bir veri olayını tespit etmenin ortalama süresi nedir ve onu ilk kim buluyor?
- Toplu ve akış mantığını birleştirmek bakım yükünüzü azaltır mıydı, yoksa risk mi eklerdi?

## Önemli çıkarımlar

- Hatları yazılım olarak ele alın: sürüm denetimi, testler, gözden geçirme, CI/CD ve gözlemlenebilirlik.
- Katmanlı, test edilmiş modellerle ELT'yi tercih edin; yeniden işleme için ham veriyi saklayın.
- Varsayılan olarak toplu işlemeyi seçin, akışı yalnızca gecikmenin gerçekten karşılığını verdiği yerde kullanın.
- Dönüşümleri eş güçlü yapın; böylece yeniden çalıştırmalar güvenli olur.
- Veriyi tüketiciler için yıldız şemaları ya da bilinçli geniş tablolarla modelleyin.
- Tazeliği, hacmi, şemayı ve dağılımı izleyin ve veri olaylarına kesinti gibi davranın.
- Depolama biçimlerini, bölümlemeyi ve işlem maliyetini birinci sınıf kaygılar olarak en iyileyin.

## Kaynaklar ve ileri okuma

- Joe Reis and Matt Housley, "Fundamentals of Data Engineering."
- Ralph Kimball and Margy Ross, "The Data Warehouse Toolkit."
- Martin Kleppmann, "Designing Data-Intensive Applications."
- Bill Inmon, "Building the Data Warehouse."
- James Densmore, "Data Pipelines Pocket Reference."
- Nathan Marz and James Warren, "Big Data" (Lambda architecture).
- Barr Moses and colleagues, "Data Quality Fundamentals" (data observability).
