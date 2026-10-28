# 11.3 Teori antrean

## Tinjauan dan motivasi

[Teori antrean](https://en.wikipedia.org/wiki/Queueing_theory) adalah studi matematis tentang antrean tunggu. Dalam rekayasa perangkat lunak, ia teori senyap di balik praktik yang sangat banyak. Responsivitas layanan pelanggan, perencanaan [kanban](https://en.wikipedia.org/wiki/Kanban_%28development%29) (metode berbasis tarik yang membatasi [kerja dalam proses](https://en.wikipedia.org/wiki/Work_in_process) untuk memperbaiki aliran), antrean pesan antarproses, jalur continuous deployment: semuanya antrean, dan semuanya mematuhi hukum yang sama. Memahami hukum itu memungkinkan tim bernalar tentang [lead time](https://en.wikipedia.org/wiki/Lead_time), [throughput](https://en.wikipedia.org/wiki/Throughput), kapasitas, dan biaya sejati menjalankan sistem dekat batasnya, alih-alih dikejutkan olehnya di produksi. Bab ini berada di bagian Aliran karena teori antrean adalah fondasi formal aliran: ia menjelaskan *mengapa* kerja menunggu, dan apa yang benar-benar mengurangi penantian.

Inilah motivasinya: intuisi tentang antrean secara andal salah, dan salah dengan cara mahal. Orang mengasumsikan server yang berjalan pada utilisasi 90% "10% dari masalah," padahal waktu tunggu meledak secara tak linear seiring utilisasi mendekati 100%. Mereka mengasumsikan menambah kerja dalam proses (WIP) mempercepat penyampaian, padahal itu memperpanjang lead time. Mereka merencanakan kapasitas di sekitar rata-rata, lalu dihancurkan variabilitas. Sedikit teori antrean mengganti intuisi mahal ini dengan sejumlah kecil hubungan tangguh, terpenting **[Hukum Little](https://en.wikipedia.org/wiki/Little%27s_law)**, yang berlaku di antrean pelanggan, papan tugas, dan jalur CI/CD sama saja.

Bagi tim besar, enterprise, dan pemerintah, teori antrean adalah bahasa bersama untuk kapasitas dan aliran, yang menghubungkan peran yang kalau tidak berbicara saling melewati. Manajer produk peduli pada lead time dari gagasan ke pelanggan. SRE peduli pada utilisasi server dan latensi. Tim DevOps peduli pada frekuensi deployment. Pemimpin dukungan peduli pada waktu respons. Semuanya metrik antrean, dan mengekspresikannya dalam satu kerangka (laju kedatangan, laju layanan, utilisasi, waktu tunggu) memungkinkan organisasi merencanakan kapasitas, menetapkan SLO (service-level objective) yang realistis, dan membenarkan investasi dengan matematika alih-alih anekdot.

## Prinsip utama

- **Segala yang punya tunggu adalah antrean:** termasuk tiket, tugas, pesan, dan deploy.
- **Hukum Little adalah jangkar:** butir dalam sistem = laju kedatangan × waktu dalam sistem (κ = λτ).
- **Utilisasi dan waktu tunggu tak linear:** 15% kapasitas terakhir adalah yang paling mahal.
- **Variabilitas adalah musuh aliran:** rata-rata menyembunyikan nyeri; varians menciptakan antrean.
- **Mengurangi kerja dalam proses mengurangi lead time:** aliran, bukan kesibukan, adalah sasarannya.
- **Ukur seluruh aliran:** kedatangan, layanan, keberhasilan, kegagalan, lewatan, dan tunggu.
- **Proses adalah antrean dari antrean:** modelkan tahap, lalu optimalkan yang menjadi kendala.

## Rekomendasi

### Pelajari notasi inti dan pakai secara konsisten

Segelintir besaran menggambarkan antrean apa pun. Membakukannya (huruf Yunani adalah konvensi) menghapus ambiguitas antar tim:

- **λ (lambda), laju kedatangan:** seberapa cepat butir baru masuk.
- **μ (mu), laju layanan:** seberapa cepat butir ditangani. Karena "laju layanan" dipakai secara ambigu, sering layak memecah throughput secara eksplisit menjadi **laju total (χ)**, **laju keberhasilan (α)**, **laju kegagalan (β)**, dan **laju lewat (σ)**, di mana χ = α + β + σ.
- **ρ (rho), utilisasi / intensitas lalu lintas = λ / μ:** ringkasan terpenting tunggal. ρ < 1 berarti antrean terkuras; ρ ≥ 1 berarti ia tumbuh tanpa batas.
- **Waktu:** lead time (τ, awal ke akhir), waktu kerja (φ, pemrosesan aktual), waktu tunggu (ω, tertunda), dan waktu langkah (θ, antar penyelesaian).
- **ε (epsilon), rasio galat:** kegagalan ÷ total.

Menamai kegagalan dan *lewatan* secara eksplisit penting dalam perangkat lunak: butir yang ditinggalkan (pelanggan yang menyerah, keranjang yang ditinggal, tiket kerja yang ditolak) meninggalkan antrean tanpa dilayani, dan berpura-pura ia "terlayani" merusak metrik Anda. Lacak **balking** (memutuskan tidak bergabung), **reneging** (menyerah setelah menunggu), dan **jockeying** (berpindah antrean) sebagai hasil kelas satu.

### Berlabuhlah pada Hukum Little dalam perencanaan

Hukum Little menyatakan bahwa jumlah rata-rata jangka panjang butir dalam sistem stabil sama dengan laju kedatangan rata-rata dikali waktu rata-rata tiap butir dalam sistem: **κ = λ τ** (klasiknya L = λW). Ia sangat umum (tak butuh asumsi tentang distribusi kedatangan atau urutan layanan), yang menjadikannya andalan perencanaan aliran. Disusun ulang, ia memberi tahu bahwa **lead time = kerja-dalam-proses ÷ throughput**. Itu dasar matematis kanban dan lean: jika Anda ingin lead time lebih pendek dan tak dapat menaikkan throughput, Anda harus menurunkan WIP. Ia juga memberi pemeriksaan kewarasan cepat. Jika 40 tiket terbuka dan Anda menutup 8 per hari, tiket rata-rata memakan sekitar 5 hari, seberapa sibuk pun semua orang merasa. Satu-satunya syaratnya adalah *stabilitas*: kedatangan tidak boleh terus-menerus melampaui keberangkatan (ρ < 1), atau antrean, dan asumsi hukum itu, runtuh.

### Hormati ketaklinearan utilisasi

Pelajaran operasional terpenting teori antrean adalah bahwa waktu respons naik tajam, bukan bertahap, seiring utilisasi mendekati 100%. *Seven insights into queueing theory* karya Bob Wescott menangkap konsekuensi praktisnya dengan hidup:

1. Makin lambat pusat layanan, makin rendah utilisasi puncak yang harus Anda rencanakan.
2. Sangat sulit memakai 15% terakhir dari apa pun.
3. Makin dekat Anda berjalan ke tepi, makin tinggi harga salah.
4. Pertumbuhan waktu respons dibatasi oleh berapa banyak butir yang dapat menunggu.
5. Ini rata-rata, bukan maksimum: rencanakan untuk ekor.
6. Waspadai efek penyangkalan manusia di beberapa pusat layanan.
7. Tunjukkan perbaikan kecil dalam cahaya terbaiknya.

Implikasi desainnya: **sediakan ruang gerak dengan sengaja.** Menargetkan utilisasi 70–80% untuk sistem sensitif latensi bukan pemborosan; itu membeli waktu respons yang dapat diprediksi. Ini langsung menginformasikan perencanaan kapasitas dan SLO (bab 3.5 dan 9.1).

### Modelkan proses sebagai antrean dari antrean

Kerja nyata mengalir melalui tahap, dan proses multitahap sekadar antrean yang butirnya sendiri mengantre di tiap langkah. Modelkan begitu: laju kedatangan proses adalah laju kedatangan tahap 1; laju keberhasilan proses adalah laju keberhasilan tahap akhir; hitungan galat dan lewat proses adalah jumlah lintas tahap. Dua bentuk umum berulang:

- **Corong**, di mana jumlah butir menyusut tiap tahap (perekrutan: penjangkauan → wawancara → penawaran; pembelian: jelajah → keranjang → bayar; penyampaian: integrasi → UAT → produksi). Optimalkan tahap yang paling penting: maksimalkan kedatangan puncak corong, minimalkan lewatan tengah corong (keranjang ditinggal), atau minimalkan galat tahap akhir (peluncuran produksi buruk).
- Aliran penemuan-dan-penyampaian **berlian ganda** (temukan → definisikan → kembangkan → sampaikan), yang dibahas langsung bagian Aliran buku ini (bab 11.1).

Menemukan dan melonggarkan **tahap kendala** (kemacetan) adalah tempat perbaikan aliran membuahkan hasil; mengoptimalkan non-kendala hanya memindahkan antrean.

### Hubungkan metrik antrean dengan KPI yang sudah dipakai tim

Besaran antrean dipetakan bersih ke metrik penyampaian dan keandalan di tempat lain dalam buku ini, yang membuat teori praktis alih-alih akademis:

- **Lead time penyampaian (Dτ)**, "konsep ke pelanggan," adalah ukuran lead time (τ) dan metrik DORA ([DevOps Research and Assessment](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment)) (bab 11.2).
- **Frekuensi deployment (Dμ)** adalah ukuran laju layanan.
- **Laju kegagalan perubahan (Dε)** adalah rasio galat.
- **Waktu pemulihan (Rτ)** adalah lead time pemulihan, yaitu MTTR (bab 9.3).

Bedakan beberapa **MTTR** (mean time to *respond*, *repair*, *recover*, dan *resolve*) karena masing-masing mengukur segmen antrean insiden berbeda dan rutin dicampuradukkan. Mendasarkan SLI/SLO/SLA (bab 9.1) pada istilah antrean menjaga target jujur dan dapat dibandingkan.

## Trade-off: kelebihan dan kekurangan

| Keputusan | Kelebihan | Kekurangan |
|---|---|---|
| **Jalankan sistem pada utilisasi tinggi** | Biaya perangkat keras/satuan lebih rendah | Ledakan latensi tak linear; rapuh terhadap lonjakan |
| **Sediakan ruang gerak murah hati** | Latensi dapat diprediksi; tahan terhadap varians | Biaya kondisi mapan lebih tinggi; tampak "kurang terpakai" |
| **Batasi WIP (kanban)** | Lead time lebih pendek; lebih sedikit alih konteks | Terasa lebih lambat; butuh disiplin menahan batas |
| **Pemodelan antrean formal** | Keputusan kapasitas terkuantifikasi; kejutan lebih sedikit | Kurva belajar; model menyederhanakan kenyataan berantakan |
| **Hanya aturan praktis** | Cepat, tanpa matematika | Salah persis di tempat paling mahal (dekat kapasitas) |

Trade-off berulangnya **efisiensi versus keterprediksian**: mendorong utilisasi naik menghemat uang sampai tiba-tiba tidak, saat latensi, kegagalan, dan biaya pemadaman kebakaran mengerdilkan penghematan. Kontribusi teori antrean adalah memberi tahu *di mana* tebing itu agar trade-off menjadi pilihan, bukan kecelakaan.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apa target utilisasi eksplisit Anda untuk setiap sistem sensitif latensi, dan siapa yang menyetujuinya?** Ruang gerak adalah pembelian sengaja atas latensi yang dapat diprediksi, jadi ia harus menjadi kebijakan yang dinyatakan, bukan kecelakaan dari beban apa pun yang kebetulan tiba. Karena waktu respons naik tak linear, berjalan di 85% sudah dapat berarti latensi ekor meningkat, namun keuangan melihat ruang gerak sebagai pemborosan dan mendorong utilisasi naik. Bawa angkanya: utilisasi saat ini, kurva latensi terukur, dan biaya insiden latensi terakhir Anda, lalu tunjukkan di mana tebing berada untuk setiap layanan. Untuk sistem enterprise dan pemerintah dengan puncak musiman (musim pengajuan, jendela pendaftaran), tetapkan target menjauh dari tebing untuk puncak, bukan rata-rata. Jika tak ada yang memiliki target utilisasi, insiden latensi akan terus muncul "entah dari mana."

2. **Di mana dalam sistem Anda antrean tak terbatas, tanpa back-pressure untuk menumpahkan beban ketika kewalahan?** Antrean tak terbatas tidak gagal dengan anggun; ia merosot menjadi keruntuhan, karena kedatangan yang terus-menerus melampaui keberangkatan (rho >= 1) berarti antrean tumbuh tanpa batas. Inventarisasi antrean pesan, kolam thread, dan buffer permintaan Anda, dan tanyakan apa yang terjadi di masing-masing ketika laju kedatangan melampaui laju layanan: apakah ia menumpahkan beban, menerapkan back-pressure, atau tumbang? Ini sangat akut pada skala enterprise, di mana satu hilir yang jenuh dapat berkaskade lintas layanan. Bawa hasil uji beban atau insiden lampau di mana antrean menumpuk, dan periksa apakah sistem menolak kerja berlebih atau mencoba menahan semuanya. Perbaikannya adalah antrean terbatas dengan back-pressure eksplisit dan timeout yang diturunkan dari Hukum Little, agar kelebihan beban menumpahkan alih-alih menumbangkan.

3. **Apakah Anda memodelkan aliran gagasan-ke-produksi sebagai antrean dari antrean, dan apakah perbaikan Anda diarahkan pada kendala nyata?** Proses multitahap adalah antrean yang butirnya mengantre di tiap tahap, dan mengoptimalkan apa pun selain tahap kendala hanya memindahkan antrean. Petakan corong penyampaian Anda (integrasi ke UAT ke produksi, atau temukan ke definisikan ke kembangkan ke sampaikan) dan ukur laju kedatangan, layanan, tunggu, dan lewat di tiap tahap untuk menemukan di mana kerja benar-benar menumpuk. Tim rutin mengoptimalkan tahap yang paling mereka pahami alih-alih kemacetan, yang menghabiskan upaya dan tak menggerakkan apa pun. Bawa data waktu tunggu per tahap, bukan firasat, karena kemacetan sering berupa keadaan tunggu (tinjauan, persetujuan, ketersediaan lingkungan) alih-alih keadaan kerja. Begitu Anda tahu kendalanya, bidik ke sana dan biarkan non-kendala.

4. **Apakah Anda memakai Hukum Little untuk menetapkan batas WIP, atau Anda menambah kapasitas untuk menyembuhkan lead time yang hanya akan diperbaiki oleh lebih banyak disiplin?** Hukum Little mengatakan lead time sama dengan kerja-dalam-proses dibagi throughput, jadi jika Anda tak dapat menaikkan throughput, satu-satunya tuas tersisa untuk lead time lebih pendek adalah menurunkan WIP, yang tidak berbiaya selain pengendalian diri. Tarikan yang bersaing nyata: membatasi kerja dalam proses terasa lebih lambat dan menganggur, dan manajer di bawah tekanan lebih suka merekrut atau membeli perangkat keras daripada menyuruh tim memulai lebih sedikit dan menyelesaikan lebih banyak. Bawa angka kerasnya, butir terbuka saat ini dan laju penyelesaian per tahap, dan hitung lead time rata-rata tersirat, lalu bandingkan dengan apa yang orang percayai; celahnya biasanya besar dan memalukan. Di enterprise atau lembaga besar, permintaan perekrutan atau pengadaan yang dibenarkan sebagai perbaikan lead time harus diuji terhadap aritmetika ini lebih dulu, karena penambahan headcount yang menaikkan WIP dapat memperpanjang justru lead time yang hendak dipersingkat.

5. **Apakah Anda merencanakan kapasitas di sekitar rata-rata, atau Anda telah mengkuantifikasi variabilitas yang sebenarnya menciptakan antrean Anda?** Antrean terbentuk dari varians, bukan dari rata-rata, sehingga dua sistem dengan beban rata-rata identik dapat berperilaku sama sekali berbeda jika satu punya kedatangan berombak atau waktu layanan berekor panjang. Ketegangannya rata-rata mudah dikumpulkan dan menenangkan untuk dilaporkan, sementara varians dan ekor lebih sulit diukur dan tidak diinginkan dalam pembaruan status. Bawa distribusinya, bukan rata-ratanya: keberombakan kedatangan, waktu layanan dan tunggu persentil ke-95 dan ke-99, dan ukuran batch yang memusatkan kerja menjadi lonjakan. Untuk sistem enterprise dan pemerintah dengan lonjakan yang dapat diprediksi (musim pengajuan, putaran gaji, jendela pendaftaran, beban akhir kuartal), rencanakan penyangga dan target utilisasi dari varians periode puncak, karena desain yang diukur pada rata-rata tahunan akan gagal persis ketika publik menyaksikan.

6. **Antrean Anda yang mana yang diam-diam menghitung pembatalan dan penolakan seolah kerja itu dilayani, dan permintaan tak terpenuhi apa yang disembunyikannya?** Butir yang balking, reneging, atau ditolak meninggalkan antrean tanpa ditangani, dan mencatatnya sebagai "terlayani" merusak throughput, rasio galat, dan rencana kapasitas Anda sekaligus. Pertimbangan yang bersaing adalah "panggilan dijawab" atau "tiket ditutup" tampak lebih baik di dasbor daripada "penelepon yang menyerah," sehingga angka jujurnya adalah yang tak ada yang sukarela memunculkan. Bawa laju lewat (σ), hitungan balking dan reneging, dan selisih antara beban yang ditawarkan dan beban yang dilayani, agar permintaan sebenarnya terlihat. Ini tajam dalam penyampaian layanan pemerintah, di mana warga yang meninggalkan antrean telepon atau aplikasi tunjangan adalah kewajiban yang tak terpenuhi alih-alih kasus yang diselesaikan, dan melaporkannya sebagai tertangani keliru menyatakan kinerja sekaligus meremehkan kapasitas yang menjadi hak publik.

## Lensa sektor

**Startup.** Anda tak punya waktu untuk pemodelan antrean formal dan tak membutuhkannya. Raih dua kemenangan termurah lebih dulu: terapkan Hukum Little pada backlog Anda untuk melihat lead time nyata yang tersirat WIP Anda, dan awasi papan kanban untuk tahap tempat kerja menumpuk sebelum Anda merekrut melawan kemacetan yang mungkin tak ada. Jaga utilisasi menjauh dari tebing pada jalur sensitif latensi mana pun dengan menyisakan ruang gerak alih-alih menyetelnya, karena pemadaman selama lonjakan pertumbuhan lebih mahal daripada sedikit kapasitas menganggur.

**Bisnis kecil.** Tanpa spesialis antrean di staf, beli metriknya alih-alih membangun modelnya. Pilih help desk, message broker, atau platform hosting yang sudah melaporkan laju kedatangan, waktu tunggu, dan pembatalan, dan baca angka itu alih-alih menurunkannya. Bingkai keputusan sebagai mengawasi dua gejala: tunggu yang naik tak linear seiring Anda makin sibuk, dan pelanggan yang menyerah sebelum dilayani, karena pelanggan hilang adalah biaya antrean yang paling menyakiti bisnis kecil.

**Enterprise.** Kerjanya menjadikan pemikiran antrean disiplin bersama di banyak tim: satu notasi yang disepakati (λ, μ, ρ, lead time), kebijakan WIP dan ruang gerak utilisasi yang konsisten, dan standar back-pressure agar hilir yang jenuh tidak berkaskade lintas layanan. Tetapkan SLO dan kapasitas dari analisis antrean alih-alih tebakan, dan kelola antrean Anda sebagai portofolio dengan garis dasar dan tinjauan agar tak ada satu tim pun berjalan panas dalam isolasi. Tanamkan analisis ke tata kelola kapasitas dan audit, sehingga target ruang gerak adalah keputusan terdokumentasi yang dimiliki seseorang.

**Pemerintah.** Pengadaan, transparansi, dan akuntabilitas publik membentuk setiap pilihan kapasitas. Ukur pusat kontak dan sistem yang menghadap warga dari varians periode puncak (musim pengajuan, jendela pendaftaran), bukan rata-rata tahunan, dan isi staf untuk menjaga utilisasi menjauh dari tebing ketika permintaan melonjak. Lacak balking dan reneging sebagai permintaan publik yang tak terpenuhi alih-alih menyembunyikannya dalam "panggilan dijawab," dan benarkan belanja kapasitas dengan perkiraan waktu tunggu Hukum Little, yang memberi auditor dan pejabat terpilih kasus berbasis matematika yang dapat dipertahankan alih-alih anekdot.

## Contoh

**Startup.** Tim SaaS lima orang yang tenggelam dalam backlog dukungan mengasumsikan mereka perlu merekrut agen lagi. Sebelum membelanjakan uang, mereka menerapkan Hukum Little: 60 tiket terbuka dan 12 ditutup per hari berarti tiket rata-rata menunggu sekitar 5 hari, yang cocok dengan email marah. Mengamati papan kanban, mereka memperhatikan tiket menumpuk menunggu rekayasa, bukan dukungan, sehingga mereka membatasi kerja dalam proses dan mengarahkan laporan bug langsung ke sprint alih-alih membiarkannya mengantre. Lead time turun ke di bawah dua hari tanpa rekrutan baru, dan mereka memakai anggaran yang dibebaskan untuk kemacetan sebenarnya.

**Enterprise.** Platform pembayaran yang mengukur layanan otorisasinya mengukur λ ≈ 850 permintaan/detik dan μ per-node ≈ 200/detik. Secara naif itu ~5 node (ρ = 0,85), tetapi mengetahui bahwa ρ = 0,85 sudah berarti latensi ekor meningkat tajam, tim menyediakan sampai ρ ≈ 0,65 dan memakai Hukum Little untuk memprediksi jumlah permintaan dalam penerbangan serta menetapkan kedalaman antrean dan timeout. Insiden musim puncak yang dulu muncul "entah dari mana" lenyap, karena tim tak lagi beroperasi pada bagian curam kurva.

**Pemerintah.** Pusat kontak badan pajak memodelkan dukungan musim pengajuan sebagai antrean: lonjakan kedatangan (λ), kapasitas agen (μ), dan, yang krusial, **laju lewat (σ)** warga yang menyerah setelah tunggu panjang. Dengan melacak balking dan reneging dan bukan hanya "panggilan dijawab," pimpinan melihat permintaan sebenarnya yang tak terpenuhi, mengisi staf untuk menjaga utilisasi menjauh dari tebing selama puncak, dan membenarkan kapasitas tambahan dengan perkiraan waktu tunggu Hukum Little, kasus berbasis matematika yang dapat dipertahankan untuk belanja publik alih-alih yang anekdotal.

## Kasus bisnis: motivasi, ROI, dan TCO

Teori antrean membuahkan hasil dengan mencegah dua kesalahan mahal: **penyediaan berlebih** (membayar kapasitas menganggur yang tak Anda butuhkan) dan, jauh lebih merusak, **penyediaan kurang dekat tebing** (di mana kenaikan beban kecil menyebabkan latensi besar, SLA dilanggar, pelanggan yang meninggalkan, dan belanja darurat). Karena biaya berjalan dekat utilisasi 100% tak linear, penghematan dari "tambah sedikit beban" kecil dan sisi rugi katastrofik, persis asimetri yang diubah sedikit matematika menjadi keputusan sengaja. Imbal hasilnya diukur dalam pemadaman yang dihindari, SLA yang terpenuhi, pelanggan yang dipertahankan yang kalau tidak akan balking, dan rotasi on-call yang lebih tenang.

Pada **total biaya kepemilikan**, kerangka ini murah diadopsi (ia pengetahuan, bukan perkakas) dan memperbaiki hampir setiap keputusan kapasitas, latensi, dan aliran yang dibuat organisasi besar sepanjang umur sistem. Hukum Little dan batas WIP mengurangi lead time tanpa membeli apa pun (kemenangan proses murni), sementara disiplin utilisasi menukar biaya kondisi mapan yang sederhana dan dapat diprediksi dengan penghapusan kegagalan yang mahal dan tak dapat diprediksi. Untuk mengajukan kasus kepada pimpinan, terjemahkan insiden latensi terbaru ke kurva utilisasi dan tunjukkan bagaimana target ruang gerak akan mencegahnya, dan pakai Hukum Little untuk menghubungkan pengurangan WIP langsung dengan penyampaian lebih cepat.

## Anti-pola dan jebakan

- **Merencanakan kapasitas di sekitar rata-rata:** mengabaikan varians, yang sebenarnya menciptakan antrean.
- **Berjalan panas:** menargetkan utilisasi 90%+ pada sistem sensitif latensi dan terkejut oleh latensi ekor.
- **Menghitung lewatan sebagai layanan:** memperlakukan pelanggan yang menyerah atau tiket yang ditolak sebagai tertangani, merusak metrik.
- **Menumpuk WIP:** menyamakan kesibukan dengan throughput dan memperpanjang lead time.
- **Mengoptimalkan non-kemacetan:** memperbaiki tahap yang bukan kendala dan memindahkan antrean ke tempat lain.
- **Mencampuradukkan MTTR:** melaporkan "pemulihan" sambil mengukur "perbaikan," atau sebaliknya.
- **Antrean tak terbatas:** tanpa back-pressure, sehingga sistem kelebihan beban merosot menjadi keruntuhan alih-alih menumpahkan beban.
- **Rata-rata sebagai maksimum:** mendesain ke rata-rata dan dipanggil oleh ekor.

## Model kematangan

- **Tingkat 1, Memulai:** Antrean (tiket, tugas, pesan, deploy) tak dikelola dan reaktif; kapasitas ditebak; utilisasi berjalan di mana pun beban mendarat; masalah latensi mengejutkan tim dan dipadamkan setelah kejadian.
- **Tingkat 2, Mengembangkan:** Beberapa tim mengumpulkan metrik dasar (throughput, rata-rata tunggu) tetapi membacanya sebagai rata-rata dan menerapkannya tidak konsisten; sebagian kelompok membatasi WIP atau menyisakan ruang gerak sementara yang lain berjalan panas; tak ada notasi bersama, sehingga praktik tidak menjalar antar tim.
- **Tingkat 3, Membakukan:** Notasi umum (λ, μ, ρ, lead time) didokumentasikan dan ditegakkan di seluruh organisasi; batas WIP dan target ruang gerak utilisasi ditetapkan dengan sengaja untuk setiap sistem sensitif latensi; beberapa MTTR dibedakan; antrean terbatas dengan back-pressure adalah bawaan di semua layanan.
- **Tingkat 4, Mengelola:** Antrean diukur dan dikendalikan terhadap garis dasar: laju kedatangan, laju layanan, utilisasi, latensi ekor (p95/p99), dan lead time dilacak terhadap target dan SLO terdefinisi; kedalaman antrean, timeout, dan ruang gerak diturunkan dari Hukum Little alih-alih ditebak; balking, reneging, dan laju lewat dihitung sehingga beban yang ditawarkan dibedakan dari beban yang dilayani; keputusan kapasitas ditinjau atas bukti ini, bukan firasat.
- **Tingkat 5, Mengorkestrasi:** Aliran dimodelkan terus-menerus sebagai antrean dari antrean; kemacetan diidentifikasi dan dilonggarkan sebagai praktik berkelanjutan; kapasitas, SLO, dan back-pressure beradaptasi dengan permintaan dan varians yang bergeser; metrik antrean terikat langsung dengan DORA dan KPI bisnis, dan organisasi menyeimbangkan ulang kapasitas di seluruh aliran seiring gambaran beban dan risiko berubah.

## Gagasan untuk didiskusikan

1. Pada utilisasi berapa sistem sensitif latensi Anda sebenarnya berjalan, dan di mana tebingnya?
2. Terapkan Hukum Little pada backlog Anda saat ini: lead time apa yang tersirat dari WIP ÷ throughput Anda, dan apakah cocok dengan kenyataan?
3. Antrean Anda yang mana yang diam-diam menghitung "lewatan" (pembatalan, penolakan) seolah dilayani?
4. Di mana menurunkan WIP akan memperpendek lead time lebih murah daripada menambah kapasitas?
5. Tahap mana dalam aliran gagasan-ke-produksi Anda yang kemacetan sebenarnya, dan apakah perbaikan Anda diarahkan ke sana?
6. Apakah dasbor Anda menunjukkan rata-rata di mana ekornya yang sebenarnya menyakiti Anda?

## Poin-poin utama

- Antrean pelanggan, papan kanban, antrean pesan, dan jalur deploy semuanya antrean yang diatur hukum yang sama.
- **Hukum Little (κ = λτ)** menjangkarkan perencanaan aliran: lead time = WIP ÷ throughput.
- Utilisasi dan waktu tunggu **tak linear**: sediakan ruang gerak; 15% terakhir adalah yang paling mahal.
- Lacak gambaran penuh: kedatangan, layanan, keberhasilan, **kegagalan dan lewatan**, dan tunggu; jangan biarkan pembatalan bersembunyi.
- Modelkan proses sebagai **antrean dari antrean** dan perbaiki **kemacetan**, bukan kesibukan.
- Metrik antrean dipetakan langsung ke ukuran **DORA/aliran** dan **SLI/SLO** (bab 11.1, 11.2, 9.1), memberi seluruh organisasi satu bahasa untuk kapasitas dan aliran.

## Referensi dan bacaan lanjutan

- Bob Wescott, *Seven Insights into Queueing Theory* (dan *The Every Computer Performance Book*).
- John D. C. Little, "A Proof for the Queuing Formula L = λW" (1961): Hukum Little.
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate*: metrik DORA berbasis aliran yang selaras dengan KPI antrean.
- Donald Reinertsen, *The Principles of Product Development Flow*: antrean, ukuran batch, dan ekonomi WIP.
- Daniel Vacanti, *Actionable Agile Metrics for Predictability*: Hukum Little diterapkan pada kanban.
- Joel Parker Henderson, *Queueing Theory*: notasi, KPI, dan antrean-dari-antrean (github.com/joelparkerhenderson/queueing-theory).
- Dan Slimmon, "The most important thing to understand about queues" (2016).
- Wikipedia: "Queueing theory," "M/M/1 queue," "Little's law," "Markov chain."
