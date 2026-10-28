# 6.8 Evaluasi dan pengujian AI

## Tinjauan dan motivasi

Menguji perangkat lunak biasa bertumpu pada asumsi yang menenangkan: diberi masukan yang sama, program mengembalikan keluaran yang sama, dan Anda dapat menegaskan persis apa keluaran itu seharusnya. Kecerdasan buatan mematahkan asumsi itu. Model dapat menjawab pertanyaan yang sama dengan dua cara berbeda, keduanya dapat diterima. Ia dapat dinilai pada spektrum dari salah hingga brilian alih-alih lulus atau gagal. Dan sering tidak ada satu jawaban benar untuk dijadikan pegangan. Maka disiplin evaluasi, mengukur seberapa baik model berperilaku di banyak kasus representatif alih-alih memeriksa satu keluaran terhadap satu nilai yang diharapkan, menjadi tulang punggung sistem AI tepercaya mana pun. Ketika tim mengirim fitur AI yang mempermalukan mereka, akar penyebabnya hampir selalu mereka tak punya cara serius mengukur kualitas sebelum rilis.

Bagi tim besar, evaluasi adalah yang membuat perubahan aman. Anda akan menukar model, menulis ulang prompt, menyetel pengambilan, dan menambah perkakas, dan setiap perubahan itu dapat diam-diam menurunkan perilaku yang Anda kira kokoh. Tanpa cara terulang untuk mengukur kualitas, setiap perubahan adalah judi dan setiap regresi ditemukan oleh pengguna. Bab ini adalah pendamping pengukuran bagi bab-bab pembangunan: AI generatif dan aplikasi LLM (bab 6.3), agen AI dan sistem agentik (bab 6.7), dan rekayasa pembelajaran mesin dan MLOps (bab 6.2). Ia memperluas strategi pengujian umum Anda (bab 2.4) ke dunia probabilistik.

Pengaturan enterprise dan pemerintah menaikkan taruhan lebih jauh. Enterprise yang menjalankan puluhan fitur AI membutuhkan platform evaluasi bersama agar setiap tim tidak menciptakan ulang penilaian dari nol. Lembaga pemerintah membutuhkan evaluasi yang terdokumentasi dan dapat diaudit, karena "kami sudah mengujinya" harus menjadi "ini buktinya, dataset-nya, metriknya, dan persetujuannya." Evaluasi adalah tempat AI yang bertanggung jawab dan tepercaya (bab 6.5) berhenti menjadi pernyataan nilai dan menjadi sesuatu yang dapat Anda tunjukkan kepada regulator.

## Prinsip utama

- Perlakukan evaluasi sebagai produk kelas satu, bukan renungan belakangan yang ditempel sebelum peluncuran.
- Ukur dengan data representatif yang mencerminkan pemakaian nyata, bukan contoh mainan yang menyanjung model.
- Padukan evaluasi offline untuk iterasi cepat dengan evaluasi online untuk kebenaran dasar.
- Jadikan penilaian manusia jangkar Anda, dan kalibrasi setiap penilai otomatis terhadapnya.
- Jaga himpunan evaluasi Anda dari kontaminasi, atau angka Anda akan berbohong.
- Sambungkan evaluasi ke integrasi berkelanjutan sebagai gerbang, agar kualitas tak dapat diam-diam mundur.
- Terus ukur di produksi, karena kualitas menyimpang bahkan ketika kode Anda tidak berubah.

## Rekomendasi

### Adopsi pengembangan berbasis eval

Sebelum Anda menyetel prompt atau memilih model, tulis evaluasinya. Ini mencerminkan pengembangan berbasis pengujian: Anda mendefinisikan apa arti "baik" dalam istilah terukur, lalu membangun ke arahnya. Evaluasi di sini berarti dataset masukan yang dipasangkan dengan metode penilaian yang mengembalikan angka atau nilai untuk setiap keluaran. Mulailah kecil. Dua puluh kasus yang dipilih cermat yang mencerminkan maksud pengguna nyata mengalahkan seribu kasus acak. Tumbuhkan himpunan seiring Anda belajar di mana sistem gagal, menambahkan setiap kegagalan produksi kembali sebagai kasus permanen agar kesalahan yang sama tak dapat kembali tanpa disadari.

Pengembangan berbasis eval mengubah perilaku tim. Ketika definisi baik tertulis dan dapat dijalankan, perdebatan tentang apakah perubahan membantu menjadi dapat diperiksa alih-alih urusan selera. Jadikan himpunan eval artefak yang ditinjau dalam kontrol versi, tepat di samping prompt dan kode yang diukurnya.

### Pisahkan evaluasi offline dan online, dan pakai keduanya

