# 2.12 Model dan metode perangkat lunak

## Tinjauan dan motivasi

Model perangkat lunak adalah penyederhanaan yang disengaja atas sebuah sistem, dibangun untuk menjawab pertanyaan tertentu. Metode adalah cara disiplin menghasilkan perangkat lunak, termasuk model yang dipakainya sepanjang jalan. Bersama-sama keduanya membentuk area pengetahuan Software Engineering Body of Knowledge (SWEBOK), karena merupakan perkakas mental yang Anda pakai untuk bernalar tentang sistem sebelum, selama, dan setelah Anda membangunnya. Diagram kelas UML ([Unified Modelling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language)), [diagram entitas-relasi](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) (ERD), [mesin status](https://en.wikipedia.org/wiki/Finite-state_machine), [spesifikasi formal](https://en.wikipedia.org/wiki/Formal_specification), dan prototipe sekali pakai semuanya adalah model. [Waterfall](https://en.wikipedia.org/wiki/Waterfall_model), [pembuatan prototipe](https://en.wikipedia.org/wiki/Software_prototyping), pengembangan formal, dan [agile](https://en.wikipedia.org/wiki/Agile_software_development) semuanya adalah metode.

Mengapa repot-repot dengan model? Karena memori kerja manusia kecil dan sistem perangkat lunak besar. Tak seorang pun dapat memegang sistem seratus ribu baris di kepalanya, jadi kita menggambar dan menulis abstraksi yang menunjukkan satu segi sekaligus: data, alur kendali, status, interaksi. Model tidak pernah dimaksudkan untuk setia pada kode; ia dimaksudkan untuk pas bagi sebuah keputusan. Model yang baik menunjukkan persis yang Anda butuhkan untuk memutuskan sesuatu, dan menyembunyikan segala yang lain.

Pada tim besar, taruhan sebenarnya adalah koordinasi dan komunikasi. Ketika ratusan insinyur, arsitek, analis, dan auditor mengerjakan satu sistem, model bersama adalah landasan umum tempat mereka menegosiasikan desain, persyaratan, dan risiko. Jadi anggap pemodelan sebagai perkakas dengan tugas yang harus dikerjakan. Ia membuahkan hasil ketika model lebih murah daripada kesalahan yang dicegahnya. Ia menjadi pemborosan ketika Anda menggambarnya demi dirinya sendiri, menyimpannya lama setelah basi, atau mengelaborasinya melampaui keputusan yang hendak dilayaninya. Pemodelan terhubung erat dengan persyaratan perangkat lunak (bab 2.8), prinsip desain perangkat lunak (bab 2.2), arsitektur dan notasinya seperti C4 dan arc42 (bab 3.1), dan cara kerja agile (bab 10.7).

## Prinsip utama

- Setiap model punya tujuan; jika Anda tidak dapat menamai keputusan yang diinformasikan sebuah model, jangan gambar.
- Abstraksi adalah tindakan inti pemodelan: sertakan apa yang penting untuk tujuan, hilangkan sisanya.
- Konsistensi penting dalam dan lintas model; model yang bertentangan lebih buruk daripada tidak ada.
- Model adalah artefak komunikasi lebih dulu; audiensnya menentukan notasi dan detailnya.
- Pilih model teringan yang menjawab pertanyaan; elaborasi punya biaya penanggungan.
- Model hanya sebaik analisisnya; model yang tidak diperiksa adalah asumsi yang belum teruji.
- Pilih metode yang sesuai dengan ketidakpastian, risiko, dan konsekuensi kegagalan masalah.

## Rekomendasi

### Modelkan dengan abstraksi, tujuan, dan konsistensi

Mulailah setiap model dengan menamai tujuan dan audiensnya. Lalu abstraksikan tanpa ampun menuju tujuan itu: diagram urutan yang dimaksudkan untuk menyelesaikan race condition harus menunjukkan waktu dan pesan, bukan setiap bidang. Jaga model Anda konsisten satu sama lain, agar entitas dalam ERD, kelas dalam diagram kelas, dan kata benda dalam persyaratan semuanya sepakat, dan konsisten dengan kenyataan, artinya Anda memperbarui atau menghapus model ketika sistem berpindah. Model basi yang dipercaya orang adalah bahaya. Model basi yang diabaikan semua orang adalah pemborosan yang masih memakan perhatian.

### Pilih model struktural atau perilaku agar sesuai dengan pertanyaan

Gunakan model struktural untuk menunjukkan apa penyusun sistem dan bagaimana bagian-bagiannya berhubungan: diagram kelas, diagram komponen, dan diagram entitas-relasi untuk struktur data. Gunakan model perilaku untuk menunjukkan apa yang dilakukan sistem dari waktu ke waktu: mesin status untuk objek dengan siklus hidup bermakna, diagram urutan untuk interaksi antarkomponen, dan diagram aktivitas untuk alur kerja dan proses bisnis. Pilih satu notasi yang mengungkap keputusan di depan Anda. Sebagian besar sistem hanya membutuhkan segelintir jenis diagram, digambar secara selektif, bukan seluruh katalog UML yang diterapkan pada segalanya.

### Analisis model, jangan hanya menggambarnya

Model pantas dipertahankan lewat analisis, bukan sekadar gambar. Periksa mesin status untuk status yang tak terjangkau, transisi yang hilang, dan deadlock. Periksa ERD untuk masalah normalisasi dan relasi yatim. Telusuri diagram urutan terhadap persyaratan untuk menemukan jalur galat yang hilang. Tinjau model Anda bersama pakar domain yang dapat melihat apa yang keliru. Dan di tempat biaya kegagalan tinggi, raih analisis berbantuan perkakas (model checker, pemeriksa konsistensi, simulasi) alih-alih menebak dengan mata.

### Terapkan metode heuristik sebagai bawaan

Sebagian besar perangkat lunak dibangun dengan metode heuristik: pendekatan berbasis pengalaman dan iteratif yang memakai model secara informal dan menilai hasil terhadap ekspektasi alih-alih bukti. Untuk sebagian besar sistem bisnis dan pemerintah, itu persis tepat: persyaratan berkembang, dan cacat biasanya dapat dipulihkan. Metode heuristik berpasangan secara alami dengan agile (bab 10.7): modelkan secukupnya untuk menyelaraskan tim, lalu bangun dan belajar.

### Sisakan metode formal untuk inti berkonsekuensi tinggi

[Metode formal](https://en.wikipedia.org/wiki/Formal_methods) mengekspresikan spesifikasi dalam matematika dan memakai verifikasi, entah bukti atau [model checking](https://en.wikipedia.org/wiki/Model_checking) menyeluruh, untuk menetapkan sifat. Mereka memakan keterampilan dan waktu nyata, dan membuahkan hasil persis di tempat kegagalan bersifat katastrofik atau tak terbalikkan: kendali kritis keselamatan, protokol kriptografi, inti penyelesaian keuangan, dan sejenisnya. Terapkan pada inti kritis yang kecil, bukan seluruh sistem. Dan catat bahwa spesifikasi formal saja, bahkan tanpa bukti penuh, sering menambah nilai hanya dengan memaksa Anda menjadi presisi.

### Gunakan pembuatan prototipe untuk menghapus ketidakpastian

Ketika persyaratan atau kelayakan tidak jelas, bangun prototipe untuk belajar, lalu putuskan, dengan sengaja, apakah akan mengembangkannya atau membuangnya. Prototipe sekali pakai menjelajahi pertanyaan dengan murah lalu dihapus. Prototipe evolusioner menjadi produk dan harus dibangun menurut standar produksi. Kegagalan klasiknya adalah membiarkan prototipe sekali pakai terselip ke produksi secara tidak sengaja. Jadi namai jenis prototipe sebelum Anda membangunnya.

### Cocokkan metode dengan risiko, bukan mode

Pilih metode menurut ketidakpastian masalah dan konsekuensi kegagalan. Ketidakpastian tinggi mendukung pembuatan prototipe dan iterasi agile. Konsekuensi tinggi mendukung analisis formal dan verifikasi ketat. Sistem dengan keduanya membutuhkan inti formal kritis di dalam amplop agile yang selain itu. Apa pun yang Anda lakukan, jangan adopsi metode hanya karena prestisius atau karena vendor menjualnya.

## Trade-off: kelebihan dan kekurangan

| Model atau metode | Diterapkan dengan baik | Mode kegagalan |
|---|---|---|
| Model struktural (UML, ERD) | Gambaran bersama tentang bagian dan data | Diagram menjamur; menyimpang dari kode |
| Model perilaku (status, urutan, aktivitas) | Mengungkap waktu, status, dan kasus tepi | Diagram terlalu terperinci yang tak dibaca siapa pun |
| Metode heuristik | Cepat, fleksibel, cocok untuk sebagian besar sistem | Tidak disiplin; asumsi tersembunyi |
| Metode formal | Sifat yang dapat dibuktikan untuk inti kritis | Biaya tinggi; disalahterapkan pada seluruh sistem |
| Pembuatan prototipe | Pembelajaran murah; menghapus risiko lebih awal | Kode sekali pakai dipromosikan ke produksi |
| Metode agile | Beradaptasi dengan persyaratan yang berubah | Melewatkan pemodelan yang dibutuhkan masalah sulit |

Ketegangan yang berulang adalah antara ketelitian dan kecepatan. Pemodelan yang terlalu sedikit merilis asumsi tersembunyi ke produksi. Pemodelan yang terlalu banyak membakar upaya pada diagram yang tidak pernah menginformasikan keputusan dan membusuk begitu kode berubah. Tidak ada dosis tetap yang memperbaiki ini, hanya aturan proporsi: berinvestasilah pada model atau metode sebanding dengan ketidakpastian yang diselesaikannya dan biaya salah mengambil keputusan. Mesin pembayaran dan situs mikro pemasaran layak mendapat perlakuan berbeda.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apakah kita menganalisis model kita, atau hanya menggambarnya lalu berlalu?** Model pantas dipertahankan lewat analisis, bukan karena keberadaannya: mesin status yang tidak pernah Anda periksa untuk status tak terjangkau atau transisi yang hilang adalah asumsi yang belum teruji yang berdandan sebagai diagram. Pada tim besar di sinilah cacat nyata bersembunyi, karena gambar yang tampak masuk akal dipercaya persis ketika tak seorang pun menelusurinya terhadap persyaratan untuk menemukan jalur galat yang hilang atau relasi yatim. Bawa model perilaku terpenting Anda ke rapat dan coba patahkan: transisi mana yang tak terdefinisi, status mana yang tak punya jalan keluar, urutan mana yang tak punya timeout? Di tempat biaya kegagalan tinggi, jawabannya harus mendorong Anda menuju analisis berbantuan perkakas (model checker, pemeriksa konsistensi, simulasi) alih-alih menebak dengan mata, karena seluruh alasan memodelkan inti kritis adalah menemukan cacat di papan tulis alih-alih di produksi.

2. **Ketika dua model kita bertentangan, mana yang menang, dan siapa yang memperhatikan kontradiksinya?** Konsistensi penting dalam dan lintas model, dan model yang bertentangan lebih buruk daripada tidak ada, karena orang bertindak berdasarkan keduanya. Pada sistem besar entitas dalam model data, kelas dalam desain, dan kata benda dalam persyaratan menyimpang diam-diam saat tim berbeda memperbarui artefak berbeda, dan tanda pertama sering bug produksi di mana dua komponen tidak sepakat tentang apa sesuatu itu. Bawa contoh: pilih konsep inti dan periksa apakah ERD, kode, dan persyaratan benar-benar sepakat tentang bentuk dan siklus hidupnya. Jika tidak, putuskan artefak mana yang berwenang dan siapa yang bertanggung jawab menjaga yang lain sejalan, dan bersedialah menghapus model alih-alih membiarkan yang basi terus membohongi tim.

3. **Inti mana dalam sistem kita yang, jika keliru, kehilangan uang nyata atau mencelakai seseorang, dan apakah ia mendapat ketelitian yang pantas?** Langkah sentral bab ini adalah mencocokkan metode dengan risiko: heuristik dan agile untuk mayoritas yang dapat dipulihkan, spesifikasi dan verifikasi formal untuk inti kecil berkonsekuensi tinggi, dan pembuatan prototipe murah untuk yang benar-benar tidak pasti. Mode kegagalannya simetris dan keduanya mahal: menerapkan metode formal pada situs mikro pemasaran membakar uang, dan memperlakukan mesin penyelesaian atau rangkaian aturan kelayakan sebagai pekerjaan agile biasa mengundang cacat katastrofik yang tak terbalikkan. Bawa peta sistem Anda dan tandai di mana galat bersifat katastrofik versus dapat dipulihkan, dan di mana persyaratan pasti versus tidak diketahui. Jawabannya harus memusatkan investasi pemodelan Anda di tempat uang dan ambiguitas berada, dan secara eksplisit menahannya di tempat lain, agar inti formal kritis dapat duduk di dalam amplop agile tanpa metode mana pun merembes ke wilayah yang lain.

4. **Berapa banyak pemodelan yang kita lakukan sebelum menulis kode, dan apakah dosis itu berubah menurut ketidakpastian di depan kita?** Desain besar di muka dan tanpa desain sama sekali sama-sama mode kegagalan, dan dosis yang tepat berada di antaranya, diatur oleh seberapa banyak ketidakpastian yang benar-benar dihapus model. Pada tim besar tekanan berjalan ke dua arah: proses tata kelola dapat menuntut seperangkat diagram lengkap sebelum kode apa pun, mengunci keputusan yang dibuat dengan informasi paling sedikit, sementara tekanan pengiriman dapat mendorong tim melewatkan satu mesin status yang akan menangkap kasus tepi mahal. Bawa dua proyek terakhir Anda dan pilah model yang Anda hasilkan menjadi yang menginformasikan keputusan nyata dan yang digambar hanya karena templat memintanya. Dalam program enterprise dan pemerintah, di mana gerbang fase atau dewan persetujuan sering mewajibkan dokumen di muka, bersiaplah berargumen untuk pemodelan yang mengikuti risiko alih-alih daftar keluaran tetap, agar inti pembayaran mendapat ketelitiannya dan perkakas pelaporan internal tidak tenggelam dalam diagram yang tak dibaca siapa pun.

5. **Apakah kita telah menyepakati notasi bersama dan satu rumah untuk model kita, atau setiap tim menciptakan sendiri?** Model adalah artefak komunikasi lebih dulu, dan nilainya runtuh ketika mesin status yang digambar di perkakas satu tim tidak dapat dibaca, ditemukan, atau dipercaya oleh tim yang mewarisinya. Bagi ratusan insinyur pertimbangan yang bersaing itu nyata: notasi dan repositori yang diwajibkan membeli konsistensi dan kemudahan ditemukan, tetapi juga memaksakan biaya belajar dan dapat mendorong orang ke perkakas berat ketika papan tulis yang difoto sudah cukup. Bawa contoh di mana model sebenarnya berada (wiki, perkakas diagram, dek slide, laptop seseorang) dan tanyakan siapa yang dapat menemukan dan memahaminya enam bulan kemudian. Dalam lingkungan enterprise dan yang diatur sudut audit mempertajam ini: auditor yang tidak dapat menemukan model data terkini atau menelusuri keputusan kembali ke mesin status terdokumentasi akan memperlakukan sistem sebagai tidak terdokumentasi, jadi sepakati notasi bersama yang kecil dan lokasi yang tahan lama, dan terima pencatatan ringan daripada upacara di mana pun konsekuensinya rendah.

6. **Sebelum kita membangun prototipe, apakah kita memutuskan dengan sengaja apakah ia sekali pakai atau evolusioner, dan apakah kita menahan diri pada pilihan itu?** Kegagalan klasik yang mahal adalah prototipe sekali pakai yang diam-diam terselip ke produksi karena tampil baik dalam demo dan tak seorang pun menamai jenisnya di muka. Ketegangannya sejati: prototipe sekali pakai membeli pembelajaran termurah dan harus dihapus, sementara prototipe evolusioner menjadi produk dan harus dibangun menurut standar produksi sejak baris pertama, dan mencampuradukkan keduanya entah membuang pengerjaan ulang atau merilis kode rapuh ke peran yang tidak pernah direkayasa untuknya. Bawa prototipe terbaru dan tanyakan apa yang diputuskan sebelum dibangun, siapa yang memegang wewenang mempromosikan atau membuangnya, dan apakah keputusan itu bertahan dari tekanan pengiriman. Dalam pemerintah dan lingkungan akuntabel lainnya, di mana sistem yang menghadap warga membawa kewajiban transparansi dan keandalan, perlakukan promosi tidak sengaja sebagai kegagalan kontrol: tetapkan nasib prototipe di muka, dan jadikan membuang prototipe sekali pakai yang sukses sebagai hasil yang dirayakan alih-alih pemborosan yang dihindari.

## Lensa sektor

**Startup.** Modelkan di papan tulis, foto, dan lanjutkan. Sumber daya Anda yang paling langka adalah perhatian rekayasa, jadi raih model hanya ketika lebih murah daripada kesalahan yang dicegahnya: mesin status langganan sebelum Anda mengode kasus tepi penagihan, bukan seluruh katalog UML untuk produk yang mungkin berputar haluan bulan depan. Tetaplah heuristik dan agile, jauhkan metode formal sepenuhnya, dan perlakukan setiap prototipe sebagai sekali pakai kecuali Anda memutuskan lain secara sadar.

**Bisnis kecil.** Anda kemungkinan tidak punya orang yang tugasnya pemodelan formal, jadi bersandarlah pada model yang sudah tertanam dalam perkakas dan kerangka kerja yang Anda beli alih-alih mendirikan praktik pemodelan sendiri. Bingkai beberapa model yang Anda gambar di sekitar keputusan konkret: sketsa model data sederhana untuk menyepakati data pelanggan apa yang Anda pegang, diagram status untuk satu alur kerja yang membuat Anda kehilangan pelanggan ketika rusak. Pilih produk yang dibeli dengan model data yang terbukti daripada membangun dan mendokumentasikan sendiri, dan jaga apa pun yang Anda gambar cukup ringan agar satu orang dapat memeliharanya.

**Enterprise.** Masalah intinya adalah koordinasi di banyak tim, jadi model bersama menjadi landasan umum: model data yang disepakati, notasi yang konsisten, dan rumah tempat ERD, diagram C4, dan mesin status dapat ditemukan dan dipercaya. Bakukan notasi kecil dan tegakkan konsistensi agar entitas dalam persyaratan, desain, dan basis data tidak menyimpang antartim. Sisakan spesifikasi formal dan model checking untuk inti berkonsekuensi tinggi (penyelesaian, rekonsiliasi, kendali akses), danai keterampilan spesialis yang dituntutnya, dan simpan jejak audit dari setiap model terdokumentasi kembali ke keputusan yang dibenarkannya.

**Pemerintah.** Aturan yang ditetapkan dalam hukum harus dapat dilacak ke undang-undang, di situlah spesifikasi formal pantas biayanya: spesifikasikan logika kelayakan atau penilaian secara presisi, verifikasi sifat kunci, dan biarkan auditor menelusuri setiap hasil kembali ke aturan yang menghasilkannya. Pengadaan menambah bobotnya sendiri, karena dokumen dan model sering menjadi keluaran kontraktual, jadi sepakati model mana yang benar-benar pembawa keputusan alih-alih diproduksi hanya untuk memenuhi daftar periksa. Terbitkan deskripsi bahasa sederhana tentang cara kerja sistem yang berdampak, dan pakai pembuatan prototipe sekali pakai untuk menguji penerimaan yang menghadap warga bersama pengguna nyata sebelum berkomitmen pada build produksi.

## Contoh

**Startup.** Sebuah startup kecil yang membangun produk penagihan langganan membuat sketsa siklus hidup langganan (percobaan, aktif, jatuh tempo, dibatalkan, diaktifkan kembali) sebagai mesin status di papan tulis sebelum menulis kode. Menelusuri diagram, mereka menyadari bahwa mereka tidak pernah mendefinisikan apa yang terjadi ketika pembayaran akun jatuh tempo akhirnya masuk, kasus tepi yang akan membiarkan pelanggan nyata terkatung-katung. Model lima menit itu menyelamatkan sakit kepala produksi, dan mereka memotretnya alih-alih memelihara perkakas diagram berat. Di tempat lain mereka tetap agile dan memodelkan secukupnya untuk menyelaraskan, karena pada skala mereka cacat dapat dipulihkan dan metode formal akan menjadi biaya murni.

**Enterprise.** Sebuah bank global membangun platform pembayaran baru. Tim memakai diagram entitas-relasi untuk menyepakati model data bersama di antara tim rekening, buku besar, dan pesan, dan diagram C4 (bab 3.1) untuk menunjukkan bagaimana layanan saling cocok. Mereka memodelkan siklus hidup transaksi (tertunda, kliring, diselesaikan, dibalik, disengketakan) sebagai mesin status eksplisit, dan analisis mengungkap ia kehilangan transisi untuk pembalikan parsial. Celah itu diperbaiki di papan tulis alih-alih di produksi. Diagram urutan menelusuri alur penyelesaian terhadap persyaratan (bab 2.8) untuk memunculkan jalur timeout dan retry yang hilang. Pengiriman harian bersifat agile, tetapi algoritma rekonsiliasi inti, di mana galat berarti uang nyata hilang, mendapat spesifikasi formal dan diperiksa dengan model checker sebelum implementasi. Pemodelan dipusatkan di tempat uang dan ambiguitas berada, dan dijaga ringan di tempat lain.

**Pemerintah.** Sebuah lembaga pajak nasional memodernisasi penilaian tunjangan. Karena aturan kelayakan ditetapkan dalam hukum dan diaudit, tim menulis spesifikasi formal aturan sebagai transformasi murni dan memverifikasi sifat kunci, seperti tak ada pemohon yang sekaligus layak dan tidak layak dan setiap kasus mencapai keputusan, agar auditor dapat menelusuri hasil kembali ke undang-undang. Berdampingan dengan inti formal, tim membangun prototipe sekali pakai formulir penerimaan yang menghadap warga untuk diuji dengan pengguna nyata. Mereka mengetahui bahwa wizard multilangkah mengurangi galat, lalu membuang prototipe dan membangun ulang penerimaan menurut standar produksi. Diagram aktivitas mendokumentasikan proses petugas kasus dari ujung ke ujung untuk pelatihan dan audit. Aturan berkonsekuensi tinggi mendapat ketelitian formal; pengalaman pengguna yang tidak pasti mendapat pembuatan prototipe murah; tak satu pun metode diterapkan di tempat yang menjadi milik yang lain.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil pemodelan datang dari menemukan cacat lebih awal, di mana jauh lebih murah diperbaiki. Kontradiksi yang ditemukan di papan tulis memakan menit. Kontradiksi yang sama yang ditemukan di produksi dapat memakan pemadaman, program pengerjaan ulang, atau, di ranah yang diatur, liabilitas hukum. Model juga menurunkan total biaya kepemilikan dengan berfungsi sebagai komunikasi tahan lama. Sistem yang hidup lebih lama daripada penulisnya, kasus normal di enterprise dan pemerintah, jauh lebih murah dipelihara ketika model data, mesin status, dan alur kuncinya terdokumentasi secara akurat.

Biayanya nyata, dan Anda harus menimbangnya. Model memakan waktu untuk dibangun, keterampilan untuk dibangun dengan baik, dan upaya berkelanjutan untuk dijaga mutakhir; metode formal menambah tenaga kerja spesialis. Titik impas diatur oleh ketidakpastian dan konsekuensi. Di tempat keduanya rendah, pemodelan berat menghancurkan nilai dan heuristik agile menang. Di tempat salah satunya tinggi, pemodelan yang ditargetkan, dan, untuk inti kritis, verifikasi formal, membalas berkali-kali lipat dengan mencegah kelas kegagalan yang mahal. Untuk meyakinkan pimpinan, kaitkan investasi pemodelan dengan risiko spesifik yang dihapus dan dengan kemudahan pemeliharaan sistem berumur panjang. Dan lacak apakah model benar-benar dirujuk, karena model yang tak terpakai adalah biaya murni.

## Anti-pola dan jebakan

- **Pemodelan demi pemodelan:** memproduksi diagram karena proses menuntutnya, bukan karena menginformasikan keputusan.
- **Model basi dipercaya sebagai kebenaran:** diagram yang tidak lagi cocok dengan kode tetapi masih diandalkan.
- **Desain besar di muka:** model menyeluruh yang diproduksi sebelum kode apa pun, mengunci keputusan yang dibuat dengan informasi paling sedikit.
- **Diagram menjamur:** setiap jenis UML diterapkan seragam, menenggelamkan beberapa tampilan yang berguna dalam derau.
- **Metode formal di mana-mana:** menerapkan verifikasi mahal pada kode di tempat konsekuensi kegagalan tidak membenarkannya.
- **Promosi prototipe tidak sengaja:** prototipe sekali pakai diam-diam dirilis sebagai produk.
- **Notasi di atas substansi:** berdebat tentang kebenaran UML alih-alih apakah model menjawab pertanyaan.

## Model kematangan

- **Tingkat 1 (Memulai):** Pemodelan ad hoc atau tidak ada dan murni reaktif; tidak ada metode yang dinamai; model, bila digambar sama sekali, tidak konsisten, tidak dianalisis, dan ditinggalkan begitu rapat berakhir.
- **Tingkat 2 (Mengembangkan):** Beberapa tim menggambar diagram umum dan mengikuti metode bernama, tetapi praktik tidak merata di seluruh organisasi: model sering diproduksi secara seremonial, menyimpang dari kode, dan jarang dianalisis untuk cacat.
- **Tingkat 3 (Membakukan):** Notasi bersama, panduan pemilihan metode terdokumentasi, dan aturan konsistensi didefinisikan dan ditegakkan di seluruh organisasi; model dipilih menurut tujuan, dijaga sejalan dengan sistem, ditinjau untuk cacat, dan metode dicocokkan dengan risiko setiap masalah.
- **Tingkat 4 (Mengelola):** Pemodelan diukur dan dikendalikan terhadap garis dasar; tim melacak berapa banyak cacat yang ditangkap analisis sebelum implementasi, seberapa jauh model menyimpang dari kode, apakah setiap model benar-benar dirujuk untuk keputusan nyata, dan pengerjaan ulang serta waktu siklus yang dihemat versus garis dasar terdefinisi; pilihan metode dikalibrasi terhadap ketidakpastian dan konsekuensi terukur, dan inti kritis diverifikasi secara formal terhadap target cakupan yang disepakati.
- **Tingkat 5 (Mengorkestrasi):** Pemodelan dan pemilihan metode terus diperbaiki dan terintegrasi dengan perencanaan pengiriman dan risiko di seluruh organisasi; investasi beradaptasi seiring bergesernya ketidakpastian dan konsekuensi, model secara rutin dijaga mutakhir, dipensiunkan, atau diperdalam berdasarkan bukti, dan metode formal, heuristik, dan pembuatan prototipe dikomposisikan agar masing-masing berada persis di tempat ia membuahkan hasil.

## Gagasan untuk didiskusikan

- Untuk proyek terakhir Anda, model mana yang menginformasikan keputusan nyata, dan mana yang digambar hanya karena proses menuntutnya?
- Di mana dalam sistem Anda spesifikasi formal akan membayar dirinya sendiri, dan di mana akan menjadi pemborosan?
- Bagaimana Anda memutuskan apakah prototipe sekali pakai atau evolusioner, dan apakah Anda menegakkan keputusan itu?
- Bagaimana Anda menjaga model agar tidak menyimpang dari kode, atau apakah Anda menerima bahwa sebagian harus dihapus?
- Berapa jumlah pemodelan yang tepat sebelum kode dalam konteks Anda, dan bagaimana ia berubah menurut ketidakpastian?
- Model perilaku mana (status, urutan, atau aktivitas) yang akan menangkap insiden produksi terbaru Anda?

## Poin-poin utama

- Model adalah abstraksi yang bertujuan; jika Anda tidak dapat menamai keputusan yang diinformasikannya, jangan gambar.
- Cocokkan model struktural dan perilaku dengan pertanyaan spesifik, dan jaga tetap konsisten dan mutakhir.
- Analisis model; model yang tidak diperiksa adalah asumsi yang belum teruji.
- Metode heuristik dan agile cocok untuk sebagian besar sistem; sisakan metode formal untuk inti berkonsekuensi tinggi.
- Gunakan prototipe untuk menghapus ketidakpastian, dan putuskan di muka apakah sekali pakai atau evolusioner.
- Berinvestasilah dalam pemodelan sebanding dengan ketidakpastian yang diselesaikannya dan biaya salah mengambil keputusan.

## Referensi dan bacaan lanjutan

- IEEE Computer Society, *SWEBOK Guide (Software Engineering Body of Knowledge), Version 4.0*, area pengetahuan Software Engineering Models and Methods
- Martin Fowler, *UML Distilled: A Brief Guide to the Standard Object Modelling Language*
- Grady Booch, James Rumbaugh, Ivar Jacobson, *The Unified Modelling Language User Guide*
- Frederick P. Brooks, *The Mythical Man-Month* dan *No Silver Bullet: Essence and Accident in Software Engineering*
- Daniel Jackson, *Software Abstractions: Logic, Language, and Analysis* (bahasa pemodelan Alloy)
- Leslie Lamport, *Specifying Systems* (TLA+)
- Simon Brown, *Software Architecture for Developers* (model C4)
- David Harel, *Statecharts: A Visual Formalism for Complex Systems*
