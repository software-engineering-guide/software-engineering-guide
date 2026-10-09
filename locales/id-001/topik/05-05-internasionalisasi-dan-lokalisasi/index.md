# 5.5 Internasionalisasi dan lokalisasi

## Tinjauan dan motivasi

[Internasionalisasi](https://en.wikipedia.org/wiki/Internationalization_and_localization) (i18n) adalah pekerjaan rekayasa membangun perangkat lunak agar dapat disesuaikan dengan bahasa, wilayah, dan budaya apa pun tanpa mengubah kode. Lokalisasi (l10n) adalah pekerjaan yang menyusul: benar-benar menyesuaikan produk untuk lokal tertentu dengan menerjemahkan teks, memformat tanggal dan angka, menyesuaikan tata letak, dan memperhitungkan ekspektasi budaya. Keduanya berbeda. Internasionalisasi dilakukan sekali, dalam arsitektur. Lokalisasi dilakukan berkali-kali, dalam konten. Dapatkan arsitektur yang benar di muka dan setiap lokalisasi murah. Salah, dan masing-masing menjadi pemasangan belakangan yang menyakitkan dan rawan galat.

Bagi tim besar, i18n adalah keputusan arsitektural fondasional. Ia menyentuh setiap lapisan: penyimpanan data, penanganan string, tata letak, dan pipeline konten. Jika Anda tidak menetapkannya sejak dini dan menegakkannya lewat pustaka bersama dan aturan lint, tim mengodekan keras string Inggris, menggabungkan fragmen terjemahan, dan mengasumsikan aksara Latin. Utang itu harus diurai sebelum produk dapat memasuki pasar baru mana pun. Kerangka i18n bersama dan alur kerja lokalisasi memungkinkan puluhan tim merilis produk dalam banyak bahasa tanpa masing-masing menciptakan ulang perpipaan.

Relevansi enterprise dan pemerintah langsung. Enterprise multinasional harus melayani pelanggan dan karyawan lintas negara, bahasa, dan rezim regulasi. Pemerintah harus melayani populasi yang beragam bahasa. Banyak negara resmi multibahasa, dan banyak yang secara hukum wajib menyediakan layanan dalam beberapa bahasa, termasuk aksara [kanan-ke-kiri](https://en.wikipedia.org/wiki/Bidirectional_text) dan bahasa adat atau minoritas. Untuk layanan publik, akses bahasa adalah isu kesetaraan dan hukum: warga yang tak dapat membaca satu-satunya bahasa yang tersedia pada dasarnya ditolak layanan.

## Prinsip utama

- Internasionalisasikan arsitektur sekali; lokalkan konten berkali-kali.
- Jangan pernah mengodekan keras teks yang menghadap pengguna; eksternalisasikan semua string ke sumber daya terkelola.
- Gunakan [Unicode](https://en.wikipedia.org/wiki/Unicode) (UTF-8) di mana-mana; asumsikan teks dapat dalam aksara apa pun.
- Jangan pernah menggabungkan fragmen terjemahan; tata bahasa dan urutan kata berbeda menurut bahasa.
- Rencanakan perluasan teks, aksara kanan-ke-kiri, dan aturan jamak serta gender yang kompleks.
- Format tanggal, angka, mata uang, dan nama menurut lokal, bukan kode.
- Pisahkan konten yang dapat diterjemahkan dari kode agar penerjemah tidak pernah menyentuh sumber.
- Lokalisasi bersifat budaya, bukan hanya linguistik: warna, citra, dan contoh penting.

## Rekomendasi

### Bangun arsitektur internasionalisasi yang kokoh

Simpan dan proses semua teks sebagai Unicode (UTF-8) dari ujung ke ujung (basis data, API, dan UI) agar aksara apa pun dapat direpresentasikan. Eksternalisasikan setiap string yang menghadap pengguna ke berkas sumber daya atau katalog pesan berkunci pengidentifikasi, tidak pernah tertanam dalam kode atau markup. Representasikan lokal sebagai bahasa plus wilayah (dan aksara bila perlu) agar Anda dapat membedakan, misalnya, varian satu bahasa lintas negara. Jaga logika pemformatan dalam pustaka internasionalisasi yang teruji baik alih-alih menggulirkan pemformatan tanggal, angka, dan mata uang sendiri. Simpan data dalam bentuk netral dan tak ambigu (stempel waktu UTC, kode negara dan mata uang ISO, satuan dasar) dan format hanya di lapisan presentasi.

### Tangani kompleksitas bahasa dengan benar

Jangan mengasumsikan panjang teks; sediakan ruang lega karena terjemahan lazim jauh lebih panjang daripada bahasa Inggris, dan rancang tata letak yang mengalir ulang alih-alih memotong atau bertumpuk. Dukung aksara dua arah (kanan-ke-kiri) dengan memakai properti tata letak logis alih-alih fisik dan mencerminkan antarmuka bila sesuai. Gunakan aturan jamak lokal lewat pustaka i18n Anda (bahasa punya satu hingga enam bentuk jamak) alih-alih logika tunggal/jamak naif. Tangani gender dan kesesuaian gramatikal di tempat bahasa memerlukannya. Jangan pernah membangun kalimat dengan penggabungan; gunakan templat pesan lengkap berparameter agar penerjemah mengendalikan urutan kata.

### Dirikan alur kerja lokalisasi dan manajemen terjemahan

Perlakukan lokalisasi sebagai pipeline berkelanjutan, bukan batch pra-peluncuran. Ekstrak string secara otomatis, dorong ke [sistem manajemen terjemahan](https://en.wikipedia.org/wiki/Translation_management_system), dan tarik terjemahan yang selesai kembali, idealnya terintegrasi dengan CI agar string baru ditandai dan versi terlokalkan tetap sinkron. Beri penerjemah konteks: tangkapan layar, deskripsi, batas karakter, dan glosarium serta panduan gaya per bahasa untuk menjaga terminologi dan nada konsisten. Gunakan [memori terjemahan](https://en.wikipedia.org/wiki/Translation_memory) untuk memakai ulang pekerjaan sebelumnya dan memotong biaya. Putuskan dengan sengaja di mana [terjemahan mesin](https://en.wikipedia.org/wiki/Machine_translation) dapat diterima (konten berisiko rendah dan bervolume tinggi) dan di mana terjemahan serta tinjauan manusia diwajibkan (hukum, medis, keselamatan, kritis merek). [Pseudo-lokalisasi](https://en.wikipedia.org/wiki/Pseudolocalization) sejak dini, mengganti string dengan penampung berakses yang diperpanjang, untuk menangkap string yang dikodekan keras, pemotongan, dan bug pengkodean sebelum terjemahan nyata dimulai.

### Lokalkan format, budaya, dan konten, bukan hanya kata

Format tanggal, waktu, angka, mata uang, alamat, nomor telepon, dan nama per lokal, menghormati konvensi setempat (urutan tanggal, pemisah desimal dan pengelompokan, penempatan mata uang, urutan nama). Sesuaikan citra, ikon, warna, contoh, dan metafora dengan makna budaya setempat, karena simbol dan warna membawa konotasi berbeda lintas budaya. Perhitungkan perbedaan konten hukum dan regulasi setempat. Bedakan konsistensi global (merek, fungsionalitas inti) dari adaptasi regional (konten, contoh, kepatuhan) dan putuskan secara eksplisit elemen mana yang tetap dan mana yang lentur.

### Atur i18n sebagai infrastruktur bersama

Sediakan pustaka i18n bersama, aturan lint eksternalisasi string, dan mekanisme resolusi lokal standar agar tim tidak dapat tak sengaja mengodekan keras teks. Tetapkan kepemilikan pipeline lokalisasi dan glosarium. Uji dalam beberapa lokal di CI, termasuk lokal kanan-ke-kiri dan pseudo-lokal teks panjang, agar regresi tertangkap otomatis.

## Trade-off: kelebihan dan kekurangan

| Keputusan | Kelebihan | Kekurangan |
|---|---|---|
| Internasionalisasi sejak hari pertama | Masuk pasar kelak murah, tanpa pemasangan belakangan | Biaya di muka bahkan sebelum lokal kedua dibutuhkan |
| Pasang i18n belakangan | Menunda biaya jika kebutuhan global tidak pasti | Sangat mahal dan berisiko mengurai asumsi yang dikodekan keras |
| Terjemahan manusia | Kualitas tinggi, akurat secara budaya | Lebih lambat dan lebih mahal |
| Terjemahan mesin | Cepat, murah, berskala ke volume sangat besar | Risiko kualitas dan akurasi; tidak cocok untuk konten taruhan tinggi |
| Pipeline lokalisasi berkelanjutan | Lokal tetap sinkron, tanpa kerumitan peluncuran | Investasi perkakas dan proses |
| Adaptasi budaya mendalam per wilayah | Kecocokan dan kepercayaan lokal lebih baik | Lebih banyak varian konten untuk dibangun dan dipelihara |

Trade-off penentu adalah kapan berinvestasi pada internasionalisasi. Memasang i18n ke produk yang penuh kode terkodekan keras, tergabung, dan berasumsi Latin termasuk bentuk utang teknis yang lebih mahal untuk dilunasi. Untuk organisasi mana pun dengan ambisi internasional atau multibahasa yang masuk akal, yang mencakup pada dasarnya semua enterprise besar dan pemerintah multibahasa, menginternasionalisasikan arsitektur sejak dini jauh lebih murah daripada memasang belakangan, meski imbalannya tertunda.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apakah kita menegakkan eksternalisasi string dengan aturan lint, dan apakah pseudo-lokalisasi berjalan di CI sebelum terjemahan nyata?** Utang yang membuat internasionalisasi mahal (string Inggris dikodekan keras, fragmen kalimat tergabung, asumsi aksara Latin) menumpuk diam-diam kecuali perkakas menghentikannya saat komit. Aturan lint yang menandai teks pengguna terkodekan keras, plus pseudo-lokal berakses teks panjang yang dijalankan di CI, menangkap pemotongan, tumpang tindih, dan bug pengkodean selagi murah diperbaiki. Inilah yang memungkinkan puluhan tim merilis satu produk dalam banyak bahasa tanpa masing-masing menciptakan ulang perpipaan atau mengurai asumsi di bawah tenggat kelak. Bawa pencarian string terkodekan keras dan tanyakan apakah ada tim yang bisa tak sengaja mengirimnya hari ini. Jika tak ada dalam pipeline yang akan menangkapnya, itu celah yang ditutup lebih dulu.

2. **Di mana kita menyimpan data kanonik, dan apakah pemformatan terbatas pada lapisan presentasi?** Menyimpan stempel waktu sebagai UTC, negara dan mata uang sebagai kode ISO, dan jumlah dalam satuan dasar berarti lokal apa pun dapat memformatnya dengan benar di tepi, sementara logika pemformatan yang tertanam di lapisan data menghasilkan bug yang menyakitkan untuk diurai. Sepakati bahwa tanggal, angka, mata uang, alamat, dan nama diformat hanya pada presentasi, lewat pustaka teruji alih-alih kode buatan tangan. Ini penting bagi enterprise multinasional dan pemerintah multibahasa di mana warga harus melihat urutan tanggal, pemisah desimal, dan urutan nama yang benar dalam konvensi mereka sendiri. Bawa contoh nilai yang sistem Anda simpan sudah terformat dan telusuri apa yang rusak ketika lokal baru membutuhkannya berbeda. Jika data dan presentasi kusut, putuskan bagaimana Anda mengurainya sebelum menambah lokal.

3. **Di mana persisnya terjemahan mesin dapat diterima, dan bagaimana pipeline lokalisasi kita dijaga berkelanjutan alih-alih batch?** Terjemahan mesin cepat dan murah untuk konten berisiko rendah dan bervolume tinggi tetapi tidak cocok untuk teks hukum, medis, keselamatan, atau kritis merek di mana salah terjemah menyebabkan bahaya nyata, sehingga batasnya perlu menjadi kebijakan eksplisit, bukan tebakan per tim. Sama halnya, memperlakukan lokalisasi sebagai batch pra-peluncuran menjamin kerumitan terjemahan, sedangkan mengekstrak string secara otomatis dan menyinkronkan lewat sistem manajemen terjemahan menjaga setiap lokal tetap mutakhir. Putuskan siapa yang memiliki pipeline, glosarium, dan gerbang tinjauan manusia untuk string taruhan tinggi. Bawa rilis terbaru dan tanyakan berapa lama string barunya muncul di setiap bahasa. Jika lokal menyimpang tak sinkron antarrilis, pipeline Anda batch yang menyamar.

4. **Apakah kita menguji lokal kanan-ke-kiri dan pseudo-lokal teks panjang secara otomatis, atau diam-diam mengasumsikan aksara Latin dan tata letak sepanjang bahasa Inggris?** Dukungan dua arah (kanan-ke-kiri) dan perluasan teks adalah asumsi yang paling terlihat patah di pasar baru: antarmuka tercermin yang tak pernah dicerminkan, dan tombol yang terpotong begitu bahasa Jerman atau Finlandia berjalan empat puluh persen lebih panjang daripada Inggris. Tarikan yang bersaing adalah kecepatan, karena membangun di atas properti tata letak logis alih-alih fisik dan menyambungkan pseudo-lokal berakses ke integrasi berkelanjutan (CI) memakan upaya sebelum pelanggan nyata membutuhkannya. Bawa tangkapan layar layar tersibuk Anda yang dirender dalam lokal kanan-ke-kiri dan dalam pseudo-lokal yang diperpanjang, dan hitung tumpang tindih, label terpotong, dan panah yang macet. Untuk enterprise multinasional atau pemerintah yang secara hukum wajib melayani bahasa kanan-ke-kiri atau minoritas, tata letak yang tak dapat mencerminkan bukan cacat kosmetik, melainkan pasar atau kewajiban undang-undang yang tak dapat Anda penuhi tanpa pembangunan ulang.

5. **Bagian produk mana yang tetap secara global dan mana yang lentur menurut wilayah, dan siapa yang berwenang memutuskan?** Lokalisasi bersifat budaya, bukan sekadar linguistik, sehingga warna, citra, contoh, sapaan hormat, dan bahkan fitur mana yang ditawarkan dapat berbeda menurut pasar, namun setiap varian regional yang Anda izinkan adalah artefak lain untuk dibangun, diterjemahkan, ditinjau, dan dipelihara selamanya. Ketegangannya antara kecocokan lokal, yang membangun kepercayaan dan konversi, dan konsistensi, yang menjaga merek koheren dan beban pemeliharaan terbatas. Bawa daftar konkret apa yang akan diubah lokal baru yang diusulkan di luar string terjemahan, dan hargai pemeliharaan berkelanjutan setiap varian, bukan hanya pembangunan pertamanya. Dalam enterprise besar keputusan ini butuh pemilik bernama agar tim regional tidak dapat mem-fork produk secara ad hoc, dan di pemerintah ia harus menghormati aturan konten hukum dan aksesibilitas yang bervariasi menurut yurisdiksi dan tidak opsional.

6. **Lokal mana yang benar-benar kita komit, bagaimana kita menjaga terminologi konsisten di antaranya, dan bukti apa yang menggerakkan daftar itu?** Menambah bahasa mudah dijanjikan dan mahal dipertahankan, karena masing-masing membutuhkan glosarium, panduan gaya, tinjauan manusia untuk string taruhan tinggi, dan penanganan jamak serta gender yang benar yang gagal ditangani logika tunggal-atau-jamak naif di sebagian besar bahasa. Pertimbangan yang bersaing adalah jangkauan melawan biaya: pasar atau populasi yang dilayani buruk bisa lebih buruk daripada yang tidak dilayani sama sekali. Bawa populasi atau pendapatan di balik setiap lokal kandidat, cakupan aturan jamak dan pemformatan yang disediakan pustaka Anda untuknya, dan siapa yang memiliki glosariumnya. Untuk enterprise multinasional pendorongnya pasar yang dapat dijangkau dan biaya dukungan per bahasa, sementara untuk pemerintah itu kewajiban akses bahasa hukum dan kesetaraan, dikuantifikasi oleh jumlah penduduk yang hanya dapat bertransaksi dalam bahasa itu.

## Lensa sektor

**Startup.** Buat pilihan arsitektural murah pada hari pertama dan berhenti di sana: UTF-8 dari ujung ke ujung, setiap string yang menghadap pengguna dalam katalog pesan, dan tanggal, angka, serta mata uang diformat lewat pustaka sadar-lokal. Ini hampir tak berbiaya selagi Anda merilis dalam satu bahasa dan menghemat penulisan ulang ketika pelanggan besar pertama Anda menginginkan bahasa kedua. Jangan dirikan pipeline terjemahan atau dukung lokal yang belum dibayar siapa pun; jaga pintu tetap terbuka, bukan seluruh rumah dilengkapi perabot.

**Bisnis kecil.** Tanpa spesialis internasionalisasi dan dengan anggaran ketat, bersandarlah pada fitur i18n yang sudah ada di kerangka kerja Anda dan layanan manajemen terjemahan ter-hosting alih-alih membangun pipeline sendiri. Pakai terjemahan mesin untuk konten berisiko rendah dan bervolume tinggi dan bayar terjemahan manusia hanya di tempat kesalahan akan membuat Anda kehilangan pelanggan atau melanggar aturan, seperti teks hukum, keselamatan, atau penagihan. Berkomitmen pada lokal hanya ketika pasar tertentu jelas membenarkan biaya terjemahan dan tinjauan berkelanjutan.

**Enterprise.** Masalahnya tata kelola lintas banyak tim: pustaka i18n bersama, aturan lint yang menolak string terkodekan keras, pipeline lokalisasi berkelanjutan dengan memori terjemahan dan glosarium per bahasa, dan CI multilokal yang mencakup pseudo-lokal kanan-ke-kiri dan teks panjang. Jalankan lokalisasi sebagai infrastruktur bersama dengan pemilik jelas agar kelompok berhenti menciptakan ulang perpipaan atau menyimpang tak sinkron. Ukur cakupan bahasa, kualitas lokalisasi, dan waktu meluncurkan lokal baru, dan kelola portofolio lokal terhadap angka itu alih-alih meluncurkan pasar secara ad hoc.

**Pemerintah.** Akses bahasa sering kewajiban hukum, mencakup bahasa resmi, aksara kanan-ke-kiri, dan bahasa adat atau minoritas, sehingga transparansi dan kesetaraan membentuk setiap pilihan. Bangun kerangka i18n dan alur kerja terjemahan bersama lintas lembaga, wajibkan tinjauan manusia untuk terminologi hukum dan keselamatan, dan terbitkan glosarium agar istilah tetap konsisten antarlayanan. Pengadaan harus menuntut dukungan lokal, kanan-ke-kiri, dan aksesibilitas dalam kontrak, dan populasi yang dilayani dalam setiap bahasa adalah metrik yang membenarkan pengeluaran kepada publik.

## Contoh

**Startup.** Sebuah startup kecil yang hanya merilis dalam bahasa Inggris tetap membuat beberapa pilihan arsitektural murah pada hari pertama: UTF-8 di mana-mana, setiap string yang menghadap pengguna ditarik ke katalog pesan alih-alih dikodekan keras, dan tanggal serta mata uang diformat lewat pustaka sadar-lokal. Itu hampir tak berbiaya selagi mereka punya satu bahasa. Setahun kemudian, ketika calon pelanggan terbesar mereka meminta versi Prancis dan Jerman, menambah lokal itu sebagian besar latihan terjemahan yang diserahkan kepada kontraktor, bukan penulisan ulang, dan mereka menutup kesepakatan dalam hitungan minggu alih-alih menundanya selama satu kuartal pekerjaan rekayasa.

**Enterprise.** Sebuah perusahaan e-commerce global menginternasionalisasikan platformnya sejak dini: UTF-8 di seluruhnya, string terekstenalisasi, pustaka pemformatan sadar-lokal, dan pipeline lokalisasi berkelanjutan dengan memori terjemahan dan glosarium per bahasa. Memasuki pasar baru sebagian besar menjadi latihan konten (terjemahkan, tinjau, sesuaikan citra) alih-alih proyek rekayasa, memungkinkan perusahaan meluncur di lokal baru dalam hitungan minggu. Dukungan kanan-ke-kiri yang dibangun di atas properti tata letak logis berarti pasar Arab dan Ibrani membutuhkan sedikit kerja UI baru.

**Pemerintah.** Sebuah pemerintah nasional yang secara hukum wajib menyampaikan layanan dalam beberapa bahasa resmi, termasuk aksara kanan-ke-kiri dan bahasa minoritas, membangun kerangka i18n dan alur kerja terjemahan bersama yang dipakai lintas lembaga. Pseudo-lokalisasi di CI menangkap string terkodekan keras dan pemotongan sebelum peluncuran; glosarium bersama menjaga terminologi hukum konsisten lintas layanan dan bahasa. Warga dapat menyelesaikan transaksi pajak, kesehatan, dan tunjangan dalam bahasa mereka sendiri dengan pemformatan tanggal, angka, dan nama yang benar, memenuhi hukum akses bahasa dan memperbaiki kesetaraan bagi penutur bahasa non-mayoritas.

## Kasus bisnis: motivasi, ROI, dan TCO

ROI internasionalisasi adalah akses pasar dan kecepatan. Produk yang diinternasionalisasikan baik dapat memasuki negara dan pasar bahasa baru dengan cepat dan murah, mengubah setiap lokal baru menjadi pendapatan tambahan atau jangkauan warga alih-alih proyek besar. Kualitas lokalisasi menggerakkan konversi, kepercayaan, dan biaya dukungan di setiap pasar: pengguna bertransaksi lebih banyak dan menghubungi dukungan lebih sedikit ketika produk berbicara dalam bahasa mereka dengan benar dan menghormati konvensi mereka.

Pada TCO, biaya adopsi adalah rekayasa di muka untuk menginternasionalisasikan, plus biaya terjemahan dan pipeline berkelanjutan. Biaya tidak mengadopsi adalah pemasangan belakangan yang mahal: mengurai string terkodekan keras, penggabungan, bug pengkodean, dan asumsi tata letak di seluruh basis kode, sering di bawah tenggat yang digerakkan pasar atau persyaratan hukum. Lokalisasi buruk juga membawa biaya tersembunyi: penjualan hilang di pasar yang dilayani buruk, beban dukungan dari format yang membingungkan, dan kerusakan hukum atau reputasi dari konten taruhan tinggi yang salah diterjemahkan. Lokalisasi berkelanjutan menghindari kerumitan terjemahan pra-peluncuran yang mahal.

Untuk mengajukan kasus kepada pimpinan, bingkai internasionalisasi sebagai opsi atas pasar masa depan. Ia investasi di muka sederhana yang secara dramatis menurunkan biaya dan waktu setiap masuk pasar mendatang. Untuk pemerintah, pendorongnya kewajiban akses bahasa hukum dan kesetaraan, dikuantifikasi oleh populasi yang dilayani dalam setiap bahasa.

## Anti-pola dan jebakan

- **String terkodekan keras**: teks pengguna yang tertanam dalam kode, memaksa perubahan kode per lokal.
- **Penggabungan string**: membangun kalimat dari fragmen, yang merusak tata bahasa dan urutan kata.
- **Asumsi non-Unicode**: bug pengkodean, [mojibake](https://en.wikipedia.org/wiki/Mojibake) (teks kacau akibat pengkodean karakter yang tak cocok), dan ketidakmampuan merepresentasikan aksara.
- **Mengasumsikan panjang teks Inggris**: tata letak yang terpotong atau bertumpuk ketika diterjemahkan.
- **Mengabaikan kanan-ke-kiri**: memakai tata letak kiri/kanan fisik yang tak dapat mencerminkan.
- **Pluralisasi naif**: logika tunggal/jamak yang salah di sebagian besar bahasa.
- **Pemformatan buta-lokal**: format tanggal, angka, dan mata uang yang dikodekan keras.
- **Menerjemahkan tanpa konteks**: penerjemah menebak makna, menghasilkan galat.
- **Lokalisasi batch menit terakhir**: kerumitan pra-peluncuran alih-alih pipeline berkelanjutan.
- **Ketulian budaya**: citra, warna, atau contoh yang menyinggung atau membingungkan secara lokal.

## Model kematangan

**Tingkat 1: Memulai.** Satu bahasa, string terkodekan keras, asumsi non-Unicode, dan teks dibangun dengan penggabungan. Internasionalisasi reaktif: lokal baru apa pun berarti mengubah kode, dan bug pengkodean serta tata letak ditemukan secara tak sengaja di produksi.

**Tingkat 2: Mengembangkan.** Sebagian string terekstenalisasi dan Unicode dipakai di beberapa tempat, tetapi praktik tidak konsisten antartim. Lokalisasi adalah upaya manual, batch, pra-peluncuran, dan pemformatan, penanganan jamak, dan dukungan kanan-ke-kiri ditangani berbeda (atau tidak sama sekali) dari satu tim ke tim lain.

**Tingkat 3: Membakukan.** Arsitektur i18n bersama dan pustaka pemformatan sadar-lokal adalah standar terdokumentasi yang ditegakkan di seluruh organisasi. Eksternalisasi string diperiksa aturan lint, sistem manajemen terjemahan dan pipeline berkelanjutan ada dengan glosarium dan memori terjemahan, dan pseudo-lokalisasi plus pengujian multilokal (termasuk lokal kanan-ke-kiri dan teks panjang) berjalan di CI.

**Tingkat 4: Mengelola.** Program lokalisasi diukur dan dikendalikan terhadap garis dasar. Tim melacak cakupan bahasa, kualitas lokalisasi dan tingkat cacat, latensi sinkronisasi string dari komit ke rilis terjemahan, cacat pemotongan dan render kanan-ke-kiri yang tertangkap per rilis, biaya terjemahan per lokal, dan waktu meluncurkan lokal baru, dan metrik ini menggerbangi rilis dan menggerakkan di mana berinvestasi tinjauan manusia versus terjemahan mesin.

**Tingkat 5: Mengorkestrasi.** Internasionalisasi dan lokalisasi terus diperbaiki dan terintegrasi di seluruh organisasi. Lokalisasi berkelanjutan, terjemahan mesin dan manusia dipilih dengan sengaja per kelas konten, dan adaptasi budaya sistematis. Organisasi menambah, memensiunkan, dan menentukan ulang cakupan lokal sebagai respons terhadap bukti pasar dan kesetaraan, dan lokal baru meluncur cepat dengan kualitas tinggi tanpa pemasangan belakangan.

## Gagasan untuk didiskusikan

- Seawal apa produk harus diinternasionalisasikan jika permintaan internasional tidak pasti?
- Di mana terjemahan mesin dapat diterima, dan di mana manusia harus meninjau?
- Bagaimana Anda menjaga terminologi konsisten lintas banyak bahasa dan tim?
- Seberapa banyak adaptasi budaya regional layak pemeliharaan varian tambahan?
- Bagaimana dukungan kanan-ke-kiri dan bahasa minoritas harus diprioritaskan dan diuji?
- Bagaimana Anda memberi penerjemah konteks cukup tanpa memperlambat pipeline?

## Poin-poin utama

- Internasionalisasikan arsitektur sekali; lokalkan konten berkali-kali.
- Gunakan Unicode di mana-mana, eksternalisasikan semua string, dan jangan pernah menggabungkan terjemahan.
- Rencanakan perluasan teks, aksara kanan-ke-kiri, dan aturan jamak serta pemformatan khusus lokal.
- Jalankan pipeline lokalisasi berkelanjutan dengan memori terjemahan, glosarium, dan konteks.
- Pseudo-lokalisasi sejak dini di CI untuk menangkap bug i18n sebelum terjemahan nyata.
- Lokalisasi bersifat budaya, bukan hanya linguistik.
- Internasionalisasi dini jauh lebih murah daripada memasang belakangan; bagi pemerintah ia persyaratan kesetaraan hukum.

## Referensi dan bacaan lanjutan

- The Unicode Consortium, *The Unicode Standard* dan Common Locale Data Repository (CLDR)
- W3C Internationalisation (i18n) Activity, teknik dan praktik terbaik
- Richard Ishida, artikel dan tutorial internasionalisasi W3C
- Bert Esselink, *A Practical Guide to Localisation*
- John Yunker, *Beyond Borders: Web Globalisation Strategies*
- Unicode Technical Standard #35 (markup data lokal) dan dokumentasi pustaka ICU
- IETF BCP 47 tag bahasa
- Panduan layanan multibahasa dan akses bahasa pemerintah
- Artikel Nielsen Norman Group dan W3C tentang RTL, perluasan teks, dan UX lokalisasi
