# 5.3 Aksesibilitas

## Tinjauan dan motivasi

[Aksesibilitas](https://en.wikipedia.org/wiki/Accessibility) (sering disingkat "a11y") adalah praktik membangun perangkat lunak yang dapat dipersepsi, dipahami, dinavigasi, dan dipakai penyandang disabilitas. Itu mencakup orang yang buta atau berpenglihatan rendah, yang tuli atau kurang dengar, yang punya gangguan motorik, yang punya perbedaan kognitif atau belajar, dan yang menghadapi batasan sementara atau situasional seperti lengan patah, sinar matahari terang, atau ruangan bising. Kira-kira satu dari lima orang memiliki disabilitas, dan semua orang diuntungkan desain yang dapat diakses pada suatu saat. Ini bukan akomodasi niche. Ia garis dasar kualitas.

Bagi tim besar, aksesibilitas harus dibangun ke dalam sistem, tidak diserahkan pada niat baik individu. Ketika banyak tim merilis ke satu produk, satu komponen yang tak dapat diakses (bidang formulir tanpa label, indikator status hanya-warna, jebakan keyboard dalam modal) dapat mengunci pengguna disabilitas keluar dari seluruh perjalanan. Membangun aksesibilitas ke dalam komponen bersama, token desain, pipeline pengujian, dan definisi selesai adalah satu-satunya cara membuatnya andal pada skala besar. Memasangnya belakangan mahal dan rawan galat. Merancangnya masuk murah dan tahan lama.

Bagi pemerintah, aksesibilitas adalah persyaratan hukum dan kewajiban sipil, bukan sekadar bagus untuk dimiliki. Layanan publik harus melayani setiap anggota publik, dan warga disabilitas sering tak punya penyedia alternatif: jika situs web pemerintah tak dapat diakses, mereka tidak dapat memperoleh tunjangan, izin, atau suara mereka dengan cara lain. Undang-undang dan standar di seluruh dunia menjadikan aksesibilitas wajib bagi badan publik, dan makin bagi sektor swasta. Bab ini memperlakukan aksesibilitas sebagai tiga hal sekaligus: kewajiban hukum, kewajiban etis, dan sekadar desain yang baik.

*Lihat juga:* bab 5.2 (desain UI dan sistem desain), bab 5.6 (rekayasa frontend), dan bab 5.1 (fondasi UX).

## Prinsip utama

- Aksesibilitas adalah atribut kualitas garis dasar, seperti keamanan dan kinerja, bukan fitur opsional.
- Prinsip POUR: antarmuka harus Perceivable (dapat dipersepsi), Operable (dapat dioperasikan), Understandable (dapat dipahami), dan Robust (kokoh).
- [HTML semantik](https://en.wikipedia.org/wiki/Semantic_HTML) lebih dulu; gunakan [ARIA](https://en.wikipedia.org/wiki/WAI-ARIA) hanya untuk mengisi celah sejati, tidak pernah sebagai pengganti elemen bawaan.
- Segala yang dapat dipakai dengan mouse harus dapat dipakai dengan keyboard saja.
- Jangan menyampaikan informasi hanya lewat warna, bentuk, atau posisi.
- Perkakas otomatis hanya menangkap sebagian isu; pengujian manual dan [teknologi bantu](https://en.wikipedia.org/wiki/Assistive_technology) esensial.
- Desain yang dapat diakses adalah desain lebih baik untuk semua orang (["efek curb-cut,"](https://en.wikipedia.org/wiki/Curb_cut) di mana fitur yang dibangun untuk penyandang disabilitas menguntungkan semua pengguna).
- Rancang dan uji bersama penyandang disabilitas, bukan hanya untuk mereka.

## Rekomendasi

### Rancang dan bangun menurut WCAG, menargetkan standar terkini

[Web Content Accessibility Guidelines](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) adalah rujukan internasional. WCAG 2.1 dan 2.2 diorganisasi di bawah empat prinsip POUR, dengan kriteria keberhasilan yang dapat diuji pada tingkat kesesuaian A, AA, dan AAA. Targetkan Tingkat AA sebagai garis dasar Anda; itu yang dirujuk sebagian besar undang-undang. WCAG 2.2 menambah kriteria untuk visibilitas fokus, ukuran target, dan pengurangan beban kognitif. WCAG 3.0 adalah penerus yang muncul, distrukturkan berbeda dan masih dikembangkan. Awasi, tetapi bangun ke 2.2 AA hari ini. Perlakukan pedoman sebagai lantai, bukan langit-langit: lulus setiap kriteria tidak menjamin pengalaman yang benar-benar dapat dipakai.

### Gunakan HTML semantik dan ARIA yang benar

Elemen HTML bawaan (tombol, tautan, kontrol formulir, judul, daftar, landmark) datang dengan semantik aksesibilitas bawaan, perilaku keyboard, dan dukungan teknologi bantu. Gunakan itu lebih dulu. Raih peran, keadaan, dan properti ARIA (Accessible Rich Internet Applications) hanya untuk mendeskripsikan widget khusus yang tak dapat diekspresikan HTML, dan ikuti ARIA Authoring Practices. Aturan pertama ARIA sederhana: jangan pakai ARIA jika elemen bawaan sudah cukup. ARIA yang salah lebih buruk daripada tidak ada: ia aktif menyesatkan [pembaca layar](https://en.wikipedia.org/wiki/Screen_reader). Beri halaman struktur judul logis, label bermakna, teks alternatif untuk gambar, teks keterangan dan transkrip untuk media, dan tautan terprogram antara setiap label dan kontrolnya.

### Jamin keterioperasian keyboard dan teknologi bantu

Setiap elemen interaktif harus dapat dijangkau dan dioperasikan dengan keyboard saja, dalam urutan logis, dengan indikator fokus yang terlihat jelas. Hindari jebakan keyboard. Kelola fokus dengan sengaja ketika konten berubah: pindahkan fokus ke dialog saat terbuka, kembalikan saat dialog menutup, dan umumkan pembaruan dinamis lewat live region. Uji dengan teknologi bantu nyata, termasuk pembaca layar di desktop dan seluler, pembesaran layar, kendali suara, dan akses sakelar. Dan hormati preferensi pengguna seperti gerak berkurang dan kontras meningkat.

### Uji dengan perkakas otomatis, tinjauan manual, dan pengguna nyata

Pemindai aksesibilitas otomatis berharga, dan harus berjalan dalam pipeline pada setiap perubahan. Tetapi studi secara konsisten menunjukkan mereka hanya menangkap minoritas isu nyata, kira-kira sepertiga. Sisanya butuh penilaian manusia: penelusuran keyboard, pengujian pembaca layar, pemeriksaan kontras, dan bertanya apakah konten benar-benar dapat dipahami. Yang paling penting, sertakan penyandang disabilitas dalam uji kegunaan. Bangun kriteria penerimaan aksesibilitas ke definisi selesai, agar isu tertangkap per story alih-alih dalam audit pra-peluncuran.

### Jadikan aksesibilitas organisasional, bukan heroik

Tanamkan aksesibilitas ke dalam sistem desain agar komponen dikirim dapat diakses secara bawaan. Tawarkan pelatihan agar desainer, insinyur, penulis konten, dan manajer produk masing-masing tahu apa tanggung jawab mereka. Tetapkan standar aksesibilitas, pemilik atau pusat keunggulan, dan proses remediasi. Terbitkan pernyataan aksesibilitas dan beri pengguna cara melaporkan hambatan. Dan lakukan pengadaan secara dapat diakses: wajibkan vendor dan komponen pihak ketiga memenuhi, dan menyediakan bukti (seperti laporan kesesuaian aksesibilitas).

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan |
|---|---|---|
| Bangun aksesibilitas sejak awal | Termurah, tahan lama, lebih baik untuk semua orang | Membutuhkan pelatihan dan disiplin di muka |
| Pasang / perbaiki belakangan | Menunda upaya, membuka peluncuran cepat | Jauh lebih mahal, rapuh, paparan hukum selama jeda |
| Hanya pengujian otomatis | Cepat, murah, menangkap regresi di CI | Melewatkan ~dua pertiga isu; keyakinan palsu |
| Pengujian manual + teknologi bantu | Menangkap hambatan kegunaan nyata | Lebih lambat, butuh penguji dan perangkat terampil |
| Pengujian dengan pengguna disabilitas | Kebenaran lapangan tentang pengalaman nyata | Upaya dan biaya perekrutan, harus dilakukan dengan hormat |

Trade-off pusatnya adalah disiplin di muka versus biaya yang ditunda. Aksesibilitas yang dibangun masuk murah dan memperbaiki kualitas untuk semua orang; aksesibilitas yang dipasang belakangan di bawah tekanan hukum mahal, tidak lengkap, dan penuh tekanan. Dalam jangka panjang tidak ada trade-off nyata terhadap "kecepatan": perangkat lunak yang tak dapat diakses sekadar tidak berfungsi bagi seperlima pengguna Anda. Itu cacat, bukan penghematan.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apakah regresi aksesibilitas menggagalkan build kita seperti tes rusak, dan jika tidak, mengapa?** Pemindai otomatis hanya menangkap sekitar sepertiga isu, tetapi yang mereka tangkap (label hilang, kegagalan kontras, kontrol tanpa label) murah ditangkap di CI dan mahal ditemukan dalam audit pra-peluncuran. Memperlakukan regresi sebagai kegagalan build adalah yang memindahkan aksesibilitas dari upaya individu heroik ke properti sistem yang andal, satu-satunya yang berfungsi ketika banyak tim merilis ke satu produk. Putuskan pemeriksaan mana yang memblokir, mana yang bersifat nasihat, dan siapa yang dapat menimpa kegagalan. Bawa hasil pemindai dan definisi selesai Anda saat ini ke rapat. Jika kriteria aksesibilitas tidak tertulis dalam definisi selesai per story, ia akan dikesampingkan begitu tenggat mengetat.

2. **Apa aturan kita untuk widget khusus, dan siapa yang meninjau ARIA sebelum dikirim?** Elemen HTML bawaan datang dengan perilaku keyboard dan dukungan teknologi bantu secara gratis, dan ARIA yang salah lebih buruk daripada tidak ada karena aktif menyesatkan pembaca layar. Sepakati bahwa HTML semantik adalah bawaan dan bahwa widget khusus apa pun (dropdown, pemilih tanggal, atau modal pesanan) memerlukan penelusuran keyboard dan pembaca layar sebelum penggabungan, mengikuti ARIA Authoring Practices. Ini paling penting untuk komponen interaktif yang dipakai ulang banyak tim, karena satu modal rusak dengan jebakan keyboard dapat mengunci pengguna disabilitas keluar dari seluruh perjalanan. Bawa daftar widget khusus Anda dan tanyakan mana yang telah diuji dengan pembaca layar sungguhan. Yang belum adalah liabilitas yang bersembunyi di kode bersama.

3. **Apa kebijakan kita tentang overlay aksesibilitas, dan adakah yang percaya itu perbaikan nyata?** Overlay dipasarkan sebagai skrip satu baris yang membuat situs sesuai, dan menggoda ketika tekanan hukum tiba dan tenggat mendekat. Mereka tidak memberi kesesuaian sejati, dapat memperburuk pengalaman pengguna teknologi bantu, dan bagi pemerintah mereka membiarkan kewajiban hukum mendasar tak terpenuhi. Putuskan secara eksplisit bahwa Anda akan berinvestasi pada markup semantik, dukungan keyboard, dan pengujian dengan penyandang disabilitas alih-alih membeli widget yang menutupi masalah. Bawa biaya langganan overlay dan bandingkan dengan membangun aksesibilitas ke komponen dan pipeline Anda sekali. Membingkai ini lebih awal mencegah keputusan pengadaan panik kelak yang membelanjakan uang dan tak memperbaiki apa-apa.

4. **Apakah penyandang disabilitas bagian dari desain dan pengujian kita, atau kita masih merancang untuk pengguna khayalan yang kita ciptakan?** Pemindai otomatis dan bahkan audit ahli memberi tahu apakah markup sesuai; mereka tidak memberi tahu apakah pengguna buta benar-benar dapat menyelesaikan checkout Anda atau orang dengan disabilitas kognitif dapat memahami pesan galat Anda. Melibatkan peserta disabilitas adalah satu-satunya sumber kebenaran lapangan, dan ia mengubah apa yang Anda bangun, tetapi ia menimbulkan pertanyaan nyata tentang bagaimana merekrut secara adil, bagaimana mengompensasi waktu orang, dan bagaimana menghindari memperlakukan satu peserta sebagai juru bicara untuk setiap disabilitas. Bawa daftar riset Anda saat ini, praktik perekrutan dan pembayaran Anda, dan hitungan jujur berapa studi dalam setahun terakhir yang menyertakan peserta disabilitas. Bagi organisasi besar, panel berulang dengan kompensasi adil dan cakupan lintas kebutuhan penglihatan, pendengaran, motorik, dan kognitif mengubah ini dari isyarat sekali jalan menjadi masukan yang dapat diandalkan; di pemerintah, melibatkan publik yang dilayani sering bagian kewajiban hukum dan sipil, bukan basa-basi opsional.

5. **Ketika kita membeli atau menyematkan komponen pihak ketiga, apakah kita mewajibkan bukti aksesibilitas, dan siapa yang memeriksanya?** Banyak dari apa yang dikirim dalam produk besar tidak ditulis internal: pemilih tanggal dari pustaka, widget pembayaran dalam iframe, paket bagan, seluruh modul SaaS. Satu komponen tersemat yang tak dapat diakses dapat menggagalkan seluruh perjalanan betapa pun bersih kode Anda sendiri, dan begitu terpasang, menggantinya mahal. Putuskan bahwa aksesibilitas adalah persyaratan pengadaan, bahwa vendor harus menyediakan laporan kesesuaian aksesibilitas (dokumen seperti VPAT yang menyatakan bagaimana produk terukur terhadap WCAG), dan bahwa seseorang yang teknis memvalidasi klaim itu alih-alih mengarsipkannya. Bawa inventaris komponen pihak ketiga Anda dan tanyakan mana yang punya bukti kesesuaian terkini dan kredibel. Dalam pembelian enterprise dan pemerintah, tulis kesesuaian WCAG 2.2 AA dan hak remediasi ke kontrak, karena janji yang dibuat sebelum menandatangani jauh lebih murah ditegakkan daripada hambatan yang ditemukan setelah go-live.

6. **Apa tingkat kesesuaian target kita, siapa yang memilikinya, dan bagaimana kita menjaganya tetap mutakhir saat standar bergerak?** WCAG 2.2 AA adalah lantai hari ini dan sebagian besar undang-undang merujuknya, tetapi 2.2 menambah kriteria yang belum diadopsi banyak tim, dan WCAG 3.0 akan datang dengan struktur berbeda. Tanpa pemilik bernama, standar menyimpang: tim berbeda menargetkan versi berbeda, tak ada yang melacak celah, dan kesesuaian diam-diam membusuk di antara audit. Putuskan versi dan tingkat persisnya yang Anda bangun, siapa yang berwenang menaikkannya, dan bagaimana kriteria baru mencapai sistem desain dan definisi selesai. Bawa target yang dinyatakan saat ini, bukti di mana tim benar-benar memenuhinya, dan peta jalan singkat untuk mengadopsi kriteria 2.2 yang Anda lewati. Untuk organisasi besar atau publik, pemilik atau pusat keunggulan aksesibilitas, pernyataan aksesibilitas yang diterbitkan, dan rencana terdokumentasi untuk versi standar berikutnya adalah yang memungkinkan Anda menjawab regulator atau pengadilan dengan bukti alih-alih niat baik.

## Lensa sektor

**Startup.** Kecepatan menguntungkan Anda di sini, karena aksesibilitas termurah ketika basis kode kecil. Tambahkan pemindai otomatis ke CI dan penelusuran keyboard ke daftar periksa pull request Anda sejak sprint pertama, dan bersandarlah pada HTML semantik agar Anda mendapat dukungan keyboard dan pembaca layar gratis. Lewati overlay dan perkakas berat; imbalannya ketika tim pengadaan pelanggan meminta laporan kesesuaian di tengah penjualan, Anda dapat menjawab dalam hari alih-alih kalang kabut.

**Bisnis kecil.** Tanpa spesialis aksesibilitas dan dengan anggaran ketat, beli aksesibilitas alih-alih bangun: pilih platform, tema, atau pustaka komponen yang sudah sesuai dan menyatakannya, dan pilih vendor yang menerbitkan pernyataan aksesibilitas. Tutup dasar bernilai tinggi sendiri dengan perkakas gratis, pemeriksaan hanya-keyboard, pemeriksa kontras, dan label jelas pada setiap bidang, karena itu menangkap kegagalan yang paling sering mengecualikan pelanggan. Perlakukan alur otomatis yang salah atau tak dapat dipakai sebagai pelanggan hilang, karena bisnis kecil jarang menawarkan kanal berbantuan sebagai cadangan.

**Enterprise.** Pada skala besar pekerjaannya menjadikan aksesibilitas properti sistem lintas banyak tim. Kirim komponen yang dapat diakses secara bawaan dalam sistem desain, gerbangi regresi di CI, dan dirikan pemilik atau pusat keunggulan dengan proses remediasi dan pelatihan untuk desainer, insinyur, dan penulis konten. Lacak kesesuaian seiring waktu sebagai metrik, tulis kesesuaian WCAG ke pengadaan, dan kelola komponen pihak ketiga sebagai portofolio agar satu widget tersemat tidak dapat diam-diam menggagalkan perjalanan bersama.

**Pemerintah.** Aksesibilitas adalah mandat hukum dan kewajiban sipil, karena warga disabilitas sering tak punya penyedia alternatif untuk tunjangan, izin, atau suara. Bangun ke standar yang dikutip yurisdiksi Anda (misalnya Section 508, EN 301 549, atau European Accessibility Act yang dipetakan ke WCAG 2.2 AA), terbitkan pernyataan aksesibilitas dengan jalur melaporkan hambatan, dan uji dengan publik disabilitas yang Anda layani. Tolak overlay sebagai pengganti kesesuaian nyata, dan wajibkan vendor menyediakan bukti kredibel dan hak remediasi dalam kontrak.

## Contoh

**Startup.** Startup tiga orang yang membangun perkakas perekrutan menambahkan pemindai aksesibilitas ke build mereka dan penelusuran keyboard cepat ke daftar periksa pull request mereka sejak sprint pertama, beralasan lebih murah tetap dapat diakses daripada memperbaikinya belakangan. Ketika tim pengadaan pelanggan menengah meminta laporan kesesuaian aksesibilitas selama siklus penjualan, startup sudah memakai HTML semantik, melabeli setiap bidang, dan punya fokus terlihat di mana-mana, sehingga mereka menjawab dalam hari alih-alih kalang kabut. Kesiapan itu memenangkan kesepakatan yang dikalahkan pesaing pada persyaratan yang sama.

**Enterprise.** Sebuah pengecer besar menghadapi gugatan kelompok karena pelanggan buta tak dapat menyelesaikan checkout dengan pembaca layar. Di luar penyelesaian dan biaya hukum, perusahaan harus melakukan remediasi di bawah garis waktu yang diawasi pengadilan. Sesudahnya ia membangun ulang aksesibilitas ke sistem desain dan pipeline CI-nya, menambahkan pengujian pembaca layar ke definisi selesai, dan melatih timnya. Checkout yang dibangun ulang dan dapat diakses juga memperbaiki konversi dan mengurangi kontak dukungan untuk semua orang: perbaikan yang membantu pengguna pembaca layar (label jelas, pesan galat, urutan logis) membantu semua pengguna.

**Pemerintah.** Sebuah lembaga tunjangan publik secara hukum wajib memenuhi WCAG 2.1 AA untuk aplikasi daringnya. Pengujian awal dengan pengguna buta dan berpenglihatan rendah, pengguna hanya-keyboard, dan pengguna dengan disabilitas kognitif mengungkap bahwa indikator "bidang wajib" hanya-warna, pemilih tanggal yang tak dapat diakses, dan galat validasi yang tak diumumkan memblokir orang menyelesaikan. Memperbaikinya, lewat markup semantik, fokus terlihat, pengumuman galat live-region, dan bantuan [bahasa sederhana](https://en.wikipedia.org/wiki/Plain_language), memungkinkan warga disabilitas mengajukan sendiri untuk pertama kalinya. Itu mengurangi ketergantungan pada bantuan tatap muka dan menurunkan biaya melayani, sambil memenuhi mandat hukum.

## Kasus bisnis: motivasi, ROI, dan TCO

Kasus bisnis bertumpu pada jangkauan pasar, risiko hukum, biaya melayani, dan kualitas. Penyandang disabilitas dan keluarganya mengendalikan daya beli signifikan; mengecualikan mereka melepas itu. Layanan yang dapat diakses mengurangi kebutuhan kanal berbantuan yang mahal (bantuan telepon dan tatap muka), yang penghematan operasional langsung, terutama bagi pemerintah. Dan karena perbaikan aksesibilitas (label jelas, dukungan keyboard, konten terbaca, markup kokoh) membantu semua orang, ia biasanya menaikkan penyelesaian dan kepuasan keseluruhan.

Pada TCO, biaya adopsi adalah pelatihan, perkakas, dan membangun aksesibilitas ke komponen dan pipeline, semuanya sederhana bila dilakukan dari awal. Biaya tidak mengadopsi parah dan datang dari beberapa arah: liabilitas hukum (gugatan, penyelesaian, remediasi perintah pengadilan, penalti regulasi), biaya jauh lebih tinggi memasang di bawah tekanan tenggat, kerusakan reputasi, dan biaya berkelanjutan melayani pengguna yang terkecualikan lewat kanal lebih mahal. Memasang belakangan biasanya berbiaya beberapa kali lipat dari merancang masuk.

Untuk mengajukan kasus kepada pimpinan, mulai dengan kewajiban hukum di tempat ia berlaku (tak dapat ditawar bagi pemerintah dan makin bagi sektor swasta). Lalu kuantifikasi populasi yang dapat dijangkau yang Anda kecualikan, biaya kanal berbantuan dari pengecualian itu, dan keuntungan "curb-cut" bagi semua pengguna. Posisikan aksesibilitas sebagai manajemen risiko plus kualitas, bukan amal.

## Anti-pola dan jebakan

- **Aksesibilitas sebagai kotak centang pra-peluncuran**: audit di akhir alih-alih praktik berkelanjutan, menjamin pengerjaan ulang menit terakhir yang mahal.
- **"Div soup"**: markup non-semantik dengan penangan klik pada elemen generik, tak terlihat oleh teknologi bantu.
- **Penyalahgunaan ARIA**: menempelkan ARIA ke markup rusak, yang lebih menyesatkan pembaca layar daripada markup biasa.
- **Informasi hanya-warna**: status ditunjukkan hanya oleh warna, tak terlihat oleh pengguna buta warna.
- **Fokus tak terlihat**: menghapus outline fokus demi estetika, menelantarkan pengguna keyboard.
- **Jebakan keyboard**: modal dan widget yang menjebak atau kehilangan fokus.
- **Kepuasan diri atas pemindaian otomatis**: lulus pemindai dan mengasumsikan produk dapat diakses.
- **Overlay aksesibilitas**: widget "perbaikan satu baris" pihak ketiga yang tidak memberi kesesuaian nyata dan dapat memperburuk pengalaman.
- **Mengecualikan pengguna disabilitas dari riset**: merancang untuk pengguna disabilitas khayalan alih-alih menguji dengan yang nyata.

## Model kematangan

**Tingkat 1: Memulai.** Tidak ada praktik aksesibilitas. Isu ditemukan hanya ketika pengguna mengeluh atau gugatan tiba, dan respons reaktif. Markup non-semantik dan tak teruji, dan tak ada yang memiliki masalah.

**Tingkat 2: Mengembangkan.** Kesadaran ada dan sebagian tim bertindak: pemindai otomatis dalam build di sini, penelusuran keyboard di sana, audit pra-peluncuran sebelum rilis besar. Praktik dasar dan tidak konsisten lintas tim, aksesibilitas masih daftar periksa tahap akhir, dan sering dikesampingkan di bawah tekanan jadwal.

**Tingkat 3: Membakukan.** WCAG 2.2 AA adalah standar terdokumentasi, ditegakkan di seluruh organisasi. Aksesibilitas dibangun ke dalam sistem desain agar komponen dikirim dapat diakses secara bawaan, diuji otomatis dan manual, dan ditulis dalam definisi selesai. Tim dilatih, pemilik atau pusat keunggulan ada, dan proses remediasi terdefinisi.

**Tingkat 4: Mengelola.** Aksesibilitas diukur dan dikendalikan dengan data terhadap garis dasar. Organisasi melacak metrik kesesuaian seiring waktu (tingkat lulus pemindai, jumlah hambatan terbuka menurut keparahan, cakupan uji pembaca layar atas perjalanan kritis, dan waktu-ke-remediasi), melaporkannya per tim di dasbor, dan memperlakukan regresi sebagai kegagalan build alih-alih peringatan nasihat. Target ditetapkan terhadap garis dasar dan kemajuan ditinjau, sehingga tim yang tergelincir terlihat sebelum audit menemukannya.

**Tingkat 5: Mengorkestrasi.** Aksesibilitas terus diperbaiki dan terintegrasi di seluruh organisasi. Penyandang disabilitas menjadi bagian riset dan pengujian secara berulang, dan aksesibilitas tertanam dalam pengadaan, token desain, dan CI. Organisasi beradaptasi seiring standar bergerak (mengadopsi kriteria WCAG baru dan bersiap untuk WCAG 3.0), dan mempengaruhi vendor serta mitra agar seluruh rantai pasok sesuai.

## Gagasan untuk didiskusikan

- Bagaimana Anda menjaga aksesibilitas agar tidak dikesampingkan ketika tenggat mengetat?
- Apa campuran yang tepat antara pengujian otomatis, manual, dan pengguna untuk profil risiko Anda?
- Bagaimana kesesuaian aksesibilitas harus ditulis ke kontrak vendor dan pengadaan?
- Bagaimana Anda menangani celah antara kesesuaian WCAG dan kegunaan sejati bagi penyandang disabilitas?
- Bagaimana tim harus bersiap untuk WCAG 3.0 sambil membangun ke 2.2 hari ini?
- Bagaimana Anda merekrut dan mengompensasi peserta disabilitas untuk riset secara adil dan hormat?

## Poin-poin utama

- Aksesibilitas adalah atribut kualitas garis dasar dan, bagi pemerintah, persyaratan hukum.
- Rancang ke WCAG 2.2 AA sebagai lantai; gunakan prinsip POUR sebagai model mental.
- HTML semantik lebih dulu; ARIA hanya untuk mengisi celah nyata, dilakukan dengan benar.
- Perkakas otomatis menangkap sekitar sepertiga isu; pengujian manual dan teknologi bantu esensial.
- Uji bersama penyandang disabilitas, bukan hanya untuk mereka.
- Membangun aksesibilitas masuk murah dan tahan lama; memasang belakangan mahal dan rapuh.
- Desain yang dapat diakses adalah desain lebih baik untuk semua orang: efek curb-cut itu nyata.

## Referensi dan bacaan lanjutan

- W3C, *Web Content Accessibility Guidelines (WCAG) 2.2* dan dokumen Understanding/Techniques pendukung
- W3C, *WAI-ARIA Authoring Practices Guide*
- W3C Web Accessibility Initiative (WAI), materi pengantar dan tutorial
- Laura Kalbag, *Accessibility for Everyone*
- Sarah Horton dan Whitney Quesenbery, *A Web for Everyone*
- Regine Gilbert, *Inclusive Design for a Digital World*
- Standar U.S. Section 508 dan panduan Section508.gov
- Standar Eropa EN 301 549 dan European Accessibility Act
- Panduan aksesibilitas pemerintah (mis., manual aksesibilitas UK GDS)
- WebAIM, riset dan artikel termasuk analisis aksesibilitas tahunan
