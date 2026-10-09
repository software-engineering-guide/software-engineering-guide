# 2.4 Strategi pengujian

## Tinjauan dan motivasi

Strategi [pengujian](https://en.wikipedia.org/wiki/Software_testing) adalah serangkaian pilihan yang disengaja tentang apa yang diuji, pada tingkat apa, seberapa otomatis, dan hingga keyakinan seberapa, agar tim Anda dapat mengubah kode dengan cepat tanpa merusaknya. Tes adalah yang memungkinkan organisasi besar melakukan deployment sering dan aman. Tes mengkodekan perilaku yang diharapkan, menangkap regresi, dan memberi insinyur keyakinan untuk [merefaktor](https://en.wikipedia.org/wiki/Code_refactoring). Tanpa strategi yang koheren, pengujian cenderung menempuh salah satu dari dua jalan buruk: tidak ada (pengembangan yang digerakkan ketakutan dan lambat) atau membengkak (ribuan tes lambat dan goyah yang tidak dipercaya siapa pun).

Bagi tim besar, strategi lebih penting daripada tes tunggal mana pun. Ratusan insinyur yang bekerja dalam basis kode bersama membutuhkan jaring pengaman yang cepat dan andal. Tanpanya, setiap perubahan berisiko dan setiap rilis berubah menjadi cobaan manual. Tes juga berfungsi sebagai dokumentasi perilaku yang dimaksudkan yang dapat dieksekusi, yang tak ternilai begitu penulis aslinya berpindah. Strategi menentukan apakah rangkaian tes Anda adalah aset yang mempercepat pengiriman atau liabilitas yang menyeretnya.

Dalam konteks enterprise dan pemerintah, pengujian membawa bobot ekstra. Regulasi dapat mensyaratkan cakupan dan bukti pengujian yang terdokumentasi. Sistem kritis keselamatan dan yang menghadap warga menuntut jaminan tinggi. Pengujian aksesibilitas dan keamanan mungkin diwajibkan hukum. Jadi strategi harus menyeimbangkan kecepatan, keyakinan, biaya, dan kepatuhan, dan harus memperlakukan cakupan sebagai sinyal, bukan target untuk dipermainkan.

## Prinsip utama

- Uji untuk mendapatkan keyakinan mengubah, bukan untuk mencapai angka.
- Pilih tes yang cepat, andal, dan terisolasi. Tes yang lambat atau goyah mengikis kepercayaan yang membuat rangkaian tes berguna.
- Dorong tes ke tingkat terendah yang memberi keyakinan nyata, dan sisakan tes lambat dan luas untuk risiko integrasi yang sejati.
- Tes yang goyah adalah tes yang rusak. Perlakukan kegoyahan sebagai cacat kelas satu.
- Cakupan adalah sinyal, bukan tujuan. Cakupan tinggi atas kode sepele membuktikan sedikit.
- Uji perilaku dan kontrak, bukan detail implementasi, agar tes Anda bertahan dari refaktoring.
- Jadikan pengujian non-fungsional (aksesibilitas, kinerja, keamanan) bagian dari strategi, bukan renungan belakangan.

## Rekomendasi

### Gunakan piramida tes sebagai bawaan, dan kenali kritiknya

Jadikan bawaan banyak [tes unit](https://en.wikipedia.org/wiki/Unit_testing) yang cepat, lebih sedikit [tes integrasi](https://en.wikipedia.org/wiki/Integration_testing), dan sedikit tes ujung ke ujung, karena biaya dan kerapuhan naik seiring cakupan membesar. Kenali juga kritiknya: bentuknya harus mengikuti arsitektur Anda, bukan dogma. Sistem yang berat layanan mungkin memerlukan lapisan integrasi lebih besar ("testing trophy"), dan tujuan sebenarnya adalah keyakinan per satuan biaya dan kecepatan, bukan siluet tertentu. Apa pun yang Anda lakukan, hindari piramida terbalik yang sebagian besar tes ujung ke ujung yang lambat.

### Adopsi TDD, BDD, dan pengembangan berbasis spesifikasi di tempat yang membantu

Gunakan [pengembangan berbasis tes](https://en.wikipedia.org/wiki/Test-driven_development) (TDD) untuk menggerakkan desain dan menjamin kemampuan diuji, terutama untuk logika kompleks. Ini disiplin desain sama banyaknya dengan disiplin pengujian. Gunakan [pengembangan berbasis perilaku](https://en.wikipedia.org/wiki/Behavior-driven_development) (BDD) untuk mengekspresikan tes dalam bahasa domain yang Anda bagikan dengan pemangku kepentingan, yang berharga untuk kriteria penerimaan di lingkungan yang diatur atau sarat persyaratan. Pengembangan berbasis spesifikasi melangkah satu tahap lebih jauh: ia memperlakukan spesifikasi yang dapat dieksekusi (perilaku yang disepakati, diekspresikan sebagai contoh) sebagai sumber kebenaran tunggal yang memandu implementasi sekaligus memverifikasinya. Ini bersinar di tempat persyaratan harus dapat dilacak ke bukti penerimaan, seperti dalam program pemerintah dan yang diatur. Terkait ketiganya adalah **[pengujian shift-left](https://en.wikipedia.org/wiki/Shift-left_testing)**: memindahkan verifikasi sedini mungkin dalam siklus hidup, menulis tes bersamaan dengan atau sebelum kode dan menjalankannya terus-menerus, agar Anda menangkap cacat ketika paling murah diperbaiki, bukan pada fase tes akhir atau di produksi. Tak satu pun ini wajib di mana-mana. Terapkan di tempat yang menambah kejelasan.

### Gunakan teknik lanjutan untuk kode bernilai tinggi

Gunakan pengujian berbasis properti untuk memeriksa invarian di banyak masukan yang dihasilkan, menangkap kasus tepi yang terlewat tes berbasis contoh. Gunakan [fuzz testing](https://en.wikipedia.org/wiki/Fuzzing) pada parser dan batas masukan tak tepercaya untuk menemukan crash dan celah keamanan. Gunakan [mutation testing](https://en.wikipedia.org/wiki/Mutation_testing) untuk mengukur apakah tes Anda benar-benar mendeteksi kesalahan yang disuntikkan, sinyal kualitas yang jauh lebih baik daripada cakupan mentah. Gunakan pengujian snapshot dengan bijak untuk keluaran terserialisasi, dan waspadai jebakan menyetujui ulang snapshot secara membabi buta.

### Kelola data tes dan gunakan data sintetis

Buat tes deterministik dengan data tes yang terkendali dan terisolasi, dan hindari fixture mutabel bersama yang mengopel tes satu sama lain. Hasilkan [data sintetis](https://en.wikipedia.org/wiki/Synthetic_data) yang mencerminkan karakteristik produksi tanpa mengekspos informasi pribadi nyata, yang esensial di tempat aturan privasi melarang pemakaian data produksi di lingkungan tes. Sediakan factory atau builder agar setiap tes dapat membangun persis data yang dibutuhkannya.

### Perlakukan tes yang goyah sebagai cacat

Deteksi kegoyahan secara otomatis, pindahkan tes yang goyah keluar dari jalur pemblokiran, dan perbaiki atau hapus dengan tenggat. Rangkaian tes yang gagal secara acak melatih insinyur mengabaikan kegagalan, yang menghancurkan seluruh nilainya. Lacak tingkat kegoyahan dan jadikan keandalan metrik kualitas eksplisit untuk rangkaian tes itu sendiri.

### Gunakan cakupan sebagai sinyal, dan tambahkan pengujian non-fungsional

Ukur cakupan untuk menemukan area yang belum teruji, tetapi jangan jadikan target keras yang mengundang permainan dengan tes tanpa asersi. Lengkapi dengan mutation testing untuk kedalaman. Bangun pengujian aksesibilitas (pemeriksaan otomatis ditambah audit manual), pengujian kinerja (garis dasar beban dan latensi dengan deteksi regresi), dan pengujian keamanan (pemindaian dependensi, [analisis statis](https://en.wikipedia.org/wiki/Static_program_analysis), dan pengujian dinamis) ke dalam pipeline.

## Trade-off: kelebihan dan kekurangan

| Jenis tes / praktik | Kelebihan | Kekurangan |
|---|---|---|
| Tes unit | Cepat, presisi, murah, stabil | Melewatkan bug tingkat integrasi dan sistem |
| Tes integrasi | Menangkap cacat antarmuka dan pengawatan | Lebih lambat; lebih banyak persiapan; lebih rapuh |
| Tes ujung ke ujung | Keyakinan tertinggi pada perilaku nyata | Lambat, goyah, mahal dipelihara |
| TDD | Desain lebih baik, kemampuan diuji terjamin | Kurva belajar; awalnya terasa lambat |
| Pengujian berbasis properti | Menemukan kasus tepi, mengkodekan invarian | Perlu berpikir dalam properti; lebih sulit ditulis |
| Mutation testing | Ukuran sejati efektivitas tes | Mahal secara komputasi; lambat dijalankan |
| Target cakupan tinggi | Memunculkan kode yang belum teruji | Dapat dipermainkan; dapat mendorong tes bernilai rendah |

Trade-off pusatnya adalah keyakinan versus kecepatan dan biaya. Tes yang lebih luas memberi lebih banyak keyakinan tetapi berjalan lebih lambat dan lebih sering rusak. Tes yang lebih sempit cepat dan stabil tetapi melewatkan cacat tingkat sistem. Campuran yang tepat memaksimalkan keyakinan per detik umpan balik dan per jam pemeliharaan. Dan pengujian berlebihan adalah mode kegagalan nyata: rangkaian tes yang membengkak dengan tes redundan, lambat, dan rapuh dapat memakan biaya lebih daripada bug yang dicegahnya.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Tes non-fungsional mana, aksesibilitas, kinerja, dan keamanan, yang harus memblokir rilis, dan mana yang hanya melapor?** Bab ini berargumen bahwa pengujian non-fungsional termasuk dalam strategi alih-alih renungan belakangan, dan mencatat bahwa aksesibilitas dapat diwajibkan hukum dan pengujian keamanan dapat menjadi bagian dari bukti authority-to-operate. Untuk sistem besar atau yang menghadap warga, gerbang pemblokir memperlambat pengiriman, tetapi cacat aksesibilitas atau keamanan yang ditemukan di produksi membawa biaya perbaikan, reputasi, dan hukum yang jauh melampaui tesnya. Bawa sinyal yang menentukan: paparan regulasi Anda, apakah sistem menghadap warga, dan seberapa sering cacat ini saat ini lolos ke produksi. Jadikan pemeriksaan yang diwajibkan hukum sebagai pemblokir dan biarkan pemeriksaan berisiko lebih rendah melapor dengan tren, agar gerbang mencerminkan risiko nyata, bukan dogma. Jawabannya langsung menentukan apa yang dapat dan tidak dapat digabung.

2. **Apakah Anda menetapkan persentase cakupan keras sebagai gerbang, dan jika ya, apa yang mencegah insinyur mempermainkannya dengan tes tanpa asersi?** Bab ini tegas bahwa cakupan adalah sinyal, bukan tujuan, bahwa cakupan tinggi atas kode sepele membuktikan sedikit, dan bahwa target keras mengundang permainan. Satu angka yang dipaksakan di organisasi besar secara andal menghasilkan tes yang mengeksekusi kode tanpa menegaskan apa pun, yang menaikkan metrik dan menurunkan keyakinan nyata. Bawa sinyal yang lebih baik ke diskusi: skor mutation testing pada modul bernilai tertinggi Anda, yang mengukur apakah tes benar-benar mendeteksi kesalahan yang disuntikkan. Gunakan cakupan untuk menemukan area yang belum teruji dan mutation testing untuk kedalaman, dan tahan diri dari menjadikan keduanya target yang dilacak pimpinan secara terpisah. Putuskan di mana angka itu benar-benar membantu dan di mana ia hanya mengundang teater.

3. **Apa kebijakan Anda ketika rangkaian tes tumbuh terlalu lambat untuk ditunggu insinyur?** Trade-off pusat bab ini adalah keyakinan versus kecepatan dan biaya, dan menyebut pengujian berlebihan sebagai mode kegagalan nyata di mana rangkaian tes yang membengkak, redundan, dan lambat memakan biaya lebih daripada bug yang dicegahnya. Pada tim besar, waktu jalan rangkaian tes adalah pajak bersama yang dibayar pada setiap perubahan, dan rangkaian yang dipelajari orang untuk dilewati kehilangan semua nilainya. Bawa buktinya: waktu jam dinding CI, tes terlambat, dan berapa banyak cakupan ujung ke ujung redundan yang menduplikasi tes unit yang lebih murah. Dorong tes ke tingkat terendah yang memberi keyakinan nyata, paralelkan, dan hapus tes lambat yang redundan dengan tenggat. Mengoptimalkan keyakinan per detik umpan balik, bukan jumlah tes mentah, adalah tujuannya.

4. **Ketika sebuah tes menjadi goyah, siapa yang memilikinya, seberapa cepat harus diperbaiki atau dihapus, dan apa yang menegakkan tenggat itu?** Bab ini memperlakukan tes yang goyah sebagai tes yang rusak, cacat kelas satu, karena rangkaian tes yang gagal secara acak melatih tim besar mengabaikan build merah dan diam-diam menghancurkan jaring pengaman yang diandalkan semua orang. Tekanan yang bersaing itu nyata: mengarantina tes goyah membuka hambatan pengiriman hari ini tetapi berisiko menutupi bug intermiten yang sebenarnya, sementara memblokir karenanya menghentikan ratusan insinyur karena kegagalan yang mungkin murni derau. Bawa bukti yang menyelesaikannya: tingkat kegoyahan Anda saat ini, berapa lama tes berada dalam karantina sebelum ada yang menyentuhnya, dan berapa banyak tes terkarantina yang ternyata menyembunyikan cacat nyata. Tugaskan pemilik untuk setiap tes terkarantina, tetapkan tenggat keras untuk memperbaiki atau menghapus, dan lacak keandalan sebagai metrik eksplisit untuk rangkaian itu sendiri. Dalam konteks enterprise dan pemerintah di mana build hijau adalah bagian dari bukti rilis, tumpukan karantina yang tak dikelola juga liabilitas audit, karena Anda merilis berdasarkan sinyal yang secara pribadi telah Anda sepakati untuk tidak dipercaya.

5. **Apakah Anda diizinkan menggunakan data produksi di lingkungan tes, dan jika tidak, bagaimana Anda akan menghasilkan data sintetis yang cukup setia untuk menangkap cacat nyata?** Bab ini terus terang bahwa aturan privasi sering melarang data pribadi nyata dalam tes, dan bahwa data sintetis harus mencerminkan karakteristik produksi atau tes Anda memberi keyakinan palsu. Bagi organisasi besar ketegangannya antara kesetiaan dan kepatuhan: data produksi menangkap kasus tepi berantakan yang terlewat data sintetis, tetapi setiap salinannya melipatgandakan paparan dan kewajiban Anda. Bawa spesifiknya: set data mana yang membawa data pribadi atau yang diatur, apa yang sebenarnya dipersyaratkan aturan privasi dan residensi data Anda, dan seberapa baik fixture Anda saat ini mereproduksi distribusi dan kasus tepi yang terlihat di produksi. Bakukan factory atau builder agar setiap tes membangun persis data yang dibutuhkannya, dan berinvestasilah pada pembangkitan sintetis yang cocok dengan distribusi demografis dan volume nyata. Dalam program pemerintah dan yang diatur, memakai data warga di lingkungan tes bukan jalan pintas, melainkan pelanggaran yang wajib dilaporkan, jadi strategi data harus diselesaikan sebelum lingkungan pertama didirikan.

6. **Di mana TDD, BDD, atau pengembangan berbasis spesifikasi harus diharapkan alih-alih opsional, dan siapa yang memutuskan?** Bab ini menyajikannya sebagai disiplin untuk diterapkan di tempat yang menambah kejelasan, bukan mandat untuk setiap baris kode, namun tim besar mendapat manfaat dari bawaan bersama agar praktik tidak terfragmentasi tim demi tim. Trade-off-nya antara manfaat desain dan keterlacakan (spesifikasi yang dapat dieksekusi yang dapat ditinjau pakar kebijakan, tes yang bertahan dari refaktoring) dan kurva belajar nyata serta kelambatan awal yang membuat mandat menyeluruh berbalik merugikan. Bawa bukti untuk membatasi cakupannya: modul mana yang membawa logika kompleks atau tingkat kegagalan perubahan tinggi, di mana kriteria penerimaan harus dapat dilacak ke persyaratan, dan bagaimana tim yang sudah mempraktikkannya melaporkan kecepatan dan tingkat cacat. Sisakan ekspektasi untuk logika kompleks dan area sarat persyaratan, dan biarkan kode yang lebih sederhana memilih sendiri. Dalam program pemerintah dan yang diatur di mana perangkat lunak harus dapat dilacak ke hukum yang diimplementasikannya, pengembangan berbasis spesifikasi dengan bukti penerimaan yang dapat dieksekusi lebih merupakan jalan menuju authority-to-operate Anda daripada preferensi, jadi namai secara eksplisit di mana ia diwajibkan.

## Lensa sektor

**Startup.** Tim mungil tidak dapat mengisi QA, jadi buat rangkaian tes pantas dipertahankan: tes unit cepat pada setiap commit ditambah beberapa tes ujung ke ujung atas satu jalur yang membayar tagihan, dan tidak ada yang tidak akan Anda pelihara. Lewati target cakupan dan uji logika yang paling Anda takut rusak, agar Anda dapat merilis beberapa kali sehari tanpa lintasan regresi manual. Perbaiki tes goyah pada hari yang sama, karena pada tahap ini rangkaian tes yang dipelajari tim untuk diabaikan lebih buruk daripada tidak ada rangkaian sama sekali.

**Bisnis kecil.** Tanpa insinyur tes khusus dan dengan anggaran ketat, bersandarlah pada pengujian yang sudah tertanam dalam kerangka kerja dan perkakas yang sudah Anda jalankan alih-alih harness buatan sendiri yang tidak dapat Anda dukung. Prioritaskan segelintir pemeriksaan yang melindungi pendapatan dan kepercayaan pelanggan, dan gunakan CI yang di-hosting agar Anda tidak memelihara infrastruktur build sendiri. Pilih membeli pemindaian aksesibilitas dan keamanan sebagai layanan daripada membangunnya, karena satu cacat yang terlewat dapat memakan biaya lebih daripada setahun perkakas itu.

**Enterprise.** Di banyak tim, masalah strategi adalah konsistensi: bawaan piramida bersama, karantina tes goyah otomatis, dan gerbang non-fungsional yang berarti sama di mana-mana, sehingga build hijau tepercaya siapa pun yang menghasilkannya. Anggarkan waktu jalan rangkaian tes sebagai pajak bersama dan paralelkan secara agresif, karena waktu jam dinding CI dibayar pada setiap perubahan oleh setiap insinyur. Kelola skor cakupan dan mutation sebagai sinyal portofolio dengan kepemilikan jelas, bukan angka yang dilacak pimpinan secara terpisah.

**Pemerintah.** Pengadaan dan pengawasan menjadikan pengujian bukti, bukan sekadar kebersihan rekayasa. Ekspresikan aturan kelayakan dan kebijakan sebagai spesifikasi yang dapat dieksekusi yang ditinjau pakar domain, agar Anda dapat melacak perangkat lunak ke hukum yang diimplementasikannya, dan jadikan pengujian aksesibilitas dan keamanan pemblokir karena diwajibkan hukum dan bagian dari bukti authority-to-operate. Gunakan data sintetis yang dihasilkan agar cocok dengan distribusi nyata, karena data warga di lingkungan tes adalah pelanggaran yang wajib dilaporkan, dan jaga artefak tes tetap dapat diaudit agar peninjau eksternal dapat mengonfirmasi persis apa yang diverifikasi.

## Contoh

**Startup.** Sebuah startup lima orang tidak sanggup membiayai tim QA, jadi ia bersandar pada rangkaian tes unit cepat yang berjalan pada setiap commit ditambah beberapa tes ujung ke ujung yang mencakup jalur pendaftaran-ke-checkout yang membayar tagihan. Para pendiri melewatkan cakupan menyeluruh dan sebagai gantinya menguji logika yang paling mereka takut rusak, yang memungkinkan mereka merilis beberapa kali sehari tanpa lintasan regresi manual. Ketika sebuah tes goyah mulai gagal secara acak, mereka memperbaikinya pada hari yang sama, karena rangkaian tes yang dipelajari tim untuk diabaikan lebih buruk daripada tidak ada rangkaian pada tahap di mana kepercayaan adalah segalanya.

**Enterprise.** Sebuah platform e-commerce besar memelihara ribuan tes unit cepat yang berjalan pada setiap commit dalam hitungan menit, sekumpulan terfokus tes integrasi di sekitar batas pembayaran dan inventaris, dan rangkaian kecil tes ujung ke ujung untuk perjalanan checkout kritis. Tes ujung ke ujung yang goyah dikarantina otomatis dan ditugaskan untuk diperbaiki. Karena insinyur memercayai rangkaian tes, mereka melakukan deployment berkali-kali sehari, yakin bahwa build merah berarti masalah nyata.

**Pemerintah.** Sistem tunjangan nasional yang beroperasi di bawah pengawasan regulasi memakai BDD untuk mengekspresikan aturan kelayakan sebagai spesifikasi yang dapat dieksekusi yang ditinjau pakar kebijakan, yang memberi bukti yang dapat dilacak bahwa perangkat lunak mengimplementasikan hukum. Ia memakai data sintetis yang dihasilkan agar cocok dengan distribusi demografis nyata, karena aturan privasi melarang data warga di lingkungan tes. Pengujian aksesibilitas wajib dan memblokir rilis, karena layanan harus dapat digunakan semua warga. Dan pengujian keamanan adalah bagian dari bukti authority-to-operate (ATO), persetujuan formal untuk menjalankan sistem di produksi.

## Kasus bisnis: motivasi, ROI, dan TCO

Imbal hasil pengujian adalah kemampuan mengubah perangkat lunak dengan cepat dan aman, fondasi kecepatan pengiriman yang berkelanjutan. Rangkaian tes otomatis yang tepercaya menggantikan [pengujian regresi](https://en.wikipedia.org/wiki/Regression_testing) manual yang lambat dan mahal serta menangkap cacat ketika paling murah diperbaiki, sebelum rilis alih-alih di produksi. Dalam sistem yang diatur atau menghadap warga, biaya cacat produksi (perbaikan, reputasi, dan potensi paparan hukum) jauh melampaui biaya tes yang akan menangkapnya.

Biaya adopsinya nyata: Anda menulis dan memelihara tes, dan membangun infrastruktur [integrasi berkelanjutan](https://en.wikipedia.org/wiki/Continuous_integration) (CI). Tetapi biaya tidak menguji lebih tinggi dan berlipat: pengembangan yang digerakkan ketakutan yang melambat menjadi merangkak, regresi yang sering, dan proses rilis manual yang tidak dapat diskalakan. Ada juga biaya pengujian berlebihan, jadi argumennya adalah untuk strategi yang dirancang baik, bukan jumlah tes maksimum. Untuk meyakinkan pimpinan, hubungkan rangkaian tes dengan frekuensi deployment, tingkat kegagalan perubahan, dan waktu rata-rata pemulihan, dan kuantifikasi upaya pengujian manual yang digantikannya serta insiden produksi yang dicegahnya.

## Anti-pola dan jebakan

- **Pengujian kerucut es krim:** sebagian besar tes ujung ke ujung yang lambat di atas dasar unit yang tipis; lambat, goyah, mahal.
- **Cakupan sebagai target:** mengejar persentase dengan tes tanpa asersi atau sepele yang tidak membuktikan apa-apa.
- **Menguji detail implementasi:** tes yang berpasangan dengan internal yang rusak pada setiap refaktoring, menghambat perubahan.
- **Kegoyahan yang ditoleransi:** kegagalan acak yang melatih tim mengabaikan build merah.
- **Data tes mutabel bersama:** tes yang saling mengganggu dan gagal tak terduga.
- **Memakai data produksi dalam tes:** pelanggaran privasi dan kepatuhan yang menunggu terjadi.
- **Pengujian non-fungsional dilewati:** aksesibilitas, kinerja, dan keamanan baru ditemukan di produksi.
- **Rangkaian tes yang tidak dipercaya:** begitu tidak andal sehingga insinyur rutin menjalankannya ulang atau melewatinya, meniadakan tujuannya.

## Model kematangan

- **Tingkat 1, Memulai:** Pengujian manual dan reaktif; cakupan otomatis minimal; regresi sering dan tertangkap terlambat, sering oleh pengguna alih-alih rangkaian tes.
- **Tingkat 2, Mengembangkan:** Tes unit otomatis dan sebagian tes integrasi ada, tetapi rangkaian tes lambat atau goyah, kepercayaan rendah, dan praktik sangat bervariasi dari satu tim ke tim lain.
- **Tingkat 3, Membakukan:** Rangkaian tes yang seimbang, cepat, dan andal menggerbangi setiap perubahan; bawaan piramida terdokumentasi, kebijakan tes goyah, dan pengujian non-fungsional (aksesibilitas, kinerja, keamanan) ditegakkan secara konsisten di semua tim.
- **Tingkat 4, Mengelola:** Kesehatan rangkaian tes diukur dan dikendalikan terhadap garis dasar; tingkat kegoyahan, waktu jam dinding CI, skor mutation pada modul bernilai tinggi, dan tingkat cacat yang lolos dilacak dan ditinjau; cakupan adalah satu sinyal di antara beberapa, dan gerbang terpicu oleh bukti alih-alih opini.
- **Tingkat 5, Mengorkestrasi:** Teknik lanjutan (berbasis properti, mutation, fuzz) menargetkan kode bernilai tinggi; pengujian terintegrasi dengan metrik pengiriman seperti frekuensi deployment, tingkat kegagalan perubahan, dan waktu rata-rata pemulihan; organisasi terus membentuk ulang rangkaian tes sesuai arsitektur dan risikonya, mengakhiri tes redundan dan berinvestasi di tempat bukti menunjukkan cacat masih lolos.

## Gagasan untuk didiskusikan

- Bentuk apa yang sebenarnya diambil distribusi tes Anda, dan apakah cocok dengan arsitektur dan risiko Anda?
- Bagaimana Anda memutuskan kapan sepotong kode layak mendapat pengujian berbasis properti atau mutation dibandingkan tes berbasis contoh?
- Apa kebijakan Anda untuk tes goyah, dan apakah benar-benar ditegakkan?
- Bagaimana Anda menghasilkan data sintetis yang realistis tanpa membocorkan informasi sensitif?
- Di mana cakupan benar-benar membantu Anda, dan di mana ia telah dipermainkan?
- Bagaimana tes yang dihasilkan AI harus ditinjau agar menambah keyakinan alih-alih derau?

## Poin-poin utama

- Uji untuk mendapat keyakinan mengubah; optimalkan keyakinan per satuan kecepatan dan biaya.
- Gunakan piramida sebagai bawaan tetapi bentuk pengujian sesuai arsitektur Anda.
- Perlakukan tes goyah sebagai cacat dan cakupan sebagai sinyal, bukan target.
- Terapkan teknik lanjutan di tempat nilainya membenarkan biayanya.
- Sertakan pengujian aksesibilitas, kinerja, dan keamanan dalam strategi, dan gunakan data sintetis untuk melindungi privasi.

## Referensi dan bacaan lanjutan

- Kent Beck, *Test-Driven Development: By Example*
- Lisa Crispin dan Janet Gregory, *Agile Testing: A Practical Guide for Testers and Agile Teams*
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*
- Michael Feathers, *Working Effectively with Legacy Code*
- Nicole Forsgren, Jez Humble, Gene Kim, *Accelerate: The Science of Lean Software and DevOps*
- Martin Fowler, artikel tentang Test Pyramid dan pola terkait tes