Evaluasi offline menjalankan dataset tetap melalui sistem Anda dalam pengaturan terkendali, cepat, murah, dan dapat diulang, agar Anda dapat membandingkan versi sebelum apa pun dikirim. Evaluasi online mengukur sistem langsung dengan pengguna nyata lewat metrik seperti penyelesaian tugas, tingkat eskalasi, umpan balik jempol naik dan turun, dan hasil bisnis hilir. Offline memberi tahu apakah perubahan kemungkinan aman; online memberi tahu apakah ia benar-benar berhasil. Anda butuh keduanya, karena himpunan offline tak pernah sepenuhnya menangkap kenyataan dan sinyal online tiba terlalu terlambat untuk menjadi satu-satunya guardrail Anda.

Sambungkan keduanya menjadi loop. Ketika metrik online turun atau pengguna menandai jawaban buruk, tangkap kasus itu, beri label, dan masukkan ke himpunan offline. Alirkan eksperimen melalui perbandingan terkendali yang sama seperti yang Anda pakai untuk perubahan produk apa pun, yang merupakan wilayah analitik produk dan eksperimen (bab 7.4). Uji A/B yang menunjukkan model baru menaikkan keberhasilan tugas lebih berharga daripada skor offline mana pun, namun skor offline-lah yang membuat Anda berani menjalankan ujinya.

### Bangun himpunan eval representatif dan jaga dari kontaminasi

Evaluasi Anda hanya sejujur datanya. Bangun dataset emas, koleksi masukan terkurasi dengan keluaran yang diharapkan atau rubrik penilaian yang telah diperiksa, yang mencerminkan distribusi nyata apa yang ditanyakan pengguna: kasus umum, kasus langka-tetapi-kritis, kasus adversarial, dan kasus yang saat ini salah ditangani sistem Anda. Stratifikasi agar Anda dapat membaca kualitas per segmen alih-alih menyembunyikan kategori gagal di dalam rata-rata yang lumayan. Minta pakar ranah memeriksa jawaban yang diharapkan, karena himpunan emas yang dibangun di atas jawaban salah lebih buruk daripada tidak ada.

Lalu lindungi data itu dari kontaminasi. Kontaminasi himpunan uji terjadi ketika contoh evaluasi Anda bocor ke data pelatihan model atau ke prompt itu sendiri, sehingga model tampak berkinerja baik karena secara efektif telah melihat jawabannya. Inilah mengapa model dapat mencetak skor cemerlang pada tolok ukur publik dan tersandung pada lalu lintas nyata Anda. Jaga sebagian data eval Anda privat dan jangan pernah mengirimnya ke pihak ketiga yang tak dapat Anda percaya. Segarkan himpunan seiring waktu. Waspadai kebocoran lebih halus di mana pengembang menyetel prompt dengan tangan terhadap himpunan eval sampai skornya tak bermakna, bentuk overfitting pada uji alih-alih perbaikan sejati. Sisihkan himpunan segar yang hanya Anda lihat sesekali.

### Pilih metrik yang sesuai tugas

