# 10.7 Çeviklik

## Genel bakış ve motivasyon

[Çeviklik](https://en.wikipedia.org/wiki/Agile_software_development), yazılımı (ve değeri) yinelemeli, artımlı olarak ve onu kullanacak insanlarla yakın iş birliği içinde teslim etmeye yönelik bir zihniyettir. 2001 tarihli *Manifesto for Agile Software Development* ile kodlanmıştır ve bir süreç olarak değil, bir **değerler ve ilkeler** kümesi olarak anlaşılması en doğrusudur: kendilerinden önce gelen plan ağırlıklı, sözleşme ağırlıklı, belge ağırlıklı varsayılanlara karşı bireylere ve etkileşimlere, çalışan yazılıma, müşteri iş birliğine ve değişime yanıt vermeye öncelik verin. [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development)), [Kanban](https://en.wikipedia.org/wiki/Kanban_(development)) ve [Aşırı Programlama](https://en.wikipedia.org/wiki/Extreme_programming) (XP) gibi çerçeveler bu zihniyetin *uygulamalarıdır*. Yararlı başlangıç noktalarıdır, ama zihniyetin kendisi değildir. Bu bölüm, yöntemleri geniş biçimde tarayan bölüm 1.4'ü (çalışma biçimleri) tamamlar ve özellikle Çeviklik'e derinlemesine girer.

Çeviklik, keşif ve teslimat hatlarına (bölümler 11.1–11.2) can veren aynı güçle yönlendirilir: yazılım gereksinimleri baştan tam olarak bilinmez, *keşfedilir* ve dünya uzun bir planın emebileceğinden hızlı değişir. Büyük patlama, önce her şeyi planla teslimatı defalarca geç, bütçeyi aşan ve en kötüsü yanlış sistemler üretir; çünkü tüm öğrenme, harekete geçmenin en pahalı olduğu sonda gelir. Çevikliğin temel bahsi basittir: gerçek, çalışan yazılım inşa edip gerçek geri bildirim almanın kısa döngüleri, spekülasyonun uzun döngülerinden iyidir. İyi yapıldığında riski ertelemek yerine sürekli azaltır.

Büyük takımlar, kurumlar ve kamu için Çeviklik hem güçlü hem de sık sık çarpıtılmıştır. Kurumlar onu yüzlerce takıma yayar ve çoğu zaman kararların nasıl verildiğini ya da değerin nasıl ölçüldüğünü değiştirmeden ritüele indirger ("artık günlük toplantı yapıyoruz"). Hükümet Çevikliği bilinçli olarak benimsemiştir, çünkü yinelemeli, kullanıcı merkezli teslimat büyük kamu programlarının riskini gösterilebilir biçimde azaltır: U.S. Digital Service ve *Digital Services Playbook*'u, Birleşik Krallık'ın Government Digital Service'i ve Service Standard'ı ve çevik satın alma reformlarının hepsi kısmen yüksek profilli [şelale](https://en.wikipedia.org/wiki/Waterfall_model) başarısızlıklarına yanıt olarak ortaya çıktı. Ödül gerçektir. "Yalnızca adıyla çevik" başarısızlık biçimi de öyle.

## Temel ilkeler

- **Manifesto'nun dört değerine** (insanlar, çalışan yazılım, iş birliği ve duyarlılık) süreç ürünlerinden daha çok değer verin.
- **Çalışan yazılımı sık sık** küçük artımlarla teslim edin; çalışan yazılım ilerlemenin birincil ölçüsüdür.
- **Değişikliği karşılayın**, geç olsa bile; uyarlanabilirlik bir özelliktir, başarısızlık değil.
- **Motive, yetkili, kendi kendini örgütleyen takımlar etrafında inşa edin.**
- **Kullanıcılar ve paydaşlarla sürekli iş birliği yapın.**
- **Düzenli bir ritimle düşünün ve iyileştirin.**
- **İnsani bir tempoyu** ve teknik mükemmelliği sürdürün: zanaatsız hız çöker.

## Öneriler

### Törenlere değil, değerlere ve ilkelere dayanın

En önemli tek Çeviklik önerisi *neden* ile başlamaktır. Günlük toplantı, sprint gözden geçirmesi ve retrospektif yapan, ama yine de sabit bir tarihte sabit kapsama söz veren, kötü haberi saklayan ve planı hiç değiştirmeyen bir takım çevik değildir. Toplantılı şelaledir. Gerçek çeviklik için on iki ilkeyi kontrol listesi olarak kullanın. Sık sık çalışan yazılım teslim ediyor musunuz? Bir sonraki iterasyonda bir değişikliği karşılayabilir misiniz? İşin *nasıl* yapılacağına takım mı karar veriyor? Müşteri gerçekten döngüde mi? Törenler bu sonuçları üretmiyorsa törenleri değil, sonuçları düzeltin.

### Bir çerçeveyi başlangıç noktası olarak seçin, din olarak değil

İşe uyan bir çerçeve seçin ve onu uyarlayın:

- **Scrum:** zaman kutulu sprintler, öncelikli bir iş listesi ve tanımlı roller (ürün sahibi, scrum master, geliştiriciler). Net bir ürün sahibi olan özellik teslimatı için iyi; iş yüksek ölçüde kesinti güdümlü olduğunda zayıf.
- **Kanban:** açık devam eden iş (WIP) sınırları ve çekme sistemiyle sürekli akış. Destek, operasyon ve öngörülemeyen varış için iyi (ve doğrudan akış ve kuyruk kuramına dayanır, bkz. bölümler 11.2, 11.3). WIP'yi sınırlamak teslim süresini kısaltır ([Little Yasası](https://en.wikipedia.org/wiki/Little%27s_law)).
- **Aşırı Programlama (XP):** [test güdümlü geliştirme](https://en.wikipedia.org/wiki/Test-driven_development), [eşli programlama](https://en.wikipedia.org/wiki/Pair_programming), [sürekli entegrasyon](https://en.wikipedia.org/wiki/Continuous_integration), yeniden düzenleme ve küçük sürümler dahil mühendislik uygulamaları. Her çerçeveyi sürdürülebilir kılan teknik omurga.
- **Scrumban** ve karışımlar: birçok olgun takımın yöneldiği pragmatik birleşimler.

Çerçeveler iskeledir. İşe yarayanı tutun, yaramayanı bırakın ve "çerçeve öyle diyor"un "ilkeler nedenini söylüyor"u asla geçersiz kılmasına izin vermeyin.

### Teknik mükemmelliği şart koşun

Mühendislik disiplini olmayan Çeviklik hızla bakımı yapılamaz kodun hızlı üretimine, "karanlık scrum"a dönüşür; takımlar kendilerini kusurların ve [teknik borcun](https://en.wikipedia.org/wiki/Technical_debt) katran çukuruna doğru sprint atar. XP uygulamaları isteğe bağlı ekstralar değildir. Sürekli entegrasyon (bölüm 8.1), otomatik test (bölüm 2.4), yeniden düzenleme, gövde tabanlı geliştirme (bölüm 2.6) ve temiz tasarım (bölüm 2.2), bir takımın yazılımı ucuza değiştirmeye devam etmesini sağlayan şeylerdir ve bu, çevikliğin bütün öncülüdür. Sürdürülebilir tempo aynı nedenle önemlidir: tükenmiş takımlar kaliteyi ya da duyarlılığı sürdüremez.

### Ölçeklemeyi dikkatle yapın ve ölçeği küçültmeyi tercih edin

SAFe (Scaled Agile Framework), LeSS, Nexus ve Scrum@Scale gibi ölçekleme çerçeveleri birçok takımı ortak hedeflere doğru koordine eder. Yardımcı olabilirler, ama bir uyarı taşırlar (bölüm 1.4'ü yankılayarak): ağır ölçekleme çerçeveleri çoğu zaman Çevikliğin kaldırmak istediği komuta-kontrol ve plan ağırlıklı ek yükü yeniden getirir. Büyük bir çerçeve benimsemeden önce *ölçeği küçültmeyi* deneyin. Baştan daha az koordinasyon makinesine ihtiyaç duymak için net sahipliği ve asgari takımlar arası bağımlılığı olan bağımsız, akışa hizalı takımlar etrafında örgütlenin (bölüm 1.2). Koordinasyonun gerçekten gerektiği yerde işe yarayan en hafif yapıyı ekleyin ve onu çıktıya değil, sonuçlara (OKR'ler, hedefler ve anahtar sonuçlar, bölüm 11.1) bağlayın.

### Çevikliği kurumsal ve kamuda gerçek kılın

Uyarlanabilir teslimat ve kurumsal kısıtlar bir arada var olabilir, ama bilinçli tasarım gerektirir:

- **Melez yönetişim:** öngörülü bir finansman/uyum kabuğunun (bölüm 10.6) içinde uyarlanabilir bir teslimat çekirdeği; böylece iterasyon denetimle savaşmak yerine onu tatmin eder.
- **Çevik satın alma:** tek bir sabit kapsamlı mega sözleşme yerine modüler, sonuç tabanlı sözleşmeler ve daha kısa artımlar; kamu sektörü Çevikliğinin en sık başardığı ya da başarısız olduğu yer burasıdır.
- **Yürürken uyum:** denetimi, erişilebilirliği (bölüm 5.3) ve güvenliği (bölüm 4.1) geç bir kapı yerine otomasyon ve uygunluk işlevleriyle (mimari ve kalite özelliklerini sürekli doğrulayan otomatik kontroller; bölümler 8.5, 1.6) artıma yerleştirin.
- **Gerçek kullanıcı erişimi:** en zor ve en önemlisi. Takımların vatandaşlar ya da müşterilerle gerçek temasa ihtiyacı vardır ve satın alma ile güvenlik kuralları çoğu zaman buna engel olur.

### Sürekli iyileştirin ve ciddi olun

Retrospektif Çevikliğin iyileştirme motorudur ve hiçbir değişiklik üretmiyorsa değersizdir. Az sayıda somut, sahipli eylem üreten retrospektifler yürütün ve bir sonrakinden önce bunları gerçekten tamamlayın. Sonuçları (değişiklik bir anahtar sonucu hareket ettirdi mi? bkz. bölüm 11.1) ve akışı (teslim süreleri kısalıyor mu? bkz. bölümler 11.2, 11.3) ölçün. Hızı ölçmeyin: bir kapasite sinyalidir ve onu üretkenlik hedefi olarak kullandığınız anda bir yalana dönüşür.

## Ödünleşimler: artılar ve eksiler

| Karar | Artılar | Eksiler |
|---|---|---|
| **Çevik (uyarlanabilir)** | Hızlı geri bildirim; değişikliği içine alır; erken, sürekli değer | Kapsam ve maliyeti baştan sabitlemek daha zor; ilgili müşteri ve disiplin ister |
| **Şelale (öngörülü)** | Öngörülebilir kapsam; sözleşme/denetim dostu | Geç geri bildirim; büyük patlama riski; belirsiz gereksinimlere kötü uyum |
| **Scrum** | Ritim, roller, odak; yaygın biçimde anlaşılır | Tören ek yükü; kesinti güdümlü işle zorlanır |
| **Kanban** | Akış, WIP sınırları, esnek; operasyon için harika | Daha az yapı; sınırları tutmak için disiplin gerekir |
| **Ağır ölçekleme (SAFe)** | Birçok takımı koordine eder; büyük kurumlara tanıdık | Komuta-kontrolü yeniden getirebilir; tören ağır |
| **Ölçeği küçültme / takım özerkliği** | Daha az koordinasyon ek yükü; daha hızlı takımlar | Düşük bağlaşım ve güçlü platform/sahiplik gerektirir |

Tanımlayıcı gerilim **uyarlanabilirlik ile öngörülebilirlik** arasındadır ve klasik yanlış okuma Çevikliğin "plan yok" demek olduğudur. Öyle değil. Sürekli planlamak ve *kapsamın* esnemesine izin verirken *sonuçlara ve ritme* söz vermek demektir. Diğer yinelenen tuzak, Çevikliği *yalnızca* süreç (törenler) ya da *yalnızca* mühendislik (XP) olarak görmektir. İkisine de ihtiyaç vardır.

## Takımınızla tartışılacak sorular

1. **Kurumsal ya da kamu bağlamınızda sözleşmeleriniz modüler ve sonuç tabanlı mı, yoksa teslimat tek bir sabit kapsamlı mega sözleşmenin içine mi kilitli?** Çevik satın alma, kamu sektörü çevikliğinin en sık başardığı ya da başarısız olduğu yerdir; çünkü tek bir sabit fiyatlı, sabit kapsamlı sözleşme, teslimat takımları toplantılarına ne derse desin şelaleyi zorunlu kılar. Daha kısa artımlı modüler, sonuç tabanlı sözleşmeler, kapsamın sabit finansman içinde değerli bir çekirdeğe esnemesine izin verir; bu da modern kamu başarılarının ardındaki kalıp ve geçmiş büyük patlama başarısızlıklarının panzehiridir. Kanıt getirin: mevcut sözleşmelerinize bakın ve bir tedarikçinin gösterilmiş çalışan yazılım için mi yoksa yıllar önce onaylanmış sabit bir kapsam için mi ödendiğini sorun. Cevap, bir sonraki satın almayı yapılandırma biçiminizi, takımlarınızın dahilen hangi çerçeveyi benimsediğinden çok daha fazla şekillendirmelidir. Sözleşmeniz uzak, ya hep ya hiç bir devreye almayı zorunlu kılarken teslimatta uyarlanabilir olamazsınız.

2. **Denetim, erişilebilirlik ve güvenlik her artıma otomasyonla mı yerleştiriliyor, yoksa geç bir kapı olarak mı ekleniyor?** Yürürken uyum, uyarlanabilir teslimatın kurumsal kısıtlarla bir arada var olmasını sağlayan şeydir: kontrolleri, sürüm öncesi telaş için saklamak yerine otomasyon ve uygunluk işlevleriyle artıma yerleştirin. Geç bir uyum kapısı Çevikliğin kaldırmak için var olduğu büyük patlama riskini yeniden getirir, çünkü pahalı sorunlar düzeltmenin en zor olduğu sonda yüzeye çıkar. Kanıt getirin: son artımınız için erişilebilirlik, güvenlik ve denetim kanıtının hatta otomatik olarak mı doğrulandığına yoksa lansmandan önceki manuel bir incelemeye mi ertelendiğine bakın. Cevap bu özellikleri sürekli otomatik kontrollere itmeli; böylece denetim ayrı bir aşamayla değil, inşa etme eylemiyle tatmin edilir. Bu aynı zamanda düzenlemeye tabi bir programı yalnızca denetimden önceki haftalarda değil, denetimler arasında da dürüst tutar.

3. **Takımlarınızın teknik borca doğru sprint attığını nasıl anlarsınız ve lansman baskısı altında sürdürülebilir tempoyu ne korur?** Mühendislik disiplini olmayan Çeviklik, takımların kusurların ve bakımı yapılamaz kodun katran çukuruna hızla sprint attığı karanlık scruma dönüşür ve tükenmiş takımlar kaliteyi ya da duyarlılığı sürdüremez. XP uygulamaları (sürekli entegrasyon, otomatik test, yeniden düzenleme, gövde tabanlı geliştirme) bir takımın yazılımı ucuza değiştirmeye devam etmesini sağlayan şeylerdir ve bu çevikliğin bütün öncülüdür; bu yüzden bir tarih yaklaşırken feda edilecek isteğe bağlı ekstralar değildir. Kanıt getirin: teslim sürelerinin kısalıp kısalmadığını, kusur oranlarının tırmanıp tırmanmadığını ve takımın her sprinti tutturmak için sessizce daha uzun saatler çalışıp çalışmadığını izleyin. Cevap teknik mükemmelliği ve insani tempoyu tartışılmaz kılmalıdır; çünkü zanaattan ödün vererek satın alınan hız birkaç iterasyonda çöker. Akışı ve sonuçları ölçün, hızı asla hedef olarak ölçmeyin; çünkü bir kapasite sinyalini üretkenlik hedefi yaptığınız anda yalana dönüşür.

4. **Ağır bir ölçekleme çerçevesine uzanmadan önce, koordine etme ihtiyacını baştan yaratan takımlar arası bağımlılıkları azaltmayı denediniz mi?** Bu en çok büyük bir kurum için önemlidir; çünkü birçok takımın birlikte yayın yapması gerektiğinde refleks SAFe, LeSS ya da Scrum@Scale gibi bir çerçeve almaktır ve ağır ölçekleme makinesi çoğu zaman Çevikliğin kaldırmak için var olduğu komuta-kontrol ve plan ağırlıklı ek yükü geri sokar. Rakip değerlendirme gerçektir: bir miktar koordinasyon gerçekten gereklidir ve bağımsız, akışa hizalı takımlara ölçeği küçültmek düşük bağlaşım, net sahiplik ve takımların kendi kendine hizmet almasına izin verecek kadar olgun bir platform ister; henüz buna sahip olmayabilirsiniz. Tartışmaya kanıt getirin: takımların birbirini beklemesine yol açan gerçek bağımlılıkları haritalayın ve takım sınırlarının ve hizmet sahipliğinin bilinçli bir yeniden tasarımından kaçının hayatta kalacağını sorun. Düzinelerce takımlık bir organizasyon şemasının yaygın olduğu kurumsal ve kamu programlarında dürüst soru, hiç koordinasyona ihtiyaç duymamak için basitleştirebileceğiniz bir mimari ve takım tasarımını telafi etmek üzere koordinasyon yapısı ekleyip eklemediğinizdir.

5. **Takımlarınızın inşa ettikleri vatandaşlarla ya da müşterilerle gerçek, tekrarlanan teması var mı, yoksa geri bildirim vekiller aracılığıyla süzülerek mi geliyor?** Müşteri iş birliği Manifesto'nun dört değerinden biridir ve gerçek kullanıcı teması olmayan iterasyonlar sessizce yanlış şeyi optimize eder; bu, Çevikliğin önlemesi gereken en pahalı başarısızlıktır. Gerilim şudur: doğrudan erişimi ölçekte düzenlemek zordur ve çoğu zaman büyük ve kamu kurumlarının uyması gereken satın alma, gizlilik ve güvenlik kurallarınca engellenir; bu yüzden kolay yol bir vekil koymaktır: bir iş analisti, bir paydaş komitesi ya da geçen çeyreğin araştırma sunumu. Kanıt getirin: son birkaç artımınız için kaçının yazılımı gerçekten kullanan gerçek bir kullanıcıyla doğrulandığını ve kaçının birinin kullanıcıların ne istediğine dair görüşüne dayandığını sayın. Bir kamu hizmeti için, kullanılabilirlik testinizin en çok etkilenen insanlara, yardımcı teknoloji kullanıcıları ve düşük dijital güvene sahip olanlar dahil, ulaşıp ulaşmadığını ekleyin; çünkü yalnızca kendinden emin çoğunluk için çalışan bir kamu hizmeti, her tören zamanında yapılmış olsa bile hesap verebilirlik yükümlülüğünde başarısız olmuştur.

6. **Takımlarınız sonuçlar ve ritim etrafında mı finanse edilip yönetiliyor, yoksa törenlerin ardında sessizce şelaleyi zorlayan sabit bir kapsam etrafında mı?** Bu, gerçek çeviklik ile sahte çeviklik arasındaki farktır ve takımın üstünde, paranın nasıl serbest bırakıldığında ve başarının nasıl raporlandığında karara bağlanır; günlük toplantıların yapılıp yapılmadığında değil. Rakip çekim, finans, portföy ve denetim işlevlerinin yıllar önceden sabit bir bütçeye karşı sabit bir kapsamı onaylamak üzere kurulmuş olması ve onlardan esnek kapsamlı bir sonucu finanse etmelerini istemenin, direneceği bir denetim kaybı gibi hissettirmesidir. Kanıt getirin: mevcut bir girişimin nasıl finanse edildiğini ve neyi raporladığını izleyin ve takımların teslim edilen sonuçlar ve akış üzerinden mi yoksa hikâye puanları ve uzun zaman önce onaylanmış bir kapsama bağlılık üzerinden mi ölçüldüğünü kontrol edin. Kurumsal ve kamu ortamlarında bunu doğrudan finansman ve uyum kabuğuna (bölüm 10.6) bağlayın: para uzak, ya hep ya hiç bir devreye almaya taahhüt edilmişse, takımlar ritüelleri ne kadar sadık biçimde icra ederse etsin uyarlanabilir olamaz ve çözüm teslimat takımlarına değil, yönetişim modeline aittir.

## Sektör merceği

**Girişim.** Değerleri yaşayın ve çerçeve tartışmasını atlayın. Her hafta gerçek kullanıcılara çalışan bir dilim yayınlayın, geri bildirimin günlük gelmesi için kurucuların ve ilk müşterilerin yeterince yakınında oturun ve kanıt mevcut bahsin yanlış olduğunu söylediği anda bir yön değişikliğini karşılayın. En kıt kaynağınız mühendislik dikkatidir; bu yüzden lansman baskısı altında bile teknik mükemmelliği (sürekli entegrasyon, otomatik testler, gövde tabanlı geliştirme) koruyun, çünkü gelecek hafta ucuza yön değiştirebilmenizi sağlayan o disiplindir.

**Küçük işletme.** Çeviklik koçunuz ve dar bir bütçeniz yok; bu yüzden Çevikliği kadro tutacağınız bir dönüşüm programı olarak değil, bir avuç alışkanlık olarak ele alın: kısa haftalık bir döngü, WIP sınırlı görünür bir pano ve her hafta gerçekten bitirdiğiniz tek bir somut iyileştirme. Az törene ihtiyaç duyan ve kesinti güdümlü işe uyan Kanban'a yaslanın ve ağır bir süreç kurmak yerine zaten satın aldığınız araçlara gömülü uygulamaları benimseyin. Çabayı Scrum'ı ne kadar yakından taklit ettiğinizle değil, müşterilere yararlı yazılımı daha sık yayınlayıp yayınlamadığınızla yargılayın.

**Kurumsal.** Sorun, komuta-kontrolü yeniden getirmeden birçok takımı koordine etmektir. Ağır bir ölçekleme çerçevesi benimsemeden önce ölçeği küçültmeyi, yani akışa hizalı takım tasarımı ve sağlam bir platformla takımlar arası bağımlılıkları azaltmayı tercih edin. Sabit yıllık kapsam ve hikâye puanları yerine sonuçlar (OKR'ler) ve ritim etrafında finanse edip yönetin, XP tarzı mühendislik uygulamalarını takımlar boyunca tartışılmaz yapın ve gruplar ritüel yerine kanıtla iyileşsin diye teslimatı akış metrikleri ve sonuç ölçüleriyle bir portföy olarak yönetin.

**Kamu.** Satın alma kuralları, şeffaflık ve kamusal hesap verebilirlik her tercihi şekillendirir. Tek bir sabit kapsamlı mega sözleşme yerine daha kısa artımlı modüler, sonuç tabanlı sözleşmeler yapılandırın; çünkü çevik satın alma, kamu sektörü çevikliğinin en sık başardığı ya da başarısız olduğu yerdir. Denetimi, erişilebilirliği ve güvenliği her artıma otomasyonla yerleştirin; böylece denetim inşa etme eylemiyle tatmin edilir, ilerlemeyi ve kamusal değer kanıtını denetim organlarına yayımlayın ve her iterasyonda vatandaşlara (yardımcı teknoloji kullanıcıları dahil) gerçek erişim için mücadele edin; çünkü en sık pazarlıkta feda edilen kısıt budur.

## Örnekler

**Girişim.** Beş kişilik bir girişim tören tartışmasını atlar ve Çeviklik değerlerini doğrudan yaşar. Her hafta gerçek kullanıcılara çalışan bir dilim yayınlar, geri bildirimin günlük gelmesi için kurucuların ve ilk müşterilerin yeterince yakınında oturur ve kanıt mevcut bahsin yanlış olduğunu söylediğinde gelecek hafta bir yön değişikliğini karşılar. Takım teknik mükemmelliği hız için takas etmeyi reddeder; bu yüzden sürekli entegrasyon, otomatik testler ve gövde tabanlı geliştirme lansman baskısı altında bile tartışılmazdır ve her Cuma retrospektifi, takımın bir sonrakinden önce gerçekten bitirdiği tek bir somut değişiklik üretir. Hızı asla hedef olarak izlemez; bunun yerine yayınlanan işin aktivasyonu hareket ettirip ettirmediğini ve teslim sürelerinin kısalıp kısalmadığını ölçer.

**Kurumsal.** 60 takımlı bir telekomun dönüşümü başta "Scrum yapar" ama iyileşme görmez. Takımlar hâlâ sabit yıllık kapsam alır ve hız üzerinden raporlar. Bir sıfırlama ilkelere yeniden odaklanır: üç aylık OKR'ler özellik zorunluluklarının yerini alır, takımlar takımlar arası bağımlılıkları azaltmak için yeniden örgütlenir (ölçeği küçültme) ve XP uygulamaları (SE, TDD, gövde tabanlı geliştirme) tartışılmaz yapılır. Teslim süreleri düşer, kusurlar azalır ve en önemlisi iş, hikâye puanları yerine sonuçları ölçmeye başlar; böylece Çevik teslimatı keşif hattına bağlar (bölüm 11.1).

**Kamu.** Bir dijital hizmet takımı, vatandaşa dönük bir yardım başvurusunu melez bir yönetişim kabuğu içinde Çeviklikle yeniden inşa eder: çalışan, kullanıcıyla test edilmiş yazılım teslim eden iki haftalık artımlar; her artıma yerleştirilmiş erişilebilirlik ve güvenlik; ve tek bir sabit fiyatlı sözleşmenin yerini alan modüler satın alma. Her iterasyonda vatandaşlarla (yardımcı teknoloji kullanıcıları dahil) yapılan gerçek kullanılabilirlik testi, eski şelale sürecinin yayınlayacağı sorunları yakalar. Program kullanılabilir bir hizmeti erken teslim eder ve denetim organlarına ölçülebilir kamusal değer gösterir. Bu, modern kamu sektörü başarılarının ardındaki kalıptır ve geçmiş büyük patlama başarısızlıklarının panzehiridir.

## İş gerekçesi: motivasyonlar, YG ve TSM

Çevikliğin getirisi **risk azaltma ve daha hızlı değer gerçekleştirmeden** gelir. Çalışan yazılımı erken ve sık teslim ederek takımlar belirsizliği sürekli kanıta çevirir; yanlış şey ve işe yaramaz başarısızlıklarını uzak, pahalı bir devreye alma yerine ucuzken yakalar. Modern teslimatın ardındaki araştırma (DORA, [DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment) bulguları, bölüm 11.2), Çevikliğin teşvik ettiği uygulamaların (küçük partiler, sık sürümler, hızlı geri bildirim, teknik mükemmellik) daha iyi teslimat *ve* istikrar *ve* kurumsal performansla ilişkili olduğunu gösterir. Erken artımlar da değer getirmeye daha erken başlar ve sonuna kadar hiçbir şey getirmeyen büyük patlama sürümüne göre YG'nin zamanlamasını ve toplam büyüklüğünü iyileştirir.

**[Toplam sahip olma maliyetinde](https://en.wikipedia.org/wiki/Total_cost_of_ownership)**, mühendislik disiplini gerçekse Çeviklik, bir sistemin ömrü boyunca değişikliğin maliyetini düşürür. Başlıca riski *sahte çeviklik*tir: ilkesiz ya da zanaatsız tören, toplantı ek yükü ekler ve hiçbir faydayı teslim etmez, hatta dürüst bir şelaleden daha kötü olabilir. Yani iş gerekçesi koşulludur. Çevikliği zihniyet artı mühendislik olarak benimsediğinizde YG yüksektir, ritüel olarak benimsediğinizde kabaca sıfırdır (ya da negatif). Liderliğe gerekçeyi Çevikliği "daha hızlı gitmek" olarak değil, sürekli risk azaltma ve sonuç ölçümü olarak çerçeveleyerek ve yatırımın yalnızca yeni toplantıları değil, teknik uygulamaları da içermesinde ısrar ederek sunun.

## Anti-kalıplar ve tuzaklar

- **Sahte / kargo kültü çeviklik:** kararlar, finansman ve zihniyet şelale kalırken yapılan törenler.
- **Üretkenlik olarak hız:** bir kapasite tahminini hedefe çevirmek, onu bozar ([Goodhart Yasası](https://en.wikipedia.org/wiki/Goodhart%27s_law)).
- **Karanlık scrum:** teknik mükemmellik olmadan bakımı yapılamaz, kusurlarla dolu koda doğru sprint atmak.
- **Değişiklik üretmeyen retrospektifler:** tamamlanmış hiçbir eylem üretmeyen düşünme.
- **Sabit kapsam *ve* tarih *ve* maliyet:** kalite baskıyı sessizce emerken buna çevik demek.
- **Yok müşteri:** gerçek kullanıcı geri bildirimi yok, bu yüzden iterasyonlar yanlış şeyi optimize eder.
- **Çerçeve tapınması:** "SAFe/Scrum öyle diyor"un ilkeleri ve takımın yargısını geçersiz kılması.
- **Ölçeği küçültmeden ölçeklemek:** bağımlılıkları azaltmak yerine ağır koordinasyon çerçeveleri eklemek.

## Olgunluk modeli

- **Düzey 1, Başlangıç.** Şelale ya da gelişigüzel teslimat; büyük patlama sürümleri; iş tepkisel ve plan ağırlıklı, yinelemeli geri bildirim yok ve Çevikliğin neden yardımcı olabileceğine dair paylaşılan bir anlayış yok.
- **Düzey 2, Geliştirme.** Birkaç takım Çevik törenleri (günlük toplantılar, sprintler, retrospektifler) benimser, ama uygulama kurum genelinde tutarsızdır: zihniyet ve mühendislik disiplini ritüellerin gerisinde kalır, hız çıktı olarak ele alınır ve kapsam hâlâ baştan sabittir.
- **Düzey 3, Standartlaştırma.** Değerler ve ilkeler kurum genelinde işi gerçekten yönlendirir, belgelenmiş ve her takımdan beklenir: XP tarzı teknik mükemmellik (SE, otomatik test, yeniden düzenleme, gövde tabanlı geliştirme) standart uygulamadır, takımlar kendi kendini örgütler, müşteriler her iterasyonda dahil edilir ve retrospektifler somut, tamamlanmış değişiklik üretir.
- **Düzey 4, Yönetme.** Teslimat temel çizgilere göre ölçülür ve denetlenir: takımlar teslim süresini, devreye alma sıklığını, değişiklik başarısızlık oranını ve kusur kaçış oranını (DORA tarzı akış ve istikrar metrikleri), anahtar sonuçlara bağlı sonuç ölçüleriyle birlikte izler ve her birini bilinen bir temel çizgiyle karşılaştırır. Retrospektif eylemleri tamamlanana kadar izlenir, fazla mesai ve tükenmişlik gibi sürdürülebilir tempo sinyalleri gözlenir ve hız asla üretkenlik hedefi olarak kullanılmaz. Gidilir ya da gidilmez kararları görüşe değil, bu kanıta dayanır.
- **Düzey 5, Orkestrasyon.** Uyarlanabilir teslimat kurum genelinde iş ve risk planlamasıyla bütünleşiktir: sonuçlar (OKR'ler) finansmanı ve ritmi yönlendirir, düşük bağımlılıklı takım tasarımı (ölçeği küçültme) koordinasyon ek yükünü en aza indirir ve melez yönetişim teslimatı yavaşlatmadan denetimi tatmin eder. Sürekli iyileştirme törensel değil kültüreldir ve kurum kanıt ve risk tablosu değiştikçe portföyünü rutin olarak yeniden kapsamlandırır, yeniden takımlandırır ve yeniden dengeler.

## Tartışma fikirleri

1. Takımınızı on iki Çevik ilkeye göre puanlayın: nerede törende çeviksiniz ama özde değilsiniz?
2. Takımınızda hız bir öngörü olarak mı yoksa bir hedef olarak mı kullanılıyor ve bu davranışa ne yaptı?
3. Hangi XP teknik uygulamaları eksik ve yokluğu kusurlar ya da yavaş değişiklik olarak nasıl ortaya çıkıyor?
4. Bir ölçekleme çerçevesi benimsemeden önce, bunun yerine takımlar arası bağımlılıkları azaltabilir miydiniz?
5. Sizin bağlamınızda her iterasyonda gerçek kullanıcı erişimini özellikle ne engelliyor ve bunu nasıl kaldırabilirsiniz?
6. Bir retrospektifin gerçekten ürettiği son somut değişiklik neydi?

## Önemli çıkarımlar

- Çeviklik, bir tören kümesi değil, **değerler ve ilkelerden oluşan bir zihniyettir**; çerçeveler başlangıç noktasıdır, amaç değil.
- **Çalışan yazılımı sık sık** teslim edin, değişikliği karşılayın ve **kendi kendini örgütleyen takımları** güçlendirin.
- **Teknik mükemmellik (XP uygulamaları) tartışılmazdır.** Onsuz çeviklik hızlı çürümeye dönüşür.
- **Dikkatle ölçekleyin; ölçeği küçültmeyi tercih edin.** Koordinasyon çerçeveleri eklemeden önce bağımlılıkları azaltın.
- Kurumsal/kamuda **uyarlanabilir teslimatı melez yönetişim ve çevik satın almayla** birleştirin ve gerçek kullanıcı erişimi için mücadele edin.
- YG **sürekli risk azaltma ve daha erken değerdir**, ama yalnızca Çeviklik ritüel değil gerçek olduğunda. Bkz. bölümler 1.4, 11.1, 11.2, 10.6 ve 11.3.

## Kaynaklar ve ileri okuma

- Kent Beck et al., *Manifesto for Agile Software Development* and its twelve principles (agilemanifesto.org, 2001).
- Ken Schwaber and Jeff Sutherland, *The Scrum Guide*.
- Kent Beck, *Extreme Programming Explained: Embrace Change*.
- David J. Anderson, *Kanban: Successful Evolutionary Change for Your Technology Business*.
- Mike Cohn, *User Stories Applied* and *Succeeding with Agile*.
- Jeff Patton, *User Story Mapping*.
- Stephen Denning, *The Age of Agile*.
- Matthew Skelton and Manuel Pais, *Team Topologies* (team design and descaling).
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate* (evidence for agile/DevOps practices).
- U.S. Digital Service, *Digital Services Playbook*; UK Government, *Government Service Standard*.
