# 4.5 Privasi dan pelindungan data

## Tinjauan dan motivasi

Keamanan melindungi data dari akses tidak sah. Privasi mengajukan pertanyaan berbeda: haruskah Anda mengumpulkan, memakai, dan menyimpan data itu sama sekali, dan apakah orang yang digambarkannya mendapat suara? Keduanya tumpang tindih, tetapi tidak sama. Anda bisa sepenuhnya aman namun tetap melanggar privasi. Anda melakukannya dengan menimbun data yang tidak berhak Anda pegang, memakainya untuk tujuan yang tak pernah disetujui orang, atau memindahkannya melintasi perbatasan dengan cara yang dilarang hukum. Bagi tim besar, privasi adalah kendala desain. Ia menyentuh setiap layanan yang menangani informasi pribadi, yang hari ini berarti hampir semuanya.

Taruhannya tinggi dan makin naik. Regulasi privasi telah menyebar ke seluruh dunia. Ia membawa denda yang berskala dengan pendapatan, dan memberi individu hak yang dapat ditegakkan atas data mereka. Bagi enterprise, salah menangani data pribadi mengundang tindakan regulator, litigasi gugatan kelompok, dan hilangnya kepercayaan pelanggan yang mahal dibangun kembali. Bagi pemerintah, kewajibannya lebih berat lagi. Warga tidak dapat memilih penyedia lain untuk data pajak, kesehatan, atau tunjangan mereka, sehingga negara berutang kewajiban kehati-hatian khusus kepada mereka. Dan kegagalan privasi mengikis kepercayaan publik yang menjadi sandaran pemerintah.

