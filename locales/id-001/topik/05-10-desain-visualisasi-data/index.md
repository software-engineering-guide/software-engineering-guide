# 5.10 Desain visualisasi data

## Tinjauan dan motivasi

Bagan adalah argumen yang dibuat dari tinta. Ketika Anda memplot data, Anda memilih apa yang akan diperhatikan pembaca lebih dulu, apa yang akan mereka bandingkan, dan kesimpulan apa yang akan mereka capai dalam dua detik sebelum beralih. Lakukan dengan baik dan pertanyaan sulit menjawab dirinya sendiri: tren jelas, pencilan melompat keluar, dua kelompok jelas berbeda. Lakukan dengan buruk dan data yang sama menyesatkan, membingungkan, atau sekadar membosankan, dan keputusan yang hendak diinformasikannya dibuat berdasarkan firasat. [Visualisasi data](https://en.wikipedia.org/wiki/Data_and_information_visualization) adalah kerajinan desain mengubah angka menjadi gambar yang memungkinkan orang melihat apa arti angka itu.

Bab ini tentang kerajinan itu: memilih bagan yang tepat, meng-encode data dengan jujur, memakai warna dan tata letak agar mata mendarat di tempat yang seharusnya, dan menjaga seluruhnya dapat diakses. Ia berada dalam Bagian 5 karena bagan adalah antarmuka, dan mewarisi segala dari sisa bagian ini. Ia bertumpu pada fondasi [pengalaman pengguna](https://en.wikipedia.org/wiki/User_experience) (UX) bab 5.1, meminjam token dan komponen dari sistem desain bab 5.2, harus memenuhi kewajiban aksesibilitas bab 5.3, dan berbicara dengan suara sederhana dan bertujuan desain konten di bab 5.4. Ia sengaja menjauh dari perpipaan. Pipeline data, gudang, dan perkakas pelaporan analitik dan business intelligence (bab 7.3) adalah subjek berbeda, begitu pula ilmu keputusan dan budaya data yang lebih luas di bab 7.5. Di sini Anda belajar membuat gambar menjadi baik, dari mana pun data berasal.

Bagi tim besar, taruhannya koordinasi dan kepercayaan. Ketika setiap skuad menata bagannya sendiri, perusahaan berakhir dengan lima puluh dialek "pendapatan seiring waktu," masing-masing dengan sumbu, warna, dan pembulatan berbeda, dan eksekutif belajar tidak memercayai semuanya. Dalam pengaturan enterprise, dasbor yang menyesatkan menggerakkan anggaran nyata ke arah yang salah. Di pemerintah, bagan publik adalah tindakan komunikasi dengan warga dan soal komunikasi pemangku kepentingan di bab 10.16: sumbu terpotong pada grafik kesehatan publik dapat memanikkan atau keliru menenangkan jutaan orang, dan aksesibilitas adalah kewajiban hukum, bukan preferensi. Desain visualisasi yang baik adalah cara data memperoleh hak untuk dipercaya.

## Prinsip utama

- Mulailah dari pertanyaan yang dimiliki pembaca, lalu pilih bagan yang menjawabnya.
- Cocokkan encoding visual dengan jenis data: posisi untuk perbandingan presisi, rona untuk kategori.
- Maksimalkan bagian tinta yang membawa data; hapus dekorasi yang tak membawa apa pun.
- Gunakan atribut pra-perhatian dengan sengaja agar mata mendarat pada titik itu lebih dulu.
- Pilih palet menurut peran data (sekuensial, divergen, kategorikal) dan jaga tetap aman bagi buta warna.
- Jangan pernah bergantung pada warna saja; sediakan teks, struktur, dan cadangan tabel.
- Katakan kebenaran tentang skala: tanpa sumbu terpotong, tanpa area menyesatkan, tanpa dual axis tak perlu.
- Anotasi wawasannya; jangan membuat pembaca memburunya.

## Rekomendasi

### Mulai dari pertanyaan, lalu pilih bagan

Setiap bagan yang baik dimulai dengan pertanyaan, bukan dataset. Sebelum Anda meraih jenis bagan, namai pertanyaan pembaca dalam satu kalimat, lalu cocokkan dengan tugas. Perbandingan ("mana yang lebih besar?") menginginkan [diagram batang](https://en.wikipedia.org/wiki/Bar_chart), di mana panjang berada pada garis dasar bersama dan mata memeringkatnya tanpa upaya. Tren seiring waktu ("ke arah mana ini bergerak?") menginginkan [diagram garis](https://en.wikipedia.org/wiki/Line_chart), karena garis tersambung terbaca sebagai perubahan berkelanjutan. Distribusi ("bagaimana ia tersebar?") menginginkan histogram atau box plot, yang menunjukkan bentuk, pusat, dan pencilan. Bagian-terhadap-keseluruhan ("berapa pangsa setiap potong?") biasanya lebih baik dilayani batang bertumpuk daripada pai, karena orang membandingkan panjang jauh lebih akurat daripada sudut; sisihkan [diagram pai](https://en.wikipedia.org/wiki/Pie_chart) untuk dua atau tiga potong di mana pembagian itu seluruh ceritanya. Hubungan ("apakah keduanya bergerak bersama?") menginginkan [diagram sebar](https://en.wikipedia.org/wiki/Scatter_plot), satu-satunya bagan yang mengungkap korelasi dan gugus sekilas.

Disiplinnya adalah membiarkan pertanyaan memilih bagan, tidak pernah sebaliknya. Jenis bagan yang dipilih karena tampak mengesankan (pai 3D meledak, diagram radar, donat dengan angka di lubangnya) adalah keputusan yang dibuat demi desainer, bukan pembaca. Ketika tabel akan menjawab pertanyaan lebih cepat (pembaca yang butuh angka eksak untuk empat baris tidak butuh bagan sama sekali), pakai tabel. Bagan dibenarkan hanya ketika gambar mengungkap pola yang akan disembunyikan digit pada grid.

### Cocokkan encoding visual dengan data

Bagan bekerja dengan memetakan data ke properti visual, dan properti itu tidak setara. Puluhan tahun riset persepsi memeringkatkannya. Posisi sepanjang skala bersama adalah kanal paling akurat yang dimiliki manusia, itulah mengapa batang dan titik pada sumbu bersama mengalahkan yang lain untuk perbandingan. Panjang berikutnya, lalu sudut dan kemiringan, lalu area, lalu intensitas warna, dan terakhir rona, yang nyaris tak berguna untuk menilai kuantitas tetapi unggul untuk melabeli kategori. Belanjakan kanal paling presisi Anda pada kuantitas terpenting Anda.

Cocokkan kanal dengan jenis data juga. Data kuantitatif (hitungan, jumlah, durasi) termasuk pada posisi, panjang, atau ramp warna sekuensial. Data ordinal (kecil, sedang, besar) dapat memakai ukuran berurutan atau ramp terang-ke-gelap. Data kategorikal (wilayah, lini produk, partai) termasuk pada rona atau bentuk, tidak pernah pada ukuran yang menyiratkan satu kategori "lebih" dari yang lain. Kesalahan klasik adalah meng-encode kategori sebagai pelangi sehingga mata pembaca menciptakan urutan yang tak dimiliki data. Encode kuantitas di tempat mata membaca kuantitas, dan identitas di tempat mata membaca identitas.

### Kejar keunggulan grafis: maksimalkan data-ink

Edward Tufte memberi visualisasi etika desain paling jelas, dan layak diinternalisasi. Ukuran pusatnya adalah [rasio data-ink](https://en.wikipedia.org/wiki/Data-ink_ratio): dari semua tinta (atau piksel) di halaman, berapa pecahan yang benar-benar meng-encode data? Segala yang lain (garis grid tebal, batas berkotak, bayangan, isian latar, legenda redundan, 3D dekoratif) adalah pajak atas perhatian pembaca. Tufte menyebut dekorasi ini chartjunk, dan instruksinya blak-blakan: hapus. Ringankan garis grid sampai berbisik, buang batas bagan, labeli data langsung alih-alih memaksa perjalanan ke legenda, dan biarkan data berdiri hampir sendirian. Bagan selesai bukan ketika tak ada lagi yang dapat ditambah melainkan ketika tak ada lagi yang dapat dihapus tanpa kehilangan makna.

Satu gagasan Tufte layak disebut khusus untuk tim: small multiples. Alih-alih menjejalkan delapan seri ke satu diagram garis kusut, gambar delapan bagan kecil dalam grid, masing-masing dengan sumbu dan skala sama, satu per seri. Mata memindai grid dan melihat yang janggal seketika, karena setiap panel dapat langsung dibandingkan. Small multiples mengubah "terlalu banyak garis untuk dibaca" menjadi "halaman yang dapat dipindai," dan berskala jauh lebih baik daripada menumpuk lebih banyak warna dan entri legenda pada satu plot yang kelebihan beban.

### Gunakan atribut pra-perhatian dan hierarki visual

Beberapa perbedaan visual terdaftar sebelum perhatian sadar, dalam pecahan detik, tanpa pembaca "mencarinya." Atribut pra-perhatian ini (satu titik merah di antara yang abu-abu, satu batang lebih panjang, satu butir diletakkan terpisah dalam ruang) adalah perkakas paling ampuh yang Anda punya untuk mengarahkan mata. Pakai dengan sengaja. Jika inti bagan adalah satu wilayah tertinggal, warnai wilayah itu dan abu-abukan sisanya; pembaca melihat pesan sebelum membaca judul. Jika segalanya cerah dan tebal, tak ada yang demikian, karena kontras bersifat relatif dan halaman penuh penekanan adalah halaman penuh derau.

Inilah hierarki visual yang diterapkan pada data: putuskan satu hal yang harus diperhatikan pembaca lebih dulu, dan belanjakan sinyal terkuat Anda di sana. Judul dan anotasi menyatakan intisari dalam kata. Warna dan bobot menunjuk ke bukti. Segala yang mendukung (sumbu, garis grid, seri sekunder) mundur ke abu-abu agar latar depan dapat berbicara. Bagan tanpa hierarki meminta pembaca melakukan pekerjaan desainer mencari tahu apa yang penting.

### Pilih warna menurut peran, dan jadikan aman bagi buta warna

Warna adalah kanal yang paling sering disalahgunakan, jadi perlakukan sebagai sistem dengan tiga keluarga. Palet sekuensial berjalan terang ke gelap dalam satu rona dan meng-encode kuantitas yang berjalan dari rendah ke tinggi (kepadatan penduduk, pendapatan). Palet divergen punya dua rona bertemu di titik tengah netral dan meng-encode deviasi dari pusat (anomali suhu, untung dan rugi di sekitar nol, kesepakatan survei di sekitar netral). Palet kategorikal adalah himpunan rona berbeda untuk melabeli kelompok tanpa urutan; jaga sekitar tujuh warna, karena melebihi itu pembaca tidak dapat membedakannya. Memilih keluarga yang salah (pelangi kategorikal untuk kuantitas, ramp sekuensial untuk kategori tak berurutan) melawan persepsi pembaca.

Lalu jadikan dapat diakses, karena kira-kira satu dari dua belas pria punya bentuk [buta warna](https://en.wikipedia.org/wiki/Color_blindness). Merah dan hijau adalah jebakan klasik: bagan merah-buruk hijau-baik tak terlihat oleh defisiensi paling umum. Pilih palet aman bagi buta warna (skema divergen biru-ke-oranye dan himpunan kategorikal teruji baik dari perkakas seperti ColorBrewer adalah titik awal aman), dan verifikasi dengan mensimulasikan defisiensi umum sebelum dikirim. Periksa kontras juga, agar teks dan tanda memenuhi rasio yang dituntut standar aksesibilitas di bab 5.3. Warna harus memperkuat pesan yang sudah selamat tanpanya.

### Jangan bergantung pada warna saja; sediakan alternatif

Aksesibilitas dalam data viz melampaui pilihan palet. Aturan inti dari [Web Content Accessibility Guidelines](https://en.wikipedia.org/wiki/Web_Content_Accessibility_Guidelines) (WCAG) adalah warna tidak boleh menjadi satu-satunya cara informasi disampaikan. Jadi padukan warna dengan isyarat kedua: label langsung, bentuk atau penanda berbeda pada diagram sebar, gaya garis berbeda (padat, putus-putus) pada diagram garis, atau label teks pada batang penting. Pembaca yang tidak dapat membedakan rona Anda tetap harus mendapat pesan penuh dari encoding redundan.

Sediakan alternatif teks yang sejati dan cadangan. Citra bagan butuh teks alt yang menyatakan intisari, bukan "bagan penjualan," dan deskripsi lebih panjang atau keterangan yang menamai tren. Di mana praktis, tawarkan data dasar sebagai tabel yang dapat diakses, agar pengguna pembaca layar dan analis berpikiran spreadsheet sama-sama mendapat angka langsung. Ini mencerminkan disiplin "selesaikan sekali dalam komponen" bab 5.2: bangun komponen bagan yang dapat diakses dengan peran yang tepat, fokus keyboard untuk elemen interaktif, dan tampilan tabel bawaan, agar setiap tim mewarisi aksesibilitas alih-alih menciptakannya ulang per dasbor.

### Ketahui apakah Anda menjelajahi, menjelaskan, atau memantau

Bagan melayani tiga tugas berbeda, dan mencampuradukkannya menghasilkan kerja buruk. Visualisasi eksploratif untuk Anda, analis, memburu data untuk apa yang menarik; boleh cepat, padat, dan jelek, karena audiensnya satu ahli yang akan beriterasi. Visualisasi penjelas untuk audiens, mengomunikasikan temuan spesifik yang sudah Anda pahami; ia disengaja, dianotasi, dan dilucuti menjadi satu pesan, dan termasuk dalam penceritaan bab 10.16. Dasbor adalah hal ketiga: tampilan persisten dan dapat dilihat sekilas untuk memantau metrik yang diketahui seiring waktu, dioptimalkan untuk "adakah yang salah sekarang?" alih-alih argumen sekali jalan.

Cocokkan desain dengan tugas. Bagan penjelas dengan judul dan satu seri yang disorot salah untuk dasbor pemantauan, di mana pembaca butuh banyak metrik sekilas dan penempatan konsisten agar mata mereka mempelajari tata letak. Dasbor yang dijejali anotasi naratif melelahkan diperiksa setiap pagi. Dan notebook eksploratif penuh plot mentah tidak boleh diserahkan kepada eksekutif seolah ia penjelasan. Putuskan tugasnya lebih dulu; desain mengikuti.

### Jangan menyesatkan: skala jujur, area jujur

Cara tercepat menghancurkan kepercayaan adalah bagan yang berdusta sambil tampak jujur. Dusta paling umum adalah sumbu terpotong: memulai sumbu-y diagram batang pada 90 alih-alih 0 mengubah perbedaan 2% menjadi tebing, karena panjang batang tak lagi memetakan nilai. Batang harus mulai dari nol, selalu; diagram garis, yang meng-encode perubahan alih-alih besaran, boleh memakai garis dasar bukan-nol jika Anda melabelinya dengan jelas. Jebakan kedua adalah dual axis: dua skala-y pada satu bagan memungkinkan Anda memproduksi korelasi apa pun yang Anda suka dengan menggeser skala, dan pembaca jarang menyadarinya. Pilih dua bagan sejajar atau tampilan terindeks sebagai gantinya. Ketiga adalah area menyesatkan: ketika Anda menskalakan ikon atau gelembung menurut lebar dan tinggi untuk merepresentasikan nilai, area tumbuh sebagai kuadrat dan melebih-lebihkan perbedaan secara liar; skalakan menurut area, bukan panjang sisi.

Perlakukan ini sebagai aturan integritas, bukan preferensi gaya. Bagan adalah klaim yang Anda minta dipercaya pembaca, dan setiap distorsi ini mengeksploitasi cara persepsi bekerja untuk membuat hal kecil tampak besar atau hal tak terkait tampak terhubung. Contoh pemerintah dan enterprise di bawah menunjukkan betapa mahalnya pengkhianatan itu ketika audiensnya publik atau dewan.

### Anotasi wawasan dan tambah interaktivitas dengan menahan diri

Bagan yang membuat pembaca menemukan intinya baru separuh selesai. Anotasi: judul yang menyatakan temuan ("Pendaftaran berlipat dua setelah peluncuran Maret") alih-alih topik ("Pendaftaran seiring waktu"), callout pada peristiwa kunci, garis rujukan untuk target atau rata-rata. Anotasi adalah tempat desain bab 5.4 bertemu gambar; kata membawa argumen dan tanda memberikan bukti.

Interaktivitas layak tempatnya hanya ketika menjawab pertanyaan lanjutan nyata. Tooltip untuk nilai eksak, pemfilteran ke segmen, dan drill-down ke detail semuanya membantu ketika pembaca punya pertanyaan berikutnya yang tidak dapat ditampung bagan statis. Tetapi interaktivitas adalah biaya: ia menyembunyikan informasi di balik hover, gagal pada sentuhan dan bagi pengguna keyboard, dan dapat menyeret kinerja merayap. Di web, awasi anggaran render dari bab 5.6: puluhan ribu titik menginginkan canvas atau tampilan teragregasi, bukan puluhan ribu elemen dokumen individual. Jadikan tampilan statis bawaan menceritakan seluruh kisah inti, dan biarkan interaksi mengungkap kedalaman di bawahnya.

## Trade-off: kelebihan dan kekurangan

| Keputusan | Kelebihan | Kekurangan |
|---|---|---|
| Bangun viz di produk Anda | Kendali penuh atas desain, aksesibilitas, interaksi | Memakan waktu rekayasa; Anda memiliki kinerja dan pemeliharaan |
| Pakai bagan perkakas BI | Cepat, murah, terhubung ke gudang | Tampilan generik; kendali aksesibilitas dan anotasi terbatas |
| Bagan interaktif | Menjawab pertanyaan lanjutan; menjelajah di tempat | Lebih lambat, lebih sulit dibuat dapat diakses, gagal pada cetak dan sentuhan |
| Bagan statis | Cepat, dapat diakses, siap cetak, tak ambigu | Tidak dapat menjawab pertanyaan berikutnya pembaca |
| Dasbor | Pemantauan sekilas banyak metrik yang diketahui | Buruk untuk argumen sekali jalan; menggoda sebaran metrik |
| Bagan penjelas | Menyampaikan satu pesan dengan kekuatan | Salah untuk pemantauan atau eksplorasi terbuka |
| Warna dan efek kaya | Menarik mata; terasa dipoles | Chartjunk; merugikan rasio data-ink dan aksesibilitas |

Ketegangan yang berulang adalah ekspresivitas versus kejujuran dan kejelasan. Setiap fitur yang membuat bagan lebih kaya (sumbu kedua, gradien warna, perspektif 3D, animasi) juga menambah cara menyesatkan atau mengubur intinya. Selesaikan dengan bawaan lebih sedikit: bagan paling sederhana yang menjawab pertanyaan, dalam warna paling sedikit, dengan skala yang menyatakan kebenaran. Tambahkan ekspresivitas hanya ketika pertanyaan pembaca spesifik menuntutnya, dan bayar biaya aksesibilitas dan kinerja dengan sadar. Trade-off tetap lainnya adalah bangun versus beli. Perkakas BI mendapatkan bagan di layar dalam menit dan pilihan tepat untuk pemantauan internal; viz yang tertanam dalam produk yang menghadap pelanggan biasanya membutuhkan kendali desain, aksesibilitas, dan kinerja yang hanya diberikan komponen khusus.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apakah bagan kita berbagi satu bahasa visual, atau setiap tim menciptakan sendiri?** Ketika setiap skuad memilih warna, konvensi sumbu, pembulatan, dan jenis bagannya sendiri, organisasi mengumpulkan dialek yang diam-diam merusak kepercayaan: dua dasbor yang menampilkan "pengguna aktif" dengan skala berbeda dan hijau berbeda mengajari eksekutif bahwa data tak dapat diandalkan. Bawa tiga bagan dari metrik yang sama dari tiga tim dan letakkan berdampingan. Celah yang Anda temukan (sumbu terpotong di sini, pelangi kategori di sana, pendapatan dalam ribuan di satu dan jutaan di yang lain) adalah argumen untuk pustaka komponen bagan bersama dengan palet yang disepakati, aturan sumbu bawaan, dan aksesibilitas bawaan, diatur seperti sistem desain di bab 5.2. Tujuannya bagan apa pun di perusahaan terbaca dengan benar sekilas, karena tata bahasanya bersama.

2. **Akankah bagan terpenting kita selamat dari pembaca buta warna dan pembaca layar?** Aksesibilitas dalam data viz mudah dilewatkan karena bagan masih tampak baik bagi orang yang membangunnya, dan itulah persis jebakannya. Ambil tiga bagan yang paling sering dilihat pimpinan Anda dan jalankan melalui simulator buta warna, lalu coba pahami dengan layar mati, hanya memakai teks alt dan cadangan tabel apa pun. Jika bagan status merah-hijau menjadi datar, jika teks alt mengatakan "bagan" dan tidak lebih, atau jika tak ada cara menjangkau angka dasar tanpa mouse, Anda telah menemukan kelompok pembaca yang saat ini Anda kecualikan, yang dalam kerja sektor publik adalah paparan hukum di bawah standar bab 5.3. Putuskan siapa yang memiliki perbaikan dan apakah perbaikan itu termasuk dalam komponen bersama agar diselesaikan sekali.

3. **Untuk setiap bagan yang menggerakkan keputusan, dapatkah kita menunjuk pertanyaan yang dijawabnya dan memastikan ia tidak menyesatkan?** Banyak bagan ada karena seseorang pernah membuatnya, bukan karena menjawab pertanyaan hidup, dan sebagian yang paling banyak ditonton mendistorsi skala tanpa disadari siapa pun. Telusuri bagan di dasbor utama Anda dan, untuk masing-masing, namai keputusan yang diinformasikannya dan periksa integritasnya: batang dari nol, tanpa dual axis tak perlu, area diskalakan jujur, judul yang menyatakan temuan alih-alih topik. Bagan yang tak menjawab pertanyaan saat ini adalah kandidat untuk dihapus, dan yang menyesatkan kandidat untuk perbaikan mendesak, karena bagan yang diam-diam melebih-lebihkan perbedaan lebih buruk daripada tanpa bagan sama sekali. Ini terhubung langsung dengan budaya keputusan bab 7.5: tim yang memercayai bagannya membuat keputusan lebih cepat dan lebih berlandaskan.

4. **Ketika tim membutuhkan bagan, apakah kita pertama-tama meraih bagan bawaan perkakas BI atau pustaka komponen yang diatur, dan siapa yang memutuskan mana?** Tarikan ke perkakas BI nyata: cepat, murah, dan sudah tersambung ke gudang, jadi sebagian besar dasbor pemantauan termasuk di sana. Tetapi bawaan generiknya adalah tempat dialek dan chartjunk merayap masuk, dan kendali aksesibilitas serta anotasinya biasanya lemah, yang paling penting untuk bagan yang menghadap pelanggan dan publik yang membawa reputasi Anda. Bagi organisasi besar bahayanya bawaan tak pernah diputuskan, sehingga setiap tim hanyut ke apa pun yang paling mudah dan properti terfragmentasi. Bawa inventaris di mana bagan benar-benar dibangun hari ini, beberapa contoh berdampingan dari perkakas BI versus komponen khusus, dan celah aksesibilitas pada masing-masing. Dalam pengaturan enterprise dan pemerintah, masukkan kenyataan pengadaan: Anda sering terkunci pada satu platform BI selama bertahun-tahun, jadi ketahui persis bagan mana yang dapat dirender dengan jujur dan dapat diakses dan mana yang butuh komponen yang diatur, sebelum kontrak, bukan sesudah.

5. **Siapa yang diizinkan menerbitkan bagan ke audiens eksternal atau eksekutif, dan tinjauan apa yang dilaluinya lebih dulu?** Analitik swalayan adalah kebaikan sejati, tetapi itu berarti bagan menyesatkan dapat mencapai dewan atau publik tanpa pasang mata kedua, dan sumbu terpotong atau lonjakan tak berlabel pada grafik publik jauh lebih sulit diurai daripada dicegah. Ketegangannya otonomi dan kecepatan melawan integritas dan kepercayaan: gerbangi terlalu keras dan orang menyiasati Anda, gerbangi terlalu sedikit dan Anda mengirim bagan yang memanikkan pasar atau konstituen. Bawa jalur penerbitan saat ini untuk bagan paling terlihat Anda, contoh yang mencapai audiens luar tanpa tinjauan, dan bukti apakah metode dan ketidakpastian dianotasi pada bagan itu sendiri. Dalam kerja sektor publik dan teregulasi ini akut: statistik resmi adalah komunikasi dengan warga dan soal kepercayaan pemangku kepentingan di bab 10.16, jadi namai siapa yang menyetujui, daftar periksa integritas dan aksesibilitas apa yang mereka terapkan, dan di mana akuntabilitas berada ketika bagan menyesatkan.

6. **Di mana kita telah menambah interaktivitas, dan apakah tampilan statis bawaan masih menceritakan seluruh kisah tanpa mouse?** Interaktivitas menggoda dan mahal: ia menyembunyikan nilai di balik hover, patah pada sentuhan dan bagi pengguna keyboard, dan dapat menyeret anggaran render merayap pada dataset besar, sebagaimana diperingatkan bab 5.6. Pertimbangan yang bersaing adalah bahwa pertanyaan lanjutan nyata (nilai eksak, drill-down, segmen yang difilter) kadang layak biayanya, sehingga tujuannya menahan diri alih-alih larangan. Bawa daftar bagan interaktif yang Anda kirim, hasil mencoba masing-masing dengan mouse dijauhkan dan di ponsel, dan angka kinerja ketika data tumbuh menjadi puluhan ribu titik. Untuk audiens enterprise dan pemerintah sudut aksesibilitas adalah kewajiban hukum di bawah standar bab 5.3, dan bagan dibaca di kios, cetakan, dan teknologi bantu, sehingga bawaan statis yang dianotasi harus membawa pesan inti dan interaksi hanya dapat menambah kedalaman di bawahnya.

## Lensa sektor

**Startup.** Kecepatan menang, jadi bersandarlah pada bagan yang sudah ada dalam perkakas BI Anda atau pustaka bagan ringan alih-alih membangun properti komponen viz yang tak sanggup Anda isi stafnya. Satu keputusan murah yang membayar belakangan adalah memilih satu palet aman bagi buta warna dan kebiasaan batang-dari-nol pada hari pertama, agar Anda tidak menumpuk selusin dialek metrik yang sama sebelum punya sepuluh pelanggan. Pilih bagan statis yang dianotasi yang menyatakan temuannya daripada yang interaktif yang tak akan sempat Anda jadikan dapat diakses.

**Bisnis kecil.** Tanpa spesialis data dan dengan anggaran ketat, perlakukan visualisasi sebagai sesuatu yang Anda dapat dari perkakas yang sudah Anda bayar: spreadsheet, SaaS analitik, dasbor di CRM Anda. Pelajari segelintir aturan integritas yang penting (batang mulai dari nol, tanpa pelangi untuk kuantitas, tanpa pai dengan sembilan potong) dan terapkan palet aman bagi buta warna siap pakai alih-alih memesan yang khusus. Beli bagan, jangan bangun, dan sisihkan perhatian Anda untuk membacanya dengan benar.

**Enterprise.** Masalahnya konsistensi lintas banyak tim, jadi atur visualisasi seperti sistem desain: pustaka komponen bagan bersama dengan palet sekuensial, divergen, dan kategorikal yang disepakati, bawaan sumbu jujur, pemformatan angka standar, dan aksesibilitas tertanam. Tegakkan dengan pemeriksaan regresi visual dan integritas dalam pipeline pengiriman bab 8.1, agar bagan yang memotong sumbu atau gagal kontras diblokir sebelum dikirim. Imbalannya bagan dari tim mana pun terbaca dengan benar sekilas dan pimpinan berhenti bertanya versi angka mana yang harus dipercaya.

**Pemerintah.** Setiap bagan publik adalah tindakan komunikasi dan tunduk pada akuntabilitas publik, sehingga skala jujur dan aksesibilitas WCAG adalah kewajiban, bukan preferensi. Wajibkan batang dari nol, area di-encode oleh area, palet aman bagi buta warna, judul bahasa sederhana yang menyatakan temuan, dan tabel yang dapat diunduh dan diakses di samping setiap bagan. Anotasi metode dan ketidakpastian pada bagan itu sendiri agar angka kontroversial tidak dapat direduksi menjadi judul menyesatkan, dan pastikan perkakas BI apa pun yang Anda beli dapat memenuhi standar ini, karena kewajiban itu milik Anda terlepas dari vendor.

## Contoh

**Startup.** Startup analitik sepuluh orang merilis dasbor pemakaian yang menghadap pelanggan. Versi pertama memakai tema bawaan perkakas BI: pelangi warna kategori, garis grid di mana-mana, dan diagram pai dengan sembilan potong yang tak dapat dibaca siapa pun. Pengguna mengeluh angkanya terasa tak tepercaya. Tim membangun ulangnya sebagai komponen tertanam dengan palet kecil aman bagi buta warna, mengganti pai dengan diagram batang terurut, meringankan garis grid, dan menambah label langsung agar legenda lenyap. Mereka menetapkan judul yang menyatakan temuan dan menambah teks alt serta tombol tabel ke setiap bagan. Keterlibatan dengan dasbor naik karena pelanggan akhirnya dapat membacanya sekilas, dan desain yang lebih bersih menjadi nilai jual dalam demo.

**Enterprise.** Sebuah bank multinasional punya ratusan dasbor internal yang dibangun puluhan tim, masing-masing dengan warna dan kebiasaan sumbu sendiri, dan eksekutif rutin tidak memercayainya karena metrik yang sama tampak berbeda di setiap dek. Perusahaan memperkenalkan pustaka bagan terkelola di atas platform BI-nya: palet sekuensial, divergen, dan kategorikal yang disepakati; aturan tegas bahwa sumbu batang mulai dari nol; pemformatan angka standar; dan aksesibilitas tertanam dalam setiap komponen. Pemeriksaan regresi visual dalam pipeline pengiriman bab 8.1 memblokir bagan yang melanggar standar. Dalam setahun, bagan dari tim mana pun terbaca dengan benar sekilas, dan pimpinan berhenti bertanya "versi angka ini mana yang harus saya percaya?"

**Pemerintah.** Sebuah badan statistik nasional menerbitkan data publik tentang ekonomi, kesehatan, dan penduduk, dan bagannya dibaca wartawan, pembuat kebijakan, dan warga yang tak dapat memverifikasi angka dasarnya. Badan memperlakukan setiap bagan sebagai komunikasi dengan publik dan soal kepercayaan pemangku kepentingan di bab 10.16. Ia mewajibkan skala jujur (batang dari nol, tanpa dual axis menyesatkan, area di-encode oleh area), palet divergen aman bagi buta warna untuk perbandingan wilayah, judul bahasa sederhana yang menyatakan temuan, dan tabel yang dapat diunduh dan diakses di samping setiap bagan untuk memenuhi WCAG. Ketika angka kontroversial diterbitkan, anotasi menjelaskan metode dan ketidakpastian pada bagan itu sendiri, sehingga sumbu terpotong atau lonjakan tak berlabel tak pernah dapat menjadi judul menyesatkan yang mengikis kepercayaan publik.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil desain visualisasi yang baik adalah keputusan lebih cepat dan lebih baik serta lebih sedikit kesalahan mahal. Dasbor yang mengungkap masalah sekilas memperpendek waktu dari sinyal ke tindakan, dan bagan yang menyatakan kebenaran mencegah anggaran mengejar ilusi yang diproduksi sumbu terpotong. Keuntungan ini sulit ditaruh pada faktur, tetapi nyata: setiap rapat pimpinan yang dihabiskan berdebat bagan mana yang dipercaya, setiap strategi yang dibangun di atas tren yang salah baca, dan setiap pelanggan yang churn karena analitik produk Anda tak terbaca adalah biaya yang dihapus desain jelas. Di mana bagan menggerakkan uang nyata, seperti dalam contoh bank, nilai angka tepercaya jauh melampaui biaya membangunnya dengan baik.

Biaya adopsi sebagian besar sekali jalan dan bersama. Anda mendefinisikan palet, aturan sumbu dan pemformatan, serta bawaan aksesibilitas yang disepakati, lalu menyandikannya dalam pustaka komponen bagan agar tim mewarisinya alih-alih memutuskan ulang per dasbor. Biaya kepemilikan berkelanjutan nyata tetapi sederhana: memelihara pustaka, menjaganya dapat diakses seiring standar berevolusi, dan menahan sebaran bagan khusus sekali pakai. Biaya pengabaian berlipat diam-diam: bagan yang tidak konsisten, menyesatkan, dan tak dapat diakses mengikis kepercayaan pada semua data Anda, mengundang risiko hukum dalam pengaturan teregulasi dan sektor publik, dan mendorong orang kembali ke spreadsheet mentah, yang membuang seluruh investasi pada tumpukan analitik bab 7.3. Untuk mengajukan kasus kepada pimpinan, kaitkan kualitas visualisasi dengan hasil yang sudah mereka lacak: kecepatan keputusan, kepercayaan pada pelaporan, dan, di sektor publik, kepatuhan aksesibilitas.

## Anti-pola dan jebakan

- **Sumbu batang terpotong:** memulai batang di atas nol sehingga perbedaan kecil tampak seperti jurang; dusta bagan tunggal paling umum.
- **Dual axis tak perlu:** dua skala-y pada satu bagan, bergeser untuk memproduksi korelasi apa pun yang ingin ditunjukkan penulis.
- **Area menyesatkan:** menskalakan ikon atau gelembung menurut panjang sisi sehingga areanya, dan nilai yang dipersepsikan, tumbuh sebagai kuadrat.
- **Pelangi untuk kuantitas:** meng-encode kuantitas berurutan dengan rona kategorikal tak berurutan, sehingga mata tidak dapat membaca besaran.
- **Pai dengan banyak potong:** lebih dari tiga potong, memaksa pembaca membandingkan sudut yang tak dapat mereka nilai; pakai batang terurut.
- **Chartjunk:** garis grid tebal, batas, 3D, dan bayangan yang menurunkan rasio data-ink dan mengubur sinyal.
- **Warna sebagai satu-satunya isyarat:** status merah-hijau tanpa label atau bentuk, tak terlihat oleh pembaca buta warna dan pembaca layar.
- **Memburu legenda:** memaksa perjalanan ke legenda yang jauh di tempat label langsung pada garis atau batang sudah cukup.
- **Segalanya ditekankan:** setiap seri tebal dan cerah, sehingga kontras runtuh dan tak ada yang menonjol.
- **Bagan di tempat tabel menang:** gambar untuk empat angka eksak yang perlu dibaca pembaca dengan presisi.

## Model kematangan

- **Tingkat 1, Memulai:** Bagan dibuat ad hoc di perkakas apa pun yang ada. Warna, sumbu, dan format bervariasi menurut penulis, sumbu terpotong dan kategori pelangi lazim, aksesibilitas tak dipertimbangkan, dan pembaca tidak memercayai hasilnya.
- **Tingkat 2, Mengembangkan:** Beberapa tim mengadopsi praktik dasar, tetapi tidak konsisten di seluruh organisasi. Batang mulai dari nol di beberapa tempat, chartjunk yang nyata dicegah dalam tinjauan, dan palet rumah ada pada beberapa tim, namun tim lain di ujung lorong masih mengirim pai sembilan potong dan bagan status merah-hijau.
- **Tingkat 3, Membakukan:** Pustaka komponen bagan bersama menyandikan palet sekuensial, divergen, dan kategorikal yang disepakati, aturan sumbu jujur, pemformatan standar, dan aksesibilitas (aman bagi buta warna, teks alt, cadangan tabel). Standar terdokumentasi dan ditegakkan di seluruh organisasi, dan pemakaian eksploratif, penjelas, dan dasbor dibedakan secara desain.
- **Tingkat 4, Mengelola:** Kualitas visualisasi diukur dan dikendalikan terhadap garis dasar. Pemeriksaan aksesibilitas dan integritas bagan berjalan dalam pipeline pengiriman dan melaporkan tingkat lulus; bagian bagan dengan batang dari nol, warna patuh kontras, dan cadangan tabel dilacak sebagai metrik; pemahaman diuji dengan pembaca nyata terhadap garis dasar; dan jumlah dialek berbeda setiap metrik kunci diawasi seiring cenderung menuju satu. Bagan yang melanggar standar tertangkap sebelum rilis, dan angka, bukan opini, menggerakkan di mana pustaka butuh kerja.
- **Tingkat 5, Mengorkestrasi:** Visualisasi terus diperbaiki dan terintegrasi di seluruh organisasi. Standar beradaptasi seiring persyaratan aksesibilitas dan kebutuhan pembaca berubah, palet, komponen, dan konvensi diperhalus dari bukti terukur, anotasi dan narasi adalah norma, dan praktik dijalin ke budaya analitik dan keputusan sehingga bagan dari tim mana pun terbaca dengan benar sekilas dan bahasa visual berevolusi seiring organisasi belajar.

## Gagasan untuk didiskusikan

1. Bagan mana di dasbor utama Anda yang akan tampak berbeda jika sumbunya dimulai dari nol, dan apakah itu mengubah ceritanya?
2. Pilih bagan terpenting Anda: apakah pesannya selamat dalam skala abu-abu, dan jika tidak, isyarat redundan apa yang akan memperbaikinya?
3. Di mana Anda memakai bagan interaktif padahal bagan statis yang dianotasi akan menceritakan seluruh kisah lebih cepat?
4. Apakah judul bagan Anda menyatakan temuan atau topik, dan siapa yang akan menyadari jika angka judul diam-diam berbalik?
5. Bagan Anda yang mana yang tak menjawab keputusan saat ini, dan apa yang diperlukan untuk menghapusnya tanpa ada yang merasa kehilangan?
6. Kapan tim harus membangun viz di produk versus memakai perkakas BI, dan apakah Anda punya aturan tertulis untuk memilih?

## Poin-poin utama

- Mulailah dari pertanyaan pembaca, lalu pilih bagan: batang untuk perbandingan, garis untuk tren, sebar untuk hubungan, histogram untuk distribusi, batang terurut daripada pai untuk bagian-terhadap-keseluruhan.
- Cocokkan encoding dengan data: belanjakan posisi dan panjang pada kuantitas terpenting Anda, dan pakai rona untuk kategori, tidak pernah untuk besaran.
- Kejar keunggulan grafis: maksimalkan rasio data-ink, hapus chartjunk, pakai small multiples, dan arahkan mata dengan kontras pra-perhatian dan hierarki jelas.
- Perlakukan warna sebagai sistem (sekuensial, divergen, kategorikal), jaga aman bagi buta warna, dan jangan pernah bergantung pada warna saja; sediakan label, teks alt, dan cadangan tabel.
- Katakan kebenaran tentang skala (batang dari nol, area jujur, tanpa dual axis tak perlu), anotasi wawasannya, dan tambahkan interaktivitas hanya ketika pertanyaan lanjutan nyata menuntutnya.

## Referensi dan bacaan lanjutan

- Edward R. Tufte, *The Visual Display of Quantitative Information*
- Edward R. Tufte, *Envisioning Information*
- Stephen Few, *Show Me the Numbers: Designing Tables and Graphs to Enlighten*
- Stephen Few, *Information Dashboard Design: Displaying Data for At-a-Glance Monitoring*
- Cole Nussbaumer Knaflic, *Storytelling with Data: A Data Visualisation Guide for Business Professionals*
- Alberto Cairo, *The Truthful Art: Data, Charts, and Maps for Communication*
- Alberto Cairo, *How Charts Lie: Getting Smarter about Visual Information*
- William S. Cleveland, *The Elements of Graphing Data*
- Jacques Bertin, *Semiology of Graphics: Diagrams, Networks, Maps*
- Tamara Munzner, *Visualisation Analysis and Design*
- Cynthia A. Brewer, ColorBrewer: Colour Advice for Cartography (colorbrewer2.org)
- World Wide Web Consortium (W3C), *Web Content Accessibility Guidelines (WCAG) 2.2*
