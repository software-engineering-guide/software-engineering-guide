# 6.7 Agen AI dan sistem agentik

## Tinjauan dan motivasi

**Agen AI** adalah [model bahasa besar](https://en.wikipedia.org/wiki/Large_language_model) (LLM) yang dibungkus dalam sebuah loop: ia diberi tujuan, dapat memanggil perkakas, menyimpan sedikit memori tentang apa yang telah dilakukannya, dan memutuskan sendiri langkah berikutnya sampai tujuan tercapai atau ia menyerah. Loop itulah seluruh perbedaan antara agen dan panggilan prompt-respons biasa di bab 6.3. Satu panggilan menjawab satu pertanyaan. Agen membaca email-nya, mencari di basis data, membuat tiket, memeriksa hasilnya, dan mencoba lagi. Model tidak lagi sekadar menghasilkan teks; ia memilih tindakan di sistem Anda.

Pergeseran itu mengubah masalah rekayasa. Ketika model hanya menulis kata, keluaran buruk adalah kalimat buruk. Ketika model menggerakkan perkakas, keluaran buruk dapat mengirim pesan yang salah, menghapus catatan, atau memindahkan uang. Jadi [agen cerdas](https://en.wikipedia.org/wiki/Intelligent_agent) paling baik dipahami sebagai perencana tak tepercaya yang duduk di dalam sistem tepercaya, dan sebagian besar kerja Anda tercurah untuk membatasi apa yang boleh dilakukan perencana itu. Bab ini dibangun langsung di atas fondasi LLM bab 6.3, kekhawatiran kepercayaan dan akuntabilitas bab 6.5, dan praktik platform bab 6.6.

Bagi tim besar, taruhannya bersifat organisasi sebanyak teknis. Enterprise ingin agen tersambung ke sistem internal nyata (tiket, keuangan, catatan pelanggan), yang berarti agen mewarisi kontrol akses nyata dan kewajiban manajemen perubahan nyata. Pemerintah menambah akuntabilitas publik: tindakan otonom yang memengaruhi seorang warga harus dapat dijelaskan, diawasi, dan diaudit setelah kejadian. Polanya kuat. Di-deploy tanpa disiplin, ia cara cepat mengotomatisasi kesalahan.

## Prinsip utama

- Agen adalah model ditambah loop, perkakas, memori, dan tujuan. Risiko berada di loop, bukan prosa.
- Batasi otonomi pada tugas. Beri kebebasan sesedikit mungkin yang menyelesaikan pekerjaan.
- Pilih alur kerja tetap ketika langkahnya diketahui. Raih otonomi terbuka hanya ketika tidak.
- Perlakukan setiap perkakas sebagai permukaan serangan dan beri hak istimewa paling sedikit yang masih dapat dipakainya bekerja.
- Taruh manusia dalam lingkaran untuk tindakan berdampak atau tak dapat dibalik, dan buat pembalikan murah.
- Evaluasi atas keberhasilan tugas, bukan atas bagaimana transkrip terbaca.
- Telusuri setiap proses. Tindakan yang tak dapat Anda rekonstruksi adalah tindakan yang tak dapat Anda atur.
- Desain paling sederhana yang berfungsi biasanya yang tepat. Sering itu bukan agen sama sekali.

## Rekomendasi

### Mulai dengan alur kerja, tambah otonomi hanya di mana Anda harus

Kesalahan paling umum adalah meraih agen otonom ketika pipeline tetap sudah cukup. Jika Anda sudah tahu langkahnya (ekstrak bidang, validasi, cari catatan, susun balasan), tulis itu sebagai alur kerja terorkestrasi dengan model mengisi slot tertentu. Otonomi layak tempatnya ketika jalur benar-benar tidak dapat ditentukan sebelumnya, misalnya riset terbuka atau triase lintas banyak perkakas yang mungkin. Batasi otonomi pada tugas: batasi jumlah langkah, batasi himpunan perkakas pada apa yang dibutuhkan tujuan ini, dan tetapkan kondisi berhenti yang jelas. Aturan baik adalah memberi model kebebasan persis sebanyak yang dituntut masalah dan tidak satu derajat pun lebih.

### Jadikan pemakaian perkakas kemampuan inti, dan jadikan aman

Pemakaian perkakas (juga disebut function calling) adalah yang mengubah model menjadi agen. Definisikan setiap perkakas dengan skema presisi, validasi setiap argumen yang disuplai model, dan terapkan [prinsip hak istimewa paling sedikit](https://en.wikipedia.org/wiki/Principle_of_least_privilege): agen pelaporan hanya-baca mendapat kredensial hanya-baca, tidak pernah akses tulis yang mungkin disalahgunakannya. Jalankan perkakas di dalam [sandbox](https://en.wikipedia.org/wiki/Sandbox_(computer_security)) agar panggilan buruk tak dapat menjangkau melampaui radius ledakannya. Pilih banyak perkakas sempit berfungsi tunggal daripada beberapa yang luas, karena perkakas sempit lebih mudah dinalar, diberi izin, dan diaudit. Ini adalah menahan diri yang sama yang didesakkan bab 6.3 untuk pemakaian perkakas LLM, dijadikan pusat.

### Gunakan pola penalaran dan perencanaan eksplisit

Agen bekerja lebih baik ketika pemikirannya terstruktur. Dalam pola reason-and-act (dipopulerkan oleh riset ReAct), model bergantian antara menalar situasi dan mengambil tindakan, lalu mengamati hasil sebelum menalar lagi. Untuk tujuan lebih sulit, minta model merencanakan dulu (menguraikan menjadi subtugas) lalu mengeksekusi, agar Anda dapat memeriksa dan bahkan menyetujui rencana sebelum perkakas apa pun berjalan. Jaga loop ini dapat diamati dan dapat diinterupsi. Rencana yang dapat Anda baca adalah rencana yang dapat Anda hentikan.

### Jaga manusia dalam lingkaran untuk tindakan berdampak

Putuskan, per perkakas dan per tindakan, apakah model boleh bertindak sendiri atau harus bertanya dulu. Tindakan yang dapat dibalik dan berisiko rendah (mencari, menyusun draf) dapat berjalan tanpa pengawasan. Yang berdampak atau tak dapat dibalik (mengirim komunikasi eksternal, memindahkan uang, mengubah data produksi, memutuskan kasus seorang warga) membutuhkan gerbang [human-in-the-loop](https://en.wikipedia.org/wiki/Human-in-the-loop) dengan wewenang nyata untuk mengatakan tidak. Rancang untuk reversibilitas di mana pun Anda bisa: pilih menahapkan perubahan daripada meng-commit-nya, dan jadikan undo fitur kelas satu agar tindakan keliru berbiaya menit, bukan insiden.

### Perlakukan model keamanan sebagai adversarial

Agen memperluas permukaan serangan yang dijelaskan di bab 4.2. Ancaman utamanya adalah [prompt injection](https://en.wikipedia.org/wiki/Prompt_injection): instruksi berbahaya tersembunyi di halaman web, dokumen, atau email yang dibaca dan dipatuhi agen. Berkaitan erat adalah [masalah confused deputy](https://en.wikipedia.org/wiki/Confused_deputy_problem), di mana penyerang menipu agen berhak istimewa untuk menyalahgunakan akses sahnya sendiri, misalnya mengeksfiltrasi data lewat perkakas yang boleh dipanggil agen. Asumsikan konten apa pun yang dicerna agen mungkin bermusuhan. Pisahkan instruksi tepercaya dari data tak tepercaya, batasi perkakas agar agen yang dibajak tak dapat menjangkau sistem sensitif, dan jangan pernah biarkan keluaran model mentah memicu tindakan tak dapat dibalik tanpa validasi.

### Evaluasi atas keberhasilan tugas dan uji regresi non-determinisme

Nilai agen dari apakah ia menyelesaikan tugas, bukan dari apakah transkrip terdengar pintar. Bangun himpunan evaluasi tujuan representatif dengan kriteria keberhasilan yang dapat diperiksa (apakah tiket mendapat prioritas tepat, apakah pengembalian dana sesuai kebijakan) dan jalankan pada setiap perubahan prompt, model, atau perkakas. Karena agen non-deterministik, satu kali lolos membuktikan sedikit: jalankan setiap kasus berkali-kali dan lacak tingkat keberhasilan, bukan lulus atau gagal. Ini memperluas disiplin evaluasi offline dan online bab 6.3 dan 6.2 (rekayasa pembelajaran mesin dan MLOps) ke sistem yang keluarannya berupa urutan tindakan.

### Instrumentasi proses untuk observabilitas, biaya, dan penanganan kegagalan

Anda tak dapat mengatur apa yang tak dapat Anda lihat. Telusuri setiap proses agen ujung ke ujung (bab 6.6): tujuan, setiap langkah penalaran, setiap pemanggilan perkakas beserta argumen dan hasilnya, token yang dihabiskan, dan hasil akhir. Penelusuran ini sekaligus debugger, jejak audit, dan meteran biaya Anda. Tetapkan anggaran keras pada langkah, waktu, dan pengeluaran, karena agen yang berputar dapat membakar latensi dan uang dengan cepat. Tangani kegagalan secara eksplisit: coba ulang galat perkakas sementara dengan backoff, tetapi deteksi loop di mana model mengulang tindakan yang gagal, dan gagal dengan aman alih-alih berontak.

## Trade-off: kelebihan dan kekurangan

| Pilihan | Kelebihan | Kekurangan | Terbaik ketika |
|---|---|---|---|
| Alur kerja tetap (model mengisi slot) | Dapat diprediksi, murah, mudah diuji dan diaudit | Kaku; patah pada jalur tak terduga | Langkah diketahui sebelumnya |
| Agen tunggal otonom | Fleksibel; menangani tujuan terbuka | Lebih sulit dikendalikan, dievaluasi, dan dibatasi | Jalur tidak dapat ditentukan sebelumnya |
| Orkestrasi multi-agen | Paralelisme; peran khusus | Biaya koordinasi, galat bertumpuk, pengeluaran lebih tinggi | Tugas benar-benar terurai menjadi bagian independen |
| Tindakan tanpa pengawasan | Cepat, gesekan rendah | Kesalahan dieksekusi tanpa pemeriksaan | Tindakan dapat dibalik dan berisiko rendah |
| Gerbang human-in-the-loop | Keselamatan, akuntabilitas, reversibilitas | Lebih lambat; butuh kapasitas peninjau | Tindakan berdampak atau tak dapat dibalik |

Ketegangan sentralnya adalah otonomi versus kendali. Otonomi lebih besar menangani lebih banyak situasi tetapi menuntut lebih banyak guardrail, lebih banyak evaluasi, dan lebih banyak uang, dan gagal dengan cara yang lebih sulit diprediksi. Desain multi-agen menggoda tim dengan keanggunan, namun setiap agen tambahan menambah overhead koordinasi dan satu tempat lagi bagi galat kecil bertumpuk menjadi hasil salah. Selesaikan ketegangan dengan memulai dari otonomi paling sedikit yang menyelesaikan masalah dan menambah kebebasan hanya ketika tugas konkret memaksa Anda, selalu dipasangkan dengan guardrail yang sepadan.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apakah fitur ini benar-benar membutuhkan agen, atau akankah alur kerja tetap lebih aman dan murah?** Otonomi memikat, tetapi kebanyakan pekerjaan punya langkah yang dapat diketahui yang ditangani pipeline terorkestrasi dengan risiko jauh lebih sedikit. Bagi tim besar, menjadikan agen sebagai bawaan berarti setiap kelompok memikul beban evaluasi, penelusuran, dan keamanan yang akan dihindari desain lebih sederhana. Bawa tugas spesifiknya dan tanyakan apakah langkahnya dapat ditentukan sebelumnya; jika bisa, agen kemungkinan rekayasa berlebihan. Sisihkan otonomi terbuka untuk tujuan di mana jalurnya benar-benar bervariasi per kasus. Jawabannya harus mendorong sebagian besar fitur ke alur kerja dan menyisakan himpunan kecil yang disengaja sebagai agen sejati.

2. **Untuk setiap perkakas yang dapat dipanggil agen kita, hal terburuk apa yang dapat dilakukan agen yang dibajak dengannya, dan apa yang menghentikannya?** Prompt injection dan serangan confused-deputy membalikkan akses sah agen itu sendiri melawan Anda, jadi lensa yang tepat adalah adversarial (bab 4.2). Inventarisasi setiap perkakas, cakupan hak istimewanya, dan apakah instruksi berbahaya yang diselundupkan lewat konten tercerna dapat menjangkaunya. Bagi enterprise yang menyambungkan agen ke sistem internal, di sinilah hak istimewa paling sedikit, sandboxing, dan gerbang manusia atas tindakan tak dapat dibalik menjadi nyata. Bawa daftar perkakas dan kredensial yang dipegang masing-masing. Jika tindakan berdampak apa pun dapat dicapai tanpa validasi atau pemeriksaan manusia, itulah hal pertama yang harus diperbaiki.

3. **Bagaimana kita akan tahu tingkat keberhasilan agen turun, mengingat setiap proses tampak masuk akal?** Agen non-deterministik, sehingga transkrip yang terbaca baik masih dapat mengambil tindakan salah, dan satu proses hijau tidak membuktikan apa-apa. Tanyakan apakah Anda punya himpunan evaluasi tujuan dengan hasil yang dapat diperiksa, dijalankan berkali-kali per kasus untuk menghasilkan tingkat keberhasilan alih-alih satu kali lolos. Untuk deployment berisiko tinggi atau publik, diskusikan bagaimana jejak proses memungkinkan Anda merekonstruksi persis apa yang terjadi ketika ada yang salah (bab 6.5 dan 6.6). Jika satu-satunya sinyal Anda keluhan pengguna, Anda sudah terlambat. Jawabannya harus mendanai harness evaluasi sebelum skala, bukan setelah insiden.

4. **Tindakan agen ini yang mana yang benar-benar tak dapat dibalik, siapa yang memegang wewenang menyetujuinya, dan apakah kita punya kapasitas peninjau untuk mengisi staf gerbang itu?** Godaannya adalah membiarkan model bertindak tanpa pengawasan di mana-mana, tetapi gerbang manusia hanya nyata jika orang bernama dengan wewenang mengatakan tidak tersedia saat agen bertanya. Bagi tim besar, antrean persetujuan yang tak dimiliki siapa pun diam-diam menjadi stempel karet, dan keselamatan yang Anda rancang menguap di bawah volume. Bawa daftar lengkap tindakan yang dapat diambil agen, tandai masing-masing dapat dibalik atau tak dapat dibalik, dan perkirakan volume harian kasus berkeyakinan rendah yang akan mendarat pada peninjau. Timbang gesekan dan biaya staf gerbang terhadap radius ledakan kesalahan tanpa pengawasan, dan pilih mendesain ulang tindakan tak dapat dibalik menjadi bertahap dan dapat di-undo daripada menambah peninjau lain. Dalam pengaturan enterprise dan pemerintah, kaitkan setiap tindakan berdampak dengan pejabat akuntabel dan catatan manajemen perubahan, karena tindakan otonom yang memengaruhi warga atau pelanggan yang tidak disetujui manusia mana pun adalah persis kegagalan yang akan ditemukan audit.

5. **Apakah kita meraih desain multi-agen karena tugasnya benar-benar terurai, atau karena tampak anggun?** Membagi pekerjaan ke agen khusus memikat, namun setiap agen tambahan menambah overhead koordinasi dan satu tempat lagi di mana galat kecil bertumpuk menjadi hasil salah. Bagi organisasi besar, biayanya bukan hanya pengeluaran dan latensi: sistem multi-agen jauh lebih sulit ditelusuri, dievaluasi, dan dinalar ketika gagal, sehingga beban tata kelola berlipat dengan setiap peran yang Anda tambah. Bawa tugasnya dan tunjukkan secara konkret bagian mana yang berjalan independen dan paralel, lalu bandingkan tingkat keberhasilan dan biaya terukur versi multi-agen terhadap agen tunggal pada himpunan evaluasi yang sama. Jika agen tunggal menang atau seri, desain anggun itu rekayasa berlebihan. Untuk deployment teregulasi atau publik, ingat bahwa setiap agen dalam rantai adalah komponen lain yang harus dapat diperiksa badan pengawas, jadi struktur tambahan yang tak dapat Anda benarkan adalah liabilitas tambahan.

6. **Apa anggaran keras pada langkah, waktu, dan pengeluaran agen, dan bagaimana agen yang berputar akan tertangkap sebelum menaikkan biaya atau latensi?** Agen yang mengulang tindakan gagal dapat membakar uang dan waktu tanpa peringatan, sehingga otonomi tak terbatas adalah risiko finansial sebanyak risiko keselamatan. Bagi tim besar yang menjalankan banyak agen, satu loop yang berperilaku buruk dapat melonjakkan tagihan cloud atau menghabiskan batas laju yang membuat kelaparan setiap beban kerja lain, yang menjadikan batas per proses perhatian operasional bersama alih-alih masalah satu tim. Bawa anggaran langkah, waktu, dan token saat ini untuk setiap agen, peringatan yang menyala ketika proses melampauinya, dan deteksi loop yang gagal dengan aman alih-alih berontak. Timbang anggaran ketat, yang mungkin memotong tugas yang sah sulit, terhadap yang longgar yang membiarkan biaya lepas kendali. Dalam pengaturan enterprise dan pemerintah di mana pengeluaran harus diperkirakan dan dibenarkan, agen yang biayanya tak terbatas adalah butir baris yang tak dapat Anda bela dalam tinjauan anggaran atau audit.

## Lensa sektor

**Startup.** Kirim satu agen sempit yang menyentuh nilai inti Anda, di model ter-hosting, dengan himpunan perkakas terkecil yang menyelesaikan pekerjaan dan batas keras pada langkah dan pengeluaran. Tolak demo multi-agen: perhatian rekayasa langka Anda lebih baik dihabiskan membatasi otonomi satu agen dan menelusuri prosesnya daripada mengoordinasi peran yang tak dapat Anda pelihara. Jaga setiap tindakan berdampak di balik satu gerbang "susun draf, jangan pernah kirim" agar kesalahan berbiaya satu klik untuk di-undo, bukan insiden.

**Bisnis kecil.** Anda tidak punya siapa pun untuk menjalankan harness evaluasi atau sandbox, jadi pilih agen yang tertanam dalam perkakas yang sudah Anda percaya, dan aktifkan hanya otonomi yang dapat Anda awasi dengan mata. Perlakukan agen apa pun yang dapat mengirim, membayar, atau menghapus atas nama Anda sebagai sesuatu untuk dimatikan sampai orang mengonfirmasi setiap tindakan, karena pesan otomatis yang salah kepada pelanggan merugikan hubungan Anda. Pilih vendor yang menunjukkan apa yang dilakukan agen dan membiarkan Anda mematikan otomasi.

**Enterprise.** Masalahnya mengatur agen lintas banyak tim: pola bersama untuk membatasi otonomi, kredensial perkakas hak istimewa paling sedikit, sandboxing, gerbang human-in-the-loop, dan penelusuran ujung ke ujung agar tak ada kelompok menciptakan ulang guardrail. Sambungkan agen ke sistem internal di bawah kontrol akses yang sama seperti yang dipegang manusia, gerbangi tindakan tak dapat dibalik di balik penyetuju bernama dan manajemen perubahan, dan kelola portofolio dengan metrik tingkat keberhasilan, anggaran per proses, dan pengujian injeksi adversarial. Bakukan lapisan penelusuran dan evaluasi agar perilaku agen mana pun dapat direkonstruksi dan diaudit.

**Pemerintah.** Pengadaan, transparansi, dan akuntabilitas publik membatasi setiap pilihan. Jaga agen pada mengumpulkan fakta dan menyusun draf, dan sisihkan setiap keputusan yang memengaruhi warga untuk manusia akuntabel, karena tanggung jawab atas keputusan sektor publik tidak dapat didelegasikan kepada model. Catat setiap proses agar badan pengawas dapat melihat sumber mana yang dikonsultasikan dan apa yang dilakukan, tuntut vendor mengungkap perkakas dan keterbatasan agen, dan buktikan lewat himpunan evaluasi adversarial bahwa agen menolak bertindak melampaui kewenangan terbatasnya.

## Contoh

**Startup.** Startup analitik lima orang membangun agen triase dukungan. Ia membaca tiket masuk, mencari di dokumen, dan entah menyusun balasan atau merutekan tiket ke manusia, dan itulah seluruh himpunan perkakasnya. Kredensialnya hanya-baca ditambah satu tindakan "buat draf" yang tak pernah mengirim tanpa orang mengeklik kirim. Setiap proses ditelusuri agar para pendiri dapat melihat mengapa tiket dirutekan ke tempatnya, dan himpunan evaluasi malam berisi lima puluh tiket nyata menjalankan agen lima kali masing-masing untuk melacak tingkat akurasi perutean. Ketika demo multi-agen cerdas pesaing menggoda mereka, mereka tetap agen tunggal karena tugas mereka tidak terurai.

**Enterprise.** Sebuah bank membangun agen untuk membantu staf operasi merekonsiliasi pembayaran gagal. Ia terintegrasi dengan sistem internal di bawah kontrol akses yang sama seperti yang dimiliki klerk manusia, diberikan lewat kredensial layanan hak istimewa paling sedikit yang dicakup hanya untuk rekonsiliasi. Agen boleh menyelidiki bebas (membaca buku besar, mencari riwayat transaksi) tetapi tindakan apa pun yang memindahkan uang atau mengedit catatan ditahapkan dan membutuhkan penyetuju manusia bernama, memenuhi manajemen perubahan. Dokumen tercerna diperlakukan sebagai tak tepercaya untuk menumpulkan prompt injection, perkakas berjalan dalam sandbox, dan setiap proses ditelusuri ujung ke ujung untuk audit. Himpunan evaluasi offline menggerbangi setiap perubahan model atau prompt, dan anggaran per proses membatasi langkah dan pengeluaran agar agen yang berputar tak dapat menaikkan biaya atau latensi.

**Pemerintah.** Sebuah lembaga tunjangan melakukan percontohan agen untuk membantu petugas kasus menghimpun fakta suatu klaim: menarik catatan, memeriksa aturan kelayakan, dan menyusun ringkasan. Lembaga menarik garis tegas: agen mengumpulkan dan menyusun draf, tetapi petugas kasus manusia membuat dan memiliki setiap keputusan yang memengaruhi warga, karena akuntabilitas atas keputusan sektor publik tidak dapat didelegasikan kepada model (bab 6.5). Setiap proses dicatat penuh, menunjukkan sumber mana yang dikonsultasikan dan apa yang disusun, agar badan pengawas dapat mengaudit kasus mana pun. Otonomi sengaja dibatasi pada baca-dan-susun, perkakas berhak istimewa paling sedikit dan ter-sandbox, dan himpunan evaluasi adversarial memastikan agen menolak bertindak melampaui mengumpulkan fakta.

## Kasus bisnis: motivasi, ROI, dan TCO

Agen memberi imbal hasil dengan mengotomatisasi pekerjaan multilangkah yang dulu membutuhkan orang untuk mengeklik antarsistem: triase, rekonsiliasi, riset, dan operasi rutin. Nilai tampak sebagai pekerjaan selesai tanpa manusia di setiap langkah, waktu siklus lebih cepat, dan staf dibebaskan untuk tugas padat penilaian. Karena agen dibangun di atas LLM dan perkakas yang ada, waktu ke prototipe yang berfungsi singkat, yang persis mengapa tim membangun berlebihan.

Total biaya kepemilikan adalah tempat agen berbeda dari fitur LLM biasa. Di atas biaya inferensi Anda membayar integrasi perkakas, perpipaan sandboxing dan izin, harness evaluasi, tumpukan penelusuran dan observabilitas (bab 6.6), dan peninjau manusia yang mengisi staf gerbang persetujuan. Agen yang berputar atau terbatas buruk menambah biaya variabel yang dapat melonjak tanpa peringatan, jadi anggaran pada langkah dan pengeluaran adalah bagian dari desain, bukan renungan belakangan. Biaya tidak mengadopsi adalah operasi lebih lambat dan kerja manual membosankan yang diotomatisasi pesaing Anda. Biaya mengadopsi dengan sembrono adalah tindakan otonom yang mengirim pesan salah, membocorkan data, atau membuat keputusan tanpa akuntabilitas. Ajukan kasus kepada pimpinan dengan memasangkan satu target otomasi konkret dengan rencana konkret untuk guardrail, evaluasi, dan pengawasan manusia, dan dengan jujur bahwa guardrail adalah sebagian besar biayanya.

## Anti-pola dan jebakan

- **Agen ketika alur kerja sudah cukup.** Menanggung risiko penuh otonomi untuk tugas yang langkahnya dapat diketahui.
- **Perkakas dan kredensial terlalu luas.** Satu perkakas "lakukan apa saja" alih-alih yang sempit berhak istimewa paling sedikit.
- **Buta prompt injection.** Memberi konten tak tepercaya kepada agen yang memegang hak istimewa nyata.
- **Tanpa gerbang manusia pada tindakan tak dapat dibalik.** Membiarkan model mengirim, membayar, atau menghapus tanpa pemeriksaan.
- **Teater multi-agen.** Membagi tugas sederhana ke banyak agen, membayar biaya koordinasi tanpa keuntungan.
- **Evaluasi berbasis firasat.** Menilai dari bagaimana transkrip terbaca alih-alih tingkat keberhasilan tugas.
- **Loop tak terbatas.** Tanpa batas langkah, waktu, atau pengeluaran, sehingga agen macet membakar uang dan latensi.
- **Proses tak ditelusuri.** Tanpa catatan apa yang dilakukan agen, membuat Anda tak dapat men-debug, mengaudit, atau mempertanggungjawabkan.

## Model kematangan

- **Tingkat 1, Memulai:** Agen diprototipekan ad hoc dengan akses perkakas luas dan tanpa batas. Keberhasilan dinilai dari demo, secara reaktif, setelah ada yang rusak. Tidak ada himpunan evaluasi, penelusuran, atau gerbang manusia pada tindakan berdampak.
- **Tingkat 2, Mengembangkan:** Sebagian agen punya loop terbatas dan perkakas hak istimewa paling sedikit, dan penelusuran dasar ada, tetapi praktik bervariasi antartim. Himpunan evaluasi manual menangkap regresi kasar di beberapa proyek sementara yang lain tidak punya. Persetujuan manusia menjaga tindakan tak dapat dibalik yang paling jelas, namun cakupannya tidak merata dan tak terdokumentasi.
- **Tingkat 3, Membakukan:** Pola bersama mengatur otonomi, izin perkakas, sandboxing, dan gerbang human-in-the-loop, didokumentasikan dan ditegakkan di setiap tim. Setiap tindakan berdampak digerbangi atau divalidasi, agen ditelusuri ujung ke ujung, dan himpunan evaluasi otomatis dengan penilaian tingkat keberhasilan berjalan pada setiap perubahan. Prompt injection diperlakukan sebagai ancaman tetap dengan respons terdefinisi.
- **Tingkat 4, Mengelola:** Portofolio agen diukur dan dikendalikan terhadap garis dasar. Tingkat keberhasilan per tugas, tingkat lolos pertahanan prompt-injection, biaya dan jumlah langkah per proses, latensi persetujuan manusia, dan insiden loop atau kegagalan dilacak sebagai metrik; ambang rollback dan hentikan ditegakkan atas bukti itu alih-alih keluhan. Anggaran per proses pada langkah, waktu, dan pengeluaran dipantau, dan regresi pada metrik mana pun memicu tindakan sebelum skala, bukan setelah insiden.
- **Tingkat 5, Mengorkestrasi:** Otonomi dicocokkan dengan risiko tugas lewat kebijakan dan disesuaikan terus-menerus seiring hasil masuk. Evaluasi offline dan online berkelanjutan mengikat perilaku agen pada hasil bisnis, dan organisasi rutin memensiunkan, menentukan ulang cakupan, atau memberi izin ulang agen seiring gambaran risiko bergeser. Penelusuran, anggaran biaya, dan jejak audit seragam di seluruh portofolio; pertahanan injeksi dan confused-deputy diuji secara adversarial; akuntabilitas atas tindakan otonom jelas dan dapat diaudit.

## Gagasan untuk didiskusikan

1. Fitur LLM Anda saat ini yang mana diam-diam telah menjadi agen, dan apakah otonomi masing-masing telah dibatasi dengan sengaja?
2. Untuk setiap perkakas agen, apa cara termurah penyerang menyalahgunakannya lewat konten yang disuntikkan, dan apa yang menghentikannya?
3. Di mana Anda memilih desain multi-agen, dan dapatkah Anda menunjukkan biaya koordinasi terbayar dibanding agen tunggal?
4. Tindakan agen mana yang benar-benar tak dapat dibalik, dan dapatkah setiap darinya didesain ulang menjadi dapat dibalik atau bertahap?
5. Jika agen mengambil tindakan merugikan besok, dapatkah Anda merekonstruksi persis apa yang dilakukannya dan siapa yang akuntabel?

## Poin-poin utama

- Agen adalah LLM dalam loop dengan perkakas, memori, dan tujuan. Risiko berada di loop dan perkakas, bukan teks.
- Pilih alur kerja tetap ketika langkahnya diketahui; sisihkan otonomi untuk tujuan yang benar-benar terbuka dan batasi ketat.
- Pemakaian perkakas adalah kemampuan inti. Beri setiap perkakas hak istimewa paling sedikit, skema tervalidasi, dan sandbox.
- Gerbangi tindakan berdampak dan tak dapat dibalik di balik manusia dengan wewenang nyata, dan rancang untuk pembalikan murah.
- Perlakukan agen sebagai adversarial: bertahan dari prompt injection dan penyalahgunaan confused-deputy (bab 4.2).
- Evaluasi atas tingkat keberhasilan tugas di banyak proses, dan telusuri setiap proses untuk debugging, kendali biaya, dan audit (bab 6.5 dan 6.6).
- Sering jawaban yang tepat adalah tidak membangun agen sama sekali.

## Referensi dan bacaan lanjutan

- Shunyu Yao et al., *ReAct: Synergising Reasoning and Acting in Language Models*.
- Timo Schick et al., *Toolformer: Language Models Can Teach Themselves to Use Tools*.
- Anthropic, *Building Effective Agents* (panduan rekayasa tentang alur kerja versus agen).
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications* (termasuk prompt injection dan excessive agency).
- Simon Willison, tulisan tentang prompt injection dan "lethal trifecta" untuk agen AI.
- Norman Hardy, *The Confused Deputy* (pernyataan klasik masalah confused-deputy).
- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Stuart Russell dan Peter Norvig, *Artificial Intelligence: A Modern Approach* (agen cerdas dan tindakan rasional).
