# 8.1 CI/CD dan pengiriman

## Tinjauan dan motivasi

[Integrasi berkelanjutan](https://en.wikipedia.org/wiki/Continuous_integration) dan [pengiriman berkelanjutan](https://en.wikipedia.org/wiki/Continuous_delivery) (CI/CD) adalah jaringan penghubung antara menulis kode dan menaruhnya di depan pengguna dengan aman. Integrasi berkelanjutan berarti setiap perubahan sering di-merge ke mainline bersama, lalu otomatis dibangun dan diuji, sehingga masalah integrasi muncul dalam hitungan menit alih-alih di akhir siklus rilis yang panjang. Pengiriman berkelanjutan berarti setiap perubahan yang lolos pipeline dijaga dalam keadaan dapat di-deploy, sehingga merilis ke produksi menjadi keputusan bisnis alih-alih kerepotan rekayasa. [Deployment berkelanjutan](https://en.wikipedia.org/wiki/Continuous_deployment) melangkah satu tahap lebih jauh dan merilis setiap perubahan yang lolos secara otomatis, tanpa gerbang manusia.

Bagi tim besar, perbedaan ini sangat penting. Ketika ratusan insinyur meng-commit ke sistem yang tumpang tindih, biaya integrasi manual dan pengujian manual tumbuh secara non-linear. Pipeline otomatis bersama adalah satu-satunya cara praktis untuk memberi banyak kontributor umpan balik cepat dan tepercaya serta mencegah perubahan satu tim diam-diam merusak perubahan tim lain. Pipeline menjadi sumber kebenaran tunggal tentang apakah perangkat lunak sehat, dan ia menegakkan konsistensi yang tak dapat dijamin dokumentasi atau niat baik pada skala besar.

Konteks enterprise dan pemerintah menambah satu dimensi lagi: kemampuan diaudit dan kendali perubahan. Regulator, petugas keamanan, dan auditor membutuhkan bukti bahwa perubahan telah ditinjau, diuji, dan disetujui, dan bahwa artefak yang berjalan di produksi persis yang dibangun dan diperiksa. Pipeline CI/CD yang dirancang baik mengubah kewajiban kepatuhan ini dari beban administrasi menjadi produk sampingan otomatis alur kerja rekayasa normal. Dilakukan dengan baik, pengiriman menjadi lebih cepat dan lebih aman sekaligus, yang merupakan hasil yang paling penting bagi pimpinan.

*Lihat juga:* bab 8.4 (rekayasa platform dan pengalaman pengembang), bab 8.5 (otomasi pengujian dan proses), dan bab 7.4 (analitik produk dan eksperimen) untuk praktik [feature flag](https://en.wikipedia.org/wiki/Feature_toggle) (sakelar runtime yang mengekspos fungsionalitas kepada pengguna tanpa deploy ulang) dan eksperimen yang dimungkinkan pengiriman progresif (merilis perubahan secara bertahap sambil otomatis memantau metrik kesehatannya).

## Prinsip utama

- Integrasikan perubahan kecil sesering mungkin; branch berumur panjang adalah musuh integrasi berkelanjutan.
- Bangun artefak sekali dan promosikan artefak identik melalui setiap lingkungan.
- Jadikan pipeline gerbang otoritatif: jika hijau, perubahan siap dikirim; jika merah, pekerjaan berhenti sampai diperbaiki.
- Optimalkan umpan balik cepat tanpa henti agar pengembang tetap dalam alur dan cacat tertangkap selagi konteks segar.
- Otomatiskan segala yang berulang, termasuk uji, pemindaian keamanan, penyediaan, dan deployment.
- Perlakukan definisi pipeline sebagai kode terkontrol versi yang ditinjau, bukan konfigurasi konsol yang diklik.
- Rancang rilis yang aman dan dapat dibalik agar deployment mana pun dapat dibatalkan dengan cepat.
- Pisahkan deployment (memasang kode) dari rilis (mengeksposnya kepada pengguna) memakai feature flag.

## Rekomendasi

### Rancang pipeline sebagai rangkaian gerbang kualitas

Susun pipeline menjadi tahap yang berkembang dari murah dan cepat ke mahal dan menyeluruh: compile dan unit test dulu, lalu uji integrasi, pemindaian keamanan dan lisensi, dan akhirnya deployment ke staging dan produksi. Setiap tahap adalah gerbang yang harus dilewati perubahan. Urutkan gerbang agar pemeriksaan tercepat dan paling mungkin gagal berjalan lebih dulu, yang memberi pengembang umpan balik dalam waktu sesingkat mungkin. Jaga loop umpan balik tahap commit di bawah sepuluh menit di mana pun Anda bisa. Lebih dari itu, pengembang berganti konteks dan produktivitas turun.

### Bangun sekali, promosikan di mana-mana

Hasilkan satu artefak tak berubah di tahap build dan promosikan artefak persis itu melalui test, staging, dan produksi. Jangan pernah membangun ulang per lingkungan, karena build ulang dapat diam-diam memperkenalkan perbedaan. Konfigurasi yang bervariasi menurut lingkungan harus disuntikkan saat deploy, bukan dipanggang ke dalam build terpisah. Praktik ini juga yang memungkinkan Anda memberi tahu auditor, dengan pasti, bahwa biner di produksi adalah yang lolos setiap gerbang.

### Jadikan pipeline titik penegakan kebijakan

Kodekan pemeriksaan wajib (persetujuan tinjauan kode, ambang cakupan uji, hasil pemindaian keamanan, commit bertanda tangan) langsung ke dalam pipeline dan aturan proteksi branch. Kebijakan manual yang hidup di wiki rutin dilewati di bawah tekanan tenggat. Kebijakan yang dikodekan dalam pipeline diterapkan seragam dan otomatis pada setiap perubahan.

### Jaga mainline selalu dapat dirilis

Pakai pengembangan berbasis trunk, yang mengintegrasikan semua pekerjaan ke satu branch bersama dengan sedikit atau tanpa branch berumur panjang, atau pakai feature branch berumur pendek, dan andalkan feature flag untuk menyembunyikan pekerjaan belum selesai alih-alih branch berumur panjang. Ini menjaga konflik merge tetap kecil dan menjaga mainline selalu dalam keadaan dapat di-deploy, yang merupakan prasyarat pengiriman berkelanjutan sejati.

### Pilih strategi deployment dengan sengaja

Cocokkan strategi deployment dengan risiko dan radius ledakan layanan:

- Deployment **rolling** mengganti instans secara bertahap dan merupakan bawaan masuk akal untuk layanan tanpa status.
- **[Blue-green](https://en.wikipedia.org/wiki/Blue-green_deployment)** memelihara dua lingkungan identik dan mengalihkan lalu lintas sekaligus, memberi jalur rollback instan.
- Rilis **canary** merutekan persentase kecil lalu lintas ke versi baru, mengawasi metrik kesehatan, dan memperluas hanya jika sinyalnya baik.
- **Feature flag** memisahkan rilis dari deployment, memungkinkan Anda mengaktifkan fungsionalitas untuk pengguna atau kohort tertentu tanpa deploy ulang.

### Adopsi pengiriman progresif dengan rollback otomatis

Pengiriman progresif memadukan rilis canary dengan analisis otomatis metrik seperti tingkat galat, latensi, dan saturasi. Definisikan kriteria kesehatan objektif di muka, lalu biarkan sistem mempromosikan atau me-rollback secara otomatis berdasarkan sinyal itu. Rollback otomatis menghilangkan keraguan manusia yang mengubah insiden kecil menjadi besar.

### Sediakan manajemen rilis dan kendali perubahan untuk lingkungan teregulasi

Dalam pengaturan teregulasi, simpan catatan manajemen perubahan yang ringan tetapi nyata. Tangkap otomatis siapa yang menyetujui setiap perubahan, uji apa yang berjalan, dan artefak apa yang di-deploy. Pakai proses penasihat perubahan untuk perubahan yang benar-benar berisiko tinggi, tetapi sisihkan untuk kasus itu. Mengalirkan setiap perubahan rutin melalui dewan mingguan menghancurkan nilai otomasi. Bidik sebagai gantinya jenis perubahan standar yang telah disetujui sebelumnya yang mengalir melalui pipeline tanpa upacara.

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan | Paling cocok |
|---|---|---|---|
| Pengiriman berkelanjutan (gerbang rilis manual) | Bisnis mengendalikan waktu; kuat untuk jendela rilis teregulasi | Butuh disiplin menjaga mainline siap kirim | Enterprise dengan jendela perubahan |
| Deployment berkelanjutan (sepenuhnya otomatis) | Umpan balik tercepat; batch terkecil | Menuntut uji dan observabilitas matang | Tim berkepercayaan tinggi dan berfrekuensi tinggi |
| Blue-green | Rollback instan; model mental sederhana | Menggandakan biaya lingkungan saat peralihan | Layanan kritis yang butuh pengembalian cepat |
| Canary + pengiriman progresif | Membatasi radius ledakan; digerakkan data | Kompleks dibangun; butuh metrik baik | Sistem menghadap pengguna skala besar |
| Feature flag | Memisahkan deploy dari rilis | Utang flag jika tak dibersihkan | Tim yang mengirim pekerjaan belum selesai dengan aman |

Trade-off sentralnya adalah kecepatan versus kendali, tetapi itu sering pilihan palsu. Otomasi matang memberi keduanya: rilis lebih cepat karena lebih kecil, dan lebih aman karena masing-masing diverifikasi dan dapat dibalik. Biaya sebenarnya adalah investasi di muka dalam cakupan uji, observabilitas, dan rekayasa pipeline, plus disiplin berkelanjutan menjaganya tetap sehat. Organisasi yang pelit pada investasi itu mendapat kecepatan tanpa keamanan, yang lebih buruk daripada proses manual yang lambat.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apa target Anda untuk waktu umpan balik tahap commit, dan apa yang dipotong ketika rangkaian uji melampaui sepuluh menit?** Tahap commit yang lambat diam-diam membunuh integrasi berkelanjutan, karena pengembang berhenti menunggu hijau dan mulai menumpuk perubahan. Putuskan angkanya sekarang (bab ini berargumen di bawah sepuluh menit) dan putuskan mekanisme untuk menjaganya: pekerja paralel, piramida uji yang ketat, dan memindahkan pemeriksaan integrasi lambat ke tahap berikutnya. Pada skala enterprise ini keputusan platform, karena ratusan insinyur berbagi pipeline yang sama dan setiap menit tambahan berlipat ke setiap commit. Bawa data nyata ke rapat: durasi pipeline p50 dan p95 saat ini, sepuluh uji paling lambat, dan seberapa sering orang menjalankan ulang alih-alih menunggu. Jika Anda tak dapat menyatakan target dan mempertahankannya dengan angka, pipeline Anda bergeser menuju proses batch yang mengenakan kostum CI.

2. **Strategi deployment mana yang dipakai setiap layanan, dan siapa yang akuntabel atas pilihan itu?** Rolling, blue-green, dan canary tidak dapat dipertukarkan: mereka menukar biaya, kecepatan rollback, dan kompleksitas secara berbeda, dan pilihan tepat bergantung pada radius ledakan layanan. Blue-green membeli rollback instan dengan harga lingkungan ganda selama peralihan, yang sepadan untuk sistem pembayaran dan boros untuk dasbor internal. Canary membatasi paparan tetapi menuntut metrik kesehatan baik dan lebih banyak rekayasa pipeline. Untuk properti besar atau teregulasi, menyerahkan ini pada kebiasaan tiap tim menghasilkan inkonsistensi yang muncul selama insiden, jadi sepakati bawaan per tingkat layanan dan catat keputusannya. Bawa katalog layanan Anda dan tandai setiap layanan dengan strateginya, jalur rollback-nya, dan orang yang memiliki keputusan itu.

3. **Bagaimana Anda membuktikan artefak di produksi persis yang lolos setiap gerbang?** Bangun sekali dan promosikan artefak identik adalah seluruh permainan untuk kemampuan diaudit, dan ia patah begitu ada yang membangun ulang per lingkungan atau menambal mesin berjalan. Dalam pengaturan enterprise dan pemerintah auditor akan meminta Anda menelusuri biner berjalan kembali ke commit, tinjauan, dan persetujuannya, dan Anda ingin jawabannya memakan detik, bukan seminggu. Putuskan bagaimana Anda menegakkannya: artefak tak berubah, citra bertanda tangan, verifikasi tanda tangan saat deploy, dan konfigurasi disuntikkan saat deploy alih-alih dipanggang ke build terpisah. Bawa celah saat ini ke meja, seperti tahap mana pun yang membangun ulang, jalur hotfix manual mana pun, dan di mana pun config mencabangkan artefak. Jawabannya menentukan apakah bukti kepatuhan Anda adalah produk sampingan pipeline atau kerepotan manual sebelum setiap audit.

4. **Ketika mainline menjadi merah, apa yang sebenarnya berhenti, dan bagaimana Anda menangani uji flaky?** Pipeline hanya gerbang otoritatif jika build merah benar-benar menghentikan pekerjaan, namun banyak organisasi diam-diam menoleransi mainline rusak dan tumpukan kegagalan sesekali, yang melatih pengembang menjalankan ulang sampai hijau dan mengirim di atas kegagalan. Bagi tim besar pembusukan ini bertumpuk, karena flake yang diabaikan satu tim menjadi dalih semua orang untuk melewati gerbang, dan kepercayaan pada pipeline jauh lebih murah dijaga daripada dibangun ulang. Timbang tarikan yang bersaing: aturan hentikan-lini yang ketat melindungi kualitas tetapi dapat memblokir ratusan insinyur karena satu commit buruk, sementara kebijakan longgar menjaga throughput dan mengikis gerbang. Bawa bukti ke diskusi: waktu merah mainline Anda saat ini, jumlah uji terkarantina atau flaky, tingkat jalankan-ulang, dan seberapa sering perubahan di-merge di atas pemeriksaan gagal. Dalam pengaturan enterprise dan pemerintah, namai siapa yang memiliki triase flake dan siapa yang berwenang membekukan merge, karena gerbang yang tak ada yang bertanggung jawab menegakkannya adalah yang akan ditemukan auditor rutin dilewati.

5. **Apa siklus hidup feature flag Anda, dan siapa yang bertanggung jawab memensiunkannya?** Flag adalah yang memungkinkan Anda memisahkan deployment dari rilis dan menyembunyikan pekerjaan belum selesai, tetapi setiap flag adalah cabang dalam kode Anda yang tak dibersihkan sendiri, dan flag tak terkelola menumpuk menjadi kompleksitas kondisional yang tak berani disentuh siapa pun. Dalam properti besar utang ini berbahaya, karena flag basi dapat diam-diam menggerbangi perbaikan keamanan atau membalik jalur kode yang tak teruji ke produksi, dan orang yang membuatnya sering sudah pindah. Seimbangkan ketegangan: flag membeli pengiriman bertahap yang aman, jadi tujuannya bukan lebih sedikit flag melainkan siklus hidup disiplin dengan pemilik, ekspektasi kedaluwarsa, dan perkakas yang memunculkan yang basi. Bawa inventaris saat ini ke rapat: berapa flag hidup, seberapa tua yang tertua, mana yang tak punya pemilik, dan apakah ada flag berumur panjang yang kini berfungsi sebagai konfigurasi permanen yang seharusnya di tempat lain. Untuk lingkungan teregulasi, tambahkan siapa yang dapat mengubah flag di produksi dan apakah perubahan itu dicatat dengan ketelitian sama seperti deployment, karena membalik flag adalah rilis bahkan ketika pipeline tak pernah berjalan.

6. **Di mana batas antara pengiriman berkelanjutan dengan gerbang manusia dan deployment berkelanjutan penuh, dan siapa yang menetapkan ambang rollback?** Pengiriman berkelanjutan menjaga orang mengendalikan waktu rilis, yang cocok untuk jendela perubahan menurut undang-undang dan sistem berradius ledakan tinggi, sementara deployment berkelanjutan mengirim setiap perubahan lolos secara otomatis dan menuntut uji, observabilitas, dan rollback otomatis yang matang agar aman. Bagi organisasi besar atau teregulasi jawabannya jarang seragam: situs pemasaran Anda dapat di-deploy berkelanjutan sementara inti pembayaran Anda menjaga gerbang manusia terdokumentasi, dan menarik garis itu per tingkat layanan mencegah gesekan tak perlu maupun otomasi sembrono. Pertimbangan yang bersaing adalah kecepatan dan ukuran batch melawan kendali dan kemampuan diaudit, plus biaya rekayasa metrik kesehatan yang dibutuhkan rollback otomatis. Bawa buktinya: tingkat kegagalan perubahan per layanan, mean time to recovery, irama rilis saat ini, dan sinyal objektif (tingkat galat, latensi, saturasi) yang akan Anda percaya untuk mempromosikan atau me-rollback tanpa manusia. Dalam pengaturan pemerintah dan enterprise, kaitkan setiap tingkat dengan siapa yang memiliki ambang rollback dan siapa yang menyetujui perpindahan apa pun dari rilis bergerbang ke otomasi penuh, agar keputusan disengaja alih-alih melayang.

## Lensa sektor

**Startup.** Bersandarlah pada CI/CD terkelola sejak hari pertama: runner ter-hosting, satu pipeline, satu citra tak berubah, dan deploy otomatis ke staging saat merge. Jangan membangun infrastruktur pipeline yang kemudian harus Anda pelihara. Feature flag memungkinkan dua atau tiga insinyur me-merge pekerjaan setengah jadi dengan aman dan mengirim beberapa kali sehari, dan deploy produksi satu klik plus flag-off cepat adalah semua kendali perubahan yang Anda butuhkan sampai skala memaksa lebih.

**Bisnis kecil.** Tanpa platform atau insinyur rilis khusus, pilih pipeline yang diberikan host sumber Anda (Actions bawaan atau setara) dan strategi deployment bawaannya daripada apa pun yang pesanan. Bingkai pilihan beli-versus-bangun dengan jujur: pipeline terkelola dan platform hosting dengan rollback bawaan berbiaya lebih rendah daripada jam-insinyur yang dikonsumsi penyiapan pesanan. Jaga yang esensial, yaitu bangun sekali, promosikan artefak yang sama, dan pengembalian mudah, dan lewati mesin pengiriman progresif sampai volume membenarkannya.

**Enterprise.** Masalah intinya konsistensi lintas banyak tim: bakukan templat pipeline bersama yang menegakkan tinjauan, pemindaian, artefak tak berubah bertanda tangan, dan strategi deployment per tingkat, agar kualitas tidak bervariasi tim demi tim. Perlakukan definisi pipeline sebagai kode yang ditinjau, tangkap bukti kendali perubahan secara otomatis, dan kelola feature flag serta ambang rollback sebagai aset teratur alih-alih kebiasaan pribadi tiap tim. Imbalannya pengiriman lebih cepat dan bukti audit yang dihasilkan sebagai produk sampingan alih-alih kerepotan triwulanan.

**Pemerintah.** Aturan pengadaan, jendela perubahan menurut undang-undang, dan akuntabilitas publik membentuk pipeline. Pilih pengiriman berkelanjutan dengan gerbang rilis manusia terdokumentasi daripada otomasi penuh untuk sistem berdampak, klasifikasikan pekerjaan rutin sebagai perubahan standar yang disetujui sebelumnya, dan jaga jalur rollback instan (blue-green atau canary otomatis) untuk layanan yang diandalkan warga selama jendela tahunan yang sempit. Pastikan pipeline mencatat siapa yang menyetujui setiap perubahan, uji apa yang berjalan, dan artefak mana yang di-deploy, agar kewajiban transparansi dan audit dipenuhi oleh alur kerja normal alih-alih kertas manual.

## Contoh

**Startup.** Startup SaaS empat orang menyambungkan satu pipeline GitHub Actions yang menjalankan unit test, membangun satu citra Docker, dan men-deploy citra yang sama itu ke staging secara otomatis pada setiap merge ke main. Deploy produksi satu klik, dan para pendiri bersandar pada feature flag agar dapat me-merge pekerjaan setengah jadi di balik flag alih-alih menjaga branch tetap hidup berminggu-minggu. Ketika rilis buruk lolos, mereka membalik flag mati dalam hitungan detik dan memperbaikinya dengan tenang, yang menjaga tim kecil mereka mengirim beberapa kali sehari tanpa orang ops khusus.

**Enterprise.** Sebuah bank global mengonsolidasikan puluhan pekerjaan Jenkins khusus tim menjadi templat pipeline terbakukan yang diwarisi setiap tim produk. Templat menegakkan analisis statis, pemindaian dependensi, dan artefak bertanda tangan tak berubah, dan men-deploy lewat canary dengan rollback otomatis yang dikaitkan pada ambang tingkat galat dan latensi. Karena artefak yang sama dipromosikan dari test ke produksi dan setiap gerbang dicatat, auditor bank dapat menelusuri biner produksi mana pun kembali ke commit, tinjauan, dan persetujuannya dalam hitungan detik, menggantikan latihan pengumpulan bukti manual triwulanan.

**Pemerintah.** Sebuah otoritas pajak nasional yang memodernisasi sistem pengajuan mengadopsi pengiriman berkelanjutan dengan gerbang rilis manusia eksplisit, agar dapat menghormati jendela perubahan menurut undang-undang selama musim pengajuan. Perubahan rutin diklasifikasikan sebagai perubahan standar yang disetujui sebelumnya yang mengalir otomatis ke staging. Rilis produksi memerlukan satu persetujuan terdokumentasi yang dicatat pipeline. Deployment blue-green memberi lembaga jalur rollback instan jika cacat mencapai produksi, yang krusial ketika jutaan warga bergantung pada layanan selama jendela tahunan yang sempit.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil investasi CI/CD tampak sebagai lead time perubahan yang berkurang, tingkat kegagalan perubahan yang lebih rendah, dan pemulihan lebih cepat ketika insiden terjadi: metrik yang secara konsisten dikaitkan riset dengan kinerja pengiriman dan hasil organisasi. Rilis lebih cepat dan lebih kecil memangkas overhead koordinasi yang menghabiskan kapasitas rekayasa pada skala besar, dan verifikasi otomatis memangkas pekerjaan mahal dan melemahkan semangat memadamkan cacat produksi.

Total biaya kepemilikan menimbang biaya adopsi terhadap biaya tidak mengadopsi. Biaya adopsi mencakup membangun dan memelihara pipeline, menumbuhkan cakupan uji, dan berinvestasi pada observabilitas dan staf platform. Biaya tidak mengadopsi lebih besar tetapi kurang terlihat: rilis manual yang lambat, nyeri integrasi, insiden produksi yang merusak reputasi, dan, dalam pengaturan teregulasi, audit gagal dan remediasi. Bagi pimpinan, argumen paling baik dibingkai dalam pengurangan risiko dan kapasitas. Otomasi mengubah waktu insinyur senior yang langka dari kerja membosankan rilis berulang menjadi kerja produk, sambil membuat pemadaman lebih jarang dan lebih singkat.

## Anti-pola dan jebakan

- **Pipeline snowflake.** Setiap tim membangun sendiri pipeline unik, sehingga perbaikan tak dapat dibagikan dan kualitas bervariasi liar.
- **Build ulang per lingkungan.** Membangun ulang untuk setiap tahap mematahkan jaminan "bangun sekali" dan membiarkan perbedaan halus mencapai produksi.
- **Build merah yang diabaikan.** Menoleransi mainline yang terus rusak menghancurkan kepercayaan pada pipeline dan menormalkan pengiriman di atas kegagalan.
- **Uji flaky yang tak ditangani.** Kegagalan sesekali melatih pengembang menjalankan ulang sampai hijau, menggagalkan tujuan gerbang.
- **Teater persetujuan manual.** Dewan penasihat perubahan yang mengecap semuanya menambah penundaan tanpa menambah keamanan.
- **Utang flag.** Feature flag yang tak pernah dihapus menumpuk menjadi kompleksitas kondisional yang tak dapat dipelihara.
- **Deploy sama dengan rilis.** Menggabungkan keduanya berarti setiap perubahan menghadap pengguna membutuhkan deploy ulang berisiko.

## Model kematangan

**Tingkat 1: Memulai.** Build dan deployment sebagian besar manual, ad hoc, dan reaktif. Integrasi terjadi terlambat, rilis jarang dan menegangkan, rollback berarti men-deploy versi lama dengan tangan, dan tak ada gagasan bersama tentang gerbang pipeline.

**Tingkat 2: Mengembangkan.** Build dan unit test otomatis berjalan pada setiap commit, tetapi praktik bervariasi tim demi tim. Deployment dibuat skrip namun masih dipicu dan diawasi secara manual, sebagian lingkungan konsisten, dan artefak mungkin masih dibangun ulang per tahap. Di mana pipeline ada, ia sering snowflake yang tak dapat dibagikan.

**Tingkat 3: Membakukan.** Templat pipeline terbakukan dan terdokumentasi ditegakkan lintas tim. Ia mempromosikan satu artefak tak berubah melalui semua lingkungan, menerapkan gerbang kualitas dan keamanan otomatis, mengodekan pemeriksaan wajib seperti persetujuan tinjauan dan hasil pemindaian, dan menangkap catatan perubahan secara otomatis. Strategi deployment seperti canary atau blue-green dipilih dengan sengaja per tingkat layanan.

**Tingkat 4: Mengelola.** Pengiriman diukur dan dikendalikan terhadap garis dasar. Organisasi melacak lead time perubahan, frekuensi deployment, tingkat kegagalan perubahan, dan mean time to recovery, bersama durasi pipeline p50 dan p95, tingkat flaky-test dan jalankan-ulang, dan usia feature flag. Ambang rollback ditetapkan dari data tingkat galat, latensi, dan saturasi teramati, gerbang ditegakkan atas bukti alih-alih kebiasaan, dan setiap metrik punya pemilik yang bertindak ketika ia menyimpang dari target.

**Tingkat 5: Mengorkestrasi.** Pengiriman terus membaik dan terintegrasi di seluruh organisasi. Pengiriman progresif dengan rollback otomatis berbasis metrik adalah norma, rilis dipisahkan dari deployment lewat flag yang diatur baik, dan bukti kepatuhan dihasilkan otomatis sebagai produk sampingan. Pipeline beradaptasi seiring properti berubah, dan metrik pengiriman memberi makan perencanaan bisnis dan risiko sehingga investasi mengalir ke perbaikan berdaya ungkit tertinggi.

## Gagasan untuk didiskusikan

- Di mana batas yang tepat antara pengiriman berkelanjutan dengan gerbang manusia dan deployment berkelanjutan penuh untuk sistem paling kritis Anda?
- Bagaimana Anda menjaga proses manajemen perubahan wajib tetap bermakna tanpa mengubahnya menjadi teater stempel karet?
- Metrik kesehatan objektif apa yang harus mengatur rollback otomatis, dan siapa yang memiliki ambangnya?
- Bagaimana tim platform harus menyeimbangkan templat pipeline terbakukan terhadap kebutuhan sah tim dengan persyaratan tak biasa?
- Apa kebijakan dan perkakas Anda untuk memensiunkan feature flag sebelum menjadi utang?
- Bagaimana Anda mengukur apakah pengiriman lebih cepat benar-benar memperbaiki hasil bisnis dan bukan sekadar mengirim lebih banyak?

## Poin-poin utama

- CI, CD, dan deployment berkelanjutan berbeda; pilih tingkat otomasi yang cocok dengan toleransi risiko dan kematangan Anda.
- Bangun artefak sekali dan promosikan artefak identik melalui setiap lingkungan.
- Rancang pipeline sebagai gerbang kualitas berurutan yang dioptimalkan untuk umpan balik cepat, dan perlakukan sebagai keputusan pengiriman otoritatif.
- Pilih strategi deployment dengan sengaja, dan adopsi pengiriman progresif dengan rollback otomatis untuk membatasi radius ledakan.
- Pisahkan rilis dari deployment dengan feature flag, dan kelola utang flag.
- Di lingkungan teregulasi, tangkap bukti kendali perubahan secara otomatis alih-alih lewat kertas manual.

## Referensi dan bacaan lanjutan

- Jez Humble dan David Farley, *Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation*.
- Nicole Forsgren, Jez Humble, dan Gene Kim, *Accelerate: The Science of Lean Software and DevOps*.
- Gene Kim, Jez Humble, Patrick Debois, dan John Willis, *The DevOps Handbook*.
- Gene Kim, Kevin Behr, dan George Spafford, *The Phoenix Project*.
- Betsy Beyer, Chris Jones, Jennifer Petoff, dan Niall Richard Murphy (ed.), *Site Reliability Engineering*.
- Pete Hodgson, "Feature Toggles (Feature Flags)" (esai).
- ITIL (Information Technology Infrastructure Library), panduan manajemen perubahan.
