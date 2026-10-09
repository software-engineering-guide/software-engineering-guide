# 6.5 AI yang bertanggung jawab dan tepercaya

## Tinjauan dan motivasi

AI yang bertanggung jawab dan tepercaya adalah praktik membangun dan mengoperasikan sistem AI yang adil, transparan, akuntabel, aman, dan menghormati privasi. Itu juga berarti mampu menunjukkan semua ini kepada orang yang terdampak dan kepada regulator. Ketika AI mengambil keputusan yang membentuk kehidupan orang (perekrutan, pinjaman, kelayakan tunjangan), pertanyaannya bukan lagi sekadar "apakah ini berfungsi?" melainkan "apakah ini benar, dan dapatkah kita membenarkannya?" Sistem yang akurat secara rata-rata masih dapat tidak adil terhadap subkelompok, tak dapat dijelaskan kepada orang yang dipengaruhinya, atau tidak aman ketika disalahgunakan. Anda memperoleh kepercayaan dengan menangani dimensi-dimensi ini secara sengaja, bukan dengan berharap semuanya mengurus diri sendiri.

Bagi tim besar, AI yang bertanggung jawab tidak boleh menjadi pekerjaan satu orang atau kotak centang di akhir. Anyamkan ke dalam cara Anda mendesain, mengevaluasi, men-deploy, dan mengatur sistem, dengan kepemilikan dan eskalasi jelas. Pada skala besar, bias kecil dan celah pengawasan memengaruhi banyak orang. Satu kegagalan berprofil tinggi dapat merusak reputasi Anda dan mengundang regulasi. Kerangka tata kelola ada justru karena niat baik ad hoc tidak berskala.