Cocokkan pengukuran Anda dengan bentuk keluaran. Untuk klasifikasi dan ekstraksi, di mana ada label benar, metrik klasik berlaku: [presisi dan recall](https://en.wikipedia.org/wiki/Precision_and_recall) (dari item yang Anda tandai, berapa yang benar, dan dari item yang benar, berapa yang Anda temukan), [skor-F](https://en.wikipedia.org/wiki/F-score) yang menyeimbangkannya, dan akurasi exact-match. Untuk apa pun di mana probabilitas yang yakin penting, ukur [kalibrasi](https://en.wikipedia.org/wiki/Calibration_(statistics)), apakah keyakinan 80 persen yang dinyatakan benar sekitar 80 persen waktu, karena model terkalibrasi baik yang tahu kapan ia tidak yakin jauh lebih aman daripada yang terlalu percaya diri.

Keluaran generatif lebih sulit. Metrik berbasis referensi seperti [BLEU](https://en.wikipedia.org/wiki/BLEU) dan ROUGE, awalnya dibuat untuk terjemahan mesin dan perangkuman, membandingkan teks yang dihasilkan terhadap teks referensi dengan menghitung kata dan frasa yang tumpang tindih. Mereka murah dan dapat diulang, dan proksi lemah untuk kualitas: mereka menghargai tumpang tindih permukaan dan menghukum jawaban benar yang dirumuskan berbeda dari referensi. Pakai sebagai sinyal regresi kasar, bukan sebagai definisi baik Anda. Untuk tugas terbuka, penilaian berbasis rubrik bekerja lebih baik: definisikan kriteria eksplisit (apakah membumi, lengkap, aman, dan terformat benar) dan nilai masing-masing. Rubrik membuat kualitas subjektif terbaca dan dapat ditinjau.

### Pakai LLM-as-a-judge, tetapi kalibrasi terhadap manusia

Menilai keluaran generatif dengan tangan tidak berskala, jadi tim makin memakai [model bahasa besar](https://en.wikipedia.org/wiki/Large_language_model) yang kuat sebagai juri otomatis, memberinya prompt berisi masukan, keluaran, dan rubrik, dan memintanya menilai. Pendekatan LLM-as-a-judge ini cepat dan mengejutkan mampu, dan membawa bias nyata yang harus Anda kelola. Juri cenderung menyukai jawaban lebih panjang, menyukai opsi pertama yang ditampilkan dalam perbandingan berpasangan (bias posisi), menghargai gaya tulisan mereka sendiri, dan dapat digoyahkan oleh penalaran fasih namun salah. Dibiarkan tanpa pemeriksaan, juri bias memberi Anda angka yang yakin, presisi, dan salah.

Kalibrasi juri terhadap label manusia. Minta orang menilai sampel, lalu periksa seberapa baik juri model sepakat dengan mereka, dan terus setel prompt juri sampai kesepakatan cukup tinggi untuk dipercaya. Kurangi bias yang diketahui dengan sengaja: acak urutan opsi, kendalikan panjang, dan minta skor berjangkar rubrik dengan alasan alih-alih angka telanjang. Perlakukan juri sebagai instrumen ukur yang butuh kalibrasi ulang berkala, bukan orakel tetap. Saat membangun juri, pilih secara bawaan model paling mumpuni yang tersedia, karena juri lemah adalah penggaris lemah.

### Jaga manusia dalam lingkaran untuk kebenaran dasar

Evaluasi manusia tetap menjadi jangkar yang menjadi ukuran setiap metrik otomatis, jadi berinvestasilah melakukannya dengan baik. Tulis panduan anotasi yang jelas, latih anotator Anda, dan ukur kesepakatan antar-anotator, tingkat di mana peninjau independen memberi nilai sama pada kasus yang sama. Kesepakatan rendah biasanya berarti rubrik Anda ambigu, bukan peninjau Anda ceroboh, jadi perbaiki rubriknya. Untuk ranah berisiko tinggi, pakai pakar berkualifikasi, bukan pekerja kerumunan yang kurang konteks untuk menilai jawaban hukum atau medis.

### Red-team untuk keselamatan dan ketahanan adversarial

Himpunan eval standar mengukur apakah sistem melakukan hal benar pada masukan yang wajar. [Red teaming](https://en.wikipedia.org/wiki/Red_team), sengaja menyerang sistem Anda sendiri untuk menemukan di mana ia berperilaku salah, mengukur apa yang terjadi di bawah tekanan. Selidiki prompt injection, jailbreak, konten tidak aman, kebocoran privasi, dan keluaran bias. Jadikan rangkaian yang dapat diulang, bukan latihan sekali jalan: ubah setiap serangan berhasil menjadi kasus regresi permanen agar kerentanan yang diperbaiki tetap diperbaiki. Pekerjaan ini terhubung langsung dengan AI yang bertanggung jawab dan tepercaya (bab 6.5), dan dalam pengaturan teregulasi sering menjadi bukti yang memenuhi tinjauan keselamatan.

### Evaluasi agen berdasarkan keberhasilan tugas ujung ke ujung

Agen yang merencanakan dan bertindak dalam banyak langkah tidak dapat dinilai satu keluaran sekali. Yang penting adalah apakah seluruh tugas berhasil: apakah agen memesan rapat, menyelesaikan tiket, atau menuntaskan alur kerja dengan benar dan aman. Bangun evaluasi tingkat-tugas dalam lingkungan ter-sandbox di mana agen dapat bertindak terhadap fixture realistis namun aman, dan nilai hasil akhir ditambah trajektori, yakni urutan langkah dan pemanggilan perkakas yang diambilnya untuk sampai ke sana. Jawaban benar yang dicapai lewat jalur berbahaya atau boros tetap masalah. Ini esensial bagi agen AI dan sistem agentik (bab 6.7), di mana satu tindakan salah dapat berkonsekuensi nyata.

### Sambungkan evaluasi ke CI dan pantau produksi

Jadikan evaluasi otomatis. Jalankan rangkaian offline Anda dalam [integrasi berkelanjutan](https://en.wikipedia.org/wiki/Continuous_integration) (CI) pada setiap perubahan prompt, model, atau pengambilan, dan gerbangi merge padanya seperti Anda menggerbangi pada unit test, praktik yang berakar pada strategi pengujian Anda yang lebih luas (bab 2.4). Karena skor berisik, gerbangi pada ambang dan tren alih-alih menuntut satu proses sempurna, dan gagalkan build ketika metrik kunci turun di bawah lantainya atau mundur melampaui margin yang ditetapkan. Lalu terus awasi di produksi: pantau sinyal kualitas, distribusi keluaran, dan drift masukan agar Anda menangkap degradasi lambat yang dilewatkan uji offline, yang terkait dengan praktik observabilitas rekayasa pembelajaran mesin dan MLOps (bab 6.2). Model yang akurat saat peluncuran dapat meluruh ketika dunia yang dideskripsikannya berubah di bawahnya.

## Trade-off: kelebihan dan kekurangan

| Pendekatan evaluasi | Kelebihan | Kekurangan | Terbaik ketika |
|---|---|---|---|
| Evaluasi manusia | Fidelitas tertinggi, menangkap nuansa | Lambat, mahal, sulit diskalakan | Kebenaran dasar, berisiko tinggi, mengkalibrasi juri |
| LLM-as-a-judge | Cepat, murah, berskala ke himpunan besar | Bias, butuh kalibrasi | Proses offline sering atas keluaran generatif |
| Metrik berbasis referensi (BLEU, ROUGE) | Murah, deterministik, dapat diulang | Proksi lemah untuk kualitas nyata | Sinyal regresi kasar, bukan vonis akhir |
| Metrik klasik (presisi, recall, skor-F) | Objektif, dipahami baik | Hanya cocok untuk tugas dengan label benar | Klasifikasi, ekstraksi, pengambilan |
| Tolok ukur publik | Dapat dibandingkan antarmodel, tanpa penyiapan | Kontaminasi, kecocokan buruk dengan tugas Anda | Penyaringan awal model, bukan gerbang rilis |
| Evaluasi online (A/B, umpan balik) | Mencerminkan pengguna dan hasil nyata | Lambat, tiba setelah paparan | Mengonfirmasi perubahan benar-benar membantu |

Ketegangan sentralnya adalah kecepatan versus fidelitas. Evaluasi manusia paling tepercaya dan paling tidak berskala; penilaian otomatis sebaliknya. Resolusinya adalah melapisi keduanya: pakai metode cepat dan murah untuk iterasi konstan, jangkarkan metode itu pada penilaian manusia lewat kalibrasi rutin, dan sisihkan tinjauan manusia penuh untuk keputusan berisiko tertinggi dan untuk memeriksa bahwa metrik murah Anda masih melacak kenyataan. Ketegangan kedua adalah kenyamanan offline versus kebenaran online. Himpunan offline memungkinkan Anda bergerak cepat tetapi tak pernah sepenuhnya mencerminkan produksi, jadi perlakukan skor offline kuat sebagai izin menjalankan uji online yang cermat, bukan bukti bahwa Anda selesai.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Apa batas "cukup baik" kita, dan siapa yang memiliki himpunan eval yang mendefinisikannya?** Setiap fitur AI punya ambang kualitas implisit, dan ketika tetap implisit, tiap insinyur menetapkan ambangnya sendiri berdasarkan perasaan dan sengketa diselesaikan oleh siapa pun yang paling senior di ruangan. Menuliskan batas sebagai himpunan eval yang dapat dijalankan dengan skor target per segmen mengubah sengketa itu menjadi pertanyaan terukur. Bawa definisi keberhasilan Anda saat ini, data di baliknya, dan catatan jujur siapa yang benar-benar memeliharanya, karena himpunan eval tanpa pemilik membusuk secepat kode tak terurus lainnya. Putuskan apakah batas berbeda menurut tingkat risiko, karena jawaban hukum yang menghadap publik harus melewati batas lebih tinggi daripada bantuan curah gagasan internal. Jawabannya harus memberi tahu apakah ada yang saat ini dapat mengirim perubahan AI tanpa pengukuran apa pun berdiri di antara mereka dan pengguna.

2. **Bagaimana kita tahu angka evaluasi kita jujur dan bukan terkontaminasi atau overfit?** Skor hanya berguna jika memprediksi kualitas dunia nyata, dan ada banyak cara ia berhenti melakukannya: data tolok ukur bocor ke pelatihan, pengembang menyetel prompt terhadap himpunan uji sampai angkanya tak bermakna, atau dataset emas yang dibangun di atas jawaban yang tak pernah diverifikasi. Bawa bukti tentang dari mana data eval Anda berasal, berapa banyak yang dijaga privat, dan seberapa sering disegarkan. Diskusikan apakah Anda menjaga holdout segar yang jarang dilihat, agar Anda punya setidaknya satu angka yang tak pernah dioptimalkan siapa pun. Jika Anda tak dapat menjelaskan mengapa skor Anda akan tetap berlaku pada data yang tak pernah dipengaruhi model, Anda mengukur bayangan Anda sendiri.

3. **Di mana manusia tetap dalam lingkaran, dan bagaimana kita menjaga juri otomatis tetap terkalibrasi terhadap mereka?** LLM-as-a-judge dan metrik referensi memungkinkan Anda menilai pada skala besar, dan mereka menyimpang dari penilaian manusia dengan cara yang tak terlihat kecuali Anda memeriksa. Bawa tingkat kesepakatan Anda saat ini antara penilaian otomatis dan tinjauan manusia, seberapa baru Anda mengukurnya, dan bias mana (panjang, posisi, gaya) yang telah Anda uji. Putuskan keputusan mana yang membutuhkan penilai manusia terlepas dari biaya, biasanya yang berisiko tertinggi dan yang dipakai untuk mengkalibrasi ulang juri otomatis. Bicarakan kualitas anotasi juga, karena juri yang dikalibrasi terhadap label manusia tak konsisten mewarisi ketidakkonsistenan itu. Jawabannya harus menghasilkan jadwal kalibrasi ulang, bukan restu sekali jalan.

4. **Perubahan AI mana yang digerbangi evaluasi hari ini, dan mana yang masih mencapai pengguna hanya berdasarkan keyakinan seseorang?** Gerbang yang berjalan pada sebagian perubahan tetapi tidak yang lain memberi Anda ilusi keselamatan sambil membiarkan regresi sebenarnya lolos lewat jalur tanpa gerbang: tweak prompt senyap, penyetelan pengambilan, kenaikan versi model yang tak dianggap siapa pun sebagai perubahan. Bagi tim besar, bahayanya tumbuh dengan jumlah orang yang dapat menyentuh prompt, karena setiap jalur tanpa gerbang adalah cara mengirim regresi yang tak pernah dilihat dataset mana pun. Bawa daftar jenis perubahan yang saat ini memicu rangkaian offline di integrasi berkelanjutan, yang tidak, dan beberapa insiden terakhir yang ditelusuri ke perubahan tanpa gerbang. Putuskan ambang dan tren apa yang ditegakkan gerbang, karena skor berisik menuntut lantai dan margin regresi alih-alih tuntutan proses sempurna. Dalam pengaturan enterprise dan pemerintah, kaitkan gerbang dengan catatan rilis itu sendiri, agar bukti bahwa perubahan diukur menjadi bagian jejak audit dan bukan tangkapan layar yang diambil seseorang sekali.

5. **Berapa banyak yang kita habiskan untuk evaluasi, dan apakah pengeluaran itu dicocokkan dengan risiko setiap fitur?** Evaluasi tidak gratis: tenaga anotasi, komputasi yang dibakar juri otomatis pada setiap proses, dan kerja tetap menjaga dataset emas tetap representatif semuanya berbiaya uang nyata, dan tim yang tak pernah menamai biaya itu cenderung entah kurang berinvestasi pada fitur berisiko tinggi atau menyepuh emas fitur sekali pakai. Tarikan yang bersaing ada antara fidelitas dan anggaran, karena metode paling tepercaya, tinjauan pakar manusia, juga paling tidak berskala, sehingga Anda tak mampu membayarnya di mana-mana dan harus memutuskan di mana ia layak harganya. Bawa biaya saat ini per proses evaluasi, jam anotasi per fitur, dan tingkat risiko jujur untuk setiap sistem agar ruangan dapat melihat ke mana uang pergi versus di mana bahaya tinggal. Bagi enterprise, ini argumen terkuat untuk platform evaluasi bersama yang mengamortisasi anotasi dan komputasi di banyak tim; bagi lembaga pemerintah, tingkat risiko harus dipetakan langsung ke kedalaman bukti yang kelak akan dituntut badan pengawas.

6. **Ketika model lebih baik tiba, secepat apa kita dapat membuktikan apakah ia membantu, dan siapa yang diizinkan membuat peralihan?** Nilai rangkaian evaluasi terwujud paling tajam pada hari model lebih kuat dirilis, karena tim yang dapat menjalankan dataset emas dan rangkaian red-team terhadap model baru dalam satu sore dapat mengadopsi perbaikan yang akan terlewat berbulan-bulan oleh tim yang menilai dengan tangan. Ketegangannya antara kecepatan dan kehati-hatian: Anda ingin bergerak pada hari model lebih baik muncul, dan Anda tak dapat membiarkan pertukaran diam-diam menurunkan kategori jawaban yang disembunyikan skor rata-rata Anda. Bawa waktu yang saat ini diperlukan untuk menjalankan perbandingan offline penuh terhadap penyedia baru, apakah himpunan eval Anda portabel antarmodel, dan segmen di mana regresi paling berarti. Dalam pengaturan teregulasi dan publik, namai siapa yang memegang wewenang menyetujui perubahan model dan bukti terdokumentasi apa yang mereka butuhkan, karena pertukaran tak terdokumentasi atas model di balik keputusan yang menghadap warga adalah persis jenis perubahan yang akan diminta auditor untuk Anda benarkan.

## Lensa sektor

**Startup.** Bangun eval jujur terkecil yang Anda bisa dan biarkan tumbuh bersama produk. Spreadsheet berisi dua puluh hingga empat puluh kasus nyata, masing-masing dengan jawaban diharapkan yang telah diperiksa, dijalankan oleh skrip sebelum setiap merge, mengalahkan tolok ukur publik mana pun untuk niche Anda dan nyaris tak berbiaya. Lewati platform bersama dan LLM-as-a-judge sampai penilaian manual benar-benar menyakitkan, tetapi masukkan setiap kegagalan yang dilaporkan pengguna kembali ke himpunan sejak hari pertama, karena refleks itulah yang mencegah rasa malu yang sama dua kali.

**Bisnis kecil.** Anda mungkin tidak punya spesialis evaluasi dan membeli AI Anda tertanam dalam perkakas, jadi tugas Anda adalah menuntut bukti alih-alih membangunnya. Tanyakan kepada setiap vendor bagaimana mereka mengukur kualitas, apakah mereka menguji pada data yang menyerupai milik Anda, dan bagaimana Anda akan menyadari regresi setelah pembaruan yang tidak Anda pilih. Simpan himpunan kecil privat berisi kasus nyata Anda sendiri untuk memeriksa perkakas itu sendiri secara acak, karena jawaban otomatis salah yang mencapai pelanggan merugikan Anda jauh lebih banyak daripada menit yang dibutuhkan pemeriksaan itu.

**Enterprise.** Hadiahnya adalah platform evaluasi bersama agar belasan tim tidak masing-masing menciptakan ulang penilaian: penyimpanan bersama untuk dataset emas, rangkaian offline yang digerbangi di integrasi berkelanjutan, prompt juri LLM terdaftar beserta skor kalibrasinya, dan metrik online per fitur. Lapiskan tata kelola di atasnya dengan tingkat risiko yang menetapkan batas yang dibutuhkan dan persetujuan sebelum rilis, agar fitur berisiko tinggi melewati gerbang lebih tinggi daripada bantuan internal. Platform mengamortisasi anotasi dan komputasi antartim, yang merupakan alasan terkuat untuk membangunnya alih-alih membiarkan setiap kelompok berimprovisasi.

**Pemerintah.** Evaluasi harus dapat diaudit, bukan sekadar dilakukan, jadi arsipkan versi dataset, metrik, nama peninjau, dan persetujuan sebagai bukti akuntabilitas untuk setiap rilis. Rangkaian red-team harus membuktikan sistem menolak menciptakan kebijakan atau menyatakan hukum yang tidak ada dalam sumbernya, dan pengadaan harus mewajibkan vendor mengungkap bagaimana mereka mengevaluasi model dan memberi portabilitas data eval Anda. Ketika badan pengawas bertanya bagaimana Anda tahu perkakas itu aman, jawabannya harus catatan bertanggal, bukan jaminan.

## Contoh

**Startup.** Perusahaan beranggota empat orang yang membangun asisten tinjauan kontrak AI memulai dengan spreadsheet berisi empat puluh klausul nyata, masing-masing diberi label oleh pengacara internal mereka dengan risiko yang seharusnya ditandai. Setiap perubahan prompt dijalankan terhadap himpunan itu dalam skrip sebelum merge, dan skor dicetak di pull request. Ketika pengguna menandai klausul yang terlewat, ia langsung masuk ke spreadsheet, sehingga himpunan tumbuh bersama produk. Seiring volume naik mereka menambah LLM-as-a-judge untuk menilai kualitas penjelasan, tetapi hanya setelah memeriksa bahwa ia sepakat dengan pengacara pada sampel. Murah, privat, dan jujur mengalahkan tolok ukur publik mana pun untuk niche mereka.

**Enterprise.** Sebuah bank besar menjalankan belasan fitur AI di dukungan, pencarian, dan perkakas internal, dan setiap tim menilai berbeda. Mereka membangun platform evaluasi bersama: tempat umum untuk menyimpan dataset emas, menjalankan rangkaian offline di CI, mendaftarkan prompt juri LLM dengan skor kalibrasinya, dan melacak metrik online per fitur. Tata kelola berada di atasnya, dengan tingkat risiko yang menetapkan batas yang dibutuhkan dan persetujuan yang diperlukan sebelum rilis. Fitur penjelasan penipuan baru tidak dapat dikirim sampai himpunan eval-nya ditinjau, rangkaian red-team-nya lulus, dan pemilik akuntabelnya menandatangani hasilnya. Memakai ulang platform berarti tim memperdebatkan ranah mereka, bukan cara mengukur.

**Pemerintah.** Sebuah lembaga kesehatan publik men-deploy asisten untuk membantu staf menjawab pertanyaan tunjangan dari panduan yang disetujui. Karena jawaban salah dapat memengaruhi kelayakan seseorang, evaluasi harus dapat diaudit. Setiap rilis menjalankan himpunan eval terdokumentasi yang mencakup pertanyaan umum, kasus tepi, dan prompt adversarial, dan hasilnya, versi dataset, metrik, dan nama peninjau diarsipkan sebagai bukti akuntabilitas. Rangkaian red-team memeriksa bahwa sistem menolak menciptakan kebijakan atau menyatakan hukum yang tidak ada dalam sumbernya. Ketika badan pengawas bertanya bagaimana lembaga tahu perkakas itu aman, jawabannya adalah catatan bertanggal, bukan jaminan.

## Kasus bisnis: motivasi, ROI, dan TCO

Evaluasi terbayar dengan membuat setiap investasi AI lain lebih aman dan cepat. Imbal hasil investasinya (ROI) tampak sebagai insiden produksi lebih sedikit, iterasi lebih cepat karena tim dapat mengubah prompt dan model dengan percaya diri, dan kemampuan mengadopsi model lebih baik pada hari mereka tiba karena Anda dapat membuktikan apakah mereka membantu. Cara paling jelas menilainya adalah biaya ketiadaannya: satu halusinasi publik, keluaran bias, atau kebocoran data dapat berbiaya jauh lebih besar dalam remediasi, hilangnya kepercayaan, dan paparan regulasi daripada bertahun-tahun infrastruktur evaluasi. Ia adalah beda antara menemukan regresi di CI secara gratis dan menemukannya di surat kabar.

Total biaya kepemilikan (TCO) nyata dan layak dinamai. Anda membayar tenaga anotasi, komputasi yang dikonsumsi juri otomatis, dan kerja berkelanjutan menjaga himpunan eval tetap representatif seiring pemakaian bergeser. Pada skala enterprise, platform bersama mengamortisasi sebagian besar ini di banyak tim, yang merupakan argumen terkuat untuk membangunnya alih-alih membiarkan setiap kelompok berimprovisasi. Ajukan kasus kepada pimpinan dengan memasangkan risiko konkret (biaya satu jawaban publik buruk di ranah Anda) dengan kemampuan konkret (kecepatan mengadopsi setiap model baru dengan aman), dan dengan membingkai evaluasi sebagai kontrol yang memungkinkan organisasi bergerak cepat tanpa bergerak sembrono.

## Anti-pola dan jebakan

- **Pengiriman berbasis firasat.** Menilai perubahan AI dengan mencoba beberapa prompt secara manual, tanpa dataset dan tanpa skor yang dapat diulang.
- **Teater tolok ukur.** Memercayai skor tolok ukur publik yang kuat sebagai bukti sistem cocok dengan tugas Anda, mengabaikan kontaminasi dan ketidakcocokan distribusi.
- **Overfitting pada himpunan eval.** Menyetel prompt terhadap himpunan tetap yang sama sampai angkanya tinggi dan tak bermakna, tanpa holdout segar.
- **Juri tak terkalibrasi.** Men-deploy LLM-as-a-judge dan memercayai skornya tanpa pernah memeriksa kesepakatan dengan penilai manusia.
- **Pemujaan metrik.** Mengoptimalkan BLEU atau ROUGE seolah itu kualitas, dan mengirim jawaban lebih buruk yang kebetulan tumpang tindih dengan teks referensi.
- **Red teaming sekali jalan.** Menyerang sistem sekali sebelum peluncuran dan tak pernah mengubah temuan menjadi uji regresi permanen.
- **Keyakinan hanya-offline.** Percaya skor offline baik berarti fitur berfungsi, tanpa pengukuran online atas hasil nyata.
- **Himpunan eval yatim.** Dataset yang tak dimiliki siapa pun, tak pernah menyerap kegagalan produksi, dan perlahan berhenti mencerminkan kenyataan.

## Model kematangan

- **Tingkat 1, Memulai:** Perubahan AI dinilai dengan tangan pada beberapa contoh, secara reaktif, ketika seseorang kebetulan khawatir. Tidak ada dataset, skor yang dapat diulang, dan gerbang. Regresi ditemukan oleh pengguna, dan tak ada yang dapat mengatakan apakah sistem lebih baik atau lebih buruk daripada bulan lalu.
- **Tingkat 2, Mengembangkan:** Sebagian tim menyimpan dataset emas kecil dan menjalankannya secara manual sebelum perubahan besar, dan beberapa skor klasik atau berbasis referensi ada. Tinjauan manusia terjadi untuk fitur penting, tetapi penilaian tidak konsisten antartim, evaluasi tidak otomatis atau digerbangi, dan setiap kelompok melakukannya berbeda.
- **Tingkat 3, Membakukan:** Rangkaian offline berjalan di integrasi berkelanjutan pada setiap perubahan prompt, model, atau pengambilan dan menggerbangi merge, mengikuti satu praktik terdokumentasi di seluruh organisasi. LLM-as-a-judge dikalibrasi terhadap label manusia, red teaming adalah rangkaian yang dapat diulang, dan dataset dimiliki, diversikan, dan diberi makan kegagalan produksi, dengan kontaminasi dijaga secara aktif.
- **Tingkat 4, Mengelola:** Evaluasi diukur dan dikendalikan dengan data terhadap garis dasar. Tingkat kesepakatan juri-ke-manusia, tingkat lolos red-team, skor per segmen, keberhasilan tugas online, dan drift dilacak seiring waktu, dan merge digerbangi pada ambang dan margin regresi alih-alih satu proses sempurna. Biaya anotasi dan komputasi per proses dianggarkan per fitur, kalibrasi ulang terjadi sesuai jadwal, dan setiap hasil membawa pemilik akuntabel dan persetujuan.
- **Tingkat 5, Mengorkestrasi:** Platform evaluasi bersama melayani seluruh organisasi, dan evaluasi offline dan online membentuk loop berkelanjutan yang terikat pada hasil bisnis. Model baru dibuktikan terhadap himpunan eval portabel pada hari mereka tiba, portofolio beradaptasi seiring pemakaian dan risiko bergeser, bukti evaluasi dapat diaudit oleh regulator dan badan pengawas, dan pelajaran dari kegagalan satu tim mengalir ke dataset setiap tim.

## Gagasan untuk didiskusikan

1. Bagaimana Anda memutuskan kapan skor offline cukup kuat untuk membenarkan eksperimen online, dan kapan tidak?
2. Berapa rasio tepat evaluasi manusia terhadap penilaian otomatis untuk profil risiko Anda, dan seberapa sering Anda harus meninjau ulang?
3. Ketika tolok ukur publik dan himpunan eval privat Anda tidak sepakat tentang model mana yang lebih baik, mana yang Anda percaya dan mengapa?
4. Bagaimana Anda menjaga himpunan eval tetap representatif seiring perilaku pengguna bergeser, tanpa membiarkannya menggelembung menjadi terlalu lambat untuk dijalankan di CI?
5. Apa yang termasuk dalam rangkaian red-team untuk ranah Anda, dan siapa yang berkualifikasi merancang serangannya?
6. Bagaimana Anda mengevaluasi trajektori agen, bukan hanya jawaban akhirnya, tanpa tenggelam dalam biaya menilai setiap langkah?

## Poin-poin utama

- Evaluasi AI berbeda dari pengujian perangkat lunak karena keluaran non-deterministik dan jarang ada satu jawaban benar, sehingga Anda mengukur kualitas di kasus representatif alih-alih menegaskan nilai eksak.
- Praktikkan pengembangan berbasis eval: definisikan kualitas terukur lebih dulu, lalu bangun ke arahnya, dan masukkan setiap kegagalan produksi kembali ke himpunan.
- Lapisi metode menurut kecepatan dan fidelitas: penilaian otomatis murah untuk iterasi konstan, penilaian manusia sebagai jangkar, dan kalibrasi untuk menjaga keduanya selaras.
- Jaga dari kontaminasi dan overfitting, atau angka Anda akan menyanjung sementara sistem nyata mengecewakan pengguna.
- Sambungkan evaluasi offline ke CI sebagai gerbang dan terus ukur kualitas dan drift di produksi, karena model yang baik saat peluncuran dapat meluruh.

## Referensi dan bacaan lanjutan

- Chip Huyen, *AI Engineering: Building Applications with Foundation Models*.
- Lianmin Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*.
- Kishore Papineni et al., *BLEU: A Method for Automatic Evaluation of Machine Translation*.
- Chin-Yew Lin, *ROUGE: A Package for Automatic Evaluation of Summaries*.
- Percy Liang et al., *Holistic Evaluation of Language Models (HELM)*.
- Deep Ganguli et al., *Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviours, and Lessons Learned*.
- OWASP Foundation, *OWASP Top 10 for Large Language Model Applications*.
- National Institute of Standards and Technology, *AI Risk Management Framework*.
