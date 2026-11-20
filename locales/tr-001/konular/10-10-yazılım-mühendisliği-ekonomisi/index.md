# 10.10 Yazılım mühendisliği ekonomisi

## Genel bakış ve motivasyon

Yazılım mühendisliği ekonomisi, mühendislik kararlarını değer ve maliyet cinsinden, belirsizlik altında ve zaman içinde verme disiplinidir. Liderliğin gerçekten sorduğu soruları yanıtlayan muhakemedir. Bunu inşa etmeye değer mi? Bu üç seçenekten hangisi en iyi getiriyi sağlar? Bu sistemin sahipliği yalnızca bu çeyrekte yayına almak değil, önümüzdeki on yıl boyunca bize neye mal olacak? Bu [teknik borcu](https://en.wikipedia.org/wiki/Technical_debt) şimdi mi ödemeliyiz, yoksa erteleyip faizini mi ödemeliyiz? Her yol haritası, satın alma, platform yatırımı ve modernizasyon programı, özünde ekonomik bir savdır. Bu bölüm, o savları açık, karşılaştırılabilir ve savunulabilir kılan disiplini adlandırır.

Tek bir takım için ekonomik muhakeme gayriresmi kalabilir, çünkü yanlış bir kararın bedeli küçüktür ve çabuk düzeltilir. Bir kurumsal ya da kamu kuruluşunda bahisler büyüktür, para başkalarının parasıdır ve kararlar finans, denetçiler ve kamuoyu tarafından incelenir. Yalnızca inşa maliyetini sayıp yılların işletme, lisans, destek ve nihai değiştirme masrafını yok saydığı için ucuz görünen bir program, kasvetli bir güvenilirlikle bütçesini aşacaktır. Varsayımlarını hiç belirtmeden getiri vadeden bir öneri sorgulanamaz, karşılaştırılamaz ve hesabı sorulamaz. Yazılım mühendisliği ekonomisi size ortak, nicel bir dil verir; böylece kıt sermaye en çok değer yaratan işe akar.

Bu bölüm, bu rehber boyunca kullanılan [yatırım getirisi](https://en.wikipedia.org/wiki/Return_on_investment) (YG) ve [toplam sahip olma maliyeti](https://en.wikipedia.org/wiki/Total_cost_of_ownership) (TSM) muhakemesinin analitik omurgasıdır. Portföy ve program yönetimi (bölüm 10.1) *neyin* fonlanacağına karar verir; bu bölüm *nasıl* karar verileceğinin ekonomik yöntemini sağlar. Bölüm şunlara bağlanır: bu hesapların satın alma-ya-da-inşa etme ve sözleşme seçimlerini gerekçelendirdiği satın alma (bölüm 10.3); işletme maliyeti ekonomisini operasyonel pratiğe çeviren maliyet, FinOps (finansal operasyonlar, yani bulut ve çalışma zamanı harcamasının disiplinli yönetimi) ve yeşil yazılım (bölüm 9.4); değer hipotezlerinin oluşturulup sınandığı keşif hattı ve çıktılar (bölüm 11.1); karar alma ve yönetişimde teknik borç (bölüm 1.5); ve sahip olma maliyetinin uzun kuyruğunun gerçekten düştüğü yazılım bakımı (bölüm 3.7).

## Temel ilkeler

- **Değer ve maliyet ikisi de tahmindir.** Her sayıya, olgu olarak değil, varsayımlarıyla bir aralık olarak davranın. Dürüst belirsizlik, sahte kesinlikten iyidir.
- **Paranın zaman değeri vardır.** Bugünkü bir dolar, gelecek yılki bir dolardan daha değerlidir; seçenekleri karşılaştırmadan önce gelecekteki nakit akışlarını iskonto edin.
- **Satın alma fiyatına değil, toplam sahip olma maliyetine göre karar verin.** İnşa bir peşinattır; işletme, destek ve sürdürme ise ipoteğin kendisidir.
- **Bir karar için yalnızca gelecekteki maliyetler ve faydalar önemlidir.** [Batık maliyetler](https://en.wikipedia.org/wiki/Sunk_cost) gitmiştir; sırada ne yapacağınızı seçerken onları yok sayın.
- **Her seçimin bir [fırsat maliyeti](https://en.wikipedia.org/wiki/Opportunity_cost) vardır.** İlgili karşılaştırma her zaman aynı paranın, insanın ve zamanın en iyi alternatif kullanımıdır.
- **Gecikmenin bir fiyatı vardır.** [Gecikme maliyeti](https://en.wikipedia.org/wiki/Cost_of_delay), yani bir karar ya da teslimat beklerken vazgeçilen değer, modeldeki çoğu zaman en büyük ve en çok göz ardı edilen sayıdır.
- **İş gerekçesini çürütülebilir kılın.** Varsayımları o kadar net belirtin ki gerçeklik bunları sonradan doğru ya da yanlış çıkarabilsin.

## Öneriler

### Kararları ekonominin temellerine dayandırın

Hesap tablolarını kurmadan önce ortak bir sözcük dağarcığı kurun. *Değeri* (bir paydaşın elde ettiği fayda) *maliyetten* (onu üretmek için tüketilen şey) ayırın ve ikisini de *nakit akışı*, yani belirli zamanlarda içeri ya da dışarı hareket eden para olarak ifade edin. Gelecek yılki bir ödeme bugünkünden daha az değerli olduğu için *[paranın zaman değerini](https://en.wikipedia.org/wiki/Time_value_of_money)* uygulayın: gelecekteki nakit akışlarını, [sermaye maliyetinizi](https://en.wikipedia.org/wiki/Cost_of_capital) ya da resmî bir oranı yansıtan bir iskonto oranıyla bugünkü değere indirin. Bir *öneri* de o zaman, rakip seçeneklerin nakit akışı dizilerinin tanımlı bir ufuk üzerinde yapılandırılmış karşılaştırmasıdır. Her önemli önerinin ufkunu, iskonto oranını ve varsayımlarını tek bir sayfada belirtmesini isteyin; böylece gözden geçirenler matematiği tersine mühendislikle çözmek yerine özü tartışır.

### Belirsizlik ve risk altında açıkça karar verin

Yazılım kararları eksik bilgiyle verilir. Aksini varsaymak hatadır. Belirsizliği gizlemek yerine modelleyin. Tek sayılar yerine üç noktalı tahminler (iyimser, olası, kötümser) kullanın ve sonuçları olasılıklarıyla ağırlıklandırarak bir *[beklenen değer](https://en.wikipedia.org/wiki/Expected_value)* hesaplayın. Sonuçları büyük kararlar için [duyarlılık analizi](https://en.wikipedia.org/wiki/Sensitivity_analysis) yapın: en önemli iki ya da üç girdiyi değiştirin ve önerinin tersine dönüp dönmediğine bakın. *Riski* (nicellenebilir olasılıklar) derin *belirsizlikten* (bilinmeyen olasılıklar) ayırın ve belirsizlik yüksekken esnekliği koruyan seçenekleri tercih edin. Öğrendikten sonra durmanıza, yön değiştirmenize ya da bahsi artırmanıza izin veren aşamalı bir taahhüt, ya hep ya hiç türünden daha ucuz bir bahisten çoğu zaman daha değerlidir.

### Karar yöntemini kâr amaçlı ve kamusal bağlamlara uydurun

Kâr amaçlı kuruluşlar tipik olarak finansal getiriyi eniyiler; bir sermaye maliyetine karşı [net bugünkü değer](https://en.wikipedia.org/wiki/Net_present_value), YG ve geri ödeme süresini kullanır. Kâr amacı gütmeyen ve kamu sektörü kuruluşları misyon değerini, hizmet sonuçlarını, hakkaniyeti ve kamu parasının sorumlu yönetimini eniyiler ve her faydayı gelire indirgeyemez. İki ortamda da aynı analitik aygıtı kullanın, ama amaç işlevini dürüstçe seçin. Kamuda [maliyet-fayda](https://en.wikipedia.org/wiki/Cost%E2%80%93benefit_analysis) ve maliyet-etkinlik analizi, resmî iskonto oranları ve ömür boyu maliyetleme sıklıkla zorunludur. Parayla ifade edilebileni parayla ifade edin, geri kalanı için ise onları ayar katsayısı olarak içeri kaçırmak yerine açık, belgelenmiş parasal olmayan ölçütler kullanın. İki dünyada da disiplin aynıdır: amacı ve ödünleşimleri görünür kılın.

### Maliyeti birden fazla yöntemle tahmin edin

Hiçbir tahmin yaklaşımı tek başına güvenilir değildir, bu yüzden üçgenleyin. *Benzetmeyi* (benzer geçmiş işlerle karşılaştırma), *uzman yargısını* (deneyimli mühendislerden yapılandırılmış girdi, örneğin geniş bantlı Delphi ya da planlama pokeri), *ayrıştırmayı* (işi parçalara ayırıp tahminleri aşağıdan yukarıya toplama) ve *parametrik modelleri* (verinizle kalibre edilmiş, [COCOMO II](https://en.wikipedia.org/wiki/COCOMO) gibi formül güdümlü modeller) birleştirin. Ampirik verimlilik verisine sahip olduğunuz yerde, spekülatif boyutlandırma yerine geçmiş akış verisini tercih edin. Tahminleri her zaman güvenle birlikte aralıklar olarak ifade edin, öğrendikçe yeniden tahmin edin ve *efor* tahminini bir *tarih* taahhüdünden ayırın. İkisini birbirine karıştırmak, tahminlerin bozulmuş sözlere dönüşmesinin yoludur.

### TSM, YG, NBD ve geri ödemeyi tutarlı hesaplayın

Küçük, standart bir araç takımı benimseyin ve onu tekdüze uygulayın; böylece seçenekler portföy genelinde karşılaştırılabilir olur. *Toplam sahip olma maliyeti* tüm ömür boyunca bütün maliyetleri toplar: inşa, dağıtım, lisans, işletme, destek, güvenlik ve emeklilik. *YG* net faydayı maliyetin yüzdesi olarak ifade eder. *Net bugünkü değer (NBD)* her gelecek nakit akışını bugüne iskonto eder ve toplar; pozitif bir NBD, seçeneğin iskonto oranınızda değer yarattığı anlamına gelir. *[Geri ödeme süresi](https://en.wikipedia.org/wiki/Payback_period)* ilk harcamanın geri kazanılma süresidir. Basit ve sezgiseldir, ama başa baş noktasından sonrasına ve paranın zaman değerine karşı kördür; bu yüzden onu yalnızca NBD ile birlikte kullanın. Karşılaştırılan seçenekler arasında ufku ve iskonto oranını standartlaştırın, yoksa karşılaştırma anlamsızdır.

### Teknik borcu ve gecikme maliyetini fiyatlayın

Normalde görünmeyen iki maliyeti açık kılın. *Teknik borç* finansal borç gibi davranır: kestirmeler şimdi hız ödünç alır ve faizi sonra, daha yavaş teslimat, daha çok kusur ve daha yüksek işletme maliyeti olarak tahsil eder. Faizi, yani borcun her gelecek sürümü ne kadar vergilendirdiğini tahmin edin; böylece borca girme ya da onu ödeme tercihi ahlaki değil ekonomik bir karar olur (bölüm 1.5 ve 3.7'ye bakın). *Gecikme maliyeti*, değerli bir şeyin geç kaldığı her zaman birimi için kaybedilen değerdir. Onu nicellemek, bulanık "acele etmeliyiz" sezgilerini gerçek önceliklendirmeye çevirir; en doğrudan Ağırlıklı En Kısa İş Önce (WSJF) sıralamasıyla. Gecikmeyi fiyatlayan takımlar kullanım oranını eniyilemeyi bırakıp değeri eniyilemeye başlar.

### Soyut değerleri değerlendirin ve iş gerekçesini kurun

En büyük faydaların birçoğu net bir dolar rakamına direnir: azalan risk, gelişen güvenlik duruşu, geliştirici verimliliği, marka güveni, misyon sonuçları, seçenek değeri. Onları sıfır saymak her kararı somut olana doğru yanlı kılar. Yine de değerleyin. Güvenilir olduğu yerde vekil ölçütlerle parasallaştırın (önlenen bir ihlalin maliyeti, kazanılan saatler çarpı yüklü saat ücreti). Yapamadığınız yerde onları adlandırılmış ölçütlere göre açıkça puanlayın ve finansal modelin yanında taşıyın. Bütünü bir *iş gerekçesi* olarak toparlayın: sorun, değerlendirilen seçenekler (hiçbir şey yapmamak dahil), ufuk boyunca maliyetler ve faydalar, temel varsayımlar ve riskler, öneri ve işe yarayıp yaramadığını sonradan yargılayacağınız ölçütler. Onu canlı tutun ve gerçekleşenlerle karşılaştırarak yeniden gözden geçirin; böylece kuruluşunuz daha iyi tahmin etmeyi öğrenir.

## Ödünleşimler: artılar ve eksiler

| Yaklaşım | Artılar | Eksiler |
|---|---|---|
| Ayrıntılı nicel modelleme (NBD, TSM) | Titiz, karşılaştırılabilir, denetlenebilir; varsayımları açığa çıkarmaya zorlar | Zaman alıcı; girdiler zayıfsa sahte kesinlik; ölçülmeyeni dışarıda bırakabilir |
| Hafif sezgiseller (geri ödeme, gecikme maliyeti) | Hızlı, sezgisel, iletmesi kolay | Paranın zaman değerini ya da uzun kuyruk maliyetleri yok sayar; büyük taahhütler için kaba |
| Tek sayılı tahminler | Basit, kesin, etrafında plan yapması kolay | Belirsizliği gizler; sahte sözlere dönüşür; dürüstlüğü cezalandırır |
| Aralıklar ve beklenen değer | Riskle ilgili dürüst; aşamalı kararları destekler | İletmesi daha zor; tek sayı isteyen paydaşlara kaçamak gelebilir |
| Soyut değerleri vekillerle parasallaştırma | Büyük faydaları modelde tutar; ödünleşimleri mümkün kılar | Vekiller tartışmaya açık; elverişli sayılar üretme riski |
| Tam ömür boyu TSM analizi | Ucuz inşa, pahalı işletme sürprizlerini önler | Birçok takımın erkenden sahip olmadığı işletme maliyeti verisi gerektirir |

Süregelen gerilim titizlik ile hız arasındadır. Ağır finansal modelleme büyük, geri döndürülemez, pahalı kararları iyileştirir; ama küçük, geri döndürülebilir kararlarda boşa gider, hatta zararlıdır, çünkü orada yalnızca önceden belirlenmiş bir yanıtı hesap tablosunun otoritesiyle aklar. Olgun kuruluşlar analizi bahsin büyüklüğüne göre boyutlandırır: sıradan bir özellik için tek sayfalık bir gecikme maliyeti savı, çok yıllı bir platform ya da satın alma için tam bir NBD ve TSM iş gerekçesi. İkinci gerilim kesinlik ile dürüstlük arasındadır. Tek ve özgüvenli bir sayı üzerinde harekete geçmek daha kolaydır ama çoğu zaman yanlıştır. Bir aralık doğrudur ama ona bağlanmak daha zordur. Çözüm, aralıklar ve beklenen değerle karar vermek, sonra aşamalı artışlara bağlanmaktır; böylece kanıt geldikçe rotayı düzeltme seçeneğini korursunuz.

## Takımınızla tartışılacak sorular

1. **Efor tahminini tarih taahhüdünden ayırıyor muyuz ve tek bir sayıya güvenmek yerine tahminleri üçgenliyor muyuz?** Tek ve özgüvenli bir sayının etrafında plan yapmak kolaydır ve çoğu zaman yanlıştır; aralığa dayalı bir efor tahmini sabit bir tarihe dönüştüğü anda dürüstlük cezalandırılır ve tahmin bozulmuş bir söze dönüşür. Üçgenleyin: benzetmeyi, uzman yargısını, ayrıştırmayı ve geçmiş verimliliği birleştirin ve spekülatif boyutlandırma yerine gerçek akış verisini tercih edin. Tahminleri güvenle birlikte aralıklar olarak ifade edin ve öğrendikçe yeniden tahmin edin. Finans ve denetim incelemesi altındaki büyük bir program için bu, savunulabilir bir öngörü ile kimsenin sorgulayamayacağı bir sayı arasındaki farktır. Kayan yakın tarihli bir tahmini getirin ve bunun takvime göre yönetilmiş bir efor tahmini olup olmadığını sorun.

2. **Gecikme maliyetini fiyatlıyor ve işi sıralamak için kullanıyor muyuz, yoksa hâlâ kullanım oranını mı eniyiliyoruz?** Gecikme maliyeti, değerli bir şeyin geç kaldığı her zaman birimi için kaybedilen değerdir ve modeldeki çoğu zaman en büyük ve en çok göz ardı edilen sayıdır. Onu hiç fiyatlamayan takımlar herkesi meşgul tutmak için eniyileme yapar ve bu, en yüksek değerli işi sessizce aç bırakır. Onu nicelleyin ve Ağırlıklı En Kısa İş Önce ile sıralayın; böylece beklerken en çok değer kaybeden iş önce gider. Bu, yol haritalarını yeniden sıralar ve "acele etmeliyiz"i gerçek önceliklendirmeye çevirir. Devam eden iki ya da üç girişimi getirin ve her birinin haftalık gecikmenin neye mal olduğunu tahmin edin; edemiyorsanız kapatılacak boşluk budur.

3. **İş gerekçelerimiz hiçbir şey yapmama temel çizgisine karşı ömür boyu TSM'ye göre mi karar veriyor ve titizlik bahsin büyüklüğüne göre mi boyutlandırılıyor?** İnşa bir peşinattır; işletme, lisans, destek ve nihai değiştirme ipoteğin kendisidir ve yalnızca inşa maliyetini sayan bir program kasvetli bir güvenilirlikle bütçesini aşacaktır. Her ciddi öneri, seçenekleri (hiçbir şey yapmamak dahil) standart bir ufuk üzerinde ortak bir iskonto oranıyla karşılaştırmalı ve varsayımlarını tek sayfada belirtmelidir; böylece gözden geçirenler aritmetik değil öz üzerinde tartışır. Çabayı boyutlandırın: sıradan bir özellik için tek sayfalık bir gecikme maliyeti savı, çok yıllı bir platform ya da satın alma için tam bir NBD ve TSM gerekçesi. Küçük, geri döndürülebilir bir kararın ağır modellenmesi, önceden belirlenmiş bir yanıtı hesap tablosunun otoritesiyle aklamaktan başka bir şey yapmaz. Yakın tarihli bir kararı getirin ve etiket fiyatının değil işletme maliyetinin belirleyici olup olmadığını sorun.

4. **Seçenekleri zaman içinde karşılaştırmak için hangi iskonto oranını kullanıyoruz ve önerinin farklı bir orana dayanıp dayanmadığını sınadık mı?** Paranın zaman değeri, beşinci yıldaki bir doların bugünkü bir dolar olmadığı anlamına gelir; yine de birçok öneri ya iskontoyu tümüyle atlar ya da kimsenin üzerinde anlaşmadığı bir oranı gömer. Karşılaştırılan seçenekler arasında tek bir oran ve tek bir ufuk standartlaştırın, yoksa karşılaştırma içgörü kılığına girmiş aritmetiktir. Karşıt husus, oranın kendisinin tartışmalı olmasıdır: çok düşükse uzun vadeli dev projeleri kayırırsınız, çok yüksekse yavaş geri ödeyen yatırımları aç bırakırsınız. Kullandığınız oranı, nereden geldiğini (sermaye maliyetiniz ya da yayımlanmış resmî bir oran) ve önerinin hangi oranda tersine döndüğünü gösteren bir duyarlılık analizini getirin. Kurumsal finans ve özellikle kamu için oran çoğu zaman zorunludur, örneğin resmî bir değerlendirme oranıdır; belgelenmemiş ya da tutarsız bir oran bir denetçinin ilk sorgulayacağı şeydir.

5. **Bir girişim kötü performans gösterdiğinde, harcadığımızı yok sayıp beklenen gelecek değere göre mi karar veriyoruz ve fonlamayı gerçekten durabilecek şekilde yapılandırdık mı?** Batık maliyetler gitmiştir, ama güçlü bir çekim uygularlar: takımlar, önlerindeki değer yerine, çoktan akıtılan parayla başarısız çabaları savunur. Karşıt baskı gerçektir, çünkü durmak israfı kabul etmek gibi görünür ve siyasi bir bedeli vardır; bu yüzden disiplin, o anda herkesin ne hissettiğine bırakılmamalı, fonlama biçiminize yerleştirilmelidir. Tek bir geri döndürülemez bahis yerine, bağımsız olarak değerli olan ve her artıştan sonra durmanıza, yön değiştirmenize ya da bahsi artırmanıza izin veren aşamalı taahhütleri tercih edin. Geride kalan bir devam eden çabayı, bitirmek için kalan maliyeti beklenen kalan faydaya karşı koyarak ve bir sonraki fonlama kapısının düştüğü noktayla birlikte getirin. Kurumsal ya da kamu portföyünde, bir programı durdurma yetkisinin kimde olduğunu ve fonlama yapısının onlara gerçek bir karar noktası verip vermediğini adlandırın; çünkü kapısı olmayan bir taahhüt kimsenin durduramayacağı bir taahhüttür.

6. **Amaç işlevimiz konusunda dürüst müyüz ve soyut değerleri sıfır saymak yerine açıkça değerliyor muyuz?** En büyük faydaların bazıları, azalan risk, güvenlik duruşu, geliştirici verimliliği, misyon sonuçları ve seçenek değeri, net bir dolar rakamına direnir ve onları sıfır saymak her kararı somuta ve yakın vadeliye doğru yanlı kılar. Karşıt risk ters hatadır: elverişli bir sayı üretmek ve bir tahmini sahte kesinlikle giydirmek. Hangi faydaları güvenilir vekillerle parasallaştıracağınıza (önlenen bir ihlal, kazanılan saatler çarpı yüklü bir ücret) ve hangilerini modelin yanında taşınan adlandırılmış parasal olmayan ölçütlere göre puanlayacağınıza bilinçle karar verin. Soyut bir değerin önemli olduğu yakın tarihli bir kararı getirin ve bunun fiyatlanıp, puanlanıp ya da sessizce düşürülüp düşürülmediğini sorun. Bir kamu kuruluşu için bu daha da keskindir: misyon değeri, hakkaniyet ve kamu parasının sorumlu yönetimi hepsi gelire indirgenemez; bu yüzden amaç işlevini açıkça seçin ve parasal olmayan ölçütleri ayar katsayısı olarak içeri kaçırmak yerine belgeleyin.

## Sektör merceği

**Girişim.** Birkaç aylık nakit ömrüyle baskın ekonomik sayı gecikme maliyetidir: az sayıdaki mühendisinizin çekirdek üründen uzakta geçirdiği her hafta ertelenen gelir ve öğrenmedir. Analizi tek sayfada tutun ve olağan yetenekleri inşa etmek yerine satın almayı tercih edin; böylece kıt mühendislik dikkati ayırt edici özellikte kalır. Ayrıntılı NBD modellerini atlayın; kabaca bir ömür boyu karşılaştırma ve sert bir harcama tavanı, ucuz inşa, pahalı işletme tuzağını size zarar vermeden önce yakalamak için yeterlidir.

**Küçük işletme.** Finansal analistiniz yok; bu yüzden yöntemi basit ve dürüst tutun: her seçeneğe sahip olmanın tam maliyetini, yani abonelik artı tükettiği personel saatlerini, hiçbir şey yapmamakla karşılaştırın. Satın alma-ya-da-inşa etme kararı hemen her zaman satın almayı kayırır, çünkü bakımını yapamayacağınız bir sistem sessizce büyüyen bütçelenmemiş bir işletme maliyetine dönüşür. Yatırımları iskontolu modeller yerine kısa, sezgisel bir geri ödemeyle yargılayın ve ölçeklenene kadar ucuz görünen koltuk başına fiyatlamaya dikkat edin.

**Kurumsal.** Zorluk, birçok takım ve uzun bir portföy genelinde karşılaştırılabilirliktir: rakip önerilerin aynı temelde sıralanabilmesi için tek bir iskonto oranını, tek bir ufku ve tek bir araç takımını (NBD, TSM, gecikme maliyeti) standartlaştırın. Teknik borç faizini ve gecikme maliyetini açıkça fiyatlayın, çünkü ölçekte bunlar başlıktaki inşa maliyetlerini gölgede bırakır. İş gerekçelerini gerçekleşenlerle karşılaştırılarak yeniden gözden geçirilen canlı belgeler yapın; böylece tahmin doğruluğu artar ve finans ile denetim sermayenin neden oraya aktığını görebilir.

**Kamu.** Maliyet-fayda analizi, resmî bir iskonto oranı ve ömür boyu maliyetleme sıklıkla zorunludur ve amaç gelir değil kamusal değerdir; bu yüzden güvenilir biçimde parasallaştırabildiğinizi parasallaştırın ve geri kalanını açık, yayımlanmış ölçütlere göre puanlayın. Her varsayımı bir hiçbir şey yapmama temel çizgisine karşı açıkça belirtin, çünkü denetçiler ve kamuoyu onları sınayacaktır. Fonlamayı bağımsız olarak değerli artışlara bölün; böylece bir sonraki aşama taahhüt edilmeden önce her aşamanın faydaları gerçekleşir ve ölçülür ve bir program batık kamu parasını ortada bırakmadan durdurulabilir.

## Örnekler

**Girişim.** Dokuz aylık nakit ömrü olan altı kişilik bir girişim, kendi faturalama sistemini mi kuracağını yoksa barındırılan bir sistemi mi satın alacağını tartışır. Kurucular tek sayfada iki seçeneği on sekiz aylık bir ufuk üzerinde karşılaştırır: inşa kâğıt üzerinde daha ucuz görünür ama önceden üç mühendis-ayına mal olur ve gecikme maliyeti (bu mühendisler çekirdek ürünü yayına almazken ertelenen gelir) abonelik ücretini gölgede bırakır. Barındırılan faturalamayı satın alırlar, kıt mühendislik zamanlarını ayırt edici özellik için korurlar ve kararı yalnızca fiyatlama ya da hacim matematiği değiştirirse yeniden gözden geçirirler.

**Kurumsal.** Bir perakendeci, e-ticaret yığınını yeniden platformlamayı mı yoksa mevcut sistemi yamamaya devam etmeyi mi tartar. Mühendislik ve finans takımı, kurumsal iskonto oranında beş yıllık bir model kurar; üç seçeneği (hiçbir şey yapmamak, artımlı yeniden düzenleme ve tam yeniden platformlama) inşa, bulut işletme maliyeti, lisans ve destek üzerinden TSM açısından karşılaştırır. Mevcut durumun teknik borç faizini (artan olay oranları ve yavaşlayan sürüm temposu) ve eski yığının destekleyemediği özelliklerin gecikme maliyetini nicelerler. Yeniden platformlama daha yüksek bir peşin maliyet ama üçüncü yılda pozitif bir NBD ve sonrasında daha düşük bir işletme maliyeti gösterir. Duyarlılık analizi, bulut fiyatları keskin biçimde yükselmedikçe önerinin geçerli kaldığını doğrular. Onu tek bir geri döndürülemez taahhüt olarak değil, kilometre taşlarına bağlı aşamalarla fonlarlar.

**Kamu.** Bir yardım sistemini modernleştiren bir kurumdan, resmî iskonto oranını ve ömür boyu maliyetlemeyi kullanan bir maliyet-fayda analizi sunması istenir. Başlıca faydalar misyon sonuçları (daha hızlı, daha doğru, daha hakkaniyetli hizmet) olduğu için takım güvenilir biçimde parasallaştırabildiğini (azalan çağrı merkezi yükü, daha az hatalı ödeme, önlenen dolandırıcılık) parasallaştırır ve geri kalanını dolar rakamları uydurmak yerine açık kamusal değer ölçütlerine göre puanlar. İş gerekçesi bir hiçbir şey yapmama temel çizgisi sunar, varsayımlarını denetim için açıkça belirtir ve fonlamayı bağımsız olarak değerli artışlara bölerek yapılandırır; böylece bir sonraki aşama taahhüt edilmeden önce her aşamanın faydaları gerçekleşir ve ölçülür.

## İş gerekçesi: motivasyonlar, YG ve TSM

Yazılım mühendisliği ekonomisini uygulamanın getirisi daha iyi sermaye tahsisidir: para, insan ve zaman en çok değer yaratan işe akar. Mekanizma üç katmanlıdır. Birincisi, önlenen israf: dürüst bir NBD ya da TSM sınamasında başarısız olan öneriler, yıllarca harcama tüketmeden önce reddedilir. İkincisi, daha iyi sıralama: gecikme maliyetini fiyatlamak en yüksek değerli işi öne taşır ve getirileri portföy boyunca bileşik hale getirir. Üçüncüsü, daha az pahalı sürpriz: ömür boyu maliyetleme, ucuz bir inşayı fonlayıp pahalı bir işletmeyle pusuya düşme gibi klasik başarısızlığı önler.

Uygulamanın maliyeti mütevazıdır: modelleri kurmak için analist zamanı, varsayımları belirtme disiplini ve liderleri başlık fiyatlar yerine iskontolu, ömür boyu sayılara göre karar vermeye ikna etmenin kültürel işi. Onu *uygulamamanın* maliyeti daha büyüktür ama dağınıktır. Somut ve yakın vadeliyi sistematik olarak fazla değerlersiniz, borcu ve gecikmeyi eksik fiyatlarsınız ve işletme maliyetlerini ancak kaçınılmaz hale geldikten sonra keşfedersiniz. Disiplini liderliğe diğer her yatırım kararının kalite kontrolü olarak sunun. Yeni bir harcama kalemi eklemez; daha çok mevcut her harcama kaleminin hesap verebilir olmasını sağlar. Önlenen tek bir düşük değerli program ya da bir işletme maliyeti patlamasını önleyen tek bir doğru TSM öngörüsü, tüm uygulamanın bedelini kat kat öder.

## Anti-kalıplar ve tuzaklar

- **Satın alma fiyatını toplam maliyet saymak.** İnşa ya da lisans ücretine göre karar verip yılların işletme, destek ve nihai değiştirme maliyetini yok saymak.
- **Batık maliyet bağlılığı.** Beklenen gelecek değer yerine çoktan harcanan paradan dolayı başarısız bir çabayı sürdürmek.
- **Kesinlik tiyatrosu.** Tahmin edilmiş girdiler üzerine kurulu, on ondalıklı hesap tabloları; önceden belirlenmiş bir sonuca sahte otorite kazandırmak.
- **Paranın zaman değerini yok saymak.** Yakın vadeli ve uzak gelecekteki nakit akışlarını, beşinci yıldaki bir dolar bugünkü bir dolara eşitmiş gibi karşılaştırmak.
- **Soyut değerleri sıfır saymak.** Fiyatlaması zor olduğu için riski, güvenliği, verimliliği ve misyon değerini dışarıda bırakıp her kararı ölçülebilir olana doğru yanlı kılmak.
- **Tahmini söz saymak.** Aralığa dayalı bir efor tahminini sabit tarihli bir taahhüt olarak ele alıp sonra takvime göre yönetmek.
- **Fiyatlanmamış teknik borç.** Faizi hesaba katmadan kestirmelere başvurmak, ta ki teslimat üzerindeki bileşik vergi bir krize dönüşene kadar.
- **Gecikme maliyeti körlüğü.** Takım kullanım oranını ve birim maliyeti eniyilerken geç kalmaktan kaybedilen çok daha büyük değeri yok saymak.

## Olgunluk modeli

**Düzey 1, Başlangıç.** Kararlar başlık fiyatı ve iç güdüyle, tepkisel olarak ve vaka vaka gerekçelendirilir. İskonto yok, TSM yok, belirtilmiş varsayım yok. Tahminler söz sayılan tek sayılardır. Teknik borç ve gecikme maliyeti hiçbir modelde görünmez.

**Düzey 2, Geliştirme.** Daha büyük yatırımlar, bazı maliyetler ve faydalar içeren kaba bir iş gerekçesi taşır ve bazı işletme maliyetleri göz önüne alınır. Basit geri ödeme ya da YG ortaya çıkar, ama paranın zaman değeri ve ömür boyu maliyetleme eşitsiz uygulanır ve takımdan takıma değişir. Tahminler bazen aralık taşır, ancak uygulama tutarsızdır.

**Düzey 3, Standartlaştırma.** Paylaşılan bir iskonto oranı ve ufukla standart bir ekonomik araç takımı (NBD, TSM, YG, gecikme maliyeti) belgelenir ve portföy genelinde tutarlı uygulanır. Belirsizlik aralıklar ve beklenen değerle modellenir. Teknik borç tahmin edilir ve önceliklendirilir. İş gerekçeleri bir hiçbir şey yapmama temel çizgisini karşılaştırır, varsayımlarını belirtir ve denetlenebilirdir.

**Düzey 4, Yönetme.** Öngörüler gerçekleşenlerle karşılaştırılarak ölçülür ve veriyle kontrol edilir. Tahmin doğruluğu, gerçekleşen YG, işletme maliyetinin projeksiyona karşı durumu ve gecikme maliyeti sonuçları temel çizgilere karşı izlenir ve önemli sapma bir gözden geçirmeyi tetikler. İş gerekçeleri tanımlı başarı ölçütleri ve duygu yerine kanıta göre uygulanan sonlandırma ölçütleri taşır; iskonto oranı ve duyarlılık varsayımları geçmiş sonuçlara karşı doğrulanır, böylece sayılar yalnızca üretilmekle kalmaz kontrol edilir.

**Düzey 5, Orkestrasyon.** Ekonomik muhakeme süreklidir, kalibre edilmiştir ve portföy, satın alma ve risk planlamasıyla bütünleşiktir. İş gerekçeleri kanıt geldikçe yeniden gözden geçirilen canlı belgelerdir ve sonuçlar geri beslendiği için tahmin doğruluğu zamanla artar. Gecikme maliyeti sıralamayı yönlendirir, soyut değerler açıkça değerlenir ve aşamalı fonlama seçenek değerini korur; böylece kuruluş koşullar değiştikçe sermayeyi en çok değer yaratan işe doğru uyarlanır biçimde yeniden dengeler.

## Tartışma fikirleri

- Analiz kararın kendisinden daha pahalıya gelmeden önce, geri döndürülebilir, düşük maliyetli bir karara ne kadar finansal titizlik uygulamaya değer?
- Kuruluşunuz hangi iskonto oranını kullanmalı ve onu değiştirdiğinizde öneri ne kadar değişiyor?
- Soyut bir değeri parasallaştırmak ne zaman gerçek bir içgörüdür, ne zaman elverişli bir sayı üretmektir?
- Teknik borcun faizini, liderliğin geri ödemesini fonlayacağı kadar ikna edici biçimde nasıl fiyatlarsınız?
- Bir kamu sektörü ortamında, parasallaştırmaya direnen hakkaniyeti ve misyon sonuçlarını daha net finansal getirileri olan seçeneklerle nasıl tartarsınız?
- İş gerekçeleri gerçekleşenlerle karşılaştırılarak yeniden gözden geçirilmeli mi ve gerçekleşen değer öngörüden saptığında kim hesap verir?

## Önemli çıkarımlar

- Yazılım mühendisliği ekonomisi değer ve maliyet ödünleşimlerini açık, karşılaştırılabilir ve savunulabilir kılar: bu rehber boyunca kullanılan YG ve TSM muhakemesinin analitik omurgasıdır.
- Satın alma fiyatına değil, tüm ömür boyunca toplam sahip olma maliyetine göre karar verin ve paranın zaman değerine saygı gösterecek şekilde gelecekteki nakit akışlarını iskonto edin.
- Tahminlere belirsizlik altında aralıklar olarak davranın, maliyeti birden fazla yöntemle üçgenleyin ve bir efor tahmininin sabit tarihli bir söze dönüşmesine asla izin vermeyin.
- Normalde görünmeyen maliyetleri fiyatlayın: faiz olarak teknik borç ve vazgeçilen değer olarak gecikme maliyeti; çünkü çoğu zaman modeldeki en büyük sayılardır.
- Soyut değerleri sıfır saymak yerine açıkça değerleyin ve kâr amaçlı ya da kamusal bir amaç işlevini dürüstçe seçin.
- Varsayımları ve seçenekleri (hiçbir şey yapmamak dahil) belirten canlı iş gerekçeleri kurun, titizliği bahsin büyüklüğüne göre boyutlandırın ve öngörüleri gerçekleşenlerle karşılaştırarak yeniden gözden geçirin; böylece kuruluş daha iyi tahmin etmeyi öğrenir.

## Kaynaklar ve ileri okuma

- Barry W. Boehm, *Software Engineering Economics*
- Barry W. Boehm et al., *Software Cost Estimation with COCOMO II*
- IEEE Computer Society, *SWEBOK Guide* (Software Engineering Economics knowledge area)
- Donald G. Reinertsen, *The Principles of Product Development Flow* (cost of delay, WSJF)
- Steve McConnell, *Software Estimation: Demystifying the Black Art*
- Douglas W. Hubbard, *How to Measure Anything: Finding the Value of Intangibles in Business*
- Ward Cunningham, "The WyCash Portfolio Management System" (the technical-debt metaphor)
- Philippe Kruchten, Robert Nord, and Ipek Ozkaya, *Managing Technical Debt*
- Mark Schwartz, *The Art of Business Value* and *A Seat at the Table*
- U.S. Office of Management and Budget, Circular A-94 (guidelines and discount rates for benefit-cost analysis)
- HM Treasury, *The Green Book: Central Government Guidance on Appraisal and Evaluation*
