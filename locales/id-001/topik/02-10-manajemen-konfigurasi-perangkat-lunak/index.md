# 2.10 Manajemen konfigurasi perangkat lunak

## Tinjauan dan motivasi

[Manajemen konfigurasi perangkat lunak](https://en.wikipedia.org/wiki/Software_configuration_management) (SCM) adalah disiplin mengidentifikasi komponen sistem perangkat lunak, mengendalikan bagaimana mereka berubah, mencatat keadaan setiap perubahan, dan memverifikasi bahwa apa yang Anda bangun dan serahkan cocok dengan apa yang Anda maksudkan. Ia menjawab pertanyaan yang terdengar sederhana tetapi menjadi sulit pada skala besar: apa persisnya yang ada dalam rilis ini, bagaimana sampai di sana, dan siapa yang menyetujuinya? [SWEBOK](https://en.wikipedia.org/wiki/Software_Engineering_Body_of_Knowledge) memperlakukan SCM sebagai area pengetahuan fondasional dengan alasan yang jelas: setiap kegiatan rekayasa lain membutuhkan konfigurasi yang stabil dan diketahui untuk dikerjakan.

Pada tim besar, SCM adalah jaringan penghubung yang menjaga ribuan bagian yang bergerak tetap koheren. Kode sumber, pustaka, citra kontainer, definisi infrastruktur, data konfigurasi, dokumentasi, dan artefak tes semuanya berubah menurut jamnya sendiri, dan sistem yang diserahkan adalah satu kombinasi spesifik dari versi spesifik semuanya. Tanpa manajemen konfigurasi yang disengaja, kombinasi itu tidak diketahui dan tidak dapat direproduksi. Anda tidak dapat menciptakan ulang rilis masa lalu, melacak cacat ke perubahan yang menyebabkannya, atau mengatakan dengan percaya diri apa yang berjalan di produksi.

Lingkungan enterprise dan pemerintah menaikkan taruhan. Program yang diatur dan sektor publik harus menunjukkan bahwa perubahan diotorisasi, ditinjau, dan dicatat; bahwa build yang diserahkan dapat dilacak ke persyaratan dan sumber yang disetujui; dan bahwa tidak ada yang masuk ke sistem tanpa kendali. Di sini SCM sama banyaknya sistem bukti seperti sistem rekayasa. [Kontrol versi](https://en.wikipedia.org/wiki/Version_control) (bab 2.6) mengelola riwayat sumber; SCM mengatur seluruh konfigurasi dan proses terkendali tempat ia berubah. Ia terkait erat dengan [infrastruktur sebagai kode](https://en.wikipedia.org/wiki/Infrastructure_as_code) (bab 8.2), pipeline pengiriman (bab 8.1), dan audit serta jaminan (bab 10.2).

## Prinsip utama

- Segala sesuatu yang menentukan perilaku sistem adalah [butir konfigurasi](https://en.wikipedia.org/wiki/Configuration_item) di bawah kendali, bukan hanya kode sumber.
- [Baseline](https://en.wikipedia.org/wiki/Baseline_(configuration_management)) adalah titik rujukan yang diketahui dan disepakati; perubahan dibuat terhadap baseline dengan sengaja, bukan sembarangan.
- Perubahan dikendalikan dan dicatat, bukan dicegah; tujuannya adalah perubahan yang diotorisasi dan dapat dilacak.
- Akuntansi status berarti Anda selalu dapat menjawab apa yang ada dalam suatu konfigurasi dan apa riwayat perubahannya.
- Audit memverifikasi bahwa sistem yang dibangun dan diserahkan cocok dengan konfigurasi tercatat dan persyaratan yang disetujui.
- Keterreproduksian tidak dapat ditawar: setiap versi yang dirilis harus dapat dibangun ulang dari masukan terkendali.
- Otomatiskan identifikasi, pencatatan, dan verifikasi; pembukuan manual tidak berskala dan tidak bertahan dari audit.

## Rekomendasi

### Definisikan proses SCM dan tetapkan kepemilikan

Tuliskan rencana SCM yang menyatakan apa yang berada di bawah kendali konfigurasi, bagaimana butir diidentifikasi, bagaimana perubahan diusulkan dan disetujui, dan bagaimana status dicatat dan diaudit. Tetapkan kepemilikan yang jelas, seperti manajer konfigurasi atau tim yang bertanggung jawab, agar SCM tidak menjadi tugas semua orang dan karenanya tugas tak seorang pun. Skalakan proses menurut risiko: perkakas internal kecil memerlukan kendali ringan, sementara sistem kritis keselamatan atau yang diatur memerlukan dewan dan catatan formal. Berlabuhlah pada standar yang diakui seperti IEEE 828 agar auditor dan mitra dapat mengikutinya.

### Identifikasi butir konfigurasi dan tetapkan baseline

Daftarkan butir konfigurasi yang menentukan bagaimana sistem berperilaku: sumber, dependensi, skrip build, citra kontainer, definisi infrastruktur, data konfigurasi, skema, dan dokumen kunci. Beri masing-masing pengenal yang stabil dan skema pembuatan versi. Tetapkan baseline pada titik yang bermakna (versi yang dirilis, set persyaratan yang disetujui, build tersertifikasi) agar Anda punya rujukan yang disepakati untuk berubah terhadapnya dan untuk kembali ke sana. Baseline bersifat tak berubah: begitu Anda menyatakannya, Anda tidak menyuntingnya. Anda hanya menggantikannya dengan baseline baru yang dibuat melalui proses perubahan.

### Kendalikan perubahan lewat proses terdefinisi dan dewan yang sesuai

Rutekan perubahan pada butir terkendali melalui jalur terdefinisi: usulan, penilaian dampak, persetujuan, implementasi, dan verifikasi. Untuk butir berisiko lebih tinggi, gunakan [dewan kendali perubahan](https://en.wikipedia.org/wiki/Change_control_board) (CCB) yang menimbang biaya, risiko, dan jadwal sebelum mengotorisasi perubahan. Sesuaikan ukuran dewan: gerbang otomatis ringan untuk perubahan kode rutin, dan CCB lintas fungsi formal untuk perubahan yang menyentuh baseline, antarmuka, atau perilaku yang diatur. Catat setiap keputusan dan alasan di baliknya, dan hubungkan keputusan konfigurasi penting dengan catatan keputusan (bab 1.6) agar alasannya bertahan.

### Pertahankan akuntansi status konfigurasi

Simpan catatan yang akurat dan dapat dikueri atas setiap butir konfigurasi: versinya saat ini, baseline mana yang dimilikinya, dan permintaan perubahan yang diterapkan padanya. Akuntansi status inilah yang memungkinkan Anda menjawab, kapan pun, apa yang dikandung rilis dan bagaimana ia sampai di sana. Hasilkan catatan secara otomatis dari perkakas pencatat Anda (kontrol versi, pipeline, registri artefak) alih-alih memelihara lembar kerja paralel yang menyimpang dari kenyataan. Catatan ini adalah tulang punggung keterlacakan dari persyaratan ke perubahan ke build ke deployment.

### Lakukan audit konfigurasi

Verifikasi dua hal secara berkala. Audit konfigurasi fungsional mengonfirmasi bahwa konfigurasi berkinerja seperti yang dispesifikasikan persyaratannya. Audit konfigurasi fisik mengonfirmasi bahwa artefak yang diserahkan cocok dengan konfigurasi tercatat: bahwa build berasal dari sumber dan dependensi tercatat dan tidak berisi apa pun yang tak terhitung. Otomatiskan sebanyak mungkin: [build yang dapat direproduksi](https://en.wikipedia.org/wiki/Reproducible_builds), checksum artefak, software bill of materials (SBOM), dan atestasi asal-usul mengubah audit dari inspeksi manual menjadi pemeriksaan berkelanjutan.

### Kelola rilis dan pengiriman sebagai peristiwa terkendali

Perlakukan rilis sebagai baseline spesifik yang teridentifikasi yang diserahkan lewat proses yang dapat diulang. Beri versi pada rilis Anda secara eksplisit, hasilkan manifes atau bill of materials yang menjelaskan persis apa yang termasuk, dan catat pemetaan dari rilis ke revisi sumber ke artefak yang di-deploy. Tanda tangani dan checksum artefak yang dirilis agar siapa pun di hilir dapat memverifikasi integritasnya. Kaitkan manajemen rilis dengan pipeline pengiriman (bab 8.1) agar promosi melalui lingkungan itu sendiri terkendali, tercatat, dan dapat dibalik.

### Pilih dan integrasikan perkakas SCM

Bersandarlah pada perkakas yang mengotomatiskan identifikasi, kendali, akuntansi, dan audit alih-alih mengandalkan disiplin saja: kontrol versi untuk sumber, registri artefak dan citra untuk biner, pipeline tak berubah untuk build, infrastruktur sebagai kode untuk lingkungan, dan perkakas dependensi serta SBOM untuk asal-usul. Hubungkan mereka agar satu perubahan mengalir secara dapat dilacak dari commit ke rilis yang di-deploy. Yang Anda kejar adalah toolchain di mana catatan konfigurasi adalah hasil sampingan mengerjakan pekerjaan, bukan tugas klerikal terpisah.

## Trade-off: kelebihan dan kekurangan

| Pilihan | Kelebihan | Kekurangan |
|---|---|---|
| Dewan kendali perubahan formal | Otorisasi dan jejak audit kuat; risiko ditimbang sebelum perubahan | Throughput lebih lambat; beban bila diterapkan pada perubahan rutin |
| Gerbang otomatis ringan | Aliran cepat; beban rendah; berskala ke banyak perubahan | Lebih lemah untuk baseline berisiko tinggi; kurang pertimbangan |
| Baseline tak berubah yang ketat | Titik rujukan yang dapat direproduksi dan diaudit | Perlu disiplin dan perkakas; gesekan bila berlebihan |
| Akuntansi status otomatis | Catatan akurat dan selalu mutakhir; siap audit | Investasi perkakas dan integrasi di muka |
| Catatan konfigurasi manual | Mudah dimulai; tanpa perkakas | Menyimpang dari kenyataan; gagal pada skala besar dan di bawah audit |

Trade-off pusatnya adalah kendali versus aliran. Kendali perubahan yang berat memberi jaminan kuat tetapi memperlambat pengiriman. Kendali ringan mengalir cepat tetapi melemahkan keterlacakan. Jawabannya bukan memilih satu secara global; melainkan menjenjang kendali menurut risiko: otomatiskan perubahan rutin lewat gerbang cepat, dan sisakan dewan formal serta baseline tak berubah untuk butir di mana otorisasi dan kemampuan diaudit benar-benar penting. Trade-off kedua adalah investasi perkakas di muka versus biaya klerikal berkelanjutan dan risiko audit. Akuntansi otomatis memakan biaya lebih untuk disiapkan dan jauh lebih sedikit untuk dijalani.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apa persisnya yang termasuk dalam daftar butir konfigurasi kita, dan siapa yang memiliki keputusan ketika sesuatu yang baru muncul?** SCM hanya berfungsi jika daftar butir terkendali cocok dengan kumpulan hal yang benar-benar menentukan perilaku, dan pada sistem besar kumpulan itu lebih besar daripada yang dikira kebanyakan tim: sumber, dependensi, skrip build, citra kontainer, definisi infrastruktur, skema, feature flag, dan data konfigurasi yang diam-diam mengubah apa yang dilakukan perangkat lunak. Jika tak seorang pun memiliki daftar, ia menjadi basi, dan butir yang menjatuhkan Anda di produksi ternyata satu-satunya hal yang tidak terpikir untuk dikendalikan. Bawa inventaris Anda saat ini ke rapat dan buru butir penentu perilaku yang hilang darinya. Tetapkan pemilik yang bertanggung jawab (manajer konfigurasi atau tim bernama) agar menambah butir baru adalah keputusan yang disengaja, bukan kecelakaan, karena SCM yang menjadi tugas semua orang adalah tugas tak seorang pun.

2. **Dapatkah kita membuktikan bahwa artefak yang di-deploy berasal dari sumber dan pipeline yang kita kira, dan akankah bukti itu bertahan dari pemalsuan?** Keterreproduksian dan keterlacakan adalah inti SCM, dan versi tajam pertanyaannya adalah apakah Anda dapat menautkan biner yang berjalan kembali ke commit dan eksekusi build tertentu dengan bukti, bukan pernyataan. Dalam sistem yang diatur atau bernilai tinggi ini juga pertahanan rantai pasok Anda: atestasi asal-usul bertanda tangan, checksum artefak, dan software bill of materials mengubah "kami cukup yakin" menjadi sesuatu yang dapat diverifikasi auditor atau penanggap insiden. Bawa rilis terakhir Anda dan coba telusuri mundur dari artefak yang di-deploy ke perubahan yang disetujui. Jika ada lompatan yang berupa klaim manual alih-alih tautan tercatat yang dapat diverifikasi, di situlah penyerang atau kesalahan jujur dapat menyelipkan sesuatu tanpa diketahui, dan menutupnya berarti memasang penandatanganan dan asal-usul ke pipeline agar catatan menjadi hasil sampingan pengiriman.

3. **Apakah ada yang dapat menyunting rilis di tempat hari ini, dan apa dampaknya terhadap kemampuan kita memercayainya?** Baseline hanya berguna jika tak berubah: begitu "rilis" dapat disunting setelah kejadian, Anda tidak dapat lagi mereproduksinya atau mengandalkannya sebagai rujukan, dan setiap audit hilir menjadi arkeologi. Kegagalan klasik adalah konfigurasi yang disunting langsung di produksi atau tag yang diam-diam dipindah, persis jalan pintas yang terasa tidak berbahaya dan membuat rilis mustahil direkonstruksi kelak. Bawa jawaban jujur ke rapat: siapa yang punya akses untuk mengubah baseline yang di-deploy tanpa melewati proses perubahan, dan apakah itu pernah terjadi? Perbaikannya adalah menjadikan baseline benar-benar tak berubah dan merutekan setiap perubahan melalui usulan, penilaian dampak, persetujuan, dan verifikasi, menjenjangkan ketelitian agar perubahan rutin mengalir lewat gerbang otomatis cepat sementara perubahan baseline dan yang diatur masuk ke dewan.

4. **Apakah akuntansi status konfigurasi kita dihasilkan otomatis dari perkakas pencatat kita, atau dipelihara dengan tangan, dan seberapa jauh ia telah menyimpang dari apa yang sebenarnya di-deploy?** Akuntansi status adalah catatan yang memungkinkan Anda menjawab, kapan pun, apa yang dikandung rilis dan bagaimana ia sampai di sana, dan pada sistem besar catatan itu hanya tepercaya jika ia jatuh dari pekerjaan alih-alih diketik ke lembar kerja paralel. Tarikan yang bersaing adalah bahwa register tulisan tangan terasa murah dimulai dan fleksibel, sementara mengotomatiskannya berarti mengintegrasikan kontrol versi, pipeline, dan registri artefak agar catatan menjadi hasil sampingan pengiriman. Bawa register yang Anda andalkan hari ini, pilih tiga rilis terbaru secara acak, dan periksa apakah versi, baseline, dan permintaan perubahan yang diterapkan yang tercatat cocok dengan apa yang dikatakan perkakas telah dirilis. Untuk program enterprise atau pemerintah, catatan status yang menyimpang dari kenyataan bukan soal kerapian, melainkan temuan audit yang menunggu terjadi, karena auditor yang menangkap satu celah berhenti memercayai seluruh penjelasan dan meminta Anda merekonstruksinya dengan tangan.

5. **Apakah kendali perubahan kita dijenjangkan menurut risiko, atau tingkat upacara yang sama mengatur setiap perubahan terlepas dari apa yang disentuhnya?** Kendali dan aliran saling menarik: dewan kendali perubahan formal menimbang biaya, risiko, dan jadwal sebelum mengotorisasi perubahan, tetapi menerapkan upacara itu pada penyesuaian kode rutin hanya menambah penundaan, sementara mendorong baseline bersama atau alur pembayaran yang diatur melalui gerbang otomatis cepat menghilangkan pertimbangan persis di tempat Anda membutuhkannya. Mode kegagalannya simetris, kekakuan seragam yang dipelajari orang untuk dihindari, atau kelonggaran seragam yang membiarkan perubahan berisiko tinggi lolos tanpa diperiksa. Bawa sampel perubahan kuartal lalu yang dipilah menurut apa yang disentuh masing-masing, dan periksa apakah ketelitian yang diterimanya benar-benar sepadan dengan risikonya. Dalam konteks yang diatur atau sektor publik, namai kelas butir mana yang harus mencapai dewan lintas fungsi dan mana yang boleh mengalir lewat gerbang otomatis, dan catat penjenjangan itu secara eksplisit, karena "kami memakai penilaian" bukan kontrol yang dapat diverifikasi auditor atau badan pengawas.

6. **Kapan terakhir kali kita menjalankan audit konfigurasi fungsional dan fisik, dan berapa banyak bukti yang akan berupa catatan hidup alih-alih rekonstruksi?** Audit konfigurasi fungsional mengonfirmasi sistem berkinerja seperti yang dispesifikasikan persyaratannya, dan audit konfigurasi fisik mengonfirmasi artefak yang diserahkan cocok dengan konfigurasi tercatat dan tidak berisi apa pun yang tak terhitung; lewatkan keduanya dan Anda memercayai bahwa baseline dan akuntansi status Anda jujur tanpa pernah memeriksanya. Ketegangannya adalah biaya: audit manual lambat dan menyakitkan, itulah mengapa tim menundanya, dan jalan keluarnya adalah mengotomatiskan pemeriksaan dengan build yang dapat direproduksi, checksum artefak, software bill of materials, dan atestasi asal-usul agar verifikasi menjadi berkelanjutan. Bawa rilis terbaru Anda dan coba hasilkan, seketika, jejak persyaratan-ke-perubahan-ke-build-ke-deployment dan bukti artefak-ke-sumber. Untuk program enterprise dan pemerintah, jejak bukti ini yang dituntut sertifikasi dan pengawasan, jadi pertanyaan jujurnya adalah apakah audit besok akan dijawab dari catatan yang sudah Anda pegang atau dari latihan arkeologi yang tidak sanggup Anda lakukan.

## Lensa sektor

**Startup.** Jaga SCM ringan tetapi nyata. Taruh sumber, definisi infrastruktur, dan data konfigurasi di kontrol versi, dan jadikan setiap rilis build bertag yang dihasilkan satu pipeline alih-alih artefak rakitan tangan. Lewati dewan kendali perubahan dan baseline formal, yang berlebihan pada ukuran Anda, tetapi jangan biarkan siapa pun menyunting konfigurasi langsung di produksi, karena satu jalan pintas itu yang membuat rilis mustahil direproduksi ketika pelanggan menemui bug Selasa depan.

**Bisnis kecil.** Tanpa manajer konfigurasi dan dengan anggaran ketat, bersandarlah pada perkakas yang memberi Anda SCM nyaris gratis: platform kontrol versi yang di-hosting, pipeline bawaannya, dan registri artefak, sehingga catatan konfigurasi adalah hasil sampingan alih-alih pekerjaan yang harus Anda isi stafnya. Beli kemampuan ini yang tertanam dalam perkakas yang sudah Anda bayar alih-alih membangun proses khusus. Belanjakan perhatian langka Anda pada dua kebiasaan yang paling penting, rilis bertag yang dapat direproduksi dan menjaga konfigurasi pengubah perilaku dari suntingan produksi manual.

**Enterprise.** Masalahnya adalah konsistensi di banyak tim: rencana SCM bersama, taksonomi butir konfigurasi umum, kendali perubahan berjenjang, dan akuntansi status yang dihasilkan otomatis dari kontrol versi, registri artefak, dan pipeline. Sisakan dewan kendali perubahan formal dan baseline tak berubah untuk platform bersama dan alur yang diatur, biarkan perubahan rutin mengalir lewat gerbang otomatis, dan bakukan asal-usul bertanda tangan serta SBOM agar rilis tim mana pun dapat dilacak dan auditor mana pun dapat mengkueri catatan hidup alih-alih meminta rekonstruksi.

**Pemerintah.** Aturan pengadaan, transparansi, dan akuntabilitas publik membentuk proses. Ikuti rencana SCM formal yang selaras dengan standar yang diakui seperti IEEE 828, baselinekan butir konfigurasi pada tonggak kontraktual, dan rutekan setiap perubahan ke baseline terkendali melalui dewan yang mencatat dampak, keputusan, dan alasan. Wajibkan artefak yang diserahkan dapat direproduksi dari masukan terkendali, di-checksum, dan dapat dilacak ujung ke ujung dari persyaratan yang disetujui ke build yang diserahkan, karena jejak bukti terdokumentasi itu persis yang dituntut sertifikasi, audit, dan pengawasan publik.

## Contoh

**Startup.** Sebuah startup enam orang menjaga SCM-nya ringan tetapi nyata: sumber, definisi infrastruktur, dan data konfigurasi semuanya berada di kontrol versi, dan setiap rilis adalah build bertag dan berversi yang dihasilkan pipeline yang sama alih-alih dirakit tangan. Ketika pelanggan melaporkan bug yang muncul Selasa lalu, mereka menelusuri artefak yang di-deploy kembali ke commit persisnya dalam hitungan menit alih-alih menebak. Mereka melewatkan dewan kendali perubahan dan baseline formal, yang berlebihan pada ukuran mereka, tetapi menolak membiarkan siapa pun menyunting konfigurasi langsung di produksi, karena satu jalan pintas itu yang membuat rilis mustahil direproduksi kelak.

**Enterprise.** Sebuah perusahaan jasa keuangan besar menempatkan semua artefak yang dapat di-deploy, definisi infrastruktur, dan data konfigurasi di bawah kendali konfigurasi. Setiap rilis adalah baseline tak berubah dan berversi dengan software bill of materials yang dihasilkan, dan setiap artefak yang di-deploy membawa atestasi asal-usul bertanda tangan yang menautkannya ke revisi sumber dan eksekusi pipeline tertentu. Perubahan aplikasi rutin mengalir lewat gerbang pipeline otomatis, sementara perubahan pada baseline platform bersama atau alur pembayaran yang diatur masuk ke dewan kendali perubahan. Akuntansi status dihasilkan otomatis dari kontrol versi, registri artefak, dan pipeline, sehingga auditor mengkueri catatan hidup alih-alih meminta rekonstruksi.

**Pemerintah.** Sebuah program pertahanan mengikuti rencana SCM formal yang selaras dengan IEEE 828. Butir konfigurasi didaftarkan dan di-baseline pada tonggak kontraktual, dan dewan kendali perubahan mengotorisasi setiap perubahan pada baseline terkendali, mencatat dampak, keputusan, dan alasan. Audit konfigurasi fungsional mengonfirmasi sistem yang diserahkan memenuhi persyaratan yang dispesifikasikan, dan audit konfigurasi fisik mengonfirmasi artefak yang diserahkan cocok persis dengan konfigurasi tercatat. Rilis dapat direproduksi dari masukan terkendali, di-checksum, dan dapat dilacak ujung ke ujung, dari persyaratan yang disetujui melalui permintaan perubahan ke build yang diserahkan, yaitu persis jejak bukti yang dituntut sertifikasi dan pengawasan.

## Kasus bisnis: motivasi, ROI, dan TCO

SCM ada untuk mengendalikan risiko dan biaya sepanjang umur sistem. Imbal hasilnya datang dari keterreproduksian dan keterlacakan: Anda dapat menciptakan ulang rilis apa pun, melacak cacat ke perubahan yang menyebabkannya, dan menjawab pertanyaan audit dari catatan alih-alih arkeologi. Itu menyusutkan waktu diagnosis insiden, mengurangi biaya dan panjang audit, dan mencegah kelas kegagalan mahal di mana tak seorang pun dapat mengatakan apa yang berjalan atau bagaimana membangunnya ulang.

Total biaya kepemilikan berpihak pada otomasi. Catatan konfigurasi manual murah dimulai dan terus mahal dipelihara, dan gagal persis ketika Anda paling membutuhkannya, selama insiden atau audit, karena telah menyimpang dari kenyataan. Identifikasi, akuntansi, dan audit otomatis memakan biaya lebih di muka tetapi mengubah catatan konfigurasi menjadi hasil sampingan hampir gratis dari pipeline pengiriman. Untuk meyakinkan pimpinan, bingkai SCM sebagai kontrol yang membuat rilis dapat direproduksi dan perubahan dapat diaudit, dan timbang terhadap biaya rilis yang tak dapat direproduksi, audit berkepanjangan, dan risiko kepatuhan dari perubahan tak terkendali.

## Anti-pola dan jebakan

- **Konfigurasi berdasarkan pengetahuan suku:** isi sebenarnya dari sebuah rilis hidup hanya di kepala insinyur, bukan di catatan mana pun.
- **Baseline yang dapat diubah:** "rilis" disunting di tempat, sehingga tidak lagi dapat direproduksi atau dipercaya sebagai rujukan.
- **Data konfigurasi tak terkendali:** kode berada di kontrol versi tetapi konfigurasi yang mengubah perilakunya disunting ad hoc di produksi.
- **Teater kendali perubahan:** dewan yang mencap karet segalanya, menambah penundaan tanpa menambah pengawasan nyata.
- **Akuntansi status manual:** lembar kerja versi yang diam-diam menyimpang dari apa yang sebenarnya di-deploy.
- **Build yang tak dapat direproduksi:** rilis yang tidak dapat dibangun ulang dari masukan terkendali, sehingga audit dan pembangunan ulang menjadi tebakan.
- **Rilis yang tak dapat dilacak:** tanpa pemetaan dari artefak yang di-deploy kembali ke revisi sumber, permintaan perubahan, dan persetujuan.

## Model kematangan

- **Tingkat 1 (Memulai):** SCM ad hoc dan reaktif. Hanya sumber yang dikendalikan; rilis dirakit tangan; tidak ada baseline, tidak ada catatan andal tentang apa yang di-deploy, dan tidak ada cara mereproduksi build masa lalu.
- **Tingkat 2 (Mengembangkan):** Praktik dasar ada tetapi bervariasi dari tim ke tim. Beberapa sistem mendefinisikan butir konfigurasi dan proses perubahan serta memberi versi pada rilis, baseline ada di sana-sini, tetapi catatan sebagian manual dan ketelitian kendali tidak konsisten di seluruh organisasi.
- **Tingkat 3 (Membakukan):** Praktik didokumentasikan dan ditegakkan di seluruh organisasi. Taksonomi butir konfigurasi umum, baseline tak berubah, kendali perubahan berjenjang, dan akuntansi status ditetapkan dan sebagian besar otomatis; rilis dapat direproduksi dan dilacak, dan audit didukung perkakas alih-alih ingatan.
- **Tingkat 4 (Mengelola):** SCM diukur dan dikendalikan dengan data. Tingkat keterreproduksian, cakupan keterlacakan dari persyaratan ke artefak yang di-deploy, lead time perubahan melalui setiap jenjang kendali, insiden penyimpangan konfigurasi, dan temuan audit dilacak terhadap garis dasar dan target. Penyimpangan memicu koreksi, dan setiap keputusan jalan atau tidak bertumpu pada bukti ini alih-alih pernyataan.
- **Tingkat 5 (Mengorkestrasi):** SCM terus diperbaiki dan terintegrasi di seluruh organisasi. Sepenuhnya otomatis dan terverifikasi terus-menerus dengan build yang dapat direproduksi, SBOM, atestasi asal-usul, dan akuntansi status hidup, proses dijalin ke dalam pengiriman, keamanan, dan audit, dan beradaptasi seiring bergesernya risiko dan hasil pengiriman, mengakhiri dan mengubah cakupan kontrol berdasarkan bukti.

## Gagasan untuk didiskusikan

- Dapatkah Anda mereproduksi rilis terakhir Anda persis dari masukan terkendali hari ini, dan berapa lama?
- Butir konfigurasi mana yang menentukan perilaku tetapi sebenarnya tidak berada di bawah kendali, terutama data konfigurasi dan infrastruktur?
- Apakah kendali perubahan Anda dijenjangkan menurut risiko, atau menambah beban seragam atau kelonggaran seragam di mana-mana?
- Di mana catatan konfigurasi Anda berada, dan seberapa jauh ia telah menyimpang dari apa yang sebenarnya di-deploy?
- Bukti apa yang dapat Anda hasilkan dalam audit besok, dan berapa banyak yang akan berupa rekonstruksi alih-alih catatan?
- Bagaimana build yang dapat direproduksi, SBOM, dan asal-usul mengubah apa yang dapat diverifikasi audit Anda secara otomatis?

## Poin-poin utama

- SCM mengendalikan seluruh konfigurasi (kode, dependensi, infrastruktur, dan data konfigurasi), bukan hanya sumber.
- Baseline adalah titik rujukan tak berubah; perubahan diotorisasi dan dicatat terhadapnya, bukan dicegah.
- Akuntansi status harus memungkinkan Anda menjawab, kapan pun, apa yang dikandung rilis dan bagaimana ia sampai di sana.
- Audit memverifikasi bahwa apa yang dibangun dan diserahkan cocok dengan konfigurasi tercatat dan persyaratan yang disetujui.
- Jenjangkan kendali menurut risiko dan otomatiskan identifikasi, akuntansi, dan audit agar catatan menjadi hasil sampingan pengiriman.

## Referensi dan bacaan lanjutan

- IEEE Computer Society, *SWEBOK Guide (Guide to the Software Engineering Body of Knowledge)*, area pengetahuan Software Configuration Management
- IEEE Std 828, *Standard for Configuration Management in Systems and Software Engineering*
- ISO/IEC/IEEE 12207, *Systems and software engineering: Software life cycle processes* (proses manajemen konfigurasi)
- Jez Humble dan David Farley, *Continuous Delivery*
- Bob Aiello dan Leslie Sachs, *Configuration Management Best Practices: Practical Methods that Work in the Real World*
- Panduan NIST tentang keamanan rantai pasok perangkat lunak, software bill of materials (SBOM), dan asal-usul artefak
- CNCF dan standar terbuka untuk asal-usul build dan atestasi (sebagai kerangka rujukan)
