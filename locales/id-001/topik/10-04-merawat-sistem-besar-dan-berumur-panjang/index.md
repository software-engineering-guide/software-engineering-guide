# 10.4 Merawat sistem besar dan berumur panjang

## Tinjauan dan motivasi

Sebagian besar tulisan tentang rekayasa perangkat lunak membahas membangun hal baru. Tetapi sebagian besar perangkat lunak penting dunia sudah tua, besar, dan masih berjalan: sistem pajak, pembayaran tunjangan, kontrol lalu lintas udara, perbankan inti, kontrol industri, dan infrastruktur kehidupan sehari-hari. Sistem ini rutin berjalan sepuluh, dua puluh, atau tiga puluh tahun. Itu jauh lebih lama daripada masa kerja siapa pun yang membangunnya, dan sering lebih lama daripada perusahaan dan bahasa yang menghasilkannya. Merawat sistem semacam itu berarti menjaganya andal, aman, dipahami, dan mampu berubah, lintas puluhan tahun dan lintas generasi staf. Ini salah satu disiplin tersulit dan paling tak glamor di bidang ini, dan di mana enterprise besar dan pemerintah memikul beban terberat.

Mengapa ini lebih penting bagi organisasi besar? Kesinambungan kewajiban. Startup dapat menulis ulang atau meninggalkan perangkat lunaknya. Pemerintah nasional tidak dapat berhenti membayar pensiun sementara ia me-refactor. Enterprise dan lembaga memiliki sistem yang kegagalannya berkonsekuensi diukur dalam mata pencarian, keselamatan, atau kepercayaan publik. Dan mereka memiliki banyak sekaligus, diisi staf yang bergabung dan pergi selama puluhan tahun. Ancaman sentralnya tidak eksotis. Ia adalah erosi lambat orang yang memahami sistem ([bus factor](https://en.wikipedia.org/wiki/Bus_factor), seberapa sedikit orang yang harus pergi sebelum pengetahuan sistem hilang), penumpukan pengetahuan tak terdokumentasi di beberapa kepala, pembusukan tumpukan teknologi menuju [akhir masa pakai](https://en.wikipedia.org/wiki/End-of-life_(product)), dan kelumpuhan yang menyerang ketika sistem menjadi terlalu kritis untuk disentuh dan terlalu kurang dipahami untuk diubah dengan aman.

Bab ini tentang kepengurusan: kerja yang disengaja dan tak glamor membantu sistem hidup lebih lama daripada penulisnya dengan anggun. Ia mencakup kesinambungan kepemilikan dan mitigasi bus factor, [deprekasi](https://en.wikipedia.org/wiki/Deprecation) terencana dan penghentian, transfer pengetahuan, tantangan khas sistem berumur puluhan tahun, dan aksi penyeimbangan konstan antara berinovasi dan menjaga stabilitas yang diandalkan warga dan pelanggan.

## Prinsip utama

- **Setiap sistem kritis butuh pemilik, selalu.** Kepemilikan adalah penugasan berkelanjutan, bukan ingatan tentang siapa yang menulisnya.
- **Pengetahuan yang hidup di satu kepala adalah risiko, bukan aset.** Lembagakan pemahaman sebelum orangnya pergi.
- **Membosankan adalah fitur.** Untuk sistem kritis berumur panjang, stabilitas dan keterprediksian sering mengungguli kebaruan.
- **Rencanakan akhir sejak awal.** Setiap sistem akan dipensiunkan atau diganti; rancang dan dokumentasikan untuk hari itu.
- **Perubahan adalah cara tetap aman.** Sistem yang terlalu menakutkan untuk disentuh sudah gagal; kemampuan berubah adalah sifat bertahan hidup.
- **Kesinambungan melampaui individu.** Rancang tim, dokumentasi, dan proses agar tak ada kepergian tunggal menjadi krisis.
- **Kepercayaan adalah produk sebenarnya.** Untuk sistem menghadap warga dan pelanggan, keandalan dan keadilan yang dipertahankan seiring waktu adalah misinya.

## Rekomendasi

### Tetapkan kepengurusan dan kesinambungan kepemilikan

Tetapkan kepemilikan eksplisit dan terkini untuk setiap sistem yang penting. Miliki di tingkat tim, bukan tingkat individu, agar kepemilikan selamat dari kepergian. Pelihara [katalog layanan](https://en.wikipedia.org/wiki/Service_catalog) yang mencatat, untuk setiap sistem, siapa yang memilikinya, apa yang dilakukannya, apa yang diandalkannya, dan seberapa kritis. Tinjau kepemilikan secara rutin, dan jangan pernah biarkan sistem menjadi yatim. Sistem kritis tak dimiliki adalah keadaan darurat yang menunggu terjadi. Ketika tim bereorganisasi, pindahkan kepemilikan dengan sengaja, dengan serah terima, bukan dengan asumsi. Untuk sistem berumur panjang paling kritis, pastikan kepemilikan mencakup bukan hanya operasi tetapi kemampuan memahami dan mengubah sistem, agar kepengurusan tidak merosot menjadi sekadar mengasuh.

### Mitigasi bus factor dan risiko orang kunci

Ukur dan kurangi konsentrasi pengetahuan secara aktif. Jika hanya satu orang yang dapat men-deploy, men-debug, atau mengubah sistem, itu [titik kegagalan tunggal](https://en.wikipedia.org/wiki/Single_point_of_failure) senyata perangkat keras mana pun. Kurangi lewat pairing dan rotasi, tinjauan kode wajib, on-call bersama, dan aturan sengaja bahwa tak ada tugas kritis yang hanya punya satu orang mampu. Latih silang agar setidaknya dua (lebih baik tiga) orang dapat menjalankan setiap fungsi esensial. Perlakukan kepergian orang kunci sebagai peristiwa yang dapat diperkirakan yang Anda persiapkan terus-menerus, bukan kejutan yang Anda serap. Dokumentasi membantu. Tetapi pengetahuan kerja yang tersebar di tim lewat praktik nyata jauh lebih tahan lama daripada dokumen yang tak pernah dilatih siapa pun.

### Lembagakan transfer pengetahuan

Tangkap pengetahuan yang kalau tidak akan pergi bersama orang. Fokus lebih dulu pada pengetahuan yang sulit direkonstruksi: mengapa keputusan dibuat, alternatif apa yang ditolak dan mengapa, di mana sisi tajam dan peretasan kritis yang diandalkan diam-diam oleh sisa sistem, dan bagaimana sistem berperilaku di bawah tekanan. Pakai architecture decision record untuk menjaga penalaran di balik pilihan, bukan hanya pilihannya. Simpan [runbook](https://en.wikipedia.org/wiki/Runbook) dan dokumentasi operasional dekat dengan sistem, dan latih secara teratur agar tetap benar. Bangun jalur onboarding yang membawa pengurus baru ke kompetensi sejati. Perlakukan kepergian sebagai peristiwa transfer pengetahuan dengan waktu serah terima nyata. Ingat bahwa [pengetahuan tacit](https://en.wikipedia.org/wiki/Tacit_knowledge), rasa terhadap sistem, berpindah terutama lewat mengerjakan bersama seseorang yang memilikinya, jadi tumpang tindihkan pengurus yang pergi dan yang tiba di mana Anda bisa.

### Kelola deprekasi, penghentian, dan akhir masa pakai

Rencanakan akhir dengan sengaja. Ketika Anda memutuskan untuk memensiunkan atau mengganti sistem, perlakukan penghentian sebagai proyek tersendiri: identifikasi setiap konsumen dan dependensi, sediakan jalur migrasi dan garis waktu realistis, komunikasikan jelas dan berulang, dan dukung konsumen melalui transisi. Hindari jebakan menjalankan sistem lama dan baru secara paralel selamanya karena tak ada yang mau melakukan kerja sulit mematikan yang lama. Tetapkan akuntabilitas eksplisit untuk menuntaskan dekomisioning. Pertahankan data, catatan, dan kemampuan menjawab pertanyaan tentang sistem yang dipensiunkan lama setelah ia berhenti berjalan, terutama di mana aturan retensi hukum berlaku. Penghentian yang dilakukan buruk meninggalkan sistem zombi yang tak dipelihara namun masih diandalkan: yang terburuk dari segalanya.

### Pertahankan sistem lintas puluhan tahun

Untuk sistem yang harus berjalan dua puluh atau tiga puluh tahun, rencanakan untuk hidup lebih lama daripada segalanya: tim asli, vendor, ekosistem bahasa, dan perangkat keras. Pilih [standar terbuka](https://en.wikipedia.org/wiki/Open_standard) dan antarmuka terdokumentasi daripada kotak hitam proprietari, agar pemelihara masa depan punya peluang. Modularisasi, agar bagian dapat diganti satu per satu alih-alih lewat [penulisan ulang](https://en.wikipedia.org/wiki/Rewrite_(programming)) semua-atau-tidak-sama-sekali yang terlalu berisiko untuk pernah dicoba. Jaga sistem terus dipelihara. Sistem yang dijaga mutakhir dalam langkah kecil tetap berkelanjutan. Sistem yang dibekukan "karena berfungsi" diam-diam menjadi tak dapat dipelihara seiring tumpukannya keluar dari dukungan. Jaga keterampilan untuk mengoperasikannya juga: untuk teknologi yang benar-benar tua, latih penerus dengan sengaja alih-alih berharap pakar terakhir tak pernah pensiun.

### Seimbangkan inovasi dengan stabilitas dan kepercayaan

Bedakan bagian properti Anda di mana kebaruan menciptakan nilai dari bagian di mana stabilitas adalah nilainya. Sistem inti yang diandalkan warga dan pelanggan setiap hari biasanya menghargai keandalan, kompatibilitas mundur, dan perubahan hati-hati daripada penulisan ulang yang mendebarkan. Investasikan inovasi di tepi (kanal baru, fitur baru, antarmuka baru) sambil menjaga inti tahan lama tetap stabil dan dipahami baik. Ubah inti, ya, tetapi dalam kenaikan kecil, dapat dibalik, dan teruji baik alih-alih lompatan heroik. Tujuannya sistem yang andal sekaligus mampu berevolusi: tak pernah begitu beku sehingga [membusuk](https://en.wikipedia.org/wiki/Software_rot), tak pernah begitu bergolak sehingga menjadi tak andal.

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan |
|---|---|---|
| Pertahankan dan pelihara sistem lama | Menjaga pengetahuan institusional; gangguan rendah; keandalan terbukti | Tumpukan menua; keterampilan langka; risiko mounting jika tak dipelihara |
| Penulisan ulang big-bang | Tumpukan segar; melepas kerak terakumulasi | Tingkat kegagalan sangat tinggi; kehilangan pengetahuan kasus tepi yang diperoleh susah payah |
| Modernisasi inkremental | Pengurangan risiko berkelanjutan; terus berjalan | Lambat; butuh pendanaan dan disiplin berkelanjutan |
| Transfer berat-dokumentasi | Catatan eksplisit dan dapat dicari | Membusuk jika tak dipelihara; melewatkan pengetahuan tacit |
| Transfer berbasis orang (pairing/rotasi) | Pengetahuan kerja tahan lama; tim tangguh | Memakan produktivitas saat ini; butuh penjadwalan sengaja |
| Bekukan inti kritis | Stabilitas maksimum jangka pendek | Tumpukan menua menjadi tak dapat dipelihara; tumbuh terlalu menakutkan untuk disentuh |

Trade-off penentu adalah stabilitas versus evolusi, dan resolusi naif keduanya gagal. Bekukan sistem kritis untuk melindunginya, dan Anda menjamin ia akhirnya menjadi tak dapat dipelihara dan tidak aman. Tulis ulang seluruhnya untuk memodernisasi, dan Anda mengundang tingkat kegagalan tinggi yang terkenal pada penggantian big-bang, dan Anda membuang puluhan tahun pengetahuan kasus tepi terkodekan yang tak diingat siapa pun ada. Jalan tahan lama adalah perubahan berkelanjutan dan inkremental: jaga sistem hidup dan bergerak dalam langkah kecil, agar ia tak pernah keluar dari dukungan dan tak pernah butuh lompatan menakutkan. Transfer pengetahuan adalah trade-off serupa, antara kemudahan dokumen dan ketahanan pengalaman yang dijalani. Jawabannya keduanya: pengetahuan hidup yang dipegang tim sebagai tulang punggung, dan dokumen sebagai rujukan.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Sistem kritis Anda yang mana tidak punya pemilik tim bernama saat ini?** Kepemilikan adalah penugasan berkelanjutan, bukan ingatan tentang siapa yang menulis kode, dan sistem kritis tak dimiliki adalah keadaan darurat yang menunggu terjadi, disadari hanya ketika rusak. Telusuri katalog layanan Anda (atau bangun satu) dan periksa bahwa setiap sistem mencatat siapa yang memilikinya, apa yang diandalkannya, dan seberapa kritis. Bawa bukti: pilih tiga sistem penting dan coba namai tim akuntabel serta kapan terakhir kepemilikan ditinjau. Di mana sistem yatim, atau di mana reorganisasi diam-diam menjatuhkannya, tetapkan kepemilikan dengan sengaja dengan serah terima nyata alih-alih asumsi. Pastikan kepemilikan mencakup kemampuan memahami dan mengubah sistem, agar kepengurusan tidak merosot menjadi sekadar mengasuh.

2. **Ketika Anda mengganti sistem, siapa yang akuntabel benar-benar mematikan yang lama?** Proses paralel abadi adalah kegagalan umum dan mahal: sistem lama dan baru berjalan berdampingan tanpa batas karena tak ada yang memiliki penghentian, meninggalkan Anda memelihara dua sistem dan mendapat keamanan dari keduanya tidak. Perlakukan setiap penghentian sebagai proyek terkelola dengan akuntabilitas bernama untuk menuntaskan dekomisioning, daftar konsumen terpetakan, jalur migrasi, dan garis waktu realistis. Bawa bukti: berapa banyak proses paralel "sementara" atau sistem setengah-dipensiunkan yang masih menyerap pemeliharaan di properti Anda hari ini? Pertahankan data dan catatan untuk memenuhi aturan retensi hukum lama setelah sistem berhenti berjalan, tetapi jangan biarkan retensi menjadi dalih tak pernah menyelesaikan. Penghentian yang dilakukan buruk meninggalkan sistem zombi yang tak dipelihara namun masih diandalkan, yang terburuk dari segalanya.

3. **Keterampilan untuk sistem berumur panjang Anda yang mana akan berhenti dipasok pasar tenaga kerja, dan apa rencana suksesi Anda?** Sistem yang berjalan dua puluh atau tiga puluh tahun hidup lebih lama daripada ekosistem bahasanya, vendornya, dan karier orang yang memahami tumpukan lama, dan pasar tidak akan secara andal menyerahkan pengganti. Kurangi bus factor dengan sengaja agar tak ada fungsi kritis yang hanya punya satu orang mampu, dan latih silang agar setidaknya dua, lebih baik tiga, orang dapat menjalankan setiap tugas esensial. Bawa bukti: untuk setiap sistem kritis yang menua, hitung berapa orang yang dapat mengubahnya dengan aman dan seberapa dekat yang paling berpengetahuan dengan pensiun. Jawabannya harus mendorong pelatihan penerus yang disengaja dan tumpang tindih nyata antara pengurus yang pergi dan yang tiba, karena pengetahuan tacit (rasa terhadap sistem) berpindah terutama dengan mengerjakan bersama seseorang yang memilikinya. Dokumen adalah rujukan; pengetahuan hidup yang dipegang tim adalah tulang punggung.

4. **Kapan terakhir Anda mengubah sistem berumur panjang paling kritis Anda, dan adakah yang masih berani?** Sistem yang tak disentuh siapa pun selama setahun bukan stabil, ia melayang menuju jebakan "terlalu menakutkan untuk disentuh," di mana setiap perubahan ditakuti sehingga tumpukan diam-diam keluar dari dukungan. Bagi organisasi besar ini penting karena kelumpuhan bertambah: makin lama pembekuan, makin pudar pengetahuan dan makin berisiko perubahan tak terhindarkan akhirnya. Bawa bukti: untuk setiap sistem kritis, tanggal perubahan sengaja terakhir, ukuran perubahan terkecil yang berani dicoba siapa pun hari ini, dan apakah dependensi rutin atau tambalan keamanan dapat dikirim minggu ini tanpa kepahlawanan. Pertimbangan yang bersaing nyata, karena perubahan juga memperkenalkan risiko, jadi tujuannya bukan gejolak tetapi irama stabil langkah kecil, dapat dibalik, dan teruji baik. Dalam properti enterprise dan pemerintah, di mana inti beku dapat duduk di bawah layanan warga selama satu dekade, perlakukan "kami tak pernah mengubahnya" sebagai bendera merah alih-alih jaminan, dan danai pemeliharaan berkelanjutan yang menjaga opsi untuk berubah tetap hidup.

5. **Seberapa banyak properti Anda berjalan pada teknologi yang di atau dekat akhir masa pakai, dan siapa yang melacak jam itu?** Runtime menua, basis data tak didukung, dan kerangka kerja di luar pemeliharaan adalah mode kegagalan lambat yang berubah menjadi krisis mendadak pada hari tambalan keamanan berhenti tiba. Bagi tim besar bahayanya adalah tak ada yang memiliki cakrawala: tim individual menambal apa yang rusak, tetapi tak ada yang memelihara pandangan portofolio tentang tumpukan mana kehilangan dukungan vendor dan kapan. Bawa bukti: inventaris teknologi inti setiap sistem kritis, tanggal akhir masa pakai atau akhir dukungan terbitannya, dan celah saat ini antara apa yang Anda jalankan dan apa yang masih didukung. Ketegangannya antara biaya peningkatan berkelanjutan dan risiko penundaan, dan penundaan biasanya menang sampai ia kalah secara katastrofik. Dalam pengaturan enterprise dan pemerintah, di mana siklus pengadaan dan akreditasi dapat memakan setahun atau lebih, tanggal akhir masa pakai yang tampak jauh sering sudah di dalam lead time Anda, sehingga kerja suksesi dan peningkatan harus mulai jauh sebelum jam habis.

6. **Di mana dalam properti Anda stabilitas adalah nilai dan kebaruan liabilitas, dan bagaimana Anda menjaga batas itu jujur?** Tidak semua sistem menghargai perlakuan sama: sistem inti yang diandalkan warga dan pelanggan setiap hari biasanya menghargai keandalan dan perubahan hati-hati, sementara tepi menghargai eksperimen, dan mencampuradukkan keduanya memboroskan uang atau mengundang pemadaman. Bagi organisasi besar risikonya adalah ambisi dan insentif karier mendorong penulisan ulang mendebarkan ke persis inti tahan lama yang seharusnya tetap membosankan. Bawa bukti: peta properti Anda yang menandai di mana keandalan adalah misi dan di mana kebaruan menciptakan nilai, plus perubahan terbaru yang melintasi garis itu di kedua arah dan biayanya. Pertimbangan yang bersaing adalah bahwa bahkan inti stabil harus tetap berevolusi, jadi "stabil" tak boleh menjadi dalih membeku. Dalam konteks enterprise dan pemerintah, kaitkan batas ini dengan tingkat kekritisan eksplisit dan otoritas bernama yang dapat memveto penulisan ulang berisiko atas sistem yang tak mampu dilihat publik gagal, agar penilaian tidak melayang mengikuti siapa pun yang paling lantang kuartal ini.

## Lensa sektor

**Startup.** Dengan segelintir insinyur dan sedikit runway, risiko pemeliharaan Anda terkonsentrasi pada satu atau dua orang yang menulis sistem yang tak sanggup Anda hilangkan, seperti penagihan atau autentikasi. Habiskan nyaris tak ada untuk proses, tetapi lakukan hal murah dan bernilai tinggi sekarang: pasangkan orang kedua melalui setiap sistem kritis, tulis architecture decision record satu halaman untuk bagian mengejutkan, dan simpan runbook yang benar-benar Anda pakai. Tahan dorongan menulis ulang sesuatu hanya karena tua, karena pada ukuran Anda penulisan ulang inti yang gagal dapat mengakhiri perusahaan.

**Bisnis kecil.** Anda tidak punya tim pemeliharaan khusus dan anggaran ketat, jadi pilih membeli dan menghosting daripada membangun apa pun yang harus Anda rawat sendiri. Pilih vendor dan standar terbuka yang memungkinkan Anda pergi, dan simpan catatan sederhana sistem luar mana menjalankan fungsi kritis mana dan siapa yang dihubungi ketika rusak. Di mana Anda memiliki kode kustom, pastikan setidaknya dua orang (atau kontraktor tepercaya plus satu karyawan) memahaminya, agar satu kepergian atau kontrak dukungan yang lapse tidak mendamparkan Anda.

**Enterprise.** Tantangan Anda skala portofolio: banyak sistem berumur panjang, banyak tim, dan staf yang berotasi selama puluhan tahun. Bakukan kepemilikan tingkat tim dalam katalog layanan, ukur bus factor di seluruh properti, dan danai modernisasi inkremental berkelanjutan alih-alih bertaruh pada penulisan ulang big-bang. Atur cakrawala akhir masa pakai secara terpusat agar tak ada tumpukan kritis yang diam-diam keluar dari dukungan, dan jalankan setiap penghentian sebagai proyek teraudit dengan akuntabilitas bernama untuk menuntaskan dekomisioning.

**Pemerintah.** Kesinambungan kewajiban absolut: Anda tak dapat berhenti membayar tunjangan atau menjalankan kontrol lalu lintas udara sementara me-refactor, dan kegagalan bersifat publik dan berkonsekuensi. Aturan pengadaan mendorong Anda ke standar terbuka, portabilitas data, dan antarmuka terdokumentasi agar pemelihara dan vendor masa depan punya peluang. Danai pelatihan suksesi sengaja untuk teknologi lebih tua yang tak lagi dipasok pasar tenaga kerja, pertahankan catatan sistem yang dipensiunkan untuk memenuhi retensi undang-undang, dan perlakukan keandalan layanan warga yang berkelanjutan sebagai misi akuntabel alih-alih overhead.

## Contoh

**Startup.** Startup lima orang sudah punya sistem yang tak sanggup dihilangkan: layanan penagihan yang ditulis satu pendiri pada bulan pertama dan kini menjalankan setiap tagihan pelanggan. Hanya pendiri itu yang memahaminya, jadi tim memperlakukan bus factor sebagai risiko nyata alih-alih pujian. Mereka memasangkan insinyur kedua melalui siklus penagihan penuh, menulis architecture decision record singkat yang menjelaskan mengapa logika retry yang aneh ada, dan menyimpan runbook di samping kode yang benar-benar mereka latih selama insiden. Mereka menolak menulis ulang hanya karena ia tua dan tak glamor, dan sebagai gantinya memperbaikinya dalam langkah kecil yang dapat dibalik, sehingga layanan yang menjaga perusahaan tetap hidup dipahami lebih dari satu kepala.

**Enterprise.** Sebuah perusahaan asuransi besar menjalankan sistem administrasi polis yang pertama kali ditulis puluhan tahun lalu dan masih sentral bagi bisnisnya. Alih-alih mencoba penulisan ulang menyeluruh yang berisiko, ia memodularisasi sistem di balik antarmuka terdefinisi baik dan kini mengganti satu komponen sekali waktu, setiap perubahan kecil dan dapat dibalik. Setiap fungsi kritis punya setidaknya tiga orang yang dapat menjalankannya. On-call dibagi. Architecture decision record menangkap mengapa sistem bekerja seperti itu. Kursus internal terkurasi membawa insinyur baru ke kompetensi pada tumpukan [warisan](https://en.wikipedia.org/wiki/Legacy_system), dan pakar yang pergi tumpang tindih dengan penerus agar pengetahuan tacit berpindah dengan mengerjakan.

**Pemerintah.** Sebuah lembaga jaminan sosial nasional mengoperasikan sistem pembayaran tunjangan yang telah berjalan lebih dari tiga puluh tahun dan tak boleh berhenti. Ia mencatat kepemilikan tim eksplisit dalam katalog layanan. Ia mendanai pemeliharaan berkelanjutan alih-alih membekukan sistem. Ia melatih penerus dalam teknologi lebih tua dengan sengaja, karena pasar tenaga kerja tidak akan memasoknya. Ketika ia memensiunkan subsistem usang, ia menjalankan penghentian sebagai proyek terkelola: memetakan setiap konsumen, menyediakan dukungan migrasi, mempertahankan catatan untuk memenuhi aturan retensi hukum, dan menetapkan akuntabilitas untuk benar-benar menuntaskan dekomisioning, sehingga tak ada sistem zombi yang tersisa.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil merawat sistem berumur panjang datang dari menghindari dua mode kegagalan katastrofik yang mendominasi [total biaya kepemilikan](https://en.wikipedia.org/wiki/Total_cost_of_ownership)-nya. Yang pertama krisis mendadak: orang kunci pergi, komponen tak didukung dibobol, atau sistem yatim gagal tanpa ada yang memahaminya. Yang kedua megaproyek yang gagal: penulisan ulang menyeluruh yang tergesa-gesa yang melebihi anggaran, kurang memberikan, atau runtuh. Keduanya sangat mahal, dan keduanya sebagian besar dapat dicegah oleh kepengurusan stabil. Biaya satu kegagalan penulisan ulang yang dihindari, atau satu pemadaman berkepanjangan layanan warga kritis yang dihindari, biasanya melampaui bertahun-tahun investasi pemeliharaan berkelanjutan.

Biaya adopsi berkelanjutan dan tak glamor: mendanai pemeliharaan yang tak menghasilkan fitur baru, membayar waktu pelatihan silang dan dokumentasi yang mengurangi keluaran jangka pendek, dan berinvestasi pada modernisasi inkremental yang tak pernah masuk berita utama. Biaya *tidak* mengadopsi tertunda dan lebih besar: risiko naik seiring tumpukan menua, paparan orang kunci membengkak, dan akhirnya penggantian paksa, berisiko tinggi, dan berbiaya tinggi di bawah kondisi darurat. Ketika Anda mengajukan kasus kepada pimpinan, bingkai ulang pemeliharaan dari "pusat biaya" menjadi "manajemen risiko untuk sistem yang tak sanggup dihilangkan organisasi." Sajikan total biaya kepemilikan di seluruh umur multidekade penuh (termasuk pemeliharaan dan dekomisioning akhirnya) alih-alih hanya pembangunan. Dan tekankan ini: untuk sistem menghadap warga dan pelanggan, keandalan berkelanjutan bukan overhead. Ia kepercayaan yang merupakan produk sebenarnya.

## Anti-pola dan jebakan

- **Pemelihara pahlawan.** Satu orang tak tergantikan yang memahami sistem; kepergiannya peristiwa eksistensial.
- **Bekukan dan lupakan.** Menyatakan sistem kritis "selesai," menghentikan pemeliharaan, dan menyaksikan tumpukannya menua menjadi tak dapat dipelihara.
- **Penulisan ulang yang ditakdirkan.** Mempertaruhkan organisasi pada penggantian menyeluruh yang membuang pengetahuan terkodekan dan biasanya melebihi anggaran atau gagal.
- **Sistem yatim.** Perangkat lunak kritis tanpa pemilik saat ini, disadari hanya ketika rusak.
- **Teater dokumentasi.** Volume dokumen yang usang, tak dilatih, dan tak dipercaya siapa pun.
- **Proses paralel abadi.** Sistem lama dan baru berjalan berdampingan tanpa batas karena tak ada yang akuntabel atas penghentian.
- **Kehilangan pengetahuan tacit.** Membiarkan pakar pergi tanpa tumpang tindih, sehingga rasa terhadap sistem menguap.
- **Terlalu menakutkan untuk disentuh.** Sistem yang begitu kurang dipahami sehingga perubahan apa pun ditakuti, yang menjamin ia membusuk.

## Model kematangan

**Tingkat 1: Memulai.** Pemeliharaan ad hoc dan reaktif. Sistem bergantung pada pahlawan individual, kepemilikan diingat alih-alih ditetapkan, dan pengetahuan hidup tak terdokumentasi di beberapa kepala. Sistem lama dibekukan sampai rusak, tumpukan menua melayang ke akhir masa pakai tanpa disadari, dan pemensiunan diumumkan tetapi tak pernah dituntaskan.

**Tingkat 2: Mengembangkan.** Praktik dasar muncul tetapi bervariasi tim demi tim. Kepemilikan dituliskan untuk sistem utama yang paling jelas, sebagian runbook dan dokumentasi ada, dan beberapa fungsi kritis punya orang mampu kedua. Pemeliharaan didanai tetapi reaktif, pelatihan silang terjadi ketika seseorang ingat, dan tak ada cara bersama mengerjakan semuanya di seluruh organisasi.

**Tingkat 3: Membakukan.** Praktik kepengurusan didokumentasikan dan ditegakkan di seluruh organisasi. Kepemilikan tingkat tim dicatat dalam katalog layanan dan selamat dari reorganisasi. Mitigasi bus factor lewat rotasi dan pelatihan silang adalah aturan tetap, architecture decision record dan runbook yang dilatih diharapkan, modernisasi inkremental menurut kebijakan, dan setiap penghentian berjalan sebagai proyek terkelola dengan akuntabilitas bernama untuk menuntaskan dekomisioning.

**Tingkat 4: Mengelola.** Pemeliharaan diukur dan dikendalikan dengan data terhadap garis dasar. Anda melacak bus factor per sistem kritis, jumlah orang yang dapat mengubah masing-masing dengan aman, usia setiap teknologi inti terhadap tanggal akhir masa pakainya, pangsa properti di bawah pemeliharaan berkelanjutan versus tertunda, dan jumlah proses paralel macet dan dekomisioning setengah selesai. Metrik ini membawa ambang yang memicu tindakan: sistem yang jatuh di bawah lantai bus factor atau melintasi cakrawala akhir dukungan mendapat remediasi terdanai, dan kesehatan kepengurusan dilaporkan kepada pimpinan di samping pengiriman.

**Tingkat 5: Mengorkestrasi.** Kepengurusan terus diperbaiki dan terintegrasi di seluruh organisasi. Tak ada sistem kritis yang menjadi titik kegagalan manusia tunggal, transfer pengetahuan termasuk pengetahuan tacit lewat tumpang tindih adalah rutin, dan sistem berevolusi dalam langkah kecil yang dapat dibalik sehingga tak ada yang menua keluar dari dukungan. Kepemilikan, pelacakan akhir masa pakai, suksesi, dan perencanaan penghentian dijalin ke perencanaan portofolio dan risiko, properti diseimbangkan ulang seiring teknologi dan kewajiban bergeser, dan sistem multidekade dipertahankan sambil menjaga kepercayaan orang yang bergantung padanya.

## Gagasan untuk didiskusikan

- Bagaimana Anda mengukur bus factor secara bermakna, dan target mana yang tepat untuk tingkat kekritisan berbeda?
- Kapan modernisasi inkremental benar-benar tak layak, menjadikan penulisan ulang risiko yang lebih kecil?
- Bagaimana Anda mendanai dan menghargai kerja pemeliharaan agar kepengurusan menjadi jalur karier yang dihormati, bukan jalan buntu?
- Apa cara yang tepat mempertahankan pengetahuan tacit ketika pakar terakhir akan pensiun dan tumpang tindih tak mungkin?
- Berapa lama Anda harus mempertahankan kemampuan menjawab pertanyaan tentang sistem yang dipensiunkan, dan siapa yang membayarnya?
- Di mana dalam properti Anda stabilitas adalah nilai dan kebaruan liabilitas, dan bagaimana Anda menjaga penilaian itu jujur seiring waktu?

## Poin-poin utama

- Sebagian besar perangkat lunak penting sudah tua dan berumur panjang; merawatnya lintas puluhan tahun dan generasi staf adalah disiplin kelas satu.
- Setiap sistem kritis butuh kepemilikan tingkat tim yang terkini; sistem kritis yatim adalah keadaan darurat laten.
- Kurangi bus factor dengan sengaja (tak ada tugas kritis yang hanya punya satu orang mampu) dan transfer pengetahuan tacit lewat tumpang tindih, bukan hanya dokumen.
- Jaga sistem berumur panjang dipelihara secara berkelanjutan dan inkremental; membekukannya dan bertaruh pada penulisan ulang menyeluruh sama-sama mode kegagalan.
- Rencanakan akhir sebagai proyek terkelola dengan penuntasan akuntabel, mempertahankan data dan catatan untuk memenuhi kewajiban.
- Untuk sistem menghadap warga dan pelanggan, keandalan dan keadilan berkelanjutan adalah misi, dan pemeliharaan adalah manajemen risiko untuk apa yang tak sanggup Anda hilangkan.

## Referensi dan bacaan lanjutan

- Michael Feathers, *Working Effectively with Legacy Code*
- Titus Winters, Tom Manshreck, dan Hyrum Wright, *Software Engineering at Google*
- Frederick P. Brooks Jr., *The Mythical Man-Month*
- Nat Pryce dan Steve Freeman, *Growing Object-Oriented Software, Guided by Tests*
- Sam Newman, *Monolith to Microservices*
- Martin Fowler, *Refactoring* dan tulisan tentang pola Strangler Fig
- Betsy Beyer et al., *Site Reliability Engineering* dan *The Site Reliability Workbook* (Google)
- Diomidis Spinellis, *Code Reading: The Open Source Perspective*
- U.S. Government Accountability Office, laporan tentang modernisasi TI warisan federal
