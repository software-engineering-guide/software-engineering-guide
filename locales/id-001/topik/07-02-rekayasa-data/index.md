# 7.2 Rekayasa data

## Tinjauan dan motivasi

[Rekayasa data](https://en.wikipedia.org/wiki/Data_engineering) adalah disiplin membangun dan mengoperasikan pipeline dan platform yang memindahkan data dari tempat ia dihasilkan ke tempat ia menciptakan nilai. Ia mencakup ingesti dari sistem sumber, transformasi menjadi bentuk bersih dan bermodel, penyimpanan dalam format hemat biaya, orkestrasi seluruh alur, dan praktik keandalan yang menjaga semuanya tepercaya. Jika strategi data memutuskan data apa yang seharusnya ada dan siapa yang memilikinya, rekayasa data adalah perpipaan dan mesin yang membuatnya mengalir.

Bagi tim besar, disiplin ini fundamental. Analitik, [business intelligence](https://en.wikipedia.org/wiki/Business_intelligence), eksperimen produk, [pembelajaran mesin](https://en.wikipedia.org/wiki/Machine_learning), dan pelaporan regulasi semuanya berada di hilir pipeline data. Ketika pipeline itu rapuh, lambat, atau buram, setiap fungsi yang bergantung menderita. Dasbor menampilkan angka basi. Model berlatih pada fitur rusak. Auditor tak dapat merekonstruksi bagaimana angka dihasilkan. Pada skala enterprise dan pemerintah, pipeline memproses miliaran catatan dari banyak sistem sumber, dan satu kegagalan senyap dapat mendorong data salah ke keputusan, pembayaran, atau statistik publik.

Bidang ini telah tumbuh dari skrip pesanan dan perkakas [ETL (extract, transform, load)](https://en.wikipedia.org/wiki/Extract,_transform,_load) monolitik menjadi tumpukan data modern: komponen modular, sebagian besar digerakkan SQL, untuk ingesti, transformasi, orkestrasi, dan penyimpanan, dihubungkan oleh format terbuka. Modularitas ini sekaligus anugerah dan jebakan. Ia memungkinkan Anda merakit perkakas terbaik di kelasnya, tetapi tanpa disiplin rekayasa ia menghasilkan sebaran pekerjaan tak terdokumentasi dan tak teruji. Bab ini membahas praktik yang menjaga pipeline idempoten, dapat diuji, dapat diamati, dan terjangkau pada skala besar.

## Prinsip utama

- Pipeline adalah perangkat lunak dan layak mendapat kontrol versi, pengujian, tinjauan, dan CI/CD.
- Pilih transformasi idempoten dan dapat direproduksi yang aman dijalankan ulang.
- Jadikan aliran data dapat diamati: kesegaran, volume, skema, dan kualitas dipantau.
- Modelkan data dengan sengaja untuk konsumennya alih-alih membuang tabel mentah.
- Pilih batch atau streaming berdasarkan kebutuhan latensi nyata, bukan kebaruan.
- Optimalkan format penyimpanan, partisi, dan biaya komputasi sebagai perhatian kelas satu.
- Pisahkan ingesti, transformasi, dan penyajian agar masing-masing dapat berevolusi mandiri.
- Gagal dengan lantang dan dini; pipeline rusak lebih aman daripada data salah yang senyap.

## Rekomendasi

### Pilih ETL atau ELT dengan sengaja

ETL mentransformasi data sebelum memuatnya ke tujuan. [ELT (extract, load, transform)](https://en.wikipedia.org/wiki/Extract,_load,_transform) memuat data mentah dulu dan mentransformasinya di dalam warehouse atau lakehouse yang bertenaga. Platform cloud modern menjadikan ELT bawaan, karena penyimpanan murah dan komputasi elastis, dan menyimpan data mentah memungkinkan Anda memproses ulang ketika logika berubah atau bug muncul. Pilih ELT untuk beban kerja analitik: daratkan data mentah tak berubah, lalu bangun transformasi berlapis di atasnya. Sisihkan transformasi pra-muat untuk kasus di mana privasi, biaya, atau kendala kontrak mewajibkan pembersihan atau penyaringan sebelum data mendarat.

### Rancang pipeline batch dan streaming sesuai kebutuhan latensinya

Sebagian besar kebutuhan analitik terlayani baik oleh pipeline batch terjadwal, yang lebih sederhana dinalar, diuji, dan di-backfill. Raih streaming hanya ketika bisnis benar-benar membutuhkan data berlatensi rendah: deteksi penipuan, peringatan operasional, personalisasi real-time. Streaming menambah kompleksitas nyata seputar pengurutan, semantik exactly-once, data yang tiba terlambat, dan manajemen keadaan. Di mana Anda butuh keduanya, pertimbangkan arsitektur yang menyatukan logika batch dan streaming alih-alih memelihara dua basis kode yang bercabang. Jujurlah tentang persyaratan latensi Anda. "Real-time" sering keinginan yang tak diperiksa yang menggandakan biaya Anda.

### Orkestrasi dengan dependensi eksplisit

Pakai orkestrator untuk mengekspresikan pipeline sebagai [directed acyclic graph (DAG)](https://en.wikipedia.org/wiki/Directed_acyclic_graph) tugas dengan dependensi eksplisit, percobaan ulang, dan penjadwalan. Ini memberi Anda visibilitas ke apa yang berjalan, apa yang gagal, dan apa yang terblokir, plus kemampuan backfill dan menjalankan ulang secara deterministik. Dasarkan dependensi pada ketersediaan data, bukan hanya waktu jam, agar pekerjaan hilir menunggu data hulu alih-alih menyala berdasarkan tebakan. Jaga logika orkestrasi dalam kontrol versi, dan perlakukan perubahan DAG seperti perubahan kode.

### Modelkan data untuk konsumsi

Tabel mentah jarang layak bagi analis. Terapkan [pemodelan dimensional](https://en.wikipedia.org/wiki/Dimensional_modeling), yang menata fakta dan dimensi terkonformasi dalam [skema bintang](https://en.wikipedia.org/wiki/Star_schema), di mana Anda butuh analitik swalayan yang teratur dan dapat dipakai ulang. Tabel lebar denormalisasi ("satu tabel besar") dapat berkinerja lebih baik untuk pola kueri tertentu dan lebih sederhana bagi sebagian konsumen, dengan biaya duplikasi dan fleksibilitas. Lapisi transformasi Anda: lapisan staging mentah, lapisan inti bersih dan terkonformasi, dan mart yang menghadap konsumen. Pemisahan ini memungkinkan Anda memperbaiki logika di satu tempat, dan memungkinkan konsumen bergantung pada antarmuka stabil.

### Jadikan pipeline idempoten dan dapat diuji

Rancang transformasi agar menjalankannya ulang menghasilkan hasil yang sama, alih-alih menduplikasi atau merusak data, misalnya dengan memakai upsert deterministik berkunci pada pengenal bisnis dan pola penimpaan partisi. Tulis uji di berbagai tingkat: unit test untuk logika transformasi, uji skema, dan uji data yang menegaskan ekspektasi seperti keunikan, kunci non-null, integritas referensial, dan rentang nilai yang diterima. Jalankan ini di CI, agar perubahan buruk tertangkap sebelum mencapai data produksi.

### Instrumentasi observabilitas dan keandalan

Pantau empat sinyal inti kesehatan data: kesegaran (apakah mutakhir), volume (apakah jumlah baris dalam rentang diharapkan), skema (apakah struktur berubah tak terduga), dan distribusi (apakah nilai menyimpang secara anomali). Beri peringatan atas pelanggaran, dan alirkan ke tim pemilik. Simpan runbook, rotasi on-call, dan postmortem tanpa menyalahkan untuk insiden data, sama seperti untuk layanan. Lacak silsilah, agar ketika sesuatu rusak, Anda dapat melihat dampak hilir seketika.

### Optimalkan penyimpanan dan biaya

Pakai format kolumnar terbuka seperti Parquet, atau format tabel terbuka yang mendukung evolusi skema, time travel, dan pembaruan efisien. Partisi data menurut kolom yang paling sering Anda filter, biasanya tanggal, dan hindari menjamurnya berkas kecil dengan pemadatan. Pisahkan data panas dan dingin dengan penyimpanan bertingkat dan kebijakan siklus hidup. Pantau pengeluaran komputasi per pipeline dan per kueri. Biaya liar biasanya datang dari pemindaian penuh, partisi yang hilang, dan pemrosesan ulang tak terbatas. Perlakukan biaya sebagai metrik dengan pemilik, bukan kejutan di tagihan bulanan.

## Trade-off: kelebihan dan kekurangan

| Pilihan | Kelebihan | Kekurangan | Paling cocok |
|---|---|---|---|
| ELT (transformasi di tempat) | Menyimpan data mentah, penyimpanan murah, dapat diproses ulang | Jejak penyimpanan besar, butuh tata kelola | Analitik cloud |
| ETL (transformasi sebelum muat) | Mengendalikan biaya, menyaring data sensitif sejak dini | Kehilangan data mentah, lebih sulit diproses ulang | Muatan teregulasi atau terkendala |
| Batch | Sederhana, dapat diuji, backfill mudah | Latensi lebih tinggi | Sebagian besar analitik |
| Streaming | Latensi rendah, reaksi real-time | Kompleks, mahal, sulit diuji | Penipuan, peringatan operasional |
| Skema bintang | Teratur, dapat dipakai ulang, ramah swalayan | Upaya pemodelan di muka | BI bersama |
| Tabel lebar | Cepat untuk kueri yang diketahui, sederhana | Duplikasi, kurang fleksibel | Penggunaan sempit berkinerja tinggi |

Trade-off dominannya adalah kesederhanaan versus latensi dan fleksibilitas. Batch dan ELT dengan skema bintang berlapis memberi Anda sistem yang dapat diuji, dapat di-backfill, dan dipahami baik yang melayani sebagian besar kebutuhan dengan terjangkau. Streaming, real-time, dan desain denormalisasi tinggi membeli kecepatan dan kinerja spesifik, tetapi dengan biaya curam dalam kompleksitas operasional dan kesulitan pengujian. Adopsi kompleksitas hanya di mana persyaratan bisnis konkret membayarnya, dan jaga jalur sederhana sebagai bawaan Anda.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Sudahkah Anda dengan sengaja memilih ELT daripada ETL, dan apakah Anda menyimpan data mentah tak berubah agar dapat memproses ulang ketika logika berubah atau bug muncul?** Bawaan bab ini adalah ELT: daratkan data mentah dengan murah, lalu bangun transformasi berlapis, karena menyimpan data mentah memungkinkan Anda menjalankan ulang segalanya ketika aturan berubah atau bug muncul berminggu-minggu kemudian. Menghapus data mentah menutup opsi itu dan merupakan jebakan umum yang menyakitkan. Argumen yang bersaing untuk ETL nyata dalam muatan teregulasi atau terkendala, di mana privasi, biaya, atau ketentuan kontrak mewajibkan penyaringan atau masking sebelum data mendarat. Bawa bukti: seberapa sering Anda perlu memproses ulang riwayat, dan berapa biayanya ketika tidak bisa? Untuk pipeline pemerintah atau enterprise yang harus menelusuri angka mana pun ke sumber, catatan mentah tak berubah juga persyaratan kemampuan diaudit, jadi jawabannya membentuk baik kebijakan penyimpanan maupun kemampuan dipertahankan secara hukum.

2. **Dari empat sinyal kesehatan data, mana yang benar-benar Anda pantau, dan siapa yang dipanggil ketika salah satunya rusak?** Bab ini menamai empat sinyal yang layak diawasi: kesegaran, volume, skema, dan distribusi. Banyak tim tidak memantau satu pun dan mengetahui kegagalan dari eksekutif yang menatap dasbor basi, yang merupakan pendeteksi terburuk. Pada skala enterprise dan pemerintah, satu kegagalan senyap dapat mendorong data salah ke pembayaran, laporan, atau statistik publik, sehingga biaya deteksi terlambat diukur dalam kepercayaan dan uang, bukan sekadar pengerjaan ulang. Bawa mean time to detect Anda yang sebenarnya dan nama siapa yang saat ini menemukan insiden lebih dulu. Jika jawabannya "konsumen," Anda butuh peringatan yang dialirkan ke tim pemilik plus runbook dan postmortem tanpa menyalahkan, memperlakukan insiden data persis seperti pemadaman layanan.

3. **Apakah analis Anda mengonsumsi mart bermodel dan teruji, atau Anda membuang tabel mentah kepada mereka dan menyebutnya swalayan?** Bab ini lugas: tabel mentah jarang layak bagi analis, dan melapisi transformasi menjadi lapisan staging mentah, inti terkonformasi, dan mart yang menghadap konsumen memungkinkan Anda memperbaiki logika sekali dan memberi konsumen antarmuka stabil. Tarikan yang bersaing adalah kecepatan, karena pemodelan dengan skema bintang atau tabel lebar yang disengaja memakan upaya di muka dan menggoda untuk dilewati. Tetapi membuang data mentah mendorong biaya pemodelan ke setiap analis berulang kali, menghasilkan angka berbeda dan jam terbuang. Bawa sinyal: berapa pangsa waktu analis dihabiskan membentuk ulang data mentah, dan berapa tim telah membangun ulang join yang sama. Jika angkanya tinggi, berinvestasilah pada lapisan inti terkonformasi agar konsumen bergantung pada antarmuka teruji yang dapat dipakai ulang alih-alih menciptakan ulang.

4. **Di mana "real-time" benar-benar layak biayanya, dan di mana ia keinginan tak diperiksa yang diam-diam menggandakan beban operasional Anda?** Bawaan bab ini adalah batch terjadwal, yang lebih sederhana dinalar, diuji, dan di-backfill, dengan streaming disisihkan untuk kasus di mana bisnis benar-benar butuh latensi rendah, seperti deteksi penipuan atau peringatan operasional. Tarikan yang bersaing adalah gengsi dan permintaan pemangku kepentingan yang samar akan data "langsung," yang terdengar murah dalam rapat perencanaan dan menjadi mahal di produksi, karena streaming menyeret pengurutan, semantik exactly-once, data terlambat, dan manajemen keadaan, plus basis kode kedua yang harus diselaraskan dengan logika batch. Bawa bukti ke diskusi: untuk setiap pipeline streaming yang Anda jalankan atau usulkan, namai keputusan yang diberinya makan dan latensi yang benar-benar ditoleransi keputusan itu, diukur dalam menit atau jam alih-alih kata sifat. Untuk platform enterprise atau pemerintah besar, tambahkan biaya on-call dan pengujian setiap jalur real-time, karena pipeline streaming yang tak dapat diuji atau diisi staf sepanjang waktu adalah liabilitas keandalan yang berpakaian fitur, dan jawaban jujur sering meruntuhkan persyaratan "real-time" kembali ke batch per jam yang melayani keputusan yang sama.

5. **Pipeline Anda yang mana yang tak dapat dijalankan ulang dengan aman hari ini, dan apa yang dibutuhkan untuk menjadikan setiap transformasi idempoten?** Bab ini mendesakkan transformasi idempoten dan dapat direproduksi, memakai upsert deterministik berkunci pada pengenal bisnis dan pola penimpaan partisi, agar proses ulang menghasilkan hasil yang sama alih-alih menduplikasi atau merusak data. Tekanan yang bersaing adalah kecepatan pengiriman, karena pekerjaan append-only naif terkirim lebih cepat daripada yang dirancang agar dapat dijalankan ulang, dan biaya jalan pintas itu tersembunyi sampai kegagalan memaksa proses ulang parsial pukul 2 pagi dan seseorang menghitung ganda pendapatan. Bawa inventaris konkret: daftarkan pekerjaan yang akan merusak data jika dijalankan ulang dari titik kegagalan, dan perkirakan radius ledakan yang terburuk. Pada skala enterprise dan pemerintah, di mana satu kegagalan senyap dapat mendorong data salah ke pembayaran, laporan, atau statistik publik, pemrosesan non-idempoten bukan sekadar merepotkan, ia merusak kemampuan diaudit yang memungkinkan Anda memproses ulang suatu periode setelah aturan berubah dan tetap menelusuri setiap angka ke sumber, jadi mendanai pengerjaan ulang agar proses ulang aman adalah soal kontrol, bukan sekadar kerapian.

6. **Apakah Anda tahu berapa biaya menjalankan setiap pipeline, siapa yang memiliki angka itu, dan seberapa banyak tagihan cloud Anda berasal dari pemindaian penuh dan partisi yang hilang?** Bab ini memperlakukan format penyimpanan, partisi, dan pengeluaran komputasi sebagai perhatian kelas satu dengan pemilik, memperingatkan bahwa biaya liar biasanya ditelusuri ke pemindaian penuh, partisi yang hilang, dan pemrosesan ulang tak terbatas. Pertimbangan yang bersaing adalah kerja biaya terasa kurang mendesak daripada mengirim fitur, sehingga ditunda sampai tagihan bulanan menjadi kejutan dan keuangan mulai bertanya yang tak dapat dijawab rekayasa. Bawa bukti: pengeluaran per pipeline dan per kueri, pangsa biaya yang datang dari pemindaian tak terpartisi, dan jumlah berkas kecil yang seharusnya dipadatkan. Untuk organisasi besar yang menjalankan miliaran catatan dari banyak sistem sumber, tagihan cloud tanpa pemilik tumbuh tanpa satu tim pun merasa bertanggung jawab, dan dalam pengaturan pemerintah pengeluaran publik harus dibenarkan baris demi baris, sehingga mengatribusikan biaya komputasi kepada pemilik bernama dengan metrik terlacak mengubah pengeluaran buram menjadi yang terkelola dan sering mengungkap penghematan cukup besar untuk mendanai investasi platform berikutnya.

## Lensa sektor

**Startup.** Kecepatan mengalahkan arsitektur. Sambungkan ingesti ke konektor terkelola, bangun segelintir transformasi terkontrol versi, dan jalankan di orkestrator ringan yang mencoba ulang dan melakukan backfill sendiri, alih-alih menulis tangan pekerjaan cron yang patah senyap semalaman. Jaga setiap model idempoten sejak commit pertama dan tambahkan beberapa uji murah untuk kunci null dan jumlah baris, agar perubahan sumber yang buruk gagal di CI alih-alih muncul di dasbor Senin sang pendiri. Jangan mendirikan streaming atau platform pesanan: sumber daya Anda yang paling langka adalah perhatian rekayasa.

**Bisnis kecil.** Tanpa insinyur data khusus, pilih membeli tumpukan terintegrasi daripada merakitnya. Layanan ELT terkelola plus warehouse cloud memberi Anda konektor, penjadwalan, dan penyimpanan tanpa tim platform untuk memeliharanya. Bingkai pilihan sebagai kebersihan data alih-alih proyek pipeline: ketahui sistem sumber mana yang memberi makan laporan Anda, simpan data mentah agar angka salah dapat ditelusuri dan diproses ulang, dan pilih perkakas yang biayanya dapat diprediksi agar pemindaian tabel penuh tidak menghancurkan anggaran bulanan.

**Enterprise.** Masalahnya konsistensi lintas banyak tim dan miliaran catatan dari banyak sistem sumber. Bakukan pola ELT, model staging-inti-mart berlapis, dan empat sinyal kesehatan data agar kelompok berhenti menciptakan ulang pipeline rapuh. Tegakkan uji data dan CI pada setiap model, atribusikan biaya komputasi ke tim pemilik, dan jalankan insiden data melalui disiplin on-call, runbook, dan postmortem tanpa menyalahkan yang sama dengan yang Anda pakai untuk layanan, agar kegagalan senyap tak pernah mencapai dasbor tanpa disadari.

**Pemerintah.** Aturan pengadaan, transparansi, dan akuntabilitas publik membentuk pipeline. Daratkan catatan mentah tak berubah demi kemampuan diaudit, transformasikan dalam tahap berlapis yang teruji, dan simpan silsilah penuh agar auditor dapat menelusuri angka terbitan mana pun kembali ke dokumen sumbernya, sering persyaratan hukum. Pemrosesan idempoten memungkinkan Anda memproses ulang pengajuan atau periode pelaporan dengan aman ketika aturan berubah, dan memilih format terbuka serta kode transformasi portabel menjaga Anda dari terkunci pada satu vendor sepanjang kontrak multitahun.

## Contoh

**Startup.** Startup analitik sepuluh orang telah menumbuhkan kekusutan pekerjaan cron yang patah senyap semalaman dan kadang menghitung ganda baris ketika insinyur menjalankan ulang satu dengan tangan. Tim pindah ke konektor terkelola untuk ingesti, kerangka transformasi untuk model terkontrol versi, dan orkestrator ringan yang mencoba ulang dan melakukan backfill sendiri. Mereka menjadikan setiap model idempoten dan menambah segelintir uji untuk kunci null dan jumlah baris, sehingga perubahan sumber yang buruk kini gagal di CI alih-alih muncul di dasbor Senin sang pendiri.

**Enterprise.** Sebuah pengecer global mengganti ratusan skrip ekstrak tulisan tangan dengan tumpukan ELT. Konektor terkelola mendaratkan data sumber mentah, kerangka transformasi membangun model teruji dan terkontrol versi di lakehouse, dan orkestrator mengelola dependensi dengan percobaan ulang dan backfill. Uji data menangkap drift skema dari sistem sumber sebelum mencapai dasbor. Penyimpanan kolumnar terpartisi memangkas biaya kueri secara substansial, sambil memperbaiki kesegaran dari harian menjadi per jam.

**Pemerintah.** Sebuah otoritas pajak mengingesti pengajuan dan data pihak ketiga melalui pipeline teratur yang mendaratkan catatan mentah tak berubah demi kemampuan diaudit, lalu mentransformasinya dalam tahap berlapis yang teruji. Pemrosesan idempoten memungkinkan mereka memproses ulang periode pengajuan dengan aman ketika aturan berubah. Silsilah penuh memungkinkan auditor menelusuri angka terhitung mana pun kembali ke dokumen sumber, persyaratan hukum untuk akuntabilitas publik.

## Kasus bisnis: motivasi, ROI, dan TCO

ROI rekayasa data yang disiplin datang dari keandalan, kecepatan, dan kendali biaya. Pipeline andal berarti keputusan dan laporan bertumpu pada data tepercaya, sehingga Anda menghindari pengerjaan ulang mahal dan kerusakan reputasi karena angka salah. Pipeline modular dan teruji memungkinkan tim mengirim produk data baru lebih cepat, menggandakan nilai setiap investasi analitik dan ML hilir. Mengoptimalkan penyimpanan dan komputasi langsung mengurangi tagihan cloud, sering dengan margin besar setelah partisi dan pola kueri diperbaiki.

Biaya adopsi mencakup perkakas platform, waktu rekayasa untuk membangun pipeline modular teruji, dan disiplin memperlakukan data sebagai perangkat lunak. Timbang ini terhadap biaya tidak mengadopsi: pekerjaan pesanan rapuh yang hanya dipahami penulisnya, kerusakan data senyap yang ditemukan eksekutif, pengeluaran cloud menggelembung dari pemindaian tabel penuh, dan analis terblokir menunggu data. Kepada pimpinan, bingkai rekayasa data sebagai fondasi yang membuat analitik, BI, dan AI tepercaya dan terjangkau. Kurang berinvestasi di sini, dan Anda membatasi imbal hasil setiap inisiatif data di atasnya.

## Anti-pola dan jebakan

- Pipeline dibangun sebagai skrip sekali pakai tanpa kontrol versi, uji, atau tinjauan.
- Pekerjaan non-idempoten yang menduplikasi atau merusak data ketika dijalankan ulang setelah kegagalan.
- Mengadopsi streaming demi gengsi ketika batch akan memenuhi persyaratan latensi.
- Membuang tabel mentah kepada analis dan menyebutnya swalayan.
- Tanpa observabilitas, sehingga kegagalan ditemukan oleh konsumen hilir.
- Mengabaikan partisi dan ukuran berkas sampai tagihan cloud meledak.
- Menggabungkan ingesti, transformasi, dan penyajian sehingga tak ada yang dapat berubah dengan aman.
- Menghapus data mentah, membuat mustahil memproses ulang ketika logika berubah.

## Model kematangan

1. Memulai: Skrip ad hoc dan proses manual, tanpa uji atau pemantauan. Kegagalan ditemukan konsumen hilir, pekerjaan tidak aman dijalankan ulang, dan biaya cloud tak dikelola serta tak diatribusikan.
2. Mengembangkan: Sebagian tim telah mengadopsi orkestrator dan menaruh transformasi dasar dalam kontrol versi, tetapi praktik tidak konsisten di seluruh organisasi. Uji sesekali ada, idempotensi tambal-sulam, dan pipeline rusak masih berarti pemadaman kebakaran reaktif.
3. Membakukan: ELT dengan model staging-inti-mart berlapis, teruji dan terkontrol versi, adalah standar terdokumentasi yang diterapkan lintas tim. Dependensi terorkestrasi dengan percobaan ulang dan backfill, uji data berjalan di CI, dan konvensi bersama untuk pemodelan skema bintang dan partisi ditegakkan di seluruh organisasi alih-alih diserahkan kepada tiap kelompok.
4. Mengelola: Platform diukur dan dikendalikan. Kesegaran, volume, skema, dan distribusi dipantau dengan peringatan yang dialirkan ke tim pemilik, dan SLA pipeline, mean time to detect, tingkat lolos kualitas data, serta biaya komputasi per pipeline dan per kueri dilacak terhadap garis dasar. Ambang rollback dan hentikan ditegakkan atas bukti, dan biaya serta keandalan punya pemilik bernama yang dimintai target.
5. Mengorkestrasi: Pipeline diperlakukan sepenuhnya sebagai perangkat lunak dengan CI/CD, kontrak data, dan deteksi anomali otomatis yang menangkap drift sebelum konsumen. Logika batch dan streaming disatukan di mana latensi benar-benar terbayar, platform terus diperbaiki dan swalayan, dan kapasitas, tingkatan penyimpanan, serta biaya diseimbangkan ulang secara adaptif seiring beban kerja bergeser sehingga produk data baru terkirim cepat di atas fondasi stabil.

## Gagasan untuk didiskusikan

- Di mana dalam tumpukan Anda "real-time" benar-benar layak biayanya, dan di mana ia sekadar angan-angan?
- Pipeline mana yang tak dapat dijalankan ulang dengan aman hari ini, dan apa yang dibutuhkan untuk memperbaikinya?
- Seberapa banyak tagihan data cloud Anda berasal dari pemindaian penuh dan partisi yang hilang?
- Apakah analis Anda mengonsumsi mart bermodel atau tabel mentah, dan apa biayanya bagi mereka?
- Berapa mean time to detect Anda untuk insiden data, dan siapa yang menemukannya lebih dulu?
- Apakah menyatukan logika batch dan streaming akan mengurangi beban pemeliharaan Anda atau menambah risiko?

## Poin-poin utama

- Perlakukan pipeline sebagai perangkat lunak: kontrol versi, uji, tinjauan, CI/CD, dan observabilitas.
- Pilih ELT dengan model berlapis yang teruji; simpan data mentah untuk pemrosesan ulang.
- Pilih batch sebagai bawaan dan streaming hanya di mana latensi benar-benar terbayar.
- Jadikan transformasi idempoten agar proses ulang aman.
- Modelkan data untuk konsumen dengan skema bintang atau tabel lebar yang disengaja.
- Pantau kesegaran, volume, skema, dan distribusi, dan perlakukan insiden data seperti pemadaman.
- Optimalkan format penyimpanan, partisi, dan biaya komputasi sebagai perhatian kelas satu.

## Referensi dan bacaan lanjutan

- Joe Reis dan Matt Housley, "Fundamentals of Data Engineering."
- Ralph Kimball dan Margy Ross, "The Data Warehouse Toolkit."
- Martin Kleppmann, "Designing Data-Intensive Applications."
- Bill Inmon, "Building the Data Warehouse."
- James Densmore, "Data Pipelines Pocket Reference."
- Nathan Marz dan James Warren, "Big Data" (arsitektur Lambda).
- Barr Moses dan rekan, "Data Quality Fundamentals" (observabilitas data).
