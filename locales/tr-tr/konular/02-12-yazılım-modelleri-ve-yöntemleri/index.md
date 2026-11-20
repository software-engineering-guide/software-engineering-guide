# 2.12 Yazılım modelleri ve yöntemleri

## Genel bakış ve motivasyon

Bir yazılım modeli, belirli bir soruyu cevaplamak için kurulmuş, bir sistemin bilinçli bir sadeleştirmesidir. Bir yöntem, yol boyunca kullandığı modeller dahil, yazılım üretmenin disiplinli bir yoludur. Birlikte bir Yazılım Mühendisliği Bilgi Birikimi (SWEBOK) bilgi alanı oluştururlar, çünkü bir sistemi inşa etmeden önce, inşa ederken ve inşa ettikten sonra onun üzerinde akıl yürütmek için kullandığınız zihinsel araçlardır. Bir UML ([Birleşik Modelleme Dili](https://en.wikipedia.org/wiki/Unified_Modeling_Language)) sınıf diyagramı, bir [varlık-ilişki diyagramı](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) (VİD), bir [durum makinesi](https://en.wikipedia.org/wiki/Finite-state_machine), bir [biçimsel belirtim](https://en.wikipedia.org/wiki/Formal_specification) ve at-kullan bir prototip, hepsi modeldir. [Şelale](https://en.wikipedia.org/wiki/Waterfall_model), [prototipleme](https://en.wikipedia.org/wiki/Software_prototyping), biçimsel geliştirme ve [çevik](https://en.wikipedia.org/wiki/Agile_software_development) hepsi yöntemdir.

Modellerle neden uğraşılır? Çünkü insanın çalışma belleği küçük ve yazılım sistemleri büyüktür. Hiç kimse yüz bin satırlık bir sistemi kafasında tutamaz; bu yüzden her seferinde bir yönü gösteren resimler çizer ve soyutlamalar yazarız: veriyi, kontrol akışını, durumları, etkileşimleri. Bir model asla koda sadık olması için değildir; bir karara uygun olması içindir. İyi bir model bir şeye karar vermek için tam olarak ihtiyacınız olanı gösterir ve geri kalan her şeyi gizler.

Büyük takımlarda gerçek bahisler eşgüdüm ve iletişimdir. Yüzlerce mühendis, mimar, analist ve denetçi tek bir sistem üzerinde çalıştığında, paylaşılan modeller tasarımı, gereksinimleri ve riski pazarlık ettikleri ortak zemindir. Bu yüzden modellemeyi yapacak bir işi olan bir araç olarak düşünün. Bir model önlediği hatadan ucuz olduğunda karşılığını verir. Kendi iyiliği için çizdiğinizde, bayatladıktan çok sonra tuttuğunuzda ya da hizmet etmesi amaçlanan kararın ötesine ayrıntılandırdığınızda israf olur. Modelleme, yazılım gereksinimlerine (bölüm 2.8), yazılım tasarım ilkelerine (bölüm 2.2), mimariye ve C4 ve arc42 gibi notasyonlarına (bölüm 3.1) ve çevik çalışma biçimlerine (bölüm 10.7) sıkıca bağlanır.

## Temel ilkeler

- Her modelin bir amacı vardır; bir modelin hangi kararı bilgilendirdiğini adlandıramıyorsanız çizmeyin.
- Soyutlama modellemenin çekirdek eylemidir: amaç için önemli olanı dahil edin, gerisini bırakın.
- Tutarlılık modeller içinde ve arasında önemlidir; çelişen modeller hiç olmamasından kötüdür.
- Modeller önce iletişim yapıtlarıdır; hedef kitleleri notasyonlarını ve ayrıntılarını belirler.
- Soruyu cevaplayan en hafif modeli tercih edin; ayrıntılandırmanın taşıma maliyeti vardır.
- Bir model analizi kadar iyidir; denetlenmemiş bir model test edilmemiş bir varsayımdır.
- Yöntemi sorunun belirsizliğine, riskine ve başarısızlığın sonucuna uyacak şekilde seçin.

## Öneriler

### Soyutlama, amaç ve tutarlılıkla modelleyin

Her modele amacını ve hedef kitlesini adlandırarak başlayın. Sonra o amaca doğru acımasızca soyutlayın: bir yarış koşulunu çözmeyi amaçlayan bir sıra diyagramı her alanı değil, zamanlamayı ve mesajları göstermelidir. Modellerinizi birbirleriyle tutarlı tutun; böylece bir VİD'deki varlıklar, bir sınıf diyagramındaki sınıflar ve gereksinimlerdeki isimler hepsi uyuşsun ve gerçeklikle tutarlı tutun; bu, sistem ilerlediğinde bir modeli güncellemeniz ya da silmeniz anlamına gelir. İnsanların güvendiği bayat bir model bir tehlikedir. Herkesin görmezden geldiği bayat bir model hâlâ dikkate mal olan bir israftır.

### Soruya uyan yapısal ya da davranışsal modeller seçin

Bir sistemin neyden yapıldığını ve parçaların nasıl ilişkili olduğunu göstermek için yapısal modeller kullanın: veri yapısı için sınıf diyagramları, bileşen diyagramları ve varlık-ilişki diyagramları. Bir sistemin zaman içinde ne yaptığını göstermek için davranışsal modeller kullanın: anlamlı yaşam döngüleri olan nesneler için durum makineleri, bileşenler arası etkileşimler için sıra diyagramları ve iş akışları ile iş süreçleri için etkinlik diyagramları. Önünüzdeki kararı açığa çıkaran tek notasyonu seçin. Çoğu sistem yalnızca bir avuç diyagram türüne ihtiyaç duyar; her şeye uygulanan tüm UML kataloğuna değil, seçici çizilmiş.

### Modelleri yalnızca çizmeyin, analiz edin

Bir model yalnızca çizimle değil, analizle yerini hak eder. Bir durum makinesini ulaşılamaz durumlar, eksik geçişler ve kilitlenme için kontrol edin. Bir VİD'yi normalleştirme sorunları ve yetim ilişkiler için kontrol edin. Eksik hata yollarını bulmak için bir sıra diyagramını gereksinimlere karşı gözden geçirin. Modellerinizi neyin yanlış olduğunu fark edebilecek alan uzmanlarıyla inceleyin. Ve başarısızlık maliyetinin yüksek olduğu yerde, gözle kontrol etmek yerine araç destekli analize (model denetleyiciler, tutarlılık denetleyiciler, benzetim) başvurun.

### Sezgisel yöntemleri varsayılan olarak uygulayın

Yazılımın çoğu sezgisel yöntemlerle inşa edilir: modelleri gayriresmi kullanan ve sonuçları kanıtlara değil beklentilere göre yargılayan, deneyime dayalı, yinelemeli yaklaşımlar. Çoğu iş ve kamu sistemi için bu tam olarak doğrudur: gereksinimler evrilir ve bir kusur genellikle telafi edilebilir. Sezgisel yöntemler doğal olarak çevik ile eşleşir (bölüm 10.7): takımı hizalamaya yetecek kadar modelleyin, sonra inşa edin ve öğrenin.

### Biçimsel yöntemleri yüksek sonuçlu çekirdeklere saklayın

[Biçimsel yöntemler](https://en.wikipedia.org/wiki/Formal_methods) belirtimleri matematikle ifade eder ve özellikleri kanıtlamak için doğrulama, ister kanıt ister kapsamlı [model denetimi](https://en.wikipedia.org/wiki/Model_checking) olsun, kullanır. Gerçek beceriye ve zamana mal olurlar ve tam olarak başarısızlığın felaket ya da geri döndürülemez olduğu yerde karşılığını verirler: güvenlik açısından kritik kontrol, şifreleme protokolleri, mali takas çekirdekleri ve benzerleri. Onları tüm sisteme değil, küçük kritik çekirdeğe uygulayın. Ve tam kanıt olmadan bile, yalnızca biçimsel belirtimin sizi kesin olmaya zorlayarak çoğu zaman değer kattığını not edin.

### Belirsizliği gidermek için prototiplemeyi kullanın

Gereksinimler ya da uygulanabilirlik net olmadığında, öğrenmek için bir prototip inşa edin, sonra onu evriltip evriltmeyeceğinize ya da atacağınıza bilerek karar verin. At-kullan prototipler bir soruyu ucuza araştırır ve sonra silinir. Evrimsel prototipler ürün olur ve üretim standartlarında inşa edilmelidir. Klasik başarısızlık, at-kullan bir prototipin kazara üretime kaymasına izin vermektir. Bu yüzden inşa etmeden önce prototipin türünü adlandırın.

### Yöntemi moda değil riske uydurun

Yöntemleri sorunun belirsizliğine ve başarısızlığın sonucuna göre seçin. Yüksek belirsizlik prototiplemeyi ve çevik yinelemeyi tercih eder. Yüksek sonuç biçimsel analizi ve titiz doğrulamayı tercih eder. İkisine de sahip bir sistem, aksi halde çevik bir zarfın içinde kritik bir biçimsel çekirdeğe ihtiyaç duyar. Ne yaparsanız yapın, bir yöntemi yalnızca prestijli olduğu ya da bir satıcı sattığı için benimsemeyin.

## Ödünleşimler: artılar ve eksiler

| Model veya yöntem | İyi uygulandığında | Başarısızlık biçimi |
|---|---|---|
| Yapısal modeller (UML, VİD) | Parçaların ve verinin paylaşılan resmi | Diyagram yayılması; koddan sapma |
| Davranışsal modeller (durum, sıra, etkinlik) | Zamanlamayı, durumları ve uç durumları açığa çıkarır | Kimsenin okumadığı aşırı ayrıntılı diyagramlar |
| Sezgisel yöntemler | Hızlı, esnek, çoğu sisteme uyar | Disiplinsiz; gizli varsayımlar |
| Biçimsel yöntemler | Kritik çekirdekler için kanıtlanabilir özellikler | Yüksek maliyet; tüm sisteme yanlış uygulanır |
| Prototipleme | Ucuz öğrenme; riski erken giderir | Üretime terfi ettirilen at-kullan kod |
| Çevik yöntemler | Değişen gereksinimlere uyum sağlar | Zor sorunlar için gereken modellemeyi atlar |

Yinelenen gerilim titizlik ile hız arasındadır. Çok az modelleme gizli varsayımları üretime gönderir. Çok fazla modelleme, hiçbir zaman bir kararı bilgilendirmeyen ve kod değiştiği anda çürüyen diyagramlara çaba yakar. Bunu düzeltecek sabit bir doz yoktur, yalnızca bir oran kuralı vardır: bir modele ya da yönteme çözdüğü belirsizlikle ve kararı yanlış verme maliyetiyle orantılı yatırım yapın. Bir ödeme motoru ile bir pazarlama mikro sitesi farklı muamele hak eder.

## Takımınızla tartışılacak sorular

1. **Modellerimizi analiz mi ediyoruz, yoksa yalnızca çizip geçiyor muyuz?** Bir model varlığıyla değil analiziyle yerini hak eder: ulaşılamaz durumlar ya da eksik geçişler için hiç kontrol etmediğiniz bir durum makinesi, diyagram kılığına girmiş test edilmemiş bir varsayımdır. Büyük bir takımda gerçek kusurların saklandığı yer burasıdır, çünkü inandırıcı görünen bir resme tam olarak kimse onu eksik hata yolunu ya da yetim ilişkiyi bulmak için gereksinimlere karşı yürümediğinde güvenilir. Toplantıya en önemli davranışsal modelinizi getirin ve onu kırmaya çalışın: hangi geçiş tanımsız, hangi durumun çıkışı yok, hangi sıranın zaman aşımı yok? Başarısızlık maliyetinin yüksek olduğu yerde cevap sizi gözle kontrol yerine araç destekli analize (model denetleyiciler, tutarlılık denetleyiciler, benzetim) itmelidir, çünkü kritik bir çekirdeği modellemenin tüm nedeni kusuru üretimde değil bir beyaz tahtada bulmaktır.

2. **İki modelimiz çeliştiğinde hangisi kazanır ve çelişkiyi kim fark eder?** Tutarlılık modeller içinde ve arasında önemlidir ve çelişen modeller hiç olmamasından kötüdür, çünkü insanlar ikisine de göre davranır. Büyük bir sistemde veri modelindeki varlıklar, tasarımdaki sınıflar ve gereksinimlerdeki isimler, farklı takımlar farklı yapıtları güncelledikçe sessizce birbirinden uzaklaşır ve ilk işaret çoğu zaman iki bileşenin bir şeyin ne olduğu konusunda anlaşamadığı bir üretim hatasıdır. Bir örnek getirin: bir çekirdek kavram seçin ve VİD'nin, kodun ve gereksinimlerin şekli ve yaşam döngüsü konusunda gerçekten uyuşup uyuşmadığını kontrol edin. Uyuşmuyorlarsa hangi yapıtın yetkili olduğuna ve diğerlerini uyumlu tutmaktan kimin sorumlu olduğuna karar verin ve bayat bir modelin takıma yalan söylemeye devam etmesine izin vermek yerine bir modeli silmeye istekli olun.

3. **Sistemimizde hangi çekirdek, yanlışsa gerçek para kaybettirir ya da birine zarar verir ve hak ettiği titizliği alıyor mu?** Bu bölümün merkezi hamlesi yöntemi riske uydurmaktır: telafi edilebilir çoğunluk için sezgisel ve çevik yöntemler, küçük yüksek sonuçlu çekirdek için biçimsel belirtim ve doğrulama ve gerçekten belirsiz olan için ucuz prototipleme. Başarısızlık biçimleri simetriktir ve ikisi de pahalıdır: bir pazarlama mikro sitesine biçimsel yöntemler uygulamak para yakar ve bir takas motorunu ya da bir uygunluk kuralları kümesini sıradan çevik iş olarak ele almak felaket, geri döndürülemez kusuru davet eder. Sisteminizin bir haritasını getirin ve bir hatanın felaket mi yoksa telafi edilebilir mi olduğu yerleri ve gereksinimlerin kesin mi yoksa bilinmez mi olduğu yerleri işaretleyin. Cevap modelleme yatırımınızı para ve belirsizliğin olduğu yere yoğunlaştırmalı ve başka her yerde açıkça esirgemelidir; böylece kritik bir biçimsel çekirdek, yöntemlerden biri diğerinin bölgesine sızmadan aksi halde çevik bir zarfın içinde durabilir.

4. **Kod yazmadan önce ne kadar modelleme yapıyoruz ve bu doz önümüzdeki belirsizlikle değişiyor mu?** Büyük tasarımı baştan yapmak da hiç tasarım yapmamak da başarısızlık biçimleridir ve doğru doz, bir modelin gerçekte ne kadar belirsizliği giderdiğiyle yönetilen, ikisinin arasında durur. Büyük bir takımda baskı iki yöne de işler: bir yönetişim süreci herhangi bir koddan önce tam diyagram kümesi talep ederek en az bilgiyle verilmiş kararları kilitleyebilir, teslimat baskısı ise bir takımı maliyetli bir uç durumu yakalayacak tek durum makinesini atlamaya itebilir. Son iki projenizi getirin ve ürettiğiniz modelleri gerçek bir kararı bilgilendirenler ve yalnızca bir şablon istediği için çizilenler diye ayırın. Bir aşama kapısı ya da onay kurulunun çoğu zaman belgeleri baştan zorunlu kıldığı kurumsal ve kamu programlarında, sabit bir teslimat listesi yerine riski izleyen modellemeyi savunmaya hazır gelin; böylece ödeme çekirdeği titizliğini alır ve dahili raporlama aracı kimsenin okumadığı diyagramlarda boğulmaz.

5. **Ortak bir notasyon ve modellerimiz için tek bir ev üzerinde anlaştık mı, yoksa her takım kendi notasyonunu mu icat ediyor?** Modeller önce iletişim yapıtlarıdır ve bir takımın aracında çizilen bir durum makinesi, onu miras alan takım tarafından okunamadığında, bulunamadığında ya da güvenilemediğinde değerleri çöker. Yüzlerce mühendis için rakip değerlendirmeler gerçektir: zorunlu bir notasyon ve depo tutarlılık ve keşfedilebilirlik satın alır, ama aynı zamanda bir öğrenme maliyeti dayatır ve fotoğraflanmış bir beyaz tahta yeterli olacakken insanları ağır araçlara itebilir. Bir modelin gerçekte nerede yaşadığına (bir viki, bir diyagram aracı, bir slayt destesi, birinin dizüstü bilgisayarı) dair örnekler getirin ve altı ay sonra kimin onu bulup anlayabileceğini sorun. Kurumsal ve düzenlemeye tabi ortamlarda denetim açısı bunu keskinleştirir: güncel veri modelini bulamayan ya da bir kararı belgelenmiş bir durum makinesine izleyemeyen bir denetçi sistemi belgelenmemiş sayacaktır; bu yüzden küçük bir ortak notasyon ve kalıcı bir konum üzerinde anlaşın ve sonucun düşük olduğu her yerde törene karşı hafif yakalamayı kabul edin.

6. **Bir prototip inşa etmeden önce onun at-kullan mı yoksa evrimsel mi olduğuna bilerek karar veriyor muyuz ve bu seçime sadık kalıyor muyuz?** Klasik, pahalı başarısızlık, iyi gösteri yaptığı ve kimse türünü baştan adlandırmadığı için sessizce üretime kayan at-kullan bir prototiptir. Gerilim gerçektir: at-kullan prototipler mümkün olan en ucuz öğrenmeyi satın alır ve silinmelidir; evrimsel prototipler ise ürün olur ve ilk satırdan üretim standartlarında inşa edilmelidir ve ikisini karıştırmak ya yeniden işi boşa harcar ya da kırılgan kodu hiç mühendislik yapılmadığı bir role gönderir. Yakın tarihli bir prototip getirin ve inşa edilmeden önce ne kararlaştırıldığını, onu terfi ettirme ya da atma yetkisinin kimde olduğunu ve o kararın teslimat baskısından sağ çıkıp çıkmadığını sorun. Vatandaşa dönük bir sistemin şeffaflık ve güvenilirlik yükümlülükleri taşıdığı kamu ve diğer hesap verebilir ortamlarda, kazara terfiyi bir kontrol başarısızlığı olarak ele alın: prototipin kaderini önceden sabitleyin ve başarılı bir at-kullanı atmayı kaçınılacak bir israf değil, kutlanan bir sonuç yapın.

## Sektör merceği

**Girişim.** Beyaz tahtada modelleyin, fotoğrafını çekin ve devam edin. En kıt kaynağınız mühendislik dikkatidir; bu yüzden bir modele yalnızca önlediği hatadan ucuz olduğunda uzanın: faturalama uç durumlarını kodlamadan önce bir abonelik durum makinesi, gelecek ay yön değiştirebilecek bir ürün için tam bir UML kataloğu değil. Sezgisel ve çevik kalın, biçimsel yöntemleri tamamen masadan kaldırın ve her prototipi bilinçli aksine karar vermedikçe at-kullan olarak ele alın.

**Küçük işletme.** Muhtemelen işi biçimsel modelleme olan kimsenizin yoktur; bu yüzden kendi modelleme uygulamanızı kurmak yerine satın aldığınız araçlara ve çerçevelere gömülü modellere yaslanın. Çizdiğiniz birkaç modeli somut kararlar etrafında çerçeveleyin: hangi müşteri verisini tuttuğunuz konusunda anlaşmak için basit bir veri modeli taslağı, bozulduğunda müşteri kaybettiren tek iş akışı için bir durum diyagramı. Kendi veri modelinizi inşa edip belgelemek yerine kanıtlanmış veri modeline sahip satın alınmış bir ürünü tercih edin ve çizdiğiniz her şeyi tek bir kişinin sürdürebileceği kadar hafif tutun.

**Kurumsal.** Temel sorun birçok takım arasında eşgüdümdür; bu yüzden paylaşılan modeller ortak zemin olur: üzerinde anlaşılmış bir veri modeli, tutarlı bir notasyon ve VİD'nin, C4 diyagramlarının ve durum makinelerinin bulunup güvenilebileceği bir ev. Küçük bir notasyonu standartlaştırın ve tutarlılığı uygulayın; böylece gereksinimlerdeki, tasarımdaki ve veritabanındaki varlıklar takımlar arasında birbirinden uzaklaşmaz. Biçimsel belirtimi ve model denetimini yüksek sonuçlu çekirdeklere (takas, mutabakat, erişim kontrolü) saklayın, bunun gerektirdiği uzman becerisini finanse edin ve her belgelenmiş modelden haklı çıkardığı karara bir denetim izi tutun.

**Kamu.** Yasayla belirlenen kurallar kanuna izlenebilir olmalıdır; biçimsel belirtimin maliyetini çıkardığı yer burasıdır: uygunluk ya da tahakkuk mantığını kesin belirtin, kilit özellikleri doğrulayın ve denetçilerin her sonucu onu üreten kurala izlemesine izin verin. Tedarik kendi ağırlığını ekler, çünkü belgeler ve modeller çoğu zaman sözleşmesel teslimatlardır; bu yüzden hangi modellerin gerçekten karar taşıyıcı olduğuna, yalnızca bir kontrol listesini tatmin etmek için üretilmediğine karar verin. Sonuçlu sistemlerin nasıl çalıştığına dair sade dilli açıklamalar yayımlayın ve üretim inşasına geçmeden önce vatandaşa dönük girişi gerçek kullanıcılarla test etmek için at-kullan prototiplemeyi kullanın.

## Örnekler

**Girişim.** Abonelik faturalama ürünü inşa eden küçük bir girişim, kod yazmadan önce abonelik yaşam döngüsünü (deneme, etkin, gecikmiş, iptal edilmiş, yeniden etkinleştirilmiş) bir beyaz tahtada durum makinesi olarak çizer. Diyagramı yürürken, gecikmiş bir hesabın ödemesi sonunda temizlendiğinde ne olacağını hiç tanımlamadıklarını fark ederler; bu, gerçek müşterileri belirsizlikte bırakacak bir uç durumdur. O beş dakikalık model bir üretim baş ağrısını önler ve ağır bir diyagram aracını sürdürmek yerine fotoğraflarlar. Başka her yerde çevik kalır ve takımı hizalamaya yetecek kadar modellerler; çünkü onların ölçeğinde bir kusur telafi edilebilirdir ve biçimsel yöntemler saf maliyet olurdu.

**Kurumsal.** Küresel bir banka yeni bir ödeme platformu inşa eder. Takım, hesaplar, defter ve mesajlaşma takımları arasında paylaşılan veri modeli üzerinde anlaşmak için bir varlık-ilişki diyagramı ve hizmetlerin nasıl bir araya geldiğini göstermek için C4 diyagramları (bölüm 3.1) kullanır. İşlem yaşam döngüsünü (beklemede, takas edildi, uzlaştırıldı, geri alındı, itiraz edildi) açık bir durum makinesi olarak modellerler ve analiz, kısmi geri almalar için bir geçişin eksik olduğunu ortaya çıkarır. Boşluk üretimde değil bir beyaz tahtada giderilir. Sıra diyagramları, eksik zaman aşımı ve yeniden deneme yollarını ortaya çıkarmak için uzlaştırma akışını gereksinimlere (bölüm 2.8) karşı yürür. Günlük teslimat çeviktir, ama bir hatanın gerçek para kaybı anlamına geldiği çekirdek mutabakat algoritması biçimsel bir belirtim alır ve uygulamadan önce model denetiminden geçer. Modelleme para ve belirsizliğin olduğu yerde yoğunlaşır ve başka her yerde hafif tutulur.

**Kamu.** Ulusal bir vergi kurumu yardım tahakkukunu modernleştirir. Uygunluk kuralları yasayla belirlenip denetlendiği için takım kuralların biçimsel belirtimini saf dönüşümler olarak yazar ve hiçbir hak sahibinin hem uygun hem uygunsuz olmaması ve her vakanın bir karara ulaşması gibi kilit özellikleri doğrular; böylece denetçiler sonuçları kanuna izleyebilir. Biçimsel çekirdeğin yanında takım, gerçek kullanıcılarla test etmek için vatandaşa dönük giriş formunun at-kullan bir prototipini inşa eder. Çok adımlı bir sihirbazın hataları azalttığını öğrenir, sonra prototipi atar ve girişi üretim standartlarında yeniden inşa eder. Etkinlik diyagramları uçtan uca vaka işçisi sürecini eğitim ve denetim için belgeler. Yüksek sonuçlu kurallar biçimsel titizlik alır; belirsiz kullanıcı deneyimi ucuz prototipleme alır; hiçbir yöntem diğerinin ait olduğu yere uygulanmaz.

## İş gerekçesi: motivasyonlar, YG ve TSM

Modellemenin getirisi, düzeltmesi çok daha ucuz olan kusurları daha erken bulmaktan gelir. Bir beyaz tahtada bulunan çelişki dakikalara mal olur. Aynı çelişki üretimde bulunursa bir kesintiye, bir yeniden iş programına ya da düzenlenen alanlarda yasal sorumluluğa mal olabilir. Modeller ayrıca kalıcı iletişim olarak hizmet ederek toplam sahip olma maliyetini düşürür. Yazarlarından uzun yaşayan bir sistem, kurumsal ve kamuda normal durum, veri modeli, durum makineleri ve kilit akışları doğru belgelendiğinde sürdürmesi çok daha ucuzdur.

Maliyetler gerçektir ve tartmalısınız. Modellerin kurulması zaman, iyi kurulması beceri ve güncel tutulması süregelen çaba gerektirir; biçimsel yöntemler uzman emeği ekler. Başabaş noktası belirsizlik ve sonuçla yönetilir. İkisinin de düşük olduğu yerde ağır modelleme değeri yok eder ve çevik sezgiseller kazanır. Birinin yüksek olduğu yerde hedefli modelleme ve kritik çekirdek için biçimsel doğrulama, pahalı başarısızlık sınıfını önleyerek kat kat karşılığını verir. Gerekçeyi liderliğe sunmak için modelleme yatırımını giderilen belirli risklere ve uzun ömürlü sistemlerin sürdürülebilirliğine bağlayın. Ve modellere gerçekten başvurulup başvurulmadığını izleyin, çünkü kullanılmayan bir model saf maliyettir.

## Anti-kalıplar ve tuzaklar

- **Kendi iyiliği için modelleme:** bir kararı bilgilendirdikleri için değil, bir süreç talep ettiği için diyagram üretmek.
- **Gerçek diye güvenilen bayat modeller:** artık koda uymayan ama hâlâ güvenilen diyagramlar.
- **Büyük tasarımı baştan yapmak:** hiçbir koddan önce üretilen, en az bilgiyle verilmiş kararları kilitleyen kapsamlı modeller.
- **Diyagram yayılması:** her UML türünün tekdüze uygulanması; birkaç yararlı görünümü gürültüde boğmak.
- **Her yerde biçimsel yöntemler:** başarısızlığın sonucunun haklı çıkarmadığı koda pahalı doğrulama uygulamak.
- **Kazara prototip terfisi:** sessizce ürün olarak gönderilen at-kullan prototip.
- **Öz yerine notasyon:** modelin soruyu cevaplayıp cevaplamadığı yerine UML doğruluğunu tartışmak.

## Olgunluk modeli

- **Düzey 1 (Başlangıç):** Modelleme gelişigüzel ya da yoktur ve tamamen reaktiftir; adı konmuş yöntem yoktur; modeller hiç çizilirse tutarsız, analiz edilmemiş ve toplantı biter bitmez terk edilmiştir.
- **Düzey 2 (Geliştirme):** Bazı takımlar yaygın diyagramlar çizer ve adı konmuş bir yöntemi izler, ama uygulama kuruluş genelinde eşitsizdir: modeller çoğu zaman törensel üretilir, koddan sapar ve kusurlar için nadiren analiz edilir.
- **Düzey 3 (Standartlaştırma):** Paylaşılan bir notasyon, belgelenmiş bir yöntem seçim kılavuzu ve tutarlılık kuralları tanımlanır ve kuruluş genelinde uygulanır; modeller amaca göre seçilir, sistemle uyumlu tutulur, kusurlar için gözden geçirilir ve yöntem her sorunun riskine uydurulur.
- **Düzey 4 (Yönetme):** Modelleme temel çizgilere karşı ölçülür ve kontrol edilir; takımlar analizin uygulamadan önce kaç kusuru yakaladığını, modellerin koddan ne kadar saptığını, her modele gerçek bir karar için gerçekten başvurulup başvurulmadığını ve tanımlı bir temel çizgiye karşı tasarruf edilen yeniden işi ve çevrim süresini izler; yöntem seçimi ölçülen belirsizliğe ve sonuca göre kalibre edilir ve kritik çekirdekler üzerinde anlaşılmış kapsam hedeflerine karşı biçimsel doğrulanır.
- **Düzey 5 (Orkestrasyon):** Modelleme ve yöntem seçimi sürekli iyileştirilir ve kuruluş genelinde teslimat ve risk planlamasıyla bütünleşir; yatırım belirsizlik ve sonuç kaydıkça uyum sağlar, modeller kanıta dayanarak rutin olarak güncel tutulur, emekliye ayrılır ya da derinleştirilir ve biçimsel, sezgisel ve prototipleme yöntemleri her biri tam olarak karşılığını verdiği yere otursun diye bir araya getirilir.

## Tartışma fikirleri

- Son projeniz için hangi modeller gerçek bir kararı bilgilendirdi ve hangileri yalnızca bir süreç talep ettiği için çizildi?
- Sistemlerinizde biçimsel bir belirtim nerede kendini öderdi ve nerede israf olurdu?
- Bir prototipin at-kullan mı yoksa evrimsel mi olduğuna nasıl karar veriyorsunuz ve bu kararı uyguluyor musunuz?
- Modelleri koddan eşgüdümsüz kaymaktan nasıl korursunuz, yoksa bazılarının silinmesi gerektiğini mi kabul edersiniz?
- Sizin bağlamınızda koddan önce doğru modelleme miktarı nedir ve belirsizlikle nasıl değişir?
- Hangi davranışsal model (durum, sıra ya da etkinlik) en son üretim olayınızı yakalamış olurdu?

## Önemli çıkarımlar

- Bir model amaçlı bir soyutlamadır; hangi kararı bilgilendirdiğini adlandıramıyorsanız çizmeyin.
- Yapısal ve davranışsal modelleri belirli soruya uydurun ve tutarlı ve güncel tutun.
- Modelleri analiz edin; denetlenmemiş bir model test edilmemiş bir varsayımdır.
- Sezgisel ve çevik yöntemler çoğu sisteme uyar; biçimsel yöntemleri yüksek sonuçlu çekirdeklere saklayın.
- Belirsizliği gidermek için prototipleri kullanın ve baştan at-kullan mı evrimsel mi olduklarına karar verin.
- Modellemeye, çözdüğü belirsizlikle ve kararı yanlış verme maliyetiyle orantılı yatırım yapın.

## Kaynaklar ve ileri okuma

- IEEE Computer Society, *SWEBOK Guide (Software Engineering Body of Knowledge), Version 4.0*, Software Engineering Models and Methods knowledge area
- Martin Fowler, *UML Distilled: A Brief Guide to the Standard Object Modelling Language*
- Grady Booch, James Rumbaugh, Ivar Jacobson, *The Unified Modelling Language User Guide*
- Frederick P. Brooks, *The Mythical Man-Month* and *No Silver Bullet: Essence and Accident in Software Engineering*
- Daniel Jackson, *Software Abstractions: Logic, Language, and Analysis* (the Alloy modelling language)
- Leslie Lamport, *Specifying Systems* (TLA+)
- Simon Brown, *Software Architecture for Developers* (the C4 model)
- David Harel, *Statecharts: A Visual Formalism for Complex Systems*