Bab ini memperlakukan privasi sebagai disiplin rekayasa. Kami membahas merancang untuk privasi sejak awal, meminimalkan dan menyimpan data secara bertanggung jawab, mengklasifikasikan dan melindungi kategori sensitif seperti [PII](https://en.wikipedia.org/wiki/Personally_identifiable_information) dan [PHI](https://en.wikipedia.org/wiki/Protected_health_information), menangani persetujuan dan dasar hukum, dan mengelola persyaratan transfer lintas batas dan residensi yang makin membentuk arsitektur.

*Lihat juga:* bab 4.6 (kepatuhan dan tata kelola), bab 7.1 (strategi dan tata kelola data), dan bab 4.1 (fondasi dan budaya keamanan).

## Prinsip utama

- **[Privacy by design](https://en.wikipedia.org/wiki/Privacy_by_design) dan secara bawaan.** Bangun privasi sejak awal, dan jadikan pengaturan yang paling melindungi privasi sebagai bawaan.
- **[Minimisasi data](https://en.wikipedia.org/wiki/Data_minimization).** Kumpulkan hanya yang benar-benar Anda butuhkan, simpan hanya selama Anda membutuhkannya, dan bagikan hanya seperlunya.
- **Pembatasan tujuan.** Pakai data hanya untuk tujuan spesifik yang diungkapkan saat dikumpulkan.
- **Dasar hukum.** Miliki pembenaran hukum yang sah untuk setiap aktivitas pemrosesan.
- **Hak individu.** Hormati hak orang untuk mengakses, mengoreksi, menghapus, dan memindahkan data mereka.
- **Transparansi.** Katakan dengan jelas kepada orang apa yang Anda kumpulkan, mengapa, dan dengan siapa Anda membagikannya.
- **Akuntabilitas.** Mampu mendemonstrasikan kepatuhan, bukan sekadar mengklaimnya.

## Rekomendasi

### Rancang untuk privasi sejak awal

Privasi yang ditempelkan pada sistem jadi mahal dan tidak lengkap. Bangun sejak awal.

- Lakukan **[Data Protection Impact Assessment](https://en.wikipedia.org/wiki/Data_protection_impact_assessment) (DPIA)** untuk sistem dan fitur baru yang memproses data pribadi pada skala besar atau membawa risiko lebih tinggi, mengidentifikasi dan memitigasi risiko privasi sebelum membangun.
- Jadikan bawaan melindungi privasi: opt-in alih-alih opt-out untuk pemrosesan nonesensial, bidang data minimal, dan retensi tersingkat yang masuk akal.
- Libatkan keahlian privasi sejak dini dalam desain, bersama pemodelan ancaman keamanan, agar keduanya dipertimbangkan pada tahap batas kepercayaan.
- Pelihara **peta atau inventaris data**: data pribadi apa yang Anda pegang, di mana ia berada, mengapa, dan ke mana ia mengalir. Anda tidak dapat melindungi atau mempertanggungjawabkan data yang tak dapat Anda lihat.

### Minimalkan, simpan, dan hapus secara bertanggung jawab

Setiap bagian data pribadi yang Anda pegang adalah liabilitas sebanyak aset.

- **Minimalkan pengumpulan:** tantang setiap bidang. Jika Anda tidak membutuhkannya untuk tujuan yang dinyatakan, jangan kumpulkan.
- **Tetapkan jadwal retensi** menurut jenis data dan tujuan, dan tegakkan dengan penghapusan otomatis. Data yang disimpan "untuk jaga-jaga" adalah data yang menunggu dibobol atau di-subpoena.
- **Dukung hak penghapusan:** bangun kemampuan menemukan dan menghapus data individu di semua sistem, termasuk cadangan dan salinan hilir, dalam tenggat hukum. Ini jauh lebih mudah bila dirancang masuk daripada ditempelkan.
- **[Anonimkan](https://en.wikipedia.org/wiki/Data_anonymization) atau agregasikan** data untuk analitik dan pengujian agar data yang dapat diidentifikasi tidak menyebar ke lingkungan sekunder.

### Klasifikasikan dan lindungi data sensitif

Tidak semua data pribadi membawa risiko yang sama, dan sebagian kategori membawa bobot hukum khusus.

- Klasifikasikan data ke dalam tingkatan, membedakan **PII** (personally identifiable information), **PHI** (protected health information), data keuangan, dan kategori khusus (seperti ras, agama, kesehatan, biometrik, atau seksualitas) yang membawa perlindungan hukum yang ditingkatkan.
- Terapkan perlindungan sebanding dengan sensitivitas: kendali akses, enkripsi, dan pemantauan lebih kuat untuk tingkatan paling sensitif.
- Gunakan **[tokenisasi](https://en.wikipedia.org/wiki/Tokenization_(data_security))** untuk mengganti nilai sensitif (seperti nomor kartu atau pengenal nasional) dengan token nonsensitif, mengecilkan sistem yang pernah menyentuh data mentah dan dengan demikian mengecilkan cakupan kepatuhan.
- Gunakan **[pseudonimisasi](https://en.wikipedia.org/wiki/Pseudonymization)** untuk memisahkan pengenal dari sisa catatan agar data kurang dapat langsung diatribusikan, mengurangi risiko sambil mempertahankan kegunaan.
- Samarkan data sensitif dalam log, pesan galat, analitik, dan lingkungan nonproduksi.

### Tangani persetujuan dan dasar hukum dengan benar

Memproses data pribadi membutuhkan landasan hukum yang sah, dan persetujuan hanya salah satu dari beberapa.

- Identifikasi dan dokumentasikan **dasar hukum** untuk setiap aktivitas pemrosesan: persetujuan, kontrak, kewajiban hukum, kepentingan vital, tugas publik, atau kepentingan sah, tergantung rezim yang berlaku.
- Di mana persetujuan adalah dasarnya, jadikan **diberikan dengan bebas, spesifik, terinformasi, dan tidak ambigu**, dengan cara yang sama mudahnya untuk menariknya. Kotak yang sudah dicentang dan persetujuan yang dibundel tidak sah.
- Catat persetujuan: apa yang disetujui orang, kapan, dan atas ketentuan apa, agar Anda dapat mendemonstrasikannya.
- Hormati **pembatasan tujuan**: jangan alihkan tujuan data untuk sesuatu yang tidak sesuai dengan alasan pengumpulannya tanpa dasar baru.
- Hormati sinyal seperti [Do Not Track](https://en.wikipedia.org/wiki/Do_Not_Track) / [Global Privacy Control](https://en.wikipedia.org/wiki/Global_Privacy_Control) dan permintaan opt-out di tempat hukum mewajibkan.

### Kelola transfer lintas batas dan residensi data

Di mana data secara fisik berada dan bergerak kini perhatian arsitektural tingkat pertama.

- Pahami persyaratan **residensi data**: sebagian yurisdiksi mewajibkan data tertentu tetap di dalam perbatasan nasional, dan sebagian data pemerintah harus tetap di lingkungan berdaulat atau terakreditasi tertentu.
- Untuk **transfer lintas batas**, pastikan mekanisme hukum yang sah (keputusan kecukupan, klausul kontraktual standar, atau padanannya) ada dan terdokumentasi.
- Arsitekturkan untuk residensi sejak awal: penyimpanan terpaku wilayah, lokalisasi data, dan kendali hati-hati atas ke mana cadangan, log, dan data analitik mengalir, karena ini sering membocorkan data lintas batas tanpa disadari.
- Lacak sub-prosesor dan pihak ketiga; vendor yang memindahkan data ke luar negeri dapat melanggar kewajiban residensi atas nama Anda.

## Trade-off: kelebihan dan kekurangan

| Keputusan | Kelebihan | Kekurangan |
|---|---|---|
| Minimisasi data agresif | Risiko lebih kecil, dampak pembobolan lebih kecil, kepatuhan lebih sederhana | Dapat membatasi analitik dan opsi produk masa depan |
| Retensi panjang | Riwayat kaya untuk analitik, ML, sengketa | Liabilitas lebih besar, paparan pembobolan, kompleksitas penghapusan |
| Tokenisasi | Mengecilkan cakupan kepatuhan, melindungi data mentah | Kompleksitas sistem tambahan, vault token untuk diamankan |
| Bawaan opt-in | Kepercayaan lebih kuat, kepatuhan jelas | Volume data lebih rendah, metrik pertumbuhan lebih sulit |
| Residensi data regional | Memenuhi mandat hukum, membangun kepercayaan kedaulatan | Kompleksitas arsitektural, biaya lebih tinggi, infrastruktur terduplikasi |
| Data lake terpusat | Kekuatan analitik, satu sumber | Risiko terkonsentrasi, pembatasan tujuan lebih sulit |

Ketegangan pusatnya adalah antara selera bisnis terhadap data dan liabilitas yang diwakili data itu. Tim produk dan analitik secara alami ingin mengumpulkan lebih banyak dan menyimpannya lebih lama. Disiplin privasi menarik ke arah lain. Penyelesaian yang matang membingkai ulang data sebagai liabilitas yang harus dibenarkan, bukan aset yang ditimbun. Setiap keputusan pengumpulan dan retensi harus layak dipertahankan terhadap risiko yang diciptakannya. Residensi data menambah dimensi biaya-versus-kepatuhan. Memenuhi persyaratan kedaulatan dapat melipatgandakan infrastruktur, namun itu sama sekali tidak dapat ditawar di sebagian pasar dan konteks pemerintah.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apa jadwal retensi Anda untuk setiap kelas data pribadi, dan apa yang menegakkan penghapusan?** Data yang disimpan "untuk jaga-jaga" adalah data yang menunggu dibobol atau di-subpoena, jadi setiap bidang dan setiap catatan butuh masa hidup terdefinisi yang terikat pada tujuannya. Putuskan jadwal menurut jenis data, lalu tegakkan dengan penghapusan otomatis alih-alih memercayai siapa pun untuk mengingat. Bagi enterprise ini mengecilkan paparan pembobolan dan biaya penyimpanan sekaligus, dan bagi pemerintah ia selaras dengan kewajiban undang-undang menahan data warga tidak lebih lama daripada yang diizinkan hukum. Bawa sampel catatan tersimpan tertua Anda dan tanyakan siapa yang masih membutuhkannya dan atas dasar apa, karena jawaban jujurnya sering tak ada. Jika penghapusan manual atau tidak ada, data menumpuk selamanya dan liabilitas Anda tumbuh diam-diam di neraca.

2. **Bidang sensitif mana yang dapat Anda tokenisasi atau pseudonimkan untuk mengecilkan risiko sekaligus cakupan kepatuhan?** Mengganti nomor kartu atau pengenal nasional dengan token membatasi nilai mentah pada vault kecil yang dikendalikan ketat, yang tajam memotong sistem dalam cakupan untuk audit seperti PCI-DSS. Pseudonimisasi memisahkan pengenal dari sisa catatan, menurunkan risiko sambil mempertahankan kegunaan data untuk analitik dan pengujian. Putuskan nilai sensitivitas tinggi mana yang membenarkan vault token (kompleksitas tambahan, vault untuk diamankan) dan mana yang cukup disamarkan dalam log dan nonproduksi. Bawa peta ke mana nilai sensitif mentah mengalir hari ini, karena setiap sistem yang menyentuhnya adalah sistem yang harus Anda lindungi dan audit. Untuk data teregulasi dan pemerintah, pengurangan cakupan ini salah satu dari sedikit langkah yang menurunkan biaya dan risiko sekaligus, jadi targetkan bidang paling sensitif Anda lebih dulu.

3. **Sebelum fitur Anda berikutnya dikirim, apa yang memicu Data Protection Impact Assessment dan siapa yang menjalankannya?** Privasi yang ditempelkan pada sistem jadi mahal dan tidak lengkap, jadi DPIA harus berjalan lebih awal, bersama pemodelan ancaman keamanan, ketika Anda masih dapat mengubah desain dengan murah. Putuskan pemicunya (pemrosesan baru pada skala besar, data kategori khusus, tujuan baru) dan namai siapa yang memiliki penilaian agar tidak terlewat di bawah tekanan pengiriman. DPIA nyata dapat menangkap pengumpulan berlebih sebelum peluncuran, misalnya mengganti lokasi presisi dengan data wilayah kasar tanpa kehilangan produk. Bawa fitur yang akan datang dan telusuri: data pribadi apa yang dikumpulkannya, mengapa, dan apakah desain yang kurang invasif mencapai tujuan yang sama. Untuk layanan pemerintah yang tidak dapat dipilih keluar oleh warga, pemeriksaan awal ini bagian dari kewajiban kehati-hatian, jadi jadikan ia gerbang, bukan renungan belakangan.

4. **Ketika data pribadi melintasi perbatasan, termasuk lewat cadangan, log, dan sub-prosesor, mekanisme hukum apa yang mencakup setiap persilangan, dan dapatkah Anda membuktikannya?** Aturan residensi dan transfer kini membentuk arsitektur sebanyak persyaratan kinerja mana pun, dan persilangan yang menjebak tim jarang yang jelas: log yang dikirim ke perkakas observabilitas luar negeri, cadangan yang direplikasi ke wilayah lebih murah, atau sub-prosesor yang diam-diam memindahkan data ke luar negeri. Bagi organisasi besar tekanan yang bersaing itu nyata, karena infrastruktur terpaku wilayah berbiaya lebih dan menduplikasi operasi, namun satu transfer melanggar hukum dapat membatalkan masuk pasar atau memicu perintah penegakan. Bawa peta aliran data saat ini yang menamai setiap tempat data pribadi secara fisik berada atau berpindah, mekanisme hukum untuk setiap perbatasan yang dilintasinya (keputusan kecukupan, klausul kontraktual standar, atau padanannya), dan daftar sub-prosesor beserta lokasinya. Untuk konteks pemerintah dan data berdaulat, perlakukan residensi sebagai kendala arsitektural keras alih-alih klausul kontrak, karena sebagian catatan tidak boleh pernah meninggalkan lingkungan nasional terakreditasi, dan badan yang bertanggung jawab tidak dapat mendelegasikan kewajiban itu kepada vendor.

5. **Dasar hukum mana yang mendukung setiap aktivitas pemrosesan, dan dapatkah Anda membela pilihan itu kepada regulator besok?** Persetujuan hanya salah satu dari beberapa landasan hukum, dan tim sering bawaan ke sana padahal kontrak, kewajiban hukum, tugas publik, atau kepentingan sah akan lebih jujur dan lebih tahan lama. Ini penting pada skala besar karena dasar yang lemah atau salah pilih dapat membatalkan seluruh pipeline, dan mengurai pemrosesan yang tidak berhak Anda lakukan jauh lebih mahal daripada memilih dasar yang benar di muka. Timbang pertimbangan yang bersaing secara terbuka: persetujuan memberi individu kendali tetapi dapat ditarik dan harus diberikan bebas, spesifik, dan tidak dibundel, sementara dasar seperti kepentingan sah menghindari kelelahan persetujuan tetapi menuntut uji penimbangan terdokumentasi. Bawa register yang memetakan setiap aktivitas pemrosesan ke dasar yang diklaimnya, bukti yang mendukung, dan bagaimana Anda akan menarik atau beralih jika ditantang. Di pemerintah, sebagian besar pemrosesan inti bertumpu pada tugas publik alih-alih persetujuan, jadi presisilah tentang di mana persetujuan opsional yang dapat ditarik dimulai, karena mengaburkan keduanya mengikis kepercayaan yang tak punya pilihan selain diberikan warga.

6. **Jika seseorang menggunakan hak akses, penghapusan, atau portabilitas hari ini, dapatkah Anda memenuhinya di setiap sistem dalam tenggat hukum?** Hak individu mudah dijanjikan dalam kebijakan privasi dan sulit dihormati dalam arsitektur yang menyebar salinan data pribadi ke cadangan, cache, penyimpanan analitik, dan layanan hilir. Bagi tim besar ini momen kepatuhan abstrak menjadi uji rekayasa konkret, dan tenggat undang-undang yang terlewat adalah kegagalan yang harus dilaporkan sekaligus sinyal bahwa Anda tidak dapat melihat data Anda sendiri. Pertimbangan yang bersaing adalah biaya dan kompleksitas, karena membangun penghapusan dan ekspor lintas sistem yang sejati adalah kerja nyata, tetapi alternatifnya pemenuhan manual, lambat, dan rawan galat yang tidak berskala dan diam-diam melanggar hukum. Bawa penelusuran jujur satu permintaan nyata dari penerimaan sampai selesai, termasuk bagaimana cadangan dan pihak ketiga dijangkau, dan ukur terhadap tenggat hukum. Untuk layanan pemerintah yang tidak dapat ditinggalkan orang, perlakukan pemenuhan hak yang swalayan, lengkap, dan dapat diaudit sebagai bagian kewajiban kehati-hatian, bukan fitur untuk dijadwalkan belakangan.

## Lensa sektor

**Startup.** Dengan tim kecil dan landasan pendek, perlakukan privasi sebagai asuransi murah alih-alih program yang tak sanggup Anda isi stafnya. Kumpulkan hanya bidang yang dibutuhkan fitur inti Anda, simpan peta data spreadsheet ringan agar Anda benar-benar dapat menjawab permintaan penghapusan, dan jaga email serta token di luar log Anda. Alur persetujuan yang jelas dan penghapusan nyata memakan satu sore sekarang; memasangnya belakangan setelah pelanggan enterprise pertama atau regulator bertanya berbiaya jauh lebih besar, dan data yang dikumpulkan berlebih adalah liabilitas yang tidak memberi Anda keuntungan apa pun.

**Bisnis kecil.** Tanpa spesialis privasi khusus dan dengan anggaran ketat, bersandarlah pada kendali privasi yang sudah ada dalam perkakas yang Anda beli, dan pilih vendor yang membuat penanganan data transparan dan residensi jelas. Bingkai keputusan sebagai beli versus bangun: Anda hampir tidak pernah membangun tokenisasi atau pemenuhan hak sendiri, jadi pilih platform yang menawarkan aturan retensi, ekspor, dan penghapusan secara langsung. Ketahui data pribadi apa yang Anda pegang dan di mana catatan yang salah atau hilang akan membuat Anda kehilangan pelanggan, dan tuliskan dasar hukum untuk setiap penggunaan meski dokumennya singkat.

**Enterprise.** Pada skala besar masalahnya konsistensi di banyak tim: peta data bersama, tingkat klasifikasi terstandar, dan retensi yang ditegakkan agar tak ada kelompok tunggal yang menjadi mata rantai lemah. Anggarkan rekayasa untuk penghapusan lintas sistem, vault tokenisasi, dan arsitektur sadar-residensi secara eksplisit, dan atur sub-prosesor secara terpusat agar satu vendor tidak dapat melanggar kewajiban transfer atas nama Anda. Jadikan DPIA gerbang dalam proses pengiriman dan ukur postur privasi, karena auditor dan regulator akan meminta Anda mendemonstrasikan kepatuhan, bukan sekadar menegaskannya.

**Pemerintah.** Aturan pengadaan, kewajiban transparansi, dan akuntabilitas publik membentuk setiap pilihan, dan warga tidak dapat membawa data pajak, kesehatan, atau tunjangan mereka ke tempat lain, sehingga kewajiban kehati-hatian meningkat. Kunci catatan sensitif ke lingkungan nasional terakreditasi termasuk cadangan dan analitik, ikat setiap vendor secara kontraktual pada kewajiban residensi dan penghapusan yang sama, dan dokumentasikan dasar hukum (sering tugas publik) untuk pemrosesan inti sambil menjaga penggunaan opsional pada persetujuan terpisah yang dapat ditarik. Terbitkan deskripsi bahasa sederhana tentang apa yang Anda kumpulkan dan mengapa, dan buat pemenuhan hak andal dalam garis waktu undang-undang, karena kegagalan privasi di sini mengikis kepercayaan publik yang menjadi sandaran layanan.

## Contoh

**Startup.** Sebuah aplikasi konsumen tahap awal hanya mengumpulkan data yang benar-benar dibutuhkannya, karena setiap bidang tambahan adalah liabilitas yang lebih suka tidak ia bela kelak. Ia menyimpan peta data spreadsheet sederhana tentang di mana data pribadi berada agar benar-benar dapat menjawab permintaan penghapusan, menjaga email dan token di luar log, dan menetapkan aturan retensi dasar untuk membersihkan data dari akun yang sudah lama mati. Membangun alur persetujuan yang jelas dan penghapusan nyata sekarang memakan satu sore; memasangnya belakangan setelah pelanggan enterprise atau regulator pertama bertanya berbiaya jauh lebih besar.

**Enterprise.** Sebuah aplikasi konsumen global melakukan DPIA sebelum meluncurkan fitur rekomendasi baru dan menemukan bahwa ia akan mengumpulkan lokasi presisi secara tidak perlu; tim beralih ke data wilayah kasar, mengurangi risiko tanpa kehilangan produk. Nomor kartu ditokenisasi sehingga hanya vault kecil yang dikendalikan ketat yang pernah menyimpan nilai mentah, memotong cakupan [PCI](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard) (payment card industry) perusahaan secara dramatis. Aturan retensi otomatis membersihkan data akun tidak aktif sesuai jadwal, dan alur swalayan memungkinkan pengguna mengekspor dan menghapus data mereka dalam tenggat hukum di semua sistem termasuk cadangan.

**Pemerintah.** Sebuah layanan kesehatan nasional mengklasifikasikan semua rekam pasien sebagai PHI dan data kategori khusus, menegakkan kendali akses ketat, enkripsi, dan pencatatan audit. Kebijakan residensi data menjaga semua catatan di dalam perbatasan nasional, termasuk cadangan dan analitik, dan setiap vendor terikat secara kontraktual pada hal yang sama. Warga memiliki dasar hukum terdokumentasi (tugas publik) untuk pemrosesan inti, sementara penggunaan riset opsional memerlukan persetujuan terpisah yang dapat ditarik, dicatat, dan dihormati. Peta data menopang kemampuan menanggapi permintaan akses dan penghapusan dalam garis waktu undang-undang.

## Kasus bisnis: motivasi, ROI, dan TCO

Investasi privasi sering dibingkai sebagai biaya kepatuhan murni, tetapi itu meremehkannya. Total biaya kepemilikan mencakup proses DPIA, perkakas pemetaan dan inventaris data, infrastruktur tokenisasi dan retensi, serta rekayasa untuk mendukung hak individu dan residensi. Timbang itu terhadap biaya tidak berinvestasi, yang parah dan makin mungkin. Denda privasi kini mencapai persentase pendapatan global, gugatan kelompok menyusul pembobolan besar, dan regulator telah menunjukkan mereka akan bertindak. Di luar denda, privasi yang salah ditangani menghancurkan kepercayaan pelanggan yang menopang pendapatan. Dan memperbaiki kegagalan privasi setelah kejadian (memasang penghapusan, mengurai aliran data melanggar hukum) berbiaya jauh lebih besar daripada membangunnya masuk.

ROI juga punya sisi atas yang nyata. Privasi yang kuat adalah pembeda kompetitif, dan di pasar teregulasi dan pemerintah ia prasyarat untuk memenangkan bisnis sama sekali. Minimisasi data langsung mengurangi paparan pembobolan dan biaya penyimpanan, dan tokenisasi mengecilkan cakupan mahal audit seperti PCI-DSS. Ketika mengajukan kasus kepada pimpinan, sajikan privasi dengan dua cara: sebagai manajemen liabilitas berbobot risiko dengan paparan regulasi nyata, dan sebagai aset kepercayaan yang membuka pasar. Tekankan bahwa privacy-by-design murah dibanding privacy-by-lawsuit, dan bahwa data yang ditimbun tanpa tujuan adalah liabilitas yang duduk di neraca, menunggu direalisasikan.

## Anti-pola dan jebakan

- **Kumpulkan semuanya, putuskan nanti.** Menimbun data tanpa tujuan, memaksimalkan liabilitas tanpa manfaat.
- **Retensi karena pengabaian.** Tidak pernah menghapus apa pun karena tak ada jadwal, sehingga data menumpuk selamanya.
- **Teater persetujuan.** Kotak sudah dicentang, persetujuan dibundel, atau pola gelap yang tidak sah secara hukum dan mengikis kepercayaan.
- **Penghapusan yang melewatkan cadangan.** Menghapus dari penyimpanan utama tetapi meninggalkan salinan di cadangan, log, dan analitik.
- **PII dalam log dan data uji.** Menyebar data sensitif ke lingkungan yang kurang terkendali tempat ia mudah terekspos.
- **Mengabaikan aliran data.** Mengabaikan bahwa log, cadangan, analitik, dan sub-prosesor memindahkan data lintas batas.
- **Privasi sebagai urusan hukum saja.** Memperlakukannya sebagai kertas kerja alih-alih kendala desain rekayasa.
- **Tanpa peta data.** Tidak mampu menjawab di mana data pribadi berada, yang membuat permintaan hak dan respons pembobolan mustahil.

## Model kematangan

**Tingkat 1: Memulai.** Privasi ditangani secara reaktif, jika ada. Data pribadi dikumpulkan bebas tanpa inventaris, minimisasi, atau batas retensi. Persetujuan adalah renungan belakangan, tidak ada proses untuk permintaan akses atau penghapusan, dan di mana data secara fisik berada tidak dipertimbangkan.

**Tingkat 2: Mengembangkan.** Praktik dasar muncul tetapi bervariasi menurut tim. Kebijakan privasi ada dan persetujuan dasar ditangkap, dengan sedikit kesadaran tentang retensi. Permintaan hak ditangani manual dan lambat, klasifikasi data informal, dan satu tim mungkin memetakan datanya sementara yang lain mengumpulkan bebas. Tidak ada yang ditegakkan konsisten di seluruh organisasi.

**Tingkat 3: Membakukan.** Privacy by design terdokumentasi dan ditegakkan di seluruh organisasi. DPIA berjalan untuk proyek berisiko lebih tinggi, data dipetakan dan diklasifikasikan ke dalam tingkatan, dan jadwal retensi ditegakkan dengan penghapusan otomatis. Dasar hukum didokumentasikan untuk setiap aktivitas pemrosesan, mekanisme persetujuan yang sah ada, permintaan hak dipenuhi dalam tenggat, dan residensi ditangani untuk data teregulasi.

**Tingkat 4: Mengelola.** Program privasi diukur dan dikendalikan terhadap garis dasar. Anda melacak waktu pemenuhan permintaan hak terhadap tenggat undang-undang, cakupan kebijakan retensi dan usia catatan tertua, jumlah bidang data pribadi dalam cakupan dan berapa yang ditokenisasi atau dipseudonimkan, tingkat penyelesaian DPIA untuk fitur yang memenuhi syarat, dan jumlah aliran lintas batas tak terkelola yang ditemukan dalam audit. Metrik memberi makan ambang terdefinisi, sehingga pelanggaran target (permintaan hak mendekati tenggat, transfer tak terduga, penyimpangan retensi) memicu respons terdokumentasi alih-alih tak terlihat.

**Tingkat 5: Mengorkestrasi.** Privasi adalah kendala rekayasa bawaan yang terus diperbaiki dan terintegrasi di seluruh organisasi. Minimisasi, tokenisasi, dan retensi otomatis adalah standar, permintaan hak bersifat swalayan dan lengkap di semua sistem termasuk cadangan, dan aliran data serta residensi dilacak dan ditegakkan secara berkelanjutan. Postur privasi beradaptasi seiring regulasi, pasar, dan arsitektur bergeser, memasukkan pelajaran kembali ke desain sehingga garis dasar terus naik alih-alih sekadar bertahan.

## Gagasan untuk didiskusikan

1. Bagaimana Anda menyelesaikan ketegangan antara tim analitik yang menginginkan lebih banyak data dan privasi yang menginginkan lebih sedikit?
2. Apa arsitektur realistis untuk menghormati penghapusan di penyimpanan utama, cadangan, dan salinan hilir?
3. Dasar hukum mana yang cocok untuk setiap aktivitas pemrosesan Anda, dan dapatkah Anda membela pilihan itu?
4. Bagaimana Anda menjaga data pribadi di luar log dan lingkungan nonproduksi tanpa menghambat debugging?
5. Persyaratan residensi data apa yang berlaku untuk pasar Anda, dan bagaimana cadangan dan analitik memperumitnya?
6. Bagaimana pemodelan ancaman privasi dan keamanan harus digabungkan menjadi satu aktivitas desain?

## Poin-poin utama

- Privasi mengatur apakah dan bagaimana Anda memakai data pribadi; ia berbeda dari dan melengkapi keamanan.
- Rancang privasi masuk sejak awal dengan DPIA dan bawaan yang melindungi privasi.
- Minimalkan pengumpulan, tegakkan jadwal retensi, dan bangun kemampuan penghapusan yang sejati.
- Klasifikasikan PII, PHI, dan kategori khusus, dan lindungi secara sebanding dengan tokenisasi dan penyamaran.
- Tetapkan dan dokumentasikan dasar hukum; jadikan persetujuan diberikan bebas, spesifik, dan dapat ditarik.
- Perlakukan residensi data dan transfer lintas batas sebagai kendala arsitektural tingkat pertama.
- Data adalah liabilitas sekaligus aset; menimbunnya tanpa tujuan adalah risiko yang menunggu direalisasikan.

## Referensi dan bacaan lanjutan

- Ann Cavoukian, *Privacy by Design: The 7 Foundational Principles*
- European Union, teks dan panduan *General Data Protection Regulation (GDPR)*
- National Institute of Standards and Technology, *Privacy Framework* dan *SP 800-122* (Guide to Protecting PII)
- ISO/IEC 27701, *Privacy Information Management*
- Daniel Solove, *Understanding Privacy*
- OECD, *Privacy Guidelines* dan *Fair Information Practice Principles (FIPPs)*
- Teks undang-undang California Consumer Privacy Act (CCPA/CPRA) dan panduan regulator
