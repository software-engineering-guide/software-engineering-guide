# 1.2 Topologi tim dan desain organisasi

## Tinjauan dan motivasi

Cara Anda membagi orang ke dalam tim menentukan perangkat lunak apa yang dapat Anda bangun dan seberapa cepat Anda membangunnya. Ini bukan metafora. Ini adalah konsekuensi yang nyaris mekanis, dikenal sebagai [Hukum Conway](https://en.wikipedia.org/wiki/Conway%27s_law): organisasi merancang sistem yang mencerminkan struktur komunikasinya sendiri. Jika tiga tim membangun sebuah [kompiler](https://en.wikipedia.org/wiki/Compiler), Anda mendapatkan kompiler tiga-lintasan. Jika logika pembayaran Anda terbagi di antara tim frontend, tim backend, dan tim basis data, setiap perubahan pembayaran memerlukan koordinasi tiga arah. Bagi organisasi kecil, hal itu masih dapat dikelola. Bagi organisasi besar, bentuk bagan organisasi menjadi kendala dominan atas rekayasa, arsitektur, kecepatan pengiriman, dan kualitas Anda. Karena itu merancang struktur tim adalah kegiatan rekayasa kelas satu, bukan urusan SDM yang dipikirkan belakangan.

Topologi tim memberi Anda kosakata yang disengaja untuk desain ini. Alih-alih membiarkan struktur menumpuk tanpa sengaja lewat reorganisasi dan penambahan personel, organisasi yang matang memilih jenis tim dan mode interaksi dengan sengaja, lalu meninjau ulang pilihan itu seiring berkembangnya sistem dan bisnis. Tujuannya adalah menjaga [beban kognitif](https://en.wikipedia.org/wiki/Cognitive_load) setiap tim tetap rendah, yaitu total yang harus dipegang sebuah tim dalam kepalanya agar efektif, sehingga tim dapat memiliki domainnya dari ujung ke ujung dan menyampaikan aliran nilai yang stabil tanpa terus menunggu pihak lain.

Bagi enterprise dan pemerintah, disiplin ini menentukan. Organisasi besar secara alami melebar menjadi hierarki dalam, layanan bersama dengan antrean panjang, dan rantai serah terima yang mengubah perubahan dua hari menjadi proyek dua bulan. Pemerintah menambahkan batas pengadaan, tim kontraktor, dan [pemisahan tugas](https://en.wikipedia.org/wiki/Separation_of_duties) yang diwajibkan, yang memecah kepemilikan lebih jauh. Desain topologi yang eksplisit adalah cara organisasi-organisasi ini merebut kembali alirannya: menyelaraskan tim dengan aliran nilai, membangun platform yang mengurangi beban kognitif, dan memilih pola interaksi yang membuat dependensi terlihat dan disengaja, bukan tersembunyi dan konstan.

## Prinsip utama

- Hukum Conway tak terhindarkan; rancang tim agar sesuai dengan rekayasa perangkat lunak yang Anda inginkan ("manuver terbalik").
- Optimalkan beban kognitif tim, bukan pemanfaatan maksimum individu.
- Pilih tim yang selaras dengan aliran dan memiliki seiris nilai dari ujung ke ujung.
- Platform ada untuk mengurangi beban kognitif tim yang selaras dengan aliran, bukan untuk menjadi penjaga gerbang.
- Buat interaksi tim eksplisit dan sedikit: kolaborasi, X-as-a-service, atau fasilitasi.
- Minimalkan dependensi; setiap serah terima lintas tim adalah antrean dan risiko.
- Struktur tim adalah desain hidup yang harus berkembang seiring perubahan sistem dan bisnis.

## Rekomendasi

### Gunakan empat jenis tim dasar

Topologi tim mendefinisikan empat jenis tim yang mencakup sebagian besar kebutuhan. Tim yang selaras dengan aliran (stream-aligned) adalah bawaan: masing-masing memiliki aliran kerja berkelanjutan untuk produk, layanan, atau perjalanan pengguna tertentu dari ujung ke ujung. Tim platform menyediakan produk internal (komputasi, deployment, pipeline data, identitas) yang dikonsumsi tim stream-aligned secara swalayan, sehingga menurunkan beban kognitif mereka. Tim pemberdaya (enabling) adalah spesialis (pengujian, keamanan, observabilitas) yang membimbing tim stream-aligned membangun suatu kemampuan, lalu mundur. Tim subsistem rumit (complicated-subsystem) memiliki komponen yang membutuhkan keahlian spesialis mendalam (mesin penetapan harga, [kodek video](https://en.wikipedia.org/wiki/Video_codec), modul kriptografi), di mana tidak masuk akal setiap tim memegang pengetahuan itu. Sebagian besar tim Anda sebaiknya stream-aligned; tiga jenis lainnya ada untuk mendukungnya.

### Terapkan manuver Conway terbalik

Karena perangkat lunak mencerminkan struktur organisasi Anda, bentuklah tim agar menghasilkan perangkat lunak yang Anda inginkan. Ingin layanan yang berpasangan longgar dengan batas jelas? Buat tim yang berpasangan longgar dengan batas kepemilikan jelas. Ingin kemampuan pembayaran yang dirilis dengan jadwalnya sendiri? Bentuk tim pembayaran yang memilikinya dari depan sampai belakang. Jangan melawan Hukum Conway dengan koordinasi heroik. Gambar ulang batas tim agar arsitektur yang Anda inginkan menjadi jalur dengan hambatan terkecil.

### Kelola beban kognitif secara eksplisit

Sebuah tim hanya dapat menguasai sebatas tertentu. Beban kognitif mencakup kompleksitas domain, teknologi, beban operasional, dan luasnya pemangku kepentingan. Ketika tim memiliki terlalu banyak layanan yang tidak berhubungan, kualitas dan kecepatan sama-sama runtuh. Maka batasi tanggung jawab setiap tim pada domain yang benar-benar dapat dikuasainya, dan gunakan platform serta tim pemberdaya untuk mengambil kompleksitas tak berdiferensiasi dari piringnya. Jaga tim kira-kira lima sampai sembilan orang: cukup kecil untuk berkomunikasi dengan mudah dan, secara kiasan, cukup diberi makan oleh beberapa kotak pizza.

### Pilih mode interaksi dengan sengaja

Batasi interaksi tim pada tiga mode. Kolaborasi adalah kerja erat berbandwidth tinggi antara dua tim untuk jangka waktu tertentu; ampuh untuk penemuan, tetapi mahal, jadi buatlah sementara. X-as-a-service adalah hubungan penyedia/konsumen yang bersih dengan antarmuka yang terdefinisi baik, ideal untuk konsumsi platform dalam skala besar. Fasilitasi adalah satu tim membantu tim lain belajar, yang dikerjakan tim pemberdaya. Beri nama mode untuk setiap hubungan lintas tim yang penting, dan baca kolaborasi berkepanjangan antara dua tim yang sama sebagai sinyal bahwa batas mereka berada di tempat yang salah.

### Pilih model operasi untuk fungsi lintas bidang

Keamanan, data, desain, dan disiplin serupa dapat diorganisasi dengan tiga cara: tersentralisasi (satu tim memilikinya untuk semua), terfederasi (spesialis ditempatkan paruh waktu, berkoordinasi lewat guild), atau tertanam (spesialis khusus di dalam setiap tim stream-aligned). Tersentralisasi memberi konsistensi dan kedalaman, tetapi menjadi hambatan. Tertanam memberi kecepatan dan konteks, tetapi berisiko inkonsistensi dan duplikasi. Terfederasi (sering model hub-and-spoke atau [komunitas praktik](https://en.wikipedia.org/wiki/Community_of_practice)) berada di antara keduanya. Pilih per fungsi dan per skala. Sebagian besar organisasi besar mendarat pada terfederasi untuk disiplin ini, dengan inti pusat kecil yang menetapkan standar.

### Berinvestasi pada inner-source

[Inner-source](https://en.wikipedia.org/wiki/Inner_source) membawa pola kolaborasi [sumber terbuka](https://en.wikipedia.org/wiki/Open-source_software) ke dalam organisasi: repositori internal bersama, pedoman kontribusi yang diterbitkan, [tinjauan kode](https://en.wikipedia.org/wiki/Code_review) lintas batas tim, dan pemelihara yang jelas. Ketika sebuah tim membutuhkan perubahan pada komponen tim lain, ia dapat menyumbangkan perubahan itu langsung alih-alih membuat tiket dan menunggu dalam antrean. Ini meringankan dependensi lintas tim tanpa melarutkan kepemilikan, dan menyebarkan pengetahuan serta standar secara alami di populasi rekayasa yang besar.

## Trade-off: kelebihan dan kekurangan

| Model untuk fungsi lintas bidang | Kelebihan | Kekurangan |
| --- | --- | --- |
| Tersentralisasi (satu tim untuk semua) | Konsistensi, keahlian mendalam, standar jelas | Hambatan, antrean, hilangnya konteks produk |
| Terfederasi (hub-and-spoke, guild) | Menyeimbangkan konsistensi dan kecepatan; berbagi pengetahuan | Memerlukan disiplin koordinasi; akuntabilitas dapat kabur |
| Tertanam (spesialis per tim) | Cepat, kaya konteks, kepemilikan tinggi | Duplikasi, inkonsistensi, sulit diisi pada skala besar |

| Jenis tim | Terbaik untuk | Risiko jika berlebihan |
| --- | --- | --- |
| Stream-aligned | Sebagian besar pengiriman produk dan layanan | Tidak ada; inilah yang seharusnya dominan |
| Platform | Mengurangi beban kognitif bersama | Menjadi penjaga gerbang di menara gading |
| Enabling | Menyebarkan kemampuan secara sementara | Berubah menjadi dependensi permanen |
| Complicated-subsystem | Domain spesialis yang benar-benar mendalam | Dipakai sebagai alasan menimbun pekerjaan biasa |

Trade-off yang berulang adalah otonomi versus konsistensi. Tim yang sepenuhnya otonom bergerak cepat, tetapi menyimpang dalam standar, perkakas, dan postur keamanan. Kendali yang sepenuhnya tersentralisasi menjaga konsistensi, tetapi mencekik aliran. Desain topologi yang baik menemukan sambungannya: otonomi untuk pengiriman stream-aligned, ditambah standar pusat yang tipis dan platform jalan beraspal (perkakas bawaan yang didukung baik dan membuat pilihan yang patuh menjadi yang mudah) untuk hal-hal yang memang harus konsisten.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Sinyal konkret apa yang akan memberi tahu Anda bahwa beban kognitif sebuah tim terlalu tinggi, sebelum kualitas runtuh?** "Batasi setiap tim pada domain yang dapat dikuasainya" mudah diucapkan dan sulit ditindaklanjuti tanpa bukti, karena beban kognitif tetap tak terlihat sampai pengiriman dan keandalan memburuk. Perhatikan gejala yang terukur: jumlah layanan atau repositori tak berhubungan yang dimiliki tim, berapa lama orientasi berlangsung, berapa banyak domain yang harus dialihkan konteksnya oleh seorang insinyur dalam seminggu, dan naiknya tingkat insiden di sudut-sudut wewenang tim. Bagi organisasi besar, ini penting karena tim yang kelebihan beban diam-diam menjadi hambatan yang tidak diprediksi oleh diagram reorganisasi mana pun. Bawa angka-angka ini ke diskusi, ditambah perasaan tim sendiri tentang apa yang dapat dan tidak dapat mereka pegang di kepala. Jika sinyal menunjukkan kelebihan beban, langkahnya adalah melimpahkan pekerjaan tak berdiferensiasi ke platform atau tim pemberdaya, bukan menuntut lebih banyak aksi heroik.

2. **Apakah reorganisasi benar-benar sepadan dengan gangguannya di sini, atau Anda sedang memberi makan kecanduan reorganisasi?** Menggambar ulang batas untuk menerapkan manuver Conway terbalik itu ampuh, dan setiap reorganisasi juga menghancurkan stabilitas yang dibutuhkan tim untuk menyatu serta mengatur ulang pengetahuan domain yang diperoleh dengan susah payah. Pertimbangan yang bersaing adalah pajak koordinasi berkelanjutan dari struktur saat ini versus biaya sekali jalan dan pukulan moral akibat mengubahnya. Dalam konteks enterprise dan pemerintah, batas pengadaan, tim kontraktor, dan pemisahan tugas yang diwajibkan membuat reorganisasi lebih lambat dan lebih mahal, sehingga ambang batasnya harus lebih tinggi. Bawa bukti keterlambatan akibat dependensi: berapa banyak inisiatif yang terhambat menunggu tim lain, dan berapa lama. Reorganisasilah ketika penantian itu struktural dan besar, dan tahan diri dari mengocok ulang ketika rasa sakitnya sementara atau lebih murah diselesaikan dengan kontribusi inner-source dan antarmuka yang lebih jelas.

3. **Untuk keamanan, data, dan desain, peristiwa apa yang akan memicu Anda berpindah antara tertanam, terfederasi, dan tersentralisasi?** Rekomendasi bab ini adalah memilih per fungsi dan per skala, dan disiplin yang lebih sulit adalah memutuskan sebelumnya pertumbuhan atau risiko apa yang akan membuat Anda meninjau ulang pilihan itu. Model yang cocok untuk lima puluh insinyur dapat menjadi hambatan atau bencana konsistensi pada lima ratus, dan organisasi enterprise serta pemerintah terutama perlu menamai standar yang akan selalu dipegang inti pusat kecil. Bawa waktu antrean dan kesenjangan konsistensi saat ini untuk setiap fungsi: tim keamanan pusat dengan antrean tinjauan berminggu-minggu adalah sinyal untuk memfederasi, sedangkan spesialis tertanam yang menghasilkan model data yang tidak kompatibel adalah sinyal untuk menambah inti standar pusat. Putuskan pemicunya sekarang, seperti ambang panjang antrean atau temuan audit, sehingga perubahan menjadi evolusi terencana, bukan reaksi krisis. Jawabannya menentukan di mana Anda berinvestasi pada jalan beraspal dan champion versus hub pusat.

4. **Bagaimana Anda tahu apakah tim platform Anda benar-benar menurunkan beban kognitif atau diam-diam menjadi penjaga gerbang?** Platform ada untuk membuat pilihan yang patuh dan andal menjadi yang mudah lewat swalayan, dan tim yang sama dapat melenceng ke arah mewajibkan perkakas, meninjau setiap permintaan dengan tangan, dan menambah gesekan yang seharusnya ia hilangkan. Bagi organisasi besar, perbedaan ini menentukan apakah investasi platform kembali modal atau berubah menjadi hambatan pusat yang diantrekan setiap tim stream-aligned. Pertimbangan yang bersaing adalah konsistensi dan kendali di satu sisi melawan otonomi konsumen dan aliran di sisi lain. Bawa bukti yang akan dikenali konsumen: berapa lama sebuah tim stream-aligned dapat membuat lingkungan atau pipeline baru secara swalayan tanpa membuat tiket, rasio tindakan swalayan terhadap yang dimediasi manusia, dan adopsi platform yang diukur dari tim yang memilihnya, bukan tim yang dipaksa. Dalam konteks enterprise dan pemerintah, tuntut agar platform menghasilkan bukti audit dan kepatuhan secara otomatis, bukan lewat gerbang manual, karena platform yang memenuhi aturan pemisahan tugas dengan menyisipkan peninjau manusia telah menciptakan ulang hambatan yang didanai untuk dilarutkan.

5. **Hubungan lintas tim mana yang telah mengendap menjadi kolaborasi permanen, dan apa yang akan mengubah masing-masing menjadi antarmuka layanan yang bersih atau batas yang digambar ulang?** Mode kolaborasi dimaksudkan intens dan sementara, dan kerja berpasangan yang tidak pernah berakhir biasanya merupakan sinyal bahwa kepemilikan berada di tempat yang salah atau bahwa antarmuka antara dua tim tidak pernah dibuat eksplisit. Ini penting pada skala besar karena kolaborasi tetap yang tidak bernama adalah tempat biaya koordinasi bersembunyi: ia tidak muncul di bagan organisasi mana pun, tetapi membebani setiap perubahan yang disentuh kedua tim. Pertimbangan yang bersaing adalah nilai penemuan dari tetap dekat versus aliran yang Anda peroleh dengan mengubah hubungan menjadi kontrak X-as-a-service dengan antarmuka terdefinisi, atau dengan menggabungkan tanggung jawab ke dalam satu tim. Bawa daftar pasangan tim yang berkolaborasi terus-menerus lebih dari satu kuartal, perubahan yang membutuhkan kedua tim dalam beberapa bulan terakhir, dan apakah antarmuka stabil di antara mereka dapat dituliskan. Untuk konteks enterprise dan pemerintah, di mana batas kontraktor dan paket pengadaan dapat membekukan serah terima selama bertahun-tahun, sebutkan hubungan mana yang dapat Anda ubah dengan antarmuka dan kontribusi inner-source dan mana yang terkunci secara kontrak dan harus dikelola sebagai dependensi eksplisit.

6. **Ketika tim pemberdaya membantu tim lain membangun suatu kemampuan, bagaimana Anda tahu ia telah berhasil dan dapat mundur alih-alih menjadi dependensi permanen?** Tim pemberdaya dimaksudkan membimbing tim stream-aligned menguasai pengujian, keamanan, atau observabilitas lalu melanjutkan, dan tanpa syarat keluar yang eksplisit hubungan bimbingan itu mengeras menjadi layanan tetap yang tidak pernah benar-benar diserap tim stream-aligned. Bagi organisasi besar, ini adalah beda antara menyebarkan kemampuan ke puluhan tim dan menciptakan hambatan bersama baru yang semakin buruk skalanya setiap tahun. Pertimbangan yang bersaing adalah kedalaman dan konsistensi yang diberikan tim spesialis melawan otonomi dan kepemilikan ujung-ke-ujung yang ingin Anda bangun ke dalam tim stream-aligned. Bawa bukti alih kemampuan: apakah tim penerima kini menangani pekerjaan tanpa kehadiran tim pemberdaya, berapa banyak tim yang menjadi komitmen satu kelompok pemberdaya tetap sekaligus, dan berapa lama setiap keterlibatan telah berjalan melewati serah terima yang dimaksudkan. Dalam konteks enterprise dan pemerintah, di mana keterampilan spesialis yang langka mungkin berada di balik satu tim pusat atau satu kontrak, putuskan sebelumnya bagaimana Anda mendanai alih kemampuan dan champion agar keahlian menyebar ke tim pengiriman alih-alih terkunci di balik antrean yang harus ditunggu setiap audit dan rilis.

## Lensa sektor

**Startup.** Dengan segelintir insinyur dan runway terbatas, topologi yang tepat adalah satu tim stream-aligned yang memiliki seluruh produk, dan disiplinnya adalah menolak membuat silo sebelum Anda membutuhkannya. Tahan diri merekrut satu orang "DevOps" atau "QA" yang menjadi gerbang; lebur keterampilan itu ke dalam satu tim sebagai kemampuan tertanam. Jaga agar Hukum Conway bekerja untuk Anda dengan menjaga organisasi tetap datar, sehingga arsitektur tetap sesederhana dan semudah diubah seperti tim.

**Bisnis kecil.** Anda tidak akan mengisi tim platform atau tim pemberdaya khusus, jadi belilah platformnya: gunakan layanan cloud terkelola, pipeline yang di-hosting, dan perkakas keamanan siap pakai untuk mengambil beban kognitif tak berdiferensiasi dari satu atau dua tim Anda. Bingkai urusan lintas bidang seperti keamanan dan data sebagai hal yang Anda konfigurasi dan konsumsi, bukan fungsi yang Anda bangun. Sisakan kepemilikan khusus hanya untuk satu subsistem rumit yang benar-benar membedakan Anda, dan biarkan vendor memikul sisanya.

**Enterprise.** Pada skala besar, masalahnya adalah biaya koordinasi lintas banyak tim, jadi jadikan topologi desain yang eksplisit dan diatur: taksonomi bersama empat jenis tim, mode interaksi yang dinamai, platform jalan beraspal, dan inner-source untuk meringankan antrean lintas tim. Lacak keterlambatan akibat dependensi dan beban kognitif tim sebagai metrik portofolio, dan jalankan reorganisasi sebagai evolusi yang disengaja dengan ambang tinggi, bukan refleks tahunan. Inti pusat yang tipis memegang standar yang harus konsisten, sementara tim stream-aligned mempertahankan otonomi atas pengiriman.

**Pemerintah.** Aturan pengadaan, batas kontraktor, dan pemisahan tugas yang diwajibkan memecah kepemilikan, jadi rancang topologi untuk memenuhi kendala itu lewat perkakas dan antarmuka yang jelas, bukan serah terima manusia. Pilih model terfederasi dengan inti standar kecil dan platform yang menghasilkan bukti audit dan kepatuhan secara otomatis, sehingga pemisahan tugas ditegakkan oleh pipeline, bukan antrean tinjauan. Dokumentasikan batas tim, mode interaksi, dan model operasi secara terbuka, sehingga struktur transparan bagi auditor, badan pengawas, dan publik yang mendanainya.

## Contoh

**Startup.** Sebuah startup sepuluh orang memiliki satu tim stream-aligned yang memiliki seluruh produk dari ujung ke ujung, yang tepat pada skalanya: tanpa serah terima, tanpa pajak koordinasi, semua orang berbagi konteks yang sama. Masalah dimulai ketika mereka merekrut "orang DevOps" khusus dan "orang QA" terpisah dan tanpa sengaja menciptakan ulang silo fungsional, sehingga setiap rilis kini menunggu dua individu. Mereka mengoreksi arah dengan memperlakukan rekrutan itu sebagai kemampuan platform-dan-pengujian tertanam di dalam satu tim, bukan gerbang yang harus dilalui pekerjaan. Pada ukuran ini, topologi termurah adalah yang menjaga semua orang dalam satu aliran.

**Enterprise.** Checkout sebuah pengecer besar lambat berubah karena logika frontend, backend, dan pemenuhan pesanan terbagi di tiga tim yang diorganisasi secara fungsional, memaksa setiap perubahan melalui tiga backlog. Dengan menerapkan manuver Conway terbalik, mereka mereorganisasi menjadi tim stream-aligned di sekitar perjalanan pelanggan ("jelajah," "keranjang dan checkout," "pascapembelian"), masing-masing memiliki irisannya dari depan sampai belakang, didukung tim platform yang menyediakan deployment dan observabilitas sebagai layanan. Perubahan checkout yang dulu memakan satu kuartal mulai dirilis dalam hitungan hari, karena koordinasi yang dulu melintasi tim kini terjadi di dalam satu tim.

**Pemerintah.** Sebuah lembaga pajak pemerintah menjalankan tim keamanan pusat yang meninjau setiap rilis, menciptakan antrean berminggu-minggu yang menunda perbaikan kritis. Mereka beralih ke model terfederasi: fungsi keamanan pusat kecil menetapkan standar dan menyediakan "jalan beraspal" berupa pipeline yang telah disetujui dan dipindai otomatis, sementara champion keamanan yang ditempatkan paruh waktu di tiap tim pengiriman menangani keputusan sehari-hari. Platform menghasilkan bukti kepatuhan secara otomatis. Persyaratan pemisahan tugas yang diwajibkan tetap terpenuhi, tetapi lewat perkakas dan antarmuka yang jelas, bukan hambatan manusia, yang memangkas lead time rilis secara dramatis sambil meningkatkan kesiapan audit.

## Kasus bisnis: motivasi, ROI, dan TCO

Anda membayar desain tim yang buruk dalam bentuk beban koordinasi, dan beban itu tumbuh lebih cepat daripada linear terhadap jumlah tim yang harus bersinkronisasi untuk perubahan tipikal. Setiap serah terima adalah antrean dengan waktu tunggu, transfer konteks yang kehilangan informasi, dan peluang baru untuk salah komunikasi. Ketika perubahan rutin membutuhkan tiga tim menyelaraskan peta jalan mereka, biaya sebenarnya bukan jumlah kerja mereka; melainkan biaya jauh lebih besar dari penjadwalan, penantian, dan pengerjaan ulang. Gambar ulang batas agar sebagian besar perubahan muat di dalam kepemilikan satu tim, dan beban itu hilang begitu saja.

Biaya adopsi itu nyata. Reorganisasi mengganggu, dan membangun platform serta praktik inner-source memerlukan investasi awal sebelum hasilnya tiba. Tetapi biaya tidak mengadopsi berlipat ganda. Organisasi yang membiarkan struktur menumpuk tanpa sengaja menimbun rantai serah terima, tim hambatan bersama dengan antrean selama satu kuartal, dan arsitektur yang membatu oleh bagan organisasi. Untuk meyakinkan pimpinan, ukur keterlambatan akibat dependensi: berapa banyak inisiatif aktif yang terhambat menunggu tim lain, dan berapa lama. Investasi platform dan topologi biasanya kembali modal dengan mengubah penantian itu menjadi aliran, yang tampak sebagai lead time lebih pendek dan throughput lebih tinggi tanpa menambah personel.

## Anti-pola dan jebakan

- Mengabaikan Hukum Conway: merancang arsitektur yang tidak dapat dikirimkan oleh struktur organisasi.
- Silo fungsional: tim frontend, backend, QA, dan ops terpisah yang harus berkoordinasi untuk setiap perubahan.
- Hambatan layanan bersama: tim pusat yang harus diantrekan oleh setiap proyek.
- Platform sebagai penjaga gerbang: tim platform yang mewajibkan alih-alih melayani, menambah gesekan alih-alih menghilangkannya.
- Kelebihan beban kognitif: tim memiliki sistem luas yang tidak berhubungan dan tidak dapat mereka kuasai.
- "Kolaborasi" permanen: dua tim terjerat terus-menerus, menandakan batas yang salah tempat.
- Kecanduan reorganisasi: mengocok ulang terus-menerus, menghancurkan stabilitas yang dibutuhkan tim untuk menyatu.

## Model kematangan

- **Tingkat 1, Memulai.** Tim terbentuk karena kebetulan, jumlah personel, atau hierarki warisan; tidak ada yang menamai jenis tim atau mode interaksi; silo fungsional dan hambatan layanan bersama ada di mana-mana dan dependensi tersembunyi sampai menghambat rilis.
- **Tingkat 2, Mengembangkan.** Beberapa tim stream-aligned ada dan upaya platform atau inner-source pertama muncul, tetapi polanya diterapkan tidak merata: beberapa tim memiliki irisan mereka dari ujung ke ujung sementara yang lain masih mengantre di balik fungsi pusat, dan beban kognitif dibicarakan secara anekdot, bukan dikelola.
- **Tingkat 3, Membakukan.** Empat jenis tim dan tiga mode interaksi didokumentasikan dan digunakan dengan sengaja di seluruh organisasi; platform dan inner-source meringankan dependensi lintas tim; model operasi untuk keamanan, data, dan desain dipilih dan dituliskan, dan tim baru dibentuk berdasarkan standar ini, bukan improvisasi.
- **Tingkat 4, Mengelola.** Topologi diukur dan dikendalikan terhadap garis dasar: tim melacak beban kognitif, keterlambatan akibat dependensi (inisiatif yang terhambat menunggu tim lain, dan berapa lama), rasio swalayan dan adopsi platform, durasi mode interaksi, dan metrik aliran pengiriman seperti lead time dan frekuensi perubahan. Ambang batas memicu tindakan, misalnya panjang antrean yang memaksa sebuah fungsi memfederasi atau kolaborasi tetap yang menandai batas yang salah tempat, sehingga keputusan bertumpu pada bukti, bukan opini.
- **Tingkat 5, Mengorkestrasi.** Desain tim terus diperbaiki dan terintegrasi dengan perencanaan arsitektur, produk, dan risiko; organisasi membentuk ulang batas seiring berkembangnya sistem dan bisnis, mengakhiri keterlibatan pemberdayaan setelah kemampuan berpindah, dan menyeimbangkan kembali investasi platform seiring bergesernya beban kognitif, menjaga aliran cepat sebagai sifat adaptif yang tetap, bukan reorganisasi sekali jalan.

## Gagasan untuk didiskusikan

- Untuk perubahan tipikal, berapa tim yang harus berkoordinasi, dan mengapa?
- Tim kita yang mana yang memikul terlalu banyak beban kognitif, dan apa yang dapat dilimpahkan ke platform?
- Di mana kita melawan Hukum Conway alih-alih menggambar ulang batas?
- Apakah tim platform kita melayani tim stream-aligned atau menjadi penjaga gerbang bagi mereka?
- Haruskah keamanan, data, dan desain tersentralisasi, terfederasi, atau tertanam bagi kita saat ini?
- Kolaborasi "sementara" mana yang diam-diam telah menjadi dependensi permanen?

## Poin-poin utama

- Struktur organisasi menentukan arsitektur dan kecepatan pengiriman; rancanglah dengan sengaja.
- Gunakan empat jenis tim, dengan stream-aligned sebagai bawaan dan sisanya sebagai pendukung.
- Terapkan manuver Conway terbalik untuk menjadikan arsitektur yang diinginkan sebagai jalur yang mudah.
- Kelola beban kognitif; batasi setiap tim pada domain yang dapat dikuasainya.
- Batasi dan namai mode interaksi lintas tim; perlakukan dependensi yang berlarut-larut sebagai cacat batas.
- Pilih model tersentralisasi, terfederasi, atau tertanam untuk fungsi lintas bidang menurut skala, dan gunakan InnerSource untuk meringankan antrean.

## Referensi dan bacaan lanjutan

- Matthew Skelton dan Manuel Pais, "Team Topologies: Organising Business and Technology Teams for Fast Flow"
- Melvin Conway, "How Do Committees Invent?" (asal Hukum Conway)
- Nicole Forsgren, Jez Humble, Gene Kim, "Accelerate"
- Will Larson, "An Elegant Puzzle: Systems of Engineering Management"
- Sam Newman, "Building Microservices" (tentang menyelaraskan layanan dengan tim)
- Danese Cooper dan Klaas-Jan Stol, "Adopting InnerSource," dan pola-pola InnerSource Commons
- Frederick Brooks, "The Mythical Man-Month" (beban komunikasi)