Organisasi pemerintah dan teregulasi menghadapi kewajiban mengikat. Hukum yang muncul, seperti [EU AI Act](https://en.wikipedia.org/wiki/Artificial_Intelligence_Act), memaksakan persyaratan bertingkat menurut risiko. Standar seperti NIST AI Risk Management Framework dan ISO/IEC 42001 memberi Anda cara terstruktur untuk memenuhinya. Badan publik harus menghindari diskriminasi melanggar hukum, menyediakan jalur untuk menggugat keputusan otomatis, dan transparan tentang bagaimana AI dipakai dalam menjalankan kewenangan publik. AI yang bertanggung jawab dalam pengaturan ini adalah kewajiban etis sekaligus keharusan hukum.

*Lihat juga:* bab 6.1 (strategi dan kesiapan AI), bab 10.5 (etika, akuntabilitas, dan kepentingan publik), dan bab 4.5 (privasi dan pelindungan data).

## Prinsip utama

- Keadilan adalah tujuan desain untuk diukur dan dikelola, bukan diasumsikan.
- Orang yang terdampak keputusan AI berhak atas penjelasan dan jalur untuk menggugatnya.
- Akuntabilitas berada pada manusia dan organisasi, tidak pernah pada model.
- Privasi dan keselamatan harus direkayasa masuk, termasuk pelindungan terhadap penyalahgunaan dan pelecehan.
- Tata kelola harus mengikuti kerangka yang diakui agar dapat dipertahankan dan diaudit.
- Pengawasan manusia harus bermakna, dengan wewenang nyata untuk mengesampingkan dan menghentikan.
- Pertimbangkan biaya AI yang lebih luas, termasuk jejak lingkungannya.

## Rekomendasi

### Deteksi dan mitigasi bias serta ketidakadilan

Definisikan apa arti keadilan untuk konteks Anda. Ada beberapa definisi matematis, kadang saling bertentangan, dan yang tepat bergantung pada keputusan dan hukum. Uji model untuk kinerja yang berbeda di berbagai kelompok yang dilindungi dan rentan memakai data representatif. Lakukan ini sebelum deployment dan terus lakukan sesudahnya, karena [bias](https://en.wikipedia.org/wiki/Algorithmic_bias) dapat muncul seiring populasi bergeser. Mitigasi lewat data lebih baik, pembobotan ulang, kendala, atau mengubah cara sistem dipakai, dan dokumentasikan trade-off yang Anda terima. Menghapus atribut yang dilindungi tidak menghapus bias, karena proksi tetap ada. Perlakukan keadilan sebagai disiplin pengukuran dan pengelolaan berkelanjutan, bukan izin sekali jalan.

### Sediakan keterjelasan, interpretabilitas, dan transparansi

Sesuaikan tingkat penjelasan dengan taruhan dan audiens. Untuk keputusan berdampak, beri orang yang terdampak alasan bahasa sederhana yang jelas yang dapat mereka pahami dan tindak lanjuti. Untuk tata kelola internal, pertahankan [interpretabilitas](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence) teknis yang cukup untuk men-debug dan membela sistem. Pilih model yang secara inheren dapat diinterpretasi di mana taruhannya tinggi dan interpretabilitas dapat dicapai. Di mana model kompleks diperlukan, pakai teknik penjelasan sambil jujur tentang batasnya. Bersikap transparan tentang kapan AI dipakai sama sekali, terutama dalam interaksi dengan publik.

### Atur dengan kerangka yang diakui

Adopsi pendekatan tata kelola terstruktur alih-alih menciptakan sendiri. **NIST AI Risk Management Framework** mengorganisasi kerja seputar mengatur, memetakan, mengukur, dan mengelola risiko AI. **EU AI Act** mengklasifikasi sistem menurut risiko dan memaksakan kewajiban sesuai, dengan persyaratan ketat untuk penggunaan berisiko tinggi. **ISO/IEC 42001** mendefinisikan sistem manajemen AI yang dapat diaudit dan disertifikasi. Petakan sistem Anda ke kerangka-kerangka ini. Pelihara dokumentasi seperti kartu model dan kartu data (ringkasan terstandar tentang tujuan, kinerja, dan keterbatasan model atau dataset). Jalankan penilaian risiko sebelum deployment, dan simpan inventaris sistem AI beserta tingkat risiko dan pemiliknya. Tata kelola yang baik menetapkan peran jelas, hak keputusan, dan jalur eskalasi.

### Pastikan pengawasan manusia, akuntabilitas, dan banding

Jaga manusia secara bermakna mengendalikan keputusan berdampak, dengan wewenang sejati dan informasi yang dibutuhkan untuk mengesampingkan sistem, bukan stempel karet. Tetapkan akuntabilitas jelas: namai pemilik yang bertanggung jawab atas perilaku setiap sistem. Beri orang yang terdampak keputusan otomatis hak atas penjelasan dan proses banding yang dapat dijalankan kepada manusia yang dapat mengubah hasilnya. Catat keputusan dan dasarnya, agar Anda dapat menangani banding dan audit dengan adil dan cepat.

### Lindungi privasi, keselamatan, dan dari penyalahgunaan

Minimalkan data pribadi yang Anda kumpulkan dan pakai, tetapkan dasar hukum, dan terapkan teknik privasi yang sesuai kepekaan yang terlibat. [Red-team](https://en.wikipedia.org/wiki/Red_team) sistem sebelum dan sesudah deployment untuk menemukan cara mereka dapat dimanipulasi, di-jailbreak, atau disalahgunakan untuk menyebabkan kerugian, dan perbaiki yang Anda temukan. Bangun pengaman terhadap menghasilkan konten berbahaya, membocorkan data sensitif, atau memungkinkan pelecehan. Rencanakan insiden: pemantauan, respons, dan pengungkapan. Pertimbangkan [dwiguna](https://en.wikipedia.org/wiki/Dual-use_technology) (kemampuan sama yang melayani tujuan bermanfaat sekaligus berbahaya) dan penyalahgunaan hilir, bukan hanya penggunaan yang dimaksudkan.

### Perhitungkan biaya lingkungan

Melatih dan menyajikan model besar mengonsumsi energi dan air yang signifikan. Ukur dan laporkan jejak beban kerja AI utama. Pilih model dan perangkat keras efisien di mana memenuhi kebutuhan. Sesuaikan ukuran model dengan tugas alih-alih menjadikan yang terbesar sebagai bawaan, dan masukkan biaya lingkungan ke keputusan arsitektur dan pengadaan.

## Trade-off: kelebihan dan kekurangan

| Ketegangan | Satu sisi | Sisi lain |
|---|---|---|
| Akurasi vs keadilan | Akurasi rata-rata tertinggi | Hasil adil di semua kelompok |
| Kinerja vs interpretabilitas | Model kompleks dan kuat | Model yang dapat dijelaskan dan dipertahankan |
| Otomasi vs pengawasan | Efisiensi dan skala | Kendali manusia dan akuntabilitas |
| Utilitas data vs privasi | Model lebih kaya dari lebih banyak data | Minimisasi dan pelindungan data |
| Kemampuan vs keselamatan | Fungsi luas dan terbuka | Perilaku terbatas dan terjaga |
| Kecepatan vs tata kelola | Deployment cepat | Tinjauan dan dokumentasi menyeluruh |

Jarang ada makan siang gratis. Meningkatkan keadilan dapat mengorbankan sedikit akurasi. Interpretabilitas dapat mengorbankan sedikit kinerja. Tata kelola memakan waktu. Jalur yang bertanggung jawab adalah membuat trade-off ini dengan sadar, mendokumentasikannya, dan memilih berpihak pada orang yang terdampak serta kemampuan dipertahankan ketika taruhannya tinggi. Membingkai tata kelola sebagai rem inovasi adalah dikotomi palsu. Risiko AI yang tak dikelola sendiri adalah ancaman bagi inovasi berkelanjutan.

## Pertanyaan untuk didiskusikan dengan tim Anda

1. **Sistem AI kita yang ter-deploy mana yang akan diklasifikasikan EU AI Act sebagai berisiko tinggi, dan apakah kita memenuhi kewajiban itu hari ini?** Hukum bertingkat-risiko kini mengikat, bukan hipotetis, dan sistem yang memutuskan perekrutan, pinjaman, atau kelayakan tunjangan dapat memikul persyaratan ketat yang mungkin sudah Anda langgar. Bagi organisasi besar, pertanyaan ini memaksa inventaris jujur alih-alih asumsi nyaman bahwa tata kelola "sudah ditangani." Bawa daftar sistem AI Anda dengan tingkat risiko dan pemiliknya, dipetakan terhadap EU AI Act, NIST AI Risk Management Framework, dan ISO/IEC 42001 di mana relevan. Sinyal yang diawasi adalah sistem berdampak apa pun tanpa klasifikasi risiko, tanpa penilaian dampak, dan tanpa kartu model atau data. Bagi badan publik yang menjalankan kewenangan publik, kewajiban yang terlewat bukan butir tunggakan, melainkan paparan hukum, dan jawabannya harus memicu penilaian dan dokumentasi yang dibutuhkan sistem-sistem itu.

2. **Ketika salah satu model kita menolak seseorang, dapatkah orang itu memperoleh alasan bahasa sederhana dan menjangkau manusia yang benar-benar dapat membalikkan hasilnya?** Hak atas penjelasan dan banding yang dapat dijalankan memisahkan AI akuntabel dari kotak hitam yang merugikan orang tanpa jalan pemulihan. Keadilan yang diukur rata-rata masih dapat mengecewakan individu, dan interpretabilitas yang dipilih setelah deployment biasanya sandiwara. Bawa satu keputusan ter-deploy yang spesifik dan telusuri: alasan yang diterima orang terdampak, saluran banding, dan apakah manusia di ujung sana punya wewenang sejati dan dasar tercatat untuk mengesampingkan. Dalam pengaturan pemerintah dan teregulasi, jalur banding sering persyaratan hukum, bukan kesopanan. Jika alasannya tak terpahami atau banding berujung stempel karet, itulah celah yang harus diperbaiki sebelum rilis berikutnya.

3. **Siapa satu orang bernama yang akuntabel ketika model menyebabkan kerugian, dan apakah mereka punya wewenang nyata untuk menghentikannya?** Akuntabilitas berada pada manusia dan organisasi, tidak pernah pada model, tetapi prinsip itu kosong sampai nama dilekatkan pada setiap sistem dan orang itu benar-benar dapat mencabut steker. Bagi tim besar, kepemilikan yang menyebar berarti ketika kegagalan keadilan atau jailbreak muncul, semua orang mengira orang lain yang mengawasi. Bawa peta kepemilikan, jalur eskalasi, dan bukti bahwa pengawasan bermakna: apakah pemilik bernama mendapat informasi dan kuasa untuk mengesampingkan atau menghentikan sistem, atau hanya untuk mengangguk? Diskusikan bagaimana Anda me-red-team untuk penyalahgunaan dan pelecehan yang belum Anda bayangkan, karena menguji hanya penggunaan yang dimaksudkan melewatkan kegagalan yang menjadi berita utama. Jawabannya harus tidak meninggalkan sistem berdampak tanpa pemilik akuntabel yang dapat menghentikannya.

4. **Untuk setiap model berdampak, definisi keadilan mana yang kita pilih, siapa yang menyetujuinya, dan apakah metrik subkelompok kita benar-benar bertahan di produksi?** Keadilan punya beberapa definisi matematis yang bertentangan satu sama lain, sehingga model yang memenuhi tingkat positif-palsu setara dapat melanggar hasil setara, dan memilih definisi adalah penilaian nilai yang tidak boleh diserahkan kepada siapa pun yang menulis loop pelatihan. Bagi tim besar, bawaan yang tak diperiksa menyembunyikan pilihan di dalam kode dan membuat setiap kelompok hilir mewarisi keputusan yang tak diperdebatkan siapa pun. Bawa metrik keadilan yang Anda optimalkan, kelompok dilindungi dan rentan yang Anda uji, data representatif yang Anda pakai, dan drift yang telah Anda lihat sejak peluncuran, karena menghapus atribut dilindungi menyisakan proksi yang menjaga bias tetap hidup. Dalam pengaturan enterprise dan pemerintah, namai orang dengan wewenang menerima trade-off keadilan dan catat, karena regulator atau ombudsman akan bertanya siapa yang memutuskan bahwa definisi adil ini yang tepat bagi orang yang ditolak pinjaman, tunjangan, atau pekerjaan. Jika tak ada metrik subkelompok yang dipantau setelah deployment, perlakukan model sebagai tidak terukur, bukan adil.

5. **Sesedikit apa data pribadi yang dapat dijalankan setiap sistem, dan sudahkah kita me-red-team untuk penyalahgunaan dan dwiguna yang lebih suka tidak kita pikirkan?** Privasi dan keselamatan harus direkayasa masuk, dan cara termurah mengurangi risiko pelanggaran sekaligus permukaan penyalahgunaan adalah mengumpulkan dan menyimpan lebih sedikit data sejak awal, namun tim rutin menimbun masukan "kalau-kalau berguna nanti." Bagi organisasi besar, setiap bidang tambahan adalah pertanyaan dasar hukum, kewajiban retensi, dan hadiah lebih besar bagi penyerang atau jailbreak. Bawa inventaris data dan dasar hukum untuk setiap sistem, hasil red-teaming untuk manipulasi, kebocoran, dan generasi berbahaya, dan daftar jujur kemampuan dwiguna di mana fitur yang sama yang membantu pengguna sah juga membantu pihak beritikad buruk. Dalam konteks teregulasi dan publik, kaitkan ini dengan rencana insiden Anda: pemantauan, respons, dan pengungkapan, karena badan publik yang membocorkan data sensitif atau mengirim sistem yang dapat di-jailbreak menghadapi kewajiban undang-undang, bukan sekadar rasa malu. Jika red-teaming hanya pernah menguji jalur yang dimaksudkan, Anda telah menguji demo, bukan sistemnya.

6. **Apakah kita mengukur dan memiliki jejak lingkungan beban kerja AI utama kita, atau "pakai model terbesar" adalah bawaan tanpa harga?** Melatih dan menyajikan model besar mengonsumsi energi dan air nyata, dan menjadikan model terbesar sebagai bawaan untuk tugas yang dapat ditangani yang lebih kecil mengubah jalan pintas rekayasa menjadi biaya berulang yang tak pernah dilihat organisasi di dasbor. Bagi tim besar yang menjalankan banyak beban kerja, ketidakefisienan kecil per panggilan bertambah menjadi jejak yang menjadi liabilitas pengadaan dan pelaporan seiring ekspektasi pengungkapan mengetat. Bawa jejak terukur beban kerja terberat Anda, perbandingan ukuran model terhadap akurasi yang benar-benar dibutuhkan tugas, dan pilihan perangkat keras serta penyajian yang dapat Anda sesuaikan ukurannya. Dalam pengaturan enterprise dan pemerintah, hubungkan ini dengan komitmen keberlanjutan dan kriteria pengadaan, karena badan publik makin harus melaporkan dampak lingkungan dan membenarkan pengeluaran, dan jejak yang tak terukur adalah angka yang suatu hari akan diminta dari Anda dan tak dapat Anda sediakan. Putuskan apakah biaya lingkungan masukan formal bagi pemilihan model, atau akui bahwa hari ini bukan.

## Lensa sektor

**Startup.** Anda tidak dapat mengisi staf dewan tata kelola, jadi lakukan versi ringan yang tetap berarti. Pilih model yang dapat diinterpretasi di mana keputusan berdampak, tulis kartu model satu halaman, uji hasil berbeda di kelompok yang dapat Anda ukur, dan catat keputusan agar dapat meninjau ulang keadilan seiring Anda tumbuh. Beri setiap keputusan merugikan alasan sederhana dan jalur ke manusia. Melewatkan ini bukan kecepatan, melainkan liabilitas yang tak sanggup Anda tanggung jika satu keputusan tidak adil mencapai pers atau regulator.

**Bisnis kecil.** Tanpa spesialis khusus, perlakukan AI yang bertanggung jawab sebagai pertanyaan pembelian: pilih vendor yang mendokumentasikan pengujian keadilan, mengekspos kartu model dan data, dan membiarkan Anda mengungkapkan kepada pelanggan ketika AI dipakai. Ketahui data pribadi apa yang dikumpulkan perkakas Anda dan apakah Anda punya dasar hukum memakainya. Di mana jawaban otomatis yang salah dapat merugikan pelanggan, jaga orang dalam lingkaran alih-alih memercayai perkakas yang tak dapat Anda periksa atau jelaskan.

**Enterprise.** Tugasnya tata kelola pada skala besar lintas banyak tim: petakan setiap sistem ke NIST AI Risk Management Framework, EU AI Act, dan ISO/IEC 42001, simpan inventaris dengan tingkat risiko dan pemilik bernama, dan wajibkan pengujian keadilan, keselamatan, dan privasi sebelum dan sesudah peluncuran. Bakukan kartu model dan data, red-teaming, dan proses banding agar kelompok berhenti menciptakan ulang. Anggarkan biaya tata kelola, pengawasan, dan interpretabilitas secara eksplisit, dan perlakukan risiko AI yang tak dikelola sebagai ancaman bagi izin beroperasi.

**Pemerintah.** Aturan pengadaan, transparansi, dan akuntabilitas publik membentuk setiap pilihan. Terbitkan pemberitahuan transparansi bahasa sederhana, jalankan penilaian dampak sebelum deployment, dan jaga pengambilan keputusan manusia yang bermakna untuk tindakan apa pun yang memengaruhi warga, dengan jalur banding yang dapat dijalankan. Tuntut vendor mengungkap keterbatasan model dan memberi portabilitas data, hindari diskriminasi melanggar hukum, namai pejabat akuntabel untuk setiap sistem, dan laporkan jejak lingkungan beban kerja utama.

## Contoh

**Startup.** Startup pinjaman kecil yang membangun fitur penilaian kredit awal tidak dapat mengisi staf dewan tata kelola, jadi ia melakukan versi ringan yang tetap berarti. Dua pendiri menyetujui model bersama-sama, mengujinya untuk hasil berbeda di kelompok yang dapat mereka ukur, dan menulis kartu model satu halaman singkat yang mencakup data, batas, dan risiko yang diketahui. Mereka memilih model yang lebih sederhana dan dapat diinterpretasi agar dapat memberi setiap pemohon yang ditolak alasan sederhana dan jalur ke tinjauan manusia, dan mereka mencatat keputusan agar dapat meninjau ulang keadilan seiring tumbuh.

**Enterprise.** Sebuah bank yang men-deploy model kredit membentuk dewan tata kelola AI, memetakan model ke kategori berisiko tinggi, dan mewajibkan pengujian keadilan di seluruh kelompok demografis sebelum dan sesudah peluncuran. Ia mendokumentasikan model dalam kartu model. Ia memberi pemohon yang ditolak alasan bahasa sederhana dan banding ke penjamin emisi manusia, dan me-red-team sistem untuk manipulasi. Ia memilih model yang sedikit kurang akurat tetapi lebih dapat diinterpretasi, karena harus menjelaskan dan membela setiap keputusan kepada regulator.

**Pemerintah.** Sebuah lembaga publik yang memakai AI untuk membantu mengalokasikan sumber daya inspeksi menyelaraskan programnya dengan NIST AI RMF dan ketentuan relevan hukum AI yang berlaku. Ia menerbitkan pemberitahuan transparansi yang menjelaskan cara kerja sistem dan pengamannya. Ia melakukan penilaian dampak sebelum deployment, menjaga pengambilan keputusan manusia yang bermakna untuk tindakan apa pun yang memengaruhi warga, dan menyediakan proses banding. Keadilan dipantau terus-menerus, biaya lingkungan beban kerja dilaporkan, dan pejabat akuntabel dinamai sebagai yang bertanggung jawab atas sistem.

## Kasus bisnis: motivasi, ROI, dan TCO

AI yang bertanggung jawab melindungi nilai sebanyak ia menciptakannya. ROI sebagian besar adalah biaya yang dihindari: klaim diskriminasi, penalti regulasi, dan bencana reputasi yang lebih sedikit; audit lebih mulus; dan kepercayaan pengguna dan publik lebih besar, yang mendorong adopsi. Sistem tepercaya juga lebih kokoh, karena disiplin yang menghasilkan keadilan dan keselamatan juga menghasilkan rekayasa lebih baik.

TCO mencakup staf tata kelola, pengujian keadilan dan keselamatan, dokumentasi, red-teaming, proses pengawasan, dan kinerja yang kadang dikorbankan demi interpretabilitas atau keadilan. Timbang ini terhadap biaya tidak berinvestasi: liabilitas hukum, penutupan paksa, hilangnya kepercayaan publik, dan biaya jauh lebih tinggi memasang tata kelola setelah kegagalan. Dalam konteks teregulasi, investasi AI yang bertanggung jawab makin tak dapat ditawar. Ajukan kasus kepada pimpinan dengan membingkainya sebagai manajemen risiko dan izin beroperasi: prasyarat untuk men-deploy AI pada skala besar sama sekali.

## Anti-pola dan jebakan

- **Keadilan lewat pengabaian.** Mengasumsikan model adil karena mengabaikan atribut yang dilindungi.
- **Sandiwara keterjelasan.** Menghasilkan penjelasan yang tidak benar-benar mencerminkan bagaimana keputusan dibuat.
- **Pengawasan stempel karet.** Tinjauan manusia nominal tanpa wewenang atau informasi nyata untuk mengesampingkan.
- **Tata kelola sebagai renungan belakangan.** Menempelkan dokumentasi dan tinjauan setelah desain dan deployment.
- **Tanpa jalur banding.** Meninggalkan orang terdampak tanpa cara menggugat keputusan otomatis.
- **Mengabaikan penyalahgunaan.** Menguji hanya penggunaan yang dimaksudkan dan melewatkan jailbreak dan pelecehan.
- **Buta jejak.** Menjadikan model terbesar sebagai bawaan tanpa mempertimbangkan biaya lingkungan.

## Model kematangan

1. **Memulai.** Tanpa pengujian keadilan, penjelasan, atau tata kelola; tanggung jawab tak terdefinisi; masalah bias, penyalahgunaan, dan privasi muncul hanya setelah kerugian, dan tak ada inventaris sistem AI atau risikonya.
2. **Mengembangkan.** Sebagian pengujian bias, kartu model, dan red-teaming terjadi pada sistem individual, tetapi praktik tidak konsisten antartim; pengawasan ad hoc; kerangka seperti NIST AI Risk Management Framework dan EU AI Act dikenal tetapi hanya sebagian diadopsi.
3. **Membakukan.** Tata kelola didokumentasikan dan ditegakkan di seluruh organisasi: sistem dipetakan ke kerangka yang diakui dan ISO/IEC 42001, masing-masing punya tingkat risiko dan pemilik bernama, dan pengujian keadilan, keselamatan, dan privasi, kartu model dan data, jalur banding, dan red-teaming untuk sistem berisiko tinggi diwajibkan alih-alih opsional.
4. **Mengelola.** Program diukur dan dikendalikan dengan data: metrik keadilan subkelompok, temuan keselamatan dan jailbreak, volume banding dan tingkat pembalikan, tingkat pengesampingan pengawasan, dan jejak beban kerja dilacak terhadap garis dasar dan ambang; drift dan hasil berbeda memicu tindakan terdefinisi; keputusan go atau no-go bertumpu pada bukti alih-alih jaminan.
5. **Mengorkestrasi.** AI yang bertanggung jawab terus diperbaiki dan terintegrasi di seluruh organisasi: pemantauan keadilan, keselamatan, dan penyalahgunaan berjalan di produksi, tata kelola dibangun ke dalam pengiriman, biaya lingkungan adalah masukan formal bagi pemilihan model, dan organisasi menyesuaikan kontrolnya seiring hukum, risiko, dan kemampuan bergeser, dengan tanggung jawab dimiliki semua orang alih-alih satu tim.

## Gagasan untuk didiskusikan

- Definisi keadilan mana yang berlaku untuk keputusan tertentu, dan siapa yang memutuskan?
- Berapa banyak akurasi atau kinerja yang dapat diterima untuk dikorbankan demi keadilan atau interpretabilitas?
- Apa yang membuat pengawasan manusia bermakna alih-alih stempel karet?
- Bagaimana banding terhadap keputusan otomatis harus dirancang agar adil dan tepat waktu?
- Bagaimana Anda me-red-team untuk penyalahgunaan yang belum Anda bayangkan?
- Haruskah biaya lingkungan memengaruhi pemilihan model, dan bagaimana Anda menimbangnya?

## Poin-poin utama

- AI tepercaya adil, dapat dijelaskan, akuntabel, aman, dan menghormati privasi, secara desain.
- Keadilan dan keselamatan adalah disiplin pengukuran dan pengelolaan berkelanjutan, bukan pemeriksaan sekali jalan.
- Selaraskan tata kelola dengan NIST AI RMF, EU AI Act, dan ISO/IEC 42001 agar dapat dipertahankan dan diaudit.
- Jaga pengawasan manusia yang bermakna, akuntabilitas jelas, dan hak banding nyata.
- Rekayasa untuk privasi dan terhadap penyalahgunaan, dan perhitungkan biaya lingkungan.

## Referensi dan bacaan lanjutan

- National Institute of Standards and Technology, *AI Risk Management Framework (AI RMF 1.0)*.
- European Union, *Artificial Intelligence Act (Regulation on Artificial Intelligence)*.
- ISO/IEC 42001, *Information technology, Artificial intelligence, Management system*.
- Solon Barocas, Moritz Hardt, dan Arvind Narayanan, *Fairness and Machine Learning: Limitations and Opportunities*.
- Christoph Molnar, *Interpretable Machine Learning*.
- Cathy O'Neil, *Weapons of Maths Destruction*.
- Emma Strubell, Ananya Ganesh, dan Andrew McCallum, *Energy and Policy Considerations for Deep Learning in NLP*.
