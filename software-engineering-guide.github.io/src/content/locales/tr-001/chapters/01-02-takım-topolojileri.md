# 1.2 Takım topolojileri ve örgütsel tasarım

## Genel bakış ve motivasyon

İnsanları takımlara nasıl böldüğünüz, hangi yazılımı inşa edebileceğinizi ve ne kadar hızlı inşa edebileceğinizi belirler. Bu bir mecaz değildir. [Conway Yasası](https://en.wikipedia.org/wiki/Conway%27s_law) olarak bilinen, neredeyse mekanik bir sonuçtur: kuruluşlar, kendi iletişim yapılarını yansıtan sistemler tasarlar. Üç takım bir [derleyici](https://en.wikipedia.org/wiki/Compiler) yazarsa, üç geçişli bir derleyici elde edersiniz. Ödeme mantığınız bir ön yüz takımı, bir arka yüz takımı ve bir veritabanı takımı arasında bölünmüşse, her ödeme değişikliği üç yönlü eşgüdüm gerektirir. Küçük bir kuruluş için bu yönetilebilirdir. Büyük bir kuruluş için organizasyon şemasının biçimi, mühendisliğiniz, mimariniz, teslimat hızınız ve kaliteniz üzerindeki baskın kısıt haline gelir. Dolayısıyla takım yapısını tasarlamak, bir İK sonradan düşüncesi değil, birinci sınıf bir mühendislik faaliyetidir.

Takım topolojileri bu tasarım için size kasıtlı bir sözcük dağarcığı verir. Yapının yeniden yapılanmalar ve kadro artışlarıyla tesadüfen birikmesine izin vermek yerine, olgun kuruluşlar takım türlerini ve etkileşim biçimlerini bilerek seçer ve sistem ile iş geliştikçe bu seçimleri yeniden gözden geçirir. Amaç, her takımın [bilişsel yükünü](https://en.wikipedia.org/wiki/Cognitive_load), yani etkili olmak için aklında tutması gereken toplam miktarı düşük tutmaktır; böylece takımlar alanlarına baştan sona sahip çıkabilir ve sürekli başkalarını beklemeden istikrarlı bir değer akışı sunabilir.

Kurumsal ve kamu kuruluşları için bu disiplin belirleyicidir. Büyük kuruluşlar doğal olarak derin hiyerarşilere, uzun kuyrukları olan paylaşılan hizmetlere ve iki günlük bir değişikliği iki aylık bir projeye çeviren devir zincirlerine doğru yayılır. Kamu, sahipliği daha da parçalayan tedarik sınırları, yüklenici takımları ve zorunlu [görev ayrılıkları](https://en.wikipedia.org/wiki/Separation_of_duties) ekler. Açık topoloji tasarımı, bu kuruluşların akışı geri kazanma yoludur: takımları değer akışlarına hizalayın, bilişsel yükü azaltan platformlar kurun ve bağımlılıkları gizli ve sürekli değil, görünür ve kasıtlı kılan etkileşim kalıpları seçin.

## Temel ilkeler

- Conway Yasası kaçınılmazdır; takımları istediğiniz yazılım mühendisliğine uyacak şekilde tasarlayın ("ters manevra").
- Bireylerin azami kullanımını değil, takım bilişsel yükünü optimize edin.
- Bir değer dilimine baştan sona sahip çıkan akışa hizalı takımları tercih edin.
- Platformlar, akışa hizalı takımların bilişsel yükünü azaltmak için vardır, kapı bekçiliği için değil.
- Takım etkileşimlerini açık ve az tutun: iş birliği, hizmet olarak X veya kolaylaştırma.
- Bağımlılıkları en aza indirin; her takımlar arası devir bir kuyruk ve bir risktir.
- Takım yapısı, sistem ve iş değiştikçe evrilmesi gereken yaşayan bir tasarımdır.

## Öneriler

### Dört temel takım türünü kullanın

Takım topolojileri, çoğu ihtiyacı karşılayan dört takım türü tanımlar. Akışa hizalı takımlar varsayılandır: her biri belirli bir ürün, hizmet ya da kullanıcı yolculuğu için sürekli bir iş akışına baştan sona sahip çıkar. Platform takımları, akışa hizalı takımların kendi kendine hizmet olarak tükettiği dahili ürünler (hesaplama, dağıtım, veri hatları, kimlik) sunar ve böylece bilişsel yüklerini azaltır. Destekleyici takımlar, akışa hizalı takımlara bir yetenek kazandırmak için koçluk yapan ve sonra geri çekilen uzmanlardır (test, güvenlik, gözlemlenebilirlik). Karmaşık alt sistem takımları, derin uzmanlık gerektiren bileşenlere (bir fiyatlama motoru, bir [video kodeği](https://en.wikipedia.org/wiki/Video_codec), bir kriptografik modül) sahip çıkar; her takımın bu bilgiyi taşımasının anlamsız olduğu yerlerde. Takımlarınızın çoğu akışa hizalı olmalıdır; diğer üç tür onları desteklemek için vardır.

### Ters Conway manevrasını uygulayın

Yazılım kuruluşunuzun yapısını yansıttığına göre, takımlarınızı istediğiniz yazılımı üretecek şekilde biçimlendirin. Net sınırları olan gevşek bağlı hizmetler mi istiyorsunuz? Net sahiplik sınırları olan gevşek bağlı takımlar oluşturun. Kendi takviminde yayımlanan bir ödeme yeteneği mi istiyorsunuz? Ona baştan sona sahip çıkan bir ödeme takımı kurun. Conway Yasası'yla kahramanca eşgüdümle savaşmayın. İstediğiniz mimari en az direnç yolu haline gelecek şekilde takım sınırlarını yeniden çizin.

### Bilişsel yükü açıkça yönetin

Bir takım yalnızca belirli bir miktarı ustalıkla kavrayabilir. Bilişsel yük; alan karmaşıklığını, teknolojileri, operasyonel yükü ve paydaşların genişliğini kapsar. Bir takım birbiriyle ilgisiz çok fazla hizmete sahip olduğunda hem kalite hem hız çöker. Bu nedenle her takımın sorumluluklarını gerçekten ustalaşabileceği bir alanla sınırlayın ve ayrışmamış karmaşıklığı tabağından almak için platformları ve destekleyici takımları kullanın. Takımları kabaca beş ila dokuz kişi arasında tutun: kolayca iletişim kurabilecek ve, deyim yerindeyse, birkaç pizzayla doyurulabilecek kadar küçük.

### Etkileşim biçimlerini bilinçli seçin

Takım etkileşimlerini üç biçimle sınırlayın. İş birliği, iki takım arasında belirli bir süre boyunca yakın, yüksek bant genişlikli çalışmadır; keşif için güçlüdür ama pahalıdır, bu yüzden geçici tutun. Hizmet olarak X, iyi tanımlanmış bir arayüze sahip temiz bir sağlayıcı/tüketici ilişkisidir; ölçekte platform tüketimi için idealdir. Kolaylaştırma, bir takımın diğerine öğrenmesinde yardım etmesidir; destekleyici takımların yaptığı şey budur. Her önemli takımlar arası ilişki için biçimi adlandırın ve aynı iki takım arasındaki uzun süreli iş birliğini, sınırlarının yanlış yerde olduğunun işareti olarak okuyun.

### Kesişen işlevler için bir işletim modeli seçin

Güvenlik, veri, tasarım ve benzeri disiplinler üç şekilde örgütlenebilir: merkezi (bir takım herkes için sahiplenir), federe (uzmanlar yarı zamanlı yerleştirilir, bir lonca aracılığıyla eşgüdüm sağlar) veya gömülü (her akışa hizalı takımın içinde özel bir uzman). Merkezi model tutarlılık ve derinlik verir ama darboğaz olur. Gömülü model hız ve bağlam verir ama tutarsızlık ve yinelenme riski taşır. Federe model (çoğunlukla bir merkez ve uç ya da [uygulama topluluğu](https://en.wikipedia.org/wiki/Community_of_practice) modeli) ikisinin arasında yer alır. İşlev ve ölçek başına seçin. Çoğu büyük kuruluş bu disiplinler için, standartları belirleyen küçük bir merkezi çekirdekle federe modele ulaşır.

### İç kaynağa yatırım yapın

[İç kaynak](https://en.wikipedia.org/wiki/Inner_source), [açık kaynak](https://en.wikipedia.org/wiki/Open-source_software) iş birliği kalıplarını kuruluşun içine getirir: paylaşılan dahili depolar, yayımlanmış katkı yönergeleri, takım sınırları boyunca [kod incelemesi](https://en.wikipedia.org/wiki/Code_review) ve net sorumlular. Bir takımın başka bir takımın bileşeninde değişikliğe ihtiyacı olduğunda, bilet açıp kuyrukta beklemek yerine değişikliği doğrudan katkı olarak sunabilir. Bu, sahipliği çözmeden takımlar arası bağımlılıkları hafifletir ve bilgiyi ve standartları büyük bir mühendislik nüfusuna doğal yoldan yayar.

## Ödünleşimler: artılar ve eksiler

| Kesişen işlevler için model | Artılar | Eksiler |
| --- | --- | --- |
| Merkezi (hepsi için tek takım) | Tutarlılık, derin uzmanlık, net standartlar | Darboğaz, kuyruklar, ürün bağlamı kaybı |
| Federe (merkez ve uç, loncalar) | Tutarlılık ile hızı dengeler; bilgiyi paylaşır | Eşgüdüm disiplini gerektirir; hesap verebilirlik bulanıklaşabilir |
| Gömülü (takım başına uzman) | Hızlı, bağlam zengini, yüksek sahiplik | Yinelenme, tutarsızlık, ölçekte kadrolaması zor |

| Takım türü | En uygun olduğu durum | Aşırı kullanılırsa risk |
| --- | --- | --- |
| Akışa hizalı | Ürün ve hizmet teslimatının çoğu | Yok; bu baskın olmalı |
| Platform | Paylaşılan bilişsel yükü azaltma | Fildişi kule kapı bekçisine dönüşür |
| Destekleyici | Bir yeteneği geçici olarak yaymak | Kalıcı bir bağımlılığa dönüşür |
| Karmaşık alt sistem | Gerçekten derin uzmanlık alanları | Sıradan işi biriktirmek için bahane olur |

Yinelenen ödünleşim özerklik ile tutarlılık arasındadır. Tam özerk takımlar hızlı hareket eder ama standartlar, araçlar ve güvenlik duruşunda birbirinden uzaklaşır. Tam merkezi kontrol işleri tutarlı tutar ama akışı boğar. İyi topoloji tasarımı dikişi bulur: akışa hizalı teslimat için özerklik, artı gerçekten tutarlı olması gereken şeyler için ince merkezi standartlar ve asfalt yol platformları (uyumlu seçimi kolay seçim yapan, iyi desteklenen varsayılan araçlar).

## Takımınızla tartışılacak sorular

1. **Kalite çökmeden önce bir takımın bilişsel yükünün çok yüksek olduğunu hangi somut sinyaller size söyleyecek?** "Her takımı ustalaşabileceği bir alanla sınırla" söylemesi kolay, kanıt olmadan harekete geçirmesi zor bir ifadedir, çünkü bilişsel yük teslimat ve güvenilirlik bozulana kadar görünmez kalır. Ölçülebilir belirtileri izleyin: bir takımın sahip olduğu birbiriyle ilgisiz hizmet ya da depo sayısı, uyumun ne kadar sürdüğü, tek bir mühendisin bir haftada bağlam değiştirmesi gereken alan sayısı ve takımın sorumluluk alanının köşelerinde artan olay oranları. Büyük bir kuruluş için bu önemlidir, çünkü aşırı yüklü takımlar hiçbir yeniden yapılanma şemasının öngörmediği darboğazlara sessizce dönüşür. Bu sayıları, ayrıca takımın kendi kafalarında neyi tutup neyi tutamayacaklarına dair hislerini tartışmaya getirin. Sinyaller aşırı yük diyorsa, hamle daha fazla kahramanlık talep etmek değil, ayrışmamış işi bir platforma ya da destekleyici takıma bırakmaktır.

2. **Burada bir yeniden yapılanma gerçekten yarattığı aksamaya değer mi, yoksa bir yeniden yapılanma bağımlılığını mı besliyorsunuz?** Ters Conway manevrasını uygulamak için sınırları yeniden çizmek güçlüdür ve her yeniden yapılanma aynı zamanda takımların kaynaşması için gereken istikrarı yok eder ve zor kazanılmış alan bilgisini sıfırlar. Karşıt değerlendirmeler, mevcut yapının süregelen eşgüdüm vergisi ile onu değiştirmenin bir kerelik maliyeti ve moral darbesidir. Kurumsal ve kamu ortamlarında tedarik sınırları, yüklenici takımları ve zorunlu görev ayrılıkları yeniden yapılanmaları daha yavaş ve pahalı kılar, bu yüzden çıta daha yüksek olmalıdır. Bağımlılık kaynaklı gecikme kanıtı getirin: kaç girişim başka bir takımı beklerken tıkanmış ve ne kadar süredir. Bu bekleme yapısal ve büyük olduğunda yeniden yapılandırın; acı geçici olduğunda ya da iç kaynak katkıları ve daha net arayüzlerle çözmek daha ucuz olduğunda yeniden dağıtmaya direnin.

3. **Güvenlik, veri ve tasarım için gömülü, federe ve merkezi arasında geçiş yapmanızı hangi olay tetikleyecek?** Bölümün önerisi işlev ve ölçek başına seçmektir ve daha zor disiplin, hangi büyümenin ya da riskin bu seçimi yeniden gözden geçirtmesi gerektiğine önceden karar vermektir. Elli mühendise uyan bir model beş yüzde darboğaza ya da tutarlılık felaketine dönüşebilir ve özellikle kurumsal ve kamu kuruluşlarının küçük bir merkezi çekirdeğin her zaman elinde tutacağı standartları adlandırması gerekir. Her işlev için mevcut kuyruk sürelerini ve tutarlılık açıklarını getirin: haftalarca inceleme kuyruğu olan merkezi bir güvenlik takımı federe etmek için bir sinyaldir, uyumsuz veri modelleri üreten gömülü uzmanlar ise merkezi bir standart çekirdeği eklemek için bir sinyaldir. Tetikleyiciye şimdiden karar verin, örneğin bir kuyruk uzunluğu eşiği ya da bir denetim bulgusu, böylece değişiklik bir kriz tepkisi değil planlı bir evrim olur. Cevap, asfalt yollara ve şampiyonlara mı yoksa merkezi bir merkeze mi yatırım yapacağınızı belirler.

4. **Platform takımınızın bilişsel yükü gerçekten düşürdüğünü mü yoksa sessizce bir kapı bekçisine mi dönüştüğünü nasıl anlayacaksınız?** Bir platform, kendi kendine hizmet yoluyla uyumlu, güvenilir seçimi kolay seçim yapmak için vardır ve aynı takım araçları dayatmaya, her isteği elle incelemeye ve ortadan kaldırmak için kurulduğu sürtünmeyi eklemeye kayabilir. Büyük bir kuruluş için bu ayrım, platform yatırımının karşılığını vermesini mi yoksa her akışa hizalı takımın arkasında kuyruk olduğu merkezi bir darboğaza dönüşmesini mi belirler. Karşıt değerlendirmeler bir yanda tutarlılık ve kontrol, diğer yanda tüketici özerkliği ve akıştır. Bir tüketicinin tanıyacağı kanıtı getirin: akışa hizalı bir takımın bilet açmadan yeni bir ortam ya da hat için kendi kendine hizmet alması ne kadar sürüyor, kendi kendine hizmet eylemlerinin insan aracılı olanlara oranı ve platformu seçen takımlarla ona zorlanan takımlar olarak ölçülen platform benimsemesi. Kurumsal ve kamu ortamlarında platformun denetim ve uyum kanıtını manuel kapılar yerine otomatik üretmesinde ısrar edin, çünkü görev ayrılığı kurallarını bir insan inceleyici ekleyerek karşılayan bir platform, çözmek için finanse edildiği darboğazı yeniden yaratmıştır.

5. **Takımlar arası ilişkilerinizden hangileri kalıcı iş birliğine yerleşti ve hangi şey her birini temiz bir hizmet arayüzüne ya da yeniden çizilmiş bir sınıra dönüştürürdü?** İş birliği biçimi yoğun ve geçici olmak üzere tasarlanmıştır ve hiç bitmeyen bir ortaklık genellikle sahipliğin yanlış yerde durduğunun ya da iki takım arasındaki arayüzün hiç açık kılınmadığının işaretidir. Bu ölçekte önemlidir, çünkü adlandırılmamış, süregelen iş birliği eşgüdüm maliyetinin saklandığı yerdir: hiçbir organizasyon şemasında görünmez, ama iki takımın dokunduğu her değişikliğe vergi koyar. Karşıt değerlendirmeler, yakın kalmanın keşif değeri ile ilişkiyi tanımlı bir arayüze sahip bir hizmet olarak X sözleşmesine dönüştürerek ya da sorumluluğu tek bir takımda birleştirerek kazanacağınız akıştır. Bir çeyrekten uzun süredir kesintisiz iş birliği yapan takım çiftlerinin listesini, son birkaç ayda her iki takımı da gerektiren değişiklikleri ve aralarında kararlı bir arayüzün yazılıp yazılamayacağını getirin. Yüklenici sınırlarının ve tedarik partilerinin bir devri yıllarca yerinde dondurabildiği kurumsal ve kamu bağlamlarında, hangi ilişkileri bir arayüz ve iç kaynak katkılarıyla dönüştürebileceğinizi ve hangilerinin sözleşmeyle sabit olduğunu ve açık bağımlılıklar olarak yönetilmesi gerektiğini adlandırın.

6. **Bir destekleyici takım başka bir takımın yetenek kazanmasına yardım ettiğinde, başarılı olduğunu ve kalıcı bir bağımlılık olmak yerine geri çekilebileceğini nasıl anlayacaksınız?** Destekleyici takımların akışa hizalı bir takıma test, güvenlik ya da gözlemlenebilirlikte ustalaşması için koçluk yapıp sonra devam etmesi beklenir ve açık bir çıkış koşulu olmadan koçluk ilişkisi, akışa hizalı takımın hiçbir zaman özümsemediği süregelen bir hizmete sertleşir. Büyük bir kuruluş için bu, bir yeteneği onlarca takıma yaymak ile her yıl daha kötü ölçeklenen yeni bir paylaşılan darboğaz yaratmak arasındaki farktır. Karşıt değerlendirmeler, uzman bir takımın sağladığı derinlik ve tutarlılık ile akışa hizalı takımlara kurmaya çalıştığınız özerklik ve baştan sona sahiplik arasındadır. Yetenek aktarımının kanıtını getirin: alıcı takım artık işi destekleyici takım olmadan yürütüyor mu, sabit bir destekleyici grup aynı anda kaç takıma bağlı ve her angajman amaçlanan devirden ne kadar uzun sürdü. Kıt bir uzman becerisinin tek bir merkezi takımın ya da tek bir sözleşmenin ardında durabildiği kurumsal ve kamu ortamlarında, uzmanlığın her denetimin ve yayının beklemek zorunda olduğu bir kuyruğun ardında kilitli kalmak yerine teslimat takımlarına yayılması için yetenek aktarımını ve şampiyonları nasıl finanse edeceğinize önceden karar verin.

## Sektör merceği

**Girişim.** Bir avuç mühendis ve az pist ile doğru topoloji, tüm ürüne sahip çıkan tek bir akışa hizalı takımdır ve disiplin, ihtiyacınız olmadan silolar yaratmayı reddetmektir. Kapı haline gelen tek bir "DevOps" ya da "QA" kişisi işe almaya direnin; bu becerileri tek takıma gömülü bir yetenek olarak katın. Organizasyonu düz tutarak Conway Yasası'nı lehinize çalıştırın, böylece mimari takım kadar basit ve değiştirilebilir kalır.

**Küçük işletme.** Özel bir platform ya da destekleyici takım kadrolamayacaksınız, bu yüzden platformu satın alın: bir iki takımınızın ayrışmamış bilişsel yükünü almak için yönetilen bulut hizmetleri, barındırılan hatlar ve hazır güvenlik araçları kullanın. Güvenlik ve veri gibi kesişen kaygıları inşa ettiğiniz bir işlev değil, yapılandırıp tükettiğiniz şeyler olarak çerçeveleyin. Özel sahipliği sizi gerçekten farklılaştıran tek karmaşık alt sisteme ayırın ve geri kalanını tedarikçilere taşıtın.

**Kurumsal.** Ölçekte sorun birçok takım arasındaki eşgüdüm maliyetidir, bu yüzden topolojiyi açık, yönetilen bir tasarım yapın: dört takım türünün paylaşılan bir sınıflandırması, adlandırılmış etkileşim biçimleri, bir asfalt yol platformu ve takımlar arası kuyrukları hafifletmek için iç kaynak. Bağımlılık kaynaklı gecikmeyi ve takım bilişsel yükünü portföy metrikleri olarak izleyin ve yeniden yapılanmaları yıllık bir refleks olarak değil, yüksek çıtayla bilinçli evrimler olarak yürütün. İnce bir merkezi çekirdek tutarlı olması gereken standartları tutarken, akışa hizalı takımlar teslimat üzerindeki özerkliğini korur.

**Kamu.** Tedarik kuralları, yüklenici sınırları ve zorunlu görev ayrılıkları sahipliği parçalar, bu yüzden topolojiyi bu kısıtları insan devirleri yerine araçlar ve net arayüzler yoluyla karşılayacak şekilde tasarlayın. Küçük bir standart çekirdeği ve denetim ile uyum kanıtını otomatik üreten bir platform ile federe modelleri tercih edin; böylece görev ayrılığı inceleme kuyrukları yerine hatlar tarafından uygulanır. Takım sınırlarını, etkileşim biçimlerini ve işletim modelini açıkça belgeleyin, böylece yapı denetçilere, gözetim organlarına ve onu finanse eden kamuya şeffaf olur.

## Örnekler

**Girişim.** On kişilik bir girişimin tüm ürüne baştan sona sahip çıkan tek bir akışa hizalı takımı vardır; bu, ölçeğinde tam da doğrudur: devir yok, eşgüdüm vergisi yok, herkes aynı bağlamı paylaşıyor. Sorun, özel bir "DevOps kişisi" ve ayrı bir "QA kişisi" işe aldıklarında ve kazara işlevsel silolar yeniden yarattıklarında başlar; artık her yayın iki kişiyi bekliyor. Bu işe alımları, işin geçmesi gereken kapılar olarak değil, tek takımın içinde gömülü bir platform ve test yeteneği olarak ele alarak yön düzeltirler. Bu boyutta en ucuz topoloji, herkesi tek bir akışta tutandır.

**Kurumsal.** Büyük bir perakendecinin ödeme akışı, ön yüz, arka yüz ve karşılama mantığı işlevsel olarak örgütlenmiş üç takım arasında bölündüğü için, her değişikliği üç iş listesinden geçirmeye zorlayarak yavaş değişiyordu. Ters Conway manevrasını uygulayarak müşteri yolculukları etrafında ("göz at", "sepet ve ödeme", "satın alma sonrası") akışa hizalı takımlara yeniden örgütlendiler; her biri diliminin baştan sona sahibi, arkalarında dağıtım ve gözlemlenebilirliği hizmet olarak sunan bir platform takımı. Eskiden bir çeyrek süren ödeme değişiklikleri günler içinde yayımlanmaya başladı, çünkü eskiden takımlar arasına yayılan eşgüdüm artık tek takımın içinde gerçekleşiyordu.

**Kamu.** Bir kamu vergi dairesi her yayını inceleyen merkezi bir güvenlik takımı çalıştırıyordu; bu, kritik düzeltmeleri geciktiren haftalarca bir kuyruk yarattı. Federe bir modele geçtiler: küçük bir merkezi güvenlik işlevi standartları belirledi ve önceden onaylı, otomatik taranan hatlardan oluşan bir "asfalt yol" sundu; her teslimat takımına yarı zamanlı gömülü güvenlik şampiyonları ise gündelik kararları ele aldı. Platform uyum kanıtını otomatik üretti. Zorunlu görev ayrılığı gereksinimleri yine karşılandı, ama bir insan darboğazı yerine araçlar ve net arayüzler yoluyla; bu, denetim hazırlığını iyileştirirken yayın bekleme süresini dramatik biçimde azalttı.

## İş gerekçesi: motivasyonlar, YG ve TSM

Kötü takım tasarımının bedelini eşgüdüm yükünde ödersiniz ve bu yük, tipik bir değişiklik için senkronize olması gereken takım sayısıyla doğrusaldan daha hızlı büyür. Her devir; bekleme süresi olan bir kuyruk, bilgi kaybeden bir bağlam aktarımı ve yanlış iletişim için yeni bir fırsattır. Rutin bir değişiklik üç takımın yol haritalarını hizalamasını gerektirdiğinde, gerçek maliyet işlerinin toplamı değil; planlamanın, beklemenin ve yeniden işin çok daha büyük maliyetidir. Sınırları çoğu değişiklik tek bir takımın sahipliğine sığacak şekilde yeniden çizin ve bu yük ortadan kalkar.

Benimseme maliyeti gerçektir. Yeniden yapılanmalar aksatıcıdır ve platformlar ve iç kaynak uygulamaları kurmak, getiri gelmeden önce başlangıç yatırımı gerektirir. Ama benimsememenin maliyeti bileşir. Yapının tesadüfen birikmesine izin veren kuruluşlar devir zincirleri, çeyrek uzunluğunda kuyrukları olan paylaşılan darboğaz takımları ve organizasyon şemasıyla fosilleşmiş mimariler biriktirir. Liderliğe gerekçeyi sunmak için bağımlılık kaynaklı gecikmeyi ölçün: kaç aktif girişim başka bir takımı beklerken tıkanmış ve ne kadar süredir. Platform ve topoloji yatırımları genellikle bu beklemeyi akışa çevirerek karşılığını verir; bu da kadro eklemeden daha kısa bekleme süreleri ve daha yüksek verim olarak görünür.

## Anti-kalıplar ve tuzaklar

- Conway Yasası'nı görmezden gelmek: organizasyon yapısının teslim edemeyeceği bir mimari tasarlamak.
- İşlevsel silolar: herhangi bir değişiklik için eşgüdüm sağlaması gereken ayrı ön yüz, arka yüz, QA ve operasyon takımları.
- Paylaşılan hizmet darboğazı: her projenin arkasında kuyruk olduğu merkezi bir takım.
- Kapı bekçisi olarak platform: hizmet etmek yerine dayatan, sürtünmeyi kaldırmak yerine ekleyen bir platform takımı.
- Bilişsel aşırı yük: ustalaşamayacakları yayılmış, birbiriyle ilgisiz sistemlere sahip takımlar.
- Kalıcı "iş birliği": birbirine sürekli dolanmış iki takım, yanlış yerleştirilmiş bir sınırın işareti.
- Yeniden yapılanma bağımlılığı: sürekli yeniden dağıtmak, takımların kaynaşması için gereken istikrarı yok etmek.

## Olgunluk modeli

- **Düzey 1, Başlangıç.** Takımlar tesadüfen, kadro sayısıyla ya da eski hiyerarşiyle oluşur; kimse takım türlerini ya da etkileşim biçimlerini adlandırmaz; işlevsel silolar ve paylaşılan hizmet darboğazları her yerdedir ve bağımlılıklar bir yayını engelleyene kadar gizli kalır.
- **Düzey 2, Geliştirme.** Bazı akışa hizalı takımlar vardır ve ilk bir platform ya da iç kaynak çabası ortaya çıkar, ancak kalıp eşitsiz uygulanır: birkaç takım dilimine baştan sona sahip çıkarken diğerleri hâlâ merkezi işlevlerin arkasında kuyruk bekler ve bilişsel yük yönetilmek yerine anekdot olarak konuşulur.
- **Düzey 3, Standartlaştırma.** Dört takım türü ve üç etkileşim biçimi belgelenmiş ve kuruluş genelinde bilinçli olarak kullanılır; platformlar ve iç kaynak takımlar arası bağımlılıkları hafifletir; güvenlik, veri ve tasarım için bir işletim modeli seçilmiş ve yazılmıştır ve yeni takımlar doğaçlamayla değil bu standartlara göre oluşturulur.
- **Düzey 4, Yönetme.** Topoloji temel çizgilere karşı ölçülür ve kontrol edilir: takımlar bilişsel yükü, bağımlılık kaynaklı gecikmeyi (başka bir takımı beklerken tıkanan girişimler ve ne kadar süredir), platform kendi kendine hizmet oranlarını ve benimsemeyi, etkileşim biçimi süresini ve bekleme süresi ile değişiklik sıklığı gibi teslimat akışı metriklerini izler. Eşikler eylemi tetikler, örneğin bir işlevi federe etmeye zorlayan bir kuyruk uzunluğu ya da yanlış yerleştirilmiş bir sınırı işaretleyen süregelen bir iş birliği; böylece kararlar görüşe değil kanıta dayanır.
- **Düzey 5, Orkestrasyon.** Takım tasarımı sürekli iyileştirilir ve mimari, ürün ve risk planlamasıyla bütünleşir; kuruluş sistem ve iş evrildikçe sınırları yeniden biçimlendirir, yetenek aktarıldığında destekleyici angajmanları sonlandırır ve bilişsel yük değiştikçe platform yatırımını yeniden dengeler; hızlı akışı tek seferlik bir yeniden yapılanma değil, uyarlanabilir, kalıcı bir özellik olarak tutar.

## Tartışma fikirleri

- Tipik bir değişiklik için kaç takımın eşgüdüm sağlaması gerekiyor ve neden?
- Hangi takımlarımız çok fazla bilişsel yük taşıyor ve bir platform ne boşaltabilir?
- Sınırları yeniden çizmek yerine Conway Yasası'yla nerede savaşıyoruz?
- Platform takımlarımız akışa hizalı takımlara hizmet mi ediyor yoksa onlara kapı bekçiliği mi yapıyor?
- Güvenlik, veri ve tasarım şu anda bizim için merkezi, federe ya da gömülü mü olmalı?
- Hangi "geçici" iş birlikleri sessizce kalıcı bağımlılıklara dönüştü?

## Önemli çıkarımlar

- Organizasyon yapısı mimariyi ve teslimat hızını belirler; onu bilinçli tasarlayın.
- Dört takım türünü kullanın; akışa hizalı varsayılan, geri kalanı destek olsun.
- İstenen mimariyi kolay yol yapmak için ters Conway manevrasını uygulayın.
- Bilişsel yükü yönetin; her takımı ustalaşabileceği bir alanla sınırlayın.
- Takımlar arası etkileşim biçimlerini sınırlayın ve adlandırın; süregelen bağımlılıkları sınır kusuru olarak ele alın.
- Kesişen işlevler için ölçek başına merkezi, federe veya gömülü modelleri seçin ve kuyrukları hafifletmek için iç kaynak kullanın.

## Kaynaklar ve ileri okuma

- Matthew Skelton and Manuel Pais, "Team Topologies: Organising Business and Technology Teams for Fast Flow"
- Melvin Conway, "How Do Committees Invent?" (the origin of Conway's Law)
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate"
- Will Larson, "An Elegant Puzzle: Systems of Engineering Management"
- Sam Newman, "Building Microservices" (on aligning services to teams)
- Danese Cooper and Klaas-Jan Stol, "Adopting InnerSource," and the InnerSource Commons patterns
- Frederick Brooks, "The Mythical Man-Month" (communication overhead)
