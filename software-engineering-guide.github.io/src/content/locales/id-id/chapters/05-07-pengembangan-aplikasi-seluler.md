# 5.7 Pengembangan aplikasi seluler

## Tinjauan dan motivasi

[Pengembangan aplikasi seluler](https://en.wikipedia.org/wiki/Mobile_app_development) adalah disiplin membangun perangkat lunak untuk ponsel dan tablet. Bagi banyak orang, ponsel kini komputer utama atau satu-satunya yang mereka miliki. Itu menjadikan aplikasi seluler pintu depan layanan Anda, dan sering permukaan tempat pengguna menilai seluruh organisasi Anda.

Seluler adalah lingkungan rekayasa yang berbeda, bukan versi kecil dari web atau desktop. Perangkat berjalan di saku, pada baterai, melalui koneksi yang datang dan pergi. Layarnya kecil. Sistem operasi mengendalikan apa yang boleh dilakukan aplikasi Anda. Dua platform dominan ada ([iOS](https://en.wikipedia.org/wiki/IOS) dari Apple dan [Android](https://en.wikipedia.org/wiki/Android_%28operating_system%29) dari Google), masing-masing dengan bahasa, aturan desain, dan tokonya sendiri. Anda tidak bisa sekadar merilis pembaruan kapan pun Anda suka, karena toko meninjaunya lebih dulu, dan pengguna memilih kapan memasangnya. Bab ini bertumpu pada rekayasa frontend (bab 5.6), fondasi UX (bab 5.1), dan aksesibilitas (bab 5.3), dan bersandar pada keamanan aplikasi (bab 4.2) serta CI/CD dan pengiriman (bab 8.1).

Relevansi enterprise dan pemerintah tinggi. Enterprise merilis aplikasi pelanggan dan aplikasi internal untuk tenaga kerja mereka sendiri, sering dikelola lewat [manajemen perangkat seluler](https://en.wikipedia.org/wiki/Mobile_device_management) (MDM: perangkat lunak pusat yang mengonfigurasi dan mengamankan perangkat perusahaan). Pemerintah membangun aplikasi untuk warga untuk tunjangan, kesehatan, identitas, dan pembayaran, dan harus melayani semua orang, termasuk orang pada perangkat lama dan koneksi lambat, di bawah hukum aksesibilitas. Dalam kedua pengaturan, seluler adalah komitmen serius dan berumur panjang, jadi perlakukan dengan ketelitian yang sama seperti sistem produksi lain.

## Prinsip utama

- Rancang untuk perangkat: layar kecil, baterai, dan jaringan yang datang dan pergi.
- Asumsikan konektivitas terputus-putus; bekerja offline lebih dulu dan sinkronkan ketika bisa.
- Hormati konvensi desain dan interaksi setiap platform.
- Anda tidak mengendalikan waktu rilis; toko dan pengguna yang melakukannya.
- Fragmentasi itu normal; dukung rentang nyata perangkat dan versi OS.
- Simpan data dengan aman di perangkat, karena perangkat hilang dan dicuri.
- Aksesibilitas adalah persyaratan, bukan sentuhan akhir.
- Pilih pendekatan build untuk seluruh umur aplikasi, bukan hanya hari peluncuran.

## Rekomendasi

### Pilih pendekatan build dengan sengaja

Ada tiga pendekatan luas, dan masing-masing cocok untuk kebutuhan berbeda.

[Pengembangan native](https://en.wikipedia.org/wiki/Mobile_app_development) berarti menulis terpisah untuk setiap platform memakai perkakasnya sendiri: Swift untuk iOS, Kotlin untuk Android. Anda mendapat kinerja terbaik, akses terlengkap ke fitur perangkat, dan nuansa platform paling setia, dengan biaya membangun dan memelihara dua basis kode.

[Kerangka kerja lintas platform](https://en.wikipedia.org/wiki/Cross-platform_software) memungkinkan satu basis kode menargetkan kedua platform. [React Native](https://en.wikipedia.org/wiki/React_Native) memakai JavaScript dan merender komponen native nyata. [Flutter](https://en.wikipedia.org/wiki/Flutter_%28software%29) memakai bahasa Dart dan menggambar widget-nya sendiri. Ini mengurangi upaya terduplikasi dan dapat mempercepat pengiriman, tetapi menambah ketergantungan pada kesehatan kerangka kerja dan dapat tertinggal dari fitur platform terbaru.

[Aplikasi web progresif](https://en.wikipedia.org/wiki/Progressive_web_app) (PWA: situs web yang dapat dipasang dan dapat bekerja offline) tidak butuh toko dan diperbarui seketika, tetapi punya akses terbatas ke sebagian fitur perangkat dan kehadiran yang lebih lemah di layar utama.

Pilih berdasarkan fitur perangkat yang dibutuhkan, profil kinerja, cakrawala pemeliharaan, keterampilan yang dapat Anda rekrut, dan jangkauan yang Anda butuhkan. Aplikasi konsumen berkinerja tinggi mungkin membenarkan native. Aplikasi konten-dan-formulir dengan tim kecil mungkin cocok dengan lintas platform atau PWA.

### Ikuti pedoman desain platform

Setiap platform punya konvensi terbit dan terperinci. Apple menyediakan [Human Interface Guidelines](https://en.wikipedia.org/wiki/Human_interface_guidelines), dan Google menyediakan [Material Design](https://en.wikipedia.org/wiki/Material_Design). Ini mencakup navigasi, gestur, tipografi, jarak, dan perilaku sistem. Mengikutinya membuat aplikasi Anda terasa familier, yang menurunkan upaya pengguna mempelajarinya. Melawannya membuat aplikasi terasa asing dan canggung. Basis kode lintas platform tetap perlu menghormati konvensi per platform di tempat berbeda, alih-alih memaksakan tampilan satu platform ke yang lain.

### Rancang untuk kendala seluler

Bangun offline-first: biarkan tugas inti berfungsi tanpa koneksi, simpan perubahan secara lokal, dan sinkronkan ketika jaringan kembali. Tangani konflik dengan cermat ketika data yang sama berubah di dua tempat. Hemat baterai dan data: kelompokkan panggilan jaringan, hindari lokasi atau kerja latar belakang konstan, kompres muatan, dan hormati pengaturan penghemat data pengguna. Rencanakan fragmentasi, sebaran luas ukuran layar, daya perangkat, dan versi OS. Pilih rentang dukungan berdasarkan data pemakaian nyata, dan uji pada perangkat keras sederhana, bukan hanya unggulan. Rancang untuk layar kecil dengan hierarki jelas, target sentuh besar, dan konten yang beradaptasi dengan ukuran dan orientasi berbeda.

### Rencanakan distribusi, pembuatan versi, dan pembaruan

Penerbitan melalui [Apple App Store](https://en.wikipedia.org/wiki/App_Store_%28Apple%29) dan [Google Play](https://en.wikipedia.org/wiki/Google_Play), masing-masing dengan proses tinjauan dan kebijakan yang dapat menunda atau menolak rilis. Masukkan waktu tinjauan ke jadwal Anda, dan baca kebijakan sejak awal. Karena pengguna memilih kapan memperbarui, Anda akan selalu punya banyak versi di lapangan sekaligus. Jaga aplikasi Anda kompatibel mundur dengan klien lama, dan versikan API Anda (bab 2.3) agar aplikasi lama tetap berfungsi. Sediakan cara mewajibkan pembaruan ketika harus, misalnya prompt pembaruan paksa ketika versi tidak aman atau tidak didukung, dan pakai dengan hemat. Enterprise juga dapat mendistribusikan aplikasi internal lewat MDM atau kanal privat alih-alih toko publik.

### Gunakan notifikasi push dan deep link dengan hati-hati

[Notifikasi push](https://en.wikipedia.org/wiki/Push_technology) memungkinkan Anda menjangkau pengguna ketika aplikasi tertutup. Pakai untuk nilai sejati, hormati persetujuan pengguna dan izin platform, dan hindari derau, karena orang mematikan notifikasi dari aplikasi yang berlebihan. [Deep link](https://en.wikipedia.org/wiki/Deep_linking) mengirim pengguna langsung ke layar tertentu dari tautan atau notifikasi. Konfigurasikan agar tautan membuka tempat yang tepat dalam aplikasi, dan kembali ke web dengan anggun ketika aplikasi tidak terpasang.

### Amankan aplikasi dan datanya

Perlakukan perangkat sebagai tak tepercaya dan mungkin hilang. Simpan data sensitif di penyimpanan aman platform ([Keychain iOS](https://en.wikipedia.org/wiki/Keychain_%28software%29) atau Keystore Android), tidak pernah dalam berkas biasa. Tawarkan [autentikasi biometrik](https://en.wikipedia.org/wiki/Biometrics) (sidik jari atau wajah) untuk membuka tindakan sensitif, didukung kode sandi. Pertimbangkan [certificate pinning](https://en.wikipedia.org/wiki/Public_key_pinning) (memeriksa bahwa server menyajikan sertifikat yang diharapkan) untuk koneksi bernilai tinggi, dan rencanakan rotasi sertifikat itu. Minimalkan apa yang Anda simpan di perangkat, lindungi rahasia, dan ikuti panduan lebih luas dalam keamanan aplikasi (bab 4.2).

### Bangun pipeline pengujian dan pengiriman yang nyata

Uji pada perangkat nyata, bukan hanya [emulator](https://en.wikipedia.org/wiki/Emulator) dan simulator, karena perangkat keras, sensor, dan kinerja berbeda. Gunakan lab perangkat atau farm perangkat cloud untuk mencakup sebaran representatif model dan versi OS. Otomatiskan build, tes, penandatanganan, dan pengiriman ke toko lewat [integrasi dan pengiriman berkelanjutan](https://en.wikipedia.org/wiki/CI/CD) (bab 8.1), termasuk distribusi beta ke penguji sebelum rilis publik. Mengelola kunci penandatanganan dan kredensial toko dengan aman adalah bagian pipeline ini.

### Jadikan aksesibilitas persyaratan

Dukung fitur aksesibilitas setiap platform: pembaca layar ([VoiceOver](https://en.wikipedia.org/wiki/VoiceOver) di iOS, [TalkBack](https://en.wikipedia.org/wiki/Google_TalkBack) di Android), ukuran teks dinamis, kontras warna cukup, dan target sentuh besar. Beri label kontrol agar teknologi bantu dapat mendeskripsikannya. Uji dengan perkakas bantu sebenarnya, bukan hanya pemeriksaan otomatis. Untuk pemerintah khususnya, aksesibilitas adalah mandat hukum, dan rinciannya ada dalam aksesibilitas (bab 5.3).

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan |
|---|---|---|
| Native (Swift, Kotlin) | Kinerja terbaik, akses perangkat penuh, nuansa platform sejati | Dua basis kode, biaya lebih tinggi, lebih banyak staf |
| React Native | Satu basis kode JavaScript, komponen native nyata, iterasi cepat | Ketergantungan kerangka kerja, kompleksitas bridging, fitur tertinggal |
| Flutter | Satu basis kode, UI konsisten, kinerja kuat | Keterampilan Dart kurang umum, ukuran aplikasi lebih besar, model widget sendiri |
| Aplikasi web progresif | Tanpa toko, pembaruan seketika, satu basis kode web | Fitur perangkat terbatas, kehadiran lebih lemah, batas platform |
| Pembaruan paksa | Menghapus versi lama tak aman dengan cepat | Mengganggu pengguna jika berlebihan; dapat memblokir akses |
| Certificate pinning | Perlindungan kuat terhadap intersepsi | Rusak jika sertifikat dirotasi tanpa pembaruan aplikasi |

Trade-off yang berulang adalah jangkauan dan kecepatan pengiriman versus kedalaman dan fidelitas. Native memberi pengalaman terkaya dan paling setia tetapi berbiaya paling besar dibangun dan dipelihara. Pendekatan lintas platform dan PWA menghemat upaya dan memperluas jangkauan, dengan sedikit biaya dalam nuansa platform atau akses perangkat. Untuk tim kecil yang merilis formulir dan konten, berbagi basis kode sering bijak. Untuk aplikasi konsumen yang menuntut, kedalaman native bisa layak harganya. Putuskan dengan seluruh umur aplikasi dalam pandangan, bukan hanya peluncuran.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Berapa lama kita mendukung klien lama di lapangan, dan apakah API kita berversi untuk menjaga mereka tetap berfungsi?** Karena pengguna memilih kapan memperbarui, Anda selalu punya banyak versi aplikasi terpasang sekaligus, dan perubahan backend yang mengasumsikan semua orang mutakhir akan merusak ekor panjang klien lama. Putuskan jendela kompatibilitas mundur Anda, versikan API agar aplikasi lama tetap berfungsi, dan simpan jalur pembaruan paksa yang jarang dipakai untuk versi yang benar-benar tak aman. Ini penting bagi aplikasi warga pemerintah dan aplikasi tenaga kerja enterprise sama-sama, di mana orang pada perangkat lama tidak bisa atau tidak mau meningkatkan sesuai jadwal Anda. Bawa data distribusi versi Anda saat ini dan tanyakan apa yang rusak untuk klien tertua yang masih dipakai nyata. Jika Anda tidak tahu distribusi itu, instrumentasikan sebelum Anda mengirim perubahan merusak berikutnya.

2. **Apa standar kita untuk mengirim notifikasi push, dan siapa yang memutuskan apa yang layak mengganggu pengguna?** Notifikasi push menjangkau orang ketika aplikasi tertutup, yang membuatnya ampuh dan mudah disalahgunakan, dan pengguna mematikan notifikasi (atau menghapus aplikasi) dari produk yang berlebihan. Sepakati apa yang dihitung sebagai nilai sejati, bagaimana pengguna mengendalikan frekuensi dan kanal, dan bagaimana Anda menghormati persetujuan platform alih-alih merengek meminta izin. Tanpa standar bersama, setiap tim dengan metrik untuk dicapai akan meraih push, dan seluruh kanal merosot menjadi derau. Bawa notifikasi bulan terakhir yang Anda kirim dan tanyakan mana yang akan disyukuri pengguna. Jika sebagian besar promosi, kencangkan kebijakan sebelum tingkat opt-out melakukannya untuk Anda.

3. **Apakah pipeline pengiriman seluler kita nyata, mencakup penandatanganan, farm perangkat, dan distribusi beta, atau rilis adalah perebutan manual yang menegangkan?** Seluler menambah bahaya yang tidak dimiliki web: tinjauan toko dapat menunda atau menolak rilis, kunci penandatanganan dan kredensial toko harus ditangani dengan aman, dan perangkat keras serta sensor cukup berbeda sehingga emulator menyembunyikan masalah nyata. Mengotomatisasi build, tes, penandatanganan, dan pengiriman ke toko lewat CI/CD, dengan distribusi beta ke penguji dan farm perangkat cloud yang mencakup model yang benar-benar dibawa pengguna Anda, adalah yang mengubah rilis dari heroik menjadi rutin. Putuskan siapa yang memiliki pipeline dan kunci penandatanganan, dan bagaimana waktu tinjauan toko dimasukkan ke setiap rencana rilis. Bawa kisah rilis terakhir Anda dan hitung langkah manualnya. Masing-masing adalah tempat rilis yang menegangkan dapat salah di bawah tenggat.

4. **Sudahkah kita memilih native, lintas platform, atau aplikasi web progresif untuk seluruh umur produk ini, atau hanya untuk hari peluncuran?** Pendekatan build adalah tuas tunggal terbesar atas biaya dan kemampuan aplikasi seluler selama bertahun-tahun, dan pilihan yang dibuat untuk merilis cepat dapat menjebak Anda: native membeli akses perangkat terkaya dan nuansa platform dengan harga dua basis kode dan dua himpunan keterampilan, sementara lintas platform dan PWA berbagi kode tetapi menambah ketergantungan kerangka kerja atau kehilangan akses ke sebagian fitur perangkat. Bagi tim besar, keputusan ini menggerakkan perekrutan, anggaran pemeliharaan, dan seberapa cepat Anda dapat mengadopsi setiap rilis OS tahunan, sehingga layak mendapat pemilik eksplisit alih-alih bawaan yang ditetapkan siapa pun yang menulis prototipe pertama. Bawa fitur perangkat yang dibutuhkan, profil kinerja, cakrawala pemeliharaan, dan keterampilan yang benar-benar dapat Anda rekrut, dan jujurlah fitur platform mana yang akan Anda lepas di bawah setiap opsi. Dalam pengaturan enterprise dan pemerintah, timbang apakah aplikasi adalah komitmen berumur panjang yang harus selamat dari pergantian staf dan satu dekade perubahan platform, dan catat keputusan beserta alasannya agar tim mendatang tidak menebak mengapa basis kode tampak seperti itu.

5. **Rentang dukungan perangkat dan versi OS apa yang dibutuhkan pengguna nyata kita, dan apakah kita menguji pada perangkat keras yang benar-benar mereka bawa alih-alih ponsel di meja kita?** Fragmentasi adalah kondisi normal seluler: pengguna mencakup sebaran luas ukuran layar, daya perangkat, dan versi OS, dan aplikasi yang disetel pada unggulan tim akan dikirim lamban atau rusak pada perangkat keras sederhana yang dimiliki sebagian besar audiens Anda. Menetapkan rentang dukungan adalah pertukaran antara jangkauan dan upaya, karena setiap model dan versi OS lama yang Anda janjikan didukung memperlebar matriks uji dan beban pemeliharaan, sehingga rentang harus datang dari data pemakaian nyata alih-alih asumsi. Bawa distribusi perangkat dan versi OS Anda, model yang saat ini dicakup farm perangkat cloud atau lab, dan kinerja yang telah Anda ukur pada perangkat keras kelas bawah, bukan hanya simulator. Untuk aplikasi warga pemerintah ini nyaris tak dapat ditawar, karena Anda harus melayani semua orang termasuk orang pada perangkat lama dan koneksi lambat di bawah kewajiban aksesibilitas, dan untuk armada enterprise Anda harus menguji persis ponsel tahan banting yang dibawa staf alih-alih sampel generik.

6. **Data sensitif apa yang hidup di perangkat, dan apakah masing-masing dilindungi terhadap ponsel yang hilang, dicuri, atau di tangan orang lain?** Perangkat seluler bepergian di saku dan hilang atau dicuri, sehingga data atau rahasia apa pun yang disimpan dalam berkas biasa satu ponsel salah taruh dari terekspos, dan radius ledakannya tumbuh dengan setiap pengguna. Pertimbangan saling tarik: menyimpan data di perangkat adalah yang membuat offline-first berfungsi dan menjaga aplikasi cepat, namun setiap butir ter-cache adalah liabilitas yang harus berada di penyimpanan aman platform (Keychain iOS atau Keystore Android), diminimalkan, dan idealnya dikunci di balik biometrik atau kode sandi. Bawa inventaris persis apa yang disimpan aplikasi secara lokal, di mana setiap butir disimpan, apa yang membukanya, dan apakah koneksi bernilai tinggi memakai certificate pinning dengan rencana rotasi yang dapat dijalankan. Dalam pengaturan enterprise, kaitkan ini dengan kebijakan manajemen perangkat seluler dan penghapusan jarak jauh, dan dalam pengaturan pemerintah perlakukan data pribadi di perangkat sebagai paparan privasi dan hukum yang harus dibenarkan, didokumentasikan, dan dapat dipertahankan di bawah audit.

## Lensa sektor

**Startup.** Dengan tim kecil dan landasan pendek, Anda jarang mampu dua basis kode native atau dua himpunan keterampilan, sehingga kerangka kerja lintas platform atau bahkan PWA yang menjangkau kedua toko dari satu basis kode biasanya menang. Rilis offline-first untuk satu tugas inti yang penting, simpan token apa pun di penyimpanan aman alih-alih berkas biasa, dan masukkan waktu tinjauan toko ke setiap rilis agar penolakan tidak menggagalkan tanggal peluncuran. Lewati pembaruan paksa, certificate pinning, dan farm perangkat sampai pemakaian nyata membenarkannya.

**Bisnis kecil.** Tanpa spesialis seluler khusus dan dengan anggaran ketat, condonglah keras ke beli daripada bangun: pembangun aplikasi tanpa kode, aplikasi white-label dari vendor point-of-sale atau pemesanan Anda, atau PWA yang dibuat baik dari situs web Anda yang ada sering mengalahkan aplikasi pesanan yang tak dapat Anda pelihara. Jika Anda memang memesan aplikasi, miliki sendiri kunci penandatanganan dan akun toko agar kontraktor tidak dapat menyandera kehadiran Anda, dan desak aksesibilitas serta penyimpanan aman di perangkat dalam kontrak. Jaga cakupan pada satu atau dua tugas yang benar-benar dilakukan pelanggan di ponsel.

**Enterprise.** Pada skala besar, aplikasi adalah komitmen berumur panjang lintas banyak tim, jadi bakukan pendekatan build, pola penyimpanan aman, pipeline CI/CD, dan kebijakan pembuatan versi API alih-alih membiarkan setiap produk menciptakan ulang. Aplikasi tenaga kerja internal biasanya mengalir lewat manajemen perangkat seluler untuk pemasangan, konfigurasi, penghapusan jarak jauh, dan kebijakan, sementara aplikasi pelanggan butuh farm perangkat yang mencakup pemakaian nyata dan aksesibilitas serta keamanan yang diaudit. Atur kunci penandatanganan, kredensial toko, dan waktu rilis secara terpusat agar perubahan backend yang merusak tidak pernah menelantarkan ekor panjang klien lama.

**Pemerintah.** Aturan pengadaan, transparansi, dan akuntabilitas publik membentuk setiap pilihan. Anda harus melayani semua orang, termasuk orang pada perangkat lama dan koneksi lambat, sehingga aksesibilitas adalah mandat hukum yang diverifikasi dengan perkakas bantu nyata, dan rentang dukungan perangkat luas nyaris tak dapat ditawar. Pilih pendekatan dan kontrak yang menghindari lock-in vendor, jaga data tetap portabel, dan biarkan publik memeriksa apa yang dilakukan aplikasi dengan data mereka, dan perlakukan data pribadi di perangkat sebagai paparan yang harus Anda benarkan dan dokumentasikan di bawah audit.

## Contoh

**Startup.** Startup tiga orang yang membangun aplikasi pelacak kebiasaan harus menjangkau iOS dan Android tetapi tak mampu dua basis kode native atau dua himpunan keterampilan. Mereka memilih kerangka kerja lintas platform agar satu tim kecil dapat merilis ke kedua toko, dan merancang offline-first sejak awal agar pengguna dapat mencatat kebiasaan di kereta bawah tanah tanpa sinyal dan menyinkronkan kemudian. Mereka menyimpan token login di penyimpanan aman platform alih-alih berkas biasa, memasukkan waktu tinjauan toko ke setiap rencana rilis, dan menguji pada beberapa ponsel tua murah di samping ponsel sendiri, yang menangkap kinerja lamban yang kalau tidak akan mereka kirim.

**Enterprise.** Sebuah perusahaan logistik membangun aplikasi internal untuk pengemudi dan staf gudangnya. Karena gudang dan rute pengiriman punya sinyal tersendat, tim memilih desain offline-first: pindaian dan pembaruan status disimpan lokal dan disinkronkan ketika koneksi kembali. Mereka memakai kerangka kerja lintas platform untuk melayani satu basis kode ke kedua platform dengan tim kecil. Aplikasi didistribusikan lewat manajemen perangkat seluler alih-alih toko publik, sehingga TI mengendalikan pemasangan, konfigurasi, dan kebijakan keamanan pada perangkat perusahaan. Kredensial sensitif hidup di penyimpanan aman platform, dan biometrik membuka aplikasi. Farm perangkat cloud menguji sebaran representatif ponsel tahan banting yang benar-benar dibawa staf.

**Pemerintah.** Sebuah lembaga nasional merilis aplikasi warga untuk identitas dan tunjangan. Aksesibilitas adalah persyaratan keras sejak hari pertama: dukungan pembaca layar penuh, ukuran teks dinamis, dan kontras kuat, diuji dengan perkakas bantu nyata untuk memenuhi hukum. Karena warga memakai rentang perangkat sangat luas, tim mendukung pita lebar model lama dan koneksi lambat, dan menjaga tugas inti berfungsi offline. Data sensitif tetap di penyimpanan perangkat yang aman, biometrik melindungi akses, dan koneksi bernilai tinggi memakai certificate pinning dengan proses rotasi terencana. Pembuatan versi API menjaga aplikasi terpasang lama tetap berfungsi, dan jalur pembaruan paksa yang jarang dipakai ada untuk perbaikan keamanan. Garis waktu tinjauan toko dimasukkan ke setiap rencana rilis.

## Kasus bisnis: motivasi, ROI, dan TCO

Seluler adalah tempat banyak pengguna bertemu layanan Anda, sehingga aplikasi memengaruhi adopsi, kepuasan, dan penyelesaian tugas yang penting bagi organisasi Anda. Aplikasi yang cepat, andal, dan dirancang baik meningkatkan pemakaian dan mengurangi beban dukungan. Untuk enterprise, aplikasi seluler internal dapat membuat tenaga kerja bergerak terukur lebih produktif dan memangkas kertas kerja. Untuk pemerintah, aplikasi warga yang dapat dipakai memperluas akses dan mengurangi permintaan pusat panggilan dan tatap muka.

Pada total biaya kepemilikan (TCO), pilihan pendekatan adalah tuas terbesar. Native berarti membayar dua basis kode dan dua himpunan keterampilan sepanjang umur aplikasi. Lintas platform menukar sebagian itu dengan ketergantungan yang harus Anda jaga mutakhir. Di luar kode, anggarkan biaya toko dan siklus tinjauan, lab pengujian perangkat atau farm cloud, dukungan versi OS berkelanjutan seiring platform merilis tahunan, dan kerja keamanan yang dituntut seluler. Biaya kurang berinvestasi muncul sebagai crash pada perangkat yang tak didukung, insiden keamanan dari data di perangkat yang tak terlindungi, rilis ditolak atau tertunda, dan pengguna yang meninggalkan aplikasi lambat atau canggung.

Untuk mengajukan kasus kepada pimpinan, kaitkan aplikasi dengan hasil konkret: penyelesaian tugas, retensi, produktivitas tenaga kerja, atau biaya dukungan berkurang. Hargai keputusan pendekatan penuh sepanjang umur aplikasi, bukan hanya rilis pertama, dan namai risiko (keamanan, hukum aksesibilitas, penolakan toko) yang dikurangi praktik seluler yang serius.

## Anti-pola dan jebakan

- **Memperlakukan seluler sebagai situs web yang dikecilkan**: mengabaikan sentuhan, gestur, dan konvensi platform.
- **Mengasumsikan jaringan sempurna**: tanpa penanganan offline, sehingga aplikasi rusak begitu sinyal jatuh.
- **Menguji hanya di unggulan terbaru**: menyembunyikan kinerja buruk pada perangkat yang dibawa pengguna nyata.
- **Menyimpan rahasia dalam berkas biasa**: data sensitif terekspos ketika perangkat hilang atau dicuri.
- **Kelebihan notifikasi**: terlalu banyak push, sehingga pengguna membisukan atau menghapus aplikasi.
- **Mengabaikan waktu tinjauan toko**: rencana rilis yang mengasumsikan penerbitan seketika lalu meleset.
- **Tanpa jalur pembaruan paksa**: versi lama tak aman bertahan tanpa cara memensiunkannya.
- **Menguras baterai dan data**: kerja latar belakang konstan dan jaringan cerewet yang disadari pengguna.
- **Aksesibilitas sebagai renungan belakangan**: mengecualikan pengguna dan, untuk pemerintah, melanggar hukum.
- **Satu basis kode dipaksa tampak identik di mana-mana**: aplikasi yang terasa asing di kedua platform.

## Model kematangan

**Tingkat 1: Memulai.** Seluler ad hoc dan reaktif. Aplikasi dibangun seperti situs web, diuji di ponsel tim sendiri, dan sering rusak offline. Sedikit pemikiran diberikan pada penyimpanan aman, aksesibilitas, atau garis waktu tinjauan toko. Rilis adalah perebutan manual yang menegangkan, dan tak ada yang memiliki pendekatan build atau kunci penandatanganan.

**Tingkat 2: Mengembangkan.** Praktik dasar muncul, tetapi tidak konsisten lintas tim dan produk. Pendekatan build dipilih untuk aplikasi tertentu, mengikuti dasar platform dan diuji pada beberapa perangkat nyata, dan sebagian penanganan offline dan penyimpanan aman ada. Build sebagian otomatis dan seseorang memiliki pengiriman toko, namun aplikasi tim lain mungkin masih melakukan semua ini berbeda atau tidak sama sekali.

**Tingkat 3: Membakukan.** Praktik baik terdokumentasi dan ditegakkan di seluruh organisasi. Offline-first adalah bawaan, rentang dukungan perangkat terdokumentasi diuji pada lab perangkat atau farm cloud, dan pedoman desain platform serta aksesibilitas diikuti dan diverifikasi dengan perkakas bantu nyata. Penyimpanan aman, biometrik, dan pembuatan versi API adalah standar, CI/CD mengotomatisasi build, tes, penandatanganan, dan distribusi beta, dan waktu tinjauan toko direncanakan ke setiap rilis.

**Tingkat 4: Mengelola.** Kualitas seluler diukur dan dikendalikan terhadap garis dasar. Crash, kinerja cold-start dan render layar, penggunaan baterai dan data, serta tingkat penyelesaian tugas ditangkap terus-menerus dari perangkat nyata dan dilacak terhadap target, dengan rincian per model dan per versi OS agar regresi pada perangkat keras kelas bawah tertangkap, tidak dikirim. Aksesibilitas dan keamanan diaudit alih-alih diasumsikan, tingkat opt-out notifikasi dan adopsi pembaruan dipantau, dan rentang dukungan serta pendekatan build ditinjau atas bukti ini. Keputusan perbaiki atau hentikan untuk rilis bertumpu pada metrik, bukan pada bagaimana aplikasi terasa di ponsel pemimpin.

**Tingkat 5: Mengorkestrasi.** Seluler terus diperbaiki dan terintegrasi di seluruh organisasi, dan beradaptasi seiring lanskap perangkat bergeser. Rotasi sertifikat, jalur pembaruan paksa, dan rollback rutin, rentang dukungan dan pendekatan build ditentukan ulang cakupannya atas bukti seiring platform merilis tahunan, dan seluruh sebaran pengguna dan perangkat diperlakukan kelas satu. Perencanaan seluler terpadu dengan praktik keamanan, aksesibilitas, API, dan pengiriman, sehingga perubahan OS, tingkat perangkat baru, atau pergeseran kebijakan diserap sebagai kerja rutin alih-alih darurat.

## Gagasan untuk didiskusikan

- Bagaimana Anda memutuskan antara native, lintas platform, dan aplikasi web progresif untuk produk tertentu?
- Rentang dukungan perangkat dan versi OS apa yang cocok dengan data pengguna nyata Anda, dan bagaimana Anda menjaganya tetap mutakhir?
- Di mana offline-first esensial dalam aplikasi Anda, dan bagaimana Anda menangani konflik sinkronisasi?
- Kapan pembaruan paksa dibenarkan, dan bagaimana Anda menghindari memblokir pengguna secara tidak adil?
- Bagaimana Anda akan menguji pada perangkat nyata pada skala yang mencerminkan pengguna Anda?
- Data sensitif apa yang hidup di perangkat, dan bagaimana masing-masing dilindungi?
- Bagaimana Anda menghormati konvensi setiap platform dari basis kode bersama?

## Poin-poin utama

- Pilih pendekatan build (native, lintas platform, atau PWA) untuk seluruh umur aplikasi.
- Ikuti pedoman desain platform agar aplikasi terasa familier dan menurunkan upaya pengguna.
- Rancang untuk kendala seluler: offline-first, hemat baterai dan data, fragmentasi, layar kecil.
- Anda tidak mengendalikan waktu rilis; rencanakan tinjauan toko, pembuatan versi, dan pembaruan paksa.
- Gunakan notifikasi push dan deep link dengan menahan diri dan persetujuan.
- Amankan data di perangkat dengan penyimpanan aman, biometrik, dan, bila dibenarkan, certificate pinning.
- Uji pada perangkat nyata dan otomatiskan pipeline seluler lewat CI/CD.
- Jadikan aksesibilitas persyaratan, yang bagi pemerintah adalah mandat hukum.

## Referensi dan bacaan lanjutan

- Apple, *Human Interface Guidelines*
- Google, pedoman *Material Design*
- Apple, *App Store Review Guidelines*
- Google, *Google Play developer policies and Android developer documentation*
- OWASP, *Mobile Application Security Verification Standard (MASVS)* dan *Mobile Security Testing Guide*
- Dokumentasi proyek React Native
- Dokumentasi proyek Flutter
- Google, panduan *web.dev* tentang aplikasi web progresif
- Rujukan U.S. Section 508 dan WCAG (Web Content Accessibility Guidelines) untuk aksesibilitas seluler
- NIST, *Guidelines on mobile device security and management*
