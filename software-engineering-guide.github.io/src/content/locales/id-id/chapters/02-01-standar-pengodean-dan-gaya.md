# 2.1 Standar pengodean dan gaya

## Tinjauan dan motivasi

Standar pengodean adalah konvensi bersama yang memungkinkan banyak orang menulis kode seolah-olah satu penulis yang cermat yang menulisnya. Standar ini mencakup penamaan, format, tata letak berkas, idiom, penanganan galat, dan paradigma yang disukai sebuah tim. Pada tim kecil, selera individu bisa menentukan. Pada tim besar (ratusan atau ribuan insinyur, banyak kontraktor, pergantian tinggi), inkonsistensi menjadi pajak yang Anda bayar pada setiap pembacaan, setiap tinjauan, dan setiap orientasi. Standar mengubah perdebatan gaya kecil yang tak terhitung menjadi satu keputusan sekali jalan yang kemudian ditegakkan mesin untuk Anda.

Bagi organisasi besar taruhannya konkret. Kode dibaca jauh lebih sering daripada ditulis. Dalam konteks enterprise dan pemerintah, sebaris kode mungkin dibaca auditor, peninjau keamanan, dan pemelihara bertahun-tahun setelah penulisnya pergi. Gaya yang konsisten menurunkan beban mental pembacaan itu, mengecilkan permukaan bagi bug, dan membuat analisis otomatis andal di seluruh [linter](https://en.wikipedia.org/wiki/Lint_(software)) (perkakas yang menandai bug yang mungkin dan pelanggaran gaya secara otomatis), pemindai keamanan, dan perkakas [refaktoring](https://en.wikipedia.org/wiki/Code_refactoring). Di tempat regulasi berlaku, seperti layanan keuangan, kesehatan, pertahanan, dan sistem sektor publik, standar juga menjadi bagian dari bukti bahwa basis kode dapat dipelihara dan terkendali.

Pendekatan modern memperlakukan gaya sebagai persoalan yang sudah terpecahkan dan otomatis, bukan perkara penilaian manusia yang terus-menerus. Formatter dan linter berjalan di editor, di pre-commit hook, dan di [integrasi berkelanjutan](https://en.wikipedia.org/wiki/Continuous_integration) (CI), proses build-dan-tes otomatis yang berjalan pada setiap perubahan. Mesin menegakkan gaya, sehingga Anda dapat membelanjakan perhatian tinjauan pada desain dan kebenaran. Tujuannya bukan keseragaman demi keseragaman. Tujuannya menghilangkan gesekan: Anda harus dapat berpindah antarlayanan dan tim tanpa mempelajari ulang dasar-dasarnya.

## Prinsip utama

- Konsistensi mengalahkan preferensi individu; satu gaya yang disepakati dan diterapkan di mana-mana lebih bernilai daripada gaya "terbaik" yang diterapkan tidak merata.
- Otomatiskan penegakan. Formatter dan linter adalah sumber kebenaran, bukan komentar tinjauan kode tentang spasi.
- Optimalkan untuk pembaca dan pemelihara, bukan penulis aslinya.
- Pilih konvensi yang sudah dipakai komunitas bahasa yang lebih luas daripada aturan rumah yang dibuat sendiri.
- Permudah adopsi standar: sediakan konfigurasi bersama, templat, dan perkakas alih-alih PDF yang tak dibaca siapa pun.
- Aturan gaya harus sedikit, dapat dipertahankan, dan tidak ambigu; setiap aturan punya mekanisme penegakan atau hanya saran.
- Penamaan adalah keputusan keterbacaan berdaya ungkit tertinggi dan layak mendapat panduan eksplisit.

## Rekomendasi

### Adopsi panduan gaya kanonik per bahasa

Untuk setiap bahasa yang Anda pakai, adopsi panduan gaya yang diakui luas sebagai garis dasar (misalnya, panduan komunitas atau vendor untuk bahasa itu) dan dokumentasikan hanya selisih yang dibutuhkan organisasi Anda. Jangan menciptakan gaya rumah dari nol. Terbitkan pilihan Anda di tempat pusat yang mudah ditemukan, dan beri versi seperti kode.

### Jadikan formatter sebagai bawaan yang tidak dapat ditawar

Gunakan formatter otomatis yang beropini untuk setiap bahasa yang memilikinya, dengan satu konfigurasi bersama yang di-check-in ke repositori. Format tidak boleh pernah muncul dalam tinjauan, karena diterapkan otomatis saat simpan dan diverifikasi di CI. Di mana bahasa tidak memiliki formatter yang kuat, pilih satu konfigurasi linter dan perlakukan dengan cara yang sama.

### Jalankan linter sebagai gerbang yang ditegakkan, bukan saran

Konfigurasikan linter dengan rangkaian aturan yang disepakati, gagalkan build saat ada pelanggaran, dan simpan rangkaian aturan di [kontrol versi](https://en.wikipedia.org/wiki/Version_control) agar perubahan melalui tinjauan. Pisahkan aturan yang dapat diperbaiki otomatis (terapkan secara otomatis) dari aturan yang membutuhkan penilaian manusia (tandai dan blokir). Perkenalkan aturan baru dalam mode "warn," bersihkan tunggakannya, lalu naikkan menjadi "error."

### Tegakkan pada banyak lapisan

Sediakan integrasi editor untuk umpan balik instan, pre-commit hook untuk penegakan lokal, dan pemeriksaan CI sebagai gerbang yang berwenang. Semakin awal Anda menangkap pelanggaran, semakin murah. CI harus menjadi penopang terakhir, karena hook lokal dapat dilewati.

### Beri penamaan aturan yang eksplisit

Bakukan konvensi huruf per bahasa, wajibkan nama yang mengungkapkan maksud, larang singkatan yang menyesatkan, dan tetapkan konvensi untuk boolean, koleksi, satuan, dan operasi asinkron. Tuliskan kosakata domain Anda dalam glosarium bersama agar konsep yang sama memiliki nama yang sama di mana-mana.

### Kelola konsistensi poliglot dengan sengaja

Dalam basis kode yang mencakup beberapa bahasa, upayakan konsep yang konsisten (pola penanganan galat, struktur logging, tata letak proyek) meskipun sintaksisnya berbeda. Sediakan konfigurasi per bahasa dari repositori pusat agar layanan baru mewarisi standar secara otomatis melalui templat atau scaffolding.

### Kodifikasikan idiom dan paradigma

Melampaui format. Tuliskan idiom pilihan Anda, seperti cara menangani galat, cara menyusun modul, dan kapan memakai exception versus tipe hasil, beserta paradigma yang disukai tim Anda. Di sinilah keterbacaan dan kemudahan pemeliharaan yang sebenarnya hidup.

## Trade-off: kelebihan dan kekurangan

| Pendekatan | Kelebihan | Kekurangan |
|---|---|---|
| Auto-formatter ketat, tanpa konfigurasi | Mengakhiri semua debat format; konsistensi instan; orientasi sepele | Sebagian pilihan yang tidak disukai tak dapat ditawar; diff awal besar saat pertama diterapkan |
| Linter yang dapat dikonfigurasi dengan aturan rumah | Disesuaikan dengan kebutuhan organisasi; dapat mengkodekan aturan pencegah bug yang nyata | Penyimpangan konfigurasi; bikeshedding aturan; beban pemeliharaan |
| Standar komunitas diadopsi bulat-bulat | Akrab bagi karyawan baru; ekosistem perkakas kuat; pemeliharaan rendah | Mungkin tidak cocok dengan kendala organisasi khusus; aturan canggung sesekali |
| Standar internal buatan sendiri | Cocok persis dengan organisasi | Mahal ditulis dan dipelihara; tidak akrab bagi karyawan; perkakas lemah |
| Otonomi per tim | Moral lokal tinggi; spesifik konteks | Fragmentasi; mobilitas lintas tim menyakitkan; perkakas tidak konsisten |

Bawaan yang ditegakkan menukar sedikit otonomi individu dengan keuntungan kolektif yang besar: gesekan tinjauan lebih sedikit, orientasi lebih cepat, dan otomasi yang andal. Risiko utamanya adalah merekayasa berlebihan standar menjadi ratusan aturan yang memperlambat semua orang tanpa mencegah cacat nyata. Jaga rangkaian aturan kecil dan berbasis bukti, dan condonglah ke mengadopsi standar yang ada agar pemeliharaan tetap murah.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Aturan linter mana yang harus menggagalkan build, dan bagaimana Anda menaikkan aturan dari peringatan ke galat tanpa menghentikan semua orang?** Bab ini berargumen bahwa setiap aturan membutuhkan mekanisme penegakan, dan bahwa aturan baru harus masuk dalam mode warn, dibersihkan tunggakannya, lalu dibalik menjadi error. Pada tim besar, membalik aturan menjadi error terhadap basis kode yang kotor memblokir ratusan perubahan tak terkait dalam semalam. Bawa bukti keras ke rapat: jumlah pelanggaran saat ini untuk setiap aturan kandidat, dan apakah dapat diperbaiki otomatis atau butuh penilaian manusia. Dalam konteks enterprise dan pemerintah garis lulus/gagal juga memberi makan gerbang audit, sehingga rangkaian aturan yang ambigu melemahkan cerita kepatuhan Anda. Putuskan peluncuran bertahap: perbaiki otomatis yang bisa, anggarkan pembersihan, lalu beri gerbang.

2. **Ketika Anda pertama kali menerapkan formatter pada kode warisan, bagaimana Anda menjaga agar reformat itu tidak merusak git blame dan menenggelamkan tinjauan?** Tabel trade-off memperingatkan diff awal yang besar, dan bagian anti-pola menyebut pencampuran commit reformat dengan perubahan logika. Satu reformat menyapu menulis ulang ribuan baris dan membuat blame menunjuk ke reformat alih-alih penulis sebenarnya, yang menyakiti siapa pun yang men-debug bertahun-tahun kemudian. Lakukan reformat sebagai satu commit terisolasi yang berlabel jelas, dan daftarkan dalam berkas blame-ignore agar riwayat tetap berguna. Bagi auditor yang menelusuri siapa mengubah apa, isolasi itu adalah beda antara bukti bersih dan derau. Sepakati urutannya sebelum Anda menyentuh kode, bukan sesudahnya.

3. **Siapa yang memiliki glosarium penamaan dan kosakata domain Anda, dan bagaimana istilah baru ditambahkan?** Bab ini menyebut penamaan sebagai keputusan keterbacaan berdaya ungkit tertinggi dan meminta Anda menuliskan kosakata domain dalam glosarium bersama. Tanpa pemilik bernama, konsep yang sama mengambil tiga nama berbeda di berbagai tim, dan perkakas analisis statis dan pencarian kehilangan keandalan. Bawa contoh konsep yang sudah memiliki nama bertentangan dalam basis kode Anda sebagai sinyal konkret. Tetapkan satu pemilik dan jalur usulan ringan, agar menambah atau mengganti nama istilah menjadi perubahan kecil yang ditinjau, bukan perdebatan di setiap pull request. Jawabannya mengubah orientasi: karyawan baru membaca satu glosarium alih-alih merekayasa balik maksud dari kode yang tidak konsisten.

4. **Untuk setiap bahasa, apakah Anda mengadopsi panduan gaya komunitas atau vendor yang diakui secara bulat-bulat, dan di mana selisih rumah benar-benar dibenarkan?** Bab ini berargumen Anda harus mengambil standar yang ada sebagai garis dasar dan mendokumentasikan hanya selisih yang dibutuhkan organisasi Anda, karena standar buatan sendiri mahal ditulis dan tidak akrab bagi karyawan. Tarikan yang bersaing itu nyata: kendala internal (aturan keamanan, kerangka kerja warisan, mandat aksesibilitas) kadang benar-benar bertentangan dengan bawaan komunitas, dan setiap selisih yang Anda pertahankan adalah aturan yang kini Anda miliki dan pelihara selamanya. Bawa daftar selisih yang diusulkan ke rapat, masing-masing dengan kendala konkret yang memotivasinya, dan bersiaplah memotong selisih mana pun yang hanya soal selera. Dalam konteks enterprise dan pemerintah, garis dasar yang cocok dengan komunitas bahasa yang lebih luas juga berarti kontraktor dan vendor baru datang sudah fasih, yang mempersingkat orientasi dan memperkuat bukti kemudahan pemeliharaan yang dicari auditor.

5. **Dalam basis kode poliglot, konvensi mana yang benar-benar universal dan mana yang tetap lokal bahasa, dan bagaimana Anda mencegah konfigurasi per repo menyimpang?** Bab ini meminta konsep yang konsisten (penanganan galat, struktur logging, tata letak proyek) di seluruh bahasa meskipun sintaksis berbeda, dan konfigurasi per bahasa yang disajikan dari repositori pusat agar layanan baru mewarisi standar secara otomatis. Ketegangannya adalah memaksakan idiom satu bahasa ke bahasa lain menghasilkan kode yang canggung dan tidak idiomatis, sementara membiarkan setiap tim memecah konfigurasinya sendiri berakhir dengan "standar" yang tak berarti apa-apa. Bawa inventaris konfigurasi linter dan formatter per repo Anda saat ini dan diff yang menunjukkan seberapa jauh mereka sudah menyimpang, sebagai sinyal konkret. Bagi organisasi besar yang menjalankan puluhan layanan, putuskan mekanisme distribusi (templat, scaffolding, paket konfigurasi bersama) agar perubahan aturan menyebar sekali alih-alih disalin manual ke setiap repositori.

6. **Kapan menonaktifkan aturan itu sah, siapa yang meninjau supresinya, dan bagaimana Anda menjaga agar penonaktifan menyeluruh tidak menggerogoti standar?** Bagian anti-pola menandai supresi inline yang meluas sebagai tanda aturan yang keliru atau tim yang menyerah, namun kebijakan tanpa pengecualian yang kaku mendorong orang menulis kode lebih buruk hanya untuk memuaskan linter. Sepakati jalur ringan: supresi harus membawa alasan, berada pada cakupan tersempit, dan terlihat dalam tinjauan alih-alih terkubur dalam berkas ignore global. Bawa jumlah supresi saat ini per aturan dan per repositori, karena aturan yang disupresi ratusan kali sedang mengatakan sesuatu tentang aturannya, bukan kodenya. Dalam pekerjaan yang diatur dan sektor publik, supresi menyeluruh tanpa penjelasan melemahkan cerita audit secara langsung, karena pipeline tidak lagi dapat menunjukkan bahwa kode yang digabung benar-benar lolos gerbang yang disepakati.

## Lensa sektor

**Startup.** Kecepatan menang, jadi adopsi bawaan formatter dan linter komunitas untuk satu bahasa Anda pada hari pertama dan pasang ke pre-commit hook dan CI sebelum insinyur kedua tiba. Jangan menulis gaya rumah yang tidak punya waktu Anda pelihara: konfigurasi yang dikirim dalam repo adalah seluruh standar. Ketika Anda menambah bahasa kedua, raih panduan kanonik bahasa itu alih-alih menciptakan konvensi dari nol.

**Bisnis kecil.** Tanpa spesialis perkakas khusus dan dengan anggaran ketat, bersandarlah sepenuhnya pada formatter gratis yang beropini yang datang bersama atau berdampingan dengan bahasa Anda, dan terima bawaannya alih-alih menyetelnya. Ini kasus jelas beli-daripada-bangun: memelihara rangkaian aturan kustom memakan waktu yang tidak Anda miliki, sementara formatter siap pakai tidak berbiaya dan mengakhiri debat gaya seketika. Simpan konfigurasi dalam repositori agar kontraktor yang Anda rekrut tahun depan mewarisinya tanpa percakapan.

**Enterprise.** Pada skala besar tugasnya adalah tata kelola di banyak tim: repositori standar rekayasa pusat yang memegang konfigurasi formatter dan linter bersama per bahasa, layanan baru dibuat dari templat yang menarik konfigurasi itu, dan gerbang CI yang memblokir penggabungan yang tidak patuh. Beri versi pada rangkaian aturan seperti kode dan salurkan perubahan melalui tinjauan berkala agar standar berkembang dengan sengaja alih-alih menyimpang. Imbalannya adalah insinyur berpindah antartim ke kode yang akrab, dan perkakas otomatis yang menghasilkan sinyal andal karena setiap repositori konsisten.

**Pemerintah.** Pengadaan dan akuntabilitas membentuk pilihan: wajibkan gaya dan rangkaian aturan keamanan tertentu sebagai bagian dari persyaratan authority-to-operate, dan minta pipeline mengeluarkan laporan yang menunjukkan setiap perubahan yang digabung lolos gerbang yang disepakati sebagai bukti audit. Karena formatter diterapkan otomatis, kode dari banyak vendor dan kontraktor tampak konsisten, yang melindungi pekerjaan pemeliharaan publik lama setelah kontrak berakhir. Pilih garis dasar komunitas yang diakui daripada aturan buatan sendiri agar standar transparan dan pemasok mana pun di masa depan dapat mengadopsinya tanpa lock-in proprietari.

## Contoh

**Startup.** Sebuah startup empat orang mengadopsi bawaan formatter dan linter komunitas untuk satu bahasanya pada hari pertama, memasangnya ke pre-commit hook dan CI agar tak seorang pun berdebat soal spasi dalam tinjauan. Karena konfigurasi dikirim di dalam repo, karyawan kelima dan keenam mewarisinya secara otomatis dan tidak pernah melihat komentar format. Ketika tim kemudian menambah bahasa kedua, mereka meraih panduan standar bahasa itu alih-alih menciptakan gaya rumah yang tidak punya waktu mereka pelihara.

**Enterprise.** Sebuah bank besar menjalankan layanan dalam Java, Python, dan TypeScript di puluhan tim. Ia menerbitkan repositori "standar rekayasa" pusat yang memegang konfigurasi formatter dan linter bersama untuk setiap bahasa. Layanan baru dibuat dari templat yang menarik konfigurasi itu, sehingga setiap repositori mulai dalam keadaan patuh. CI memblokir penggabungan pada pelanggaran apa pun, dan tinjauan kuartalan mengatur perubahan aturan. Waktu orientasi bagi insinyur yang berpindah antartim turun terasa, karena setiap repositori tampak akrab.

**Pemerintah.** Sebuah lembaga sektor publik yang memodernisasi sistem warisan mewajibkan rangkaian aturan linting aksesibilitas dan keamanan sebagai bagian dari persyaratan authority-to-operate (ATO)-nya, persetujuan formal yang dibutuhkan untuk menjalankan sistem di produksi. Kepatuhan gaya menjadi bagian dari bukti audit: pipeline menghasilkan laporan yang menunjukkan semua kode yang digabung lolos gerbang [analisis statis](https://en.wikipedia.org/wiki/Static_program_analysis) yang disepakati. Karena formatter diterapkan otomatis, kontraktor dari banyak vendor menghasilkan kode yang konsisten secara visual, yang memudahkan pekerjaan pemeliharaan jangka panjang pemerintah setelah kontrak berakhir.

## Kasus bisnis: motivasi, ROI, dan TCO

Biaya mengadopsi standar sebagian besar sekali jalan: memilih panduan, memasang perkakas, dan menerapkan satu commit reformat awal yang besar. Biaya berulangnya rendah, karena penegakan bersifat otomatis. Biaya *tidak* mengadopsi standar berulang dan berlipat: setiap tinjauan menghabiskan menit untuk gaya, setiap orientasi lebih lambat, perkakas analisis statis menghasilkan derau, dan kode yang tidak konsisten menyembunyikan bug. Di organisasi besar, menit-menit itu berjumlah menjadi kerugian setara karyawan penuh waktu.

Imbal hasilnya tampak sebagai latensi tinjauan yang berkurang, komentar tinjauan terkait gaya yang lebih sedikit, orientasi lebih cepat, dan sinyal lebih tinggi dari perkakas otomatis. Di lingkungan yang diatur ada imbal hasil tambahan dalam kesiapan audit: kontrol yang dapat didemonstrasikan dan ditegakkan mengurangi upaya dan risiko tinjauan kepatuhan. Untuk meyakinkan pimpinan, bingkai standar sebagai tuas berbiaya rendah berdaya ungkit tinggi atas produktivitas pengembang dan postur audit, dan beri angka pada biaya inkonsistensi saat ini dengan analisis komentar tinjauan dan data survei orientasi.

## Anti-pola dan jebakan

- **Gaya diperdebatkan dalam tinjauan kode:** tanda penegakan tidak otomatis; pindahkan aturan ke perkakas.
- **Dokumen standar yang tak dibaca:** halaman wiki tanpa penegakan adalah hiasan; setiap aturan butuh mekanisme.
- **Aturan menjamur:** ratusan aturan pedantik yang memperlambat kerja tanpa mencegah cacat.
- **Penyimpangan konfigurasi:** setiap repositori memecah konfigurasi linter sendiri sampai "standar" tak berarti apa-apa.
- **Memformat seluruh repo di tengah kerja fitur:** mencampur commit reformat dengan perubahan logika menghancurkan tinjauan dan blame; lakukan reformat besar dalam commit terisolasi yang berlabel jelas.
- **Mengabaikan linter dengan supresi menyeluruh:** penonaktifan inline yang meluas menandakan aturan yang keliru atau tim yang menyerah.
- **Standar tanpa kepemilikan:** tanpa pemilik jelas, aturan tidak pernah berkembang dan membusuk.

## Model kematangan

- **Tingkat 1, Memulai:** Gaya bersifat per penulis dan reaktif; tidak ada konfigurasi bersama; format diperdebatkan dalam tinjauan dan diselesaikan oleh siapa pun yang paling peduli hari itu.
- **Tingkat 2, Mengembangkan:** Tim individual mengadopsi formatter dan linter, tetapi konfigurasi dan rangkaian aturan bervariasi dari tim ke tim dan repo ke repo, sehingga konsistensi berhenti di batas setiap tim.
- **Tingkat 3, Membakukan:** Konfigurasi bersama pusat per bahasa didokumentasikan dan ditegakkan di seluruh organisasi; CI memblokir penggabungan yang tidak patuh; repositori baru mewarisi standar secara otomatis melalui templat atau scaffolding.
- **Tingkat 4, Mengelola:** Standar diukur dan dikendalikan dengan data: tingkat pelanggaran, jumlah supresi, komentar tinjauan terkait gaya, dan waktu orientasi dilacak terhadap garis dasar, dan perubahan aturan dinaikkan atau dipensiunkan berdasarkan bukti itu, bukan opini.
- **Tingkat 5, Mengorkestrasi:** Standar terus diperbaiki dan terintegrasi di seluruh organisasi; idiom poliglot dan kosakata domain didokumentasikan dan ditegakkan, penegakan nyaris tanpa gesekan, dan rangkaian aturan beradaptasi seiring bergesernya bahasa, perkakas, dan kebutuhan organisasi.

## Gagasan untuk didiskusikan

- Di mana garis antara aturan yang ditegakkan dan pedoman terdokumentasi yang memercayai penilaian insinyur?
- Bagaimana organisasi harus menangani aturan komunitas yang disukai yang bertentangan dengan kendala internal yang sejati?
- Siapa yang memiliki standar, dan bagaimana perubahan aturan diusulkan, diperdebatkan, dan diluncurkan tanpa gangguan?
- Dalam basis kode poliglot, konvensi mana yang benar-benar universal dan mana yang tetap lokal bahasa?
- Bagaimana Anda memasang standar pada basis kode warisan yang besar tanpa reformat big-bang yang mengganggu?
- Peran apa yang harus dimainkan perkakas berbantuan AI dalam menyarankan atau menegakkan idiom melampaui format mekanis?

## Poin-poin utama

- Perlakukan gaya sebagai masalah otomatis yang sudah terpecahkan agar manusia meninjau desain dan kebenaran.
- Adopsi standar komunitas yang ada dan dokumentasikan hanya selisihnya.
- Tegakkan pada lapisan editor, pre-commit, dan CI, dengan CI sebagai gerbang yang berwenang.
- Jaga rangkaian aturan tetap kecil, dapat dipertahankan, dan diatur secara terpusat.
- Penamaan dan idiom, bukan spasi, adalah tempat keterbacaan benar-benar dimenangkan.

## Referensi dan bacaan lanjutan

- Robert C. Martin, *Clean Code: A Handbook of Agile Software Craftsmanship*
- Andrew Hunt dan David Thomas, *The Pragmatic Programmer*
- Steve McConnell, *Code Complete*
- Dustin Boswell dan Trevor Foucher, *The Art of Readable Code*
- Kevlin Henney (ed.), *97 Things Every Programmer Should Know*
- Google, *Google Engineering Practices* dan panduan gaya bahasa (sebagai contoh rujukan)
